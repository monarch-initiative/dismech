# TODO: Explicit Trait Ontology Bindings for GWAS Integration

## Problem

GWAS pipelines output quantitative traits (MCH, LDL, BMI) but dismech's `Biochemical`
section uses free-text names and informal presence (Elevated/Decreased). No formal binding
to trait ontologies means no automated mapping from pipeline outputs to dismech entries.

## Proposed Schema Changes

### Option A: Add `trait_term` slot to `Biochemical`

```yaml
Biochemical:
  slots:
    - name
    - biomarker_term     # existing (NCIT)
    - trait_term          # NEW - OBA or LOINC binding
    - presence
    ...
```

### Option B: Separate `QuantitativeTrait` class

```yaml
QuantitativeTrait:
  slots:
    - name
    - trait_term          # OBA binding (e.g. OBA:VT0001586 "blood hemoglobin amount")
    - loinc_code          # LOINC binding (e.g. 718-7 "Hemoglobin [Mass/volume] in Blood")
    - efo_term            # EFO binding (for GWAS Catalog / Open Targets compatibility)
    - direction           # INCREASED / DECREASED / ABNORMAL
    - evidence
```

## Relevant Ontologies

| Ontology | Use Case | Example |
|----------|----------|---------|
| **OBA** (Ontology of Biological Attributes) | Quantitative trait attributes | OBA:VT0001586 "blood hemoglobin amount" |
| **LOINC** | Lab test codes (clinical) | 718-7 "Hemoglobin [Mass/volume] in Blood" |
| **EFO** (Experimental Factor Ontology) | GWAS Catalog / Open Targets trait IDs | EFO:0004509 "hemoglobin measurement" |
| **NCIT** | Already used for biomarker_term | C64848 "Hemoglobin" |

## Mapping Coverage Needed

From Ota et al. Table S2 (54 traits):
- 12 RBC traits → need OBA/LOINC mappings
- 10 other blood traits → need OBA/LOINC mappings
- 28 serum biomarkers → most have LOINC codes
- 4 anthropometric traits → OBA mappings

## Notes

- EFO is probably the most pragmatic choice since Open Targets and GWAS Catalog both use it
- OBA is the most ontologically principled (it's an OBO ontology)
- LOINC is essential for clinical interoperability but has licensing considerations
- Could support multiple bindings (OBA + EFO + LOINC) similar to how phenotypes have HP terms
- The `presence` field (Elevated/Decreased/Present) is already directional but informal;
  could be formalized with the same modifier enum used on phenotypes (INCREASED/DECREASED/ABNORMAL)
- Most GWAS-scale studies use continuous quantitative traits as endpoints, but disease-endpoint
  GWAS (case/control) use EFO disease terms which map to MONDO (already in dismech)
