# Regroupement des decks N2

6 octobre 2026. Organisation approuvée : cinq catégories directement sous `Plongée::N2` :
Réglementation, Physique, Prévention des accidents, Désaturation, Matériel et préparation.
Les fichiers restent séparés par chapitre et les tags sont conservés. Le plan et l’audit
reflètent ces destinations ; les catégories futures apparaîtront avec leurs premières cartes.

Les 53 cartes publiées ont maintenant `deck: Réglementation`. Comparaison des YAML avec
Git : seul ce champ change, les IDs, contenus, sources et tags sont identiques.

Migration Anki effectuée avec `changeDeck`, avant import du nouveau package. Les trois
anciens sous-decks ont été supprimés après vérification qu’ils étaient vides. La collection
contenait 60 cartes dans ce périmètre : 53 actuelles et 7 anciennes conservées. Toutes ont été
déplacées, sans modifier leurs états (dont 5 cartes suspendues). Les quatre decks utilisaient
le même préréglage Anki, ID 1.

Comparaison avant déplacement, après déplacement et après `make push` : mêmes IDs de cartes
et de notes, échéances, intervalles, facteurs de facilité, files et types, nombres de révisions
et d’oublis, étapes restantes, drapeaux et historique complet (132 entrées). Le marqueur de
synchronisation `usn` des entrées d’historique est exclu de la comparaison après synchronisation.

`make check` : 53 cartes valides, 13 tests réussis. `make push` : package de 53 notes importé
et synchronisation AnkiWeb réussie. Aucun changement de contenu pédagogique.
