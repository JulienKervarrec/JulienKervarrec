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

**Contribution proposée : [iden3/snarkjs #635](https://github.com/iden3/snarkjs/pull/635)** — correction de cinq commandes du tutoriel pour retrouver les bons fichiers d’entrée, le WASM et la clé FFLONK. PR ouverte le 10 septembre 2026 ; consulter le lien pour son statut actuel.

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

<details>
<summary>Explorer les autres parcours Base par domaine</summary>

### Wallets, identité et permissions

[paymaster](https://github.com/JulienKervarrec/paymaster/tree/main/docs/fr) · [webauthn-sol](https://github.com/JulienKervarrec/webauthn-sol/tree/main/docs/fr) · [eip-7702-proxy](https://github.com/JulienKervarrec/eip-7702-proxy/tree/main/docs/fr) · [account-policies](https://github.com/JulienKervarrec/account-policies/tree/main/docs/fr) · [sub-account-demo](https://github.com/JulienKervarrec/sub-account-demo/tree/master/docs/fr) · [base-account-privy](https://github.com/JulienKervarrec/base-account-privy/tree/main/docs/fr) · [base-verify-demo](https://github.com/JulienKervarrec/base-verify-demo/tree/master/docs/fr)

### Paiements et usages

[commerce-payments](https://github.com/JulienKervarrec/commerce-payments/tree/main/docs/fr) · [pos-dapp](https://github.com/JulienKervarrec/pos-dapp/tree/master/docs/fr)

### Infrastructure L2, ponts et données

[withdrawer](https://github.com/JulienKervarrec/withdrawer/tree/main/docs/fr) · [op-enclave](https://github.com/JulienKervarrec/op-enclave/tree/main/docs/fr) · [rollup-boost](https://github.com/JulienKervarrec/rollup-boost/tree/main/docs/fr) · [triedb](https://github.com/JulienKervarrec/triedb/tree/main/docs/fr) · [blob-archiver](https://github.com/JulienKervarrec/blob-archiver/tree/master/docs/fr) · [dispute-game-tool](https://github.com/JulienKervarrec/dispute-game-tool/tree/master/docs/fr) · [fault-proof-monitors](https://github.com/JulienKervarrec/fault-proof-monitors/tree/main/docs/fr) · [sol2base](https://github.com/JulienKervarrec/sol2base/tree/main/docs/fr)

### Primitives et outillage développeur

[base-std](https://github.com/JulienKervarrec/base-std/tree/main/docs/fr) · [based-ox](https://github.com/JulienKervarrec/based-ox/tree/main/docs/fr) · [ui](https://github.com/JulienKervarrec/ui/tree/main/docs/fr) · [skills](https://github.com/JulienKervarrec/skills/tree/master/docs/fr) · [base-flashblocks-demo](https://github.com/JulienKervarrec/base-flashblocks-demo/tree/master/docs/fr)

Ces liens présentent des lectures documentaires de l’écosystème Base, pas des projets dont je revendique la création ni une affiliation aux équipes amont.

</details>

## Focus 2026 — preuves et sûreté opérationnelle

- Pipeline Base : domaine public ZK, reprise idempotente des workers et modèle de confiance TEE.
- HyperEVM : arrondis bornés, instantanés de début de bloc et actifs toujours récupérables.
- Données Hyperliquid : manifeste de provenance, décimaux exacts et jointures sans biais d’anticipation.

## Ma démarche

Lire les sources, expliquer un mécanisme à la fois, citer les fichiers et rendre les limites explicites. Les parcours de mes forks sont distincts des correctifs proposés aux projets originaux. Je privilégie les contributions précises, faciles à relire et à vérifier.

Ces analyses reposent sur une lecture statique : aucun audit, benchmark ou résultat de test n’est revendiqué.

## Autres explorations

[DeFi et protocoles](https://github.com/JulienKervarrec?tab=repositories) · [Cairo](https://github.com/JulienKervarrec/cairo/tree/main/docs/fr) · IA et automatisation
