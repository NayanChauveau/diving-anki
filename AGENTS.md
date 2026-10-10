# Instructions aux agents

Projet de théorie de plongée en français : N2 et N3 réalisés, structure prévue pour N4.
Avant de préparer ou rédiger des cartes, lire [CONTENT_GUIDELINES.md](CONTENT_GUIDELINES.md)
et [docs/CARD_DESIGN.md](docs/CARD_DESIGN.md), puis la
[grille de relecture qualité](docs/STUDY_CARD_QUALITY.md). Lire [CONTRIBUTING.md](CONTRIBUTING.md)
pour le workflow. Ces règles s’appliquent à toutes les cartes et tous les niveaux.

## Critères de qualité obligatoires — adaptation WSET3 du 9 octobre 2026

La référence de la passe pédagogique est [docs/STUDY_CARD_QUALITY.md](docs/STUDY_CARD_QUALITY.md).
Appliquer ses cinq critères à **chaque** carte : **ISOLATION, CREDIBILITY, LENGTH,
WHY, SENSE**. Un échec sur un seul critère impose une correction ; une réponse
factuellement exacte ne compense jamais un QCM facile à deviner.

- Pour chaque leurre, identifier une confusion crédible d’un candidat qui connaît
  imparfaitement le cours. Rejeter un choix hors cadre ou contradictoire avec le recto,
  même s’il contient une affirmation vraie dans une autre situation.
- La clé ne doit pas être dévoilée par les mots du recto, une légende, sa longueur,
  son style ou sa prudence. Ne pas remplacer un mauvais leurre par du remplissage.
- Le corrigé explique la distinction posée : mécanisme, hypothèse, erreur ou exemple
  vérifiable. Ne pas recopier systématiquement la clé ni renvoyer à « option B ».
- Relire le français comme un texte autonome ; réécrire les phrases abstraites ou
  incompréhensibles, pas seulement les mots isolés.
- Rédaction puis critique distincte, correction puis nouvelle critique des IDs rejetés.
  Lots d’au plus 40 cartes ; revue de toutes les cartes du chapitre, pas un échantillon.
  Documenter par ID les verdicts et défauts concrets dans `docs/reviews/`.
  `review.fact_check: pass`, tests et build ne constituent pas une acceptation pédagogique.
- Une nouvelle carte reste `draft` jusqu’à réussite des contrôles factuel et pédagogique.
  Ne pas présenter une seconde passe du même agent comme une relecture indépendante,
  ni déclarer les cartes anciennes conformes à cette grille sans les avoir relues.

Les consignes bilingues, d’import de l’ancien deck et d’organisation des agents du
WSET3 ne s’appliquent pas à ce dépôt français. Conserver les règles de sources,
d’identité et d’AnkiConnect propres à la plongée.

## Distracteurs — calibration renforcée du 9 octobre 2026

- Une réponse fausse doit attirer un apprenant ayant une **confusion précise du cours**.
  La revue nomme cette confusion pour chaque leurre, puis la condition qui le rend faux.
  « C’est une erreur possible », « c’est dangereux » ou « c’est l’inverse » ne suffisent pas.
- Interdire les QCM où la clé est la seule réponse prudente, coopérative, conditionnelle
  ou médicalement sérieuse. Comparer des conduites plausibles au même stade, des mécanismes
  voisins ou des paramètres concurrents ; ne pas opposer les secours à une imprudence caricaturale.
- Ne pas rendre un leurre reconnaissable en lui ajoutant « automatiquement », « seulement »,
  « quelle que soit », « sans alerter » ou une justification manifestement incohérente.
  Vérifier aussi la crédibilité d'une inversion : toute négation de la clé n'est pas un leurre.
- Si le fait initial ne permet que des leurres faibles, reconstruire le recto autour d'une
  application ou d'une distinction du **même objectif**, sans multiplier les questions.
  Pour un calcul, les résultats faux doivent découler d'opérations erronées identifiées.
- Tester chaque choix séparément : pourquoi un candidat hésiterait-il, et quelle connaissance
  précise permet de l'écarter ? Rejeter la carte si la logique ordinaire, la prudence ou le style
  suffisent à répondre. Trois choix solides valent mieux que quatre, sans quota de difficulté.
- Dans la revue par ID, consigner les deux justifications de chaque distracteur (attrait et
  réfutation), puis refaire une lecture après réécriture. Un tableau générique de critères
  « pass » ne remplace pas cette analyse. Vérifier l'unicité de la clé avec les mêmes hypothèses.

## Format des cartes — calibration finale du 6 octobre 2026

Pour une nouvelle rédaction ou revue, appliquer aussi les
[points du contrôle final N2 du 10 octobre](docs/STUDY_CARD_QUALITY.md#points-de-contrôle-issus-de-la-passe-finale-n2-du-10-octobre-2026) :
réponse donnée par le recto, leurres contredisant ses acteurs, distinction calcul réel /
majoration prudente, mécanismes crédibles et résolution des divergences de versions.
Le [journal par sujet](docs/reviews/CONTROLE_FINAL_ITERATIF_N2_2026-10-10.md)
et son CSV complètent les revues précédentes ; leurs corrections ne changent aucun ID.

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


## Sources et véracité

- Partir des documents convenus et du plan du niveau : [N2](docs/IMPLEMENTATION_N2.md),
  [N3](docs/IMPLEMENTATION_N3.md). Les supports pédagogiques sont à vérifier, pas une
  garantie d’exactitude. Pour N3, consulter l’inventaire des sources et le tri des reprises
  N2 liés dans le plan ; clore les vérifications G01–G11 pour les cartes concernées avant
  publication. Comparer les niveaux pour partager un objectif existant plutôt que le recréer.
- Vérifier chaque affirmation : question, réponse, explication, distracteurs, unités et hypothèses.
  Re-vérifier au moindre doute. Pour réglementation, médecine et sécurité, consulter les sources
  primaires actuelles, contrôler version et champ d’application, puis croiser en cas de doute.
- Résoudre et documenter les contradictions. Toute incertitude non résolue maintient la carte
  en `draft` ; ne pas choisir arbitrairement une source.
- Garder les références précises et la date de vérification dans `review.sources` ; consigner
  les divergences et la revue dans `docs/reviews/`. Effectuer une passe critique distincte de
  la rédaction avant `reviewed`. Tests et build ne valident pas la véracité.

## Pertinence pédagogique

- Un fait simple = une carte : Anki assure les répétitions. Fusionner paraphrases, cartes inverses
  du même fait et scénarios qui ne changent qu’un nom ou une profondeur dans une définition.
- Pour un sujet complexe, conserver plusieurs angles ou exemples si chacun ajoute une opération,
  une erreur à comprendre, une hypothèse ou une contrainte. Pour les calculs, une courte série de valeurs variées est utile pour automatiser la méthode.
- Comparer chaque proposition aux cartes de tous les chapitres et au catalogue. Noter son apport
  distinct dans la revue du lot ; sinon fusionner ou écarter. Une fusion ne doit pas produire
  un recto qui empile des questions indépendantes.
- Consulter [l’audit global](docs/reviews/PREPARATION_GLOBALE.md) : les objectifs fusionnés ne
  sont pas des cartes supplémentaires à recréer. Conserver leur traçabilité et leurs sources.
- Viser une préparation solide, sans quota ni réduction au strict minimum N2. Garder les
  approfondissements utiles, en signalant leur portée sans inventer de prérogative ou de procédure.

## Clarté des questions et réponses

- Poser la question directement. Éviter « selon le MFT… », les noms de documents et les dates
  d’édition répétés sur les rectos. Garder le contexte qui détermine la réponse (France, FFESSM,
  âge, exploration, modèle de matériel ou hypothèses), et les références dans `review.sources`.
- La difficulté vient de la connaissance et des distinctions testées, jamais d’un contexte flou.
  Le recto doit préciser le sujet, la situation et ce qu’on demande (minimum obligatoire,
  configuration conforme, plafond, rôle ou condition). Les choix doivent répondre à cette même
  question ; une possibilité valide mais non obligatoire ne doit pas être déclarée fausse si
  le recto demande seulement ce qui est possible. Préciser « obligatoire » ou « minimum » au besoin.
- Chaque QCM doit exiger une connaissance du cours : distracteurs crédibles issus de confusions
  réelles, même catégorie et niveau de précision, sans réponse fantaisiste ni indice de longueur.
  Ne pas demander seulement de reconnaître le nom suggéré par la description d’un document.
  Relire tous les choix : une personne sans connaissance du cours pourrait-elle éliminer les
  leurres au bon sens ? Si oui, reformuler. Préférer trois choix solides à un quatrième faible.
  La difficulté ne doit pas créer d’ambiguïté, de piège linguistique ou de mauvaise réponse défendable.
- Garder les explications centrées sur la connaissance : supprimer « cette carte ne… »,
  les commentaires sur sa portée, les disclaimers et précautions éditoriales adressées à l’apprenant.
  Conserver les notes de méthode et limites de validation dans docs/reviews/, pas dans les cartes.
  Garder les conditions factuelles nécessaires à une réponse exacte, sans avertissement ajouté.
- Donner une réponse courte, compréhensible et précise. Expliquer les expressions techniques
  avec des mots concrets ; ne pas recopier une formulation abstraite du référentiel.
  Exemple : préciser « ordinateur ou tables pour déterminer les paliers » au lieu de laisser
  « moyen de désaturation » sans explication.
- Développer les sigles nécessaires à la compréhension dans l’explication. Pour une question
  portant sur une partie des conditions, préciser ce périmètre et expliquer pourquoi un distracteur
  est faux sans laisser croire que ses autres éléments sont inutiles ou interdits.
- Pour un équipement, préciser qui doit en disposer et où : matériel collectif sur le site,
  matériel par palanquée ou équipement individuel porté en plongée. Donner un exemple concret
  lorsque « disponible » ou « personnel » peut prêter à confusion.
- Expliciter les valeurs et conditions des restrictions évoquées. Vérifier leur couverture par
  les cartes existantes ; créer une carte manquante seulement si elle apporte un objectif distinct.
- Distinguer compétences certifiées et prérogatives effectivement exerçables. Si les âges diffèrent,
  expliquer ce que la certification atteste et ce que le titulaire peut faire entre ces âges.
  Distinguer qualification isolée et brevet combiné ; ne pas attribuer PE40 à PA20 seul.
- Calculs d’air : données, réserves, unités et hypothèses explicites ; vérification par une résolution
  distincte. Un modèle simplifié n’est pas une procédure opérationnelle de plongée.

## Structure et vérifications techniques

- Les YAML de `cards/` sont la source de vérité, un fichier par chapitre ; `fr` obligatoire,
  `levels` explicite et aucun héritage automatique entre niveaux.
- Pour partager une carte avec un nouveau niveau, relire recto, verso et tous les choix,
  vérifier le champ d’application et consigner la décision dans la revue du lot. Garder
  les sources factuelles N2 ; ajouter la référence de pertinence N3. Consulter
  `docs/reviews/n3/00-reprises-n2.md` et les états du CSV avant toute nouvelle reprise.
- Identité partagée N2/N3/N4 : une identité Anki par ID de carte, indépendante des niveaux.
  Le sel historique N2 du GUID est permanent, même pour une nouvelle carte N3/N4.
  Ajouter des niveaux ne recrée pas une note ; les tags `level::N2/N3/N4` reflètent tous
  les niveaux de la carte, dans le paquet unique `diving-fr.apkg`. Aucun export séparé par niveau.
- Paquets classiques uniquement : `Plongée::N2` contient la base N2 (308 cartes),
  `Plongée::N3` les compléments N3 (140 cartes). Une carte commune reste au plus petit
  niveau de `levels` (N2 avant N3 avant N4), avec tous ses tags de niveau et un seul
  historique. Aucun dossier Collection commune, aucun paquet filtré dans le workflow.
  Catégories thématiques sous chaque niveau ; elles peuvent différer si nécessaire.
- Tout fonctionnement livré doit venir du dépôt : cartes, arborescence et préréglage
  de révision dans le `.apkg`. `config/study.json` règle les limites quotidiennes.
  Ne jamais utiliser l’interface d’Anki pour créer/modifier un paquet, des options ou
  une configuration locale. Pour importer, migrer et synchroniser, utiliser le code
  du dépôt via AnkiConnect. Aucun test manuel de séance à la place de l’utilisateur.
- Une migration conserve IDs de note/carte, modèles, historique, échéances et suspensions.
  Ne retirer que des paquets vides, jamais leurs cartes. Comme WSET 3, `make push`
  fait uniquement l'import du paquet puis la synchronisation AnkiWeb : aucun déplacement
  systématique de cartes ni réécriture d'options après import. Ces écritures marquent
  des états locaux comme récents et peuvent concurrencer les révisions d'un autre appareil.
  Une migration exceptionnelle doit être distincte ; un import seul ne garantit pas
  le déplacement des anciennes cartes.
- Cartes nouvelles en `draft`, puis `reviewed` après revue factuelle et pédagogique.
- IDs publiés permanents ; ne pas renommer ni réutiliser un ID pour un autre objectif.
  Les IDs Anki de `src/diving_anki/ids.py` restent stables.
- Exécuter `make check` après changement ; `make schema` après changement de schéma.
  Inspecter les rectos/versos après build quand le contenu ou le rendu des cartes change.
- Documents privés dans `sources/`, jamais dans Git ; packages générés non committés.

## Points consolidés à la clôture N2

- Consulter `docs/reviews/COUVERTURE_FINALE_N2.md` avant toute carte supplémentaire :
  les objectifs du catalogue sont couverts, parfois par fusion entre plusieurs chapitres.
  Ne pas recréer les objectifs fusionnés lors d’une extension N3/N4.
- Une date de dépôt en ligne n’est pas une date d’édition ; relever les deux si nécessaire.
- Distinguer les paramètres du fabricant et les repères fédéraux (GF, paliers profonds,
  vitesse, verrouillage). Le contexte air/algorithme/modèle détermine la réponse.
- Les schémas fonctionnels peuvent être des SVG autonomes intégrés au Markdown, comme
  P508. Contrôler le rendu, la lisibilité et leur présence dans le package sans média externe.

## Revue finale et retraits de cartes

- Consulter `docs/reviews/REVUE_FINALE_N2.md` et `RETIREMENTS_N2.yaml` : 17 IDs
  publiés sont réservés hors catalogue actif, dont dix retirés pendant cette revue. Ne jamais les recycler ou recréer leurs doublons.
- Retirer un YAML ne retire pas la note déjà importée. Pour une fusion, identifier exactement
  les notes concernées et les suspendre en conservant leurs révisions ; vérifier IDs, échéances
  et historique avant/après. Ne pas supprimer les notes ni réactiver les suspensions existantes.
- Une situation chiffrée doit mobiliser un raisonnement : un nombre déjà nommé DTR ou
  une catégorie dont la définition est donnée au recto ne crée pas un exercice utile.
- Un plafond d’ordinateur est une profondeur à ne pas franchir vers la surface ; deux
  plafonds différents ne se gèrent pas comme deux simples durées au même palier.

## Extension après clôture N3

Consulter [la couverture N3](docs/reviews/n3/COUVERTURE_N3.md),
[le recoupement des PDF](docs/reviews/n3/RECOUPEMENT_PDF_2026-10-07.md) et le CSV des objectifs
avant tout ajout. Le catalogue compte 448 notes, dont 204 communes et 140 créations N3.
Les douze modules du plan ne sont pas douze nouveaux sous-decks. Réutiliser les cartes
de tables, GF, secours et matériel à leur ID existant. Respecter les contextes fabricant,
air et établissement ; ne pas faire des hypothèses numériques une procédure réelle.

Une clôture de plan ne prouve pas l’exhaustivité des sources. Pour un audit de couverture,
partir des PDF et de leurs objectifs, comparer questions et corrigés du catalogue N2+N3,
et distinguer objectif interrogé, simple mention, compétence pratique et hors périmètre.
L’absence d’un terme exact ne suffit pas : vérifier les descriptions équivalentes avant
de proposer une carte. Revalider les cours anciens avec les sources primaires actuelles.

Les compléments issus du recoupement PDF du 7 octobre sont suivis dans
[COMPLEMENTS_PDF_2026-10-07.md](docs/reviews/n3/COMPLEMENTS_PDF_2026-10-07.md).
Le catalogue courant compte 448 cartes : 308 de base N2 et 140 compléments N3.
