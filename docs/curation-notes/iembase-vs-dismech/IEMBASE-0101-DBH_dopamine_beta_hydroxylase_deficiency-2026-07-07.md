# IEMbase 0101: DBH-related dopamine beta-hydroxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 101 |
| Nosology | 23.1.03.01 |
| Gene | DBH |
| External IDs | OMIM:223360 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | None; fuzzy candidate `Congenital_Adrenal_Hyperplasia.yaml#11B-OHD` is not valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as DBH-related dopamine beta-hydroxylase deficiency in
the monoamine neurotransmission group. Treatability is marked yes, although the
cached JSON has no treatment rows.

The biochemical signal is strong and specific: decreased CSF MHPG, increased
plasma dopamine, very low plasma epinephrine and norepinephrine, increased CSF
and urinary homovanillic acid, increased CSF and plasma L-dopa, decreased
urinary VMA, very low plasma dopamine beta-hydroxylase, and low-to-normal plasma
glucose in neonatal or infancy rows.

The clinical rows are behavioral disorder and syncope, with syncope becoming
more prominent in adolescence and adulthood.

## DisMech phenotype coverage

There is no valid local DBH deficiency target. The generated fuzzy candidate to
`Congenital_Adrenal_Hyperplasia.yaml#11B-OHD` is a beta-hydroxylase lexical
collision: 11-beta-hydroxylase congenital adrenal hyperplasia is a steroidogenic
adrenal disorder, not dopamine beta-hydroxylase deficiency.

The `Disorder_of_Catecholamine_Synthesis.yaml` umbrella includes AADC, TH,
recessive GTP cyclohydrolase I, sepiapterin reductase, and DNAJC12-related
monoamine synthesis disease, but it does not currently include a DBH subtype or
the norepinephrine/epinephrine-deficiency biochemical pattern.

## Concordance and completeness

Judgement: true local gap.

IEMbase provides enough biochemical specificity to seed a future entry:
dopamine is high while norepinephrine and epinephrine are very low, with low
DBH enzyme activity and low VMA. DisMech currently has no place to capture that
pattern except as a future expansion of monoamine/catecholamine disorder
coverage.

## Curation actions

- Do not map this record to congenital adrenal hyperplasia.
- Add a future standalone DBH deficiency entry or extend the catecholamine
  synthesis umbrella with a DBH subtype if that umbrella remains the preferred
  modeling level.
- Capture syncope/orthostatic-autonomic presentation and the distinctive plasma
  catecholamine profile when curated.
