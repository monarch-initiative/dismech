---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T16:14:19.280922'
end_time: '2026-05-10T16:32:10.299240'
duration_seconds: 1071.02
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Postcricoid Region Cancer
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Postcricoid Region Cancer
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Postcricoid Region Cancer** covering all of the
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
- **Disease Name:** Postcricoid Region Cancer
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Postcricoid Region Cancer** covering all of the
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


# Postcricoid Region Cancer (Postcricoid Hypopharyngeal Carcinoma): Disease Characteristics Research Report

## Target disease
**Disease name:** Postcricoid region cancer (most commonly **postcricoid hypopharyngeal squamous cell carcinoma**, a hypopharyngeal cancer subsite) (glastonbury2020headandneck pages 1-2, mousavi2024globalepidemiologyand pages 1-2).

---

## Executive summary (current understanding)
Postcricoid region cancer is best conceptualized as a **hypopharyngeal malignancy** arising from the **postcricoid region** (anterior wall of the hypopharynx, overlying the posterior cricoid cartilage), most often **squamous cell carcinoma (SCC)**. It is clinically important because (i) it is frequently advanced at diagnosis, (ii) it exhibits submucosal spread toward the cervical esophagus, and (iii) treatment requires balancing oncologic control with laryngo-esophageal function preservation (glastonbury2020headandneck pages 1-2, sahu2023imagingrecommendationsfor pages 5-8, katano2024earlystagehypopharyngealsquamous pages 1-2).

A concise evidence table of key recent quantitative findings is provided below.

| Topic | Key quantitative data | Key qualitative takeaway | Source (first author, year) | URL |
|---|---|---|---|---|
| Global epidemiology of hypopharyngeal cancer (includes postcricoid subsite) | 84,254 new cases globally in 2020; ASIR 0.91/100,000; 38,599 deaths; ASMR 0.41/100,000; MIR 0.45; projected increase by 2040: new cases +50%, deaths +55%; subsite distribution: ~70% pyriform sinus, ~25% posterior pharyngeal wall, remainder largely post-cricoid; HC is <5% of head and neck malignancies (mousavi2024globalepidemiologyand pages 1-2, mousavi2024globalepidemiologyand pages 2-3) | Postcricoid-region cancer is best understood as a rare hypopharyngeal cancer subsite within a high-mortality disease that is more common in men and often diagnosed late. | Mousavi, 2024 | https://doi.org/10.3389/fonc.2024.1398063 |
| Symptoms and NCCN diagnostic workup | Common symptoms: hoarseness, breathing difficulty, dysphagia/odynophagia, foreign-body sensation, ear ache; advanced signs include stridor/aspiration. NCCN-referenced workup: examination under anesthesia with endoscopy/biopsy; CECT and/or MRI of primary and neck; chest CT for advanced nodal disease/smokers; FDG PET-CT for stage III-IV disease (sahu2023imagingrecommendationsfor pages 1-2, sahu2023imagingrecommendationsfor pages 5-8, sahu2023imagingrecommendationsfor pages 2-3) | Endoscopy is essential for mucosal assessment and biopsy, but CT/MRI/PET are required to define submucosal spread, cartilage invasion, nodal disease, response, and recurrence in postcricoid tumors. | Sahu, 2023 | https://doi.org/10.1055/s-0042-1759504 |
| Radical radiotherapy outcomes for early-stage HSCC, including postcricoid subsite | Uniform RT: 70 Gy in 35 fractions to primary site plus elective nodal irradiation; 5-year OS 80.7% (95% CI 66.5-89.4%); 5-year DFS 66.4%; 5-year LRC 79.3%; postcricoid subsite 5-year OS 100% in this small series; no grade >=3 toxicities reported (katano2024earlystagehypopharyngealsquamous pages 1-2, katano2024earlystagehypopharyngealsquamous pages 2-5) | For stage I-II hypopharyngeal SCC, organ-preserving radical RT can produce strong long-term control with favorable toxicity; postcricoid outcomes were encouraging but based on very small numbers. | Katano, 2024 | https://doi.org/10.1007/s00405-024-08722-w |
| Surgery-based therapy vs definitive chemoradiotherapy in hypopharyngeal carcinoma | 167 patients; 5-year OS 59.7% with surgery-based therapy vs 24.0% with definitive CRT (p<0.0001); 5-year PFS 49.9% vs 22.6% (p=0.0002); surgery also improved LFFS, RFFS, DMFFS; survival similar between modalities mainly for T3 or stage III disease (lin2023survivalanalysesof pages 1-2, lin2023survivalanalysesof pages 2-3) | In retrospective data, surgery-based therapy often outperformed definitive CRT overall, but organ-preservation approaches may remain reasonable for selected T3/stage III cases. Extensive postcricoid/esophageal inlet involvement favored total laryngectomy/pharyngectomy. | Lin, 2023 | https://doi.org/10.3389/fonc.2023.1109417 |
| Plummer-Vinson syndrome (PVS) as a risk context for postcricoid/pharyngeal SCC | Reported malignancy incidence in PVS: 3-15% overall; one report cites post-cricoid carcinoma in ~4-16% across studies; yearly surveillance endoscopy is commonly suggested though no definitive guideline exists (patil2023endoscopicsubmucosaldissection pages 1-2, lo2019plummervinsonsyndromeimproving pages 5-6, patil2023endoscopicsubmucosaldissection pages 2-4, lo2019plummervinsonsyndromeimproving pages 2-3) | PVS (iron deficiency anemia + dysphagia + upper esophageal/post-cricoid web) is a classic premalignant association for postcricoid/pharyngeal SCC; long-term surveillance is generally recommended despite limited evidence and lack of standardized intervals. | Lo, 2019; Patil, 2023 | https://doi.org/10.2147/JMDH.S180410 ; https://doi.org/10.1055/s-0042-1759510 |
| Organ-preservation chemoimmunotherapy studies/trials | NCT04156698: phase II, n=51, camrelizumab + modified TPF; ORR 82.4% (42/51); 2-year OS 83.0%; 2-year PFS 77.1%; 2-year larynx preservation rate 70.0%. NCT06039631: randomized phase II, planned n=82; neoadjuvant chemoimmunotherapy followed by organ-preservation surgery vs concurrent chemoradiation; RT arm 70 Gy/35 fractions + weekly cisplatin; primary endpoint 2-year PFS; key secondary endpoints include larynx preservation, OS, QoL (NCT04156698 chunk 1, NCT06039631 chunk 1) | Recent organ-preservation strategies are shifting toward PD-1-based chemoimmunotherapy for locally advanced hypopharyngeal/laryngeal cancer, aiming to improve response and preserve laryngeal function without routine upfront total laryngectomy. | Gong/Wang, 2024-2023 (NCT04156698/NCT06039631) | https://clinicaltrials.gov/study/NCT04156698 ; https://clinicaltrials.gov/study/NCT06039631 |


*Table: This table summarizes key recent evidence and quantitative findings relevant to postcricoid-region cancer within hypopharyngeal squamous cell carcinoma. It highlights epidemiology, diagnosis, outcomes, risk context, and emerging organ-preservation approaches.*

---

## 1. Disease information

### 1.1 Disease overview and definition
* **Definition/anatomic subsite**: The postcricoid region is described as the **anterior wall of the hypopharynx** and corresponds to **mucosa overlying the posterior surface of the cricoid cartilage** (glastonbury2020headandneck pages 1-2). Postcricoid region cancer is therefore a subtype of hypopharyngeal cancer arising from this subsite (glastonbury2020headandneck pages 1-2, mousavi2024globalepidemiologyand pages 1-2).

### 1.2 Key identifiers and ontology mappings
* **ICD-O-3 topography (commonly used in SEER/registry datasets):** **C13.0 = postcricoid region** ().
* **MONDO:** OpenTargets returns **MONDO_0021358 (neoplasm of hypopharynx)** as a related disease entity in its hypopharynx cancer space (OpenTargets Search: hypopharyngeal carcinoma,head and neck squamous cell carcinoma). A postcricoid-specific MONDO term was not retrieved in the current evidence set.
* **EFO terms observed via OpenTargets context:** hypopharyngeal carcinoma **EFO_0002938**; hypopharyngeal squamous cell carcinoma **EFO_1001960** (OpenTargets Search: hypopharyngeal carcinoma,head and neck squamous cell carcinoma).

### 1.3 Common synonyms
* Postcricoid hypopharyngeal carcinoma; post-cricoid carcinoma; hypopharyngeal SCC of the postcricoid region; postcricoid-region hypopharyngeal cancer (li2026novellaryngealpreservation pages 1-2, glastonbury2020headandneck pages 1-2).

### 1.4 Evidence source type
The evidence here is largely from **aggregated disease-level resources** (GLOBOCAN 2020 analysis, imaging recommendations, trials) and **cohort studies/case series**, not single EHR-derived patient observations (mousavi2024globalepidemiologyand pages 1-2, sahu2023imagingrecommendationsfor pages 1-2, katano2024earlystagehypopharyngealsquamous pages 1-2).

---

## 2. Etiology

### 2.1 Causal factors and mechanisms (high-level)
Most postcricoid cancers are **mucosal epithelial SCCs** arising in the upper aerodigestive tract, consistent with the broader hypopharyngeal SCC pathogenesis (mousavi2024globalepidemiologyand pages 1-2, li2026novellaryngealpreservation pages 1-2).

### 2.2 Risk factors
**Lifestyle/environmental:**
* **Tobacco and alcohol** are highlighted as major risk factors in imaging-based clinical guidance for larynx/hypopharynx cancers (sahu2023imagingrecommendationsfor pages 1-2).

**Syndromic/premalignant association (important for the postcricoid region): Plummer–Vinson syndrome (PVS)**
* PVS is classically defined by the triad of **iron deficiency anemia, post-cricoid dysphagia, and an upper esophageal/post-cricoid web**, and is consistently described as associated with upper aerodigestive squamous cancers (patil2023endoscopicsubmucosaldissection pages 1-2, lo2019plummervinsonsyndromeimproving pages 1-2).
* Quantitative risk ranges reported in retrieved sources:
  * “**Malignancies occur at an incidence of 3–15%**” in PVS (lo2019plummervinsonsyndromeimproving pages 2-3).
  * A pooled frequency range reported in one PVS-focused source indicates **post-cricoid carcinoma occurs in ~4–16%** across studies (patil2023endoscopicsubmucosaldissection pages 1-2).

**Protective factors:** not clearly identified in the retrieved evidence set for this specific subsite.

### 2.3 Gene–environment considerations
The strongest evidence in this set supports classic **carcinogen exposure (tobacco/alcohol)** and **mucosal vulnerability due to iron deficiency** (PVS) as converging pathways toward squamous carcinogenesis (sahu2023imagingrecommendationsfor pages 1-2, patil2023endoscopicsubmucosaldissection pages 2-4).

---

## 3. Phenotypes (clinical presentation)

### 3.1 Key symptoms and signs
Common presenting features for larynx/hypopharynx cancers include **hoarseness, breathing difficulty, dysphagia/odynophagia, foreign-body sensation, ear ache**, and advanced presentations including **stridor or aspiration** (sahu2023imagingrecommendationsfor pages 1-2).

Early-stage hypopharyngeal SCC (including postcricoid) is often not detected promptly. One 2024 cohort reports: **“HSCC is often undetected until advanced stages”** and notes that **“More than 50% of patients with hypopharyngeal cancers … present at an advanced stage.”** (katano2024earlystagehypopharyngealsquamous pages 1-2).

### 3.2 Phenotype characteristics
* **Typical onset:** adult-onset cancer (registry-level; not a congenital disease entity).
* **Progression:** often insidious until advanced.

### 3.3 Quality-of-life impact
Swallowing and voice/airway issues are intrinsic to hypopharyngeal/postcricoid tumors due to proximity to the larynx and esophageal inlet; contemporary organ-preservation trials explicitly include QoL instruments (e.g., EORTC QLQ-H&N35; MDADI; VHI-10) as endpoints (NCT06957938 chunk 2, NCT06039631 chunk 1).

### 3.4 Suggested HPO terms (examples)
* Dysphagia **HP:0002015**
* Odynophagia **HP:0033050**
* Hoarseness/dysphonia **HP:0001609**
* Stridor **HP:0010448**
* Aspiration **HP:0002835**
* Otalgia (ear pain) **HP:0030766**

(These are suggested mappings based on the symptom set described in the clinical literature above; the exact HPO identifiers were not explicitly provided in retrieved sources.)

---

## 4. Genetic / molecular information

### 4.1 Somatic landscape (current understanding; largely extrapolated from HNSCC/HSCC)
Postcricoid cancers are usually SCC and share canonical head-and-neck SCC alterations.

* A 2024 review emphasizes TP53 as central: **“Mutation on the TP53 tumour suppressor gene is a key factor in cancer development”** and notes TP53-related biology intersects with tumor immune behavior including PD-L1 (CD274) in some contexts (shirima2024epithelial‑derivedheadand pages 3-4).
* A 2023 review lists recurrently altered tumor suppressors and oncogenes in HNSCC, including **TP53, CDKN2A, NOTCH1, FAT1, EGFR, PIK3CA, and RAS/HRAS** (afshari2023potentialalternativetherapeutic pages 1-2).
* OpenTargets associations (supportive, not definitive for this subsite) link hypopharyngeal carcinoma space to targets including **ADH1B** (with PubMed-listed evidence) and, in related pharyngeal SCC entities, to **TP53, EGFR, MET, PIK3CA, NOTCH1, KMT2D/KMT2C**, etc. (OpenTargets Search: hypopharyngeal carcinoma,head and neck squamous cell carcinoma).

### 4.2 Key pathways/processes implicated
From the retrieved HNSCC-focused reviews, major implicated signaling and cellular processes include:
* **Cell-cycle dysregulation / DNA damage response** (TP53, CDKN2A/p16, RB1/CCND1 context) (shirima2024epithelial‑derivedheadand pages 3-4, afshari2023potentialalternativetherapeutic pages 1-2).
* **RTK/RAS and EGFR signaling** (EGFR and RAS family contributions, therapeutic implications such as cetuximab resistance) (shirima2024epithelial‑derivedheadand pages 3-4).
* **PI3K/AKT/mTOR pathway and PTEN** (shirima2024epithelial‑derivedheadand pages 3-4).
* **Squamous differentiation programs** including NOTCH signaling (afshari2023potentialalternativetherapeutic pages 1-2).
* **Immune evasion/checkpoint biology** (PD-1/PD-L1 axis relevance in SCC immunotherapy selection) (shirima2024epithelial‑derivedheadand pages 3-4).

### 4.3 Suggested GO terms (examples)
* GO:0007049 **cell cycle**
* GO:0006974 **cellular response to DNA damage stimulus**
* GO:0008285 **negative regulation of cell proliferation**
* GO:0008283 **cell population proliferation**
* GO:0045123 **cellular extravasation / invasion** (as a proxy for local invasion; general)
* GO:0006955 **immune response**; GO:0045087 **innate immune response**

(These are suggested mechanism mappings; explicit GO annotations were not provided in the retrieved sources.)

### 4.4 Suggested Cell Ontology terms (examples)
* CL:0000066 **epithelial cell** (tumor origin)
* CL:0000624 **CD8-positive, alpha-beta T cell** (immune microenvironment)
* CL:0000235 **macrophage** (TME)

(Again, suggested mappings; CL identifiers are not explicitly stated in retrieved sources.)

---

## 5. Environmental information

### 5.1 Environmental/lifestyle factors
* Tobacco and alcohol exposure are repeatedly emphasized as major risk factors for hypopharyngeal/laryngeal cancers (sahu2023imagingrecommendationsfor pages 1-2).

### 5.2 Infectious agents
HPV appears to be relevant to a subset of non-oropharyngeal SCCs, but postcricoid-specific HPV prevalence was not extracted from the current evidence set.

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (subsite-relevant, evidence-based narrative)
1. **Chronic exposures/host susceptibility** (tobacco/alcohol carcinogens; iron deficiency and mucosal degeneration in PVS) predispose to squamous mucosal dysplasia and malignant transformation (sahu2023imagingrecommendationsfor pages 1-2, patil2023endoscopicsubmucosaldissection pages 2-4).
2. Tumor arises in a region with **propensity for submucosal spread**; imaging guidance notes postcricoid hypopharyngeal carcinoma can show **submucosal spread toward the cervical esophagus**, and MRI can better delineate extent (sahu2023imagingrecommendationsfor pages 5-8).
3. Progressive local growth leads to **dysphagia and airway/voice symptoms**, while deep spread and nodal metastasis drive advanced-stage presentation (sahu2023imagingrecommendationsfor pages 1-2, katano2024earlystagehypopharyngealsquamous pages 1-2).

### 6.2 Immune system involvement (current understanding)
The broader HNSCC literature emphasizes immune checkpoint biology (PD-1/PD-L1) as both a therapeutic target and part of immune evasion programs. TP53 alterations may intersect with immune-related tumor behaviors, and immune checkpoint inhibition is central in contemporary organ-preservation trials for hypopharyngeal cancer (shirima2024epithelial‑derivedheadand pages 3-4, NCT04156698 chunk 1).

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue localization
* **Primary site:** postcricoid region of the hypopharynx (anterior wall hypopharynx; mucosa over posterior cricoid cartilage) (glastonbury2020headandneck pages 1-2).

### 7.2 Suggested UBERON terms (examples)
* Hypopharynx: **UBERON:0001727** (suggested)
* Cricoid cartilage: **UBERON:0002379** (suggested)

(UBERON IDs are provided as suggested ontology mappings; explicit UBERON annotations were not contained in the retrieved text.)

### 7.3 Visual evidence for anatomy and subsite imaging
The Sahu 2023 imaging recommendations include CT figures of **normal hypopharynx anatomy** and imaging of **postcricoid-region cancer**, as well as TNM staging tables, supporting subsite localization and staging criteria (sahu2023imagingrecommendationsfor media 624946c3, sahu2023imagingrecommendationsfor media dd0e55cc, sahu2023imagingrecommendationsfor media 9d694104, sahu2023imagingrecommendationsfor media 0adf3cdb, sahu2023imagingrecommendationsfor media ea5671f7, sahu2023imagingrecommendationsfor media 2fc9a3ce).

---

## 8. Temporal development

### 8.1 Onset and progression
Hypopharyngeal SCC commonly presents late; early disease may be subtle. In the 2024 early-stage HSCC radiotherapy cohort: **“HSCC is often undetected until advanced stages”** and “**More than 50% of patients … present at an advanced stage**” (katano2024earlystagehypopharyngealsquamous pages 1-2).

### 8.2 Staging system
Staging follows **AJCC TNM for hypopharyngeal SCC**, with T descriptors incorporating extension/subsite involvement and invasion of structures including the **cricoid cartilage** (T4a) (sahu2023imagingrecommendationsfor pages 10-12).

---

## 9. Inheritance and population

### 9.1 Epidemiology (prioritizing 2024)
A 2024 GLOBOCAN 2020 analysis reported:
* **84,254 new cases** globally in 2020; **ASIR 0.91 per 100,000**.
* **38,599 deaths** in 2020; **ASMR 0.41 per 100,000**.
* **MIR 0.45**.
* Projected increases by 2040: **+50% new cases** and **+55% deaths** (mousavi2024globalepidemiologyand pages 1-2).

Subsite distribution of hypopharyngeal cancer reported in the same source: **~70% pyriform sinus, ~25% posterior pharyngeal wall, remainder largely post-cricoid** (mousavi2024globalepidemiologyand pages 1-2).

### 9.2 Sex and age distribution
Hypopharyngeal cancer shows higher incidence/mortality in men than women and increases with age (notably ≥70 years) (mousavi2024globalepidemiologyand pages 1-2, mousavi2024globalepidemiologyand pages 2-3).

---

## 10. Diagnostics

### 10.1 Clinical tests and imaging (guideline-style synthesis)
Imaging recommendations emphasize that endoscopy is essential for mucosal assessment but is insufficient for complete staging because submucosal and deep-space spread can be missed.

**NCCN-referenced diagnostic workup items (as quoted/compiled in Sahu 2023):**
* “examination under anesthesia with endoscopy”
* “CECT and/ or MRI for primary and neck”
* “Chest CT … for advanced nodal disease”
* “FDG PET-CT … for stage III-IV disease” (sahu2023imagingrecommendationsfor pages 1-2)

**Postcricoid-specific imaging note:** post-cricoid hypopharyngeal carcinoma is described as **uncommon** and “often shows submucosal spread toward the cervical esophagus,” with MRI better delineating extent (sahu2023imagingrecommendationsfor pages 5-8).

### 10.2 Histopathology
Squamous cell carcinoma is the predominant histology in hypopharyngeal cancer (mousavi2024globalepidemiologyand pages 1-2, li2026novellaryngealpreservation pages 1-2).

### 10.3 Biomarkers (current practice direction)
PD-1/PD-L1 axis is clinically actionable in HNSCC broadly and is integral to the modern immunotherapy-based organ-preservation strategies tested in hypopharyngeal cancer trials (NCT04156698 chunk 1, NCT06039631 chunk 1).

### 10.4 Differential diagnosis
Sahu 2023 notes non-squamous malignant lesions are rare and often submucosal; a full differential diagnosis list was not extracted in the current evidence set (sahu2023imagingrecommendationsfor pages 1-2).

---

## 11. Outcome / prognosis

### 11.1 Survival statistics from recent/authoritative studies
* Early-stage hypopharyngeal SCC treated with definitive RT (70 Gy/35 fractions) reported **5-year OS 80.7%**, and for the postcricoid subsite **5-year OS 100%** in a small subsite-stratified subset (katano2024earlystagehypopharyngealsquamous pages 1-2).
* For hypopharyngeal carcinoma treatment modality comparisons (retrospective): **5-year OS 59.7% (surgery-based therapy) vs 24.0% (definitive chemoradiotherapy)** (p<0.0001), and **5-year PFS 49.9% vs 22.6%** (p=0.0002) (lin2023survivalanalysesof pages 1-2).

### 11.2 Prognostic factors
Performance status (ECOG PS) was an independent OS risk factor in the early-stage RT cohort (HR 8.457) (katano2024earlystagehypopharyngealsquamous pages 1-2).

---

## 12. Treatment

### 12.1 Standard modalities (real-world implementation)
**Early stage:** single-modality RT or surgery; a uniform definitive RT approach of **70 Gy/35 fractions** with elective nodal irradiation is feasible with low high-grade toxicity in one modern series (katano2024earlystagehypopharyngealsquamous pages 1-2).

**Advanced disease:** multimodality management. Imaging recommendations summarize: “Early stage disease is treated with single modalities such as radiotherapy or surgery. Advanced disease is treated with multimodality of either chemoradiotherapy or surgery followed by adjuvant radiotherapy with or without concurrent chemotherapy.” (sahu2023imagingrecommendationsfor pages 1-2).

### 12.2 Surgery vs definitive CRT
A retrospective cohort comparing surgery-based therapy (SBT) vs definitive chemoradiotherapy (CRT) found significantly better survival with SBT overall; however, for some subgroups (e.g., T3/stage III) survival differences were less pronounced (lin2023survivalanalysesof pages 1-2).

### 12.3 Immunotherapy and organ-preservation developments (prioritizing 2023–2024)
**Key 2024 phase II trial (directly in hypopharyngeal SCC):**
* *Nature Communications* 2024 reports: “**This phase II trial aimed to determine the efficacy and safety of induction chemoimmunotherapy of camrelizumab plus modified TPF in locally advanced hypopharyngeal squamous cell carcinoma (LA HSCC) (NCT04156698).**” It reports ORR 82.4% and interim 2-year OS/PFS/LPR outcomes: **2-year OS 83.0%, PFS 77.1%, larynx preservation rate 70.0%** (sahu2023imagingrecommendationsfor media ea5671f7, NCT04156698 chunk 1).

**Ongoing 2023-start randomized phase II organ-preservation strategy (larynx/hypopharynx):**
* NCT06039631 (Fudan University; recruiting; start Aug 22, 2023) randomizes post-neoadjuvant chemoimmunotherapy patients to organ-preservation surgery vs concurrent chemoradiation (RT **70 Gy/35 fractions** plus weekly cisplatin in one arm), with **adjuvant toripalimab**; primary endpoint is **2-year PFS** and key secondary endpoints include larynx preservation rate and QoL (MDADI, VHI-10) (NCT06039631 chunk 1).

### 12.4 Suggested MAXO terms (examples)
* Radiotherapy **MAXO:0000016** (suggested)
* Chemotherapy **NCIT:C15986** (suggested)
* Surgery / surgical excision **MAXO:0000004** (suggested)
* Immune checkpoint inhibitor therapy **MAXO:0001527** (suggested)

(MAXO IDs are suggested; the retrieved sources do not contain explicit MAXO mappings.)

---

## 13. Prevention

### 13.1 Primary prevention
Risk-factor modification (tobacco/alcohol reduction) is implied by the strong risk-factor association described in clinical guidance (sahu2023imagingrecommendationsfor pages 1-2).

### 13.2 Secondary prevention (high-risk surveillance)
Plummer–Vinson syndrome is consistently described as carrying malignancy risk that warrants surveillance:
* PVS review abstract: “**the risk of malignancy warrants long-term surveillance**” (lo2019plummervinsonsyndromeimproving pages 1-2).
* A PVS-focused excerpt notes “**Surveillance endoscopy can be performed yearly, though no definitive recommendation exists**” (patil2023endoscopicsubmucosaldissection pages 2-4).

---

## 14. Other species / natural disease
No naturally occurring postcricoid-region cancer analogs in other species were identified in the retrieved evidence set.

---

## 15. Model organisms
No postcricoid-region–specific experimental animal models were identified in the retrieved evidence set; mechanistic studies are therefore typically extrapolated from broader HNSCC models (cell lines, xenografts/PDX), but this is a current evidence gap in this retrieval (afshari2023potentialalternativetherapeutic pages 1-2).

---

## Notes on evidence gaps and limitations
* Postcricoid-region–specific **molecular profiling**, **differential diagnosis**, and **model organism** literature were not retrieved at depth in this run; much of the molecular discussion necessarily relies on broader HNSCC/HSCC evidence (afshari2023potentialalternativetherapeutic pages 1-2, shirima2024epithelial‑derivedheadand pages 3-4).
* Several modern immunotherapy studies relevant to hypopharyngeal SCC exist beyond 2024; however, the highest-priority 2023–2024 organ-preservation chemoimmunotherapy trial evidence in this set is NCT04156698 / *Nature Communications* 2024 (NCT04156698 chunk 1).

---

## Key URLs (as retrieved)
* Mousavi et al., 2024 (Frontiers in Oncology; Sep 2024): https://doi.org/10.3389/fonc.2024.1398063 (mousavi2024globalepidemiologyand pages 1-2)
* Sahu et al., 2023 (Indian J Med Paediatr Oncol; Jan 2023): https://doi.org/10.1055/s-0042-1759504 (sahu2023imagingrecommendationsfor pages 1-2)
* Katano & Yamashita, 2024 (Eur Arch Otorhinolaryngol; May 2024): https://doi.org/10.1007/s00405-024-08722-w (katano2024earlystagehypopharyngealsquamous pages 1-2)
* Lin et al., 2023 (Frontiers in Oncology; Mar 2023): https://doi.org/10.3389/fonc.2023.1109417 (lin2023survivalanalysesof pages 1-2)
* Lo et al., 2019 (J Multidiscip Healthc; Jun 2019): https://doi.org/10.2147/jmdh.s180410 (lo2019plummervinsonsyndromeimproving pages 1-2)
* Patil et al., 2023 (J Digestive Endoscopy; Dec 2023): https://doi.org/10.1055/s-0042-1759510 (patil2023endoscopicsubmucosaldissection pages 1-2)
* NCT04156698: https://clinicaltrials.gov/study/NCT04156698 (NCT04156698 chunk 1)
* NCT06039631: https://clinicaltrials.gov/study/NCT06039631 (NCT06039631 chunk 1)



References

1. (glastonbury2020headandneck pages 1-2): Christine M. Glastonbury. Head and neck squamous cell cancer: approach to staging and surveillance. IDKD Springer Series, pages 215-222, Feb 2020. URL: https://doi.org/10.1007/978-3-030-38490-6\_17, doi:10.1007/978-3-030-38490-6\_17. This article has 46 citations.

2. (mousavi2024globalepidemiologyand pages 1-2): Seyed Ehsan Mousavi, Mehran Ilaghi, Yasaman Mirzazadeh, Alireza Mosavi Jarrahi, and Seyed Aria Nejadghaderi. Global epidemiology and socioeconomic correlates of hypopharyngeal cancer in 2020 and its projection to 2040: findings from globocan 2020. Frontiers in Oncology, Sep 2024. URL: https://doi.org/10.3389/fonc.2024.1398063, doi:10.3389/fonc.2024.1398063. This article has 13 citations.

3. (sahu2023imagingrecommendationsfor pages 5-8): Arpita Sahu, Abhishek Mahajan, Delnaz Palsetia, Richa Vaish, Sarbani Ghosh Laskar, Jyoti Kumar, Namita Kamath, Ashu Seith Bhalla, Diva Shah, Amit Sahu, Ujjwal Agarwal, Aditi Venkatesh, Suman Kumar Ankathi, Amit Janu, Vasundhara Patil, Tejas H. Kapadia, Munita Bal, Shwetabh Sinha, Kumar Prabhash, and A. K. Dcruz. Imaging recommendations for diagnosis, staging and management of larynx and hypopharynx cancer. Indian Journal of Medical and Paediatric Oncology, 44:054-065, Jan 2023. URL: https://doi.org/10.1055/s-0042-1759504, doi:10.1055/s-0042-1759504. This article has 15 citations.

4. (katano2024earlystagehypopharyngealsquamous pages 1-2): Atsuto Katano and Hideomi Yamashita. Early-stage hypopharyngeal squamous cell carcinoma treated with radical radiotherapy at a uniform dose of 70 gy in 35 fractions: a single-center study. European Archives of Oto-Rhino-Laryngology, 281:4401-4407, May 2024. URL: https://doi.org/10.1007/s00405-024-08722-w, doi:10.1007/s00405-024-08722-w. This article has 11 citations and is from a peer-reviewed journal.

5. (mousavi2024globalepidemiologyand pages 2-3): Seyed Ehsan Mousavi, Mehran Ilaghi, Yasaman Mirzazadeh, Alireza Mosavi Jarrahi, and Seyed Aria Nejadghaderi. Global epidemiology and socioeconomic correlates of hypopharyngeal cancer in 2020 and its projection to 2040: findings from globocan 2020. Frontiers in Oncology, Sep 2024. URL: https://doi.org/10.3389/fonc.2024.1398063, doi:10.3389/fonc.2024.1398063. This article has 13 citations.

6. (sahu2023imagingrecommendationsfor pages 1-2): Arpita Sahu, Abhishek Mahajan, Delnaz Palsetia, Richa Vaish, Sarbani Ghosh Laskar, Jyoti Kumar, Namita Kamath, Ashu Seith Bhalla, Diva Shah, Amit Sahu, Ujjwal Agarwal, Aditi Venkatesh, Suman Kumar Ankathi, Amit Janu, Vasundhara Patil, Tejas H. Kapadia, Munita Bal, Shwetabh Sinha, Kumar Prabhash, and A. K. Dcruz. Imaging recommendations for diagnosis, staging and management of larynx and hypopharynx cancer. Indian Journal of Medical and Paediatric Oncology, 44:054-065, Jan 2023. URL: https://doi.org/10.1055/s-0042-1759504, doi:10.1055/s-0042-1759504. This article has 15 citations.

7. (sahu2023imagingrecommendationsfor pages 2-3): Arpita Sahu, Abhishek Mahajan, Delnaz Palsetia, Richa Vaish, Sarbani Ghosh Laskar, Jyoti Kumar, Namita Kamath, Ashu Seith Bhalla, Diva Shah, Amit Sahu, Ujjwal Agarwal, Aditi Venkatesh, Suman Kumar Ankathi, Amit Janu, Vasundhara Patil, Tejas H. Kapadia, Munita Bal, Shwetabh Sinha, Kumar Prabhash, and A. K. Dcruz. Imaging recommendations for diagnosis, staging and management of larynx and hypopharynx cancer. Indian Journal of Medical and Paediatric Oncology, 44:054-065, Jan 2023. URL: https://doi.org/10.1055/s-0042-1759504, doi:10.1055/s-0042-1759504. This article has 15 citations.

8. (katano2024earlystagehypopharyngealsquamous pages 2-5): Atsuto Katano and Hideomi Yamashita. Early-stage hypopharyngeal squamous cell carcinoma treated with radical radiotherapy at a uniform dose of 70 gy in 35 fractions: a single-center study. European Archives of Oto-Rhino-Laryngology, 281:4401-4407, May 2024. URL: https://doi.org/10.1007/s00405-024-08722-w, doi:10.1007/s00405-024-08722-w. This article has 11 citations and is from a peer-reviewed journal.

9. (lin2023survivalanalysesof pages 1-2): Tian-Yun Lin, Tsung-Lun Lee, Yen-Bin Hsu, Shyh-Kuan Tai, Ling-Wei Wang, Muh-Hwa Yang, and Pen-Yuan Chu. Survival analyses of different treatment modalities and clinical stage for hypopharyngeal carcinoma. Frontiers in Oncology, Mar 2023. URL: https://doi.org/10.3389/fonc.2023.1109417, doi:10.3389/fonc.2023.1109417. This article has 10 citations.

10. (lin2023survivalanalysesof pages 2-3): Tian-Yun Lin, Tsung-Lun Lee, Yen-Bin Hsu, Shyh-Kuan Tai, Ling-Wei Wang, Muh-Hwa Yang, and Pen-Yuan Chu. Survival analyses of different treatment modalities and clinical stage for hypopharyngeal carcinoma. Frontiers in Oncology, Mar 2023. URL: https://doi.org/10.3389/fonc.2023.1109417, doi:10.3389/fonc.2023.1109417. This article has 10 citations.

11. (patil2023endoscopicsubmucosaldissection pages 1-2): Gaurav Patil, Amol Vadgaonkar, Ankit Dalal, Sanil Parekh, Animesh Shah, Poorva Haridas, Prajakta Gupte, Sehajad Vora, and Amit Maydeo. Endoscopic submucosal dissection for esophageal squamous cell high-grade dysplasia in a patient with plummer vinson syndrome. Journal of Digestive Endoscopy, 14:051-055, Dec 2023. URL: https://doi.org/10.1055/s-0042-1759510, doi:10.1055/s-0042-1759510. This article has 1 citations.

12. (lo2019plummervinsonsyndromeimproving pages 5-6): Kevin Bryan Lo, Jeri Albano, Naemat Sandhu, and Nellowe Candelario. Plummer-vinson syndrome: improving outcomes with a multidisciplinary approach. Journal of Multidisciplinary Healthcare, 12:471-477, Jun 2019. URL: https://doi.org/10.2147/jmdh.s180410, doi:10.2147/jmdh.s180410. This article has 35 citations and is from a peer-reviewed journal.

13. (patil2023endoscopicsubmucosaldissection pages 2-4): Gaurav Patil, Amol Vadgaonkar, Ankit Dalal, Sanil Parekh, Animesh Shah, Poorva Haridas, Prajakta Gupte, Sehajad Vora, and Amit Maydeo. Endoscopic submucosal dissection for esophageal squamous cell high-grade dysplasia in a patient with plummer vinson syndrome. Journal of Digestive Endoscopy, 14:051-055, Dec 2023. URL: https://doi.org/10.1055/s-0042-1759510, doi:10.1055/s-0042-1759510. This article has 1 citations.

14. (lo2019plummervinsonsyndromeimproving pages 2-3): Kevin Bryan Lo, Jeri Albano, Naemat Sandhu, and Nellowe Candelario. Plummer-vinson syndrome: improving outcomes with a multidisciplinary approach. Journal of Multidisciplinary Healthcare, 12:471-477, Jun 2019. URL: https://doi.org/10.2147/jmdh.s180410, doi:10.2147/jmdh.s180410. This article has 35 citations and is from a peer-reviewed journal.

15. (NCT04156698 chunk 1):  Induction Chemotherapy Combined With Immunotherapy for Locally Advanced Hypopharyngeal Carcinoma. Eye & ENT Hospital of Fudan University. 2020. ClinicalTrials.gov Identifier: NCT04156698

16. (NCT06039631 chunk 1): Yu Wang. Neoadjuvant Chemoimmunotherapy Followed By Radiation Or Organ Preservation Surgery In Laryngeal/Hypopharyngeal Cancer. Fudan University. 2023. ClinicalTrials.gov Identifier: NCT06039631

17. (OpenTargets Search: hypopharyngeal carcinoma,head and neck squamous cell carcinoma): Open Targets Query (hypopharyngeal carcinoma,head and neck squamous cell carcinoma, 13 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

18. (li2026novellaryngealpreservation pages 1-2): Xuexin Li, Xiaoran Zhang, Yun Lin, Yan Ma, Zheng Jiang, Dapeng Lei, Xinliang Pan, and Jun Liu. Novel laryngeal preservation technique in postcricoid hypopharyngeal carcinoma: a case-series study. BMC Surgery, Mar 2026. URL: https://doi.org/10.1186/s12893-026-03586-9, doi:10.1186/s12893-026-03586-9. This article has 0 citations and is from a peer-reviewed journal.

19. (lo2019plummervinsonsyndromeimproving pages 1-2): Kevin Bryan Lo, Jeri Albano, Naemat Sandhu, and Nellowe Candelario. Plummer-vinson syndrome: improving outcomes with a multidisciplinary approach. Journal of Multidisciplinary Healthcare, 12:471-477, Jun 2019. URL: https://doi.org/10.2147/jmdh.s180410, doi:10.2147/jmdh.s180410. This article has 35 citations and is from a peer-reviewed journal.

20. (NCT06957938 chunk 2): Yu Wang. Comparing Neoadjuvant Chemotherapy Combined With PD-1 Inhibitor Versus Neoadjuvant Chemotherapy in Locally Advanced Laryngeal and Hypopharyngeal Carcinoma. Fudan University. 2025. ClinicalTrials.gov Identifier: NCT06957938

21. (shirima2024epithelial‑derivedheadand pages 3-4): Charles Shirima, Coralia Bleotu, Demetrios Spandidos, Adel El‑Naggar, Gratiela Gradisteanu Pircalabioru, and Ioannis Michalopoulos. Epithelial‑derived head and neck squamous tumourigenesis (review). Oncology Reports, Aug 2024. URL: https://doi.org/10.3892/or.2024.8800, doi:10.3892/or.2024.8800. This article has 12 citations and is from a peer-reviewed journal.

22. (afshari2023potentialalternativetherapeutic pages 1-2): Keihan Afshari and Karpal Singh Sohal. Potential alternative therapeutic modalities for management head and neck squamous cell carcinoma: a review. Cancer Control : Journal of the Moffitt Cancer Center, Apr 2023. URL: https://doi.org/10.1177/10732748231185003, doi:10.1177/10732748231185003. This article has 13 citations.

23. (sahu2023imagingrecommendationsfor media 624946c3): Arpita Sahu, Abhishek Mahajan, Delnaz Palsetia, Richa Vaish, Sarbani Ghosh Laskar, Jyoti Kumar, Namita Kamath, Ashu Seith Bhalla, Diva Shah, Amit Sahu, Ujjwal Agarwal, Aditi Venkatesh, Suman Kumar Ankathi, Amit Janu, Vasundhara Patil, Tejas H. Kapadia, Munita Bal, Shwetabh Sinha, Kumar Prabhash, and A. K. Dcruz. Imaging recommendations for diagnosis, staging and management of larynx and hypopharynx cancer. Indian Journal of Medical and Paediatric Oncology, 44:054-065, Jan 2023. URL: https://doi.org/10.1055/s-0042-1759504, doi:10.1055/s-0042-1759504. This article has 15 citations.

24. (sahu2023imagingrecommendationsfor media dd0e55cc): Arpita Sahu, Abhishek Mahajan, Delnaz Palsetia, Richa Vaish, Sarbani Ghosh Laskar, Jyoti Kumar, Namita Kamath, Ashu Seith Bhalla, Diva Shah, Amit Sahu, Ujjwal Agarwal, Aditi Venkatesh, Suman Kumar Ankathi, Amit Janu, Vasundhara Patil, Tejas H. Kapadia, Munita Bal, Shwetabh Sinha, Kumar Prabhash, and A. K. Dcruz. Imaging recommendations for diagnosis, staging and management of larynx and hypopharynx cancer. Indian Journal of Medical and Paediatric Oncology, 44:054-065, Jan 2023. URL: https://doi.org/10.1055/s-0042-1759504, doi:10.1055/s-0042-1759504. This article has 15 citations.

25. (sahu2023imagingrecommendationsfor media 9d694104): Arpita Sahu, Abhishek Mahajan, Delnaz Palsetia, Richa Vaish, Sarbani Ghosh Laskar, Jyoti Kumar, Namita Kamath, Ashu Seith Bhalla, Diva Shah, Amit Sahu, Ujjwal Agarwal, Aditi Venkatesh, Suman Kumar Ankathi, Amit Janu, Vasundhara Patil, Tejas H. Kapadia, Munita Bal, Shwetabh Sinha, Kumar Prabhash, and A. K. Dcruz. Imaging recommendations for diagnosis, staging and management of larynx and hypopharynx cancer. Indian Journal of Medical and Paediatric Oncology, 44:054-065, Jan 2023. URL: https://doi.org/10.1055/s-0042-1759504, doi:10.1055/s-0042-1759504. This article has 15 citations.

26. (sahu2023imagingrecommendationsfor media 0adf3cdb): Arpita Sahu, Abhishek Mahajan, Delnaz Palsetia, Richa Vaish, Sarbani Ghosh Laskar, Jyoti Kumar, Namita Kamath, Ashu Seith Bhalla, Diva Shah, Amit Sahu, Ujjwal Agarwal, Aditi Venkatesh, Suman Kumar Ankathi, Amit Janu, Vasundhara Patil, Tejas H. Kapadia, Munita Bal, Shwetabh Sinha, Kumar Prabhash, and A. K. Dcruz. Imaging recommendations for diagnosis, staging and management of larynx and hypopharynx cancer. Indian Journal of Medical and Paediatric Oncology, 44:054-065, Jan 2023. URL: https://doi.org/10.1055/s-0042-1759504, doi:10.1055/s-0042-1759504. This article has 15 citations.

27. (sahu2023imagingrecommendationsfor media ea5671f7): Arpita Sahu, Abhishek Mahajan, Delnaz Palsetia, Richa Vaish, Sarbani Ghosh Laskar, Jyoti Kumar, Namita Kamath, Ashu Seith Bhalla, Diva Shah, Amit Sahu, Ujjwal Agarwal, Aditi Venkatesh, Suman Kumar Ankathi, Amit Janu, Vasundhara Patil, Tejas H. Kapadia, Munita Bal, Shwetabh Sinha, Kumar Prabhash, and A. K. Dcruz. Imaging recommendations for diagnosis, staging and management of larynx and hypopharynx cancer. Indian Journal of Medical and Paediatric Oncology, 44:054-065, Jan 2023. URL: https://doi.org/10.1055/s-0042-1759504, doi:10.1055/s-0042-1759504. This article has 15 citations.

28. (sahu2023imagingrecommendationsfor media 2fc9a3ce): Arpita Sahu, Abhishek Mahajan, Delnaz Palsetia, Richa Vaish, Sarbani Ghosh Laskar, Jyoti Kumar, Namita Kamath, Ashu Seith Bhalla, Diva Shah, Amit Sahu, Ujjwal Agarwal, Aditi Venkatesh, Suman Kumar Ankathi, Amit Janu, Vasundhara Patil, Tejas H. Kapadia, Munita Bal, Shwetabh Sinha, Kumar Prabhash, and A. K. Dcruz. Imaging recommendations for diagnosis, staging and management of larynx and hypopharynx cancer. Indian Journal of Medical and Paediatric Oncology, 44:054-065, Jan 2023. URL: https://doi.org/10.1055/s-0042-1759504, doi:10.1055/s-0042-1759504. This article has 15 citations.

29. (sahu2023imagingrecommendationsfor pages 10-12): Arpita Sahu, Abhishek Mahajan, Delnaz Palsetia, Richa Vaish, Sarbani Ghosh Laskar, Jyoti Kumar, Namita Kamath, Ashu Seith Bhalla, Diva Shah, Amit Sahu, Ujjwal Agarwal, Aditi Venkatesh, Suman Kumar Ankathi, Amit Janu, Vasundhara Patil, Tejas H. Kapadia, Munita Bal, Shwetabh Sinha, Kumar Prabhash, and A. K. Dcruz. Imaging recommendations for diagnosis, staging and management of larynx and hypopharynx cancer. Indian Journal of Medical and Paediatric Oncology, 44:054-065, Jan 2023. URL: https://doi.org/10.1055/s-0042-1759504, doi:10.1055/s-0042-1759504. This article has 15 citations.
