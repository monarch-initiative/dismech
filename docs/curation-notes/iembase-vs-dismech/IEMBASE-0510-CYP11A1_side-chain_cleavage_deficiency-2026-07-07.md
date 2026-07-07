# IEMbase 0510: CYP11A1-related side-chain cleavage enzyme deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 510 |
| Nosology | 15.7.01.02 |
| Gene | CYP11A1 |
| External IDs | OMIM:118485; ORPHA:289548 |
| Generated mapping | UNMAPPED; best candidate `Nonketotic_Hyperglycinemia.yaml` |
| Candidate DisMech targets | No exact local target found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as CYP11A1-related side-chain cleavage enzyme deficiency,
with alternate labels desmolase deficiency and P450scc deficiency. No treatments
are listed. The biochemical rows show a salt-wasting adrenal pattern: potassium
is high or very high from the neonatal period onward, and sodium is very low in
the neonatal/infant period with persistent low or low-normal values later.

Clinical-characteristic rows include adrenal insufficiency, frequent ambiguous
genitalia in 46,XY individuals, and very frequent cryptorchidism. Adrenal
hyperplasia is recorded as normal, which helps distinguish this from some other
congenital adrenal hyperplasia presentations.

## DisMech phenotype coverage

No exact local CYP11A1/P450scc target was found. The generated candidate
`Nonketotic_Hyperglycinemia.yaml` is invalid: it covers GLDC/AMT/GCSH glycine
cleavage deficiency with glycine accumulation, neonatal encephalopathy, seizures,
hypotonia, and apnea, not adrenal steroidogenesis or sex-development findings.

`Congenital_Adrenal_Hyperplasia.yaml` provides useful pathway context for
steroidogenesis disorders, and `Chronic_Primary_Adrenal_Insufficiency.yaml`
provides syndrome context for adrenal failure with electrolyte disturbance. The
local CAH entry includes common enzyme defects such as CYP21A2, CYP11B1,
CYP17A1, HSD3B2, and STAR, but it does not include CYP11A1/desmolase/P450scc
side-chain cleavage deficiency.

## Concordance and completeness

Judgement: true local gap.

The IEMbase profile is specific for CYP11A1 steroid side-chain cleavage failure:
salt-wasting adrenal insufficiency, potassium/sodium abnormalities, and 46,XY
undervirilization/cryptorchidism. Local adrenal entries give context but not the
gene-specific disease.

## Curation actions

- Track CYP11A1-related P450scc deficiency as a local steroidogenesis gap.
- Reject `Nonketotic_Hyperglycinemia.yaml` as a lexical false candidate.
- If curated, decide whether CYP11A1 belongs as a new subtype under congenital
  adrenal hyperplasia or as a linked adrenal-insufficiency/sex-development entry;
  preserve the normal adrenal hyperplasia row as a differentiating prompt.
