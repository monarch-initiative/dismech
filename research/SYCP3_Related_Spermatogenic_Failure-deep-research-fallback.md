# SYCP3-Related Spermatogenic Failure (SPGF4) Deep Research Fallback

## Provider Attempts

No Falcon or OpenScientist deep research artifact was generated for this entry.
Curation was conducted directly from primary literature using fetched PubMed
caches, without hand-editing any `references_cache/*.md` files.

## Evidence Scope Used For Curation

- PMID:14643120 (Miyamoto et al., Lancet 2003): human clinical series reporting
  heterozygous SYCP3 C-terminal truncating variants (643delA) in two azoospermic
  men; functional data showing dominant-negative interference with SYCP3 fibre
  formation in cultured cells; anchors the causal variant and dominant mechanism.
- PMID:10678170 (Yuan et al., Mol Cell 2000): Sycp3-null male mouse model
  demonstrating that SYCP3/SCP3 is required for axial/lateral element assembly,
  homologous chromosome synapsis, and male fertility; complete azoospermia with
  pachytene-stage apoptotic germ-cell death in homozygous null males.
- PMID:12004129 (Yuan et al., Science 2002): Sycp3-null female mouse model
  demonstrating oocyte aneuploidy and early embryo death via defective meiotic
  chromosome segregation; supports the mechanistic basis for the contested female
  oocyte-aneuploidy / recurrent pregnancy loss branch.
- PMID:19110213 (Bolor et al., AJHG 2009): human female cohort reporting SYCP3
  variants associated with recurrent pregnancy loss; provides SUPPORT evidence
  for the contested female branch.
- PMID:21357605 (Mizutani et al., Hum Reprod 2011): follow-up human study failing
  to confirm the SYCP3 657T>C variant association with aneuploidy-related
  recurrent miscarriage; provides REFUTE evidence for the contested female branch.

## NEC Preflight Summary

MONDO:0010052 (spermatogenic failure 4) was verified via OAK as the correct
gene-anchored entity for SYCP3 (HGNC:18130, OMIM:270960). The disease is
defined as azoospermia caused by mutation in SYCP3. No "SYCP3-related
gametogenic failure" dyadic MONDO term exists; this entry is therefore anchored
on the male azoospermia entity and models the contested female branch in the
pathophysiology rather than as an asserted phenotype.

## Curation Conclusions

SYCP3 encodes the axial/lateral element of the synaptonemal complex. Dominant-
negative heterozygous C-terminal truncating variants prevent SYCP3 fibre
assembly, causing synaptonemal complex assembly failure and homologous
chromosome asynapsis during meiotic prophase I. Asynapsis triggers the pachytene
checkpoint (meiotic recombination checkpoint signaling) and germ-cell apoptosis,
producing spermatogenic maturation arrest and non-obstructive azoospermia. The
male phenotype is well established. A female recurrent-pregnancy-loss phenotype
linked to oocyte aneuploidy has been proposed but is contested: one small cohort
study (Bolor 2009) reports the association; a subsequent study (Mizutani 2011)
does not replicate it. The female branch is therefore modeled with both
supporting and refuting evidence.

The entry conforms to the `meiotic_prophase_failure` module at:
- `#Synaptonemal Complex Assembly`
- `#Pachytene Checkpoint Arrest and Germ Cell Apoptosis`
- `#Spermatogenic Arrest and Non-Obstructive Azoospermia`
