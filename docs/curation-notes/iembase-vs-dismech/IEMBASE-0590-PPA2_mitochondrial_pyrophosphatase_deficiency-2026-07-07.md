# IEMbase 0590: PPA2-related mitochondrial inorganic pyrophosphatase 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 590 |
| Nosology | 11.4.01.01 |
| Gene | PPA2 |
| External IDs | OMIM:617222 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Dilated_Cardiomyopathy.yaml#PPA2` (partial) |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PPA2-related mitochondrial inorganic pyrophosphatase 2
deficiency, with alternate label infantile sudden cardiac failure / SCFI. The
record is autosomal recessive, classified under miscellaneous disorders
associated with mitochondrial dysfunction, has unknown treatability, and has no
treatment rows.

Biochemical rows include increased plasma lactate. Clinical rows include
seizures, cardiac arrhythmia, lactic acidosis, and sudden death.

## DisMech phenotype coverage

No generated DisMech target was proposed. `Dilated_Cardiomyopathy.yaml` contains
PPA2 as an autosomal recessive dilated-cardiomyopathy gene with ClinGen support
and includes a mitochondrial dysfunction node that names PPA2. That is real
gene-level and cardiac-disease-class coverage, but it is not an exact model of
PPA2 mitochondrial inorganic pyrophosphatase deficiency / infantile sudden
cardiac failure.

The local entry does not yet represent the IEMbase-specific acute infantile
presentation, lactic-acidosis signal, seizures, arrhythmia, or sudden-death
phenotype as a PPA2-centered disease mechanism.

## Concordance and completeness

Judgement: generated false negative for partial local coverage, but exact
PPA2 deficiency remains a local gap.

DisMech and IEMbase agree that PPA2 is relevant to recessive cardiac disease,
but the local coverage is embedded in broad dilated cardiomyopathy. The IEMbase
record is more specific: a mitochondrial pyrophosphatase defect with infantile
sudden cardiac failure and metabolic-decompensation features.

## Curation actions

- Use `Dilated_Cardiomyopathy.yaml#PPA2` as partial context only.
- Create or identify an exact PPA2 mitochondrial pyrophosphatase deficiency /
  infantile sudden cardiac failure target before import, or add a clearly
  scoped PPA2 subtype if that matches project modeling decisions.
- Preserve increased lactate, lactic acidosis, seizures, cardiac arrhythmia,
  and sudden death as PPA2-specific review prompts.
