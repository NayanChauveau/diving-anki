# Anki — Théorie de plongée

Un deck Anki en français pour réviser la théorie des **niveaux 2, 3 et 4**, dans le cadre
français et du cursus FFESSM : réglementation, physique, prévention des accidents,
désaturation, matériel et préparation de la plongée.

**585 cartes** : 583 QCM à une seule bonne réponse, et deux situations à réponse libre.
Chaque carte explique la réponse, souvent avec un cas ou un calcul.

**[Télécharger diving-fr.apkg](https://github.com/NayanChauveau/diving-anki/releases/latest/download/diving-fr.apkg)**
· [Dernière version](https://github.com/NayanChauveau/diving-anki/releases/latest)
· [Toutes les versions](https://github.com/NayanChauveau/diving-anki/releases)

## Installer

Le plus simple est **[Deck Manager](https://github.com/NayanChauveau/anki-deckdock/)**.
Cette extension installe le deck et propose une mise à jour quand une nouvelle version
sort. Il faut Anki **26.09** ou plus récent.

1. Installer [Anki Desktop](https://apps.ankiweb.net/).
2. Installer Deck Manager, puis ouvrir **Outils → Deck Manager**.
3. Ouvrir la [dernière version](https://github.com/NayanChauveau/diving-anki/releases/latest),
   rubrique **Assets**, et copier le lien de `diving-fr.apkg`.
4. Coller ce lien. Il a cette forme :

```text
https://github.com/NayanChauveau/diving-anki/releases/download/v0.1.0/diving-fr.apkg
```

Le fichier s’appelle toujours `diving-fr.apkg`. Seul le numéro de version change.
Deck Manager attend ce lien précis : le bouton **Télécharger** en haut de cette page
ne convient pas.

À l’import, accepter les **préréglages de paquet** : 10 nouvelles cartes par jour,
et jusqu’à 200 révisions.

### Sans Deck Manager

1. Télécharger [diving-fr.apkg](https://github.com/NayanChauveau/diving-anki/releases/latest/download/diving-fr.apkg).
   Prendre le fichier dans **Assets**, pas l’archive **Source code**.
2. Dans Anki : **Fichier → Importer**, puis confirmer.
3. Activer l’import des préréglages de paquet.

Le deck apparaît sous **Plongée**. Si Anki refuse le fichier, mettre l’application
à jour et télécharger le paquet à nouveau. Le
[manuel d’import](https://docs.ankiweb.net/importing/packaged-decks.html) décrit les options.

### Sur le téléphone ou un autre ordinateur

Après l’import sur l’ordinateur, connecter le profil à [AnkiWeb](https://ankiweb.net/)
et lancer **Synchroniser**. Utiliser le même compte sur les autres appareils.

Sur iPhone et iPad : **AnkiMobile**. Sur Android : **AnkiDroid**. Les liens sont sur
la [page de téléchargement d’Anki](https://apps.ankiweb.net/). Le
[guide de synchronisation](https://docs.ankiweb.net/syncing.html) couvre la première
configuration.

## Réviser

```text
Plongée
├── N2 — 339 cartes, la base
├── N3 — 122 cartes en plus
└── N4 — 124 cartes en plus
```

Ouvrir **N2** pour commencer. N3 et N4 ajoutent leurs cartes à ce qui précède :
une carte déjà vue en N2 reste dans N2, avec son historique. Continuer les révisions
N2 pendant l’apprentissage de N3.

| Niveau | Cartes du programme | Dont déjà vues plus tôt |
| --- | ---: | ---: |
| N2 | 339 | — |
| N3 | 357 | 235, dans N2 |
| N4 | 454 | 330, dans N2 ou N3 |

Pour voir tout un programme dans **Parcourir** :

```text
tag:diving-theory tag:level::N3
tag:diving-theory tag:level::N4
```

Les QCM ont une seule bonne réponse. L’ordre des choix change à chaque révision.
Choisir une réponse, puis afficher le verso : la note se fait avec les boutons d’Anki,
qui programment la prochaine révision. Le [guide d’étude](https://docs.ankiweb.net/studying.html)
explique ces boutons.

Pour un calcul, refaire le raisonnement et vérifier les unités avant de répondre.
Le deck accompagne les cours et la pratique : les gestes, les nœuds et le guidage
se travaillent aussi en formation.

Le rangement, les réglages et une ancienne installation sont détaillés dans le
[guide des niveaux](docs/SHARED_COLLECTION.md).

## Mettre à jour

Avec Deck Manager, Anki propose la nouvelle version au démarrage. **Importer**, puis
confirmer le dialogue d’Anki.

À la main :

1. Télécharger à nouveau `diving-fr.apkg`.
2. L’importer dans la **même** collection, sans supprimer le deck.
3. Synchroniser les autres appareils.

L’historique et les échéances des cartes déjà révisées sont conservés. L’import ajoute
et met à jour les cartes. Celles qui ont disparu du paquet restent dans la collection :
les retrouver dans **Parcourir** et les suspendre pour qu’elles ne reviennent plus.
Une première installation contient les 585 cartes actuelles.

Une collection installée autrefois sous **Plongée → N2** garde ses cartes. Pour les
ranger dans les catégories actuelles, suivre le
[guide de migration](docs/SHARED_COLLECTION.md#migrer-une-installation-n2-existante).

## Contenu

| Catégorie | Cartes | Thèmes |
| --- | ---: | --- |
| Réglementation | 89 | Prérogatives, âges, organisation, équipements, documents, environnement |
| Physique | 103 | Pression, flottabilité, gaz, consommation, autonomie, vision |
| Prévention des accidents | 109 | Barotraumatismes, essoufflement, froid, narcose |
| Désaturation | 110 | Accidents, tables MN90, ordinateurs, remontées anormales |
| Matériel et préparation | 119 | Blocs, gonflage, détendeurs, pannes, orientation |
| Anatomie et physiologie | 26 | Ventilation, échanges, circulation, shunts |
| Conduite de palanquée | 7 | Accueil, surveillance, adaptation, débriefing |
| Matelotage et repérage | 15 | Nœuds, mouillage, carte, GPS, marée |
| Environnement | 7 | Milieux, biodiversité, protection |

Les textes sont originaux. Ils sont recoupés avec les références FFESSM, la
réglementation, la médecine et les notices des fabricants selon le sujet.
Le détail des sources et des revues est dans `docs/reviews/`.

- [Plan N2](docs/IMPLEMENTATION_N2.md) et [couverture N2](docs/reviews/COUVERTURE_FINALE_N2.md)
- [Plan N3](docs/IMPLEMENTATION_N3.md) et [couverture N3](docs/reviews/n3/COUVERTURE_N3.md)
- [Plan N4](docs/IMPLEMENTATION_N4.md) et [couverture N4](docs/reviews/n4/COUVERTURE_PLAN.md)

## Modifier les cartes

Pour utiliser le deck publié, la section **Installer** suffit. Pour le modifier :

- [Git](https://git-scm.com/)
- [Python 3.12](https://www.python.org/downloads/) ou plus récent
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- `make`

```sh
git clone https://github.com/NayanChauveau/diving-anki.git
cd diving-anki
uv sync --extra dev
make check
make build
```

Le paquet est écrit dans `dist/diving-fr.apkg`.

| Commande | Effet |
| --- | --- |
| `make check` | Vérifie le format, les cartes et les tests |
| `make build` | Construit `diving-fr.apkg` |
| `make push` | Construit, importe dans Anki et synchronise AnkiWeb |
| `make schema` | Régénère le schéma après un changement du modèle de données |

`make push` a besoin d’[AnkiConnect](https://ankiweb.net/shared/info/2055492159)
(code `2055492159` dans **Outils → Extensions**). Anki doit être ouvert sur le bon
profil : la synchronisation concerne tout ce profil. L’import d’un `.apkg` à la main
n’a pas besoin de ce module.

```sh
uv run diving-anki push --out dist --no-launch
```

Les cartes sont des fichiers YAML dans `cards/n2/`, `cards/n3/` et `cards/n4/`,
un fichier par chapitre. Une carte indique ses niveaux, par exemple `[N2]` ou
`[N2, N3]`. Son identité Anki ne change pas d’une version à l’autre : c’est ce qui
permet de mettre à jour sans perdre les révisions.

Avant une modification, lire [CONTRIBUTING.md](CONTRIBUTING.md).
Une erreur peut aussi être signalée par une
[issue](https://github.com/NayanChauveau/diving-anki/issues/new), avec le texte de
la question et, si possible, une source.

```text
cards/          Cartes, un YAML par chapitre
docs/           Plans, schémas et revues
src/            Construction des paquets et import Anki
templates/      Présentation des cartes
sources/        Documents privés, absents de Git
```

## Versions

Chaque mise à jour publiée sur `main` reçoit un numéro `vX.Y.Z`, à partir de `v0.1.0`.
Le paquet de cette version est à :

```text
https://github.com/NayanChauveau/diving-anki/releases/download/vX.Y.Z/diving-fr.apkg
```

C’est cette adresse que Deck Manager enregistre. Le lien
[latest](https://github.com/NayanChauveau/diving-anki/releases/latest/download/diving-fr.apkg)
en tête de page suit la dernière publication réussie. Si un contrôle échoue, aucune
nouvelle version n’est publiée.

`git push origin main` envoie le dépôt sur GitHub et lance cette publication.
`make push` importe le deck dans Anki sur la machine locale.

## Licence

- Code, modèles, tests et automatisation : [MIT](LICENSE).
- Contenu des cartes : [CC BY-SA 4.0](LICENSE-CONTENT).

Les cartes peuvent être partagées et adaptées, avec attribution. Une adaptation du
contenu reste sous CC BY-SA 4.0. Les documents sources privés ne sont pas distribués
avec le dépôt.
