# IEMbase 0147: PRPS1-related phosphoribosyl pyrophosphate synthetase 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 147 |
| Nosology | 16.2.02.01 |
| Gene | PRPS1 |
| External IDs | OMIM:311850; ORPHA:1187 |
| Generated mapping | MAPPED to `Arts_syndrome.yaml` |
| Candidate DisMech targets | `Arts_syndrome.yaml`; broader context in `PRPS1_Deficiency_Spectrum.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as PRPS1-related phosphoribosyl pyrophosphate synthetase
1 deficiency, with alternate labels X-linked Charcot-Marie-Tooth disease 5 and
Arts syndrome. Treatability is marked unknown.

The biochemical row is decreased phosphoribosyl pyrophosphate synthetase
activity across age ranges. Clinical rows include psychomotor retardation,
tetraplegia, ataxia, sensorineural deafness or hearing loss, hypotonia,
intellectual disability, peripheral neuropathy, optic atrophy, recurrent
infections, and progressive vision loss.

## DisMech phenotype coverage

`Arts_syndrome.yaml` is an exact MONDO/Orphanet leaf match for the severe PRPS1
deficiency presentation. It models PRPS1 loss of function, reduced PRS-I enzyme
activity, impaired purine/nucleotide biosynthesis, sensorineural hearing
impairment, ataxia, hypotonia, optic atrophy, recurrent infections, and related
supportive and precursor-supplementation care.

`PRPS1_Deficiency_Spectrum.yaml` is the broader local entry for the PRPS1
deficiency continuum. It explicitly covers Arts syndrome, CMTX5, and
DFN2/DFNX1, which better matches IEMbase's broad alternate-label scope.

## Concordance and completeness

Judgement: generated mapping is valid for the ORPHA leaf, but the broader
PRPS1 spectrum should remain secondary context.

The generated Arts syndrome mapping is acceptable because IEMbase's ORPHA code
and severe clinical rows point to Arts syndrome. However, IEMbase also names
X-linked CMT5, so future crosswalk work should avoid losing the broader PRPS1
deficiency continuum represented locally in `PRPS1_Deficiency_Spectrum.yaml`.

## Curation actions

- Keep `Arts_syndrome.yaml` as the exact disease-leaf target for ORPHA:1187.
- Record `PRPS1_Deficiency_Spectrum.yaml` as important broader context when
  subtype-aware mapping becomes available.
- No new standalone disease gap is present for the core PRPS1 deficiency
  phenotype signal.
