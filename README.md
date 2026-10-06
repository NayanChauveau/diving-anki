# Anki — Théorie de plongée

Un deck Anki en français pour réviser la théorie du **niveau 2 de plongée**, dans le cadre
français et du cursus FFESSM : réglementation, physique, prévention des accidents,
désaturation, matériel et préparation de la plongée.

Le deck N2 comprend **308 cartes revues** : 308 QCM à réponse unique,
avec des explications, des cas concrets et des exercices de calcul. Il peut être téléchargé
et utilisé directement dans Anki. Le dépôt contient aussi les sources des cartes et les
outils permettant de les vérifier, de les modifier et de construire les paquets.

**[Télécharger le catalogue complet](https://github.com/NayanChauveau/diving-anki/releases/download/latest-main/diving-fr.apkg)**
· [Voir la dernière build publiée](https://github.com/NayanChauveau/diving-anki/releases/tag/latest-main)
· [Toutes les versions](https://github.com/NayanChauveau/diving-anki/releases)

## Sommaire

- [Installer le deck sans outils de développement](#installer-le-deck-sans-outils-de-développement)
- [Réviser avec le deck](#réviser-avec-le-deck)
- [Mettre à jour et conserver sa progression](#mettre-à-jour-et-conserver-sa-progression)
- [Contenu et niveaux disponibles](#contenu-et-niveaux-disponibles)
- [Construire le deck depuis les sources](#construire-le-deck-depuis-les-sources)
- [Importer et synchroniser avec AnkiConnect](#importer-et-synchroniser-avec-ankiconnect)
- [Contribuer ou signaler une erreur](#contribuer-ou-signaler-une-erreur)
- [Organisation du dépôt](#organisation-du-dépôt)
- [Builds et releases](#builds-et-releases)
- [Licences](#licences)

## Installer le deck sans outils de développement

Il suffit d’Anki et du fichier `.apkg`. Aucun clonage du dépôt, Python, terminal ou
module complémentaire n’est nécessaire pour cette installation.

1. Installer **[Anki Desktop](https://apps.ankiweb.net/)** sur son ordinateur.
2. Télécharger **[diving-fr.apkg](https://github.com/NayanChauveau/diving-anki/releases/download/latest-main/diving-fr.apkg)**
   pour le catalogue complet N2/N3/N4.
   Sur la page de release, le fichier se trouve dans **Assets**. Les archives
   **Source code** contiennent le dépôt, pas le deck prêt à importer.
3. Ouvrir Anki, puis choisir **Fichier → Importer** et sélectionner le fichier `.apkg`.
4. Confirmer l’import. Le deck apparaît sous **Plongée**, avec ses cinq catégories.
5. Ouvrir **Plongée** pour réviser l’ensemble, ou une catégorie pour travailler un thème.
   Pour cibler un niveau dans le catalogue complet, suivre le guide ci-dessous.

Le lien de téléchargement conserve le même nom et pointe vers la dernière build publiée
avec succès depuis la branche `main`.

### Réviser aussi sur téléphone ou sur un autre ordinateur

Après l’import sur ordinateur, connecter le profil Anki à un compte
**[AnkiWeb](https://ankiweb.net/)**, puis lancer **Synchroniser**. Utiliser le même compte
sur les autres appareils et y synchroniser également.

Les applications mobiles sont **AnkiMobile** sur iPhone/iPad et **AnkiDroid** sur Android ;
leurs liens officiels figurent sur la [page de téléchargement d’Anki](https://apps.ankiweb.net/).
Les cartes et la progression se synchronisent entre les appareils.
Voir le [guide officiel de synchronisation](https://docs.ankiweb.net/syncing.html) pour
la configuration initiale et les choix de synchronisation.

### Si le téléchargement ou l’import ne fonctionne pas

- **La page de release ne montre pas les fichiers :** ouvrir la rubrique **Assets**, ou
  utiliser le lien direct vers `diving-fr.apkg` ci-dessus.
- **Le fichier téléchargé est un ZIP :** télécharger le `.apkg` plutôt que l’archive des sources.
- **Le fichier n’est pas disponible :** le nouveau paquet unique sera disponible après la
  prochaine publication réussie ; les anciennes releases conservaient des paquets par niveau.
- **Anki refuse le fichier :** utiliser une version récente de l’application officielle
  et télécharger à nouveau le paquet. Le
  [manuel d’import Anki](https://docs.ankiweb.net/importing/packaged-decks.html) décrit les options disponibles.

## Réviser avec le deck

Pour les calculs, refaire le raisonnement et vérifier les unités avant de choisir une
proposition, puis comparer sa méthode à la solution détaillée.

Les QCM comportent **une seule bonne réponse**. L’ordre des choix est mélangé lors des
révisions ; le verso indique la réponse et explique le raisonnement. On peut sélectionner
un choix, puis afficher la réponse si elle ne s’ouvre pas automatiquement sur l’application utilisée.

Après la correction, évaluer son rappel avec les boutons d’Anki. La sélection d’un choix
ne note pas automatiquement la carte : c’est cette évaluation qui programme la prochaine
révision. Le [guide d’étude Anki](https://docs.ankiweb.net/studying.html) explique ces boutons.

Le deck accompagne les cours et la formation pratique. Les cartes précisent le contexte
quand la réponse dépend du pays, du cursus, de l’âge, d’un modèle de matériel ou des
hypothèses d’un exercice.

### Passer de N2 à N3 ou N4

Une connaissance commune est **une seule note**, portant plusieurs tags, par exemple
`level::N2`, `level::N3` et `level::N4`. Importer une nouvelle version du paquet dans la même collection
conserve ses échéances et ses révisions ; seules les connaissances nouvelles créent de nouvelles notes.
Les niveaux sont attribués explicitement après revue : aucune inclusion automatique de tout N2 en N3/N4.

Dans **Parcourir**, `tag:diving-theory tag:level::N4` montre les cartes utiles au N4.
Pour les réviser au rythme normal, créer un **paquet filtré** avec
`tag:diving-theory tag:level::N4 (is:due or is:new)` et conserver l’option de reprogrammation
selon les réponses. Les cartes communes ne sont reprises que lorsqu’elles sont dues.
Le [guide de la collection partagée](docs/SHARED_COLLECTION.md) détaille l’usage et la migration.
Le [manuel Anki](https://docs.ankiweb.net/filtered-decks.html) décrit les paquets filtrés.

## Mettre à jour et conserver sa progression

1. Télécharger à nouveau `diving-fr.apkg` depuis la dernière build publiée.
2. L’importer **dans la même collection Anki**, sans supprimer le deck existant.
3. Synchroniser ensuite les appareils utilisés.

Les identifiants des cartes publiées et des modèles sont stables. Anki peut ainsi reconnaître
les notes déjà importées, mettre à jour leur contenu et ajouter les nouvelles cartes,
tout en conservant l’historique et les échéances des cartes existantes. Les options d’import
et les modifications personnelles apportées aux notes ou aux modèles peuvent influencer
la mise à jour ; voir le [manuel officiel](https://docs.ankiweb.net/importing/packaged-decks.html#updating).

### Ancienne installation sous Plongée → N2

Les identités des notes N2 sont conservées. L’import ne garantit pas le déplacement des
cartes déjà présentes vers les catégories communes : suivre le
[guide de migration](docs/SHARED_COLLECTION.md#migrer-une-installation-n2-existante).
Le déplacement conserve les notes et leur progression.

### Cartes fusionnées ou retirées dans une nouvelle version

**Un import `.apkg` ne supprime ni ne suspend automatiquement les anciennes cartes absentes
du nouveau paquet.** Une ancienne installation peut donc conserver plus de 308 cartes.

La [revue finale N2](docs/reviews/REVUE_FINALE_N2.md#fusions--aucun-objectif-utile-abandonné)
indique les questions fusionnées et leurs remplacements. Si elles figurent encore dans
sa collection, les retrouver dans **Parcourir** et les suspendre. Elles restent consultables
avec leur historique, mais ne reviennent plus dans les révisions.
Les identifiants réservés sont conservés dans le [registre des retraits](docs/reviews/RETIREMENTS_N2.yaml).
Une première installation du paquet actuel contient uniquement les 308 cartes actives.

## Contenu et niveaux disponibles

Le fichier unique **`diving-fr.apkg`** contient les cartes revues de tous les niveaux.
Le build actuel contient **308 notes uniques** : 308 cartes N2, dont **164 partagées avec N3**.
Le N3 reste **en cours de réalisation** : ces reprises couvrent le socle commun, pas encore
les connaissances spécifiques du niveau. Aucune carte N4 n’est encore incluse.
Les nouveaux contenus validés rejoindront ce même fichier ; les reprises conservent leur
identité et leur historique. La release en ligne reflète le dernier push ayant réussi la CI.

Le [plan détaillé de préparation N3](docs/IMPLEMENTATION_N3.md) décrit les sources,
les objectifs, les reprises du N2 et les vérifications avant rédaction.

Les cartes sont regroupées dans cinq sous-decks directement sous `Plongée`, communs aux niveaux :

| Catégorie | Cartes | Thèmes |
| --- | ---: | --- |
| Réglementation | 52 | Prérogatives, âges, organisation, équipements requis, documents et environnement |
| Physique | 82 | Pressions, flottabilité, compression des gaz, consommation et autonomie |
| Prévention des accidents | 53 | Barotraumatismes, essoufflement, froid et narcose |
| Désaturation | 77 | Mécanismes et accidents de désaturation, tables MN90, ordinateurs et remontées anormales |
| Matériel et préparation | 44 | Blocs, gonflage, détendeurs, pannes, orientation et préparation collective |

Les 18 chapitres restent identifiés dans les fichiers et les tags `chapitre::01` à
`chapitre::18`, sans multiplier les petits sous-decks dans Anki.

### Sources et qualité du contenu

Les formulations sont originales. Les supports pédagogiques sont recroisés avec des références
FFESSM, réglementaires, médicales et constructeurs selon le sujet. Les références et les
vérifications sont conservées dans les sources des cartes et dans `docs/reviews/`.

Un fait simple est interrogé une fois ; les raisonnements complexes reçoivent plusieurs
angles ou exercices utiles. Les cartes nouvelles restent en `draft` et sont exclues des
builds ordinaires jusqu’à leur revue factuelle et pédagogique.

- [Plan d’implémentation N2](docs/IMPLEMENTATION_N2.md).
- [Couverture des 334 objectifs suivis](docs/reviews/COUVERTURE_FINALE_N2.md).
- [Dernière revue intégrale et corrections](docs/reviews/REVUE_FINALE_N2.md).
- [Règles de contenu](CONTENT_GUIDELINES.md) et [guide de conception des cartes](docs/CARD_DESIGN.md).

## Construire le deck depuis les sources

Cette partie s’adresse aux personnes qui souhaitent modifier les cartes ou générer elles-mêmes
les paquets. Pour utiliser le deck publié, les étapes d’installation ci-dessus suffisent.

### Prérequis

- [Git](https://git-scm.com/).
- [Python 3.12 ou ultérieur](https://www.python.org/downloads/).
- [uv](https://docs.astral.sh/uv/getting-started/installation/).
- `make` pour les commandes courtes ; des équivalents directs sont donnés ci-dessous.

```sh
git clone https://github.com/NayanChauveau/diving-anki.git
cd diving-anki
uv sync --extra dev
make check
make build
```

Le paquet complet est écrit dans `dist/diving-fr.apkg`. Il peut être importé manuellement
dans Anki comme le paquet téléchargé. Les documents sources privés ne sont pas nécessaires
à la construction du deck depuis les YAML.

### Commandes utiles

| Commande | Fonction |
| --- | --- |
| `make check` | Lint, formatage, types, schéma, validation des cartes et tests |
| `make build` | Construire le catalogue complet (`diving-fr.apkg`) |
| `make build-all` | Alias de `make build` : le même paquet unique |
| `make push` | Construire le catalogue complet, l’importer et synchroniser AnkiWeb |
| `uv run diving-anki validate` | Valider uniquement les fichiers de cartes |
| `make schema` | Régénérer le schéma après une modification du modèle de données |

Sans `make`, depuis la racine du dépôt :

```sh
uv run diving-anki check
uv run diving-anki build --out dist
```

Pour une prévisualisation éditoriale incluant les brouillons :

```sh
uv run diving-anki build --include-drafts --out dist
```

## Importer et synchroniser avec AnkiConnect

`make push` automatise le build, l’ouverture d’Anki Desktop lorsque possible, l’import du
paquet et la synchronisation AnkiWeb. **AnkiConnect est nécessaire uniquement pour ce
workflow automatique**, pas pour importer un fichier `.apkg` manuellement.

### Configuration initiale

1. Installer [Anki Desktop](https://apps.ankiweb.net/) et connecter le profil voulu à AnkiWeb.
2. Ouvrir **Outils → Greffons / Extensions → Télécharger des greffons** dans Anki.
3. Saisir le code **`2055492159`**, correspondant à
   [AnkiConnect](https://ankiweb.net/shared/info/2055492159).
4. Redémarrer Anki pour charger le module.

Puis, depuis la racine du dépôt :

```sh
make push
```

Ou directement :

```sh
uv run diving-anki push --out dist
```

La synchronisation porte sur **tout le profil Anki actif**. Ouvrir le profil et le compte
souhaités avant la commande, et résoudre dans Anki les éventuelles demandes de synchronisation
à sens unique. La commande ne gère pas les suspensions de cartes retirées : suivre la section de mise à jour.

Par défaut, AnkiConnect est contacté sur `http://127.0.0.1:8765`. Une installation personnalisée
peut utiliser les variables `ANKI_CONNECT_URL` et `ANKI_CONNECT_KEY`.
Pour ouvrir Anki soi-même avant l’import :

```sh
uv run diving-anki push --out dist --no-launch
```

### Dépannage AnkiConnect

- **Connexion impossible :** vérifier l’installation du module, redémarrer Anki et le laisser ouvert.
- **Ouverture automatique impossible :** ouvrir Anki manuellement, puis relancer avec `--no-launch`.
- **Échec de synchronisation :** vérifier le compte du profil actif et terminer les éventuelles
  demandes de confirmation ou de résolution de conflit dans Anki.
- **Endpoint personnalisé :** vérifier `ANKI_CONNECT_URL` et, si une clé est configurée,
  `ANKI_CONNECT_KEY`. Voir la [documentation AnkiConnect](https://github.com/FooSoft/anki-connect).

## Contribuer ou signaler une erreur

Une question imprécise, une réponse discutable ou un calcul incorrect peut être signalé
sans modifier le dépôt : **[ouvrir une issue](https://github.com/NayanChauveau/diving-anki/issues/new)**.
Indiquer le texte de la question, le thème, le problème constaté et, si possible, une source
ou une capture de la carte. Pour un problème d’import, préciser l’application et sa version.

Pour proposer une modification :

1. Lire [CONTRIBUTING.md](CONTRIBUTING.md), [CONTENT_GUIDELINES.md](CONTENT_GUIDELINES.md)
   et [docs/CARD_DESIGN.md](docs/CARD_DESIGN.md).
2. Créer une branche ou un fork et modifier le fichier de chapitre concerné.
3. Donner des formulations originales et des références vérifiables ; garder les documents privés hors Git.
4. Créer les nouvelles cartes en `draft`, puis documenter leur revue avant `reviewed`.
5. Conserver les IDs publiés et consulter le registre des retraits avant tout ajout.
6. Exécuter `make check`, construire le paquet et contrôler le rendu si le contenu change.
7. Ouvrir une pull request expliquant la modification, son intérêt et les vérifications réalisées.

Anki et AnkiConnect ne sont pas nécessaires pour modifier et valider les sources.

## Organisation du dépôt

Le socle technique reprend celui de `anki-deck-wset-3` : YAML, Pydantic, genanki,
Markdown, modèles Anki, mélange des choix QCM, AnkiConnect, Ruff, basedpyright, pytest,
schéma JSON, pre-commit et CI GitHub.

```text
cards/n2/              Cartes N2, un fichier YAML par chapitre
cards/n3/              Emplacement prévu pour les cartes N3
cards/n4/              Emplacement prévu pour les cartes N4
docs/                  Plan, conception, schémas et revues de contenu
sources/               Documents privés, ignorés par Git
src/diving_anki/        Validation, rendu, génération et import AnkiConnect
templates/             Modèles HTML/CSS/JavaScript et libellés français
schema/                Schéma JSON généré pour les YAML
tests/                 Contrôles des formats, niveaux et paquets Anki
.github/workflows/     Vérifications, builds et publication des releases
dist/                  Paquets générés localement, non committés
```

Les YAML sont la source de vérité. Une carte indique explicitement ses `levels`, par exemple
`[N2]` ou `[N2, N3]` : aucune inclusion automatique d’un niveau dans un autre.
Une carte possède un seul GUID Anki pour tous ses niveaux. Le paquet unique utilise les
mêmes identités et catégories à chaque mise à jour : les imports successifs retrouvent
la note existante et son historique. Les GUIDs N2 déjà publiés sont conservés.
Les GUIDs des notes et les IDs des modèles et decks sont déterministes et distincts de ceux du projet WSET.

Le générateur prend en charge `basic`, `mcq` et `cloze` ; le contenu N2 actuel utilise
les deux premiers formats. Les éditeurs YAML peuvent utiliser `schema/cards.schema.json`
pour la validation. Après une modification de `src/diving_anki/schema.py`, régénérer
et committer le schéma avec `make schema`.

## Builds et releases

Les pull requests et pushes passent les contrôles complets et construisent le paquet unique `diving-fr.apkg`
dans GitHub Actions. Les brouillons sont exclus des builds ordinaires.

Chaque push réussi sur `main` met à jour la release **Latest main build**, portant le tag
`latest-main`, et remplace ses fichiers `.apkg`. C’est la version utilisée par le lien de
téléchargement en tête de ce README. Si un contrôle ou un build échoue, ce workflow ne publie
pas de nouveau paquet : le téléchargement reste celui de la dernière publication réussie.

Un tag `vX.Y.Z` déclenche une release versionnée distincte. La release `latest-main` est
mobile ; les releases versionnées servent de points de référence séparés.

`git push origin main` publie les commits du dépôt sur GitHub et déclenche la CI.
`make push` construit et importe le deck dans Anki local, puis synchronise AnkiWeb.
Ce sont deux destinations et deux workflows différents.

## Licences

- Code, modèles, tests et automatisation : **[MIT](LICENSE)**.
- Contenu des cartes : **[CC BY-SA 4.0](LICENSE-CONTENT)**.

Les cartes peuvent être partagées et adaptées avec attribution ; les adaptations de leur
contenu doivent conserver la licence CC BY-SA 4.0. Les documents sources privés ne sont
pas distribués avec le dépôt et ne sont pas couverts par cette licence.
