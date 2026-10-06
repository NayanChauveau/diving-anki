.PHONY: check lint format typecheck validate schema test build build-all push

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
	uv run diving-anki build --out dist

push:
	uv run diving-anki push --out dist


build-all: build
