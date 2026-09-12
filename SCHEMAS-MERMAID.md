# Schémas de lecture : Base, ZK et menaces

Ces schémas synthétisent les relations documentées dans les parcours associés. Ils servent de carte de lecture : ils ne remplacent ni le code source ni un audit.

## Base — parcours de la transaction à la finalité

	dgraph LR
	A[Wallet / dApp] --> B[Transaction L2]
	B --> C[Batcher et séquenceur]
	C --> D[Préimage de state]
	D --> E[Worker de dérivation]
	E --> F[Preuve ZK ou attestation TEE]
	F --> G[Challenge / vérification]
	G --> H[Finalisation vers Ethereum]

## ZK — du témoin à la preuve vérifiée

	dgraph LR
	I[Entrée publique] --> J[Témoin privé]
	J --> K[Circuit / contraintes]
	K --> L[Polynômes ou AIR]
	L --> M[Engagements]
	M --> N[Preuve]
	N --> O[Vérificateur]
	I --> O
	O --> P[Acceptation ou rejet]

## Menaces — défense en profondeur

	dgraph TD
	Q[Actifs : état, clés, preuves, données] --> R[Menaces]
	R --> R1[Entrée malformée]
	R --> R2[Rejeu / non-idempotence]
	R --> R3[Hypothèse de confiance excessive]
	R --> R4[Perte de provenance]
	R1 --> S[Validation et bornes]
	R2 --> T[Identifiants et reprise idempotente]
	R3 --> U[Modèle de confiance explicite]
	R4 --> V[Références, version et horodatage]

## Limites

Les liens entre concepts sont des relations pédagogiques. Les noms exacts de fonctions et les invariants doivent être confirmés dans la version de code citée par chaque parcours.
