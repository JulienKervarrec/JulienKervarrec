## Documentation technique

- [Index des parcours](INDEX-PARCOURS.md) — navigation par thème et mécanisme.
- [Matrice d’architecture Base](MATRICE-ARCHITECTURE-BASE.md) — composants, flux et responsabilités.
- [Guide d’évaluation des preuves](GUIDE-EVALUATION-PREUVES.md) — critères de solidité et limites.
- [Modèle de menaces opérationnel](MODELE-MENACES-OPERATIONNEL.md) — actifs, surfaces d’attaque et contrôles.
- [Guide de reproductibilité](GUIDE-REPRODUCTIBILITE.md) — provenance, hypothèses et reprise des analyses.
- [Glossaire blockchain français](GLOSSAIRE-BLOCKCHAIN-FR.md) — vocabulaire partagé.
- [Références et lectures](REFERENCES-ET-LECTURES.md) — sources organisées pour approfondir.

## Parcours français

Travaux récents : [AirScript / STARK](https://github.com/JulienKervarrec/air-script/tree/next/docs/fr), [engagements polynomiaux / SNARK](https://github.com/JulienKervarrec/poly-commit/tree/master/docs/fr), [Microsoft SEAL / FHE](https://github.com/JulienKervarrec/SEAL/tree/main/docs/fr), [architecture Base](https://github.com/JulienKervarrec/base/tree/main/docs/fr) et [données Hyperliquid](https://github.com/JulienKervarrec/historical_data/tree/master/docs/fr).

Chaque parcours est fondé sur une lecture des sources, documente les hypothèses et limites de sécurité, et renvoie vers les mécanismes vérifiables du dépôt.

# Julien Kervarrec

### Comprendre les protocoles. Documenter les mécanismes. Contribuer à l’open source.

J’explore la blockchain, les systèmes de preuve, l’IA et l’automatisation. Je construis une bibliothèque technique francophone : des parcours courts dans les dépôts, reliés aux fichiers source et centrés sur les décisions de conception.

## ZK : STARK, SNARK et rollups

- **[ZK Research](https://github.com/JulienKervarrec/zk-research)** — point d’entrée, comparaison des mécanismes et journal de contribution.
- **[Winterfell / STARK](https://github.com/JulienKervarrec/winterfell/tree/main/docs/fr)** — trace Fibonacci, contraintes AIR, engagements, FRI et limites du vérificateur.
- **[snarkjs / SNARK](https://github.com/JulienKervarrec/snarkjs/tree/master/docs/fr)** — circuit, témoin, paramètres, Groth16, PLONK, FFLONK et export EVM.

## Hyperliquid / HyperEVM

- **[hyper-evm-lib](https://github.com/JulienKervarrec/hyper-evm-lib/tree/main/docs/fr)** — dix chapitres sur CoreWriter, précompiles, identité, visibilité inter-blocs, précision et ponts bidirectionnels.
- **[historical_data](https://github.com/JulienKervarrec/historical_data/tree/master/docs/fr)** — huit chapitres sur provenance, unités, déduplication, couverture et biais temporel.
- **Valeur pratique** — distinction explicite entre action EVM émise, traitement HyperCore, état observé et finalité.

## Base : du wallet à l’infrastructure L2

| Pour commencer | Ce que le parcours explique |
| --- | --- |
| [base](https://github.com/JulienKervarrec/base/tree/main/docs/fr) | Pipeline de preuve : préimages, workers, ZK, TEE et challenge |
| [base-std](https://github.com/JulienKervarrec/base-std/tree/main/docs/fr) | Précompiles B20, factory, rôles et registres de politiques |
| [account-sdk](https://github.com/JulienKervarrec/account-sdk/tree/master/docs/fr) | Provider Base Account, communication, sous-comptes et paiements |
| [commerce-payments](https://github.com/JulienKervarrec/commerce-payments/tree/main/docs/fr) | Autorisation, capture, remboursements et collecte par signature |
| [withdrawer](https://github.com/JulienKervarrec/withdrawer/tree/main/docs/fr) | Preuve et finalisation des retraits L2 vers Ethereum |

## Focus 2026 — preuves et sûreté opérationnelle

- Pipeline Base : domaine public ZK, reprise idempotente des workers et modèle de confiance TEE.
- HyperEVM : arrondis bornés, instantanés de début de bloc et actifs toujours récupérables.
- Données Hyperliquid : manifeste de provenance, décimaux exacts et jointures sans biais d’anticipation.

## Ma démarche

Lire les sources, expliquer un mécanisme à la fois, citer les fichiers et rendre les limites explicites. Les parcours de mes forks sont distincts des correctifs proposés aux projets originaux. Je privilégie les contributions précises, faciles à relire et à vérifier. Ces analyses reposent sur une lecture statique : aucun audit, benchmark ou résultat de test n’est revendiqué.

## Autres explorations

[DeFi et protocoles](https://github.com/JulienKervarrec) · [Cairo](https://github.com/JulienKervarrec) · IA et automatisation
