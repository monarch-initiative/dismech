# IEMbase 0652: KYNU-related 3-hydroxykynureninase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 652 |
| Nosology | 1.8.01.02 |
| Nosology code | IEM0162 |
| Gene | KYNU |
| External IDs | OMIM:605197; ORPHA:79155 |
| Generated mapping | UNMAPPED; weak candidate `Hereditary_Orotic_Aciduria.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive KYNU-related 3-hydroxykynureninase
deficiency, with alternate labels vertebral, cardiac, renal, and limb defects
syndrome type 2 and xanthurenic aciduria.

Biochemical rows include increased urinary 3-hydroxykynurenine, kynurenine, and
xanthurenic acid; increased plasma 3-hydroxykynurenine; and decreased plasma
NAD+. Clinical rows include anteriorly placed anus, hypoplastic left heart,
patent ductus arteriosus, rhizomelia, abnormal/delayed/absent speech,
syndactyly, renal hypoplasia, short stature, and talipes.

## DisMech phenotype coverage

`Hereditary_Orotic_Aciduria.yaml` is a lexical false candidate. It models
UMPS-related de novo pyrimidine synthesis failure, urinary orotic acid,
megaloblastic anemia, developmental delay, and uridine responsiveness. It does
not model KYNU, kynurenine-pathway flux, xanthurenic aciduria, NAD+ deficiency,
or the VCRL2 malformation pattern.

Targeted search did not find a local KYNU, 3-hydroxykynureninase deficiency,
xanthurenic aciduria, or VCRL type 2 disease entry.

## Concordance and completeness

Judgement: true local KYNU / VCRL2 gap; reject hereditary orotic aciduria as
exact.

The generated candidate is an unrelated nucleotide-metabolism disorder. IEMbase
points to a separate tryptophan/kynurenine-pathway malformation disorder with
specific metabolite readouts and cardiac/renal/limb/developmental prompts.

## Curation actions

- Keep this row unmapped until a KYNU / VCRL type 2 target exists.
- Do not map to `Hereditary_Orotic_Aciduria.yaml`.
- Preserve increased 3-hydroxykynurenine, kynurenine, xanthurenic acid,
  decreased NAD+, congenital heart findings, renal hypoplasia, rhizomelia,
  syndactyly, talipes, anteriorly placed anus, short stature, and speech prompts.
