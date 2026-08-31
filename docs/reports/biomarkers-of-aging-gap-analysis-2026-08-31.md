# Biomarkers of aging in dismech: what we have, what to add

*2026-08-31. Landscape and gap analysis. Report-only — no KB changes are made by this
document.*

## Summary

dismech has an essentially complete **mechanism** representation of aging and an
essentially empty **biomarker** representation of it. Eleven of the twelve
[hallmarks of aging](https://doi.org/10.1016/j.cell.2022.11.001) exist as modules with
proper trigger→consequence node chains, and 63 disease-entry nodes conform to them. But
of those eleven modules, exactly one — `cellular_senescence` — carries a `biochemical:`
block. It is also the **only module of all 166 in `kb/modules/`** that carries one.

The good news is that no schema work is needed. `BiomarkerReadout` already encodes the
qualification vocabulary that the NIA/Biomarkers of Aging Consortium literature asks
for, and `ExperimentalReadout` on `modeled_mechanisms` is its model-system twin. Both
carry a `biomarker_term` and both point at a pathophysiology `target`. The
clinical-versus-model-system reconciliation the field treats as an open problem is,
in dismech's data model, already a join on a shared pathograph node — nobody has used
it for aging yet.

## What we have

### Modules: hallmark coverage is complete

| Hallmark (López-Otín 2023) | Module | Nodes | `biochemical:` |
|---|---|---|---|
| Genomic instability | `genomic_instability_aging` | 4 | — |
| Telomere attrition | `telomere_attrition` | 3 | — |
| Epigenetic alterations | `epigenetic_alterations` | 3 | — |
| Loss of proteostasis | `loss_of_proteostasis` | 4 | — |
| Disabled macroautophagy | `disabled_macroautophagy` | 3 | — |
| Deregulated nutrient sensing | `deregulated_nutrient_sensing` | 7 | — |
| Mitochondrial dysfunction | `mitochondrial_dysfunction` | 5 | — |
| Cellular senescence | `cellular_senescence` | 5 | **2 markers** |
| Stem cell exhaustion | `stem_cell_exhaustion` | 3 | — |
| Altered intercellular communication | *(folded into `inflammaging`)* | — | — |
| Chronic inflammation | `inflammaging` | 4 | — |
| Dysbiosis | `gut_dysbiosis` | 4 | — |

Adjacent modules also exist: `il11_erk_ampk_mtor_aging`, `senescence_tumor_suppression`,
`photoaging`, `cytokine_storm_hyperinflammation`.

"Altered intercellular communication" is not a standalone module; it appears as the
`inflammaging` node *Systemic Propagation via Altered Intercellular Communication*.
That is a defensible lump — the hallmark's aging-relevant content is largely the
inflammatory secretome — but it means a curator looking for a conformance target by
hallmark name will not find one, and it should be stated in the `inflammaging`
description if it is not already.

### The one worked example

`cellular_senescence` carries two markers, and they are curated correctly — worth
reading before adding any others:

- **p16INK4a** → `NCIT:C129948` (CDKN2A Gene Product), `presence: INCREASED`, with a
  `readouts:` link to *Senescence-Associated Cell Cycle Arrest*
  (`relationship: READOUT_OF`, `direction: POSITIVE`, `endpoint_context: PROGNOSTIC`),
  each layer separately evidenced.
- **SA-β-galactosidase** → `NCIT:C107438` (Beta-Galactosidase).

This is the template. The `readouts:` link is what makes a marker part of the
pathograph rather than a disconnected list entry — the same rule that governs
`modeled_mechanisms` and `influences_mechanisms`.

### Conformance uptake is thin and inverted

Diseases conforming to each aging module:

```
loss_of_proteostasis        11      gut_dysbiosis                3
mitochondrial_dysfunction   10      deregulated_nutrient_sensing 3
genomic_instability_aging    9      stem_cell_exhaustion         1
disabled_macroautophagy      9      inflammaging                 1
epigenetic_alterations       6
cellular_senescence          6
telomere_attrition           4
```

`inflammaging` at 1 conformer is the anomaly. It is the hallmark with the most
mature clinical biomarker panel (IL-6, hsCRP, TNF-α) and the widest disease reach,
and it is nearly unused.

### The progeroid entries are the obvious pilot

`Werner_Syndrome` conforms to four aging hallmarks
(`cellular_senescence`, `genomic_instability_aging`, `mitochondrial_dysfunction`,
`telomere_attrition`) and `Hutchinson-Gilford_Progeria_Syndrome` to six. **Both carry
zero biochemical markers.** These are the entries where a segmental-progeroid biomarker
panel would be least speculative and most informative, and they already have the
pathograph nodes to hang readouts on. `Nestor-Guillermo_progeria_syndrome` has no
`conforms_to` at all and should get one.

## What the NIA/BAC landscape says

The [Biomarkers of Aging–NIA Joint Symposium 2024](https://doi.org/10.1111/acel.70124)
(PMID:40525821, held 12 Sep 2024, published 2025) and the Consortium's translation
papers converge on a few points that bear directly on what dismech should curate.

**There is no gold standard, and that is the stated problem.** The symposium report is
explicit that there is "no gold-standard measurement of biological aging … nor consensus
about what one should be," and that "systematic validation of biomarkers of aging for
clinical use has remained elusive." A knowledge base should therefore record aging
biomarkers with their *context of use* attached, not as facts about biological age.
dismech's `endpoint_context` enum already forces this, and its `CANDIDATE_SURROGATE`
value is the honest setting for nearly every aging biomarker today.

**Biomarker classes in play.** Epigenetic clocks (pan-mammalian, DunedinPACE,
PRC2-AgeIndex, and foundation-model clocks like CpGPT/MethylGPT); plasma-proteomic
**organ-specific** clocks; metabolomic markers of mitochondrial function
(glycerophospholipids) predicting cognitive and mobility decline; senescent-cell burden
from blood; and functional proxies (gait speed, grip strength, healthspan as time to
first chronic condition).

**Organ-specific and individual-level heterogeneity is the frontier.** Gladyshev's point
that "aging within individuals may likewise not occur at uniform rates," and Barzilai's
proteome findings varying by genetic heritage and sex, argue against a single
whole-organism marker and in favour of markers attached to specific mechanisms — which
is what a pathograph node *is*.

**Evidence triangulation.** Belsky's framing — predictive modelling, *in vitro*
mechanistic experiments, and intervention-response — maps onto dismech's existing
`evidence_source` axis (`HUMAN_CLINICAL` / `IN_VITRO` / `MODEL_ORGANISM`), and the
existing `check-snippet-grading` gate already prevents the same quote being re-graded
across those categories.

Also worth tracking: the **FAST initiative** (mining biospecimens from completed trials
of metformin, SGLT-2 inhibitors, GLP-1 agonists, bisphosphonates) and the **Hevolution
Alliance for Aging Biomarkers**, both of which will produce citable
intervention-response biomarker data over the next cycle; and NIA's Fifth Geroscience
Summit, *Revisiting the Geroscience Hypothesis — Focus on Health*, 2–3 December 2026.

## Clinical markers vs model-system markers, and how to reconcile them

This is the part where dismech has an actual structural answer, so it is worth being
precise about the problem first.

### The problem

AFAR's criteria for a "true" biomarker of aging include **applicability in both humans
and model organisms**. That criterion systematically favours molecular and subcellular
markers and disfavours organism-specific ones. The clean illustration is the **FRIGHT
clock**, built on mouse frailty indices: it is a good mouse biomarker and it does not
translate, because the measurement itself has no human counterpart. The inverse holds
too — gait speed and grip strength are excellent human markers with no faithful mouse
equivalent. Meanwhile epigenetic clocks *do* cross species (pan-mammalian clocks,
EnsembleAge HumanMouse), which is exactly why they dominate the field.

A useful worked case sits in the `inflammaging` block added alongside this report: the
IgG N-glycome is reported in healthy old people, centenarians and their offspring **and**
in calorie-restricted mice (PMID:22353383). That is a marker satisfying AFAR's
cross-species criterion on its face — and it is still not a clean case, because IgG-G0 is
itself pro-inflammatory, so a mouse-to-human concordance in the marker is partly a
concordance in the mechanism. Cross-species agreement in a marker that is also a mechanism
is weaker evidence of a shared clock than it first appears.

So "reconciliation" is not one problem but three:

1. **Same marker, both species** (DNAm age, p16, IL-6) — needs a concordance claim.
2. **Species-specific marker of a shared mechanism** (mouse frailty index vs human
   SPPB gait speed) — needs a *mechanism-level* bridge, not a marker-level one.
3. **Marker measurable in only one system** (SA-β-gal in tissue/NAMs; organ-specific
   plasma proteomic clocks in humans) — needs to be recorded as such, not silently
   generalised.

### How the existing schema handles all three

The join is **the pathophysiology node**, not the marker.

| Side | Where it lives | Class | Key slots |
|---|---|---|---|
| Clinical | `biochemical[].readouts[]` | `BiomarkerReadout` | `target`, `relationship`, `direction`, `endpoint_context`, `regulatory_endpoint_refs` |
| Animal | `animal_models[].modeled_mechanisms[].readouts[]` | `ExperimentalReadout` | `target`, `biomarker_term`, `direction`, `assays` |
| NAM | `experimental_models[].modeled_mechanisms[].readouts[]` | `ExperimentalReadout` | same |

Both readout classes carry `biomarker_term` and both carry a `target` that must name a
node in the same entry. That gives the three cases clean, distinct representations:

- **Case 1** — the same `biomarker_term` appears on a clinical `BiomarkerReadout` and a
  model-side `ExperimentalReadout` pointing at the *same* `target` node. Concordance is
  then a query, not an assertion, and the directions can be compared
  (`BiomarkerReadoutDirectionEnum` `POSITIVE` vs `ModelReadoutDirectionEnum` `INCREASED`).
- **Case 2** — different `biomarker_term` values, same `target` node. The mechanism
  bridges what the markers cannot. This is precisely what the FRIGHT-vs-SPPB case needs,
  and it is why attaching markers to hallmark *nodes* beats maintaining a flat
  cross-species marker table.
- **Case 3** — a marker that exists on only one side simply has no counterpart readout,
  and `ModelMechanismLink.fidelity` plus `limitations` carry the translational caveat.
  `FAILS_TO_RECAPITULATE` is available for the genuinely negative result and requires
  both `limitations` and evidence.

**One thing to be careful about.** A model-side readout tempts a curator to grade its
evidence `HUMAN_CLINICAL` because the *claim* is about human aging. It is not:
`evidence_source` classifies the cited publication. A mouse epigenetic-clock result is
`MODEL_ORGANISM` however translatable the clock is. `just check-snippet-grading`
enforces this per quoted sentence and will catch the drift.

## Ontology gaps

`BiomarkerTerm` validates term existence against NCIT with no hierarchy constraint, so
binding is permissive. Availability, checked against NCIT via OLS:

**Already available and mostly already cached** — `NCIT:C129765` Telomere Length;
`NCIT:C181406` GDF-15 Measurement; `NCIT:C74834` Interleukin 6 Measurement;
`NCIT:C157114` High Sensitivity C-Reactive Protein Measurement; `NCIT:C127624` Klotho
Protein Measurement; `NCIT:C88043` Neurofilament Light Polypeptide; `NCIT:C20535` Tumor
Necrosis Factor; `NCIT:C17783` Cyclin-Dependent Kinase Inhibitor 1 (p21); `NCIT:C107438`
Beta-Galactosidase; `NCIT:C129948` CDKN2A Gene Product; `NCIT:C165222` DNA Methylation
Array; `NCIT:C63328` DNA Methylation Analysis; `NCIT:C129903` Global DNA Methylation
Profile. Functional markers are covered too: `NCIT:C139210` Grip Strength,
`NCIT:C181968` SPPB Gait Speed Test, `NCIT:C185373` Clinical Frailty Scale.

**The real gap: there is no NCIT term for an epigenetic clock or for biological age.**
Searching NCIT for "Epigenetic Clock" returns nothing, and "Biological Age" returns only
*Biological Agent* and its descendants. The single most important class of aging
biomarker is unbindable.

Per the `dismech-terms` rule that no term beats a bad one, the answer is **not** to bind
a clock to `NCIT:C17961` (DNA Methylation) or to `NCIT:C16269` (Aging) — neither is the
measurement. Two defensible options:

1. Bind the **assay** (`NCIT:C165222` DNA Methylation Array) and carry the clock identity
   in a free-text `preferred_term` — e.g. `preferred_term: DunedinPACE pace-of-aging
   estimate`. This is the documented pattern for a `preferred_term` more specific than
   the best available term, and it validates today.
2. Leave `term:` off, record in `notes` that NCIT was searched and what was missing, and
   submit an NCIT term request. Given how central these measures are, a request is
   probably worth making regardless of which option is used in the interim.

Note that a composite clock is not really a biomarker in the `Biochemical` sense at all —
it is a model output over many features. If clocks become a substantial part of the KB,
whether they belong in `biochemical:` or in `computational_models:` is a genuine open
design question, not a curation detail.

## Recommendations

**Tier 1 — close the module biomarker gap.** Add `biochemical:` blocks with
`readouts:` links to the ten bare hallmark modules, following the `cellular_senescence`
pattern. Highest value first, because these are the markers with real clinical evidence
behind them:

| Module | Candidate markers | Node to read out |
|---|---|---|
| `inflammaging` | IL-6, hsCRP, TNF-α | Chronic Low-Grade Sterile Inflammation |
| `telomere_attrition` | Leukocyte telomere length | Progressive Telomere Attrition |
| `epigenetic_alterations` | DNAm age / pace-of-aging *(see ontology gap)* | Age-Associated Epigenetic Drift |
| `mitochondrial_dysfunction` | GDF-15, lactate, glycerophospholipids | Bioenergetic Decline and Oxidative Stress |
| `deregulated_nutrient_sensing` | IGF-1, FGF21 | mTORC1 Hyperactivation; Attenuated FGF21 Response |

`inflammaging` first: best-evidenced markers, worst conformance uptake (1 disease), and
adding markers gives curators a reason to conform to it.

> **Status update.** `inflammaging` is **done** — a five-marker block (IL-6, hsCRP, TNF,
> cf-mtDNA, IgG-G0 N-glycans) with `BiomarkerReadout` links was added on the same branch
> as this report, grounded in Franceschi 2018 (PMID:30046148), Harris 1999
> (PMID:10335721), Pinti 2014 (PMID:24470107) and Dall'Olio 2013 (PMID:22353383). It is
> now the second module in the KB with a `biochemical:` block and the worked example for
> the rest of Tier 1. Two patterns established there are worth copying: IL-6 carries
> **two** readouts against different nodes to show one marker serving distinct contexts of
> use (`MONITORING` on the mechanism, `PROGNOSTIC` on the outcome), and cf-mtDNA/IgG-G0
> are annotated as **both marker and mechanism**, which is common in aging biology and
> which the `READOUT_OF` relationship deliberately does not assert away.
>
> **`mitochondrial_dysfunction` is also done** — GDF-15, FGF-21 and blood mtDNA copy
> number, plus a knowledge gap on the disease-vs-aging scope limit. Both modules also
> carry `KNOWLEDGE_GAP` discussions now; see the next section, which the gaps changed.

### A correction to this report's framing

Curating the first two modules surfaced a 2025 Delphi expert consensus statement
([PMID:39708300](https://pubmed.ncbi.nlm.nih.gov/39708300/), *J Gerontol A*) that
postdates the NIA symposium summarized above and is more directly useful than anything
else cited here. It reached 70–98% agreement on **14 biomarkers**: IGF-1, GDF-15, hsCRP,
IL-6, muscle mass, muscle strength, grip strength, Timed-Up-and-Go, gait speed, standing
balance, frailty index, cognitive health, blood pressure, and DNA methylation/epigenetic
clocks. Three findings in it bear directly on the recommendations above:

- **hsCRP, TNF-α, HbA1c and blood pressure did *not* reach agreement that they predict
  biological age better than chronological age.** They are accepted as measures of state,
  and unresolved as measures of *rate*. That is a sharper claim than "unvalidated" and it
  is now recorded as a gap on the markers themselves.
- **Physiological markers dominate the consensus list** — grip strength had the highest
  agreement of all 14, at 98%, against IGF-1's lowest at 70%. The panel notes this may
  reflect its own composition, but it cuts against this report's molecular emphasis, and
  it is a problem for cross-species work, since grip strength and TUG are exactly the
  human-only measures that do not translate to mice.
- **Composites are preferred and no consensus composite exists** — the paper calls this a
  research priority in as many words. This is the same structural question flagged under
  ontology gaps: a composite is a model over features, not an analyte.

A further process note. The gap this section originally intended to record was
Franceschi 2018's statement that the DNAm-age/inflammaging relationship "has not been
investigated." A PubMed check found 51 papers on epigenetic age acceleration and
inflammaging, so that claim is eight years stale and was deliberately **not** curated.
Recording a knowledge gap from a review's own framing without checking whether the field
has since closed it is a failure mode worth naming.

**Tier 2 — the progeroid pilot.** Give `Werner_Syndrome` and
`Hutchinson-Gilford_Progeria_Syndrome` biochemical blocks with readouts to the hallmark
nodes they already conform to, and add `conforms_to` to
`Nestor-Guillermo_progeria_syndrome`. This exercises the whole pattern on entries where
the mechanism scaffolding is already in place.

**Tier 3 — the cross-species demonstration.** Pick one node — *Senescent Cell
Accumulation* is the natural choice — and curate a clinical `BiomarkerReadout`, an
animal-model `ExperimentalReadout`, and a NAM `ExperimentalReadout` all pointing at it,
with honest `fidelity` and `limitations`. That makes the reconciliation pattern concrete
and reviewable rather than theoretical, and it is the thing to point at when the question
comes up again.

**Tier 4 — worth deciding, not yet doing.** A `Biomarkers_of_Aging` grouping over the
progeroid and age-related entries; whether composite clocks belong in `biochemical:` or
`computational_models:`; and an NCIT term request for epigenetic clock / biological age.

## Caveats

Module and conformance counts are from the working tree at the date above and will drift.
The NIA/BAC summary is drawn from the published symposium report and Consortium
translation papers, not from primary attendance. No marker in the recommendation tables
has had its evidence curated or its snippet verified — they are leads with plausible NCIT
bindings, and each still needs the normal `just fetch-reference` /
`just count-verified-snippets` loop before it goes into an entry.

## Sources

- [Biomarkers of Aging–NIA Joint Symposium 2024: New Insights Into Aging Biomarkers](https://doi.org/10.1111/acel.70124) — PMID:40525821
- [Challenges and recommendations for the translation of biomarkers of aging](https://www.nature.com/articles/s43587-024-00683-3) — *Nature Aging*
- [Invigorating discovery and clinical translation of aging biomarkers](https://www.nature.com/articles/s43587-025-00838-w) — *Nature Aging*
- [Validation of biomarkers of aging](https://www.nature.com/articles/s41591-023-02784-9) — *Nature Medicine*
- [Biomarkers of aging for the identification and evaluation of longevity interventions](https://www.cell.com/cell/fulltext/S0092-8674(23)00857-7) — *Cell*
- [NIA Division of Aging Biology workshops and reports](https://www.nia.nih.gov/research/dab/workshops)
- [Trans-NIH Geroscience Interest Group](https://www.nia.nih.gov/gsig)
