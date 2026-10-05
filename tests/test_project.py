import sqlite3
import zipfile
from pathlib import Path

import genanki
import jsonschema
import pytest
from pydantic import ValidationError

from diving_anki.build import build_level, prepare
from diving_anki.cli import main
from diving_anki.ids import MCQ_MODEL_ID, note_guid
from diving_anki.json_schema import card_file_json_schema, schema_matches
from diving_anki.load import load_cards
from diving_anki.schema import CardAdapter
from diving_anki.validate import validate_cards

ROOT = Path(__file__).resolve().parents[1]


def card(kind: str = "basic", **overrides: object):
    content = {
        "basic": {"front": "Question", "back": "Réponse"},
        "mcq": {
            "question": "Question",
            "choices": [{"text": "Oui", "correct": True}, {"text": "Non"}],
            "explanation": "Explication",
        },
        "cloze": {"text": "Texte {{c1::masqué}}"},
    }
    return CardAdapter.validate_python(
        {
            "id": f"test-{kind}-001",
            "type": kind,
            "deck": "Thème",
            "levels": ["N2"],
            "fr": content[kind],
            **overrides,
        }
    )


def test_selection_and_drafts():
    shared = card(levels=["N2", "N3"], status="reviewed")
    draft = card("mcq")
    assert len(prepare([shared, draft], "N2").notes) == 1
    assert len(prepare([shared, draft], "N2", include_drafts=True).notes) == 2
    assert len(prepare([shared, draft], "N3").notes) == 1
    assert not prepare([shared, draft], "N4").notes
    assert prepare([shared], "N2").notes[0].guid != prepare([shared], "N3").notes[0].guid


@pytest.mark.parametrize(
    "overrides",
    [
        {"levels": []},
        {"levels": ["N1"]},
        {"fr": None},
        {"en": {}},
        {"typo": True},
        {"deck": "A::::B"},
    ],
)
def test_invalid_cards(overrides):
    with pytest.raises(ValidationError):
        card(**overrides)


def test_duplicates():
    assert validate_cards([card(), card()])
    assert validate_cards([card(levels=["N2", "N2"])])


def test_ids():
    assert note_guid("test-basic-001", "N2") == note_guid("test-basic-001", "N2")
    assert note_guid("test-basic-001", "N2") != genanki.guid_for(
        "wset3-vin", "test-basic-001", "fr"
    )
    assert MCQ_MODEL_ID != 1760000101


def test_schema_and_sources():
    assert schema_matches(ROOT / "schema/cards.schema.json")
    cards = load_cards(ROOT / "cards")
    assert not validate_cards(cards)
    validator = jsonschema.Draft202012Validator(card_file_json_schema())
    validator.validate({"cards": [card().model_dump(mode="json")]})
    validator.validate({"cards": [item.model_dump(mode="json") for item in cards]})


def test_recursive_loading(tmp_path):
    (tmp_path / "n2").mkdir()
    import yaml

    (tmp_path / "n2/chapter.yaml").write_text(
        yaml.safe_dump({"cards": [card().model_dump(mode="json")]})
    )
    assert len(load_cards(tmp_path)) == 1


def test_real_package(tmp_path):
    cards = [card(kind, status="reviewed") for kind in ("basic", "mcq", "cloze")]
    package, result = build_level(cards, "N2", templates=ROOT / "templates", out_dir=tmp_path)
    assert len(result.notes) == 3
    with zipfile.ZipFile(package) as archive:
        archive.extract("collection.anki2", tmp_path)
    with sqlite3.connect(tmp_path / "collection.anki2") as db:
        assert db.execute("select count(*) from notes").fetchone()[0] == 3
        assert db.execute("select count(*) from cards").fetchone()[0] == 3
        fields = db.execute("select flds from notes").fetchall()
        assert any("Explication" in row[0] for row in fields)


def test_cli_all(tmp_path):
    assert main(["build", "--root", str(ROOT), "--level", "all", "--out", str(tmp_path)]) == 0
    assert sorted(p.name for p in tmp_path.glob("*.apkg")) == [
        "diving-n2-fr.apkg",
        "diving-n3-fr.apkg",
        "diving-n4-fr.apkg",
    ]
