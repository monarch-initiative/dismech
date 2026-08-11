# IEMbase 0217: GSS-related Glutathione synthetase deficiency, mild

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 217 |
| Nosology | 2.1.02.01 |
| Gene | GSS |
| External IDs | OMIM:266130 |
| Generated mapping | UNMAPPED; best candidate `Hereditary_Orotic_Aciduria.yaml` |
| Candidate DisMech targets | No valid local target found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as GSS-related glutathione synthetase deficiency, mild,
with alternate labels 5-oxoprolinuria and pyroglutamic aciduria. The record is
autosomal recessive, marked as a mild form, and treatability is marked yes,
though no treatment rows are listed in the cached record.

The biochemical rows include markedly decreased glutathione synthetase activity
in fibroblasts and RBCs, decreased RBC glutathione, normal-to-increased urinary
5-oxoproline, low hemoglobin, and increased reticulocytes. The clinical rows
are hemolytic anemia and jaundice.

## DisMech phenotype coverage

No dedicated GSS or glutathione synthetase deficiency disorder was found in
`kb/disorders`. The generated candidate `Hereditary_Orotic_Aciduria.yaml` is
not valid: it covers UMPS-related pyrimidine synthesis failure and orotic acid
overexcretion, not GSS-related glutathione synthesis failure or
5-oxoprolinuria. `5-Oxoprolinase_Deficiency.yaml` is a useful pathway/differential
neighbor because OPLAH and GSS can both produce 5-oxoprolinuria, but it is not a
valid target for this GSS disease.

## Concordance and completeness

Judgement: true local gap.

IEMbase has a compact but coherent mild GSS deficiency profile: GSS enzyme
deficiency, low RBC glutathione, urinary 5-oxoproline, hemolytic anemia,
reticulocytosis, and jaundice. No local entry represents that gene-specific
glutathione synthetase defect.

## Curation actions

- Add GSS-related glutathione synthetase deficiency as a future local disease if
  glutathione-cycle disorders are curated.
- Reject `Hereditary_Orotic_Aciduria.yaml` as a lexical/metabolite-neighbor
  false candidate.
- Use `5-Oxoprolinase_Deficiency.yaml` only as differential context, not as a
  mapping target.
