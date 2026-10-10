# Relecture de la qualité des cartes

Grille adaptée le 9 octobre 2026 du dépôt voisin `anki-deck-wset-3`, notamment
`import/STUDY_CARD_QUALITY.md`, `CONTENT_GUIDELINES.md` et `import/AGENT_PLAYBOOK.md`.
Elle s’applique à toute création, réécriture ou revue de cartes N2, N3 et N4.
Elle complète [CARD_DESIGN.md](CARD_DESIGN.md) et les vérifications des sources.

**Une carte factuellement exacte peut échouer à la revue pédagogique.**
Inversement, un QCM bien rédigé ne prouve pas l’exactitude de ses affirmations.
Les deux contrôles sont obligatoires et leurs conclusions restent distinctes.

## Les cinq critères de rejet

| Critère | Question à se poser | Rejet typique |
| --- | --- | --- |
| ISOLATION | La carte se comprend-elle seule, dans un ordre aléatoire ? | « ce calcul » renvoie à une carte précédente ; hypothèse manquante ; réponse dévoilée |
| CREDIBILITY | Un candidat qui se souvient imparfaitement du cours pourrait-il choisir chaque leurre ? | Choix hors sujet, impossible ou éliminable au bon sens |
| LENGTH | La forme des choix révèle-t-elle la bonne réponse ? | Bonne réponse seule longue, précise, nuancée ou développée |
| WHY | Le corrigé aide-t-il à comprendre la distinction interrogée ? | Réponse simplement recopiée ; explication d’un autre sujet |
| SENSE | Question, choix et corrigé sont-ils du français clair et naturel ? | Formule abstraite, sujet perdu, jargon non expliqué, phrase vide |

Le succès sur quatre critères ne compense pas l’échec sur le cinquième. Réécrire
les cartes rejetées et les relire après correction. Ne pas valider un lot seulement
parce qu’un échantillon semble bon ou que `make check` réussit.

## 1. ISOLATION — autonomie et absence de réponse dévoilée

Anki présente les cartes dans un ordre indépendant du chapitre. Nommer le sujet,
les acteurs et le cadre qui déterminent la réponse. Un démonstratif est acceptable
si son référent est présent sur la même carte ; il échoue s’il exige la précédente.

- Éviter « Quelle réserve faut-il pour ce retour ? » si le profil n’est pas donné.
  Fournir sur le recto les phases, débits, blocs, unités et pression finale utiles.
- Poser une seule distinction. Ne pas assembler deux objectifs indépendants avec
  « et pourquoi », ni proposer un choix qui répond à une autre question.
- Vérifier les classes : un brevet, une aptitude, une fonction et un document ne
  sont pas interchangeables. Les alternatives doivent répondre au même objet.
- Supprimer les adjectifs, exceptions, parenthèses et annotations qui préannoncent
  la clé. Si le recto nomme déjà une DTR, demander simplement d’identifier la DTR
  n’interroge aucune connaissance.
- Dans un schéma, retirer les légendes qui donnent la réponse, garder les données
  nécessaires au raisonnement. Dans un cas d’identification, les signes observés
  sont des données utiles ; le diagnostic déjà nommé serait une réponse dévoilée.
- Placer les exceptions secondaires dans le corrigé lorsqu’elles ne déterminent
  pas la réponse. Conserver au recto les conditions qui évitent une ambiguïté réelle.

## 2. CREDIBILITY — leurres réellement choisissables

Le candidat doit hésiter entre des réponses proches parce qu’il connaît imparfaitement
le cours. Pour **chaque** mauvaise réponse, identifier la confusion précise qui peut
la rendre attirante. « C’est faux » ne justifie pas sa qualité pédagogique.

- Même classe : profondeur/profondeur, mécanisme/mécanisme, action/action,
  qualification/qualification, matériel/matériel. Une cause demande des causes,
  pas une cause correcte opposée à des noms d’équipements.
- Même cadre : même âge, milieu, appareil, phase de plongée et population que le
  recto. Une action après émersion n’est pas un leurre crédible pour une tâche qui
  doit précisément avoir lieu avant émersion.
- Inclure les confusions principales du sujet, pas seulement des possibilités
  marginales faciles à écarter. Par exemple : pression absolue/relative,
  stock total/utilisable, palier/plafond, DP/guide, certification/exercice.
- Rejeter les contradictions avec les données du recto, les actions caricaturales,
  les impossibilités physiques et les propositions sans rapport. Un calcul de stock
  n’a pas pour bons leurres « stock illimité » ou « profondeur sans effet ».
- Une demi-vérité peut être un bon leurre si une condition précise du recto la rend
  fausse. Vérifier cette condition ; une réponse valable dans le contexte ne devient
  pas fausse parce qu’elle est moins complète ou qu’elle n’était pas la clé prévue.
- Éviter le oui/non où le « non » est évident face à plusieurs « oui » fantaisistes.
  Reformuler autour du mécanisme, du seuil ou de la décision réellement à apprendre.
- Ne pas rendre les mauvaises réponses reconnaissables par « toujours », « jamais »,
  « uniquement » ou une imprudence ajoutée artificiellement. Ces mots restent permis
  quand ils expriment exactement une règle ou une confusion réellement pertinente.
- Relire en candidat sans connaissances : s’il peut trouver la clé par logique
  ordinaire, politesse ou prudence générale, reconstruire le recto et les choix.
  Préférer trois alternatives solides à quatre dont une sert de remplissage.

### Contrôle approfondi de chaque distracteur

Calibration renforcée après le retour utilisateur du 9 octobre 2026 : la revue
globale précédente acceptait encore trop de réponses évidemment fausses.

Pour chaque leurre, écrire dans la revue **pourquoi il peut attirer** un candidat
et **quel fait précis le réfute**. Exemples : appliquer 6 m/min à tout le trajet
MN90 ; traiter la majoration comme du palier ; prendre le plafond le moins profond
des équipiers ; confondre oxygénothérapie normobare et recompression hyperbare.
Une simple inversion, une imprudence ou un mot technique ne prouvent pas la plausibilité.

Les alternatives doivent être concurrentes dans le contexte. Pour un calcul,
résoudre l'opération erronée qui produit chaque nombre proposé. Pour les secours,
opposer des protocoles ou interprétations voisins plutôt que « aider et alerter »
à « abandonner ou attendre ». La clé ne doit pas être seule prudente ou nuancée.
Retirer les qualifications qui trahissent les leurres ; rendre tous les choix
affirmatifs, conditionnels ou détaillés de façon comparable.

Si le recto conduit à deux mauvais choix caricaturaux, le réécrire : une situation,
une distinction, le même objectif et le même ID. Ne pas ajouter une ambiguïté pour
créer de l'hésitation. Vérifier chaque alternative comme si elle était la clé :
si elle peut être vraie sous une lecture raisonnable, préciser le contexte ou la changer.
Un test de crédibilité échoué impose une correction, même après une revue antérieure.

### Points de contrôle issus de la passe finale N2 du 10 octobre 2026

- Une limite numérique annoncée suivie de deux valeurs qui la dépassent peut donner
  la réponse sans connaissance du cours. Tester la responsabilité ou la règle visée,
  plutôt que fabriquer un exercice d'application qui se résout au seul recto.
- Un guide explicitement absent ne peut servir de destinataire aux deux mauvaises
  réponses d'une question d'autonomie. Comparer des limites de compétence plausibles.
- Pour un budget de gaz, distinguer le calcul du profil réel d'une majoration prudente :
  une estimation conservatrice n'est pas fausse simplement parce qu'elle est moins exacte.
- Ne pas attribuer à un rhume, au lest ou à la fatigue un changement fantaisiste des
  lois physiques ou de la composition du gaz. Chercher une confusion du cours ; si un
  troisième choix reste faible, deux choix solides sont préférables au remplissage.
- Ne pas justifier artificiellement un leurre chiffré par une confusion inventée
  entre une profondeur et une durée. Une valeur proche mal mémorisée peut suffire
  pour un fait de rappel ; la revue doit décrire cette raison honnêtement.
- Devant des formulations différentes d'une procédure, rechercher le référentiel
  consolidé et consigner la différence. Une newsletter ou un article peut omettre
  une étape ; conserver les dates d'édition et de consultation distinctes.

## 3. LENGTH — aucun indice de forme

Lire d’abord le bloc des choix sans chercher à résoudre la question. La bonne réponse
ne doit pas se distinguer par sa longueur, son registre ou son degré de précision.

- Raccourcir la clé et déplacer les détails utiles dans le corrigé.
- Donner aux leurres une précision comparable, sans les gonfler avec du remplissage.
- Éviter une clé qui contient action, condition, justification et exception face à
  deux fragments. Tous les choix doivent avoir une structure grammaticale comparable.
- Des noms ou des nombres naturellement de longueurs différentes sont acceptables.
  Une règle de comptage de mots ne remplace pas la lecture.
- Ne pas souligner, mettre en gras ou qualifier favorablement la seule clé au recto.
  Ne pas imposer sa position dans les choix : le rendu peut les mélanger.

## 4. WHY — un corrigé qui enseigne

Nommer la bonne réponse est permis. La recopier systématiquement, souvent en gras,
sans expliquer la distinction n’apporte rien.

- Expliquer le mécanisme, la condition déterminante, l’erreur de raisonnement ou une
  exception utile. Un exemple doit être concret et vérifiable, pas une anecdote inventée.
- Pour un calcul, montrer l’opération et les unités ; expliquer la confusion importante
  plutôt que seulement répéter le nombre obtenu.
- Pour une règle simple, garder un corrigé court si aucun complément utile ne s’impose.
  Ne pas ajouter un autre objectif pour remplir le verso.
- Répondre à la question effectivement posée. Une carte sur la cause d’un accident
  n’appelle pas un paragraphe générique sur un autre accident.
- Ne jamais écrire « option B », « réponse 2 » ou un renvoi à l’ordre des choix.
  Désigner le contenu du choix lorsqu’il faut expliquer une erreur.
- Garder hors de la carte les commentaires éditoriaux, le bilan de couverture,
  les mentions de rédaction, chapitre ou source qui ne déterminent pas la réponse.

## 5. SENSE — français naturel et vocabulaire concret

Lire à nouveau le recto, chaque choix et le verso comme des phrases françaises,
sans s’aider du document source. Si une phrase ne veut rien dire immédiatement,
la réécrire entièrement ; remplacer un mot ne suffit pas toujours.

- Employer les termes usuels de plongée et développer les sigles utiles au corrigé.
  Expliquer les termes techniques nécessaires plutôt que juxtaposer du jargon.
- Nommer ce qui est suivi ou comparé : « profondeur et durée du palier » est plus
  concret que « gestion des contraintes selon les moyens ».
- Éviter les pronoms sans sujet identifiable, les calques et les nominalisations
  abstraites. Une phrase correcte grammaticalement peut rester incompréhensible.
- Ton précis et calme ; formulation impersonnelle ou vouvoiement, sans tutoiement,
  marketing ni piège qui repose sur la lecture d’un seul adjectif.
- Respecter les noms d’organismes, espèces, appareils et qualifications. Ne pas
  inventer un terme pour simplifier un contraste ou fabriquer un leurre.

## Workflow : rédaction, critique, correction, nouvelle lecture

1. Lire tout le chapitre et rechercher les objectifs voisins dans l’ensemble du
   catalogue. Pour une revue de chapitre, ne pas se limiter aux cartes signalées.
2. Travailler par lots d’au plus **40 cartes**, avec un périmètre et des IDs explicites.
   Les nouvelles cartes restent `draft`. Les faits incertains restent hors publication.
3. Faire une passe factuelle sourcée, puis une **passe critique distincte** de la
   rédaction : lire chaque recto, chaque choix et chaque corrigé avec les cinq critères.
   Si un relecteur distinct est disponible, sa passe est en lecture seule. Sinon,
   reprendre le lot dans une seconde passe explicite, sans présenter cela comme
   une validation indépendante. Ce workflow n’impose pas de lancer des sous-agents.
4. Consigner par ID les critères acceptés ou rejetés, le motif concret, la correction
   et les incertitudes dans `docs/reviews/`. Distinguer le contrôle factuel de la qualité
   pédagogique ; `review.fact_check: pass` ne remplace pas ce relevé.
5. Corriger les IDs rejetés et refaire leur critique. Passer une nouvelle carte à
   `reviewed` seulement après succès factuel **et** pédagogique. Une carte publiée
   réécrite garde son ID, son modèle Anki et le sens de son objectif.
6. Lancer `make check`, puis contrôler les champs recto/verso du build si le contenu
   change. Ne pas piloter l’interface Anki ; suivre le workflow AnkiConnect du dépôt.

Les anciennes revues ne deviennent pas automatiquement des succès sur cette grille.
Indiquer les cartes effectivement relues ; ne pas déclarer tout le catalogue conforme
à partir d’un lot. Si la correction modifie un fait, refaire sa vérification primaire.
Les limites de lots organisent la relecture et ne constituent pas un quota de cartes.

### Brief de critique à réutiliser

```text
Relire les IDs indiqués avec docs/STUDY_CARD_QUALITY.md.
Passe critique en lecture seule : ne pas corriger pendant la formulation du verdict.
Examiner chaque question, chaque choix et chaque explication, pas un échantillon.
Cette passe pédagogique ne remplace pas le fact-check.

ISOLATION : autonomie, une tâche, cadre explicite, aucune clé dévoilée.
CREDIBILITY : chaque leurre choisissable, même classe et même cadre.
LENGTH : aucune clé visible par la longueur, le détail ou le style.
WHY : raisonnement utile, pas simple répétition ni renvoi à une lettre.
SENSE : français clair et naturel, sujet et vocabulaire compréhensibles.

ACCEPT_ALL=yes|no
ACCEPT: IDs effectivement relus et acceptés
REVISE: id — critère(s) — défaut précis et correction attendue
HOLD: id — incertitude factuelle à résoudre avant publication
MERGE: id — objectif déjà porté par un autre ID ; proposer sans supprimer de note
```
