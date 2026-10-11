# Recoupement des deux PDF N2 — 11 octobre 2026

## Résultat

Le commit préalable `43b39d7` a enregistré la revue N3 en cours ; le dépôt était propre avant cette extension.
Les **36 pages du cours** et les **8 pages des tables** ont été lues. Recoupement des objectifs avec les
rectos, choix et corrigés du catalogue N2+N3 : **18 cartes existantes passent du paquet N3 au paquet N2**,
avec `levels: [N2, N3]`, **13 cartes distinctes sont ajoutées**, sans duplication des connaissances déjà interrogées.
Bilan : **461 notes uniques**, **339 cartes dans N2**, **122 compléments dans N3** ; le programme tagué
N3 comprend **357 cartes**, dont **235 communes**. Aucun ID publié, modèle Anki ou GUID n’est modifié.

Il s’agit d’un audit des objectifs pédagogiques de ces supports, pas d’une validation de toutes leurs affirmations.
Les indications anciennes, simplifications inexactes et procédures hors périmètre sont distinguées ci-dessous.
Les compétences gestuelles, les identifications locales et les procédures spécialisées ne deviennent pas une
collection de QCM sur chaque phrase. Les schémas de modèles et tableaux ont été contrôlés visuellement.

## Sources privées identifiées

| Référence | Document | Version constatée | Pages | SHA-256 |
| --- | --- | --- | ---: | --- |
| N2-S04 | `Downloads/N2 - theorie PDF.pdf`, Patrice Serresseque ; copie privée `sources/n2-complements-2026-10-11/theorie-n2.pdf` | Couverture 01/07/2026 ; création/modification PDF 06/07/2026, distinctes de la date du cours | 36 | `571284696453136b91cc4287e6803e1bd29299211b113c8e0fad056023dac8d6` |
| N2-S05 | `Downloads/Tables MN90.pdf`, Tables MN90-FFESSM, Éditions GAP / Alain Foret ; copie privée `sources/n2-complements-2026-10-11/tables-mn90.pdf` | Novembre 2013, relevé au pied de la dernière page ; téléchargement du 11/10/2026 | 8 | `16c306fd97051185a7e2b4b865beed3b9acdf047dd77255370eec10e311294a2` |

Les deux PDF restent ignorés par Git et exclus du paquet. Les références de validation, versions et dates sont
dans `review.sources`. Le cours daté de 2026 reprend pourtant des âges et conseils plus anciens : sa date ne
prouve pas que son contenu ait été actualisé.

## Couverture du cours, page par page

« Interrogé » signifie qu’un recto appelle la connaissance ; une mention au corrigé seule ne suffit pas.
Les liens de chapitre désignent les YAML où les objectifs précis sont déjà interrogés. Les nouveaux IDs
et reprises détaillés plus bas complètent ces chapitres. Les valeurs d’exemples ne constituent pas autant
de nouveaux objectifs lorsque la même opération est déjà travaillée à plusieurs profondeurs.

| Page | Objectifs examinés | Couverture / décision |
| ---: | --- | --- |
| 1 | Titre, auteur, date | Métadonnées ; aucun objectif de carte. |
| 2 | Sommaire et intérêt de la théorie | Index de l’audit ; pas de carte sur le sommaire. |
| 3 | PA20/PE40, DP, accès, autonomie, expérience N1 | Interrogé dans `01-prerogatives.yaml` ; âges du cours écartés, règles 2026 déjà correctes. |
| 4 | Cadre réglementaire, fédération, palanquée, octopus/parachute | `02-organisation.yaml` et `03-documents-environnement.yaml` ; rôle fédéral distinct de l’État et de la CMAS. |
| 5 | DP, paramètres, aptitudes, responsabilité, cohésion | `01-prerogatives.yaml`, `02-organisation.yaml`, `17-competences-transversales.yaml` ; reconnaissance d’aptitude ne vaut pas brevet supérieur automatique. |
| 6 | Gilet, secours respiratoire, suivi personnel, parachute par palanquée | Quatre obligations interrogées individuellement dans `02-organisation.yaml`, sans doublon. |
| 7 | Licence, RC, brevet, CACI, carnet | `01-prerogatives.yaml` et `03-documents-environnement.yaml` ; licence fédérale ne vaut pas obligation universelle de toute plongée. |
| 8 | Archimède, lestage, bloc, combinaison | `05-flottabilite.yaml` et `15-gonflage-blocs.yaml` ; distinguer capacité interne et volume extérieur déplacé. |
| 9 | Pression, force/surface, atmosphérique/hydrostatique/absolue, Boyle | `04-pression.yaml`, `06-gaz-autonomie.yaml` ; séries de calculs directs/inverses déjà présentes. |
| 10 | Henry, durée/profondeur, Dalton, pressions partielles | `11-add.yaml`, `10-narcose.yaml` ; sursaturation ne signifie pas automatiquement palier obligatoire. |
| 11 | Consommation et autonomie selon profondeur | `06-gaz-autonomie.yaml` : débits, stocks, seuils, réserves, retour, phases et remontée ; pas de duplication du tableau qui dépense tout le bloc. |
| 12 | Réfraction, distance/taille apparentes, couleurs | Trois nouveaux QCM `n2-vision-*` : effet optique, calcul inverse, absorption/lampe. |
| 13 | Familles de barotraumatismes, froid, prévention noyade | `07-barotraumatismes.yaml`, `09-froid.yaml` ; ajout `n2-noyade-flottabilite-surface-001`. |
| 14 | Oreilles, équilibrage, rhume, vertige alternobarique | `07-barotraumatismes.yaml` et `06-gaz-autonomie.yaml` ; manœuvres et explication des pressions vérifiées, pas de règle médicamenteuse du cours reprise. |
| 15 | Surpression pulmonaire, ventilation, signes, alerte/O2 | `07-barotraumatismes.yaml` : mécanisme, faible profondeur, signes, urgence et amélioration sous O2. |
| 16 | Essoufflement/CO2, facteurs, effort, assistance | `08-essoufflement.yaml` ; aucun débit universel d’essoufflement ni modèle de respiration forcée imposé. |
| 17 | ADD, signes, facteurs, conduite en surface | `11-add.yaml` : formes, délais, urgence/O2, eau sous conditions, équipiers, avis médical. |
| 18 | Prévention ADD, nitrox, avion/altitude, courbe sans palier | `11-add.yaml`, `12-tables.yaml` et gaz/Dalton ; chiffres de délais et ordre de saturation du cours écartés. La formation nitrox reste une qualification distincte. |
| 19 | Narcose : pression, symptômes, variabilité, conduite | `10-narcose.yaml` ; pas de seuil clinique universel ni de lien artificiel avec une prérogative légale. |
| 20 | Azote dissous, désaturation, remontée, paliers | `11-add.yaml`, `12-tables.yaml`, `13-ordinateurs.yaml` ; ne pas enseigner le gaz dissous comme de petites bulles. |
| 21 | Profil carré, lecture palier/DTR/GPS | `12-tables.yaml` : profil carré, durée, arrondis, DTR et exemples ; 30 m/25 min contrôlé. L’histoire de Haldane n’est pas un objectif supplémentaire. |
| 22 | Successive, GPS, résiduel, majoration, temps fictif | `12-tables.yaml` : exemple complet et arrondi de l’intervalle ; exemple H/4 h/.89/20 m relu visuellement. Trois nouveaux cas complètent les deux immersions. |
| 23 | Affichages et critères d’un ordinateur | `13-ordinateurs.yaml` : profil, affichages, alarme et limites personnelles. |
| 24 | Modèles dissous/bulles, Bühlmann/RGBM | Reprises compartiment, Bühlmann et RGBM ; pas de classement générique « RGBM toujours plus conservateur ». |
| 25 | Réglages avant immersion, plan résiduel, suivi après plongée | `13-ordinateurs.yaml` + reprise planificateur ; air/GF et absence de paliers profonds déjà interrogés. |
| 26 | Compartiments, M-values, principe GF | Reprises compartiment/M-value/calcul GF ; `n2-ordinateurs-gf-principe-001` existe déjà. Organes réels et tissus fictifs restent distincts. |
| 27 | GF bas/haut, réglages, comparaison de modèles | Reprises GF bas/haut et cohabitation ; repère fédéral air 85–90 égal déjà présent. Le « 80/80 renforce forcément la sécurité » n’est pas repris. |
| 28 | Panne ordinateur, suivi personnel, limites des calculs | Reprise secours personnel ; `13-ordinateurs.yaml` interroge déjà le partage et les modèles. Les recettes +5 min/vider le bloc sont rejetées. |
| 29 | Co-gestion, plan, consignes, cohésion, successive, adaptation | `17-competences-transversales.yaml`, organisation, ADD et remontées anormales ; reprise comparaison résiduel tables/ordinateur. |
| 30 | Orientation, gaz/temps de retour, perte de repères, signalisation | Trois reprises d’orientation, ajout première limite gaz/temps ; cap inverse et alignements déjà interrogés. Valeurs de demi-tour du cours non transposées à toute plongée. |
| 31 | Impact du palmage/lumière, contacts, espèces protégées, dangers | Cinq reprises milieu (dont anémone), ajout grande nacre et rascasse ; prélèvement/accès aux sites déjà interrogés. Noms d’espèces et dangers locaux complètent aussi la formation sur site, sans prétendre couvrir toutes les espèces. |
| 32 | Blocs, TIV/requalification, compresseur, tampons, filtration | `15-gonflage-blocs.yaml` : échéances, pression, contrôles, corrosion, contaminations, tampons ; ajout compression/traitement. |
| 33 | Piston/membrane et compensation des détendeurs | `16-detendeurs.yaml` : compensation/asservissement ; ajout isolation par membrane. |
| 34 | HP/MP/ambiante, flexibles, entretien | `16-detendeurs.yaml`, `18-lecture-pannes.yaml` : fonctions, calculs, contrôle et notice fabricant ; échéance universelle du cours écartée. |
| 35 | Quiz reprenant brevet/licence/CACI, pressions, Henry, espèces | Aucun nouvel objectif de calcul/document. La portée exacte de la protection de la grande nacre est désormais interrogée ; les quatre espèces citées n’ont pas un même régime juridique. |
| 36 | Remerciements | Aucun objectif de carte. |

## Couverture des tables, page par page

| Page | Objectifs examinés | Couverture / décision |
| ---: | --- | --- |
| 1 | Historique, domaine air/effort/mer, deux plongées, profondeur max, définitions | Domaine/limites interrogés dans `12-tables.yaml`. Lignes de secours 62/65 m ne créent pas de prérogative N2 ni de profil normal à apprendre. |
| 2 | Durée/profondeur/arrondis, vitesses, simple/successive, GPS/résiduel/majoration, changement de profondeur | Cartes de lecture et successives existantes ; ajout des deux branches profondeur moindre/supérieure en conservant la majoration. À exactement 12 h, conserver « isolée », source FFESSM 2005. |
| 3 | Consécutive, remontée lente/rapide, interruption ; O2 aux paliers, altitude | Ajout exercice consécutif ; remontée lente déjà interrogée. Procédures MN90 historiques distinguées des cartes actuelles ordinateur. O2 et altitude : hors extension N2 (MFT p.12), pas de procédure extrapolée. |
| 4 | Lignes 6–32 m | Lecture directe/arrondis/courbe/DTR déjà interrogés. Pas une carte par ligne. |
| 5 | Lignes 32–65 m, GPS astérisque | Ajout sens de l’astérisque ; aucune carte de plongée normale au-delà du domaine N2. |
| 6 | Tableaux I et II | Arrondi inférieur d’intervalle/supérieur de résiduel, majoration et application déjà interrogés ; valeurs H/.98/.99, H/4 h/.89/20 m contrôlées. |
| 7 | Tableau III O2 en surface, IV durée de trajet | Tableau IV/calcul de remontée : cartes DTR existantes. Tableau III : procédure spécialisée exclue de l’extension N2, distincte de l’oxygène de secours. |
| 8 | O2 entre plongées, nitrox équivalent, convention DTR, publication | Nitrox/O2 tables : hors périmètre de cette extension ; calcul de DTR réel, transitions et arrondi final déjà interrogés. Édition novembre 2013 constatée. |

## Contradictions et passages non repris

Les références primaires ci-dessous ont été consultées le 11/10/2026. Les références médicales/fabricant
déjà portées par les cartes sont conservées ; l’ajout d’une source pédagogique ne les remplace pas.

| Passage | Problème | Décision |
| --- | --- | --- |
| Cours p.3 | Accès N2 16 ans/autonomie majeure | MFT N2 mai 2026 : certification dès 15 ans et autonomie dès 16 ans avec les autres conditions ; conserver les cartes publiées correctes. |
| p.4–7 | Fédération assimilée à l’État, licence dite universellement obligatoire | Garder les champs établissement/fédéral et les obligations exactes ; ne pas remplacer le cadre légal par une formulation du cours. |
| p.8 | 12 L/15 L utilisés comme volumes déplacés par un bloc | Capacité interne et volume extérieur ne sont pas identiques ; cartes de flottabilité actuelles conservent cette distinction. |
| p.10/18/20 | Sursaturation impliquant systématiquement paliers ; graisse assimilée à tissu rapide ; gaz dissous assimilé à bulles | Henry à l’équilibre, vitesse des échanges et modèle à compartiments séparés ; validation avec références de désaturation existantes et Shearwater/Pollock. |
| p.11/30 | Autonomie tout stock ; demi-tour moitié du stock comme règle générale ; arrondi 22,5 vers 23 ; temps de trajet oublié | Modèles avec gaz alloué, retour et réserves explicités ; premier seuil réellement atteint déclenche le retour. Aucun de ces exemples n’est enseigné comme procédure générale. |
| p.13/16 | Refroidissement « 23 fois » et débit d’essoufflement présenté comme constant | Effets et variabilité enseignés ; pas de facteur physiologique universel. |
| p.14/15 | Description des pressions sur le tympan, formulation médicamenteuse, ventilation en remontée trop générale | Conserver les mécanismes déjà vérifiés avec DAN/MFT ; aucune recommandation de médicament ni blocage respiratoire. |
| p.18/19 | 12 h signifierait élimination totale, 24 h avion/altitude universels ; narcose définie par un seuil universel | Conserver intervalle MN90 comme catégorie de modèle, délais DAN conditionnels, symptômes/variabilité. |
| p.24 | Bühlmann « prend la température », tous RGBM auraient paliers plus profonds/longs | Séparer modèle et adaptations du fabricant ; la température mesurée n’implique pas qu’elle soit un paramètre du Bühlmann de base. Contexte de chaque appareil dans les cartes existantes. |
| p.25 | Palier profond présenté comme ajout ordinaire à l’air | MFT N2 p.12/16 : GF jumeaux 85–90 ; recommandations fédérales air et carte sur les paliers profonds conservées. |
| p.26/27 | GF comme fraction de M depuis zéro ; tissus = organes ; 80/80 forcément plus sûr | Limite = Pamb + GF × (M − Pamb) ; calcul vérifié. Aucun indicateur de probabilité personnelle d’accident déduit des GF. |
| p.28 | Panne ordinateur : +5 min ou vider le bloc à 5 m | Recettes non validées rejetées ; secours personnel ayant suivi la série et procédure préparée, sans inventer une durée de décompression. |
| p.31/35 | Mérou/corb/nacre/posidonie rassemblés sous un régime unique | Grande nacre : arrêté national 08/07/2025, art.1/3. Mérou et corb : régimes de pêche/moratoires à vérifier selon zone et espèces, pas une même protection de tous les gestes. Posidonie : habitat/plante et impact du mouillage déjà interrogés. |
| p.34 | Entretien 18 mois/150 plongées universel | Notice fabricant et configuration air/Nitrox restent déterminants ; périodicités SCUBAPRO déjà contextualisées. |
| Tables p.2 | « Plus de 12 h » pour plongée isolée | Source primaire FFESSM juillet 2005 p.2 : minimum 12 h ; conserver la carte qui interroge exactement la frontière. |
| Tables p.3 | Procédures anciennes tables susceptibles d’être lues comme règles ordinateur | Garder les contextes distincts ; ne pas remplacer les rattrapages actuels FFESSM ordinateur par ceux de la MN90. |
| Fiche complémentaire DORIS rascasse | Présentation des épines pectorales comme venimeuses et toutes les épines comme creuses ; chaleur à 50 °C | Dr Claude Maillaud, Subaqua 25/02/2019, révision 18/09/2024 : épines pectorales non venimeuses, gouttières/tissu glandulaire. La carte conserve uniquement le mécanisme établi épine/venin ; aucune procédure de soins extraite de la fiche. |

Références de contrôle principales :

- [MFT N2 mai 2026](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/d7c761c8-79ed-42f2-a675-90e4c6095a56), p.3, 10–12, 16, 19–20.
- [Tables et mode d’emploi FFESSM juillet 2005](https://ffessm-ctr-aura.fr/wp-content/uploads/2019/03/MN90.pdf), p.1–3, tableaux p.4–7.
- [Shearwater/Pollock, Flexible Control of Decompression Stress](https://shearwater.com/blogs/community/flexible-control-of-decompression-stress) et manuel Peregrine référencé sur les reprises.
- [OpenStax, Images formed by refraction §2.3](https://openstax.org/books/university-physics-volume-3/pages/2-3-images-formed-by-refraction), approximation d’interface plane.
- [DAN, A Clear Picture](https://dan.org/alert-diver/article/a-clear-picture/) ; [Lessons in Gas Management](https://dan.org/alert-diver/article/lessons-in-gas-management/).
- [NOAA, couleur des animaux profonds](https://oceanexplorer.noaa.gov/ocean-fact/red-color/).
- [SCUBAPRO, notice 2020 §5.1](https://scubapro.johnsonoutdoors.com/sites/default/files/2022-08/scp_productmanual_regulator_vL2020-07_en.pdf) ; la distinction mécanique stable n’actualise pas les échéances d’entretien, sourcées séparément dans la notice 2025.
- [BAUER, I-Series et systèmes P100](https://www.bauer-kompressoren.de/en_en/i-baureihe) ; anciennes URL PDF redirigées, référence courante conservée.
- [Arrêté 08/07/2025, copie DREAL officielle](https://www.normandie.developpement-durable.gouv.fr/IMG/pdf/am8juillet2025-invertebresfaunemarine.pdf), art.1–3, entrée en vigueur 01/10/2025 ; [art.1 Légifrance](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000051862651).
- [DORIS grande nacre, 25/06/2026](https://doris.ffessm.fr/Especes/Pinna-nobilis-Grande-nacre-311) ; [Dr Maillaud, appareils venimeux](https://subaqua.ffessm.fr/article/envenimations-par-poissons-osseux-des-mers-tropicales-et-temperees).

## Relecture séquentielle des transferts

Chaque carte ci-dessous a été lue avec **tous ses choix et son corrigé**. Verdict : retenue pour N2,
objectif distinct, QCM à clé unique ; le contenu était déjà validé et est conservé à l’identique.
Les faux choix sont examinés dans la dernière colonne : ils représentent une confusion du cours,
réfutée par la connaissance interrogée. La revue antérieure conserve leur contrôle factuel détaillé.

| Lot | ID permanent | Apport N2 / contrôle des leurres |
| --- | --- | --- |
| T1 | `n3-modeles-compartiment-001` | Tissu fictif et paramètres : un organe ou une tranche de profondeur ne représente pas ce compartiment. |
| T1 | `n3-modeles-m-value-001` | Limite propre au compartiment : pression d’équilibre et plafond ambiant sont d’autres grandeurs. |
| T1 | `n3-modeles-gf-calcul-001` | Calcul du gradient : 2,04 multiplie M depuis zéro ; 0,68 omet Pamb ; recomposition 1,6 + .85×.8 = 2,28. |
| T1 | `n3-modeles-gf-bas-haut-001` | Peregrine : inverser premier arrêt/surface ou affecter les deux au premier arrêt contredit la notice. |
| T1 | `n3-modeles-buhlmann-zhl-gf-001` | Paramètres du modèle vs ajustement de limite : les GF ne changent pas les périodes, ni ZHL ne devient un réglage GF. |
| T1 | `n3-modeles-rgbm-001` | Gaz libre en plus du dissous : suivi O2 et simple ajustement du gradient ne décrivent pas cette modélisation. |
| T1 | `n3-modeles-successives-001` | MN90 GPS/majoration vs calcul continu : l’ordinateur ne repart pas de zéro et n’applique pas une majoration tabulaire commune. |
| T2 | `n3-ordinateur-gf-cohabitation-001` | Comparaison des obligations, pas classement par un seul GF ; les charges et profils peuvent différer. |
| T2 | `n3-ordinateur-planificateur-residuel-001` | Peregrine plan : intervalle saisi et charge actuelle ; ni charge figée à la sortie ni remise à zéro. |
| T2 | `n3-ordinateur-panne-briefing-001` | Secours porté sur les deux immersions : même réglage au bateau ou appareil sans plongée du matin ne reconstitue pas l’historique. |
| T2 | `n3-orientation-reperes-compas-001` | Recoupement des repères et cap 270° ; 090° garde le sens aller et 000° n’est pas le réciproque. |
| T2 | `n3-orientation-perte-limite-gaz-001` | Recherche limitée au gaz disponible hors repli : 150/60=2,5 ; 3,75 confond absolue/relative, 9,17 dépense le repli. |
| T2 | `n3-orientation-trafic-surface-001` | Parachute localise la palanquée dérivée ; Alpha au mouillage signale le bateau, pas sa nouvelle position. |
| T3 | `n3-milieu-sediments-001` | Assiette/hauteur/direction : palmes basses ou battements rapides au ras du fond soulèvent le sédiment. |
| T3 | `n3-milieu-eclairage-001` | Intensité et durée adaptées ; forte lumière pour « habituer » n’est pas une méthode respectueuse. |
| T3 | `n3-milieu-posidonie-nature-001` | Plante à fleurs ; algues vertes/brunes sont des confusions de classification, pas une propriété déduite de la couleur. |
| T3 | `n3-milieu-posidonie-mouillage-001` | Rhizomes/croissance lente : renouvellement des feuilles ou dispersion des fragments ne restaure pas vite l’herbier. |
| T3 | `n3-milieu-anemone-contact-001` | Cnidocytes : bactéries immédiates et épines calcaires sont deux autres mécanismes ; apporte le danger des cnidaires cité via les méduses. |

T1 : sept cartes ; T2 : six ; T3 : cinq. Les 122 autres compléments restent en N3 : les exercices approfondis
sur périodes/compartiment limitant, l’espace 40–60 m, le secours avancé et les réglementations N3 ne sont
pas transférés au seul motif qu’un mot existe dans un support N2. L’arrêt/tour d’horizon à 3 m, qui n’est pas
spécifié par ce nouveau cours, n’est pas déplacé sur cette seule base. Les objectifs supplémentaires du
MFT N2 sur les espèces courantes ne sont pas présentés comme entièrement couverts par ces deux PDF.

## Rédaction puis critique distincte des ajouts

Tous les ajouts sont des QCM. Ils ont été rédigés en `draft`, puis relus indépendamment avant `reviewed`.
Critères : apport distinct, recto explicite, choix plausibles/comparables, réponse unique, corrigé exact.
Deux choix manifestement plus faibles (second étage dans un recto premier étage ; apnée en surface)
ont été retirés ; trois choix ne sont pas obligatoires. Les corrigés ont été adaptés après ce retrait.

| Lot | ID | Apport distinct et justification des faux choix / relecture |
| --- | --- | --- |
| C1 | `n2-vision-masque-refraction-001` | Inversions taille/distance ; hypothèses proximité, axe et vitre plane explicites. Le masque/lame d’air est expliqué sans seconde carte de définition. |
| C1 | `n2-vision-distance-reelle-001` | 2,25 applique le facteur dans le mauvais sens ; 3,75 ajoute 25 % au lieu d’inverser une baisse de 25 %. Calcul inverse 4 m refait séparément. |
| C1 | `n2-vision-couleur-eclairage-001` | Inversion rouge/bleu et absorption identique ; la lampe proche apporte la composante rouge. Aucune profondeur d’absorption universelle. |
| C1 | `n2-noyade-flottabilite-surface-001` | Flottabilité neutre valable au palier mais insuffisante pour attendre sans palmage ; maintien de la respiration normale, gilet fonctionnel et attente en surface explicites. |
| C1 | `n2-detendeurs-membrane-isolation-001` | Isolation interne vs totalité du premier étage : chambre extérieure peut rester humide ; choix sur second étage retiré car éliminable par la question. |
| C1 | `n2-gonflage-blocs-filtration-001` | Séparation des seuls condensats et simple refroidissement ne représentent pas le traitement complet eau/huile/contaminants ciblés ; aucun filtre dit universel. |
| C2 | `n2-tables-consecutive-calcul-001` | 45 min ajoute les 8 min de surface avant arrondi ; 18 m ignore la seconde profondeur max. Calcul 25+10=35 et max(18,20)=20 refait. |
| C2 | `n2-tables-successive-moins-profond-001` | 18 m abaisse la profondeur tout en gardant la majoration initiale ; 25 min omet la majoration. Conservation explicitement choisie, donc pas une alternative de recalcul également vraie. |
| C2 | `n2-tables-successive-plus-profond-001` | 20 m garde la profondeur prévue malgré le dépassement ; 25 min omet la majoration. Profondeur 23→25 et fictive 25+10=35 contrôlées séparément. |
| C2 | `n2-tables-gps-asterisque-001` | P et calcul tableau I semblent permettre une successive, alors que * ne désigne aucun groupe ; le sens est contrôlé sur la légende de la table, sans inventer une ligne K*. |
| C2 | `n2-planification-premiere-limite-001` | Attendre le temps ou le gaz des deux équipiers dépasse le premier seuil ; 118<120 à t14, la réserve n’est pas enseignée comme une valeur universelle. |
| C2 | `n2-milieu-grande-nacre-protection-001` | Confusion vivant seul / aire protégée seule ; préciser milieu naturel et Méditerranée française exclut les collections/élevages licites et les problèmes de champ territorial. Art.1/3 vérifiés. |
| C3 | `n2-milieu-rascasse-envenimation-001` | Cnidocytes = confusion avec anémone/méduse ; dents = autre appareil d’inoculation. La piqûre par épine est distincte du contact urticant ; divergence anatomique documentée plus haut. |

## Identité, build et installation existante

Les cartes reprises sont déplacées dans les fichiers N2 mais gardent leur ID historique `n3-*`, leur thème,
leur modèle et leur contenu. Ajouter N2 dans `levels` change la destination générée, pas leur GUID.
Les anciens tags de chapitre restent des repères historiques ; les tags `level::N2` et `level::N3` sont générés.

Le recoupement ne modifie ni le code de `make push`, ni les options de révision, ni le préréglage quotidien.
**Le déplacement est livré dans le nouveau `.apkg`**. Pour une collection ayant déjà importé ces 18 cartes,
un import seul ne garantit pas leur déplacement : une migration ciblée via le code du dépôt/AnkiConnect
reste nécessaire au moment du déploiement. Ne pas réintroduire le déplacement de toutes les cartes
après chaque push, qui avait perturbé les révisions quotidiennes. Aucun import ni changement de collection
locale n’est effectué pendant ce recoupement. La conservation de l’historique local n’est donc pas testée ici.

Vérification technique finale : `make check` réussi (461 cartes valides ; 20 tests réussis, un module
optionnel ignoré ; lint, format, types et schéma conformes). Build unique de 461 notes sans draft.
Comparaison indépendante avec le catalogue au commit préalable : les 448 GUID/modèles et contenus
publiés sont conservés ; seules les 18 destinations prévues changent. Les 13 ajouts ont des identités
nouvelles, sans doublon. Paquets classiques et préréglage du dépôt contrôlés dans le SQLite du package.
Les 31 rectos/versos concernés ont été inspectés en HTML à 390 et 1000 px (124 rendus), sans erreur
JavaScript ni débordement, avec une seule clé visible au verso et aucune au recto. Les captures des
exercices MN90, du calcul de vision, de la membrane et de la grande nacre ont également été relues.
Il s’agit de previews du build, sans ouvrir ni manipuler l’interface Anki.
