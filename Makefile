.PHONY: check lint format typecheck validate schema test build build-all push

ANKI_LEVEL ?= N2

check:
	uv run diving-anki check

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff format .
	uv run ruff check --fix .

typecheck:
	uv run basedpyright src tests

validate:
	uv run diving-anki validate

schema:
	uv run diving-anki schema

test:
	uv run pytest

build:
	uv run diving-anki build --level $(ANKI_LEVEL) --out dist

push:
	uv run diving-anki push --level $(ANKI_LEVEL) --out dist


build-all:
	uv run diving-anki build --level all --out dist
