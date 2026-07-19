# IEMbase 0113: CPOX-related coproporphyrinogen oxidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 113 |
| Nosology | 17.1.07.01 |
| Gene | CPOX |
| External IDs | OMIM:121300; ORPHA:79273 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Inherited_Porphyria.yaml#Hereditary Coproporphyria` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as CPOX-related coproporphyrinogen oxidase deficiency,
with alternate labels hereditary coproporphyria and HC. Treatability is marked
yes, but the cached JSON has no treatment rows.

The characteristic biochemical rows are increased urinary delta-ALA, increased
stool coproporphyrin III, increased urinary porphobilinogen, and markedly
increased total urinary porphyrins in adolescence and adulthood. Clinical rows
include psychotic behavior, blisters, red-brown fluorescent urine, coma,
constipation, depression, hyperesthesia, hypertension, motor neuropathy, nausea,
renal failure, seizures, tachycardia, and vomiting.

## DisMech phenotype coverage

`Inherited_Porphyria.yaml` includes a hereditary coproporphyria subtype anchored
to CPOX loss of function. The umbrella entry covers the shared acute hepatic
porphyria pattern: attacks with abdominal pain, vomiting, weakness,
neuropathy, urinary ALA and porphobilinogen, and cutaneous photosensitivity for
the cutaneous/overlap porphyrias.

The treatment section applies group-level acute hepatic porphyria management,
including trigger avoidance/supportive care, hemin or heme arginate, and
givosiran, but it is not tailored specifically to HCP.

## Concordance and completeness

Judgement: correct subtype-level mapping with incomplete HCP-specific
granularity.

The mapping is concordant for CPOX/HCP and for the acute hepatic porphyria
attack phenotype. DisMech provides a good mechanism scaffold and shared
treatment rationale. IEMbase is more specific for HCP biochemical
discrimination, especially stool coproporphyrin III, and it enumerates several
attack features not specifically called out for the subtype: blisters,
fluorescent urine, coma, hyperesthesia, renal failure, and depressive or
psychotic symptoms.

## Curation actions

- Keep the current target as `Inherited_Porphyria.yaml#Hereditary
  Coproporphyria`.
- Consider HCP-specific biochemical rows for stool coproporphyrin III and
  urinary total porphyrins.
- Review whether HCP should remain a subtype only or eventually get a
  standalone entry if subtype-specific phenotype/treatment evidence is expanded.
