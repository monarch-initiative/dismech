---
provider: claude-code
model: claude-opus-5
disease_name: WAPL-Related Developmental Disorder
target_entry: kb/disorders/WAPL-Related_Developmental_Disorder.yaml
search_backend: NCBI E-utilities (esearch + esummary), PubMed
date: '2026-08-05'
pull_request: monarch-initiative/dismech#7730
artifacts: []
---

# WAPL-Related Developmental Disorder — Claude Code literature sweep

- **Target entry:** `kb/disorders/WAPL-Related_Developmental_Disorder.yaml`
- **Provider:** Claude Code (curation-scanner, high_effort tier) — not an external DR provider
- **Date:** 2026-08-05
- **Search backend:** NCBI E-utilities (`esearch` + `esummary`), PubMed
- **PR:** monarch-initiative/dismech#7730

## Why this artifact exists

The dismech review SOP requires a deep-research artifact for new disease entries.
Three successive reviews of #7730 flagged its absence. This is that sweep, run
directly against PubMed rather than through an external DR provider, which means
the usual DR failure modes are structurally excluded: every PMID below came back
from a live PubMed query, and every snippet subsequently curated was verified
against a `just fetch-reference` cache by `just validate-references`. There is no
provider-synthesised prose in this file to be hallucinated.

## NEC preflight

`just preflight-dr` compares gene mentions in a report against the canonical
causal gene of a MONDO term. It is **not applicable in the usual way here**, and
saying why is more useful than running it for the sake of a green tick:

- The entry deliberately carries **no `disease_term`** — no MONDO class exists for
  the monogenic entity (`wapl_mondo_term_request` tracks the new-term request).
- The nearest MONDO term, `MONDO:0012830`, denotes the **contiguous-gene** 10q22.3q23.3
  deletion syndrome, not the WAPL-driven monogenic disorder. Running the preflight
  against it would be expected to `WARN`/`FAIL` *by design*, because a correct
  WAPL report is dominated by WAPL while `MONDO:0012830`'s identity is the
  interval, not the gene. A `FAIL` there would be a true negative about the
  ontology mapping, not a Named Entity Confusion signal about this sweep.

The identity check that *is* meaningful was done manually, and is the reason the
entry models a subtype split rather than one blended graph:

| Anchor | Monogenic entity | Deletion entity |
|---|---|---|
| Gene | WAPL (`hgnc:23293`) | ~30 genes incl. WAPL, NRG3, BMPR1A, GRID1 |
| MONDO | none | `MONDO:0012830` |
| OMIM | none | 612242 |
| Primary source | PMID:42431198 / DOI:10.64898/2026.02.23.26346364 | PMID:17436248, PMID:21248748 |

Distinct-entity risk worth flagging for future curators: **10q23 deletion
literature is dominated by a different, PTEN-containing interval** (Bannayan-Riley-Ruvalcaba,
Cowden, prostate/glioma PTEN loss). Query Q2 below returned 248 hits of which the
large majority are that PTEN interval, not the LCR3-4 WAPL interval. A DR provider
querying "10q23 deletion" without an interval constraint would very plausibly
produce a coherent report about PTEN. Every deletion-arm claim curated from this
sweep was checked to be about the LCR3-4/BMPR1A interval specifically.

## Queries run

All against `db=pubmed`, Title/Abstract fields, `retmax` 60.

| # | Query intent | Hits |
|---|---|---|
| Q1 | `WAPL` AND (variant / patient / syndrome / developmental delay / neurodevelopmental / haploinsufficiency) | 31 |
| Q2 | (`10q22` OR `10q23`) AND (deletion / microdeletion / duplication) | 248 |
| Q3 | `"cohesin release factor"` OR (`WAPL` AND `"release factor"`) | 37 |
| Q4 | (`PDS5A` OR `PDS5B`) AND (variant / disease / patient / developmental) | 39 |
| Q5 | `WAPL` AND (loop / genome folding / TAD / Hi-C) | 48 |
| Q6 | `Wapl` AND (mouse / mice / knockout / conditional) | 50 |
| Q7 | (cohesinopathy OR `"Cornelia de Lange"`) AND (episignature / methylation signature) | 11 |

## Findings incorporated into the entry

Four references were fetched with `just fetch-reference` and cited. All snippets
verified: `65/91` by the validator, the remaining 26 being `DOI:`-prefixed
preprint snippets the validator skips by prefix and which were hand-verified.

| PMID | Why it mattered | Where it landed |
|---|---|---|
| **31561016** | **Highest-value finding of the sweep.** The recurrent deletion removes one copy of *BMPR1A*, a juvenile-polyposis gene. Reported adult had severe JPS requiring preventive colectomy at 25 and died of gastric adenocarcinoma at 32. The paper's argument is that polyps were never previously reported because CNV arrays now diagnose the deletion years before the digestive phenotype, and it recommends active digestive surveillance. This is the entry's only cancer-predisposition and only actionable-surveillance content, and it was absent. | New `Hamartomatous Polyposis` phenotype (`HP:0004390`) on the 10q Deletion subtype; supporting evidence on the `Contiguous Loss of Neighbouring Genes` node |
| **36449618** | Sci Adv 2022 — >1000 genes dysregulated in `Wapl^Δ/+` embryonic mouse brain, with patterns highly similar to `Nipbl^+/-`, explicitly predicting that WAPL mutations would cause human disease. Published four years before the clinical delineation, so it is a non-circular model-organism prior for the whole WAPL → transcription → neurodevelopment chain. Also shows lowering Wapl dosage *partially corrects* the CdLS model — the two disorders are antagonistic, not merely adjacent. | `Transcriptional Dysregulation` node (MODEL_ORGANISM); Cornelia de Lange differential |
| **33318687** | Nat Genet 2021 — corrects an intuition the loop-extension model invites. WAPL turnover frees cohesin for reloading, so WAPL ablation *depletes* cohesin from cell-type-specific regulatory sites and loses promoter-enhancer loops, rather than simply leaving cohesin in place. Supplies the missing step between the folding defect and the transcriptional one. | `Transcriptional Dysregulation` node (IN_VITRO) |
| **34070827** | IJMS 2021 review — Pds5 knockout mice have cardiac, palatal and skeletal defects but **no brain phenotype**, unlike Wapl heterozygotes. The strongest available counterweight to PDS5A/PDS5B being neurodevelopmental disease genes. Curated as `REFUTE`, with the caveat that the two published Pds5 mouse models disagree with each other. | `wapl_pds5a_pds5b_validity` KNOWLEDGE_GAP discussion |

## Findings deliberately NOT incorporated

Recording these matters as much as the positives — they are the boundary of the sweep.

- **PMID:28588438, PMID:35707596, PMID:34365621** — additional single-case reports
  of the LCR3-4 10q22.3q23.2 microdeletion. Real and on-interval, but each adds one
  case to a phenotype already delineated by the 41-carrier rCNV cohort and the
  27-case literature review inside the primary source. Citing them would inflate the
  reference count without changing any claim or band.
- **Q2's PTEN-interval bulk** (Bannayan-Riley-Ruvalcaba, Cowden, juvenile polyposis
  *via PTEN*, prostate/glioma PTEN loss) — a different 10q23 interval. Excluded on
  identity grounds. Note that dismech already has a `Bannayan-Riley-Ruvalcaba
  Syndrome` entry; it is a distinct entity and this entry does not overlap it.
- **PMID:31905366 (cohesin-CTCF structural basis), PMID:41807408 (sororin/exit gate),
  PMID:39110738 (Wapl-cohesin interaction mechanism)** — cohesin cell biology at a
  level of molecular detail below what the entry's `Impaired Cohesin Release from
  Chromatin` node claims. The node is already supported by PMID:17113138 and
  PMID:28475897.
- **PMID:41994921** — Pds5a/Pds5b constrain long-range chromatin interactions in
  vertebrate embryos. Relevant to the PDS5 arm, but it addresses chromatin
  architecture rather than the disease-gene-validity question the discussion asks.
- **Cancer / somatic cohesin literature** (myeloid malignancy cohesin mutations,
  WAPL overexpression in cervical cancer, various prognostic-marker papers) — somatic
  rather than germline, out of scope for this entry.
- **PMID:40916800** — a 2025 review of WAPL in cell biology and disease. Predates the
  clinical delineation and would be cited for background only.

## Residual gaps this sweep did not close

1. **No `variants:` block.** Blocked at source, not by search: the medRxiv preprint
   has had case-level data removed from Table 1, Table S4, Fig. 2 and Fig. S12 per
   medRxiv policy. Tracked in `wapl_full_text_curation`.
2. **`ORPHA:276413` still uncached** — `just refresh-orphadata` fails on an
   `en_product1.xml` checksum mismatch against `data/orphadata/MANIFEST.yaml`.
   Re-pinning is a repo-wide operation. Tracked in
   `wapl_10q_deletion_orphanet_phenotypes`.
3. **No treatments.** No WAPL-specific therapy exists. The digestive-surveillance
   recommendation from PMID:31561016 is curated as phenotype `notes` rather than as a
   `treatments:` entry, since it is a deletion-subtype surveillance action rather
   than a therapy for the disorder.
4. **No GeneReviews chapter** exists for either the gene-disease relationship (first
   published 2026) or the 10q22q23 deletion syndrome.

## Reproducibility

The queries above are plain PubMed Title/Abstract queries and can be re-run
verbatim. Counts will drift as PubMed grows. The four incorporated references are
cached under `references_cache/PMID_{31561016,33318687,34070827,36449618}.md`,
created by `just fetch-reference` and never hand-edited.
