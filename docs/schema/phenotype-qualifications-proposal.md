# Phenotype Qualifications: Schema Proposal

**Status**: Implemented (pilot on Fanconi Anemia)
**Related issues**: #112 (frequency evidence gap), #113 (qualifier patterns), #222 (spatial qualifiers), #126 (genetics specificity), #272 (lumping/splitting granularity)
**Slot name**: `phenotype_contexts` (on `Phenotype` class)

## Problem Statement

The current `Phenotype` class has a flat structure where:

1. `evidence` conflates two distinct claims: (a) "this phenotype occurs in this disease" (D2P association) and (b) "it occurs at this frequency" — these often have different supporting evidence.
2. `frequency` is a scalar that applies to the entire disease population, but many diseases (especially lumped entries like Fanconi Anemia) have subtype-specific or context-specific frequencies.
3. Genotype-phenotype correlations are relegated to free-text `notes` fields with no computable structure.
4. Sex-specific, population-specific, and age-specific frequency differences cannot be represented.

### Concrete Example: Fanconi Anemia

Currently in `Fanconi_Anemia.yaml`:
```yaml
- name: Microcephaly
  frequency: FREQUENT
  notes: >-
    Skull anomalies were significantly more common in patients with
    downstream FA gene mutations (FANCD1, FANCJ) compared to core
    complex mutations (P<0.001). FA-S (biallelic BRCA1) patients
    also frequently present with microcephaly.
  evidence:
  - reference: PMID:20301575
    supports: SUPPORT
    snippet: "skull anomalies (microcephaly)..."  # supports D2P, not frequency
```

The notes contain structured claims (gene-specific frequencies, P-values) that are invisible to computation.

## Design Goals

1. **Separate D2P evidence from frequency/severity evidence** (issue #112)
2. **Enable context-qualified frequency/severity** — qualified by genetic context, sex, population, age, or disease subtype
3. **Support the simple case** — attaching evidence to the overall frequency without any context qualifier
4. **Be generic** — the same mechanism works for genetic, demographic, and clinical qualifiers
5. **Backward compatible** — existing `frequency` and `evidence` remain valid; qualifications are additive
6. **Composable** — qualifiers can combine (e.g., "in FANCA females aged 10-20")

## Proposed Schema

### New Classes

```yaml
classes:
  PhenotypeQualification:
    description: >-
      A context-specific annotation qualifying how a phenotype manifests
      under particular conditions. Each qualification can specify a
      genetic context, demographic stratum, or disease subtype, along
      with the frequency, severity, onset, and supporting evidence
      specific to that context.

      When no context slots are set, the qualification provides
      evidence for the overall/default frequency claim (addressing
      the frequency-evidence separation problem from issue #112).
    slots:
      - frequency
      - severity
      - onset
      - notes
      - evidence
      # Context qualifiers (all optional)
      - genetic_context
      - sex
      - population
      - age_range
      - subtype

  GeneticContext:
    description: >-
      A structured description of a genetic context that modifies
      phenotype frequency, severity, or presentation. Captures
      gene identity, mutation type, zygosity, and functional impact.
    slots:
      - gene
      - genes
      - allele_type
      - zygosity
      - functional_impact
      - complementation_group
      - description
      - notes
```

### New Slots

```yaml
slots:
  qualifications:
    description: >-
      Context-specific qualifications of this phenotype's frequency,
      severity, or onset. Each qualification can optionally specify
      a genetic context, demographic stratum, or disease subtype.
      When no context is set, provides evidence for the base
      frequency/severity claim.
    multivalued: true
    range: PhenotypeQualification
    inlined_as_list: true

  genetic_context:
    description: >-
      The genetic context under which this qualification applies.
      May specify a gene, mutation type, zygosity, or complementation group.
    range: GeneticContext
    inlined: true

  allele_type:
    description: >-
      Type of allele or mutation (e.g., null, missense, splice_site,
      deletion, frameshift, nonsense, hypomorphic).
    range: string

  zygosity:
    description: >-
      Zygosity context (e.g., biallelic, heterozygous, compound_heterozygous,
      hemizygous). Particularly relevant for AR diseases where biallelic
      null may be more severe than compound het with a hypomorphic allele.
    range: string

  functional_impact:
    description: >-
      Functional consequence of the genetic variant
      (e.g., loss_of_function, gain_of_function, dominant_negative).
    range: string

  complementation_group:
    description: >-
      Complementation group designation (e.g., FA-A, FA-D1, BBS1).
      Used for genetically heterogeneous diseases where subtypes
      are historically named by complementation analysis.
    range: string

  onset:
    description: >-
      Age of onset or onset pattern for the phenotype in this context.
    range: string
    examples:
      - value: "First decade"
      - value: "Neonatal"
      - value: "Mean 18.5 years"
```

### Modified Phenotype Class

```yaml
classes:
  Phenotype:
    slots:
      - category
      - name
      - phenotype_term
      - frequency          # Retained: overall/typical frequency
      - description
      - diagnostic
      - sequelae
      - evidence           # Retained: scoped to D2P association evidence
      - context
      - review_notes
      - severity
      - notes
      - subtype
      - qualifications     # NEW: context-specific frequency/severity/evidence
```

## Usage Patterns

### Pattern 1: Simple frequency evidence (no context) — addresses #112

When you just want to provide separate evidence for the frequency claim:

```yaml
- name: Short Stature
  frequency: VERY_FREQUENT
  evidence:
  - reference: PMID:20301575
    supports: SUPPORT
    snippet: "short stature..."
    explanation: Confirms short stature occurs in FA.
  qualifications:
  - frequency: VERY_FREQUENT
    evidence:
    - reference: PMID:31558676
      supports: SUPPORT
      snippet: "57% met criteria for short stature"
      explanation: Quantitative data from Israeli cohort (n=111).
```

### Pattern 2: Gene-specific frequency — addresses FA genotype-phenotype

```yaml
- name: Microcephaly
  frequency: FREQUENT
  evidence:
  - reference: PMID:20301575
    supports: SUPPORT
    snippet: "skull anomalies (microcephaly)..."
  qualifications:
  - genetic_context:
      genes:
      - preferred_term: FANCD1
      - preferred_term: FANCJ
      description: Downstream FA pathway genes
    frequency: VERY_FREQUENT
    evidence:
    - reference: PMID:31558676
      supports: SUPPORT
      snippet: "skull anomalies were significantly more common in downstream group"
      explanation: "P<0.001 vs core complex mutations."
  - genetic_context:
      gene:
        preferred_term: BRCA1
      complementation_group: FA-S
      zygosity: biallelic
    frequency: VERY_FREQUENT
    evidence:
    - reference: PMID:38146508
      supports: SUPPORT
      snippet: "microcephaly was present in all reported FA-S patients"
```

### Pattern 3: Mutation-type qualification

```yaml
- name: Congenital Heart Defects
  frequency: FREQUENT
  qualifications:
  - genetic_context:
      allele_type: missense
    frequency: OCCASIONAL
    notes: >-
      Missense mutations associated with significantly less congenital
      heart disease (P=0.022) in the Israeli cohort.
    evidence:
    - reference: PMID:31558676
      supports: SUPPORT
      snippet: "patients with missense mutations had fewer congenital heart defects"
```

### Pattern 4: Sex-specific frequency

```yaml
- name: Infertility
  frequency: VERY_FREQUENT
  qualifications:
  - sex: MALE
    frequency: OBLIGATE
    notes: Near-universal azoospermia
    evidence:
    - reference: PMID:25575015
      supports: SUPPORT
      snippet: "males are almost universally infertile"
  - sex: FEMALE
    frequency: FREQUENT
    notes: Reduced but not absent; pregnancies reported.
    evidence:
    - reference: PMID:25575015
      supports: SUPPORT
      snippet: "females have reduced fertility but pregnancies have been reported"
```

### Pattern 5: Population-specific frequency

```yaml
- name: Some Phenotype
  frequency: OCCASIONAL
  qualifications:
  - population: Ashkenazi Jewish
    frequency: FREQUENT
    notes: Founder effect for FANCC IVS4+4A>T
    evidence:
    - reference: PMID:XXXXXXXX
      supports: SUPPORT
      snippet: "..."
```

### Pattern 6: Combined qualifiers

```yaml
- name: Myelodysplastic Syndrome
  frequency: FREQUENT
  qualifications:
  - genetic_context:
      gene:
        preferred_term: FANCA
    onset: "Mean 18.5 years"
    evidence:
    - reference: PMID:31558676
      supports: SUPPORT
      snippet: "FANCA patients developed cancer at significantly older age (mean 18.5 years)"
  - genetic_context:
      genes:
      - preferred_term: FANCC
      - preferred_term: FANCD1
      - preferred_term: FANCG
      - preferred_term: FANCJ
      description: Non-FANCA complementation groups
    onset: "Mean 5.2 years"
    evidence:
    - reference: PMID:31558676
      supports: SUPPORT
      snippet: "non-FANCA groups (mean 5.2 years, P=0.001)"
```

## How This Resolves Open Issues

| Issue | Resolution |
|-------|------------|
| **#112** (frequency evidence gap) | Use a qualification with no context set to attach evidence specifically to the frequency claim, separate from D2P evidence |
| **#113** (qualifier patterns) | `PhenotypeQualification` replaces the deprecated generic `Qualifier` mechanism for phenotype-level qualifiers. Temporal qualifiers can use the `onset` slot. |
| **#222** (spatial extent) | Orthogonal — spatial extent is about qualifying the phenotype itself (post-composition on the Descriptor), not about context-dependent frequency. The deprecated `qualifiers` or explicit spatial slots address that. |
| **#126** (genetics specificity) | `GeneticContext` on qualifications provides structured gene/variant info linked to specific phenotypes |
| **#272** (lumping/splitting) | For Level 2A lumped diseases, qualifications allow capturing subtype-specific frequencies within a single entry, reducing pressure to split |

## Migration Strategy

**Fully backward compatible.** No existing files need to change:

- `frequency` on Phenotype remains and works as-is (overall frequency)
- `evidence` on Phenotype remains and works as-is (D2P evidence)
- `qualifications` is a new optional multivalued slot
- Existing `notes` with genotype-phenotype info can be gradually migrated to structured qualifications

### Incremental migration steps:

1. Add schema classes (non-breaking)
2. Migrate Fanconi Anemia as pilot (move notes → qualifications)
3. Add compliance check for "phenotype has notes mentioning gene names but no qualifications"
4. Migrate other genetically heterogeneous entries (BBS, NF1, etc.)

## Slot Usage on PhenotypeQualification

```yaml
slot_usage:
  sex:
    range: SexEnum
  evidence:
    description: >-
      Evidence supporting the frequency, severity, or onset claims
      made in this specific context. Distinct from the D2P evidence
      on the parent Phenotype.
  frequency:
    description: >-
      The frequency of this phenotype in the specified context.
      Overrides or supplements the parent Phenotype's base frequency.
```

## Design Decisions (Resolved)

1. **Naming**: `phenotype_contexts` — specific to phenotypes, and suggests a pattern reusable on other entity types (e.g., `biochemical_contexts`).

2. **`onset`**: Uses `OnsetDescriptor` bound to HPO onset terms (HP:0003674 subtree) via dynamic enum `OnsetTerm`. Also accepts free text for specific values like "Mean 18.5 years" (slot is `any_of: [OnsetDescriptor, string]`).

3. **`zygosity`**: Uses `ZygosityDescriptor` bound to GENO zygosity terms (GENO:0000133 subtree) via dynamic enum `ZygosityTerm`. Captures homozygous (GENO:0000136), heterozygous (GENO:0000135), compound heterozygous (GENO:0000402), hemizygous (GENO:0000134), etc.

4. **`allele_type`**: Free text string. The diversity of mutation nomenclature (null, missense, splice_site, deletion, frameshift, structural_variant, hypomorphic, etc.) makes a closed enum impractical.

5. **`GeneticContext` flexibility**: Uses existing `GeneDescriptor` for `gene`/`genes` slots (gets HGNC validation for free). But also has `description`, `complementation_group`, `allele_type`, `functional_impact` as free-text slots. This accommodates everything from single genes to structural variants to complex genotypes without disrupting existing entries.

6. **`onset` and `severity` alongside frequency**: Yes — both are included. The FA data shows onset varies by genotype (mean 18.5 vs 5.2 years) and severity varies by mutation type (deletion patients shorter than nonsense).

## Remaining Open Questions

1. **Should `functional_impact` become an enum?** Candidates: loss_of_function, gain_of_function, dominant_negative, haploinsufficiency. Currently free text.

2. **Should we add an `onset` slot directly to `Phenotype`?** Currently onset can only be captured inside a `PhenotypeContext`. Some phenotypes have an overall onset independent of genetic context.

3. **Should the `_contexts` pattern be extended to other classes?** Biochemical markers, histopathology findings, and treatments could all benefit from context-dependent annotations.
