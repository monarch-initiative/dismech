# IEMbase 0755: PLIN1-related perilipin 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 755 |
| Nosology | 14.4.08.01 |
| Nosology code | IEM0662 |
| Gene | PLIN1 |
| External IDs | OMIM:613877; ORPHA:280356 |
| Generated mapping | UNMAPPED; weak candidate `Familial_Partial_Lipodystrophy.yaml` |
| Candidate DisMech targets | `Familial_Partial_Lipodystrophy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase labels this autosomal dominant record as PLIN1-related perilipin 1
deficiency, with alternate name familial partial lipodystrophy type 4. The
source signal includes very high serum cholesterol and triglycerides,
lipodystrophy, low body fat percentage, low BMI, acanthosis nigricans,
diabetes, hypertension, hepatic steatosis, cushingoid appearance, ovarian
failure, and stroke. Several findings are possible in early age bands and
present in adolescence or adulthood.

## DisMech phenotype coverage

`Familial_Partial_Lipodystrophy.yaml` includes a PLIN1-related familial
partial lipodystrophy type 4 subtype with the expected gene and MONDO subtype
context. The generated mapper status is therefore best interpreted as a false
negative or weak partial hit rather than a true local absence.

The local FPLD entry provides broad group-level coverage for partial loss of
subcutaneous fat, insulin resistance, diabetes, hypertriglyceridemia, decreased
HDL, pancreatitis, hepatic steatosis, hypertension, acanthosis nigricans, and
atherosclerosis. It is less explicit for PLIN1-specific phenotype detail and
does not clearly capture IEMbase prompts such as hypercholesterolemia, low BMI,
cushingoid appearance, ovarian failure, or stroke.

## Concordance and completeness

Judgement: false negative with partial local coverage in a broader FPLD entry.

The local entry should be considered disease-family coverage for PLIN1 / FPLD4,
but subtype-level phenotype completeness is limited. IEMbase is useful for
adding PLIN1-specific metabolic, adipose-distribution, reproductive, and
vascular prompts.

## Curation actions

- Treat `Familial_Partial_Lipodystrophy.yaml` as partial local coverage for
  PLIN1 / FPLD4 rather than as an unrelated weak candidate.
- Consider adding subtype-specific PLIN1 phenotype detail if the entry supports
  subtype-level annotations.
- Preserve hypercholesterolemia, low BMI, cushingoid appearance, ovarian
  failure, and stroke as source-specific prompts not clearly covered by the
  group-level entry.
