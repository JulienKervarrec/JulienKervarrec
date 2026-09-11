# Méthodologie de recherche

Ce dépôt présente des parcours techniques francophones sur les systèmes de preuve, la confidentialité et l’infrastructure blockchain. L’objectif est de relier chaque explication à des éléments vérifiables du code et de rendre les limites visibles.

## 1. Définir le périmètre

Identifier le dépôt, la branche ou le commit étudié, puis préciser les composants couverts et ceux qui ne le sont pas.

## 2. Partir des sources

Privilégier les fichiers source, les spécifications et la documentation officielle. Pour chaque affirmation importante, conserver le chemin, le symbole, la constante ou l’invariant qui sert de preuve. Distinguer ce qui est observé de ce qui est interprété.

## 3. Décrire les frontières de confiance

Préciser qui peut appeler chaque composant, quelles données sont contrôlées par un adversaire, quelles dépendances sont externes et où interviennent les opérateurs, bridges, workers ou services RPC.

## 4. Suivre les invariants

Analyser les autorisations, les transitions d’état, le flux de valeur, la fraîcheur, la protection contre le rejeu et les chemins d’échec. Pour ZK, suivre la relation entre trace, contraintes, transcript et vérification. Pour FHE, relever les paramètres, le bruit et les limites opérationnelles. Pour Base et HyperEVM, distinguer l’action émise, le traitement, l’état observé et la finalité.

## 5. Documenter les limites

Signaler les chemins non vérifiés, la sensibilité aux versions, les hypothèses et les questions ouvertes. Un parcours documentaire ne constitue ni un audit, ni un benchmark, ni une garantie de sécurité.

## Résultat attendu

Chaque parcours doit laisser une piste de lecture claire : sources consultées, mécanisme expliqué, hypothèses explicites et limites utiles pour une revue plus approfondie.
