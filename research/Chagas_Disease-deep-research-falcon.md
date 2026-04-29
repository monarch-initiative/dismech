---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:50:38.869096'
end_time: '2026-04-04T13:02:22.648377'
duration_seconds: 703.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chagas disease
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 80
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chagas disease
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Chagas disease** covering all of the
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
- **Disease Name:** Chagas disease
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Chagas disease** covering all of the
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


## Comprehensive Research Report: Chagas disease (American trypanosomiasis)

### Target disease
**Chagas disease** is a chronic, often lifelong zoonotic infection caused by the protozoan parasite *Trypanosoma cruzi*. Transmission is classically vector-borne via triatomine (“kissing bug”) feces contaminating skin/mucosa, but important non-vector routes include congenital (vertical), blood transfusion, organ transplantation, and oral/foodborne outbreaks. Infections are frequently silent for years to decades, but a subset progress to chronic cardiac and/or digestive disease with substantial morbidity and mortality. (cucunuba2024theepidemiologyof pages 1-2, cucunuba2024theepidemiologyof pages 7-9)

| Domain | Key finding | Quantitative data | Source (author year journal) | URL/DOI |
|---|---|---:|---|---|
| Epidemiology | Global population at risk in the Americas | ~75 million at risk | Cucunubá et al. 2024, *Lancet Regional Health – Americas* (cucunuba2024theepidemiologyof pages 2-3) | https://doi.org/10.1016/j.lana.2024.100881 |
| Epidemiology | Global number infected | 6.26 million (2010) to 6.30 million (2021) by GBD; WHO/PAHO estimates ~5.7 million in 21 endemic countries | Cucunubá et al. 2024, *Lancet Regional Health – Americas* (cucunuba2024theepidemiologyof pages 9-10, cucunuba2024theepidemiologyof pages 10-11) | https://doi.org/10.1016/j.lana.2024.100881 |
| Epidemiology | Annual incidence | WHO/PAHO ~40,000 new infections/year; historical decline from ~200,000/year in early 1990s to ~40,000/year by 2010 | Cucunubá et al. 2024, *Lancet Regional Health – Americas* (cucunuba2024theepidemiologyof pages 2-3, cucunuba2024theepidemiologyof pages 10-11) | https://doi.org/10.1016/j.lana.2024.100881 |
| Epidemiology | Underdiagnosis and treatment gap | >90% undiagnosed overall; ~70% unaware of infection; ~1% receive etiologic treatment | Cucunubá et al. 2024, *Lancet Regional Health – Americas* (cucunuba2024theepidemiologyof pages 2-3, cucunuba2024theepidemiologyof pages 1-2) | https://doi.org/10.1016/j.lana.2024.100881 |
| Epidemiology | Congenital transmission risk | Usually ~1–2% to ~5–6%; meta-analytic estimates ~4.7% and ~2.0%; pooled migrant setting estimate 4.4% | Cucunubá et al. 2024, *Lancet Regional Health – Americas*; de Andrade et al. 2024, *Lancet Regional Health – Europe* (cucunuba2024theepidemiologyof pages 2-3, cucunuba2024theepidemiologyof pages 3-5, andrade2024prevalenceofchagas pages 1-2) | https://doi.org/10.1016/j.lana.2024.100881 ; https://doi.org/10.1016/j.lanepe.2024.101040 |
| Diagnostics | Chronic Chagas diagnosis requires serologic confirmation with 2 assays | At least 2 different serologic assays; if discordant, add a 3rd test | Schijman et al. 2024, *Lancet Regional Health – Americas*; Lopez-Albizu et al. 2023, *Frontiers in Parasitology* (schijman2024retrospectadvancesand pages 8-9, schijman2024retrospectadvancesand pages 4-6, lopezalbizu2023laboratorydiagnosisof pages 6-7) | https://doi.org/10.1016/j.lana.2024.100821 ; https://doi.org/10.3389/fpara.2023.1138375 |
| Diagnostics | Serology performance for chronic disease | ELISA sensitivity 77.4–100%; specificity 84.2–100%; chronic-stage tests mean sensitivity 94.66%, specificity 91.76% | Ascanio et al. 2024, *Frontiers in Microbiology* (ascanio2024invitrodiagnostic pages 1-2, ascanio2024invitrodiagnostic pages 8-9) | https://doi.org/10.3389/fmicb.2024.1393992 |
| Diagnostics | Acute/congenital diagnosis relies on parasite detection or molecular methods | PCR sensitivities 58.88–100%; specificities 68.8–100%; qPCR for vertical infection 84.2–100%; microhematocrit preferred in neonates | Ascanio et al. 2024, *Frontiers in Microbiology*; Lopez-Albizu et al. 2023, *Frontiers in Parasitology*; Schijman et al. 2024, *Lancet Regional Health – Americas* (ascanio2024invitrodiagnostic pages 1-2, ascanio2024invitrodiagnostic pages 8-9, lopezalbizu2023laboratorydiagnosisof pages 6-7, schijman2024retrospectadvancesand pages 2-3, pinazo2023clinicaluseof pages 1-2) | https://doi.org/10.3389/fmicb.2024.1393992 ; https://doi.org/10.3389/fpara.2023.1138375 ; https://doi.org/10.1016/j.lana.2024.100821 |
| Treatment | Etiologic therapy is most effective in acute disease | Acute-phase cure rate ~60–85% | Farani et al. 2024, *Vaccines* (farani2024treatmentsandthe pages 2-4) | https://doi.org/10.3390/vaccines12080870 |
| Treatment | Pre-pregnancy trypanocidal therapy prevents congenital transmission | OR 0.05 (95% CI 0.01–0.27); pooled congenital Chagas prevalence 0.0% (95% CI 0–0.91%) in offspring of treated women | de Moraes et al. 2024, *PLOS Neglected Tropical Diseases* (moraes2024preventionofcongenital pages 6-8, moraes2024preventionofcongenital pages 4-6, moraes2024preventionofcongenital pages 1-2) | https://doi.org/10.1371/journal.pntd.0012407 |
| Treatment | Adverse events with benznidazole vs nifurtimox in a recent real-world comparison | ≥1 AE: BNZ 65% (79/121) vs NFX 84% (96/115); mean AE duration 0.7 vs 1.7 days; AE intensity 1.1 vs 2.1; 2 dropouts due to AEs in NFX only | Kann et al. 2024, *Journal of Clinical Medicine* (kann2024chagasdiseasecomparison pages 1-2) | https://doi.org/10.3390/jcm13092565 |
| Prevention / vector control | Añatuya 14-year ecohealth program reduced household infestation | Intra-domiciliary infestation 17.9% → 0.2%; peri-domiciliary 20.4% → 3%; 4,193 inspections; 399 households structurally improved | Weinberg et al. 2023, *PLOS Neglected Tropical Diseases* (weinberg2023chagaspreventionand pages 1-2) | https://doi.org/10.1371/journal.pntd.0011410 |
| Prevention / vector control | Pampa del Indio 9-year intervention reduced infected-vector prevalence | *T. cruzi* infection prevalence in *Triatoma infestans* 24.1% at baseline → 0.9% at endpoint among 6,397 bugs examined | Gürtler et al. 2023, *Parasites & Vectors* (gurtler2023thepampadel pages 1-2) | https://doi.org/10.1186/s13071-023-05861-7 |
| Prevention / vector control | Pyrethroid resistance sustains infestation hotspots | House infestation 33.8% (2018) and 31.6% (2020); peridomestic 26.4–26.7%; domestic 12.2% → 8.3% | Cecere et al. 2024, *Parasites & Vectors* (cecere2024slowrecoveryrates pages 1-2) | https://doi.org/10.1186/s13071-024-06366-7 |
| Quality of life / implementation | Exercise-based cardiac rehabilitation improved short-term QoL in CCC | At 3 months: physical functioning β=+10.7 (p=0.02), role-physical β=+25.0 (p=0.01), social functioning β=+19.2 (p<0.01); no significant between-group differences at 6 months | Vieira et al. 2024, *Scientific Reports* (vieira2024effectofan pages 1-2, vieira2024effectofan pages 3-4) | https://doi.org/10.1038/s41598-024-58776-3 |


*Table: This table compiles high-yield quantitative findings on Chagas disease epidemiology, diagnosis, treatment, and prevention/public-health implementation from the evidence gathered. It is designed as a quick-reference artifact for a research report or disease knowledge base entry.*

## 1. Disease information
### 1.1 Overview and definitions
Chagas disease is a long-lasting infection in which most acute infections are clinically mild or asymptomatic, followed by a chronic phase that can remain indeterminate for decades; approximately **30–40%** of infected individuals develop symptomatic chronic disease, frequently cardiac involvement. (cucunuba2024theepidemiologyof pages 9-10, cucunuba2024theepidemiologyof pages 7-9)

### 1.2 Synonyms and alternative names
- **American trypanosomiasis** (common synonym used in clinical/public-health settings). (cucunuba2024theepidemiologyof pages 1-2)
- **Trypanosoma cruzi infection** (etiologic phrasing frequently used in diagnostics and guidelines). (ascanio2024invitrodiagnostic pages 1-2, forsyth2022recommendationsforscreening pages 3-4)

### 1.3 Key identifiers (ontology / coding)
- **MONDO ID**: not retrieved in the tool-based evidence available in this run; MONDO is described as a disease-ontology unification framework, but this specific disease’s MONDO identifier was not captured in the retrieved texts. (cucunuba2024theepidemiologyof pages 2-3)
- **ICD / MeSH / Orphanet / OMIM**: not reliably extractable from the retrieved evidence set in this run; therefore not asserted here.

### 1.4 Evidence source type (patient-level vs aggregated)
Most quantitative estimates in this report come from **aggregated sources** (systematic reviews, meta-analyses, guideline statements, modeling/GBD estimates, and long-running intervention programs). (cucunuba2024theepidemiologyof pages 2-3, andrade2024prevalenceofchagas pages 1-2, weinberg2023chagaspreventionand pages 1-2, forsyth2022recommendationsforscreening pages 3-4)

## 2. Etiology
### 2.1 Primary causes
- **Causative agent**: *Trypanosoma cruzi*, an intracellular protozoan parasite (zoonotic). (cucunuba2024theepidemiologyof pages 1-2)
- **Transmission routes (with quantitative estimates where available)**:
  - **Vector-borne**: main driver across the Americas; transmission occurs when triatomines feed and contaminate the bite site with infective feces/urine. (cucunuba2024theepidemiologyof pages 1-2)
  - **Congenital**: mother-to-child transmission probability often **~1–2% to ~5–6%**, with meta-analytic estimates ranging from **~2.0%** to **~4.7%** depending on period and setting. (cucunuba2024theepidemiologyof pages 2-3, cucunuba2024theepidemiologyof pages 3-5)
  - **Transfusion-associated**: risk estimated **~10–20% per infected blood unit** in endemic countries (with component-specific estimates also reported). (cucunuba2024theepidemiologyof pages 2-3)
  - **Organ transplantation**: risk varies substantially (reported roughly **~13–75%**, depending on organ and setting). (cucunuba2024theepidemiologyof pages 2-3)
  - **Oral/foodborne outbreaks**: associated with **higher clinical severity** and reported crude case-fatality rates around **~4–6.5%** in compiled series. (cucunuba2024theepidemiologyof pages 9-10)

### 2.2 Risk factors
#### Environmental / socioeconomic
- Living in rural/peri-urban settings with **vector-infested housing**, often tied to poverty and substandard construction, increases risk of vector-borne transmission; large-scale vector programs target these conditions. (weinberg2023chagaspreventionand pages 1-2, gurtler2023thepampadel pages 1-2)

#### Demographic / clinical
- Risk of chronic cardiac disease: approximately **30–40%** develop symptomatic chronic disease; about one-third develop chronic cardiac disease, with annual progression rates reported **~2–7%** among those at risk in some settings. (cucunuba2024theepidemiologyof pages 9-10, higuita2024chagasdiseasein pages 1-2)

#### Parasite diversity
- *T. cruzi* has multiple discrete typing units (DTUs TcI–TcVI), broadly distributed across the Americas; DTU variability may influence clinical and immunologic phenotypes, but proinflammatory cytokine patterns are described across DTUs. (cucunuba2024theepidemiologyof pages 7-9, albaalvarado2024thefunctionsof pages 8-10)

### 2.3 Protective factors
- **Preconception etiologic treatment of infected women** (benznidazole or nifurtimox) is supported by observational evidence as a protective factor against congenital transmission (see Treatment/Prevention sections). (moraes2024preventionofcongenital pages 1-2)

### 2.4 Gene–environment (host–pathogen) interactions
- Disease progression appears to reflect **host genetic predisposition interacting with chronic inflammatory signaling**. Whole-exome sequencing studies in families with different clinical outcomes have identified **rare heterozygous pathogenic variants in mitochondrial and inflammatory genes** segregating with chronic Chagas cardiomyopathy (CCC), supporting the hypothesis that cytokine-driven mitochondrial dysfunction in genetically predisposed individuals contributes to severity. (nunes2023inflammationandmitochondria pages 1-2)
- Candidate host polymorphisms in cytokine/chemokine pathways (e.g., **TGFB1, CCR5, IFNG**, IL10-related loci) have been reported, but authoritative reviews emphasize that **“solid genetic biomarkers are lacking”** given dependence on host and parasite biology. (albaalvarado2024thefunctionsof pages 8-10, albaalvarado2024thefunctionsof pages 8-8)

## 3. Phenotypes (clinical manifestations)
Chagas disease is commonly conceptualized as **acute → chronic indeterminate → chronic determinate** (cardiac and/or digestive) phenotypes.

### 3.1 Acute infection
- Often silent: initial infection is asymptomatic in ~**95%** of vector-mediated cases. (cucunuba2024theepidemiologyof pages 7-9)
- Acute infections typically last **~4–8 weeks**. (cucunuba2024theepidemiologyof pages 9-10)
- **Suggested HPO terms** (examples): Fever (HP:0001945), Periorbital edema (HP:0000520; aligns with Romaña sign when present), Myocarditis (HP:0001637).

### 3.2 Chronic indeterminate form
- Indeterminate chronic infection can last decades; **60–70%** may never progress to symptomatic disease. (cucunuba2024theepidemiologyof pages 7-9)
- **Suggested HPO terms**: Asymptomatic (HP:0003745), Abnormal ECG (HP:0001650).

### 3.3 Chronic Chagas cardiomyopathy (CCC)
- CCC is characterized by myocarditis and fibrosis leading to **conduction disorders, arrhythmias, and progressive ventricular dilation**. (nunes2023inflammationandmitochondria pages 2-3)
- Clinically, a 2024 cytokine-focused review describes that ~**27%** of patients develop progressive heart failure with conduction defects, apical aneurysms, thrombi, and reduced ejection fraction. (albaalvarado2024thefunctionsof pages 1-2)
- **Suggested HPO terms**: Dilated cardiomyopathy (HP:0001644), Ventricular arrhythmia (HP:0004756), Heart failure (HP:0001635), Bundle branch block (HP:0011710), Apical aneurysm (HP:0031557).

### 3.4 Digestive Chagas disease
- Digestive complications (classically megaesophagus/megacolon) are established clinical manifestations; however, robust frequency estimates were not available in the retrieved 2023–2024 primary evidence set used here.
- **Suggested HPO terms**: Megacolon (HP:0002563), Esophageal dysmotility (HP:0007047), Dysphagia (HP:0002015), Constipation (HP:0002019).

### 3.5 Congenital Chagas disease
- Congenital transmission risk is commonly reported in the **low single-digit percent range** (see Etiology/Epidemiology). (cucunuba2024theepidemiologyof pages 3-5, andrade2024prevalenceofchagas pages 1-2)
- **Suggested HPO terms**: Hepatosplenomegaly (HP:0001433), Neonatal infection (HP:0002715), Myocarditis (HP:0001637).

### 3.6 Quality-of-life impact (CCC)
A randomized trial (PEACH) in CCC with reduced ejection fraction evaluated SF-36 outcomes. Exercise-based cardiac rehabilitation produced **short-term QoL improvements** at 3 months (physical functioning β=+10.7; role-physical β=+25.0; social functioning β=+19.2), with no sustained between-group differences at 6 months. (vieira2024effectofan pages 1-2, vieira2024effectofan pages 3-4)

## 4. Genetic / molecular information
### 4.1 Causal genes
Chagas disease is **infectious** rather than Mendelian; there are no single causal human genes.

### 4.2 Host susceptibility / modifier genetics
- CCC risk and severity are linked to immune and inflammatory pathways; reported candidate associations include variants in cytokine and chemokine axes (e.g., TGFB1, CCR5, IFNG, IL10 pathway), but consensus biomarkers remain insufficient. (albaalvarado2024thefunctionsof pages 8-10, albaalvarado2024thefunctionsof pages 8-8)
- WES-based family studies suggest rare variants in **mitochondrial and inflammatory genes** may modify progression to CCC. (nunes2023inflammationandmitochondria pages 1-2)

### 4.3 Parasite genetics (clinically relevant diversity)
- Broad geographic distribution of DTUs (TcI–TcVI) across the Americas is described; DTU variability may influence magnitude of inflammation and clinical patterns, but proinflammatory profiles are described across DTUs. (cucunuba2024theepidemiologyof pages 7-9, albaalvarado2024thefunctionsof pages 8-10)

## 5. Environmental information
### 5.1 Environmental and housing factors
- Household construction and peridomestic ecologies drive vector colonization; interventions coupling surveillance, insecticide application, and **structural housing improvements** are effective in reducing infestation (see Prevention). (weinberg2023chagaspreventionand pages 1-2)

### 5.2 Lifestyle factors
Not specifically quantified in the retrieved evidence set.

### 5.3 Infectious agent
- *Trypanosoma cruzi* (protozoan). (cucunuba2024theepidemiologyof pages 1-2)

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (CCC-focused)
A contemporary mechanistic model supported by recent reviews is:
1) **Persistent low-level infection / antigenic stimulation** in chronic disease (low parasitemia but continued immune activation) (nunes2023inflammationandmitochondria pages 1-2)
2) **Innate sensing via TLR pathways** (e.g., TLR2/4 and endosomal TLR7/9) signaling through **MyD88 → NF-κB** and inflammasome activation, driving IL-12 and Th1 differentiation (nunes2023inflammationandmitochondria pages 1-2, albaalvarado2024thefunctionsof pages 1-2)
3) **Th1-rich myocarditis** with high IFN-γ/TNF-α and chemokine-driven recruitment (e.g., CCL5, CXCL9/CXCL10), with CD8+ infiltration (nunes2023inflammationandmitochondria pages 2-3, albaalvarado2024thefunctionsof pages 4-5)
4) **Fibrosis and remodeling** (TGF-β pathway involvement; ECM regulators such as MMP-2/MMP-9, fibronectin) contributing to conduction disease and ventricular dilation (albaalvarado2024thefunctionsof pages 4-5, albaalvarado2024thefunctionsof pages 7-8)
5) **Mitochondrial dysfunction and metabolic impairment** in cardiomyocytes: reduced oxidative phosphorylation capacity and high-energy phosphate levels, impaired ATP production; IFN-γ/TNF-α signaling can negatively affect mitochondrial function and redox homeostasis, linking inflammation to bioenergetic failure. (nunes2023inflammationandmitochondria pages 1-2, nunes2023inflammationandmitochondria pages 2-3)

### 6.2 Key pathways and mediators (ontology suggestions)
- **GO Biological Process (examples)**: inflammatory response (GO:0006954), cytokine-mediated signaling pathway (GO:0019221), regulation of apoptotic process (GO:0042981), extracellular matrix organization (GO:0030198), collagen fibril organization (GO:0030199), mitochondrial ATP synthesis coupled electron transport (GO:0042776).
- **Cell types (CL examples)**: CD8-positive T cell (CL:0000625), macrophage (CL:0000235), cardiac fibroblast (CL:0002548), cardiomyocyte (CL:0000746), dendritic cell (CL:0000451).

### 6.3 Biochemical and immunometabolic abnormalities
- CCC myocardium shows reduced expression of mitochondrial energy metabolism enzymes, reduced high-energy phosphates and impaired ATP generation; cytokine signaling (IFN-γ/TNF-α) is linked mechanistically to mitochondrial dysfunction and nitro-oxidative stress. (nunes2023inflammationandmitochondria pages 1-2, nunes2023inflammationandmitochondria pages 2-3)

## 7. Anatomical structures affected
### 7.1 Primary organ systems
- **Cardiovascular system**: myocardium, conduction system (arrhythmias, conduction blocks), progressive ventricular dilation and fibrosis. (nunes2023inflammationandmitochondria pages 2-3)
- **Digestive system**: colon and esophagus (megacolon/megaesophagus as recognized chronic phenotypes, though frequencies not extracted from the present evidence set). (forsyth2022recommendationsforscreening pages 3-4)

### 7.2 UBERON suggestions (examples)
- Heart (UBERON:0000948), myocardium (UBERON:0002349), cardiac conduction system (UBERON:0004537), esophagus (UBERON:0001043), colon (UBERON:0001155).

## 8. Temporal development
- **Acute phase**: typically 4–8 weeks; often asymptomatic. (cucunuba2024theepidemiologyof pages 9-10, cucunuba2024theepidemiologyof pages 7-9)
- **Chronic phase**: prolonged indeterminate stage can last decades; symptomatic progression occurs in ~30–40% overall, with annual progression rates to cardiomyopathy reported ~2–7% in some estimates. (cucunuba2024theepidemiologyof pages 9-10, higuita2024chagasdiseasein pages 1-2, cucunuba2024theepidemiologyof pages 7-9)

## 9. Inheritance and population
### 9.1 Epidemiology (2023–2024 prioritized)
- **Americas at risk**: ~75 million people. (Cucunubá et al., Sep 2024) (cucunuba2024theepidemiologyof pages 2-3)
- **Global infected**: GBD estimates ~6.26 million (2010) increasing slightly to ~6.30 million (2021). (Cucunubá et al., Sep 2024) (cucunuba2024theepidemiologyof pages 10-11)
- **Undiagnosed / unaware**: likely >90% undiagnosed overall; ~70% unaware; ~1% receive etiologic treatment. (cucunuba2024theepidemiologyof pages 2-3, cucunuba2024theepidemiologyof pages 1-2)
- **Non-endemic countries (migration-associated prevalence)**: In Latin American immigrants in non-endemic countries, pooled prevalence ~3.5% overall, with very high prevalence among Bolivian migrants (~21.5%). (de Andrade et al., Nov 2024) (andrade2024prevalenceofchagas pages 1-2)
- **United States**: estimated 326,000–347,000 infected; annual congenital infections estimated 22–108; <1% access testing and treatment. (Higuita et al., Jun 2024; Forsyth et al., Oct 2022) (higuita2024chagasdiseasein pages 1-2, forsyth2022recommendationsforscreening pages 1-2)

## 10. Diagnostics
### 10.1 Current diagnostic principles
Because parasitemia is high in acute infection but low/intermittent in chronic infection, diagnostic strategy is phase-dependent, illustrated in a 2024 Lancet Regional Health–Americas diagnostic algorithm figure (stage-dependent transition from parasitemia-based tests to serology). (schijman2024retrospectadvancesand media 49150249)

### 10.2 Chronic infection diagnosis (serology)
**WHO/PAHO standard**: confirm chronic infection using **two assays with different principles**; if discordant, perform a third test. A 2024 comprehensive review states: **“[WHO] recommends to use at least two assays with different principles to conﬁrm a positive serological result for *T. cruzi* infection.”** (Schijman et al., Aug 2024) (schijman2024retrospectadvancesand pages 8-9, schijman2024retrospectadvancesand pages 4-6)

PAHO/WHO diagnostic standard is operationalized as requiring reactive results on two tests of different principles/antigens, with a third test if only one is reactive. (lopezalbizu2023laboratorydiagnosisof pages 6-7)

### 10.3 Acute / congenital infection diagnosis
- Recommended approaches include **direct parasitological methods** (e.g., microhematocrit) and **molecular testing (PCR/qPCR)**; parasitological methods are operator dependent and can have limited sensitivity, while PCR enables rapid and sensitive detection but is cost/infrastructure intensive. (schijman2024retrospectadvancesand pages 8-9, schijman2024retrospectadvancesand pages 4-6)
- Microhematocrit is highlighted as preferred for congenital diagnosis in neonates, with serologic follow-up later if early tests are negative. (schijman2024retrospectadvancesand pages 2-3)

### 10.4 Recent diagnostic performance data (2024)
A 2024 scoping review quantified broad performance ranges:
- ELISA sensitivity **77.4–100%** and specificity **84.2–100%** across studies. (ascanio2024invitrodiagnostic pages 1-2)
- PCR-based methods: sensitivity **58.88–100%** and specificity **68.8–100%**; qPCR mean sensitivity ~82.84% and specificity ~94.01% in the compiled review. (ascanio2024invitrodiagnostic pages 8-9)

### 10.5 Real-world implementation issues
- Multi-test algorithms and infrastructure needs contribute to delayed turnaround and loss to follow-up in low-resource settings. (schijman2024retrospectadvancesand pages 4-6)
- In the U.S., experts note that most commercial labs start with a single IgG assay; ensuring two distinct assays often requires confirming which assay was used and potentially sending specimens to CDC for confirmation. (forsyth2022recommendationsforscreening pages 7-8)

### 10.6 U.S. screening guidance (authoritative)
A U.S. expert working group recommends testing people born in or with prolonged residence in endemic regions of Mexico/Central/South America, screening family members of those who test positive, and giving special consideration to women of childbearing age and infants born to seropositive mothers. Diagnostic confirmation requires **two distinct assays** (and a third if discordant). (Forsyth et al., Oct 2022) (forsyth2022recommendationsforscreening pages 1-2, forsyth2022recommendationsforscreening pages 2-3)

## 11. Outcome / prognosis
- Once chronic cardiomyopathy is established, some syntheses cite annual mortality up to **~8%** and increased death risk (e.g., 1.74×) compared with controls/other cardiomyopathies, underscoring severity and the need for early detection. (cucunuba2024theepidemiologyof pages 10-11, higuita2024chagasdiseasein pages 1-2)

## 12. Treatment
### 12.1 Standard etiologic pharmacotherapy
- **Benznidazole (BZN)** and **nifurtimox (NFX)** remain the principal approved etiologic therapies; a 2024 review notes they have been used for ~60 years and that efficacy is highest in acute infection, with a reported **~60–85% cure rate** in the acute phase. (Farani et al., Aug 2024) (farani2024treatmentsandthe pages 2-4)

### 12.2 Chronic-phase effectiveness and “test of cure” limitations
- Serologic cure in chronic infection is slow and uncommon; a 2024 synthesis reports that **“only 15% of patients show negative seroconversion after ten years.”** (farani2024treatmentsandthe pages 2-4)
- The absence of a practical test of cure has motivated guideline incorporation of PCR to detect therapeutic failure in some contexts. (pinazo2023clinicaluseof pages 1-2)

### 12.3 Safety / adverse events (real-world 2024)
In a Colombian indigenous-community comparison, adverse events occurred in **65%** (79/121) of BNZ-treated patients versus **84%** (96/115) of NFX-treated patients, with longer and more severe AEs in the NFX group and dropouts due to AEs only in NFX. (Kann et al., Apr 2024) (kann2024chagasdiseasecomparison pages 1-2)

### 12.4 Preventing congenital Chagas via treatment before pregnancy (2024 meta-analysis)
A 2024 meta-analysis of observational studies found that prior trypanocidal treatment in women of reproductive age strongly reduced congenital transmission, reporting **OR 0.05 (95% CI 0.01–0.27)** and **0.0% pooled prevalence** of congenital Chagas among offspring of treated mothers (95% CI 0–0.91%). (de Moraes et al., Sep 2024) (moraes2024preventionofcongenital pages 4-6, moraes2024preventionofcongenital pages 1-2)

### 12.5 Recent developments: shortened benznidazole regimens and trials
- **BENDITA (NCT03378661)**: randomized, masked Phase 2 trial evaluating shortened and alternative benznidazole regimens (including 2- and 4-week strategies and combinations with E1224/fosravuconazole), focusing on sustained PCR clearance and tolerability. (NCT03378661 chunk 1, NCT03378661 chunk 2)
- **NuestroBen (NCT04897516)**: recruiting Phase 3 non-inferiority trial comparing **2-week** and **4-week** benznidazole regimens versus standard **8-week** therapy, using sustained qualitative PCR negativity through 12 months as the primary efficacy endpoint, and comprehensive safety/adherence endpoints. (NCT04897516 chunk 1, NCT04897516 chunk 2)

**MAXO suggestions (examples)**: antiparasitic therapy (MAXO:0000788), benznidazole administration (as a drug intervention concept), nifurtimox administration, prenatal screening (MAXO:0000934), vector control intervention (MAXO:0000753), cardiac rehabilitation therapy (MAXO:0000554).

## 13. Prevention
### 13.1 Primary prevention: vector control and housing improvement
A 14-year ecohealth program in rural Argentina (Añatuya) combining surveillance, insecticide use, health promotion, and **community-led structural housing improvements** reduced intra-domiciliary infestation from **17.9% to 0.2%** and peri-domiciliary infestation from **20.4% to 3%**, with 399 households structurally improved. (Weinberg et al., Jun 2023) (weinberg2023chagaspreventionand pages 1-2)

### 13.2 Sustained surveillance + spraying: parasite-based transmission indices
In the Pampa del Indio project (Argentina, 2007–2016), infection prevalence in *Triatoma infestans* fell from **24.1% at baseline to 0.9% at endpoint** (6,397 bugs examined), aligning with human serosurveys and suggesting interruption of vector-borne transmission. (Gürtler et al., Aug 2023) (gurtler2023thepampadel pages 1-2)

### 13.3 Challenges: insecticide resistance and hotspot persistence (2024)
A 2024 longitudinal survey in a high pyrethroid-resistance area reported persistent infestation (house infestation **33.8% in 2018** and **31.6% in 2020**) with spatially aggregated hotspots; the authors recommend targeting hotspots, house-modification measures, and judicious use of alternative insecticides. (Cecere et al., Jul 2024) (cecere2024slowrecoveryrates pages 1-2)

### 13.4 Secondary prevention: screening programs
- In non-endemic settings, **pregnancy and blood/organ donation** pathways are high-yield points for detection and prevention of congenital/transfusion/transplant transmission. (forsyth2022recommendationsforscreening pages 3-4, hochberg2023chagasdisease pages 4-6)

### 13.5 Tertiary prevention: preventing complications in established disease
- Cardiac management (ECG/echo surveillance) is recommended even for asymptomatic confirmed infections to identify indeterminate vs organ involvement and guide follow-up. (forsyth2022recommendationsforscreening pages 3-4)
- Exercise-based cardiac rehabilitation can improve QoL short-term in CCC (implementation-level supportive intervention). (vieira2024effectofan pages 1-2)

## 14. Other species / natural disease (One Health)
### 14.1 Reservoirs and cross-species ecology
Chagas disease involves complex zoonotic cycles; transmission cycles involve many mammalian host species, and *T. cruzi* infects a wide range of mammals. (cucunuba2024theepidemiologyof pages 1-2, duraesoliveira2024chagasdiseasea pages 2-4)

### 14.2 Dogs as reservoirs and sentinels
A 2024 One Health review emphasizes dogs as major peridomestic reservoirs and sentinels: dogs “play a major role in the domestic cycle” and develop clinically similar disease to humans, making them useful for surveillance and risk mapping. (Durães-Oliveira et al., Mar 2024) (duraesoliveira2024chagasdiseasea pages 1-2)

Quantitative comparative reservoir evidence from a 2024 dissertation dataset found high and similar lineage-specific seroreactivity in humans (69.5%) and dogs (65.8%) using a rapid test for TcII/V/VI signatures, supporting dogs as highly exposed sentinels in those studied settings. (murphy2024developmentofrapid pages 64-65)

### 14.3 Emerging One Health interventions
Systemic insecticides targeting domestic animals (especially dogs) are being explored to reduce vector populations and contact; a 2024 vector-control paper cites evidence that treating dogs with fluralaner reduced pyrethroid-resistant *T. infestans* abundance and *T. cruzi* infection, highlighting a One Health approach to complement house spraying and surveillance. (pereira2024insecticidalactivityof pages 12-13)

## 15. Model organisms / model systems
The retrieved evidence set in this run did not include primary-methods descriptions of standard experimental models (e.g., specific mouse strains, in vitro cardiomyocyte systems) beyond mechanistic reviews and some preclinical synthesis; therefore, model-organism details are not exhaustively characterized here. Mechanistic studies nevertheless commonly implicate macrophage/innate sensing pathways and cardiomyocyte mitochondrial dysfunction, supporting use of macrophage infection systems and murine cardiomyopathy models in the field. (nunes2023inflammationandmitochondria pages 1-2, albaalvarado2024thefunctionsof pages 1-2)

## Expert opinions and analysis (authoritative sources; 2023–2024 prioritized)
- A 2024 Lancet Regional Health epidemiology synthesis highlights the ethical and societal challenge of Chagas disease driven by underdiagnosis and undertreatment, noting the vast majority of infections go undiagnosed and only ~1% receive etiologic treatment. (cucunuba2024theepidemiologyof pages 2-3)
- Diagnostic experts emphasize that **no single test is a gold standard for all phases**, requiring algorithmic testing (serology for chronic; direct detection/PCR for acute/congenital), and that infrastructure and follow-up losses are major barriers. (ascanio2024invitrodiagnostic pages 1-2, schijman2024retrospectadvancesand pages 4-6)
- CCC mechanistic reviews increasingly frame disease as an interplay between persistent immune activation, fibrosis/remodeling, and mitochondrial/metabolic impairment, potentially modulated by host genetics. (nunes2023inflammationandmitochondria pages 1-2, albaalvarado2024thefunctionsof pages 4-5)

## Visual evidence (diagnostic algorithm and test characteristics)
A 2024 comprehensive diagnostic review provides a stage-dependent diagnostic algorithm (Figure) and tables summarizing assay characteristics and recommended testing strategies, supporting the phase-specific approach described above. (schijman2024retrospectadvancesand media 49150249, schijman2024retrospectadvancesand media 2264cf25, schijman2024retrospectadvancesand media b8b9a0ae)

## Notes on limitations of this report
- Several requested identifier fields (MONDO disease ID, ICD/MeSH/Orphanet/OMIM codes) were not extractable from the retrieved evidence set in this run and are not asserted without direct citation.
- Some phenotype frequencies (especially digestive manifestations) and many model-organism specifics are recognized as important but were not supported by the current retrieved primary evidence excerpts.

## Key references (URLs and publication dates)
- Cucunubá ZM et al. *The Lancet Regional Health – Americas* (Sep 2024). https://doi.org/10.1016/j.lana.2024.100881 (cucunuba2024theepidemiologyof pages 2-3)
- Schijman AG et al. *The Lancet Regional Health – Americas* (Aug 2024). https://doi.org/10.1016/j.lana.2024.100821 (schijman2024retrospectadvancesand pages 8-9)
- Ascanio LC et al. *Frontiers in Microbiology* (Apr 2024). https://doi.org/10.3389/fmicb.2024.1393992 (ascanio2024invitrodiagnostic pages 1-2)
- de Moraes FCA et al. *PLOS Neglected Tropical Diseases* (Sep 2024). https://doi.org/10.1371/journal.pntd.0012407 (moraes2024preventionofcongenital pages 1-2)
- Kann S et al. *Journal of Clinical Medicine* (Apr 2024). https://doi.org/10.3390/jcm13092565 (kann2024chagasdiseasecomparison pages 1-2)
- Vieira MC et al. *Scientific Reports* (Apr 2024). https://doi.org/10.1038/s41598-024-58776-3 (vieira2024effectofan pages 1-2)
- Cecere MC et al. *Parasites & Vectors* (Jul 2024). https://doi.org/10.1186/s13071-024-06366-7 (cecere2024slowrecoveryrates pages 1-2)
- Weinberg D et al. *PLOS Neglected Tropical Diseases* (Jun 2023). https://doi.org/10.1371/journal.pntd.0011410 (weinberg2023chagaspreventionand pages 1-2)
- Nunes JPS et al. *Experimental Biology and Medicine* (Nov 2023). https://doi.org/10.1177/15353702231220658 (nunes2023inflammationandmitochondria pages 1-2)
- Durães-Oliveira J et al. *International Journal of Molecular Sciences* (Mar 2024). https://doi.org/10.3390/ijms25073840 (duraesoliveira2024chagasdiseasea pages 1-2)
- Forsyth CJ et al. *Journal of Infectious Diseases* (Oct 2022). https://doi.org/10.1093/infdis/jiab513 (forsyth2022recommendationsforscreening pages 1-2)
- Hochberg NS, Montgomery SP. *Annals of Internal Medicine* (Feb 2023). https://doi.org/10.7326/aitc202302210 (hochberg2023chagasdisease pages 1-3)

References

1. (cucunuba2024theepidemiologyof pages 1-2): Zulma M. Cucunubá, Sebastián A. Gutiérrez-Romero, Juan-David Ramírez, Natalia Velásquez-Ortiz, Soledad Ceccarelli, Gabriel Parra-Henao, Andrés F. Henao-Martínez, Jorge Rabinovich, María-Gloria Basáñez, Pierre Nouvellet, and Fernando Abad-Franch. The epidemiology of chagas disease in the americas. Lancet Regional Health - Americas, 37:100881, Sep 2024. URL: https://doi.org/10.1016/j.lana.2024.100881, doi:10.1016/j.lana.2024.100881. This article has 128 citations.

2. (cucunuba2024theepidemiologyof pages 7-9): Zulma M. Cucunubá, Sebastián A. Gutiérrez-Romero, Juan-David Ramírez, Natalia Velásquez-Ortiz, Soledad Ceccarelli, Gabriel Parra-Henao, Andrés F. Henao-Martínez, Jorge Rabinovich, María-Gloria Basáñez, Pierre Nouvellet, and Fernando Abad-Franch. The epidemiology of chagas disease in the americas. Lancet Regional Health - Americas, 37:100881, Sep 2024. URL: https://doi.org/10.1016/j.lana.2024.100881, doi:10.1016/j.lana.2024.100881. This article has 128 citations.

3. (cucunuba2024theepidemiologyof pages 2-3): Zulma M. Cucunubá, Sebastián A. Gutiérrez-Romero, Juan-David Ramírez, Natalia Velásquez-Ortiz, Soledad Ceccarelli, Gabriel Parra-Henao, Andrés F. Henao-Martínez, Jorge Rabinovich, María-Gloria Basáñez, Pierre Nouvellet, and Fernando Abad-Franch. The epidemiology of chagas disease in the americas. Lancet Regional Health - Americas, 37:100881, Sep 2024. URL: https://doi.org/10.1016/j.lana.2024.100881, doi:10.1016/j.lana.2024.100881. This article has 128 citations.

4. (cucunuba2024theepidemiologyof pages 9-10): Zulma M. Cucunubá, Sebastián A. Gutiérrez-Romero, Juan-David Ramírez, Natalia Velásquez-Ortiz, Soledad Ceccarelli, Gabriel Parra-Henao, Andrés F. Henao-Martínez, Jorge Rabinovich, María-Gloria Basáñez, Pierre Nouvellet, and Fernando Abad-Franch. The epidemiology of chagas disease in the americas. Lancet Regional Health - Americas, 37:100881, Sep 2024. URL: https://doi.org/10.1016/j.lana.2024.100881, doi:10.1016/j.lana.2024.100881. This article has 128 citations.

5. (cucunuba2024theepidemiologyof pages 10-11): Zulma M. Cucunubá, Sebastián A. Gutiérrez-Romero, Juan-David Ramírez, Natalia Velásquez-Ortiz, Soledad Ceccarelli, Gabriel Parra-Henao, Andrés F. Henao-Martínez, Jorge Rabinovich, María-Gloria Basáñez, Pierre Nouvellet, and Fernando Abad-Franch. The epidemiology of chagas disease in the americas. Lancet Regional Health - Americas, 37:100881, Sep 2024. URL: https://doi.org/10.1016/j.lana.2024.100881, doi:10.1016/j.lana.2024.100881. This article has 128 citations.

6. (cucunuba2024theepidemiologyof pages 3-5): Zulma M. Cucunubá, Sebastián A. Gutiérrez-Romero, Juan-David Ramírez, Natalia Velásquez-Ortiz, Soledad Ceccarelli, Gabriel Parra-Henao, Andrés F. Henao-Martínez, Jorge Rabinovich, María-Gloria Basáñez, Pierre Nouvellet, and Fernando Abad-Franch. The epidemiology of chagas disease in the americas. Lancet Regional Health - Americas, 37:100881, Sep 2024. URL: https://doi.org/10.1016/j.lana.2024.100881, doi:10.1016/j.lana.2024.100881. This article has 128 citations.

7. (andrade2024prevalenceofchagas pages 1-2): Gisele Nepomuceno de Andrade, Pau Bosch-Nicolau, Bruno R. Nascimento, Francisco Rogerlândio Martins-Melo, Pablo Perel, Yvonne Geissbühler, Caroline Demacq, Monica Quijano, Jonathan F. Mosser, Ewerton Cousin, Ísis Eloah Machado, Matheus Lucca A.C. Rodrigues, Antonio Luiz P. Ribeiro, and Israel Molina. Prevalence of chagas disease among latin american immigrants in non-endemic countries: an updated systematic review and meta-analysis. The Lancet Regional Health - Europe, 46:101040, Nov 2024. URL: https://doi.org/10.1016/j.lanepe.2024.101040, doi:10.1016/j.lanepe.2024.101040. This article has 27 citations.

8. (schijman2024retrospectadvancesand pages 8-9): Alejandro Gabriel Schijman, Julio Alonso-Padilla, Constança Britto, and Claudia Patricia Herrera Bernal. Retrospect, advances and challenges in chagas disease diagnosis: a comprehensive review. The Lancet Regional Health - Americas, 36:100821, Aug 2024. URL: https://doi.org/10.1016/j.lana.2024.100821, doi:10.1016/j.lana.2024.100821. This article has 60 citations.

9. (schijman2024retrospectadvancesand pages 4-6): Alejandro Gabriel Schijman, Julio Alonso-Padilla, Constança Britto, and Claudia Patricia Herrera Bernal. Retrospect, advances and challenges in chagas disease diagnosis: a comprehensive review. The Lancet Regional Health - Americas, 36:100821, Aug 2024. URL: https://doi.org/10.1016/j.lana.2024.100821, doi:10.1016/j.lana.2024.100821. This article has 60 citations.

10. (lopezalbizu2023laboratorydiagnosisof pages 6-7): Constanza Lopez-Albizu, Rocío Rivero, Griselda Ballering, Hector Freilij, María Soledad Santini, and Margarita María Catalina Bisio. Laboratory diagnosis of trypanosoma cruzi infection: a narrative review. Frontiers in Parasitology, May 2023. URL: https://doi.org/10.3389/fpara.2023.1138375, doi:10.3389/fpara.2023.1138375. This article has 23 citations.

11. (ascanio2024invitrodiagnostic pages 1-2): Luis C. Ascanio, Savannah Carroll, Alberto Paniz-Mondolfi, and Juan David Ramírez. In vitro diagnostic methods of chagas disease in the clinical laboratory: a scoping review. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1393992, doi:10.3389/fmicb.2024.1393992. This article has 19 citations and is from a peer-reviewed journal.

12. (ascanio2024invitrodiagnostic pages 8-9): Luis C. Ascanio, Savannah Carroll, Alberto Paniz-Mondolfi, and Juan David Ramírez. In vitro diagnostic methods of chagas disease in the clinical laboratory: a scoping review. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1393992, doi:10.3389/fmicb.2024.1393992. This article has 19 citations and is from a peer-reviewed journal.

13. (schijman2024retrospectadvancesand pages 2-3): Alejandro Gabriel Schijman, Julio Alonso-Padilla, Constança Britto, and Claudia Patricia Herrera Bernal. Retrospect, advances and challenges in chagas disease diagnosis: a comprehensive review. The Lancet Regional Health - Americas, 36:100821, Aug 2024. URL: https://doi.org/10.1016/j.lana.2024.100821, doi:10.1016/j.lana.2024.100821. This article has 60 citations.

14. (pinazo2023clinicaluseof pages 1-2): Maria-Jesus Pinazo, Colin J. Forsyth, Constanza Lopez-Albizu, Margarita María Catalina Bisio, Adriana González-Martínez, Laura Bohorquez, Jimy Pinto, Israel Molina, Andrea Marchiol, Rafael Herazo, Irene Losada Galván, Tayná Marques, Fabiana Barreira, Juan Carlos Villar, Yanina Sguassero, Maria Soledad Santini, Jaime Altcheh, Belkisyolé Alarcón de Noya, and Sergio Sosa-Estani. Clinical use of molecular methods for trypanosoma cruzi infection in endemic and non-endemic countries: benefits, limitations and challenges. Frontiers in Parasitology, Nov 2023. URL: https://doi.org/10.3389/fpara.2023.1241154, doi:10.3389/fpara.2023.1241154. This article has 7 citations.

15. (farani2024treatmentsandthe pages 2-4): Priscila Silva Grijó Farani, Kathryn Marie Jones, and Cristina Poveda. Treatments and the perspectives of developing a vaccine for chagas disease. Vaccines, 12:870, Aug 2024. URL: https://doi.org/10.3390/vaccines12080870, doi:10.3390/vaccines12080870. This article has 15 citations.

16. (moraes2024preventionofcongenital pages 6-8): Francisco Cezar Aquino de Moraes, Maria Eduarda Cavalcanti Souza, Lucca Dal Moro, Isabelle Batista Donadon, Emanuele Rocha da Silva, Dilma do Socorro Moraes de Souza, and Rommel Mario Rodríguez Burbano. Prevention of congenital chagas disease by trypanocide treatment in women of reproductive age: a meta-analysis of observational studies. PLOS Neglected Tropical Diseases, 18:e0012407, Sep 2024. URL: https://doi.org/10.1371/journal.pntd.0012407, doi:10.1371/journal.pntd.0012407. This article has 19 citations and is from a domain leading peer-reviewed journal.

17. (moraes2024preventionofcongenital pages 4-6): Francisco Cezar Aquino de Moraes, Maria Eduarda Cavalcanti Souza, Lucca Dal Moro, Isabelle Batista Donadon, Emanuele Rocha da Silva, Dilma do Socorro Moraes de Souza, and Rommel Mario Rodríguez Burbano. Prevention of congenital chagas disease by trypanocide treatment in women of reproductive age: a meta-analysis of observational studies. PLOS Neglected Tropical Diseases, 18:e0012407, Sep 2024. URL: https://doi.org/10.1371/journal.pntd.0012407, doi:10.1371/journal.pntd.0012407. This article has 19 citations and is from a domain leading peer-reviewed journal.

18. (moraes2024preventionofcongenital pages 1-2): Francisco Cezar Aquino de Moraes, Maria Eduarda Cavalcanti Souza, Lucca Dal Moro, Isabelle Batista Donadon, Emanuele Rocha da Silva, Dilma do Socorro Moraes de Souza, and Rommel Mario Rodríguez Burbano. Prevention of congenital chagas disease by trypanocide treatment in women of reproductive age: a meta-analysis of observational studies. PLOS Neglected Tropical Diseases, 18:e0012407, Sep 2024. URL: https://doi.org/10.1371/journal.pntd.0012407, doi:10.1371/journal.pntd.0012407. This article has 19 citations and is from a domain leading peer-reviewed journal.

19. (kann2024chagasdiseasecomparison pages 1-2): Simone Kann, Gustavo Concha, Hagen Frickmann, Ralf Matthias Hagen, Philipp Warnke, Ernst Molitor, Achim Hoerauf, and Joy Backhaus. Chagas disease: comparison of therapy with nifurtimox and benznidazole in indigenous communities in colombia. Journal of Clinical Medicine, 13:2565, Apr 2024. URL: https://doi.org/10.3390/jcm13092565, doi:10.3390/jcm13092565. This article has 10 citations.

20. (weinberg2023chagaspreventionand pages 1-2): Diego Weinberg, Maria Florencia Casale, Rosa Graciela Cejas, Rafael Hoyos, María Victoria Periago, Elsa Segura, and Marcelo Claudio Abril. Chagas prevention and control in an endemic area from the argentinian gran chaco region: data from 14 years of uninterrupted intervention. PLOS Neglected Tropical Diseases, 17:e0011410, Jun 2023. URL: https://doi.org/10.1371/journal.pntd.0011410, doi:10.1371/journal.pntd.0011410. This article has 8 citations and is from a domain leading peer-reviewed journal.

21. (gurtler2023thepampadel pages 1-2): Ricardo Esteban Gürtler, Gustavo Fabián Enriquez, María Sol Gaspe, Natalia Paula Macchiaverna, María del Pilar Fernández, Lucía Inés Rodríguez-Planes, Yael Mariana Provecho, and Marta Victoria Cardinal. The pampa del indio project: sustainable vector control and long-term declines in the prevalence and abundance of triatoma infestans infected with trypanosoma cruzi in the argentine chaco. Parasites & Vectors, Aug 2023. URL: https://doi.org/10.1186/s13071-023-05861-7, doi:10.1186/s13071-023-05861-7. This article has 7 citations and is from a peer-reviewed journal.

22. (cecere2024slowrecoveryrates pages 1-2): María Carla Cecere, María Sol Gaspe, Natalia Paula Macchiaverna, Gustavo Fabián Enriquez, Alejandra Alvedro, Mariano Alberto Laiño, Julián Antonio Alvarado-Otegui, Marta Victoria Cardinal, and Ricardo Esteban Gürtler. Slow recovery rates and spatial aggregation of triatoma infestans populations in an area with high pyrethroid resistance in the argentine chaco. Parasites & Vectors, Jul 2024. URL: https://doi.org/10.1186/s13071-024-06366-7, doi:10.1186/s13071-024-06366-7. This article has 5 citations and is from a peer-reviewed journal.

23. (vieira2024effectofan pages 1-2): Marcelo Carvalho Vieira, Fernanda de Souza Nogueira Sardinha Mendes, Paula Simplício da Silva, Gilberto Marcelo Sperandio da Silva, Flavia Mazzoli-Rocha, Andrea Silvestre de Sousa, Roberto Magalhães Saraiva, Marcelo Teixeira de Holanda, Daniel Arthur Barata Kasal, Henrique Silveira Costa, Juliana Pereira Borges, Michel Silva Reis, Luiz Fernando Rodrigues Junior, Alejandro Marcel Hasslocher-Moreno, Pedro Emmanuel Alvarenga Americano do Brasil, and Mauro Felippe Felix Mediano. Effect of an exercise-based cardiac rehabilitation program on quality of life of patients with chronic chagas cardiomyopathy: results from the peach randomized clinical trial. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-58776-3, doi:10.1038/s41598-024-58776-3. This article has 5 citations and is from a peer-reviewed journal.

24. (vieira2024effectofan pages 3-4): Marcelo Carvalho Vieira, Fernanda de Souza Nogueira Sardinha Mendes, Paula Simplício da Silva, Gilberto Marcelo Sperandio da Silva, Flavia Mazzoli-Rocha, Andrea Silvestre de Sousa, Roberto Magalhães Saraiva, Marcelo Teixeira de Holanda, Daniel Arthur Barata Kasal, Henrique Silveira Costa, Juliana Pereira Borges, Michel Silva Reis, Luiz Fernando Rodrigues Junior, Alejandro Marcel Hasslocher-Moreno, Pedro Emmanuel Alvarenga Americano do Brasil, and Mauro Felippe Felix Mediano. Effect of an exercise-based cardiac rehabilitation program on quality of life of patients with chronic chagas cardiomyopathy: results from the peach randomized clinical trial. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-58776-3, doi:10.1038/s41598-024-58776-3. This article has 5 citations and is from a peer-reviewed journal.

25. (forsyth2022recommendationsforscreening pages 3-4): Colin J Forsyth, Jennifer Manne-Goehler, Caryn Bern, Jeffrey Whitman, Natasha S Hochberg, Morven Edwards, Rachel Marcus, Norman L Beatty, Yagahira E Castro-Sesquen, Christina Coyle, Paula Stigler Granados, Davidson Hamer, James H Maguire, Robert H Gilman, and Sheba Meymandi. Recommendations for screening and diagnosis of chagas disease in the united states. The Journal of Infectious Diseases, 225:1601-1610, Oct 2022. URL: https://doi.org/10.1093/infdis/jiab513, doi:10.1093/infdis/jiab513. This article has 114 citations.

26. (higuita2024chagasdiseasein pages 1-2): Nelson Iván Agudelo Higuita, Norman L. Beatty, Colin Forsyth, Andrés F. Henao-Martínez, Jennifer Manne-Goehler, Daniel Bourque, Natalie M. Bowman, Malwina Carrion, Christina Coyle, Madolyn Dauphinais, Kelly DeToy, Robert Gilman, Davidson H. Hamer, Jesica Herick, Salvador Hernandez, Claudia Herrera, Rachel Marcus, Sheba Meymandi, Melissa Nolan, Katherine Reifler, Adrienne Showler, Paula Stigler Granados, Anshule Takyar, Kawsar Talaat, Shilah Waters, and Alyse Wheelock. Chagas disease in the united states: a call for increased investment and collaborative research. The Lancet Regional Health - Americas, 34:100768, Jun 2024. URL: https://doi.org/10.1016/j.lana.2024.100768, doi:10.1016/j.lana.2024.100768. This article has 32 citations.

27. (albaalvarado2024thefunctionsof pages 8-10): Mariana Citlalli de Alba-Alvarado, Margarita Cabrera-Bravo, Edgar Zenteno, Paz María Salazar-Schetino, and Martha Irene Bucio-Torres. The functions of cytokines in the cardiac immunopathogenesis of chagas disease. Pathogens, 13:870, Oct 2024. URL: https://doi.org/10.3390/pathogens13100870, doi:10.3390/pathogens13100870. This article has 9 citations.

28. (nunes2023inflammationandmitochondria pages 1-2): João Paulo Silva Nunes, Vinicius Moraes de Paiva Roda, Pauline Andrieux, Jorge Kalil, Christophe Chevillard, and Edecio Cunha-Neto. Inflammation and mitochondria in the pathogenesis of chronic chagas disease cardiomyopathy. Experimental Biology and Medicine, 248:2062-2071, Nov 2023. URL: https://doi.org/10.1177/15353702231220658, doi:10.1177/15353702231220658. This article has 15 citations and is from a peer-reviewed journal.

29. (albaalvarado2024thefunctionsof pages 8-8): Mariana Citlalli de Alba-Alvarado, Margarita Cabrera-Bravo, Edgar Zenteno, Paz María Salazar-Schetino, and Martha Irene Bucio-Torres. The functions of cytokines in the cardiac immunopathogenesis of chagas disease. Pathogens, 13:870, Oct 2024. URL: https://doi.org/10.3390/pathogens13100870, doi:10.3390/pathogens13100870. This article has 9 citations.

30. (nunes2023inflammationandmitochondria pages 2-3): João Paulo Silva Nunes, Vinicius Moraes de Paiva Roda, Pauline Andrieux, Jorge Kalil, Christophe Chevillard, and Edecio Cunha-Neto. Inflammation and mitochondria in the pathogenesis of chronic chagas disease cardiomyopathy. Experimental Biology and Medicine, 248:2062-2071, Nov 2023. URL: https://doi.org/10.1177/15353702231220658, doi:10.1177/15353702231220658. This article has 15 citations and is from a peer-reviewed journal.

31. (albaalvarado2024thefunctionsof pages 1-2): Mariana Citlalli de Alba-Alvarado, Margarita Cabrera-Bravo, Edgar Zenteno, Paz María Salazar-Schetino, and Martha Irene Bucio-Torres. The functions of cytokines in the cardiac immunopathogenesis of chagas disease. Pathogens, 13:870, Oct 2024. URL: https://doi.org/10.3390/pathogens13100870, doi:10.3390/pathogens13100870. This article has 9 citations.

32. (albaalvarado2024thefunctionsof pages 4-5): Mariana Citlalli de Alba-Alvarado, Margarita Cabrera-Bravo, Edgar Zenteno, Paz María Salazar-Schetino, and Martha Irene Bucio-Torres. The functions of cytokines in the cardiac immunopathogenesis of chagas disease. Pathogens, 13:870, Oct 2024. URL: https://doi.org/10.3390/pathogens13100870, doi:10.3390/pathogens13100870. This article has 9 citations.

33. (albaalvarado2024thefunctionsof pages 7-8): Mariana Citlalli de Alba-Alvarado, Margarita Cabrera-Bravo, Edgar Zenteno, Paz María Salazar-Schetino, and Martha Irene Bucio-Torres. The functions of cytokines in the cardiac immunopathogenesis of chagas disease. Pathogens, 13:870, Oct 2024. URL: https://doi.org/10.3390/pathogens13100870, doi:10.3390/pathogens13100870. This article has 9 citations.

34. (forsyth2022recommendationsforscreening pages 1-2): Colin J Forsyth, Jennifer Manne-Goehler, Caryn Bern, Jeffrey Whitman, Natasha S Hochberg, Morven Edwards, Rachel Marcus, Norman L Beatty, Yagahira E Castro-Sesquen, Christina Coyle, Paula Stigler Granados, Davidson Hamer, James H Maguire, Robert H Gilman, and Sheba Meymandi. Recommendations for screening and diagnosis of chagas disease in the united states. The Journal of Infectious Diseases, 225:1601-1610, Oct 2022. URL: https://doi.org/10.1093/infdis/jiab513, doi:10.1093/infdis/jiab513. This article has 114 citations.

35. (schijman2024retrospectadvancesand media 49150249): Alejandro Gabriel Schijman, Julio Alonso-Padilla, Constança Britto, and Claudia Patricia Herrera Bernal. Retrospect, advances and challenges in chagas disease diagnosis: a comprehensive review. The Lancet Regional Health - Americas, 36:100821, Aug 2024. URL: https://doi.org/10.1016/j.lana.2024.100821, doi:10.1016/j.lana.2024.100821. This article has 60 citations.

36. (forsyth2022recommendationsforscreening pages 7-8): Colin J Forsyth, Jennifer Manne-Goehler, Caryn Bern, Jeffrey Whitman, Natasha S Hochberg, Morven Edwards, Rachel Marcus, Norman L Beatty, Yagahira E Castro-Sesquen, Christina Coyle, Paula Stigler Granados, Davidson Hamer, James H Maguire, Robert H Gilman, and Sheba Meymandi. Recommendations for screening and diagnosis of chagas disease in the united states. The Journal of Infectious Diseases, 225:1601-1610, Oct 2022. URL: https://doi.org/10.1093/infdis/jiab513, doi:10.1093/infdis/jiab513. This article has 114 citations.

37. (forsyth2022recommendationsforscreening pages 2-3): Colin J Forsyth, Jennifer Manne-Goehler, Caryn Bern, Jeffrey Whitman, Natasha S Hochberg, Morven Edwards, Rachel Marcus, Norman L Beatty, Yagahira E Castro-Sesquen, Christina Coyle, Paula Stigler Granados, Davidson Hamer, James H Maguire, Robert H Gilman, and Sheba Meymandi. Recommendations for screening and diagnosis of chagas disease in the united states. The Journal of Infectious Diseases, 225:1601-1610, Oct 2022. URL: https://doi.org/10.1093/infdis/jiab513, doi:10.1093/infdis/jiab513. This article has 114 citations.

38. (NCT03378661 chunk 1):  BENDITA BEnznidazole New Doses Improved Treatment and Associations. Drugs for Neglected Diseases. 2016. ClinicalTrials.gov Identifier: NCT03378661

39. (NCT03378661 chunk 2):  BENDITA BEnznidazole New Doses Improved Treatment and Associations. Drugs for Neglected Diseases. 2016. ClinicalTrials.gov Identifier: NCT03378661

40. (NCT04897516 chunk 1):  Shorter Benznidazole Regimens Compared to the Standard Regimen for Chagas Disease. Laboratorio Elea Phoenix S.A.. 2021. ClinicalTrials.gov Identifier: NCT04897516

41. (NCT04897516 chunk 2):  Shorter Benznidazole Regimens Compared to the Standard Regimen for Chagas Disease. Laboratorio Elea Phoenix S.A.. 2021. ClinicalTrials.gov Identifier: NCT04897516

42. (hochberg2023chagasdisease pages 4-6): Natasha S. Hochberg and Susan P. Montgomery. Chagas disease. Annals of Internal Medicine, 176:ITC17-ITC32, Feb 2023. URL: https://doi.org/10.7326/aitc202302210, doi:10.7326/aitc202302210. This article has 107 citations and is from a highest quality peer-reviewed journal.

43. (duraesoliveira2024chagasdiseasea pages 2-4): João Durães-Oliveira, Joana Palma-Marques, Cláudia Moreno, Armanda Rodrigues, Marta Monteiro, Graça Alexandre-Pires, Isabel Pereira da Fonseca, and Gabriela Santos-Gomes. Chagas disease: a silent threat for dogs and humans. International Journal of Molecular Sciences, 25:3840, Mar 2024. URL: https://doi.org/10.3390/ijms25073840, doi:10.3390/ijms25073840. This article has 40 citations.

44. (duraesoliveira2024chagasdiseasea pages 1-2): João Durães-Oliveira, Joana Palma-Marques, Cláudia Moreno, Armanda Rodrigues, Marta Monteiro, Graça Alexandre-Pires, Isabel Pereira da Fonseca, and Gabriela Santos-Gomes. Chagas disease: a silent threat for dogs and humans. International Journal of Molecular Sciences, 25:3840, Mar 2024. URL: https://doi.org/10.3390/ijms25073840, doi:10.3390/ijms25073840. This article has 40 citations.

45. (murphy2024developmentofrapid pages 64-65): N Murphy. Development of rapid diagnostic tests for trypanosoma cruzi lineage-specific serology, comparative epidemiology and for monitoring efficacy of chemotherapy. Dissertation, Jan 2024. URL: https://doi.org/10.17037/pubs.04673813, doi:10.17037/pubs.04673813. This article has 0 citations.

46. (pereira2024insecticidalactivityof pages 12-13): Luanderson Cardoso Pereira, Nathalie de Sena Pereira, Andressa Noronha Barbosa da Silva, Clarice de Freitas Bezerra, Kivia Millana de Sousa, João Ciro Fagundes Neto, George Harisson Felinto Sampaio, Carlos Ramon do Nascimento Brito, Rita de Cássia Moreira Souza, Lúcia Maria da Cunha Galvão, Antônia Claudia Jácome da Câmara, Manuela Sales Lima Nascimento, and Paulo Marcos Matta Guedes. Insecticidal activity of fluralaner (exzolt®) administered to gallus gallus domesticus against triatomines (hemiptera, reduviidae, triatominae). Parasites & Vectors, May 2024. URL: https://doi.org/10.1186/s13071-024-06276-8, doi:10.1186/s13071-024-06276-8. This article has 5 citations and is from a peer-reviewed journal.

47. (schijman2024retrospectadvancesand media 2264cf25): Alejandro Gabriel Schijman, Julio Alonso-Padilla, Constança Britto, and Claudia Patricia Herrera Bernal. Retrospect, advances and challenges in chagas disease diagnosis: a comprehensive review. The Lancet Regional Health - Americas, 36:100821, Aug 2024. URL: https://doi.org/10.1016/j.lana.2024.100821, doi:10.1016/j.lana.2024.100821. This article has 60 citations.

48. (schijman2024retrospectadvancesand media b8b9a0ae): Alejandro Gabriel Schijman, Julio Alonso-Padilla, Constança Britto, and Claudia Patricia Herrera Bernal. Retrospect, advances and challenges in chagas disease diagnosis: a comprehensive review. The Lancet Regional Health - Americas, 36:100821, Aug 2024. URL: https://doi.org/10.1016/j.lana.2024.100821, doi:10.1016/j.lana.2024.100821. This article has 60 citations.

49. (hochberg2023chagasdisease pages 1-3): Natasha S. Hochberg and Susan P. Montgomery. Chagas disease. Annals of Internal Medicine, 176:ITC17-ITC32, Feb 2023. URL: https://doi.org/10.7326/aitc202302210, doi:10.7326/aitc202302210. This article has 107 citations and is from a highest quality peer-reviewed journal.
