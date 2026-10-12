# Lot N4 02 — fonctions et organisation fédérale

12 octobre 2026. Cinq créations QCM. Rédaction en `draft`, vérification factuelle,
puis seconde passe pédagogique par le même agent, avant correction et acceptation.
Pas de validation indépendante revendiquée. Aucun build, import ni commit.

## Vérification des sources

- Baptême : Code du sport A322-98, texte en vigueur depuis le 18 avril 2012,
  et annexe III-16a, consultés sur Légifrance le 12 octobre 2026.
- N5 : le résultat de recherche pointait vers le MFT de février 2019. Il est
  écarté comme référence de version ; le MFT **mai 2026** a été téléchargé depuis
  l’index national courant. p.3 : quinze plongées en situation de guide, acquisition
  des compétences en situation réelle, encadrant habilité E3 minimum.
- MF1 : MFT **juillet 2026** téléchargé depuis l’index national, p.4 et 6 : GP admis
  au stage initial classique, ni initiateur ni N5 obligatoire ; allègements distincts.
- Commissions : statuts 2023 actuellement liés par la commission juridique FFESSM,
  art.27 et 30, pages physiques 21–22. Organismes et conseil distingués.
- Examen GP : MFT **mai 2026**, p.9 : compétence CTR et délégation possible.

G01/G02 sont validés pour les affirmations de ces cartes, pas pour toutes les autres
questions juridiques du plan. Les deux PDF complémentaires restent privés dans
`sources/n4/`, avec extraction paginée et références publiques dans l’inventaire.

## n4-cadre-artificiel-bapteme-001

Apport : l’exception de baptême par un GP dépend de la profondeur maximale de
l’installation, pas seulement de la profondeur réellement atteinte. Complète
`n4-cadre-exploration-enseignement-001`, qui traite le milieu naturel.

- Fosse de 20 m, baptême à 5 m : confusion entre espace utilisé et profondeur
  de l’installation. A322-98 applique les règles du milieu naturel à la fosse >6 m.
- Mer sur fond de 6 m : confusion entre faible profondeur et milieu artificiel.
  Le baptême en milieu naturel exige E1 au minimum, même à 5 m.

Seconde lecture : même activité, même profondeur de baptême, autorisation du DP
dans les trois cas. La différence d’installation n’est pas explicitée comme critère
au recto. Les choix sont voisins en longueur ; la bonne réponse ne contient pas
une prudence ou une justification réservée à elle seule. Le corrigé distingue
les deux erreurs. **ISOLATION / CREDIBILITY / LENGTH / WHY / SENSE : acceptés.**

## n4-cadre-acces-dp-n5-001

Apport : exigences d’expérience et de validation pour obtenir N5, au-delà du rappel
de la fonction N5 dans `n3-prerogatives-fonctions-001`.

- Quinze plongées autonomes : confusion entre expérience de plongeur N3 et
  expérience de guidage ; le MFT exige quinze plongées en situation de guide.
- Validation E2 : confusion entre enseignant déjà habilité à former jusqu’à 20 m
  et encadrant habilité à valider le N5 ; ce dernier est au minimum E3.

Seconde lecture : le recto annonce exactement les deux conditions demandées,
les autres étant remplies. Les trois dossiers modifient une seule donnée à la fois,
avec même construction et longueur. Aucune expérience ne délivre automatiquement
le brevet : le corrigé explique l’évaluation continue. **Les cinq critères : acceptés.**

## n4-cadre-parcours-moniteur-001

Apport : entrée dans le cursus classique MF1 avec GP, sans imposer initiateur ou N5.
La carte E2 existante interroge la qualification obtenue après initiateur et sa
profondeur, pas ce prérequis d’accès. Aucun objectif équivalent dans N2/N3.

- Initiateur obligatoire : confusion entre filière classique et filière par
  capitalisation, ou entre qualification E2 et prérequis MF1 ; le GP suffit pour
  la filière classique, sous les autres conditions.
- N5 obligatoire : confusion entre diplôme de directeur et modules d’organisation
  du parcours MF1 ; le N5 donne un allègement, pas un prérequis.

Seconde lecture : candidat explicitement sans ces deux diplômes ; l’objectif est
son accès au stage initial, pas l’attribution immédiate d’E3. Bonne réponse concise,
choix de nature comparable. Le corrigé explique pourquoi des qualifications utiles
ne sont pas obligatoires. **Les cinq critères : acceptés.**

## n4-cadre-commissions-comite-001

Apport : pouvoir rendant exécutoires les propositions d’une commission technique.
Le rôle général de la fédération déjà traité en N2 n’interroge pas cette répartition.

- CTN : confusion entre expertise proposant le changement et décision exécutoire.
  Art.27 soumet les propositions au Comité directeur national.
- Conseil des commissions : confusion entre conseil transversal et instance de
  décision ; art.30 décrit une mission de réflexion et de proposition.

Seconde lecture : trois instances fédérales nationales, aucune réponse hors
institution ni déduction par géographie. Aucun contenu de réforme n’est inventé.
Les libellés officiels ont des longueurs naturelles voisines. Corrigé fondé sur
les rôles des trois instances. **Les cinq critères : acceptés.**

## n4-cadre-echelons-001

Apport : identifier l’échelon compétent pour organiser l’examen GP, dans un exemple
concret qui exige la connaissance de la répartition fédérale. Une simple question
« action départementale → comité départemental » a été écartée avant rédaction :
les noms auraient permis de répondre sans connaissance du cours.

- CTD : confusion entre organisateur pouvant recevoir délégation et autorité
  compétente ; le club doit demander à sa CTR, même si un Codep organise ensuite.
- CTN : confusion entre diplôme fédéral national et gestion habituelle de l’examen ;
  la CTN intervient notamment pour les structures non rattachées à une CTR.

Seconde lecture : club métropolitain dans le cadre habituel, donc aucune exception
territoriale ambiguë. Les trois choix sont des commissions techniques de niveaux
différents. Le corrigé distingue compétence et délégation ; sigles développés dans
les choix. **Les cinq critères : acceptés.**

## Verdict après seconde lecture

ACCEPT_ALL=yes, pour ces cinq IDs uniquement. Aucun leurre défendable dans le
contexte fourni, aucun nouvel objectif fusionné. Les cartes passent à `reviewed`
après cette passe factuelle et pédagogique. Le build reste réservé à la fin de N4.
