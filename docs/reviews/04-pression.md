# Chapitre 04 — Pressions

6 octobre 2026. 16 cartes revues pour les 18 objectifs retenus, dans `Plongée::N2::Physique`.
Rédaction en draft suivie d’une passe factuelle et pédagogique distincte par le même agent.

## Sources et corrections

S1 p.9–10 et S3 p.2–3 (imprimées 4–5), extraits relus. Croisement avec NIST Appendix B.9
(unités), NOAA/NWS Pressure (atmosphère, altitude, météo), NOAA How does pressure change with
ocean depth? (ordre de grandeur hydrostatique), NOAA Outta Gas (extrait indexé : pression absolue)
et NASA Equation of State (Boyle, quantité et température constantes). Les URLs figurent dans les YAML.
Le PDF Outta Gas était indexé mais son ouverture web a échoué ; il ne constitue pas la seule source.

- S3 corrige 6 m en 2,5 bars : erreur. Le modèle annoncé donne 1 + 6/10 = 1,6 bar.
- Une masse en kg n’est pas une force. NIST donne 1 kgf/cm² = 98 066,5 Pa = 0,980665 bar.
- +1 bar/10 m et 1 bar atmosphérique sont des approximations de cours annoncées sur les calculs.
- Les variations en bars sur deux tranches de 10 m sont identiques ; leurs rapports diffèrent.
- P111 précise eau au repos, densité uniforme et même surface ; la profondeur du fond n’intervient pas.
- Boyle utilise les pressions absolues ; aucun calcul de volume ni procédure d’accident ajouté ici.

## Apport distinct et couverture

| Objectif | Apport |
| --- | --- |
| P096 | Relation force/surface. |
| P097 | Raisonnement combinant deux changements opposés : force doublée, surface triplée. |
| P101 + P132 | Reconnaissance des unités de pression dans une seule carte de rappel. |
| P102 | Distinguer masse, poids et pression, corriger kg/kgf. |
| P103 | Origine de la pression atmosphérique, indépendante du vent. |
| P105 | Effet qualitatif de l’altitude. |
| P106 | Variation météorologique à altitude constante. |
| P107 | Origine hydrostatique et référence relative à la surface. |
| P110 + P118 | Addition atmosphère/eau et calcul à 6 m ; pas de série numérique. |
| P111 | Profondeur sous la surface, à distinguer de celle du fond. |
| P114 | Calcul de la seule contribution hydrostatique. |
| P123 | Calcul inverse depuis une pression absolue. |
| P126 | Calcul inverse depuis une pression relative, sans soustraire l’atmosphère. |
| P127 | Diagnostic d’un double comptage atmosphérique. |
| P128 | Choix des pressions à employer dans une relation de gaz. |
| P129 | Distinguer rapport et différence de pression. |

Les fusions antérieures de l’audit restent applicables. P118 et P132 restent cochés comme couverts
au catalogue, sans nouveau YAML. Les 53 cartes précédentes ne couvrent pas ces objectifs.
Pour le chapitre 06, P175/P176 porteront sur la loi et ses conditions ; ne pas recréer P128.
Les variantes de volumes devront exiger un raisonnement supplémentaire, pas redemander les pressions.

## Passe critique

P096 recentré sur la relation, unités développées au verso. P097 rendu concret par deux caisses.
P101 demande un rappel libre de la grandeur, sans QCM évident. P105 compare deux lieux sans
suggérer qu’un même lac change d’altitude. P127 passe en rappel libre pour expliquer l’erreur
plutôt que recopier une valeur du recto. P129 : distracteurs issus de rapports inversés,
confusion avec l’addition et confusion avec les valeurs finales ; suppression du leurre « ×1 ».
Chaque QCM a une seule réponse dans le contexte annoncé. Pas de changement aux IDs existants.

Calculs recontrôlés par substitution inverse : 0,3 × 10 = 3 m ; (1,6 − 1) × 10 = 6 m ;
1 + 5/10 = 1,5 bar ; 20/10 = 2 bars relatifs. Rapports 2/1 = 2 et 3/2 = 1,5.
Pour la caisse, un exemple F=300 N, S=0,3 m² donne 1000 Pa ; 600 N / 0,9 m²
= 666,67 Pa, soit 2/3 de la pression initiale.

## Vérifications techniques

`make check` réussi : 69 cartes, 13 tests. Package inspecté : 69 GUID uniques, 16 notes
du chapitre 04, champs HTML recto/verso non vides, Physique directement sous N2.
Cette inspection des champs a corrigé un reliquat « deux unités » après élargissement
du recto à quatre unités. Pas de contrôle visuel dans l’interface Anki.

## Complément d’entraînement — 6 octobre 2026

À la demande de l’utilisateur, huit exercices supplémentaires : le chapitre comporte désormais
24 cartes (77 dans le deck). La série initiale couvrait les opérations mais manquait de pratique
à des profondeurs variées. Une répétition numérique limitée est désormais explicitement admise
dans les consignes aux agents, sans exiger une nouvelle opération pour chaque exercice.

| Objectif | Exercice | Résultat | Intérêt |
| --- | --- | --- | --- |
| P110 | Absolue à 20 m | 3 bars | Application sur profondeur ronde |
| P110 | Absolue à 33 m | 4,3 bars | Application plus profonde, décimale |
| P123 | Profondeur à 2,8 bars absolus | 18 m | Inverse avec décimales |
| P123 | Profondeur à 4 bars absolus | 30 m | Consolider le retrait atmosphérique |
| P114 | Hydrostatique à 27 m | 2,7 bars | Contribution de l’eau seule |
| P129 | Diminution de 30 à 12 m | 1,8 bar | Différence entre deux positions |
| P110 | Absolue à 18 m, atmosphère 0,8 bar | 2,6 bars | Employer la référence fournie |
| P123 | Inverse à 2,3 bars, atmosphère 0,8 bar | 15 m | Inverser avec référence différente |

Chaque exercice est en rappel libre, avec modèle explicite et solution détaillée. Les cas
de lac emploient une donnée atmosphérique fictive fournie, sans calcul d’altitude ni procédure
de plongée. Sources : mêmes relations S1 p.10 et S3 p.3 ; aucune nouvelle loi introduite.
Rédaction en draft, puis relecture séparée de tous les rectos/versos et vérification de chacun
des huit résultats par substitution inverse en arithmétique décimale, avant passage à reviewed.
Les 16 IDs déjà publiés sont conservés. Aucun nouvel objectif compté dans le catalogue.

Validation du complément : `make check` réussi (77 cartes et 13 tests), build inspecté
(77 GUID uniques ; huit nouvelles notes basic avec rectos et versos HTML complets).
`make push` réussi : package importé et synchronisé avec AnkiWeb.
