# Keratoconus — Claude Code literature sweep

**Disease:** Keratoconus (`MONDO:0015486`, `HP:0000563`)
**KB entry:** `kb/disorders/Keratoconus.yaml`
**Provider:** Claude Code literature sweep (PubMed E-utilities, `esearch` + `esummary`)
**Run date:** 2026-07-31
**Context:** PR #7128, review item 🟡 #3 ("no deep-research artifact for a new entry")

## Method

No third-party deep-research provider (Falcon / Asta / OpenScientist / Perplexity) was
available in this runner, so this is a Claude Code literature sweep rather than a DR
provider report. Ten independent PubMed queries were issued, one per coverage axis, each
retrieving the top 6 relevance-ranked hits. This is a **multi-modal sweep** — each axis is
blind to what the others surface, which is what makes it a coverage audit rather than a
single-query snapshot.

Because the axes were chosen to probe the specific coverage gaps the PR review named
(phenotypes, histopathology, comorbidities, clinical trials, genetics depth), a
"nothing new" result on an axis is itself a finding.

**Provenance discipline.** Every PMID below came back from a live PubMed query — none was
recalled from model memory. Every PMID that was *mined into the KB entry* was first cached
with `just fetch-reference`, and every snippet was verified as an exact
whitespace-normalized substring of that cache before commit. Titles for PMIDs that were
surfaced but **not** mined are reproduced from the `esummary` payload and have **not** been
independently re-verified — treat them as leads, per the CLAUDE.md DR guidance.

### Queries

| Axis | PubMed query |
|---|---|
| biomechanics | `keratoconus AND corneal biomechanics AND (review[pt])` |
| tear proteomics / inflammation | `keratoconus AND (tear OR proteomic) AND (cytokine OR MMP OR inflammation)` |
| atopy / eye rubbing | `keratoconus AND (eye rubbing OR atopy OR allergic conjunctivitis)` |
| comorbidity | `keratoconus AND (comorbidity OR association) AND (sleep apnea OR Down syndrome OR connective tissue)` |
| hydrops management | `acute corneal hydrops keratoconus management` |
| keratoplasty outcomes | `keratoconus AND (keratoplasty OR DALK OR penetrating) AND outcomes` |
| cross-linking evidence | `corneal collagen crosslinking keratoconus AND (randomized OR meta-analysis)` |
| progression definition | `keratoconus progression definition criteria` |
| pediatric | `pediatric keratoconus progression` |
| genetics | `keratoconus genetics AND (GWAS OR polygenic risk score)` |

## Findings acted on in this PR

Four sweep hits were material enough to mine into the entry. All four were cached with
`just fetch-reference` and their snippets verified.

### 1. `PMID:42228627` — Global Consensus on Keratoconus and Ectatic Diseases, Edition 2 (Cornea, 2026)

**The most consequential finding of the sweep.** The entry cited the 2015 first edition
(`PMID:25738235`). Edition 2 was published 2026-07 and supersedes it: 128 ophthalmologists
from 6 continents and 12 international societies, 4 Delphi rounds, covering definition,
diagnosis, **staging**, and progression criteria. Curating a brand-new entry against a
superseded consensus would have been a real defect.

→ Mined into `diagnosis` as the current framework, with the 2015 edition **retained**
(not replaced) because it is the consensus underlying most of the intervening literature
this entry cites.

### 2. `PMID:37374145` — Systemic Associations with Keratoconus (Life, 2023)

Directly addresses the review's `comorbidities` gap. Names atopy, Down syndrome and
connective tissue disease as the most frequently cited associations, and reports diabetes
mellitus as a candidate **protective** factor.

→ Mined as a `KNOWLEDGE_GAP` discussion (`gap_kc_systemic_associations`) rather than as
comorbidity assertions. Reasoning: the three "positive" associations are not
mechanistically equivalent — the atopy association is plausibly mediated *entirely* by
itch-driven eye rubbing (already modelled as both an environmental factor and a
pathophysiology node), so asserting it as an independent comorbidity would double-count a
single causal pathway. The review itself states the mechanisms "are largely unknown". The
gap carries two proposed experiments (rubbing-adjusted mediation analysis; MR for the
diabetes inverse association) that would resolve which pairs deserve `kb/comorbidities/`
entries.

### 3. `PMID:33649486` full text (already cached) — per-gene GWAS mining

Not a new PMID, but the sweep's genetics axis prompted a re-read of the cached **full
text** (not just the abstract) of the multi-ethnic GWAS. Review item 🟡 #4 was correct that
this source was under-mined: it supports named per-gene records with quotable association
statistics.

→ Added `COL12A1` (strongest coding signal: rs35523808 p.Glu2160Val, and collagen XII
localises to Bowman's layer — connecting the locus directly to the "Anterior Limiting
Membrane Rupture" node), `FNDC3B`, `ZNF469`, `ALDH3A1`, `ITGA2`; and added genuine
association evidence (Table 1 rows) to the pre-existing `COL5A1` and `LOX` records.

The LOX/VSX1 typing inconsistency the review flagged is resolved by this: `LOX` now rests
on a genome-wide significant association (rs840464) plus an eQTL effect on its own
transcription, whereas `VSX1` still rests only on the shared "analysed markers" sentence —
so `SUSCEPTIBILITY` vs `DISPUTED` no longer rest on the same evidence.

### 4. `HP:6001232` Corneal iron line / `HP:0012040` Corneal stromal edema

Not literature, but found while closing the phenotype gap: HPO *does* have a term for the
Fleischer ring (`HP:6001232`, whose own definition names keratoconus as a typical setting)
and for the stromal oedema of acute hydrops (`HP:0012040`). Both verified present in the
local `sqlite:obo:hp` adapter.

→ Both added as phenotypes; a `histopathology` section was added for stromal thinning,
Bowman's-layer breaks and epithelial basement-membrane iron deposition (all unbound —
NCIT has no corneal morphologic finding terms for these).

## Findings NOT acted on, and why

Recording these explicitly so the next curator does not re-run the same searches.

| Lead | Axis | Why deferred |
|---|---|---|
| ~~`PMID:39448666` Keratoconus (Nat Rev Dis Primers, 2024)~~ | atopy/rubbing | **Now mined** (round 3) — supplied the UV-light-exposure and contact-lens-wear `environmental:` records. |
| ~~`PMID:38830186` The Pathophysiology of Keratoconus (Cornea, 2025)~~ | biomechanics | **Now mined** (round 3) — supplied two new pathophysiology nodes (`Corneal Oxidative Stress`, `Keratocyte Apoptosis`), a biomechanical-primacy evidence item, and two REFUTE items strengthening the inflammatory-status controversy. |
| ~~`PMID:39535071` polygenic risk score (Hum Mol Genet, 2025)~~ | genetics | **Now mined** (round 3) — added as two evidence items on the `Polygenic susceptibility architecture` genetic record. The cohort ambiguity flagged here was handled by quoting the biobank by name in each snippet (EstBB OR 2.28; UKB AUC 0.84→0.88) rather than stating a bare AUC. |
| ~~`PMID:39671084` Definition of Progressive Keratoconus: systematic review (Cornea, 2025)~~ | progression | **Now mined** (round 3) — supplied a "Documented progression (the cross-linking indication)" `progression:` record; typed the lack-of-unified-criteria conclusion PARTIAL, and cross-referenced the Edition 2 consensus in the diagnosis section rather than presenting it as superseded. |
| `PMID:39681212` Corneal cross-linking (Prog Retin Eye Res, 2025); `PMID:37938377` epi-on vs epi-off meta-analysis; `PMID:36094374` oxygen in CXL | CXL evidence | The entry's CXL treatment is already evidenced. These would deepen protocol-level detail, which is below the abstraction level this KB curates. |
| `PMID:39943883` PK vs DALK meta-analysis (27,018 eyes); `PMID:27802912` | keratoplasty | Would support a surgical-outcomes elaboration of the existing keratoplasty treatment. Not a mechanism claim. |
| `PMID:38317314` Management of acute corneal hydrops (2024) | hydrops | Management-level; the hydrops *mechanism* is already curated from `PMID:24491416` and was split into two atomic nodes in this PR. |
| `PMID:37227479` Ocular manifestations of OSA meta-analysis | comorbidity | A genuine candidate comorbidity (OSA-keratoconus) not covered by `PMID:37374145`. Left as a lead; it belongs in the systemic-associations gap discussion's scope. |
| `PMID:33463562`, `PMID:39396644`, `PMID:36973341` pediatric keratoconus | pediatric | Pediatric-onset keratoconus progresses faster and is a distinct management context. Not curated — the entry does not currently model onset-stratified subtypes, and adding one is a scoping decision beyond this review round. |
| Clinical trials (`clinical_trials` section) | — | **Deliberately not added.** The review suggested an NCT record for the US multicentre CXL trial (`PMID:28495149`). ClinicalTrials.gov queries returned several plausible CXL trials, but none could be confirmed as *that* trial (the closest enrollment/design match, `NCT00567671`, is an Emory **single-site** study — not the multicentre trial). Guessing an NCT here would be exactly the misattribution failure the repository's evidence SOP exists to prevent. Left uncurated pending a verifiable registry link. |

## Coverage assessment after this round

| Section | Before | After |
|---|---|---|
| `phenotypes` | 4 | 6 |
| `histopathology` | absent | 3 findings |
| `genetic` | 5 records, 1 real source | 10 records, GWAS-anchored |
| `diagnosis` | 1 | 2 (current consensus) |
| `discussions` | 2 | 3 |
| `comorbidities` (separate files) | absent | still absent — deliberately, see above |
| `clinical_trials` | absent | still absent — deliberately, see above |

## Round 3 — mining pass over cached-but-unconsumed references

Prompted by the second PR review, which flagged that four references shipped in
`references_cache/` in this PR were consumed by zero evidence items. All four are now
mined; no new literature search was run and no new cache files were fetched.

| Section | After round 2 | After round 3 |
|---|---|---|
| `pathophysiology` | 12 nodes | 14 nodes (`Corneal Oxidative Stress`, `Keratocyte Apoptosis`) |
| `environmental` | 2 | 4 (UV exposure, contact lens wear) |
| `progression` | 1 record | 2 records (progression definition / CXL indication) |
| `genetic` evidence on the polygenic record | 1 item | 3 items (PRS validation in two biobanks) |
| verified snippets | 73/73 | 85/85 |
| cached-but-unconsumed references | 4 | 0 |

Both new pathophysiology nodes carry a `notes:` stating which upstream edge was
deliberately *not* asserted and why — the source reports oxidative stress and keratocyte
apoptosis without establishing what drives either, and "along with" is co-observation, not
causation. The `Anterior Limiting Membrane Rupture` → `Loss of Corneal Biomechanical
Rigidity` edge was also recalibrated from `DIRECT` to `INDIRECT_UNKNOWN_INTERMEDIATES`
(review suggestion 2): the snippets establish the lesion histopathologically, not its
biomechanical consequence, and Bowman's layer is ablated wholesale in PRK without
inducing ectasia.

## Open follow-ups worth issues

1. **`keratoconus_corneal_ectasia` mechanism module.** Keratoconus carries both an HP and a MONDO id and is used as a *phenotype* by at least five other entries (`Ehlers-Danlos_Syndrome`, `Arterial_Tortuosity_Syndrome`, `Spondylodysplastic_Ehlers-Danlos_Syndrome`, `CRB1_Retinal_Dystrophies`, `GUCY2D-Related_Retinopathy`). That is the "disease-like phenotype" pattern that glaucoma, cataract and osteoporosis each model as a disorder entry *plus* a `kb/modules/` module. Raised by the PR reviewer (suggestion 13) and endorsed here.
2. **MAXO NTR for corneal collagen cross-linking.** Neither MAXO nor NCIT codes CXL; the entry uses `NCIT:C15301` Phototherapy + `CHEBI:17015` riboflavin as an interim composition.
3. **OSA-keratoconus** (`PMID:37227479`) as a candidate comorbidity pair.
