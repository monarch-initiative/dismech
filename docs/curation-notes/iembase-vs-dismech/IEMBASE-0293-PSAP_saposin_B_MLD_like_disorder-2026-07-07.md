# IEMbase 0293: PSAP-related Metachromatic leukodystrophy-like disorder due to saposin B deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 293 |
| Nosology | 20.1.11.01 |
| Gene | PSAP |
| External IDs | OMIM:249900; ORPHA:309263 |
| Generated mapping | CANDIDATE; `Gaucher_Disease_Due_To_Saposin_C_Deficiency.yaml` |
| Candidate DisMech targets | `Gaucher_Disease_Due_To_Saposin_C_Deficiency.yaml`; partial context in `Metachromatic_Leukodystrophy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents isolated saposin B deficiency / cerebroside sulfatase
activator deficiency, a PSAP-domain disorder producing a
metachromatic-leukodystrophy-like phenotype. Inheritance is autosomal recessive
and treatability is unknown.

The phenotype rows resemble MLD: ataxia, dysarthria, leukodystrophy, muscle
weakness, neuropathy, seizures, slow nerve conduction velocity, spasticity,
gait disturbance, irritability, emotional lability, psychotic behavior, and
neurologic deterioration. Biochemical rows show increased CSF protein and
markedly increased urinary sulfatide.

## DisMech phenotype coverage

The generated saposin C candidate is not the correct target. Saposin C
deficiency is a Gaucher-like glucosylceramide cofactor disorder, while this
record is a saposin B sulfatide/MLD-like disorder.

`Metachromatic_Leukodystrophy.yaml` provides the closest local phenotype and
biochemical context. It covers leukodystrophy, peripheral demyelination, motor
and neurologic regression, seizures, sulfatide accumulation, and urinary
sulfatide excretion. The local biochemical section explicitly notes that
urinary sulfatide excretion can confirm MLD whether caused by ARSA defects or
saposin B.

However, the local MLD entry is genetically and mechanistically centered on
ARSA. It does not yet model PSAP/saposin B as a causal gene or as an isolated
activator-defect subtype/entry.

## Concordance and completeness

Judgement: reject the generated saposin C candidate; treat as partial local MLD
context plus a missing saposin B-specific target.

IEMbase and local MLD coverage agree on the leukodystrophy, peripheral nerve,
spasticity, seizure, gait, behavioral, and urinary sulfatide signal. The
critical discordance is the proximal mechanism: IEMbase is PSAP/saposin B,
whereas the local entry primarily represents ARSA deficiency. That makes this a
false-positive candidate to saposin C and a partial false negative for a
saposin B-specific DisMech entity.

IEMbase adds a focused checklist for any future saposin B curation: PSAP gene
causality, sulfatide excretion, elevated CSF protein, psychiatric/behavioral
features, dysarthria, gait disturbance, and slow nerve conduction.

## Curation actions

- Do not map this record to `Gaucher_Disease_Due_To_Saposin_C_Deficiency.yaml`.
- Use `Metachromatic_Leukodystrophy.yaml` only as partial phenotype/biochemical
  context until a saposin B-specific entry or subtype is curated.
- Consider a future PSAP/saposin B MLD-like disorder entry that preserves the
  activator-defect distinction from ARSA-deficient MLD.
