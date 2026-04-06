---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:42:53.058184'
end_time: '2026-04-04T12:57:27.458587'
duration_seconds: 874.4
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ANK2 Ankyrin-B Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ANK2 Ankyrin-B Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **ANK2 Ankyrin-B Syndrome** covering all of the
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
- **Disease Name:** ANK2 Ankyrin-B Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **ANK2 Ankyrin-B Syndrome** covering all of the
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


# Comprehensive Research Report: ANK2 Ankyrin‑B Syndrome (LQT4)

## Executive summary
ANK2 (ankyrin‑B) syndrome—historically “long QT syndrome type 4 (LQT4)”—is an autosomal‑dominant, variably expressive, incompletely penetrant inherited arrhythmia disorder caused by pathogenic ANK2 variants that impair ankyrin‑B scaffold function in cardiomyocytes and sinoatrial node cells. It classically presents with QTc prolongation and sinus node dysfunction, but the phenotype extends to atrial fibrillation, ventricular arrhythmias (often catecholamine/stress‑induced), conduction disease, sudden cardiac death, and in some families/variants, structural heart disease/arrhythmogenic cardiomyopathy. (mohler2003ankyrinbmutationcauses pages 1-2, koenig2017theevolvingrole pages 2-4, york2022mechanismsunderlyingthe pages 1-2, sucharski2020mechanismsandalterations pages 1-2)

## 1. Disease information
### 1.1 Definition and overview
Ankyrin‑B (encoded by ANK2) is a membrane–cytoskeleton adaptor (“scaffold”) protein that organizes key ion channels/transporters and signaling proteins required for cardiac excitability and excitation–contraction coupling. Loss‑of‑function ANK2 variants cause a multisystem cardiac electrical disorder originally described as LQT4 and now commonly termed “ankyrin‑B syndrome” due to its broader phenotype beyond QT prolongation. (ackerman2010defininganew pages 2-3, york2022mechanismsunderlyingthe pages 1-2, sucharski2020mechanismsandalterations pages 1-2)

**Key primary description and disease establishment**: a large French pedigree with ANK2 missense variant c.4274A>G (p.Glu1425Gly; historical numbering) exhibited QTc prolongation, sinus node dysfunction, atrial fibrillation, and sudden death, establishing ANK2 as a cause of congenital long‑QT and arrhythmia through a non–ion-channel mechanism. (mohler2003ankyrinbmutationcauses pages 1-2)

### 1.2 Key identifiers
| Concept | Value | Notes | Key citation |
|---|---|---|---|
| Primary disease name | ANK2 ankyrin-B syndrome | Autosomal-dominant inherited arrhythmia syndrome caused by loss-of-function ANK2 variants; broader term now preferred over the older LQT4 label because the phenotype extends beyond isolated QT prolongation | (york2022mechanismsunderlyingthe pages 1-2, sucharski2020mechanismsandalterations pages 1-2) |
| Alternative names | Ankyrin-B syndrome; Long QT syndrome type 4 (LQT4) | Ackerman & Mohler (2010) state that “LQT4 is now more appropriately termed ankyrin-B syndrome” | (york2022mechanismsunderlyingthe pages 1-2) |
| OMIM disease number | #600919 | Retrieved evidence identifies ANK2-LQTS/LQT4 under OMIM #600919 | (mohler2003ankyrinbmutationcauses pages 1-2) |
| Causal gene | ANK2 | Encodes ankyrin-2; human disease-associated variants are typically heterozygous and loss-of-function or functionally deleterious | (mohler2003ankyrinbmutationcauses pages 1-2, york2022mechanismsunderlyingthe pages 1-2) |
| Protein | Ankyrin-B | Scaffold/adaptor protein that organizes ion channels, transporters, structural proteins, and signaling molecules in cardiomyocytes | (koenig2017theevolvingrole pages 2-4, sucharski2020mechanismsandalterations pages 1-2) |
| Historical classification | LQT4 | Original classification emphasized prolonged QT; later work showed broader manifestations including sinus node dysfunction, atrial fibrillation, conduction disease, ventricular arrhythmias, and sudden death | (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2, sucharski2020mechanismsandalterations pages 1-2) |
| Disease-defining paper 1 | Mohler et al., 2003, Nature | “Ankyrin-B mutation causes type 4 long-QT cardiac arrhythmia and sudden cardiac death”; DOI: https://doi.org/10.1038/nature01335 | (mohler2003ankyrinbmutationcauses pages 1-2) |
| Disease-defining paper 2 | Mohler et al., 2004, PNAS | “A cardiac arrhythmia syndrome caused by loss of ankyrin-B function”; DOI: https://doi.org/10.1073/pnas.0402546101 | (mohler2003ankyrinbmutationcauses pages 1-2) |
| Nomenclature-shift paper | Ackerman & Mohler, 2010, Circulation Research | Review arguing the phenotype is broader than classic LQTS and that “ankyrin-B syndrome” is the preferred name; DOI: https://doi.org/10.1161/CIRCRESAHA.110.224592 | (york2022mechanismsunderlyingthe pages 1-2) |
| MONDO ID | not found in retrieved evidence | No disease-specific MONDO identifier for ankyrin-B syndrome was established from retrieved primary/review evidence; Open Targets returned broader long-QT MONDO associations rather than a specific ankyrin-B syndrome term | (york2022mechanismsunderlyingthe pages 1-2) |
| Orphanet ID | not found in retrieved evidence | Not identified in retrieved evidence set | (york2022mechanismsunderlyingthe pages 1-2) |
| ICD-10 / ICD-11 | not found in retrieved evidence | No specific ICD code for ankyrin-B syndrome was identified in retrieved evidence; patients are often captured under inherited arrhythmia/long-QT diagnostic categories | (york2022mechanismsunderlyingthe pages 1-2, sucharski2020mechanismsandalterations pages 1-2) |
| Evidence type for nomenclature/definition | Aggregated disease-level literature plus family-based human studies | Core naming/definition comes from seminal family studies and later disease reviews, not EHR-derived nosology | (mohler2003ankyrinbmutationcauses pages 1-2, york2022mechanismsunderlyingthe pages 1-2, sucharski2020mechanismsandalterations pages 1-2) |


*Table: This table summarizes the core identifiers and naming conventions for ANK2/ankyrin-B syndrome, including its historical LQT4 designation and the seminal papers that established and renamed the condition. It is useful as a compact reference for disease database curation and knowledge-base normalization.*

### 1.3 Synonyms / alternative names
* Ankyrin‑B syndrome (preferred) (ackerman2010defininganew pages 2-3)
* Long QT syndrome type 4 (LQT4) (mohler2003ankyrinbmutationcauses pages 1-2)

### 1.4 Evidence source types
The core disease concept is derived from:
* **Human family studies** with segregation and clinical phenotyping (e.g., Mohler 2003; Scouarnec 2008) (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2)
* **Human cohort “reappraisal”** in referred patients assessing penetrance and variant validity (Giudicessi & Ackerman 2020) (giudicessi2020establishedlossoffunctionvariants pages 1-5)
* **Animal and cellular models** (AnkB+/− mice, conditional Ank2 knockouts, knock‑in mice) used to establish mechanistic links and test targeted interventions (mohler2003ankyrinbmutationcauses pages 1-2, zhu2018ankyrinbq1283hvariant pages 1-2, roberts2019ankyrinbdysfunctionpredisposes pages 9-10)

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** germline ANK2 variants that reduce ankyrin‑B function (often heterozygous loss‑of‑function or functionally deleterious missense variants), leading to abnormal targeting/localization and regulation of ion‑handling and signaling complexes. (koenig2017theevolvingrole pages 2-4, ackerman2010defininganew pages 2-3, mohler2003ankyrinbmutationcauses pages 1-2)

### 2.2 Risk factors
**Genetic risk factors:**
* Pathogenic/likely pathogenic ANK2 variants in key functional regions (e.g., E1425G/E1458G, S646F, Q1283H) are associated with increased arrhythmia susceptibility. (mohler2003ankyrinbmutationcauses pages 1-2, swayne2017novelvariantin pages 1-2, zhu2018ankyrinbq1283hvariant pages 1-2)
* **Oligogenic/variant interpretation caveat:** a large referral reappraisal concluded several historically alleged ankyrin‑B syndrome variants were not enriched compared with gnomAD and often had low/uncertain penetrance in referred individuals, cautioning against assuming monogenic high‑risk for all reported ANK2 variants. (giudicessi2020establishedlossoffunctionvariants pages 1-5)

**Non‑genetic (environmental/lifestyle) risk factors:** not specifically established for ankyrin‑B syndrome in the retrieved evidence. Triggering by adrenergic/catecholaminergic stress is mechanistically supported (mouse/cell models and KI model), consistent with clinical stress/exercise provocation in some patients. (zhu2018ankyrinbq1283hvariant pages 1-2, ackerman2010defininganew pages 2-3)

### 2.3 Protective factors
No validated protective genetic or environmental factors specific to ankyrin‑B syndrome were identified in retrieved evidence.

### 2.4 Gene–environment interaction
Direct gene–environment interaction data were not identified in retrieved evidence; however, **catecholaminergic stimulation** acts as an important physiologic “environmental” trigger for ventricular arrhythmias in models, implicating an interaction between ANK2 defects and adrenergic stress. (zhu2018ankyrinbq1283hvariant pages 1-2, ackerman2010defininganew pages 2-3)

## 3. Phenotypes
### 3.1 Core phenotype spectrum (cardiac)
| Phenotype | Description/clinical notes | Suggested HPO term(s) | Quantitative data/frequency (if available) | Key supporting citations |
|---|---|---|---|---|
| Prolonged QTc / long QT syndrome type 4 | Historical defining feature of LQT4, but QT prolongation is variably expressed and not universally present in ANK2-related disease; broader “ankyrin-B syndrome” terminology is now preferred. | HP:0001657 Prolonged QT interval; HP:0005117 Long QT syndrome | In the original E1425G kindred, mean QTc was ~490 ± 30 ms in adults and ~465 ± 38 ms in children; variant segregated with long-QT phenotype in 22/24 carriers. In the First Nations p.S646F cohort, average QTc was 475 ± 40 ms among carriers. (mohler2003ankyrinbmutationcauses pages 1-2, swayne2017novelvariantin pages 1-2, york2022mechanismsunderlyingthe pages 4-5) | (mohler2003ankyrinbmutationcauses pages 1-2, swayne2017novelvariantin pages 1-2, york2022mechanismsunderlyingthe pages 4-5) |
| Sinus bradycardia / sinus node dysfunction | Core and often prominent manifestation; includes sinus bradycardia, sinus arrhythmia, junctional or escape rhythms, chronotropic abnormalities, and frequent need for pacing in some families. | HP:0001662 Bradycardia; HP:0001679 Cardiac conduction abnormality; HP:0001778 Sinus arrhythmia | In Mohler 2003, sinus node bradycardia or junctional escape rhythm was present in 23/24 carriers. In Scouarnec 2008 Family 1, 74 relatives were screened; escape rhythm origin was SAN in 7, coronary sinus in 7, and junctional in 12; 14 family members required pacemakers. Some AnkB+/− cardiomyocyte data also showed reduced contraction rate (~144 to ~78 bpm) and Ca2+ transient frequency (~2.7 to ~1.3 Hz). (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2) | (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2) |
| Atrial fibrillation / atrial arrhythmias | Frequently reported supraventricular phenotype; may occur with sinus-node disease and may precede or accompany broader ankyrin-B syndrome. | HP:0005110 Atrial fibrillation; HP:0011675 Atrial arrhythmia | Mohler 2003 reported atrial fibrillation in 12 adults from the pedigree. Scouarnec 2008 Family 1 reported AF in 13 relatives, including 5 paroxysmal and 8 permanent cases; mean AF onset ~40 ± 18 years. (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2) | (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2) |
| Ventricular arrhythmias / VT / VF / CPVT-like stress-induced arrhythmias | Includes ventricular tachycardia, ventricular fibrillation, catecholaminergic/stress-induced ventricular arrhythmia susceptibility, and idiopathic VF-like presentations; mechanistically linked to abnormal Ca2+ handling and triggered activity. | HP:0004756 Ventricular tachycardia; HP:0001663 Ventricular fibrillation; HP:0011677 Cardiac arrest; HP:0005110 Arrhythmia (broad) | Mohler 2003 identified sudden cardiac death in the E1425G family and framed the condition as an arrhythmia syndrome with ventricular risk. Zhu 2018 identified ANK2 p.Q1283H in 25 unrelated Han Chinese probands with VT; knock-in mice showed increased stress-induced ventricular arrhythmias. Swayne 2017 notes LQTS-related risk of ventricular arrhythmias in p.S646F carriers. (mohler2003ankyrinbmutationcauses pages 1-2, swayne2017novelvariantin pages 1-2, zhu2018ankyrinbq1283hvariant pages 1-2) | (mohler2003ankyrinbmutationcauses pages 1-2, swayne2017novelvariantin pages 1-2, zhu2018ankyrinbq1283hvariant pages 1-2) |
| Premature atrial contractions | Ectopy is part of the atrial phenotype and was illustrated in ECG examples from affected individuals. | HP:0011707 Atrial premature complexes | ECG examples in the original report showed multiple premature atrial contractions in affected individuals; no cohort-wide count was available in retrieved evidence. (mohler2003ankyrinbmutationcauses media 3330bf40, mohler2003ankyrinbmutationcauses media b13c3b4f) | (mohler2003ankyrinbmutationcauses media 3330bf40, mohler2003ankyrinbmutationcauses media b13c3b4f) |
| Conduction block / conduction disease | Broader conduction system involvement beyond sinus-node dysfunction is recognized in reviews and clinical descriptions of ankyrin-B syndrome. | HP:0001678 Atrioventricular block; HP:0000077 Abnormality of cardiac conduction | Reported qualitatively as part of the phenotype spectrum in disease reviews; no family-level count for conduction block specifically was available in the retrieved core cohorts summarized here. (koenig2017theevolvingrole pages 2-4, sucharski2020mechanismsandalterations pages 1-2) | (koenig2017theevolvingrole pages 2-4, sucharski2020mechanismsandalterations pages 1-2) |
| Structural heart disease / cardiomyopathy / arrhythmogenic cardiomyopathy | Not part of the earliest LQT4 definition, but later evidence linked some ANK2 variants to congenital/adult structural disease, LV dysfunction, and arrhythmogenic cardiomyopathy. | HP:0001638 Cardiomyopathy; HP:0001644 Dilated cardiomyopathy; HP:0033758 Arrhythmogenic cardiomyopathy; HP:0001642 Structural heart abnormality | In Swayne 2017, among 16 additional p.S646F carriers identified by cascade testing, 2 had structural heart disease (1 cardiomyopathy with sudden death, 1 congenital heart disease). Roberts 2019 established a mechanistic ANK2-related arrhythmogenic cardiomyopathy model in mice and linked rare ANK2 variants to ACM in human probands. Giudicessi 2020 found no cardiomyopathy in their 12-variant referral cohort carrying historically alleged ABS variants, underscoring heterogeneity and disputed pathogenicity for some variants. (swayne2017novelvariantin pages 1-2, roberts2019ankyrinbdysfunctionpredisposes pages 9-10, roberts2019ankyrinbdysfunctionpredisposes pages 1-2, giudicessi2020establishedlossoffunctionvariants pages 1-5) | (swayne2017novelvariantin pages 1-2, roberts2019ankyrinbdysfunctionpredisposes pages 9-10, roberts2019ankyrinbdysfunctionpredisposes pages 1-2, giudicessi2020establishedlossoffunctionvariants pages 1-5) |
| Sudden cardiac death | Major adverse outcome and key reason for surveillance and family screening; can occur with electrical disease alone or in the setting of structural disease in some variant backgrounds. | HP:0001645 Sudden cardiac death | Mohler 2003 reported sudden cardiac death in the original kindred. Scouarnec 2008 described premature sudden deaths at ages 18 and 12 in Family 1. Swayne 2017 reported one cardiomyopathy-associated sudden death among p.S646F carriers. Korn 2023 described a family with 3 sudden cardiac deaths in the paternal line associated with ANK2 c.11791G>A plus MYO18B c.3761G>A. (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2, swayne2017novelvariantin pages 1-2, korn2023anewinherited pages 1-2) | (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2, swayne2017novelvariantin pages 1-2, korn2023anewinherited pages 1-2) |


*Table: This table summarizes the core cardiac manifestations reported in ANK2/ankyrin-B syndrome, with suggested HPO mappings and quantitative data from landmark family studies and later variant-specific cohorts. It is useful for structured disease-knowledge-base curation and phenotype annotation.*

### 3.2 Phenotype characteristics (onset, severity, progression)
* **Sinus node dysfunction (SND)** can be severe and highly penetrant in some families, sometimes requiring pacemakers; SND in the ANK2‑mapped kindreds included sinus bradycardia, sinus arrest/exit block, and tachyarrhythmias. (scouarnec2008dysfunctioninankyrinbdependent pages 1-2)
* **Atrial fibrillation (AF)** tends to present in adulthood in reported kindreds (mean onset ~40 ± 18 years in one family). (scouarnec2008dysfunctioninankyrinbdependent pages 1-2)
* **QTc prolongation** may be present in adults and children but can show incomplete penetrance, including non‑penetrant carriers with QTc ~420 ms in the original E1425G family. (mohler2003ankyrinbmutationcauses pages 1-2)
* **Ventricular arrhythmia susceptibility** can be catecholamine/stress‑dependent; in a KI mouse model, stress provoked ventricular arrhythmias in the absence of structural disease. (zhu2018ankyrinbq1283hvariant pages 1-2)
* **Structural heart disease / cardiomyopathy** is variably reported; some variant carriers show structural disease (e.g., 2/16 additional S646F carriers), while a referral reappraisal found no malignant echo findings in their ANK2 variant carriers, underscoring heterogeneity. (swayne2017novelvariantin pages 1-2, giudicessi2020establishedlossoffunctionvariants pages 1-5)

### 3.3 Quality of life impact
Disease impact is inferred from high‑burden arrhythmias, device therapy (pacemakers), and sudden death risk, but formal QoL instruments (e.g., SF‑36/EQ‑5D) were not reported in the retrieved evidence. (scouarnec2008dysfunctioninankyrinbdependent pages 1-2, mohler2003ankyrinbmutationcauses pages 1-2)

### 3.4 Visual clinical evidence (ECG examples)
Representative ECG panels from the original LQT4/ankyrin‑B syndrome report show bradycardia/sinus arrhythmia and atrial ectopy (premature atrial contractions). (mohler2003ankyrinbmutationcauses media 3330bf40, mohler2003ankyrinbmutationcauses media b13c3b4f)

## 4. Genetic / molecular information
### 4.1 Causal gene
**ANK2 (ankyrin 2)** encodes ankyrin‑B, a scaffold protein that directly binds key transporters/channels and recruits signaling complexes needed for normal cardiac electrical and Ca2+ handling function. (ackerman2010defininganew pages 2-3, koenig2017theevolvingrole pages 2-4)

### 4.2 Inheritance, penetrance, expressivity
* **Inheritance:** autosomal dominant (koenig2017theevolvingrole pages 2-4)
* **Penetrance:** incomplete (e.g., E1425G family: QT phenotype in 22/24 carriers; SND in 23/24 carriers; specific non‑penetrant examples reported). (mohler2003ankyrinbmutationcauses pages 1-2)
* **Expressivity:** variable, including electrical phenotypes with/without structural disease across variants/families. (swayne2017novelvariantin pages 1-2, york2022mechanismsunderlyingthe pages 1-2)

### 4.3 Pathogenic variant classes and examples
* Missense loss‑of‑function variants (e.g., E1425G/E1458G; S646F; Q1283H). (mohler2003ankyrinbmutationcauses pages 1-2, swayne2017novelvariantin pages 1-2, zhu2018ankyrinbq1283hvariant pages 1-2)
* Loss‑of‑function variants and heterozygous null alleles are implicated in reviews and models; variant interpretation is challenging because ANK2 has many rare variants in population datasets. (koenig2017theevolvingrole pages 2-4, giudicessi2020establishedlossoffunctionvariants pages 1-5, york2022mechanismsunderlyingthe pages 4-5)

| Variant (HGVS c./p.) | Domain/region (if known) | Evidence type (family, cohort, model) | Reported phenotypes | Quantitative notes (QTc, counts) | Pathogenicity/interpretation notes | Key citations |
|---|---|---|---|---|---|---|
| c.4274A>G, p.Glu1425Gly (historical) / p.Glu1458Gly (updated numbering), E1425G/E1458G | Near regulatory/C-terminal region; review places p.E1458G in spectrin-binding domain context | Large French family; segregation study; mouse/cardiomyocyte functional rescue model | Prolonged QTc/LQT4, sinus node dysfunction/bradycardia, atrial fibrillation, sudden cardiac death | 45 relatives screened; 24 carriers, 21 non-carriers; QT phenotype in 22/24 carriers; sinus node dysfunction in 23/24 carriers; 2 nonpenetrant QT carriers had QTc 420 ms; mean QTc adults ~490 ± 30 ms, children ~465 ± 38 ms | Landmark disease-defining ANK2 variant; functional loss-of-function/haploinsufficiency model supported. Later review/reappraisal notes incomplete penetrance and population observations complicating interpretation in some settings | (mohler2003ankyrinbmutationcauses pages 1-2, york2022mechanismsunderlyingthe pages 4-5) |
| c.1937C>T, p.Ser646Phe (p.S646F) | Membrane-binding domain (first disease-causing ANK2 variant mapped to this domain) | Multigenerational Gitxsan First Nation families; cascade screening; cultured cardiac cell/primary cardiomyocyte functional studies | Ankyrin-B syndrome/LQTS, ventricular arrhythmia risk, structural heart disease in some carriers, congenital heart disease, seizures reported in extended review | 16 additional carriers identified; average QTc 475 ± 40 ms; 2 carriers had structural heart disease (1 cardiomyopathy with sudden death, 1 congenital heart disease); review notes seizures in 8/18 carriers | Loss-of-function allele with reduced expression, abnormal localization, and failed Na/Ca exchanger targeting; possible founder effect in Gitxsan population with high LQTS prevalence | (swayne2017novelvariantin pages 1-2, york2022mechanismsunderlyingthe pages 5-6) |
| p.Q1283H | ZU5C region | Variant discovery in 25 Han Chinese VT probands; knock-in mouse model; single-cell cardiomyocyte mechanistic studies | Stress-induced ventricular arrhythmias/VT susceptibility without structural abnormalities | Identified in 25 unrelated VT probands screen; KI mice showed increased stress-induced ventricular arrhythmias; no human QTc summary provided in retrieved evidence | Disease-associated variant causing loss of local PP2A activity, increased RyR2 Ser2814 phosphorylation, delayed afterdepolarizations/Ca2+ waves; metoprolol or flecainide reduced stress-induced arrhythmias in mice | (zhu2018ankyrinbq1283hvariant pages 1-2, york2022mechanismsunderlyingthe pages 4-4) |
| p.Val3634Asp (historical p.Val1516Asp; V3634D) | C-terminal/regulatory region | Variant listed in historical ABS literature; re-evaluated in Mayo Clinic referral cohort | Usually mild or absent phenotype in reappraisal cohort; possible palpitations or nonspecific ECG findings | Giudicessi cohort: part of 12/1,727 referrals (0.7%) carrying 1 of 4 alleged ABS variants overall; across all 12 carriers, only 4/12 (33%) had potentially attributable symptoms, 67% asymptomatic, 6/12 (50%) had ≥1 ECG finding of uncertain significance; variant frequency comparison to gnomAD argued against enrichment | Reappraisal concluded alleged ABS variants such as p.V3634D are unlikely to cause a highly penetrant monogenic SCD syndrome by themselves; pathogenicity remains uncertain/likely overcalled in older literature | (giudicessi2020establishedlossoffunctionvariants pages 1-5, york2022mechanismsunderlyingthe pages 5-6) |
| p.Thr3744Asn (reported as p.T3744N/T3744ASN) | C-terminal/regulatory region | Historical alleged ABS variant; Mayo Clinic referral cohort reappraisal | Mostly low-penetrance or uncertain cardiac significance in available human reappraisal | Included among 4 alleged variants found in 12/1,727 referrals overall; combined carrier data: only 4/12 (33%) had potentially ABS-attributable symptoms and 6/12 (50%) had uncertain ECG findings | Considered an alleged ABS-causative variant with weak human penetrance evidence in reappraisal; observed in public/population datasets and lacking robust segregation support | (giudicessi2020establishedlossoffunctionvariants pages 1-5, york2022mechanismsunderlyingthe pages 4-4) |
| p.Arg3906Trp (p.R3906W) | C-terminal/regulatory region | Historical alleged ABS variant; Mayo Clinic referral cohort reappraisal | Mild/uncertain phenotype spectrum; no strong malignant phenotype enrichment in reappraisal | Included among the 12 carriers of 4 alleged variants in 1,727 referrals; aggregate carrier data showed low symptom burden and no overall enrichment vs gnomAD [12/1,727 (0.7%) vs 1,297/141,456 (0.9%)] | Reappraisal argues low penetrance and insufficient evidence for a penetrant monogenic SCD-predisposing role for many historical ABS variants, including p.R3906W | (giudicessi2020establishedlossoffunctionvariants pages 1-5, york2022mechanismsunderlyingthe pages 2-3) |
| p.Glu1458Gly (same variant family as historical E1425G; included in Giudicessi reappraisal) | Spectrin-binding/regulatory boundary in review context | Historical family-based disease report plus later referral-cohort reappraisal | Classical ankyrin-B syndrome in original pedigree vs often absent/mild findings in later referrals | In Giudicessi reappraisal, alleged variant carriers overall: 12/1,727 referrals; only 4/12 symptomatic, 67% asymptomatic; one variant-level comparison example 8/1,727 vs 150/141,456 in gnomAD (p=0.006) | Illustrates major interpretive tension in ANK2: a historically causal family variant can appear incompletely penetrant and not strongly enriched in broad referral cohorts, suggesting context dependence/possible oligogenic contribution | (giudicessi2020establishedlossoffunctionvariants pages 1-5, mohler2003ankyrinbmutationcauses pages 1-2, york2022mechanismsunderlyingthe pages 4-5) |


*Table: This table summarizes major ANK2 variants implicated in ankyrin-B syndrome and related cardiac phenotypes, combining landmark family studies with later variant reappraisal data. It is useful for comparing evidence strength, phenotype breadth, and the important issue of incomplete penetrance in ANK2-associated disease.*

### 4.4 Population frequency / founder effects
A First Nations Gitxsan population was reported to have a high rate of LQTS (~15× higher; ~1:125) and ANK2 p.S646F was reported in multigenerational families with a possible founder effect context. (swayne2017novelvariantin pages 1-2)

### 4.5 Modifier genes / protective variants
No specific modifier genes or protective variants were established in retrieved evidence.

### 4.6 Chromosomal abnormalities
A reciprocal chromosomal translocation mechanism for “human cardiac ankyrin‑B syndrome” is referenced in the retrieved corpus (Huq 2017), but detailed evidence extraction for that report was not obtained in the current evidence set. (No extracted context id available for mechanistic/phenotypic specifics beyond citation metadata.)

## 5. Environmental information
No specific toxic, occupational, lifestyle, or infectious drivers of ankyrin‑B syndrome were identified in retrieved evidence. The main non‑genetic influence supported by mechanistic evidence is **adrenergic/catecholaminergic stress** precipitating ventricular arrhythmias in susceptible genotypes. (zhu2018ankyrinbq1283hvariant pages 1-2, ackerman2010defininganew pages 2-3)

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic model (causal chain)
**Upstream trigger:** ANK2 loss‑of‑function (haploinsufficiency or functional missense variants). (mohler2003ankyrinbmutationcauses pages 1-2, ackerman2010defininganew pages 2-3)

**Core scaffold disruption:** ankyrin‑B normally binds/targets ion transporters/channels and signaling proteins—including **NCX1 (Na+/Ca2+ exchanger), NKA (Na+/K+ ATPase), IP3R, Kir6.2, and atrial Cav1.3**—and recruits **PP2A (via B56α)** to regulate multiple components of Ca2+ handling. (koenig2017theevolvingrole pages 2-4, koenig2017theevolvingrole pages 1-2)

**Cellular consequences (ventricular myocytes):** loss of ankyrin‑B disrupts membrane localization/expression of **NCX, NKA, IP3R**, producing defective intracellular Na+ and Ca2+ handling and SR Ca2+ overload; during catecholaminergic stimulation this promotes afterdepolarizations and polymorphic ventricular arrhythmias. (ackerman2010defininganew pages 2-3, wolf2010definingnewinsight pages 1-1)

**Quantitative cellular data (example):** in AnkB+/− cardiomyocytes, spontaneous contraction rate decreased from **144 ± 10 to 78 ± 8 bpm**, and Ca2+ transient frequency from **~2.7 Hz to ~1.3 Hz**; wild‑type ankyrin‑B rescued these abnormalities, while E1425G ankyrin‑B did not. (mohler2003ankyrinbmutationcauses pages 1-2)

**RyR2/PP2A signaling mechanism (stress‑induced VT model):** ANK2 p.Q1283H reduced ankyrin‑B binding to **PP2A B56α**, dissociated PP2A from **RyR2**, and increased **RyR2 Ser2814 phosphorylation**, leading to DADs, Ca2+ waves/sparks, and catecholamine‑triggered ventricular arrhythmias in KI mice. (zhu2018ankyrinbq1283hvariant pages 1-2)

**Atrial fibrillation mechanism:** ankyrin‑B deficiency reduces atrial **Cav1.3** (identified as an ankyrin‑binding partner), decreases L‑type Ca2+ current and shortens atrial APs, increasing AF susceptibility; reduced ankyrin‑B levels were also observed in human AF atrial tissue. (cunha2011defectsinankyrinbased pages 11-11)

**Sinoatrial node dysfunction mechanism:** ankyrin‑B is highly expressed in the SAN and required for proper channel/transporter targeting and membrane organization; dysfunction leads to abnormal Ca2+ handling, impaired automaticity, and bradycardia/escape rhythms. (scouarnec2008dysfunctioninankyrinbdependent pages 1-2)

### 6.2 Structural remodeling / cardiomyopathy pathway
A cardiac‑specific Ank2 conditional knockout model developed marked dilation, fibrosis and systolic dysfunction with abnormal β‑catenin patterning, supporting ankyrin‑B—β‑catenin signaling as a pathway to arrhythmogenic cardiomyopathy. (roberts2019ankyrinbdysfunctionpredisposes pages 9-10, roberts2019ankyrinbdysfunctionpredisposes pages 1-2)

**Preclinical targeted therapy evidence:** pharmacologic activation of WNT/β‑catenin signaling (GSK‑3β inhibitor **SB‑216763**) prevented and partially reversed cardiomyopathy phenotypes in Ank2‑cKO mice; figure panels show β‑catenin patterning differences and prevention/reversal of functional decline and fibrosis. (roberts2019ankyrinbdysfunctionpredisposes media 52e6c3c8, roberts2019ankyrinbdysfunctionpredisposes pages 9-10)

### 6.3 Suggested ontology terms (computable annotations)
**GO (Biological Process) candidates** (mechanistically implied by the evidence):
* GO:0010038 response to metal ion (general stress) is not specific; instead suggest: **calcium ion homeostasis**, **protein localization to membrane**, **regulation of cardiac conduction**, **regulation of heart rate**, **sarcoplasmic reticulum calcium ion transport** (supported by disrupted Ca2+ handling and transporter targeting). (ackerman2010defininganew pages 2-3, zhu2018ankyrinbq1283hvariant pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2)

**CL (Cell Ontology) candidates:**
* sinoatrial node pacemaker cell; atrial cardiomyocyte; ventricular cardiomyocyte (supported by SAN‑specific and atrial/ventricular mechanisms). (scouarnec2008dysfunctioninankyrinbdependent pages 1-2, cunha2011defectsinankyrinbased pages 11-11, ackerman2010defininganew pages 2-3)

**UBERON candidates:**
* sinoatrial node; atrial myocardium; ventricular myocardium; cardiac conduction system. (scouarnec2008dysfunctioninankyrinbdependent pages 1-2, cunha2011defectsinankyrinbased pages 11-11)

## 7. Anatomical structures affected
**Primary system:** cardiovascular conduction and myocardium.
* **Sinoatrial node / conduction system** (SND, bradycardia, escape rhythms, pacemaker requirement). (scouarnec2008dysfunctioninankyrinbdependent pages 1-2)
* **Atria** (atrial arrhythmias/AF; Cav1.3 mechanism; atrial ectopy shown on ECG). (cunha2011defectsinankyrinbased pages 11-11, mohler2003ankyrinbmutationcauses media 3330bf40)
* **Ventricles** (QT prolongation, ventricular arrhythmias; in some contexts cardiomyopathy/ACM remodeling). (mohler2003ankyrinbmutationcauses pages 1-2, roberts2019ankyrinbdysfunctionpredisposes pages 9-10)

## 8. Temporal development
* **Congenital/pediatric to adult onset:** QT prolongation and SND can be present early (including pediatric cases in family studies), whereas AF tends to present in adults in reported kindreds. (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2, york2022mechanismsunderlyingthe pages 5-6)
* **Course:** episodic arrhythmias with stress triggers for ventricular events; chronic bradycardia/SND may progress to pacemaker requirement. (zhu2018ankyrinbq1283hvariant pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2)

## 9. Inheritance and population
* **Autosomal dominant with incomplete penetrance and variable expressivity** is supported by family segregation and reviews. (mohler2003ankyrinbmutationcauses pages 1-2, koenig2017theevolvingrole pages 2-4, york2022mechanismsunderlyingthe pages 1-2)
* **Population prevalence/incidence:** a specific prevalence for ankyrin‑B syndrome is not available in the retrieved evidence. For context, LQTS overall prevalence is ~**1:2,000**. (spoonamore2016genetictestingand pages 6-10)
* **Founder effect / enriched populations:** Gitxsan First Nation high LQTS prevalence ~**1:125** with ANK2 p.S646F in families consistent with a founder context. (swayne2017novelvariantin pages 1-2)

## 10. Diagnostics
### 10.1 Clinical testing
Minimum or typical evaluation in inherited arrhythmia/genetic referrals includes:
* 12‑lead ECG, Holter monitoring, echocardiography, and treadmill exercise testing (used as a standardized test battery in ANK2 variant reappraisal). (giudicessi2020establishedlossoffunctionvariants pages 1-5)

### 10.2 Genetic testing and molecular autopsy
* Targeted arrhythmia gene panels (e.g., 42‑gene panel including ANK2; 174‑gene inherited cardiac disease panel on MiSeq) and WES (performed in the 2023 molecular‑autopsy family investigation) are used in real‑world settings. (haase2024asinglenucleotide pages 2-4, korn2023anewinherited pages 1-2)
* A consensus‑style principle for inherited arrhythmias is that a pathogenic variant in a LQTS gene can establish diagnosis regardless of ECG findings, motivating cascade testing; QTc‑based screening alone can miss genotype‑positive individuals. (spoonamore2016genetictestingand pages 6-10)

### 10.3 Differential diagnosis
Not exhaustively extracted in the current evidence set, but clinical differential commonly includes other inherited arrhythmia/channelopathy syndromes (e.g., other LQTS subtypes, CPVT, Brugada syndrome) because ANK2 phenotypes overlap and may present without consistent QT prolongation. (koenig2017theevolvingrole pages 2-4, giudicessi2020establishedlossoffunctionvariants pages 1-5)

## 11. Outcome / prognosis
* Sudden cardiac death is a central adverse outcome in multiple ANK2‑linked kindreds and recent reports. (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2, korn2023anewinherited pages 1-2)
* Prognostic statistics (e.g., long‑term survival curves) specific to ankyrin‑B syndrome were not identified in retrieved evidence; prognosis appears highly variant‑ and family‑dependent, and some alleged variants may confer low risk. (giudicessi2020establishedlossoffunctionvariants pages 1-5)

## 12. Treatment
### 12.1 Current clinical management (real‑world implementation)
Management is individualized based on phenotype (SND vs AF vs ventricular arrhythmias) and standard inherited arrhythmia practice, including:
* **Pacemaker implantation** for significant sinus node dysfunction/bradycardia (14 patients in one ANK2‑mapped SND family; pacing also used in the original LQT4 family). (scouarnec2008dysfunctioninankyrinbdependent pages 1-2, mohler2003ankyrinbmutationcauses pages 1-2)
* **Antiarrhythmic drugs** (e.g., flecainide, mexiletine in case‑based contexts; broader antiarrhythmic approaches in ACM). (haase2024asinglenucleotide pages 1-2, roberts2019ankyrinbdysfunctionpredisposes pages 9-10)
* **ICD** and **catheter ablation** in malignant ventricular arrhythmia/ACM contexts (palliative but potentially life‑saving). (roberts2019ankyrinbdysfunctionpredisposes pages 9-10)

### 12.2 Mechanism‑informed therapy evidence
* In a KI mouse model of ANK2 p.Q1283H, **metoprolol** or **flecainide** reduced stress‑induced ventricular arrhythmias, supporting adrenergic suppression and triggered‑activity suppression as rational approaches for catecholamine‑provoked disease components. (zhu2018ankyrinbq1283hvariant pages 1-2)

### 12.3 Targeted/experimental therapies
* WNT/β‑catenin activation with **SB‑216763** prevented/partially reversed Ank2‑cKO cardiomyopathy in mice, supporting a possible targeted therapy concept for ANK2‑related structural disease; there is no human clinical‑trial evidence in the retrieved set. (roberts2019ankyrinbdysfunctionpredisposes pages 9-10, roberts2019ankyrinbdysfunctionpredisposes media 52e6c3c8)

### 12.4 MAXO terms
See diagnostics/management table for suggested MAXO terms. (spoonamore2016genetictestingand pages 14-17, scouarnec2008dysfunctioninankyrinbdependent pages 1-2)

| Domain | Intervention/test | Details | Suggested MAXO term(s) where appropriate | Evidence notes/quantitative data | Key citations |
|---|---|---|---|---|---|
| Diagnostics | 12-lead ECG | Core first-line evaluation for QTc prolongation, sinus bradycardia/sinus arrhythmia, premature atrial beats, conduction disease, and ST-segment abnormalities in some newer ANK2-associated families | MAXO:0000001 clinical examination; MAXO:0000487 electrocardiography | Original E1425G family had mean QTc ~490 ± 30 ms in adults and ~465 ± 38 ms in children; ECG examples showed bradycardia/sinus arrhythmia and multiple premature atrial contractions; one 2024 case reported QT 470 ms | (mohler2003ankyrinbmutationcauses pages 1-2, mohler2003ankyrinbmutationcauses media 3330bf40, mohler2003ankyrinbmutationcauses media b13c3b4f, haase2024asinglenucleotide pages 2-4) |
| Diagnostics | Holter / ambulatory rhythm monitoring | Used to capture intermittent ventricular tachycardia, sinus-node dysfunction, escape rhythms, and atrial arrhythmias not evident on resting ECG | MAXO:0000487 electrocardiography | 24-hour Holter was used in 2023 family investigation; 2024 case used patch Holter/Kardia tracings showing salvos of VT | (korn2023anewinherited pages 1-2, haase2024asinglenucleotide pages 2-4) |
| Diagnostics | Exercise stress testing / treadmill testing | Helps reveal exercise- or catecholamine-associated ventricular ectopy/arrhythmia and may support phenotype clarification in inherited arrhythmia clinics | MAXO:0001024 exercise test | Giudicessi 2020 minimum evaluation included treadmill exercise testing in all referred individuals with alleged ANK2 variants; 2023 family workup included exercise ECGs | (giudicessi2020establishedlossoffunctionvariants pages 1-5, korn2023anewinherited pages 1-2) |
| Diagnostics | Transthoracic echocardiography | Used to exclude or define structural heart disease, cardiomyopathy, ventricular dysfunction, or congenital heart disease in ANK2 carriers | MAXO:0000372 echocardiography | Giudicessi 2020 included echocardiography in all cases; 2023 family evaluation used standard TTE; important because some ANK2 variants are associated with structural disease/ACM while others are not | (giudicessi2020establishedlossoffunctionvariants pages 1-5, korn2023anewinherited pages 1-2, swayne2017novelvariantin pages 1-2) |
| Diagnostics | Family history and pedigree assessment | Essential because disease is typically autosomal dominant with incomplete penetrance and variable expressivity | MAXO:0000127 genetic counseling | Mohler 2003 screened 45 relatives (24 carriers); Scouarnec 2008 screened 74 relatives and identified 25 affected by SND; 2023 multidisciplinary workup emphasized pedigree analysis | (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2, korn2023anewinherited pages 1-2) |
| Diagnostics | Targeted inherited-arrhythmia gene panel | Preferred clinical genetic approach in many inherited arrhythmia settings; can include ANK2 with other LQTS/SND/arrhythmia genes | MAXO:0000129 genetic testing | 2024 case used a 42-gene arrhythmia panel; 2023 molecular-autopsy/family workup used a 174-gene inherited-cardiac-disease panel on MiSeq; targeted panels are generally favored for depth and coverage | (haase2024asinglenucleotide pages 2-4, korn2023anewinherited pages 1-2, spoonamore2016genetictestingand pages 14-17) |
| Diagnostics | Whole-exome sequencing (WES) | Useful when phenotype is heterogeneous, syndromic, or panel testing is unrevealing; may help discover atypical ANK2-associated syndromes | MAXO:0000129 genetic testing | 2023 SCD family study performed WES on the index patient plus 2 affected relatives; general inherited-arrhythmia guidance notes WES is increasingly used but may have lower depth and incidental findings | (korn2023anewinherited pages 1-2, spoonamore2016genetictestingand pages 10-14, spoonamore2016genetictestingand pages 14-17) |
| Diagnostics | Variant interpretation (ACMG/ClinVar/gnomAD comparison) | Needed because ANK2 has disputed/low-penetrance variants and population frequency can complicate causality assessment | MAXO:0000129 genetic testing | 2023 family report used ACMG revised criteria; Giudicessi 2020 compared 1,727 referrals with gnomAD and found no overall enrichment of 4 alleged ABS variants [12/1,727 (0.7%) vs 1,297/141,456 (0.9%)] | (korn2023anewinherited pages 1-2, giudicessi2020establishedlossoffunctionvariants pages 1-5) |
| Diagnostics | Molecular autopsy | Post-mortem genetic testing in unexplained young sudden death to identify ANK2 and other inherited arrhythmia causes | MAXO:0000129 genetic testing | 2023 study combined autopsy, preserved heart analysis, gene panel testing, and WES; broader inherited-arrhythmia review notes postmortem molecular autopsy yields ~20–50% in cohorts and can be especially useful in pediatric SCD | (korn2023anewinherited pages 1-2, spoonamore2016genetictestingand pages 14-17) |
| Diagnostics / Prevention | Cascade screening of relatives | Genetic and clinical evaluation of at-risk relatives once a pathogenic/likely pathogenic familial variant is identified | MAXO:0000129 genetic testing; MAXO:0000127 genetic counseling | Recommended across inherited arrhythmia practice; relatives positive for the familial pathogenic variant should undergo surveillance, whereas genotype-negative relatives generally do not require surveillance; VUS should not be used for predictive testing | (spoonamore2016genetictestingand pages 14-17, spoonamore2016genetictestingand pages 6-10, scouarnec2008dysfunctioninankyrinbdependent pages 1-2) |
| Treatment | Beta-blockers | Mechanistically rational for catecholamine/stress-triggered ventricular arrhythmias in ANK2-related disease | MAXO:0000014 drug therapy; MAXO:0000120 beta-adrenergic receptor antagonist therapy | In the p.Q1283H knock-in model, metoprolol reduced stress-induced ventricular arrhythmias; 2024 ANK2-variant myocarditis case also reported suppression of VT with beta-blockers in combination therapy | (zhu2018ankyrinbq1283hvariant pages 1-2, haase2024asinglenucleotide pages 1-2) |
| Treatment | Flecainide | Antiarrhythmic option supported by preclinical ANK2 evidence for stress-induced VT susceptibility | MAXO:0000014 drug therapy; MAXO:0000058 anti-arrhythmic agent therapy | In p.Q1283H knock-in mice, flecainide decreased catecholamine-induced ventricular arrhythmias; a 2024 case report used flecainide early in management of recurrent VT | (zhu2018ankyrinbq1283hvariant pages 1-2, haase2024asinglenucleotide pages 1-2) |
| Treatment | Mexiletine | Used in a recent mechanistically selected case with ANK2 variant and VT; may be considered case-by-case rather than disease-standard therapy | MAXO:0000014 drug therapy; MAXO:0000058 anti-arrhythmic agent therapy | 2024 case report described mexiletine plus beta-blockers suppressing highly symptomatic VT and coinciding with QT normalization as myocarditis resolved | (haase2024asinglenucleotide pages 1-2) |
| Treatment | Pacemaker implantation | Important for severe sinus-node dysfunction/bradycardia in ANK2 families | MAXO:0000582 cardiac pacemaker implantation | Mohler 2003 noted some affected individuals required atrial pacing; Scouarnec 2008 reported pacemaker implantation in 14 patients from the mapped SND kindreds | (mohler2003ankyrinbmutationcauses pages 1-2, scouarnec2008dysfunctioninankyrinbdependent pages 1-2) |
| Treatment | Implantable cardioverter-defibrillator (ICD) | Used for prevention of sudden cardiac death in malignant ventricular arrhythmia syndromes / ACM settings when clinically indicated | MAXO:0000445 implantable cardioverter-defibrillator implantation | Roberts 2019 notes ICDs can be life-saving in ACM management, though such therapy is palliative and does not correct underlying ANK2 pathophysiology | (roberts2019ankyrinbdysfunctionpredisposes pages 9-10, roberts2019ankyrinbdysfunctionpredisposes pages 1-2) |
| Treatment | Catheter ablation | May be useful for suppression of malignant ventricular arrhythmias or recurrent arrhythmic burden in selected patients | MAXO:0000005 catheter-based procedure; MAXO:0000944 catheter ablation | Roberts 2019 notes catheter ablation may be effective in suppressing malignant ventricular arrhythmias in ACM, but does not target root disease mechanism | (roberts2019ankyrinbdysfunctionpredisposes pages 9-10, roberts2019ankyrinbdysfunctionpredisposes pages 1-2) |
| Treatment | Standard acute VT care (e.g., cardioversion; amiodarone in selected settings) | Relevant for unstable sustained VT regardless of ANK2 status; supportive rather than genotype-specific | MAXO:0000514 cardioversion; MAXO:0000014 drug therapy | 2024 case report explicitly discusses prompt cardioversion for hemodynamically unstable sustained VT and mentions amiodarone as an option for recurrent monomorphic VT | (haase2024asinglenucleotide pages 1-2) |
| Experimental treatment | SB-216763 / WNT-β-catenin pathway activation | Preclinical targeted therapy for ANK2-related arrhythmogenic cardiomyopathy caused by ankyrin-B dysfunction and abnormal β-catenin signaling | MAXO:0000014 drug therapy | In Ank2-cKO mice, SB-216763 prevented disease when started at 4 weeks and partially reversed established disease; figure evidence showed prevention/reversal of EF/FS decline and fibrosis; no human trial evidence retrieved | (roberts2019ankyrinbdysfunctionpredisposes pages 9-10, roberts2019ankyrinbdysfunctionpredisposes pages 1-2, roberts2019ankyrinbdysfunctionpredisposes media 52e6c3c8) |
| Prevention | Ongoing surveillance of ANK2 variant carriers | Serial clinical follow-up for arrhythmia and cardiomyopathy given incomplete penetrance and age-dependent expression | MAXO:0000408 monitoring | York 2022 recommends monitoring carriers of functional ANK2 variants for arrhythmia and cardiomyopathy; inherited-arrhythmia guidance recommends surveillance for relatives who carry the familial pathogenic variant | (york2022mechanismsunderlyingthe pages 14-16, spoonamore2016genetictestingand pages 14-17) |
| Prevention | Genetic counseling / family planning counseling | Important because disease is usually autosomal dominant and expression is variable | MAXO:0000127 genetic counseling | General inherited-arrhythmia guidance recommends testing/counseling at diagnosis, at transition of care, and during family planning; counseling is also crucial when ANK2 findings are VUS or low-penetrance alleles | (spoonamore2016genetictestingand pages 10-14, spoonamore2016genetictestingand pages 14-17, giudicessi2020establishedlossoffunctionvariants pages 1-5) |


*Table: This table summarizes the main diagnostic tests, genetic workflows, management strategies, and prevention measures reported or recommended for ANK2/ankyrin-B syndrome. It integrates primary family studies, recent case reports, and inherited-arrhythmia practice guidance, while distinguishing established clinical care from preclinical ANK2-targeted therapy.*

## 13. Prevention
* **Cascade screening** and **genetic counseling** are central preventive strategies in inherited arrhythmias, enabling early identification and surveillance of at‑risk relatives when a pathogenic familial variant is known; VUS results should not be used for predictive testing. (spoonamore2016genetictestingand pages 14-17)
* **Surveillance** is recommended because of incomplete penetrance/age‑dependent expression and possible cardiomyopathy risk in some variants: “monitoring carriers of ANK2 functional variants for arrhythmia and cardiomyopathy” is emphasized in review guidance. (york2022mechanismsunderlyingthe pages 14-16)

## 14. Other species / natural disease
Naturally occurring ankyrin‑B syndrome analogs in companion animals or livestock were not identified in the retrieved evidence.

## 15. Model organisms
Multiple experimental models support mechanism and therapy development:
* **AnkB+/− mice and neonatal cardiomyocytes**: bradycardia, HR variability, Ca2+‑handling defects, and sudden death; rescue with WT ankyrin‑B but not E1425G ankyrin‑B. (mohler2003ankyrinbmutationcauses pages 1-2)
* **ANK2‑linked SND family model alignment**: AnkB+/− mice phenocopy severe SND with bradycardia and HR variability. (scouarnec2008dysfunctioninankyrinbdependent pages 1-2)
* **p.Q1283H knock‑in mice**: catecholamine‑triggered ventricular arrhythmias via PP2A–RyR2 dysregulation and RyR2 Ser2814 hyperphosphorylation; responsive to metoprolol/flecainide in vivo. (zhu2018ankyrinbq1283hvariant pages 1-2)
* **Cardiac‑specific Ank2 conditional knockout (Ank2‑cKO)**: structural remodeling/ACM phenotype linked to β‑catenin patterning; preventable/reversible with SB‑216763 in mice. (roberts2019ankyrinbdysfunctionpredisposes pages 9-10, roberts2019ankyrinbdysfunctionpredisposes media 52e6c3c8)

**Model limitations (from retrieved evidence):** global Ank2 knockout is lethal; some murine cardiomyopathy models do not recapitulate fatty infiltration; adult cardiomyocytes are difficult to transfect, affecting rescue assay design. (york2022mechanismsunderlyingthe pages 9-10, mohler2003ankyrinbmutationcauses pages 1-2, roberts2019ankyrinbdysfunctionpredisposes pages 9-10)

## Expert interpretation and current controversies
A key contemporary issue is the **interpretation of ANK2 variants**: while some variants (e.g., the original E1425G family) show strong segregation and compelling functional evidence, a referral cohort reappraisal found that several historically alleged ankyrin‑B syndrome variants were not enriched compared with population databases and often had minimal phenotype, leading to the conclusion they are “unlikely to result in a penetrant, monogenic SCD‑predisposing condition” in many cases. This supports a clinical stance emphasizing careful variant classification, segregation testing, and phenotype‑driven management rather than assuming high risk for all rare ANK2 variants. (giudicessi2020establishedlossoffunctionvariants pages 1-5, mohler2003ankyrinbmutationcauses pages 1-2)

## Key 2023–2024 updates (prioritized)
* **Dec 2023:** A reported inherited syndrome with sudden cardiac death and distinct ST‑segment depression involved ANK2 c.11791G>A plus MYO18B c.3761G>A, investigated through multidisciplinary autopsy plus 174‑gene panel sequencing and WES. (korn2023anewinherited pages 1-2)
* **May 2024:** A case of COVID‑19 myocarditis complicated by recurrent VT reported an ANK2 SNV and described use of mechanistically selected antiarrhythmics (mexiletine) plus beta‑blockers and a 42‑gene arrhythmia panel workflow. (haase2024asinglenucleotide pages 2-4)

## Data gaps for a knowledge base entry (explicit)
* Disease‑specific MONDO/Orphanet/ICD identifiers were not found in the retrieved evidence set. (york2022mechanismsunderlyingthe pages 1-2)
* Robust ankyrin‑B syndrome‑specific prevalence/incidence, survival, and standardized quality‑of‑life metrics were not identified in retrieved evidence. (spoonamore2016genetictestingand pages 6-10, giudicessi2020establishedlossoffunctionvariants pages 1-5)
* No ANK2‑specific interventional clinical trials for cardiac ankyrin‑B syndrome were retrieved; targeted therapy evidence remains preclinical. (roberts2019ankyrinbdysfunctionpredisposes media 52e6c3c8, roberts2019ankyrinbdysfunctionpredisposes pages 9-10)


References

1. (mohler2003ankyrinbmutationcauses pages 1-2): Peter J. Mohler, Jean-Jacques Schott, Anthony O. Gramolini, Keith W. Dilly, Silvia Guatimosim, William H. duBell, Long-Sheng Song, Karine Haurogné, Florence Kyndt, Mervat E. Ali, Terry B. Rogers, W. J. Lederer, Denis Escande, Herve Le Marec, and Vann Bennett. Ankyrin-b mutation causes type 4 long-qt cardiac arrhythmia and sudden cardiac death. Nature, 421:634-639, Feb 2003. URL: https://doi.org/10.1038/nature01335, doi:10.1038/nature01335. This article has 1267 citations and is from a highest quality peer-reviewed journal.

2. (koenig2017theevolvingrole pages 2-4): Sara N. Koenig and Peter J. Mohler. The evolving role of ankyrin-b in cardiovascular disease. Heart rhythm, 14 12:1884-1889, Dec 2017. URL: https://doi.org/10.1016/j.hrthm.2017.07.032, doi:10.1016/j.hrthm.2017.07.032. This article has 62 citations and is from a peer-reviewed journal.

3. (york2022mechanismsunderlyingthe pages 1-2): Nicole S. York, Juan C. Sanchez-Arias, Alexa C. H. McAdam, Joel E. Rivera, Laura T. Arbour, and Leigh Anne Swayne. Mechanisms underlying the role of ankyrin-b in cardiac and neurological health and disease. Frontiers in Cardiovascular Medicine, Aug 2022. URL: https://doi.org/10.3389/fcvm.2022.964675, doi:10.3389/fcvm.2022.964675. This article has 20 citations and is from a peer-reviewed journal.

4. (sucharski2020mechanismsandalterations pages 1-2): Holly C. Sucharski, Emma K. Dudley, Caullin B.R. Keith, Mona El Refaey, Sara N. Koenig, and Peter J. Mohler. Mechanisms and alterations of cardiac ion channels leading to disease: role of ankyrin-b in cardiac function. Biomolecules, 10:211, Jan 2020. URL: https://doi.org/10.3390/biom10020211, doi:10.3390/biom10020211. This article has 37 citations.

5. (ackerman2010defininganew pages 2-3): Michael J. Ackerman and Peter J. Mohler. Defining a new paradigm for human arrhythmia syndromes: phenotypic manifestations of gene mutations in ion channel- and transporter-associated proteins. Circulation research, 107 4:457-65, Aug 2010. URL: https://doi.org/10.1161/circresaha.110.224592, doi:10.1161/circresaha.110.224592. This article has 92 citations and is from a highest quality peer-reviewed journal.

6. (scouarnec2008dysfunctioninankyrinbdependent pages 1-2): Solena Le Scouarnec, Naina Bhasin, Claude Vieyres, Thomas J. Hund, Shane R. Cunha, Olha Koval, Celine Marionneau, Biyi Chen, Yuejin Wu, Sophie Demolombe, Long-Sheng Song, Hervé Le Marec, Vincent Probst, Jean-Jacques Schott, Mark E. Anderson, and Peter J. Mohler. Dysfunction in ankyrin-b-dependent ion channel and transporter targeting causes human sinus node disease. Proceedings of the National Academy of Sciences, 105:15617-15622, Oct 2008. URL: https://doi.org/10.1073/pnas.0805500105, doi:10.1073/pnas.0805500105. This article has 202 citations and is from a highest quality peer-reviewed journal.

7. (giudicessi2020establishedlossoffunctionvariants pages 1-5): John R. Giudicessi and Michael J. Ackerman. Established loss-of-function variants in <i>ank2</i> -encoded ankyrin-b rarely cause a concerning cardiac phenotype in humans. Circulation: Genomic and Precision Medicine, Apr 2020. URL: https://doi.org/10.1161/circgen.119.002851, doi:10.1161/circgen.119.002851. This article has 10 citations.

8. (zhu2018ankyrinbq1283hvariant pages 1-2): Wengen Zhu, Cen Wang, Jinzhu Hu, Rong Wan, Jianhua Yu, Jinyan Xie, Jianyong Ma, Linjuan Guo, Jin Ge, Yumin Qiu, Leifeng Chen, Hualong Liu, Xia Yan, Xiuxia Liu, Jin Ye, Wenfeng He, Yang Shen, Chao Wang, Peter J. Mohler, and Kui Hong. Ankyrin-b q1283h variant linked to arrhythmias via loss of local protein phosphatase 2a activity causes ryanodine receptor hyperphosphorylation. Circulation, 138:2682-2697, Dec 2018. URL: https://doi.org/10.1161/circulationaha.118.034541, doi:10.1161/circulationaha.118.034541. This article has 24 citations and is from a highest quality peer-reviewed journal.

9. (roberts2019ankyrinbdysfunctionpredisposes pages 9-10): Jason D. Roberts, Nathaniel P. Murphy, Robert M. Hamilton, Ellen R. Lubbers, Cynthia A. James, Crystal F. Kline, Michael H. Gollob, Andrew D. Krahn, Amy C. Sturm, Hassan Musa, Mona El-Refaey, Sara Koenig, Meriam Åström Aneq, Edgar T. Hoorntje, Sharon L. Graw, Robert W. Davies, Muhammad Arshad Rafiq, Tamara T. Koopmann, Shabana Aafaqi, Meena Fatah, David A. Chiasson, Matthew R.G. Taylor, Samantha L. Simmons, Mei Han, Chantal J.M. van Opbergen, Loren E. Wold, Gianfranco Sinagra, Kirti Mittal, Crystal Tichnell, Brittney Murray, Alberto Codima, Babak Nazer, Duy T. Nguyen, Frank I. Marcus, Nara Sobriera, Elisabeth M. Lodder, Maarten P. van den Berg, Danna A. Spears, John F. Robinson, Philip C. Ursell, Anna K. Green, Allan C. Skanes, Anthony S. Tang, Martin J. Gardner, Robert A. Hegele, Toon A.B. van Veen, Arthur A.M. Wilde, Jeff S. Healey, Paul M.L. Janssen, Luisa Mestroni, J. Peter van Tintelen, Hugh Calkins, Daniel P. Judge, Thomas J. Hund, Melvin M. Scheinman, and Peter J. Mohler. Ankyrin-b dysfunction predisposes to arrhythmogenic cardiomyopathy and is amenable to therapy. The Journal of clinical investigation, 130:3171-3184, Jul 2019. URL: https://doi.org/10.1172/jci125538, doi:10.1172/jci125538. This article has 69 citations.

10. (swayne2017novelvariantin pages 1-2): Leigh Anne Swayne, Nathaniel P. Murphy, Sirisha Asuri, Lena Chen, Xiaoxue Xu, Sarah McIntosh, Chao Wang, Peter J. Lancione, Jason D. Roberts, Charles Kerr, Shubhayan Sanatani, Elizabeth Sherwin, Crystal F. Kline, Mingjie Zhang, Peter J. Mohler, and Laura T. Arbour. Novel variant in the ank2 membrane-binding domain is associated with ankyrin-b syndrome and structural heart disease in a first nations population with a high rate of long qt syndrome. Circulation: Cardiovascular Genetics, 10:e001537, Feb 2017. URL: https://doi.org/10.1161/circgenetics.116.001537, doi:10.1161/circgenetics.116.001537. This article has 62 citations.

11. (york2022mechanismsunderlyingthe pages 4-5): Nicole S. York, Juan C. Sanchez-Arias, Alexa C. H. McAdam, Joel E. Rivera, Laura T. Arbour, and Leigh Anne Swayne. Mechanisms underlying the role of ankyrin-b in cardiac and neurological health and disease. Frontiers in Cardiovascular Medicine, Aug 2022. URL: https://doi.org/10.3389/fcvm.2022.964675, doi:10.3389/fcvm.2022.964675. This article has 20 citations and is from a peer-reviewed journal.

12. (mohler2003ankyrinbmutationcauses media 3330bf40): Peter J. Mohler, Jean-Jacques Schott, Anthony O. Gramolini, Keith W. Dilly, Silvia Guatimosim, William H. duBell, Long-Sheng Song, Karine Haurogné, Florence Kyndt, Mervat E. Ali, Terry B. Rogers, W. J. Lederer, Denis Escande, Herve Le Marec, and Vann Bennett. Ankyrin-b mutation causes type 4 long-qt cardiac arrhythmia and sudden cardiac death. Nature, 421:634-639, Feb 2003. URL: https://doi.org/10.1038/nature01335, doi:10.1038/nature01335. This article has 1267 citations and is from a highest quality peer-reviewed journal.

13. (mohler2003ankyrinbmutationcauses media b13c3b4f): Peter J. Mohler, Jean-Jacques Schott, Anthony O. Gramolini, Keith W. Dilly, Silvia Guatimosim, William H. duBell, Long-Sheng Song, Karine Haurogné, Florence Kyndt, Mervat E. Ali, Terry B. Rogers, W. J. Lederer, Denis Escande, Herve Le Marec, and Vann Bennett. Ankyrin-b mutation causes type 4 long-qt cardiac arrhythmia and sudden cardiac death. Nature, 421:634-639, Feb 2003. URL: https://doi.org/10.1038/nature01335, doi:10.1038/nature01335. This article has 1267 citations and is from a highest quality peer-reviewed journal.

14. (roberts2019ankyrinbdysfunctionpredisposes pages 1-2): Jason D. Roberts, Nathaniel P. Murphy, Robert M. Hamilton, Ellen R. Lubbers, Cynthia A. James, Crystal F. Kline, Michael H. Gollob, Andrew D. Krahn, Amy C. Sturm, Hassan Musa, Mona El-Refaey, Sara Koenig, Meriam Åström Aneq, Edgar T. Hoorntje, Sharon L. Graw, Robert W. Davies, Muhammad Arshad Rafiq, Tamara T. Koopmann, Shabana Aafaqi, Meena Fatah, David A. Chiasson, Matthew R.G. Taylor, Samantha L. Simmons, Mei Han, Chantal J.M. van Opbergen, Loren E. Wold, Gianfranco Sinagra, Kirti Mittal, Crystal Tichnell, Brittney Murray, Alberto Codima, Babak Nazer, Duy T. Nguyen, Frank I. Marcus, Nara Sobriera, Elisabeth M. Lodder, Maarten P. van den Berg, Danna A. Spears, John F. Robinson, Philip C. Ursell, Anna K. Green, Allan C. Skanes, Anthony S. Tang, Martin J. Gardner, Robert A. Hegele, Toon A.B. van Veen, Arthur A.M. Wilde, Jeff S. Healey, Paul M.L. Janssen, Luisa Mestroni, J. Peter van Tintelen, Hugh Calkins, Daniel P. Judge, Thomas J. Hund, Melvin M. Scheinman, and Peter J. Mohler. Ankyrin-b dysfunction predisposes to arrhythmogenic cardiomyopathy and is amenable to therapy. The Journal of clinical investigation, 130:3171-3184, Jul 2019. URL: https://doi.org/10.1172/jci125538, doi:10.1172/jci125538. This article has 69 citations.

15. (korn2023anewinherited pages 1-2): Hubertus von Korn, Cristina Basso, Kalliopi Pilichou, Victor Stefan, and Patrick Swojanowsky. A new inherited syndrome causing sudden cardiac death with distinct st-segment depression and ankyrin-2-mutation. The Application of Clinical Genetics, 16:233-239, Dec 2023. URL: https://doi.org/10.2147/tacg.s438957, doi:10.2147/tacg.s438957. This article has 0 citations.

16. (york2022mechanismsunderlyingthe pages 5-6): Nicole S. York, Juan C. Sanchez-Arias, Alexa C. H. McAdam, Joel E. Rivera, Laura T. Arbour, and Leigh Anne Swayne. Mechanisms underlying the role of ankyrin-b in cardiac and neurological health and disease. Frontiers in Cardiovascular Medicine, Aug 2022. URL: https://doi.org/10.3389/fcvm.2022.964675, doi:10.3389/fcvm.2022.964675. This article has 20 citations and is from a peer-reviewed journal.

17. (york2022mechanismsunderlyingthe pages 4-4): Nicole S. York, Juan C. Sanchez-Arias, Alexa C. H. McAdam, Joel E. Rivera, Laura T. Arbour, and Leigh Anne Swayne. Mechanisms underlying the role of ankyrin-b in cardiac and neurological health and disease. Frontiers in Cardiovascular Medicine, Aug 2022. URL: https://doi.org/10.3389/fcvm.2022.964675, doi:10.3389/fcvm.2022.964675. This article has 20 citations and is from a peer-reviewed journal.

18. (york2022mechanismsunderlyingthe pages 2-3): Nicole S. York, Juan C. Sanchez-Arias, Alexa C. H. McAdam, Joel E. Rivera, Laura T. Arbour, and Leigh Anne Swayne. Mechanisms underlying the role of ankyrin-b in cardiac and neurological health and disease. Frontiers in Cardiovascular Medicine, Aug 2022. URL: https://doi.org/10.3389/fcvm.2022.964675, doi:10.3389/fcvm.2022.964675. This article has 20 citations and is from a peer-reviewed journal.

19. (koenig2017theevolvingrole pages 1-2): Sara N. Koenig and Peter J. Mohler. The evolving role of ankyrin-b in cardiovascular disease. Heart rhythm, 14 12:1884-1889, Dec 2017. URL: https://doi.org/10.1016/j.hrthm.2017.07.032, doi:10.1016/j.hrthm.2017.07.032. This article has 62 citations and is from a peer-reviewed journal.

20. (wolf2010definingnewinsight pages 1-1): Roseanne M. Wolf, Colleen C. Mitchell, Matthew D. Christensen, Peter J. Mohler, and Thomas J. Hund. Defining new insight into atypical arrhythmia: a computational model of ankyrin-b syndrome. American journal of physiology. Heart and circulatory physiology, 299 5:H1505-14, Nov 2010. URL: https://doi.org/10.1152/ajpheart.00503.2010, doi:10.1152/ajpheart.00503.2010. This article has 12 citations.

21. (cunha2011defectsinankyrinbased pages 11-11): Shane R. Cunha, Thomas J. Hund, Seyed Hashemi, Niels Voigt, Na Li, Patrick Wright, Olha Koval, Jingdong Li, Hjalti Gudmundsson, Richard J. Gumina, Matthias Karck, Jean-Jacques Schott, Vincent Probst, Herve Le Marec, Mark E. Anderson, Dobromir Dobrev, Xander H.T. Wehrens, and Peter J. Mohler. Defects in ankyrin-based membrane protein targeting pathways underlie atrial fibrillation. Circulation, 124:1212–1222, Sep 2011. URL: https://doi.org/10.1161/circulationaha.111.023986, doi:10.1161/circulationaha.111.023986. This article has 140 citations and is from a highest quality peer-reviewed journal.

22. (roberts2019ankyrinbdysfunctionpredisposes media 52e6c3c8): Jason D. Roberts, Nathaniel P. Murphy, Robert M. Hamilton, Ellen R. Lubbers, Cynthia A. James, Crystal F. Kline, Michael H. Gollob, Andrew D. Krahn, Amy C. Sturm, Hassan Musa, Mona El-Refaey, Sara Koenig, Meriam Åström Aneq, Edgar T. Hoorntje, Sharon L. Graw, Robert W. Davies, Muhammad Arshad Rafiq, Tamara T. Koopmann, Shabana Aafaqi, Meena Fatah, David A. Chiasson, Matthew R.G. Taylor, Samantha L. Simmons, Mei Han, Chantal J.M. van Opbergen, Loren E. Wold, Gianfranco Sinagra, Kirti Mittal, Crystal Tichnell, Brittney Murray, Alberto Codima, Babak Nazer, Duy T. Nguyen, Frank I. Marcus, Nara Sobriera, Elisabeth M. Lodder, Maarten P. van den Berg, Danna A. Spears, John F. Robinson, Philip C. Ursell, Anna K. Green, Allan C. Skanes, Anthony S. Tang, Martin J. Gardner, Robert A. Hegele, Toon A.B. van Veen, Arthur A.M. Wilde, Jeff S. Healey, Paul M.L. Janssen, Luisa Mestroni, J. Peter van Tintelen, Hugh Calkins, Daniel P. Judge, Thomas J. Hund, Melvin M. Scheinman, and Peter J. Mohler. Ankyrin-b dysfunction predisposes to arrhythmogenic cardiomyopathy and is amenable to therapy. The Journal of clinical investigation, 130:3171-3184, Jul 2019. URL: https://doi.org/10.1172/jci125538, doi:10.1172/jci125538. This article has 69 citations.

23. (spoonamore2016genetictestingand pages 6-10): Katherine G. Spoonamore and Stephanie M. Ware. Genetic testing and genetic counseling in patients with sudden death risk due to heritable arrhythmias. Heart rhythm, 13 3:789-97, Mar 2016. URL: https://doi.org/10.1016/j.hrthm.2015.11.013, doi:10.1016/j.hrthm.2015.11.013. This article has 41 citations and is from a peer-reviewed journal.

24. (haase2024asinglenucleotide pages 2-4): Erin Haase, Chandana Kulkarni, Peyton Moore, Akash Ramanathan, and Mohanakrishnan Sathyamoorthy. A single nucleotide variant in ankyrin-2 influencing ventricular tachycardia in covid-19 associated myocarditis. Cardiogenetics, 14:84-92, May 2024. URL: https://doi.org/10.3390/cardiogenetics14020007, doi:10.3390/cardiogenetics14020007. This article has 0 citations.

25. (haase2024asinglenucleotide pages 1-2): Erin Haase, Chandana Kulkarni, Peyton Moore, Akash Ramanathan, and Mohanakrishnan Sathyamoorthy. A single nucleotide variant in ankyrin-2 influencing ventricular tachycardia in covid-19 associated myocarditis. Cardiogenetics, 14:84-92, May 2024. URL: https://doi.org/10.3390/cardiogenetics14020007, doi:10.3390/cardiogenetics14020007. This article has 0 citations.

26. (spoonamore2016genetictestingand pages 14-17): Katherine G. Spoonamore and Stephanie M. Ware. Genetic testing and genetic counseling in patients with sudden death risk due to heritable arrhythmias. Heart rhythm, 13 3:789-97, Mar 2016. URL: https://doi.org/10.1016/j.hrthm.2015.11.013, doi:10.1016/j.hrthm.2015.11.013. This article has 41 citations and is from a peer-reviewed journal.

27. (spoonamore2016genetictestingand pages 10-14): Katherine G. Spoonamore and Stephanie M. Ware. Genetic testing and genetic counseling in patients with sudden death risk due to heritable arrhythmias. Heart rhythm, 13 3:789-97, Mar 2016. URL: https://doi.org/10.1016/j.hrthm.2015.11.013, doi:10.1016/j.hrthm.2015.11.013. This article has 41 citations and is from a peer-reviewed journal.

28. (york2022mechanismsunderlyingthe pages 14-16): Nicole S. York, Juan C. Sanchez-Arias, Alexa C. H. McAdam, Joel E. Rivera, Laura T. Arbour, and Leigh Anne Swayne. Mechanisms underlying the role of ankyrin-b in cardiac and neurological health and disease. Frontiers in Cardiovascular Medicine, Aug 2022. URL: https://doi.org/10.3389/fcvm.2022.964675, doi:10.3389/fcvm.2022.964675. This article has 20 citations and is from a peer-reviewed journal.

29. (york2022mechanismsunderlyingthe pages 9-10): Nicole S. York, Juan C. Sanchez-Arias, Alexa C. H. McAdam, Joel E. Rivera, Laura T. Arbour, and Leigh Anne Swayne. Mechanisms underlying the role of ankyrin-b in cardiac and neurological health and disease. Frontiers in Cardiovascular Medicine, Aug 2022. URL: https://doi.org/10.3389/fcvm.2022.964675, doi:10.3389/fcvm.2022.964675. This article has 20 citations and is from a peer-reviewed journal.