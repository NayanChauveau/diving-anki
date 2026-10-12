# Lot N4 21_MATERIEL

12 octobre 2026. Rédaction en draft, contrôle factuel puis seconde lecture critique par le même agent. Pas de validation indépendante revendiquée. Aucun build, import ou commit.

## Références contrôlées

- N4-S01 — MFT GP-N4 mai 2026 p.28–29 ; N4-S11 Jourdren matériel p.5–6,24–31 ; fiche compresseur p.3 et robinet p.1–2 ; contrôlés 2026-10-12
- BAUER — extraits indexés notice Betreiberhandbuch, dépannage pression insuffisante/purges non étanches ; lien PDF ancien redirige ; catalogue accessoires 2025/2028 p.20 B-TIMER et suivi de cartouche : https://www.bauer-kompressoren.de/fileadmin/documents/products/spare-part-list/zubehoer_kataloge/High-pressure-accessories-catalogue_EN.pdf ; consultés 2026-10-12
- Schéma fonctionnel original docs/diagrams/n4/robinet-ouvert.svg ; exercice thermique gaz idéal, aucun seuil opérationnel de gonflage

## n4-materiel-compresseur-panne-001

Apport distinct : Diagnostic localisé et portée des observations ; pas panne devinée à partir d’un symptôme non spécifique.

Contrôle de chaque leurre :
- Un défaut d’ouverture du clapet d’admission : Peut réduire le débit mais ne constitue pas le défaut observé à la purge.
- Un défaut de tarage du pressostat : Concerne la commande d’arrêt, pas l’étanchéité de l’orifice observé.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-materiel-compresseur-verification-001

Apport distinct : Raisonner sur deux échéances et leur opérateur OU ; cas concret sans durée universelle inventée.

Contrôle de chaque leurre :
- L’échéance reste valable : il reste 12 heures de fonctionnement : Ignore l’échéance calendaire pourtant indépendante.
- L’échéance est dépassée seulement après 30 heures et 3 mois réunis : Remplace le premier terme atteint par l’obligation d’atteindre les deux.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-materiel-compresseur-temperature-calcul-001

Apport distinct : Transfert thermique avec kelvins et vérification de conservation ; différent des calculs isothermes existants.

Contrôle de chaque leurre :
- 110 bar : Utilise 22/42 au lieu du rapport des températures absolues.
- 224 bar : Inverse les températures et prévoit une hausse lors du refroidissement.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-materiel-robinet-schema-001

Apport distinct : Identifier les deux pièces et le passage ouvert ; fusion avec le candidat siège-clapet pour éviter un second nommage identique.

Contrôle de chaque leurre :
- A : clapet mobile ; B : siège fixe : Inverse la pièce mobile et la portée fixée au corps.
- A : joint de tige ; B : clapet mobile : Confond le siège traversé par le gaz avec le joint autour de la tige.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-materiel-robinet-etancheite-001

Apport distinct : Localisation fonctionnelle de fuite distincte du joint détendeur-bloc N2.

Contrôle de chaque leurre :
- Le joint d’étanchéité autour de la tige du volant : Une fuite à ce joint se manifesterait autour de la tige, exclue par l’observation.
- Le joint entre robinet et col du bloc : Une fuite à ce joint se manifesterait au col, pas uniquement par la sortie fermée.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

Seconde passe : le symptôme de montée lente seul serait insuffisant pour une panne unique ; la fuite localisée établit uniquement une purge non étanche, pas sa cause matérielle exacte. Journal : choix fondés sur OU versus compteur seul versus ET, dates imposées et non prescription fabricant. Résolution distincte thermique : 210/315 = 2/3 bar/K, multiplié par 295 = 196,666… ; contrôle direction baisse de température/baisse de pression. Schéma : porté du siège corrigé pour que le clapet le recouvre lors de sa descente (10 unités de recouvrement de chaque côté) ; aucune couleur indiquant les noms. Joint de tige distinct du contact siège-clapet. La fuite à la sortie ne désigne pas automatiquement un clapet usé : corrigé limité à la fonction de conservation. Ancienne fiche robinet : pas de couple 4/5 newton ni coups de maillet repris ; unités/procédure non fiables.

Fusion : `n4-materiel-siege-clapet-001` → `n4-materiel-robinet-schema-001` ; même identification fixe/mobile, aucune identité publiée retirée.
