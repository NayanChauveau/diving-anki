# Contribution

Avant de rédiger ou modifier le contenu, lire [AGENTS.md](AGENTS.md),
[CONTENT_GUIDELINES.md](CONTENT_GUIDELINES.md) et [le guide de conception](docs/CARD_DESIGN.md).

Installer avec `uv sync --extra dev`. Exécuter `make check` après les changements :
lint, formatage, types, schéma JSON, validation des cartes et tests.
Après modification du modèle Pydantic, exécuter `make schema`.

Les cartes sont en français, une collection `cards:` par fichier de chapitre.
Les types pris en charge sont `mcq`, `basic` et `cloze`.
Exemple de structure (contenu fictif, à adapter aux documents) :

```yaml
cards:
  - id: n2-exemple-001
    type: basic
    deck: Exemple
    levels: [N2]
    status: draft
    review:
      sources: ["document-source, section à préciser"]
    fr:
      front: Question à rédiger depuis la source
      back: Réponse à rédiger et vérifier
```

Un QCM exige `fr.question`, `fr.choices` (2 à 10 choix, exactement un `correct: true`)
et `fr.explanation`. Une cloze exige `fr.text` avec `{{c1::…}}` et peut avoir `fr.extra`.
`tags` et `source_id` sont facultatifs. Les champs inconnus sont rejetés.

Les cartes nouvelles sont `draft` par défaut et exclues des builds ordinaires.
Après vérification factuelle et pédagogique, passer à `reviewed`.
Ne jamais renommer ni réutiliser un ID publié, ni changer les IDs des modèles.
Ne pas committer les documents privés ou les packages générés.
La CI contrôle le projet et construit les trois packages ; les pushes sur main
mettent à jour la release latest-main, les tags v* créent une release versionnée.
