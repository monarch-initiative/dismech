# IEMbase 0691: NDUFS6-related NADH dehydrogenase iron-sulfur protein 6 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 691 |
| Nosology | 7.1.09.02 |
| Nosology code | IEM0421 |
| Gene | NDUFS6 |
| External IDs | OMIM:618232; ORPHA:2609 |
| Generated mapping | CANDIDATE to `PET117-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFS6 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFS6-related NADH dehydrogenase
iron-sulfur protein 6 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 9.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate in neonatal, infancy, and childhood ages. Clinical rows include
failure to thrive and Leigh syndrome, with characteristic basal ganglia MRI
abnormalities, hypertrophic cardiomyopathy, hypotonia, lactic acidosis, and
severe multisystem disease.

## DisMech phenotype coverage

No exact NDUFS6 or MC1DN9 local target was identified.

`Leigh_Syndrome.yaml` overlaps broadly but is not a gene-specific NDUFS6 model.
The generated `PET117-Related_COX_Deficiency.yaml` candidate is a complex IV
assembly-factor disorder and should be rejected.

## Concordance and completeness

Judgement: true local gap.

The IEMbase row is a severe multisystem complex I deficiency with cardiomyopathy,
basal ganglia lesions, hypotonia, lactic acidosis, and failure to thrive. It is
not covered by a complex IV PET117 entry.

## Curation actions

- Add a dedicated NDUFS6/MC1DN9 target if curated.
- Reject PET117-related complex IV deficiency as exact coverage.
- Preserve decreased complex I activity, increased lactate, severe multisystem
  disease, basal ganglia MRI abnormalities, hypertrophic cardiomyopathy,
  hypotonia, lactic acidosis, failure to thrive, and Leigh syndrome.
