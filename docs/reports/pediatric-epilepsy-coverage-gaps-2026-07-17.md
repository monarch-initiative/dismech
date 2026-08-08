# Pediatric epilepsy coverage gaps in dismech (2026-07-17)

A survey of childhood-relevant epilepsy syndromes and developmental &
epileptic encephalopathies (DEEs) that do **not** yet have a dedicated
`Disease` entry in `kb/disorders/`. Presence was tested against each entry's
own top-level `name:` field (not incidental text mentions), since many of the
genes below appear only as differential-diagnosis mentions inside unrelated
entries (e.g. Lennox-Gastaut named inside `KBG_Syndrome`/`DNM1_Encephalopathy`,
CDKL5 inside `STXBP1_Encephalopathy`, SCN2A/SCN8A as comparisons).

This report is the motivating analysis behind the Lennox-Gastaut syndrome
curation and is a candidate worklist for subsequent pediatric-epilepsy
curation batches.

## Already represented (for reference)

Dravet, GEFS+, Infantile Spasms (West), GLUT1 Deficiency Syndrome, STXBP1,
SNAP25, STX1B, CPLX1-DEE, DNM1, UNC13A (×2), Rett, MECP2 duplication, FOXG1,
Angelman, Tuberous Sclerosis Complex, Aicardi, Jeavons, Landau-Kleffner,
Pallister-Hall (gelastic/hypothalamic hamartoma), the lissencephaly spectrum
(ARX, Miller-Dieker, Reelin, etc.), Menkes, Wolf-Hirschhorn, Mesial Temporal
Lobe Epilepsy with Hippocampal Sclerosis, Progressive Myoclonus Epilepsy,
Benign Familial Infantile Epilepsy, Benign Neonatal Seizures (KCNQ2/3 benign).

## Missing — the common, high-impact childhood syndromes

- **Lennox-Gastaut syndrome** — defining childhood epileptic encephalopathy
  (tonic seizures, slow spike-wave, cognitive regression). *(now in progress)*
- **CDKL5 deficiency disorder** — one of the commonest single-gene DEEs.
- **PCDH19 clustering epilepsy** (girls-clustering / EFMR) — X-linked,
  female-predominant, cellular-interference mechanism.
- **SYNGAP1-related DEE** — among the commonest genetic NDD-plus-epilepsy
  disorders (myoclonic-atonic/absence, eyelid myoclonia).
- **Childhood absence epilepsy** and **juvenile myoclonic epilepsy** — the two
  commonest genetic generalized epilepsies; currently only list-items inside the
  umbrella `Epilepsy.yaml`.
- **Self-limited epilepsy with centrotemporal spikes** (SeLECTS / Rolandic /
  BECTS) — the single most common focal epilepsy of childhood.

## Missing — high-value because treatable or mechanistically distinct

- **Pyridoxine-dependent epilepsy** (ALDH7A1/antiquitin) and **PNPO
  deficiency** — the archetypal vitamin-responsive neonatal epilepsies.
- **KCNQ2 developmental & epileptic encephalopathy** — the severe-end companion
  to the already-curated Benign Neonatal Seizures entry (same gene, opposite
  severity; directly answers a knowledge gap posed in that entry).
- **Sturge-Weber syndrome** — structural childhood epilepsy with a somatic-GNAQ
  vascular mechanism.
- **Rasmussen encephalitis** — immune/inflammatory unihemispheric pediatric
  focal epilepsy; mechanistically unlike the rest of the pool.

## Missing — other recurrent DEE genes / syndromes

- **Ohtahara / early-infantile DEE** (neonatal anchor of the age spectrum)
- **Epilepsy of infancy with migrating focal seizures** (EIMFS, KCNT1)
- **SCN2A-DEE**, **SCN8A-DEE**
- **Doose syndrome** (epilepsy with myoclonic-atonic seizures)
- **GRIN2A / GRIN2B**, **GNAO1**, **SLC6A1**, **CHD2**, **KCNB1**, **SLC13A5**

## Missing — structural / etiologic

- **Hemimegalencephaly** (currently only inside `CLOVES_Syndrome`)
- **Hypothalamic hamartoma / gelastic epilepsy** (currently only inside
  `Pallister-Hall_Syndrome`)
- **Focal cortical dysplasia** (no standalone mechanism entry)
- **Panayiotopoulos syndrome**, **Ring chromosome 20 syndrome**, **Alpers
  syndrome (POLG)**

## Suggested next batches

- **Treatable/companion trio:** KCNQ2-DEE + pyridoxine-dependent epilepsy + PNPO
  deficiency.
- **Commonest missing childhood DEEs:** Lennox-Gastaut (in progress) + CDKL5 +
  PCDH19 + SYNGAP1.
