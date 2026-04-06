---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:24:59.245636'
end_time: '2026-04-04T12:35:32.888865'
duration_seconds: 633.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: RYR2 CPVT
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RYR2 CPVT
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **RYR2 CPVT** covering all of the
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
- **Disease Name:** RYR2 CPVT
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **RYR2 CPVT** covering all of the
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


## Research report: RYR2-mediated catecholaminergic polymorphic ventricular tachycardia (RYR2-CPVT / CPVT1)

### Scope and evidence types
This report focuses on RYR2-mediated catecholaminergic polymorphic ventricular tachycardia (CPVT1), integrating 2023–2024 narrative reviews, pediatric observational cohorts/series, mechanistic structural/physiology studies, and ClinicalTrials.gov interventional trial records. Evidence sources here are aggregated disease-level resources (reviews and cohorts) rather than EHR-derived single-patient records, except where explicitly noted as case series. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, peltenburg2024prognosisandclinical pages 1-2, lee2024treatmentoutcomesin pages 1-2, jurisic2023catecholaminergicpolymorphicventricular pages 1-2)

| Disease name | Common synonyms / alternative names | Primary causal gene | Typical inheritance | Typical triggers | Key diagnostic test | Citation |
|---|---|---|---|---|---|---|
| RYR2-mediated catecholaminergic polymorphic ventricular tachycardia | CPVT; CPVT1; RYR2-CPVT; catecholaminergic polymorphic ventricular tachycardia type 1; RYR2-related CPVT | RYR2 | Autosomal dominant | Exercise, acute emotional stress, catecholaminergic stimulation | Exercise stress test to provoke polymorphic/bidirectional ventricular arrhythmias; epinephrine challenge if exercise testing is not feasible | (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4, aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, aggarwal2024catecholaminergicpolymorphicventricular pages 6-8, peltenburg2024prognosisandclinical pages 1-2) |


*Table: This table summarizes the core naming and identification fields for RYR2-mediated CPVT, including synonyms, causal gene, inheritance, triggers, and the principal diagnostic test. It is useful as a compact normalization artifact for a disease knowledge base entry.*

---

## 1. Disease information

### 1.1 Concise overview (current understanding)
RYR2-mediated CPVT is an inherited cardiac arrhythmia syndrome characterized by adrenergically triggered ventricular arrhythmias—classically bidirectional or polymorphic ventricular tachycardia—occurring in the absence of structural heart disease and typically with a normal resting ECG. Clinical presentations include exercise- or emotion-triggered syncope and risk of sudden cardiac death. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, peltenburg2024prognosisandclinical pages 1-2)

### 1.2 Identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
The retrieved literature set did not include OMIM, Orphanet, MeSH, ICD-10/ICD-11, or MONDO identifier pages/records, so these identifiers cannot be verified or cited from primary database sources within the current tool context. (Evidence gap in retrieved documents.)

### 1.3 Synonyms/alternative names
Common synonyms include CPVT, CPVT1, RYR2-CPVT, and catecholaminergic polymorphic ventricular tachycardia type 1. (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4, peltenburg2024prognosisandclinical pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline pathogenic or likely pathogenic variants in **RYR2**, encoding the cardiac ryanodine receptor (RyR2), a sarcoplasmic reticulum (SR) Ca2+ release channel. The dominant mechanism emphasized in recent reviews is RyR2 dysfunction leading to **diastolic SR Ca2+ leak** and triggered arrhythmias under catecholaminergic stimulation. (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4, peltenburg2024prognosisandclinical pages 1-2)

### 2.2 Risk factors
**Genetic risk factors**
- **Autosomal dominant inheritance** is typical for RYR2-mediated CPVT. (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4)
- **Variant class/type:** Most pathogenic RYR2 variants associated with CPVT are **missense** and are described as **gain-of-function** (in one review, ~96% missense). (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4)
- **Penetrance:** Reviews summarize high but incomplete penetrance for RYR2-mediated disease, approximately **~75–80%**. (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4)
- **De novo variants** are described as common in some monogenic RYR2 cases and associated with earlier and more severe phenotypes. (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4, peltenburg2024prognosisandclinical pages 1-2)

**Non-genetic/clinical risk factors (phenotype triggers)**
- **Exercise and emotional stress** are the dominant triggers, consistent with catecholamine-dependent arrhythmogenesis. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, peltenburg2024prognosisandclinical pages 1-2)

### 2.3 Protective factors
Direct protective factors (genetic or environmental) were not explicitly identified/quantified in the retrieved sources.

### 2.4 Gene–environment interactions
A central, well-supported interaction is **genotype (RYR2 dysfunction) × catecholaminergic environment (exercise/emotion, adrenergic stimulation)** leading to arrhythmia provocation. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, peltenburg2024prognosisandclinical pages 1-2)

---

## 3. Phenotypes

### 3.1 Core clinical phenotype spectrum (with onset, severity, progression)
**Typical presentation:** exertion- or emotion-triggered syncope; palpitations may occur; ventricular tachyarrhythmias can degenerate to ventricular fibrillation and sudden death. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, aggarwal2024catecholaminergicpolymorphicventricular pages 2-4)

**Age of onset:** pediatric predominance, with mean onset in one review **7–12 years** and **>60%** experiencing their first syncope/cardiac arrest by **age 20**. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2)

**Episodic nature:** events are often episodic and triggered, rather than continuously progressive; however, untreated disease is described as highly lethal with substantial pre-diagnosis syncope/cardiac arrest burden. (aggarwal2024catecholaminergicpolymorphicventricular pages 8-9)

**Atrial arrhythmias and sinus node dysfunction:** RYR2 mutation carriers can present with broader rhythm phenotypes (including sinoatrial node dysfunction and atrial arrhythmias), particularly in children. (wang2024clinicalcharacteristicsand pages 7-8)

### 3.2 Frequency among affected individuals (recent study statistics)
- In a 2024 Korean pediatric cohort (n=23), **73.9%** developed cardiac events, **43.5%** had aborted cardiac arrest, and **21.7%** died during follow-up (mean follow-up 9.4±6.5 years). (lee2024treatmentoutcomesin pages 7-9)
- In a 2023 Chinese pediatric cohort/review of 95 children, **13 deaths** were reported during the disease course; RYR2 variants were **70.1%** of genotyped cases (47/67). (yan2023clinicalandgenetic pages 1-2)

### 3.3 Suggested HPO terms (non-exhaustive)
Based on reported phenotypes and triggers in the retrieved sources:
- Syncope — **HP:0001279** (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, jurisic2023catecholaminergicpolymorphicventricular pages 1-2)
- Sudden cardiac arrest — **HP:0001695** (lee2024treatmentoutcomesin pages 7-9)
- Ventricular tachycardia (polymorphic/bidirectional) — **HP:0004756** (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, peltenburg2024prognosisandclinical pages 1-2)
- Premature ventricular contractions — **HP:0001669** (peltenburg2024prognosisandclinical pages 1-2)
- Atrial fibrillation/flutter — **HP:0005110 / HP:0004799** (supported as atrial tachyarrhythmias occur in CPVT case series) (jurisic2023catecholaminergicpolymorphicventricular pages 1-2)
- Sinus bradycardia / sinus node dysfunction — **HP:0001688 / HP:0001642** (yan2023clinicalandgenetic pages 2-4, wang2024clinicalcharacteristicsand pages 7-8)

### 3.4 Quality of life impact
Quality-of-life impact is primarily mediated by exercise restriction, syncope risk, and ICD shock burden/psychological distress; LCSD is noted in review-level evidence as potentially improving quality of life by reducing events/shocks. (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15)

---

## 4. Genetic / molecular information

### 4.1 Causal gene(s)
**RYR2** is the predominant causal gene for CPVT1, accounting for roughly **~60–70%** of cases in review summaries; cohort data in Chinese children showed **70.1%** of genetically positive tests were RYR2. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, aggarwal2024catecholaminergicpolymorphicventricular pages 2-4, yan2023clinicalandgenetic pages 1-2)

### 4.2 Variant characteristics
- **Variant type:** predominantly **missense** (~96% per one review), described as **gain-of-function**. (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4)
- **Penetrance:** review summaries estimate ~75–80% for RYR2-mediated disease. (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4)
- **Variant distribution:** RYR2 pathogenic variants often cluster in three regions (N-terminal, central, C-terminal), though rare variants occur in healthy individuals, complicating interpretation. (peltenburg2024prognosisandclinical pages 1-2)

**Variant classification:** Some cohorts explicitly reference ACMG/AMP variant classification (pathogenic/likely pathogenic/VUS), indicating clinical use of standardized classification frameworks in CPVT workups. (lee2024treatmentoutcomesin pages 7-9)

### 4.3 Modifier genes / multiple variants
A review notes that multiple variants are an independent predictor of adverse events in CPVT risk modeling. (aggarwal2024catecholaminergicpolymorphicventricular pages 8-9)

### 4.4 Epigenetics / chromosomal abnormalities
No RYR2-CPVT–specific epigenetic or chromosomal abnormality evidence was identified in the retrieved sources.

---

## 5. Environmental information

### 5.1 Environmental and lifestyle factors
**Adrenergic stimuli (exercise, emotional stress)** are the key real-world triggers. Lifestyle recommendations and exercise modification are embedded in treatment algorithms and management considerations. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, aggarwal2024catecholaminergicpolymorphicventricular media 56a4a30c)

### 5.2 Infectious agents
No infectious etiology is implicated for CPVT in the retrieved sources.

---

## 6. Mechanism / pathophysiology (causal chain, upstream vs downstream)

### 6.1 Canonical causal chain (current consensus)
**Upstream trigger:** catecholaminergic stimulation (exercise/emotion) increases adrenergic drive. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, peltenburg2024prognosisandclinical pages 1-2)

**Molecular defect:** RYR2 pathogenic variants predispose RyR2 to abnormal gating and **diastolic SR Ca2+ leak**. (peltenburg2024prognosisandclinical pages 1-2, keefe2023roleofca^2+ pages 8-9)

**Downstream electrophysiology:** increased cytosolic Ca2+ activates the **sodium–calcium exchanger (NCX)**, generating net inward current that produces **delayed afterdepolarizations (DADs)** and triggered action potentials → ventricular ectopy → polymorphic/bidirectional VT → VF/sudden death. (peltenburg2024prognosisandclinical pages 1-2, keefe2023roleofca^2+ pages 8-9)

### 6.2 Upstream modulators and structural biology (2023–2024 developments)
**RyR2 regulatory complex and phosphorylation:** A 2023 review summarizes RyR2 regulation by PKA and CaMKII (e.g., CaMKII phosphorylation at S2814; PKA at S2808/2830) and links phosphorylation and disrupted regulatory binding (e.g., FKBP12.6/calstabin2) to increased RyR2 open probability and diastolic Ca2+ sparks/leak. (keefe2023roleofca^2+ pages 29-34, keefe2023roleofca^2+ pages 3-4)

**Structural “primed” state and Rycal stabilization (2024):** A 2024 Nature Communications structural study reports that CPVT-linked RyR2 variants and remodeled RyR2 in heart failure share a pathologic **“primed” intermediate conformation** associated with diastolic Ca2+ leak; “Rycal” drugs are described as reverting the primed state toward closed and reducing leak. The paper describes RyR2 channels as hyperphosphorylated/oxidized and depleted of calstabin-2 in heart failure, and frames a unified structural-physiological mechanism of leak across arrhythmogenic disorders. (miotto2024structuralbasisfor pages 1-2)

### 6.3 Suggested GO biological process / cellular component terms (examples)
- Regulation of cardiac muscle contraction by calcium ion signaling — **GO:0010881** (mechanistically central to RyR2 dysfunction and EC coupling) (keefe2023roleofca^2+ pages 29-34)
- Ryanodine-sensitive calcium-release channel activity — **GO:0005219** (RyR2 function) (peltenburg2024prognosisandclinical pages 1-2)
- Calcium ion transport into cytosol — **GO:0060402** (SR Ca2+ release) (peltenburg2024prognosisandclinical pages 1-2)
- Sarcoplasmic reticulum membrane — **GO:0033017** (RyR2 localization) (peltenburg2024prognosisandclinical pages 1-2)

### 6.4 Suggested Cell Ontology (CL) terms (examples)
Primary affected cell type is the **cardiac muscle cell / cardiomyocyte** (e.g., **CL:0000746**), as the pathophysiology centers on SR Ca2+ handling in cardiomyocytes. (peltenburg2024prognosisandclinical pages 1-2, miotto2024structuralbasisfor pages 1-2)

---

## 7. Anatomical structures affected

### 7.1 Organ and system level
Primary system: **cardiovascular**; primary organ: **heart** with electrophysiologic dysfunction rather than structural cardiomyopathy in typical CPVT presentation. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2)

### 7.2 Tissue/cell level
Primary tissue: **cardiac muscle**; primary cell type: **cardiomyocytes** with abnormal SR Ca2+ handling. (peltenburg2024prognosisandclinical pages 1-2)

### 7.3 Subcellular level
Key compartment: **sarcoplasmic reticulum** (SR) Ca2+ stores and the SR membrane-localized RyR2 channel complex. (peltenburg2024prognosisandclinical pages 1-2, keefe2023roleofca^2+ pages 29-34)

---

## 8. Temporal development

### 8.1 Onset
Most commonly in childhood/adolescence; mean onset 7–12 years in a 2024 review summary, with a majority presenting by age 20. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2)

### 8.2 Progression/course
Course is typically episodic and trigger-dependent. However, multiple studies highlight that delayed/missed diagnosis is common and can contribute to poor outcomes. In China, pediatric CPVT showed a mean diagnostic delay of **4.3±6.6 years** in a 95-patient compilation. (yan2023clinicalandgenetic pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology
- **Prevalence:** estimated at **~1 in 10,000** (review-level). (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2)
- **Contribution to sudden death:** may account for **up to ~15%** of unexplained SCD in young people (review-level). (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2)
- **Autopsy-negative SUD:** one review states ~12% of autopsy-negative sudden unexplained deaths in young individuals have been linked to CPVT. (aggarwal2024catecholaminergicpolymorphicventricular pages 8-9)

### 9.2 Inheritance
- RYR2-mediated CPVT is typically **autosomal dominant**. (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4)

### 9.3 Penetrance/expressivity
- Penetrance estimates in reviews range roughly **~63–78%** overall and **~75–80%** for RYR2-mediated CPVT, consistent with variable expressivity and incomplete penetrance. (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4)

---

## 10. Diagnostics

### 10.1 Clinical criteria and key tests
- **Exercise stress testing** is the principal diagnostic modality to unmask adrenergically mediated polymorphic/bidirectional ventricular ectopy in the setting of a structurally normal heart and typically normal baseline ECG. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2, aggarwal2024catecholaminergicpolymorphicventricular pages 6-8)
- **Epinephrine infusion test** is an alternative when exercise testing is not feasible; one review provides a protocol (starting 0.05–0.1 mcg/kg/min titrated to 0.20 mcg/kg/min) and notes low sensitivity (**28%**) but high specificity (**98%**) relative to exercise testing, using arrhythmia induction criteria including polymorphic VT and high PVC burden. (aggarwal2024catecholaminergicpolymorphicventricular pages 6-8)

### 10.2 Genetic testing approach
- Genetic testing for CPVT-susceptibility genes (including **RYR2**) is recommended for probands with a clinical CPVT diagnosis, alongside cascade screening of first-degree relatives. (aggarwal2024catecholaminergicpolymorphicventricular pages 6-8)
- Because rare RYR2 variants occur in healthy individuals, recent expert discussion emphasizes careful variant adjudication and multidisciplinary review; de novo status increases pathogenic likelihood. (peltenburg2024prognosisandclinical pages 1-2)

### 10.3 Differential diagnosis (limited by retrieved evidence)
The retrieved texts emphasize that CPVT can be misdiagnosed as neurologic events (e.g., seizures) due to syncope and that careful arrhythmia provocation testing is needed. Detailed differential diagnosis lists were not extracted from the current evidence set. (jurisic2023catecholaminergicpolymorphicventricular pages 1-2)

---

## 11. Outcome / prognosis

### 11.1 Natural history severity and pre-diagnosis burden
A 2024 review summarizes substantial pre-diagnosis burden: ~30% experiencing at least one cardiac arrest and up to 80% having syncope prior to diagnosis; mortality is reported as high (30–50% by age 35 in review-level summaries). (aggarwal2024catecholaminergicpolymorphicventricular pages 8-9)

### 11.2 Recent cohort outcome statistics (2023–2024)
In the 2024 Korean pediatric cohort (n=23):
- **5-year cardiac event-free survival:** 31.2% 
- **10-year overall survival:** 73.1%
- Marked improvement in those diagnosed since 2009 (no deaths in that subgroup), consistent with evolving implementation of combination therapy and procedural adjuncts. (lee2024treatmentoutcomesin pages 1-2, lee2024treatmentoutcomesin pages 7-9)

---

## 12. Treatment

### Current real-world algorithm (review-derived)
A recent treatment algorithm emphasizes lifestyle modification, first-line non-selective beta-blockade, escalation to flecainide and/or LCSD for persistent arrhythmias, and reserving ICD for the highest-risk patients or refractory cases; the same figure stratifies approaches for symptomatic vs asymptomatic individuals. (aggarwal2024catecholaminergicpolymorphicventricular media 56a4a30c)

| Therapy (drug/procedure) | Mechanism/rationale | Indications/real-world use | Quantitative outcome data reported in 2024 Aggarwal review and 2024 Lee cohort | Key safety/limitations |
|---|---|---|---|---|
| Non-selective beta-blockers (preferred: nadolol; propranolol where nadolol unavailable) | Reduce adrenergic stimulation that precipitates RyR2-mediated diastolic SR Ca2+ leak and triggered ventricular arrhythmias | First-line, lifelong therapy for essentially all clinically affected RYR2-CPVT patients; non-selective agents preferred over beta1-selective drugs; background therapy before considering add-on flecainide, LCSD, or ICD (aggarwal2024catecholaminergicpolymorphicventricular pages 11-12, aggarwal2024catecholaminergicpolymorphicventricular pages 1-2) | Aggarwal review: higher arrhythmic risk with beta1-selective blockers versus nadolol, HR 2.04 in symptomatic children (p=0.002) and HR 5.8 in 216 RYR2-variant patients (p=0.001); up to 30% of patients on optimal beta-blocker therapy require additional treatment; nonadherence reported in ~15% and implicated in 60% of evening events (aggarwal2024catecholaminergicpolymorphicventricular pages 11-12). Lee cohort: all 23 patients received beta-blockers, yet 73.9% developed cardiac events, 43.5% had aborted cardiac arrest, and 21.7% died during follow-up, showing monotherapy is often insufficient in high-risk pediatric disease (lee2024treatmentoutcomesin pages 6-7, lee2024treatmentoutcomesin pages 7-9) | Breakthrough events occur despite treatment; adherence problems are clinically important; side effects may preclude use in ~10%; selective beta-blockers were commonly used in one real-world pediatric cohort despite evidence favoring non-selective agents (aggarwal2024catecholaminergicpolymorphicventricular pages 11-12, lee2024treatmentoutcomesin pages 6-7) |
| Flecainide add-on to beta-blocker | Direct antiarrhythmic effect with RyR2-related reduction of ventricular ectopy/triggered activity; used to suppress exercise-induced ventricular arrhythmias beyond sympathetic blockade | Add-on therapy when arrhythmias persist on beta-blockers or in higher-risk patients; commonly combined with beta-blockers in pediatric practice and expert treatment pathways (aggarwal2024catecholaminergicpolymorphicventricular pages 11-12, lee2024treatmentoutcomesin pages 6-7) | Aggarwal review: randomized crossover study (n=14) found flecainide + beta-blocker superior to beta-blocker alone for exercise-induced arrhythmias, with no couplets/NSVT in the flecainide arm; multinational retrospective cohort (n=247) showed significant reduction in major arrhythmic events with adjunctive flecainide (aggarwal2024catecholaminergicpolymorphicventricular pages 11-12, aggarwal2024catecholaminergicpolymorphicventricular pages 12-14). Lee cohort: combination beta-blocker + flecainide markedly lowered cardiac-event risk versus beta-blocker alone, HR 0.08 (95% CI 0.02-0.38; p=0.002); however, small subgroup analyses showed no significant reduction in treadmill arrhythmia score (p=0.317) or Holter PVC burden (p=0.144) (lee2024treatmentoutcomesin pages 7-9, lee2024treatmentoutcomesin pages 6-7) | Evidence for monotherapy is limited and combination therapy is generally preferred; some monitoring endpoints may not improve despite event reduction; availability varies by region (aggarwal2024catecholaminergicpolymorphicventricular pages 12-14, lee2024treatmentoutcomesin pages 9-10) |
| Left cardiac sympathetic denervation (LCSD) | Surgical/procedural reduction of cardiac sympathetic input to decrease catecholamine-triggered arrhythmogenesis | Adjunct for patients with persistent events or intolerance despite beta-blocker ± flecainide; may be used before or alongside ICD, including in recurrent shock scenarios; used substantially in pediatric tertiary centers (aggarwal2024catecholaminergicpolymorphicventricular pages 12-14, aggarwal2024catecholaminergicpolymorphicventricular pages 14-15, lee2024treatmentoutcomesin pages 6-7) | Aggarwal review: in multicenter data, major cardiac events fell from 86% to 21% over median 37 months; mean annual event rate dropped 92%, from 3.4 (95% CI 3.2-3.7) to 0.5 (95% CI 0.4-0.6); among those symptomatic despite optimal medical therapy, about one-third had recurrent events (aggarwal2024catecholaminergicpolymorphicventricular pages 12-14, aggarwal2024catecholaminergicpolymorphicventricular pages 14-15). Lee cohort: LCSD performed in 15/23; Holter PVC burden fell from 0.7994% to 0.0103% (p=0.018); trend toward fewer cardiac events, univariable HR 0.26 (p≈0.055), multivariable HR 0.38 (p=0.174) (lee2024treatmentoutcomesin pages 6-7, lee2024treatmentoutcomesin pages 7-9) | Not curative; recurrence still occurs in ~1/3; procedural complications include ptosis, Horner syndrome, pneumothorax, and neuropathic pain, though often infrequent/transient (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15) |
| Implantable cardioverter-defibrillator (ICD) | Rescue therapy for malignant ventricular arrhythmias/sudden cardiac arrest, but shocks can themselves provoke catecholamine release and further arrhythmia | Reserved for highest-risk patients, especially after aborted cardiac arrest; increasingly considered a last resort after optimized beta-blocker + flecainide + LCSD; in Lee cohort used rarely for refractory syncope/ACA despite other therapy (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15, aggarwal2024catecholaminergicpolymorphicventricular pages 15-16, lee2024treatmentoutcomesin pages 6-7) | Aggarwal review: one review found 85% experienced device complications; inappropriate shocks in 20-30%; shocks failed for VT in 99% but succeeded for VF in 94%; meta-analysis showed 40% appropriate shocks, 21% inappropriate shocks, 20% electrical storms; registry data showed composite events 47% with ICD versus 15.8% without ICD (likely confounded) (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15). Additional review data reported other device-related complications in 29% (aggarwal2024catecholaminergicpolymorphicventricular pages 15-16). Lee cohort: 2/23 received ICDs; one had 2 appropriate shocks, another 1 appropriate shock, but one experienced electrical storm from inappropriate shocks and VT acceleration after shock (lee2024treatmentoutcomesin pages 6-7) | High morbidity, inappropriate shocks, electrical storms, and possible proarrhythmia; may not improve survival in observational comparisons; careful programming is required, and guideline-exempt management without ICD is increasingly accepted in selected CPVT patients (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15, aggarwal2024catecholaminergicpolymorphicventricular pages 15-16) |
| Triple therapy (nadolol + flecainide + LCSD) | Mechanistically complementary suppression of adrenergic drive, triggered activity, and sympathetic outflow | Expert-endorsed escalation strategy after sentinel sudden cardiac arrest or persistent high risk before/defaulting to ICD-only management (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15) | Aggarwal review: expert opinion specifically supports "triple therapy" after a sentinel sudden cardiac arrest, reflecting contemporary shift toward aggressive combined non-device therapy before ICD dependence; no single pooled HR reported for the full triple regimen in the excerpts (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15) | Evidence base is largely observational/expert-opinion; some patients still require ICD or experience recurrent events despite multimodal therapy (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15, lee2024treatmentoutcomesin pages 7-9) |
| Catheter ablation of triggering PVCs (adjunctive, selected cases) | Eliminates identifiable PVC triggers for polymorphic VT/VF but does not remove the underlying arrhythmogenic RyR2 substrate | Considered in selected refractory patients, especially if flecainide cannot be used or if discrete triggering PVCs are mappable; adjunct rather than core therapy (aggarwal2024catecholaminergicpolymorphicventricular pages 16-18, aggarwal2024catecholaminergicpolymorphicventricular pages 15-16) | Aggarwal review: trigger elimination achieved non-inducibility in >90% of patients and nearly 60% remained free from syncope during follow-up; however, recurrence remained substantial, with 80% recurrence in one 5-patient series and mean time to recurrence ~4 years (aggarwal2024catecholaminergicpolymorphicventricular pages 16-18, aggarwal2024catecholaminergicpolymorphicventricular pages 15-16) | Does not treat the underlying disease substrate; recurrence can be high; usually requires continued consideration of LCSD/ICD in high-risk patients (aggarwal2024catecholaminergicpolymorphicventricular pages 16-18, aggarwal2024catecholaminergicpolymorphicventricular pages 15-16) |


*Table: This table summarizes the main evidence-based management strategies for RYR2-mediated CPVT, integrating current review-level evidence with recent real-world pediatric cohort data. It is useful for comparing mechanism, clinical use, quantitative outcomes, and limitations across medications and procedures.*

### 12.1 Evidence-based therapies (key quantitative findings)
**Beta-blockers:** non-selective agents (especially nadolol) are preferred; review-level hazard ratios suggest higher arrhythmic risk with beta1-selective blockers compared with nadolol (HR 2.04 in symptomatic children; HR 5.8 in a 216-patient RYR2 cohort). (aggarwal2024catecholaminergicpolymorphicventricular pages 11-12)

**Flecainide add-on:** in the 2024 Korean pediatric cohort, beta-blocker + flecainide was associated with a large reduction in cardiac events vs beta-blocker alone (HR 0.08; 95% CI 0.02–0.38; p=0.002). (lee2024treatmentoutcomesin pages 7-9)

**LCSD:** multicenter observational evidence summarized in a 2024 review suggests a 92% reduction in mean annual event rate (3.4 to 0.5) and major cardiac events reduction (86% to 21% over ~37 months), with ~1/3 recurrence even on optimal medical therapy. (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15, aggarwal2024catecholaminergicpolymorphicventricular pages 12-14)

**ICD:** evidence summarized in a 2024 review highlights high complication and shock burdens (e.g., 20–30% inappropriate shocks; high device complication rates; electrical storms), and concern that shocks may fail for VT and can worsen arrhythmia in CPVT; ICD is increasingly framed as last-resort after optimal medical and LCSD therapy. (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15, aggarwal2024catecholaminergicpolymorphicventricular pages 15-16)

### 12.2 MAXO term suggestions (examples)
(Provided as ontology normalization suggestions; not validated from a MAXO database in the retrieved sources.)
- Beta-adrenergic antagonist therapy — **MAXO: beta blocker therapy** (aggarwal2024catecholaminergicpolymorphicventricular pages 11-12)
- Flecainide therapy — **MAXO: antiarrhythmic drug therapy** (aggarwal2024catecholaminergicpolymorphicventricular pages 11-12)
- Left cardiac sympathetic denervation — **MAXO: cardiac sympathetic denervation** (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15)
- Implantable cardioverter-defibrillator placement — **MAXO: implantable cardioverter defibrillator implantation** (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15)

### 12.3 Recent/experimental treatments and latest research (2023–2024)
**RyR2 stabilizers (“Rycals”) and structural mechanism:** 2024 structural work supports the concept of pharmacologic stabilization of RyR2 away from a leak-prone primed state, providing mechanistic grounding for RyR2-stabilizing small-molecule approaches. (miotto2024structuralbasisfor pages 1-2)

**Genome editing (preclinical, 2024):** AAV9-delivered, mutation-specific CRISPR/SaCas9 disruption of the mutant Ryr2 allele in R176Q/+ mice produced durable suppression of inducible ventricular arrhythmias at 6 weeks and out to 12 months, with favorable cardiac safety on serial echocardiography and histology; it also reduced Ca2+ spark frequency (e.g., from 8.0±1.6 toward 2.2±0.5 sparks/100 mm/s). (moore2024longtermefficacyand pages 6-9, moore2024longtermefficacyand pages 1-3)

---

## 13. Prevention

**Secondary prevention:** cascade family screening is highlighted as increasing detection of asymptomatic RYR2 variant carriers; guidance suggests these individuals often develop phenotype in the first two decades and may have low arrhythmic risk, but evidence-based monitoring/therapy timing remains limited. (peltenburg2024prognosisandclinical pages 1-2)

**Tertiary prevention:** optimal beta-blocker adherence, escalation to flecainide and LCSD, and cautious ICD deployment aim to prevent recurrent malignant arrhythmias and device-related harm. (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15, aggarwal2024catecholaminergicpolymorphicventricular pages 11-12)

---

## 14. Other species / natural disease
No naturally occurring veterinary CPVT information was retrieved in the current evidence set.

---

## 15. Model organisms / disease models

### 15.1 Mammalian genetic models
**Ryr2 R176Q/+ mouse model** is used for CPVT mechanistic and therapeutic studies; allele-specific AAV9-CRISPR editing in this model demonstrated durable antiarrhythmic efficacy and safety signals through 12 months. (moore2024longtermefficacyand pages 1-3, moore2024longtermefficacyand pages 6-9)

### 15.2 Human cellular models (in vitro)
Human iPSC-cardiomyocyte models engineered to carry CPVT-linked RYR2 variants demonstrate arrhythmogenic Ca2+ handling phenotypes; for example, CRISPR-introduced RyR2-S4938F in hiPSC-CMs is associated with altered Ca2+ signaling and increased spontaneous Ca2+ sparks/transients consistent with an arrhythmogenic phenotype. (toth2023calciumsignalingconsequences pages 1-2)

---

## Recent developments and active clinical trials (ClinicalTrials.gov)

1) **SGT-501 gene therapy in CPVT (NCT07148089)**
- Sponsor: Solid Biosciences; **Phase 1b**, open-label dose-finding; **Recruiting**; estimated enrollment 18.
- Key inclusion: central-lab confirmed **pathogenic/likely pathogenic RYR2 variant** and prior life-threatening ventricular arrhythmic event; stable beta-blocker and/or flecainide regimen.
- Primary endpoint: treatment-emergent adverse events through Day 360; secondary endpoint includes change in **ventricular arrhythmia score (VAS)** on exercise stress test at Day 180. Long-term follow-up planned for 5 years. (posted/record date in excerpt: 2026-04-03). URL: https://clinicaltrials.gov/study/NCT07148089 (NCT07148089 chunk 1, NCT07148089 chunk 2)

2) **S48168 (ARM210) RyR2 modulator trial in CPVT1 (NCT05122975)**
- Sponsor: RyCarma Therapeutics; **Phase 2**, randomized crossover, quadruple-masked; enrollment 8; **Terminated** due to recruitment challenges.
- Intervention: oral S48168 (ARM210) vs placebo on top of standard of care, 28-day periods.
- Primary endpoint: change in exercise ectopy score from baseline to Day 28 vs placebo; additional endpoints include safety, PK, and wearable monitoring. Start date 2023-08-01; primary completion 2024-04-01. URL: https://clinicaltrials.gov/study/NCT05122975 (NCT05122975 chunk 1)

---

## Direct quotes from abstracts (supporting key statements)

- Diagnostic hallmark and phenotype: “Diagnosing CPVT typically involves unmasking the arrhythmia through exercise stress testing… in the absence of structural heart disease… and with a normal baseline electrocardiogram.” (Aggarwal et al., 2024-03; URL https://doi.org/10.3390/jcm13061781) (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2)

- Asymptomatic carrier management gap: asymptomatic family members with a pathogenic RYR2 variant have arrhythmic risk described as “presumably low” and phenotype “seems to develop in the first two decades of life,” with limited guidance. (Peltenburg et al., 2024-04; URL https://doi.org/10.1017/s1047951124000714) (peltenburg2024prognosisandclinical pages 1-2)

- Structural mechanism: RyR2 variants “linked either to heart failure or inherited sudden cardiac death… are in the primed state… Binding of Rycal drugs… reverts the primed state back towards the closed state, decreasing Ca2+ leak… preventing arrhythmias.” (Miotto et al., 2024-09; URL https://doi.org/10.1038/s41467-024-51791-y) (miotto2024structuralbasisfor pages 1-2)

---

## Key limitations / evidence gaps
- Formal database identifiers (OMIM/Orphanet/MeSH/ICD/MONDO) were not retrievable within the current evidence set; a dedicated database lookup would be required to populate those fields with citations.
- Several important quantitative claims in review articles summarize prior cohorts/meta-analyses; the underlying primary sources (often pre-2023) were not all retrieved as full text in this run, limiting direct PMID-level citation.
- Differential diagnosis lists, QoL instrument data (EQ-5D/SF-36/PROMIS), and protective genetic/environmental factors were not found in the retrieved evidence.

---

## URLs and publication dates (selected high-priority sources used)
- Aggarwal et al. “Catecholaminergic Polymorphic Ventricular Tachycardia: Clinical Characteristics, Diagnostic Evaluation and Therapeutic Strategies.” *J Clin Med* (2024-03). https://doi.org/10.3390/jcm13061781 (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2)
- Peltenburg et al. “Prognosis and clinical management of asymptomatic family members with RYR2-mediated CPVT.” *Cardiol Young* (2024-04). https://doi.org/10.1017/S1047951124000714 (peltenburg2024prognosisandclinical pages 1-2)
- Lee et al. “Treatment outcomes in children with CPVT: a single institutional experience.” *Korean Circ J* (2024-12). https://doi.org/10.4070/kcj.2024.0183 (lee2024treatmentoutcomesin pages 1-2)
- Yan et al. “Clinical and genetic profiles of Chinese pediatric CPVT patients.” *Orphanet J Rare Dis* (2023-12). https://doi.org/10.1186/s13023-023-02991-0 (yan2023clinicalandgenetic pages 1-2)
- Miotto et al. “Structural basis for RyR2 leak…” *Nat Commun* (2024-09). https://doi.org/10.1038/s41467-024-51791-y (miotto2024structuralbasisfor pages 1-2)
- Moore et al. “Long-term efficacy and safety of cardiac genome editing for CPVT.” *J Cardiovasc Aging* (2024-01). https://doi.org/10.20517/jca.2023.42 (moore2024longtermefficacyand pages 1-3)
- ClinicalTrials.gov NCT07148089 (SGT-501 gene therapy) record excerpt date 2026-04-03. https://clinicaltrials.gov/study/NCT07148089 (NCT07148089 chunk 1)
- ClinicalTrials.gov NCT05122975 (S48168/ARM210) start 2023-08-01; primary completion 2024-04-01. https://clinicaltrials.gov/study/NCT05122975 (NCT05122975 chunk 1)

References

1. (aggarwal2024catecholaminergicpolymorphicventricular pages 1-2): Abhinav Aggarwal, Anton Stolear, Md Mashiul Alam, Swarnima Vardhan, Maxim Dulgher, Sun-Joo Jang, and Stuart W. Zarich. Catecholaminergic polymorphic ventricular tachycardia: clinical characteristics, diagnostic evaluation and therapeutic strategies. Journal of Clinical Medicine, 13:1781, Mar 2024. URL: https://doi.org/10.3390/jcm13061781, doi:10.3390/jcm13061781. This article has 27 citations.

2. (peltenburg2024prognosisandclinical pages 1-2): Puck J. Peltenburg, Harry Gibson, Arthur A. M. Wilde, Christian van der Werf, Sally-Ann B. Clur, and Nico A. Blom. Prognosis and clinical management of asymptomatic family members with ryr2-mediated catecholaminergic polymorphic ventricular tachycardia: a review. Cardiology in the young, 34:1-8, Apr 2024. URL: https://doi.org/10.1017/s1047951124000714, doi:10.1017/s1047951124000714. This article has 1 citations and is from a peer-reviewed journal.

3. (lee2024treatmentoutcomesin pages 1-2): Joowon Lee, Bo Sang Kwon, Mi Kyoung Song, Sang-Yun Lee, Jung Min Ko, Gi Beom Kim, and Eun Jung Bae. Treatment outcomes in children with catecholaminergic polymorphic ventricular tachycardia: a single institutional experience. Korean Circulation Journal, 54:853-864, Dec 2024. URL: https://doi.org/10.4070/kcj.2024.0183, doi:10.4070/kcj.2024.0183. This article has 1 citations and is from a peer-reviewed journal.

4. (jurisic2023catecholaminergicpolymorphicventricular pages 1-2): Stjepan Jurisic, Argelia Medeiros-Domingo, Florian Berger, Christian Balmer, Corinna Brunckhorst, Frank Ruschitzka, Ardan M. Saguner, and Firat Duru. Catecholaminergic polymorphic ventricular tachycardia: multiple clinical presentations of a genetically determined disease. Journal of Clinical Medicine, 13:47, Dec 2023. URL: https://doi.org/10.3390/jcm13010047, doi:10.3390/jcm13010047. This article has 5 citations.

5. (aggarwal2024catecholaminergicpolymorphicventricular pages 2-4): Abhinav Aggarwal, Anton Stolear, Md Mashiul Alam, Swarnima Vardhan, Maxim Dulgher, Sun-Joo Jang, and Stuart W. Zarich. Catecholaminergic polymorphic ventricular tachycardia: clinical characteristics, diagnostic evaluation and therapeutic strategies. Journal of Clinical Medicine, 13:1781, Mar 2024. URL: https://doi.org/10.3390/jcm13061781, doi:10.3390/jcm13061781. This article has 27 citations.

6. (aggarwal2024catecholaminergicpolymorphicventricular pages 6-8): Abhinav Aggarwal, Anton Stolear, Md Mashiul Alam, Swarnima Vardhan, Maxim Dulgher, Sun-Joo Jang, and Stuart W. Zarich. Catecholaminergic polymorphic ventricular tachycardia: clinical characteristics, diagnostic evaluation and therapeutic strategies. Journal of Clinical Medicine, 13:1781, Mar 2024. URL: https://doi.org/10.3390/jcm13061781, doi:10.3390/jcm13061781. This article has 27 citations.

7. (aggarwal2024catecholaminergicpolymorphicventricular pages 8-9): Abhinav Aggarwal, Anton Stolear, Md Mashiul Alam, Swarnima Vardhan, Maxim Dulgher, Sun-Joo Jang, and Stuart W. Zarich. Catecholaminergic polymorphic ventricular tachycardia: clinical characteristics, diagnostic evaluation and therapeutic strategies. Journal of Clinical Medicine, 13:1781, Mar 2024. URL: https://doi.org/10.3390/jcm13061781, doi:10.3390/jcm13061781. This article has 27 citations.

8. (wang2024clinicalcharacteristicsand pages 7-8): Yefeng Wang, Yufan Yang, Ningan Xu, Yunbin Xiao, Chao Zuo, and Zhi Chen. Clinical characteristics and follow-up of complex arrhythmias associated with ryr2 gene mutations in children. Frontiers in Genetics, May 2024. URL: https://doi.org/10.3389/fgene.2024.1405437, doi:10.3389/fgene.2024.1405437. This article has 1 citations and is from a peer-reviewed journal.

9. (lee2024treatmentoutcomesin pages 7-9): Joowon Lee, Bo Sang Kwon, Mi Kyoung Song, Sang-Yun Lee, Jung Min Ko, Gi Beom Kim, and Eun Jung Bae. Treatment outcomes in children with catecholaminergic polymorphic ventricular tachycardia: a single institutional experience. Korean Circulation Journal, 54:853-864, Dec 2024. URL: https://doi.org/10.4070/kcj.2024.0183, doi:10.4070/kcj.2024.0183. This article has 1 citations and is from a peer-reviewed journal.

10. (yan2023clinicalandgenetic pages 1-2): Yu Yan, Liting Tang, Xiaoqin Wang, Kaiyu Zhou, Fan Hu, Hongyu Duan, Xiaoliang Liu, Yimin Hua, and Chuan Wang. Clinical and genetic profiles of chinese pediatric patients with catecholaminergic polymorphic ventricular tachycardia. Orphanet Journal of Rare Diseases, Dec 2023. URL: https://doi.org/10.1186/s13023-023-02991-0, doi:10.1186/s13023-023-02991-0. This article has 4 citations and is from a peer-reviewed journal.

11. (yan2023clinicalandgenetic pages 2-4): Yu Yan, Liting Tang, Xiaoqin Wang, Kaiyu Zhou, Fan Hu, Hongyu Duan, Xiaoliang Liu, Yimin Hua, and Chuan Wang. Clinical and genetic profiles of chinese pediatric patients with catecholaminergic polymorphic ventricular tachycardia. Orphanet Journal of Rare Diseases, Dec 2023. URL: https://doi.org/10.1186/s13023-023-02991-0, doi:10.1186/s13023-023-02991-0. This article has 4 citations and is from a peer-reviewed journal.

12. (aggarwal2024catecholaminergicpolymorphicventricular pages 14-15): Abhinav Aggarwal, Anton Stolear, Md Mashiul Alam, Swarnima Vardhan, Maxim Dulgher, Sun-Joo Jang, and Stuart W. Zarich. Catecholaminergic polymorphic ventricular tachycardia: clinical characteristics, diagnostic evaluation and therapeutic strategies. Journal of Clinical Medicine, 13:1781, Mar 2024. URL: https://doi.org/10.3390/jcm13061781, doi:10.3390/jcm13061781. This article has 27 citations.

13. (aggarwal2024catecholaminergicpolymorphicventricular media 56a4a30c): Abhinav Aggarwal, Anton Stolear, Md Mashiul Alam, Swarnima Vardhan, Maxim Dulgher, Sun-Joo Jang, and Stuart W. Zarich. Catecholaminergic polymorphic ventricular tachycardia: clinical characteristics, diagnostic evaluation and therapeutic strategies. Journal of Clinical Medicine, 13:1781, Mar 2024. URL: https://doi.org/10.3390/jcm13061781, doi:10.3390/jcm13061781. This article has 27 citations.

14. (keefe2023roleofca^2+ pages 8-9): Joshua A. Keefe, Oliver M. Moore, Kevin S. Ho, and Xander H. T. Wehrens. Role of ca^2+ in healthy and pathologic cardiac function: from normal excitation–contraction coupling to mutations that cause inherited arrhythmia. Archives of Toxicology, 97:73-92, Oct 2023. URL: https://doi.org/10.1007/s00204-022-03385-0, doi:10.1007/s00204-022-03385-0. This article has 45 citations and is from a highest quality peer-reviewed journal.

15. (keefe2023roleofca^2+ pages 29-34): Joshua A. Keefe, Oliver M. Moore, Kevin S. Ho, and Xander H. T. Wehrens. Role of ca^2+ in healthy and pathologic cardiac function: from normal excitation–contraction coupling to mutations that cause inherited arrhythmia. Archives of Toxicology, 97:73-92, Oct 2023. URL: https://doi.org/10.1007/s00204-022-03385-0, doi:10.1007/s00204-022-03385-0. This article has 45 citations and is from a highest quality peer-reviewed journal.

16. (keefe2023roleofca^2+ pages 3-4): Joshua A. Keefe, Oliver M. Moore, Kevin S. Ho, and Xander H. T. Wehrens. Role of ca^2+ in healthy and pathologic cardiac function: from normal excitation–contraction coupling to mutations that cause inherited arrhythmia. Archives of Toxicology, 97:73-92, Oct 2023. URL: https://doi.org/10.1007/s00204-022-03385-0, doi:10.1007/s00204-022-03385-0. This article has 45 citations and is from a highest quality peer-reviewed journal.

17. (miotto2024structuralbasisfor pages 1-2): Marco C. Miotto, Steven Reiken, Anetta Wronska, Qi Yuan, Haikel Dridi, Yang Liu, Gunnar Weninger, Carl Tchagou, and Andrew R. Marks. Structural basis for ryanodine receptor type 2 leak in heart failure and arrhythmogenic disorders. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51791-y, doi:10.1038/s41467-024-51791-y. This article has 40 citations and is from a highest quality peer-reviewed journal.

18. (aggarwal2024catecholaminergicpolymorphicventricular pages 11-12): Abhinav Aggarwal, Anton Stolear, Md Mashiul Alam, Swarnima Vardhan, Maxim Dulgher, Sun-Joo Jang, and Stuart W. Zarich. Catecholaminergic polymorphic ventricular tachycardia: clinical characteristics, diagnostic evaluation and therapeutic strategies. Journal of Clinical Medicine, 13:1781, Mar 2024. URL: https://doi.org/10.3390/jcm13061781, doi:10.3390/jcm13061781. This article has 27 citations.

19. (lee2024treatmentoutcomesin pages 6-7): Joowon Lee, Bo Sang Kwon, Mi Kyoung Song, Sang-Yun Lee, Jung Min Ko, Gi Beom Kim, and Eun Jung Bae. Treatment outcomes in children with catecholaminergic polymorphic ventricular tachycardia: a single institutional experience. Korean Circulation Journal, 54:853-864, Dec 2024. URL: https://doi.org/10.4070/kcj.2024.0183, doi:10.4070/kcj.2024.0183. This article has 1 citations and is from a peer-reviewed journal.

20. (aggarwal2024catecholaminergicpolymorphicventricular pages 12-14): Abhinav Aggarwal, Anton Stolear, Md Mashiul Alam, Swarnima Vardhan, Maxim Dulgher, Sun-Joo Jang, and Stuart W. Zarich. Catecholaminergic polymorphic ventricular tachycardia: clinical characteristics, diagnostic evaluation and therapeutic strategies. Journal of Clinical Medicine, 13:1781, Mar 2024. URL: https://doi.org/10.3390/jcm13061781, doi:10.3390/jcm13061781. This article has 27 citations.

21. (lee2024treatmentoutcomesin pages 9-10): Joowon Lee, Bo Sang Kwon, Mi Kyoung Song, Sang-Yun Lee, Jung Min Ko, Gi Beom Kim, and Eun Jung Bae. Treatment outcomes in children with catecholaminergic polymorphic ventricular tachycardia: a single institutional experience. Korean Circulation Journal, 54:853-864, Dec 2024. URL: https://doi.org/10.4070/kcj.2024.0183, doi:10.4070/kcj.2024.0183. This article has 1 citations and is from a peer-reviewed journal.

22. (aggarwal2024catecholaminergicpolymorphicventricular pages 15-16): Abhinav Aggarwal, Anton Stolear, Md Mashiul Alam, Swarnima Vardhan, Maxim Dulgher, Sun-Joo Jang, and Stuart W. Zarich. Catecholaminergic polymorphic ventricular tachycardia: clinical characteristics, diagnostic evaluation and therapeutic strategies. Journal of Clinical Medicine, 13:1781, Mar 2024. URL: https://doi.org/10.3390/jcm13061781, doi:10.3390/jcm13061781. This article has 27 citations.

23. (aggarwal2024catecholaminergicpolymorphicventricular pages 16-18): Abhinav Aggarwal, Anton Stolear, Md Mashiul Alam, Swarnima Vardhan, Maxim Dulgher, Sun-Joo Jang, and Stuart W. Zarich. Catecholaminergic polymorphic ventricular tachycardia: clinical characteristics, diagnostic evaluation and therapeutic strategies. Journal of Clinical Medicine, 13:1781, Mar 2024. URL: https://doi.org/10.3390/jcm13061781, doi:10.3390/jcm13061781. This article has 27 citations.

24. (moore2024longtermefficacyand pages 6-9): Oliver M. Moore, Y. Aguilar-Sánchez, S. Lahiri, M. Hulsurkar, J. Navarro-Garcia, Tarah A. Word, Joshua A. Keefe, Dean Barazi, Elda Munivez, Charles T. Moore, Vaidya Parthasarathy, Jaysón M. Davidson, W. Lagor, So Hyun Park, Gang Bao, Christina Y Miyake, X. Wehrens, OM Moore, WR Lagor, Wehrens Xht, SK Lahiri, MM Hulsurkar, J. Navarro-Garcia, Tarah A. Word, JA Keefe, CT Moore, Parthasarathy Barazi D, SH Park, and CY Miyake. Long-term efficacy and safety of cardiac genome editing for catecholaminergic polymorphic ventricular tachycardia. The Journal of Cardiovascular Aging, Jan 2024. URL: https://doi.org/10.20517/jca.2023.42, doi:10.20517/jca.2023.42. This article has 11 citations.

25. (moore2024longtermefficacyand pages 1-3): Oliver M. Moore, Y. Aguilar-Sánchez, S. Lahiri, M. Hulsurkar, J. Navarro-Garcia, Tarah A. Word, Joshua A. Keefe, Dean Barazi, Elda Munivez, Charles T. Moore, Vaidya Parthasarathy, Jaysón M. Davidson, W. Lagor, So Hyun Park, Gang Bao, Christina Y Miyake, X. Wehrens, OM Moore, WR Lagor, Wehrens Xht, SK Lahiri, MM Hulsurkar, J. Navarro-Garcia, Tarah A. Word, JA Keefe, CT Moore, Parthasarathy Barazi D, SH Park, and CY Miyake. Long-term efficacy and safety of cardiac genome editing for catecholaminergic polymorphic ventricular tachycardia. The Journal of Cardiovascular Aging, Jan 2024. URL: https://doi.org/10.20517/jca.2023.42, doi:10.20517/jca.2023.42. This article has 11 citations.

26. (toth2023calciumsignalingconsequences pages 1-2): Noemi Toth, Xiao-Hua Zhang, Alexandra Zamaro, and Martin Morad. Calcium signaling consequences of ryr2-s4938f mutation expressed in human ipsc-derived cardiomyocytes. International Journal of Molecular Sciences, 24:15307, Oct 2023. URL: https://doi.org/10.3390/ijms242015307, doi:10.3390/ijms242015307. This article has 3 citations.

27. (NCT07148089 chunk 1):  A Study of SGT-501 Gene Therapy in Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT). Solid Biosciences Inc.. 2026. ClinicalTrials.gov Identifier: NCT07148089

28. (NCT07148089 chunk 2):  A Study of SGT-501 Gene Therapy in Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT). Solid Biosciences Inc.. 2026. ClinicalTrials.gov Identifier: NCT07148089

29. (NCT05122975 chunk 1):  Treatment of an Inherited Ventricular Arrhythmia. RyCarma Therapeutics, Inc.. 2023. ClinicalTrials.gov Identifier: NCT05122975