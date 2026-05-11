---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T06:49:47.703971'
end_time: '2026-05-10T07:23:43.742548'
duration_seconds: 2036.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neuromyelitis Optica Spectrum Disorder with Anti-AQP4 Antibodies
  mondo_id: ''
  category: Neurological Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 63
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neuromyelitis Optica Spectrum Disorder with Anti-AQP4 Antibodies
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **Neuromyelitis Optica Spectrum Disorder with Anti-AQP4 Antibodies** covering all of the
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
- **Disease Name:** Neuromyelitis Optica Spectrum Disorder with Anti-AQP4 Antibodies
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **Neuromyelitis Optica Spectrum Disorder with Anti-AQP4 Antibodies** covering all of the
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


## Comprehensive Research Report: Neuromyelitis Optica Spectrum Disorder (NMOSD) with Anti–Aquaporin-4 (AQP4) Antibodies

### Scope and evidence provenance
This report synthesizes evidence from international diagnostic criteria, pivotal randomized controlled trials (RCTs), real‑world cohorts, and 2023–2024 mechanistic/epidemiologic updates. Evidence is drawn from aggregated disease-level resources (consensus criteria, RCTs, registries/cohorts, reviews) rather than individual EHR records, except where explicitly described as real‑world chart review. (wingerchuk2015internationalconsensusdiagnostic pages 3-3, pittock2019eculizumabinaquaporin4–positive pages 1-2, ringelstein2024eculizumabusein pages 1-2)

### Key 2023–2024 takeaways (executive summary)
* **Epidemiology:** Recent population-based data (Sardinia) estimate **prevalence 2.6/100,000** and **incidence 1.9 per million person‑years** for AQP4‑IgG+ NMOSD, with **median onset age 54** and **96% female** among incident cases. (May 2024; https://doi.org/10.1016/j.msard.2024.105522) (sechi2024epidemiologyofaquaporin4iggpositive pages 8-12)
* **Sex ratio meta-analysis:** A 2024 PRISMA meta-analysis across 19,415 individuals estimated **female:male 8.89** for AQP4‑IgG+ NMOSD and mean onset age influenced by population longevity. (Jul 2024; https://doi.org/10.1007/s00415-024-12452-8) (arnett2024sexratioand pages 1-2)
* **Mechanistic advances:** 2024 studies link **complement + AQP4 immune complexes** to **complement‑dependent IL‑6/IL‑17A release** (Th17 bias) and identify **IFN‑γ signaling as a regulator of AQP4‑specific Th17/B‑cell responses**, enabling new tolerance/immune‑modulating model systems. (Feb 2024; https://doi.org/10.1038/s41598-024-53661-5) (nishiyama2024antiaquaporin4immunecomplex pages 1-2) and (Nov 2024; https://doi.org/10.1093/brain/awad373) (arellano2024interferonγcontrolsaquaporin4specific pages 1-2)
* **Therapeutics update:** 2024 adds **ravulizumab (long‑acting C5 inhibition)** evidence via CHAMPION‑NMOSD pharmacology and indirect comparisons; real‑world data refine **meningococcal vaccine timing risks** for eculizumab users. (Jan 2024; https://doi.org/10.3389/fneur.2024.1332890) (clardy2024networkmetaanalysisof pages 1-3) and (Nov 2024; https://doi.org/10.1212/WNL.0000000000209888) (ringelstein2024eculizumabusein pages 1-2)

---

## 1. Disease Information
### 1.1 Definition and overview
NMOSD with anti‑AQP4 antibodies is an autoimmune inflammatory CNS disorder distinct from multiple sclerosis, unified under the term **neuromyelitis optica spectrum disorders (NMOSD)** and **stratified by AQP4‑IgG serostatus** (AQP4‑IgG positive vs negative/unknown). (wingerchuk2015internationalconsensusdiagnostic pages 1-2, wingerchuk2015internationalconsensusdiagnostic pages 3-3)

**Core concept:** In AQP4‑IgG+ disease, pathogenic antibodies target the astrocyte water channel **aquaporin‑4** (AQP4), producing an **astrocytopathy** with secondary demyelination and neuroaxonal injury. (contentti2021neuromyelitisopticaspectrum pages 1-2, collongues2019pharmacotherapyforneuromyelitis pages 1-2)

### 1.2 Key identifiers and controlled vocabularies
* **MONDO / Orphanet / ICD-10/ICD-11 / MeSH:** Not retrieved in the current evidence set; recommended to populate from MONDO/Orphanet/WHO ICD browsers and MeSH “Neuromyelitis Optica” entries. (Gap)

### 1.3 Synonyms and alternative names
* Neuromyelitis optica (NMO)
* Devic disease (historical)
* AQP4‑IgG‑positive NMOSD / AQP4‑Ab+ NMOSD (wingerchuk2015internationalconsensusdiagnostic pages 3-3, wingerchuk2015internationalconsensusdiagnostic pages 5-6)

### 1.4 Diagnostic category per 2015 IPND
The 2015 International Panel for NMO Diagnosis (IPND) created two categories:
1) **NMOSD with AQP4‑IgG**
2) **NMOSD without AQP4‑IgG (or unknown)** (wingerchuk2015internationalconsensusdiagnostic pages 3-3, bennett2016findingnmothe pages 11-12)

Visual evidence: the IPND criteria table is available as a cropped image from the original consensus paper. (wingerchuk2015internationalconsensusdiagnostic media 83817c93)

---

## 2. Etiology
### 2.1 Primary causal factors
**Autoantibody-mediated astrocytopathy**: AQP4‑IgG binds AQP4 at astrocyte endfeet, triggers classical complement activation and inflammatory injury; astrocyte loss precedes secondary demyelination/neuronal injury. (contentti2021neuromyelitisopticaspectrum pages 1-2, collongues2019pharmacotherapyforneuromyelitis pages 1-2)

### 2.2 Risk factors
**Sex:** Strong female predominance is consistent across cohorts and meta-analysis (female:male ~8.9 overall). (arnett2024sexratioand pages 1-2, sechi2024epidemiologyofaquaporin4iggpositive pages 8-12)

**Coexisting autoimmunity:** Coexisting systemic autoimmune diseases are common; in Sardinia **52%** had concomitant autoimmune disorders (autoimmune thyroiditis most frequent). (sechi2024epidemiologyofaquaporin4iggpositive pages 8-12, sechi2024epidemiologyofaquaporin4iggpositive pages 34-37)

**Environmental factors (suggested):** Proposed factors include infections, smoking, and vitamin D deficiency, based on epidemiologic discussion; high-quality causal estimates were not identified in the current evidence set. (sechi2024epidemiologyofaquaporin4iggpositive pages 34-37)

### 2.3 Genetic susceptibility (non-Mendelian)
No single causal gene defines AQP4‑IgG+ NMOSD. Reported susceptibility loci/haplotypes include **HLA‑DPB1**, **HLA‑DRB1*03:01**, immune regulatory variants (e.g., **PTPN22 PD‑1.3A allele**, **CD226 Gly307Ser**) and possible protective signal at **CYP7A1 G/G**; **HLA‑DRB1*1501** (MS risk) is not associated with NMO. (melamed2015updateonbiomarkers pages 4-5, contentti2021neuromyelitisopticaspectrum pages 2-4)

### 2.4 Protective factors and gene–environment interactions
No robust protective factors or formal gene–environment interaction studies were retrieved in the current evidence set. (Gap)

---

## 3. Phenotypes
### 3.1 Core clinical characteristics (2015 IPND)
For AQP4‑IgG+ NMOSD, **≥1** of the following core clinical characteristics is sufficient (with AQP4‑IgG positivity and exclusion of alternative diagnoses):
1) Optic neuritis
2) Acute myelitis
3) Area postrema syndrome (hiccups or nausea/vomiting)
4) Acute brainstem syndrome
5) Diencephalic syndrome (e.g., symptomatic narcolepsy) with typical features
6) Symptomatic cerebral syndrome with NMOSD-typical lesions (wingerchuk2015internationalconsensusdiagnostic pages 3-3, bennett2016findingnmothe pages 11-12)

### 3.2 Frequency and presentation statistics
**AQP4‑IgG+ cohort phenotype frequencies (Korea cohort evaluating 2015 criteria):**
* Acute myelitis occurred in **190/226 (84%)** (disease course) (hyun2016evaluationofthe pages 4-6)
* Symptomatic brain syndromes occurred in **100/252 (40%)** overall, with lesion-category counts **area postrema 16%**, **brainstem 16%**, **cerebral 15%** (hyun2016evaluationofthe pages 4-6)

**Sardinia incident AQP4‑IgG+ cases (2013–2022):**
* LETM **68%**
* Optic neuritis **16%**
* Brainstem syndromes **6%**
* Encephalitis **3%**
* Combinations **6%** (including area postrema syndromes) (sechi2024epidemiologyofaquaporin4iggpositive pages 8-12)

### 3.3 Temporal patterns (onset and course)
NMOSD is generally **relapsing**: 80–90% relapsing course; after first attack **60% relapse within 1 year** and **90% within 3 years** (older but widely cited synthesis). (jasiakzatonska2016theimmunologyof pages 3-6)

### 3.4 Quality of life (QoL)
QoL and fatigue are recognized as burdensome symptoms in NMOSD, but disease‑specific quantitative QoL metrics and 2023–2024 trial‑embedded QoL data were not retrieved in the current evidence set. (duchow2020currentandemerging pages 1-5)

### 3.5 Suggested HPO terms (examples)
* Optic neuritis – **HP:0000540**
* Transverse myelitis – **HP:0002240**
* Nausea – **HP:0002018**; Vomiting – **HP:0002013**; Hiccups – **HP:0002030** (area postrema syndrome features)
* Paraplegia – **HP:0003401**
* Blindness – **HP:0000618**
(These ontology mappings are suggested; not validated in retrieved texts.)

---

## 4. Genetic / Molecular Information
### 4.1 Causal genes
NMOSD with AQP4‑IgG is not a monogenic disorder; **AQP4** is the antigenic target, not typically mutated. (contentti2021neuromyelitisopticaspectrum pages 1-2)

### 4.2 AQP4 protein biology relevant to pathogenesis
AQP4 is enriched at **astrocyte endfeet** and forms supramolecular **orthogonal arrays of particles (OAPs)**, with M23 favoring OAPs; OAP clustering facilitates complement activation after antibody binding. (chan2021treatmentofneuromyelitis pages 2-3, contentti2021neuromyelitisopticaspectrum pages 2-4)

### 4.3 Biomarkers and targets
* **AQP4‑IgG (serum)** is the key diagnostic biomarker; CSF-only positivity is rare. (wingerchuk2015internationalconsensusdiagnostic pages 5-6, contentti2021neuromyelitisopticaspectrum pages 2-4)
* **GFAP** is discussed as an emerging biomarker concept in the biomarker literature; prospective validation was not available in the retrieved primary dataset. (bennett2016findingnmothe pages 3-4)
* Therapeutic targets with approval-stage evidence include **IL6R**, **CD19**, **C5** (OpenTargets). (OpenTargets Search: Neuromyelitis optica spectrum disorder)

### 4.4 Epigenetics and omics
No robust epigenetic or multi‑omics (transcriptomic/proteomic/metabolomic) signatures were retrieved in the current evidence set. (Gap)

---

## 5. Mechanism / Pathophysiology
### 5.1 Causal chain (current understanding)
1) Peripheral immune dysregulation with plasmablast expansion; **IL‑6 supports plasmablast survival** and AQP4‑Ab secretion. (contentti2021neuromyelitisopticaspectrum pages 2-4)
2) AQP4‑IgG enters CNS via disrupted BBB or permissive regions and binds AQP4 on astrocyte endfeet/ependymal surfaces. (contentti2021neuromyelitisopticaspectrum pages 2-4)
3) Binding triggers **classical complement activation** and inflammatory infiltration (neutrophils/eosinophils/macrophages), causing astrocyte injury with loss of AQP4 and GFAP, then secondary demyelination and neuronal injury. (collongues2019pharmacotherapyforneuromyelitis pages 1-2, contentti2021neuromyelitisopticaspectrum pages 1-2)

### 5.2 2024 mechanistic developments
**Complement-dependent Th17 cytokine release:** PBMCs from treatment‑naïve AQP4‑IgG+ NMOSD patients stimulated with AQP4 immune complexes + complement produced elevated **IL‑17A and IL‑6**, supporting a complement‑dependent Th17‑biased peripheral inflammatory loop. (Feb 2024; https://doi.org/10.1038/s41598-024-53661-5) (nishiyama2024antiaquaporin4immunecomplex pages 1-2)

**IFN‑γ axis and modeling:** Decreased IFN‑γ receptor signaling and IFN‑γ depletion in AQP4 peptide‑immunized mice produced severe NMOSD‑like disease; IL‑6/Th17 activation increased, and targeting IL‑17A, IL‑6R, or B cells improved disease; a tolerance strategy (AQP4‑peptide PLGA nanoparticles) prevented/treated disease in the model. (Nov 2024; https://doi.org/10.1093/brain/awad373) (arellano2024interferonγcontrolsaquaporin4specific pages 1-2)

### 5.3 Suggested GO biological processes / cell types (examples)
* GO:0006956 **complement activation**
* GO:0006955 **immune response**
* GO:0006954 **inflammatory response**
* GO:0006957 **complement activation, classical pathway**
* CL:0000127 **astrocyte**; CL:0000540 **microglial cell**; CL:0000775 **neutrophil**; CL:0000236 **B cell**; CL:0000624 **CD4-positive T cell**
(These are suggested mappings; not explicitly enumerated in the retrieved texts.)

---

## 6. Anatomical Structures Affected
### 6.1 Organ/system level
Primarily affects the **central nervous system** with lesions in:
* **Optic nerve/chiasm** (optic neuritis) (wingerchuk2015internationalconsensusdiagnostic pages 5-6)
* **Spinal cord** (LETM; central cord predilection) (wingerchuk2015internationalconsensusdiagnostic pages 5-6)
* **Dorsal medulla/area postrema** (area postrema syndrome) (wingerchuk2015internationalconsensusdiagnostic pages 5-6)
* **Periependymal regions** around the third/fourth ventricles, hypothalamus/thalamus (wingerchuk2015internationalconsensusdiagnostic pages 5-6)

### 6.2 Tissue/cell level
Targeted cell compartment: **astrocyte endfeet at the BBB** and **ependymal surfaces**, reflecting AQP4 localization. (collongues2019pharmacotherapyforneuromyelitis pages 1-2, contentti2021neuromyelitisopticaspectrum pages 2-4)

### 6.3 Subcellular level
AQP4 supramolecular organization into **OAPs** influences complement activation, linking membrane organization to cytotoxicity. (chan2021treatmentofneuromyelitis pages 2-3, jasiakzatonska2016theimmunologyof pages 8-10)

---

## 7. Temporal Development
* **Onset:** Typically adult onset; in Sardinia median onset 54 years with rare pediatric onset. (sechi2024epidemiologyofaquaporin4iggpositive pages 8-12)
* **Course:** Relapses drive disability; gradual progression is rare (red flag). (wingerchuk2015internationalconsensusdiagnostic pages 3-4)

---

## 8. Inheritance and Population
### 8.1 Epidemiology (recent quantitative estimates)
* Population-based Sardinia study (May 2024): **incidence 1.9 per million person‑years** and **prevalence 2.6 per 100,000** (AQP4‑IgG+ NMOSD). (sechi2024epidemiologyofaquaporin4iggpositive pages 8-12)
* Reviews summarize broad prevalence ranges and highlight ancestry differences (higher in East‑Asian and African‑Caribbean populations). (duchow2020currentandemerging pages 1-5, sechi2024epidemiologyofaquaporin4iggpositive pages 12-14)

### 8.2 Sex ratio and age of onset
Meta-analysis estimate for AQP4‑IgG+ NMOSD: **female:male 8.89 (95% CI 7.78–10.15)**; pediatric estimate 5.68; late-onset 5.48. (Jul 2024; https://doi.org/10.1007/s00415-024-12452-8) (arnett2024sexratioand pages 1-2)

### 8.3 Inheritance
No Mendelian inheritance pattern is established; susceptibility appears polygenic/immune‑regulatory. (melamed2015updateonbiomarkers pages 4-5)

---

## 9. Diagnostics
### 9.1 Clinical criteria (2015 IPND)
For **AQP4‑IgG+ NMOSD** diagnosis requires:
1) **At least one** core clinical characteristic,
2) **Positive AQP4‑IgG** (best available method; CBA strongly recommended),
3) **Exclusion of alternative diagnoses**. (wingerchuk2015internationalconsensusdiagnostic pages 3-3, bennett2016findingnmothe pages 11-12)

### 9.2 AQP4‑IgG testing and performance
2015 IPND emphasizes **cell‑based serum assays** (microscopy/flow) as preferred, citing pooled mean sensitivity ~**76.7%** and very low false-positive rate (~**0.1%** in an MS clinic cohort), while ELISA and IIF have lower sensitivity and more false positives. (wingerchuk2015internationalconsensusdiagnostic pages 5-6)

A separate review summarizes assay performance across platforms (example: CBA ~91% sensitivity/100% specificity reported in that review). (jasiakzatonska2016theimmunologyof pages 11-14)

### 9.3 MRI and CSF patterns
* **Spinal MRI:** LETM (≥3 vertebral segments), central gray matter predilection. (wingerchuk2015internationalconsensusdiagnostic pages 4-5)
* **Optic nerve MRI:** long lesions, posterior/chiasm involvement. (wingerchuk2015internationalconsensusdiagnostic pages 4-5)
* **Brain MRI:** dorsal medulla/area postrema; periependymal third/fourth ventricle lesions; hypothalamus/thalamus; long corticospinal/corpus callosum lesions. (wingerchuk2015internationalconsensusdiagnostic pages 5-6)
* **CSF (typical):** pleocytosis often >50 cells/mm³, neutrophils; elevated protein (100–500 mg/dL); oligoclonal bands uncommon (~15–30%). (jasiakzatonska2016theimmunologyof pages 3-6)

### 9.4 Differential diagnosis
Red flags favoring MS include Dawson fingers/cortical lesions, typical MS brain lesion distribution, and high frequency of oligoclonal bands; MOG‑IgG should be tested in seronegative NMOSD phenotypes. (wingerchuk2015internationalconsensusdiagnostic pages 5-6, seze2016neuromyelitisopticaspectrum pages 1-2)

### 9.5 Suggested LOINC-like test concepts (examples)
* Serum aquaporin‑4 IgG by cell-based immunoassay (preferred)
* CSF oligoclonal bands
* CSF cell count and differential
(Actual LOINC codes not retrieved.)

---

## 10. Outcome / Prognosis
### 10.1 Relapse-driven disability
Relapses are the main driver of irreversible disability; severe relapses can cause blindness and paralysis. (contentti2021neuromyelitisopticaspectrum pages 2-4)

### 10.2 Relapse probability and prognostic factors
Older synthesis: after first attack **60% relapse within 1 year** and **90% within 3 years**; worse prognosis linked to high early relapse frequency, severe first attack, and coexisting systemic autoimmunity. (jasiakzatonska2016theimmunologyof pages 3-6)

Pediatric AQP4‑IgG+ NMOSD: non‑White ethnicity associated with shorter time to first relapse and worse EDSS at last follow‑up. (paolilo2020treatmentandoutcome pages 3-4)

### 10.3 Modern outcomes with targeted therapy
Real-world eculizumab cohort (Germany/Austria, 2014–2022): **88% attack-free**; median annualized attack rate decreased from 1.0 to 0; EDSS stable (median 6.0). (ringelstein2024eculizumabusein pages 1-2)

---

## 11. Treatment
### 11.1 Acute relapse treatment
* High-dose IV methylprednisolone is standard initial therapy; plasma exchange (PLEX) is used for refractory attacks. (contentti2021neuromyelitisopticaspectrum pages 2-4, tugizova2021newtherapeuticlandscape pages 1-4)

### 11.2 Relapse prevention: pivotal trials (key statistics)
* **Eculizumab (C5 inhibitor; PREVENT RCT, NEJM 2019):** relapses **3/96 (3%)** vs **20/47 (43%)**; **HR 0.06** (95% CI 0.02–0.20; p<0.001); trial ARR 0.02 vs 0.35. (Aug 2019; https://doi.org/10.1056/NEJMoa1900866) (pittock2019eculizumabinaquaporin4–positive pages 1-2)
* **Satralizumab (IL‑6R inhibitor):**
  * Add-on SAkuraSky (NEJM 2019): relapse **20%** vs **43%** overall; AQP4‑IgG+ subgroup relapse **11%** vs **43%**; HRs provided in secondary synthesis. (contentti2021neuromyelitisopticaspectrum pages 11-13)
  * Monotherapy SAkuraStar (Lancet Neurol 2020): relapse **30%** vs **50%**; **HR 0.45** (95% CI 0.23–0.89; p=0.018). (May 2020; https://doi.org/10.1016/S1474-4422(20)30078-8) (traboulsee2020safetyandefficacy pages 1-2)
* **Inebilizumab (anti‑CD19; N‑MOmentum):** relapse **12% (21/174)** vs **39% (22/56)**; AQP4+ relapse **11% (18/161)** vs **42% (22/52)**; disability benefit reported (3‑month CDP HR 0.375). (tugizova2021newtherapeuticlandscape pages 9-11)

### 11.3 Real-world implementation and safety considerations (2024)
**Eculizumab real-world cohort:** vaccination prior to therapy was common; **19%** had attacks shortly after pre‑treatment meningococcal vaccination when not on prednisone; serious infections in 13% and deaths in 10% (including meningococcal sepsis). (ringelstein2024eculizumabusein pages 1-2)

### 11.4 Ravulizumab (2024 update)
Ravulizumab achieved immediate and sustained terminal complement inhibition in CHAMPION‑NMOSD pharmacology analyses; indirect comparisons suggest strong relapse prevention versus other mechanisms. (clardy2024networkmetaanalysisof pages 1-3)

### 11.5 Suggested MAXO terms (examples)
* Plasma exchange therapy – MAXO:0000503 (suggested)
* High‑dose corticosteroid therapy – MAXO term needed (suggested)
* Monoclonal antibody therapy – MAXO:0000142 (suggested)
(Exact MAXO IDs not retrieved.)

---

## 12. Prevention
### 12.1 Primary prevention
No established strategy prevents initial development of AQP4‑IgG autoimmunity. (Gap)

### 12.2 Secondary prevention
Early recognition using IPND criteria and high‑specificity AQP4‑IgG testing enables earlier disease-modifying therapy and avoidance of MS therapies that may worsen NMOSD. (wingerchuk2015internationalconsensusdiagnostic pages 3-3, bennett2016findingnmothe pages 3-4)

### 12.3 Tertiary prevention
Maintenance immunotherapy to prevent relapses is the central prevention strategy; complement inhibitor use requires meningococcal vaccination and careful infection vigilance. (chan2021treatmentofneuromyelitis pages 17-19, ringelstein2024eculizumabusein pages 1-2)

---

## 13. Other Species / Natural Disease
Naturally occurring AQP4‑IgG NMOSD in non‑human species was not identified in the current evidence set. (Gap)

---

## 14. Model Organisms
### 14.1 Passive-transfer and experimental lesion models
AQP4‑IgG + complement applied to in vitro/ex vivo CNS tissues or injected into CNS regions produces NMO‑like lesions (AQP4 loss, astrocytopathy, demyelination, neuron loss) but often requires BBB disruption or local delivery, limiting modeling of chronic relapsing disease. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 4-5, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 8-8)

### 14.2 2024 AQP4 peptide immunization model (IFN‑γ depletion)
IFN‑γ depletion in AQP4_201–220‑immunized mice induces severe NMOSD‑like disease and provides a platform to test IL‑17A/IL‑6R/B‑cell targeting and tolerization nanoparticles. (arellano2024interferonγcontrolsaquaporin4specific pages 1-2)

### 14.3 2024 humanized-AQP4 rat model
Gene‑edited rats expressing humanized AQP4 extracellular domains enable astrocyte‑loss lesions to be induced by human AQP4‑specific antibodies, addressing species-binding limitations. (Jul 2024; https://doi.org/10.3390/ijms25158169) (namatame2024humanizedaquaporin4expressingratcreated pages 1-2)

---

## Current applications and real-world implementations
* Clinical application of IPND criteria with cell‑based AQP4‑IgG assays enables diagnosis after a single core clinical event in seropositive patients, influencing earlier initiation of relapse-prevention therapy. (wingerchuk2015internationalconsensusdiagnostic pages 3-3, wingerchuk2015internationalconsensusdiagnostic pages 5-6)
* Relapse prevention now uses mechanism‑targeted biologics (C5 inhibition, IL‑6R blockade, CD19 B‑cell depletion) with demonstrated RCT efficacy and expanding real‑world safety datasets. (pittock2019eculizumabinaquaporin4–positive pages 1-2, traboulsee2020safetyandefficacy pages 1-2, ringelstein2024eculizumabusein pages 1-2)

---

## Expert opinions and authoritative analyses
* The IPND emphasizes that **seropositive NMOSD can present with diverse neuroanatomic syndromes**, and that **cell‑based assays** should be used due to sensitivity/specificity advantages. (wingerchuk2015internationalconsensusdiagnostic pages 5-6, wingerchuk2015internationalconsensusdiagnostic pages 3-3)
* Reviews in high-impact neurology journals frame relapse prevention as the key therapeutic goal because disability accrues from attacks rather than progressive degeneration. (contentti2021neuromyelitisopticaspectrum pages 2-4, levy2021newtherapiesfor pages 3-4)

---

## Embedded evidence summary table
| Item | Key quantitative result | Population/notes | Primary source (journal, year) | URL |
|---|---|---|---|---|
| 2015 IPND definition of AQP4-IgG+ NMOSD | Diagnosis requires **≥1 core clinical characteristic** + **positive AQP4-IgG** (best available assay; cell-based assay preferred) + **exclusion of alternative diagnoses**. Core characteristics: optic neuritis, acute myelitis, area postrema syndrome, acute brainstem syndrome, diencephalic syndrome, symptomatic cerebral syndrome with NMOSD-typical brain lesions (wingerchuk2015internationalconsensusdiagnostic pages 3-3, wingerchuk2015internationalconsensusdiagnostic pages 1-2, wingerchuk2015internationalconsensusdiagnostic pages 5-6) | AQP4-IgG status stratifies NMOSD into seropositive vs seronegative/unknown categories; seronegative cases require more stringent clinico-radiologic evidence (wingerchuk2015internationalconsensusdiagnostic pages 3-3, wingerchuk2015internationalconsensusdiagnostic pages 1-2) | Wingerchuk et al., *Neurology*, 2015 | https://doi.org/10.1212/WNL.0000000000001729 |
| Eculizumab (PREVENT) | Adjudicated relapse in **3/96 (3%)** vs **20/47 (43%)** with placebo; **HR 0.06** (95% CI 0.02-0.20; **P<0.001**). Trial ARR **0.02** vs **0.35**; rate ratio **0.04** (95% CI 0.01-0.15; **P<0.001**) (pittock2019eculizumabinaquaporin4–positive pages 1-2) | Adults with **AQP4-IgG+ NMOSD**; 76% remained on background immunosuppression. Headache and URTI more common; one death from pulmonary empyema in eculizumab arm (pittock2019eculizumabinaquaporin4–positive pages 1-2) | Pittock et al., *New England Journal of Medicine*, 2019 | https://doi.org/10.1056/NEJMoa1900866 |
| Satralizumab add-on (SAkuraSky) | Relapse in **8/41 (20%)** vs **18/42 (43%)** with placebo; **HR 0.38** (95% CI 0.16-0.88). In **AQP4-IgG+** subgroup: **11%** vs **43%**; **HR 0.21** (95% CI 0.06-0.75) (contentti2021neuromyelitisopticaspectrum pages 11-13) | Satralizumab added to stable immunosuppressive therapy; serious adverse events and infections did not differ between groups; pain/fatigue endpoints not significantly different (contentti2021neuromyelitisopticaspectrum pages 11-13) | Yamamura et al., *New England Journal of Medicine*, 2019 | https://doi.org/10.1056/NEJMoa1901747 |
| Satralizumab monotherapy (SAkuraStar) | Protocol-defined relapse in **19/63 (30%)** vs **16/32 (50%)** with placebo; **HR 0.45** (95% CI 0.23-0.89; **P=0.018**) (traboulsee2020safetyandefficacy pages 1-2) | Monotherapy phase 3 trial in NMOSD; adverse-event rates **473.9 vs 495.2 per 100 patient-years** (satralizumab vs placebo), with similar serious adverse events and withdrawals (traboulsee2020safetyandefficacy pages 1-2) | Traboulsee et al., *The Lancet Neurology*, 2020 | https://doi.org/10.1016/S1474-4422(20)30078-8 |
| Inebilizumab (N-MOmentum) | Relapse in **21/174 (12%)** vs **22/56 (39%)** with placebo; **HR 0.27**. In **AQP4-IgG+** subgroup: **18/161 (11%)** vs **22/52 (42%)**; **HR 0.23**. Three-month confirmed disability progression: **HR 0.375** (95% CI 0.148-0.952; **P=0.0390**) (tugizova2021newtherapeuticlandscape pages 9-11) | Anti-CD19 B-cell depletion; serious adverse events **5% (8/174)** vs **9% (5/56)**, transient grade 3 neutropenia **2%**, infusion reactions similar; two deaths occurred in open-label period (tugizova2021newtherapeuticlandscape pages 9-11) | Cree et al., *The Lancet*, 2019; Marignier et al., *Neurology: Neuroimmunology & Neuroinflammation*, 2021 | https://doi.org/10.1016/S0140-6736(19)31817-3 |
| 2024 update: Ravulizumab (CHAMPION-NMOSD PK/PD) | In **58** treated patients, serum ravulizumab stayed above therapeutic threshold in **all patients** through 50 weeks; **immediate and complete terminal complement inhibition** (free C5 **<0.5 μg/mL**) achieved by end of first infusion and sustained. Trial summary notes **no adjudicated on-trial relapses** among ravulizumab recipients (clardy2024networkmetaanalysisof pages 1-3) | Long-acting C5 inhibitor in adults with **AQP4+ NMOSD**; weight-based loading then maintenance every 8 weeks (clardy2024networkmetaanalysisof pages 1-3) | Ortiz et al., *Frontiers in Neurology*, 2024 | https://doi.org/10.3389/fneur.2024.1332890 |
| 2024 update: Ravulizumab network meta-analysis | Compared with monotherapy alternatives, ravulizumab showed lower relapse risk vs **inebilizumab HR 0.09** (95% CrI 0.02-0.57) and **satralizumab HR 0.08** (95% CrI 0.01-0.55), and was comparable to **eculizumab HR 0.86** (95% CrI 0.16-4.52). ARR about **98% lower** vs inebilizumab/satralizumab monotherapy (clardy2024networkmetaanalysisof pages 1-3) | Bayesian network meta-analysis using PREVENT, N-MOmentum, SAkuraSky, SAkuraStar, and CHAMPION-NMOSD; indirect comparisons only, no head-to-head RCTs (clardy2024networkmetaanalysisof pages 1-3) | Clardy et al., *Neurology and Therapy*, 2024 | https://doi.org/10.1007/s40120-024-00597-7 |
| 2024 update: Real-world eculizumab effectiveness/safety | In **52** AQP4-IgG+ patients, **88% attack-free** on eculizumab; median annualized attack rate fell from **1.0** pre-treatment to **0** (**P<0.001**). Serious infections in **13%**, deaths in **10%**; among 36 vaccinated pre-eculizumab without prednisone, **7 (19%)** had attacks shortly after vaccination (ringelstein2024eculizumabusein pages 1-2) | Multicenter German/Austrian real-world cohort; disability median EDSS remained stable at **6.0** and MRI lesion activity decreased (ringelstein2024eculizumabusein pages 1-2) | Ringelstein et al., *Neurology*, 2024 | https://doi.org/10.1212/WNL.0000000000209888 |


*Table: This table summarizes the defining 2015 diagnostic criteria for AQP4-IgG-positive NMOSD and the major relapse-prevention therapies with pivotal trial outcomes, plus key 2024 clinical updates. It is useful as a compact reference for diagnosis and current treatment evidence.*

---

## Notable evidence gaps (for knowledge-base completion)
* Ontology identifiers (MONDO, ICD-10/11, Orphanet, MeSH) were not retrievable from the current tool context and should be filled via dedicated ontology lookups.
* Robust 2023–2024 QoL metrics, OCT retinal thickness meta-analytic values, and multi‑omics/epigenetic datasets were not captured in the evidence retrieved here.



References

1. (wingerchuk2015internationalconsensusdiagnostic pages 3-3): Dean M. Wingerchuk, Brenda Banwell, Jeffrey L. Bennett, Philippe Cabre, William Carroll, Tanuja Chitnis, Jérôme de Seze, Kazuo Fujihara, Benjamin Greenberg, Anu Jacob, Sven Jarius, Marco Lana-Peixoto, Michael Levy, Jack H. Simon, Silvia Tenembaum, Anthony L. Traboulsee, Patrick Waters, Kay E. Wellik, and Brian G. Weinshenker. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. Neurology, 85:177-189, Jul 2015. URL: https://doi.org/10.1212/wnl.0000000000001729, doi:10.1212/wnl.0000000000001729. This article has 5364 citations and is from a highest quality peer-reviewed journal.

2. (pittock2019eculizumabinaquaporin4–positive pages 1-2): Sean J. Pittock, Achim Berthele, Kazuo Fujihara, Ho Jin Kim, Michael Levy, Jacqueline Palace, Ichiro Nakashima, Murat Terzi, Natalia Totolyan, Shanthi Viswanathan, Kai-Chen Wang, Amy Pace, Kenji P. Fujita, Róisín Armstrong, and Dean M. Wingerchuk. Eculizumab in aquaporin-4–positive neuromyelitis optica spectrum disorder. New England Journal of Medicine, 381:614-625, Aug 2019. URL: https://doi.org/10.1056/nejmoa1900866, doi:10.1056/nejmoa1900866. This article has 957 citations and is from a highest quality peer-reviewed journal.

3. (ringelstein2024eculizumabusein pages 1-2): Marius Ringelstein, Susanna Asseyer, Gero Lindenblatt, Katinka Fischer, Refik Pul, Jelena Skuljec, Lisa Revie, Katrin Giglhuber, Vivien Häußler, Michael Karenfort, Kerstin Hellwig, Friedemann Paul, Judith Bellmann-Strobl, Carolin Otto, Klemens Ruprecht, Tjalf Ziemssen, Alexander Emmer, Veit Rothhammer, Florian T. Nickel, Klemens Angstwurm, Ralf Linker, Sarah A. Laurent, Clemens Warnke, Sven Jarius, Mirjam Korporal-Kuhnke, Brigitte Wildemann, Stephanie Wolff, Maria Seipelt, Yavor Yalachkov, Nele Retzlaff, Uwe K. Zettl, Paulus S. Rommer, Markus C. Kowarik, Jonathan Wickel, Christian Geis, Martin W. Hümmert, Corinna Trebst, Makbule Senel, Ralf Gold, Luisa Klotz, Christoph Kleinschnitz, Sven G. Meuth, Orhan Aktas, Achim Berthele, and Ilya Ayzenberg. Eculizumab use in neuromyelitis optica spectrum disorders. Neurology, Nov 2024. URL: https://doi.org/10.1212/wnl.0000000000209888, doi:10.1212/wnl.0000000000209888. This article has 32 citations and is from a highest quality peer-reviewed journal.

4. (sechi2024epidemiologyofaquaporin4iggpositive pages 8-12): Elia Sechi, Mariangela Puci, Maria Ida Pateri, Pietro Zara, Sabrine Othmani, Stefano Sotgiu, Maria Valeria Saddi, Stefania Leoni, Giuseppe Fenu, Maurizio Melis, Giovanni Sotgiu, Paolo Solla, Eleonora Cocco, and Jessica Frau. Epidemiology of aquaporin-4-igg-positive nmosd in sardinia. Multiple Sclerosis and Related Disorders, 85:105522, May 2024. URL: https://doi.org/10.1016/j.msard.2024.105522, doi:10.1016/j.msard.2024.105522. This article has 4 citations and is from a peer-reviewed journal.

5. (arnett2024sexratioand pages 1-2): Simon Arnett, Sin Hong Chew, Unnah Leitner, Jyh Yung Hor, Friedemann Paul, Michael R. Yeaman, Michael Levy, Brian G. Weinshenker, Brenda L. Banwell, Kazuo Fujihara, Hesham Abboud, Irena Dujmovic Basuroski, Georgina Arrambide, Veronika E. Neubrand, Chao Quan, Esther Melamed, Jacqueline Palace, Jing Sun, Nasrin Asgari, Simon A. Broadley, Hesham Abboud, Orhan Aktas, Raed Alroughani, Ayse Altintas, Metha Apiwattannakul, Georgina Arrambide, Jagannadha Avasarala, Brenda Banwell, Terrence F. Blaschke, James Bowen, Edgar Carnero Contentti, Tanuja Chitnis, Jerome de Seze, Guillermo Delgado-Garcia, Irena Dujmovic Basuroski, Jose Flores, Kazuo Fujihara, Lorna Galleguillos, Benjamin M. Greenberg, May Han, Joachim Havla, Kerstin Hellwig, Jyh Yung Hor, Sven Jarius, Jorge Andres Jimenez, Najib Kissani, Ingo Kleiter, Marco Lana-Peixoto, M. Isabel Leite, Michael Levy, Sara Mariotto, Maureen A. Mealy, Veronika E. Neubrand, Celia Oreja-Guevara, Lekha Pandit, Sarah M. Planchon, Anne-Katrin Pröbstel, Peiqing Qian, Chao Quan, Pavle Repovic, Claire Riley, Marius Ringelstein, Juan I.Rojas, Dalia Rotstein, Klemens Ruprecht, Maria José Sá, Albert Saiz, Sara Salama, Sasitorn Siritho, Aksel Siva, Terry J. Smith, Elias S. Sotirchos, Ibis Soto de Castillo, Silvia Tenembaum, Pablo Villoslada, Barbara Willekens, Dean Wingerchuk, Bassem I. Yamout, and Michael Yeaman. Sex ratio and age of onset in aqp4 antibody-associated nmosd: a review and meta-analysis. Journal of Neurology, 271:4794-4812, Jul 2024. URL: https://doi.org/10.1007/s00415-024-12452-8, doi:10.1007/s00415-024-12452-8. This article has 39 citations and is from a domain leading peer-reviewed journal.

6. (nishiyama2024antiaquaporin4immunecomplex pages 1-2): Shuhei Nishiyama, Jin Myong Seok, Amy E. Wright, Itay Lotan, Takahisa Mikami, Natalia C. Drosu, Natasha Bobrowski-Khoury, Monique R. Anderson, Philippe A. Bilodeau, Patrick Schindler, Friedemann Paul, Masashi Aoki, Michael R. Yeaman, Michael Levy, Jacinta M. Behne, Megan K. Behne, Jeffrey L. Bennett, Terrence F. Blaschke, Tanuja Chitnis, Lawrence J. Cook, Michael Levy, Sarah M. Planchon, Pavle Repovic, Claire S. Riley, Terry J. Smith, Anthony Traboulsee, and Michael R. Yeaman. Anti-aquaporin-4 immune complex stimulates complement-dependent th17 cytokine release in neuromyelitis optica spectrum disorders. Scientific Reports, Feb 2024. URL: https://doi.org/10.1038/s41598-024-53661-5, doi:10.1038/s41598-024-53661-5. This article has 20 citations and is from a peer-reviewed journal.

7. (arellano2024interferonγcontrolsaquaporin4specific pages 1-2): Gabriel Arellano, Eileah Loda, Yanan Chen, Tobias Neef, Andrew C Cogswell, Grant Primer, Godwin Joy, Kevin Kaschke, Samantha Wills, Joseph R Podojil, Brian Popko, Roumen Balabanov, and Stephen D Miller. Interferon-γ controls aquaporin-4-specific th17 and b cells in neuromyelitis optica spectrum disorder. Brain : a journal of neurology, 147:1344-1361, Nov 2024. URL: https://doi.org/10.1093/brain/awad373, doi:10.1093/brain/awad373. This article has 26 citations.

8. (clardy2024networkmetaanalysisof pages 1-3): Stacey L. Clardy, Sean J. Pittock, Orhan Aktas, Jin Nakahara, Noriko Isobe, Diego Centonze, Sami Fam, Adrian Kielhorn, Jeffrey C. Yu, Jeroen Jansen, and Ina Zhang. Network meta-analysis of ravulizumab and alternative interventions for the treatment of neuromyelitis optica spectrum disorder. Neurology and Therapy, 13:535-549, May 2024. URL: https://doi.org/10.1007/s40120-024-00597-7, doi:10.1007/s40120-024-00597-7. This article has 24 citations and is from a domain leading peer-reviewed journal.

9. (wingerchuk2015internationalconsensusdiagnostic pages 1-2): Dean M. Wingerchuk, Brenda Banwell, Jeffrey L. Bennett, Philippe Cabre, William Carroll, Tanuja Chitnis, Jérôme de Seze, Kazuo Fujihara, Benjamin Greenberg, Anu Jacob, Sven Jarius, Marco Lana-Peixoto, Michael Levy, Jack H. Simon, Silvia Tenembaum, Anthony L. Traboulsee, Patrick Waters, Kay E. Wellik, and Brian G. Weinshenker. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. Neurology, 85:177-189, Jul 2015. URL: https://doi.org/10.1212/wnl.0000000000001729, doi:10.1212/wnl.0000000000001729. This article has 5364 citations and is from a highest quality peer-reviewed journal.

10. (contentti2021neuromyelitisopticaspectrum pages 1-2): Edgar Carnero Contentti and Jorge Correale. Neuromyelitis optica spectrum disorders: from pathophysiology to therapeutic strategies. Journal of Neuroinflammation, Sep 2021. URL: https://doi.org/10.1186/s12974-021-02249-1, doi:10.1186/s12974-021-02249-1. This article has 376 citations and is from a peer-reviewed journal.

11. (collongues2019pharmacotherapyforneuromyelitis pages 1-2): Nicolas Collongues, Estelle Ayme-Dietrich, Laurent Monassier, and Jérôme de Seze. Pharmacotherapy for neuromyelitis optica spectrum disorders: current management and future options. Drugs, 79:125-142, Jan 2019. URL: https://doi.org/10.1007/s40265-018-1039-7, doi:10.1007/s40265-018-1039-7. This article has 73 citations and is from a domain leading peer-reviewed journal.

12. (wingerchuk2015internationalconsensusdiagnostic pages 5-6): Dean M. Wingerchuk, Brenda Banwell, Jeffrey L. Bennett, Philippe Cabre, William Carroll, Tanuja Chitnis, Jérôme de Seze, Kazuo Fujihara, Benjamin Greenberg, Anu Jacob, Sven Jarius, Marco Lana-Peixoto, Michael Levy, Jack H. Simon, Silvia Tenembaum, Anthony L. Traboulsee, Patrick Waters, Kay E. Wellik, and Brian G. Weinshenker. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. Neurology, 85:177-189, Jul 2015. URL: https://doi.org/10.1212/wnl.0000000000001729, doi:10.1212/wnl.0000000000001729. This article has 5364 citations and is from a highest quality peer-reviewed journal.

13. (bennett2016findingnmothe pages 11-12): Jeffrey L. Bennett. Finding nmo: the evolving diagnostic criteria of neuromyelitis optica. Journal of neuro-ophthalmology : the official journal of the North American Neuro-Ophthalmology Society, 36 3:238-45, Sep 2016. URL: https://doi.org/10.1097/wno.0000000000000396, doi:10.1097/wno.0000000000000396. This article has 57 citations.

14. (wingerchuk2015internationalconsensusdiagnostic media 83817c93): Dean M. Wingerchuk, Brenda Banwell, Jeffrey L. Bennett, Philippe Cabre, William Carroll, Tanuja Chitnis, Jérôme de Seze, Kazuo Fujihara, Benjamin Greenberg, Anu Jacob, Sven Jarius, Marco Lana-Peixoto, Michael Levy, Jack H. Simon, Silvia Tenembaum, Anthony L. Traboulsee, Patrick Waters, Kay E. Wellik, and Brian G. Weinshenker. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. Neurology, 85:177-189, Jul 2015. URL: https://doi.org/10.1212/wnl.0000000000001729, doi:10.1212/wnl.0000000000001729. This article has 5364 citations and is from a highest quality peer-reviewed journal.

15. (sechi2024epidemiologyofaquaporin4iggpositive pages 34-37): Elia Sechi, Mariangela Puci, Maria Ida Pateri, Pietro Zara, Sabrine Othmani, Stefano Sotgiu, Maria Valeria Saddi, Stefania Leoni, Giuseppe Fenu, Maurizio Melis, Giovanni Sotgiu, Paolo Solla, Eleonora Cocco, and Jessica Frau. Epidemiology of aquaporin-4-igg-positive nmosd in sardinia. Multiple Sclerosis and Related Disorders, 85:105522, May 2024. URL: https://doi.org/10.1016/j.msard.2024.105522, doi:10.1016/j.msard.2024.105522. This article has 4 citations and is from a peer-reviewed journal.

16. (melamed2015updateonbiomarkers pages 4-5): Esther Melamed, Michael Levy, Patrick J. Waters, Douglas Kazutoshi Sato, Jeffrey L. Bennett, Gareth R. John, Douglas C. Hooper, Albert Saiz, Amit Bar-Or, Ho Jin Kim, Lakha Pandit, Maria Isabel Leite, Nasrin Asgari, Najib Kissani, Rogier Hintzen, Romain Marignier, Sven Jarius, John Marcelletti, Terry J. Smith, Michael R. Yeaman, May H. Han, Orhan Aktas, Metha Apiwattanakul, Brenda Banwell, Denis Bichuetti, Simon Broadley, Philippe Cabre, Tanuja Chitnis, Jerome De Seze, Kazuo Fujihara, Benjamin Greenberg, Kerstin Hellwig, Raffaele Iorio, Sven Jarius, Eric Klawiter, Ingo Kleiter, Marco Lana-Peixoto, Nakashima, Kevin O'Connor, Jacqueline Palace, Friedman Paul, Naraporn Prayoonwiwat, Klemens Ruprecht, Olaf Stuve, Thomas Tedder, Silvia Tenembaum, Juan P. Garrahan, Buenos Aires, Katja van Herle, Danielle van Pelt, Pablo Villoslada, Emmanuelle Waubant, Brian Weinshenker, Dean Wingerchuk, Jens Würfel, and Scott Zamvil. Update on biomarkers in neuromyelitis optica. Neurology Neuroimmunology &amp; Neuroinflammation, Aug 2015. URL: https://doi.org/10.1212/nxi.0000000000000134, doi:10.1212/nxi.0000000000000134. This article has 146 citations.

17. (contentti2021neuromyelitisopticaspectrum pages 2-4): Edgar Carnero Contentti and Jorge Correale. Neuromyelitis optica spectrum disorders: from pathophysiology to therapeutic strategies. Journal of Neuroinflammation, Sep 2021. URL: https://doi.org/10.1186/s12974-021-02249-1, doi:10.1186/s12974-021-02249-1. This article has 376 citations and is from a peer-reviewed journal.

18. (hyun2016evaluationofthe pages 4-6): Jae-Won Hyun, In Hye Jeong, AeRan Joung, Su-Hyun Kim, and Ho Jin Kim. Evaluation of the 2015 diagnostic criteria for neuromyelitis optica spectrum disorder. Neurology, 86:1772-1779, May 2016. URL: https://doi.org/10.1212/wnl.0000000000002655, doi:10.1212/wnl.0000000000002655. This article has 99 citations and is from a highest quality peer-reviewed journal.

19. (jasiakzatonska2016theimmunologyof pages 3-6): Michalina Jasiak-Zatonska, Alicja Kalinowska-Lyszczarz, Slawomir Michalak, and Wojciech Kozubski. The immunology of neuromyelitis optica—current knowledge, clinical implications, controversies and future perspectives. International Journal of Molecular Sciences, 17:273, Mar 2016. URL: https://doi.org/10.3390/ijms17030273, doi:10.3390/ijms17030273. This article has 148 citations.

20. (duchow2020currentandemerging pages 1-5): Ankelien Duchow, Friedemann Paul, and Judith Bellmann-Strobl. Current and emerging biologics for the treatment of neuromyelitis optica spectrum disorders. Expert Opinion on Biological Therapy, 20:1061-1072, Apr 2020. URL: https://doi.org/10.1080/14712598.2020.1749259, doi:10.1080/14712598.2020.1749259. This article has 25 citations and is from a peer-reviewed journal.

21. (chan2021treatmentofneuromyelitis pages 2-3): Koon-Ho Chan and Chi-Yan Lee. Treatment of neuromyelitis optica spectrum disorders. International Journal of Molecular Sciences, 22:8638, Aug 2021. URL: https://doi.org/10.3390/ijms22168638, doi:10.3390/ijms22168638. This article has 74 citations.

22. (bennett2016findingnmothe pages 3-4): Jeffrey L. Bennett. Finding nmo: the evolving diagnostic criteria of neuromyelitis optica. Journal of neuro-ophthalmology : the official journal of the North American Neuro-Ophthalmology Society, 36 3:238-45, Sep 2016. URL: https://doi.org/10.1097/wno.0000000000000396, doi:10.1097/wno.0000000000000396. This article has 57 citations.

23. (OpenTargets Search: Neuromyelitis optica spectrum disorder): Open Targets Query (Neuromyelitis optica spectrum disorder, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

24. (jasiakzatonska2016theimmunologyof pages 8-10): Michalina Jasiak-Zatonska, Alicja Kalinowska-Lyszczarz, Slawomir Michalak, and Wojciech Kozubski. The immunology of neuromyelitis optica—current knowledge, clinical implications, controversies and future perspectives. International Journal of Molecular Sciences, 17:273, Mar 2016. URL: https://doi.org/10.3390/ijms17030273, doi:10.3390/ijms17030273. This article has 148 citations.

25. (wingerchuk2015internationalconsensusdiagnostic pages 3-4): Dean M. Wingerchuk, Brenda Banwell, Jeffrey L. Bennett, Philippe Cabre, William Carroll, Tanuja Chitnis, Jérôme de Seze, Kazuo Fujihara, Benjamin Greenberg, Anu Jacob, Sven Jarius, Marco Lana-Peixoto, Michael Levy, Jack H. Simon, Silvia Tenembaum, Anthony L. Traboulsee, Patrick Waters, Kay E. Wellik, and Brian G. Weinshenker. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. Neurology, 85:177-189, Jul 2015. URL: https://doi.org/10.1212/wnl.0000000000001729, doi:10.1212/wnl.0000000000001729. This article has 5364 citations and is from a highest quality peer-reviewed journal.

26. (sechi2024epidemiologyofaquaporin4iggpositive pages 12-14): Elia Sechi, Mariangela Puci, Maria Ida Pateri, Pietro Zara, Sabrine Othmani, Stefano Sotgiu, Maria Valeria Saddi, Stefania Leoni, Giuseppe Fenu, Maurizio Melis, Giovanni Sotgiu, Paolo Solla, Eleonora Cocco, and Jessica Frau. Epidemiology of aquaporin-4-igg-positive nmosd in sardinia. Multiple Sclerosis and Related Disorders, 85:105522, May 2024. URL: https://doi.org/10.1016/j.msard.2024.105522, doi:10.1016/j.msard.2024.105522. This article has 4 citations and is from a peer-reviewed journal.

27. (jasiakzatonska2016theimmunologyof pages 11-14): Michalina Jasiak-Zatonska, Alicja Kalinowska-Lyszczarz, Slawomir Michalak, and Wojciech Kozubski. The immunology of neuromyelitis optica—current knowledge, clinical implications, controversies and future perspectives. International Journal of Molecular Sciences, 17:273, Mar 2016. URL: https://doi.org/10.3390/ijms17030273, doi:10.3390/ijms17030273. This article has 148 citations.

28. (wingerchuk2015internationalconsensusdiagnostic pages 4-5): Dean M. Wingerchuk, Brenda Banwell, Jeffrey L. Bennett, Philippe Cabre, William Carroll, Tanuja Chitnis, Jérôme de Seze, Kazuo Fujihara, Benjamin Greenberg, Anu Jacob, Sven Jarius, Marco Lana-Peixoto, Michael Levy, Jack H. Simon, Silvia Tenembaum, Anthony L. Traboulsee, Patrick Waters, Kay E. Wellik, and Brian G. Weinshenker. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. Neurology, 85:177-189, Jul 2015. URL: https://doi.org/10.1212/wnl.0000000000001729, doi:10.1212/wnl.0000000000001729. This article has 5364 citations and is from a highest quality peer-reviewed journal.

29. (seze2016neuromyelitisopticaspectrum pages 1-2): J. D. Seze, L. Kremer, and N. Collongues. Neuromyelitis optica spectrum disorder (nmosd): a new concept. Revue neurologique, 172 4-5:256-62, Apr 2016. URL: https://doi.org/10.1016/j.neurol.2016.03.003, doi:10.1016/j.neurol.2016.03.003. This article has 60 citations and is from a peer-reviewed journal.

30. (paolilo2020treatmentandoutcome pages 3-4): Renata Barbosa Paolilo, Yael Hacohen, Elise Yazbeck, Thais Armangue, Arlette Bruijstens, Christian Lechner, Samira Luisa Apostolos-Pereira, Yana Martynenko, Markus Breu, Carolina de Medeiros Rimkus, Evangeline Wassmer, Matthias Baumann, Laura Papetti, Marco Capobianco, Barbara Kornek, Kevin Rostásy, José Albino da Paz, Olga Ciccarelli, Ming Lim, Albert Saiz, Rinze Neuteboom, Romain Marignier, Cheryl Hemingway, Douglas Kazutoshi Sato, and Kumaran Deiva. Treatment and outcome of aquaporin-4 antibody–positive nmosd. Neurology Neuroimmunology &amp; Neuroinflammation, Sep 2020. URL: https://doi.org/10.1212/nxi.0000000000000837, doi:10.1212/nxi.0000000000000837. This article has 72 citations.

31. (tugizova2021newtherapeuticlandscape pages 1-4): Madina Tugizova, Luka Vlahovic, Anna Tomczak, Nora Sandrine Wetzel, and May Htwe Han. New therapeutic landscape in neuromyelitis optica. Current Treatment Options in Neurology, Mar 2021. URL: https://doi.org/10.1007/s11940-021-00667-3, doi:10.1007/s11940-021-00667-3. This article has 28 citations and is from a peer-reviewed journal.

32. (contentti2021neuromyelitisopticaspectrum pages 11-13): Edgar Carnero Contentti and Jorge Correale. Neuromyelitis optica spectrum disorders: from pathophysiology to therapeutic strategies. Journal of Neuroinflammation, Sep 2021. URL: https://doi.org/10.1186/s12974-021-02249-1, doi:10.1186/s12974-021-02249-1. This article has 376 citations and is from a peer-reviewed journal.

33. (traboulsee2020safetyandefficacy pages 1-2): Anthony Traboulsee, Benjamin M Greenberg, Jeffrey L Bennett, Lech Szczechowski, Edward Fox, Svitlana Shkrobot, Takashi Yamamura, Yusuke Terada, Yuichi Kawata, Padraig Wright, Athos Gianella-Borradori, Hideki Garren, and Brian G Weinshenker. Safety and efficacy of satralizumab monotherapy in neuromyelitis optica spectrum disorder: a randomised, double-blind, multicentre, placebo-controlled phase 3 trial. The Lancet Neurology, 19:402-412, May 2020. URL: https://doi.org/10.1016/s1474-4422(20)30078-8, doi:10.1016/s1474-4422(20)30078-8. This article has 585 citations and is from a highest quality peer-reviewed journal.

34. (tugizova2021newtherapeuticlandscape pages 9-11): Madina Tugizova, Luka Vlahovic, Anna Tomczak, Nora Sandrine Wetzel, and May Htwe Han. New therapeutic landscape in neuromyelitis optica. Current Treatment Options in Neurology, Mar 2021. URL: https://doi.org/10.1007/s11940-021-00667-3, doi:10.1007/s11940-021-00667-3. This article has 28 citations and is from a peer-reviewed journal.

35. (chan2021treatmentofneuromyelitis pages 17-19): Koon-Ho Chan and Chi-Yan Lee. Treatment of neuromyelitis optica spectrum disorders. International Journal of Molecular Sciences, 22:8638, Aug 2021. URL: https://doi.org/10.3390/ijms22168638, doi:10.3390/ijms22168638. This article has 74 citations.

36. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 4-5): Li Xu, Huiming Xu, and Changyong Tang. Aquaporin-4-igg-seropositive neuromyelitis optica spectrum disorders: progress of experimental models based on disease pathogenesis. Neural Regeneration Research, 20:354-365, Jan 2024. URL: https://doi.org/10.4103/nrr.nrr-d-23-01325, doi:10.4103/nrr.nrr-d-23-01325. This article has 16 citations and is from a peer-reviewed journal.

37. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 8-8): Li Xu, Huiming Xu, and Changyong Tang. Aquaporin-4-igg-seropositive neuromyelitis optica spectrum disorders: progress of experimental models based on disease pathogenesis. Neural Regeneration Research, 20:354-365, Jan 2024. URL: https://doi.org/10.4103/nrr.nrr-d-23-01325, doi:10.4103/nrr.nrr-d-23-01325. This article has 16 citations and is from a peer-reviewed journal.

38. (namatame2024humanizedaquaporin4expressingratcreated pages 1-2): Chihiro Namatame, Yoichiro Abe, Yoshiki Miyasaka, Yoshiki Takai, Yuki Matsumoto, Toshiyuki Takahashi, Tomoji Mashimo, Tatsuro Misu, Kazuo Fujihara, Masato Yasui, and Masashi Aoki. Humanized-aquaporin-4-expressing rat created by gene-editing technology and its use to clarify the pathology of neuromyelitis optica spectrum disorder. International Journal of Molecular Sciences, 25:8169, Jul 2024. URL: https://doi.org/10.3390/ijms25158169, doi:10.3390/ijms25158169. This article has 4 citations.

39. (levy2021newtherapiesfor pages 3-4): Michael Levy, Kazuo Fujihara, and Jacqueline Palace. New therapies for neuromyelitis optica spectrum disorder. The Lancet Neurology, 20:60-67, Jan 2021. URL: https://doi.org/10.1016/s1474-4422(20)30392-6, doi:10.1016/s1474-4422(20)30392-6. This article has 170 citations and is from a highest quality peer-reviewed journal.
