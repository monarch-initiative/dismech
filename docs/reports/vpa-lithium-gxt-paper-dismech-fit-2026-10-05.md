# How the valproic acid and lithium "GxT in a dish" paper fits dismech

Written 2026-10-05 against dismech `main` at commit `681ac38851`. Revised
2026-10-09 against `main` at `bd855d0346`, after the paper was curated, and
again at `1148dee5d8` to correct what it said about the issue tracker.

## Status of this report

The paper is now in dismech. `Fetal_Valproate_Syndrome.yaml` was added in
[#13604](https://github.com/monarch-initiative/dismech/pull/13604), merged
2026-10-06, and cites it 13 times. The five gaps below were written before
that, and this revision records what each one became.

| Gap | State |
|---|---|
| 1. Fetal valproate syndrome has no entry | Closed by #13604 |
| 2. Autism valproate link has no intermediates | Open, reframed as a cross-reference. Issue [#13779](https://github.com/monarch-initiative/dismech/issues/13779) |
| 3. Bipolar Disorder has no model sections | Open. Issue [#13600](https://github.com/monarch-initiative/dismech/issues/13600) |
| 4. Neural tube defect entries contradict the new entry | Open. Issue [#13778](https://github.com/monarch-initiative/dismech/issues/13778) |
| 5. Schizophrenia and Epilepsy have no model sections | Dropped as not worth the work |

The schema gaps at the end of this report were confirmed by how #13604 had to
record the model, and are the part of this report that has not been acted on.

## The paper

Valone JM, Le BD, Matoba N, Mory JT, Wolter JM, Love MI, Stein JL. "Assessing
molecular gene by treatment interactions using a population of neural
progenitors exposed to valproic acid and lithium." *Molecular Psychiatry*, 2026.

- DOI: [10.1038/s41380-026-03578-4](https://doi.org/10.1038/s41380-026-03578-4)
- PMID: 41935183
- Full text: PMC13364665 (open access, CC BY-NC-ND)

When this report was written dismech did not cite the paper at all. It is now
cited 13 times, all in `Fetal_Valproate_Syndrome.yaml`, and is cached in
`references_cache/`.

This review covers the main text only. The 21 supplementary tables were not
read.

## What the paper offers as a model

The model is a primary culture of human neural progenitor cells from fetal
dorsal telencephalon (14 to 21 gestational weeks). The cells come from 83
genotyped donors described as neurotypical. Each line was exposed for 48 hours
to 1 mM valproic acid (VPA), 1.5 mM lithium chloride, or vehicle, then profiled
by ATAC-seq, RNA-seq and an EdU proliferation assay.

In dismech terms this is an `ExperimentalModel` of type `PRIMARY_CELL_CULTURE`.
It models an exposure and a treatment response. It does not model a disease
genotype.

Main results:

- VPA changed chromatin accessibility at 65% of peaks, more often closing than
  opening. Lithium changed 18%, more often opening.
- VPA shifted progenitors from proliferation toward differentiation and reduced
  the S-phase fraction in every donor at 1 mM. Lithium increased proliferation
  at 0.75 to 1.5 mM and decreased it at higher concentrations.
- VPA-responsive regions were enriched for the heritability of autism,
  intelligence, educational attainment and bipolar disorder. Lithium-responsive
  regions were enriched for bipolar disorder heritability.
- Genetic variants changed the molecular response to the drugs: 779 response
  caQTLs and 214 response eQTLs for VPA, and 15 of each for lithium.
- Under VPA only, a transcriptome-wide association study linked folate and
  cobalamin metabolism genes (DHFR2, MTFMT, MTHFD1, MMACHC, MTRR, MMUT) to
  educational attainment.

## Gaps in disorder entries the paper could fill

### 1. Fetal valproate syndrome has no entry and no stub

**Closed.** `Fetal_Valproate_Syndrome.yaml` was added in #13604: 4,165 lines,
17 pathophysiology nodes, five experimental models and four animal models. The
paper is curated there as the model this section anticipated, under
`experimental_models`:

```yaml
- name: Genotyped human neural progenitor population exposed to valproic acid
  experimental_model_type: PRIMARY_CELL_CULTURE
  publication: PMID:41935183
```

linked to mechanism nodes with `MEASURES` and `RECAPITULATES` relationships at
`MODERATE` fidelity. What follows is the original analysis, kept because the
schema limits it predicted are what the merged entry ran into.

MONDO:0012275 appeared nowhere in `kb/` or `stubs/`. This is the disorder the
model most directly represents.

The paper can be used for an entry, with limits. An `ExperimentalModel` could
hold:

- the model itself: type, organism, cell type, tissue and publication;
- links to mechanism nodes through `modeled_mechanisms`, each with a
  relationship, fidelity, divergences and evidence;
- structured readouts on each link, such as chromatin accessibility changed and
  S-phase fraction decreased, with a direction and a quoted snippet.

Three things would fall back to prose (see "Gaps in the schema" below): the
exposure dose and duration, the donor population, and the gene-by-exposure
results. The last is the paper's main novelty.

The paper cannot found the entry on its own. It would supply the experimental
model and evidence for one or two mechanism nodes, such as chromatin change and
the shift from proliferation to differentiation. Phenotypes, prevalence, the
clinical exposure-outcome evidence and the mechanism nodes themselves have to
come from the clinical and teratology literature.

### 2. Autism Spectrum Disorder: the valproate link has no molecular intermediates

**Open, but reframed.** The chain this section asked for now exists in
`Fetal_Valproate_Syndrome.yaml`, and no entry references that file: a `git
grep` for its name across `kb/` matches only inside it. So the work is to point
the autism entry's existing valproate factor at that chain with a cross-entry
reference, not to add a model to the autism entry. Issue #13779.

The "Prenatal valproate exposure" factor is linked to the node "Heterogeneous
neurodevelopmental molecular effects" as `INDIRECT_UNKNOWN_INTERMEDIATES`. Its
description says "No cited sentence follows valproate to any molecular step".

The paper supplies human in-vitro intermediates. It also shows that
VPA-responsive regions are enriched for autism heritability and VPA-responsive
genes for autism-associated genes.

The entry has no valproate model of any kind. Its two animal models are a
Cntnap2 knockout with maternal immune activation and a prenatal
interferon-alpha rat.

### 3. Bipolar Disorder has no model sections

**Open.** Issue #13600 proposes the lithium model described here.

The entry has neither `experimental_models` nor `animal_models`. The patient
iPSC neuron work is cited only inside pathophysiology nodes.

The paper would add a lithium model with three findings:

- lithium increases progenitor proliferation at 0.75 to 1.5 mM;
- lithium-responsive regions are enriched for bipolar disorder heritability;
- 105 genes associate with bipolar disorder under lithium, including FADS1,
  TRANK1 and BDNF.

There is no neurogenesis or progenitor-proliferation node to link to.
"Neuroplasticity Alterations" is the closest. The companion paper on
lithium-induced proliferation and GNL3 (PMID:36307327) is also absent.

### 4. Neural tube defects: the folate question is open or contradicted

**Open, and now a contradiction between entries rather than a gap.** Issue
#13778.

- Anencephaly records the valproate link as indirect because the responsible
  step is "unsettled between folate antagonism and histone deacetylase
  inhibition".
- Spina Bifida Cystica says VPA acts independently of maternal folate status.
  It has no model sections.

`Fetal_Valproate_Syndrome.yaml` curates folate receptor antagonism as a
mechanism, quoting that valproate-exposed cells take up less folate, while
recording separately that the evidence for folic acid *preventing* valproate
teratogenesis is conflicting. Those are two different claims, and the spina
bifida wording conflates them: "independent of maternal folate status" is
defensible about rescue and is contradicted about mechanism. The three entries
cannot all be right.

The paper's own folate result bears on this only indirectly, since its outcome
is cognition (educational attainment) rather than neural tube closure.

### 5. Schizophrenia and Epilepsy have no model sections

**Dropped** on 2026-10-09 as not worth the work: one colocalization and a
"modest" enrichment, against the cost of opening model sections in two large
entries. No issue filed.

The contribution here is thinner.

- Schizophrenia: a VPA-responsive eQTL for AS3MT (rs7096169) colocalizes with a
  schizophrenia GWAS signal. AS3MT is not among the entry's genes.
- Epilepsy: the paper describes the heritability contribution of VPA-responsive
  regions as modest.

## Gaps in the schema

**Confirmed by the merged entry, and not acted on.** #13604 hit all three rows
below. It recorded the donor panel as `cell_source: Primary human neural
progenitor cells from 83 genotyped multi-ancestry donors` and the exposure as
`culture_system: Monolayer, 48-hour exposure to 1 mM valproic acid`, so both
are prose in slots not meant for them. The genetic half of the paper was
dropped: the entry has no mention of a response QTL, of MTHFD1, or of
educational attainment, which is the paper's own headline result.

`ExperimentalModel` can record this model, but three parts of the design have
no structured home.

| Part of the design | What the schema offers | Consequence |
|---|---|---|
| Exposure, dose and duration (1 mM VPA, 48 h) | The free-text `conditions` slot. `ExperimentalPerturbation` exists only on `Experiment`, which holds proposed experiments | "All models exposed to valproate" cannot be queried |
| Donor population (83 genotyped, unaffected donors) | The free-text `cell_source` slot | A population-scale donor panel cannot be told apart from a single line |
| Gene-by-exposure interaction (response QTLs) | Nothing. `EnvironmentalMechanismTarget` has no genetic-context field, and `TreatmentEffectModifier` covers patient subgroups | The result can only be mentioned in `findings` or `notes` |

No disorder file mentions a response QTL, and one mentions a caQTL.

The first two rows are a loss of queryability, not of content. The third is a
loss of content.

The authors' stated limitations fit the existing `ModelDivergence` kinds: a
single cell type is a `BOUNDARY_OMISSION`, and acute 48-hour exposure is a
`TEMPORAL_SCOPE` divergence.

## Caveats for curation

- The findings are associative: heritability enrichment, colocalization and
  transcriptome-wide association. They belong as `IN_VITRO` evidence on model
  links, not as support for human phenotypes.
- The donors are unaffected, so the model says how typical progenitors respond
  to the drugs. It does not say how patient cells respond.
- Snippets can be checked against the PMC full text, which is open access and
  now cached in `references_cache/`.

## What is left

Gaps 2, 3 and 4 are filed as issues and need a curator.

One of the three schema gaps is filed, which this report originally said none
were. [#13768](https://github.com/monarch-initiative/dismech/issues/13768)
covers the exposure and perturbation row: it asks for a structured
perturbation on the model classes, and notes that
`ExperimentalModel.conditions` is a list of strings.

No issue proposes a fix for the other two rows. The donor-population row is
recorded in #13602's list of what the schema cannot hold today — `cell_source`
is free text, so a genotyped donor panel cannot be told apart from a single
cell line — but nothing asks for the change. For the gene-by-exposure row,
searching the tracker for QTL, gene-by-exposure, `cell_source` and donor panel
turned up nothing beyond those two issues. That row is the paper's own
headline result — common variants change how neural progenitors respond to
these drugs — and it was dropped when the paper was curated.

Whether that last result belongs in dismech is an open question rather than a
gap to close. A response QTL describes variance across a donor panel, not a
step in any one patient's disease, and dismech is organized around a single
disease with a reasonably conserved pathograph.
[#13602](https://github.com/monarch-initiative/dismech/issues/13602), which
sorts models by what ties them to the disease, is where that question is being
worked out; its bottom row already places a looser case, model-responsive
regions overlapping GWAS signal, outside what a model link should carry. A
response QTL is not that case — it is measured in the dish, on the model's own
donors — but it raises the same question about scope.

One candidate home is [EnviroMech](https://github.com/monarch-initiative/enviromech),
a separate knowledge base in the same family, which records the
exposure-outcome association itself rather than hanging it on a curated
disease. A Mech scoped to pharmacogenomic and gene-by-environment response is
another. Neither is settled.
