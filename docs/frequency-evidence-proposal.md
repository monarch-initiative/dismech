# Frequency Evidence: Schema Design Proposals

## Problem Statement

Issue #112 identifies a fundamental problem: the current schema conflates evidence for two distinct claims:

1. **Disease-to-Phenotype (D2P) Association**: "This phenotype occurs in this disease"
2. **Frequency Claim**: "This phenotype occurs in X% of patients with this disease"

Currently, a `Phenotype` has:
- `frequency`: a simple enum value (FREQUENT, OCCASIONAL, etc.)
- `evidence`: a list of EvidenceItem objects

The evidence list is intended to support the D2P association, but curators often include frequency-related evidence in the same list, or worse, assign frequency qualifiers without any quantitative evidence at all.

### Example of the Problem

```yaml
phenotypes:
- name: Memory Impairment
  frequency: VERY_FREQUENT   # Claims 80-99% prevalence
  evidence:
  - reference: PMID:24459411
    snippet: "Loss of memory is among the first symptoms reported..."
    # This snippet supports D2P but says nothing about frequency
```

The snippet confirms memory impairment occurs in Alzheimer's but provides no data supporting "VERY_FREQUENT" (80-99%).

---

## Option 1: Add `frequency_evidence` Slot (Minimal Change)

### Schema Change

Add a new slot `frequency_evidence` to the `Phenotype` class:

```yaml
slots:
  frequency_evidence:
    description: Evidence specifically supporting the frequency qualifier claim
    multivalued: true
    range: EvidenceItem
    inlined_as_list: true

classes:
  Phenotype:
    slots:
      - category
      - name
      - phenotype_term
      - frequency
      - frequency_evidence   # NEW
      - description
      - diagnostic
      - sequelae
      - evidence            # Scoped to D2P association
      - context
      - ...
```

### Example Usage

```yaml
phenotypes:
- name: Memory Impairment
  frequency: VERY_FREQUENT
  evidence:
    - reference: PMID:24459411
      snippet: "Loss of memory is among the first symptoms reported..."
      explanation: Confirms memory impairment is characteristic of AD.
  frequency_evidence:
    - reference: PMID:12345678
      snippet: "In our cohort of 500 AD patients, 94% exhibited memory impairment at presentation."
      explanation: Quantitative data supporting VERY_FREQUENT classification.
```

### Pros

1. **Minimal disruption**: Existing data remains valid; migration is optional
2. **Clear separation**: Unambiguous which evidence supports which claim
3. **Backward compatible**: Files without `frequency_evidence` still validate
4. **Simple implementation**: No new classes, just one new slot
5. **Low cognitive load**: Easy for curators to understand

### Cons

1. **Flat structure**: Frequency remains a simple enum; no room for additional metadata (e.g., population, source study, confidence)
2. **Duplication potential**: Same PMID might appear in both `evidence` and `frequency_evidence`
3. **Incomplete model**: Does not capture frequency as a first-class entity with its own semantics
4. **Validation gaps**: Cannot easily validate that frequency_evidence contains quantitative data

---

## Option 2: Promote Frequency to Full Object (Comprehensive Refactor)

### Design Philosophy

Following the pattern established by other descriptor classes (PhenotypeDescriptor, TreatmentDescriptor, etc.), frequency becomes a structured object that can hold its own evidence, source context, and metadata.

### Schema Changes

```yaml
classes:
  FrequencyDescriptor:
    description: A structured descriptor for phenotype frequency with supporting evidence
    slots:
      - frequency_category    # The enum value (FREQUENT, OCCASIONAL, etc.)
      - percentage            # Optional: exact percentage if known (e.g., "70%", "30-50%")
      - population            # Optional: which population this applies to
      - source_cohort_size    # Optional: sample size from source study
      - evidence              # Evidence supporting this frequency claim
      - notes                 # Additional context
    slot_usage:
      evidence:
        description: Evidence specifically supporting this frequency claim

slots:
  frequency_category:
    range: FrequencyEnum
    description: The HPO frequency category (FREQUENT, OCCASIONAL, etc.)

  frequency_descriptor:
    description: Structured frequency information with evidence
    range: FrequencyDescriptor
    inlined: true

classes:
  Phenotype:
    slots:
      - category
      - name
      - phenotype_term
      - frequency_descriptor   # REPLACES: frequency
      - description
      - diagnostic
      - sequelae
      - evidence              # Scoped to D2P association
      - context
      - ...
```

### Example Usage

```yaml
phenotypes:
- name: Memory Impairment
  phenotype_term:
    preferred_term: Memory impairment
    term:
      id: HP:0002354
      label: Memory impairment
  evidence:
    - reference: PMID:24459411
      snippet: "Loss of memory is among the first symptoms reported..."
      explanation: Confirms memory impairment is characteristic of AD.
  frequency_descriptor:
    frequency_category: VERY_FREQUENT
    percentage: "94%"
    population: "Sporadic late-onset AD"
    source_cohort_size: 500
    evidence:
      - reference: PMID:12345678
        snippet: "In our cohort of 500 AD patients, 94% exhibited memory impairment at presentation."
        explanation: Large cohort study providing quantitative frequency data.
    notes: Rate may vary in early-onset familial forms.
```

### Pros

1. **Rich semantics**: Captures percentage, population context, cohort size alongside the category
2. **Pattern consistency**: Follows established Descriptor pattern used throughout schema
3. **Future-proof**: Easy to add additional metadata fields (e.g., confidence intervals, method)
4. **Self-documenting**: Structure makes it obvious what frequency evidence should contain
5. **Population-specific frequencies**: Can model different frequencies in different populations
6. **Validation potential**: Can validate that frequency_category aligns with percentage

### Cons

1. **Breaking change**: Requires migration of all existing files
2. **Increased complexity**: Deeper nesting may be harder for curators
3. **Migration effort**: Need scripts to transform `frequency: ENUM` to `frequency_descriptor: {...}`
4. **Tooling updates**: HTML renderer, compliance checker, etc. all need updates
5. **Optional bloat**: Many files may only use `frequency_category` with empty optional fields

---

## Migration Considerations

### Option 1 Migration

Essentially zero migration required. Existing files remain valid. Curators can optionally add `frequency_evidence` over time.

### Option 2 Migration

Requires a migration script. Basic transformation:

```python
# Before
phenotype = {
    "name": "Memory Impairment",
    "frequency": "VERY_FREQUENT",
    "evidence": [...]
}

# After (automated migration - conservative)
phenotype = {
    "name": "Memory Impairment",
    "frequency_descriptor": {
        "frequency_category": "VERY_FREQUENT"
        # evidence intentionally left empty - needs curation
    },
    "evidence": [...]
}
```

The migration script would:
1. Convert `frequency: ENUM` to `frequency_descriptor: {frequency_category: ENUM}`
2. Leave `evidence` in place (scoped to D2P)
3. Flag files for curator review to add frequency evidence

---

## Recommendation Summary

| Criterion | Option 1 | Option 2 |
|-----------|----------|----------|
| Implementation effort | Low | High |
| Migration required | No | Yes |
| Semantic clarity | Good | Excellent |
| Captures population context | No | Yes |
| Captures exact percentages | No | Yes |
| Pattern consistency | Moderate | High |
| Curator learning curve | Low | Moderate |
| Backward compatibility | Full | None |

### When to Choose Option 1

- If the primary goal is distinguishing D2P evidence from frequency evidence
- If rapid deployment is needed
- If curator bandwidth for migration is limited

### When to Choose Option 2

- If long-term semantic richness is prioritized
- If population-specific frequencies are important (e.g., "90% in Europeans, 70% in East Asians")
- If capturing exact percentages alongside categories is valuable
- If consistency with other Descriptor patterns is desired

---

## Questions for Discussion

1. How important is capturing population-specific frequencies?
2. Do we want to record exact percentages, or are HPO categories sufficient?
3. What is the appetite for a breaking change requiring migration?
4. Should we consider a hybrid: Option 1 now, Option 2 later?
