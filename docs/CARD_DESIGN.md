# Concevoir des cartes pertinentes

Calibration convenue avec l’utilisateur le 5 octobre 2026. À appliquer à tous les niveaux,
au plan de préparation et à chaque lot de cartes, en complément de [CONTENT_GUIDELINES.md](../CONTENT_GUIDELINES.md).

Depuis le 9 octobre 2026, appliquer aussi [STUDY_CARD_QUALITY.md](STUDY_CARD_QUALITY.md),
adapté de la passe qualité du WSET3. Ce document détaille les cinq critères de rejet,
les exemples et le brief de critique. La conception ci-dessous prépare les objectifs ;
la grille contrôle chaque question, chaque choix et chaque corrigé avant publication.
Une revue factuelle réussie ne valide pas à elle seule la qualité pédagogique.

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


## Décider si une carte mérite d’exister

Un fait simple reçoit une carte : Anki assure sa répétition au fil des révisions.
Ne pas ajouter une carte inverse, une paraphrase ou un faux scénario pour redemander
la même information. Une précision secondaire peut figurer dans l’explication.
Le nombre de cartes n’est jamais un objectif de production.

Un sujet complexe peut recevoir plusieurs cartes si chacune exige un raisonnement distinct :
relation physique, calcul direct, calcul inverse, conversion, erreur de modèle,
lecture de données, combinaison de phases ou décision avec une contrainte supplémentaire.
Une courte série de calculs avec des valeurs différentes est utile pour pratiquer la méthode,
même sans nouvelle opération à chaque carte : profondeurs rondes et intermédiaires, résultats
entiers et décimaux, calcul direct et inverse. Cette préférence a été précisée le 6 octobre 2026.
Éviter les longues séries mécaniques ; garder aussi des exercices aux hypothèses différentes.

Avant chaque nouvelle carte, rechercher les objectifs voisins dans tout le catalogue et les YAML,
y compris les autres chapitres. Écrire dans la revue du lot une phrase précisant son apport.
Si cette phrase décrit le même fait simple qu’une autre carte, fusionner. Pour les calculs,
conserver les applications supplémentaires utiles à l’entraînement, même avec la même opération.
Conserver la correspondance des IDs ; ne jamais recycler un ID publié pour un autre objectif.
Une fusion dans le plan ne déclenche pas automatiquement une suppression dans Anki.

## Exemples de calibration

| Famille | Carte utile | Variante à absorber |
| --- | --- | --- |
| Aptitudes N2 | Une question rappelant l’articulation PA20 / PE40, contexte réglementaire précisé | Redemander séparément le sens des sigles ou substituer une profondeur inférieure à la limite |
| Prérogatives en situation | Décider avec des aptitudes différentes dans la palanquée ou distinguer certification et exercice | Reposer la définition en ajoutant seulement le nom d’un plongeur |
| Pressions | Calcul absolu, problème inverse, confusion absolu/relatif, rapport près de la surface | Une longue série sans progression ; garder quelques profondeurs variées pour pratiquer |
| Gaz | Stock utilisable, débit à profondeur donnée, besoin de deux équipiers, somme de phases | Une longue série de blocs sans progression ; garder quelques calculs variés |
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

## Explications sans commentaires éditoriaux

Préférence de l’utilisateur : expliquer directement la connaissance, avec des phrases utiles
et courtes. Supprimer les formules « cette carte ne remplace pas… », « cette carte ne prescrit
pas… », « cette carte n’enseigne pas… » et les disclaimers génériques. Les précautions de méthode,
les limites de validation et les sujets non traités restent dans la revue interne.
Une condition factuelle qui détermine la réponse reste expliquée ; ne pas la transformer
pour autant en avertissement ou commentaire sur la carte. Cette règle s’applique à tous les formats.

## Difficulté sans incertitude — calibration du 6 octobre 2026

Le recto expose une situation déterminée et demande une chose précise. La difficulté vient
du savoir à mobiliser, pas d’un contexte manquant, d’une phrase abstraite ou d’un choix hors sujet.
Avant validation, reformuler mentalement la question puis examiner chaque choix avec exactement
les mêmes hypothèses. Si deux choix peuvent être vrais selon une lecture raisonnable, corriger.

- Distinguer « permis », « conforme », « obligatoire » et « minimum exigé ». Un équipement
  supplémentaire possible ou un médecin plus spécialisé ne devient pas faux par sa présence.
- Donner la plage complète demandée pour un effectif ; ne pas opposer une plage à une valeur
  incluse dans cette plage sans préciser que l’on demande l’ensemble des effectifs permis.
- Garder le même objet dans tous les choix : un seuil de profondeur appelle des seuils, une
  fonction appelle des fonctions, une exigence minimale appelle des exigences minimales.
- Expliciter les sujets : qui fournit le matériel, qui le porte, à qui s’applique la restriction,
  et quels équipements sont communs ou personnels. Développer le vocabulaire technique utile.
- Mettre les nombres et cas d’application utiles dans l’explication ; retirer les détours qui
  empêchent de comprendre pourquoi le bon choix est vrai et les autres faux.
- Si la clarté rend les mauvais choix trop évidents, reconstruire des distracteurs plausibles.
  Ne jamais réintroduire du flou pour rendre la question difficile.

La première passe de clarté sur 53 cartes est consignée dans reviews/CLARTE_GLOBALE.md.
La dernière revue de l’ensemble du N2 est dans [reviews/REVUE_FINALE_N2.md](reviews/REVUE_FINALE_N2.md).
