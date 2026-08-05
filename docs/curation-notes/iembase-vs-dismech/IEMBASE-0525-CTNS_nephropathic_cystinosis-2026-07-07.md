# IEMbase 0525: CTNS-related nephropathic cystinosis

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 525 |
| Nosology | 1.11.01.02 |
| Gene | CTNS |
| External IDs | OMIM:219800; OMIM:219900; OMIM:219750; ORPHA:411634 |
| Generated mapping | AMBIGUOUS; identifier match on OMIM:219750 |
| Candidate DisMech targets | `Cystinosis.yaml`; `Cystinosis.yaml#Non-nephropathic ocular cystinosis` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as CTNS-related nephropathic cystinosis, with juvenile
cystinosis and CTNS as alternate labels. The record is autosomal recessive,
treatability is marked yes, and treatment rows list oral cysteamine bitartrate
and cysteamine eyedrops.

The characteristic biochemical rows include increased cystine in fibroblasts and
white blood cells, aminoaciduria, urinary losses of albumin, glucose, phosphate,
potassium, sodium, calcium, and uric acid, low plasma bicarbonate, low plasma
phosphate, low plasma potassium, and low or normal free carnitine. Clinical rows
emphasize renal Fanconi syndrome, chronic renal failure, polyuria, rickets,
renal osteodystrophy, nephrocalcinosis/nephrolithiasis, failure to thrive,
corneal cystine crystals, photophobia, retinopathy, hypogonadism, male
infertility, hypothyroidism, diabetes, myopathy, swallowing difficulty, and
later neurologic involvement.

## DisMech phenotype coverage

`Cystinosis.yaml` is the correct local target, but the generated mapping is
ambiguous because the IEMbase row carries the ocular-cystinosis OMIM identifier
alongside nephropathic infantile and juvenile identifiers. The local file
explicitly models CTNS lysosomal cystine transporter deficiency and has
nephropathic infantile, nephropathic juvenile, and non-nephropathic ocular
subtypes.

Local coverage is strong for CTNS/cystinosin biology, lysosomal cystine
accumulation, proximal tubule dysfunction, renal Fanconi syndrome, progressive
kidney disease, corneal crystal disease, oral and ophthalmic cysteamine, and
replacement therapy for Fanconi losses.

## Concordance and completeness

Judgement: correct local cystinosis target; manually resolve the ambiguity to
the nephropathic cystinosis context rather than the ocular-only subtype.

IEMbase and DisMech agree on CTNS, lysosomal cystine storage, autosomal
recessive inheritance, Fanconi syndrome, renal progression, corneal crystals,
photophobia, and cysteamine therapy. IEMbase is useful as a detailed analyte
checklist for tubular solute wasting and extrarenal late manifestations.

## Curation actions

- Keep this record mapped to `Cystinosis.yaml`, with nephropathic infantile and
  juvenile subtype context.
- Do not use OMIM:219750 alone to collapse this record to ocular cystinosis.
- Preserve the IEMbase renal-wasting analytes, free-carnitine row, endocrine,
  gonadal, ocular, myopathy, swallowing, and neurologic prompts for future
  review.
