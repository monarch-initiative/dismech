---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T16:14:28.044175'
end_time: '2026-05-10T16:44:46.057499'
duration_seconds: 1818.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chondrodysplasia Punctata, Tibial-metacarpal Type
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chondrodysplasia Punctata, Tibial-metacarpal Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chondrodysplasia Punctata, Tibial-metacarpal Type** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


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

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chondrodysplasia Punctata, Tibial-metacarpal Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chondrodysplasia Punctata, Tibial-metacarpal Type** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Comprehensive Research Report: Chondrodysplasia Punctata, Tibia(l)-metacarpal Type (CDP‑TM)

### Scope and evidence note
Chondrodysplasia punctata (CDP) is a heterogeneous radiographic/clinical spectrum rather than a single disease entity, and “tibia–metacarpal type” (CDP‑TM) is a rare non‑rhizomelic subtype with uncertain molecular cause. Much of the most clinically actionable guidance comes from (i) long-term natural history case series for CDP‑TM and (ii) broader CDP reviews and cervical-spine surgical series that include multiple CDP subtypes, including one CDP‑TM patient. Recent (2023–2024) literature specific to CDP‑TM is sparse; therefore, recent developments are drawn from 2023 CDP‑TM cervical myelopathy management and 2023–2024 skeletal dysplasia nosology/NGS context plus related CDP subtypes. (patel2023cervicalcorpectomyin pages 1-2, unger2023nosologyofgenetic pages 4-6, unger2023nosologyofgenetic pages 6-8)

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
**CDP‑TM (OMIM 118651)** is a very rare skeletal dysplasia within the non‑rhizomelic CDP spectrum, characterized by **punctate (stippled) calcifications in cartilage/epiphyses in fetal/neonatal life** and a **distinctive pattern of limb shortening**, especially **short tibiae** and **short metacarpals (notably 3rd/4th)**, with variable vertebral anomalies. Many punctate calcifications **fade/disappear in early childhood**, but disproportionate short stature and orthopedic/spinal complications can persist or emerge later. (rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, savarirayan2004longtermfollow‐upin pages 1-2, savarirayan2004longtermfollow‐upin pages 5-8)

**Primary evidence (human clinical):** original series (7 patients) (Rittler 1990), long-term adult follow-up (3 unrelated patients) (Savarirayan 2004), and multiple case reports including prenatal detection (Jansen 2000; Wester 2002; Kaissi 2008; Shukla 2015) (rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, savarirayan2004longtermfollow‐upin pages 1-2, jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, wester2002chondrodysplasiapunctata(cdp) pages 2-3, kaissi2008progressivejointlimitations pages 2-5, shukla2015chondrodysplasiapunctatatibia pages 1-2).

### 1.2 Key identifiers and synonyms
A structured summary of identifiers/synonyms supported by retrieved sources is provided here:

| Identifier type | Value | Source (citation id) | URL (if present) | Notes |
|---|---|---|---|---|
| Preferred disease name | Chondrodysplasia punctata, tibia-metacarpal type | (shukla2015chondrodysplasiapunctatatibia pages 1-2, savarirayan2004longtermfollow‐upin pages 1-2, rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5) | https://doi.org/10.1097/mcd.0000000000000076 | Very rare skeletal dysplasia/CDP subtype. |
| Abbreviation | CDP-TM | (shukla2015chondrodysplasiapunctatatibia pages 1-2, savarirayan2004longtermfollow‐upin pages 1-2, patel2023cervicalcorpectomyin pages 1-2) | https://doi.org/10.1002/ajmg.a.20383 | Common shorthand used in the literature for tibia-metacarpal type chondrodysplasia punctata. |
| OMIM | 118651 | (wessels2003fetuswithan pages 2-2, shukla2015chondrodysplasiapunctatatibia pages 1-2) | https://doi.org/10.1097/mcd.0000000000000076 | Explicitly linked to tibia-metacarpal CDP in retrieved sources. |
| Alternative name | Chondrodysplasia punctata, tibial-metacarpal type | (kaissi2008progressivejointlimitations pages 5-5, jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, kozłowski2006retrospectivediagnosisof pages 1-4) | https://doi.org/10.1186/1757-1626-1-112 | Spelling variant using “tibial” rather than “tibia”; used in case reports/reviews. |
| Alternative name | Chondrodysplasia punctata, tibia–metacarpal type | (savarirayan2004longtermfollow‐upin pages 1-2, savarirayan2004longtermfollow‐upin pages 5-8) | https://doi.org/10.1002/ajmg.a.20383 | En dash variant used in Savarirayan et al. |
| Alternative name | Chondrodysplasia punctata, tibia-metacarpal (MT) type | (rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5) | https://doi.org/10.1002/ajmg.1320370208 | Original designation in Rittler et al.; “MT” is an abbreviation of metacarpal-tibia/tibia-metacarpal type. |
| Alternative name | MT type | (rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5) | https://doi.org/10.1002/ajmg.1320370208 | Short form used by Rittler et al. for the subtype. |
| Nosologic scope note | Non-rhizomelic chondrodysplasia punctata subclassification | (wessels2003fetuswithan pages 1-2, wessels2003fetuswithan pages 3-7) | https://doi.org/10.1002/ajmg.a.20202 | Retrieved review text lists tibia-metacarpal type among non-rhizomelic/anatomical subclassifications of CDP. |
| MONDO | not found in retrieved sources |  |  | No MONDO identifier was present in the retrieved evidence. |
| Orphanet | not found in retrieved sources |  |  | No Orphanet identifier was present in the retrieved evidence. |
| ICD-10/ICD-11 | not found in retrieved sources |  |  | No ICD identifier was present in the retrieved evidence. |
| MeSH | not found in retrieved sources |  |  | No MeSH identifier was present in the retrieved evidence. |


*Table: This table summarizes the disease identifiers and naming variants directly supported by the retrieved literature for chondrodysplasia punctata, tibia-metacarpal type. It is useful for harmonizing nomenclature across case reports, reviews, and database-oriented knowledge base entries.*

**Not found in retrieved sources:** MONDO, Orphanet, ICD‑10/ICD‑11, and MeSH identifiers for this specific subtype were not present in the retrieved texts, so they cannot be asserted from this evidence set (artifact-00).

### 1.3 Data provenance
The CDP‑TM evidence base in this corpus is primarily **individual patient reports** and **small case series**, plus broader CDP reviews/surgical series extrapolated to CDP‑TM. (rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, savarirayan2004longtermfollow‐upin pages 1-2, morota2017surgicalmanagementof pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**CDP‑TM etiology remains unknown**. A fetal CDP‑TM report states: “**the genetic defect in CP‑MT remains to be delineated**.” (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 4-4)

In three unrelated CDP‑TM patients followed long term, extensive investigations were unrevealing, including **normal karyotypes**, **no SHOX deletion by FISH**, **normal sterol and VLCFA profiles**, and **no detected arylsulfatase D/E mutations**, leading to the conclusion that “**the etiology of CDP‑TM therefore remains unknown**.” (savarirayan2004longtermfollow‐upin pages 5-8)

### 2.2 Risk factors
**Genetic risk factors (causal variants):** none have been established for CDP‑TM in the retrieved primary literature; no pathogenic variant spectrum can be listed for CDP‑TM itself. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 4-4, savarirayan2004longtermfollow‐upin pages 5-8)

**Inheritance pattern (reported):** CDP‑TM is usually described as **sporadic** with historical suggestion of **autosomal dominant** inheritance/new dominant mutations; Savarirayan notes it is “**thought to be inherited as an autosomal dominant trait**” but also that “**no cases of familial recurrence have been reported**” in their context. (savarirayan2004longtermfollow‐upin pages 1-2) Shukla similarly describes sporadic occurrence with “probable autosomal dominant” inheritance but cites a sibling recurrence report raising **recessive inheritance or gonadal mosaicism**. (shukla2015chondrodysplasiapunctatatibia pages 1-2)

**Environmental/teratogenic phenocopies and exposures (important differential):** CDP in general can arise from maternal exposures/conditions including warfarin, hydantoin/phenytoin, maternal vitamin K deficiency/malabsorption, and maternal autoimmune disease (e.g., SLE). (wessels2003fetuswithan pages 1-2, irving2008chondrodysplasiapunctataa pages 2-3, wessels2003fetuswithan pages 7-8)

A specific relevant observation is a case with CDP‑TM-like features in the context of **maternal phenytoin treatment during pregnancy**, supporting that anticonvulsant exposure can mimic or contribute to a tibia–metacarpal phenotype in some cases. (wester2002chondrodysplasiapunctata(cdp) pages 2-3)

### 2.3 Protective factors
No protective genetic or environmental factors for CDP‑TM were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Direct gene–environment interaction studies for CDP‑TM were not found in the retrieved literature. For CDP more broadly, multiple genetic etiologies and multiple maternal exposures converge on a shared endpoint of abnormal endochondral mineralization/stippling (see mechanism). (wessels2003fetuswithan pages 1-2, irving2008chondrodysplasiapunctataa pages 10-11)

---

## 3. Phenotypes

### 3.1 Phenotype spectrum (with onset, progression, and frequency where available)
A structured phenotype/HPO suggestion table is provided here:

| Feature (plain language) | Evidence/notes | Suggested HPO term(s) |
|---|---|---|
| Congenital short-limbed disproportionate stature | CDP-TM presents from fetal/neonatal life with disproportionately short limbs and later short stature. Prenatal ultrasound at 16 weeks showed generalized shortening of long bones; childhood/adult follow-up showed persistent disproportionate short stature, with reported adult heights 152, 138, and 148 cm in 3 unrelated adults. Rittler reported height typically 2–4 SD below the median. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, savarirayan2004longtermfollow‐upin pages 1-2, rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5) | HP:0000006 Autosomal dominant inheritance (historical/uncertain); HP:0004322 Short stature; HP:0003095 Short limb |
| Tibial shortening, often bowed | A defining feature is marked shortening of the tibiae, often with bowing; Rittler and Savarirayan considered shortened/bowed tibiae a constant neonatal feature. Prenatal and infant imaging showed short tibiae, sometimes with mesomelic or rhizomelic limb shortening. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, savarirayan2004longtermfollow‐upin pages 1-2, rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, savarirayan2004longtermfollow‐upin pages 5-8) | HP:0005737 Short tibia; HP:0002980 Bowing of the long bones |
| Relatively long/overshooting fibula | Fibula may appear relatively long compared with the short tibia; Shukla described an “overshooting” fibula, and earlier reports noted relatively elongated fibulae/proximal fibular overgrowth. Present from infancy and may persist radiographically into adulthood. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, savarirayan2004longtermfollow‐upin pages 5-8, shukla2015chondrodysplasiapunctatatibia pages 2-4) | HP:0003097 Fibular overgrowth |
| Short metacarpals, especially 3rd/4th | Characteristic hand finding is shortening of metacarpals, especially the 4th and sometimes 3rd; seen in infancy and usually persists after stippling resolves. Trident hand/small hands may be present in severe cases. (shukla2015chondrodysplasiapunctatatibia pages 1-2, rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, savarirayan2004longtermfollow‐upin pages 5-8, shukla2015chondrodysplasiapunctatatibia pages 2-4) | HP:0010049 Short metacarpal; HP:0001166 Arachnodactyly/hand anomaly not specific; HP:0004050 Short 4th metacarpal |
| Short proximal/middle/terminal phalanges | Reports describe brachyphalangy, including a very short proximal phalanx of digit 2 and shortened middle/terminal phalanges; present prenatally/infancy and may remain after neonatal calcific stippling fades. (shukla2015chondrodysplasiapunctatatibia pages 1-2, wester2002chondrodysplasiapunctata(cdp) pages 2-3, shukla2015chondrodysplasiapunctatatibia pages 2-4) | HP:0009381 Short phalanx of finger; HP:0009823 Brachydactyly |
| Punctate calcific stippling of epiphyses/cartilage | Hallmark early radiologic sign is punctate (stippled) calcification, most marked neonatally/infancy in sacral, tarsal, carpal, vertebral, calcaneal, metatarsal, distal femoral, and hand regions. Prenatally, stippling and abnormal calcification can be seen on ultrasound/radiography. (kaissi2008progressivejointlimitations pages 5-5, jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, shukla2015chondrodysplasiapunctatatibia pages 1-2, savarirayan2004longtermfollow‐upin pages 1-2, wester2002chondrodysplasiapunctata(cdp) pages 2-3) | HP:0010655 Stippled epiphysis |
| Vertebral clefts and delayed/deficient vertebral ossification | Newborn/fetal imaging shows coronal clefts and deficient ossification of cervical/thoracolumbar vertebral bodies; Shukla also described severe platyspondyly/ovoid vertebrae in a severe infant case. These changes often improve over time, though some spinal morphology changes may persist. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, shukla2015chondrodysplasiapunctatatibia pages 1-2, rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, savarirayan2004longtermfollow‐upin pages 5-8, shukla2015chondrodysplasiapunctatatibia pages 2-4) | HP:0008463 Coronal cleft vertebrae; HP:0000926 Platyspondyly; HP:0003312 Delayed vertebral ossification |
| Radial bowing with distal ulnar hypoplasia/short ulna | Upper-limb radiology may show short ulnae, distal ulnar hypoplasia, and radial bowing/dislocation. Present in infancy/childhood; some abnormalities may remain after generalized stippling resolves. (savarirayan2004longtermfollow‐upin pages 1-2, rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5) | HP:0003035 Bowing of radius; HP:0003025 Short ulna |
| Craniofacial hypoplasia | Common facial features include flat or hypoplastic midface, depressed nasal bridge, small mouth, micrognathia, and sometimes short neck. Present prenatally or at birth and may remain clinically recognizable. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, wester2002chondrodysplasiapunctata(cdp) pages 2-3, shukla2015chondrodysplasiapunctatatibia pages 2-4) | HP:0000326 Hypoplasia of the midface; HP:0005280 Depressed nasal bridge; HP:0000347 Micrognathia; HP:0000470 Short neck |
| Clubfoot / pes equinovarus | Fetal and infant cases have bilateral clubfeet/equinovarus. This is congenital and may require orthopedic management. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, wester2002chondrodysplasiapunctata(cdp) pages 2-3) | HP:0001762 Talipes equinovarus |
| Small hands and feet / brachymetatarsia | Case reports describe small hands/feet and short metatarsals with tarsal involvement; may be apparent prenatally or in infancy. (kaissi2008progressivejointlimitations pages 2-5, shukla2015chondrodysplasiapunctatatibia pages 2-4) | HP:0001182 Small hands; HP:0001773 Short foot; HP:0010741 Short metatarsal |
| Catch-up remodeling and disappearance of stippling | Natural history is notable for resolution of stippling and many vertebral/tibial radiographic abnormalities over the first years of life and childhood. Coronal clefts and tarsal stippling may disappear with age; calcifications were nearly gone by 18 months in one infant, and Savarirayan documented impressive tibial catch-up growth into adulthood. (rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, wester2002chondrodysplasiapunctata(cdp) pages 2-3, savarirayan2004longtermfollow‐upin pages 5-8) | HP:0010655 Stippled epiphysis; HP:0009115 Abnormality of skeletal morphology |
| Progressive joint limitation/contracture phenotype | Although stippling fades, some patients develop progressive limitation of hip/ankle and other joints after early childhood; Kaissi emphasized progressive joint limitation becoming clearer after age 4 years. Supportive physiotherapy/hydrotherapy has been used. (kaissi2008progressivejointlimitations pages 5-5, kaissi2008progressivejointlimitations pages 2-5) | HP:0001376 Limited joint mobility; HP:0001385 Hip contracture; HP:0001771 Ankle contracture |
| Recurrent patellar dislocation | A frequent long-term orthopedic complication in reported follow-up; present in all 3 adults in Savarirayan’s series and also highlighted in Kaissi. (savarirayan2004longtermfollow‐upin pages 1-2, kaissi2008progressivejointlimitations pages 5-5, kaissi2008progressivejointlimitations pages 2-5) | HP:0006380 Recurrent patellar dislocation |
| Hip dysplasia / hip instability | Hip dysplasia/luxation and later degenerative hip problems can occur as complications during childhood/adulthood. (savarirayan2004longtermfollow‐upin pages 1-2, kaissi2008progressivejointlimitations pages 2-5) | HP:0001388 Hip dysplasia; HP:0003272 Hip dislocation |
| Spinal stenosis / cervical or lumbar cord compression | Long-term complications can include spinal stenosis. Savarirayan reported lumbar stenosis requiring laminectomy in one adult; Patel 2023 described an 18-year-old with CDP-TM and dysplastic C4–C5 vertebrae causing focal kyphosis, cord compression, and myelomalacia requiring corpectomies/fusion. (savarirayan2004longtermfollow‐upin pages 1-2, patel2023cervicalcorpectomyin media d3641eed, patel2023cervicalcorpectomyin pages 1-2, patel2023cervicalcorpectomyin pages 2-3) | HP:0003418 Spinal stenosis; HP:0008439 Cervical vertebral dysplasia; HP:0008443 Kyphosis |
| Motor development generally preserved; cognition often normal | Limited longitudinal data suggest normal psychomotor/intellectual development in many reported cases, including the adult series, although individual variability exists and one case report noted subnormal intelligence. (savarirayan2004longtermfollow‐upin pages 1-2, kaissi2008progressivejointlimitations pages 5-5, rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5) | HP:0001256 Intellectual disability (if present); HP:0011342 Mild global developmental delay (if present) |
| Otitis media / auditory problems | Chronic serous otitis media or auditory issues were reported in 2 of 3 adults in Savarirayan’s natural history series. (savarirayan2004longtermfollow‐upin pages 1-2, shukla2015chondrodysplasiapunctatatibia pages 2-4) | HP:0000388 Chronic otitis media; HP:0000365 Hearing impairment |
| Typical onset pattern | Earliest manifestations are prenatal or congenital, detectable by second-trimester ultrasound or neonatal radiography. Stippling is most obvious in the fetal/newborn period, while orthopedic complications such as joint limitation, patellar dislocation, and spinal stenosis may emerge later in childhood/adolescence/adulthood. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, savarirayan2004longtermfollow‐upin pages 1-2, wester2002chondrodysplasiapunctata(cdp) pages 2-3, patel2023cervicalcorpectomyin pages 1-2) | HP:0003577 Congenital onset; HP:0011462 Childhood onset |
| Disease course summary | Course is mixed: early radiographic abnormalities are often partially self-resolving, but residual skeletal disproportions and later orthopedic/spinal complications can be chronic and sometimes progressive. Long-term physical function may remain relatively good, but selected patients need orthopedic or neurosurgical intervention. (savarirayan2004longtermfollow‐upin pages 1-2, savarirayan2004longtermfollow‐upin pages 5-8, patel2023cervicalcorpectomyin pages 1-2, patel2023cervicalcorpectomyin pages 2-3) | HP:0002715 Abnormality of the musculoskeletal system; HP:0012828 Progressive abnormality |


*Table: This table summarizes the phenotype and radiologic spectrum of chondrodysplasia punctata, tibia-metacarpal type (OMIM 118651), including onset, natural history, complications, and suggested HPO mappings based only on the specified literature.*

Key recurring clinical/radiologic features include:
- **Stippled epiphyses / punctate calcifications** (neonatal/infant; often sacral/carpal/tarsal prominent) (savarirayan2004longtermfollow‐upin pages 1-2, rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5)
- **Short tibiae (often bowed)** with **relative fibular overgrowth/“overshooting” fibula** (savarirayan2004longtermfollow‐upin pages 5-8, shukla2015chondrodysplasiapunctatatibia pages 2-4)
- **Short metacarpals** (classically 3rd/4th) and brachyphalangy (rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, savarirayan2004longtermfollow‐upin pages 5-8)
- **Vertebral ossification anomalies** (coronal clefts, deficient ossification; variable platyspondyly in severe infant report) (rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, shukla2015chondrodysplasiapunctatatibia pages 2-4)
- **Craniofacial**: midface hypoplasia/depressed nasal bridge/micrognathia (rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, wester2002chondrodysplasiapunctata(cdp) pages 2-3)
- **Orthopedic complications**: recurrent patellar dislocation (noted in all three long‑term adults), hip dysplasia, joint limitation/contractures, spinal stenosis (savarirayan2004longtermfollow‐upin pages 1-2, kaissi2008progressivejointlimitations pages 2-5)

**Natural history (quantitative):** In long-term follow-up of three unrelated CDP‑TM patients (followed **37, 25, and 32 years**), adult heights were **152 cm, 138 cm, and 148 cm**, with “**intellectual function… normal, and physical function… well preserved**,” but common morbidities included patellar dislocation (all), chronic serous otitis media (two), hip dysplasia (one), and lumbar stenosis requiring laminectomy (one). (savarirayan2004longtermfollow‐upin pages 1-2)

### 3.2 Quality of life impact
Formal QoL instruments (EQ‑5D/SF‑36/PROMIS) were not reported in the retrieved CDP‑TM sources. Functional impact is inferred from reported orthopedic and neurologic complications (e.g., patellar instability, joint limitation, spinal stenosis/myelopathy) and from need for surgeries/rehabilitation. (savarirayan2004longtermfollow‐upin pages 1-2, patel2023cervicalcorpectomyin pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes for CDP‑TM
**No causal gene has been confirmed for CDP‑TM** in the retrieved literature; multiple publications explicitly state the defect is unknown. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 4-4, savarirayan2004longtermfollow‐upin pages 5-8)

### 4.2 Pathogenic variants (CDP‑TM)
Because no causal gene is established, **no CDP‑TM pathogenic variant list** (HGNC IDs, variant classes, allele frequencies) can be provided from this evidence set.

### 4.3 Related CDP entities with known genes/pathways (for differential)
The CDP umbrella includes subtypes with defined mechanisms/genes:
- **RCDP**: peroxisomal dysfunction (PEX7 highlighted) (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 4-4, wessels2003fetuswithan pages 7-8)
- **CDPX1**: ARSE-related X‑linked CDP (wessels2003fetuswithan pages 2-3, irving2008chondrodysplasiapunctataa pages 10-11)
- **CDPX2**: cholesterol biosynthesis/sterol pathway disorders (patel2023cervicalcorpectomyin pages 2-3, wessels2003fetuswithan pages 1-2)

A comparative etiologic summary table is provided:

| Entity/subtype | Mode of inheritance (if stated) | Gene/pathway implicated | Evidence type (human clinical/biochemical) | Key supporting statement (short) | Key citations (citation ids) | URL+pub date where available |
|---|---|---|---|---|---|---|
| CDP-TM / tibia-metacarpal type (OMIM 118651) | Usually sporadic; historically thought to be autosomal dominant; advanced parental age/new dominant mutation suggested; familial recurrence rarely reported | Unknown; tested pathways/genes negative in reported cases | Human clinical + biochemical/genetic exclusion testing | CDP-TM is a distinct non-rhizomelic CDP subtype with unknown molecular cause; Savarirayan reported normal karyotype, no SHOX deletion, normal sterol profile, and no ARSD/ARSE mutations; Jansen stated “the genetic defect in CP-MT remains to be delineated.” | (shukla2015chondrodysplasiapunctatatibia pages 1-2, savarirayan2004longtermfollow‐upin pages 1-2, savarirayan2004longtermfollow‐upin pages 5-8, patel2023cervicalcorpectomyin pages 2-3, jansen2000chondrodysplasiapunctatatibialmetacarpal pages 4-4) | https://doi.org/10.1002/ajmg.a.20383 (Jan 2004); https://doi.org/10.7863/jum.2000.19.10.719 (Oct 2000); https://doi.org/10.1097/mcd.0000000000000076 (Jul 2015); https://doi.org/10.3171/case23302 (Nov 2023) |
| CDPX1 / X-linked recessive CDP / brachytelephalangic type | X-linked recessive | ARSE (arylsulfatase E); often framed within vitamin K–related biology/pathway | Human clinical + molecular/genetic + review | ARSE mutations/deletions cause CDPX1; Wessels notes “mutations in the arylsulfatase E gene (ARSE)” and Morota identifies CDPX1 as due to ARSE mutations on Xp22. | (wessels2003fetuswithan pages 2-3, morota2017surgicalmanagementof pages 6-8, jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, irving2008chondrodysplasiapunctataa pages 2-3) | https://doi.org/10.1002/ajmg.a.20202 (Jul 2003); https://doi.org/10.3171/2017.5.PEDS16554 (Aug 2017 online / Oct 2017 issue); https://doi.org/10.7863/jum.2000.19.10.719 (Oct 2000); https://doi.org/10.1097/mcd.0b013e3282fdcc70 (Oct 2008) |
| CDPX2 / Conradi-Hünermann type | X-linked dominant | Cholesterol biosynthesis / sterol pathway (EBP named in broader CDP review literature; Patel/Morota summarize as cholesterol-synthesis related) | Human clinical + biochemical/review | CDPX2 is a cholesterol-synthesis disorder within the CDP spectrum; Patel describes CDPX2 as “X-linked dominant, disordered cholesterol synthesis,” and Wessels classifies Conradi-Hünermann among cholesterol-metabolism defects. | (patel2023cervicalcorpectomyin pages 2-3, wessels2003fetuswithan pages 1-2, irving2008chondrodysplasiapunctataa pages 2-3, morota2017surgicalmanagementof pages 6-8) | https://doi.org/10.3171/case23302 (Nov 2023); https://doi.org/10.1002/ajmg.a.20202 (Jul 2003); https://doi.org/10.1097/mcd.0b013e3282fdcc70 (Oct 2008); https://doi.org/10.3171/2017.5.PEDS16554 (Aug 2017 online / Oct 2017 issue) |
| RCDP / rhizomelic CDP | Autosomal recessive | Peroxisomal pathway; PEX7 emphasized | Human clinical + biochemical + molecular/review | Rhizomelic CDP is the peroxisomal form; Jansen/Wessels/Irving note peroxisomal defects and PEX7, and Patel summarizes RCDP as autosomal recessive with peroxisomal dysfunction. | (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 4-4, jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, patel2023cervicalcorpectomyin pages 2-3, wessels2003fetuswithan pages 1-2, irving2008chondrodysplasiapunctataa pages 2-3, irving2008chondrodysplasiapunctataa pages 3-4) | https://doi.org/10.7863/jum.2000.19.10.719 (Oct 2000); https://doi.org/10.3171/case23302 (Nov 2023); https://doi.org/10.1002/ajmg.a.20202 (Jul 2003); https://doi.org/10.1097/mcd.0b013e3282fdcc70 (Oct 2008) |
| Warfarin embryopathy–associated CDP | Not inherited; teratogenic embryopathy | Vitamin K cycle disruption; Wessels notes warfarin inhibits EPHX1 and ARSE | Human clinical embryopathy + mechanistic review | Warfarin exposure is a classic non-genetic cause of CDP phenocopy; Wessels lists warfarin embryopathy among vitamin K–related causes and states warfarin inhibits EPHX1 and ARSE. | (wessels2003fetuswithan pages 2-3, wessels2003fetuswithan pages 7-8, wessels2003fetuswithan pages 1-2, irving2008chondrodysplasiapunctataa pages 2-3) | https://doi.org/10.1002/ajmg.a.20202 (Jul 2003); https://doi.org/10.1097/mcd.0b013e3282fdcc70 (Oct 2008) |
| Hydantoin/phenytoin embryopathy–associated CDP | Not inherited; teratogenic embryopathy | Likely vitamin K pathway interference via EPHX1; fetal anticonvulsant exposure | Human clinical case report + mechanistic review | Wessels states “Antiepileptics such as hydantoin probably exert their toxicity through EPHX1”; Wester reported a child with CDP-TM-like features after maternal phenytoin treatment during pregnancy. | (wester2002chondrodysplasiapunctata(cdp) pages 2-3, wessels2003fetuswithan pages 7-8, irving2008chondrodysplasiapunctataa pages 2-3) | https://doi.org/10.1002/pd.352 (Aug 2002); https://doi.org/10.1002/ajmg.a.20202 (Jul 2003); https://doi.org/10.1097/mcd.0b013e3282fdcc70 (Oct 2008) |
| Maternal vitamin K deficiency / malabsorption embryopathy | Not inherited; maternal deficiency state | Vitamin K metabolism / gamma-carboxylation pathway | Human clinical embryopathy + biochemical/review | Non-genetic CDP may result from impaired maternal-fetal vitamin K biology; Wessels and Irving list maternal vitamin K malabsorption/deficiency among recognized causes. | (wessels2003fetuswithan pages 2-3, wessels2003fetuswithan pages 7-8, irving2008chondrodysplasiapunctataa pages 2-3, wessels2003fetuswithan pages 1-2) | https://doi.org/10.1002/ajmg.a.20202 (Jul 2003); https://doi.org/10.1097/mcd.0b013e3282fdcc70 (Oct 2008) |
| Maternal SLE / autoimmune embryopathy–associated CDP | Not inherited; maternal autoimmune embryopathy | Suspected vitamin K–related/anticoagulant mechanism | Human clinical embryopathy + review | Wessels includes maternal SLE/lupus embryopathy in the differential and notes it may act through a similar mechanism because some SLE antibodies have anticoagulant activity. | (wessels2003fetuswithan pages 2-3, wessels2003fetuswithan pages 7-8, wessels2003fetuswithan pages 1-2) | https://doi.org/10.1002/ajmg.a.20202 (Jul 2003) |


*Table: This table compares the suspected and established etiologies of tibia-metacarpal chondrodysplasia punctata with other major CDP subtypes and embryopathic mimics. It highlights where CDP-TM remains genetically unresolved and where other CDP entities have clearer molecular or teratogenic mechanisms.*

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No CDP‑TM-specific modifier genes or epigenetic signatures were identified in the retrieved sources. Chromosomal anomalies are discussed as part of the general CDP differential diagnosis (not as a proven cause of CDP‑TM). (irving2008chondrodysplasiapunctataa pages 2-3)

---

## 5. Environmental Information

### 5.1 Environmental/lifestyle/infectious agents
CDP‑TM itself has not been linked to a specific non-genetic exposure in the core CDP‑TM case series, but **CDP phenocopies** are well recognized:
- **Warfarin embryopathy** and **vitamin K deficiency/malabsorption embryopathy** (wessels2003fetuswithan pages 2-3, wessels2003fetuswithan pages 7-8)
- **Hydantoin/phenytoin embryopathy** (wessels2003fetuswithan pages 7-8, wester2002chondrodysplasiapunctata(cdp) pages 2-3)
- **Maternal autoimmune disease (SLE) embryopathy** discussed as potentially anticoagulant/vitamin K–related (wessels2003fetuswithan pages 7-8, wessels2003fetuswithan pages 2-3)

No lifestyle or infectious risk factors were identified for CDP‑TM.

---

## 6. Mechanism / Pathophysiology

### 6.1 Current mechanistic understanding (CDP spectrum; relevance to CDP‑TM)
Across CDP entities, the proximal pathologic event is **abnormal calcium deposition in cartilage during endochondral ossification**, producing radiographic stippling. (irving2008chondrodysplasiapunctataa pages 10-11, patel2023cervicalcorpectomyin pages 1-2)

A key mechanistic framework for many non‑rhizomelic CDP phenotypes is **vitamin K–dependent gamma‑carboxylation of Gla proteins**:
- “**Vit K is a cofactor of vit K carboxylase (gamma-glutamylcarboxylase, GGCX)**” and deficient gamma-carboxylation is stated to be “**most likely… responsible for the skeletal and cartilaginous abnormalities in CDP**.” (wessels2003fetuswithan pages 3-7)
- “**matrix GLA protein (MGP) and bone GLA protein (BGP, osteocalcin)**” are described as inhibitors of cartilage calcification/bone formation; impaired carboxylation plausibly removes this inhibition and permits ectopic calcification. (wessels2003fetuswithan pages 3-7)
- Warfarin is described as inhibiting “**EPHX1 and ARSE**,” and hydantoin toxicity is proposed to act through EPHX1, linking maternal exposures to the same pathway. (wessels2003fetuswithan pages 7-8)

Other causal routes (CDP spectrum) include:
- **Peroxisomal dysfunction** (PEX7) affecting cartilage development (rhizomelic CDP) (wessels2003fetuswithan pages 7-8, jansen2000chondrodysplasiapunctatatibialmetacarpal pages 4-4)
- **Cholesterol biosynthesis defects** (CDPX2 and related entities) (patel2023cervicalcorpectomyin pages 2-3, irving2008chondrodysplasiapunctataa pages 8-10)
- **ARSE-related cartilage sulfate metabolism**, described as an “error of cartilage metabolism in sulfate transport.” (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 4-4)

**CDP‑TM-specific mechanism:** remains **unknown**, but CDP‑TM lies within the non‑rhizomelic CDP spectrum where vitamin K–related phenocopies are emphasized, and CDP‑TM has been repeatedly framed as an “unknown etiology” subtype. (savarirayan2004longtermfollow‐upin pages 5-8, irving2008chondrodysplasiapunctataa pages 10-11)

### 6.2 Causal chain (proposed, evidence-constrained)
A plausible, evidence-constrained chain consistent with the literature is:
1) Upstream perturbation in vitamin K cycle / gamma-carboxylation (genetic defects in GGCX/VKORC1/MGP or maternal warfarin/hydantoin; or ARSE-related pathway for CDPX1)
2) Impaired post-translational modification of mineralization regulators (e.g., MGP/osteocalcin)
3) Loss of inhibition/altered regulation of cartilage mineralization
4) Premature/ectopic cartilage calcification during endochondral ossification
5) Radiographic stippling + dysregulated growth plate architecture → limb shortening and skeletal dysplasia patterns (including tibia–metacarpal patterns) (wessels2003fetuswithan pages 3-7, chitayat2008chondrodysplasiapunctataassociated pages 11-12)

### 6.3 Suggested ontology terms (mechanism)
**GO Biological Process (suggested):** endochondral ossification; cartilage development; extracellular matrix organization; biomineral tissue development; regulation of calcification.

**Cell types (CL suggested):** chondrocyte; hypertrophic chondrocyte; osteoblast.

**Anatomy (UBERON suggested):** growth plate cartilage; tibia; fibula; metacarpal bone; vertebral column; epiphysis.

(These are ontology suggestions based on the described pathology and imaging distribution; the retrieved sources do not provide explicit ontology mappings.) (wessels2003fetuswithan pages 3-7, chitayat2008chondrodysplasiapunctataassociated pages 11-12)

### 6.4 Molecular profiling, models, and functional studies
No CDP‑TM-specific transcriptomic/proteomic/metabolomic signatures or model organism studies were identified in the retrieved sources.

---

## 7. Anatomical Structures Affected

**Primary:** long bones of the lower limb (tibia ± fibula), hands (metacarpals/phalanges), vertebrae, and epiphyseal cartilage (sites of stippling). (rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, savarirayan2004longtermfollow‐upin pages 5-8)

**Secondary/complications:** knees (patellar instability), hips (dysplasia), and spine (cervical/lumbar stenosis with potential cord compression/myelomalacia). (savarirayan2004longtermfollow‐upin pages 1-2, patel2023cervicalcorpectomyin pages 1-2)

---

## 8. Temporal Development

- **Onset:** typically **prenatal/congenital**, detectable on prenatal ultrasound in some cases and on neonatal radiographs. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, wessels2003fetuswithan pages 2-3)
- **Progression/course:** early stippling and some vertebral clefting often **resolve in infancy/early childhood**, but orthopedic issues (joint limitation, patellar dislocation) and spinal stenosis/myelopathy may **emerge later**. (wester2002chondrodysplasiapunctata(cdp) pages 2-3, savarirayan2004longtermfollow‐upin pages 5-8, patel2023cervicalcorpectomyin pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
No population prevalence/incidence estimates for **CDP‑TM specifically** were found in the retrieved sources.

However, available quantitative context includes:
- CDP‑TM has been “described in at least 11 children” (case-based count). (savarirayan2004longtermfollow‐upin pages 1-2)
- For other CDP subtypes (context): CDPX1 estimated prevalence **1 in 500,000** (one report) and RCDP incidence **~1 in 100,000**. (morota2017surgicalmanagementof pages 6-8)

### 9.2 Inheritance pattern
CDP‑TM is generally described as **sporadic** with historical suggestion of **autosomal dominant** inheritance/new mutations, but familial recurrence has been rare/uncertain in the literature cited here. (shukla2015chondrodysplasiapunctatatibia pages 1-2, savarirayan2004longtermfollow‐upin pages 1-2)

No robust data on penetrance, expressivity, sex ratio, founder effects, or carrier frequency were found for CDP‑TM.

---

## 10. Diagnostics

### 10.1 Clinical and imaging diagnosis
Diagnosis relies on **pattern recognition** combining:
- Prenatal ultrasound findings when present (limb shortening, facial hypoplasia, clubfeet, stippling) (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4)
- **Early postnatal skeletal survey** demonstrating stippled epiphyses and the tibia/metacarpal pattern (savarirayan2004longtermfollow‐upin pages 1-2, rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5)

A key clinical lesson is that early radiographs are crucial because stippling can fade, making later retrospective diagnosis difficult. (kaissi2008progressivejointlimitations pages 5-5)

### 10.2 Biochemical and genetic testing strategy
A practical approach is to:
1) **Exclude RCDP/peroxisomal disease** (plasmalogens, VLCFA, phytanic acid; fibroblast studies when needed) (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, irving2008chondrodysplasiapunctataa pages 3-4)
2) **Exclude cholesterol pathway disorders** (sterol profile; gene testing in the appropriate phenotype) (irving2008chondrodysplasiapunctataa pages 2-3)
3) **Consider vitamin K pathway/coagulation studies** and maternal exposure history (warfarin/hydantoin/phenytoin; malabsorption) (irving2008chondrodysplasiapunctataa pages 2-3, wessels2003fetuswithan pages 7-8)
4) Use **NGS panel/exome/genome** for skeletal dysplasia differential diagnosis, acknowledging that CDP‑TM may remain unsolved genetically (unger2023nosologyofgenetic pages 6-8, savarirayan2004longtermfollow‐upin pages 5-8)

### 10.3 Differential diagnosis
Major differentials include RCDP, CDPX1, CDPX2, Keutel syndrome, Binder phenotype, warfarin/hydantoin embryopathy, maternal vitamin K deficiency, maternal autoimmune embryopathy, chromosomal anomalies, and selected storage/metabolic disorders. (wessels2003fetuswithan pages 2-3, irving2008chondrodysplasiapunctataa pages 2-3, mirzaa1993chondrodysplasiapunctata2a pages 9-10)

---

## 11. Outcome / Prognosis

### 11.1 CDP‑TM prognosis
Best available direct evidence is long-term follow-up of three unrelated adults:
- Follow-up durations: **37, 25, and 32 years** (savarirayan2004longtermfollow‐upin pages 1-2)
- Adult heights: **152, 138, and 148 cm** (savarirayan2004longtermfollow‐upin pages 1-2)
- Development/function: “**intellectual function was normal, and physical function was well preserved**.” (savarirayan2004longtermfollow‐upin pages 1-2)
- Morbidities: recurrent patellar dislocation (all), chronic otitis media (two), hip dysplasia (one), lumbar stenosis requiring laminectomy (one). (savarirayan2004longtermfollow‐upin pages 1-2)

### 11.2 Spinal/cervical prognosis and risk
CDP broadly is reported to have cervical spine abnormalities in **~20%–38%** of patients (not CDP‑TM-specific). (patel2023cervicalcorpectomyin pages 1-2)

A 2023 CDP‑TM case demonstrates that cervical disease can be clinically significant in CDP‑TM: an 18‑year‑old with CDP‑TM had dysplastic C4–C5 with kyphosis/retropulsion, cord compression, and myelomalacia, treated with C4–C5 vertebrectomies and C3–C6 anterior fusion with symptom resolution. (patel2023cervicalcorpectomyin pages 1-2, patel2023cervicalcorpectomyin media d3641eed)

---

## 12. Treatment

No disease-modifying pharmacotherapy specific to CDP‑TM was identified in the retrieved literature; management is **supportive and complication-directed**.

### 12.1 Orthopedic and rehabilitative care
Supportive measures described include **physical therapy and hydrotherapy** to maintain hip range of motion and function, and advice such as **restricting weight-bearing/sports** in certain contexts. (kaissi2008progressivejointlimitations pages 2-5)

**MAXO suggestions (non-exhaustive):** physical therapy; orthopedic surgery; spinal decompression; spinal fusion; assistive orthoses.

### 12.2 Neurosurgical management (real-world implementation)
**2017 surgical series (mixed CDP subtypes including 1 CDP‑TM):** among 9 infants/toddlers undergoing cervical surgery (12 operations), approaches included **C1 laminectomy**, **occipitocervical fusion (OCF)** ± **halo fixation**; early intervention was feasible but outcomes depended strongly on preoperative respiratory status. The authors conclude surgical decompression/fusion “generally saves lives and increases the likelihood of motor function recovery.” (morota2017surgicalmanagementof pages 1-2)

**2023 case-based expert synthesis:** no consensus guidelines exist; many authors recommend initial conservative management given operative risks, but surgery is indicated when symptoms correlate with stenosis/instability or when MRI shows new pathological signal; recommended approach depends on CVJ vs subaxial lesion and presence of dysplastic vertebral body. (patel2023cervicalcorpectomyin pages 3-4, patel2023cervicalcorpectomyin pages 4-5)

An imaging example from the 2023 CDP‑TM cervical myelopathy case is available (MRI progression and CT showing dysplastic C4/C5): (patel2023cervicalcorpectomyin media d3641eed).

A structured management summary is provided here:

| Domain | Key points | Evidence (citation ids) | Notes/implementation |
|---|---|---|---|
| Prenatal diagnostics | High-resolution prenatal ultrasound can detect shortened long bones, micrognathia/facial hypoplasia, clubfeet, and abnormal stippling/calcification; prenatal diagnosis is easier in severe/rhizomelic forms but non-rhizomelic/CDP-TM can be missed because stippling may be subtle. | (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 4-4, jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, wessels2003fetuswithan pages 2-3, irving2008chondrodysplasiapunctataa pages 2-3) | Consider referral to fetal medicine, radiology, and clinical genetics when limb shortening plus stippling or Binder-like facies are seen. |
| Postnatal imaging diagnosis | Skeletal survey/radiographs are central: early films show punctate calcifications in sacral, carpal, tarsal, vertebral, tibial, metacarpal, calcaneal, and metatarsal regions, plus short tibiae and short metacarpals. | (kaissi2008progressivejointlimitations pages 5-5, shukla2015chondrodysplasiapunctatatibia pages 1-2, savarirayan2004longtermfollow‐upin pages 1-2, rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5, wester2002chondrodysplasiapunctata(cdp) pages 2-3) | Early-life radiographs are particularly important because stippling may fade in infancy/early childhood, complicating retrospective diagnosis. |
| Targeted biochemical testing | Workup should exclude better-defined CDP mechanisms: peroxisomal studies (plasmalogens, VLCFA, phytanic/pristanic acid, enzyme assays), sterol/cholesterol pathway testing, and vitamin K pathway/coagulation studies when indicated. | (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4, wessels2003fetuswithan pages 2-3, wester2002chondrodysplasiapunctata(cdp) pages 2-3, irving2008chondrodysplasiapunctataa pages 2-3, irving2008chondrodysplasiapunctataa pages 3-4) | In reported CDP-TM cases, peroxisomal and sterol studies were often normal; these tests are used mainly to rule out RCDP, cholesterol disorders, and vitamin K–related embryopathies. |
| Molecular/genetic testing | No causative gene is established for CDP-TM, but genetic testing is still useful to exclude other CDP subtypes (e.g., ARSE/CDPX1, PEX7-related RCDP, cholesterol-pathway disorders) and chromosomal causes. | (savarirayan2004longtermfollow‐upin pages 1-2, savarirayan2004longtermfollow‐upin pages 5-8, patel2023cervicalcorpectomyin pages 2-3, irving2008chondrodysplasiapunctataa pages 2-3, unger2023nosologyofgenetic pages 4-6, unger2023nosologyofgenetic pages 6-8) | Practical approach: phenotype-driven skeletal dysplasia panel or exome/genome sequencing, interpreted with expert radiology and reverse phenotyping. Negative testing does not exclude CDP-TM. |
| Differential diagnosis | Important differentials include RCDP, CDPX1, CDPX2, warfarin embryopathy, hydantoin/phenytoin embryopathy, maternal vitamin K deficiency, maternal SLE/autoimmune embryopathy, chromosomal anomalies, and some lysosomal/storage disorders. | (wessels2003fetuswithan pages 1-2, wessels2003fetuswithan pages 2-3, mirzaa1993chondrodysplasiapunctata2 pages 9-10, mirzaa1993chondrodysplasiapunctata2a pages 9-10, irving2008chondrodysplasiapunctataa pages 2-3) | Maternal drug/exposure history, autoimmune history, coagulation/vitamin K evaluation, and dysmorphology review are clinically important. |
| Longitudinal monitoring | Serial radiographs document fading stippling and skeletal remodeling; long-term follow-up is needed because orthopedic and spinal complications can emerge after infancy even as early calcifications resolve. | (savarirayan2004longtermfollow‐upin pages 1-2, savarirayan2004longtermfollow‐upin pages 5-8, savarirayan2004longtermfollow‐upin pages 8-10) | Monitor growth, limb alignment, patellar stability, hips, gait, and symptoms suggesting spinal stenosis. |
| Spine surveillance | CDP patients are at risk for cervical spine abnormalities; MRI is indicated when there are neurological findings, progressive deformity, or concern for stenosis/myelomalacia. | (patel2023cervicalcorpectomyin pages 1-2, patel2023cervicalcorpectomyin pages 3-4, patel2023cervicalcorpectomyin pages 4-5) | Patel 2023 notes cervical spine abnormalities in about 20%–38% of CDP patients; low threshold for cross-sectional imaging is warranted in symptomatic individuals. |
| Conservative orthopedic management | Supportive treatment includes physical therapy and hydrotherapy to preserve range of motion and function; some reports advise avoiding excessive weight-bearing or sports in patients with joint instability/limb deformity. | (kaissi2008progressivejointlimitations pages 2-5) | Tailor to joint limitation, patellar instability, hip disease, and gait mechanics; ankle-foot orthoses may be used when needed. |
| Orthopedic surgery / complication management | Long-term complications can include recurrent patellar dislocation, hip dysplasia/luxation, genu valgum, and spinal stenosis; some patients require laminectomy or orthopedic procedures. | (savarirayan2004longtermfollow‐upin pages 1-2, kaissi2008progressivejointlimitations pages 5-5, kaissi2008progressivejointlimitations pages 2-5, savarirayan2004longtermfollow‐upin pages 8-10) | Management is individualized and complication-driven rather than disease-specific. |
| Neurosurgical indications | Surgery is considered when clinical symptoms correlate with cervical stenosis/instability, or when MRI shows new pathological cord signal even in minimally symptomatic patients; risks and benefits must be weighed carefully. | (patel2023cervicalcorpectomyin pages 3-4, patel2023cervicalcorpectomyin pages 4-5, morota2017surgicalmanagementof pages 1-2) | Preoperative respiratory status and overall condition strongly influence outcomes. |
| Neurosurgical approaches | Reported approaches include C1 laminectomy, occipitocervical fusion, halo fixation for CVJ lesions, posterior decompression for selected stable lesions, and anterior decompression/fusion or corpectomy for dysplastic subaxial vertebral body disease. | (morota2017surgicalmanagementof pages 1-2, patel2023cervicalcorpectomyin pages 3-4, patel2023cervicalcorpectomyin pages 1-2, patel2023cervicalcorpectomyin pages 2-3) | Long-term follow-up is essential because deformity progression and reoperation are common; combined stabilization strategies may be required in complex cases. |
| Multidisciplinary care | Optimal care requires coordination among genetics, radiology, orthopedics, neurosurgery, rehabilitation, and primary pediatrics/adult medicine. | (morota2017surgicalmanagementof pages 1-2, patel2023cervicalcorpectomyin pages 1-2, unger2023nosologyofgenetic pages 4-6, unger2023nosologyofgenetic pages 6-8) | Rare-disease management benefits from specialized skeletal dysplasia expertise and shared interpretation of imaging plus genomic data. |
| Genetic counseling | Counseling should explain that CDP-TM is very rare and genetically unresolved, usually sporadic, historically considered possibly autosomal dominant, with rare familial recurrence reports; recurrence risk is therefore uncertain. | (shukla2015chondrodysplasiapunctatatibia pages 1-2, savarirayan2004longtermfollow‐upin pages 1-2, wester2002chondrodysplasiapunctata(cdp) pages 2-3) | Review family history, discuss uncertainty around inheritance, and consider prenatal imaging/genetic evaluation in future pregnancies when prior affected pregnancy or child exists. |


*Table: This table summarizes practical diagnostic, monitoring, orthopedic, neurosurgical, and counseling considerations for chondrodysplasia punctata, with emphasis on the tibia-metacarpal subtype. It is useful as a concise implementation-oriented guide because direct CDP-TM-specific management literature is sparse and often extrapolated from broader CDP experience.*

---

## 13. Prevention

Primary prevention for genetic CDP‑TM is not established because the causal gene is unknown. Prevention considerations apply mainly to **phenocopies**:
- Avoid **warfarin** exposure in pregnancy when possible; review maternal medication and vitamin K status (general CDP differential context). (wessels2003fetuswithan pages 2-3, irving2008chondrodysplasiapunctataa pages 2-3)
- Manage maternal conditions associated with fetal vitamin K deficiency/malabsorption and consider teratogen counseling. (wessels2003fetuswithan pages 7-8)

Prenatal detection via ultrasound and targeted biochemical/genetic evaluation is a form of secondary prevention (early identification and counseling), especially when a prior affected pregnancy/child exists. (wessels2003fetuswithan pages 2-3, jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4)

---

## 14. Other Species / Natural Disease

No naturally occurring CDP‑TM analogs in other species were identified in the retrieved sources.

---

## 15. Model Organisms

No CDP‑TM-specific model organism or cellular model evidence was identified in the retrieved sources.

---

## 2023–2024 developments and latest research (prioritized)

1) **Cervical spine management in CDP‑TM (2023):** A CDP‑TM adolescent with progressive cervical kyphosis and myelomalacia underwent anterior corpectomy/fusion with symptom resolution, and the authors emphasize CDP cervical abnormalities (20–38%) and lack of consensus guidelines, advocating individualized management and long-term follow-up. (Patel et al., published Nov 20, 2023; https://doi.org/10.3171/CASE23302) (patel2023cervicalcorpectomyin pages 1-2, patel2023cervicalcorpectomyin pages 4-5)

2) **Skeletal dysplasia nosology and NGS-era diagnostics (2023):** The 2023 Nosology revision reports expansion from **461 to 771 disorders** and **437 to 552 genes**, and highlights clinical utility for targeted panels and exome/genome interpretation (reverse phenotyping), which is relevant for unsolved entities like CDP‑TM. (Unger et al., Feb 2023; https://doi.org/10.1002/ajmg.a.63132) (unger2023nosologyofgenetic pages 6-8)

3) **2024 CDP multidisciplinary care and NGS in related subtype CDPX2:** A 2024 case report of Conradi–Hünermann–Happle syndrome (CDPX2) illustrates real-world implementation of WES/NGS skeletal dysplasia panels and multidisciplinary management; while not CDP‑TM, it exemplifies current practice trends applicable to CDP differential diagnosis workups. ()

(Direct 2023–2024 molecular discovery papers specifically resolving CDP‑TM were not identified in the retrieved evidence.)

---

## Key statistics and data extracted from recent/seminal studies
- CDP‑TM adult heights in long-term follow-up (n=3): **152, 138, 148 cm**; follow-up **37, 25, 32 years** (savarirayan2004longtermfollow‐upin pages 1-2).
- CDP cervical spine abnormalities (CDP overall): **~20%–38%** (patel2023cervicalcorpectomyin pages 1-2).
- CDPX1 prevalence estimate (context): **~1 in 500,000**; RCDP incidence (context): **~1 in 100,000** (morota2017surgicalmanagementof pages 6-8).
- Prenatal CDPX1 case series (context, not CDP‑TM): nasal hypoplasia 55%, stippling 41%, polyhydramnios 32%, shortened long bones 23% (broerenUnknownyearstoer pages 3-3).

---

## Expert opinions / authoritative synthesis (evidence-linked)
- CDP is explicitly described as “genetically heterogeneous” and characterized by “aberrant deposition of calcium (stippled epiphyses)” in endochondral bone formation, supporting a unifying pathophysiologic endpoint despite diverse upstream causes. (morota2017surgicalmanagementof pages 1-2)
- Vitamin K–dependent gamma-carboxylation of Gla proteins is presented as a mechanistic explanation for multiple non-rhizomelic CDP entities and phenocopies; Wessels explicitly states deficient gamma-carboxylation is “most likely” responsible for skeletal/cartilaginous abnormalities in CDP. (wessels2003fetuswithan pages 3-7)

---

## Figure evidence (cervical spine disease in CDP‑TM)
The 2023 CDP‑TM cervical myelopathy case includes MRI/CT evidence of progressive kyphosis and spinal cord myelomalacia with dysplastic C4–C5 vertebrae (Figure 1). (patel2023cervicalcorpectomyin media d3641eed)

---

## Limitations and evidence gaps
- **No MONDO/Orphanet/ICD/MeSH** identifiers for CDP‑TM were present in retrieved full texts; database lookups were not available within this tool-only evidence set.
- **No confirmed causal gene/variant spectrum** exists in these retrieved sources for CDP‑TM; thus ClinVar/gnomAD statistics and ACMG variant classifications cannot be provided for CDP‑TM.
- **No trials** and no disease-modifying therapies were identified for CDP‑TM.
- **QoL metrics** and population epidemiology for CDP‑TM are not available in the retrieved literature.



References

1. (patel2023cervicalcorpectomyin pages 1-2): Nirali P Patel, Mark W Youngblood, Melissa A LoPresti, and Tord D Alden. Cervical corpectomy in a pediatric patient with chondrodysplasia punctata and c5 dysplasia with spinal cord compression: illustrative case. Journal of Neurosurgery: Case Lessons, Nov 2023. URL: https://doi.org/10.3171/case23302, doi:10.3171/case23302. This article has 1 citations.

2. (unger2023nosologyofgenetic pages 4-6): Sheila Unger, Carlos R. Ferreira, Geert R. Mortier, Houda Ali, Débora R. Bertola, Alistair Calder, Daniel H. Cohn, Valerie Cormier‐Daire, Katta M. Girisha, Christine Hall, Deborah Krakow, Outi Makitie, Stefan Mundlos, Gen Nishimura, Stephen P. Robertson, Ravi Savarirayan, David Sillence, Marleen Simon, V. Reid Sutton, Matthew L. Warman, and Andrea Superti‐Furga. Nosology of genetic skeletal disorders: 2023 revision. American Journal of Medical Genetics Part A, 191:1164-1209, Feb 2023. URL: https://doi.org/10.1002/ajmg.a.63132, doi:10.1002/ajmg.a.63132. This article has 474 citations.

3. (unger2023nosologyofgenetic pages 6-8): Sheila Unger, Carlos R. Ferreira, Geert R. Mortier, Houda Ali, Débora R. Bertola, Alistair Calder, Daniel H. Cohn, Valerie Cormier‐Daire, Katta M. Girisha, Christine Hall, Deborah Krakow, Outi Makitie, Stefan Mundlos, Gen Nishimura, Stephen P. Robertson, Ravi Savarirayan, David Sillence, Marleen Simon, V. Reid Sutton, Matthew L. Warman, and Andrea Superti‐Furga. Nosology of genetic skeletal disorders: 2023 revision. American Journal of Medical Genetics Part A, 191:1164-1209, Feb 2023. URL: https://doi.org/10.1002/ajmg.a.63132, doi:10.1002/ajmg.a.63132. This article has 474 citations.

4. (rittler1990chondrodysplasiapunctatatibiametacarpal pages 3-5): M. Rittler, H. Menger, and J. W. Spranger. Chondrodysplasia punctata, tibia-metacarpal (mt) type. American journal of medical genetics, 37 2:200-8, Oct 1990. URL: https://doi.org/10.1002/ajmg.1320370208, doi:10.1002/ajmg.1320370208. This article has 44 citations.

5. (savarirayan2004longtermfollow‐upin pages 1-2): Ravi Savarirayan, Robert J. Boyle, John Masel, John G. Rogers, and Leslie J. Sheffield. Longterm follow‐up in chondrodysplasia punctata, tibia–metacarpal type, demonstrating natural history. American Journal of Medical Genetics Part A, 124A:148-157, Jan 2004. URL: https://doi.org/10.1002/ajmg.a.20383, doi:10.1002/ajmg.a.20383. This article has 20 citations.

6. (savarirayan2004longtermfollow‐upin pages 5-8): Ravi Savarirayan, Robert J. Boyle, John Masel, John G. Rogers, and Leslie J. Sheffield. Longterm follow‐up in chondrodysplasia punctata, tibia–metacarpal type, demonstrating natural history. American Journal of Medical Genetics Part A, 124A:148-157, Jan 2004. URL: https://doi.org/10.1002/ajmg.a.20383, doi:10.1002/ajmg.a.20383. This article has 20 citations.

7. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 1-4): V Jansen, K Sarafoglou, A Rebarber, A Greco, N B Genieser, and R Wallerstein. Chondrodysplasia punctata, tibial-metacarpal type in a 16 week fetus. Journal of Ultrasound in Medicine, 19:719-722, Oct 2000. URL: https://doi.org/10.7863/jum.2000.19.10.719, doi:10.7863/jum.2000.19.10.719. This article has 7 citations and is from a peer-reviewed journal.

8. (wester2002chondrodysplasiapunctata(cdp) pages 2-3): Ulrika Wester, G. Brandberg, M. Larsson, T. Lönnerholm, and G. Annéren. Chondrodysplasia punctata (cdp) with features of the tibia‐metacarpal type and maternal phenytoin treatment during pregnancy. Prenatal Diagnosis, 22:663-668, Aug 2002. URL: https://doi.org/10.1002/pd.352, doi:10.1002/pd.352. This article has 12 citations and is from a peer-reviewed journal.

9. (kaissi2008progressivejointlimitations pages 2-5): Ali Al Kaissi, Klaus Klaushofer, and Franz Grill. Progressive joint limitations as the first alarming signs in a boy with short – limbed dwarfism: a case report. Cases Journal, 1:112-112, Aug 2008. URL: https://doi.org/10.1186/1757-1626-1-112, doi:10.1186/1757-1626-1-112. This article has 2 citations.

10. (shukla2015chondrodysplasiapunctatatibia pages 1-2): Anju Shukla and Shubha R. Phadke. Chondrodysplasia punctata tibia metacarpal type: report of a 1.5 year old child with severe short stature and extensive calcific stippling. Clinical Dysmorphology, 24:118–121, Jul 2015. URL: https://doi.org/10.1097/mcd.0000000000000076, doi:10.1097/mcd.0000000000000076. This article has 4 citations and is from a peer-reviewed journal.

11. (wessels2003fetuswithan pages 2-2): Marja W. Wessels, Nicolette J. Den Hollander, Ronald R. De Krijger, Peter G.J. Nikkels, Helen Brandenburg, Raoul Hennekam, and Patrick J. Willems. Fetus with an unusual form of nonrhizomelic chondrodysplasia punctata: case report and review. American Journal of Medical Genetics Part A, 120A:97-104, Jul 2003. URL: https://doi.org/10.1002/ajmg.a.20202, doi:10.1002/ajmg.a.20202. This article has 22 citations.

12. (kaissi2008progressivejointlimitations pages 5-5): Ali Al Kaissi, Klaus Klaushofer, and Franz Grill. Progressive joint limitations as the first alarming signs in a boy with short – limbed dwarfism: a case report. Cases Journal, 1:112-112, Aug 2008. URL: https://doi.org/10.1186/1757-1626-1-112, doi:10.1186/1757-1626-1-112. This article has 2 citations.

13. (kozłowski2006retrospectivediagnosisof pages 1-4): K. Kozłowski, D. Basel, and P. Beighton. Retrospective diagnosis of chondrodysplasia punctata. Australasian radiology, 50 1:55-8, Feb 2006. URL: https://doi.org/10.1111/j.1440-1673.2005.01531.x, doi:10.1111/j.1440-1673.2005.01531.x. This article has 0 citations.

14. (wessels2003fetuswithan pages 1-2): Marja W. Wessels, Nicolette J. Den Hollander, Ronald R. De Krijger, Peter G.J. Nikkels, Helen Brandenburg, Raoul Hennekam, and Patrick J. Willems. Fetus with an unusual form of nonrhizomelic chondrodysplasia punctata: case report and review. American Journal of Medical Genetics Part A, 120A:97-104, Jul 2003. URL: https://doi.org/10.1002/ajmg.a.20202, doi:10.1002/ajmg.a.20202. This article has 22 citations.

15. (wessels2003fetuswithan pages 3-7): Marja W. Wessels, Nicolette J. Den Hollander, Ronald R. De Krijger, Peter G.J. Nikkels, Helen Brandenburg, Raoul Hennekam, and Patrick J. Willems. Fetus with an unusual form of nonrhizomelic chondrodysplasia punctata: case report and review. American Journal of Medical Genetics Part A, 120A:97-104, Jul 2003. URL: https://doi.org/10.1002/ajmg.a.20202, doi:10.1002/ajmg.a.20202. This article has 22 citations.

16. (morota2017surgicalmanagementof pages 1-2): Nobuhito Morota, Satoshi Ihara, Hideki Ogiwara, and Goichiro Tamura. Surgical management of cervical spine deformity in chondrodysplasia punctata. Journal of Neurosurgery: Pediatrics, 20:378-387, Oct 2017. URL: https://doi.org/10.3171/2017.5.peds16554, doi:10.3171/2017.5.peds16554. This article has 14 citations and is from a peer-reviewed journal.

17. (jansen2000chondrodysplasiapunctatatibialmetacarpal pages 4-4): V Jansen, K Sarafoglou, A Rebarber, A Greco, N B Genieser, and R Wallerstein. Chondrodysplasia punctata, tibial-metacarpal type in a 16 week fetus. Journal of Ultrasound in Medicine, 19:719-722, Oct 2000. URL: https://doi.org/10.7863/jum.2000.19.10.719, doi:10.7863/jum.2000.19.10.719. This article has 7 citations and is from a peer-reviewed journal.

18. (irving2008chondrodysplasiapunctataa pages 2-3): Melita D. Irving, Lyn S. Chitty, Sahar Mansour, and Christine M. Hall. Chondrodysplasia punctata: a clinical diagnostic and radiological review. Clinical Dysmorphology, 17:229-241, Oct 2008. URL: https://doi.org/10.1097/mcd.0b013e3282fdcc70, doi:10.1097/mcd.0b013e3282fdcc70. This article has 121 citations and is from a peer-reviewed journal.

19. (wessels2003fetuswithan pages 7-8): Marja W. Wessels, Nicolette J. Den Hollander, Ronald R. De Krijger, Peter G.J. Nikkels, Helen Brandenburg, Raoul Hennekam, and Patrick J. Willems. Fetus with an unusual form of nonrhizomelic chondrodysplasia punctata: case report and review. American Journal of Medical Genetics Part A, 120A:97-104, Jul 2003. URL: https://doi.org/10.1002/ajmg.a.20202, doi:10.1002/ajmg.a.20202. This article has 22 citations.

20. (irving2008chondrodysplasiapunctataa pages 10-11): Melita D. Irving, Lyn S. Chitty, Sahar Mansour, and Christine M. Hall. Chondrodysplasia punctata: a clinical diagnostic and radiological review. Clinical Dysmorphology, 17:229-241, Oct 2008. URL: https://doi.org/10.1097/mcd.0b013e3282fdcc70, doi:10.1097/mcd.0b013e3282fdcc70. This article has 121 citations and is from a peer-reviewed journal.

21. (shukla2015chondrodysplasiapunctatatibia pages 2-4): Anju Shukla and Shubha R. Phadke. Chondrodysplasia punctata tibia metacarpal type: report of a 1.5 year old child with severe short stature and extensive calcific stippling. Clinical Dysmorphology, 24:118–121, Jul 2015. URL: https://doi.org/10.1097/mcd.0000000000000076, doi:10.1097/mcd.0000000000000076. This article has 4 citations and is from a peer-reviewed journal.

22. (patel2023cervicalcorpectomyin media d3641eed): Nirali P Patel, Mark W Youngblood, Melissa A LoPresti, and Tord D Alden. Cervical corpectomy in a pediatric patient with chondrodysplasia punctata and c5 dysplasia with spinal cord compression: illustrative case. Journal of Neurosurgery: Case Lessons, Nov 2023. URL: https://doi.org/10.3171/case23302, doi:10.3171/case23302. This article has 1 citations.

23. (patel2023cervicalcorpectomyin pages 2-3): Nirali P Patel, Mark W Youngblood, Melissa A LoPresti, and Tord D Alden. Cervical corpectomy in a pediatric patient with chondrodysplasia punctata and c5 dysplasia with spinal cord compression: illustrative case. Journal of Neurosurgery: Case Lessons, Nov 2023. URL: https://doi.org/10.3171/case23302, doi:10.3171/case23302. This article has 1 citations.

24. (wessels2003fetuswithan pages 2-3): Marja W. Wessels, Nicolette J. Den Hollander, Ronald R. De Krijger, Peter G.J. Nikkels, Helen Brandenburg, Raoul Hennekam, and Patrick J. Willems. Fetus with an unusual form of nonrhizomelic chondrodysplasia punctata: case report and review. American Journal of Medical Genetics Part A, 120A:97-104, Jul 2003. URL: https://doi.org/10.1002/ajmg.a.20202, doi:10.1002/ajmg.a.20202. This article has 22 citations.

25. (morota2017surgicalmanagementof pages 6-8): Nobuhito Morota, Satoshi Ihara, Hideki Ogiwara, and Goichiro Tamura. Surgical management of cervical spine deformity in chondrodysplasia punctata. Journal of Neurosurgery: Pediatrics, 20:378-387, Oct 2017. URL: https://doi.org/10.3171/2017.5.peds16554, doi:10.3171/2017.5.peds16554. This article has 14 citations and is from a peer-reviewed journal.

26. (irving2008chondrodysplasiapunctataa pages 3-4): Melita D. Irving, Lyn S. Chitty, Sahar Mansour, and Christine M. Hall. Chondrodysplasia punctata: a clinical diagnostic and radiological review. Clinical Dysmorphology, 17:229-241, Oct 2008. URL: https://doi.org/10.1097/mcd.0b013e3282fdcc70, doi:10.1097/mcd.0b013e3282fdcc70. This article has 121 citations and is from a peer-reviewed journal.

27. (irving2008chondrodysplasiapunctataa pages 8-10): Melita D. Irving, Lyn S. Chitty, Sahar Mansour, and Christine M. Hall. Chondrodysplasia punctata: a clinical diagnostic and radiological review. Clinical Dysmorphology, 17:229-241, Oct 2008. URL: https://doi.org/10.1097/mcd.0b013e3282fdcc70, doi:10.1097/mcd.0b013e3282fdcc70. This article has 121 citations and is from a peer-reviewed journal.

28. (chitayat2008chondrodysplasiapunctataassociated pages 11-12): David Chitayat, Sarah Keating, Dina J. Zand, Teresa Costa, Elaine H. Zackai, Earl Silverman, George Tiller, Sheila Unger, Stephen Miller, John Kingdom, Ants Toi, and Cynthia J.R. Curry. Chondrodysplasia punctata associated with maternal autoimmune diseases: expanding the spectrum from systemic lupus erythematosus (sle) to mixed connective tissue disease (mctd) and scleroderma report of eight cases. American Journal of Medical Genetics Part A, 146A:3038-3053, Dec 2008. URL: https://doi.org/10.1002/ajmg.a.32554, doi:10.1002/ajmg.a.32554. This article has 44 citations.

29. (mirzaa1993chondrodysplasiapunctata2a pages 9-10): GM Mirzaa. Chondrodysplasia punctata 2, x-linked. Unknown journal, 1993.

30. (patel2023cervicalcorpectomyin pages 3-4): Nirali P Patel, Mark W Youngblood, Melissa A LoPresti, and Tord D Alden. Cervical corpectomy in a pediatric patient with chondrodysplasia punctata and c5 dysplasia with spinal cord compression: illustrative case. Journal of Neurosurgery: Case Lessons, Nov 2023. URL: https://doi.org/10.3171/case23302, doi:10.3171/case23302. This article has 1 citations.

31. (patel2023cervicalcorpectomyin pages 4-5): Nirali P Patel, Mark W Youngblood, Melissa A LoPresti, and Tord D Alden. Cervical corpectomy in a pediatric patient with chondrodysplasia punctata and c5 dysplasia with spinal cord compression: illustrative case. Journal of Neurosurgery: Case Lessons, Nov 2023. URL: https://doi.org/10.3171/case23302, doi:10.3171/case23302. This article has 1 citations.

32. (mirzaa1993chondrodysplasiapunctata2 pages 9-10): GM Mirzaa. Chondrodysplasia punctata 2, x-linked. Unknown journal, 1993.

33. (savarirayan2004longtermfollow‐upin pages 8-10): Ravi Savarirayan, Robert J. Boyle, John Masel, John G. Rogers, and Leslie J. Sheffield. Longterm follow‐up in chondrodysplasia punctata, tibia–metacarpal type, demonstrating natural history. American Journal of Medical Genetics Part A, 124A:148-157, Jan 2004. URL: https://doi.org/10.1002/ajmg.a.20383, doi:10.1002/ajmg.a.20383. This article has 20 citations.

34. (broerenUnknownyearstoer pages 3-3): E Broeren. Sto er. Unknown journal, Unknown year.