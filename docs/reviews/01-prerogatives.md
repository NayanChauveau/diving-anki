# Revue du chapitre 01 — Prérogatives

Date : 5 octobre 2026. Périmètre : P001 à P027 du plan, 28 cartes (P020 scindé).
Revue effectuée par l’agent rédacteur dans une seconde passe ; aucune validation humaine
ou par un moniteur n’est revendiquée. Statut éditorial : reviewed, fact_check: pass.

## Références contrôlées

- Source pédagogique : Théorie N2 Stade de Vanves, édition 2024, p.3–4.
- [MFT N2 FFESSM, version mai 2026, p.3–4 et historique p.22](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/d7c761c8-79ed-42f2-a675-90e4c6095a56).
- [Règles générales de formation/certification, janvier 2025, p.2](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/fb0d17fd-84a2-40ef-a59a-48ee2ab230e3).
- [Code du sport A322-73, version depuis le 31 octobre 2025](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052464714).
- [Présentation fédérale du N2](https://ffessm.fr/plongeur-niveau-2) : utilisée pour la correspondance CMAS deux étoiles uniquement. Ses âges issus du flyer ancien ne sont pas repris.

Le MFT est l’édition mai 2026 malgré un résultat de recherche indiquant initialement décembre
2025. Le contenu ouvert, la page 3 et la liste des modifications ont été contrôlés.

## Divergences résolues et limites

- Le flyer 2021 indique des âges anciens. Les cartes utilisent les seuils du MFT actuel :
  PE40 à 14 ans, entrée/certification PA20 et N2 à 15 ans, exercice PA20 à 16 ans.
- Les limites supplémentaires PE40 concernent les moins de 16 ans, pas tous les mineurs.
- Le cours de 2024 cite un cadre antérieur : l’ancien A322-88 a été abrogé ; l’autonomie
  est désormais portée par A322-73. Les références de cartes pointent le nouvel article.
- Autorisation du responsable légal et information de la palanquée sont présentées comme
  conditions du cadre FFESSM. Elles ne sont pas attribuées à tort au seul Code du sport.
- P012 utilise un équipier PA12 pour tester la limite la plus restrictive sans prétendre
  qu’un PE20 peut devenir autonome en étant accompagné d’un N2.
- P020 produit deux cartes pour séparer le nombre journalier et l’intervalle minimal.
- P027 exprime une règle de préparation à l’étranger, sans inventer les droits d’une destination.
  La présentation fédérale justifie la reconnaissance internationale, pas un droit universel.
- Aucune nouvelle carte N3/N4, procédure médicale ou technique d’assistance ajoutée.

## Revue pédagogique

Contrôle des 28 rectos, réponses, explications et distracteurs : contexte fédéral/français explicite,
certification distincte de l’exercice, plafond de profondeur distinct de la profondeur imposée,
une seule bonne réponse par QCM, répétitions sous des angles complémentaires.
Deux cartes basic facilitent le rappel libre (décision du DP et information des équipiers).
Les autres sont des QCM, avec rappel numérique, comparaison et scénarios.
Les bonnes réponses ne sont pas référencées par leur lettre : le template mélange les choix.
La carte documentaire a été revue pour remplacer des distracteurs sans rapport par des
combinaisons plausibles mais incomplètes de licence, CACI, carnet et carte N1.

## Correspondance plan → IDs

- P001 : `n2-prerogatives-n2-aptitudes-001`.
- P002 : `n2-prerogatives-pe40-exploration-001`.
- P003 : `n2-prerogatives-pa20-exploration-001`.
- P004 : `n2-prerogatives-qualifications-separees-001`.
- P005 : `n2-prerogatives-pe20-pe40-001`.
- P006 : `n2-prerogatives-autonomie-dp-001`.
- P007 : `n2-prerogatives-pa20-effectif-001`.
- P008 : `n2-prerogatives-pa20-equipiers-001`.
- P009 : `n2-prerogatives-decision-dp-001`.
- P010 : `n2-prerogatives-autonome-trente-001`.
- P011 : `n2-prerogatives-encadre-trentecinq-001`.
- P012 : `n2-prerogatives-aptitude-restrictive-001`.
- P013 : `n2-prerogatives-age-pe40-001`.
- P014 : `n2-prerogatives-age-certification-001`.
- P015 : `n2-prerogatives-age-autonomie-001`.
- P016 : `n2-prerogatives-quinze-ans-n2-001`.
- P017 : `n2-prerogatives-mineur-autorisation-001`.
- P018 : `n2-prerogatives-mineur-information-001`.
- P019 : `n2-prerogatives-pe40-moins-seize-paliers-001`.
- P020 : `n2-prerogatives-pe40-moins-seize-nombre-001`, `n2-prerogatives-pe40-moins-seize-intervalle-001`.
- P021 : `n2-prerogatives-pe40-moins-seize-seconde-001`.
- P022 : `n2-prerogatives-documents-formation-001`.
- P023 : `n2-prerogatives-prerequis-niveau-001`.
- P024 : `n2-prerogatives-experience-naturel-001`.
- P025 : `n2-prerogatives-autorisation-seule-001`.
- P026 : `n2-prerogatives-cmas-etoiles-001`.
- P027 : `n2-prerogatives-etranger-regles-001`.

## Validation et import

- `make check` : Ruff, formatage, basedpyright, schéma JSON, validation YAML et 13 tests réussis.
- Build N2 : 28 notes / 28 cartes ; GUIDs attendus, deux modèles, script de mélange injecté.
- `make push` : import effectué, puis première synchronisation ayant dépassé le délai d’attente.
- Vérification AnkiConnect : 28 notes retrouvées dans le sous-deck attendu.
- Relance ciblée de `sync` : réponse sans erreur ; 28 cartes confirmées ensuite dans Anki.
