---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-05-13T12:00:00Z'
end_time: '2026-05-13T13:30:00Z'
duration_seconds: 5400.0
citation_count: 6
notes: >
  No automated deep-research provider was invoked for this entry. The
  curation was performed directly from the verified primary literature
  already cached in `references_cache/` (PMID:9425895, PMID:9425900,
  PMID:9836639, PMID:28926830, PMID:36939707, PMID:37827512) plus the
  Orphanet structured-database record ORPHA:1949. This fallback
  artifact records the literature synthesis underlying the disorder
  YAML so the content-completeness checklist can be applied.
---

## Question

Produce a disease-level dismech curation for benign neonatal seizures
(self-limited familial neonatal epilepsy, BFNS/SeLNE; MONDO:0016027)
with ontology-grounded disease and subtype identifiers, ILAE-aligned
clinical phenotypes, a precise KCNQ2/KCNQ3 M-current pathophysiology
model, and PMID-backed evidence for inheritance, subtypes, diagnosis,
and targeted therapy.

## Output

# Benign Neonatal Seizures: Manual Deep Research Summary

## Disease-level modeling decision

Benign neonatal seizures is modeled as one disease-level entry covering
the autosomal-dominant KCNQ2- and KCNQ3-related forms of self-limited
familial neonatal epilepsy. Two molecular subtypes are exposed via
`has_subtypes`, each grounded to the corresponding MONDO term:

- **KCNQ2-BFNS** → `MONDO:0007365` (seizures, benign familial neonatal,
  1; xref OMIM:121200).
- **KCNQ3-BFNS** → `MONDO:0007366` (seizures, benign familial neonatal,
  2; xref OMIM:121201).

The much more severe KCNQ2-related developmental and epileptic
encephalopathy (KCNQ2-DEE) is intentionally excluded from this entry —
the disease description notes the boundary so future curators do not
collapse the two clinical entities.

## Inheritance and penetrance

ORPHA:1949 lists autosomal dominant inheritance for self-limited
neonatal epilepsy. The original KCNQ2 paper (PMID:9425895) frames the
condition as "a dominantly inherited disorder of newborns."

The ILAE Genetic Literacy review (PMID:36939707) is the strongest
source for **incomplete penetrance and de novo inheritance**:

> "incomplete penetrance and de novo inheritance occur."

This justifies tagging both `KCNQ2` and `KCNQ3` Inheritance blocks in
the `genetic` section with `penetrance: INCOMPLETE`.

## Pathophysiology: KCNQ2/KCNQ3 LOF → M-current attenuation → transient neonatal hyperexcitability

The mechanistic chain is documented across the cached literature:

1. **KCNQ2 and KCNQ3 subunits form the neuronal M-channel.**
   PMID:9836639: "It is concluded that both these subunits contribute
   to the native M-current."
2. **The M-current sets subthreshold excitability.** PMID:9836639:
   "The M-current regulates the subthreshold electrical excitability
   of many neurons, determining their firing properties and
   responsiveness to synaptic input."
3. **Heterozygous LOF variants in KCNQ2/3 reduce M-current density and
   cause BFNC.** PMID:9425895: "This finding in BFNC provides
   additional evidence that defects in potassium channels are involved
   in the mammalian epilepsy phenotype." PMID:9425900 maps a KCNQ3
   pore-region missense variant co-segregating with BFNC.
4. **Network-level hyperexcitability is transient and remits.**
   PMID:36939707: "Seizures tend to remit during infancy or early
   childhood and are therefore called 'self-limited'."

The disorder YAML therefore exposes two atomic pathophysiology nodes
connected by a `downstream` edge:

- **`KCNQ2/KCNQ3 K+ Channel Loss-of-Function and M-Current
  Attenuation`** (`central_effector`) — captures the molecular
  function (GO:0005249, DECREASED) and process (GO:0086009 membrane
  repolarization, DECREASED).
- **`Neonatal Neuronal Hyperexcitability`** (`downstream_phenotype`)
  — captures the network-level firing increase (GO:0019228 neuronal
  action potential, INCREASED), localized to cerebral cortex, with a
  further `downstream` edge to the clinical Focal-onset Seizure
  phenotype.

This decomposition deliberately avoids the bundled "channelopathy →
seizures" anti-pattern flagged in prior dismech reviews.

## Clinical phenotypes

ORPHA:1949 supplies a curated HPO-frequency table that I have mapped
directly into the `phenotypes` block:

- Neonatal seizure (HP:0032807) — Very frequent (99–80%)
- Focal-onset seizure (HP:0007359) — Very frequent
- Focal tonic seizure (HP:0011167) — Very frequent
- Focal clonic seizure (HP:0002266) — Very frequent
- Apnea (HP:0002104) — Frequent (79–30%)
- Focal EEG discharges with secondary generalization (HP:0011188) —
  Very frequent

PMID:28926830 (the multicenter aEEG case series) supports the focal
tonic semiology with characteristic apnea and desaturation.

## Diagnosis and targeted therapy

PMID:36939707 supports `molecular genetic testing` (MAXO:0000533) as
part of the diagnostic workup. PMID:28926830 and PMID:37827512 jointly
support amplitude-integrated EEG (aEEG) as an early-recognition tool
that enables targeted carbamazepine therapy before genetic
confirmation:

> "Recognition of the distinctive ictal aEEG pattern in the NICU
> allowed early and effective targeted therapy with CBZ in four
> neonates, well before genetic results became available."
> (PMID:37827512)

Carbamazepine (CHEBI:3387) is exposed as a specific treatment using
the `treatment_term` = MAXO:0000167 (anticonvulsant agent therapy) +
`therapeutic_agent` = CHEBI:3387 pattern, with a `target_mechanisms`
link back to the Neonatal Neuronal Hyperexcitability node. The
`Sodium-channel-blocking Antiseizure Medication Therapy` treatment
generalizes this to the drug class.

Phenobarbital is recognized in clinical practice as an empiric
first-line neonatal antiseizure agent before genetic confirmation,
but is intentionally **not** modeled as a targeted therapy because
it does not act on the KCNQ2/3 mechanism; the YAML keeps the
mechanistic focus on sodium-channel blockers, per the precision-
medicine framing in PMID:28926830.

## References used

- PMID:9425895 — KCNQ2 discovery in BFNC.
- PMID:9425900 — KCNQ3 pore-region missense in BFNC.
- PMID:9836639 — KCNQ2/KCNQ3 as molecular correlates of the M-channel.
- PMID:28926830 — Distinctive ictal aEEG pattern in KCNQ2 neonatal
  epilepsy; precision medicine with Na+-channel blockers.
- PMID:36939707 — ILAE Genetic Literacy review of self-limited
  familial neonatal/infantile epilepsies; incomplete penetrance and
  de novo inheritance.
- PMID:37827512 — Carbamazepine targeted therapy guided by aEEG
  pattern recognition.
- ORPHA:1949 — Orphanet structured-database record (HPO frequencies,
  gene-disease table, MONDO/OMIM cross-references, inheritance).
