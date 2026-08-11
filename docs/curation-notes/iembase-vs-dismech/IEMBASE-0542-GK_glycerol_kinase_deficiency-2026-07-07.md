# IEMbase 0542: GK-related isolated glycerol kinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 542 |
| Nosology | 3.2.01.01 |
| Gene | GK |
| External IDs | OMIM:307030; ORPHA:408 |
| Generated mapping | UNMAPPED; low candidate `BCKDK_Deficiency.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents isolated glycerol kinase deficiency, with hyperglycerolemia
and GKD as alternate labels. The record is X-linked, subtype is marked benign
form, and treatability is marked yes. No treatment rows are listed.

The characteristic biochemical rows are increased plasma and urinary glycerol
and increased pseudo-triglyceride in plasma. Plasma glucose is low or normal.
Clinical rows include no clinical significance across ages, with optional
hypoglycemia and adult insulin-resistant diabetes.

## DisMech phenotype coverage

There is no exact local DisMech target for isolated glycerol kinase deficiency.
The generated `BCKDK_Deficiency.yaml` candidate is a lexical kinase-deficiency
neighbor, not a glycerol-metabolism match. BCKDK deficiency models branched-chain
amino acid catabolism, low BCAAs, neurodevelopmental disease, epilepsy, and BCAA
supplementation.

No local disorder file was found for GK, glycerol kinase deficiency,
hyperglycerolemia, or pseudo-hypertriglyceridemia.

## Concordance and completeness

Judgement: true local gap; reject the BCKDK candidate.

The IEMbase record is a benign X-linked glycerol-metabolism disorder with
pseudo-hypertriglyceridemia and glycerol elevation. It should not be mapped to
branched-chain amino acid kinase disease or to neutral-lipid storage disorders.

## Curation actions

- Keep this record unmapped until a GK / isolated glycerol kinase deficiency
  target exists.
- Do not map to `BCKDK_Deficiency.yaml`.
- Preserve increased plasma/urine glycerol, pseudo-triglyceride, low-normal
  glucose, benign/no-clinical-significance scope, hypoglycemia, and
  insulin-resistant diabetes prompts.
