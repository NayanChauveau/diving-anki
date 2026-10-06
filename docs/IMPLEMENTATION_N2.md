# Plan d’implémentation du deck Plongée N2

Plan établi le 5 octobre 2026. Chapitre 01 resserré : 21 cartes actives pour P001–P027 ; certaines lignes sont fusionnées ou retirées.
Voir [la revue et la correspondance des IDs](reviews/01-prerogatives.md).

## Objectif et volume

Préparer un deck français solide, avec rappel, compréhension, calcul, correction d’erreur,
lecture de schéma et mise en situation. Après revue globale, le catalogue contient **325 objectifs
retenus**, dont 7 nouveaux exercices de gaz à documenter. Ils proviennent de 629 propositions
initiales : 318 conservées, 297 fusionnées, 11 écartées et 3 transformées en tâches éditoriales.
Ce sont des objectifs de préparation, pas un quota ni un nombre définitif de cartes : P020
correspond déjà à deux cartes. Le chapitre 01 conserve ses **21 cartes actives**.

Voir [l’audit de toute la préparation](reviews/PREPARATION_GLOBALE.md) pour les décisions
par chapitre et chaque correspondance de fusion ; aucun identifiant ancien n’est réattribué.

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

Une case du catalogue représente un objectif à concevoir puis à valider. Les variantes fusionnées
se trouvent dans l’audit ; ne pas les recréer comme cartes supplémentaires.
Chaque ligne a un ID de plan (Pxxx), un format et un angle. Les numéros sont stables dans ce plan.
Les futurs IDs YAML seront permanents, par exemple `n2-pression-pabs-6m-001` ; ne pas utiliser
le seul numéro de ligne comme identité sémantique d’une carte publiée.

- `QCM` : une seule bonne réponse, distracteurs plausibles, explication du mécanisme ou de l’erreur.
- `Basic` : réponse courte activement rappelée ; utile pour définitions et justification.
- `Cloze` : seulement formule, relation ou repère validé, une suppression utile par carte.
- `Calcul` / `Scénario` / `Comparaison` / `Erreur` / `Lecture` : angles ; pas de nouveaux types YAML.
- `Vxx` : contrôle éditorial de la section, à appliquer aux lignes concernées avant publication.
- `Complément` : objectif prévu mais source insuffisante ; obtenir une référence avant rédaction.
- Les trivia historiques et statistiques ont été écartés dans l’audit ; ne pas les réintroduire pour augmenter le volume.

Toutes les futures cartes ciblent `levels: [N2]`, sont en `fr` et commencent `draft`.
Ne pas attribuer N3/N4 automatiquement. Un sujet partagé entre S1 et S3 n’est pas dupliqué
mot pour mot : il est fusionné puis décliné en angles complémentaires.

## Pertinence et répétition pédagogique

**Un fait simple, une carte.** Anki assure ensuite sa répétition dans le temps. Une définition
de sigle n’a pas besoin de sa carte inverse, d’une paraphrase et d’un scénario qui change seulement
un chiffre. Les précisions utiles vont dans l’explication, sans transformer le recto en liste à réciter.

**Un raisonnement complexe, plusieurs tâches distinctes.** Conserver les calculs direct et inverse,
les conversions, l’erreur de modèle, les phases de profondeur différente et les contraintes collectives
lorsqu’ils exigent une opération ou une décision nouvelle. Une courte série de valeurs variées aide aussi à automatiser une méthode de calcul ;
combiner profondeurs, résultats entiers et décimaux, puis opérations directes et inverses.

Pour un accident, mécanisme, reconnaissance, prévention et priorité de réponse peuvent être séparés.
Un scénario reste utile s’il oblige à hiérarchiser une action avec une incertitude ou une contrainte ;
un simple habillage d’une définition ne suffit pas. Ne pas multiplier les cartes de chaque symptôme
isolé ni demander de longues listes. Les familles de signes sont travaillées par cas courts.

Avant rédaction, comparer l’objectif à **tout le deck**, y compris les autres chapitres, puis écrire
l’apport de la nouvelle carte en une phrase. Sans apport distinct, fusionner ou écarter.
Lire [les règles de conception](CARD_DESIGN.md) et consigner les décisions dans la revue du chapitre.

## Ordre d’implémentation

1. Résoudre les erreurs de physique V04/V05, fixer le modèle simplifié et les conventions d’unités.
2. Rédiger pressions, flottabilité et gaz ; tester les calculs avec une résolution indépendante.
3. Valider V01–V03, puis rédiger prérogatives et organisation.
4. Valider V07–V09 avec les références appropriées, puis accidents et prévention.
5. Valider V10–V12, puis tables, ordinateurs et remontées anormales.
6. Valider V13/V14, puis blocs et détendeurs ; produire les schémas originaux.
7. Préparation collective et scénarios transversaux ; intégrer les compléments obtenus.
8. Reprises retenues seulement si elles ajoutent une difficulté ; revoir la couverture sans viser un volume.

Un lot peut contenir 15 à 25 cartes d’un même thème. Après chaque lot : revue factuelle,
revue pédagogique, `make check`, build avec drafts et inspection dans Anki.
Le passage à `reviewed` n’est autorisé qu’après revue ; les contrôles techniques seuls ne suffisent pas.

## Registre des vérifications avant rédaction normative

Les observations suivantes comparent les documents fournis ; elles ne constituent pas une
vérification de la réglementation ou des protocoles en vigueur. Cette recherche primaire
fait partie de l’implémentation future. Ne pas choisir arbitrairement un support en cas de conflit.

- [x] **V01** — Âges et aptitudes : S2 (flyer 2021) annonce PE40 16 ans et PA20 18 ans ; S1 (2024) distingue PE40 14 ans, PA20/N2 15 ans et exercice autonome 16 ans. Vérifier MFT FFESSM et Code du sport en vigueur avant toute réponse normative ; conserver distinction formation/certification/exercice.

- [x] **V02** — Organisation et équipements : vérifier les articles cités, leur version et le champ exact (milieu naturel, circuit ouvert, air, exploration). S1 introduit le GP avec un article définissant surtout la palanquée : ne pas confondre citation et définition du rôle.

- [x] **V03** — CACI, licence, chasse, signalisation et patrimoine : vérifier textes fédéraux et règles applicables au lieu. Les chiffres de licenciés, structures et gouvernance sont datés et de faible priorité. La reconnaissance CMAS ne donne pas une autorisation universelle de plonger.

- [x] **V04** — Erreur confirmée dans S3 p.3, exercice à 6 m : le corrigé indique 2,5 bar alors que sa propre formule 1 + 6/10 donne 1,6 bar. kg n’est pas une unité de force ; kgf/cm² et bar ne sont pas strictement identiques. Les calculs doivent annoncer le modèle pédagogique simplifié.

- [x] **V05** — Incohérence confirmée S3 p.6 : eau de mer plus porteuse, mais le support propose de retirer du lest lors du passage eau douce vers mer. Vérifier puis corriger la direction ; aucun décalage fixe universel. Les différences acier/alu, 12/15 L et bloc plein/vide dépendent du matériel. Le lest ajouté a lui-même un volume : préciser si négligé dans les exercices.

- [x] **V06** — Boyle-Mariotte : température et quantité de gaz constantes, pressions absolues. Le stock calculé avec la pression nominale est une approximation de cours, pas une planification réelle. Tous les calculs sans réserve doivent être nommés « théoriques » ; obtenir une source pour les règles opérationnelles de réserve et de retour.

- [x] **V07** — Accidents, froid et essoufflement : vérifier mécanismes et conduites avec les supports de formation/secourisme actuels. Ne pas adopter automatiquement rinçage nasal à l’eau de mer, collyre, reprise de plongée après un délai fixe, boisson à toute victime, Valsalva forcé ou consigne de réimmersion sans contexte. Le tableau p.16 et les paragraphes p.13–16 ne sont pas entièrement équivalents.

- [x] **V08** — Narcose : seuils non universels ; ne pas reprendre « constante à 50 m » ni « pas de prévention » comme absolus. Composition détaillée de l’air et rôle des différents gaz à vérifier. Ne pas étendre ces documents à une formation nitrox ou à des limites de toxicité absentes.

- [x] **V09** — ADD : vérifier symptômes et protocole de secours actuel, installation de la victime, débit et administration O2, hydratation, avion/altitude et effort après plongée. Ne pas enseigner un délai de 12 h comme exclusion ni une formule obligatoire d’hydratation. Le résumé physiologique sur les bulles est simplifié ; éviter de présenter tout retour de l’azote comme une formation nécessaire de microbulles.

- [x] **V10** — MN90 : identifier l’édition, domaine d’emploi et tableaux complets avant exercices chiffrés. S1 p.25 montre un extrait et non les tables de calcul de successives. S1 p.24 contient une courbe illustrée : confirmer valeurs et conventions, notamment frontières d’intervalles. Pas d’utilisation comme consigne universelle de plongée.

- [x] **V11** — Ordinateurs : vitesses, fréquence de mesure, verrouillage, autonomie batterie, modes et algorithmes dépendent du modèle. Ne pas retenir « 24 h de verrouillage » ou « 2–3 plongées max » comme universels. Vérifier les écrans originaux et le manuel ; tenir compte des obligations de tous les équipiers.

- [x] **V12** — Remontées anormales : S1 juxtapose procédures MN90 et préconisations fédérales dites nouvelles en 2024. Retrouver le texte primaire et sa version avant rédiger des cartes d’action (seuils, délais, profondeurs, paliers, réimmersion, observation). Aucune carte de réimmersion prête à publier sur le seul extrait.

- [x] **V13** — Blocs : S1 mentionne 2 ans / 5 ans avec TIV et « ne pas transporter sous pression ». Vérifier réglementation des équipements sous pression, régime TIV et consignes de transport actuels. Ne pas publier ces formulations telles quelles. Gonflage réservé aux opérateurs habilités.

- [x] **V14** — Détendeurs : schémas et tableaux décrivent des conceptions particulières. Confirmer différences de MP, compensation, froid, entretien et stockage au manuel constructeur. Panne observée ≠ cause certaine ; ne pas transformer la colonne réparation en tutoriel de démontage. Les modèles commerciaux sont des exemples datés, pas une liste à apprendre.

- [ ] **V15** — S2 énonce des compétences sans cours détaillé pour orientation, assistance et planification. Les cartes fondées sur ce flyer peuvent tester les objectifs et responsabilités ; obtenir une source supplémentaire pour les procédures techniques. Les cartes ne valident pas la maîtrise pratique.

## Répartition et fichiers proposés

Les fichiers proposés restent dans `cards/n2/`, un fichier par chapitre. Les sous-decks sont
français ; le builder ajoutera `Plongée::N2::` devant les chemins indiqués.

| Chapitre | Sous-deck | Objectifs retenus |
| --- | --- | ---: |
| `01-prerogatives.yaml` | Réglementation | 20 |
| `02-organisation.yaml` | Réglementation | 20 |
| `03-documents-environnement.yaml` | Réglementation | 14 |
| `04-pression.yaml` | Physique | 18 |
| `05-flottabilite.yaml` | Physique | 23 |
| `06-gaz-autonomie.yaml` | Physique | 28 |
| `07-barotraumatismes.yaml` | Prévention des accidents | 21 |
| `08-essoufflement.yaml` | Prévention des accidents | 13 |
| `09-froid.yaml` | Prévention des accidents | 11 |
| `10-narcose.yaml` | Prévention des accidents | 14 |
| `11-add.yaml` | Désaturation | 34 |
| `12-tables.yaml` | Désaturation | 18 |
| `13-ordinateurs.yaml` | Désaturation | 18 |
| `14-remontees-anormales.yaml` | Désaturation | 10 |
| `15-gonflage-blocs.yaml` | Matériel et préparation | 18 |
| `16-detendeurs.yaml` | Matériel et préparation | 19 |
| `17-competences-transversales.yaml` | Matériel et préparation | 16 |
| `18-lecture-pannes.yaml` | Matériel et préparation | 6 |
| Reprises complémentaires, réparties dans les chapitres existants | Plusieurs | 4 |
| **Total objectifs retenus** | | **325** |

## Catalogue des cartes à produire

Cocher seulement après rédaction et validation de la carte correspondante. Dans chaque section,
les références et vérifications annoncées valent pour toutes les cartes. En cas de fusion,
intégrer aussi les références et contrôles de l’objectif absorbé indiqués dans l’audit ; affiner ensuite
`review.sources` avec le paragraphe ou la figure précis pendant la rédaction.

### 01-prerogatives — Réglementation

Source : **S1 p.3–4 ; S2 p.1–2**. Contrôle : **V01**. Fichier futur : `cards/n2/01-prerogatives.yaml`.

- [x] **P001** · QCM · Rappel / application — N2 : articulation des aptitudes PA20 et PE40.
- [x] **P004** · QCM · Rappel / application — Qualifications PA20 et PE40 acquises séparément.
- [x] **P006** · QCM · Comparaison — Distinguer autonomie et absence de directeur de plongée.
- [x] **P007** · QCM · Rappel / application — Composition d’une palanquée PA20 : nombre d’équipiers.
- [x] **P008** · QCM · Rappel / application — Compétences minimales des équipiers PA20.
- [x] **P010** · QCM · Scénario — Scénario : N2 demandant une exploration autonome à 30 m.
- [x] **P012** · QCM · Scénario — Scénario : N2 autonome avec un équipier aux aptitudes plus restrictives.
- [x] **P013** · QCM · Rappel / application — Âge d’entrée en formation PE40.
- [x] **P014** · QCM · Rappel / application — Âge de délivrance PA20 et N2.
- [x] **P016** · QCM · Comparaison — Distinction formation, certification et exercice des prérogatives.
- [x] **P017** · QCM · Rappel / application — Autorisation du représentant légal pour un mineur autonome.
- [x] **P018** · QCM · Rappel / application — Information des équipiers de la présence d’un mineur.
- [x] **P019** · QCM · Rappel / application — PE40 mineur : absence de palier obligatoire.
- [x] **P020** · QCM · Rappel / application — PE40 mineur : nombre de plongées et intervalle.
- [x] **P021** · QCM · Rappel / application — PE40 mineur : profondeur de la seconde après une première profonde.
- [x] **P022** · QCM · Rappel / application — Conditions communes : licence et CACI.
- [x] **P023** · QCM · Rappel / application — Prérequis N1 ou équivalence.
- [x] **P024** · QCM · Rappel / application — Expérience préalable en milieu naturel.
- [x] **P026** · QCM · Rappel / application — Double certification FFESSM et CMAS deux étoiles.
- [x] **P027** · QCM · Rappel / application — Reconnaissance internationale et règles locales : éviter la promesse de droit universel.

### 02-organisation — Réglementation

Source : **S1 p.4–5 ; S2 p.1–2**. Contrôle : **V02**. Fichier futur : `cards/n2/02-organisation.yaml`.

- [x] **P028** · QCM · Rappel / application — Définir une palanquée par la plongée effectuée ensemble ; expliquer les paramètres communs.
- [x] **P030** · QCM · Rappel / application — Palanquée avec mélanges ou aptitudes différents : contrainte la plus restrictive.
- [x] **P032** · QCM · Rappel / application — DP : caractéristiques fixées pour la plongée.
- [x] **P033** · QCM · Rappel / application — DP : dispositions de sécurité.
- [x] **P035** · QCM · Rappel / application — Lire une fiche de sécurité : identifier participants et paramètres prévus/réalisés.
- [x] **P038** · QCM · Rappel / application — GP : conduite d’une exploration PE40.
- [x] **P039** · QCM · Rappel / application — Équipiers PA20 : sécurité collective.
- [x] **P041** · QCM · Rappel / application — Plan de secours : modalités d’alerte et coordonnées.
- [x] **P043** · QCM · Rappel / application — Moyen de communication et contexte d’emploi de la VHF.
- [x] **P044** · QCM · Rappel / application — Eau potable et couverture isothermique à disposition.
- [x] **P045** · QCM · Rappel / application — Oxygénothérapie : capacité adaptée à l’attente des secours.
- [x] **P047** · QCM · Rappel / application — Fiche d’évacuation : fonction.
- [x] **P048** · QCM · Rappel / application — Bloc de secours équipé et adapté au mélange.
- [x] **P049** · QCM · Rappel / application — Moyen de rappel des plongeurs depuis le bateau.
- [x] **P050** · QCM · Rappel / application — Tablette de notation et tables disponibles selon le contexte.
- [x] **P052** · QCM · Rappel / application — Système gonflable pour regagner et tenir la surface.
- [x] **P053** · QCM · Rappel / application — Source d’air pour un équipier sans partage d’embout.
- [x] **P054** · QCM · Compréhension — Contrôle des paramètres personnels en autonomie ou au-delà de 20 m encadré.
- [x] **P055** · QCM · Rappel / application — Équipement spécifique de l’encadrant : deux sorties et deux détendeurs.
- [x] **P056** · QCM · Rappel / application — Parachute : équipement de la palanquée.

### 03-documents-environnement — Réglementation

Source : **S1 p.5–7 ; S2 p.2**. Contrôle : **V03**. Fichier futur : `cards/n2/03-documents-environnement.yaml`.

- [x] **P059** · Comparaison — Distinguer brevet, licence et CACI. Couvert par P022/P023, pas de nouvelle carte.
- [x] **P061** · QCM · Rappel / application — Validité du CACI et médecin habilité selon le contexte.
- [x] **P063** · QCM · Rappel / application — Licence : affiliation et participation aux activités.
- [x] **P064** · QCM · Rappel / application — Licence : responsabilité civile.
- [x] **P069** · Basic · Rappel / application — Zones interdites et dérogations locales.
- [x] **P070** · Basic · Rappel / application — Prélèvement au fond et respect du milieu.
- [x] **P071** · QCM · Rappel / application — Objet archéologique : laisser en place.
- [x] **P073** · QCM · Comparaison — Chasse sous-marine et scaphandre : distinguer les interdictions.
- [x] **P074** · QCM · Rappel / application — Signalisation depuis un bateau.
- [x] **P076** · Basic · Rappel / application — Distance de sécurité des navires : règle locale à vérifier.
- [x] **P077** · Application — Respect des prérogatives. Couvert par P010/P012, pas de nouvelle carte.
- [x] **P078** · Basic · Rappel / application — Requalification des blocs : responsabilité.
- [x] **P079** · Basic · Rappel / application — Identifier le rôle de la FFESSM et situer club, structure et commissions en explication ; éviter les listes à réciter.
- [x] **P080** · Basic · Compréhension — Signification et rôle de la CMAS.

### 04-pression — Physique

Source : **S1 p.9–10 ; S3 p.2–3 (imprimées 4–5)**. Contrôle : **V04**. Fichier futur : `cards/n2/04-pression.yaml`.

- [x] **P096** · Cloze · Relation — Relation P = F / S.
- [x] **P097** · Basic · Compréhension — Expliquer l’effet de la force et de la surface sur la pression à partir d’un seul exemple concret.
- [x] **P101** · QCM · Rappel / application — Unité usuelle en plongée : bar.
- [x] **P102** · QCM · Comparaison — Distinguer masse, force et pression.
- [x] **P103** · Basic · Compréhension — Pression atmosphérique : origine.
- [x] **P105** · QCM · Rappel / application — Altitude : évolution qualitative de la pression atmosphérique.
- [x] **P106** · QCM · Rappel / application — Météo : variation qualitative de la pression atmosphérique.
- [x] **P107** · Basic · Compréhension — Pression hydrostatique : origine.
- [x] **P110** · QCM · Rappel / application — Calculer la pression absolue en distinguant pression atmosphérique et hydrostatique ; annoncer le modèle simplifié.
- [x] **P111** · QCM · Rappel / application — À même profondeur : pression identique dans le modèle.
- [x] **P114** · Basic · Calcul — Phyd à 3 m.
- [x] **P118** · Couvert par P110 — Calcul absolu à 6 m et correction du support ; pas de carte supplémentaire.
- [x] **P123** · Basic · Calcul — Profondeur correspondant à 1,5 bar absolu.
- [x] **P126** · Basic · Calcul — Profondeur correspondant à 2 bars relatifs.
- [x] **P127** · QCM · Erreur / limite — Erreur : ajouter deux fois la pression atmosphérique.
- [x] **P128** · QCM · Erreur / limite — Erreur : appliquer une pression relative à Boyle-Mariotte.
- [x] **P129** · QCM · Comparaison — Comparer les rapports de pression 0–10 m et 10–20 m.
- [x] **P132** · Couvert par P101 — Reconnaître les unités de pression, sans carte supplémentaire ni conversions à mémoriser.

### 05-flottabilite — Physique

Source : **S1 p.8–9 ; S3 p.4–6 (imprimées 6–8)**. Contrôle : **V05**. Fichier futur : `cards/n2/05-flottabilite.yaml`.

- [x] **P133** · QCM · Comparaison — Poids réel et poids apparent : distinction.
- [x] **P134** · QCM · Rappel / application — Poussée d’Archimède : direction et sens.
- [x] **P136** · Cloze · Relation — Formule du poids apparent.
- [x] **P138** · QCM · Rappel / application — Déduire coule / neutre / remonte du signe du poids apparent avec la convention fournie.
- [x] **P142** · Basic · Calcul — Objet de 5 kg et 3 L : calcul.
- [x] **P145** · Basic · Calcul — Objet de 8 kg et 5 L : lest ou portance nécessaires.
- [x] **P146** · Basic · Calcul — Caisson de 1,5 kg et 3 L : neutralisation simplifiée.
- [x] **P147** · Basic · Compréhension — Volume déplacé doublé à poids fixe : effet.
- [x] **P149** · Couvert par P133 — Pourquoi un bloc paraît moins lourd sous l’eau.
- [x] **P151** · QCM · Rappel / application — Écrasement du néoprène à la descente.
- [x] **P152** · Couvert par P151 — Expansion du néoprène à la remontée, dans l’explication du mécanisme.
- [x] **P154** · QCM · Rappel / application — Gilet gonflé : volume et poussée.
- [x] **P155** · QCM · Rappel / application — Poumon ballast : inspiration et flottabilité.
- [x] **P157** · QCM · Rappel / application — Poumon ballast et ventilation continue : ne pas enseigner l’apnée.
- [x] **P158** · QCM · Rappel / application — Bloc plein et bloc consommé : différence de masse.
- [x] **P162** · QCM · Rappel / application — Changement d’épaisseur de combinaison : réévaluer.
- [x] **P163** · QCM · Rappel / application — Eau salée plus porteuse que l’eau douce.
- [x] **P166** · QCM · Rappel / application — Noter configuration et lestage dans le carnet.
- [x] **P168** · QCM · Rappel / application — Parachute tenu au gonflage : risque d’être entraîné.
- [x] **P169** · Basic · Compréhension — Perte de lest : mécanisme de remontée.
- [x] **P170** · QCM · Rappel / application — Sur-lestage : efforts et consommation.
- [x] **P171** · Couvert par P172 — Sous-lestage en fin de plongée, traité dans le scénario.
- [x] **P172** · QCM · Scénario — Scénario de stabilisation au palier avec un bloc allégé.

### 06-gaz-autonomie — Physique

Source : **S1 p.10–12**. Contrôle : **V06**. Fichier futur : `cards/n2/06-gaz-autonomie.yaml`.

- [x] **P175** · QCM · Rappel / application — Boyle-Mariotte : relation inverse volume-pression.
- [x] **P176** · QCM · Rappel / application — Conditions du modèle : température et quantité de gaz constantes.
- [x] **P179** · Basic · Calcul — Calcul direct de volume d’un gaz souple en descente ; température et quantité de gaz constantes.
- [x] **P182** · Basic · Calcul — Gaz de 2 L à 20 m : volume en surface.
- [x] **P183** · Basic · Calcul — Gaz de 4 L à 10 m : volume à 30 m.
- [x] **P184** · QCM · Comparaison — Comparer expansion 10–0 m et 20–10 m.
- [x] **P185** · QCM · Rappel / application — Bloc rigide et ballon souple : ne pas confondre volumes.
- [x] **P186** · QCM · Rappel / application — Gilet à la descente : compensation de compression.
- [x] **P187** · QCM · Rappel / application — Gilet à la remontée : purge et expansion.
- [x] **P188** · QCM · Rappel / application — Masque à la descente : apport d’air.
- [x] **P189** · QCM · Rappel / application — Oreille à la descente : équilibrage.
- [x] **P190** · QCM · Rappel / application — Détendeur : gaz délivré à la pression ambiante.
- [x] **P193** · Basic · Calcul — Convertir un débit ambiant en consommation ramenée surface à une profondeur donnée ; unités explicites.
- [x] **P195** · Basic · Calcul — Calculer le stock théorique depuis volume intérieur et pression du bloc ; hypothèses explicites.
- [x] **P197** · Basic · Calcul — Calculer une autonomie théorique à profondeur constante ; identifier ce que le modèle omet.
- [x] **P200** · QCM · Comparaison — Rapport d’autonomie surface versus 40 m.
- [x] **P201** · Basic · Compréhension — Pourquoi les exemples sans réserve ne constituent pas une planification.
- [x] **P202** · Couvert par P201 — Air des phases de retour, remontée et paliers inclus dans les besoins à prévoir.
- [x] **P203** · QCM · Rappel / application — Effort, stress et froid : limites de la consommation constante.
- [x] **P205** · Basic · Complément — Complément à documenter : calcul inverse d’une chute de pression.
- [x] **P206** · Basic · Complément — Complément à documenter : comparer deux équipiers avant le demi-tour.

Réserve et calculs composés : **complément BSAC consulté le 6 octobre 2026 (V06)** ; voir la revue du chapitre. Les nombres
ci-dessous sont des données d’exercice, jamais une réserve ou une procédure universelle.
Toute phase omise limite le résultat au modèle annoncé ; pas d’autonomie opérationnelle implicite.

- [x] **P630** · Basic · Calcul · Complément — Calculer le gaz théoriquement utilisable d’un bloc de 12 L de 200 à 70 bar, réserve de 70 bar imposée dans l’énoncé ; distinguer stock total et stock utilisable.
- [x] **P631** · Basic · Calcul · Complément — Avec stock utilisable et débit surface donnés, calculer une durée à 20 m ; convertir avec la pression absolue avant la division.
- [x] **P632** · Basic · Calcul inverse · Complément — Retrouver la pression minimale initiale pour une phase à profondeur constante, avec durée, débit surface, volume de bloc et réserve imposés.
- [x] **P633** · Basic · Calcul par phases · Complément — Additionner le gaz nécessaire pour deux phases à profondeurs constantes différentes, durées et débits fournis ; phases fictives, pas une consigne de remontée.
- [x] **P634** · Basic · Comparaison · Complément — Comparer une même réserve en bar dans des blocs de 12 et 15 L ; expliquer pourquoi elle ne représente pas le même volume de gaz.
- [x] **P635** · Basic · Calcul / équipiers · Complément — Calculer le besoin théorique de deux équipiers respirant sur le même stock durant une phase fictive ; débits distincts donnés, puis comparer au stock disponible.
- [x] **P636** · Basic · Erreur / marge · Complément — Recalculer un besoin avec un débit augmenté fourni dans l’énoncé ; expliquer pourquoi une autonomie calculée au repos ne suffit pas pour une situation d’effort.

### 07-barotraumatismes — Prévention des accidents

Source : **S1 p.12–16**. Contrôle : **V07**. Fichier futur : `cards/n2/07-barotraumatismes.yaml`.

- [x] **P207** · Basic · Compréhension — Barotraumatisme : mécanisme général.
- [x] **P211** · Basic · Compréhension — Placage du masque : effet ventouse.
- [x] **P215** · QCM · Rappel / application — Sinus : cavités et communication avec le nez.
- [x] **P218** · QCM · Rappel / application — Sinus : signes d’alerte.
- [x] **P220** · QCM · Rappel / application — Sinus : ne pas forcer devant une douleur.
- [x] **P221** · Basic · Compréhension — Blocage des sinus à la remontée et nécessité d’une évaluation ; pas de redescente automatique chiffrée.
- [x] **P224** · QCM · Rappel / application — Trompe d’Eustache : communication et équilibrage.
- [x] **P226** · Couvert par P189 (chapitre 06) — Équilibrage précoce et doux, arrêt de descente en cas d’échec ; anatomie complétée par P224.
- [x] **P230** · QCM · Rappel / application — Rhume et efficacité de l’équilibrage.
- [x] **P231** · QCM · Rappel / application — Descente tête haute : intérêt décrit.
- [x] **P233** · QCM · Rappel / application — Différence entre les deux oreilles : vertige alternobarique.
- [x] **P236** · Basic · Compréhension — Pourquoi les bouchons non adaptés posent problème.
- [x] **P237** · QCM · Rappel / application — Dents : poche de gaz et obstruction.
- [x] **P239** · Basic · Application — Douleur dentaire à la remontée : contrôle dentaire après la plongée avant reprise ; pas de redescente automatique.
- [x] **P240** · QCM · Rappel / application — Gaz digestifs : expansion à la remontée.
- [x] **P243** · QCM · Rappel / application — Expliquer la surpression pulmonaire par gaz piégé et baisse de pression ; ne pas invoquer la dissolution d’azote.
- [x] **P245** · QCM · Rappel / application — Surpression pulmonaire possible près de la surface.
- [x] **P246** · Couvert par P157 (chapitre 05) et P245 — Respiration libre et risque près de la surface.
- [x] **P249** · QCM · Rappel / application — Identifier des signes respiratoires suspects après plongée ; ne pas demander un diagnostic certain.
- [x] **P250** · QCM · Rappel / application — Surpression : signes neurologiques.
- [x] **P252** · QCM · Rappel / application — Suspicion de surpression : alerte et oxygène selon protocole.

### 08-essoufflement — Prévention des accidents

Source : **S1 p.17**. Contrôle : **V07**. Fichier futur : `cards/n2/08-essoufflement.yaml`.

- [x] **P261** · QCM · Rappel / application — Profondeur et effort ventilatoire.
- [x] **P262** · QCM · Rappel / application — Expliquer le cercle vicieux de l’essoufflement et pourquoi accélérer sa respiration ne suffit pas.
- [x] **P263** · QCM · Rappel / application — Effort excessif : facteur déclenchant.
- [x] **P265** · QCM · Rappel / application — Détendeur, robinet et ventilation : causes possibles.
- [x] **P266** · QCM · Rappel / application — Manque d’entraînement et mauvaise forme.
- [x] **P267** · QCM · Rappel / application — Air pollué : facteur cité à vérifier.
- [x] **P268** · QCM · Rappel / application — Signes de respiration haletante.
- [x] **P270** · QCM · Rappel / application — Risques de panique et d’arrachement d’embout.
- [x] **P272** · QCM · Rappel / application — Premiers signes : arrêter l’effort et prévenir.
- [x] **P274** · QCM · Rappel / application — Remontée assistée contrôlée : objectif.
- [x] **P277** · QCM · Rappel / application — Éviter de lutter contre un courant.
- [x] **P279** · QCM · Scénario — Scénario : réduire profondeur sans ignorer les autres contraintes.
- [x] **P280** · QCM · Rappel / application — Prise en charge en surface : protocole à vérifier.

### 09-froid — Prévention des accidents

Source : **S1 p.17–18**. Contrôle : **V07**. Fichier futur : `cards/n2/09-froid.yaml`.

- [x] **P281** · QCM · Rappel / application — Équilibre entre chaleur produite et perdue.
- [x] **P283** · QCM · Rappel / application — Repérer une dégradation liée au froid à partir d’un petit tableau de signes contextualisés.
- [x] **P286** · QCM · Rappel / application — Disparition progressive des frissons : pas un signe rassurant.
- [x] **P288** · QCM · Rappel / application — Froid : signaler et terminer la plongée.
- [x] **P289** · QCM · Rappel / application — Protection adaptée : combinaison, cagoule et chaussons.
- [x] **P291** · QCM · Rappel / application — Fatigue et alimentation : facteurs à considérer.
- [x] **P292** · QCM · Rappel / application — Froid, essoufflement et narcose : interaction.
- [x] **P293** · QCM · Rappel / application — Sortie : sécher et protéger du vent.
- [x] **P295** · Basic · Scénario — Hypothermie avec confusion : manipulations douces, sans friction ; boisson non alcoolisée couverte avec P296.
- [x] **P296** · QCM · Rappel / application — Boisson : conditions de conscience et déglutition à vérifier.
- [x] **P298** · QCM · Scénario — Scénario : doigts maladroits au moment du parachute.

### 10-narcose — Prévention des accidents

Source : **S1 p.18–19**. Contrôle : **V08**. Fichier futur : `cards/n2/10-narcose.yaml`.

- [x] **P299** · QCM · Rappel / application — Composition simplifiée de l’air 80/20.
- [x] **P302** · QCM · Rappel / application — Calculer une pression partielle avec fraction et pression absolue ; comprendre la somme en explication.
- [x] **P304** · Basic · Calcul — Calcul PpO2 à 30 m dans le modèle 20 %.
- [x] **P306** · Basic · Calcul — Calcul PpN2 à 40 m.
- [x] **P307** · QCM · Rappel / application — Pourcentage constant et pression partielle croissante.
- [x] **P308** · Basic · Compréhension — Narcose : lien avec la profondeur et les gaz.
- [x] **P309** · QCM · Rappel / application — Comprendre la variabilité de la narcose ; ne pas transformer une profondeur en seuil universel.
- [x] **P313** · QCM · Rappel / application — Attention et mémoire diminuées.
- [x] **P316** · QCM · Rappel / application — Fatigue, anxiété et manque d’expérience récente.
- [x] **P319** · QCM · Rappel / application — Médicaments : facteur cité à vérifier.
- [x] **P321** · Basic · Compréhension — Réduire la profondeur sous contrôle.
- [x] **P324** · QCM · Scénario — Scénario : euphorie prise pour un signe de bonne forme.
- [x] **P325** · QCM · Scénario — Scénario : équipier inhabituellement lent à répondre.
- [x] **P326** · QCM · Comparaison — Comparer narcose pendant immersion et symptômes après sortie.

### 11-add — Désaturation

Source : **S1 p.20–23**. Contrôle : **V09**. Fichier futur : `cards/n2/11-add.yaml`.

- [x] **P328** · QCM · Rappel / application — Loi de Henry : relation qualitative avec la pression.
- [x] **P330** · QCM · Rappel / application — Analogie eau gazeuse : dépressurisation.
- [x] **P333** · QCM · Rappel / application — Profondeur et charge en azote.
- [x] **P334** · QCM · Rappel / application — Durée d’exposition et charge en azote.
- [x] **P335** · QCM · Rappel / application — Irrigation et différences entre tissus.
- [x] **P336** · QCM · Rappel / application — Élimination pendant remontée et après sortie.
- [x] **P337** · Basic · Compréhension — Rôle de la ventilation et des poumons.
- [x] **P338** · QCM · Rappel / application — Remontée rapide et formation de bulles.
- [x] **P341** · QCM · Rappel / application — Effort et froid : facteurs de risque à contextualiser.
- [x] **P342** · Basic · Compréhension — ADD et surpression pulmonaire : mécanismes différents.
- [x] **P343** · QCM · Rappel / application — ADD malgré le respect affiché du moyen de désaturation.
- [x] **P344** · QCM · Rappel / application — Apparition des signes immédiate ou retardée.
- [x] **P346** · QCM · Rappel / application — Manifestations cutanées : reconnaissance.
- [x] **P350** · QCM · Rappel / application — Oreille interne : vertiges et troubles auditifs.
- [x] **P351** · QCM · Rappel / application — Reconnaître des signes neurologiques suspects après plongée ; choisir l’alerte plutôt que l’autodiagnostic.
- [x] **P354** · QCM · Rappel / application — Fatigue inhabituelle et changement de comportement.
- [x] **P355** · QCM · Rappel / application — Signes respiratoires et douleur thoracique.
- [x] **P358** · QCM · Rappel / application — Déclencher les secours sans attendre une certitude.
- [x] **P359** · Basic · Compréhension — Oxygène : rôle et protocole applicable.
- [x] **P360** · QCM · Rappel / application — Installation de la victime : posture à vérifier.
- [x] **P361** · QCM · Rappel / application — Hydratation : conditions à vérifier, pas de règle universelle.
- [x] **P362** · QCM · Rappel / application — Paramètres de plongée à transmettre.
- [x] **P365** · QCM · Rappel / application — Surveiller les équipiers.
- [x] **P366** · QCM · Erreur / limite — Ne pas réimmerger une victime suspecte.
- [x] **P367** · QCM · Rappel / application — Amélioration apparente : ne pas interrompre l’alerte ou l’oxygène.
- [x] **P368** · QCM · Rappel / application — Évacuation décidée avec les secours.
- [x] **P369** · QCM · Rappel / application — Respecter paliers et consignes de remontée.
- [x] **P370** · QCM · Rappel / application — Éviter efforts importants après immersion.
- [x] **P371** · QCM · Rappel / application — Apnée après plongée : précautions à documenter.
- [x] **P374** · QCM · Rappel / application — Oscillations de profondeur : effets et prévention ; pas d’interdiction absolue de tout profil inversé.
- [x] **P375** · QCM · Rappel / application — Nombre de plongées et intervalle : référentiel à préciser.
- [x] **P376** · QCM · Rappel / application — Avion et altitude : délai à documenter.
- [x] **P377** · QCM · Scénario — Scénario : douleur articulaire après retour au bateau.
- [x] **P380** · QCM · Scénario — Scénario : deux accidents possibles, même priorité d’alerte.

### 12-tables — Désaturation

Source : **S1 p.23–26**. Contrôle : **V10**. Fichier futur : `cards/n2/12-tables.yaml`.

- [x] **P381** · Basic · Compréhension — Tables : rôle historique et principe.
- [x] **P384** · QCM · Rappel / application — Temps table : début immersion à début remontée.
- [x] **P386** · QCM · Rappel / application — Minute commencée et arrondi supérieur.
- [x] **P388** · QCM · Rappel / application — Tables MN90 : domaine d’emploi à l’air.
- [x] **P390** · QCM · Rappel / application — Courbe sans palier : définition.
- [x] **P394** · QCM · Rappel / application — Durée totale de remontée : composants.
- [x] **P395** · Basic · Compréhension — GPS : rôle et lettre.
- [x] **P396** · QCM · Rappel / application — Vitesse fond-premier palier propre aux MN90.
- [x] **P398** · QCM · Erreur / limite — Ne pas transposer une vitesse table à tout ordinateur.
- [x] **P399** · QCM · Rappel / application — Distinguer les catégories d’intervalle dans une édition de tables fournie ; bornes précisées dans la question.
- [x] **P405** · QCM · Rappel / application — Majoration : définition.
- [x] **P406** · QCM · Comparaison — Durée théorique versus durée réelle.
- [x] **P407** · QCM · Rappel / application — Variables qui déterminent la majoration.
- [x] **P408** · QCM · Rappel / application — Remontée lente : temps pris en compte selon MN90.
- [x] **P411** · Basic · Complément — Exercice de lecture d’une ligne de table : données à obtenir.
- [x] **P412** · QCM · Rappel / application — Exercice de courbe sans palier : valeurs à vérifier visuellement.
- [x] **P413** · Basic · Complément — Exercice de calcul DTR : données complètes nécessaires.
- [x] **P414** · Basic · Complément — Exercice de successive : obtenir les tables complémentaires.

### 13-ordinateurs — Désaturation

Source : **S1 p.27–29 ; S2 p.1–2**. Contrôle : **V11**. Fichier futur : `cards/n2/13-ordinateurs.yaml`.

- [x] **P415** · QCM · Rappel / application — Distinguer le profil suivi par un ordinateur et le profil carré d’une table ; calcul du modèle et historique expliqués.
- [x] **P418** · QCM · Rappel / application — Temps écoulé et temps restant sans palier.
- [x] **P422** · QCM · Rappel / application — Vitesse de remontée et alarme.
- [x] **P423** · QCM · Rappel / application — Affichage du gaz sélectionné.
- [x] **P424** · QCM · Rappel / application — Réglage eau douce/eau salée.
- [x] **P427** · QCM · Rappel / application — Garder le même ordinateur pour une série.
- [x] **P430** · QCM · Lecture / repérage — Avant immersion : vérifier écran, énergie et réglages.
- [x] **P432** · QCM · Rappel / application — Expliquer pourquoi la fin de ses propres obligations ne suffit pas à autoriser une remontée solitaire.
- [x] **P433** · QCM · Rappel / application — Algorithmes et réglages différents : résultats différents.
- [x] **P437** · QCM · Scénario — Lire deux ordinateurs aux obligations différentes et organiser une fin de plongée commune.
- [x] **P438** · QCM · Scénario — Scénario : DTR augmente pendant la plongée.
- [x] **P439** · QCM · Scénario — Scénario : confusion NDL et autonomie en air.
- [x] **P440** · QCM · Rappel / application — Gestion de l’air intégrée : dépend d’une sonde.
- [x] **P441** · QCM · Erreur / limite — Erreur ou verrouillage après incident : dépend du modèle.
- [x] **P443** · QCM · Lecture / repérage — Lire le manuel du modèle utilisé.
- [x] **P444** · QCM · Rappel / application — Pas de garantie de sécurité fournie par un ordinateur.
- [x] **P445** · QCM · Rappel / application — Choix : lisibilité et acuité visuelle.
- [x] **P446** · QCM · Rappel / application — Choix : air ou nitrox selon pratique future.

### 14-remontees-anormales — Désaturation

Source : **S1 p.26–27**. Contrôle : **V12**. Fichier futur : `cards/n2/14-remontees-anormales.yaml`.

- [x] **P454** · QCM · Comparaison — Distinguer MN90 historique et recommandation fédérale ordinateur.
- [x] **P456** · QCM · Rappel / application — Remontée trop rapide : critères de déclenchement à vérifier.
- [x] **P458** · QCM · Rappel / application — Réimmersion après remontée anormale : conditions à confirmer.
- [x] **P461** · QCM · Rappel / application — Réimmersion impossible : conduite du protocole validé.
- [x] **P463** · QCM · Rappel / application — Yoyos : identifier le profil.
- [x] **P464** · QCM · Rappel / application — Exercices d’assistance : limiter les remontées répétées selon recommandation.
- [x] **P465** · QCM · Comparaison — Palier obligatoire interrompu versus palier de confort.
- [x] **P466** · QCM · Rappel / application — Reprise après interruption : conditions à confirmer.
- [x] **P468** · QCM · Rappel / application — Expliquer le suivi après incident sans symptômes selon la référence validée ; aucune garantie d’absence d’accident.
- [x] **P472** · QCM · Scénario — Scénario : paliers non réalisés et symptômes.

### 15-gonflage-blocs — Matériel et préparation

Source : **S1 p.29–30**. Contrôle : **V13**. Fichier futur : `cards/n2/15-gonflage-blocs.yaml`.

- [x] **P474** · QCM · Rappel / application — Compresseur : aspiration atmosphérique et compression.
- [x] **P477** · QCM · Comparaison — Gonflage direct versus bouteilles tampons.
- [x] **P479** · QCM · Rappel / application — Pression de gonflage : respecter la pression de service.
- [x] **P480** · QCM · Rappel / application — Habilitation et accès au local de gonflage.
- [x] **P482** · QCM · Rappel / application — Bloc : stockage du gaz respirable.
- [x] **P483** · QCM · Rappel / application — Acier et aluminium : matériaux.
- [x] **P484** · QCM · Rappel / application — Mono et bi : configurations.
- [x] **P488** · QCM · Rappel / application — Distinguer pression de service et pression d’épreuve ; choisir la donnée pertinente pour le gonflage.
- [x] **P494** · QCM · Rappel / application — Éviter chocs et grandes variations thermiques.
- [x] **P495** · QCM · Rappel / application — Robinetterie ouverte dans l’eau : risque.
- [x] **P496** · QCM · Rappel / application — Décharge brutale à l’air : risque.
- [x] **P497** · QCM · Rappel / application — Peinture et corrosion : surveillance.
- [x] **P498** · QCM · Comparaison — Inspection visuelle et requalification : distinction.
- [x] **P500** · QCM · Rappel / application — Périodicités et régime de suivi : vérifier la règle actuelle.
- [x] **P502** · QCM · Rappel / application — Transport d’un bloc gonflé : corriger la formulation générale du support.
- [x] **P504** · QCM · Scénario — Lire une inscription de bloc fictive : trouver capacité et pression de service parmi les autres marquages.
- [x] **P505** · QCM · Scénario — Scénario : bloc à requalification dépassée.
- [x] **P506** · QCM · Scénario — Scénario : changement de bloc et réévaluation du lestage.

### 16-detendeurs — Matériel et préparation

Source : **S1 p.30–34**. Contrôle : **V14**. Fichier futur : `cards/n2/16-detendeurs.yaml`.

- [x] **P508** · QCM · Rappel / application — Sur un circuit bloc–détendeur, associer HP, MP et pression ambiante à leur position et aux deux étages.
- [x] **P512** · QCM · Comparaison — MP relative et MP absolue : distinction.
- [x] **P514** · QCM · Rappel / application — Fixation DIN et étrier : identifier.
- [x] **P515** · QCM · Rappel / application — Premier étage à membrane ou piston.
- [x] **P519** · QCM · Rappel / application — Expliquer l’ouverture puis la fermeture du premier étage dans une conception annoncée ; pièces en explication.
- [x] **P521** · QCM · Rappel / application — Second étage à l’inspiration : membrane et levier.
- [x] **P523** · QCM · Rappel / application — Bouton de purge : fonction.
- [x] **P524** · QCM · Rappel / application — Second étage immergé : évacuer l’eau avant inspiration.
- [x] **P525** · QCM · Rappel / application — Entrée premier étage : prévenir la pénétration d’eau.
- [x] **P526** · QCM · Comparaison — Détendeur simple versus compensé : rôle de la compensation.
- [x] **P532** · QCM · Rappel / application — Choisir un détendeur adapté au contexte à partir de caractéristiques constructeur ; éviter les slogans commerciaux.
- [x] **P537** · QCM · Rappel / application — Éviter soleil, chocs et écrasement.
- [x] **P539** · QCM · Rappel / application — Révision périodique selon constructeur et usage.
- [x] **P540** · QCM · Rappel / application — Débit continu : causes dans le tableau source à relever.
- [x] **P541** · QCM · Rappel / application — Fuite de robinetterie : joint et montage, tableau à relever.
- [x] **P542** · QCM · Rappel / application — Inspiration difficile : pression, ouverture, filtre ou réglage, à confirmer.
- [x] **P543** · QCM · Rappel / application — Incident de détendeur : priorité à la sécurité de la palanquée.
- [x] **P544** · QCM · Rappel / application — Tableau de pannes : séparer observation, cause possible et action autorisée.
- [x] **P545** · QCM · Scénario — Scénario : confusion entre MP et pression délivrée à la bouche.

### 17-competences-transversales — Matériel et préparation

Source : **S2 p.1–2 ; S1 p.3–5, 11–12, 23, 28**. Contrôle : **V15**. Fichier futur : `cards/n2/17-competences-transversales.yaml`.

- [ ] **P547** · QCM · Rappel / application — PE40 : vérifier son propre matériel.
- [ ] **P549** · QCM · Rappel / application — PE40 : comprendre le briefing du GP.
- [ ] **P550** · QCM · Rappel / application — Construire un briefing commun cohérent avec profondeur, gaz, désaturation et communication ; une décision contextualisée.
- [ ] **P552** · Basic · Complément — Planification : stock de gaz et réserve, complément nécessaire.
- [ ] **P555** · QCM · Rappel / application — Code de communication pour les paliers.
- [ ] **P557** · QCM · Rappel / application — Expliquer la stabilisation pendant remontée et palier ; relier gestion du volume et contrôle de la profondeur.
- [ ] **P560** · QCM · Rappel / application — PA20 : responsabilité collective d’assistance.
- [ ] **P561** · Basic · Complément — Orientation et retour au bateau : compétence citée, cours absent.
- [ ] **P562** · Basic · Complément — Repères naturels : complément à documenter.
- [ ] **P563** · Basic · Complément — Boussole et cap retour : complément à documenter.
- [ ] **P564** · Basic · Complément — Perte de palanquée : procédure absente à obtenir.
- [ ] **P565** · QCM · Rappel / application — Parachute : compétence opérationnelle, support incomplet.
- [ ] **P567** · QCM · Rappel / application — Signaler une difficulté avant aggravation.
- [ ] **P569** · QCM · Scénario — Scénario : autorisation réglementaire mais état personnel défavorable.
- [ ] **P570** · QCM · Scénario — Scénario : guide présent ne dispense pas de surveiller son ordinateur.
- [ ] **P572** · QCM · Scénario — Scénario : choix collectif de la contrainte la plus protectrice.

### 18-lecture-pannes — Matériel et préparation

Source : **S1 p.24–25, 31–34 (figures et tableau)**. Contrôle : **V14**. Fichier futur : `cards/n2/18-lecture-pannes.yaml`.

- [x] **P573** · QCM · Rappel / application — Entrée d’eau à l’inspiration : embout endommagé.
- [x] **P577** · QCM · Rappel / application — Absence d’air : premier étage bloqué, cause possible non exclusive.
- [x] **P578** · QCM · Rappel / application — Bulles chambre humide : défaut de joints, hypothèse source.
- [x] **P580** · QCM · Rappel / application — Flexible endommagé : fuite et vidange rapide.
- [x] **P581** · QCM · Rappel / application — Réparation interne : confier à une personne qualifiée.
- [x] **P585** · QCM · Lecture / repérage — Lire un schéma original : distinguer les fonctions des deux étages ; détails du modèle explicités.

### Reprises complémentaires à répartir dans les fichiers existants

Chaque reprise ci-dessous teste un autre angle ; le rapprochement avec la section sert à
la revue de couverture, pas à imposer un ordre de révision. Même source et contrôle que la section.

- [ ] **P594** · QCM · Erreur · `04-pression.yaml` — Un calcul donne 2 bar à 20 m : identifier la pression oubliée.
- [ ] **P606** · QCM · Comparaison · `07-barotraumatismes.yaml` — Distinguer équilibrage d’oreille à la descente et ventilation libre à la remontée.
- [ ] **P622** · QCM · Erreur · `13-ordinateurs.yaml` — Différencier temps écoulé, NDL et DTR sur trois écrans fictifs.
- [x] **P627** · Basic · Calcul · `16-detendeurs.yaml` — Avec MP relative fournie, calculer MP absolue à 20 m dans un modèle fictif.

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
- [ ] Écrire l’apport distinct par rapport aux cartes existantes de tous les chapitres ; fusionner les doublons simples.
- [ ] `id` permanent, `levels: [N2]`, `fr` obligatoire, tags de thème et d’angle.
- [ ] `status: draft` jusqu’à la revue factuelle et pédagogique.
- [ ] Validation du YAML, schéma JSON cohérent et `make check` réussi.
- [ ] Build de prévisualisation ; affichage recto/verso et mélange des choix contrôlés.

## Suivi final de couverture

Pour chaque section : noter cartes rédigées, cartes revues, cartes publiées, cartes bloquées
par manque de source et cartes écartées avec justification. Conserver le lien entre chaque Pxxx
et les IDs YAML produits. Une carte éventuellement scindée donne plusieurs IDs, une proposition fusionnée ou écartée
reste retrouvable dans l’audit avec sa justification. Le nombre de cartes réel sera recalculé après rédaction.

Le deck N2 sera prêt lorsque tous les objectifs essentiels couverts par les sources auront
été traités ou explicitement reportés, les contradictions résolues et la couverture comparée au
référentiel choisi. Les éléments culturels écartés ne conditionnent pas ce jalon.

## Avancement du chapitre 01

P001–P027 examinés : 21 cartes actives ; 7 variantes retirées (P020 reste scindé en deux). Source actualisée : MFT N2 mai 2026,
Code du sport A322-73 depuis octobre 2025. Détail dans docs/reviews/01-prerogatives.md.

## Avancement du chapitre 02

20 cartes revues ; P057 absorbé dans P053/P054 pour éviter un doublon. V02 contrôlé dans
les textes actuels. Voir [la revue du chapitre](reviews/02-organisation.md).

## Avancement du chapitre 03

12 nouvelles cartes revues ; P059 et P077 couverts par les chapitres précédents, P498 couvert
par P078. V03 vérifié dans le périmètre rédigé ; pas de distance locale chiffrée ni d’interdiction
universelle de prélèvement. Voir [la revue du chapitre](reviews/03-documents-environnement.md).

### Chapitre 04 — réalisé le 6 octobre 2026

24 cartes revues dans Physique couvrent les 18 objectifs : P118 absorbé par P110, P132 par P101.
V04 vérifié ; voir [la revue](reviews/04-pression.md). Total publié : 77 cartes.

Complément du chapitre 04 : huit exercices supplémentaires demandés pour pratiquer à plusieurs
profondeurs. Ils approfondissent P110, P114, P123 et P129 sans créer de nouveaux objectifs
au catalogue. Voir la revue du chapitre pour les cas et leur validation.

### Chapitre 05 — réalisé le 6 octobre 2026

25 cartes revues, dont huit exercices de calcul, couvrent les 23 objectifs. P149 → P133,
P152 → P151 et P171 → P172 ; les exercices supplémentaires pratiquent les objectifs existants.
V05 vérifié : eau salée, unités, volume du lest et limites des généralités sur le matériel.
Voir [la revue](reviews/05-flottabilite.md). Total publié après ce chapitre : 102 cartes.

### Chapitre 06 — réalisé le 6 octobre 2026

31 cartes revues, dont 20 exercices, couvrent les 28 objectifs. P202 → P201 ; les variantes
de calcul pratiquent P179, P193 et P195. Compléments P205/P206 et P630–P636 sourcés
par les relations et principes BSAC, avec données fictives imposées. Aucune réserve
universelle ou procédure de demi-tour n’est créée. Voir [la revue](reviews/06-gaz-autonomie.md).
Total publié : 133 cartes.

### Chapitre 07 — réalisé le 6 octobre 2026

21 nouvelles cartes revues pour les 21 objectifs, dont deux déjà couverts : P226 par P189,
P246 par P157/P245. Deux cas distincts complètent P252 : amélioration sous oxygène et
victime ne respirant pas normalement. P221/P239 adaptés aux connaissances et recommandations
primaires vérifiées, sans procédure universelle de redescente. V07 vérifié pour ce chapitre ;
reste ouvert pour essoufflement et froid. Voir [la revue](reviews/07-barotraumatismes.md).
Total publié : 154 cartes ; 180 objectifs du catalogue encore à traiter.

### Chapitres 08–10 — 6 octobre 2026

11 cartes essoufflement, 11 froid et 14 narcose, vérifiées et relues. P266 → P263 ;
P280 → secours P252 du chapitre 07 ; P324 → P313. V07 et V08 clôturés.
Total : 190 cartes revues ; 142 objectifs encore à traiter.

### Chapitre 11 — 6 octobre 2026

26 cartes nouvelles ; sept objectifs de reconnaissance/secours réutilisent le chapitre 07.
Total : 216 cartes revues ; 109 objectifs encore à traiter. P375 sera couvert avec les tables ;
V09 reste ouvert pour cette dernière précision de domaine d’emploi.

### Chapitre 12 — 6 octobre 2026

20 cartes, dont huit exercices de lecture/calcul, avec tables complètes de juillet 2005
contrôlées visuellement. P375 couvert, V09/V10 clôturés.
Total : 236 cartes revues ; 90 objectifs encore à traiter.

### Chapitre 13 — 6 octobre 2026

17 cartes revues. P444 → P343 ; V11 clôturé. Total 253 cartes, 72 objectifs restants.

### Chapitre 14 — 6 octobre 2026

10 cartes revues. V12 clôturé. Total 263 cartes, 62 objectifs restants.

### Chapitres 15, 16 et 18 — 6 octobre 2026

14 cartes blocs/gonflage, 21 détendeurs dont trois calculs et un schéma original,
3 pannes complémentaires. P488 → P479 ; P482 → P185/P195 ; P504 → P479/P195 ;
P577 → P542/P544 ; P581 → P544 ; P585 → schéma P508. V13/V14 clôturés.
Total : 301 cartes revues ; 19 objectifs encore à traiter.
