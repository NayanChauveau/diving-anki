# Revue du chapitre 13 — ordinateurs

17 cartes, rédaction puis revue critique distincte le 6 octobre 2026.

## Sources

- S1 p.27–29, sonde et gestion de l’air.
- S1 p.28 ; coordination des paliers dans la palanquée.
- S1 p.28 ; obligations collectives.
- S1 p.29, acuité et lisibilité.
- S1 — Théorie N2 Stade de Vanves 2024, p.27–29.
- Shearwater — Petrel 2 Support, conversion pression/profondeur et salinité : https://shearwater.com/en-eu/pages/petrel-2-support
- Suunto — Zoop Novo User Guide, Alarms, alerts and notifications : https://us.suunto.com/pages/suunto-zoop-novo-user-guide
- Suunto — Zoop Novo User Guide, fonctions et contrôles, consulté le 2026-10-06 : https://us.suunto.com/pages/suunto-zoop-novo-user-guide
- Suunto — Zoop Novo, Ascent rate : https://www.suunto.com/Support/Product-support/suunto_zoop_novo/suunto_zoop_novo/features/ascent-rate/
- Suunto — Zoop Novo, Error state / algorithm lock : https://www.suunto.com/Support/Product-support/suunto_zoop_novo/suunto_zoop_novo/features/error-state-algorithm-lock/

## Vérification et améliorations

Le modèle est nommé pour les valeurs dépendantes de l’appareil : Zoop Novo, SLOW au-delà
 de 10 m/min, ER et verrouillage de décompression 48 h après sortie si plafond violé plus de
 3 min. P422 précise SLOW plutôt qu’une description graphique imprécise ; contrôle du manuel
 chapitre alarmes. P424 repose sur la FAQ officielle Petrel 2 : salinité = conversion pression
 en profondeur, sans attribuer ce réglage au Zoop. Fréquence d’enregistrement et cadence
 des calculs non confondues. Pas de limite universelle de deux/trois plongées, batterie ou lock.
 P444 réutilise P343 du chapitre 11, pas de nouvelle carte. La palanquée termine ensemble,
 en respectant les obligations et plafonds de chacun ; ne pas additionner mécaniquement
 les durées de tous les ordinateurs. P437 teste un écran avec mise à jour, pas une liste
 de minutes à additionner une fois. Contrôle de la cohérence des réglages avant immersion.
 Aucun screenshot fabricant recopié.

## Pertinence

Basic : lecture et rappel actif, aucune difficulté provenant de leurres absurdes.
Contextes précis ; sources détaillées hors recto, noms de modèle et champ nécessaires
conservés. Comparaison avec les chapitres publiés, aucun ID existant renommé.

| Objectif | Tâche distincte |
| --- | --- |
| P415 | Pourquoi un ordinateur peut-il donner une décompression différente d’une table pour une plongée qui remonte progressivement le long d’un tombant ? |
| P418 | Un écran affiche temps de plongée 24 min et temps restant sans palier 6 min à la profondeur actuelle. Que représentent ces deux valeurs ? |
| P422 | Sur un Suunto Zoop Novo, une alarme sonore s’accompagne du message SLOW. Que signale-t-elle et quelle action attend-elle ? |
| P423 | Pourquoi vérifier le gaz sélectionné sur l’ordinateur avant de plonger, même si la profondeur affichée paraît correcte ? |
| P424 | Sur un appareil offrant un réglage de salinité, à quoi sert ce réglage dans l’affichage de profondeur ? |
| P427 | Entre deux plongées rapprochées, pourquoi remplacer son ordinateur par celui d’un équipier peut-il fausser la décompression affichée ? |
| P430 | Avant de s’immerger avec son ordinateur, quels contrôles évitent de découvrir un mauvais réglage ou un affichage inutilisable sous l’eau ? |
| P432 | Votre ordinateur n’indique plus de palier obligatoire, mais celui de votre équipier en impose encore un. Pourquoi ne remontez-vous pas seul ? |
| P433 | Deux plongeurs restent côte à côte pendant une plongée mais leurs ordinateurs annoncent des paliers différents. Quelles différences peuvent l’expliquer ? |
| P437 | Deux équipiers doivent rester à 3 m : A affiche encore 2 min de palier obligatoire et B 5 min. Le gaz est suffisant et aucun autre plafond n’est indiqué. Après 2 min, comment organiser la suite ? |
| P438 | Pendant l’exploration, la durée totale de remontée affichée augmente. Quelle conséquence pour la décision de rester au fond ? |
| P439 | Un ordinateur annonce 12 min sans palier, mais la réserve de gaz convenue sera atteinte dans 4 min à la consommation actuelle. Quelle contrainte commande la décision de fin d’exploration ? |
| P440 | Pourquoi un ordinateur sans liaison de pression avec le bloc ne peut-il pas connaître directement le gaz encore disponible ? |
| P441 | Un Suunto Zoop Novo reste plus de 3 min au-dessus de son plafond de décompression et affiche ER. Quelle information de décompression devient indisponible et pour quelle durée annoncée par le manuel ? |
| P443 | Vous empruntez pour la première fois un modèle d’ordinateur différent. Quelles informations de son manuel devez-vous maîtriser pour gérer la remontée ? |
| P445 | Pourquoi tester la lecture de l’écran avec son masque et sa correction visuelle avant de choisir un ordinateur ? |
| P446 | Si l’on envisage une formation nitrox plus tard, quel point vérifier dans les fonctions de l’ordinateur ? |

## Vérification technique

`make check` réussi : 263 cartes valides, 13 tests, lint/types/schéma conformes.
Build inspecté : 263 GUID uniques, 27 notes nouvelles avec champs HTML complets.
`make push` réussi : import et synchronisation AnkiWeb.

## Complément de clôture

Deux cartes MFT, P637/P638, portent ce chapitre à 19 cartes. Vérification, sources et
références dans COUVERTURE_FINALE_N2.md. Pas de modification des IDs publiés.
