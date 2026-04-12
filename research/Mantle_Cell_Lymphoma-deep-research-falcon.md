---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T19:53:09.636746'
end_time: '2026-04-05T20:03:52.215554'
duration_seconds: 642.58
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mantle Cell Lymphoma
  mondo_id: ''
  category: ''
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
- **Disease Name:** Mantle Cell Lymphoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Mantle Cell Lymphoma** covering all of the
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
- **Disease Name:** Mantle Cell Lymphoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Mantle Cell Lymphoma** covering all of the
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


# Mantle Cell Lymphoma (MCL) — Disease Characteristics Research Report (2023–2024 prioritized)

## Target Disease
- **Disease name:** Mantle cell lymphoma (MCL)
- **Category:** Mature B-cell non-Hodgkin lymphoma (B-NHL) (harmanen2024mantlecelllymphoma pages 31-34, lopez2024biologicalandclinical pages 1-2)
- **MONDO / MeSH / ICD / Orphanet / OMIM IDs:** Not recoverable from the retrieved corpus/tools in this run; therefore not asserted here.
- **Evidence provenance note:** Statements below are based on aggregated, disease-level resources (reviews, registries, clinical studies) rather than individual EHRs unless explicitly stated.

## 1. Disease information
### Overview (current understanding)
Mantle cell lymphoma is a **rare mature B-cell neoplasm** arising from the **mantle zone of lymphoid follicles** (harmanen2024mantlecelllymphoma pages 31-34). Contemporary sources emphasize a **wide clinical spectrum** from indolent to aggressive behavior (lopez2024biologicalandclinical pages 1-2).

**Direct abstract quote (2024, Blood Advances):** “Mantle cell lymphoma (MCL) is an uncommon mature B-cell lymphoma that presents a clinical spectrum ranging from indolent to aggressive disease…” (López et al., *Blood Advances*, 2024-07; https://doi.org/10.1182/bloodadvances.2023011763) (lopez2024biologicalandclinical pages 1-2).

### Synonyms / alternative names (used in contemporary literature)
- Mantle cell lymphoma (MCL)
- Conventional MCL (cMCL) (lopez2024biologicalandclinical pages 1-2)
- Leukemic non-nodal MCL (nnMCL) / leukemic non-nodal (LNN) presentation (harmanen2024mantlecelllymphoma pages 31-34, cencini2024survivaloutcomesof pages 1-2)
- “Peripheral leukemic (non-nodal)” MCL presentations (clinical descriptor) (md2023currenttreatmentsin pages 12-13)

### Classification context (WHO/ICC)
A 2024 registry thesis/review explicitly references the **WHO 5th edition (2022)** classification framework for haematolymphoid tumors and describes WHO-based categorization of MCL subtypes (harmanen2024mantlecelllymphoma pages 24-31, harmanen2024mantlecelllymphoma pages 31-34). A 2025 review also notes and cites both **ICC (Blood 2022)** and **WHO 5th edition** classification documents as key taxonomy references for MCL (ip2025updatesonthe pages 20-21).

## 2. Etiology
### Disease causal factors (genetic/mechanistic)
MCL pathogenesis is strongly associated with a **primary chromosomal translocation t(11;14)(q13;q32)** that juxtaposes **IGH::CCND1** and drives **cyclin D1 overexpression** (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 31-34). This event is commonly treated as the pathognomonic initiating lesion in disease-level reviews (lopez2024biologicalandclinical pages 1-2).

MCL is described as having **significant genomic instability**, affecting multiple processes including **cell cycle regulation**, **cell survival**, **DNA damage response**, **telomere maintenance**, **NOTCH signaling**, **NF-κB/B-cell receptor (BCR) pathways**, and **chromatin modification** (lopez2024biologicalandclinical pages 1-2).

### Risk factors
**Demographic risk factors:**
- Older age (typical onset >60 years; median age around mid-to-late 60s in multiple sources) and male predominance (male:female >2:1 reported in a 2024 registry source) (harmanen2024mantlecelllymphoma pages 31-34, lopez2024biologicalandclinical pages 1-2).

**Molecular risk factors for aggressive disease / treatment resistance:**
- High tumor proliferation, blastoid morphology, **TP53** alterations and/or **CDKN2A/B** inactivation, and high genetic complexity are repeatedly highlighted as adverse determinants of outcome with standard regimens (lopez2024biologicalandclinical pages 1-2).

### Protective factors / gene–environment interactions
No specific protective variants, lifestyle protective factors, or gene–environment interaction findings were identified in the retrieved 2023–2024 sources; therefore none are asserted here.

## 3. Phenotypes (clinical presentation)
### Common presenting manifestations (with frequencies where available)
- **Advanced stage at diagnosis** is common. A 2023 review reports: “More than 80% of patients present with stage III/ IV disease at the time of diagnosis” (Kallam & Vose, *Oncology*, 2023-08; https://doi.org/10.46883/2023.25921002) (md2023currenttreatmentsin pages 12-13). A 2024 real-world cohort reported **84.9%** advanced stage (stage III 12.3%, stage IV 72.6%) (cencini2024survivaloutcomesof pages 3-5).
- **B symptoms**: ~30% in one 2023 review (md2023currenttreatmentsin pages 12-13).
- **Leukemic/non-nodal presentations**: ~10–20% of patients described as leukemic non-nodal/LNN in a 2024 real-world study (cencini2024survivaloutcomesof pages 1-2) and in other disease summaries (harmanen2024mantlecelllymphoma pages 31-34).
- **Gastrointestinal involvement**: rare “lymphomatous GI polyposis” presentations mentioned in a 2023 review (md2023currenttreatmentsin pages 12-13).

### Suggested HPO terms (examples)
(Phenotype frequencies are not uniformly available across sources; terms below reflect typical clinical descriptors.)
- Lymphadenopathy — **HP:0002716**
- Splenomegaly — **HP:0001744**
- Fever — **HP:0001945**
- Night sweats — **HP:0030166**
- Weight loss — **HP:0001824**
- Lymphocytosis — **HP:0001974** (for leukemic presentations)
- Anemia — **HP:0001903**
- Thrombocytopenia — **HP:0001873**

### Quality of life impact
A 2024 registry source notes survivorship burdens and reports PTSD prevalence in survivors ≈3× higher than the general population (without providing detailed QoL instrument values in the excerpt) (harmanen2024mantlecelllymphoma pages 60-66). Disease- and treatment-related toxicity (e.g., cytopenias/infections with intensive therapy; CRS/ICANS with CAR-T) also plausibly impacts functioning, but detailed instrument-based QoL statistics were not captured in the retrieved excerpts.

## 4. Genetic / molecular information
### Causal / hallmark genes and abnormalities
- **t(11;14)(q13;q32), IGH::CCND1 → cyclin D1 overexpression** (hallmark lesion) (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 31-34).
- **SOX11**: diagnostically and biologically informative; nuclear staining in ~90% of cases in a 2024 registry source (harmanen2024mantlecelllymphoma pages 31-34) and used to help classify subtypes (lopez2024biologicalandclinical pages 1-2).

### Recurrently altered genes and processes (somatic)
Recent reviews/registry sources list frequent alterations including **ATM**, **TP53**, **CDKN2A/B**, and additional pathway-level changes (NOTCH; NF-κB/BCR; chromatin modifiers) (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 34-39).

A 2023 review provides example frequencies: **CDKN2A deletions** “Seen in 25% of MCL cases,” **TP53 mutations** ~11%, and **17p deletions** up to 16% (md2023currenttreatmentsin pages 12-13).

### Molecular subtypes
Two major subtypes are emphasized:
- **Conventional MCL (cMCL)**: typically SOX11+, more genomically complex/aggressive (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 31-34).
- **Leukemic non-nodal MCL (nnMCL/LNN)**: ~10–20%, often SOX11−, more indolent with greater genomic stability; some initially asymptomatic/stable cases may progress over time (lopez2024biologicalandclinical pages 1-2, cencini2024survivaloutcomesof pages 1-2).

### Suggested ontology mappings
- **GO biological processes (examples):**
  - Cell cycle G1/S transition — GO:0044843
  - B-cell receptor signaling pathway — GO:0050853
  - NF-κB signaling — GO:0043122
  - DNA damage response — GO:0006974
  - Chromatin organization — GO:0006325
- **Cell Ontology (CL) (examples):**
  - B cell — **CL:0000236**
  - Memory B cell (relevant to nnMCL hypotheses) — **CL:0000787**
- **GO cellular components (examples):**
  - Nucleus — GO:0005634 (e.g., SOX11 nuclear staining)

## 5. Environmental information
The retrieved sources did not provide specific, well-supported environmental, occupational, lifestyle, or infectious causal contributors unique to MCL. Therefore, no disease-specific environmental etiologies are asserted here.

## 6. Mechanism / pathophysiology (with causal chains)
### Core causal chain (tumor-intrinsic)
1. **Initiating lesion:** t(11;14) juxtaposes **IGH** with **CCND1** → **cyclin D1 overexpression** (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 31-34).
2. **Cell-cycle dysregulation:** cyclin D1 promotes G1/S transition (cell-cycle control concept noted in registry source) (harmanen2024mantlecelllymphoma pages 31-34).
3. **Progression / heterogeneity:** subsequent genomic instability and pathway disruptions accrue (DNA damage response, NOTCH, NF-κB/BCR signaling, chromatin modification), resulting in clinically heterogeneous phenotypes (lopez2024biologicalandclinical pages 1-2).
4. **Aggressive biology / treatment resistance:** high proliferation, blastoid/pleomorphic morphology, and inactivation of **TP53** and/or **CDKN2A/B** are linked with poorer outcomes under standard regimens (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 34-39).

### Tumor microenvironment (TME)
A 2024 immunology review highlights macrophage contributions to prognosis and therapy response.

**Direct abstract quote (2024, Frontiers in Immunology):** “In Mantle Cell Lymphoma (MCL), the role of macrophages within the tumour microenvironment (TME) has recently gained attention due to their impact on prognosis and response to therapy.” (Nylund et al., *Front Immunol*, 2024-03; https://doi.org/10.3389/fimmu.2024.1373269) (nylund2024empoweringmacrophagesthe pages 1-2).

Mechanistic themes include:
- M2-like macrophages (e.g., **CD163+**) linked to angiogenesis and immunosuppression (nylund2024empoweringmacrophagesthe pages 1-2).
- Immunomodulation approaches: lenalidomide-associated reductions in CD163+ macrophages and enhanced phagocytosis; CD47-blockade + rituximab to increase phagocytosis (nylund2024empoweringmacrophagesthe pages 1-2).

### Recent developments / latest research themes (2023–2024 emphasis)
- Increasing use of molecular stratification and proliferation signatures (e.g., MCL35), and early-progression endpoints like POD24 being validated in large trial datasets (lopez2024biologicalandclinical pages 12-13, harmanen2024mantlecelllymphoma pages 144-152).
- Integration of targeted therapies and immune therapies (BTK inhibitors, BCL2 inhibition, CAR-T; investigational bispecific antibodies) to address relapse and high-risk disease (lopez2024biologicalandclinical pages 12-13, nylund2024empoweringmacrophagesthe pages 1-2).

## 7. Anatomical structures affected
### Organ-level involvement (typical)
- Lymph nodes (common primary site for nodal disease) (md2023currenttreatmentsin pages 12-13)
- Bone marrow involvement is frequent in advanced-stage disease descriptions and workups (md2023currenttreatmentsin pages 12-13, harmanen2024mantlecelllymphoma pages 34-39)
- Extranodal sites such as GI tract can be involved (clinical descriptions include GI polyposis) (md2023currenttreatmentsin pages 12-13)

### Suggested UBERON mappings (examples)
- Lymph node — **UBERON:0000029**
- Spleen — **UBERON:0002106**
- Bone marrow — **UBERON:0002371**
- Gastrointestinal tract — **UBERON:0001555**

## 8. Temporal development
### Onset and course
- Typical onset in older adults (median ~65 in Blood Advances review; older than 60 in registry source) (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 31-34).
- Course often relapsing; indolent nnMCL exists but may progress over time (lopez2024biologicalandclinical pages 1-2).

### Disease staging and prognostic indices
- **MIPI** and **Ki-67** are widely used (cencini2024survivaloutcomesof pages 1-2, harmanen2024mantlecelllymphoma pages 34-39).
- High Ki-67 (e.g., >30%) is used to define high-risk in a 2024 registry source (harmanen2024mantlecelllymphoma pages 34-39).
- POD24 (progression within 24 months) is highlighted as a strong poor-prognosis indicator in registry analyses and reviews (harmanen2024mantlecelllymphoma pages 144-152, lopez2024biologicalandclinical pages 12-13).

## 9. Inheritance and population
### Epidemiology (recent quantitative data)
- MCL accounts for **~2–6% of NHL cases** in a 2024 registry source, with incidence commonly reported around **~1 per 100,000 persons** in US/EU settings; Finland 2021 incidence reported as **1.63/100,000** with 102 new cases (harmanen2024mantlecelllymphoma pages 31-34).
- A 2024 immunology review reports MCL accounts for about **5% of NHL** (nylund2024empoweringmacrophagesthe pages 1-2).

### Demographics
- Male predominance (male:female >2:1 in a 2024 registry source) (harmanen2024mantlecelllymphoma pages 31-34).
- Older median age; example real-world cohort median age 70, 69.9% male (cencini2024survivaloutcomesof pages 3-5).

## 10. Diagnostics
### Standard diagnostic approach (pathology + immunophenotype + cytogenetics)
Key diagnostic elements across sources include:
- Histopathology on tissue biopsy (md2023currenttreatmentsin pages 12-13).
- Immunophenotype typically includes B-cell markers (CD19, CD20) with **cyclin D1** nuclear expression; MCL is often **CD5+** (md2023currenttreatmentsin pages 12-13, harmanen2024mantlecelllymphoma pages 34-39).
- **FISH for IGH::CCND1 (t(11;14))** is emphasized as a preferred diagnostic method (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 34-39).
- **SOX11 immunohistochemistry** as a diagnostic/subtyping tool, including cyclin D1-negative cases (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 31-34).

### Emerging / advanced diagnostics
- MRD is emphasized as prognostic and may predict relapse following CAR-T: ZUMA-2 translational analyses identify MRD as predictive for relapse (wang2023threeyearfollowupof pages 1-2, wang2023threeyearfollowupof pages 3-4).

## 11. Outcome / prognosis
### Survival statistics (real-world and trial)
- **Population-based registry (Finland/Spain; n≈564; 2000–2020):** median OS ≈80 months; 2-year OS 77%, 5-year OS 58%, 10-year OS 32% (harmanen2024mantlecelllymphoma pages 144-152).
- **Real-life monocenter cohort (n=73; 2006–2020):** median PFS 60 months; OS not reached; OS at 2/5/10 years 80%/63%/51% (cencini2024survivaloutcomesof pages 3-5). Age-stratified outcomes showed markedly worse PFS for ≥75 years (median 36 months) than <65 years (median 72 months) (cencini2024survivaloutcomesof pages 1-2).
- **CAR-T (ZUMA-2, 3-year follow-up):** median follow-up 35.6 months; median PFS 25.8 months; median OS 46.6 months (wang2023threeyearfollowupof pages 1-2).

### Prognostic factors (consistent across sources)
- Ki-67/proliferation, blastoid/pleomorphic morphology, TP53 alterations, CDKN2A/B inactivation, and overall genetic complexity (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 34-39).

## 12. Treatment
### Current applications and real-world implementations
Frontline management remains risk- and fitness-adapted:
- Younger/fit: cytarabine-containing regimens ± ASCT and rituximab maintenance (as summarized in 2024 real-world study) (cencini2024survivaloutcomesof pages 1-2).
- Older/transplant-ineligible: bendamustine-rituximab (BR), R-BAC, VR-CAP (cencini2024survivaloutcomesof pages 1-2).

Relapsed/refractory MCL: BTK inhibitors are established therapies and CAR-T is implemented for appropriate patients.

**Direct abstract quote (ZUMA-2 3-year follow-up, JCO 2023):** “After a median follow-up of 35.6 months, the objective response rate among all 68 treated patients was 91%… with 68% complete responses… medians for duration of response, progression-free survival, and overall survival were 28.2 months…, 25.8 months…, and 46.6 months…” (Wang et al., *J Clin Oncol*, 2023-01; https://doi.org/10.1200/JCO.21.02370) (wang2023threeyearfollowupof pages 1-2).

### Recent developments and latest research (2023–2024 highlighted)
- **CAR-T durability and MRD association:** In ZUMA-2 follow-up, month-6 MRD negativity is common among assessable patients (79%) and associated with favorable outcomes (medians not reached in MRD-negative subgroup) (wang2023threeyearfollowupof pages 2-3).
- **Real-world CAR-T outcomes:** A real-world series summarized in 2024 reported ORR 90%, CR 82%, estimated 12-month PFS 59% (cencini2024survivaloutcomesof pages 2-3).
- **BTK inhibitor sequencing and unmet need post-BTKi:** Ibrutinib outcomes appear better when used earlier; median OS after ibrutinib failure can be extremely poor (2.9 months in a 114-patient retrospective series cited) (cencini2024survivaloutcomesof pages 1-2).

### MAXO term suggestions (examples)
- Anti-CD20 monoclonal antibody therapy (rituximab) — **MAXO:0000133** (suggested)
- Bruton tyrosine kinase inhibitor therapy — (suggested)
- Chimeric antigen receptor T-cell therapy — (suggested)
- Autologous hematopoietic stem cell transplantation — (suggested)

### Key 2023–2024 treatment/outcome evidence summary (table)
| Setting | Intervention | Study type/source | Key efficacy results (ORR/CR/PFS/OS with timepoints) | Safety notes (brief) | Publication date | URL | Evidence citation id(s) |
|---|---|---|---|---|---|---|---|
| R/R MCL | Brexucabtagene autoleucel (KTE-X19, anti-CD19 CAR-T) | Phase 2 pivotal follow-up, ZUMA-2; Wang et al., *J Clin Oncol* | Median follow-up 35.6 months; ORR 91%; CR 68%; median DOR 28.2 months; median PFS 25.8 months; median OS 46.6 months; 37% remained in ongoing response; month-6 MRD-negative patients (79% of assessable) had ORR 100% and DOR/PFS/OS not reached (wang2023threeyearfollowupof pages 9-10, wang2023threeyearfollowupof pages 1-2, wang2023threeyearfollowupof pages 3-4) | Late-onset toxicities infrequent; only 3% of treatment-emergent adverse events of interest occurred during extended follow-up; no new major CRS signal reported (wang2023threeyearfollowupof pages 9-10, wang2023threeyearfollowupof pages 1-2, wang2023threeyearfollowupof pages 3-4) | Jan 2023 | https://doi.org/10.1200/jco.21.02370 | (wang2023threeyearfollowupof pages 9-10, wang2023threeyearfollowupof pages 1-2, wang2023threeyearfollowupof pages 3-4) |
| R/R MCL | Brexucabtagene autoleucel (real-world) | Real-world leukapheresis/treated cohort summarized in Cencini 2024 | ORR 90%; CR 82%; estimated 12-month PFS 59%; median follow-up 14.3 months in cited real-life series (cencini2024survivaloutcomesof pages 2-3) | Feasibility limited by CRS, ICANS, prolonged cytopenia, and infections in real-world practice (cencini2024survivaloutcomesof pages 2-3) | Jan 2024 | https://doi.org/10.3390/hematolrep16010006 | (cencini2024survivaloutcomesof pages 2-3) |
| R/R MCL | Ibrutinib (covalent BTK inhibitor) | Real-world/literature summary in Cencini 2024 | Median PFS about 12.8 months overall; if used second line, PFS 25.4 vs 10.3 months and OS not reached vs 22.5 months compared with later-line use; after ibrutinib failure, median OS 2.9 months in a 114-patient retrospective series (cencini2024survivaloutcomesof pages 9-10, cencini2024survivaloutcomesof pages 1-2) | Outcomes particularly poor after BTKi failure; high-risk biology such as TP53 mutation associated with worse outcomes in summarized literature (cencini2024survivaloutcomesof pages 1-2) | Jan 2024 | https://doi.org/10.3390/hematolrep16010006 | (cencini2024survivaloutcomesof pages 9-10, cencini2024survivaloutcomesof pages 1-2) |
| Frontline / mixed real-world cohort | Contemporary real-life management era effect | Monocenter 73-patient retrospective cohort; Cencini et al., *Hematology Reports* | Median PFS 60 months; 2/5/10-year PFS 63%/50%/32%; 2/5/10-year OS 80%/63%/51%; age <65 years: median PFS 72 months, 5-year OS 82%; age ≥75 years: median PFS 36 months, 5-year OS 55%; 5-year OS improved to 91% in 2016-2020 vs 44% and 33% in earlier eras (cencini2024survivaloutcomesof pages 1-2, cencini2024survivaloutcomesof pages 3-5) | Improvement likely associated with wider BR use first line in elderly patients and ibrutinib second line; retrospective non-randomized cohort (cencini2024survivaloutcomesof pages 1-2, cencini2024survivaloutcomesof pages 3-5) | Jan 2024 | https://doi.org/10.3390/hematolrep16010006 | (cencini2024survivaloutcomesof pages 1-2, cencini2024survivaloutcomesof pages 3-5) |
| Frontline / population registry | Rituximab/cytarabine era registry outcomes | Binational registry study; Harmanen 2024 | Population-based cohort (n=564) had median OS about 80 months; 2-year OS 77%; 5-year OS 58%; 10-year OS 32%; POD24 identified as a strong poor-prognosis marker (cencini2024survivaloutcomesof pages 9-10, harmanen2024mantlecelllymphoma pages 144-152) | Reflects real-world heterogeneity across age/comorbidity; detailed regimen-specific toxicity not provided in excerpt (harmanen2024mantlecelllymphoma pages 144-152) | 2024 | Not available in provided context | (harmanen2024mantlecelllymphoma pages 144-152, cencini2024survivaloutcomesof pages 9-10) |
| Frontline intensive, real-world eligible/ineligible subsets | MCL2-like intensive cytarabine-containing approaches | Real-world registry analysis summarized in Harmanen 2024 | Trial-eligible patients treated with intensive MCL2-like regimens: median OS 14.3 years and median PFS about 6.4 years; trial-ineligible patients: median OS 9.8 years and median PFS about 4.4 years; Nordic MCL2 trial comparator median OS 12.7 years and PFS 8.5 years (harmanen2024mantlecelllymphoma pages 179-185) | Real-world expansion included older/frailer patients; retrospective comparisons subject to selection bias and incomplete subgroup reporting (harmanen2024mantlecelllymphoma pages 179-185) | 2024 | Not available in provided context | (harmanen2024mantlecelllymphoma pages 179-185) |
| Frontline / R/R supportive biologic strategies | Lenalidomide macrophage modulation; CD47 blockade + rituximab; bispecific antibodies (emerging) | 2024 tumor-microenvironment review; Nylund et al., *Front Immunol* | No practice-defining efficacy estimates provided in the excerpt for approval-level use in MCL; review notes lenalidomide can reduce CD163+ macrophages and enhance phagocytosis, and CD47 blockade plus rituximab can increase macrophage phagocytosis of MCL cells; bispecific antibodies described as promising next-step therapies rather than established standards (nylund2024empoweringmacrophagesthe pages 1-2, harmanen2024mantlecelllymphoma pages 60-66) | Avoid overstatement: these approaches are emerging/investigational or context-dependent in MCL, with efficacy and approval status still evolving in 2024 sources (nylund2024empoweringmacrophagesthe pages 1-2, harmanen2024mantlecelllymphoma pages 60-66) | Mar 2024 | https://doi.org/10.3389/fimmu.2024.1373269 | (nylund2024empoweringmacrophagesthe pages 1-2, harmanen2024mantlecelllymphoma pages 60-66) |


*Table: This table summarizes key 2023-2024 treatment and real-world outcome evidence for mantle cell lymphoma across frontline and relapsed/refractory settings. It highlights pivotal CAR-T data, BTK inhibitor outcomes, registry survival trends, and emerging microenvironment-directed strategies with citations to the provided evidence context.*

## 13. Prevention
### Primary prevention
No validated primary prevention strategies were identified in the retrieved sources.

### Secondary/tertiary prevention (complication prevention)
A real-world cohort description notes infection prophylaxis practices (e.g., HBV/HCV management; PCP prophylaxis) in clinical care contexts (cencini2024survivaloutcomesof pages 2-3). Additional guideline-level vaccination/prophylaxis details were not present in the retrieved excerpts.

## 14. Other species / natural disease
No evidence on naturally occurring MCL in non-human species was retrieved in this run; thus not asserted.

## 15. Model organisms
No primary model-organism papers were retrieved in this run; thus model organism details (e.g., Eµ-CCND1 mice; xenografts; cell lines) cannot be cited here.

## Consolidated KB-ready biology/prognosis snapshot (table)
| Topic | Key facts (include quantitative where available) | Supporting recent source (include first author, year, journal) | PMID if known | URL | Evidence citation id(s) |
|---|---|---|---|---|---|
| Definition / rarity / age-sex | Mantle cell lymphoma (MCL) is a rare mature B-cell neoplasm arising from the mantle zone. It accounts for ~2–6% of all NHL in one 2024 registry source, with incidence commonly ~1 per 100,000 persons; Finnish 2021 data reported 102 new cases, incidence 1.63/100,000. Typical patients are older than 60 years, median age ~65, with male predominance >2:1. | Harmanen, 2024, registry study; López, 2024, *Blood Advances* |  | https://doi.org/10.1182/bloodadvances.2023011763 | (harmanen2024mantlecelllymphoma pages 31-34, lopez2024biologicalandclinical pages 1-2) |
| Hallmark t(11;14) / CCND1 | The pathognomonic primary event is t(11;14)(q13;q32), usually IGH::CCND1, causing constitutive cyclin D1 overexpression. This lesion is present in >95% of classic/nodal MCL in one recent review and is preferentially detected by FISH in diagnostic workup. | López, 2024, *Blood Advances*; Ip, 2025, *Cancers*; Harmanen, 2024, registry study |  | https://doi.org/10.1182/bloodadvances.2023011763 | (lopez2024biologicalandclinical pages 1-2, ip2025updatesonthe pages 2-4, harmanen2024mantlecelllymphoma pages 34-39) |
| Cyclin D1-negative cases | Cyclin D1-negative MCL is uncommon; recent reviews note rarer alternative cyclin-driven cases, including CCND2-rearranged disease, and emphasize SOX11 as particularly useful for identifying cyclin D1-negative MCL in practice. | López, 2024, *Blood Advances*; Ip, 2025, *Cancers* |  | https://doi.org/10.1182/bloodadvances.2023011763 | (lopez2024biologicalandclinical pages 1-2, ip2025updatesonthe pages 2-4) |
| SOX11 | SOX11 is a key diagnostic and biologic marker. About 90% of MCL show nuclear SOX11 staining in one 2024 registry source; SOX11 IHC helps support diagnosis and subtype assignment, especially for cyclin D1-negative cases. Lack of SOX11 expression is linked to leukemic non-nodal/indolent presentations. | Harmanen, 2024, registry study; López, 2024, *Blood Advances*; Cencini, 2024, *Hematology Reports* |  | https://doi.org/10.1182/bloodadvances.2023011763 | (harmanen2024mantlecelllymphoma pages 31-34, lopez2024biologicalandclinical pages 1-2, cencini2024survivaloutcomesof pages 1-2) |
| Molecular subtypes: cMCL vs nnMCL | Two main molecular/clinical subtypes are recognized: conventional MCL (cMCL) and leukemic non-nodal MCL (nnMCL). cMCL is typically SOX11+, often IGHV-unmutated, genomically more complex, and clinically more aggressive. nnMCL represents ~10–20% of cases, is often SOX11-negative, IGHV-mutated, genetically more stable, and may follow an indolent course, though some cases later progress. | López, 2024, *Blood Advances*; Harmanen, 2024, registry study; Cencini, 2024, *Hematology Reports* |  | https://doi.org/10.1182/bloodadvances.2023011763 | (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 31-34, cencini2024survivaloutcomesof pages 1-2) |
| Pathways affected | MCL shows marked genomic instability affecting cell cycle control, cell survival, DNA damage response, telomere maintenance, NOTCH signaling, NF-κB/B-cell receptor signaling, and chromatin modification. Frequent recurrently altered genes include ATM, TP53, CDKN2A/B, and CCND1. | López, 2024, *Blood Advances*; Harmanen, 2024, registry study |  | https://doi.org/10.1182/bloodadvances.2023011763 | (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 34-39) |
| Adverse prognostic factors | Recurrently adverse features include TP53 mutation/inactivation, CDKN2A/B loss/inactivation, high Ki-67/proliferation, blastoid or pleomorphic morphology, and high genetic complexity. Ki-67 >30% is cited as high-risk in one 2024 registry source; TP53 mutation is recommended for sequencing at diagnosis in 2024 guidance cited there. | López, 2024, *Blood Advances*; Harmanen, 2024, registry study |  | https://doi.org/10.1182/bloodadvances.2023011763 | (lopez2024biologicalandclinical pages 1-2, harmanen2024mantlecelllymphoma pages 34-39) |
| Stage at diagnosis | Advanced presentation is typical. One 2023 review states >80% present with stage III/IV disease. In a 2024 real-life cohort, 84.9% had advanced-stage disease, including stage III 12.3% and stage IV 72.6%. | Kallam, 2023, *Oncology*; Cencini, 2024, *Hematology Reports* |  | https://doi.org/10.46883/2023.25921002 | (md2023currenttreatmentsin pages 12-13, cencini2024survivaloutcomesof pages 3-5) |


*Table: This table condenses key mantle cell lymphoma biology, subtype distinctions, diagnostic markers, and adverse prognostic features from recent sources. It is useful as a knowledge-base-ready snapshot linking core facts to supporting evidence and URLs.*

## Visual evidence from key 2023 trial follow-up
Cropped figures/tables were retrieved from the ZUMA-2 3-year follow-up paper showing the key efficacy endpoints and MRD-related summaries (wang2023threeyearfollowupof media 7705478f, wang2023threeyearfollowupof media 514e8505, wang2023threeyearfollowupof media d297d7b8, wang2023threeyearfollowupof media 87d7a7f7).

## Notes on evidence gaps vs. template requirements
- **Ontology IDs (MONDO/MeSH/ICD/Orphanet/OMIM):** not available in retrieved documents/tools for this run.
- **Environmental/protective factors; infectious triggers; gene–environment interactions:** not evidenced in retrieved excerpts.
- **Model organism / comparative pathology:** not evidenced in retrieved excerpts.
- **Some 2024 guidelines (e.g., BSH 2024) were listed as unobtainable by the tool and could not be used as sources in this report.**


References

1. (harmanen2024mantlecelllymphoma pages 31-34): M Harmanen. Mantle cell lymphoma in the rituximab era: retrospective registry study on survival, treatment and prognostic factors. Unknown journal, 2024.

2. (lopez2024biologicalandclinical pages 1-2): Cristina López, Elisabeth Silkenstedt, Martin Dreyling, and Sílvia Beà. Biological and clinical determinants shaping heterogeneity in mantle cell lymphoma. Blood Advances, 8:3652-3664, Jul 2024. URL: https://doi.org/10.1182/bloodadvances.2023011763, doi:10.1182/bloodadvances.2023011763. This article has 19 citations and is from a peer-reviewed journal.

3. (cencini2024survivaloutcomesof pages 1-2): Emanuele Cencini, Natale Calomino, Marta Franceschini, Andreea Dragomir, Sara Fredducci, Beatrice Esposito Vangone, Giulia Lucco Navei, Alberto Fabbri, and Monica Bocchia. Survival outcomes of patients with mantle cell lymphoma: a retrospective, 15-year, real-life study. Hematology Reports, 16:50-62, Jan 2024. URL: https://doi.org/10.3390/hematolrep16010006, doi:10.3390/hematolrep16010006. This article has 17 citations.

4. (md2023currenttreatmentsin pages 12-13): Avyakta Kallam Md and J. Vose. Current treatments in mantle cell lymphoma. Oncology, 37 8:326-333, Aug 2023. URL: https://doi.org/10.46883/2023.25921002, doi:10.46883/2023.25921002. This article has 2 citations and is from a peer-reviewed journal.

5. (harmanen2024mantlecelllymphoma pages 24-31): M Harmanen. Mantle cell lymphoma in the rituximab era: retrospective registry study on survival, treatment and prognostic factors. Unknown journal, 2024.

6. (ip2025updatesonthe pages 20-21): Andrew Ip, Maciej Kabat, Lindsay Fogel, Hassan Alkhatatneh, Jason Voss, Amolika Gupta, Alexandra Della Pia, Lori A. Leslie, Tatyana Feldman, Maher Albitar, and Andre H. Goy. Updates on the biological heterogeneity of mantle cell lymphoma. Cancers, 17:696, Feb 2025. URL: https://doi.org/10.3390/cancers17040696, doi:10.3390/cancers17040696. This article has 3 citations.

7. (cencini2024survivaloutcomesof pages 3-5): Emanuele Cencini, Natale Calomino, Marta Franceschini, Andreea Dragomir, Sara Fredducci, Beatrice Esposito Vangone, Giulia Lucco Navei, Alberto Fabbri, and Monica Bocchia. Survival outcomes of patients with mantle cell lymphoma: a retrospective, 15-year, real-life study. Hematology Reports, 16:50-62, Jan 2024. URL: https://doi.org/10.3390/hematolrep16010006, doi:10.3390/hematolrep16010006. This article has 17 citations.

8. (harmanen2024mantlecelllymphoma pages 60-66): M Harmanen. Mantle cell lymphoma in the rituximab era: retrospective registry study on survival, treatment and prognostic factors. Unknown journal, 2024.

9. (harmanen2024mantlecelllymphoma pages 34-39): M Harmanen. Mantle cell lymphoma in the rituximab era: retrospective registry study on survival, treatment and prognostic factors. Unknown journal, 2024.

10. (nylund2024empoweringmacrophagesthe pages 1-2): Patrick Nylund, Anna Nikkarinen, Sara Ek, and Ingrid Glimelius. Empowering macrophages: the cancer fighters within the tumour microenvironment in mantle cell lymphoma. Frontiers in Immunology, Mar 2024. URL: https://doi.org/10.3389/fimmu.2024.1373269, doi:10.3389/fimmu.2024.1373269. This article has 7 citations and is from a peer-reviewed journal.

11. (lopez2024biologicalandclinical pages 12-13): Cristina López, Elisabeth Silkenstedt, Martin Dreyling, and Sílvia Beà. Biological and clinical determinants shaping heterogeneity in mantle cell lymphoma. Blood Advances, 8:3652-3664, Jul 2024. URL: https://doi.org/10.1182/bloodadvances.2023011763, doi:10.1182/bloodadvances.2023011763. This article has 19 citations and is from a peer-reviewed journal.

12. (harmanen2024mantlecelllymphoma pages 144-152): M Harmanen. Mantle cell lymphoma in the rituximab era: retrospective registry study on survival, treatment and prognostic factors. Unknown journal, 2024.

13. (wang2023threeyearfollowupof pages 1-2): Michael Wang, Javier Munoz, Andre Goy, Frederick L. Locke, Caron A. Jacobson, Brian T. Hill, John M. Timmerman, Houston Holmes, Samantha Jaglowski, Ian W. Flinn, Peter A. McSweeney, David B. Miklos, John M. Pagel, Marie José Kersten, Krimo Bouabdallah, Rashmi Khanal, Max S. Topp, Roch Houot, Amer Beitinjaneh, Weimin Peng, Xiang Fang, Rhine R. Shen, Rubina Siddiqi, Ioana Kloos, and Patrick M. Reagan. Three-year follow-up of kte-x19 in patients with relapsed/refractory mantle cell lymphoma, including high-risk subgroups, in the zuma-2 study. Journal of Clinical Oncology, 41:555-567, Jan 2023. URL: https://doi.org/10.1200/jco.21.02370, doi:10.1200/jco.21.02370. This article has 354 citations and is from a highest quality peer-reviewed journal.

14. (wang2023threeyearfollowupof pages 3-4): Michael Wang, Javier Munoz, Andre Goy, Frederick L. Locke, Caron A. Jacobson, Brian T. Hill, John M. Timmerman, Houston Holmes, Samantha Jaglowski, Ian W. Flinn, Peter A. McSweeney, David B. Miklos, John M. Pagel, Marie José Kersten, Krimo Bouabdallah, Rashmi Khanal, Max S. Topp, Roch Houot, Amer Beitinjaneh, Weimin Peng, Xiang Fang, Rhine R. Shen, Rubina Siddiqi, Ioana Kloos, and Patrick M. Reagan. Three-year follow-up of kte-x19 in patients with relapsed/refractory mantle cell lymphoma, including high-risk subgroups, in the zuma-2 study. Journal of Clinical Oncology, 41:555-567, Jan 2023. URL: https://doi.org/10.1200/jco.21.02370, doi:10.1200/jco.21.02370. This article has 354 citations and is from a highest quality peer-reviewed journal.

15. (wang2023threeyearfollowupof pages 2-3): Michael Wang, Javier Munoz, Andre Goy, Frederick L. Locke, Caron A. Jacobson, Brian T. Hill, John M. Timmerman, Houston Holmes, Samantha Jaglowski, Ian W. Flinn, Peter A. McSweeney, David B. Miklos, John M. Pagel, Marie José Kersten, Krimo Bouabdallah, Rashmi Khanal, Max S. Topp, Roch Houot, Amer Beitinjaneh, Weimin Peng, Xiang Fang, Rhine R. Shen, Rubina Siddiqi, Ioana Kloos, and Patrick M. Reagan. Three-year follow-up of kte-x19 in patients with relapsed/refractory mantle cell lymphoma, including high-risk subgroups, in the zuma-2 study. Journal of Clinical Oncology, 41:555-567, Jan 2023. URL: https://doi.org/10.1200/jco.21.02370, doi:10.1200/jco.21.02370. This article has 354 citations and is from a highest quality peer-reviewed journal.

16. (cencini2024survivaloutcomesof pages 2-3): Emanuele Cencini, Natale Calomino, Marta Franceschini, Andreea Dragomir, Sara Fredducci, Beatrice Esposito Vangone, Giulia Lucco Navei, Alberto Fabbri, and Monica Bocchia. Survival outcomes of patients with mantle cell lymphoma: a retrospective, 15-year, real-life study. Hematology Reports, 16:50-62, Jan 2024. URL: https://doi.org/10.3390/hematolrep16010006, doi:10.3390/hematolrep16010006. This article has 17 citations.

17. (wang2023threeyearfollowupof pages 9-10): Michael Wang, Javier Munoz, Andre Goy, Frederick L. Locke, Caron A. Jacobson, Brian T. Hill, John M. Timmerman, Houston Holmes, Samantha Jaglowski, Ian W. Flinn, Peter A. McSweeney, David B. Miklos, John M. Pagel, Marie José Kersten, Krimo Bouabdallah, Rashmi Khanal, Max S. Topp, Roch Houot, Amer Beitinjaneh, Weimin Peng, Xiang Fang, Rhine R. Shen, Rubina Siddiqi, Ioana Kloos, and Patrick M. Reagan. Three-year follow-up of kte-x19 in patients with relapsed/refractory mantle cell lymphoma, including high-risk subgroups, in the zuma-2 study. Journal of Clinical Oncology, 41:555-567, Jan 2023. URL: https://doi.org/10.1200/jco.21.02370, doi:10.1200/jco.21.02370. This article has 354 citations and is from a highest quality peer-reviewed journal.

18. (cencini2024survivaloutcomesof pages 9-10): Emanuele Cencini, Natale Calomino, Marta Franceschini, Andreea Dragomir, Sara Fredducci, Beatrice Esposito Vangone, Giulia Lucco Navei, Alberto Fabbri, and Monica Bocchia. Survival outcomes of patients with mantle cell lymphoma: a retrospective, 15-year, real-life study. Hematology Reports, 16:50-62, Jan 2024. URL: https://doi.org/10.3390/hematolrep16010006, doi:10.3390/hematolrep16010006. This article has 17 citations.

19. (harmanen2024mantlecelllymphoma pages 179-185): M Harmanen. Mantle cell lymphoma in the rituximab era: retrospective registry study on survival, treatment and prognostic factors. Unknown journal, 2024.

20. (ip2025updatesonthe pages 2-4): Andrew Ip, Maciej Kabat, Lindsay Fogel, Hassan Alkhatatneh, Jason Voss, Amolika Gupta, Alexandra Della Pia, Lori A. Leslie, Tatyana Feldman, Maher Albitar, and Andre H. Goy. Updates on the biological heterogeneity of mantle cell lymphoma. Cancers, 17:696, Feb 2025. URL: https://doi.org/10.3390/cancers17040696, doi:10.3390/cancers17040696. This article has 3 citations.

21. (wang2023threeyearfollowupof media 7705478f): Michael Wang, Javier Munoz, Andre Goy, Frederick L. Locke, Caron A. Jacobson, Brian T. Hill, John M. Timmerman, Houston Holmes, Samantha Jaglowski, Ian W. Flinn, Peter A. McSweeney, David B. Miklos, John M. Pagel, Marie José Kersten, Krimo Bouabdallah, Rashmi Khanal, Max S. Topp, Roch Houot, Amer Beitinjaneh, Weimin Peng, Xiang Fang, Rhine R. Shen, Rubina Siddiqi, Ioana Kloos, and Patrick M. Reagan. Three-year follow-up of kte-x19 in patients with relapsed/refractory mantle cell lymphoma, including high-risk subgroups, in the zuma-2 study. Journal of Clinical Oncology, 41:555-567, Jan 2023. URL: https://doi.org/10.1200/jco.21.02370, doi:10.1200/jco.21.02370. This article has 354 citations and is from a highest quality peer-reviewed journal.

22. (wang2023threeyearfollowupof media 514e8505): Michael Wang, Javier Munoz, Andre Goy, Frederick L. Locke, Caron A. Jacobson, Brian T. Hill, John M. Timmerman, Houston Holmes, Samantha Jaglowski, Ian W. Flinn, Peter A. McSweeney, David B. Miklos, John M. Pagel, Marie José Kersten, Krimo Bouabdallah, Rashmi Khanal, Max S. Topp, Roch Houot, Amer Beitinjaneh, Weimin Peng, Xiang Fang, Rhine R. Shen, Rubina Siddiqi, Ioana Kloos, and Patrick M. Reagan. Three-year follow-up of kte-x19 in patients with relapsed/refractory mantle cell lymphoma, including high-risk subgroups, in the zuma-2 study. Journal of Clinical Oncology, 41:555-567, Jan 2023. URL: https://doi.org/10.1200/jco.21.02370, doi:10.1200/jco.21.02370. This article has 354 citations and is from a highest quality peer-reviewed journal.

23. (wang2023threeyearfollowupof media d297d7b8): Michael Wang, Javier Munoz, Andre Goy, Frederick L. Locke, Caron A. Jacobson, Brian T. Hill, John M. Timmerman, Houston Holmes, Samantha Jaglowski, Ian W. Flinn, Peter A. McSweeney, David B. Miklos, John M. Pagel, Marie José Kersten, Krimo Bouabdallah, Rashmi Khanal, Max S. Topp, Roch Houot, Amer Beitinjaneh, Weimin Peng, Xiang Fang, Rhine R. Shen, Rubina Siddiqi, Ioana Kloos, and Patrick M. Reagan. Three-year follow-up of kte-x19 in patients with relapsed/refractory mantle cell lymphoma, including high-risk subgroups, in the zuma-2 study. Journal of Clinical Oncology, 41:555-567, Jan 2023. URL: https://doi.org/10.1200/jco.21.02370, doi:10.1200/jco.21.02370. This article has 354 citations and is from a highest quality peer-reviewed journal.

24. (wang2023threeyearfollowupof media 87d7a7f7): Michael Wang, Javier Munoz, Andre Goy, Frederick L. Locke, Caron A. Jacobson, Brian T. Hill, John M. Timmerman, Houston Holmes, Samantha Jaglowski, Ian W. Flinn, Peter A. McSweeney, David B. Miklos, John M. Pagel, Marie José Kersten, Krimo Bouabdallah, Rashmi Khanal, Max S. Topp, Roch Houot, Amer Beitinjaneh, Weimin Peng, Xiang Fang, Rhine R. Shen, Rubina Siddiqi, Ioana Kloos, and Patrick M. Reagan. Three-year follow-up of kte-x19 in patients with relapsed/refractory mantle cell lymphoma, including high-risk subgroups, in the zuma-2 study. Journal of Clinical Oncology, 41:555-567, Jan 2023. URL: https://doi.org/10.1200/jco.21.02370, doi:10.1200/jco.21.02370. This article has 354 citations and is from a highest quality peer-reviewed journal.
