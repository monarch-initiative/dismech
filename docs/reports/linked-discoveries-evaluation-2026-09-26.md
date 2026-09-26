# NLM Linked Discoveries as a literature-discovery source

**Date:** 2026-09-26
**Source evaluated:** <https://linkeddiscoveries.ncbi.nlm.nih.gov/>
**Question:** does Linked Discoveries help curators find literature and content gaps for
dismech disease entries, and could any of it be automated?

## Verdict

**Useful as a manual literature-discovery aid seeded from an entry's own papers. Not
usable as a source of KB content, and not suitable for an automated pipeline.**

- Its **article neighbourhoods** are complementary to PubMed's "Similar articles": they
  overlap only ~25–30 % with them, and recovered more of each entry's own citations. The
  recent uncited papers they surface look like genuine curation leads.
- Its **human gene tags** point at a few real gaps (IL18R1 for asthma; BRAF and PIK3CA
  for pancreatic ductal adenocarcinoma), mixed with stale candidate genes and mouse
  model-construction genes. Leads only.
- Its **MedGen disease tags** contain systematic abbreviation mis-normalizations
  (PDAC, CAF and ADM each resolve to an unrelated rare syndrome). They must not be used
  to classify or filter literature for dismech.
- It has **no documented API** and describes itself as an early-stage pilot, so nothing
  in CI or a recipe should depend on it.

## What the resource is

Linked Discoveries is an NLM pilot that, for a seed PubMed article, retrieves the most
semantically similar PubMed records (BiomedBERT embeddings of title, abstract and
keywords; 49 by default, up to 200). Each article is annotated with:

- MedGen condition CUIs, NCBI Gene IDs (human and model organism), PubChem CIDs
- citation edges within the neighbourhood (cites / cited-by)
- review, retraction, erratum, expression-of-concern and NIH-funding flags
- the full abstract

The site states that results "may be incomplete or inaccurate" and that small
differences in similarity score are not meaningful.

**Access.** The only supported export is a browser "Download CSV" button. The web page
itself obtains the whole neighbourhood as JSON from a single undocumented request
(`POST /<PMID>/links/` with a CSRF token taken from the page's cookie and a
`neighbors` form field). That is what this evaluation used; it works, but it is an
internal endpoint of a pilot service and may change without notice.

## Method

Three existing entries, one per disease class, each seeded from three papers the entry
already cites, 200 neighbours per seed:

| Entry | Seeds |
|---|---|
| `Marfan_Syndrome` (Mendelian) | PMID:8180508 (FBN1 defects in Marfan syndrome), PMID:16928994 (aneurysm syndromes caused by TGF-beta receptor mutations), PMID:34916231 (FBN1 variant types and severe scoliosis) |
| `Pancreatic_Ductal_Adenocarcinoma` (cancer) | PMID:26592447 (p53 mutations cooperate with oncogenic Kras), PMID:33347393 (driver mutations KRAS/CDKN2A/TP53/SMAD4), PMID:30366930 (IL1/JAK-STAT vs TGFβ in CAF heterogeneity) |
| `Asthma` (common) | PMID:21276132 (asthma GWAS review), PMID:42613890 (eosinophilic inflammation in severe asthma), PMID:27177493 (mepolizumab by eosinophil threshold) |

The union of each entry's three neighbourhoods was compared with the entry's cited PMIDs
and HGNC-bound genes, and with the top 200 PubMed "Similar articles" (E-utilities
`elink`, `pubmed_pubmed`) for the same seeds. An article was counted as on-topic if its
title or abstract matched the disease name (or, for Marfan, FBN1/fibrillin).

## Results

| | Marfan | PDAC | Asthma |
|---|---|---|---|
| Distinct articles (3 × 200 neighbours) | 557 | 602 | 598 |
| On-topic | 418 (75 %) | 548 (91 %) | 565 (94 %) |
| Published 2023 or later | 87 | 193 | 153 |
| Entry's cited PMIDs recovered | 18 / 79 | 9 / 70 | 8 / 152 |
| … by PubMed similar articles (top 200/seed) | 17 | 3 | 5 |
| … recovered only by Linked Discoveries | 7 | 6 | 4 |
| Overlap with PubMed similar articles | 182 | 146 | 152 |
| Articles carrying any gene tag | 49 % | 46 % | 11 % |

Low recall of the entries' own citations is expected: 600 nearest neighbours of three
seeds cover a narrow slice of the literature. What matters is whether the slice is
relevant and different from what PubMed already offers, and on both counts it is.

### Article neighbourhoods

The neighbourhood is dominated by the seed's specific topic rather than the disease as
a whole:

- The TGF-beta-receptor seed returns mostly **Loeys-Dietz syndrome** papers, which
  accounts for the lower Marfan on-topic rate.
- The mepolizumab seed pulls in ~30 papers on mepolizumab in **eosinophilic COPD and
  EGPA** — pharmacologically related, but not asthma.
- The PDAC driver-mutation seed pulls in KRAS/TP53 prognostic meta-analyses in
  **colorectal and lung cancer**.

Within the on-topic set, recent uncited papers are plausible leads, for example:

- **PDAC:** single-cell and spatial studies of cancer-associated fibroblast subtypes
  (PMID:42520475, PMID:42373588), KRAS-variant-specific tumorigenesis (PMID:42480541).
- **Marfan:** a 2026 Loeys-Dietz care-management primer (PMID:41988792), FBN1
  genotype–phenotype series (PMID:42663022), microfibril changes in SMAD3 variant
  carriers (PMID:42273728).
- **Asthma:** IL-5 pathway reviews and real-world mepolizumab/benralizumab outcome
  studies (PMID:42674274, PMID:42723568).

These are leads, not evidence. Each still goes through `just fetch-reference` and an
exact-quote snippet, and being close to a seed says nothing about whether a paper
supports a claim.

### Gene tags

Most frequently tagged genes not bound in the entry:

| Entry | Tagged, not in entry | Assessment |
|---|---|---|
| Asthma | IL18R1, DPP10, NPSR1, PHF11, MS4A2; IL33 and IL1RL1 (tagged as `IL33R`) | IL18R1 and IL33/IL1RL1 are well-replicated GWAS loci; the entry cites a paper on IL33/IL1RL1 but has no gene record or pathophysiology node for either. DPP10, NPSR1 and PHF11 are 2003–2004 positional-cloning candidates with mixed replication. |
| PDAC | BRAF, PIK3CA, EGFR (prose only), Ptf1a, Hras, Trp53, Gt(ROSA)26Sor | BRAF (in KRAS-wild-type tumours) and PIK3CA are real gaps. Ptf1a, ROSA26 and Trp53 are components of engineered mouse models (Cre drivers, reporter loci), not disease genes. |
| Marfan | TGFB2, TGFB3, FBN2, COL3A1, MYH11 | TGFB2 and TGFB3 are already named in the entry's Loeys-Dietz differential; FBN2 (congenital contractural arachnodactyly) appears only in a cited title. COL3A1 and MYH11 are thoracic-aortic differential genes and belong to other entries. |

Gene tags also include tags not supported by the abstract: `Hras` (mouse) is attached
to 72 PDAC papers, none of whose abstracts mention Hras or H-Ras — they are Kras mouse
model papers. The tagging source is not documented, so the reason is unknown.

Entry genes the tags never surfaced (e.g. NRG1, MLH1, ATM for PDAC; NFKB1, STAT3,
TNFAIP3 for asthma) show that absence of a tag is not evidence of absence, as the
user guide also states.

### Disease (MedGen) tags

Abbreviations are resolved to unrelated MedGen concepts that share the acronym:

| Text in abstract | Tagged as | Articles affected |
|---|---|---|
| PDAC (pancreatic ductal adenocarcinoma) | *Microphthalmia, syndromic 9* (alias "PDAC syndrome") | 26 |
| CAF / CAFs (cancer-associated fibroblasts) | *Conotruncal anomaly face syndrome* (CAF) | 21 |
| ADM (acinar-to-ductal metaplasia) | *Amyopathic dermatomyositis* | 7 |
| eosinophilic granulomatosis with polyangiitis | *Granulomatosis with polyangiitis* (partial-span match) | 25 |

This is the Named Entity Confusion failure dismech's evidence workflow already guards
against, produced systematically by the tagger. It rules out using these tags to select
papers "about" a disease or to propose `disease_term`, phenotype or comorbidity content.

### Chemical tags

Weak. Correct hits (losartan for Marfan; gemcitabine, irinotecan, caerulein for PDAC;
methacholine, budesonide for asthma) are mixed with registry numbers used as names
("7728-73-6", "609-36-9"), UNII codes ("KN7U54F9LQ") and spurious amino-acid matches
(L-cysteine on 16 Marfan papers).

### Retractions

Two retracted papers appeared in the PDAC neighbourhoods (PMID:22806240, PMID:28230016);
neither is cited anywhere in `kb/`. None of the 301 PMIDs cited by the three entries is
retracted, checked directly against PubMed publication types via E-utilities
`esummary`. A KB-wide retraction check should use E-utilities directly; Linked
Discoveries only flags retractions for articles that happen to fall in a neighbourhood.

## Recommendations

1. **Use it manually as a discovery aid.** When curating or refreshing an entry, open
   Linked Discoveries on two or three of the entry's mechanism-level papers and scan
   the recent, uncited, on-topic articles. Seed choice dominates the result; seed from
   the node being curated, not from a general review.
2. **Treat human gene tags as leads only.** A report of frequently tagged human genes
   absent from an entry surfaced real gaps here, but model-organism tags and stale
   candidate genes must be filtered by a curator, and nothing should be written to an
   entry from a tag.
3. **Do not use the MedGen disease tags or chemical tags** for any dismech purpose.
4. **Do not build a recipe or CI step on it** while the only machine access is the
   web page's internal endpoint. Revisit if NLM publishes an API or bulk export.
5. **Do not treat neighbourhood similarity as evidence strength.** The resource itself
   warns that scores within a neighbourhood are nearly indistinguishable.
