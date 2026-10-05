# Anki — Théorie de plongée

Socle repris de `anki-deck-wset-3` : YAML, Pydantic, genanki, modèles QCM/basic/cloze,
Markdown, mélange des choix QCM, AnkiConnect, Ruff, basedpyright, pytest, schéma JSON,
pre-commit et CI avec artefacts et releases GitHub.

Le contenu est en français. N2 est le niveau par défaut ; N3 et N4 sont prêts à recevoir
leurs cartes. Les deux premiers chapitres contiennent 41 cartes revues : 21 sur les prérogatives N2
et 20 sur l’organisation et les équipements.
Voir les revues des [prérogatives](docs/reviews/01-prerogatives.md) et de
[l’organisation](docs/reviews/02-organisation.md).

## Démarrage

```sh
uv sync --extra dev
make check
make build                        # N2 → dist/diving-n2-fr.apkg
make build ANKI_LEVEL=N3           # N3
make build-all                    # trois packages indépendants
make push ANKI_LEVEL=N2            # importe dans Anki et synchronise AnkiWeb
uv run diving-anki build --level N2 --include-drafts
```

`push` nécessite Anki Desktop et l’extension AnkiConnect. Il déclenche une synchronisation.
Un build sans cartes produit un package vide destiné à vérifier le pipeline.

## Organisation

- `cards/n2/`, `cards/n3/`, `cards/n4/` : un fichier YAML par chapitre.
- `sources/` : documents privés, ignorés par Git.
- `src/diving_anki/` : validation, rendu, génération et import AnkiConnect.
- `templates/` : modèles HTML/CSS et libellés français.
- `schema/cards.schema.json` : schéma généré pour les éditeurs.
- `tests/` : contrôles des formats, des niveaux et des packages Anki.

Chaque carte indique explicitement `levels: [N2]` ou, pour une carte commune,
`levels: [N2, N3]`. Aucune inclusion automatique d’un niveau dans un autre.
Le dossier sert à ranger les chapitres ; `levels` détermine les packages.
Les IDs des cartes sont uniques dans tout le projet. Les GUIDs et IDs des modèles
sont stables et distincts du projet WSET. Une carte partagée possède un GUID par niveau,
pour pouvoir importer plusieurs decks sans déplacer ses notes entre les niveaux.
Les sous-decks suivent `Plongée::N2::Physique`, par exemple.

Voir [CONTRIBUTING.md](CONTRIBUTING.md) et [CONTENT_GUIDELINES.md](CONTENT_GUIDELINES.md).
