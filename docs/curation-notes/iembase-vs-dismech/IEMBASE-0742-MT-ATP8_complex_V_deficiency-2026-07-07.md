# IEMbase 0742: MT-ATP8-related mitochondrial ATP synthase subunit 8 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 742 |
| Nosology | 6.1.05.01 |
| Nosology code | IEM0485 |
| Gene | MT-ATP8 |
| External IDs | OMIM:516070; ORPHA:397750 |
| Generated mapping | UNMAPPED; weak candidate `3-Hydroxy-3-Methylglutaryl-CoA_Synthase_Deficiency.yaml` |
| Candidate DisMech targets | `NARP_syndrome.yaml` has partial MT-ATP6/8 context; no exact MT-ATP8 target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents mitochondrial MT-ATP8-related ATP synthase F0 subunit 8
deficiency. The cached rows point to adolescent neurologic disease with
increased CSF lactate but normal plasma lactate, adolescent ataxia, dysarthria,
hyporeflexia, learning disability, ophthalmoplegia, polyneuropathy, childhood
exercise intolerance, childhood muscle weakness, childhood vision loss/optic
atrophy, and adolescent hypertrophic cardiomyopathy.

## DisMech phenotype coverage

No exact MT-ATP8 local target was identified.

`NARP_syndrome.yaml` is relevant context because it includes MT-ATP6/8 complex V
biology and cites MT-ATP8 as a less frequent mitochondrial disease gene in the
ATP synthase spectrum. However, the file is centered on MT-ATP6/NARP and does
not model a standalone MT-ATP8 disease. The generated
`3-Hydroxy-3-Methylglutaryl-CoA_Synthase_Deficiency.yaml` candidate is a false
positive and has no disease-identity relationship to ATP synthase subunit 8.

## Concordance and completeness

Judgement: true MT-ATP8 complex V local gap, with partial MT-ATP6/8 context in
`NARP_syndrome.yaml`.

IEMbase supplies a useful phenotype seed for future MT-ATP8 curation:
CSF/plasma lactate discordance, ataxia, dysarthria, exercise intolerance,
hyporeflexia, learning disability, ophthalmoplegia, polyneuropathy, vision
loss/optic atrophy, muscle weakness, and hypertrophic cardiomyopathy.

## Curation actions

- Add a dedicated MT-ATP8 ATP synthase subunit 8 deficiency target if curated.
- Treat `NARP_syndrome.yaml` as context only, not exact coverage.
- Reject `3-Hydroxy-3-Methylglutaryl-CoA_Synthase_Deficiency.yaml` as exact
  coverage.
- Preserve adolescent neurologic, visual, peripheral nerve, cardiomyopathy, and
  lactate prompts.
