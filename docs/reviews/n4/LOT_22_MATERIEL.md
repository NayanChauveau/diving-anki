# Lot N4 22_MATERIEL

12 octobre 2026. Rédaction en draft, contrôle factuel puis seconde lecture critique par le même agent. Pas de validation indépendante revendiquée. Aucun build, import ou commit.

## Références contrôlées

- N4-S01 — MFT GP-N4 mai 2026 p.28–29 ; fiches CODEP92 : premier étage piston simple p.1–2, piston compensé p.1–2 ; Jourdren matériel p.10–13 ; relus 2026-10-12
- SCUBAPRO — notice détendeurs juillet 2025, sources/n3/scubapro-detendeurs-juillet-2025.pdf, §5.1 premiers étages ; contrôle de pertinence des montages, pas performance universelle
- Modèles fonctionnels explicitement imposés : chambres et forces ; aucune équation numérique de forces exigée au MFT ; reprise après critique des formulations anciennes « au repos ouvert » et MP constante pour tous les détendeurs

## n4-materiel-robinet-volume-piege-001

Apport distinct : Séparer interruption du chemin d’alimentation et volume de gaz piégé dans un double robinet.

Contrôle de chaque leurre :
- Le circuit du détendeur B seulement : Confond fermeture de A avec évacuation du gaz situé en aval.
- Le circuit du détendeur A seulement : Ignore que B reste relié à la bouteille commune.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-materiel-amont-aval-001

Apport distinct : Déduire force et qualification d’une géométrie, au lieu de réciter une marque.

Contrôle de chaque leurre :
- Elle tend à l’ouvrir : montage aval : Inverse l’effet de la pression sur la face amont.
- Elle tend à le fermer : montage aval : Déduit correctement la fermeture mais emploie la qualification inverse.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-materiel-piston-simple-forces-001

Apport distinct : Analyse du piston après variation de MP ; analogue au cycle N2 mais organe mobile et bilan explicités.

Contrôle de chaque leurre :
- Le piston se rapproche du siège et coupe l’entrée de gaz haute pression : Une baisse de la force fermante favorise l’ouverture, pas la fermeture.
- Le piston reste au siège jusqu’à une variation de la pression ambiante : La demande respiratoire modifie la MP même à profondeur constante.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-materiel-piston-simple-hp-001

Apport distinct : Effet d’une variation de HP sur l’équilibre, distinct du cycle provoqué par la demande.

Contrôle de chaque leurre :
- Elle augmente : Une hausse de MP renforcerait la force fermante, alors que la force ouvrante a diminué.
- Elle reste indépendante de la HP : Suppose une compensation absente dans le montage donné.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-materiel-piston-equilibre-schema-001

Apport distinct : Interpréter la neutralisation des forces HP, et non la seule promesse de confort d’un détendeur compensé.

Contrôle de chaque leurre :
- Deux surfaces efficaces égales de l’ensemble mobile, soumises à des forces de même sens : Additionne deux forces de même sens au lieu de les neutraliser.
- Deux surfaces efficaces égales, l’une mobile et l’autre sur le corps fixe, soumises à des forces opposées : Réalise un bilan de tout le corps du détendeur alors que l’équilibre à contrôler est celui de la pièce mobile.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

Seconde passe : compensation réécrite entièrement ; les leurres initiaux confondaient grossièrement HP et ambiante/MP. La version finale compare des dispositions mécaniques de même nature : direction et appartenance au même ensemble mobile. Pas de coupe inventant un produit ; le modèle en mots définit précisément les surfaces efficaces. Piston simple : le sens de HP est imposé, car dépend du montage. Sens de MP vérifié indépendamment par bilan : perte de force fermante → ouverture, perte de force ouvrante HP → MP de fermeture moindre. Amont : pression amont pousse vers le siège du côté aval, tandis que le déplacement d’ouverture est vers la chambre HP ; ces directions sont cohérentes. Volume piégé : les deux circuits sont initialement pressurisés, l’absence de purge est explicite ; aucune consigne de fermeture en plongée déduite. Les schémas de circuit physique seront interrogés au lot suivant plutôt que donner un faux éclaté constructeur.
