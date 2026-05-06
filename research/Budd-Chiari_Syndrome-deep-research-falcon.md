---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T07:56:56.730294'
end_time: '2026-05-06T08:28:10.693976'
duration_seconds: 1873.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Budd-Chiari Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Budd-Chiari Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Budd-Chiari Syndrome** covering all of the
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
- **Disease Name:** Budd-Chiari Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Budd-Chiari Syndrome** covering all of the
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


# Budd–Chiari Syndrome (BCS) — Disease Characteristics Research Report

## Executive summary
Budd–Chiari syndrome (BCS) is **hepatic venous outflow tract obstruction (HVOTO)** causing hepatic congestion, portal hypertension, and progressive fibrosis/cirrhosis, defined **in the absence of right heart failure or constrictive pericarditis**. It is rare (typically ~0.35–0.8 cases per million per year in Europe) but clinically high impact; most patients have an underlying prothrombotic condition—especially **myeloproliferative neoplasms (MPN)** with **JAK2 V617F**—and contemporary management relies on **anticoagulation plus endovascular restoration/decompression** (angioplasty/stent or TIPS), with transplantation reserved for refractory/advanced disease. (valla2018budd–chiarisyndromehepaticvenous pages 1-2, ollivierhourmand2018theepidemiologyof pages 1-2)

---

## 1. Disease information
### 1.1 Definition and overview (current understanding)
- **Definition:** BCS is **partial or complete impairment/obstruction of hepatic venous drainage/outflow** (from small hepatic venules to the IVC/right atrium), **excluding** obstruction due to right-sided heart failure or constrictive pericarditis. (porrello2023buddchiarisyndromeimaging pages 1-2, valla2018budd–chiarisyndromehepaticvenous pages 1-2)
- **Synonyms / alternative names:**
  - *Hepatic venous outflow tract obstruction* (**HVOTO**) (valla2018budd–chiarisyndromehepaticvenous pages 1-2)
  - *Hepatic vein thrombosis* (commonly used clinically; BCS is a form of hepatic venous thrombosis) (valla2018budd–chiarisyndromehepaticvenous pages 1-2)
- **Classification (etiologic):**
  - **Primary BCS**: obstruction from **thrombosis** (or evolution to fibrotic stenosis) within hepatic veins/IVC. (porrello2023buddchiarisyndromeimaging pages 1-2, valla2018budd–chiarisyndromehepaticvenous pages 1-2)
  - **Secondary BCS**: obstruction from **external compression or tumor invasion/encasement**. (porrello2023buddchiarisyndromeimaging pages 1-2, valla2018budd–chiarisyndromehepaticvenous pages 1-2)

### 1.2 Key identifiers/codes (from retrieved sources)
- **ICD-10:** **I82.0** used for BCS case ascertainment in French national hospital discharge data. (ollivierhourmand2018theepidemiologyof pages 2-3)
- **MeSH / OMIM / Orphanet / MONDO:** Not directly extractable from the retrieved texts in this run; therefore not reported here.

### 1.3 Evidence source type
Most information in this report comes from **aggregated disease-level resources** (systematic reviews, national cohorts, guidelines) plus selected case reports for rarer etiologies and prevention messaging. (porrello2023buddchiarisyndromeimaging pages 1-2, ollivierhourmand2018theepidemiologyof pages 1-2, joueidi2024transjugularintrahepaticportosystemic pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors (mechanistic categories)
- **Core causal mechanism:** hepatic venous outflow obstruction → hepatic sinusoidal congestion → hepatocyte injury/necrosis → fibrosis and portal hypertension. (rossle2024fibrosisprogressionina pages 1-2, porrello2023buddchiarisyndromeimaging pages 1-2)
- **Primary BCS** is predominantly **thrombotic**, driven by systemic or local prothrombotic states. (valla2018budd–chiarisyndromehepaticvenous pages 1-2, valla2018budd–chiarisyndromehepaticvenous pages 2-4)
- **Secondary BCS** results from **invasion/compression** by benign or malignant lesions (rare, reported as <1% in one review). (porrello2023buddchiarisyndromeimaging pages 1-2)

### 2.2 Risk factors (with quantitative data where available)
#### 2.2.1 MPN and somatic mutations (JAK2/CALR/MPL)
- **MPN frequency (France, liver-unit cohort):** MPN in **72/151 (47.7%)**. (ollivierhourmand2018theepidemiologyof pages 3-5)
- **JAK2 V617F frequency (France cohort):** detected in **55/139 tested**. (ollivierhourmand2018theepidemiologyof pages 3-5)
- **Europe vs China heterogeneity (review):** a table in Valla 2018 summarizes markedly higher JAK2-V617F-positive MPN prevalence in European BCS (~40%) than in China (~2%). (valla2018budd–chiarisyndromehepaticvenous pages 2-4)
- **CALR mutations in BCS/PVT (multinational cohort):** CALR mutation **0.7% (1/141)** overall; enriched among JAK2-negative MPN (**1/11; 9.1%**). (plompen2015somaticcalreticulinmutations pages 1-2)
- **Expert synthesis (2024 molecular review):** MPNs are emphasized as major causes of unusual-site thrombosis including BCS, and **JAK2 V617F screening is recommended early** in SVT work-up. (morsia2024exploringthemolecular pages 1-2)

#### 2.2.2 Inherited thrombophilias and APS/PNH/Behçet
- **France (liver units):** factor V Leiden **19/120 (15.8%)**; PNH **8.9%**; Behçet **5.9%**. (ollivierhourmand2018theepidemiologyof pages 5-6, ollivierhourmand2018theepidemiologyof pages 1-2)
- **Valla 2018 (Europe vs China table):** heterozygous factor V Leiden ~20% in Europe vs ~0% in China; antiphospholipid syndrome ~15% Europe vs ~2% China; PNH ~2% Europe vs <1% China. (valla2018budd–chiarisyndromehepaticvenous pages 2-4)
- **Chinese SVT cohort (Fan 2020):** among BCS patients, **MPN 6.3%** (lower than Western cohorts), APS ~7%, and natural anticoagulant deficiencies combined ~22–26%; FVL/prothrombin G20210A/PNH were rare (<1%). (fan2020prevalenceofprothrombotic pages 1-2)

#### 2.2.3 Hormonal and reproductive factors
- **France cohort (women of child-bearing age):** recent oral contraceptive use **36 (35.0%)**. (ollivierhourmand2018theepidemiologyof pages 5-5)
- **Valla 2009 (primary BCS expert review):** explicitly recommends **stopping oral contraceptives and other hormonal therapy** as part of management/risk reduction. (valla2009primarybuddchiarisyndrome. pages 6-7)

#### 2.2.4 Local inflammatory/mechanical factors and secondary causes
- **France discharge database:** among primary BCS incident cases, local factors were prominent in coding (e.g., **38.3% local factors** among those with risk-factor ICD-10 codes), highlighting potential differences between referral-cohort phenotyping and administrative coding. (ollivierhourmand2018theepidemiologyof pages 5-5)
- **Secondary BCS example:** extraluminal compression from a hydatid cyst is described as a rare but fatal cause in an endemic-area case report. (ollivierhourmand2018theepidemiologyof pages 3-5)

### 2.3 Protective factors
No specific **genetic protective variants** were identified in the retrieved texts. Protective/mitigating factors are mainly **treatment-based** (anticoagulation, cytoreduction, restoration of outflow). (magaz2020buddchiarisyndromeanticoagulation pages 1-2, martens2015buddchiarisyndrome pages 5-7)

### 2.4 Gene–environment interactions
BCS frequently reflects **interaction of inherited/acquired thrombophilia with environmental/hormonal exposures**, exemplified by oral contraceptives in patients with clonal MPN thrombophilia (JAK2 V617F) or combined thrombophilic defects. (karns2024a27yearoldfemale pages 1-2, valla2009primarybuddchiarisyndrome. pages 6-7)

---

## 3. Phenotypes
### 3.1 Clinical phenotypes and frequencies
BCS can be acute, subacute/chronic, asymptomatic, or fulminant. (porrello2023buddchiarisyndromeimaging pages 1-2)

**Common presenting features (France 2010 cohort):**
- Ascites **122/164 (74.4%)**
- Hepatomegaly **115/164 (70.1%)**
- Abdominal pain **113/156 (72.4%)**
- Esophageal varices **74/135 (54.8%)**
- Splenomegaly **78/159 (49.1%)**
- Jaundice **27/133 (20.3%)** (ollivierhourmand2018theepidemiologyof pages 2-3)

**From imaging review (Porrello 2023):** ascites 62–85%, hepatomegaly ~67%, pain ~61%, varices ~58%, GI bleeding 5–21%; concomitant portal vein thrombosis ~10–15% (worse prognosis). (porrello2023buddchiarisyndromeimaging pages 2-3)

### 3.2 Laboratory abnormalities
BCS can present with normal liver tests, but AST/ALT can rise markedly in acute/fulminant disease; ascites often has a portal-hypertension pattern (e.g., SAAG ≥1.1 g/dL noted as supportive in one review). (goel2015budd–chiarisyndromeinvestigation pages 1-2)

### 3.3 Complications and quality-of-life impact
- Portal hypertension complications (varices/bleeding, refractory ascites) are major morbidity drivers. (porrello2023buddchiarisyndromeimaging pages 2-3, rossle2023interventionaltreatmentof pages 13-14)
- BCS can cause acute liver failure; a case report notes BCS accounts for **<1% of acute liver failure** presentations. (craciun2024tipswitha pages 1-2)

### 3.4 Suggested HPO terms (examples)
- Ascites — **HP:0001541** (supported by high frequency) (ollivierhourmand2018theepidemiologyof pages 2-3)
- Hepatomegaly — **HP:0002240** (ollivierhourmand2018theepidemiologyof pages 2-3)
- Abdominal pain — **HP:0002027** (ollivierhourmand2018theepidemiologyof pages 2-3)
- Esophageal varices — **HP:0002040** (ollivierhourmand2018theepidemiologyof pages 2-3)
- Splenomegaly — **HP:0001744** (ollivierhourmand2018theepidemiologyof pages 2-3)
- Jaundice — **HP:0000952** (ollivierhourmand2018theepidemiologyof pages 2-3)
- Portal hypertension — **HP:0002579** (porrello2023buddchiarisyndromeimaging pages 2-3)
- Hepatic vein thrombosis — **HP:0012372** (concept supported by HV outflow obstruction definition) (valla2018budd–chiarisyndromehepaticvenous pages 1-2)

---

## 4. Genetic / molecular information
### 4.1 Causal genes (risk/etiology genes rather than single-gene “causal disease”)
BCS is not classically monogenic; it is a **complex thrombotic phenotype** with strong association to clonal hematopoiesis and thrombophilia genes.

Key genes/molecular drivers in relevant etiologies:
- **JAK2** (somatic **V617F** mutation) in MPN-associated BCS (ollivierhourmand2018theepidemiologyof pages 3-5, valla2018budd–chiarisyndromehepaticvenous pages 2-4)
- **CALR** (somatic frameshift mutations) uncommon but present in a minority of JAK2-negative MPN-SVT (plompen2015somaticcalreticulinmutations pages 1-2)
- **MPL** (MPN driver; mentioned as relevant in BCS work-up) (valla2018budd–chiarisyndromehepaticvenous pages 2-4)

### 4.2 Pathogenic variants / prothrombotic variants
- **Factor V Leiden (F5)**: 12–31% reported in European cohorts; table summary ~20%. (valla2018budd–chiarisyndromehepaticvenous pages 2-4)
- **Prothrombin G20210A (F2)**: table ~7% Europe vs 0% China. (valla2018budd–chiarisyndromehepaticvenous pages 2-4)
- **Antiphospholipid syndrome**: ~15% in Europe (table). (valla2018budd–chiarisyndromehepaticvenous pages 2-4)

Variant-level nomenclature and allele frequencies in population databases (gnomAD) were not available in retrieved sources.

### 4.3 Somatic vs germline
- MPN drivers (JAK2, CALR, MPL) are **somatic** in the hematopoietic compartment; inherited thrombophilias (F5 Leiden, F2 G20210A) are **germline**. (plompen2015somaticcalreticulinmutations pages 1-2, valla2018budd–chiarisyndromehepaticvenous pages 2-4)

---

## 5. Environmental information
Environmental/lifestyle triggers are primarily **hormonal exposure** (estrogen-containing oral contraceptives) and pregnancy/puerperium as prothrombotic states. (ollivierhourmand2018theepidemiologyof pages 5-5, valla2009primarybuddchiarisyndrome. pages 6-7)

Infectious agents are not typical primary causes, but secondary BCS can arise from space-occupying lesions (e.g., hydatid cyst) in endemic areas. (ollivierhourmand2018theepidemiologyof pages 3-5)

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain
1) **Trigger:** systemic thrombophilia (e.g., MPN/JAK2, APS, inherited thrombophilia) or secondary compression/invasion. (valla2018budd–chiarisyndromehepaticvenous pages 2-4, porrello2023buddchiarisyndromeimaging pages 1-2)
2) **Vascular event:** hepatic vein/IVC obstruction and thrombosis. (valla2018budd–chiarisyndromehepaticvenous pages 1-2)
3) **Hemodynamic consequence:** sinusoidal congestion and increased sinusoidal pressure → portal hypertension and collateral formation. (porrello2023buddchiarisyndromeimaging pages 1-2, rossle2024fibrosisprogressionina pages 1-2)
4) **Tissue injury:** congestion-related hepatocyte hypoxia/necrosis; evolving fibrosis/cirrhosis; regenerative nodules. (rossle2024fibrosisprogressionina pages 1-2, porrello2023buddchiarisyndromeimaging pages 3-5)
5) **Clinical manifestations:** ascites, hepatomegaly, pain, varices/bleeding; in severe cases acute liver failure. (ollivierhourmand2018theepidemiologyof pages 2-3, craciun2024tipswitha pages 1-2)

### 6.2 Molecular/cellular processes (suggested GO / CL)
- **GO biological processes (suggested):**
  - blood coagulation (GO:0007596)
  - platelet activation (GO:0030168)
  - inflammatory response (GO:0006954)
  - response to hypoxia (GO:0001666)
  - extracellular matrix organization / fibrosis (GO:0030198)
- **Cell types (CL suggestions):**
  - vascular endothelial cell (CL:0000115)
  - hepatocyte (CL:0000182)
  - hepatic stellate cell (CL:0000632)
  - megakaryocyte (CL:0000554) / myeloid lineage cells relevant to MPN (valla2018budd–chiarisyndromehepaticvenous pages 2-4)

### 6.3 Epigenetics / multi-omics
No BCS-specific epigenomic or multi-omic signatures were available in the retrieved evidence set.

---

## 7. Anatomical structures affected
- **Primary anatomical site:** hepatic veins and/or suprahepatic IVC (hepatic venous outflow tract). (valla2018budd–chiarisyndromehepaticvenous pages 1-2)
- **Secondary consequences:** liver parenchyma (congestion, necrosis, fibrosis), portal venous system (portal hypertension, collaterals), spleen (congestive splenomegaly). (ollivierhourmand2018theepidemiologyof pages 2-3, porrello2023buddchiarisyndromeimaging pages 2-3)

**Suggested UBERON terms (examples):**
- Liver — UBERON:0002107
- Hepatic vein — UBERON:0001638
- Inferior vena cava — UBERON:0001072
- Portal vein — UBERON:0001616

---

## 8. Temporal development
- **Onset:** may be acute, subacute, chronic, or fulminant; chronic/subacute is most common. (porrello2023buddchiarisyndromeimaging pages 1-2)
- **Progression:** congestion can progress to fibrosis/cirrhosis early; in a TIPS-followed cohort most patients had liver stiffness >12 kPa years after diagnosis, suggesting advanced fibrosis commonly persists. (rossle2024fibrosisprogressionina pages 1-2)

---

## 9. Inheritance and population
### 9.1 Epidemiology (quantitative)
- **Europe incidence:** ~0.35–0.8 per million per year (review). (valla2018budd–chiarisyndromehepaticvenous pages 1-2)
- **France national liver-unit survey (2010):** prevalence **4.04 per million**, incidence **0.68 per million/year** for primary BCS; primary BCS female predominance **68.1%**, mean age at diagnosis **40.2 ± 13.9**. (ollivierhourmand2018theepidemiologyof pages 1-2, ollivierhourmand2018theepidemiologyof pages 2-3)
- **France discharge database (2012):** incidence **2.17 per million/year** for primary BCS (higher than liver-unit estimate). (ollivierhourmand2018theepidemiologyof pages 1-2)

### 9.2 Demographics
- Imaging review notes BCS “most commonly affects women aged 19–49”. (porrello2023buddchiarisyndromeimaging pages 1-2)

### 9.3 Inheritance patterns
BCS itself is not inherited as a Mendelian disorder; predisposition can arise from **germline thrombophilia variants** and acquired somatic MPN mutations. (valla2018budd–chiarisyndromehepaticvenous pages 2-4, plompen2015somaticcalreticulinmutations pages 1-2)

---

## 10. Diagnostics
### 10.1 Diagnostic principle
Diagnosis requires **radiologic demonstration** of hepatic venous outflow obstruction (noninvasive first-line), with biopsy reserved for uncertain/small-vessel disease. (porrello2023buddchiarisyndromeimaging pages 3-5, porrello2023buddchiarisyndromeimaging pages 2-3)

### 10.2 Imaging tests and performance
- **First-line:** Color Doppler ultrasound (CDUS). (porrello2023buddchiarisyndromeimaging pages 3-5)
  - Pooled CDUS sensitivity/specificity reported as **89%/68%** (meta-analysis cited in Porrello 2023). (porrello2023buddchiarisyndromeimaging pages 3-5)
  - APASL consensus reports Doppler US **87.5%/85%** and CT venography **86.1%/97.3%** (as summarized). (shukla2021buddchiarisyndromeconsensus pages 5-6)
- **CT / MRI:** used to confirm diagnosis, map extent, characterize nodules, and plan intervention.
  - Meta-analysis summary: CT **89%/72%**, MRI **93%/55%** sensitivity/specificity. (porrello2023buddchiarisyndromeimaging pages 5-8)

### 10.3 Key imaging signs (with frequencies)
From Porrello 2023 (frequencies across studies):
- Splenomegaly **78%**
- Inhomogeneous parenchyma **76%**
- Intrahepatic collaterals **73%**
- Caudate hypertrophy **67%**
- Ascites **56%**
- Extrahepatic collaterals **44%** (porrello2023buddchiarisyndromeimaging pages 3-5)

Specificity note: **a direct US sign plus caudate lobe hypertrophy** reported as **100% specificity** for BCS. (porrello2023buddchiarisyndromeimaging pages 3-5)

### 10.4 Biopsy / histopathology
- Liver biopsy is indicated in inconclusive/discordant cases or suspected small hepatic vein involvement. (porrello2023buddchiarisyndromeimaging pages 3-5)
- Biopsy findings include centrilobular hemorrhage/necrosis and sinusoidal dilatation; sampling variation limits prognostication. (goel2015budd–chiarisyndromeinvestigation pages 1-2, elkilany2022percutaneoustransluminalangioplasty pages 12-13)

### 10.5 Differential diagnosis
BCS needs differentiation from sinusoidal obstruction syndrome and cardiac/pericardial causes of hepatic congestion. (porrello2023buddchiarisyndromeimaging pages 1-2, ollivierhourmand2018theepidemiologyof pages 2-3)

---

## 11. Outcome / prognosis
### 11.1 Untreated natural history
Natural history is poor; multiple sources emphasize high mortality without treatment (e.g., case series and reviews cite very low long-term survival), but exact untreated survival statistics were not extractable from the retrieved evidence excerpts in this run. One 2024 cohort paper reiterates that untreated BCS has very poor prognosis and cites historical estimates (50% mortality at 2 years; <10% survival at 3 years) within its discussion. (joueidi2024transjugularintrahepaticportosystemic pages 1-2)

### 11.2 Survival with modern therapy
- **Interventional management review:** reported **5- and 10-year survival ~90% and 80%** with contemporary interventional strategies (angioplasty/stent/TIPS) and low complication rates. (rossle2023interventionaltreatmentof pages 1-2)
- **Covered-stent TIPS cohort (single center, 2010–2022; n=70 TIPS):** survival at **1, 3, 5 years: 98.8%, 97.9%, 97.7%**. (joueidi2024transjugularintrahepaticportosystemic pages 1-2)

### 11.3 Prognostic scores (examples of performance)
From a 2022 review summarizing published cutoffs:
- Rotterdam 5-year survival: Class I **89%**, Class II **74%**, Class III **42%**. (gavriilidis2022stateofthe pages 3-5)
- BCS-TIPSS 1-year OLT-free survival: score **<7: 95%** vs **>7: 12%**. (gavriilidis2022stateofthe pages 3-5)

---

## 12. Treatment
### 12.1 Core strategy (stepwise algorithm)
A widely endorsed approach: **anticoagulation and management of underlying thrombophilia → endovascular recanalization (angioplasty ± stent) for short lesions → TIPS for decompression if needed → liver transplantation for refractory/advanced disease**. (rossle2023interventionaltreatmentof pages 1-2, mukhiya2023survivalandclinical pages 1-2)

**Visual evidence (treatment algorithm):** (rossle2023interventionaltreatmentof media 5657bdfb)

### 12.2 Pharmacotherapy
- **Anticoagulation:** recommended for essentially all patients; LMWH initiation and VKA (INR 2–3) are commonly used. (martens2015buddchiarisyndrome pages 5-7, valla2009primarybuddchiarisyndrome. pages 6-7)
- **DOACs:** emerging/used in practice for splanchnic thrombosis, but BCS-specific evidence is limited; not formally approved and caution in APS. (magaz2020buddchiarisyndromeanticoagulation pages 1-2, monaco2023directoralanticoagulants pages 13-14)

### 12.3 Endovascular and interventional procedures (real-world outcomes)
- **Angioplasty ± stent (short webs/stenoses):** technical success >90%; routine primary stenting reduces restenosis (2% with stent vs 40% without; 3-yr restenosis-free survival 96% vs 60.4%). (rossle2023interventionaltreatmentof pages 1-2)
- **TIPS:** successful in ~95% of patients in experienced hands; PTFE-covered stents improved long-term patency; reported 5- and 10-year survival ~90% and 80% in an interventional review. (rossle2023interventionaltreatmentof pages 1-2)

### 12.4 Liver transplantation
Reserved for patients who fail/are not candidates for durable endovascular therapy, or with progressive failure/HCC. Post-transplant recurrence of hepatic vein thrombosis can approach ~20% without adequate long-term anticoagulation. (magaz2020buddchiarisyndromeanticoagulation pages 4-5)

### 12.5 Suggested MAXO terms (examples)
- Anticoagulant therapy — **MAXO:0000747** (concept)
- Percutaneous transluminal angioplasty — **MAXO:0001113** (concept)
- Vascular stent placement — **MAXO:0000958** (concept)
- Transjugular intrahepatic portosystemic shunt — **MAXO:0000610** (concept)
- Liver transplantation — **MAXO:0001116** (concept)

(These MAXO IDs are suggested mappings; not provided in the retrieved texts.)

---

## 13. Prevention
### 13.1 Primary prevention (risk-factor modification)
- **Avoid estrogen-containing oral contraceptives/hormonal therapy** in at-risk patients; Valla 2009 explicitly recommends stopping oral contraceptives and hormonal therapy in primary BCS management, and a 2024 case report highlights combined OCPs as contraindicated in JAK2-mutated MPN patients due to thrombosis risk. (valla2009primarybuddchiarisyndrome. pages 6-7, karns2024a27yearoldfemale pages 1-2)
- **MPN thrombosis prevention:** cytoreduction and disease control; one review notes in PV targeting hematocrit <45% reduces major thrombosis risk (evidence imported from PV trials). (magaz2020buddchiarisyndromeanticoagulation pages 1-2)

### 13.2 Secondary prevention (prevent recurrence/extension)
- **Prompt, often lifelong anticoagulation** when prothrombotic risk cannot be corrected; LMWH then VKA (INR 2–3) is common practice. (martens2015buddchiarisyndrome pages 5-7, valla2009primarybuddchiarisyndrome. pages 6-7)
- **Variceal screening/prophylaxis** before/while anticoagulated to reduce bleeding risk. (khan2019reviewarticlea pages 10-11)

### 13.3 Tertiary prevention (prevent complications)
- **Early endovascular restoration/decompression** to control portal hypertension, preserve liver function, and reduce complications. (rossle2023interventionaltreatmentof pages 13-14, rossle2023interventionaltreatmentof pages 1-2)

Protective factors beyond these clinical interventions were not identified.

---

## 14. Other species / natural disease
Naturally occurring BCS-like hepatic venous outflow obstruction is reported in veterinary contexts:
- **Dogs:** endovascular stent use in three dogs with Budd–Chiari syndrome is reported in the veterinary literature. ()

---

## 15. Model organisms
Experimental models exist to study hepatic venous outflow obstruction and mechanisms:
- **Rat model:** BCS model via partial ligation of the IVC with biochemical measures of hypoxia/oxidative stress changes over time. ()
- **Canine model:** diffuse hepatic vein obstruction via endovascular occlusion to mimic human BCS. ()

---

## Recent developments (2023–2024 prioritized)
1) **Imaging synthesis and meta-analytic performance estimates:** Porrello 2023 provides pooled sensitivity/specificity estimates and sign frequencies and highlights the centrality of radiology for diagnosis and surveillance. (Published 2023-07; https://doi.org/10.3390/diagnostics13132256) (porrello2023buddchiarisyndromeimaging pages 3-5, porrello2023buddchiarisyndromeimaging pages 5-8)
2) **Interventional outcomes and debate on early intervention:** Rössle 2023 argues the conventional step-up algorithm may be “unproven” and supports earlier angioplasty/TIPS, backed by high technical success and survival estimates and the impact of covered stents on patency. (Published 2023-04; https://doi.org/10.3390/diagnostics13081458) (rossle2023interventionaltreatmentof pages 1-2, rossle2023interventionaltreatmentof pages 13-14)
3) **Real-world covered-stent TIPS outcomes:** A 2024 single-center cohort reports very high 5-year survival (~97.7%) after covered-stent TIPS. (Published 2024-10; https://doi.org/10.3390/jcm13195858) (joueidi2024transjugularintrahepaticportosystemic pages 1-2)
4) **Long-term fibrosis tracking after TIPS:** 2024 transient elastography follow-up suggests fibrosis is often advanced and may develop early; timing of TIPS did not change stiffness trajectories in that cohort. (Published 2024-02; https://doi.org/10.3390/diagnostics14030344) (rossle2024fibrosisprogressionina pages 1-2)

---

## Current applications and real-world implementation
BCS care is typically concentrated in referral centers that can deliver: (i) rapid imaging confirmation, (ii) multidisciplinary thrombophilia/MPN work-up, (iii) anticoagulation with variceal prophylaxis, and (iv) endovascular expertise for recanalization and TIPS, with transplant backup. (porrello2023buddchiarisyndromeimaging pages 3-5, magaz2020buddchiarisyndromeanticoagulation pages 4-5)

---

## Clinical trials and registries (ClinicalTrials.gov)
- **NCT06960473 (2025; not yet recruiting):** randomized trial IVUS-guided vs DSA-guided intervention; n=260; primary endpoint restenosis at 1–12 months. (NCT06960473 chunk 1)
- **NCT02201485 (2014; completed):** randomized PTA alone vs PTA+stent; n=88; primary endpoint reocclusion over 2 years; secondary endpoints survival/complications/symptom recurrence. (NCT02201485 chunk 1)
- **NCT05117684 (2021; completed):** retrospective comparison of balloon-occluded thrombolysis vs conventional catheter thrombolysis for occluded DIPSS stents; n=33; endpoints include re-stenting, thrombolytic dose, patency at 1 month. (NCT05117684 chunk 1)
- **NCT05123326 (2021; recruiting):** prospective global coagulation assessment in PVT and BCS/HVOTO including genetic testing (JAK2, CALR, FVL) and outcomes up to 3 years. (NCT05123326 chunk 2)
- **NCT03541057 (VALID registry; Vienna):** prospective observational cohort/biobank including BCS; target ~200; primary endpoint time to first hepatic decompensation. (NCT03541057 chunk 1)

---

## Limitations and gaps
- Ontology identifiers (MONDO, Orphanet, MeSH IDs) were not captured in the retrieved sources, so this report cannot provide verified values.
- Several key “landmark” outcome papers (e.g., Murad et al. Ann Intern Med 2009) were retrieved but not fully mined here for untreated vs treated survival due to time constraints; however, multiple independent sources in this evidence set provide quantitative modern survival and prognostic score performance. (gavriilidis2022stateofthe pages 3-5, rossle2023interventionaltreatmentof pages 1-2)

---

## URLs and publication dates (selected key sources)
- Porrello et al. *Diagnostics* — 2023-07 — https://doi.org/10.3390/diagnostics13132256 (porrello2023buddchiarisyndromeimaging pages 1-2)
- Rössle. *Diagnostics* — 2023-04 — https://doi.org/10.3390/diagnostics13081458 (rossle2023interventionaltreatmentof pages 1-2)
- Joueidi et al. *J Clin Med* — 2024-10 — https://doi.org/10.3390/jcm13195858 (joueidi2024transjugularintrahepaticportosystemic pages 1-2)
- Rössle et al. *Diagnostics* — 2024-02 — https://doi.org/10.3390/diagnostics14030344 (rossle2024fibrosisprogressionina pages 1-2)
- Ollivier-Hourmand et al. *Dig Liver Dis* — 2018-09 — https://doi.org/10.1016/j.dld.2018.04.004 (ollivierhourmand2018theepidemiologyof pages 1-2)
- Valla. *Hepatology International* — 2018-02 — https://doi.org/10.1007/s12072-017-9810-5 (valla2018budd–chiarisyndromehepaticvenous pages 1-2)



References

1. (valla2018budd–chiarisyndromehepaticvenous pages 1-2): Dominique-Charles Valla. Budd–chiari syndrome/hepatic venous outflow tract obstruction. Hepatology International, 12:168-180, Feb 2018. URL: https://doi.org/10.1007/s12072-017-9810-5, doi:10.1007/s12072-017-9810-5. This article has 172 citations and is from a peer-reviewed journal.

2. (ollivierhourmand2018theepidemiologyof pages 1-2): Isabelle Ollivier-Hourmand, Manon Allaire, Nathalie Goutte, Rémy Morello, Carine Chagneau-Derrode, Odile Goria, Jerôme Dumortier, Jean Paul Cervoni, Sébastien Dharancy, Nathalie Ganne-Carrié, Christophe Bureau, Nicolas Carbonell, Armand Abergel, Jean Baptiste Nousbaum, Rodolphe Anty, Hélène Barraud, Marie Pierre Ripault, Victor De Ledinghen, Anne Minello, Frédéric Oberti, Sylvie Radenne, Noelle Bendersky, Olivier Farges, Isabelle Archambeaud, Anne Guillygomarc’h, Marie Ecochard, Violaine Ozenne, Marie Noelle Hilleret, Eric Nguyen-Khac, Barbara Dauvois, Jean Marc Perarnau, Pascale Lefilliatre, Jean Jacques Raabe, Michel Doffoel, Jean Philippe Becquart, Eric Saillard, Dominique Valla, Thong Dao, and Aurélie Plessier. The epidemiology of budd-chiari syndrome in france. Digestive and liver disease : official journal of the Italian Society of Gastroenterology and the Italian Association for the Study of the Liver, 50 9:931-937, Sep 2018. URL: https://doi.org/10.1016/j.dld.2018.04.004, doi:10.1016/j.dld.2018.04.004. This article has 63 citations.

3. (porrello2023buddchiarisyndromeimaging pages 1-2): Giorgia Porrello, Giuseppe Mamone, and Roberto Miraglia. Budd-chiari syndrome imaging diagnosis: state of the art and future perspectives. Diagnostics, 13:2256, Jul 2023. URL: https://doi.org/10.3390/diagnostics13132256, doi:10.3390/diagnostics13132256. This article has 35 citations.

4. (ollivierhourmand2018theepidemiologyof pages 2-3): Isabelle Ollivier-Hourmand, Manon Allaire, Nathalie Goutte, Rémy Morello, Carine Chagneau-Derrode, Odile Goria, Jerôme Dumortier, Jean Paul Cervoni, Sébastien Dharancy, Nathalie Ganne-Carrié, Christophe Bureau, Nicolas Carbonell, Armand Abergel, Jean Baptiste Nousbaum, Rodolphe Anty, Hélène Barraud, Marie Pierre Ripault, Victor De Ledinghen, Anne Minello, Frédéric Oberti, Sylvie Radenne, Noelle Bendersky, Olivier Farges, Isabelle Archambeaud, Anne Guillygomarc’h, Marie Ecochard, Violaine Ozenne, Marie Noelle Hilleret, Eric Nguyen-Khac, Barbara Dauvois, Jean Marc Perarnau, Pascale Lefilliatre, Jean Jacques Raabe, Michel Doffoel, Jean Philippe Becquart, Eric Saillard, Dominique Valla, Thong Dao, and Aurélie Plessier. The epidemiology of budd-chiari syndrome in france. Digestive and liver disease : official journal of the Italian Society of Gastroenterology and the Italian Association for the Study of the Liver, 50 9:931-937, Sep 2018. URL: https://doi.org/10.1016/j.dld.2018.04.004, doi:10.1016/j.dld.2018.04.004. This article has 63 citations.

5. (joueidi2024transjugularintrahepaticportosystemic pages 1-2): Faisal Joueidi, Amnah Alhanaee, Hamad Alsuhaibani, Ali Albenmousa, Ahmad Joueidi, Ahmed Elhassan, Abdallah Nabeel Nasir, Kris Ann Hervera Marquez, Saad Alghamdi, Waleed Al Hamoudi, Saad Abualganam, Dieter Broering, and Khalid Ibrahim Bzeizi. Transjugular intrahepatic portosystemic shunt for budd–chiari syndrome: a single-centre experience. Journal of Clinical Medicine, 13:5858, Oct 2024. URL: https://doi.org/10.3390/jcm13195858, doi:10.3390/jcm13195858. This article has 0 citations.

6. (rossle2024fibrosisprogressionina pages 1-2): Martin Rössle, Dominik Bettinger, Lukas Sturm, Marlene Reincke, Robert Thimme, and Michael Schultheiss. Fibrosis progression in patients with budd–chiari syndrome and transjugular intrahepatic portosystemic shunt (tips): a long-term study using transient elastography. Diagnostics, 14:344, Feb 2024. URL: https://doi.org/10.3390/diagnostics14030344, doi:10.3390/diagnostics14030344. This article has 3 citations.

7. (valla2018budd–chiarisyndromehepaticvenous pages 2-4): Dominique-Charles Valla. Budd–chiari syndrome/hepatic venous outflow tract obstruction. Hepatology International, 12:168-180, Feb 2018. URL: https://doi.org/10.1007/s12072-017-9810-5, doi:10.1007/s12072-017-9810-5. This article has 172 citations and is from a peer-reviewed journal.

8. (ollivierhourmand2018theepidemiologyof pages 3-5): Isabelle Ollivier-Hourmand, Manon Allaire, Nathalie Goutte, Rémy Morello, Carine Chagneau-Derrode, Odile Goria, Jerôme Dumortier, Jean Paul Cervoni, Sébastien Dharancy, Nathalie Ganne-Carrié, Christophe Bureau, Nicolas Carbonell, Armand Abergel, Jean Baptiste Nousbaum, Rodolphe Anty, Hélène Barraud, Marie Pierre Ripault, Victor De Ledinghen, Anne Minello, Frédéric Oberti, Sylvie Radenne, Noelle Bendersky, Olivier Farges, Isabelle Archambeaud, Anne Guillygomarc’h, Marie Ecochard, Violaine Ozenne, Marie Noelle Hilleret, Eric Nguyen-Khac, Barbara Dauvois, Jean Marc Perarnau, Pascale Lefilliatre, Jean Jacques Raabe, Michel Doffoel, Jean Philippe Becquart, Eric Saillard, Dominique Valla, Thong Dao, and Aurélie Plessier. The epidemiology of budd-chiari syndrome in france. Digestive and liver disease : official journal of the Italian Society of Gastroenterology and the Italian Association for the Study of the Liver, 50 9:931-937, Sep 2018. URL: https://doi.org/10.1016/j.dld.2018.04.004, doi:10.1016/j.dld.2018.04.004. This article has 63 citations.

9. (plompen2015somaticcalreticulinmutations pages 1-2): E. P. C. Plompen, P. J. M. Valk, I. Chu, S. D. Murad, A. Plessier, F. Turon, J. Trebicka, M. Primignani, J. C. Garcia-Pagan, D. C. Valla, H. L. A. Janssen, and F. W. G. Leebeek. Somatic calreticulin mutations in patients with budd-chiari syndrome and portal vein thrombosis. Haematologica, 100:e226-e228, Feb 2015. URL: https://doi.org/10.3324/haematol.2014.120857, doi:10.3324/haematol.2014.120857. This article has 60 citations.

10. (morsia2024exploringthemolecular pages 1-2): Erika Morsia, Elena Torre, Francesco Martini, Sonia Morè, Antonella Poloni, Attilio Olivieri, and Serena Rupoli. Exploring the molecular aspects of myeloproliferative neoplasms associated with unusual site vein thrombosis: review of the literature and latest insights. International Journal of Molecular Sciences, 25:1524, Jan 2024. URL: https://doi.org/10.3390/ijms25031524, doi:10.3390/ijms25031524. This article has 9 citations.

11. (ollivierhourmand2018theepidemiologyof pages 5-6): Isabelle Ollivier-Hourmand, Manon Allaire, Nathalie Goutte, Rémy Morello, Carine Chagneau-Derrode, Odile Goria, Jerôme Dumortier, Jean Paul Cervoni, Sébastien Dharancy, Nathalie Ganne-Carrié, Christophe Bureau, Nicolas Carbonell, Armand Abergel, Jean Baptiste Nousbaum, Rodolphe Anty, Hélène Barraud, Marie Pierre Ripault, Victor De Ledinghen, Anne Minello, Frédéric Oberti, Sylvie Radenne, Noelle Bendersky, Olivier Farges, Isabelle Archambeaud, Anne Guillygomarc’h, Marie Ecochard, Violaine Ozenne, Marie Noelle Hilleret, Eric Nguyen-Khac, Barbara Dauvois, Jean Marc Perarnau, Pascale Lefilliatre, Jean Jacques Raabe, Michel Doffoel, Jean Philippe Becquart, Eric Saillard, Dominique Valla, Thong Dao, and Aurélie Plessier. The epidemiology of budd-chiari syndrome in france. Digestive and liver disease : official journal of the Italian Society of Gastroenterology and the Italian Association for the Study of the Liver, 50 9:931-937, Sep 2018. URL: https://doi.org/10.1016/j.dld.2018.04.004, doi:10.1016/j.dld.2018.04.004. This article has 63 citations.

12. (fan2020prevalenceofprothrombotic pages 1-2): Jiahao Fan, Qiuhe Wang, Bohan Luo, Hui Chen, Zhengyu Wang, Jing Niu, Jie Yuan, Xulong Yuan, Wei Bai, Chuangye He, Wengang Guo, Kai Li, Zhanxin Yin, Daiming Fan, and Guohong Han. Prevalence of prothrombotic factors in patients with budd–chiari syndrome or non‐cirrhotic nonmalignant portal vein thrombosis: a hospital‐based observational study. Journal of Gastroenterology and Hepatology, 35:1215-1222, Dec 2020. URL: https://doi.org/10.1111/jgh.14925, doi:10.1111/jgh.14925. This article has 28 citations and is from a peer-reviewed journal.

13. (ollivierhourmand2018theepidemiologyof pages 5-5): Isabelle Ollivier-Hourmand, Manon Allaire, Nathalie Goutte, Rémy Morello, Carine Chagneau-Derrode, Odile Goria, Jerôme Dumortier, Jean Paul Cervoni, Sébastien Dharancy, Nathalie Ganne-Carrié, Christophe Bureau, Nicolas Carbonell, Armand Abergel, Jean Baptiste Nousbaum, Rodolphe Anty, Hélène Barraud, Marie Pierre Ripault, Victor De Ledinghen, Anne Minello, Frédéric Oberti, Sylvie Radenne, Noelle Bendersky, Olivier Farges, Isabelle Archambeaud, Anne Guillygomarc’h, Marie Ecochard, Violaine Ozenne, Marie Noelle Hilleret, Eric Nguyen-Khac, Barbara Dauvois, Jean Marc Perarnau, Pascale Lefilliatre, Jean Jacques Raabe, Michel Doffoel, Jean Philippe Becquart, Eric Saillard, Dominique Valla, Thong Dao, and Aurélie Plessier. The epidemiology of budd-chiari syndrome in france. Digestive and liver disease : official journal of the Italian Society of Gastroenterology and the Italian Association for the Study of the Liver, 50 9:931-937, Sep 2018. URL: https://doi.org/10.1016/j.dld.2018.04.004, doi:10.1016/j.dld.2018.04.004. This article has 63 citations.

14. (valla2009primarybuddchiarisyndrome. pages 6-7): Dominique-Charles Valla. Primary budd-chiari syndrome. Journal of hepatology, 50 1:195-203, Jan 2009. URL: https://doi.org/10.1016/j.jhep.2008.10.007, doi:10.1016/j.jhep.2008.10.007. This article has 456 citations and is from a highest quality peer-reviewed journal.

15. (magaz2020buddchiarisyndromeanticoagulation pages 1-2): Marta Magaz, Guillem Soy, and Juan Carlos García-Pagán. Budd-chiari syndrome: anticoagulation, tips, or transplant. Current Hepatology Reports, pages 1-6, Jun 2020. URL: https://doi.org/10.1007/s11901-020-00528-8, doi:10.1007/s11901-020-00528-8. This article has 4 citations.

16. (martens2015buddchiarisyndrome pages 5-7): Pieter Martens and Frederik Nevens. Budd-chiari syndrome. United European Gastroenterology Journal, 3:489-500, Dec 2015. URL: https://doi.org/10.1177/2050640615582293, doi:10.1177/2050640615582293. This article has 102 citations and is from a peer-reviewed journal.

17. (karns2024a27yearoldfemale pages 1-2): John P. Karns, An Nguyen, Nikita Wong, Aisha True-Malhotra, Dennis Smythe, and Raghavendra C Vemulapalli. A 27-year-old female with jak2 mutation: a case of budd-chiari syndrome secondary to prolonged oral contraceptive pill use. Cureus, Jul 2024. URL: https://doi.org/10.7759/cureus.64858, doi:10.7759/cureus.64858. This article has 0 citations.

18. (porrello2023buddchiarisyndromeimaging pages 2-3): Giorgia Porrello, Giuseppe Mamone, and Roberto Miraglia. Budd-chiari syndrome imaging diagnosis: state of the art and future perspectives. Diagnostics, 13:2256, Jul 2023. URL: https://doi.org/10.3390/diagnostics13132256, doi:10.3390/diagnostics13132256. This article has 35 citations.

19. (goel2015budd–chiarisyndromeinvestigation pages 1-2): Rishi M Goel, Emma L Johnston, Kamal V Patel, and Terence Wong. Budd–chiari syndrome: investigation, treatment and outcomes. Postgraduate Medical Journal, 91:692-697, Oct 2015. URL: https://doi.org/10.1136/postgradmedj-2015-133402, doi:10.1136/postgradmedj-2015-133402. This article has 54 citations and is from a peer-reviewed journal.

20. (rossle2023interventionaltreatmentof pages 13-14): Martin Rössle. Interventional treatment of budd–chiari syndrome. Diagnostics, 13:1458, Apr 2023. URL: https://doi.org/10.3390/diagnostics13081458, doi:10.3390/diagnostics13081458. This article has 15 citations.

21. (craciun2024tipswitha pages 1-2): Rares Craciun, Romeo Chira, Andrada Nemes, Horia Stefanescu, Simona Cocu, and Bogdan Procopet. Tips with a twist � the real life management of a case of budd-chiarirelated acute liver and subsequent multiple organ failure. Current Medical Imaging Formerly Current Medical Imaging Reviews, Oct 2024. URL: https://doi.org/10.2174/1573405620666230908111803, doi:10.2174/1573405620666230908111803. This article has 1 citations.

22. (porrello2023buddchiarisyndromeimaging pages 3-5): Giorgia Porrello, Giuseppe Mamone, and Roberto Miraglia. Budd-chiari syndrome imaging diagnosis: state of the art and future perspectives. Diagnostics, 13:2256, Jul 2023. URL: https://doi.org/10.3390/diagnostics13132256, doi:10.3390/diagnostics13132256. This article has 35 citations.

23. (shukla2021buddchiarisyndromeconsensus pages 5-6): Akash Shukla, Ananta Shreshtha, Amar Mukund, Chhagan Bihari, C. E. Eapen, Guohong Han, Hemant Deshmukh, Ian Homer Y. Cua, Cosmas Rinaldi Adithya Lesmana, Mamun Al Meshtab, Masayoshi Kage, Roongruedee Chaiteeraki, Sombat Treeprasertsuk, Suprabhat Giri, Sundeep Punamiya, Valerie Paradis, Xingshun Qi, Yasuhiko Sugawara, Zaigham Abbas, and Shiv Kumar Sarin. Budd-chiari syndrome: consensus guidance of the asian pacific association for the study of the liver (apasl). Hepatology International, 15:531-567, Jun 2021. URL: https://doi.org/10.1007/s12072-021-10189-4, doi:10.1007/s12072-021-10189-4. This article has 116 citations and is from a peer-reviewed journal.

24. (porrello2023buddchiarisyndromeimaging pages 5-8): Giorgia Porrello, Giuseppe Mamone, and Roberto Miraglia. Budd-chiari syndrome imaging diagnosis: state of the art and future perspectives. Diagnostics, 13:2256, Jul 2023. URL: https://doi.org/10.3390/diagnostics13132256, doi:10.3390/diagnostics13132256. This article has 35 citations.

25. (elkilany2022percutaneoustransluminalangioplasty pages 12-13): Aboelyazid Elkilany, Mohamed Alwarraky, Timm Denecke, and Dominik Geisel. Percutaneous transluminal angioplasty for symptomatic hepatic vein-type budd-chiari syndrome: feasibility and long-term outcomes. Scientific Reports, Aug 2022. URL: https://doi.org/10.1038/s41598-022-16818-8, doi:10.1038/s41598-022-16818-8. This article has 2 citations and is from a peer-reviewed journal.

26. (rossle2023interventionaltreatmentof pages 1-2): Martin Rössle. Interventional treatment of budd–chiari syndrome. Diagnostics, 13:1458, Apr 2023. URL: https://doi.org/10.3390/diagnostics13081458, doi:10.3390/diagnostics13081458. This article has 15 citations.

27. (gavriilidis2022stateofthe pages 3-5): Paschalis Gavriilidis, Gabriele Marangoni, Jawad Ahmad, and Daniel Azoulay. State of the art, current perspectives, and controversies of budd-chiari syndrome: a review. Journal of Clinical Medicine Research, 14:147-157, Apr 2022. URL: https://doi.org/10.14740/jocmr4724, doi:10.14740/jocmr4724. This article has 38 citations.

28. (mukhiya2023survivalandclinical pages 1-2): Gauri Mukhiya, Dechao Jiao, Xinwei Han, Xueliang Zhou, and Gaurab Pokhrel. Survival and clinical success of endovascular intervention in patients with budd-chiari syndrome: a systematic review. Journal of Clinical Imaging Science, 13:5, Jan 2023. URL: https://doi.org/10.25259/jcis\_130\_2022, doi:10.25259/jcis\_130\_2022. This article has 9 citations.

29. (rossle2023interventionaltreatmentof media 5657bdfb): Martin Rössle. Interventional treatment of budd–chiari syndrome. Diagnostics, 13:1458, Apr 2023. URL: https://doi.org/10.3390/diagnostics13081458, doi:10.3390/diagnostics13081458. This article has 15 citations.

30. (monaco2023directoralanticoagulants pages 13-14): Giovanni Monaco, Luca Bucherini, Bernardo Stefanini, Fabio Piscaglia, Francesco Giuseppe Foschi, and Luca Ielasi. Direct oral anticoagulants for the treatment of splanchnic vein thrombosis: a state of art. World Journal of Gastroenterology, 29:4962-4974, Sep 2023. URL: https://doi.org/10.3748/wjg.v29.i33.4962, doi:10.3748/wjg.v29.i33.4962. This article has 16 citations.

31. (magaz2020buddchiarisyndromeanticoagulation pages 4-5): Marta Magaz, Guillem Soy, and Juan Carlos García-Pagán. Budd-chiari syndrome: anticoagulation, tips, or transplant. Current Hepatology Reports, pages 1-6, Jun 2020. URL: https://doi.org/10.1007/s11901-020-00528-8, doi:10.1007/s11901-020-00528-8. This article has 4 citations.

32. (khan2019reviewarticlea pages 10-11): Faisal Khan, Matthew J. Armstrong, Homoyon Mehrzad, Frederick Chen, Desley Neil, Rachel Brown, Owen Cain, and Dhiraj Tripathi. Review article: a multidisciplinary approach to the diagnosis and management of budd‐chiari syndrome. Alimentary Pharmacology & Therapeutics, 49:840-863, Mar 2019. URL: https://doi.org/10.1111/apt.15149, doi:10.1111/apt.15149. This article has 76 citations and is from a highest quality peer-reviewed journal.

33. (NCT06960473 chunk 1):  A Prospective Study on IVUS and DSA Guidance in the Treatment of Budd-Chiari Syndrome. The Affiliated Hospital of Xuzhou Medical University. 2025. ClinicalTrials.gov Identifier: NCT06960473

34. (NCT02201485 chunk 1): Guohong Han. Budd-Chiari Syndrome in China: Balloon Angioplasty Alone or Combined With Stent Placement?. Air Force Military Medical University, China. 2014. ClinicalTrials.gov Identifier: NCT02201485

35. (NCT05117684 chunk 1):  To Compare "Balloon Occluded Thrombolysis" With "Conventional Catheter Directed Thrombolysis" in Thrombotically Occluded DIPSS Stent in Patients of Budd- Chiari Syndrome.. Institute of Liver and Biliary Sciences, India. 2021. ClinicalTrials.gov Identifier: NCT05117684

36. (NCT05123326 chunk 2): Madhumita Premkumar. Global Coagulation Assessment in Portal Vein Thrombosis and Budd-Chiari Syndrome. Post Graduate Institute of Medical Education and Research, Chandigarh. 2021. ClinicalTrials.gov Identifier: NCT05123326

37. (NCT03541057 chunk 1): Thomas Reiberger. Vienna Vascular Liver Disease Study. Medical University of Vienna. 2017. ClinicalTrials.gov Identifier: NCT03541057