# Citations for Research Query

**Query:** # NAM mining: iPSC protocols for retinal organoids, RGCs and photoreceptors (PMID:37686457)

🤖 *Written by [Claude Code](https://claude.com/claude-code) for Ginnie Hench.*

Second paper of the Complement-ARIE disease-paper round, tracked in the registry's
[review log](https://github.com/monarch-initiative/nams-registry/blob/main/projects/COMPLEMENT_ARIE_DISEASE_PAPERS.md)
([nams-registry#37](https://github.com/monarch-initiative/nams-registry/issues/37)).
Screened in from the abstract, then read in full. Target for an OpenScientist deep-research run.

- **Reference:** PMID:37686457, DOI [10.3390/ijms241713652](https://doi.org/10.3390/ijms241713652), *International Journal of Molecular Sciences* 24(17):13652 (2023). Open access, PMC10487913, so the full text is quotable.
- **Found in:** the Complement-ARIE Landscape Analysis dashboard, "Disease(s) Examined" = retinitis pigmentosa, glaucoma and age-related macular degeneration.

## What kind of paper this is

A **methods review** of protocols for differentiating three retinal cell products
from human iPSCs. It is not a study of any disease: across the full text, retinitis
pigmentosa is named once, glaucoma twice, AMD three times, and "disease modeling"
three times, always as motivation for the protocols. No patient-derived or
disease-genotype line is described.

That is a different shape from
[#17532](https://github.com/monarch-initiative/dismech/issues/17532) and from most
NAM-mining issues, and it should not be read as settling whether the work supports
any mechanism claim — the run decides that from the paper. Two things make it worth
mining either way:

- The three cell products are the cell populations whose loss defines the named
  diseases: photoreceptors in RP and AMD, retinal ganglion cells in glaucoma.
- The review's comparisons against human fetal retina are unusually good material
  for the `fidelity`, `limitations` and `divergences` fields, which are normally the
  hardest part of a model link to source.

## Models in the paper

Three cell products, each reviewed across a set of published protocols summarized in
its own table:

| Cell product | Protocol variants | Table |
|---|---|---|
| iPSC-derived retinal organoids | chemically defined storable organoids; retinoic acid timing; 9-cis retinal for rod maturation; BMP4 yield and composition; several ways of isolating optic vesicle-like structures | Table 1, 7 studies |
| iPSC-derived retinal ganglion cells | chemically defined conditions; biomaterial scaffolds for neurite outgrowth; dual SMAD plus Wnt inhibition; organoid dissociation with magnetic-activated cell sorting; rapid NGN2 overexpression | Table 2, 9 studies |
| iPSC-derived photoreceptors | defined conditions with signaling modulators; without extrinsic modulators; small-molecule inhibitors; bioreactor culture for yield and maturation | Table 3, 9 studies |

## Characterization and validation methods

These are readouts on the three products, not models in their own right:
immunofluorescence marker panels, qPCR, flow cytometry, single-cell RNA sequencing,
transmission electron microscopy of photoreceptor ultrastructure, patch-clamp
recording, multielectrode arrays, and calcium imaging.

## Fidelity content worth extracting

Verify and quote each against the full text:

- scRNA-seq comparison of hPSC-derived retinal organoids and retinospheres against
  human fetal retina: close in cellular composition and gene expression, with
  differences in the developmental trajectories of some cell types, photoreceptors
  among them.
- iPSC-derived RGCs resemble fetal RGCs more closely than organoid-derived RGCs; the
  review reports fetal and directly differentiated RGCs predominantly expressing
  BRN3A where most organoid RGCs express BRN3B.
- TEM comparison of photoreceptor maturation after 9-cis retinal versus all-trans
  retinoic acid.
- Calcium imaging as a maturation stage marker: immature RGCs depolarize to a GABA
  agonist, mature ones do not.

## Candidate dismech anchors

Each needs checking before anything is curated.

- **`Age_Related_Macular_Degeneration.yaml`, `Glaucoma.yaml` and
  `Inherited_Retinal_Dystrophy.yaml` have no `experimental_models:`,
  `animal_models:` or `computational_models:` at all.** Anything curated from this
  paper would be the first model on those entries.
- **`kb/modules/photoreceptor_degeneration.yaml`** has `Photoreceptor Gene Defect`,
  `Photoreceptor Metabolic and Oxidative Stress`, `Rod Photoreceptor Apoptosis`,
  `Secondary Cone Degeneration and Outer Retinal Thinning` and
  `Progressive Visual Field Loss and Blindness`. The photoreceptor and organoid
  products are candidates here.
- **`kb/modules/retinoid_visual_cycle_disruption.yaml` is probably the wrong anchor,
  and is flagged so a run does not land there by name-matching.** The retinoic acid
  and 9-cis retinal in these protocols are differentiation chemistry, not the RPE
  retinoid recycling the module describes. If the run does link them, it needs to say
  why in its own words.

## Existing records this sits beside

dismech already holds iPSC-derived retinal models, and every one is a patient or
genotype-specific instance:

- `Leber_Congenital_Amaurosis_10.yaml`: CEP290 patient iPSC optic cups and RPE, and
  LCA10 patient organoids treated with sepofarsen.
- `OPTN-related_Open_Angle_Glaucoma.yaml`: isogenic OPTN(E50K) hPSC-derived retinal
  ganglion cells.
- `RDH12-Related_Dominant_Retinopathy.yaml`: RDH12 patient iPSC organoids.
- `Stargardt_Disease.yaml`: patient-derived retinal organoid and an STGD1 iPSC-RPE
  model.

This review supplies the **baseline protocols those instances are built on**, which
makes it a direct test of
[nams-registry#86](https://github.com/monarch-initiative/nams-registry/issues/86),
whether a record describes a canonical model or one lab's instance. Read those
records before writing new ones, so the canonical and the instance descriptions agree
and the OPTN RGC model in particular is cross-referenced rather than duplicated.

## Gaps to record

- **No models on the three named disease entries**, as above.
- **Citing a review for a protocol.** Each protocol here belongs to a primary paper
  the review cites. Whether a record cites this review, the primary paper, or both
  needs deciding; the precedent in `Parkinsons_Disease.yaml` is a generic organoid
  record citing a review (PMID:42727800). Report what was done either way.

## Deliverables

1. One model-to-mechanism row per pairing, verified against the full text with an
   exact quote.
2. For pairings that map to a node, a `ModelMechanismLink` with `relationship`,
   `fidelity`, `model_scale`, `readouts` and `limitations`, drawing the fidelity
   content from the fetal-retina comparisons above.
3. Three NAM records in
   [nams-registry](https://github.com/monarch-initiative/nams-registry), one per cell
   product: the retinal organoid, the retinal ganglion cell, and the photoreceptor.
   The protocol variants in the three tables are described differences on those
   records, not records of their own — but report whether any variant differs enough
   to deserve its own, since that would revisit the granularity rule set for this
   round. Each record names `scientific-literature` and
   `complement-arie-landscape-dashboard` with this paper's DOI, and carries
   `dismech_status`.
4. A line in the review log's row for this paper: the entries changed, the gap issues
   opened, and the pull requests.


**Provider:** openscientist
**Generated:** 2026-11-14T03:16:45.482587

1. PMID:37686457
2. PMID:39425218
3. PMID:42727800