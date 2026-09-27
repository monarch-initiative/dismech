---
disorder: Multiple Mitochondrial Dysfunctions Syndrome 6
mondo_id: MONDO:0054785
gene: PMPCB (hgnc:9119)
provider: claude_code
report_type: claude-code-literature-sweep
template_file: (manual claude-code literature sweep)
start_time: "2026-09-05"
run_metadata:
  tool: claude-code
  method: PubMed E-utilities + primary-source reading
  models_used:
  - claude-opus-4-8
---

# Multiple Mitochondrial Dysfunctions Syndrome 6 (MMDS6, PMPCB) — Literature Sweep

## Scope and identity

Multiple mitochondrial dysfunctions syndrome 6 (MMDS6; MONDO:0054785; OMIM
#617954) is an autosomal-recessive, childhood-onset mitochondrial
neurodegeneration caused by biallelic variants in **PMPCB** (hgnc:9119), which
encodes the catalytic β-subunit of the mitochondrial processing peptidase (MPP).
The parent MONDO term MONDO:0017338 ("fatal multiple mitochondrial dysfunctions
syndrome") has been ruled a GROUPING in the dismech curation queue, so the
numbered forms are the curatable single-gene units. MMDS6 is the numbered form
that fits the Fe-S "series" least well: PMPCB is **not** an Fe-S scaffold protein
but a presequence protease, and it reaches the shared Fe-S/respiratory-chain
phenotype **indirectly**, in significant part through failure to mature
frataxin. Its presentation is a **Leigh-like childhood neurodegeneration with
basal-ganglia and cerebellar involvement**, not neonatal lactic acidosis.

**entry_type decision: DISEASE.** One causal gene, one reasonably conserved
pathograph (MPP catalytic deficiency → impaired mitochondrial presequence /
frataxin processing → Fe-S cluster + respiratory-chain compromise →
basal-ganglia/cerebellar neurodegeneration). Curate as `kb/disorders/`.

## Disease mechanism (pathograph)

The landmark description (Vögtle et al., 2018, Am J Hum Genet; PMID:29576218)
established the mechanism from four families:

1. **PMPCB catalytic deficiency.** Biallelic PMPCB variants reduce PMPCB protein
   levels and MPP proteolytic activity. MPP is the essential protease that
   cleaves the N-terminal presequences of the majority of nuclear-encoded
   mitochondrial precursor proteins imported into the matrix.
2. **Impaired presequence/frataxin processing.** Fibroblasts, patient iPSCs and
   differentiated neuroepithelial stem cells accumulate the **frataxin processing
   intermediate**, "a sensitive substrate for MPP dysfunction." A yeast model
   (homologous Mas1 protein) reproduced the growth and MPP-processing defect with
   accumulation of mitochondrial precursor proteins.
3. **Iron-sulfur cluster biogenesis defect.** The processing defect causes
   "early impairment of the biogenesis of iron-sulfur clusters." (Frataxin is a
   core Fe-S biogenesis factor; its failed maturation is the mechanistic link to
   the Fe-S phenotype shared with the rest of the MMDS series and with Friedreich
   ataxia.)
4. **Respiratory-chain / Fe-S enzyme compromise.** Biopsy of an affected
   individual showed "changes and decreased activity in iron-sulfur
   cluster-containing respiratory chain complexes and dysfunction of
   mitochondrial and cytosolic Fe-S cluster-dependent enzymes."
5. **Neurodegeneration in early childhood** with cerebellar atrophy.

A zebrafish `pmpcb-/-` model (Jing et al., 2026, Mol Neurobiol; PMID:41999531)
adds cellular-level detail downstream of the same lesion: reduced neural cells,
uncompacted myelin, and dysfunctional locomotion, driven by decreased
mitochondrial membrane potential and insufficient ATP synthesis, elevated
ROS/ER stress, and consequent neural-cell apoptosis with impaired WNT/β-catenin
signaling. This is a model-organism corroboration, not human evidence.

## Clinical phenotype

From Vögtle 2018 (PMID:29576218) and Matthews et al., 2024 (J Hum Genet;
PMID:38374165), which reviews all prior cases and reports the sixth patient:

- Only ~6 individuals from ~4-5 families reported to date; original five all
  carried **missense** variants (c.523C>T p.Arg175Cys recurrent; p.Arg175His at
  the same residue), Matthews adds the first **splice** variant (exon-12
  skipping).
- **Leigh-like syndrome**: developmental regression + symmetrical basal-ganglia
  lesions, often triggered by a febrile/intercurrent illness.
- **Prominent cerebellar atrophy** with increased T2 signal of cerebellar cortex;
  putaminal atrophy and hyperintensity.
- **Ataxia**, **dystonia**, **epilepsy** (dystonia/epilepsy/ataxia in four of the
  original five), dysarthria, nystagmus.
- Onset by 12 months in the classic cases; none had obtained ambulation or
  speech; three of five deceased by age six. The Matthews proband is an outlier:
  later onset (age ~2.5 y, following otitis media), residual splicing, survival
  to 39 y, without dystonia/epilepsy — a milder end of the spectrum.

## Genetics

- Autosomal recessive; biallelic PMPCB variants (hgnc:9119, 7q22.1).
- MPP is an α/β heterodimer: PMPCA (α, substrate recognition) + PMPCB (β,
  catalytic, metalloendopeptidase). PMPCB carries the catalytic site; both
  subunits are required for processing.
- Recurrent p.Arg175 residue (Cys and His substitutions); missense predominates,
  one splice-acceptor variant (c.1330-2A>T, exon-12 skipping) reported.

## Treatment / management

No disease-modifying therapy. Supportive/symptomatic care only: anticonvulsants
for epilepsy, management of dystonia, physical/occupational/rehabilitative
therapy, nutritional support, and prompt treatment of intercurrent infection
(a documented precipitant of Leigh-like decompensation). Genetic counseling for
autosomal-recessive recurrence. (No PMPCB-specific trials or drugs; the zebrafish
study's rescue agents — WNT agonist BIO, creatine, PBA, glial pmpcb
re-expression — are preclinical model findings, not human therapies.)

## Key references (leads — verified against primary sources)

- **PMID:29576218** — Vögtle FN et al. Mutations in PMPCB Encoding the Catalytic
  Subunit of the Mitochondrial Presequence Protease Cause Neurodegeneration in
  Early Childhood. Am J Hum Genet 2018. (Landmark; HUMAN_CLINICAL + IN_VITRO.)
- **PMID:38374165** — Matthews E et al. Leigh syndrome with developmental
  regression and ataxia due to a novel splicing variant in the PMPCB gene.
  J Hum Genet 2024. (Sixth case + review of prior five; HUMAN_CLINICAL.)
- **PMID:41999531** — Jing Y et al. Pmpcb modulates zebrafish neurogenesis and
  stress resistance via regulating mitochondria metabolism and function. Mol
  Neurobiol 2026. (Zebrafish model; MODEL_ORGANISM.)

## Verification note

This is a Claude Code literature sweep (no external DR provider key configured in
this environment). Every PMID above was fetched from PubMed via NCBI E-utilities
and read in the primary source before use; snippets curated into the KB entry are
exact substrings of the cached abstract/full text. No GeneReviews chapter exists
for PMPCB/MMDS6 (PubMed `PMPCB GeneReviews` returned no results). Frataxin as an
MPP substrate and the Fe-S link are stated explicitly in the Vögtle abstract;
model-organism (zebrafish/yeast) findings are kept distinct via `evidence_source`
and are never the sole support for a human phenotype.
