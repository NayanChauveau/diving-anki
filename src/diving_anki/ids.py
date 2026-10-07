from __future__ import annotations

import hashlib

import genanki

NAMESPACE = "diving-theory"
ROOT_DECK_NAME = "Plongée"
MCQ_MODEL_ID = 1860000101
BASIC_MODEL_ID = 1860000102
CLOZE_MODEL_ID = 1860000103
ROOT_DECK_ID = 1860001000
ROOT_DECK_IDS = {ROOT_DECK_NAME: ROOT_DECK_ID}


def note_guid(card_id: str) -> str:
    """One identity across levels, preserving the GUIDs of the published N2 notes.

    N2 is a fixed legacy salt, not the current membership of the card. Keep it even
    for new N3/N4 cards and when a card's levels change.
    """
    return genanki.guid_for(NAMESPACE, card_id, "N2", "fr")


def deck_id_for(deck_path_name: str) -> int:
    if deck_path_name in ROOT_DECK_IDS:
        return ROOT_DECK_IDS[deck_path_name]
    digest = hashlib.sha256(f"{NAMESPACE}:{deck_path_name}".encode()).hexdigest()
    return ROOT_DECK_ID + 1 + (int(digest[:8], 16) % 8_000_000)


def deck_path(chapter: str, *, root: str = ROOT_DECK_NAME) -> str:
    chapter = chapter.strip()
    if not chapter:
        return root
    return f"{root}::{chapter}"


def ancestor_paths(deck_path_name: str) -> list[str]:
    parts = deck_path_name.split("::")
    return ["::".join(parts[: i + 1]) for i in range(len(parts))]
