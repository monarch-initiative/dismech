# IEMbase 0287: GM2A-related GM2 activator protein deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 287 |
| Nosology | 20.1.07.01 |
| Gene | GM2A |
| External IDs | OMIM:272750; ORPHA:309246 |
| Generated mapping | MAPPED; `Tay-Sachs_Disease_AB_Variant.yaml` |
| Candidate DisMech targets | `Tay-Sachs_Disease_AB_Variant.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GM2 gangliosidosis AB variant / hexosaminidase activator
deficiency due to GM2A. Inheritance is autosomal recessive and treatability is
unknown.

The clinical rows are sparse but neurologically focused: muscular hypotonia,
psychiatric disturbances, spasticity, and urinary incontinence. Biochemical
rows list normal-to-increased beta-hexosaminidase A activity and increased
urinary oligosaccharides, consistent with a cofactor defect rather than a
primary HEXA or HEXB catalytic-subunit deficiency.

## DisMech phenotype coverage

`Tay-Sachs_Disease_AB_Variant.yaml` is the correct local target. The DisMech
entry models GM2A loss, absence of the GM2 activator protein, preserved
hexosaminidase A and B catalytic activity, failure of GM2 presentation to
hexosaminidase A, and neuronal GM2 storage.

Local phenotypes include developmental regression, cherry-red spot of the
macula, neurodegeneration, nystagmus, hypotonia, and hyperacusis. Local
treatment coverage is supportive care. Genetic coverage correctly uses GM2A.

## Concordance and completeness

Judgement: correct mapping to `Tay-Sachs_Disease_AB_Variant.yaml`.

IEMbase and DisMech agree on GM2A identity, autosomal recessive inheritance, a
GM2 activator/cofactor defect, hypotonia, and the important distinction from
HEXA/HEXB disease: beta-hexosaminidase catalytic activity is not the primary
defect. DisMech is stronger for mechanism and classic neuro-ophthalmic
phenotypes. IEMbase is thinner overall but adds spasticity, urinary
incontinence, psychiatric disturbance, and urinary oligosaccharide rows as
review prompts.

The normal-to-increased beta-hexosaminidase A row is especially useful because
it helps distinguish AB variant disease from classic Tay-Sachs, where Hex A
activity is decreased.

## Curation actions

- Keep this record mapped to `Tay-Sachs_Disease_AB_Variant.yaml`.
- Consider adding an explicit biochemical/diagnostic row for preserved Hex A/B
  catalytic activity if supported by local evidence sources.
- Review spasticity, urinary incontinence, psychiatric disturbance, and urinary
  oligosaccharides before importing them locally.
