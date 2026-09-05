# Spatially resolved in vitro tissue models: a curation pass and a schema gap (2026-09-02)

**Date:** 2026-09-02
**Source:** Brenden CK, Williams JT, Rivas D, Forro C, Choi S. *Spatiotemporal instrumentation of in vitro tissues: Toward understanding human disease.* Cell Biomaterials (2026). [DOI:10.1016/j.celbio.2026.100576](https://doi.org/10.1016/j.celbio.2026.100576)
**Scope:** What this perspective's argument and citation list yield for dismech's `experimental_models` section.
**Purpose:** Record one curation tranche against `Myocardial_Infarction`, and the schema limitation the exercise exposed.

## The source is a lead-generator, not a citable reference

The perspective is in press and **not indexed in PubMed** (title search returns
zero hits), so it has no PMID. `just fetch-reference doi:10.1016/j.celbio.2026.100576`
succeeds but returns `content_type: unavailable` — a header-only cache entry with
no body. Nothing in it can be quoted as a validated `snippet`, and no evidence item
in this pass cites it.

That is the correct outcome rather than a problem to work around. It is a
perspective: its value here is its citation list and its argument, both of which
point at primary experimental papers that *are* indexed and *do* have abstracts.
Those are what got curated. Where the perspective's framing is used in the KB it
appears in a `notes:` field as provenance, never as evidence.

## What the perspective argues

Two claims are load-bearing for dismech.

**A spatially uniform disease stimulus is a different experiment from a spatially
graded one.** The paper's recurring example is myocardial infarction: uniform
hypoxia shifts a whole construct into a disease state, but the actual lesion is
an interface between injured and viable tissue. Models that engineer a gradient
reproduce phenotypes that uniform models do not. This is an empirical claim, and
the primary papers below test it directly.

**Endpoint assays lose the phenomenon.** Cytokine dynamics, action-potential
morphology and contractile mechanics change on timescales that fixed-timepoint
immunoassays cannot resolve, which motivates the instrumented-tissue programme the
paper is arguing for.

## Curation output

Five models added as an `experimental_models` block on `kb/disorders/Myocardial_Infarction.yaml`,
which previously had none. All were selected because pathology is spatially graded
*within* the construct, which is the property the perspective is about.

| PMID | Model | Type | Links → node | Fidelity |
|---|---|---|---|---|
| 32284552 | Cardiac infarct organoid with an internal oxygen-diffusion gradient | `ORGANOID` | `Myocardial Ischemia and Cardiomyocyte Death` (RECAPITULATES); `Cardiac Fibrosis and Ventricular Remodeling` (PARTIALLY_RECAPITULATES) | MODERATE |
| 36475790 | Myocardial infarct border-zone-on-a-chip | `ORGAN_ON_CHIP` | `Myocardial Ischemia and Cardiomyocyte Death` (PARTIALLY_RECAPITULATES); `Post-Infarction Inflammation and Cardiac Repair` (PARTIALLY_RECAPITULATES) | MODERATE / LOW |
| 33055246 | Human heart-on-a-chip IRI assay with endothelial EV rescue | `ORGAN_ON_CHIP` | `Ischemia-Reperfusion Injury` (RECAPITULATES) | MODERATE |
| 32092276 | Bioelectronically instrumented heart-on-a-chip under acute hypoxia | `ORGAN_ON_CHIP` | `Myocardial Ischemia and Cardiomyocyte Death` (PARTIALLY_RECAPITULATES) | LOW |
| 38683053 | Epicardial-myocardial Biowire II heart-on-a-chip | `ORGAN_ON_CHIP` | `Ischemia-Reperfusion Injury` (PARTIALLY_RECAPITULATES); `Cardiac Fibrosis and Ventricular Remodeling` (PARTIALLY_RECAPITULATES) | MODERATE |

Eight `modeled_mechanisms` links against four of the entry's five existing
pathophysiology nodes, with 11 evidence-backed readouts. Every snippet was checked
as an exact substring of its cached reference *before* being written, not after.
All eight links carry `model_scale` and typed `divergences` (see below).

Two gradings are worth flagging because they are the ones a reviewer would
challenge:

**PMID:32092276 is graded `LOW` fidelity and kept anyway.** Its cells are HL-1, an
immortalized *murine atrial* line — wrong species and wrong chamber for human
ventricular myocardium. It earns its place because the instrumentation is the
contribution: multiplexed extra- and intracellular electrodes give a continuous
time course through the ischemic insult, showing tachycardia resolving into
bradycardia and then arrhythmia. No other model in the entry produces that. The
`limitations` field says so explicitly, and a `notes:` field records why the record
was retained despite the cell source.

**PMID:36475790's inflammation link is graded `LOW`, not `MODERATE`.** The chip
raises inflammatory-cascade expression under a gradient with no leukocytes present,
which is a real and interesting result — but `Post-Infarction Inflammation and
Cardiac Repair` is a node about neutrophil and monocyte recruitment, efferocytosis,
and the inflammatory-to-reparative transition. The model reaches the cardiac-tissue
half of that and none of the cellular half.

## Not curated, and why

| Candidate | Disposition |
|---|---|
| Basara et al. 2024, 3D bioprinted aged post-infarct myocardium (perspective ref 29) | Plausible sixth MI model. Identified from the reference list, **not assessed** this pass — not fetched, not read. |
| Yamasaki et al. 2021, bioengineered cardiac tissue in hypoxia/re-oxygenation (ref 20) | Same: identified, not assessed. |
| Lin et al. 2023, stretchable nanoelectronics in cardiac microtissues (ref 26) | Not a disease model. It studies electrical *maturation* of healthy microtissue, so it has no pathophysiology node to link to. |
| Kim et al. 2023, iPSC-CM arrhythmogenic cardiomyopathy (ref 39) | Relevant to `Arrhythmogenic_Right_Ventricular_Cardiomyopathy`, not to MI. Out of scope for this entry. |
| Kim et al. 2016, gut-on-a-chip inflammation (ref 22) | Belongs to the IBD/barrier work already tracked in `projects/NAMO_RD_MODELS.md`. |
| Yang et al. 2024, Kirigami electronics for neural organoids (ref 84) | Instrumentation method, no disease claim. |

The unassessed rows are recorded as unassessed deliberately. Reading a title in a
reference list is not evidence about a paper, and the distinction matters more here
than usual because the whole point of the exercise was evidence discipline.

## What the schema does and does not carry

**Correction to an earlier draft of this report.** It claimed that an exhaustive
search of the schema found no slot for the measurement context these models need.
That was wrong by the time it was written. `model_scale` and `divergences` had
already landed on `ModelMechanismLink`, between this branch's original base and
the `main` it was rebased onto, and the survey behind the claim was run against
the older base and never re-run. Both slots are now populated on all eight links
in this pass. What follows is the corrected position.

### What the new slots do cover

`model_scale` (`BiologicalScaleEnum`) records the scale a model actually
*observes*, so a scale gap against the target node's `biological_scale` is
computable rather than buried in prose. `divergences` types the caveat that
`limitations` writes as prose, each entry naming a kind, explaining why it applies
here, and grading whether it bears on this link's claim.

Three of the four problems the first draft listed are answered by `divergences`:

| Claim | Now carried as |
|---|---|
| HL-1 is a murine atrial line, not human ventricular myocardium | `SPECIES_MISMATCH`, `INVALIDATING` |
| The border-zone chip's inflammation link has no leukocytes at all | `BOUNDARY_OMISSION`, `INVALIDATING` |
| Its inflammatory readout is transcript abundance standing in for a cellular response | `PROXY_QUANTITY`, `QUALIFYING` |
| Ischemia is imposed by diffusion limit or gas control, not by coronary occlusion | `CAUSE_UNREPRESENTED`, `QUALIFYING` |

That last one is worth flagging: every model in this entry is
`CAUSE_UNREPRESENTED` against a disease whose defining lesion is atherothrombotic,
and the taxonomy makes that queryable across the KB rather than leaving it as a
sentence eight times over.

### What still has nowhere to go

Both new slots describe how a model **falls short**. Neither records positive
metadata about how a measurement was *made*, which is the axis the perspective
argues about. Three things from this pass still survive only as prose:

1. **An internal spatial comparator.** The Richards calcium readout compares
   *interior* to *edge* cardiomyocytes within the same organoid. `model_scale`
   says the model observes cellular state; it cannot say the control is a
   different region of the same construct, which is the methodological point.
   `STRUCTURAL_IDEALIZATION` is the nearest divergence type and is the wrong
   shape — the spatial structure here is the model's strength, not its idealization.
2. **Temporal resolution.** The two-photon light-sheet calcium imaging runs at
   20 ms, which is what makes the arrhythmia visible. It sits in free-text
   `culture_system` next to the culture format. `TEMPORAL_SCOPE` again types a
   mismatch, not a sampling rate.
3. **An unnamed comparator.** `ModelReadoutDirectionEnum` is defined "relative to
   the model's control or comparator arm", yet no slot names that arm. The
   Bannerman cell-death readout is `DECREASED` against *epicardium-free tissue*,
   not against untreated tissue; read without the prose, `DECREASED` is close to
   meaningless. This is the smallest and most tractable of the three, is not
   specific to spatial models, and every one of the KB's readouts inherits it.

The fourth item in the first draft — a non-monotonic beat-rate time course
recorded as `ALTERED` — is a real loss of information but is adequately handled by
`ALTERED` plus `interpretation`, and is withdrawn as a schema concern.

### Two observations that still hold

- **`assays` is defined, OBI-bound, and populated on 0 of 289 readouts.** The slot
  for naming the measurement technique exists and is universally unused. `OBI` is
  absent from `conf/oak_config.yaml` and has no `cache/enums/` membership cache, so
  a curator who tried to use it could not validate it — the disuse is a tooling
  consequence, not curator neglect.
- **230 `modeled_mechanisms` links carry no `relationship` at all**, against 160
  `RECAPITULATES` and 49 `PARTIALLY_RECAPITULATES`. The expressive slots that
  exist are under-populated, which is worth weighing before adding more. The same
  caution applies to the new slots: `just model-scale-audit` reports 1,876 of 1,886
  links as scale-`UNDETERMINED`.

### A follow-on this pass deliberately did not take

The eight links here set `model_scale`, but all eight stay `UNDETERMINED` in
`just model-scale-audit` because no `Myocardial_Infarction` pathophysiology node
carries `biological_scale`. Populating those five nodes would make the comparison
computable and is probably right, but it edits nodes this PR did not author and
that `main` revised independently, so it belongs in its own change.

## Notes for future scans

- **Re-run a schema survey against the base you actually ship on.** The gap section
  of this report was written from a survey run against the branch's original base,
  and by the time it was committed `main` had added `model_scale` and `divergences`
  to the very class it claimed had no such slot. The rebase brought the new schema
  in and silently invalidated the prose. A survey is a claim about repository state
  and rots exactly like a `notes:` sentence does.
- Fetch the reference before believing a perspective's characterization of it.
  The perspective describes PMID:32092276 among cardiac instrumentation advances
  without foregrounding that its cells are murine; that only surfaced on reading
  the abstract, and it changed the fidelity grade from MODERATE to LOW.
- `just fetch-reference` on a DOI succeeds with an empty body. Check
  `content_type:` in the cache header before planning to quote a source —
  `unavailable` means no snippet from it will ever validate.
- The richest existing pattern to copy for an instrumented in vitro model is
  `kb/disorders/High_Altitude_Pulmonary_Edema.yaml` (lung-on-chip with `fidelity`,
  `limitations`, and directional readouts). It also independently hit the gap above,
  carrying "spatially uneven … overperfusion" in free-text `limitations`.
