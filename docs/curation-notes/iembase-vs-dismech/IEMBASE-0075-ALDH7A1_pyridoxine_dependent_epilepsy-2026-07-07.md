# IEMbase 0075: ALDH7A1-related alpha-aminoadipic semialdehyde dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 75 |
| Nosology | 21.6.02.02 |
| Gene | ALDH7A1 |
| External IDs | OMIM:266100 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Best fuzzy candidate `Succinic_Semialdehyde_Dehydrogenase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive ALDH7A1-related
alpha-aminoadipic semialdehyde dehydrogenase deficiency, with alternate labels
pyridoxine-dependent seizures, antiquitin deficiency, and AASADHD. Treatability
is marked yes, with a reported prevalence of 1:400,000 to 1:700,000.

The characteristic biochemical signal includes abnormal delta1-piperideine-
6-carboxylate in CSF and urine, abnormal pipecolic acid in CSF, and abnormal
CSF pyridoxal 5-phosphate. IEMbase also lists alpha-aminoadipic semialdehyde in
CSF, plasma, and urine, pipecolic acid before and under B6 treatment, glucose,
and lactate.

The characteristic clinical row is pharmacoresistant seizures. Additional rows
include agenesis or hypogenesis of the corpus callosum, developmental delay,
feeding difficulty, hypotension, hypothermia, hypotonia, intestinal
pseudo-obstruction, low Apgar scores, mega cisterna magna, and vomiting.

Treatment rows include pyridoxine, lysine restriction, and arginine.

## DisMech phenotype coverage

No valid local DisMech target was found for ALDH7A1, antiquitin deficiency, or
pyridoxine-dependent epilepsy.

The best fuzzy candidate, `Succinic_Semialdehyde_Dehydrogenase_Deficiency.yaml`,
is a false positive. SSADH deficiency is an ALDH5A1/GABA catabolism disorder.
ALDH7A1 disease is a lysine-catabolism/antiquitin disorder with alpha-AASA,
P6C, pipecolic-acid, and pyridoxine-responsive seizure biology.

## Concordance and completeness

Judgement: true local gap.

The candidate match is driven by shared "semialdehyde dehydrogenase" wording and
epilepsy/neurodevelopmental features, but the genes, pathway, biomarkers, and
treatment logic differ. A future DisMech entry should also remain distinct from
AASS-related hyperlysinemia/saccharopinuria.

## Curation actions

- Keep this IEMbase record unmapped for now.
- Add a future standalone ALDH7A1 pyridoxine-dependent epilepsy / antiquitin
  deficiency entry.
- Prioritize alpha-AASA, P6C, pipecolic acid, PLP depletion, neonatal or
  infantile pharmacoresistant seizures, pyridoxine response, lysine restriction,
  and arginine as curation anchors.
