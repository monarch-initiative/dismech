# IEMbase 0657: ALDH3A2-related fatty aldehyde dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 657 |
| Nosology | 14.1.01.01 |
| Nosology code | IEM0651 |
| Gene | ALDH3A2 |
| External IDs | OMIM:270200; ORPHA:816 |
| Generated mapping | UNMAPPED; weak candidate `Sjogrens_Syndrome.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive ALDH3A2-related fatty aldehyde
dehydrogenase deficiency, also labeled Sjogren-Larsson syndrome, ichthyosis,
spastic neurologic disorder and oligophrenia.

Biochemical rows include decreased fibroblast aldehyde dehydrogenase activity.
Clinical rows include childhood spastic paraparesis/paraplegia/tetraplegia,
infantile-to-childhood ichthyosis, childhood intellectual disability,
infantile-to-childhood leukoencephalopathy, and infantile-to-childhood macular
degeneration.

## DisMech phenotype coverage

`Sjogrens_Syndrome.yaml` is a name-collision false candidate. It models primary
Sjogren disease, a systemic autoimmune exocrinopathy with lymphocytic gland
infiltration, sicca symptoms, interferon/JAK-STAT immune biology, and lymphoma
risk. It does not model ALDH3A2, fatty aldehyde dehydrogenase deficiency,
ichthyosis, spastic diplegia/tetraplegia, leukoencephalopathy, or retinal
crystalline/macular disease.

Targeted search did not find a local Sjogren-Larsson syndrome, ALDH3A2, or
fatty aldehyde dehydrogenase deficiency entry.

## Concordance and completeness

Judgement: true local ALDH3A2 / Sjogren-Larsson syndrome gap; reject Sjogren
autoimmune disease as exact.

The generated candidate is a lexical eponym collision. It should not be used
for coverage because the biology, gene, inheritance, and phenotype package are
unrelated.

## Curation actions

- Keep this row unmapped until an ALDH3A2 / Sjogren-Larsson syndrome target
  exists.
- Do not map to `Sjogrens_Syndrome.yaml`.
- Preserve decreased fibroblast aldehyde dehydrogenase, ichthyosis, spastic
  paraparesis/paraplegia/tetraplegia, intellectual disability,
  leukoencephalopathy, and macular-degeneration prompts.
