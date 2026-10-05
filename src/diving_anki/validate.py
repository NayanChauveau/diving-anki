from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from diving_anki.schema import Card


@dataclass(frozen=True)
class ValidationIssue:
    card_id: str | None
    message: str

    def __str__(self) -> str:
        if self.card_id:
            return f"{self.card_id}: {self.message}"
        return self.message


def validate_cards(cards: list[Card]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    counts = Counter(card.id for card in cards)
    for card_id, count in sorted(counts.items()):
        if count > 1:
            issues.append(ValidationIssue(card_id, f"duplicate id ({count} occurrences)"))

    for card in cards:
        if len(card.levels) != len(set(card.levels)):
            issues.append(ValidationIssue(card.id, "duplicate levels"))
    return issues
