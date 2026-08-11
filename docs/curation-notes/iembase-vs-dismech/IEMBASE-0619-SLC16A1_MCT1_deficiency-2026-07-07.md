# IEMbase 0619: SLC16A1-related monocarboxylate transporter-1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 619 |
| Nosology | 4.3.04.01 |
| Gene | SLC16A1 |
| External IDs | OMIM:616095; ORPHA:438075 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | None exact; `Primary_Carnitine_Deficiency.yaml` is a weak false candidate |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SLC16A1-related monocarboxylate transporter 1 deficiency /
MCT1 deficiency as an autosomal dominant or autosomal recessive disorder with
unknown treatability.

The biochemical signal is ketone-utilization focused: acetoacetate and ketones
in blood/plasma and urine range from normal to very high in infancy and
childhood, urinary 3-hydroxybutyric acid ranges from normal to very high, and
urinary C6-C10 dicarboxylic acids range from normal to high. Glucose can be low
to normal, while ammonia, lactate, free carnitine, acylcarnitines, and
acylglycines are represented as normal in the cached rows.

Clinical and characteristic rows include optional developmental delay, optional
hypoglycemia from the neonatal period through childhood, and optional
ketoacidosis in infancy/childhood. The treatment row is avoidance of fasting
with level 4 evidence from PMID:25390740, with decreased blood ketones as the
reported metabolic effect.

## DisMech phenotype coverage

No exact local SLC16A1/MCT1 deficiency entry was identified.
`Primary_Carnitine_Deficiency.yaml` is a false candidate: SLC22A5-related
carnitine transport deficiency is mechanistically and biochemically distinct
from SLC16A1-related monocarboxylate/ketone transport deficiency.

This record should also stay distinct from the earlier SLC16A1 superactivity /
HHF7 note. Both involve SLC16A1, but IEMbase separates MCT1 deficiency from
exercise-induced hyperinsulinism due to MCT1 superactivity.

## Concordance and completeness

Judgement: true local gap.

DisMech currently lacks an exact MCT1 deficiency target, and the closest local
candidate is a transporter-neighborhood false positive rather than useful
coverage.

## Curation actions

- Do not map to `Primary_Carnitine_Deficiency.yaml`.
- Curate SLC16A1/MCT1 deficiency separately from SLC16A1/HHF7 superactivity.
- Preserve ketone-utilization, hypoglycemia, ketoacidosis, normal
  carnitine/acylcarnitine, and avoidance-of-fasting prompts during source
  review.
