---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T12:10:31.368589'
end_time: '2026-04-05T12:21:44.575475'
duration_seconds: 673.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alveolar Rhabdomyosarcoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alveolar Rhabdomyosarcoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Alveolar Rhabdomyosarcoma** covering all of the
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
- **Disease Name:** Alveolar Rhabdomyosarcoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Alveolar Rhabdomyosarcoma** covering all of the
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


## Disease Characteristics Research Report: Alveolar Rhabdomyosarcoma (ARMS)

### Target disease
**Alveolar rhabdomyosarcoma (ARMS)** is an aggressive rhabdomyosarcoma (RMS) subtype (a malignant mesenchymal tumor showing skeletal muscle differentiation) that occurs primarily in children, adolescents, and young adults and is typically managed with multimodality therapy (systemic chemotherapy plus local control with surgery and/or radiotherapy). (wasti2025childhoodadolescentand pages 2-4, pantelakis2025recentadvanceson pages 1-2)

| Topic | Key finding | Evidence type (human/model/in vitro/computational) | Quantitative/statistic | Citation details (first author, journal, year, PMID if present in text; otherwise DOI) | URL |
|---|---|---|---|---|---|
| Liquid biopsy / prognostic biomarker | Baseline ctDNA detection is feasible in intermediate-risk RMS and is prognostic; in fusion-positive RMS, detecting pathognomonic PAX3/7::FOXO1 rearrangements by Rhabdo-Seq was the best ctDNA strategy. (abbou2023circulatingtumordna pages 1-2) | Human clinical cohort | 124 patients total; ctDNA detected in 27/49 FP-RMS (55%); FP-RMS EFS 37% vs 70% and OS 39.2% vs 75% for ctDNA-positive vs ctDNA-negative cases. (abbou2023circulatingtumordna pages 1-2) | Abbou, *J Clin Oncol*, 2023, DOI: 10.1200/JCO.22.00409 (abbou2023circulatingtumordna pages 1-2) | https://doi.org/10.1200/JCO.22.00409 |
| Cell of origin / developmental biology | PAX3-FOXO1 can reprogram endothelial progenitors into fusion-positive RMS, supporting a non-myogenic cell of origin and showing activation of myogenic super-enhancers. (searcy2023pax3foxo1dictatesmyogenic pages 1-2, searcy2023pax3foxo1dictatesmyogenic media a3da86b9) | Mouse model + human iPSC + in vivo xenograft | “3-year survival rate for children with high-risk RMS has remained at 20%”; in ACP mice, 30% of 940 lineage-traced cells in SCM co-localized with PAX7; P3F-expressing TP53-null human iPSCs formed FP-RMS tumors in mice. (searcy2023pax3foxo1dictatesmyogenic pages 1-2, searcy2023pax3foxo1dictatesmyogenic media a3da86b9) | Searcy, *Nat Commun*, 2023, DOI: 10.1038/s41467-023-43044-1 (searcy2023pax3foxo1dictatesmyogenic pages 1-2) | https://doi.org/10.1038/s41467-023-43044-1 |
| Single-cell tumor states / heterogeneity | A unified single-cell atlas identified four dominant RMS cell states and showed that some FP-RMS tumors harbor tumor-acquired non-myogenic states, including a neuronal state, with implications for therapy resistance. (danielli2024singlecelltranscriptomic pages 1-2) | Human tumors + PDX + primary cultures + cell lines; single-cell computational analysis | 72 datasets integrated; 12 Louvain clusters collapsed into 4 dominant states: progenitor, proliferative, differentiated, and ground. (danielli2024singlecelltranscriptomic pages 1-2) | Danielli, *Nat Commun*, 2024, DOI: 10.1038/s41467-024-50527-2 (danielli2024singlecelltranscriptomic pages 1-2) | https://doi.org/10.1038/s41467-024-50527-2 |
| Epigenetic dependency / targeted therapy | Small-molecule KDM inhibitors P3FI-63/P3FI-90 suppress PAX3-FOXO1-driven transcriptional output; KDM3B emerged as the strongest biochemical target, and P3FI-90 showed in vivo antitumor activity. (kim2024kdm3binhibitorsdisrupt pages 1-2, kim2024kdm3binhibitorsdisrupt pages 10-12, kim2024kdm3binhibitorsdisrupt pages 2-3) | In vitro screen + biochemical assays + xenograft models + omics | 62,643-compound screen; P3FI-63 KDM3B IC50 = 7 µM; metastatic IV xenograft progression delayed (p=0.0016); orthotopic intramuscular model tumor-volume reduction (p=0.0046). (kim2024kdm3binhibitorsdisrupt pages 1-2, kim2024kdm3binhibitorsdisrupt pages 10-12, kim2024kdm3binhibitorsdisrupt pages 2-3) | Kim, *Nat Commun*, 2024, DOI: 10.1038/s41467-024-45902-y (kim2024kdm3binhibitorsdisrupt pages 1-2, kim2024kdm3binhibitorsdisrupt pages 10-12, kim2024kdm3binhibitorsdisrupt pages 2-3) | https://doi.org/10.1038/s41467-024-45902-y |
| Fusion diagnostics / molecular pathology | One-step RT-PCR on FFPE tissue is a reliable, low-cost method for fusion detection in soft tissue tumors, with high PAX3–FOXO1 detection in ARMS and concordance with FISH. (song2023detectionofvarious pages 1-2) | Human diagnostic cohort / molecular pathology | 242 cases tested, 213 evaluable; overall fusion-positive rate 60% (133/213); PAX3–FOXO1 detected in 31/35 ARMS (88.6%); FISH concordant in 18/18 tested cases. (song2023detectionofvarious pages 1-2) | Song, *Front Cell Dev Biol*, 2023, DOI: 10.3389/fcell.2023.1214262 (song2023detectionofvarious pages 1-2) | https://doi.org/10.3389/fcell.2023.1214262 |
| Fusion status and clinical aggressiveness | In RMS, PAX3–FOXO1 positivity correlated with lymph node metastasis, distant metastasis, and shorter overall survival, reinforcing fusion testing as clinically informative. (song2023detectionofvarious pages 1-2) | Human clinicopathologic correlation study | PAX3–FOXO1 status correlated with lymph node metastasis and distant metastasis; positive patients had significantly shorter OS than fusion-negative patients. (song2023detectionofvarious pages 1-2) | Song, *Front Cell Dev Biol*, 2023, DOI: 10.3389/fcell.2023.1214262 (song2023detectionofvarious pages 1-2) | https://doi.org/10.3389/fcell.2023.1214262 |


*Table: This table summarizes major 2023–2024 advances in alveolar/fusion-positive rhabdomyosarcoma across diagnostics, biology, prognosis, and therapeutic targeting. It is designed for rapid knowledge-base curation with quantitative findings, evidence type, and source links.*

---

## 1. Disease information

### 1.1 Concise overview
RMS is “a mesenchymal tumour showing skeletal muscle differentiation,” and ARMS is one of the major WHO-recognized RMS histologic subtypes. (wasti2025childhoodadolescentand pages 2-4, sankhe2025fusiononcogenesin pages 1-2)

A current clinical–biologic framing is that RMS comprises two dominant molecular groups: **fusion-positive (FP)** tumors (most often driven by **PAX3(7)::FOXO1** fusions and classically associated with alveolar histology) and **fusion-negative (FN)** tumors (more often embryonal histology and molecularly heterogeneous). (wasti2025childhoodadolescentand pages 2-4)

### 1.2 Synonyms / alternative names
Commonly used synonyms and near-synonyms in the literature include:
- “Alveolar RMS / aRMS” (histology-based)
- “Fusion-positive RMS / FP-RMS” (molecularly defined subset; largely overlaps classical ARMS) (wasti2025childhoodadolescentand pages 2-4, sankhe2025fusiononcogenesin pages 1-2)

### 1.3 Key identifiers (knowledge-base note)
In the retrieved corpus, standardized identifiers (MONDO, MeSH, ICD-10/ICD-11, Orphanet, OMIM) were not explicitly enumerated in-text; therefore, this report cannot provide a verified list from primary sources in context.

### 1.4 Evidence source type
Most information below is derived from **aggregated disease-level resources** (reviews, cooperative-group summaries, and prospective/retrospective cohorts) plus **primary translational studies** in cell lines, mouse models, xenografts, and patient-derived models. (wasti2025childhoodadolescentand pages 2-4, sankhe2025fusiononcogenesin pages 1-2, abbou2023circulatingtumordna pages 1-2, searcy2023pax3foxo1dictatesmyogenic pages 1-2, danielli2024singlecelltranscriptomic pages 1-2, kim2024kdm3binhibitorsdisrupt pages 1-2)

---

## 2. Etiology

### 2.1 Primary causal factors (genetic/mechanistic)
**Pathognomonic gene fusions** are central causal drivers for most ARMS/FP-RMS:
- ARMS frequently harbors **PAX3::FOXO1** or **PAX7::FOXO1** fusions; one review cites that ~**80% of ARMS** harbor these fusions. (wasti2025childhoodadolescentand pages 2-4)
- In a large RT-PCR fusion-detection cohort of soft tissue tumors, **PAX3–FOXO1** was detected in **88.6% (31/35)** of ARMS cases. (song2023detectionofvarious pages 1-2)

**Direct abstract quote (mechanistic framing):** Searcy et al. describe FP-RMS as “driven by the expression of the PAX3-FOXO1 (P3F) fusion oncoprotein” and emphasize that FP-RMS “occurs throughout the body in areas devoid of skeletal muscle,” motivating non-myogenic cell-of-origin models. (searcy2023pax3foxo1dictatesmyogenic pages 1-2)

### 2.2 Risk factors
**Clinical risk/prognostic factors (often used as risk stratifiers)** include fusion status, primary site, tumor size, age, extent of disease, nodal status, and metastatic status. (wasti2025childhoodadolescentand pages 1-2, wasti2025childhoodadolescentand pages 2-4)

In a pediatric single-center cohort from India (localized RMS with FOXO1 known, n=140), adverse baseline features were common (e.g., nodal disease ~39–40% and tumors >5 cm in ~56–60%), and in multivariable models, nodal involvement and very large tumor size (>10 cm) were adverse prognostic factors. (ramanathan2023outcomeandprognostic pages 11-13)

**Fusion status as a biologic risk factor:** PAX3–FOXO1 positivity in RMS was associated with lymph node metastasis and distant metastasis in a multi-center one-step RT-PCR study, and was linked to shorter overall survival. (song2023detectionofvarious pages 1-2)

### 2.3 Protective factors
No protective genetic variants or environmental protective factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence specific to ARMS was identified in the retrieved sources.

---

## 3. Phenotypes (clinical presentation)

### 3.1 Typical clinical phenotype (high-level)
ARMS is a malignant soft tissue tumor that can occur in multiple anatomic sites; one case-based review notes ARMS is prevalent in adolescents and “usually develops in the extremities and can also involve the trunk, perineum, and pelvis.” (song2023detectionofvarious pages 1-2)

### 3.2 Phenotype characteristics (structured suggestions)
Evidence in the retrieved corpus is strongest for **oncologic phenotype** (local invasion, nodal/distant metastasis) rather than symptom frequency catalogs. The following HPO term suggestions are therefore provided as **knowledge-base candidates** (not all have frequencies in the cited sources):
- Mass of soft tissue (HP:0001417)
- Regional lymph node metastasis (HP:0032726)
- Distant metastasis (HP:0002665)
- Pain (HP:0012531) and swelling (HP:0000984) as common sarcoma presentations (not quantified in retrieved sources)

### 3.3 Quality of life impact
No ARMS-specific QoL instrument statistics were identified in the retrieved sources.

---

## 4. Genetic / molecular information

### 4.1 Causal genes / chromosomal abnormalities
**Core causal alterations (somatic):**
- **PAX3::FOXO1** and **PAX7::FOXO1** fusions define FP-RMS/ARMS biology and are key diagnostic and prognostic markers. (wasti2025childhoodadolescentand pages 2-4)

**Other poor-risk variants (contextual):** Cooperative-group summaries note additional poor-risk variants such as **MYOD1** and **TP53** in RMS risk stratification discussions. (wasti2025childhoodadolescentand pages 1-2)

### 4.2 Variant type/class and origin
- The canonical ARMS alterations are **structural rearrangements (chromosomal translocations)** yielding fusion transcription factors. (obeidin2023what’snewin pages 2-3, obeidin2023what’snewin pages 1-2)
- These are generally **somatic** drivers (germline predisposition was not specifically established for ARMS in the retrieved sources).

### 4.3 Epigenetic dependencies and regulators (mechanistic genetics)
Recent mechanistic work underscores epigenetic and transcriptional dependencies in FP-RMS:
- Searcy et al. report that PAX3-FOXO1 “functions as a pioneer transcription factor” and “activates myogenic super-enhancers that define RMS cell identity including MYOD1, MYOGENIN and MYCN.” (searcy2023pax3foxo1dictatesmyogenic pages 1-2)
- Kim et al. identify small-molecule **KDM3B**-selective inhibitors (P3FI-63/P3FI-90) that downregulate PAX3-FOXO1 transcriptional output and alter chromatin-associated features at PAX3-FOXO1 sites; P3FI-63 inhibits KDM3B with **IC50 = 7 µM**. (kim2024kdm3binhibitorsdisrupt pages 2-3)

---

## 5. Environmental information
No disease-specific environmental, lifestyle, toxin, radiation, or infectious causal factors for ARMS were identified in the retrieved sources.

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (current synthesis)
1) **Initiating genomic event**: a PAX3/7::FOXO1 fusion forms an aberrant transcription factor in FP-RMS/ARMS. (wasti2025childhoodadolescentand pages 2-4, searcy2023pax3foxo1dictatesmyogenic pages 1-2)
2) **Transcriptional reprogramming**: PAX3-FOXO1 can reprogram non-myogenic progenitors; Searcy et al. demonstrate PAX3-FOXO1 “reprograms mouse and human endothelial progenitors to FP-RMS.” (searcy2023pax3foxo1dictatesmyogenic pages 1-2)
3) **Epigenetic remodeling and super-enhancer activation**: PAX3-FOXO1 “activates myogenic super-enhancers” and establishes RMS cell identity programs. (searcy2023pax3foxo1dictatesmyogenic pages 1-2, searcy2023pax3foxo1dictatesmyogenic media 14ad6904)
4) **Cell-state heterogeneity and therapy resistance**: single-cell profiling identifies dominant RMS cell states and shows FP-RMS can include tumor-acquired, non-developmental programs (e.g., a neuronal state) that may persist after therapy. (danielli2024singlecelltranscriptomic pages 1-2)
5) **Clinical phenotype**: aggressive local behavior and higher propensity for metastasis and poor outcomes in fusion-positive disease cohorts. (wasti2025childhoodadolescentand pages 2-4, song2023detectionofvarious pages 1-2)

### 6.2 2023–2024 mechanistic developments (selected)
- **Cell of origin and lineage plasticity (Nov 2023, Nature Communications):** Searcy et al. generate an endothelial-driven FP-RMS model and report lineage-traced myogenic stem-cell features; for example, in their ACP model “of 940 Tom+ cells counted in the SCM … 30% co-localized with PAX7.” (searcy2023pax3foxo1dictatesmyogenic pages 1-2, searcy2023pax3foxo1dictatesmyogenic media a3da86b9)
- **Single-cell atlas of RMS (Jul 2024, Nature Communications):** Danielli et al. integrate 72 datasets and identify four dominant muscle-lineage cell states (progenitor, proliferative, differentiated, ground), with some FP-RMS tumors containing tumor-acquired neuronal cell states not observed in normal myogenesis. (danielli2024singlecelltranscriptomic pages 1-2)
- **Epigenetic drug discovery (Feb 2024, Nature Communications):** Kim et al. screen 62,643 compounds and develop KDM3B-selective inhibitors that suppress FP-RMS growth in vivo; e.g., P3FI-90 delayed tumor progression in a metastatic IV xenograft model (p=0.0016) and reduced tumor volume in an orthotopic intramuscular model (p=0.0046). (kim2024kdm3binhibitorsdisrupt pages 1-2, kim2024kdm3binhibitorsdisrupt pages 10-12)

### 6.3 Suggested ontology terms (mechanisms)
**GO biological process (suggestions):**
- Regulation of transcription by RNA polymerase II (GO:0006357)
- Chromatin organization (GO:0006325)
- Skeletal muscle cell differentiation (GO:0035914)
- Cell cycle process (GO:0022402)
- Apoptotic process (GO:0006915)

**Cell types (CL suggestions):**
- Endothelial cell (CL:0000115) (supported conceptually by endothelial progenitor reprogramming) (searcy2023pax3foxo1dictatesmyogenic pages 1-2)
- Myoblast / skeletal muscle precursor (e.g., CL:0000056 myoblast)

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level
ARMS is a **soft tissue** sarcoma that frequently arises in skeletal muscle-associated soft tissues but can occur at sites without skeletal muscle, consistent with reprogramming models and broad anatomic distribution. (searcy2023pax3foxo1dictatesmyogenic pages 1-2)

**Common sites in cited literature:** extremities, trunk, perineum/pelvis. (song2023detectionofvarious pages 1-2)

### 7.2 UBERON suggestions
- Skeletal muscle tissue (UBERON:0001134)
- Pelvis (UBERON:0001270)
- Lymph node (UBERON:0000029)

---

## 8. Temporal development

### 8.1 Onset
RMS is predominantly pediatric/adolescent; ARMS is noted as prevalent in adolescents in clinical literature. (song2023detectionofvarious pages 1-2)

### 8.2 Progression
High-risk biology is linked to fusion-positive status, nodal involvement, and metastatic presentation; relapses commonly occur within ~2 years in one cohort (median relapse ~18 months). (ramanathan2023outcomeandprognostic pages 4-7)

---

## 9. Inheritance and population

### 9.1 Epidemiology (disease burden)
RMS accounts for ~3% of childhood cancers, with ~400–500 cases diagnosed annually in the United States (all RMS). (sankhe2025fusiononcogenesin pages 1-2)

### 9.2 Demographics (selected)
In a localized RMS cohort with FOXO1 status known (n=140), the median age was 4.4 years and the sex ratio was ~2.1:1 (boys:girls). (ramanathan2023outcomeandprognostic pages 2-4)

### 9.3 Fusion prevalence in clinical cohorts
- Cooperative-group synthesis: ~80% of ARMS harbor PAX3/7::FOXO1 fusions. (wasti2025childhoodadolescentand pages 2-4)
- Single-center cohort (localized RMS with fusion known): among ARMS, **25/49 (51%)** were FOXO1 fusion-positive (PAX3–FOXO1 or PAX7–FOXO1). (ramanathan2023outcomeandprognostic pages 4-7)
- Multi-center diagnostic RT-PCR cohort: **PAX3–FOXO1 in 31/35 ARMS (88.6%)**. (song2023detectionofvarious pages 1-2)

(These differences likely reflect case mix, assay targets, and classification differences across cohorts; the retrieved sources did not provide a harmonized prevalence estimate.)

---

## 10. Diagnostics

### 10.1 Histopathology and immunohistochemistry (IHC)
Molecular testing is frequently needed in soft tissue tumor diagnosis; a 2023 guideline-style review emphasizes that in rhabdomyoblastic tumors molecular confirmation can be important to distinguish embryonal from alveolar RMS when morphology/IHC are insufficient, with FOXO1 fusions serving as definitive classification markers. (obeidin2023what’snewin pages 2-3)

### 10.2 Molecular testing approaches (2023 best-practice themes)
A morphology-driven, tiered diagnostic strategy is recommended across sarcoma molecular-testing guidance:
- **FISH** remains useful, including break-apart probes when a fusion partner is unknown;
- **RT-PCR** can detect known fusion breakpoints but “generally lacks the ability to detect new fusion partners”;
- **RNA-based NGS** (hybrid-capture or anchored multiplex PCR) is increasingly adopted for sensitive fusion detection and novel partner discovery; methylation profiling is emerging for classification. (obeidin2023what’snewin pages 1-2)

### 10.3 ARMS-specific fusion testing performance data
Song et al. provide real-world performance data in FFPE tissues:
- Among evaluable samples (n=213), overall fusion-positive rate 60% (133/213).
- In ARMS, **PAX3–FOXO1** detected in **88.6% (31/35)**.
- FISH concordant with one-step RT-PCR in **18/18** tested cases.
These findings support one-step RT-PCR as an accurate, low-cost fusion assay in routine settings. (song2023detectionofvarious pages 1-2)

### 10.4 Liquid biopsy (2023 clinical implementation direction)
Abbou et al. (COG biorepository; intermediate-risk RMS) show that baseline ctDNA is detectable and prognostic:
- In FP-RMS, translocation-based ctDNA detection identified ctDNA in **27/49 (55%)**.
- Outcomes were worse with baseline ctDNA detection (FP-RMS OS **39.2% vs 75%**; EFS **37% vs 70%** for ctDNA-positive vs negative). (abbou2023circulatingtumordna pages 1-2)

**Direct abstract quote (purpose and conclusion excerpts):** The study states, “We sought to evaluate strategies for identifying circulating tumor DNA (ctDNA) in IR RMS and to determine whether ctDNA detection before therapy is associated with outcome,” and concludes that “baseline ctDNA detection is feasible and is prognostic in IR RMS.” (abbou2023circulatingtumordna pages 1-2)

### 10.5 Differential diagnosis (high-level)
ARMS frequently falls within the “small round blue cell tumor” differential; the retrieved sources emphasize molecular testing (FISH/RT-PCR/NGS) to resolve histologic overlap across entities. (obeidin2023what’snewin pages 1-2, choi2023therecentadvances pages 1-2)

---

## 11. Outcome / prognosis

### 11.1 Survival statistics (selected)
- In a cooperative-group synthesis, **fusion-positive tumors with locoregional nodal involvement (N1)** are a recognized poor-risk group; cited **5-year OS 45.5%** and **5-year EFS 43%**. (wasti2025childhoodadolescentand pages 2-4)
- A broad RMS epidemiology review reports risk-group survival ranges (all RMS): low-risk ~70–90%, intermediate 50–70%, high-risk 20–30%, and highlights worse outcomes in fusion-positive disease. (pantelakis2025recentadvanceson pages 1-2)

### 11.2 Prognostic factors (reproducible across cohorts)
Prognosis is strongly influenced by fusion status plus classic clinicopathologic factors including tumor site, size, nodal status, metastatic status, extent of resection/residual disease, and age. (wasti2025childhoodadolescentand pages 1-2, wasti2025childhoodadolescentand pages 2-4)

### 11.3 Recent prognostic biomarker: ctDNA
Baseline ctDNA detection adds prognostic resolution within intermediate-risk RMS, with large differences in OS/EFS by ctDNA status as reported above. (abbou2023circulatingtumordna pages 1-2)

---

## 12. Treatment

### 12.1 Standard of care (real-world implementation)
Standard RMS care remains **multimodality**: systemic multi-agent chemotherapy combined with surgery and/or radiotherapy for local control, delivered through risk-stratified cooperative-group protocols. (wasti2025childhoodadolescentand pages 2-4, pantelakis2025recentadvanceson pages 1-2)

### 12.2 Risk stratification increasingly incorporates fusion status
Fusion status is emphasized as a key prognostic biomarker used alongside clinical features to guide therapy intensity and duration; algorithms are evolving as molecular biology and genomics advance. (wasti2025childhoodadolescentand pages 1-2, wasti2025childhoodadolescentand pages 2-4)

### 12.3 Selected clinical trials (with real-world identifiers)
**Relapsed/refractory RMS (includes ARMS):**
- **NCT01222715** (start 2010; completed 2015): randomized phase II trial of vinorelbine + cyclophosphamide combined with either bevacizumab or temsirolimus; cycles every 21 days up to 12 courses; primary objectives included feasibility and estimation/comparison of EFS. (NCT01222715 chunk 1)
- **NCT03041701** (start 2017; terminated): open-label phase I/II of ganitumab (anti–IGF-1R) plus dasatinib (SFK inhibitor) in relapsed/refractory embryonal or alveolar RMS; terminated due to drug availability; phase II closed early. (NCT03041701 chunk 1)
- **NCT02867592** (start 2017; active-not-recruiting): phase II single-group cabozantinib (oral, continuous dosing) in children/young adults with refractory/recurrent solid tumors including rhabdomyosarcoma; primary endpoint objective response rate by RECIST v1.1 for non-osteosarcoma strata. (NCT02867592 chunk 1)

**High-risk RMS upfront strategy refinement:**
- **NCT04994132 / ARST2031** (start 2021; active-not-recruiting; estimated primary completion 2026): phase III comparing VINO-AC vs VAC induction approaches, followed by vinorelbine + oral cyclophosphamide maintenance for 24 weeks; includes correlative ctDNA and genomic prognostic objectives. (NCT04994132 chunk 1)

### 12.4 MAXO (Medical Action Ontology) suggestions
- Chemotherapy (MAXO:0000058)
- Surgical resection (MAXO:0000011)
- Radiotherapy (MAXO:0000014)
- Molecular genetic testing (MAXO:0001001)
- Liquid biopsy / ctDNA testing (MAXO suggestion; not validated in retrieved sources)

---

## 13. Prevention
No primary prevention strategies specific to ARMS were identified in the retrieved sources. Given the dominant role of somatic fusion oncogenes and the rarity of the disease, prevention focuses pragmatically on early diagnosis, referral to sarcoma centers, and enrollment in cooperative-group protocols (not quantitatively evaluated in retrieved sources).

---

## 14. Other species / natural disease
No naturally occurring ARMS analogs in non-human species were identified in the retrieved sources.

---

## 15. Model organisms and experimental models
Recent studies emphasize diverse model systems:
- **Genetically engineered mouse models and lineage tracing:** Searcy et al. develop an endothelial-driven PAX3-FOXO1 model and demonstrate reprogramming toward myogenic stem-like states and FP-RMS formation. (searcy2023pax3foxo1dictatesmyogenic pages 1-2, searcy2023pax3foxo1dictatesmyogenic media a3da86b9)
- **Human iPSC-based developmental models:** PAX3-FOXO1 expression in TP53-null iPSCs redirects differentiation and yields FP-RMS tumors in immunocompromised mice. (searcy2023pax3foxo1dictatesmyogenic pages 1-2)
- **Patient-derived xenografts and single-cell atlases:** Danielli et al. include patient tumors, PDXs, primary cultures, and cell lines in a unified single-cell analysis, enabling cross-model comparisons of cell states and therapy-associated changes. (danielli2024singlecelltranscriptomic pages 1-2)

Limitations noted implicitly by these approaches include model dependence on engineered genetic contexts (e.g., TP53-null backgrounds), and the challenge of faithfully capturing therapy-induced and tumor-acquired states in vitro.

---

## Expert synthesis / analysis (authoritative perspectives)
Across cooperative-group summaries, fusion status is consistently treated as a cornerstone biomarker that should be integrated into diagnostics and risk stratification, because it captures biology linked to adverse outcome and can refine treatment intensity. (wasti2025childhoodadolescentand pages 1-2, wasti2025childhoodadolescentand pages 2-4)

The 2023–2024 translational literature increasingly converges on the idea that FP-RMS is a **transcriptionally and epigenetically addicted** fusion-driven cancer, where vulnerabilities may lie in chromatin regulators (e.g., KDM dependencies) and in measurable tumor burden via ctDNA, rather than in high mutational burden targets. This framing is supported by direct functional studies (KDM3B inhibitors), developmental reprogramming models (endothelial progenitor origin), and clinical biomarker work (ctDNA prognostic value). (abbou2023circulatingtumordna pages 1-2, searcy2023pax3foxo1dictatesmyogenic pages 1-2, kim2024kdm3binhibitorsdisrupt pages 10-12)

---

## References (URLs and publication dates)
- Abbou S. et al. *Journal of Clinical Oncology* (May 2023). “Circulating Tumor DNA Is Prognostic in Intermediate-Risk Rhabdomyosarcoma: A Report From the Children’s Oncology Group.” https://doi.org/10.1200/jco.22.00409 (abbou2023circulatingtumordna pages 1-2)
- Song L. et al. *Frontiers in Cell and Developmental Biology* (Aug 2023). “Detection of various fusion genes by one-step RT-PCR…” https://doi.org/10.3389/fcell.2023.1214262 (song2023detectionofvarious pages 1-2)
- Searcy M.B. et al. *Nature Communications* (Nov 2023). “PAX3-FOXO1 dictates myogenic reprogramming…” https://doi.org/10.1038/s41467-023-43044-1 (searcy2023pax3foxo1dictatesmyogenic pages 1-2)
- Kim Y.Y. et al. *Nature Communications* (Feb 2024). “KDM3B inhibitors disrupt the oncogenic activity of PAX3-FOXO1…” https://doi.org/10.1038/s41467-024-45902-y (kim2024kdm3binhibitorsdisrupt pages 1-2)
- Danielli S.G. et al. *Nature Communications* (Jul 2024). “Single cell transcriptomic profiling identifies…” https://doi.org/10.1038/s41467-024-50527-2 (danielli2024singlecelltranscriptomic pages 1-2)
- Obeidin F. *Journal of Pathology and Translational Medicine* (May 2023). “What’s new in bone and soft tissue pathology 2023: guidelines for molecular testing.” https://doi.org/10.4132/jptm.2023.03.20 (obeidin2023what’snewin pages 1-2)
- ClinicalTrials.gov: NCT01222715 (2010 record; completed 2015). https://clinicaltrials.gov/study/NCT01222715 (NCT01222715 chunk 1)
- ClinicalTrials.gov: NCT03041701 (2017 record; terminated). https://clinicaltrials.gov/study/NCT03041701 (NCT03041701 chunk 1)
- ClinicalTrials.gov: NCT02867592 (2017 record; active-not-recruiting). https://clinicaltrials.gov/study/NCT02867592 (NCT02867592 chunk 1)
- ClinicalTrials.gov: NCT04994132 (2021 record; active-not-recruiting). https://clinicaltrials.gov/study/NCT04994132 (NCT04994132 chunk 1)


References

1. (wasti2025childhoodadolescentand pages 2-4): Ajla T. Wasti, Gianni Bisogno, Raquel Hladun, Anne-Sophie Defachelles, Michela Casanova, Willemijn B. Breunis, Susanne A. Gatz, Reineke A. Schoot, Andrea Ferrari, Meriel Jenney, Rita Alaggio, Raquel Davila Fajardo, Sheila Terwisscha van Scheltinga, Janet Shipley, Michael Torsten Meister, Rick R. van Rijn, John Anderson, Monika Sparber-Sauer, Julia C. Chisholm, and Johannes H. M. Merks. Childhood, adolescent and young adult poor-prognosis rhabdomyosarcoma. Cancers, 17:3100, Sep 2025. URL: https://doi.org/10.3390/cancers17193100, doi:10.3390/cancers17193100. This article has 1 citations.

2. (pantelakis2025recentadvanceson pages 1-2): Konstantinos Pantelakis and George I. Lambrou. Recent advances on the biology, prognosis and treatment of rhabdomyosarcoma. Journal of Research and Practice on the Musculoskeletal System, 9:46-53, Jun 2025. URL: https://doi.org/10.22540/jrpms-09-046, doi:10.22540/jrpms-09-046. This article has 0 citations.

3. (abbou2023circulatingtumordna pages 1-2): Samuel Abbou, Kelly Klega, Junko Tsuji, Mohammad Tanhaemami, David Hall, Donald A. Barkauskas, Mark D. Krailo, Carrie Cibulskis, Anwesha Nag, Aaron R. Thorner, Samuel Pollock, Alma Imamovic-Tuco, Jack F. Shern, Steven G. DuBois, Rajkumar Venkatramani, Douglas S. Hawkins, and Brian D. Crompton. Circulating tumor dna is prognostic in intermediate-risk rhabdomyosarcoma: a report from the children's oncology group. Journal of Clinical Oncology, 41:2382-2393, May 2023. URL: https://doi.org/10.1200/jco.22.00409, doi:10.1200/jco.22.00409. This article has 36 citations and is from a highest quality peer-reviewed journal.

4. (searcy2023pax3foxo1dictatesmyogenic pages 1-2): Madeline B. Searcy, Randolph K. Larsen, Bradley T. Stevens, Yang Zhang, Hongjian Jin, Catherine J. Drummond, Casey G. Langdon, Katherine E. Gadek, Kyna Vuong, Kristin B. Reed, Matthew R. Garcia, Beisi Xu, Darden W. Kimbrough, Grace E. Adkins, Nadhir Djekidel, Shaina N. Porter, Patrick A. Schreiner, Shondra M. Pruett-Miller, Brian J. Abraham, Jerold E. Rehg, and Mark E. Hatley. Pax3-foxo1 dictates myogenic reprogramming and rhabdomyosarcoma identity in endothelial progenitors. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43044-1, doi:10.1038/s41467-023-43044-1. This article has 36 citations and is from a highest quality peer-reviewed journal.

5. (searcy2023pax3foxo1dictatesmyogenic media a3da86b9): Madeline B. Searcy, Randolph K. Larsen, Bradley T. Stevens, Yang Zhang, Hongjian Jin, Catherine J. Drummond, Casey G. Langdon, Katherine E. Gadek, Kyna Vuong, Kristin B. Reed, Matthew R. Garcia, Beisi Xu, Darden W. Kimbrough, Grace E. Adkins, Nadhir Djekidel, Shaina N. Porter, Patrick A. Schreiner, Shondra M. Pruett-Miller, Brian J. Abraham, Jerold E. Rehg, and Mark E. Hatley. Pax3-foxo1 dictates myogenic reprogramming and rhabdomyosarcoma identity in endothelial progenitors. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43044-1, doi:10.1038/s41467-023-43044-1. This article has 36 citations and is from a highest quality peer-reviewed journal.

6. (danielli2024singlecelltranscriptomic pages 1-2): Sara G. Danielli, Yun Wei, Michael A. Dyer, Elizabeth Stewart, Heather Sheppard, Marco Wachtel, Beat W. Schäfer, Anand G. Patel, and David M. Langenau. Single cell transcriptomic profiling identifies tumor-acquired and therapy-resistant cell states in pediatric rhabdomyosarcoma. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50527-2, doi:10.1038/s41467-024-50527-2. This article has 39 citations and is from a highest quality peer-reviewed journal.

7. (kim2024kdm3binhibitorsdisrupt pages 1-2): Yong Yean Kim, Berkley E. Gryder, Ranuka Sinniah, Megan L. Peach, Jack F. Shern, Abdalla Abdelmaksoud, Silvia Pomella, Girma M. Woldemichael, Benjamin Z. Stanton, David Milewski, Joseph J. Barchi, John S. Schneekloth, Raj Chari, Joshua T. Kowalczyk, Shilpa R. Shenoy, Jason R. Evans, Young K. Song, Chaoyu Wang, Xinyu Wen, Hsien-Chao Chou, Vineela Gangalapudi, Dominic Esposito, Jane Jones, Lauren Procter, Maura O’Neill, Lisa M. Jenkins, Nadya I. Tarasova, Jun S. Wei, James B. McMahon, Barry R. O’Keefe, Robert G. Hawley, and Javed Khan. Kdm3b inhibitors disrupt the oncogenic activity of pax3-foxo1 in fusion-positive rhabdomyosarcoma. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45902-y, doi:10.1038/s41467-024-45902-y. This article has 22 citations and is from a highest quality peer-reviewed journal.

8. (kim2024kdm3binhibitorsdisrupt pages 10-12): Yong Yean Kim, Berkley E. Gryder, Ranuka Sinniah, Megan L. Peach, Jack F. Shern, Abdalla Abdelmaksoud, Silvia Pomella, Girma M. Woldemichael, Benjamin Z. Stanton, David Milewski, Joseph J. Barchi, John S. Schneekloth, Raj Chari, Joshua T. Kowalczyk, Shilpa R. Shenoy, Jason R. Evans, Young K. Song, Chaoyu Wang, Xinyu Wen, Hsien-Chao Chou, Vineela Gangalapudi, Dominic Esposito, Jane Jones, Lauren Procter, Maura O’Neill, Lisa M. Jenkins, Nadya I. Tarasova, Jun S. Wei, James B. McMahon, Barry R. O’Keefe, Robert G. Hawley, and Javed Khan. Kdm3b inhibitors disrupt the oncogenic activity of pax3-foxo1 in fusion-positive rhabdomyosarcoma. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45902-y, doi:10.1038/s41467-024-45902-y. This article has 22 citations and is from a highest quality peer-reviewed journal.

9. (kim2024kdm3binhibitorsdisrupt pages 2-3): Yong Yean Kim, Berkley E. Gryder, Ranuka Sinniah, Megan L. Peach, Jack F. Shern, Abdalla Abdelmaksoud, Silvia Pomella, Girma M. Woldemichael, Benjamin Z. Stanton, David Milewski, Joseph J. Barchi, John S. Schneekloth, Raj Chari, Joshua T. Kowalczyk, Shilpa R. Shenoy, Jason R. Evans, Young K. Song, Chaoyu Wang, Xinyu Wen, Hsien-Chao Chou, Vineela Gangalapudi, Dominic Esposito, Jane Jones, Lauren Procter, Maura O’Neill, Lisa M. Jenkins, Nadya I. Tarasova, Jun S. Wei, James B. McMahon, Barry R. O’Keefe, Robert G. Hawley, and Javed Khan. Kdm3b inhibitors disrupt the oncogenic activity of pax3-foxo1 in fusion-positive rhabdomyosarcoma. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45902-y, doi:10.1038/s41467-024-45902-y. This article has 22 citations and is from a highest quality peer-reviewed journal.

10. (song2023detectionofvarious pages 1-2): Lingxie Song, Ying Zhang, Yuanyuan Wang, Qingxin Xia, Dandan Guo, Jiachen Cao, Xin Xin, Haoyue Cheng, Chunxia Liu, Xingyuan Jia, and Feng Li. Detection of various fusion genes by one-step rt-pcr and the association with clinicopathological features in 242 cases of soft tissue tumor. Frontiers in Cell and Developmental Biology, Aug 2023. URL: https://doi.org/10.3389/fcell.2023.1214262, doi:10.3389/fcell.2023.1214262. This article has 6 citations.

11. (sankhe2025fusiononcogenesin pages 1-2): Chinmay S. Sankhe, Lisa Hall, and Genevieve C. Kendall. Fusion oncogenes in rhabdomyosarcoma: model systems, mechanisms of tumorigenesis, and therapeutic implications. Frontiers in Oncology, Jun 2025. URL: https://doi.org/10.3389/fonc.2025.1570070, doi:10.3389/fonc.2025.1570070. This article has 7 citations.

12. (wasti2025childhoodadolescentand pages 1-2): Ajla T. Wasti, Gianni Bisogno, Raquel Hladun, Anne-Sophie Defachelles, Michela Casanova, Willemijn B. Breunis, Susanne A. Gatz, Reineke A. Schoot, Andrea Ferrari, Meriel Jenney, Rita Alaggio, Raquel Davila Fajardo, Sheila Terwisscha van Scheltinga, Janet Shipley, Michael Torsten Meister, Rick R. van Rijn, John Anderson, Monika Sparber-Sauer, Julia C. Chisholm, and Johannes H. M. Merks. Childhood, adolescent and young adult poor-prognosis rhabdomyosarcoma. Cancers, 17:3100, Sep 2025. URL: https://doi.org/10.3390/cancers17193100, doi:10.3390/cancers17193100. This article has 1 citations.

13. (ramanathan2023outcomeandprognostic pages 11-13): Subramaniam Ramanathan, Sneha Sisodiya, Omshree Shetty, Maya Prasad, Badira C Parambil, Sneha Shah, Mukta Ramadwar, Nehal Khanna, Siddhartha Laskar, Sajid Qureshi, Tushar Vora, and Girish Chinnaswamy. Outcome and prognostic variables in childhood rhabdomyosarcoma (rms) with emphasis on impact of foxo1 fusions in non-metastatic rms: experience from a tertiary cancer centre in india. ecancermedicalscience, Apr 2023. URL: https://doi.org/10.3332/ecancer.2023.1539, doi:10.3332/ecancer.2023.1539. This article has 5 citations and is from a peer-reviewed journal.

14. (obeidin2023what’snewin pages 2-3): Farres Obeidin. What’s new in bone and soft tissue pathology 2023: guidelines for molecular testing. Journal of Pathology and Translational Medicine, 57:184-187, May 2023. URL: https://doi.org/10.4132/jptm.2023.03.20, doi:10.4132/jptm.2023.03.20. This article has 5 citations.

15. (obeidin2023what’snewin pages 1-2): Farres Obeidin. What’s new in bone and soft tissue pathology 2023: guidelines for molecular testing. Journal of Pathology and Translational Medicine, 57:184-187, May 2023. URL: https://doi.org/10.4132/jptm.2023.03.20, doi:10.4132/jptm.2023.03.20. This article has 5 citations.

16. (searcy2023pax3foxo1dictatesmyogenic media 14ad6904): Madeline B. Searcy, Randolph K. Larsen, Bradley T. Stevens, Yang Zhang, Hongjian Jin, Catherine J. Drummond, Casey G. Langdon, Katherine E. Gadek, Kyna Vuong, Kristin B. Reed, Matthew R. Garcia, Beisi Xu, Darden W. Kimbrough, Grace E. Adkins, Nadhir Djekidel, Shaina N. Porter, Patrick A. Schreiner, Shondra M. Pruett-Miller, Brian J. Abraham, Jerold E. Rehg, and Mark E. Hatley. Pax3-foxo1 dictates myogenic reprogramming and rhabdomyosarcoma identity in endothelial progenitors. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43044-1, doi:10.1038/s41467-023-43044-1. This article has 36 citations and is from a highest quality peer-reviewed journal.

17. (ramanathan2023outcomeandprognostic pages 4-7): Subramaniam Ramanathan, Sneha Sisodiya, Omshree Shetty, Maya Prasad, Badira C Parambil, Sneha Shah, Mukta Ramadwar, Nehal Khanna, Siddhartha Laskar, Sajid Qureshi, Tushar Vora, and Girish Chinnaswamy. Outcome and prognostic variables in childhood rhabdomyosarcoma (rms) with emphasis on impact of foxo1 fusions in non-metastatic rms: experience from a tertiary cancer centre in india. ecancermedicalscience, Apr 2023. URL: https://doi.org/10.3332/ecancer.2023.1539, doi:10.3332/ecancer.2023.1539. This article has 5 citations and is from a peer-reviewed journal.

18. (ramanathan2023outcomeandprognostic pages 2-4): Subramaniam Ramanathan, Sneha Sisodiya, Omshree Shetty, Maya Prasad, Badira C Parambil, Sneha Shah, Mukta Ramadwar, Nehal Khanna, Siddhartha Laskar, Sajid Qureshi, Tushar Vora, and Girish Chinnaswamy. Outcome and prognostic variables in childhood rhabdomyosarcoma (rms) with emphasis on impact of foxo1 fusions in non-metastatic rms: experience from a tertiary cancer centre in india. ecancermedicalscience, Apr 2023. URL: https://doi.org/10.3332/ecancer.2023.1539, doi:10.3332/ecancer.2023.1539. This article has 5 citations and is from a peer-reviewed journal.

19. (choi2023therecentadvances pages 1-2): Joon Hyuk Choi and Jae Y. Ro. The recent advances in molecular diagnosis of soft tissue tumors. International Journal of Molecular Sciences, 24:5934, Mar 2023. URL: https://doi.org/10.3390/ijms24065934, doi:10.3390/ijms24065934. This article has 32 citations.

20. (NCT01222715 chunk 1):  Vinorelbine Tartrate and Cyclophosphamide in Combination With Bevacizumab or Temsirolimus in Treating Patients With Recurrent or Refractory Rhabdomyosarcoma. National Cancer Institute (NCI). 2010. ClinicalTrials.gov Identifier: NCT01222715

21. (NCT03041701 chunk 1): Christine Heske, M.D.. Insulin-like Growth Factor 1 Receptor (IGF-1R) Antibody AMG479 (Ganitumab) in Combination With the Src Family Kinase (SFK) Inhibitor Dasatinib in People With Embryonal and Alveolar Rhabdomyosarcoma. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT03041701

22. (NCT02867592 chunk 1):  Cabozantinib-S-Malate in Treating Younger Patients With Recurrent, Refractory, or Newly Diagnosed Sarcomas, Wilms Tumor, or Other Rare Tumors. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT02867592

23. (NCT04994132 chunk 1):  A Study to Compare Early Use of Vinorelbine and Maintenance Therapy for Patients With High Risk Rhabdomyosarcoma. Children's Oncology Group. 2021. ClinicalTrials.gov Identifier: NCT04994132
