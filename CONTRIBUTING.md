# Contribution

Avant de rédiger ou modifier le contenu, lire [AGENTS.md](AGENTS.md),
[CONTENT_GUIDELINES.md](CONTENT_GUIDELINES.md), [le guide de conception](docs/CARD_DESIGN.md)
et [la grille de qualité](docs/STUDY_CARD_QUALITY.md).

Installer avec `uv sync --extra dev`. Exécuter `make check` après les changements :
lint, formatage, types, schéma JSON, validation des cartes et tests.
Après modification du modèle Pydantic, exécuter `make schema`.

Les cartes sont en français, une collection `cards:` par fichier de chapitre.
Une connaissance partagée conserve le même ID et indique `levels: [N2, N3, N4]`
selon sa pertinence vérifiée. Le paquet unique utilise la même identité de note Anki,
les catégories sous le premier niveau concerné (N2 avant N3 avant N4) et les tags de
tous ses niveaux. N2 est la base ; N3 et N4 sont des compléments, sans copie.
Tous les paquets sont classiques. Le préréglage quotidien vient de `config/study.json`
et est embarqué dans le `.apkg`. Ne jamais configurer Anki via son interface :
`make push` importe, déplace les cartes existantes et synchronise via AnkiConnect.
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
Faire une critique distincte de la rédaction avec les cinq critères de la grille,
sur toutes les cartes du lot (40 au plus), puis corriger et relire les IDs rejetés.
Consigner les verdicts et motifs par ID dans `docs/reviews/` ; une mention globale
« QCM relus » sans examen des leurres, de la forme et du corrigé ne suffit pas.
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
