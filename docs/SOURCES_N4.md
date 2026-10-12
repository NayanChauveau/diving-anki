# Sources pour la théorie N4 — recherche du 12 octobre 2026

## Livrable et périmètre

**Corpus initial : 59 PDF téléchargés, 1 050 pages**, dans `sources/n4/`. Le corpus comprend
18 cours de Philippe Jourdren, cinq références nationales FFESSM, 25 PDF de cours
et fiches du CoDep 92, un cours du CoDep 93, huit annales/recueils, un support de
matelotage et un cours de circulation d’Arnaud Melese.

Cette étape est une acquisition documentaire et un repérage des thèmes, **pas une
revue factuelle complète des 1 050 pages**. Cet état initial est conservé comme historique. L’implémentation et le recoupement
ont depuis été réalisés : [plan N4](IMPLEMENTATION_N4.md),
[couverture finale](reviews/n4/COUVERTURE_PLAN.md). Le corpus local complété comporte
**61 PDF, 1 101 pages** ; les notices et références primaires supplémentaires sont
consignées précisément dans les sources des cartes et les revues de lots.

Les PDF et leurs extractions restent locaux, ignorés par Git conformément aux règles
du dépôt. Cet inventaire et [le manifeste public](reviews/SOURCES_N4.json) donnent
les liens de téléchargement, versions observées, pages et empreintes SHA-256.
Les versions de cours, dates de révision et dates de mise en ligne sont distinguées.
Un manifeste identique et les textes paginés sont dans `sources/n4/manifest.json`
et `sources/n4/text/`. Trois références sont identiques à des fichiers déjà utilisés
pour N3 ; elles sont signalées dans le manifeste, sans prétendre être des sources nouvelles.

## Référence principale et changement de programme

Le point de départ est **N4-S01 : MFT FFESSM GP-N4, version mai 2026**, 33 pages,
révision du 23 mai 2026 et mise en ligne du 14 juin 2026 dans l’index national
[MFT](https://mft.ffessm.fr). Les pages physiques 25 à 29 détaillent les épreuves
théoriques ; les pages 3 à 6, 15 à 18 et 20 éclairent le rôle de guide, l’environnement,
la conduite de palanquée et le matelotage.

Le journal des modifications, page 33, signale la **suppression de l’épreuve séparée
« aspects théoriques de l’activité » en décembre 2025**. Le programme actuel comporte
les épreuves de désaturation (10), anatomie/physiologie/physiopathologie (11), cadre
réglementaire (12) et matériel (13, oral). Il ne faut donc pas reprendre la numérotation,
les coefficients ou le programme des annales 2025 comme références actuelles.
Les connaissances physiques restent utiles lorsqu’elles servent les compétences
et les situations du programme ; chaque approfondissement sera évalué pour son apport.

Autre repère utile : les connaissances des niveaux antérieurs sont considérées comme
maîtrisées, avec possibilité de les vérifier à l’évaluation. Cela va dans le sens du
projet : **N2 demeure la base, N3 le premier complément, N4 apporte les objectifs
manquants et les applications propres au guide**, sans recopier les cartes existantes.
Un fait connu et une décision nouvelle du GP peuvent constituer deux objectifs différents.

## Comment utiliser le corpus ensuite

| Famille de connaissances | Sources de travail | Apport à rechercher avant toute carte N4 |
| --- | --- | --- |
| Accueil, briefing, conduite et adaptation de la palanquée | MFT ; Jourdren briefing et encadrement ; CoDep 92 conduite ; recueils Martinique GP | Décisions du guide, évaluation des plongeurs, consignes, surveillance et adaptation à des plongeurs encadrés |
| Désaturation et procédures hétérogènes | MFT ; Jourdren pressions/dissolution, modèles et ADD ; CoDep 93 ordinateurs ; CoDep 92 tables ; corrigés Martinique | Raisonnement de guide, gestion collective des profils et ordinateurs, mécanismes et exercices réellement distincts du N2/N3 |
| Ventilation, circulation, oreille et effort | MFT ; Jourdren appareils respiratoire/circulatoire, oreille et système nerveux ; Melese circulation 2024 | Liens fonctionnels et décisions de prévention ; comparer avec les objectifs déjà interrogés dans N2/N3 |
| Accidents et prévention pour un GP | MFT et RIFAP ; Jourdren froid, apnée, narcose, OPI, ADD et barotraumatismes ; CoDep 92 accidents | Reconnaissance et conduite adaptées au rôle de guide ; revalider les protocoles avec les sources actuelles |
| Matériel, lecture d’éclatés et fonctionnement | MFT ; Jourdren matériel ; 17 fiches de Patrick Poincelet | Distinctions de mécanismes, pannes et configurations ; contrôler les variantes dans les notices fabricants |
| Cadre fédéral, responsabilité et accueil des pratiquants | MFT et généralités ; Jourdren réglementation ; annales BFC et Martinique | Prérogatives, honorabilité, signalement, responsabilités ; vérifier le Code du sport consolidé à la rédaction |
| Milieu, environnement et sensibilisation | MFT ; Jourdren protection de l’environnement ; CoDep 92 accidents liés au milieu | Choix et comportements du guide, connaissance du milieu ; approfondissements utiles plutôt que reconnaissance exhaustive des espèces |
| Matelotage et participation à l’organisation | MFT ; Gilles Foubert ; références ANFR déjà acquises en N3 | Nœuds, mouillage, manœuvres, repères et communication ; séparer savoir théorique et geste pratique |
| Physique appliquée et calculs | Jourdren physique et dissolution ; CoDep 92 physique 1/2 ; annales | Conserver les applications utiles au programme actuel ; éviter de recréer les exercices N2/N3 sans opération ou contrainte supplémentaire |

Ce tableau indique des pistes bibliographiques. Il n’affirme pas que tous ces sujets
manquent aujourd’hui : le futur audit devra lire les cartes existantes, pas seulement
chercher les termes dans les YAML.

## Statut et précautions propres aux sources

- Les cinq documents FFESSM proviennent de l’API liée à l’index MFT actuel.
  Leur champ d’application et leur version seront recontrôlés lors de la rédaction.
- Les cours Jourdren portent des mises à jour de 2024 à octobre 2026. Ils sont utiles
  pour les explications, mais ne se substituent pas au référentiel ou aux notices.
  L’auteur précise les conditions d’utilisation sur sa page et cite les schémas
  d’Alain Foret / Illustra-Pack : ne pas recopier ces illustrations dans les cartes.
- Les cours CoDep 92 sont principalement de 2020–2022 ; plusieurs fiches de matériel
  ne portent pas de date exploitable. Le mot « Nouveau » de l’index ne prouve pas
  une édition récente. La version circulation janvier 2024 est acquise en complément
  de celle de janvier 2022, pas comme source indépendante d’un autre auteur.
- Les annales BFC juin 2025 et les recueils corrigés Martinique non datés servent
  d’exemples de tâches. Les corrigés ne constituent pas une validation scientifique
  ou une garantie de conformité au programme mai 2026. Certaines questions de tables
  portent sur des procédures anciennes, des profondeurs ou des usages de l’oxygène
  dont le périmètre devra être contrôlé avant adaptation.
- Le document de Gilles Foubert est diffusé par un article de juin 2005 et cite des
  règles anciennes. Retenir les notions nautiques pertinentes ; revalider la division
  240, les communications et les règles de sécurité avec leurs publications actuelles.
- L’oreille est explicitement rattachée aux acquis N3 dans le MFT actuel ; la narcose
  et l’OPI ont des limites de connaissances précisées page 26. Ne pas transformer
  automatiquement chaque diapositive des cours en exigence d’examen.

## Inventaire des PDF acquis

La pagination est physique, à partir de 1. Les liens locaux fonctionnent dans cette
copie du dépôt ; les URL de source permettent l’acquisition dans une autre copie.
Pour un PDF extrait d’une archive, le manifeste précise l’URL ZIP, le membre extrait
et l’empreinte de l’archive. Les 17 fiches de matériel constituent un seul ensemble
pédagogique ; leur nombre de fichiers n’impose aucun découpage du futur deck.

| Référence | Document local | Pages | Édition observée | Origine |
| --- | --- | ---: | --- | --- |
| N4-S01 | [Niveau 4 - Guide de palanquée](../sources/n4/ffessm-niveau-4-guide-de-palanquee.pdf) | 33 | Mai 2026 | [Source](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/ce05a4c2-a73f-4f6e-b7d7-e5cf09751528) |
| N4-S02 | [Recommandations de la CTN](../sources/n4/ffessm-recommandations-de-la-ctn.pdf) | 4 | Mai 2025 | [Source](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/53a34a0f-7c3f-4eb5-9c52-32284b2e1151) |
| N4-S03 | [RIFAP Réactions et Intervention face à un Accident de Plongée](../sources/n4/ffessm-rifap-reactions-et-intervention-face-a-un-accident-de-plongee.pdf) | 38 | Mai 2026 | [Source](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/a8b1dadb-cd94-4046-86c5-8790f32716e5) |
| N4-S04 | [Formation - Délivrance - Certifications](../sources/n4/ffessm-formation-delivrance-certifications.pdf) | 4 | Janvier 2025 | [Source](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/fea9d5b9-09da-4e61-a417-997751211424) |
| N4-S05 | [Brevets Fédéraux - Généralités](../sources/n4/ffessm-brevets-federaux-generalites.pdf) | 5 | Janvier 2025 | [Source](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/fb7a6abb-20e5-4e5b-a3a6-9a074422637c) |
| N4-S06 | [Barotraumatismes](../sources/n4/jourdren-barotraumatismes.pdf) | 22 | Août 2024 | [Source](https://drive.google.com/uc?export=download&id=1XC3HpXPwgtw58r7a2XokmLbolbb1gIzV) |
| N4-S07 | [Pressions partielles et dissolution](../sources/n4/jourdren-pressions-partielles-et-dissolution.pdf) | 22 | Août 2024 | [Source](https://drive.google.com/uc?export=download&id=1v0N0AcQlBezE1J22vkNliOZeD6wUi-Hf) |
| N4-S08 | [Modèles de décompression](../sources/n4/jourdren-modeles-de-decompression.pdf) | 29 | Janvier 2026 | [Source](https://drive.google.com/uc?export=download&id=1yd02fOuSfaj1jgCkTvYZkyX3EqBH291d) |
| N4-S09 | [Briefing et Débriefing](../sources/n4/jourdren-briefing-et-debriefing.pdf) | 15 | Septembre 2025 | [Source](https://drive.google.com/uc?export=download&id=1lVtfeaXKDEI8K8J7iOkq1bupEJBHt9lc) |
| N4-S10 | [Protection de l'environnement](../sources/n4/jourdren-protection-de-l-environnement.pdf) | 29 | Août 2024 | [Source](https://drive.google.com/uc?export=download&id=1j3N8a_LutM5Wjp6hqsedQ6QdQwjfQbkf) |
| N4-S11 | [Matériel](../sources/n4/jourdren-materiel.pdf) | 37 | Septembre 2025 | [Source](https://drive.google.com/uc?export=download&id=12X_4lql-hG73AXw38XrK8MTaXOX9KNW8) |
| N4-S12 | [Réglementation](../sources/n4/jourdren-reglementation.pdf) | 39 | Novembre 2025 | [Source](https://drive.google.com/uc?export=download&id=10WnEpitcGXMz4tlt-MPrdjPrWBkS54lq) |
| N4-S13 | [Physique](../sources/n4/jourdren-physique.pdf) | 23 | Août 2024 | [Source](https://drive.google.com/uc?export=download&id=1Ud6AjEMtiw0v3lLcQkQR5fDEEniacxlN) |
| N4-S14 | [Le froid en plongée](../sources/n4/jourdren-le-froid-en-plongee.pdf) | 20 | Septembre 2025 | [Source](https://drive.google.com/uc?export=download&id=1omPrguWUPSQMzwGpiIi9B2dJEwaI3MP9) |
| N4-S15 | [L'oreille du plongeur](../sources/n4/jourdren-l-oreille-du-plongeur.pdf) | 23 | Octobre 2025 | [Source](https://drive.google.com/uc?export=download&id=1Y9Th8zWF6ZfIXGX_rY5e8RysAKP3YylM) |
| N4-S16 | [L'appareil respiratoire](../sources/n4/jourdren-l-appareil-respiratoire.pdf) | 30 | Octobre 2025 | [Source](https://drive.google.com/uc?export=download&id=1jWIaimd_PWd62S0Kix6DRcZ27TktYwRx) |
| N4-S17 | [L'appareil circulatoire](../sources/n4/jourdren-l-appareil-circulatoire.pdf) | 27 | Septembre 2025 | [Source](https://drive.google.com/uc?export=download&id=1dfUH2Yo7ajVvljv4gkUTHbj4gwpq_i4D) |
| N4-S18 | [L'apnée](../sources/n4/jourdren-l-apnee.pdf) | 19 | Décembre 2025 | [Source](https://drive.google.com/uc?export=download&id=1F8z6iMuHIvou1beBWCWIiYqADg42kFfe) |
| N4-S19 | [Le système nerveux](../sources/n4/jourdren-le-systeme-nerveux.pdf) | 23 | Septembre 2025 | [Source](https://drive.google.com/uc?export=download&id=1xZ_AaEdIGH9ztBZqw7AUspvI8pXk6RlH) |
| N4-S20 | [Encadrement et plongée profonde](../sources/n4/jourdren-encadrement-et-plongee-profonde.pdf) | 17 | Octobre 2025 | [Source](https://drive.google.com/uc?export=download&id=1_nG5VcXOT423CGvGaFjB6c3_cwM-oADy) |
| N4-S21 | [L'œdème pulmonaire d'immersion](../sources/n4/jourdren-l-deme-pulmonaire-d-immersion.pdf) | 18 | Octobre 2025 | [Source](https://drive.google.com/uc?export=download&id=1GeM_uGrkXrs8-gOVPJqiYGvjQAIS7pdH) |
| N4-S22 | [L'accident de désaturation](../sources/n4/jourdren-l-accident-de-desaturation.pdf) | 30 | Novembre 2025 | [Source](https://drive.google.com/uc?export=download&id=1oFpe4blvbNyu3OhQfRT5NrqKzFRIyKIk) |
| N4-S23 | [La narcose et le guide de palanquée](../sources/n4/jourdren-la-narcose-et-le-guide-de-palanquee.pdf) | 19 | Octobre 2026 | [Source](https://drive.google.com/uc?export=download&id=1uo2Qp98jKJ2XGRkbP_77ABaglzR_5ZHV) |
| N4-S24 | [Accidents Biochimiques N4_Codep92.pdf](../sources/n4/codep92-accidents-biochimiques-n4-codep92.pdf) | 33 | 20 février 2021, v1.1 | [Source](https://ffessm-cd92.com/telecharge/Accidents%20Biochimiques%20N4_Codep92.pdf) |
| N4-S25 | [Accidents.pdf](../sources/n4/codep92-accidents.pdf) | 36 | Février 2021 | [Source](https://ffessm-cd92.com/telecharge/Accidents.pdf) |
| N4-S26 | [ConduiteDePalanquee_N4_.pdf](../sources/n4/codep92-conduitedepalanquee-n4.pdf) | 57 | 2022 (signature Ivan Tousnakhoff ; cite le MFT mai 2021) | [Source](https://ffessm-cd92.com/telecharge/ConduiteDePalanquee_N4_.pdf) |
| N4-S27 | [Cours Tables MN90_Codep 92_2022.pdf](../sources/n4/codep92-cours-tables-mn90-codep-92-2022.pdf) | 25 | 2022 dans le nom du fichier ; édition interne non identifiée | [Source](https://ffessm-cd92.com/telecharge/Cours Tables MN90_Codep 92_2022.pdf) |
| N4-S28 | [A Détendeurs Définitions](../sources/n4/codep92-fiches-materiel-pdf-a-detendeurs-definitions.pdf) | 4 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S29 | [B Détendeurs Fonctionnement](../sources/n4/codep92-fiches-materiel-pdf-b-detendeurs-fonctionnement.pdf) | 1 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S30 | [C Détendeurs Pannes courantes](../sources/n4/codep92-fiches-materiel-pdf-c-detendeurs-pannes-courantes.pdf) | 2 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S31 | [D Détendeurs Givrage](../sources/n4/codep92-fiches-materiel-pdf-d-detendeurs-givrage.pdf) | 2 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S32 | [E 1er étagePiston Simple](../sources/n4/codep92-fiches-materiel-pdf-e-1er-etagepiston-simple.pdf) | 3 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S33 | [F 1er étage Piston Compensé](../sources/n4/codep92-fiches-materiel-pdf-f-1er-etage-piston-compense.pdf) | 3 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S34 | [G 1er étage Membrane  Compensé](../sources/n4/codep92-fiches-materiel-pdf-g-1er-etage-membrane-compense.pdf) | 4 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S35 | [H 1er étage Piston Surcompensé](../sources/n4/codep92-fiches-materiel-pdf-h-1er-etage-piston-surcompense.pdf) | 2 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S36 | [I 1er étage Membrane Surcompensé](../sources/n4/codep92-fiches-materiel-pdf-i-1er-etage-membrane-surcompense.pdf) | 4 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S37 | [J 2eme étage simple](../sources/n4/codep92-fiches-materiel-pdf-j-2eme-etage-simple.pdf) | 4 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S38 | [K 2eme compensé](../sources/n4/codep92-fiches-materiel-pdf-k-2eme-compense.pdf) | 3 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S39 | [L 2eme étage co axial](../sources/n4/codep92-fiches-materiel-pdf-l-2eme-etage-co-axial.pdf) | 2 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S40 | [M Compresseur](../sources/n4/codep92-fiches-materiel-pdf-m-compresseur.pdf) | 5 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S41 | [N  Inflateurs](../sources/n4/codep92-fiches-materiel-pdf-n-inflateurs.pdf) | 4 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S42 | [O Manomètres](../sources/n4/codep92-fiches-materiel-pdf-o-manometres.pdf) | 3 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S43 | [P Robinet](../sources/n4/codep92-fiches-materiel-pdf-p-robinet.pdf) | 2 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S44 | [Q Trucs et astuces](../sources/n4/codep92-fiches-materiel-pdf-q-trucs-et-astuces.pdf) | 2 | Non identifiée dans les pages de repérage | [Source](https://ffessm-cd92.com/telecharge/Fiches_Materiel_PDF.zip) |
| N4-S45 | [L'appareil circulatoire](../sources/n4/codep92-l-appareil-circulatoire-pdf-l-appareil-circulatoire.pdf) | 28 | Janvier 2022 | [Source](https://ffessm-cd92.com/telecharge/L%27appareil%20circulatoire.pdf.zip) |
| N4-S46 | [L'oreille v3.pdf](../sources/n4/codep92-l-oreille-v3.pdf) | 31 | Janvier 2020 | [Source](https://ffessm-cd92.com/telecharge/L%27oreille%20v3.pdf) |
| N4-S47 | [Physique N4 2021 Codep92 Partie 1](../sources/n4/codep92-physique-n4-2021-codep92-partie-1-pdf-physique-n4-2021-codep92-partie-1.pdf) | 53 | 2021 (titre) | [Source](https://ffessm-cd92.com/telecharge/Physique%20N4%202021%20Codep92%20Partie%201.pdf.zip) |
| N4-S48 | [Physique N4 2021 Codep92 Partie 2](../sources/n4/codep92-physique-n4-2021-codep92-partie-2-pdf-physique-n4-2021-codep92-partie-2.pdf) | 36 | Décembre 2021 | [Source](https://ffessm-cd92.com/telecharge/Physique%20N4%202021%20Codep92%20Partie%202.pdf.zip) |
| N4-S49 | [Ordinateurs GP-N4 CoDep 93](../sources/n4/ordinateurs-gp-n4-codep-93.pdf) | 31 | 21 mars 2025 | [Source](https://codep93.fr/uploads/menus/433/vUTGaBHIZFgKNx8LzPpucSoCtlfX3sMmr6A9Rj072iO/media/lesordinateurs.pdf) |
| N4-S50 | [Annale BFC juin 2025 02-Reglementation](../sources/n4/annale-bfc-juin-2025-02-reglementation.pdf) | 2 | Session juin 2025 | [Source](https://technique.ffessm-bfc.fr/uploads/file_manager/rug4ifBAS1d4EHvoNsdaOloSHpTCrqkBf75zBVawqkw/Annales/2025/GPN4-JUIN/02-Reglementation 062025 BFC - vierge.pdf) |
| N4-S51 | [Annale BFC juin 2025 03-Anatomie](../sources/n4/annale-bfc-juin-2025-03-anatomie.pdf) | 5 | Session juin 2025 | [Source](https://technique.ffessm-bfc.fr/uploads/file_manager/rug4ifBAS1d4EHvoNsdaOloSHpTCrqkBf75zBVawqkw/Annales/2025/GPN4-JUIN/03-Anatomie 062025 BFC.pdf) |
| N4-S52 | [CTR Martinique Tables classiques corrigées](../sources/n4/ctr-martinique-tables-classiques-corrigees.pdf) | 25 | Non identifiée dans les pages de repérage | [Source](https://www.ctrmartinique.com/_files/ugd/bef5df_7b8d690bf5ac4099ba25c5803aad36f8.pdf) |
| N4-S53 | [CTR Martinique Accidents de désaturation corrigés](../sources/n4/ctr-martinique-accidents-de-desaturation-corriges.pdf) | 9 | Non identifiée dans les pages de repérage | [Source](https://www.ctrmartinique.com/_files/ugd/bef5df_3a2b078445da489f9ff731fee4775788.pdf) |
| N4-S54 | [CTR Martinique Oreille corrigée](../sources/n4/ctr-martinique-oreille-corrigee.pdf) | 3 | Non identifiée dans les pages de repérage | [Source](https://www.ctrmartinique.com/_files/ugd/bef5df_2f15a83925c040ecb2a2b9e9cb6efb44.pdf) |
| N4-S55 | [CTR Martinique Rôle du GP corrigé](../sources/n4/ctr-martinique-role-du-gp-corrige.pdf) | 14 | Non identifiée dans les pages de repérage | [Source](https://www.ctrmartinique.com/_files/ugd/bef5df_20fbf79e6a694f4d8a0f4c5426c460d4.pdf) |
| N4-S56 | [CTR Martinique Physiopathologie du guide corrigée](../sources/n4/ctr-martinique-physiopathologie-du-guide-corrigee.pdf) | 3 | Non identifiée dans les pages de repérage | [Source](https://www.ctrmartinique.com/_files/ugd/bef5df_ef65f272e4794e459678481571aaae85.pdf) |
| N4-S57 | [CTR Martinique Procédures tables corrigées](../sources/n4/ctr-martinique-procedures-tables-corrigees.pdf) | 5 | Non identifiée dans les pages de repérage | [Source](https://www.ctrmartinique.com/_files/ugd/bef5df_f34e4223041a4eb0b2c06b860a4fc8b3.pdf) |
| N4-S58 | [Matelotage et plongée Gilles Foubert](../sources/n4/matelotage-et-plongee-gilles-foubert.pdf) | 44 | Édition interne non identifiée ; article de mise à disposition juin 2005 | [Source](https://www.ffessm-opm.fr/la-federation/espace-culturel/publications/item/download/1164_3b8a08f328782f2f47581dc6e3fc3833) |
| N4-S59 | [Appareil circulatoire janvier 2024 Arnaud Melese](../sources/n4/appareil-circulatoire-janvier-2024-arnaud-melese.pdf) | 34 | Janvier 2024 | [Source](https://plouf.melese.com/wp-content/uploads/L-appareil-circulatoire-v2024-1.pdf) |

## Liens indisponibles et recherche à compléter

Six téléchargements annoncés dans les index ont renvoyé une erreur 404 : anciennes
versions CoDep 92 « Accidents biochimiques », apnée, cadre réglementaire avril 2022,
système ventilatoire et quizz matériel, ainsi que le livret GP FSGT janvier 2025.
Leurs URL et erreurs figurent dans `failed_downloads` du manifeste. Ils ne sont pas
comptés parmi les PDF acquis. Les thèmes sont déjà documentés par d’autres cours du
corpus ; le livret FSGT reste une piste comparative facultative, distincte du cursus FFESSM.

Les pages CoDep 93 « Documents » et BFC « Sujets et annales » sont encore indexées
avec des listes de fichiers, mais leur corps ne restitue plus ces listes au navigateur
lors de cette recherche. Les PDF directement retrouvés et téléchargés sont inventoriés ;
la collection complète CoDep 93 2024–2025 et toutes les annales BFC ne sont pas acquises.

Pour les faits sensibles, le futur travail devra consulter le Code du sport consolidé,
les publications médicales actuelles, les notices des fabricants concernés et les textes
nautiques en vigueur. Les références ANFR, remontées anormales et désaturation déjà
acquises pour N3 sont à réutiliser après contrôle de version. Ce corpus n’est pas une
preuve d’exhaustivité du N4.

## Contrôles réalisés

- Vérification de 59 PDF lisibles, de leurs empreintes et de leur pagination par deux
  lecteurs indépendants (`pypdf` et `pdfinfo`) : 1 050 pages, 59 empreintes distinctes.
- Extraction locale paginée de chaque PDF ; repérage des couvertures, titres, sommaires,
  dates explicites et sections du référentiel actuel.
- Contrôle visuel de la couverture du MFT et d’une page de schémas du cours matériel.
- Aucune revue exhaustive des assertions, aucun audit de couverture des cartes,
  aucune création de carte, aucun import dans Anki pendant cette recherche.

## Compléments acquis pendant la rédaction

Le lot 02 ajoute deux références nationales actuelles : le corpus local compte
désormais **61 PDF, 1 101 pages**. Ces compléments servent à vérifier des conditions
d’accès ; ils n’étendent pas le deck à une préparation complète au N5 ou au MF1.

| Code | Document | Pages | Version | Référence |
| --- | --- | ---: | --- | --- |
| N4-S60 | [MFT N5](../sources/n4/ffessm-n5-mai-2026.pdf) | 8 | Mai 2026 | [FFESSM](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/8cf7d863-c58a-4ce1-ad2d-116bdbde6a1f) |
| N4-S61 | [MFT MF1](../sources/n4/ffessm-mf1-juillet-2026.pdf) | 43 | Juillet 2026 | [FFESSM](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/273c29e5-04c9-4a39-8f0a-d682255dccd8) |

## Références primaires actualisées à la clôture

- MFT Initiateur décembre 2025 : stage initial p.5 et examen p.18, [PDF officiel](https://api.ffessm.fr/V1/Commissions/ManuelFormationList/Download/c73522e4-acb2-4b56-9691-3a807334ab39).
- Règlement intérieur FFESSM du 7 décembre 2024, [PDF actuellement lié par la fédération](https://ffessm.fr/uploads/media/docs/0001/13/be9dd3c7e7d5695fa87946441349372266dac34f.pdf), art.V.2.4 commissions culturelles.
- [CRR ANFR juin 2025](https://www.anfr.fr/fileadmin/manuel-crr-maritime-25.pdf), p.20–23 ; appels ASN urgence/sécurité distingués de l’alerte de détresse.
- [Division240, arrêté du 21 mai 2026](https://www.mer.gouv.fr/sites/default/files/2026-06/division-240_arrete_du_21_05_26.pdf), repérée sur le site du ministère ; aucune ancienne longueur de mouillage ou valeur d’armement transformée en prescription actuelle.
- [DAN, OPI et résistance inspiratoire](https://dan.org/safety-prevention/diver-safety/divers-blog/can-you-recognize-ipe/) et [prévention OPI](https://world.dan.org/health-medicine/health-resource/dive-medical-reference-books/the-heart-diving/pulmonary-and-venous-disorders/), utilisés au lot105.

Consultation le 12 octobre 2026. Ces références web complémentaires ne sont pas
comptées comme fichiers acquis dans le manifeste des 61 PDF.
