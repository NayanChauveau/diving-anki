# Dernière revue intégrale N2 — 6 octobre 2026

Relecture des **312 cartes du commit 806960e**, rectos, réponses, explications et chaque
choix des 69 QCM. Comparaison entre les 18 chapitres, puis rédaction de six compléments
et seconde lecture des modifications. Résultat : **308 cartes actives** (68 QCM, 240 basic),
23 cartes corrigées, dix cartes fusionnées et six nouvelles cartes. Aucun changement
d’ID ou de modèle pour les 302 cartes conservées.

Le [registre par ID](REVUE_FINALE_N2.json) distingue conservation, correction, fusion et
ajout pour les 318 cartes examinées. Il trace les décisions ; les justifications sont ici.
Les revues de lots restent des bilans historiques. La
[couverture actuelle](COUVERTURE_FINALE_N2.md) remplace leurs correspondances devenues obsolètes.

## Méthode et constat d’ensemble

- Lecture intégrale par chapitre, puis comparaison des tâches voisines entre chapitres.
- Contrôle des QCM : contexte, portée de l’obligation, unicité de la réponse, plausibilité
  et indices de style. Six QCM reconstruits ; une question de périmètre précisée.
- Recalcul des résultats chiffrés pendant la lecture, puis contrôle numérique distinct
  des exercices avec résultats explicites et résolution alternative des nouveaux calculs.
- Réouverture des références primaires sur les points réglementaires et de sécurité à enjeu :
  MFT, Code du sport, suivi des blocs, CMPN, DAN, manuel de décompression Suunto.
  Le manuel constructeur SCUBAPRO 2025 a été relu dans son extraction locale pour l’entretien.
- Recherche des lacunes par tâche, pas par nombre de cartes : calcul inverse, parcours
  à pression variable, plusieurs paliers, lecture de plafond et coordination de deux plafonds.

Les séries de pressions, flottabilité et consommation sont conservées : les valeurs variées,
les signes, les calculs inverses, les changements d’hypothèses et les besoins de deux équipiers
ont un intérêt d’entraînement. Les reconnaître comme proches ne suffit pas à les supprimer.
À l’inverse, une question de bon sens répétée dans un autre chapitre ne devient pas utile
par le seul ajout d’une profondeur ou d’un incident.

## Fusions — aucun objectif utile abandonné

Les IDs complets et leurs remplacements sont dans [RETIREMENTS_N2.yaml](RETIREMENTS_N2.yaml).

| Carte retirée | Couverture active | Motif |
| --- | --- | --- |
| P010, N2 autonome à 30 m | P001 | Repose la limite PA20 par substitution d’une profondeur ; précision absorbée dans l’aptitude N2. |
| P265, contrôle respiratoire du matériel | P542 | Même contrôle de robinet/détendeur. Sa conséquence ventilatoire est intégrée dans la réponse P542. |
| P279, remonter moins profond avec l’équipier | P261/P274 | La baisse de densité est déjà expliquée ; les contraintes d’assistance sont réunies dans P274. |
| P288, signaler le froid | P283 | Répète la décision attachée à la dégradation des gestes ; P283 teste reconnaissance et décision dans un même cas. |
| P298, froid et dévidoir | P283 | Même perte de capacité, désormais donnée comme exemple concret de P283. |
| P411, relire une DTR déjà nommée | P394/P413 | La réponse est nommée au recto ; définition et vrai calcul existent déjà. |
| P437, deux durées au même palier | P432 | Même règle de fin collective. L’actualisation des appareils est conservée dans P432. |
| P506, changer de bloc et de lestage | P483 | Même dépendance masse/volume extérieur ; changement de configuration et contrôle final absorbés. |
| P544, « cause probable » | P542/P573 et autres pannes | Question générique. Les véritables cas de panne enseignent déjà hypothèse, contrôle et absence de diagnostic certain. |
| P565, dévidoir accroché à soi | P168 | Doublon exact de mécanisme ; les précautions de ligne sont conservées dans P168. |

Les dix notes déjà importées sont destinées à la **suspension**, jamais à la suppression.
Leur ID est réservé. Sept notes anciennes, absentes dès le commit de départ, ont également
été identifiées dans Anki : cinq déjà suspendues, deux encore actives (P011/P015), redondantes
avec P001/P016. Ces deux dernières rejoignent la suspension ; les cinq autres la conservent.
Le registre réserve donc 17 IDs au total, dont dix retirés lors de cette revue. L’import d’un package ne suspend pas automatiquement une note absente
du catalogue : le contrôle Anki avant/après est une étape séparée.

## Corrections de clarté et de difficulté

| Objectifs | Changement et raison |
| --- | --- |
| P001 | Intègre la précision de P010 : l’accord du DP n’étend pas PA20 à 30 m. |
| P012 | Retrait du leurre « 12 m à l’aller, 20 m au retour » ; trois choix portent sur aptitude, assistance et accord du DP. |
| P022 | Le recto ne demande plus une paire « licence et certificat » en la nommant déjà. Il interroge affiliation et état médical ; le verso distingue CACI, licence, brevet et expérience. |
| P027 | Trois cadres concurrents explicites (local, français, CMAS) ; retrait de « sans vérifier » qui rendait les mauvais choix trop faciles. |
| P038 | Choix comparables sur l’adaptation par le guide, les limites du DP et la zone PE40 ; suppression d’un quatrième choix faible. |
| P044 | Suppression du distracteur facultatif lié aux paliers, sans confusion utile. |
| P045 | Les fins de couverture O₂ proposées sont des étapes du secours ; retrait de l’arrêt à la première amélioration comme leurre évident. |
| P049 | Demande l’ensemble des situations soumises à l’obligation, plutôt qu’une « condition suffisante » ambiguë face à des sous-ensembles. |
| P168 | Ajout de la ligne à distance du corps et du maintien de profondeur depuis P565. |
| P272 | Essoufflement constitué : arrêt de l’effort, signalement et fin organisée. L’ancienne formulation « avant de poursuivre » et « si la gêne persiste » pouvait suggérer une reprise d’exploration. |
| P274 | Contraintes concrètes de vitesse, respiration, désaturation, gaz et groupe ; intégration du bénéfice de moindre densité sans donner une remontée libre. |
| P283 | Cas concret de gestes dégradés par le froid, avec aide et sortie commune ; rassemble les répétitions P288/P298. |
| P376 | Plage de pression cabine explicite en altitude équivalente, pas altitude de vol de l’avion. L’explication est recentrée sur le cas sans palier ; retrait de la recommandation vague sur les plongées avec décompression. |
| P381 | Restreint le profil carré à la lecture classique des MN90 ; ne généralise pas à toutes les tables. |
| P399 | Les définitions ne figurent plus au recto : il faut connaître les bornes 15 min/12 h ; elles sont expliquées au verso. |
| P432 | Demande une organisation concrète, pas « pourquoi ne pas partir seul ». Intègre les mises à jour des appareils depuis P437. |
| P637 | Retrait de l’alternative suggérée « risque ou marge » : rappel actif du sens physique du GF. |
| P461 | Champ air/ordinateur explicite sur ce recto autonome. |
| P466 | Gaz, assistance et retour effectif au palier dans le délai explicités. |
| P468 | Distingue minutes de palier non faites et délai depuis la sortie de l’eau ; ces deux durées ne sont pas interchangeables. |
| P483 | Intègre changement de bloc et contrôle de lestage en fin de plongée. |
| P508 | Réponse désigne directement A et B, plutôt que laisser refaire la correspondance du schéma. |
| P542 | Réunit contrôle concret et conséquence sur la ventilation, sans désigner une panne unique. |

## Six compléments retenus après comparaison

| Objectif | Apport | Contrôle distinct |
| --- | --- | --- |
| P640 | Boyle inverse : calculer la pression finale, puis la profondeur. Aucun exercice antérieur ne demandait la profondeur à partir des volumes. | 3 L × 2 bar = 2 L × 3 bar ; profondeur 20 m. |
| P641 | Consommation sur une remontée régulière : la pression varie avec le temps, contrairement aux phases fixes de P633. | Deux demi-trajets de 1 min, pressions moyennes 2,5 et 1,5 bar : 50 + 30 = 80 L. |
| P642 | Inverser la majoration pour obtenir la durée réelle maximale sans palier. | 18 + 22 = 40 ; 19 + 22 dépasse la ligne sans palier. |
| P643 | Additionner deux arrêts et tous les trajets, puis arrondir une seule fois. | 88 s + 30 s + 30 s + 300 s = 448 s ; arrondi 8 min. Les arrêts sont imposés par l’énoncé, pas attribués à une ligne MN90 réelle. |
| P644 | Lire le sens du plafond de décompression ; les cartes existantes évoquaient le mot sans le tester. | 7 m reste sous 6 m ; 5 m franchit le plafond. |
| P645 | Coordonner deux plafonds différents, au-delà du cas de deux durées à même profondeur. | 3 m viole le plafond à 6 m ; crédit du palier dépend des indications de chaque appareil. |

Pas d’ajout de longues séries de blocs, de réserves universelles, de demi-vies de compartiments
ou de recettes de réparation. Les calculs de cours restent à hypothèses explicites. Le deck
ne prétend pas fournir toutes les pratiques ou tous les approfondissements du MFT.

## Bilan des 18 chapitres

| Chapitre | Avant → après | Décision globale de couverture |
| --- | --- | --- |
| 01 Prérogatives | 21 → 20 | Âges de certification et d’exercice distincts ; restriction de seconde plongée, nombre et intervalle conservés comme faits différents. |
| 02 Organisation | 20 → 20 | DP/guide, matériel collectif/individuel, minimum réglementaire distingués ; QCM corrigés sans doubler les rôles. |
| 03 Documents/environnement | 12 → 12 | Licence/CACI/assurance et réglementation locale ont des fonctions différentes ; pas de délai universel inventé ni de distance maritime généralisée. |
| 04 Pressions | 24 → 24 | Direct/inverse, relatif/absolu, météo/altitude, rapports et lac : série variée conservée. |
| 05 Flottabilité | 25 → 25 | Signes, poids apparent, volume du lest et eau salée conservés ; physique du parachute unique. |
| 06 Gaz/autonomie | 31 → 33 | Variété des stocks, réserves imposées, débits, phases et équipiers suffisante ; deux opérations absentes ajoutées. |
| 07 Barotraumatismes | 21 → 21 | Mécanisme, cavités différentes, faible profondeur et signes pulmonaires/neuro distincts ; secours communs restent ici. |
| 08 Essoufflement | 11 → 9 | CO₂, densité, signes, effort, courant, contamination et assistance conservés ; deux répétitions transversales fusionnées. |
| 09 Froid | 11 → 9 | Progression des signes et conduite adaptée à la conscience conservées ; deux scénarios de même dégradation fusionnés. |
| 10 Narcose | 14 → 14 | Dalton, composition donnée, variabilité, signes au fond et persistance en surface distincts ; pas de seuil individuel garanti. |
| 11 Désaturation | 26 → 26 | Dissolution, cinétique, élimination, signes cutanés/articulaires/auditifs et urgences ont des apports différents. |
| 12 Tables | 20 → 21 | Extraits contrôlés ; lecture trop facile retirée, inverse et plusieurs arrêts ajoutés. |
| 13 Ordinateurs | 19 → 20 | Réglages/historique, modèle, air/temps, GF et fabricant conservés ; répétition à même palier remplacée par plafonds différents. |
| 14 Remontées anormales | 10 → 10 | Critères et procédures fédérales relus ; absence de symptôme, faisabilité, deux durées et ancien domaine MN90 distingués. |
| 15 Blocs/gonflage | 14 → 13 | PS/PT, inspection/requalification et prescriptions constructeur distinctes ; un cas de lestage fusionné. |
| 16 Détendeurs | 21 → 20 | Deux étages, MP relative/absolue, membrane/piston, compensation et pannes conservés ; diagnostic générique fusionné. |
| 17 Préparation collective | 9 → 8 | Caps réciproques avec et sans passage par 360°, briefing, séparation et paliers profonds conservés ; parachute doublonné retiré. |
| 18 Pannes | 3 → 3 | Entrée d’eau, étanchéité de chambre humide et flexible abîmé portent sur des mécanismes différents. |

## Sources recroisées et limites

Consultation le 6 octobre 2026. Les références détaillées de chaque carte restent dans
`review.sources` et dans les revues de chapitres.

- [MFT N2, mai 2026](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/d7c761c8-79ed-42f2-a675-90e4c6095a56), p.3–4, 8, 12–14, 16–20 : âges, planification, GF et compétences.
- [Code du sport A322-73](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052464714), version depuis le 31 octobre 2025 : palanquée, contraintes et autonomie.
- [Code du sport A322-78](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000025393863) : secours, capacité O₂ et assistance collective.
- [Pêche maritime R921-92](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000029978123) : scaphandre et équipement de pêche à bord.
- [Suivi des équipements sous pression](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000036128632), art.15/18 : inspection et requalification des blocs.
- [CMPN, conduite en cas d’accident](https://medical.ffessm.fr/cat-accident-de-plongee-bouteille-ou-recycleur) : bilan vital, position, O₂, hydratation et transmission.
- [FFESSM, remontées anormales 2024](https://ffessm.fr/uploads/media/docs/0001/12/1e862af90f137e0c9bf98859c31092e14b8a3c5e.pdf), p.1–2 : procédures et distinctions de durées.
- [DAN, oreilles](https://dan.org/health-medicine/health-resource/dive-medical-reference-books/ears-diving/ears-equalization/), [sinus](https://dan.org/health-medicine/health-resources/diseases-conditions/sinus-barotrauma/), [hypothermie](https://dan.org/health-medicine/travelers-medical-guide/travel-related-injuries/exposure-related-injuries/) : mécanismes et conditions de prise en charge.
- [DAN, facteurs de désaturation](https://dan.org/health-medicine/health-resource/dive-medical-reference-books/decompression-sickness/contributing-factors/), [contamination du gaz](https://dan.org/safety-prevention/diver-safety/psa/breathing-gas-contamination/), [vol après plongée](https://world.dan.org/health-medicine/health-resource/health-safety-guidelines/guidelines-for-flying-after-diving/) : cas et champs d’application.
- [NASA, équation d’état](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/equation-of-state/), [BSAC, calculs de consommation](https://www.bsac.com/news-and-blog/so-you-think-you-use-too-much-gas/), section « How much gas do you use? » : modèles physiques. Pas de transfert de la règle BSAC des tiers ou de ses conseils de respiration.
- [MN90, juillet 2005](https://ffessm-ctr-aura.fr/wp-content/uploads/2019/03/MN90.pdf) : contrôle visuel du tableau p.4 et règles p.8 ; 20 m/40 min sans palier et 45 min/1 min à 3 m.
- [Suunto Zoop Novo, décompression](https://www.suunto.com/Support/Product-support/suunto_zoop_novo/suunto_zoop_novo/features/decompression-dives/) : plafond, actualisation et temps de remontée.
- [SCUBAPRO, manuel français RevQ 2025](https://johnsonoutdoors.widen.net/s/hlkmf7vhpb/sp_45101180_revq_reg_manual_202507_fra), p.16–17 et 20 : entretien et causes de panne.

La revue est réalisée par le même agent, avec une passe critique distincte ; elle ne constitue
pas une validation par un moniteur ou un médecin. La lecture intégrale porte sur les textes
des cartes. Les sources nouvelles ou sensibles ont été recroisées ; tous les liens historiques
n’ont pas fait l’objet d’un contrôle automatique de disponibilité.

## Vérifications de livraison

- `make check` : 308 cartes valides ; lint, formatage, types, schéma et 13 tests passent.
- Vérification distincte : 56 contrôles numériques, dont intégration de la consommation
  par 10 000 tranches et DTR calculée en secondes ; les exemples de rapports, bornes et
  lectures non numériques ont été relus séparément.
- Package : 308 GUID uniques, tous les champs HTML requis remplis, six nouvelles notes,
  zéro draft. Les 302 IDs et types conservés sont identiques au commit de départ.
- Traçabilité : 334 objectifs cochés ; toutes les correspondances de la couverture finale
  pointent vers des IDs actifs. Dix retraits récents et sept anciens IDs sont réservés.
- Rendu HTML à 390 px : cinq versos représentatifs inspectés visuellement, aucun débordement
  horizontal (CACI/QCM, consommation en remontée, DTR à deux arrêts, plafonds différents,
  schéma des détendeurs). Ce contrôle de navigateur n’est pas une revue visuelle des 308
  cartes dans Anki Desktop. Le SVG réellement contenu dans le package est présent et lisible.
- Anki : import réussi ; 325 notes conservées, dont 308 actives et 17 suspendues. Douze
  suspensions ciblées, aucune suppression ou réactivation. Les 319 noteIds/cardIds initiaux,
  les 132 révisions et les échéances, intervalles, facteurs et compteurs antérieurs sont
  identiques avant/après ; les rectos et les versos basic corrigés ont été contrôlés sur
  leurs noteIds d’origine. Synchronisation AnkiWeb réussie.
- Les notes et règles des agents ont été mises à jour ; les répétitions de la même règle
  sur les exercices numériques ont été consolidées, sans retirer cette préférence.
