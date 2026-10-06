# Plan détaillé d’implémentation — théorie N3 FFESSM en français

Préparé le **6 octobre 2026** à partir des documents téléchargés et du catalogue N2 au commit `3cf5bfd`. Statut initial : **préparation**. Mise à jour du 6 octobre 2026 : **164 reprises N2/N3 validées et intégrées**, aucune carte spécifique N3 encore rédigée.

## Décision de périmètre

Préparer un plongeur à la **théorie N3 FFESSM à l’air**, en France : autonomie jusqu’à 40 m, adaptation à l’espace 40–60 m, organisation sans DP dans les conditions autorisées, désaturation et gestion des secours. Le cadre de référence est le MFT **décembre 2025**, complété par le RIFAP **mai 2026** et les règles communes de certification **janvier 2025**. Les pages citées sont les pages physiques des PDF, à partir de 1.

L’augmentation de profondeur seule ne justifie pas de recréer la physique ou les accidents du N2. Les ajouts doivent surtout faire travailler la **planification complète**, les **contraintes simultanées**, les **modèles de désaturation**, la **lecture des instruments** et les **décisions collectives**. Une définition simple n’est créée qu’une fois. Les gestes d’assistance, de tractage, de hissage et de secourisme relèvent aussi d’un apprentissage pratique ; les cartes portent sur leur compréhension, leur préparation et les décisions pertinentes.

Sont exclus du socle : cursus d’encadrement N4/N5, enseignement, diplôme nitrox/trimix, recycleur, plongée sous plafond, pénétration d’épave, réparation interne de matériel et résolution complète de modèles de décompression. Les ouvertures utiles ne doivent attribuer ni nouvelle qualification ni procédure opérationnelle implicite. Les règles nautiques dépendent du bateau et de la zone : pas de diplôme de navigation ajouté artificiellement au N3.

## Livrables et état de la préparation

- **12 PDF, 290 pages**, téléchargés dans `sources/n3/`, avec manifeste local, URL d’origine, nombre de pages et empreinte SHA-256.
- [Inventaire public des sources](reviews/SOURCES_N3.json) : mêmes références et empreintes, sans publier les documents eux-mêmes.
- [Tri des 308 cartes N2](reviews/REUTILISATION_N2_N3.csv) : un enregistrement par ID publié, avec recto actuel, décision initiale, motif et état de reprise N3.
- Le présent document : périmètre, couverture, catalogue détaillé, exercices, vérifications, workflow, validation et estimation.

Les PDF restent ignorés par Git. Les télécharger et extraire leurs textes n’équivaut pas à les valider intégralement. Les passages déterminants du MFT, du RIFAP et du cours 2024 ont été confrontés au périmètre ; les supports de Grenoble servent de compléments anciens, pas de références actuelles de sécurité. Les pages en tableaux doivent être contrôlées visuellement avant rédaction, en particulier les fiches et affichages. Les tableaux du MFT p.15 et du RIFAP p.28 ont déjà été inspectés visuellement pendant cette préparation.

## Sources effectivement disponibles

| Référence | Fichier / téléchargement | Édition observée | Pages | Utilisation |
|---|---|---|---:|---|
| N3-S01 | [ffessm-mft-n3-decembre-2025.pdf](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/fcc5f7d1-a03f-483a-9acc-008db991e5ac) | Décembre 2025 | 17 | Référentiel principal FFESSM pour le périmètre et la couverture |
| N3-S02 | [eragnole-cours-n3-2024.pdf](https://eragnole.com/WordPress3/wp-content/uploads/2016/10/2024-Niveau-3-Cours-Theoriques.pdf) | 2024 | 45 | Cours continu secondaire ; explications et idées d’exercices à contrôler |
| N3-S03 | [fsgt-pa60-n3-juillet-2025.pdf](https://plongee-fsgt.org/wp-content/uploads/2025/10/MdM-PA60-P3-2025-07.pdf) | Juillet 2025 | 3 | Comparaison FSGT seulement ; aucun transfert automatique de conditions FFESSM |
| N3-S04 | [ffessm-rifap-mai-2026.pdf](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/f65d4fd1-beec-4dff-a803-b36101f71f88) | Mai 2026 | 38 | Référentiel principal du volet secours/RIFAP ; renvoie aux référentiels d’État pour les gestes |
| N3-S05 | [ffessm-regles-certification-janvier-2025.pdf](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/fb0d17fd-84a2-40ef-a59a-48ee2ab230e3) | Janvier 2025 | 4 | Complément primaire sur les conditions communes de formation/certification |
| N3-S06 | [ffessm-remontees-anormales-novembre-2024.pdf](https://ffessm.fr/uploads/media/docs/0001/12/1e862af90f137e0c9bf98859c31092e14b8a3c5e.pdf) | Novembre 2024 | 6 | Texte fédéral ciblé air + ordinateur ; confronter au RIFAP 2026 et à toute mise à jour |
| N3-S07 | [grenoble-accidents-1-n3-2017.pdf](https://drive.google.com/uc?id=18T2u83ccfzp0rjPjIEfGel5n5KttjofE&export=download) | 2017 indiqué par le nom du fichier ; datation interne non établie | 45 | Complément ancien sur les accidents ; suggestions seulement |
| N3-S08 | [grenoble-physique-n3-2016-2017.pdf](https://drive.google.com/uc?id=1-uVpjpIFI_CpSOPJBP6wLprvmgU3uxF-&export=download) | 2016–2017 indiqué par le nom du fichier ; datation interne non établie | 34 | Complément ancien de physique ; suggestions d’exercices seulement |
| N3-S09 | [grenoble-reglementation-n3-2016-2017.pdf](https://drive.google.com/uc?id=1HnM9LuVoPfdSTPthFQekCiHNVVI3oznc&export=download) | 2016–2017 indiqué par le nom du fichier ; datation interne non établie | 20 | Complément ancien de réglementation ; ne fait pas autorité sur les règles actuelles |
| N3-S10 | [grenoble-accidents-2-n3-2017.pdf](https://drive.google.com/uc?id=1zEXgx-sfsM-DBZSYhdq3r5ccGtvDuZ7N&export=download) | 2017 indiqué par le nom du fichier ; datation interne non établie | 35 | Complément ancien sur les accidents ; suggestions seulement |
| N3-S11 | [grenoble-autonomie-organisation-planification-n3-2017.pdf](https://drive.google.com/uc?id=1lNl-1dDCsgYBJd4l3-TMsmxGIZ6bvh2K&export=download) | 2017 indiqué par le nom du fichier ; datation interne non établie | 34 | Complément ancien organisation/planification ; suggestions de cas seulement |
| N3-S12 | [baker-understanding-m-values.pdf](https://cdn.shopify.com/s/files/1/0838/3732/1530/files/understanding_m-values.pdf?v=1712803291) | Document historique ; date éditoriale non établie | 9 | Publication originale de théorie des M-values ; pas un guide de conduite médicale ni de réglage actuel |

Le portail [MFT FFESSM](https://mft.ffessm.fr/) sert à rechercher les mises à jour ; le pied de page du PDF téléchargé fait foi pour l’édition utilisée. Le lien RIFAP, précédemment associé par la recherche à octobre 2021, fournit maintenant **mai 2026** : le fichier a été nommé d’après cette version réelle.

La [page de formation du Nautile Club de Grenoble](https://sites.google.com/view/ncg38/ncg38-accueil/formations/formations-plong%C3%A9e) présentait une divergence entre l’index de recherche et le HTML effectivement récupéré : huit supports N3 annoncés comme 2025–2026 dans l’index, mais cinq liens N3 2016–2017 dans la page téléchargée. **Ce sont ces cinq anciens PDF qui ont été récupérés.** Les huit fichiers récents ne sont ni téléchargés ni utilisés comme s’ils avaient été lus. Leur récupération éventuelle pourra améliorer les exemples, sans bloquer le socle MFT/RIFAP/cours continu déjà disponible.

Le document FSGT est conservé pour distinguer les cursus. Ses conditions d’accès, CAFSAN, délivrance et recommandations de mélanges ne deviennent pas des conditions FFESSM. Le texte de Baker complète la théorie ; ses illustrations historiques ne servent pas à prescrire une stratégie de paliers actuelle.

## Compléments primaires à acquérir avant rédaction des lots concernés

1. **Code du sport en vigueur** : articles A.322-71 à A.322-99 et annexes pertinentes, notamment III-14a, III-14b et III-16a ; archiver le texte/date et les articles réellement utilisés. L’accès direct à [A.322-99](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000025393795) n’a pas abouti avec l’outil web pendant cette préparation. Les modalités fines sans DP restent donc à revalider, pas réputées vérifiées juridiquement.
2. **Secourisme d’État** : obtenir les recommandations PSC/PSE applicables depuis le [Ministère de l’Intérieur](https://www.interieur.gouv.fr/Media/Securite-civile/Files/Recommandations-premiers-secours) et contrôler leur édition à l’intérieur du document. Le lien trouvé ne prouve pas à lui seul que le PDF est le plus récent. Utiliser les niveaux pertinents pour le sauveteur du scénario, sans mélanger les gestes d’un citoyen et d’un équipier PSE.
3. **CMPN FFESSM** : dernières recommandations accidents/OPI, oxygénothérapie et éventuelles précisions sur les remontées anormales. Conserver une référence datée, avec page/section. Chercher toute clarification publiée après les textes 2024/2026.
4. **Notices d’ordinateurs** : deux modèles/versions explicitement identifiés, l’un avec GF paramétrables et l’autre avec une présentation différente des plafonds/paliers. Recueillir affichages, mode planification, historique, vitesses et conduite en cas de panne ; aucune procédure ne doit être attribuée à tous les fabricants. L’[article de Shearwater sur les GF](https://shearwater.com/zh-cn/blogs/community/surface-gf-teric-musings) a permis de retrouver la publication originale de Baker ; les notices seront nécessaires pour les écrans et comportements propres aux appareils.
5. **Sources locales et milieu** : bulletin météorologique officiel, informations de marées/courants SHOM, arrêté du secteur retenu, fiches FFESSM/DORIS pour espèces/habitats. Chaque scénario fournit les données nécessaires ; pas de conditions géographiques supposées.
6. **Matériel** : notices des dispositifs retenus (oxygène, détendeur, parachute), version et limites d’utilisation. Les illustrations publiées seront originales ou assorties de droits explicites ; les PDF téléchargés ne seront pas copiés dans les packages.

## Points de vérification obligatoires

Ces points sont des tâches de validation éditoriale, pas des demandes d’autorisation à l’utilisateur. Tant qu’un point reste ouvert, les cartes qui en dépendent restent en `draft`. Les lots indépendants peuvent avancer.

| Porte | Problème observé / risque | Travail nécessaire et critère de clôture |
|---|---|---|
| G01 — Réglementation | Le MFT résume les prérogatives mais ne remplace pas le Code ; sa formulation « conditions identiques au PA40 » ne suffit pas à détailler une sortie sans DP. | Contrôler âges/certification/exercice, effectifs, aptitudes, présence du DP, autorisation de l’exploitant, information préalable et fiche de sécurité. Fixer le contexte établissement/FFESSM/exploration ; distinguer le cas hors structure sans transposer automatiquement les mêmes obligations. Références article + version dans la revue. |
| G02 — Modèles et successives | Le MFT p.15 contient une formule elliptique sur la non-modélisation des successives ; prise littéralement, elle serait trompeuse pour un ordinateur. | Expliquer séparément charge résiduelle, réduction tabulaire via majoration et calcul continu d’un ordinateur. Si le sens pédagogique précis demeure incertain, documenter une clarification CTN ou limiter la carte à des faits vérifiés ; aucun recto laissant croire que les ordinateurs ignorent les successives. |
| G03 — Remontées anormales | Le cours 2024 p.32 décrit les anciennes procédures MN90 ; le texte fédéral novembre 2024 donne un autre cadre air + ordinateur. | Réutiliser/revalider les cartes N2 concernées au lieu de copier le cours. Vérifier l’existence d’une actualisation postérieure. Distinguer rattrapage conditionnel et recompression thérapeutique interdite. |
| G04 — Secours actuels | Le cours 2024 p.40 propose une position allongée et minimise le recours à l’évacuation après essoufflement ; la gêne peut relever d’un autre accident. | Établir les actions selon conscience/respiration/signes de gravité, avec CMPN, RIFAP 2026 et référentiels d’État. Supprimer les généralisations et les diagnostics certains quand les signes sont communs. |
| G05 — Hydratation et positions | RIFAP 2026 p.28 énumère trois exclusions ; la carte N2 sur l’eau inclut d’autres conditions de sécurité, dont la gêne respiratoire. | Comparer les champs d’application et les sources existantes, noter ce qui relève d’une exclusion formelle ou de la capacité réelle à boire. Pas de reprise mécanique ni de nouvelle carte discordante. Même contrôle pour les positions. |
| G06 — Alerte / réimmersion | RIFAP 2026 p.29 interdit la recompression thérapeutique ; p.32 demande un avis médical pour tout incident/accident, tandis que le texte 2024 prévoit une branche d’observation après certains paliers manqués. La radio/ASN p.31 nécessite également un contexte précis. | Vérifier portée et chronologie des textes avec CTN/CMPN ; ne pas affirmer que la branche d’observation dispense d’un avis médical. Contrôler les critères urgence/détresse auprès des sources maritimes officielles avant PAN-PAN/ASN. Consigner explicitement les divergences non résolues. |
| G07 — Site, bateau et matériel | Les obligations changent avec la zone, le support et l’organisation ; les anciens cours donnent parfois une règle locale comme générale. | Vérifier texte national + texte local + notice selon la carte. Préciser équipement individuel/palanquée/collectif et lieu de disponibilité. Les faits déjà dans N2 ne deviennent pas plusieurs cartes de checklist. |
| G08 — Modèles de gaz | Cours 2024 p.9 : autonomie jusqu’à épuisement ; p.10 : règle des tiers et déduction de DTR qui ne démontrent pas un retour complet à deux. | Refaire les calculs avec phases, deux débits, temps d’attente, marge et pression finale fournis. Vérification indépendante, unités explicites ; aucune réserve universelle prescrite. |
| G09 — Fabricants / GF | Réglages, alarmes, plafonds et verrouillage varient. Le repère fédéral air ne devient pas une consigne universelle nitrox/trimix. | MFT p.8/13 + notice/version. Vérifier l’affichage simulé et toutes ses contraintes ; distinguer GF bas/haut, limite du modèle et risque individuel. |
| G10 — OPI, noyade, premiers secours | Le MFT nomme l’OPI ; le cours continu n’en donne pas une couverture fiable. Le RIFAP renvoie aux recommandations d’État pour les gestes. | Compléter avec CMPN et PSC/PSE actuels. Reconnaître/agir sans exiger un diagnostic certain ; ne pas publier de séquence de réanimation chiffrée sans référence précise. |
| G11 — Milieu et images | Le secteur et les espèces ne sont pas encore choisis ; identification et dangers dépendent du lieu. | Choisir un socle Méditerranée/Atlantique clairement contextualisé, vérifier identifications et droits. Limiter aux observations/comportements utiles, sans créer un second deck naturaliste. |

Autres raccourcis du cours secondaire à écarter : lest fixe lors d’un changement 12 L/15 L ou mer/eau douce (p.12–13), température corporelle donnée à 34 °C et explication de la diurèse comme réchauffement (p.41), quantité d’azote directement attribuée à la fréquence ventilatoire (p.39–42), repli sur l’ordinateur du binôme sans historique/procédure préparée (p.30). Les connaissances correctes déjà validées en N2 ont priorité sur ces raccourcis. Le relevé ne constitue pas une revue exhaustive de toutes les phrases des douze PDF.

## Réutilisation du N2 et absence de doublons

Les **308 cartes existantes** ont reçu une décision éditoriale initiale dans le CSV. La [revue des reprises](reviews/n3/00-reprises-n2.md) a ensuite retenu les **164 R**, désormais explicitement N2/N3 dans les YAML. Les 7 A et 8 V restent à traiter ; les colonnes `etat_n3` et `revue_n3` distinguent la décision initiale de son résultat. Le paquet unique conserve 308 notes, dont 164 appartenant aussi au N3 ; ce socle ne constitue pas encore une préparation N3 complète.

| Décision | Nombre | Signification |
|---|---:|---|
| R — Reprise candidate | 164 | Objectif commun relu et validé : appartenance N3 ajoutée, sans nouvelle note. |
| A — Adaptation | 7 | Recto cadré N2/PA20 ou autre contexte à généraliser avec prudence ; même objectif = préserver l’ID, sans copie. |
| V — Revalidation | 8 | Secours/remontées concernés par les divergences ; inclusion suspendue à G03–G06. |
| P — Acquis disponibles | 109 | Révision possible via N2 ; non inclus par défaut pour éviter d’alourdir N3. |
| H — Hors cible N3 | 20 | Conditions et cas propres au cursus N2/PA20/PE40 ; conserver dans N2. |

| Fichier N2 | Cartes | R | A | V | P/H |
|---|---:|---:|---:|---:|---:|
| 01-prerogatives | 20 | 0 | 0 | 0 | 20 |
| 02-organisation | 20 | 11 | 4 | 0 | 5 |
| 03-documents-environnement | 12 | 8 | 1 | 0 | 3 |
| 04-pression | 24 | 12 | 0 | 0 | 12 |
| 05-flottabilite | 25 | 9 | 0 | 0 | 16 |
| 06-gaz-autonomie | 33 | 15 | 0 | 0 | 18 |
| 07-barotraumatismes | 21 | 11 | 0 | 0 | 10 |
| 08-essoufflement | 9 | 9 | 0 | 0 | 0 |
| 09-froid | 9 | 6 | 0 | 0 | 3 |
| 10-narcose | 14 | 10 | 0 | 0 | 4 |
| 11-add | 26 | 23 | 0 | 2 | 1 |
| 12-tables | 21 | 10 | 0 | 0 | 11 |
| 13-ordinateurs | 20 | 13 | 1 | 0 | 6 |
| 14-remontees-anormales | 10 | 4 | 0 | 6 | 0 |
| 15-gonflage-blocs | 13 | 7 | 0 | 0 | 6 |
| 16-detendeurs | 20 | 8 | 0 | 0 | 12 |
| 17-competences-transversales | 8 | 7 | 1 | 0 | 0 |
| 18-lecture-pannes | 3 | 1 | 0 | 0 | 2 |

Cette première sélection est volontairement **révisable** : elle repère le socle mobilisable, sans recopier tout le N2. Pour chaque lot, lire les versos, contrôler leur actualité, éliminer les cartes dont l’intérêt repose uniquement sur un rappel déjà maîtrisé et rapprocher les cas du catalogue ci-dessous. Le N3 doit pouvoir proposer les rappels essentiels, mais sa rédaction doit porter surtout sur la différence de niveau. Une seconde série d’exercices sur une méthode complexe est justifiée par l’automatisation ou une nouvelle contrainte, pas par un simple changement de prénom.

Exemples de rapprochements obligatoires :

- GF : `n2-ordinateurs-gf-principe-001` est partagé ; `n2-ordinateurs-gf-air-ffessm-001` demande un travail de contexte. Ajouter les rôles bas/haut et un calcul illustratif, pas une seconde définition du pourcentage.
- Gaz : les cartes `n2-gaz-deux-phases-001`, `n2-gaz-deux-equipiers-001` et `n2-gaz-consommation-remontee-001` couvrent déjà les méthodes élémentaires. Le N3 ajoute leur combinaison en **retour complet**, bar/min, attente et décision de départ du fond.
- Plafonds : `n2-ordinateurs-plafond-lecture-001` et `n2-ordinateurs-plafonds-differents-001` sont déjà présentes. Un nouvel écran doit ajouter une lecture utile, pas seulement une autre profondeur.
- Orientation : les caps réciproques simples existent ; créer des parcours avec courant/obstacle/plusieurs branches uniquement si leur résolution ajoute une opération.
- Accidents : symptômes d’ADD, surpression, froid et narcose déjà couverts ; l’OPI et les décisions avec plusieurs contraintes demandent une extension ciblée.
- Matériel : entretien, requalification et fonctionnement de détendeur ne doivent pas être recopiés en entier ni élargis artificiellement au N3.

## Organisation du deck et conservation des identités

Garder des sous-decks larges, directement sous `Plongée` : **Réglementation**, **Physique**, **Prévention des accidents**, **Désaturation**, **Matériel et préparation**. Les 12 modules ci-dessous servent de fichiers/tags et d’ordre de travail, pas de 12 petits sous-decks. Un module exclusivement couvert par des cartes partagées n’a pas besoin d’un fichier N3 vide supplémentaire.

- Carte partagée : garder fichier et ID publiés, ajouter `N3` dans `levels` **après revue**. Aucun héritage global N2 → N3. Le préfixe `n2-` d’un ID reste acceptable : sa stabilité prime.
- Adaptation de contexte : vérifier la pertinence pour les deux niveaux. Si l’objectif change réellement, nouvelle carte `n3-...` ; sinon reformuler la carte commune sans changer son identité. Documenter chaque choix.
- Objectifs du présent plan : `N3-01-01`, etc., identifiants de préparation. Ils ne sont pas des IDs Anki et ne remplacent pas les IDs publiés ni le registre des retraits.
- Le générateur produit **un GUID par carte pour tous les niveaux**, compatible avec les GUIDs N2 publiés. L’ajout N3/N4 ajoute des appartenances et des tags à la même note ; son historique et ses échéances restent communs dans une même collection Anki. Un seul paquet `diving-fr.apkg` contient tous les niveaux ; les tags permettent de sélectionner N2/N3/N4 dans Anki. Voir [la collection partagée](SHARED_COLLECTION.md) pour la migration des anciens sous-decks.
- Pas de changement de modèles, de namespace ni des IDs Anki de `src/diving_anki/ids.py`. Pas de suppression de notes existantes pour faire le ménage.

## Catalogue détaillé des objectifs

Ce catalogue contient **147 objectifs**, dont **140 propositions nouvelles à instruire**, **6 reprises** et **1 adaptation**. Ce sont des objectifs de travail, **pas un quota de cartes à produire** : la revue peut fusionner, reprendre une carte existante ou écarter une proposition trop proche. Les 164 candidates communes du CSV ne sont pas autant de nouvelles cartes à rédiger.

Formats proposés : **F** fait simple (QCM par défaut), **C** cas/décision (QCM crédible par défaut), **E** exercice chiffré (QCM ou réponse libre justifiée), **V** lecture visuelle originale (QCM ou réponse libre justifiée), **R** reprise existante, **A** adaptation. Un QCM ne sera choisi que s’il existe des confusions plausibles, de même catégorie, et une réponse unique. Tout cas de sécurité doit demander une action déterminable avec les données fournies ; quand plusieurs diagnostics sont possibles, ne pas demander d’en choisir un comme certain.

Chaque objectif neuf passe par : référence précise → comparaison N2/N3 → recto/verso → vérification factuelle → revue pédagogique distincte → rendu → `reviewed`. Les références ci-dessous sont des **points d’entrée** : compléter la page/section exacte dans `review.sources`, surtout pour les exercices originaux et les compléments primaires restant à acquérir.

### N3-01 — Prérogatives, cursus et responsabilités

Sous-deck : **Réglementation**. Sources de départ : N3-S01 p.3–4, 12, 15 ; N3-S05 p.2–3 ; N3-S04 p.7. Vérifications : G01, G02.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-01-01 | F | Distinguer la profondeur d’autonomie N3 avec DP et sans DP. | Une comparaison, sans série PA60/PA40 inversée. |
| N3-01-02 | C | Décider si une exploration à 50 m est admissible sans DP pour trois N3 majeurs. | Appliquer la restriction à une situation ; fusion possible avec la définition si trop immédiat. |
| N3-01-03 | F | Distinguer obtenir le N3 à 17 ans et exercer l’autonomie au-delà de 40 m à 18 ans. | Expliquer ce que le titulaire peut effectivement faire entre les deux âges. |
| N3-01-04 | C | Déterminer les conditions de participation d’un N3 de 17 ans à une palanquée autonome à 40 m. | Autorisation, information des équipiers et décision du DP ; pas seulement réciter un âge. |
| N3-01-05 | C | Distinguer PA40, PE60 et N3 pour un candidat qui ne possède qu’une qualification isolée. | Prérogatives combinées et prérequis ; éviter l’assimilation d’une qualification au brevet. |
| N3-01-06 | F | Identifier le prérequis de certification d’entrée en formation N3 FFESSM. | N2 ou PA40/aptitudes équivalentes ; ne pas reproduire les conditions d’entrée N2. |
| N3-01-07 | F | Situer l’exigence RIFAP dans la délivrance du N3 plutôt que l’inventer pour toute entrée en formation. | Développer le sigle et séparer formation, acquisition et délivrance. |
| N3-01-08 | F | Distinguer N3/CMAS 3* et fonction de guide de palanquée en France. | Pas de prérogative française d’encadrement déduite des étoiles. |
| N3-01-09 | C | Déterminer l’effectif et les aptitudes nécessaires pour une exploration autonome à 55 m. | Palanquée entièrement compatible ; contrôle des annexes du Code, pas de chiffre issu d’un ancien diaporama. |
| N3-01-10 | C | Traiter une palanquée N3 + PA40 souhaitant descendre à 50 m. | Appliquer l’aptitude limitante en situation N3, à comparer au cas PA20/PA12 existant. |
| N3-01-11 | C | Distinguer autonomie, direction de plongée et encadrement à partir des fonctions exercées. | Cas où un N3 organise sa plongée sans devenir automatiquement DP pour les autres. |
| N3-01-12 | C | Distinguer responsabilité civile et responsabilité pénale dans un incident d’organisation. | Nature de la responsabilité ; ne pas promettre une qualification juridique automatique. |
| N3-01-13 | C | Déterminer les conditions d’une sortie sans DP organisée par un établissement. | Autorisation/information de l’exploitant et traçabilité à établir sur le Code actuel. |
| N3-01-14 | F | Distinguer exploration et formation technique dans l’espace 40–60 m. | Champ de l’encadrement E4, sans généraliser les modalités d’un exercice à la remontée ordinaire. |

### N3-02 — Organiser une sortie sans DP

Sous-deck : **Matériel et préparation**. Sources de départ : N3-S01 p.12 ; N3-S02 p.34–35 ; N3-S11 p.10–28 comme complément ancien. Vérifications : G01, G07.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-02-01 | C | Identifier ce qui manque à une organisation sans DP dont seul le profil sous-marin est prévu. | Parcours + mise à l’eau/récupération + surveillance + secours ; une décision ciblée au recto. |
| N3-02-02 | C | Choisir entre deux sites en fonction du vent prévu et de leur exposition réelle. | Données météo/topographie fournies ; pas de mémorisation de toute l’échelle de Beaufort. |
| N3-02-03 | F | Distinguer direction du vent et direction de propagation de la houle dans le choix du site. | Orientation explicitée ; rechercher une source météorologique primaire. |
| N3-02-04 | C | Réévaluer une sortie si les conditions de récupération se dégradent malgré un fond abrité. | Le retour au bateau peut devenir le facteur limitant. |
| N3-02-05 | C | Interpréter une fenêtre de marée/courant à partir d’informations locales fournies. | Pas de règle universelle sur l’heure d’étale ni sur la direction des courants. |
| N3-02-06 | C | Choisir une sortie de repli atteignable dans un scénario où le retour prévu est compromis. | Distances, courant et autonomie donnés ; pas de scénario qui demande seulement de “rester prudent”. |
| N3-02-07 | F | Déterminer les informations à communiquer à une personne restée à terre. | Site, personnes, horaires, déclenchement de l’alerte ; distinguer cette mesure du plan de secours. |
| N3-02-08 | C | Définir une rotation de palanquées permettant de conserver une surveillance de surface. | Effectif et disponibilité du pilote donnés ; pas de présence minimale inventée. |
| N3-02-09 | C | Identifier le problème d’une mise à l’eau générale laissant un bateau dériver sans récupération organisée. | Responsabilité collective et solution concrète adaptée au cas. |
| N3-02-10 | C | Renseigner les paramètres prévus puis réalisés d’une fiche de sécurité sans DP. | Contexte différent de la carte où le DP tient la fiche ; adapter plutôt que doubler sa définition. |
| N3-02-11 | C | Choisir un moyen de communication adapté à un site où le téléphone ne couvre pas la zone. | VHF/portée/contact ; réutiliser le fait réglementaire N2 déjà couvert. |
| N3-02-12 | C | Vérifier la capacité réelle d’oxygène au regard d’un délai de secours annoncé. | Renvoi aux exercices N3-10 ; aucun délai de secours présenté comme garanti. |
| N3-02-13 | C | Distinguer armement du bateau, matériel de secours de plongée et équipement individuel. | Cas d’une vérification incomplète ; obligations nautiques à sourcer selon bateau/zone. |
| N3-02-14 | C | Rechercher les règles locales de mouillage et d’accès avant une sortie sur zone protégée. | Cas concret avec avis/arrêté fourni ; la définition générale est déjà en N2. |

### N3-03 — Planifier le profil et les décisions collectives

Sous-deck : **Matériel et préparation**. Sources de départ : N3-S01 p.8–9, 11–13 ; N3-S02 p.10, 30, 34–35. Vérifications : G01, G08.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-03-01 | C | Hiérarchiser les limites d’une plongée : aptitude, consigne DP, gaz, désaturation, milieu. | Déterminer la contrainte effective avec toutes les données nécessaires. |
| N3-03-02 | C | Fixer un critère de fin d’exploration avant que la réserve de remontée soit atteinte. | Séparer déclenchement de remontée et pression finale ; le principe N2 reste partagé. |
| N3-03-03 | E | Choisir le membre limitant avec blocs, consommations et obligations de remontée différents. | Les comparaisons de phases simples N2 sont réutilisées ; ici comparer des retours complets. |
| N3-03-04 | E | Réévaluer le temps de fond lorsqu’un palier supplémentaire apparaît. | Relier le temps de palier à son coût réel en gaz, pas uniquement à une DTR affichée. |
| N3-03-05 | C | Distinguer palier obligatoire, palier de sécurité et temps de trajet dans un plan de retour. | Application à un budget donné ; les définitions seules sont réutilisées. |
| N3-03-06 | C | Définir une limite commune de DTR en tenant compte du gaz et des procédures de chacun. | Aucune durée universelle ni équivalence “DTR = consommation fond × DTR”. |
| N3-03-07 | E | Traiter un profil multi-niveaux dont une remontée intermédiaire devient beaucoup plus lente que prévu. | Recalcul d’une phase et révision du plan, sans inventer des paliers calculés hors modèle. |
| N3-03-08 | C | Identifier une redescente tardive ajoutée à un profil initialement prévu sans elle. | Contraintes de gaz et désaturation ; éviter “tout profil inverse est interdit”. |
| N3-03-09 | C | Adapter le briefing à un équipier qui reprend après une longue interruption. | Expérience récente, profondeur progressive, critères de renoncement ; pas de seuil arbitraire. |
| N3-03-10 | C | Réviser le plan lorsqu’un équipier devient froid ou fatigué avant le critère chiffré prévu. | Le plan n’oblige pas à poursuivre jusqu’aux maxima ; comparer aux cartes N2 déjà proches. |
| N3-03-11 | C | Définir ce qui doit être communiqué si l’ordinateur impose une nouvelle profondeur de palier. | Information comprise par toute la palanquée, reprise des contraintes communes. |
| N3-03-12 | C | Analyser un changement de sortie qui augmente à la fois trajet et durée de décompression. | Exercice à données complètes ; séparer calcul du gaz et décision finale si trop long. |

### N3-04 — Gestion du gaz : profondeur, remontée et partage

Sous-deck : **Physique**. Sources de départ : N3-S01 p.8, 13, 15 ; N3-S02 p.8–10 ; N2 chapitre 06. Vérifications : G08.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-04-01 | E | Passer d’un débit de référence à 1 bar à une baisse de pression en bar/min à 40 m. | Ajout : conversion litres → pression dans un bloc donné. |
| N3-04-02 | E | Refaire la conversion en bar/min à 55 m avec un autre volume de bloc. | Courte série d’automatisation ; pas de nouvelle définition de la pression. |
| N3-04-03 | E | Retrouver le débit de référence à partir d’une consommation en bar/min à profondeur donnée. | Sens inverse de la conversion ; hypothèses sur gilet/fuites/transitions explicites. |
| N3-04-04 | E | Comparer deux plongeurs dont les baisses en bar/min sont identiques mais les blocs différents. | Distinguer pression consommée et quantité de gaz ; opération différente du cas N2. |
| N3-04-05 | E | Calculer la consommation d’un trajet de remontée linéaire de 50 à 6 m. | Réutiliser la méthode N2 de pression moyenne ; prolongement au retour avec palier. |
| N3-04-06 | E | Ajouter un palier à 6 m puis à 3 m au budget d’un trajet de remontée donné. | Addition de phases ; les durées sont fournies, jamais inventées comme tables. |
| N3-04-07 | E | Calculer le gaz utilisé pendant une attente profonde avant le début d’une remontée assistée. | Coût du délai initial, souvent omis dans le calcul à deux. |
| N3-04-08 | E | Calculer le gaz nécessaire à deux équipiers pour un trajet et des paliers fournis. | Addition des deux débits de référence et de toutes les phases du retour. |
| N3-04-09 | E | Convertir le volume nécessaire au retour à deux en pression minimale dans le bloc donneur. | Réserve de retour exprimée dans le bon bloc, marge finale explicitement donnée. |
| N3-04-10 | E | Comparer deux réserves à pression identique pour une remontée à deux. | Volumes de blocs différents + scénario de retour ; ne pas refaire seulement 50 bar × volume. |
| N3-04-11 | E | Déterminer la pression de départ du fond à partir du retour, d’une attente et d’une marge imposée. | Ne pas confondre seuil de demi-tour, réserve de retour et pression finale. |
| N3-04-12 | E | Retrouver le temps de fond compatible avec un budget déjà diminué du retour complet. | Calcul inverse ; aucune règle des tiers présentée comme norme. |
| N3-04-13 | E | Calculer le besoin supplémentaire si les débits de stress augmentent pendant le retour partagé. | Analyse de sensibilité ; valeurs fictives données, pas “consommation universelle en stress”. |
| N3-04-14 | E | Trouver un temps de palier supplémentaire maximal dans un budget fictif restant. | Exercice algébrique limité aux hypothèses ; distinguer ce maximum théorique d’une décision réelle. |
| N3-04-15 | E | Choisir le bloc limitant dans une palanquée après conversion de tous les retours en pressions. | Comparaison en quantités/contraintes, pas au plus petit manomètre seul. |
| N3-04-16 | C | Détecter une erreur consistant à utiliser la consommation à 50 m pour tout le trajet et tous les paliers. | Expliquer l’erreur de modèle ; éventuellement comparer les résultats pour comprendre son effet. |
| N3-04-17 | C | Détecter l’oubli du temps d’attente, des deux consommateurs ou de la marge finale. | Un défaut ciblé par carte ; fusionner avec correction d’un exercice déjà conservé. |
| N3-04-18 | C | Interpréter une différence entre prévision et consommation observée en immersion. | Recalcul avant dépassement du seuil ; limites d’une mesure en bar/min. |
| N3-04-19 | C | Expliquer pourquoi une fraction fixe du bloc ne garantit pas le retour à deux pour tout profil. | Contre-exemple chiffré vérifié ; corriger le raccourci du cours 2024 p.10. |
| N3-04-20 | E | Comparer deux retours de même DTR mais de profondeurs et paliers différents. | Même durée, coût de gaz différent ; apport distinct de la définition de DTR. |

### N3-05 — Comprendre les modèles de désaturation

Sous-deck : **Désaturation**. Sources de départ : N3-S01 p.8, 13, 15 ; N3-S12 p.1–3 pour les M-values ; notice fabricant à acquérir. Vérifications : G02, G09.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-05-01 | F | Distinguer compartiment mathématique et organe anatomique. | Les compartiments ne sont pas seize organes directement mesurés. |
| N3-05-02 | F | Définir la période d’un compartiment pour un écart à l’équilibre sous conditions constantes. | Réponse concrète ; ne pas la définir comme “temps pour éliminer tout l’azote”. |
| N3-05-03 | E | Calculer la fraction d’un écart comblée après une période. | Exemple abstrait, données en pression de gaz inerte ; pas de calcul d’un palier réel. |
| N3-05-04 | E | Calculer la fraction d’un écart restante après deux périodes. | Sens inverse et cumul ; courte série à fusionner si trivialité constatée à la revue. |
| N3-05-05 | C | Comparer compartiment rapide et lent sur un changement bref de pression inspirée. | Lecture d’une courbe originale ; départ et gaz explicités. |
| N3-05-06 | C | Distinguer saturation, sous-saturation et sursaturation sur trois états donnés. | Les définitions générales de Henry restent dans les cartes communes N2. |
| N3-05-07 | C | Identifier le compartiment limitant dans un exemple de deux contraintes de remontée. | Le plus chargé en valeur absolue n’est pas automatiquement le plus contraignant. |
| N3-05-08 | F | Interpréter une M-value comme limite du modèle pour une pression ambiante donnée. | Pas de frontière garantissant l’absence d’accident. |
| N3-05-09 | V | Lire un graphique pression ambiante/pression du gaz inerte avec droite limite. | Axes et valeurs nommés ; schéma original simplifié. |
| N3-05-10 | R | Expliquer ce que réduit un gradient factor par rapport à la limite du modèle. | Déjà n2-ordinateurs-gf-principe-001 ; aucune nouvelle carte de définition. |
| N3-05-11 | E | Calculer une limite fictive avec Pamb, M et un GF donnés. | Limite = Pamb + GF × (M − Pamb), uniquement comme illustration mathématique. |
| N3-05-12 | F | Distinguer le rôle de GF bas et GF haut dans une stratégie de remontée. | Source fabricant précise ; ne pas donner une paire universelle “plus sûre”. |
| N3-05-13 | A | Relier le repère FFESSM pour la plongée à l’air au contexte N3. | Adapter n2-ordinateurs-gf-air-ffessm-001 après revue du champ N2/N3 ; éviter un doublon. |
| N3-05-14 | F | Distinguer Bühlmann, ZHL-16C et stratégie GF. | Famille/modèle/paramétrage ; pas trois synonymes. |
| N3-05-15 | F | Distinguer principes d’un modèle à gaz dissous et prise en compte des bulles dans une implémentation RGBM. | Source fabricant à compléter ; ne pas classer tous les RGBM comme une implémentation identique. |
| N3-05-16 | C | Distinguer azote résiduel, majoration MN90 et mémoire d’un ordinateur lors d’une successive. | Résoudre G02 ; ne jamais enseigner que les ordinateurs ignorent les successives. |
| N3-05-17 | F | Comprendre qu’un GF affiché n’est pas un pourcentage de risque personnel d’ADD. | Éviter “GF 85 = 15 % de risque en moins” ; comparer au fait N2 sur les limites des modèles. |

### N3-06 — Ordinateurs, écrans et cohabitation

Sous-deck : **Désaturation**. Sources de départ : N3-S01 p.9, 13, 15 ; N3-S02 p.28–30, 33 ; notices précises à acquérir. Vérifications : G09.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-06-01 | V | Interpréter ensemble profondeur courante, plafond et durée du prochain arrêt sur un écran simulé. | Les valeurs ne sont pas déjà étiquetées avec leur définition au recto ; reprendre N2 si identique. |
| N3-06-02 | V | Distinguer NDL, temps du palier courant et DTR/TTS sur un écran à plusieurs champs. | Lire un affichage original ; une seule opération demandée. |
| N3-06-03 | V | Comparer deux écrans avec plafonds et contraintes de remontée différents. | Prolongement des plafonds N2 ; compatible avec les notices des deux appareils. |
| N3-06-04 | C | Gérer des durées de paliers différentes à une profondeur compatible avec les deux appareils. | Éviter la formule floue “la procédure la plus pénalisante” ; en partie réutilisation N2. |
| N3-06-05 | C | Expliquer l’effet d’un réglage GF différent sur les contraintes communes de la palanquée. | Contrainte collective ; pas de classement absolu des appareils par sécurité. |
| N3-06-06 | V | Interpréter le mode planification d’un modèle donné avec un historique résiduel. | Notice et version ; ne pas inventer de calcul de palier ni omettre la successive. |
| N3-06-07 | V | Identifier une incohérence de mélange sélectionné sur un écran d’ordinateur emprunté. | Le fait générique N2 est partagé ; nouvelle carte seulement si lecture utile. |
| N3-06-08 | C | Distinguer affichage de profondimètre et calcul actif de désaturation. | Mode réellement documenté ; aucune procédure automatique de bascule attribuée à tous les modèles. |
| N3-06-09 | C | Définir avant immersion la conduite commune si l’un des ordinateurs tombe en panne. | Historique, moyen de secours et procédures validées ; jamais “copier simplement le binôme”. |
| N3-06-10 | C | Distinguer une alarme de vitesse normale des critères fédéraux de remontée anormale. | Deux cadres différents ; réutiliser les seuils N2 après G03. |
| N3-06-11 | C | Comprendre ce que peut et ne peut pas prévoir une DTR dans des conditions modifiées. | Gaz, vitesse, maintien de profondeur et paliers ; ne pas traiter une estimation comme une promesse. |

### N3-07 — Tables et plongées successives

Sous-deck : **Désaturation**. Sources de départ : N3-S01 p.15 ; N3-S02 p.31–33 ; N2 chapitre 12. Vérifications : G02, G03.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-07-01 | R | Reprendre profil carré, durée, arrondis et domaine des MN90. | Cartes N2 existantes, aucune série nouvelle de définitions. |
| N3-07-02 | R | Reprendre GPS, majoration et lecture des successives avec un extrait fourni. | Cartes n2-tables-gps/majoration/variables/successive déjà présentes ; garder les ID. |
| N3-07-03 | E | Relier un résultat de lecture de tables au budget de gaz d’une remontée fournie. | Cas combiné tables + gaz, uniquement si N3-03/04 ne couvre pas déjà l’objectif. |

### N3-08 — Risques de la profondeur et reconnaissance des accidents

Sous-deck : **Prévention des accidents**. Sources de départ : N3-S01 p.10–11, 15 ; N3-S02 p.37–45 ; N3-S04 p.24–29 ; CMPN à compléter pour l’OPI. Vérifications : G04, G05, G10.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-08-01 | C | Distinguer augmentation de densité du gaz et augmentation de pression partielle dans les risques profonds. | Mécanismes différents ; les lois et signes génériques sont déjà communs N2. |
| N3-08-02 | E | Calculer une pression partielle à 60 m dans un modèle d’air explicitement donné. | Une extension profonde ; aucune qualification nitrox ni seuil inventé. |
| N3-08-03 | C | Relier une tâche cognitive complexe à une marge réduite sous narcose. | Décision concrète en palanquée ; fusion si simple paraphrase de n2-narcose-equipier-001. |
| N3-08-04 | C | Interpréter une gêne respiratoire qui persiste malgré l’arrêt de l’effort. | Ne pas conclure automatiquement à un simple essoufflement ; triage, pas diagnostic certain. |
| N3-08-05 | F | Définir l’œdème pulmonaire d’immersion avec un mécanisme simple vérifié. | OPI explicitement nommé dans le MFT ; apport absent du socle N2 comme notion autonome. |
| N3-08-06 | C | Reconnaître un faisceau de signes évocateurs d’OPI en immersion ou au retour. | Ne pas exiger une expectoration mousseuse pour agir ; source CMPN actuelle. |
| N3-08-07 | C | Choisir les priorités devant une suspicion d’OPI sans attendre un diagnostic sur le bateau. | Sortie, prise en charge et alerte à établir sur recommandations actuelles. |
| N3-08-08 | C | Distinguer accident de désaturation, barotraumatisme pulmonaire et OPI sans retarder le secours. | Informations insuffisantes à un diagnostic unique : demander l’action commune, pas un faux diagnostic certain. |
| N3-08-09 | C | Évaluer l’effet combiné froid + effort + profondeur sur une fin de plongée. | Contraintes simultanées, pas trois répétitions des cartes existantes. |
| N3-08-10 | R | Repérer un possible problème de gaz commun à plusieurs plongeurs. | n2-essoufflement-air-pollue-001 et n2-gonflage-blocs-compresseur-001 ; ajout CO seulement si manque réel. |

### N3-09 — Assistance et sécurité en immersion

Sous-deck : **Prévention des accidents**. Sources de départ : N3-S01 p.9–11, 13 ; N3-S04 p.10–20. Vérifications : G04, G08.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-09-01 | C | Reconnaître un besoin d’assistance sans signe volontaire de l’équipier. | Comportement, ventilation et vigilance ; pas uniquement la récitation des signes. |
| N3-09-02 | C | Distinguer aide à un plongeur conscient coopératif et assistance à un plongeur qui ne réagit plus. | Contexte et priorités ; pas de chorégraphie de remontée enseignée par écrit. |
| N3-09-03 | C | Identifier les informations de gaz à transmettre quand un équipier utilise la source du donneur. | Le retour est désormais alimenté par un seul bloc ; lien au budget N3-04. |
| N3-09-04 | C | Relier une remontée assistée à la dilatation du gaz dans les deux équipements. | Surveillance du contrôle de flottabilité ; lois N2 partagées. |
| N3-09-05 | C | Identifier une décision qui rompt la cohésion pendant une assistance à trois plongeurs. | Rôle du troisième, observation et communication adaptés au cas. |
| N3-09-06 | C | Déterminer les priorités lors d’une assistance avec décompression obligatoire et gaz limité. | Données/procédure explicites ; ne pas proposer une conduite universelle improvisée. |
| N3-09-07 | F | Distinguer profondeur d’exercice, vitesse attendue pendant l’exercice et règles ordinaires de remontée. | Empêcher le transfert d’une tolérance d’évaluation à toutes les plongées ; retirer si pure question d’examen sans utilité. |
| N3-09-08 | C | Sécuriser la flottabilité et les voies aériennes au retour en surface. | Principes RIFAP ; les gestes de tractage/hissage restent à apprendre en pratique. |

### N3-10 — Secours en surface, alerte et oxygène

Sous-deck : **Prévention des accidents**. Sources de départ : N3-S04 p.4–5, 19–32, 34–35 ; N3-S01 p.10, 12 ; référentiels d’État et CMPN à compléter. Vérifications : G04, G05, G06, G10.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-10-01 | C | Répartir les tâches de secours selon les compétences disponibles sur un bateau. | Bilan, alerte, oxygène, récupération, surveillance : une tâche manquante ciblée. |
| N3-10-02 | C | Contrôler le retour de toutes les palanquées pendant la prise en charge d’un accidenté. | L’accident ne fait pas disparaître les plongeurs encore immergés. |
| N3-10-03 | R | Recueillir et conserver les ordinateurs/paramètres utiles de la palanquée. | Prolongement du recueil N2 ; réutiliser si recto générique suffisant. |
| N3-10-04 | F | Distinguer bilan vital, diagnostic médical et recueil des paramètres de plongée. | Le sauveteur ne retarde pas les gestes en attendant un diagnostic précis. |
| N3-10-05 | C | Choisir la prise en charge initiale d’une victime consciente avec gêne respiratoire. | Position et dispositif adaptés ; sourcer sans généraliser une position allongée. |
| N3-10-06 | C | Distinguer victime inconsciente qui respire normalement et absence de respiration normale. | Données et branche de secours nettes ; pas de test de diagnostic implicite. |
| N3-10-07 | F | Comprendre les spécificités d’une noyade dans une prise en charge de secours. | Ventilation et gestes appris en formation ; détails chiffrés seulement après référentiel d’État versionné. |
| N3-10-08 | C | Reconnaître une hémorragie importante dans un accident sur bateau ou épave. | Complément RIFAP 2026 ; décision prioritaire à sourcer au niveau PSC/PSE pertinent. |
| N3-10-09 | C | Reconnaître une situation de traumatisme qui exige de limiter les mobilisations. | Sécurisation du site et recours aux secours ; aucun algorithme médical improvisé. |
| N3-10-10 | C | Choisir inhalation ou assistance ventilatoire selon la respiration observée. | Source RIFAP + recommandations d’État ; préciser les compétences requises au scénario. |
| N3-10-11 | F | Connaître le débit d’oxygène du masque à haute concentration dans le cadre fédéral retenu. | Vérifier la couverture N2 ; un seul fait, pas un débit répété dans cinq rectos. |
| N3-10-12 | E | Déterminer l’autonomie théorique d’une bouteille d’O₂ avec volume, pression et débit donnés. | Modèle simplifié, stock utilisable et marge résiduelle explicites. |
| N3-10-13 | E | Comparer cette autonomie au temps estimé avant prise en charge. | Le temps annoncé n’est pas une durée garantie ; inclure la marge fournie. |
| N3-10-14 | E | Calculer le stock O₂ nécessaire pour deux victimes avec débits/durée imposés. | Deux consommations simultanées, différence réelle d’opération. |
| N3-10-15 | C | Identifier un risque de manipulation de l’oxygène dans la préparation du matériel. | Notice et référentiel d’État ; éviter graisse/flamme/installation improvisée. |
| N3-10-16 | C | Choisir le canal d’alerte en mer depuis le bateau ou depuis l’intérieur des terres. | VHF, 196, 15/112 selon contexte ; faits N2 partagés quand déjà exacts. |
| N3-10-17 | C | Transmettre la position et les informations de gravité dans un appel simulé. | Les informations manquantes changent la prise en charge ; pas un QCM de vocabulaire. |
| N3-10-18 | C | Distinguer PAN-PAN, détresse et déclenchement ASN dans une situation précisément décrite. | G06 obligatoire ; ne pas transformer toute urgence médicale en même message automatique. |
| N3-10-19 | C | Actualiser la fiche d’évacuation et transmettre une aggravation pendant l’attente. | Chronologie, surveillance, nouvelles victimes et stock O₂ ; exemple utile. |
| N3-10-20 | F | Distinguer entretien des compétences RIFAP et expiration administrative du brevet. | Recommandation 2026 de réactualisation ; pas de durée d’expiration inventée. |

### N3-11 — Matériel et préparation pour une plongée profonde

Sous-deck : **Matériel et préparation**. Sources de départ : N3-S01 p.8–13 ; N3-S02 p.12–13 ; notices fabricant à compléter. Vérifications : G07, G09.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-11-01 | C | Choisir une configuration compatible avec la fourniture de gaz à un équipier à la profondeur prévue. | Minimum réglementaire déjà N2 ; ici capacité/configuration documentée selon matériel. |
| N3-11-02 | R | Distinguer deux bouteilles reliées et deux réserves réellement isolables dans un bi-bloc. | n2-gonflage-blocs-bi-001 ; pas de doublon ni d’obligation universelle de bi-bloc N3. |
| N3-11-03 | C | Relier un défaut de détendeur identifié avant immersion à une décision de départ. | Cas documenté ; pas de réparation interne ni de diagnostic certain à partir d’un seul symptôme. |
| N3-11-04 | E | Comparer le comportement de deux blocs à partir de leur masse et volume extérieur réels. | Si reprise du caisson N2 sans gain, réutiliser ; pas de règle “acier toujours plus lourd”. |
| N3-11-05 | C | Vérifier la stabilité à faible profondeur après consommation d’une partie importante du gaz. | n2-flottabilite-palier-bloc-allege-001 déjà très proche : privilégier reprise ou fusion. |
| N3-11-06 | C | Vérifier la compatibilité dévidoir/parachute et le risque de traction pendant son lancement. | Source fabricant ; le principe de ne pas se solidariser au dévidoir est déjà partagé. |

### N3-12 — Orientation, milieu et environnement

Sous-deck : **Matériel et préparation**. Sources de départ : N3-S01 p.8–9, 12–15 ; N3-S11 p.13–28 comme complément ancien ; sources locales/SHOM/DORIS à acquérir. Vérifications : G07, G11.

| Objectif | Format | Connaissance ou opération à travailler | Apport et consigne de rédaction |
|---|---|---|---|
| N3-12-01 | E | Construire un retour avec deux changements de cap et un obstacle explicitement donné. | Les deux caps réciproques simples N2 sont réutilisés, pas redéclinés. |
| N3-12-02 | C | Distinguer cap suivi et trajectoire réelle lorsqu’un courant entraîne la palanquée. | Déplacement relatif au fond ; schéma original avec direction du courant donnée. |
| N3-12-03 | C | Combiner repères naturels et compas quand la visibilité diminue. | Données géométriques suffisantes ; pas de réponse abstraite “utiliser les deux”. |
| N3-12-04 | V | Interpréter un profil de relief pour éviter une fausse remontée vers une roche isolée. | Carte bathymétrique simplifiée originale, critères de retour explicites. |
| N3-12-05 | C | Réagir à une perte d’orientation avant que la limite de gaz ne soit atteinte. | Parcours de repli et communication ; comparer au cas N2 sur la sortie alternative. |
| N3-12-06 | C | Prévoir le risque de trafic en surface après une remontée loin du mouillage. | Signalisation/récupération et règles locales ; pas de distance nationale inventée. |
| N3-12-07 | C | Limiter contact et remise en suspension lors d’un passage étroit au-dessus du fond. | Position, trajectoire et technique générale ; connaissances N2 conservées. |
| N3-12-08 | C | Adapter l’éclairage et l’observation pour limiter le dérangement des organismes. | Comportement sur un cas concret ; aucune intensité de phare universelle. |
| N3-12-09 | V | Distinguer végétation marine et organisme animal sessile à partir d’une observation locale. | Images originales ou licence vérifiée ; choix d’espèces défini avant rédaction. |
| N3-12-10 | V | Identifier un habitat sensible et expliquer l’effet d’un mauvais mouillage. | Posidonie, coralligène ou autre habitat local : secteur et source précis. |
| N3-12-11 | V | Reconnaître une faune présentant un risque de contact dans le secteur choisi. | Identification + conduite pertinente ; pas un catalogue encyclopédique d’espèces. |
| N3-12-12 | C | Préparer une sortie sur un nouveau site en croisant carte, réglementation et informations locales. | Synthèse de deux contraintes ; fusion avec N3-02 si même apprentissage. |

## Exercices pilotes et corrigés de référence

Ces exemples fixent le niveau de précision attendu lors de la rédaction. Les valeurs sont **fictives et imposées pour les exercices** ; elles ne définissent ni profil de décompression ni réserve opérationnelle. Les cartes finales devront isoler une opération ou une décision au recto. Les vitesses/durées fournies dans les exercices ne constituent pas des recommandations de plongée.

### E1 — Débits en litres/minute et bar/minute

Hypothèses : gaz parfait, température constante, 1 bar à la surface, +1 bar/10 m, volume intérieur du bloc constant, seul le gaz respiré fait diminuer la pression. `q₀` représente le débit ramené à 1 bar, pas les litres effectivement inspirés à la pression ambiante.

- Bloc 15 L, q₀ = 18 L/min, profondeur 40 m : Pamb = 5 bar ; débit ramené à 1 bar = 90 L/min ; baisse du manomètre = **6 bar/min**.
- Bloc 12 L, q₀ = 22 L/min, profondeur 55 m : Pamb = 6,5 bar ; débit = 143 L/min ; baisse = **11,92 bar/min** environ.
- Sens inverse : bloc 12 L, baisse de 9 bar/min à 40 m ; q₀ = 9 × 12 / 5 = **21,6 L/min à 1 bar**.

Relation de cours : `Δp/Δt ≈ q₀ × (Pamb / 1 bar) / Vbloc`. Pour une mesure réelle, gaz ajouté au gilet, fuites et changement de température empêchent d’attribuer automatiquement toute la baisse à la ventilation.

### E2 — Retour à deux avec attente, trajet et paliers fournis

Deux équipiers utilisent un seul stock. Débits de référence imposés : 30 et 40 L/min à 1 bar, constants dans cet exercice. Départ à 50 m, attente de 1 min à cette profondeur ; trajet linéaire jusqu’à 6 m en 4,4 min ; arrêt fourni de 3 min à 6 m ; trajet 6 → 3 m en 0,5 min ; arrêt fourni de 5 min à 3 m ; trajet 3 m → surface en 0,5 min. Les arrêts sont des données, pas une décompression calculée. Même modèle de pression que E1.

| Phase | Pression utilisée | Gaz ramené à 1 bar |
|---|---:|---:|
| Attente à 50 m, 1 min | 6 bar | 420 L |
| Remontée 50 → 6 m, 4,4 min | Moyenne 3,8 bar | 1 170,4 L |
| Arrêt à 6 m, 3 min | 1,6 bar | 336 L |
| Trajet 6 → 3 m, 0,5 min | Moyenne 1,45 bar | 50,75 L |
| Arrêt à 3 m, 5 min | 1,3 bar | 455 L |
| Trajet 3 m → surface, 0,5 min | Moyenne 1,15 bar | 40,25 L |
| **Total pour les phases données** | | **2 472,4 L** |

Dans un bloc donneur de 15 L, ces phases correspondent à **164,83 bar** de baisse théorique. Si l’énoncé impose encore 20 bar à la fin, le seuil théorique initial devient **184,83 bar**, arrondi au supérieur à **185 bar** dans le modèle. Une autre marge ou consommation modifierait ce seuil. Ce résultat ne démontre pas qu’une plongée réelle serait réalisable : le profil, les consommations, la décompression et le matériel sont imposés pour l’exercice.

Angles réellement distincts à conserver : (a) conversion du total en pression ; (b) oubli du coût de l’attente ; (c) retour à deux au lieu d’un consommateur ; (d) comparaison de deux blocs ; (e) effet d’un palier supplémentaire. Éviter cinq cartes qui demandent simplement de refaire la même somme.

### E3 — Même durée totale, coût de gaz différent

Deux trajets fictifs de 6 min alimentent un seul plongeur, q₀ = 20 L/min à 1 bar. Trajet A : 2 min à 40 m puis 4 min à 3 m ; trajet B : 4 min à 40 m puis 2 min à 3 m. Les transitions sont volontairement exclues de cet exercice de comparaison, et les deux durées ne sont donc pas des DTR opérationnelles.

A : 20 × (2 × 5 + 4 × 1,3) = **304 L**. B : 20 × (4 × 5 + 2 × 1,3) = **452 L**. La durée seule ne détermine pas le coût en gaz ; la répartition en profondeur compte aussi.

### E4 — Modèle abstrait de compartiment et GF

Un compartiment fictif a une pression initiale de gaz inerte de 2 bar et une pression d’équilibre de 4 bar, maintenue constante. Après une période : **3 bar** ; après deux périodes : **3,5 bar**. Les fractions portent sur **l’écart à l’équilibre**, pas sur un pourcentage de tout le gaz contenu dans un tissu humain.

Autre illustration indépendante : Pamb = 1,6 bar, M = 2,4 bar et GF = 85 %. Limite fictive = 1,6 + 0,85 × (2,4 − 1,6) = **2,28 bar**. Cela illustre une interpolation dans un modèle ; aucun temps de palier ni risque médical individuel n’est déduit de ce calcul.

### E5 — Capacité d’oxygène et délai fourni

Bouteille de 5 L à 200 bar, résiduel imposé de 20 bar ; débit constant de 15 L/min. Modèle nominal simplifié : 5 × (200 − 20) = **900 L utilisables**, soit **60 min**. Deux victimes consommant chacune 15 L/min donnent **30 min**. Pour un délai fourni de 75 min, ce stock ne suffit pas même pour une seule victime. Les pertes, équipements et marges réelles doivent être traités selon le matériel et les consignes validées ; ne pas modifier le débit prescrit pour faire durer une réserve insuffisante.

Le RIFAP p.28 donne environ une heure pour une bouteille de 5 L à 200 bar et 15 L/min. L’exercice explicite son propre résiduel ; distinguer approximation pédagogique et capacité réelle jusqu’à la prise en charge. Un délai de secours présenté dans un support ne constitue pas une garantie pour un site donné.

## Couverture du référentiel

| Attendu du MFT / RIFAP | Modules et cartes communes mobilisés | Validation attendue |
|---|---|---|
| Conditions, prérogatives, responsabilités — MFT p.3–4, 12, 15 | N3-01, N3-02 ; documents/assurance communs N2 | Cas avec/sans DP, mineur/majeur, aptitude limitante ; G01 clos. |
| Planifier la plongée — MFT p.8 | N3-03, N3-04, N3-06 ; gaz/pression N2 | Au moins un retour complet et une décision de limite collective. |
| Évoluer en autonomie — MFT p.9 et 13 | N3-03, N3-06, N3-09, N3-12 ; orientation/communication N2 | Lecture réelle ou simulée vérifiée, gestion d’un imprévu et cohésion. |
| Intervenir et porter assistance — MFT p.10 | N3-08, N3-09, N3-10 ; accidents N2 | Reconnaissance sans signe volontaire, priorité d’assistance, retour en surface, relais aux secours. |
| S’adapter à la profondeur — MFT p.11 | N3-03/04/08/11 ; prévention N2 | Gaz, densité, narcose, froid, désaturation ; pas seulement des définitions à 60 m. |
| Organiser sans DP — MFT p.12 | N3-01/02/10/12 | Deux ou trois contextes utiles : bateau, départ du bord/eau intérieure, conditions de récupération changeantes ; aucune obligation inventée. |
| Physique et consommation en L/min et bar/min — MFT p.13, 15 | N3-04 ; physique N2 | Calculs directs/inverses, trajet, palier, deux consommateurs ; corrigés indépendants. |
| Modèles, M-values, GF, successives — MFT p.15 | N3-05/06/07 ; tables/GF N2 | G02/G09 clos ; modèle distinct de la physiologie et du risque individuel. |
| Milieu et comportement — MFT p.14–15 | N3-02/12 ; environnement N2 | Site, habitat/organisme contextualisé, comportement ; sources et droits contrôlés. |
| RIFAP capacité 1 — communiquer, sécuriser la surface | N3-09 + communication N2 | Priorités et compréhension ; validation pratique distincte. |
| RIFAP capacité 2 — mettre hors d’eau | N3-09/10 | Voies aériennes, flottabilité, adaptation au support ; tractage/hissage pratiqués en formation. |
| RIFAP capacité 3 — palanquée, matériel, informations | N3-10 + transmission N2 | Comptage, regroupement, paramètres conservés et fiche. |
| RIFAP capacité 4 — coordination | N3-02/10 | Répartition selon compétences et présence d’autres plongeurs. |
| RIFAP capacité 5 — bilan et premiers secours | N3-08/10 | Conscience/respiration, noyade, hémorragie/traumatisme ; G04/G10 clos. |
| RIFAP capacité 6 — O₂ et surveillance | N3-10 + prise en charge N2 | Mode adapté, débit, autonomie, surveillance ; G05 clos pour hydratation/positions. |
| RIFAP capacité 7 — acteurs, alerte, suivi | N3-10 | Canal, localisation, message, évolution et liaison médicale ; G06 clos. |

Cette matrice couvre les **attendus théoriques et de préparation**, pas l’exécution pratique ni la certification. Les modalités de validation du MFT p.16 seront conservées dans les notes de méthode ; pas de cartes sur la mise en page de la fiche ou sur les noms des évaluateurs sans utilité pour le plongeur.

## Ordre d’exécution et lots de travail

### Lot 0 — Fixer le socle et les références

- [ ] Lire les sources primaires téléchargées dans leur intégralité pour le lot concerné ; contrôler les tables/figures et compléter le relevé de divergences.
- [ ] Acquérir et dater Code du sport, CMPN, PSC/PSE, notices et sources locales nécessaires.
- [ ] Clore G01 ; établir clairement les frontières FFESSM / réglementation / fabricant.
- [x] Relire les rectos, **versos, choix et sources** des 164 candidates R et valider leur appartenance N3 : [bilan](reviews/n3/00-reprises-n2.md).
- [ ] Traiter les 7 adaptations A et les 8 revalidations V avant leur éventuelle inclusion N3.
- [ ] Fixer la liste finale partagée et marquer chaque proposition nouvelle comme distincte/fusion/reprise/retrait, avec motif.
- [ ] Conserver les retraits N2 et réserver les ID ; aucun renommage de cartes existantes.

### Lot 1 — Prérogatives et organisation

Rédiger N3-01 et les situations réglementaires de N3-02. Partager documents communs vérifiés. Préparer deux ou trois contextes d’organisation suffisamment différents, en fournissant les conditions locales. Critère de sortie : chaque cas de profondeur/âge/DP a une réponse unique et toutes les conditions fines sont sourcées.

### Lot 2 — Gaz et planification

Rédiger N3-04 puis N3-03. Réutiliser les méthodes élémentaires N2 et tester E1–E3. Critère de sortie : les erreurs de conversion, d’attente, de réserve et de retour à deux sont couvertes sans multiplications artificielles de cartes ; chaque calcul a un corrigé obtenu indépendamment.

### Lot 3 — Modèles et instruments

Rédiger N3-05, N3-06 et décider des reprises N3-07. Clore G02/G09. Produire des SVG/écrans **originaux**, compatibles avec un modèle/une notice identifiés ; légendes lisibles sur mobile. Critère de sortie : GF et plafonds exacts, successives comprises, pas de “procédure la plus pénalisante” laissée abstraite.

### Lot 4 — Profondeur et assistance

Rédiger les apports N3-08 et N3-09 après revue des accidents N2. Compléter l’OPI par des références médicales primaires. Critère de sortie : conduite claire devant signes communs et absence de fausse certitude diagnostique ; pas de transformation d’une description d’exercice en procédure générale.

### Lot 5 — Secours et oxygène

Rédiger N3-10 ; clôturer G03–G06/G10. Réexaminer les cartes N2 dont le texte récent modifie ou précise la portée ; consigner séparément toute correction commune avant partage. Critère de sortie : sept capacités RIFAP couvertes dans leur partie théorique, appel médical correctement cadré, capacité d’O₂ vérifiée, aucun conseil ancien recopié sans revue.

### Lot 6 — Matériel, navigation et milieu

Terminer N3-11/N3-12 et les cas restants N3-02. Clore G07/G11 et contrôler les illustrations/droits. Critère de sortie : matériel individuel/collectif clairement situé, orientation exploitable et environnement contextualisé sans sous-decks minuscules.

### Lot 7 — Revue globale et publication

Comparer **l’ensemble N2 + N3**, pas uniquement chaque fichier. Clore les doublons, vérifier les scénarios de gaz et de secours, compléter la matrice de couverture et vérifier les versions des sources. Puis contrôles techniques, revue de rendu, import d’essai et publication selon le workflow ci-dessous. Les lots encore incertains restent hors du build standard.

## Workflow d’écriture, revue et build

1. Préparer un YAML par module qui possède du contenu nouveau, dans `cards/n3/`. `levels: [N3]`, `status: draft`, `source_id: N3-XX-YY` pour la traçabilité. Pour le socle partagé, modifier les niveaux dans les fichiers existants seulement après la revue correspondante.
2. Tenir `docs/reviews/n3/XX-theme.md` : objectifs, IDs, contribution distincte, reprises/fusions, sources versionnées, calculs indépendants, divergences résolues et encore ouvertes. Les notes éditoriales restent dans ces revues, pas sur les versos.
3. Vérifier recto, verso, explication et **chaque distracteur**. Les nombres, unités, hypothèses et la portée de la réponse doivent suffire à lever les ambiguïtés. Lire les QCM sans la bonne réponse pour contrôler la plausibilité des leurres.
4. Faire une passe critique distincte de la rédaction ; ne pas confondre test de schéma et exactitude. Passer uniquement les cartes validées à `reviewed`. Toute source complémentaire non acquise ou conflit non résolu garde les cartes concernées en brouillon.
5. Exécuter `make check`, puis `make build`. Aucun changement de schéma attendu ; `make schema` uniquement si le schéma change réellement. Le support N3 et les GUIDs communs entre niveaux existent déjà.
6. Inspecter rectos/versos et médias dans le package, notamment sur affichage étroit. Vérifier unités, lisibilité des écrans, compatibilité SVG/HTML, mélange des choix et absence de fuite de la réponse.
7. Vérifier dans un profil Anki de test : nombres de notes, catégories, unicité, historique N2 intact après import, GUID identiques pour les cartes communes N2/N3/N4 et conservation des cartes suspendues. Vérifier une mise à jour du paquet après ajout des niveaux N3/N4, puis une étude filtrée N4.
8. Réaliser un commit cohérent par lot révisé ; `git push origin main` publie les commits et déclenche la CI/release. `make push` construit et importe le paquet unique dans l’Anki local puis synchronise AnkiWeb. Une publication GitHub et un import local sont deux actions distinctes.
9. Actualiser README, statistiques par niveau et docs de couverture uniquement après validation du contenu publié. Ne pas annoncer un N3 utilisable tant que ses objectifs essentiels restent en brouillon.

## Critères de clôture

- [ ] Chaque ligne du catalogue a une issue : carte revue, reprise, fusion ou exclusion motivée.
- [ ] Toutes les candidates communes ont une décision finale ; leur contexte N3 et leurs sources sont contrôlés.
- [ ] Couverture MFT p.8–15 et sept capacités RIFAP tracée ; les connaissances pratiques non évaluables par Anki sont identifiées dans la documentation.
- [ ] G01–G11 clos pour toutes les cartes publiées ; les éventuelles cartes écartées n’entraînent pas un manque essentiel non documenté.
- [ ] Aucun fait simple décliné artificiellement ; aucun cas chiffré résolu par un indice donné dans sa formulation.
- [ ] QCM plausibles, réponse vraie unique, contexte sans ambiguïté ; sigles développés et explications concrètes.
- [ ] Calculs indépendamment vérifiés ; les réserves, débits, marges et temps de paliers ne sont jamais présentés comme universels.
- [ ] Aucun conseil de secours ancien, diagnostic certain à signes non spécifiques, ni stratégie d’ordinateur inventée.
- [ ] Statistiques exactes, tests/validation/build réussis, rendu vérifié, IDs et historique N2 préservés.
- [ ] Sources privées et paquets hors Git ; publication accompagnée du bilan de revue.

## Estimation de complexité

**Technique : faible.** Le dépôt sait déjà filtrer N3, construire un package et partager explicitement une carte entre niveaux. Le travail attendu est surtout du contenu, des illustrations et de la revue ; aucun nouveau moteur de build n’est nécessaire.

**Rédaction/relecture : moyenne à élevée.** Les 140 propositions nouvelles donnent un ordre de grandeur de **120 à 150 nouvelles cartes**, après les fusions et exclusions, sans quota. La sélection validée de 164 reprises donne un N3 complet autour de **280 à 315 cartes** si elle est conservée ; ce total peut baisser quand les acquis N2 simplement redondants sont retirés. Ces nombres ne sont ni une exigence du diplôme ni un résultat garanti avant la rédaction.

**Vérification : élevée sur quatre blocs.** Réglementation sans DP/mineurs ; gaz à deux avec phases et marges ; GF/modèles/écrans ; secours et divergences entre textes. Leur revue distincte doit faire partie du travail prévu, pas être ajoutée après la publication.

Ordre de grandeur, pour une personne connaissant le dépôt et rédigeant soigneusement : **8 à 14 journées de travail effectif**, comprenant acquisition/revue des compléments (1–2 j), tri final des reprises (1–2 j), rédaction et exercices (3–5 j), revue factuelle/pédagogique et illustrations (2–4 j), validation finale/publication (environ 1 j). Les fourchettes ne s’additionnent pas strictement : certaines lectures/revues se font pendant chaque lot. Une clarification externe CTN/CMPN peut ajouter un délai calendaire, sans empêcher les modules indépendants d’avancer. Ce chiffrage est une estimation de charge éditoriale, pas une promesse de durée d’exécution automatisée.

## Bilan de la préparation

Documents récupérés, versions et empreintes consignées ; tri provisoire de toutes les cartes N2 effectué ; objectifs, couverture, exercices pilotes et séquence de réalisation établis. Les compléments primaires et divergences listés dans G01–G11 restent du travail explicite avant la publication des cartes concernées. Les cartes N2 et le placeholder N3 ont été conservés inchangés pendant la préparation initiale. La première passe d’implémentation a ensuite partagé 164 cartes N2 avec N3 et ajusté deux formulations de contexte ; les nouvelles cartes N3 restent à rédiger.
