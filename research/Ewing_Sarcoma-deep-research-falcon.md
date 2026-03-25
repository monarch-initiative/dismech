---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-24T13:36:15.730248'
end_time: '2026-01-24T13:40:49.760866'
duration_seconds: 274.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ewing Sarcoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 13
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Ewing Sarcoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ewing Sarcoma**.
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Ewing Sarcoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ewing Sarcoma**.
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


Disease Pathophysiology Research Report

Target Disease
- Disease Name: Ewing Sarcoma
- MONDO ID: —
- Category: Malignant small round cell tumor of bone/soft tissue

Pathophysiology description
Ewing sarcoma (EwS) is defined by pathognomonic FET–ETS gene fusions, most commonly EWSR1::FLI1 generated by t(11;22)(q24;q12), with recurrent junction types (EWSR1 exon 7 to FLI1 exon 6 [type I] or exon 5 [type II]) (jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24). The fusion encodes a potent aberrant transcription factor that couples the low-complexity transactivation domain of EWSR1 to the ETS DNA-binding domain of FLI1; both halves are necessary for oncogenic activity, yet transformation efficiency depends on permissive cellular context (jimenez2024anepigeneticapproacha pages 21-24). EwS tumors are genomically “quiet” by point mutation burden (approximately 0.15–0.45 mutations/Mb) but display recurrent copy-number changes (e.g., gains of 8, 2, 1q; loss of 16q) and focal 9p loss with CDKN2A deletion; recurrent secondary alterations include STAG2 (~20%) and TP53 (5–20%), with adverse impact especially when co-mutated (jimenez2024anepigeneticapproachb pages 21-24, jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24).

At the chromatin level, EWSR1::FLI1 drives extensive enhancer reprogramming. The fusion binds canonical ETS motifs and uniquely occupies tandem GGAA microsatellite “super-enhancers,” creating de novo regulatory elements and activating lineage-inappropriate targets (e.g., NR0B1/DAX1); as summarized, the protein “binds tandem GGAA microsatellite repeats” to amplify transcriptional output beyond wild-type FLI1 (petrescu2024preclinicalmodelsfor pages 3-5). This enhanceropathy couples to transcriptional stress, R-loop formation, and replication stress, which engages ATR pathways and creates vulnerabilities to DNA damage response (DDR) agents such as PARP inhibitors (petrescu2024preclinicalmodelsfor pages 3-5). EWSR1::FLI1 also directly and indirectly remodels metabolic programs. It binds the ATF4 promoter and elevates ATF4, a master regulator of the serine biosynthesis pathway (SSP), while the scaffold protein menin is additionally required to sustain ATF4 and the broader ATF4-dependent transcriptome; inhibiting either EWSR1::FLI1 or menin reduces ATF4 and SSP enzymes (e.g., PHGDH) (jimenez2021ewsfli1andmenin pages 1-3).

Clinically, EwS presents as undifferentiated small round blue cell tumors, typically with strong membranous CD99 expression; outcomes are good for localized disease with dose-compressed chemotherapy but remain poor for metastatic/recurrent disease. A position summary reports five-year event-free survival (EFS) around 87% for localized disease and approximately 38% three-year EFS for recurrent/metastatic disease, with relapse driven by resistant clones (jimenez2024anepigeneticapproach pages 21-24). Trials targeting IGF1R and mTOR have shown limited yet notable activity in subsets, reflecting frequent IGF axis engagement in EwS biology (jimenez2024anepigeneticapproach pages 21-24).

Key concepts and definitions with current understanding
- Initiating lesion: Balanced translocation producing EWSR1::FLI1 (or other FET–ETS fusions), often exon 7 of EWSR1 fused to exon 6 (type I) or exon 5 (type II) of FLI1 (jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24). URL: https://doi.org/ (as cited within 2024 thesis); publication year 2024 (jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24).
- Chromatin enhanceropathy: EWSR1::FLI1 binds canonical ETS sites and GGAA microsatellites to establish de novo enhancers and high-output transcriptional programs (“binds tandem GGAA microsatellite repeats”) (petrescu2024preclinicalmodelsfor pages 3-5). URL: https://doi.org/10.3389/fonc.2024.1388484; publication date Jul 2024 (petrescu2024preclinicalmodelsfor pages 3-5).
- Genomic landscape: Low SNV burden (0.15–0.45/Mb), recurrent CNAs (chr8, chr2, 1q gains; 16q loss), and TP53/STAG2 alterations with prognostic interaction (jimenez2024anepigeneticapproachb pages 21-24, jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24). Publication year 2024 (jimenez2024anepigeneticapproachb pages 21-24, jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24).
- Metabolic rewiring: EWSR1::FLI1 and menin converge on ATF4 to upregulate serine biosynthesis; ATF4 is directly activated by EWSR1::FLI1 binding to its promoter (jimenez2021ewsfli1andmenin pages 1-3). URL: https://doi.org/10.1158/1541-7786.mcr-20-0679; publication date Mar 2021 (jimenez2021ewsfli1andmenin pages 1-3).
- Diagnostic phenotype: Small round blue cell tumor with strong CD99; fusion is disease-defining (petrescu2024preclinicalmodelsfor pages 3-5, jimenez2024anepigeneticapproacha pages 21-24). URL: https://doi.org/10.3389/fonc.2024.1388484; publication date Jul 2024 (petrescu2024preclinicalmodelsfor pages 3-5).

Recent developments and latest research (2023–2024 priority)
- 2024 epigenetics-focused synthesis: Updated compendium of EwS fusion biology, genomic landscape, and epigenetic targets, reiterating dominant EWSR1::FLI1 fusion types, low point-mutation burden, recurrent CNAs, and the need for epigenetic/DDR-targeted strategies (jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24). Publication year 2024.
- 2024 preclinical models review: Emphasizes EWSR1::FLI1 enhancer rewiring at GGAA microsatellites, R-loop–associated genomic instability, and associated sensitivity to DDR targeting, integrating model systems that recapitulate these features (petrescu2024preclinicalmodelsfor pages 3-5). URL: https://doi.org/10.3389/fonc.2024.1388484; Jul 2024.

Current applications and real-world implementations
- Molecular diagnosis: Detection of EWSR1::FLI1 (or alternate FET–ETS) fusion is the defining diagnostic test; morphology and CD99 support the diagnosis (petrescu2024preclinicalmodelsfor pages 3-5, jimenez2024anepigeneticapproacha pages 21-24). Jul 2024; 2024.
- Systemic therapy: Standard dose-compressed chemotherapy achieves high EFS in localized disease; investigational/adjunct approaches include IGF1R antibodies and mTOR inhibitors, with limited success and need for biomarker-driven selection (jimenez2024anepigeneticapproach pages 21-24). Publication year 2024.
- Emerging therapeutic rationale: DDR targeting (e.g., PARP inhibitors) leverages EWSR1::FLI1-induced transcriptional/replication stress and R-loops (petrescu2024preclinicalmodelsfor pages 3-5). Jul 2024.

Expert opinions and analysis from authoritative sources
- Fusion-centric disease model: Contemporary synthesis underscores that the EWSR1::FLI1 chimeric transcription factor is the primary oncogenic driver, with cellular context determining permissiveness for transformation; ectopic fusion expression alone “often fails to recapitulate transformation,” arguing for a developmental window/cell-of-origin constraint (jimenez2024anepigeneticapproacha pages 21-24). 2024.
- Enhancer rewiring as core pathophysiology: The capacity of EWSR1::FLI1 to create de novo enhancers at GGAA microsatellites is a unifying explanation for widespread transcriptional dysregulation and downstream vulnerabilities (petrescu2024preclinicalmodelsfor pages 3-5). 2024.
- Metabolic dependency via ATF4: Menin and EWSR1::FLI1 co-regulate ATF4, sustaining serine biosynthesis; this axis links oncogenic transcription to metabolic plasticity and may yield therapeutic windows (jimenez2021ewsfli1andmenin pages 1-3). 2021.

Relevant statistics and data from recent studies
- Mutation burden: ~0.15–0.45 mutations/Mb (jimenez2024anepigeneticapproachb pages 21-24, jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24). 2024.
- Fusion junction frequencies: EWSR1 exon 7 to FLI1 exon 6 (~60%, type I) and exon 5 (~25%, type II) (jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24). 2024.
- Secondary alterations: STAG2 ~20%; TP53 5–20% (jimenez2024anepigeneticapproachb pages 21-24, jimenez2024anepigeneticapproacha pages 21-24). 2024.
- Outcomes: Five-year EFS ~87% for localized disease; ~38% three-year EFS for metastatic/recurrent (jimenez2024anepigeneticapproach pages 21-24). 2024.

Structured knowledge for ontology/annotation
- Key molecular players (HGNC): EWSR1 (EWSR1::FLI1 fusion; HGNC:3508), FLI1 (HGNC:3749), TP53 (HGNC:11998), STAG2 (HGNC:11354), CDKN2A (HGNC:1787), ATF4 (HGNC:792), PHGDH (HGNC:8922), MEN1 (menin; HGNC:7010) (jimenez2024anepigeneticapproacha pages 21-24, jimenez2021ewsfli1andmenin pages 1-3, jimenez2024anepigeneticapproach pages 21-24). Where directly supported: EWSR1, FLI1, TP53, STAG2, CDKN2A (jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24); ATF4/PHGDH/MEN1 (jimenez2021ewsfli1andmenin pages 1-3).
- Biological processes (GO examples, aligned to evidence):
  - Regulation of transcription by RNA polymerase II; enhancer activation/de novo enhancer formation at GGAA microsatellites (petrescu2024preclinicalmodelsfor pages 3-5).
  - Response to endoplasmic reticulum stress and amino acid biosynthetic process (serine biosynthesis) via ATF4 (jimenez2021ewsfli1andmenin pages 1-3).
  - DNA replication stress and DNA repair signaling engagement (linked to R-loops/ATR vulnerability) (petrescu2024preclinicalmodelsfor pages 3-5).
- Cellular components: Chromatin, enhancers/super-enhancers (GGAA microsatellite-associated), nucleoplasm; cell membrane (CD99 immunophenotype) (petrescu2024preclinicalmodelsfor pages 3-5).
- Cell types (CL terms): Primitive mesenchymal progenitors/neural crest–related progenitors implicated as permissive cells of origin; tumor cells are undifferentiated small round cells (petrescu2024preclinicalmodelsfor pages 3-5, jimenez2021ewsfli1andmenin pages 1-3). 2024; 2021.
- Anatomical locations (UBERON): Long bones, pelvis, axial skeleton (general clinical domain, consistent with EwS bone/soft tissue presentation; diagnostic phenotype summarized in review) (petrescu2024preclinicalmodelsfor pages 3-5).
- Chemical entities (CHEBI): Not specifically evidenced in the extracted items beyond general references to chemotherapy and targeted agents; IGF1R/mTOR targeted agents noted (jimenez2024anepigeneticapproach pages 21-24).

Detailed sections
1) Core Pathophysiology
- Primary mechanisms: Oncogenic EWSR1::FLI1 fusion establishes aberrant transcriptional networks by binding ETS motifs and GGAA microsatellites, remodeling chromatin into de novo super-enhancers and amplifying target gene expression; this produces lineage-inappropriate programs and replication/transcription stress (petrescu2024preclinicalmodelsfor pages 3-5). The limited co-mutation landscape underscores the centrality of the fusion (jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24).
- Dysregulated pathways: EWSR1::FLI1-driven enhancer programs converge on growth and survival signaling; clinically and translationally, the IGF1R/PI3K–AKT–mTOR axis has been repeatedly implicated and targeted (jimenez2024anepigeneticapproach pages 21-24). EWSR1::FLI1 and menin activate ATF4 and the serine biosynthesis pathway, linking oncogenic transcription to metabolic support (jimenez2021ewsfli1andmenin pages 1-3).
- Affected processes: Transcriptional regulation, enhancer biogenesis, RNA processing/replication coupling (R-loops), metabolic reprogramming (serine biosynthesis), and DDR pathway engagement (petrescu2024preclinicalmodelsfor pages 3-5, jimenez2021ewsfli1andmenin pages 1-3).

2) Key Molecular Players
- Genes/proteins: EWSR1::FLI1 fusion (defining driver); TP53, STAG2, CDKN2A as recurrent alterations (jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24). ATF4 and PHGDH are upregulated downstream of fusion/menin (jimenez2021ewsfli1andmenin pages 1-3).
- Chemical entities/drugs: Historical and ongoing targeting of IGF1R and mTOR in the clinic (jimenez2024anepigeneticapproach pages 21-24).
- Cell types: Undifferentiated small round tumor cells; proposed permissive progenitors include mesenchymal and neural crest–related stem/progenitor states (petrescu2024preclinicalmodelsfor pages 3-5, jimenez2021ewsfli1andmenin pages 1-3).
- Anatomical locations: Bone and soft tissues; commonly long bones and pelvis (review scope) (petrescu2024preclinicalmodelsfor pages 3-5).

3) Biological Processes (for GO annotation)
- Positive regulation of transcription by RNA polymerase II and enhancer assembly at GGAA microsatellites (petrescu2024preclinicalmodelsfor pages 3-5).
- Cellular response to stress and amino acid biosynthetic process (serine biosynthesis) via ATF4 (jimenez2021ewsfli1andmenin pages 1-3).
- DNA damage response to replication stress/R-loop accumulation (petrescu2024preclinicalmodelsfor pages 3-5).

4) Cellular Components
- Chromatin (enhancers/super-enhancers), nucleoplasm; plasma membrane marker CD99 (diagnostic) (petrescu2024preclinicalmodelsfor pages 3-5).

5) Disease Progression
- Sequence: Initiation by EWSR1::FLI1 fusion in a developmentally defined, permissive progenitor; establishment of enhancer-driven transcriptional programs; induction of replication/transcription stress and DDR engagement; acquisition of cooperating CNAs or secondary hits (e.g., STAG2, TP53) that may influence progression and therapy response; clinical presentation with rapidly growing bone/soft tissue masses; therapeutic response with high cure rates in localized disease but frequent resistance and relapse in metastatic/recurrent settings (jimenez2024anepigeneticapproacha pages 21-24, petrescu2024preclinicalmodelsfor pages 3-5, jimenez2024anepigeneticapproach pages 21-24).

6) Phenotypic Manifestations
- Clinical: Painful bone/soft tissue mass; histology of undifferentiated small round blue cells with strong CD99; aggressive course when metastatic (petrescu2024preclinicalmodelsfor pages 3-5, jimenez2024anepigeneticapproach pages 21-24).
- Mechanistic links: Fusion-driven enhanceropathy underlies proliferation/immaturity; DDR stress explains sensitivity to DNA-damaging regimens and rationale for PARP targeting; ATF4/serine pathway supports biosynthetic needs of rapidly proliferating cells (petrescu2024preclinicalmodelsfor pages 3-5, jimenez2021ewsfli1andmenin pages 1-3).

Evidence items with PMIDs/DOIs/URLs and dates
- Jiménez MS. An epigenetic approach for Ewing sarcoma patients. 2024. Details: fusion types (type I/II), low mutation burden, recurrent CNAs, STAG2/TP53, clinical outcomes, IGF1R/mTOR targeting (jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24). Publication year 2024.
- Petrescu DI et al. Preclinical models for bone sarcomas. Front Oncol. Jul 2024; emphasizes EWSR1::FLI1 enhancer rewiring at GGAA microsatellites, R-loop/DDR vulnerabilities, CD99 phenotype. DOI: 10.3389/fonc.2024.1388484; URL: https://doi.org/10.3389/fonc.2024.1388484 (petrescu2024preclinicalmodelsfor pages 3-5).
- Jiménez JA et al. EWS-FLI1 and menin converge to regulate ATF4 activity. Mol Cancer Res. Mar 2021; shows EWSR1::FLI1 binding at ATF4 promoter, menin dependence, serine biosynthesis upregulation. DOI: 10.1158/1541-7786.mcr-20-0679; URL: https://doi.org/10.1158/1541-7786.mcr-20-0679 (jimenez2021ewsfli1andmenin pages 1-3).

Direct quotes supporting key statements
- “binds tandem GGAA microsatellite repeats” (on EWSR1::FLI1 enhancer binding) (petrescu2024preclinicalmodelsfor pages 3-5).
- “ectopic expression alone often fails to recapitulate transformation,” emphasizing context dependency (jimenez2024anepigeneticapproacha pages 21-24).

Notes and limitations
- Additional emerging mechanisms (e.g., detailed roles of Polycomb/LSD1, ferroptosis control, immune axes such as MIF–CD74, CD99 immunobiology, and liquid biopsy ctDNA measures) are active research areas but were not captured in the extracted evidence set used here; they should be integrated when primary 2023–2024 sources are available for citation.

Gene/protein annotations with ontology terms (examples; evidence-linked)
- EWSR1 (HGNC:3508) and FLI1 (HGNC:3749): fusion oncoprotein EWSR1::FLI1; function: transcription factor activity; process: positive regulation of transcription, enhancer activation at GGAA microsatellites (petrescu2024preclinicalmodelsfor pages 3-5, jimenez2024anepigeneticapproacha pages 21-24).
- ATF4 (HGNC:792): transcription factor; processes: cellular response to stress; regulation of serine biosynthetic process (jimenez2021ewsfli1andmenin pages 1-3).
- PHGDH (HGNC:8922): serine biosynthesis enzyme; process: L-serine biosynthetic process (downstream of ATF4 in EwS) (jimenez2021ewsfli1andmenin pages 1-3).
- TP53 (HGNC:11998), STAG2 (HGNC:11354), CDKN2A (HGNC:1787): tumor suppressors/cohesin; processes: DNA damage response, cell cycle regulation; alterations recurrent in EwS (jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24).

Phenotype associations (HP terms; evidence-linked narrative)
- HP:0009732 (Bone pain) and HP:0100753 (Bone neoplasm) consistent with EwS presentation; undifferentiated small round cell histology and strong CD99 immunostaining (petrescu2024preclinicalmodelsfor pages 3-5). (Note: phenotype terms aligned by clinical convention; narrative support from cited reviews.)

Cell type involvement (CL terms)
- CL:0000134 (mesenchymal stem cell) and neural crest–related progenitors as permissive/transformed lineages; tumor cells are undifferentiated small round cells (petrescu2024preclinicalmodelsfor pages 3-5, jimenez2021ewsfli1andmenin pages 1-3).

Anatomical locations (UBERON terms)
- UBERON:0001474 (long bone), UBERON:0002348 (pelvis) as common sites for primary EwS (review context) (petrescu2024preclinicalmodelsfor pages 3-5).

Chemical entities (CHEBI)
- Agents targeting IGF1R/mTOR pathways have been trialed clinically in EwS; specific compounds not detailed in extracted text (jimenez2024anepigeneticapproach pages 21-24).

Citations
- Jiménez MS. An epigenetic approach for Ewing sarcoma patients. 2024 (jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24).
- Petrescu DI et al. Preclinical models for the study of pediatric solid tumors: focus on bone sarcomas. Front Oncol. Jul 2024. DOI: 10.3389/fonc.2024.1388484. URL: https://doi.org/10.3389/fonc.2024.1388484 (petrescu2024preclinicalmodelsfor pages 3-5).
- Jiménez JA et al. EWS-FLI1 and Menin Converge to Regulate ATF4 Activity in Ewing Sarcoma. Mol Cancer Res. Mar 2021. DOI: 10.1158/1541-7786.mcr-20-0679. URL: https://doi.org/10.1158/1541-7786.mcr-20-0679 (jimenez2021ewsfli1andmenin pages 1-3).
- Additional overview excerpts on fusion structure/genomic landscape/outcomes from 2024 thesis (jimenez2024anepigeneticapproachb pages 21-24, jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24).

References (context IDs)
(jimenez2024anepigeneticapproacha pages 21-24, jimenez2024anepigeneticapproach pages 21-24, petrescu2024preclinicalmodelsfor pages 3-5, jimenez2021ewsfli1andmenin pages 1-3, jimenez2024anepigeneticapproachb pages 21-24)

References

1. (jimenez2024anepigeneticapproacha pages 21-24): M Sánchez Jiménez. An epigenetic approach for ewing sarcoma patients. Unknown journal, 2024.

2. (jimenez2024anepigeneticapproach pages 21-24): M Sánchez Jiménez. An epigenetic approach for ewing sarcoma patients. Unknown journal, 2024.

3. (jimenez2024anepigeneticapproachb pages 21-24): M Sánchez Jiménez. An epigenetic approach for ewing sarcoma patients. Unknown journal, 2024.

4. (petrescu2024preclinicalmodelsfor pages 3-5): D. I. Petrescu, J. Yustein, Atreyi Dasgupta, Joanna Kitlinska, and Massimo Broggini. Preclinical models for the study of pediatric solid tumors: focus on bone sarcomas. Frontiers in Oncology, Jul 2024. URL: https://doi.org/10.3389/fonc.2024.1388484, doi:10.3389/fonc.2024.1388484. This article has 7 citations and is from a poor quality or predatory journal.

5. (jimenez2021ewsfli1andmenin pages 1-3): Jennifer A. Jiménez, April A. Apfelbaum, Allegra G. Hawkins, Laurie K. Svoboda, Abhijay Kumar, Ramon Ocadiz Ruiz, Alessandra X. Garcia, Elena Haarer, Zeribe C. Nwosu, Joshua Bradin, Trupta Purohit, Dong Chen, Tomasz Cierpicki, Jolanta Grembecka, Costas A. Lyssiotis, and Elizabeth R. Lawlor. Ews-fli1 and menin converge to regulate atf4 activity in ewing sarcoma. Molecular Cancer Research, 19:1182-1195, Mar 2021. URL: https://doi.org/10.1158/1541-7786.mcr-20-0679, doi:10.1158/1541-7786.mcr-20-0679. This article has 13 citations and is from a peer-reviewed journal.