# Concevoir des cartes pertinentes

Calibration convenue avec l’utilisateur le 5 octobre 2026. À appliquer à tous les niveaux,
au plan de préparation et à chaque lot de cartes, en complément de [CONTENT_GUIDELINES.md](../CONTENT_GUIDELINES.md).

## Décider si une carte mérite d’exister

Un fait simple reçoit une carte : Anki assure sa répétition au fil des révisions.
Ne pas ajouter une carte inverse, une paraphrase ou un faux scénario pour redemander
la même information. Une précision secondaire peut figurer dans l’explication.
Le nombre de cartes n’est jamais un objectif de production.

Un sujet complexe peut recevoir plusieurs cartes si chacune exige un raisonnement distinct :
relation physique, calcul direct, calcul inverse, conversion, erreur de modèle,
lecture de données, combinaison de phases ou décision avec une contrainte supplémentaire.
Changer seulement les nombres ou le nom du plongeur ne suffit pas. Plusieurs exemples sont
bienvenus quand leurs hypothèses ou leurs difficultés diffèrent réellement.

Avant chaque nouvelle carte, rechercher les objectifs voisins dans tout le catalogue et les YAML,
y compris les autres chapitres. Écrire dans la revue du lot une phrase précisant son apport.
Si cette phrase décrit le même fait ou la même opération qu’une autre carte, fusionner.
Conserver la correspondance des IDs ; ne jamais recycler un ID publié pour un autre objectif.
Une fusion dans le plan ne déclenche pas automatiquement une suppression dans Anki.

## Exemples de calibration

| Famille | Carte utile | Variante à absorber |
| --- | --- | --- |
| Aptitudes N2 | Une question rappelant l’articulation PA20 / PE40, contexte réglementaire précisé | Redemander séparément le sens des sigles ou substituer une profondeur inférieure à la limite |
| Prérogatives en situation | Décider avec des aptitudes différentes dans la palanquée ou distinguer certification et exercice | Reposer la définition en ajoutant seulement le nom d’un plongeur |
| Pressions | Calcul absolu, problème inverse, confusion absolu/relatif, rapport près de la surface | Une série de profondeurs testant exactement la même substitution |
| Gaz | Stock utilisable, débit à profondeur donnée, besoin de deux équipiers, somme de phases | Plusieurs blocs ne changeant que le résultat arithmétique |
| Accidents | Mécanisme, reconnaissance contextualisée, prévention et priorité de réponse | Une carte par mot d’une liste de symptômes ou un scénario redemandant la même alerte |
| Matériel | Lire une inscription ou expliquer une fonction dans un modèle défini | Isoler chaque libellé d’une inscription dans une carte de vocabulaire |

## Rédiger sans surcharger

Une carte vise une tâche précise et tient seule. Fusionner des doublons ne signifie pas
empiler plusieurs questions indépendantes sur un recto. Réponse courte ; les précisions,
limites et erreurs fréquentes appartiennent à l’explication. Pour les signes d’accident,
préférer de courts cas à des listes exhaustives à réciter ; vérifier séparément la couverture.

Pour un calcul, annoncer les unités, le modèle et les données nécessaires. Distinguer
litres ambiants, volume ramené surface, pression absolue et pression de bloc. Donner
explicitement toute réserve utilisée ; ne pas en faire une règle universelle. Un modèle
à profondeur constante ou à phases fictives ne constitue pas un plan réel de plongée.
Vérifier le résultat par une résolution distincte, avec contrôle des unités et de la cohérence.

## Véracité et revue

Vérifier question, réponse, explication et distracteurs. En cas de doute, retrouver et recroiser
les références pertinentes. Pour réglementation, sécurité et médecine, contrôler la source
primaire actuelle, sa version et son champ d’application. Une absence de source ou une
contradiction non résolue bloque le statut `reviewed` ; l’audit pédagogique ne les résout pas.

Dans la revue de chaque lot, consigner : objectif/ID, apport distinct, source précise,
contrôles factuels, doublons absorbés et limites restantes. Les connaissances allant au-delà
du minimum N2 restent bienvenues lorsqu’elles aident à comprendre ; ne pas leur attribuer
une nouvelle prérogative ou une procédure non étayée.

Consulter [le plan actuel](IMPLEMENTATION_N2.md) et [son audit](reviews/PREPARATION_GLOBALE.md).
Les objectifs fusionnés restent des précisions à intégrer, pas une liste de cartes à recréer.

## Formulation directe et couverture des restrictions

Éviter les préambules « selon le MFT… » répétés sur les rectos. Les sources et versions sont
conservées dans review.sources ; le contexte qui conditionne la réponse reste visible.
Quand une explication évoque d’autres limites, préciser leurs valeurs et vérifier les cartes
qui les interrogent. Ne pas ajouter de doublon si ces cartes existent déjà.

## Réponse compréhensible et portée de la règle

Une réponse correcte doit aussi faire comprendre la règle. Ne pas laisser une expression
abstraite inexpliquée ni suggérer une contradiction entre deux conditions.

- Certification et exercice : expliquer les compétences attestées et les possibilités effectives
  avant l’âge d’exercice. Distinguer qualification isolée et brevet regroupant des qualifications.
- Paliers : préférer « plongée prévue sans palier de décompression obligatoire » ; expliquer
  que l’ordinateur ou les tables déterminent les paliers. Ne pas laisser croire qu’une restriction
  de planification permet d’ignorer un palier devenu obligatoire.
- Conditions liées : donner leurs valeurs dans l’explication et vérifier les objectifs de rappel.
  Le nombre de plongées, l’intervalle et une limite de profondeur conditionnelle sont des faits
  distincts ; la règle « un fait, une carte » ne demande pas de les supprimer ou de tout empiler.

Relire les questions entières, y compris leurs lignes de continuation dans le YAML,
pour repérer les préambules et termes abstraits restants. Vérifier aussi les réponses,
explications et autres formats (`basic`, `cloze`), pas seulement les QCM.

## QCM exigeants : qualité des distracteurs

Chaque question doit demander une connaissance spécifique : un nom déductible de sa seule
formulation ou trois alternatives absurdes ne constituent pas un test utile. Pour un document,
interroger une obligation précise, les informations requises ou une distinction avec les autres
documents plutôt que décrire son nom. Pour une règle, opposer des conditions proches ; pour un
équipement, opposer des configurations crédibles ou des fonctions voisines.

Construire les distracteurs depuis des erreurs identifiables : DP/guide, prévision/réalisation,
qualification/exercice, matériel individuel/collectif, deuxième étage/détendeur complet,
condition de profondeur ou d’organisation. Garder les choix comparables en longueur et précision.
Éviter la réponse correcte seule détaillée, seule prudente ou seule positive, et les absolus
ajoutés uniquement aux mauvaises réponses pour les rendre faciles à éliminer.

Avant validation, faire une passe en lecteur sans connaissances de plongée : peut-il répondre
par bon sens, par répétition des mots du recto ou par différence de style ? Refaire le QCM
si oui. Trois choix crédibles valent mieux que quatre dont un est de remplissage.
Les faits chiffrés restent des objectifs de mémorisation : choisir des valeurs plausibles ;
ne pas ajouter de complexité artificielle ni transformer le rappel en longue énigme.
Une seule réponse incontestable dans le contexte donné reste obligatoire.
