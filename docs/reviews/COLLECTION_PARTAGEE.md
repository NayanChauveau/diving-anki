# Passage au paquet unique N2/N3/N4

6 octobre 2026. Demande : une note et un historique pour une connaissance commune aux
niveaux, avec un seul paquet publié. Aucune modification du contenu pédagogique.

## Changements

- `diving-fr.apkg` est le seul export du build et de la CI ; `make build-all` reste un alias.
  Les anciens fichiers générés N2/N3/N4 sont retirés du dossier de sortie après réussite.
  La CI retirera ces trois anciens assets de la release mobile après publication du paquet unique.
- GUID unique par ID YAML, utilisant le sel historique fixe N2. Les 308 GUIDs publiés N2
  restent identiques. L’identité ne dépend pas du contenu ni de l’ordre des niveaux.
- Catégories communes sous `Plongée`, tous les tags `level::...` de la carte dans l’export.
- Les modèles, champs, templates et contenus des cartes restent identiques.
- La sélection d’étude par niveau se fait avec les tags dans Anki. Les appartenances N3/N4
  seront attribuées après leur revue ; elles ne sont pas ajoutées automatiquement au N2.

## Vérification

- `make check` : 16 tests réussis ; le module d’intégration Anki est facultatif dans
  l’environnement standard et vérifié séparément, obligatoirement dans la CI.
- `uv run --with anki python -m pytest tests/test_anki_import.py` : deux tests d’import réels
  réussis, dans des collections temporaires (installation N2 historique et installation
  directement via une carte pertinente N4). Les imports répétés ajoutent seulement la
  nouvelle note propre à N4 ; notes communes, IDs de cartes, échéances, intervalles,
  révisions, oublis, facilité, suspension, drapeaux et entrées revlog restent identiques.
- Contrat de niveaux testé : appartenance à N2/N3/N4, retrait d’une appartenance N2 sans
  changement de GUID, export complet sans doublon, exclusion des brouillons.
- `make build` : un seul paquet, 308 notes, tous les champs attendus remplis ; ensemble
  des GUIDs identique à la formule N2 publiée ; cinq catégories communes.
- Le nettoyage des exports générés laisse intact un package personnel d’un autre nom.
- Les YAML de cartes ont été comparés par empreinte à la préparation précédente : inchangés.

## Installation existante

Ces tests n’ont pas modifié la collection personnelle ni synchronisé AnkiWeb.
L’import conserve les notes communes mais ne garantit pas leur déplacement de deck.
Le [guide de migration](../SHARED_COLLECTION.md#migrer-une-installation-n2-existante)
explique le regroupement des anciennes catégories avec conservation des révisions et
suspensions. Les anciennes revues décrivant `Plongée::N2` restent des bilans historiques.
