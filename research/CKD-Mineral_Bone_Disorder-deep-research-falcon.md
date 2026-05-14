---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T10:54:30.720965'
end_time: '2026-05-08T11:21:19.687609'
duration_seconds: 1608.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CKD-Mineral Bone Disorder
  mondo_id: ''
  category: Complex
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
- **Disease Name:** CKD-Mineral Bone Disorder
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **CKD-Mineral Bone Disorder** covering all of the
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
- **Disease Name:** CKD-Mineral Bone Disorder
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **CKD-Mineral Bone Disorder** covering all of the
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


## Comprehensive Research Report: CKD–Mineral and Bone Disorder (CKD-MBD)

### Executive summary
Chronic kidney disease–mineral and bone disorder (CKD-MBD) is a **systemic syndrome** arising in CKD characterized by **biochemical abnormalities (Ca–P–PTH–vitamin D/FGF23 axis), bone disease (renal osteodystrophy), and vascular/soft-tissue calcification**, contributing to fractures and high cardiovascular morbidity/mortality. Recent 2023–2024 literature emphasizes (i) the **bone–vascular axis** and osteocyte/vascular transdifferentiation biology, (ii) **real-world gaps** in biomarker availability (FGF23/Klotho/CPP), and (iii) **emerging markers** (calciprotein particles, T50) and data-science/AI approaches for personalization. (williams2023updatesinthe pages 1-2, fusaro2024realworldusageof pages 1-3, lederer2024applicationofartificial pages 1-3, feenstra2024calciproteinparticlecounts pages 1-2)

---

## 1. Disease information

### 1.1 What is CKD-MBD?
Recent authoritative definitions converge on CKD-MBD as a systemic syndrome linking mineral dysregulation to bone and cardiovascular pathology. A CKJ 2024 AI-focused review defines CKD-MBD as: **“the collective skeletal and cardiovascular organ damage resulting from the deranged mineral metabolism that complicates CKD.”** (https://doi.org/10.1093/ckj/sfae143; advance publication June 2024) (lederer2024applicationofartificial pages 1-3)

A 2024 Clinical Kidney Journal survey paper states: **“Chronic kidney disease mineral bone disorder (CKD-MBD) is a condition characterized by alterations of calcium, phosphate, parathyroid hormone (PTH), and fibroblast growth factor 23 (FGF-23) metabolism that in turn promote bone disorders, vascular calcifications, and increase cardiovascular (CV) risk.”** (https://doi.org/10.1093/ckj/sfad290; published 2024) (fusaro2024realworldusageof pages 1-3)

A 2024 overview emphasizes the broader systemic scope: CKD-MBD involves **dysregulation of bone turnover/mineralization/strength** with **soft-tissue and vascular calcification**, driven by disturbances in calcium, phosphate, PTH, vitamin D, FGF-23, and Klotho that occur **early in CKD**. (https://doi.org/10.3390/life14030418; March 2024) (izzo2024chronickidneydisease pages 1-2, izzo2024chronickidneydisease pages 2-4)

### 1.2 Key identifiers and codes
A single, definitive ontology/ICD code set for CKD-MBD was **not retrieved in the current evidence corpus**, and should not be guessed. The corpus supports standard naming, synonyms, and related component terms (renal osteodystrophy). See artifact below. (ketteler2017executivesummaryof pages 4-5, fusaro2024realworldusageof pages 1-3)

| Concept (identifier type) | Identifier/Code | Label | Notes/Source |
|---|---|---|---|
| Preferred disease name | — | Chronic kidney disease–mineral and bone disorder (CKD-MBD) | KDIGO 2017 and recent reviews use CKD-MBD as the standard term for the systemic disorder of mineral and bone metabolism due to CKD (https://doi.org/10.1016/j.kint.2017.04.006, 2017; https://doi.org/10.1093/ckj/sfad290, 2024; https://doi.org/10.1093/ckj/sfae143, 2024) (ketteler2017executivesummaryof pages 4-5, fusaro2024realworldusageof pages 1-3, lederer2024applicationofartificial pages 1-3) |
| Core definition | — | Systemic disorder of mineral and bone metabolism due to CKD | KDIGO-linked review states CKD-MBD is “defined as a systemic disorder of mineral and bone metabolism due to CKD” manifested by abnormalities of calcium, phosphorus, PTH, or vitamin D metabolism; abnormalities in bone turnover/mineralization/volume/growth/strength; and vascular or other soft-tissue calcification (Bone Reports review summarizing KDIGO; https://doi.org/10.1016/j.bonr.2018.07.002, 2018). Recent reviews restate this as a complex disorder linking mineral dysregulation, bone disease, and vascular calcification (https://doi.org/10.3390/life14030418, 2024; https://doi.org/10.1093/ckj/sfae143, 2024) (izzo2024chronickidneydisease pages 1-2, lederer2024applicationofartificial pages 1-3) |
| Abbreviation | — | CKD-MBD | Widely used abbreviation in guideline and review literature (https://doi.org/10.1016/j.kint.2017.04.006, 2017; https://doi.org/10.1093/ckj/sfad290, 2024) (ketteler2017executivesummaryof pages 4-5, fusaro2024realworldusageof pages 1-3) |
| Related component term | — | Renal osteodystrophy | KDIGO executive summary clarifies renal osteodystrophy is one component of CKD-MBD and refers specifically to “abnormal bone histology,” not the entire syndrome (https://doi.org/10.1016/j.kint.2017.04.006, 2017) (ketteler2017executivesummaryof pages 4-5) |
| Common synonym/near-synonym | — | CKD-related mineral and bone disorder | Used interchangeably in some reviews, but CKD-MBD remains preferred standard nomenclature (https://doi.org/10.1093/ckj/sfae143, 2024; https://doi.org/10.3390/jcm12196306, 2023) (lederer2024applicationofartificial pages 1-3, fusaro2023currentandemerging pages 5-6) |
| Common synonym/near-synonym | — | Mineral and bone disorder in chronic kidney disease | Plain-language inversion of CKD-MBD used in reviews/surveys; same syndrome (https://doi.org/10.1093/ckj/sfad290, 2024; https://doi.org/10.3390/life14030418, 2024) (fusaro2024realworldusageof pages 1-3, izzo2024chronickidneydisease pages 1-2) |
| Related pathobiology phrase | — | Bone–vascular axis / bone–vascular paradox | Not a synonym for the disease itself, but a mechanistic framing commonly used for CKD-MBD linking low bone turnover/remodeling abnormalities with vascular calcification (https://doi.org/10.3389/fphys.2023.1120308, 2023; https://doi.org/10.3390/life14030418, 2024) (williams2023updatesinthe pages 1-2, izzo2024chronickidneydisease pages 1-2) |
| MONDO | not retrieved in current corpus | — | No MONDO identifier was available in the retrieved evidence corpus; should not be guessed (fusaro2024realworldusageof pages 1-3, ketteler2017executivesummaryof pages 4-5) |
| MeSH | not retrieved in current corpus | — | No MeSH identifier for CKD-MBD was directly retrieved in the current evidence corpus; related historical indexing may use broader bone/kidney disorder terms, but not confirmed here (fusaro2024realworldusageof pages 1-3, ketteler2017executivesummaryof pages 4-5) |
| ICD-10 | not retrieved in current corpus | — | No single ICD-10 code for CKD-MBD was directly retrieved in the current corpus; syndrome is typically represented across CKD, mineral metabolism, bone disorder, and hyperparathyroidism coding domains rather than a single dedicated code (not confirmed from current evidence) (fusaro2024realworldusageof pages 1-3, izzo2024chronickidneydisease pages 1-2) |
| ICD-11 | not retrieved in current corpus | — | No directly retrieved ICD-11 identifier in the current corpus (fusaro2024realworldusageof pages 1-3, izzo2024chronickidneydisease pages 1-2) |
| OMIM | not retrieved in current corpus | — | No OMIM entry was retrieved; CKD-MBD is a complex acquired syndrome rather than a single-gene Mendelian disease entity in the reviewed sources (izzo2024chronickidneydisease pages 1-2, lederer2024applicationofartificial pages 1-3) |
| Orphanet | not retrieved in current corpus | — | No Orphanet identifier was retrieved in the current evidence corpus (fusaro2024realworldusageof pages 1-3) |
| Evidence source type | — | Aggregated disease-level resource and cohort/review literature | Information here is derived from disease-level guidelines/reviews and clinical cohorts/surveys rather than individual-patient EHR extraction alone (KDIGO 2017 guideline/update; Italian nephrologist survey; recent reviews) (https://doi.org/10.1016/j.kint.2017.04.006, 2017; https://doi.org/10.1093/ckj/sfad290, 2024; https://doi.org/10.3390/life14030418, 2024) (ketteler2017executivesummaryof pages 4-5, fusaro2024realworldusageof pages 1-3, izzo2024chronickidneydisease pages 1-2) |


*Table: This table summarizes the core disease definition, standard terminology, related terms, and identifier availability for CKD-MBD using only the retrieved evidence corpus. It is useful for populating a knowledge-base entry while clearly marking identifiers that were not directly retrieved.*

### 1.3 Synonyms and alternative names
Commonly used alternatives include “mineral and bone disorder in chronic kidney disease,” “CKD-related mineral and bone disorder,” and the component term “renal osteodystrophy” (a bone histology entity within CKD-MBD). (ketteler2017executivesummaryof pages 4-5, fusaro2024realworldusageof pages 1-3)

### 1.4 Evidence source type
Information here is derived primarily from **aggregated disease-level guidelines/reviews and cohorts/surveys** (KDIGO guideline update, observational cohorts, biomarker trials), not individual-patient EHR extraction. (wheeler2017kdigo2017clinical pages 13-16, neri2019detectinghighriskchronic pages 1-2, thiem2023effectofthe pages 1-3)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
CKD-MBD is an **acquired, CKD-driven systemic syndrome** caused by reduced kidney function leading to disturbed phosphate excretion, impaired vitamin D activation, altered calcium homeostasis, endocrine adaptations (PTH/FGF23), and downstream bone remodeling abnormalities and calcification biology. Reviews highlight that **phosphate stress** is central (“phosphorocentric hypothesis”), with feedback actors including vitamin D, PTH, CPPs, FGF-23 and Klotho. (https://doi.org/10.1111/nep.14407; Oct 2024) (izzo2024chronickidneydisease pages 2-4)

### 2.2 Risk factors
Evidence from a large CKD cohort (CRIC) indicates multiple modifiable and CKD-related factors are associated with hip/vertebral fractures. In 3939 participants, baseline **diabetes, lower BMI, steroid use, proteinuria, and elevated PTH** were associated with fracture risk; time-updated **lower eGFR, lower serum calcium, and lower bicarbonate** were also associated. (https://doi.org/10.1093/jbmr/zjae021; advance access Feb 4, 2024) (hsu2024riskfactorsfor pages 1-2)

In dialysis populations, combinations of Ca/P/PTH abnormalities define high-risk CKD-MBD phenotypes with increased mortality and hospitalization, consistent with CKD-MBD as a risk-enrichment syndrome. (neri2019detectinghighriskchronic pages 1-2, fuller2020combinationsofmineral pages 1-2)

### 2.3 Protective factors
Protective factors are incompletely defined in the retrieved corpus. One recent systematic review/meta-analysis suggests **physical exercise** may beneficially modulate the **Klotho–FGF23 axis**, reporting decreased FGF23 and increased Klotho in pooled RCT data (though this pertains to CKD broadly and is not limited to CKD-MBD endpoints). (https://doi.org/10.7150/ijms.90195; Jan 2024) (simic2024boneandbone pages 1-2)

### 2.4 Gene–environment interactions
Not retrieved in current corpus at a specificity appropriate for CKD-MBD knowledge base annotation.

---

## 3. Phenotypes

### 3.1 Core phenotype domains
CKD-MBD phenotypes cluster into:
1) **Laboratory abnormalities**: hyperphosphatemia (or phosphate stress), hypocalcemia/hypercalcemia, elevated iPTH, low active vitamin D, elevated FGF23, Klotho deficiency (often investigational). (lederer2024applicationofartificial pages 1-3, izzo2024chronickidneydisease pages 2-4, fusaro2024realworldusageof pages 1-3)
2) **Skeletal abnormalities / renal osteodystrophy** (bone turnover/mineralization/strength). (izzo2024chronickidneydisease pages 1-2, ketteler2017executivesummaryof pages 4-5)
3) **Vascular and soft-tissue calcification** and related cardiovascular sequelae. (izzo2024chronickidneydisease pages 1-2, williams2023updatesinthe pages 1-2)

### 3.2 Quantitative clinical phenotype data (fracture outcomes)
In CRIC (n=3939), fracture incidence for hip/vertebral fractures was **2.4 events per 1000 person-years** (95% CI 2.0–2.9) over mean 11.1 years; fracture hazard was highest in **kidney failure treated with dialysis** vs eGFR≥60 (HR 4.53; 95% CI 1.77–11.60). (hsu2024riskfactorsfor pages 1-2)

### 3.3 Quality-of-life impact
Direct QoL instrument statistics (e.g., EQ-5D, PROMIS) were not retrieved in the current corpus; however, fractures and cardiovascular disease are consistently identified as major morbidity drivers in CKD-MBD reviews and cohorts. (simic2024boneandbone pages 1-2, neri2019detectinghighriskchronic pages 1-2)

### 3.4 HPO term suggestions (non-exhaustive; ontology IDs not validated in corpus)
Not retrieved in current corpus; should be mapped during curation using validated HPO resources. Phenotypic concepts to map include: hyperparathyroidism, hyperphosphatemia, hypocalcemia/hypercalcemia, vitamin D deficiency, renal osteodystrophy, osteoporosis/low bone mineral density, vascular calcification.

---

## 4. Genetic / molecular information

### 4.1 Causal genes and pathogenic variants
CKD-MBD is primarily a **complex acquired syndrome** secondary to CKD rather than a Mendelian disorder; no causal gene/variant lists were retrieved in the current corpus. (izzo2024chronickidneydisease pages 1-2, lederer2024applicationofartificial pages 1-3)

### 4.2 Key molecular mediators emphasized in 2023–2024 literature
Key endocrine and signaling mediators include:
- **PTH** and parathyroid hyperplasia in secondary hyperparathyroidism (SHPT), linked to fractures and mortality in advanced CKD. (https://doi.org/10.3803/enm.2024.1978; June 2024) (simic2024boneandbone pages 1-2)
- **FGF23–Klotho axis** as a phosphate/vitamin D regulator and potential mediator of off-target organ effects (causality for outcomes remains under investigation). (simic2024boneandbone pages 1-2)
- **Wnt signaling / sclerostin (SOST)** framing the bone–vascular paradox; vascular-derived sclerostin may function as a brake on Wnt-driven calcification, complicating therapeutic inhibition strategies. The 2023 update review states: **“inhibition of sclerostin activity by a monoclonal antibody improved bone remodeling as expected, but stimulated vascular calcification”**, arguing that a better target is reducing vascular osteoblastic/osteocytic transdifferentiation. (https://doi.org/10.3389/fphys.2023.1120308; Jan 2023) (williams2023updatesinthe pages 1-2)

### 4.3 Suggested GO / CL terms
Ontology term IDs were not retrieved in the corpus; however, mechanistic processes supported here include endothelial activation, inflammation, extracellular matrix remodeling, ossification, and osteogenic transdifferentiation of vascular smooth muscle cells. (feenstra2024calciproteinparticlecounts pages 1-2, williams2023updatesinthe pages 1-2)

---

## 5. Environmental information

### 5.1 Lifestyle / nutrition
The corpus emphasizes phosphate loading and calcium load as contributors to vascular calcification biology, but does not provide detailed exposure-response estimates for lifestyle factors.

### 5.2 Exercise as a potential modifier
A 2024 meta-analysis of 4 RCTs (n=272) reported exercise decreased FGF23 (MD −102.07 pg/mL; p=0.001) and increased Klotho (MD 158.82 pg/mL; p=0.001). (simic2024boneandbone pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (simplified)
**Declining kidney function** → phosphate retention/phosphate stress → compensatory endocrine changes (**↑FGF23**, **↑PTH**, **↓calcitriol**) and altered calcium balance → disturbed bone remodeling/turnover (renal osteodystrophy; osteoporosis phenotypes) and generation of **calciprotein particles (CPP)** → vascular smooth muscle cell osteogenic programming, endothelial activation/inflammation/ECM remodeling → **vascular calcification** and cardiovascular complications, contributing to mortality. This integrated, systemic framing is emphasized in 2023–2024 literature. (izzo2024chronickidneydisease pages 2-4, izzo2024chronickidneydisease pages 1-2, feenstra2024calciproteinparticlecounts pages 1-2)

### 6.2 Vascular calcification and CPP biology (2023–2024 developments)
A 2024 Cardiovascular Research study linking imaging, vascular transcriptomics and CPP measures reports that CKD is characterized by systemic vascular calcification with increased calcification propensity and CPP counts, and vascular tissue shows enrichment of **“endothelial activation, inflammation, extracellular matrix (ECM) remodelling, and ossification”** processes; CPP counts were significantly associated with vascular remodeling markers. (https://doi.org/10.1093/cvr/cvae164; online ahead Aug 5, 2024) (feenstra2024calciproteinparticlecounts pages 1-2)

Mechanistic-interventional evidence in dialysis patients supports CPP reduction as a plausible therapeutic axis: in a randomized crossover secondary analysis (n=28), high-dose sucroferric oxyhydroxide reduced primary CPP by **−62%** and secondary CPP by **−38%** versus washout, and reduced inflammatory cytokines (including IL-6 and IL-8); serum from treated patients induced less vascular calcification and endothelial activation in vitro. (https://doi.org/10.1093/ndt/gfac271; NDT 2023) (thiem2023effectofthe pages 1-3)

### 6.3 AI and systems modeling (2024)
A 2024 CKJ review argues that guideline-era therapies targeting surrogate biochemical targets have not changed cardiovascular outcomes and proposes a combined mathematical modeling + machine learning approach for hypothesis generation, in-silico trials, and therapy personalization. It reiterates the biochemical signature as **“high serum phosphate, low calcium, high parathyroid hormone (PTH), low active vitamin D (calcitriol), and high fibroblast growth factor 23 (FGF23).”** (https://doi.org/10.1093/ckj/sfae143; June 2024) (lederer2024applicationofartificial pages 1-3)

---

## 7. Anatomical structures affected

### 7.1 Organ level (supported in corpus)
- **Bone/skeleton** (renal osteodystrophy; osteoporosis phenotype) (izzo2024chronickidneydisease pages 1-2, ketteler2017executivesummaryof pages 4-5)
- **Vasculature** (arterial media calcification; remodeling) (feenstra2024calciproteinparticlecounts pages 1-2, izzo2024chronickidneydisease pages 1-2)
- **Cardiovascular system** (CVD risk and mortality association emphasized) (williams2023updatesinthe pages 1-2, izzo2024chronickidneydisease pages 1-2)

### 7.2 Tissue/cell level
- **Vascular smooth muscle cells (VSMCs)** undergoing osteogenic transdifferentiation in uremic milieu (review framing). (izzo2024chronickidneydisease pages 1-2)
- Vascular tissues exhibit transcriptomic enrichment for endothelial activation/inflammation/ECM remodeling/ossification. (feenstra2024calciproteinparticlecounts pages 1-2)

### 7.3 UBERON / CL suggestions
Ontology IDs not retrieved; map bone tissue, arterial media, VSMCs, endothelial cells during curation.

---

## 8. Temporal development

### 8.1 Onset and progression
Biochemical perturbations and endocrine adaptations can occur early (often from CKD stage 3) and progress with declining eGFR; bone and vascular complications accumulate, with highest fracture hazard observed in kidney failure/dialysis populations. (izzo2024chronickidneydisease pages 2-4, hsu2024riskfactorsfor pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (CKD burden)
A 2024 overview summarizes global CKD burden as **697.5 million affected worldwide**, **35.8 million DALYs**, and **1.2 million deaths in 2017**, with CKD mortality increasing **41.5%** from 1990 to 2017. (https://doi.org/10.3390/life14030418; 2024) (izzo2024chronickidneydisease pages 1-2)

### 9.2 CKD-MBD population-risk statistics from cohorts
In a 35,721-patient international dialysis cohort (EuCliD), there were **126.7 deaths/1000 person-years** and CKD-MBD phenotype-specific adjusted mortality HRs ranged **1.07 to 1.59** across Ca/P/PTH phenotype combinations. (neri2019detectinghighriskchronic pages 1-2)

---

## 10. Diagnostics

### 10.1 Standard biochemical testing and monitoring (KDIGO 2017)
KDIGO 2017 recommends **monitoring serum calcium, phosphate, PTH, and alkaline phosphatase starting in CKD G3a**, and optionally measuring 25(OH)D with correction of deficiency/insufficiency per general-population strategies. Suggested monitoring frequencies are stage-based (see table image citation and details below). (wheeler2017kdigo2017clinical pages 13-16, wheeler2017kdigo2017clinical media ed681c34)

**Visual evidence (KDIGO monitoring frequency table/summary):** (wheeler2017kdigo2017clinical media ed681c34)

KDIGO suggested monitoring intervals (adult CKD) include:
- **CKD G3a–G3b:** Ca and phosphate every **6–12 months**; PTH based on baseline and progression.
- **CKD G4:** Ca and phosphate every **3–6 months**; PTH every **6–12 months**.
- **CKD G5/G5D:** Ca and phosphate every **1–3 months**; PTH every **3–6 months**.
- **CKD G4–G5D:** alkaline phosphatase every **12 months** (more often if PTH elevated).
- **25(OH)D:** “might be measured” with repeat testing based on baseline and interventions.
(wheeler2017kdigo2017clinical pages 13-16, wheeler2017kdigo2017clinical media ed681c34)

### 10.2 Bone and vascular imaging tools
The 2024 overview notes multiple approaches for vascular calcification detection (e.g., lateral plain X-ray, Kauppila and Adragao scores, pulse wave velocity, and pQCT). (izzo2024chronickidneydisease pages 1-2)

### 10.3 Emerging markers/tools
A 2023 review on non-dialysis CKD highlights a need for additional markers beyond late-stage dialysis practice and discusses emerging markers including CPP/T50 approaches in CKD-MBD management contexts. (https://doi.org/10.3390/jcm12196306; Sep 2023) (fusaro2023currentandemerging pages 5-6)

### 10.4 Real-world implementation of diagnostic testing (2024)
A 2024 Italian survey (n=106 nephrologists) provides a real-world snapshot of biomarker availability and guideline use:
- Hospital labs could support requests for **ionized calcium** (99.1%), **PTH** (99.1%), **ALP** (99.1%), **25(OH)D** (94.3%), but only **1,25(OH)2D** (57.5%).
- Most labs did **not** support **FGF-23** (intact 88.7% unavailable; C-terminal 93.4% unavailable) or **Klotho** (95.3% unavailable; soluble 97.2% unavailable).
- Guideline usage for starting SHPT therapy varied: **KDOQI** used by 51.9% vs **KDIGO** by 37.7%.
(https://doi.org/10.1093/ckj/sfad290; 2024) (fusaro2024realworldusageof pages 1-3)

| Biomarker (CHEBI/protein where applicable) | What it reflects in CKD-MBD | KDIGO 2017 monitoring recommendation | Common real-world availability / implementation notes | Key evidence citation (URL/year) |
|---|---|---|---|---|
| Calcium (ionized/serum calcium; CHEBI:29108) | Core mineral homeostasis abnormality; tends to decrease with CKD progression, and both hypo- and hypercalcemia are linked with CKD progression and higher cardiovascular mortality; integrated with phosphate and PTH for treatment decisions (izzo2024chronickidneydisease pages 2-4, wheeler2017kdigo2017clinical pages 16-18) | Monitor from CKD G3a onward. Suggested intervals: G3a–G3b every 6–12 mo; G4 every 3–6 mo; G5/G5D every 1–3 mo. Use serial assessments of phosphate, calcium, and PTH together rather than single values (wheeler2017kdigo2017clinical pages 13-16, wheeler2017kdigo2017clinical pages 16-18, wheeler2017kdigo2017clinical media ed681c34) | Italian survey: ionized calcium available in 99.1% of hospital laboratories; widely implemented routine biomarker (fusaro2024realworldusageof pages 1-3) | KDIGO update https://doi.org/10.1016/j.kint.2017.04.006 (2017); survey https://doi.org/10.1093/ckj/sfad290 (2024) (ketteler2017executivesummaryof pages 4-5, fusaro2024realworldusageof pages 1-3) |
| Phosphate / phosphorus (CHEBI:18367) | Phosphorocentric driver of CKD-MBD; linked to bone osteodystrophy, vascular calcification, CKD progression, ESKD, and all-cause/CV mortality; early compensatory rises in FGF23/PTH initially maintain normophosphatemia (izzo2024chronickidneydisease pages 2-4, izzo2024chronickidneydisease pages 1-2) | Monitor from CKD G3a onward at same intervals as calcium: G3a–G3b every 6–12 mo; G4 every 3–6 mo; G5/G5D every 1–3 mo. Treatment should focus on progressively or persistently elevated phosphate and lower elevated phosphate toward the normal range; avoid phosphate loading (wheeler2017kdigo2017clinical pages 13-16, wheeler2017kdigo2017clinical pages 16-18, fusaro2023currentandemerging pages 5-6) | Routine lab marker; widely available. In real-world practice, phosphate control is guideline-driven but implementation is heterogeneous; advanced CPP/T50 tools are not routine substitutes for serum phosphate (fusaro2024realworldusageof pages 1-3, fusaro2023currentandemerging pages 5-6) | Review https://doi.org/10.1111/nep.14407 (2024); KDIGO https://doi.org/10.1016/j.kint.2017.04.006 (2017) (izzo2024chronickidneydisease pages 2-4, ketteler2017executivesummaryof pages 4-5) |
| Intact PTH / parathyroid hormone (PTH; UniProt P01270) | Central marker of secondary hyperparathyroidism and bone turnover disturbance; rises from CKD stage 3; associated with fractures, vascular events, and mortality in observational studies (izzo2024chronickidneydisease pages 2-4, fusaro2023currentandemerging pages 5-6) | Monitor from CKD G3a onward. Suggested intervals: G3a–G3b based on baseline level and CKD progression; G4 every 6–12 mo; G5/G5D every 3–6 mo. In CKD G5D, maintain iPTH approximately 2–9× assay ULN and use trends rather than single measurements (wheeler2017kdigo2017clinical pages 13-16, wheeler2017kdigo2017clinical pages 16-18, fusaro2023currentandemerging pages 5-6) | Italian survey: PTH available in 99.1% of hospital laboratories. Most clinicians used KDOQI (51.9%) vs KDIGO (37.7%) to start sHPT treatment, showing heterogeneous implementation (fusaro2024realworldusageof pages 1-3) | Roles review https://doi.org/10.3803/enm.2024.1978 (2024); KDIGO https://doi.org/10.1016/j.kint.2017.04.006 (2017) (fusaro2024realworldusageof pages 1-3, ketteler2017executivesummaryof pages 4-5) |
| Alkaline phosphatase, total and bone-specific if available (ALP; bone ALP/BSAP) | Surrogate marker of bone turnover; bone-specific ALP can help evaluate turnover alongside PTH; treatment decisions should consider abnormal alkaline phosphatase among other CKD-MBD markers (ketteler2017executivesummaryof pages 4-5, wheeler2017kdigo2017clinical pages 13-16) | Monitor alkaline phosphatase beginning in CKD G3a; suggested in G4–G5D every 12 mo, more often if PTH elevated. Serum PTH or bone-specific ALP may be used to evaluate bone disease because markedly high or low values predict underlying bone turnover (wheeler2017kdigo2017clinical pages 13-16) | Italian survey: ALP available in 99.1% of laboratories; bone-specific assays were not specifically quantified, suggesting standard total ALP is the practical routine marker (fusaro2024realworldusageof pages 1-3) | KDIGO guideline pages summarized in https://doi.org/10.1016/j.kint.2017.04.006 (2017); real-world survey https://doi.org/10.1093/ckj/sfad290 (2024) (wheeler2017kdigo2017clinical pages 13-16, fusaro2024realworldusageof pages 1-3) |
| 25-hydroxyvitamin D / 25(OH)D (calcidiol; CHEBI:28940) | Nutritional vitamin D status; deficiency/insufficiency is common in CKD and contributes to CKD-MBD pathogenesis and SHPT (izzo2024chronickidneydisease pages 2-4) | In CKD G3a–G5D, 25(OH)D levels may be measured; repeat testing should depend on baseline values and interventions. Correct deficiency/insufficiency as in the general population (wheeler2017kdigo2017clinical pages 13-16, wheeler2017kdigo2017clinical media ed681c34) | Italian survey: 25(OH)D available in 94.3% of laboratories, supporting moderate-to-high real-world implementation (fusaro2024realworldusageof pages 1-3) | Vitamin D review https://doi.org/10.32948/ajsep.2024.05.20 (2024); KDIGO update https://doi.org/10.1016/j.kint.2017.04.006 (2017) (fusaro2024realworldusageof pages 1-3, wheeler2017kdigo2017clinical pages 13-16) |
| 1,25-dihydroxyvitamin D / calcitriol (CHEBI:28934) | Active vitamin D deficiency is part of the biochemical signature of CKD-MBD; suppressed early by rising FGF23 and reduced renal activation capacity, promoting SHPT and impaired mineral balance (lederer2024applicationofartificial pages 1-3, izzo2024chronickidneydisease pages 2-4) | No routine stage-specific monitoring interval retrieved from KDIGO evidence here; KDIGO recommendations cited in retrieved reviews emphasize use of nutritional vitamin D in earlier CKD and reserving calcitriol/analogs for more advanced disease/SHPT rather than routine serial assay-based targeting (izzo2024chronickidneydisease pages 2-4, wheeler2017kdigo2017clinical pages 16-18) | Italian survey: 1,25(OH)2D available in only 57.5% of laboratories, indicating substantially lower real-world availability than 25(OH)D (fusaro2024realworldusageof pages 1-3) | AI review https://doi.org/10.1093/ckj/sfae143 (2024); survey https://doi.org/10.1093/ckj/sfad290 (2024) (lederer2024applicationofartificial pages 1-3, fusaro2024realworldusageof pages 1-3) |
| FGF23 / fibroblast growth factor 23 (UniProt Q9GZV9) | Early osteocyte-derived phosphaturic hormone; rises early in CKD, suppresses calcitriol, reflects phosphate stress, and is associated with mortality and vascular calcification severity in observational studies (izzo2024chronickidneydisease pages 2-4, simic2024boneandbone pages 1-2) | Not part of standard KDIGO 2017 routine monitoring panel in retrieved text; considered an emerging/non-routine biomarker rather than a guideline-mandated serial test (wheeler2017kdigo2017clinical pages 13-16, fusaro2023currentandemerging pages 5-6) | Italian survey: intact FGF23 unavailable in 88.7% of laboratories and C-terminal FGF23 unavailable in 93.4%, indicating poor routine implementation despite mechanistic importance (fusaro2024realworldusageof pages 1-3) | FGF23/Klotho review https://doi.org/10.3803/enm.2024.1978 (2024); survey https://doi.org/10.1093/ckj/sfad290 (2024) (fusaro2024realworldusageof pages 1-3, simic2024boneandbone pages 1-2) |
| Klotho / α-Klotho (UniProt Q9UEF7) | Anti-aging co-receptor for FGF23; deficiency begins early in CKD and is linked to phosphate retention, FGF23 resistance, vascular calcification, and CKD-MBD progression (izzo2024chronickidneydisease pages 2-4, simic2024boneandbone pages 1-2) | No KDIGO 2017 routine monitoring recommendation retrieved; currently investigational/controversial as a biomarker because assays and standardization remain limited (wheeler2017kdigo2017clinical pages 13-16, simic2024boneandbone pages 1-2) | Italian survey: Klotho unavailable in 95.3% of labs and soluble Klotho unavailable in 97.2%, showing minimal clinical implementation (fusaro2024realworldusageof pages 1-3) | Klotho meta-analysis https://doi.org/10.1038/s41598-024-54812-4 (2024); survey https://doi.org/10.1093/ckj/sfad290 (2024) (fusaro2024realworldusageof pages 1-3, simic2024boneandbone pages 1-2) |
| Calciprotein particles / calcification propensity T50 (CPPs/T50; mineral-protein nanoparticles, not a single CHEBI entity) | Emerging markers of phosphate toxicity and mineral buffering; higher CPP burden and lower T50 indicate greater calcification propensity and associate with vascular remodeling, inflammation, endothelial activation, and ossification in CKD (izzo2024chronickidneydisease pages 1-2, fusaro2023currentandemerging pages 5-6) | No KDIGO 2017 routine monitoring recommendation retrieved; CPP/T50 are emerging research tools, not standard guideline biomarkers (fusaro2023currentandemerging pages 5-6, wheeler2017kdigo2017clinical pages 13-16) | Not included in routine hospital lab menus in the Italian survey; CPP/T50 are discussed as emerging markers/tools rather than standard practice. Proof-of-principle studies show high-dose sucroferric oxyhydroxide reduced primary CPP by 62% and secondary CPP by 38%, while etelcalcetide reduced CPP fractions without significantly changing T50 (fusaro2023currentandemerging pages 5-6) | CPP vascular study https://doi.org/10.1093/cvr/cvae164 (2024); sucroferric oxyhydroxide https://doi.org/10.1093/ndt/gfac271 (2023); etelcalcetide https://doi.org/10.1093/ckj/sfae097 (2024) (fusaro2023currentandemerging pages 5-6, izzo2024chronickidneydisease pages 1-2) |


*Table: This table summarizes the main laboratory and emerging biomarkers used in CKD-MBD, what they represent biologically, how KDIGO 2017 recommends monitoring the standard markers, and what recent real-world evidence shows about laboratory availability and implementation.*

---

## 11. Outcome / prognosis

### 11.1 Mortality and hospitalization risk (dialysis)
- In the EuCliD dialysis cohort (n=35,721), mortality was **126.7 deaths/1000 person-years** and hospitalization incidence **203.9/1000 person-years**, with phenotype-dependent adjusted mortality HRs up to **1.59**. (neri2019detectinghighriskchronic pages 1-2)
- In international DOPPS hemodialysis patients, having 2–3 markers above target (Ca/P/PTH composite) was associated with higher mortality (USA HR **1.41**, 95% CI 1.10–1.82) vs all markers in target; in age ≥65 the HR was **1.82** (95% CI 1.28–2.58). (fuller2020combinationsofmineral pages 1-2)

### 11.2 Fracture outcomes (non-dialysis CKD and kidney failure)
CRIC reports 2.4 hip/vertebral fractures per 1000 person-years; fracture hazard is markedly increased in kidney failure on dialysis (HR 4.53). (hsu2024riskfactorsfor pages 1-2)

---

## 12. Treatment

### 12.1 KDIGO 2017 treatment principles (selected)
KDIGO 2017 emphasizes treatment based on **serial assessments** of phosphate, calcium and PTH considered together, and suggests:
- **Lower elevated phosphate toward the normal range** and focus phosphate-lowering treatment on hyperphosphatemia.
- **Avoid hypercalcemia**.
- In adults receiving phosphate-lowering treatment, **restrict calcium-based phosphate binders**.
- In CKD G5D, maintain iPTH roughly **2–9×** the assay ULN; options include calcimimetics, calcitriol, vitamin D analogs, or combination when PTH-lowering therapy is needed.
(wheeler2017kdigo2017clinical pages 16-18, wheeler2017kdigo2017clinical pages 13-16, ketteler2017executivesummaryof pages 4-5)

### 12.2 Therapeutic innovation and mechanistic interventions (recent literature)
- **CPP-focused effects of phosphate binders (2023):** sucroferric oxyhydroxide reduced CPP fractions and attenuated inflammatory/pro-calcific serum effects in vitro. (thiem2023effectofthe pages 1-3)
- **Data-science/AI for personalization (2024):** proposed as an approach to address heterogeneity and improve targeting beyond surrogate biochemical targets. (lederer2024applicationofartificial pages 1-3)

### 12.3 MAXO suggestions
Not retrieved in the current corpus; map standard actions such as phosphate binder therapy, calcimimetic therapy, vitamin D supplementation/analogs, dialysis prescription changes, and parathyroidectomy during ontology curation.

---

## 13. Prevention
Primary prevention of CKD-MBD is primarily prevention/mitigation of CKD progression and early control of mineral metabolism disturbances. KDIGO’s emphasis on early monitoring from CKD G3a and trend-based management supports secondary prevention of complications. (wheeler2017kdigo2017clinical pages 13-16)

---

## 14. Other species / natural disease
Not retrieved in current corpus.

---

## 15. Model organisms
Not retrieved in current corpus for CKD-MBD-specific models; mechanistic literature referenced in reviews indicates animal studies exist (e.g., sclerostin/Wnt, erythropoiesis/FGF23), but model details were not extracted from the retrieved pages. (simic2024boneandbone pages 1-2, williams2023updatesinthe pages 1-2)

---

## Appendix: Key 2023–2024 sources (with dates/URLs as available in corpus)
- KDIGO CKD-MBD guideline update (2017): https://doi.org/10.1016/j.kint.2017.04.006 (July 2017) (ketteler2017executivesummaryof pages 4-5)
- Fusaro et al., CKJ real-world biomarker usage survey: https://doi.org/10.1093/ckj/sfad290 (2024) (fusaro2024realworldusageof pages 1-3)
- Lederer et al., AI in CKD-MBD: https://doi.org/10.1093/ckj/sfae143 (June 2024) (lederer2024applicationofartificial pages 1-3)
- Izzo et al., CKD-MBD and vascular calcification overview: https://doi.org/10.3390/life14030418 (March 2024) (izzo2024chronickidneydisease pages 1-2)
- Hsu et al., CRIC fracture risk factors: https://doi.org/10.1093/jbmr/zjae021 (Feb 2024) (hsu2024riskfactorsfor pages 1-2)
- Feenstra et al., CPP counts and vascular remodeling: https://doi.org/10.1093/cvr/cvae164 (Aug 2024 online ahead) (feenstra2024calciproteinparticlecounts pages 1-2)
- Thiem et al., sucroferric oxyhydroxide effects on CPP/inflammation: https://doi.org/10.1093/ndt/gfac271 (2023; advance access Sept 2022) (thiem2023effectofthe pages 1-3)
- Williams et al., osteocytic proteins/bone–vascular paradox update: https://doi.org/10.3389/fphys.2023.1120308 (Jan 2023) (williams2023updatesinthe pages 1-2)


References

1. (williams2023updatesinthe pages 1-2): Matthew J. Williams, Sarah C. White, Zachary Joseph, and Keith A. Hruska. Updates in the chronic kidney disease-mineral bone disorder show the role of osteocytic proteins, a potential mechanism of the bone—vascular paradox, a therapeutic target, and a biomarker. Frontiers in Physiology, Jan 2023. URL: https://doi.org/10.3389/fphys.2023.1120308, doi:10.3389/fphys.2023.1120308. This article has 23 citations.

2. (fusaro2024realworldusageof pages 1-3): Maria Fusaro, Simona Barbuto, Maurizio Gallieni, Althea Cossettini, Giulia Vanessa Re Sartò, Laura Cosmai, Giuseppe Cianciolo, Gaetano La Manna, Thomas Nickolas, Serge Ferrari, Jordi Bover, Mathias Haarhaus, Carmela Marino, Maria Cristina Mereu, Maura Ravera, Mario Plebani, Martina Zaninotto, Mario Cozzolino, Stefano Bianchi, Piergiorgio Messa, Mariacristina Gregorini, Lorenzo Gasperoni, Caterina Agosto, Andrea Aghi, and Giovanni Tripepi. Real-world usage of chronic kidney disease – mineral bone disorder (ckd–mbd) biomarkers in nephrology practices. Clinical Kidney Journal, Nov 2024. URL: https://doi.org/10.1093/ckj/sfad290, doi:10.1093/ckj/sfad290. This article has 25 citations and is from a peer-reviewed journal.

3. (lederer2024applicationofartificial pages 1-3): Eleanor D Lederer, Mahmoud M Sobh, Michael E Brier, and Adam E Gaweda. Application of artificial intelligence to chronic kidney disease mineral bone disorder. Clinical Kidney Journal, Jun 2024. URL: https://doi.org/10.1093/ckj/sfae143, doi:10.1093/ckj/sfae143. This article has 5 citations and is from a peer-reviewed journal.

4. (feenstra2024calciproteinparticlecounts pages 1-2): Lian Feenstra, Melanie Reijrink, Andreas Pasch, Edward R Smith, Lotte M Visser, Marian Bulthuis, Monique E Lodewijk, Mirjam F Mastik, Marcel J W Greuter, Riemer H J A Slart, Douwe J Mulder, Robert A Pol, Charlotte A te Velde-Keyzer, Guido Krenning, Jan-Luuk Hillebrands, V Adelita Ranchor, Antonio W Gomes Neto, Arjan Diepstra, G Bouke Hepkema, C Tji Gan, Caecilia S E Doorenbos, Charlotte A te Velde-Keyzer, Coretta van Leer-Buter, J Daan Touw, Eelko Hak, A M Erik Verschuuren, A J A Frank Bodewes, Frank Klont, Gerard Dijkstra, J Gertrude Nieuwenhuis-Moeke, Hans Blokzijl, G D Henri Leuvenink, Hubert G M Niesters, J Cas Swarte, Jan-Stephan F Sanders, Kevin Damman, L Joost van Pelt, Marco van Londen, Marieke T de Boer, Marion J Siebelink, Marius C van den Heuvel, Michel J Vos, Michiel E Erasmus, Rianne M Douwes, Riemer J H J A Slart, Rinse K Weersma, Robert A Pol, Robert J Porte, Vincent E de Meijer, and Willem S Lexmond. Calciprotein particle counts associate with vascular remodelling in chronic kidney disease. Cardiovascular Research, 120:1953-1966, Aug 2024. URL: https://doi.org/10.1093/cvr/cvae164, doi:10.1093/cvr/cvae164. This article has 19 citations and is from a domain leading peer-reviewed journal.

5. (izzo2024chronickidneydisease pages 1-2): Carmine Izzo, Carmine Secondulfo, Giancarlo Bilancio, Valeria Visco, Nicola Virtuoso, Serena Migliarino, Michele Ciccarelli, Paola Di Pietro, Lucia La Mura, Antonio Damato, Albino Carrizzo, and Carmine Vecchione. Chronic kidney disease with mineral bone disorder and vascular calcification: an overview. Life, 14:418, Mar 2024. URL: https://doi.org/10.3390/life14030418, doi:10.3390/life14030418. This article has 58 citations.

6. (izzo2024chronickidneydisease pages 2-4): Carmine Izzo, Carmine Secondulfo, Giancarlo Bilancio, Valeria Visco, Nicola Virtuoso, Serena Migliarino, Michele Ciccarelli, Paola Di Pietro, Lucia La Mura, Antonio Damato, Albino Carrizzo, and Carmine Vecchione. Chronic kidney disease with mineral bone disorder and vascular calcification: an overview. Life, 14:418, Mar 2024. URL: https://doi.org/10.3390/life14030418, doi:10.3390/life14030418. This article has 58 citations.

7. (ketteler2017executivesummaryof pages 4-5): Markus Ketteler, Geoffrey A. Block, Pieter Evenepoel, Masafumi Fukagawa, Charles A. Herzog, Linda McCann, Sharon M. Moe, Rukshana Shroff, Marcello A. Tonelli, Nigel D. Toussaint, Marc G. Vervloet, and Mary B. Leonard. Executive summary of the 2017 kdigo chronic kidney disease–mineral and bone disorder (ckd-mbd) guideline update: what’s changed and why it matters. Kidney International, 92:26-36, Jul 2017. URL: https://doi.org/10.1016/j.kint.2017.04.006, doi:10.1016/j.kint.2017.04.006. This article has 1291 citations and is from a highest quality peer-reviewed journal.

8. (fusaro2023currentandemerging pages 5-6): Maria Fusaro, Luciano Pereira, and Jordi Bover. Current and emerging markers and tools used in the diagnosis and management of chronic kidney disease–mineral and bone disorder in non-dialysis adult patients. Journal of Clinical Medicine, 12:6306, Sep 2023. URL: https://doi.org/10.3390/jcm12196306, doi:10.3390/jcm12196306. This article has 18 citations.

9. (wheeler2017kdigo2017clinical pages 13-16): DC Wheeler and WC Winkelmayer. Kdigo 2017 clinical practice guideline update for the diagnosis, evaluation, prevention, and treatment of chronic kidney disease-mineral and bone disorder (ckd …. Unknown journal, 2017.

10. (neri2019detectinghighriskchronic pages 1-2): Luca Neri, Ursula Kreuzberg, Francesco Bellocchio, Diego Brancaccio, Carlo Barbieri, Bernard Canaud, Stefano Stuard, and Markus Ketteler. Detecting high-risk chronic kidney disease-mineral bone disorder phenotypes among patients on dialysis: a historical cohort study. Nephrology, dialysis, transplantation : official publication of the European Dialysis and Transplant Association - European Renal Association, 34 4:682-691, Aug 2019. URL: https://doi.org/10.1093/ndt/gfy273, doi:10.1093/ndt/gfy273. This article has 13 citations.

11. (thiem2023effectofthe pages 1-3): Ursula Thiem, Tim D Hewitson, Nigel D Toussaint, Stephen G Holt, Maria C Haller, Andreas Pasch, Daniel Cejka, and Edward R Smith. Effect of the phosphate binder sucroferric oxyhydroxide in dialysis patients on endogenous calciprotein particles, inflammation, and vascular cells. Nephrology Dialysis Transplantation, 38:1282-1296, Sep 2023. URL: https://doi.org/10.1093/ndt/gfac271, doi:10.1093/ndt/gfac271. This article has 32 citations and is from a domain leading peer-reviewed journal.

12. (hsu2024riskfactorsfor pages 1-2): Simon Hsu, Nisha Bansal, Michelle Denburg, Charles Ginsberg, Andrew N Hoofnagle, Tamara Isakova, Joachim H Ix, Cassianne Robinson-Cohen, Myles Wolf, Bryan R Kestenbaum, Ian H de Boer, and Leila R Zelnick. Risk factors for hip and vertebral fractures in chronic kidney disease: the cric study. Journal of bone and mineral research : the official journal of the American Society for Bone and Mineral Research, 39:433-442, Feb 2024. URL: https://doi.org/10.1093/jbmr/zjae021, doi:10.1093/jbmr/zjae021. This article has 21 citations.

13. (fuller2020combinationsofmineral pages 1-2): Douglas S Fuller, Paul J Dluzniewski, Kerry Cooper, Brian D Bradbury, Bruce M Robinson, and Francesca Tentori. Combinations of mineral and bone disorder markers and risk of death and hospitalizations in the international dialysis outcomes and practice patterns study. Clinical Kidney Journal, 13:1056-1062, Nov 2020. URL: https://doi.org/10.1093/ckj/sfz112, doi:10.1093/ckj/sfz112. This article has 22 citations and is from a peer-reviewed journal.

14. (simic2024boneandbone pages 1-2): Petra Simic. Bone and bone derived factors in kidney disease. Frontiers in Physiology, Mar 2024. URL: https://doi.org/10.3389/fphys.2024.1356069, doi:10.3389/fphys.2024.1356069. This article has 8 citations.

15. (wheeler2017kdigo2017clinical media ed681c34): DC Wheeler and WC Winkelmayer. Kdigo 2017 clinical practice guideline update for the diagnosis, evaluation, prevention, and treatment of chronic kidney disease-mineral and bone disorder (ckd …. Unknown journal, 2017.

16. (wheeler2017kdigo2017clinical pages 16-18): DC Wheeler and WC Winkelmayer. Kdigo 2017 clinical practice guideline update for the diagnosis, evaluation, prevention, and treatment of chronic kidney disease-mineral and bone disorder (ckd …. Unknown journal, 2017.
