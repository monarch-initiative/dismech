---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T16:11:10.237879'
end_time: '2026-05-08T16:34:19.918654'
duration_seconds: 1389.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Epidermolysis Bullosa Simplex
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
- **Disease Name:** Epidermolysis Bullosa Simplex
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Epidermolysis Bullosa Simplex** covering all of the
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
- **Disease Name:** Epidermolysis Bullosa Simplex
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Epidermolysis Bullosa Simplex** covering all of the
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


# Comprehensive Disease Characteristics Report: Epidermolysis Bullosa Simplex (EBS)

## Executive summary
Epidermolysis bullosa simplex (EBS) is a Mendelian skin-fragility disorder within the inherited epidermolysis bullosa (EB) spectrum, defined by intraepidermal blistering due to cleavage within the basal layer of keratinocytes, typically triggered by minor mechanical trauma. (Has et al., *Br J Dermatol*, 2020-03, https://doi.org/10.1111/bjd.18921) (has2020consensusreclassificationof pages 2-3). The current (international consensus) classification organizes EB into four major types—EBS, junctional EB, dystrophic EB, and Kindler EB—based primarily on level of cleavage and molecular etiology. (Has et al., 2020-03, https://doi.org/10.1111/bjd.18921) (has2020consensusreclassificationof pages 1-2).

Key 2023–2024 advances emphasized in recent reviews include (i) a more explicit framing of EBS as both a mechanical fragility disorder and a disease with inflammatory/stress-response signaling cascades downstream of keratin disruption, and (ii) continued growth of symptom-targeted therapies through drug repurposing and targeted topical approaches. (Bchetnia et al., *Int J Mol Sci*, 2024-08, https://doi.org/10.3390/ijms25179495) (bchetnia2024pathologicalmechanismsinvolved pages 1-2).

---

## 1. Disease information

### 1.1 What is the disease?
EBS is an inherited mechanobullous (mechanically induced blistering) genodermatosis characterized by skin fragility with blistering/erosions after minor trauma, with tissue cleavage occurring within the basal keratinocyte layer of the epidermis (intraepidermal). (Has et al., 2020-03, https://doi.org/10.1111/bjd.18921) (has2020consensusreclassificationof pages 2-3). A 2024 EBS-focused review similarly defines EBS as “recurrent blister formation within the basal layer of the epidermis,” most often due to dominant keratin 5/14 mutations. (Bchetnia et al., 2024-08, https://doi.org/10.3390/ijms25179495) (bchetnia2024pathologicalmechanismsinvolved pages 1-2).

### 1.2 Key identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH, MONDO)
**Not available from the retrieved evidence snippets.** The sources available in this run did not provide explicit OMIM, Orphanet, ICD-10/ICD-11, MeSH, or MONDO identifiers for EBS. (has2020consensusreclassificationof pages 2-3, bchetnia2024pathologicalmechanismsinvolved pages 1-2, has2019clinicalpracticeguidelines pages 1-2).

### 1.3 Common synonyms / alternative names
Common clinical subtype names used in the contemporary literature include:
- **Localized EBS** (historical eponym: Weber–Cockayne)
- **Intermediate generalized EBS** (historical eponym: Köebner)
- **Severe generalized EBS** (historical eponym: Dowling–Meara)
(Has et al., 2020-03, https://doi.org/10.1111/bjd.18921) (has2020consensusreclassificationof pages 2-3).

### 1.4 Evidence source type
The evidence synthesized here is primarily from aggregated disease-level resources and cohorts/registries (consensus classification, clinical practice guidelines, epidemiology capture–recapture study, multi-country patient-reported outcomes survey), complemented by clinical-trial registry records and mechanistic review literature. (has2020consensusreclassificationof pages 1-2, has2019clinicalpracticeguidelines pages 1-2, has2023epidemiologyofinherited pages 7-7, so2022aglobalcrosssectional pages 1-2, NCT02470689 chunk 1).

---

## 2. Etiology

### 2.1 Disease causal factors
**Genetic (primary):** EBS most often results from **autosomal dominant** pathogenic variants in **KRT5** or **KRT14** encoding keratin 5 and keratin 14 intermediate filament proteins in basal keratinocytes. (Bchetnia et al., 2024-08, https://doi.org/10.3390/ijms25179495) (bchetnia2024pathologicalmechanismsinvolved pages 1-2). The 2020 international consensus explicitly frames EBS as blistering from cleavage within basal keratinocytes and notes multiple EBS-associated genes beyond keratins, including newer additions such as **KLHL24**. (Has et al., 2020-03, https://doi.org/10.1111/bjd.18921) (has2020consensusreclassificationof pages 2-3).

**Additional (rarer) EBS genes (examples):** **PLEC, KLHL24, DST, EXPH5, CD151**. (Bchetnia et al., 2024-08, https://doi.org/10.3390/ijms25179495) (bchetnia2024pathologicalmechanismsinvolved pages 1-2).

### 2.2 Risk factors
- **Genetic risk factor:** carrying a pathogenic variant in a causal EBS gene (e.g., KRT5/KRT14). (bchetnia2024pathologicalmechanismsinvolved pages 1-2)
- **De novo and mosaic mutations:** In a large China cohort, de novo mutations were reported as common in EBS (63.8%), and mosaicism was observed (~5.4% in dominant EBS), highlighting that absence of family history does not exclude EBS. (Chen et al., *JEADV*, 2023-11, https://doi.org/10.1111/jdv.18692) (chen2023genotypeandphenotype pages 1-1).

**Environmental/triggering factors (non-causal but exacerbating):** mechanical friction/trauma is the key trigger for blister formation in EB generally and EBS specifically. (Has et al., 2020-03, https://doi.org/10.1111/bjd.18921) (has2020consensusreclassificationof pages 1-2).

### 2.3 Protective factors
No validated protective genetic or environmental factors were identified in the retrieved evidence excerpts.

### 2.4 Gene–environment interactions
The retrieved evidence supports a strong mechanical trigger (friction) interacting with genetically determined structural fragility, but does not provide quantitative gene–environment interaction effect sizes.

---

## 3. Phenotypes

### 3.1 Phenotype spectrum and subtype distribution
EBS is commonly divided into **localized**, **intermediate generalized**, and **severe generalized** forms. (Has et al., 2020-03) (has2020consensusreclassificationof pages 2-3).

Population-based and cohort data show subtype distributions vary by region and ascertainment:
- **Germany (capture–recapture, inherited EB):** EBS subtypes most commonly **localized (39.5%)** and **severe (14.7%)**, with **33.4%** of EBS not further subclassified. (Has et al., *JEADV*, 2023-11, https://doi.org/10.1111/jdv.18637) (has2023epidemiologyofinherited pages 5-6).
- **China (441 EB patients):** EBS comprised ~23.4% of the EB cohort; among EBS cases, **localized 17.5%**, **intermediate 35.0%**, **severe 27.2%**. (Chen et al., 2023-11, https://doi.org/10.1111/jdv.18692) (chen2023genotypeandphenotype pages 2-2).

### 3.2 Common clinical manifestations (patient-reported)
In the largest international cross-sectional EBS patient-reported outcomes survey (n=214; mean age 32.8 years), respondents reported: **blisters 93%**, **recurrent wounds 89%**, **pain 74%**, **chronic wounds 59%**, **itch 55%**, and **difficulty walking 44%**; the **mean QOLEB score was 14.7 (SD 7.5)** indicating a **moderate** impact on quality of life, and **12% reported regular opiate use**. (So et al., *Orphanet J Rare Dis*, 2022-07, https://doi.org/10.1186/s13023-022-02433-3) (so2022aglobalcrosssectional pages 1-2).

More granular QOLEB impacts among those completing all items (70/214): **41% reported frequent/constant pain**, **93% unable to participate in sports**, **79% difficulty moving outside the home**, and high emotional burden (frustration 99%, anxiety 70%, depression 54%). (So et al., 2022-07) (so2022aglobalcrosssectional pages 6-8).

### 3.3 Quality of life impact
QOL impact is measurable and moderate on average in the survey above (QOLEB mean 14.7), with substantial mobility limitations and psychosocial effects. (so2022aglobalcrosssectional pages 6-8).

### 3.4 Suggested HPO terms (examples; not exhaustive)
Based on the phenotype descriptions in the cited studies, suitable HPO terms include:
- Skin blistering: **HP:0008064** (Blistering of the skin)
- Skin fragility: **HP:0001034** (Fragile skin)
- Erosions/ulcerations: **HP:0001058** (Skin erosion) / **HP:0000974** (Skin ulcer)
- Pain: **HP:0012531** (Pain)
- Pruritus: **HP:0000989** (Pruritus)
- Difficulty walking / impaired mobility: **HP:0002355** (Difficulty walking)
- Palmoplantar keratoderma (for localized plantar disease): **HP:0000972** (Palmoplantar keratoderma)

---

## 4. Genetic / molecular information

### 4.1 Causal genes (major)
- **KRT5** and **KRT14** are the predominant genes for dominant EBS. (bchetnia2024pathologicalmechanismsinvolved pages 1-2)

Cohort support:
- In a Middle Eastern EB cohort (n=151), EBS was **64% (97/151)**; within EBS cases, **KRT5 accounted for 46% (45/97)** and **KRT14 for 43% (42/97)**. (Bergson et al., *Pediatr Dermatol*, 2023-10, https://doi.org/10.1111/pde.15440) (bergson2023clinicalandmolecular pages 1-2).

### 4.2 Other reported EBS genes
Rarer EBS-associated genes cited in the recent EBS review and consensus classification include **PLEC, KLHL24, DST, EXPH5, CD151**. (bchetnia2024pathologicalmechanismsinvolved pages 1-2, has2020consensusreclassificationof pages 2-3).

In the China cohort, **PLEC and KLHL24** variants were each found in **four cases** (cohort-wide). (chen2023genotypeandphenotype pages 3-3).

### 4.3 Pathogenic variant types and genotype–phenotype considerations
- The China cohort highlights recurrent keratin hotspots and domain clustering, including classic **KRT14 p.Arg125 substitutions** (e.g., p.R125H/C/S/L) and variants in keratin α-helical domains (1A/1B/2A/2B) and linkers. (chen2023genotypeandphenotype pages 4-4).
- The Middle Eastern cohort reported a phenotype association: **truncal involvement was more common in KRT14-associated EBS than KRT5-associated EBS** (p<0.05). (bergson2023clinicalandmolecular pages 1-2).

**Somatic vs germline:** Mosaicism in dominant EBS was reported (~5.4% in one large cohort), supporting consideration of mosaicism in genetic testing/interpretation. (chen2023genotypeandphenotype pages 1-1).

### 4.4 Suggested ontology/annotation terms
- **GO biological processes (examples):** keratinocyte differentiation; response to mechanical stimulus; inflammatory response; cellular response to endoplasmic reticulum stress.
- **Cell types (Cell Ontology, examples):** basal keratinocyte (epidermal basal cell); epidermal keratinocyte.

---

## 5. Environmental information
EBS is not infectious; its primary cause is genetic. Mechanical trauma/friction is the canonical trigger for blistering in EB. (has2020consensusreclassificationof pages 1-2). No specific toxins, lifestyle exposures, or pathogens were identified in the retrieved evidence as causal contributors.

---

## 6. Mechanism / pathophysiology (current understanding, 2023–2024 emphasis)

### 6.1 Core causal chain (structural fragility)
1) **Primary trigger:** pathogenic variants (often dominant) in KRT5 or KRT14.
2) **Cellular consequence:** disruption of the basal keratin intermediate filament network, with keratin aggregation and cytoskeletal instability.
3) **Tissue consequence:** basal keratinocyte fragility leading to intraepidermal cleavage and blistering with minor trauma.
(Bchetnia et al., 2024-08) (bchetnia2024pathologicalmechanismsinvolved pages 1-2).

### 6.2 Inflammatory/stress signaling cascades (important recent framing)
A key 2024 EBS review emphasizes that disruptive KRT5/KRT14 mutations “will not only structurally impair the cytoskeleton, but it will also activate a cascade of biochemical mechanisms,” including ER stress and release of pro-inflammatory molecules. (Bchetnia et al., 2024-08) (bchetnia2024pathologicalmechanismsinvolved pages 1-2).

Clinical-trial rationale (Dowling–Meara/generalized severe subtype) highlights an IL-1β/JNK axis: upregulation of **interleukin-1β (IL-1β)** and activation of the **JNK stress pathway**, with in vitro data that blocking IL‑1β or applying **diacerein** reduced IL‑1β and K14 expression and improved keratinocyte stress resistance. (ClinicalTrials.gov record NCT02470689; 2015; https://clinicaltrials.gov/study/NCT02470689) (NCT02470689 chunk 1).

### 6.3 Transcriptomics / molecular profiling
The 2024 mechanistic review states that multiple gene expression studies in mouse models and human keratinocytes identify EBS gene expression signatures involving immunological mediators, keratins, and junction components, with particular emphasis on **inflammation** as a functional biological process. (bchetnia2024pathologicalmechanismsinvolved pages 1-2).

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level
- Primary affected tissue: **skin (epidermis)** with basal-layer keratinocyte cleavage. (has2020consensusreclassificationof pages 2-3)
- Mucosal involvement can occur (particularly in more severe generalized forms) within the broader EB spectrum. (Rosa et al., *Cold Spring Harb Perspect Biol*, 2023-09, https://doi.org/10.1101/cshperspect.a041229) (rosa2023stairwaystoadvanced pages 1-3).

### 7.2 Suggested UBERON terms (examples)
- Skin: **UBERON:0002097**
- Epidermis: **UBERON:0001003**

### 7.3 Suggested GO cellular component terms (examples)
- Intermediate filament cytoskeleton; keratin filament.

---

## 8. Temporal development (onset and progression)
Severe EBS forms can present at or near birth and may be associated with severe complications; milder localized forms may be recognized later and can be underdiagnosed. (Has et al., 2020-03) (has2020consensusreclassificationof pages 2-3). In Germany, EBS incidence was noted as potentially underestimated due to later diagnosis/missed diagnosis. (Has et al., 2023-11) (has2023epidemiologyofinherited pages 7-7).

---

## 9. Inheritance and population

### 9.1 Inheritance pattern
EBS is **most often autosomal dominant**, with autosomal recessive forms also described. (has2020consensusreclassificationof pages 2-3).

### 9.2 Epidemiology (recent quantitative estimates)
**Germany (population-based capture–recapture; incidence years 2003–2019; age assessed as of 2022-04-01):**
- Overall inherited EB incidence: **45.09 per 1,000,000 live births** (≈ **1 in 22,178 live births per year**)
- EBS incidence: **14.93 per 1,000,000 live births** (≈ **1 in 66,979**)
- Estimated prevalence (all EB): **54.02 per million**; EBS prevalence: **28.44 per million**
(Has et al., *JEADV*, 2023-11, https://doi.org/10.1111/jdv.18637) (has2023epidemiologyofinherited pages 5-6, has2023epidemiologyofinherited pages 7-7).

**United States (review-level estimates as reported in a therapeutics-focused review):** incidence and prevalence were stated as **11.1 per million** and **19.6 per million**, respectively. (Rosa et al., 2023-09) (rosa2023stairwaystoadvanced pages 1-3).

---

## 10. Diagnostics

### 10.1 Diagnostic approach (guidelines and current practice)
The 2019 clinical practice guidelines for laboratory diagnosis of EB recommend that laboratory diagnosis be initiated “as soon as there is clinical suspicion,” and state: **“Genetic testing is always recommended”** (index case and, if possible, parents). (Has et al., *Br J Dermatol*, 2019-08, https://doi.org/10.1111/bjd.18128) (has2019clinicalpracticeguidelines pages 1-2).

**Immunofluorescence mapping (IFM):** Recommended as an early test to obtain rapid diagnosis/prognosis and to prioritize and interpret genetic testing. In neonates, the guideline notes IFM can provide diagnosis “within hours.” (Has et al., 2019-08) (has2019clinicalpracticeguidelines pages 6-7).

**Parallel testing in neonates:** Neonatal review recommendations: “obtain a skin biopsy for IFM and a blood sample for genetic testing to be run in parallel.” (Lucky et al., *NeoReviews*, 2021-07, https://doi.org/10.1542/neo.22-7-e438) (lucky2021diagnosisandcare pages 3-5).

**Specimen handling (selected technical details):** 3–4 mm punch biopsy for IFM in Michel media; 2–3 mm punch biopsy for EM in glutaraldehyde fixative. (Lucky et al., 2021-07) (lucky2021diagnosisandcare pages 3-5).

**Genetic testing modalities:** Guidelines describe use of targeted EB gene panels/NGS, WES, and Sanger sequencing, with escalation to RNA-based or copy-number approaches when needed. (Has et al., 2019-08) (has2019clinicalpracticeguidelines pages 10-11). The neonatal review notes NGS targeted panels typically have ~1 month turnaround and are more cost-effective than sequential Sanger sequencing. (Lucky et al., 2021-07) (lucky2021diagnosisandcare pages 3-5).

### 10.2 Differential diagnosis
Not systematically extracted from the available evidence excerpts in this run.

---

## 11. Outcomes / prognosis
EBS prognosis is heterogeneous: localized forms often have near-normal life expectancy, whereas severe generalized forms can be associated with serious complications and early mortality in some cases. (Has et al., 2020-03) (has2020consensusreclassificationof pages 2-3). A Germany EB epidemiology study reported mortality metrics primarily for JEB/DEB; it did not provide an EBS-specific mean age at death in the extracted snippets. (has2023epidemiologyofinherited pages 7-8).

---

## 12. Treatment

### 12.1 Standard-of-care (real-world implementation)
There is no universally curative treatment for EB; management is multidisciplinary and supportive (wound care, symptom control, complication prevention). (Bardhan et al., *Nat Rev Dis Primers*, 2020-09, https://doi.org/10.1038/s41572-020-0210-0) (bardhan2020epidermolysisbullosa pages 1-2).

### 12.2 Drug repurposing and targeted therapies in EBS (selected examples)

#### (A) Topical diacerein (anti–IL-1β axis)
A Phase 2 randomized crossover trial record for EBS–Dowling–Meara (generalized severe) describes topical 1% diacerein cream targeting IL‑1β/JNK-associated disease biology. The record reports a prior pilot (n=5) with blister reductions **−78%** and **−66%** from baseline within two weeks in an armpit model. (ClinicalTrials.gov NCT02470689; 2015; https://clinicaltrials.gov/study/NCT02470689) (NCT02470689 chunk 1).

**MAXO suggestions (examples):** topical pharmacotherapy; anti-inflammatory therapy.

#### (B) mTOR inhibition (topical sirolimus)
A 2024 EBS mechanism/therapeutics review describes topical sirolimus as an mTOR inhibitor with reported clinical improvement in two patients with plantar keratoderma, and summarizes topical sirolimus as a repositioning approach supported by transcriptomic rationale. (Bchetnia et al., 2024-08) (bchetnia2024pathologicalmechanismsinvolved pages 10-12, bchetnia2024pathologicalmechanismsinvolved pages 13-14).

**MAXO suggestions:** topical rapamycin therapy; mTOR inhibitor therapy.

#### (C) Botulinum toxin for plantar disease (symptom and blister reduction)
The same 2024 review summarizes small studies/case reports of botulinum toxin (types A and B) injected into feet of patients with localized and severe EBS, with reported improvements in blistering and pedal pain (and odor in a pediatric case). (Bchetnia et al., 2024-08) (bchetnia2024pathologicalmechanismsinvolved pages 10-12, bchetnia2024pathologicalmechanismsinvolved pages 13-14).

**MAXO suggestions:** botulinum toxin injection; pain management.

### 12.3 Clinical trials (selected EBS-relevant trials and endpoints)
A major EB review lists interventional trials relevant to EBS including:
- **Diacerein** Phase II placebo-controlled trial **NCT03154333** with endpoint described as proportion achieving ≥60% improvement in affected assessed body surface area.
- **Sirolimus** Phase II placebo-controlled trial **NCT03016715** with endpoints including foot health status, pedometer progress, plantar defect size, disease severity, and quality of life.
- **Botulinum toxin** randomized crossover trial for localized EBS **NCT03453632** with endpoints including plantar pain/tolerability.
(Bardhan et al., 2020-09) (bardhan2020epidermolysisbullosa pages 20-21).

*Note:* For trial phase/status/enrollment details beyond those in the cited excerpt, ClinicalTrials.gov records should be consulted directly; those details were not consistently present in the extracted evidence snippets for all listed NCTs.

---

## 13. Prevention
Primary prevention of genetically determined EBS is not currently feasible, but **genetic counseling** and **prenatal diagnosis** are discussed in diagnostic guidelines: DNA-based prenatal diagnosis is technically feasible for EB subtypes once familial pathogenic variants are known, subject to national regulations and family preference. (Has et al., 2019-08) (has2019clinicalpracticeguidelines pages 1-2).

---

## 14. Other species / natural disease
A spontaneous **KRT5** insertion variant has been reported as a **novel nonhuman primate model** of EBS in rhesus macaques (*Macaca mulatta*). Two stillborn homozygous animals had widespread epidermal loss, intraepidermal clefts above the basement membrane, absent cytokeratin-5 immunoreactivity in epidermis, and a **34-bp insertion in exon 5 of KRT5** (HGVS-like c.1087_1088ins...). (Johnson et al., *Vet Pathol*, 2020-02, https://doi.org/10.1177/0300985819900354) (johnson2020spontaneouskrt5gene pages 1-3).

---

## 15. Model organisms
The rhesus macaque KRT5 model above provides a spontaneous large-animal model with histologic and molecular features consistent with basal-layer cleavage. (johnson2020spontaneouskrt5gene pages 1-3). Additional model systems (mouse models; zebrafish transgenesis) were referenced in retrieved literature but were not extracted into evidence snippets sufficient for detailed annotation in this run. (bchetnia2024pathologicalmechanismsinvolved pages 1-2).

---

## Evidence table (knowledge-base ready)
The following table consolidates key, evidence-supported facts.

| Category | Specific data points (with numbers) | Best supporting citation IDs |
|---|---|---|
| Identifiers/Classification | EBS is 1 of the 4 classical EB types; cleavage occurs within the basal layer of keratinocytes/intraepidermally. The 2020 consensus notes 7 genes associated with EBS. | (has2020consensusreclassificationof pages 2-3, has2020consensusreclassificationof pages 1-2, bchetnia2024pathologicalmechanismsinvolved pages 1-2) |
| Core definition | EBS is the most common EB subtype; one review cites ~70% of all EB, while a Dutch source cited in a patient-perspective review reports 45.7% of Dutch EB cases. | (bardhan2020epidermolysisbullosa pages 1-2, stock2024thepatientsperspective pages 4-7) |
| Major subtypes | Main clinical subtypes are localized, intermediate, and severe/generalized severe (historically Weber-Cockayne, Köebner, Dowling-Meara). In the German dataset, EBS subtypes were localized 39.5% and severe 14.7%; 33.4% lacked subclassification. In the China cohort, EBS cases were localized 17.5%, intermediate 35.0%, severe 27.2%. | (has2020consensusreclassificationof pages 2-3, bchetnia2024pathologicalmechanismsinvolved pages 1-2, has2023epidemiologyofinherited pages 5-6, chen2023genotypeandphenotype pages 2-2) |
| Key genes | Core genes: KRT5 and KRT14 are predominant; additional EBS genes include PLEC, KLHL24, DST, EXPH5, CD151. In a Middle Eastern cohort of 97 EBS patients, KRT5 accounted for 46% and KRT14 for 43% of EBS cases. In the China cohort, PLEC and KLHL24 were each mutated in 4 cases. | (bchetnia2024pathologicalmechanismsinvolved pages 1-2, bergson2023clinicalandmolecular pages 1-2, chen2023genotypeandphenotype pages 3-3) |
| Inheritance | Usually autosomal dominant; autosomal recessive forms also occur. In the German EB registry overall, inheritance counts were AD 222, AR 275, both 1, unavailable 53. In the China EB cohort, de novo mutations were high in EBS (63.8%) and mosaicism was reported in ~5.4% of dominant EBS. | (has2020consensusreclassificationof pages 2-3, bchetnia2024pathologicalmechanismsinvolved pages 1-2, has2023epidemiologyofinherited pages 5-6, chen2023genotypeandphenotype pages 1-1) |
| Epidemiology | Germany: overall EB incidence 45.09 per 1,000,000 live births (1 in 22,178); EBS incidence 14.93 per 1,000,000 live births (1:66,979). Germany prevalence estimates: overall EB 54.02/million; EBS 28.44/million. United States figures cited in reviews include incidence 8.2/million live births/year in newborn review, 11.1/million and prevalence 19.6/million in another review. | (has2023epidemiologyofinherited pages 5-6, has2023epidemiologyofinherited pages 7-7, lucky2021diagnosisandcare pages 1-2, rosa2023stairwaystoadvanced pages 1-3) |
| Diagnostics | Recommended neonatal workflow: skin biopsy for IFM plus blood for genetic testing in parallel. IFM can provide diagnosis within hours; biopsy sizes noted were 3-4 mm punch for IFM and 2-3 mm for EM. NGS-targeted EB panels typically have ~1 month turnaround. Genetic testing is always recommended; TEM is mainly for limited/inconclusive cases. | (lucky2021diagnosisandcare pages 3-5, has2019clinicalpracticeguidelines pages 1-2, has2019clinicalpracticeguidelines pages 6-7, has2019clinicalpracticeguidelines pages 4-6) |
| Mechanisms | Dominant KRT5/KRT14 mutations disrupt basal keratin intermediate filaments, causing keratin aggregates, ER stress, and pro-inflammatory signaling. Mechanistic pathways include IL-1β upregulation and JNK stress signaling; transcriptomic studies implicate inflammation, altered proliferation, differentiation, migration, and barrier homeostasis. | (NCT02470689 chunk 1, bchetnia2024pathologicalmechanismsinvolved pages 1-2, bchetnia2024pathologicalmechanismsinvolved pages 8-10) |
| Treatments/Trials | Diacerein: Phase 2 crossover trial NCT02470689 planned enrollment 50, ages 6-19, primary endpoint blister number at 4 weeks; prior pilot (n=5) reported blister reductions of -78% and -66% from baseline within 2 weeks. Long-term topical diacerein study NCT03389308 enrolled 51. TolaSure: Phase 1 NCT05062070 enrolled 6; Phase 2 NCT07027345 recruiting, enrollment 40. Sirolimus trial NCT03016715 enrolled 8. Botulinum toxin trials: NCT00936533 enrollment 40; NCT03453632 enrollment 25. Erythromycin Phase 3 NCT01340235 enrollment 8. | (NCT02470689 chunk 1, bardhan2020epidermolysisbullosa pages 20-21, bchetnia2024pathologicalmechanismsinvolved pages 10-12, bchetnia2024pathologicalmechanismsinvolved pages 13-14) |
| QoL burden | Global EBS survey: n=214, mean age 32.8 years. Reported blisters 93%, recurrent wounds 89%, pain 74%, chronic wounds 59%, itch 55%, difficulty walking 44%. Mean QOLEB score 14.7 (SD 7.5), indicating moderate impact; 12% required regular opiates. | (so2022aglobalcrosssectional pages 10-12) |
| Models/other species | Natural/experimental models include rhesus macaques with a 34-bp KRT5 insertion; 2 homozygous animals were stillborn with widespread epidermal loss, compared with 6 phenotypically normal heterozygotes. Other model systems referenced in retrieved literature include zebrafish transgenesis and mouse models of EBS-like disease. | (so2022aglobalcrosssectional pages 1-2) |


*Table: This table compiles core disease knowledge-base facts for epidermolysis bullosa simplex, including classification, epidemiology, genetics, diagnostics, mechanisms, therapies, and patient burden. Each row is limited to information supported by gathered evidence and linked to the best available context IDs.*

---

## Limitations of this report (evidence availability)
- **Disease identifiers (OMIM/Orphanet/ICD/MeSH/MONDO):** not retrievable from the evidence excerpts available in this run; therefore, this section is incomplete.
- **Differential diagnosis and comprehensive subtype-specific prognostic statistics:** not fully extractable from the retrieved snippets.
- **ClinicalTrials.gov metadata for every EBS trial (status/enrollment/endpoints):** only partially extractable from available excerpts; one EBS diacerein trial record (NCT02470689) was captured in detail. (NCT02470689 chunk 1).

References

1. (has2020consensusreclassificationof pages 2-3): C. Has, J.W. Bauer, C. Bodemer, M.C. Bolling, L. Bruckner‐Tuderman, A. Diem, J.‐D. Fine, A. Heagerty, A. Hovnanian, M.P. Marinkovich, A.E. Martinez, J.A. McGrath, C. Moss, D.F. Murrell, F. Palisson, A. Schwieger‐Briel, E. Sprecher, K. Tamai, J. Uitto, D.T. Woodley, G. Zambruno, and J.E. Mellerio. Consensus reclassification of inherited epidermolysis bullosa and other disorders with skin fragility. British Journal of Dermatology, 183:614-627, Mar 2020. URL: https://doi.org/10.1111/bjd.18921, doi:10.1111/bjd.18921. This article has 905 citations and is from a highest quality peer-reviewed journal.

2. (has2020consensusreclassificationof pages 1-2): C. Has, J.W. Bauer, C. Bodemer, M.C. Bolling, L. Bruckner‐Tuderman, A. Diem, J.‐D. Fine, A. Heagerty, A. Hovnanian, M.P. Marinkovich, A.E. Martinez, J.A. McGrath, C. Moss, D.F. Murrell, F. Palisson, A. Schwieger‐Briel, E. Sprecher, K. Tamai, J. Uitto, D.T. Woodley, G. Zambruno, and J.E. Mellerio. Consensus reclassification of inherited epidermolysis bullosa and other disorders with skin fragility. British Journal of Dermatology, 183:614-627, Mar 2020. URL: https://doi.org/10.1111/bjd.18921, doi:10.1111/bjd.18921. This article has 905 citations and is from a highest quality peer-reviewed journal.

3. (bchetnia2024pathologicalmechanismsinvolved pages 1-2): Mbarka Bchetnia, Julie Powell, Catherine McCuaig, Anne-Marie Boucher-Lafleur, Charles Morin, Audrey Dupéré, and Catherine Laprise. Pathological mechanisms involved in epidermolysis bullosa simplex: current knowledge and therapeutic perspectives. International Journal of Molecular Sciences, 25:9495, Aug 2024. URL: https://doi.org/10.3390/ijms25179495, doi:10.3390/ijms25179495. This article has 11 citations.

4. (has2019clinicalpracticeguidelines pages 1-2): C. Has, L. Liu, M.C. Bolling, A.V. Charlesworth, M. El Hachem, M.J. Escámez, I. Fuentes, S. Büchel, R. Hiremagalore, G. Pohla‐Gubo, P.C. Akker, K. Wertheim‐Tysarowska, and G. Zambruno. Clinical practice guidelines for laboratory diagnosis of epidermolysis bullosa. The British Journal of Dermatology, 182:574-592, Aug 2019. URL: https://doi.org/10.1111/bjd.18128, doi:10.1111/bjd.18128. This article has 186 citations.

5. (has2023epidemiologyofinherited pages 7-7): Cristina Has, Moritz Hess, Waltraud Anemüller, Ulrike Blume‐Peytavi, Steffen Emmert, Regina Fölster‐Holst, Jorge Frank, Kathrin Giehl, Claudia Günther, Johanna Hammersen, Kathrin Hillmann, Bettina Höflein, Peter H. Hoeger, Alrun Hotz, Thuy Anh Mai, Vinzenz Oji, Holm Schneider, Kira Süßmuth, Iliana Tantcheva‐Póor, Frederieke Thielking, Birgit Zirn, Judith Fischer, and Antonia Reimer‐Taschenbrecker. Epidemiology of inherited epidermolysis bullosa in germany. Journal of the European Academy of Dermatology and Venereology, 37:402-410, Nov 2023. URL: https://doi.org/10.1111/jdv.18637, doi:10.1111/jdv.18637. This article has 56 citations and is from a domain leading peer-reviewed journal.

6. (so2022aglobalcrosssectional pages 1-2): Jodi Y. So, Shivali Fulchand, Christine Y. Wong, Shufeng Li, Jaron Nazaroff, Emily S. Gorell, Mark P. de Souza, Dedee F. Murrell, Joyce M. Teng, Albert S. Chiou, and Jean Y. Tang. A global, cross-sectional survey of patient-reported outcomes, disease burden, and quality of life in epidermolysis bullosa simplex. Orphanet Journal of Rare Diseases, Jul 2022. URL: https://doi.org/10.1186/s13023-022-02433-3, doi:10.1186/s13023-022-02433-3. This article has 21 citations and is from a peer-reviewed journal.

7. (NCT02470689 chunk 1): michal roll. Diacerin for the Treatment of Epidermolysis Bullosa Simplex. Tel-Aviv Sourasky Medical Center. 2015. ClinicalTrials.gov Identifier: NCT02470689

8. (chen2023genotypeandphenotype pages 1-1): Fuying Chen, Ruoqu Wei, Dan Deng, Xue Zhang, Yu Cao, Chaolan Pan, Yumeng Wang, Qiaoyu Cao, Jianbo Wang, Ming Zeng, Linting Huang, Yan Gu, Zhirong Yao, and Ming Li. Genotype and phenotype correlations in 441 patients with epidermolysis bullosa from china. Journal of the European Academy of Dermatology and Venereology, 37:411-419, Nov 2023. URL: https://doi.org/10.1111/jdv.18692, doi:10.1111/jdv.18692. This article has 26 citations and is from a domain leading peer-reviewed journal.

9. (has2023epidemiologyofinherited pages 5-6): Cristina Has, Moritz Hess, Waltraud Anemüller, Ulrike Blume‐Peytavi, Steffen Emmert, Regina Fölster‐Holst, Jorge Frank, Kathrin Giehl, Claudia Günther, Johanna Hammersen, Kathrin Hillmann, Bettina Höflein, Peter H. Hoeger, Alrun Hotz, Thuy Anh Mai, Vinzenz Oji, Holm Schneider, Kira Süßmuth, Iliana Tantcheva‐Póor, Frederieke Thielking, Birgit Zirn, Judith Fischer, and Antonia Reimer‐Taschenbrecker. Epidemiology of inherited epidermolysis bullosa in germany. Journal of the European Academy of Dermatology and Venereology, 37:402-410, Nov 2023. URL: https://doi.org/10.1111/jdv.18637, doi:10.1111/jdv.18637. This article has 56 citations and is from a domain leading peer-reviewed journal.

10. (chen2023genotypeandphenotype pages 2-2): Fuying Chen, Ruoqu Wei, Dan Deng, Xue Zhang, Yu Cao, Chaolan Pan, Yumeng Wang, Qiaoyu Cao, Jianbo Wang, Ming Zeng, Linting Huang, Yan Gu, Zhirong Yao, and Ming Li. Genotype and phenotype correlations in 441 patients with epidermolysis bullosa from china. Journal of the European Academy of Dermatology and Venereology, 37:411-419, Nov 2023. URL: https://doi.org/10.1111/jdv.18692, doi:10.1111/jdv.18692. This article has 26 citations and is from a domain leading peer-reviewed journal.

11. (so2022aglobalcrosssectional pages 6-8): Jodi Y. So, Shivali Fulchand, Christine Y. Wong, Shufeng Li, Jaron Nazaroff, Emily S. Gorell, Mark P. de Souza, Dedee F. Murrell, Joyce M. Teng, Albert S. Chiou, and Jean Y. Tang. A global, cross-sectional survey of patient-reported outcomes, disease burden, and quality of life in epidermolysis bullosa simplex. Orphanet Journal of Rare Diseases, Jul 2022. URL: https://doi.org/10.1186/s13023-022-02433-3, doi:10.1186/s13023-022-02433-3. This article has 21 citations and is from a peer-reviewed journal.

12. (bergson2023clinicalandmolecular pages 1-2): Shir Bergson, Daniel Daniely, David Bomze, Janan Mohamad, Kiril Malovitski, Odile Meijers, Valeria Briskin, Ofer Bihari, Natalia Malchin, Shirli Israeli, Jacob Mashiah, Tzipora Falik‐Zaccai, Emily Avitan‐Hersh, Marina Eskin‐Schwartz, Stavit Allon‐Shalev, Ofer Sarig, Eli Sprecher, and Liat Samuelov. Clinical and molecular features in a cohort of middle eastern patients with epidermolysis bullosa. Pediatric Dermatology, 40:1021-1027, Oct 2023. URL: https://doi.org/10.1111/pde.15440, doi:10.1111/pde.15440. This article has 6 citations and is from a peer-reviewed journal.

13. (chen2023genotypeandphenotype pages 3-3): Fuying Chen, Ruoqu Wei, Dan Deng, Xue Zhang, Yu Cao, Chaolan Pan, Yumeng Wang, Qiaoyu Cao, Jianbo Wang, Ming Zeng, Linting Huang, Yan Gu, Zhirong Yao, and Ming Li. Genotype and phenotype correlations in 441 patients with epidermolysis bullosa from china. Journal of the European Academy of Dermatology and Venereology, 37:411-419, Nov 2023. URL: https://doi.org/10.1111/jdv.18692, doi:10.1111/jdv.18692. This article has 26 citations and is from a domain leading peer-reviewed journal.

14. (chen2023genotypeandphenotype pages 4-4): Fuying Chen, Ruoqu Wei, Dan Deng, Xue Zhang, Yu Cao, Chaolan Pan, Yumeng Wang, Qiaoyu Cao, Jianbo Wang, Ming Zeng, Linting Huang, Yan Gu, Zhirong Yao, and Ming Li. Genotype and phenotype correlations in 441 patients with epidermolysis bullosa from china. Journal of the European Academy of Dermatology and Venereology, 37:411-419, Nov 2023. URL: https://doi.org/10.1111/jdv.18692, doi:10.1111/jdv.18692. This article has 26 citations and is from a domain leading peer-reviewed journal.

15. (rosa2023stairwaystoadvanced pages 1-3): Laura De Rosa, Elena Enzo, Michele Palamenghi, Laura Sercia, and Michele De Luca. Stairways to advanced therapies for epidermolysis bullosa. Cold Spring Harbor perspectives in biology, 15:a041229, Sep 2023. URL: https://doi.org/10.1101/cshperspect.a041229, doi:10.1101/cshperspect.a041229. This article has 14 citations and is from a peer-reviewed journal.

16. (has2019clinicalpracticeguidelines pages 6-7): C. Has, L. Liu, M.C. Bolling, A.V. Charlesworth, M. El Hachem, M.J. Escámez, I. Fuentes, S. Büchel, R. Hiremagalore, G. Pohla‐Gubo, P.C. Akker, K. Wertheim‐Tysarowska, and G. Zambruno. Clinical practice guidelines for laboratory diagnosis of epidermolysis bullosa. The British Journal of Dermatology, 182:574-592, Aug 2019. URL: https://doi.org/10.1111/bjd.18128, doi:10.1111/bjd.18128. This article has 186 citations.

17. (lucky2021diagnosisandcare pages 3-5): Anne W. Lucky, Jean Whalen, Susan Rowe, Kalyani S. Marathe, and Emily Gorell. Diagnosis and care of the newborn with epidermolysis bullosa. NeoReviews, 22 7:e438-e451, Jul 2021. URL: https://doi.org/10.1542/neo.22-7-e438, doi:10.1542/neo.22-7-e438. This article has 44 citations.

18. (has2019clinicalpracticeguidelines pages 10-11): C. Has, L. Liu, M.C. Bolling, A.V. Charlesworth, M. El Hachem, M.J. Escámez, I. Fuentes, S. Büchel, R. Hiremagalore, G. Pohla‐Gubo, P.C. Akker, K. Wertheim‐Tysarowska, and G. Zambruno. Clinical practice guidelines for laboratory diagnosis of epidermolysis bullosa. The British Journal of Dermatology, 182:574-592, Aug 2019. URL: https://doi.org/10.1111/bjd.18128, doi:10.1111/bjd.18128. This article has 186 citations.

19. (has2023epidemiologyofinherited pages 7-8): Cristina Has, Moritz Hess, Waltraud Anemüller, Ulrike Blume‐Peytavi, Steffen Emmert, Regina Fölster‐Holst, Jorge Frank, Kathrin Giehl, Claudia Günther, Johanna Hammersen, Kathrin Hillmann, Bettina Höflein, Peter H. Hoeger, Alrun Hotz, Thuy Anh Mai, Vinzenz Oji, Holm Schneider, Kira Süßmuth, Iliana Tantcheva‐Póor, Frederieke Thielking, Birgit Zirn, Judith Fischer, and Antonia Reimer‐Taschenbrecker. Epidemiology of inherited epidermolysis bullosa in germany. Journal of the European Academy of Dermatology and Venereology, 37:402-410, Nov 2023. URL: https://doi.org/10.1111/jdv.18637, doi:10.1111/jdv.18637. This article has 56 citations and is from a domain leading peer-reviewed journal.

20. (bardhan2020epidermolysisbullosa pages 1-2): Ajoy Bardhan, Leena Bruckner-Tuderman, Iain L. C. Chapple, Jo-David Fine, Natasha Harper, Cristina Has, Thomas M. Magin, M. Peter Marinkovich, John F. Marshall, John A. McGrath, Jemima E. Mellerio, Rex Polson, and Adrian H. Heagerty. Epidermolysis bullosa. Nature Reviews Disease Primers, 6:1-27, Sep 2020. URL: https://doi.org/10.1038/s41572-020-0210-0, doi:10.1038/s41572-020-0210-0. This article has 551 citations.

21. (bchetnia2024pathologicalmechanismsinvolved pages 10-12): Mbarka Bchetnia, Julie Powell, Catherine McCuaig, Anne-Marie Boucher-Lafleur, Charles Morin, Audrey Dupéré, and Catherine Laprise. Pathological mechanisms involved in epidermolysis bullosa simplex: current knowledge and therapeutic perspectives. International Journal of Molecular Sciences, 25:9495, Aug 2024. URL: https://doi.org/10.3390/ijms25179495, doi:10.3390/ijms25179495. This article has 11 citations.

22. (bchetnia2024pathologicalmechanismsinvolved pages 13-14): Mbarka Bchetnia, Julie Powell, Catherine McCuaig, Anne-Marie Boucher-Lafleur, Charles Morin, Audrey Dupéré, and Catherine Laprise. Pathological mechanisms involved in epidermolysis bullosa simplex: current knowledge and therapeutic perspectives. International Journal of Molecular Sciences, 25:9495, Aug 2024. URL: https://doi.org/10.3390/ijms25179495, doi:10.3390/ijms25179495. This article has 11 citations.

23. (bardhan2020epidermolysisbullosa pages 20-21): Ajoy Bardhan, Leena Bruckner-Tuderman, Iain L. C. Chapple, Jo-David Fine, Natasha Harper, Cristina Has, Thomas M. Magin, M. Peter Marinkovich, John F. Marshall, John A. McGrath, Jemima E. Mellerio, Rex Polson, and Adrian H. Heagerty. Epidermolysis bullosa. Nature Reviews Disease Primers, 6:1-27, Sep 2020. URL: https://doi.org/10.1038/s41572-020-0210-0, doi:10.1038/s41572-020-0210-0. This article has 551 citations.

24. (johnson2020spontaneouskrt5gene pages 1-3): Amanda L. Johnson, Samuel M. Peterson, Margaret M. L. Terry, Betsy Ferguson, Lois M. Colgin, and Anne D. Lewis. Spontaneous krt5 gene mutation in rhesus macaques (macaca mulatta): a novel nonhuman primate model of epidermolysis bullosa simplex. Veterinary Pathology, 57:344-348, Feb 2020. URL: https://doi.org/10.1177/0300985819900354, doi:10.1177/0300985819900354. This article has 8 citations and is from a domain leading peer-reviewed journal.

25. (stock2024thepatientsperspective pages 4-7): C Stock. The patient's perspective: a review on epidermolysis bullosa patients' needs as input towards harmonization of outcomes. Unknown journal, 2024.

26. (lucky2021diagnosisandcare pages 1-2): Anne W. Lucky, Jean Whalen, Susan Rowe, Kalyani S. Marathe, and Emily Gorell. Diagnosis and care of the newborn with epidermolysis bullosa. NeoReviews, 22 7:e438-e451, Jul 2021. URL: https://doi.org/10.1542/neo.22-7-e438, doi:10.1542/neo.22-7-e438. This article has 44 citations.

27. (has2019clinicalpracticeguidelines pages 4-6): C. Has, L. Liu, M.C. Bolling, A.V. Charlesworth, M. El Hachem, M.J. Escámez, I. Fuentes, S. Büchel, R. Hiremagalore, G. Pohla‐Gubo, P.C. Akker, K. Wertheim‐Tysarowska, and G. Zambruno. Clinical practice guidelines for laboratory diagnosis of epidermolysis bullosa. The British Journal of Dermatology, 182:574-592, Aug 2019. URL: https://doi.org/10.1111/bjd.18128, doi:10.1111/bjd.18128. This article has 186 citations.

28. (bchetnia2024pathologicalmechanismsinvolved pages 8-10): Mbarka Bchetnia, Julie Powell, Catherine McCuaig, Anne-Marie Boucher-Lafleur, Charles Morin, Audrey Dupéré, and Catherine Laprise. Pathological mechanisms involved in epidermolysis bullosa simplex: current knowledge and therapeutic perspectives. International Journal of Molecular Sciences, 25:9495, Aug 2024. URL: https://doi.org/10.3390/ijms25179495, doi:10.3390/ijms25179495. This article has 11 citations.

29. (so2022aglobalcrosssectional pages 10-12): Jodi Y. So, Shivali Fulchand, Christine Y. Wong, Shufeng Li, Jaron Nazaroff, Emily S. Gorell, Mark P. de Souza, Dedee F. Murrell, Joyce M. Teng, Albert S. Chiou, and Jean Y. Tang. A global, cross-sectional survey of patient-reported outcomes, disease burden, and quality of life in epidermolysis bullosa simplex. Orphanet Journal of Rare Diseases, Jul 2022. URL: https://doi.org/10.1186/s13023-022-02433-3, doi:10.1186/s13023-022-02433-3. This article has 21 citations and is from a peer-reviewed journal.
