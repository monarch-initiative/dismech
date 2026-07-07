# IEMbase 0135: ACAD8-related Isobutyryl-CoA dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 135 |
| Nosology | 1.2.08.01 |
| Gene | ACAD8 |
| External IDs | OMIM:611283; ORPHA:79159 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Isobutyryl-CoA_Dehydrogenase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ACAD8-related isobutyryl-CoA dehydrogenase
deficiency, with alternate labels isobutyrylglycinuria and IBD. Treatability is
marked unknown.

Characteristic biochemical rows include increased urinary isobutyrylglycine,
increased C4 acylcarnitine, and decreased free carnitine in dried blood spot and
plasma. Other rows include increased esterified carnitine and decreased
fibroblast isobutyryl-CoA dehydrogenase activity. Clinical rows include that
most patients appear asymptomatic, episodic vomiting, anemia, and dilated
cardiomyopathy. No treatment rows are listed.

## DisMech phenotype coverage

`Isobutyryl-CoA_Dehydrogenase_Deficiency.yaml` is the correct local target. It
models ACAD8 deficiency as a rare autosomal recessive valine-catabolism disorder
often detected by newborn screening through elevated C4-acylcarnitine, with
many individuals remaining asymptomatic and a minority having anemia,
developmental delay, hepatic abnormalities, vomiting, or rare cardiomyopathy.

The local biochemical section includes C4-acylcarnitine, urinary
isobutyrylglycine, free carnitine, C4 ratio biomarkers, and related organic-acid
signals. Treatment coverage includes conservative monitoring, dietary
management, L-carnitine supplementation when secondary deficiency is present,
emergency glucose precautions, and newborn screening.

## Concordance and completeness

Judgement: correct mapping with strong local coverage.

IEMbase and DisMech agree on the ACAD8/valine-catabolism mechanism, elevated C4
acylcarnitine, urinary isobutyrylglycine, carnitine depletion, usually
asymptomatic course, and rare anemia/cardiomyopathy/vomiting signals. DisMech is
substantially richer for mechanism, penetrance nuance, subtype framing,
treatment/monitoring, and evidence-backed clinical uncertainty.

## Curation actions

- Keep `Isobutyryl-CoA_Dehydrogenase_Deficiency.yaml` as the canonical target.
- No mapping correction is needed.
- Consider whether decreased fibroblast isobutyryl-CoA dehydrogenase activity
  or esterified carnitine should be represented explicitly if the local
  biochemical panel is expanded.
