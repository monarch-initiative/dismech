---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-03T17:38:42.415126'
end_time: '2026-09-03T17:44:51.543984'
duration_seconds: 369.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Noonan Syndrome 11 NS11, the MRAS-related form of Noonan syndrome,
    OMIM 618499, MONDO:0032786, caused by germline activating missense variants in
    MRAS encoding the RAS-family GTPase M-Ras. NOT LZTR1-related Noonan syndrome and
    NOT any other numbered Noonan syndrome type.
  mondo_id: ''
  category: Genetic
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
  web_search_requests: 22
  num_turns: 34
  total_cost_usd: 1.8190216000000001
  session_id: 4353db50-7706-594d-b7e9-ddac7d1a6181
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Noonan Syndrome 11 NS11, the MRAS-related form of Noonan syndrome, OMIM 618499, MONDO:0032786, caused by germline activating missense variants in MRAS encoding the RAS-family GTPase M-Ras. NOT LZTR1-related Noonan syndrome and NOT any other numbered Noonan syndrome type.
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Noonan Syndrome 11 NS11, the MRAS-related form of Noonan syndrome, OMIM 618499, MONDO:0032786, caused by germline activating missense variants in MRAS encoding the RAS-family GTPase M-Ras. NOT LZTR1-related Noonan syndrome and NOT any other numbered Noonan syndrome type.** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

I'll research this rare RASopathy using web search and fetch tools, then compile a comprehensive report.

I have sufficient material now to compile a comprehensive, well-cited report. Let me do a couple more targeted searches on remaining gaps (prenatal case details, mouse/zebrafish models, growth hormone/other treatments) before writing the final report.

# Noonan Syndrome 11 (NS11): MRAS-Related Noonan Syndrome — Comprehensive Research Report

**Target entity:** Noonan syndrome 11 (NS11), OMIM #618499, MONDO:0032786, caused by germline heterozygous activating (gain-of-function) missense variants in *MRAS* (HGNC:7227, OMIM *608435, chromosome 3q22.3), encoding the atypical RAS-family GTPase M-Ras (also called R-Ras3). This report excludes LZTR1-Noonan syndrome and all other numbered Noonan syndrome types.

---

## 1. Disease Information

**Overview.** Noonan syndrome 11 (NS11) is an ultra-rare, autosomal dominant RASopathy caused by de novo (in essentially all reported cases) germline gain-of-function missense variants in *MRAS*. It presents with the core Noonan syndrome triad — short stature, characteristic facial dysmorphism, and congenital heart disease — but is distinguished from other Noonan subtypes by an unusually high, near-obligate rate of **hypertrophic cardiomyopathy (HCM)**, which in the published cohort has been essentially universal (reported in 100% of the small number of confirmed cases) ([OMIM #618499](https://omim.org/entry/618499); [Motta et al. 2020, *Hum Mol Genet* 29:1772–1783, PMID:31108500](https://pubmed.ncbi.nlm.nih.gov/31108500/)). MRAS was established as a Noonan-susceptibility gene by Higgins et al. in 2017 via mutational screening of 109 unrelated Noonan-syndrome-with-cardiac-hypertrophy probands, of whom molecularly confirmed MRAS variants were found in a small subset ([Higgins et al. 2017, *JCI Insight* 2(5):e91225, PMCID:PMC5333962](https://insight.jci.org/articles/view/91225)).

**Key identifiers:**
- OMIM phenotype: **#618499** — NOONAN SYNDROME 11; NS11
- OMIM gene: ***608435** — MUSCLE RAS VIRAL ONCOGENE HOMOLOG; MRAS*
- MONDO: **MONDO:0032786**
- HGNC: **HGNC:7227** (MRAS); NCBI Gene ID: 22808
- Parent concept ICD-10/11: Noonan syndrome codes (Q87.1x, RASopathy group); no MRAS-specific ICD code exists
- MeSH: Noonan Syndrome (D009634); no separate MeSH term for NS11
- Orphanet: cross-referenced under the general Noonan syndrome gene list ([Orphanet MRAS](https://www.orpha.net/en/disease/gene/MRAS))
- ClinGen gene-disease validity: **Moderate** (as of the RASopathy Gene Curation Expert Panel assessment), meaning the strongest classification a variant can currently receive is "Likely Pathogenic" rather than "Pathogenic" under strict ClinGen/ACMG rules, reflecting the still-small number of published cases ([ClinGen RASopathy curation](https://search.clinicalgenome.org/kb/genes/HGNC:7227); [PMC12151217](https://pmc.ncbi.nlm.nih.gov/articles/PMC12151217/)) — note individual ClinVar submissions for specific variants (e.g., p.Gly23Val) have nonetheless reached "Pathogenic," 2-star review status ([ClinVar RCV000787303](https://www.ncbi.nlm.nih.gov/clinvar/RCV000787303/)).

**Synonyms/alternative names:** Noonan syndrome type 11; NS11; MRAS-related Noonan syndrome; MRAS-associated RASopathy. Gene aliases: M-Ras, R-Ras3, RRAS3.

**Evidence base composition.** Essentially all available data for NS11 specifically come from **individual, molecularly confirmed patient case reports and small case series** (fewer than ten published probands as of early 2026), supplemented by **cell-based and iPSC-derived functional/mechanistic studies** of the specific variants. There is no disease registry, no large aggregated cohort, and no epidemiological database entry specific to NS11 — all prevalence/frequency figures for MRAS-NS are extrapolated from this very small case literature, not population-level aggregation.

---

## 2. Etiology

**Disease causal factor.** NS11 is caused exclusively by **germline heterozygous, de novo (with rare exception) missense gain-of-function variants in *MRAS***, which constitutively activate M-Ras GTPase signaling. There is no known environmental, infectious, or multifactorial contribution to primary disease causation — this is a monogenic RASopathy.

**Genetic risk factors.**
- **Causal variant hotspots** cluster in two structurally critical regions of M-Ras:
  - **Gly23** (P-loop/phosphate-binding loop, analogous to Gly12/13 of classical RAS): p.Gly23Val (c.68G>T) — the index Higgins et al. 2017 mutation; p.Gly23Arg (c.67G>C) — reported by Motta et al. 2020 in a fatal neonatal case.
  - **Thr68** (switch II region): p.Thr68Ile (c.203C>T) — reported by Motta et al. 2020 and subsequently the **most recurrent** MRAS-NS variant, accounting for the majority (up to ~5 of 8) of published cases including the first reported adult and the first infective-endocarditis case ([PMC12794993](https://pmc.ncbi.nlm.nih.gov/articles/PMC12794993/); [Priolo et al. 2023, PMID:36734411](https://pubmed.ncbi.nlm.nih.gov/36734411/)).
  - **Gln71** (switch II region, structurally equivalent to the classic oncogenic Gln61 hotspot of HRAS/KRAS/NRAS): p.Gln71Arg (c.212A>G) — reported by Suzuki et al. 2019 in a patient with a particularly severe phenotype including HCM ([Suzuki et al. 2019, *Am J Med Genet A* 179:1628–1630, PMID:31173466](https://pubmed.ncbi.nlm.nih.gov/31173466/)).
- All variants reported to date have been **de novo**; no transmission from an affected parent has yet been documented in the literature (consistent with the severity of the cardiac phenotype limiting reproductive fitness in some cases), though autosomal dominant transmission (50% recurrence risk to offspring of an affected individual) is the expected Mendelian pattern for any surviving proband ([GeneReviews: Noonan Syndrome, NBK1124](https://www.ncbi.nlm.nih.gov/books/NBK1124/)).
- No allele-frequency data exist in gnomAD for any pathogenic MRAS-NS variant (all absent from >280,000 alleles), consistent with de novo occurrence and negative selection against germline transmission of a severe cardiac phenotype ([Higgins et al. 2017](https://insight.jci.org/articles/view/91225)).
- **Somatic parallel:** Gln71 of MRAS is the direct structural homolog of Gln61 in classical RAS oncoproteins, a well-known oncogenic hotspot in human cancers — underscoring that the same activating biochemistry (impaired intrinsic and GAP-stimulated GTP hydrolysis) drives both germline RASopathy and somatic oncogenesis at this residue ([Suzuki et al. 2019](https://pubmed.ncbi.nlm.nih.gov/31173466/)).

**Environmental/lifestyle risk factors:** None established. As with other RASopathies, **advanced paternal age** has been proposed as a general risk factor for de novo variants in Noonan syndrome broadly, but this has not been specifically documented across the small MRAS-NS case series.

**Protective factors:** None identified; no protective genetic modifiers or environmental protective factors have been described for MRAS-NS specifically.

**Gene-environment interactions:** Not established for NS11.

---

## 3. Phenotypes

Because MRAS-NS has been reported in fewer than ten molecularly confirmed individuals, phenotype "frequencies" below are drawn from case aggregation rather than population statistics, and should be interpreted with that caveat.

### Cardiovascular (dominant/defining phenotype)

| Phenotype | Frequency in reported MRAS-NS cases | Onset | HPO term |
|---|---|---|---|
| Hypertrophic cardiomyopathy | Reported in essentially 100% of confirmed pediatric-onset cases (vs. ~20–30% in Noonan syndrome overall) | Ranges from prenatal/neonatal (severe, often fatal) to mild adult-onset (first reported by Priolo et al. 2023) | HP:0001639 (Hypertrophic cardiomyopathy) |
| Left ventricular outflow tract obstruction | Documented in multiple cases (e.g., systolic anterior motion of mitral valve) | Variable | HP:0001692 |
| Biventricular hypertrophy | Reported in severe/fatal cases (e.g., Motta et al. patient 2, died at 2 months of cardiac failure) | Neonatal | HP:0001637 (Abnormal myocardium morphology) |

The **Motta et al. 2020** paper explicitly frames these as "the third and fourth known cases" of MRAS-NS, both presenting with severe cardiac hypertrophy; one (p.Gly23Arg) died at two months of age of cardiac failure, underscoring the risk of a severe, early-lethal phenotype at this locus ([PMID:31108500](https://pubmed.ncbi.nlm.nih.gov/31108500/)). In contrast, **Priolo et al. 2023** reported the first adult with a p.Thr68Ile variant and only **mild, late-onset left ventricular hypertrophy**, demonstrating that HCM is not obligatorily early-onset or lethal in this gene, and broadening the recognized phenotypic spectrum ([PMID:36734411](https://pubmed.ncbi.nlm.nih.gov/36734411/)). A 2025/2026 case report described the **first infective endocarditis** complicating MRAS-NS HCM (a 22-year-old woman with p.Thr68Ile presenting with fever and a 19 mm LVOT vegetation, *Streptococcus mutans* bacteremia) ([PMC12794993](https://pmc.ncbi.nlm.nih.gov/articles/PMC12794993/)). Antenatally, a 2026 literature review (Martineau et al.) described the first case with severe early antenatal manifestations: increased nuchal translucency, ductus venosus agenesis, pulmonary lymphangiectasia, and complex hepatic vascular anomalies, with autopsy confirming HCM plus obliterative portal venopathy and lymphangiectasia ([Martineau et al. 2026, *Prenatal Diagnosis*, DOI:10.1002/pd.70134](https://obgyn.onlinelibrary.wiley.com/doi/10.1002/pd.70134)).

### Craniofacial/dysmorphic
- Characteristic Noonan facial gestalt: hypertelorism, downslanting palpebral fissures, low-set/posteriorly rotated ears (HP:0000368), ptosis — reported across cases (e.g., "low set and mildly posteriorly angulated ears" in Higgins et al.'s second patient).
- Suggested HPO terms: HP:0000280 (Coarse facial features, when applicable), HP:0000582 (Upslanted palpebral fissure)/HP:0000494 (downslanted), HP:0000369 (Low-set ears).

### Growth
- Short stature (HP:0004322) documented in reported adult cases (e.g., 150 cm/37 kg in the endocarditis case report).

### Skeletal
- Mild pectus excavatum reported in at least one case (HP:0000767).

### Neurodevelopmental
- Developmental delay/cognitive disability reported across multiple cases, ranging from mild learning difficulties (Priolo adult case; endocarditis case: "childhood learning difficulties") to more pronounced cognitive impairment and hypotonia with delayed independent walking (achieved at 2.5 years) in pediatric cases (Higgins et al. 2017).
- Priolo et al. 2023 specifically highlighted **neuropsychiatric features** as an under-recognized adult-onset component of the MRAS-NS phenotype, expanding beyond the classically emphasized cardiac phenotype.
- Suggested HPO terms: HP:0001263 (Global developmental delay), HP:0001249 (Intellectual disability), HP:0001252 (Hypotonia).

### Quality of life impact
No disease-specific EQ-5D/SF-36/PROMIS data exist for MRAS-NS. Qualitatively, the severe pediatric cardiac phenotype carries substantial early mortality risk and functional burden (heart failure, cardiac surgery/myectomy as in the Higgins index case), while the milder adult-onset presentations described by Priolo et al. suggest a meaningfully better prognosis is possible depending on variant and individual course.

---

## 4. Genetic/Molecular Information

**Causal gene:** *MRAS* (HGNC:7227; NCBI Gene 22808; OMIM *608435), chromosome 3q22.3.

**Gene/protein function.** MRAS encodes M-Ras (also called R-Ras3), a member of the **atypical RAS subfamily** of small GTPases (distinct from, but ~55% identical to, the classical RAS proteins HRAS/KRAS/NRAS). Like classical RAS, M-Ras is a GDP/GTP-binding molecular switch, post-translationally modified at a C-terminal CaaX motif by **geranylgeranylation** (in combination with a polybasic region) for membrane targeting ([GeneCards MRAS](https://www.genecards.org/cgi-bin/carddisp.pl?gene=MRAS)). In its active, GTP-bound state, M-Ras assembles — together with the scaffold protein SHOC2 and the catalytic subunit of protein phosphatase 1 (PP1C, isoforms PPP1CA/B/C) — into the **SHOC2–MRAS–PP1C (SMP) holoenzyme complex**, which specifically dephosphorylates an inhibitory serine residue on RAF kinases (Ser259 on CRAF/RAF1; Ser365 on BRAF). This dephosphorylation partially displaces inhibitory 14-3-3 binding and promotes RAF–RAS association and active RAF dimer formation, thereby **positively regulating RAF/MEK/ERK (MAPK) signaling** ([Kwon et al. 2018, *PNAS*, PMID:30348783](https://www.pnas.org/doi/10.1073/pnas.1720352115); [Kwon et al. 2022, *Nature*, PMID:35830882](https://pmc.ncbi.nlm.nih.gov/articles/PMC9452295/); [Bonsor et al. 2022, *Nat Struct Mol Biol*, PMID:36175670](https://www.nature.com/articles/s41594-022-00841-4)). MRAS acts both as a **regulatory subunit** conferring RAF specificity to PP1C and as a **membrane-targeting subunit**, since membrane localization is required for efficient RAF dephosphorylation. The SMP complex forms preferentially when MRAS is GTP-loaded (active), and structural work shows that both RASopathy and cancer mutations in SHOC2, MRAS, and PPP1CB map to protein–protein interfaces within this holophosphatase, enhancing ternary complex formation. M-Ras also modulates AKT/PI3K signaling and, outside this RASopathy context, has documented roles in TNFα-stimulated LFA-1 activation and integrin-mediated leukocyte adhesion, and (via GWAS) a coronary artery disease susceptibility locus ([Shah 2024, *IUBMB Life*](https://iubmb.onlinelibrary.wiley.com/doi/full/10.1002/iub.2805)).

**Pathogenic variants (all reported to date):**

| Variant (protein) | cDNA change | Domain/region | Source publication | PMID |
|---|---|---|---|---|
| p.Gly23Val | c.68G>T | P-loop (G12/13 analog) | Higgins et al. 2017, *JCI Insight* | PMCID:PMC5333962 |
| p.Gly23Arg | c.67G>C | P-loop (G12/13 analog) | Motta et al. 2020, *Hum Mol Genet* | 31108500 |
| p.Thr68Ile | c.203C>T | Switch II region | Motta et al. 2020; recurrent — Priolo et al. 2023; PMC12794993 case | 31108500; 36734411 |
| p.Gln71Arg | c.212A>G | Switch II region (Gln61 analog) | Suzuki et al. 2019, *Am J Med Genet A* | 31173466 |

**Variant classification (ACMG/ClinVar):** p.Gly23Val is classified **Pathogenic** (2-star review status, 5 concordant submitters including OMIM, Baylor Genetics, 3billion, Eurofins-Biomnis, NCGM) for Noonan syndrome 11 ([ClinVar RCV000787303](https://www.ncbi.nlm.nih.gov/clinvar/RCV000787303/)). Gene-level, ClinGen's RASopathy expert panel rates the MRAS–Noonan syndrome relationship as **Moderate**, capping individual variant classifications at "Likely Pathogenic" under strict ClinGen rules pending further case accrual ([PMC12151217](https://pmc.ncbi.nlm.nih.gov/articles/PMC12151217/)).

**Variant type/class:** All reported variants are **missense**, clustering at two structurally critical GTPase regions (P-loop and switch II) — no frameshift, nonsense, splice-site, or structural (CNV) MRAS variants have been reported in NS11.

**Functional consequences — gain of function / constitutive activation.** Multiple orthogonal functional studies converge on a **gain-of-function** mechanism:
- **GTP loading:** p.Gly23Val shows a **~40-fold increase** in GTP loading relative to wild-type MRAS following EGF stimulation, measured by GST-Raf-RBD pulldown (Ras activation assay) ([Higgins et al. 2019, *Circ Genom Precis Med* 12:e002648](https://www.ahajournals.org/doi/10.1161/CIRCGEN.119.002648)).
- **Impaired GTP hydrolysis:** Structural modeling shows p.Gly23 mutations cause steric clashes in the phosphate-binding loop impairing GAP-stimulated GTP hydrolysis; p.Thr68Ile strengthens switch-region interactions to stabilize the active conformation; p.Gln71Arg (structurally homologous to the classical oncogenic Q61R) is predicted to drastically slow intrinsic GTP hydrolysis, by analogy to NRAS Q61R kinetics ([Suzuki et al. 2019](https://pubmed.ncbi.nlm.nih.gov/31173466/); [Motta et al. 2020](https://academic.oup.com/hmg/article/29/11/1772/5492387)).
- **Enhanced downstream signaling:** p.Gly23Val and p.Thr68Ile/p.Gly23Arg show enhanced ERK phosphorylation (context-dependent — weak in HEK293T, robust in Neuro2A cells) and enhanced AKT phosphorylation at basal and stimulated levels ([Motta et al. 2020](https://academic.oup.com/hmg/article/29/11/1772/5492387)).
- **Enhanced complex formation:** Co-immunoprecipitation shows augmented binding of mutant MRAS to SHOC2 and PPP1CB, consistent with enhanced SMP holophosphatase assembly and consequent RAF activation ([Motta et al. 2020](https://academic.oup.com/hmg/article/29/11/1772/5492387); mechanistically consistent with [Kwon et al. 2018, PMID:30348783](https://pubmed.ncbi.nlm.nih.gov/30348783/)).
- **Constitutive membrane targeting:** Mutant MRAS shows persistent GTP-bound state and constitutive plasma membrane localization/prolonged non-raft microdomain localization post-EGF stimulation, compared to transient wild-type localization.

**Germline vs. somatic:** All reported NS11 variants are germline. The structurally homologous Gln61 position in classical RAS genes is a well-known **somatic oncogenic hotspot** in various cancers, and Suzuki et al. explicitly frame Q71R as "a recurrent substitution in RAS homologs in various cancers," highlighting shared biochemistry between germline RASopathy and somatic oncogenesis, though MRAS itself is not a common somatic cancer driver.

**Modifier genes:** None specifically identified for MRAS-NS; general RASopathy modifier-gene research (e.g., variability in *PTPN11*-Noonan syndrome) has not been extended to this ultra-rare subtype.

**Epigenetic information:** No MRAS-NS-specific epigenetic (DNA methylation/histone) studies have been published.

**Chromosomal abnormalities:** None — NS11 is caused by point missense variants, not chromosomal rearrangements.

---

## 5. Environmental Information

No environmental, occupational, toxin, infectious, or lifestyle factors have been implicated in the causation of NS11; it is a purely monogenic disorder. There is no known infectious trigger. (The infective endocarditis reported in one adult case is a **secondary complication** of the pre-existing HCM/LVOT anatomical substrate — caused by *Streptococcus mutans* bacteremia — not an etiological infectious agent for the syndrome itself) ([PMC12794993](https://pmc.ncbi.nlm.nih.gov/articles/PMC12794993/)).

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, from initiating lesion to clinical manifestation)

1. A **de novo germline missense variant** in *MRAS* (at Gly23, Thr68, or Gln71) **leads to** structural disruption of the GTPase P-loop or switch II region of M-Ras (demonstrated: molecular dynamics simulations; structural modeling).
2. This structural change **results in** impaired intrinsic and GAP-stimulated GTP hydrolysis and/or enhanced nucleotide exchange, **leading to** a constitutively/predominantly **GTP-bound, active state** of M-Ras (demonstrated: ~40-fold increased GTP loading for p.Gly23Val in cell-based Ras-activation assays).
3. GTP-bound mutant M-Ras **shows increased/constitutive plasma-membrane targeting and prolonged localization to signaling microdomains** post-growth-factor stimulation (demonstrated in HEK293T/COS-1 cells).
4. Active, membrane-localized mutant M-Ras **drives enhanced assembly of the SHOC2–MRAS–PP1C (SMP) holophosphatase complex**, evidenced by augmented co-immunoprecipitation of mutant MRAS with SHOC2 and PPP1CB (demonstrated in cell-based binding assays).
5. The SMP complex **dephosphorylates the inhibitory serine on RAF kinases** (Ser259-CRAF/Ser365-BRAF), **leading to** partial displacement of inhibitory 14-3-3 binding and promotion of RAF–RAS association and active RAF dimer formation (mechanistically demonstrated by cryo-EM/X-ray structural studies of the SMP complex, largely in non-disease-specific but directly relevant biochemical systems — inferred to apply to the disease variants by structural mapping of RASopathy mutations to SMP interfaces).
6. Activated RAF **drives hyperactivation of the canonical MEK–ERK (MAPK) cascade**, with additional **enhancement of AKT/PI3K signaling** observed for MRAS mutants (demonstrated: increased basal and EGF-stimulated pERK and pAKT in transfected cells; context-dependent magnitude — weaker in HEK293T, robust in Neuro2A neuronal-lineage cells, suggesting cell-type-specific downstream consequences that may partly explain both the cardiac and neurodevelopmental phenotype).
7. In cardiomyocytes specifically, chronic RAF/MEK/ERK (and AKT) pathway hyperactivation **leads to pathological cardiomyocyte hypertrophy** — directly demonstrated in **patient-specific and CRISPR-corrected iPSC-derived cardiomyocytes**, in which cells carrying p.Gly23Val-MRAS were significantly larger than isogenic controls and showed altered hypertrophy-associated gene expression and intracellular signaling ([Higgins et al. 2019, PMID pending / DOI:10.1161/CIRCGEN.119.002648](https://www.ahajournals.org/doi/10.1161/CIRCGEN.119.002648)).
8. Cardiomyocyte hypertrophy at the tissue level **manifests clinically as hypertrophic cardiomyopathy**, in some cases with left ventricular outflow tract obstruction (systolic anterior motion of the mitral valve), progressing in severe neonatal cases to heart failure and death, or in milder/later-onset cases to a stable or slowly progressive adult HCM phenotype (this step — from cellular hypertrophy to organ-level HCM and its clinical severity spectrum — is directly demonstrated at the clinical/imaging level across the case series but the determinants of severity, e.g., variant identity, genetic background, or developmental timing of pathway hyperactivation, remain **inferred rather than mechanistically established**).
9. In parallel, **RAS/MAPK pathway hyperactivation during development is inferred (by analogy with other Noonan-syndrome genes, not MRAS-specific data) to drive** the craniofacial dysmorphism, growth impairment, and neurodevelopmental phenotype characteristic of Noonan syndrome broadly, via effects on cranial neural crest, growth plate, and neuronal signaling — this branch is **extrapolated from the general RASopathy paradigm rather than demonstrated with MRAS-specific developmental data**, since no MRAS-NS animal model publications currently exist.

### Molecular pathways
- **RAS/MAPK (RAF–MEK–ERK) pathway** — the central, disease-defining pathway; MRAS acts non-canonically (not as a classical RAS effector-activator, but via the SMP holophosphatase mechanism that removes an inhibitory RAF phosphorylation) ([KEGG hsa04014 Ras signaling pathway]; [Reactome RAF/MAP kinase cascade]).
- **PI3K–AKT pathway** — secondarily hyperactivated by mutant MRAS.
- Suggested GO terms: **GO:0007265** (Ras protein signal transduction), **GO:0000165** (MAPK cascade), **GO:0004725** (protein tyrosine phosphatase activity — for the PP1C dephosphorylation step, though PP1C is a serine/threonine phosphatase, more precisely **GO:0004722**, protein serine/threonine phosphatase activity), **GO:0007172** (signal complex assembly).

### Cellular processes
- **Pathological cardiomyocyte hypertrophy** (increased cell size, altered sarcomeric/hypertrophy gene expression) — directly demonstrated in iPSC-CM model.
- Altered **cell proliferation/growth signaling** more broadly (inferred from general RAS/MAPK biology).
- Suggested GO term: **GO:0003300** (cardiac muscle hypertrophy) / **GO:0014897** (striated muscle hypertrophy).

### Protein dysfunction
- **Gain of function via impaired intrinsic/GAP-stimulated GTPase activity**, not loss of function or simple overexpression — a qualitative, not merely quantitative, defect (structurally analogous to but biochemically distinct from classical RAS G12/G13/Q61 oncogenic mutations).

### Tissue damage mechanisms
- Not primarily degenerative; the cardiac pathology is a **hypertrophic/hyperplastic** remodeling response to chronic pathway hyperactivation rather than oxidative/ischemic/fibrotic injury, though secondary myocardial fibrosis may occur in longstanding HCM (as in other HCM etiologies; not specifically documented for MRAS-NS in the literature reviewed).

### Molecular profiling / omics
No published transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial-omics datasets specific to MRAS-NS patient tissue were identified in this search. The iPSC-CM study by Higgins et al. 2019 did report **gene expression changes characteristic of cardiac hypertrophy** in mutant vs. corrected isogenic lines, but did not perform genome-wide profiling per the available summary.

### Structural biology
Cryo-EM and X-ray crystallography have resolved the **SHOC2–MRAS–PP1C (SMP) holoenzyme structure**, showing a crescent-shaped SHOC2 scaffold that bridges MRAS and PP1C into a cooperative, GTP-state-dependent assembly ([Kwon et al. 2022, *Nature*, PMID:35830882](https://pmc.ncbi.nlm.nih.gov/articles/PMC9452295/); [Bonsor et al. 2022, *Nat Struct Mol Biol*, PMID:36175670](https://www.nature.com/articles/s41594-022-00841-4); [Young/Hall 2022, PMID:35768504](https://pubmed.ncbi.nlm.nih.gov/35768504/)). These structures show that RASopathy mutations (in SHOC2, MRAS, and PPP1CB alike) map to protein-protein interfaces within the complex, increasing affinity and enhancing constitutive RAF dephosphorylation — providing the direct structural rationale for the NS11 disease mechanism.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Heart (myocardium — ventricular septum and free wall hypertrophy; LVOT). UBERON:0000948 (heart), UBERON:0002012 (ventricle).
- **Secondary:** Craniofacial skeleton (dysmorphic features), growth plate (short stature), central nervous system (developmental delay/cognitive impairment), skeletal system (pectus deformity).
- **Body systems:** Cardiovascular (primary), musculoskeletal, nervous/neurodevelopmental, and (in the severe antenatal case) lymphatic/hepatic vascular systems (pulmonary lymphangiectasia, hepatic vascular anomalies, obliterative portal venopathy).

**Tissue/cell level:**
- Cardiac muscle tissue — **cardiomyocytes** (CL:0000746) are the principal affected cell type, directly demonstrated by iPSC-CM hypertrophy modeling.
- Cranial neural crest-derived tissues (craniofacial dysmorphism) — inferred by analogy to general Noonan syndrome pathogenesis, not MRAS-specific data.

**Subcellular level:**
- **Plasma membrane** (site of M-Ras geranylgeranylation-dependent localization and SMP complex assembly) — GO:0005886 (plasma membrane), GO:0031234 (extrinsic component of cytoplasmic side of plasma membrane).
- Cytoplasmic signaling complexes (SHOC2–MRAS–PP1C holoenzyme).

**Localization:** Cardiac hypertrophy is typically **biventricular or predominantly left ventricular/septal**, sometimes with LVOT obstruction; no consistent laterality pattern reported (not applicable to a diffuse myocardial process).

---

## 8. Temporal Development

**Onset:** Highly variable — this is one of the most striking features of MRAS-NS reported to date.
- **Prenatal/antenatal:** Severe cases detectable in utero (increased nuchal translucency, ductus venosus agenesis, fetal HCM) — reported by Martineau et al. 2026.
- **Neonatal/infantile:** Severe biventricular HCM, sometimes fatal within months (Motta et al. 2020, p.Gly23Arg patient died at 2 months).
- **Childhood:** Cardiac hypertrophy diagnosed in infancy with later surgical myectomy (Higgins et al. 2017 index case, surgery at age 8).
- **Adult-onset:** Mild, late-onset left ventricular hypertrophy first reported by Priolo et al. 2023 in a p.Thr68Ile carrier — demonstrating the phenotypic spectrum extends into adulthood-onset, non-lethal disease.

**Onset pattern:** Insidious/chronic for the cardiac hypertrophy in mild cases; can be acute/rapidly progressive to heart failure in severe neonatal cases.

**Progression:** Ranges from **rapidly progressive and fatal** (neonatal HCM with heart failure) to **stable/mild and slowly progressive** (adult-onset LVH). No formal staging system exists for NS11-specific HCM; standard HCM staging concepts (from general cardiomyopathy literature) would apply clinically but have not been validated in this gene-specific population.

**Disease course pattern:** Chronic, generally non-remitting for the cardiac and dysmorphic features (structural, not relapsing-remitting); neurodevelopmental features are typically stable/lifelong rather than progressive.

**Critical periods:** The prenatal/perinatal period appears to represent a **critical window of vulnerability** for the most severe cardiac and lymphatic/vascular manifestations, based on the most severely affected reported cases (fatal neonatal HCM; antenatal multi-system anomalies). This suggests a potential window for prenatal/early therapeutic intervention (e.g., MEK inhibition), analogous to approaches used in other severe neonatal Noonan-HCM genotypes (RAF1, RIT1, SOS1) — though this has not yet been reported for MRAS specifically.

---

## 9. Inheritance and Population

**Epidemiology:** No disease-registry or population-based prevalence/incidence estimate exists for NS11 specifically; it is an ultra-rare Noonan syndrome subtype. General Noonan syndrome (all genes combined) has an estimated incidence of **1:1,000 to 1:2,500 live births** (with milder undiagnosed presentations potentially as common as 1:100) ([GeneReviews NBK1124](https://www.ncbi.nlm.nih.gov/books/NBK1124/)). MRAS accounts for only a small fraction of molecularly diagnosed Noonan syndrome (well under 1% based on published mutational-screening yield: Higgins et al. found MRAS variants in a small subset of 109 unrelated Noonan-with-cardiac-hypertrophy probands screened). As of the most recent comprehensive literature review (Martineau et al. 2026), fewer than **eight molecularly confirmed cases** have been published worldwide.

**Inheritance pattern:** **Autosomal dominant**, consistent with other Noonan syndrome genes; all reported cases to date are **de novo**.

**Penetrance:** Appears to be **high/complete** for the core Noonan phenotype among reported cases, though ascertainment bias (severe cases more likely to be sequenced and published) cannot be excluded given the very small numbers.

**Expressivity:** **Markedly variable**, spanning fatal neonatal HCM to mild adult-onset LVH — among the most variable expressivity reported for any single Noonan-syndrome gene, and a key point emphasized by Priolo et al. 2023.

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented for MRAS to date, though theoretically possible as for other autosomal dominant de novo conditions; genetic counseling for future pregnancies of unaffected parents of an affected child should still account for a low empiric recurrence risk due to possible parental gonadal mosaicism, per general Noonan syndrome counseling practice.

**Founder effects:** None identified; reported probands are of diverse ancestries (North African Jewish, German, Japanese, and others), and each mutation site (Gly23, Thr68, Gln71) has arisen independently and recurrently, consistent with mutational hotspots rather than a single founder allele.

**Consanguinity:** Not implicated (dominant, de novo mechanism).

**Carrier frequency:** Not applicable (not a recessive/carrier-based condition).

**Population demographics:** No specific ethnic or geographic enrichment identified; case reports span Europe (France/Italy — Motta et al., Priolo et al.), the Middle East/North Africa, Japan (Suzuki et al.), and other regions, consistent with pan-ethnic occurrence typical of de novo dominant conditions.

**Sex ratio:** No clear sex bias apparent from the small case series (both male and female probands reported); too few cases for statistical inference.

**Age distribution:** Bimodal-appearing in the literature — a cluster of severe pediatric/neonatal presentations and a smaller but growing recognition of mild adult presentations, likely reflecting both true biological variability and historical ascertainment bias toward the most severe (most readily diagnosed) cases.

---

## 10. Diagnostics

**Clinical/laboratory tests:** No MRAS-NS-specific biomarker exists. Standard Noonan syndrome/HCM diagnostic workup applies: echocardiography (initial and primary imaging modality for HCM detection — LOINC/RadLex imaging codes apply generically), cardiac MRI (used in at least one reported case for detailed characterization of wall hypertrophy and LVOT obstruction), and standard HCM-associated laboratory studies (BNP/NT-proBNP, troponin) as clinically indicated (not specifically reported in the MRAS-NS literature reviewed).

**Genetic testing:**
- **Recommended approach:** Given the phenotypic overlap across Noonan-syndrome genes, testing is typically performed via a **multi-gene RASopathy/Noonan syndrome panel** (including *PTPN11, SOS1, RAF1, RIT1, KRAS, NRAS, BRAF, MRAS, LZTR1, SHOC2, PPP1CB, CBL*, etc.) or **exome/genome sequencing**, rather than single-gene *MRAS* testing as first-line, given MRAS's rarity as a cause.
- **Whole exome sequencing (WES)** was the discovery method for the index Higgins et al. 2017 case (trio-based WES with genomic triangulation) and has been used in subsequent cases.
- **Single-gene MRAS testing** is appropriate as a targeted confirmatory test once a specific familial variant or a strong phenotype-driven hypothesis (e.g., severe HCM + Noonan features with panel-negative results for more common genes) is present, or for prenatal confirmation when a fetal variant is suspected.
- **Prenatal diagnostic testing** of Noonan syndrome gene panels (including MRAS) in fetuses with abnormal ultrasound findings (increased nuchal translucency, cystic hygroma, polyhydramnios, cardiac anomalies) is an established approach in the field generally ([Nature EJHG 2012285](https://www.nature.com/articles/ejhg2012285)) and was applied in the Martineau et al. 2026 antenatal MRAS case.
- **Chromosomal microarray/karyotype/FISH:** Not diagnostic for NS11 (a point-mutation disorder), but are typically performed as part of standard prenatal/postnatal differential diagnostic workup to exclude chromosomal causes of overlapping phenotypes (e.g., Turner syndrome, which shares some prenatal ultrasound findings) before or alongside gene panel testing.

**Clinical diagnostic criteria:** No MRAS-specific clinical criteria exist. Diagnosis follows the general Noonan syndrome approach: clinical suspicion based on characteristic facial features, cardiac defects (with unusually high suspicion warranted when HCM specifically, rather than pulmonic stenosis, is the presenting cardiac lesion), and short stature, confirmed by identification of a heterozygous pathogenic/likely pathogenic variant in a Noonan-syndrome-associated gene ([GeneReviews NBK1124](https://www.ncbi.nlm.nih.gov/books/NBK1124/)).

**Differential diagnosis:** Other Noonan syndrome genotypes (particularly *RAF1* and *RIT1*, which also show elevated HCM rates among Noonan genes), other RASopathies (Costello syndrome, cardiofaciocutaneous syndrome), and non-syndromic/isolated familial HCM (sarcomeric gene panel-negative cases with subtle dysmorphism should prompt RASopathy panel testing).

**Screening:** No population-based newborn or carrier screening program exists for MRAS-NS given its extreme rarity and de novo inheritance pattern; case-finding is driven by clinical phenotype recognition (particularly early/severe HCM with dysmorphic features) followed by genetic testing.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Highly variable and strongly dependent on age of onset and severity of cardiac involvement:
- **Severe neonatal presentations** carry a poor prognosis: the Motta et al. 2020 p.Gly23Arg patient died of cardiac failure at 2 months of age. This mirrors the broader Noonan-syndrome-with-neonatal-HCM literature, where infants under 6 months with HCM and congestive heart failure have historically had a **~34% one-year survival rate** across Noonan syndrome genotypes generally (not MRAS-specific figure) ([Mount Sinai/ScienceDaily coverage of MEK-inhibitor trial](https://www.mountsinai.org/about/newsroom/2019/a-promising-new-treatment-for-infants-with-noonan-syndrome)).
- **Milder/adult-onset presentations** (Priolo et al. 2023; the endocarditis case) show that survival into adulthood with a good functional status is achievable, particularly with the recurrent p.Thr68Ile variant in some individuals.
- No formal disease-specific survival curves or life-expectancy tables exist given the small case numbers.

**Morbidity/complications:**
- Heart failure (severe cases).
- LVOT obstruction requiring surgical intervention (septal myectomy performed in the Higgins et al. index case at age 8).
- **Infective endocarditis** as a newly recognized complication of the LVOT/HCM anatomical substrate in adult MRAS-NS (first reported 2025/2026).
- Developmental/cognitive morbidity ranging from mild learning difficulty to more significant intellectual disability.

**Recovery potential:** Surgical myectomy has provided symptomatic benefit in at least one reported case; no MRAS-NS-specific data exist on pharmacological (e.g., MEK-inhibitor) reversal of HCM, though this is mechanistically plausible and has been demonstrated in other Noonan-syndrome genotypes (see Treatment section).

**Prognostic factors:** Variant identity appears to correlate loosely with severity in the small case series (the two Gly23 variants — G23V, G23R — and Q71R associate with the most severe pediatric presentations reported to date, while T68I has been associated with both severe pediatric and the mildest reported adult presentation), but this is not a robust, statistically validated genotype-severity correlation given the tiny sample size — Priolo et al. explicitly caution against assuming obligate severe HCM for any MRAS variant.

**Prognostic biomarkers:** None established specific to MRAS-NS.

---

## 12. Treatment

**Pharmacotherapy — targeted RAS/MAPK pathway inhibition (most significant emerging therapeutic direction):**
- **MEK inhibitors (e.g., trametinib)** have been used successfully as targeted, mechanism-based therapy to reverse or ameliorate hypertrophic cardiomyopathy in **other** Noonan-syndrome genotypes with RAS/MAPK pathway hyperactivation — *RAF1*, *RIT1*, and *SOS1* — with dramatic reduction in ventricular wall thickness and improved clinical status reported within months of treatment initiation ([Gross et al. 2019/2022 case reports; PMC6916648](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6916648/); [RIT1 MEK-inhibition case, PMID:36184070]). Because MRAS-NS-associated HCM shares the identical downstream mechanism (RAF/MEK/ERK hyperactivation via the SMP holophosphatase), **MEK inhibition is a mechanistically strongly rationalized candidate therapy for MRAS-NS HCM**, though **no MRAS-NS-specific trametinib case has yet been published** in the literature surveyed here — this represents an important treatment gap/opportunity given the severity of neonatal presentations. Suggested NCIT term: **NCIT:C15632** (Chemotherapy) is too broad/inaccurate; the more appropriate NCIT category is **NCIT:C93352** (Targeted Therapy) or **NCIT:C15986** (Pharmacotherapy) with `therapeutic_agent` bound to trametinib (NCIT:C77908, if curating).
- **Growth hormone therapy** is FDA-approved and effective for short stature in Noonan syndrome generally (not MRAS-specific efficacy data, but the mechanism and approval apply across genotypes), with height SDS improvements of roughly +0.7 to +1 SD over 3 years of therapy reported in general Noonan syndrome GH trials ([Romano et al. 2010, *Pediatrics* 126:746–759]; [PMC8999676](https://pmc.ncbi.nlm.nih.gov/articles/PMC8999676/)). **Caution:** GH stimulates the RAS/MAPK pathway itself, so cardiac status (especially HCM) must be carefully evaluated and monitored before and during GH therapy in any Noonan syndrome patient, a consideration of particular relevance given MRAS-NS's high HCM prevalence.

**Surgical/interventional:**
- **Septal myectomy** for LVOT obstruction — performed in the Higgins et al. index patient at age 8, with the paper describing this as part of her clinical course before her Noonan diagnosis was established. Suggested NCIT term: **NCIT:C15329** (Surgical Procedure), or more specifically a cardiac procedure term.

**Supportive/anti-infective:**
- **Endocarditis prophylaxis/treatment:** The 2025/2026 endocarditis case was managed per 2023 European Society of Cardiology guidelines with intravenous gentamicin plus ceftriaxone, with fever resolution within 5 days ([PMC12794993](https://pmc.ncbi.nlm.nih.gov/articles/PMC12794993/)) — underscoring that patients with MRAS-NS HCM/LVOT pathology may warrant standard endocarditis-prophylaxis consideration for high-risk procedures, per general cardiology guidelines for structural heart disease.
- Standard heart-failure supportive management for severe neonatal presentations (not itemized in detail in the case reports reviewed).

**Rehabilitative/supportive care:**
- Developmental/early intervention services, physical/occupational therapy as clinically indicated for hypotonia and developmental delay (general Noonan syndrome management guideline, not MRAS-specific) — see [Romano et al. 2010 Noonan syndrome management guidelines, *Pediatrics*].

**Experimental/investigational:**
- No MRAS-NS-specific clinical trials (NCT-registered) were identified. Broader Noonan-syndrome/RASopathy MEK-inhibitor and other targeted-therapy trials (e.g., trametinib compassionate-use/case-series programs for neonatal Noonan-HCM) are ongoing and would plausibly be applicable to MRAS-NS on a compassionate or off-label basis given shared pathway biology.
- A related preclinical direction: **mavacamten** (a cardiac myosin inhibitor, FDA-approved for sarcomeric HCM) has shown benefit in improving myocardial energy balance in a preclinical **RASopathy-associated HCM model** (Pediatric Research, 2026), suggesting another potential pharmacologic avenue for RASopathy-HCM including MRAS-NS, though again without MRAS-specific data yet.

**Treatment strategy/algorithm:** No MRAS-NS-specific treatment algorithm exists. Clinically, management should follow (a) general Noonan syndrome multidisciplinary surveillance guidelines (cardiology, growth, development, ophthalmology, audiology), (b) standard pediatric/adult HCM management principles (including consideration of implantable defibrillator risk-stratification in severe cases, though not specifically discussed in the MRAS literature reviewed), and (c) growing consideration of **early mechanism-targeted MEK inhibition** for severe neonatal HCM, extrapolating from the RAF1/RIT1/SOS1 precedent.

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense — NS11 arises from de novo germline mutation and cannot currently be prevented; there are no known modifiable risk-factor exposures.

**Secondary prevention/early detection:**
- **Prenatal ultrasound screening** for the characteristic (though nonspecific) Noonan syndrome antenatal findings (increased nuchal translucency, cystic hygroma, polyhydramnios, pleural/pericardial effusion, and especially fetal cardiac hypertrophy) can prompt **prenatal Noonan-syndrome gene panel testing** (including MRAS) via chorionic villus sampling or amniocentesis, as was done in the Martineau et al. 2026 antenatal case.
- Once a proband is diagnosed, **early and vigilant cardiac surveillance** (echocardiography starting in infancy, given the very high HCM prevalence in this specific genotype) is the key secondary-prevention strategy to detect and manage HCM before decompensation.

**Genetic counseling:** Essential for families of an affected individual — counseling should convey the (a) predominantly de novo occurrence, (b) 50% recurrence risk to future offspring of an affected individual should they reproduce, (c) low but non-zero empiric recurrence risk for parents of an affected child due to possible (undocumented but theoretically possible) germline mosaicism, and (d) markedly variable expressivity (from fatal neonatal HCM to mild adult-onset disease), meaning a specific variant's severity cannot be reliably predicted in a new case, per current evidence (Priolo et al. 2023 explicitly caution against assuming HCM is an "obligatory, early-onset and severe complication").

**Screening/risk stratification:** Given the small case numbers, no formal MRAS-specific risk-stratification tool exists; standard HCM risk-stratification approaches (family history, wall thickness, LVOT gradient, arrhythmia risk factors) would be applied clinically by extension from general HCM/Noonan syndrome cardiology practice.

**Public health/behavioral/prophylactic interventions:** Not applicable to this monogenic disorder beyond the endocarditis-prophylaxis consideration noted under Treatment.

---

## 14. Other Species / Natural Disease

No naturally occurring MRAS-associated Noonan-syndrome-like disease has been reported in non-human species in the literature surveyed. The orthologous gene is well conserved (mouse *Mras*, MGI:1100856, "muscle and microspikes RAS"; rat *Mras*, UniProt P97538). No veterinary case reports, OMIA entries, or comparative pathology studies specific to spontaneous MRAS-driven cardiomyopathy in companion animals or wildlife were identified.

**Taxonomy/comparative biology:** MRAS orthologs are broadly conserved across vertebrates (human *MRAS* NCBI Gene 22808; mouse *Mras* MGI:1100856; rat *Mras* UniProt P97538/Gene), consistent with its fundamental role in RAS/MAPK signaling; the conservation of the specific mutated residues (Gly23, Thr68, Gln71 all noted as "highly conserved from zebrafish to humans" in the primary literature) supports functional conservation and the biological plausibility of cross-species modeling.

---

## 15. Model Organisms

This is a notable **evidence gap** for NS11 specifically:

- **No germline MRAS-NS mouse, zebrafish, or other whole-organism knock-in model** was identified in the literature reviewed for this report. This contrasts with several other Noonan-syndrome genes (e.g., LZTR1, PTPN11, RAF1), for which dedicated mouse models exist (e.g., a 2026 JCI Insight paper on "Dysregulation of RAS proteostasis by autosomal-dominant LZTR1 mutation induces Noonan syndrome–like phenotypes in mice" demonstrates this modeling approach has been applied to other Noonan genes but evidently not yet published for MRAS).
- An existing ***Mras*-knockout mouse** exists but has been studied in the context of **coronary artery disease/atherosclerosis** (showing a B-cell phenotype and reduced macrophage infiltration in atherosclerotic plaques) rather than as a Noonan-syndrome or cardiac-hypertrophy disease model — this is a **loss-of-function** model relevant to a distinct MRAS biology (GWAS-identified coronary artery disease association) and does **not** recapitulate the gain-of-function NS11 mechanism ([Shah 2024, IUBMB Life](https://iubmb.onlinelibrary.wiley.com/doi/full/10.1002/iub.2805)).
- **Cellular/iPSC models** are the primary experimental system used to date:
  - **Patient-derived and CRISPR/Cas9-corrected isogenic iPSC-derived cardiomyocytes (iPSC-CMs)** carrying p.Gly23Val-MRAS: mutant/patient-derived iPSC-CMs were significantly larger than corrected isogenic controls, with altered gene expression and signaling consistent with cardiac hypertrophy — providing direct, tissue-relevant (though in vitro) recapitulation of the cardiac phenotype and representing the strongest available functional disease model ([Higgins et al. 2019, *Circ Genom Precis Med*, DOI:10.1161/CIRCGEN.119.002648](https://www.ahajournals.org/doi/10.1161/CIRCGEN.119.002648)).
  - **Heterologous overexpression systems** (HEK293T, COS-1, Neuro2A cells) transiently expressing tagged wild-type or mutant MRAS constructs have been used across all the primary genetic/functional papers (Higgins 2017, Motta 2020, Suzuki 2019) to establish GTP-loading, ERK/AKT signaling, and SHOC2/PPP1CB binding phenotypes.
- **Zebrafish RASopathy models** exist as a general platform (e.g., FRET-based "Teen" ERK biosensor zebrafish models used to study RASopathy-associated ERK dynamics and MEK-inhibitor rescue; [PMC11005195](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11005195/)), and zebrafish/frog systems are recognized as valuable for RASopathy research generally ([PMID:32506834](https://pubmed.ncbi.nlm.nih.gov/32506834/)), but **no MRAS-specific zebrafish knock-in model** was found in this search.

**Model limitations:** The absence of an in vivo (whole-organism) MRAS-NS model is a significant gap limiting understanding of the developmental origins of the extracardiac phenotype (craniofacial dysmorphism, growth, neurodevelopment) and precluding preclinical in vivo testing of MEK-inhibitor or other targeted therapies specifically for this genotype — an important direction for future research given the mechanistic rationale for such therapy.

---

## Summary of Key Ontology Term Suggestions for KB Curation

- **Gene:** hgnc:7227 (MRAS)
- **MONDO:** MONDO:0032786 (Noonan syndrome 11)
- **Key HP terms:** HP:0001639 (Hypertrophic cardiomyopathy), HP:0001692 (Left ventricular outflow tract obstruction), HP:0004322 (Short stature), HP:0001263 (Global developmental delay), HP:0001249 (Intellectual disability), HP:0000369 (Low-set ears), HP:0001252 (Hypotonia)
- **Key GO terms (biological process):** GO:0007265 (Ras protein signal transduction), GO:0000165 (MAPK cascade), GO:0003300/GO:0014897 (cardiac/striated muscle hypertrophy)
- **Key CL terms:** CL:0000746 (cardiomyocyte)
- **Key UBERON terms:** UBERON:0000948 (heart), UBERON:0002012 (ventricle)
- **CHEBI/NCIT for treatment:** trametinib (MEK inhibitor, targeted therapy), NCIT:C15329 (Surgical Procedure, for myectomy)
- **Functional impact category:** GAIN_OF_FUNCTION (constitutive/hyperactive GTPase signaling — not simply increased pathway flux, given evidence of qualitatively altered nucleotide cycling and complex assembly)

---

## Sources

- [OMIM #618499 — Noonan Syndrome 11 (NS11)](https://omim.org/entry/618499)
- [OMIM *608435 — MRAS (Muscle RAS Viral Oncogene Homolog)](https://omim.org/entry/608435)
- [Higgins EM et al. 2017. "Elucidation of MRAS-mediated Noonan syndrome with cardiac hypertrophy." JCI Insight 2(5):e91225.](https://insight.jci.org/articles/view/91225) (PMCID: PMC5333962)
- [Higgins EM et al. 2019. "MRAS Variants Cause Cardiomyocyte Hypertrophy in Patient-Specific iPSC-Derived Cardiomyocytes." Circ Genom Precis Med 12:e002648.](https://www.ahajournals.org/doi/10.1161/CIRCGEN.119.002648)
- [Motta M et al. 2020. "Activating MRAS mutations cause Noonan syndrome associated with hypertrophic cardiomyopathy." Hum Mol Genet 29(11):1772–1783. PMID:31108500.](https://academic.oup.com/hmg/article/29/11/1772/5492387)
- [Suzuki H et al. 2019. "Severe Noonan syndrome phenotype associated with a germline Q71R MRAS variant." Am J Med Genet A 179:1628–1630. PMID:31173466.](https://pubmed.ncbi.nlm.nih.gov/31173466/)
- [Priolo M et al. 2023. "Natural history of MRAS-related Noonan syndrome: Evidence of mild adult-onset left ventricular hypertrophy and neuropsychiatric features." Am J Med Genet C Semin Med Genet. PMID:36734411.](https://onlinelibrary.wiley.com/doi/full/10.1002/ajmg.c.32034)
- [Martineau et al. 2026. "Hypertrophic Cardiomyopathy as a Key Feature of MRAS-Related Noonan Syndrome: New Case and Comprehensive Literature Review." Prenatal Diagnosis. DOI:10.1002/pd.70134.](https://obgyn.onlinelibrary.wiley.com/doi/10.1002/pd.70134)
- [Novel characterization of MRAS mutation-associated Noonan syndrome: infective endocarditis case report. PMC12794993.](https://pmc.ncbi.nlm.nih.gov/articles/PMC12794993/)
- [Kwon JJ et al. 2018. "SHOC2-MRAS-PP1 complex positively regulates RAF activity and contributes to Noonan syndrome pathogenesis." PNAS. PMID:30348783.](https://www.pnas.org/doi/10.1073/pnas.1720352115)
- [Kwon JJ et al. 2022. "Structure of the MRAS–SHOC2–PP1C phosphatase complex." Nature. PMID:35830882.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9452295/)
- [Bonsor DA et al. 2022. "Structure of the SHOC2–MRAS–PP1C complex provides insights into RAF activation and Noonan syndrome." Nat Struct Mol Biol. PMID:36175670.](https://www.nature.com/articles/s41594-022-00841-4)
- [ClinVar RCV000787303 — MRAS c.68G>T (p.Gly23Val)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000787303/)
- [ClinGen RASopathy gene curation — MRAS (HGNC:7227)](https://search.clinicalgenome.org/kb/genes/HGNC:7227)
- [GeneReviews — Noonan Syndrome (NBK1124)](https://www.ncbi.nlm.nih.gov/books/NBK1124/)
- [Gross AM et al. and related case reports — MEK-inhibition (trametinib) in Noonan-syndrome hypertrophic cardiomyopathy (RAF1, RIT1, SOS1). PMC6916648.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6916648/)
- [GeneCards — MRAS](https://www.genecards.org/cgi-bin/carddisp.pl?gene=MRAS)
- [Shah et al. 2024. "MRAS in coronary artery disease—Uncharted territory." IUBMB Life.](https://iubmb.onlinelibrary.wiley.com/doi/full/10.1002/iub.2805)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 21 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001692` (2 mentions) - the report calls it "Variable", "Left ventricular outflow tract obstruction"; HP calls it **Atrial arrhythmia**
- `UBERON:0002012` (2 mentions) - the report calls it "ventricle"; UBERON calls it **pulmonary artery**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0000368` (obsolete Low-set, posteriorly rotated ears) (1 mention) - replaced by `HP:0000358`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000280` (1 mention) - the report calls it "Coarse facial features, when applicable"; HP calls it **Coarse facial features**
- `HP:0000494` (1 mention) - the report calls it "downslanted"; HP calls it **Downslanted palpebral fissures**
- `GO:0014897` (2 mentions) - the report calls it "cardiac/striated muscle hypertrophy"; GO calls it **striated muscle hypertrophy**
- `CL:0000746` (2 mentions) - the report calls it "cardiomyocytes", "Cardiac muscle tissue — **cardiomyocytes", "cardiomyocyte"; CL calls it **cardiac muscle cell**, and lists "cardiac muscle fiber" among its other names
- `NCIT:C15329` (2 mentions) - the report calls it "Surgical Procedure, for myectomy"; NCIT calls it **Surgical Procedure**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001692` - called "Variable", "Left ventricular outflow tract obstruction"
- `CL:0000746` - called "cardiomyocytes", "Cardiac muscle tissue — **cardiomyocytes", "cardiomyocyte"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.
