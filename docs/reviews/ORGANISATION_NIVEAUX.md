# Organisation de la collection — 6 octobre 2026

Structure validée par l’utilisateur après un essai avec trois cartes :
`Plongée::Collection commune`, `Plongée::N2`, `Plongée::N3`.
Les catégories peuvent différer selon le niveau si un besoin pédagogique apparaît.
Actuellement, chacun présente les cinq catégories thématiques du catalogue.

Le build exporte les 426 notes uniques sous Collection commune. Les catégories
N2/N3 sont des paquets filtrés configurés dans Anki, avec le tag du niveau et la
catégorie d’origine, en sélectionnant les cartes dues ou nouvelles. Reprogrammation
active, création même si vide, limite de séance de 100 cartes. Les accès ne sont pas
exportés dans le `.apkg` ; leur configuration est décrite dans SHARED_COLLECTION.md.

La migration locale déplace les cartes existantes via AnkiConnect `changeDeck`,
sans recréer de note, de modèle ou de carte. Le catalogue inclut les 308 identités
N2 historiques. Les anciennes cartes retirées restent suspendues avec leur historique
et sont déplacées dans leur catégorie commune. Les anciennes branches ne sont
retirées qu’après constat qu’elles sont vides ; aucune carte n’est supprimée.
Une sauvegarde des cartes, notes et révisions avant migration est conservée localement
hors Git dans `/tmp/diving-n3/generalize-before.json`.

À la demande de l’utilisateur, aucun test de séance ou réponse dans Anki n’est effectué
après généralisation. La vérification de l’usage est laissée à l’utilisateur.
`make check` passe : catalogue de 426 cartes, 17 tests, contrôles de code et schéma.
`make push` construit le paquet commun et l’importe ; la synchronisation finale
transmet aussi les accès N2/N3 créés dans Anki.

Avant de passer de N2 à N3, vider les filtres N2 puis reconstruire les filtres N3.
Une carte commune garde sa progression mais ne peut pas occuper deux paquets filtrés
simultanément. Le compte affiché est celui de la séance chargée, pas le total du niveau.

## Décision finale — organisation précédente abandonnée

L’utilisateur demande que toute configuration soit reproductible depuis le dépôt,
interdit toute manipulation de l’interface Anki, et choisit N2 comme base avec N3
comme complément. Les sections précédentes décrivent seulement l’essai abandonné.
La structure finale contient des paquets classiques N2 (308 notes) et N3 (118 notes),
sans Collection commune. Les 204 cartes pertinentes pour N3 déjà dans N2 y restent.
Le build embarque les limites de config/study.json ; make push restaure les destinations
et les réglages via AnkiConnect. Aucun futur paquet filtré n’est créé ou configuré.

## Clôture technique — 7 octobre 2026

Le build contient 308 notes sous N2 et 118 sous N3, toutes dans des paquets
classiques. `make push` a restauré l’installation existante via AnkiConnect et
synchronisé avec AnkiWeb, sans nouvelle manipulation de l’interface.
Une comparaison des données avant/après a confirmé les mêmes IDs de note/carte,
modèles, échéances, intervalles, suspensions et révisions pour les 443 cartes
présentes (426 actives et 17 retirées). Aucun apprentissage n’a été réinitialisé.
Les contrôles passent : 18 tests de projet et 5 tests d’import Anki, dont le
préréglage de 10 nouvelles cartes embarqué et le maintien du préréglage Default.
La migration des filtres est limitée aux destinations du catalogue : les paquets
filtrés personnels ayant d’autres noms ne sont pas concernés.
