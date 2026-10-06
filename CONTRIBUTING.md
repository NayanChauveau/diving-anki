# Contribution

Avant de rédiger ou modifier le contenu, lire [AGENTS.md](AGENTS.md),
[CONTENT_GUIDELINES.md](CONTENT_GUIDELINES.md) et [le guide de conception](docs/CARD_DESIGN.md).

Installer avec `uv sync --extra dev`. Exécuter `make check` après les changements :
lint, formatage, types, schéma JSON, validation des cartes et tests.
Après modification du modèle Pydantic, exécuter `make schema`.

Les cartes sont en français, une collection `cards:` par fichier de chapitre.
Une connaissance partagée conserve le même ID et indique `levels: [N2, N3, N4]`
selon sa pertinence vérifiée. Le paquet unique utilise la même identité de note Anki,
les mêmes catégories sous `Plongée` et les tags de tous ses niveaux.
`make build` génère `diving-fr.apkg`, contenant tous les niveaux ; `make build-all` est un alias.
Les types pris en charge sont `mcq`, `basic` et `cloze`.
Exemple de structure (contenu fictif, à adapter aux documents) :

```yaml
cards:
  - id: n2-exemple-001
    type: mcq
    deck: Exemple
    levels: [N2]
    status: draft
    review:
      sources: ["document-source, section à préciser"]
    fr:
      question: Question à rédiger depuis la source
      choices:
        - text: Réponse correcte à vérifier
          correct: true
        - text: Confusion plausible à vérifier
          correct: false
      explanation: Explication à rédiger et vérifier
```

Un QCM exige `fr.question`, `fr.choices` (2 à 10 choix, exactement un `correct: true`)
et `fr.explanation`. Une cloze exige `fr.text` avec `{{c1::…}}` et peut avoir `fr.extra`.
`tags` et `source_id` sont facultatifs. Les champs inconnus sont rejetés.

Les cartes nouvelles sont `draft` par défaut et exclues des builds ordinaires.
Après vérification factuelle et pédagogique, passer à `reviewed`.
Ne jamais renommer ni réutiliser un ID publié, ni changer les IDs des modèles.
Ne pas committer les documents privés ou les packages générés.
La CI contrôle le projet et construit le paquet unique ; les pushes sur main
mettent à jour la release latest-main, les tags v* créent une release versionnée.

Choisir le QCM dès qu’il convient à la question, y compris calculs et schémas.
Un autre format reste possible s’il est plus pertinent ; justifier ce gain carte par carte.
Pour convertir une Basic publiée en QCM, conserver son ID et ajouter `anki_model: basic`.
Le générateur exporte les choix interactifs dans ses deux champs existants ; aucune
conversion manuelle de type de note ni nouvelle note n’est nécessaire dans Anki.
Ne jamais retirer ce marqueur lors d’une réécriture ultérieure.
