# IEMbase 0512: GSS-related Glutathione synthetase deficiency, severe

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 512 |
| Nosology | 2.1.02.02 |
| Gene | GSS |
| External IDs | OMIM:266130; ORPHA:32 |
| Generated mapping | UNMAPPED; best candidate `Hereditary_Orotic_Aciduria.yaml` |
| Candidate DisMech targets | No exact local target found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as severe GSS-related glutathione synthetase deficiency,
with alternate labels 5-oxoprolinuria and pyroglutamic aciduria. Treatability is
marked yes, though no treatment rows are listed in the cached JSON.

The biochemical rows include very markedly decreased glutathione synthetase
activity in fibroblasts and RBCs, very low RBC glutathione, very markedly
increased urinary 5-oxoproline, low hemoglobin, high reticulocytes, and high
lactate. The clinical and clinical-characteristic rows add acidosis, lactic
acidosis, hemolytic anemia, recurrent bacterial infections, neurological
symptoms, psychomotor delay, seizures, ataxia, tone abnormalities, myopathy,
corneal clouding, pigmentary retinopathy, night blindness, and jaundice.

## DisMech phenotype coverage

No dedicated GSS or glutathione synthetase deficiency entry was found in
`kb/disorders`. The generated candidate `Hereditary_Orotic_Aciduria.yaml` is
not valid because it covers UMPS-related pyrimidine synthesis failure and orotic
acid overexcretion, not glutathione synthesis failure or 5-oxoprolinuria.

`5-Oxoprolinase_Deficiency.yaml` is a useful gamma-glutamyl-cycle neighbor and
differential diagnosis because both OPLAH and GSS defects can produce
5-oxoprolinuria. It is not an exact target for this GSS disease.

## Concordance and completeness

Judgement: true local gap.

The earlier mild GSS IEMbase record also resolved as a local gap. This severe
record strengthens the same gap and adds multisystem severity: metabolic/lactic
acidosis, neurological disease, recurrent infections, and ocular findings on top
of the core GSS enzyme deficiency, low glutathione, urinary 5-oxoproline, and
hemolytic anemia signal.

## Curation actions

- Add GSS-related glutathione synthetase deficiency as a future local disease,
  with mild and severe phenotype branches if the spectrum is curated.
- Reject `Hereditary_Orotic_Aciduria.yaml` as a metabolite-neighbor false
  candidate.
- Use `5-Oxoprolinase_Deficiency.yaml` only as pathway/differential context.
- Preserve severe-form prompts for acidosis, lactic acidosis, recurrent
  infections, seizures, psychomotor delay, tone abnormalities, myopathy, and
  ocular involvement.
