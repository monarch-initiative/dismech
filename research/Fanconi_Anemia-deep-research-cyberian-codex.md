---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-02-08T09:58:17.770239'
end_time: '2026-02-08T10:19:52.670309'
duration_seconds: 1294.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fanconi Anemia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: codex
    port: 3284
    skip_permissions: true
    manage_server: true
citation_count: 35
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Fanconi Anemia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Fanconi Anemia**.
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

## Introduction
Fanconi anemia (FA; MONDO:0019391) is a rare inherited genome‑instability disorder. A recent review summarizes its core definition: “Fanconi anemia (FA) is a rare genetic disorder caused by defects in the repair of DNA interstrand crosslinks (ICLs)”—lesions that block replication and transcription and drive genome instability.[fang-2025-fanconi-review][mondo-fanconi-anemia] Clinically, FA manifests with bone‑marrow failure, congenital anomalies, and cancer predisposition, especially myeloid leukemia and squamous cell carcinomas, which links the molecular repair defect to multi‑system pathology.[fang-2025-fanconi-review]

## Core Pathophysiology
ICLs are among the most toxic DNA lesions because they covalently tether both strands and stall replication forks. The FA pathway coordinates their recognition and repair, and its central effector is the FANCI–FANCD2 (ID) complex. The structural primary literature emphasizes that “Central to this pathway is the FANCI‑FANCD2 (ID) complex, which is activated by DNA damage‑induced phosphorylation and monoubiquitination,” and that the ID complex recognizes DNA structures associated with replication forks encountering ICLs.[joo-2011-id2-structure] Reviews of the FA/BRCA pathway further place ICL repair at the intersection of nucleolytic processing, translesion synthesis, and homologous recombination.[kim-2012-genesdev-icls] The FA pathway is activated when replication forks encounter ICLs, leading to ID2 activation and recruitment to chromatin at damage foci; disruption of this activation step underlies the canonical FA cellular phenotype of ICL hypersensitivity and chromosomal breakage.[joo-2011-id2-structure][alpi-2015-ube2t-deficiency]

## Molecular Players and Pathway Architecture
FA genes encode proteins that operate in DNA damage repair pathways, “particularly in the repair of interstrand crosslinks (ICLs).”[fang-2025-fanconi-review] Current syntheses place at least 22 FA proteins in the pathway, organized into core complex, ID2, and downstream effector modules.[fang-2025-fanconi-review] At the core, FANCA (HGNC:3582), FANCL (HGNC:20748), and the E2 enzyme UBE2T (HGNC:25009; FANC‑T) cooperate to monoubiquitinate FANCD2 (HGNC:3585) and FANCI (HGNC:25568), an essential activation step for ICL repair.[ncbi-fanca-hgnc3582][ncbi-fancl-hgnc20748][encode-ube2t-hgnc25009][ncbi-fancd2-hgnc3585][ncbi-fanci-hgnc25568][machida-2007-ube2t-chromatin] Mechanistically, the FA core complex and UBE2T “are required for the S phase and DNA damage‑restricted monoubiquitination of FANCD2,” and UBE2T‑deficient patient cells lose FANCD2/FANCI monoubiquitination and become hypersensitive to crosslinking agents, demonstrating causality in FA‑T.[machida-2007-ube2t-chromatin][alpi-2015-ube2t-deficiency]

Downstream of ID2, monoubiquitinated FANCD2 acts as a recruitment hub for nucleases and repair factors. The FAN1 nuclease (HGNC:26672) “interacts with, and is recruited to sites of DNA damage by, the monoubiquitinated form of FANCD2,” and its loss causes ICL sensitivity and genome instability.[mackay-2013-fan1-nuclease][ncbi-fan1-hgnc26672] SLX4/FANCP (HGNC:23845) is a scaffold for structure‑specific nucleases; its UBZ domain “was required for interaction of SLX4 with ubiquitylated FANCD2” and for recruitment to ICL‑induced damage foci, linking ID2 ubiquitination to endonuclease deployment.[yamamoto-2011-slx4-icls][ncbi-slx4-hgnc23845] Structural work further shows that “recruitment of the [FANCD2–FANCI] complex to a stalled replication fork serves as the trigger for the activating monoubiquitination event,” establishing the order of activation and recruitment at ICL‑stalled forks.[rajan-2016-id2-recruitment] These modules ultimately coordinate incision/unhooking, translesion synthesis, and homologous recombination to restore replication, processes that align with the pathway’s role in DNA interstrand crosslink repair.[mackay-2013-fan1-nuclease][yamamoto-2011-slx4-icls]

## Cellular Processes and Components
The FA pathway maps to defined GO biological processes, including DNA interstrand crosslink repair (GO:0036297), DNA repair (GO:0006281), DNA damage response (GO:0006974), homologous recombination (GO:0000724), and translesion synthesis (GO:0019985).[go-icls-repair][go-dna-repair][go-dna-damage-response][go-homologous-recombination][go-translesion-synthesis] The cellular context is largely nuclear, with repair machinery operating on chromatin (GO:0000785) at replication forks (GO:0005657) inside the nucleus (GO:0005634).[go-chromatin][go-replication-fork][go-nucleus] FA proteins assemble at DNA‑damage foci on chromatin after monoubiquitination, emphasizing chromatin‑localized repair factories rather than cytoplasmic signaling.[machida-2007-ube2t-chromatin][joo-2011-id2-structure]

## Disease Progression
A plausible sequence begins with endogenous or exogenous ICLs (including aldehyde‑derived lesions), which stall replication forks and recruit the ID2 complex. In FA, pathogenic variants disrupt core complex assembly or E2/E3 activity, impairing FANCD2/FANCI monoubiquitination and preventing orderly recruitment of FAN1, SLX4, and other nucleases needed for unhooking and repair.[machida-2007-ube2t-chromatin][alpi-2015-ube2t-deficiency][mackay-2013-fan1-nuclease][yamamoto-2011-slx4-icls] In model systems, SLX4 loss produces cell death with extensive chromosomal aberrations, illustrating how incomplete repair converts replication‑associated lesions into chromosome breaks.[yamamoto-2011-slx4-icls] Persistent DNA damage activates p53‑dependent surveillance; in hematopoietic stem cells, “deletion of p53 completely rescues the survival of aldehyde‑stressed and mutated haematopoietic stem cells,” demonstrating that damage‑response pathways drive stem‑cell attrition.[garaycoechea-2018-aldehydes-hsc] The combined result is progressive bone‑marrow failure from stem‑cell depletion plus clonal evolution of surviving cells with genomic instability, yielding leukemia and solid‑tumor risk.[fang-2025-fanconi-review][garaycoechea-2018-aldehydes-hsc]

## Clinical Phenotypes, Cell Types, and Anatomy
The most vulnerable cell population is the hematopoietic stem cell (CL:0000037) within the hematopoietic system (UBERON:0002390), which sustains lifelong blood production in bone marrow (UBERON:0002371) and blood (UBERON:0000178).[cl-hematopoietic-stem-cell][uberon-hematopoietic-system][uberon-bone-marrow][uberon-blood] Clinically, FA is characterized by bone‑marrow hypocellularity (HP:0005528) and aplastic anemia (HP:0001915), reflecting stem‑cell loss and defective regeneration.[hp-bone-marrow-hypocellularity][hp-aplastic-anemia] Developmental phenotypes such as short stature (HP:0004322) are common, consistent with genome‑maintenance defects during embryogenesis.[hp-short-stature] The cancer‑predisposition phenotype includes acute myeloid leukemia (HP:0004808), consistent with ICL‑repair failure, mutational accumulation, and selection.[hp-aml][fang-2025-fanconi-review]

## Chemical and Environmental Modifiers
Endogenous aldehydes such as acetaldehyde (CHEBI:15343) and formaldehyde (CHEBI:16842) are physiologic genotoxins that generate DNA damage; acetaldehyde‑driven DNA damage in stem cells is documented in vivo, and FA pathway defects heighten susceptibility to such insults.[chebi-acetaldehyde][chebi-formaldehyde][garaycoechea-2018-aldehydes-hsc] Clinically and experimentally, FA cells display hypersensitivity to ICL‑inducing agents such as mitomycin C (CHEBI:27504) and cisplatin (CHEBI:27899), which is diagnostically leveraged in chromosome‑breakage testing and mechanistically reflects failure of the FA ICL repair cascade.[chebi-mitomycin-c][chebi-cisplatin][alpi-2015-ube2t-deficiency][yamamoto-2011-slx4-icls]

## Open Questions
Important unresolved questions include how tissue‑specific aldehyde loads and detoxification capacity set the threshold for FA pathway failure in different organs, and how the balance between p53‑mediated attrition and clonal escape determines cancer risk trajectories. Another gap is the precise ordering and kinetics of nuclease recruitment and translesion synthesis at ICL‑stalled forks in human cells, which could identify therapeutic windows to protect hematopoietic stem cells without increasing mutational burden.

## References
fang-2025-fanconi-review — Fang C, et al. “Comprehensive review on Fanconi anemia: insights into DNA interstrand cross-links, repair pathways, and associated tumors.” Orphanet J Rare Dis. 2025 Jul 30;20:389. DOI: 10.1186/s13023-025-03896-w. PMCID: PMC12312369. PMID: 40739565. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12312369/
kim-2012-genesdev-icls — Kim H, D’Andrea AD. “Regulation of DNA cross-link repair by the Fanconi anemia/BRCA pathway.” Genes Dev. 2012 Jul 1;26(13):1393–1408. DOI: 10.1101/gad.195248.112. PMCID: PMC3403008. PMID: 22751496. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3403008/
joo-2011-id2-structure — Joo W, et al. “Structure of the FANCI-FANCD2 Complex: Insights into the Fanconi Anemia DNA Repair Pathway.” Science. 2011;333(6040):312–316. DOI: 10.1126/science.1205805. PMCID: PMC3310437. PMID: 21764741. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3310437/
rajan-2016-id2-recruitment — Rajan A, et al. “The FANCD2–FANCI complex is recruited to DNA interstrand crosslinks before monoubiquitination of FANCD2.” Nat Commun. 2016 Jul 13;7:12124. DOI: 10.1038/ncomms12124. PMCID: PMC4947157. PMID: 27405460. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4947157/
machida-2007-ube2t-chromatin — Machida YJ, et al. “UBE2T, the Fanconi Anemia Core Complex, and FANCD2 Are Recruited Independently to Chromatin: a Basis for the Regulation of FANCD2 Monoubiquitination.” Mol Cell Biol. 2007 Oct 15;27(24):8421–8430. DOI: 10.1128/MCB.00504-07. PMCID: PMC2169426. PMID: 17938197. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC2169426/
alpi-2015-ube2t-deficiency — Alpi AF, et al. “Deficiency of UBE2T, the E2 ubiquitin ligase necessary for FANCD2 and FANCI ubiquitination, causes FA‑T subtype of Fanconi anemia.” Cell Rep. 2015;12(1):35–45. DOI: 10.1016/j.celrep.2015.06.014. PMCID: PMC4497947. PMID: 26119737. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4497947/
mackay-2013-fan1-nuclease — MacKay C, et al. “Identification of KIAA1018/FAN1, a DNA Repair Nuclease Recruited to DNA Damage by Monoubiquitinated FANCD2.” Cell. 2010 Jul 9;142(1):65–76. DOI: 10.1016/j.cell.2010.06.021. PMCID: PMC3710700. PMID: 20603015. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3710700/
yamamoto-2011-slx4-icls — Yamamoto KN, et al. “Involvement of SLX4 in interstrand cross-link repair is regulated by the Fanconi anemia pathway.” Proc Natl Acad Sci U S A. 2011 Apr 4;108(16):6492–6496. DOI: 10.1073/pnas.1018487108. PMCID: PMC3080998. PMID: 21464321. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3080998/
garaycoechea-2018-aldehydes-hsc — Garaycoechea JI, et al. “Alcohol and endogenous aldehydes damage chromosomes and mutate stem cells.” Nature. 2018;553(7687):171–177. DOI: 10.1038/nature25154. PMCID: PMC6047743. PMID: 29323295. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6047743/
mondo-fanconi-anemia — MONDO:0019391 “Fanconi anemia.” BioPortal. URL: https://bioportal.bioontology.org/ontologies/MONDO/?p=classes&conceptid=MONDO:0019391
ncbi-fanca-hgnc3582 — FANCA (HGNC:3582) in NCBI Gene. URL: https://www.ncbi.nlm.nih.gov/gene/2176
ncbi-fancd2-hgnc3585 — FANCD2 (HGNC:3585) in NCBI Gene. URL: https://www.ncbi.nlm.nih.gov/gene/2177
ncbi-fanci-hgnc25568 — FANCI (HGNC:25568) in NCBI Gene. URL: https://www.ncbi.nlm.nih.gov/gene/55215
ncbi-fancl-hgnc20748 — FANCL (HGNC:20748) in NCBI Gene. URL: https://www.ncbi.nlm.nih.gov/gene/55120
encode-ube2t-hgnc25009 — UBE2T (HGNC:25009) in ENCODE gene summary. URL: https://www.encodeproject.org/search/?searchTerm=UBE2T
ncbi-fan1-hgnc26672 — FAN1 (HGNC:26672) in NCBI Gene. URL: https://www.ncbi.nlm.nih.gov/gene/22909
ncbi-slx4-hgnc23845 — SLX4 (HGNC:23845) in NCBI Gene. URL: https://www.ncbi.nlm.nih.gov/gene/80206
go-icls-repair — GO:0036297 “DNA interstrand cross-link repair.” AmiGO 2. URL: http://amigo.geneontology.org/amigo/term/GO:0036297
go-dna-repair — GO:0006281 “DNA repair.” AmiGO 2. URL: http://amigo.geneontology.org/amigo/term/GO:0006281
go-dna-damage-response — GO:0006974 “cellular response to DNA damage stimulus.” AmiGO 2. URL: http://amigo.geneontology.org/amigo/term/GO:0006974
go-homologous-recombination — GO:0000724 “double-strand break repair via homologous recombination.” AmiGO 2. URL: http://amigo.geneontology.org/amigo/term/GO:0000724
go-translesion-synthesis — GO:0019985 “translesion synthesis.” AmiGO 2. URL: http://amigo.geneontology.org/amigo/term/GO:0019985
go-replication-fork — GO:0005657 “replication fork.” AmiGO 2. URL: http://amigo.geneontology.org/amigo/term/GO:0005657
go-nucleus — GO:0005634 “nucleus.” SGD GO term page. URL: https://www.yeastgenome.org/go/GO:0005634
go-chromatin — GO:0000785 “chromatin.” AmiGO 2. URL: http://amigo.geneontology.org/amigo/term/GO:0000785
cl-hematopoietic-stem-cell — CL:0000037 “hematopoietic stem cell.” ZFIN. URL: https://zfin.org/action/ontology/term/CL:0000037
uberon-bone-marrow — UBERON:0002371 “bone marrow.” BioPortal. URL: https://bioportal.bioontology.org/ontologies/UBERON/?p=classes&conceptid=UBERON:0002371
uberon-blood — UBERON:0000178 “blood.” BioPortal. URL: https://bioportal.bioontology.org/ontologies/UBERON/?p=classes&conceptid=UBERON:0000178
uberon-hematopoietic-system — UBERON:0002390 “hematopoietic system.” ZFIN. URL: https://zfin.org/action/ontology/term/UBERON:0002390
hp-bone-marrow-hypocellularity — HP:0005528 “Bone marrow hypocellularity.” Orphanet. URL: https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=HP:0005528
hp-aplastic-anemia — HP:0001915 “Aplastic anemia.” MSigDB. URL: https://www.gsea-msigdb.org/gsea/msigdb/geneset_page.jsp?geneSetName=HP_APLASTIC_ANEMIA
hp-aml — HP:0004808 “Acute myeloid leukemia.” MSigDB. URL: https://www.gsea-msigdb.org/gsea/msigdb/geneset_page.jsp?geneSetName=HP_ACUTE_MYELOID_LEUKEMIA
hp-short-stature — HP:0004322 “Short stature.” Mendelian Genomics Research Program HPO features table. URL: https://mendelian.genome.wustl.edu/cmg/feature_table
chebi-formaldehyde — CHEBI:16842 “formaldehyde.” ChEBI. URL: https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:16842
chebi-cisplatin — CHEBI:27899 “cisplatin.” ChEBI. URL: https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:27899
chebi-mitomycin-c — CHEBI:27504 “mitomycin C.” ChEBI. URL: https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:27504
chebi-acetaldehyde — CHEBI:15343 “acetaldehyde.” SGD chemical page. URL: https://www.yeastgenome.org/chemical/CHEBI:15343
