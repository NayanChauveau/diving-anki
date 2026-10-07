# Recoupement des PDF N3 avec le catalogue — 7 octobre 2026

> État avant implémentation. Les [22 compléments du 7 octobre](COMPLEMENTS_PDF_2026-10-07.md)
> traitent les objectifs théoriques prioritaires ci-dessous ; les limites pratiques et
> extensions facultatives restent distinguées dans ce bilan.

## Conclusion

**Le socle est solide, mais la couverture des PDF n’est pas complète.** La clôture du
6 octobre valide la réalisation du plan retenu, pas l’exhaustivité des enseignements
présents dans les sources. Les lacunes se concentrent sur des détails du secours,
l’environnement et quelques points explicitement cités dans le MFT.

Le périmètre examiné est **N2 comme base (308 cartes) + N3 comme complément (118)**,
soit 426 identités. Les 204 cartes partagées sont conservées dans N2 ; les tags N3 ne
remplacent pas la révision de cette base. Une notion présente dans N2 n’est pas à
recopier dans N3. Aucun contenu, ID, modèle, paquet ou réglage Anki n’a été modifié
pendant cet audit.

## Méthode et limites

- Recoupement à partir des **18 PDF locaux de `sources/n3/`**, inventoriés dans
  [SOURCES_N3.json](../SOURCES_N3.json). Empreintes et nombres de pages contrôlés.
- Extraction fraîche du texte, comparaison des questions, réponses et explications
  des YAML ; contrôle visuel des pages MFT 11, 14, 15 et RIFAP 26 pour les tableaux.
- Pagination ci-dessous : **pages physiques du PDF, à partir de 1**.
- Le MFT définit les compétences attendues ; le RIFAP précise le secours. Les cours
  secondaires servent à chercher des enseignements oubliés, sans faire autorité sur
  les procédures actuelles. Les notices restent propres à leur modèle.
- Les référentiels PSC/PSE sont consultés pour les gestes auxquels renvoie le RIFAP :
  leurs 50 et 389 pages ne sont pas un programme N3 à transformer intégralement en cartes.
- « Couvert » signifie qu’un objectif théorique est effectivement interrogé ; une
  mention dans une explication est distinguée d’un objectif travaillé. Cela ne valide
  pas les gestes en pratique, ni une certification. Cet audit n’est pas une nouvelle
  revue exhaustive de véracité de chaque distracteur.
- Recherche sémantique : l’absence du mot exact ne suffit pas à constater une lacune.
  Exemple : le cutis marmorata est déjà traité sous la description de marbrures.

## Référentiel MFT : rapprochement avec les cartes

| PDF / pages | Enseignement | Cartes ou fichiers existants | Bilan |
| --- | --- | --- | --- |
| S01 p.3 | Autonomie avec/sans DP, effectifs et profondeur limitante | `n3-prerogatives-dp-001`, `n3-prerogatives-effectif-001`, `n3-prerogatives-aptitude-limitante-001` | Couvert |
| S01 p.3 | Certification/exercice, mineurs, qualifications isolées | `n3-prerogatives-age-001`, `n3-prerogatives-mineur-001`, `n3-prerogatives-qualifications-001` | Couvert pour N3 ; conditions d’accès propres aux qualifications isolées peu travaillées |
| S01 p.3–4 | Accès N3, RIFAP, enseignement dans 0–40 / 40–60 m | `n3-formation-prerequis-001`, `n3-formation-rifap-001`, `n3-formation-espace-profond-001` ; CACI/licence dans N2 | Couvert dans les grandes lignes ; délai et modalités de certification incomplets |
| S01 p.5–7,11 | Équipement, immersion, ventilation, stabilisation | N2 `05-flottabilite.yaml`, `07-barotraumatismes.yaml`, `16-detendeurs.yaml` ; N3 `11-materiel.yaml` | Base théorique couverte ; maîtrise pratique à entraîner |
| S01 p.8,13 | Budget, consommations, retour ordinaire et incident | N2 `06-gaz-autonomie.yaml` ; N3 `03-planification.yaml`, `04-gaz.yaml` | Couvert, avec opérations et contraintes variées ; pas besoin de doubler les exercices |
| S01 p.8,13 | Choix collectif, expérience et reprise progressive | `n3-planification-limite-effective-001`, `n3-planification-reprise-001`, `n3-planification-dtr-collective-001` | Couvert |
| S01 p.9,13 | Cohésion, communication et obligations différentes | N2 `17-competences-transversales.yaml`, `13-ordinateurs.yaml` ; N3 `06-ordinateurs.yaml` | Couvert |
| S01 p.9,13 | Orientation naturelle/instrumentale, itinéraires variés | N2 caps/repères ; N3 `12-orientation-milieu.yaml` | Couvert en théorie ; parcours réels à pratiquer |
| S01 p.9 | Profils à risques, yoyo, répétitives | `n2-add-yoyo-001`, `n2-tables-deux-plongees-001`, `n2-ordinateurs-profil-001` | Partiel : yoyo et limites des répétitives travaillés ; profil inverse non interrogé comme objectif distinct. Ne pas transformer la prévention en interdiction absolue |
| S01 p.9 | Arrêt et tour d’horizon de sécurité à 3 m | `n3-orientation-trafic-surface-001` traite le trafic ; aucune carte explicite sur ce repère | Partiel : complément distinct utile |
| S01 p.10,13,16 | Détection et assistance, gaz, remontée, surface | N3 `09-assistance.yaml` + assistance/essoufflement/barotraumatismes N2 | Raisonnements couverts ; gestes, nage capelée et validation finale restent pratiques |
| S01 p.11 | Risques accrus en profondeur, froid, narcose, essoufflement | N2 `08-essoufflement.yaml`, `09-froid.yaml`, `10-narcose.yaml` ; N3 `08-risques.yaml` | Couvert |
| S01 p.11 | ADD : mécanismes, symptômes, prévention et secours | N2 `11-add.yaml`, `14-remontees-anormales.yaml` ; N3 modèles et secours | Couvert pour les principaux objectifs ; réserve sur acclimatation ci-dessous |
| S01 p.11 | Manifestations cutanées rares : cutis marmorata | `n2-add-peau-001` interroge les marbrures du tronc et leur signalement | Notion couverte ; enrichir éventuellement le vocabulaire du corrigé, sans nouvelle carte |
| S01 p.11 | Acclimatation à la désaturation | La reprise progressive de `n3-planification-reprise-001` ne traite pas ce mécanisme | Non couvert explicitement ; clarification scientifique nécessaire avant rédaction |
| S01 p.12 | Sans DP : site, météo, bateau, rotations, veille, secours | N3 `02-organisation.yaml`, `n3-organisation-exploitant-001` ; équipements/fiche/Alpha N2 | Couvert dans les principales décisions ; fenêtre de courant travaillée, pas de seuil météo universel |
| S01 p.12 | Responsabilités civile/pénale, décisions collectives | `n3-responsabilites-civile-penale-001`, `n3-prerogatives-fonctions-001` | Couvert |
| S01 p.14 | Stabilisation, sédiments, éclairage, absence de prélèvement | `n3-milieu-sediments-001`, `n3-milieu-eclairage-001`, `n2-documents-prelevements-observation-001` | Couvert |
| S01 p.14 | Refus du nourrissage, nuisances sonores et discrétion | Aucune question dédiée ; l’éclairage ne couvre pas ces décisions | Non couvert explicitement |
| S01 p.14 | Nommer/décrire espèces fréquentes ; Charte internationale | Posidonie et anémone ; Charte citée dans le corrigé N2 sur le prélèvement | Partiel : deux exemples ne suffisent pas à une reconnaissance variée du milieu |
| S01 p.15 | Pressions, Boyle, Archimède, Dalton | Physique N2 + gaz/risques/matériel N3 | Couvert ; formules avec hypothèses et exercices directs/inverses |
| S01 p.15 | Haldane/Bühlmann, M-values, GF, RGBM et successives | N3 `05-modeles.yaml` ; tables/ordinateurs N2 | Couvert au niveau des principes et applications retenus, sans transformer un modèle en mesure du corps |

## RIFAP et renvois PSC/PSE

| PDF / pages | Enseignement | Couverture actuelle | Bilan |
| --- | --- | --- | --- |
| S04 p.10–18 | Reconnaître, rassurer, récupérer et mettre en sécurité | Communication/assistance N2 ; N3 assistance et surface | Principes couverts ; remorquage, déséquipement et hissage nécessitent surtout pratique |
| S04 p.19–21 | Comptage, autres équipiers, fiche, coordination | `n3-secours-repartition-001`, `n2-add-equipiers-001`, `n2-add-transmission-001`, fiche d’évacuation N2 | Couvert ; préparation matérielle détaillée d’une évacuation héliportée non travaillée |
| S04 p.23–26 ; S14 p.36–41 | Bilan, respiration anormale, PLS, traumatisme, surveillance | `n3-secours-bilan-diagnostic-001`, `n3-secours-gasp-001`, `n3-secours-inconscient-respire-001`, `n3-secours-traumatisme-001`, `n3-secours-aggravation-001` | Grandes branches couvertes ; gestes détaillés non tous interrogés |
| S04 p.26 ; S13 p.273–274 | Noyade : ventilation initiale, réanimation hors de l’eau, pas de tentative de vider les poumons | `n3-secours-noyade-eau-001` teste seulement l’erreur « vider les poumons » | Partiel : priorité des insufflations initiales manquante ; vérifier la fiche technique complète avant fixer une séquence chiffrée |
| S04 p.26 ; S14 p.26–33 | Compressions et insufflations : repères de RCP | Arrêt cardiaque identifié, mais paramètres techniques pas interrogés | Partiel : fréquence, profondeur, alternance chez l’adulte à travailler selon contexte ; pas un apprentissage intégral PSC |
| S04 p.24 ; S14 p.16–19 | Hémorragie et compression, adaptation si échec/impossibilité | `n3-secours-hemorragie-001` ; indication du garrot seulement dans le corrigé | Partiel : décision devant échec/impossibilité mérite un cas distinct |
| S04 p.25 | Plaies, brûlures, blessures avec/sans envenimation | Traumatisme et prévention du contact avec anémone | Partiel : prévention du contact ne couvre pas la prise en charge d’une blessure ; choisir quelques cas locaux utiles |
| S04 p.26 | Couverture isothermique, corps et tête | `n2-froid-sortie-001` + matériel de secours N2 | Principe couvert : ne pas ajouter une carte paraphrase uniquement pour le nom de la couverture |
| S04 p.27–29 ; renvois S13 | Oxygène : dispositif, débit, continuité, autonomie, montage et manipulation | ADD/oxygène N2 ; `n3-secours-inhalation-insufflation-001`, trois exercices d’autonomie, corps gras | Décisions et stock couverts ; contrôle du montage, réservoir et efficacité de ventilation peu travaillés |
| S04 p.28–29 | Hydratation/exclusions, pas de recompression thérapeutique | `n2-add-eau-001`, `n2-add-remontee-001` | Couvert ; conserver les exclusions et le contexte |
| S04 p.30–32 ; S18 p.20–23,30–34 | Alerte, moyens maritimes/terrestres, position, urgence/détresse | VHF et plan de secours N2 ; quatre cartes N3 d’alerte/message/radio/aggravation | Couvert pour les décisions retenues ; la qualification CRR complète est hors périmètre |
| S04 p.26 | Utilité du défibrillateur | `n3-secours-gasp-001` dans le corrigé | Mention présente ; le PDF exclut expressément l’apprentissage de son utilisation du RIFAP. Ne pas déclarer tous les gestes DEA obligatoires dans le deck N3 |

## Contrôle des autres PDF et arbitrages

| Source | Apport / sections rapprochées | Conclusion |
| --- | --- | --- |
| S02 — Eragnole, 45 p. | Réglementation, physique/gaz p.3–13 ; accidents, décompression, ordinateurs p.14–33 ; autonomie et risques p.34–45 | Grandes familles présentes dans N2+N3. Ne pas reprendre réserve générique par tiers, lest fixe, ancienne procédure tabulaire ou secours simplifié comme règle universelle |
| S03 — FSGT, 3 p. | Conditions et compétences PA60/P3 | Comparaison de périmètre ; conditions FSGT non transférables automatiquement au cursus FFESSM |
| S05 — certification FFESSM, 4 p. | Conditions communes, validation et délivrance | CACI/licence déjà couverts. Modalités propres au N3 incomplètes : voir compléments administratifs ci-dessous |
| S06 — bulletin FFESSM, p.1–2 ; S17 — recommandations CTN, p.2 | Remontées anormales air/ordinateur | Dix cartes N2 réutilisées ; pas besoin d’une copie N3. Reste du bulletin hors programme |
| S07 — accidents 1, p.3–31,33–43 | Barotraumatismes, narcose, gaz et hyperoxie | Barotraumatismes/narcose/gaz pollué dans N2. PO2 calculée en N3 ; toxicité de l’oxygène non travaillée comme objectif distinct. Approfondissement à revalider avec source primaire, sans inventer une qualification nitrox |
| S08 — physique, 34 p. | Pressions, volumes, flottabilité, pressions partielles, dissolution | Réparti dans physique/gaz/ADD N2 et modèles N3 ; absence de copies N3 justifiée |
| S09 — réglementation, 20 p. | Prérogatives, matériel, sécurité, documents et responsabilités | Familles couvertes avec règles actuelles ; les valeurs anciennes ne définissent pas les cartes. Ne pas recréer toutes les conditions administratives historiques |
| S10 — accidents 2, p.13–32 | ADD, facteurs favorisants, déshydratation, OPI | ADD et hydratation dans N2 ; mécanisme/signes/priorités OPI en N3. Schémas circulatoires/FOP : approfondissements possibles, pas exigence de recopier toute l’anatomie |
| S11 — autonomie/organisation/planification, p.4–19,21–33 | Météo/site, organisation, veille, gaz, retour et DTR | Cas et calculs représentés. Valeurs idéales, vitesses ou débits d’exemple non promus en règles universelles |
| S12 — Baker, p.1–9 | M-values, relations de pression et limites théoriques | Principes et calculs représentés dans modèles N3 ; pas de besoin de recopier chaque coefficient/table du document historique |
| S13/S14 — PSE/PSC | Sections pertinentes appelées par RIFAP | Grandes branches couvertes ; détails manquants consignés ci-dessus. Le reste des référentiels n’est pas un programme N3 obligatoire |
| S15 — Peregrine, notamment p.16,25,28,32–34,38 | CEIL, TTS, GF, planificateur, gaz et mode Profondimètre | Objectifs représentés ; entretien, chaque menu et tout le manuel ne sont pas à transformer en cartes |
| S16 — SCUBAPRO, notamment p.2,5,7 | Configuration, limites et partage de gaz | `n3-materiel-partage-profondeur-001` + détendeurs N2 ; conditions fabricant distinctes des prérogatives |
| S18 — ANFR CRR, p.20–23,30–34 | Urgence/détresse et ASN | Cas N3 couverts dans leur périmètre ; procédures/examen radio complets hors périmètre |

## Compléments proposés, sans quota

### Priorité : secours

1. **Noyade et insufflations initiales** : une carte sur la priorité ventilatoire,
   distincte de celle qui interdit de « vider » les poumons. Pour une séquence chiffrée,
   relire la fiche PSE d’arrêt cardiaque/ventilation correspondante, pas seulement la
   fiche noyade ni une formule générique PSC.
2. **Repères de RCP adulte** : séparer alternance, qualité des compressions et rôle de
   la ventilation uniquement si les questions mobilisent des erreurs différentes.
3. **Kit d’oxygène** : contrôle du dispositif monté et du réservoir ; efficacité de la
   ventilation au BAVU. Les exercices de stock existants sont déjà suffisants.
4. **Échec/impossibilité de compression** : un cas de décision ; le garrot apparaît
   actuellement surtout dans l’explication de la carte de compression.
5. **Blessures et brûlures pertinentes pour la plongée** : quelques décisions de
   premiers secours, avec source actuelle et contexte local pour les envenimations.
   Ne pas inventer un traitement unique commun à toutes les espèces.

### Priorité : objectifs explicites du MFT

6. **Arrêt et tour d’horizon à 3 m** : un objectif distinct du parachute ou de la seule
   surveillance du trafic ; vérifier formulation/contexte lors de la rédaction.
7. **Nourrissage et discrétion** : un fait simple sur le refus de nourrir ; un cas distinct
   sur le dérangement si cela ajoute une décision, sans doubler la carte d’éclairage.
8. **Milieu courant** : quelques espèces supplémentaires réellement rencontrées,
   avec identification visuelle si les médias sont utilisables. Adapter au terrain ;
   les PDF ne fournissent pas ici une liste universelle d’espèces à mémoriser.
9. **Profils inversés** : préciser ce que le référentiel appelle un profil à risques,
   avec un cas qui ajoute une distinction au yoyo et aux successives déjà traités.
10. **Acclimatation à la désaturation** : le MFT la cite mais ne la définit pas. Rechercher
   une explication primaire avant rédaction ; ne pas la confondre avec reprise d’aisance,
   saturation des compartiments ou diminution garantie du risque par répétition.

### Secondaire : vocabulaire et cursus

- Ajouter éventuellement « cutis marmorata » dans le corrigé de `n2-add-peau-001` ;
  conserver l’ID et la question de reconnaissance existants.
- Compléter les modalités N3 : délai de **15 mois depuis la première compétence
  validée**, cadre de validation en milieu naturel et délivrance (S01 p.4,16).
  Les accès spécifiques PA40/PE60 peuvent être traités si le deck entend aussi préparer
  ces qualifications isolées, et non uniquement l’accès au brevet N3.
- Approfondissement hyperoxie : possible d’après S07, avec revalidation primaire et
  périmètre explicite. Le calcul de PO2 n’interroge pas à lui seul les manifestations
  et réactions ; ce manque secondaire ne signifie pas qu’un cours nitrox entier manque.

## Décision éditoriale

Ne pas annoncer « tout le N3 couvert par les PDF » à ce stade. Conserver la structure
N2/base + N3/compléments, puis traiter ces objectifs distincts avec des QCM quand ils
s’y prêtent. La majorité du contenu ne demande ni répétition supplémentaire ni refonte.
Le prochain lot doit partir de ce recoupement, puis vérifier chaque nouveau fait et
chaque choix avec les sources primaires actuelles avant publication. Le nombre final
résultera des objectifs utiles, pas d’un objectif de volume.
