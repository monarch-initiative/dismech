# IEMbase 0378: ABCA1-related Tangier disease

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 378 |
| Nosology | 15.4.23.01 |
| Gene | ABCA1 |
| External IDs | OMIM:600046; OMIM:205400; ORPHA:31150 |
| Generated mapping | MAPPED; `Tangier_Disease.yaml` |
| Candidate DisMech targets | `Tangier_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ABCA1-related Tangier disease, with alternate name primary
familial hypoalphalipoproteinemia and abbreviation TD/FHA. Inheritance is
autosomal recessive.

Clinical rows include hepatosplenomegaly, enlarged orange tonsils, and
peripheral neuropathy. Biochemical rows include serum cholesterol, plasma HDL
cholesterol, serum triglyceride, and apolipoprotein A-I level. There are no
treatment rows.

## DisMech phenotype coverage

The generated mapping to `Tangier_Disease.yaml` is correct. Local DisMech
models biallelic ABCA1 pathogenic variants, impaired apolipoprotein-mediated
cholesterol and phospholipid efflux, failure of HDL biogenesis, severe HDL-C
and ApoA-I depletion, tissue cholesteryl ester accumulation, orange tonsils,
hepatosplenomegaly, peripheral neuropathy, corneal opacity, cardiovascular risk,
dietary risk management, lipid-lowering treatment for ASCVD risk, and
tonsillectomy for obstructive tonsillar disease.

Local coverage is stronger for ABCA1 mechanism, reverse cholesterol transport,
HDL biogenesis, tissue storage, and management. IEMbase is a concise
high-specificity phenotype and biomarker summary.

## Concordance and completeness

Judgement: correct mapping with high concordance.

The resources agree on ABCA1 identity, autosomal recessive inheritance, Tangier
disease identity, orange tonsils, hepatosplenomegaly, peripheral neuropathy,
low HDL cholesterol, low total cholesterol context, triglyceride abnormalities,
and low apolipoprotein A-I. IEMbase lacks treatment rows, while local DisMech
captures supportive/risk-directed management.

## Curation actions

- Keep the generated mapping to `Tangier_Disease.yaml`.
- Consider future enrichment with concise IEMbase wording for enlarged orange
  tonsils, serum cholesterol, serum triglyceride, HDL cholesterol, and
  apolipoprotein A-I rows after source verification.
- Do not import absent IEMbase treatments as negative evidence, because local
  supportive and risk-directed management is already curated.
