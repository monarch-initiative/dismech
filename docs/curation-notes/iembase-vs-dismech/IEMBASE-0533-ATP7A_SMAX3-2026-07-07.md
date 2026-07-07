# IEMbase 0533: ATP7A-related distal spinal muscular atrophy type 3

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 533 |
| Nosology | 22.1.03.01 |
| Gene | ATP7A |
| External IDs | OMIM:300489; ORPHA:404538 |
| Generated mapping | UNMAPPED; best candidate `Menkes_Disease.yaml` |
| Candidate DisMech targets | `Menkes_Disease.yaml#ATP7A-related distal motor neuropathy` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ATP7A-related copper-transporting ATPase subunit alpha
deficiency with the SMAX3 label. Alternate labels are X-linked distal spinal
muscular atrophy and SMAX3. The record is X-linked, subtype is marked
idiopathic, and no treatments are listed.

The IEMbase signal is narrow and motor-neuron predominant: normal serum copper,
distal muscle weakness, weak or absent tendon reflexes, and possible optic nerve
pallor. It does not present the severe infantile Menkes copper-deficiency
phenotype.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative if reviewed at the ATP7A
spectrum level. `Menkes_Disease.yaml` models ATP7A-related copper transport
disorders and explicitly includes ATP7A-related distal motor neuropathy /
X-linked distal spinal muscular atrophy type 3 as the mildest allelic variant.
The local subtype description distinguishes this from classic Menkes disease by
residual copper transport, adult-onset or milder distal motor weakness, and
little or no copper-deficiency biochemical pattern.

## Concordance and completeness

Judgement: false negative; resolve to the ATP7A-related distal motor neuropathy
subtype within `Menkes_Disease.yaml`.

IEMbase and DisMech agree on ATP7A, X-linked inheritance, SMAX3/X-linked distal
spinal muscular atrophy type 3 identity, and distal motor weakness. IEMbase adds
explicit normal serum copper, weak/absent reflexes, and optic nerve pallor rows
that should not be overwritten by classic Menkes assumptions.

## Curation actions

- Map this record to `Menkes_Disease.yaml#ATP7A-related distal motor neuropathy`.
- Keep the note scoped to SMAX3 and do not treat it as classic infantile Menkes
  disease.
- Preserve normal serum copper, distal weakness, reflex, and optic nerve pallor
  prompts for subtype-specific review.
