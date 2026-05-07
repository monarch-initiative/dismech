---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T19:31:20.373788'
end_time: '2026-05-07T19:42:51.902600'
duration_seconds: 691.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Motor and Sensory Axonal Neuropathy
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Motor and Sensory Axonal Neuropathy
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Acute Motor and Sensory Axonal Neuropathy** covering all of the
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
- **Disease Name:** Acute Motor and Sensory Axonal Neuropathy
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Acute Motor and Sensory Axonal Neuropathy** covering all of the
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


# Acute Motor and Sensory Axonal Neuropathy (AMSAN) — Comprehensive Disease Characteristics Report

**Target disease:** Acute motor and sensory axonal neuropathy (AMSAN) (autoimmune; acute post-infectious immune-mediated peripheral neuropathy; axonal Guillain–Barré syndrome (GBS) variant). (shang2021axonalvariantsof pages 1-2)

**High-level definition (current understanding):** AMSAN is an **axonal** form of GBS with acute involvement of **motor and sensory axons**, typically presenting with rapidly progressive limb weakness plus sensory loss/paresthesia and areflexia/hyporeflexia, often after an infectious trigger. (shang2021axonalvariantsof pages 1-2, leonhard2024guillain–barrésyndrome pages 1-3)

**Key abstract-quoted definition (GBS umbrella):** Nature Reviews Disease Primers (published **2024-12-19**) states: “**Guillain–Barré syndrome (GBS) is a rare immune-mediated polyradiculoneuropathy**” and notes that “Diagnosis is based on clinical features, supported by cerebrospinal fluid analysis and nerve conduction studies.” (leonhard2024guillain–barrésyndrome pages 1-3)

---

## 1. Disease Information

### 1.1 Overview
AMSAN is a GBS subtype within “axonal variants” (primarily **AMAN** and **AMSAN**). AMSAN differs from AMAN by having prominent sensory axonal involvement in addition to motor axonal injury. (shang2021axonalvariantsof pages 1-2)

### 1.2 Key identifiers / ontology mappings (availability in retrieved sources)
The retrieved literature focused on GBS and axonal variants but **did not provide a specific MONDO ID or Orphanet code for AMSAN**.

**ICD (from real-world claims-based definitions for GBS):**
- GBS was defined using **ICD-9 357.0** and **ICD-10 G61.0, G65.0** in a US prescribing-patterns study. (stino2024intravenousimmunoglobulinand pages 1-2)

**MeSH / MONDO / Orphanet / OMIM:** not explicitly stated in the retrieved texts; thus not reliably reportable here.

### 1.3 Synonyms / alternative names
- “Acute motor-sensory axonal polyneuropathy” (used as a synonym in case literature). (geng2023acutemotorsensoryaxonal pages 3-5)
- “Axonal Guillain–Barré syndrome” (umbrella term encompassing AMAN/AMSAN). (umar2024complexneurologicalsequelae pages 4-6, shang2021axonalvariantsof pages 1-2)

### 1.4 Evidence source type
Most disease-level statements here are derived from **aggregated disease resources and reviews** (e.g., Nature Reviews Disease Primers; axonal GBS update review; Campylobacter–ganglioside review), supplemented by **human clinical case reports** illustrating AMSAN phenotypes/triggers and treatment response. (leonhard2024guillain–barrésyndrome pages 1-3, shang2021axonalvariantsof pages 1-2, latov2022campylobacterjejuniinfection pages 1-2, geng2023acutemotorsensoryaxonal pages 3-5)

---

## 2. Etiology

### 2.1 Primary causal factors (mechanistic etiology)
**Post-infectious autoimmunity via molecular mimicry** is the leading paradigm for axonal GBS/AMSAN, particularly in Campylobacter jejuni–associated disease. (shang2021axonalvariantsof pages 1-2, latov2022campylobacterjejuniinfection pages 1-2, leonhard2024guillain–barrésyndrome pages 1-3)

**Abstract quote (Campylobacter–GBS link; published 2022-10-28):** Latov writes: “**Preceding infection with Campylobacter jejuni (Cj) occurs in approximately 30% of patients with Guillain–Barre syndrome (GBS), and the risk of GBS following Cj infection is increased by 77 to 100-fold. GBS is most often of the axonal subtype and is thought to be mediated by IgG antibodies to peripheral nerve gangliosides** … induced by molecular mimicry.” (latov2022campylobacterjejuniinfection pages 1-2)

### 2.2 Risk factors
**Infectious triggers (human clinical + epidemiologic evidence):**
- **Campylobacter jejuni enteritis**: strong epidemiologic association and mechanistic evidence via ganglioside mimicry. (latov2022campylobacterjejuniinfection pages 1-2, leonhard2024guillain–barrésyndrome pages 1-3)
- **Viral and other infectious triggers** reported for axonal variants include Zika and other pathogens in review summaries; case literature also reports post–COVID-19 AMSAN. (shang2021axonalvariantsof pages 1-2, geng2023acutemotorsensoryaxonal pages 3-5)

**Timing after diarrheal illness:** in C. jejuni–associated GBS, neurological symptoms “usually begin at **10 days to 3 weeks** after the onset of diarrhea.” (latov2022campylobacterjejuniinfection pages 1-2)

**COVID-19 association (case-level, mechanistic hypotheses):** AMSAN has been described following SARS-CoV-2 infection, with proposed mechanisms including molecular mimicry and hyperinflammatory para-infectious immune injury; anti-ganglioside antibodies may be absent in some cases. (geng2023acutemotorsensoryaxonal pages 3-5, geng2023acutemotorsensoryaxonal pages 5-6)

### 2.3 Protective factors
No specific protective genetic variants, environmental protective factors, or proven preventive interventions for AMSAN were identified in the retrieved sources.

### 2.4 Gene–environment interactions
The retrieved sources emphasize infection-triggered autoimmunity and mention “host genetic predisposition” as an important research direction in GBS broadly, but **do not provide validated AMSAN-specific gene–environment interaction loci**. (shang2021axonalvariantsof pages 1-2)

---

## 3. Phenotypes (clinical features)

### 3.1 Core phenotype spectrum (suggested HPO terms)
AMSAN typically includes:
- Acute/subacute **limb weakness** (often symmetric), progressing over days (HP:0001324 Muscle weakness; HP:0003674 Motor delay/impairment not specific; consider HP:0003323 Progressive muscular weakness).
- **Areflexia/hyporeflexia** (HP:0001284 Areflexia). (leonhard2024guillain–barrésyndrome pages 1-3)
- **Sensory symptoms** (paresthesia, sensory loss) (HP:0003401 Paresthesia; HP:0000763 Sensory neuropathy). (leonhard2024guillain–barrésyndrome pages 1-3, geng2023acutemotorsensoryaxonal pages 3-5)
- **Pain** (HP:0012531 Pain). (leonhard2024guillain–barrésyndrome pages 1-3)
- **Cranial nerve involvement** may occur in severe GBS phenotypes (facial palsy, bulbar weakness) (HP:0001343 Facial palsy; HP:0002493 Dysphagia). (leonhard2024guillain–barrésyndrome pages 1-3)
- **Autonomic dysfunction** in severe cases (HP:0001278 Orthostatic hypotension; HP:0002013 Vomiting; broader: dysautonomia). (busl2023guidelinesforneuroprognostication pages 1-3, umar2024complexneurologicalsequelae pages 4-6)
- **Respiratory failure / need for ventilation** in severe cases (HP:0002878 Respiratory failure; HP:0002094 Dyspnea). (leonhard2024guillain–barrésyndrome pages 1-3)

### 3.2 Onset and progression
GBS (including AMSAN) is characterized by rapid progression with a typical nadir within weeks. Neurocritical Care guidelines note symptoms reach maximum “within **2–4 weeks**.” (busl2023guidelinesforneuroprognostication pages 1-3)

### 3.3 Frequency among affected individuals (data availability)
Phenotype frequencies are best described for GBS overall rather than AMSAN specifically in the retrieved sources:
- “Around **20% of patients** may develop weakness in all four limbs … and respiratory failure requiring mechanical ventilation.” (leonhard2024guillain–barrésyndrome pages 1-3)

### 3.4 Quality-of-life impact
Nature Reviews Disease Primers emphasizes residual disability: “~**20%** of patients who received treatment are **unable to walk after 6 months**.” (leonhard2024guillain–barrésyndrome pages 1-3)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes
AMSAN is **not** a monogenic disorder in standard clinical framing; the retrieved sources do not identify causal genes or OMIM disease entries specific to AMSAN. (leonhard2024guillain–barrésyndrome pages 1-3, shang2021axonalvariantsof pages 1-2)

### 4.2 Key molecular targets (autoantigens)
Gangliosides on peripheral nerves are key immune targets in axonal GBS/AMSAN:
- Anti-ganglioside antibodies reported in association with AMSAN include **anti-GM1, anti-GM1b, anti-GD1a**. (shang2021axonalvariantsof pages 6-7)

### 4.3 Pathogenic “variants” (not applicable)
Pathogenic DNA variants are not established as causal for AMSAN in the provided evidence.

### 4.4 Epigenetics / chromosomal abnormalities
Not established for AMSAN in the retrieved sources.

---

## 5. Environmental Information

### 5.1 Infectious agents (key environmental triggers)
- **Campylobacter jejuni** is the best-supported trigger for axonal GBS/AMSAN. (latov2022campylobacterjejuniinfection pages 1-2, leonhard2024guillain–barrésyndrome pages 1-3)
- **SARS-CoV-2** has been associated with AMSAN in case literature, with immune-mediated mechanisms proposed. (geng2023acutemotorsensoryaxonal pages 3-5, geng2023acutemotorsensoryaxonal pages 5-6)

### 5.2 Lifestyle/occupational factors
No AMSAN-specific lifestyle protective/risk factors were established in the retrieved sources.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (upstream → downstream)
**Upstream trigger:** infection (especially C. jejuni; also viral triggers). (latov2022campylobacterjejuniinfection pages 1-2, leonhard2024guillain–barrésyndrome pages 1-3)

**Immune priming via molecular mimicry:** bacterial lipooligosaccharides mimic peripheral nerve gangliosides, producing cross-reactive antibodies. Nature Reviews Disease Primers explicitly summarizes: “For example, in patients with preceding *Campylobacter jejuni* infection, **molecular mimicry causes a cross-reactive antibody response to nerve gangliosides**.” (leonhard2024guillain–barrésyndrome pages 1-3)

**Effector injury:** anti-ganglioside antibodies activate complement at nodes/paranodes and axolemma, causing conduction failure and structural axonal injury/degeneration (axonal variants). (leonhard2024guillain–barrésyndrome pages 5-7, latov2022campylobacterjejuniinfection pages 2-4)

**Downstream clinical manifestations:** reduced compound muscle action potentials (CMAPs), sensory nerve action potential (SNAP) abnormalities, weakness + sensory loss, and in severe cases bulbar/respiratory/autonomic failure. (geng2023acutemotorsensoryaxonal pages 3-5, leonhard2024guillain–barrésyndrome pages 1-3)

### 6.2 Immune system involvement
- Axonal variants are associated with anti-ganglioside antibodies and complement-dependent mechanisms; Latov describes that GBS axonal subtype is “thought to be mediated by **IgG antibodies** to peripheral nerve gangliosides” cross-reactive with C. jejuni components. (latov2022campylobacterjejuniinfection pages 1-2)

### 6.3 Suggested GO biological process terms (mechanism-oriented)
- GO:0006956 **complement activation**
- GO:0006955 **immune response**
- GO:0002250 **adaptive immune response**
- GO:0042113 **B cell activation**
- GO:0007166 **cell surface receptor signaling pathway** (broad)

### 6.4 Suggested Cell Ontology terms (CL)
- CL:0000945 **B cell**
- CL:0000084 **T cell**
- CL:0000235 **macrophage**
- CL:0000584 **Schwann cell** (peripheral glia; mechanistic relevance to peripheral nerves broadly)

### 6.5 Molecular profiling / biomarkers (availability)
The retrieved sources highlight a **lack of specific biomarkers** for GBS broadly (including axonal variants). (leonhard2024guillain–barrésyndrome pages 1-3)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- **Peripheral nervous system** (peripheral nerves and roots; polyradiculoneuropathy). (leonhard2024guillain–barrésyndrome pages 1-3)

### 7.2 Tissue/cell level (suggested UBERON terms)
- UBERON:0000010 **peripheral nerve**
- UBERON:0001021 **spinal nerve root**

### 7.3 Subcellular (suggested GO Cellular Component)
- GO:0033267 **axon part**
- GO:0043209 **myelin sheath** (even in “axonal” variants, nerve architecture is involved)
- GO:0030054 **cell junction** (node/paranode microdomains; mechanistic target region) (leonhard2024guillain–barrésyndrome pages 5-7)

---

## 8. Temporal Development

### 8.1 Onset pattern
Acute onset with rapid progression; nadir typically within **2–4 weeks** in GBS overall. (busl2023guidelinesforneuroprognostication pages 1-3)

### 8.2 Course
Typically monophasic: Nature Reviews Disease Primers states “GBS is usually a **monophasic disease**.” (leonhard2024guillain–barrésyndrome pages 1-3)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
Data are primarily for GBS overall; AMSAN-specific incidence is not provided in the retrieved evidence.

- GBS annual global incidence “**1–2 per 100,000 persons per year**.” (leonhard2024guillain–barrésyndrome pages 1-3)
- Axonal-variants review provides a similar range: **0.81–1.89 per 100,000/year**. (shang2021axonalvariantsof pages 1-2)
- Sex/age: males affected ~**1.5×** more than females; risk rises ~**20% per decade** of age. (leonhard2024guillain–barrésyndrome pages 1-3)

### 9.2 Population differences (axonal variants)
Axonal variants (including AMSAN) are discussed as having geographic variability, with higher representation in some regions (review-level). (restrepojimenez2018theimmunotherapyof pages 46-47)

---

## 10. Diagnostics

### 10.1 Diagnostic approach (real-world implementation)
GBS diagnosis is “based on clinical features, supported by cerebrospinal fluid analysis and nerve conduction studies.” (leonhard2024guillain–barrésyndrome pages 1-3)

**CSF:**
- Axonal-variants review: CSF albuminocytologic dissociation is a hallmark “detectable in almost **90%**,” with CSF albumin rising from week 2 and present in ~**70%** by the end of week 2. (shang2021axonalvariantsof pages 1-2)

**Electrophysiology (NCS/EMG):**
- Axonal variants: early studies can be misleading; decreased CMAP amplitudes and reversible conduction failure/block can appear early; electrophysiology “more reliable” at **3–6 weeks** than at 1–2 weeks. (shang2021axonalvariantsof pages 1-2)
- Nature Reviews Disease Primers emphasizes heterogeneity: mixed axonal–demyelinating or even normal NCS can occur, limiting strict NCS-only subclassification. (leonhard2024guillain–barrésyndrome pages 4-5)

**Serology (supportive, not required for all):**
Anti-ganglioside antibodies support axonal subtype classification (anti-GM1/anti-GD1a and related), but seronegative axonal cases exist. (shang2021axonalvariantsof pages 6-7, geng2023acutemotorsensoryaxonal pages 5-6)

### 10.2 Differential diagnosis (high-level)
- Acute onset CIDP (A-CIDP) is clinically challenging and can lead to reclassification; this carries therapeutic implications. (stino2024intravenousimmunoglobulinand pages 1-2)

---

## 11. Outcome / Prognosis

### 11.1 Key outcome statistics (GBS overall)
Nature Reviews Disease Primers reports: “~**20%** of patients who received treatment are unable to walk after **6 months** and ~**5% die** as a consequence of GBS.” (leonhard2024guillain–barrésyndrome pages 1-3)

Neurocritical Care neuroprognostication guidelines provide ICU-relevant statistics:
- “**10–30%** require mechanical ventilation during the acute phase.” (busl2023guidelinesforneuroprognostication pages 1-3)
- Mortality “range between **1 and 13%**,” with “mortality rates up to **20%**” among ventilated patients. (busl2023guidelinesforneuroprognostication pages 1-3)

### 11.2 Prognostic tools / expert consensus
Busl et al. recommend:
- **EGRIS** (Erasmus GBS Respiratory Insufficiency Score) for predicting ventilation, and
- **EGOS / modified EGOS** for predicting independent ambulation at 3 months and beyond. (busl2023guidelinesforneuroprognostication pages 1-3)

---

## 12. Treatment

### 12.1 Standard of care
**Only proven effective disease-modifying treatments for GBS (including AMSAN) remain:**
- **Intravenous immunoglobulin (IVIg)**
- **Plasma exchange (PE/PLEX)** (leonhard2024guillain–barrésyndrome pages 1-3)

Nature Reviews Disease Primers (2024) abstract quote: “Effective treatments include plasma exchange and intravenous immunoglobulins.” (leonhard2024guillain–barrésyndrome pages 1-3)

### 12.2 Treatment strategy and common pitfalls (guidelines + evidence)
A US real-world analysis emphasizes trials showing no benefit from:
- **Repeat IVIG dosing** and
- **PLEX followed by IVIG (combination therapy)** in non-responders. (stino2024intravenousimmunoglobulinand pages 1-2)

**Abstract quote (real-world utilization; published 2024-09):** Stino et al. state: “Randomized controlled trials show that **repeat IVIG dosing and … combination therapy have no additional therapeutic benefit** in Guillain-Barre Syndrome (GBS) non-responders.” (stino2024intravenousimmunoglobulinand pages 1-2)

### 12.3 Recent developments (2023–2024) — complement inhibition (eculizumab)
A key 2024 development is a **phase 3 randomized trial** of **eculizumab** (C5 inhibitor) added to IVIg in severe GBS.

**Abstract quote (published 2024-07; J Peripher Nerv Syst):** “This study evaluated the efficacy and safety of **eculizumab add-on therapy to IVIg** … in patients with severe GBS.” (kuwabara2024efficacyandsafety pages 1-2)

**Results:**
- Primary endpoint not met (time to Hughes FG ≤1): HR **0.9**, 95% CI 0.45–1.97; **p = 0.89**. (kuwabara2024efficacyandsafety pages 1-2)
- Strong target engagement: serum free C5 reduced by **99.99% at 1 hour** postdose and sustained to week 5. (kuwabara2024efficacyandsafety pages 1-2)

### 12.4 MAXO (Medical Action Ontology) suggestions
- MAXO:0000412 **intravenous immunoglobulin therapy**
- MAXO:0000756 **therapeutic plasma exchange**
- MAXO:0000610 **mechanical ventilation** (for respiratory failure)
- MAXO:0000571 **physical therapy / rehabilitation** (supportive)

---

## 13. Prevention

No established primary-prevention intervention is specific to AMSAN beyond prevention/management of infectious triggers at the population level.

**Vaccine-associated GBS (broader context):** The retrieved evidence supports ongoing pharmacovigilance and risk assessment for GBS after vaccination, but does not provide AMSAN-specific prevention guidance. (shang2021axonalvariantsof pages 1-2)

---

## 14. Other Species / Natural Disease

Direct naturally occurring AMSAN analogs in non-human species were not identified in the retrieved sources.

---

## 15. Model Organisms

**Experimental autoimmune neuritis and anti-ganglioside models (mechanistic relevance):** Latov reports animal models in which rabbits immunized with GM1 or C. jejuni LPS develop acute axonal neuropathy with anti-GM1 antibodies, supporting the antibody-mediated mechanism relevant to axonal GBS/AMSAN. (latov2022campylobacterjejuniinfection pages 2-4)

---

# 2023–2024 “latest research” highlights (prioritized)

1. **2024 authoritative synthesis:** Nature Reviews Disease Primers (Leonhard et al.; **2024-12-19**) consolidates contemporary consensus on GBS triggers, diagnosis (CSF + NCS), treatment (IVIg/PE), and residual disability (20% non-ambulant at 6 months; ~5% mortality). (leonhard2024guillain–barrésyndrome pages 1-3)
2. **2024 mechanism-directed therapy trial:** Phase 3 add-on **eculizumab** to IVIg did not improve functional recovery despite robust complement suppression, suggesting complement blockade alone is insufficient or that patient selection/timing remain unresolved. (kuwabara2024efficacyandsafety pages 1-2)
3. **2024 real-world implementation gap:** A US claims-based cohort (2001–2018) found repeat IVIG use (**39.7%**) and combination therapy (**6.1%**) persisted, despite RCT evidence against these approaches in non-responders; diagnostic reclassification to CIDP occurred in **32%**. (stino2024intravenousimmunoglobulinand pages 1-2)

---

## Evidence summary table

| Domain | Evidence summary | Key quantitative stats (with values) | Primary source (first author, year, journal) | PMID if available | URL | Context citation ID |
|---|---|---|---|---|---|---|
| Definition | AMSAN is an axonal Guillain-Barré syndrome (GBS) subtype characterized by acute motor and sensory axonal involvement; axonal GBS variants include AMAN and AMSAN. GBS is an acute, immune-mediated polyradiculoneuropathy with rapidly progressive weakness and sensory deficits. | Global GBS incidence: 1–2/100,000/year; males affected ~1.5× more often; risk rises ~20% per decade of age. | Leonhard, 2024, Nature Reviews Disease Primers |  | https://doi.org/10.1038/s41572-024-00580-4 | (leonhard2024guillain–barrésyndrome pages 1-3, shang2021axonalvariantsof pages 1-2) |
| Triggers | AMSAN is usually post-infectious, with Campylobacter jejuni the best-supported trigger; COVID-19, chikungunya, and other infections have also been reported as antecedents in axonal GBS/AMSAN cases. Molecular mimicry between microbial glycans and nerve gangliosides is the leading mechanism. | Preceding C. jejuni in ~30% of GBS; GBS risk after C. jejuni infection increased 77–100-fold; neurologic symptoms usually begin 10 days to 3 weeks after diarrhea. | Latov, 2022, Microorganisms |  | https://doi.org/10.3390/microorganisms10112139 | (latov2022campylobacterjejuniinfection pages 1-2, latov2022campylobacterjejuniinfection pages 2-4, geng2023acutemotorsensoryaxonal pages 3-5) |
| Autoantibodies | Axonal GBS including AMSAN is associated most often with anti-ganglioside antibodies, particularly anti-GM1, anti-GM1b, and anti-GD1a. Antibodies are often IgG1/IgG3 subclasses and can cross-react with C. jejuni lipooligosaccharides. | Anti-ganglioside antibodies reported in 41–85% of GBS following C. jejuni infection. | Shang, 2021, Journal of Neurology |  | https://doi.org/10.1007/s00415-020-09742-2 | (shang2021axonalvariantsof pages 6-7, latov2022campylobacterjejuniinfection pages 2-4, latov2022campylobacterjejuniinfection pages 1-2) |
| Pathophysiology | The best-supported causal chain is infection → molecular mimicry → anti-ganglioside antibody generation → complement activation at nodes/paranodes/axolemma → conduction failure and axonal degeneration. Pathology in axonal GBS shows antibody/complement deposition on axolemma and macrophage-associated axonal injury. | Serum C5 in the eculizumab phase 3 trial was reduced by 99.99% 1 hour post-dose and remained suppressed through week 5, showing effective target engagement. | Latov, 2022, Microorganisms |  | https://doi.org/10.3390/microorganisms10112139 | (latov2022campylobacterjejuniinfection pages 2-4, leonhard2024guillain–barrésyndrome pages 5-7, kuwabara2024efficacyandsafety pages 1-2) |
| Diagnostics | Diagnosis is primarily clinical and supported by CSF and electrophysiology. For axonal variants, serial NCS/EMG are important because early studies may show reduced CMAPs, reversible conduction failure/block, or equivocal findings; CSF albuminocytologic dissociation is common but may lag. | CSF albuminocytologic dissociation in almost 90%; CSF protein elevated in ~70% by end of week 2; electrophysiology more reliable at 3–6 weeks than 1–2 weeks. | Shang, 2021, Journal of Neurology |  | https://doi.org/10.1007/s00415-020-09742-2 | (shang2021axonalvariantsof pages 1-2, busl2023guidelinesforneuroprognostication pages 1-3, leonhard2024guillain–barrésyndrome pages 1-3) |
| Prognosis | Axonal GBS/AMSAN generally has a more severe course and slower recovery than demyelinating GBS. Across GBS, respiratory failure, bulbar weakness, and severe nadir disability are major poor prognostic features; EGOS and EGRIS are used for outcome and ventilation risk prediction. | 10–30% require mechanical ventilation; ~20% of treated GBS patients cannot walk at 6 months; ~5% die; mortality can reach up to 20% among ventilated patients. | Busl, 2023, Neurocritical Care |  | https://doi.org/10.1007/s12028-023-01707-3 | (busl2023guidelinesforneuroprognostication pages 1-3, leonhard2024guillain–barrésyndrome pages 1-3, umar2024complexneurologicalsequelae pages 4-6) |
| Treatment | Standard evidence-based treatment remains IVIG or plasma exchange; combination therapy and repeat IVIG do not add benefit and can increase adverse events. Supportive ICU care and rehabilitation remain essential, especially in severe axonal cases. | Median time to walk without aid: 51 days with IVIG, 49 days with plasma exchange, 40 days with combined treatment in older trial data; repeat IVIG used in 39.7% and combination therapy in 6.1% of a US real-world cohort before newer evidence/guidelines. | Kuwabara, 2024, Journal of the Peripheral Nervous System |  | https://doi.org/10.1111/jns.12646 | (kuwabara2024efficacyandsafety pages 1-2, stino2024intravenousimmunoglobulinand pages 1-2) |
| Recent developments 2023-2024 | Recent work emphasized 2023 EAN/PNS guideline-based care and mechanism-directed therapy. A 2024 phase 3 trial of eculizumab added to IVIG in severe GBS did not meet its primary endpoint despite strong complement suppression and acceptable safety. | Phase 3 eculizumab trial enrolled 57 participants (37 eculizumab, 20 placebo); primary endpoint HR 0.9, 95% CI 0.45–1.97, p=.89. | Kuwabara, 2024, Journal of the Peripheral Nervous System |  | https://doi.org/10.1111/jns.12646 | (kuwabara2024efficacyandsafety pages 1-2, freiha2026guillainbarrésyndromeprogress pages 7-9) |
| Real-world implementation | Real-world US prescribing data show persistent use of non-recommended repeat IVIG and some IVIG/PLEX combination therapy, suggesting a gap between evidence/guidelines and practice. Diagnostic reclassification from GBS to CIDP also occurs frequently in claims-based care pathways. | US cohort n=2325; repeat IVIG 39.7%; combination therapy 6.1%; later reclassified to CIDP 32.0%. | Stino, 2024, Muscle & Nerve |  | https://doi.org/10.1002/mus.28265 | (stino2024intravenousimmunoglobulinand pages 1-2) |


*Table: This table condenses the most supported AMSAN findings from the available context into disease knowledge base fields. It highlights what is known specifically for axonal GBS/AMSAN and where evidence comes from broader GBS literature used to inform AMSAN care.*

---

## Limitations of this report (evidence availability constraints)

- **AMSAN-specific ontology identifiers (MONDO, Orphanet, OMIM, MeSH term strings)** were not available in the retrieved full-text excerpts and therefore are not asserted here.
- Many epidemiologic and prognosis statistics are reported at the **GBS umbrella level**; AMSAN-specific incidence, subtype-specific mortality, and antibody-frequency distributions require additional targeted cohort studies not captured in the retrieved evidence subset.



References

1. (shang2021axonalvariantsof pages 1-2): Pei Shang, Mingqin Zhu, Ying Wang, Xiang-yu Zheng, Xiujuan Wu, Jie Zhu, Jiachun Feng, and Hong-Liang Zhang. Axonal variants of guillain–barré syndrome: an update. Journal of Neurology, pages 1-18, Mar 2021. URL: https://doi.org/10.1007/s00415-020-09742-2, doi:10.1007/s00415-020-09742-2. This article has 93 citations and is from a domain leading peer-reviewed journal.

2. (leonhard2024guillain–barrésyndrome pages 1-3): Sonja E. Leonhard, Nowshin Papri, Luis Querol, Simon Rinaldi, Nortina Shahrizaila, and Bart C. Jacobs. Guillain–barré syndrome. Nature Reviews Disease Primers, Dec 2024. URL: https://doi.org/10.1038/s41572-024-00580-4, doi:10.1038/s41572-024-00580-4. This article has 48 citations.

3. (stino2024intravenousimmunoglobulinand pages 1-2): Amro M. Stino, Evan L. Reynolds, Maya Watanabe, and Brian C. Callaghan. Intravenous immunoglobulin and plasma exchange prescribing patterns for guillain‐barre syndrome in the united states—2001 to 2018. Muscle & Nerve, 70:1192-1199, Sep 2024. URL: https://doi.org/10.1002/mus.28265, doi:10.1002/mus.28265. This article has 3 citations and is from a peer-reviewed journal.

4. (geng2023acutemotorsensoryaxonal pages 3-5): Na Geng, Pengfei Wang, and Yong Zhang. Acute motor-sensory axonal polyneuropathy variant of guillain-barré syndrome with a thalamic lesion and covid-19: a case report and discussion on mechanism. Frontiers in Neurology, Sep 2023. URL: https://doi.org/10.3389/fneur.2023.1227505, doi:10.3389/fneur.2023.1227505. This article has 6 citations and is from a peer-reviewed journal.

5. (umar2024complexneurologicalsequelae pages 4-6): Anam Umar, Amber E Faquih, Bilal Jawed, and Muhammad Bilal. Complex neurological sequelae: axonal guillain-barré syndrome post covid-19 in a young patient. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.67213, doi:10.7759/cureus.67213. This article has 0 citations.

6. (latov2022campylobacterjejuniinfection pages 1-2): Norman Latov. Campylobacter jejuni infection, anti-ganglioside antibodies, and neuropathy. Microorganisms, 10:2139, Oct 2022. URL: https://doi.org/10.3390/microorganisms10112139, doi:10.3390/microorganisms10112139. This article has 25 citations.

7. (geng2023acutemotorsensoryaxonal pages 5-6): Na Geng, Pengfei Wang, and Yong Zhang. Acute motor-sensory axonal polyneuropathy variant of guillain-barré syndrome with a thalamic lesion and covid-19: a case report and discussion on mechanism. Frontiers in Neurology, Sep 2023. URL: https://doi.org/10.3389/fneur.2023.1227505, doi:10.3389/fneur.2023.1227505. This article has 6 citations and is from a peer-reviewed journal.

8. (busl2023guidelinesforneuroprognostication pages 1-3): Katharina M. Busl, Herbert Fried, Susanne Muehlschlegel, Katja E. Wartenberg, Venkatakrishna Rajajee, Sheila A. Alexander, Claire J. Creutzfeldt, Gabriel V. Fontaine, Sara E. Hocker, David Y. Hwang, Keri S. Kim, Dominik Madzar, Dea Mahanes, Shraddha Mainali, Juergen Meixensberger, Oliver W. Sakowitz, Panayiotis N. Varelas, Thomas Westermaier, and Christian Weimar. Guidelines for neuroprognostication in adults with guillain–barré syndrome. Neurocritical Care, 38:564-583, Mar 2023. URL: https://doi.org/10.1007/s12028-023-01707-3, doi:10.1007/s12028-023-01707-3. This article has 52 citations and is from a peer-reviewed journal.

9. (shang2021axonalvariantsof pages 6-7): Pei Shang, Mingqin Zhu, Ying Wang, Xiang-yu Zheng, Xiujuan Wu, Jie Zhu, Jiachun Feng, and Hong-Liang Zhang. Axonal variants of guillain–barré syndrome: an update. Journal of Neurology, pages 1-18, Mar 2021. URL: https://doi.org/10.1007/s00415-020-09742-2, doi:10.1007/s00415-020-09742-2. This article has 93 citations and is from a domain leading peer-reviewed journal.

10. (leonhard2024guillain–barrésyndrome pages 5-7): Sonja E. Leonhard, Nowshin Papri, Luis Querol, Simon Rinaldi, Nortina Shahrizaila, and Bart C. Jacobs. Guillain–barré syndrome. Nature Reviews Disease Primers, Dec 2024. URL: https://doi.org/10.1038/s41572-024-00580-4, doi:10.1038/s41572-024-00580-4. This article has 48 citations.

11. (latov2022campylobacterjejuniinfection pages 2-4): Norman Latov. Campylobacter jejuni infection, anti-ganglioside antibodies, and neuropathy. Microorganisms, 10:2139, Oct 2022. URL: https://doi.org/10.3390/microorganisms10112139, doi:10.3390/microorganisms10112139. This article has 25 citations.

12. (restrepojimenez2018theimmunotherapyof pages 46-47): Paula Restrepo-Jiménez, Yhojan Rodríguez, Paulina González, Christopher Chang, M. Eric Gershwin, and Juan-Manuel Anaya. The immunotherapy of guillain-barré syndrome. Expert Opinion on Biological Therapy, 18:619-631, May 2018. URL: https://doi.org/10.1080/14712598.2018.1468885, doi:10.1080/14712598.2018.1468885. This article has 26 citations and is from a peer-reviewed journal.

13. (leonhard2024guillain–barrésyndrome pages 4-5): Sonja E. Leonhard, Nowshin Papri, Luis Querol, Simon Rinaldi, Nortina Shahrizaila, and Bart C. Jacobs. Guillain–barré syndrome. Nature Reviews Disease Primers, Dec 2024. URL: https://doi.org/10.1038/s41572-024-00580-4, doi:10.1038/s41572-024-00580-4. This article has 48 citations.

14. (kuwabara2024efficacyandsafety pages 1-2): Satoshi Kuwabara, Susumu Kusunoki, Motoi Kuwahara, Yoshihisa Yamano, Yoichiro Nishida, Hirokazu Ishida, Tomoyuki Kasuya, Erik Kupperman, Qun Lin, Glen Frick, and Sonoko Misawa. Efficacy and safety of eculizumab in guillain‐barré syndrome: a phase 3, multicenter, double‐blind, randomized, placebo‐controlled clinical trial. Journal of the Peripheral Nervous System, 29:339-349, Jul 2024. URL: https://doi.org/10.1111/jns.12646, doi:10.1111/jns.12646. This article has 29 citations and is from a peer-reviewed journal.

15. (freiha2026guillainbarrésyndromeprogress pages 7-9): Joumana Freiha, Young Gi Min, Chinar Osman, and Yusuf Rajabally. Guillain-barré syndrome: progress in diagnosis, biomarkers, neuroimaging and management. ImmunoTargets and Therapy, Volume 15:1-13, Apr 2026. URL: https://doi.org/10.2147/itt.s390161, doi:10.2147/itt.s390161. This article has 0 citations.