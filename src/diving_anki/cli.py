from __future__ import annotations

import argparse
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path

from diving_anki.anki_connect import AnkiConnectError, push_packages
from diving_anki.build import build_collection
from diving_anki.json_schema import default_schema_path, schema_matches, write_schema
from diving_anki.load import LoadError, load_cards
from diving_anki.paths import cards_dir, find_repo_root, templates_dir
from diving_anki.validate import validate_cards


def _add_root_cards(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--cards", type=Path, default=None, help="Cards directory")
    parser.add_argument("--root", type=Path, default=None, help="Repository root")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="diving-anki",
        description="Valider et générer les decks de théorie de plongée en français.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate", help="Validate card YAML against the schema")
    _add_root_cards(p_validate)

    p_schema = sub.add_parser("schema", help="Write or check schema/cards.schema.json")
    p_schema.add_argument(
        "--check",
        action="store_true",
        help="Fail if the committed JSON Schema is out of date",
    )
    p_schema.add_argument("--out", type=Path, default=None, help="Override output path")
    p_schema.add_argument("--root", type=Path, default=None, help="Repository root")

    p_check = sub.add_parser("check", help="Run the full quality gate (lint, types, tests, cards)")
    p_check.add_argument("--root", type=Path, default=None, help="Repository root")

    p_build = sub.add_parser("build", help="Generate the unified N2/N3/N4 .apkg package")
    p_build.add_argument("--out", type=Path, default=Path("dist"), help="Output directory")
    p_build.add_argument(
        "--include-drafts",
        action="store_true",
        help="Include cards with status: draft",
    )
    _add_root_cards(p_build)

    p_push = sub.add_parser(
        "push",
        help="Build, import into Anki Desktop, then sync with AnkiWeb",
    )
    p_push.add_argument("--out", type=Path, default=Path("dist"), help="Output directory")
    p_push.add_argument(
        "--include-drafts",
        action="store_true",
        help="Include cards with status: draft",
    )
    p_push.add_argument(
        "--no-launch",
        action="store_true",
        help="Do not launch Anki Desktop when AnkiConnect is unavailable",
    )
    p_push.add_argument(
        "--anki-connect-url",
        default=None,
        help="Override AnkiConnect URL (or set ANKI_CONNECT_URL)",
    )
    p_push.add_argument(
        "--startup-timeout",
        type=float,
        default=30,
        help="Seconds to wait for Anki Desktop and AnkiConnect",
    )
    _add_root_cards(p_push)

    args = parser.parse_args(argv)
    root = find_repo_root(args.root) if getattr(args, "root", None) else find_repo_root()

    if args.command == "schema":
        return _schema_command(root, check=args.check, out=args.out)
    if args.command == "check":
        return _check_command(root)
    source = args.cards or cards_dir(root)
    templates = templates_dir(root)

    try:
        cards = load_cards(source)
    except LoadError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    issues = validate_cards(cards)
    if issues:
        for issue in issues:
            print(f"error: {issue}", file=sys.stderr)
        return 1

    if args.command == "validate":
        print(f"{len(cards)} card(s) OK")
        return 0

    out_dir = args.out if args.out.is_absolute() else Path.cwd() / args.out
    path, result = build_collection(
        cards,
        templates=templates,
        out_dir=out_dir,
        include_drafts=args.include_drafts,
    )
    print(f"wrote {path} ({len(result.notes)} notes, {result.skipped_drafts} drafts skipped)")
    packages = [path]

    if args.command == "push":
        try:
            push_packages(
                packages,
                endpoint=args.anki_connect_url,
                launch=not args.no_launch,
                startup_timeout=args.startup_timeout,
            )
        except AnkiConnectError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        for package in packages:
            print(f"imported {package.name}")
        print("synced with AnkiWeb")
    return 0


def _schema_command(root: Path, *, check: bool, out: Path | None) -> int:
    path = out or default_schema_path(root)
    if check:
        if schema_matches(path):
            print(f"{path} is up to date")
            return 0
        print(f"error: {path} is missing or stale; run `diving-anki schema`", file=sys.stderr)
        return 1
    write_schema(path)
    print(f"wrote {path}")
    return 0


def _check_command(root: Path) -> int:
    steps: list[tuple[str, list[str]]] = [
        ("ruff lint", ["ruff", "check", str(root)]),
        ("ruff format", ["ruff", "format", "--check", str(root)]),
        ("basedpyright", ["basedpyright", str(root / "src"), str(root / "tests")]),
        ("json schema", ["diving-anki", "schema", "--check", "--root", str(root)]),
        ("cards", ["diving-anki", "validate", "--root", str(root)]),
        ("pytest", ["pytest", str(root / "tests")]),
    ]
    failed = 0
    for label, command in steps:
        print(f"→ {label}", flush=True)
        result = subprocess.run(command, cwd=root, check=False)
        if result.returncode != 0:
            print(f"✗ {label} failed", file=sys.stderr)
            failed = 1
    if failed:
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
