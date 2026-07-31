# Assessment of the OpenScientist RAS(ON)-immune-remodeling report

- **Provider:** OpenScientist
- **Assessor:** Codex
- **Source:** `../openscientist.md`
- **Overall verdict:** `PARTIALLY_SUPPORTED`

## Overall assessment

The report reaches the right high-level verdict but misses the most directly
matched primary study. RAS(ON) multiselective inhibition has strong preclinical
support for remodeling PDAC immunity and sensitizing tumors to immunotherapy.
No clinical PDAC trial yet shows that daraxonrasib plus checkpoint blockade
improves outcomes or produces the proposed on-treatment immune changes.

The missing paper materially changes several details of the report.
[PMID:40057911](https://pubmed.ncbi.nlm.nih.gov/40057911/) evaluated
RAS(ON) multiselective inhibition in immunocompetent PDAC models using
RMC-7977 and daraxonrasib. It reported increased MHC-I on tumor cells, reduced
MDSC-like myeloid subsets, increased CD4 and CD8 T cells, T-cell and
conventional-dendritic-cell dependence, and deeper, more durable regressions
with immunotherapy. Its methods include a daraxonrasib-plus-anti-PD-1
combination.

## What should be retained

The central preclinical mechanism is supported. Allele-selective MRTX1133
studies also show CD8-dependent regression, reduced myeloid infiltration, and
checkpoint synergy
([PMID:37625401](https://pubmed.ncbi.nlm.nih.gov/37625401/);
[PMID:37782788](https://pubmed.ncbi.nlm.nih.gov/37782788/)).
The immune window may not be durable: long-term MRTX1133 treatment can reverse
early infiltration through a CDK8-CXCL2/FAS program
([PMID:42436354](https://pubmed.ncbi.nlm.nih.gov/42436354/)).

The human evidence gap is also real. The phase 1-2 and phase 3 daraxonrasib
studies report efficacy and safety without a checkpoint arm or paired immune
profiling
([PMID:42090791](https://pubmed.ncbi.nlm.nih.gov/42090791/);
[PMID:42223072](https://pubmed.ncbi.nlm.nih.gov/42223072/)).

## Corrections to the report

The report's claimed daraxonrasib/PDAC “agent gap” is false because it omitted
PMID:40057911. The same omission invalidates the categorical statement that
antigen presentation is largely RAS-independent. Autophagy/NBR1 and FAK are
important parallel MHC-I regulators
([PMID:32376951](https://pubmed.ncbi.nlm.nih.gov/32376951/);
[PMID:36977556](https://pubmed.ncbi.nlm.nih.gov/36977556/)), but those studies
do not establish dominance over RAS signaling, while RAS(ON) inhibition itself
increased tumor-cell MHC-I in the directly matched study.

The Treg edge remains unresolved, but the literature-search claim needs
qualification. PMID:40057911 measured FoxP3-positive CD4 Tregs and found that
the treatment-associated CD4 increase was not attributable to them. It did not
show Treg depletion or loss of suppressive function.

The report also treats the preprint PMID:36824971 and its final publication
PMID:37625401 as separate support. They are versions of the same study.
Additionally, its non-immune alternative cites
[PMID:41329731](https://pubmed.ncbi.nlm.nih.gov/41329731/), which PubMed marks
as retracted. The corrected republication is
[PMID:42224594](https://pubmed.ncbi.nlm.nih.gov/42224594/).

## Curation implication

Retain the hypothesis as preclinically supported but clinically unvalidated.
The strongest disease- and drug-class-matched evidence is PMID:40057911, with
explicit caveats for mouse models and combination composition. Do not promote a
patient-level checkpoint-benefit claim, a Treg-relief edge, or a singular
antigen-presentation “owner” without paired human biopsies and direct mediation
experiments.

The tumor-cell MHC-I, MDSC-like-subset, FoxP3-positive Treg, and
daraxonrasib-plus-anti-PD-1 details are available in the
[open-access full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12319402/), not
the PubMed abstract. Any later promotion of those details into the disease YAML
should cite a full-text source with an exact supporting snippet.
