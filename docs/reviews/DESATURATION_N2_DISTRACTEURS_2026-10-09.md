# Désaturation N2 : revue approfondie des distracteurs — 9 octobre 2026

## Retour utilisateur et périmètre

La première revue globale restait trop indulgente : des clés seules prudentes,
des négations grossières, des choix hors sujet et des questions suggérant la réponse
étaient encore acceptés. Cette passe reprend **toutes les 77 cartes** du paquet
classique `Plongée::N2::Désaturation`, y compris celles partagées avec N3.
Elle ne déclare pas les autres catégories conformes au contrôle renforcé.

**52 cartes améliorées**, 25 conservées après examen des choix. Pas de création,
retrait ou changement de format ; le paquet complet reste à 448 cartes. IDs,
modèles Anki historiques, niveaux, tags, destinations et références d’objectifs
sont conservés. Les modèles Basic historiques portent toujours leurs QCM.

| Fichier | Relues | Modifiées |
| --- | ---: | ---: |
| `11-add.yaml` | 26 | 25 |
| `12-tables.yaml` | 21 | 8 |
| `13-ordinateurs.yaml` | 20 | 13 |
| `14-remontees-anormales.yaml` | 10 | 6 |

Le [relevé complet par ID et par choix](DESATURATION_N2_DISTRACTEURS_2026-10-09.csv)
contient le texte final de chaque leurre, la confusion qui le rend attirant,
le fait qui le réfute, le motif de réécriture, la relecture et l’empreinte du contenu.
Le relevé de la précédente passe reste une photographie antérieure ; ce nouveau
relevé remplace ses verdicts pour ces 77 IDs.

## Méthode et nouvelles règles

Lecture initiale des quatre fichiers par chapitre (26 cartes au maximum), puis
réécriture des cartes rejetées et seconde critique des rectos, de chaque choix
et des corrigés. Des propositions ont encore été rejetées à cette seconde étape :
valeur donnée dans le recto, liste administrative hors chronologie clinique,
voie cutanée inventée pour le gaz inerte, production d’azote par les muscles,
et qualification révélant trop facilement une fausse réponse. Les dernières
retouches ont fait l’objet d’une lecture supplémentaire. Même agent pour ces
passes ; aucune validation indépendante ou mesure de difficulté auprès d’apprenants.

Les nouvelles règles sont inscrites dans `AGENTS.md`, `CONTENT_GUIDELINES.md`,
`docs/STUDY_CARD_QUALITY.md`, `docs/CARD_DESIGN.md` et `CONTRIBUTING.md` :
justification de l’attrait et de la réfutation de chaque leurre, rejet des clés
seules prudentes, réécriture du recto au même objectif si nécessaire, et calcul
explicite des résultats faux. Une inversion ou un terme technique ne suffisent
pas à justifier un distracteur. Le contrôle d’unicité garde les mêmes hypothèses
pour tous les choix ; la difficulté ne se fabrique pas avec une ambiguïté.

## Changements représentatifs

- **Henry** : doubler la pression partielle donne des réponses quantitatives.
  Les erreurs viennent de la fraction de gaz inchangée ou de Boyle-Mariotte,
  plutôt qu’une affirmation sur le temps incompatible avec l’équilibre demandé.
- **Élimination de l’azote** : transport dissous et filtration des bulles ne sont
  pas la même étape ; la troisième voie compare gaz inerte et déchets azotés rénaux.
- **ADD cutané** : trois atteintes de plongée réelles remplacent la clé prudente
  opposée à une allergie déclarée certaine. Le corrigé distingue marbrures,
  emphysème sous-cutané et tableau respiratoire, sans faire un diagnostic certain.
- **Oxygène** : distinguer l’aide aux échanges gazeux, la recompression et une
  prétendue stimulation ventilatoire. L’alerte et l’apport d’oxygène restent expliqués.
- **Chronologie** : le début des anomalies observées peut précéder la première
  plainte ; date du brevet ou du CACI ne servent plus de leurres hors sujet.
- **Tables** : DTR complète, accès au premier palier et seule somme des arrêts
  sont des confusions proches. Le calcul DTR 12 min explique aussi le faux 13 min
  obtenu en appliquant 10 m/min au trajet initial au lieu de 15.
- **Ordinateurs** : les choix comparent données mesurées et calculées, paramètres
  du modèle, historique du porteur précédent, arrêt/plafond et coût du retour.
  Deux plafonds de 6 et 3 m s’opposent à leur moyenne 4,5 m, sans expliquer le
  mot plafond dans le recto. Les choix de modes n’annoncent plus leur propre erreur.
- **Rattrapages** : les alternatives opposent branches et séquences étudiées
  (MN90, texte 2024, rupture limitée de palier, présence de signes). Elles ne se
  résument plus à secours contre imprudence grossière. Les conditions médicales,
  délais, gaz et assistance restent déterminants.

## Sources et contrôle factuel

Références factuelles antérieures conservées. Les nouvelles distinctions sensibles
et les paramètres retouchés ont été confrontés aux sources primaires suivantes,
consultées le **9 octobre 2026** :

- [FFESSM, MN90 juillet 2005](https://ffessm-ctr-aura.fr/wp-content/uploads/2019/03/MN90.pdf),
  généralités et convention de DTR, p.1 et 8 : domaine, durées, arrondis et vitesses.
- [Suunto Zoop Novo : décompression](https://www.suunto.com/Support/Product-support/suunto_zoop_novo/suunto_zoop_novo/features/decompression-dives/)
  et [vitesse](https://www.suunto.com/Support/Product-support/suunto_zoop_novo/suunto_zoop_novo/features/ascent-rate/) :
  plafond, évolution des indications et seuil d’alarme. Les valeurs du fabricant
  restent distinctes de celles des MN90 et du repère fédéral air.
- [FFESSM, préconisations de novembre 2024](https://ffessm.fr/uploads/media/docs/0001/12/1e862af90f137e0c9bf98859c31092e14b8a3c5e.pdf),
  p.1–2, croisées avec le PDF CTN mai 2025, p.2, et
  [l’article fédéral](https://subaqua.ffessm.fr/article/procedures-rattrapage-remontee-anormale-ordinateur).
  Le PDF CTN a aussi été contrôlé visuellement. La branche remontée rapide sans
  réimmersion n’est pas remplacée par la surveillance de rupture limitée de palier.
- PDF RIFAP mai 2026, p.32 : avis médical pour tout incident et transmission des
  évolutions. L’avis médical complète la surveillance du texte de 2024.
- [FFESSM CMPN, prise en charge](https://medical.ffessm.fr/pec-d-un-accident-de-plongee-bouteille-ou-recycleur)
  et RIFAP : oxygène, hydratation, surveillance et coordination médicale.
- [DAN, manifestations de désaturation](https://dan.org/health-medicine/health-resources/diseases-conditions/decompression-illness-what-is-it-and-what-is-the-treatment/),
  signes discrets et retardés ; [facteurs de stress de décompression](https://dan.org/health-medicine/health-resource/dive-medical-reference-books/decompression-sickness/contributing-factors/),
  effort et circulation ; [barotraumatisme et emphysème](https://dan.org/alert-diver/article/barotrauma-in-bonaire/),
  distinction des crépitements sous-cutanés.
- [DAN, vol après plongée](https://world.dan.org/health-medicine/health-resource/health-safety-guidelines/guidelines-for-flying-after-diving/),
  repère 18 h conservé avec son contexte de plongées multiples sans palier.

Cette passe ne recoupe pas à nouveau tout le contenu de tous les PDF ; elle vérifie
les distinctions nécessaires aux réécritures, en gardant les sources détaillées
par carte. Les hypothèses des calculs restent explicites. Pas de seuil médical
nouveau inventé pour construire une fausse réponse.

## Validation

`make check` : 448 cartes validées, lint/format/types/schéma conformes,
**18 tests réussis, 1 module ignoré**. Build : `diving-fr.apkg`, **448 notes**.
Contrôle de la base exportée : GUID et modèles historiques attendus, choix présents
et champs remplis. Rectos/versos exportés relus sur des corrections représentatives
(physiologie, tables, ordinateur, procédure). Comparaison de l’ensemble des 77 IDs,
types, modèles, niveaux, tags et destinations avec l’état avant cette passe.

Aucune importation ou synchronisation dans Anki pendant cette revue et aucune
action dans son interface. L’historique local n’a pas été modifié ; le contrôle
porte sur la stabilité des identités exportées, pas sur une migration exécutée.
