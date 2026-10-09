# Revue pédagogique complète — 9 octobre 2026

## Périmètre et résultat

Les **448 cartes actives** ont été lues intégralement : question, chaque choix et
explication. **57 cartes corrigées**, **391 conservées**. Le catalogue reste à
308 cartes de base N2 et 140 compléments N3, sans création ni retrait.

La revue applique les cinq critères de [STUDY_CARD_QUALITY.md](../STUDY_CARD_QUALITY.md).
Le [relevé par ID](QUALITE_GLOBALE_2026-10-09.csv) contient la question examinée,
le verdict initial, les cinq verdicts finaux, le motif, la nouvelle critique et
une empreinte SHA-256 du contenu français final. Les motifs des cartes acceptées
précisent les points communs contrôlés dans leur chapitre ; ceux des cartes rejetées
décrivent leur défaut concret. Les verdicts sont des appréciations pédagogiques,
pas des mesures statistiques de difficulté auprès d’apprenants.

Lecture par chapitre, en lots de 33 cartes au maximum. Après correction, nouvelle
lecture des 57 cartes en deux lots de 30 et 27. Huit cartes ont demandé une retouche
supplémentaire, puis une troisième lecture. Ces passes ont été effectuées par le
même agent ; elles ne constituent pas une validation indépendante.

## Corrections principales

- Rectos qui donnaient la clé : intitulés d’écran déjà traduits, justification
  annoncée dans la question, profondeur du relief explicitement reliée à la côte.
- Leurres de catégories différentes, hors scénario ou caricaturaux : rôles du DP,
  causes contre actions, objet pénétrant à enfoncer, réimmersion dans un cas d’OPI.
- Différences de forme : clé détaillée face à des fragments, mauvaises réponses
  trahies par une restriction artificielle ou une précision expliquant leur erreur.
- Corrigés hérités d’anciens rectos : « Non » à une question d’action, références
  A/B disparues, négation sur une sonde qui n’était plus absente du scénario.
- Ambiguïtés : justificatifs N1 déjà vérifiés, champ complet d’une obligation,
  précision de l’arrondi demandé pour la composition de l’air.

Exemples : `n2-organisation-fiche-evacuation-001` interroge maintenant la disponibilité
préalable du document plutôt que la reconnaissance de son nom ;
`n2-ordinateurs-affichages-001` fait interpréter DIVE TIME et NDL ;
`n3-risques-opi-mecanisme-001` oppose trois mécanismes pulmonaires ;
`n3-secours-plaie-objet-penetrant-001` oppose laisser, retirer et mobiliser un objet.

## Répétitions et progression

La proximité N2/N3 sur la densité du gaz a conduit à retravailler
`n3-risques-densite-partielle-001` : le N2 porte le mécanisme respiratoire, le N3
applique la relation entre masse volumique et pression absolue par un rapport 7/3.
L’ID et le thème sont conservés ; ce n’est plus une simple paraphrase du mécanisme.

Les séries de pression, gaz, caps et tables sont conservées : calcul direct/inverse,
pression absolue/relative, stock utilisable, débits cumulés, somme des phases et
budget de retour apportent un entraînement utile. Les deux caps réciproques
travaillent aussi le passage par 360°. Les exercices chiffrés restent des modèles
explicitement fournis, sans transformation en procédures opérationnelles.

Les cartes voisines de prévention, reconnaissance et assistance sont conservées
lorsqu’elles testent des décisions distinctes. Les rappels d’un même principe dans
les corrigés restent utiles. Aucun retrait d’ID publié n’a été engagé et aucun
nouveau lot de cartes n’a été ajouté pour atteindre un quota. La difficulté d’un
rappel simple reste celle du fait à mémoriser ; elle n’est pas augmentée par du flou.

## Vérifications factuelles ciblées

Cette passe porte sur la qualité pédagogique de tout le catalogue. Elle conserve
les références et vérifications factuelles antérieures ; elle n’est pas un nouveau
recoupement exhaustif de tous les PDF ou de toutes les règles médicales. Les points
sensibles reformulés ont été confrontés aux références suivantes le 9 octobre :

- [Code du sport, A322-78](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000025393863/),
  matériel disponible, plan de secours et rappel depuis une embarcation : confirme
  le périmètre des cartes d’organisation retouchées.
- [FFESSM CMPN, prise en charge préhospitalière](https://medical.ffessm.fr/pec-d-un-accident-de-plongee-bouteille-ou-recycleur),
  texte publié en 2021 toujours proposé par la commission : alerte, oxygène,
  transmission et exclusions de l’hydratation orale, notamment en cas de dyspnée.
- [DAN, troubles pulmonaires et veineux](https://world.dan.org/health-medicine/health-resource/dive-medical-reference-books/the-heart-diving/pulmonary-and-venous-disorders/),
  rubrique IPE : mécanisme de l’œdème et prise en charge initiale.
- [DAN, oxygène d’urgence et toxicité](https://dan.org/alert-diver/article/emergency-oxygen-and-oxygen-toxicity/),
  toxicité neurologique et convulsions : confirme la distinction avec narcose et ADD.
- PDF primaire déjà présent `N3-S14`, PSC juillet 2026 : bilan, perte de connaissance,
  plaies (p. 43) et limites des gestes. Les nouvelles alternatives ne changent pas
  la conduite correcte de ces cartes.

Le nouveau rapport de densités est contrôlé avec ρ = PM/(RT) à température et
composition constantes : ρ60/ρ20 = 7/3. Aucun seuil médical ou réglementaire nouveau
n’a été introduit. Les sources des cartes restent conservées dans `review.sources`,
avec un lien vers cette revue pour chaque carte modifiée.

## Validation technique et livraison

- `make check` : lint, formatage, types, schéma et 448 cartes validés ; **18 tests
  réussis, 1 module optionnel ignoré**.
- Build par l’entrée CLI du dépôt : `diving-anki build --out dist`, **448 notes**.
- Comparaison avec l’état de départ : IDs, types, marqueurs `anki_model`, niveaux,
  tags, références d’objectif et destinations inchangés.
- Inspection de la base du `.apkg` : 448 GUID attendus, modèles historiques conformes,
  champs non vides et chaque choix présent. Relecture des champs exportés de cinq
  corrections représentatives, dont une QCM portée par le modèle Basic historique.
- Les templates et schémas n’ont pas changé. Aucun test de séance ni aucune action
  dans l’interface Anki ; aucune importation ou synchronisation effectuée pour cette revue.
  La conservation effective d’un historique local n’a donc pas été testée par migration.

## Répartition de la lecture

| Chapitre | Cartes relues | Cartes corrigées |
| --- | ---: | ---: |
| `cards/n2/01-prerogatives.yaml` | 20 | 6 |
| `cards/n2/02-organisation.yaml` | 20 | 5 |
| `cards/n2/03-documents-environnement.yaml` | 12 | 2 |
| `cards/n2/04-pression.yaml` | 24 | 2 |
| `cards/n2/05-flottabilite.yaml` | 25 | 1 |
| `cards/n2/06-gaz-autonomie.yaml` | 33 | 3 |
| `cards/n2/07-barotraumatismes.yaml` | 21 | 4 |
| `cards/n2/08-essoufflement.yaml` | 9 | 1 |
| `cards/n2/09-froid.yaml` | 9 | 2 |
| `cards/n2/10-narcose.yaml` | 14 | 1 |
| `cards/n2/11-add.yaml` | 26 | 1 |
| `cards/n2/12-tables.yaml` | 21 | 0 |
| `cards/n2/13-ordinateurs.yaml` | 20 | 5 |
| `cards/n2/14-remontees-anormales.yaml` | 10 | 1 |
| `cards/n2/15-gonflage-blocs.yaml` | 13 | 1 |
| `cards/n2/16-detendeurs.yaml` | 20 | 2 |
| `cards/n2/17-competences-transversales.yaml` | 8 | 1 |
| `cards/n2/18-lecture-pannes.yaml` | 3 | 0 |
| `cards/n3/01-prerogatives.yaml` | 16 | 0 |
| `cards/n3/02-organisation.yaml` | 9 | 3 |
| `cards/n3/03-planification.yaml` | 10 | 3 |
| `cards/n3/04-gaz.yaml` | 18 | 0 |
| `cards/n3/05-modeles.yaml` | 16 | 1 |
| `cards/n3/06-ordinateurs.yaml` | 9 | 1 |
| `cards/n3/08-risques.yaml` | 8 | 4 |
| `cards/n3/09-assistance.yaml` | 7 | 2 |
| `cards/n3/10-secours.yaml` | 27 | 3 |
| `cards/n3/11-materiel.yaml` | 2 | 0 |
| `cards/n3/12-orientation-milieu.yaml` | 18 | 2 |
