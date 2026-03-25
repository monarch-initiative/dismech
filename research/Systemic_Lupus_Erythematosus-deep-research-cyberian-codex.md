---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-02-01T14:04:10.190694'
end_time: '2026-02-01T14:47:49.161854'
duration_seconds: 2618.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Systemic Lupus Erythematosus
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: codex
    port: 3284
    skip_permissions: true
    manage_server: true
citation_count: 57
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Systemic Lupus Erythematosus
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Systemic Lupus Erythematosus**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


## Output

# Systemic Lupus Erythematosus Pathophysiology Report

## Introduction
Systemic lupus erythematosus (SLE; MONDO:0007915) is a systemic autoimmune disorder with heterogeneous organ involvement and a core immunologic theme of loss of tolerance to ubiquitous nuclear antigens.[medgen-6146-sle][crispin-2010-pathogenesis-human-sle] As summarized in a mechanistic review, "SLE is a systemic autoimmune disorder driven by an immune response directed against ubiquitous, mostly intranuclear, self-antigens," and patients can manifest "skin rash, photosensitivity" and other systemic features.[crispin-2010-pathogenesis-human-sle] The disease course is shaped by autoantibodies, immune complex formation, innate immune activation, and tissue-damaging inflammatory cascades that link molecular triggers to clinical phenotypes.[obermoser-2010-interferon-alpha-signature][crispin-2010-pathogenesis-human-sle]

## Core Pathophysiology
A recurring early step is defective handling of self-antigens derived from dying cells. In SLE, "apoptotic material and production of autoantibodies have long been recognized as major pathogenic events in this disease," emphasizing the connection between self-antigen exposure and autoimmunity.[obermoser-2010-interferon-alpha-signature] Consistent with this, disturbances in cell death and clearance are mechanistically important; one review notes that "Disturbances in apoptosis and/or clearance of apoptotic cells can play an important role in the pathogenesis of SLE."[crispin-2010-pathogenesis-human-sle]

Type I interferon (IFN) pathways form a central amplification loop. Plasmacytoid dendritic cells are highlighted as critical innate sensors because "pDCs ... are the main source of type I interferon (IFN) cytokines, which contribute to the immunopathogenesis of SLE."[kim-2015-pdc-ifn-axis-sle] This fits with the broader observation that "the type I interferon cytokine family has been postulated to play a central role in SLE pathogenesis," linking nucleic acid recognition to systemic immune activation.[obermoser-2010-interferon-alpha-signature]

Transcriptomic studies in blood reinforce the centrality of interferon programs and myeloid signatures. One study reported that the IFN gene expression "signature" served as a marker for more severe disease involving the kidneys, hematopoetic cells, and/or the central nervous system.[baechler-2003-interferon-signature-severe-sle] Another found that active SLE shows overexpression of granulopoiesis-related and IFN-induced genes and that immature neutrophils are present in many patients, indicating a granulopoiesis signature linked to disease activity.[bennett-2003-interferon-granulopoiesis-signature]

Complement biology adds an additional axis of susceptibility and tissue injury. Classical pathway deficiency is strongly associated with disease, with a review noting that "deficiency of early complement proteins from the classical pathway ... is strongly associated with development of systemic lupus erythematosus (SLE)."[macedo-2016-complement-classical] Complement and Fc receptor-mediated handling of immune complexes thereby influences both tolerance and end-organ inflammation.[macedo-2016-complement-classical]

Neutrophil extracellular traps (NETs) are another source of nuclear autoantigens and inflammatory signals. NETs are described as "web-like structures composed of chromatin backbones and granular molecules," and "an imbalance between NET formation and clearance in SLE patients may play a prominent role in the perpetuation of autoimmunity and the exacerbation of disease."[kaplan-2013-nets-sle] This integrates neutrophil biology into the self-amplifying cycles of autoantigen exposure and interferon-driven activation.

Neutrophil heterogeneity further refines this axis. A systems analysis notes that "SLE is characterized by elevated levels of a pathogenic neutrophil subset known as low-density granulocytes (LDGs)" and highlights functional diversity among neutrophil subsets.[li-2019-neutrophil-diversity-sle] A comprehensive review adds that "LDNs in SLE can secrete increased levels of type I interferon (IFN)" and readily form NETs, linking neutrophil subsets to IFN amplification and tissue damage.[carriere-2020-low-density-neutrophils-sle]

Endosomal nucleic-acid sensing via TLR7 and TLR9 is differentially regulated in SLE. In pDCs, TLR7-mediated IFN-alpha production is up-regulated and correlates with disease activity, whereas TLR9-mediated IFN-alpha production is down-regulated, indicating asymmetric tuning of these pathways.[takeda-2018-tlr7-ifn-pdc-sle] In B cells, TLR9 responses are impaired, with defective upregulation of activation molecules and diminished cytokine production, and this defect is restricted to B cells rather than pDCs, suggesting loss of TLR9 tolerogenic function contributes to the break of B cell tolerance.[mahdavi-2018-tlr9-bcells-sle]

Mitochondrial stress and oxidized mitochondrial DNA (mtDNA) provide an additional source of interferogenic nucleic acids. In a primary study of NETosis, "release of oxidized mitochondrial DNA is proinflammatory in vitro" and "stimulates type-I interferon (IFN) signaling through a pathway dependent on the DNA sensor, STING."[campbell-2016-oxidized-mtdna-nets-sle] Complementary evidence shows that "Mitochondrial stress releases mitochondrial DNA (mtDNA) into the cytosol and triggers the type-I interferon (IFN) response" and that mtDNA fragments are released "via pores formed by the voltage-dependent anion channel (VDAC) oligomers" in the mitochondrial outer membrane.[liu-2019-vdac-mtdna-lupus]

Defective extracellular DNA degradation can further fuel autoreactivity. In a primary study, "SLE patients with nephritis manifested reduced DNASE1L3 activity in circulation, which was associated with neutralizing autoantibodies to DNASE1L3," directly linking nuclease impairment to lupus nephritis and immune activation.[hartl-2021-dnase1l3-autoantibodies]

## Key Molecular Players and Ontology Annotations
Genetic susceptibility spans immune recognition, signaling, and clearance pathways. A genomic-era review reports "more than 30 robust genetic associations with SLE including genetic variants of HLA and Fc gamma receptor genes, IRF5, STAT4, PTPN22, TNFAIP3, BLK, BANK1, TNFSF4 and ITGAM."[deng-2011-genetic-susceptibility-sle] These translate into key gene annotations such as IRF5 (HGNC:6120), STAT4 (HGNC:11365), PTPN22 (HGNC:9652), TNFAIP3 (HGNC:11896), BLK (HGNC:1057), BANK1 (HGNC:18233), TNFSF4 (HGNC:11934), ITGAM (HGNC:6149), and Fc gamma receptor genes FCGR2A (HGNC:3616) and FCGR2B (HGNC:3618), all implicated in immune signaling and tolerance in SLE.[deng-2011-genetic-susceptibility-sle]

Complement-associated genes are also central, reflecting the strong disease association of classical pathway deficiency: C1QA (HGNC:1241), C1QB (HGNC:1242), C1QC (HGNC:1245), C2 (HGNC:1248), and C4A/C4B (HGNC:1323/1324) underpin immune complex clearance and tolerance.[macedo-2016-complement-classical] Nuclease-mediated clearance of extracellular DNA involves DNASE1L3 (HGNC:2959), which is functionally impaired in a substantial subset of patients with nephritis.[hartl-2021-dnase1l3-autoantibodies] Innate nucleic-acid sensing by endosomal receptors contributes to the interferon program; pDCs recognize nucleic acids through TLR7 (HGNC:15631) and TLR9 (HGNC:15633), which links nucleic acid exposure to IFN production in SLE.[kim-2015-pdc-ifn-axis-sle]

BAFF signaling provides a bridge between T cell activation and autoreactive B cell expansion. In active SLE, CD4+ and CD8+ T cells express BAFF (TNFSF13B; HGNC:11929), and the authors conclude that "BAFF may play a pathogenic role in SLE by stimulating T cell-dependent B cell autoantibodies production."[zhang-2007-baff-tcells-sle] BAFF receptors including TACI (TNFRSF13B; HGNC:18153) and BAFF-R (TNFRSF13C; HGNC:17755) are expressed on B cells, and blockade with TACI-Ig suppresses spontaneous anti-dsDNA production in active SLE with kidney involvement, linking BAFF to pathogenic autoantibody generation.[zhang-2007-baff-tcells-sle] Altered B cell signaling components also emerge in TLR9-defective B cells, including decreased expression of the CD19/CD21 complex (CD19 HGNC:1633; CR2 HGNC:2336), underscoring disrupted B cell regulatory circuits.[mahdavi-2018-tlr9-bcells-sle]

Mitochondrial pathways implicated in lupus include VDAC1 (HGNC:12669), where VDAC oligomerization controls mtDNA release and downstream IFN signaling in lupus-like disease models.[liu-2019-vdac-mtdna-lupus]

Relevant chemical entities include nucleic acids that act as autoantigens and innate immune ligands: deoxyribonucleic acid (DNA; CHEBI:16991) and ribonucleic acid (RNA; CHEBI:33697) as well as the cGAS-STING second messenger 2'-3'-cGAMP (CHEBI:75947) implicated in DNA-sensing pathways.[kim-2015-pdc-ifn-axis-sle][thim-2020-sting-lupus] The antimalarial immunomodulator hydroxychloroquine (CHEBI:5801) is relevant in SLE studies of TLR9 function, where defective responses were reported in B cells from patients without hydroxychloroquine treatment.[mahdavi-2018-tlr9-bcells-sle]

Evidence items with PMIDs anchoring these mechanistic claims include 20138006 (apoptotic clearance and lupus pathogenesis), 20693194 (type I IFN signature), 26110387 (pDC-IFN axis), 26941740 (complement deficiency), 24244889 (NETs), 33783474 (DNASE1L3 autoantibodies), 21060334 (genetic susceptibility), 23929771 and 25014039 (lupus nephritis), 12604793 and 12642603 (interferon and granulopoiesis signatures), 30210502 and 29515028 (TLR7/9 dysregulation), 17500077 (BAFF in T cells), 26779811 (oxidized mtDNA NETs), 31857488 (VDAC-mediated mtDNA release), 31754025 (neutrophil diversity and LDGs), 32524751 (LDNs in SLE), and 33083760 (STING-mediated lupus in vivo).[crispin-2010-pathogenesis-human-sle][obermoser-2010-interferon-alpha-signature][kim-2015-pdc-ifn-axis-sle][macedo-2016-complement-classical][kaplan-2013-nets-sle][hartl-2021-dnase1l3-autoantibodies][deng-2011-genetic-susceptibility-sle][lech-2013-lupus-nephritis][schwartz-2014-lupus-nephritis-pathogenesis][baechler-2003-interferon-signature-severe-sle][bennett-2003-interferon-granulopoiesis-signature][takeda-2018-tlr7-ifn-pdc-sle][mahdavi-2018-tlr9-bcells-sle][zhang-2007-baff-tcells-sle][campbell-2016-oxidized-mtdna-nets-sle][liu-2019-vdac-mtdna-lupus][li-2019-neutrophil-diversity-sle][carriere-2020-low-density-neutrophils-sle][thim-2020-sting-lupus]

## Cellular Components and Dysregulated Processes
Core dysregulated biological processes include type I interferon-mediated signaling (GO:0060337), B cell activation (GO:0042113), T cell activation (GO:0042110), classical pathway complement activation (GO:0006958), apoptotic cell clearance (GO:0043277), neutrophil extracellular trap formation (GO:0140645), toll-like receptor 7 signaling pathway (GO:0034154), toll-like receptor 9 signaling pathway (GO:0034162), and myeloid cell differentiation (GO:0030099), all of which are repeatedly implicated across mechanistic studies and reviews.[obermoser-2010-interferon-alpha-signature][kim-2015-pdc-ifn-axis-sle][macedo-2016-complement-classical][crispin-2010-pathogenesis-human-sle][kaplan-2013-nets-sle][takeda-2018-tlr7-ifn-pdc-sle][mahdavi-2018-tlr9-bcells-sle][bennett-2003-interferon-granulopoiesis-signature]

The principal cellular participants include plasmacytoid dendritic cells (CL:0000784), B cells (CL:0000236), CD4-positive helper T cells (CL:0000492), neutrophils (CL:0000775), monocytes (CL:0000576), macrophages (CL:0000235), and plasma cells (CL:0000786), which together integrate innate sensing with adaptive autoantibody production.[kim-2015-pdc-ifn-axis-sle][crispin-2010-pathogenesis-human-sle][kaplan-2013-nets-sle] Key cellular components and compartments include endosomes (GO:0005768) for TLR7/9 sensing, cytosolic DNA-sensing pathways involving cGAS-STING, nuclear reservoirs of autoantigens, mitochondria (GO:0005739) including the mitochondrial outer membrane (GO:0005741) where VDAC oligomers release mtDNA, and extracellular space (GO:0005615) where immune complexes and NETs accumulate and trigger complement activation.[kim-2015-pdc-ifn-axis-sle][thim-2020-sting-lupus][kaplan-2013-nets-sle][macedo-2016-complement-classical][liu-2019-vdac-mtdna-lupus] The granulopoiesis signature in active SLE also points to altered myeloid development in bone marrow (UBERON:0002371), consistent with the presence of immature neutrophils in peripheral blood.[bennett-2003-interferon-granulopoiesis-signature]

## Disease Progression Model
A plausible mechanistic sequence begins with genetic susceptibility to immune dysregulation and clearance defects.[deng-2011-genetic-susceptibility-sle] Environmental or endogenous triggers increase cell death and the release of nuclear antigens, while defective apoptotic and extracellular DNA clearance allows these ligands to persist.[crispin-2010-pathogenesis-human-sle][hartl-2021-dnase1l3-autoantibodies] Nucleic acid-rich material and immune complexes stimulate pDCs and endosomal TLR7/9, promoting a sustained type I IFN program that is skewed toward enhanced TLR7 and reduced TLR9 responses.[kim-2015-pdc-ifn-axis-sle][obermoser-2010-interferon-alpha-signature][takeda-2018-tlr7-ifn-pdc-sle][mahdavi-2018-tlr9-bcells-sle] Mitochondrial stress and VDAC-dependent mtDNA release further amplify cytosolic DNA sensing and type I IFN signaling.[campbell-2016-oxidized-mtdna-nets-sle][liu-2019-vdac-mtdna-lupus] IFN-driven activation of B and T cells feeds autoantibody production, which is further supported by BAFF signaling and leads to immune complex formation and complement activation, culminating in tissue deposition and inflammation.[obermoser-2010-interferon-alpha-signature][macedo-2016-complement-classical][zhang-2007-baff-tcells-sle] NETosis provides an additional source of extracellular chromatin that sustains this loop, particularly in LDG/LDN subsets.[kaplan-2013-nets-sle][li-2019-neutrophil-diversity-sle][carriere-2020-low-density-neutrophils-sle] In parallel, cGAS-STING signaling can promote dendritic cell activation and lupus-like disease in vivo, indicating a cytosolic DNA-sensing axis that may reinforce the interferon circuit.[thim-2020-sting-lupus]

## Phenotypic Manifestations and Mechanistic Links
The systemic autoimmune phenotype (HP:0002725) manifests across multiple tissues, consistent with widespread exposure to nuclear autoantigens and immune complex-mediated inflammation.[crispin-2010-pathogenesis-human-sle][obermoser-2010-interferon-alpha-signature] Gene-expression data indicate that the IFN signature is associated with severe disease involving kidneys, hematopoetic cells, and the central nervous system (UBERON:0001017), providing a molecular link between interferon biology and organ involvement.[baechler-2003-interferon-signature-severe-sle] Cutaneous involvement is common in skin (UBERON:0002097), and SLE patients can exhibit skin rash, cutaneous photosensitivity (HP:0000992), and malar rash (HP:0025300).[crispin-2010-pathogenesis-human-sle] Musculoskeletal involvement includes arthritis (HP:0001369), reflecting immune activation and inflammatory cascades.[crispin-2010-pathogenesis-human-sle] Hematologic manifestations include hemolytic anemia (HP:0001878), thrombocytopenia (HP:0001873), and decreased total leukocyte count (HP:0001882), consistent with systemic immune activation and granulopoiesis signatures.[crispin-2010-pathogenesis-human-sle][bennett-2003-interferon-granulopoiesis-signature] Neurologic involvement can include seizures (HP:0001250), aligning with central nervous system involvement in severe disease.[crispin-2010-pathogenesis-human-sle][baechler-2003-interferon-signature-severe-sle]

Renal disease is a central end-organ manifestation. Lupus nephritis occurs in kidney (UBERON:0002113), particularly in the renal glomerulus (UBERON:0000074), and is characterized clinically by nephritis (HP:0000123) and proteinuria (HP:0000093).[lech-2013-lupus-nephritis][schwartz-2014-lupus-nephritis-pathogenesis] Mechanistically, "Lupus nephritis is an immune complex GN that develops as a frequent complication of SLE," linking autoantibody-immune complex formation to glomerular injury.[lech-2013-lupus-nephritis] Impaired DNA clearance (e.g., DNASE1L3 neutralization) is enriched in patients with nephritis, providing a mechanistic bridge between nucleic acid-driven autoimmunity and renal damage.[hartl-2021-dnase1l3-autoantibodies]

## Open Questions
A major open question is how distinct sources of self-nucleic acids (apoptotic debris versus NET-derived chromatin versus microparticle-associated DNA) differentially drive interferon programs and organ tropism in human SLE.[crispin-2010-pathogenesis-human-sle][kaplan-2013-nets-sle][hartl-2021-dnase1l3-autoantibodies] Another unresolved issue is the hierarchy of innate sensors in patient subsets, whether endosomal TLR7/9 or cytosolic cGAS-STING pathways dominate in specific clinical phenotypes and how this relates to genetic background or treatment response.[kim-2015-pdc-ifn-axis-sle][thim-2020-sting-lupus] Finally, the precise mechanisms by which classical pathway complement deficiencies and Fc receptor variants skew tolerance and immune complex handling in vivo remain incompletely mapped, particularly in the transition from systemic autoimmunity to organ-specific injury.[macedo-2016-complement-classical][deng-2011-genetic-susceptibility-sle]

## References
- crispin-2010-pathogenesis-human-sle: Crispin JC, Liossis SN, Kis-Toth K, Lieberman LA, Kyttaris VC, Juang YT, Tsokos GC. Pathogenesis of human systemic lupus erythematosus: recent advances. Trends in Molecular Medicine. 2010;16(2):47-57. PMID:20138006. PMCID:PMC2823952. DOI:10.1016/j.molmed.2009.12.005. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC2823952/
- obermoser-2010-interferon-alpha-signature: Obermoser G, Pascual V. The interferon-alpha signature of systemic lupus erythematosus. Lupus. 2010;19(9):1012-1019. PMID:20693194. PMCID:PMC3658279. DOI:10.1177/0961203310371161. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3658279/
- kim-2015-pdc-ifn-axis-sle: Kim JM, Park SH, Kim HY, Kwok SK. A Plasmacytoid Dendritic Cells-Type I Interferon Axis Is Critically Implicated in the Pathogenesis of Systemic Lupus Erythematosus. International Journal of Molecular Sciences. 2015;16(6):14158-14170. PMID:26110387. PMCID:PMC4490545. DOI:10.3390/ijms160614158. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4490545/
- macedo-2016-complement-classical: Macedo AC, Isaac L. Systemic Lupus Erythematosus and Deficiencies of Early Components of the Complement Classical Pathway. Frontiers in Immunology. 2016;7:55. PMID:26941740. PMCID:PMC4764694. DOI:10.3389/fimmu.2016.00055. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4764694/
- kaplan-2013-nets-sle: Yu Y, Su K. Neutrophil Extracellular Traps and Systemic Lupus Erythematosus. Journal of Clinical & Cellular Immunology. 2013;4:139. PMID:24244889. PMCID:PMC3826916. DOI:10.4172/2155-9899.1000139. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3826916/
- lech-2013-lupus-nephritis: Lech M, Anders HJ. The pathogenesis of lupus nephritis. Journal of the American Society of Nephrology. 2013;24(9):1357-1366. PMID:23929771. PMCID:PMC3752952. DOI:10.1681/ASN.2013010026. URL: https://pubmed.ncbi.nlm.nih.gov/23929771/
- schwartz-2014-lupus-nephritis-pathogenesis: Schwartz N, Goilav B, Putterman C. The pathogenesis, diagnosis and treatment of lupus nephritis. Current Opinion in Rheumatology. 2014;26(5):502-509. PMID:25014039. PMCID:PMC4221732. DOI:10.1097/BOR.0000000000000089. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4221732/
- hartl-2021-dnase1l3-autoantibodies: Hartl J, Serpas L, Wang Y, et al. Autoantibody-mediated impairment of DNASE1L3 activity in sporadic systemic lupus erythematosus. Journal of Experimental Medicine. 2021;218(5):e20201138. PMID:33783474. PMCID:PMC8020718. DOI:10.1084/jem.20201138. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8020718/
- deng-2011-genetic-susceptibility-sle: Deng Y, Tsao BP. Genetic susceptibility to systemic lupus erythematosus in the genomic era. Nature Reviews Rheumatology. 2010;6(12):683-692. PMID:21060334. PMCID:PMC3135416. DOI:10.1038/nrrheum.2010.176. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3135416/
- thim-2020-sting-lupus: Thim-uam A, Prabakaran T, Tansakul M, et al. STING Mediates Lupus via the Activation of Conventional Dendritic Cell Maturation and Plasmacytoid Dendritic Cell Differentiation. iScience. 2020;23(9):101530. PMID:33083760. PMCID:PMC7502826. DOI:10.1016/j.isci.2020.101530. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC7502826/
- baechler-2003-interferon-signature-severe-sle: Baechler EC, Batliwalla FM, Karypis G, et al. Interferon-inducible gene expression signature in peripheral blood cells of patients with severe lupus. Proceedings of the National Academy of Sciences of the United States of America. 2003;100(5):2610-5. PMID:12604793. DOI:10.1073/pnas.0337679100. URL: https://pubmed.ncbi.nlm.nih.gov/12604793/
- bennett-2003-interferon-granulopoiesis-signature: Bennett L, Palucka AK, Arce E, et al. Interferon and granulopoiesis signatures in systemic lupus erythematosus blood. The Journal of Experimental Medicine. 2003;197(6):711-23. PMID:12642603. DOI:10.1084/jem.20021553. URL: https://pubmed.ncbi.nlm.nih.gov/12642603/
- takeda-2018-tlr7-ifn-pdc-sle: Sakata K, Nakayamada S, Miyazaki Y, et al. Up-Regulation of TLR7-Mediated IFN-alpha Production by Plasmacytoid Dendritic Cells in Patients With Systemic Lupus Erythematosus. Frontiers in Immunology. 2018;9:1957. PMID:30210502. PMCID:PMC6121190. DOI:10.3389/fimmu.2018.01957. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6121190/
- zhang-2007-baff-tcells-sle: Morimoto S, Nakano S, Watanabe T, et al. Expression of B-cell activating factor of the tumour necrosis factor family (BAFF) in T cells in active systemic lupus erythematosus: the role of BAFF in T cell-dependent B cell pathogenic autoantibody production. Rheumatology (Oxford). 2007;46(7):1083-6. PMID:17500077. DOI:10.1093/rheumatology/kem097. URL: https://pubmed.ncbi.nlm.nih.gov/17500077/
- mahdavi-2018-tlr9-bcells-sle: Gies V, Schickel JN, Jung S, et al. Impaired TLR9 responses in B cells from patients with systemic lupus erythematosus. JCI Insight. 2018;3(5). PMID:29515028. PMCID:PMC5922279. DOI:10.1172/jci.insight.96795. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5922279/
- campbell-2016-oxidized-mtdna-nets-sle: Lood C, Blanco LP, Purmalek MM, et al. Neutrophil extracellular traps enriched in oxidized mitochondrial DNA are interferogenic and contribute to lupus-like disease. Nature Medicine. 2016;22(2):146-153. PMID:26779811. PMCID:PMC4742415. DOI:10.1038/nm.4027. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4742415/
- liu-2019-vdac-mtdna-lupus: Kim J, Gupta R, Blanco LP, et al. VDAC oligomers form mitochondrial pores that release mtDNA fragments and promote lupus-like disease. Science. 2019;366(6472):1531-1536. PMID:31857488. PMCID:PMC8325171. DOI:10.1126/science.aav4011. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8325171/
- li-2019-neutrophil-diversity-sle: Mistry P, Nakabo S, O'Neil L, et al. Transcriptomic, epigenetic, and functional analyses implicate neutrophil diversity in the pathogenesis of systemic lupus erythematosus. Proceedings of the National Academy of Sciences of the United States of America. 2019;116(50):25222-25228. PMID:31754025. PMCID:PMC6911190. DOI:10.1073/pnas.1908576116. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6911190/
- carriere-2020-low-density-neutrophils-sle: Tay SH, Celhar T, Fairhurst AM. Low-Density Neutrophils in Systemic Lupus Erythematosus. Arthritis & Rheumatology. 2020;72(10):1587-1595. PMID:32524751. PMCID:PMC7590095. DOI:10.1002/art.41395. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC7590095/
- medgen-6146-sle: NCBI MedGen. Systemic lupus erythematosus (C0024141) with MONDO:0007915 mapping. URL: https://www.ncbi.nlm.nih.gov/medgen/6146
