---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T17:36:23.114932'
end_time: '2026-05-12T18:00:52.602092'
duration_seconds: 1469.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Castleman Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 62
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Castleman Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Castleman Disease** covering all of the
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
- **Disease Name:** Castleman Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Castleman Disease** covering all of the
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


# Castleman Disease (CD): Comprehensive Disease Characteristics Report (2024–2026 evidence-focused)

## 1. Disease information

### 1.1 Overview (what is the disease?)
Castleman disease (CD) is a **rare, nonclonal lymphoproliferative disorder** characterized by distinctive lymph node histopathology and heterogeneous clinical phenotypes ranging from localized lymphadenopathy to life-threatening systemic inflammatory disease. (kobrin2026castlemandisease pages 1-3, chen2025expertperspectivediagnosis pages 1-2)

A modern, clinically actionable framework classifies CD by **anatomic distribution** into:
- **Unicentric Castleman disease (UCD):** single lymph node station/region involvement. (gasljevic2025themorphologicalspectrum pages 1-3, hoffmann2024theclinicalpicture pages 1-2)
- **Multicentric Castleman disease (MCD):** ≥2 lymph node groups with systemic inflammation. (gasljevic2025themorphologicalspectrum pages 1-3, hoffmann2024theclinicalpicture pages 1-2)

MCD is further subdivided by etiology/association into:
- **HHV-8/KSHV–associated MCD (HHV8+ MCD)** (often with HIV or immunosuppression). (hoffmann2024theclinicalpicture pages 1-2, jitaru2026snapshotlookat pages 3-4)
- **Idiopathic MCD (iMCD; HHV-8 negative)**, which is further clinically stratified into **iMCD-TAFRO**, **iMCD-IPL**, and **iMCD-NOS**. (chen2025expertperspectivediagnosis pages 1-2)
- **POEMS-associated MCD (MCD-POEMS)** linked to a plasma cell neoplasm/POEMS syndrome. (hoffmann2024theclinicalpicture pages 1-2, chen2025expertperspectivediagnosis pages 1-2)

### 1.2 Key identifiers (as evidenced in retrieved sources)
- **ICD-10-CM:** **D47.Z2** (Castleman disease). (kobrin2026castlemandisease pages 1-3)

**Not found in retrieved full-text excerpts:** MONDO ID, MeSH ID, Orphanet ID, OMIM ID, ICD-11 code. The accessible literature excerpts reviewed here did not include these identifiers explicitly. (kobrin2026castlemandisease pages 1-3, dispenzieri2020overviewofcastleman pages 1-2, gasljevic2025themorphologicalspectrum pages 1-3, patel2024castlemandiseasea pages 1-2)

### 1.3 Synonyms and alternative names
The retrieved excerpts consistently use “Castleman disease” and subtype labels (UCD, MCD, iMCD, TAFRO, IPL, POEMS-associated MCD). (hoffmann2024theclinicalpicture pages 1-2, chen2025expertperspectivediagnosis pages 1-2, gasljevic2025themorphologicalspectrum pages 1-3)

**Not found verbatim in retrieved excerpts:** “angiofollicular lymph node hyperplasia,” “giant lymph node hyperplasia.” (kobrin2026castlemandisease pages 1-3, dispenzieri2020overviewofcastleman pages 1-2, patel2024castlemandiseasea pages 1-2)

### 1.4 Evidence source type
The content summarized below is derived from **aggregated disease-level resources** (systematic review/meta-analysis, expert perspective, registry natural history), plus **real-world retrospective cohorts** and **ClinicalTrials.gov registry records**, rather than single EHR-only observations. (hoffmann2024theclinicalpicture pages 1-2, chen2025expertperspectivediagnosis pages 1-2, bustamante2024longitudinalnaturalhistory pages 1-2, jitaru2024siltuximabinidiopathic pages 1-2, NCT03933904 chunk 1)

## 2. Etiology

### 2.1 Disease causal factors
**HHV-8–associated MCD:** HHV-8 infection in B cells is a direct causal driver in HHV8+ MCD and is linked to production of viral IL-6 (vIL-6) and cytokine storm biology. (jitaru2026snapshotlookat pages 3-4, fraticelli2023aclinicalhistological pages 6-10)

**iMCD and UCD:** The etiology of UCD and iMCD is not established. A computational virome study using Viral-Track on RNA-seq data (UCD n=22; iMCD n=19; controls n=86) concluded that **active viral infection is unlikely to be a shared pathological driver** of UCD or iMCD. (miller2025noevidencefor pages 1-2)

### 2.2 Risk factors
Evidence in the retrieved excerpts supports **immunocompromised states** (e.g., HIV) as an association particularly for HHV8+ MCD, consistent with HHV-8 biology. (hoffmann2024theclinicalpicture pages 1-2, jitaru2026snapshotlookat pages 3-4)

Robust quantitative, population-level risk factor estimates (e.g., odds ratios for sex/age/exposures) were not present in the accessible excerpts.

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in the retrieved excerpts.

### 2.4 Gene–environment interactions
Direct gene–environment interaction evidence is not provided in the accessible excerpts. However, the HHV-8 subtype illustrates a biologically plausible interaction between **viral infection** and **host immune suppression** in driving cytokine storm phenotypes. (jitaru2026snapshotlookat pages 3-4, fraticelli2023aclinicalhistological pages 6-10)

## 3. Phenotypes

### 3.1 Core phenotype spectrum by subtype
**Systemic inflammatory phenotype (MCD/iMCD):** MCD is described as systemic and potentially life-threatening with multifocal lymphadenopathy and systemic inflammation/constitutional symptoms; HHV8+ MCD is often more aggressive than iMCD. (hoffmann2024theclinicalpicture pages 1-2)

**iMCD-TAFRO phenotype:** Hallmarks include rapid-onset cytokine storm with **anasarca**, **thrombocytopenia**, and **renal dysfunction/reticulin fibrosis**, often resembling sepsis or HLH. (chen2025expertperspectivediagnosis pages 1-2)

**iMCD-IPL phenotype:** Presents with subacute/chronic lymphadenopathy, anemia of inflammation, polyclonal hypergammaglobulinemia, sometimes with increased IgG4 in serum and lymph node tissue; can be difficult to distinguish from IgG4-related disease. (chen2025expertperspectivediagnosis pages 1-2)

### 3.2 Frequency data (recent meta-analysis)
A 2024 systematic review/meta-analysis quantified frequencies of iMCD criteria and features across subtypes (UCD, iMCD, HHV8+ MCD), including lab abnormalities (e.g., CRP elevation, anemia, hypoalbuminemia, thrombocytopenia, hypergammaglobulinemia) and clinical symptoms (e.g., constitutional symptoms, splenomegaly, fluid accumulation). (hoffmann2024theclinicalpicture pages 1-2, hoffmann2024theclinicalpicture media e3e1d910, hoffmann2024theclinicalpicture media 14015b06)

### 3.3 Imaging phenotype (selected quantified examples)
**iMCD subtype CT differences (Dec 2024):** In a 20-patient iMCD CT study, compared with non-TAFRO iMCD, iMCD-TAFRO had higher frequencies of ascites (100% vs 37.5%), gallbladder wall edema (75.0% vs 12.5%), periportal collar (91.7% vs 25.0%), and anterior mediastinal infiltrative lesions (66.7% vs 12.5%). (iguchi2024computedtomographyfindings pages 1-2)

**UCD ultrasound phenotype (Sep 2025):** In 41 UCD patients, ultrasound frequencies included indistinct corticomedullary interface (95.12%), fatty hilum effacement (58.54%), macrocalcification (24.39%), and short linear hyperechoic foci (56.10%). (liu2025thesonographiccharacteristics pages 1-2)

### 3.4 Quality-of-life impact
A 2024 iMCD natural history analysis reported substantial morbidity and QOL impairment; QOL was assessed using EQ-5D-5L and a global health 0–100 scale, with symptom burden correlating inversely with QOL. (bustamante2024longitudinalnaturalhistory pages 6-7, bustamante2024longitudinalnaturalhistory pages 7-9)

### 3.5 Suggested HPO terms (non-exhaustive; mapping aids)
- **Lymphadenopathy** (HP:0002716)
- **Fever** (HP:0001945)
- **Weight loss** (HP:0001824)
- **Anemia** (HP:0001903)
- **Hypoalbuminemia** (HP:0003073)
- **Thrombocytopenia** (HP:0001873) — prominent in TAFRO (chen2025expertperspectivediagnosis pages 1-2)
- **Ascites** (HP:0001541) / **Edema/Anasarca** (HP:0000969)
- **Splenomegaly** (HP:0001744)
- **Hepatomegaly** (HP:0002240)
- **Acute kidney injury / renal insufficiency** (e.g., HP:0001919 / HP:0000083)

(These HPO mappings are ontology suggestions to support KB standardization; they are not direct claims that each term is present in every patient.)

## 4. Genetic / molecular information

### 4.1 Causal genes
CD is generally considered **nonclonal/nonmalignant** rather than a monogenic disorder; however, multiple studies report **somatic alterations** and pathway perturbations, particularly in stromal compartments in UCD and inflammatory signaling in iMCD. (kobrin2026castlemandisease pages 1-3, fraticelli2023aclinicalhistological pages 6-10, smith2025spatialandsingle pages 1-2)

### 4.2 Reported variants and molecular drivers (selected)
- **PDGFRB N666S** recurrently reported in UCD (somatic), supporting stromal-driven biology. (zhang2025mimickersandassociated pages 1-3)
- **PDGFRB mutations** reported in ~17% of UCD (localized to CD45-negative stromal cells) in referenced work summarized in 2023 transcriptomic review-style text. (fraticelli2023aclinicalhistological pages 6-10)
- **NCOA4 p.L261F (L261F)** reported in iMCD and suggested as potentially specific to iMCD in a 2025 review/case discussion. (sikora2025castlemandisease—stillmore pages 7-9)
- **IL6ST variants** are cited as prognostic biomarkers in a 2024 WES study of paraneoplastic pemphigus–associated UCD (not fully accessible in retrieved full-text, but referenced in 2025 review). (sikora2025castlemandisease—stillmore pages 12-14)

### 4.3 Pathway-level molecular signatures
- **IL-6 axis:** central inflammatory mediator in MCD/iMCD; forms the rationale for IL-6 blockade therapies (siltuximab) and IL-6R blockade (tocilizumab). (chen2025expertperspectivediagnosis pages 1-2, jitaru2024siltuximabinidiopathic pages 1-2, jitaru2026snapshotlookat pages 8-9)
- **Beyond IL-6 in iMCD subtypes:** A 2024 lymph node transcriptome study found iMCD-TAFRO/NOS had increased expression of multiple inflammatory mediators and signaling nodes (e.g., STATs, JAKs, MAPKs, NFKB family members, MTOR) and reported **IL33 upregulation for the first time** in iMCD-TAFRO/NOS. (nishikori2024transcriptomeanalysisof pages 1-2)

### 4.4 Epigenetic and chromosomal abnormalities
A 2025 pathology review on mimickers notes iMCD alterations in chromatin-organization genes (e.g., SETD1A, ASH1L, KMT2E, DNMT3A) and describes clonal cytogenetic changes/complex karyotypes in some hyaline vascular CD cases with chromosome 7 abnormalities. (zhang2025mimickersandassociated pages 1-3)

## 5. Environmental information

### 5.1 Infectious agents
- **HHV-8/KSHV:** etiologic agent in HHV8+ MCD. (jitaru2026snapshotlookat pages 3-4, fraticelli2023aclinicalhistological pages 6-10)
- **UCD/iMCD:** Active viral infection is not supported as a shared driver by Viral-Track analysis (RNA-seq based). (miller2025noevidencefor pages 1-2)

### 5.2 Other environmental/lifestyle factors
No robust environmental exposure or lifestyle risk/protective factor evidence was present in the retrieved excerpts.

## 6. Mechanism / pathophysiology

### 6.1 Core mechanistic model (causal chain)
A widely supported causal chain for multicentric/systemic forms is:
1) **Trigger** (HHV-8 infection for HHV8+ MCD; unknown triggers for iMCD) →
2) **Cytokine dysregulation** (IL-6 and other inflammatory/angiogenic mediators, including VEGF) →
3) **Systemic inflammation and vascular permeability** (anasarca/effusions/ascites, cytopenias, organ dysfunction) →
4) **Clinical syndrome** ranging from chronic inflammatory illness to critical cytokine storm (notably iMCD-TAFRO). (chen2025expertperspectivediagnosis pages 1-2, nishikori2024transcriptomeanalysisof pages 1-2, iguchi2024computedtomographyfindings pages 1-2)

### 6.2 Immune and stromal-cell biology (single-cell/spatial advances)
A major recent advance is a 2025 Nature Communications integrated spatial proteome/transcriptome and single-nucleus RNA-seq study across UCD, iMCD, HHV8+ MCD, and reactive nodes. It concluded that CD shows **expanded stromal populations** and identified stromal subsets as major sources of IL-6/VEGF signaling:
- **CXCL13+ follicular dendritic cells (FDCs)**
- **PDGFRA+ T-zone reticular cells (TRCs)**
- **ACTA2+ perivascular reticular cells (PRCs)**
These stromal programs were linked to **B-cell activation/differentiation**, **neovascularization**, and **stromal remodeling**, with inferred activation of **JAK–STAT**, **TGFβ**, and **MAPK** signaling via ligand–receptor interactions. (smith2025spatialandsingle pages 1-2, smith2025spatialandsingle pages 6-8, smith2025spatialandsingle pages 6-6)

### 6.3 Suggested GO biological process terms (examples)
- **GO:0006954 inflammatory response**
- **GO:0001816 cytokine production**
- **GO:0001525 angiogenesis**
- **GO:0007165 signal transduction** (for JAK–STAT/MAPK modules)

### 6.4 Suggested Cell Ontology (CL) terms (examples)
- **Follicular dendritic cell** (CL:0000447)
- **Plasma cell** (CL:0000786)
- **Endothelial cell** (CL:0000115)

(These ontology mappings support KB structure; cell types and pathways are supported by single-cell/spatial evidence above.) (smith2025spatialandsingle pages 1-2, smith2025spatialandsingle pages 6-8)

## 7. Anatomical structures affected

### 7.1 Organ/system level
- **Lymph nodes (primary):** the defining pathologic site; UCD is localized, MCD is generalized. (gasljevic2025themorphologicalspectrum pages 1-3, hoffmann2024theclinicalpicture pages 1-2)
- **Spleen/liver and systemic compartments:** organomegaly and systemic edema/effusions are common in iMCD-TAFRO and may be present across MCD phenotypes. (iguchi2024computedtomographyfindings pages 1-2, bustamante2024longitudinalnaturalhistory pages 4-6)

### 7.2 Suggested UBERON terms (examples)
- **Lymph node** (UBERON:0000029)
- **Spleen** (UBERON:0002106)
- **Liver** (UBERON:0002107)
- **Bone marrow** (UBERON:0002371)

## 8. Temporal development

### 8.1 Onset and course
iMCD ranges from moderate chronic inflammatory disease to acute, life-threatening cytokine storm. iMCD-TAFRO is characterized by rapid onset severe inflammation and can resemble sepsis/HLH. (chen2025expertperspectivediagnosis pages 1-2)

### 8.2 Progression, flares, and burden
Registry-based natural history data indicate significant ongoing disease burden with defined flare dynamics; notably, iMCD-NOS patients spent a higher proportion of follow-up time in flare than iMCD-TAFRO (median 52.3% vs 18.9%). (bustamante2024longitudinalnaturalhistory pages 6-7)

## 9. Inheritance and population

### 9.1 Epidemiology
Quantitative prevalence/incidence estimates were not present in the accessible excerpts. However, iMCD burden and outcome statistics from registry analyses and cohorts provide clinically relevant population-level context for severity and mortality risk. (bustamante2024longitudinalnaturalhistory pages 1-2)

### 9.2 Genetics and inheritance
CD is not typically inherited as a Mendelian trait, but rare germline predisposition has been reported in referenced literature (e.g., germline FAS mutation in a family with UCD and iMCD). (fraticelli2023aclinicalhistological pages 51-53)

## 10. Diagnostics

### 10.1 Diagnostic principles
Diagnosis requires **lymph node histopathology** integrated with clinical/laboratory findings and **exclusion of mimics** (autoimmune disease, infections, lymphoma, POEMS, etc.). (gasljevic2025themorphologicalspectrum pages 1-3, hoffmann2024theclinicalpicture pages 1-2, chen2025expertperspectivediagnosis pages 1-2)

For iMCD specifically, the 2017 international consensus criteria require:
- Major criteria: **multicentric lymphadenopathy** and **Castleman-consistent lymph node histopathology**
- Plus minor criteria and exclusion criteria. (hoffmann2024theclinicalpicture pages 1-2)

### 10.2 Biopsy strategy and PET/CT
Expert guidance recommends cross-sectional imaging (CT neck-to-pelvis or PET-CT) and emphasizes obtaining an **excisional lymph node biopsy** when possible; fine-needle aspiration is discouraged and core biopsies can have low yield. (chen2025expertperspectivediagnosis pages 6-7)

A 2024 case report provides a direct, implementation-oriented statement on PET for biopsy targeting: **“A PET scan allowed the best selection of a lymph node to be biopsied”** after an initial non-diagnostic biopsy, enabling diagnosis of iMCD. (bitektine2024thevalueof pages 1-2)

### 10.3 Imaging biomarkers
- **CT imaging to differentiate iMCD subtypes**: quantified features in iMCD-TAFRO vs non-TAFRO are listed above (ascites, gallbladder wall edema, periportal collar, anterior mediastinal lesions). (iguchi2024computedtomographyfindings pages 1-2)
- **Ultrasound patterns in UCD**: quantified features include corticomedullary interface changes, hilum effacement, calcification, and hyperechoic foci. (liu2025thesonographiccharacteristics pages 1-2)

### 10.4 Biomarkers and labs (examples)
A 2024 systematic review/meta-analysis synthesized frequencies of minor criteria/lab abnormalities (e.g., CRP elevation, anemia, hypoalbuminemia, thrombocytopenia, hypergammaglobulinemia) across subtypes; see Figures 3–4 in the paper. (hoffmann2024theclinicalpicture pages 1-2, hoffmann2024theclinicalpicture media e3e1d910, hoffmann2024theclinicalpicture media 14015b06)

## 11. Outcome / prognosis

### 11.1 iMCD burden, organ failure, and mortality signals
In a 2024 longitudinal registry study, iMCD patients frequently required life-sustaining interventions during hospitalization (dialysis 27%; mechanical ventilation 17%), and post-diagnosis morbidities included acute renal failure (48%) and chronic kidney disease (15.7%). (bustamante2024longitudinalnaturalhistory pages 6-7)

### 11.2 UCD outcomes after surgery
In a 2024 retroperitoneal UCD surgical series (n=15), there were **no perioperative deaths** and **no deaths or recurrences** over a median follow-up of 78.5 months, supporting excellent long-term outcomes with complete resection in that anatomical context. (gao2024clinicalfeaturesand pages 1-2)

## 12. Treatment

### 12.1 Standard treatment concepts (real-world implementation)
**UCD:** Primary treatment is typically **complete surgical excision**, often curative. (kobrin2026castlemandisease pages 1-3, gao2024clinicalfeaturesand pages 1-2)

**iMCD:** First-line therapy is **IL-6 pathway inhibition**, most prominently **siltuximab (anti–IL-6)**; expert opinion frames IL-6 pathway inhibition as first-line for all iMCD subtypes. (chen2025expertperspectivediagnosis pages 1-2, jitaru2024siltuximabinidiopathic pages 1-2)

**Tocilizumab (anti–IL-6R):** used as an alternative option in some clinical contexts, including for HHV-8/KSHV-associated MCD in clinical trials and as an option discussed after siltuximab relapse/non-response in reviews. (jitaru2026snapshotlookat pages 8-9, NCT01441063 chunk 1)

### 12.2 Recent quantitative treatment outcomes (2024–2025)
**Siltuximab real-world Europe (2017–2022; published Oct 2024):** ORR 71.1% with 55.3% complete response; estimated 3-year OS ~74%; serious adverse events 16.7%. (jitaru2024siltuximabinidiopathic pages 1-2)

**Siltuximab real-world China (Jul 2022–Mar 2024; published Apr 2025):** ORR 59% at week 3 and 91% at week 12; in severe iMCD treated with siltuximab + bortezomib/cyclophosphamide/dexamethasone (BCD), ORR increased to 100% at week 12. (li2025realworlddataof pages 1-2, li2025realworlddataof pages 4-5)

### 12.3 Treatment-related trials and investigational therapies (NCT-linked)
Key ongoing/recent trials include:
- **Sirolimus (mTOR inhibitor) in previously treated iMCD:** Phase II single-arm trial NCT03933904 (active, not recruiting). (NCT03933904 chunk 1)
- **Ruxolitinib (JAK1/2 inhibitor) in previously treated iMCD:** Phase II trial NCT07085039 (recruiting; started 2025-12-18). (NCT07085039 chunk 1)
- **Tocilizumab for KSHV-associated MCD:** Phase II pilot study NCT01441063 (completed; enrolled 8; tocilizumab 8 mg/kg q2 weeks up to 12 weeks; primary endpoint overall clinical benefit response). (NCT01441063 chunk 1)
- **Rituximab for KSHV-associated MCD in Malawi:** Phase II trial NCT04585893 (active, not recruiting; rituximab 375 mg/m^2 weekly ×4; high-risk patients also received etoposide). (NCT04585893 chunk 1)

### 12.4 Suggested MAXO terms (examples)
- **Lymph node excision** (surgical resection) — UCD
- **Interleukin-6 neutralization** (siltuximab) — iMCD
- **Interleukin-6 receptor inhibition** (tocilizumab)
- **B cell depletion therapy** (rituximab)
- **mTOR inhibition** (sirolimus)
- **JAK inhibition** (ruxolitinib)

## 13. Prevention
No established primary prevention strategy is supported in the retrieved excerpts. For HHV8+ MCD, prevention is indirectly related to management of HIV/immunosuppression and HHV-8 disease monitoring in relevant settings, but explicit prevention guidelines were not accessible in the excerpts used here.

## 14. Other species / natural disease
No veterinary or cross-species naturally occurring Castleman disease evidence was identified in the retrieved excerpts.

## 15. Model organisms / experimental systems
While classic whole-animal models were not described in accessible excerpts, **human-tissue multi-omic experimental systems** represent a major “model” for mechanism discovery:
- Single-nucleus RNA-seq and spatial transcriptomics/proteomics mapping of CD lymph nodes demonstrated stromal-cell programs and ligand–receptor networks driving IL-6/VEGF signaling and JAK–STAT/MAPK/TGFβ pathway signatures. (smith2025spatialandsingle pages 1-2, smith2025spatialandsingle pages 6-8)

## Summary tables (for knowledge base ingestion)

| Subtype | Core definition | Typical triggers/associations | Hallmark clinical pattern | Hallmark pathology pattern | Key diagnostics/tests |
|---|---|---|---|---|---|
| Unicentric Castleman disease (UCD) | Localized Castleman disease involving a single lymph node station/region (hoffmann2024theclinicalpicture pages 1-2, chen2025expertperspectivediagnosis pages 1-2, gasljevic2025themorphologicalspectrum pages 1-3) | Usually no defined infectious trigger; may reflect localized stromal/FDC-related process rather than systemic cytokine disease (jitaru2026snapshotlookat pages 3-4, fraticelli2023aclinicalhistological pages 6-10) | Solitary, often indolent enlarged node or mass; minimal or no systemic inflammation in many cases (hoffmann2024theclinicalpicture pages 1-2, jitaru2026snapshotlookat pages 3-4, kobrin2026castlemandisease pages 1-3) | Most often hyaline vascular/hypervascular pattern with regressed germinal centers, onion-skin mantle zones, penetrating “lollipop” vessels, increased FDCs/vascularity (gasljevic2025themorphologicalspectrum pages 1-3) | Excisional lymph node biopsy with histopathology; CT/MRI/PET for localization and biopsy planning; exclude mimics such as lymphoma/infection (kobrin2026castlemandisease pages 1-3, chen2025expertperspectivediagnosis pages 6-7) |
| HHV-8–associated multicentric Castleman disease (HHV8+ MCD) | Multicentric systemic Castleman disease driven by KSHV/HHV-8 infection, typically involving multiple node groups (hoffmann2024theclinicalpicture pages 1-2, chen2025expertperspectivediagnosis pages 1-2, gasljevic2025themorphologicalspectrum pages 1-3) | HHV-8/KSHV infection; often associated with HIV or other immunocompromised states; viral IL-6 biology central (hoffmann2024theclinicalpicture pages 1-2, jitaru2026snapshotlookat pages 3-4) | Aggressive systemic inflammatory syndrome with multifocal lymphadenopathy, constitutional symptoms, organomegaly, cytokine-storm flares (hoffmann2024theclinicalpicture pages 1-2, jitaru2026snapshotlookat pages 3-4) | Usually plasmacytic or mixed Castleman histology with HHV-8–infected plasmablast/plasma-cell populations (jitaru2026snapshotlookat pages 3-4, fraticelli2023aclinicalhistological pages 6-10) | Lymph node biopsy plus HHV-8 testing; HIV serology and HHV-8 qPCR are key adjuncts; exclude other inflammatory/neoplastic mimics (hoffmann2024theclinicalpicture pages 1-2, chen2025expertperspectivediagnosis pages 1-2) |
| Idiopathic multicentric Castleman disease (iMCD), NOS | HHV-8–negative multicentric Castleman disease diagnosed by characteristic histopathology + multicentric lymphadenopathy + minor criteria after exclusion of mimics; NOS if not meeting TAFRO/IPL patterns (hoffmann2024theclinicalpicture pages 1-2, chen2025expertperspectivediagnosis pages 1-2) | No established cause; IL-6-driven cytokine dysregulation common, but non-IL-6 pathways also implicated (chen2025expertperspectivediagnosis pages 1-2, nishikori2024transcriptomeanalysisof pages 1-2, miller2025noevidencefor pages 1-2) | Systemic inflammation with generalized lymphadenopathy; can mimic autoimmune disease or indolent lymphoma; variable anemia, constitutional symptoms, organomegaly (chen2025expertperspectivediagnosis pages 1-2, hoffmann2024theclinicalpicture pages 1-2) | Hypervascular, plasmacytic, or mixed patterns on lymph node biopsy (hoffmann2024theclinicalpicture pages 1-2, gasljevic2025themorphologicalspectrum pages 1-3) | Consensus diagnostic workup: excisional node biopsy, cross-sectional imaging/PET-CT, inflammatory labs, and exclusion of infections, autoimmune disease, lymphoma, and POEMS (hoffmann2024theclinicalpicture pages 1-2, chen2025expertperspectivediagnosis pages 6-7) |
| iMCD-TAFRO | Clinical subtype of iMCD marked by thrombocytopenia, anasarca, fever/elevated CRP, reticulin fibrosis or renal dysfunction, and organomegaly (chen2025expertperspectivediagnosis pages 1-2, kobrin2026castlemandisease pages 1-3) | Idiopathic cytokine storm phenotype; often severe/rapid-onset; may show broader inflammatory signaling beyond IL-6 (JAK-STAT/MAPK/VEGF-related) (nishikori2024transcriptomeanalysisof pages 1-2, kobrin2026castlemandisease pages 3-5) | Rapid-onset severe inflammation with anasarca, thrombocytopenia, renal dysfunction, small-volume lymphadenopathy; can resemble HLH or sepsis (chen2025expertperspectivediagnosis pages 1-2, chen2025expertperspectivediagnosis pages 6-7) | Castleman-like lymph node changes, often with increased vascularity and atrophic follicles; marrow may show reticulin fibrosis/megakaryocytic changes (alnoor2025theevolutionand pages 3-3) | Biopsy when feasible; CT/PET often shows ascites/effusions, periportal collar, anterior mediastinal lesions, mild-moderate FDG avidity; marrow exam may support diagnosis (chen2025expertperspectivediagnosis pages 6-7, iguchi2024computedtomographyfindings pages 1-2) |
| iMCD-IPL | iMCD subtype also called idiopathic plasmacytic lymphadenopathy, defined by plasmacytic iMCD phenotype with chronic inflammatory features (chen2025expertperspectivediagnosis pages 1-2, jitaru2026snapshotlookat pages 3-4) | HHV-8 negative; often strong humoral/IL-6-associated inflammatory phenotype, sometimes overlapping with IgG4-related disease clinically (chen2025expertperspectivediagnosis pages 1-2) | Subacute/chronic lymphadenopathy, anemia of inflammation, polyclonal hypergammaglobulinemia, often increased IgG4 in serum/node tissue (chen2025expertperspectivediagnosis pages 1-2) | Plasma cell/plasmacytic histologic pattern is typical (jitaru2026snapshotlookat pages 3-4) | Excisional biopsy, serum immunoglobulins/IgG subclasses, inflammatory markers, and careful exclusion of IgG4-related disease and histiocytic/lymphoid mimics (chen2025expertperspectivediagnosis pages 1-2, hoffmann2024theclinicalpicture pages 1-2) |
| POEMS-associated MCD | Multicentric Castleman disease occurring in association with POEMS syndrome/plasma-cell neoplasm rather than idiopathic or HHV-8-driven disease (hoffmann2024theclinicalpicture pages 1-2, chen2025expertperspectivediagnosis pages 1-2, gasljevic2025themorphologicalspectrum pages 1-3) | Associated with plasma cell dyscrasia and POEMS features; VEGF-related biology emphasized in POEMS context (patel2024castlemandiseasea pages 3-4, fraticelli2023aclinicalhistological pages 15-22) | Multicentric disease with Castleman pathology plus POEMS manifestations (especially neuropathy/endocrinopathy/monoclonal plasma-cell disorder) rather than isolated cytokine syndrome alone (chen2025expertperspectivediagnosis pages 1-2, fraticelli2023aclinicalhistological pages 15-22) | Commonly plasma-cell pattern on lymph node histology (jitaru2026snapshotlookat pages 3-4, fraticelli2023aclinicalhistological pages 15-22) | Diagnose Castleman pathology plus dedicated POEMS evaluation: serum/urine monoclonal protein studies, VEGF assessment where available, and clinical assessment for neuropathy/endocrinopathy/organomegaly/skin changes (hoffmann2024theclinicalpicture pages 1-2, chen2025expertperspectivediagnosis pages 1-2) |


*Table: This table summarizes the major Castleman disease subtypes, how they are defined, their typical associations, hallmark clinicopathologic features, and the main diagnostic tests used to distinguish them. It is useful as a compact reference for subtype-aware diagnosis and knowledge base curation.*

| Item | Population/subtype | Design & dates | Key quantitative outcomes | URL |
|---|---|---|---|---|
| iMCD natural history (Haematologica 2024) | 102 patients with idiopathic multicentric Castleman disease; 61 iMCD-TAFRO and 41 iMCD-NOS | Longitudinal natural history registry study; published Jan 2024; median follow-up ~3.4 years (bustamante2024longitudinalnaturalhistory pages 1-2, bustamante2024longitudinalnaturalhistory pages 4-6) | Hospitalization during year around diagnosis: TAFRO median 36 days vs NOS 0 days; dialysis 27%; mechanical ventilation 17%; acute renal failure 48%; anemia 85.3%; NOS spent more time in flare than TAFRO: 52.3% vs 18.9% (bustamante2024longitudinalnaturalhistory pages 6-7, bustamante2024longitudinalnaturalhistory pages 1-2, bustamante2024longitudinalnaturalhistory pages 7-9, bustamante2024longitudinalnaturalhistory pages 4-6) | https://doi.org/10.3324/haematol.2023.283603 |
| Siltuximab real-world Europe (J Hematol 2024) | 48 adults with iMCD in Greece and Romania | Retrospective real-world cohort, Jan 2017–Dec 2022; published Oct 2024 (jitaru2024siltuximabinidiopathic pages 1-2) | Median 9 cycles; overall response rate 71.1%; complete response 55.3%; partial response 15.8%; estimated 3-year overall survival 74%; median survival 123 months; serious adverse events 16.7% (jitaru2024siltuximabinidiopathic pages 1-2) | https://doi.org/10.14740/jh1343 |
| Siltuximab real-world China (Ann Hematol 2025) | 43 consecutive iMCD patients; 18 severe cases received siltuximab+BCD | Single-center retrospective study, Jul 2022–Mar 2024; published Apr 2025 (li2025realworlddataof pages 1-2, li2025realworlddataof pages 4-5) | ORR 59% at week 3 and 91% at week 12; week-12 complete response 54% and partial response 37%; first-line siltuximab predicted better response; severe iMCD with siltuximab+BCD had ORR 50% at week 3 and 100% at week 12; mostly mild adverse events (li2025realworlddataof pages 1-2, li2025realworlddataof pages 4-5) | https://doi.org/10.1007/s00277-025-06329-7 |
| UCD retroperitoneal surgery series (Front Surg 2024) | 15 patients with retroperitoneal unicentric Castleman disease | Single-center retrospective surgical series including cases treated through Dec 2022; published Sep 2024 (gao2024clinicalfeaturesand pages 1-2) | 73.3% male; 80% age <40 years; hyaline-vascular 66.7%, mixed 33.3%; serious complications 13.3%; no perioperative deaths; median follow-up 78.5 months; no deaths or recurrences (gao2024clinicalfeaturesand pages 1-2) | https://doi.org/10.3389/fsurg.2024.1371968 |
| iMCD subtype CT imaging (JCEH 2024) | 20 iMCD patients: 12 TAFRO, 5 IPL, 3 NOS | Single-center retrospective CT study; published Dec 2024 (iguchi2024computedtomographyfindings pages 1-2) | TAFRO vs non-TAFRO: ascites 100% vs 37.5%; gallbladder wall edema 75.0% vs 12.5%; periportal collar 91.7% vs 25.0%; anterior mediastinal infiltrative lesions 66.7% vs 12.5%; para-aortic edema 83.3% vs 37.5% (trend) (iguchi2024computedtomographyfindings pages 1-2) | https://doi.org/10.3960/jslrt.24053 |
| UCD ultrasound cohort (Cancer Imaging 2025) | 41 UCD patients | Single-center retrospective preoperative ultrasound cohort, Jan 2016–Mar 2024; published Sep 2025 (liu2025thesonographiccharacteristics pages 1-2) | 100% solitary well-defined enlarged nodes with increased cortical thickness; indistinct corticomedullary interface 95.12%; asymmetric cortical thickening 41.46%; fatty hilum effacement 58.54%; macrocalcification 24.39%; short linear hyperechoic foci 56.10%; abundant flow more frequent in HV and mixed lesions (75.86% and 87.50%) than PC-type (25%) (liu2025thesonographiccharacteristics pages 1-2) | https://doi.org/10.1186/s40644-025-00937-2 |
| Sirolimus trial NCT03933904 | Previously treated HHV-8-negative iMCD refractory/relapsed after or intolerant of anti–IL-6 therapy | Phase II, single-arm, open-label University of Pennsylvania trial; started 2019-09-25; active, not recruiting (NCT03933904 chunk 1, NCT03933904 chunk 2) | Actual enrollment 7; oral sirolimus for 12 months with target trough 10–15 ng/mL; primary endpoint is positive Clinical Benefit Response at ~12 months; secondary endpoints include CHAP score, symptom score, and modified Cheson radiologic response (NCT03933904 chunk 1, NCT03933904 chunk 2) | https://clinicaltrials.gov/study/NCT03933904 |
| Ruxolitinib trial NCT07085039 | Previously treated iMCD refractory/relapsed or intolerant to anti–IL-6 therapy | Phase II, single-arm, open-label, multicenter University of Pennsylvania trial; recruiting; start 2025-12-18; estimated primary completion 2028-07-31 (NCT07085039 chunk 1, NCT07085039 chunk 2) | Estimated enrollment 14; daily oral ruxolitinib up to 1 year; primary endpoint is positive Clinical Benefit Response at 12 months; secondary endpoints include CBR at 3/6/9 months, CHAP score, 34-item symptom score, modified Cheson response, treatment retention, and grade ≥3 adverse events/SAEs (NCT07085039 chunk 1, NCT07085039 chunk 2) | https://clinicaltrials.gov/study/NCT07085039 |
| Tocilizumab KSHV-MCD trial NCT01441063 | Symptomatic KSHV/HHV-8–associated multicentric Castleman disease, largely in HIV-infected adults | Phase II, open-label, single-center NCI pilot study; start 2011-09-13; primary completion 2018-06-06; completion 2020-10-05; completed (NCT01441063 chunk 2, NCT01441063 chunk 1) | Actual enrollment 8; tocilizumab 8 mg/kg every 2 weeks up to 12 weeks; inadequate responders could add zidovudine/valganciclovir; primary endpoint overall clinical benefit response; secondary endpoints included radiographic/biochemical response, safety, 4-month PFS and OS (NCT01441063 chunk 2, NCT01441063 chunk 1) | https://clinicaltrials.gov/study/NCT01441063 |
| Rituximab Malawi trial NCT04585893 | Pathologically confirmed KSHV-associated MCD in Malawi, HIV-positive or HIV-negative adults | Phase II, single-group interventional trial; start 2021-06-22; primary completion 2024-08-30; estimated completion 2026-06-07; active, not recruiting (NCT04585893 chunk 1, NCT04585893 chunk 2) | Enrollment 15; rituximab 375 mg/m^2 weekly ×4; high-risk patients also received etoposide 100 mg/m^2 weekly ×4; primary endpoint non-hematologic grade ≥3 adverse events through ~12 weeks; secondary endpoints include overall survival, event-free survival, response rates, QoL by PROMIS Global-10, Kaposi sarcoma exacerbation, and hemoglobin change (NCT04585893 chunk 1, NCT04585893 chunk 2) | https://clinicaltrials.gov/study/NCT04585893 |


*Table: This table summarizes key 2024–2025 clinical studies and active or recent trials across Castleman disease subtypes, including natural history, imaging, surgery, and systemic therapies. It is useful for quickly comparing study populations, designs, major quantitative findings, and trial status.*

## Notes on evidence gaps vs template requirements
- **MONDO/MeSH/Orphanet/OMIM/ICD-11 identifiers and classic synonyms** were not present in the retrieved full-text excerpts available through the tools in this run; only ICD-10-CM D47.Z2 was explicitly captured. (kobrin2026castlemandisease pages 1-3)
- **Prevalence/incidence** (population epidemiology) was not directly available in the accessible excerpts; this report therefore emphasizes recent registry-based burden/outcomes and real-world treatment data. (bustamante2024longitudinalnaturalhistory pages 1-2, jitaru2024siltuximabinidiopathic pages 1-2)


References

1. (kobrin2026castlemandisease pages 1-3): Dale M. Kobrin and D. Fajgenbaum. Castleman disease. Advances in Lymphatic Medicine, Mar 2026. URL: https://doi.org/10.5772/intechopen.1009424, doi:10.5772/intechopen.1009424. This article has 0 citations.

2. (chen2025expertperspectivediagnosis pages 1-2): Luke Y.C. Chen, Lu Zhang, and David C. Fajgenbaum. Expert perspective: diagnosis and treatment of castleman disease. Arthritis & rheumatology, Jun 2025. URL: https://doi.org/10.1002/art.43269, doi:10.1002/art.43269. This article has 25 citations and is from a highest quality peer-reviewed journal.

3. (gasljevic2025themorphologicalspectrum pages 1-3): Gorana Gasljevic, Arturo Bonometti, Ioannis Anagnostopoulos, Olga Balaguè, Michiel Van den Brand, James R. Cook, Camille Laurent, Maurilio Ponzoni, Leticia Quintanilla-Martinez, Birgitta Sander, and Stefan Dirnhofer. The morphological spectrum of castleman disease and related disorders: a report from the lymphoma workshop of the 22nd meeting of the european association of hematopathology. Virchows Archiv : an international journal of pathology, Jul 2025. URL: https://doi.org/10.1007/s00428-025-04171-w, doi:10.1007/s00428-025-04171-w. This article has 5 citations.

4. (hoffmann2024theclinicalpicture pages 1-2): Christian Hoffmann, Eric Oksenhendler, Sarah Littler, Lisa Grant, Karan Kanhai, and David C. Fajgenbaum. The clinical picture of castleman disease: a systematic review and meta-analysis. Blood Advances, 8:4924-4935, Sep 2024. URL: https://doi.org/10.1182/bloodadvances.2024013548, doi:10.1182/bloodadvances.2024013548. This article has 29 citations and is from a peer-reviewed journal.

5. (jitaru2026snapshotlookat pages 3-4): Ciprian Jitaru, Natalia Zlampa, Delia Dima, Anca Bojan, Mihnea Zdrenghea, Laura Urian, David Kegyes, Anamaria Bancos, Maria Santa, Andrei Ivancuta, Bobe Petrushev, Madalina Nistor, Bogdan Tigu, Catalin Constantinescu, Bogdan Fetica, Maria Puiu, Mihai‐Stefan Muresan, and Ciprian Tomuleasa. Snapshot look at castleman disease. Journal of Cellular and Molecular Medicine, Feb 2026. URL: https://doi.org/10.1111/jcmm.70961, doi:10.1111/jcmm.70961. This article has 1 citations and is from a peer-reviewed journal.

6. (dispenzieri2020overviewofcastleman pages 1-2): Angela Dispenzieri and David C. Fajgenbaum. Overview of castleman disease. Blood, 135:1353-1364, Apr 2020. URL: https://doi.org/10.1182/blood.2019000931, doi:10.1182/blood.2019000931. This article has 530 citations and is from a highest quality peer-reviewed journal.

7. (patel2024castlemandiseasea pages 1-2): Jay P Patel, Deep P Patel, Trishul H Amin, Rushikesh K Dave, Daksh Hardaswani, Faizanali Saiyed, and Rushita J Goswami. Castleman disease: a rare lymphoproliferative disorder with diverse clinical presentation, diagnosis, and treatment approach. Cureus, Sep 2024. URL: https://doi.org/10.7759/cureus.69149, doi:10.7759/cureus.69149. This article has 5 citations.

8. (bustamante2024longitudinalnaturalhistory pages 1-2): Mateo Sarmiento Bustamante, Sheila K. Pierson, Yue Ren, Adam Bagg, Joshua D. Brandstadter, Gordan Srkalovic, Natalie Mango, Daisy Alapat, Mary Jo Lechowicz, Hongzhe Li, Frits Van Rhee, Megan S. Lim, and David C. Fajgenbaum. Longitudinal, natural history study reveals the disease burden of idiopathic multicentric castleman disease. Haematologica, 109:2196-2206, Jan 2024. URL: https://doi.org/10.3324/haematol.2023.283603, doi:10.3324/haematol.2023.283603. This article has 16 citations.

9. (jitaru2024siltuximabinidiopathic pages 1-2): Ciprian Jitaru, Argyris Symeonidis, Sorina Badelita, Eirini Katodritou, Andrei Colita, Anastasia Mpanti, Anamaria Bancos, Bogdan Tigu, Petra Rotariu, Laura Urian, Ioana Rus, Delia Dima, Anca Bojan, Marc Damian, Vasiliki Labropoulou, Mihai Stefan Muresan, Despina Fotiou, Bogdan Fetica, Bobe Petrushev, Angela Dascalescu, Dimitra Dalampira, Sanda Buruiana, Catalin Constantinescu, Mihnea Zdrenghea, Meletios A. Dimopoulos, Ciprian Tomuleasa, and Evangelos Terpos. Siltuximab in idiopathic multicentric castleman disease: real-world experience. Journal of Hematology, 13:207-215, Oct 2024. URL: https://doi.org/10.14740/jh1343, doi:10.14740/jh1343. This article has 8 citations.

10. (NCT03933904 chunk 1):  Sirolimus in Previously Treated Idiopathic Multicentric Castleman Disease. University of Pennsylvania. 2019. ClinicalTrials.gov Identifier: NCT03933904

11. (fraticelli2023aclinicalhistological pages 6-10): S Fraticelli. A clinical, histological and transcriptomic characterization of a selected series of castleman disease's cases. Unknown journal, 2023.

12. (miller2025noevidencefor pages 1-2): Ira Miller, Melanie D. Mumau, Saishravan Shyamsundar, Mateo Sarmiento Bustamante, Pedro Horna, Michael V. Gonzalez, and David C. Fajgenbaum. No evidence for active viral infection in unicentric and idiopathic multicentric castleman disease by viral-track analysis. Scientific Reports, Jan 2025. URL: https://doi.org/10.1038/s41598-025-85193-x, doi:10.1038/s41598-025-85193-x. This article has 3 citations and is from a peer-reviewed journal.

13. (hoffmann2024theclinicalpicture media e3e1d910): Christian Hoffmann, Eric Oksenhendler, Sarah Littler, Lisa Grant, Karan Kanhai, and David C. Fajgenbaum. The clinical picture of castleman disease: a systematic review and meta-analysis. Blood Advances, 8:4924-4935, Sep 2024. URL: https://doi.org/10.1182/bloodadvances.2024013548, doi:10.1182/bloodadvances.2024013548. This article has 29 citations and is from a peer-reviewed journal.

14. (hoffmann2024theclinicalpicture media 14015b06): Christian Hoffmann, Eric Oksenhendler, Sarah Littler, Lisa Grant, Karan Kanhai, and David C. Fajgenbaum. The clinical picture of castleman disease: a systematic review and meta-analysis. Blood Advances, 8:4924-4935, Sep 2024. URL: https://doi.org/10.1182/bloodadvances.2024013548, doi:10.1182/bloodadvances.2024013548. This article has 29 citations and is from a peer-reviewed journal.

15. (iguchi2024computedtomographyfindings pages 1-2): Toshihiro Iguchi, Asami Nishikori, Yasuharu Sato, Midori Filiz Nishimura, Noriko Iwaki, Katsuhide Kojima, Takashi Asahara, Fumio Otsuka, Yoshinobu Maeda, and Takao Hiraki. Computed tomography findings of idiopathic multicentric castleman disease subtypes. Journal of Clinical and Experimental Hematopathology, 64:292-296, Dec 2024. URL: https://doi.org/10.3960/jslrt.24053, doi:10.3960/jslrt.24053. This article has 5 citations.

16. (liu2025thesonographiccharacteristics pages 1-2): Zihan Liu, Zihan Niu, Yuhan Gao, Mengsu Xiao, Ying Wang, Qingli Zhu, and Lu Zhang. The sonographic characteristics of unicentric castleman disease - a single-center retrospective study. Cancer Imaging, Sep 2025. URL: https://doi.org/10.1186/s40644-025-00937-2, doi:10.1186/s40644-025-00937-2. This article has 0 citations and is from a peer-reviewed journal.

17. (bustamante2024longitudinalnaturalhistory pages 6-7): Mateo Sarmiento Bustamante, Sheila K. Pierson, Yue Ren, Adam Bagg, Joshua D. Brandstadter, Gordan Srkalovic, Natalie Mango, Daisy Alapat, Mary Jo Lechowicz, Hongzhe Li, Frits Van Rhee, Megan S. Lim, and David C. Fajgenbaum. Longitudinal, natural history study reveals the disease burden of idiopathic multicentric castleman disease. Haematologica, 109:2196-2206, Jan 2024. URL: https://doi.org/10.3324/haematol.2023.283603, doi:10.3324/haematol.2023.283603. This article has 16 citations.

18. (bustamante2024longitudinalnaturalhistory pages 7-9): Mateo Sarmiento Bustamante, Sheila K. Pierson, Yue Ren, Adam Bagg, Joshua D. Brandstadter, Gordan Srkalovic, Natalie Mango, Daisy Alapat, Mary Jo Lechowicz, Hongzhe Li, Frits Van Rhee, Megan S. Lim, and David C. Fajgenbaum. Longitudinal, natural history study reveals the disease burden of idiopathic multicentric castleman disease. Haematologica, 109:2196-2206, Jan 2024. URL: https://doi.org/10.3324/haematol.2023.283603, doi:10.3324/haematol.2023.283603. This article has 16 citations.

19. (smith2025spatialandsingle pages 1-2): David Smith, Anna Eichinger, É. Fennell, Z. Xu-Monette, Andrew Rech, Julia Wang, E. Esteva, Arta Seyedian, Xiaoxu Yang, Mei Zhang, Dan Martinez, Kai Tan, Minjie Luo, Katherine J Young, Paul G Murray, Christopher Y Park, Boris Reizis, and Vinodh Pillai. Spatial and single cell mapping of castleman disease reveals key stromal cell types and cytokine pathways. Nature Communications, Jul 2025. URL: https://doi.org/10.1038/s41467-025-61214-1, doi:10.1038/s41467-025-61214-1. This article has 11 citations and is from a highest quality peer-reviewed journal.

20. (zhang2025mimickersandassociated pages 1-3): Xiaohui Zhang, Sara Niyazi, Huazhang Guo, and Ling Zhang. Mimickers and associated neoplasms of castleman disease. Journal of Clinical and Translational Pathology, 000:000-000, Mar 2025. URL: https://doi.org/10.14218/jctp.2024.00047, doi:10.14218/jctp.2024.00047. This article has 2 citations.

21. (sikora2025castlemandisease—stillmore pages 7-9): Mariusz Sikora, Nel Dąbrowska-Leonik, Piotr Buda, Beata Wolska-Kuśnierz, Karina Jahnz-Różyk, Małgorzata Pac, and Ewa Więsik-Szewczyk. Castleman disease—still more questions than answers: a case report and review of the literature. Journal of Clinical Medicine, 14:2799, Apr 2025. URL: https://doi.org/10.3390/jcm14082799, doi:10.3390/jcm14082799. This article has 2 citations.

22. (sikora2025castlemandisease—stillmore pages 12-14): Mariusz Sikora, Nel Dąbrowska-Leonik, Piotr Buda, Beata Wolska-Kuśnierz, Karina Jahnz-Różyk, Małgorzata Pac, and Ewa Więsik-Szewczyk. Castleman disease—still more questions than answers: a case report and review of the literature. Journal of Clinical Medicine, 14:2799, Apr 2025. URL: https://doi.org/10.3390/jcm14082799, doi:10.3390/jcm14082799. This article has 2 citations.

23. (jitaru2026snapshotlookat pages 8-9): Ciprian Jitaru, Natalia Zlampa, Delia Dima, Anca Bojan, Mihnea Zdrenghea, Laura Urian, David Kegyes, Anamaria Bancos, Maria Santa, Andrei Ivancuta, Bobe Petrushev, Madalina Nistor, Bogdan Tigu, Catalin Constantinescu, Bogdan Fetica, Maria Puiu, Mihai‐Stefan Muresan, and Ciprian Tomuleasa. Snapshot look at castleman disease. Journal of Cellular and Molecular Medicine, Feb 2026. URL: https://doi.org/10.1111/jcmm.70961, doi:10.1111/jcmm.70961. This article has 1 citations and is from a peer-reviewed journal.

24. (nishikori2024transcriptomeanalysisof pages 1-2): Asami Nishikori, Midori Filiz Nishimura, Shuta Tomida, Ryota Chijimatsu, Himawari Ueta, You Cheng Lai, Yuri Kawahara, Yudai Takeda, Sayaka Ochi, Tomoka Haratake, Daisuke Ennishi, Naoya Nakamura, Shuji Momose, and Yasuharu Sato. Transcriptome analysis of the cytokine storm-related genes among the subtypes of idiopathic multicentric castleman disease. Journal of Clinical and Experimental Hematopathology : JCEH, 64:297-306, Oct 2024. URL: https://doi.org/10.3960/jslrt.24061, doi:10.3960/jslrt.24061. This article has 4 citations.

25. (smith2025spatialandsingle pages 6-8): David Smith, Anna Eichinger, É. Fennell, Z. Xu-Monette, Andrew Rech, Julia Wang, E. Esteva, Arta Seyedian, Xiaoxu Yang, Mei Zhang, Dan Martinez, Kai Tan, Minjie Luo, Katherine J Young, Paul G Murray, Christopher Y Park, Boris Reizis, and Vinodh Pillai. Spatial and single cell mapping of castleman disease reveals key stromal cell types and cytokine pathways. Nature Communications, Jul 2025. URL: https://doi.org/10.1038/s41467-025-61214-1, doi:10.1038/s41467-025-61214-1. This article has 11 citations and is from a highest quality peer-reviewed journal.

26. (smith2025spatialandsingle pages 6-6): David Smith, Anna Eichinger, É. Fennell, Z. Xu-Monette, Andrew Rech, Julia Wang, E. Esteva, Arta Seyedian, Xiaoxu Yang, Mei Zhang, Dan Martinez, Kai Tan, Minjie Luo, Katherine J Young, Paul G Murray, Christopher Y Park, Boris Reizis, and Vinodh Pillai. Spatial and single cell mapping of castleman disease reveals key stromal cell types and cytokine pathways. Nature Communications, Jul 2025. URL: https://doi.org/10.1038/s41467-025-61214-1, doi:10.1038/s41467-025-61214-1. This article has 11 citations and is from a highest quality peer-reviewed journal.

27. (bustamante2024longitudinalnaturalhistory pages 4-6): Mateo Sarmiento Bustamante, Sheila K. Pierson, Yue Ren, Adam Bagg, Joshua D. Brandstadter, Gordan Srkalovic, Natalie Mango, Daisy Alapat, Mary Jo Lechowicz, Hongzhe Li, Frits Van Rhee, Megan S. Lim, and David C. Fajgenbaum. Longitudinal, natural history study reveals the disease burden of idiopathic multicentric castleman disease. Haematologica, 109:2196-2206, Jan 2024. URL: https://doi.org/10.3324/haematol.2023.283603, doi:10.3324/haematol.2023.283603. This article has 16 citations.

28. (fraticelli2023aclinicalhistological pages 51-53): S Fraticelli. A clinical, histological and transcriptomic characterization of a selected series of castleman disease's cases. Unknown journal, 2023.

29. (chen2025expertperspectivediagnosis pages 6-7): Luke Y.C. Chen, Lu Zhang, and David C. Fajgenbaum. Expert perspective: diagnosis and treatment of castleman disease. Arthritis & rheumatology, Jun 2025. URL: https://doi.org/10.1002/art.43269, doi:10.1002/art.43269. This article has 25 citations and is from a highest quality peer-reviewed journal.

30. (bitektine2024thevalueof pages 1-2): Erica Bitektine, Hamila Hagh-Daoust, René P. Michel, Stephane Isnard, and Jean-Pierre Routy. The value of a pet scan in selecting the best lymph node to biopsy, and confirming the diagnosis of idiopathic multicentric castleman disease with hlh and ebv viremia in a previously healthy adult. European Journal of Case Reports in Internal Medicine, Nov 2024. URL: https://doi.org/10.12890/2024\_004908, doi:10.12890/2024\_004908. This article has 2 citations.

31. (gao2024clinicalfeaturesand pages 1-2): Haicheng Gao, Wenjie Li, Boyuan Zou, Shibo Liu, and Chengli Miao. Clinical features and outcomes of retroperitoneal unicentric castleman disease resected as sarcomas: insights from a high-volume sarcoma center. Frontiers in Surgery, Sep 2024. URL: https://doi.org/10.3389/fsurg.2024.1371968, doi:10.3389/fsurg.2024.1371968. This article has 0 citations.

32. (NCT01441063 chunk 1): Robert Yarchoan. Tocilizumab for KSHV-Associated Multicentric Castleman Disease. National Cancer Institute (NCI). 2011. ClinicalTrials.gov Identifier: NCT01441063

33. (li2025realworlddataof pages 1-2): Si-yuan Li, Yu-han Gao, Yue Dang, Long Chang, Kai-ni Shen, Hua-cong Cai, Dan-qing Zhao, Chong Wei, Jun Feng, Lu Zhang, and Jian Li. Real-world data of siltuximab for chinese patients with imcd: combination with bcd regimen as a potential approach for severe cases. Annals of Hematology, 104:1713-1720, Apr 2025. URL: https://doi.org/10.1007/s00277-025-06329-7, doi:10.1007/s00277-025-06329-7. This article has 8 citations and is from a peer-reviewed journal.

34. (li2025realworlddataof pages 4-5): Si-yuan Li, Yu-han Gao, Yue Dang, Long Chang, Kai-ni Shen, Hua-cong Cai, Dan-qing Zhao, Chong Wei, Jun Feng, Lu Zhang, and Jian Li. Real-world data of siltuximab for chinese patients with imcd: combination with bcd regimen as a potential approach for severe cases. Annals of Hematology, 104:1713-1720, Apr 2025. URL: https://doi.org/10.1007/s00277-025-06329-7, doi:10.1007/s00277-025-06329-7. This article has 8 citations and is from a peer-reviewed journal.

35. (NCT07085039 chunk 1):  Ruxolitinib in Previously Treated Idiopathic Multicentric Castleman Disease. University of Pennsylvania. 2025. ClinicalTrials.gov Identifier: NCT07085039

36. (NCT04585893 chunk 1):  Safety and Efficacy of Rituximab for Treatment of Multicentric Castleman Disease in Malawi. UNC Lineberger Comprehensive Cancer Center. 2021. ClinicalTrials.gov Identifier: NCT04585893

37. (kobrin2026castlemandisease pages 3-5): Dale M. Kobrin and D. Fajgenbaum. Castleman disease. Advances in Lymphatic Medicine, Mar 2026. URL: https://doi.org/10.5772/intechopen.1009424, doi:10.5772/intechopen.1009424. This article has 0 citations.

38. (alnoor2025theevolutionand pages 3-3): FNU Alnoor, Nicholas C. Spies, Jyoti Kumar, Peyman Samghabadi, Oscar Silva, Matt X. Luo, Karen M. Chisholm, Jingjing Zhang, Alexandra Rangel, David Ng, Peng Li, and Robert S. Ohgami. The evolution and recent advances in diagnostic criteria for idiopathic multicentric castleman disease. American Journal of Hematology, 100:2064-2073, Aug 2025. URL: https://doi.org/10.1002/ajh.70039, doi:10.1002/ajh.70039. This article has 3 citations and is from a domain leading peer-reviewed journal.

39. (patel2024castlemandiseasea pages 3-4): Jay P Patel, Deep P Patel, Trishul H Amin, Rushikesh K Dave, Daksh Hardaswani, Faizanali Saiyed, and Rushita J Goswami. Castleman disease: a rare lymphoproliferative disorder with diverse clinical presentation, diagnosis, and treatment approach. Cureus, Sep 2024. URL: https://doi.org/10.7759/cureus.69149, doi:10.7759/cureus.69149. This article has 5 citations.

40. (fraticelli2023aclinicalhistological pages 15-22): S Fraticelli. A clinical, histological and transcriptomic characterization of a selected series of castleman disease's cases. Unknown journal, 2023.

41. (NCT03933904 chunk 2):  Sirolimus in Previously Treated Idiopathic Multicentric Castleman Disease. University of Pennsylvania. 2019. ClinicalTrials.gov Identifier: NCT03933904

42. (NCT07085039 chunk 2):  Ruxolitinib in Previously Treated Idiopathic Multicentric Castleman Disease. University of Pennsylvania. 2025. ClinicalTrials.gov Identifier: NCT07085039

43. (NCT01441063 chunk 2): Robert Yarchoan. Tocilizumab for KSHV-Associated Multicentric Castleman Disease. National Cancer Institute (NCI). 2011. ClinicalTrials.gov Identifier: NCT01441063

44. (NCT04585893 chunk 2):  Safety and Efficacy of Rituximab for Treatment of Multicentric Castleman Disease in Malawi. UNC Lineberger Comprehensive Cancer Center. 2021. ClinicalTrials.gov Identifier: NCT04585893