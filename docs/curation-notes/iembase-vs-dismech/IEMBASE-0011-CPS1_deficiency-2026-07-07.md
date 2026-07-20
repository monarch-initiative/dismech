# IEMbase 0011: CPS1-related carbamoyl phosphate synthetase I deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 11 |
| Nosology | 1.1.02.01 |
| Gene | CPS1 |
| External IDs | OMIM:237300 |
| Generated mapping | AMBIGUOUS by `alias_exact:carbamoyl phosphate synthetase i deficiency` |
| Candidate DisMech targets | `Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml`; `Urea_Cycle_Disorder.yaml#Carbamoyl Phosphate Synthetase I Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

Characteristic clinical features are coma, developmental delay, encephalopathy,
and vomiting, with stronger neonatal/infantile intensity for acute
decompensation. Additional features include failure to thrive, feeding
difficulty/protein aversion, seizures, and neonatal temperature instability.

The biochemical profile is urea-cycle proximal: increased ammonia, increased
glutamine, low arginine, very low citrulline, normal argininosuccinic acid, and
low/normal urinary orotic acid. IEMbase also lists mild/variable urinary
3-methylglutaconic acid.

Treatments include protein-defined diet, arginine or citrulline,
nitrogen-scavenger drugs, carglumic acid, hemodialysis, peritoneal dialysis, and
liver transplantation.

## DisMech phenotype coverage

The standalone DisMech disease is the best curation target. It captures
hyperammonemia, episodic ammonia intoxication, respiratory insufficiency,
aminoaciduria, hypoargininemia, encephalopathy, seizures, coma, developmental
delay, intellectual disability, hypotonia, vomiting, lethargy, microcephaly,
cerebral edema, abnormal white matter, and atypical behavior. Biochemical
entries cover plasma ammonia, citrulline, glutamine, urinary orotic acid, and
alanine. Treatments cover diet, nitrogen scavengers, citrulline/arginine,
carglumic acid, dialysis, liver transplantation, and genetic counseling.

The `Urea Cycle Disorder` umbrella also includes a subtype with the same name,
which explains the generated ambiguous match.

## Concordance and completeness

Judgement: phenotype concordance is high, but mapping should prefer the
standalone disease over the umbrella subtype for one-to-one IEMbase crosswalks.

IEMbase adds feeding difficulty/protein aversion and neonatal temperature
instability, which are not explicit in the standalone DisMech entry. DisMech adds
respiratory insufficiency, hypotonia, lethargy, microcephaly, cerebral edema,
white matter abnormalities, and broader neurologic sequelae.

## Curation actions

- Resolve crosswalk ambiguity by treating `Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml`
  as the canonical target.
- Consider whether umbrella subtype aliases should be de-prioritized in
  generated exact-alias mapping.
- Consider adding feeding difficulty/protein aversion if supported by evidence.
