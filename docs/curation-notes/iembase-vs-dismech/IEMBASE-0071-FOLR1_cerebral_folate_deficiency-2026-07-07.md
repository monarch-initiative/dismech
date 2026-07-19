# IEMbase 0071: FOLR1-related folate receptor alpha deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 71 |
| Nosology | 21.8.02.01 |
| Gene | FOLR1 |
| External IDs | OMIM:613068 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Best fuzzy candidate `Pyruvate_Dehydrogenase_Deficiency.yaml#E1-alpha deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive FOLR1-related folate receptor
alpha deficiency, also labeled cerebral folate deficiency and CFD.
Treatability is marked yes.

The characteristic biochemical signal includes abnormal CSF
5-methyltetrahydrofolic acid, plasma folate, and MRS choline and inositol rows.
Characteristic clinical rows include ataxia, cerebral atrophy on MRI,
dyskinesia, hypertonia, hypomyelination on MRI, seizures, and
myoclonic-astatic seizures.

Additional clinical rows include autism spectrum disorder, aggressive behavior,
cerebellar atrophy, chorea, developmental regression, abnormal EEG, gait
disturbance, microcephaly, movement disorder, tonic-clonic seizures, increased
tendon reflexes, and tremor. The treatment row is folinic acid.

## DisMech phenotype coverage

No valid local DisMech target was found for FOLR1, folate receptor alpha
deficiency, or primary cerebral folate deficiency.

The best fuzzy candidate, `Pyruvate_Dehydrogenase_Deficiency.yaml#E1-alpha
deficiency`, is a false positive. PDH deficiency can include neurologic disease,
seizures, and brain MRI abnormalities, but it is a pyruvate-to-acetyl-CoA
oxidative decarboxylation disorder, not a folate receptor or CSF folate
transport disorder.

The local `Tetrahydrobiopterin_Deficiency.yaml` entry mentions secondary
cerebral folate deficiency in DHPR deficiency, but that is not FOLR1-related
primary cerebral folate deficiency and should not be used as the mapping target.

## Concordance and completeness

Judgement: true local gap.

This is a treatable folate-receptor disorder with a distinctive low-CSF
5-MTHF/folinic-acid axis and neurologic presentation. Current DisMech coverage
only touches secondary cerebral folate issues in other disorders, not the
primary FOLR1 disease.

## Curation actions

- Keep this IEMbase record unmapped for now.
- Add a future standalone FOLR1 cerebral folate deficiency entry.
- Preserve distinction from PDH deficiency and DHPR/BH4 deficiency, which can
  share neurologic or folate-related features but have different primary
  mechanisms.
