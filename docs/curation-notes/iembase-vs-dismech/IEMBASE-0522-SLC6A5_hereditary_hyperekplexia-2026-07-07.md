# IEMbase 0522: SLC6A5-related glycine transporter 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 522 |
| Nosology | 17.4.02.03 |
| Gene | SLC6A5 |
| External IDs | OMIM:149400; ORPHA:3197 |
| Generated mapping | MAPPED; `Hereditary_Hyperekplexia.yaml` |
| Candidate DisMech targets | `Hereditary_Hyperekplexia.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as SLC6A5-related glycine transporter 2 deficiency, with
alternate labels hereditary hyperekplexia type 3, familial startle disease,
stiff-baby syndrome, and HE. No biochemical rows or treatment rows are listed.

Clinical-characteristic rows include increased head-retraction reflex, startle
reflex, and stiffness. Additional clinical rows include optional hernias, hip
dislocation, intellectual disability, periodic limb movement during sleep, and
sudden infant death.

## DisMech phenotype coverage

`Hereditary_Hyperekplexia.yaml` is the correct target. The local entry models
inhibitory glycinergic neurotransmission failure and explicitly includes SLC6A5
as the presynaptic glycine transporter GlyT2 branch. It covers SLC6A5 variants,
defective GlyT2 localization or glycine uptake, exaggerated startle, hypertonia
or stiffness, neonatal apnea, developmental delay/intellectual disability
context, and the broader GLRA1/GLRB/GPHN/ATAD1 hyperekplexia spectrum.

## Concordance and completeness

Judgement: correct mapping with high concordance.

IEMbase and DisMech agree on SLC6A5/GlyT2 identity and the core startle/stiffness
phenotype. DisMech is richer for glycinergic synapse pathophysiology and broader
gene-spectrum context. IEMbase adds practical phenotype prompts for
head-retraction reflex, hernias, hip dislocation, periodic limb movement during
sleep, and sudden infant death.

## Curation actions

- Keep this record mapped to `Hereditary_Hyperekplexia.yaml`.
- Consider whether head-retraction reflex, periodic limb movements, hernias, hip
  dislocation, and sudden infant death should be reviewed as future enrichment
  prompts for the hyperekplexia entry.
- Preserve the SLC6A5/GlyT2 subtype language when importing aliases.
