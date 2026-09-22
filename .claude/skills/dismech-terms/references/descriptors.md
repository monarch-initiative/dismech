# Descriptor qualifiers

### Descriptor Qualifier Slots

Common clinical qualifiers on ontology-bound descriptors should use explicit slots on
the descriptor object rather than the deprecated generic `qualifiers` list:

- `temporality`: `ACUTE`, `TRANSIENT`, `SUBACUTE`, `CHRONIC`, `RECURRENT`,
  `DIURNAL`, `NOCTURNAL`, `PROLONGED`
- `clinical_course`: `PROGRESSIVE`, `STABLE`
- `severity`: prefer enum-backed values (`MILD`, `MODERATE`, `SEVERE`) when the qualifier
  is part of the ontology post-composition; free text is still tolerated for legacy
  phenotype/context summaries
- `onset`: structured `OnsetDescriptor` with `onset_category` and optional age fields

Pattern:
```yaml
phenotype_term:
  preferred_term: Diarrhea
  term:
    id: HP:0002014
    label: Diarrhea
  temporality: CHRONIC

phenotype_term:
  preferred_term: Muscle weakness
  term:
    id: HP:0001324
    label: Muscle weakness
  clinical_course: PROGRESSIVE
```

Use these first-class slots for common post-composition. Reserve `qualifiers` for
more complex predicate-value patterns that are not covered by dedicated slots.
