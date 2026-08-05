# IEMbase 0554: ABCC2-related Dubin-Johnson syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 554 |
| Nosology | 17.2.02.01 |
| Gene | ABCC2 |
| External IDs | OMIM:237500; OMIM:601107; ORPHA:234 |
| Generated mapping | UNMAPPED; best candidate `Stevens-Johnson_Syndrome.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ABCC2-related canalicular bilirubin glucuronide transporter
deficiency, with alternate labels Dubin-Johnson syndrome and ABCC2/DJS. The
record is autosomal recessive, and treatability is unknown. No treatment rows
are listed.

The biochemical rows include positive ABCC2 sequencing, normal clearance of
unconjugated bromsulfthalein, normal urinary coproporphyrin I,
normal-to-increased conjugated bilirubin, and pigment granules in liver biopsy.
Characteristic clinical rows are episodic jaundice and a normal myocardial
ischemia row.

## DisMech phenotype coverage

No exact local Dubin-Johnson syndrome target was found for ABCC2 or canalicular
bilirubin transport. The generated `Stevens-Johnson_Syndrome.yaml` candidate is
a lexical false positive from the name "Johnson"; it is a severe mucocutaneous
drug-reaction phenotype, not an inherited bilirubin transporter disorder.

Local porphyria records mention coproporphyrins, but they do not model ABCC2,
black liver pigment, or benign conjugated hyperbilirubinemia.

## Concordance and completeness

Judgement: true local disease gap; reject the Stevens-Johnson candidate.

IEMbase provides a focused Dubin-Johnson profile with ABCC2 identity,
conjugated bilirubin, liver pigment granules, episodic jaundice, and
distinguishing normal coproporphyrin I and bromsulfthalein rows. No current
local disease file captures this target.

## Curation actions

- Keep this record unmapped until an ABCC2 / Dubin-Johnson syndrome target
  exists.
- Do not map to `Stevens-Johnson_Syndrome.yaml` or porphyria entries.
- Preserve liver pigment granules, conjugated bilirubin, episodic jaundice,
  normal coproporphyrin I, normal bromsulfthalein clearance, and the
  differential normal myocardial-ischemia row as review prompts.
