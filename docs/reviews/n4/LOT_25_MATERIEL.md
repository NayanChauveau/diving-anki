# Lot N4 25_MATERIEL

12 octobre 2026. Rédaction en draft, contrôle factuel puis seconde lecture critique par le même agent. Pas de validation indépendante revendiquée. Aucun build, import ou commit.

## Références contrôlées

- N4-S01 — MFT GP-N4 mai 2026 p.28–29 ; CODEP92 givrage p.1–2 et manomètre p.1 ; Jourdren matériel p.16–20 ; relus 2026-10-12
- SCUBAPRO RevQ juillet 2025 p.8 et 15–16, XTIS/chambre sèche et débit en eau froide ; fichier sources/n3/scubapro-detendeurs-juillet-2025.pdf
- Mares — Natural Breathing : https://www.mares.com/natural-breathing ; technologie VAD et trajet bypass/vortex, consulté 2026-10-12
- WIKA fabricant — Bourdon tube pressure gauge functional principle : https://blog.wika.com/en/knowhow/bourdon-tube-pressure-gauge-functional-principle/ ; déformation élastique et transmission mécanique, consulté 2026-10-12

## n4-materiel-vortex-001

Apport distinct : Mécanisme VAD nommé au référentiel, distinct de l’équilibrage MP et de la molette.

Contrôle de chaque leurre :
- Un mouvement tourbillonnant crée une surpression repoussant la membrane vers l’extérieur : Inverse le signe de la pression locale et la direction de l’action sur la membrane.
- Un mouvement tourbillonnant augmente la MP fournie par le premier étage : Attribue au système du second étage un changement du réglage de pression du premier.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-materiel-givrage-interne-externe-001

Apport distinct : Deux sources d’eau et deux circuits, pas une confiance absolue dans un type de détendeur.

Contrôle de chaque leurre :
- Glace issue de l’eau environnante ; glace issue de l’humidité du gaz : Inverse les sources d’eau entre circuit de gaz et chambre exposée.
- Dans les deux cas, glace issue seulement de l’humidité du gaz : Ignore l’eau ambiante présente dans la chambre du ressort décrite.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-materiel-givrage-debit-001

Apport distinct : Cumul de débits et bilan thermique du premier étage ; distinct de la seule certification froid.

Contrôle de chaque leurre :
- Le débit du premier étage reste celui de la respiration, car l’inflateur prend le gaz après la détente : Ignore que toute alimentation MP de l’inflateur provient elle aussi du débit détendu au premier étage.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

## n4-materiel-manometre-bourdon-001

Apport distinct : Principe physique de l’instrument, distinct d’une simple lecture du cadran.

Contrôle de chaque leurre :
- Le tube tend à s’enrouler davantage et son extrémité entraîne l’aiguille : Inverse la déformation du tube : la hausse de pression augmente le rayon de courbure au lieu de resserrer la courbe.

Seconde lecture : ISOLATION — situation et tâche autonomes ; CREDIBILITY — confusions précisées ci-dessus ; LENGTH — mêmes objets comparés, clé non surdéveloppée ; WHY — distinction expliquée dans le corrigé ; SENSE — recto, chaque choix et corrigé relus en français. Aucun second choix valide retenu dans les hypothèses du recto. **ACCEPT après cette lecture.**

Seconde passe : les leurres débit (augmentation d’ambiante/humidité) étaient trop éliminables ; remplacés par la confusion entre débit prélevé en MP et débit déjà compris dans celui de la respiration. Bourdon : retrait du boîtier rempli d’eau, trop grossier ; paire finale compare redressement et resserrement, tous deux avec transmission mécanique. Vortex : technologie Mares explicitée, pas d’allégation comparative commerciale de confort ni absence garantie de givrage. Gel : eau du circuit versus eau extérieure, membrane de commande et isolation environnementale ne sont pas confondues. Ancienne fiche givrage : aucune température universelle −30/−80°C, pas d’alternance systématique entre détendeurs, pas de pincement de flexible, pas de StopFlow ajouté. Notice SCUBAPRO confirme débit cumulé et froid ; aucune consigne de démontage.

Cinquième identité : `n2-detendeurs-eau-froide-001` relue intégralement, N4 ajouté sans modification de modèle/ID/contenu. Ensemble versus seul premier/second étage : deux leurres plausibles et faux pour le contrôle de certification. Candidat `n4-materiel-givrage-configuration-001` fusionné ; exercice chiffré de limite de température déjà assuré aussi par `n3-materiel-partage-profondeur-001`, repris au lot 04.
