# Chapitre 06 — Gaz et autonomie en air

6 octobre 2026. 31 cartes (26 basic, 5 QCM), dont 20 exercices, dans `Plongée::N2::Physique`.
28 objectifs couverts. Rédaction en draft suivie d’une passe critique distincte par le même
agent ; pas de validation par un tiers. Les 102 IDs publiés précédemment sont conservés.

## Sources et vérifications — V06

- S1, Théorie N2 Stade de Vanves 2024, p.10–12 : compression, gilet, masque, oreilles,
  Boyle-Mariotte, stock et durées théoriques. Extrait relu.
- [NASA, Equation of State](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/equation-of-state/) : relation pression-volume et température/quantité constantes.
- [BSAC, So, you think you use too much gas?](https://www.bsac.com/news-and-blog/so-you-think-you-use-too-much-gas/), section How much gas do you use? : débit de référence × pression absolue × durée,
  somme des phases et mesures personnelles. Seules ces relations sont reprises, sans les
  moyennes physiologiques ou les recommandations de rythme respiratoire de l’article.
- [BSAC, Safe diving guide — Gas reserves](https://www.bsac.com/safety/safe-diving-guide/gas/) : besoin de réserve adapté aux blocs, phases et équipiers, variabilité du débit.
- [DAN, Lack of Buoyancy Control](https://dan.org/health-medicine/health-resource/smart-guides/7-mistakes-divers-make-and-how-to-avoid-them/4-lack-of-buoyancy-control/) : gaz du gilet et réglage progressif.
- [DAN World, Preventing Mask Squeeze](https://world.dan.org/id/alert-diver/article/preventing-mask-squeeze/) : apport d’air par le nez.
- [DAN, Ears and Diving](https://dan.org/health-medicine/health-resource/dive-medical-reference-books/ears-diving/ears-equalization/) : équilibrage précoce, doux, arrêt de descente en cas d’échec.
- [DAN, Breathe In, Breathe Out](https://dan.org/alert-diver/article/breathe-in-breathe-out/) : deuxième étage et pression ambiante.

Consultées le 6 octobre 2026. Le PDF BSAC ST5 trouvé par recherche n’a pas pu être ouvert
avec l’outil web ; il n’est pas cité comme document intégralement vérifié. Le complément de
source repose sur les pages HTML consultées et les relations de physique, pas sur ce PDF.

Les calculs sont des modèles de cours : gaz parfait, température constante, volumes de gaz
ramenés à 1 bar, pression ambiante absolue. Le volume intérieur du bloc se distingue du volume
de gaz ramené à 1 bar. Les différences de pressions manométriques d’un bloc donnent la quantité
prélevée via Vbloc × ΔP / 1 bar ; la référence atmosphérique se soustrait dans cette différence.

Le stock nominal Vbloc × pression du manomètre est explicitement une approximation de cours,
comme dans S1. Ce n’est pas une égalité exacte pour la quantité totale de molécules enfermées :
elle néglige notamment le gaz restant à pression ambiante et les écarts au gaz parfait à haute
pression. Les autres exercices utilisent des différences de pression ou un stock alloué donné.

Les débits de référence décrivent une ventilation donnée à 1 bar. Le débit prélevé dans le bloc,
ramené à 1 bar, est multiplié par Pamb / 1 bar. Les énoncés P193 distinguent explicitement litres
mesurés à la pression ambiante et litres ramenés à 1 bar.

Les seuils 60/70 bars sont des données fictives imposées par les exercices. Aucune règle BSAC
des tiers n’est transférée en règle FFESSM, aucune réserve universelle et aucune procédure de
demi-tour ou de partage d’air opérationnelle ne sont définies. Les calculs par phases excluent
explicitement les transitions et la réserve ; les durées couvrent seulement les phases annoncées.
V15 reste ouvert pour les procédures techniques ultérieures, sans bloquer ces modèles sourcés.

## Objectifs, apport et doublons

| Objectif | Cartes / apport |
| --- | --- |
| P175 | Inverse pression-volume et produit constant |
| P176 | Conditions de conservation ; ajout/purge change la quantité |
| P179 | 12 L → 20 m, 6 L → 10 m, 10 L → 40 m : entraînement à trois profondeurs |
| P182 | Expansion de 2 L à 20 m jusqu’à la surface |
| P183 | Passage entre deux profondeurs non nulles |
| P184 | Comparaison de deux remontées de 10 m avec volumes initiaux égaux |
| P185 | Récipient rigide fermé contre enveloppe souple |
| P186 | Ajustement progressif à la descente, pas seulement mécanisme de flottabilité |
| P187 | Purges répétées pendant la remontée : expansion du gaz restant |
| P188 | Apport au masque par le nez |
| P189 | Oreille moyenne, prévention précoce sans forcer |
| P190 | Délivrance à pression ambiante et application à 20 m |
| P193 | Deux conversions litres ambiants → litres à 1 bar, à 20 et 30 m |
| P195 | Deux estimations de stock, blocs de 12 et 15 L |
| P197 | Durée d’une phase isolée avec stock alloué |
| P200 | Rapport de durées surface / 40 m |
| P201 + P202 | Ce qui manque dans une division naïve tout le stock / débit au fond |
| P203 | Limite d’un débit observé au repos |
| P205 | Retrouver le débit de référence depuis une chute de manomètre |
| P206 | Comparer les équipiers avec blocs et débits différents |
| P630 | Stock utilisable au-dessus du seuil fourni |
| P631 | Durée combinant stock utilisable et conversion de débit |
| P632 | Pression initiale pour une phase et un seuil final donnés |
| P633 | Addition de deux phases à pressions différentes |
| P634 | Même ΔP, volumes de blocs différents |
| P635 | Addition des débits de deux équipiers, comparaison au stock alloué |
| P636 | Recalcul avec débit accru et différence de besoin |

P202 est absorbé dans P201 ; pas de carte séparée. Les variantes numériques sont volontaires
pour l’entraînement, sans nouveaux objectifs au catalogue. P128 du chapitre 04 teste déjà le
choix des pressions absolues ; il n’est pas recréé. P151/P154 du chapitre 05 testent les causes
physiques de flottabilité : P186/P187 travaillent l’ajustement au cours du déplacement.
Le chapitre barotraumatismes devra apporter reconnaissance, mécanisme ou prévention distincts
plutôt que recréer P188/P189. Comparaison réalisée avec les YAML des cinq chapitres existants.

## Passe critique et calculs

P186 et P188 passés en basic : les distracteurs initiaux étaient trop faciles. Modèle de gaz
parfait ajouté aux ballons ; température constante ajoutée au rapport de durées. Chaque QCM
relit les choix sous les mêmes hypothèses. Aucun préambule de source ni commentaire éditorial.

23 vérifications numériques distinctes en Decimal, par inversion/conservation :

- Ballons : 4 × 3 = 12 × 1 ; 3 × 2 = 6 × 1 ; 2 × 5 = 10 × 1.
- Remontée : 6 × 1 = 2 × 3. Entre profondeurs : 2 × 4 = 4 × 2.
- Comparaison : 4 × 1 = 2 × 2 ; 3 × 2 = 2 × 3.
- Débits : 60/3 = 20 ; 72/4 = 18 L/min de référence.
- Stocks : 2400/12 = 200 ; 2700/15 = 180 bars.
- Durée : 30 × 20 × 2 = 1200 L.
- Débit inverse : 20 × 3 × 10/12 = 50 bars consommés.
- Équipiers : 18 × 20 × 3/12 = 90 bars ; 15 × 30 × 3/15 = 90 bars.
- Stock au-dessus du seuil : 1560/12 + 70 = 200 bars.
- Durée avec seuil : 26 × 20 × 3/12 + 70 = 200 bars.
- Pression initiale : 12 × (135 − 60) = 20 × 3 × 15 = 900 L.
- Phases : 720 − 20 × 3 × 8 = 20 × 2 × 6 = 240 L.
- Volumes de réserve : 600/12 = 50 ; 750/15 = 50 bars.
- Deux équipiers : 630/3/3 = 70 = 30 + 40 L/min de référence.
- Débit accru : 300/3/10 = 10 = 30 − 20 L/min supplémentaires.

## Vérifications techniques et publication

`make check` réussi : 133 cartes valides, 13 tests, lint/types/schéma conformes.
Build inspecté : 133 GUID uniques, 31 notes nouvelles avec champs HTML complets,
cinq QCM avec une réponse correcte. Inspection des champs, pas de contrôle visuel Anki.
`make push` réussi : 133 notes importées et synchronisation AnkiWeb effectuée.
