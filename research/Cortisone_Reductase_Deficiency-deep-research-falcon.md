---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T01:05:19.666935'
end_time: '2026-05-10T01:31:06.562166'
duration_seconds: 1546.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cortisone Reductase Deficiency
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Cortisone Reductase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cortisone Reductase Deficiency** covering all of the
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
- **Disease Name:** Cortisone Reductase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cortisone Reductase Deficiency** covering all of the
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


## Cortisone Reductase Deficiency (CRD): Comprehensive Disease Characteristics Report

### Target disease
- **Disease name:** Cortisone Reductase Deficiency (CRD)
- **Category:** Mendelian endocrine/metabolic disorder (rare)

> **Important scope note:** The retrieved evidence base contains strong primary literature for CRD/“apparent” CRD but did **not** include authoritative MONDO/Orphanet/ICD/MeSH identifiers in accessible full text. Where those identifiers are required, this report explicitly marks them as **not available in the retrieved sources**.

---

## 1. Disease information

### 1.1 Concise overview (current understanding)
Cortisone reductase deficiency (CRD) is a rare disorder of **impaired regeneration of active cortisol from inactive cortisone** due to deficient **11β-hydroxysteroid dehydrogenase type 1 (11β-HSD1)** reductase function in vivo, producing increased cortisol clearance and compensatory activation of the hypothalamic–pituitary–adrenal (HPA) axis with consequent **ACTH-driven adrenal androgen excess**. (g2008steroidbiomarkersand pages 1-2, draper2003mutationsinthe pages 1-2)

A clinically overlapping entity, **apparent cortisone reductase deficiency (ACRD)**, results from defects in the **cofactor system** that supplies NADPH to 11β-HSD1 (notably **H6PD** in the endoplasmic reticulum), leading to a functional loss of 11β-HSD1 reductase directionality. (zajkowska2017afollowuphistory pages 1-2, white2018alterationsofcortisol pages 3-4)

### 1.2 Key identifiers (as available in retrieved sources)
- **OMIM/MIM (disease):** **CRD MIM #604931** (example cited in an OMIM/medical genetics context). (zajkowska2017afollowuphistory pages 1-2)
- **OMIM (genes):** **HSD11B1 (MIM *600713)** and **H6PD (MIM *138090)** referenced in the same OMIM example context. (zajkowska2017afollowuphistory pages 1-2)
- **“Cortisone reductase type 2 deficiency / CRD2”:** a 2024 case report cites **MIM #614662** in association with HSD11B1 frameshift disease presentation. (almache2024migueldelos pages 2-5)
- **MONDO / Orphanet / ICD-10/ICD-11 / MeSH:** **Not identified in retrieved full-text evidence** (cannot be asserted from current tool outputs).

### 1.3 Synonyms / alternative names
- Cortisone reductase deficiency (CRD) (draper2003mutationsinthe pages 1-2, g2008steroidbiomarkersand pages 1-2)
- Apparent cortisone reductase deficiency (ACRD) (zajkowska2017afollowuphistory pages 1-2, white2018alterationsofcortisol pages 3-4)
- Apparent cortisone reductase deficiency / “AERD” (historical usage in early case literature) (biasonlauber2000apparentcortisonereductase pages 1-3)

### 1.4 Evidence source type
Most disease knowledge is derived from **case reports/series**, and **mechanistic genetic studies**, with synthesis in expert reviews. (draper2003mutationsinthe pages 1-2, g2008steroidbiomarkersand pages 1-2, biasonlauber2000apparentcortisonereductase pages 1-3)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal mechanism:** Reduced 11β-HSD1-dependent cortisone→cortisol regeneration in tissues, due to:
1) **HSD11B1** variants that reduce 11β-HSD1 expression or activity, and/or (draper2003mutationsinthe pages 1-2, lawson2011cortisonereductasedeficiencyassociated pages 1-2)
2) **H6PD** loss-of-function variants impairing ER **NADPH generation**, shifting/abrogating 11β-HSD1 oxoreductase activity in vivo. (g2008steroidbiomarkersand pages 1-2, seckl202411β‐hydroxysteroiddehydrogenaseand pages 2-2)

**Mechanistic causal chain (human disease):** impaired tissue cortisol regeneration → increased cortisol clearance → reduced negative feedback → increased ACTH drive → increased adrenal androgen (and cortisol) production → clinical hyperandrogenism/precocious puberty or PCOS-like phenotype. (g2008steroidbiomarkersand pages 1-2, white2018alterationsofcortisol pages 3-4)

### 2.2 Genetic risk factors / causal variants

#### Causal genes
- **HSD11B1** (encodes 11β-HSD1) (lawson2011cortisonereductasedeficiencyassociated pages 1-2)
- **H6PD** (encodes hexose-6-phosphate dehydrogenase; provides NADPH in ER lumen) (g2008steroidbiomarkersand pages 1-2)

#### Pathogenic variants (examples explicitly stated in retrieved evidence)
- **H6PD** inactivating variants identified in CRD cohorts include **R109AfsX3**, **Y316X**, **G359D**, and compound heterozygous combinations including **D620fsX3** (as reported in the JCEM 2008 cohort). (g2008steroidbiomarkersand pages 1-2)
- **HSD11B1** coding variants reported in PNAS 2011: **c.409C>T (R137C)** and **c.561G>T (K187N)**, heterozygous and maternally inherited in those families. (lawson2011cortisonereductasedeficiencyassociated pages 1-2, lawson2011cortisonereductasedeficiencyassociated pages 1-1)
- **HSD11B1** frameshift in a 2024 pediatric case: **HSD11B1:c.513delG:p.(Ala172Leufs*47)** identified by whole-exome sequencing. (almache2024migueldelos pages 2-5)

#### Inheritance patterns (as supported by retrieved sources)
- A **digenic/triallelic** interaction model (HSD11B1 intronic variants + H6PD mutations) was proposed in the 2003 Nature Genetics report. (draper2003mutationsinthe pages 1-2)
- A recessive pattern is strongly suggested in the 2008 JCEM series by **homozygous** and **compound heterozygous** H6PD loss-of-function genotypes. (g2008steroidbiomarkersand pages 1-2)
- A heterozygous/maternal transmission pattern was described in PNAS 2011 for some HSD11B1 missense cases (mothers shared the biochemical phenotype). (lawson2011cortisonereductasedeficiencyassociated pages 1-2)

### 2.3 Environmental risk/protective factors and GxE
No disease-specific environmental risk/protective factors or gene–environment interactions were identified in the retrieved evidence; CRD/ACRD is primarily described as a **genetic/cofactor-enzyme defect**. (white2018alterationsofcortisol pages 3-4, g2008steroidbiomarkersand pages 1-2)

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum
CRD/ACRD phenotypes cluster around **ACTH-driven adrenal androgen excess** and related reproductive/androgenic manifestations:
- **Females:** hirsutism, acne, oligomenorrhea/oligo-amenorrhea, anovulation and infertility; androgenic alopecia in some cases. (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23, g2008steroidbiomarkersand pages 1-2)
- **Males/children:** precocious puberty or **precocious pseudopuberty**, precocious pubarche, virilization, advanced bone age. (zajkowska2017afollowuphistory pages 1-2, almache2024migueldelos pages 1-2)

Additional reported findings/associations include adrenal hyperplasia in at least one adult case, and mild hypertension in that report. (biasonlauber2000apparentcortisonereductase pages 1-3)

### 3.2 Age of onset, severity, progression
- Typical female presentation: adolescence or early adulthood (reviewed case aggregate), but also midlife presentations occur in case series (e.g., ages 44 and 55 in one report set). (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23, g2008steroidbiomarkersand pages 1-2)
- Pediatric male presentation: childhood onset with precocious pubarche/pseudopuberty; a 2017 follow-up report describes diagnosis at ~7 years with advanced bone age and androgen excess. (zajkowska2017afollowuphistory pages 1-2)
- A 2024 case report highlights progression from peripheral androgen excess to **secondary central precocious puberty** with sustained androgen exposure. (almache2024migueldelos pages 1-2)

### 3.3 Phenotype frequencies
Robust per-phenotype frequency percentages are not available because evidence is predominantly case-based. However, an endocrine review summarized that among **11 described cases** (at that time) the majority were female. (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23)

### 3.4 Quality-of-life impact
Direct standardized QoL instruments were not reported in retrieved sources. Based on clinical phenotype, QoL impact is expected through infertility, hirsutism/acne/alopecia, and early puberty with psychosocial and growth consequences. (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23, almache2024migueldelos pages 5-5)

### 3.5 Suggested HPO terms (non-exhaustive; mapped from retrieved phenotypes)
- **Hyperandrogenism** (HP:0000843)
- **Hirsutism** (HP:0001007)
- **Acne** (HP:0001061)
- **Oligomenorrhea / Amenorrhea** (HP:0000876 / HP:0000869)
- **Infertility** (HP:0000789)
- **Androgenic alopecia** (HP:0002210)
- **Precocious puberty** (HP:0000826)
- **Precocious pubarche** (HP:0008080)
- **Advanced bone age** (HP:0002808)

(These HPO IDs are standard ontology mappings; the underlying clinical features are supported by the cited sources.) (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23, zajkowska2017afollowuphistory pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Core molecular concept
11β-HSD1 is an ER-localized enzyme that **predominantly acts as a reductase in vivo** to regenerate cortisol from cortisone. A key modern concept emphasized by Seckl (2024) is that the **directionality** of 11β-HSD1 is governed by **co-localized H6PDH**, which generates luminal NADPH; without sufficient NADPH, 11β-HSD1 can lose reductase directionality. (seckl202411β‐hydroxysteroiddehydrogenaseand pages 2-2)

### 4.2 Protein dysfunction and functional consequence
- Loss of H6PD function reduces NADPH, impairing 11β-HSD1 reductase activity; in vivo this manifests as markedly low urinary cortisol-derived metabolites relative to cortisone-derived metabolites. (g2008steroidbiomarkersand pages 1-2, draper2003mutationsinthe media 390e56cf)
- HSD11B1 missense variants can reduce enzyme activity and show dominant-negative behavior in co-expression (reported in PNAS 2011). (lawson2011cortisonereductasedeficiencyassociated pages 1-1)

### 4.3 Suggested GO biological process terms (examples)
- **Glucocorticoid metabolic process** (GO:0008211)
- **Steroid metabolic process** (GO:0008202)
- **Cortisol biosynthetic/metabolic process** (general mapping; supported mechanistically by tissue regeneration described) (seckl202411β‐hydroxysteroiddehydrogenaseand pages 2-2)

### 4.4 Suggested GO cellular component terms
- **Endoplasmic reticulum lumen** (GO:0005788) (H6PDH NADPH generation locale)
- **Endoplasmic reticulum membrane** (GO:0005789) (11β-HSD1 localization concept)

### 4.5 Suggested Cell Ontology (CL) terms (inferred from expression sites discussed in 2024 expert review)
Seckl (2024) emphasizes 11β-HSD1 abundance in liver, adipose, vasculature, muscle, inflammatory cells, gonads and brain. Candidate CL terms include:
- Hepatocyte (CL:0000182)
- Adipocyte (CL:0000136)
- Macrophage (CL:0000235)
- Neuron (CL:0000540)

(These are plausible mechanistic cell types; clinical disease manifestations are primarily adrenal axis-driven.) (seckl202411β‐hydroxysteroiddehydrogenaseand pages 2-2)

---

## 5. Environmental information
No specific environmental or infectious contributors were identified in retrieved sources. CRD/ACRD is described as a genetic/cofactor-enzyme defect with endocrine downstream consequences. (white2018alterationsofcortisol pages 3-4)

---

## 6. Mechanism / pathophysiology

### 6.1 Molecular pathway summary
- **Upstream defect:** HSD11B1 loss-of-function and/or H6PD loss-of-function → reduced 11β-HSD1 oxoreductase activity (cortisone→cortisol). (g2008steroidbiomarkersand pages 1-2, seckl202411β‐hydroxysteroiddehydrogenaseand pages 2-2)
- **Intermediate:** increased metabolic clearance of cortisol; reduced tissue cortisol regeneration. (g2008steroidbiomarkersand pages 1-2)
- **Downstream endocrine compensation:** increased ACTH drive → adrenal hyperandrogenism → PCOS-like phenotype (women) or precocious puberty/pubarche (children). (g2008steroidbiomarkersand pages 1-2, tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23)

### 6.2 Biochemical abnormalities (key measurable signature)
A defining biochemical feature is a **markedly reduced urinary tetrahydrocortisol (THF + allo-THF or THF + 5α-THF) to tetrahydrocortisone (THE) ratio**, often around **0.03–0.05** compared with reference ~**0.7–1.2**. (draper2003mutationsinthe pages 1-2, g2008steroidbiomarkersand pages 1-2, draper2003mutationsinthe media 390e56cf)

The key diagnostic table in Draper et al. shows affected ratios **0.03–0.04** vs reference **0.7–1.1**. (draper2003mutationsinthe media 390e56cf)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
- **Endocrine system:** HPA axis (hypothalamus/pituitary signaling), adrenal androgen production (functional outcome). (g2008steroidbiomarkersand pages 1-2)
- **Reproductive system:** ovulatory dysfunction/infertility in females; pubertal development axis in children. (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23, almache2024migueldelos pages 5-5)

### 7.2 Suggested UBERON terms (examples)
- Adrenal gland (UBERON:0002369)
- Pituitary gland (UBERON:0000007)
- Ovary (UBERON:0000992)
- Testis (UBERON:0000473)

---

## 8. Temporal development

- **Onset:** childhood (boys with precocious pubarche/pseudopuberty) or adolescence/early adulthood (women with hyperandrogenism/infertility). (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23, zajkowska2017afollowuphistory pages 1-2)
- **Course:** chronic endocrine imbalance; androgen excess can drive progression (e.g., peripheral → central precocious puberty in sustained pediatric cases). (almache2024migueldelos pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology
CRD/ACRD is described as **extremely rare**; case-based counts include:
- ~**11 cases** described as of an Endocrine Reviews synthesis (majority female). (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23)
- A later case report review states “around **16 cases**” in literature. (zajkowska2017afollowuphistory pages 1-2)

No reliable population prevalence/incidence estimates were found in the retrieved evidence.

### 9.2 Inheritance
See Section 2.2 (digenic/triallelic model in early report; recessive H6PD LOF patterns in later cohort; heterozygous HSD11B1 families reported). (draper2003mutationsinthe pages 1-2, lawson2011cortisonereductasedeficiencyassociated pages 1-2, g2008steroidbiomarkersand pages 1-2)

---

## 10. Diagnostics

### 10.1 Core clinical tests and biomarkers
- **Urinary steroid metabolomics by GC/MS**: hallmark low **THF+5α-THF/THE** (or THF+allo-THF/THE) ratio. Thresholds reported include **<0.1** (typical CRD) with reference ranges approximately **0.7–1.2**, and individual patient ratios ~**0.03–0.05**. (g2008steroidbiomarkersand pages 1-2, zajkowska2017afollowuphistory pages 1-2)
- The Nature Genetics table demonstrates ratios **0.03–0.04** vs reference **0.7–1.1**. (draper2003mutationsinthe media 390e56cf)
- Additional urinary metrics: cortols/cortolones ratio used as a measure of 11β-HSD1 activity. (lawson2011cortisonereductasedeficiencyassociated pages 1-1)
- Blood tests in reported cases: plasma androgens (DHEAS, androstenedione, testosterone), and sometimes **17-hydroxyprogesterone** elevations. (zajkowska2017afollowuphistory pages 1-2)

### 10.2 Genetic testing
- **Targeted sequencing** of **H6PD** and **HSD11B1** is supported by cohort studies. (g2008steroidbiomarkersand pages 1-2)
- **Whole-exome sequencing (WES)** enabled diagnosis in the 2024 pediatric CRD2 report with identification of an HSD11B1 frameshift. (almache2024migueldelos pages 2-5)

### 10.3 Differential diagnosis
Because CRD/ACRD can mimic common hyperandrogenism disorders, differential diagnosis includes:
- **Polycystic ovary syndrome (PCOS)** phenocopy (explicitly noted as a clinical resemblance). (draper2003mutationsinthe pages 1-2)
- **Congenital adrenal hyperplasia** (e.g., 21-hydroxylase deficiency) as a diagnostic alternative in hyperandrogenic/precocious puberty presentations.

---

## 11. Outcome / prognosis

Formal survival/mortality statistics were not identified (rare, non-lethal endocrine disorder). Reported long-term outcomes include attainment of near-target adult height in one male pediatric ACRD follow-up when treatment was titrated carefully, with mild therapy-related adverse effects noted. (zajkowska2017afollowuphistory pages 5-6)

Key prognosis determinants appear to include:
- Degree and duration of androgen excess (bone age advancement)
- Side effects of chronic glucocorticoid suppression strategies (e.g., risk of iatrogenic Cushingoid effects). (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23, zajkowska2017afollowuphistory pages 5-6)

---

## 12. Treatment

### 12.1 Mechanism-based endocrine management (real-world implementations)
**Goal:** suppress ACTH-driven adrenal androgen excess and manage consequences (puberty progression, fertility, androgenic symptoms).

- **Dexamethasone**: suppresses ACTH and androgens; serum androgens fall with dexamethasone in reviewed cases. (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23)
- **Hydrocortisone**: may be ineffective in ACRD due to rapid metabolism to cortisone; a pediatric ACRD follow-up described ineffective hydrocortisone and improved biochemical control after switching to dexamethasone. (zajkowska2017afollowuphistory pages 2-4)
- **Antiandrogen strategies:** prednisone plus antiandrogens (e.g., cyproterone acetate, spironolactone) improved symptoms in an adult female case. (biasonlauber2000apparentcortisonereductase pages 1-3)
- **Precocious puberty regimens (2024 case):** GnRH analogue (triptorelin), antiandrogen (bicalutamide), aromatase inhibitor (letrozole) and glucocorticoid adjustments in a child with CRD2. (almache2024migueldelos pages 1-2, almache2024migueldelos pages 5-5)

### 12.2 Suggested MAXO terms (examples)
- Glucocorticoid therapy / ACTH suppression (MAXO concept: corticosteroid therapy)
- Gonadotropin-releasing hormone agonist therapy (for central precocious puberty)
- Aromatase inhibitor therapy
- Antiandrogen therapy

(These are standard intervention categories; the specific clinical implementations are supported by cited case literature.) (zajkowska2017afollowuphistory pages 2-4, almache2024migueldelos pages 5-5)

### 12.3 Clinical trials
No CRD/ACRD-specific interventional trials were identified in the clinical trial search results available in this run. (clinical trials tool output: none relevant)

Related translational landscape: Seckl (2024) summarizes broad development of **11β-HSD1 inhibitors** in other diseases, noting that metabolic benefits in humans have often been modest and “the magnitude of benefits has been insufficient to support progression” for metabolic indications, while other indications (including brain-related) remain under evaluation. (seckl202411β‐hydroxysteroiddehydrogenaseand pages 3-4)

---

## 13. Prevention
No primary prevention is described (genetic disorder). Practical prevention pertains to:
- **Genetic counseling** and **cascade testing** in families once a pathogenic variant is identified.

No newborn screening or population screening strategies were found in retrieved sources.

---

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in the retrieved evidence.

---

## 15. Model organisms
The retrieved evidence base for this run did not include detailed CRD-specific model organism phenotyping text, though it references broader mouse mechanistic work in reviews and pathway studies (e.g., H6PD knockout physiology is discussed in related literature outside the disease report focus). (white2018alterationsofcortisol pages 3-4)

---

## Recent developments (2023–2024 priority) and expert analysis

### 2024 expert synthesis: mechanistic refinement and translational outlook
Seckl (2024, *Journal of Internal Medicine*, publication month **Nov 2024**, URL https://doi.org/10.1111/joim.13741) emphasizes that 11β-HSD1 is a tissue amplifier of glucocorticoid action and that its reductase directionality depends on ER NADPH supply by H6PDH. (seckl202411β‐hydroxysteroiddehydrogenaseand pages 2-2)

Seckl (2024) provides a frank translational assessment: although 11β-HSD1 inhibitors show metabolic improvements in some human trials, clinical impact has often been insufficient for progression in metabolic disease development programs. (seckl202411β‐hydroxysteroiddehydrogenaseand pages 3-4)

### 2024 case-based expansion of clinical spectrum
A 2024 pediatric case report (publication year **2024**; details as retrieved) describes “cortisone reductase type 2 deficiency” diagnosed by **WES** with HSD11B1 frameshift **c.513delG:p.(Ala172Leufs*47)** and complex management of precocious puberty (GnRHa, aromatase inhibitor, antiandrogen, and corticosteroid changes due to Cushingoid signs). (almache2024migueldelos pages 2-5, almache2024migueldelos pages 5-5)

---

## Key quantitative statistics and data (from recent/primary studies)
- **Urinary steroid ratio (diagnostic):** tetrahydrocortisols/tetrahydrocortisone reference ~**0.7–1.1**; CRD examples **0.03–0.04**. (draper2003mutationsinthe media 390e56cf)
- **Diagnostic threshold (cohort statement):** THF + 5α-THF / THE typically **<0.1** in CRD vs reference **0.7–1.2**. (g2008steroidbiomarkersand pages 1-2)
- **Rarity counts:** ~**11 cases** described as of a 2004 synthesis; ~**16 cases** noted in a 2017 review/case report context. (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23, zajkowska2017afollowuphistory pages 1-2)

---

## Comparative summary table (CRD vs ACRD and variants)

| Entity | Causal gene(s) | Inheritance model reported | Core biochemical signature (urinary steroid ratios) | Key clinical features | Key references (year, journal, DOI) |
|---|---|---|---|---|---|
| CRD | **HSD11B1** with interacting **H6PD** variants reported in early cases; later reports also identified **H6PD** inactivating mutations without enzyme-affecting **HSD11B1** mutations in the studied cohort (draper2003mutationsinthe pages 1-2, g2008steroidbiomarkersand pages 1-2) | **Digenic/triallelic model** proposed in 2003 involving intronic **HSD11B1** variants plus **H6PD** mutations; 2008 cohort showed **3 homozygous** and **1 compound heterozygous H6PD** genotypes, consistent with recessive inheritance in those families (draper2003mutationsinthe pages 1-2, g2008steroidbiomarkersand pages 1-2) | Markedly reduced urinary **tetrahydrocortisols/tetrahydrocortisone** ratio; reported values **0.03, 0.032, 0.04** vs reference **0.7–1.1**; 2008 review/cohort states **THF + 5α-THF / THE <0.1** vs reference **0.7–1.2** (draper2003mutationsinthe pages 1-2, g2008steroidbiomarkersand pages 1-2, draper2003mutationsinthe media 390e56cf) | ACTH-driven adrenal androgen excess; hyperandrogenism with **hirsutism, oligo-/amenorrhea, infertility** in females and **premature pseudopuberty** in males; cortisol regenerated poorly from cortisone (g2008steroidbiomarkersand pages 1-2, g2008steroidbiomarkersand pages 2-3, draper2003mutationsinthe pages 1-2) | **Draper et al.** 2003, *Nature Genetics*, doi: **10.1038/ng1214**; **Lavery et al.** 2008, *J Clin Endocrinol Metab*, doi: **10.1210/jc.2008-0743** (draper2003mutationsinthe pages 1-2, g2008steroidbiomarkersand pages 1-2) |
| ACRD | **H6PD** (hexose-6-phosphate dehydrogenase), impairing NADPH supply to 11β-HSD1; Horm Res Paediatr 2018 also notes apparent cortisone reductase deficiency can result from **HSD11B1** loss-of-function or **H6PD** defects affecting 11β-HSD1 activity (zajkowska2017afollowuphistory pages 1-2, white2018alterationsofcortisol pages 3-4) | 2017 case report identifies ACRD as resulting from **inactivating H6PD mutations**; no explicit Mendelian label quoted in the snippet, but mutation-based disease mechanism is stated (zajkowska2017afollowuphistory pages 1-2) | Very low **THF+allo-THF/THE** (or **THF+5α-THF/THE**) ratio; 2017 example **0.021** with normal approximately **0.7–1.2**; hydrocortisone did not normalize the ratio, whereas dexamethasone improved biochemical control (zajkowska2017afollowuphistory pages 1-2, zajkowska2017afollowuphistory pages 2-4) | Adrenal androgen excess with **precocious pubarche**, elevated plasma androgens, increased **17-hydroxyprogesterone**; rare hyperandrogenic syndrome in women or children (zajkowska2017afollowuphistory pages 1-2, white2018alterationsofcortisol pages 3-4) | **Zajkowska et al.** 2017, *Pediatr Endocrinol Diabetes Metab*, doi: **10.18544/pedm-23.01.0073**; **White** 2018, *Horm Res Paediatr*, doi: **10.1159/000485508** (zajkowska2017afollowuphistory pages 1-2, white2018alterationsofcortisol pages 3-4) |
| CRD associated with heterozygous **HSD11B1** variants | **HSD11B1** missense variants **c.409C>T (R137C)** and **c.561G>T (K187N)** reported in two cases; **H6PD** normal in those cases (lawson2011cortisonereductasedeficiencyassociated pages 1-2) | **Heterozygous, maternally inherited** biochemical phenotype reported; mothers showed urine biochemistry similar to affected offspring, fathers were normal (lawson2011cortisonereductasedeficiencyassociated pages 1-2) | The provided snippet links these cases to abnormal urinary biochemistry characteristic of cortisone-reductase deficiency, but does not restate exact ratio values in the excerpt (lawson2011cortisonereductasedeficiencyassociated pages 1-2) | CRD phenotype as in prior reports; article title and context associate these cases with cortisone-reductase deficiency (lawson2011cortisonereductasedeficiencyassociated pages 1-2) | **Lawson et al.** 2011, *PNAS*, doi: **10.1073/pnas.1014934108** (lawson2011cortisonereductasedeficiencyassociated pages 1-2) |


*Table: This table compares cortisone reductase deficiency and apparent cortisone reductase deficiency using only the provided evidence snippets. It highlights genes, reported inheritance patterns, diagnostic urinary steroid signatures, clinical manifestations, and the most relevant supporting references.*

---

## Visual evidence (urinary steroid ratios)
A key diagnostic table from the landmark Nature Genetics report shows dramatically reduced urinary tetrahydrocortisols/tetrahydrocortisone ratios in CRD vs reference range. (draper2003mutationsinthe media 390e56cf)

---

## Reference URLs (selected)
- Draper et al., *Nature Genetics* (Aug 2003): https://doi.org/10.1038/ng1214 (draper2003mutationsinthe pages 1-2)
- Lavery et al., *J Clin Endocrinol Metab* (Oct 2008): https://doi.org/10.1210/jc.2008-0743 (g2008steroidbiomarkersand pages 1-2)
- Lawson et al., *PNAS* (Feb 2011): https://doi.org/10.1073/pnas.1014934108 (lawson2011cortisonereductasedeficiencyassociated pages 1-2)
- Zajkowska et al., *Pediatr Endocrinol Diabetes Metab* (Jan 2017): https://doi.org/10.18544/pedm-23.01.0073 (zajkowska2017afollowuphistory pages 1-2)
- White, *Horm Res Paediatr* (May 2018): https://doi.org/10.1159/000485508 (white2018alterationsofcortisol pages 3-4)
- Seckl, *J Intern Med* (Nov 2024): https://doi.org/10.1111/joim.13741 (seckl202411β‐hydroxysteroiddehydrogenaseand pages 1-2)



References

1. (g2008steroidbiomarkersand pages 1-2): G G Lavery, E A Walker, A Tiganescu, J P Ride, C H L Shackleton, J W Tomlinson, J M C Connell, D W Ray, A Biason-Lauber, E M Malunowicz, W Arlt, and P M Stewart. Steroid biomarkers and genetic studies reveal inactivating mutations in hexose-6-phosphate dehydrogenase in patients with cortisone reductase deficiency. The Journal of clinical endocrinology and metabolism, 93 10:3827-32, Oct 2008. URL: https://doi.org/10.1210/jc.2008-0743, doi:10.1210/jc.2008-0743. This article has 109 citations.

2. (draper2003mutationsinthe pages 1-2): Nicole Draper, Elizabeth A Walker, Iwona J Bujalska, Jeremy W Tomlinson, Susan M Chalder, Wiebke Arlt, Gareth G Lavery, Oliver Bedendo, David W Ray, Ian Laing, Ewa Malunowicz, Perrin C White, Martin Hewison, Philip J Mason, John M Connell, Cedric H L Shackleton, and Paul M Stewart. Mutations in the genes encoding 11β-hydroxysteroid dehydrogenase type 1 and hexose-6-phosphate dehydrogenase interact to cause cortisone reductase deficiency. Nature Genetics, 34:434-439, Aug 2003. URL: https://doi.org/10.1038/ng1214, doi:10.1038/ng1214. This article has 376 citations and is from a highest quality peer-reviewed journal.

3. (zajkowska2017afollowuphistory pages 1-2): Adrianna Zajkowska, Marta Rydzewska, Katarzyna Wojtkielewicz, Janusz Pomaski, Tomasz Romer, and Artur Bossowski. A follow-up history of young man with apparent cortisone reductase deficiency (acrd) – several years after diagnosis. Pediatric Endocrinology Diabetes and Metabolism, 23:42-48, Jan 2017. URL: https://doi.org/10.18544/pedm-23.01.0073, doi:10.18544/pedm-23.01.0073. This article has 2 citations.

4. (white2018alterationsofcortisol pages 3-4): Perrin C. White. Alterations of cortisol metabolism in human disorders. Hormone Research in Paediatrics, 89:320-330, May 2018. URL: https://doi.org/10.1159/000485508, doi:10.1159/000485508. This article has 31 citations and is from a peer-reviewed journal.

5. (almache2024migueldelos pages 2-5): ON Almache, RL de Lama, and EC Tejada. Miguel de los santos la torre, pamela azabache tafur. case report:“precocious puberty in a child with cortisone reductase type 2 deficiency”. Unknown journal, 2024.

6. (biasonlauber2000apparentcortisonereductase pages 1-3): Anna Biason-Lauber, Stephan L. Suter, Cedric H.L. Shackleton, and Milo Zachmann. Apparent cortisone reductase deficiency: a rare cause of hyperandrogenemia and hypercortisolism. Hormone Research in Paediatrics, 53:260-266, Nov 2000. URL: https://doi.org/10.1159/000023577, doi:10.1159/000023577. This article has 49 citations and is from a peer-reviewed journal.

7. (lawson2011cortisonereductasedeficiencyassociated pages 1-2): Alexander J. Lawson, Elizabeth A. Walker, Gareth G. Lavery, Iwona J. Bujalska, Beverly Hughes, Wiebke Arlt, Paul M. Stewart, and Jonathan P. Ride. Cortisone-reductase deficiency associated with heterozygous mutations in 11β-hydroxysteroid dehydrogenase type 1. Proceedings of the National Academy of Sciences, 108:4111-4116, Feb 2011. URL: https://doi.org/10.1073/pnas.1014934108, doi:10.1073/pnas.1014934108. This article has 74 citations and is from a highest quality peer-reviewed journal.

8. (seckl202411β‐hydroxysteroiddehydrogenaseand pages 2-2): Jonathan Seckl. 11β‐hydroxysteroid dehydrogenase and the brain: not (yet) lost in translation. Journal of Internal Medicine, 295:20-37, Nov 2024. URL: https://doi.org/10.1111/joim.13741, doi:10.1111/joim.13741. This article has 41 citations and is from a domain leading peer-reviewed journal.

9. (lawson2011cortisonereductasedeficiencyassociated pages 1-1): Alexander J. Lawson, Elizabeth A. Walker, Gareth G. Lavery, Iwona J. Bujalska, Beverly Hughes, Wiebke Arlt, Paul M. Stewart, and Jonathan P. Ride. Cortisone-reductase deficiency associated with heterozygous mutations in 11β-hydroxysteroid dehydrogenase type 1. Proceedings of the National Academy of Sciences, 108:4111-4116, Feb 2011. URL: https://doi.org/10.1073/pnas.1014934108, doi:10.1073/pnas.1014934108. This article has 74 citations and is from a highest quality peer-reviewed journal.

10. (tomlinson200411βhydroxysteroiddehydrogenasetype pages 22-23): Jeremy W. Tomlinson, Elizabeth A. Walker, Iwona J. Bujalska, Nicole Draper, Gareth G. Lavery, Mark S. Cooper, Martin Hewison, and Paul M. Stewart. 11β-hydroxysteroid dehydrogenase type 1: a tissue-specific regulator of glucocorticoid response. Endocrine Reviews, 25:831-866, Oct 2004. URL: https://doi.org/10.1210/er.2003-0031, doi:10.1210/er.2003-0031. This article has 1273 citations and is from a domain leading peer-reviewed journal.

11. (almache2024migueldelos pages 1-2): ON Almache, RL de Lama, and EC Tejada. Miguel de los santos la torre, pamela azabache tafur. case report:“precocious puberty in a child with cortisone reductase type 2 deficiency”. Unknown journal, 2024.

12. (almache2024migueldelos pages 5-5): ON Almache, RL de Lama, and EC Tejada. Miguel de los santos la torre, pamela azabache tafur. case report:“precocious puberty in a child with cortisone reductase type 2 deficiency”. Unknown journal, 2024.

13. (draper2003mutationsinthe media 390e56cf): Nicole Draper, Elizabeth A Walker, Iwona J Bujalska, Jeremy W Tomlinson, Susan M Chalder, Wiebke Arlt, Gareth G Lavery, Oliver Bedendo, David W Ray, Ian Laing, Ewa Malunowicz, Perrin C White, Martin Hewison, Philip J Mason, John M Connell, Cedric H L Shackleton, and Paul M Stewart. Mutations in the genes encoding 11β-hydroxysteroid dehydrogenase type 1 and hexose-6-phosphate dehydrogenase interact to cause cortisone reductase deficiency. Nature Genetics, 34:434-439, Aug 2003. URL: https://doi.org/10.1038/ng1214, doi:10.1038/ng1214. This article has 376 citations and is from a highest quality peer-reviewed journal.

14. (zajkowska2017afollowuphistory pages 5-6): Adrianna Zajkowska, Marta Rydzewska, Katarzyna Wojtkielewicz, Janusz Pomaski, Tomasz Romer, and Artur Bossowski. A follow-up history of young man with apparent cortisone reductase deficiency (acrd) – several years after diagnosis. Pediatric Endocrinology Diabetes and Metabolism, 23:42-48, Jan 2017. URL: https://doi.org/10.18544/pedm-23.01.0073, doi:10.18544/pedm-23.01.0073. This article has 2 citations.

15. (zajkowska2017afollowuphistory pages 2-4): Adrianna Zajkowska, Marta Rydzewska, Katarzyna Wojtkielewicz, Janusz Pomaski, Tomasz Romer, and Artur Bossowski. A follow-up history of young man with apparent cortisone reductase deficiency (acrd) – several years after diagnosis. Pediatric Endocrinology Diabetes and Metabolism, 23:42-48, Jan 2017. URL: https://doi.org/10.18544/pedm-23.01.0073, doi:10.18544/pedm-23.01.0073. This article has 2 citations.

16. (seckl202411β‐hydroxysteroiddehydrogenaseand pages 3-4): Jonathan Seckl. 11β‐hydroxysteroid dehydrogenase and the brain: not (yet) lost in translation. Journal of Internal Medicine, 295:20-37, Nov 2024. URL: https://doi.org/10.1111/joim.13741, doi:10.1111/joim.13741. This article has 41 citations and is from a domain leading peer-reviewed journal.

17. (g2008steroidbiomarkersand pages 2-3): G G Lavery, E A Walker, A Tiganescu, J P Ride, C H L Shackleton, J W Tomlinson, J M C Connell, D W Ray, A Biason-Lauber, E M Malunowicz, W Arlt, and P M Stewart. Steroid biomarkers and genetic studies reveal inactivating mutations in hexose-6-phosphate dehydrogenase in patients with cortisone reductase deficiency. The Journal of clinical endocrinology and metabolism, 93 10:3827-32, Oct 2008. URL: https://doi.org/10.1210/jc.2008-0743, doi:10.1210/jc.2008-0743. This article has 109 citations.

18. (seckl202411β‐hydroxysteroiddehydrogenaseand pages 1-2): Jonathan Seckl. 11β‐hydroxysteroid dehydrogenase and the brain: not (yet) lost in translation. Journal of Internal Medicine, 295:20-37, Nov 2024. URL: https://doi.org/10.1111/joim.13741, doi:10.1111/joim.13741. This article has 41 citations and is from a domain leading peer-reviewed journal.
