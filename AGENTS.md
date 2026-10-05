# Instructions aux agents

Projet de théorie de plongée français N2/N3/N4. Lire CONTRIBUTING.md avant de changer
le workflow ; lire CONTENT_GUIDELINES.md et [docs/CARD_DESIGN.md](docs/CARD_DESIGN.md)
avant de préparer ou rédiger des cartes.

- YAML dans cards/ est la source de vérité, un fichier par chapitre.
- `fr` obligatoire ; `levels` explicite, aucune héritage automatique entre niveaux.
- Ne pas rédiger de contenu sans les documents et le référentiel convenus.
- Nouvelles cartes en draft ; revue factuelle avant reviewed.
- IDs publiés permanents, IDs Anki stables dans src/diving_anki/ids.py.
- Après changement : make check. Après changement de schéma : make schema.
- Documents privés dans sources/, jamais dans Git.

## Véracité et pertinence des cartes

- La véracité prime sur le volume : vérifier chaque affirmation, y compris les distracteurs,
  les explications, les unités et les conditions des scénarios. Re-vérifier au moindre doute.
- Pour réglementation, médecine et sécurité : consulter les sources primaires actuelles,
  contrôler leur date/version et leur champ d’application, et croiser les sources en cas de doute.
- Les trois PDF de référence servent de base pédagogique, sans présomption d’exactitude.
  Une contradiction exige une résolution documentée ; ne pas choisir arbitrairement une source.
- Conserver les références précises et la date de vérification dans review.sources ; consigner
  les divergences et la revue du chapitre dans docs/reviews/. Toute incertitude non résolue reste draft.
- Relire les cartes dans une passe critique distincte de la rédaction avant de marquer reviewed.
  Les tests et le build ne constituent pas une validation factuelle.
- Vérifier la pertinence pour apprendre : contexte explicite, une notion par question, explication
  utile et distracteurs plausibles. La redondance entre angles complémentaires est souhaitée.
- Un approfondissement au-delà du minimum N2 est bienvenu s’il aide à comprendre ou à sécuriser
  les connaissances ; le signaler clairement sans inventer de prérogative ou de procédure.
- L’objectif est une préparation solide au N2, pas un quota de cartes ni une réduction au strict minimum.

- La répétition doit ajouter une difficulté utile (mécanisme, erreur fréquente, contrainte nouvelle).
  Regrouper les simples variantes d’une définition ou d’un sigle ; ne pas faire un scénario
  qui ne fait que remplacer 40 m par 35 m. Le catalogue est un réservoir, pas un quota.

## Calibration pédagogique obligatoire

- Un fait simple = une carte : Anki assure déjà la répétition. Pas de cartes inverses,
  de paraphrases ou de scénarios qui ne font que reformuler ce fait.
- Plusieurs cartes pour un sujet complexe si elles changent l’opération, le modèle,
  l’erreur travaillée ou la contrainte ; plusieurs exemples utiles, pas une série mécanique.
- Comparer chaque proposition aux cartes de tous les chapitres. Noter son apport distinct
  dans la revue du lot ; sinon fusionner ou écarter. Ne pas surcharger une carte fusionnée.
- Calculs d’air : données et réserves explicites, unités et hypothèses contrôlées, résolution
  distincte pour vérifier le résultat. Ne pas déduire une procédure opérationnelle d’un modèle simplifié.
- Consulter docs/reviews/PREPARATION_GLOBALE.md : les anciens objectifs fusionnés ne sont
  pas des cartes supplémentaires à recréer. Conserver les IDs et la traçabilité des sources.
- Ces critères valent pour tout le deck, sans réduire les approfondissements utiles au N2.

- Lorsqu’une certification est acquise avant l’âge d’exercice d’une prérogative, expliquer
  ce qu’elle atteste et ce que le titulaire peut effectivement faire entre ces deux âges.
  Distinguer qualification isolée et brevet combiné ; ne pas laisser entendre que PA20 seul
  confère PE40. Une réponse exacte mais laissant une contradiction apparente doit être clarifiée.

- Formuler les questions directement : éviter « selon le MFT… » et la date d’édition à chaque
  recto. Garder la référence/version dans review.sources ; conserver le contexte utile (France,
  FFESSM, âge, exploration) lorsqu’il détermine la réponse. Une restriction évoquée dans une
  explication doit être explicite et sa couverture par les cartes voisines vérifiée.
