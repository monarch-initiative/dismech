# IEMbase 0203: HFE-related hereditary hemochromatosis type 1

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 203 |
| Nosology | 22.2.01.01 |
| Gene | HFE |
| External IDs | OMIM:235200; ORPHA:443062 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Hemochromatosis.yaml#Type 1` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as HFE-related hereditary hemochromatosis type 1, with
alternate labels HLAH and HFE. Treatability is marked yes.

The biochemical rows include normal-to-increased AST/ALT, normal-to-increased
bilirubin, normal-to-increased ferritin, variable glucose, normal-to-increased
liver iron, normal-to-increased urinary iron, and elevated transferrin
saturation. Characteristic clinical rows include cardiomyopathy, hypogonadism,
and liver fibrosis. Additional rows include abdominal pain, arthralgia,
hyperpigmentation, and hepatocellular carcinoma or hepatoblastoma. No treatment
rows are listed in this IEMbase record.

## DisMech phenotype coverage

`Hemochromatosis.yaml#Type 1` is the correct target even though the generated
mapping left this record unmapped. The local entry explicitly defines Type 1 as
HFE-related hemochromatosis, most often HFE p.Cys282Tyr homozygosity, with
hepcidin insufficiency, elevated transferrin saturation, elevated ferritin,
systemic iron overload, hepatic fibrosis/cirrhosis, hepatocellular carcinoma,
cardiomyopathy, diabetes/hyperglycemia, hypogonadism, arthropathy, fatigue,
abdominal pain, bronze hyperpigmentation, phlebotomy, iron chelation, and
dietary/lifestyle measures.

## Concordance and completeness

Judgement: generated false negative; correct subtype target is
`Hemochromatosis.yaml#Type 1`.

IEMbase and DisMech agree on HFE hemochromatosis identity, iron-overload
biomarkers, elevated transferrin saturation and ferritin, hepatic injury,
cardiomyopathy, hypogonadism, arthralgia/arthropathy, hyperpigmentation, and
hepatocellular carcinoma risk. DisMech is richer for mechanism, subtype scope,
penetrance, treatment, and evidence. IEMbase adds explicit urinary iron and
liver iron rows that could be reviewed as structured biochemical readouts.

## Curation actions

- Correct the crosswalk conclusion to `Hemochromatosis.yaml#Type 1`.
- Consider adding liver iron and urinary iron rows if expanding biochemical
  markers in the hemochromatosis entry.
- Do not treat the unmapped status as a true local gap.
