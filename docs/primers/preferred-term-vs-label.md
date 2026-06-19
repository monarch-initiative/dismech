# Primer: Preferred Term vs Ontology Label

Every descriptor in Dismech (phenotype, cell type, treatment, …) carries **two**
label fields, and they answer different questions. Mixing them up is one of the
most common curation slips.

## The two-field contract

```
descriptor:
  preferred_term: <- YOUR display name. Can be MORE specific than the ontology.
  term:
    id:    <- the ontology CURIE
    label: <- MUST match the ontology's canonical label EXACTLY (verified by OAK)
```

| Field | Rule | Who checks it |
|-------|------|---------------|
| `term.label` | **Exact** canonical ontology string. Never paraphrase. | `just validate-terms-file` (OAK) |
| `preferred_term` | Human-readable display name. **May be more specific/nuanced** than the ontology term. | curator judgment |

Why diverge? Because the ontology often only has a **broad parent** when you
want to convey clinical granularity. Link to the best-fit term anyway, and let
`preferred_term` carry the nuance. A `modifier` can capture some of that meaning
too.

```
  ontology term (broad, canonical)        preferred_term (specific, display)
  ┌───────────────────────────┐           ┌──────────────────────────────┐
  │ CL:0000815                │  ◄───────  │ CD4+ regulatory T cell       │
  │ "regulatory T cell"       │   binds    │                              │
  └───────────────────────────┘            └──────────────────────────────┘
        term.label = exact                       more specific than CL has
```

## Three worked examples

**1. Cell type more specific than CL has a term for:**
```yaml
cell_types:
- preferred_term: CD4+ regulatory T cell   # the clinical specificity you want
  term:
    id: CL:0000815
    label: regulatory T cell               # the exact CL label
```

**2. Treatment more specific than the generic action term:**
```yaml
treatments:
- name: Anti-TNF Biologic Therapy
  treatment_term:
    preferred_term: anti-TNF biologic therapy
    term:
      id: NCIT:C15986
      label: Pharmacotherapy               # generic action; specifics go elsewhere
```

**3. When the ontology *does* match closely — prefer its label for clarity:**
```yaml
phenotype_term:
  preferred_term: Diarrhea
  term:
    id: HP:0002014
    label: Diarrhea                         # preferred_term == label is fine & ideal
  temporality: CHRONIC
```

## Guidelines

- Always link to the **most specific available** ontology term, even when `preferred_term` is more granular.
- If a term matches closely, reuse its label as `preferred_term` for consistency.
- Reach for a more nuanced `preferred_term` **only** when the ontology term is genuinely too broad.
- Verify every `term.label` with OAK, e.g. `uv run runoak -i sqlite:obo:hp info HP:0002014 -O obo`.

## Go deeper

- [Post-composition Terms](../explanation/post-composition.md) — `modifier`, `located_in`, `laterality`, onset/temporality/severity, and `therapeutic_agent`.
- [Schema: PhenotypeDescriptor](../schema/classes/PhenotypeDescriptor.md) · [CellTypeDescriptor](../schema/classes/CellTypeDescriptor.md) · [TreatmentDescriptor](../schema/classes/TreatmentDescriptor.md)
