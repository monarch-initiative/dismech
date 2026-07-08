# IEMbase 0759: PTDSS1-related phosphatidylserine synthase 1 superactivity

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 759 |
| Nosology | 14.5.01.08 |
| Nosology code | IEM0667 |
| Gene | PTDSS1 |
| External IDs | OMIM:151050; ORPHA:2658 |
| Generated mapping | AMBIGUOUS; exact alias `LMHD` matched multiple local subtype entities |
| Candidate DisMech targets | `Lenz-Majewski_hyperostotic_dwarfism.yaml` |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal dominant record as PTDSS1-related
phosphatidylserine synthase 1 superactivity, with alternate name
Lenz-Majewski syndrome and abbreviation LMHD. The phenotype signal is extensive
and classic for Lenz-Majewski hyperostotic dwarfism: hyperostosis, skeletal
dysplasia, dwarfism or short stature, macrocephaly, wide forehead, delayed or
enlarged fontanels, brachydactyly, syndactyly, possible absent phalanges,
humeral-radial synostosis, skull-base sclerosis, osteopenic epiphyses,
metaphyseal hypostosis, cutis laxa, thin skin, cutis marmorata, sparse hair,
enamel hypoplasia, choanal atresia or stenosis, anteriorly placed anus,
hypospadias, chordee, inguinal hernia, hydrocephalus, corpus callosum agenesis,
intellectual disability, hypotonia, sensorineural hearing loss, and failure to
thrive.

## DisMech phenotype coverage

`Lenz-Majewski_hyperostotic_dwarfism.yaml` is the correct local target. The
generated ambiguity is caused by local `Classic` and `Attenuated` subtype
entities sharing the LMHD match key, not by uncertainty about the disease file.
The DisMech entry models PTDSS1 gain-of-function phosphatidylserine
biosynthesis dysregulation, progressive hyperostotic skeletal dysplasia, cutis
laxa, short stature, brachydactyly, syndactyly, cranial hyperostosis,
craniofacial dysmorphism, intellectual disability, sensorineural hearing
impairment, hydrocephalus, seizures, and hyperphosphoserinuria.

## Concordance and completeness

Judgement: exact local coverage with subtype-level mapper ambiguity.

The core disease identity, gene, inheritance, and skeletal-cutaneous-neurologic
phenotype cluster are strongly concordant. IEMbase is more granular for several
malformation and anatomic findings, including corpus callosum agenesis,
anteriorly placed anus, chordee, hypospadias, inguinal hernia, choanal stenosis,
nasolacrimal duct stenosis, humeral-radial synostosis, osteopenic epiphyses,
and skull-base sclerosis. DisMech is stronger mechanistically and explicitly
distinguishes classic from attenuated PTDSS1-related LMHD.

## Curation actions

- Treat `Lenz-Majewski_hyperostotic_dwarfism.yaml` as the exact disease-file
  mapping.
- Do not treat the generated ambiguity as a local gap; it reflects local
  subtype matches.
- Consider IEMbase's detailed skeletal, craniofacial, genitourinary, and
  gastrointestinal malformation rows as future phenotype-completeness prompts.
