# IEMbase 0292: PSAP-related Krabbe disease-like disorder due to saposin A deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 292 |
| Nosology | 20.1.09.01 |
| Gene | PSAP |
| External IDs | OMIM:611722; ORPHA:309263 |
| Generated mapping | MAPPED; `Krabbe_Disease_Due_To_Saposin_A_Deficiency.yaml` |
| Candidate DisMech targets | `Krabbe_Disease_Due_To_Saposin_A_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents isolated saposin A deficiency, a PSAP-domain disorder with a
Krabbe-like phenotype rather than primary GALC deficiency. Inheritance is
autosomal recessive and treatability is unknown.

The clinical signal is neurologic and leukodystrophy-centered: blindness,
deafness, fever, leukodystrophy, neurologic deterioration, seizures, slow nerve
conduction velocity, spasticity, ataxia, feeding difficulties, irritability, and
neuropathy. Biochemical rows add increased CSF protein, especially in infancy,
and increased serum lysogalactosylceramide.

## DisMech phenotype coverage

`Krabbe_Disease_Due_To_Saposin_A_Deficiency.yaml` is the correct local target.
The local entry explicitly models PSAP variants affecting the saposin A domain,
loss of the galactosylceramidase activator cofactor, galactosylceramide
accumulation, demyelination, autophagic-lysosomal dysfunction, and the
Krabbe-like distinction from GALC-deficient Krabbe disease.

Local phenotypes include progressive encephalopathy, leukodystrophy, seizures,
hypertonia/spasticity, and peripheral neuropathy. Local diagnosis also captures
the key activator-defect clue: a Krabbe-like phenotype with discordant
galactocerebrosidase assay behavior and confirmatory PSAP sequencing.

## Concordance and completeness

Judgement: correct high-concordance mapping to
`Krabbe_Disease_Due_To_Saposin_A_Deficiency.yaml`.

IEMbase and DisMech agree on the disease identity, PSAP/saposin A mechanism,
recessive inheritance, Krabbe-like leukodystrophy, seizures, spasticity or
hypertonia, and peripheral neuropathy. DisMech is stronger for mechanistic
framing, especially the cofactor-versus-enzyme distinction and the diagnostic
assay pattern.

IEMbase adds useful phenotype prompts not yet explicit locally: blindness,
deafness, fever, feeding difficulties, irritability, ataxia, increased CSF
protein, and serum lysogalactosylceramide. These should be reviewed against the
sparse case literature before import because the disease is very rare and rows
may reflect Krabbe-like syndrome-level expectations.

## Curation actions

- Keep this record mapped to `Krabbe_Disease_Due_To_Saposin_A_Deficiency.yaml`.
- Consider adding IEMbase-only sensory, fever, feeding, irritability, ataxia,
  CSF-protein, and lysogalactosylceramide prompts after evidence review.
- Preserve the saposin A activator-defect distinction from GALC-deficient
  `Krabbe_Disease.yaml`.
