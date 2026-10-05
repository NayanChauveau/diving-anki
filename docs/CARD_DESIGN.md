# Concevoir des cartes pertinentes

Calibration convenue avec l’utilisateur le 5 octobre 2026. À appliquer à tous les niveaux,
au plan de préparation et à chaque lot de cartes, en complément de CONTENT_GUIDELINES.md.

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

Le plan actuel et son audit sont dans IMPLEMENTATION_N2.md et reviews/PREPARATION_GLOBALE.md.
Les objectifs fusionnés restent des précisions à intégrer, pas une liste de cartes à recréer.

## Formulation directe et couverture des restrictions

Éviter les préambules « selon le MFT… » répétés sur les rectos. Les sources et versions sont
conservées dans review.sources ; le contexte qui conditionne la réponse reste visible.
Quand une explication évoque d’autres limites, préciser leurs valeurs et vérifier les cartes
qui les interrogent. Ne pas ajouter de doublon si ces cartes existent déjà.
