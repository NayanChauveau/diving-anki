# Revue du chapitre 12 — Tables

20 cartes, dont huit exercices, rédigées puis relues le 6 octobre 2026.

## Sources et édition

S1 p.23–26 et images p.24–25. Complément primaire : [Tables et mode d’emploi
FFESSM, juillet 2005](https://ffessm-ctr-aura.fr/wp-content/uploads/2019/03/MN90.pdf),
auteurs Jean-Louis Blanchard et Francis Imbert, publié par la CTR AURA. Document complet,
8 pages ; mode d’emploi p.1–3, table principale p.4, tableaux I/II p.6, IV p.7,
conventions de calcul p.8. Pages p.4,6,7,8 rendues et inspectées visuellement.
La date de dépôt 2019 n’est pas la date d’édition. Les procédures anormales historiques
p.2–3 ne servent pas de conduite actuelle à l’ordinateur ; elles sont traitées au chapitre 14.

## Corrections et passe critique

- Le temps table inclut la descente. Remontée lente : intégrer sa durée jusqu’au premier palier.
- Arrondi durée et profondeur vers la valeur supérieure ; intervalle de surface vers
  l’inférieure ; azote résiduel vers la valeur supérieure. Éviter un vague « toujours arrondir ».
- À 12 h exactement, le mode d’emploi définit la plongée isolée « au minimum 12 h ».
  S1 dit successive <12 h. Les bornes sont fournies dans l’exercice, sans devinette d’édition.
- GPS = lettre pour le gaz résiduel, pas mesure directe des tissus. La majoration est fictive.
- P375 précise que deux plongées/24 h appartient aux MN90, pas à tout ordinateur.
- P413 : vérifier la DTR par trajets séparés : 108 s + 540 s + 30 s = 678 s,
  soit 11,3 min → 12 min. Cohérent avec 30 m / 30 min de la table principale.
- P414 : lecture visuelle H/2 h = 0,98 ; prendre 0,99 au tableau II ; 20 m → 22 min ;
  20 + 22 = 42 → 45 min ; table principale = 1 min à 3 m.
- P411 : 25 m/30 min = 2 min à 3 m, DTR 4, H. P412 : 20 m/40 min sans palier,
  45 min avec 1 min à 3 m. Valeurs relues sur l’image, pas sur un extrait OCR.

Questions situées dans les exercices MN90. Les extraits nécessaires sont inclus dans les
rectos et les données ne sont pas inventées. Basic favorise le calcul actif ; aucun distracteur
évident ajouté. Les deux exercices P414 travaillent des arrondis différents.
Les vitesses sont rattachées à la table et ne sont pas des consignes pour tout ordinateur.
Comparaison des onze YAML précédents : aucun doublon de calcul physique ou secours.

## Couverture

Tous les 18 objectifs du chapitre 12 et P375 sont couverts. P414 a deux applications.
V09 est clôturé après cette distinction de domaine ; V10 est clôturé pour ces exercices
à l’air au niveau de la mer, sans procédure nitrox/oxygène/altitude ajoutée.

## Vérification technique

`make check` réussi : 236 cartes valides, 13 tests et contrôles lint/types/schéma.
Build inspecté : 236 GUID uniques, 20 notes nouvelles aux champs HTML complets.
`make push` réussi : import et synchronisation AnkiWeb.
