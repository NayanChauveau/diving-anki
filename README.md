# Anki — Théorie de plongée

Socle repris de `anki-deck-wset-3` : YAML, Pydantic, genanki, modèles QCM/basic/cloze,
Markdown, mélange des choix QCM, AnkiConnect, Ruff, basedpyright, pytest, schéma JSON,
pre-commit et CI avec artefacts et releases GitHub.

Le contenu est en français. N2 est le niveau par défaut ; N3 et N4 sont prêts à recevoir
leurs cartes. Les chapitres 01–16 et 18 contiennent 301 cartes revues : 21 sur les prérogatives N2,
20 sur l’organisation et les équipements, 12 sur les documents, la responsabilité et l’environnement,
24 sur les [pressions](docs/reviews/04-pression.md) et 25 sur la
[flottabilité](docs/reviews/05-flottabilite.md), ainsi que 31 sur les
[gaz et l’autonomie](docs/reviews/06-gaz-autonomie.md), dont 20 exercices, et 21 sur les
[barotraumatismes](docs/reviews/07-barotraumatismes.md), 11 sur
[l’essoufflement](docs/reviews/08-essoufflement.md), 11 sur le
[froid](docs/reviews/09-froid.md) et 14 sur la [narcose](docs/reviews/10-narcose.md), ainsi que 26 sur les
[accidents de désaturation](docs/reviews/11-add.md) et 20 sur les
[tables](docs/reviews/12-tables.md), 17 sur les [ordinateurs](docs/reviews/13-ordinateurs.md)
et 10 sur les [remontées anormales](docs/reviews/14-remontees-anormales.md), 14 sur les
[blocs et le gonflage](docs/reviews/15-gonflage-blocs.md), 21 sur les
[détendeurs](docs/reviews/16-detendeurs.md) et 3 sur les
[pannes complémentaires](docs/reviews/18-lecture-pannes.md).
Voir les revues des [prérogatives](docs/reviews/01-prerogatives.md) et de
[l’organisation](docs/reviews/02-organisation.md) et des
[documents et de l’environnement](docs/reviews/03-documents-environnement.md).

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
N2 comporte cinq catégories sans sous-deck par chapitre : **Réglementation**, **Physique**,
**Prévention des accidents**, **Désaturation**, **Matériel et préparation**.
53 cartes sont regroupées dans Réglementation et 80 dans Physique et 57 dans Prévention des accidents ; 73 dans Désaturation ; 38 dans Matériel et préparation. Les fichiers et tags conservent le détail des chapitres.

Voir [CONTRIBUTING.md](CONTRIBUTING.md) et [CONTENT_GUIDELINES.md](CONTENT_GUIDELINES.md).

Le dépôt distant est [NayanChauveau/diving-anki](https://github.com/NayanChauveau/diving-anki).
`git push origin main` publie les commits sur GitHub ; `make push` construit et synchronise
le deck avec AnkiWeb. Ces deux commandes ont des destinations différentes.
