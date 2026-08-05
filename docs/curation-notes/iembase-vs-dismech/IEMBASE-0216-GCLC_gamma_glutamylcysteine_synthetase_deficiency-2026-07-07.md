# IEMbase 0216: GCLC-related Gamma-glutamylcysteine synthetase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 216 |
| Nosology | 2.1.01.01 |
| Gene | GCLC |
| External IDs | OMIM:230450 |
| Generated mapping | UNMAPPED; best candidate `Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml` |
| Candidate DisMech targets | No valid local target found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as GCLC-related gamma-glutamylcysteine synthetase
deficiency, with alternate labels glutamate-cysteine ligase deficiency,
hemolytic anemia due to GGCS deficiency, and GGCS. The record is autosomal
recessive and treatability is marked unknown.

The biochemical rows include markedly decreased gamma-glutamyl-cysteine
synthetase activity in fibroblasts and RBCs, markedly decreased RBC
glutathione, low hemoglobin, increased reticulocytes, and normal-to-increased
plasma amino acids. Characteristic clinical rows include hemolytic anemia and
jaundice, with additional rows for ataxia, psychotic behavior, myopathy, and
neurocognitive/behavioral issues. No treatment rows are listed in the cached
record.

## DisMech phenotype coverage

No dedicated GCLC or gamma-glutamylcysteine synthetase deficiency disorder was
found in `kb/disorders`. The generated candidate
`Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml` is not valid: it covers CPS1
proximal urea-cycle disease with hyperammonemia, low citrulline, and normal or
low orotic acid, not GCLC/glutathione-biosynthesis disease. Nearby local
gamma-glutamyl-cycle content in `5-Oxoprolinase_Deficiency.yaml` is
OPLAH-specific and does not cover GCLC deficiency.

## Concordance and completeness

Judgement: true local gap.

IEMbase provides a coherent GCLC deficiency profile anchored on enzyme
deficiency, low RBC glutathione, hemolytic anemia, reticulocytosis, jaundice,
and optional neurologic/psychiatric features. The local CPS1 candidate shares
only a synthetase-word lexical overlap and is mechanistically unrelated.

## Curation actions

- Add GCLC-related gamma-glutamylcysteine synthetase deficiency as a future
  local disease if glutathione-cycle disorders are curated.
- Reject `Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml` as a false
  candidate.
- Use IEMbase as a lead for RBC glutathione, enzyme-activity, hemolytic anemia,
  reticulocyte, and jaundice rows.
