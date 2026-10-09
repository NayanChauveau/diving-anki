import pytest

from diving_anki import anki_connect


def test_push_does_not_modify_cards_or_options_after_import(tmp_path, monkeypatch):
    package = tmp_path / "diving-fr.apkg"
    package.write_bytes(b"package")
    calls = []

    def request(action, **kwargs):
        calls.append((action, kwargs.get("params")))
        assert action in {"version", "importPackage", "sync"}
        return 6 if action == "version" else None

    monkeypatch.setattr(anki_connect, "_request", request)
    anki_connect.push_packages([package], launch=False)
    assert calls == [
        ("version", None),
        ("importPackage", {"path": str(package.resolve())}),
        ("sync", None),
    ]


def test_failed_import_does_not_sync(tmp_path, monkeypatch):
    package = tmp_path / "diving-fr.apkg"
    package.write_bytes(b"package")

    def request(action, **kwargs):
        if action == "importPackage":
            raise anki_connect.AnkiConnectError("import failed")
        assert action == "version"
        return 6

    monkeypatch.setattr(anki_connect, "_request", request)
    with pytest.raises(anki_connect.AnkiConnectError, match="import failed"):
        anki_connect.push_packages([package], launch=False)
