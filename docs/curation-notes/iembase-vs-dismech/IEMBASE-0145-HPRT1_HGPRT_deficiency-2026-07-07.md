# IEMbase 0145: HPRT1-related hypoxanthine guanine phosphoribosyltransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 145 |
| Nosology | 16.2.11.01 |
| Gene | HPRT1 |
| External IDs | OMIM:300322; OMIM:308000; ORPHA:206428 |
| Generated mapping | MAPPED to `Lesch-Nyhan_Syndrome.yaml` |
| Candidate DisMech targets | `Lesch-Nyhan_Syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as HPRT1-related hypoxanthine guanine
phosphoribosyltransferase deficiency, with alternate labels Lesch-Nyhan
syndrome and Kelley-Seegmiller syndrome. Treatability is marked yes.

The biochemical rows include markedly decreased red-cell HGPRT activity,
increased plasma and urinary hypoxanthine, increased urinary xanthine, increased
plasma and urinary uric acid, and increased urinary AICA riboside. Clinical rows
include gouty arthritis, hematuria, acute renal failure, urolithiasis,
intellectual disability, action dystonia, choreoathetosis, pyramidal signs,
spasticity, self-mutilation, cerebral palsy wording, urinary infections, and
renal/urologic complications.

## DisMech phenotype coverage

`Lesch-Nyhan_Syndrome.yaml` is the correct target. It models HPRT1 deficiency as
an X-linked purine-salvage disorder with HPRT enzyme deficiency, purine
overproduction, hyperuricemia and hyperuricosuria, gout, nephrolithiasis,
renal insufficiency, acute kidney injury, hematuria, dystonia, choreoathetosis,
spasticity, intellectual disability, and self-injurious behavior.

The local entry also distinguishes classic loss-of-function Lesch-Nyhan disease
from hypomorphic Kelley-Seegmiller variants and includes treatment branches for
urate lowering and neurobehavioral management.

## Concordance and completeness

Judgement: correct mapping with high concordance.

The local entry is broader and more mechanistic than IEMbase for basal-ganglia
and treatment coverage. IEMbase is more granular for compartment-specific purine
metabolites, especially hypoxanthine, xanthine, and AICA riboside. Those are
useful biomarker refinement leads, but they do not change the mapping.

## Curation actions

- Keep the mapping to `Lesch-Nyhan_Syndrome.yaml`.
- Treat the IEMbase Kelley-Seegmiller label as already conceptually covered by
  the local hypomorphic HPRT1 variant discussion.
- Consider future biomarker refinement for hypoxanthine, xanthine, and AICA
  riboside compartment-specific rows.
