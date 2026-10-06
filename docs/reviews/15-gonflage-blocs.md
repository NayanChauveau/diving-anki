# Revue du chapitre 15 — gonflage-blocs

14 cartes nouvelles. Rédaction puis passe critique le 6 octobre 2026.

## Sources consultées

- Arrêté du 20 novembre 2017, version en vigueur au 2026-10-06, articles 5, 15 et 18 : https://www.legifrance.gouv.fr/loda/id/JORFTEXT000036128632
- DAN Europe — Transport routier personnel de bouteilles : https://alertdiver.eu/fr_FR/articles/comment-transporter-une-bouteille-de-plongee-regles-a-respecter/
- DAN — Breathing Gas Contamination, consulté le 2026-10-06 : https://dan.org/safety-prevention/diver-safety/psa/breathing-gas-contamination/
- FFESSM — Cahier des charges inspection des bouteilles métalliques, 4 décembre 2015 : https://tiv.ffessm.fr/Docs/CC-TIV-04-12-2015.pdf
- Roth Mions — Notice FC244 révision 9 janvier 2020, p.1, consultée le 2026-10-06 : https://roth2.com/wp-content/uploads/2021/06/Notice_FR-2020-V9-2.pdf
- S1 p.29, compresseur et tampons.
- S1 p.30 ; calcul de flottabilité du chapitre 05.
- S1 p.30 ; flottabilité chapitre 05.
- S1 p.30, mono/bi ; configuration conceptuelle.
- S1 — Théorie N2 Stade de Vanves 2024, p.29–30 ; tableau p.34 inspecté visuellement.

## Décisions et corrections

V13 : [arrêté consolidé du 20 novembre 2017](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000036128632),
 en vigueur au 6 octobre 2026, données mises à jour septembre 2025. Art.15 : inspection
 annuelle des bouteilles de plongée ; art.18 : 2 ans en régime ordinaire, 6 ans sous cahier
 des charges, et inspection avant réutilisation si plus d’un an. Le 5 ans de S1 est corrigé.
 Une simple inspection informelle ne confère pas ce régime. PS ≠ PT ; panne absente ne
 remplace pas la requalification. Art.5 et notice Roth : compétence/autorisation au gonflage,
 pas habilitation par brevet N2, ni interdiction nationale inventée de présence au local.
 Transport : question de protection du bloc en voiture à usage personnel ; source DAN
 Europe de 2015 et notice Roth, sans importer ses seuils ADR ou règles aériennes anciennes.
 Pas d’interdiction générale de transport gonflé. Chocs/corrosion/température recroisés
 notice Roth FC244 rev9, p.1. Pas de conseils de démontage, gravage ou repeinture d’un
 métal corrodé sans évaluation. Compresseur/tampon : principe physique de S1, pas
 manuel d’utilisation. Matériau ≠ flottabilité ; mono/bi ≠ indépendance de réserves.
 P488 fusionné P479 ; P482 P185/P195 ; P504 P479/P195.

## Pertinence et clarté

Rappel actif basic, pas de QCM avec leurres évidents. Questions concrètes et modèle nommé
quand il conditionne la réponse. Comparaison avec tous les YAML publiés ; fusions des
facts simples conservées ci-dessus, variantes numériques limitées et justifiées.
Aucun ID existant renommé.

| Objectif | Tâche retenue |
| --- | --- |
| P474 | Pourquoi une station de gonflage aspire-t-elle l’air loin de sources de fumées ou d’échappement ? |
| P477 | Quelle différence entre gonfler directement avec un compresseur et utiliser une batterie de bouteilles tampons ? |
| P479 | Un bloc est marqué PS 230 bar et PT 345 bar. Quelle pression fixe sa limite admissible de gonflage ? |
| P480 | Le brevet N2 suffit-il à autoriser l’utilisation autonome d’une station de gonflage du club ? |
| P483 | Le seul mot « aluminium » suffit-il à conclure qu’un bloc sera plus léger et moins négatif qu’un bloc acier ? |
| P484 | Deux bouteilles réunies en bi-bloc garantissent-elles automatiquement deux réserves indépendantes ? |
| P494 | Pourquoi éviter de laisser un bloc gonflé dans un véhicule surchauffé et de le faire tomber ? |
| P495 | Pourquoi un bloc vide ne doit-il pas rester robinet ouvert dans l’eau ou au fond d’un bateau mouillé ? |
| P496 | Pourquoi ne faut-il pas vider brutalement un bloc en ouvrant grand son robinet à l’air libre ? |
| P497 | Des éclats de peinture et de la rouille apparaissent sous le culot d’un bloc. Pourquoi ne suffit-il pas de recouvrir la zone de peinture ? |
| P500 | En France, pour un bloc métallique de plongée suivi selon le cahier des charges donnant droit au régime de six ans, quelles échéances distinguer de la requalification ordinaire ? |
| P502 | Pour transporter personnellement un bloc d’air gonflé en voiture, quelle précaution matérielle est essentielle ? |
| P505 | La date de requalification d’un bloc a dépassé l’échéance de son régime de suivi, mais il garde sa pression sans fuite. Peut-on le faire gonfler pour une dernière plongée ? |
| P506 | Vous remplacez votre bloc habituel par un autre modèle de même capacité intérieure. Pourquoi vérifier à nouveau le lestage ? |

## Contrôles et publication

`make check` réussi : 301 cartes valides, 13 tests, lint/types/schéma conformes.
Build inspecté : 301 GUID uniques, 38 nouvelles notes aux champs HTML complets ;
SVG autonome présent dans la note P508 sans échappement.
`make push` réussi : import du package et synchronisation AnkiWeb.
