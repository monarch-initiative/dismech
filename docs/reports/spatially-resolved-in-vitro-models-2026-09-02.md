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

## The schema gap this exposed

**dismech can say that a measurement was made and which way it went. It cannot say
where in the tissue, how often, with what instrument, or against which comparator.**
That is precisely the axis the perspective argues is what makes an in vitro model
informative, and writing the block above ran into it four times.

`ExperimentalReadout` carries `name`, `description`, `target`, `phenotype_term`,
`biomarker_term`, `biological_processes`, `assays`, `direction`, `interpretation`,
`evidence`, `notes`. An exhaustive search of `src/dismech/schema/dismech.yaml` for
spatial, temporal, sensor, instrument, sampling, coordinate and heterogeneity
vocabulary finds no slot on this path. The nearest analogues both belong elsewhere:
`spatial_extent` (`SpatialExtentEnum`: FOCAL, MULTIFOCAL, DIFFUSE, …) is a coarse
qualifier on a phenotype descriptor, and `platform` belongs to `Dataset`.

Four concrete claims from this pass that the schema forced into prose:

1. **An internal spatial comparator.** The Richards calcium readout compares
   *interior* to *edge* cardiomyocytes within the same organoid. That the control is
   internal is the methodological point of the model, and it survives only as a
   sentence in `interpretation`.
2. **Temporal resolution.** The two-photon light-sheet calcium imaging runs at 20 ms
   resolution, which is what makes the arrhythmia visible at all. It is recorded in
   free-text `culture_system`, alongside the culture format, because there is
   nowhere else.
3. **A non-monotonic time course.** The bioelectronic chip's beat rate rises, then
   falls, then becomes arrhythmic. `direction` is single-valued, so this is
   `ALTERED` plus prose — accurate, but it discards the ordering that was the result.
4. **An unnamed comparator.** `ModelReadoutDirectionEnum` is defined "relative to the
   model's control or comparator arm", yet no slot names that arm. The Bannerman
   cell-death readout is `DECREASED` against *epicardium-free tissue*, not against
   untreated tissue; read without the prose, `DECREASED` is close to meaningless.

Item 4 is the smallest and most tractable of these, and is not specific to spatial
models: every one of the 289 readouts in `kb/` inherits it.

Two supporting observations, both from a full parse of `kb/`:

- **`assays` is defined, OBI-bound, and populated on 0 of 289 readouts.** The slot
  for naming the measurement technique exists and is universally unused. `OBI` is
  absent from `conf/oak_config.yaml` and has no `cache/enums/` membership cache, so
  a curator who tried to use it could not validate it — the disuse is a tooling
  consequence, not curator neglect.
- **230 `modeled_mechanisms` links carry no `relationship` at all**, against 160
  `RECAPITULATES` and 49 `PARTIALLY_RECAPITULATES`. The expressive slots that do
  exist are under-populated, which is worth weighing before adding more.

This is written up as an open gap, not a proposed schema change. A row has been
added to §12 of the decision register pointing here. The trade the register would
have to weigh is real: the fields are optional and would be sparsely filled — as
`assays` demonstrates — and the value of a `spatial_context` free-text slot over a
well-written `interpretation` is genuinely unclear. The comparator slot (item 4) is
the strongest candidate because it repairs an ambiguity in a slot that is already
heavily used, rather than adding a new one that might not be.

## Notes for future scans

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
