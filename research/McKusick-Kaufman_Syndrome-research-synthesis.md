# McKusick-Kaufman Syndrome — Deep Research Synthesis

- **Disease:** McKusick-Kaufman syndrome (MKS)
- **MONDO:** MONDO:0009367 · **Gene:** MKKS/BBS6 (hgnc:7108)
- **Method / provider:** dismech deep-research harness over **PubMed (NCBI E-utilities via MCP)** — fan-out search → fetch abstracts → adversarial PMID↔claim↔quote verification → synthesis. No third-party DR synthesizer (Falcon/Asta/OpenScientist) was used; every citation below is a primary PubMed source whose quoted snippet was verified as an exact substring of the cached abstract (`references_cache/PMID_*.md`) with the dismech reference validator.
- **GeneReviews baseline:** PMID:20301675 (tagged `GeneReviews` in the entry `references:` block).

## Verified findings integrated into the entry

### Gene / mechanism
- **Causative chaperonin gene (discovery).** PMID:10802661 — *"The MKKS predicted protein shows amino acid similarity to the chaperonin family of proteins, suggesting a role for protein processing in limb, cardiac and reproductive system development."* (Subject ties the chaperonin to all three triad branches.)
- **Divergent CCT/TRiC-derived chaperonin in the pericentriolar material.** PMID:15731008 — *"the majority of BBS6 resides within the pericentriolar material (PCM)"*; cytokinesis defects on RNAi.
- **Mutant misfolding / CHIP-mediated degradation.** PMID:18094050 — *"the MKKS mutants have an abnormal conformation and ... chaperone-dependent degradation mediated by CHIP is a key feature of MKKS/BBS diseases."*

### Non-ciliary CHD mechanism (model-system; HUMAN_MODEL_MISMATCH)
- PMID:28753627 — *"Mutations in BBS6 cause two clinically distinct syndromes ... McKusick-Kaufman syndrome, a genetic disorder characterized by congenital heart defects"*; *"BBS6 is actively transported between the cytoplasm and nucleus, and that BBS6H84Y; A242S, is defective in this transport"*; identifies a non-ciliary nuclear-cytoplasmic transport function (SMARCC1/SWI-SNF chromatin remodeling) underlying MKS CHD. Flagged as a HUMAN_MODEL_MISMATCH discussion (zebrafish/cell models; human cardiac fidelity unconfirmed).

### Genotype–phenotype (allelic model)
- **null → BBS, specific missense → MKS.** PMID:15772095 (Mkks-null mouse) — *"the complete absence of MKKS leads to BBS while the MKS phenotype is likely to be due to specific mutations."* PMID:10973251 — complete loss of function → BBS.
- **No reliable clinical correlation / continuum.** PMID:22090721 — *"significant clinical overlap between MKS and BBS-6 in childhood."* PMID:26900326 — an MKKS/BBS6 H395R allele causes RP + polydactyly only, *"do not always result in classic MKKS or BBS findings."* Captured as a KNOWLEDGE_GAP discussion.

### Inheritance / epidemiology
- PMID:9467007 — *"diagnosed most frequently in the Old Order Amish population ... autosomal recessive ... with reduced penetrance and variable expressivity."* (Corrected an initial Hutterite assumption to **Old Order Amish**.)
- PMID:35860126 — rarity; perinatal case + literature review.

### Clinical surface (GeneReviews PMID:20301675)
- Triad detail (HMC neonatal cystic mass; PAP ulnar/fibular); CHD spectrum incl. atrioventricular canal; **male genital malformations: hypospadias, cryptorchidism, chordee**; molecular diagnosis; BBS differential with age caution; treatments (HMC surgery, supportive surveillance, genetic counseling, **25% sib recurrence**); **agents/circumstances to avoid: anesthesia caution in the neonate from HMC diaphragmatic compression**.

## Anti-hallucination notes
- **Chordee ontology ID corrected:** the PR #4328 review suggested `HP:0000023` for chordee, but `HP:0000023` is **Inguinal hernia**; the correct term is **HP:0000041 (Chordee)**, used here. Verified with OAK.
- All PMIDs and quotes independently re-derived from PubMed and verified as exact substrings; none taken on faith from prior recall or third-party synthesis.

## Provenance / relationship to PR #4328
This entry consolidates the dismech BBSome-opathy work with the genuinely additive content from the parallel draft PR #4328 (dragon-ai-agent): the non-ciliary nuclear-transport CHD mechanism node, the male-genital and atrioventricular-canal phenotypes, and the diagnosis/differential/treatments sections — all re-verified here against freshly fetched caches.
