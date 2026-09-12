# Mini-prototype : mesurer des critères de commits

Ce prototype fournit une hypothèse contrôlable pour analyser pourquoi un historique GitHub peut être partiellement reconnu par un service externe comme Guild. Il ne prétend pas connaître le code de Guild.

## Domaines couverts

Les fixtures de test couvrent quatre axes du profil : Base, Hyperliquid, systèmes ZK et FHE. Le domaine est une étiquette d’analyse ; la décision commune porte sur la visibilité, l’auteur, la branche et les fichiers réellement modifiés.

## Exécution reproductible

Depuis ce dossier, avec Python 3.10 ou supérieur :

    python -m unittest -v test_commit_classifier.py

Aucune dépendance externe n’est requise. Les tests utilisent uniquement la bibliothèque standard et ne modifient ni GitHub ni le dépôt.

## Format d’un commit d’entrée

    {
      "sha": "abc123",
      "author": "JulienKervarrec",
      "visibility": "public",
      "branch": "main",
      "files": ["docs/base.md"],
      "domain": "Base",
      "is_merge": false
    }

## Interprétation

Un commit accepté par ce modèle satisfait tous les critères déclarés. Un commit rejeté expose ses raisons, ce qui permet de comparer méthodiquement les résultats avec le compteur Guild après une vérification manuelle. Une divergence constitue une information expérimentale : elle indique qu’un critère, une fenêtre temporelle ou un cache externe doit être étudié.

## Limites et suite

Le prototype ne récupère pas automatiquement l’API GitHub, ne déduit pas l’identité d’un auteur à partir d’une adresse e-mail et ne reproduit pas les règles privées de Guild. Une prochaine évolution utile serait un export JSON contrôlé de commits déjà observés, avec conservation du SHA, de la branche et des fichiers modifiés.
