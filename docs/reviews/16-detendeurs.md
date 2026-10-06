# Revue du chapitre 16 — detendeurs

21 cartes nouvelles. Rédaction puis passe critique le 6 octobre 2026.

## Sources consultées

- S1 — Théorie N2 Stade de Vanves 2024, p.30–34 ; tableau p.34 inspecté visuellement.
- SCUBAPRO — Manuel détendeurs, 2025 Rev Q (juillet), p.6–9, 13–17 et 20 ; consulté le 2026-10-06 : https://johnsonoutdoors.widen.net/s/hlkmf7vhpb/sp_45101180_revq_reg_manual_202507_fra
- Schéma original intégré : docs/diagrams/circuit-detendeur.svg ; P585 fusionné avec P508.

## Décisions et corrections

V14 : manuel constructeur actuel récupéré via la page officielle, SCUBAPRO Rev Q juillet
 2025, 24 pages, fichier Français. P.6–9 principes, p.13–17 usage/soin, p.20 dépannage.
 Première pression intermédiaire annoncée relative 9,5 bar ; ne pas la donner comme une
 pression absolue constante. Calculs séparés : 3 + 9 = 12 ; 14 − 5 = 9 ; 3 + 9,5 = 12,5,
 puis second étage vers environ 3 bar. Résolution inverse validée. P627 a deux exercices.
 Le modèle de cycle P519 est conceptuel : ne pas attribuer à tous les premiers étages
 l’effet de la HP sur le clapet représenté dans S1. Membrane/piston ≠ compensation.
 Les performances froid, entretien et confort ne sont pas déduits du seul type de mécanisme.
 S1 conseille stockage sans bouchon ; notice constructeur actuelle p.17 demande protection
 d’entrée correcte : corrigé. Les périodicités sont liées au constructeur et à l’usage.
 P508 absorbe P585 : lecture d’un schéma original SVG, HP → MP → pression ambiante,
 sans copier la figure du support. Diagramme dessiné et rendu pour contrôle : fond blanc,
 labels et flèches lisibles. SVG inline, autonome : aucun asset externe requis, aucun
 changement de schéma/builder ni de GUID publié. Schéma fonctionnel, pas plan de réparation.
 « cause probable » reste une hypothèse ; débit continu n’est pas preuve unique de givrage.

## Pertinence et clarté

Rappel actif basic, pas de QCM avec leurres évidents. Questions concrètes et modèle nommé
quand il conditionne la réponse. Comparaison avec tous les YAML publiés ; fusions des
facts simples conservées ci-dessus, variantes numériques limitées et justifiées.
Aucun ID existant renommé.

| Objectif | Tâche retenue |
| --- | --- |
| P508 | Sur ce schéma conceptuel d’un détendeur à deux étages, quelle réduction de pression réalise A, puis B ? |
| P512 | Une pression intermédiaire est annoncée « 9,5 bar au-dessus de l’ambiante ». Pourquoi sa valeur absolue augmente-t-elle avec la profondeur ? |
| P514 | Quelle différence mécanique entre une fixation DIN et une fixation par étrier du premier étage ? |
| P515 | Dans un premier étage, quelle distinction entre un mécanisme à piston et un mécanisme à membrane ? |
| P519 | Dans un modèle conceptuel de premier étage à membrane, comment la consommation d’air déclenche-t-elle puis arrête-t-elle l’arrivée de gaz depuis le bloc ? |
| P521 | Comment l’inspiration commande-t-elle l’arrivée de gaz dans un second étage classique à membrane et levier ? |
| P523 | Comment le bouton de purge d’un second étage provoque-t-il un débit sans inspiration ? |
| P524 | Un second étage a été immergé hors de la bouche. Que faut-il faire avant d’inspirer à nouveau dedans ? |
| P525 | Pour rincer un détendeur SCUBAPRO démonté du bloc, quelle protection de l’entrée du premier étage faut-il vérifier ? |
| P526 | Quel intérêt a la compensation d’un premier étage lorsque la pression du bloc diminue ? |
| P532 | Pourquoi ne suffit-il pas de choisir « un premier étage à membrane » pour une plongée en eau froide ? |
| P537 | Pourquoi sécher et ranger son détendeur loin de la chaleur, du soleil direct et des contraintes sur les flexibles ? |
| P539 | Comment déterminer l’échéance d’entretien d’un détendeur plutôt que d’appliquer une fréquence unique à tous les modèles ? |
| P540 | Un détendeur se met en débit continu hors de la bouche. Pourquoi ce constat ne permet-il pas de diagnostiquer à lui seul un givrage ? |
| P541 | Des bulles sortent au raccord bloc–premier étage après montage. Pourquoi faut-il contrôler l’étanchéité et le montage plutôt que serrer toujours plus fort ? |
| P542 | Avant de plonger, respirer sur le détendeur demande un effort inhabituel. Que faut-il contrôler avant de décider de s’immerger ? |
| P543 | En immersion, un débit continu persistant fait chuter rapidement la pression du bloc. Quelle priorité pour la palanquée ? |
| P544 | Dans un tableau de dépannage, que signifie « cause probable » face à un symptôme tel qu’une fuite ou l’absence d’air ? |
| P545 | À 20 m dans le modèle 1 bar en surface et +1 bar/10 m, un détendeur a une MP de 9,5 bar au-dessus de l’ambiante. Délivre-t-il 12,5 bar absolus dans la bouche ? |
| P627 | Modèle fictif : premier étage réglé à 9 bar au-dessus de l’ambiante, à 20 m. Prendre 1 bar en surface et +1 bar/10 m. Quelle est sa MP absolue ? |
| P627 | Modèle fictif : à 40 m, la MP absolue vaut 14 bar. Prendre 1 bar en surface et +1 bar/10 m. Quelle est la MP relative à l’ambiante ? |

## Contrôles et publication

`make check` réussi : 301 cartes valides, 13 tests, lint/types/schéma conformes.
Build inspecté : 301 GUID uniques, 38 nouvelles notes aux champs HTML complets ;
SVG autonome présent dans la note P508 sans échappement.
`make push` réussi : import du package et synchronisation AnkiWeb.
