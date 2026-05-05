---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T18:26:49.275391'
end_time: '2026-05-04T18:43:30.449232'
duration_seconds: 1001.17
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Capillary Malformation-Arteriovenous Malformation Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 72
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Capillary Malformation-Arteriovenous Malformation Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Capillary Malformation-Arteriovenous Malformation Syndrome** covering all of the
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
- **Disease Name:** Capillary Malformation-Arteriovenous Malformation Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Capillary Malformation-Arteriovenous Malformation Syndrome** covering all of the
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


# Capillary Malformation–Arteriovenous Malformation (CM‑AVM) Syndrome — Disease Characteristics Research Report

## 1. Disease Information

### Concise overview (current understanding)
Capillary malformation–arteriovenous malformation (CM‑AVM) syndrome is a **rare, autosomal dominant vascular malformation disorder** characterized by **multifocal cutaneous capillary malformations (CMs)** and an increased risk of **fast‑flow vascular lesions**, especially **arteriovenous malformations (AVMs)** and **arteriovenous fistulas (AVFs)**. (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, brix2022capillarymalformationarteriovenousmalformation pages 1-2)

A recent systematic review abstract summarizes the canonical definition: CM‑AVM is “**characterized by cutaneous capillary malformations and fast‑flow vascular lesions, including arteriovenous malformations (AVMs) and arteriovenous fistulas (AVFs)**.” (Palermo et al., 2025‑12; https://doi.org/10.1007/s00381-025-07089-5) (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2)

### Key identifiers (retrieved in this run)
| Identifier type | Value | Notes | Source URL |
|---|---|---|---|
| MONDO ID | MONDO_0012016 | Open Targets disease association lists **capillary malformation-arteriovenous malformation syndrome** as MONDO_0012016; associated targets include **RASA1** and **EPHB4** (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2) | https://platform.opentargets.org |
| OMIM | 608354 | CM-AVM / CMAVM / capillary malformation-arteriovenous malformation syndrome; cited as **OMIM #608354** in RASA1-focused CM-AVM literature (wooderchakdonahue2018expandingtheclinical pages 1-2, revencu2020rasa1mosaicmutations pages 1-2) | https://doi.org/10.1038/s41431-018-0196-1 |
| OMIM | 618196 | CM-AVM2; EPHB4-related form explicitly noted as **OMIM #618196** in EPHB4/VOGM literature (zhao2023geneticdysregulationof pages 12-14, zhao2023mutationofkey pages 1-2) | https://doi.org/10.1038/s41467-023-43062-z |
| Orphanet | 137667 | Open Targets evidence includes **Orphanet_137667** for “Capillary malformation - arteriovenous malformation”; direct Orphanet page URL not retrieved in provided evidence (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2) | https://www.orpha.net |
| Synonym | CM-AVM | Standard abbreviation used across cohort/review papers for the syndrome (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, wooderchakdonahue2018expandingtheclinical pages 1-2) | https://doi.org/10.1007/s00381-025-07089-5 |
| Synonym | CMAVM | Variant abbreviation used in clinical genetics/neurovascular literature (le2025arteriovenousmalformations(avms) pages 1-3) | https://doi.org/10.3389/fped.2022.871565 |
| Synonym | capillary malformation-arteriovenous malformation syndrome | Full disease name used in reviews and case series (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, coccia2023prenatalclinicalfindings pages 9-11) | https://doi.org/10.3390/genes14030549 |
| Synonym | capillary malformation–AVM syndrome | Punctuation variant used in recent reviews (morin2025vascularmalformationsfrom pages 5-6) | https://doi.org/10.1038/s44321-025-00344-x |
| Synonym | CM-AVM1 | RASA1-related subtype; papers distinguish **CM-AVM1** from **CM-AVM2** (lin2026chinesecapillarymalformationarteriovenous pages 7-9, zhao2023geneticdysregulationof pages 12-14) | https://doi.org/10.1038/s41467-023-43062-z |
| Synonym | CM-AVM2 | EPHB4-related subtype; recognized in EPHB4 case review and cerebrovascular genetics literature (brix2022capillarymalformationarteriovenousmalformation pages 1-2, zhao2023geneticdysregulationof pages 12-14) | https://doi.org/10.2340/actadv.v102.1126 |


*Table: This table compiles key disease identifiers and commonly used synonyms for capillary malformation-arteriovenous malformation syndrome from the available evidence. It is useful for harmonizing nomenclature across knowledge base entries and linked resources.*

**Notes on missing identifiers:** ICD‑10/ICD‑11 and MeSH terms were not retrieved from the available full texts in this tool run; MONDO and OMIM/Orphanet identifiers were recovered (artifact above). (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, wooderchakdonahue2018expandingtheclinical pages 1-2, revencu2020rasa1mosaicmutations pages 1-2)

### Synonyms and alternative names
Commonly used synonyms include **CM‑AVM**, **CMAVM**, **capillary malformation–AVM syndrome**, and genetic subtypes **CM‑AVM1 (RASA1)** and **CM‑AVM2 (EPHB4)**. (brix2022capillarymalformationarteriovenousmalformation pages 1-2, wooderchakdonahue2018expandingtheclinical pages 1-2, zhao2023mutationofkey pages 1-2)

### Evidence source type
Most knowledge about CM‑AVM comes from **aggregated disease‑level resources** (systematic reviews and cohorts) plus **case series** and **family studies**; some mechanistic understanding derives from **mouse and zebrafish models** and **endothelial cell studies**. (palermo2025capillarymalformation–arteriovenousmalformation pages 2-4, zhao2023mutationofkey pages 1-2, zhao2023geneticdysregulationof pages 35-39)

---

## 2. Etiology

### Disease causal factors
CM‑AVM is primarily a **Mendelian genetic disorder** caused by pathogenic variants in **RASA1** (CM‑AVM1) and **EPHB4** (CM‑AVM2), which disrupt endothelial signaling that normally restrains **RAS‑MAPK/ERK** activity. (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, chen2023ephb4rasa1mediatednegativeregulation pages 2-4, morin2025vascularmalformationsfrom pages 5-6)

### Risk factors
* **Genetic:** Heterozygous pathogenic variants in **RASA1** or **EPHB4**; de novo variants occur (e.g., ~26.5% likely de novo in a large RASA1 cohort). (revencu2013rasa1mutationsand pages 7-9)
* **Somatic/mosaic contributions:** Low‑level **post‑zygotic mosaic RASA1** variants can cause classical CM‑AVM; mosaic allele fractions as low as a few percent were detected, and gonosomal mosaicism can confer recurrence risk. (revencu2020rasa1mosaicmutations pages 1-2)

### Protective factors
No disease‑specific protective genetic or environmental factors were identified in the retrieved sources.

### Gene–environment interactions
No specific gene–environment interactions were identified in the retrieved sources.

---

## 3. Phenotypes

### Core phenotype spectrum with HPO suggestions
| Clinical feature | Description | Typical onset/course | Frequency/quant data | Suggested HPO term(s) |
|---|---|---|---|---|
| Multifocal capillary malformations (CMs) | Small round-to-oval pink-red to violaceous capillary malformations, often multifocal and sometimes with surrounding pale halo/white halo; hallmark cutaneous finding of CM-AVM | Usually congenital or early childhood; chronic, often stable in number/appearance but variable expressivity | RASA1 cohort: 306/314 (97%) had CMs; EPHB4 review: multiple CMs in 114/127 (89.8%), solitary CM in 12/127 (9.4%); ARUP RASA1 series: 75.4% had CMs (revencu2013rasa1mutationsand pages 1-2, wooderchakdonahue2018expandingtheclinical pages 1-2, brix2022capillarymalformationarteriovenousmalformation pages 1-2, revencu2013rasa1mutationsand pages 7-9) | Capillary malformation [HP:0001052]; Multiple capillary malformations [HP:0200049] |
| Pale halo / white halo around skin lesions | Perilesional pale halo or white halo surrounding CMs; may reflect microshunting and is diagnostically suggestive | Present from infancy/childhood; usually persistent | Reported as characteristic in RASA1- and EPHB4-related disease; proposed as diagnostic clue though precise pooled prevalence not established in the provided evidence (brix2022capillarymalformationarteriovenousmalformation pages 1-2, wooderchakdonahue2018expandingtheclinical pages 1-2, revencu2020rasa1mosaicmutations pages 1-2, brix2022capillarymalformationarteriovenousmalformation pages 4-5) | Halo nevus-like lesion / Perilesional pallor [suggested HPO mapping: Abnormality of skin color around lesion, no exact term confirmed] |
| Fast-flow vascular malformation (AVM/AVF spectrum) | Arteriovenous malformations and arteriovenous fistulas affecting skin, muscle, bone, brain, spine, and other sites; major source of morbidity | Congenital/developmental; may present in childhood or later when symptomatic; can progress or decompensate hemodynamically | Revencu 2013: 75/314 (23%) had AVM/AVF; Wooderchak-Donahue 2018: ~30% historically, 44.9% in the ARUP referred series; EPHB4 review: 23/127 (18.1%) had AVM/AVF (revencu2013rasa1mutationsand pages 1-2, wooderchakdonahue2018expandingtheclinical pages 1-2, brix2022capillarymalformationarteriovenousmalformation pages 1-2, revencu2013rasa1mutationsand pages 7-9) | Arteriovenous malformation [HP:0100026]; Arteriovenous fistula [HP:0012404] |
| Intracranial / cerebrovascular fast-flow lesions | Brain vascular lesions including pial AVFs, parenchymal AVMs, and vein-of-Galen malformations; important screening target | Often congenital or pediatric onset; may be asymptomatic or present acutely with neurologic/hemodynamic complications | Palermo 2025 pooled 148 genetically confirmed patients: pial AVF 63/148 (43.3%), AVM 54/148 (36.0%), vein-of-Galen malformation 26/148 (17.3%); Revencu 2013: 32/314 (10%) had intracranial lesions (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, palermo2025capillarymalformation–arteriovenousmalformation pages 2-4, revencu2013rasa1mutationsand pages 1-2) | Cerebral arteriovenous malformation [HP:0002409]; Intracranial arteriovenous fistula [suggested HPO mapping]; Vein of Galen malformation [suggested HPO mapping] |
| Spinal arteriovenous lesions | Intraspinal AVM/AVF causing neurologic risk | Congenital/developmental; may present in childhood with neurologic deficits or pain | Revencu 2013 included intraspinal AVM/AVF within fast-flow spectrum; Brix 2022 review noted 2/127 (1.6%) spinal AVMs among EPHB4 cases (revencu2013rasa1mutationsand pages 7-9, brix2022capillarymalformationarteriovenousmalformation pages 4-5) | Spinal arteriovenous malformation [suggested HPO mapping]; Abnormality of the spinal vasculature [suggested HPO mapping] |
| Vein of Galen aneurysmal malformation (VGAM/VGaM) | Distinct high-flow cerebral shunt phenotype particularly enriched in EPHB4-related disease | Prenatal, neonatal, or infancy presentation common; may cause heart failure/hydrocephalus | Palermo 2025: 26/148 (17.3%) overall; Tas 2022: among VGAM (n=64), 9 EPHB4 and 2 RASA1 cases; Brix 2022 EPHB4 review: 3/127 (2.4%) VGaM (palermo2025capillarymalformation–arteriovenousmalformation pages 2-4, tas2022arteriovenouscerebralhigh pages 3-4, brix2022capillarymalformationarteriovenousmalformation pages 4-5) | Vein of Galen malformation [suggested HPO mapping]; Cerebral arteriovenous malformation [HP:0002409] |
| Parkes Weber syndrome / limb overgrowth with AV shunting | Combined capillary malformation, soft-tissue/bony hypertrophy, and AV microfistulas/high-flow shunting in an extremity | Usually congenital/childhood; may progress with growth and hemodynamic burden | Revencu 2013: 26/314 (8%) had Parkes Weber syndrome; characteristic within RASA1 spectrum (revencu2013rasa1mutationsand pages 1-2, revencu2020rasa1mosaicmutations pages 1-2, revencu2013rasa1mutationsand pages 7-9) | Hemihyperplasia [HP:0003074]; Limb overgrowth [HP:0001537]; Arteriovenous fistula [HP:0012404] |
| Telangiectasia | Punctate or macular telangiectatic lesions, often contributing to HHT-like appearance | Childhood to adulthood; persistent | EPHB4 literature review: 28/127 (22.0%) had telangiectasia; Wooderchak-Donahue reported telangiectatic dermal lesions in 11 individuals with pathogenic RASA1 variants (brix2022capillarymalformationarteriovenousmalformation pages 1-2, brix2022capillarymalformationarteriovenousmalformation pages 2-4, wooderchakdonahue2018expandingtheclinical pages 10-11) | Telangiectasia [HP:0001009] |
| Bier spots | Irregular pale macules/spots, especially reported in EPHB4-related CM-AVM2 | Often childhood/adolescence; may persist | EPHB4 literature review: 20/127 (15.7%) with Bier spots (brix2022capillarymalformationarteriovenousmalformation pages 1-2, brix2022capillarymalformationarteriovenousmalformation pages 4-5) | Bier spots [HP:0025548] |
| Epistaxis / recurrent nosebleeds | Recurrent epistaxis can occur, particularly in EPHB4-related disease, creating overlap with HHT | Variable onset, often later childhood/adulthood; episodic | Reported in at least 9 CM-AVM2 cases in Brix review; frequency incompletely reported across studies (brix2022capillarymalformationarteriovenousmalformation pages 1-2, brix2022capillarymalformationarteriovenousmalformation pages 2-4, brix2022capillarymalformationarteriovenousmalformation pages 4-5, palermo2025capillarymalformation–arteriovenousmalformation pages 11-13) | Epistaxis [HP:0000421] |
| Heart failure from high-flow shunt | Congestive heart failure due to significant AV shunting, especially neonatal cerebral or thoracoabdominal lesions | Prenatal/neonatal or infantile in severe cases; potentially life-threatening | Highlighted in prenatal RASA1 series and AVM literature as major complication; prenatal-onset cases included congestive heart failure among key warning signs (coccia2023prenatalclinicalfindings pages 9-11, wooderchakdonahue2018expandingtheclinical pages 1-2, palermo2025capillarymalformation–arteriovenousmalformation pages 11-13) | Congestive heart failure [HP:0001635] |
| Neurologic complications | Hemorrhage, seizures, hydrocephalus, neurologic injury, or brain/spinal dysfunction from CNS vascular malformations | Childhood to adulthood; may be acute if hemorrhage occurs | Wooderchak-Donahue notes AVMs/AVFs can cause hemorrhage and neurologic injury; Palermo review emphasizes severe neurologic complications if lesions are undetected (wooderchakdonahue2018expandingtheclinical pages 1-2, palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, palermo2025capillarymalformation–arteriovenousmalformation pages 11-13) | Seizure [HP:0001250]; Intracranial hemorrhage [HP:0002170]; Hydrocephalus [HP:0000238]; Abnormal nervous system physiology [suggested HPO mapping] |
| Prenatal hydrops / non-immune hydrops fetalis | Severe prenatal manifestation of RASA1-related CM-AVM, likely reflecting occult high-flow lesions or lymphatic/hemodynamic compromise | Prenatal onset; severe, sometimes fatal | Coccia 2023 notes only 21 prenatal-onset cases had been reported; death occurred in 6/21 (30%); key prenatal signs include non-immune hydrops fetalis and polyhydramnios (coccia2023prenatalclinicalfindings pages 9-11) | Nonimmune hydrops fetalis [HP:0001790]; Fetal hydrops [HP:0001789] |
| Polyhydramnios | Excess amniotic fluid in prenatal-onset CM-AVM | Prenatal onset; may signal severe fetal disease | Reported among prenatal warning signs in RASA1-related CM-AVM; included among 21 published prenatal-onset cases reviewed by Coccia et al. (coccia2023prenatalclinicalfindings pages 9-11) | Polyhydramnios [HP:0001561] |
| Pleural effusion / chylothorax | Prenatal or neonatal thoracic fluid accumulation reported in severe prenatal cases | Prenatal or neonatal onset; can contribute to respiratory compromise | Coccia 2023 specifically lists pleural effusion and chylothorax among prenatal manifestations (coccia2023prenatalclinicalfindings pages 9-11) | Pleural effusion [HP:0002202]; Chylothorax [HP:0010310] |
| Multifocal neurovascular malformations in children with syndromic clue lesions | In pediatric neurovascular cohorts, the presence of multiple cutaneous capillary malformations increases suspicion for CM-AVM | Usually recognized in childhood; supports syndromic diagnosis and surveillance | Engel 2023 found having ≥2 capillary malformations strongly associated with definite CM-AVM; genetic diagnoses included RASA1 and EPHB4 variants (engel2023prevalenceandpredictors pages 13-17) | Multiple capillary malformations [HP:0200049]; Vascular malformation [HP:0005297] |


*Table: This table summarizes the core clinical phenotype spectrum of capillary malformation–arteriovenous malformation syndrome, including quantitative frequencies where available and suggested HPO mappings. It is useful for disease knowledge-base curation, phenotype annotation, and genotype-phenotype interpretation.*

### High‑value quantitative phenotype statistics (recent aggregated sources)
* In a 2025 systematic review of **148 genetically confirmed** CM‑AVM patients with cerebrovascular manifestations, pooled lesion frequencies were: **pial AVF 43.3% (63/148)**, **AVM 36.0% (54/148)**, **vein of Galen malformation 17.3% (26/148)**; nearly **24.7%** underwent endovascular embolization and **5.3%** underwent surgery. (Palermo et al., 2025‑12; https://doi.org/10.1007/s00381-025-07089-5) (palermo2025capillarymalformation–arteriovenousmalformation pages 2-4, palermo2025capillarymalformation–arteriovenousmalformation pages 7-9)
* For CM‑AVM2 (EPHB4) across a 2022 literature review of **127 EPHB4‑confirmed** patients: **multiple CMs 89.8%**, **AVM/AVF 18.1%**, **telangiectasia 22%**, **Bier spots 15.7%**, and **CNS fast‑flow lesions 3.9%** (including vein‑of‑Galen malformations and spinal AVMs). (Brix et al., 2022‑03; https://doi.org/10.2340/actadv.v102.1126) (brix2022capillarymalformationarteriovenousmalformation pages 1-2, brix2022capillarymalformationarteriovenousmalformation pages 4-5)
* For RASA1 CM‑AVM across combined cohorts: **capillary malformations in 97%**, **AVM/AVF in 23%**, **intracranial lesions in 10%**, and **Parkes Weber syndrome in 8%**. (Revencu et al., 2013‑12; https://doi.org/10.1002/humu.22431) (revencu2013rasa1mutationsand pages 1-2)

### Prenatal/neonatal manifestations (recent, 2023)
Coccia et al. (Genes, 2023‑02; https://doi.org/10.3390/genes14030549) emphasize that prenatal presentations exist and can be severe. Their abstract states: “**Pathogenic variants in RASA1 are typically associated with a clinical condition called ‘capillary malformation‑arteriovenous malformation’ (CM‑AVM) syndrome, an autosomal dominant genetic disease characterized by a broad phenotypic variability, even within families.**” (coccia2023prenatalclinicalfindings pages 9-11)

In the same abstract: “**Although CM‑AVM syndrome has been widely described in the literature, only 21 cases with prenatal onset of clinical features have been reported thus far.**” and prenatal warning signs include hydrops‑type presentations; mortality among reported prenatal‑onset cases was **~30% (6/21)**. (coccia2023prenatalclinicalfindings pages 9-11)

---

## 4. Genetic / Molecular Information

### Causal genes
* **RASA1** (RAS p21 protein activator 1) — CM‑AVM1 (OMIM 608354). (wooderchakdonahue2018expandingtheclinical pages 1-2, revencu2020rasa1mosaicmutations pages 1-2)
* **EPHB4** (EPH receptor B4) — CM‑AVM2 (OMIM 618196). (zhao2023mutationofkey pages 1-2)

### Variant types, mosaicism, and “second hit” concept
| Subtype | Causal gene | Variant class (typical) | Inheritance | Key pathway/mechanism | Evidence highlights (include at least one quantitative/stat statement where available) | Key citations (PMID if available in text; otherwise DOI) |
|---|---|---|---|---|---|---|
| CM-AVM1 | **RASA1** | Predominantly loss-of-function; truncating/nonsense, frameshift, splice-site; multi-exon deletions also reported; mosaic variants can occur | Autosomal dominant with high penetrance and variable expressivity; de novo and mosaic cases documented | RASA1 encodes p120 RasGAP, a negative regulator of **RAS-MAPK/ERK** signaling in endothelial cells; lesion formation is supported by a **second-hit** model in at least some vascular beds | In a 68-family cohort, **306/314 (97%)** had capillary malformations, **75/314 (23%)** had AVM/AVF, **32/314 (10%)** had intracranial lesions, and **26/314 (8%)** had Parkes Weber syndrome; penetrance reported as **98.5%** and ~**26.5%** of mutations were likely de novo (revencu2013rasa1mutationsand pages 1-2, revencu2013rasa1mutationsand pages 7-9) | Revencu 2013, *Human Mutation*, DOI: https://doi.org/10.1002/humu.22431 |
| CM-AVM1 with mosaicism | **RASA1** | Low-level postzygotic mosaic loss-of-function variants, including nonsense/truncating alleles; occasional lesion-specific second hits | Mosaic; can include gonosomal/germline transmission risk | Mosaic loss of endothelial RASA1 can produce classical CM-AVM; supports germline-or-mosaic susceptibility plus local second-hit pathogenesis | Four distinct mosaic RASA1 variants were detected with allele fractions ranging from **3% to 25%** overall; one patient also had a somatic second hit, and one mosaic proband had **3 affected children**, showing reproductive risk (revencu2020rasa1mosaicmutations pages 1-2) | Revencu 2020, *Journal of Medical Genetics*, DOI: https://doi.org/10.1136/jmedgenet-2019-106024 |
| RASA1-related CM-AVM spectrum | **RASA1** | Function-affecting variants of diverse classes, including nonsense/frameshift/splice and large deletions/duplications | Autosomal dominant; familial and sporadic cases | Loss of RASA1 activity disrupts endothelial Ras restraint and promotes fast-flow malformations; somatic second-hit events in lesions further support focal disease biology | In an ARUP series of **69 unrelated cases**, **60** had deleterious RASA1 variants, **29** of them novel; **5** large deletions gave a deletion/duplication rate of **8.3%**; **75.4%** had capillary malformations and **44.9%** had AVM/AVF (wooderchakdonahue2018expandingtheclinical pages 1-2, wooderchakdonahue2018expandingtheclinical pages 10-11) | Wooderchak-Donahue 2018, *Eur J Hum Genet*, DOI: https://doi.org/10.1038/s41431-018-0196-1 |
| CM-AVM2 | **EPHB4** | Germline loss-of-function variants are typical; kinase-domain damaging variants also implicated in cerebrovascular disease | Autosomal dominant with incomplete/variable expressivity | **EPHB4** acts upstream of **RASA1** to suppress endothelial **RAS-MAPK** signaling and regulate venous identity, endothelial sorting, and arteriovenous patterning | Recent pooled cerebrovascular review found **21/148 (14.0%)** genetically confirmed CM-AVM cases carried **EPHB4** variants; compared with RASA1, EPHB4 cases showed a narrower cerebrovascular phenotype and were more often linked to vein-of-Galen malformations (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, palermo2025capillarymalformation–arteriovenousmalformation pages 2-4) | Palermo 2025, *Child's Nervous System*, DOI: https://doi.org/10.1007/s00381-025-07089-5 |
| CM-AVM1/2 shared mechanism | **RASA1 / EPHB4** | Germline loss-of-function; mosaic/postzygotic events also reported in vascular malformations | Usually autosomal dominant for syndromic disease | **EPHB4→RASA1→RAS inactivation**: EPHB4 signaling restrains endothelial Ras-MAPK activity via RASA1-dependent mechanisms; failure perturbs angiogenic remodeling and AV specification | Morin summarizes CM-AVM as caused by germline **RASA1** or **EPHB4** loss-of-function and places both genes in the endothelial RAS regulatory module; the review also notes that such variants can occur as **mosaic events** in sporadic vascular malformations (morin2025vascularmalformationsfrom pages 5-6) | Morin 2025, *EMBO Mol Med*, DOI: https://doi.org/10.1038/s44321-025-00344-x |
| Endothelial signaling module underlying CM-AVM | **EPHB4-RASA1 axis** | Functional disruption of receptor-effector signaling; disease-causing missense or loss-of-function changes can converge on failed Ras suppression | Mechanism relevant to inherited and mosaic disease | EPHB4 normally recruits/activates RASA1-linked Ras suppression in endothelial cells; loss causes excess **ERK/MAPK** activity, impaired collagen IV export, abnormal angiogenesis, and defective arterial-capillary-venous remodeling | Mechanistic review states **RASA1 mutations account for ~70%** of CM-AVM and **EPHB4 ~30%**; constitutive mouse deficiency of either gene causes embryonic lethality around **E10.5** with failure of primitive plexus remodeling into hierarchical arterial-capillary-venous networks (chen2023ephb4rasa1mediatednegativeregulation pages 2-4, chen2023ephb4rasa1mediatednegativeregulation pages 7-9, chen2023ephb4rasa1mediatednegativeregulation pages 6-7) | Chen/van der Ent/King 2023 mechanistic review, DOI: 10.1101/2023.03.18.532837 (preprint-related mechanistic source as available in context) |
| Cerebrovascular/high-flow subtype enrichment | **RASA1 predominantly; EPHB4 enriched in VGAM** | Heterozygous damaging germline variants | Autosomal dominant susceptibility for syndromic cases | Developing endothelial cells are the likely spatiotemporal locus; genotype influences shunt subtype | In children with cerebral high-flow shunts, **RASA1** variants were found in **25%** overall and across all shunt types, whereas **EPHB4** variants were found in **8%** overall and were **specific to true VGAM** in that cohort; among **VGAM (n=64)** there were **9 EPHB4** vs **2 RASA1** cases (tas2022arteriovenouscerebralhigh pages 3-4) | Tas 2022, *Front Pediatr*, DOI: https://doi.org/10.3389/fped.2022.871565 |
| Human genetics plus animal-model evidence for cerebrovascular CM-AVM biology | **RASA1 / EPHB4** | De novo RASA1 loss-of-function; damaging transmitted EPHB4 variants; EPHB4 kinase-domain variant model | Germline susceptibility with evidence for additional-hit requirement in some models | Integrated human genetics and model systems support an endothelial **RAS signaling network** controlling developmental angiogenesis and AV network hierarchy | Nature Communications 2023 identified a genome-wide significant burden of **de novo RASA1 loss-of-function** variants (**2042.5-fold, p=4.79×10⁻⁷**) and **17.5-fold** enrichment of damaging transmitted **EPHB4** variants (**p=1.22×10⁻⁵**); an EPHB4 **Phe867Leu** mouse model showed disrupted angiogenesis **only with a second-hit allele** (zhao2023mutationofkey pages 1-2, zhao2023geneticdysregulationof pages 12-14) | Zhao 2023, *Nature Communications*, DOI: https://doi.org/10.1038/s41467-023-43062-z |
| Arteriovenous specification relevance to EPHB4 disease | **EPHB4** | Endothelial Ephb4 loss in model systems | Experimental conditional endothelial loss | Eph/ephrin signaling couples endothelial cell sorting, arterial specification, and AV patterning; provides mechanistic rationale for EPHB4-related vascular malformations | In inducible mouse retina models, postnatal **Ephb4** inactivation increased incorporation of mutant endothelial cells into arteries and produced **more arterial branches** and increased arterial extension, linking EPHB4 deficiency to abnormal AV patterning (stewen2024ephephrinsignalingcouples pages 1-2) | Stewen 2024, *Nature Communications*, DOI: https://doi.org/10.1038/s41467-024-46300-0 |
| Aggregate cerebrovascular CM-AVM phenotype across genes | **RASA1 / EPHB4** | Genetically confirmed pathogenic variants | Mostly autosomal dominant syndromic disease | Shared fast-flow predisposition, but genotype influences lesion spectrum; screening is justified because lesions are clinically important and often treatable | In a systematic review of **148** genetically confirmed CM-AVM patients, cerebrovascular lesions included **pial AVF 43.3% (63/148)**, **AVM 36.0% (54/148)**, and **vein-of-Galen malformation 17.3% (26/148)**; **24.7%** underwent endovascular embolization and **5.3%** surgery (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, palermo2025capillarymalformation–arteriovenousmalformation pages 2-4) | Palermo 2025, *Child's Nervous System*, DOI: https://doi.org/10.1007/s00381-025-07089-5 |


*Table: This table summarizes the main genetic subtypes and mechanisms underlying capillary malformation–arteriovenous malformation syndrome, focusing on RASA1 and EPHB4. It integrates cohort data, mosaic/second-hit evidence, and recent mechanistic studies to support genotype-to-pathway interpretation.*

Key primary‑literature findings:
* **High penetrance and de novo events:** Revencu et al. report penetrance ~**98.5%** and **~26.5% de novo** RASA1 variants in their cohort; they also report strong variability and support for second‑hit biology. (revencu2013rasa1mutationsand pages 7-9)
* **Mosaicism:** Revencu et al. (J Med Genet, 2020‑07) report mosaic RASA1 allele fractions in blood/tissue and conclude: “**This study shows that RASA1 mosaic mutations can cause capillary malformation‑arteriovenous malformation.**” (https://doi.org/10.1136/jmedgenet-2019-106024) (revencu2020rasa1mosaicmutations pages 1-2)
* **Human genetics + systems biology (2023):** Zhao et al. (Nat Commun, 2023‑11; https://doi.org/10.1038/s41467-023-43062-z) found a genome‑wide significant burden of **de novo loss‑of‑function RASA1** and enrichment of damaging **EPHB4** variants in vein‑of‑Galen malformations, and used endothelial‑focused analyses and animal models to localize mechanism to **developing endothelial cells**. (zhao2023mutationofkey pages 1-2)

### Allele frequency in population databases
Specific gnomAD allele frequencies for CM‑AVM pathogenic variants were not available in the retrieved excerpts.

### Modifier genes / epigenetics / chromosomal abnormalities
No definitive modifier genes, epigenetic signatures specific to CM‑AVM, or recurrent chromosomal abnormalities were identified in the retrieved CM‑AVM‑focused evidence.

---

## 5. Environmental Information
No specific non‑genetic environmental, lifestyle, or infectious causal contributors were identified in the retrieved sources; CM‑AVM is predominantly a genetic developmental vascular disorder in the available literature. (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, revencu2013rasa1mutationsand pages 1-2)

---

## 6. Mechanism / Pathophysiology

### Upstream → downstream causal chain (current model)
1. **Germline heterozygous loss‑of‑function** in **RASA1** or **EPHB4** establishes a susceptibility state in endothelial development. (morin2025vascularmalformationsfrom pages 5-6)
2. In some lesions, additional **mosaic/second‑hit** events or focal endothelial dysfunction further reduce pathway restraint, resulting in localized malformations (multifocality). (revencu2020rasa1mosaicmutations pages 1-2, revencu2013rasa1mutationsand pages 7-9)
3. Loss of EPHB4–RASA1 negative regulation increases **RAS‑MAPK/ERK signaling**, altering angiogenic remodeling, endothelial survival/ECM handling, and arteriovenous specification, producing fast‑flow shunts (AVMs/AVFs) and related lesions. (chen2023ephb4rasa1mediatednegativeregulation pages 2-4, zhao2023geneticdysregulationof pages 12-14)

### Key pathways
* **RAS‑MAPK/ERK signaling**: CM‑AVM is described as resulting from RASA1/EPHB4 mutations “**leading to aberrant Ras‑MAPK signaling**.” (Palermo et al., 2025‑12) (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2)
* **EPHB4–RASA1 axis as Ras restraint in endothelium:** experimental work reviewed in 2023 indicates EPHB4 inhibits endothelial Ras‑MAPK via a RASA1‑dependent mechanism and that disruption affects vascular remodeling and extracellular matrix handling (collagen IV export). (chen2023ephb4rasa1mediatednegativeregulation pages 2-4, chen2023ephb4rasa1mediatednegativeregulation pages 7-9)

### Cell types (CL term suggestions)
* **Endothelial cell** (CL:0000115) — primary implicated cell type; single‑cell integration in Zhao et al. localizes disease to developing endothelial cells. (zhao2023mutationofkey pages 1-2, zhao2023geneticdysregulationof pages 12-14)
* **Venous endothelial cell** (suggested; EphB4 is a venous EC marker) and **tip cell progeny** in retinal angiogenesis models. (stewen2024ephephrinsignalingcouples pages 1-2)

### GO biological process term suggestions
* **angiogenesis** (GO:0001525)
* **blood vessel morphogenesis** (GO:0048514)
* **artery development / arteriovenous specification** (suggested mapping; supported by EphB4/ephrin signaling models) (stewen2024ephephrinsignalingcouples pages 1-2)
* **negative regulation of Ras protein signal transduction** (GO:0046579) (supported conceptually by RASA1 function) (chen2023ephb4rasa1mediatednegativeregulation pages 2-4)

### Anatomical loci and tissue damage mechanisms
Mechanistic and clinical data highlight cerebrovascular and cutaneous vascular beds; severe lesions can cause heart failure, hemorrhage, and neurologic injury. (palermo2025capillarymalformation–arteriovenousmalformation pages 11-13, wooderchakdonahue2018expandingtheclinical pages 1-2)

---

## 7. Anatomical Structures Affected

### Organ/system level (UBERON suggestions)
* **Skin** (UBERON:0002097): multifocal capillary malformations. (brix2022capillarymalformationarteriovenousmalformation pages 1-2, revencu2013rasa1mutationsand pages 1-2)
* **Brain / intracranial vasculature** (UBERON:0000955; cerebrovasculature): pial AVF, AVM, vein‑of‑Galen malformations. (palermo2025capillarymalformation–arteriovenousmalformation pages 2-4)
* **Spinal cord / spinal vasculature** (UBERON:0002240): spinal AVMs reported. (brix2022capillarymalformationarteriovenousmalformation pages 4-5)
* **Extremities (limb)** (UBERON:0002101): Parkes Weber syndrome (overgrowth + AV shunting). (revencu2013rasa1mutationsand pages 1-2)

### Subcellular/localization notes
No CM‑AVM‑specific subcellular compartment pathology was explicitly described in the retrieved excerpts.

---

## 8. Temporal Development

### Onset
* Cutaneous lesions are often **present at birth or in early childhood**. (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, brix2022capillarymalformationarteriovenousmalformation pages 1-2)
* Severe **prenatal** presentations exist (hydrops‑type findings, polyhydramnios). (coccia2023prenatalclinicalfindings pages 9-11)

### Progression/course
Course is variable; morbidity is driven by high‑flow lesion location and hemodynamic effects. There is no uniform staging system described in the retrieved sources.

---

## 9. Inheritance and Population

### Inheritance pattern
CM‑AVM is **autosomal dominant** with high but not necessarily complete penetrance and **variable expressivity**. (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, brix2022capillarymalformationarteriovenousmalformation pages 1-2, revencu2013rasa1mutationsand pages 7-9)

### Penetrance/expressivity
* RASA1 cohort penetrance reported as **98.5%** with substantial intra‑ and interfamilial variability. (revencu2013rasa1mutationsand pages 7-9)
* Mosaic cases can transmit to offspring (germline involvement). (revencu2020rasa1mosaicmutations pages 1-2)

### Epidemiology
Reliable prevalence/incidence estimates were not present in the retrieved excerpts; the condition is consistently described as **rare**. (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2)

---

## 10. Diagnostics

### Clinical suspicion
Suspicion is raised by **multiple small capillary malformations**, especially with **pale halos**, and by personal/family history of fast‑flow lesions. (brix2022capillarymalformationarteriovenousmalformation pages 1-2, wooderchakdonahue2018expandingtheclinical pages 1-2)

### Genetic testing (real‑world implementation)
* **RASA1 and EPHB4** are central diagnostic genes and are commonly included in **NGS vascular anomaly panels**. (palermo2025capillarymalformation–arteriovenousmalformation pages 11-13, revencu2020rasa1mosaicmutations pages 1-2)
* High‑depth sequencing may be needed when blood testing is negative, as **mosaicism** can explain apparently sporadic presentations; Revencu et al. recommend highly sensitive sequencing approaches in such settings. (revencu2020rasa1mosaicmutations pages 1-2)
* Copy‑number analysis matters for RASA1: a clinical series found **multi‑exon deletions (8.3%)** among function‑affecting RASA1 variants, supporting deletion/duplication testing in workflows. (wooderchakdonahue2018expandingtheclinical pages 10-11)

### Imaging and screening/surveillance
* CM‑AVM can be confused with HHT; **genetic testing and cerebrovascular screening** are emphasized to prevent missed intracranial lesions. (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, palermo2025capillarymalformation–arteriovenousmalformation pages 13-14)
* Palermo et al. stress that “regular imaging and clinical evaluation” are key for early lesion detection and to prevent severe neurologic complications. (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2)
* A pediatric neurovascular cohort noted lack of consensus on intervals; their clinical approach was **brain and spine imaging at diagnosis**, with repeat imaging before puberty and after puberty depending on circumstances. (engel2023prevalenceandpredictors pages 13-17)

### Differential diagnosis
Important differentials include:
* **Hereditary hemorrhagic telangiectasia (HHT)** (ENG/ACVRL1/SMAD4/GDF2), because epistaxis/telangiectasia can occur in CM‑AVM2 and some RASA1 cases, causing misclassification. (brix2022capillarymalformationarteriovenousmalformation pages 2-4, palermo2025capillarymalformation–arteriovenousmalformation pages 11-13)
* **Sturge–Weber syndrome** and **Klippel–Trenaunay syndrome** in the dermatologic differential of capillary malformations. (brix2022capillarymalformationarteriovenousmalformation pages 2-4)

---

## 11. Outcome / Prognosis

### Morbidity
Morbidity is driven by fast‑flow shunts (CNS/spine/face/extremity) with risks including hemorrhage, seizures, and high‑output cardiac failure. (wooderchakdonahue2018expandingtheclinical pages 1-2, palermo2025capillarymalformation–arteriovenousmalformation pages 11-13)

### Outcome statistics
* In prenatal‑onset RASA1 CM‑AVM cases reviewed by Coccia et al., **death occurred in 30% (6/21)**; however, they note “generally a good long‑term prognosis” overall while warning that unrecognized deep malformations can be fatal. (coccia2023prenatalclinicalfindings pages 9-11)
* In the cerebrovascular systematic review cohort, **~25%** required embolization and **~5%** surgery, indicating clinically significant lesion burden in screened/ascertained cases. (palermo2025capillarymalformation–arteriovenousmalformation pages 7-9)

---

## 12. Treatment

### Standard and interventional management (current practice)
CM‑AVM management is typically **multidisciplinary** and focused on detection and treatment of **treatable high‑flow lesions** (endovascular embolization and sometimes surgery). (palermo2025capillarymalformation–arteriovenousmalformation pages 11-13, palermo2025capillarymalformation–arteriovenousmalformation pages 7-9)

**MAXO suggestions** (non‑exhaustive):
* Endovascular embolization (MAXO term suggestion: endovascular embolization procedure)
* Surgical resection of vascular malformation (MAXO suggestion: surgical excision)
* Genetic counseling (MAXO suggestion: genetic counseling)
* Surveillance imaging (MAXO suggestion: diagnostic imaging procedure)

### Targeted/medical therapies (emerging; 2024+ reviews)
Recent vascular anomalies reviews emphasize the shift toward **theragnostic** targeted therapy, repurposing oncology/transplant drugs:
* Seront et al. (ASH Hematology, 2024‑12; https://doi.org/10.1182/hematology.2024000598) highlight MEK inhibition and mTOR inhibition as precision approaches in vascular malformations; they describe clinical benefit signals with trametinib in AVM cohorts and symptom control with sirolimus in some vascular anomalies contexts. (seront2024molecularlandscapeand pages 6-7)
* Morin et al. (EMBO Mol Med, 2025‑11; https://doi.org/10.1038/s44321-025-00344-x) explicitly lists **CM‑AVM (RASA1/EPHB4)** among syndromes and notes that MAPK inhibitors (e.g., **trametinib**) and mTOR/PI3K inhibitors (e.g., **sirolimus**, **alpelisib**) are being applied across vascular malformations with genotype–phenotype logic. (morin2025vascularmalformationsfrom pages 3-5, morin2025vascularmalformationsfrom pages 12-13)

### Clinical trials (real‑world implementations; ClinicalTrials.gov)
* **Trametinib for complicated extracranial AVM**: NCT04258046 (Stanford; Phase 2; status COMPLETED; start 2020‑12‑01; primary completion 2026‑02‑02). Inclusion requires complicated extracranial AVM; genetic testing for RAS/MAPK variants is preferred. Primary endpoint is disease response at month 6 using composite radiographic/clinical/functional/QoL criteria. https://clinicaltrials.gov/study/NCT04258046 (NCT04258046 chunk 1)
* **Trametinib for Ras/MAPK pathway vascular anomalies (VATCH)**: NCT07549646 (CHOP; Phase 2; ACTIVE_NOT_RECRUITING; ages 2 months–30 years). Primary endpoint uses an individualized composite response after 6 cycles (radiology + PROMIS PRO + clinical benefit). https://clinicaltrials.gov/study/NCT07549646 (NCT07549646 chunk 1)
* **Trametinib for complicated vascular anomalies (pediatric)**: NCT07072403 (West China Hospital; Phase 1/2; ACTIVE_NOT_RECRUITING; ages 1–18). Objective response defined as ≥20% lesion volume reduction at month 12. https://clinicaltrials.gov/study/NCT07072403 (NCT07072403 chunk 1)
* **Sirolimus for severe AVMs**: NCT02042326 (Amiens; Phase 2; prospective evaluation of efficacy/safety in severe arteriovenous malformations). https://clinicaltrials.gov/study/NCT02042326 (morin2025vascularmalformationsfrom pages 6-7)

**Relevance to CM‑AVM specifically:** These trials generally enroll AVMs/vascular anomalies rather than CM‑AVM genetically defined cohorts; however, CM‑AVM lesions are mechanistically linked to RAS/MAPK dysregulation and therefore overlap with eligibility in Ras/MAPK‑targeted vascular anomaly trials. (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2, NCT04258046 chunk 1)

---

## 13. Prevention

### Primary prevention
No known primary prevention exists for inherited CM‑AVM aside from reproductive options.

### Secondary/tertiary prevention
* **Cascade testing and early detection**: Because of autosomal dominant inheritance and clinically significant occult lesions, genetic confirmation plus appropriate imaging surveillance is emphasized to prevent complications. (palermo2025capillarymalformation–arteriovenousmalformation pages 11-13, engel2023prevalenceandpredictors pages 13-17)
* **Prenatal considerations**: Coccia et al. stress careful interpretation of prenatal ultrasound signs and recommend genetic counseling and family evaluation because undiagnosed deep malformations can be fatal in newborns and relatives with the same variant. (coccia2023prenatalclinicalfindings pages 9-11)

---

## 14. Other Species / Natural Disease
No naturally occurring CM‑AVM syndrome in non‑human species was identified in the retrieved sources.

---

## 15. Model Organisms
Animal and experimental systems support causal biology:
* **Mouse (EPHB4 kinase-domain variant; two-hit requirement)**: Zhao et al. report that mice expressing an EPHB4 missense variant (Phe867Leu) show disrupted angiogenesis and impaired arterial–capillary–venous network development, with severe phenotypes requiring an additional “second‑hit” allele. (zhao2023geneticdysregulationof pages 12-14, zhao2023mutationofkey pages 1-2)
* **Mouse retinal angiogenesis (conditional Ephb4 inactivation)**: Eph/ephrin signaling experiments in retina show EphB4 influences endothelial sorting and arterial specification, supporting relevance to EPHB4‑related vascular malformations. (stewen2024ephephrinsignalingcouples pages 1-2)
* **Zebrafish ephb4 depletion**: zebrafish models show supernumerary arteriovenous connections and altered venous structures with ephb4 perturbation, consistent with disturbed arteriovenous patterning. (zhao2023geneticdysregulationof pages 35-39)

**Model limitations:** Most models address developmental angiogenesis and may not perfectly recapitulate focal post‑zygotic mosaic lesions typical of human CM‑AVM; mechanistic reviews explicitly note the need for models that more closely mimic somatic second hits. (chen2023ephb4rasa1mediatednegativeregulation pages 7-9)

---

# Recent Developments (2023–2024 prioritization)

1. **Integrated genetics + single‑cell approaches in cerebrovascular malformations (2023):** Zhao et al. (Nature Communications, 2023‑11) combined large-scale human exome analysis with cerebrovascular single-cell transcriptomics, implicating **RASA1** and **EPHB4** in a developing endothelial Ras signaling network relevant to vein-of-Galen malformations and, by extension, CM‑AVM biology. https://doi.org/10.1038/s41467-023-43062-z (zhao2023mutationofkey pages 1-2)
2. **Prenatal CM‑AVM characterization (2023):** Coccia et al. (Genes, 2023‑02) consolidate prenatal warning signs and stress the risk of fatal neonatal complications if deep malformations are missed. https://doi.org/10.3390/genes14030549 (coccia2023prenatalclinicalfindings pages 9-11)
3. **Precision medicine framing in vascular anomalies (2024):** Seront et al. (ASH Hematology, 2024‑12) emphasize genomic testing for vascular malformations and discuss targeted inhibitors (MEK, mTOR/PI3K) as an emerging management paradigm. https://doi.org/10.1182/hematology.2024000598 (seront2024molecularlandscapeand pages 1-3, seront2024molecularlandscapeand pages 6-7)
4. **Mechanistic arteriovenous specification biology (2024):** Stewen et al. (Nat Commun, 2024‑04) provide in vivo evidence that EphB4/ephrin signaling couples endothelial cell sorting and arterial specification, relevant to EPHB4‑driven CM‑AVM2. https://doi.org/10.1038/s41467-024-46300-0 (stewen2024ephephrinsignalingcouples pages 1-2)

---

# Key Gaps / Not Available in Retrieved Evidence
* ICD‑10/ICD‑11 codes and MeSH terms were not captured in the retrieved full texts in this run.
* Population prevalence/incidence estimates were not available from the retrieved sources.
* Variant‑level population allele frequencies (gnomAD) and ClinVar aggregation were not retrieved in the excerpts.



References

1. (palermo2025capillarymalformation–arteriovenousmalformation pages 1-2): Matteo Palermo, Alessandro Olivi, and Carmelo Lucio Sturiale. Capillary malformation–arteriovenous malformation syndrome (cm-avm): a systematic review of cerebrovascular manifestations. Child's Nervous System, Dec 2025. URL: https://doi.org/10.1007/s00381-025-07089-5, doi:10.1007/s00381-025-07089-5. This article has 0 citations.

2. (brix2022capillarymalformationarteriovenousmalformation pages 1-2): Anna Trier Heiberg Brix, Pernille Mathiesen Tørring, and Anette Bygum. Capillary malformation-arteriovenous malformation type 2: a case report and review. Acta Dermato-Venereologica, 102:adv00662, Mar 2022. URL: https://doi.org/10.2340/actadv.v102.1126, doi:10.2340/actadv.v102.1126. This article has 15 citations and is from a domain leading peer-reviewed journal.

3. (wooderchakdonahue2018expandingtheclinical pages 1-2): Whitney L. Wooderchak-Donahue, Peter Johnson, Jamie McDonald, Francine Blei, Alejandro Berenstein, Michelle Sorscher, Jennifer Mayer, Angela E. Scheuerle, Tracey Lewis, J. Fredrik Grimmer, Gresham T. Richter, Marcie A. Steeves, Angela E. Lin, David A. Stevenson, and Pinar Bayrak-Toydemir. Expanding the clinical and molecular findings in rasa1 capillary malformation-arteriovenous malformation. European Journal of Human Genetics, 26:1521-1536, Jun 2018. URL: https://doi.org/10.1038/s41431-018-0196-1, doi:10.1038/s41431-018-0196-1. This article has 79 citations and is from a domain leading peer-reviewed journal.

4. (revencu2020rasa1mosaicmutations pages 1-2): Nicole Revencu, Elodie Fastre, Marie Ravoet, Raphaël Helaers, Pascal Brouillard, Annouk Bisdorff-Bresson, Clara W T Chung, Marion Gerard, Veronika Dvorakova, Alan D Irvine, Laurence M Boon, and Miikka Vikkula. Rasa1 mosaic mutations in patients with capillary malformation-arteriovenous malformation. Journal of Medical Genetics, 57:48-52, Jul 2020. URL: https://doi.org/10.1136/jmedgenet-2019-106024, doi:10.1136/jmedgenet-2019-106024. This article has 79 citations and is from a domain leading peer-reviewed journal.

5. (zhao2023geneticdysregulationof pages 12-14): Shujuan Zhao, Kedous Y. Mekbib, Martijn A. van der Ent, Garrett Allington, Andrew Prendergast, Jocelyn E. Chau, Hannah Smith, John Shohfi, Jack Ocken, Daniel Duran, Charuta G. Furey, Hao Thi Le, Phan Q. Duy, Benjamin C. Reeves, Junhui Zhang, Carol Nelson-Williams, Di Chen, Boyang Li, Timothy Nottoli, Suxia Bai, Myron Rolle, Xue Zeng, Weilai Dong, Po-Ying Fu, Yung-Chun Wang, Shrikant Mane, Paulina Piwowarczyk, Katie Pricola Fehnel, Alfred Pokmeng See, Bermans J. Iskandar, Beverly Aagaard-Kienitz, Adam J. Kundishora, Tyrone DeSpenza, Ana B.W. Greenberg, Seblewengel M. Kidanemariam, Andrew T. Hale, James M. Johnston, Eric M. Jackson, Phillip B. Storm, Shih-Shan Lang, William E. Butler, Bob S. Carter, Paul Chapman, Christopher J. Stapleton, Aman B. Patel, Georges Rodesch, Stanislas Smajda, Alejandro Berenstein, Tanyeri Barak, E. Zeynep Erson-Omay, Hongyu Zhao, Andres Moreno-De-Luca, Mark R. Proctor, Edward R. Smith, Darren B. Orbach, Seth L. Alper, Stefania Nicoli, Titus J. Boggon, Richard P. Lifton, Murat Gunel, Philip D. King, Sheng Chih Jin, and Kristopher T. Kahle. Genetic dysregulation of an endothelial ras signaling network in vein of galen malformations. BioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.03.18.532837, doi:10.1101/2023.03.18.532837. This article has 3 citations.

6. (zhao2023mutationofkey pages 1-2): Shujuan Zhao, Kedous Y. Mekbib, Martijn A. van der Ent, Garrett Allington, Andrew Prendergast, Jocelyn E. Chau, Hannah Smith, John Shohfi, Jack Ocken, Daniel Duran, Charuta G. Furey, Le Thi Hao, Phan Q. Duy, Benjamin C. Reeves, Junhui Zhang, Carol Nelson-Williams, Di Chen, Boyang Li, Timothy Nottoli, Suxia Bai, Myron Rolle, Xue Zeng, Weilai Dong, Po-Ying Fu, Yung-Chun Wang, Shrikant Mane, Paulina Piwowarczyk, Katie Pricola Fehnel, Alfred Pokmeng See, Bermans J. Iskandar, Beverly Aagaard-Kienitz, Quentin J. Moyer, Evan Dennis, Emre Kiziltug, Adam J. Kundishora, Tyrone DeSpenza, Ana B. W. Greenberg, Seblewengel M. Kidanemariam, Andrew T. Hale, James M. Johnston, Eric M. Jackson, Phillip B. Storm, Shih-Shan Lang, William E. Butler, Bob S. Carter, Paul Chapman, Christopher J. Stapleton, Aman B. Patel, Georges Rodesch, Stanislas Smajda, Alejandro Berenstein, Tanyeri Barak, E. Zeynep Erson-Omay, Hongyu Zhao, Andres Moreno-De-Luca, Mark R. Proctor, Edward R. Smith, Darren B. Orbach, Seth L. Alper, Stefania Nicoli, Titus J. Boggon, Richard P. Lifton, Murat Gunel, Philip D. King, Sheng Chih Jin, and Kristopher T. Kahle. Mutation of key signaling regulators of cerebrovascular development in vein of galen malformations. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43062-z, doi:10.1038/s41467-023-43062-z. This article has 25 citations and is from a highest quality peer-reviewed journal.

7. (le2025arteriovenousmalformations(avms) pages 1-3): Nga Le, Yan Li, Gianni Walker, Bao-Ngoc Nguyen, Arash Bornak, Sapna Deo, Omaida Velazquez, and Zhao-Jun Liu. Arteriovenous malformations (avms): molecular pathogenesis, clinical features, and emerging therapeutic strategies. Biomolecules, Nov 2025. URL: https://doi.org/10.3390/biom15121661, doi:10.3390/biom15121661. This article has 4 citations.

8. (coccia2023prenatalclinicalfindings pages 9-11): Emanuele Coccia, Lara Valeri, Roberta Zuntini, Stefano Giuseppe Caraffi, Francesca Peluso, Luca Pagliai, Antonietta Vezzani, Zaira Pietrangiolillo, Francesco Leo, Nives Melli, Valentina Fiorini, Andrea Greco, Francesca Romana Lepri, Elisa Pisaneschi, Annabella Marozza, Diana Carli, Alessandro Mussa, Francesca Clementina Radio, Beatrice Conti, Maria Iascone, Giancarlo Gargano, Antonio Novelli, Marco Tartaglia, Orsetta Zuffardi, Maria Francesca Bedeschi, and Livia Garavelli. Prenatal clinical findings in rasa1-related capillary malformation-arteriovenous malformation syndrome. Genes, 14:549, Feb 2023. URL: https://doi.org/10.3390/genes14030549, doi:10.3390/genes14030549. This article has 14 citations.

9. (morin2025vascularmalformationsfrom pages 5-6): Gabriel Morin, Ilaria Galasso, and Guillaume Canaud. Vascular malformations: from genetics to therapeutics. EMBO Molecular Medicine, 18:1-21, Nov 2025. URL: https://doi.org/10.1038/s44321-025-00344-x, doi:10.1038/s44321-025-00344-x. This article has 4 citations and is from a highest quality peer-reviewed journal.

10. (lin2026chinesecapillarymalformationarteriovenous pages 7-9): Yan-yan Lin, Shuyan Dong, Changhua Zhu, Linxin Dong, Lihang Lin, and Xuemin Xiao. Chinese capillary malformation-arteriovenous malformation: clinical and genetic analysis of eight cases. Frontiers in Medicine, Mar 2026. URL: https://doi.org/10.3389/fmed.2026.1774495, doi:10.3389/fmed.2026.1774495. This article has 0 citations.

11. (palermo2025capillarymalformation–arteriovenousmalformation pages 2-4): Matteo Palermo, Alessandro Olivi, and Carmelo Lucio Sturiale. Capillary malformation–arteriovenous malformation syndrome (cm-avm): a systematic review of cerebrovascular manifestations. Child's Nervous System, Dec 2025. URL: https://doi.org/10.1007/s00381-025-07089-5, doi:10.1007/s00381-025-07089-5. This article has 0 citations.

12. (zhao2023geneticdysregulationof pages 35-39): Shujuan Zhao, Kedous Y. Mekbib, Martijn A. van der Ent, Garrett Allington, Andrew Prendergast, Jocelyn E. Chau, Hannah Smith, John Shohfi, Jack Ocken, Daniel Duran, Charuta G. Furey, Hao Thi Le, Phan Q. Duy, Benjamin C. Reeves, Junhui Zhang, Carol Nelson-Williams, Di Chen, Boyang Li, Timothy Nottoli, Suxia Bai, Myron Rolle, Xue Zeng, Weilai Dong, Po-Ying Fu, Yung-Chun Wang, Shrikant Mane, Paulina Piwowarczyk, Katie Pricola Fehnel, Alfred Pokmeng See, Bermans J. Iskandar, Beverly Aagaard-Kienitz, Adam J. Kundishora, Tyrone DeSpenza, Ana B.W. Greenberg, Seblewengel M. Kidanemariam, Andrew T. Hale, James M. Johnston, Eric M. Jackson, Phillip B. Storm, Shih-Shan Lang, William E. Butler, Bob S. Carter, Paul Chapman, Christopher J. Stapleton, Aman B. Patel, Georges Rodesch, Stanislas Smajda, Alejandro Berenstein, Tanyeri Barak, E. Zeynep Erson-Omay, Hongyu Zhao, Andres Moreno-De-Luca, Mark R. Proctor, Edward R. Smith, Darren B. Orbach, Seth L. Alper, Stefania Nicoli, Titus J. Boggon, Richard P. Lifton, Murat Gunel, Philip D. King, Sheng Chih Jin, and Kristopher T. Kahle. Genetic dysregulation of an endothelial ras signaling network in vein of galen malformations. BioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.03.18.532837, doi:10.1101/2023.03.18.532837. This article has 3 citations.

13. (chen2023ephb4rasa1mediatednegativeregulation pages 2-4): D Chen, MA Van der Ent, NL Lartey, and PD King. Ephb4-rasa1-mediated negative regulation of ras-mapk signaling in the vasculature: implications for the treatment of ephb4-and rasa1-related vascular …. Unknown journal, 2023.

14. (revencu2013rasa1mutationsand pages 7-9): Nicole Revencu, Laurence M. Boon, Antonella Mendola, Maria Rosa Cordisco, Josée Dubois, Philippe Clapuyt, Frank Hammer, David J. Amor, Alan D. Irvine, Eulalia Baselga, Anne Dompmartin, Samira Syed, Ana Martin-Santiago, Lesley Ades, Felicity Collins, Janine Smith, Sarah Sandaradura, Victoria R. Barrio, Patricia E. Burrows, Francine Blei, Mariarosaria Cozzolino, Nicola Brunetti-Pierri, Asuncion Vicente, Marc Abramowicz, Julie Désir, Catheline Vilain, Wendy K. Chung, Ashley Wilson, Carol A. Gardiner, Yim Dwight, David J.E. Lord, Leona Fishman, Cheryl Cytrynbaum, Sarah Chamlin, Fred Ghali, Yolanda Gilaberte, Shelagh Joss, Maria del C. Boente, Christine Léauté-Labrèze, Marie-Ange Delrue, Susan Bayliss, Loreto Martorell, Maria-Antonia González-Enseñat, Juliette Mazereeuw-Hautier, Brid O'Donnell, Didier Bessis, Reed E. Pyeritz, Aicha Salhi, Oon T. Tan, Orli Wargon, John B. Mulliken, and Miikka Vikkula. Rasa1 mutations and associated phenotypes in 68 families with capillary malformation–arteriovenous malformation. Human Mutation, 34:1632-1641, Dec 2013. URL: https://doi.org/10.1002/humu.22431, doi:10.1002/humu.22431. This article has 353 citations and is from a domain leading peer-reviewed journal.

15. (revencu2013rasa1mutationsand pages 1-2): Nicole Revencu, Laurence M. Boon, Antonella Mendola, Maria Rosa Cordisco, Josée Dubois, Philippe Clapuyt, Frank Hammer, David J. Amor, Alan D. Irvine, Eulalia Baselga, Anne Dompmartin, Samira Syed, Ana Martin-Santiago, Lesley Ades, Felicity Collins, Janine Smith, Sarah Sandaradura, Victoria R. Barrio, Patricia E. Burrows, Francine Blei, Mariarosaria Cozzolino, Nicola Brunetti-Pierri, Asuncion Vicente, Marc Abramowicz, Julie Désir, Catheline Vilain, Wendy K. Chung, Ashley Wilson, Carol A. Gardiner, Yim Dwight, David J.E. Lord, Leona Fishman, Cheryl Cytrynbaum, Sarah Chamlin, Fred Ghali, Yolanda Gilaberte, Shelagh Joss, Maria del C. Boente, Christine Léauté-Labrèze, Marie-Ange Delrue, Susan Bayliss, Loreto Martorell, Maria-Antonia González-Enseñat, Juliette Mazereeuw-Hautier, Brid O'Donnell, Didier Bessis, Reed E. Pyeritz, Aicha Salhi, Oon T. Tan, Orli Wargon, John B. Mulliken, and Miikka Vikkula. Rasa1 mutations and associated phenotypes in 68 families with capillary malformation–arteriovenous malformation. Human Mutation, 34:1632-1641, Dec 2013. URL: https://doi.org/10.1002/humu.22431, doi:10.1002/humu.22431. This article has 353 citations and is from a domain leading peer-reviewed journal.

16. (brix2022capillarymalformationarteriovenousmalformation pages 4-5): Anna Trier Heiberg Brix, Pernille Mathiesen Tørring, and Anette Bygum. Capillary malformation-arteriovenous malformation type 2: a case report and review. Acta Dermato-Venereologica, 102:adv00662, Mar 2022. URL: https://doi.org/10.2340/actadv.v102.1126, doi:10.2340/actadv.v102.1126. This article has 15 citations and is from a domain leading peer-reviewed journal.

17. (tas2022arteriovenouscerebralhigh pages 3-4): Berivan Tas, Daniele Starnoni, Stanislas Smajda, Alexandre J. Vivanti, Catherine Adamsbaum, Mélanie Eyries, Judith Melki, Marcel Tawk, Augustin Ozanne, Nicole Revencu, Florent Soubrier, Selima Siala, Miikka Vikkula, Kumaran Deiva, and Guillaume Saliou. Arteriovenous cerebral high flow shunts in children: from genotype to phenotype. Frontiers in Pediatrics, Apr 2022. URL: https://doi.org/10.3389/fped.2022.871565, doi:10.3389/fped.2022.871565. This article has 10 citations.

18. (brix2022capillarymalformationarteriovenousmalformation pages 2-4): Anna Trier Heiberg Brix, Pernille Mathiesen Tørring, and Anette Bygum. Capillary malformation-arteriovenous malformation type 2: a case report and review. Acta Dermato-Venereologica, 102:adv00662, Mar 2022. URL: https://doi.org/10.2340/actadv.v102.1126, doi:10.2340/actadv.v102.1126. This article has 15 citations and is from a domain leading peer-reviewed journal.

19. (wooderchakdonahue2018expandingtheclinical pages 10-11): Whitney L. Wooderchak-Donahue, Peter Johnson, Jamie McDonald, Francine Blei, Alejandro Berenstein, Michelle Sorscher, Jennifer Mayer, Angela E. Scheuerle, Tracey Lewis, J. Fredrik Grimmer, Gresham T. Richter, Marcie A. Steeves, Angela E. Lin, David A. Stevenson, and Pinar Bayrak-Toydemir. Expanding the clinical and molecular findings in rasa1 capillary malformation-arteriovenous malformation. European Journal of Human Genetics, 26:1521-1536, Jun 2018. URL: https://doi.org/10.1038/s41431-018-0196-1, doi:10.1038/s41431-018-0196-1. This article has 79 citations and is from a domain leading peer-reviewed journal.

20. (palermo2025capillarymalformation–arteriovenousmalformation pages 11-13): Matteo Palermo, Alessandro Olivi, and Carmelo Lucio Sturiale. Capillary malformation–arteriovenous malformation syndrome (cm-avm): a systematic review of cerebrovascular manifestations. Child's Nervous System, Dec 2025. URL: https://doi.org/10.1007/s00381-025-07089-5, doi:10.1007/s00381-025-07089-5. This article has 0 citations.

21. (engel2023prevalenceandpredictors pages 13-17): ER Engel. Prevalence and predictors of hht and cm-avm syndrome among children with neurovascular malformations. Unknown journal, 2023.

22. (palermo2025capillarymalformation–arteriovenousmalformation pages 7-9): Matteo Palermo, Alessandro Olivi, and Carmelo Lucio Sturiale. Capillary malformation–arteriovenous malformation syndrome (cm-avm): a systematic review of cerebrovascular manifestations. Child's Nervous System, Dec 2025. URL: https://doi.org/10.1007/s00381-025-07089-5, doi:10.1007/s00381-025-07089-5. This article has 0 citations.

23. (chen2023ephb4rasa1mediatednegativeregulation pages 7-9): D Chen, MA Van der Ent, NL Lartey, and PD King. Ephb4-rasa1-mediated negative regulation of ras-mapk signaling in the vasculature: implications for the treatment of ephb4-and rasa1-related vascular …. Unknown journal, 2023.

24. (chen2023ephb4rasa1mediatednegativeregulation pages 6-7): D Chen, MA Van der Ent, NL Lartey, and PD King. Ephb4-rasa1-mediated negative regulation of ras-mapk signaling in the vasculature: implications for the treatment of ephb4-and rasa1-related vascular …. Unknown journal, 2023.

25. (stewen2024ephephrinsignalingcouples pages 1-2): Jonas Stewen, Kai Kruse, Anca T. Godoi-Filip, Zenia, Hyun-Woo Jeong, Susanne Adams, Frank Berkenfeld, Martin Stehling, Kristy Red-Horse, Ralf H. Adams, and Mara E. Pitulescu. Eph-ephrin signaling couples endothelial cell sorting and arterial specification. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46300-0, doi:10.1038/s41467-024-46300-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

26. (palermo2025capillarymalformation–arteriovenousmalformation pages 13-14): Matteo Palermo, Alessandro Olivi, and Carmelo Lucio Sturiale. Capillary malformation–arteriovenous malformation syndrome (cm-avm): a systematic review of cerebrovascular manifestations. Child's Nervous System, Dec 2025. URL: https://doi.org/10.1007/s00381-025-07089-5, doi:10.1007/s00381-025-07089-5. This article has 0 citations.

27. (seront2024molecularlandscapeand pages 6-7): Emmanuel Seront, Angela Queisser, Laurence M. Boon, and Miikka Vikkula. Molecular landscape and classification of vascular anomalies. Hematology, 2024:700-708, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000598, doi:10.1182/hematology.2024000598. This article has 8 citations and is from a peer-reviewed journal.

28. (morin2025vascularmalformationsfrom pages 3-5): Gabriel Morin, Ilaria Galasso, and Guillaume Canaud. Vascular malformations: from genetics to therapeutics. EMBO Molecular Medicine, 18:1-21, Nov 2025. URL: https://doi.org/10.1038/s44321-025-00344-x, doi:10.1038/s44321-025-00344-x. This article has 4 citations and is from a highest quality peer-reviewed journal.

29. (morin2025vascularmalformationsfrom pages 12-13): Gabriel Morin, Ilaria Galasso, and Guillaume Canaud. Vascular malformations: from genetics to therapeutics. EMBO Molecular Medicine, 18:1-21, Nov 2025. URL: https://doi.org/10.1038/s44321-025-00344-x, doi:10.1038/s44321-025-00344-x. This article has 4 citations and is from a highest quality peer-reviewed journal.

30. (NCT04258046 chunk 1): Joyce Teng. Trametinib in the Treatment of Complicated Extracranial Arterial Venous Malformation. Stanford University. 2020. ClinicalTrials.gov Identifier: NCT04258046

31. (NCT07549646 chunk 1):  24VA021; VATCH Trametinib for Ras/MAPK Pathway VAs. Children's Hospital of Philadelphia. 2025. ClinicalTrials.gov Identifier: NCT07549646

32. (NCT07072403 chunk 1): Yi Ji. Trametinib Treatment for Complicated Vascular Anomalies. West China Hospital. 2025. ClinicalTrials.gov Identifier: NCT07072403

33. (morin2025vascularmalformationsfrom pages 6-7): Gabriel Morin, Ilaria Galasso, and Guillaume Canaud. Vascular malformations: from genetics to therapeutics. EMBO Molecular Medicine, 18:1-21, Nov 2025. URL: https://doi.org/10.1038/s44321-025-00344-x, doi:10.1038/s44321-025-00344-x. This article has 4 citations and is from a highest quality peer-reviewed journal.

34. (seront2024molecularlandscapeand pages 1-3): Emmanuel Seront, Angela Queisser, Laurence M. Boon, and Miikka Vikkula. Molecular landscape and classification of vascular anomalies. Hematology, 2024:700-708, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000598, doi:10.1182/hematology.2024000598. This article has 8 citations and is from a peer-reviewed journal.