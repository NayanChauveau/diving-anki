# Revue du chapitre 18 — lecture-pannes

3 cartes nouvelles. Rédaction puis passe critique le 6 octobre 2026.

## Sources consultées

- S1 p.31 et tableau p.34, conception avec chambre humide ouverte.
- S1 — Théorie N2 Stade de Vanves 2024, p.30–34 ; tableau p.34 inspecté visuellement.
- SCUBAPRO — Manuel détendeurs 2025 Rev Q, p.6–9 et 20 : https://johnsonoutdoors.widen.net/s/hlkmf7vhpb/sp_45101180_revq_reg_manual_202507_fra

## Décisions et corrections

Tableau S1 p.34 inspecté en image, puis comparé au tableau constructeur SCUBAPRO RevQ
 2025 p.20, rendu et inspecté. Ce dernier admet plusieurs causes d’entrée d’eau et de
 défaut d’alimentation, contrairement à l’unique premier étage bloqué indiqué dans S1.
 Pas de réparation interne autonome reprise depuis le cours. P577 → P542/P544 ;
 P581 → P544 ; P585 → schéma P508. Trois apports nouveaux : voies d’entrée d’eau,
 fuite vers une chambre humide explicitement ouverte à l’eau, flexible détérioré.
 P578 précise une conception à piston et formule la cause comme hypothèse physique,
 pas comme diagnostic certain pour n’importe quel détendeur étanche ou membrane.

## Pertinence et clarté

Rappel actif basic, pas de QCM avec leurres évidents. Questions concrètes et modèle nommé
quand il conditionne la réponse. Comparaison avec tous les YAML publiés ; fusions des
facts simples conservées ci-dessus, variantes numériques limitées et justifiées.
Aucun ID existant renommé.

| Objectif | Tâche retenue |
| --- | --- |
| P573 | De l’eau entre dans la bouche à l’inspiration sur un second étage. Quelles parties peuvent être en cause, au-delà de la seule purge ? |
| P578 | Dans un modèle de premier étage à piston dont la chambre humide est ouverte à l’eau, des bulles d’air sortent durablement par ses orifices. Que suggère ce passage de gaz ? |
| P580 | Un flexible présente une fissure ou un renflement visible. Pourquoi ne faut-il pas l’utiliser jusqu’à l’apparition d’une fuite importante ? |

## Contrôles et publication

`make check` réussi : 301 cartes valides, 13 tests, lint/types/schéma conformes.
Build inspecté : 301 GUID uniques, 38 nouvelles notes aux champs HTML complets ;
SVG autonome présent dans la note P508 sans échappement.
`make push` réussi : import du package et synchronisation AnkiWeb.
