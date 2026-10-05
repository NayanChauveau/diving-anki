# Instructions aux agents

Projet de théorie de plongée français N2/N3/N4. Lire CONTRIBUTING.md avant de changer
le workflow et CONTENT_GUIDELINES.md avant de rédiger des cartes.

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
