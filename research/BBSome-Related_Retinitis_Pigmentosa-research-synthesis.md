# BBSome-Related Retinitis Pigmentosa — Deep Research Synthesis

- **Disease:** BBSome-related retinitis pigmentosa (mechanism-anchored, cross-gene lump for non-syndromic RP at BBSome-machine loci)
- **disease_term:** MONDO:0019200 (retinitis pigmentosa); federates per-locus MONDO nodes via `mappings`.
- **Method / provider:** dismech deep-research harness over **PubMed (NCBI E-utilities via MCP)** — fan-out search → fetch abstracts → adversarial PMID↔claim↔quote verification → synthesis. No third-party DR synthesizer was used; every quoted snippet was verified as an exact substring of the cached abstract with the dismech reference validator.

## Curation discipline (mechanism vs association split)
The lump's MECHANISM (BBSome trafficking failure → rod photoreceptor degeneration) is transferred by conformance to the `bbsome_trafficking` and `photoreceptor_degeneration` modules, where it is richly evidenced. Each LOCUS→human-RP ASSOCIATION rests on its own (often single-family / n-of-1) report and is not inflated by borrowing the Bardet-Biedl syndrome evidence. Per-locus ClinGen Gene-Disease Validity grading is a documented follow-up (pinned ClinGen snapshot needs refresh).

## Verified findings (loci integrated into the entry)

### Keystone spectrum locus
- **BBS1.** PMID:23143442 — *"The 14 patients with 2 BBS1 variants showed the entire clinical spectrum, from nonsyndromic RP to full-blown BBS."*; *"Variants in BBS1 are significantly associated with nonsyndromic autosomal recessive RP and relatively mild forms of BBS."* (The keystone for "organ-restricted expressivity along one allelic series".)

### Solid loci
- **TTC8/BBS8 (RP51).** PMID:20451172 — *"an in-frame splice mutation in BBS8 ... is sufficient to cause nonsyndromic retinitis pigmentosa (RP)"*; retina-specific exon *"expressed exclusively in the retina and enriched significantly in the photoreceptor layer."*
- **ARL6/BBS3 (RP55).** PMID:21282186 — consanguineous family with *"isolated retinitis pigmentosa identified a missense mutation in BBS3"*; the BBS3 A89V allele *"only present with isolated retinitis pigmentosa"* (zebrafish functional; evidence_source MODEL_ORGANISM).

### Loci added by this deep-research pass
- **BBS2.** PMID:25541840 — *"BBS2 mutations can cause nonsyndromic retinitis pigmentosa"* (4 missense mutations, Moroccan/Ashkenazi Jewish families).
- **BBS9.** PMID:22353939 — *"the occurrence of nonsyndromic retinitis pigmentosa in a family with a novel BBS9 mutation."* PMID:38534779 — a **hypomorphic** BBS9 splice allele → mild, essentially non-syndromic rod-cone dystrophy; directly evidences the partial-loss → photoreceptor-restricted mechanism on the proximal pathophysiology node.

## Scope discipline
Strict BBSome machine + dedicated operators only (subunits + chaperonins + ARL6/LZTFL1/IFT27). IFT-B (IFT172, IFT74) and transition-zone (CFAP418, etc.) loci that also cause non-syndromic RP are deliberately out of scope and belong to the broader ciliopathy spectrum.

## Anti-hallucination notes
All PMIDs and snippets independently re-derived from PubMed and verified as exact substrings of freshly fetched caches; the MODEL_ORGANISM vs HUMAN_CLINICAL split is set per the study type reported in each paper.
