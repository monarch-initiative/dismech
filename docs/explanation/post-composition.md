# Post-Composition Term Strategy

This document explains the strategies for representing complex concepts in dismech when a single precoordinated ontology term doesn't exist.

## Background: Precoordination vs Post-Composition

**Precoordinated terms** are atomic terms defined in an ontology that already combine multiple concepts. For example:
- `HP:0012532` - "Chronic pain" (combines "chronic" + "pain")
- `GO:0032640` - "tumor necrosis factor production" (already combines a process with a specific cytokine)

**Post-composition** (also called post-coordination) combines a base term with qualifiers to express a more specific concept. This is needed when:
1. The ontology lacks a precoordinated term for the specific concept
2. You need to express directionality (increased/decreased) not captured in the term
3. You need to specify additional context (location, laterality)

## Post-Composition Slots in dismech

The Descriptor base class provides explicit slots for post-composition:

| Slot | Purpose | Range | Available On |
|------|---------|-------|--------------|
| `modifier` | Directional/qualitative change | `ModifierEnum` | All Descriptors |
| `located_in` | Anatomical location | `AnatomicalEntityDescriptor` | All Descriptors |
| `laterality` | Left/right/bilateral | `LateralityEnum` | All Descriptors |
| `therapeutic_agent` | Drug/chemical used in treatment | `ChemicalEntityDescriptor` | TreatmentDescriptor |

### 1. The `modifier` Slot

The most commonly used post-composition mechanism. Handles directional or qualitative changes:

```yaml
biological_processes:
  - preferred_term: neural crest cell migration
    modifier: DECREASED          # Post-composed: "decreased neural crest cell migration"
    term:
      id: GO:0001755
      label: neural crest cell migration
```

**Available modifiers** (`ModifierEnum`):
| Value | Meaning | Example usage |
|-------|---------|---------------|
| `INCREASED` | Upregulated, hyperactive, elevated | Cytokine overproduction |
| `DECREASED` | Downregulated, hypoactive, reduced | Impaired migration |
| `ABNORMAL` | Qualitatively abnormal | Protein misfolding |
| `DYSREGULATED` | Regulation impaired (may be either direction) | BBB permeability |
| `ABSENT` | Not occurring/present | Missing ganglion cells |

**Examples from the knowledge base:**

From `Hirschsprung_Disease.yaml`:
```yaml
cell_types:
  - preferred_term: enteric neuron
    modifier: ABSENT
    term:
      id: CL:0007011
      label: enteric neuron
```

From `Dengue.yaml`:
```yaml
biological_processes:
  - preferred_term: TNF-alpha Production
    modifier: INCREASED
    term:
      id: GO:0032640
      label: tumor necrosis factor production
```

### 2. The `located_in` Slot

Specifies the anatomical location where an entity/process occurs or a procedure is performed:

```yaml
diagnosis_term:
  preferred_term: right heart catheterization
  term:
    id: MAXO:0035118
    label: cardiac catheterization
  located_in:
    preferred_term: right cardiac chamber
    term:
      id: UBERON:0035554
      label: right cardiac chamber
```

This expresses: "cardiac catheterization performed in the right cardiac chamber"

The `located_in` slot takes an `AnatomicalEntityDescriptor`, so you can bind to UBERON terms.

### 3. The `laterality` Slot

Specifies laterality (left, right, or bilateral) for anatomical structures or procedures:

```yaml
phenotype_term:
  preferred_term: unilateral renal agenesis
  term:
    id: HP:0000104
    label: Renal agenesis
  laterality: LEFT
```

**Available values** (`LateralityEnum`):
| Value | Description |
|-------|-------------|
| `LEFT` | Left side of the body |
| `RIGHT` | Right side of the body |
| `BILATERAL` | Both sides of the body |

### 4. The `therapeutic_agent` Slot

Specifies the drug or chemical agent used in a treatment. Use when the MAXO term is generic (e.g., `pharmacotherapy`) but specific drugs are involved:

```yaml
treatment_term:
  preferred_term: pharmacotherapy
  term:
    id: MAXO:0000058
    label: pharmacotherapy
  therapeutic_agent:
    - preferred_term: zinc acetate
      term:
        id: CHEBI:62984
        label: zinc acetate
```

This expresses: "pharmacotherapy using zinc acetate"

**Key points:**
- Multivalued: treatments can involve multiple drugs
- Bind to CHEBI for specific drugs (e.g., `CHEBI:62984` for zinc acetate)
- Use NCIT for drug classes when specific CHEBI term unavailable
- Only available on `TreatmentDescriptor` (used in `treatment_term`)

**Example from `Wilsons_Disease.yaml`:**
```yaml
- name: Zinc Acetate
  description: Blocks intestinal copper absorption, maintenance therapy.
  treatment_term:
    preferred_term: pharmacotherapy
    term:
      id: MAXO:0000058
      label: pharmacotherapy
    therapeutic_agent:
      - preferred_term: zinc acetate
        term:
          id: CHEBI:62984
          label: zinc acetate
```

### Combining Multiple Slots

Slots can be combined when needed:

```yaml
biological_processes:
  - preferred_term: decreased glucose uptake in left ventricle
    modifier: DECREASED
    term:
      id: GO:0098708
      label: glucose import across plasma membrane
    located_in:
      preferred_term: left ventricle
      term:
        id: UBERON:0002084
        label: heart left ventricle
    laterality: LEFT
```

## Deprecated: The `qualifiers` Pattern

The generic `qualifiers` slot (predicate-value pairs) is **deprecated**. It provided OWL-like expressivity but was:
- Difficult to constrain and validate
- Overly complex for common use cases
- Used only once in the entire knowledge base

**Use explicit slots instead:**
- For anatomical location: use `located_in`
- For laterality: use `laterality`
- For directional changes: use `modifier`

If you encounter a post-composition need not covered by these slots, open an issue to discuss adding a new explicit slot rather than using the deprecated `qualifiers` pattern.

## When to Use Post-Composition

### Prefer precoordinated terms when available

Always check if the ontology has the specific term you need:

```bash
uv run runoak -i sqlite:obo:hp search "chronic diarrhea"
```

If `HP:0002028` "Chronic diarrhea" exists, use it directly:
```yaml
phenotype_term:
  preferred_term: Chronic diarrhea
  term:
    id: HP:0002028
    label: Chronic diarrhea
```

### Use `modifier` when:
- Expressing directional changes (increased/decreased)
- The base ontology term exists but you need to indicate abnormality
- The change is about quantity or presence

### Use `located_in` when:
- Specifying where a process occurs anatomically
- Qualifying a procedure with its location
- The location is not part of the precoordinated term

### Use `laterality` when:
- The condition/finding is unilateral or bilateral
- Distinguishing left vs right side involvement
- The laterality is not captured in the base term

## The "Below the Shoreline" Problem

A key issue noted in PR reviews (see PR #60): **precoordinated terms in GO for processes like "X cell activation" exist at a certain level of granularity, but more specific combinations may not exist**.

For example:
- `GO:0042113` - "B cell activation" exists
- But "regulatory B cell activation" might not have a precoordinated term

In such cases:
1. Use the nearest ancestor precoordinated term
2. Add specificity via the cell type descriptor alongside the process
3. Document in `notes` if the representation is approximate

From @cmungall's review: *"extend data model to include precise cell types below the shoreline of GO precoordinated activation terms"*

## Future Extensions: Identified Gaps from PR Reviews

Based on @cmungall's PR reviews, additional post-composition patterns have been identified as candidates for future explicit slots:

### 1. Therapeutic Agent / Drug Specification - IMPLEMENTED

**Status:** Now addressed by the `therapeutic_agent` slot on `TreatmentDescriptor`.

When MAXO lacks a specific term (e.g., no term for "zinc therapy"), use the generic term plus `therapeutic_agent`:

```yaml
treatment_term:
  preferred_term: pharmacotherapy
  term:
    id: MAXO:0000058
    label: pharmacotherapy
  therapeutic_agent:
    - preferred_term: zinc acetate
      term:
        id: CHEBI:62984
        label: zinc acetate
```

**Best practice:** Always prefer specific MAXO terms when available (e.g., `MAXO:0000109` for vitamin C supplementation). Use `therapeutic_agent` only when MAXO is too generic.

### 2. Substrate / Target for Pathophysiology

**Problem:** Pathophysiology entries describing protein aggregation or dysfunction without specifying the protein.

From PR #38 (Frontotemporal Dementia):
```yaml
# Current - describes TDP-43 aggregation but no UniProt term
- name: TDP-43 Proteinopathy
  description: TAR DNA-binding protein of 43 kDa (TDP-43) aggregation...
```

**Future slot candidates:**
- `substrate` or `has_input` - the molecule being processed/affected
- `target` - the protein/gene being targeted (UniProt/HGNC reference)

From @cmungall's review: *"consider adding some kind of GO term plus qualifier to indicate the process/function that is aberrant. Consider also indicating the target e.g. uniprot. This may require extending the data model"*

### 3. Anatomical Qualifiers for Treatments

From PR #61 (Holt-Oram): *"consider adding anatomical qualifiers to the treatment data model"*

This is now addressed by the `located_in` slot being available on all Descriptors, including treatment terms.

## Recommendations for Curators

1. **Always search first**: Use OAK to check if a precoordinated term exists before post-composing
2. **Use explicit slots**: `modifier`, `located_in`, `laterality`, `therapeutic_agent` - these are constrained and validated
3. **Document approximations**: If the representation is inexact, add a `notes` field
4. **Request new explicit slots**: If you frequently need a post-composition pattern not covered by existing slots, open an issue
5. **Avoid deprecated `qualifiers`**: Do not use the generic predicate-value pattern
6. **For pharmacotherapy**: Prefer specific MAXO terms when available. When using generic `MAXO:0000058`, add `therapeutic_agent` with CHEBI terms for the specific drugs

## See Also

- [OWL Post-Coordination](https://oboacademy.github.io/obook/reference/post-composition/) - OBO Academy guide
- [ROBOT Template Post-Composition](http://robot.obolibrary.org/template) - Tooling for creating composite terms
- [HPO Annotations Guide](https://hpo.jax.org/app/help/annotations) - How HPO handles qualifiers
