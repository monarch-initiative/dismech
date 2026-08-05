# IEMbase 0012: NAGS-related N-acetylglutamate synthase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 12 |
| Nosology | 1.1.01.01 |
| Gene | NAGS |
| External IDs | OMIM:237310 |
| Generated mapping | AMBIGUOUS by `alias_exact:n acetylglutamate synthase deficiency` |
| Candidate DisMech targets | `N-Acetylglutamate_Synthase_Deficiency.yaml`; `Urea_Cycle_Disorder.yaml#N-Acetylglutamate Synthase Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

Characteristic clinical features are coma, developmental delay, encephalopathy,
and vomiting, again with stronger neonatal/infantile acute-decompensation
signal. Additional features include failure to thrive, feeding
difficulty/protein aversion, seizures, and neonatal temperature instability.

The biochemical profile includes high ammonia, increased plasma and CSF
glutamine, low arginine, very low citrulline, normal argininosuccinic acid, and
low/normal urinary orotic acid.

Treatments include protein-defined diet, arginine or citrulline,
nitrogen-scavenger drugs, carglumic acid, hemodialysis, peritoneal dialysis, and
liver transplantation.

## DisMech phenotype coverage

The standalone DisMech disease is the best curation target. It covers
hyperammonemia, encephalopathy, vomiting, lethargy, seizures, intellectual
disability, failure to thrive, headache, cerebral edema, coma, and respiratory
alkalosis. Biochemical entries cover plasma ammonia, plasma glutamine, plasma
citrulline, urine orotic acid, and N-acetylglutamate. Treatments include
carglumic acid, dietary protein management, nitrogen scavengers, extracorporeal
ammonia removal, acute-crisis supportive care, citrulline/arginine, genetic
counseling, and a carbamylglutamate therapeutic trial.

The `Urea Cycle Disorder` umbrella subtype causes the exact-alias ambiguity.

## Concordance and completeness

Judgement: phenotype concordance is high, but mapping should prefer the
standalone disease over the umbrella subtype for disease-level crosswalks.

IEMbase adds feeding difficulty/protein aversion and neonatal temperature
instability. DisMech adds headache, cerebral edema, respiratory alkalosis, NAG
biochemistry, and explicit carglumic-acid therapeutic testing.

## Curation actions

- Resolve crosswalk ambiguity by treating `N-Acetylglutamate_Synthase_Deficiency.yaml`
  as the canonical target.
- Consider adding feeding difficulty/protein aversion if supported by evidence.
- Consider whether peritoneal dialysis needs explicit mention or is adequately
  covered by extracorporeal ammonia removal.
