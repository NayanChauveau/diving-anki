# Revue du chapitre 17 — Préparation collective

9 cartes nouvelles dont deux calculs de cap réciproque et le complément MFT P639.
Rédaction puis passe critique le 6 octobre 2026.

## Sources et limites résolues

- S2 p.1–2 : compétences, sans invention de séquence pratique complète.
- [MFT N2 mai 2026](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/d7c761c8-79ed-42f2-a675-90e4c6095a56),
  p.12–13 autonomie/planification, p.15–18 PE40 et intervention, p.19–20 théorie.
- [BSAC Going diving](https://www.bsac.com/safety/safe-diving-guide/going-diving/), checks
  et separation. La recherche de 30 secondes conseillée par BSAC n’est pas une règle
  universelle FFESSM : P564 teste le briefing d’une conduite commune, pas un délai inventé.
- [Suunto SK-8, guide multilingue](https://cdn.shopify.com/s/files/1/0850/4878/7229/files/SUUNTO_SK-SERIES_UG_MULTI.pdf?v=1714977581),
  p.11–13 Français : orientation préalable, repères, cap, alignements et dérive.
- [DAN Current Dives](https://dan.org/alert-diver/article/current-dives/), trajet et sortie.
- [DAN, What is a DSMB?](https://world.dan.org/alert-diver/article/popping-the-question-what-is-a-dsmb/),
  risques de ligne accrochée au plongeur et remontée incontrôlée.

## Passe critique et fusions

P547 réutilise contrôles P265/P430. P549 et P550 : P039 et P561 couvrent la planification
commune et le trajet, P432 les obligations ; le brouillon P550 donnait la réponse dans
l’énoncé, supprimé. P552 réutilise les exercices d’air ; P557 la flottabilité ; P560 P039 ;
P567 P272 ; P570 P054 ; P572 P432/P437. Les trois reprises P594/P606/P622 réutilisent
les cartes existantes, sans nouvelles paraphrases. Correspondances exactes dans l’audit final.

P562 amélioré vers l’alignement de repères stables, documenté par le manuel, plutôt que
une seule impression de direction. Calculs relus séparément : 70+180=250, puis
250+180 modulo 360=70 ; 300+180 modulo 360=120, puis 120+180=300.
Hypothèses sans dérive et obstacle explicitent le rôle du cap géométrique.
P565 teste un risque précis, pas une description entière de déploiement ; la pratique reste
avec l’encadrant. P569 distingue décision personnelle et autorisation du DP.

Basic, aucune difficulté due à des leurres faibles. Aucun ID publié renommé.

## Validation technique

`make check` réussi : 312 cartes valides, 13 tests, lint/types/schéma conformes.
Build N2 : 312 notes, aucun draft ; N3/N4 vides et indépendants.
Inspection des champs HTML, GUIDs uniques et 69 QCM à une seule bonne réponse.
`make push` réussi : package importé, AnkiWeb synchronisé.
