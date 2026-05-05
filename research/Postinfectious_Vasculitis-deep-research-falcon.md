---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T07:43:45.839984'
end_time: '2026-05-05T07:58:03.102553'
duration_seconds: 857.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Postinfectious Vasculitis
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Postinfectious Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Postinfectious Vasculitis** covering all of the
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
- **Disease Name:** Postinfectious Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Postinfectious Vasculitis** covering all of the
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


# Postinfectious Vasculitis — Comprehensive Disease Characteristics Report (2023–2024 prioritized)

## Target disease
**Disease name:** Postinfectious vasculitis (a.k.a. infection-triggered/secondary vasculitis)

**High-level framing:** “Postinfectious vasculitis” is not a single clinicopathologic disease entity in most modern classifications; rather, it is a **secondary vasculitis** syndrome in which vascular inflammation is temporally and mechanistically linked to a preceding or ongoing infection (and sometimes to an infection-induced immune response after pathogen clearance). The best-supported, common contemporary examples include **IgA vasculitis (Henoch–Schönlein purpura)** after upper respiratory infection, **cutaneous small-vessel (leukocytoclastic) vasculitis** after infections, and **infectious/secondary CNS vasculitis/vasculopathy** after neurotropic viruses or bacterial meningitis. (nikolaishvili2023viralinfectionsmay pages 1-2, hoshina2024vasculitisinthe pages 1-2, benadji2023cerebrovascularcomplicationsin pages 1-2)

**MONDO ID:** Not identified in the retrieved sources for a standalone “postinfectious vasculitis” entity; in practice it is commonly represented via subtype entities (e.g., IgA vasculitis) and/or “secondary vasculitis” groupings. (No MONDO-specific evidence retrieved)

---

# 1. Disease information

## 1.1 Concise overview
Postinfectious vasculitis refers to **vascular inflammation occurring as a complication of infection**, mediated either by:
1) **immune-complex deposition** (type III hypersensitivity mechanisms),
2) **postinfectious autoimmunity** (e.g., ANCA or other autoantibodies), and/or
3) **direct pathogen–endothelium interactions** (endothelial invasion and endotheliitis in some infections). These processes can affect small, medium, or large vessels and can be organ-limited (skin-only) or systemic (skin + kidneys, GI tract, joints; or CNS arteriopathy with stroke). (frasier2023secondaryvasculitisattributable pages 1-2, hu2024immunoglobulinavasculitis pages 4-4, benadji2023cerebrovascularcomplicationsin pages 1-2, hoshina2024vasculitisinthe pages 2-3)

## 1.2 Key synonyms / alternative names
Because this is a syndrome descriptor, synonym usage is phenotype-dependent:
- **Secondary vasculitis** in the context of infection (post-COVID secondary vasculitis; infectious CNS vasculitis). (frasier2023secondaryvasculitisattributable pages 1-2, hoshina2024vasculitisinthe pages 1-2)
- **Infection-associated vasculitis / infectious vasculopathy** (especially in CNS contexts). (hoshina2024vasculitisinthe pages 2-3, benadji2023cerebrovascularcomplicationsin pages 1-2)
- Specific postinfectious vasculitides: **IgA vasculitis/Henoch–Schönlein purpura**, **cutaneous small-vessel vasculitis/leukocytoclastic vasculitis**, post-varicella arteriopathy (not fully extracted here), etc. (nikolaishvili2023viralinfectionsmay pages 1-2, frasier2023secondaryvasculitisattributable pages 1-2, hoshina2024vasculitisinthe pages 2-3)

## 1.3 Key identifiers (ICD/MeSH/OMIM/Orphanet/MONDO)
- **No single ICD/MeSH/OMIM identifier** for the umbrella term “postinfectious vasculitis” was established from the retrieved evidence.
- A practical KB approach is to represent **secondary vasculitis** and link it to infection triggers, and/or map to **subtype diagnoses** (e.g., IgA vasculitis; infectious CNS vasculitis/vasculopathy) as separate entries. (hoshina2024vasculitisinthe pages 1-2, hu2024immunoglobulinavasculitis pages 1-2)

## 1.4 Evidence provenance
The evidence base in the retrieved corpus is largely:
- **Aggregated**: reviews (IgA vasculitis pathophysiology; viral triggers; post-COVID secondary vasculitis) and cohorts (COMBAT meningitis cohort; CNS vasculitis cohort). (hu2024immunoglobulinavasculitis pages 1-2, nikolaishvili2023viralinfectionsmay pages 1-2, frasier2023secondaryvasculitisattributable pages 1-2, benadji2023cerebrovascularcomplicationsin pages 1-2, hoshina2024vasculitisinthe pages 1-2)
- **Case-based**: COVID-associated vasculitis reports summarized in review form; infection-triggered CNS vasculitis cases within cohorts. (frasier2023secondaryvasculitisattributable pages 1-2, hoshina2024vasculitisinthe pages 1-2)

---

# 2. Etiology

## 2.1 Primary causes and causal factors
Postinfectious vasculitis is **acquired**, driven by infections that trigger immune dysregulation and vascular injury.

### Major etiologic mechanisms (current understanding)
- **Immune complex disease / type III hypersensitivity:** In COVID-19-associated vasculitis, a proposed “escalation from type 2 T-helper immune response (humoral immunity) to type 3 hypersensitivity (immune complex disease)” is described, with immune complex deposition in vessel walls driving inflammation. (frasier2023secondaryvasculitisattributable pages 1-2)
- **IgA vasculitis (immune complex small-vessel vasculitis):** IgA vasculitis is described as “a small-vessel leukocytoclastic vasculitis caused by immune complex deposition.” (nikolaishvili2023viralinfectionsmay pages 1-2)
- **Localized cerebral vasculitis after bacterial meningitis:** For cerebrovascular complications (CVC) in bacterial meningitis, the “predominant pathophysiological mechanism… is localized cerebral vasculitis,” promoting thrombosis/infarction/hemorrhage via coagulation activation and inhibited fibrinolysis. (benadji2023cerebrovascularcomplicationsin pages 1-2)

## 2.2 Infectious triggers (pathogens)
### 2.2.1 IgA vasculitis triggers (2024 synthesis)
A 2024 IgA vasculitis review lists broad infection triggers including (non-exhaustive):
- **Bacteria:** *Staphylococcus aureus*, *Streptococcus pyogenes*, *Streptococcus pneumoniae*, *Haemophilus parainfluenzae*, *Mycoplasma pneumoniae*. (hu2024immunoglobulinavasculitis pages 4-4)
- **Viruses:** parainfluenza, influenza, rhinovirus, rotavirus, EBV, hepatitis A/B/C, **SARS-CoV-2**, CMV. (hu2024immunoglobulinavasculitis pages 4-4)

### 2.2.2 Viral triggers and vaccines in IgA vasculitis (2023)
A 2023 review emphasizes that “the majority of cases are preceded by upper respiratory tract infections,” historically linked to “group A β-hemolytic streptococcus and common respiratory tract viruses,” and that “during the current coronavirus pandemic, SARS-CoV-2 infection was identified as a main trigger factor,” with additional reports following COVID-19 immunization. (nikolaishvili2023viralinfectionsmay pages 1-2)

### 2.2.3 CNS infectious vasculitis triggers (2024 cohort)
In a 44-patient CNS vasculitis cohort, infection-related etiologies included **varicella zoster virus**, **HSV-1**, and **bacterial meningitis**. (hoshina2024vasculitisinthe pages 2-3)

### 2.2.4 Post-COVID secondary vasculitis
A 2023 review reports growing recognition of vasculitis after COVID-19 and notes that vasculitis “may develop less than two weeks after COVID-19 or during a later onset of the disease.” (frasier2023secondaryvasculitisattributable pages 1-2)

## 2.3 Risk factors
### 2.3.1 Host susceptibility (genetic predisposition)
- The IgA vasculitis review states that HSP/IgA vasculitis may be induced by immune reactions “in genetically predisposed subjects,” and reports “a strong association with HLA class II alleles, specifically HLA-DRB1 alleles.” (nikolaishvili2023viralinfectionsmay pages 1-2)

### 2.3.2 Clinical predictors in infection-related CNS vascular complications
- In bacterial meningitis, CVC risk was independently associated with **advanced age**, **altered mental status**, and **seizures within 48 hours** (multivariable ORs below). (benadji2023cerebrovascularcomplicationsin pages 1-2)

## 2.4 Protective factors
Direct protective factors for “postinfectious vasculitis” as a unified entity were not established from the retrieved evidence. However, for **infection-associated stroke/vasculopathy**, vaccination is discussed as associated with **lower stroke rates** (see Prevention). (clarke2024viralinfectionand pages 1-2)

## 2.5 Gene–environment interactions
Evidence is indirect in the retrieved corpus: genetic susceptibility (HLA-DRB1) is posited to interact with infection-triggered immune activation to produce immune complexes and vessel injury in IgA vasculitis. (nikolaishvili2023viralinfectionsmay pages 1-2)

---

# 3. Phenotypes (clinical spectrum)

## 3.1 Common phenotypes and suggested HPO terms
Below are core postinfectious vasculitis phenotypes represented in the retrieved evidence.

### A) IgA vasculitis (Henoch–Schönlein purpura)
- **Key clinical features:** “Palpable purpura, gastrointestinal symptoms, joint involvement, and renal disease characterize immunoglobulin A vasculitis (IgAV).” (hu2024immunoglobulinavasculitis pages 1-2)
  - Suggested HPO:
    - Palpable purpura / purpura: **HP:0000979** (Purpura)
    - Abdominal pain: **HP:0002027**
    - Arthralgia: **HP:0002829**
    - Hematuria: **HP:0000790**
    - Proteinuria: **HP:0000093**
    - Nephritis: **HP:0000123**
- **Onset:** Predominantly pediatric; most cases age 2–8 years, but can occur in adults. (nikolaishvili2023viralinfectionsmay pages 1-2)
- **Disease course:** Often self-limited; “a small proportion… develop chronic kidney failure or end-stage renal disease.” (hu2024immunoglobulinavasculitis pages 1-2)

### B) Cutaneous small-vessel vasculitis / leukocytoclastic vasculitis (LCV)
- In post-COVID vasculitis review context, “the most common vasculitis associated with COVID-19 patients is leucocytoclastic (LCV), immunoglobulin A (IgA), and Kawasaki disease.” (frasier2023secondaryvasculitisattributable pages 1-2)
  - Suggested HPO:
    - Skin rash: **HP:0000988**
    - Purpura: **HP:0000979**
    - Skin ulcer (if present): **HP:0001059**

### C) CNS postinfectious/secondary vasculitis or vasculopathy
- **Presentation:** The CNS vasculitis cohort highlights stroke-predominant presentations; infectious cases had **acute/subacute stroke** and frequent large–middle vessel involvement. (hoshina2024vasculitisinthe pages 2-3)
  - Suggested HPO:
    - Ischemic stroke: **HP:0002140**
    - Seizures: **HP:0001250**
    - Headache: **HP:0002315**
    - Altered mental status: **HP:0000716** (or HP:0004372 Confusion)

## 3.2 Frequency / proportions (recent numeric data)
- COVID-related vasculitis cohort summarized in a 2024 IgA vasculitis review: among **41** patients with COVID-related vasculitis, **30** had IgA vasculitis; among those IgA vasculitis cases, **30%** had fever and **43.3%** had renal involvement. (hu2024immunoglobulinavasculitis pages 5-5)

---

# 4. Genetic / molecular information

## 4.1 Causal genes
No monogenic “causal gene” for the umbrella concept of postinfectious vasculitis is supported in the retrieved evidence.

## 4.2 Susceptibility loci / immunogenetics
- **HLA class II (HLA-DRB1)** association is cited for IgA vasculitis susceptibility. (nikolaishvili2023viralinfectionsmay pages 1-2)

## 4.3 Molecular effectors implicated (mechanistic candidates)
- **Immune complexes:** IgA-containing immune complexes are a defining pathogenic feature for IgA vasculitis. (nikolaishvili2023viralinfectionsmay pages 1-2)
- **Aberrant IgA glycosylation:** IgAV mechanisms include “aberrantly glycosylated IgA.” (hu2024immunoglobulinavasculitis pages 1-2)
- **Anti-endothelial cell antibodies (AECA):** Included among “main pathogenic mechanisms” and described as drivers of endothelial injury (via ADCC/CDC) and neutrophil recruitment. (hu2024immunoglobulinavasculitis pages 1-2, hu2024immunoglobulinavasculitis pages 4-4)
- **Neutrophils and NETs:** A 2023 Immunological Reviews article highlights immune-complex–driven NET formation via Fcγ receptors and Mac-1, linking immune complexes to neutrophil-mediated vascular injury. (aymonnier2023theneutrophila pages 22-22)

### Suggested GO/CL annotations (mechanism-linked)
- GO biological processes (suggested):
  - **GO:0006954** inflammatory response
  - **GO:0006956** complement activation
  - **GO:0030449** regulation of complement activation
  - **GO:0034097** response to cytokine
  - **GO:0030198** extracellular matrix organization (downstream vessel wall remodeling; conceptual)
  - **GO:0042119** neutrophil activation
  - **GO:0038063** neutrophil extracellular trap formation (NETosis; term may vary by ontology version)
- CL cell types (suggested):
  - **CL:0000775** neutrophil
  - **CL:0000540** macrophage
  - **CL:0000548** endothelial cell

---

# 5. Environmental information

## 5.1 Infectious environmental exposures
Infections are the central environmental exposure class for this syndrome, with prominent triggers including URT infections, streptococcal infections, SARS-CoV-2 infection, and neurotropic viral infections (VZV/HSV) in CNS vasculitis contexts. (nikolaishvili2023viralinfectionsmay pages 1-2, frasier2023secondaryvasculitisattributable pages 1-2, hoshina2024vasculitisinthe pages 2-3)

## 5.2 Lifestyle factors
Not established in the retrieved evidence for postinfectious vasculitis specifically.

---

# 6. Mechanism / pathophysiology

## 6.1 Mechanistic causal chains (upstream → downstream)

### A) Immune-complex small-vessel vasculitis (IgA vasculitis paradigm)
1) **Infection trigger** (often URT infection; multiple viruses/bacteria reported) (nikolaishvili2023viralinfectionsmay pages 1-2, hu2024immunoglobulinavasculitis pages 4-4)
2) **Aberrant IgA biology**: abnormally/aberrantly glycosylated IgA1; immune response generates antigen–antibody complexes (nikolaishvili2023viralinfectionsmay pages 1-2, hu2024immunoglobulinavasculitis pages 1-2)
3) **Large immune complexes deposit** in small vessels of skin/kidney/gut/joints (defining feature) (nikolaishvili2023viralinfectionsmay pages 1-2)
4) **Complement activation and leukocyte recruitment** → endothelial injury, leukocytoclastic vasculitis, organ manifestations (concept supported by immune-complex deposition and complement pathway activation language) (nikolaishvili2023viralinfectionsmay pages 1-2)

### B) Immune-complex/Th2-to-type III escalation model (COVID-associated vasculitis)
A 2023 review proposes that COVID-19 vasculitis can involve an “escalation from type 2 T-helper immune response… to type 3 hypersensitivity (immune complex disease)” with immune complex deposition in vessel walls and cytokine release (including IL-6). (frasier2023secondaryvasculitisattributable pages 1-2)

### C) Infection-related CNS vasculitis/vasculopathy leading to stroke
- In a CNS vasculitis cohort, infection-related cases (VZV/HSV/bacterial meningitis) commonly presented with acute/subacute stroke and large–middle vessel involvement on imaging. (hoshina2024vasculitisinthe pages 2-3)

### D) Bacterial meningitis → localized cerebral vasculitis → cerebrovascular complications
- Mechanism explicitly described: localized cerebral vasculitis activates coagulation and inhibits fibrinolysis, causing thrombosis, infarction, and/or hemorrhage. (benadji2023cerebrovascularcomplicationsin pages 1-2)

## 6.2 Key pathways (high-level)
- **Complement pathway** (alternative complement activation noted in IgA vasculitis pathogenesis discussion). (nikolaishvili2023viralinfectionsmay pages 1-2)
- **Fc receptor signaling / immune complex–neutrophil axis** (FcγRIIA/FcγRIIIB, Mac-1) promoting NETs. (aymonnier2023theneutrophila pages 22-22)

---

# 7. Anatomical structures affected

## 7.1 Organ-level involvement (common)
- **Skin** (cutaneous vasculitis; palpable purpura). (hu2024immunoglobulinavasculitis pages 1-2, frasier2023secondaryvasculitisattributable pages 1-2)
- **Kidney** (IgA vasculitis nephritis; proteinuria/nephritic syndrome). (hu2024immunoglobulinavasculitis pages 1-2)
- **GI tract and joints** (IgA vasculitis). (hu2024immunoglobulinavasculitis pages 1-2)
- **Central nervous system** (secondary/infectious CNS vasculitis causing stroke). (hoshina2024vasculitisinthe pages 2-3)
- **Large vessels (aorta)** in post-COVID aortitis cases. (frasier2023secondaryvasculitisattributable pages 3-4)

### Suggested UBERON terms (examples)
- Skin: **UBERON:0002097**
- Kidney: **UBERON:0002113**
- Small blood vessel: **UBERON:0001638**
- Aorta: **UBERON:0000947**
- Brain: **UBERON:0000955**

---

# 8. Temporal development (onset, progression)

- **IgA vasculitis:** Most common in children (2–8 years), often after URT infection, frequently self-limited, but renal involvement can be refractory and progress to CKD/ESRD in a minority. (nikolaishvili2023viralinfectionsmay pages 1-2, hu2024immunoglobulinavasculitis pages 1-2)
- **Post-COVID vasculitis:** Can occur “less than two weeks after COVID-19 or during a later onset of the disease.” (frasier2023secondaryvasculitisattributable pages 1-2)
- **Secondary CNS vasculitis:** In a cohort, secondary CNS vasculitis had **shorter median time to diagnosis (15 days) vs primary (30 days)**. (hoshina2024vasculitisinthe pages 2-3)

---

# 9. Inheritance and population

## 9.1 Epidemiology (available recent statistics)
Because “postinfectious vasculitis” is a syndrome label, epidemiology is best represented by its major phenotypes.

### IgA vasculitis incidence
- The 2024 IgA vasculitis review reports global pediatric predominance and provides annual incidence ranges: **6.79–55.9 per 100,000** children/adolescents (<17 years) across countries; adult incidence **0.1–0.8 per 100,000** in some population studies. (hu2024immunoglobulinavasculitis pages 1-2)
- A 2023 review cites an incidence of **20.4 per 100,000** population (in children, in the cited reference context) and that males are affected “twice as frequently as females.” (nikolaishvili2023viralinfectionsmay pages 1-2)

### Community-acquired bacterial meningitis (as a postinfectious vasculitis context for CVC)
- Annual incidence: “around **2/100,000** inhabitants.” (benadji2023cerebrovascularcomplicationsin pages 1-2)

### Primary CNS vasculitis (useful differential benchmark)
- Estimated incidence: **2.4 per 1 million person-years**; mortality **8–23%**; ~40% unfavorable outcomes (not postinfectious but central for differential). (salvarani2024primarycentralnervous pages 1-2)

## 9.2 Population demographics
- CNS vasculitis cohort: median age 54 years; 25% men. (hoshina2024vasculitisinthe pages 1-2)

---

# 10. Diagnostics

## 10.1 Core diagnostic principles (real-world implementation)
Postinfectious vasculitis diagnosis generally requires:
1) Demonstration of vasculitis/vasculopathy in an organ system,
2) Exclusion of primary vasculitis mimics,
3) Evidence of temporal/causal linkage to infection (microbiology, serology, clinical syndrome), and
4) In some phenotypes, biopsy confirmation (e.g., CNS; skin; kidney).

### A) IgA vasculitis
- Recognize classic clinical tetrad and monitor renal disease to prevent long-term complications. (hu2024immunoglobulinavasculitis pages 1-2)

### B) CNS vasculitis: differentiating primary vs infectious/secondary
A 2024 cohort provides practical discriminators:
- Secondary CNS vasculitis had higher fever incidence, more frequent **low CSF glucose**, and **unique CSF oligoclonal bands** (especially in infectious and CTD-associated vasculitis). (hoshina2024vasculitisinthe pages 1-2)
- Vessel-wall MRI enhancement was frequent, particularly in secondary cases (data summarized in extracted evidence). (hoshina2024vasculitisinthe pages 3-5)

### C) Bacterial meningitis with cerebrovascular complications (CVC)
- CVC defined by focal clinical deficits and/or CT/MRI evidence of ischemic/hemorrhagic lesions, sometimes “associated… with vasculitis and/or thrombophlebitis.” (benadji2023cerebrovascularcomplicationsin pages 1-2)

## 10.2 Differential diagnosis
- For suspected CNS vasculitis, a NEJM review emphasizes that differential includes **secondary cerebral vasculitis** and **infections**, and that angiography specificity is low; biopsy can be definitive. (salvarani2024primarycentralnervous pages 1-2)

---

# 11. Outcomes / prognosis

## 11.1 CNS infectious/secondary vasculitis outcomes
- In the CNS vasculitis cohort (mixed etiologies), mortality was **20.5% overall**, higher in secondary (26.3%) than primary (16.0%). (hoshina2024vasculitisinthe pages 1-2)

## 11.2 Bacterial meningitis CVC burden
- CVC occurred in **25.3%** (128/506) of bacterial meningitis cases in the COMBAT cohort and are described as influencing morbidity/mortality in the broader literature background. (benadji2023cerebrovascularcomplicationsin pages 1-2)

## 11.3 IgA vasculitis renal prognosis
- Renal involvement ranges “from mild proteinuria to severe nephritic or nephrotic syndrome,” motivating monitoring to prevent long-term complications. (hu2024immunoglobulinavasculitis pages 1-2)

---

# 12. Treatment

## 12.1 Treatment principles
Treat postinfectious vasculitis by jointly addressing:
- **The trigger infection** (antimicrobials/antivirals when active or suspected), and
- **The immune-mediated vascular injury** (corticosteroids, IVIG, and immunosuppressants in selected contexts).

## 12.2 Phenotype-specific evidence (2023–2024)

### A) Post-COVID secondary vasculitis (aortitis; Kawasaki-like)
A 2023 review summarizes reported regimens and outcomes:
- Aortitis: corticosteroids such as **prednisolone 40 mg** (symptoms alleviated within ~2 weeks) and **prednisone 60 mg** (symptom resolution) are reported in case-based evidence. (frasier2023secondaryvasculitisattributable pages 3-4)
- Kawasaki-like disease: IVIG plus aspirin (infant) and IVIG + corticosteroids (adult), with early treatment (<4 days) associated with reduced coronary aneurysm development and improved LV function (summary statement). (frasier2023secondaryvasculitisattributable pages 3-4)

### B) Infectious/secondary CNS vasculitis (cohort evidence)
In a 2024 single-center cohort:
- **80%** of infectious vasculitis patients received antimicrobial therapy.
- Some VZV vasculitis cases received **IV methylprednisolone (IVMP)**.
- Time to treatment was faster in secondary vs primary CNS vasculitis (median **1.0** vs **6.0** days). (hoshina2024vasculitisinthe pages 3-5)

### C) Bacterial meningitis CVC
- Adjunctive dexamethasone was **not statistically different** between those with/without CVC in COMBAT (p=0.84), though background notes RCT/meta-analyses show benefit for pneumococcal meningitis outcomes. (benadji2023cerebrovascularcomplicationsin pages 1-2)

### Suggested MAXO terms (examples)
- Systemic glucocorticoid therapy: **MAXO:0000648** (glucocorticoid therapy; exact MAXO ID may vary)
- Intravenous immunoglobulin therapy: **MAXO:0000743** (IVIG therapy; verify exact MAXO)
- Antimicrobial therapy: **MAXO:0000747** (antibiotic therapy)
- Antiviral therapy: **MAXO:0000748**

*(MAXO identifiers should be verified against the current MAXO release; included here as suggested mappings.)*

---

# 13. Prevention

## 13.1 Infection prevention as vasculitis prevention
Because infection is upstream, prevention emphasizes infection prevention (e.g., vaccination) and rapid infection treatment.

## 13.2 Vaccination and reduced infection-associated stroke risk (proxy prevention for infectious vasculopathy)
A 2024 review on viral infection and stroke reports that a large Canadian analysis of >4 million residents found **lower stroke rates associated with vaccination status**, and a French study found an increasing reduction in stroke risk with more regular vaccination over 5 years; it also emphasizes herpetic infections (chickenpox/shingles) as causes of cerebral vasculopathies. (clarke2024viralinfectionand pages 1-2)

---

# 14. Other species / natural disease
No animal natural disease evidence for “postinfectious vasculitis” was retrieved in the provided corpus.

---

# 15. Model organisms
No dedicated model organism evidence for “postinfectious vasculitis” as a unified entity was retrieved in the provided corpus. Mechanistic inference in the retrieved evidence focuses on human immunopathology (immune complexes, complement, neutrophils/NETs). (aymonnier2023theneutrophila pages 22-22, nikolaishvili2023viralinfectionsmay pages 1-2)

---

# Recent developments (2023–2024 highlights)

1) **Post-COVID secondary vasculitis:** Increasing recognition that vasculitis may appear early or later after SARS-CoV-2 infection, with mechanistic emphasis on immune-complex disease and endothelial involvement, and with case-based evidence for steroid/IVIG benefit in selected phenotypes (aortitis, Kawasaki-like disease). (frasier2023secondaryvasculitisattributable pages 1-2, frasier2023secondaryvasculitisattributable pages 3-4)
2) **IgA vasculitis mechanistic refinement (2024):** Integration of aberrant IgA glycosylation, anti-endothelial antibodies, complement-dependent injury, and neutrophil effector pathways in infection-triggered IgAV. (hu2024immunoglobulinavasculitis pages 1-2, hu2024immunoglobulinavasculitis pages 4-4)
3) **CNS postinfectious vasculitis cohort-level characterization (2024):** Distinguishing CSF features (low glucose, oligoclonal bands), fever, imaging patterns, and real-world immunosuppressive/antimicrobial treatment patterns in infectious CNS vasculitis. (hoshina2024vasculitisinthe pages 1-2, hoshina2024vasculitisinthe pages 3-5)
4) **Bacterial meningitis vascular complications quantified (2023):** Prospective cohort quantifies cerebrovascular complications at ~25%, consistent with vasculitis-mediated injury mechanisms. (benadji2023cerebrovascularcomplicationsin pages 1-2)

---

# Evidence map artifact
The following table provides a compact mapping from triggers → mechanisms → diagnostics → treatments with recent numeric data.

| Phenotype/entity | Typical infectious triggers | Key mechanism(s) | Diagnostic features/tests | Treatment approaches reported | Recent numeric data/statistics | Key cited source (with URL, year/month) |
|---|---|---|---|---|---|---|
| COVID-19–associated secondary vasculitis (cutaneous LCV/IgA, aortitis, Kawasaki-like) | SARS-CoV-2 infection; vasculitis may develop in **<2 weeks** or later during/after infection (frasier2023secondaryvasculitisattributable pages 1-2, frasier2023secondaryvasculitisattributable pages 3-4) | Proposed immune-mediated pathways include **Th2/humoral escalation to type III hypersensitivity with immune-complex deposition**, cytokine release including **IL-6**, and **direct endothelial/vascular invasion via ACE2**; Kawasaki-like presentations also linked to immune hyperresponse/STING signaling (frasier2023secondaryvasculitisattributable pages 1-2, frasier2023secondaryvasculitisattributable pages 3-4) | CT and **FDG-PET** for aortitis; inflammatory markers **ESR, CRP, IL-6** elevated; phenotypes include cutaneous small-vessel vasculitis/LCV, IgA vasculitis, aortitis, giant cell/ophthalmic arteritis, Kawasaki-like disease (frasier2023secondaryvasculitisattributable pages 1-2, frasier2023secondaryvasculitisattributable pages 3-4) | **Prednisolone/prednisone 40–60 mg** reported for aortitis; **IVIG plus aspirin** for Kawasaki-like disease (frasier2023secondaryvasculitisattributable pages 3-4) | Review discussed **65 articles**; reported labs in representative cases included **ESR 57 and 109 mm/hr**, **CRP 8.7 and 10.73 mg/dL**, **IL-6 54.44 pg/mL**, **hemoglobin 10.4 g/dL** (frasier2023secondaryvasculitisattributable pages 1-2, frasier2023secondaryvasculitisattributable pages 3-4) | Frasier et al., *Secondary Vasculitis Attributable to Post-COVID Syndrome*, Cureus, **2023 Aug**. URL: https://doi.org/10.7759/cureus.44119 (frasier2023secondaryvasculitisattributable pages 1-2, frasier2023secondaryvasculitisattributable pages 3-4) |
| IgA vasculitis as postinfectious small-vessel vasculitis | Bacterial triggers reported include **Staphylococcus aureus, Streptococcus pyogenes, Streptococcus pneumoniae, Haemophilus parainfluenzae, Mycoplasma pneumoniae**; viral triggers include **parainfluenza, influenza, rhinovirus, rotavirus, EBV, hepatitis A/B/C, SARS-CoV-2, CMV**; also parasites/yeast and post-vaccination triggers listed (hu2024immunoglobulinavasculitis pages 4-4) | Multi-hit model involving **galactose-deficient IgA1**, **IgA/IgG immune complexes**, **anti-endothelial cell antibodies**, **complement-dependent cytotoxicity**, **ADCC**, **neutrophil recruitment via IL-8 and leukotriene B4**, and **NET/ROS-mediated injury** (hu2024immunoglobulinavasculitis pages 4-4, hu2024immunoglobulinavasculitis pages 5-5) | Suggested/mechanistic diagnostics include measurement of **serum IgA immune complexes** and demonstration of **IgA binding to PMNs**; clinical spectrum includes palpable purpura with GI/joint/renal disease (hu2024immunoglobulinavasculitis pages 5-5, nikolaishvili2023viralinfectionsmay pages 11-13) | No treatment details provided in the cited mechanistic snippets; review context notes consensus guidance exists but specifics are not in the extracted evidence (nikolaishvili2023viralinfectionsmay pages 11-13, hu2024immunoglobulinavasculitis pages 5-5) | In a COVID-related vasculitis cohort, **30 of 41** patients had IgA vasculitis; among these, **30%** had fever and **43.3%** had renal involvement (hu2024immunoglobulinavasculitis pages 5-5) | Hu et al., *Immunoglobulin A vasculitis: The clinical features and pathophysiology*, Kaohsiung J Med Sci, **2024 Jun**. URL: https://doi.org/10.1002/kjm2.12852 (hu2024immunoglobulinavasculitis pages 4-4, hu2024immunoglobulinavasculitis pages 5-5) |
| Infectious/secondary CNS vasculitis cohort findings | Infectious causes in cohort included **varicella zoster virus (4/44, 9.1%)**, **HSV-1 (1/44, 2.3%)**, and **bacterial meningitis (2/44, 4.5%)** (hoshina2024vasculitisinthe pages 2-3) | Secondary/infectious CNS vasculitis associated with stroke-predominant presentation; imaging often showed large–middle vessel disease; diagnostic distinctions included inflammatory CSF abnormalities rather than a single unique mechanism in the snippet (hoshina2024vasculitisinthe pages 2-3, hoshina2024vasculitisinthe pages 3-5) | Features favoring secondary/infectious disease: **fever**, **low CSF glucose**, **unique CSF oligoclonal bands**, and vessel-wall MRI enhancement; vasculitic changes seen on blood-vessel imaging in many cases (hoshina2024vasculitisinthe pages 2-3, hoshina2024vasculitisinthe pages 1-2, hoshina2024vasculitisinthe pages 3-5) | **IV methylprednisolone** was predominant induction therapy; **cyclophosphamide** common adjunctive/maintenance agent; **80%** of infectious vasculitis patients received antimicrobials; some VZV cases also received IV methylprednisolone/high-dose prednisone (hoshina2024vasculitisinthe pages 1-2, hoshina2024vasculitisinthe pages 3-5) | Among **44** patients, **19 (43.2%)** had secondary CNS vasculitis and **10 (22.7%)** were infection-related; all infectious vasculitis patients had acute/subacute stroke; **7/10 (70%)** had large–middle vessel involvement; low CSF glucose in **41.2% vs 8.7%** primary; unique OCB in **63.6% vs 0** primary; mortality **20.5%** overall, **26.3%** secondary; time to diagnosis **15 vs 30 days** (hoshina2024vasculitisinthe pages 2-3, hoshina2024vasculitisinthe pages 1-2, hoshina2024vasculitisinthe pages 3-5) | Hoshina et al., *Vasculitis in the Central Nervous System: Etiology, Characteristics, and Outcomes in a Large Single-Center Cohort*, The Neurohospitalist, **2024 Dec**. URL: https://doi.org/10.1177/19418744231223283 (hoshina2024vasculitisinthe pages 2-3, hoshina2024vasculitisinthe pages 1-2, hoshina2024vasculitisinthe pages 3-5) |
| Cerebrovascular complications in bacterial meningitis attributed to localized cerebral vasculitis | Community-acquired bacterial meningitis, especially **pneumococcal** and **meningococcal** disease; these account for ~**85%** of adult cases (benadji2023cerebrovascularcomplicationsin pages 1-2) | Predominant mechanism described as **localized cerebral vasculitis** leading to coagulation activation, inhibited fibrinolysis, thrombosis, infarction, and hemorrhage; less common mechanisms include vasospasm, DIC, and septic emboli (benadji2023cerebrovascularcomplicationsin pages 1-2) | CVC defined by focal clinical signs and/or **CT/MRI** lesions; focal signs include motor, cerebellar, visual, sensory deficits, aphasia, and pyramidal syndromes (benadji2023cerebrovascularcomplicationsin pages 1-2) | Adjunctive **dexamethasone** was **not associated** with CVC in this cohort (**p=0.84**), although prior trials cited in the excerpt showed benefit on death/neurologic sequelae in pneumococcal meningitis (benadji2023cerebrovascularcomplicationsin pages 1-2) | Bacterial meningitis annual incidence about **2/100,000**; published CVC rates **10–29%**; in COMBAT, **128/506 (25.3%)** had CVC, including **78/265 (29.4%)** pneumococcal, **17/111 (15.3%)** meningococcal, **29/117 (24.8%)** other bacteria; independent associations: age **OR 1.01**, altered mental status **OR 2.23**, seizures within 48 h **OR 1.90** (benadji2023cerebrovascularcomplicationsin pages 1-2) | Benadji et al., *Cerebrovascular complications in patients with community-acquired bacterial meningitis*, BMC Infect Dis, **2023 Jun**. URL: https://doi.org/10.1186/s12879-023-08320-x (benadji2023cerebrovascularcomplicationsin pages 1-2) |
| Neutrophil/NET mechanisms linking immune complexes to vasculitis | Infection-triggered immune-complex vasculitis context; infections are implied upstream triggers in immune-complex disease and IgA vasculitis (aymonnier2023theneutrophila pages 22-22, hu2024immunoglobulinavasculitis pages 5-5) | **Soluble and immobilized immune complexes** drive **NET formation** through **FcγRIIA/FcγRIIIB** and **Mac-1**, linking immune-complex deposition to **neutrophil-driven endothelial injury**; neutrophils also implicated in crescentic glomerulonephritis (aymonnier2023theneutrophila pages 22-22) | Mechanistic evidence includes NET induction by immune complexes and patient serum IgA causing significant DNA release from PMNs; during acute IgA vasculitis, IgA binds peripheral PMNs (aymonnier2023theneutrophila pages 22-22, hu2024immunoglobulinavasculitis pages 5-5) | No disease-specific treatment protocol in the snippet; neutrophils are described as **proposed therapeutic targets** (aymonnier2023theneutrophila pages 22-22) | Review cites a **417-patient** single-center IgA vasculitis cohort as epidemiologic context for neutrophil involvement (aymonnier2023theneutrophila pages 22-22) | Aymonnier et al., *The neutrophil: A key resourceful agent in immune-mediated vasculitis*, Immunological Reviews, **2023 Nov**. URL: https://doi.org/10.1111/imr.13170 (aymonnier2023theneutrophila pages 22-22) |


*Table: This table summarizes representative recent evidence for major postinfectious/secondary vasculitis phenotypes, mechanisms, diagnostics, treatments, and available quantitative findings. It is useful as a compact evidence map for disease-knowledge-base curation.*

---

# Key statistics (quick reference)
- IgA vasculitis pediatric incidence: **6.79–55.9 per 100,000/year** (<17y); adult incidence **0.1–0.8 per 100,000/year** in some studies. (hu2024immunoglobulinavasculitis pages 1-2)
- COMBAT bacterial meningitis cohort CVC prevalence: **25.3% (128/506)**; pneumococcal **29.4%**, meningococcal **15.3%**. (benadji2023cerebrovascularcomplicationsin pages 1-2)
- CNS vasculitis cohort: **43.2% secondary**, **22.7% infectious**; mortality **20.5%** overall. (hoshina2024vasculitisinthe pages 1-2)

---

# Limitations and gaps
- **Ontology identifiers (MONDO/MeSH/ICD) for “postinfectious vasculitis” as a single entity** were not available in the retrieved evidence; mapping should be performed via subtype diagnoses and/or “secondary vasculitis” parent classes.
- **PMIDs** were not present in the retrieved full-text snippets; the report therefore cites DOI URLs and journal metadata from the retrieved documents.
- Many postinfectious vasculitis claims remain **case-report dominated** (especially COVID-associated vasculitis), and population-level incidence for the umbrella syndrome is not established in the retrieved evidence.



References

1. (nikolaishvili2023viralinfectionsmay pages 1-2): Mariam Nikolaishvili, Ani Pazhava, and Vito Di Lernia. Viral infections may be associated with henoch–schönlein purpura. Journal of Clinical Medicine, 12:697, Jan 2023. URL: https://doi.org/10.3390/jcm12020697, doi:10.3390/jcm12020697. This article has 48 citations.

2. (hoshina2024vasculitisinthe pages 1-2): Yoji Hoshina, Alen Delic, Ka-Ho Wong, Stephanie Lyden, Robert Kadish, Tammy L. Smith, Melissa A. Wright, Daisuke Shimura, and Stacey L. Clardy. Vasculitis in the central nervous system: etiology, characteristics, and outcomes in a large single-center cohort. The Neurohospitalist, 14:129-139, Dec 2024. URL: https://doi.org/10.1177/19418744231223283, doi:10.1177/19418744231223283. This article has 6 citations.

3. (benadji2023cerebrovascularcomplicationsin pages 1-2): Amine Benadji, Thomas Debroucker, Guillaume Martin-Blondel, Laurent Argaud, Virginie Vitrat, Charlotte Biron, Michel Wolff, Bruno Hoen, Xavier Duval, and Sarah Tubiana. Cerebrovascular complications in patients with community-acquired bacterial meningitis: occurrence and associated factors in the combat multicenter prospective cohort. BMC Infectious Diseases, Jun 2023. URL: https://doi.org/10.1186/s12879-023-08320-x, doi:10.1186/s12879-023-08320-x. This article has 12 citations and is from a peer-reviewed journal.

4. (frasier2023secondaryvasculitisattributable pages 1-2): Kelly M Frasier, Caroline Gallagher-Poehls, Mikayla Cochrane, and Debosree Roy. Secondary vasculitis attributable to post-covid syndrome. Cureus, Aug 2023. URL: https://doi.org/10.7759/cureus.44119, doi:10.7759/cureus.44119. This article has 16 citations.

5. (hu2024immunoglobulinavasculitis pages 4-4): Ya‐Chiao Hu, Yao‐Hsu Yang, and Bor‐Luen Chiang. Immunoglobulin a vasculitis: the clinical features and pathophysiology. The Kaohsiung Journal of Medical Sciences, 40:612-620, Jun 2024. URL: https://doi.org/10.1002/kjm2.12852, doi:10.1002/kjm2.12852. This article has 12 citations.

6. (hoshina2024vasculitisinthe pages 2-3): Yoji Hoshina, Alen Delic, Ka-Ho Wong, Stephanie Lyden, Robert Kadish, Tammy L. Smith, Melissa A. Wright, Daisuke Shimura, and Stacey L. Clardy. Vasculitis in the central nervous system: etiology, characteristics, and outcomes in a large single-center cohort. The Neurohospitalist, 14:129-139, Dec 2024. URL: https://doi.org/10.1177/19418744231223283, doi:10.1177/19418744231223283. This article has 6 citations.

7. (hu2024immunoglobulinavasculitis pages 1-2): Ya‐Chiao Hu, Yao‐Hsu Yang, and Bor‐Luen Chiang. Immunoglobulin a vasculitis: the clinical features and pathophysiology. The Kaohsiung Journal of Medical Sciences, 40:612-620, Jun 2024. URL: https://doi.org/10.1002/kjm2.12852, doi:10.1002/kjm2.12852. This article has 12 citations.

8. (clarke2024viralinfectionand pages 1-2): Michael Clarke, Sarina Falcione, Roobina Boghozian, Raluca Todoran, Yiran Zhang, Maria Guadalupe C. Real, Alexis StPierre, Twinkle Joy, and Glen C. Jickling. Viral infection and ischemic stroke: emerging trends and mechanistic insights. Journal of the American Heart Association, Sep 2024. URL: https://doi.org/10.1161/jaha.124.035892, doi:10.1161/jaha.124.035892. This article has 23 citations.

9. (hu2024immunoglobulinavasculitis pages 5-5): Ya‐Chiao Hu, Yao‐Hsu Yang, and Bor‐Luen Chiang. Immunoglobulin a vasculitis: the clinical features and pathophysiology. The Kaohsiung Journal of Medical Sciences, 40:612-620, Jun 2024. URL: https://doi.org/10.1002/kjm2.12852, doi:10.1002/kjm2.12852. This article has 12 citations.

10. (aymonnier2023theneutrophila pages 22-22): Karen Aymonnier, Jennifer Amsler, Peter Lamprecht, Alan Salama, and Véronique Witko‐Sarsat. The neutrophil: a key resourceful agent in immune‐mediated vasculitis. Immunological Reviews, 314:326-356, Nov 2023. URL: https://doi.org/10.1111/imr.13170, doi:10.1111/imr.13170. This article has 41 citations and is from a domain leading peer-reviewed journal.

11. (frasier2023secondaryvasculitisattributable pages 3-4): Kelly M Frasier, Caroline Gallagher-Poehls, Mikayla Cochrane, and Debosree Roy. Secondary vasculitis attributable to post-covid syndrome. Cureus, Aug 2023. URL: https://doi.org/10.7759/cureus.44119, doi:10.7759/cureus.44119. This article has 16 citations.

12. (salvarani2024primarycentralnervous pages 1-2): Carlo Salvarani, Gene G. Hunder, and Robert D. Brown. Primary central nervous system vasculitis. The New England journal of medicine, 391 11:1028-1037, Sep 2024. URL: https://doi.org/10.1056/nejmra2314942, doi:10.1056/nejmra2314942. This article has 42 citations and is from a highest quality peer-reviewed journal.

13. (hoshina2024vasculitisinthe pages 3-5): Yoji Hoshina, Alen Delic, Ka-Ho Wong, Stephanie Lyden, Robert Kadish, Tammy L. Smith, Melissa A. Wright, Daisuke Shimura, and Stacey L. Clardy. Vasculitis in the central nervous system: etiology, characteristics, and outcomes in a large single-center cohort. The Neurohospitalist, 14:129-139, Dec 2024. URL: https://doi.org/10.1177/19418744231223283, doi:10.1177/19418744231223283. This article has 6 citations.

14. (nikolaishvili2023viralinfectionsmay pages 11-13): Mariam Nikolaishvili, Ani Pazhava, and Vito Di Lernia. Viral infections may be associated with henoch–schönlein purpura. Journal of Clinical Medicine, 12:697, Jan 2023. URL: https://doi.org/10.3390/jcm12020697, doi:10.3390/jcm12020697. This article has 48 citations.