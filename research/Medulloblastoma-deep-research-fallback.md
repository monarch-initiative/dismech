# Medulloblastoma Deep Research Fallback

## Provider Attempts

No deep-research provider was invoked for this root-level entry. The
two existing subgroup-specific dismech files
(`Medulloblastoma_WNT_Activated`, `Medulloblastoma_SHH_Activated`)
already have full deep-research artifacts in `research/` from their
own curation. This root entry was curated **directly from the
verified literature already cached in `references_cache/`** and
shared by both subgroup files; no provider was re-run because the
root scope only synthesises features that are shared across the four
WHO 2021 molecular subgroups (WNT, SHH, Group 3, Group 4).

## Integrated Literature Synthesis

Medulloblastoma (`MONDO:0007959`) is an embryonal, malignant brain
tumor that arises in the cerebellum and is the most common malignant
pediatric posterior-fossa tumor. PMID:35489737 ("Molecular
Stratification of Medulloblastoma: Clinical Outcomes and Therapeutic
Interventions") establishes that "Recent WHO (2021) guidelines
stratified MB into four molecular subgroups with four and eight
further subgroups for SHH and non-WNT/non-SHH MB, respectively." The
four subgroups are listed via `has_subtypes` rather than as a
pathophysiology node — per the reviewer feedback, classification
logic belongs in `has_subtypes` and `description`, not in
`pathophysiology[]`.

**Cellular origin / shared mechanism.** Across subgroups, tumors
derive from cerebellar progenitor populations and converge on
dysregulated proliferation in the developing cerebellum (`CL:0001031`
cerebellar granule cell, `GO:0008283` cell-population proliferation
INCREASED, `GO:0021549` cerebellum development ABNORMAL,
`UBERON:0002037` cerebellum). WNT tumors derive from lower-rhombic-lip
progenitors; SHH tumors from external-granule-layer granule-neuron
precursors. The subgroup-specific oncogenic pathways
(WNT/beta-catenin, Sonic Hedgehog, MYC-driven programs) feed this
common proliferative endpoint — the single shared pathophysiology
node curated here.

**Clinical syndrome.** Five HP-bound phenotypes are captured without
`frequency:` tags (Headache `HP:0002315`, Ataxia `HP:0001251`,
Vomiting `HP:0002013`, Macrocephaly `HP:0000256`, Papilledema
`HP:0001085`). Per the PR review the frequency tags were removed
because no quantitative cohort evidence was cited in scope to
support specific frequency bands; reintroduce per the
frequency-evidence SOP once subgroup-pooled clinical-cohort data
are curated.

**Management.** Three modalities of standard care across subgroups:
- Surgical resection (`MAXO:0000004`).
- Craniospinal irradiation (`MAXO:0000014`), generally avoided in
  children <3 years to limit neurocognitive late effects.
- Multi-agent chemotherapy (`MAXO:0000647`) with cisplatin
  (`CHEBI:27899`), vincristine (`CHEBI:28445`), cyclophosphamide
  (`CHEBI:4027`), and lomustine (`CHEBI:6520`) as the canonical
  agents (added in response to PR review).

## Out of scope for the root entry

- The previously-included histopathology block has been removed
  because it relied on `NCIT:C3222` (the disease) as the
  `finding_term` and evidenced an epidemiological claim, not a
  pathologist-level histological finding. True histology (densely
  packed small blue round cells, Homer Wright rosettes,
  desmoplastic-nodular vs anaplastic large-cell morphology,
  synaptophysin expression) belongs in subgroup-specific entries and
  in a future repo-wide reframing of `histopathology[]` (the WNT and
  SHH subtype files carry the same "epidemiology as histopathology"
  pattern; flagged for follow-up).
- Subgroup-specific driver mutations, prognosis stratification, and
  targeted therapy (SHH-pathway inhibitors, WNT radiation
  de-escalation, ONC201 for H3K27M-mutant variants) live in the
  existing subtype files.
- Group 3 and Group 4 dismech entries are scoped as follow-up
  curation.
- CSF biomarkers and leptomeningeal-dissemination staging biology
  are scoped as follow-up.
