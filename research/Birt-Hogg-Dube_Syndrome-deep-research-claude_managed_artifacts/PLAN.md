# Research Plan: Birt-Hogg-Dubé Syndrome (MONDO:0800444; gene FLCN)

## Interpretation
The request is a knowledge-base style disease characterisation of Birt-Hogg-Dubé
syndrome (BHD), the autosomal-dominant cancer-predisposition / genodermatosis caused by
germline loss-of-function variants in **FLCN** (folliculin, 17p11.2). The template's 15
sections are followed as the report structure (the template asks for its own sections, so
the report follows them rather than a free-form review), ending with Open Questions and
References. The template's OMIM field says "not recorded"; any OMIM number used will
come from evidence files only (the classic BHD entry, if found, is cited as retrieved). Where a
template item is not applicable (e.g., infectious agents, vaccines, repeat expansions), the
report says so explicitly. Ontology term suggestions (HPO, GO, CL, UBERON, NCIT, CHEBI)
are offered as curator suggestions; they are not factual claims requiring citation, but
are labelled as suggestions.

## Sub-questions and likely sources

1. **Definition, identifiers, nomenclature, history, diagnostic criteria** — OMIM, Orphanet,
   MeSH, GeneReviews, Menko 2009 European BHD Consortium criteria, original Birt/Hogg/Dubé 1977 paper, recent reviews.
2. **FLCN gene and variant spectrum** — Nickerson 2002 discovery, C8 tract hotspot
   c.1285dup/del, LOVD/ClinVar, large deletions, splice variants, missense functional studies,
   founder variants, de novo cases, somatic second hits in tumours.
3. **Cutaneous phenotype** — fibrofolliculoma/trichodiscoma/acrochordon frequencies,
   onset age, histology, QoL, laser/surgical and topical rapamycin therapy.
4. **Pulmonary phenotype** — lung cyst prevalence/morphology on CT, pneumothorax
   frequency, age, recurrence, pleurodesis, smoking, the stretch hypothesis, cohort studies (NIH, Dutch, Asian).
5. **Renal phenotype** — RCC risk (penetrance), histotypes (hybrid oncocytic/chromophobe,
   oncocytoma), age at diagnosis, bilateral/multifocal, surveillance (MRI), 3-cm rule, nephron-sparing surgery, metastatic disease outcomes.
6. **Molecular mechanism** — FLCN–FNIP1/2, Rag/RagC-D GAP activity, lysosomal mTORC1,
   TFE3/TFEB nuclear localisation, AMPK, mitochondrial biogenesis/PGC1α, cilia/Wnt, TGF-β, cryo-EM structure of LFC complex.
7. **Model organisms and other species** — kidney-specific Flcn KO mice, Flcn+/- mice,
   Tfe3 rescue, Nihon rat, German Shepherd dog RCND, Drosophila, C. elegans, zebrafish, yeast Lst7; orthologs.
8. **Epidemiology, inheritance, penetrance, population differences** — prevalence
   estimates (including gnomAD-based), founder effects, Asian vs European phenotype, sex ratio, penetrance and expressivity.
9. **Diagnosis, genetic testing, differential diagnosis, surveillance guidelines** — Menko 2009,
   2015 Lancet Oncol recommendations, GeneReviews, testing of primary spontaneous pneumothorax cohorts, differentials (LAM/TSC, LCH, Cowden, HLRCC).
10. **Treatment and clinical trials** — RCC management, systemic therapy (mTOR inhibitors,
    VEGF TKIs, immunotherapy) in BHD RCC, topical rapamycin RCT, ClinicalTrials.gov NCTs, pneumothorax management.
11. **Other associated tumours, prognosis, mortality, quality of life** — colorectal neoplasia,
    parotid oncocytoma, melanoma, thyroid; survival, QoL / psychological burden.
12. **Molecular profiling of BHD tumours** — transcriptomics, genomic profiling, single-cell,
    TCGA chromophobe, epigenetics, metabolomics of FLCN-deficient tissue.

Each sub-question is assigned to one retrieval agent; thin areas get a second smaller run.

## Execution notes
- Run 1: 12 retrievers (one per sub-question above); all succeeded; ~155 evidence files.
- Run 2 (gap filling): ontology term records (HPO, GO, CL, UBERON, NCIT, ChEBI, HGNC, UniProt), ortholog/taxon/OMIA/VBO/MGI identifiers, and thin clinical topics (de novo variants, childhood pneumothorax, pregnancy, tumour growth, metastasis <3 cm, lung-function trends).
