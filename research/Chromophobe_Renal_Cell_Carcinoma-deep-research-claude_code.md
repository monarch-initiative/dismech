---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-15T01:49:41.516445'
end_time: '2026-08-15T01:54:05.539608'
duration_seconds: 264.02
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chromophobe Renal Cell Carcinoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 19
  total_cost_usd: 1.8707431000000003
  session_id: 8b2993a2-19f3-5c15-887c-bcc5c26df7a0
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chromophobe Renal Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Chromophobe Renal Cell Carcinoma** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

I'll research Chromophobe Renal Cell Carcinoma thoroughly using web search and fetch tools, then compile a comprehensive report.

# Chromophobe Renal Cell Carcinoma (ChRCC): Comprehensive Research Report

## 1. Disease Information

### Overview
Chromophobe renal cell carcinoma (ChRCC) is a distinct malignant epithelial neoplasm of the kidney, believed to arise from the intercalated cells of the distal nephron/collecting duct (in contrast to clear cell RCC, which arises from proximal tubule cells) (PMID:25155756). It is the third most common renal cell carcinoma subtype after clear cell RCC (ccRCC) and papillary RCC, accounting for approximately 5–7% (range 5–10%) of all RCC cases. It is characterized histologically by large polygonal cells with prominent cell membranes, finely reticulated ("wispy") pale cytoplasm, perinuclear halos, and raisinoid (wrinkled) nuclei, and molecularly by a distinctive pattern of multiple whole-chromosome losses and a comparatively low point-mutation burden. ChRCC is generally regarded as a tumor of relatively low malignant potential with favorable prognosis compared with clear cell and most papillary RCCs, though a subset — particularly tumors with sarcomatoid dedifferentiation — behaves aggressively.

### Key Identifiers
- **MONDO ID:** MONDO:0017885
- **Orphanet ID:** ORPHA:319303
- **ICD-11:** XH6153 (Renal cell carcinoma, chromophobe type); parent code 2C90 (Malignant neoplasms of kidney, except renal pelvis)
- **ICD-O-3 morphology code:** 8270/3
- **OMIM:** No disease-specific OMIM entry exists for sporadic ChRCC; it falls under the general nonpapillary renal cell carcinoma entry **OMIM #144700**. Birt–Hogg–Dubé syndrome (the principal hereditary predisposition syndrome) is **OMIM #135150** (FLCN gene, OMIM *607273*).
- **MeSH:** Carcinoma, Renal Cell (D002292); no distinct MeSH heading for the chromophobe subtype specifically, indexed under this parent term.

### Synonyms
Chromophobe adenocarcinoma of kidney; chromophobe carcinoma of kidney; chromophobe cell carcinoma of kidney; chromophobe cell renal carcinoma; chromophobe renal cell adenocarcinoma; ChRCC (common abbreviation).

### Data Source Character
Information on ChRCC is derived predominantly from **aggregated disease-level resources**: multi-institutional surgical pathology case series (e.g., 145-case and 53-case cohorts), national cancer registries (SEER), and large consortium genomic studies (The Cancer Genome Atlas [TCGA] KICH cohort, n=66) (PMID:25155756; PMID:18813125). Individual-patient-level EHR data are less commonly published given the tumor's rarity; most clinical outcome data come from retrospective institutional or registry-based cohorts rather than prospective clinical trials specific to this histology, reflecting the broader challenge of studying rare RCC subtypes.

---

## 2. Etiology

### Disease Causal Factors
The great majority (~95%+) of ChRCC cases are **sporadic**, arising from somatic (acquired) genomic events — principally large-scale chromosomal losses and, in a subset, TP53/PTEN pathway mutations and mitochondrial DNA (mtDNA) alterations (PMID:25155756). A minority of cases occur in the context of **hereditary tumor-predisposition syndromes**, most notably Birt–Hogg–Dubé (BHD) syndrome, in which ChRCC (and the closely related hybrid oncocytic/chromophobe tumor, HOCT) is the dominant renal tumor histology.

### Genetic Risk Factors

**Birt–Hogg–Dubé syndrome (FLCN, OMIM *607273*, chr17p11.2).** Autosomal dominant loss-of-function mutations in the folliculin (FLCN) tumor suppressor gene cause BHD syndrome, characterized by fibrofolliculomas, pulmonary cysts/spontaneous pneumothorax, and multiple, often bilateral, renal tumors — most commonly hybrid oncocytic/chromophobe tumors and chromophobe RCC, followed by clear cell and papillary histologies (PMID:36258004). Comparative genomic studies show BHD-associated ChRCC/HOCT is molecularly distinct from sporadic ChRCC, lacking the characteristic sporadic-ChRCC chromosome-loss signature and instead showing FLCN biallelic inactivation with mTORC1 pathway hyperactivation (PMC10200853).

**Cowden syndrome / PTEN hamartoma tumor syndrome (PTEN, OMIM *601728*).** Germline PTEN mutations confer elevated lifetime risk of renal cell carcinoma (in addition to breast, thyroid, and endometrial cancer), with RCC risk estimated in some cohorts to approach 15–34% lifetime; ChRCC is one of the reported histologies. Somatically, PTEN is also the second most frequently mutated gene in **sporadic** ChRCC (~9% of TCGA cases) (PMID:25155756), converging genetic evidence on PTEN/mTOR pathway dysregulation as a recurring driver axis.

**Tuberous sclerosis complex (TSC1/TSC2, OMIM #191100/#613254)** and germline succinate dehydrogenase (SDH) mutations are associated with distinct renal tumor entities (angiomyolipoma/eosinophilic solid-and-cystic RCC for TSC; SDH-deficient RCC for SDHB/SDHC/SDHD) that enter the differential diagnosis of, and occasionally overlap morphologically with, chromophobe/oncocytic tumors, though these are separate WHO entities rather than ChRCC itself.

**Somatic driver landscape (TCGA, n=66 tumors) (PMID:25155756):**
- **TP53** — most frequently mutated gene, ~32% of cases; mutations correlate with decreased expression of p53 transcriptional targets and are enriched in the more aggressive "eosinophilic"/high-grade subset.
- **PTEN** — ~9% of cases (nonsilent mutations).
- **mTOR pathway** — mutations in MTOR, NRAS, TSC1, and TSC2 collectively occur in ~23% of cases, converging on mTORC1 hyperactivation as a major pathway.
- **TERT promoter** structural rearrangements — recurrent structural breakpoints juxtapose the TERT promoter with strong enhancers, correlating with markedly elevated TERT expression and localized hypermutation ("kataegis") — a mechanism of telomerase reactivation distinct from the point mutations/amplifications seen in other cancers.
- **~40%** of tumors have no identified driver mutation in a known oncogene/tumor suppressor, implicating the characteristic chromosomal-loss pattern itself (see Genetic/Molecular section) as a primary oncogenic event.

### Environmental Risk Factors
No environmental exposure has been specifically and robustly linked to ChRCC as distinct from RCC broadly. General RCC risk factors — cigarette smoking, obesity, hypertension, acquired cystic kidney disease in dialysis patients, and occupational exposure to trichloroethylene — apply to renal cancer as a class; ChRCC-specific epidemiologic data isolating these exposures are limited given the tumor's rarity.

### Protective Factors
No specific genetic or environmental protective factors have been established for ChRCC; general RCC-protective associations (e.g., physical activity, moderate alcohol intake) reported in broader RCC epidemiology have not been separately validated for the chromophobe subtype.

### Gene-Environment Interactions
Not well characterized for ChRCC specifically; the tumor's genomic architecture (whole-chromosome loss plus a low point-mutation burden) suggests a less environmentally mutagen-driven pathogenesis than smoking-associated urothelial or some clear-cell RCC cases, consistent with its occurrence at a somewhat younger mean age and with strong intrinsic genomic instability as the dominant driver mechanism.

---

## 3. Phenotypes

Because ChRCC is a solid tumor, its "phenotypes" are principally clinical presenting features, laboratory/imaging findings, and pathologic characteristics rather than a syndromic multi-organ phenotype (except in the context of BHD syndrome, discussed above).

### Clinical Signs and Symptoms
- **Often asymptomatic**, incidentally discovered on imaging performed for unrelated indications — an increasingly common presentation pattern for renal masses generally.
- **Flank pain** — HPO: HP:0030057 (Flank pain)
- **Hematuria** — HPO: HP:0000790 (Hematuria)
- **Palpable abdominal/flank mass** — HPO: HP:0031817 (Abdominal mass) / HP:0031279 (Renal mass, if available) — a palpable renal mass, when present with pain and hematuria, forms the classic (but now uncommon) triad seen more with advanced-stage disease.
- **Weight loss** — HPO: HP:0001824
- **Fatigue** — HPO: HP:0012378

### Phenotype Characteristics
- **Age of onset:** Adult-onset; mean age at diagnosis ~59 years (range 27–82 in the largest surgical series) (PMID:18813125); somewhat younger on average than clear cell RCC.
- **Severity/progression:** Most tumors behave indolently (low-grade, low metastatic potential); a minority show aggressive behavior, particularly with **sarcomatoid or rhabdoid dedifferentiation**, high nuclear grade, or the eosinophilic morphologic variant, which — despite resembling benign oncocytoma — can behave more aggressively than classic ChRCC.
- **Multifocality/bilaterality:** Present in ~8% and ~3% of cases respectively in sporadic disease (PMID:18813125); bilaterality and multifocality are much more common in BHD-associated disease and should prompt genetic evaluation.
- **Tumor size at diagnosis:** Frequently large; mean ~8.0 cm (range 1.0–30.0 cm) in surgical series, often larger than clear cell RCC at diagnosis despite favorable behavior (PMID:18813125).

### Imaging Findings (a major "phenotype" category for renal masses)
- **Homogeneous, well-circumscribed solid renal mass**, often hypovascular relative to clear cell RCC.
- **Central stellate scar with "spoke-wheel"-pattern enhancement** on contrast CT/MRI — reported in a substantial minority of cases (historically ~27% in early case series) and classically associated with (but not specific for, and overlapping with) oncocytoma (PMID:15479284).
- **Segmental enhancement inversion** on multiphase MRI has been proposed as a discriminating feature between ChRCC and oncocytoma, though sensitivity is limited (reported in only a small percentage of cases in some series).

### Frequency Among Affected Individuals
Because ChRCC is itself the "disease" rather than a phenotype-bearing syndrome, formal HPO frequency annotation of individual signs (e.g., "flank pain in X% of ChRCC patients") is less standardized than for Mendelian disease; most series report the majority of cases as **incidentally discovered**, with symptomatic presentation (pain, hematuria, mass) more typical of larger or locally advanced tumors.

### Quality of Life Impact
Localized, surgically resected ChRCC generally carries minimal long-term QoL impact beyond standard post-nephrectomy renal function considerations. Metastatic disease carries QoL burdens similar to other advanced RCCs, including treatment-related toxicity from targeted/immunotherapy agents (fatigue, hand-foot syndrome with TKIs, immune-related adverse events with checkpoint inhibitors such as colitis and interstitial nephritis) (academic.oup.com/oncolo/29/5/392).

---

## 4. Genetic/Molecular Information

### Causal/Driver Genes
No single gene is causally sufficient for sporadic ChRCC in the way, e.g., VHL is for clear cell RCC. Instead, ChRCC is defined by a **characteristic multi-chromosome loss signature** plus a low but recurrent point-mutation burden in **TP53** and **PTEN** (PMID:25155756).

### Chromosomal Abnormalities — the defining molecular signature
A hallmark, near-pathognomonic feature: **combined monosomy/loss of chromosomes 1, 2, 6, 10, 13, 17, and 21**, occurring in 70–93% of cases, first described by comparative genomic hybridization (PMID:7519827) and confirmed by TCGA (loss of most/all of chromosomes 1, 2, 6, 10, 13, and 17 in 86% of cases) (PMID:25155756). Karyotypically, tumors frequently show a markedly hypodiploid chromosome count (32–39), sometimes with subsequent endoreduplication producing a near-diploid or hyperdiploid appearance. This combination of losses is used diagnostically to distinguish ChRCC from renal oncocytoma and other mimics, and the **classic morphologic variant loses significantly more chromosomes than the eosinophilic variant** (PMID:33021507).

### Pathogenic Variants
- **TP53** (HGNC:11998; chr17p13.1) — ~32% of TCGA cases; missense and truncating mutations; somatic. Associated with worse outcome and enrichment in high-grade/eosinophilic tumors.
- **PTEN** (HGNC:9588; chr10q23.31) — ~9% of cases; somatic loss-of-function; converges with germline PTEN (Cowden syndrome) and FLCN (BHD) pathways on **mTORC1 hyperactivation** as a recurring pathogenic mechanism.
- **MTOR, NRAS, TSC1, TSC2** — collectively mutated in ~23% of cases (PMID:25155756), reinforcing mTOR pathway centrality; a Modern Pathology molecular study found mTOR pathway alterations enriched in patients with poor outcome (S0893395222004264).
- **TERT promoter structural rearrangements** — recurrent enhancer-hijacking breakpoints near the TERT promoter, correlating with elevated TERT expression and a localized hypermutation ("kataegis") signature — a distinctive telomerase-reactivation mechanism (PMID:25155756).
- **FLCN** (HGNC:27310; chr17p11.2) — germline biallelic loss in BHD-associated tumors (not typically somatically mutated in sporadic ChRCC).
- **Mitochondrial DNA (mtDNA) mutations** — somatic mtDNA mutations, particularly in genes encoding NADH dehydrogenase (Complex I) subunits, have been reported in ChRCC since early sequencing studies (PMID:12353267). A specific **C3572ins insertion in MT-ND1** has been reported in the eosinophilic variant, potentially disrupting Complex I structure/function; ND1 mutations are associated with worse 5-year recurrence-free survival in localized RCC generally (PMID:5187849/PMC5187849). TCGA analysis found ChRCC shows the **highest expression of 13 mtDNA-encoded genes** among RCC subtypes and increased mitochondrial genome content, with near-universal upregulation of Krebs cycle and electron transport chain (ETC) genes relative to normal kidney (PMID:25155756).

### Variant Classification / Allele Frequency
As a somatic cancer-driver context, variants are typically classified via COSMIC/cancer-specific frameworks (pathogenic somatic driver vs. passenger) rather than ACMG/AMP germline classification, except for the germline FLCN, PTEN, TSC1/2, and SDHx variants relevant to hereditary predisposition, which follow standard ClinVar/ACMG classification.

### Somatic vs. Germline Origin
The overwhelming majority of ChRCC-associated variants (TP53, PTEN, MTOR pathway, TERT rearrangements, mtDNA mutations, chromosomal losses) are **somatic**. Germline variants (FLCN in BHD, PTEN in Cowden syndrome) account for the hereditary minority and are associated with characteristic multifocal/bilateral, earlier-onset, hybrid-histology disease.

### Functional Consequences
- TP53 loss-of-function → impaired p53-dependent transcriptional responses (apoptosis, senescence, DNA damage response).
- PTEN loss / MTOR-TSC1/TSC2-NRAS alterations → constitutive **mTORC1 pathway activation**, driving anabolic growth signaling — the mechanistic rationale for mTOR-inhibitor (everolimus) sensitivity in metastatic disease.
- TERT promoter rearrangement → gain-of-function-like transcriptional upregulation of telomerase, promoting replicative immortality.
- Complex I mtDNA mutations → altered oxidative phosphorylation efficiency and mitochondrial oxidative stress, proposed as a partially independent (from mTOR) oncogenic axis specific to this tumor's distal-nephron, mitochondria-rich cell of origin (S1040842825003737; PMID:25155756).

### Modifier Genes
CDKN1A (p21) loss of mRNA/protein expression has been identified as an independent predictor of poor outcome in ChRCC (PMC7072616), suggesting a modifying role for cell-cycle checkpoint regulators beyond the core driver genes.

### Epigenetic Information
TCGA multi-platform analysis included DNA methylation profiling of ChRCC as part of its integrated molecular characterization; ChRCC shows a distinctive expression/methylation profile relative to other RCC subtypes consistent with its distal-nephron/intercalated-cell origin, though disease-specific therapeutic epigenetic targets remain an active research area (S1040842825003737, "emerging vulnerabilities").

**Suggested ontology terms:** HGNC:11998 (TP53), HGNC:9588 (PTEN), HGNC:27310 (FLCN), HGNC:3942 (TSC1), HGNC:12363 (TSC2), HGNC:3942/HGNC:12395 (MTOR), HGNC:1791 (CDKN1A); GO:0031929 (TOR signaling), GO:0006457 (protein folding — not central here), GO:0006120 (mitochondrial electron transport, NADH to ubiquinone).

---

## 5. Environmental Information

### Environmental Factors
No disease-specific environmental toxin has been robustly and specifically associated with ChRCC (as distinct from RCC as a whole). General renal carcinogen exposures (trichloroethylene, cadmium, certain herbicides) are studied predominantly in relation to clear cell RCC.

### Lifestyle Factors
Smoking and obesity are established general RCC risk factors; ChRCC-specific attributable-risk data are sparse given the tumor's rarity and the difficulty of subtype-stratified epidemiologic studies.

### Infectious Agents
Not applicable — ChRCC has no established infectious etiology.

---

## 6. Mechanism / Pathophysiology

### Causal Chain Overview
ChRCC pathogenesis centers on a convergence of (1) large-scale genomic instability producing the characteristic multi-chromosome loss pattern, (2) recurrent point mutations/pathway alterations converging on **mTORC1 hyperactivation** (via PTEN, MTOR, TSC1/2, NRAS, or germline FLCN loss), and (3) **mitochondrial dysfunction** with altered oxidative phosphorylation, reflecting the tumor's origin from mitochondria-rich distal nephron intercalated cells.

**Upstream events:**
- Whole-chromosome losses (1, 2, 6, 10, 13, 17, 21) — an early, near-universal genomic event of unclear precise mechanism, possibly reflecting a distinct chromosomal instability process in the cell of origin.
- TERT promoter structural rearrangement — enables replicative immortality.

**Midstream/convergent pathway alterations:**
- PTEN loss / TSC1-TSC2-MTOR-NRAS mutations / germline FLCN loss → loss of negative regulation of mTORC1 → increased protein synthesis, cell growth, and proliferation (GO:0031929, TOR signaling; GO:0038202, TORC1 signaling).
- TP53 mutation → impaired DNA damage response/apoptosis, permitting accumulation of further genomic instability; enriched in higher-grade, more aggressive tumors.

**Downstream/metabolic consequences:**
- Increased mitochondrial genome content and near-universal transcriptional upregulation of Krebs cycle and electron transport chain (ETC) genes relative to normal kidney — a metabolic reprogramming distinct from the glycolytic (Warburg) shift typical of clear cell RCC, consistent with ChRCC retaining an oxidative-phosphorylation-dependent metabolic phenotype (PMID:25155756).
- Somatic mtDNA mutations (notably in Complex I/ND subunits) may further perturb ETC function and increase oxidative stress, potentially contributing to genomic instability and influencing prognosis (recurrence-free survival) (PMID:5187849).

### Cellular Processes
- Cell cycle dysregulation (via TP53/CDKN1A axis)
- Anabolic growth signaling (mTORC1 pathway) — GO:0016239 not directly, but GO:0045821 (positive regulation of glycolytic process) is more relevant to ccRCC; for ChRCC the relevant term is oxidative-phosphorylation maintenance, GO:0006119 (oxidative phosphorylation).
- Impaired apoptosis/DNA damage response (TP53-dependent) — GO:0006977 (DNA damage response, signal transduction by p53).
- Telomere maintenance (TERT reactivation) — GO:0007004 (telomere maintenance via telomerase).

### Protein Dysfunction
- p53: loss of transcriptional activator function (many mutations are missense, disrupting DNA-binding domain function, consistent with dominant-negative or loss-of-function effects typical of TP53 cancer mutations).
- PTEN: loss of lipid phosphatase activity (PIP3 → PIP2 dephosphorylation), removing the brake on PI3K-AKT-mTOR signaling.
- Mitochondrial Complex I subunits (e.g., ND1): structural/functional impairment from mtDNA insertions/mutations, potentially reducing ETC efficiency.

### Metabolic Changes
Distinctive **oxidative, mitochondria-centered metabolic phenotype** (elevated ETC and Krebs cycle gene expression, increased mtDNA copy number), contrasting with the glycolytic/pseudohypoxic phenotype of VHL-mutant clear cell RCC — an important conceptual distinction, since it implies ChRCC tumor cells may remain relatively dependent on oxidative phosphorylation, a potential therapeutic vulnerability under active investigation (S1040842825003737).

### Tissue Damage / Cell of Origin
Immunohistochemical, ultrastructural, and TCGA transcriptomic evidence supports origin from **intercalated cells of the distal nephron/cortical collecting duct**, distinguishing ChRCC from clear cell RCC (proximal tubule origin) and explaining shared antigenic overlap with the benign oncocytoma (also thought to arise from intercalated cells), which underlies their diagnostic overlap.

### Molecular Profiling Summary (TCGA KICH, n=66) (PMID:25155756)
- **Transcriptomics:** Distal-nephron gene expression signature; upregulation of mitochondrial/OXPHOS genes.
- **Genomics:** Low somatic mutation rate overall; dominant signal is arm/whole-chromosome copy-number loss rather than point mutation burden.
- **mtDNA sequencing:** Recurrent somatic mtDNA mutations, particularly Complex I genes.
- **Structural variation:** TERT promoter rearrangements as a recurrent, disease-defining structural event.

### Single-Cell / Spatial / Multi-omics
Dedicated single-cell and spatial transcriptomic atlases of ChRCC are less mature than for clear cell RCC given rarity, but emerging work (e.g., studies of the hybrid oncocytic/chromophobe tumor in BHD syndrome) uses sequencing to resolve **dual lineage markers capturing the two cellular populations of HOT**, distinguishing oncocytoma-like and chromophobe-like cell populations within hybrid tumors (PMC10871670).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** Kidney (UBERON:0002113), specifically arising in the **renal cortex** from the distal nephron/collecting duct system.
- **Secondary/metastatic sites** (in advanced disease): lung, liver, bone, and regional lymph nodes — a pattern broadly similar to other RCC subtypes, though metastatic ChRCC is less common than in clear cell RCC given its generally indolent behavior.
- **Body systems:** Genitourinary system primarily; renal insufficiency can occur post-nephrectomy or with bilateral disease (as in BHD syndrome).

### Tissue and Cell Level
- **Tissue type:** Renal epithelial (glandular) tissue.
- **Cell of origin / cell type involved:** Intercalated cells of the distal nephron/cortical collecting duct — Cell Ontology candidate term **CL:1000497** (kidney collecting duct intercalated cell) or more specifically CL:0002201 (collecting duct intercalated cell).
- Tumor cells themselves: large, polygonal cells with abundant pale reticulated cytoplasm ("plant-cell" appearance) and prominent cell membranes.

### Subcellular Level
- **Mitochondria** (GO:0005739, mitochondrion) — central to pathophysiology; tumor cells are characteristically packed with mitochondria (contributing to the "chromophobe" — pale, poorly staining — cytoplasmic appearance on light microscopy, related to microvesicle accumulation rather than mitochondrial density per se, though mitochondrial content is elevated at the molecular level per TCGA data).
- Cytoplasmic microvesicles (ultrastructurally distinctive, contributing to the finely reticulated cytoplasmic texture).
- Nucleus — irregular, wrinkled ("raisinoid") nuclear contour, a key diagnostic feature.

### Localization
- Renal mass, typically unifocal in sporadic disease; UBERON:0002113 (kidney), more specifically involving the renal parenchyma/cortex.
- **Lateralization:** Usually unilateral in sporadic disease; bilaterality (~3% sporadic) is a hallmark clue to BHD syndrome when present, and multifocality within one kidney occurs in ~8% (PMID:18813125).

---

## 8. Temporal Development

### Onset
- **Adult-onset** malignancy; mean age at diagnosis ~59 years (range 27–82) (PMID:18813125); some sources note diagnoses clustering in the 40–50 age range as well, reflecting heterogeneity across cohorts, with overall a somewhat younger mean age than clear cell RCC.
- **Onset pattern:** Typically insidious — an asymptomatic mass discovered incidentally on imaging performed for unrelated reasons, reflecting the generally indolent natural history.

### Progression
- **Disease stages:** Staged using the standard **AJCC/TNM system for renal cell carcinoma** (pT1–pT4, N, M), the same staging framework applied across RCC histologic subtypes; ChRCC-specific prognostic nomograms (Leibovich 2018, GRANT models) have also been developed and externally validated using SEER data (PMC10093654).
- **Progression rate:** Generally slow/indolent for classic ChRCC; more rapid and aggressive when sarcomatoid/rhabdoid dedifferentiation, high nuclear grade, or the eosinophilic variant is present.
- **Disease course pattern:** Typically stable/slowly progressive if untreated over years in localized disease; can recur or metastasize years after nephrectomy in a minority of cases, warranting long-term surveillance.
- **Duration:** Curable with surgery in the majority of localized cases; chronic/incurable in the metastatic setting, though median survival even then is measured in years for many patients given the generally favorable underlying biology, in contrast to more rapidly fatal metastatic clear cell RCC.

### Patterns
- **Remission:** Surgical resection (partial or radical nephrectomy) is curative in the vast majority of localized cases; no established spontaneous remission pattern.
- **Critical periods:** Early detection via incidental imaging is the primary driver of favorable outcomes; delayed diagnosis with larger tumor size or dedifferentiated (sarcomatoid) transformation is associated with worse prognosis, making surveillance imaging in known predisposition syndromes (e.g., BHD) clinically important for early intervention.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence/proportion of RCC:** ChRCC accounts for approximately **5–7%** (range cited 5–10%) of all renal cell carcinomas.
- **Incidence:** Estimated annual age-standardized incidence in Western populations of roughly **0.5–1 per 100,000** individuals.

### Inheritance Pattern (for hereditary forms)
- **Birt–Hogg–Dubé syndrome:** Autosomal dominant (FLCN, OMIM #135150); high but incomplete penetrance for cutaneous and pulmonary manifestations, with variable renal tumor risk (lifetime renal tumor risk estimated around 15–30% in various cohorts, though estimates vary).
- **Cowden syndrome (PTEN hamartoma tumor syndrome):** Autosomal dominant (PTEN, OMIM #158350); variable expressivity across the classic Cowden phenotypic spectrum, with RCC (including ChRCC) as one of several associated malignancies alongside breast, thyroid, and endometrial cancer.
- Sporadic ChRCC itself, being a somatically driven malignancy, has no Mendelian inheritance pattern.

### Penetrance / Expressivity
BHD-associated renal tumor risk is age-dependent and incompletely penetrant; expressivity is variable even within families (histology mix of ChRCC, HOCT, oncocytoma, clear cell, and papillary tumors can differ between affected relatives).

### Founder Effects / Consanguinity
Not specifically documented for ChRCC or its associated syndromes; FLCN and PTEN pathogenic variants occur across diverse populations without a strong reported founder-population enrichment specific to renal manifestations.

### Population Demographics
- **Sex ratio:** Reported as roughly **male:female 1.1:1** in the largest histomorphologic series (PMID:18813125), though other summary sources describe a slight female predominance — the literature is not fully concordant, and sex distribution appears closer to balanced than the male predominance seen in clear cell RCC.
- **Geographic distribution:** No strong endemic geographic clustering reported; distribution roughly parallels general RCC incidence patterns globally, modulated by imaging utilization rates (higher incidental detection in high-resource settings with frequent cross-sectional imaging).
- **Age distribution:** Peak diagnosis in the 5th–6th decade of life; can occur across a wide age range (documented from late 20s to 80s) (PMID:18813125).

---

## 10. Diagnostics

### Clinical/Laboratory Tests
- Routine urinalysis (hematuria assessment), basic metabolic panel/renal function testing — nonspecific, used in general renal mass workup rather than ChRCC-specific diagnosis.
- No validated blood or urine biomarker is specific for ChRCC at present.

### Imaging Studies
- **Contrast-enhanced CT** — first-line for renal mass characterization; ChRCC typically appears as a well-circumscribed, homogeneously enhancing (often less avidly than clear cell RCC) solid mass, sometimes with a central stellate scar and "spoke-wheel" enhancement pattern (PMID:15479284).
- **MRI** — used particularly to assess segmental enhancement inversion, a proposed (though imperfectly sensitive) discriminator from oncocytoma (PMC11992432).
- **Multiphase MDCT** enhancement pattern analysis has been studied to differentiate ChRCC from other renal masses (AJR.13.10813).

### Biopsy / Pathology (definitive diagnosis)
- **Renal mass core-needle biopsy or nephrectomy specimen** — gold standard for diagnosis.
- **Histopathology:** Large polygonal cells with pale, finely reticulated ("wispy") cytoplasm, sharp/distinct ("plant-cell-like") cell membranes, perinuclear halos, and irregular ("raisinoid") nuclear contours; classic vs. eosinophilic morphologic variants recognized.
- **Special stains:** Hale's colloidal iron stain classically shows diffuse cytoplasmic staining in ChRCC (though now used less due to variable/focal staining and superseded largely by immunohistochemistry) (pathologyoutlines.com).
- **Immunohistochemistry — the "three 7" panel:** **CK7** (positive, diffusely in >75% of cases), **CD117/KIT** (positive in ~95.5% of cases), and **Claudin-7** — combined use is highly effective for confirming ChRCC and excluding mimics such as oncocytoma (typically CK7-focal/negative) and clear cell RCC (typically CD117-negative) (PMC6815563).
- **Electron microscopy:** Characteristic numerous cytoplasmic microvesicles, historically used to confirm diagnosis in ambiguous cases (PMC4687210).

### Genetic Testing
- Not routinely required for sporadic ChRCC diagnosis (which is a histopathologic/immunohistochemical diagnosis), but **germline FLCN testing** should be considered in patients with bilateral/multifocal tumors, hybrid oncocytic/chromophobe histology, young age at diagnosis, or a personal/family history suggestive of BHD syndrome (fibrofolliculomas, spontaneous pneumothorax). **Germline PTEN testing** is indicated when Cowden syndrome features are present.
- Cytogenetic/FISH or copy-number array testing for the characteristic multi-chromosome loss pattern (chromosomes 1, 2, 6, 10, 13, 17, 21) can support diagnosis in histologically ambiguous cases, distinguishing ChRCC from oncocytoma and other mimics.

### Differential Diagnosis
- **Renal oncocytoma** — the principal benign mimic; distinguished by more diffuse/uniform CK7-negative or focal staining, absence of the characteristic chromosomal loss pattern, and different nuclear features (though "hybrid oncocytic/chromophobe tumor" represents genuine morphologic overlap, especially in BHD syndrome).
- **Eosinophilic solid and cystic RCC (ESC-RCC)** — a distinct WHO 2022-recognized entity, sometimes TSC1/TSC2-mutated, in the differential for oncocytic renal tumors.
- **Low-grade oncocytic tumor (LOT)** — an emerging provisional entity in the WHO 2022 classification, overlapping morphologically with both oncocytoma and eosinophilic ChRCC.
- **Succinate dehydrogenase (SDH)-deficient RCC** and clear cell RCC (eosinophilic variants) — distinguished by SDHB immunohistochemistry loss and CA-IX/CD10 positivity respectively.

### Screening
No population-level screening program exists for sporadic ChRCC given its rarity and generally favorable prognosis. In confirmed BHD syndrome, periodic renal imaging surveillance (e.g., MRI every 1–3 years starting in early adulthood) is recommended given the risk of multiple, recurrent renal tumors.

---

## 11. Outcome/Prognosis

### Survival and Mortality
ChRCC has a notably favorable prognosis relative to other RCC subtypes:
- **5-year overall survival:** Reported around **91%** in aggregate literature, with SEER-based analyses showing 5-year overall survival for localized, post-nephrectomy disease **exceeding 95%**, and cancer-specific survival approaching **98%**.
- **5-year and 10-year cancer-specific survival (broader literature range):** 78–100% and 80–90% respectively, reflecting biological behavior of "low malignant potential" for the majority of tumors.
- **Metastatic disease:** Median overall survival is more guarded, approximately **24 months** in the targeted-therapy era, underscoring the divergent prognosis between localized and advanced disease.

### Prognostic Models
The **Leibovich 2018** and **GRANT (Grade, Age, Nodes, Tumor)** models have been externally validated specifically for non-metastatic ChRCC using a SEER cohort of 5,522 patients, showing moderate discriminative accuracy (concordance ~0.64–0.65 at 10 years) — indicating room for improvement in ChRCC-specific prognostic tools relative to their performance in clear cell RCC (PMC10093654). SEER-based nomograms for overall and cancer-specific survival have also been developed (PMC9438212).

### Morbidity and Function
Post-nephrectomy renal function considerations are relevant, particularly with bilateral/multifocal disease (as in BHD syndrome) where nephron-sparing (partial nephrectomy) approaches are prioritized to preserve function across repeated interventions.

### Disease Course / Complications
- **Sarcomatoid and/or rhabdoid dedifferentiation** is the principal adverse prognostic feature, associated with markedly worse survival and a shift toward more aggressive, systemic-therapy-requiring disease.
- Loss of **CDKN1A (p21)** mRNA/protein expression is an independent predictor of poor outcome (PMC7072616).
- **TP53** mutation and **mTOR pathway alterations** are associated with poorer outcomes in molecular characterization studies (S0893395222004264).
- **MT-ND1** (mitochondrial Complex I) mutation status has been associated with worse recurrence-free survival in localized RCC (PMC5187849).

### Prognostic Factors/Biomarkers
Tumor stage (pT), nuclear grade, presence of sarcomatoid/rhabdoid features, TP53 mutation status, mTOR pathway alteration status, and CDKN1A expression loss are the principal reported prognostic correlates.

---

## 12. Treatment

### Surgical (primary curative modality)
- **Partial nephrectomy (nephron-sparing surgery)** — preferred when technically feasible, especially important in bilateral/multifocal disease (e.g., BHD syndrome) to preserve renal function across potential repeat surgeries.
- **Radical nephrectomy** — for larger or anatomically unfavorable tumors.
- NCIT suggested term: **NCIT:C15329** (Surgical Procedure); more specifically partial/radical nephrectomy procedure codes.

### Pharmacotherapy — Metastatic/Advanced Disease
- **mTOR inhibitors (everolimus)** — mechanistically well-supported given the mTORC1 pathway centrality in ChRCC pathogenesis (via PTEN/TSC1/TSC2/MTOR mutations and FLCN loss in hereditary cases); the ASPEN phase II study reported a chromophobe RCC cohort progression-free survival of **11.4 months** with everolimus, among the better-performing non-clear-cell RCC histologies in that trial.
  - NCIT: **NCIT:C15986** (Pharmacotherapy); therapeutic_agent CHEBI term for everolimus (CHEBI:68478).
- **VEGFR tyrosine kinase inhibitors (sunitinib, cabozantinib, pazopanib)** — used per general non-clear-cell RCC guidelines; case reports document **exceptional responses of metastatic ChRCC to VEGF inhibitors**, with increased VEGF-C expression proposed as a potential predictive biomarker in some cases (PMC6949673).
- **Combination regimens** — current NCCN-guideline-informed approaches for advanced non-clear-cell RCC (including ChRCC) favor doublet therapy: VEGFR-inhibitor + mTOR-inhibitor, VEGFR-inhibitor + immune checkpoint inhibitor, or doublet checkpoint inhibition, extrapolated substantially from broader RCC trials given the paucity of ChRCC-specific randomized data.
- **Lenvatinib plus everolimus** — evaluated in a phase 2 study for advanced non-clear-cell RCC including ChRCC (PMC12684810).
- **Pembrolizumab plus lenvatinib** — under investigation in the first-line advanced/metastatic non-clear-cell RCC setting (KEYNOTE trial program, NCT04704219).

### Immunotherapy
- **Immune checkpoint inhibitors (nivolumab, ipilimumab-nivolumab combination)** — case reports document significant responses in **metastatic ChRCC with sarcomatoid differentiation**, including a notable case of response to nivolumab as seventh-line therapy (PMID:29558933/PMC5907256) and additional cases using combination checkpoint blockade as first-line therapy for sarcomatoid ChRCC (link.springer.com/10.1007/s13691-022-00561-y). Immune-related adverse events reported include interstitial nephritis and colitis.
  - NCIT term candidates: monoclonal antibody / immune checkpoint inhibitor class terms; therapeutic_modality: MONOCLONAL_ANTIBODY.

### Treatment for Sarcomatoid/Rhabdoid Dedifferentiation
- This aggressive subset is treated more like sarcomatoid RCC generally: combination immune checkpoint therapy is a preferred first-line approach; **cabozantinib** as second/third-line therapy after progression on VEGFR-TKI or checkpoint inhibitor combinations has shown objective response rates of **44–47%** in retrospective multicenter series of sarcomatoid-dedifferentiated RCC (academic.oup.com/oncolo/29/5/392).

### Surveillance/Active Monitoring
Active surveillance is a reasonable option for small, incidentally discovered renal masses in appropriately selected (e.g., elderly, comorbid) patients, given ChRCC's generally indolent behavior, though tissue diagnosis (biopsy) is typically pursued first given the differential with oncocytoma and other entities.

### Experimental/Emerging
Given ChRCC's distinctive **mitochondrial/oxidative phosphorylation-dependent metabolism**, targeting mitochondrial vulnerabilities has been proposed as an emerging therapeutic strategy, reviewed as "emerging vulnerabilities" for a new therapeutic landscape in recent literature (S1040842825003737). HIF2α inhibitors (e.g., belzutifan) are primarily developed for VHL-pathway-driven clear cell RCC and are not a standard mechanistic fit for ChRCC, though broader RCC trials sometimes include mixed histology cohorts.

---

## 13. Prevention

### Primary Prevention
No specific primary prevention strategy exists for sporadic ChRCC beyond general cancer risk-factor modification (smoking cessation, weight management) applicable to RCC broadly.

### Secondary Prevention / Screening
- In confirmed hereditary predisposition (BHD syndrome, Cowden syndrome), **periodic renal imaging surveillance** (typically MRI to limit cumulative radiation exposure given repeated lifetime studies) is recommended to enable early detection and nephron-sparing surgical management before tumors grow large or multiply.
- Incidental detection via imaging performed for unrelated indications remains the dominant "screening" mechanism for sporadic disease in practice, given the absence of a formal population screening program.

### Genetic Counseling
Recommended for patients with bilateral/multifocal renal tumors, hybrid oncocytic/chromophobe histology, or a personal/family history suggestive of BHD syndrome (fibrofolliculomas, spontaneous pneumothorax history) or Cowden syndrome, to guide germline testing (FLCN, PTEN) and cascade testing of at-risk relatives.

### Prophylaxis
Not applicable in the pharmacologic sense; nephron-sparing surgical strategy in known predisposition syndromes functions as a form of tertiary/preventive management to preserve long-term renal function against anticipated recurrent tumor development.

---

## 14. Other Species / Natural Disease

### Taxonomy
Primarily a human disease entity (NCBITaxon:9606); renal epithelial tumors morphologically and molecularly analogous to ChRCC are not well established as a naturally occurring veterinary disease entity in the way, e.g., some hereditary cancer syndromes are documented in dogs.

### Comparative/Model Relevance
Comparative biology work has focused on genetically engineered mouse models rather than naturally occurring animal disease (see Model Organisms below). No substantial OMIA (Online Mendelian Inheritance in Animals) entry specific to ChRCC-equivalent naturally occurring disease was identified in this research pass.

### Transmission
Not applicable — ChRCC is a non-communicable, non-zoonotic malignancy.

---

## 15. Model Organisms

### Genetically Engineered Mouse Models
- **Kidney-specific Flcn knockout mouse** — proximal-tubule-targeted disruption of Flcn produces renal cysts and early-onset (~6 months), high-penetrance multi-histology renal neoplasia; the majority of tumors in affected mice under 1 year of age are **chromophobe RCC-like**, with papillary RCC predominating in older knockout mice. Both **mTOR and TGF-β signaling pathways** are upregulated in Flcn-deficient tumors, directly modeling the human BHD-associated tumor biology, and treatment with the mTOR inhibitor **rapamycin** for 10 months suppressed tumor growth in this model — providing preclinical rationale for mTOR-inhibitor use in human BHD-associated and sporadic ChRCC (sciencedirect.com/S0085253815609875).

### Cell Line Models
- **UOK276** — a spontaneously immortalized human cell line derived from a large chromophobe RCC with regions of sarcomatoid differentiation; hyperdiploid with a modal chromosome number of 49 and evidence of copy-neutral loss of heterozygosity. Genomic and metabolic characterization of UOK276 supports its use as a model for studying aggressive, sarcomatoid-differentiated ChRCC and associated treatment resistance (PMC5561006).

### Model Characteristics — Phenotype Recapitulation and Limitations
The Flcn-knockout mouse recapitulates the mTOR/TGF-β pathway activation and histologic spectrum (including a ChRCC-predominant early phenotype transitioning to papillary-predominant with age) seen in human BHD-associated renal tumors, and demonstrates in vivo therapeutic responsiveness to rapamycin — a translationally validated model. A limitation is that this model specifically captures the **FLCN-driven hereditary** pathway rather than the chromosome-loss/TP53/mtDNA-driven **sporadic** ChRCC pathway, which currently lacks an equally well-validated genetically engineered mouse model reproducing the characteristic multi-chromosome-loss genomic signature.

### Applications
These models support mechanistic study of mTOR pathway dependency (rationale for everolimus use), sarcomatoid dedifferentiation biology and drug resistance (UOK276), and preclinical testing of mitochondrial-pathway-targeted therapeutics given ChRCC's distinctive oxidative metabolic phenotype.

### Resources
Mouse Genome Informatics (MGI) for Flcn allele records; Cellosaurus/ATCC for UOK276 and related renal cancer cell line characterization data.

---

## Summary of Suggested Ontology Term Bindings for KB Curation

| Category | Term |
|---|---|
| Disease | MONDO:0017885 (chromophobe renal cell carcinoma) |
| Disease (hereditary) | MONDO for Birt-Hogg-Dube syndrome; OMIM #135150 |
| Causal genes | HGNC:11998 (TP53), HGNC:9588 (PTEN), HGNC:27310 (FLCN), HGNC:3942/12395 (TSC1/TSC2 relevant IDs), MTOR |
| Cell type | CL term for kidney collecting duct intercalated cell (e.g., CL:1000497/CL:0002201) |
| Anatomy | UBERON:0002113 (kidney) |
| Biological process | GO:0031929/GO:0038202 (TOR/TORC1 signaling), GO:0006119 (oxidative phosphorylation), GO:0006977 (DNA damage response via p53), GO:0007004 (telomere maintenance via telomerase) |
| Phenotypes | HP:0000790 (Hematuria), HP:0030057 (Flank pain), HP:0031817 (Abdominal mass) |
| Treatment | NCIT:C15329 (Surgical Procedure), NCIT:C15986 (Pharmacotherapy) with therapeutic_agent CHEBI:68478 (everolimus) |

---

## Sources

- [The Somatic Genomic Landscape of Chromophobe Renal Cell Carcinoma (Davis et al., Cancer Cell 2014) — PMID:25155756](https://pmc.ncbi.nlm.nih.gov/articles/PMC4160352/)
- [Chromophobe renal cell carcinoma: Novel molecular insights and clinicopathologic updates — PubMed](https://pubmed.ncbi.nlm.nih.gov/35198391/)
- [Molecular characterization of chromophobe renal cell carcinoma reveals mTOR pathway alterations in patients with poor outcome — Modern Pathology](https://www.sciencedirect.com/science/article/pii/S0893395222004264)
- [Chromophobe renal cell carcinoma — Cancer Cell (2023 review)](https://www.cell.com/cancer-cell/fulltext/S1535-6108(23)00246-5)
- [Chromophobe renal cell carcinoma: Emerging vulnerabilities as a promise for a new therapeutic landscape](https://www.sciencedirect.com/science/article/abs/pii/S1040842825003737)
- [A tale of two cancers: Complete genetic analysis of chromophobe renal cell carcinoma contrasts with clear cell renal cell carcinoma — PMC](https://ncbi.nlm.nih.gov/pmc/articles/PMC4904899)
- [Mutations in BHD and TP53 genes, but not in HNF1β gene, in a large series of sporadic chromophobe renal cell carcinoma — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2360004/)
- [Heterozygous germline FLCN mutation in Birt–Hogg–Dubé syndrome with bilateral renal hybrid oncocytic/chromophobe tumor — PMID:36258004](https://pubmed.ncbi.nlm.nih.gov/36258004/)
- [Comparative analyses define differences between BHD-associated renal tumour and sporadic chromophobe renal cell carcinoma — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10200853/)
- [Hybrid oncocytic tumors (HOT) in Birt-Hogg-Dubé syndrome patients — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10871670/)
- [Chromophobe renal cell carcinoma: histomorphologic characteristics and evaluation of conventional pathologic prognostic parameters in 145 cases — PMID:18813125](https://pubmed.ncbi.nlm.nih.gov/18813125/)
- [Critical Appraisal of Leibovich 2018 and GRANT Models for Prediction of Cancer-Specific Survival in Non-Metastatic Chromophobe Renal Cell Carcinoma — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10093654/)
- [Nomograms for predicting overall and cancer-specific survival of patients with chromophobe renal cell carcinoma after nephrectomy — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9438212/)
- [Combined Immunohistochemistry for the "Three 7" Markers (CK7, CD117, Claudin-7) — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6815563/)
- [Chromophobe renal cell carcinoma, oncocytic variant: Cytological and ultrastructural observations — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4687210/)
- [Eosinophilic variant of chromophobe renal cell carcinoma — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4264712/)
- [The WHO 2022 Classification of Renal Neoplasms (5th Edition): Salient Updates — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11100973/)
- [Comprehensive Review of Numerical Chromosomal Aberrations in Chromophobe Renal Cell Carcinoma Including Its Variant Morphologies — PMID:33021507](https://pubmed.ncbi.nlm.nih.gov/33021507/)
- [Specific loss of chromosomes 1, 2, 6, 10, 13, 17, and 21 in chromophobe renal cell carcinomas revealed by comparative genomic hybridization — PMID:7519827](https://pubmed.ncbi.nlm.nih.gov/7519827/)
- [Loss of CDKN1A mRNA and Protein Expression Are Independent Predictors of Poor Outcome in Chromophobe Renal Cell Carcinoma Patients — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7072616/)
- [Somatic mitochondrial DNA mutations in human chromophobe renal cell carcinomas — PMID:12353267](https://pubmed.ncbi.nlm.nih.gov/12353267/?dopt=Abstract)
- [Mutations in the Mitochondrial ND1 Gene Are Associated with Postoperative Prognosis of Localized Renal Cell Carcinoma — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5187849/)
- [Spoke-wheel-like enhancement as an important imaging finding of chromophobe cell renal carcinoma — PMID:15479284](https://pubmed.ncbi.nlm.nih.gov/15479284/)
- [Peak early-phase enhancement ratio on contrast-enhanced MRI to differentiate chromophobe renal cell carcinoma from oncocytoma — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11992432/)
- [Germline mutations and variants in the succinate dehydrogenase genes in Cowden and Cowden-like syndromes — PMID:18678321](https://pubmed.ncbi.nlm.nih.gov/18678321/)
- [Significant response to nivolumab for metastatic chromophobe renal cell carcinoma with sarcomatoid differentiation: a case report — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5907256/)
- [Two case reports of immune checkpoint therapy on chromophobe renal cell carcinoma with sarcomatoid differentiation — International Cancer Conference Journal](https://link.springer.com/article/10.1007/s13691-022-00561-y)
- [Treatment Outcomes in Patients With Metastatic Renal Cell Carcinoma With Sarcomatoid and/or Rhabdoid Dedifferentiation After Progression on Immune Checkpoint Therapy — The Oncologist](https://academic.oup.com/oncolo/article/29/5/392/7456167)
- [Exceptional Response of Metastatic Chromophobe Renal Cell Carcinoma to VEGF Inhibitors — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6949673/)
- [Selecting First-Line Treatment for Patients With Chromophobe Renal Cell Carcinoma — ASCO Daily News](https://dailynews.ascopubs.org/do/selecting-first-line-treatment-patients-chromophobe-renal-cell-carcinoma)
- [A Single-arm, Multicenter, Phase 2 Study of Lenvatinib Plus Everolimus in Patients with Advanced Non-Clear Cell Renal Cell Carcinoma — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12684810/)
- [Genomic and metabolic characterization of a chromophobe renal cell carcinoma cell line model (UOK276) — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5561006/)
- [Disruption of tubular Flcn expression as a mouse model for renal tumor induction — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0085253815609875)
- [Chromophobe renal cell carcinoma — Atlas of Genetics and Cytogenetics in Oncology and Haematology](https://atlasgeneticsoncology.org/solid-tumor/209207/chromophobe-renal-cell-carcinoma)
- [Chromophobe renal cell carcinoma — MONDO/NORD disease page](https://rarediseases.org/mondo-disease/chromophobe-renal-cell-carcinoma/)
- [XH6153 Renal cell carcinoma, chromophobe type — ICD-11 MMS](https://www.findacode.com/icd-11/code-455649353.html)
- [Entry #144700 — RENAL CELL CARCINOMA, NONPAPILLARY — OMIM](https://www.omim.org/entry/144700)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.
