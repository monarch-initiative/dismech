# Pilot: How much of dismech's evidence could carry a CEBM/GRADE-style level?

_Pilot investigation for issue #5000 ("Add a level-of-evidence / strength tier to
EvidenceItem"), requested by @cmungall in lieu of implementing the field directly.
Generated from a corpus-wide scan of `kb/disorders/*.yaml` and `kb/modules/*.yaml`
plus a live NCBI EFetch query of the MEDLINE `PublicationTypeList` for every
unique PMID cited. Reproduce with `scripts/cebm_pilot_analysis.py`
(see "Reproducing this pilot" below). This is a data-gathering pilot, not a
schema change — no `evidence_level` field has been added anywhere._

## TL;DR

- Only **~2.5% of dismech's PMID-backed evidence** is drawn from a publication
  MEDLINE itself classifies as a systematic review/meta-analysis or RCT. Case
  reports/series (14.9%) alone outnumber SR+RCT+guideline evidence (4.4%) by
  more than 3:1.
- For the specific case cmungall asked about — **pathophysiology assertions**
  — RCT-typed evidence is even rarer: **82 of 17,425 pathophysiology evidence
  items (0.47%)** cite a MEDLINE-tagged RCT, and only 2.26% are SR/RCT/guideline
  combined. This is expected: CEBM/GRADE were built to grade *therapeutic
  intervention* evidence, and pathophysiology nodes mostly cite mechanistic
  observation, not intervention trials. By contrast, in the `treatments`
  section 11.8% of evidence is SR/RCT/guideline-tier, and the dedicated
  `clinical_trials` section is 66.7% RCT — CEBM is a much better fit there.
- **Real examples confirm cmungall's "impeccable source, subjective
  interpretation" worry** — see the ALS/riluzole and celiac/ZED1227 cases
  below. The same RCT PMID backs both a snippet that IS the trial's own novel
  finding and a snippet that is background literature merely repeated in the
  trial's introduction. A per-reference evidence level would misclassify one
  of the two.
- **Published inter-rater-reliability studies exist for both GRADE and
  orthopaedic-journal levels-of-evidence**, and even under much easier
  conditions than dismech's (pre-filtered study designs, trained
  methodologists, whole-article not per-snippet judgments) agreement is only
  moderate-to-substantial (κ 0.44–0.85 depending on domain/experience) — see
  "Existing inter-annotator agreement literature" below. This directly
  informs the #1105 oscillation problem: disagreement is not unique to
  dismech's LLM curators, it's inherent to the task.
- **PubMed already publishes a structured, NLM-curated `PublicationTypeList`**
  field (Randomized Controlled Trial, Meta-Analysis, Systematic Review,
  Practice Guideline, Case Reports, Review, …) that dismech's own reference
  fetcher does not currently capture — it only stores `MeshHeadingList`
  (`src/dismech/schema` consumes `linkml_reference_validator`'s
  `PMIDSource._fetch_mesh_terms`, which ignores the sibling
  `PublicationTypeList` element in the same XML payload it already
  downloads). This is a concrete, low-cost opportunity: ingest an
  externally-curated ranking rather than asking an LLM to re-derive it — see
  "Actionable finding" below.

## Method

`scripts/cebm_pilot_analysis.py`:

1. Recursively walks every `kb/disorders/*.yaml` and `kb/modules/*.yaml`
   (excluding `*.history.yaml`) and collects every dict that looks like an
   `EvidenceItem` (has `reference` + `evidence_source`/`supports`), tagging
   each with the top-level slot it was found under (`pathophysiology`,
   `treatments`, `phenotypes`, `clinical_trials`, …).
2. Filters to `PMID:`-backed items and gets the unique PMID set.
3. Batch-queries `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi`
   (`db=pubmed`, `rettype=xml`, 200 IDs/request, rate-limited to NCBI's
   3 req/s unauthenticated cap) for the real MEDLINE `PublicationTypeList` of
   each PMID, caching results in `research/cebm_pilot_pubtypes_cache.json`.
4. Buckets each PMID's publication types into a coarse CEBM-oriented tier
   (see the script's `LEVEL_1_SR` / `LEVEL_2_RCT` / … constants) and
   cross-tabulates `evidence_source × bucket` and `KB-section × bucket`.

Corpus scanned: 1,568 disorder/module YAML files, 67,967 evidence-item-shaped
nodes, 54,821 (80.7%) PMID-backed, spanning **16,370 unique PMIDs**. NCBI
returned `PublicationTypeList` data for 16,058 of those (98.1%); the
remainder are mostly NCBI Bookshelf records (GeneReviews chapters, which are
indexed as `PubmedBookArticle` rather than `PubmedArticle` and carry no
`PublicationTypeList`) or PMIDs the live query didn't resolve.

**Caveat on the bucketing itself:** this is a coarse pilot mapping, not a
proposed final scheme — e.g. `Review` (narrative review) has no clean home in
either CEBM or GRADE (see "What CEBM doesn't capture well" below), and a
publication can carry multiple `PublicationType` tags simultaneously (e.g. a
paper tagged both `Randomized Controlled Trial` and `Multicenter Study`);
the script takes the highest tier present.

## Headline numbers (all PMID-backed evidence, corpus-wide)

| Bucket | Evidence items | % of PMID-backed | Unique PMIDs |
|---|---:|---:|---:|
| L1 — Systematic review / meta-analysis | 1,394 | 2.54% | 533 |
| L2 — RCT (incl. controlled/pragmatic trial) | 731 | 1.33% | 368 |
| Guideline / consensus | 283 | 0.52% | 77 |
| L3 — Other trial or observational study | 2,509 | 4.58% | 905 |
| L4 — Case report / case series | 8,153 | 14.87% | 2,101 |
| Narrative review (non-systematic) | 15,340 | 27.98% | 4,699 |
| Journal article, no special design tag | 22,178 | 40.46% | 7,279 |
| Non-evidentiary (letter/comment/editorial) | 187 | 0.34% | 96 |
| No `PublicationTypeList` data (Bookshelf, etc.) | 4,046 | 7.38% | 312 |

**SR + RCT + Guideline combined ("classic CEBM top tier"): 2,408 evidence
items = 4.39% of PMID-backed evidence (3.54% of all 67,967 evidence items).**

The remaining ~19.3% of all evidence items (13,146) are not literature
citations at all — `ORPHA:`, `CGGV:`/`CGDS:` (ClinGen), `ICEES:`,
`clinicaltrials:`, `NCIT:`, `CIVIC_*`, `GEO:`/`geo:`, `DOI:` (non-PMID),
`url:`. CEBM/GRADE, which grade individual primary/secondary clinical
studies, don't apply to these directly — they already carry their own
source-native provenance signal (ClinGen's own gene-disease validity
classification tier, Orphanet's expert-review status, a trial's own
`clinicaltrials.gov` phase/status field). Worth a follow-up note in any
`evidence_level` design: for these sources, "ingest the external ranking"
(see below) is the *only* sensible model — there's no paper to re-grade.

## Section breakdown — where does CEBM actually fit?

This is the direct answer to "how many pathograph[y] assertions come from RCTs":

| KB section | Total PMID evidence | SR+RCT+Guideline | RCT only | Case report/series | Narrative review |
|---|---:|---:|---:|---:|---:|
| **pathophysiology** | 17,425 | 394 (2.26%) | 82 (0.47%) | 2,176 (12.49%) | 5,705 (32.74%) |
| phenotypes | 13,629 | 476 (3.49%) | 64 (0.47%) | 2,891 (21.21%) | 3,310 (24.29%) |
| genetic | 4,151 | 119 (2.87%) | 10 (0.24%) | 578 (13.93%) | 827 (19.93%) |
| **treatments** | 6,823 | 803 (11.77%) | 453 (6.64%) | 771 (11.30%) | 2,000 (29.31%) |
| **clinical_trials** | 36 | 24 (66.7%) | 24 (66.7%) | 0 | 0 |
| diagnosis | 1,960 | 73 (3.72%) | 7 (0.36%) | 404 (20.61%) | 440 (22.45%) |
| biochemical | 1,877 | 87 (4.64%) | 33 (1.76%) | 279 (14.87%) | 451 (24.03%) |

The pattern is exactly what CEBM's own design would predict: it's a scheme
for grading *therapeutic intervention* evidence, and it concentrates where
dismech records intervention evidence (`treatments`, `clinical_trials`).
Applying it to `pathophysiology` — the section that carries the plurality of
all evidence (17,425 of 67,967 items, 25.6%) — would leave essentially all of
it (97.7%) bottomed out at CEBM's lowest tier ("Level 5, mechanism-based
reasoning") or unclassifiable, which is not very discriminating for the
evidence type dismech actually depends on most.

## Concrete examples: impeccable source, subjective dismech interpretation

Pulled from the 82 pathophysiology evidence items backed by a MEDLINE-tagged
RCT, then manually checked against the cached abstract:

**1. Amyotrophic Lateral Sclerosis, `PMID:8302340`** (Bensimon et al., the
landmark 1994 riluzole survival RCT — `PublicationType`: `Randomized
Controlled Trial`, `Clinical Trial`):

```yaml
snippet: "Some research suggests that the excitatory amino acid neurotransmitter
           glutamate may be involved in the pathogenesis."
explanation: "Trial of riluzole, an antiglutamate agent, supports role of
              glutamate excitotoxicity in ALS pathogenesis."
supports: PARTIAL
```

The trial's design (RCT, survival endpoint) is about as strong as clinical
evidence gets. But the dismech claim being supported is *mechanistic*
("glutamate excitotoxicity drives pathogenesis"), inferred backward from
drug response — a drug working through target X is suggestive, not
confirmatory, of X's causal role (response could be off-target, or the
target could be downstream of the true driver). **The curator already
encoded this gap via `supports: PARTIAL`, without any `evidence_level`
field** — evidence that `supports` and a future `evidence_level` are doing
different jobs and both matter: `evidence_level` would say "RCT, strong
study design"; `supports: PARTIAL` says "the *inferential leap* from that
RCT's result to this specific mechanistic claim is only partial." A naive
per-reference `evidence_level: HIGH` tag on this item, divorced from
`supports`, would overstate confidence in the mechanistic claim itself.

**2. Celiac Disease, `PMID:38914866`** (Dotsenko et al. 2024, *Nat Immunol* —
the CEC-3 phase-2a randomized placebo-controlled trial of the TG2 inhibitor
ZED1227 — `PublicationType`: `Randomized Controlled Trial`). This single PMID
backs **four** pathophysiology evidence items in the dismech entry, and they
are not equally strong:

- `"Transglutaminase 2 (TG2) plays a pivotal role in the pathogenesis of
  celiac disease... by deamidating dietary gluten peptides"` — this is
  **background/introduction text restating prior literature**, not a new
  finding of this trial (confirmed by reading the full cached abstract:
  `references_cache/PMID_38914866.md`).
- `"ZED1227 treatment preserved transcriptome signatures associated with
  mucosal morphology, inflammation, cell differentiation and nutrient
  absorption to the level of the gluten-free diet group"` — this **is** the
  trial's own novel transcriptomic result.

Both snippets would inherit the identical `Randomized Controlled Trial`
`PublicationType` tag if `evidence_level` were assigned per-reference. Only
the second deserves it; the first is really citing background literature at
one remove. **This is the concrete version of cmungall's worry** —
`evidence_level` has to stay scoped to the individual `EvidenceItem` (which
is what the schema in #5000 already proposes, correctly) and cannot be
safely bulk-assigned from a reference's own publication type without a
human/LLM check on whether the *specific quoted sentence* is the paper's own
finding or borrowed context.

## Existing inter-annotator agreement literature

Two real, checked studies bear directly on the #1105 oscillation problem
(disagreement isn't a dismech-specific defect — it's intrinsic to this kind
of classification):

- **Hartling L, Fernandes RM, Seida J, Vandermeer B, Dryden DM. "From the
  Trenches: A Cross-Sectional Study Applying the GRADE Tool in Systematic
  Reviews of Healthcare Interventions." *PLOS ONE* 2012.**
  ([PMC3320617](https://pmc.ncbi.nlm.nih.gov/articles/PMC3320617/)) — two
  trained methodologists independently GRADE-rated evidence for clinically
  important outcomes across three systematic reviews. Inter-rater κ ranged
  from 0.18 (precision — poor) to 0.84 (consistency — near-perfect), with
  **overall quality-of-evidence κ = 0.44 (only moderate)**, even between
  trained raters doing the much narrower job of grading an already-conducted
  systematic review's outcomes (not raw individual papers, and not
  mechanistic claims).
- **Obremskey WT, Pappas N, Attallah-Wasif E, Tornetta P 3rd, Bhandari M.
  "Level of evidence in orthopaedic journals." *J Bone Joint Surg Am.*
  2005;87(12):2632-2638.** ([PMID:16322612](https://pubmed.ncbi.nlm.nih.gov/16322612/))
  — 382 clinical articles, rated Level I–IV by 3 experienced + 2 inexperienced
  reviewers using the JBJS-A scheme (a close cousin of CEBM). κ = 0.62
  (level of evidence) / 0.76 (study type) between experienced and
  inexperienced reviewers; κ = 0.75 / 0.85 between experienced reviewers only;
  κ = 0.84 / 1.00 against the journal's own gold-standard grade. **Crucially,
  this study pre-excluded** animal/cadaver studies, basic-science articles,
  review articles, case reports, and expert opinion — i.e., it only tested
  agreement on the subset of literature CEBM/JBJS-A levels were built for.

**Implication for dismech:** even in a much friendlier setting than dismech's
(single per-article grade rather than per-snippet/per-claim, expert human
raters rather than an LLM, and — in the orthopaedic study — a pre-filtered
set that already excludes the review articles, case reports, and mechanistic
papers that make up ~73% of dismech's `pathophysiology` evidence), agreement
tops out around "substantial" (κ ~0.75–0.85), not "near-perfect." No
published study was found that measures agreement on the *specific* judgment
dismech needs: given one quoted snippet supporting one specific mechanistic
edge, what CEBM/GRADE tier applies. That task is likely *harder* than either
study above, because it also requires the "is this snippet the paper's own
finding or borrowed background" distinction from the celiac-disease example.
This argues for treating any curation-LLM-assigned `evidence_level` as
provisional/advisory rather than authoritative, at least initially — possibly
with a lower confidence bar than other structured curation fields, and a
compliance/QC pass analogous to `linkml-reference-validator`'s snippet check.

## What CEBM doesn't capture well

Two real gaps surfaced by this corpus, beyond what issue #5000 already flags:

1. **Narrative (non-systematic) reviews are 28% of all PMID-backed evidence**
   and CEBM 2011 has no clean tier for them — they're not "systematic review
   of RCTs" (Level 1), and calling them "Level 5 mechanism-based reasoning"
   undersells a review that synthesizes a large primary literature (e.g. a
   GeneReviews-style clinical overview) versus one author's speculative
   mechanistic hypothesis, which really are both "Level 5" under CEBM's
   letter. GRADE has the same blind spot (it grades *primary* study evidence
   feeding into a specific recommendation, not narrative synthesis).
2. **`JOURNAL_ARTICLE_UNCLASSIFIED` (40.5%) is dismech's largest single
   bucket** — case series too small to be coded `Case Reports`, small
   cohort/mechanistic-observation papers, etc. This is exactly the tier the
   original issue's Option A (GRADE) buckets as `VERY_LOW`/`LOW` without
   further distinction, which may be too coarse: a 200-patient mechanistic
   cohort study and a 1-family linkage study both land here today.

These reinforce the issue's own Option C instinct (a dismech-native scheme)
for the *pathophysiology-heavy* majority of the corpus, while Option A/B
(GRADE/CEBM proper) look like a strong, low-friction fit specifically for the
`treatments`/`clinical_trials` sections where intervention evidence actually
concentrates.

## Actionable finding: an external ranking already exists — dismech just isn't ingesting it

cmungall's third question — "*maybe there is separate ranking of the
references from external sources and we just ingest these?*" — has a
concrete, immediately actionable answer: **yes, for the RCT/SR/guideline
axis specifically.**

PubMed's MEDLINE `PublicationTypeList` (NLM-indexer-curated, not
author-self-reported, not LLM-derived) already answers "is this an RCT /
meta-analysis / systematic review / practice guideline?" with the same
`Entrez.efetch(db="pubmed", rettype="xml")` call dismech's reference fetcher
already makes for every PMID. But
`linkml_reference_validator.etl.sources.pmid.PMIDSource._fetch_mesh_terms`
(the function `just fetch-reference` uses) only extracts `MeshHeadingList`
from that XML and discards the sibling `PublicationTypeList` element —
confirmed by inspecting the installed package
(`.venv/lib/python3.12/site-packages/linkml_reference_validator/etl/sources/pmid.py`).
**A false-friend caution surfaced in this pilot:** naively grepping the MeSH
`keywords` already cached in `references_cache/*.md` for RCT-like terms is
*not* a safe substitute — `PMID:10693687` carries the MeSH heading
"Randomized Controlled Trials as Topic" (the paper *discusses* RCT
methodology) while its real `PublicationType` is plain "Journal Article";
MeSH topic headings and PublicationType tags are different NLM fields that
happen to share vocabulary.

This suggests a two-tier design for the eventual `evidence_level` schema
work: (1) a **deterministic, externally-sourced signal** — capture
`PublicationTypeList` in the reference cache (e.g. a `publication_types:`
frontmatter field alongside the existing `keywords:`), and let tooling
auto-suggest `HIGH`/L1–L2 for RCT/SR/meta-analysis/guideline tags — vs.
(2) the **subjective per-snippet judgment** (mechanistic-inference strength,
background-vs-finding distinction) that the ALS and celiac examples show
must stay a curator/LLM call, never auto-derived from the reference alone.
Implementing (1) is a small, self-contained change to
`src/dismech/reference_cache_frontmatter.py` / the `just fetch-reference`
pipeline and would give dismech an auto-suggested floor for `evidence_level`
on ~4.4% of PMID evidence (the SR/RCT/guideline tier) with essentially no
hallucination risk, before any LLM judgment is asked to do the harder
(2)-type work for the rest.

## Open questions for the schema-design follow-up (not answered by this pilot)

- Should `evidence_level` be required to be internally consistent with
  `supports`, or are they allowed to diverge the way the riluzole example
  does (`PARTIAL` support from what would nominally be `HIGH`-level design)?
- For the ~19.3% of evidence that isn't a PMID at all (ORPHA/ClinGen/ICEES/
  clinicaltrials/etc.), should `evidence_level` be left absent, or should each
  structured source define its own mapping (e.g. ClinGen's own validity
  classification tiers)?
- Given the IRR literature above, should a first `evidence_level` rollout be
  scoped to `treatments`/`clinical_trials` only (where the scheme fits well
  and reliability precedent is closest to this pilot's citations), leaving
  `pathophysiology`/mechanistic evidence for a later, possibly
  dismech-native, scheme?

## Reproducing this pilot

```bash
# Full corpus + live NCBI query (~3-4 min, respects NCBI's 3 req/s unauthenticated cap)
uv run python scripts/cebm_pilot_analysis.py --out research/cebm_pilot_data.json

# Reruns reuse research/cebm_pilot_pubtypes_cache.json and only fetch new/uncached PMIDs
uv run python scripts/cebm_pilot_analysis.py --sample 400   # fast dev run
```

Outputs: `research/cebm_pilot_data.json` (summary cross-tabs) and
`research/cebm_pilot_pubtypes_cache.json` (raw `pmid -> [PublicationType,...]`,
committed so the numbers above are reproducible without re-querying NCBI).
