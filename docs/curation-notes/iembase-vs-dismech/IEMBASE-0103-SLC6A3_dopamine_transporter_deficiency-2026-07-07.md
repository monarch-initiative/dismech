# IEMbase 0103: SLC6A3-related dopamine transporter deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 103 |
| Nosology | 23.1.05.01 |
| Gene | SLC6A3 |
| External IDs | OMIM:613135; OMIM:126455 |
| Generated mapping | MAPPED |
| Candidate DisMech targets | `Infantile_Parkinsonism-Dystonia.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as SLC6A3-related dopamine transporter deficiency, with
alternate labels infantile parkinsonism-dystonia and DAT. Treatability is marked
unknown and the cached JSON has no treatment rows.

The characteristic biochemical rows are increased CSF HVA/5-HIAA ratio,
increased CSF homovanillic acid, and increased urinary homovanillic acid. The
clinical rows are bulbar dysfunction, dyskinesia, dystonia, ocular flutter, and
parkinsonism with hypokinetic features.

## DisMech phenotype coverage

The generated mapping to `Infantile_Parkinsonism-Dystonia.yaml` is correct. The
local entry describes dopamine transporter deficiency syndrome caused by
biallelic SLC6A3 loss of function, impaired dopamine reuptake, dysregulated
synaptic dopamine homeostasis, raised CSF HVA:5-HIAA ratio, and progressive
nigrostriatal dysfunction.

Phenotype coverage includes parkinsonism-dystonia, dystonia, bradykinesia,
rigidity, tremor, early hyperkinetic movement disorder, oculogyric crisis, axial
hypotonia, delayed motor development, feeding difficulties, irritability, and
decreased facial expression. Treatment coverage is broader than IEMbase:
supportive care, tetrabenazine, benzodiazepines, dopamine agonists, physical
therapy, and a note that levodopa is generally ineffective.

## Concordance and completeness

Judgement: correct high-confidence mapping with high concordance.

IEMbase is more compact and emphasizes the diagnostic HVA/HVA:5-HIAA pattern
and the bulbar/ocular-flutter rows. DisMech is richer for disease mechanism,
progressive motor phenotype, treatment nuance, and the reason dopaminergic
replacement is not analogous to synthesis-defect disorders.

## Curation actions

- Keep `Infantile_Parkinsonism-Dystonia.yaml` as the canonical target.
- Consider adding urinary HVA and bulbar dysfunction or ocular flutter as review
  targets if the SLC6A3 entry is expanded.
- No mapping correction needed.
