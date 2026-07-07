# IEMbase 0550: SLC33A1-related acetyl-CoA transporter deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 550 |
| Nosology | 22.1.05.01 |
| Gene | SLC33A1 |
| External IDs | OMIM:614482; ORPHA:300313 |
| Generated mapping | MAPPED; `Huppke-Brendel_syndrome.yaml` |
| Candidate DisMech targets | `Huppke-Brendel_syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SLC33A1-related acetyl-CoA transporter deficiency, with
alternate labels congenital cataracts, hearing loss, low serum copper and
ceruloplasmin, Huppke-Brendel syndrome, and CCHLND. The record is autosomal
recessive, and treatability is unknown. No treatment rows are listed.

The biochemical signal is decreased serum ceruloplasmin and decreased serum
copper. Clinical rows include congenital cataract, hearing loss, hypomyelination
on MRI, axial muscular hypotonia, cerebellar atrophy, and cerebral atrophy.

## DisMech phenotype coverage

`Huppke-Brendel_syndrome.yaml` is the correct local target. The local entry
models biallelic SLC33A1 variants causing AT-1 acetyl-CoA transporter
deficiency in the endoplasmic reticulum, defective secretory-pathway
acetylation, reduced ceruloplasmin secretion, secondary low serum copper, and a
severe neurodevelopmental syndrome with congenital cataracts, hearing loss,
developmental delay, cerebellar hypoplasia, and hypomyelination.

The local file also distinguishes the low copper/ceruloplasmin pattern from
primary copper deficiency and Wilson disease mimicry.

## Concordance and completeness

Judgement: correct high-concordance mapping to
`Huppke-Brendel_syndrome.yaml`.

IEMbase and DisMech agree on SLC33A1 identity, recessive inheritance, AT-1 /
acetyl-CoA transporter scope, low serum copper, low ceruloplasmin, congenital
cataracts, hearing loss, hypomyelination, and hypotonia. DisMech is stronger
for the secretory-pathway acetylation and ceruloplasmin-secretion mechanism.

IEMbase adds compact age-patterned prompts for cerebellar and cerebral atrophy
and specifies axial muscular hypotonia.

## Curation actions

- Keep this record mapped to `Huppke-Brendel_syndrome.yaml`.
- Consider adding the IEMbase cerebral/cerebellar atrophy and axial-hypotonia
  wording if supported by existing evidence.
- Preserve low serum copper as secondary to low ceruloplasmin, not as primary
  copper deficiency.
