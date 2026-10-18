# IMD122 Research Notes

## Identity
- Immunodeficiency 122 (IMD122); OMIM:620869; MONDO:0971151; DOID:0061088; MedGen C5935632/1860800; UMLS C5935632
- Gene: POLD3; HGNC:20932; Entrez 10714; Ensembl ENSG00000077514; chr 11q13.4 (GRCh38 11:74,493,851-74,669,117, + strand); NM_006591.3
- Protein: 66-kDa accessory subunit of DNA polymerase delta (PolD); interacts with PCNA; part of complex with catalytic POLD1 + accessory POLD2, POLD4
- Inheritance: Autosomal recessive; both probands consanguineous

## Variants
- p.Ile10Thr (NM_006591.3) homozygous, Lebanese consanguineous family — abolishes POLD3, POLD1, POLD2 expression (PMID 37030525)
- c.1118A>C p.K373T homozygous — Omenn syndrome (PMID 38099988)

## Phenotype (HPO from Monarch)
SCID (HP:0000958); Omenn features: erythroderma (HP:0410377), increased IgE (HP:0002716), eosinophilia (HP:0001999), oligoclonal T cell expansion (HP:0010975), lymphadenopathy (HP:0002110), hepatomegaly (HP:0004429), splenomegaly (HP:0002783), alopecia (HP:0008404); decreased total T cells (HP:0500093), decreased naive CD4/CD8 (HP:0001744/HP:0005359), reduced NK (HP:0000407), low IgG (HP:0001019), thymus aplasia (HP:0004430); neurodevelopmental: global dev delay (HP:0001596), motor delay (HP:0002718); sensorineural hearing loss (HP:0001880); frontal bossing (HP:0003212), abnormal facial shape (HP:0410378); ectodermal: enamel hypoplasia (HP:0011968), nail dystrophy (HP:0031430), dry skin (HP:0005403); infections: recurrent viral/bacterial/URTI/LRTI (HP:0002788/HP:0001270/HP:0001263/HP:0032126), bronchiectasis (HP:0002007); food allergy (HP:0006297), feeding difficulties (HP:0002240).

## Mechanism
Biallelic POLD3 missense -> destabilized/LOF Pol delta -> defective S-phase entry + dsDNA breaks (rescued by WT POLD3) -> impaired lymphoid progenitor proliferation + defective TCR/V(D)J recombination -> naive T-cell lymphopenia, restricted TCR repertoire, oligoclonal expansion -> SCID/Omenn. Non-immune replication stress -> neurodev delay, hearing loss, ectodermal/skeletal.

## Treatment
- HSCT (one patient transplanted at 6 months; died at age 4 of progressive neurological regression) — PMID 38099988
- Supportive: Ig replacement, antimicrobial prophylaxis (standard SCID care; inferred)

## Related context
- POLD1 / POLD2 mutations cause syndromic CID with T-cell lymphopenia +/- intellectual disability + SNHL (cited in PMID 37030525). POLD1 also linked to MDPL syndrome (mandibular hypoplasia, deafness, progeroid, lipodystrophy) and colorectal cancer (germline CRC/polyposis) — distinct phenotype.

## Protein (UniProt Q15054)
- DNA polymerase delta subunit 3 (p66/p68); 466 aa; localization Nucleus + Cytoplasm (GO:0005634 nucleus; GO:0043625 delta DNA polymerase complex)
- Accessory subunit of BOTH Pol-delta (Pol-delta3/Pol-delta4 with POLD1/p125, POLD2/p50, POLD4/p12) AND Pol-zeta (translesion synthesis, with REV3L/REV7)
- Stabilizes Pol-delta; major role in Pol-delta stimulation by PCNA; high-fidelity replication incl. lagging strand + repair
- gnomAD constraint: pLI 0.994, LOEUF 0.48, LoF o/e 0.33, lof_z 4.36; missense unconstrained
- Mouse ortholog Pold3 (NCBI Gene 69745); Pold3-/- embryonic lethal E6.5 (PMID 29447390)

## Identifiers summary
- OMIM 620869; MONDO:0971151; DOID:0061088; MedGen C5935632; UMLS C5935632
- No dedicated Orphanet/ICD-10 code (ultra-rare, newly described 2023); ICD-11 would map to 4A00 (primary immunodeficiencies); MeSH: Severe Combined Immunodeficiency (D016511) / Omenn — no specific MeSH
- Synonyms: IMD122; POLD3 deficiency; DNA polymerase delta 3 deficiency; syndromic SCID due to POLD3; (presents as) Omenn syndrome

## Key refs
- PMID 37030525 Mehawej 2023 — first POLD3 case (p.Ile10Thr), syndromic SCID
- PMID 38099988 Riestra 2023 — POLD3 Omenn (p.K373T), functional S-phase/DSB rescue
- PMID 31449058 Conde 2019 JCI — POLD1/POLD2 PolD deficiency (parent syndrome)
- PMID 29447390 Zhou 2018 — Pold3 mouse KO embryonic lethal / ESC genomic instability

## TODO next iterations
- Fetch POLD1/POLD2 CID references (Conde et al.), gnomAD frequency of POLD3 variants
- Epidemiology (ultra-rare, <10 cases), prognosis
- Diagnostics (immune workup, TREC/newborn screen, WES), differential dx (RAG1/2 Omenn, DCLRE1C, etc.)
- Model organisms (Pold3 KO mouse embryonic lethal; chicken DT40 POLD3)
- Build final_report.md in iteration 4-5
