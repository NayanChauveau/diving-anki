# Instructions aux agents

Projet de théorie de plongée en français : N2 actuellement, structure prévue pour N3/N4.
Avant de préparer ou rédiger des cartes, lire [CONTENT_GUIDELINES.md](CONTENT_GUIDELINES.md)
et [docs/CARD_DESIGN.md](docs/CARD_DESIGN.md). Lire [CONTRIBUTING.md](CONTRIBUTING.md)
pour le workflow. Ces règles s’appliquent à toutes les cartes et tous les niveaux.

## Sources et véracité

- Partir des documents convenus et du [plan N2](docs/IMPLEMENTATION_N2.md).
  Les trois PDF sont des supports pédagogiques à vérifier, pas une garantie d’exactitude.
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
  une erreur à comprendre, une hypothèse ou une contrainte. Pas de substitutions numériques en série.
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
- Sous-decks N2 : cinq catégories directement sous `Plongée::N2` — Réglementation, Physique,
  Prévention des accidents, Désaturation, Matériel et préparation. Ne pas créer de sous-deck
  par chapitre ; conserver les fichiers et tags thématiques. Pour une réorganisation, déplacer
  les cartes existantes dans Anki en conservant leurs IDs, historique et échéances, puis vérifier
  ces données avant/après. Un import de package ne garantit pas à lui seul leur déplacement.
- Cartes nouvelles en `draft`, puis `reviewed` après revue factuelle et pédagogique.
- IDs publiés permanents ; ne pas renommer ni réutiliser un ID pour un autre objectif.
  Les IDs Anki de `src/diving_anki/ids.py` restent stables.
- Exécuter `make check` après changement ; `make schema` après changement de schéma.
  Inspecter les rectos/versos après build quand le contenu ou le rendu des cartes change.
- Documents privés dans `sources/`, jamais dans Git ; packages générés non committés.
