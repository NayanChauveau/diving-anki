# Clôture du plan N3 — 6 octobre 2026

> Complété par le [recoupement direct des PDF du 7 octobre](RECOUPEMENT_PDF_2026-10-07.md).
> La réalisation du plan initial ne garantit pas une couverture exhaustive des PDF :
> ce nouvel audit identifie des compléments de secours, environnement et quelques
> objectifs du MFT encore absents ou partiels.

> Implémentation du 7 octobre : [22 compléments relus](COMPLEMENTS_PDF_2026-10-07.md),
> 448 cartes au total, dont 140 compléments N3. Le bilan ci-dessous décrit le lot initial.

Le paquet du 6 octobre contenait **426 notes uniques** : 308 N2 et **322 N3**, dont
**204 communes N2/N3 et 118 nouvelles**. Les 118 nouvelles cartes sont des QCM à
réponse unique. Le format a été choisi pour chaque tâche, sans quota : calculs,
comparaison de contraintes, lecture d’instruments et cas de secours s’y prêtent.
Aucune note commune n’est copiée, renommée ni convertie de modèle.

## Traçabilité et relecture

- [OBJECTIFS_N3.csv](OBJECTIFS_N3.csv) : les **147 lignes du catalogue détaillé** ont
  une issue — 117 créations, 17 reprises, 12 fusions et une exclusion. L’estimation
  initiale de 140 propositions ne comptait pas exactement les lignes du catalogue.
  Une carte supplémentaire distingue inconscience avec respiration normale et arrêt.
- [REVUE_CARTES_N3.csv](REVUE_CARTES_N3.csv) : question finale, alternatives et références
  des 118 nouvelles cartes, après une passe distincte de la rédaction.
- [CALCULS_N3.csv](CALCULS_N3.csv) : 35 résultats recalculés par fractions exactes et
  intégration par phases. Contrôles complémentaires : caps réciproques 180°/270°,
  somme des déplacements nord/est, fenêtre de courant et limites de DTR.
- [REUTILISATION_N2_N3.csv](../REUTILISATION_N2_N3.csv) : décision finale pour les 308
  candidates N2 ; le classement initial R/A/V/P/H est conservé comme historique.
- [SOURCES_N3.json](../SOURCES_N3.json) : 18 PDF téléchargés, versions, pages et empreintes.
  Les documents bruts restent privés dans `sources/n3/`.

Les 164 reprises initiales ont été conservées. Les sept adaptations de contexte et huit
revalidations ont été réalisées, puis 25 renforts ciblés retenus : GF, alarme, signalisation,
organisation, lecture des tables, salinité, verrouillage et pressions du détendeur.
Les 84 autres renforts P restent disponibles dans N2 ; leurs rappels élémentaires ou
exercices supplémentaires ne sont pas nécessaires à la couverture distincte retenue.
Les 20 H portent sur le cursus N2. Il n’y a aucun héritage automatique entre niveaux.

La relecture a examiné chaque stem, chaque choix et le corrigé : même tâche dans tous
les choix, hypothèses explicites, une réponse exacte et absence d’indice éditorial.
Les distracteurs reprennent des confusions concrètes (absolue/relative, litres/bar,
pression/profondeur, stock utilisable/stock total, palier/plafond, certification/exercice,
urgence/détresse). Les valeurs mathématiques des mauvais choix ont aussi été comparées.
L’effectif réglementaire demande la **plage complète**, pour ne pas déclarer fausse une
configuration valide incluse dans une plage plus large.

Corrections issues de cette passe : formulation du bloc limitant ; mode précis du
planificateur Peregrine ; faux choix de surface, radio et milieu ; référence A322-86 ;
exclusion digestive dans la carte commune d’hydratation ; définition du SCMM ; contexte
avec DP dans deux cartes communes. Les questions restent directes et les références
restent hors des rectos, sauf le modèle ou le cadre qui détermine effectivement la réponse.

## Doublons et approfondissements

Le brouillon « GF = pourcentage de risque » a été retiré **avant toute publication** :
`n2-ordinateurs-gf-principe-001` teste déjà cette distinction. Les effectifs, équipements,
bi-blocs, bloc allégé, parachute, narcose, gaz pollué et transmission des paramètres sont
réutilisés à leur ID existant. Aucun retrait de note publiée n’est nécessaire.

Les exercices de gaz ajoutent des opérations distinctes : débit en bar/min, problème
inverse, volumes différents, attente profonde, retour partagé, somme de phases, pression
finale imposée, sensibilité au débit et temps de fond restant. Les demi-périodes, M-values
et GF reçoivent définitions et applications distinctes ; les profils et coefficients
mathématiques imposés sont fictifs. Aucun chiffre d’exercice n’est une réserve universelle.

Le fichier de tables demeure dans N2 avec les appartenances communes ; créer un fichier
N3 vide ou recopier ces cartes n’apporterait rien. Les cartes partagées restent dans les catégories de N2 ; N3 contient ses compléments,
sans Collection commune et sans paquet filtré.

## Vérifications G01–G11

| Porte | Issue et références décisives |
| --- | --- |
| G01 | Clos pour le contenu retenu. MFT N3 décembre 2025 p.3–4,12 ; Code du sport A322-73 (modification 17/10/2025), A322-86, A322-99 et annexe III-16b actuels : certification à 17 ans, autonomie >40 m à 18 ans, deux/trois PA60, 60 m avec DP et 40 m sans DP avec décision/accord de l’exploitant. La fiche sans DP relève aussi de l’enseignement MFT p.12 ; elle n’est pas attribuée à un paragraphe inexistant d’A322-99. Aucun régime hors établissement n’est extrapolé. |
| G02 | Clos par limitation aux faits vérifiables. Baker p.1–3, notice Peregrine p.25,32–34, MN90 et Shearwater/Pollock : compartiments calculés, limites du modèle, majoration tabulaire et suivi continu des successives. La formule elliptique MFT sur les successives n’est pas recopiée ; aucune clarification CTN externe n’est prétendue. |
| G03 | Clos. Le chapitre officiel « Recommandations CTN » mai2025 p.2 reprend les décisions de2024 : les cartes N2 sont revalidées, les anciennes procédures MN90 du cours secondaire ne sont pas utilisées pour l’ordinateur. Symptômes, faisabilité et délais restent explicites. |
| G04 | Clos. RIFAP mai2026 p.18,24–29 et PSC juillet2026 p.26–27,36–41,47 : gestes guidés par le bilan, position adaptée, aggravation et avis médical ; aucune attente sans alerte après dyspnée persistante. |
| G05 | Clos. RIFAP p.28 et [CMPN, PEC](https://medical.ffessm.fr/pec-d-un-accident-de-plongee-bouteille-ou-recycleur) : trois exclusions dont lésion digestive ; réflexes oropharyngés compromis/risque d’inhalation, notamment avec dyspnée. PSC p.41 : assise si difficulté respiratoire, sinon confort. La correction est dans la note N2/N3 existante. |
| G06 | Clos dans les cadres explicités. RIFAP p.29,32 : pas de recompression thérapeutique, avis médical pour tout incident ; observation CTN conservée avec cet avis, sans inventer une abrogation. ANFR CRR juin2025 p.20–23,30–34 : catégories graduées ; DISTRESS n’est pas l’ASN automatique de tout accident. Mer : CROSS/VHF16 ; terres :15/112. L’exemple radio du RIFAP est distingué des critères officiels ANFR. |
| G07 | Clos pour le périmètre retenu. A322-78/80, MFT p.8,12, notice SCUBAPRO RevQ juillet2025 p.2,5,7 : matériel individuel/collectif, limites fabricant distinctes du brevet. Les restrictions locales sont à consulter pour le secteur, sans distance nationale inventée ; les limites de kits particuliers ne sont pas extrapolées. |
| G08 | Clos. 35 résultats recalculés ; deux débits additionnés, profondeur variable intégrée, attente/arrêts/trajets/final séparés. Les calculs concernent des exercices à hypothèses imposées ; ils ne génèrent pas une décompression réelle. |
| G09 | Clos. Peregrine Doc.16001-SI-RevB du06/07/2020 (nom du fichier2021), p.16,25,28,33–34,38 ; Suunto Zoop Novo notice officielle. TTS, @+5, CEIL, gaz activés, mode Profondimètre et réinitialisation sont contextualisés. GF fabricant par défaut 40/85 distinct du repère fédéral air 85/85–90/90. |
| G10 | Clos pour les connaissances théoriques publiées. RIFAP2026, PSC/PSE juillet2026 ; [DAN, IPE](https://dan.org/safety-prevention/diver-safety/divers-blog/can-you-recognize-ipe/) pour mécanisme, signes et O₂/évaluation. Aucune attribution certaine d’OPI à des signes communs, aucune séquence chiffrée de réanimation inventée. Noyade : ne pas retarder la réanimation pour « vider » les poumons (PSE p.273–274). |
| G11 | Clos pour le socle choisi. MFT p.14–15, Météo-France Guide marine2022 p.28–30, DORIS fiches265/111 et OFB : contexte Méditerranée pour posidonie/anémone, protection des habitats et absence de contact. Pas de photos DORIS copiées ; la vue de déplacement est une illustration originale intégrée, sans média externe. |

Ces décisions résultent de la comparaison des versions et champs d’application ; les tests
techniques ne servent pas de preuve médicale, réglementaire ou pédagogique.

## Couverture du référentiel et limites de l’outil

| Référentiel | Couverture théorique |
| --- | --- |
| MFT p.8 — planifier | Gaz, profil, contraintes collectives et reprise ; N3-03/04 et socle N2. |
| MFT p.9 — autonomie PA40 | Orientation, cohésion, communication et désaturation ; N3-06/09/12 et cartes communes. |
| MFT p.10 — intervenir | Signes volontaires/observés, coopération, contrôle de la remontée ; N3-08/09. |
| MFT p.11 — planifier N3 | Contraintes profondeur/consommation/accidents ; N3-03/04/08 et risques N2 partagés. |
| MFT p.12 — organiser sans DP | Exploitant, météo, site, rotation, récupération, fiche, Alpha et secours ; N3-01/02/10/12 et communs. |
| MFT p.13 — autonomie N3 | Exercices gaz fond/palier en L/min et bar/min, instruments, profils communs ; N3-04/06/12. |
| MFT p.14–15 — milieu/connaissances | Prérogatives, physique, modèles, accidents, environnement ; douze modules et socle partagé. |
| RIFAP1 — communication | Signes, paramètres, faits et chronologie ; socle N2 et N3-03/09/10. |
| RIFAP2 — mise en sécurité | Flottabilité/voies aériennes, bilan après extraction ; N3-09/10. |
| RIFAP3 — récupération | Regroupement, comptage, autres palanquées, matériel ; N3-10-01 et organisation. |
| RIFAP4 — coordination | Répartition, interlocuteurs, suivi ; N3-10-01/17/19 et N2. |
| RIFAP5 — bilan/gestes | Réponse/respiration, gasps, noyade, hémorragie, trauma, perte de connaissance ; N3-08/10. |
| RIFAP6 — oxygène/surveillance | Mode d’administration, débit, stock, hydratation, positions, aggravation ; N3-10 et notes communes. |
| RIFAP7 — alerte | Canaux, catégorie radio, position, avis médical et évolution ; N3-10 et transmission N2. |

La théorie est couverte selon le périmètre décrit. Remontée assistée, manipulation des
équipements, tractage/hissage, ventilation/RCP, orientation réelle et reconnaissance visuelle
d’espèces se valident en formation pratique. N3-09-07 est écarté comme rappel de tolérance
d’examen ; les règles ordinaires de remontée sont couvertes. La compatibilité d’un kit précis
dévidoir/parachute se contrôle avec sa notice et en pratique ; le risque général de traction
reste sur la note commune. Les compétences pratiques ne sont pas certifiées par Anki.

## Vérifications techniques et publication

Les IDs et marqueurs de modèle des 308 notes N2 ont été comparés à la version publiée.
Contrôles du catalogue, tests et build unique exécutés ; inspection des champs exportés,
réponse correcte unique et illustration intégrée. Le résultat de l’import réel et de la
synchronisation est vérifié séparément avant la livraison.

Résultats de livraison : `make check` réussi (17 tests), quatre tests optionnels
avec le véritable importeur Anki réussis, `make build` : 426 notes/aucun brouillon.
Le package contient une note par GUID, les tags exacts de niveau, un corrigé vrai unique
et le SVG dans le champ Question. `make push` a importé puis synchronisé AnkiWeb :
les 308 notes existantes conservent IDs, modèles, decks, flags, échéances et historique ;
les **191 révisions sont intégralement conservées**, sans changement de planning.
Les 118 nouvelles notes ont été ajoutées une fois. Aucun pilotage de l’interface Anki
n’a été nécessaire ; l’inspection a porté sur les champs du package et la collection réelle.
