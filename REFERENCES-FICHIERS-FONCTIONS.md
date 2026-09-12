# Références précises : fichiers, mécanismes et fonctions

Cette fiche relie les conclusions du profil aux documents qui les portent. Les chemins ci-dessous sont ceux de ce dépôt ; lorsqu’une fonction de l’implémentation amont n’est pas confirmée dans la version consultée, elle est volontairement indiquée comme « à confirmer ».

## Carte de traçabilité

| Sujet | Référence de ce dépôt | Élément technique à vérifier dans la source |
| --- | --- | --- |
| Architecture générale Base | [MATRICE-ARCHITECTURE-BASE.md](MATRICE-ARCHITECTURE-BASE.md) | dérivation d’état, workers, preuve et finalisation — fonctions exactes à confirmer dans la version amont |
| Évaluation d’une preuve | [GUIDE-EVALUATION-PREUVES.md](GUIDE-EVALUATION-PREUVES.md) | génération, vérification, disponibilité des données et hypothèses de confiance |
| Menaces opérationnelles | [MODELE-MENACES-OPERATIONNEL.md](MODELE-MENACES-OPERATIONNEL.md) | validation d’entrée, déduplication, reprise idempotente et frontières de confiance |
| Reproductibilité | [GUIDE-REPRODUCTIBILITE.md](GUIDE-REPRODUCTIBILITE.md) | version du dépôt, commit source, paramètres, horodatage et provenance |
| Vocabulaire partagé | [GLOSSAIRE-BLOCKCHAIN-FR.md](GLOSSAIRE-BLOCKCHAIN-FR.md) | correspondance entre terme métier, structure de données et invariant |
| Parcours et couverture | [INDEX-PARCOURS.md](INDEX-PARCOURS.md) | périmètre couvert, documents associés et lacunes restantes |

## Méthode pour citer une fonction

Une référence de fonction utile doit toujours comporter : dépôt, branche ou tag, chemin du fichier, symbole exact et rôle observé. Exemple de forme :

projet@branche : chemin/vers/fichier.ext — NomDeLaFonction(...) : responsabilité observée et invariant associé.

Le nom ne doit pas être déduit d’un résumé ou d’un schéma. Il doit être relevé dans la version de code citée, car les renommages et déplacements de fonctions changent la valeur d’une référence.

## Contrôle de qualité

Avant de publier une référence de fonction, vérifier :

- le chemin existe dans la branche ou le tag indiqué ;
- le symbole apparaît réellement dans le fichier ;
- le lien pointe vers la version étudiée ;
- la description distingue le comportement observé de l’interprétation ;
- les limites et hypothèses sont écrites à côté de la référence.

Cette fiche complète les schémas Mermaid : elle ne revendique ni audit, ni benchmark, ni résultat d’exécution. Elle fournit une base de traçabilité honnête pour enrichir ultérieurement les parcours avec des liens source au niveau symbole.
