---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T15:13:13.186472'
end_time: '2026-04-04T15:24:46.992487'
duration_seconds: 693.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mycetoma
  mondo_id: ''
  category: Infectious Disease
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
- **Disease Name:** Mycetoma
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Mycetoma** covering all of the
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
- **Disease Name:** Mycetoma
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Mycetoma** covering all of the
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


# Comprehensive Research Report: Mycetoma (Infectious Disease)

## Executive summary
Mycetoma is a chronic, progressively destructive implantation infection of skin and subcutaneous tissue that can extend into deep tissues and bone, producing disability, deformity, and sometimes amputation; it is caused by either filamentous bacteria (actinomycetoma) or true fungi (eumycetoma). A defining clinical hallmark is a triad of subcutaneous swelling, draining sinuses, and grain-containing discharge. Recent (2023–2024) advances emphasize (i) scaling molecular/isothermal diagnostics in endemic settings, (ii) improved epidemiologic quantification of burden and prevention impacts, and (iii) the first randomized, double-blind eumycetoma drug trial (fosravuconazole vs itraconazole) that did not show superiority but clarified feasibility, safety, and endpoints. (fahal2023mycetomaandthe pages 1-2, husain2023anoverviewof pages 2-4, clark2024eumycetomacausativeagents pages 1-2, fahal2024twodoselevels pages 1-2)

| Item | Details |
|---|---|
| Definition / clinical triad | Chronic granulomatous subcutaneous infection; classic triad = painless/subcutaneous swelling, multiple discharging sinuses, and grains/macroscopic granules in discharge (fahal2023mycetomaandthe pages 1-2, verma2019mycetomareviewinga pages 1-2, husain2023anoverviewof pages 1-2) |
| Classification | Eumycetoma = fungal; actinomycetoma = bacterial/filamentous bacterial. Disease is classified by causative organism (fahal2023mycetomaandthe pages 1-2, sande2024anupdatedlist pages 1-2, alhaj2024epidemiologicalobservationsand pages 1-2) |
| Key identifiers | ICD-10: **B47** “mycetoma” (ferreira2026neglectedmycosesin pages 3-4); MeSH: **D008271** “Mycetoma” (NCT06523998 chunk 2, NCT04401969 chunk 2, NCT03086226 chunk 2); ClinicalTrials.gov: **NCT03086226** (fosravuconazole vs itraconazole), **NCT04401969** (mycetoma granuloma study) (NCT04401969 chunk 2, NCT03086226 chunk 2) |
| Common synonym | **Madura foot** (verma2019mycetomareviewinga pages 1-2) |
| Endemic belt | Mainly in the “mycetoma belt,” about **15°S to 30°N** (fahal2023mycetomaandthe pages 1-2, verma2019mycetomareviewinga pages 1-2, husain2023anoverviewof pages 1-2) |
| Common sites | **Foot** is the main site: ~**79.2%** in one review; hand ~**6.6%**. Lower limb involvement ~**76.9%–77%** in systematic reviews (fahal2023mycetomaandthe pages 1-2, salah2025globalsociodemographicclinical pages 12-14, salah2025globalsociodemographicclinical pages 1-3) |
| Key risk factors | Traumatic inoculation via **thorns/minor trauma** from environmental reservoirs is the leading hypothesis; common in **farmers/rural residents**; strong **male predominance** reported, e.g. **56.6%–79.6%** in eumycetoma review, ~**73.5%–74%** in global reviews (fahal2023mycetomaandthe pages 1-2, verma2019mycetomareviewinga pages 1-2, husain2023anoverviewof pages 1-2, salah2025globalsociodemographicclinical pages 12-14, salah2025globalsociodemographicclinical pages 1-3) |


*Table: This table compiles the core identifiers, synonyms, distribution, clinical presentation, and major risk factors for mycetoma from the retrieved evidence. It is useful as a compact reference for disease knowledge base curation.*

| Domain | 2023–2024 evidence (include key numeric results) | Source (first author, year, journal) | PMID/DOI/Trial ID | URL |
|---|---|---|---|---|
| Diagnostic advances | Review highlights newer diagnostics beyond microscopy/culture: pan-fungal/pan-bacterial PCR and sequencing, MALDI-TOF MS, RCA, LAMP, and RPA. In one cited direct-detection study for *Madurella mycetomatis*, **RPA and LAMP matched PCR with 100% sensitivity and 100% specificity**; RPA was noted to have lower contamination risk. FNA in a cohort of **3,177** patients aligned with *M. mycetomatis* in **75% (2,379)** cases; cell-block cytology sensitivities reported as **85.7%** (actinomycetoma) and **87.5%** (eumycetoma). Imaging signs such as MRI/US grain patterns also aid diagnosis (husain2023anoverviewof pages 2-4) | Husain, 2023, *Indian J Dermatol Venereol Leprol* | DOI: 10.25259/IJDVL_615_2021 | https://doi.org/10.25259/IJDVL_615_2021 |
| Phase 2 treatment trial | First randomized, double-blind eumycetoma trial: **N=104** with *Madurella mycetomatis* eumycetoma; arms were **fosravuconazole 300 mg once weekly (n=34)**, **fosravuconazole 200 mg once weekly (n=34)**, and **itraconazole 400 mg daily (n=36)**, all with surgery at month 6 for 12 months total. **Complete cure (mITT)**: **50%** (17/34) for 300 mg fosravuconazole, **65%** (22/34) for 200 mg fosravuconazole, **75%** (27/36) for itraconazole. Trial was **stopped early for futility** after an unplanned interim analysis; neither fosravuconazole dose was superior. **83** patients had **205** treatment-emergent adverse events; **2** serious AEs led to discontinuation but were not treatment-related (fahal2024twodoselevels pages 1-2, fahal2024twodoselevels pages 2-2) | Fahal, 2024, randomized double-blind trial; ClinicalTrials.gov | DOI not fully available in retrieved text; **NCT03086226** | https://clinicaltrials.gov/study/NCT03086226 |
| Epidemiology and burden | 2024 systematic review found high morbidity: **moderate to severe quality-of-life impairment in 60.3%**, **amputation up to 38.5%**, and **recurrent or long-term disease in 31.8%–73.5%**. Risk factors/demographics included **male sex 56.6%–79.6%**, **age 11–30 years in 64%**, and **farming occupation 62.1%–69.7%**. Geographic concentration was strongest in Sudan, with central Sudan contributing **37%–76.6%** of cases (clark2024eumycetomacausativeagents pages 1-2, clark2024eumycetomacausativeagents pages 2-3) | Clark, 2024, *Medical Mycology* | DOI: 10.1093/mmy/myae044 | https://doi.org/10.1093/mmy/myae044 |
| Incidence and prevention impact | Same 2024 review reported incidence estimates of **0.1/100,000 persons** (Philippines) and **0.32/100,000 persons/decade** (Uganda), with Uganda declining from **3.37 to 0.32/100,000** between the 2000–2009 and 2010–2019 periods. A community-based prevention package (early detection, training, hygiene/environmental actions, free itraconazole) was associated with amputation reduction from **62.8% to 11.9%** (clark2024eumycetomacausativeagents pages 3-4, clark2024eumycetomacausativeagents pages 1-2, clark2024eumycetomacausativeagents pages 4-5) | Clark, 2024, *Medical Mycology* | DOI: 10.1093/mmy/myae044 | https://doi.org/10.1093/mmy/myae044 |
| Mechanism / pathophysiology | *Clinical Microbiology Reviews* 2024 describes four disease phases: **Phase 1 implantation**, **Phase 2 grain formation**, **Phase 3 subcutaneous swelling**, **Phase 4 bone invasion**. Grain development in vivo proceeds through four stages, including early hyphal clustering, formation of **cement material**, capsule formation, and granuloma formation. The grain matrix contains **melanin, proteins, chitin, and polysaccharides** and behaves as a biofilm-like barrier. Experimentally, adding **250 µg/mL *M. mycetomatis* melanin** to susceptibility assays caused a **strong rise in MIC** for ketoconazole and itraconazole. In vivo, amphotericin B (**1 mg/kg/day for 14 days**) cleared grains by day 21 in mice, whereas itraconazole (**40 mg/kg/day for 14 days**) did not at the tested dose (sande2024anupdatedlist pages 1-2, sande2024anupdatedlist pages 9-12, sande2024anupdatedlist pages 20-22) | van de Sande, 2024, *Clinical Microbiology Reviews* | DOI: 10.1128/cmr.00034-23 | https://doi.org/10.1128/cmr.00034-23 |


*Table: This table compiles the most decision-relevant 2023–2024 evidence on mycetoma diagnostics, treatment trials, epidemiology, and mechanism. It is useful as a compact, citation-backed summary for a disease knowledge base or research report.*

| Category | Item (plain language) | Ontology term suggestions (HPO/UBERON/GO/CL/MAXO) | Evidence notes |
|---|---|---|---|
| Phenotype | Subcutaneous swelling / tumorous mass | HPO: Subcutaneous nodule; HPO: Swelling; UBERON: subcutaneous tissue | Part of the classic triad; described as subcutaneous swelling or mass in mycetoma (fahal2023mycetomaandthe pages 1-2, verma2019mycetomareviewinga pages 1-2, husain2023anoverviewof pages 1-2) |
| Phenotype | Multiple draining sinuses | HPO: Skin sinus; HPO: Abnormality of the skin | Classic triad includes multiple discharging sinuses (fahal2023mycetomaandthe pages 1-2, verma2019mycetomareviewinga pages 1-2, husain2023anoverviewof pages 1-2) |
| Phenotype | Grains/macroscopic granules in discharge | HPO: Abnormality of skin morphology; GO: biofilm formation (suggestive mechanistic term) | Classic triad includes grains/macroscopic granules; grains are considered unique to mycetoma (husain2023anoverviewof pages 1-2, sande2024anupdatedlist pages 6-9) |
| Phenotype | Pain at lesion site | HPO: Pain; HPO: Limb pain | Usually painless, but pain was reported in ~18–20% in review data and 21% in extrapedal series (sande2024anupdatedlist pages 9-12, alhaj2024epidemiologicalobservationsand pages 1-2) |
| Phenotype | Regional lymphadenopathy | HPO: Lymphadenopathy | Reported in 11.5% of extrapedal cases (alhaj2024epidemiologicalobservationsand pages 1-2, alhaj2024epidemiologicalobservationsand pages 13-14) |
| Phenotype | Bone invasion / osseous destruction | HPO: Osteolysis; HPO: Abnormality of bone structure; UBERON: bone element | Disease progresses from implantation to bone invasion; untreated disease may extend to bone and cause disability (sande2024anupdatedlist pages 1-2, verma2019mycetomareviewinga pages 1-2, sande2024anupdatedlist pages 6-9) |
| Anatomy | Foot localization | UBERON: foot; HPO: Abnormal foot morphology | Foot is the commonest site, about 79.2% in one review; lower limb involvement ~76.9–77% in systematic reviews (fahal2023mycetomaandthe pages 1-2, salah2025globalsociodemographicclinical pages 12-14) |
| Anatomy | Hand localization | UBERON: hand | Hand is the second most common site (~6.6%) (fahal2023mycetomaandthe pages 1-2) |
| Anatomy | Buttock / gluteal extrapedal disease | UBERON: buttock | Buttocks were the most frequent extrapedal site (37.9%) in the Sudan series (alhaj2024epidemiologicalobservationsand pages 1-2) |
| Anatomy | Head and neck extrapedal disease | UBERON: head; UBERON: neck | Head and neck represented 16.9% of extrapedal cases (alhaj2024epidemiologicalobservationsand pages 1-2) |
| Diagnostic | Grain examination and microscopy | MAXO: Microscopic examination; MAXO: Microbiological testing | Routine diagnosis commonly uses clinical observation, grain examination, microscopy, and direct examination (verma2019mycetomareviewinga pages 1-2, salah2025globalsociodemographicclinical pages 12-14) |
| Diagnostic | Culture of causative organism | MAXO: Microbial culture; MAXO: Fungal culture | Culture remains standard; review notes incubation for 4–6 weeks before declaring negative (husain2023anoverviewof pages 2-4) |
| Diagnostic | Imaging: MRI / ultrasound, including dot-in-circle sign | MAXO: Magnetic resonance imaging; MAXO: Ultrasonography | MRI “dot-in-circle” and ultrasound grain patterns help diagnosis and extent assessment (husain2023anoverviewof pages 2-4) |
| Diagnostic | Fine-needle aspiration / cell block cytology | MAXO: Fine needle aspiration biopsy; MAXO: Cytopathology | FNA in 3,177 patients aligned with M. mycetomatis in 75%; cell-block sensitivities 85.7% (actinomycetoma) and 87.5% (eumycetoma) (husain2023anoverviewof pages 2-4) |
| Diagnostic | PCR and sequencing (pan-fungal / pan-bacterial / ITS) | MAXO: Polymerase chain reaction assay; MAXO: DNA sequencing | Advanced molecular tools detect culture-negative cases; ITS sequencing used in recent clinical studies/trials (husain2023anoverviewof pages 2-4, fahal2024twodoselevels pages 10-11) |
| Diagnostic | LAMP / RPA / RCA | MAXO: Nucleic acid amplification test | RPA and LAMP were reported to match PCR with 100% sensitivity and 100% specificity for direct detection of M. mycetomatis; RCA also highlighted as promising (husain2023anoverviewof pages 2-4) |
| Diagnostic | MALDI-TOF MS | MAXO: Mass spectrometry-based identification | 2023 review identifies MALDI-TOF MS as a high-throughput proteomic identification tool for mycetoma agents (husain2023anoverviewof pages 2-4) |
| Intervention | Itraconazole for eumycetoma | MAXO: Antifungal therapy; CHEBI: itraconazole | Standard current antifungal; in the 2024 RCT, itraconazole 400 mg daily had 75% complete cure in mITT, outperforming fosravuconazole arms (fahal2024twodoselevels pages 1-2, sande2024anupdatedlist pages 20-22) |
| Intervention | Fosravuconazole / ravuconazole strategy | MAXO: Antifungal therapy; CHEBI: ravuconazole | Weekly fosravuconazole was well tolerated but not superior to itraconazole in NCT03086226; practical advantages include weekly dosing and fewer drug–drug interactions (fahal2024twodoselevels pages 2-2, fahal2024twodoselevels pages 1-2) |
| Intervention | Terbinafine | MAXO: Antifungal therapy; CHEBI: terbinafine | Used as alternative/adjunct in eumycetoma; species-specific responses reported, with lower adjusted cure than itraconazole+surgery in some series (sande2024anupdatedlist pages 20-22) |
| Intervention | Amphotericin B | MAXO: Antifungal therapy; CHEBI: amphotericin B | In animal models, amphotericin B cleared grains by day 21, whereas itraconazole did not at tested doses (sande2024anupdatedlist pages 20-22) |
| Intervention | TMP-SMX (co-trimoxazole) for actinomycetoma | MAXO: Antibiotic therapy; CHEBI: sulfamethoxazole; CHEBI: trimethoprim | Co-trimoxazole is described as gold-standard therapy for actinomycetoma and is widely used in combination regimens (scolding2018drugtherapyfor pages 4-5, nenoff2015eumycetomaandactinomycetoma pages 8-9) |
| Intervention | Amikacin for actinomycetoma | MAXO: Aminoglycoside antibiotic therapy; CHEBI: amikacin | Used in severe/resistant actinomycetoma, including Welsh-type regimens and pulse-based combinations (scolding2018drugtherapyfor pages 4-5, nenoff2015eumycetomaandactinomycetoma pages 8-9) |
| Intervention | Surgery / debridement / wide excision | MAXO: Surgical excision; MAXO: Debridement | Eumycetoma often requires surgery plus medical therapy; complete cure associated with surgery, smaller lesions, and shorter duration (elkheir2020madurellamycetomatiscausing pages 1-3, sande2024anupdatedlist pages 20-22) |
| Intervention | Amputation in advanced disease | MAXO: Amputation | Used in advanced/destructive disease; 2024 burden review reported amputation up to 38.5% and prevention programs reduced amputations from 62.8% to 11.9% (clark2024eumycetomacausativeagents pages 1-2, elkheir2020madurellamycetomatiscausing pages 1-3) |
| Prevention / Public health | Protective footwear, hygiene, and early detection | MAXO: Health education; MAXO: Disease screening; MAXO: Preventive intervention | Prevention emphasized through footwear and hygiene; community program with early detection/training/hygiene/environmental action reduced amputation markedly (verma2019mycetomareviewinga pages 1-2, clark2024eumycetomacausativeagents pages 3-4, clark2024eumycetomacausativeagents pages 1-2) |
| Digital health | AI-supported frontline diagnosis and surveillance | MAXO: Clinical decision support; MAXO: Disease screening | SkincAIr trial includes mycetoma among skin NTDs; tests AI support for frontline health workers with targets for accuracy improvement, earlier detection, and hotspot mapping (NCT07506967 chunk 3, NCT07506967 chunk 2) |


*Table: This table organizes major mycetoma phenotypes, anatomical sites, diagnostic approaches, and interventions with suggested ontology mappings and evidence-backed notes. It is useful for building structured disease knowledge-base entries and annotation pipelines.*

---

## 1. Disease information
### 1.1 Overview and current definition
Mycetoma is a chronic granulomatous inflammatory disease of subcutaneous tissues that can spread to involve skin, deep tissues, and bone; it is considered a neglected tropical disease and can cause severe disability when treatment is delayed. (fahal2023mycetomaandthe pages 1-2, alhaj2024epidemiologicalobservationsand pages 1-2)

**Key clinical definition (classical triad):** “subcutaneous swelling, multiple discharging sinuses and the presence of macroscopic granules/grains.” (husain2023anoverviewof pages 1-2)

### 1.2 Classification (etiology-based)
Mycetoma is classified into:
- **Eumycetoma** (fungal mycetoma) and
- **Actinomycetoma** (bacterial/actinomycotic mycetoma). (fahal2023mycetomaandthe pages 1-2, sande2024anupdatedlist pages 1-2)

### 1.3 Key identifiers and synonyms (explicitly evidenced)
- **ICD-10:** Mycetoma = **B47**. (ferreira2026neglectedmycosesin pages 3-4)
- **MeSH:** Mycetoma = **D008271**. (NCT06523998 chunk 2, NCT04401969 chunk 2, NCT03086226 chunk 2)
- **Common synonym:** “**Madura foot**.” (verma2019mycetomareviewinga pages 1-2)
- **ClinicalTrials.gov identifiers (selected):** NCT03086226 (eumycetoma antifungal trial), NCT04401969 (granuloma microenvironment signatures), NCT06512714 (retrospective data collection), NCT07506967 (AI-based early detection of skin NTDs incl. mycetoma). (fahal2024twodoselevels pages 1-2, NCT04401969 chunk 1, NCT06512714 chunk 1, NCT07506967 chunk 1)

**Not found in retrieved evidence:** explicit **MONDO**, **Orphanet ORPHA**, or **ICD-11** identifiers were not present in the retrieved full texts/records and therefore cannot be reliably stated here.

### 1.4 Evidence provenance (patient-level vs aggregated)
The evidence base in this report mixes:
- **Aggregated disease-level resources** (systematic reviews and major reviews) (clark2024eumycetomacausativeagents pages 1-2, sande2024anupdatedlist pages 1-2)
- **Hospital-based cohorts/case series** (e.g., 420-case extrapedal series) (alhaj2024epidemiologicalobservationsand pages 1-2)
- **Clinical trial/registry records** (ClinicalTrials.gov) (NCT04401969 chunk 1, NCT07506967 chunk 3)

---

## 2. Etiology
### 2.1 Causal factors
**Primary causal factor:** implantation of environmental microorganisms into subcutaneous tissue, typically through minor trauma (e.g., thorn pricks). (fahal2023mycetomaandthe pages 1-2, alhaj2024epidemiologicalobservationsand pages 1-2)

**Examples of causative agents (representative, not exhaustive):**
- Fungal: *Madurella mycetomatis* (most commonly reported globally for eumycetoma). (sande2024anupdatedlist pages 1-2)
- Bacterial: actinomycetoma agents include *Nocardia* spp., *Streptomyces* spp., *Actinomadura* spp. (verma2019mycetomareviewinga pages 1-2, alhaj2024epidemiologicalobservationsand pages 1-2)

### 2.2 Risk factors (human epidemiology)
Recent systematic-review level estimates identify consistent demographic and occupational associations:
- Male predominance (reported ranges **56.6%–79.6%** in eumycetoma cohorts). (clark2024eumycetomacausativeagents pages 1-2)
- Younger age distribution (e.g., **11–30 years; 64%** in one eumycetoma dataset). (clark2024eumycetomacausativeagents pages 1-2)
- Agricultural/farming occupation (**62.1%–69.7%** in two studies). (clark2024eumycetomacausativeagents pages 1-2)

Environmental and contextual risk factors proposed in 2023 synthesis include soil type/consistency, temperature, aridity index, thorny trees, animal dung as a niche/reservoir, and socioeconomic/hygiene/health-education factors. (fahal2023mycetomaandthe pages 1-2)

### 2.3 Protective factors
Direct protective-factor quantification is limited in retrieved evidence; however, prevention-oriented measures are repeatedly emphasized:
- Wearing protective footwear and improving hygiene/health education are described as necessary to reduce occurrence. (fahal2023mycetomaandthe pages 1-2, verma2019mycetomareviewinga pages 1-2)

### 2.4 Gene–environment interactions
The 2023 environmental review notes that “the individual’s genetic and immunological backgrounds may determine the disease’s susceptibility and resistance,” but the retrieved evidence did **not** provide specific human susceptibility loci/variants or quantitative GxE interaction results. (fahal2023mycetomaandthe pages 1-2)

---

## 3. Phenotypes
### 3.1 Core phenotypic spectrum
Key phenotypes include:
- Subcutaneous swelling/mass (often initially painless). (fahal2023mycetomaandthe pages 1-2, husain2023anoverviewof pages 1-2)
- Multiple draining sinuses with grain discharge (the classical triad). (husain2023anoverviewof pages 1-2)
- Progressive deep extension, including bone involvement in advanced disease. (sande2024anupdatedlist pages 6-9, sande2024anupdatedlist pages 1-2)

**Pain:** While classically painless, pain is reported in a substantial minority (e.g., **~18–21%** across cited datasets). (sande2024anupdatedlist pages 9-12, alhaj2024epidemiologicalobservationsand pages 1-2)

**Lymphadenopathy:** In a 420-case extrapedal cohort, lymphadenopathy was reported in **11.5%**. (alhaj2024epidemiologicalobservationsand pages 1-2)

### 3.2 Age of onset and progression
Disease is typically chronic and insidious with long incubation (reported **3 months to 9 years**) and often affects young adults (20–40 years) with male predominance. (husain2023anoverviewof pages 1-2)

### 3.3 Quality of life impact
A 2024 systematic review reported “**moderate to severe impairment of quality of life in 60.3%**” of eumycetoma patients and substantial disability/unemployment and financial impact in included studies. (clark2024eumycetomacausativeagents pages 1-2, clark2024eumycetomacausativeagents pages 2-3)

### 3.4 Suggested HPO terms (examples)
Ontology suggestions mapped to evidence-supported phenotypes are provided in Artifact 02. (husain2023anoverviewof pages 1-2, alhaj2024epidemiologicalobservationsand pages 1-2, sande2024anupdatedlist pages 6-9)

---

## 4. Genetic / molecular information
### 4.1 Human causal genes and pathogenic variants
Mycetoma is primarily an **infectious** implantation disease; the retrieved evidence does **not** identify monogenic “causal genes,” ClinVar-annotated pathogenic variants, or validated human susceptibility loci.

### 4.2 Pathogen molecular targets and resistance-related observations (selected)
In the fosravuconazole/itraconazole trial, investigators reported no change in the *Madurella mycetomatis* **CYP51A** sequence and no MIC rise above epidemiological cutoffs after azole exposure (suggesting no clear selection of high-level azole resistance in that study). (fahal2024twodoselevels pages 10-11)

---

## 5. Environmental information
Mycetoma pathogens are described as present in endemic environments “in active or dormant forms,” with DNA detected in soil, trees, thorns, households, and animal dung; thorns may facilitate inoculation. (fahal2023mycetomaandthe pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (trigger → lesion → complications)
1) **Trigger/entry:** penetrating trauma introduces organism into subcutaneous tissue. (sande2024anupdatedlist pages 6-9, sande2024anupdatedlist pages 1-2)
2) **Grain formation:** organisms aggregate into “grains,” a hallmark structure that is difficult to replicate in vitro and best studied in vivo models. (sande2024anupdatedlist pages 6-9)
3) **Granulomatous inflammation/capsule:** grains become surrounded by host response and a capsule/granuloma; lesions enlarge and sinus tracts form. (sande2024anupdatedlist pages 9-12, sande2024anupdatedlist pages 1-2)
4) **Deep spread:** disease can invade bone (Phase 4 in 2024 review), producing destructive osteoarticular disease and disability. (sande2024anupdatedlist pages 1-2)

### 6.2 Grain as a biofilm-like barrier and drug-sequestration mechanism
A 2024 *Clinical Microbiology Reviews* synthesis describes grain cement as containing “**melanin, proteins, chitin, and polysaccharides**” and indicates this matrix “seems to protect the fungus inside against these drugs.” (sande2024anupdatedlist pages 20-22)

A key quantitative finding: adding “**250 µg/mL *M. mycetomatis* melanin**” in vitro caused “a strong rise in MIC” for ketoconazole and itraconazole, consistent with drug binding/sequestration. (sande2024anupdatedlist pages 20-22)

Animal model evidence summarized in 2024 review: amphotericin B cleared grains in mice by day 21 under tested conditions, whereas itraconazole did not, reinforcing limited azole efficacy in the presence of grain barriers in vivo. (sande2024anupdatedlist pages 20-22)

### 6.3 Immune involvement (cell types and processes)
In vivo grain maturation proceeds through four stages including early host-cell surround, cement formation, capsule formation, and granuloma formation; host hemocyte (neutrophil-like) clustering, degranulation with reactive oxygen species, and antimicrobial peptide activity are described in these models. (sande2024anupdatedlist pages 9-12)

### 6.4 Suggested GO and CL terms
Examples are suggested in Artifact 02 (e.g., biofilm-related terms; neutrophil-like/innate immune cells), but a full curated mapping would require additional primary immunology studies beyond those retrieved here. (sande2024anupdatedlist pages 9-12, sande2024anupdatedlist pages 20-22)

---

## 7. Anatomical structures affected
### 7.1 Organ/tissue level
Primarily affects **skin and subcutaneous tissues**, with potential extension into **deep tissues and bone**. (alhaj2024epidemiologicalobservationsand pages 1-2, sande2024anupdatedlist pages 6-9)

### 7.2 Localization and distribution
- Most commonly the **foot** (e.g., ~**79.2%** in one review) with lower limb involvement ~**76.9–77%** in systematic reviews. (fahal2023mycetomaandthe pages 1-2, salah2025globalsociodemographicclinical pages 12-14)
- **Hand** is less common (~**6.6%** in one review). (fahal2023mycetomaandthe pages 1-2)
- Extrapedal disease can involve buttock, head/neck, trunk/back; in a 420-case extrapedal cohort, buttock (37.9%) and head/neck (16.9%) were common. (alhaj2024epidemiologicalobservationsand pages 1-2)

---

## 8. Temporal development
Mycetoma often presents after long delays; in the extrapedal cohort, disease duration was <1 year in only **18.5%** of patients, indicating frequent chronicity before care. (alhaj2024epidemiologicalobservationsand pages 13-14)

---

## 9. Inheritance and population
### 9.1 Epidemiology (recent quantitative data)
A 2024 systematic review reported incidence estimates including:
- **0.1 per 100,000 persons** (Philippines)
- **0.32 per 100,000 persons/decade** (Uganda)
- A decline in Uganda from **3.37 to 0.32 per 100,000** between 2000–2009 and 2010–2019. (clark2024eumycetomacausativeagents pages 3-4, clark2024eumycetomacausativeagents pages 1-2)

### 9.2 Geographic distribution
Mycetoma is described as concentrated in the “mycetoma belt” (roughly 15°S–30°N) and is particularly reported from Sudan in multiple sources; the 2024 eumycetoma review notes central Sudan contributing **37%–76.6%** of cases in included datasets. (fahal2023mycetomaandthe pages 1-2, clark2024eumycetomacausativeagents pages 1-2)

### 9.3 Sex ratio and demographics
Male predominance is consistent across reviews and cohorts (see Artifact 00/01); a Sudanese extrapedal cohort reported a male:female ratio of ~4:1. (alhaj2024epidemiologicalobservationsand pages 1-2, clark2024eumycetomacausativeagents pages 1-2)

---

## 10. Diagnostics
### 10.1 Current diagnostic workflow (real-world)
Commonly used diagnostic elements include clinical pattern recognition plus grain examination/microscopy, imaging, histopathology/cytology (including FNA), and culture (often prolonged). (husain2023anoverviewof pages 2-4, salah2025globalsociodemographicclinical pages 12-14)

**Culture considerations:** incubation can be required for **4–6 weeks** before declaring negative in some protocols, which delays species-level confirmation in endemic settings. (husain2023anoverviewof pages 2-4)

### 10.2 Advanced/rapid diagnostics (2023–2024 emphasis)
The 2023 review emphasizes adoption of:
- **Pan-fungal / pan-bacterial PCR and sequencing** (including 16S approaches for bacteria)
- **MALDI-TOF MS**
- Isothermal nucleic acid tests: **LAMP**, **RPA**, and **RCA**. (husain2023anoverviewof pages 2-4)

A striking performance claim cited in that review: for direct detection of *Madurella mycetomatis*, **RPA and LAMP equaled PCR with 100% sensitivity and 100% specificity** in one study. (husain2023anoverviewof pages 2-4)

### 10.3 Differential diagnosis
The retrieved evidence focuses on mycetoma-specific diagnostics and implantation mechanisms; it does not provide a comprehensive differential list in a guideline-like format.

---

## 11. Outcome / prognosis
### 11.1 Morbidity and disability
Eumycetoma can lead to major functional impairment, with a 2024 systematic review reporting “**amputation in up to 38.5%**” and recurrent/long-term disease in **31.8%–73.5%** across included studies. (clark2024eumycetomacausativeagents pages 1-2)

### 11.2 Outcomes in a large 2024 cohort (extrapedal Sudan series)
In 420 extrapedal cases, among those with regular follow-up (n=118), cure was documented in **21.1%** (eumycetoma) and **19.4%** (actinomycetoma), with post-operative recurrence among eumycetoma patients reported as **40%**; follow-up dropout was **57%**. (alhaj2024epidemiologicalobservationsand pages 1-2)

---

## 12. Treatment
### 12.1 Treatment principles and responsiveness
Actinomycetoma is generally more responsive to antimicrobials, with one review stating cure rates “**up to 90%**,” whereas eumycetoma frequently requires prolonged antifungal therapy plus surgery and remains “suboptimal and unsatisfactory in many patients.” (elkheir2020madurellamycetomatiscausing pages 1-3)

### 12.2 Eumycetoma pharmacotherapy and surgery
**Species-specific response and drug binding barriers:** treatment efficacy differs by causative fungus and is strongly influenced by grain matrix properties and susceptibility differences. (sande2024anupdatedlist pages 20-22)

**Cure rate examples (M. mycetomatis series, adjusted):** 56.2% (ketoconazole) and 67.6% (itraconazole), and improved outcomes when itraconazole was combined with surgery (adjusted cure 100% in one setting); corrected azole responses for other agents ranged 20–38.5%. (sande2024anupdatedlist pages 20-22)

### 12.3 Key recent therapeutic development: fosravuconazole RCT (2024)
A randomized, double-blind, active-controlled superiority trial in Sudan compared once-weekly fosravuconazole regimens vs daily itraconazole (all with surgery) in 104 patients with *M. mycetomatis* eumycetoma. Complete cure (mITT) at month 12 was 50% (fosravuconazole 300 mg weekly), 65% (fosravuconazole 200 mg weekly), and 75% (itraconazole 400 mg daily); the trial was stopped early for futility and found no superiority of fosravuconazole. (fahal2024twodoselevels pages 1-2)

**Treatment trial identifier:** NCT03086226 (ClinicalTrials.gov). (fahal2024twodoselevels pages 1-2)

### 12.4 Actinomycetoma antimicrobial regimens (examples)
A Cochrane review protocol summary describes long-term combination antibiotic therapy as standard, with co-trimoxazole becoming the “gold standard,” and combination strategies including co-trimoxazole plus amikacin (Welsh regimen) or stepwise intensive + maintenance regimens. (scolding2018drugtherapyfor pages 4-5)

### 12.5 Suggested MAXO terms
Examples for antifungal therapy, antibiotic therapy, imaging, biopsy, surgical excision, and amputation are provided in Artifact 02. (scolding2018drugtherapyfor pages 4-5, elkheir2020madurellamycetomatiscausing pages 1-3, husain2023anoverviewof pages 2-4)

---

## 13. Prevention
### 13.1 Public health and primary prevention
Prevention is generally framed around reducing inoculation events and delays in care, including protective footwear, hygiene, environmental risk mitigation, and health education. (fahal2023mycetomaandthe pages 1-2, verma2019mycetomareviewinga pages 1-2)

### 13.2 Evidence for community prevention impact (2024)
A 2024 systematic review reported that a community-based, multi-pronged program was associated with a reduction in amputation rates from **62.8%** to **11.9%**. (clark2024eumycetomacausativeagents pages 3-4, clark2024eumycetomacausativeagents pages 1-2)

### 13.3 Secondary prevention / early detection
The same 2024 review emphasizes early case detection as a critical strategy; additionally, an implementation trial is underway/planned to evaluate AI-supported early detection for skin NTDs including mycetoma (SkincAIr). (clark2024eumycetomacausativeagents pages 3-4, NCT07506967 chunk 1)

---

## 14. Other species / natural disease
The retrieved evidence base for this run did not provide a systematic summary of naturally occurring mycetoma across non-human species with NCBI taxon identifiers.

---

## 15. Model organisms
An important experimental approach for grain biology uses **in vivo** models (e.g., *Galleria mellonella* and mouse models) that reproduce staged grain maturation; these models are emphasized because grains cannot be reliably generated in vitro. (sande2024anupdatedlist pages 9-12, sande2024anupdatedlist pages 6-9)

---

## Recent developments and expert analysis (2023–2024 emphasis)
1) **Diagnostics are shifting toward field-deployable molecular/isothermal assays** (LAMP/RPA/RCA) and proteomic identification (MALDI-TOF), addressing culture delays and misidentification risk. (husain2023anoverviewof pages 2-4, sande2024anupdatedlist pages 1-2)
2) **First high-quality RCT evidence in eumycetoma** (NCT03086226) clarifies that fosravuconazole did not outperform itraconazole but remains of interest for practical dosing/drug–drug interaction advantages; this informs trial design, endpoints, and future compound testing programs. (fahal2024twodoselevels pages 1-2, fahal2024twodoselevels pages 2-2)
3) **Mechanism-focused research prioritizes grain biology as the key barrier to cure**, with 2024 synthesis highlighting melanin and biofilm-like cement binding azoles and reducing effective drug exposure at the pathogen. (sande2024anupdatedlist pages 20-22)
4) **Implementation innovation includes AI-assisted frontline detection and surveillance (SkincAIr)** with explicit performance and surveillance KPIs (accuracy improvement thresholds, hotspot mapping, DHIS2 integration), representing a plausible route to reduce diagnostic delay. (NCT07506967 chunk 3, NCT07506967 chunk 2)

---

## Key statistics (recent)
- QoL impairment (moderate–severe): **60.3%** (eumycetoma systematic review). (clark2024eumycetomacausativeagents pages 1-2)
- Amputation: **up to 38.5%** (eumycetoma systematic review), and community program associated reduction **62.8% → 11.9%**. (clark2024eumycetomacausativeagents pages 1-2, clark2024eumycetomacausativeagents pages 3-4)
- Recurrence/long-term disease: **31.8%–73.5%** (systematic review). (clark2024eumycetomacausativeagents pages 1-2)
- Incidence estimates: **0.1/100,000** (Philippines), **0.32/100,000** (Uganda) with decline from **3.37 → 0.32/100,000** across decades. (clark2024eumycetomacausativeagents pages 3-4, clark2024eumycetomacausativeagents pages 1-2)
- Fosravuconazole RCT cure (mITT): **50%**, **65%** vs itraconazole **75%** at 12 months, N=104. (fahal2024twodoselevels pages 1-2)

---

## URLs and publication dates (selected from retrieved evidence)
- Fahal & Bakhiet. **Mycetoma and the environment**. *PLOS Neglected Tropical Diseases*. **Nov 2023**. https://doi.org/10.1371/journal.pntd.0011736 (fahal2023mycetomaandthe pages 1-2)
- Husain et al. **Diagnostic dilemma; advanced techniques**. *Indian J Dermatol Venereol Leprol*. **Oct 2023**. https://doi.org/10.25259/IJDVL_615_2021 (husain2023anoverviewof pages 1-2, husain2023anoverviewof pages 2-4)
- Alhaj et al. **Extrapedal mycetoma (420 cases)**. *PLOS Neglected Tropical Diseases*. **May 2024**. https://doi.org/10.1371/journal.pntd.0011841 (alhaj2024epidemiologicalobservationsand pages 1-2)
- van de Sande & Fahal. **Eumycetoma causative agents; grain differences; treatment response**. *Clinical Microbiology Reviews*. **Jun 2024**. https://doi.org/10.1128/cmr.00034-23 (sande2024anupdatedlist pages 1-2, sande2024anupdatedlist pages 20-22)
- Clark et al. **Eumycetoma causative agents systematic review (WHO fungal priority pathogens context)**. *Medical Mycology*. **Jun 2024**. https://doi.org/10.1093/mmy/myae044 (clark2024eumycetomacausativeagents pages 1-2, clark2024eumycetomacausativeagents pages 3-4)
- Clinical trial record: **NCT03086226**. “Proof-of-Concept Superiority Trial of Fosravuconazole Versus Itraconazole for Eumycetoma in Sudan.” https://clinicaltrials.gov/study/NCT03086226 (NCT03086226 chunk 2, fahal2024twodoselevels pages 1-2)
- Clinical trial record: **NCT04401969**. “Tissue Microenvironment Signatures of the Mycetoma Granuloma.” https://clinicaltrials.gov/study/NCT04401969 (NCT04401969 chunk 1)
- Clinical trial record: **NCT06512714**. “Mycetoma Retrospective Data Collection.” https://clinicaltrials.gov/study/NCT06512714 (NCT06512714 chunk 1)
- Clinical trial record: **NCT07506967**. “Early Detection and AI-Based Management of Skin-Related NTDs… (SkincAIr).” First posted **2026-04-02**; estimated start **2026-05-01**. https://clinicaltrials.gov/study/NCT07506967 (NCT07506967 chunk 1)

---

## Limitations of this evidence synthesis
- Explicit **MONDO/Orphanet/ICD-11** identifiers were not present in the retrieved texts/records and were therefore not asserted.
- Human **genetic susceptibility** evidence (GWAS/variants) was referenced only qualitatively and not supported with locus-level data in retrieved materials. (fahal2023mycetomaandthe pages 1-2)
- Several high-value items (e.g., formal differential diagnosis lists; comprehensive animal disease taxonomy) would require additional targeted retrieval beyond this run.


References

1. (fahal2023mycetomaandthe pages 1-2): Ahmed Hassan Fahal and Sahar Mubarak Bakhiet. Mycetoma and the environment. PLOS Neglected Tropical Diseases, 17:e0011736, Nov 2023. URL: https://doi.org/10.1371/journal.pntd.0011736, doi:10.1371/journal.pntd.0011736. This article has 22 citations and is from a domain leading peer-reviewed journal.

2. (husain2023anoverviewof pages 2-4): Uneza Husain, Parul Verma, Swastika Suvirya, Ketan Priyadarshi, and Prashant Gupta. An overview of mycetoma and its diagnostic dilemma: time to move on to advanced techniques. Indian journal of dermatology, venereology and leprology, 89:1-6, Oct 2023. URL: https://doi.org/10.25259/ijdvl\_615\_2021, doi:10.25259/ijdvl\_615\_2021. This article has 17 citations.

3. (clark2024eumycetomacausativeagents pages 1-2): Julia E Clark, Hannah Yejin Kim, Wendy W J van de Sande, Brendan McMullan, Paul Verweij, Ana Alastruey-Izquierdo, Arunaloke Chakrabarti, Thomas S Harrison, Felix Bongomin, Roderick J Hay, Rita Oladele, Jutta Heim, Peter Beyer, Marcelo Galas, Siswanto Siswanto, Daniel Argaw Dagne, Felipe Roitberg, Valeria Gigante, Justin Beardsley, Hatim Sati, Jan-Willem Alffenaar, and C Orla Morrissey. Eumycetoma causative agents: a systematic review to inform the world health organization priority list of fungal pathogens. Medical Mycology, Jun 2024. URL: https://doi.org/10.1093/mmy/myae044, doi:10.1093/mmy/myae044. This article has 17 citations and is from a peer-reviewed journal.

4. (fahal2024twodoselevels pages 1-2): AH Fahal, ES Ahmed, and SM Bakhiet. Two dose levels of once-weekly fosravuconazole versus daily itraconazole in combination with surgery in patients with eumycetoma in sudan: a randomised, double …. Unknown journal, 2024.

5. (verma2019mycetomareviewinga pages 1-2): P. Verma and A. Jha. Mycetoma: reviewing a neglected disease. Clinical and Experimental Dermatology, 44:123-129, May 2019. URL: https://doi.org/10.1111/ced.13642, doi:10.1111/ced.13642. This article has 161 citations and is from a peer-reviewed journal.

6. (husain2023anoverviewof pages 1-2): Uneza Husain, Parul Verma, Swastika Suvirya, Ketan Priyadarshi, and Prashant Gupta. An overview of mycetoma and its diagnostic dilemma: time to move on to advanced techniques. Indian journal of dermatology, venereology and leprology, 89:1-6, Oct 2023. URL: https://doi.org/10.25259/ijdvl\_615\_2021, doi:10.25259/ijdvl\_615\_2021. This article has 17 citations.

7. (sande2024anupdatedlist pages 1-2): Wendy W. J. van de Sande and Ahmed H. Fahal. An updated list of eumycetoma causative agents and their differences in grain formation and treatment response. Clinical Microbiology Reviews, Jun 2024. URL: https://doi.org/10.1128/cmr.00034-23, doi:10.1128/cmr.00034-23. This article has 37 citations and is from a highest quality peer-reviewed journal.

8. (alhaj2024epidemiologicalobservationsand pages 1-2): Abubakr Abdalla Mohammed Alhaj, Eiman Siddig Ahmed, Abeer Hassan, and Ahmed Hassan Fahal. Epidemiological observations and management challenges in extrapedal mycetoma: a three-decade review of 420 cases. PLOS Neglected Tropical Diseases, 18:e0011841, May 2024. URL: https://doi.org/10.1371/journal.pntd.0011841, doi:10.1371/journal.pntd.0011841. This article has 15 citations and is from a domain leading peer-reviewed journal.

9. (ferreira2026neglectedmycosesin pages 3-4): Anderson Fuentes Ferreira, Jorg Heukelbach, Eliana Amorim de Souza, Maria Aparecida Shikanai‐Yasuda, Lisandra Serra Damasceno, Fernanda Dockhorn Costa, Terezinha do Menino Jesus Silva Leitão, Helia Kawa, and Alberto Novaes Ramos. Neglected mycoses in brazil: a population‐based study of mortality and in‐hospital mortality over 25 years. Mycoses, Feb 2026. URL: https://doi.org/10.1111/myc.70144, doi:10.1111/myc.70144. This article has 0 citations and is from a peer-reviewed journal.

10. (NCT06523998 chunk 2): Daniel Barquero Orias. A Study on Rare Dermatological Infections Conducted at Three Major Reference Hospitals in Costa Rica.. Caja Costarricense de Seguro Social. 2023. ClinicalTrials.gov Identifier: NCT06523998

11. (NCT04401969 chunk 2): Dr Mohamed Osman. Tissue Microenvironment Signatures of the Mycetoma Granuloma. University of Khartoum. 2019. ClinicalTrials.gov Identifier: NCT04401969

12. (NCT03086226 chunk 2):  Proof-of-Concept Superiority Trial of Fosravuconazole Versus Itraconazole for Eumycetoma in Sudan. Drugs for Neglected Diseases. 2017. ClinicalTrials.gov Identifier: NCT03086226

13. (salah2025globalsociodemographicclinical pages 12-14): Mohamed Elmuntasir Salah, Michelle L Fearon Scales, Kirlus Habib, Fadila Alhamwi, Suad Abdelwahab, Yassin Ahmed, Manal Mohamed Khalid, Dallas J. Smith, and A. Fahal. Global sociodemographic, clinical, and epidemiological profiling of patients with mycetoma: a systematic review. PLoS neglected tropical diseases, 19 8:e0013217, Aug 2025. URL: https://doi.org/10.1371/journal.pntd.0013217, doi:10.1371/journal.pntd.0013217. This article has 3 citations and is from a domain leading peer-reviewed journal.

14. (salah2025globalsociodemographicclinical pages 1-3): Mohamed Elmuntasir Salah, Michelle L Fearon Scales, Kirlus Habib, Fadila Alhamwi, Suad Abdelwahab, Yassin Ahmed, Manal Mohamed Khalid, Dallas J. Smith, and A. Fahal. Global sociodemographic, clinical, and epidemiological profiling of patients with mycetoma: a systematic review. PLoS neglected tropical diseases, 19 8:e0013217, Aug 2025. URL: https://doi.org/10.1371/journal.pntd.0013217, doi:10.1371/journal.pntd.0013217. This article has 3 citations and is from a domain leading peer-reviewed journal.

15. (fahal2024twodoselevels pages 2-2): AH Fahal, ES Ahmed, and SM Bakhiet. Two dose levels of once-weekly fosravuconazole versus daily itraconazole in combination with surgery in patients with eumycetoma in sudan: a randomised, double …. Unknown journal, 2024.

16. (clark2024eumycetomacausativeagents pages 2-3): Julia E Clark, Hannah Yejin Kim, Wendy W J van de Sande, Brendan McMullan, Paul Verweij, Ana Alastruey-Izquierdo, Arunaloke Chakrabarti, Thomas S Harrison, Felix Bongomin, Roderick J Hay, Rita Oladele, Jutta Heim, Peter Beyer, Marcelo Galas, Siswanto Siswanto, Daniel Argaw Dagne, Felipe Roitberg, Valeria Gigante, Justin Beardsley, Hatim Sati, Jan-Willem Alffenaar, and C Orla Morrissey. Eumycetoma causative agents: a systematic review to inform the world health organization priority list of fungal pathogens. Medical Mycology, Jun 2024. URL: https://doi.org/10.1093/mmy/myae044, doi:10.1093/mmy/myae044. This article has 17 citations and is from a peer-reviewed journal.

17. (clark2024eumycetomacausativeagents pages 3-4): Julia E Clark, Hannah Yejin Kim, Wendy W J van de Sande, Brendan McMullan, Paul Verweij, Ana Alastruey-Izquierdo, Arunaloke Chakrabarti, Thomas S Harrison, Felix Bongomin, Roderick J Hay, Rita Oladele, Jutta Heim, Peter Beyer, Marcelo Galas, Siswanto Siswanto, Daniel Argaw Dagne, Felipe Roitberg, Valeria Gigante, Justin Beardsley, Hatim Sati, Jan-Willem Alffenaar, and C Orla Morrissey. Eumycetoma causative agents: a systematic review to inform the world health organization priority list of fungal pathogens. Medical Mycology, Jun 2024. URL: https://doi.org/10.1093/mmy/myae044, doi:10.1093/mmy/myae044. This article has 17 citations and is from a peer-reviewed journal.

18. (clark2024eumycetomacausativeagents pages 4-5): Julia E Clark, Hannah Yejin Kim, Wendy W J van de Sande, Brendan McMullan, Paul Verweij, Ana Alastruey-Izquierdo, Arunaloke Chakrabarti, Thomas S Harrison, Felix Bongomin, Roderick J Hay, Rita Oladele, Jutta Heim, Peter Beyer, Marcelo Galas, Siswanto Siswanto, Daniel Argaw Dagne, Felipe Roitberg, Valeria Gigante, Justin Beardsley, Hatim Sati, Jan-Willem Alffenaar, and C Orla Morrissey. Eumycetoma causative agents: a systematic review to inform the world health organization priority list of fungal pathogens. Medical Mycology, Jun 2024. URL: https://doi.org/10.1093/mmy/myae044, doi:10.1093/mmy/myae044. This article has 17 citations and is from a peer-reviewed journal.

19. (sande2024anupdatedlist pages 9-12): Wendy W. J. van de Sande and Ahmed H. Fahal. An updated list of eumycetoma causative agents and their differences in grain formation and treatment response. Clinical Microbiology Reviews, Jun 2024. URL: https://doi.org/10.1128/cmr.00034-23, doi:10.1128/cmr.00034-23. This article has 37 citations and is from a highest quality peer-reviewed journal.

20. (sande2024anupdatedlist pages 20-22): Wendy W. J. van de Sande and Ahmed H. Fahal. An updated list of eumycetoma causative agents and their differences in grain formation and treatment response. Clinical Microbiology Reviews, Jun 2024. URL: https://doi.org/10.1128/cmr.00034-23, doi:10.1128/cmr.00034-23. This article has 37 citations and is from a highest quality peer-reviewed journal.

21. (sande2024anupdatedlist pages 6-9): Wendy W. J. van de Sande and Ahmed H. Fahal. An updated list of eumycetoma causative agents and their differences in grain formation and treatment response. Clinical Microbiology Reviews, Jun 2024. URL: https://doi.org/10.1128/cmr.00034-23, doi:10.1128/cmr.00034-23. This article has 37 citations and is from a highest quality peer-reviewed journal.

22. (alhaj2024epidemiologicalobservationsand pages 13-14): Abubakr Abdalla Mohammed Alhaj, Eiman Siddig Ahmed, Abeer Hassan, and Ahmed Hassan Fahal. Epidemiological observations and management challenges in extrapedal mycetoma: a three-decade review of 420 cases. PLOS Neglected Tropical Diseases, 18:e0011841, May 2024. URL: https://doi.org/10.1371/journal.pntd.0011841, doi:10.1371/journal.pntd.0011841. This article has 15 citations and is from a domain leading peer-reviewed journal.

23. (fahal2024twodoselevels pages 10-11): AH Fahal, ES Ahmed, and SM Bakhiet. Two dose levels of once-weekly fosravuconazole versus daily itraconazole in combination with surgery in patients with eumycetoma in sudan: a randomised, double …. Unknown journal, 2024.

24. (scolding2018drugtherapyfor pages 4-5): Peter Scolding, Ahmed Fahal, and Rie R Yotsu. Drug therapy for mycetoma. Cochrane Database of Systematic Reviews, Jul 2018. URL: https://doi.org/10.1002/14651858.cd013082, doi:10.1002/14651858.cd013082. This article has 43 citations and is from a domain leading peer-reviewed journal.

25. (nenoff2015eumycetomaandactinomycetoma pages 8-9): P. Nenoff, W.W.J. van de Sande, A.H. Fahal, D. Reinel, and H. Schöfer. Eumycetoma and actinomycetoma – an update on causative agents, epidemiology, pathogenesis, diagnostics and therapy. Journal of the European Academy of Dermatology and Venereology, 29:1873-1883, Oct 2015. URL: https://doi.org/10.1111/jdv.13008, doi:10.1111/jdv.13008. This article has 179 citations and is from a domain leading peer-reviewed journal.

26. (elkheir2020madurellamycetomatiscausing pages 1-3): Lamis Y. M. Elkheir, Rayan Haroun, Magdi Awadalla Mohamed, and Ahmed Hassan Fahal. Madurella mycetomatis causing eumycetoma medical treatment: the challenges and prospects. PLOS Neglected Tropical Diseases, 14:e0008307, Aug 2020. URL: https://doi.org/10.1371/journal.pntd.0008307, doi:10.1371/journal.pntd.0008307. This article has 58 citations and is from a domain leading peer-reviewed journal.

27. (NCT07506967 chunk 3): Maurice Odiere. Early Detection and AI-Based Management of Skin-Related Neglected Tropical Diseases in Sub-Saharan Africa by Frontline Health Workers. Kenya Medical Research Institute. 2026. ClinicalTrials.gov Identifier: NCT07506967

28. (NCT07506967 chunk 2): Maurice Odiere. Early Detection and AI-Based Management of Skin-Related Neglected Tropical Diseases in Sub-Saharan Africa by Frontline Health Workers. Kenya Medical Research Institute. 2026. ClinicalTrials.gov Identifier: NCT07506967

29. (NCT04401969 chunk 1): Dr Mohamed Osman. Tissue Microenvironment Signatures of the Mycetoma Granuloma. University of Khartoum. 2019. ClinicalTrials.gov Identifier: NCT04401969

30. (NCT06512714 chunk 1):  Mycetoma Retrospective Data Collection. Drugs for Neglected Diseases. 2024. ClinicalTrials.gov Identifier: NCT06512714

31. (NCT07506967 chunk 1): Maurice Odiere. Early Detection and AI-Based Management of Skin-Related Neglected Tropical Diseases in Sub-Saharan Africa by Frontline Health Workers. Kenya Medical Research Institute. 2026. ClinicalTrials.gov Identifier: NCT07506967
