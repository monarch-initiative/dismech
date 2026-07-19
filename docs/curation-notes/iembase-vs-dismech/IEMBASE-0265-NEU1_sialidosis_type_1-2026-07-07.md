# IEMbase 0265: NEU1-related Alpha-neuraminidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 265 |
| Nosology | 20.3.01.01 |
| Gene | NEU1 |
| External IDs | OMIM:256550; ORPHA:309294 |
| Generated mapping | MAPPED; `Sialidosis_Type_1.yaml` |
| Candidate DisMech targets | `Sialidosis_Type_1.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as NEU1-related alpha-neuraminidase deficiency (CDG),
with alternate labels NEU1-CDG, sialidosis/mucolipidosis type I, and NEU. The
record is autosomal recessive and treatability is marked unknown, with no
treatment rows in the cached JSON.

Biochemical rows include decreased alpha-neuraminidase activity and increased
urinary sialic-acid-rich oligosaccharides. Clinical rows include angiokeratoma,
ataxia, cherry-red spot, foam cells, myoclonic epilepsy, chronic renal failure,
seizures, spasticity, exaggerated startle response, and vacuolated lymphocytes.

## DisMech phenotype coverage

`Sialidosis_Type_1.yaml` is the correct local target for the generated mapping.
The local entry covers type 1 sialidosis as an ultra-rare autosomal recessive
NEU1/neuraminidase-1 lysosomal storage disorder with residual but insufficient
sialidase activity, impaired degradation of sialylated glycoproteins and
oligosaccharides, adolescent or young-adult onset progressive myoclonus,
ataxia, seizures, visual impairment, cherry-red macular spots, urinary
sialylated oligosaccharides, reduced neuraminidase activity, and supportive or
investigational treatment strategies.

The local entry explicitly distinguishes normomorphic type 1 disease from the
more dysmorphic type 2 phenotype.

## Concordance and completeness

Judgement: correct file-level mapping, with phenotype-scope caution.

IEMbase and DisMech agree on NEU1/sialidosis type 1 identity, autosomal
recessive inheritance, decreased neuraminidase activity, urinary sialylated
oligosaccharide signal, ataxia, cherry-red spot, myoclonic epilepsy/seizures,
spasticity, and startle/myoclonus-related neurologic disease. IEMbase adds
angiokeratoma, foam cells, chronic renal failure, and vacuolated lymphocytes,
which should be reviewed carefully before importing into the type 1 entry
because the local curation separates type 1 from more systemic type 2
sialidosis features.

## Curation actions

- Keep this record mapped to `Sialidosis_Type_1.yaml`.
- Review IEMbase-only renal, angiokeratoma, foam-cell, and vacuolated-lymphocyte
  rows before importing them into the type 1 entry.
- No immediate mapping correction is needed, but the IEMbase label has broader
  sialidosis-spectrum wording than the local type 1 page.
