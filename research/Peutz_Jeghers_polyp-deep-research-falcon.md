---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-30T20:27:34.673609'
end_time: '2026-04-30T20:49:37.484005'
duration_seconds: 1322.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peutz-Jeghers polyp
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peutz-Jeghers polyp
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Peutz-Jeghers polyp** covering all of the
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
- **Disease Name:** Peutz-Jeghers polyp
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Peutz-Jeghers polyp** covering all of the
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


# Disease Characteristics Research Report: Peutz–Jeghers polyp (Peutz–Jeghers–type hamartomatous polyp)

## Executive summary
Peutz–Jeghers (PJ) polyps are distinctive hamartomatous gastrointestinal polyps characterized histologically by arborizing smooth-muscle bundles extending from the muscularis mucosae into the polyp, producing a branching “tree/christmas-tree” appearance with lobular/cystically dilated glands/crypts. PJ polyps most commonly occur as part of Peutz–Jeghers syndrome (PJS), an autosomal-dominant hereditary cancer predisposition syndrome driven primarily by germline STK11 (LKB1) loss-of-function, which substantially increases lifetime cancer risk and causes clinically significant morbidity through bleeding/anemia, obstruction, and intussusception. Recent 2023–2024 guidance emphasizes early small-bowel surveillance beginning in childhood (≈8 years), use of noninvasive small-bowel evaluation (SB capsule endoscopy or MR enterography) to guide targeted device-assisted enteroscopy (DAE) polypectomy, and removal of large small-bowel polyps (>15 mm) to reduce intussusception risk. (gorji2023hamartomatouspolypsdiagnosis pages 1-2, gorji2023hamartomatouspolypsdiagnosis pages 2-4, macfarland2024pediatriccancerscreening pages 5-6, pennazio2023smallbowelcapsuleendoscopy pages 21-21)


## Target disease
- **Disease name (entry focus):** Peutz–Jeghers polyp (Peutz–Jeghers–type hamartomatous polyp)
- **Related syndrome:** Peutz–Jeghers syndrome (PJS)
- **MONDO ID:** **MONDO:0008280 (Peutz–Jeghers syndrome)** (MONDO ID for “Peutz–Jeghers polyp” was not present in retrieved evidence) (zhang2025intussusceptionsecondaryto pages 5-6)
- **Category:** Genetic (typically syndromic)


## 1. Disease information
### What is the disease?
A **Peutz–Jeghers polyp** is a hamartomatous GI polyp with characteristic histology. In a 2023 review, PJ polyps are described on H&E as having a “characteristic phyllodes appearing epithelial component” with a glandular/cystic component extending toward deeper layers. (gorji2023hamartomatouspolypsdiagnosis pages 1-2)

In a 2024 multicenter endoscopy study, PJS-type hamartomatous polyps are described histologically as interdigitating smooth muscle bundles with an arborizing/branching-tree (“christmas-tree”) appearance and lobular mucosal crypts. (elfeky2024deviceassistedenteroscopyin pages 1-2)

### Key identifiers
- **MONDO:** MONDO:0008280 (Peutz–Jeghers syndrome) (zhang2025intussusceptionsecondaryto pages 5-6)
- **OMIM / Orphanet / ICD-10/ICD-11 / MeSH:** not explicitly present in retrieved full-text evidence; should be curated from dedicated disease-identifier resources for the knowledge base. (gorji2023hamartomatouspolypsdiagnosis pages 1-2, amru2024peutzjegherssyndromea pages 4-5)

### Synonyms / alternative names
For PJS (syndrome-level), reported synonyms include **polyp-and-spots syndrome**, **Hutchinson–Weber–Peutz syndrome**, and **perioral lentiginosis**. (bandaru2024areviewon pages 1-2)

### Evidence type note
Most available evidence is **aggregated disease-level (PJS) literature**; “Peutz–Jeghers polyp” is most often discussed as the key lesion within PJS. (gorji2023hamartomatouspolypsdiagnosis pages 1-2, amru2024peutzjegherssyndromea pages 4-5)


## 2. Etiology
### Disease causal factors
**Primary cause (syndromic PJ polyps):** germline pathogenic variants in **STK11/LKB1** (tumor suppressor serine/threonine kinase) on chromosome 19p13.3, inherited in an autosomal-dominant pattern; de novo cases occur. (amru2024peutzjegherssyndromea pages 1-2, amru2024peutzjegherssyndromea pages 4-5)

A mechanistic framing from a 2023 review states that PJS is an autosomal dominant disorder involving “the mammalian target of rapamycin (mTOR) pathway” as a result of germline STK11/LKB1 mutation; STK11/LKB1 modulates cellular proliferation, responds to energy deficits, and controls cellular polarity. (gorji2023hamartomatouspolypsdiagnosis pages 1-2)

### Risk factors
- **Genetic risk factor:** carrying a germline STK11/LKB1 pathogenic variant (core causal factor). (amru2024peutzjegherssyndromea pages 1-2, gorji2023hamartomatouspolypsdiagnosis pages 1-2)
- **Polyp-size risk factor for intussusception:** small-bowel polyp size **>15 mm** is emphasized as a key risk factor for intussusception and related complications. (pennazio2023smallbowelcapsuleendoscopy pages 21-21)

### Protective factors
No specific genetic/environmental protective factors were identified in the retrieved evidence.

### Gene–environment interactions
Not specifically described in retrieved evidence; variable expressivity is attributed to genetic modifiers, environment, and somatic events in at least one 2024 review. (amru2024peutzjegherssyndromea pages 2-4)


## 3. Phenotypes
### Core phenotypes (clinical signs/symptoms)
1) **Hamartomatous GI polyps / polyposis**
- **Distribution:** Polyps most frequently involve the small intestine (~75% in one 2024 review), especially proximal jejunum, distal ileum, and duodenum; stomach involvement ~25%. (amru2024peutzjegherssyndromea pages 2-4)
- **Age of onset:** median age of initial polyp development ~12 years; ~50% symptomatic by age 20 (review-level data). (gorji2023hamartomatouspolypsdiagnosis pages 1-2)
- **HPO suggestions:** HP:0004396 (Hamartomatous polyposis), HP:0004780 (Intestinal polyposis)
- **UBERON suggestions:** UBERON:0002108 (small intestine), UBERON:0002114 (jejunum), UBERON:0002116 (ileum), UBERON:0002110 (duodenum)

2) **Mucocutaneous pigmentation (lentiginosis)**
- Typically bluish-black macules on lips, buccal mucosa, perioral region, and digits; often appear in early childhood. (amru2024peutzjegherssyndromea pages 2-4, amru2024peutzjegherssyndromea pages 4-5)
- **HPO suggestions:** HP:0000992 (Cutaneous pigmentation), HP:0001053 (Hyperpigmentation)

3) **GI bleeding → anemia**
- A 2023 review states the “primary clinical manifestation is chronic bleeding from GI polyps causing anemia.” (gorji2023hamartomatouspolypsdiagnosis pages 1-2)
- **HPO suggestions:** HP:0001892 (Bleeding), HP:0001903 (Anemia), HP:0002140 (Melena) (when present)

4) **Intussusception / bowel obstruction**
- Quantitative natural history: intussusception risk reported as **≈44% by age 10** and **≈50% by age 20**, with higher risk in polyps ≥15 mm. (gorji2023hamartomatouspolypsdiagnosis pages 2-4)
- AACR 2024 pediatric guidance notes intussusception risk “over 20% by age 10 and over 50% by age 20,” and emphasizes family education for symptoms. (macfarland2024pediatriccancerscreening pages 5-6)
- **HPO suggestions:** HP:0002250 (Intussusception), HP:0002024 (Abdominal pain), HP:0001744 (Bowel obstruction)

### Quality of life impact
While multiple sources describe substantial morbidity (repeated hospitalizations/endoscopy, prior surgeries), **quantitative QoL instrument results (e.g., EQ-5D/SF-36) were not present in the retrieved evidence**. Surgical burden is indirectly supported by the fact that 75% of a DAE cohort had prior small-bowel surgery before index DAE. (elfeky2024deviceassistedenteroscopyin pages 1-2)


## 4. Genetic / molecular information
### Causal gene(s)
- **STK11 (LKB1)** is the principal causal gene for PJS-associated PJ polyps. (amru2024peutzjegherssyndromea pages 1-2, gorji2023hamartomatouspolypsdiagnosis pages 1-2)

### Pathogenic variants (examples and classes)
- **Large deletions/duplications** of STK11 are recognized as an important mutational mechanism; sequencing can detect point mutations, small indels, and larger duplications/deletions. (amru2024peutzjegherssyndromea pages 4-5, amru2024peutzjegherssyndromea pages 6-7)
- **Missense variants & functional signaling impact:** 2024 work describes STK11 missense VUS and ties them to impaired **LKB1/AMPK signaling** (article title) and provides variant-level family data, including “De novo” cases and examples such as “c.1062C>G.” (liu2024twomissensestk11 pages 1-2)
- **Frameshift example and mosaicism:** 2025 Familial Cancer report identifies **NM_000455.4:c.842del (p.Pro281Argfs*6)** in a child with PJS and documents maternal tissue-restricted mosaicism (2.7% VAF in cervical tissue) after initial “de novo” interpretation based on blood testing, supporting mosaic phenomena in hereditary cancer counseling. (jiang2025gastrictypeendocervicaladenocarcinoma pages 2-4)

### Functional consequences
STK11/LKB1 is described as regulating cellular polarity, growth/proliferation, and energy-sensing pathways; disruption is linked to mTOR-axis dysregulation and downstream proliferative effects contributing to hamartomatous polyp formation and cancer predisposition. (gorji2023hamartomatouspolypsdiagnosis pages 1-2, amru2024peutzjegherssyndromea pages 1-2)

### Epigenetic information
A 2024 review reports increased methylation of the **LKB1 promoter** in PJS polyps (bisulfite PCR/Sanger sequencing). (amru2024peutzjegherssyndromea pages 2-4)


## 5. Environmental information
No specific toxins/lifestyle/infectious triggers were identified in the retrieved evidence for PJ polyps; the condition is primarily genetically driven (syndromic). (amru2024peutzjegherssyndromea pages 1-2, gorji2023hamartomatouspolypsdiagnosis pages 1-2)


## 6. Mechanism / pathophysiology
### Proposed causal chain (current understanding)
1) **Germline STK11/LKB1 loss-of-function** (often inherited AD, sometimes de novo/mosaic) reduces tumor-suppressor kinase function. (amru2024peutzjegherssyndromea pages 1-2, jiang2025gastrictypeendocervicaladenocarcinoma pages 2-4)
2) **Cell polarity and energy-sensing dysregulation** and **mTOR-axis pathway perturbation** alter epithelial–stromal organization and proliferation controls. (gorji2023hamartomatouspolypsdiagnosis pages 1-2)
3) **Hamartomatous polyp growth** with arborizing smooth muscle and disorganized mucosal architecture leads to mucosal bleeding, anemia, and mechanical complications (obstruction/intussusception), especially with larger polyps. (gorji2023hamartomatouspolypsdiagnosis pages 1-2, gorji2023hamartomatouspolypsdiagnosis pages 2-4)
4) **Cancer predisposition** emerges with age, with elevated cumulative cancer risk across GI and extraintestinal organs. (kamiya2023feasibilityandsafety pages 1-2, elfeky2024deviceassistedenteroscopyin pages 1-2)

### Pathways and processes (ontology suggestions)
- **GO biological process:** GO:0008283 (cell population proliferation), GO:0030010 (establishment of cell polarity), GO:0006091 (generation of precursor metabolites and energy)
- **Reactome/KEGG concepts (by description in evidence):** mTOR signaling axis; LKB1/AMPK signaling (gorji2023hamartomatouspolypsdiagnosis pages 1-2, liu2024twomissensestk11 pages 1-2)

### Cell types (CL suggestions; inferred from lesion biology)
- CL:0000066 (epithelial cell), CL:0000187 (smooth muscle cell)
(These are ontology suggestions; cell-type–resolved single-cell evidence was not present in retrieved sources.)


## 7. Anatomical structures affected
- **Primary organs/sites:** small intestine (jejunum/ileum/duodenum), colon, stomach (polyps may occur), mucocutaneous sites (lips/buccal mucosa/perioral skin/digits). (amru2024peutzjegherssyndromea pages 2-4, amru2024peutzjegherssyndromea pages 4-5)
- **Complication-related structures:** intestinal lumen (intussusception/obstruction). (gorji2023hamartomatouspolypsdiagnosis pages 1-2, gorji2023hamartomatouspolypsdiagnosis pages 2-4)
- **UBERON suggestions:** small intestine (UBERON:0002108), colon (UBERON:0001155), stomach (UBERON:0000945)


## 8. Temporal development
- **Onset:** typically pediatric/childhood; mucocutaneous pigmentation often appears at birth or early childhood; polyps develop in childhood (median ~12 years). (gorji2023hamartomatouspolypsdiagnosis pages 1-2, amru2024peutzjegherssyndromea pages 2-4)
- **Progression/course:** chronic lifelong predisposition; complication risk (intussusception) increases with polyp growth and size; cancer risk increases with age, with mean age of index cancer reported ~41 years in one review. (gorji2023hamartomatouspolypsdiagnosis pages 1-2)


## 9. Inheritance and population
### Epidemiology
Reported incidence/prevalence varies widely across sources:
- **Incidence range:** ~1:8,300 to 1:200,000 (review-level range). (gorji2023hamartomatouspolypsdiagnosis pages 1-2)
- Additional estimates include prevalence 1:50,000–1:200,000 (review). (amru2024peutzjegherssyndromea pages 4-5)

### Inheritance pattern
- **Autosomal dominant** inheritance with ~50% transmission risk to offspring; de novo mutations are common (~30% in one review). (amru2024peutzjegherssyndromea pages 1-2)
- Mosaicism can explain apparent de novo cases and has reproductive-counseling implications. (jiang2025gastrictypeendocervicaladenocarcinoma pages 2-4)

### Penetrance/expressivity
Variable expressivity is reported; contributors include genetic modifiers, environment, and somatic events. (amru2024peutzjegherssyndromea pages 2-4)


## 10. Diagnostics
### Clinical criteria
Criteria include any number of PJ polyps with family history; ≥2 PJ polyps; pigmentation plus family history; or PJ polyps plus pigmentation. (gorji2023hamartomatouspolypsdiagnosis pages 1-2)

### Histopathology
Diagnostic polyp histology includes arborizing smooth muscle with branching-tree appearance and lobular/cystic gland architecture. (gorji2023hamartomatouspolypsdiagnosis pages 1-2, elfeky2024deviceassistedenteroscopyin pages 1-2)

### Imaging/endoscopy
- **Small-bowel evaluation:** capsule endoscopy (SBCE/VCE) and CT/MR enterography are key modalities. (gorji2023hamartomatouspolypsdiagnosis pages 2-4, macfarland2024pediatriccancerscreening pages 13-14)
- **Modality selection for small-bowel tumors/lesions:** a 2024 review of small-bowel tumor diagnosis recommends **three-phase enhanced CT** first-line; if CT shows mass/stenosis/wall thickening, use balloon-assisted endoscopy; if CT negative and no obstructive symptoms, use capsule endoscopy. (yano2024endoscopicdiagnosisof pages 1-2)

### Genetic testing
STK11/LKB1 sequencing can detect point mutations, indels, and larger duplications/deletions; genetic counseling is recommended. (amru2024peutzjegherssyndromea pages 4-5)

### Differential diagnosis (context)
PJ polyps are part of the broader hamartomatous polyposis syndromes spectrum, which includes juvenile polyposis and Cowden/PTEN hamartoma tumor syndrome; distinguishing features include syndromic extraintestinal findings and molecular testing. (gorji2023hamartomatouspolypsdiagnosis pages 1-2)


## 11. Outcome / prognosis
### Cancer risk and timing
- One study reports age-stratified cumulative cancer risk estimates of **1%, 3%, 19%, 32%, 63%, 81%** at ages 20, 30, 40, 50, 60, and 70 years, respectively. (kamiya2023feasibilityandsafety pages 1-2)
- A multicenter DAE paper reports lifetime cancer risk “as high as **93%** for developing any cancer by age 64,” and average lifetime risks for colorectal, gastric, and small-bowel cancer of 39%, 29%, and 13%, respectively. (elfeky2024deviceassistedenteroscopyin pages 1-2)

### Morbidity
Morbidity is driven by bleeding/anemia and mechanical complications (intussusception/obstruction). (gorji2023hamartomatouspolypsdiagnosis pages 1-2, gorji2023hamartomatouspolypsdiagnosis pages 2-4)

### Mortality/survival
Direct mortality rates and life expectancy were not available in retrieved evidence. (elfeky2024deviceassistedenteroscopyin pages 1-2)


## 12. Treatment
### Standard of care / real-world implementations
**Endoscopic surveillance and prophylactic polypectomy** are the mainstay to prevent intussusception/obstruction and manage bleeding.

**Polypectomy thresholds:** ESGE-referenced recommendations summarized in a 2023 review include elective removal of small-bowel polyps **>15–20 mm**, and removal of symptomatic polyps <15 mm. (gorji2023hamartomatouspolypsdiagnosis pages 2-4)

**Guideline emphasis (ESGE 2022 update, published 2023):** a guideline excerpt states that “**large (> 15 mm), symptomatic, or rapidly growing polyps should be promptly removed**” and advises targeted enteroscopy after prior noninvasive SB evaluation; complication rates of DAE polypectomy in PJS are reported as 4%–6% in cited evidence. (pennazio2023smallbowelcapsuleendoscopy pages 21-21)

**Device-assisted enteroscopy (DAE/DBE) outcomes (2024):** In a multicenter retrospective cohort (3 US referral centers), 46 DAEs in 23 PJS patients achieved 131 polypectomies with an adverse event rate of **1.5%** and **no emergent surgery** for small-bowel hamartoma adverse events over 336 aggregated follow-up years. The authors’ conclusion states: “**Endoscopic management of small bowel polyps in patients with PJS using DAE is an effective strategy for prophylactic removal of hamartomas**.” (elfeky2024deviceassistedenteroscopyin pages 1-2)

**Alternative endoscopic techniques:** A 2023 retrospective study of endoscopic ischemic polypectomy (EIP) in 22 PJS patients reports treatment of 607 polyps across 124 sessions, and reports no small-bowel complications or intussusceptions in that series during follow-up. (kamiya2023feasibilityandsafety pages 1-2)

### Clinical trials / investigational therapies (selected)
- **Cold snare polypectomy for small-bowel polyps (enteroscopy-based):** NCT06001476 (Phase 4; estimated start 2023-08-20; primary completion 2024-12-31) evaluates feasibility/safety of cold snare polypectomy for 5–9 mm small-bowel polyps, with endpoints including bleeding/perforation/pancreatitis within 28 days. URL: https://clinicaltrials.gov/study/NCT06001476 (NCT06001476 chunk 1)
- **Celecoxib chemoprevention:** NCT06722534 (randomized, double-blind, placebo-controlled; start 2025-02-01; recruiting) tests celecoxib 200 mg BID for 6 months vs placebo, with a composite endpoint for “progression of small bowel disease.” URL: https://clinicaltrials.gov/study/NCT06722534 (NCT06722534 chunk 1)
- **Pancreatic surveillance in high-risk cohorts including PJS:** CAPS5 NCT02000089 (recruiting) evaluates early pancreatic cancer markers in pancreatic juice and related endpoints in high-risk individuals including PJS. URL: https://clinicaltrials.gov/study/NCT02000089 (NCT02000089 chunk 2)

### MAXO suggestions (treatment/prevention actions)
- MAXO:0000011 (Endoscopy), MAXO:0000567 (Polypectomy), MAXO:0000058 (Cancer surveillance), MAXO:0000127 (Genetic counseling)
(These are ontology suggestions; MAXO IDs should be verified against the MAXO ontology release used by the knowledge base.)


## 13. Prevention
Primary prevention of the genetic condition is not available; prevention focuses on **secondary/tertiary prevention**:
- **Secondary prevention:** early surveillance beginning in childhood (≈8 years) and polypectomy to prevent intussusception/obstruction and detect early malignancy. (macfarland2024pediatriccancerscreening pages 5-6, gorji2023hamartomatouspolypsdiagnosis pages 2-4)
- **Cascade testing and genetic counseling:** early genetic testing in familial cases to enable timely surveillance is recommended by the AACR Childhood Cancer Predisposition Working Group update. (macfarland2024pediatriccancerscreening pages 5-6)


## 14. Other species / natural disease
No naturally occurring veterinary/other-species PJ polyp data were identified in retrieved evidence.


## 15. Model organisms
A 2023 review notes sirolimus (rapamycin) reduced polyp number/size in a mouse model and mentions prospective study, but detailed model-phenotype mapping was not available in retrieved evidence. (gorji2023hamartomatouspolypsdiagnosis pages 2-4)


## Recent developments (2023–2024) and expert analysis
1) **Shift to structured, targeted small-bowel management:** 2023 ESGE guidance emphasizes noninvasive mapping (SBCE/MRE) followed by targeted DAE polypectomy and prompt removal of large (>15 mm) or symptomatic polyps, reflecting a safety/benefit balancing in a technically demanding procedure with known complication rates. (pennazio2023smallbowelcapsuleendoscopy pages 21-21)
2) **Multicenter real-world evidence for DAE safety/effectiveness:** 2024 multicenter data demonstrate low adverse event rates (1.5%) and potential avoidance of emergent surgery over long follow-up, supporting referral-center implementation of prophylactic DAE programs. (elfeky2024deviceassistedenteroscopyin pages 1-2)
3) **Pediatric screening harmonization:** AACR 2024 update provides a pragmatic pediatric pathway: baseline endoscopy/colonoscopy/small-bowel study at ~8 years, surveillance every 2–3 years if polyps, and deferral to ~18 years if baseline negative and asymptomatic, with explicit family education about high intussusception risk. (macfarland2024pediatriccancerscreening pages 5-6, macfarland2024pediatriccancerscreening pages 13-14)


## Visual guideline evidence
The ESGE guideline table region containing Peutz–Jeghers syndrome small-bowel surveillance and recommendations for DAE polypectomy is available as an extracted figure/table image. (pennazio2023smallbowelcapsuleendoscopy media 9eea28e2)


## Structured summary tables
| Item | Details | Evidence |
|---|---|---|
| Disease scope: Peutz-Jeghers polyp | A Peutz-Jeghers polyp (PJP) is a hamartomatous gastrointestinal polyp with characteristic arborizing/smooth-muscle architecture. In reviewed sources, PJPs are distinguished from the broader syndrome and are described as most characteristic in the small bowel; gastric polyps in PJS may resemble hyperplastic polyps and are not always classified as true PJPs. | (gorji2023hamartomatouspolypsdiagnosis pages 1-2, amru2024peutzjegherssyndromea pages 2-4, elfeky2024deviceassistedenteroscopyin pages 1-2) |
| Disease scope: Peutz-Jeghers syndrome | Peutz-Jeghers syndrome (PJS) is a rare autosomal dominant cancer-predisposition/polyposis syndrome defined by hamartomatous GI polyps plus characteristic mucocutaneous pigmentation, usually caused by germline STK11/LKB1 pathogenic variants. | (gorji2023hamartomatouspolypsdiagnosis pages 1-2, amru2024peutzjegherssyndromea pages 4-5, amru2024peutzjegherssyndromea pages 1-2) |
| Relationship between polyp and syndrome | The “Peutz-Jeghers polyp” is a lesion/histopathologic entity; “Peutz-Jeghers syndrome” is the inherited multisystem disorder in which such polyps occur together with pigmentation and elevated cancer risk. A solitary PJP is therefore narrower than syndromic PJS. | (gorji2023hamartomatouspolypsdiagnosis pages 1-2, amru2024peutzjegherssyndromea pages 4-5, elfeky2024deviceassistedenteroscopyin pages 1-2) |
| Synonyms / alternative names | Reported synonyms for PJS include **polyp-and-spots syndrome**, **Hutchinson-Weber-Peutz syndrome**, and **perioral lentiginosis**. Abbreviation: **PJS**. | (bandaru2024areviewon pages 1-2) |
| Key identifier available from evidence | **MONDO:0008280 — Peutz-Jeghers syndrome** (from Open Targets disease-target association output in the retrieved evidence). | (zhang2025intussusceptionsecondaryto pages 5-6) |
| Key identifiers not recovered in provided sources | **OMIM, Orphanet, ICD-10/ICD-11, and MeSH identifiers were not explicitly present in the retrieved full-text evidence snippets** used here; these should be curated separately from disease databases before KB ingestion. | (gorji2023hamartomatouspolypsdiagnosis pages 1-2, amru2024peutzjegherssyndromea pages 4-5, amru2024peutzjegherssyndromea pages 6-7) |
| Core diagnostic criteria | Clinical criteria reported in reviewed sources include: **(1)** any number of PJ polyps with a family history of PJS; **(2)** two or more PJ polyps; **(3)** characteristic mucocutaneous pigmentation with a family history of PJS; or **(4)** any number of PJ polyps with mucocutaneous pigmentation. Another cited formulation uses ≥2 PJS-type hamartomatous polyps or such polyps plus pigmentation/family history. | (gorji2023hamartomatouspolypsdiagnosis pages 1-2, elfeky2024deviceassistedenteroscopyin pages 1-2) |
| Core clinical hallmarks | Hallmark features are **mucocutaneous melanotic macules** (often lips, buccal mucosa, perioral skin, digits) appearing in childhood and **GI hamartomatous polyps**, most often in the small intestine; complications include bleeding, anemia, obstruction, and intussusception. | (amru2024peutzjegherssyndromea pages 1-2, amru2024peutzjegherssyndromea pages 2-4, gorji2023hamartomatouspolypsdiagnosis pages 1-2, amru2024peutzjegherssyndromea pages 4-5) |
| Histopathologic hallmarks of PJP | Histology shows a **hamartomatous polyp with arborizing/interdigitating smooth-muscle bundles** extending from the muscularis mucosae, creating a **phyllodes / branching-tree / christmas-tree** appearance, with lobular or cystically dilated mucosal glands/crypts. | (gorji2023hamartomatouspolypsdiagnosis pages 1-2, amru2024peutzjegherssyndromea pages 2-4, elfeky2024deviceassistedenteroscopyin pages 1-2) |


*Table: This table distinguishes the lesion-level concept of a Peutz-Jeghers polyp from the syndrome-level diagnosis of Peutz-Jeghers syndrome, and summarizes synonyms, identifiers, diagnostic criteria, and histopathologic hallmarks from the retrieved evidence.*

| Organ/site | Modality | Start age | Interval | Key thresholds/notes | Evidence (citation IDs) |
|---|---|---:|---|---|---|
| Upper GI (stomach/duodenum) | EGD / upper endoscopy | 8 years | Every 1–3 years; if baseline at 8 is negative, routine surveillance can resume at 18 | Used to detect and remove accessible hamartomatous polyps; Amru 2024 also describes yearly or biannual EGD beginning in youth or when symptomatic | (gorji2023hamartomatouspolypsdiagnosis pages 2-4, amru2024peutzjegherssyndromea pages 5-6, bandaru2024areviewon pages 1-2, macfarland2024pediatriccancerscreening pages 5-6, macfarland2024pediatriccancerscreening pages 13-14) |
| Colon/rectum | Colonoscopy | 8 years | Every 1–3 years; if baseline at 8 is negative, routine surveillance can resume at 18 | Amru 2024 notes colonoscopy may begin around puberty/age 15 and be repeated annually in some practices, especially with rapid/gigantic polyp growth or early family CRC | (gorji2023hamartomatouspolypsdiagnosis pages 2-4, amru2024peutzjegherssyndromea pages 5-6, macfarland2024pediatriccancerscreening pages 5-6, macfarland2024pediatriccancerscreening pages 13-14) |
| Small bowel surveillance | SBCE / VCE or CT/MR enterography (MRE preferred alternative when VCE unavailable) | 8 years | Every 2–3 years; if baseline at ≥8 is negative, repeat around 18 if asymptomatic | Noninvasive small-bowel evaluation should guide therapy; small-bowel polyps are the major source of intussusception risk | (gorji2023hamartomatouspolypsdiagnosis pages 2-4, bandaru2024areviewon pages 1-2, macfarland2024pediatriccancerscreening pages 5-6, macfarland2024pediatriccancerscreening pages 13-14, pennazio2023smallbowelcapsuleendoscopy pages 21-21) |
| Small bowel therapeutic management | DAE / DBE polypectomy after prior SBCE/MRE | Not a screening age-based test; used when target polyps identified | Targeted/as needed; some cohorts averaged about one DAE exam every 2.5 years | ESGE: promptly remove large (>15 mm), symptomatic, or rapidly growing polyps; Gorji 2023 cites elective removal of >15–20 mm and symptomatic polyps <15 mm; DAE/DBE can reduce laparotomy but carries procedural risk | (gorji2023hamartomatouspolypsdiagnosis pages 2-4, elfeky2024deviceassistedenteroscopyin pages 1-2, pennazio2023smallbowelcapsuleendoscopy pages 21-21) |
| Small bowel complication prevention | Family education for intussusception symptoms | At diagnosis / childhood | Ongoing counseling | AACR 2024 emphasizes education because intussusception risk exceeds 20% by age 10 and 50% by age 20; risk is highest with polyps ≥15 mm | (gorji2023hamartomatouspolypsdiagnosis pages 2-4, macfarland2024pediatriccancerscreening pages 5-6, macfarland2024pediatriccancerscreening pages 13-14) |
| Pancreas | EUS or MRCP/ERCP; some sources also mention MRI/MRCP | 30 years | Annually | Gorji 2023 recommends annual pancreatic imaging from 30; later adult guidance in broader reviews supports pancreas surveillance in adulthood because of elevated cancer risk | (gorji2023hamartomatouspolypsdiagnosis pages 2-4, amru2024peutzjegherssyndromea pages 4-5) |
| Breast | Self-exam | 18 years | Annually | Early self-surveillance recommended in women with PJS due to increased lifetime breast-cancer risk | (gorji2023hamartomatouspolypsdiagnosis pages 2-4) |
| Breast | MRI / mammography | 25 years | Annual imaging | Gorji 2023 lists MRI/mammography from 25; AACR 2024 notes adult-onset breast screening begins at or after about 25 years | (gorji2023hamartomatouspolypsdiagnosis pages 2-4, macfarland2024pediatriccancerscreening pages 6-7) |
| Cervix / gynecologic tract | Cervical smear | 20 years | Annually | Used as part of adult gynecologic surveillance in PJS | (gorji2023hamartomatouspolypsdiagnosis pages 2-4) |
| Pelvic / ovarian surveillance | Pelvic ultrasound; annual gynecologic exam/physical examination | 25 years for annual pelvic US; childhood onward for physical exam in AACR update | Annual | AACR 2024 recommends annual physical exam of ovaries/cervix in childhood; pelvic ultrasound is advised for girls with precocious puberty or concerning symptoms | (gorji2023hamartomatouspolypsdiagnosis pages 2-4, macfarland2024pediatriccancerscreening pages 13-14, macfarland2024pediatriccancerscreening pages 6-7) |
| Testes | Testicular exam with/without ultrasound | From birth / childhood | Yearly | Gorji 2023 recommends yearly testicular exam/ultrasound from birth; AACR 2024 does not support routine screening ultrasound for all boys, instead emphasizing annual physical examination and selective imaging when indicated | (gorji2023hamartomatouspolypsdiagnosis pages 2-4, macfarland2024pediatriccancerscreening pages 13-14, macfarland2024pediatriccancerscreening pages 6-7) |
| Genetics / family management | STK11 testing, counseling, predictive testing for relatives | At diagnosis / early childhood in familial cases | One-time diagnostic test with cascade testing as indicated | Sequencing can detect point mutations, indels, and larger deletions/duplications; early genetic confirmation enables surveillance planning; preimplantation/prenatal testing may be considered in families with known variants | (amru2024peutzjegherssyndromea pages 4-5, macfarland2024pediatriccancerscreening pages 5-6, bandaru2024areviewon pages 3-3) |


*Table: This table summarizes 2023–2024 surveillance and management recommendations for Peutz-Jeghers syndrome/polyps across organ systems. It integrates practical start ages, intervals, and key intervention thresholds from recent reviews, guidelines, and pediatric screening updates.*


## Data gaps and curation notes (for knowledge-base ingestion)
- Controlled identifiers for the *polyp* entity (OMIM/Orphanet/ICD/MeSH/MONDO) were not present in retrieved evidence; only MONDO:0008280 for PJS was available. (zhang2025intussusceptionsecondaryto pages 5-6)
- Quantitative quality-of-life and health-economic metrics were not captured in the retrieved evidence, despite qualitative indications of high morbidity and surgical burden. (elfeky2024deviceassistedenteroscopyin pages 1-2)
- Variant allele frequencies in population databases (gnomAD), ClinVar classifications, and formal genotype–phenotype penetrance estimates were not present in retrieved full-text snippets and would require dedicated database extraction.


References

1. (gorji2023hamartomatouspolypsdiagnosis pages 1-2): Leva Gorji and Peter Albrecht. Hamartomatous polyps: diagnosis, surveillance, and management. World Journal of Gastroenterology, 29:1304-1314, Feb 2023. URL: https://doi.org/10.3748/wjg.v29.i8.1304, doi:10.3748/wjg.v29.i8.1304. This article has 16 citations.

2. (gorji2023hamartomatouspolypsdiagnosis pages 2-4): Leva Gorji and Peter Albrecht. Hamartomatous polyps: diagnosis, surveillance, and management. World Journal of Gastroenterology, 29:1304-1314, Feb 2023. URL: https://doi.org/10.3748/wjg.v29.i8.1304, doi:10.3748/wjg.v29.i8.1304. This article has 16 citations.

3. (macfarland2024pediatriccancerscreening pages 5-6): Suzanne P. MacFarland, Kerri Becktell, Kami Wolfe Schneider, Roland P. Kuiper, Harry Lesmana, Julia Meade, Kim E. Nichols, Christopher C. Porter, Sharon A. Savage, Kris Ann Schultz, Hamish Scott, Lisa States, Uri Tabori, Chieko Tamura, Gail Tomlinson, Kristin Zelley, Carol Durno, Andrew Bauer, and Sharon E. Plon. Pediatric cancer screening in hereditary gastrointestinal cancer risk syndromes: an update from the aacr childhood cancer predisposition working group. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:4566-4571, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0953, doi:10.1158/1078-0432.ccr-24-0953. This article has 19 citations.

4. (pennazio2023smallbowelcapsuleendoscopy pages 21-21): Marco Pennazio, Emanuele Rondonotti, Edward J. Despott, Xavier Dray, Martin Keuchel, Tom Moreels, David S. Sanders, Cristiano Spada, Cristina Carretero, Pablo Cortegoso Valdivia, Luca Elli, Lorenzo Fuccio, Begona Gonzalez Suarez, Anastasios Koulaouzidis, Lumir Kunovsky, Deirdre McNamara, Helmut Neumann, Enrique Perez-Cuadrado-Martinez, Enrique Perez-Cuadrado-Robles, Stefania Piccirelli, Bruno Rosa, Jean-Christophe Saurin, Reena Sidhu, Ilja Tacheci, Erasmia Vlachou, and Konstantinos Triantafyllou. Small-bowel capsule endoscopy and device-assisted enteroscopy for diagnosis and treatment of small-bowel disorders: european society of gastrointestinal endoscopy (esge) guideline – update 2022. Endoscopy, 55:58-95, Nov 2023. URL: https://doi.org/10.1055/a-1973-3796, doi:10.1055/a-1973-3796. This article has 353 citations and is from a domain leading peer-reviewed journal.

5. (zhang2025intussusceptionsecondaryto pages 5-6): Jing Zhang, Tian-Hao Xie, Yan Fu, Xiao-Shi Jin, Qiang Wang, and Zheng Niu. Intussusception secondary to peutz-jeghers syndrome: a case report and literature review of diagnostic and therapeutic advances. Frontiers in Medicine, Oct 2025. URL: https://doi.org/10.3389/fmed.2025.1687958, doi:10.3389/fmed.2025.1687958. This article has 1 citations.

6. (elfeky2024deviceassistedenteroscopyin pages 1-2): Omar Wahid Mohamed Elfeky, Suraj Panjwani, David Cave, Daniel Wild, and Daniel Raines. Device-assisted enteroscopy in the surveillance of intestinal hamartomas in peutz-jeghers syndrome. Endoscopy International Open, 12:E128-E134, Nov 2024. URL: https://doi.org/10.1055/a-2197-8554, doi:10.1055/a-2197-8554. This article has 6 citations and is from a peer-reviewed journal.

7. (amru2024peutzjegherssyndromea pages 4-5): Rohan L Amru and Archana Dhok. Peutz-jeghers syndrome: a comprehensive review of genetics, clinical features, and management approaches. Cureus, Apr 2024. URL: https://doi.org/10.7759/cureus.58887, doi:10.7759/cureus.58887. This article has 20 citations.

8. (bandaru2024areviewon pages 1-2): Lakshmi Himaja Bandaru. A review on peutz-jeghers syndrome. Journal of Clinical and Pharmaceutical Research, pages 8-10, Oct 2024. URL: https://doi.org/10.61427/jcpr.v4.i4.2024.144, doi:10.61427/jcpr.v4.i4.2024.144. This article has 0 citations.

9. (amru2024peutzjegherssyndromea pages 1-2): Rohan L Amru and Archana Dhok. Peutz-jeghers syndrome: a comprehensive review of genetics, clinical features, and management approaches. Cureus, Apr 2024. URL: https://doi.org/10.7759/cureus.58887, doi:10.7759/cureus.58887. This article has 20 citations.

10. (amru2024peutzjegherssyndromea pages 2-4): Rohan L Amru and Archana Dhok. Peutz-jeghers syndrome: a comprehensive review of genetics, clinical features, and management approaches. Cureus, Apr 2024. URL: https://doi.org/10.7759/cureus.58887, doi:10.7759/cureus.58887. This article has 20 citations.

11. (amru2024peutzjegherssyndromea pages 6-7): Rohan L Amru and Archana Dhok. Peutz-jeghers syndrome: a comprehensive review of genetics, clinical features, and management approaches. Cureus, Apr 2024. URL: https://doi.org/10.7759/cureus.58887, doi:10.7759/cureus.58887. This article has 20 citations.

12. (liu2024twomissensestk11 pages 1-2): Jin Liu, Si-Cong Zeng, An Wang, Hai-Ying Cheng, Qian-Jun Zhang, and Guang-Xiu Lu. Two missense stk11 gene variations impaired lkb1/adenosine monophosphate-activated protein kinase signaling in peutz-jeghers syndrome. World Journal of Gastrointestinal Oncology, 16:1532-1546, Apr 2024. URL: https://doi.org/10.4251/wjgo.v16.i4.1532, doi:10.4251/wjgo.v16.i4.1532. This article has 0 citations.

13. (jiang2025gastrictypeendocervicaladenocarcinoma pages 2-4): Anqi Jiang, Yingfei Ye, Haowen Tan, Xiang Tao, Fenghua Ma, Hui Wang, Congjian Xu, and Yu Kang. Gastric-type endocervical adenocarcinoma in situ as the presenting feature in a mosaic stk11 pathogenic variant carrier with a peutz-jeghers syndrome child. Familial Cancer, Jul 2025. URL: https://doi.org/10.1007/s10689-025-00485-5, doi:10.1007/s10689-025-00485-5. This article has 1 citations and is from a peer-reviewed journal.

14. (kamiya2023feasibilityandsafety pages 1-2): Kenji J. L. Limpias Kamiya, Naoki Hosoe, Kaoru Takabayashi, Anna Okuzawa, Hinako Sakurai, Yukie Hayashi, Ryoichi Miyanaga, Tomohisa Sujino, Haruhiko Ogata, and Takanori Kanai. Feasibility and safety of endoscopic ischemic polypectomy and clinical outcomes in patients with peutz–jeghers syndrome (with video). Digestive Diseases and Sciences, 68:252-258, Apr 2023. URL: https://doi.org/10.1007/s10620-022-07477-w, doi:10.1007/s10620-022-07477-w. This article has 15 citations and is from a peer-reviewed journal.

15. (macfarland2024pediatriccancerscreening pages 13-14): Suzanne P. MacFarland, Kerri Becktell, Kami Wolfe Schneider, Roland P. Kuiper, Harry Lesmana, Julia Meade, Kim E. Nichols, Christopher C. Porter, Sharon A. Savage, Kris Ann Schultz, Hamish Scott, Lisa States, Uri Tabori, Chieko Tamura, Gail Tomlinson, Kristin Zelley, Carol Durno, Andrew Bauer, and Sharon E. Plon. Pediatric cancer screening in hereditary gastrointestinal cancer risk syndromes: an update from the aacr childhood cancer predisposition working group. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:4566-4571, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0953, doi:10.1158/1078-0432.ccr-24-0953. This article has 19 citations.

16. (yano2024endoscopicdiagnosisof pages 1-2): Tomonori Yano and Hironori Yamamoto. Endoscopic diagnosis of small bowel tumor. Cancers, 16:1704, Apr 2024. URL: https://doi.org/10.3390/cancers16091704, doi:10.3390/cancers16091704. This article has 8 citations.

17. (NCT06001476 chunk 1): Xiuli Zuo. Cold Snare Polypectomy for Small Bowel Polyps in Patients With Peutz-Jeghers Syndrome. Shandong University. 2023. ClinicalTrials.gov Identifier: NCT06001476

18. (NCT06722534 chunk 1): Yanglin Pan. Celecoxib for Prevention of Progression in Peutz-Jeghers Syndrome. Air Force Military Medical University, China. 2025. ClinicalTrials.gov Identifier: NCT06722534

19. (NCT02000089 chunk 2):  The Cancer of the Pancreas Screening-5 CAPS5)Study. Johns Hopkins University. 2014. ClinicalTrials.gov Identifier: NCT02000089

20. (pennazio2023smallbowelcapsuleendoscopy media 9eea28e2): Marco Pennazio, Emanuele Rondonotti, Edward J. Despott, Xavier Dray, Martin Keuchel, Tom Moreels, David S. Sanders, Cristiano Spada, Cristina Carretero, Pablo Cortegoso Valdivia, Luca Elli, Lorenzo Fuccio, Begona Gonzalez Suarez, Anastasios Koulaouzidis, Lumir Kunovsky, Deirdre McNamara, Helmut Neumann, Enrique Perez-Cuadrado-Martinez, Enrique Perez-Cuadrado-Robles, Stefania Piccirelli, Bruno Rosa, Jean-Christophe Saurin, Reena Sidhu, Ilja Tacheci, Erasmia Vlachou, and Konstantinos Triantafyllou. Small-bowel capsule endoscopy and device-assisted enteroscopy for diagnosis and treatment of small-bowel disorders: european society of gastrointestinal endoscopy (esge) guideline – update 2022. Endoscopy, 55:58-95, Nov 2023. URL: https://doi.org/10.1055/a-1973-3796, doi:10.1055/a-1973-3796. This article has 353 citations and is from a domain leading peer-reviewed journal.

21. (amru2024peutzjegherssyndromea pages 5-6): Rohan L Amru and Archana Dhok. Peutz-jeghers syndrome: a comprehensive review of genetics, clinical features, and management approaches. Cureus, Apr 2024. URL: https://doi.org/10.7759/cureus.58887, doi:10.7759/cureus.58887. This article has 20 citations.

22. (macfarland2024pediatriccancerscreening pages 6-7): Suzanne P. MacFarland, Kerri Becktell, Kami Wolfe Schneider, Roland P. Kuiper, Harry Lesmana, Julia Meade, Kim E. Nichols, Christopher C. Porter, Sharon A. Savage, Kris Ann Schultz, Hamish Scott, Lisa States, Uri Tabori, Chieko Tamura, Gail Tomlinson, Kristin Zelley, Carol Durno, Andrew Bauer, and Sharon E. Plon. Pediatric cancer screening in hereditary gastrointestinal cancer risk syndromes: an update from the aacr childhood cancer predisposition working group. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:4566-4571, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0953, doi:10.1158/1078-0432.ccr-24-0953. This article has 19 citations.

23. (bandaru2024areviewon pages 3-3): Lakshmi Himaja Bandaru. A review on peutz-jeghers syndrome. Journal of Clinical and Pharmaceutical Research, pages 8-10, Oct 2024. URL: https://doi.org/10.61427/jcpr.v4.i4.2024.144, doi:10.61427/jcpr.v4.i4.2024.144. This article has 0 citations.