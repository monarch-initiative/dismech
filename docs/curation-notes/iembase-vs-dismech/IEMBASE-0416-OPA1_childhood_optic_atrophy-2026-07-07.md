# IEMbase 0416: OPA1-related childhood-onset optic atrophy type 1

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 416 |
| Nosology | 19.2.01.02 |
| Gene | OPA1 |
| External IDs | OMIM:165500; ORPHA:98673 |
| Generated mapping | UNMAPPED; low candidate `Autosomal_Dominant_Optic_Atrophy_Plus.yaml` |
| Candidate DisMech targets | Partial context in `Autosomal_Dominant_Optic_Atrophy_Plus.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents OPA1-related childhood-onset optic atrophy type 1, also
called juvenile optic atrophy. It records autosomal dominant inheritance and no
treatment rows. The phenotype is primarily ophthalmic: characteristic optic
atrophy, vision-loss onset, temporal optic nerve pallor, color vision deficit,
and scotomata, with nystagmus and strabismus as additional rows.

## DisMech phenotype coverage

Local `Autosomal_Dominant_Optic_Atrophy_Plus.yaml` captures the OPA1 mechanism,
retinal ganglion cell degeneration, progressive bilateral optic atrophy,
temporal disc pallor, dyschromatopsia, centrocecal scotoma, and visual loss
since childhood. It therefore provides strong mechanistic and phenotype context
for this record.

However, the local disease target is explicitly the syndromic OPA1 plus/DOA plus
entity, with extra-ocular sensorineural deafness, ataxia, neuropathy,
ophthalmoplegia, mitochondrial myopathy, and spastic paraplegia. IEMbase 416 is
the childhood/juvenile optic atrophy type 1 record without those plus features.

## Concordance and completeness

Judgement: partial context but not an exact mapping; pure OPA1 childhood-onset
optic atrophy remains a local gap or lump/split decision.

The core OPA1 optic neuropathy phenotypes are highly concordant, but the local
file's disease identity is a syndromic plus phenotype. Mapping IEMbase 416 to it
would overstate extra-ocular involvement unless the project intentionally
decides to use one OPA1-spectrum entry for both pure and plus presentations.

## Curation actions

- Treat `Autosomal_Dominant_Optic_Atrophy_Plus.yaml` as context for OPA1
  mechanism and optic atrophy phenotypes.
- Keep exact mapping pending a pure OPA1/ADOA childhood-onset optic atrophy
  target, or an explicit subtype structure inside the OPA1 spectrum entry.
- If curated, include autosomal dominant OPA1, childhood/juvenile onset, optic
  atrophy, temporal pallor, color vision deficit, scotomata, vision loss,
  nystagmus, and strabismus.
