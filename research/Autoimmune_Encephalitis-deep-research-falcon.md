---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T07:42:07.758233'
end_time: '2026-05-08T07:56:22.157353'
duration_seconds: 854.4
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autoimmune Encephalitis
  mondo_id: ''
  category: Autoimmune
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
- **Disease Name:** Autoimmune Encephalitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Autoimmune Encephalitis** covering all of the
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
- **Disease Name:** Autoimmune Encephalitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Autoimmune Encephalitis** covering all of the
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


# Autoimmune Encephalitis (AE) — Disease Characteristics Research Report (2023–2024 prioritized)

## 1. Disease Information

### 1.1 Overview (current understanding)
Autoimmune encephalitis (AE; also written “autoimmune inflammatory encephalitis”, “autoimmune encephalopathy”, or “antibody-mediated encephalitis” depending on context) is a group of immune-mediated inflammatory brain disorders that typically present subacutely with neuropsychiatric symptoms, cognitive dysfunction, seizures, movement disorders, or altered level of consciousness, and are frequently associated with autoantibodies to neuronal cell-surface/synaptic or (in paraneoplastic neurologic syndromes) intracellular neuronal antigens. In a large real-world validation study, AE is described as being “associated with neuronal autoantibodies against extracellular antigens, which are directly pathogenic.” (steenhoven2023mimicsofautoimmune pages 1-2)

A practical case-definition used in modern guidelines is the 2016 Graus clinical criteria framework, which classifies patients as possible/probable/definite AE based on a subacute encephalopathy plus supportive MRI/CSF/EEG features, and then confirmation with syndrome-specific features and/or neural-specific antibody positivity. (orozco2023autoimmuneencephalitiscriteria pages 1-3, dutra2024brazilianconsensusrecommendations pages 4-5)

### 1.2 Key identifiers (knowledge-base fields)
Within the evidence corpus retrieved for this run, explicit mappings to **MONDO**, **Orphanet**, **MeSH**, and **ICD-10/ICD-11** identifiers for “autoimmune encephalitis” were not available; therefore these identifiers cannot be reliably populated from the cited sources here.

### 1.3 Common synonyms / alternative names (usage)
Commonly used terms in the literature captured in this run include:
- Autoimmune encephalitis (AE) / Autoimmune inflammatory encephalitis (AIE) (dutra2024brazilianconsensusrecommendations pages 1-2)
- Antibody-associated encephalitis / antibody-mediated encephalitis (steenhoven2023mimicsofautoimmune pages 1-2, kerstens2024autoimmuneencephalitisand pages 1-2)
- Autoimmune encephalopathy (often used in broader clinical coding; discussed as “related autoimmune encephalopathy” in clinical practice series) (orozco2023autoimmuneencephalitiscriteria pages 1-3)

### 1.4 Evidence sources (patient-level vs aggregated)
Evidence in this report is derived from:
- **Aggregated consensus guidelines** (Canadian 2024; Brazilian 2024) (hahn2024canadianconsensusguidelines pages 8-9, dutra2024brazilianconsensusrecommendations pages 5-7)
- **Retrospective and nationwide observational cohorts** (Mayo Clinic clinical practice study; Netherlands nationwide antibody-testing cohort) (orozco2023autoimmuneencephalitiscriteria pages 1-3, kerstens2024autoimmuneencephalitisand pages 1-2)
- **Diagnostic criteria validation and mimic studies** (national referral center cohort) (steenhoven2023mimicsofautoimmune pages 1-2)


## 2. Etiology

### 2.1 Disease causal factors (mechanistic categories)
AE is typically conceptualized as antibody-associated immune-mediated encephalitis. Antibodies may target extracellular antigens (often considered directly pathogenic) or intracellular antigens (frequently paraneoplastic syndromes). (steenhoven2023mimicsofautoimmune pages 1-2, kerstens2024autoimmuneencephalitisand pages 1-2)

### 2.2 Risk factors

#### 2.2.1 Neoplasm / paraneoplastic association
Neoplasm association varies by antibody subtype. Canadian consensus emphasizes that “all subtypes of AIE may be associated with an underlying neoplasm at varying frequencies” and recommends malignancy screening for all initial adult AE presentations. (hahn2024canadianconsensusguidelines pages 9-10)

Canadian guidance provides a malignancy-risk stratification by antibody (Table 4), e.g. high-risk antibodies (>70%) including Hu/ANNA1, Yo/PCA1, Ma2, KLHL11, etc.; intermediate risk (30–70%) including NMDAR, AMPAR, GABABR; and low risk (<30%) including LGI1, GFAP, GAD65, MOG. (hahn2024canadianconsensusguidelines pages 10-11)

#### 2.2.2 Post-infectious triggers
Post-infectious immune mechanisms are recognized clinically (e.g., secondary AE after herpes encephalitis is a known paradigm in AE practice), and both Canadian and Brazilian guidance require early infectious exclusion (notably HSV PCR in CSF) during diagnostic evaluation. (dutra2024brazilianconsensusrecommendations pages 7-8, dutra2024brazilianconsensusrecommendations pages 5-7)

#### 2.2.3 Iatrogenic triggers (immune checkpoint inhibitors)
Immune checkpoint inhibitor (ICI)-related encephalitis is recognized as an AE phenotype and is treated with immunosuppressive strategies; Canadian consensus notes ICI therapy as a risk factor and discusses AE in the differential of acute encephalopathy. (hahn2024canadianconsensusguidelines pages 2-3)

#### 2.2.4 Genetic susceptibility (HLA/KIR)
Genetic predisposition is increasingly studied; however, in this run, detailed HLA/KIR evidence was retrieved but not processed into the evidence set with citable context IDs. Therefore, genetic susceptibility is not exhaustively summarized here.

### 2.3 Protective factors
Protective genetic or environmental factors were not explicitly reported in the retrieved, citable evidence for this run.

### 2.4 Gene–environment interactions
While environmental triggers (tumor, infection, ICI exposure) are recognized, explicit gene–environment interaction analyses were not available in the citable evidence retrieved for this run.


## 3. Phenotypes

### 3.1 Core clinical phenotype spectrum (with frequencies where available)
A Chinese cohort of neuronal-surface antibody AE (n=103) reported presenting frequencies: seizures **74.8%**, psychiatric/behavior disorders **66.0%**, cognitive deficits **51.5%**, disturbances of consciousness **45.6%**, and movement disorders/involuntary movements **26.2%**. (huang2023clinicalcharacteristicsand pages 1-2)

In the Mayo Clinic real-world series of 538 adults (AE or related autoimmune encephalopathy), “possible AE” required subacute onset plus supportive features; among supportive features within possible AE (n=361), focal findings, seizures, supportive MRI, and CSF pleocytosis were common (as summarized in the paper’s abstract). (orozco2023autoimmuneencephalitiscriteria pages 1-3)

### 3.2 Suggested HPO terms (examples for knowledge base)
Based on the phenotype frequencies and guideline descriptions in the cited cohorts:
- Seizures — **HP:0001250** (huang2023clinicalcharacteristicsand pages 1-2)
- Psychiatric symptoms / psychosis — **HP:0000708** / **HP:0000738** (huang2023clinicalcharacteristicsand pages 1-2)
- Cognitive impairment — **HP:0100543** (huang2023clinicalcharacteristicsand pages 1-2)
- Altered mental status / impaired consciousness — **HP:0001252** (huang2023clinicalcharacteristicsand pages 1-2)
- Movement disorder / dyskinesia — **HP:0100022** (huang2023clinicalcharacteristicsand pages 1-2)
- CSF pleocytosis — **HP:0002181** (dutra2024brazilianconsensusrecommendations pages 4-5)

### 3.3 Quality of life impact
Guidelines emphasize persistent neuropsychiatric and cognitive sequelae and the need to evaluate cognitive/functional outcomes using tools beyond mRS (e.g., CASE, MMSE, MoCA). (dutra2024brazilianconsensusrecommendations pages 8-10, hahn2024canadianconsensusguidelines pages 10-11)


## 4. Genetic/Molecular Information

### 4.1 Primary molecular targets (autoantibodies)
Netherlands nationwide testing study lists major extracellular antigen (EA) targets including **NMDAR, LGI1, CASPR2, GABABR, GABAAR, AMPAR, DPPX, GlyR, mGluR1, IgLON5, Tr/DNER** and intracellular antigen (IA) targets including **Hu/ANNA1, Yo/PCA1, CRMP5/CV2, Ri/ANNA2, Ma1/Ma2, amphiphysin, GAD65, GFAP, KLHL11**. (kerstens2024autoimmuneencephalitisand pages 1-2)

In that nationwide cohort, the four most common AIE/PNS types were anti-NMDAR, anti-LGI1, anti-Hu, and anti-GAD65, comprising **364/578 (63.0%)** of diagnoses. (kerstens2024autoimmuneencephalitisand pages 1-2)

### 4.2 Causal genes and pathogenic variants
AE is generally not a monogenic disease; causal Mendelian genes and variant-level pathogenicity (ClinVar-style) were not provided in the citable evidence retrieved in this run.

### 4.3 Epigenetic information, chromosomal abnormalities
Not reported in the citable evidence retrieved in this run.


## 5. Environmental Information

### 5.1 Infectious agents
Workup guidelines emphasize exclusion of infectious encephalitis, specifically recommending CSF PCR testing for herpesviruses as part of AE evaluation and prior to/alongside immunotherapy. (dutra2024brazilianconsensusrecommendations pages 7-8, dutra2024brazilianconsensusrecommendations pages 5-7)

### 5.2 Neoplasm-associated immune triggers
Neoplasm association is managed as a core environmental/biologic trigger; all adult AE presentations should undergo malignancy screening at diagnosis. (hahn2024canadianconsensusguidelines pages 9-10)


## 6. Mechanism / Pathophysiology

### 6.1 Mechanistic framing (causal chain)
A practical mechanistic chain in antibody-mediated AE is:
1) Triggering exposure (e.g., tumor expression of neural antigens, infection, or immune checkpoint dysregulation) →
2) Immune activation and production of neural-specific antibodies (and/or T-cell responses, particularly in intracellular-antigen/paraneoplastic syndromes) →
3) CNS access with neuroinflammation (variable MRI/CSF abnormalities; sometimes normal early) →
4) Disruption of neuronal networks leading to neuropsychiatric symptoms, seizures, cognitive deficits, movement disorders.

This framing is consistent with the guideline and cohort emphasis that extracellular-antigen AE is directly pathogenic and that MRI/EEG/CSF may be normal despite AE. (steenhoven2023mimicsofautoimmune pages 1-2, hahn2024canadianconsensusguidelines pages 6-7)

### 6.2 Suggested GO biological process terms (examples)
- GO:0006954 inflammatory response
- GO:0006955 immune response
- GO:0042113 B cell activation
- GO:0002376 immune system process

### 6.3 Suggested CL (Cell Ontology) terms (examples)
- B cell — CL:0000236
- Plasma cell — CL:0000786
- T cell — CL:0000084
- Microglial cell — CL:0000129

### 6.4 Suggested UBERON anatomy terms (examples)
Given the encephalitic phenotype and limbic predominance in multiple AE syndromes:
- Brain — UBERON:0000955
- Hippocampus — UBERON:0001954
- Amygdala — UBERON:0001876


## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary affected system is the central nervous system (CNS), with presentations including limbic encephalitis phenotypes and diffuse encephalopathy. (orozco2023autoimmuneencephalitiscriteria pages 1-3, hahn2024canadianconsensusguidelines pages 10-11)

### 7.2 Tissue/cell level
The evidence base in this run does not provide histopathology-level cell targeting across AE subtypes; however, antibody-associated mechanisms imply neuronal synaptic/extracellular target involvement for many EA antibodies and broader neuroinflammatory involvement in some cases. (kerstens2024autoimmuneencephalitisand pages 1-2, steenhoven2023mimicsofautoimmune pages 1-2)


## 8. Temporal Development

### 8.1 Onset
Core criteria and guidelines define onset as **subacute**, typically rapid progression within **<3 months** for possible AE. (dutra2024brazilianconsensusrecommendations pages 4-5)

### 8.2 Progression/course patterns
Relapse is a recognized course feature. Canadian consensus defines relapse as objective worsening after improvement or plateau, “usually at least **2–3 months** from the original presentation” and preferably supported by MRI/CSF inflammation. (hahn2024canadianconsensusguidelines pages 12-13)


## 9. Inheritance and Population

### 9.1 Epidemiology (incidence)
A Netherlands nationwide retrospective cohort (2016–2021) estimated AE/paraneoplastic neurologic syndrome (AIE/PNS) incidence increasing from **4.70 per million person-years** (2016) to **5.76 per million person-years** (2021), with overall incidence **5.57 per million person-years** (95% CI 5.13–6.05). (kerstens2024autoimmuneencephalitisand pages 1-2)

### 9.2 Demographics
The Canadian consensus notes antibody-specific demographic patterns (e.g., NMDAR tends to affect children/young women; LGI1 often in older men) but does not provide cohort-level sex-ratio statistics in the citable excerpts for this run. (hahn2024canadianconsensusguidelines pages 2-3)


## 10. Diagnostics

### 10.1 Clinical criteria and workflow
The Graus 2016 “possible AE” criteria (adult) are a widely implemented entry step: subacute onset plus ≥1 supportive feature and exclusion of alternative causes. (orozco2023autoimmuneencephalitiscriteria pages 1-3, dutra2024brazilianconsensusrecommendations pages 4-5)

A structured diagnostic workflow is supported by both Brazilian and Canadian consensus:
- Brain MRI, EEG, CSF analysis including IgG index and oligoclonal bands (OCBs). (dutra2024brazilianconsensusrecommendations pages 5-7)
- Infectious exclusion, including CSF PCR for herpesviruses. (dutra2024brazilianconsensusrecommendations pages 7-8, dutra2024brazilianconsensusrecommendations pages 5-7)
- Neural antibody testing using paired serum+CSF (Brazil explicitly recommends TBA + CBA). (dutra2024brazilianconsensusrecommendations pages 5-7)

A concise, evidence-backed diagnostic criteria/performance and workflow summary is provided in the table artifact below.

| Topic | Key points (with numbers) | Evidence type | Source (authors/year/journal) | URL |
|---|---|---|---|---|
| Graus 2016 possible AE criteria | Adult possible AE requires all 3: (1) subacute onset, rapid progression in **<3 months**, of working memory deficits/altered mental status/psychiatric symptoms; (2) **≥1** supportive feature: new focal CNS findings, unexplained seizures, **CSF pleocytosis**, or MRI suggestive of encephalitis; (3) reasonable exclusion of alternative causes. In Mayo real-world application, **361/538 (67%)** met at least possible criteria. (orozco2023autoimmuneencephalitiscriteria pages 1-3, dutra2024brazilianconsensusrecommendations pages 4-5) | Human clinical cohort + consensus criteria | Orozco et al. 2023, *Neurology Clinical Practice*; Dutra et al. 2024, *Arquivos de Neuro-Psiquiatria* | https://doi.org/10.1212/cpj.0000000000200151 ; https://doi.org/10.1055/s-0044-1788586 |
| Pediatric possible AE criteria | Pediatric possible AE: onset of neurologic/psychiatric symptoms over **<3 months** in a previously healthy child plus **2** of the following: altered mental status/EEG slowing or epileptiform activity, focal deficits, cognitive difficulties, acute developmental regression, movement disorder, psychiatric symptoms, or unexplained seizures; and exclusion of alternatives. (dutra2024brazilianconsensusrecommendations pages 4-5) | Consensus criteria | Dutra et al. 2024, *Arquivos de Neuro-Psiquiatria* | https://doi.org/10.1055/s-0044-1788586 |
| Criteria performance and specificity | In a national referral cohort (**n=239**), criteria performance was: possible AE **sensitivity 83%**, **specificity 27%**; definite autoimmune limbic encephalitis **sensitivity 10%**, **specificity 98%**; probable anti-NMDAR **sensitivity 50%**, **specificity 96%**; probable seronegative AE **specificity 99%**; proposed probable anti-LGI1 **sensitivity 66%**, **specificity 96%**. Authors note probable/definite categories are useful for early immunotherapy decisions because specificity is high. (steenhoven2023mimicsofautoimmune pages 1-2) | Human clinical validation cohort | van Steenhoven et al. 2023, *Neurology Neuroimmunology & Neuroinflammation* | https://doi.org/10.1212/nxi.0000000000200148 |
| Definite AE / antibody-defined cases in practice | In Mayo review (**n=538**), definite AE cases included limbic encephalitis **127/221 (57%)**, anti-NMDAR **32/221 (15%)**, ADEM **8/221 (4%)**, and other AE-specific IgG defined syndromes **54/221 (24%)**. Most common definite AE-IgGs: **LGI1 76 (34%)**, **NMDA-R 32 (16%)**, **high-titer GAD65 23 (12%)**. Criteria were judged highly specific but may miss AE-IgG positive isolated seizures/brainstem disease. (orozco2023autoimmuneencephalitiscriteria pages 1-3) | Human clinical cohort | Orozco et al. 2023, *Neurology Clinical Practice* | https://doi.org/10.1212/cpj.0000000000200151 |
| Common mimics and diagnostic pitfalls | Among **239** suspected cases, AE was **104/239 (44%)** and mimics **109/239 (46%)**. Common mimics: neuroinflammatory CNS disorders **26%**, psychiatric disorders **19%**, noninflammatory epilepsy **13%**, CNS infections **7%**, neurodegenerative diseases **7%**, CNS neoplasms **6%**. Confounders included mesiotemporal MRI lesions **17%** and **false-positive serum antibodies 12%**; atypical mesiotemporal features were more frequent in mimics (**61% vs 24%**). (steenhoven2023mimicsofautoimmune pages 1-2) | Human clinical cohort | van Steenhoven et al. 2023, *Neurology Neuroimmunology & Neuroinflammation* | https://doi.org/10.1212/nxi.0000000000200148 |
| Antibody assay PPV limitations | Nationwide Netherlands testing (**30,246** samples) found **2,877 (9.5%)** positive samples from **1,228** patients; clinical data on **940** patients yielded **578** AIE/PNS diagnoses. Sensitivity and specificity were generally **>95% to >99%**, but PPV was only moderate-to-poor in mass testing; for **serum intracellular-antigen antibodies PPV ranged 25%–80%**. This supports cautious interpretation of positive serum results in low-pretest-probability settings. (kerstens2024autoimmuneencephalitisand pages 1-2) | Nationwide retrospective laboratory-clinical cohort | Kerstens et al. 2024, *Neurology Neuroimmunology & Neuroinflammation* | https://doi.org/10.1212/nxi.0000000000200318 |
| Core diagnostic workflow tests | Brazilian consensus recommends that adults meeting Graus possible AE or children meeting Cellucci criteria should undergo **brain MRI, EEG, and CSF analysis**, including **IgG index** and **oligoclonal bands (OCBs)**. These are baseline tests before/alongside antibody evaluation. (dutra2024brazilianconsensusrecommendations pages 5-7, dutra2024brazilianconsensusrecommendations pages 4-5) | Consensus guideline | Dutra et al. 2024, *Arquivos de Neuro-Psiquiatria* | https://doi.org/10.1055/s-0044-1788586 |
| CSF infectious exclusion and paired antibody testing | Consensus recommends paired **serum + CSF** antineuronal antibody testing using **TBA and CBA**; anti-MOG should be added in all pediatric possible AE. CSF workup should include **PCR for herpesvirus**; sample collection should preferably occur before immunotherapy, but treatment should not be delayed while awaiting results. (dutra2024brazilianconsensusrecommendations pages 5-7) | Consensus guideline | Dutra et al. 2024, *Arquivos de Neuro-Psiquiatria* | https://doi.org/10.1055/s-0044-1788586 |
| Imaging caveats and antibody confirmation | Canadian guidance emphasizes MRI/EEG may be normal and unexpected antibody results should prompt confirmatory testing (e.g., tissue indirect immunofluorescence/immunohistochemistry). Initial screening should not wait for antibody results. (hahn2024canadianconsensusguidelines pages 9-10, hahn2024canadianconsensusguidelines pages 10-11) | Consensus guideline | Hahn et al. 2024, *Canadian Journal of Neurological Sciences* | https://doi.org/10.1017/cjn.2024.16 |
| Neoplasm screening: who to screen | All adult patients with AIE should undergo malignancy screening at diagnosis; screening should not be delayed while awaiting neural antibody results. Screening should also be considered at relapse. (hahn2024canadianconsensusguidelines pages 9-10, hahn2024canadianconsensusguidelines pages 10-11) | Consensus guideline | Hahn et al. 2024, *Canadian Journal of Neurological Sciences* | https://doi.org/10.1017/cjn.2024.16 |
| Neoplasm screening: three-step approach | Canadian consensus describes a **3-step** imaging strategy: **(1)** conventional **CT body**, **(2)** focused **sex-specific imaging**, and **(3)** **whole-body PET** if needed; terminate early if a neoplasm is found. First-line PET can be considered when there is a strong antibody-neoplasm association. Pelvic US or MRI is preferred over PET for ovarian teratoma. (hahn2024canadianconsensusguidelines pages 9-10, hahn2024canadianconsensusguidelines pages 10-11) | Consensus guideline | Hahn et al. 2024, *Canadian Journal of Neurological Sciences* | https://doi.org/10.1017/cjn.2024.16 |
| Sex-specific / directed tumor studies | Examples of directed testing include immediate **ovarian ultrasound** for young women with NMDAR encephalitis and **testicular ultrasound** for men with KLHL11 antibody encephalitis. Brazilian consensus similarly recommends CT chest/abdomen/pelvis plus sex-specific studies such as transvaginal US/mammography for women and scrotal US for men. (hahn2024canadianconsensusguidelines pages 10-11, dutra2024brazilianconsensusrecommendations pages 5-7) | Consensus guideline | Hahn et al. 2024, *Canadian Journal of Neurological Sciences*; Dutra et al. 2024, *Arquivos de Neuro-Psiquiatria* | https://doi.org/10.1017/cjn.2024.16 ; https://doi.org/10.1055/s-0044-1788586 |
| Follow-up tumor surveillance | If initial screening is negative, Canadian guidance recommends follow-up screening in patients with **intermediate- or high-risk antibodies**; for such antibodies, repeat screening every **3–6 months for at least 2 years** is recommended. Antibody-negative patients with high-risk phenotypes (e.g., limbic encephalitis, refractory/relapsing disease, malignancy risk factors) may also merit repeat screening. (hahn2024canadianconsensusguidelines pages 9-10, hahn2024canadianconsensusguidelines pages 10-11) | Consensus guideline | Hahn et al. 2024, *Canadian Journal of Neurological Sciences* | https://doi.org/10.1017/cjn.2024.16 |
| Malignancy-risk antibody categories | Canadian Table 4 classifies tumor risk: **high-risk >70%** (e.g., Hu/ANNA-1, CV2/CRMP5, Ma2/Ma, KLHL11, Yo/PCA-1), **intermediate 30–70%** (e.g., AMPAR, GABABR, mGluR5, NMDAR, CASPR2 in Morvan syndrome, GABAAR), and **low-risk <30%** (e.g., GFAP, GAD65, LGI1, DPPX, GlyR, MOG, AQP4, mGluR1). (hahn2024canadianconsensusguidelines pages 10-11) | Consensus guideline | Hahn et al. 2024, *Canadian Journal of Neurological Sciences* | https://doi.org/10.1017/cjn.2024.16 |


*Table: This table summarizes evidence-based autoimmune encephalitis diagnostic criteria, common pitfalls, core testing workflow, and neoplasm screening recommendations from recent validation studies and 2024 consensus guidelines. It is useful as a compact reference for applying Graus/Cellucci criteria, interpreting antibody results cautiously, and structuring tumor search in suspected AE.*

### 10.2 Diagnostic criteria performance and misdiagnosis pitfalls
In a real-world validation/mimic cohort (n=239), “possible AE” criteria had **sensitivity 83%** and **specificity 27%**, reflecting usefulness as an entry criterion but a high false-positive burden; “definite autoimmune limbic encephalitis” had **specificity 98%**, and “probable anti-NMDAR” had **specificity 96%**. (steenhoven2023mimicsofautoimmune pages 1-2)

Key pitfalls include:
- **False-positive serum antibodies** (reported in **12%** of the mimic/AE referral cohort). (steenhoven2023mimicsofautoimmune pages 1-2)
- In mass-testing settings, PPV can be only modest: in the Netherlands nationwide antibody-testing cohort, serum intracellular-antigen antibody PPVs ranged **25%–80%**, despite high sensitivity/specificity for most assays. (kerstens2024autoimmuneencephalitisand pages 1-2)

### 10.3 Imaging and electrophysiology (recent data)
Canadian consensus states FDG-PET can be more sensitive than MRI in AE (reported **87% vs 25–50%** sensitivity) but warns that PET findings can be nonspecific and should not be used alone. (hahn2024canadianconsensusguidelines pages 6-7, hahn2024canadianconsensusguidelines pages 12-13)

### 10.4 Neoplasm screening (real-world implementation)
Canadian consensus recommends malignancy screening for all adult AE at diagnosis and describes a 3-step imaging strategy (CT body → sex-specific imaging → whole-body PET if needed), with follow-up screening focused on intermediate/high-risk antibodies. (hahn2024canadianconsensusguidelines pages 9-10, hahn2024canadianconsensusguidelines pages 10-11)

The neoplasm screening protocol figure from the Canadian guideline is shown here. (hahn2024canadianconsensusguidelines media d7e73b99)


## 11. Outcome / Prognosis

### 11.1 Functional outcomes
In the Chinese cohort (n=103), most patients achieved favorable function at last follow-up: **78** had good prognosis (mRS 0–2) vs **21** with poor prognosis (mRS 3–6); anti-GABABR encephalitis had worse outcomes than other AE subtypes. (huang2023clinicalcharacteristicsand pages 1-2)

### 11.2 Prognostic factors and biomarkers
In the same cohort, elevated neutrophil-to-lymphocyte ratio (NLR) and tumor presence were independent predictors of poor prognosis; a model combining these achieved **AUC 0.847** (95% CI 0.733–0.961). (huang2023clinicalcharacteristicsand pages 1-2)

### 11.3 Relapse
Canadian consensus summarizes retrospective relapse rates in NMDAR/LGI1/CASPR2 encephalitis as **10–41%** and notes relapses may be similar, milder, or with a different core syndrome. (hahn2024canadianconsensusguidelines pages 12-13)


## 12. Treatment

### 12.1 Acute immunotherapy tiers (consensus practice)

#### 12.1.1 Timing
Brazilian consensus explicitly states: “**Treatment should be started within the first 4 weeks of symptoms**,” and that initiation “**should not be delayed while waiting for**” antibody results. (dutra2024brazilianconsensusrecommendations pages 1-2, dutra2024brazilianconsensusrecommendations pages 5-7)

#### 12.1.2 First-line therapy
Brazilian consensus: first-line is **methylprednisolone + IVIG** or **methylprednisolone + plasmapheresis**, with typical IVIG and steroid dosing specified (e.g., IVIG 2 g/kg over 2–5 days; IV methylprednisolone 1,000 mg daily for 3–5 days in adults). (dutra2024brazilianconsensusrecommendations pages 8-10, dutra2024brazilianconsensusrecommendations pages 5-7)

Canadian consensus: severe AE should receive high-dose corticosteroids with IVIG or plasma exchange as initial therapy; mild/moderate cases may consider steroid monotherapy with specialist input. (hahn2024canadianconsensusguidelines pages 9-10)

The Canadian guideline treatment algorithm figure is shown here. (hahn2024canadianconsensusguidelines media aed80ffe)

#### 12.1.3 Second-line therapy and escalation timing
Brazilian consensus defines “satisfactory clinical response” as improvement within **10–14 days**; lack of partial improvement within 14 days should prompt second-line therapy. (dutra2024brazilianconsensusrecommendations pages 5-7)

Canadian consensus defines first-line failure as no improvement/worsening at **5–10 days** in severe AE and **2–4 weeks** in mild/moderate AE. (hahn2024canadianconsensusguidelines pages 8-9)

Second-line choices are antibody-contextual:
- Cell-surface antibody AE or antibody-negative AE: **rituximab** favored for efficacy/safety. (hahn2024canadianconsensusguidelines pages 8-9)
- High-risk paraneoplastic/intracellular antibodies: **cyclophosphamide** preferentially used. (hahn2024canadianconsensusguidelines pages 8-9)

#### 12.1.4 Third-line / refractory options
Canadian and Brazilian guidance list **tocilizumab** and **bortezomib** as third-line/experimental options for cases refractory to second-line therapy, with specialist involvement recommended. (hahn2024canadianconsensusguidelines pages 9-10, dutra2024brazilianconsensusrecommendations pages 5-7)

### 12.2 Symptomatic treatments
Seizures in AE are commonly acute symptomatic; Brazilian consensus notes antiseizure medications may be weaned after the acute stage when stable. (dutra2024brazilianconsensusrecommendations pages 1-2)

### 12.3 MAXO term suggestions (examples)
- High-dose corticosteroid therapy — MAXO:0000601 (suggested)
- Intravenous immunoglobulin therapy — MAXO:0000747 (suggested)
- Therapeutic plasma exchange — MAXO:0000474 (suggested)
- Anti-CD20 monoclonal antibody therapy (rituximab) — MAXO:0000792 (suggested)


## 13. Prevention
Primary prevention is not established for most AE syndromes given heterogeneous triggers. Secondary/tertiary prevention is emphasized via:
- Early diagnosis and early immunotherapy to reduce morbidity and long-term deficits. (dutra2024brazilianconsensusrecommendations pages 5-7, hahn2024canadianconsensusguidelines pages 9-10)
- Tumor screening and treatment/removal when present (paraneoplastic prevention of ongoing antigenic drive). (hahn2024canadianconsensusguidelines pages 9-10)


## 14. Other Species / Natural Disease
Naturally occurring AE-like antibody-mediated encephalitis in non-human species was not addressed in the citable evidence retrieved in this run.


## 15. Model Organisms
Animal/model system evidence was not present in the citable evidence retrieved in this run.


# Expert opinion & analysis (from authoritative sources)
- **Diagnostic criteria are useful but require caution**: real-world studies highlight that entry criteria (“possible AE”) are sensitive but not specific and are prone to mimics and misdiagnosis; high-specificity categories (probable/definite) support early immunotherapy decisions while awaiting antibody confirmation. (steenhoven2023mimicsofautoimmune pages 1-2)
- **Testing pitfalls are central in modern practice**: even when assays show high analytical specificity/sensitivity, PPV can be limited in rare diseases under broad testing, especially for serum intracellular antibodies, reinforcing the need for clinical correlation and confirmatory strategies. (kerstens2024autoimmuneencephalitisand pages 1-2, steenhoven2023mimicsofautoimmune pages 1-2)
- **Treatment is time-sensitive and tiered**: 2024 consensus statements converge on early immunotherapy (often combination first-line in severe disease) and time-bound escalation to second-line agents if not improving. (hahn2024canadianconsensusguidelines pages 8-9, dutra2024brazilianconsensusrecommendations pages 5-7)


# Key images (evidence)
- Canadian guideline treatment algorithm: (hahn2024canadianconsensusguidelines media aed80ffe)
- Canadian guideline neoplasm screening protocol: (hahn2024canadianconsensusguidelines media d7e73b99)


# Notes on evidence gaps in this run
- Standard ontology identifiers (MONDO/Orphanet/MeSH/ICD) were not retrievable from the cited evidence corpus.
- Protective factors, epigenetic mechanisms, and non-human models were not available in the retrieved citable sources.



References

1. (steenhoven2023mimicsofautoimmune pages 1-2): Robin W. Van Steenhoven, Juna M. de Vries, Arlette L. Bruijstens, Manuela Paunovic, Mariska M. Nagtzaam, Suzanne C. Franken, Anna E. Bastiaansen, Marienke A. De Bruijn, Agnes Van Sonderen, Marco W.J. Schreurs, Mayke Gardeniers, Robert M. Verdijk, Rutger K. Balvers, Peter A. Sillevis Smitt, Rinze F. Neuteboom, and Maarten J. Titulaer. Mimics of autoimmune encephalitis. Neurology Neuroimmunology &amp; Neuroinflammation, Nov 2023. URL: https://doi.org/10.1212/nxi.0000000000200148, doi:10.1212/nxi.0000000000200148. This article has 72 citations.

2. (orozco2023autoimmuneencephalitiscriteria pages 1-3): Emma Orozco, Cristina Valencia-Sanchez, Jeffrey Britton, Divyanshu Dubey, Eoin P. Flanagan, A. Sebastian Lopez-Chiriboga, Nicholas Zalewski, Anastasia Zekeridou, Sean J. Pittock, and Andrew McKeon. Autoimmune encephalitis criteria in clinical practice. Neurology Clinical Practice, Jun 2023. URL: https://doi.org/10.1212/cpj.0000000000200151, doi:10.1212/cpj.0000000000200151. This article has 65 citations.

3. (dutra2024brazilianconsensusrecommendations pages 4-5): Lívia Almeida Dutra, Pedro Victor de Castro Silva, João Henrique Fregadolli Ferreira, Alexandre Coelho Marques, Fabio Fieni Toso, Claudia Cristina Ferreira Vasconcelos, Doralina Guimarães Brum, Samira Luisa dos Apóstolos Pereira, Tarso Adoni, Leticia Januzi de Almeida Rocha, Leticia Pereira de Brito Sampaio, Nise Alessandra de Carvalho Sousa, Renata Barbosa Paolilo, Angélica Dal Pizzol, Bruna Klein da Costa, Caio César Diniz Disserol, Camila Pupe, Daniel Almeida do Valle, Denise Sisterolli Diniz, Fabiano Ferreira de Abrantes, Felipe da Rocha Schmidt, Fernando Cendes, Francisco Tomaz Meneses de Oliveira, Gabriela Joca Martins, Guilherme Diogo Silva, Katia Lin, Lécio Figueira Pinto, Mara Lúcia Schimtz Ferreira Santos, Marcus Vinícius Magno Gonçalves, Mariana Braatz Krueger, Michel Elyas Jung Haziot, Orlando Graziani Povoas Barsottini, Osvaldo José Moreira do Nascimento, Paulo Ribeiro Nóbrega, Priscilla Mara Proveti, Raphael Machado do Castilhos, Vanessa Daccach, and Felipe von Glehn. Brazilian consensus recommendations on the diagnosis and treatment of autoimmune encephalitis in the adult and pediatric populations. Arquivos de Neuro-Psiquiatria, 82:001-015, Jul 2024. URL: https://doi.org/10.1055/s-0044-1788586, doi:10.1055/s-0044-1788586. This article has 10 citations and is from a peer-reviewed journal.

4. (dutra2024brazilianconsensusrecommendations pages 1-2): Lívia Almeida Dutra, Pedro Victor de Castro Silva, João Henrique Fregadolli Ferreira, Alexandre Coelho Marques, Fabio Fieni Toso, Claudia Cristina Ferreira Vasconcelos, Doralina Guimarães Brum, Samira Luisa dos Apóstolos Pereira, Tarso Adoni, Leticia Januzi de Almeida Rocha, Leticia Pereira de Brito Sampaio, Nise Alessandra de Carvalho Sousa, Renata Barbosa Paolilo, Angélica Dal Pizzol, Bruna Klein da Costa, Caio César Diniz Disserol, Camila Pupe, Daniel Almeida do Valle, Denise Sisterolli Diniz, Fabiano Ferreira de Abrantes, Felipe da Rocha Schmidt, Fernando Cendes, Francisco Tomaz Meneses de Oliveira, Gabriela Joca Martins, Guilherme Diogo Silva, Katia Lin, Lécio Figueira Pinto, Mara Lúcia Schimtz Ferreira Santos, Marcus Vinícius Magno Gonçalves, Mariana Braatz Krueger, Michel Elyas Jung Haziot, Orlando Graziani Povoas Barsottini, Osvaldo José Moreira do Nascimento, Paulo Ribeiro Nóbrega, Priscilla Mara Proveti, Raphael Machado do Castilhos, Vanessa Daccach, and Felipe von Glehn. Brazilian consensus recommendations on the diagnosis and treatment of autoimmune encephalitis in the adult and pediatric populations. Arquivos de Neuro-Psiquiatria, 82:001-015, Jul 2024. URL: https://doi.org/10.1055/s-0044-1788586, doi:10.1055/s-0044-1788586. This article has 10 citations and is from a peer-reviewed journal.

5. (kerstens2024autoimmuneencephalitisand pages 1-2): Jeroen Kerstens, Marco W.J. Schreurs, Juna M. de Vries, Rinze F. Neuteboom, Juliette Brenner, Yvette S. Crijnen, Robin W. van Steenhoven, Marienke A.A.M. de Bruijn, Agnes van Sonderen, Marleen H. van Coevorden-Hameete, Anna E.M. Bastiaansen, Marie R. Vermeiren, Jan G.M.C. Damoiseaux, Henny G. Otten, Catharina J.M. Frijns, Bob Meek, Anouk C.M. Platteel, Alina van de Mortel, Cathérine C.S. Delnooz, Maarten A.C. Broeren, Marcel M. Verbeek, Erik I. Hoff, Sanae Boukhrissi, Suzanne C. Franken, Mariska M.P. Nagtzaam, Manuela Paunovic, Sharon Veenbergen, Peter A.E. Sillevis Smitt, and Maarten J. Titulaer. Autoimmune encephalitis and paraneoplastic neurologic syndromes. Neurology Neuroimmunology &amp; Neuroinflammation, Nov 2024. URL: https://doi.org/10.1212/nxi.0000000000200318, doi:10.1212/nxi.0000000000200318. This article has 29 citations.

6. (hahn2024canadianconsensusguidelines pages 8-9): Christopher Hahn, Adrian Budhram, Katayoun Alikhani, Nasser AlOhaly, Grayson Beecher, Gregg Blevins, John Brooks, Robert Carruthers, Jacynthe Comtois, Juthaporn Cowan, Paula de Robles, Julien Hébert, Ronak K. Kapadia, Sarah Lapointe, Aaron Mackie, Warren Mason, Brienne McLane, Alexandra Muccilli, Ilia Poliakov, Penelope Smyth, Kimberly G. Williams, Christopher Uy, and Jennifer A. McCombe. Canadian consensus guidelines for the diagnosis and treatment of autoimmune encephalitis in adults. Canadian Journal of Neurological Sciences / Journal Canadien des Sciences Neurologiques, 51:734-754, Feb 2024. URL: https://doi.org/10.1017/cjn.2024.16, doi:10.1017/cjn.2024.16. This article has 33 citations.

7. (dutra2024brazilianconsensusrecommendations pages 5-7): Lívia Almeida Dutra, Pedro Victor de Castro Silva, João Henrique Fregadolli Ferreira, Alexandre Coelho Marques, Fabio Fieni Toso, Claudia Cristina Ferreira Vasconcelos, Doralina Guimarães Brum, Samira Luisa dos Apóstolos Pereira, Tarso Adoni, Leticia Januzi de Almeida Rocha, Leticia Pereira de Brito Sampaio, Nise Alessandra de Carvalho Sousa, Renata Barbosa Paolilo, Angélica Dal Pizzol, Bruna Klein da Costa, Caio César Diniz Disserol, Camila Pupe, Daniel Almeida do Valle, Denise Sisterolli Diniz, Fabiano Ferreira de Abrantes, Felipe da Rocha Schmidt, Fernando Cendes, Francisco Tomaz Meneses de Oliveira, Gabriela Joca Martins, Guilherme Diogo Silva, Katia Lin, Lécio Figueira Pinto, Mara Lúcia Schimtz Ferreira Santos, Marcus Vinícius Magno Gonçalves, Mariana Braatz Krueger, Michel Elyas Jung Haziot, Orlando Graziani Povoas Barsottini, Osvaldo José Moreira do Nascimento, Paulo Ribeiro Nóbrega, Priscilla Mara Proveti, Raphael Machado do Castilhos, Vanessa Daccach, and Felipe von Glehn. Brazilian consensus recommendations on the diagnosis and treatment of autoimmune encephalitis in the adult and pediatric populations. Arquivos de Neuro-Psiquiatria, 82:001-015, Jul 2024. URL: https://doi.org/10.1055/s-0044-1788586, doi:10.1055/s-0044-1788586. This article has 10 citations and is from a peer-reviewed journal.

8. (hahn2024canadianconsensusguidelines pages 9-10): Christopher Hahn, Adrian Budhram, Katayoun Alikhani, Nasser AlOhaly, Grayson Beecher, Gregg Blevins, John Brooks, Robert Carruthers, Jacynthe Comtois, Juthaporn Cowan, Paula de Robles, Julien Hébert, Ronak K. Kapadia, Sarah Lapointe, Aaron Mackie, Warren Mason, Brienne McLane, Alexandra Muccilli, Ilia Poliakov, Penelope Smyth, Kimberly G. Williams, Christopher Uy, and Jennifer A. McCombe. Canadian consensus guidelines for the diagnosis and treatment of autoimmune encephalitis in adults. Canadian Journal of Neurological Sciences / Journal Canadien des Sciences Neurologiques, 51:734-754, Feb 2024. URL: https://doi.org/10.1017/cjn.2024.16, doi:10.1017/cjn.2024.16. This article has 33 citations.

9. (hahn2024canadianconsensusguidelines pages 10-11): Christopher Hahn, Adrian Budhram, Katayoun Alikhani, Nasser AlOhaly, Grayson Beecher, Gregg Blevins, John Brooks, Robert Carruthers, Jacynthe Comtois, Juthaporn Cowan, Paula de Robles, Julien Hébert, Ronak K. Kapadia, Sarah Lapointe, Aaron Mackie, Warren Mason, Brienne McLane, Alexandra Muccilli, Ilia Poliakov, Penelope Smyth, Kimberly G. Williams, Christopher Uy, and Jennifer A. McCombe. Canadian consensus guidelines for the diagnosis and treatment of autoimmune encephalitis in adults. Canadian Journal of Neurological Sciences / Journal Canadien des Sciences Neurologiques, 51:734-754, Feb 2024. URL: https://doi.org/10.1017/cjn.2024.16, doi:10.1017/cjn.2024.16. This article has 33 citations.

10. (dutra2024brazilianconsensusrecommendations pages 7-8): Lívia Almeida Dutra, Pedro Victor de Castro Silva, João Henrique Fregadolli Ferreira, Alexandre Coelho Marques, Fabio Fieni Toso, Claudia Cristina Ferreira Vasconcelos, Doralina Guimarães Brum, Samira Luisa dos Apóstolos Pereira, Tarso Adoni, Leticia Januzi de Almeida Rocha, Leticia Pereira de Brito Sampaio, Nise Alessandra de Carvalho Sousa, Renata Barbosa Paolilo, Angélica Dal Pizzol, Bruna Klein da Costa, Caio César Diniz Disserol, Camila Pupe, Daniel Almeida do Valle, Denise Sisterolli Diniz, Fabiano Ferreira de Abrantes, Felipe da Rocha Schmidt, Fernando Cendes, Francisco Tomaz Meneses de Oliveira, Gabriela Joca Martins, Guilherme Diogo Silva, Katia Lin, Lécio Figueira Pinto, Mara Lúcia Schimtz Ferreira Santos, Marcus Vinícius Magno Gonçalves, Mariana Braatz Krueger, Michel Elyas Jung Haziot, Orlando Graziani Povoas Barsottini, Osvaldo José Moreira do Nascimento, Paulo Ribeiro Nóbrega, Priscilla Mara Proveti, Raphael Machado do Castilhos, Vanessa Daccach, and Felipe von Glehn. Brazilian consensus recommendations on the diagnosis and treatment of autoimmune encephalitis in the adult and pediatric populations. Arquivos de Neuro-Psiquiatria, 82:001-015, Jul 2024. URL: https://doi.org/10.1055/s-0044-1788586, doi:10.1055/s-0044-1788586. This article has 10 citations and is from a peer-reviewed journal.

11. (hahn2024canadianconsensusguidelines pages 2-3): Christopher Hahn, Adrian Budhram, Katayoun Alikhani, Nasser AlOhaly, Grayson Beecher, Gregg Blevins, John Brooks, Robert Carruthers, Jacynthe Comtois, Juthaporn Cowan, Paula de Robles, Julien Hébert, Ronak K. Kapadia, Sarah Lapointe, Aaron Mackie, Warren Mason, Brienne McLane, Alexandra Muccilli, Ilia Poliakov, Penelope Smyth, Kimberly G. Williams, Christopher Uy, and Jennifer A. McCombe. Canadian consensus guidelines for the diagnosis and treatment of autoimmune encephalitis in adults. Canadian Journal of Neurological Sciences / Journal Canadien des Sciences Neurologiques, 51:734-754, Feb 2024. URL: https://doi.org/10.1017/cjn.2024.16, doi:10.1017/cjn.2024.16. This article has 33 citations.

12. (huang2023clinicalcharacteristicsand pages 1-2): Teng Huang, Fei Liu, Baojie Wang, Chunjuan Wang, Maolin Hao, and Shougang Guo. Clinical characteristics and prognosis in patients with neuronal surface antibody-mediated autoimmune encephalitis: a single-center cohort study in china. Frontiers in Immunology, Dec 2023. URL: https://doi.org/10.3389/fimmu.2023.1213532, doi:10.3389/fimmu.2023.1213532. This article has 17 citations and is from a peer-reviewed journal.

13. (dutra2024brazilianconsensusrecommendations pages 8-10): Lívia Almeida Dutra, Pedro Victor de Castro Silva, João Henrique Fregadolli Ferreira, Alexandre Coelho Marques, Fabio Fieni Toso, Claudia Cristina Ferreira Vasconcelos, Doralina Guimarães Brum, Samira Luisa dos Apóstolos Pereira, Tarso Adoni, Leticia Januzi de Almeida Rocha, Leticia Pereira de Brito Sampaio, Nise Alessandra de Carvalho Sousa, Renata Barbosa Paolilo, Angélica Dal Pizzol, Bruna Klein da Costa, Caio César Diniz Disserol, Camila Pupe, Daniel Almeida do Valle, Denise Sisterolli Diniz, Fabiano Ferreira de Abrantes, Felipe da Rocha Schmidt, Fernando Cendes, Francisco Tomaz Meneses de Oliveira, Gabriela Joca Martins, Guilherme Diogo Silva, Katia Lin, Lécio Figueira Pinto, Mara Lúcia Schimtz Ferreira Santos, Marcus Vinícius Magno Gonçalves, Mariana Braatz Krueger, Michel Elyas Jung Haziot, Orlando Graziani Povoas Barsottini, Osvaldo José Moreira do Nascimento, Paulo Ribeiro Nóbrega, Priscilla Mara Proveti, Raphael Machado do Castilhos, Vanessa Daccach, and Felipe von Glehn. Brazilian consensus recommendations on the diagnosis and treatment of autoimmune encephalitis in the adult and pediatric populations. Arquivos de Neuro-Psiquiatria, 82:001-015, Jul 2024. URL: https://doi.org/10.1055/s-0044-1788586, doi:10.1055/s-0044-1788586. This article has 10 citations and is from a peer-reviewed journal.

14. (hahn2024canadianconsensusguidelines pages 6-7): Christopher Hahn, Adrian Budhram, Katayoun Alikhani, Nasser AlOhaly, Grayson Beecher, Gregg Blevins, John Brooks, Robert Carruthers, Jacynthe Comtois, Juthaporn Cowan, Paula de Robles, Julien Hébert, Ronak K. Kapadia, Sarah Lapointe, Aaron Mackie, Warren Mason, Brienne McLane, Alexandra Muccilli, Ilia Poliakov, Penelope Smyth, Kimberly G. Williams, Christopher Uy, and Jennifer A. McCombe. Canadian consensus guidelines for the diagnosis and treatment of autoimmune encephalitis in adults. Canadian Journal of Neurological Sciences / Journal Canadien des Sciences Neurologiques, 51:734-754, Feb 2024. URL: https://doi.org/10.1017/cjn.2024.16, doi:10.1017/cjn.2024.16. This article has 33 citations.

15. (hahn2024canadianconsensusguidelines pages 12-13): Christopher Hahn, Adrian Budhram, Katayoun Alikhani, Nasser AlOhaly, Grayson Beecher, Gregg Blevins, John Brooks, Robert Carruthers, Jacynthe Comtois, Juthaporn Cowan, Paula de Robles, Julien Hébert, Ronak K. Kapadia, Sarah Lapointe, Aaron Mackie, Warren Mason, Brienne McLane, Alexandra Muccilli, Ilia Poliakov, Penelope Smyth, Kimberly G. Williams, Christopher Uy, and Jennifer A. McCombe. Canadian consensus guidelines for the diagnosis and treatment of autoimmune encephalitis in adults. Canadian Journal of Neurological Sciences / Journal Canadien des Sciences Neurologiques, 51:734-754, Feb 2024. URL: https://doi.org/10.1017/cjn.2024.16, doi:10.1017/cjn.2024.16. This article has 33 citations.

16. (hahn2024canadianconsensusguidelines media d7e73b99): Christopher Hahn, Adrian Budhram, Katayoun Alikhani, Nasser AlOhaly, Grayson Beecher, Gregg Blevins, John Brooks, Robert Carruthers, Jacynthe Comtois, Juthaporn Cowan, Paula de Robles, Julien Hébert, Ronak K. Kapadia, Sarah Lapointe, Aaron Mackie, Warren Mason, Brienne McLane, Alexandra Muccilli, Ilia Poliakov, Penelope Smyth, Kimberly G. Williams, Christopher Uy, and Jennifer A. McCombe. Canadian consensus guidelines for the diagnosis and treatment of autoimmune encephalitis in adults. Canadian Journal of Neurological Sciences / Journal Canadien des Sciences Neurologiques, 51:734-754, Feb 2024. URL: https://doi.org/10.1017/cjn.2024.16, doi:10.1017/cjn.2024.16. This article has 33 citations.

17. (hahn2024canadianconsensusguidelines media aed80ffe): Christopher Hahn, Adrian Budhram, Katayoun Alikhani, Nasser AlOhaly, Grayson Beecher, Gregg Blevins, John Brooks, Robert Carruthers, Jacynthe Comtois, Juthaporn Cowan, Paula de Robles, Julien Hébert, Ronak K. Kapadia, Sarah Lapointe, Aaron Mackie, Warren Mason, Brienne McLane, Alexandra Muccilli, Ilia Poliakov, Penelope Smyth, Kimberly G. Williams, Christopher Uy, and Jennifer A. McCombe. Canadian consensus guidelines for the diagnosis and treatment of autoimmune encephalitis in adults. Canadian Journal of Neurological Sciences / Journal Canadien des Sciences Neurologiques, 51:734-754, Feb 2024. URL: https://doi.org/10.1017/cjn.2024.16, doi:10.1017/cjn.2024.16. This article has 33 citations.
