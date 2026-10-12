# Lot N4 09_DESATURATION

12 octobre 2026. Rédaction en draft, contrôle factuel puis seconde lecture critique par le même agent. Pas de validation indépendante revendiquée. Aucun build, import ou commit.

## Références contrôlées

- N4-S01 — MFT GP-N4 mai 2026 p.25 : absence de certification des logiciels, dissolution et procédures différentes ; vérifié le 2026-10-12
- N4-S07 — Jourdren, Pressions partielles et dissolution p.10–13 : cinétique par périodes ; modèles mathématiques fictifs, pas tables opérationnelles
- AFNOR — NF EN 13319 juin 2000, fiche officielle en vigueur et résumé du champ temps/profondeur : https://www.boutique.afnor.org/en-gb/standard/nf-en-13319/diving-accessories-depth-gauges-and-combined-depth-and-time-measuring-devic/fa048402/17312 ; consulté 2026-10-12
- Suunto Zoop Novo, notice officielle rubrique Decompression dives (ceiling) ; Shearwater Peregrine français RevB 2020 p.15–16,25 (palier nominal) ; affichages fictifs distincts ; références déjà acquises N2/N3

## n4-desaturation-certification-logiciel-001

Apport distinct : Portée exacte d’une norme, distincte du simple caractère théorique d’un modèle.

Contrôle de chaque leurre :
- Le calcul des tensions des compartiments et des paliers : Confusion entre la certification des mesures de l’appareil et celle de ses calculs physiologiques.
- Le choix des Gradient Factors et des vitesses de remontée : Confusion entre paramètres de désaturation et exigences métrologiques de temps/profondeur.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-desaturation-charge-deux-phases-001

Apport distinct : Transmettre l’état final de la première phase à la seconde, dont l’équilibre change.

Contrôle de chaque leurre :
- 3,0 bar : Réinitialise la tension avant la seconde phase au lieu de conserver la charge acquise.
- 4,0 bar : Remplace le profil à deux équilibres par deux périodes au même équilibre.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-desaturation-decharge-transition-001

Apport distinct : Enchaîner une charge sur deux périodes puis une décharge à un nouvel équilibre.

Contrôle de chaque leurre :
- 1,6 bar : Applique une division de la tension absolue au lieu de réduire l’écart à l’équilibre.
- 3,2 bar : Conserve le résultat de charge en oubliant la troisième période.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## Corrections après critique
Certification : supprimé « sans valider médicalement… » du recto, qui orientait vers la métrologie. Les trois choix désignent désormais trois familles de fonctions d'un ordinateur ; le corrigé donne la portée de la conformité. AFNOR confirme le champ temps/profondeur, le MFT confirme que cela ne certifie pas le logiciel de désaturation ; aucune lecture intégrale de la norme payante n'est revendiquée.
Calcul 1 : récurrence indépendante Tsuiv=(T+E)/2, états successifs 1 → 2 → 3,5 bar. Tension finale 3,5 ; les leurres 3 et 4 correspondent à deux erreurs de profil distinctes. Contrôle dimensionnel : toutes les données sont des tensions du même gaz en bar, pas une profondeur.
Calcul 2 : état après fond 3,2 ; réduction de l'écart de 2,4 à 1,2 ; résultat 2. La réponse 1,6 peut provenir aussi d'un fond d'une seule période suivi de la décharge : toujours fausse dans le profil donné, pas de seconde clé. Les équilibres donnés évitent une confusion entre Pabs et pression d'azote inspirée.

## Rejet de la quatrième création et deux reprises
n4-desaturation-contraintes-trois-001 : REWRITE puis FUSION. Un palier « nominal » à 6 m ne définit pas à lui seul sa zone de crédit ni le plafond du modèle ; déclarer 5,4 m faux sans ces données serait abusif. Spécifier un plafond à 6 m ramènerait le problème à l'intersection déjà testée dans n2-ordinateurs-plafonds-differents-001. Conserver cette carte et n3-ordinateur-paliers-communs-001, rectos, choix et corrigés relus : moyenne de profondeurs, adoption du plafond du voisin, fin du plus court palier, moyenne de durées sont quatre confusions bien distinctes. Leurs conditions et modèle Basic historique sont conservés. Cinq identités traitées dans le lot.
