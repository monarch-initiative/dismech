---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T14:54:37.119534'
end_time: '2026-04-04T15:01:28.949347'
duration_seconds: 411.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Leprosy
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 51
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leprosy
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Leprosy** covering all of the
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
- **Disease Name:** Leprosy
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Leprosy** covering all of the
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


## Comprehensive Research Report: Leprosy (Hansen’s disease)

### Executive summary
Leprosy is a chronic infectious disease caused mainly by *Mycobacterium leprae* (and in some settings *M. lepromatosis*), characterized by skin lesions and peripheral neuropathy that can progress to permanent disability. Despite major reductions after WHO-recommended multidrug therapy (MDT), global transmission continues, with ~174,087 new cases reported in 2022 (21.8 per million) and a persistent burden of grade-2 disability (G2D) at diagnosis, reflecting delayed detection in many settings. Recent (2023–2024) work emphasizes (i) host-directed mechanisms of nerve injury centered on Schwann cell infection and lipid metabolic reprogramming, (ii) improved diagnostic/monitoring strategies combining histopathology, serology and molecular tests, and (iii) intensified prevention via post-exposure prophylaxis (PEP), including evaluation of strengthened antimicrobial regimens beyond single-dose rifampicin. (bakoubayi2024anyresurgenceof pages 1-2, li2024leprosytreatmentprevention pages 5-6, dornelas2024roleofhistopathological pages 1-2, jong2024safetyofsingledose pages 1-2)

---

## 1. Disease information

### 1.1 Definition and overview
Leprosy (Hansen’s disease) is an infectious disease that primarily affects skin and peripheral nerves, potentially causing long-term disability and stigma. A recent narrative review states: “Leprosy is an infectious disease that remains a public health concern… [and] primarily affects the skin and peripheral nerves, potentially leading to long-term disability and stigma.” (Medicine; Aug 2024; https://doi.org/10.1097/md.0000000000039006) (huang2024anupdateof pages 1-2)

Key microbiologic features summarized in recent reviews include slow growth, prolonged incubation, and a temperature preference consistent with predilection for cooler body sites and peripheral nerves. (huang2024anupdateof pages 1-2)

### 1.2 Key identifiers and ontology mappings (knowledge-base fields)
* **MONDO ID:** Not found in the retrieved evidence corpus; needs lookup from MONDO Disease Ontology directly (e.g., via OLS/Monarch). (No MONDO-leprosy term text retrieved)
* **ICD-10:** Not retrieved in evidence; commonly A30.* (needs direct ICD reference).
* **ICD-11:** Not retrieved in evidence; needs direct ICD-11 reference.
* **MeSH:** Not retrieved in evidence; needs direct MeSH reference.
* **Orphanet / OMIM:** Not retrieved in evidence; leprosy is infectious rather than a monogenic disorder entry in OMIM.

### 1.3 Synonyms
* Leprosy
* Hansen’s disease (explicitly used in multiple recent reviews) (huang2024anupdateof pages 1-2, kimta2024leprosycomprehensiveinsights pages 1-2)

### 1.4 Data provenance type
Most information used here is aggregated from disease-level resources and peer-reviewed literature (narrative/systematic reviews, epidemiological studies, clinical trials), rather than individual EHR-derived case data. (huang2024anupdateof pages 1-2, silva2024anupdateon pages 1-2, bakoubayi2024anyresurgenceof pages 1-2)

---

## 2. Etiology

### 2.1 Causal factors
* **Infectious etiology:** Caused by *Mycobacterium leprae*; some sources also include *M. lepromatosis* as a cause. (huang2024anupdateof pages 1-2, silva2024anupdateon pages 1-2, barboza2024neutrophilicleukocytosisand pages 1-2)

### 2.2 Transmission and natural history (key concepts)
Recent synthesis notes long incubation (often years) and supports person-to-person spread, especially from untreated individuals with high bacillary load. (huang2024anupdateof pages 1-2, kimta2024leprosycomprehensiveinsights pages 1-2)

### 2.3 Risk factors
**Host genetic susceptibility (polygenic):** A 2024 review emphasizes that “the infection and pathogenesis largely depend on the host’s genetic background and immunity,” and notes “more than 30 susceptibility genes” have been implicated. (Frontiers in Immunology; Feb 2024; https://doi.org/10.3389/fimmu.2024.1298749) (li2024leprosytreatmentprevention pages 1-2)

**Contact-related risk:** Household contacts (and other close contacts) are repeatedly identified as high risk and are the target population for PEP strategies. (li2024leprosytreatmentprevention pages 1-2, hinders2024thepep++study pages 1-2)

### 2.4 Protective factors
Direct protective-factor quantification was not retrieved in the current evidence set. However, immunoprophylaxis approaches (BCG and candidate vaccines such as LepVax/MiP) are discussed as prevention tools; effectiveness varies and is still under development. (li2024leprosytreatmentprevention pages 1-2, slater2023acurrentperspective pages 45-47)

### 2.5 Gene–environment interactions
A specific, quantitatively supported gene–environment interaction model was not retrieved in the current evidence set. The most consistent “interaction” framing supported here is that genetic background shapes immune polarization and susceptibility, while exposure intensity/duration (e.g., household contact) determines infection risk. (li2024leprosytreatmentprevention pages 1-2, hinders2024thepep++study pages 1-2)

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Core clinical manifestations (with suggested HPO terms)
The WHO clinical diagnostic triad (also useful as phenotype anchors) includes:
1) **Hypopigmented or reddish skin lesions with sensory loss** (HPO suggestions: **HP:0001010** Hypopigmentation; **HP:0000989** Skin rash; **HP:0000762** Hypoesthesia). (huang2024anupdateof pages 6-6)
2) **Thickened/enlarged peripheral nerves with sensory/motor loss** (HPO suggestions: **HP:0009830** Peripheral neuropathy; **HP:0001288** Abnormality of peripheral nerve conduction; **HP:0003390** Nerve hypertrophy). (huang2024anupdateof pages 6-6)
3) **Acid-fast bacilli (AFB) demonstrable in slit-skin smear or biopsy** (maps more to lab findings than HPO). (huang2024anupdateof pages 6-6)

### 3.2 Reactional states (major morbidity drivers)
Leprosy reactions are acute inflammatory episodes that accelerate nerve injury and disability.
* **Type 2 reaction / Erythema nodosum leprosum (ENL):** In a 2024 Brazilian BL/LL cohort (n=146), reactions were common (85%) and ENL comprised 65% of reactional episodes; 55% of ENL patients had >2 episodes (mean 2.6). (Frontiers in Immunology; Jul 2024; https://doi.org/10.3389/fimmu.2024.1368460) (barboza2024neutrophilicleukocytosisand pages 1-2)
  * HPO suggestions: **HP:0000994** Erythema nodosum; **HP:0011123** Fever (often associated); **HP:0000988** Skin ulcer (severe forms).

### 3.3 Laboratory/hematologic correlates (ENL example)
ENL is associated with neutrophilia in the 2024 cohort:
* Median neutrophils higher in those developing ENL (4,567 vs 3,731 cells/mm³)
* Severity gradient: 6,066 (mild) vs 10,243 (moderate/severe) cells/mm³
* Longitudinal within-person: BL/LL 4,896 vs ENL 8,408 cells/mm³ (p<0.0001) (barboza2024neutrophilicleukocytosisand pages 1-2)

### 3.4 Quality-of-life impact
Quantitative QoL instruments (e.g., DLQI, SF-36, EQ-5D) were not retrieved in the current evidence set, but recent reviews emphasize persistent neuropathy and disability even after MDT, which is a major driver of QoL impairment. (huang2024anupdateof pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
Leprosy is not a monogenic disorder; instead it shows polygenic susceptibility with immune-related loci. The retrieved evidence supports the concept of multiple susceptibility genes (>30) rather than specific pathogenic variants with ACMG classifications. (li2024leprosytreatmentprevention pages 1-2)

### 4.2 Pathogen drug-resistance determinants (molecular genetics of *M. leprae*)
A 2024 antimicrobial resistance review (retrieved but not deeply evidenced here) is complemented by a 2024 prevention/treatment review noting concern about “the emergence of rifampicin-resistant strains.” (li2024leprosytreatmentprevention pages 1-2)

### 4.3 Epigenetics / modifier genes
Not retrieved in this evidence set.

---

## 5. Environmental information

### 5.1 Environmental and lifestyle factors
Not retrieved in this evidence set with quantitative support.

### 5.2 Infectious agents
Causal pathogens: *M. leprae* and *M. lepromatosis*. (silva2024anupdateon pages 1-2, barboza2024neutrophilicleukocytosisand pages 1-2)

---

## 6. Mechanism / pathophysiology (current understanding)

### 6.1 Core causal chain (trigger → cellular events → nerve damage → clinical disability)
1) **Exposure and infection** → bacilli establish infection in cooler tissues.
2) **Cell tropism**: Primary infected cells include **Schwann cells** (peripheral glia) and dermal macrophages/histiocytes. (silva2024anupdateon pages 1-2, santos2024adenosinea2areceptor pages 1-2)
3) **Schwann cell entry/internalization**: A 2024 review describes binding of *M. leprae* to laminin-2/α-dystroglycan on the Schwann cell basal lamina with downstream **PI3K signaling** mediating internalization. (li2024leprosytreatmentprevention pages 5-6)
4) **Immune-metabolic reprogramming**: Infection promotes “foamy” lipid-laden cells and metabolic states favorable for persistence, including lipid droplet accumulation and cholesterol dependence. (santos2024adenosinea2areceptor pages 1-2, li2024leprosytreatmentprevention pages 5-6)
5) **Immune polarization and antigen presentation defects**: PGL-1-related suppression of MHC release and PRR-driven macrophage polarization shape Th/CD8 responses and clinical spectrum; adaptive immunity can exacerbate nerve injury. (silva2024anupdateon pages 1-2)
6) **Clinical outcomes**: Peripheral neuropathy, sensory/motor loss, deformities; reactional episodes (e.g., ENL) drive acute inflammation and irreversible nerve damage if untreated. (barboza2024neutrophilicleukocytosisand pages 1-2, silva2024anupdateon pages 1-2)

### 6.2 Lipid metabolism and lipid droplets as a survival niche (recent 2024 primary evidence)
A 2024 primary study emphasizes that *M. leprae* infection “subvert[s]” host lipid metabolism to generate **cholesterol-rich lipid droplets** important for bacterial survival in Schwann cells, and reports a host-directed candidate pathway: adenosine A2A receptor signaling. Infected Schwann cells showed altered ectonucleotidase signaling (CD73/ADA up; A2AR down), while pharmacologic A2AR activation reduced lipid droplets, reduced IL-6/IL-8, and reduced intracellular *M. leprae* viability. (Frontiers in Pharmacology; Jun 2024; https://doi.org/10.3389/fphar.2024.1399363) (santos2024adenosinea2areceptor pages 1-2)

**Ontology suggestions**
* GO biological processes: **cholesterol metabolic process**, **lipid droplet organization**, **innate immune response**, **antigen processing and presentation**, **inflammatory response** (santos2024adenosinea2areceptor pages 1-2, silva2024anupdateon pages 1-2)
* Cell Ontology (CL) targets: **Schwann cell** (CL:0000218), **macrophage** (CL:0000235), **dendritic cell** (CL:0000451), **CD8-positive T cell** (CL:0000625)

---

## 7. Anatomical structures affected

### 7.1 Primary organs/systems
* **Skin** and **peripheral nervous system** are primary sites (per WHO clinical criteria and mechanistic reviews). (huang2024anupdateof pages 6-6, silva2024anupdateon pages 1-2)

**UBERON suggestions**
* UBERON:0002097 (skin)
* UBERON:0000010 (peripheral nervous system)

### 7.2 Tissue/cell types
* Peripheral nerve Schwann cells (glial cells) and dermal macrophages/histiocytes. (silva2024anupdateon pages 1-2, santos2024adenosinea2areceptor pages 1-2)

---

## 8. Temporal development

* **Incubation:** Long (often years). (huang2024anupdateof pages 1-2)
* **Course:** Chronic with episodic reactional flares; disability is strongly linked to delays in detection and to reactions. (quilter2024isthewho pages 6-9, barboza2024neutrophilicleukocytosisand pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent statistics)
A WHO-derived global estimate reported in an epidemiologic analysis indicates **174,087 new cases in 2022**, with a **detection rate of 21.8 per million**, and an increase relative to 2021 (noting COVID-era detection disruption). (bakoubayi2024anyresurgenceof pages 1-2)

Regional distribution (WHO-derived): Southeast Asia 66.5% of new cases; Africa 15.1%. (bakoubayi2024anyresurgenceof pages 1-2)

### 9.2 Disability burden (G2D) statistics and interpretation
A 2024 analysis of WHO Weekly Epidemiological Record (WER) data reports that global new case counts declined from **407,791 (2004) to 174,087 (2022)** while disability indicators show more complex patterns; notably, the **G2D rate** decreased from **2.9 per million (2004) to 1.2 per million (2022)** but the **proportion** of new cases with G2D increased over time, consistent with later detection among those still being diagnosed. (quilter2024isthewho pages 3-6)

WHO has set G2D-rate milestones toward a 2030 target, reported as **0.92 per million (2023)**, **0.68 (2025)**, and **0.12 (2030)**. (quilter2024isthewho pages 6-9)

---

## 10. Diagnostics

### 10.1 Clinical criteria (WHO)
WHO clinical diagnosis is anchored in three cardinal signs: anesthetic skin lesions, peripheral nerve thickening with neurologic deficits, and AFB detection in slit-skin smear/biopsy. (huang2024anupdateof pages 6-6)

### 10.2 Slit-skin smear (SSS) microscopy
SSS is highly specific (~100%) but insensitive (commonly 18–30%), so a negative SSS does not exclude disease. (huang2024anupdateof pages 6-6, huang2024anupdateof pages 6-7)

### 10.3 Histopathology (biopsy)
Biopsy with Fite-Faraco/modified Ziehl–Neelsen staining and histologic bacillary index supports confirmation and classification, but inter-observer variability exists in routine practice, as illustrated in the long-running Karonga (Malawi) program with thousands of biopsies and harmonization efforts. (team2024theepidemiologyof pages 11-14)

### 10.4 Molecular tests (PCR/qPCR)
PCR/qPCR can substantially increase sensitivity, especially in early/low-bacillary-load disease and for contacts, but implementation is constrained by cost and infrastructure. PCR sensitivity is much higher in BI-positive/lepromatous disease (87–100%) than in BI-negative/tuberculoid forms (30–83%) in reported studies summarized by a 2024 narrative review. (huang2024anupdateof pages 6-6)

A 2023 perspective notes that “PCR as a diagnostic tool is one of the most reliable and robust techniques,” and highlights ongoing needs for assay standardization and cost-effective deployment. (slater2023acurrentperspective pages 45-47)

### 10.5 Serology and biomarkers
Anti–PGL-I IgM serology is used as a relatively simple surrogate of bacterial load and is helpful for MB vs PB classification, but has limited utility for PB detection. (huang2024anupdateof pages 6-6)

**Treatment failure monitoring (2024 primary study):** A case-control study (BMC Infectious Diseases; Oct 2024; https://doi.org/10.1186/s12879-024-09937-2) found that foamy granulomas (OR 7.36), histologic bacillary index thresholds (AUC ~0.75), anti-PGL-I ELISA index (AUC ~0.74), and real-time PCR positivity (3.43-fold increased odds) were associated with treatment failure; combined models predicted treatment failure with high estimated likelihood (up to ~95%). (dornelas2024roleofhistopathological pages 1-2)

**Omics-derived candidate biomarkers (2024):** A transcriptomic meta-analysis proposed immune-pathway hub genes (e.g., ITK, CD48, IL2RG, CCR5, JAK3, STAT1) as potential biomarkers requiring prospective validation. (zhou2024identificationofpotential pages 1-2)

### 10.6 Health-economic/implementation evidence
A Brazilian SUS-perspective cost-effectiveness model evaluated a sequential diagnostic algorithm for household contacts (rapid IgM test → SSS → real-time PCR) versus SSS alone, reporting an incremental cost-effectiveness ratio of **USD 616.46 per avoided undiagnosed case**. (Cadernos de Saúde Pública; Jan 2024; https://doi.org/10.1590/0102-311xen038723) (costa2024acosteffectivenessanalysis pages 1-2)

---

## 11. Outcome / prognosis

Robust survival/mortality estimates were not retrieved in the current evidence set. The primary burden is morbidity from neuropathy and disability, with disability metrics (G2D rate/proportion) serving as key operational proxies for diagnostic timeliness and long-term outcomes. (quilter2024isthewho pages 3-6, quilter2024isthewho pages 6-9)

---

## 12. Treatment

### 12.1 Standard antimicrobial therapy (MDT)
WHO MDT (introduced 1981; free access from 1995) is foundational, but recent reviews stress that “multidrug therapy seems unable to eradicate leprosy,” and that antimicrobial resistance (e.g., rifampicin resistance) threatens control. (li2024leprosytreatmentprevention pages 1-2, huang2024anupdateof pages 1-2)

**MAXO suggestions**
* Antimicrobial drug therapy (MAXO:0000767)

### 12.2 Management of reactions and neuritis
Reactional episodes (including ENL) are major drivers of nerve injury. The retrieved evidence set includes recent cohort-level quantification of ENL recurrence and inflammatory correlates (neutrophilia) supporting intensive monitoring and timely anti-inflammatory treatment strategies. (barboza2024neutrophilicleukocytosisand pages 1-2)

**MAXO suggestions**
* Anti-inflammatory therapy (MAXO:0000917)
* Immunosuppressive therapy (MAXO:0000919)

### 12.3 Emerging and experimental approaches
**Host-directed approaches:** Recent mechanistic work implicates Schwann-cell lipid droplet metabolism and adenosinergic signaling (A2AR) as potential host-directed targets to reduce intracellular survival and inflammatory cytokines. (santos2024adenosinea2areceptor pages 1-2)

---

## 13. Prevention

### 13.1 Post-exposure prophylaxis (PEP) with rifampicin (SDR-PEP): current standard and real-world implementation
WHO recommends single-dose rifampicin PEP (SDR-PEP). A 2024 Phase 2 safety trial reiterates this standard and states SDR-PEP reduces leprosy risk in contacts “by around 50%” and cites the COLEP trial’s **57% incidence reduction** over 2 years. (jong2024safetyofsingledose pages 1-2, younoussa2023protocolrationaleand pages 1-2)

**Routine-program effectiveness (Nepal, 2024):** Under program conditions, SDR-PEP was associated with a **72% reduction** in risk among contacts (HR 0.28, 95% CI 0.18–0.44). (PLOS NTD; Dec 2024; https://doi.org/10.1371/journal.pntd.0012446) (banstola2024effectivenessofongoing pages 1-2)

**Program audits (Kiribati, 2024):** An SDR-PEP program audit reported coverage of **84.7%** (retrospective cohort) and **88.1%** (prospective cohort), with median time to administration of **220 days** vs **120 days** respectively, illustrating key implementation bottlenecks. (jong2024safetyofsingledose pages 1-2)

### 13.2 Enhanced PEP regimens (2023–2024 research frontier)
Because SDR-PEP effectiveness is variable across contexts, multiple strengthened regimens are in late-stage evaluation.

**BE-PEOPLE (bedaquiline + rifampicin) trial program (BMC Infectious Diseases; May 2023):** Designed to test enhanced PEP for contacts, explicitly building from COLEP’s 57% effect and addressing persistent transmission in Comoros. (https://doi.org/10.1186/s12879-023-08290-0; NCT05597280) (younoussa2023protocolrationaleand pages 1-2)

**Phase 2 safety evidence for bedaquiline-enhanced PEP (PLOS Medicine; Oct 2024):** A randomized non-inferiority safety trial (n=313; 99% completed) comparing **bedaquiline 800 mg + rifampicin 600 mg** vs rifampicin 600 mg alone found a small QTc difference (1.8 ms; 95% CI −1.8 to 5.3) and no QTc >450 ms or >50 ms increase, supporting feasibility of Phase 3 efficacy testing. (https://doi.org/10.1371/journal.pmed.1004453; NCT05406479) (jong2024safetyofsingledose pages 1-2, jong2024safetyofsingledose pages 7-9)

**PEP++ trial (BMC Infectious Diseases; Feb 2024):** Tests three monthly doses of rifampicin plus clarithromycin versus SDR-PEP to increase protection in the highest-risk contact groups. (https://doi.org/10.1186/s12879-024-09125-2) (hinders2024thepep++study pages 1-2)

### 13.3 Vaccines (status)
No leprosy-specific licensed vaccine exists; BCG provides partial protection with wide variability across studies and settings, and candidates such as LepVax/MiP are in development. (slater2023acurrentperspective pages 45-47, li2024leprosytreatmentprevention pages 1-2)

---

## 14. Other species / natural disease
Evidence on zoonotic reservoirs (e.g., armadillos/red squirrels) was not retrieved in the current evidence set.

---

## 15. Model organisms
A practical limitation emphasized in a 2023 perspective is that “The inability to culture *M. leprae* in vitro has also hampered investigations… Mouse foot pads have been the only feasible method to measure drug susceptibility,” making the mouse footpad model central for drug testing and resistance phenotyping. (slater2023acurrentperspective pages 45-47)

---

## Recent developments (2023–2024 highlights aligned to user priorities)

1) **Disability indicator debate and program metrics (2024):** Detailed analysis of WHO WER shows declining G2D rates but increasing G2D proportion, arguing for multi-metric monitoring to avoid masking worsening delayed diagnosis in high-burden settings. (quilter2024isthewho pages 3-6, quilter2024isthewho pages 6-9)
2) **PEP intensification beyond SDR-PEP:** 2024 observational program data show strong effectiveness under routine conditions (Nepal HR 0.28), while global trials are evaluating multidose/combination regimens (PEP++; BE-PEOPLE). (banstola2024effectivenessofongoing pages 1-2, hinders2024thepep++study pages 1-2, younoussa2023protocolrationaleand pages 1-2)
3) **Safety de-risking for new prophylaxis regimens:** Phase 2 randomized evidence supports cardiac/liver safety of single-dose bedaquiline + rifampicin PEP as a precursor to large Phase 3 efficacy trials. (jong2024safetyofsingledose pages 1-2)
4) **Mechanistic host-directed targets in neuropathogenesis (2024):** New Schwann-cell focused work highlights adenosinergic signaling (A2AR) and lipid droplet metabolism as intervention axes to reduce *M. leprae* viability and inflammatory cytokines. (santos2024adenosinea2areceptor pages 1-2)
5) **Diagnostics moving toward integrated algorithms:** Evidence supports combined histology/serology/PCR approaches to detect treatment failure and to operationalize earlier diagnosis in contacts, with explicit cost-effectiveness modelling in Brazil. (dornelas2024roleofhistopathological pages 1-2, costa2024acosteffectivenessanalysis pages 1-2)

---

## Evidence table (key quantitative findings)
| Descriptor | Numeric value(s) | Population / context | Year | Citation |
|---|---:|---|---|---|
| Global new cases and detection rate | 174,087 new cases; 21.8 per million | WHO global leprosy reports | 2022 | (bakoubayi2024anyresurgenceof pages 1-2) |
| Global G2D rate trend | 2.9 per million (2004) → 1.2 per million (2022) | WHO WER global grade-2 disability rate | 2004 vs 2022 | (quilter2024isthewho pages 3-6) |
| WHO G2D milestone targets | 0.92 per million (2023); 0.68 (2025); 0.12 (2030) | WHO target trajectory for new G2D cases | 2023–2030 | (quilter2024isthewho pages 6-9) |
| Regional distribution of new cases | SEAR 66.5%; Africa 15.1% | Share of global new cases reported by WHO | 2022 | (bakoubayi2024anyresurgenceof pages 1-2) |
| WHO-reported leprosy reactions | Type 1: 15,031; Type 2: 6,296; only 42 countries reported | WHO global update; reaction reporting incomplete | 2022 data reported in 2023 update | (saunderson2023whogloballeprosy pages 1-2) |
| ENL cohort: sex, ENL frequency, recurrence | Male 75%; reactional episode 85%; ENL among reactions 65%; >2 ENL episodes in 55%; mean 2.6 episodes | 146 BL/LL patients in retrospective cohort, Brazil | 2024 study | (barboza2024neutrophilicleukocytosisand pages 1-2) |
| SDR-PEP effectiveness: COLEP | 57% reduction in incidence among contacts after 2 years | Household/close contacts; foundational evidence for WHO SDR-PEP recommendation | Prior trial, cited in 2023–2024 papers | (younoussa2023protocolrationaleand pages 1-2, hinders2024thepep++study pages 1-2) |
| SDR-PEP effectiveness: Nepal routine implementation | HR 0.28 (95% CI 0.18–0.44); ~72% risk reduction | Contacts in two Nepal districts under routine programme conditions | 2024 | (banstola2024effectivenessofongoing pages 1-2) |
| Enhanced PEP: double-dose rifampicin | 45% reduction in risk | Comoros and Madagascar trial background cited in BE-PEP paper | Prior trial, summarized 2024 | (jong2024safetyofsingledose pages 2-4) |
| BE-PEP safety (bedaquiline + rifampicin) | n=313 enrolled; 310/313 (99%) completed; QTc between-arm difference 1.8 ms (95% CI −1.8 to 5.3); no QTc >450 ms or increase >50 ms | Phase 2 randomized non-inferiority safety trial, Comoros | 2024 | (jong2024safetyofsingledose pages 1-2, jong2024safetyofsingledose pages 7-9) |
| Kiribati SDR coverage and timeliness | SDR coverage 84.7% retrospective, 88.1% prospective; median time to SDR 220 days (IQR 162–468) retrospective, 120 days (IQR 36–283) prospective | Household contacts in national SDR-PEP programme audit | 2018–2022 programme, 2024 report | (jong2024safetyofsingledose pages 1-2) |


*Table: This table compiles key recent quantitative evidence on leprosy epidemiology, disability burden, reactions, prophylaxis effectiveness, and implementation metrics. It is useful as a compact evidence summary for a disease knowledge base or research report.*

---

## Notes on evidence gaps vs requested template
* **PMIDs:** The retrieved evidence snippets did not include PMID metadata; therefore PMID-citing is incomplete in this report despite the preference stated in the template.
* **Ontology identifiers (MONDO/MeSH/ICD-11):** Not retrievable from the current literature-only evidence set; these should be filled by direct ontology lookups.
* **Zoonotic reservoirs, detailed QoL statistics, and specific GWAS loci/variants:** Not adequately captured in the retrieved evidence subset; further targeted retrieval would be required.


References

1. (bakoubayi2024anyresurgenceof pages 1-2): Akila Wimima Bakoubayi, Falapalaki Haliba, Wendpouiré Ida C. Zida-Compaore, P’tanam P’kontème Bando, Yao Rodion Konu, Latame komla Adoli, Kodjo Akpadja, Kamevor Alaglo, Maweke Tchalim, P’niwè Patchali, Yaovi Djakpa, Komi Amekuse, Piham Gnossike, Denis A. Yawovi Gadah, and Didier Koumavi Ekouevi. Any resurgence of leprosy cases in the togo’s post-elimination period? trend analysis of reported leprosy cases from 2010 to 2022. BMC Infectious Diseases, Jun 2024. URL: https://doi.org/10.1186/s12879-024-09492-w, doi:10.1186/s12879-024-09492-w. This article has 2 citations and is from a peer-reviewed journal.

2. (li2024leprosytreatmentprevention pages 5-6): Xiang Li, Yun Ma, Guoli Li, Guangjie Jin, Li Xu, Yunhui Li, Pingmin Wei, and Lianhua Zhang. Leprosy: treatment, prevention, immune response and gene function. Frontiers in Immunology, Feb 2024. URL: https://doi.org/10.3389/fimmu.2024.1298749, doi:10.3389/fimmu.2024.1298749. This article has 21 citations and is from a peer-reviewed journal.

3. (dornelas2024roleofhistopathological pages 1-2): Bruno de Carvalho Dornelas, Willian Vargas Tenório da Costa, João Pablo Ferraz de Abreu, Juliana Salomão Daud, Felipe dos Anjos Rodrigues Campos, Deiriene Rodrigues de Oliveira Campos, Douglas Eulálio Antunes, Lúcio Borges de Araújo, Diogo Fernandes dos Santos, Cleverson Teixeira Soares, and Isabela Maria Bernardes Goulart. Role of histopathological, serological and molecular findings for the early diagnosis of treatment failure in leprosy. BMC Infectious Diseases, Oct 2024. URL: https://doi.org/10.1186/s12879-024-09937-2, doi:10.1186/s12879-024-09937-2. This article has 8 citations and is from a peer-reviewed journal.

4. (jong2024safetyofsingledose pages 1-2): Bouke Catherine de Jong, Said Nourdine, Auke Thomas Bergeman, Zahara Salim, Silahi Halifa Grillone, Sofie Marijke Braet, Mohamed Wirdane Abdou, Rian Snijders, Maya Ronse, Carolien Hoof, Achilleas Tsoumanis, Nimer Ortuño-Gutiérrez, Christian van der Werf, Alberto Piubello, Aboubacar Mzembaba, Younoussa Assoumani, and Epco Hasker. Safety of single-dose bedaquiline combined with rifampicin for leprosy post-exposure prophylaxis: a phase 2 randomized non-inferiority trial in the comoros islands. PLOS Medicine, 21:e1004453, Oct 2024. URL: https://doi.org/10.1371/journal.pmed.1004453, doi:10.1371/journal.pmed.1004453. This article has 4 citations and is from a highest quality peer-reviewed journal.

5. (huang2024anupdateof pages 1-2): Chien-Yuan Huang, Shih-Bin Su, and Kow-Tong Chen. An update of the diagnosis, treatment, and prevention of leprosy: a narrative review. Medicine, 103:e39006, Aug 2024. URL: https://doi.org/10.1097/md.0000000000039006, doi:10.1097/md.0000000000039006. This article has 26 citations and is from a peer-reviewed journal.

6. (kimta2024leprosycomprehensiveinsights pages 1-2): Neetika Kimta, Amin F. Majdalawieh, Gheyath K. Nasrallah, Sunil Puri, Eugenie Nepovimova, Klaudia Jomova, and Kamil Kuča. Leprosy: comprehensive insights into pathology, immunology, and cutting-edge treatment strategies, integrating nanoparticles and ethnomedicinal plants. Frontiers in Pharmacology, May 2024. URL: https://doi.org/10.3389/fphar.2024.1361641, doi:10.3389/fphar.2024.1361641. This article has 12 citations.

7. (silva2024anupdateon pages 1-2): Marcos Jessé Abrahão Silva, Caroliny Soares Silva, Thiago Pinto Brasil, Ana Karoliny Alves, Everaldina Cordeiro dos Santos, Cristiane Cunha Frota, Karla Valéria Batista Lima, and Luana Nepomuceno Gondim Costa Lima. An update on leprosy immunopathogenesis: systematic review. Frontiers in Immunology, Sep 2024. URL: https://doi.org/10.3389/fimmu.2024.1416177, doi:10.3389/fimmu.2024.1416177. This article has 20 citations and is from a peer-reviewed journal.

8. (barboza2024neutrophilicleukocytosisand pages 1-2): Marcella Feitosa da Silva Barboza, Mariana de Andrea Hacker, Anna Maria Sales, Débora Fontoura Rodrigues, Daniel Pedrosa Marques, Danillo José Ciryllo Silva Noya, Thabatta Leal Silveira Andrezo Rosa, Isabel de Fátima Alvim Braga, Helen Ferreira, Thais Porto Amadeu, Monique Gurgel de Oliveira, Alice de Miranda Machado, Ximena Illarramendi, and Veronica Schmitz. Neutrophilic leukocytosis and erythema nodosum leprosum in leprosy: insights from a retrospective observational study. Frontiers in Immunology, Jul 2024. URL: https://doi.org/10.3389/fimmu.2024.1368460, doi:10.3389/fimmu.2024.1368460. This article has 3 citations and is from a peer-reviewed journal.

9. (li2024leprosytreatmentprevention pages 1-2): Xiang Li, Yun Ma, Guoli Li, Guangjie Jin, Li Xu, Yunhui Li, Pingmin Wei, and Lianhua Zhang. Leprosy: treatment, prevention, immune response and gene function. Frontiers in Immunology, Feb 2024. URL: https://doi.org/10.3389/fimmu.2024.1298749, doi:10.3389/fimmu.2024.1298749. This article has 21 citations and is from a peer-reviewed journal.

10. (hinders2024thepep++study pages 1-2): Duane C. Hinders, Anneke T. Taal, Suchitra Lisam, Aymée M. da Rocha, Nand Lal Banstola, Prativa Bhandari, Abhijit Saha, Jugal Kishore, Virginia O. Fernandes, Abu Sufian Chowdhury, Anna T. van ‘t Noordende, Liesbeth Mieras, Jan Hendrik Richardus, and Wim H. van Brakel. The pep++ study protocol: a cluster-randomised controlled trial on the effectiveness of an enhanced regimen of post-exposure prophylaxis for close contacts of persons affected by leprosy to prevent disease transmission. BMC Infectious Diseases, Feb 2024. URL: https://doi.org/10.1186/s12879-024-09125-2, doi:10.1186/s12879-024-09125-2. This article has 14 citations and is from a peer-reviewed journal.

11. (slater2023acurrentperspective pages 45-47): Khushboo Borah Slater. A current perspective on leprosy (hansen’s disease). Vaccines for Neglected Pathogens: Strategies, Achievements and Challenges, pages 29-46, Jan 2023. URL: https://doi.org/10.1007/978-3-031-24355-4\_3, doi:10.1007/978-3-031-24355-4\_3. This article has 8 citations.

12. (huang2024anupdateof pages 6-6): Chien-Yuan Huang, Shih-Bin Su, and Kow-Tong Chen. An update of the diagnosis, treatment, and prevention of leprosy: a narrative review. Medicine, 103:e39006, Aug 2024. URL: https://doi.org/10.1097/md.0000000000039006, doi:10.1097/md.0000000000039006. This article has 26 citations and is from a peer-reviewed journal.

13. (santos2024adenosinea2areceptor pages 1-2): Plinio Marcos Freire dos Santos, Chyntia Carolina Díaz Acosta, Thabatta Leal Silveira Andrezo Rosa, Michelle Harumi Ishiba, André Alves Dias, Antonio Marcos Rodrigues Pereira, Luísa Domingos Gutierres, Melissa Pontes Pereira, Matheus da Silva Rocha, Patrícia Sammarco Rosa, Daniele F. F. Bertoluci, José Roberto Meyer-Fernandes, Fabricio da Mota Ramalho Costa, Maria Angela M. Marques, John T. Belisle, Roberta Olmo Pinheiro, Luciana Silva Rodrigues, Maria Cristina Vidal Pessolani, and Marcia Berrêdo-Pinho. Adenosine a2a receptor as a potential regulator of mycobacterium leprae survival mechanisms: new insights into leprosy neural damage. Frontiers in Pharmacology, Jun 2024. URL: https://doi.org/10.3389/fphar.2024.1399363, doi:10.3389/fphar.2024.1399363. This article has 2 citations.

14. (quilter2024isthewho pages 6-9): Emily E. V. Quilter and Cynthia Ruth Butlin. Is the who ‘global’ rate indicator an accurate reflection of the annual leprosy-associated disability burden experienced worldwide? Leprosy Review, Jun 2024. URL: https://doi.org/10.47276/lr.95.2.2024018, doi:10.47276/lr.95.2.2024018. This article has 4 citations and is from a peer-reviewed journal.

15. (quilter2024isthewho pages 3-6): Emily E. V. Quilter and Cynthia Ruth Butlin. Is the who ‘global’ rate indicator an accurate reflection of the annual leprosy-associated disability burden experienced worldwide? Leprosy Review, Jun 2024. URL: https://doi.org/10.47276/lr.95.2.2024018, doi:10.47276/lr.95.2.2024018. This article has 4 citations and is from a peer-reviewed journal.

16. (huang2024anupdateof pages 6-7): Chien-Yuan Huang, Shih-Bin Su, and Kow-Tong Chen. An update of the diagnosis, treatment, and prevention of leprosy: a narrative review. Medicine, 103:e39006, Aug 2024. URL: https://doi.org/10.1097/md.0000000000039006, doi:10.1097/md.0000000000039006. This article has 26 citations and is from a peer-reviewed journal.

17. (team2024theepidemiologyof pages 11-14): LEPKPS Team. The epidemiology of leprosy in karonga district, northern malawi 1973–2023: an analysis of leprosy’s distribution, risk factors, control and decline in rural africa. Leprosy Review, 95:7-84, Mar 2024. URL: https://doi.org/10.47276/lr.95.1.7, doi:10.47276/lr.95.1.7. This article has 1 citations and is from a peer-reviewed journal.

18. (zhou2024identificationofpotential pages 1-2): Qun Zhou, Ping Shi, Wei dong Shi, Jun Gao, Yi chen Wu, Jing Wan, Li li Yan, and Yi Zheng. Identification of potential biomarkers of leprosy: a study based on geo datasets. PLOS ONE, 19:e0302753, May 2024. URL: https://doi.org/10.1371/journal.pone.0302753, doi:10.1371/journal.pone.0302753. This article has 3 citations and is from a peer-reviewed journal.

19. (costa2024acosteffectivenessanalysis pages 1-2): Milene Rangel da Costa, Carlos Alberto da Silva Magliano, Bruno Monteiro Barros, Quenia Cristina Dias Morais, Andressa Araujo Braga, Kátia Marie Simões e Senna, Ciro Martins Gomes, Alexandre Casimiro de Macedo, and Marisa da Silva Santos. A cost-effectiveness analysis of a novel algorithm to sequentially diagnose leprosy based on manufactured tests under the sus perspective. Cadernos de Saúde Pública, Jan 2024. URL: https://doi.org/10.1590/0102-311xen038723, doi:10.1590/0102-311xen038723. This article has 7 citations.

20. (younoussa2023protocolrationaleand pages 1-2): Assoumani Younoussa, Said Nourdine Samidine, Auke T. Bergeman, Alberto Piubello, Nissad Attoumani, Silahi Halifa Grillone, Sofie Marijke Braet, Achilleas Tsoumanis, Abdallah Baco, Aboubacar Mzembaba, Zahara Salim, Mohamed Amidy, Saverio Grillone, Rian Snijders, Paul Corstjens, Nimer Ortuno-Gutierrez, Carolien Hoof, Annemieke Geluk, Bouke C. de Jong, and Epco Hasker. Protocol, rationale and design of be-people (bedaquiline enhanced exposure prophylaxis for leprosy in the comoros): a cluster randomized trial on effectiveness of rifampicin and bedaquiline as post-exposure prophylaxis of leprosy contacts. BMC Infectious Diseases, May 2023. URL: https://doi.org/10.1186/s12879-023-08290-0, doi:10.1186/s12879-023-08290-0. This article has 23 citations and is from a peer-reviewed journal.

21. (banstola2024effectivenessofongoing pages 1-2): N. Banstola, E. Hasker, L. Mieras, D. Gurung, B. Baral, S. Mehata, S. Prasai, Y. Ghimire, Brij Kumar Das, P. Napit, and Wim van Brakel. Effectiveness of ongoing single dose rifampicin post-exposure prophylaxis (sdr-pep) implementation under routine programme conditions—an observational study in nepal. PLOS Neglected Tropical Diseases, Dec 2024. URL: https://doi.org/10.1371/journal.pntd.0012446, doi:10.1371/journal.pntd.0012446. This article has 4 citations and is from a domain leading peer-reviewed journal.

22. (jong2024safetyofsingledose pages 7-9): Bouke Catherine de Jong, Said Nourdine, Auke Thomas Bergeman, Zahara Salim, Silahi Halifa Grillone, Sofie Marijke Braet, Mohamed Wirdane Abdou, Rian Snijders, Maya Ronse, Carolien Hoof, Achilleas Tsoumanis, Nimer Ortuño-Gutiérrez, Christian van der Werf, Alberto Piubello, Aboubacar Mzembaba, Younoussa Assoumani, and Epco Hasker. Safety of single-dose bedaquiline combined with rifampicin for leprosy post-exposure prophylaxis: a phase 2 randomized non-inferiority trial in the comoros islands. PLOS Medicine, 21:e1004453, Oct 2024. URL: https://doi.org/10.1371/journal.pmed.1004453, doi:10.1371/journal.pmed.1004453. This article has 4 citations and is from a highest quality peer-reviewed journal.

23. (saunderson2023whogloballeprosy pages 1-2): P Saunderson. Who global leprosy (hansen's disease) update, 2022: new paradigm–control to elimination. Unknown journal, 2023.

24. (jong2024safetyofsingledose pages 2-4): Bouke Catherine de Jong, Said Nourdine, Auke Thomas Bergeman, Zahara Salim, Silahi Halifa Grillone, Sofie Marijke Braet, Mohamed Wirdane Abdou, Rian Snijders, Maya Ronse, Carolien Hoof, Achilleas Tsoumanis, Nimer Ortuño-Gutiérrez, Christian van der Werf, Alberto Piubello, Aboubacar Mzembaba, Younoussa Assoumani, and Epco Hasker. Safety of single-dose bedaquiline combined with rifampicin for leprosy post-exposure prophylaxis: a phase 2 randomized non-inferiority trial in the comoros islands. PLOS Medicine, 21:e1004453, Oct 2024. URL: https://doi.org/10.1371/journal.pmed.1004453, doi:10.1371/journal.pmed.1004453. This article has 4 citations and is from a highest quality peer-reviewed journal.
