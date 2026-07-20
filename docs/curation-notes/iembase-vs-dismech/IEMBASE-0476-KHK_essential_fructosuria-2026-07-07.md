# IEMbase 0476: KHK-related hepatic fructokinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 476 |
| Nosology | 3.1.01.01 |
| Gene | KHK |
| External IDs | OMIM:229800; ORPHA:2056 |
| Generated mapping | UNMAPPED; low candidate `Essential_Thrombocythemia.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive KHK-related hepatic fructokinase
deficiency, also called essential fructosuria or ketohexokinase deficiency.
Biochemical rows include decreased hepatic ketohexokinase activity, normal urine
glucose, and positive urine reducing substances. The characteristic clinical
row states "no clinical significance" across age ranges. There are no
treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for KHK-related essential fructosuria.
`Hereditary_Fructose_Intolerance.yaml` mentions ketohexokinase inhibition as an
experimental treatment strategy for ALDOB-related HFI, but that is therapeutic
KHK inhibition in a different disease, not inherited KHK deficiency.

The generated `Essential_Thrombocythemia.yaml` candidate is a false positive.
Local essential thrombocythemia is a clonal myeloproliferative neoplasm with
JAK2/CALR/MPL signaling, thrombocytosis, thrombosis, and bleeding risk. It is
unrelated to benign fructose-metabolism fructosuria.

## Concordance and completeness

Judgement: true KHK essential fructosuria local gap or possible low-priority
scope-review item; reject essential thrombocythemia as an exact mapping.

The IEMbase record is clinically sparse and explicitly marks no clinical
significance, but it is mechanistically distinct from ALDOB hereditary fructose
intolerance and should not be folded into HFI without a deliberate lumping
decision.

## Curation actions

- Keep this record unmapped until a KHK essential fructosuria target exists, or
  until DisMech makes an explicit out-of-scope decision for clinically benign
  biochemical traits.
- Do not map to `Essential_Thrombocythemia.yaml`.
- Do not map to `Hereditary_Fructose_Intolerance.yaml`; KHK inhibition is only
  contextual there.
- If curated, include KHK, autosomal recessive inheritance, decreased hepatic
  ketohexokinase activity, positive urine reducing substances, normal urine
  glucose, essential fructosuria, and the clinically benign/no-significance
  characterization.
