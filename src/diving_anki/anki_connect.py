from __future__ import annotations

import json
import os
import platform
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

DEFAULT_ANKI_CONNECT_URL = "http://127.0.0.1:8765"
ANKI_CONNECT_ADDON_CODE = "2055492159"


class AnkiConnectError(RuntimeError):
    """Raised when AnkiConnect cannot complete a request."""


def _request(
    action: str,
    *,
    params: dict[str, object] | None = None,
    endpoint: str = DEFAULT_ANKI_CONNECT_URL,
    api_key: str | None = None,
    timeout: float = 30,
) -> Any:
    payload: dict[str, object] = {"action": action, "version": 6}
    if params is not None:
        payload["params"] = params
    if api_key:
        payload["key"] = api_key

    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            result = json.loads(response.read())
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise AnkiConnectError(f"cannot reach AnkiConnect at {endpoint}: {exc}") from exc

    if not isinstance(result, dict) or "error" not in result:
        raise AnkiConnectError(f"unexpected AnkiConnect response for {action!r}")
    if result["error"] is not None:
        raise AnkiConnectError(f"AnkiConnect {action} failed: {result['error']}")
    return result.get("result")


def _launch_anki() -> None:
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(["open", "-a", "Anki"], check=True)
        elif system == "Windows":
            subprocess.Popen(["cmd", "/c", "start", "", "Anki"])
        else:
            subprocess.Popen(["anki"])
    except (OSError, subprocess.CalledProcessError) as exc:
        raise AnkiConnectError(f"could not start Anki Desktop: {exc}") from exc


def _wait_until_ready(
    *,
    endpoint: str,
    api_key: str | None,
    launch: bool,
    startup_timeout: float,
) -> None:
    try:
        _request("version", endpoint=endpoint, api_key=api_key, timeout=2)
        return
    except AnkiConnectError:
        if launch:
            _launch_anki()

    deadline = time.monotonic() + startup_timeout
    while time.monotonic() < deadline:
        try:
            _request("version", endpoint=endpoint, api_key=api_key, timeout=2)
            return
        except AnkiConnectError:
            time.sleep(0.5)

    raise AnkiConnectError(
        f"AnkiConnect did not become available at {endpoint}. "
        f"Install add-on {ANKI_CONNECT_ADDON_CODE}, restart Anki, and try again."
    )


def push_packages(
    packages: list[Path],
    *,
    endpoint: str | None = None,
    api_key: str | None = None,
    launch: bool = True,
    startup_timeout: float = 30,
    card_decks: dict[str, str] | None = None,
    study_settings: dict[str, Any] | None = None,
) -> None:
    """Import packages into Anki Desktop, then synchronize once with AnkiWeb."""
    resolved = [package.resolve() for package in packages]
    missing = [str(package) for package in resolved if not package.is_file()]
    if missing:
        raise AnkiConnectError(f"missing package(s): {', '.join(missing)}")

    endpoint = endpoint or os.environ.get("ANKI_CONNECT_URL", DEFAULT_ANKI_CONNECT_URL)
    api_key = api_key or os.environ.get("ANKI_CONNECT_KEY")
    _wait_until_ready(
        endpoint=endpoint,
        api_key=api_key,
        launch=launch,
        startup_timeout=startup_timeout,
    )

    # Empty legacy filtered decks before an import reuses their names. changeDeck
    # returns cards to ordinary decks without recreating them or their reviews.
    if card_decks is not None:
        for deck in _request("deckNames", endpoint=endpoint, api_key=api_key):
            if deck not in set(card_decks.values()):
                continue
            config = _request(
                "getDeckConfig", params={"deck": deck}, endpoint=endpoint, api_key=api_key
            )
            if config.get("dyn") == 1:
                ids = _request(
                    "findCards",
                    params={"query": f'deck:"{deck}"'},
                    endpoint=endpoint,
                    api_key=api_key,
                )
                if ids:
                    category = deck.split("::")[-1]
                    target = f"Plongée::Collection commune::{category}"
                    _request(
                        "changeDeck",
                        params={"cards": ids, "deck": target},
                        endpoint=endpoint,
                        api_key=api_key,
                    )
                # Empty-deck check guards cardsToo=True in AnkiConnect's API.
                if _request(
                    "findCards",
                    params={"query": f'deck:"{deck}"'},
                    endpoint=endpoint,
                    api_key=api_key,
                ):
                    raise AnkiConnectError(f"refusing to delete nonempty filtered deck: {deck}")
                _request(
                    "deleteDecks",
                    params={"decks": [deck], "cardsToo": True},
                    endpoint=endpoint,
                    api_key=api_key,
                )

    for package in resolved:
        _request(
            "importPackage",
            params={"path": str(package)},
            endpoint=endpoint,
            api_key=api_key,
        )
    if card_decks is not None:
        for card_id, deck in card_decks.items():
            ids = _request(
                "findCards",
                params={"query": f"tag:diving-theory tag:card-id::{card_id}"},
                endpoint=endpoint,
                api_key=api_key,
            )
            if len(ids) != 1:
                raise AnkiConnectError(f"expected one existing card for {card_id}, got {len(ids)}")
            _request(
                "changeDeck",
                params={"cards": ids, "deck": deck},
                endpoint=endpoint,
                api_key=api_key,
            )
    # Retired historical N2 cards keep their suspension/history; return them from
    # the abandoned common branch as well. Leave unrelated personal cards alone.
    if card_decks is not None:
        for deck in sorted(
            _request("deckNames", endpoint=endpoint, api_key=api_key), key=len, reverse=True
        ):
            if not deck.startswith("Plongée::Collection commune::"):
                continue
            ids = _request(
                "findCards",
                params={"query": f'deck:"{deck}" tag:diving-theory'},
                endpoint=endpoint,
                api_key=api_key,
            )
            if ids:
                _request(
                    "changeDeck",
                    params={"cards": ids, "deck": "Plongée::N2::" + deck.split("::")[-1]},
                    endpoint=endpoint,
                    api_key=api_key,
                )
            if not _request(
                "findCards", params={"query": f'deck:"{deck}"'}, endpoint=endpoint, api_key=api_key
            ):
                _request(
                    "deleteDecks",
                    params={"decks": [deck], "cardsToo": True},
                    endpoint=endpoint,
                    api_key=api_key,
                )
        parent = "Plongée::Collection commune"
        if parent in _request("deckNames", endpoint=endpoint, api_key=api_key) and not _request(
            "findCards", params={"query": f'deck:"{parent}"'}, endpoint=endpoint, api_key=api_key
        ):
            _request(
                "deleteDecks",
                params={"decks": [parent], "cardsToo": True},
                endpoint=endpoint,
                api_key=api_key,
            )

    if study_settings is not None:
        # Use an isolated preset: never change the user's Default preset or other decks.
        names = [
            d
            for d in _request("deckNames", endpoint=endpoint, api_key=api_key)
            if d == "Plongée" or d.startswith("Plongée::")
        ]
        config = _request(
            "getDeckConfig",
            params={"deck": "Plongée::N2"},
            endpoint=endpoint,
            api_key=api_key,
        )
        if config["name"] != study_settings["preset_name"]:
            preset_id = _request(
                "cloneDeckConfigId",
                params={"name": study_settings["preset_name"], "cloneFrom": str(config["id"])},
                endpoint=endpoint,
                api_key=api_key,
            )
            config["id"] = preset_id
        config["name"] = study_settings["preset_name"]
        config["new"]["perDay"] = study_settings["new_cards_per_day"]
        config["rev"]["perDay"] = study_settings["reviews_per_day"]
        if not _request(
            "saveDeckConfig", params={"config": config}, endpoint=endpoint, api_key=api_key
        ):
            raise AnkiConnectError("failed to save study preset")
        if not _request(
            "setDeckConfigId",
            params={"decks": names, "configId": config["id"]},
            endpoint=endpoint,
            api_key=api_key,
        ):
            raise AnkiConnectError("failed to assign study preset")
    _request("sync", endpoint=endpoint, api_key=api_key, timeout=120)
