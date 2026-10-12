# Plan d’implémentation de la théorie N4 FFESSM

Préparé le **12 octobre 2026**, catalogue au commit `a9a7229` : 461 cartes existantes,
339 dans N2 et 122 dans N3. **Statut : plan éditorial, aucune carte N4 rédigée.**

## Combien de cartes ?

Le plan retient **143 nouvelles cartes candidates** pour le complément N4.
Ce nombre résulte des objectifs détaillés ci-dessous, après absorption de neuf
propositions redondantes. Ce n’est ni un quota ni une garantie qu’exactement 143
cartes seront publiées : une fusion, une couverture existante découverte ou une
lacune factuelle peut encore le modifier. Les sources ne sont pas converties page
par page en cartes. Aucun objectif déjà interrogé n’est recopié pour compléter N4.

À ce stade, les 143 ajouts porteraient la collection entière de 461 à **604 notes**,
avec les IDs existants conservés. Le sous-paquet N4 contiendrait ces compléments ;
les préalables restent physiquement dans N2/N3. Le nombre de cartes pertinentes au
programme N4 est donc supérieur à 143 : il comprend les acquis antérieurs retenus.

Le [tri des 461 cartes existantes](reviews/n4/REUTILISATION_N2_N3.md) identifie **333 reprises candidates** : 321 R, 2 A et 10 V. Si elles étaient toutes validées, la sélection taguée N4 compterait **476 cartes**, dont 143 nouvelles. Les 119 P restent des préalables disponibles et les 9 H des détails de certification antérieure. Aucun de ces tags n’a encore été ajouté.

## Ce que couvre le plan

Le périmètre est le **GP-N4 FFESSM à l’air en France**, dans le cadre de ses fonctions
et des établissements concernés. Le [MFT national acquis, mai 2026](../sources/n4/ffessm-niveau-4-guide-de-palanquee.pdf),
référence N4-S01, est prioritaire. Le programme écrit/oral est complété par les
connaissances nécessaires à l’accueil, au guidage, à l’environnement et au matelotage,
qui préparent des épreuves pratiques. Une carte ne valide pas un geste, une remontée,
un nœud effectivement réalisé ou un oral maîtrisé.

- Écrit 10 : désaturation, mécanismes et cas de gestion collective.
- Écrit 11 : physiologie, prévention des accidents hors ADD et gestion de l’effort.
- Écrit 12 : fonctions, réglementation et vie fédérale.
- Oral 13 : fonctionnement du matériel, choix et lecture d’éclatés.
- Préparation pratique : conduite de palanquée, matelotage et respect du milieu.

Le MFT p.33 signale la suppression de l’ancienne épreuve « aspects théoriques de
l’activité » en décembre 2025. Sa page 25 ne reprend plus l’ancien problème MN90
obligatoire. Les cartes de tables et les exercices de physique existants restent
utiles, mais ne justifient pas la création d’une nouvelle série obligatoire N4.
Les approfondissements de mécanique, de volumes et de physiologie sont marqués
comme tels quand ils dépassent ce qui est directement exigible.

Le programme actuel limite certains détails : oreille = acquis N3 appliqués au GP ;
mécanisme de la narcose et de l’OPI non demandé ; matériel = forces et principes,
sans valeurs ni équations exigibles ; électronique des ordinateurs non exigible.
Pas de nouveaux catalogues d’anatomie, d’espèces, de normes ou de barèmes sportifs.

## Sources et méthode du recoupement

- [Inventaire des 59 PDF / 1 050 pages](SOURCES_N4.md), [manifestes et versions](reviews/SOURCES_N4.json).
- Lecture des rubriques de compétences, de conduite, de matelotage, de théorie et
  d’accès à l’examen du MFT actuel ; repérage des sections utiles des cours acquis.
- Lecture des 461 rectos/clés actuels, puis consultation des corrigés voisins pour
  les objectifs susceptibles d’être des doublons. Les absences ci-dessous portent
  sur les tâches interrogées, pas seulement sur la présence d’un mot dans un fichier.
- [Matrice de couverture N4](reviews/n4/COUVERTURE_PLAN.md) : distingue acquis,
  nouvelles tâches et limites pratiques. Il reste à vérifier chaque assertion des
  nouveaux rectos, clés, distracteurs et corrigés à la rédaction.

Il n’est pas prétendu ici que les 1 050 pages ont toutes reçu une revue factuelle
complète. Les cours et annales aident à expliquer ou entraîner ; leur ancienneté,
leurs formulations et leurs corrigés ne déterminent pas à eux seuls le programme.

## Organisation dans Anki et dans le dépôt

Un seul paquet livré, `diving-fr.apkg`. Arborescence classique :

```text
Plongée
├── N2  (base existante)
├── N3  (compléments existants)
└── N4
    ├── Réglementation
    ├── Conduite de palanquée
    ├── Désaturation
    ├── Prévention des accidents
    ├── Matériel et préparation
    └── Matelotage et milieu
```

Les neuf modules de rédaction ne sont pas neuf sous-paquets : ventilation et
prévention sont regroupées, circulation et désaturation également. Les YAML peuvent
rester par chapitre dans `cards/n4/`, sans imposer un sous-paquet par petit lot.
Les cartes communes gardent leur ID, leur modèle et leur paquet N2 ou N3. Après
validation du champ d’application, un éventuel tag N4 vient de `levels`, sans copie,
paquet filtré, migration ou changement de GUID. Les IDs ci-dessous sont des IDs
**proposés, non publiés** ; les anciens IDs, même retirés, ne sont jamais recyclés.

## Lots et ordre de travail

D’abord fermer les contrôles de versions et relire les reprises R/A/V, par chapitre.
Ensuite traiter les modules dans l’ordre ci-dessous. Pour chaque module, découper
**en lots séquentiels de huit cartes au maximum** : rédiger, vérifier, critiquer,
corriger, relire puis clore avant de passer au lot suivant. Les cartes commencent
`draft` ; aucun lot n’est accepté par les seuls tests.

Le QCM est le format prévu dès qu’il permet une question claire, une seule clé et
des leurres solides. Cela inclut schémas, séquences, cas et calculs. Aucun quota de
réponses libres. Pour les schémas, produire un dessin original et masquer les labels
révélateurs ; pour les forces, préciser le montage ; pour un ordinateur, préciser
modèle/mode/notice ; pour un calcul, donner unités, réserves et hypothèses.
Un leurre doit avoir un attrait et une réfutation précis, consignés dans la revue.

| Module | Ajouts prévus | Catégorie Anki |
| --- | ---: | --- |
| 1. Cadre fédéral, fonctions et responsabilités | 20 | Réglementation |
| 2. Accueil et conduite d’une palanquée | 16 | Conduite de palanquée |
| 3. Désaturation : compléments de compréhension et cas de guide | 6 | Désaturation |
| 4. Ventilation et échanges gazeux | 14 | Prévention des accidents |
| 5. Circulation, transport et shunts | 12 | Désaturation |
| 6. Prévention : lacunes et situations nouvelles | 15 | Prévention des accidents |
| 7. Fonctionnement du matériel et lecture de schémas | 36 | Matériel et préparation |
| 8. Matelotage, repérage et rôle d’équipier | 17 | Matelotage et milieu |
| 9. Découverte et protection du milieu | 7 | Matelotage et milieu |
| **Total** | **143** | |

## Vérifications à fermer avant publication

| Porte | Travail à effectuer / raison |
| --- | --- |
| G01 — cadre actuel | Comparer le MFT mai 2026 aux articles A322-71 à A322-101 et annexes consolidés, dont l’annexe III-15b modifiée au 17 janvier 2026. Vérifier âge de certification/exercice, milieu artificiel, baptêmes, E2, N5 et MF1. La mention d’une décision en attente dans le MFT ne suffit pas à clore la règle légale. |
| G02 — vie fédérale et droit | Vérifier honorabilité, signalement, contrats d’assurance/assistance, signature numérique et conditions juridiques exactes des cas civils/pénaux. Pas de diagnostic juridique automatique d’un fait divers fictif. |
| G03 — cas de guide | Construire des situations où le contexte impose réellement une décision distincte ; pas de « prudence contre imprudence ». Faire contrôler récupération/hélice selon le support et les consignes réelles ; aucune position universelle du GP. |
| G04 — procédures et modèles | Recontrôler les recommandations CTN actuelles, les notices et l’articulation RIFAP ; garder le contexte air/ordinateur. Ne pas transférer aux ordinateurs les recettes MN90 des vieilles annales. Recalculer séparément les exercices de compartiments et gaz. |
| G05 — données médicales | Croiser CMPN/RIFAP, références de physiologie et publications spécialisées pour shunts, CO2, froid, déshydratation et hypoxie. Aucune valeur fixe ni causalité absolue recopiée d’un diaporama. |
| G06 — contradictions repérées | N4-S16 p.4/p.15 donnent des présentations discordantes de contrôle ventilatoire ; p.7 nie réchauffement/humidification que p.9 décrit ; N4-S17 p.21 emploie « hématose » pour les échanges tissulaires ; revalider les définitions et le transport O2/CO2. Ces formules ne sont pas des corrigés prêts à publier. |
| G07 — apnée | N4-S18 p.13 décrit la samba avec perte de connaissance : distinguer perte de contrôle moteur et syncope avec une référence actuelle. Recontrôler hyperventilation, remontée, surveillance en surface et échauffement ; ne pas transformer une astuce d’entraînement en protocole de sécurité. |
| G08 — matériel | Acquérir les notices des montages choisis. Vérifier forces, chambres, compensation/surcompensation, givrage, Venturi/Vortex, gilets et manomètres. Pas de sens universel d’une variation de HP pour tous les détendeurs simples. |
| G09 — station et normes | Revalider réglementation de gonflage/TIV, notices de station et compatibilité des ensembles. Le MFT dit « flexible identique » : contrôler la portée technique avant d’affirmer obligation de marque ou autorisation universelle de remplacement. |
| G10 — nautique | Le cours Foubert est ancien : contrôler division 240, textes locaux, ANFR et notices du support. Valider dessins de nœuds et usages ; pas de longueur de mouillage ni procédure de récupération universelle. |
| G11 — environnement | Choisir espèces/site/saison (socle mer et eau douce), consulter DORIS/OFB/charte pertinente, vérifier statut de protection et droits. Les illustrations de cours ne sont pas réutilisées sans autorisation. |

Ces portes sont **ouvertes pour la nouvelle rédaction N4**. Les travaux déjà clos
pour N2/N3 restent consultables, mais ne sont pas automatiquement requalifiés en
validation de nouveaux cas N4.

## Toutes les cartes à mettre en place

Chaque ligne vise une seule tâche. Les IDs voisins servent à vérifier l’apport et
à éviter les copies ; ils ne sont pas des cartes à réécrire systématiquement.
Les sources sont des repères de section physique dans les PDF. À la rédaction,
préciser les pages exactes de l’affirmation et ajouter la source primaire nécessaire.
Les tâches proposées ci-dessous ne sont pas des rectos/corrigés déjà validés.

### 1. Cadre fédéral, fonctions et responsabilités — 20 cartes

- [ ] **`n4-cadre-certification-exercice-001`** — Distinguer âge de présentation à l’examen GP-N4 et âge d’exercice de l’encadrement, dans un cas de candidat mineur.
  - Apport : Certification de guide et exercice de sa fonction, distincts de l’autonomie N3. Acquis voisins : `n3-prerogatives-age-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-admission-001`** — Identifier le dossier permettant de se présenter à l’examen GP-N4 : certification préalable, RIFAP et aptitudes attestées ; conditions non interrogées dans les autres cartes expliquées au verso.
  - Apport : Accès à un examen de cadre, et non à la formation N3. Acquis voisins : `n3-formation-prerequis-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-pe12-pe20-pe40-001`** — Déterminer la profondeur autorisée pour une exploration guidée réunissant des PE d’aptitudes différentes, DP présent et consigne donnée.
  - Apport : Composition encadrée et qualification du guide ; absorber le rappel général de l’aptitude limitante. Acquis voisins : `n2-organisation-melanges-contraintes-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-exploration-enseignement-001`** — Choisir, pour un GP seul, la conduite autorisée face à une demande d’apprentissage technique formalisé en milieu naturel.
  - Apport : Fonction obtenue avec N4 et distinction exploration/enseignement. Acquis voisins : `n3-prerogatives-guide-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-e2-001`** — Déterminer le domaine d’enseignement d’un GP titulaire de l’initiateur, dans un cas à profondeur et milieu explicités.
  - Apport : Articulation GP + initiateur ; pas une carte supplémentaire pour le sigle E2. Acquis voisins : `n3-formation-espace-profond-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-artificiel-bapteme-001`** — Identifier les conditions de qualification et d’organisation d’un baptême confié à un GP en milieu artificiel ; valider le texte applicable avant toute réponse chiffrée.
  - Apport : Exception de fonction liée au milieu artificiel, à vérifier dans le Code du sport. Acquis voisins : `n2-organisation-guide-conduite-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-acces-dp-n5-001`** — Identifier les conditions supplémentaires permettant à un GP d’accéder au DP-N5, sans confondre niveau de plongeur et fonction automatiquement obtenue.
  - Apport : Conditions de la qualification, déjà distincte du simple intitulé N5 connu. Acquis voisins : `n3-prerogatives-fonctions-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-parcours-moniteur-001`** — Dans un cas de GP souhaitant enseigner, choisir la voie fédérale adaptée entre initiateur, stage MF1 et qualification de directeur ; préciser le statut du candidat.
  - Apport : Distinguer voies d’accès et fonctions ; fusionner avec e2 si la rédaction ne teste pas une nouvelle décision. Acquis voisins : `n3-prerogatives-guide-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-commissions-comite-001`** — Attribuer une décision technique et une décision de gestion à la commission compétente ou au comité directeur.
  - Apport : Répartition interne des missions, au-delà de fédération/club. Acquis voisins : `n2-documents-federation-role-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-echelons-001`** — Identifier l’échelon fédéral compétent pour une action de portée départementale, régionale ou nationale, à partir d’un exemple concret.
  - Apport : Organisation territoriale utile à un cadre ; une carte unique pour la structure. Acquis voisins : `n2-documents-federation-role-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-commission-activite-001`** — Orienter une demande de formation spécialisée vers la commission correspondante, avec trois commissions plausibles d’activités proches.
  - Apport : Connaissance succincte des commissions ; aucune carte par commission. Acquis voisins : `n2-documents-federation-role-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-assistance-assurance-001`** — Distinguer prestation d’assistance, indemnisation individuelle et responsabilité civile dans un cas de rapatriement ou recherche ; contrat explicitement cité.
  - Apport : La prestation d’assistance n’est pas encore interrogée. Acquis voisins : `n2-documents-assurance-rc-aia-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-obligation-moyens-001`** — Dans un incident de palanquée guidée, distinguer diligence attendue du GP et garantie d’absence d’accident ; ne pas inférer une responsabilité automatique.
  - Apport : Obligation de moyens dans une situation d’encadrement. Acquis voisins : `n3-responsabilites-civile-penale-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-causalite-001`** — Dans un cas fictif, identifier le lien entre manquement, dommage et réparation civile, sans jugement de culpabilité inventé.
  - Apport : Conditions d’engagement de responsabilité, au-delà de sa définition. Acquis voisins : `n3-responsabilites-civile-penale-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-mise-danger-001`** — Distinguer un risque créé sans dommage et un dommage causé dans l’analyse d’une infraction ; faire valider les conditions juridiques de l’exemple.
  - Apport : Une responsabilité pénale ne se réduit pas au dommage effectivement subi. Acquis voisins : `n3-responsabilites-civile-penale-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-honorabilite-001`** — Identifier l’obligation d’honorabilité attachée à la fonction de guide et la conséquence d’une absence de contrôle dans le cadre fédéral.
  - Apport : Obligation propre à l’encadrant, distincte de la licence. Acquis voisins : `n2-documents-licence-affiliation-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-signalement-001`** — Face à un témoignage de violences, sélectionner une voie de signalement adaptée au contexte et au danger, parmi des démarches plausibles.
  - Apport : Protection des pratiquants et signalement, absent du catalogue. Acquis voisins : `n3-secours-bilan-diagnostic-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-rex-001`** — Distinguer le traitement immédiat d’un incident et son retour d’expérience ultérieur, avec un exemple anonymisé.
  - Apport : Apprentissage collectif après l’incident, sans confondre REX et alerte. Acquis voisins : `n2-add-transmission-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-signature-carnet-001`** — Déterminer quelles plongées un GP peut signer dans le carnet numérique et la valeur de cette signature pour un prérequis de diplôme d’État.
  - Apport : Signature d’exploration et validation par un E3 ne sont pas équivalentes. Acquis voisins : `n2-organisation-fiche-securite-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.
- [ ] **`n4-cadre-regle-norme-001`** — Distinguer prérogative réglementaire, condition fédérale et caractéristique certifiée d’un équipement dans un cas précis.
  - Apport : Hiérarchie et champ des références ; préparer la lecture des normes sans apprendre leurs listes. Acquis voisins : `n3-materiel-partage-profondeur-001`.
  - Repères : N4-S01 p.3, 8–11, 27 ; N4-S04/S05 ; N4-S12 ; N4-S50/S55 comme exemples. Périmètre : Épreuve écrite 12. Contrôles : G01, G02.

### 2. Accueil et conduite d’une palanquée — 16 cartes

- [ ] **`n4-guide-consigne-manquante-001`** — Le sujet du DP omet une information déterminante sur le retour : choisir la question utile avant de finaliser le briefing.
  - Apport : Prendre en charge un sujet incomplet plutôt que réciter le rôle du DP. Acquis voisins : `n2-organisation-dp-parametres-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-briefing-pe-001`** — Choisir un briefing compréhensible pour un PE novice, avec reformulation d’une consigne de profondeur et de contact ; alternatives de contenu comparable.
  - Apport : Adapter le langage et vérifier la compréhension d’un plongeur encadré. Acquis voisins : `n2-competences-transversales-communication-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-attentes-parcours-001`** — Deux plongeurs autorisés veulent photographier et découvrir un relief : choisir un parcours conciliant attentes, niveau et consigne, avec données de site fournies.
  - Apport : Arbitrage pédagogique et intérêt de l’exploration, pas répétition du plafond. Acquis voisins : `n3-planification-limite-effective-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-controle-materiel-pe-001`** — Un plongeur encadré utilise un équipement inhabituel : identifier le contrôle de prise en main nécessaire avant immersion.
  - Apport : Connaissance du matériel d’autrui et autonomie de manipulation, au-delà du contrôle de débit. Acquis voisins : `n2-detendeurs-inspiration-difficile-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-regroupement-mise-eau-001`** — À partir d’une mise à l’eau et d’un courant précisés, choisir où et quand regrouper les PE avant descente.
  - Apport : Organisation de l’entrée de toute une palanquée guidée. Acquis voisins : `n3-organisation-recuperation-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-descente-support-001`** — Comparer descente sur support et descente en pleine eau pour un groupe dont l’expérience, la visibilité et les difficultés de stabilisation sont données.
  - Apport : Choix d’organisation collectif de la descente ; aucune position universelle du guide. Acquis voisins : `n2-barotraumatismes-position-descente-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-regroupement-fond-001`** — Après une descente échelonnée, choisir le contrôle collectif à terminer avant de lancer l’exploration.
  - Apport : Contrôle de cohésion et d’aisance de tous les PE avant déplacement. Acquis voisins : `n2-organisation-palanquee-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-position-guide-001`** — Dans un relief et une visibilité définis, choisir la position permettant au GP de surveiller tous les membres, sans imposer une règle universelle avant/arrière.
  - Apport : Ligne de visibilité et organisation du groupe. Acquis voisins : `n2-organisation-guide-conduite-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-trois-gaz-001`** — Calculer le temps de fond collectif restant pour trois PE avec volumes de blocs, débits et budgets de retour distincts explicités.
  - Apport : Application à un groupe de trois budgets hétérogènes ; une seule carte, pas une série de changements de chiffres. Acquis voisins : `n2-gaz-comparaison-equipiers-001 ; n3-gaz-bloc-limitant-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-gaz-observe-001`** — À partir de deux relevés à profondeur stable, recalculer le seuil de retour de la palanquée avec besoin d’assistance et pression finale imposés.
  - Apport : Combinaison mesure réelle + retour partagé, pas simple rappel d’un débit plus grand. Acquis voisins : `n3-gaz-mesure-reevaluation-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-arret-observation-001`** — Organiser l’observation d’une cavité par plusieurs PE sans perdre le contact ou bloquer l’accès ; relief et places précisés.
  - Apport : Organisation de l’observation du groupe, plutôt que comportement individuel. Acquis voisins : `n3-milieu-discretion-sonore-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-limite-surveillance-001`** — Une configuration de relief empêche le GP de surveiller un membre pendant un passage : choisir une modification du parcours préservant la cohésion.
  - Apport : Obstacle concret à la surveillance, pas une nouvelle définition de palanquée. Acquis voisins : `n2-organisation-guide-conduite-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-fin-exploration-001`** — Choisir l’ordre des actions de préparation de la remontée pour une palanquée dispersée autour d’un point d’intérêt, avec obligations connues.
  - Apport : Regroupement et répartition des contrôles avant la phase collective de désaturation. Acquis voisins : `n2-ordinateurs-collectif-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-retour-echelle-001`** — Organiser le retour à une échelle pour un groupe en surface, afin de garder le dernier PE soutenu et surveillé jusqu’à sa sortie.
  - Apport : Prise en charge du dernier plongeur de la palanquée, au-delà du gonflage individuel. Acquis voisins : `n2-noyade-flottabilite-surface-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-recuperation-pilote-001`** — À l’approche d’un bateau de récupération, choisir la coordination GP/pilote adaptée à une hélice et un état de mer explicités.
  - Apport : Partage opérationnel des rôles ; procédures du support nécessaires. Acquis voisins : `n3-organisation-recuperation-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.
- [ ] **`n4-guide-debriefing-001`** — Après un écart observé, sélectionner une remarque de débriefing factuelle expliquant une amélioration précise, parmi trois commentaires professionnels plausibles.
  - Apport : Retour pédagogique du guide, non testé dans les cartes existantes. Acquis voisins : `n2-organisation-guide-conduite-001`.
  - Repères : N4-S01 p.4–6, 15–18 ; N4-S09 p.3–13 ; N4-S20 ; N4-S26. Périmètre : Savoirs de préparation à la pratique. Contrôles : G01, G03.

### 3. Désaturation : compléments de compréhension et cas de guide — 6 cartes

- [ ] **`n4-desaturation-certification-logiciel-001`** — Distinguer certification matérielle d’un ordinateur et validation de son logiciel de calcul de désaturation, avec portée précisément vérifiée.
  - Apport : Absence de certification du logiciel explicitement demandée par le MFT, différente du modèle physiologique. Acquis voisins : `n2-add-modele-001`.
  - Repères : N4-S01 p.25, 29 ; N4-S07/S08 ; N4-S22 ; N4-S49 ; acquis N2/N3. Périmètre : Épreuve écrite 10. Contrôles : G04, G05.
- [ ] **`n4-desaturation-charge-deux-phases-001`** — Calculer la charge d’un compartiment après deux phases successives d’équilibre différent, chacune durant une période ; constantes et unités données.
  - Apport : Enchaîner deux états initiaux au lieu d’un seul calcul de demi-charge. Acquis voisins : `n3-modeles-charge-une-periode-001`.
  - Repères : N4-S01 p.25, 29 ; N4-S07/S08 ; N4-S22 ; N4-S49 ; acquis N2/N3. Périmètre : Épreuve écrite 10. Contrôles : G04, G05.
- [ ] **`n4-desaturation-decharge-transition-001`** — Calculer la charge finale après fond puis désaturation dans un exemple à périodes entières ; distinguer pression inspirée et ambiante.
  - Apport : Passage charge/décharge avec modification d’équilibre, exercice complémentaire distinct. Acquis voisins : `n3-modeles-decharge-deux-periodes-001`.
  - Repères : N4-S01 p.25, 29 ; N4-S07/S08 ; N4-S22 ; N4-S49 ; acquis N2/N3. Périmètre : Épreuve écrite 10. Contrôles : G04, G05.
- [ ] **`n4-desaturation-contraintes-trois-001`** — À partir de trois écrans explicitement définis, déterminer une position et une durée communes satisfaisant plafond continu et arrêts discrets.
  - Apport : Intersection de contraintes de types différents ; pas seulement prendre le plus grand nombre. Acquis voisins : `n2-ordinateurs-plafonds-differents-001 ; n3-ordinateur-paliers-communs-001`.
  - Repères : N4-S01 p.25, 29 ; N4-S07/S08 ; N4-S22 ; N4-S49 ; acquis N2/N3. Périmètre : Épreuve écrite 10. Contrôles : G04, G05.
- [ ] **`n4-desaturation-anticipation-arrets-001`** — Un écran projeté et un budget de gaz donné évoluent différemment pour deux plongeurs : choisir le moment de retour préservant toutes les obligations.
  - Apport : Croiser projection et budgets collectifs ; calculer indépendamment et retirer si redondant. Acquis voisins : `n3-ordinateur-tts-variation-001 ; n2-planification-premiere-limite-001`.
  - Repères : N4-S01 p.25, 29 ; N4-S07/S08 ; N4-S22 ; N4-S49 ; acquis N2/N3. Périmètre : Épreuve écrite 10. Contrôles : G04, G05.
- [ ] **`n4-desaturation-reglage-inconnu-001`** — Un PE utilise un modèle inconnu au GP : choisir une préparation permettant de comprendre les alarmes et réglages sans recopier ceux du guide.
  - Apport : Prise en main d’un équipement tiers avant encadrement ; renvoi à la notice du modèle. Acquis voisins : `n2-ordinateurs-manuel-001`.
  - Repères : N4-S01 p.25, 29 ; N4-S07/S08 ; N4-S22 ; N4-S49 ; acquis N2/N3. Périmètre : Épreuve écrite 10. Contrôles : G04, G05.

### 4. Ventilation et échanges gazeux — 14 cartes

- [ ] **`n4-ventilation-trajet-air-001`** — Sur un schéma original sans légende révélatrice, identifier le trajet de l’air entre bouche, voies conductrices et alvéoles.
  - Apport : Anatomie ventilatoire ; le trajet du gaz dissous sortant des tissus n’est pas ce trajet d’air. Acquis voisins : `n2-add-poumons-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-voies-oesophage-001`** — Sur un schéma de gorge, distinguer conduit digestif et voie aérienne par leur continuité ; contextualiser une aspiration.
  - Apport : Repérage anatomique utile aux voies aériennes, sans catalogue de sous-parties. Acquis voisins : `n3-secours-noyade-eau-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-plevre-001`** — Identifier le rôle mécanique de la plèvre dans la transmission des mouvements thoraciques aux poumons.
  - Apport : Couplage mécanique, absent du catalogue. Acquis voisins : `n2-barotraumatismes-surpression-mecanisme-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-alveole-capillaire-001`** — Sur une coupe originale, identifier l’interface où se font les échanges entre air et sang.
  - Apport : Structure anatomique de l’échange, pas nouveau rappel de ventilation alvéolaire. Acquis voisins : `n2-essoufflement-effort-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-hematoses-respiration-001`** — Distinguer renouvellement d’air, échanges pulmonaires et consommation cellulaire d’O2 dans trois situations données.
  - Apport : Séparer opérations souvent confondues dans les cours. Acquis voisins : `n2-add-poumons-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-inspiration-forces-001`** — Choisir la suite mécanique contraction du diaphragme, volume thoracique et entrée d’air au repos.
  - Apport : Mécanisme du cycle ventilatoire, distinct de son effet sur la flottabilité. Acquis voisins : `n2-flottabilite-poumon-ballast-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-expiration-effort-001`** — Distinguer expiration de repos et expiration en immersion ou à l’effort ; ne pas présenter l’expiration comme toujours passive.
  - Apport : Mécanique et contraintes, au-delà de la seule densité du gaz. Acquis voisins : `n2-essoufflement-profondeur-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-volumes-spirogramme-001`** — Sur un spirogramme original, identifier le volume courant parmi les réserves et le volume résiduel ; toutes les légendes de réponse masquées.
  - Apport : Lecture des volumes pulmonaires, sans une carte par sigle. Acquis voisins : `n2-essoufflement-co2-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-capacite-vitale-001`** — À partir de volumes pulmonaires fournis, calculer la capacité vitale en excluant le volume résiduel.
  - Apport : Composition de volumes, pas répétition du calcul alvéolaire déjà disponible. Acquis voisins : `n2-essoufflement-co2-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-volume-residuel-001`** — Déterminer quelle quantité reste après une expiration maximale à partir d’un schéma, et son absence de mesure par spirométrie simple.
  - Apport : Distinguer volume résiduel et espace mort ; fusion avec spirogramme si l’explication suffit. Acquis voisins : `n2-essoufflement-co2-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-regulation-co2-001`** — Dans une situation définie, distinguer signal de régulation ventilatoire et apport d’oxygène ; éviter toute formule absolue sur les chémorécepteurs.
  - Apport : Régulation et non simple débit nécessaire aux alvéoles. Acquis voisins : `n2-essoufflement-effort-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-cercle-vicieux-001`** — Remettre dans l’ordre un mécanisme d’essoufflement mêlant expiration insuffisante, rétention de CO2 et ventilation inefficace.
  - Apport : Causalité de l’installation du phénomène, plutôt qu’une nouvelle liste de signes. Acquis voisins : `n2-essoufflement-co2-001 ; n2-essoufflement-profondeur-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-charge-hydrostatique-001`** — Comparer deux positions où bouche et thorax ont des profondeurs différentes dans un modèle donné, et leur charge mécanique ventilatoire.
  - Apport : Lien anatomie/pression, avec convention et modèle explicites ; approfondissement utile. Acquis voisins : `n2-pression-hydrostatique-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-ventilation-humidification-001`** — Identifier ce que change l’inspiration d’air sec au détendeur sans affirmer que les voies respiratoires n’humidifient plus l’air.
  - Apport : Voies aériennes et pertes respiratoires ; contradiction de source à résoudre. Acquis voisins : `n2-froid-bilan-thermique-001`.
  - Repères : N4-S01 p.25–26 ; N4-S16 p.4–21 et planches p.25–28 ; N4-S24. Périmètre : Épreuve écrite 11 ; bases de compréhension. Contrôles : G05, G06.

### 5. Circulation, transport et shunts — 12 cartes

- [ ] **`n4-circulation-circuits-001`** — Sur un schéma original, choisir le trajet reliant cœur droit, poumons, cœur gauche et tissus.
  - Apport : Organisation des deux circulations, absente des rectos actuels. Acquis voisins : `n2-add-poumons-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-circulation-artere-veine-001`** — Distinguer artère et veine par le sens par rapport au cœur, y compris la circulation pulmonaire.
  - Apport : Éviter la confusion artère = toujours oxygénée ; une seule carte pour définition et exception. Acquis voisins : `n2-add-poumons-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-circulation-valves-001`** — Identifier le rôle anti-retour des valves cardiaques dans un schéma fonctionnel simplifié.
  - Apport : Sens de circulation dans les cavités ; pas une carte par nom de valve. Acquis voisins : `n2-add-poumons-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-circulation-systole-diastole-001`** — Associer contraction et remplissage aux phases d’un cycle simplifié sans mémoriser des durées physiologiques fixes.
  - Apport : Comprendre l’action de pompe, préalable au débit. Acquis voisins : `n2-add-poumons-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-circulation-debit-cardiaque-001`** — Calculer le débit cardiaque à partir d’une fréquence et d’un volume d’éjection fournis, unités explicites.
  - Apport : Quantification de la perfusion, pas un nouveau calcul d’air. Acquis voisins : `n2-add-tissus-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-circulation-hemoglobine-001`** — Distinguer transport de l’O2 par l’hémoglobine et fraction dissoute dans le plasma.
  - Apport : Mode de transport nécessaire à la compréhension physiologique. Acquis voisins : `n3-risques-opi-mecanisme-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-circulation-co2-transport-001`** — Identifier les principales formes de transport du CO2 entre tissus et poumons sans quotas de pourcentages.
  - Apport : Le CO2 n’est pas seulement du gaz dissous ; appui physiologique. Acquis voisins : `n2-add-poumons-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-circulation-diffusion-perfusion-001`** — Distinguer gradient de pression partielle pour diffusion et débit sanguin pour perfusion dans deux modifications expérimentales.
  - Apport : Les propriétés sont mentionnées, mais leur distinction n’est pas interrogée. Acquis voisins : `n2-add-tissus-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-circulation-bloodshift-001`** — Décrire la redistribution de volume sanguin vers le thorax lors de l’immersion, sans pourcentage universel.
  - Apport : Mécanisme de l’immersion, et non le seul liquide dans les alvéoles. Acquis voisins : `n3-risques-opi-mecanisme-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-circulation-fop-localisation-001`** — Sur une représentation simplifiée, localiser le passage potentiel d’un FOP et le distinguer d’un passage pulmonaire.
  - Apport : Support anatomique explicitement demandé par le MFT. Acquis voisins : `n2-add-bulles-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-circulation-fop-passage-001`** — Dans un cas conditionnel avec inversion du gradient fournie, expliquer comment des bulles veineuses peuvent atteindre la circulation artérielle.
  - Apport : Sens du shunt ; aucun passage permanent automatique ni risque certain. Acquis voisins : `n2-add-bulles-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.
- [ ] **`n4-circulation-shunt-pulmonaire-001`** — Distinguer shunt intracardiaque et shunt pulmonaire pour le contournement d’une filtration capillaire, sur deux schémas.
  - Apport : Deux voies anatomiques différentes ; ne pas dédoubler une carte FOP inverse. Acquis voisins : `n2-add-bulles-001`.
  - Repères : N4-S01 p.25 ; N4-S17 p.5–23 ; N4-S59 ; N4-S22. Périmètre : Épreuve écrite 10 ; bases de compréhension. Contrôles : G05, G06.

### 6. Prévention : lacunes et situations nouvelles — 15 cartes

- [ ] **`n4-prevention-oreille-chaine-001`** — Sur un schéma original, relier tympan, osselets et cochlée au trajet mécanique de l’audition.
  - Apport : Anatomie de la transmission, non du seul équilibrage ; acquis N3 à compléter. Acquis voisins : `n2-barotraumatismes-trompe-eustache-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-oreille-vestibule-001`** — Sur un schéma original, distinguer fonctions cochléaire et vestibulaire sans demander une liste complète des structures.
  - Apport : Localisation fonctionnelle fine ; l’explication actuelle mentionne seulement les deux fonctions. Acquis voisins : `n2-add-oreille-interne-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-oreille-fenetres-001`** — Identifier la séparation oreille moyenne/interne et l’effet possible d’une mise en pression forcée ; pas de règle de technique inventée.
  - Apport : Mécanisme anatomique de lésion interne, sans nouvelle carte de rhume. Acquis voisins : `n2-barotraumatismes-rhume-equilibrage-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-apnee-hyperventilation-001`** — Expliquer pourquoi l’hyperventilation peut retarder l’envie de respirer sans fournir une marge suffisante contre l’hypoxie.
  - Apport : Prévention de syncope d’apnée, distincte de la désaturation après scaphandre. Acquis voisins : `n2-add-apnee-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-apnee-remontee-001`** — À partir d’un modèle de pression partielle fourni, expliquer la baisse de disponibilité d’O2 à la remontée d’une apnée.
  - Apport : Évolution de pression en apnée avec consommation, pas Dalton appliqué à une fraction constante. Acquis voisins : `n2-narcose-dalton-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-apnee-lmc-001`** — Distinguer perte de contrôle moteur et perte de conscience à partir d’observations, sans reprendre la définition erronée de samba du cours.
  - Apport : Reconnaissance d’un événement propre à l’apnée. Acquis voisins : `n3-secours-bilan-diagnostic-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-apnee-surveillance-001`** — Choisir une organisation de surveillance directe et de récupération adaptée à un exercice d’apnée avec profondeur définie.
  - Apport : Organisation avant événement, différente de la répartition des secours après accident. Acquis voisins : `n3-secours-repartition-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-apnee-sortie-001`** — Après une fin d’apnée apparemment réussie, identifier pourquoi la surveillance doit se poursuivre au retour en surface.
  - Apport : Événement hypoxique après émersion ; valider protocole et durée avant rédaction. Acquis voisins : `n3-secours-bilan-diagnostic-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-apnee-echauffement-001`** — Choisir une progression d’échauffement et de récupération sans présenter des séries intensives comme sûres par définition.
  - Apport : Importance de l’échauffement et récupération, explicitement visée par le MFT. Acquis voisins : `n2-competences-transversales-renoncer-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-froid-vasoconstriction-001`** — Distinguer diminution des pertes cutanées et production de chaleur dans deux réponses de thermorégulation.
  - Apport : La production par frissons est connue ; rôle distinct de la vasoconstriction. Acquis voisins : `n2-froid-fatigue-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-thermodifferentielle-001`** — Dans un cas de transition thermique, distinguer syncope thermo-différentielle et refroidissement progressif ; mécanisme médical à contrôler.
  - Apport : Deux phénomènes différents ; ne pas généraliser le vieux cours sur l’hydrocution. Acquis voisins : `n2-froid-bilan-thermique-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-diurese-immersion-001`** — Relier redistribution sanguine centrale et diurèse d’immersion sans expliquer l’urine par une tentative de réchauffement.
  - Apport : Mécanisme de déshydratation demandé au MFT, absent du catalogue. Acquis voisins : `n2-froid-bilan-thermique-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-diurese-froid-001`** — Distinguer l’effet circulatoire du froid et les autres pertes hydriques dans un exemple d’immersion froide.
  - Apport : Contribution du froid à la diurèse ; fusion avec diurese-immersion si aucun mécanisme distinct vérifié. Acquis voisins : `n2-froid-interactions-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-narcose-stades-001`** — Dans deux observations de comportement, distinguer premiers signes et altération majeure imposant une prise en charge du groupe ; ne pas exiger de diagnostic certain.
  - Apport : Différenciation explicitement visée au MFT ; fusion si la nouvelle situation ne teste que l’assistance déjà connue. Acquis voisins : `n2-narcose-capacites-001 ; n2-narcose-equipier-001`.
  - Repères : N4-S01 p.26 ; N4-S15 p.5–19 ; N4-S18 p.5–14 ; N4-S14 p.5–16 ; N4-S21/S23 ; N4-S03. Périmètre : Épreuve écrite 11 ; acquis d’accidentologie réutilisés. Contrôles : G05, G06, G07.
- [ ] **`n4-prevention-co2-narcose-001`** — Relier rétention de CO2 et risque de narcose dans une plongée avec effort ; distinguer ce facteur du seul changement de fraction d’azote.
  - Apport : Rôle facilitateur du CO2 explicitement demandé au MFT, non interrogé dans les acquis. Acquis voisins : `n2-narcose-conditions-001 ; n2-essoufflement-effort-001`.
  - Repères : N4-S01 p.26 ; N4-S23 ; N4-S24. Périmètre : Épreuve écrite 11. Contrôles : G05, G06.

### 7. Fonctionnement du matériel et lecture de schémas — 36 cartes

- [ ] **`n4-materiel-compresseur-cycle-001`** — Sur un schéma original, identifier admission, compression et refoulement d’un étage à piston.
  - Apport : Fonctionnement mécanique, au-delà d’augmenter la pression. Acquis voisins : `n2-gonflage-blocs-filtration-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-compresseur-etages-001`** — Distinguer compression progressive et simple stockage sur un schéma multi-étages ; éviter le calcul de performance non requis.
  - Apport : Fonction de chaque étage de la machine. Acquis voisins : `n2-gonflage-blocs-tampons-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-compresseur-refroidissement-001`** — Identifier le rôle du refroidisseur entre deux étages et les conséquences thermiques d’une ventilation insuffisante.
  - Apport : Gestion thermique de la station, pas la chaleur d’un bloc isolé. Acquis voisins : `n2-gonflage-blocs-chaleur-chocs-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-compresseur-condensats-001`** — Distinguer séparateur de condensats et cartouche de filtration sur un circuit donné.
  - Apport : Étapes de traitement et séparation de phases, pas liste générale des contaminants. Acquis voisins : `n2-gonflage-blocs-filtration-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-compresseur-soupape-001`** — Expliquer la fonction d’une soupape de sécurité par opposition à un clapet de refoulement.
  - Apport : Protection de la station et sens du flux. Acquis voisins : `n2-gonflage-blocs-pression-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-compresseur-panne-001`** — Sur un schéma de station avec observations précises, identifier la famille de défaut compatible avec une montée de pression anormale.
  - Apport : Reconnaissance de panne sans réparation réservée aux techniciens. Acquis voisins : `n2-gonflage-blocs-filtration-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-compresseur-verification-001`** — À partir du journal de station et de ses échéances, choisir le contrôle bloquant avant gonflage ; valeurs et notice fournies.
  - Apport : Suivi de station, différent du suivi réglementaire du bloc. Acquis voisins : `n2-gonflage-blocs-habilitation-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-compresseur-temperature-calcul-001`** — Comparer pression à chaud et après refroidissement dans un bloc fermé, avec gaz idéal, températures en kelvins et pressions absolues.
  - Apport : Exercice de compréhension thermique ; approfondissement, aucune consigne de sur-gonflage. Acquis voisins : `n2-gonflage-blocs-chaleur-chocs-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-robinet-schema-001`** — Sur un robinet simplifié, identifier le passage de gaz, le siège et le clapet en position ouverte.
  - Apport : Fonctionnement interne du robinet, et non raccord de détendeur. Acquis voisins : `n2-detendeurs-fuite-montage-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-robinet-etancheite-001`** — Distinguer étanchéité de conservation et étanchéité autour de la tige dans deux emplacements de fuite décrits.
  - Apport : Deux zones internes distinctes ; modèle explicite. Acquis voisins : `n2-detendeurs-fuite-montage-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-robinet-volume-piege-001`** — À partir d’un montage double sortie explicitement communicant ou isolable, déterminer quelle partie reste sous pression après fermeture.
  - Apport : Lecture du chemin de gaz et volume piégé ; sans protocole universel de fermeture. Acquis voisins : `n2-gonflage-blocs-bi-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-siege-clapet-001`** — Sur une coupe, distinguer surface fixe d’étanchéité et pièce mobile fermant le passage.
  - Apport : Repérage requis pour commenter un éclaté. Acquis voisins : `n2-detendeurs-cycle-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-amont-aval-001`** — Déterminer si la différence de pression ouvre ou ferme un clapet représenté, puis qualifier amont/aval dans ce montage.
  - Apport : Direction des forces sur le clapet, pas le simple cycle MP. Acquis voisins : `n2-detendeurs-cycle-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-piston-simple-forces-001`** — Sur un premier étage à piston simple donné, identifier les forces ouvrantes et fermantes lorsque le débit est nul.
  - Apport : Analyse du piston non compensé, distincte du schéma générique à membrane. Acquis voisins : `n2-detendeurs-cycle-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-piston-simple-hp-001`** — Comparer deux pressions de bloc dans le même montage non compensé et déterminer l’effet sur l’équilibre, surfaces et sens des forces donnés.
  - Apport : Comprendre le mécanisme de dépendance à HP ; aucun sens universel sans schéma. Acquis voisins : `n2-detendeurs-compensation-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-piston-equilibre-schema-001`** — Sur une coupe originale de piston équilibré, identifier pourquoi la HP ne produit pas la même force parasite qu’en montage simple.
  - Apport : Mécanisme de compensation, au-delà de son intérêt. Acquis voisins : `n2-detendeurs-compensation-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-piston-chemin-gaz-001`** — Identifier le chemin HP → MP dans un piston représenté, indépendamment du circuit de pression ambiante.
  - Apport : Lecture d’éclaté et séparation des circuits. Acquis voisins : `n2-detendeurs-pressions-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-membrane-forces-001`** — Sur une membrane compensée, identifier l’action de l’ambiante, du ressort et de la MP dans le mouvement du clapet.
  - Apport : Bilan de forces sur un montage identifié. Acquis voisins : `n2-detendeurs-cycle-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-membrane-isolation-001`** — Distinguer protection du mécanisme par membrane et kit d’isolation environnementale additionnel dans une notice.
  - Apport : Ne pas déduire une chambre entièrement sèche de la seule membrane. Acquis voisins : `n2-detendeurs-membrane-isolation-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-compensation-ambiante-001`** — Distinguer compensation de HP et adaptation à la pression ambiante en analysant deux chambres du premier étage.
  - Apport : Deux fonctions souvent confondues ; pas nouveau calcul de MP. Acquis voisins : `n2-detendeurs-relative-absolue-001 ; n2-detendeurs-compensation-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-surcompensation-principe-001`** — À partir d’une courbe fournie de MP relative à l’ambiante, distinguer compensé et surcompensé selon la profondeur.
  - Apport : Surcompensation non encore interrogée ; pas d’équation requise. Acquis voisins : `n2-detendeurs-compensation-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-second-aval-forces-001`** — Sur un second étage à clapet aval, identifier ce qui ouvre et ferme le passage lors d’une inspiration.
  - Apport : Forces du montage détaillé ; pas nouvelle carte sur membrane/levier seuls. Acquis voisins : `n2-detendeurs-inspiration-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-second-compense-001`** — Expliquer le rôle de la chambre d’équilibrage d’un second étage dans l’effort d’ouverture.
  - Apport : Compensation du second étage, différente de celle du premier. Acquis voisins : `n2-detendeurs-compensation-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-second-mp-variation-001`** — Dans un montage défini, comparer l’effet d’une MP différente sur l’ouverture d’un second étage simple et compensé.
  - Apport : Tester le bénéfice mécanique par une variation, sans chiffre exigible. Acquis voisins : `n2-detendeurs-inspiration-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-reglage-effort-001`** — Distinguer commande d’effort initial d’ouverture et commande Venturi dans la notice d’un second étage donné.
  - Apport : Deux réglages aux fonctions distinctes. Acquis voisins : `n2-detendeurs-debit-continu-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-venturi-position-001`** — Choisir la position pré-plongée/plongée d’une commande d’après la notice et la situation (embout hors bouche ou respiration).
  - Apport : Usage d’un réglage spécifique au modèle ; pas label universel. Acquis voisins : `n2-detendeurs-debit-continu-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-vortex-001`** — Distinguer mise en rotation du flux et augmentation de pression dans un schéma de second étage ; vérifier la description fabricant.
  - Apport : Amélioration citée dans le MFT, absente du catalogue. Acquis voisins : `n2-detendeurs-debit-continu-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-givrage-interne-externe-001`** — À partir de l’endroit où se forme la glace, distinguer blocage interne et glace dans une chambre exposée à l’eau.
  - Apport : Deux localisations et mécanismes ; ni membrane ni DIN ne suffisent à conclure. Acquis voisins : `n2-detendeurs-eau-froide-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-givrage-debit-001`** — Comparer deux usages dans des conditions données de température et débit, pour relier détente et refroidissement.
  - Apport : Débit au détendeur en immersion, pas seulement vidange du robinet à l’air libre. Acquis voisins : `n2-gonflage-blocs-vidange-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-givrage-configuration-001`** — Identifier la configuration de détendeur autorisée par une notice eau froide pour deux utilisateurs ; conditions réelles explicites.
  - Apport : Configuration eau froide plutôt que simple plafond en eau tempérée ; fusion si la notice ne fournit pas une distinction exploitable. Acquis voisins : `n3-materiel-partage-profondeur-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-manometre-bourdon-001`** — Sur un schéma original, relier déformation du tube de Bourdon et déplacement de l’aiguille.
  - Apport : Principe du manomètre mécanique demandé par le MFT. Acquis voisins : `n2-ordinateurs-sonde-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-manometre-lecture-dynamique-001`** — Un montage a un passage de gaz restreint : expliquer pourquoi la pression statique seule peut masquer une chute de pression à l’inspiration.
  - Apport : Lecture dynamique du circuit, différente de la seule vérification de respiration. Acquis voisins : `n2-detendeurs-inspiration-difficile-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-gilet-enveloppes-001`** — Comparer répartition d’enveloppe dorsale et enveloppante pour une situation de portage ou de surface définie.
  - Apport : Choix d’architecture ; aucune garantie universelle de face hors de l’eau. Acquis voisins : `n2-flottabilite-gilet-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-inflateur-schema-001`** — Sur une coupe originale, distinguer commande d’admission MP et commande de vidange de l’inflateur.
  - Apport : Fonctionnement des soupapes et chemin de gaz, absent des rectos. Acquis voisins : `n2-flottabilite-gilet-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-ordinateur-sonde-limites-001`** — Distinguer pression transmise, stock de gaz et estimation de temps selon un modèle avec sonde et des hypothèses de consommation données.
  - Apport : Une sonde ne transforme pas une estimation en marge garantie. Acquis voisins : `n2-ordinateurs-sonde-001 ; n2-ordinateurs-ndl-air-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.
- [ ] **`n4-materiel-compatibilite-flexible-001`** — Dans une substitution de flexible de MP, vérifier les caractéristiques et la compatibilité certifiée de l’ensemble, à partir d’une notice.
  - Apport : Remplacement conforme et non simple repérage d’un dommage ; contrôler le sens de « identique » du MFT. Acquis voisins : `n2-lecture-pannes-flexible-001`.
  - Repères : N4-S01 p.27–29 ; N4-S11 p.4–35 ; N4-S28 à S44 (fiches complètes) ; notices fabricants à compléter. Périmètre : Épreuve orale 13. Contrôles : G08, G09.

### 8. Matelotage, repérage et rôle d’équipier — 17 cartes

- [ ] **`n4-matelotage-chaise-001`** — Choisir le nœud réalisant une boucle fixe dans une situation de fixation explicitée ; représentation originale, sans label révélateur.
  - Apport : Nœud usuel du MFT, absent du catalogue. Acquis voisins : `—`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-cabestan-001`** — Identifier le montage d’un cabestan autour d’un support à partir d’un dessin et d’un usage précis.
  - Apport : Reconnaissance du montage ; le nom du support ne suffit pas à donner la réponse. Acquis voisins : `—`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-arret-001`** — Identifier un nœud d’arrêt empêchant un cordage de passer dans un orifice, parmi trois dessins de nœuds usuels.
  - Apport : Fonction d’arrêt et lecture de schéma. Acquis voisins : `—`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-taquet-001`** — Choisir un montage correct de fixation sur taquet dans un schéma original de cordage sous tension.
  - Apport : Lecture théorique du geste, distincte de sa réalisation pratique. Acquis voisins : `—`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-ragage-001`** — Identifier le risque d’une amarre frottant sur une arête et la protection adaptée dans un dispositif donné.
  - Apport : Risque de cordage sous charge, matériel et contexte distincts. Acquis voisins : `n2-lecture-pannes-flexible-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-ligne-mouillage-001`** — Sur un schéma, identifier rôle respectif de l’ancre, de la chaîne et de la ligne souple dans la tenue du mouillage.
  - Apport : Fonction mécanique du mouillage, différente de son impact écologique. Acquis voisins : `n3-milieu-posidonie-mouillage-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-mouillage-maree-001`** — Déterminer la hauteur d’eau utilisable à partir d’une sonde cartographique et d’une hauteur de marée fournies, convention précisée.
  - Apport : Lecture nautique : profondeur du site et marée, pas calcul de pression. Acquis voisins : `n2-pression-hydrostatique-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-parachute-ancre-001`** — Distinguer relevage de l’ancre et signalisation des plongeurs en analysant deux montages, avec rôle et procédure du pilote.
  - Apport : Deux parachutes aux fonctions différentes ; procédure et charge à contrôler. Acquis voisins : `n3-orientation-trafic-surface-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-pendeur-ligne-vie-001`** — Choisir entre appui vertical d’immersion/palier et ligne de maintien en surface dans deux situations de courant définies.
  - Apport : Installation de supports selon la phase, non obligation du bloc de secours. Acquis voisins : `n2-organisation-bloc-secours-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-bloc-secours-support-001`** — Choisir une implantation de bloc de secours accessible et sécurisée dans une organisation décrite par le DP ; aucun placement universel.
  - Apport : Mise en œuvre d’un moyen déjà exigé réglementairement. Acquis voisins : `n2-organisation-bloc-secours-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-rappel-reception-001`** — Après un signal de rappel convenu, déterminer la coordination des palanquées et de la sécurité surface sans supprimer leurs paliers.
  - Apport : Application du rappel et respect des obligations, non simple présence du dispositif. Acquis voisins : `n2-organisation-rappel-bateau-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-amer-alignements-001`** — Déterminer la position d’un site à partir de deux alignements d’amers sur une carte originale simplifiée.
  - Apport : Croisement de deux lignes de position, au-delà du maintien d’un alignement sous l’eau. Acquis voisins : `n2-competences-transversales-reperes-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-gps-sonar-001`** — Distinguer position géographique et détection du relief sous le bateau pour retrouver une épave, avec observations données.
  - Apport : Rôles de deux instruments de repérage nautique. Acquis voisins : `n3-orientation-relief-sortie-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-carte-symboles-001`** — Interpréter un extrait original avec roche, profondeur et zone réglementée, selon la légende fournie et un site fictif.
  - Apport : Lecture de carte avant consultation du règlement local. Acquis voisins : `n3-organisation-regles-locales-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-distance-carte-001`** — Mesurer une distance sur une carte simplifiée avec échelle explicite et convertir mille nautique/kilomètre.
  - Apport : Opération de navigation distincte des horaires de plongée. Acquis voisins : `n3-organisation-fenetre-courant-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-appareillage-role-001`** — Choisir l’ordre de coordination avec le pilote lors d’une libération d’amarres, situation de vent et rôles donnés.
  - Apport : Participation aux manœuvres portuaires sans se substituer au pilote. Acquis voisins : `n3-organisation-rotation-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.
- [ ] **`n4-matelotage-recuperation-courant-001`** — Sur un plan du bateau et du courant, choisir le support de récupération et le positionnement permettant au groupe d’atteindre l’accès prévu.
  - Apport : Lecture d’un dispositif nautique, distincte du seul briefing de sortie. Acquis voisins : `n3-organisation-recuperation-001`.
  - Repères : N4-S01 p.20 ; N4-S58 p.6–23, 25–34 ; ANFR CRR déjà dans sources/n3. Périmètre : Savoirs de préparation à la pratique. Contrôles : G10.

### 9. Découverte et protection du milieu — 7 cartes

- [ ] **`n4-environnement-fixe-mobile-001`** — À partir de deux organismes identifiés, distinguer organisme fixé et mobile pour expliquer leur observation sans déplacement ni contact.
  - Apport : Notion transversale de mode de vie ; éviter la taxonomie exhaustive. Acquis voisins : `n3-milieu-spirographe-001`.
  - Repères : N4-S01 p.6, 17 ; N4-S10 ; DORIS et chartes mer/eau douce à acquérir pour les taxons choisis. Périmètre : Savoirs de préparation à la pratique ; approfondissements contextualisés. Contrôles : G11.
- [ ] **`n4-environnement-eponge-ascidie-001`** — Identifier éponge ou ascidie sur un schéma original en reliant les orifices visibles à une circulation d’eau filtrante.
  - Apport : Deux groupes filtrants non interrogés ; espèces et caractères à valider DORIS. Acquis voisins : `n3-milieu-spirographe-001`.
  - Repères : N4-S01 p.6, 17 ; N4-S10 ; DORIS et chartes mer/eau douce à acquérir pour les taxons choisis. Périmètre : Savoirs de préparation à la pratique ; approfondissements contextualisés. Contrôles : G11.
- [ ] **`n4-environnement-corail-gorgone-001`** — Identifier les polypes d’une gorgone méditerranéenne comme animaux, et expliquer leur alimentation sans les assimiler à une plante.
  - Apport : Confusion animal/végétal appliquée à un autre groupe ; mécanisme distinct. Acquis voisins : `n3-milieu-posidonie-nature-001`.
  - Repères : N4-S01 p.6, 17 ; N4-S10 ; DORIS et chartes mer/eau douce à acquérir pour les taxons choisis. Périmètre : Savoirs de préparation à la pratique ; approfondissements contextualisés. Contrôles : G11.
- [ ] **`n4-environnement-herbier-habitat-001`** — Relier un herbier de posidonie à sa fonction d’habitat et de nurserie dans un cas d’observation.
  - Apport : Rôle écologique, pas répétition de sa classification ou de l’arrachage. Acquis voisins : `n3-milieu-posidonie-nature-001 ; n3-milieu-posidonie-mouillage-001`.
  - Repères : N4-S01 p.6, 17 ; N4-S10 ; DORIS et chartes mer/eau douce à acquérir pour les taxons choisis. Périmètre : Savoirs de préparation à la pratique ; approfondissements contextualisés. Contrôles : G11.
- [ ] **`n4-environnement-poulpe-comportement-001`** — Expliquer une observation de camouflage ou de refuge d’un poulpe commun avec contexte, sans prêter une intention certaine à l’animal.
  - Apport : Commentaire naturaliste du guide ; fait et espèce à vérifier. Acquis voisins : `n3-milieu-discretion-sonore-001`.
  - Repères : N4-S01 p.6, 17 ; N4-S10 ; DORIS et chartes mer/eau douce à acquérir pour les taxons choisis. Périmètre : Savoirs de préparation à la pratique ; approfondissements contextualisés. Contrôles : G11.
- [ ] **`n4-environnement-eau-douce-habitat-001`** — Lire un milieu d’eau douce (substrat, végétation, température données) pour choisir une observation possible d’un taxon identifié.
  - Apport : Ne pas réduire l’environnement N4 à la mer ; espèce et saison à vérifier. Acquis voisins : `n2-documents-zones-reglementees-001`.
  - Repères : N4-S01 p.6, 17 ; N4-S10 ; DORIS et chartes mer/eau douce à acquérir pour les taxons choisis. Périmètre : Savoirs de préparation à la pratique ; approfondissements contextualisés. Contrôles : G11.
- [ ] **`n4-environnement-groupe-approche-001`** — Organiser l’approche de plusieurs PE autour d’une faune fixée, de façon à maintenir leur stabilisation et limiter bulles et contacts.
  - Apport : Coordination du groupe, différente des comportements individuels déjà connus. Acquis voisins : `n3-milieu-eclairage-001 ; n3-milieu-sediments-001`.
  - Repères : N4-S01 p.6, 17 ; N4-S10 ; DORIS et chartes mer/eau douce à acquérir pour les taxons choisis. Périmètre : Savoirs de préparation à la pratique ; approfondissements contextualisés. Contrôles : G11.

## Objectifs absorbés : aucune carte supplémentaire

- **guide-rythme-groupe** → `n2-essoufflement-courant-001` : Même adaptation d’effort et de récupération ; le rôle de GP ne suffit pas à créer un nouvel objectif.
- **guide-suivi-apres-sortie** → `n2-add-retard-001 ; n2-add-transmission-001` : Les consignes de suivi peuvent compléter le corrigé ou le briefing ; pas de nouveau mécanisme.
- **desaturation-sursaturation-critique** → `n3-modeles-etats-001 ; n3-modeles-droite-limite-001` : États et comparaison à la limite sont déjà interrogés ; expliciter leur articulation dans les acquis.
- **desaturation-profils-guide** → `n2-ordinateurs-differences-001 ; n3-planification-reprise-001` : Historiques et reprise sont déjà interrogés ; le changement d’acteur seul ne justifie pas une carte.
- **desaturation-acclimatation-limites** → `n3-modeles-acclimatation-001` : Le corrigé expose déjà les limites de l’adaptation physiologique ; ne pas dupliquer.
- **materiel-surcompensation-limite** → `n4-materiel-surcompensation-principe-001` : Intégrer la distinction HP/profondeur dans la carte prévue, sans carte inverse.
- **materiel-venturi-schema** → `n2-detendeurs-debit-continu-001` : Le corrigé décrit déjà dépression, membrane et maintien du clapet ; adapter l’illustration à l’ID existant si utile.
- **materiel-ordinateur-capteur** → `n2-ordinateurs-salinite-001 ; n2-ordinateurs-profil-001` : La conversion pression/profondeur et l’historique sont déjà testés ; pas nouvelle chaîne de rappel.
- **environnement-briefing-fragilite** → `n3-milieu-posidonie-mouillage-001 ; n2-milieu-grande-nacre-protection-001` : Une reformulation de briefing ne constitue pas une nouvelle interdiction ; conserver les acquis.

## Clôture attendue

Pour chaque objectif : ID réel ou fusion tracée, apport distinct, sources précises et
date, résultat recalculé si nécessaire, chaque choix plausible et une seule clé,
explication claire, verdict factuel et pédagogique. Mettre à jour la matrice et les
comptages après chaque lot, puis faire une revue de couverture à partir du MFT et
des PDF pertinents. Vérifier que les précisions des explications ne cachent pas un
objectif obligatoire jamais interrogé.

`make check`, build et inspection des rectos/versos terminent la vérification technique.
Les tests ne prouvent ni la véracité ni l’exhaustivité pédagogique. Aucun déplacement
de carte, réglage Anki ou suppression de note n’est nécessaire pour cette extension.
