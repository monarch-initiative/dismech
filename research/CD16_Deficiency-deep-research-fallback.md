# CD16 Deficiency Deep Research Fallback

## Provider Attempts

No deep-research provider run was performed for this entry before the initial
curation. That was a mistake, and it was causal rather than procedural: the two
most important papers about this allele were missed, and both were reachable
from the reference list of a paper already cached in the same PR. This record
documents the literature sweep performed afterwards, in response to review.

## Literature Scope

The entity is FCGR3A L66H homozygosity (MONDO:0014313, immunodeficiency 20).
Four homozygotes are published. All four are now curated:

- **PMID:8608639** — Jawahar 1996, *Clin Exp Immunol*. Index patient. Reduced
  spontaneous cytotoxicity, intact ADCC, reduced circulating NK cells gated as
  CD56(+)CD3(-) **without** CD16.
- **PMID:8874200** — de Vries 1996, *Blood*. A second, independent homozygote,
  numbered p.L48H from the mature protein. Recurrent viral respiratory
  infection, severe course after BCG, EBV and VZV — but **normal** spontaneous
  cytotoxicity and normal ADCC on formal testing, and an explicit closing
  caveat asking whether the genotype is causally related to NK deficiency at
  all. Reachable from `references_cache/PMID_23006327.md` as reference 17.
- **PMID:23006327** — Grier 2012, *J Clin Invest*. Second affected patient plus
  the NK-92 reconstitution establishing the CD16-CD2 mechanism.
- **PMID:34448085** — Izadi 2021, *J Clin Immunol*. Asymptomatic homozygote
  found on newborn TREC screening, with normal NK lytic function and normal
  CD56-bright/CD56-dim distribution. Reports the gnomAD frequency (~5% overall,
  ~100 homozygotes) and concludes the variant is unlikely to be a direct
  genetic cause. Also documents the flow-cytometry gating artifact by which an
  L66H homozygote reads as NK-cytopenic under a CD16-inclusive gate.

## What the sweep changed

The initial entry was built on two of the four homozygotes, and the two omitted
were the two that argue hardest against a simple causal model. Incorporating
them changed the entry substantively rather than cosmetically:

- `genetic.relationship_type` moved from `CAUSATIVE` to `DISPUTED`.
- The variant's `clinical_significance` moved from `PATHOGENIC` to
  `UNCERTAIN_SIGNIFICANCE`.
- The `Deficient Spontaneous NK Cell Cytotoxicity` node gained two
  `REFUTE`-graded evidence items and a `PROVISIONAL` mechanism confidence.
- A new `l66h_pathogenicity_disputed` CONTROVERSY was added, and the existing
  NK-count controversy was rewritten around three distinct mechanisms —
  gating artifact, genuinely low count in the index patient (whose gate did not
  include CD16, so the artifact does not explain it), and normal counts in two
  others.
- `prevalence` now separates the rarity of the reported syndrome from the
  commonness of the genotype.

## Searches run

PubMed, via the MCP PubMed server:

- `FCGR3A CD16 deficiency natural killer cell spontaneous cytotoxicity immunodeficiency`
- `CD16 FCGR3A natural killer immunodeficiency herpesvirus`
- `natural killer cell deficiency epitope-deficient Fc receptor type IIIA CD16`
- `Grier CD16 spontaneous NK cell cytotoxicity human immunodeficiency-causing mutation`
- Reference-list traversal of `references_cache/PMID_23006327.md` (refs 16, 17)

GeneReviews: `GeneReviews[TI] AND (FCGR3A OR "natural killer cell deficiency" OR
"immunodeficiency 20")` returns no chapter, so none is cited.
