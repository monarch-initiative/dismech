# IEMbase 0359: B3GLCT-related Peters plus syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 359 |
| Nosology | 18.2.03.02 |
| Gene | B3GLCT |
| External IDs | OMIM:261540; ORPHA:709 |
| Generated mapping | UNMAPPED; low candidate `Gaucher_Disease.yaml` |
| Candidate DisMech targets | No exact local target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents B3GALTL-CDG/Peters plus syndrome. The record uses the legacy
B3GALTL label and abbreviation, while the gene field uses the current symbol
B3GLCT. It is an autosomal recessive O-fucose-specific beta-1,3-glucosylation
disorder.

Characteristic rows include anterior eye chamber anomalies, cryptorchidism,
facial dysmorphism, hearing loss, hydrocephalus, and normal sialotransferrins.
Additional clinical rows include anteriorly placed anus, brachydactyly, cardiac
malformations, cleft lip, cleft palate, gastroesophageal reflux, growth
retardation, hydronephrosis, hydroureter, long filtrum, malrotation, prominent
forehead, psychomotor delay, and short palpebral fissures. The only biochemical
row is sialotransferrins. No treatment rows are present.

## DisMech phenotype coverage

The low Gaucher disease candidate is a false lexical neighbor and should be
rejected. Gaucher disease is a lysosomal glucocerebrosidase disorder and does
not cover B3GLCT, Peters plus syndrome, anterior chamber dysgenesis, or
O-fucose glucosylation.

No exact DisMech disease file for B3GLCT/Peters plus syndrome was identified.
Other local anterior-segment or Peters anomaly contexts may provide phenotype
family context only; they should not be treated as a gene-level or disease-level
mapping for this IEMbase record.

## Concordance and completeness

Judgement: true local gap; reject the generated Gaucher disease candidate.

IEMbase supplies a coherent Peters plus syndrome profile: B3GLCT identity,
autosomal recessive inheritance, anterior eye chamber anomalies, short-limb or
brachydactyly signal, craniofacial clefting/dysmorphism, growth and
developmental involvement, genitourinary/GI malformations, and normal
sialotransferrins.

## Curation actions

- Do not map this record to `Gaucher_Disease.yaml`.
- Create or prioritize a future B3GLCT/Peters plus syndrome target if this
  disease enters active DisMech curation.
- Preserve both B3GALTL legacy labeling and B3GLCT current-symbol identity when
  curating the future entry.
- Verify the source spelling "long filtrum" before importing that row; the
  intended clinical term may be "long philtrum".
