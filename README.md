# Anki — Théorie de plongée

Socle repris de `anki-deck-wset-3` : YAML, Pydantic, genanki, modèles QCM/basic/cloze,
Markdown, mélange des choix QCM, AnkiConnect, Ruff, basedpyright, pytest, schéma JSON,
pre-commit et CI avec artefacts et releases GitHub.

Le contenu est en français. N2 est le niveau par défaut ; N3 et N4 sont prêts à recevoir
leurs cartes. Le deck N2 comprend **308 cartes revues**, réparties dans 18 fichiers de chapitre
et cinq catégories Anki. La [revue finale](docs/reviews/REVUE_FINALE_N2.md) détaille
les dix fusions, les six ajouts et les corrections de clarté.
La [couverture](docs/reviews/COUVERTURE_FINALE_N2.md) relie les 334 objectifs suivis
aux cartes actives. Les anciennes cartes fusionnées restent suspendues dans Anki pour
conserver leur historique ; leur [registre](docs/reviews/RETIREMENTS_N2.yaml) empêche
la réutilisation de leurs IDs. Un import de package ne suspend pas à lui seul les notes retirées.

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
52 cartes sont regroupées dans Réglementation, 82 dans Physique, 53 dans Prévention des accidents,
77 dans Désaturation et 44 dans Matériel et préparation. Les fichiers et tags conservent le détail
des chapitres.

Voir [CONTRIBUTING.md](CONTRIBUTING.md) et [CONTENT_GUIDELINES.md](CONTENT_GUIDELINES.md).

Le dépôt distant est [NayanChauveau/diving-anki](https://github.com/NayanChauveau/diving-anki).
`git push origin main` publie les commits sur GitHub ; `make push` construit et synchronise
le deck avec AnkiWeb. Ces deux commandes ont des destinations différentes.
