# Contextualization in dismech

This document explains how dismech captures gene-specific, variant-specific, demographic, and subtype-specific qualifications of phenotypes and treatments.

## The Problem

Many diseases are genetically heterogeneous. The same clinical diagnosis can be caused by mutations in different genes, and phenotype frequency, severity, and onset often vary by genotype. For example:

- In Fanconi Anemia, bone marrow failure occurs in ~82% of patients overall but is **absent** in BRCA2 (FA-D1) patients
- In EGFR-mutant NSCLC, exon 19 deletions respond better to TKIs than L858R mutations
- Nonsense mutations may cause earlier disease onset than deletions in the same gene

A flat list of phenotypes with a single frequency cannot represent this. dismech addresses this with layered contextualization at multiple levels of the data model.

## Mechanisms

### 1. `PhenotypeContext` + `GeneticContext` (structured, primary)

The most powerful mechanism. Each `Phenotype` entry can carry a `phenotype_contexts` list, where each item is a `PhenotypeContext` that qualifies the phenotype under specific conditions.

**`PhenotypeContext` slots:**

| Slot | Purpose |
|------|---------|
| `genetic_context` | Gene, allele type, zygosity, complementation group |
| `sex` | Male / Female |
| `population` | Ethnic or geographic population |
| `age_range` | Age stratum |
| `subtype` | Disease subtype label |
| `frequency` | Frequency under this context |
| `severity` | Severity under this context |
| `onset` | Age of onset (mean, min, max) |
| `evidence` | Evidence specific to this context |
| `notes` | Free-text annotation |

**`GeneticContext` slots:**

| Slot | Purpose | Example |
|------|---------|---------|
| `gene` | Single causal gene | FANCA |
| `genes` | Multiple genes (e.g., a complementation group set) | FANCC, BRCA2, FANCG |
| `allele_type` | Mutation class | `nonsense`, `splice_site`, `deletion` |
| `zygosity` | Zygosity | `HOMOZYGOUS`, `HETEROZYGOUS` |
| `functional_impact` | Functional consequence | `loss_of_function`, `gain_of_function` |
| `complementation_group` | Complementation group label | FA-D1 |
| `description` | Free text for complex genotypes | Structural variants, compound heterozygotes |

**Example: Fanconi Anemia bone marrow failure**

```yaml
phenotype_contexts:
  # Overall frequency
  - frequency: VERY_FREQUENT
    notes: Over 80% of FA patients develop bone marrow failure.
    evidence:
      - reference: PMID:31558676
        snippet: "82% of the patients developed BMF"

  # Gene-specific: BRCA2 patients do NOT get BMF
  - genetic_context:
      gene:
        preferred_term: FANCD1/BRCA2
        term: { id: hgnc:1101, label: BRCA2 }
      complementation_group: FA-D1
    frequency: EXCLUDED
    notes: Neither FANCD1/BRCA2 patient developed BMF.
    evidence:
      - reference: PMID:31558676
        snippet: "neither of the patients with FANCD1 mutations developed BMF"

  # Allele-type-specific: nonsense mutations → earlier cancer
  - genetic_context:
      allele_type: nonsense
    notes: Earlier cancer onset than deletions (P=0.011).
    evidence:
      - reference: PMID:31558676
        snippet: "patients with nonsense and splice site mutations developed the
          first cancer at a significantly lower age than patients with deletions"

  # Population-specific
  - population: Japanese
    notes: ALDH2*2 variant accelerates BMF progression in Japanese FA patients.
    evidence:
      - reference: PMID:24037726
        snippet: "the ALDH2 variant is associated with accelerated progression of BMF"
```

When no context qualifier slots are set (no `genetic_context`, `sex`, `population`, `age_range`, or `subtype`), the context provides evidence for the overall/default frequency claim. This solves the "frequency–evidence separation problem" where a phenotype has a frequency but the evidence supporting that frequency number lives elsewhere.

### 2. Disease-level subtyping (`has_subtypes`)

For diseases where the molecular subtype is the defining axis, dismech supports a `has_subtypes` list on the `Disease` itself. This is used when the subtypes are clinically distinct enough to warrant separate descriptions but share enough pathophysiology to live in one entry.

```yaml
# From EGFR_Mutant_NSCLC.yaml
has_subtypes:
  - name: EGFR Exon 19 Deletion NSCLC
    description: >-
      In-frame deletions in exon 19... Generally associated with better
      response to TKIs and longer progression-free survival than L858R.
  - name: EGFR T790M Resistance NSCLC
    description: >-
      T790M gatekeeper mutation emerges in ~50-60% of patients progressing
      on first/second-generation TKIs. Sensitive to osimertinib.
```

### 3. Treatment → phenotype/mechanism targeting

Treatments link to the phenotypes and mechanisms they address, providing implicit genotype-specificity when combined with phenotype contexts.

**`target_phenotypes`** — which phenotypes a treatment addresses:

```yaml
treatments:
  - name: Doxycycline
    target_phenotypes:
      - preferred_term: Erythema migrans
        term: { id: HP:0031180, label: Erythema migrans }
```

**`target_mechanisms`** — which pathophysiology nodes a treatment acts on, with directionality:

```yaml
treatments:
  - name: AAV-GCDH Gene Therapy
    target_mechanisms:
      - target: GCDH enzymatic deficiency and disrupted lysine catabolism
        treatment_effect: RESTORES
        description: AAV-mediated GCDH replacement restores enzyme activity.
```

Treatment effects use the `TreatmentEffectEnum`: `INHIBITS`, `RESTORES`, `ACTIVATES`, `MODULATES`, `BYPASSES`, `REPLACES`.

### 4. Pathophysiology-level gene binding

Each pathophysiology mechanism can specify which gene(s) drive it via `gene` or `genes` slots:

```yaml
pathophysiology:
  - name: Excitation-Contraction Coupling Defect
    gene:
      preferred_term: RYR1
      term: { id: hgnc:10484, label: RYR1 }
      modifier: DECREASED
```

This binds a specific causal gene to a specific mechanism, allowing different pathophysiology entries within the same disease to be driven by different genes.

### 5. Descriptor-level post-composition

The `modifier`, `located_in`, and `laterality` slots on all descriptors provide lightweight contextualization without requiring full `PhenotypeContext` structures. See [post-composition.md](post-composition.md) for details.

### 6. Free-text `context` field

Simpler classes (`Biochemical`, `Biomarker`, `Treatment`) have a `context` string slot for lightweight, unstructured annotation:

```yaml
biochemical:
  - name: Elevated Creatinine
    context: Marker of declining renal function in advanced disease
biomarkers:
  - name: Anti-Borrelia IgM/IgG
    context: Two-tier testing with ELISA screening and Western blot confirmation
```

## Choosing the Right Mechanism

| Scenario | Mechanism | Example |
|----------|-----------|---------|
| Phenotype frequency/severity differs by gene | `phenotype_contexts` + `genetic_context` | FA: BMF absent in BRCA2 |
| Phenotype differs by mutation type | `genetic_context.allele_type` | Nonsense vs deletion onset age |
| Phenotype differs by sex or population | `PhenotypeContext.sex` / `.population` | ALDH2*2 in Japanese FA |
| Disease has distinct molecular subtypes | `has_subtypes` on Disease | EGFR exon 19 del vs L858R |
| Treatment targets specific phenotypes | `target_phenotypes` on Treatment | Doxycycline → erythema migrans |
| Treatment acts on a specific mechanism | `target_mechanisms` on Treatment | Gene therapy → enzyme deficiency |
| Mechanism caused by a specific gene | `gene`/`genes` on Pathophysiology | RYR1 → calcium channel defect |
| Simple clinical context note | `context` string on Biochemical/Biomarker | "CSF levels increased" |
| Directional/anatomical qualification | `modifier` / `located_in` / `laterality` | DECREASED, right cardiac chamber |

## Limitations and Future Directions

The current model handles gene-level and mutation-type-level contextualization well. Some gaps remain:

- **Variant-level specificity**: `GeneticContext` captures allele types (nonsense, missense) but does not yet model specific variants (e.g., p.R882H in DNMT3A). The `description` free-text slot can capture these, but they are not structured or queryable.
- **Treatment–genotype pairing**: There is no direct slot linking a treatment to a specific genotype context. This is handled indirectly: a treatment's `target_mechanisms` reference pathophysiology entries that are themselves gene-bound, creating an implicit chain. For variant-specific therapies (e.g., osimertinib for T790M), the connection is typically captured in the treatment description and disease subtypes.
- **Compound heterozygotes**: `GeneticContext` supports `genes` (multiple) and `zygosity`, but representing specific compound heterozygous combinations (e.g., "one copy of p.Phe508del + one copy of p.Gly542X") requires the `description` slot.

## See Also

- [Post-Composition Term Strategy](post-composition.md) — `modifier`, `located_in`, `laterality`, `therapeutic_agent`
- `kb/disorders/Fanconi_Anemia.yaml` — richest example of genetic contextualization
- `kb/disorders/EGFR_Mutant_NSCLC.yaml` — disease-level subtyping by molecular variant
- `kb/disorders/Glutaryl-CoA_Dehydrogenase_Deficiency.yaml` — treatment `target_mechanisms` example
