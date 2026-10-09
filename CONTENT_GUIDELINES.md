# Règles de contenu

Le deck prépare la théorie de plongée N2 en français ; N3 est réalisé et N4
est prévu pour la suite. Les sources convenues, leur périmètre et les vérifications nécessaires
sont dans les plans [N2](docs/IMPLEMENTATION_N2.md) et [N3](docs/IMPLEMENTATION_N3.md).
Ne pas inventer de programme ni de procédure.

La [grille de qualité des cartes](docs/STUDY_CARD_QUALITY.md), adaptée du WSET3,
fait partie des règles de publication : **ISOLATION, CREDIBILITY, LENGTH, WHY, SENSE**.
Une seule défaillance exige une réécriture, même si la bonne réponse est exacte.
Chaque leurre doit correspondre à une confusion plausible dans le cadre du recto ;
le corrigé doit expliquer la distinction sans recopier systématiquement la clé.
Documenter pour chaque leurre son attrait et sa réfutation précise. Une clé seule
prudente face à deux imprudences, une inversion grossière ou un choix hors sujet
échoue au contrôle : reconstruire aussi le recto si nécessaire, au même objectif.
Ne jamais renvoyer à la lettre ou au numéro d’un choix : l’ordre peut changer.
Consigner une passe pédagogique distincte du contrôle factuel avant `reviewed`.

Rédiger des formulations originales depuis les sources fournies. Conserver une référence
vérifiable dans `review.sources` et, si utile, `source_id`. Une question teste une notion
précise et contient tout le contexte nécessaire. Pour les QCM : une seule bonne réponse,
distracteurs plausibles et explication qui expose le raisonnement.

Vérifier les unités, hypothèses de calcul, limites des règles et dates des références
réglementaires. Les éléments médicaux et de sécurité exigent une vérification attentive
contre les sources. Le statut `reviewed` résulte d’une revue, jamais du seul passage des tests.
Les cartes sont des aides à la révision, à utiliser avec la formation pratique encadrée.

## Format des cartes — calibration finale du 6 octobre 2026

Le **QCM est le format à choisir dès que la question peut être posée clairement avec
une réponse vraie unique et des distracteurs crédibles**. Cela vaut aussi pour les
calculs, les schémas, les cas et les séquences. Ne pas réserver automatiquement ces
familles à la réponse libre, ni viser un pourcentage fixe de cartes ouvertes.
Tout autre format est possible s’il convient mieux à la tâche ; justifier ce gain
précis carte par carte dans la revue. « C’est un calcul » ou « pour répondre sans
indices » ne suffisent pas à écarter un QCM réalisable et pertinent.
Ne pas fabriquer des distracteurs absurdes : revoir les choix, puis le recto si
nécessaire. Comparer des réponses de même nature et de longueur voisine, sans indice
lexical ni réponse correcte seule prudente. La difficulté vient du cours, pas du flou.
Relire séparément **chaque** choix et son explication : une alternative qui décrit
la même erreur que la bonne réponse peut elle aussi être vraie. Une question qui
demande une cause appelle des causes ; une question qui demande une action appelle
des actions. Retirer aussi les labels d’un schéma qui donnent déjà la réponse.
Une conversion conserve l’objectif et l’ID ; pour une Basic publiée, garder
`anki_model: basic` afin de préserver modèle, carte et historique lors de l’import.


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
