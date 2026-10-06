from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

import genanki

from diving_anki.ids import (
    BASIC_MODEL_ID,
    CLOZE_MODEL_ID,
    COLLECTION_DECK_NAME,
    MCQ_MODEL_ID,
    ancestor_paths,
    deck_id_for,
    note_guid,
)
from diving_anki.render import (
    inject_mcq_shuffle,
    load_ui,
    read_template,
    render_choices_back,
    render_choices_front,
    render_markdown,
    wrap_explanation,
)
from diving_anki.schema import BasicCard, Card, ClozeCard, McqCard, Status

Lang = Literal["fr"]
BuildLang = Literal["fr"]
Level = Literal["N2", "N3", "N4"]
BuildSelection = Level | Literal["combined"]

MONOLINGUAL_MODELS = {"mcq": "mcq", "basic": "basic", "cloze": "cloze"}


@dataclass
class PreparedNote:
    guid: str
    deck: str
    tags: list[str]
    model: str
    card: Card
    lang: Lang | None = None
    fields: list[str] = field(default_factory=list)


@dataclass
class BuildResult:
    notes: list[PreparedNote] = field(default_factory=list)
    skipped_drafts: int = 0


def select_cards(cards: Iterable[Card], *, include_drafts: bool) -> tuple[list[Card], int]:
    selected: list[Card] = []
    skipped = 0
    for card in cards:
        if card.status is Status.DRAFT and not include_drafts:
            skipped += 1
            continue
        selected.append(card)
    return selected, skipped


def card_tags(card: Card, extra: list[str] | None = None) -> list[str]:
    tags = ["diving-theory", f"type::{card.type}", f"status::{card.status.value}", *card.tags]
    if extra:
        tags.extend(extra)
    return [tag.replace(" ", "-") for tag in tags]


def _mcq_fields(card: McqCard, lang: Lang, ui: dict[str, str]) -> list[str]:
    content = card.fr
    assert content is not None
    return [
        render_markdown(content.question),
        render_choices_front(content.choices, card.id),
        render_choices_back(content.choices, card.id),
        wrap_explanation(render_markdown(content.explanation), ui["explanation"]),
    ]


def _basic_fields(card: BasicCard, lang: Lang) -> list[str]:
    content = card.fr
    assert content is not None
    return [render_markdown(content.front), render_markdown(content.back)]


def _cloze_fields(card: ClozeCard, lang: Lang) -> list[str]:
    content = card.fr
    assert content is not None
    extra = render_markdown(content.extra) if content.extra.strip() else ""
    return [content.text, extra]


def fill_fields(note: PreparedNote, *, ui_fr: dict[str, str]) -> None:
    card = note.card
    if isinstance(card, McqCard):
        note.fields = _mcq_fields(card, "fr", ui_fr)
        if note.model == "basic":
            question, front, back, explanation = note.fields
            note.fields = [question + front, back + explanation]
    elif isinstance(card, BasicCard):
        note.fields = _basic_fields(card, "fr")
    else:
        note.fields = _cloze_fields(card, "fr")


def prepare(
    cards: Iterable[Card],
    level: BuildSelection,
    *,
    include_drafts: bool = False,
) -> BuildResult:
    selected, skipped = select_cards(
        [card for card in cards if level == "combined" or level in card.levels],
        include_drafts=include_drafts,
    )
    result = BuildResult(skipped_drafts=skipped)
    for card in selected:
        result.notes.append(
            PreparedNote(
                guid=note_guid(card.id),
                deck=f"{COLLECTION_DECK_NAME}::{card.deck}",
                tags=card_tags(card, ["lang::fr", *[f"level::{item}" for item in card.levels]]),
                model=(
                    card.anki_model or "mcq"
                    if isinstance(card, McqCard)
                    else MONOLINGUAL_MODELS[card.type]
                ),
                card=card,
                lang="fr",
            )
        )
    return result


def load_models(templates: Path) -> dict[str, genanki.Model]:
    mcq_css = read_template(templates, "mcq", "style.css")
    basic_css = read_template(templates, "basic", "style.css")
    cloze_css = read_template(templates, "cloze", "style.css")
    shuffle_js = read_template(templates, "mcq", "shuffle.js")
    mcq_front = inject_mcq_shuffle(
        read_template(templates, "mcq", "front.html"),
        shuffle_js,
        reveal=False,
    )
    mcq_back = inject_mcq_shuffle(
        read_template(templates, "mcq", "back.html"),
        shuffle_js,
        reveal=True,
    )
    basic_front = read_template(templates, "basic", "front.html")
    basic_back = read_template(templates, "basic", "back.html")
    basic_front = inject_mcq_shuffle(basic_front, shuffle_js, reveal=False)
    basic_back = inject_mcq_shuffle(basic_back, shuffle_js, reveal=True)
    basic_css += "\n" + mcq_css
    cloze_front = read_template(templates, "cloze", "front.html")
    cloze_back = read_template(templates, "cloze", "back.html")

    return {
        "mcq": genanki.Model(
            MCQ_MODEL_ID,
            "Plongée MCQ",
            fields=[
                {"name": "Question"},
                {"name": "ChoicesFront"},
                {"name": "ChoicesBack"},
                {"name": "Explanation"},
            ],
            templates=[{"name": "MCQ", "qfmt": mcq_front, "afmt": mcq_back}],
            css=mcq_css,
        ),
        "basic": genanki.Model(
            BASIC_MODEL_ID,
            "Plongée Basic",
            fields=[{"name": "Front"}, {"name": "Back"}],
            templates=[{"name": "Basic", "qfmt": basic_front, "afmt": basic_back}],
            css=basic_css,
        ),
        "cloze": genanki.Model(
            CLOZE_MODEL_ID,
            "Plongée Cloze",
            fields=[{"name": "Text"}, {"name": "Extra"}],
            templates=[{"name": "Cloze", "qfmt": cloze_front, "afmt": cloze_back}],
            css=cloze_css,
            model_type=genanki.Model.CLOZE,
        ),
    }


def _ensure_decks(names: Iterable[str]) -> dict[str, genanki.Deck]:
    decks: dict[str, genanki.Deck] = {}
    for name in names:
        for path in ancestor_paths(name):
            if path not in decks:
                decks[path] = genanki.Deck(deck_id_for(path), path)
    return decks


def write_package(
    result: BuildResult,
    *,
    templates: Path,
    output: Path,
    mode: BuildLang,
) -> Path:
    models = load_models(templates)
    ui_fr = load_ui(templates, "fr")

    for note in result.notes:
        fill_fields(note, ui_fr=ui_fr)

    decks = _ensure_decks(note.deck for note in result.notes)
    for prepared in result.notes:
        decks[prepared.deck].add_note(
            genanki.Note(
                guid=prepared.guid,
                model=models[prepared.model],
                fields=prepared.fields,
                tags=prepared.tags,
            )
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    package = genanki.Package(list(decks.values()))
    package.write_to_file(str(output))
    return output


def build_collection(
    cards: list[Card],
    *,
    templates: Path,
    out_dir: Path,
    include_drafts: bool = False,
) -> tuple[Path, BuildResult]:
    result = prepare(cards, "combined", include_drafts=include_drafts)
    path = out_dir / "diving-fr.apkg"
    write_package(result, templates=templates, output=path, mode="fr")
    # Retire only this project's obsolete generated exports after a successful build.
    for legacy_level in ("n2", "n3", "n4"):
        (out_dir / f"diving-{legacy_level}-fr.apkg").unlink(missing_ok=True)
    return path, result
