# IEMbase 0421: OPA1-related optic atrophy 1 and deafness

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 421 |
| Nosology | 19.2.01.03 |
| Gene | OPA1 |
| External IDs | OMIM:125250; ORPHA:98673 |
| Generated mapping | UNMAPPED; low candidate `Autosomal_Dominant_Optic_Atrophy_Plus.yaml` |
| Candidate DisMech targets | `Autosomal_Dominant_Optic_Atrophy_Plus.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents OPA1-related optic atrophy 1 and deafness, with Behr syndrome
listed as an alternate name. Inheritance is recorded as autosomal dominant and
autosomal recessive. The characteristic clinical signal includes hearing loss,
temporal optic nerve pallor, vision-loss onset, and ophthalmoplegia. Additional
rows include ataxia, areflexia/hyperreflexia, developmental delay, diabetes,
dysmotility, foot deformities, glaucoma, hypothyroidism, migraine, myopathy,
neuropathy, ptosis, scotomata, spasticity, basal-ganglia calcifications, brain
atrophy, cerebellar atrophy, cortical atrophy, and white-matter lesions. Lactate
is low-normal to increased.

## DisMech phenotype coverage

The generated unmapped status is a false negative for practical coverage. Local
`Autosomal_Dominant_Optic_Atrophy_Plus.yaml` models OPA1 plus disease with OPA1
loss/dominant-negative dysfunction, impaired mitochondrial fusion and mtDNA
instability, retinal ganglion cell degeneration, optic atrophy, sensorineural
hearing loss, progressive external ophthalmoplegia, peripheral neuropathy,
ataxia, mitochondrial myopathy, spastic paraplegia, dyschromatopsia, and
centrocecal scotoma.

Local DisMech is stronger for OPA1 mitochondrial-dynamics mechanism and the
plus-syndrome causal path. IEMbase adds a broader Behr/optic-atrophy-with-deafness
phenotype checklist, including endocrine, brain-imaging, and dysmotility rows,
and it explicitly records possible recessive inheritance.

## Concordance and completeness

Judgement: resolve to `Autosomal_Dominant_Optic_Atrophy_Plus.yaml` as the best
local target, with inheritance/subtype caveats.

The core disease identity is concordant: OPA1 optic atrophy with deafness and
multisystem mitochondrial plus features. The local target may need subtype or
scope refinement to represent Behr/recessive OPA1 presentations cleanly.

## Curation actions

- Map this record to `Autosomal_Dominant_Optic_Atrophy_Plus.yaml`.
- Review whether the local OPA1 entry should add a Behr/optic-atrophy-with-deafness
  subtype or recessive inheritance branch.
- Consider adding IEMbase's endocrine, dysmotility, imaging, lactate, ptosis,
  scotomata, and foot-deformity prompts after source verification.
