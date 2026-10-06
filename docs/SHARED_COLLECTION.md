# Une collection partagée entre N2, N3 et N4

Une connaissance correspond à un ID YAML, une note Anki et un historique dans une même
collection. Ses niveaux sont des appartenances, pas des copies.

```yaml
levels: [N2, N3, N4]
```

Le fichier unique **`diving-fr.apkg`** contient chaque note revue une fois, pour tous
les niveaux N2/N3/N4. Une carte pertinente pour les trois niveaux porte les trois tags
`level::N2`, `level::N3`, `level::N4`. Il n’existe plus d’export séparé par niveau.

Une personne qui prépare directement N4 utilise les cartes portant `level::N4`.
Une personne qui a déjà appris N2 retrouve les mêmes notes communes lorsqu’elle passe
au N4 : leur historique et leurs échéances restent en place. Les nouvelles connaissances
créent seules de nouvelles notes. Cela suppose les mises à jour dans la même collection,
avec les modèles et identifiants du projet conservés.
Les [options d’import Anki](https://docs.ankiweb.net/importing/packaged-decks.html) déterminent
la mise à jour du contenu ; choisir la mise à jour des notes pour recevoir les tags ajoutés.

## Arborescence

```text
Plongée
├── Collection commune
│   └── Les cinq catégories contenant les cartes originales
├── N2
│   └── Les cinq catégories comme paquets filtrés N2
└── N3
    └── Les cinq catégories comme paquets filtrés N3
```

Les cinq catégories actuelles sont Réglementation, Physique, Prévention des accidents,
Désaturation, Matériel et préparation. Elles peuvent différer entre niveaux si nécessaire ;
les trois dossiers racine Collection commune, N2 et N3 restent la structure commune. Les paquets filtrés se créent dans Anki,
pas dans le `.apkg`. Le dossier N2 conserve sa présentation, mais ses catégories
sont désormais des accès filtrés aux originaux de Collection commune.

Pour chaque catégorie, utiliser **Outils → Créer un paquet filtré**, nommer le
paquet `Plongée::N2::<catégorie>` ou `Plongée::N3::<catégorie>` et remplacer
les valeurs du filtre ci-dessous :

```text
"deck:Plongée::Collection commune::Réglementation" tag:level::N2 (is:due or is:new)
```

Conserver **Reprogrammer les cartes selon mes réponses** et **Créer/mettre à jour
même si vide**. Fixer une limite de séance (par exemple 20 cartes). Les révisions
dues et les nouvelles cartes sont accessibles sans anticiper les autres échéances.
Vider les catégories du niveau précédent avant de reconstruire celles du suivant.
Une carte partagée garde son ID et son échéance : elle ne peut pas être dans deux
paquets filtrés en même temps. Leurs compteurs affichent la séance chargée, pas
la taille totale du programme du niveau.

## Réviser seulement un niveau

Les catégories thématiques se trouvent sous `Plongée::Collection commune`. Une carte ne change
pas de catégorie lorsqu’elle devient pertinente pour un nouveau niveau.

Dans **Parcourir**, chercher :

```text
tag:diving-theory tag:level::N4
```

Pour étudier N4 au rythme normal, utiliser **Outils → Créer un paquet filtré** :

```text
tag:diving-theory tag:level::N4 (is:due or is:new)
```

Conserver l’option **Reprogrammer les cartes selon mes réponses** pour que les réponses
alimentent la progression normale. Régler la limite de cartes selon la séance voulue,
ou utiliser deux filtres pour distinguer les révisions dues et les nouvelles cartes.
Les cartes communes qui ne sont pas encore dues restent hors de la séance. Reconstruire
le paquet pour récupérer les cartes dues lors d’une nouvelle séance.

Avant de changer de niveau, vider le paquet filtré précédent pour rendre les cartes à
leurs catégories : une carte déjà dans un paquet filtré ne peut pas entrer dans un autre.
Les suspensions existantes restent respectées. Ces mécanismes sont décrits dans le
[manuel des paquets filtrés](https://docs.ankiweb.net/filtered-decks.html).

Le catalogue actuel contient 426 notes uniques : 308 N2 et 322 N3, dont
204 communes et 118 créations N3. Aucune carte N4 n’est encore incluse. Les nouvelles appartenances
sont ajoutées après revue explicite, sans héritage automatique de toutes les cartes N2.
Voir la [couverture N3](reviews/n3/COUVERTURE_N3.md).

## Migrer une installation N2 existante

Les GUIDs des notes N2 publiées sont conservés à l’identique. Le nouveau nom de deck
n’impose donc pas de refaire leur apprentissage. Le package ne garantit cependant pas
que les cartes déjà présentes changent automatiquement de deck lors de l’import.

1. Synchroniser les appareils avant la réorganisation et importer le nouveau package
   dans la collection existante.
2. Dans **Parcourir**, sélectionner les cartes de chaque ancienne catégorie et utiliser
   **Cartes → Changer de paquet** pour les placer dans la catégorie commune correspondante :

| Ancien paquet | Destination |
|---|---|
| `Plongée::N2::Réglementation` | `Plongée::Collection commune::Réglementation` |
| `Plongée::N2::Physique` | `Plongée::Collection commune::Physique` |
| `Plongée::N2::Prévention des accidents` | `Plongée::Collection commune::Prévention des accidents` |
| `Plongée::N2::Désaturation` | `Plongée::Collection commune::Désaturation` |
| `Plongée::N2::Matériel et préparation` | `Plongée::Collection commune::Matériel et préparation` |

Déplacer également les cartes installées directement sous `Plongée::<catégorie>`
vers `Plongée::Collection commune::<catégorie>`.

3. Inclure les anciennes cartes retirées qui sont restées suspendues : déplacer conserve
   leur suspension et leur historique. Les garder suspendues comme indiqué dans le registre
   des retraits. Les cartes personnelles étrangères au projet peuvent rester dans leur deck.
4. Vérifier sur les cartes déplacées : mêmes IDs de note/carte, échéances, intervalles,
   nombre de révisions et historique ; conserver le même préréglage de révision dans les
   destinations pour garder les paramètres d’étude.
5. Synchroniser la collection réorganisée. Les anciens paquets vides peuvent être retirés
   une fois leur contenu vérifié. Retirer les anciennes catégories vides sous N2 avant
   de créer les paquets filtrés de même nom ; conserver le dossier parent N2.
6. Créer les accès N2/N3 comme décrit dans [Arborescence](#arborescence).
   Reconstruire seulement le niveau choisi pour la séance.

Les anciennes revues du dépôt décrivent les destinations sous `Plongée::N2` utilisées
à leur date de réalisation. Le présent guide décrit la nouvelle organisation commune.

## Contrat technique permanent

- `note_guid(card_id)` utilise le sel historique fixe `N2` : ce choix préserve les notes
  publiées, même pour les cartes qui ne portent ensuite que N3/N4. Ce sel n’est pas un niveau
  pédagogique et ne dépend jamais de l’ordre ou du contenu de `levels`.
- Le seul export contient une fois chaque carte revue, avec tous ses tags de niveau.
- `prepare(..., "combined")` parcourt le catalogue une seule fois, sans dupliquer une carte qui possède plusieurs niveaux.
- Les cartes partagées conservent leur ID, même si celui-ci commence par `n2-`.
- Les modèles publiés et leurs templates restent identiques. Un changement de modèle
  exige une analyse distincte de la migration des notes.
- Les anciens GUIDs N3/N4 du prototype étaient différents. Aucun contenu N3/N4 n’avait
  été publié ; si une collection personnelle contient des essais de ce prototype, ils
  demandent une revue séparée. L’import ne fusionne pas automatiquement deux historiques.

## Changer le format d’une carte existante

Une Basic convertie en QCM conserve `anki_model: basic` dans son YAML. Le paquet met
à jour les deux champs existants avec les choix interactifs ; le modèle et la carte
Anki restent les mêmes. L’import est vérifié avec une collection d’essai contenant
historique, échéances et suspensions. Voir la [revue QCM](reviews/QCM_GLOBALE.md).
