# IEMbase 0651: HAAO-related 3-hydroxyanthranilic acid 3,4-dioxygenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 651 |
| Nosology | 1.8.02.01 |
| Nosology code | IEM0163 |
| Gene | HAAO |
| External IDs | OMIM:604521 |
| Generated mapping | UNMAPPED; weak candidate `Alkaptonuria.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive HAAO-related 3-hydroxyanthranilic acid
3,4-dioxygenase deficiency, also labeled vertebral, cardiac, renal, and limb
defects syndrome type 1.

Biochemical rows include increased plasma 3-hydroxyanthranilic acid in neonatal
and infantile ages, decreased plasma 3-hydroxyanthranilic acid in childhood,
and decreased plasma NAD+. Clinical rows include atrial septal defect,
hypoplastic left heart, optional intellectual disability, talipes, sensorineural
hearing loss, renal hypoplasia, and short stature.

## DisMech phenotype coverage

`Alkaptonuria.yaml` is a lexical/metabolic false candidate. It models HGD-related
homogentisate 1,2-dioxygenase deficiency in tyrosine degradation, with
homogentisic acid accumulation, ochronosis, dark urine, arthropathy, and
nitisinone treatment. It does not model HAAO, the kynurenine pathway, NAD+
deficiency, or the vertebral/cardiac/renal/limb malformation syndrome.

Targeted search did not find a local HAAO, 3-hydroxyanthranilic acid
dioxygenase, or VCRL type 1 disease entry.

## Concordance and completeness

Judgement: true local HAAO / VCRL1 gap; reject alkaptonuria as exact.

The weak candidate shares the broad aromatic-amino-acid catabolism neighborhood
but has the wrong gene, metabolite, mechanism, and clinical presentation.
IEMbase supplies a distinct congenital malformation and NAD/kynurenine
phenotype package that is not represented by existing DisMech entries.

## Curation actions

- Keep this row unmapped until a HAAO / VCRL type 1 target exists.
- Do not map to `Alkaptonuria.yaml`.
- Preserve 3-hydroxyanthranilic acid, NAD+, atrial septal defect, hypoplastic
  left heart, renal hypoplasia, talipes, hearing loss, short stature, and
  optional intellectual-disability prompts.
