# Revue du chapitre 10 — narcose

Revue factuelle et passe critique distincte de la rédaction, le 6 octobre 2026.
14 cartes nouvelles en français, dans Prévention des accidents.

## Sources consultées

- BSAC — Safe diving guide, Gas, consulté le 2026-10-06 : https://www.bsac.com/safety/safe-diving-guide/gas/
- DAN World — Decompression Illness : https://world.dan.org/health-medicine/health-resources/diseases-conditions/decompression-illness-what-is-it-and-what-is-the-treatment/
- DAN — Back to Basics, narcose, consulté le 2026-10-06 : https://dan.org/alert-diver/article/back-to-basics/
- FFESSM CMPN — CAT accident de plongée bouteille ou recycleur, consulté le 2026-10-06 : https://medical.ffessm.fr/cat-accident-de-plongee-bouteille-ou-recycleur
- FFESSM CMPN — Je prends des médicaments, consulté le 2026-10-06 : https://medical.ffessm.fr/je-prends-des-medicaments
- S1 — Théorie N2 Stade de Vanves 2024, p.18–19.
- UCalgary — The Pressure of a Mixture of Gases: Dalton’s Law, consulté le 2026-10-06 : https://chem-textbook.ucalgary.ca/chapter-9-main/the-pressure-of-a-mixture-of-gases-daltons-law/
- https://www.noaa.gov/jetstream/atmosphere

## Décisions et corrections

P324 est fusionné avec P313 (euphorie trompeuse). Composition de S1 corrigée avec NOAA : environ 78 % N₂, 21 % O₂, 1 % autres gaz. Aucune profondeur garantie sans narcose, ni guérison garantie à 30 m. P319 utilise la CMPN, sans attribuer une narcose à tous les traitements. Trois applications numériques vérifiées : 0,20 × 4 = 0,8 ; 0,80 × 5 = 4 ; 0,21 × 3 = 0,63 bar. Vérification inverse : résultat/fraction = pression totale.

## Pertinence et relecture

Rappel actif en basic : pas de QCM dont les leurres seraient éliminables au bon sens.
Mécanisme, reconnaissance, prévention et décision sont séparés uniquement quand la tâche
apporte une connaissance différente. Comparaison avec les sept chapitres publiés ;
les conduites de secours communes réutilisent P252. Aucun ID existant modifié.
Questions situées, réponses sans préambule de source ni commentaire éditorial.

| Objectif | Question et apport retenu |
| --- | --- |
| P299 | Pourquoi le modèle « air = 80 % d’azote et 20 % d’oxygène » n’est-il pas sa composition exacte ? |
| P302 | Dans un mélange gazeux idéal, comment calcule-t-on la pression partielle d’un gaz ? |
| P304 | Dans le modèle d’air à 20 % d’oxygène, quelle est la pression partielle d’O₂ à 30 m ? Prendre 1 bar à la surface et +1 bar par 10 m. |
| P306 | Dans le modèle d’air à 80 % d’azote, quelle est la pression partielle d’azote à 40 m ? Prendre 1 bar à la surface et +1 bar par 10 m. |
| P302 | Un mélange idéal contient 21 % d’oxygène. Quelle est sa pression partielle d’oxygène à une pression totale de 3 bars absolus ? |
| P307 | À composition d’air inchangée, pourquoi la pression partielle d’azote augmente-t-elle à la descente ? |
| P308 | Pourquoi la narcose à l’air s’accentue-t-elle généralement avec la profondeur ? |
| P309 | Un plongeur n’a jamais ressenti de narcose à 30 m. Peut-il considérer cette profondeur comme un seuil garanti sans effet pour ses prochaines plongées ? |
| P313 | Pourquoi une euphorie inhabituelle en profondeur peut-elle être aussi inquiétante qu’une angoisse ? |
| P316 | Pourquoi fatigue, anxiété et manque de pratique récente doivent-ils inciter à choisir une plongée moins exigeante ? |
| P319 | Un médicament qui provoque somnolence ou ralentissement peut-il être considéré sans conséquence pour une plongée profonde ? |
| P321 | Lorsqu’une narcose est suspectée en immersion, quel changement de profondeur aide généralement à réduire ses effets ? |
| P325 | En profondeur, un équipier répond inhabituellement lentement aux signes et répète une manipulation inutile. Pourquoi faut-il intervenir plutôt que l’attendre passivement ? |
| P326 | Pourquoi une confusion ou une faiblesse persistante après la sortie de l’eau ne doit-elle pas être simplement attribuée à une narcose vécue au fond ? |

## Validation technique

`make check` réussi : 190 cartes valides, lint/types/schéma conformes et 13 tests.
Build inspecté : 190 GUID uniques, 36 notes nouvelles avec champs HTML complets.
Inspection HTML, sans prétendre à une vérification visuelle dans Anki.
`make push` réussi : import du package et synchronisation AnkiWeb.
