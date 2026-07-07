# IEMbase 0067: HIBADH-related 3-hydroxyisobutyrate dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 67 |
| Nosology | 1.2.25.01 |
| Gene | HIBADH |
| External IDs | OMIM:608475 |
| Generated mapping | CANDIDATE by `fuzzy_alias` |
| Candidate DisMech targets | `Succinic_Semialdehyde_Dehydrogenase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive HIBADH-related
3-hydroxyisobutyrate dehydrogenase deficiency, also labeled
3-hydroxyisobutyric aciduria. Treatability is marked unknown.

The characteristic biochemical signal is high urinary 3-hydroxyisobutyric acid,
high urinary 2-hydroxyisovaleric acid, high C4-OH
3-hydroxyisobutyrylcarnitine in dried blood spot or plasma, and low fibroblast
3-hydroxyisobutyrate dehydrogenase activity. IEMbase also lists free and
esterified carnitine and plasma lactate as ancillary rows.

The clinical signal includes failure to thrive and ketoacidosis as
characteristic rows, with developmental delay, metabolic acidosis, focal white
matter lesions, white-matter MRI changes, intracerebral calcification,
microcephaly, dysmorphic features, long philtrum, low-set ears, prominent
eyebrows and eyelashes, small triangular face, fifth-finger and toe
clinodactyly, and 2-3 toe syndactyly.

## DisMech phenotype coverage

The generated candidate target is not a valid disease match. The local
`Succinic_Semialdehyde_Dehydrogenase_Deficiency.yaml` entry is an ALDH5A1/GABA
catabolism disorder with gamma-hydroxybutyric aciduria, developmental delay,
hypotonia, ataxia, epilepsy, and behavioral dysregulation. It does not cover
HIBADH, 3-hydroxyisobutyrate dehydrogenase activity, or the valine-catabolism
3-hydroxyisobutyric aciduria signal.

No exact local DisMech disorder file, subtype, or grouping was found for
HIBADH, 3-hydroxyisobutyrate dehydrogenase deficiency, or
3-hydroxyisobutyric aciduria. The adjacent local HIBCH entry is a different
valine-catabolism step and should remain distinct.

## Concordance and completeness

Judgement: false-positive candidate and missing standalone DisMech target.

The fuzzy candidate is driven by the shared "semialdehyde dehydrogenase" wording
and neurometabolic presentation, not by shared gene, enzyme, pathway position, or
diagnostic biomarkers. IEMbase's HIBADH record would require a distinct
valine-catabolism entry rather than reuse of SSADH deficiency.

## Curation actions

- Do not map this record to
  `Succinic_Semialdehyde_Dehydrogenase_Deficiency.yaml`.
- Add a future standalone HIBADH/3-hydroxyisobutyrate dehydrogenase deficiency
  curation target.
- Preserve distinction from HIBCH deficiency, which is an adjacent but separate
  valine-catabolism disorder.
