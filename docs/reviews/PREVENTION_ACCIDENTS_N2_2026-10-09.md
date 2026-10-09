# Revue approfondie — N2 Prévention des accidents

Revue du **9 octobre 2026** : les **53 cartes** des fichiers 07–10 ont été relues,
recto, trois choix et corrigé. **40 cartes réécrites**, 13 conservées ; **106 leurres**
analysés individuellement dans le [CSV](PREVENTION_ACCIDENTS_N2_2026-10-09.csv).
Aucune création, fusion, suppression ou suspension. Tous les IDs, modèles Anki,
objectifs, paquets, niveaux et tags historiques sont conservés. Aucun fichier N3 modifié.
Les cartes N2 partagées avec N3 conservent leurs tags ; leur contenu commun est amélioré.

## Méthode

Lecture initiale intégrale, analyse des défauts, rédaction des propositions, puis
seconde critique distincte et corrections avant validation. Deux lots : 30 cartes
(barotraumatismes et essoufflement), puis 23 (froid et narcose). Même agent pour les
passes ; aucune validation indépendante ou mesure de difficulté sur des apprenants.
Le CSV donne par ID le défaut initial, la décision, les choix finaux et, pour chaque
leurre, la confusion qui peut l'attirer et le fait qui la réfute. Son empreinte SHA256
porte sur tout le contenu français final, corrigé compris.

Contrôles : ISOLATION, CREDIBILITY, LENGTH, WHY et SENSE. Les faits simples gardent
une question de rappel ; leur difficulté n'est pas fabriquée par un long scénario.
Les 53 objectifs conviennent au QCM ; aucune réponse libre introduite.

## Corrections principales

- **Sinus et oreilles** : remplacer des symptômes articulaires ou des marbrures
  éloignés du sujet par des tableaux voisins : sinus, oreille et masque. Les questions
  demandent une orientation ou un mécanisme, sans prétendre à un diagnostic exclusif.
  Les ostia, trompes d'Eustache et choanes sont des ouvertures réelles, aux connexions
  distinctes expliquées au verso.
- **Équilibrage** : distinguer obstruction des petits conduits, compression du gaz et
  pression ambiante. La descente douloureuse persistante est située après arrêt et
  légère remontée ; l'amélioration d'une douleur ou un équilibrage auriculaire facile
  ne valide pas la poursuite malgré une difficulté des sinus.
- **Dents** : préciser la phase de remontée et l'expansion de la poche de gaz ; la fin
  de douleur ne prouve ni l'intégrité de l'obturation ni une cause exclusivement sinusienne.
- **Poumons et secours** : les paliers gèrent la désaturation, sans exclure un
  barotraumatisme ou un œdème pulmonaire d'immersion. Comparer les signes neurologiques
  possibles à deux faux critères nécessaires, plutôt qu'à une simple fatigue.
  L'alerte est commune aux alternatives de prise en charge : la distinction porte sur
  oxygène normobare, réimmersion et air au masque. Amélioration sous oxygène et relais
  des secours sont distingués. La respiration absente/anormale impose réanimation
  et défibrillateur disponible ; PLS et masque seul ne répondent pas à cet état.
- **Essoufflement** : expliquer l'espace mort et séparer débit total et ventilation
  alvéolaire. Pour les premières actions, le gaz disponible et le détendeur fonctionnel
  sont explicités : changer de source ou travailler l'expiration tout en poursuivant
  l'effort ne supprime pas le déclencheur. Les critères de courant comparent capacité
  ventilatoire, réserve de gaz et temps prévu, plutôt qu'aide contre accélération.
- **Froid** : préciser la phase de lutte avec frissons pour ne pas généraliser une
  hausse des besoins ventilatoires à tous les stades d'hypothermie. Comparer les bilans
  thermiques, expliquer le renouvellement d'eau sous une combinaison trop ample et
  organiser le passage au sec à l'abri. La contre-indication à une boisson porte sur
  conscience/déglutition, plutôt que d'offrir une boisson malgré ces troubles.
- **Narcose** : trois mécanismes réels distinguent narcose, bulles de désaturation et
  embolie artérielle. Fraction, pression partielle et expérience passée sont séparées.
  Le ressenti euphorique ne valide ni jugement ni attention. L'avis médical porte sur
  traitement, maladie et plongée prévue, plutôt que sur un simple essai en profondeur.
  L'amélioration en remontant vient de la baisse des pressions partielles, sans attendre
  une désaturation complète. Le rôle de l'équipier valide est précisé.

La seconde critique a notamment retiré deux leurres qui attribuaient à la respiration
superficielle une modification de la composition du bloc : le problème relève de
l'espace mort et du débit utile. Une dernière lecture a remplacé cette question par
la comparaison de deux ventilations de même débit total : les trois choix sont des
résultats concurrents. Elle a aussi fixé le cadre de lutte contre le froid,
la disponibilité du gaz avant changement de source et la distinction entre orientation
clinique et diagnostic. Aucune procédure de plongée nouvelle n'est déduite de ces cas.

## Sources contrôlées

Les trois supports pédagogiques N2 restent référencés dans les cartes ; cette revue
ne prétend pas relire intégralement ces PDF privés. Les affirmations médicales et
les distinctions réécrites sont recroisées avec les pages primaires ci-dessous,
consultées le **9 octobre 2026**, puis tracées dans `review.sources` et le CSV.

- [DAN — Ears and Diving, Injuries](https://dan.org/health-medicine/health-resource/dive-medical-reference-books/ears-diving/ear-injuries/)
  et [Key Information](https://dan.org/health-medicine/health-resource/dive-medical-reference-books/ears-diving/ears-equalization/) :
  trompes, oreille moyenne, vertige alternobarique, position et équilibrage doux.
- [DAN — Sinus Barotrauma](https://dan.org/health-medicine/health-resources/diseases-conditions/sinus-barotrauma/) :
  ostia, blocage de descente/remontée, douleurs faciales et projetées vers les dents.
- [University of Michigan — Respiratory LOs](https://sites.google.com/a/umich.edu/bluelink/curricula/anatomy-403/respiratory-system/respiratory-los) :
  choanes et nasopharynx ; vérifier aussi l'anatomie du leurre, pas seulement la clé.
- [DAN — Unexpected Air Pockets](https://dan.org/alert-diver/article/unexpected-air-pockets/) :
  obturations défectueuses, poche de gaz et dommage malgré un changement de douleur.
- [DAN — Back to Basics](https://dan.org/alert-diver/article/back-to-basics/) :
  expansion pulmonaire, gaz artériel, variation relative près de la surface et Dalton.
- [DAN World — Your Lungs and Diving](https://world.dan.org/alert-diver/article/your-lungs-and-diving/)
  et [BSAC — Gas](https://www.bsac.com/safety/safe-diving-guide/gas/) :
  densité, effort ventilatoire, espace mort, rétention de CO₂, narcose et réduction de profondeur.
- [DAN — Breathing Gas Contamination](https://dan.org/safety-prevention/diver-safety/psa/breathing-gas-contamination/) :
  signes peu spécifiques et monoxyde de carbone inodore ; aucune certitude diagnostique
  déduite de plusieurs victimes ou d'un gonflage commun.
- [DAN — Exposure-Related Injuries](https://dan.org/health-medicine/travelers-medical-guide/travel-related-injuries/exposure-related-injuries/)
  et [Assurance Maladie — Hypothermie](https://www.ameli.fr/assure/sante/themes/froid-pathologies-sante/hypothermie) :
  bilan thermique, gravité, douceur des manipulations, protection et boisson si lucide.
  La carte de réchauffement conserve le contexte de confusion : les conseils d'exercice
  parfois cités pour un refroidissement léger ne sont pas transférés à ce cas.
- [FFESSM CMPN — CAT accident bouteille ou recycleur](https://medical.ffessm.fr/cat-accident-de-plongee-bouteille-ou-recycleur),
  page du **10 mars 2021**, toujours disponible lors de la consultation : bilan vital,
  alerte, oxygène jusqu'au relais et surveillance. Cette date est celle de la page,
  pas une édition 2026 inventée.
- [FFESSM CMPN — Je prends des médicaments](https://medical.ffessm.fr/je-prends-des-medicaments),
  page du **7 mars 2021** : médicament, pathologie et risques pour la pratique.
- [Resuscitation Council UK — Adult Basic Life Support 2025](https://www.resus.org.uk/professional-library/2025-resuscitation-guidelines/adult-basic-life-support-guidelines) :
  respiration absente/anormale, réanimation et défibrillateur. Pas de transfert du numéro
  d'alerte britannique ni de détails du protocole non demandés par la carte.

## Pertinence et calculs

Les fusions de la revue finale N2 et les objectifs voisins du catalogue ont été
consultés. Les mécanismes et priorités restent séparés lorsqu'ils testent des distinctions
utiles : cavité moyenne/externe, masque/sinus, pression du gaz/désaturation, froid léger
ou confusion, rôle de l'assistant et réponse personnelle. Les secours communs restent
sur leurs IDs existants ; aucune répétition ajoutée pour les autres chapitres.

Dalton : les trois exercices existants sont conservés (20 % à 30 m, 80 % à 40 m,
21 % sous 3 bar absolus). Contrôle distinct : 0,20×4 = 0,8 ; 0,80×5 = 4 ; 0,21×3 = 0,63.
Les six résultats faux correspondent à une omission d'atmosphère/fraction, à un arrondi
non demandé ou à une soustraction injustifiée. Pour le gaz piégé depuis 3 m :
1,3/1 = 1,3, soit +30 % dans le modèle de gaz libre, pas une dilatation prescrite des poumons.
Ventilation : 30×250 = 15×500 = 7 500 mL/min ; l'espace mort occupe respectivement
30×150 = 4 500 et 15×150 = 2 250 mL/min. Par soustraction du débit total, on retrouve
3 000 et 5 250 mL/min de débit alvéolaire. Les 150 mL sont une donnée de modèle,
pas une mesure de chaque plongeur ou une consigne de fréquence/amplitude en immersion.

## Validation technique

`make check` réussi : 448 cartes valides, lint, formatage, types et schéma conformes ;
20 tests réussis, un module facultatif ignoré. Build : 448 notes, zéro draft.
Contrôle des 53 identités, modèles, paquets et métadonnées historiques conservés,
des 106 lignes de leurres et empreintes, et des champs HTML recto/verso exportés.
Inspection des champs représentatifs : sinus, oxygène, ventilation, boisson et médicaments.
Le contrôle porte sur le HTML généré, sans prétendre à un examen visuel dans Anki.
Aucune manipulation de l'interface Anki ni import pendant cette revue.
