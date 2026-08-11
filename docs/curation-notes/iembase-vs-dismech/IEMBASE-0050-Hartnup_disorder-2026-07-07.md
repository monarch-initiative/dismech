# IEMbase 0050: SLC6A19-related Hartnup disorder

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 50 |
| Nosology | 1.11.01.01 |
| Gene | SLC6A19 |
| External IDs | OMIM:234500 |
| Generated mapping | MAPPED by `alias_exact:hartnup disorder` |
| Candidate DisMech targets | `Hartnup_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive SLC6A19-related Hartnup disorder.
The listed prevalence is 1:30,000 and treatability is marked yes, although no
specific treatment rows are present in the cached record.

The biochemical signal is increased urinary neutral amino acids, with urinary
glutamic acid normal-to-increased. The characteristic clinical feature is
possible photosensitivity in infancy through adolescence. Additional possible
features are ataxia and psychotic behavior.

## DisMech phenotype coverage

The generated mapping to `Hartnup_Disease.yaml` is correct. DisMech models
Hartnup disease as an autosomal recessive neutral aminoaciduria caused mainly by
SLC6A19/B0AT1 loss of function in renal proximal tubule and intestinal
epithelial cells, with impaired neutral amino acid and tryptophan transport.

DisMech covers neutral hyperaminoaciduria, elevated urinary indican, low
systemic tryptophan availability, malabsorption, tryptophan and nicotinamide
availability reduction, pellagra-like photosensitive rash, ataxia, psychosis,
emotional lability, hallucinations, anxiety, hypotonia, hyperreflexia, tremor,
EEG abnormality, migraine, seizures, photophobia, nystagmus, strabismus, and
vision abnormalities. It also includes SLC6A19 genetic testing and treatment
content: oral nicotinamide, experimental tryptophan ethyl ester bypass therapy,
sunlight avoidance/photoprotection, and genetic counseling.

## Concordance and completeness

Judgement: correct mapping and high concordance. IEMbase is a compact,
diagnostic-level representation; DisMech is substantially richer for mechanism,
phenotype breadth, biomarkers, and management.

IEMbase adds little beyond confirming the core SLC6A19 neutral-aminoaciduria
signal and the expected photosensitivity, ataxia, and psychotic behavior
features. DisMech already captures these and expands the mechanistic
tryptophan-nicotinamide bridge.

## Curation actions

- Keep the generated mapping to `Hartnup_Disease.yaml`.
- Do not use this mapping as support for SLC7A7 lysinuric protein intolerance
  or other non-neutral aminoacidurias.
- No immediate phenotype import is needed from IEMbase unless granular
  age-of-onset annotations become in scope.
