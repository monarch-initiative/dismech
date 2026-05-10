---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T12:50:58.567612'
end_time: '2026-05-10T12:59:14.510639'
duration_seconds: 495.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acquired Angioedema
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acquired Angioedema
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acquired Angioedema** covering all of the
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
- **Disease Name:** Acquired Angioedema
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acquired Angioedema** covering all of the
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


## Comprehensive Research Report: Acquired Angioedema (AAE), focusing on Acquired C1-Inhibitor Deficiency (AAE-C1-INH)

### Target Disease
- **Disease name:** Acquired angioedema (most commonly: acquired angioedema due to C1-inhibitor deficiency)
- **MONDO ID:** **MONDO:0019624** (“acquired angioedema”) (OpenTargets Search: Acquired angioedema)
- **Category:** Complex, typically secondary to underlying hematologic or autoimmune disease

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
Acquired angioedema due to C1-inhibitor deficiency (AAE-C1-INH; also written AAE-C1INH or C1-INH-AAE) is a **rare, non-hereditary, bradykinin-mediated** angioedema characterized by recurrent episodes of subcutaneous and/or submucosal swelling that may involve the face, tongue/oral cavity, gastrointestinal tract, and upper airway, with potential for fatal laryngeal edema. It is defined by **acquired deficiency or dysfunction of C1 inhibitor (C1-INH)** with accompanying complement abnormalities and typically occurs in adults with no family history. (bork2019angioedemadueto pages 1-2, sobotkova2021acquiredangioedemawith pages 1-2, grumach2021angioedemawithoutwheals pages 2-3)

### 1.2 Common synonyms / alternative names
- Acquired angioedema due to C1-inhibitor deficiency (AAE-C1-INH) (sobotkova2021acquiredangioedemawith pages 1-2, bork2019angioedemadueto pages 1-2)
- Acquired C1-inhibitor deficiency (johnson2023aretrospectiveanalysis pages 1-2)
- C1-INH-AAE (polai2023c1inhibitorc1inhibitorantibodycomplexes pages 1-2)

### 1.3 Key identifiers (availability in retrieved sources)
- **MONDO:** MONDO:0019624 (OpenTargets mapping) (OpenTargets Search: Acquired angioedema)
- **Other identifiers requested (ICD-10/ICD-11, Orphanet, MeSH, OMIM):** Not retrievable from the currently collected tool evidence; this report therefore **does not assert** specific ICD/Orphanet/MeSH/OMIM codes.

### 1.4 Evidence source types
The information in this report is derived primarily from **aggregated disease-level resources** (national cohort studies, referral-center cohorts, peer-reviewed reviews) and **clinical trial registry records**, rather than EHR-only sources. (sobotkova2021acquiredangioedemawith pages 1-2, bork2019angioedemadueto pages 1-2, NCT07266805 chunk 1)

---

## 2. Etiology

### 2.1 Primary causes (mechanistic)
AAE-C1-INH arises from **secondary (acquired) C1-INH deficiency**, resulting from (i) **consumption** of C1-INH and complement components (often driven by B-cell lymphoproliferation) and/or (ii) **autoantibody-mediated inactivation** of C1-INH. These processes lead to dysregulated activation of complement/contact systems and **excess bradykinin**, increasing vascular permeability and causing angioedema. (johnson2023aretrospectiveanalysis pages 1-2, bork2019angioedemadueto pages 1-2, grumach2021angioedemawithoutwheals pages 2-3)

### 2.2 Risk factors / associated conditions (high-confidence)
AAE-C1-INH is strongly associated with **B-cell lymphoproliferative disorders** and **monoclonal gammopathies**, and can also be associated with **autoimmune disease**.

Quantitative association data from cohorts:
- **Czech nationwide cohort (n=14)**: lymphoid malignancy **64% (9/14)**; MGUS **21% (3/14)**; autoimmune disease **7% (1/14)**; none identified **7% (1/14)**. (sobotkova2021acquiredangioedemawith pages 1-2)
- **Mainz referral cohort (n=44)**: MGUS **47.7%**; non-Hodgkin lymphoma **27.3%**; anti-C1-INH autoantibodies alone **11.4%**; no associated disorder **9.1%**. (bork2019angioedemadueto pages 1-2)

### 2.3 Triggers and precipitating factors
Triggers reported include **mechanical trauma, emotional stress, and ACE inhibitors** (as potential triggers/complicating exposures in bradykinin-mediated disease contexts). (polai2023c1inhibitorc1inhibitorantibodycomplexes pages 1-2)

### 2.4 Protective factors and gene–environment interactions
No protective factors or gene–environment interaction evidence specific to AAE-C1-INH were found in the retrieved tool evidence. Given that AAE-C1-INH is typically secondary and non-hereditary, genetic susceptibility is not generally the primary driver (contrast with hereditary angioedema). (sobotkova2021acquiredangioedemawith pages 1-2, grumach2021angioedemawithoutwheals pages 2-3)

---

## 3. Phenotypes

### 3.1 Clinical phenotype spectrum and frequencies
AAE-C1-INH commonly presents with recurrent non-urticarial swelling affecting facial/oropharyngeal tissues, airway, abdomen, and extremities. In a Czech nationwide series (n=14), phenotype frequencies were:
- **Facial edema:** 100% (14/14)
- **Upper airway involvement:** 85.7% (12/14)
- **Abdominal attacks:** 50% (7/14)
- **Peripheral angioedema:** 42.8% (6/14) (sobotkova2021acquiredangioedemawith pages 4-5)

Disease onset in this cohort occurred between **40–82 years** (median **59.5**). (sobotkova2021acquiredangioedemawith pages 4-5)

### 3.2 Phenotype characteristics
- **Age of onset:** Typically adult-onset, often **>40 years**; cohort median near 60 years. (sobotkova2021acquiredangioedemawith pages 1-2, sobotkova2021acquiredangioedemawith pages 4-5)
- **Course pattern:** Episodic attacks.
- **Severity:** Potentially life-threatening due to airway involvement. (bork2019angioedemadueto pages 1-2)

### 3.3 Quality-of-life (QoL) impact
Direct AAE-C1-INH QoL data in the retrieved evidence are limited; however, a small real-world prophylaxis series that included AAE-C1-INH patients reported **improvement** in angioedema-specific QoL and control measures with berotralstat (see Treatment section). (johnson2023aretrospectiveanalysis pages 1-2)

### 3.4 Suggested HPO terms (non-exhaustive)
Based on the above cohort phenotypes:
- **Angioedema:** HP:0100664
- **Facial swelling:** HP:0000280
- **Laryngeal edema / upper airway edema:** HP:0011106 (laryngeal edema) / HP:0011107 (airway edema; term usage varies)
- **Abdominal pain (during abdominal attacks):** HP:0002027
- **Edema of extremities:** HP:0000969

(sobotkova2021acquiredangioedemawith pages 4-5)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and variants
AAE-C1-INH is **not primarily a germline genetic disorder**; it is defined by an **acquired** deficiency/dysfunction of C1-INH rather than inherited SERPING1 mutations. In diagnostic frameworks, lack of SERPING1 mutation supports acquired disease when combined with late onset and complement patterns. (grumach2021angioedemawithoutwheals pages 2-3, caballero2022medicalalgorithmmanagement pages 2-2)

### 4.2 Autoantibodies and immune complexes (key molecular entities)
Anti–C1-INH autoantibodies may be present as free antibodies or in immune complexes, which has diagnostic implications:
- In a European AAE cohort (n=20), **free anti-C1INHAbs** were detected in **9/20**, while **C1INH–antiC1INHAb complexes** were detected in **18/20**; notably **9/20** were negative for free antibodies but positive for complexes at first measurement. (lopezlera2019serumcomplexesbetween pages 1-2)
- A Hungarian center cohort (n=19) reported 79% with an underlying disease and recommended measuring **C1-INH/C1-INH antibody complexes (CAC)** in parallel with free antibody testing for improved detection and monitoring. (polai2023c1inhibitorc1inhibitorantibodycomplexes pages 1-2)

### 4.3 Suggested CHEBI entities (therapeutic-relevant)
- **Bradykinin:** CHEBI:15883 (central mediator; evidence of bradykinin-mediated mechanism from reviews/algorithms) (bork2019angioedemadueto pages 1-2, grumach2021angioedemawithoutwheals pages 2-3)

---

## 5. Environmental Information

### 5.1 Environmental/lifestyle factors
No population-level environmental or lifestyle risk factor evidence specific to AAE-C1-INH was captured in the retrieved documents.

### 5.2 Drug-related triggers
ACE inhibitors are mentioned as potential triggers/associations in the context of bradykinin-mediated angioedema and can confound diagnosis; AAE-C1-INH has specific complement abnormalities that help distinguish it. (polai2023c1inhibitorc1inhibitorantibodycomplexes pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (trigger → mediator → phenotype)
1. **Underlying B-cell lymphoproliferation/MGUS** and/or **autoantibodies** leads to **consumption or inactivation** of C1-INH. (sobotkova2021acquiredangioedemawith pages 1-2, bork2019angioedemadueto pages 1-2, johnson2023aretrospectiveanalysis pages 1-2)
2. Reduced functional C1-INH permits dysregulated activation of complement/contact systems, increasing downstream generation of **bradykinin**. (grumach2021angioedemawithoutwheals pages 2-3, bork2019angioedemadueto pages 1-2)
3. Bradykinin increases **vascular permeability**, producing episodic **submucosal/subcutaneous edema** (angioedema), including potentially fatal laryngeal edema. (bork2019angioedemadueto pages 1-2, grumach2021angioedemawithoutwheals pages 2-3)

### 6.2 Upstream vs downstream
- **Upstream:** Underlying disease (lymphoproliferative, MGUS, autoimmune), anti–C1-INH antibodies/complexes, complement consumption (low C1q suggests classical pathway involvement). (sobotkova2021acquiredangioedemawith pages 1-2, bork2019angioedemadueto pages 1-2, lopezlera2019serumcomplexesbetween pages 1-2)
- **Downstream:** Bradykinin-mediated permeability and tissue swelling; failure to respond to histamine-directed therapies is a practical downstream clinical discriminator in reviews/algorithms. (falco2025orofacialangioedemaan pages 3-5, caballero2022medicalalgorithmmanagement pages 2-2)

### 6.3 Suggested GO Biological Process terms (examples)
- **Complement activation, classical pathway:** GO:0006958 (supported by complement consumption patterns, low C1q) (sobotkova2021acquiredangioedemawith pages 4-5, grumach2021angioedemawithoutwheals pages 2-3)
- **Regulation of blood vessel permeability:** GO:0008217 (bradykinin-mediated edema phenotype) (bork2019angioedemadueto pages 1-2)

### 6.4 Suggested Cell Ontology (CL) terms (best-effort)
Because many associations are B-cell/monoclonal gammopathy driven:
- **B cell:** CL:0000236
- **Plasma cell:** CL:0000786

(sobotkova2021acquiredangioedemawith pages 1-2, bork2019angioedemadueto pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Primary anatomical sites and systems (with UBERON suggestions)
From cohort phenotype data, commonly affected sites include:
- **Face:** UBERON:0001456 (sobotkova2021acquiredangioedemawith pages 4-5)
- **Upper airway/larynx:** UBERON:0001737 (larynx) (sobotkova2021acquiredangioedemawith pages 4-5, bork2019angioedemadueto pages 1-2)
- **Gastrointestinal tract (bowel):** UBERON:0001555 (digestive tract) / UBERON:0002108 (small intestine) (abdominal attacks) (sobotkova2021acquiredangioedemawith pages 4-5)
- **Extremities/limbs:** UBERON:0002101 (limb) (sobotkova2021acquiredangioedemawith pages 4-5)

---

## 8. Temporal Development

### 8.1 Onset and course
AAE-C1-INH typically has **adult onset (>40 years)**, often late middle age, and follows an **episodic** course with recurrent attacks. In the Czech nationwide cohort, the median onset age was **59.5 years** and diagnosis delay median **1 year**. (sobotkova2021acquiredangioedemawith pages 1-2)

### 8.2 Remission patterns
Treating underlying lymphoproliferative disease can reduce attack frequency and may normalize complement parameters (reported as an observation in the Czech cohort summary). (sobotkova2021acquiredangioedemawith pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Inheritance pattern
AAE-C1-INH is **acquired** and therefore **not inherited** in a Mendelian fashion; it is differentiated from hereditary angioedema by lack of family history and lack of SERPING1 mutation in diagnostic algorithms. (grumach2021angioedemawithoutwheals pages 2-3, caballero2022medicalalgorithmmanagement pages 2-2)

### 9.2 Epidemiology (statistics)
Best-available prevalence estimates from retrieved sources:
- **Czech Republic nationwide retrospective study:** prevalence ~**1:760,000**; AAE-C1-INH accounted for ~**8%** of angioedema with C1-INH deficiency in that setting. (sobotkova2021acquiredangioedemawith pages 1-2)
- Literature estimates: **1:100,000–1:500,000** inhabitants. (bork2019angioedemadueto pages 1-2, lopezlera2019serumcomplexesbetween pages 1-2)
- A recent real-world prophylaxis paper cites prevalence ~**0.15 per 100,000**. (johnson2023aretrospectiveanalysis pages 1-2)

Sex distribution in Czech cohort was **7 male / 7 female** (1:1). (sobotkova2021acquiredangioedemawith pages 4-5)

---

## 10. Diagnostics

### 10.1 Core diagnostic laboratory tests (complement/C1-INH panel)
A practical and widely referenced pattern for AAE-C1-INH is:
- **Low C4**
- **Low C1-INH functional activity**
- **Low C1-INH antigen** (often)
- **Low C1q** (frequent, helpful to differentiate acquired from hereditary forms)
- **Anti–C1-INH autoantibodies** and/or **C1-INH–anti–C1-INH immune complexes** in many cases

Czech cohort laboratory frequencies provide concrete performance-like data:
- Low C4: **14/14 (100%)**
- Low C1-INH function: **14/14 (100%)**
- Low C1-INH antigen: **13/14 (93%)**
- Low C1q: **10/14 (71.4%)** (sobotkova2021acquiredangioedemawith pages 4-5)

A review focused on laboratory differentiation summarizes the pattern as AAE-C1-INH having low C1-INH function and concentration, low C4, low C1q, and frequently anti–C1-INH antibodies, without SERPING1 mutation. (grumach2021angioedemawithoutwheals pages 2-3)

### 10.2 Antibody/complex testing as a diagnostic enhancer (recent development)
A key 2019 development is demonstration that **immune-complex detection may be more sensitive than free antibody detection**: C1INH–antiC1INHAb complexes were found in **18/20** AAE cases even when free antibodies were negative (9/20). (lopezlera2019serumcomplexesbetween pages 1-2)
A 2023 Orphanet Journal paper further argues CAC measurements can aid prediction/monitoring of underlying disease and recommends parallel measurement with free antibody. (polai2023c1inhibitorc1inhibitorantibodycomplexes pages 1-2)

### 10.3 Differential diagnosis (high-level)
- **Hereditary angioedema due to C1-INH deficiency (HAE types I/II):** similar clinical phenotype but typically earlier onset and normal C1q; SERPING1 variants may be present. (grumach2021angioedemawithoutwheals pages 2-3, caballero2022medicalalgorithmmanagement pages 2-2)
- **Histaminergic angioedema:** tends to respond to antihistamines/corticosteroids/epinephrine; complement panel typically normal. (falco2025orofacialangioedemaan pages 3-5, caballero2022medicalalgorithmmanagement pages 2-2)
- **ACE inhibitor–associated angioedema:** bradykinin-mediated but lacks the characteristic complement abnormalities; diagnosis is clinical/exclusion. (grumach2021angioedemawithoutwheals pages 2-3)

### 10.4 Suggested LOINC-style test names (best-effort)
(Exact LOINC codes were not available in retrieved evidence; below are standardized test concepts commonly used clinically.)
- Complement C4 [Mass/volume] in Serum/Plasma (C4)
- C1 esterase inhibitor [Mass/volume] in Serum/Plasma (C1-INH antigen)
- C1 esterase inhibitor activity in Serum/Plasma (C1-INH function)
- Complement C1q [Mass/volume] in Serum/Plasma (C1q)
- Anti–C1-INH antibody (IgG/IgM) in Serum; and/or C1-INH–anti–C1-INH immune complexes (ELISA-based) (lopezlera2019serumcomplexesbetween pages 1-2, polai2023c1inhibitorc1inhibitorantibodycomplexes pages 1-2)

---

## 11. Outcome / Prognosis

### 11.1 Morbidity and mortality considerations
AAE-C1-INH can be life-threatening due to **laryngeal edema/asphyxiation risk**. (bork2019angioedemadueto pages 1-2)

### 11.2 Prognostic factors (inferred from cohort observations)
- Presence and treatability of an underlying lymphoproliferative disorder is clinically important; treating lymphoma was associated with reduced angioedema activity and complement normalization in a Czech cohort summary. (sobotkova2021acquiredangioedemawith pages 1-2)

Robust survival rates, mortality rates, or long-term disability estimates were not present in the retrieved tool evidence.

---

## 12. Treatment

### 12.1 Current applications and real-world implementations
No therapies are universally approved specifically for AAE-C1-INH in many jurisdictions; clinical practice often uses HAE-directed therapies **off-label**. (johnson2023aretrospectiveanalysis pages 1-2, bork2019angioedemadueto pages 1-2)

#### On-demand (acute attack) treatments
- **Plasma-derived C1-INH concentrate (pdC1-INH)**: In a 44-patient referral cohort, pdC1-INH was reported effective in **3553/3636 attacks (97.7%)** and shortened attack duration by **54.4 ± 32.8 hours** on average; effectiveness remained high even in anti–C1-INH antibody-positive patients (93.8% effectiveness). (bork2019angioedemadueto pages 1-2)
- **Icatibant** (bradykinin B2 receptor antagonist): In Czech cohort, icatibant was used (n=8) and reported efficient in all treated cases. (sobotkova2021acquiredangioedemawith pages 4-5)
- **Recombinant C1-INH**: used acutely in Czech cohort (n=4), efficient in all treated cases. (sobotkova2021acquiredangioedemawith pages 4-5)

#### Long-term prophylaxis and disease control (recent evidence; 2023 focus)
- **Berotralstat (oral plasma kallikrein inhibitor)**: A 2023 real-world retrospective series included **3 AAE-C1-INH** patients; after 6 months, median attacks/month decreased from **2.3 to 1.0**, with **AE-QoL improvement of 13.7 points** and **AECT increase of 4.2 points**. (johnson2023aretrospectiveanalysis pages 1-2)
- **Tranexamic acid (TA)**: In Czech cohort, long-term prophylaxis was started in 9/14; TA was used in 5, and was effective as a single agent in 2/5. (sobotkova2021acquiredangioedemawith pages 4-5)

#### Treating underlying disease (mechanism-directed upstream therapy)
Because AAE-C1-INH is commonly associated with lymphoproliferative disease/MGUS, evaluation and treatment of the underlying disorder is a core real-world strategy, with cohort observations of attack reduction and complement normalization after lymphoma treatment. (sobotkova2021acquiredangioedemawith pages 1-2)

### 12.2 Experimental / clinical trials (recent developments; 2024–2026 registry data)
- **Lanadelumab in long-term prophylaxis of acquired angioedema (NCT06818474)**: Phase 4, open-label, single-group study; inclusion specifies recurrent AAE without urticaria plus labs consistent with acquired C1-INH deficiency (decreased C1INH functional/quantitative, decreased C4, decreased C1q, no family history, anti-C1INH Ab and/or paraproteinemia). Start date **2024-06-01**; first posted **2025-02-10**. URL: https://clinicaltrials.gov/ct2/show/NCT06818474 (NCT06818474 chunk 1)
- **Deucrictibant (oral bradykinin B2 receptor antagonist) for AAE-C1INH (NCT07266805, “CREAATE”)**: Phase 3 randomized placebo-controlled multi-part study testing XR prophylaxis and IR on-demand treatment; start date **2025-10-16**; first posted **2025-12-05**; last update **2026-05-07**. URL: https://clinicaltrials.gov/study/NCT07266805 (NCT07266805 chunk 1)

### 12.3 Suggested MAXO terms (examples; best-effort)
- **C1 esterase inhibitor replacement therapy** (pdC1-INH/rhC1-INH) (bork2019angioedemadueto pages 1-2, sobotkova2021acquiredangioedemawith pages 4-5)
- **Bradykinin receptor antagonist therapy** (icatibant; and oral B2 antagonist under trial) (sobotkova2021acquiredangioedemawith pages 4-5, NCT07266805 chunk 1)
- **Kallikrein inhibitor therapy** (berotralstat; lanadelumab) (johnson2023aretrospectiveanalysis pages 1-2, NCT06818474 chunk 1)
- **Antifibrinolytic therapy** (tranexamic acid) (sobotkova2021acquiredangioedemawith pages 4-5)
- **Treatment of underlying lymphoproliferative disease** (sobotkova2021acquiredangioedemawith pages 1-2, bork2019angioedemadueto pages 1-2)

---

## 13. Prevention

### 13.1 Prevention levels
- **Primary prevention:** Not well-defined because AAE-C1-INH is typically secondary to underlying conditions rather than preventable exposures.
- **Secondary/tertiary prevention:** Key strategy is early recognition of bradykinin-mediated angioedema, confirmation with complement testing, and preventing airway compromise through rapid access to effective on-demand therapy; additionally, identifying/treating underlying lymphoproliferative disease can reduce recurrence. (sobotkova2021acquiredangioedemawith pages 1-2, bork2019angioedemadueto pages 1-2)

Short-term procedural prophylaxis is discussed in broader angioedema management reviews (not AAE-specific in the retrieved evidence), but AAE patients are often managed analogously to HAE in practice where clinically justified. (caballero2022medicalalgorithmmanagement pages 2-2)

---

## 14. Other Species / Natural Disease

No evidence for naturally occurring AAE-C1-INH as a defined disease entity in other species was identified in the retrieved evidence. AAE-C1-INH is primarily a human secondary immunologic/hematologic syndrome.

---

## 15. Model Organisms

The retrieved evidence did not include specific in vivo models of **acquired** C1-INH deficiency angioedema. Mechanistic work in bradykinin/complement biology often uses complement/contact system models, but explicit AAE-C1-INH model-organism validation was not present in the collected sources.

---

## Key quantitative facts table (for knowledge base ingestion)

| Topic | Key details (quantitative where available) | Best supporting sources (with year, journal, DOI/URL) | Notes |
|---|---|---|---|
| Acquired Angioedema (AAE-C1-INH) key facts — definition | Rare, non-hereditary, bradykinin-mediated angioedema caused by acquired C1-inhibitor deficiency; clinically similar to hereditary C1-INH deficiency; may cause life-threatening laryngeal edema/asphyxiation. Typically lacks family history and SERPING1 mutation. (bork2019angioedemadueto pages 1-2, grumach2021angioedemawithoutwheals pages 2-3) | Sobotkova et al., 2021, *Int Arch Allergy Immunol*, doi:10.1159/000512933, https://doi.org/10.1159/000512933 (sobotkova2021acquiredangioedemawith pages 1-2); Bork et al., 2019, *Orphanet J Rare Dis*, doi:10.1186/s13023-019-1043-3, https://doi.org/10.1186/s13023-019-1043-3 (bork2019angioedemadueto pages 1-2); Grumach et al., 2021, *Front Immunol*, doi:10.3389/fimmu.2021.785736, https://doi.org/10.3389/fimmu.2021.785736 (grumach2021angioedemawithoutwheals pages 2-3) | Aggregated disease-level literature, not individual EHR-derived definitions. |
| Typical onset | Adult onset, usually after age 40; Czech nationwide cohort median symptom onset 59.5 years (range 40–82). Diagnostic delay in Czech cohort: median 1 year. (sobotkova2021acquiredangioedemawith pages 1-2, sobotkova2021acquiredangioedemawith pages 4-5) | Sobotkova et al., 2021, *Int Arch Allergy Immunol*, doi:10.1159/000512933, https://doi.org/10.1159/000512933 (sobotkova2021acquiredangioedemawith pages 1-2, sobotkova2021acquiredangioedemawith pages 4-5); Johnson et al., 2023, *Clin Rev Allergy Immunol*, doi:10.1007/s12016-023-08972-2, https://doi.org/10.1007/s12016-023-08972-2 (johnson2023aretrospectiveanalysis pages 1-2) | Later onset is a major clue distinguishing AAE from hereditary disease. |
| Core lab pattern | Typical pattern: low C1-INH function, low/usually low C1-INH antigen, low C4, and often low C1q. In Czech cohort: low C4 14/14 (100%), low C1-INH function 14/14 (100%), low C1-INH antigen 13/14 (93%), low C1q 10/14 (71.4%). Anti-C1-INH antibodies are frequent but not universal. (sobotkova2021acquiredangioedemawith pages 4-5, grumach2021angioedemawithoutwheals pages 2-3) | Sobotkova et al., 2021, *Int Arch Allergy Immunol*, doi:10.1159/000512933, https://doi.org/10.1159/000512933 (sobotkova2021acquiredangioedemawith pages 4-5); Grumach et al., 2021, *Front Immunol*, doi:10.3389/fimmu.2021.785736, https://doi.org/10.3389/fimmu.2021.785736 (grumach2021angioedemawithoutwheals pages 2-3); López-Lera et al., 2019, *Clin Exp Immunol*, doi:10.1111/cei.13361, https://doi.org/10.1111/cei.13361 (lopezlera2019serumcomplexesbetween pages 1-2) | Low C1q helps distinguish AAE-C1-INH from HAE-C1-INH, though exceptions exist. |
| Associated conditions — Czech cohort | Underlying disease in 13/14 (93%): lymphoid malignancy 9/14 (64%), MGUS 3/14 (21%), autoimmune disease 1/14 (7%), no underlying disease 1/14 (7%). (sobotkova2021acquiredangioedemawith pages 1-2) | Sobotkova et al., 2021, *Int Arch Allergy Immunol*, doi:10.1159/000512933, https://doi.org/10.1159/000512933 (sobotkova2021acquiredangioedemawith pages 1-2) | Supports strong need to investigate lymphoproliferative and autoimmune disorders. |
| Associated conditions — Bork cohort | In 44-patient cohort: MGUS 47.7%, non-Hodgkin lymphoma 27.3%, anti-C1-INH autoantibodies alone 11.4%, other conditions 4.5%, no associated disorder 9.1%. AAE led to lymphoma detection in 75% of patients with malignancy. (bork2019angioedemadueto pages 1-2) | Bork et al., 2019, *Orphanet J Rare Dis*, doi:10.1186/s13023-019-1043-3, https://doi.org/10.1186/s13023-019-1043-3 (bork2019angioedemadueto pages 1-2) | One of the most quantitative cohort summaries for associated disorders. |
| Prevalence / occurrence estimates | Ultra-rare. Reported prevalence estimates: ~1:760,000 in Czech Republic; literature estimate 1:100,000 to 1:500,000; one review cites ~0.15 per 100,000. AAE-C1-INH represented ~8% of angioedema with C1-INH deficiency in the Czech study. (sobotkova2021acquiredangioedemawith pages 1-2, johnson2023aretrospectiveanalysis pages 1-2, lopezlera2019serumcomplexesbetween pages 1-2) | Sobotkova et al., 2021, *Int Arch Allergy Immunol*, doi:10.1159/000512933, https://doi.org/10.1159/000512933 (sobotkova2021acquiredangioedemawith pages 1-2); Johnson et al., 2023, *Clin Rev Allergy Immunol*, doi:10.1007/s12016-023-08972-2, https://doi.org/10.1007/s12016-023-08972-2 (johnson2023aretrospectiveanalysis pages 1-2); López-Lera et al., 2019, *Clin Exp Immunol*, doi:10.1111/cei.13361, https://doi.org/10.1111/cei.13361 (lopezlera2019serumcomplexesbetween pages 1-2) | Incidence estimates are sparse; prevalence usually inferred from national or referral-center cohorts. |
| Phenotype frequencies — Czech cohort | Facial edema 14/14 (100%); upper airway involvement 12/14 (85.7%); abdominal attacks 7/14 (50%); peripheral angioedema 6/14 (42.8%). (sobotkova2021acquiredangioedemawith pages 4-5) | Sobotkova et al., 2021, *Int Arch Allergy Immunol*, doi:10.1159/000512933, https://doi.org/10.1159/000512933 (sobotkova2021acquiredangioedemawith pages 4-5) | Facial and airway attacks were especially prominent in this cohort. |
| Antibody / immune-complex detection | European cohort (n=20): free anti-C1INH antibodies detected in 9/20 (45%); C1INH–anti-C1INH immune complexes detected in 18/20 (90%); 9/20 were negative for free antibodies but positive for complexes at first measurement. Hungarian cohort (n=19): 79% had an underlying disease; 11/19 had detectable anti-C1-INH antibodies at least once. (lopezlera2019serumcomplexesbetween pages 1-2, polai2023c1inhibitorc1inhibitorantibodycomplexes pages 1-2) | López-Lera et al., 2019, *Clin Exp Immunol*, doi:10.1111/cei.13361, https://doi.org/10.1111/cei.13361 (lopezlera2019serumcomplexesbetween pages 1-2); Polai et al., 2023, *Orphanet J Rare Dis*, doi:10.1186/s13023-023-02625-5, https://doi.org/10.1186/s13023-023-02625-5 (polai2023c1inhibitorc1inhibitorantibodycomplexes pages 1-2) | Measuring complexes alongside free antibody may improve diagnostic yield and monitoring. |
| Acute treatment effectiveness | Plasma-derived C1-INH (pdC1-INH) was effective in 3553/3636 attacks (97.7%) and shortened attacks by mean 54.4 ± 32.8 hours; effectiveness in anti-C1-INH autoantibody-positive patients was 1246/1329 attacks (93.8%). Czech cohort: icatibant (n=8), pdC1-INH/Berinert (n=4), and recombinant C1-INH (n=4) were all reported effective in all treated cases. (bork2019angioedemadueto pages 7-8, sobotkova2021acquiredangioedemawith pages 4-5, bork2019angioedemadueto pages 1-2) | Bork et al., 2019, *Orphanet J Rare Dis*, doi:10.1186/s13023-019-1043-3, https://doi.org/10.1186/s13023-019-1043-3 (bork2019angioedemadueto pages 7-8, bork2019angioedemadueto pages 1-2); Sobotkova et al., 2021, *Int Arch Allergy Immunol*, doi:10.1159/000512933, https://doi.org/10.1159/000512933 (sobotkova2021acquiredangioedemawith pages 4-5) | No therapies are specifically approved for AAE-C1-INH in many regions; use is often extrapolated from HAE. |
| Prophylaxis / QoL real-world data | Berotralstat real-world series included 3 AAE-C1-INH patients. After 6 months, median attacks/month fell from 2.3 to 1.0; no aerodigestive attacks were noted; mean AE-QoL improved by 13.7 points; AECT increased by 4.2 points. (johnson2023aretrospectiveanalysis pages 1-2) | Johnson et al., 2023, *Clin Rev Allergy Immunol*, doi:10.1007/s12016-023-08972-2, https://doi.org/10.1007/s12016-023-08972-2 (johnson2023aretrospectiveanalysis pages 1-2) | Small sample, off-label use, but among the most relevant recent 2023 real-world AAE prophylaxis/QoL data. |


*Table: This table summarizes the main clinical, laboratory, epidemiologic, and treatment facts for acquired angioedema due to C1-inhibitor deficiency using only the gathered evidence. It highlights quantitative cohort findings and recent real-world treatment data that are particularly useful for a disease knowledge base.*

---

## Expert opinion and analysis (synthesis of authoritative sources)

1. **Diagnostic emphasis:** Multiple authoritative reviews/algorithms converge on the idea that AAE-C1-INH is best recognized by combining clinical context (late onset, no family history) with a complement/C1-INH laboratory panel including **C1q** and optional anti–C1-INH testing; however, these markers can show exceptions, so repeated testing and comprehensive evaluation for underlying B-cell disease are often required. (grumach2021angioedemawithoutwheals pages 2-3, caballero2022medicalalgorithmmanagement pages 2-2, sobotkova2021acquiredangioedemawith pages 4-5)
2. **Recent methodological refinement (2023):** Measuring **C1-INH/anti–C1-INH complexes** (CAC) in parallel with free antibodies is a notable 2023 development aimed at improving detection and potentially monitoring underlying disease evolution. (polai2023c1inhibitorc1inhibitorantibodycomplexes pages 1-2)
3. **Treatment reality:** Despite the absence of universally approved AAE-specific therapies, real-world cohort data support high effectiveness of **pdC1-INH** for acute attacks, and emerging prophylaxis approaches (e.g., oral kallikrein inhibition with berotralstat) show promising reductions in attack rate and improved patient-reported outcomes in small AAE subsets. (bork2019angioedemadueto pages 1-2, johnson2023aretrospectiveanalysis pages 1-2)

---

## Notes on citation requirements (PMID availability)
Several retrieved sources did not include PMIDs in the text snippets available to the tool; therefore, this report provides **DOIs/URLs and publication dates** from the retrieved metadata, and does not fabricate PMIDs.


References

1. (OpenTargets Search: Acquired angioedema): Open Targets Query (Acquired angioedema, 11 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (bork2019angioedemadueto pages 1-2): Konrad Bork, Petra Staubach-Renz, and Jochen Hardt. Angioedema due to acquired c1-inhibitor deficiency: spectrum and treatment with c1-inhibitor concentrate. Orphanet Journal of Rare Diseases, Mar 2019. URL: https://doi.org/10.1186/s13023-019-1043-3, doi:10.1186/s13023-019-1043-3. This article has 68 citations and is from a peer-reviewed journal.

3. (sobotkova2021acquiredangioedemawith pages 1-2): Marta Sobotkova, Radana Zachova, Roman Hakl, Pavel Kuklinek, Pavlina Kralickova, Irena Krcmova, Jana Hanzlikova, Martina Vachova, and Jirina Bartunkova. Acquired angioedema with c1 inhibitor deficiency: occurrence, clinical features, and management: a nationwide retrospective study in the czech republic patients. International Archives of Allergy and Immunology, 182:642-649, Jan 2021. URL: https://doi.org/10.1159/000512933, doi:10.1159/000512933. This article has 33 citations and is from a peer-reviewed journal.

4. (grumach2021angioedemawithoutwheals pages 2-3): Anete S. Grumach, Camila L. Veronez, Dorottya Csuka, and Henriette Farkas. Angioedema without wheals: challenges in laboratorial diagnosis. Frontiers in Immunology, Dec 2021. URL: https://doi.org/10.3389/fimmu.2021.785736, doi:10.3389/fimmu.2021.785736. This article has 26 citations and is from a peer-reviewed journal.

5. (johnson2023aretrospectiveanalysis pages 1-2): Felix Johnson, Anna Stenzl, Benedikt Hofauer, Helen Heppt, Eva-Vanessa Ebert, Barbara Wollenberg, Robin Lochbaum, Janina Hahn, Jens Greve, and Susanne Trainotti. A retrospective analysis of long-term prophylaxis with berotralstat in patients with hereditary angioedema and acquired c1-inhibitor deficiency—real-world data. Clinical Reviews in Allergy & Immunology, 65:354-364, Nov 2023. URL: https://doi.org/10.1007/s12016-023-08972-2, doi:10.1007/s12016-023-08972-2. This article has 14 citations and is from a peer-reviewed journal.

6. (polai2023c1inhibitorc1inhibitorantibodycomplexes pages 1-2): Zsofia Polai, Erika Kajdacsi, Laszlo Cervenak, Zsuzsanna Balla, Szabolcs Benedek, Lilian Varga, and Henriette Farkas. C1-inhibitor/c1-inhibitor antibody complexes in acquired angioedema due to c1-inhibitor deficiency. Orphanet Journal of Rare Diseases, Feb 2023. URL: https://doi.org/10.1186/s13023-023-02625-5, doi:10.1186/s13023-023-02625-5. This article has 6 citations and is from a peer-reviewed journal.

7. (NCT07266805 chunk 1):  Study of Oral Deucrictibant XR Tablet for Prophylaxis and Deucrictibant IR Capsule for On-Demand Treatment of Angioedema Attacks in Adults With Acquired Angioedema Due to C1 Inhibitor Deficiency. Pharvaris Netherlands B.V.. 2025. ClinicalTrials.gov Identifier: NCT07266805

8. (sobotkova2021acquiredangioedemawith pages 4-5): Marta Sobotkova, Radana Zachova, Roman Hakl, Pavel Kuklinek, Pavlina Kralickova, Irena Krcmova, Jana Hanzlikova, Martina Vachova, and Jirina Bartunkova. Acquired angioedema with c1 inhibitor deficiency: occurrence, clinical features, and management: a nationwide retrospective study in the czech republic patients. International Archives of Allergy and Immunology, 182:642-649, Jan 2021. URL: https://doi.org/10.1159/000512933, doi:10.1159/000512933. This article has 33 citations and is from a peer-reviewed journal.

9. (caballero2022medicalalgorithmmanagement pages 2-2): Teresa Caballero, Rosario Cabañas, and María Pedrosa. Medical algorithm: management of c1 inhibitor hereditary angioedema. Allergy, 77:1060-1063, Oct 2022. URL: https://doi.org/10.1111/all.15115, doi:10.1111/all.15115. This article has 4 citations and is from a highest quality peer-reviewed journal.

10. (lopezlera2019serumcomplexesbetween pages 1-2): A. López-Lera, S. Garrido, P. Nozal, Lillemor Skatum, A. Bygum, T. Caballero, and M. López Trascasa. Serum complexes between c1inh and c1inh autoantibodies for the diagnosis of acquired angioedema. Clinical & Experimental Immunology, 198:341-350, Dec 2019. URL: https://doi.org/10.1111/cei.13361, doi:10.1111/cei.13361. This article has 12 citations and is from a peer-reviewed journal.

11. (falco2025orofacialangioedemaan pages 3-5): Domenico De Falco, Diego Misceo, Giuseppe Carretta, Gioele Gioco, Carlo Lajolo, and Massimo Petruzzi. Oro-facial angioedema: an overview. Immuno, 5:61, Dec 2025. URL: https://doi.org/10.3390/immuno5040061, doi:10.3390/immuno5040061. This article has 2 citations.

12. (NCT06818474 chunk 1): Jonathan A. Bernstein, MD. Lanadelumab in Long-term Prophylaxis of Acquired Angioedema. Bernstein Clinical Research Center. 2024. ClinicalTrials.gov Identifier: NCT06818474

13. (bork2019angioedemadueto pages 7-8): Konrad Bork, Petra Staubach-Renz, and Jochen Hardt. Angioedema due to acquired c1-inhibitor deficiency: spectrum and treatment with c1-inhibitor concentrate. Orphanet Journal of Rare Diseases, Mar 2019. URL: https://doi.org/10.1186/s13023-019-1043-3, doi:10.1186/s13023-019-1043-3. This article has 68 citations and is from a peer-reviewed journal.