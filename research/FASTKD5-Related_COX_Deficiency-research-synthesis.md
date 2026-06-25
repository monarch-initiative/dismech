# FASTKD5-Related COX Deficiency (MC4DN24) — Research Synthesis

**Provenance.** This is a curator literature synthesis assembled by the automated
curation scanner (high_effort run) to satisfy the deep-research-artifact requirement
for the new `FASTKD5-Related_COX_Deficiency.yaml` entry (PR #4760, issue #4239). It is
**not** the raw output of an automated deep-research provider (Falcon / OpenScientist /
Asta). Because the disease has a single founding clinical paper, a provider sweep would
add little beyond the basic-science mechanism literature captured here. **Every PMID
below was verified against PubMed** (title, journal, year, authors) before inclusion, per
the anti-hallucination / anti-NEC SOP (CLAUDE.md §2a/§2b). No citation was promoted into
the YAML `evidence` blocks without its snippet being validated as an exact substring of
the cached abstract.

## Disease identifiers

- **Name:** FASTKD5-related cytochrome c oxidase deficiency / mitochondrial complex IV deficiency, nuclear type 24 (MC4DN24)
- **MONDO:** MONDO:0980755 (mitochondrial complex IV deficiency, nuclear type 24)
- **Gene:** FASTKD5 (hgnc:25790), OMIM:621431
- **Inheritance:** autosomal recessive (biallelic)
- **Grouping:** member of `Mitochondrial_Complex_IV_Deficiency` (conforms to `complex_iv_assembly_deficiency#Complex IV Biogenesis Failure`)

## Founding clinical report (sole clinical cohort to date)

**PMID:40499538** — Antonicka H, *et al.* "Bi-allelic mutations in FASTKD5 are
associated with cytochrome c oxidase deficiency and early- to late-onset Leigh syndrome."
*Am J Hum Genet* 2025;112(7):1699–1710. doi:10.1016/j.ajhg.2025.05.007.

- Exome sequencing identified compound-heterozygous FASTKD5 variants of unknown
  significance in **three** subjects with Leigh syndrome (brainstem + basal ganglia
  lesions); three missense and two frameshift (premature-stop) alleles.
- Patient fibroblasts: reduced steady-state FASTKD5 protein → reduced COX1 (cytochrome c
  oxidase subunit 1) translation → impaired Complex IV assembly → decreased COX enzymatic
  activity. Severity of the molecular deficit correlated with clinical severity.
- Wild-type FASTKD5 cDNA (but not the missense cDNAs) rescued the molecular defects,
  establishing pathogenicity. Two missense alleles were near-complete loss of function;
  one was hypomorphic (impaired protein stability).

This is the **first and (as of this synthesis) only** clinical report tying FASTKD5 to
human disease; the entry's clinical evidence is therefore drawn entirely from this paper.
A future literature check should re-confirm whether additional cases have been published.

## Mechanistic basis (basic-science literature)

The FASTKD5 disease mechanism is independently grounded in prior cell-biology work that
predates the clinical report, which strengthens the curated pathophysiology model:

- **PMID:25683715** — Antonicka H, Shoubridge EA. "Mitochondrial RNA Granules Are Centers
  for Posttranscriptional RNA Processing and Ribosome Biogenesis." *Cell Rep*
  2015;10(6):920–932. doi:10.1016/j.celrep.2015.01.030. Identified FASTKD5 as a
  mitochondrial RNA-granule (MRG) component and showed FASTKD5 is **required for maturing
  precursor mRNAs not flanked by tRNAs** (so not handled by the canonical tRNA-punctuation
  processing pathway); silencing FASTKD5 impaired COX1 mRNA maturation, COX1 synthesis,
  and Complex IV assembly — directly prefiguring the patient phenotype.

- **PMID:40637235** — Antonicka H, *et al.* "FASTKD5 processes mitochondrial pre-mRNAs at
  noncanonical cleavage sites." *Nucleic Acids Res* 2025;53(13):gkaf665.
  doi:10.1093/nar/gkaf665. FASTKD5 endonucleolytically processes the three non-canonical
  mRNAs **not flanked by tRNAs — CO1 (MT-CO1), CO3 (MT-CO3), and CYB (MT-CYB)**. Loss of
  FASTKD5 leaves these transcripts with unprocessed 5′-UTRs that cannot be translated,
  producing a severe combined OXPHOS assembly defect. Maps function-essential residues and
  finds the residue requirements are RNA-substrate-specific.

- **PMID:29036396** — Jourdain AA, *et al.* "The FASTK family of proteins: emerging
  regulators of mitochondrial RNA biology." *Nucleic Acids Res* 2017;45(19):10941–10947.
  doi:10.1093/nar/gkx772. Review situating FASTKD5 among FASTK/FASTKD1–5 as
  architecturally related mitochondrial RNA-binding regulators with distinct roles in mt
  mRNA processing, maturation, ribosome assembly, and translation.

### Mechanistic note for curation

FASTKD5 is **mechanistically distinct** from every other member of the
`Mitochondrial_Complex_IV_Deficiency` grouping. The other members act at or after
holoenzyme assembly (assembly factors, metallochaperones, structural subunits) or as a
translational activator (TACO1). FASTKD5 acts **upstream of translation**, at mitochondrial
mRNA processing — its loss impairs maturation of the COX1 mRNA itself. The curated entry
correctly models this as a new lesion class within the conserved Complex IV
biogenesis-failure mechanism. (The basic-science studies above note FASTKD5 also processes
CO3 and CYB, i.e. a broader combined-OXPHOS defect in null cell models; the human disease,
however, presents as an **isolated Complex IV / COX** deficiency, which is what the entry
models from the clinical paper.)

## Completeness assessment against the curated entry

| Element | Covered in YAML? | Source |
|---|---|---|
| Causal gene / inheritance (FASTKD5, AR, biallelic) | ✅ | PMID:40499538 |
| Allelic spectrum (3 missense, 2 frameshift; LoF vs hypomorphic) | ✅ | PMID:40499538 |
| mRNA-processing lesion → ↓COX1 translation → ↓Complex IV assembly | ✅ (3 atomic nodes) | PMID:40499538 |
| Decreased COX enzymatic activity (biochemical) | ✅ (added in this PR) | PMID:40499538 |
| Leigh syndrome + brainstem/basal-ganglia phenotypes | ✅ | PMID:40499538 |
| Genotype–severity correlation | ✅ | PMID:40499538 |
| Supportive/metabolic management | ✅ | clinical convention |

### Gaps / deferred items (not curated — evidence-limited or out of scope)

- **Onset descriptor.** The paper describes "early- to late-onset" Leigh syndrome across
  three subjects but gives no specific ages in the abstract. A structured `onset`
  descriptor was **not** added: `OnsetEnum` (the schema range for `onset_category`) has no
  `VARIABLE` member (its values are ANTENATAL/EMBRYONAL/FETAL/CONGENITAL/NEONATAL/
  INFANTILE/CHILDHOOD/JUVENILE/YOUNG_ADULT/MIDDLE_AGE/LATE/PUERPERAL), so the reviewer's
  suggested `onset_category: VARIABLE` would not validate, and no numeric ages are
  available for the quantitative fields. The variable onset is captured in prose instead.
- **Lactic acidosis.** The conserved module carries a "Lactic Acidosis and Metabolic
  Decompensation" node; the founding abstract does not mention lactic acidosis, so it is
  intentionally not modeled (omission is defensible; revisit if a full-text or additional
  case series documents it).
- **Combined-OXPHOS biology.** The CO3/CYB processing role and the severe combined-OXPHOS
  null phenotype (PMID:40637235) are mechanistic context, not the human disease
  presentation; left out of the disease nodes to avoid over-asserting beyond the clinical
  phenotype.

## Verified source list

- PMID:40499538 — *Am J Hum Genet* 2025 (founding clinical report) — verified.
- PMID:25683715 — *Cell Rep* 2015 (MRG discovery; FASTKD5 non-tRNA-flanked mRNA processing) — verified.
- PMID:40637235 — *Nucleic Acids Res* 2025 (FASTKD5 noncanonical cleavage of CO1/CO3/CYB) — verified.
- PMID:29036396 — *Nucleic Acids Res* 2017 (FASTK family review) — verified (DOI 10.1093/nar/gkx772; an automated search initially mis-returned PMID 28335001, which is a different FASTKD1/FASTKD4 paper — rejected per anti-NEC check).
