# IEMbase 0300: GNPTG-related UDP-N-acetylglucosamine-1-phosphotransferase subunit gamma deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 300 |
| Nosology | 20.6.02.01 |
| Gene | GNPTG |
| External IDs | OMIM:252605; ORPHA:577 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `GNPTG-Mucolipidosis.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GNPTG-CDG / mucolipidosis III gamma / pseudo-Hurler
polydystrophy. Inheritance is autosomal recessive and treatability is unknown.

The cached clinical signal is sparse: joint contractures, recurrent otitis
media, coarse facial features, and intellectual disability. Biochemical rows are
more informative and show increased serum gamma-subunit/phosphotransferase
readout, decreased leukocyte readout, normal-to-increased urinary
glycosaminoglycans, and normal-to-increased urinary oligosaccharides.

## DisMech phenotype coverage

`GNPTG-Mucolipidosis.yaml` is the correct local target despite the generated
UNMAPPED status. The local entry models biallelic GNPTG variants, gamma-subunit
impairment of GlcNAc-1-phosphotransferase, reduced mannose-6-phosphate tagging,
missorting and hypersecretion of lysosomal hydrolases, and slowly progressive
lysosomal substrate accumulation affecting skeletal, joint, and connective
tissues.

Local phenotypes include skeletal dysplasia, limitation of joint mobility,
chronic pain, cardiac valve disease, carpal tunnel syndrome, restrictive lung
disease, aortic valve insufficiency, motor delay, cognitive impairment, and
autosomal recessive inheritance. Local treatments include supportive care,
bisphosphonate therapy, joint replacement surgery, and pain management.

## Concordance and completeness

Judgement: false negative; resolve to `GNPTG-Mucolipidosis.yaml`.

IEMbase and DisMech agree on GNPTG identity, recessive inheritance, ML III gamma
scope, joint/connective-tissue involvement, coarse features, otitis, cognitive
involvement, and the broader lysosomal enzyme-targeting mechanism. DisMech is
richer for skeletal, pain, cardiac, carpal-tunnel, pulmonary, and management
coverage.

IEMbase adds useful biochemical prompts, especially the serum-versus-leukocyte
directionality and urinary glycosaminoglycan/oligosaccharide rows. The "(CDG)"
label in IEMbase should be treated as alternate nomenclature context, not as a
reason to separate this from GNPTG-mucolipidosis.

## Curation actions

- Map this record to `GNPTG-Mucolipidosis.yaml`.
- Consider adding the IEMbase serum/leukocyte assay directionality and urinary
  GAG/oligosaccharide prompts if evidence supports them.
- Keep GNPTG ML III gamma distinct from GNPTAB-related mucolipidosis II and
  mucolipidosis III alpha/beta.
