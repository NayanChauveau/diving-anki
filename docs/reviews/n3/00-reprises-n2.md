# Reprise initiale des cartes N2 pour le socle N3

Revue du **6 octobre 2026**, sur le catalogue de 308 notes au commit `bfe402a`.

## Résultat

Les **164 candidates R** du tri initial sont retenues avec `levels: [N2, N3]`.
Aucune note supplémentaire : le paquet reste à **308 notes**, dont 308 N2 et 164 N3.
Aucune appartenance N4 n’est attribuée. Les fichiers, IDs, types de notes, catégories,
modèles et GUIDs sont conservés ; la reprise ajoute un tag de niveau à la note existante.
L’historique reste commun dans la même collection Anki après import des mises à jour.

Cette première sélection N3 est **partielle** : elle reprend le socle déjà rédigé.
Les prérogatives N3, l’organisation sans DP, les exercices de gaz profonds à deux,
les approfondissements de désaturation et les compléments de secours restent à réaliser.
La reprise ne valide pas à elle seule la couverture complète du diplôme.

## Relecture et sources

Relecture de l’intégralité des rectos, versos, explications et choix des 164 candidates,
avec leurs références et revues N2. Vérification de leur pertinence dans le
[MFT N3 FFESSM, décembre 2025](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/fcc5f7d1-a03f-483a-9acc-008db991e5ac)
(N3-S01, pages consignées par chapitre ci-dessous et dans les YAML).
Les références factuelles précises des cartes restent celles de leurs revues N2 ;
la référence MFT ajoutée atteste l’applicabilité au N3, sans remplacer ces sources.

Contrôles ciblés renouvelés le 6 octobre :

- [Code du sport A322-80](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000025393859) : fourniture de gaz sans partage d’embout pour les autonomes et les encadrés au-delà de 20 m ; distinction avec l’équipement de l’encadrant.
- [CMPN FFESSM, conduite à tenir en cas d’accident](https://medical.ffessm.fr/cat-accident-de-plongee-bouteille-ou-recycleur) et [RIFAP, mai 2026](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/f65d4fd1-beec-4dff-a803-b36101f71f88), p.24, 26–29, 32 : alerte, absence de réimmersion d’un plongeur symptomatique, oxygène et surveillance. Aucun nouveau protocole détaillé de réanimation ajouté.
- [DAN, vol après plongée](https://world.dan.org/health-medicine/health-resource/health-safety-guidelines/guidelines-for-flying-after-diving/) : conservation du contexte explicite de la carte (plongées répétitives sans palier obligatoire, absence de symptômes, altitude cabine précisée). Le délai enseigné n’est pas étendu aux plongées avec décompression obligatoire.

Les calculs existants ont été relus avec leurs hypothèses explicites ; les méthodes
pression/profondeur, Boyle, consommation ramenée à la surface, réserve en litres,
phases et arrondis de tables restent valables indépendamment du niveau.
Les séries de calcul sont conservées lorsqu’elles font travailler une opération différente.
Les règles propres à une notice, aux MN90 ou à une activité avec DP gardent leur contexte.
Aucune paraphrase d’un fait simple n’est créée.

Deux ajustements de formulation, sans changement d’objectif :

- `n2-organisation-gaz-equipier-001` : l’explication décrit tous les plongeurs visés par la question, plutôt que seulement les N2.
- `n2-barotraumatismes-alerte-oxygene-001` : prévenir le DP **s’il est présent** ; alerte des secours et prise en charge restent prioritaires même sans DP.

## Travail encore ouvert

Les **7 A** demandent une adaptation de contexte et les **8 V** restent hors sélection N3
jusqu’à résolution des divergences G03–G06. Les 109 P et 20 H restent N2 ; ce tri n’est
pas un héritage automatique de tout N2 vers N3. La décision initiale du CSV est conservée
pour retracer la préparation ; `etat_n3` et `revue_n3` donnent maintenant l’issue de cette passe.
Le catalogue N3 peut conduire à reprendre d’autres P lors d’un lot ultérieur, si l’objectif
est commun et utile (notamment le principe des GF) ; ces cartes ne sont pas encore N3.

## Liste finale du lot

| Chapitre N2 | Notes partagées | Pages MFT N3 |
| --- | ---: | --- |
| 02 | 11 | 9, 12, 15 |
| 03 | 8 | 12, 14, 15 |
| 04 | 12 | 8, 13, 15 |
| 05 | 9 | 8, 13, 14, 15 |
| 06 | 15 | 8, 13, 15 |
| 07 | 11 | 10, 11, 15 |
| 08 | 9 | 10, 11, 15 |
| 09 | 6 | 10, 11, 15 |
| 10 | 10 | 11, 15 |
| 11 | 23 | 10, 11, 15 |
| 12 | 10 | 9, 13, 15 |
| 13 | 13 | 9, 13, 15 |
| 14 | 4 | 9, 13, 15 |
| 15 | 7 | 8, 12, 15 |
| 16 | 8 | 8, 12, 15 |
| 17 | 7 | 9, 13 |
| 18 | 1 | 8, 12 |

| ID permanent | Objectif initial | Chapitre | Issue |
| --- | --- | --- | --- |
| `n2-organisation-palanquee-001` | P028 | 02 | Partagée N2/N3 |
| `n2-organisation-melanges-contraintes-001` | P030 | 02 | Partagée N2/N3 |
| `n2-organisation-plan-secours-001` | P041 | 02 | Partagée N2/N3 |
| `n2-organisation-vhf-001` | P043 | 02 | Partagée N2/N3 |
| `n2-organisation-oxygene-capacite-001` | P045 | 02 | Partagée N2/N3 |
| `n2-organisation-fiche-evacuation-001` | P047 | 02 | Partagée N2/N3 |
| `n2-organisation-bloc-secours-001` | P048 | 02 | Partagée N2/N3 |
| `n2-organisation-tables-assistance-001` | P050 | 02 | Partagée N2/N3 |
| `n2-organisation-gilet-surface-001` | P052 | 02 | Partagée N2/N3 |
| `n2-organisation-gaz-equipier-001` | P053 | 02 | Partagée N2/N3 |
| `n2-organisation-parachute-palanquee-001` | P056 | 02 | Partagée N2/N3 |
| `n2-documents-licence-affiliation-001` | P063 | 03 | Partagée N2/N3 |
| `n2-documents-assurance-rc-aia-001` | P064 | 03 | Partagée N2/N3 |
| `n2-documents-zones-reglementees-001` | P069 | 03 | Partagée N2/N3 |
| `n2-documents-prelevements-observation-001` | P070 | 03 | Partagée N2/N3 |
| `n2-documents-decouverte-archeologique-001` | P071 | 03 | Partagée N2/N3 |
| `n2-documents-peche-scaphandre-001` | P073 | 03 | Partagée N2/N3 |
| `n2-documents-distance-navires-locale-001` | P076 | 03 | Partagée N2/N3 |
| `n2-documents-suivi-bloc-001` | P078 | 03 | Partagée N2/N3 |
| `n2-pression-altitude-001` | P105 | 04 | Partagée N2/N3 |
| `n2-pression-hydrostatique-001` | P107 | 04 | Partagée N2/N3 |
| `n2-pression-absolue-six-metres-001` | P110 | 04 | Partagée N2/N3 |
| `n2-pression-profondeur-absolue-001` | P123 | 04 | Partagée N2/N3 |
| `n2-pression-double-atmosphere-001` | P127 | 04 | Partagée N2/N3 |
| `n2-pression-boyle-pressions-001` | P128 | 04 | Partagée N2/N3 |
| `n2-pression-absolue-vingt-metres-001` | P110 | 04 | Partagée N2/N3 |
| `n2-pression-absolue-trente-trois-metres-001` | P110 | 04 | Partagée N2/N3 |
| `n2-pression-inverse-deux-huit-bars-001` | P123 | 04 | Partagée N2/N3 |
| `n2-pression-inverse-quatre-bars-001` | P123 | 04 | Partagée N2/N3 |
| `n2-pression-absolue-lac-001` | P110 | 04 | Partagée N2/N3 |
| `n2-pression-inverse-lac-001` | P123 | 04 | Partagée N2/N3 |
| `n2-flottabilite-neoprene-001` | P151 | 05 | Partagée N2/N3 |
| `n2-flottabilite-respiration-001` | P157 | 05 | Partagée N2/N3 |
| `n2-flottabilite-bloc-consomme-001` | P158 | 05 | Partagée N2/N3 |
| `n2-flottabilite-combinaison-lest-001` | P162 | 05 | Partagée N2/N3 |
| `n2-flottabilite-eau-douce-mer-001` | P163 | 05 | Partagée N2/N3 |
| `n2-flottabilite-parachute-traction-001` | P168 | 05 | Partagée N2/N3 |
| `n2-flottabilite-surlestage-001` | P170 | 05 | Partagée N2/N3 |
| `n2-flottabilite-palier-bloc-allege-001` | P172 | 05 | Partagée N2/N3 |
| `n2-flottabilite-calcul-eau-salee-001` | P163 | 05 | Partagée N2/N3 |
| `n2-gaz-loi-boyle-001` | P175 | 06 | Partagée N2/N3 |
| `n2-gaz-conditions-001` | P176 | 06 | Partagée N2/N3 |
| `n2-gaz-debit-vingt-001` | P193 | 06 | Partagée N2/N3 |
| `n2-gaz-debit-trente-001` | P193 | 06 | Partagée N2/N3 |
| `n2-gaz-stock-nominal-001` | P195 | 06 | Partagée N2/N3 |
| `n2-gaz-stock-quinze-001` | P195 | 06 | Partagée N2/N3 |
| `n2-gaz-duree-fond-planification-001` | P201 | 06 | Partagée N2/N3 |
| `n2-gaz-debit-variable-001` | P203 | 06 | Partagée N2/N3 |
| `n2-gaz-chute-pression-001` | P205 | 06 | Partagée N2/N3 |
| `n2-gaz-comparaison-equipiers-001` | P206 | 06 | Partagée N2/N3 |
| `n2-gaz-stock-utilisable-001` | P630 | 06 | Partagée N2/N3 |
| `n2-gaz-deux-phases-001` | P633 | 06 | Partagée N2/N3 |
| `n2-gaz-reserve-volumes-001` | P634 | 06 | Partagée N2/N3 |
| `n2-gaz-deux-equipiers-001` | P635 | 06 | Partagée N2/N3 |
| `n2-gaz-consommation-remontee-001` | P641 | 06 | Partagée N2/N3 |
| `n2-barotraumatismes-mecanisme-001` | P207 | 07 | Partagée N2/N3 |
| `n2-barotraumatismes-sinus-descente-001` | P220 | 07 | Partagée N2/N3 |
| `n2-barotraumatismes-rhume-equilibrage-001` | P230 | 07 | Partagée N2/N3 |
| `n2-barotraumatismes-vertige-alternobarique-001` | P233 | 07 | Partagée N2/N3 |
| `n2-barotraumatismes-surpression-mecanisme-001` | P243 | 07 | Partagée N2/N3 |
| `n2-barotraumatismes-faible-profondeur-001` | P245 | 07 | Partagée N2/N3 |
| `n2-barotraumatismes-signes-respiratoires-001` | P249 | 07 | Partagée N2/N3 |
| `n2-barotraumatismes-signes-neurologiques-001` | P250 | 07 | Partagée N2/N3 |
| `n2-barotraumatismes-alerte-oxygene-001` | P252 | 07 | Partagée N2/N3 |
| `n2-barotraumatismes-amelioration-symptomes-001` | P252 | 07 | Partagée N2/N3 |
| `n2-barotraumatismes-victime-non-respirante-001` | P252 | 07 | Partagée N2/N3 |
| `n2-essoufflement-profondeur-001` | P261 | 08 | Partagée N2/N3 |
| `n2-essoufflement-co2-001` | P262 | 08 | Partagée N2/N3 |
| `n2-essoufflement-effort-001` | P263 | 08 | Partagée N2/N3 |
| `n2-essoufflement-air-pollue-001` | P267 | 08 | Partagée N2/N3 |
| `n2-essoufflement-signes-001` | P268 | 08 | Partagée N2/N3 |
| `n2-essoufflement-panique-001` | P270 | 08 | Partagée N2/N3 |
| `n2-essoufflement-premiers-signes-001` | P272 | 08 | Partagée N2/N3 |
| `n2-essoufflement-assistance-001` | P274 | 08 | Partagée N2/N3 |
| `n2-essoufflement-courant-001` | P277 | 08 | Partagée N2/N3 |
| `n2-froid-signes-001` | P283 | 09 | Partagée N2/N3 |
| `n2-froid-fin-frissons-001` | P286 | 09 | Partagée N2/N3 |
| `n2-froid-protection-001` | P289 | 09 | Partagée N2/N3 |
| `n2-froid-interactions-001` | P292 | 09 | Partagée N2/N3 |
| `n2-froid-sortie-001` | P293 | 09 | Partagée N2/N3 |
| `n2-froid-rechauffement-001` | P295 | 09 | Partagée N2/N3 |
| `n2-narcose-dalton-001` | P302 | 10 | Partagée N2/N3 |
| `n2-narcose-partielle-vingt-001` | P302 | 10 | Partagée N2/N3 |
| `n2-narcose-effets-001` | P308 | 10 | Partagée N2/N3 |
| `n2-narcose-variabilite-001` | P309 | 10 | Partagée N2/N3 |
| `n2-narcose-capacites-001` | P313 | 10 | Partagée N2/N3 |
| `n2-narcose-conditions-001` | P316 | 10 | Partagée N2/N3 |
| `n2-narcose-medicaments-001` | P319 | 10 | Partagée N2/N3 |
| `n2-narcose-reaction-001` | P321 | 10 | Partagée N2/N3 |
| `n2-narcose-equipier-001` | P325 | 10 | Partagée N2/N3 |
| `n2-narcose-apres-sortie-001` | P326 | 10 | Partagée N2/N3 |
| `n2-add-henry-001` | P328 | 11 | Partagée N2/N3 |
| `n2-add-profondeur-001` | P333 | 11 | Partagée N2/N3 |
| `n2-add-duree-001` | P334 | 11 | Partagée N2/N3 |
| `n2-add-tissus-001` | P335 | 11 | Partagée N2/N3 |
| `n2-add-apres-sortie-001` | P336 | 11 | Partagée N2/N3 |
| `n2-add-poumons-001` | P337 | 11 | Partagée N2/N3 |
| `n2-add-bulles-001` | P338 | 11 | Partagée N2/N3 |
| `n2-add-froid-effort-001` | P341 | 11 | Partagée N2/N3 |
| `n2-add-modele-001` | P343 | 11 | Partagée N2/N3 |
| `n2-add-retard-001` | P344 | 11 | Partagée N2/N3 |
| `n2-add-peau-001` | P346 | 11 | Partagée N2/N3 |
| `n2-add-oreille-interne-001` | P350 | 11 | Partagée N2/N3 |
| `n2-add-fatigue-001` | P354 | 11 | Partagée N2/N3 |
| `n2-add-oxygene-001` | P359 | 11 | Partagée N2/N3 |
| `n2-add-transmission-001` | P362 | 11 | Partagée N2/N3 |
| `n2-add-equipiers-001` | P365 | 11 | Partagée N2/N3 |
| `n2-add-evacuation-001` | P368 | 11 | Partagée N2/N3 |
| `n2-add-remontee-001` | P369 | 11 | Partagée N2/N3 |
| `n2-add-effort-surface-001` | P370 | 11 | Partagée N2/N3 |
| `n2-add-apnee-001` | P371 | 11 | Partagée N2/N3 |
| `n2-add-yoyo-001` | P374 | 11 | Partagée N2/N3 |
| `n2-add-avion-001` | P376 | 11 | Partagée N2/N3 |
| `n2-add-articulation-001` | P377 | 11 | Partagée N2/N3 |
| `n2-tables-profil-carre-001` | P381 | 12 | Partagée N2/N3 |
| `n2-tables-duree-001` | P384 | 12 | Partagée N2/N3 |
| `n2-tables-arrondis-001` | P386 | 12 | Partagée N2/N3 |
| `n2-tables-domaine-001` | P388 | 12 | Partagée N2/N3 |
| `n2-tables-gps-001` | P395 | 12 | Partagée N2/N3 |
| `n2-tables-majoration-001` | P405 | 12 | Partagée N2/N3 |
| `n2-tables-variables-001` | P407 | 12 | Partagée N2/N3 |
| `n2-tables-successive-001` | P414 | 12 | Partagée N2/N3 |
| `n2-tables-intervalle-arrondi-001` | P414 | 12 | Partagée N2/N3 |
| `n2-tables-successive-duree-maximale-001` | P642 | 12 | Partagée N2/N3 |
| `n2-ordinateurs-profil-001` | P415 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-affichages-001` | P418 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-gaz-001` | P423 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-historique-001` | P427 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-controle-001` | P430 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-collectif-001` | P432 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-differences-001` | P433 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-dtr-augmente-001` | P438 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-ndl-air-001` | P439 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-sonde-001` | P440 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-manuel-001` | P443 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-plafond-lecture-001` | P644 | 13 | Partagée N2/N3 |
| `n2-ordinateurs-plafonds-differents-001` | P645 | 13 | Partagée N2/N3 |
| `n2-remontees-anormales-references-001` | P454 | 14 | Partagée N2/N3 |
| `n2-remontees-anormales-yoyos-001` | P463 | 14 | Partagée N2/N3 |
| `n2-remontees-anormales-confort-001` | P465 | 14 | Partagée N2/N3 |
| `n2-remontees-anormales-symptomes-001` | P472 | 14 | Partagée N2/N3 |
| `n2-gonflage-blocs-compresseur-001` | P474 | 15 | Partagée N2/N3 |
| `n2-gonflage-blocs-pression-001` | P479 | 15 | Partagée N2/N3 |
| `n2-gonflage-blocs-materiau-001` | P483 | 15 | Partagée N2/N3 |
| `n2-gonflage-blocs-bi-001` | P484 | 15 | Partagée N2/N3 |
| `n2-gonflage-blocs-chaleur-chocs-001` | P494 | 15 | Partagée N2/N3 |
| `n2-gonflage-blocs-periodicites-001` | P500 | 15 | Partagée N2/N3 |
| `n2-gonflage-blocs-date-depassee-001` | P505 | 15 | Partagée N2/N3 |
| `n2-detendeurs-pressions-001` | P508 | 16 | Partagée N2/N3 |
| `n2-detendeurs-relative-absolue-001` | P512 | 16 | Partagée N2/N3 |
| `n2-detendeurs-compensation-001` | P526 | 16 | Partagée N2/N3 |
| `n2-detendeurs-eau-froide-001` | P532 | 16 | Partagée N2/N3 |
| `n2-detendeurs-revision-001` | P539 | 16 | Partagée N2/N3 |
| `n2-detendeurs-debit-continu-001` | P540 | 16 | Partagée N2/N3 |
| `n2-detendeurs-inspiration-difficile-001` | P542 | 16 | Partagée N2/N3 |
| `n2-detendeurs-incident-immersion-001` | P543 | 16 | Partagée N2/N3 |
| `n2-competences-transversales-communication-001` | P555 | 17 | Partagée N2/N3 |
| `n2-competences-transversales-retour-001` | P561 | 17 | Partagée N2/N3 |
| `n2-competences-transversales-reperes-001` | P562 | 17 | Partagée N2/N3 |
| `n2-competences-transversales-cap-retour-001` | P563 | 17 | Partagée N2/N3 |
| `n2-competences-transversales-cap-retour-ouest-001` | P563 | 17 | Partagée N2/N3 |
| `n2-competences-transversales-separation-001` | P564 | 17 | Partagée N2/N3 |
| `n2-competences-transversales-renoncer-001` | P569 | 17 | Partagée N2/N3 |
| `n2-lecture-pannes-flexible-001` | P580 | 18 | Partagée N2/N3 |

## Validation technique

- `make check` : lint, format, typage, schéma et validation des 308 cartes réussis ; 16 tests réussis, module optionnel d’import Anki non exécuté dans ce contrôle.
- `make build` : un paquet `dist/diving-fr.apkg`, 308 notes et 308 cartes.
- Inspection SQLite du paquet : 308 tags N2, 164 tags N3, aucun tag N4 ; correspondance exacte des 308 GUIDs avec les identités publiées.
- Contrôle du catalogue avant/après : aucun ID ajouté ou retiré ; contenus inchangés hormis les deux ajustements consignés. Contrôle des deux formulations dans les champs HTML exportés.
- CSV : 308 lignes uniques, dont 164 reprises marquées `partage_reviewed`.

Paquet généré localement ; ce lot n’a pas été importé dans la collection personnelle ni publié sur GitHub.

La [passe QCM globale](../QCM_GLOBALE.md) effectuée ensuite change le format de
présentation de certaines reprises, en conservant leurs modèles Anki et leur identité.

## Suite et clôture

Ce document conserve le bilan de la première passe (164 reprises). La clôture N3
porte le nombre de cartes communes à **204** ; les sept A et huit V sont résolues,
et 25 renforts P ajoutés. Voir [la couverture finale](COUVERTURE_N3.md) et les états
actuels du CSV commun pour la décision finale.
