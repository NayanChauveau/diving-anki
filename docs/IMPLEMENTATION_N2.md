# Plan d’implémentation du deck Plongée N2

Plan établi le 5 octobre 2026. Chapitre 01 implémenté : 28 cartes revues pour P001–P027.
Voir [la revue et la correspondance des IDs](reviews/01-prerogatives.md).

## Objectif et volume

Préparer un deck français ample, avec rappel, compréhension, calcul, correction d’erreur,
lecture de schéma et mise en situation. Le catalogue ci-dessous contient **629 cartes candidates**,
chacune identifiable et cochable. Ce nombre inclut les approfondissements nécessitant un complément,
les sujets à vérifier et les quelques cartes culturelles facultatives : ce n’est pas un engagement à
publier 629 cartes sans revue. Une carte publiée doit apporter un angle distinct.

Le périmètre est celui de ces trois documents, pas une garantie de couverture exhaustive du
référentiel N2 officiel. N3 et N4 ne sont pas traités. Les compétences pratiques mentionnées
par le flyer sont séparées de leurs procédures, que ces documents ne détaillent pas.

## Sources et traçabilité

| Code | Document | Édition / nature | Pages PDF |
| --- | --- | --- | --- |
| S1 | [Théorie Niveau 2 – Stade de Vanves](/Users/nayanchauveau/Downloads/Theorie-Niveau-2-Edition-2024.pdf) | Édition 2024, version 1.1 ; cours principal | 35 |
| S2 | [Flyer FFESSM Niveau 2](/Users/nayanchauveau/Downloads/0093e41a527610a49ad0c5d39d5e660288b4c9ff.pdf) | Flyer 2021 ; compétences et conditions | 2 |
| S3 | [Notions de physique – Dominique David, CPDA](/Users/nayanchauveau/Downloads/2024Niveau2CoursTheoriquesDDNOTIONDEPHYSIQUE.pdf) | 2024 ; cours et exercices | 6 |

Toutes les références « p. » du catalogue désignent la page PDF, comptée à partir de 1.
Dans S1 la pagination imprimée correspond ; dans S3 elle commence à 3, donc ajouter 2.
S1 p.1 est la couverture, p.2 le sommaire, p.35 une page de notes : aucune carte dédiée.
Extraction textuelle complète des 43 pages, complétée par inspection des tableaux illustrés
S1 p.24–25 et p.34 ainsi que des exercices et applications S3 p.3 et p.6.
Les références sont des repères de travail ; toutes les formulations futures seront originales.

## Comment exécuter ce plan

Une case du catalogue représente une carte à concevoir, pas une notion globalement « terminée ».
Chaque ligne a un ID de plan (Pxxx), un format et un angle. Les numéros sont stables dans ce plan.
Les futurs IDs YAML seront permanents, par exemple `n2-pression-pabs-6m-001` ; ne pas utiliser
le seul numéro de ligne comme identité sémantique d’une carte publiée.

- `QCM` : une seule bonne réponse, distracteurs plausibles, explication du mécanisme ou de l’erreur.
- `Basic` : réponse courte activement rappelée ; utile pour définitions et justification.
- `Cloze` : seulement formule, relation ou repère validé, une suppression utile par carte.
- `Calcul` / `Scénario` / `Comparaison` / `Erreur` / `Lecture` : angles ; pas de nouveaux types YAML.
- `Vxx` : contrôle éditorial de la section, à appliquer aux lignes concernées avant publication.
- `Complément` : objectif prévu mais source insuffisante ; obtenir une référence avant rédaction.
- `Facultatif` : culture fédérale, histoire ou chiffres datés ; à faire après la théorie essentielle.

Toutes les futures cartes ciblent `levels: [N2]`, sont en `fr` et commencent `draft`.
Ne pas attribuer N3/N4 automatiquement. Un sujet partagé entre S1 et S3 n’est pas dupliqué
mot pour mot : il est fusionné puis décliné en angles complémentaires.

## Répétition pédagogique voulue

Pour les notions centrales, répartir les rappels sur plusieurs tâches : définir, expliquer,
calculer dans le sens direct, calculer dans le sens inverse, réfuter une erreur, puis appliquer
à une situation. Les dernières lignes du catalogue ajoutent des reprises explicites.
Ne pas générer dix variantes numériques mécaniques d’un même exercice : choisir des valeurs
qui exposent un piège distinct (surface, proche surface, pression relative, pression absolue).

Exemple de famille : pression absolue → définition ; calcul à 6 m ; profondeur inverse ;
confusion à 20 m ; effet relatif proche surface. Chaque carte tient seule sans référence
à une carte précédente. Pour un accident : mécanisme, signes, prévention, alerte et scénario
sont des objectifs séparés. Ne pas apprendre une liste entière de symptômes sur un seul recto.

## Ordre d’implémentation

1. Résoudre les erreurs de physique V04/V05, fixer le modèle simplifié et les conventions d’unités.
2. Rédiger pressions, flottabilité et gaz ; tester les calculs avec une résolution indépendante.
3. Valider V01–V03, puis rédiger prérogatives et organisation.
4. Valider V07–V09 avec les références appropriées, puis accidents et prévention.
5. Valider V10–V12, puis tables, ordinateurs et remontées anormales.
6. Valider V13/V14, puis blocs et détendeurs ; produire les schémas originaux.
7. Préparation collective et scénarios transversaux ; intégrer les compléments obtenus.
8. Renforcement ciblé ; culture et histoire facultatives en dernier.

Un lot peut contenir 15 à 25 cartes d’un même thème. Après chaque lot : revue factuelle,
revue pédagogique, `make check`, build avec drafts et inspection dans Anki.
Le passage à `reviewed` n’est autorisé qu’après revue ; les contrôles techniques seuls ne suffisent pas.

## Registre des vérifications avant rédaction normative

Les observations suivantes comparent les documents fournis ; elles ne constituent pas une
vérification de la réglementation ou des protocoles en vigueur. Cette recherche primaire
fait partie de l’implémentation future. Ne pas choisir arbitrairement un support en cas de conflit.

- [x] **V01** — Âges et aptitudes : S2 (flyer 2021) annonce PE40 16 ans et PA20 18 ans ; S1 (2024) distingue PE40 14 ans, PA20/N2 15 ans et exercice autonome 16 ans. Vérifier MFT FFESSM et Code du sport en vigueur avant toute réponse normative ; conserver distinction formation/certification/exercice.

- [ ] **V02** — Organisation et équipements : vérifier les articles cités, leur version et le champ exact (milieu naturel, circuit ouvert, air, exploration). S1 introduit le GP avec un article définissant surtout la palanquée : ne pas confondre citation et définition du rôle.

- [ ] **V03** — CACI, licence, chasse, signalisation et patrimoine : vérifier textes fédéraux et règles applicables au lieu. Les chiffres de licenciés, structures et gouvernance sont datés et de faible priorité. La reconnaissance CMAS ne donne pas une autorisation universelle de plonger.

- [ ] **V04** — Erreur confirmée dans S3 p.3, exercice à 6 m : le corrigé indique 2,5 bar alors que sa propre formule 1 + 6/10 donne 1,6 bar. kg n’est pas une unité de force ; kgf/cm² et bar ne sont pas strictement identiques. Les calculs doivent annoncer le modèle pédagogique simplifié.

- [ ] **V05** — Incohérence confirmée S3 p.6 : eau de mer plus porteuse, mais le support propose de retirer du lest lors du passage eau douce vers mer. Vérifier puis corriger la direction ; aucun décalage fixe universel. Les différences acier/alu, 12/15 L et bloc plein/vide dépendent du matériel. Le lest ajouté a lui-même un volume : préciser si négligé dans les exercices.

- [ ] **V06** — Boyle-Mariotte : température et quantité de gaz constantes, pressions absolues. Le stock calculé avec la pression nominale est une approximation de cours, pas une planification réelle. Tous les calculs sans réserve doivent être nommés « théoriques » ; obtenir une source pour les règles opérationnelles de réserve et de retour.

- [ ] **V07** — Accidents, froid et essoufflement : vérifier mécanismes et conduites avec les supports de formation/secourisme actuels. Ne pas adopter automatiquement rinçage nasal à l’eau de mer, collyre, reprise de plongée après un délai fixe, boisson à toute victime, Valsalva forcé ou consigne de réimmersion sans contexte. Le tableau p.16 et les paragraphes p.13–16 ne sont pas entièrement équivalents.

- [ ] **V08** — Narcose : seuils non universels ; ne pas reprendre « constante à 50 m » ni « pas de prévention » comme absolus. Composition détaillée de l’air et rôle des différents gaz à vérifier. Ne pas étendre ces documents à une formation nitrox ou à des limites de toxicité absentes.

- [ ] **V09** — ADD : vérifier symptômes et protocole de secours actuel, installation de la victime, débit et administration O2, hydratation, avion/altitude et effort après plongée. Ne pas enseigner un délai de 12 h comme exclusion ni une formule obligatoire d’hydratation. Le résumé physiologique sur les bulles est simplifié ; éviter de présenter tout retour de l’azote comme une formation nécessaire de microbulles.

- [ ] **V10** — MN90 : identifier l’édition, domaine d’emploi et tableaux complets avant exercices chiffrés. S1 p.25 montre un extrait et non les tables de calcul de successives. S1 p.24 contient une courbe illustrée : confirmer valeurs et conventions, notamment frontières d’intervalles. Pas d’utilisation comme consigne universelle de plongée.

- [ ] **V11** — Ordinateurs : vitesses, fréquence de mesure, verrouillage, autonomie batterie, modes et algorithmes dépendent du modèle. Ne pas retenir « 24 h de verrouillage » ou « 2–3 plongées max » comme universels. Vérifier les écrans originaux et le manuel ; tenir compte des obligations de tous les équipiers.

- [ ] **V12** — Remontées anormales : S1 juxtapose procédures MN90 et préconisations fédérales dites nouvelles en 2024. Retrouver le texte primaire et sa version avant rédiger des cartes d’action (seuils, délais, profondeurs, paliers, réimmersion, observation). Aucune carte de réimmersion prête à publier sur le seul extrait.

- [ ] **V13** — Blocs : S1 mentionne 2 ans / 5 ans avec TIV et « ne pas transporter sous pression ». Vérifier réglementation des équipements sous pression, régime TIV et consignes de transport actuels. Ne pas publier ces formulations telles quelles. Gonflage réservé aux opérateurs habilités.

- [ ] **V14** — Détendeurs : schémas et tableaux décrivent des conceptions particulières. Confirmer différences de MP, compensation, froid, entretien et stockage au manuel constructeur. Panne observée ≠ cause certaine ; ne pas transformer la colonne réparation en tutoriel de démontage. Les modèles commerciaux sont des exemples datés, pas une liste à apprendre.

- [ ] **V15** — S2 énonce des compétences sans cours détaillé pour orientation, assistance et planification. Les cartes fondées sur ce flyer peuvent tester les objectifs et responsabilités ; obtenir une source supplémentaire pour les procédures techniques. Les cartes ne valident pas la maîtrise pratique.

## Répartition et fichiers proposés

Les fichiers proposés restent dans `cards/n2/`, un fichier par chapitre. Les sous-decks sont
français ; le builder ajoutera `Plongée::N2::` devant les chemins indiqués.

| Chapitre | Sous-deck | Cartes principales |
| --- | --- | ---: |
| `01-prerogatives.yaml` | Réglementation::Prérogatives | 27 |
| `02-organisation.yaml` | Réglementation::Organisation | 31 |
| `03-documents-environnement.yaml` | Réglementation::Documents et responsabilité | 36 |
| `04-pression.yaml` | Physique::Pressions | 38 |
| `05-flottabilite.yaml` | Physique::Flottabilité | 40 |
| `06-gaz-autonomie.yaml` | Physique::Gaz et autonomie | 34 |
| `07-barotraumatismes.yaml` | Sécurité::Barotraumatismes | 53 |
| `08-essoufflement.yaml` | Sécurité::Essoufflement | 21 |
| `09-froid.yaml` | Sécurité::Froid | 18 |
| `10-narcose.yaml` | Sécurité::Narcose et pressions partielles | 28 |
| `11-add.yaml` | Sécurité::Désaturation et ADD | 54 |
| `12-tables.yaml` | Désaturation::Tables MN90 | 34 |
| `13-ordinateurs.yaml` | Désaturation::Ordinateurs | 39 |
| `14-remontees-anormales.yaml` | Désaturation::Remontées anormales | 20 |
| `15-gonflage-blocs.yaml` | Matériel::Gonflage et blocs | 33 |
| `16-detendeurs.yaml` | Matériel::Détendeurs | 40 |
| `17-competences-transversales.yaml` | Autonomie::Préparation et palanquée | 26 |
| `18-lecture-pannes.yaml` | Matériel::Pannes et lecture de supports | 20 |
| Reprises complémentaires, réparties dans les chapitres existants | Plusieurs | 37 |
| **Total candidates** | | **629** |

## Catalogue des cartes à produire

Cocher seulement après rédaction et validation de la carte correspondante. Dans chaque section,
les références et vérifications annoncées valent pour toutes les cartes ; affiner ensuite
`review.sources` avec le paragraphe ou la figure précis pendant la rédaction.

### 01-prerogatives — Réglementation::Prérogatives

Source : **S1 p.3–4 ; S2 p.1–2**. Contrôle : **V01**. Fichier futur : `cards/n2/01-prerogatives.yaml`.

- [x] **P001** · QCM · Rappel / application — N2 : articulation des aptitudes PA20 et PE40.
- [x] **P002** · QCM · Rappel / application — PE40 : profondeur maximale et présence du guide.
- [x] **P003** · QCM · Rappel / application — PA20 : profondeur maximale et autonomie.
- [x] **P004** · QCM · Rappel / application — Qualifications PA20 et PE40 acquises séparément.
- [x] **P005** · QCM · Comparaison — Comparer PE20 et PE40.
- [x] **P006** · QCM · Comparaison — Distinguer autonomie et absence de directeur de plongée.
- [x] **P007** · QCM · Rappel / application — Composition d’une palanquée PA20 : nombre d’équipiers.
- [x] **P008** · QCM · Rappel / application — Compétences minimales des équipiers PA20.
- [x] **P009** · Basic · Compréhension — Rôle de la décision du DP dans l’accès aux prérogatives.
- [x] **P010** · QCM · Scénario — Scénario : N2 demandant une exploration autonome à 30 m.
- [x] **P011** · QCM · Scénario — Scénario : N2 encadré à 35 m.
- [x] **P012** · QCM · Scénario — Scénario : N2 autonome avec un équipier aux aptitudes plus restrictives.
- [x] **P013** · QCM · Rappel / application — Âge d’entrée en formation PE40.
- [x] **P014** · QCM · Rappel / application — Âge de délivrance PA20 et N2.
- [x] **P015** · QCM · Rappel / application — Âge d’exercice effectif de l’autonomie.
- [x] **P016** · QCM · Comparaison — Distinction formation, certification et exercice des prérogatives.
- [x] **P017** · QCM · Rappel / application — Autorisation du représentant légal pour un mineur autonome.
- [x] **P018** · QCM · Rappel / application — Information des équipiers de la présence d’un mineur.
- [x] **P019** · QCM · Rappel / application — PE40 mineur : absence de palier obligatoire.
- [x] **P020** · QCM · Rappel / application — PE40 mineur : nombre de plongées et intervalle.
- [x] **P021** · QCM · Rappel / application — PE40 mineur : profondeur de la seconde après une première profonde.
- [x] **P022** · QCM · Rappel / application — Conditions communes : licence et CACI.
- [x] **P023** · QCM · Rappel / application — Prérequis N1 ou équivalence.
- [x] **P024** · QCM · Rappel / application — Expérience préalable en milieu naturel.
- [x] **P025** · QCM · Scénario — Scénario : brevet acquis mais conditions d’autonomie non réunies.
- [x] **P026** · QCM · Rappel / application — Double certification FFESSM et CMAS deux étoiles.
- [x] **P027** · QCM · Rappel / application — Reconnaissance internationale et règles locales : éviter la promesse de droit universel.

### 02-organisation — Réglementation::Organisation

Source : **S1 p.4–5 ; S2 p.1–2**. Contrôle : **V02**. Fichier futur : `cards/n2/02-organisation.yaml`.

- [ ] **P028** · QCM · Rappel / application — Définition d’une palanquée.
- [ ] **P029** · QCM · Rappel / application — Durée, profondeur et trajet communs.
- [ ] **P030** · QCM · Rappel / application — Palanquée avec mélanges ou aptitudes différents : contrainte la plus restrictive.
- [ ] **P031** · QCM · Rappel / application — DP : présence sur le site et responsabilité d’organisation.
- [ ] **P032** · QCM · Rappel / application — DP : caractéristiques fixées pour la plongée.
- [ ] **P033** · QCM · Rappel / application — DP : dispositions de sécurité.
- [ ] **P034** · QCM · Rappel / application — DP : déclenchement des secours.
- [ ] **P035** · QCM · Rappel / application — Fiche de sécurité : identité et fonction des plongeurs.
- [ ] **P036** · QCM · Rappel / application — Fiche de sécurité : paramètres prévus et réalisés.
- [ ] **P037** · QCM · Comparaison — Distinguer responsabilités du DP et du GP.
- [ ] **P038** · QCM · Rappel / application — GP : conduite d’une exploration PE40.
- [ ] **P039** · QCM · Rappel / application — Équipiers PA20 : sécurité collective.
- [ ] **P040** · QCM · Rappel / application — Plan de secours écrit et adapté au site.
- [ ] **P041** · QCM · Rappel / application — Plan de secours : modalités d’alerte et coordonnées.
- [ ] **P042** · QCM · Rappel / application — Plan de secours : personnes devant en prendre connaissance.
- [ ] **P043** · QCM · Rappel / application — Moyen de communication et contexte d’emploi de la VHF.
- [ ] **P044** · QCM · Rappel / application — Eau potable et couverture isothermique à disposition.
- [ ] **P045** · QCM · Rappel / application — Oxygénothérapie : capacité adaptée à l’attente des secours.
- [ ] **P046** · QCM · Rappel / application — Identifier BAVU et masque à haute concentration.
- [ ] **P047** · QCM · Rappel / application — Fiche d’évacuation : fonction.
- [ ] **P048** · QCM · Rappel / application — Bloc de secours équipé et adapté au mélange.
- [ ] **P049** · QCM · Rappel / application — Moyen de rappel des plongeurs depuis le bateau.
- [ ] **P050** · QCM · Rappel / application — Tablette de notation et tables disponibles selon le contexte.
- [ ] **P051** · QCM · Rappel / application — Manomètre ou système équivalent sur le bloc.
- [ ] **P052** · QCM · Rappel / application — Système gonflable pour regagner et tenir la surface.
- [ ] **P053** · QCM · Rappel / application — Source d’air pour un équipier sans partage d’embout.
- [ ] **P054** · Basic · Compréhension — Contrôle des paramètres personnels en autonomie ou au-delà de 20 m encadré.
- [ ] **P055** · QCM · Rappel / application — Équipement spécifique de l’encadrant : deux sorties et deux détendeurs.
- [ ] **P056** · QCM · Rappel / application — Parachute : équipement de la palanquée.
- [ ] **P057** · QCM · Scénario — Scénario : équipement manquant pour passer de PE20 à PE40.
- [ ] **P058** · QCM · Scénario — Scénario : équipement manquant pour une plongée PA20.

### 03-documents-environnement — Réglementation::Documents et responsabilité

Source : **S1 p.5–7 ; S2 p.2**. Contrôle : **V03**. Fichier futur : `cards/n2/03-documents-environnement.yaml`.

- [ ] **P059** · QCM · Comparaison — Distinguer licence, brevet et CACI.
- [ ] **P060** · Basic · Compréhension — Rôle du CACI.
- [ ] **P061** · QCM · Rappel / application — Validité du CACI et médecin habilité selon le contexte.
- [ ] **P062** · QCM · Rappel / application — Exceptions de découverte : ne pas les étendre à une formation N2.
- [ ] **P063** · QCM · Rappel / application — Licence : affiliation et participation aux activités.
- [ ] **P064** · QCM · Rappel / application — Licence : responsabilité civile.
- [ ] **P065** · QCM · Comparaison — Distinguer responsabilité civile et assurance individuelle accident.
- [ ] **P066** · QCM · Rappel / application — Période de couverture de la licence : vérifier la saison.
- [ ] **P067** · QCM · Rappel / application — QR code : accès aux brevets et qualifications.
- [ ] **P068** · QCM · Rappel / application — Vérification documentaire avant une sortie.
- [ ] **P069** · QCM · Rappel / application — Zones interdites et dérogations locales.
- [ ] **P070** · QCM · Rappel / application — Prélèvement au fond et respect du milieu.
- [ ] **P071** · QCM · Rappel / application — Objet archéologique : laisser en place.
- [ ] **P072** · QCM · Rappel / application — Découverte archéologique : signalement.
- [ ] **P073** · QCM · Comparaison — Chasse sous-marine et scaphandre : distinguer les interdictions.
- [ ] **P074** · QCM · Rappel / application — Signalisation depuis un bateau.
- [ ] **P075** · QCM · Rappel / application — Signalisation depuis la plage.
- [ ] **P076** · QCM · Rappel / application — Distance de sécurité des navires : règle locale à vérifier.
- [ ] **P077** · QCM · Rappel / application — Respect des prérogatives malgré une envie de suivre un autre groupe.
- [ ] **P078** · QCM · Rappel / application — Requalification des blocs : responsabilité.
- [ ] **P079** · QCM · Rappel / application — Signification de FFESSM.
- [ ] **P080** · Basic · Compréhension — Signification et rôle de la CMAS.
- [ ] **P081** · Basic · Compréhension — Rôle de la Commission Technique Nationale.
- [ ] **P082** · Basic · Compréhension — Rôle de la commission médicale et de prévention.
- [ ] **P083** · QCM · Rappel / application — Comités régionaux et départementaux.
- [ ] **P084** · QCM · Rappel / application — Clubs et structures commerciales agréées.
- [ ] **P085** · QCM · Comparaison — Distinction fédération et organismes de formation.
- [ ] **P086** · QCM · Rappel / application — Création de la FFESSM en 1955.
- [ ] **P087** · Basic · Compréhension — Lien historique FFESSM-CMAS en 1959.
- [ ] **P088** · Basic · Facultatif — Siège fédéral : repère culturel.
- [ ] **P089** · Basic · Facultatif — Commissions culturelles : identifier les familles.
- [ ] **P090** · QCM · Rappel / application — Commissions sportives : identifier les familles.
- [ ] **P091** · QCM · Rappel / application — Autres organismes français cités.
- [ ] **P092** · QCM · Rappel / application — Autres organismes internationaux cités.
- [ ] **P093** · Basic · Facultatif — Gouvernance associative et élections : détail facultatif.
- [ ] **P094** · Basic · Facultatif — Effectifs et nombre de structures : données datées, facultatives.

### 04-pression — Physique::Pressions

Source : **S1 p.9–10 ; S3 p.2–3 (imprimées 4–5)**. Contrôle : **V04**. Fichier futur : `cards/n2/04-pression.yaml`.

- [ ] **P095** · QCM · Rappel / application — Définition d’une pression.
- [ ] **P096** · Cloze · Relation — Relation P = F / S.
- [ ] **P097** · Basic · Compréhension — Force plus grande à surface fixe : effet sur la pression.
- [ ] **P098** · Basic · Compréhension — Surface plus grande à force fixe : effet sur la pression.
- [ ] **P099** · QCM · Rappel / application — Analogie raquettes : expliquer par la surface.
- [ ] **P100** · QCM · Comparaison — Analogie punaise : comparer pointe et tête.
- [ ] **P101** · QCM · Rappel / application — Unité usuelle en plongée : bar.
- [ ] **P102** · QCM · Comparaison — Distinguer masse, force et pression.
- [ ] **P103** · Basic · Compréhension — Pression atmosphérique : origine.
- [ ] **P104** · QCM · Rappel / application — Valeur de référence au niveau de la mer dans le modèle simplifié.
- [ ] **P105** · QCM · Rappel / application — Altitude : évolution qualitative de la pression atmosphérique.
- [ ] **P106** · QCM · Rappel / application — Météo : variation qualitative de la pression atmosphérique.
- [ ] **P107** · Basic · Compréhension — Pression hydrostatique : origine.
- [ ] **P108** · QCM · Comparaison — Pression relative : distinguer de la pression absolue.
- [ ] **P109** · QCM · Rappel / application — Modèle simplifié : 1 bar hydrostatique par 10 m.
- [ ] **P110** · QCM · Rappel / application — Pression absolue : somme des deux contributions.
- [ ] **P111** · QCM · Rappel / application — À même profondeur : pression identique dans le modèle.
- [ ] **P112** · QCM · Rappel / application — Descente et remontée : sens de variation.
- [ ] **P113** · Basic · Compréhension — Pourquoi 0 m ne signifie pas 0 bar absolu.
- [ ] **P114** · Basic · Calcul — Phyd à 3 m.
- [ ] **P115** · Basic · Calcul — Phyd à 10 m.
- [ ] **P116** · Basic · Calcul — Phyd à 15 m.
- [ ] **P117** · Basic · Calcul — Phyd à 27 m.
- [ ] **P118** · Basic · Calcul — Pabs à 6 m : corriger l’exercice du support.
- [ ] **P119** · Basic · Calcul — Pabs à 11 m.
- [ ] **P120** · Basic · Calcul — Pabs à 20 m.
- [ ] **P121** · Basic · Calcul — Pabs à 33 m.
- [ ] **P122** · Basic · Calcul — Pabs à 40 m.
- [ ] **P123** · Basic · Calcul — Profondeur correspondant à 1,5 bar absolu.
- [ ] **P124** · Basic · Calcul — Profondeur correspondant à 2,8 bars absolus.
- [ ] **P125** · Basic · Calcul — Profondeur correspondant à 4 bars absolus.
- [ ] **P126** · Basic · Calcul — Profondeur correspondant à 2 bars relatifs.
- [ ] **P127** · QCM · Erreur / limite — Erreur : ajouter deux fois la pression atmosphérique.
- [ ] **P128** · QCM · Erreur / limite — Erreur : appliquer une pression relative à Boyle-Mariotte.
- [ ] **P129** · QCM · Comparaison — Comparer les rapports de pression 0–10 m et 10–20 m.
- [ ] **P130** · QCM · Rappel / application — Variation absolue et variation relative : différence.
- [ ] **P131** · Basic · Compréhension — Pourquoi les dix derniers mètres demandent une vigilance accrue.
- [ ] **P132** · QCM · Rappel / application — Reconnaître hPa, mmHg et PSI sans apprendre les conversions.

### 05-flottabilite — Physique::Flottabilité

Source : **S1 p.8–9 ; S3 p.4–6 (imprimées 6–8)**. Contrôle : **V05**. Fichier futur : `cards/n2/05-flottabilite.yaml`.

- [ ] **P133** · QCM · Comparaison — Poids réel et poids apparent : distinction.
- [ ] **P134** · QCM · Rappel / application — Poussée d’Archimède : direction et sens.
- [ ] **P135** · Basic · Compréhension — Poussée d’Archimède : lien avec le volume déplacé.
- [ ] **P136** · Cloze · Relation — Formule du poids apparent.
- [ ] **P137** · QCM · Rappel / application — Convention pédagogique 1 litre d’eau ≈ 1 kg.
- [ ] **P138** · QCM · Rappel / application — Poids apparent positif : état de flottabilité.
- [ ] **P139** · QCM · Rappel / application — Poids apparent négatif : état de flottabilité.
- [ ] **P140** · QCM · Rappel / application — Poids apparent nul : état de flottabilité.
- [ ] **P141** · QCM · Erreur / limite — Ne pas confondre signe du poids apparent et signe de flottabilité.
- [ ] **P142** · Basic · Calcul — Objet de 5 kg et 3 L : calcul.
- [ ] **P143** · Basic · Calcul — Objet de 2 kg et 3 L : calcul.
- [ ] **P144** · Basic · Calcul — Objet de 3 kg et 3 L : calcul.
- [ ] **P145** · Basic · Calcul — Objet de 8 kg et 5 L : lest ou portance nécessaires.
- [ ] **P146** · Basic · Calcul — Caisson de 1,5 kg et 3 L : neutralisation simplifiée.
- [ ] **P147** · Basic · Compréhension — Volume déplacé doublé à poids fixe : effet.
- [ ] **P148** · Basic · Compréhension — Poids augmenté à volume fixe : effet.
- [ ] **P149** · Basic · Compréhension — Pourquoi un bloc paraît moins lourd sous l’eau.
- [ ] **P150** · Basic · Compréhension — Pourquoi le néoprène augmente la flottabilité.
- [ ] **P151** · QCM · Rappel / application — Écrasement du néoprène à la descente.
- [ ] **P152** · QCM · Rappel / application — Expansion du néoprène à la remontée.
- [ ] **P153** · Basic · Compréhension — Rôle du gilet pour compenser en profondeur.
- [ ] **P154** · QCM · Rappel / application — Gilet gonflé : volume et poussée.
- [ ] **P155** · QCM · Rappel / application — Poumon ballast : inspiration et flottabilité.
- [ ] **P156** · QCM · Rappel / application — Poumon ballast : expiration et flottabilité.
- [ ] **P157** · QCM · Rappel / application — Poumon ballast et ventilation continue : ne pas enseigner l’apnée.
- [ ] **P158** · QCM · Rappel / application — Bloc plein et bloc consommé : différence de masse.
- [ ] **P159** · Basic · Compréhension — Pourquoi tester le lestage en fin de plongée.
- [ ] **P160** · QCM · Rappel / application — Changement de bloc acier/aluminium : réévaluer le lestage.
- [ ] **P161** · QCM · Rappel / application — Volume nominal du bloc insuffisant pour prédire son lestage.
- [ ] **P162** · QCM · Rappel / application — Changement d’épaisseur de combinaison : réévaluer.
- [ ] **P163** · QCM · Rappel / application — Eau salée plus porteuse que l’eau douce.
- [ ] **P164** · QCM · Rappel / application — Passage eau douce vers mer : direction de correction à vérifier.
- [ ] **P165** · QCM · Rappel / application — Pas de correction universelle de 2 ou 3 kg.
- [ ] **P166** · QCM · Rappel / application — Noter configuration et lestage dans le carnet.
- [ ] **P167** · Basic · Compréhension — Caisson, phare ou accessoire : effet de flottabilité propre.
- [ ] **P168** · QCM · Rappel / application — Parachute tenu au gonflage : risque d’être entraîné.
- [ ] **P169** · Basic · Compréhension — Perte de lest : mécanisme de remontée.
- [ ] **P170** · QCM · Rappel / application — Sur-lestage : efforts et consommation.
- [ ] **P171** · QCM · Rappel / application — Sous-lestage : difficulté en fin de plongée.
- [ ] **P172** · QCM · Scénario — Scénario de stabilisation au palier avec un bloc allégé.

### 06-gaz-autonomie — Physique::Gaz et autonomie

Source : **S1 p.10–12**. Contrôle : **V06**. Fichier futur : `cards/n2/06-gaz-autonomie.yaml`.

- [ ] **P173** · QCM · Rappel / application — Gaz compressible et liquide approximativement incompressible.
- [ ] **P174** · QCM · Rappel / application — Analogie de la pompe fermée avec air puis eau.
- [ ] **P175** · QCM · Rappel / application — Boyle-Mariotte : relation inverse volume-pression.
- [ ] **P176** · QCM · Rappel / application — Conditions du modèle : température et quantité de gaz constantes.
- [ ] **P177** · QCM · Rappel / application — Utiliser les pressions absolues.
- [ ] **P178** · Cloze · Relation — Formule P1V1 = P2V2.
- [ ] **P179** · Basic · Calcul — Ballon souple de 12 L en surface : volume à 20 m.
- [ ] **P180** · Basic · Calcul — Ballon souple de 6 L en surface : volume à 10 m.
- [ ] **P181** · Basic · Calcul — Ballon souple de 10 L en surface : volume à 40 m.
- [ ] **P182** · Basic · Calcul — Gaz de 2 L à 20 m : volume en surface.
- [ ] **P183** · Basic · Calcul — Gaz de 4 L à 10 m : volume à 30 m.
- [ ] **P184** · QCM · Comparaison — Comparer expansion 10–0 m et 20–10 m.
- [ ] **P185** · QCM · Rappel / application — Bloc rigide et ballon souple : ne pas confondre volumes.
- [ ] **P186** · QCM · Rappel / application — Gilet à la descente : compensation de compression.
- [ ] **P187** · QCM · Rappel / application — Gilet à la remontée : purge et expansion.
- [ ] **P188** · QCM · Rappel / application — Masque à la descente : apport d’air.
- [ ] **P189** · QCM · Rappel / application — Oreille à la descente : équilibrage.
- [ ] **P190** · QCM · Rappel / application — Détendeur : gaz délivré à la pression ambiante.
- [ ] **P191** · QCM · Rappel / application — Consommation en litres ramenés en surface et litres ambiants.
- [ ] **P192** · Basic · Calcul — Consommation surface de 20 L/min à 10 m.
- [ ] **P193** · Basic · Calcul — Consommation surface de 20 L/min à 20 m.
- [ ] **P194** · Basic · Calcul — Consommation surface de 20 L/min à 40 m.
- [ ] **P195** · Basic · Calcul — Stock théorique d’un 12 L à 200 bar.
- [ ] **P196** · Basic · Calcul — Stock théorique d’un 15 L à 200 bar.
- [ ] **P197** · Basic · Calcul — Autonomie théorique du 12 L à la surface sans réserve.
- [ ] **P198** · Basic · Calcul — Autonomie théorique du 12 L à 10 m sans réserve.
- [ ] **P199** · Basic · Calcul — Autonomie théorique du 12 L à 20 m sans réserve.
- [ ] **P200** · QCM · Comparaison — Rapport d’autonomie surface versus 40 m.
- [ ] **P201** · Basic · Compréhension — Pourquoi les exemples sans réserve ne constituent pas une planification.
- [ ] **P202** · QCM · Rappel / application — Air consommé pendant remontée et paliers : ne pas l’oublier.
- [ ] **P203** · QCM · Rappel / application — Effort, stress et froid : limites de la consommation constante.
- [ ] **P204** · Basic · Complément — Complément à documenter : volume utilisable avec réserve.
- [ ] **P205** · Basic · Complément — Complément à documenter : calcul inverse d’une chute de pression.
- [ ] **P206** · Basic · Complément — Complément à documenter : comparer deux équipiers avant le demi-tour.

### 07-barotraumatismes — Sécurité::Barotraumatismes

Source : **S1 p.12–16**. Contrôle : **V07**. Fichier futur : `cards/n2/07-barotraumatismes.yaml`.

- [ ] **P207** · Basic · Compréhension — Barotraumatisme : mécanisme général.
- [ ] **P208** · QCM · Rappel / application — Descente : compression des cavités gazeuses.
- [ ] **P209** · QCM · Rappel / application — Remontée : expansion des cavités gazeuses.
- [ ] **P210** · QCM · Rappel / application — Zone proche de la surface : variations relatives.
- [ ] **P211** · Basic · Compréhension — Placage du masque : effet ventouse.
- [ ] **P212** · QCM · Rappel / application — Placage du masque : signes pendant l’immersion.
- [ ] **P213** · QCM · Rappel / application — Placage du masque : signes après la sortie.
- [ ] **P214** · QCM · Rappel / application — Placage du masque : prévention par apport d’air nasal.
- [ ] **P215** · QCM · Rappel / application — Sinus : cavités et communication avec le nez.
- [ ] **P216** · Basic · Compréhension — Sinus bouché à la descente : mécanisme.
- [ ] **P217** · Basic · Compréhension — Sinus bouché à la remontée : mécanisme.
- [ ] **P218** · QCM · Rappel / application — Sinus : signes d’alerte.
- [ ] **P219** · QCM · Rappel / application — Sinus : prévention avec encombrement ORL.
- [ ] **P220** · QCM · Rappel / application — Sinus : ne pas forcer devant une douleur.
- [ ] **P221** · QCM · Rappel / application — Sinus à la remontée : conduite contextualisée à vérifier.
- [ ] **P222** · Basic · Compréhension — Oreille externe, moyenne et interne : rôles.
- [ ] **P223** · QCM · Rappel / application — Tympan : séparation externe/moyenne.
- [ ] **P224** · QCM · Rappel / application — Trompe d’Eustache : communication et équilibrage.
- [ ] **P225** · QCM · Rappel / application — Oreille moyenne à la descente : déformation du tympan.
- [ ] **P226** · QCM · Rappel / application — Équilibrage précoce, doux et répété.
- [ ] **P227** · QCM · Rappel / application — Douleur d’oreille : ne pas forcer.
- [ ] **P228** · QCM · Rappel / application — Valsalva trop énergique : risque.
- [ ] **P229** · QCM · Rappel / application — Pas de Valsalva à la remontée.
- [ ] **P230** · QCM · Rappel / application — Rhume et efficacité de l’équilibrage.
- [ ] **P231** · QCM · Rappel / application — Descente tête haute : intérêt décrit.
- [ ] **P232** · QCM · Rappel / application — Oreille : douleur, baisse d’audition et saignement.
- [ ] **P233** · QCM · Rappel / application — Différence entre les deux oreilles : vertige alternobarique.
- [ ] **P234** · QCM · Rappel / application — Vertige alternobarique : situation de reconnaissance sans diagnostic.
- [ ] **P235** · QCM · Rappel / application — Obstruction externe par bouchon ou cagoule.
- [ ] **P236** · Basic · Compréhension — Pourquoi les bouchons non adaptés posent problème.
- [ ] **P237** · QCM · Rappel / application — Dents : poche de gaz et obstruction.
- [ ] **P238** · QCM · Rappel / application — Dents : symptômes et prévention.
- [ ] **P239** · QCM · Rappel / application — Dents : douleur à la remontée, conduite à vérifier.
- [ ] **P240** · QCM · Rappel / application — Gaz digestifs : expansion à la remontée.
- [ ] **P241** · Basic · Compréhension — Colique du scaphandrier : nom et mécanisme.
- [ ] **P242** · QCM · Comparaison — Comparer sinus, oreille et dent : localisation insuffisante pour diagnostiquer.
- [ ] **P243** · QCM · Rappel / application — Surpression pulmonaire : air bloqué et expansion.
- [ ] **P244** · QCM · Rappel / application — Surpression pulmonaire : lésions et embolie gazeuse.
- [ ] **P245** · QCM · Rappel / application — Surpression pulmonaire possible près de la surface.
- [ ] **P246** · QCM · Rappel / application — Ventilation libre à la remontée.
- [ ] **P247** · QCM · Rappel / application — Apnée en scaphandre : danger.
- [ ] **P248** · Basic · Compréhension — Panique et remontée incontrôlée : lien avec la surpression.
- [ ] **P249** · QCM · Rappel / application — Surpression : signes respiratoires.
- [ ] **P250** · QCM · Rappel / application — Surpression : signes neurologiques.
- [ ] **P251** · QCM · Rappel / application — Surpression : emphysème sous-cutané.
- [ ] **P252** · QCM · Rappel / application — Suspicion de surpression : alerte et oxygène selon protocole.
- [ ] **P253** · QCM · Rappel / application — Suspicion de surpression : ne pas réimmerger.
- [ ] **P254** · QCM · Comparaison — Distinguer prévention et prise en charge médicale.
- [ ] **P255** · QCM · Rappel / application — Tableau récapitulatif : ne pas transformer collyres ou rinçages en prescriptions.
- [ ] **P256** · QCM · Scénario — Scénario : douleur d’oreille ignorée pendant la descente.
- [ ] **P257** · QCM · Scénario — Scénario : retour surface puis signes respiratoires.
- [ ] **P258** · QCM · Scénario — Scénario : masque qui serre au début de descente.
- [ ] **P259** · QCM · Scénario — Scénario : équipier remonte en bloquant sa respiration.

### 08-essoufflement — Sécurité::Essoufflement

Source : **S1 p.17**. Contrôle : **V07**. Fichier futur : `cards/n2/08-essoufflement.yaml`.

- [ ] **P260** · Basic · Compréhension — Essoufflement : lien avec élimination du CO2.
- [ ] **P261** · QCM · Rappel / application — Profondeur et effort ventilatoire.
- [ ] **P262** · QCM · Rappel / application — Expiration inefficace et cercle vicieux.
- [ ] **P263** · QCM · Rappel / application — Effort excessif : facteur déclenchant.
- [ ] **P264** · QCM · Rappel / application — Froid et émotions : facteurs favorisants.
- [ ] **P265** · QCM · Rappel / application — Détendeur, robinet et ventilation : causes possibles.
- [ ] **P266** · QCM · Rappel / application — Manque d’entraînement et mauvaise forme.
- [ ] **P267** · QCM · Rappel / application — Air pollué : facteur cité à vérifier.
- [ ] **P268** · QCM · Rappel / application — Signes de respiration haletante.
- [ ] **P269** · QCM · Rappel / application — Sensation de manque d’air malgré un bloc non vide.
- [ ] **P270** · QCM · Rappel / application — Risques de panique et d’arrachement d’embout.
- [ ] **P271** · QCM · Rappel / application — Risques de remontée incontrôlée.
- [ ] **P272** · QCM · Rappel / application — Premiers signes : arrêter l’effort et prévenir.
- [ ] **P273** · QCM · Rappel / application — Demander une assistance.
- [ ] **P274** · QCM · Rappel / application — Remontée assistée contrôlée : objectif.
- [ ] **P275** · QCM · Rappel / application — Prévention par rythme ventilatoire calme.
- [ ] **P276** · Basic · Compréhension — Prévention par entretien et contrôle du matériel.
- [ ] **P277** · QCM · Rappel / application — Éviter de lutter contre un courant.
- [ ] **P278** · QCM · Scénario — Scénario : accélérer le palmage aggrave l’essoufflement.
- [ ] **P279** · QCM · Scénario — Scénario : réduire profondeur sans ignorer les autres contraintes.
- [ ] **P280** · QCM · Rappel / application — Prise en charge en surface : protocole à vérifier.

### 09-froid — Sécurité::Froid

Source : **S1 p.17–18**. Contrôle : **V07**. Fichier futur : `cards/n2/09-froid.yaml`.

- [ ] **P281** · QCM · Rappel / application — Équilibre entre chaleur produite et perdue.
- [ ] **P282** · QCM · Rappel / application — Risque de refroidissement pendant une immersion.
- [ ] **P283** · QCM · Rappel / application — Froid léger : frissons et chair de poule.
- [ ] **P284** · QCM · Rappel / application — Froid : diminution de la dextérité.
- [ ] **P285** · QCM · Rappel / application — Froid : diminution de l’attention.
- [ ] **P286** · QCM · Rappel / application — Disparition progressive des frissons : pas un signe rassurant.
- [ ] **P287** · QCM · Rappel / application — Altération de conscience : signe de gravité.
- [ ] **P288** · QCM · Rappel / application — Froid : signaler et terminer la plongée.
- [ ] **P289** · QCM · Rappel / application — Protection adaptée : combinaison, cagoule et chaussons.
- [ ] **P290** · QCM · Rappel / application — Durée d’immersion et exposition.
- [ ] **P291** · QCM · Rappel / application — Fatigue et alimentation : facteurs à considérer.
- [ ] **P292** · QCM · Rappel / application — Froid, essoufflement et narcose : interaction.
- [ ] **P293** · QCM · Rappel / application — Sortie : sécher et protéger du vent.
- [ ] **P294** · Basic · Compréhension — Réchauffement progressif : principe.
- [ ] **P295** · QCM · Rappel / application — Éviter friction et alcool.
- [ ] **P296** · QCM · Rappel / application — Boisson : conditions de conscience et déglutition à vérifier.
- [ ] **P297** · QCM · Rappel / application — Sur bateau exposé : protection avant retrait de combinaison.
- [ ] **P298** · QCM · Scénario — Scénario : doigts maladroits au moment du parachute.

### 10-narcose — Sécurité::Narcose et pressions partielles

Source : **S1 p.18–19**. Contrôle : **V08**. Fichier futur : `cards/n2/10-narcose.yaml`.

- [ ] **P299** · QCM · Rappel / application — Composition simplifiée de l’air 80/20.
- [ ] **P300** · QCM · Rappel / application — Composition simplifiée et composition réelle : différence.
- [ ] **P301** · QCM · Rappel / application — Pression partielle : définition.
- [ ] **P302** · QCM · Rappel / application — Pression partielle = fraction du gaz × Pabs.
- [ ] **P303** · Cloze · Relation — Somme des pressions partielles.
- [ ] **P304** · Basic · Calcul — Calcul PpO2 à 30 m dans le modèle 20 %.
- [ ] **P305** · Basic · Calcul — Calcul PpN2 à 30 m dans le modèle 80 %.
- [ ] **P306** · Basic · Calcul — Calcul PpN2 à 40 m.
- [ ] **P307** · QCM · Rappel / application — Pourcentage constant et pression partielle croissante.
- [ ] **P308** · Basic · Compréhension — Narcose : lien avec la profondeur et les gaz.
- [ ] **P309** · QCM · Rappel / application — Profondeur d’apparition variable selon individu et contexte.
- [ ] **P310** · QCM · Erreur / limite — Ne pas traiter 30 m comme seuil universel.
- [ ] **P311** · QCM · Erreur / limite — Ne pas apprendre la certitude à 50 m sans validation.
- [ ] **P312** · QCM · Rappel / application — Euphorie et angoisse : deux présentations possibles.
- [ ] **P313** · QCM · Rappel / application — Attention et mémoire diminuées.
- [ ] **P314** · QCM · Rappel / application — Coordination et vision perturbées.
- [ ] **P315** · QCM · Rappel / application — Comportement incohérent de l’équipier.
- [ ] **P316** · QCM · Rappel / application — Fatigue, anxiété et manque d’expérience récente.
- [ ] **P317** · QCM · Rappel / application — Descente rapide et effort.
- [ ] **P318** · QCM · Rappel / application — Froid, essoufflement, obscurité et visibilité.
- [ ] **P319** · QCM · Rappel / application — Médicaments : facteur cité à vérifier.
- [ ] **P320** · QCM · Rappel / application — Premiers signes : communiquer à l’encadrant.
- [ ] **P321** · Basic · Compréhension — Réduire la profondeur sous contrôle.
- [ ] **P322** · QCM · Rappel / application — Suite de la plongée : dépend de la gravité et du contexte.
- [ ] **P323** · QCM · Rappel / application — Narcose ne donne pas une autorisation de poursuivre profond.
- [ ] **P324** · QCM · Scénario — Scénario : euphorie prise pour un signe de bonne forme.
- [ ] **P325** · QCM · Scénario — Scénario : équipier inhabituellement lent à répondre.
- [ ] **P326** · QCM · Comparaison — Comparer narcose pendant immersion et symptômes après sortie.

### 11-add — Sécurité::Désaturation et ADD

Source : **S1 p.20–23**. Contrôle : **V09**. Fichier futur : `cards/n2/11-add.yaml`.

- [ ] **P327** · QCM · Comparaison — Gaz dissous et gaz sous forme de bulles : distinction.
- [ ] **P328** · QCM · Rappel / application — Loi de Henry : relation qualitative avec la pression.
- [ ] **P329** · QCM · Rappel / application — Température constante : condition de l’énoncé.
- [ ] **P330** · QCM · Rappel / application — Analogie eau gazeuse : dépressurisation.
- [ ] **P331** · QCM · Rappel / application — Limites de l’analogie bouteille-organisme.
- [ ] **P332** · QCM · Rappel / application — Azote : gaz inerte non consommé comme l’oxygène.
- [ ] **P333** · QCM · Rappel / application — Profondeur et charge en azote.
- [ ] **P334** · QCM · Rappel / application — Durée d’exposition et charge en azote.
- [ ] **P335** · QCM · Rappel / application — Irrigation et différences entre tissus.
- [ ] **P336** · QCM · Rappel / application — Élimination pendant remontée et après sortie.
- [ ] **P337** · Basic · Compréhension — Rôle de la ventilation et des poumons.
- [ ] **P338** · QCM · Rappel / application — Remontée rapide et formation de bulles.
- [ ] **P339** · QCM · Rappel / application — Paliers et vitesse : deux composantes de la désaturation.
- [ ] **P340** · QCM · Rappel / application — Expansion des bulles pendant remontée.
- [ ] **P341** · QCM · Rappel / application — Effort et froid : facteurs de risque à contextualiser.
- [ ] **P342** · Basic · Compréhension — ADD et surpression pulmonaire : mécanismes différents.
- [ ] **P343** · QCM · Rappel / application — ADD malgré le respect affiché du moyen de désaturation.
- [ ] **P344** · QCM · Rappel / application — Apparition des signes immédiate ou retardée.
- [ ] **P345** · QCM · Rappel / application — Pas de délai maximal de 12 h utilisé pour exclure un accident.
- [ ] **P346** · QCM · Rappel / application — Manifestations cutanées : reconnaissance.
- [ ] **P347** · QCM · Rappel / application — Puces et moutons : vocabulaire historique.
- [ ] **P348** · QCM · Rappel / application — Signes cutanés : ne pas qualifier de bénins.
- [ ] **P349** · QCM · Rappel / application — Douleurs articulaires : bends.
- [ ] **P350** · QCM · Rappel / application — Oreille interne : vertiges et troubles auditifs.
- [ ] **P351** · QCM · Rappel / application — Signes neurologiques : fourmillements et faiblesse.
- [ ] **P352** · QCM · Rappel / application — Signes neurologiques : troubles de la parole ou de la vision.
- [ ] **P353** · QCM · Rappel / application — Signes neurologiques : troubles urinaires ou douleur dorsale.
- [ ] **P354** · QCM · Rappel / application — Fatigue inhabituelle et changement de comportement.
- [ ] **P355** · QCM · Rappel / application — Signes respiratoires et douleur thoracique.
- [ ] **P356** · QCM · Rappel / application — Symptômes non spécifiques : alerter sans diagnostic personnel.
- [ ] **P357** · QCM · Rappel / application — Prévenir GP et DP.
- [ ] **P358** · QCM · Rappel / application — Déclencher les secours sans attendre une certitude.
- [ ] **P359** · Basic · Compréhension — Oxygène : rôle et protocole applicable.
- [ ] **P360** · QCM · Rappel / application — Installation de la victime : posture à vérifier.
- [ ] **P361** · QCM · Rappel / application — Hydratation : conditions à vérifier, pas de règle universelle.
- [ ] **P362** · QCM · Rappel / application — Paramètres de plongée à transmettre.
- [ ] **P363** · QCM · Rappel / application — Heure d’apparition et évolution des symptômes.
- [ ] **P364** · QCM · Rappel / application — Récupérer l’ordinateur pour les secours.
- [ ] **P365** · QCM · Rappel / application — Surveiller les équipiers.
- [ ] **P366** · QCM · Erreur / limite — Ne pas réimmerger une victime suspecte.
- [ ] **P367** · QCM · Rappel / application — Amélioration apparente : ne pas interrompre l’alerte ou l’oxygène.
- [ ] **P368** · QCM · Rappel / application — Évacuation décidée avec les secours.
- [ ] **P369** · QCM · Rappel / application — Respecter paliers et consignes de remontée.
- [ ] **P370** · QCM · Rappel / application — Éviter efforts importants après immersion.
- [ ] **P371** · QCM · Rappel / application — Apnée après plongée : précautions à documenter.
- [ ] **P372** · QCM · Rappel / application — Fatigue et mauvaise forme : renoncer.
- [ ] **P373** · QCM · Rappel / application — Sur-lestage et efforts.
- [ ] **P374** · QCM · Rappel / application — Profils inversés et yoyos : contextualiser.
- [ ] **P375** · QCM · Rappel / application — Nombre de plongées et intervalle : référentiel à préciser.
- [ ] **P376** · QCM · Rappel / application — Avion et altitude : délai à documenter.
- [ ] **P377** · QCM · Scénario — Scénario : douleur articulaire après retour au bateau.
- [ ] **P378** · QCM · Scénario — Scénario : équipier silencieux et inhabituellement fatigué.
- [ ] **P379** · QCM · Scénario — Scénario : disparition des signes après oxygène.
- [ ] **P380** · QCM · Scénario — Scénario : deux accidents possibles, même priorité d’alerte.

### 12-tables — Désaturation::Tables MN90

Source : **S1 p.23–26**. Contrôle : **V10**. Fichier futur : `cards/n2/12-tables.yaml`.

- [ ] **P381** · Basic · Compréhension — Tables : rôle historique et principe.
- [ ] **P382** · Basic · Facultatif — Repères Royal Navy et MN90 : facultatifs.
- [ ] **P383** · QCM · Rappel / application — Tables : modèle avec profondeur maximale.
- [ ] **P384** · QCM · Rappel / application — Temps table : début immersion à début remontée.
- [ ] **P385** · QCM · Rappel / application — Différence temps fond et durée totale.
- [ ] **P386** · QCM · Rappel / application — Minute commencée et arrondi supérieur.
- [ ] **P387** · QCM · Rappel / application — Profondeur non listée : règle à documenter.
- [ ] **P388** · QCM · Rappel / application — Tables MN90 : domaine d’emploi à l’air.
- [ ] **P389** · QCM · Rappel / application — Nombre de plongées prévu par le modèle.
- [ ] **P390** · QCM · Rappel / application — Courbe sans palier : définition.
- [ ] **P391** · QCM · Rappel / application — Courbe sans palier ne garantit pas absence d’accident.
- [ ] **P392** · QCM · Lecture / repérage — Lire les unités profondeur et durée.
- [ ] **P393** · QCM · Rappel / application — Colonnes des paliers : profondeur et durée.
- [ ] **P394** · QCM · Rappel / application — Durée totale de remontée : composants.
- [ ] **P395** · Basic · Compréhension — GPS : rôle et lettre.
- [ ] **P396** · QCM · Rappel / application — Vitesse fond-premier palier propre aux MN90.
- [ ] **P397** · QCM · Rappel / application — Vitesse entre paliers propre aux MN90.
- [ ] **P398** · QCM · Erreur / limite — Ne pas transposer une vitesse table à tout ordinateur.
- [ ] **P399** · QCM · Rappel / application — Intervalle de surface : définition.
- [ ] **P400** · QCM · Rappel / application — Plongées consécutives : classification MN90.
- [ ] **P401** · QCM · Rappel / application — Plongées successives : classification MN90.
- [ ] **P402** · QCM · Rappel / application — Frontière de 15 minutes : cas limite.
- [ ] **P403** · QCM · Rappel / application — Frontière de 12 heures : cas limite à documenter.
- [ ] **P404** · Basic · Compréhension — Azote résiduel et rôle du GPS.
- [ ] **P405** · QCM · Rappel / application — Majoration : définition.
- [ ] **P406** · QCM · Comparaison — Durée théorique versus durée réelle.
- [ ] **P407** · QCM · Rappel / application — Variables qui déterminent la majoration.
- [ ] **P408** · QCM · Rappel / application — Remontée lente : temps pris en compte selon MN90.
- [ ] **P409** · QCM · Comparaison — Remontée rapide : procédure historique, à distinguer des recommandations ordinateur.
- [ ] **P410** · QCM · Comparaison — Palier interrompu : procédure historique, à distinguer.
- [ ] **P411** · Basic · Complément — Exercice de lecture d’une ligne de table : données à obtenir.
- [ ] **P412** · QCM · Rappel / application — Exercice de courbe sans palier : valeurs à vérifier visuellement.
- [ ] **P413** · Basic · Complément — Exercice de calcul DTR : données complètes nécessaires.
- [ ] **P414** · Basic · Complément — Exercice de successive : obtenir les tables complémentaires.

### 13-ordinateurs — Désaturation::Ordinateurs

Source : **S1 p.27–29 ; S2 p.1–2**. Contrôle : **V11**. Fichier futur : `cards/n2/13-ordinateurs.yaml`.

- [ ] **P415** · QCM · Rappel / application — Ordinateur : modèle mathématique et capteur.
- [ ] **P416** · QCM · Comparaison — Profil réel versus profil carré des tables.
- [ ] **P417** · QCM · Rappel / application — Profondeur actuelle et profondeur maximale.
- [ ] **P418** · QCM · Rappel / application — Temps écoulé et temps restant sans palier.
- [ ] **P419** · QCM · Rappel / application — NDL : définition et limite.
- [ ] **P420** · QCM · Rappel / application — Profondeur et durée du prochain palier.
- [ ] **P421** · QCM · Comparaison — DTR : distinguer du seul temps du palier.
- [ ] **P422** · QCM · Rappel / application — Vitesse de remontée et alarme.
- [ ] **P423** · QCM · Rappel / application — Affichage du gaz sélectionné.
- [ ] **P424** · QCM · Rappel / application — Réglage eau douce/eau salée.
- [ ] **P425** · QCM · Rappel / application — Température, date et heure : informations secondaires.
- [ ] **P426** · Basic · Calcul — Calcul de désaturation après retour surface.
- [ ] **P427** · QCM · Rappel / application — Garder le même ordinateur pour une série.
- [ ] **P428** · QCM · Erreur / limite — Pourquoi ne pas échanger des ordinateurs déjà utilisés.
- [ ] **P429** · QCM · Rappel / application — Ordinateur d’un équipier : ne remplace pas son historique.
- [ ] **P430** · QCM · Lecture / repérage — Avant immersion : vérifier écran, énergie et réglages.
- [ ] **P431** · QCM · Rappel / application — Avant immersion : comprendre les alarmes.
- [ ] **P432** · QCM · Rappel / application — Avant immersion : convenir de la communication sur les paliers.
- [ ] **P433** · QCM · Rappel / application — Algorithmes et réglages différents : résultats différents.
- [ ] **P434** · QCM · Rappel / application — Palanquée : respecter les obligations de chacun.
- [ ] **P435** · QCM · Rappel / application — Mon ordinateur libéré ne libère pas mes équipiers.
- [ ] **P436** · QCM · Rappel / application — Coordination si profondeurs ou durées de paliers diffèrent.
- [ ] **P437** · QCM · Scénario — Scénario : l’un a un palier et l’autre non.
- [ ] **P438** · QCM · Scénario — Scénario : DTR augmente pendant la plongée.
- [ ] **P439** · QCM · Scénario — Scénario : confusion NDL et autonomie en air.
- [ ] **P440** · QCM · Rappel / application — Gestion de l’air intégrée : dépend d’une sonde.
- [ ] **P441** · QCM · Erreur / limite — Erreur ou verrouillage après incident : dépend du modèle.
- [ ] **P442** · QCM · Rappel / application — Limites des profils atypiques et des efforts.
- [ ] **P443** · QCM · Lecture / repérage — Lire le manuel du modèle utilisé.
- [ ] **P444** · QCM · Rappel / application — Pas de garantie de sécurité fournie par un ordinateur.
- [ ] **P445** · QCM · Rappel / application — Choix : lisibilité et acuité visuelle.
- [ ] **P446** · QCM · Rappel / application — Choix : air ou nitrox selon pratique future.
- [ ] **P447** · QCM · Rappel / application — Choix : pile ou recharge et autonomie.
- [ ] **P448** · QCM · Rappel / application — Choix : simplicité et paramétrage.
- [ ] **P449** · QCM · Rappel / application — Choix : sonde de pression et budget.
- [ ] **P450** · QCM · Rappel / application — Choix : journal et export du profil.
- [ ] **P451** · QCM · Lecture / repérage — Mode simulation : illustrer un écran original à créer.
- [ ] **P452** · QCM · Lecture / repérage — Interpréter un écran avec profondeur, NDL et pression.
- [ ] **P453** · QCM · Lecture / repérage — Interpréter un écran avec obligation de palier et DTR.

### 14-remontees-anormales — Désaturation::Remontées anormales

Source : **S1 p.26–27**. Contrôle : **V12**. Fichier futur : `cards/n2/14-remontees-anormales.yaml`.

- [ ] **P454** · QCM · Comparaison — Distinguer MN90 historique et recommandation fédérale ordinateur.
- [ ] **P455** · QCM · Rappel / application — Identifier la date et le champ d’une recommandation.
- [ ] **P456** · QCM · Rappel / application — Remontée trop rapide : critères de déclenchement à vérifier.
- [ ] **P457** · QCM · Comparaison — Distance, profondeur et vitesse : trois conditions à distinguer.
- [ ] **P458** · QCM · Rappel / application — Réimmersion après remontée anormale : conditions à confirmer.
- [ ] **P459** · QCM · Rappel / application — Délais et profondeur de reprise : paramètres à confirmer.
- [ ] **P460** · QCM · Rappel / application — Paliers supplémentaires : paramètres à confirmer.
- [ ] **P461** · QCM · Rappel / application — Réimmersion impossible : conduite du protocole validé.
- [ ] **P462** · QCM · Rappel / application — Présence de signes d’accident : priorité au secours.
- [ ] **P463** · QCM · Rappel / application — Yoyos : identifier le profil.
- [ ] **P464** · QCM · Rappel / application — Exercices d’assistance : limiter les remontées répétées selon recommandation.
- [ ] **P465** · QCM · Comparaison — Palier obligatoire interrompu versus palier de confort.
- [ ] **P466** · QCM · Rappel / application — Reprise après interruption : conditions à confirmer.
- [ ] **P467** · QCM · Rappel / application — Plus de trois minutes manquantes : règle source à vérifier.
- [ ] **P468** · QCM · Rappel / application — Moins de trois minutes et absence de signe : surveillance à vérifier.
- [ ] **P469** · QCM · Rappel / application — Délai de surveillance et interdiction de replongée : confirmer.
- [ ] **P470** · QCM · Rappel / application — Incident sans symptômes ne signifie pas absence de risque.
- [ ] **P471** · QCM · Scénario — Scénario : confusion entre ancienne et nouvelle procédure.
- [ ] **P472** · QCM · Scénario — Scénario : paliers non réalisés et symptômes.
- [ ] **P473** · QCM · Scénario — Scénario : réimmersion impossible pour raisons de sécurité.

### 15-gonflage-blocs — Matériel::Gonflage et blocs

Source : **S1 p.29–30**. Contrôle : **V13**. Fichier futur : `cards/n2/15-gonflage-blocs.yaml`.

- [ ] **P474** · QCM · Rappel / application — Compresseur : aspiration atmosphérique et compression.
- [ ] **P475** · QCM · Rappel / application — Compression par étapes successives.
- [ ] **P476** · QCM · Rappel / application — Filtres : qualité de l’air respirable.
- [ ] **P477** · QCM · Comparaison — Gonflage direct versus bouteilles tampons.
- [ ] **P478** · QCM · Rappel / application — Tampons : intérêt pour la rapidité.
- [ ] **P479** · QCM · Rappel / application — Pression de gonflage : respecter la pression de service.
- [ ] **P480** · QCM · Rappel / application — Habilitation et accès au local de gonflage.
- [ ] **P481** · QCM · Rappel / application — N2 ne donne pas à lui seul habilitation de gonflage.
- [ ] **P482** · QCM · Rappel / application — Bloc : stockage du gaz respirable.
- [ ] **P483** · QCM · Rappel / application — Acier et aluminium : matériaux.
- [ ] **P484** · QCM · Rappel / application — Mono et bi : configurations.
- [ ] **P485** · QCM · Rappel / application — Capacité en litres et pression : grandeurs différentes.
- [ ] **P486** · QCM · Rappel / application — Inscriptions : fabricant et numéro de série.
- [ ] **P487** · QCM · Rappel / application — Inscriptions : volume intérieur.
- [ ] **P488** · QCM · Rappel / application — Inscriptions : pression de service.
- [ ] **P489** · QCM · Rappel / application — Inscriptions : pression d’épreuve.
- [ ] **P490** · QCM · Comparaison — Pression de service versus pression d’épreuve.
- [ ] **P491** · QCM · Rappel / application — Inscriptions : masse à vide.
- [ ] **P492** · QCM · Rappel / application — Inscriptions : gaz contenu.
- [ ] **P493** · QCM · Rappel / application — Inscriptions : date et marquage de requalification.
- [ ] **P494** · QCM · Rappel / application — Éviter chocs et grandes variations thermiques.
- [ ] **P495** · QCM · Rappel / application — Robinetterie ouverte dans l’eau : risque.
- [ ] **P496** · QCM · Rappel / application — Décharge brutale à l’air : risque.
- [ ] **P497** · QCM · Rappel / application — Peinture et corrosion : surveillance.
- [ ] **P498** · QCM · Comparaison — Inspection visuelle et requalification : distinction.
- [ ] **P499** · Basic · Compréhension — Rôle du TIV.
- [ ] **P500** · QCM · Rappel / application — Périodicités et régime de suivi : vérifier la règle actuelle.
- [ ] **P501** · QCM · Erreur / limite — Ne pas retenir le délai de cinq ans sans vérification.
- [ ] **P502** · QCM · Rappel / application — Transport d’un bloc gonflé : corriger la formulation générale du support.
- [ ] **P503** · QCM · Rappel / application — Précautions de purge avant gonflage : procédure d’opérateur.
- [ ] **P504** · QCM · Scénario — Scénario : lire capacité et pression sur une bouteille.
- [ ] **P505** · QCM · Scénario — Scénario : bloc à requalification dépassée.
- [ ] **P506** · QCM · Scénario — Scénario : changement de bloc et réévaluation du lestage.

### 16-detendeurs — Matériel::Détendeurs

Source : **S1 p.30–34**. Contrôle : **V14**. Fichier futur : `cards/n2/16-detendeurs.yaml`.

- [ ] **P507** · QCM · Rappel / application — Détendeur : gaz à la demande et pression ambiante.
- [ ] **P508** · QCM · Rappel / application — HP, MP et PA : identifier les trois pressions.
- [ ] **P509** · QCM · Rappel / application — Premier étage : HP vers MP.
- [ ] **P510** · QCM · Rappel / application — Second étage : MP vers pression ambiante.
- [ ] **P511** · QCM · Rappel / application — Flexible entre les deux étages.
- [ ] **P512** · QCM · Comparaison — MP relative et MP absolue : distinction.
- [ ] **P513** · QCM · Rappel / application — MP au-dessus de l’ambiante : ordre de grandeur propre au modèle.
- [ ] **P514** · QCM · Rappel / application — Fixation DIN et étrier : identifier.
- [ ] **P515** · QCM · Rappel / application — Premier étage à membrane ou piston.
- [ ] **P516** · QCM · Rappel / application — Chambre sèche et captation de la pression ambiante.
- [ ] **P517** · QCM · Lecture / repérage — Ressort, clapet et siège : rôle dans un schéma simplifié.
- [ ] **P518** · QCM · Rappel / application — Premier étage au repos : équilibre.
- [ ] **P519** · QCM · Rappel / application — Premier étage à l’inspiration : ouverture puis fermeture.
- [ ] **P520** · QCM · Erreur / limite — Ne pas appliquer un schéma de membrane à tous les modèles.
- [ ] **P521** · QCM · Rappel / application — Second étage à l’inspiration : membrane et levier.
- [ ] **P522** · QCM · Rappel / application — Expiration : soupapes et moustaches.
- [ ] **P523** · QCM · Rappel / application — Bouton de purge : fonction.
- [ ] **P524** · QCM · Rappel / application — Second étage immergé : évacuer l’eau avant inspiration.
- [ ] **P525** · QCM · Rappel / application — Entrée premier étage : prévenir la pénétration d’eau.
- [ ] **P526** · QCM · Comparaison — Détendeur simple versus compensé : rôle de la compensation.
- [ ] **P527** · Basic · Compréhension — MP stable malgré baisse HP : principe de compensation.
- [ ] **P528** · QCM · Rappel / application — Confort fin de bloc : dépend du modèle.
- [ ] **P529** · QCM · Rappel / application — Piston simple : compromis coût, robustesse, environnement.
- [ ] **P530** · QCM · Rappel / application — Piston compensé : compromis confort et conception.
- [ ] **P531** · Basic · Compréhension — Membrane : isolement de mécanismes et conception.
- [ ] **P532** · QCM · Rappel / application — Froid et givrage : choix selon certification du modèle.
- [ ] **P533** · QCM · Erreur / limite — Ne pas mémoriser une généralité commerciale comme une loi physique.
- [ ] **P534** · QCM · Rappel / application — Rinçage : eau douce et entrée protégée selon manuel.
- [ ] **P535** · Basic · Complément — Bouton de purge pendant rinçage : complément à documenter.
- [ ] **P536** · QCM · Rappel / application — Stockage : suivre le manuel, vérifier la consigne de bouchon.
- [ ] **P537** · QCM · Rappel / application — Éviter soleil, chocs et écrasement.
- [ ] **P538** · QCM · Rappel / application — Filtre et facilité d’inspiration : signes à surveiller.
- [ ] **P539** · QCM · Rappel / application — Révision périodique selon constructeur et usage.
- [ ] **P540** · QCM · Rappel / application — Débit continu : causes dans le tableau source à relever.
- [ ] **P541** · QCM · Rappel / application — Fuite de robinetterie : joint et montage, tableau à relever.
- [ ] **P542** · QCM · Rappel / application — Inspiration difficile : pression, ouverture, filtre ou réglage, à confirmer.
- [ ] **P543** · QCM · Rappel / application — Incident de détendeur : priorité à la sécurité de la palanquée.
- [ ] **P544** · QCM · Rappel / application — Tableau de pannes : séparer observation, cause possible et action autorisée.
- [ ] **P545** · QCM · Scénario — Scénario : confusion entre MP et pression délivrée à la bouche.
- [ ] **P546** · QCM · Lecture / repérage — Schéma original des deux étages à produire.

### 17-competences-transversales — Autonomie::Préparation et palanquée

Source : **S2 p.1–2 ; S1 p.3–5, 11–12, 23, 28**. Contrôle : **V15**. Fichier futur : `cards/n2/17-competences-transversales.yaml`.

- [ ] **P547** · QCM · Rappel / application — PE40 : vérifier son propre matériel.
- [ ] **P548** · Basic · Compréhension — PA20 : contrôle croisé des équipiers.
- [ ] **P549** · QCM · Rappel / application — PE40 : comprendre le briefing du GP.
- [ ] **P550** · QCM · Rappel / application — PA20 : planifier avec les équipiers.
- [ ] **P551** · QCM · Rappel / application — Planification : profondeur et durée convenues.
- [ ] **P552** · Basic · Complément — Planification : stock de gaz et réserve, complément nécessaire.
- [ ] **P553** · QCM · Rappel / application — Planification : contraintes de désaturation de chacun.
- [ ] **P554** · QCM · Comparaison — Communication avec le GP versus avec les équipiers.
- [ ] **P555** · QCM · Rappel / application — Code de communication pour les paliers.
- [ ] **P556** · QCM · Rappel / application — Ventilation et stabilisation pendant exploration.
- [ ] **P557** · QCM · Rappel / application — Stabilisation pendant remontée.
- [ ] **P558** · QCM · Rappel / application — Stabilisation au palier.
- [ ] **P559** · QCM · Rappel / application — PE40 : relais de sécurité avant prise en charge du guide.
- [ ] **P560** · QCM · Rappel / application — PA20 : responsabilité collective d’assistance.
- [ ] **P561** · Basic · Complément — Orientation et retour au bateau : compétence citée, cours absent.
- [ ] **P562** · Basic · Complément — Repères naturels : complément à documenter.
- [ ] **P563** · Basic · Complément — Boussole et cap retour : complément à documenter.
- [ ] **P564** · Basic · Complément — Perte de palanquée : procédure absente à obtenir.
- [ ] **P565** · QCM · Rappel / application — Parachute : compétence opérationnelle, support incomplet.
- [ ] **P566** · QCM · Rappel / application — Briefing d’un équipier nouveau : points théoriques connus.
- [ ] **P567** · QCM · Rappel / application — Signaler une difficulté avant aggravation.
- [ ] **P568** · QCM · Rappel / application — Décision d’interrompre selon froid, effort ou air.
- [ ] **P569** · QCM · Scénario — Scénario : autorisation réglementaire mais état personnel défavorable.
- [ ] **P570** · QCM · Scénario — Scénario : guide présent ne dispense pas de surveiller son ordinateur.
- [ ] **P571** · QCM · Scénario — Scénario : ordinateur sans palier mais air insuffisant.
- [ ] **P572** · QCM · Scénario — Scénario : choix collectif de la contrainte la plus protectrice.

### 18-lecture-pannes — Matériel::Pannes et lecture de supports

Source : **S1 p.24–25, 31–34 (figures et tableau)**. Contrôle : **V14**. Fichier futur : `cards/n2/18-lecture-pannes.yaml`.

- [ ] **P573** · QCM · Rappel / application — Entrée d’eau à l’inspiration : embout endommagé.
- [ ] **P574** · QCM · Rappel / application — Entrée d’eau à l’inspiration : membrane, boîtier ou soupape.
- [ ] **P575** · QCM · Rappel / application — Détendeur dur : levier ou impuretés, causes possibles non exclusives.
- [ ] **P576** · QCM · Rappel / application — Débit continu : fuite siège-clapet et dérive de MP, exemple source.
- [ ] **P577** · QCM · Rappel / application — Absence d’air : premier étage bloqué, cause possible non exclusive.
- [ ] **P578** · QCM · Rappel / application — Bulles chambre humide : défaut de joints, hypothèse source.
- [ ] **P579** · Basic · Complément — Fuite fixation sur bloc : joint absent, défectueux ou inadapté.
- [ ] **P580** · QCM · Rappel / application — Flexible endommagé : fuite et vidange rapide.
- [ ] **P581** · QCM · Rappel / application — Réparation interne : confier à une personne qualifiée.
- [ ] **P582** · Basic · Compréhension — Rupture du flexible : lien entre inspection et prévention.
- [ ] **P583** · QCM · Rappel / application — Panne observée ne permet pas de certifier une cause unique.
- [ ] **P584** · QCM · Lecture / repérage — Identifier les chambres sur un schéma original du premier étage.
- [ ] **P585** · QCM · Lecture / repérage — Identifier membrane et levier sur un schéma original du second étage.
- [ ] **P586** · QCM · Lecture / repérage — Reconnaître DIN sur une illustration originale.
- [ ] **P587** · QCM · Lecture / repérage — Reconnaître étrier sur une illustration originale.
- [ ] **P588** · QCM · Lecture / repérage — Lire profondeur, durée, palier, DTR et GPS dans l’extrait MN90.
- [ ] **P589** · QCM · Comparaison — Comparer deux lignes adjacentes de l’extrait MN90.
- [ ] **P590** · QCM · Lecture / repérage — Courbe MN90 illustrée : cas 20 m et 40 min, vérifier édition.
- [ ] **P591** · QCM · Lecture / repérage — Courbe MN90 illustrée : cas 30 m et 10 min, vérifier édition.
- [ ] **P592** · QCM · Lecture / repérage — Courbe MN90 illustrée : ne pas transférer ses valeurs à un ordinateur.

### Reprises complémentaires à répartir dans les fichiers existants

Chaque reprise ci-dessous teste un autre angle ; le rapprochement avec la section sert à
la revue de couverture, pas à imposer un ordre de révision. Même source et contrôle que la section.

- [ ] **P593** · QCM · Comparaison · `04-pression.yaml` — Comparer Pabs à 3 m et à 13 m, puis distinguer différence et rapport.
- [ ] **P594** · QCM · Erreur · `04-pression.yaml` — Un calcul donne 2 bar à 20 m : identifier la pression oubliée.
- [ ] **P595** · Basic · Justification · `04-pression.yaml` — Expliquer pourquoi une remontée de 10 m a un effet relatif différent près de la surface.
- [ ] **P596** · QCM · Erreur · `05-flottabilite.yaml` — Un objet a un poids apparent négatif : réfuter la conclusion « il coule ».
- [ ] **P597** · QCM · Scénario · `05-flottabilite.yaml` — Descente avec gilet inchangé : relier compression du néoprène et effort de stabilisation.
- [ ] **P598** · QCM · Scénario · `05-flottabilite.yaml` — Remontée accélérée avec gilet gonflé : reconnaître la boucle expansion-portance.
- [ ] **P599** · QCM · Comparaison · `05-flottabilite.yaml` — Même équipement au début et à la fin : distinguer changement de masse et volume extérieur du bloc.
- [ ] **P600** · Basic · Justification · `05-flottabilite.yaml` — Expliquer pourquoi un changement de salinité impose un nouveau contrôle de lestage.
- [ ] **P601** · QCM · Erreur · `06-gaz-autonomie.yaml` — Un ballon à 20 m est calculé avec 2 bar : repérer l’emploi de la pression relative.
- [ ] **P602** · QCM · Comparaison · `06-gaz-autonomie.yaml` — Comparer le volume d’un ballon souple et le volume extérieur d’un bloc rigide en descente.
- [ ] **P603** · Basic · Calcul · `06-gaz-autonomie.yaml` — Comparer la consommation ramenée surface à 20 m et 40 m pour le même débit ambiant.
- [ ] **P604** · QCM · Erreur · `06-gaz-autonomie.yaml` — Refuser une durée de plongée planifiée à partir de la vidange complète du bloc.
- [ ] **P605** · QCM · Scénario · `07-barotraumatismes.yaml` — Équilibrage seulement après la douleur : reconnaître le défaut de prévention.
- [ ] **P606** · QCM · Comparaison · `07-barotraumatismes.yaml` — Distinguer équilibrage d’oreille à la descente et ventilation libre à la remontée.
- [ ] **P607** · Basic · Justification · `07-barotraumatismes.yaml` — Relier blocage ventilatoire, gaz piégé et chute de pression sans invoquer l’azote dissous.
- [ ] **P608** · QCM · Scénario · `08-essoufflement.yaml` — Réponse consistant à inspirer toujours plus vite : expliquer le cercle vicieux ventilatoire.
- [ ] **P609** · QCM · Priorité · `08-essoufflement.yaml` — Identifier la première action théorique face à un effort devenu excessif.
- [ ] **P610** · QCM · Erreur · `09-froid.yaml` — Réfuter « il ne frissonne plus, il s’est réchauffé » dans un contexte de dégradation.
- [ ] **P611** · QCM · Erreur · `10-narcose.yaml` — Réfuter « le pourcentage d’azote augmente quand on descend ».
- [ ] **P612** · QCM · Comparaison · `10-narcose.yaml` — Comparer deux plongées de même profondeur avec fatigue et visibilité différentes.
- [ ] **P613** · QCM · Scénario · `10-narcose.yaml` — Consigne simple oubliée à 38 m : reconnaître un changement de comportement à signaler.
- [ ] **P614** · QCM · Comparaison · `11-add.yaml` — Comparer deux durées à même profondeur sans prétendre calculer le risque exact.
- [ ] **P615** · QCM · Comparaison · `11-add.yaml` — Comparer origine des bulles dans ADD et surpression, sans demander un autodiagnostic.
- [ ] **P616** · QCM · Erreur · `11-add.yaml` — Réfuter l’exclusion automatique d’un accident sur la seule base d’un délai.
- [ ] **P617** · QCM · Priorité · `11-add.yaml` — Symptômes après plongée : différencier secours en surface et procédure de remontée anormale.
- [ ] **P618** · QCM · Scénario · `11-add.yaml` — Équipier soulagé sous oxygène : vérifier la poursuite du protocole d’alerte.
- [ ] **P619** · QCM · Erreur · `12-tables.yaml` — Repérer l’inclusion incorrecte de la remontée normale dans le temps fond MN90.
- [ ] **P620** · Basic · Calcul · `12-tables.yaml` — Calculer une durée théorique depuis durée réelle et majoration déjà fournies.
- [ ] **P621** · QCM · Comparaison · `12-tables.yaml` — Vitesse MN90 et alarme d’un ordinateur donné : conserver le contexte de chaque outil.
- [ ] **P622** · QCM · Erreur · `13-ordinateurs.yaml` — Différencier temps écoulé, NDL et DTR sur trois écrans fictifs.
- [ ] **P623** · QCM · Scénario · `13-ordinateurs.yaml` — Prêt d’un ordinateur entre deux plongées : identifier l’historique inadapté.
- [ ] **P624** · QCM · Scénario · `13-ordinateurs.yaml` — Un équipier termine son palier avant les autres : décision collective à expliquer.
- [ ] **P625** · QCM · Comparaison · `14-remontees-anormales.yaml` — Interruption de palier obligatoire versus saut d’un palier de confort.
- [ ] **P626** · QCM · Erreur · `15-gonflage-blocs.yaml` — Ne pas utiliser la pression d’épreuve comme pression de gonflage autorisée.
- [ ] **P627** · Basic · Calcul · `16-detendeurs.yaml` — Avec MP relative fournie, calculer MP absolue à 20 m dans un modèle fictif.
- [ ] **P628** · QCM · Comparaison · `16-detendeurs.yaml` — Distinguer premier étage rincé avec entrée protégée et second étage pouvant prendre l’eau.
- [ ] **P629** · QCM · Priorité · `17-competences-transversales.yaml` — Croiser stock de gaz, temps sans palier et contraintes de remontée dans un briefing fictif.

## Compléments nécessaires pour ne pas donner une fausse impression d’exhaustivité

- [ ] Obtenir la version actuelle du MFT N2 et vérifier la matrice compétences/objectifs.
- [ ] Identifier les textes primaires de réglementation, de suivi des blocs et de signalisation.
- [ ] Obtenir les procédures fédérales actuelles de remontée anormale et de secours.
- [ ] Documenter réserve, demi-tour et gestion collective du gaz ; les calculs du cours vident le bloc.
- [ ] Documenter orientation, perte de palanquée et mise en œuvre du parachute.
- [ ] Documenter les signes et procédures d’assistance attendus, avec un support de formation adapté.
- [ ] Obtenir l’édition complète des tables si des exercices de majoration sont conservés.
- [ ] Choisir un ou plusieurs manuels d’ordinateur pour des écrans pédagogiques précis.
- [ ] Vérifier les modalités techniques d’intégration des illustrations : le builder actuel ne gère
  pas encore une collection de médias embarquée. Prévoir ce travail uniquement si des cartes imagées
  sont retenues ; une version textuelle est possible sans modifier le builder.

Ces tâches ne sont pas comptées comme cartes supplémentaires au total du catalogue.
Aucune nouvelle matière (nitrox complet, navigation détaillée, médecine avancée N3/N4)
à inventer pour atteindre un volume arbitraire.

## Illustrations à créer si retenues

Produire des schémas originaux, sans recopier les figures des supports :

- [ ] Comparaison pression relative/absolue en surface, à 10 m et à 20 m.
- [ ] Trois objets : flottabilité négative, neutre et positive, forces et convention de signe.
- [ ] Ballon souple pendant descente et remontée, hypothèses de Boyle-Mariotte.
- [ ] Oreille avec tympan, oreille moyenne et trompe d’Eustache, validation anatomique.
- [ ] Schéma conceptuel de dissolution/désaturation, explicitement simplifié.
- [ ] Profil carré de table et profil réel d’ordinateur.
- [ ] Écran fictif avec profondeur, NDL, paliers et DTR, sans marque commerciale.
- [ ] Circuit bloc → premier étage → flexible → second étage, avec HP/MP/PA.

## Critères d’acceptation d’une carte

- [ ] Un seul objectif, question autonome, contexte suffisant et français naturel.
- [ ] Source et emplacement précis retrouvables ; contradiction résolue si elle existe.
- [ ] Format adapté : rappel actif pour calcul/justification, QCM crédible pour décision/comparaison.
- [ ] Pour tout calcul : hypothèses explicites, unités et résultat vérifiés indépendamment.
- [ ] Pour QCM : une bonne réponse incontestable ; distracteurs expliquant des erreurs plausibles.
- [ ] Explication apportant une raison, pas seulement la répétition de la bonne réponse.
- [ ] Pas de formulation médicale ou opérationnelle adoptée depuis un support non validé.
- [ ] Pas d’invention de procédure pour une compétence seulement citée dans le flyer.
- [ ] Vérifier la complémentarité des cartes voisines, sans retirer les angles utiles de répétition.
- [ ] `id` permanent, `levels: [N2]`, `fr` obligatoire, tags de thème et d’angle.
- [ ] `status: draft` jusqu’à la revue factuelle et pédagogique.
- [ ] Validation du YAML, schéma JSON cohérent et `make check` réussi.
- [ ] Build de prévisualisation ; affichage recto/verso et mélange des choix contrôlés.

## Suivi final de couverture

Pour chaque section : noter cartes rédigées, cartes revues, cartes publiées, cartes bloquées
par manque de source et cartes écartées avec justification. Conserver le lien entre chaque Pxxx
et les IDs YAML produits. Une carte éventuellement scindée donne plusieurs IDs, une carte écartée
reste visible dans le plan avec sa justification. Le total réel sera recalculé après revue.

Le deck N2 sera prêt lorsque tous les objectifs essentiels couverts par les sources auront
été traités ou explicitement reportés, les contradictions résolues et la couverture comparée au
référentiel choisi. Les cartes culturelles facultatives ne conditionnent pas ce jalon.

## Avancement du chapitre 01

P001–P027 réalisés : 28 cartes (P020 scindé en deux). Source actualisée : MFT N2 mai 2026,
Code du sport A322-73 depuis octobre 2025. Détail dans docs/reviews/01-prerogatives.md.
