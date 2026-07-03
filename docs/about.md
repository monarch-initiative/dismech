# About DisMech

**DisMech** (the **Dis**order **Mech**anisms Knowledge Base) is a structured,
evidence-backed knowledge base of disease pathophysiology. It records *how*
diseases work — the cell types, biological processes, and causal chains that
link a genetic or environmental cause to its clinical phenotypes — and ties every
claim to a citable reference.

## What's in it

- **Disorder entries** (`kb/disorders/`) — one structured YAML file per disease, each capturing pathophysiology, phenotypes, genetics, treatments, evidence, and ontology term bindings.
- **Mechanism modules** (`kb/modules/`) — conserved pathological processes (e.g. the fibrotic response) that recur across many diseases; disorders declare conformance to them. See the [Modules & Conformance primer](primers/modules-and-conformance.md).
- **Disease groupings** (`kb/groupings/`) — curated unions of related disease entries.
- **A LinkML schema** (`src/dismech/schema/dismech.yaml`) — the formal data model that every entry validates against. Browse it via the [Data Model overview](data-model.md) and the [Schema Reference](schema/schemas/dismech.md).

## Design principles

- **Mechanism-first.** Entries model the causal pathophysiology graph, not just a flat list of symptoms.
- **Evidence required.** Every claim carries a PMID/DOI/structured reference with an exact quoted snippet, validated against the source.
- **Ontology-grounded.** Phenotypes, cell types, processes, anatomy, and treatments bind to standard ontologies (HPO, CL, GO, UBERON, MAXO, NCIT, …).

The reasoning behind the project's scope, schema choice, and evidence policy is
recorded in the [Design Decisions](explanation/design-decisions.md) register.

## Where things live

- **Main site:** [dismech.monarchinitiative.org](https://dismech.monarchinitiative.org/)
- **Disorder browser:** [/app](https://dismech.monarchinitiative.org/app/)
- **Source & issues:** [github.com/monarch-initiative/dismech](https://github.com/monarch-initiative/dismech)

DisMech is developed as part of the
[Monarch Initiative](https://monarchinitiative.org).
