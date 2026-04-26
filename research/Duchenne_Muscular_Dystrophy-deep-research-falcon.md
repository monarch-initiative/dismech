---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:42.239938'
end_time: '2026-04-25T22:25:51.675950'
duration_seconds: 609.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Duchenne Muscular Dystrophy
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Duchenne Muscular Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Duchenne Muscular Dystrophy** covering all of the
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
- **Disease Name:** Duchenne Muscular Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Duchenne Muscular Dystrophy** covering all of the
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


# Duchenne Muscular Dystrophy (DMD): Disease Characteristics Research Report (2023–2025 evidence prioritized)

## Executive summary
Duchenne muscular dystrophy (DMD) is a severe X‑linked recessive dystrophinopathy caused by pathogenic variants in the DMD gene that eliminate functional dystrophin, leading to progressive skeletal muscle degeneration with cardiomyopathy and respiratory failure as major life‑limiting complications. Contemporary registries, claims datasets, and consensus guidelines show: (i) substantial variability in prevalence estimates across countries (roughly ~1.65/100,000 overall in a genetically strict Italian survey vs ~3.23/100,000 in an English claims analysis) (capasso2024prevalenceofduchenne pages 1-2, morgan2024epidemiologyandhealthcare pages 1-2); (ii) respiratory and cardiac management materially affect survival and causes of death (wahlgren2024respiratorycomorbiditiesand pages 1-2); and (iii) the therapeutic landscape is expanding (ataluren real‑world milestone delays in nonsense‑mutation DMD; AAV micro‑dystrophin gene transfer with defined adverse event profiles and management pathways) (mercuri2023safetyandeffectiveness pages 1-2, zaidman2024managementofselect pages 8-11).

A summary of key recent studies/guidelines used in this report is provided in the embedded table.

| Domain | Citation | Publication date | Key quantitative findings | URL | Evidence type |
|---|---|---|---|---|---|
| Epidemiology | Capasso et al., 2024, *European Journal of Pediatrics* | 12/2024 | • Nationwide Italian prevalence: 1.65/100,000 overall; 3.4/100,000 males • Cohort n=972; 57% non-ambulant; ~73% no ventilatory support (capasso2024prevalenceofduchenne pages 5-8, capasso2024prevalenceofduchenne pages 1-2) | https://doi.org/10.1007/s00431-024-05903-x | Nationwide survey/registry-style prevalence study |
| Epidemiology | Morgan et al., 2024, *Journal of Rare Diseases* | 08/2024 | • England point prevalence (2020): 3.23/100,000 (95% CI 2.82–3.63) • Utilization vs controls: inpatient IRR 9.24, outpatient IRR 11.44; adjusted cost ratio 9.33 (morgan2024epidemiologyandhealthcare pages 1-2) | https://doi.org/10.1007/s44162-024-00044-z | Claims database study |
| Epidemiology / prognosis | Wahlgren et al., 2024, *Journal of Neurology* | 04/2024 | • Swedish mortality cohort median lifespan: 24.3 years • 70.1% had ≥1 pneumonia; 73.0% developed hypoventilation; acute respiratory failure caused 63.3% of respiratory-related deaths (wahlgren2024respiratorycomorbiditiesand pages 1-2) | https://doi.org/10.1007/s00415-024-12372-7 | National mortality cohort / registry-linked study |
| Genetics / natural history | Zhao et al., 2024, *Orphanet Journal of Rare Diseases* | 08/2024 | • Cohort n=2,097 dystrophinopathy patients, including 1,703 DMD • Variant spectrum: deletions 66.6%, duplications 10.7%, nonsense 10.3%; glucocorticoids delayed loss of ambulation by median 2.5 years (zhao2024comprehensiveanalysisof pages 1-2) | https://doi.org/10.1186/s13023-024-03217-7 | Large single-center cohort/database study |
| Respiratory care | Childs et al., 2024, *Thorax* | 12/2024 | • Respiratory monitoring recommended every 6–12 months when ambulatory and every 6 months when non-ambulatory • FVC ≤50% predicted should remain under respiratory review; NIV considered with hypoxemia <95% or hypercapnia >45 mmHg/6 kPa (childs2024developmentofrespiratory pages 6-7, childs2024developmentofrespiratory pages 3-3, childs2024developmentofrespiratory pages 1-2) | https://doi.org/10.1136/thorax-2023-220811 | Consensus guideline |
| Treatment—ataluren | Mercuri et al., 2023, *Journal of Neurology* | 04/2023 | • STRIDE registry enrolled 307 patients from 14 countries; mean ataluren exposure 1,671 days • Ataluren + standard care delayed loss of ambulation by 4.0 years and delayed FVC decline <60% by 1.8 years, <50% by 2.3 years (mercuri2023safetyandeffectiveness pages 1-2, mercuri2023safetyandeffectiveness pages 10-11, mercuri2023safetyandeffectiveness pages 6-7) | https://doi.org/10.1007/s00415-023-11687-1 | International registry / real-world comparative study |
| Treatment—AAV gene therapy | Zaidman et al., 2024, *Journal of Neuromuscular Diseases* | 04/2024 | • In 85 treated patients, 96% had TEAEs and 86% had treatment-related AEs; vomiting was most frequent (~50–61%) • Acute liver injury occurred in 31/85 (36%); myocarditis and immune-mediated myositis each ~1/85 (~1%) (zaidman2024managementofselect pages 1-3, zaidman2024managementofselect pages 7-8, zaidman2024managementofselect pages 8-11) | https://doi.org/10.3233/jnd-230185 | Delphi consensus / safety management paper |
| Regulatory / trial guidance | McDonald et al., 2024, *Journal of Neuromuscular Diseases* | 02/2024 | • Birth prevalence summarized as ~1 in 3,500–6,000 males • Guidance emphasizes surrogate-endpoint approvals, post-marketing placebo-controlled trials, and development across the full dystrophinopathy spectrum (mcdonald2024draftguidancefor pages 4-5) | https://doi.org/10.3233/jnd-230219 | FDA/community guidance paper |
| Treatment—AAV gene therapy | D'Ambrosio & Mendell, 2023, *Neurotherapeutics* | 10/2023 | • Reviews delandistrogene moxeparvovec/SRP-9001 programs with >80 treated boys in later development • Reports protocol corticosteroids 1 mg/kg/day starting 24 h pre-infusion and key AEs including vomiting, transaminase/GGT elevations, thrombocytopenia, and immune-mediated myositis/myocarditis in 2 patients with large deletions (dambrosio2023evolvingtherapeuticoptions pages 8-9) | https://doi.org/10.1007/s13311-023-01423-y | Therapeutic review / clinical development overview |


*Table: This table summarizes the main recent studies and guidelines used as evidence in the Duchenne muscular dystrophy report, spanning epidemiology, natural history, respiratory care, and emerging therapies. It is useful for quickly locating the most relevant quantitative findings, publication dates, and evidence types.*

---

## 1. Disease information

### 1.1 Definition and overview
DMD is the most common and most severe dystrophinopathy, resulting from DMD gene mutations that reduce dystrophin or impair its function, rendering muscle cell membranes vulnerable and driving progressive muscle degeneration, inflammation, and fibrosis (mcdonald2024draftguidancefor pages 4-5). Dystrophin is a cytoskeletal protein required for myofiber strength/stability and linkage of the cytoskeleton to the dystrophin‑associated protein complex (DAPC) (zhao2024comprehensiveanalysisof pages 1-2, krishna2024molecularandbiochemical pages 1-2). Clinically, DMD typically begins in early childhood with delayed motor milestones and progressive proximal weakness, then progresses to loss of ambulation and ultimately respiratory and cardiac failure (zhao2024comprehensiveanalysisof pages 1-2, mcdonald2024draftguidancefor pages 4-5).

### 1.2 Key identifiers and ontologies (availability in retrieved evidence)
The requested cross‑ontology identifiers (OMIM, Orphanet, MeSH, ICD‑11, MONDO) were not directly contained in the retrieved full‑text evidence snippets used for this report; therefore they cannot be asserted with tool‑verifiable citations here.

**ICD‑10 (administrative data use):** In German claims analyses, ICD‑10 code **G71.0** (“muscular dystrophy”) is commonly used as an initial filter, but it is non‑specific and includes multiple muscular dystrophies beyond DMD; studies therefore require additional algorithmic criteria (e.g., glucocorticoid use in childhood, early wheelchair use, cardiomyopathy/heart medication, ventilation) to improve DMD specificity (diesing2025epidemiologydiseaseburden pages 2-4).

### 1.3 Synonyms / alternative names
Within the retrieved sources, DMD is frequently discussed under the umbrella term **“dystrophinopathies”** (including Duchenne muscular dystrophy, Becker muscular dystrophy, and dystrophin‑associated dilated cardiomyopathy) (krishna2024molecularandbiochemical pages 1-2). Additional synonym lists (e.g., “Duchenne dystrophy,” “pseudohypertrophic muscular dystrophy”) were not explicitly enumerated in the retrieved evidence.

### 1.4 Evidence provenance (patient‑level vs aggregated)
The evidence base used here includes aggregated resources (consensus guidelines and regulatory guidance) (mcdonald2024draftguidancefor pages 4-5, childs2024developmentofrespiratory pages 1-2), patient registries (STRIDE ataluren registry) (mercuri2023safetyandeffectiveness pages 1-2), national mortality/registry linkages (Sweden) (wahlgren2024respiratorycomorbiditiesand pages 1-2), nationwide prevalence ascertainment from specialist centers (Italy) (capasso2024prevalenceofduchenne pages 1-2), and administrative claims/EHR‑derived cohorts (England; Germany) (morgan2024epidemiologyandhealthcare pages 1-2, diesing2025epidemiologydiseaseburden pages 2-4).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** Germline pathogenic variants in the **DMD** gene on the X chromosome causing absent/reduced dystrophin protein (zaidman2024managementofselect pages 1-3).

**Inheritance:** X‑linked recessive (explicitly described as “recessive X‑linked” in recent gene‑therapy safety literature) (zaidman2024managementofselect pages 1-3).

### 2.2 Genetic risk factors: variant spectrum and genotype correlations
A large 2024 Chinese dystrophinopathy cohort (n=2,097; DMD n=1,703) reported the following **variant class distribution**: exonic deletions 66.6%, exonic duplications 10.7%, nonsense variants 10.3%, splice‑site variants 4.5%, small deletions 3.5%, small insertions/duplications 1.8%, missense variants 0.9%, plus rare deep intronic and inversion variants (zhao2024comprehensiveanalysisof pages 1-2). In the same cohort, **55.3%** of DMD patients were estimated to be eligible for exon‑skipping therapy overall (with **12.9%** eligible for exon 51 skipping, **10%** for exon 53 skipping, and **9.6%** for exon 45 skipping) (zhao2024comprehensiveanalysisof pages 1-2).

**Direct abstract quote (variant spectrum):** “The spectrum of identified variants included exonic deletions (66.6%), exonic duplications (10.7%), nonsense variants (10.3%), splice-site variants (4.5%), small deletions (3.5%), small insertions/duplications (1.8%), and missense variants (0.9%).” (zhao2024comprehensiveanalysisof pages 1-2)

### 2.3 Modifier genes / protective genetic factors (current evidence limitations)
Recent evidence in this tool run does not provide a comprehensive modifier‑gene review. One 2024 systematic review of predictors of cardiac disease in DMD (identified during search but not extracted here in the evidence snippets) is referenced in the state; however, modifier gene details were not returned in the gathered evidence. Therefore, a modifier gene list cannot be asserted with citations from this run.

### 2.4 Environmental and lifestyle risk factors / protective factors
DMD is a monogenic disorder; no environmental causal factors were identified in the retrieved evidence. However, care guidelines and observational studies note clinical factors that can worsen respiratory risk (e.g., overweight/Cushingoid features, often steroid‑related) even when pulmonary testing appears stable (childs2024developmentofrespiratory pages 3-3). This represents risk for complications rather than disease causation.

### 2.5 Gene–environment interactions
No explicit gene–environment interaction studies were captured in the retrieved evidence.

---

## 3. Phenotypes (clinical presentation, progression, and HPO suggestions)

### 3.1 Core neuromuscular phenotype
Typical onset is **before age 5 years**, with progression to wheelchair dependence often by **10–12 years** and death commonly from cardiac/respiratory failure between **20–40 years** (zhao2024comprehensiveanalysisof pages 1-2). Without disease‑modifying therapy, loss of ambulation is commonly before age 13 (mcdonald2024draftguidancefor pages 4-5).

**Suggested HPO terms (non‑exhaustive; not directly extracted from HPO in this run):**
- Progressive muscle weakness (HP:0003323)
- Proximal muscle weakness (HP:0008997)
- Delayed gross motor development (HP:0002194)
- Loss of ambulation (HP:0002505)

### 3.2 Respiratory phenotype
DMD respiratory decline is primarily due to intercostal and diaphragmatic weakness and tends to become clinically apparent after loss of ambulation; inspiratory weakness leads to nocturnal hypoventilation/sleep‑disordered breathing, and expiratory weakness causes ineffective cough and secretion clearance (childs2024developmentofrespiratory pages 1-2).

A Swedish mortality cohort found respiratory comorbidity is common: **70.1%** had ≥1 pneumonia (median age at first pneumonia **17.8 years**), and **73.0%** developed hypoventilation (median onset **18.1 years**) (wahlgren2024respiratorycomorbiditiesand pages 1-2). Acute respiratory failure accounted for **63.3%** of respiratory‑related deaths (wahlgren2024respiratorycomorbiditiesand pages 1-2).

**Suggested HPO terms:**
- Hypoventilation (HP:0002791)
- Sleep apnea / sleep-disordered breathing (e.g., HP:0010535)
- Recurrent respiratory infections / pneumonia (HP:0006532 / HP:0002090)

### 3.3 Cardiac phenotype
Consensus regulatory guidance emphasizes cardiomyopathy as a prominent life‑limiting feature in DMD, and notes that heart disease is now a leading cause of death as respiratory management has improved (mcdonald2024draftguidancefor pages 4-5).

**Suggested HPO terms:**
- Dilated cardiomyopathy (HP:0001644)
- Left ventricular systolic dysfunction (HP:0032094)

### 3.4 Quality‑of‑life impact
Direct quantitative HRQoL instruments (e.g., EQ‑5D, PedsQL) were not extracted in the evidence snippets. Functional milestones and respiratory/cardiac complications documented in cohort studies imply substantial impacts on mobility, independence, and survival (mcdonald2024draftguidancefor pages 4-5, wahlgren2024respiratorycomorbiditiesand pages 1-2).

---

## 4. Genetic / molecular information

### 4.1 Causal gene
- **DMD** (dystrophin) is the causal gene; dystrophin is described as a large protein linking the cytoskeleton to the dystrophin‑associated protein complex (DAPC), supporting membrane stability (krishna2024molecularandbiochemical pages 1-2).

### 4.2 Functional consequences
Loss of functional dystrophin causes muscle membrane instability and progressive skeletal/cardiac muscle atrophy (krishna2024molecularandbiochemical pages 1-2). Regulatory guidance further frames the downstream cascade as progressive degeneration with inflammation and fibrosis driven by membrane vulnerability (mcdonald2024draftguidancefor pages 4-5).

### 4.3 Variant types and testing approaches (high level)
Clinical molecular diagnosis commonly uses methods capable of detecting large deletions/duplications such as MLPA or array‑CGH, consistent with the high proportion of structural variation (krishna2024molecularandbiochemical pages 1-2, zhao2024comprehensiveanalysisof pages 1-2).

---

## 5. Environmental information
No infectious etiology or environmental cause is applicable for DMD in the retrieved evidence.

---

## 6. Mechanism / pathophysiology (with ontology suggestions)

### 6.1 Causal chain (current understanding)
1) **Pathogenic DMD variant → dystrophin absent/reduced** (zaidman2024managementofselect pages 1-3).
2) **Loss of dystrophin/DAPC linkage → membrane vulnerability** (mcdonald2024draftguidancefor pages 4-5, krishna2024molecularandbiochemical pages 1-2).
3) **Repeated contraction injury → myofiber degeneration → inflammation and fibrosis** (mcdonald2024draftguidancefor pages 4-5).
4) **Organ-level failure:** progressive skeletal muscle weakness, respiratory muscle weakness (nocturnal hypoventilation, cough failure), and cardiomyopathy leading to morbidity and premature mortality (mcdonald2024draftguidancefor pages 4-5, childs2024developmentofrespiratory pages 1-2, wahlgren2024respiratorycomorbiditiesand pages 1-2).

### 6.2 Pathways and cellular processes highlighted in retrieved sources
- **Inflammation and fibrosis** are explicitly emphasized as downstream processes in regulatory guidance for dystrophinopathies (mcdonald2024draftguidancefor pages 4-5).
- Mechanistic rationale for cardioprotective drugs includes angiotensin II‑mediated **oxidative stress and fibrosis** in cardiomyopathy (review evidence) (krishna2024molecularandbiochemical pages 23-25).

### 6.3 Ontology suggestions
**GO biological process (examples):**
- Muscle cell differentiation / muscle adaptation
- Inflammatory response
- Extracellular matrix organization / fibrosis

**Cell Ontology (CL) candidates:**
- Skeletal muscle cell / myofiber (CL:0000187)
- Cardiomyocyte (CL:0000746)

**UBERON anatomy:**
- Skeletal muscle organ (UBERON:0001134)
- Heart (UBERON:0000948)
- Diaphragm (UBERON:0001103)

(These ontology IDs are provided as plausible mappings; they were not directly looked up in this tool run and therefore are not citation-supported here.)

---

## 7. Anatomical structures affected
Primary tissues are skeletal muscle and cardiac muscle; respiratory insufficiency reflects involvement of diaphragm and intercostal muscles (childs2024developmentofrespiratory pages 1-2, mcdonald2024draftguidancefor pages 4-5). Multi‑organ involvement is also noted in gene‑therapy safety literature (zaidman2024managementofselect pages 1-3).

---

## 8. Temporal development (onset and progression)
- **Onset:** typically before age 5 (zhao2024comprehensiveanalysisof pages 1-2).
- **Progression:** wheelchair dependence often by 10–12 years (zhao2024comprehensiveanalysisof pages 1-2); respiratory decline becomes prominent after loss of ambulation, often in adolescence/adulthood (childs2024developmentofrespiratory pages 1-2).
- **Respiratory milestones:** in Sweden, median onset of hypoventilation ~18.1 years and first pneumonia ~17.8 years (wahlgren2024respiratorycomorbiditiesand pages 1-2).

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent estimates)
Estimates vary by ascertainment method and denominators:
- **Italy (nationwide survey; Jan 2021–Dec 2023 follow‑up):** period prevalence **1.65/100,000 overall** and **3.4/100,000 males** (capasso2024prevalenceofduchenne pages 1-2). Cohort characteristics included **43% ambulant** and **57% non‑ambulant** (capasso2024prevalenceofduchenne pages 1-2).
- **England (CPRD Aurum; 2020 point prevalence):** **3.23/100,000** (95% CI 2.82–3.63) (morgan2024epidemiologyandhealthcare pages 1-2).
- **Global birth prevalence range (regulatory guidance):** approximately **1 in 3,500–6,000 males** (mcdonald2024draftguidancefor pages 4-5).
- **China (cohort context statement):** worldwide live male birth prevalence cited as ~1 in 3,600–6,300; China estimate cited as 1 in 4,560 (zhao2024comprehensiveanalysisof pages 1-2).

### 9.2 Healthcare utilization and cost (real‑world)
In England claims data, DMD was associated with much higher healthcare utilization than matched controls: primary care contacts IRR **3.19**, inpatient admissions IRR **9.24**, outpatient appointments IRR **11.44**, and adjusted cost ratio **9.33** (morgan2024epidemiologyandhealthcare pages 1-2). Stage‑linked mean annual costs were reported as **£2,816** (ambulatory), **£5,700** (non‑ambulatory without ventilation), and **£7,634** (non‑ambulatory with ventilation) (morgan2024epidemiologyandhealthcare pages 1-2).

### 9.3 Sex ratio
As an X‑linked recessive condition, DMD predominantly affects males; multiple cohorts in this report are male-only by design (wahlgren2024respiratorycomorbiditiesand pages 1-2, zhao2024comprehensiveanalysisof pages 1-2).

---

## 10. Diagnostics

### 10.1 Core diagnostic approach (from retrieved sources)
Molecular testing approaches capable of detecting deletions/duplications are emphasized (MLPA, array‑CGH) (krishna2024molecularandbiochemical pages 1-2). Large cohort data show deletions/duplications constitute the majority of pathogenic variation, supporting this strategy (zhao2024comprehensiveanalysisof pages 1-2).

### 10.2 Respiratory monitoring as part of longitudinal assessment (2024 UK guideline)
The 2024 UK BTS‑endorsed consensus guideline recommends routine respiratory surveillance beginning as soon as feasible after diagnosis and typically performed routinely by age 6 (childs2024developmentofrespiratory pages 2-3). Suggested monitoring frequency is every **6–12 months** while ambulatory and every **6 months** when non‑ambulatory (childs2024developmentofrespiratory pages 3-3). Minimum assessment includes targeted history, FVC, and peak cough flow (childs2024developmentofrespiratory pages 3-3).

Key threshold‑linked recommendations include:
- Patients with **FVC ≤50% predicted** “should remain under respiratory review and should not be discharged from respiratory clinics” (childs2024developmentofrespiratory pages 6-7).
- The guideline cautions that “daytime saturations should not be relied on to diagnose or rule out ventilatory failure” (childs2024developmentofrespiratory pages 6-7).

In emergency/acute settings, the guideline excerpt advises considering NIV with hypoxemia (<95%), hypercapnia (>45 mm Hg / 6 kPa), or clinical fatigue, and warns against giving oxygen alone without checking for hypercapnia (childs2024developmentofrespiratory pages 8-8).

### 10.3 Early diagnosis / screening
Newborn screening and formal early‑diagnosis pathways were not captured in full within the retrieved evidence snippets. One preprint model notes that affected status can be determined at birth and references newborn screening pilots in discussion, but it does not provide implementable screening protocols in the extracted text (kingsmore2024mathematicalmodelingof pages 8-10).

---

## 11. Outcomes / prognosis

### 11.1 Survival and causes of death (recent cohort data)
In Sweden (males born/deceased 1970–2019; n=129), median lifespan was **24.3 years**, with pneumonia and hypoventilation common and acute respiratory failure responsible for **63.3%** of respiratory‑related causes of death (wahlgren2024respiratorycomorbiditiesand pages 1-2). The authors note that assisted ventilation and combined respiratory/cardiac management have been associated with improved life expectancy in modern eras (wahlgren2024respiratorycomorbiditiesand pages 1-2).

### 11.2 Disease milestones and supportive technology utilization (Italy)
In the Italian nationwide survey, ~**73%** had no ventilatory support, **9%** had NIV >12 hours, and **1.4%** had tracheostomy at last assessment; median age at any respiratory support was **18 years** (capasso2024prevalenceofduchenne pages 5-8).

---

## 12. Treatment

### 12.1 Standard of care / supportive care (respiratory)
The 2024 UK guideline emphasizes multidisciplinary respiratory care with ongoing surveillance and early recognition of sleep‑disordered breathing, cough weakness, and infection risk; it recommends prompt referral to specialist respiratory physiotherapy and anticipatory prescription of assisted cough devices (MI‑E settings individualized by experts) (childs2024developmentofrespiratory pages 6-7, childs2024developmentofrespiratory pages 8-9).

**MAXO suggestions (not directly mapped in evidence):** noninvasive ventilation; mechanically assisted cough; respiratory physiotherapy.

### 12.2 Glucocorticoids
Regulatory guidance and cohort data support glucocorticoids as disease‑modifying therapy that shifts milestone timing but carries important adverse effects (weight gain, growth inhibition, bone fragility/fractures, diabetes risk, behavioral changes, Cushingoid features, puberty effects, cataracts) (mcdonald2024draftguidancefor pages 4-5).

In the 2024 Chinese cohort, glucocorticoid treatment was associated with a **median 2.5‑year delay** in loss of ambulation (zhao2024comprehensiveanalysisof pages 1-2).

### 12.3 Variant‑targeted therapies

#### 12.3.1 Stop‑codon readthrough (ataluren) in nonsense‑mutation DMD (real‑world)
The STRIDE registry (NCT02369731) reported, as of Jan 31, 2022, 307 patients enrolled from 14 countries with mean ages at first symptoms **2.9 years** and genetic diagnosis **4.5 years** and mean ataluren exposure **1671 days** (mercuri2023safetyandeffectiveness pages 1-2). In propensity‑matched comparisons vs CINRG natural history, ataluren + standard of care delayed:
- **Loss of ambulation by ~4 years** (median 17.0 vs 13.0 years; p<0.0001) (mercuri2023safetyandeffectiveness pages 10-11, mercuri2023safetyandeffectiveness pages 11-13)
- Decline to **FVC <60% by 1.8 years** and **FVC <50% by 2.3 years** (mercuri2023safetyandeffectiveness pages 1-2, mercuri2023safetyandeffectiveness pages 10-11)

**Direct abstract quote (effectiveness):** “Kaplan–Meier analyses demonstrated that ataluren plus SoC significantly delayed age at loss of ambulation by 4 years … and age at decline to %-predicted forced vital capacity of <60% and <50% by 1.8 years … and 2.3 years … compared with SoC alone.” (mercuri2023safetyandeffectiveness pages 1-2)

Safety findings included that ataluren was well tolerated in the registry with no deaths to cutoff and relatively low proportions of TEAEs judged related to ataluren (3.2% of TEAEs related) (mercuri2023safetyandeffectiveness pages 6-7).

#### 12.3.2 Exon‑skipping antisense oligonucleotides (ASOs)
A 2024 mechanistic review summarizes exon‑skipping PMO therapies (eteplirsen exon 51; golodirsen exon 53; casimersen exon 45) as producing internally shortened dystrophin by restoring the reading frame, with limitations including variable dystrophin restoration and, for golodirsen, historical FDA concerns about renal toxicity (krishna2024molecularandbiochemical pages 5-7).

Real‑world implementation gaps are suggested by cohort/claims contexts rather than head‑to‑head effectiveness in the retrieved evidence: in China, although >55% were exon‑skipping eligible, the report emphasizes gaps in routine monitoring and treatment uptake (zhao2024comprehensiveanalysisof pages 1-2).

### 12.4 AAV micro‑dystrophin gene transfer: delandistrogene moxeparvovec (SRP‑9001)

#### 12.4.1 Indication and real‑world implementation considerations
A 2024 Delphi consensus paper states that delandistrogene moxeparvovec is indicated for **ambulatory pediatric patients aged 4–5 years** with an indicated DMD mutation (zaidman2024managementofselect pages 1-3).

#### 12.4.2 Safety signals and management (2024 consensus)
The Delphi panel focused on treatment‑related adverse events (TRAEs) including vomiting, acute liver injury (ALI), myocarditis, and immune‑mediated myositis (IMM) and recommended baseline lab assessments (CMP including AST/ALT/bilirubin; troponin; complement; CBC; coagulation; cystatin C, etc.) and post‑infusion serial monitoring (weekly liver enzymes for ~3 months; weekly troponin during first month; weekly platelets for first 2 weeks) (zaidman2024managementofselect pages 3-4).

In clinical development safety data summarized by the consensus paper (n=85), vomiting was the most frequent TRAE (reported ~50–61%); ALI occurred in **31/85 (36%)** typically 4–8 weeks post infusion; myocarditis and IMM were each **~1/85 (~1%)** (zaidman2024managementofselect pages 8-11). Management principles included prompt escalation of corticosteroids for immune‑mediated events and specialist consultation; refractory cases may require IV methylprednisolone, IVIg, or plasmapheresis (zaidman2024managementofselect pages 8-11, zaidman2024managementofselect pages 6-7).

A 2023 therapeutic review provides additional clinical development context, noting immune‑mediated myositis with myocarditis in two patients with large exon deletions in early programs, managed with intensified immunosuppression (prednisone, plasmapheresis, tacrolimus), and those mutation classes were subsequently excluded (dambrosio2023evolvingtherapeuticoptions pages 8-9).

---

## 13. Prevention
Primary prevention is not applicable because DMD is inherited; prevention focuses on genetic counseling and family planning. No prevention guidelines or carrier screening/newborn screening program details were captured in the retrieved evidence snippets.

---

## 14. Other species / natural disease
Naturally occurring animal disease and veterinary relevance were not captured in the retrieved evidence snippets in this run.

---

## 15. Model organisms
This tool run did not extract specific model‑organism descriptions (e.g., mdx mouse, dystrophic dogs) beyond general mentions in therapeutic reviews that preclinical efficacy has been demonstrated in mdx mice and dystrophic dogs for micro‑dystrophin approaches (krishna2024molecularandbiochemical pages 5-7). A structured model‑organism section would require additional targeted retrieval.

---

## Expert opinions and authoritative analysis (as captured in recent guidance)
- The 2024 FDA/community draft guidance emphasizes patient‑focused drug development, the role of dystrophin as a biomarker, MRI for progression assessment, cardiomyopathy prominence, and the evolving field of gene therapy (mcdonald2024draftguidancefor pages 4-5). It also explicitly notes that several exon‑skipping drugs were approved using surrogate endpoints and encourages completion of post‑marketing placebo‑controlled trials (mcdonald2024draftguidancefor pages 4-5).
- The 2024 UK BTS‑endorsed respiratory guideline highlights gaps and inconsistencies in care provision and provides consensus flow‑based recommendations for routine and emergency respiratory management (childs2024developmentofrespiratory pages 1-2).

---

## Data gaps and limitations (important for knowledge base curation)
1) **Ontology identifiers (MONDO/OMIM/Orphanet/MeSH/ICD‑11)** were not available in the retrieved evidence snippets; they should be populated from dedicated ontology sources (OMIM/Orphanet/MONDO) in a subsequent retrieval step.
2) **Modifier genes, epigenetics, and multi‑omics** were not comprehensively captured in extracted evidence in this run.
3) **Newborn screening and carrier screening** details were not retrieved with implementable specificity.
4) **Model organism and natural animal disease** evidence is incomplete.

---

## URLs and publication dates (where available)
URLs and month/year publication dates for the major cited sources are included in the table artifact embedded above (artifact-00) and in citations throughout the text.


References

1. (capasso2024prevalenceofduchenne pages 1-2): Anna Capasso, Gianpaolo Cicala, Martina Ricci, Marika Pane, Adele D’Amico, Claudio Bruno, Valeria Ada Sansone, Sonia Messina, Luca Bello, Elena Pegoraro, Maria Grazia D’Angelo, Riccardo Masson, Angela Berardinelli, Antonella Pini, Federica Ricci, Tiziana Enrica Mongini, Michela Coccia, Vincenzo Nigro, Antonio Trabacca, Massimiliano Filosto, Giacomo Comi, Francesca Magri, Andrea Barp, Roberta Battini, Stefano Carlo Previtali, Maria Lucia Valentino, Eleonora Diella, Claudia Dosi, Lucia Ruggiero, Gabriele Siciliano, Giulia Ricci, Michela Catteruccia, Chiara Arpaia, Giorgia Coratti, Giulia Norcia, Silvia Bonanno, Lorenzo Verriello, Caterina Agosto, Antonio Varone, Alessandra Ferlini, Maria Antonietta Maioli, Claudia Brogna, Sabrina Siliquini, Irene Bruno, Chiara Panicucci, Cosimo Allegra, Emilio Albamonte, Eugenio Mercuri, Concetta Palermo, Daniela Leone, Costanza Cutrona, Laura Antonaci, Simona Lucibello, Elisabetta Ferraroli, Maria Carmela Pera, Giulia Stanca, Bianca Buchignani, Lorenzo Maggi, Enrico Bertini, Giacomo de Luca, Marina Pedemonte, Federica Trucco, Melania Giannotta, Riccardo Zanin, Maria Sframeli, Alessandra Nastasi, Simona Damioli, Alice Gardani, Riccardo Zuccarino, Alberto A. Zambon, Amanda Ferrero, and Giorgia Bruno. Prevalence of duchenne muscular dystrophy in italy: a nationwide survey. European journal of pediatrics, 184 1:86, Dec 2024. URL: https://doi.org/10.1007/s00431-024-05903-x, doi:10.1007/s00431-024-05903-x. This article has 4 citations and is from a peer-reviewed journal.

2. (morgan2024epidemiologyandhealthcare pages 1-2): Christopher Llewellyn Morgan, Josie Godfrey, Fleur Chandler, Emily Reuben, and Craig J. Currie. Epidemiology and healthcare resource utilisation associated with duchenne muscular dystrophy. Journal of Rare Diseases, Aug 2024. URL: https://doi.org/10.1007/s44162-024-00044-z, doi:10.1007/s44162-024-00044-z. This article has 4 citations.

3. (wahlgren2024respiratorycomorbiditiesand pages 1-2): Lisa Wahlgren, Anna-Karin Kroksmark, Anders Lindblad, Mar Tulinius, and Kalliopi Sofou. Respiratory comorbidities and treatments in duchenne muscular dystrophy: impact on life expectancy and causes of death. Journal of Neurology, 271:4300-4309, Apr 2024. URL: https://doi.org/10.1007/s00415-024-12372-7, doi:10.1007/s00415-024-12372-7. This article has 26 citations and is from a domain leading peer-reviewed journal.

4. (mercuri2023safetyandeffectiveness pages 1-2): Eugenio Mercuri, Andrés Nascimento Osorio, Francesco Muntoni, Filippo Buccella, Isabelle Desguerre, Janbernd Kirschner, Már Tulinius, Maria Bernadete Dutra de Resende, Lauren P. Morgenroth, Heather Gordish-Dressman, Shelley Johnson, Allan Kristensen, Christian Werner, Panayiota Trifillis, Erik K. Henricson, and Craig M. McDonald. Safety and effectiveness of ataluren in patients with nonsense mutation dmd in the stride registry compared with the cinrg duchenne natural history study (2015–2022): 2022 interim analysis. Journal of Neurology, 270:3896-3913, Apr 2023. URL: https://doi.org/10.1007/s00415-023-11687-1, doi:10.1007/s00415-023-11687-1. This article has 57 citations and is from a domain leading peer-reviewed journal.

5. (zaidman2024managementofselect pages 8-11): Craig M. Zaidman, Natalie L. Goedeker, Amal A. Aqul, Russell J. Butterfield, Anne M. Connolly, Ronald G. Crystal, Kara E. Godwin, Kan N. Hor, Katherine D. Mathews, Crystal M. Proud, Elizabeth Kula Smyth, Aravindhan Veerapandiyan, Paul B. Watkins, and Jerry R. Mendell. Management of select adverse events following delandistrogene moxeparvovec gene therapy for patients with duchenne muscular dystrophy. Journal of Neuromuscular Diseases, 11:687-699, Apr 2024. URL: https://doi.org/10.3233/jnd-230185, doi:10.3233/jnd-230185. This article has 22 citations and is from a peer-reviewed journal.

6. (capasso2024prevalenceofduchenne pages 5-8): Anna Capasso, Gianpaolo Cicala, Martina Ricci, Marika Pane, Adele D’Amico, Claudio Bruno, Valeria Ada Sansone, Sonia Messina, Luca Bello, Elena Pegoraro, Maria Grazia D’Angelo, Riccardo Masson, Angela Berardinelli, Antonella Pini, Federica Ricci, Tiziana Enrica Mongini, Michela Coccia, Vincenzo Nigro, Antonio Trabacca, Massimiliano Filosto, Giacomo Comi, Francesca Magri, Andrea Barp, Roberta Battini, Stefano Carlo Previtali, Maria Lucia Valentino, Eleonora Diella, Claudia Dosi, Lucia Ruggiero, Gabriele Siciliano, Giulia Ricci, Michela Catteruccia, Chiara Arpaia, Giorgia Coratti, Giulia Norcia, Silvia Bonanno, Lorenzo Verriello, Caterina Agosto, Antonio Varone, Alessandra Ferlini, Maria Antonietta Maioli, Claudia Brogna, Sabrina Siliquini, Irene Bruno, Chiara Panicucci, Cosimo Allegra, Emilio Albamonte, Eugenio Mercuri, Concetta Palermo, Daniela Leone, Costanza Cutrona, Laura Antonaci, Simona Lucibello, Elisabetta Ferraroli, Maria Carmela Pera, Giulia Stanca, Bianca Buchignani, Lorenzo Maggi, Enrico Bertini, Giacomo de Luca, Marina Pedemonte, Federica Trucco, Melania Giannotta, Riccardo Zanin, Maria Sframeli, Alessandra Nastasi, Simona Damioli, Alice Gardani, Riccardo Zuccarino, Alberto A. Zambon, Amanda Ferrero, and Giorgia Bruno. Prevalence of duchenne muscular dystrophy in italy: a nationwide survey. European journal of pediatrics, 184 1:86, Dec 2024. URL: https://doi.org/10.1007/s00431-024-05903-x, doi:10.1007/s00431-024-05903-x. This article has 4 citations and is from a peer-reviewed journal.

7. (zhao2024comprehensiveanalysisof pages 1-2): Lei Zhao, Yiyun Shi, Chaoping Hu, Shuizhen Zhou, Hui Li, Lifeng Zhang, Chuang Qian, Yiyao Zhou, Yi Wang, and Xihua Li. Comprehensive analysis of 2097 patients with dystrophinopathy based on a database from 2011 to 2021. Orphanet Journal of Rare Diseases, Aug 2024. URL: https://doi.org/10.1186/s13023-024-03217-7, doi:10.1186/s13023-024-03217-7. This article has 4 citations and is from a peer-reviewed journal.

8. (childs2024developmentofrespiratory pages 6-7): Anne-Marie Childs, Catherine Turner, Ronan Astin, Stephen Bianchi, John Bourke, Vicki Cunningham, Lisa Edel, Christopher Edwards, Phillippa Farrant, Jane Heraghty, Meredith James, Charlotte Massey, Ben Messer, Jassi Michel Sodhi, Patrick Brian Murphy, Marianela Schiava, Ajit Thomas, Federica Trucco, and Michela Guglieri. Development of respiratory care guidelines for duchenne muscular dystrophy in the uk: key recommendations for clinical practice. Thorax, 79:476-485, Dec 2024. URL: https://doi.org/10.1136/thorax-2023-220811, doi:10.1136/thorax-2023-220811. This article has 24 citations and is from a domain leading peer-reviewed journal.

9. (childs2024developmentofrespiratory pages 3-3): Anne-Marie Childs, Catherine Turner, Ronan Astin, Stephen Bianchi, John Bourke, Vicki Cunningham, Lisa Edel, Christopher Edwards, Phillippa Farrant, Jane Heraghty, Meredith James, Charlotte Massey, Ben Messer, Jassi Michel Sodhi, Patrick Brian Murphy, Marianela Schiava, Ajit Thomas, Federica Trucco, and Michela Guglieri. Development of respiratory care guidelines for duchenne muscular dystrophy in the uk: key recommendations for clinical practice. Thorax, 79:476-485, Dec 2024. URL: https://doi.org/10.1136/thorax-2023-220811, doi:10.1136/thorax-2023-220811. This article has 24 citations and is from a domain leading peer-reviewed journal.

10. (childs2024developmentofrespiratory pages 1-2): Anne-Marie Childs, Catherine Turner, Ronan Astin, Stephen Bianchi, John Bourke, Vicki Cunningham, Lisa Edel, Christopher Edwards, Phillippa Farrant, Jane Heraghty, Meredith James, Charlotte Massey, Ben Messer, Jassi Michel Sodhi, Patrick Brian Murphy, Marianela Schiava, Ajit Thomas, Federica Trucco, and Michela Guglieri. Development of respiratory care guidelines for duchenne muscular dystrophy in the uk: key recommendations for clinical practice. Thorax, 79:476-485, Dec 2024. URL: https://doi.org/10.1136/thorax-2023-220811, doi:10.1136/thorax-2023-220811. This article has 24 citations and is from a domain leading peer-reviewed journal.

11. (mercuri2023safetyandeffectiveness pages 10-11): Eugenio Mercuri, Andrés Nascimento Osorio, Francesco Muntoni, Filippo Buccella, Isabelle Desguerre, Janbernd Kirschner, Már Tulinius, Maria Bernadete Dutra de Resende, Lauren P. Morgenroth, Heather Gordish-Dressman, Shelley Johnson, Allan Kristensen, Christian Werner, Panayiota Trifillis, Erik K. Henricson, and Craig M. McDonald. Safety and effectiveness of ataluren in patients with nonsense mutation dmd in the stride registry compared with the cinrg duchenne natural history study (2015–2022): 2022 interim analysis. Journal of Neurology, 270:3896-3913, Apr 2023. URL: https://doi.org/10.1007/s00415-023-11687-1, doi:10.1007/s00415-023-11687-1. This article has 57 citations and is from a domain leading peer-reviewed journal.

12. (mercuri2023safetyandeffectiveness pages 6-7): Eugenio Mercuri, Andrés Nascimento Osorio, Francesco Muntoni, Filippo Buccella, Isabelle Desguerre, Janbernd Kirschner, Már Tulinius, Maria Bernadete Dutra de Resende, Lauren P. Morgenroth, Heather Gordish-Dressman, Shelley Johnson, Allan Kristensen, Christian Werner, Panayiota Trifillis, Erik K. Henricson, and Craig M. McDonald. Safety and effectiveness of ataluren in patients with nonsense mutation dmd in the stride registry compared with the cinrg duchenne natural history study (2015–2022): 2022 interim analysis. Journal of Neurology, 270:3896-3913, Apr 2023. URL: https://doi.org/10.1007/s00415-023-11687-1, doi:10.1007/s00415-023-11687-1. This article has 57 citations and is from a domain leading peer-reviewed journal.

13. (zaidman2024managementofselect pages 1-3): Craig M. Zaidman, Natalie L. Goedeker, Amal A. Aqul, Russell J. Butterfield, Anne M. Connolly, Ronald G. Crystal, Kara E. Godwin, Kan N. Hor, Katherine D. Mathews, Crystal M. Proud, Elizabeth Kula Smyth, Aravindhan Veerapandiyan, Paul B. Watkins, and Jerry R. Mendell. Management of select adverse events following delandistrogene moxeparvovec gene therapy for patients with duchenne muscular dystrophy. Journal of Neuromuscular Diseases, 11:687-699, Apr 2024. URL: https://doi.org/10.3233/jnd-230185, doi:10.3233/jnd-230185. This article has 22 citations and is from a peer-reviewed journal.

14. (zaidman2024managementofselect pages 7-8): Craig M. Zaidman, Natalie L. Goedeker, Amal A. Aqul, Russell J. Butterfield, Anne M. Connolly, Ronald G. Crystal, Kara E. Godwin, Kan N. Hor, Katherine D. Mathews, Crystal M. Proud, Elizabeth Kula Smyth, Aravindhan Veerapandiyan, Paul B. Watkins, and Jerry R. Mendell. Management of select adverse events following delandistrogene moxeparvovec gene therapy for patients with duchenne muscular dystrophy. Journal of Neuromuscular Diseases, 11:687-699, Apr 2024. URL: https://doi.org/10.3233/jnd-230185, doi:10.3233/jnd-230185. This article has 22 citations and is from a peer-reviewed journal.

15. (mcdonald2024draftguidancefor pages 4-5): Craig M McDonald, Eric Camino, Rafael Escandon, Richard S. Finkel, Ryan Fischer, Kevin M. Flanigan, Pat Furlong, Rose Juhasz, Ann S Martin, Chet Villa, and H. L. Sweeney. Draft guidance for industry duchenne muscular dystrophy, becker muscular dystrophy, and related dystrophinopathies – developing potential treatments for the entire spectrum of disease. Journal of Neuromuscular Diseases, 11:499-523, Feb 2024. URL: https://doi.org/10.3233/jnd-230219, doi:10.3233/jnd-230219. This article has 14 citations and is from a peer-reviewed journal.

16. (dambrosio2023evolvingtherapeuticoptions pages 8-9): Eleonora S. D'Ambrosio and Jerry R. Mendell. Evolving therapeutic options for the treatment of duchenne muscular dystrophy. Neurotherapeutics, 20:1669-1681, Oct 2023. URL: https://doi.org/10.1007/s13311-023-01423-y, doi:10.1007/s13311-023-01423-y. This article has 38 citations and is from a peer-reviewed journal.

17. (krishna2024molecularandbiochemical pages 1-2): Lakshmi Krishna, Akila Prashant, Yogish H. Kumar, Shasthara Paneyala, Siddaramappa J. Patil, Shobha Chikkavaddaragudi Ramachandra, and Prashant Vishwanath. Molecular and biochemical therapeutic strategies for duchenne muscular dystrophy. Neurology International, 16:731-760, Jul 2024. URL: https://doi.org/10.3390/neurolint16040055, doi:10.3390/neurolint16040055. This article has 17 citations.

18. (diesing2025epidemiologydiseaseburden pages 2-4): J. Diesing, Jan Kirschner, A. Pechmann, Jörg König, Leonie Kunk, Tarcyane Barata Garcia, C. Schwedhelm, Carsta Militzer-Horstmann, Ivonne Hänsel, and A. Kisser. Epidemiology, disease burden and costs of duchenne muscular dystrophy in germany: an observational, retrospective health claims data analysis. Orphanet Journal of Rare Diseases, Aug 2025. URL: https://doi.org/10.1186/s13023-025-03906-x, doi:10.1186/s13023-025-03906-x. This article has 4 citations and is from a peer-reviewed journal.

19. (krishna2024molecularandbiochemical pages 23-25): Lakshmi Krishna, Akila Prashant, Yogish H. Kumar, Shasthara Paneyala, Siddaramappa J. Patil, Shobha Chikkavaddaragudi Ramachandra, and Prashant Vishwanath. Molecular and biochemical therapeutic strategies for duchenne muscular dystrophy. Neurology International, 16:731-760, Jul 2024. URL: https://doi.org/10.3390/neurolint16040055, doi:10.3390/neurolint16040055. This article has 17 citations.

20. (childs2024developmentofrespiratory pages 2-3): Anne-Marie Childs, Catherine Turner, Ronan Astin, Stephen Bianchi, John Bourke, Vicki Cunningham, Lisa Edel, Christopher Edwards, Phillippa Farrant, Jane Heraghty, Meredith James, Charlotte Massey, Ben Messer, Jassi Michel Sodhi, Patrick Brian Murphy, Marianela Schiava, Ajit Thomas, Federica Trucco, and Michela Guglieri. Development of respiratory care guidelines for duchenne muscular dystrophy in the uk: key recommendations for clinical practice. Thorax, 79:476-485, Dec 2024. URL: https://doi.org/10.1136/thorax-2023-220811, doi:10.1136/thorax-2023-220811. This article has 24 citations and is from a domain leading peer-reviewed journal.

21. (childs2024developmentofrespiratory pages 8-8): Anne-Marie Childs, Catherine Turner, Ronan Astin, Stephen Bianchi, John Bourke, Vicki Cunningham, Lisa Edel, Christopher Edwards, Phillippa Farrant, Jane Heraghty, Meredith James, Charlotte Massey, Ben Messer, Jassi Michel Sodhi, Patrick Brian Murphy, Marianela Schiava, Ajit Thomas, Federica Trucco, and Michela Guglieri. Development of respiratory care guidelines for duchenne muscular dystrophy in the uk: key recommendations for clinical practice. Thorax, 79:476-485, Dec 2024. URL: https://doi.org/10.1136/thorax-2023-220811, doi:10.1136/thorax-2023-220811. This article has 24 citations and is from a domain leading peer-reviewed journal.

22. (kingsmore2024mathematicalmodelingof pages 8-10): Stephen Kingsmore, Dominic Baun, Laura Tobin, Hung Nguyen, Madison Arenchild, Edwin Juarez, elizabeth kiernan, Daniel Lesser, Emily Wong, Daria Prilutsky, Neta Zach, Steve Han, Dorothee Diogo, Sandor Szalma, and Chamindra Laverty. Mathematical modeling of the progression of duchenne muscular dystrophy in san diego in an era of allele specific oligonucleotide therapy. Apr 2024. URL: https://doi.org/10.21203/rs.3.rs-4049883/v1, doi:10.21203/rs.3.rs-4049883/v1.

23. (childs2024developmentofrespiratory pages 8-9): Anne-Marie Childs, Catherine Turner, Ronan Astin, Stephen Bianchi, John Bourke, Vicki Cunningham, Lisa Edel, Christopher Edwards, Phillippa Farrant, Jane Heraghty, Meredith James, Charlotte Massey, Ben Messer, Jassi Michel Sodhi, Patrick Brian Murphy, Marianela Schiava, Ajit Thomas, Federica Trucco, and Michela Guglieri. Development of respiratory care guidelines for duchenne muscular dystrophy in the uk: key recommendations for clinical practice. Thorax, 79:476-485, Dec 2024. URL: https://doi.org/10.1136/thorax-2023-220811, doi:10.1136/thorax-2023-220811. This article has 24 citations and is from a domain leading peer-reviewed journal.

24. (mercuri2023safetyandeffectiveness pages 11-13): Eugenio Mercuri, Andrés Nascimento Osorio, Francesco Muntoni, Filippo Buccella, Isabelle Desguerre, Janbernd Kirschner, Már Tulinius, Maria Bernadete Dutra de Resende, Lauren P. Morgenroth, Heather Gordish-Dressman, Shelley Johnson, Allan Kristensen, Christian Werner, Panayiota Trifillis, Erik K. Henricson, and Craig M. McDonald. Safety and effectiveness of ataluren in patients with nonsense mutation dmd in the stride registry compared with the cinrg duchenne natural history study (2015–2022): 2022 interim analysis. Journal of Neurology, 270:3896-3913, Apr 2023. URL: https://doi.org/10.1007/s00415-023-11687-1, doi:10.1007/s00415-023-11687-1. This article has 57 citations and is from a domain leading peer-reviewed journal.

25. (krishna2024molecularandbiochemical pages 5-7): Lakshmi Krishna, Akila Prashant, Yogish H. Kumar, Shasthara Paneyala, Siddaramappa J. Patil, Shobha Chikkavaddaragudi Ramachandra, and Prashant Vishwanath. Molecular and biochemical therapeutic strategies for duchenne muscular dystrophy. Neurology International, 16:731-760, Jul 2024. URL: https://doi.org/10.3390/neurolint16040055, doi:10.3390/neurolint16040055. This article has 17 citations.

26. (zaidman2024managementofselect pages 3-4): Craig M. Zaidman, Natalie L. Goedeker, Amal A. Aqul, Russell J. Butterfield, Anne M. Connolly, Ronald G. Crystal, Kara E. Godwin, Kan N. Hor, Katherine D. Mathews, Crystal M. Proud, Elizabeth Kula Smyth, Aravindhan Veerapandiyan, Paul B. Watkins, and Jerry R. Mendell. Management of select adverse events following delandistrogene moxeparvovec gene therapy for patients with duchenne muscular dystrophy. Journal of Neuromuscular Diseases, 11:687-699, Apr 2024. URL: https://doi.org/10.3233/jnd-230185, doi:10.3233/jnd-230185. This article has 22 citations and is from a peer-reviewed journal.

27. (zaidman2024managementofselect pages 6-7): Craig M. Zaidman, Natalie L. Goedeker, Amal A. Aqul, Russell J. Butterfield, Anne M. Connolly, Ronald G. Crystal, Kara E. Godwin, Kan N. Hor, Katherine D. Mathews, Crystal M. Proud, Elizabeth Kula Smyth, Aravindhan Veerapandiyan, Paul B. Watkins, and Jerry R. Mendell. Management of select adverse events following delandistrogene moxeparvovec gene therapy for patients with duchenne muscular dystrophy. Journal of Neuromuscular Diseases, 11:687-699, Apr 2024. URL: https://doi.org/10.3233/jnd-230185, doi:10.3233/jnd-230185. This article has 22 citations and is from a peer-reviewed journal.
