# Matrice d’architecture Base

| Couche | Responsabilité | Point à vérifier | Limite |
| --- | --- | --- | --- |
| Wallet et compte | Signature, session, délégation | Intention et paramètres signés | Interface manipulable |
| Paiement | Autorisation, sponsoring, règlement | Montant, token, destinataire | Service hors chaîne |
| L2 | Séquencement, dérivation, disponibilité | Inclusion et relecture | Finalité différée |
| Preuve | Attestation d’état ou de calcul | Relation réellement prouvée | Hypothèses du système |
| Retrait | Message, délai, finalisation | Nonce et destination | Reorg ou fault proof |

## Lecture

Une application Base traverse plusieurs couches. Une garantie observée à une couche ne doit pas être étendue automatiquement aux autres.
