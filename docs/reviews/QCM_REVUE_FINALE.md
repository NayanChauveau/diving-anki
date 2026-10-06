# Revue finale des formats, de la clarté et des choix

Revue du **6 octobre 2026**, sur les **308 cartes des 18 chapitres**, à partir de la
première passe QCM et de la reprise N2/N3 encore non committées.

## Bilan

- **308 QCM, aucune réponse libre restante** : ce résultat suit l’examen des questions,
  sans quota imposé ni exclusion de principe d’un autre format futur.
- Les **47 exceptions initiales** ont toutes une formulation QCM pertinente : 44 calculs,
  un schéma fonctionnel et deux séquences de rattrapage. Elles sont converties sans
  modifier leurs IDs, modèles Anki ni appartenances.
- **68 QCM déjà présents corrigés** ; les 193 autres QCM sont conservés après relecture.
- 308 objectifs et notes uniques conservés ; N2=308, N3=164, N4=0.

Le [registre exhaustif](QCM_REVUE_FINALE.csv) comporte une décision, un motif,
le recto final et les choix pour chaque ID. La difficulté évaluée est éditoriale :
confusions du cours et erreurs de méthode, pas une mesure statistique auprès d’apprenants.
Les tests techniques ne remplacent pas cette relecture.

## Pourquoi les anciennes réponses libres passent en QCM

Pour les pressions, les faux résultats viennent de l’oubli ou du double comptage de
l’atmosphère, de l’inversion d’un rapport ou du signe. Pour la flottabilité, ils viennent
du signe du poids apparent, des unités N/kg/L ou du volume propre du lest. Pour le gaz,
ils viennent de la pression absolue, de l’omission de réserve, de phases calculées à une
seule profondeur, d’un seul équipier compté ou d’une réserve confondue avec le stock utilisable.
Les solutions détaillées restent au verso ; aucune hypothèse ni unité n’est retirée.

Le schéma du détendeur ne donne plus les pressions sur ses flèches : le lecteur doit
connaître les deux réductions, et distinguer pression ambiante, pression intermédiaire
et pression fixe de surface. Les deux séquences du texte 2024 opposent des profondeurs,
durées ou reprises différentes, en conservant la faisabilité et l’absence de symptômes
explicitement dans les énoncés.

## Corrections de fond de la relecture

- `n2-pression-double-atmosphere-001` proposait deux descriptions de la même erreur :
  double comptage de l’atmosphère et confusion absolue/relative. Nouvelle demande :
  retenir la pression ambiante correcte, parmi trois traitements différents de l’affichage.
- Plusieurs rectos demandaient une cause alors que les choix proposaient des actions,
  notamment narcose/équipier et eau froide/détendeur : demande et réponses désormais alignées.
- Les leurres de moyenne arbitraire, de variation spontanée du gaz du bloc, de pression
  respirée changée par le lest, de soupape fictive du premier étage ou de fonctions de
  journal hors question sont remplacés par des erreurs liées au concept étudié.
- Les conditions de l’eau à boire désignent les troubles de conscience, déglutition,
  respiration, nausées ou vomissements, sans exclure tout « trouble digestif » indéfini.
- Les contrôles d’ordinateur, la révision SCUBAPRO et le rinçage de modèles identifiés
  ont un périmètre précis ; les alternatives sont de même catégorie et comparables.
- Les scénarios d’accident conservent un diagnostic ouvert lorsqu’il ne peut être établi
  à partir des seuls signes. Les repères numériques sont propres au texte ou au modèle cité.

## Sources et résolution des points sensibles

Les références factuelles des YAML et les revues antérieures restent conservées.
Relecture ciblée renouvelée contre les sources primaires suivantes :

- [Code du sport A322-80](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000025393859) : matériel individuel, partage de gaz sans embout commun, équipements de l’encadrant et parachute collectif.
- [CMPN FFESSM, accident de plongée](https://medical.ffessm.fr/cat-accident-de-plongee-bouteille-ou-recycleur) : bilan vital, alerte, oxygène, installation et aptitude à boire.
- [DAN, hypothermie](https://dan.org/health-medicine/travelers-medical-guide/travel-related-injuries/exposure-related-injuries/) : confusion, fin des frissons, manipulation douce et risque cardiaque.
- [DAN, équilibrage](https://dan.org/health-medicine/health-resource/dive-medical-reference-books/ears-diving/ears-equalization/) : trompes, conduite sans forcer et position tête en haut.
- [MN90 fédérales, juillet 2005](https://ffessm-ctr-aura.fr/wp-content/uploads/2019/03/MN90.pdf) : domaine d’emploi, arrondis, successives et calculs de remontée.
- [Suunto Zoop Novo, manuel](https://us.suunto.com/pages/suunto-zoop-novo-user-guide) : SLOW au-delà de 10 m/min, affichages, plafonds et verrouillage du modèle.
- SCUBAPRO, juillet 2025 Rev Q, **p.16–17**, [notice officielle](https://johnsonoutdoors.widen.net/s/hlkmf7vhpb/sp_45101180_revq_reg_manual_202507_fra) : exemplaire déjà téléchargé et extrait relu, le lien étant inaccessible au navigateur de recherche pendant cette passe. Rinçage : bouchon HP fermé et dispositif anti-marquage R195/G260 non engagé ; révision tous les 2 ans, suivi renforcé en usage fréquent.

### Avis médical après palier manqué

Le [texte fédéral de novembre 2024](https://ffessm.fr/uploads/media/docs/0001/12/1e862af90f137e0c9bf98859c31092e14b8a3c5e.pdf), p.1–2,
prévoit observation 3 h et absence de plongée 24 h pour la branche sans symptômes et
jusqu’à 3 min de palier manqué quand la réimmersion est impossible.
Le [RIFAP de mai 2026](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/f65d4fd1-beec-4dff-a803-b36101f71f88), p.32,
demande un avis médical pour tout incident ou accident de plongée, via le CROSS en mer.
Ces deux exigences ne s’excluent pas : le suivi ne remplace pas l’appel médical.
La carte `n2-remontees-anormales-observation-001` le demande désormais explicitement,
sans attendre les premiers signes. Cette correction clôt la lecture « observation seule »
pour cette carte N2 ; les autres adaptations/revalidations N3 restent à traiter dans leur lot.

## Contrôles avant publication

- `make check` : lint, format, typage, schéma, 308 cartes et 17 tests réussis.
- Import Anki séparé : 4 cas réussis, moteurs classique (AnkiConnect) et actuel, avec réimports, conversion Basic → QCM et maintien des suspensions, échéances et historique.
- `make build` : 308 notes et cartes uniques ; inspection SQLite des choix, réponses, tags, champs, modèles et GUIDs conforme au catalogue publié.
- Contrôle arithmétique indépendant des erreurs de pression, réserve, deux équipiers, plusieurs phases et DTR ; solutions détaillées conservées.
- Aperçu visuel contrôlé : schéma sans libellés de réponse, trois choix lisibles, sélection d’un leurre et correction dans le même ordre.
- L’import réel et la synchronisation AnkiWeb seront effectués via `make push` après le commit ; comparaison de la collection locale prévue sur les mêmes 308 identités et leurs révisions.
