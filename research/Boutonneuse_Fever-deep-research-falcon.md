---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T11:24:32.001925'
end_time: '2026-05-09T11:48:12.305549'
duration_seconds: 1420.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Boutonneuse Fever
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Boutonneuse Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Boutonneuse Fever** covering all of the
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
- **Disease Name:** Boutonneuse Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Boutonneuse Fever** covering all of the
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


# Boutonneuse Fever (Mediterranean Spotted Fever) — Disease Characteristics Research Report

## Target Disease
- **Disease name:** Boutonneuse fever
- **Category:** Infectious (tick-borne spotted fever group rickettsiosis)
- **Primary etiologic agent:** *Rickettsia conorii* (notably *R. conorii* subsp. *conorii*; other subspecies/strains circulate regionally) (gafarova2023historyandcurrent pages 1-2, cambrea2023boutonneusefeverin pages 2-4)

## Executive overview (current understanding)
Boutonneuse fever (BF)—commonly synonymous with Mediterranean spotted fever (MSF) and “Marseille fever”—is a tick-borne eruptive febrile illness caused predominantly by *Rickettsia conorii* and transmitted mainly by the brown dog tick *Rhipicephalus sanguineus* (cambrea2023boutonneusefeverin pages 1-2). The canonical clinical picture is the triad of fever, rash, and an inoculation eschar (“tache noire”), though the triad is not always present and disease ranges from mild, self-limited illness to severe multisystem vasculitis with neurologic, ocular, renal, and other complications (lamloumi2025epidemiologyandclinical pages 1-2, cambrea2023boutonneusefeverin pages 4-5).

A central modern concept is that MSF/BF is a **vascular infection**: *Rickettsia* preferentially infects vascular endothelium in vivo, causing endothelial dysfunction, barrier leakage, and inflammatory vasculitis that mechanistically underlies the fever, rash, and systemic manifestations (sit2024pathogenicrickettsiaspp. pages 5-6, cambrea2023boutonneusefeverin pages 2-4).

---

## 1. Disease Information

### 1.1 What is the disease?
BF/MSF is a tick-borne spotted fever characterized by an acute febrile illness with maculopapular (sometimes purpuric) rash and a necrotic inoculation eschar at the tick bite site, caused mainly by *Rickettsia conorii* and transmitted by *Rhipicephalus sanguineus* (cambrea2023boutonneusefeverin pages 1-2).

**Abstract-supported definition (2023 review):**
- “Boutonneuse fever (BF) is an eruptive disease and is classified as a spotted fever… caused by *Rickettsia conorii*, with dog ticks being a vector (i.e., *Rhipicephalus sanguineus*).” (published **2023-11-09**, URL https://doi.org/10.3390/microorganisms11112734) (cambrea2023boutonneusefeverin pages 1-2)

### 1.2 Key identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH, MONDO)
- **ICD/MeSH/MONDO/Orphanet identifiers:** not explicitly present in the retrieved full texts for citation in this run; therefore, they cannot be asserted here with primary citations.
- **ClinicalTrials-derived MeSH context:** a trial record lists the condition browse MeSH term “Rickettsia Infections” (MeSH ID D012282), but this is broader than BF/MSF and does not provide BF/MSF-specific MeSH identifiers (NCT07307651 chunk 1).

### 1.3 Synonyms and alternative names
Synonymy is historically and geographically driven:
- Boutonneuse fever ↔ Mediterranean spotted fever (MSF) ↔ Marseille fever (cambrea2023boutonneusefeverin pages 1-2, sousa2008mediterraneanspottedfever pages 29-34).
- French historical name: *fièvre boutonneuse*; hallmark lesion: *tache noire* (eschar) (gafarova2023historyandcurrent pages 1-2).
- A broader synonym set has been used historically across regions (e.g., “Kenya tick typhus”, “Indian tick typhus”, “Astrakhan fever”, “Israeli spotted fever”), reflecting *R. conorii* complex diversity and/or local epidemiology (sousa2008mediterraneanspottedfever pages 29-34).

### 1.4 Evidence source type
Evidence cited here is derived from:
- **Aggregated disease-level resources:** narrative reviews and retrospective cohorts (e.g., Romania review; Tunisia 21-year cohort) (cambrea2023boutonneusefeverin pages 2-4, lamloumi2025epidemiologyandclinical pages 3-6).
- **Individual patient reports/series:** pediatric case report (Iran) and small series (Turkey) (hosseininasab2024rickettsiaconoriisubsp. pages 2-4, dalmanoglu2025rickettsiosiscasespresenting pages 1-2).
- **Laboratory/biomedical research reviews** on rickettsial mechanisms (sit2024pathogenicrickettsiaspp. pages 5-6, cambrea2023boutonneusefeverin pages 2-4).

---

## 2. Etiology

### 2.1 Disease causal factor
- **Infectious cause:** *Rickettsia conorii* (spotted fever group *Rickettsia*), especially *R. conorii* subsp. *conorii* in classic MSF; additional subspecies/strains (e.g., *israelensis*, *caspia*, *indica*) may circulate regionally and contribute to clinical/epidemiologic heterogeneity (gafarova2023historyandcurrent pages 1-2, cambrea2023boutonneusefeverin pages 2-4).

### 2.2 Risk factors
**Environmental/exposure**
- Tick exposure, especially to *Rhipicephalus sanguineus*; contact with dogs infested by ticks is a recurring epidemiologic feature (cambrea2023boutonneusefeverin pages 1-2, lamloumi2025epidemiologyandclinical pages 3-6).
- Strong **seasonality** in Mediterranean settings: e.g., Tunisia cohort had 68.8% of cases in the hot season and none in winter (lamloumi2025epidemiologyandclinical pages 1-2).

**Host/clinical risk factors for severe outcome (expert synthesis from prior detailed work)**
- In Portuguese MSF experience summarized in a dissertation abstract, **delay in therapy** and **diabetes mellitus** were implicated as risk factors for death, and **alcoholism** emerged as a host risk factor for fatal outcome; Israeli spotted fever (ISF) strain infection was associated with higher fatality (sousa2008mediterraneanspottedfever pages 17-21).

**Potential host susceptibility**
- Severe evolution has been linked to oxidant-mediated endothelial damage and noted to be worse in glucose-6-phosphate dehydrogenase (G6PD) deficiency in a Romanian review synthesis of pathophysiology (cambrea2023boutonneusefeverin pages 2-4).

### 2.3 Protective factors
No specific genetic protective variants or robust protective environmental factors were identified in the retrieved sources for BF/MSF.

### 2.4 Gene–environment interactions
No definitive human gene–environment interaction studies for BF/MSF were retrieved. The strongest, well-supported “interaction” concept in the present corpus is that **climatic conditions influencing tick activity** modulate exposure risk (sousa2008mediterraneanspottedfever pages 17-21).

---

## 3. Phenotypes

### 3.1 Core phenotypes (with suggested HPO terms)
Below are common clinical phenotypes with **ontology suggestions** (HPO terms are suggested; not all were explicitly enumerated in retrieved sources).

1. **Fever** (symptom)
   - Frequency: 100% in Tunisian cohort (173/173) (lamloumi2025epidemiologyandclinical pages 3-6).
   - Suggested HPO: **HP:0001945 (Fever)**.

2. **Maculopapular rash** (clinical sign)
   - Tunisia: maculopapular rash 83.8% (145/173); palms/soles involved 98.3% (170/173) (lamloumi2025epidemiologyandclinical pages 3-6).
   - Classic triad present in 69.9% (lamloumi2025epidemiologyandclinical pages 1-2).
   - Suggested HPO: **HP:0000980 (Rash)**; **HP:0000968 (Maculopapular rash)**; **HP:0001055 (Palmar rash)**; **HP:0000977 (Plantar rash)**.

3. **Eschar (“tache noire”)** (skin lesion)
   - Tunisia: eschar 69.9% (121/173) (lamloumi2025epidemiologyandclinical pages 3-6).
   - Romania series: eschar approximately 57.9–75.23% depending on dataset (cambrea2023boutonneusefeverin pages 4-5).
   - Suggested HPO: **HP:0031816 (Eschar)**.

4. **Headache / myalgia / arthralgia** (symptoms)
   - Tunisia: headache 64.5% (121/173); myalgia 60.7% (105/173); arthralgia 57.2% (99/173) (lamloumi2025epidemiologyandclinical pages 3-6).
   - Suggested HPO: **HP:0002315 (Headache)**; **HP:0003326 (Myalgia)**; **HP:0002829 (Arthralgia)**.

5. **Gastrointestinal symptoms** (variable)
   - Tunisia: vomiting 15.6% (27/173) (lamloumi2025epidemiologyandclinical pages 3-6).
   - Pediatric MSF case: abdominal pain, diarrhea, vomiting were prominent (hosseininasab2024rickettsiaconoriisubsp. pages 2-4).
   - Suggested HPO: **HP:0002027 (Abdominal pain)**; **HP:0002014 (Diarrhea)**; **HP:0002013 (Vomiting)**.

### 3.2 Laboratory abnormalities (with suggested HPO terms)
- **Thrombocytopenia**: 48% in Tunisia (lamloumi2025epidemiologyandclinical pages 1-2); also reported commonly in Romania datasets (cambrea2023boutonneusefeverin pages 4-5).
  - Suggested HPO: **HP:0001873 (Thrombocytopenia)**.
- **Leukocytosis**: 36.4% in Tunisia (lamloumi2025epidemiologyandclinical pages 1-2); reported in Romania datasets (cambrea2023boutonneusefeverin pages 4-5).
  - Suggested HPO: **HP:0001974 (Leukocytosis)**.
- **Elevated AST / transaminases**: AST elevated 50.9% in Tunisia (lamloumi2025epidemiologyandclinical pages 1-2); transaminase elevation discussed more broadly in cohorts (cambrea2023boutonneusefeverin pages 4-5, lamloumi2025epidemiologyandclinical pages 8-9).
  - Suggested HPO: **HP:0002910 (Elevated hepatic transaminase)**.
- **Hyponatremia**: discussed as frequent in Tunisian series (lamloumi2025epidemiologyandclinical pages 8-9).
  - Suggested HPO: **HP:0002902 (Hyponatremia)**.

### 3.3 Onset, severity, progression
- Typical course is **acute**, often seasonal, with rapid clinical improvement after doxycycline when started early (lamloumi2025epidemiologyandclinical pages 1-2, dalmanoglu2025rickettsiosiscasespresenting pages 1-2).

### 3.4 Quality of life impact
No disease-specific QoL instruments (e.g., SF-36/EQ-5D) were retrieved for BF/MSF.

---

## 4. Genetic/Molecular Information

### 4.1 Human causal genes / variants
- BF/MSF is **not a monogenic inherited disease**, and no host causal genes or ClinVar-style pathogenic variants were retrieved in the available corpus.

### 4.2 Pathogen genetic diversity / molecular typing
- The *R. conorii* complex includes multiple subspecies and strains (e.g., *conorii*, *israelensis*, *caspia*, *indica*) (gafarova2023historyandcurrent pages 1-2, cambrea2023boutonneusefeverin pages 2-4).
- Strain-level differences may influence virulence and clinical features; Portuguese experience summarized that ISF strain infection was more likely to have fatal outcome and eschar frequency differed (sousa2008mediterraneanspottedfever pages 17-21).

### 4.3 Molecular profiling (omics)
- **NGS/mNGS** is increasingly used for diagnosing culture-negative rickettsioses and complementing serology/PCR (published **2024-10**, URL https://doi.org/10.1371/journal.pntd.0012546) (xing2024usefulnessofnextgeneration pages 2-4).
- Surveillance/genomics in rickettsioses is expanding (amplicon-based NGS; portable WGS platforms) per the Black Sea regional review’s cited diagnostic advances (gafarova2023historyandcurrent pages 26-26).

---

## 5. Environmental Information

### 5.1 Environmental factors
- Primary environmental determinant is **tick exposure**, particularly *Rhipicephalus sanguineus* ecology and dog-associated tick contact (cambrea2023boutonneusefeverin pages 1-2, lamloumi2025epidemiologyandclinical pages 3-6).

### 5.2 Lifestyle factors
No lifestyle factors beyond exposure context (outdoor activities, dog contact) were quantified in retrieved sources.

### 5.3 Infectious agent
- **Bacterium:** *Rickettsia conorii* (obligate intracellular) (cambrea2023boutonneusefeverin pages 1-2).
- **Vector:** *Rhipicephalus sanguineus* (brown dog tick); can be both vector and reservoir (gafarova2023historyandcurrent pages 1-2, cambrea2023boutonneusefeverin pages 1-2).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (trigger → mechanism → clinical manifestations)
1. **Tick bite inoculation** introduces *R. conorii* into skin and local cells, producing an inoculation lesion that can evolve into the eschar (cambrea2023boutonneusefeverin pages 4-5, sousa2008mediterraneanspottedfever pages 46-49).
2. **Dissemination** via lymphatics/blood leads to systemic infection with strong tropism for **vascular endothelial cells** (cambrea2023boutonneusefeverin pages 2-4, sit2024pathogenicrickettsiaspp. pages 5-6).
3. **Endothelial activation/injury** causes:
   - increased vascular permeability (barrier leakage), inflammation and leukocyte infiltration (cambrea2023boutonneusefeverin pages 2-4, sit2024pathogenicrickettsiaspp. pages 5-6);
   - COX-2 activation and prostaglandin secretion (cambrea2023boutonneusefeverin pages 2-4);
   - oxidative injury (oxidant-mediated endothelial damage) (cambrea2023boutonneusefeverin pages 2-4).
4. These mechanisms manifest clinically as **fever**, **rash**, and systemic organ dysfunction/complications in severe cases (sit2024pathogenicrickettsiaspp. pages 5-6, lamloumi2025epidemiologyandclinical pages 8-9).

### 6.2 Molecular pathways / immune mediators
- **Signaling cascades in endothelial activation:** NF-κB and MAPK pathways (cambrea2023boutonneusefeverin pages 2-4).
- **Type I interferon response:** IFN-β production by infected endothelial cells with STAT-family activation interfering with intracellular replication (cambrea2023boutonneusefeverin pages 2-4).
- **Th1 cellular immunity:** IFN-γ and TNF-α synergy inducing microbicidal nitric oxide (NOS2) and other killing mechanisms (cambrea2023boutonneusefeverin pages 2-4, sousa2008mediterraneanspottedfever pages 17-21).
- **Nutritional immunity:** IDO-mediated tryptophan degradation limiting growth (cambrea2023boutonneusefeverin pages 2-4, sousa2008mediterraneanspottedfever pages 17-21).
- **Entry/cell-to-cell spread:** OmpA/OmpB-mediated adhesion, Ku70 involvement, host actin remodeling (Arp2/3, Cdc42, PI3K, c-Src) and actin-based motility for spread (sousa2008mediterraneanspottedfever pages 46-49).

### 6.3 Suggested ontology mappings
- **GO Biological Process (suggested):**
  - endothelial cell activation; inflammatory response; cytokine-mediated signaling; nitric oxide biosynthetic process; tryptophan catabolic process; regulation of vascular permeability.
- **Cell types (CL; suggested):**
  - vascular endothelial cell; macrophage; dendritic cell; NK cell; CD4+ T cell; CD8+ T cell (supported by mechanistic descriptions) (cambrea2023boutonneusefeverin pages 2-4).
- **Anatomy (UBERON; suggested):**
  - skin; dermis; vascular endothelium; microvasculature; spleen/liver (organ involvement in severe disease discussed) (lamloumi2025epidemiologyandclinical pages 8-9).

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- **Primary:** skin and **microvasculature/endothelium** (vasculitis) (cambrea2023boutonneusefeverin pages 2-4, sit2024pathogenicrickettsiaspp. pages 5-6).
- **Complication organs reported in cohorts:** neurologic (encephalitis/vasculitis), ocular (chorioretinitis/uveitis), renal failure, pancreatitis, respiratory complications (ARDS/pulmonary edema) (lamloumi2025epidemiologyandclinical pages 8-9, cambrea2023boutonneusefeverin pages 4-5).

### 7.2 Tissue/cell level
- Endothelial cells of small/medium vessels are the main pathological target; additional infection of macrophages and hepatocytes is described (cambrea2023boutonneusefeverin pages 2-4).

---

## 8. Temporal Development

### 8.1 Onset pattern
- **Acute** febrile illness; incubation windows differ by report and recall, e.g., 6–16 days reported in Romanian review synthesis and 1–11 days (mean 3.8 ± 3) in the Tunisian cohort (cambrea2023boutonneusefeverin pages 4-5, lamloumi2025epidemiologyandclinical pages 2-3).

### 8.2 Course
- Often improves rapidly after doxycycline: Tunisian cohort reported fever resolution in ~2.8 ± 1.3 days (lamloumi2025epidemiologyandclinical pages 1-2).

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent quantitative data)
**Romania (southeastern focus; aggregated surveillance review, published 2023-11-09)**
- Incidence 2000–2016: **0.3–4.2 per 100,000** overall; hotspots: Tulcea **15.76/100,000**, Constanța **5.73/100,000** (cambrea2023boutonneusefeverin pages 2-4).

**Tunisia (single-center hospitalized adult cohort; 2000–2020; published 2025)**
- 173 hospitalized MSF cases; **67.6% male**, mean age ~40, **72–75% animal exposure**, **68.8% hot season**, none in winter (lamloumi2025epidemiologyandclinical pages 1-2, lamloumi2025epidemiologyandclinical pages 3-6).

**Portugal (older but mechanistically informative epidemiology; dissertation abstract)**
- 1989–2005 incidence **8.4 per 100,000**; district-level peaks reported; climate-related seasonal shift suggested (sousa2008mediterraneanspottedfever pages 17-21).

### 9.2 Population demographics
- Male predominance in Tunisian hospitalized cohort (67.6%) (lamloumi2025epidemiologyandclinical pages 1-2).

---

## 10. Diagnostics

### 10.1 Clinical criteria and differential diagnosis
- Classic diagnostic clinical anchor: fever + rash (often palms/soles) + eschar (but triad absent in ~30% in Tunisia) (lamloumi2025epidemiologyandclinical pages 1-2).

### 10.2 Laboratory tests / biomarkers
- **Serology:** IFA/IFAT is widely referenced as serologic gold standard; diagnostic interpretation requires paired sera when possible due to delayed seroconversion and cross-reactivity within spotted fever group (dalmanoglu2025rickettsiosiscasespresenting pages 4-5, xing2024usefulnessofnextgeneration pages 2-4).
  - Example thresholds from a Turkish MSF report: single-serum negative if IgM <1/192 and IgG <1/40; four-fold rise is significant (dalmanoglu2025rickettsiosiscasespresenting pages 4-5).

- **PCR:** evidence across reviews emphasizes that **skin/eschar biopsy or swabs outperform blood** early because rickettsemia is low/transient (marques2024spottedfeverdiagnosis pages 2-3, dalmanoglu2025rickettsiosiscasespresenting pages 4-5).

### 10.3 Recent diagnostic developments (2023–2025)
- **mNGS/NGS for rickettsioses (2024):** positioned as a complement to serology for culture-negative infections and cases missed by older tests (published 2024-10; URL https://doi.org/10.1371/journal.pntd.0012546) (xing2024usefulnessofnextgeneration pages 2-4).
- **Real-time PCR “toolbox” (2024):** genus-specific assays detecting as few as **10 copies** in human-DNA background to support rapid diagnosis of febrile syndromes including *Rickettsia* (published 2024-01; URL https://doi.org/10.1007/s10096-024-04760-8) (vegagarcia2024amoleculartoolbox pages 1-2).
- **Prototype rapid antigen LFA (2025):** detects rickettsial biomarker RC0497; animal-panel sensitivity 95.5% (21/22), specificity 100% in tested negatives; LOD 0.64 ng/mL in spiked human sera (published 2025-01; URL https://doi.org/10.1371/journal.pone.0312819) (willson2025developmentofa pages 1-2).

---

## 11. Outcome / Prognosis

### 11.1 Prognosis with treatment
- In the Tunisian hospitalized cohort, complications were uncommon (2.3%) and **all patients recovered** without relapse; no deaths reported (lamloumi2025epidemiologyandclinical pages 1-2, lamloumi2025epidemiologyandclinical pages 6-7).

### 11.2 Mortality / severe disease
- Literature summarized within Tunisia cohort discussion reports case-fatality ranges of 0–3% (lamloumi2025epidemiologyandclinical pages 8-9).
- Severe disease risk is influenced by strain and host factors in Portuguese experience summarized in dissertation abstract (sousa2008mediterraneanspottedfever pages 17-21).

---

## 12. Treatment

### 12.1 First-line pharmacotherapy
- **Doxycycline** is the cornerstone therapy across modern case series/cohorts.
  - Tunisia cohort: doxycycline resolved fever in **2.8 ± 1.3 days** (range 1–5) (lamloumi2025epidemiologyandclinical pages 1-2).
  - Turkish case series: doxycycline 100 mg twice daily for 10 days with full recovery (dalmanoglu2025rickettsiosiscasespresenting pages 1-2).

**MAXO suggestions (not exhaustive):**
- **MAXO:0000058 (Antibiotic therapy)** (suggested for doxycycline; ontology ID may vary by MAXO release).
- **MAXO:0001020 (Tick control / ectoparasite control)** (suggested; for prevention).

### 12.2 Treatment strategy (implementation)
- Evidence emphasizes rapid treatment after clinical suspicion, because confirmatory serology may be delayed and PCR sensitivity depends on sampling/timing (xing2024usefulnessofnextgeneration pages 2-4, dalmanoglu2025rickettsiosiscasespresenting pages 4-5).

---

## 13. Prevention

### 13.1 Primary prevention
- Core strategy: **tick avoidance and dog tick control** (vector management), plus awareness and surveillance in endemic seasons (cambrea2023boutonneusefeverin pages 1-2, lamloumi2025epidemiologyandclinical pages 3-6).
- Example of effective integrated control: Crimea implemented epidemiologic surveillance + veterinary/environmental tick control + dog-owner education (1958–1960), producing near-elimination and sustained low incidence for decades (gafarova2023historyandcurrent pages 1-2).

### 13.2 Secondary/tertiary prevention
- Early recognition and early doxycycline to reduce complications and severe outcomes (lamloumi2025epidemiologyandclinical pages 1-2).

---

## 14. Other Species / Natural Disease
- Dogs are repeatedly described as important reservoirs/sentinels for *R. conorii* transmission ecology (cambrea2023boutonneusefeverin pages 1-2, lamloumi2025epidemiologyandclinical pages 3-6).

---

## 15. Model Organisms
- Mechanistic literature and diagnostic development studies use animal models for spotted fever rickettsioses (e.g., *R. conorii*-infected mice used in antigen detection assay development) (willson2025developmentofa pages 1-2).

---

## Visual evidence (vector distribution vs cases)
Cambrea et al. include a Romania map relating BF distribution to *Rhipicephalus sanguineus* distribution (Figure 1), supporting the ecological link between vector range and human cases (cambrea2023boutonneusefeverin media c8da9f45, cambrea2023boutonneusefeverin media e684792e).

---

## Summary evidence table
| Domain | Key points (with quantitative data) | Key sources (author/year/URL) |
|---|---|---|
| Definition | Boutonneuse fever (BF), also called Mediterranean spotted fever (MSF) or Marseille fever, is a tick-borne spotted fever caused mainly by *Rickettsia conorii* and classically associated with an eschar (“tache noire”), fever, and rash. (cambrea2023boutonneusefeverin pages 1-2, gafarova2023historyandcurrent pages 1-2) | Cambrea 2023, https://doi.org/10.3390/microorganisms11112734; Gafarova 2023, https://doi.org/10.3390/pathogens12091161 |
| Pathogen | Main agent: *Rickettsia conorii* subsp. *conorii*; related subspecies/strains include Israeli spotted fever strain, *R. conorii* subsp. *israelensis*, *caspia*, and *indica*. Strain-level differences may affect virulence. (gafarova2023historyandcurrent pages 1-2, sousa2008mediterraneanspottedfever pages 17-21, sousa2008mediterraneanspottedfever pages 29-34) | Gafarova 2023, https://doi.org/10.3390/pathogens12091161; Sousa 2008, source text; historical taxonomy in Sousa 2008, source text |
| Vector / reservoir | Principal vector and reservoir: brown dog tick *Rhipicephalus sanguineus*; dogs are important vertebrate reservoirs/sentinels, with other mammals occasionally implicated. Historical vector-control campaigns reduced incidence in Crimea to 0.4–1.44 per 100,000. (cambrea2023boutonneusefeverin pages 1-2, gafarova2023historyandcurrent pages 1-2, gafarova2023historyandcurrent pages 2-4) | Cambrea 2023, https://doi.org/10.3390/microorganisms11112734; Gafarova 2023, https://doi.org/10.3390/pathogens12091161 |
| Endemic regions | Endemic across the Mediterranean basin and Black Sea regions; also reported in Africa, Middle East, Indian subcontinent, and China. In southeastern Romania, incidence during 2000–2016 ranged 0.3–4.2/100,000 overall, peaking at 15.76/100,000 in Tulcea and 5.73/100,000 in Constanța. (gafarova2023historyandcurrent pages 1-2, cambrea2023boutonneusefeverin pages 2-4) | Gafarova 2023, https://doi.org/10.3390/pathogens12091161; Cambrea 2023, https://doi.org/10.3390/microorganisms11112734 |
| Incubation / seasonality | Incubation reported around 6–16 days in Romanian review data; Tunisia cohort reported mean 3.8 ± 3 days (range 1–11) from recalled exposure. Strong warm-season clustering: Tunisia 68.8% in hot season, August peak 32.4%, none in winter; Romania peaks noted in May and July. (cambrea2023boutonneusefeverin pages 4-5, lamloumi2025epidemiologyandclinical pages 2-3, cambrea2023boutonneusefeverin pages 2-4) | Cambrea 2023, https://doi.org/10.3390/microorganisms11112734; Lamloumi 2025, https://doi.org/10.1017/S095026882400178X |
| Classic triad and symptom frequencies | Classic triad (fever + rash + eschar) occurred in 69.9% of Tunisian hospitalized adults. Tunisia: fever/rash 100%, eschar 69.9%, maculopapular rash 83.8%, palms/soles 98.3%, headache 64.5%, myalgia 60.7%, arthralgia 57.2%. Romania datasets: fever ~97.5–99.4%, rash ~97%, eschar 57.9–75.23%, headache/myalgia common; dog/tick exposure ~67–96%. (lamloumi2025epidemiologyandclinical pages 1-2, cambrea2023boutonneusefeverin pages 4-5, lamloumi2025epidemiologyandclinical pages 3-6) | Lamloumi 2025, https://doi.org/10.1017/S095026882400178X; Cambrea 2023, https://doi.org/10.3390/microorganisms11112734 |
| Key laboratory abnormalities | Tunisia: leukocytosis 36.4%, thrombocytopenia 48%, elevated AST 50.9%; broader discussion noted hyponatremia ~50.9% and transaminase elevation ~79%. Romania: leukocytosis 31.8%, thrombocytopenia 50.9%, elevated fibrinogen 55.1%, elevated transaminases 79.5%. (lamloumi2025epidemiologyandclinical pages 1-2, cambrea2023boutonneusefeverin pages 4-5, lamloumi2025epidemiologyandclinical pages 8-9) | Lamloumi 2025, https://doi.org/10.1017/S095026882400178X; Cambrea 2023, https://doi.org/10.3390/microorganisms11112734 |
| Diagnostics | Best early molecular yield comes from eschar/skin biopsy or swab; blood PCR is less sensitive because rickettsemia is low/transient. IFA/IFAT remains serologic gold standard; example single-serum negatives were IgM <1/192 and IgG <1/40, while a four-fold rise supports diagnosis. Sequencing is useful for species-level confirmation due to serologic cross-reactivity. (marques2024spottedfeverdiagnosis pages 2-3, dalmanoglu2025rickettsiosiscasespresenting pages 4-5, xing2024usefulnessofnextgeneration pages 2-4) | Marques 2024, https://doi.org/10.1590/0037-8682-0226-2024; Dalmanoğlu 2025, https://doi.org/10.1590/S1678-9946202567041; Xing 2024, https://doi.org/10.1371/journal.pntd.0012546 |
| Treatment | Doxycycline is first-line. Tunisia cohort: fever resolved in mean 2.8 ± 1.3 days after doxycycline; no deaths in that cohort. Turkish case series used doxycycline 100 mg twice daily for 10 days with full recovery. Romanian review notes symptoms often improve within ~48 h and disease clears in ~10 days after treatment. (lamloumi2025epidemiologyandclinical pages 1-2, cambrea2023boutonneusefeverin pages 4-5, dalmanoglu2025rickettsiosiscasespresenting pages 1-2) | Lamloumi 2025, https://doi.org/10.1017/S095026882400178X; Dalmanoğlu 2025, https://doi.org/10.1590/S1678-9946202567041; Cambrea 2023, https://doi.org/10.3390/microorganisms11112734 |
| Prevention / control | Prevention centers on tick avoidance/control, dog tick control, surveillance, clinician awareness, and One Health approaches. Crimea’s integrated campaign (epidemiologic surveillance, veterinary/environmental tick control, dog-owner education) markedly reduced incidence. Recent animal/human surveillance studies emphasize companion animals as sentinels and regional surveillance under climate change. (gafarova2023historyandcurrent pages 2-4, gafarova2023historyandcurrent pages 1-2, cambrea2023boutonneusefeverin pages 1-2) | Gafarova 2023, https://doi.org/10.3390/pathogens12091161; Cambrea 2023, https://doi.org/10.3390/microorganisms11112734 |
| Recent developments | 2024 molecular toolbox: genus-specific real-time PCR assays detecting as few as 10 copies in 300 ng human DNA for febrile illnesses including *Rickettsia*. 2024 mNGS/NGS: increasingly used to diagnose culture-negative rickettsioses and complement serology/PCR. 2025 prototype antigen LFA targeting RC0497: 21/22 infected animal sera positive (95.5%), specificity 100% in tested negatives, LOD 0.64 ng/mL in spiked human serum. (vegagarcia2024amoleculartoolbox pages 1-2, xing2024usefulnessofnextgeneration pages 2-4, willson2025developmentofa pages 1-2) | Vega-García 2024, https://doi.org/10.1007/s10096-024-04760-8; Xing 2024, https://doi.org/10.1371/journal.pntd.0012546; Willson 2025, https://doi.org/10.1371/journal.pone.0312819 |


*Table: This table summarizes the most actionable facts on Boutonneuse fever/Mediterranean spotted fever, including epidemiology, clinical frequencies, diagnostics, treatment, prevention, and recent diagnostic innovations. It is designed as a compact evidence snapshot for a disease knowledge base or research report.*

---

## Notes on evidence gaps and constraints
1. **Ontology identifiers (MONDO/Orphanet/MeSH specific to BF/MSF)** were not explicitly available in the retrieved full texts, so they are not asserted here with primary citations.
2. Some mechanistic and strain-virulence evidence comes from a dissertation text (Sousa 2008) which is not a peer-reviewed journal article; it is used here only where it provides specific quantitative/qualitative statements not otherwise present in the 2023–2025 journal corpus (sousa2008mediterraneanspottedfever pages 17-21).

---

## Key recent sources (prioritized 2023–2025)
- Cambrea SC et al. **2023-11-09**. *Boutonneuse Fever in Southeastern Romania*. **Microorganisms**. https://doi.org/10.3390/microorganisms11112734 (cambrea2023boutonneusefeverin pages 1-2, cambrea2023boutonneusefeverin pages 2-4)
- Gafarova MT, Eremeeva ME. **2023-09-14**. *History and Current Status of Mediterranean Spotted Fever in the Black Sea Region*. **Pathogens**. https://doi.org/10.3390/pathogens12091161 (gafarova2023historyandcurrent pages 1-2, gafarova2023historyandcurrent pages 2-4)
- Vega-García E et al. **2024-01**. *A molecular toolbox for fast diagnosis of bacterial causes of fever of intermediate duration*. **EJCMID**. https://doi.org/10.1007/s10096-024-04760-8 (vegagarcia2024amoleculartoolbox pages 1-2)
- Xing F et al. **2024-10**. *Usefulness of next-generation sequencing for laboratory diagnosis of rickettsiosis*. **PLOS NTD**. https://doi.org/10.1371/journal.pntd.0012546 (xing2024usefulnessofnextgeneration pages 2-4)
- Willson R et al. **2025-01**. *Rapid antigen lateral flow assay for spotted fever rickettsioses (RC0497)*. **PLOS ONE**. https://doi.org/10.1371/journal.pone.0312819 (willson2025developmentofa pages 1-2)
- Lamloumi M et al. **2025**. *Epidemiology and clinical characteristics of MSF suspects (Tunisia, 2000–2020)*. **Epidemiology & Infection**. https://doi.org/10.1017/S095026882400178X (lamloumi2025epidemiologyandclinical pages 3-6, lamloumi2025epidemiologyandclinical pages 1-2)



References

1. (gafarova2023historyandcurrent pages 1-2): Muniver T. Gafarova and Marina E. Eremeeva. History and current status of mediterranean spotted fever (msf) in the crimean peninsula and neighboring regions along the black sea coast. Pathogens, 12:1161, Sep 2023. URL: https://doi.org/10.3390/pathogens12091161, doi:10.3390/pathogens12091161. This article has 7 citations.

2. (cambrea2023boutonneusefeverin pages 2-4): Simona Claudia Cambrea, Diana Badiu, Constantin Ionescu, Roxana Penciu, Loredana Pazara, Cristina Maria Mihai, Mara Andreea Cambrea, and Larisia Mihai. Boutonneuse fever in southeastern romania. Microorganisms, 11:2734, Nov 2023. URL: https://doi.org/10.3390/microorganisms11112734, doi:10.3390/microorganisms11112734. This article has 4 citations.

3. (cambrea2023boutonneusefeverin pages 1-2): Simona Claudia Cambrea, Diana Badiu, Constantin Ionescu, Roxana Penciu, Loredana Pazara, Cristina Maria Mihai, Mara Andreea Cambrea, and Larisia Mihai. Boutonneuse fever in southeastern romania. Microorganisms, 11:2734, Nov 2023. URL: https://doi.org/10.3390/microorganisms11112734, doi:10.3390/microorganisms11112734. This article has 4 citations.

4. (lamloumi2025epidemiologyandclinical pages 1-2): Meriam Lamloumi, Aida Berriche, Souheil Zayet, Boutheina Mahdi, Imen Beji, Rim Abdelmalek, Lamia Ammari, and Badreddine Kilani. Epidemiology and clinical characteristics of mediterranean spotted fever suspects in a university hospital, tunisia, 2000–2020. Epidemiology and Infection, Dec 2025. URL: https://doi.org/10.1017/s095026882400178x, doi:10.1017/s095026882400178x. This article has 5 citations and is from a peer-reviewed journal.

5. (cambrea2023boutonneusefeverin pages 4-5): Simona Claudia Cambrea, Diana Badiu, Constantin Ionescu, Roxana Penciu, Loredana Pazara, Cristina Maria Mihai, Mara Andreea Cambrea, and Larisia Mihai. Boutonneuse fever in southeastern romania. Microorganisms, 11:2734, Nov 2023. URL: https://doi.org/10.3390/microorganisms11112734, doi:10.3390/microorganisms11112734. This article has 4 citations.

6. (sit2024pathogenicrickettsiaspp. pages 5-6): Brandon Sit and Rebecca L. Lamason. Pathogenic <i>rickettsia</i> spp. as emerging models for bacterial biology. Journal of Bacteriology, Feb 2024. URL: https://doi.org/10.1128/jb.00404-23, doi:10.1128/jb.00404-23. This article has 26 citations and is from a peer-reviewed journal.

7. (NCT07307651 chunk 1):  Implementation of an RT-PCR Assay for the Diagnosis of Rickettsia Spp. Infection. IRCCS Azienda Ospedaliero-Universitaria di Bologna. 2026. ClinicalTrials.gov Identifier: NCT07307651

8. (sousa2008mediterraneanspottedfever pages 29-34): RM Sousa. Mediterranean spotted fever and identification of new agents of rickettsioses in portugal: epidemiological determinants, host and microbial features in portuguese …. Unknown journal, 2008.

9. (lamloumi2025epidemiologyandclinical pages 3-6): Meriam Lamloumi, Aida Berriche, Souheil Zayet, Boutheina Mahdi, Imen Beji, Rim Abdelmalek, Lamia Ammari, and Badreddine Kilani. Epidemiology and clinical characteristics of mediterranean spotted fever suspects in a university hospital, tunisia, 2000–2020. Epidemiology and Infection, Dec 2025. URL: https://doi.org/10.1017/s095026882400178x, doi:10.1017/s095026882400178x. This article has 5 citations and is from a peer-reviewed journal.

10. (hosseininasab2024rickettsiaconoriisubsp. pages 2-4): Ali Hosseininasab, Safoura MoradKasani, Ehsan Mostafavi, Neda Baseri, Maryam Sadeghi, and Saber Esmaeili. Rickettsia conorii subsp. israelensis infection in a pediatric patient presenting skin rash and abdominal pain: a case report from southeast iran. BMC Infectious Diseases, Jan 2024. URL: https://doi.org/10.1186/s12879-024-09002-y, doi:10.1186/s12879-024-09002-y. This article has 2 citations and is from a peer-reviewed journal.

11. (dalmanoglu2025rickettsiosiscasespresenting pages 1-2): Enes Dalmanoğlu, Mehmet Ali Tüz, Hande İdil Tüz, and Derya Tuna Ecer. Rickettsiosis cases presenting with rash: a case series from an endemic region in turkey. Revista do Instituto de Medicina Tropical de São Paulo, Jun 2025. URL: https://doi.org/10.1590/s1678-9946202567041, doi:10.1590/s1678-9946202567041. This article has 0 citations.

12. (sousa2008mediterraneanspottedfever pages 17-21): RM Sousa. Mediterranean spotted fever and identification of new agents of rickettsioses in portugal: epidemiological determinants, host and microbial features in portuguese …. Unknown journal, 2008.

13. (lamloumi2025epidemiologyandclinical pages 8-9): Meriam Lamloumi, Aida Berriche, Souheil Zayet, Boutheina Mahdi, Imen Beji, Rim Abdelmalek, Lamia Ammari, and Badreddine Kilani. Epidemiology and clinical characteristics of mediterranean spotted fever suspects in a university hospital, tunisia, 2000–2020. Epidemiology and Infection, Dec 2025. URL: https://doi.org/10.1017/s095026882400178x, doi:10.1017/s095026882400178x. This article has 5 citations and is from a peer-reviewed journal.

14. (xing2024usefulnessofnextgeneration pages 2-4): Fanfan Xing, Chaowen Deng, Jinyue Huang, Yanfei Yuan, Zhendong Luo, Simon K. F. Lo, Susanna K. P. Lau, and Patrick C. Y. Woo. Usefulness of next-generation sequencing for laboratory diagnosis of rickettsiosis. PLOS Neglected Tropical Diseases, 18:e0012546, Oct 2024. URL: https://doi.org/10.1371/journal.pntd.0012546, doi:10.1371/journal.pntd.0012546. This article has 7 citations and is from a domain leading peer-reviewed journal.

15. (gafarova2023historyandcurrent pages 26-26): Muniver T. Gafarova and Marina E. Eremeeva. History and current status of mediterranean spotted fever (msf) in the crimean peninsula and neighboring regions along the black sea coast. Pathogens, 12:1161, Sep 2023. URL: https://doi.org/10.3390/pathogens12091161, doi:10.3390/pathogens12091161. This article has 7 citations.

16. (sousa2008mediterraneanspottedfever pages 46-49): RM Sousa. Mediterranean spotted fever and identification of new agents of rickettsioses in portugal: epidemiological determinants, host and microbial features in portuguese …. Unknown journal, 2008.

17. (lamloumi2025epidemiologyandclinical pages 2-3): Meriam Lamloumi, Aida Berriche, Souheil Zayet, Boutheina Mahdi, Imen Beji, Rim Abdelmalek, Lamia Ammari, and Badreddine Kilani. Epidemiology and clinical characteristics of mediterranean spotted fever suspects in a university hospital, tunisia, 2000–2020. Epidemiology and Infection, Dec 2025. URL: https://doi.org/10.1017/s095026882400178x, doi:10.1017/s095026882400178x. This article has 5 citations and is from a peer-reviewed journal.

18. (dalmanoglu2025rickettsiosiscasespresenting pages 4-5): Enes Dalmanoğlu, Mehmet Ali Tüz, Hande İdil Tüz, and Derya Tuna Ecer. Rickettsiosis cases presenting with rash: a case series from an endemic region in turkey. Revista do Instituto de Medicina Tropical de São Paulo, Jun 2025. URL: https://doi.org/10.1590/s1678-9946202567041, doi:10.1590/s1678-9946202567041. This article has 0 citations.

19. (marques2024spottedfeverdiagnosis pages 2-3): Helen Gonçalves Marques, Anna Julia Ribeiro, Anna Karolina de Oliveira Alfenas Gadelha, Carlos Ananias Aparecido Resende, Daniela Regiane da Silva, Débora Patrícia Martins de Deus, Isabelle Caroline Dos Santos Barcelos, Isabela Maia Pereira, Iago Tadeu Santos de Paula, Lucas Da Silva Lopes, Líria Souza Silva, Mariana Campos da Paz Lopes, Miguel Angel Chávez-Fumagalli, Eduardo Antônio Ferraz Coelho, Rodolfo Cordeiro Giunchetti, Ana Alice Maia Gonçalves, and Alexsandro Sobreira Galdino. Spotted fever diagnosis using molecular methods. Revista da Sociedade Brasileira de Medicina Tropical, Nov 2024. URL: https://doi.org/10.1590/0037-8682-0226-2024, doi:10.1590/0037-8682-0226-2024. This article has 2 citations.

20. (vegagarcia2024amoleculartoolbox pages 1-2): Elva Vega-García, Génesis Palacios, José A. Pérez, Mónica Vélez-Tobarias, Ana María Torres-Vega, Carlos Ascaso-Terrén, and Emma Carmelo. A molecular toolbox for fast and convenient diagnosis of emerging and reemerging bacterial pathogens causing fever of intermediate duration. European Journal of Clinical Microbiology & Infectious Diseases, 43:649-657, Jan 2024. URL: https://doi.org/10.1007/s10096-024-04760-8, doi:10.1007/s10096-024-04760-8. This article has 2 citations and is from a peer-reviewed journal.

21. (willson2025developmentofa pages 1-2): Richard Willson, Yingxin Zhao, Kristen Brosamer, Yogita Pal, Lucas S. Blanton, Esteban Arroyave, Carsen Roach, David H. Walker, Katerina Kourentzi, and Rong Fang. Development of a rapid antigen-based lateral flow assay for tick-borne spotted fever rickettsioses. PLOS ONE, 20:e0312819, Jan 2025. URL: https://doi.org/10.1371/journal.pone.0312819, doi:10.1371/journal.pone.0312819. This article has 4 citations and is from a peer-reviewed journal.

22. (lamloumi2025epidemiologyandclinical pages 6-7): Meriam Lamloumi, Aida Berriche, Souheil Zayet, Boutheina Mahdi, Imen Beji, Rim Abdelmalek, Lamia Ammari, and Badreddine Kilani. Epidemiology and clinical characteristics of mediterranean spotted fever suspects in a university hospital, tunisia, 2000–2020. Epidemiology and Infection, Dec 2025. URL: https://doi.org/10.1017/s095026882400178x, doi:10.1017/s095026882400178x. This article has 5 citations and is from a peer-reviewed journal.

23. (cambrea2023boutonneusefeverin media c8da9f45): Simona Claudia Cambrea, Diana Badiu, Constantin Ionescu, Roxana Penciu, Loredana Pazara, Cristina Maria Mihai, Mara Andreea Cambrea, and Larisia Mihai. Boutonneuse fever in southeastern romania. Microorganisms, 11:2734, Nov 2023. URL: https://doi.org/10.3390/microorganisms11112734, doi:10.3390/microorganisms11112734. This article has 4 citations.

24. (cambrea2023boutonneusefeverin media e684792e): Simona Claudia Cambrea, Diana Badiu, Constantin Ionescu, Roxana Penciu, Loredana Pazara, Cristina Maria Mihai, Mara Andreea Cambrea, and Larisia Mihai. Boutonneuse fever in southeastern romania. Microorganisms, 11:2734, Nov 2023. URL: https://doi.org/10.3390/microorganisms11112734, doi:10.3390/microorganisms11112734. This article has 4 citations.

25. (gafarova2023historyandcurrent pages 2-4): Muniver T. Gafarova and Marina E. Eremeeva. History and current status of mediterranean spotted fever (msf) in the crimean peninsula and neighboring regions along the black sea coast. Pathogens, 12:1161, Sep 2023. URL: https://doi.org/10.3390/pathogens12091161, doi:10.3390/pathogens12091161. This article has 7 citations.