"""Real Anki import regression.

Run with `uv run --with anki python -m pytest tests/test_anki_import.py`.
"""

from pathlib import Path

import genanki
import pytest

from diving_anki.build import build_collection, prepare, write_package
from diving_anki.schema import CardAdapter

anki = pytest.importorskip("anki.collection", reason="Optional real Anki import runtime")
ROOT = Path(__file__).resolve().parents[1]


def example(card_id: str, levels: list[str]):
    return CardAdapter.validate_python(
        {
            "id": card_id,
            "type": "basic",
            "deck": "Physique",
            "levels": levels,
            "status": "reviewed",
            "fr": {"front": "Question test", "back": "Réponse test"},
        }
    )


@pytest.mark.parametrize("legacy_n2", [True, False])
def test_imports_keep_history_and_suspensions(tmp_path, legacy_n2):
    shared = example("shared-test-001", ["N2", "N3", "N4"])
    suspended = example("suspended-test-001", ["N2", "N3", "N4"])
    initial = prepare([shared, suspended], "N2" if legacy_n2 else "N4")
    if legacy_n2:
        # Reproduce the published N2 identity and location before the unification.
        for note in initial.notes:
            note.guid = genanki.guid_for("diving-theory", note.card.id, "N2", "fr")
            note.deck = "Plongée::N2::Physique"
            note.tags = ["diving-theory", "level::N2"]
    old = write_package(
        initial, templates=ROOT / "templates", output=tmp_path / "old.apkg", mode="fr"
    )
    col = anki.Collection(str(tmp_path / "collection.anki2"))
    try:

        def import_package(path):
            col.import_anki_package(
                anki.ImportAnkiPackageRequest(
                    package_path=str(path),
                    options=anki.ImportAnkiPackageOptions(
                        with_scheduling=False,
                        with_deck_configs=False,
                    ),
                )
            )

        import_package(old)
        card_ids = col.db.list("select id from cards order by id")
        assert len(card_ids) == 2
        col.db.execute(
            "update cards set type=2, queue=2, due=42, ivl=14, factor=2400, "
            "reps=7, lapses=1, flags=3"
        )
        col.db.execute("update cards set queue=-1 where id=?", card_ids[1])
        for i, cid in enumerate(card_ids):
            col.db.execute(
                "insert into revlog values (?,?,?,?,?,?,?,?,?)",
                1_700_000_000_000 + i,
                cid,
                -1,
                3,
                14,
                7,
                2400,
                3000,
                1,
            )
        # Ensure the new package is newer, as with a regular released update.
        col.db.execute("update notes set mod=1")
        state_sql = (
            "select id,nid,type,queue,due,ivl,factor,reps,lapses,left,flags,data "
            "from cards order by id"
        )
        before = col.db.all(state_sql)
        history = col.db.all("select * from revlog order by id")
        n4_only = example("n4-only-test-001", ["N4"])
        for _ in range(3):
            package, _ = build_collection(
                [shared, suspended, n4_only],
                templates=ROOT / "templates",
                out_dir=tmp_path,
            )
            import_package(package)
            assert col.db.scalar("select count(*) from notes") == 3
            assert col.db.scalar("select count(*) from cards") == 3
            assert col.db.all(state_sql)[:2] == before
            assert col.db.all("select * from revlog order by id") == history
        for note_id in col.db.list("select nid from cards where id in (?,?)", *card_ids):
            tags = col.get_note(note_id).tags
            assert {"level::N2", "level::N3", "level::N4"}.issubset(tags)
    finally:
        col.close()
