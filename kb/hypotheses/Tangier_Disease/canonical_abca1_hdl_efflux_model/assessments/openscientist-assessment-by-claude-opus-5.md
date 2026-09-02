# OpenScientist report review: `canonical_abca1_hdl_efflux_model` (Tangier disease)

- **Provider report:** `../openscientist.md` (696 lines, 35 citations, run 2026-05-22)
- **Assessor:** claude-opus-5, 2026-09-02
- **Structured assessment:** `openscientist-assessment-by-claude-opus-5.yaml`
- **Verdict:** PARTIALLY_SUPPORTED

## What the report set out to do, and what it actually contributes

The seed handed to this run was the KB's own canonical hypothesis: biallelic
ABCA1 loss of function impairs apolipoprotein-mediated lipid efflux, blocks
nascent HDL assembly, and produces cholesteryl ester storage with
reticuloendothelial, neurologic and vascular disease. The report's Executive
Judgment returns that chain almost verbatim and calls it firmly established.
That part is correct but is not new support — it is the seed restated. What
makes the report worth reviewing is its second claim: that the canonical model
is **incomplete**, and that eight "mechanistic qualifications" should be added
to it.

Those eight are where the review has to do its work, and they do not hold up
evenly.

## The one that holds

**Inflammasome activation is real in Tangier patients.** PMID:29588315 reports
that patients with Tangier disease carrying ABCA1 loss-of-function mutations and
increased myeloid cholesterol content showed a marked increase in plasma IL-1β
and IL-18 levels. That is a case-control human measurement, in the right
disease, in the stated direction, and the KB had it only as an evidence item
hanging off the hypothesis rather than as a mechanism step. It is now a
pathophysiology node.

## The ones that shrink on inspection

**Sphingosine-1-phosphate.** The report treats S1P depletion as a parallel
mechanism contributing to vascular and neurological disease. Reading
PMID:37601634 closely, the human and S1P limbs are different experiments: total
sphingolipids were drastically reduced in *one* Tangier patient, and S1P and
apoM were reduced in *hepatocyte-specific knockout mice*. No S1P value has been
reported for any person with Tangier disease. The onward step to vascular or
neurological injury is untested in either species.

**PMP22-ABCA1 in Schwann cells.** PMID:38979632 is a review about PMP22 in
Charcot-Marie-Tooth disease whose own framing is "emerging evidence" and "we
examine roles for interactions between PMP22 and ABCA1 in cholesterol efflux".
PMID:41750400 is a 2026 review that states outright that ABCA1's role has not
been investigated broadly in peripheral nerves. The evidence runs from PMP22
mutation to cholesterol mislocalization, which is the CMT direction, not from
ABCA1 loss. Calling this "a mechanistic explanation for why neuropathy is such a
prominent feature of TD" is provider inference.

**Haematopoietic progenitor myeloproliferation.** PMID:29905812 is two mouse
models of rheumatoid arthritis in which systemic inflammation is the cause and
efflux-gene downregulation the consequence. Germline ABCA1 loss inverts that
ordering and has no inflammatory trigger. The report is candid about this in its
Alternative Models section but drops the caveat in Finding 15 and in the
Executive Judgment.

**Platelets.** The observation is good: reduced dense bodies, Chediak-Higashi-like
giant granules, and an agonist-selective activation defect in Tangier platelets
(PMID:15163665). The mechanism the report attaches to it is not — it proposes
"ABCA1's role in intracellular membrane cholesterol distribution affecting
granule biogenesis", while the same abstract reports that collagen-induced
changes in phosphatidylserine and cholesterol distribution were *unaltered*.

## Errors worth naming

- **A misquantified effect size.** The report states a "67% CVD risk reduction
  per SD efflux capacity". PMID:25404125 reports 67% for the **highest versus
  lowest quartile** (HR 0.33, 95% CI 0.19–0.55). Restating a quartile contrast
  per standard deviation materially inflates it. The qualitative point — efflux
  capacity tracks risk where HDL-C does not — survives; the number does not.
  It is also a general-population cohort, so it says nothing directly about
  Tangier disease.
- **A misattributed descriptor.** Finding 1 credits PMID:12615679 with "severe
  HDL deficiency, xanthomatosis, and foam cell accumulation". That abstract
  mentions only reductions in apolipoprotein B and apolipoprotein AI. The
  xanthomatosis and foam-cell observations are PMID:11950702's.
- **Two bad candidate CURIEs.** `GO:0097530` is *granulocyte migration*, not
  NLRP3 inflammasome complex assembly (that is `GO:0044546`, already cached
  here). `CL:0000556` is offered as "megakaryocyte/platelet" but is
  megakaryocyte only; platelet is `CL:0000233`. Both were re-derived from the
  caches before use.
- **Five declared figure artifacts do not exist.** The report embeds
  `causal_chain_diagram.png`, `evidence_matrix.png`,
  `evidence_landscape_summary.png`, `knowledge_gaps_table.png` and
  `alternative_models_comparison.png` as placeholders. The hypothesis directory
  contains only the report and its citations sidecar; there is no
  `openscientist_artifacts/` bundle. The prompt calls these "important
  provenance for hypothesis-level review", so this is a provenance defect.
- **Every negative search is unauditable.** "No published evidence was found
  that refutes ABCA1 as the sole causative gene... despite systematic literature
  searches across 134 papers", the ClinicalTrials.gov null, and the GenCC null
  all arrive without query strings, dates, or logs. The conclusions are probably
  right; the searches cannot be repeated.

## One negative claim that does check out

Gap 7 asserts that no ClinGen or GenCC gene-disease validity classification
exists for ABCA1-Tangier disease. Against this repository's pinned ClinGen
snapshot (`cache/clingen/gene_validity.csv`, 2026-08-13 per
`data/clingen/MANIFEST.yaml`), that holds: the file carries ABCA3 and ABCA4
assertions and no ABCA1 (`hgnc:29`) row. Worth flagging because the same claim
made by an OpenScientist report for HMGCS2 deficiency was found to be wrong.

## Integration into the disease YAML

All changes are in `kb/disorders/Tangier_Disease.yaml`.

**Added — new pathophysiology node `Myeloid Inflammasome Activation`**
(`CELLULAR`; macrophage `CL:0000235`, neutrophil `CL:0000775`; `GO:0044546`,
`GO:0032611`, `GO:0140645`, all INCREASED). Incoming `DIRECT` edge from
`Cholesteryl Ester Tissue Storage`; outgoing
`INDIRECT_KNOWN_INTERMEDIATES` edge to `Accelerated atherosclerosis` naming
caspase-1 cleavage and plaque NETosis as intermediates. Human evidence
(PMID:29588315) is graded `HUMAN_CLINICAL`; every downstream limb is graded
`MODEL_ORGANISM` or `IN_VITRO` so the mouse/human boundary stays visible in the
node itself.

**Added — new pathophysiology node `Platelet Dense Granule Maturation Defect`**
(`CELLULAR`; platelet `CL:0000233`), downstream of `ABCA1 Dysfunction`, feeding
two new phenotypes: `Reduced platelet dense granules` (`HP:0033535`) and
`Abnormal platelet function` (`HP:0011869`). All evidence is PMID:15163665,
`HUMAN_CLINICAL`. The node description explicitly records that cholesterol and
phosphatidylserine redistribution were measured and found unaltered, so the
mechanism the report proposed cannot be reintroduced later by inference.

**Added — six `discussions:` entries** (the file previously had none):
`td_genotype_neuropathy_subtype_gap`, `td_s1p_signaling_contribution_gap`
(+ proposed sphingolipidomic experiment), `td_hspc_myeloproliferation_human_gap`
(`HUMAN_MODEL_MISMATCH`, + proposed HSPC experiment),
`td_inflammasome_netosis_human_translation_gap` (`HUMAN_MODEL_MISMATCH`, +
proposed biomarker panel), `td_compound_heterozygote_penetrance_gap`, and
`td_no_interventional_trial_evidence_gap`. This is where the report's Gaps 1-6,
Alternative Models B and D, and Discriminating Tests 2, 3 and 5 land. The S1P,
PMP22 and HSPC arms are curated as open questions rather than mechanism nodes
because that is what their evidence supports.

**Qualified — the `mechanistic_hypotheses` `notes:` block.** It previously
recited the report's eight qualifications without comment. A paragraph now
records which of them are human-grounded, which are mouse-only or cross-disease,
and the PMID:25404125 misquantification, and points at this assessment.

**Deliberately not changed:**

- `status: CANONICAL` stays. The report's own Candidate Status Change says
  retain, and nothing here argues otherwise.
- **No new `mechanistic_hypotheses` entries.** The report proposes three
  sub-hypotheses (inflammasome, S1P, PMP22). A `mechanistic_hypotheses` entry
  asserts a competing or complementary model of the disease; on one plasma
  cytokine study, zero human S1P measurements and two CMT reviews, none has
  earned that.
- **PMID:25404125 not added as evidence.** Dallas Heart Study is a
  general-population cohort with no Tangier participants. Adding it to this
  entry would be Named Entity Confusion reached through a real paper.
- **Miglustat not added as a treatment.** One patient, treated under a mistaken
  Niemann-Pick C diagnosis, with no proposed mechanism. The on-off-on rechallenge
  is genuinely informative for an n of 1, so it is recorded in
  `td_no_interventional_trial_evidence_gap` instead, with the reason for the
  omission written into that entry's `notes`.
- **`GO:0034375`, `GO:0097530` and `CL:0000556` not used** — the first is not in
  this repository's caches, the other two name different concepts than the report
  claims.
- **The existing hypothesis-level evidence items were left alone.** PMIDs
  28602350, 40617357, 20418488, 12771001, 29588315, 37601634, 38979632, 11950702
  and 29582519 were already integrated from this report in an earlier pass and
  all nine snippets still verify.

Verification after the edits: 140/140 snippets verified, and
`check-entity-refs`, `check-causal-targets`, `check-duplicate-keys`,
`check-enum-values`, `check-qualifier-terms`, `check-snippet-grading`,
`check-snippet-length` and `check-title-snippets` all pass.
