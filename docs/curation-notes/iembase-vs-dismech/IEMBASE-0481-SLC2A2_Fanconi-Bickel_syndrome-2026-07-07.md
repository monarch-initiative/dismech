# IEMbase 0481: SLC2A2-related glucose transporter 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 481 |
| Nosology | 3.6.03.01 |
| Gene | SLC2A2 |
| External IDs | OMIM:227810; ORPHA:2088 |
| Generated mapping | UNMAPPED; best candidate `SLC35A2-CDG.yaml` |
| Candidate DisMech targets | `Fanconi-Bickel_Syndrome.yaml`; rejected lexical candidate `SLC35A2-CDG.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive SLC2A2-related glucose transporter 2
deficiency as Fanconi-Bickel syndrome. It records nocturnal enteral nutrition as
a treatment. The biochemical signal is broad and hepatorenal: urinary amino
acids normal to increased, transaminases and alkaline phosphatase normal to
increased, normal glycogenolytic enzymes, increased liver glycogen, urinary
galactitol, urinary calcium and phosphate abnormalities, increased urinary
glucose, low-to-normal fasting plasma glucose, normal-to-high fed glucose,
low-to-normal plasma phosphate, increased cholesterol, triglycerides, uric acid,
and variable blood/urine galactose. Clinical rows include cataract,
hyperfiltration, hypoglycemia, hepatocellular carcinoma/hepatoblastoma, loose
stools, malabsorption, nephromegaly, renal failure, renal tubular acidosis,
rickets, and short stature.

## DisMech phenotype coverage

`Fanconi-Bickel_Syndrome.yaml` is the exact local target. The entry models
biallelic SLC2A2/GLUT2 loss of function, impaired hepatocyte glucose transport,
impaired renal proximal tubular glucose transport, hepatic glycogen
accumulation, fasting hypoglycemia, glucose/galactose intolerance, renal Fanconi
syndrome, glucosuria with normal-to-low blood glucose, hypophosphatemia,
hypophosphatemic rickets, short stature, doll-like facies, hypertriglyceridemia,
dietary management with frequent feeding/cornstarch, phosphate/alkali/active
vitamin D supplementation, and off-label empagliflozin for the renal tubular
branch.

## Concordance and completeness

Judgement: false negative generated mapping; resolve to
`Fanconi-Bickel_Syndrome.yaml`.

The `SLC35A2-CDG.yaml` candidate is not a plausible exact target. IEMbase and
DisMech agree on SLC2A2 identity, autosomal recessive inheritance, GLUT2
transport failure, hepatorenal glycogen accumulation, Fanconi-type proximal
tubulopathy, glucosuria, fasting hypoglycemia, rickets, short stature, and
galactose/glucose intolerance. IEMbase adds several granular prompts not fully
represented locally, including nocturnal enteral nutrition, urinary galactitol,
urinary calcium, fed/fasted glucose contrast, hyperuricemia, cataract,
hyperfiltration/nephromegaly/renal failure, loose stools/malabsorption, and
hepatic tumor labels.

## Curation actions

- Treat this as covered by `Fanconi-Bickel_Syndrome.yaml`.
- Reject `SLC35A2-CDG.yaml` as a false-positive glycosylation neighbor.
- If importing IEMbase prompts, prioritize evidence review for nocturnal enteral
  nutrition, urinary galactitol/calcium, renal hyperfiltration/nephromegaly,
  cataract, loose stools/malabsorption, and hepatic tumor complications.
