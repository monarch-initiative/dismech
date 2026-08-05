# IEMbase 0112: HMBS-related porphobilinogen deaminase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 112 |
| Nosology | 17.1.04.01 |
| Gene | HMBS |
| External IDs | OMIM:176000; ORPHA:79276 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Acute_Intermittent_Porphyria.yaml`; secondary umbrella subtype in `Inherited_Porphyria.yaml#Acute Intermittent Porphyria` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as HMBS-related porphobilinogen deaminase deficiency,
with alternate labels acute intermittent porphyria, hydroxymethylbilane
synthase deficiency, and AIP. Treatability is marked yes.

The characteristic biochemical rows are markedly increased urinary
delta-ALA, increased urinary porphobilinogen, and markedly increased total
urinary porphyrins in adolescence and adulthood. Clinical rows include anxiety,
aggressive or psychotic behavior, coma, constipation, depression, hepatopathy,
hyperesthesia, hypertension, hepatocellular carcinoma or hepatoblastoma, motor
neuropathy, nausea, renal failure, seizures, tachycardia, and vomiting. Hemin
is listed as pharmacological treatment.

## DisMech phenotype coverage

`Acute_Intermittent_Porphyria.yaml` is the correct canonical target. It models
HMBS/PBGD deficiency in hepatocytes, triggered hepatic ALAS1 induction, and
hepatic ALA/PBG accumulation, with urinary and plasma ALA/PBG biochemical
markers. The local phenotype set covers abdominal pain, nausea/vomiting,
constipation, tachycardia, hypertension, peripheral neuropathy, muscle
weakness, tetraparesis, hyponatremia, seizure, psychosis, mental deterioration,
cranial nerve paralysis, and pain manifestations.

The local treatment section is richer than IEMbase: intravenous hemin,
givosiran, prophylactic hemin, ovulation suppression, liver transplantation, and
carbohydrate loading are all represented with mechanism links.

## Concordance and completeness

Judgement: correct standalone mapping with high phenotype concordance.

The strongest overlap is acute hepatic precursor biochemistry, autonomic
features, gastrointestinal attacks, neuropathy, seizure/psychosis, and hemin
therapy. DisMech is much stronger for causal mechanism, plasma monitoring, and
modern prophylactic/curative treatment options. IEMbase contributes a few
review targets that are less explicit in the phenotype table, especially renal
failure, hepatopathy, liver-cancer risk, hyperesthesia, coma, anxiety, and
depression.

## Curation actions

- Keep `Acute_Intermittent_Porphyria.yaml` as the canonical target.
- Treat the inherited porphyria umbrella subtype as secondary classification
  context, not the main target.
- Review whether chronic kidney disease/renal failure, liver-cancer risk, and
  broader neuropsychiatric rows should be added or surfaced more explicitly in
  the standalone AIP entry.
