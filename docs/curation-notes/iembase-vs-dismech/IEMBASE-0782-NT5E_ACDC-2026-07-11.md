# IEMbase 0782: NT5E-related ecto-5'-nucleotidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 782 |
| Nosology | 16.3.14.01 |
| Nosology code | IEM0039 |
| Gene | NT5E |
| External IDs | OMIM:211800; ORPHA:289601 |
| Generated mapping | MAPPED; `Hereditary_Arterial_and_Articular_Multiple_Calcification_Syndrome` |
| Candidate DisMech targets | `Hereditary_Arterial_and_Articular_Multiple_Calcification_Syndrome.yaml` |
| Review date | 2026-07-11 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as NT5E-related
ecto-5'-nucleotidase deficiency, with alternate name arterial calcification due
to deficiency of CD73 and abbreviation ACDC. The signal includes adult-onset
arterial calcification of iliac, femoral, and tibial arteries, intermittent
claudication, periarticular calcification, tendon calcification, and possible
calcification of cardiac valve rings or the aorta.

## DisMech phenotype coverage

`Hereditary_Arterial_and_Articular_Multiple_Calcification_Syndrome.yaml` is the
correct local target. It models biallelic NT5E/CD73 loss, reduced extracellular
adenosine generation, TNAP upregulation, pyrophosphate depletion, ectopic
arterial and periarticular calcification, arterial calcification, intermittent
claudication, periarticular calcification, arthritis, arthralgia, joint
deformity, arterial tortuosity/arteriomegaly, genetic testing, etidronate, and
supportive vascular/joint management.

## Concordance and completeness

Judgement: exact disease coverage.

The gene, OMIM identity, inheritance, ACDC synonym, lower-extremity arterial
calcification, claudication, and periarticular mineralization are concordant.
The local entry is mechanistically richer than IEMbase because it explicitly
models CD73 loss, extracellular adenosine, alkaline phosphatase, and
pyrophosphate-linked mineralization. IEMbase adds a few phenotype-review prompts
not emphasized locally, especially tendon calcification and possible cardiac
valve-ring or aortic calcification.

## Curation actions

- Treat `Hereditary_Arterial_and_Articular_Multiple_Calcification_Syndrome.yaml`
  as exact local coverage for IEMbase 0782.
- Preserve ACDC/CALJA/HAAMC as synonymous naming for this local target.
- Consider future phenotype review for tendon calcification and cardiac
  valve-ring/aortic calcification if supported by source evidence.
