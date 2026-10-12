# Clôture de l’implémentation N4 — 12 octobre 2026

La rédaction, la critique individuelle, les reprises et la vérification finale du
package sont terminées. [Couverture du référentiel](COUVERTURE_PLAN.md) ·
[Plan détaillé](../../IMPLEMENTATION_N4.md) · [Reprises](REPRISES_DETAILLEES.md).
Les revues sont effectuées par le même agent que la rédaction ; elles ne sont pas
présentées comme une validation indépendante.

## Résultat

| Élément | Nombre |
| --- | ---: |
| Base conservée dans N2 | 339 |
| Compléments conservés dans N3 | 122 |
| Créations dans N4 | 124 |
| Collection unique | **585** |
| Reprises existantes taguées N4 | 330 |
| Sélection pertinente N4 | **454** |

Les 143 objectifs nouveaux initiaux ont donné 121 créations après 22 absorptions.
Le recoupement final a ajouté trois cartes : accès au stage initial initiateur,
commissions culturelles et résistance inspiratoire dans la prévention de l’OPI.
Les 333 candidats de reprise ont tous un verdict individuel : 330 retenus, trois
conservés uniquement dans leurs niveaux antérieurs. Aucun doublon créé.

La collection contient 583 QCM et deux réponses libres. Les deux dernières demandent
respectivement de construire une organisation spatiale de surveillance et de formuler
un conseil de débriefing : la production concrète est l’objectif, avec plusieurs
formulations ou placements recevables. Les lots07–08 justifient ces formats.

Dans N4 : réglementation20, conduite7, désaturation4, anatomie/physiologie26,
prévention12, matériel33, matelotage15 et environnement7. Les modules ventilation et
circulation partagent une catégorie ; les fichiers restent des chapitres de rédaction.

## Vérifications factuelles et pédagogiques

- Lots01–34 : cartes nouvelles vérifiées puis critiquées, cinq identités au maximum.
- Lots35–101 : lecture du recto, de chaque choix et du corrigé de chaque reprise ; sources actuelles, calculs et contexte contrôlés. Les retouches de choix et de clarté sont tracées par ID.
- Lots102–103 : huit schémas fonctionnels de matériel et retrait d’un commentaire éditorial.
- Lots104–105 : trois lacunes distinctes du recoupement final complétées.
- Lots106–108 : légendes agrandies pour le téléphone, textes raccourcis et séparation du libellé Inflateur et de la flèche de gaz.
- Les 22 objectifs absorbés ont une correspondance explicite dans les revues. Les IDs cités dans la couverture finale existent dans le catalogue.
- Les contrôles G01–G11 sont clos pour les affirmations retenues ; versions, sources primaires et contradictions résolues figurent dans la couverture et `review.sources`.

Le MFT GP-N4 mai2026 définit le périmètre. Les cours anciens servent à comprendre et
s’entraîner ; aucun ancien barème, réglage de détendeur ou protocole de remontée n’est
transformé en prescription universelle. Les quatre QCM de nœuds testent les fonctions,
passages et séquences ; ils ne livrent pas les dessins de reconnaissance envisagés
initialement. Reconnaissance sur cordage, réalisation, gestes de secours, surveillance
réelle et maîtrise de l’oral restent à travailler en formation. Cette limite est
reflétée dans le plan, sans revendiquer une validation pratique par Anki.

## Vérification du dépôt et du package

`make check` final réussi : lint/format, typage sans erreur, schéma à jour,
585 cartes valides, **22 tests réussis et un test ignoré**. Le comportement de mélange
QCM est couvert par les tests du dépôt ; aucun algorithme ni template n’a été modifié
pour cette extension.

`make build` final réussi : `dist/diving-fr.apkg`, **585 notes et 585 cartes**,
aucune draft exclue. Les contrôles directs de la base embarquée confirment :

- 585 tags `card-id` uniques, correspondant exactement au catalogue ; GUID attendus et tags de niveau explicites.
- Les 465 identités déjà présentes dans HEAD conservent ID YAML, modèle et GUID ; aucun ID publié renommé, retiré ou réutilisé.
- Chaque carte est dans le paquet classique de son plus petit niveau : N2 avant N3 avant N4. Aucun paquet filtré ni Collection commune.
- Préréglage du dépôt : **10 nouvelles cartes et 200 révisions par jour**, embarqué dans le package.
- Les SVG sont intégrés au HTML ; aucun média distant nécessaire, aucune image de cours tiers embarquée. Le manifeste de média vide est donc attendu.

Les **2 340 vues** ont été rendues avec Chromium sans interface : recto/verso de
585 cartes, en largeurs800 et390. Aucun débordement horizontal, texte SVG hors
viewBox, erreur JavaScript ou séparateur absent/mal placé détecté. Les schémas N4 ont
également été inspectés visuellement ; les huit nouveaux schémas de matériel et les
vues mobile ont motivé puis confirmé les corrections de lisibilité. Les réponses
libres et le modèle Basic conservé des QCM sont inclus dans ce contrôle.

Cette inspection utilise les templates et champs extraits du package, sans ouvrir
Anki ni effectuer une séance de révision. Elle ne teste pas l’import sur tous les
clients Anki. Aucune collection utilisateur, échéance, suspension ou configuration
locale n’a été modifiée. Les IDs/GUID et modèles stables permettent la mise à jour
ultérieure des notes existantes ; leur historique réel n’a pas été manipulé.

Les templates, couleurs, typographie et présentation des QCM restent inchangés,
dans la continuité de WSET3. Les corrections graphiques concernent les schémas
pédagogiques et la lisibilité de leurs légendes, sans refonte du design général.

## Livrables et publication

YAML, SVG originaux intégrés, sources de vérification, plan, couverture, règles agents
et README sont mis à jour dans le dépôt. Les PDF privés et le package généré restent
hors Git. Les artefacts de rendu sont temporaires, sans ajouter de CSV massif au dépôt.

Conformément aux dernières consignes : **aucun commit, push Git ou `make push` AnkiConnect
n’a été effectué à cette clôture**. Le package local est prêt ; la release publique
reste celle de la dernière CI réussie jusqu’à publication de ces changements.
