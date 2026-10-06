# Règles de contenu

Le deck prépare actuellement la théorie de plongée N2 en français ; N3 et N4 sont prévus
pour la suite. Les sources convenues, leur périmètre et les vérifications nécessaires sont
dans [le plan N2](docs/IMPLEMENTATION_N2.md). Ne pas inventer de programme ni de procédure.

Rédiger des formulations originales depuis les sources fournies. Conserver une référence
vérifiable dans `review.sources` et, si utile, `source_id`. Une question teste une notion
précise et contient tout le contexte nécessaire. Pour les QCM : une seule bonne réponse,
distracteurs plausibles et explication qui expose le raisonnement.

Vérifier les unités, hypothèses de calcul, limites des règles et dates des références
réglementaires. Les éléments médicaux et de sécurité exigent une vérification attentive
contre les sources. Le statut `reviewed` résulte d’une revue, jamais du seul passage des tests.
Les cartes sont des aides à la révision, à utiliser avec la formation pratique encadrée.

## Pertinence et répétition

Appliquer [la calibration de conception](docs/CARD_DESIGN.md). Un fait simple ne doit être
interrogé qu’une fois ; Anki assure les rappels. Pour les calculs et raisonnements complexes,
plusieurs angles et exemples sont utiles, ainsi qu’une courte série numérique pour pratiquer.
Consigner cet apport dans la revue du lot après comparaison avec tout le deck.
Fusionner les paraphrases de faits simples et éviter les longues séries numériques ; placer les précisions utiles
dans l’explication sans multiplier les objectifs sur un recto. La couverture prime sur le quota.

## Clarté

Poser les questions directement, sans préambule de source répété ; conserver le contexte
nécessaire à une réponse exacte. Sources et versions restent dans `review.sources`.
Donner une réponse courte et expliquer les termes techniques avec des mots concrets.
Une règle exacte mais incompréhensible ou apparemment contradictoire doit être reformulée.
Expliciter les restrictions évoquées et vérifier qu’elles sont couvertes par des objectifs
distincts ; ne pas recréer une carte déjà présente. Les exemples détaillés de calibration
(certification/exercice, paliers, calculs) sont dans [le guide](docs/CARD_DESIGN.md).

Les QCM doivent exiger la connaissance du cours : distracteurs crédibles et comparables,
issus de confusions précises. Éliminer les réponses absurdes et les indices de formulation.
Préférer trois choix solides à quatre choix dont un trop facile ; difficulté et véracité
se vérifient ensemble. Voir la grille de revue dans docs/CARD_DESIGN.md.

La difficulté ne doit pas provenir du flou. Chaque QCM demande une chose précise dans un
contexte explicite ; tous les choix répondent à cette même demande. Distinguer minimum imposé,
configuration possible et condition obligatoire pour éviter plusieurs réponses défendables.
