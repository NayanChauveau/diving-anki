# Chapitre 05 — Flottabilité

6 octobre 2026. 25 cartes (18 basic, 7 QCM), dont huit exercices, dans `Plongée::N2::Physique`.
Les 23 objectifs du catalogue sont couverts. Rédaction en draft, puis passe critique distincte
par le même agent avant reviewed ; cela ne constitue pas une validation par un tiers.

## Sources

- S1, Théorie N2 Stade de Vanves 2024, p.8–9 : poids apparent, Archimède, néoprène,
  gilet, poumon-ballast et caisson. Extrait relu.
- S3, CPDA Notions de physique 2024, p.4–6 (imprimées 6–8) : états de flottabilité,
  équipements et lestage. Extrait relu.
- [OpenStax, University Physics 1, §14.4](https://openstax.org/books/university-physics-volume-1/pages/14-4-archimedes-principle-and-buoyancy) : vérification des relations de physique.
- [DAN, Weight Up!](https://dan.org/alert-diver/article/weight-up/) : lestage, configuration,
  eau salée, consommation et contrôle en fin de plongée.
- [DAN, Lack of Buoyancy Control](https://dan.org/health-medicine/health-resource/smart-guides/7-mistakes-divers-make-and-how-to-avoid-them/4-lack-of-buoyancy-control/) : effets du néoprène et du gaz consommé.
- [DAN, Lung Expansion Injuries](https://dan.org/alert-diver/article/lung-expansion-injuries/) : blocage respiratoire et expansion pulmonaire.
- [DAN World, What is a DSMB?](https://world.dan.org/alert-diver/article/popping-the-question-what-is-a-dsmb/) : traction et risque de fil bloqué au lancement.

Sources web consultées le 6 octobre 2026 ; formulations originales, pas de reproduction de
procédure complète de lestage, relevage, lancement de parachute ou assistance.

## Corrections et limites des supports — V05

- S3 dit que passer de l’eau douce à la mer permet de retirer 2–3 kg : direction inversée.
  Une eau plus dense accroît la poussée à volume égal ; le besoin de lest augmente généralement.
  Aucune correction fixe universelle n’est retenue.
- Les supports assimilent masse et poids. Les cartes distinguent kg et N. Dans les exercices
  numériques, g = 10 N/kg est donné lorsque nécessaire. L’équilibre peut aussi se résoudre en
  égalant masse totale et masse d’eau déplacée : pas besoin d’introduire des kg de force implicites.
- Un objet à flottabilité positive entièrement immergé tend à remonter ; ne pas assimiler cela
  à un objet déjà en équilibre à la surface. P138 précise état initial immobile et liberté de mouvement.
- Le lest ajouté déplace lui-même de l’eau. L’exercice de caisson simplifié néglige explicitement
  ce volume ; un second exercice le prend en compte. La masse du flotteur et du gaz est négligée
  explicitement dans le calcul de portance.
- Pas de règle « 12 L = +1 kg par rapport au 15 L », « tout bloc acier plus lourd que tout alu »
  ni de perte universelle de 2–3 kg. Le changement de bloc sera détaillé sous P506.
- Poumon-ballast : respiration conservée, aucun blocage enseigné. La carte de parachute porte
  sur le risque de traction ; le conseil du support « bien expirer suffit » n’est pas repris.

## Couverture et intérêt de chaque carte

| Objectif | Suffixe d’ID après `n2-flottabilite-` | Apport |
| --- | --- | --- |
| P133 + P149 | poids-reel-apparent-001 | Apparent allègement sans perte de masse du bloc fermé |
| P134 | archimede-001 | Poussée = poids du fluide déplacé ; direction au verso |
| P136 | relation-poids-apparent-001 | Bilan signé et unités de force |
| P138 | signe-001 | Signe négatif du poids apparent ≠ flottabilité négative |
| P142 | calcul-cinq-kg-001 | Calcul avec tendance à couler |
| P142 | calcul-deux-kg-001 | Pratique avec tendance à remonter |
| P142 | calcul-neutre-001 | Pratique avec équilibre, forces non nulles |
| P145 | volume-portance-001 | Volume supplémentaire pour neutraliser 8 kg / 5 L |
| P146 | lest-caisson-001 | Masse de lest, volume du lest négligé |
| P147 | volume-double-001 | Variation de la poussée sans conclusion abusive sur le mouvement |
| P151 + P152 | neoprene-001 | Compression et expansion du même matériau |
| P154 | gilet-001 | Transfert interne de gaz : masse globale conservée, volume accru |
| P155 | poumon-ballast-001 | Volume pulmonaire en circuit ouvert, expiration au verso |
| P157 | respiration-001 | Comprendre pourquoi le réglage ne doit pas devenir une apnée |
| P158 | bloc-consomme-001 | Gaz consommé, masse moindre et volume extérieur stable |
| P162 | combinaison-lest-001 | Réévaluation du lestage sans coefficient universel |
| P163 | eau-douce-mer-001 | Sens de correction et erreur du support |
| P166 | carnet-lestage-001 | Configuration et conditions nécessaires à une note réutilisable |
| P168 | parachute-traction-001 | Lien mécanique entre parachute et plongeur |
| P169 | perte-lest-001 | Perte de poids supérieure à la perte de poussée |
| P170 | surlestage-001 | Effort malgré la compensation du gilet |
| P172 + P171 | palier-bloc-allege-001 | Comprendre une difficulté de fin de plongée |
| P145 | volume-neutre-001 | Calcul inverse masse → volume neutre |
| P146 | volume-lest-001 | Bilan avec volume du lest explicitement non nul |
| P163 | calcul-eau-salee-001 | Calcul avec masse volumique différente de 1 kg/L |

Les exercices multiples sont volontaires selon la calibration du 6 octobre. Ils ne créent
pas d’objectifs supplémentaires dans le total du catalogue. P143/P144 restent rattachés à P142.
P149 → P133, P152 → P151 et P171 → P172 évitent trois cartes paraphrasant le même mécanisme.
Les 77 cartes précédentes ne testent pas ces bilans de flottabilité.

P154/P151 préparent P186/P187 du chapitre gaz : les futures cartes devront travailler le
réglage ou une application distincte plutôt que refaire les mêmes explications. P157 introduit
le risque d’apnée ; les cartes de barotraumatisme devront apporter mécanisme, reconnaissance
ou prévention distincts. P506 reste prévu pour le changement de bloc.

## Relecture et calculs

Chaque recto/verso et chaque distracteur relus. P168 et P172 passent en basic : les choix
initiaux permettaient une élimination trop facile. Le troisième choix de P154 teste désormais
une erreur de périmètre (masse du gilet seul contre masse totale de l’équipement).
Les hypothèses distinguent volume intérieur du bloc et volume extérieur immergé ; les cas
de calcul supposent une immersion totale. Le sens positif du poids apparent est annoncé.

Vérification distincte des huit résultats par bilan de forces avec Decimal :

- 5 kg / 3 L : 50 − 30 = +20 N.
- 2 kg / 3 L : 20 − 30 = −10 N.
- 3 kg / 3 L : 30 − 30 = 0 N.
- Portance : 80 − (5 + 3) × 10 = 0 N.
- Lest négligé en volume : (1,5 + 1,5) × 10 − 3 × 10 = 0 N.
- Volume neutre 6 L : 60 − 6 × 10 = 0 N.
- Lest de volume 0,1 L : (1,5 + 1,6) × 10 − (3 + 0,1) × 10 = 0 N.
- Eau à 1,025 kg/L : 40 − 4 × 1,025 × 10 = −1 N.

## Vérifications techniques et publication

`make check` réussi : 102 cartes valides, 13 tests réussis, lint/types/schéma conformes.
Build inspecté : 102 GUID uniques, 25 nouvelles notes aux champs HTML recto/verso complets,
sept QCM avec une seule réponse correcte. Inspection des champs générés, pas de contrôle
visuel dans l’interface Anki. `make push` réussi : 102 notes importées, AnkiWeb synchronisé.
