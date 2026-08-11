---
provider: claude-deep-research
model: claude-opus-4-8
harness: dismech PR-shepherd literature sweep (targeted WebSearch + WebFetch, PubMed/OMIM/review cross-check)
cached: false
generated: '2026-06-23T00:00:00Z'
template_variables:
  disease_name: COX4I2-Related Pancreatic Insufficiency-Anemia-Hyperostosis Syndrome (EPIDACH)
  mondo_id: MONDO:0012992
  category: Mendelian
verification:
  searches_run: 4
  sources_fetched: 1
  primary_papers_found: 1
  primary_papers_cited_before: 1
  new_primary_papers_added: 0
note: >
  Provenance artifact generated to satisfy the new-entry deep-research requirement
  for PR #4689 (review by ai4c-agent, 2026-06-21/22/23). This was a targeted
  literature-completeness sweep rather than the full fan-out adversarial harness:
  because COX4I2-related disease (EPIDACH) is ultra-rare and the primary literature
  is essentially a single founding report, the goal was specifically to confirm
  whether any subsequent primary literature (new families, novel variants,
  functional studies) had been missed in the 17 years since the 2009 discovery. It
  had not: the sweep surfaced no additional primary case reports. The single
  defining paper PMID:19268275 (Shteyer et al. 2009) remains the only primary
  source, so no new snippet-validated evidence was added to the YAML as a result of
  this sweep. This file documents research provenance only; the authoritative,
  snippet-validated evidence lives in the YAML. Do not import claims from this file
  without re-verifying the snippet against the cited primary source via
  `just fetch-reference` + `just validate-references`.
---

# COX4I2-Related Pancreatic Insufficiency-Anemia-Hyperostosis Syndrome (EPIDACH) — Deep Research Report

**Disease:** COX4I2-related exocrine pancreatic insufficiency, dyserythropoietic
anemia, and calvarial hyperostosis (EPIDACH); MONDO:0012992 classifies it under
mitochondrial complex IV (cytochrome c oxidase) deficiency
**MONDO:** MONDO:0012992 &nbsp;|&nbsp; **OMIM phenotype:** 612714 &nbsp;|&nbsp;
**Gene:** COX4I2 (HGNC:16232; OMIM:607976; chr20q11.21) &nbsp;|&nbsp; **Inheritance:** autosomal recessive

## Executive Summary

EPIDACH is an ultra-rare autosomal recessive multisystem disorder caused by a
biallelic missense mutation in **COX4I2**, the gene encoding the lung/acinar-biased,
hypoxia-responsive isoform 2 of structural subunit 4 (COX4) of cytochrome c oxidase
(mitochondrial respiratory chain Complex IV). Unlike the encephalomyopathic /
Leigh-like presentation typical of most nuclear COX-assembly defects, COX4I2 disease
presents as a distinctive **non-neurological triad**: congenital exocrine pancreatic
insufficiency (steatorrhea, malabsorption of lipid-soluble vitamins, failure to
thrive), dyserythropoietic anemia, and calvarial hyperostosis. The mechanistic
hallmark is **tissue-biased** Complex IV deficiency: COX4I2 is the predominant COX4
isoform in pancreatic acinar cells, so its loss selectively impairs oxidative
phosphorylation in tissues that depend on it, while sparing tissues where the
ubiquitous COX4I1 isoform predominates.

The primary human literature is exceptionally small and, after this sweep, considered
complete. It comprises **one primary report**:

1. **Shteyer et al., 2009 (PMID:19268275, *Am J Hum Genet* 84(3):412–7)** — the
   founding and, to date, only primary report. Four patients with congenital
   exocrine pancreatic insufficiency, dyserythropoietic anemia, and calvarial
   hyperostosis were studied after cystic fibrosis, Shwachman-Bodian-Diamond,
   Pearson, and Johanson-Blizzard syndromes were excluded; homozygosity mapping
   identified a homozygous **COX4I2** mutation. The mutation markedly reduced COX4I2
   expression and attenuated its physiologic hypoxia response. (OMIM #612714
   describes 5 affected individuals from 2 consanguineous Arab Muslim families and
   records the variant as **c.412G>A, p.Glu138Lys [E138K]**; the specific nucleotide
   change is not named in the cached PubMed abstract, so the YAML cites only what the
   abstract states and does not assert the E138K detail as snippet-validated
   evidence.)

A separate ClinVar submission (`NM_032609.3(COX4I2):c.1-6C>T`, a 5′-UTR/splice-region
variant) is annotated to the same condition but is not backed by a distinct primary
clinical report and was not used as evidence.

No curative therapy exists; management is supportive — pancreatic enzyme replacement
therapy (PERT) for the exocrine pancreatic insufficiency, fat-soluble vitamin
supplementation, and transfusion/supportive care for the anemia.

## 1. Literature Completeness Check (the point of this sweep)

Targeted searches (PubMed/Google Scholar-style queries via WebSearch, plus a fetch of
the 2022 *Frontiers in Pediatrics* review of congenital exocrine pancreatic
insufficiency etiologies) were run to find any COX4I2/EPIDACH primary literature
published after the 2009 founding report:

- Queries combined the gene symbol (**COX4I2**) and the disease acronym/phenotype
  terms (**EPIDACH**, "exocrine pancreatic insufficiency", "dyserythropoietic
  anemia", "calvarial hyperostosis") with case-report / novel-variant / second-family
  modifiers across 2010–2025.
- The most authoritative secondary source surfaced, **Tóth et al. (2022),
  *Frontiers in Pediatrics* — "Congenital etiologies of exocrine pancreatic
  insufficiency"** ([10.3389/fped.2022.909925](https://doi.org/10.3389/fped.2022.909925)),
  cites **only Shteyer et al. 2009** for COX4I2 disease and explicitly states "To
  date 4 patients have been described with the disease," confirming no second cohort
  had been reported as of 2022.

**Result: no new primary papers.** The sweep surfaced no additional families, no
novel pathogenic variants beyond the founder allele, and no new functional studies.
The entry's reliance on the single PMID:19268275 citation is therefore appropriate
and reflects a complete primary literature, not an under-curated one. This mirrors
the situation for sibling ultra-rare nuclear COX-deficiency leaf entries (e.g.
PET100, TACO1) where the primary literature is likewise near-exhaustive.

## 2. Anti-NEC / Named-Entity Confirmation

EPIDACH is a member of the high-NEC-risk class flagged in #3889/#4239 (a
gene-numbered/eponymic mitochondrial-deficiency series with a "sanity-check
membership" caveat in the issue). The identity anchors were cross-checked:

- **Gene:** every search consistently resolved COX4I2 (HGNC:16232, chr20q11) to the
  EPIDACH phenotype; no competing gene dominated the literature.
- **OMIM:** the phenotype maps to OMIM #612714, consistent with MONDO:0012992
  (*pancreatic insufficiency-anemia-hyperostosis syndrome*).
- **Membership caveat:** MONDO files MONDO:0012992 under complex IV deficiency, but
  clinically EPIDACH is a distinct multisystem syndrome rather than a classic
  encephalomyopathy. Consistent with the PR, the entry **conforms_to** the
  `complex_iv_assembly_deficiency` module on mechanistic grounds (subunit loss →
  Complex IV biogenesis failure → tissue-biased bioenergetic failure) but the
  decision to add it to the `Mitochondrial_Complex_IV_Deficiency` grouping is left
  to a human maintainer (documented in the entry's `notes`).

## 3. Mechanism (as curated in the YAML)

- **COX4I2 subunit loss → failed Complex IV assembly.** COX4 is an essential
  structural subunit of cytochrome c oxidase; COX4I2 is the acinar/hypoxia-responsive
  isoform. Biallelic loss reduces COX4I2 expression and blunts the hypoxia response,
  destabilizing holoenzyme assembly in COX4I2-dependent tissues.
- **Impaired terminal electron transfer and ATP synthesis.** Reduced Complex IV
  activity impairs cytochrome-c-to-O₂ electron transfer and oxidative ATP synthesis.
- **Tissue-biased bioenergetic failure.** Because acinar pancreas, erythroid lineage,
  and calvarium rely on COX4I2, the deficit is selectively expressed there,
  producing the EPIDACH triad while sparing the CNS (in contrast to most nuclear COX
  defects).

## 4. Treatment / Management

No disease-modifying therapy. Supportive management curated in the entry:

- **Pancreatic enzyme replacement therapy (PERT)** — pharmacotherapy (pancrelipase)
  for exocrine pancreatic insufficiency and steatorrhea.
- **Fat-soluble vitamin (A/D/E/K) supplementation** — dietary intervention for the
  documented malabsorption / reduced vitamin E.
- **Supportive care** — transfusion and general support for the dyserythropoietic
  anemia.

## 5. Sources

- Shteyer E, Saada A, Shaag A, et al. *Exocrine pancreatic insufficiency,
  dyserythropoeitic anemia, and calvarial hyperostosis are caused by a mutation in
  the COX4I2 gene.* Am J Hum Genet. 2009;84(3):412–7. **PMID:19268275** —
  [PubMed](https://pubmed.ncbi.nlm.nih.gov/19268275/) /
  [doi:10.1016/j.ajhg.2009.02.006](https://doi.org/10.1016/j.ajhg.2009.02.006)
- OMIM #612714 — *Exocrine Pancreatic Insufficiency, Dyserythropoietic Anemia, and
  Calvarial Hyperostosis* — [omim.org/entry/612714](https://www.omim.org/entry/612714)
- Tóth et al. *Congenital etiologies of exocrine pancreatic insufficiency.* Front
  Pediatr. 2022;10:909925 —
  [doi:10.3389/fped.2022.909925](https://doi.org/10.3389/fped.2022.909925)
  (secondary review; cites only Shteyer 2009 for COX4I2)
- ClinVar RCV000395757 — `NM_032609.3(COX4I2):c.1-6C>T` annotated to EPIDACH
  (no distinct primary clinical report; not used as evidence)
