# DisMech Documentation

Welcome to the documentation for **DisMech**, the Disorder Mechanisms Knowledge
Base — a structured, evidence-backed knowledge base of disease pathophysiology.

This site covers the curation guides, the conceptual explanations, the data
model, and the auto-generated schema reference. For the live knowledge base
itself, head to the main site.

!!! warning "AI-curated resource — not medical advice"

    DisMech content is generated and maintained by AI curation agents under human review,
    from publicly accessible literature and curated biomedical knowledge resources. It is a
    research resource and is **not intended to inform medical diagnosis or treatment**.
    See the [full disclaimer](disclaimer.md).

## Start here

- **Brand new?** Read [Onboarding](onboarding.md) — how the system fits together, a step-by-step first curation (web and CLI), and what to try next.
- **New to the data model?** Read the [Data Model overview](data-model.md) — a curated map of the key schema classes.
- **Curating an entry?** Start with the [Curation Primers](#curation-primers) and the [How-to Guides](quality-control.md).
- **Need exact schema details?** See the full [Schema Reference](schema/schemas/dismech.md).

## Curation Primers

Short, visual guides to the modeling patterns you'll use most:

- [Phenotype Association Context](primers/phenotype-context.md) — scoped phenotype assertions; OMIM-like vs Orphanet-like sources; `phenotype_contexts` vs `has_subtypes`.
- [Preferred Term vs Ontology Label](primers/preferred-term-vs-label.md) — the two-field display/ontology contract and when to diverge.
- [Modules & Conformance](primers/modules-and-conformance.md) — `conforms_to` as consistency checking, not inheritance.

For the deeper conceptual background, see
[Contextualization](explanation/contextualization.md) and
[Post-composition Terms](explanation/post-composition.md).

## The main site

- [dismech.monarchinitiative.org](https://dismech.monarchinitiative.org/) — project home
- [Disorder browser](https://dismech.monarchinitiative.org/app/) — browse the knowledge base
- [Detailed docs](https://dismech.monarchinitiative.org/details/) — how a disorder page is built
- [GitHub repository](https://github.com/monarch-initiative/dismech)
