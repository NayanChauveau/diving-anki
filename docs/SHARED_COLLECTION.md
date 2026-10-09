# Une seule identité par connaissance, N2 comme base

La structure livrée utilise uniquement des paquets classiques :

```text
Plongée
├── N2 — 308 cartes
│   ├── Réglementation
│   ├── Physique
│   ├── Prévention des accidents
│   ├── Désaturation
│   └── Matériel et préparation
└── N3 — 118 compléments
    ├── Réglementation
    ├── Physique
    ├── Prévention des accidents
    ├── Désaturation
    └── Matériel et préparation
```

N3 suppose la base N2. Continuer les révisions N2 et apprendre les compléments N3.
Les catégories peuvent différer entre niveaux si les contenus futurs le demandent.
Le dossier Collection commune et les paquets filtrés sont abandonnés.

## Cartes partagées et progression

Chaque carte possède un ID YAML, une note Anki et un historique. `levels` indique
les programmes auxquels elle contribue, sans la copier. Le paquet physique correspond
au premier niveau présent, dans l’ordre N2, N3, N4. Ajouter N3 à une carte N2 ne la déplace
pas et ne recrée pas sa note. Son ID reste identique même s’il commence par `n2-`.
Le sel historique fixe `N2` dans `note_guid()` est permanent pour tous les niveaux.

Le fichier unique `diving-fr.apkg` contient 426 notes : 308 en N2 et 118 en N3.
Le programme N3 comporte 322 connaissances, dont 204 présentes dans N2. Le dossier N3
seul contient donc les compléments, pas tout le programme. Pour voir le programme
complet dans Parcourir : `tag:diving-theory tag:level::N3`.
Aucune carte N4 n’est actuellement incluse. N4 suivra cette logique de complément.

## Réglages fournis par le dépôt

`config/study.json` définit un préréglage propre à Plongée : 10 nouvelles cartes
par jour et par paquet, et une limite de 200 révisions dues. Les révisions dues
peuvent donc s’ajouter aux dix nouvelles cartes ; il s’agit des limites quotidiennes
classiques d’Anki, pas de lots de dix à reconstruire.
Le préréglage est embarqué dans le `.apkg`, avec des paquets ordinaires (`dyn=0`).
À l’import, activer l’import des préréglages de paquet pour recevoir ces réglages.
Si cette option est désactivée, les options de la collection destinataire s’appliquent.
Les options du paquet parent interviennent également dans les limites lorsque l’on
révise le parent. Le préréglage Default des autres paquets n’est pas modifié.

Tout est versionné et généré depuis le dépôt. Aucun paquet filtré, configuration
manuelle locale ou manipulation de l’interface Anki ne fait partie du workflow.
`make push` importe via AnkiConnect puis synchronise avec AnkiWeb, comme WSET 3.
Il ne déplace pas les cartes ni ne réécrit les options après import. L'arborescence
et les limites du dépôt sont embarquées dans le paquet. Le GUID, le modèle et les
IDs des cartes existantes restent identiques.

## Migrer une installation N2 existante

Importer le nouveau `.apkg` dans la même collection, sans supprimer les notes.
`make push` ne migre plus automatiquement l’ancienne structure. Un import seul ne garantit pas le déplacement
des cartes déjà importées ; cette limite des mises à jour concerne les anciennes
installations, pas une première installation du paquet actuel.

La migration des paquets filtrés de l’organisation temporaire a été réalisée séparément.
Toute nouvelle migration doit conserver les échéances, suspensions et révisions,
et ne retirer que des paquets vides. Elle ne fait pas partie du push courant.

Les anciennes revues décrivent l’organisation à leur date ; ce guide fait référence
pour la structure actuelle. Une Basic convertie en QCM conserve `anki_model: basic`,
ses deux champs et son identité, comme décrit dans la revue QCM.
