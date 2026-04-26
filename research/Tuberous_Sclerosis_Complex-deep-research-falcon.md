---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:40.298667'
end_time: '2026-04-25T22:27:54.938854'
duration_seconds: 734.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tuberous Sclerosis Complex
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Tuberous Sclerosis Complex
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tuberous Sclerosis Complex** covering all of the
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
- **Disease Name:** Tuberous Sclerosis Complex
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tuberous Sclerosis Complex** covering all of the
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


# Tuberous Sclerosis Complex (TSC) — Disease Characteristics Research Report

## Target disease
- **Disease name:** Tuberous Sclerosis Complex (TSC)
- **Category:** Mendelian / autosomal dominant “mTORopathy” (prototypical)
- **MONDO ID:** **MONDO:0001734** (“tuberous sclerosis”; OpenTargets disease node) (man2024thegeneticsof pages 1-2)

## Executive summary (current understanding)
Tuberous sclerosis complex (TSC) is a rare, autosomal dominant, multisystem disorder caused by heterozygous loss-of-function pathogenic variants in the tumor suppressor genes **TSC1** and **TSC2**, encoding **hamartin** and **tuberin** (conte2024therapeuticapproachesto pages 1-2, racioppi2024prenatalmtorinhibitors pages 1-2). Loss of TSC complex function increases **RHEB-GTP** and hyperactivates **mTORC1**, driving abnormal growth and benign tumor (hamartoma) formation across multiple organs (brain, kidneys, skin, heart, lungs) and causing major neurologic morbidity including epilepsy and neurodevelopmental disorders (dufneralmeida2024molecularandfunctional pages 1-2, man2024thegeneticsof pages 1-2, monich2024tuberoussclerosiscomplex pages 1-2).

A quantitative evidence summary is provided in the table below.

| Domain | Metric | Value(s) | Population/Study | Year (publication) | PMID | DOI/URL |
|---|---|---|---|---:|---|---|
| Epidemiology | Incidence at birth/live births | 1:5,800 to 1:13,520 live births | Review of TSC genetics and epidemiology | 2024 |  | https://doi.org/10.3390/genes15030332 (man2024thegeneticsof pages 1-2) |
| Epidemiology | Incidence at birth/live births | 1:6,000 to 1:10,000 live births | Therapeutic review of TSC | 2024 |  | https://doi.org/10.3390/biom14091190 (conte2024therapeuticapproachesto pages 1-2) |
| Epidemiology | Prevalence | ~1 in 6,000 live births | Prenatal mTOR inhibitor review | 2024 |  | https://doi.org/10.3390/jcm13216335 (racioppi2024prenatalmtorinhibitors pages 1-2) |
| Epidemiology | Adjusted prevalence | 10.2 per 100,000 | Shizuoka Kokuho Database; 125 TSC patients; ICD-10 Q85.1 ascertainment | 2025 |  | https://doi.org/10.1186/s13023-025-03799-w (kishida2025epidemiologicalinsightsand pages 1-2, kishida2025epidemiologicalinsightsand pages 2-4) |
| Epidemiology | Crude annual prevalence (2019) | 85 cases among 1,401,399 registrants; ~6.1 per 100,000 | Shizuoka Kokuho Database | 2025 |  | https://doi.org/10.1186/s13023-025-03799-w (kishida2025epidemiologicalinsightsand pages 2-4) |
| Epidemiology | Age-specific prevalence, males | 0–19 y: 18.29/100,000; 20–64 y: 8.53/100,000; 65+ y: 2.37/100,000 | Shizuoka, 2019 | 2025 |  | https://doi.org/10.1186/s13023-025-03799-w (kishida2025epidemiologicalinsightsand pages 2-4) |
| Epidemiology | Age-specific prevalence, females | 0–19 y: 15.38/100,000; 20–64 y: 8.56/100,000; 65+ y: 2.24/100,000 | Shizuoka, 2019 | 2025 |  | https://doi.org/10.1186/s13023-025-03799-w (kishida2025epidemiologicalinsightsand pages 2-4) |
| Epidemiology | Prevalence trend | 5.4/100,000 (2014) to 6.1/100,000 (2015) | Shizuoka prevalence trend after criteria/treatment changes | 2025 |  | https://doi.org/10.1186/s13023-025-03799-w (kishida2025epidemiologicalinsightsand pages 5-6) |
| Genetics | No mutation identified (NMI) by conventional testing | ~15% | Genetics review | 2024 |  | https://doi.org/10.3390/genes15030332 (man2024thegeneticsof pages 1-2) |
| Genetics | Molecular diagnostic yield | 106/116 (91%) definite clinical TSC cases had pathogenic TSC1/TSC2 alteration | Molecular and functional assessment cohort | 2024 |  | https://doi.org/10.3390/genes15111432 (dufneralmeida2024molecularandfunctional pages 1-2) |
| Genetics | Gene distribution in molecularly solved cohort | TSC1: 18/106 (17%); TSC2: 88/106 (83%); 35 novel variants | Molecular and functional assessment cohort | 2024 |  | https://doi.org/10.3390/genes15111432 (dufneralmeida2024molecularandfunctional pages 1-2) |
| Phenotypes | Epilepsy frequency | 62% to 93% | Therapeutic review | 2024 |  | https://doi.org/10.3390/biom14091190 (conte2024therapeuticapproachesto pages 1-2) |
| Phenotypes | Drug-resistant/pharmacoresistant epilepsy | ~two-thirds affected | Prenatal mTOR inhibitor review | 2024 |  | https://doi.org/10.3390/jcm13216335 (racioppi2024prenatalmtorinhibitors pages 1-2) |
| Phenotypes | Intellectual disability | ~50% | Prenatal mTOR inhibitor review | 2024 |  | https://doi.org/10.3390/jcm13216335 (racioppi2024prenatalmtorinhibitors pages 1-2) |
| Phenotypes | Autism spectrum disorder | ~50%; TAND affects ~90% lifetime | Prenatal mTOR inhibitor review | 2024 |  | https://doi.org/10.3390/jcm13216335 (racioppi2024prenatalmtorinhibitors pages 1-2, racioppi2024prenatalmtorinhibitors pages 2-3) |
| Phenotypes | SEGA prevalence | Up to 20% | Therapeutic review | 2024 |  | https://doi.org/10.3390/biom14091190 (conte2024therapeuticapproachesto pages 1-2) |
| Phenotypes | TSC-LAM incidence | About 30% | Therapeutic review | 2024 |  | https://doi.org/10.3390/biom14091190 (conte2024therapeuticapproachesto pages 1-2) |
| Diagnostics | Current clinical diagnostic rule | Definite TSC: 2 major, or 1 major + ≥2 minor, or pathogenic TSC1/TSC2 variant | Clinical criteria table image/summary | 2023 |  | https://doi.org/10.3390/genes14020433 (jurca2023tuberoussclerosistype media b5f360a7) |
| Diagnostics | Median time-to-diagnosis (TTD), TSC-specific vs non-specific manifestations | 1 month (range 1–27) vs 11 months (range 1–84); p=0.0035 | Japan JMDC claims database, Cohort 1 | 2024 |  | https://doi.org/10.1186/s13023-024-03460-y (okanishi2024diagnosticflowanalysis pages 4-5) |
| Diagnostics | Longest TTD by presentation | Renal tumor median 23 months (up to 91 months) | Japan JMDC claims database | 2024 |  | https://doi.org/10.1186/s13023-024-03460-y (okanishi2024diagnosticflowanalysis pages 1-2, okanishi2024diagnosticflowanalysis pages 7-9) |
| Diagnostics | TTD with vs without TSC clinic (all manifestations) | 3.0 months (range 1–49) vs 13.0 months (range 1–91); p=0.0966 | Japan JMDC claims database | 2024 |  | https://doi.org/10.1186/s13023-024-03460-y (okanishi2024diagnosticflowanalysis pages 5-7) |
| Diagnostics | TTD for epilepsy with vs without TSC clinic | 11.5 months (range 1–31) vs 19.0 months (range 1–89); p=0.0379 | Japan JMDC claims database | 2024 |  | https://doi.org/10.1186/s13023-024-03460-y (okanishi2024diagnosticflowanalysis pages 5-7, okanishi2024diagnosticflowanalysis pages 1-2) |
| Diagnostics | Manifestation frequencies in delayed-diagnosis cohort | Epilepsy 29.2%; renal tumor 9.4%; brain/intraventricular tumor 8.5% | Japan JMDC claims database, Cohort 1 | 2024 |  | https://doi.org/10.1186/s13023-024-03460-y (okanishi2024diagnosticflowanalysis pages 4-5, okanishi2024diagnosticflowanalysis pages 5-7) |
| Diagnostics | Early-life manifestations | Cardiac rhabdomyoma 54.8%; epilepsy 38.1% | Japan JMDC claims database, Cohort 2 | 2024 |  | https://doi.org/10.1186/s13023-024-03460-y (okanishi2024diagnosticflowanalysis pages 5-7, okanishi2024diagnosticflowanalysis pages 7-9) |
| Treatment | Everolimus seizure response (real world) | 14/45 (31%) achieved ≥50% seizure reduction; any reduction 68%; ≥30% reduction 44% | Norway/Denmark real-world cohort, 64 treated patients | 2023 |  | https://doi.org/10.1186/s13023-023-02982-1 (cockerell2023effectivenessandsafety pages 1-2, cockerell2023effectivenessandsafety pages 4-6, cockerell2023effectivenessandsafety pages 2-4) |
| Treatment | Everolimus seizure response by age | <18 y: 46% responders; ≥18 y: 14% responders | Real-world cohort | 2023 |  | https://doi.org/10.1186/s13023-023-02982-1 (cockerell2023effectivenessandsafety pages 1-2) |
| Treatment | Everolimus seizure response by country | Norway: 4/26 (15%); Denmark: 10/19 (53%) | Real-world cohort | 2023 |  | https://doi.org/10.1186/s13023-023-02982-1 (cockerell2023effectivenessandsafety pages 4-6) |
| Treatment | Everolimus rAML response (real world) | Largest lesion LD response ≥30% decrease: 35%; mean bilateral diameter response: 38%; stable size 52%/59%; progression 14%/3% | Real-world cohort, 29 patients with rAML imaging | 2023 |  | https://doi.org/10.1186/s13023-023-02982-1 (cockerell2023effectivenessandsafety pages 4-6) |
| Treatment | rAML burden change on everolimus (real world) | Lesions >4 cm decreased from 75% to 55%; lesions >6 cm from 31% to 24% | Real-world cohort | 2023 |  | https://doi.org/10.1186/s13023-023-02982-1 (cockerell2023effectivenessandsafety pages 4-6) |
| Treatment | SEGA response (real world examples) | Volume reductions of 71%, 43%, and 48% after 39, 34, and 82 months | Real-world cohort | 2023 |  | https://doi.org/10.1186/s13023-023-02982-1 (cockerell2023effectivenessandsafety pages 1-2, cockerell2023effectivenessandsafety pages 6-7) |
| Treatment | Everolimus adverse effects (real world) | Any AE 61/64 (95%); stomatitis/oral ulceration 63%; URTI 38%; rash 27%; fatigue 22% | Real-world cohort | 2023 |  | https://doi.org/10.1186/s13023-023-02982-1 (cockerell2023effectivenessandsafety pages 1-2, cockerell2023effectivenessandsafety pages 6-7) |
| Treatment | Everolimus lab abnormalities (real world) | Hypercholesterolemia 41%; anaemia 30%; leucopoenia 25% | Real-world cohort | 2023 |  | https://doi.org/10.1186/s13023-023-02982-1 (cockerell2023effectivenessandsafety pages 1-2, cockerell2023effectivenessandsafety pages 7-9) |
| Treatment | Everolimus severe toxicity/discontinuation (real world) | Grade 3–4 AEs 36%; hospitalization/prolonged hospitalization 34%; discontinuation 9/64 (14%); two life-threatening events | Real-world cohort | 2023 |  | https://doi.org/10.1186/s13023-023-02982-1 (cockerell2023effectivenessandsafety pages 1-2, cockerell2023effectivenessandsafety pages 7-9, cockerell2023effectivenessandsafety pages 10-12) |
| Treatment | EXIST-2 AML response | 42% response (33/79; 95% CI 31–53%) vs 0% placebo; median response time 2–9 months | EXIST-2 everolimus trial, adults with AML | 2024 review summarizing prior trial |  | https://doi.org/10.1590/2175-8239-jbn-2024-0013en (monich2024tuberoussclerosiscomplex pages 5-7) |
| Treatment | EXIST-2 extension AML response | Response increased from 42% to 54%; ~97% showed some AML reduction | EXIST-2 extension | 2024 review summarizing prior trial |  | https://doi.org/10.1590/2175-8239-jbn-2024-0013en (monich2024tuberoussclerosiscomplex pages 5-7) |
| Quality of life & costs | EQ-5D-3L index and VAS | TSC: TTO 0.705; VAS 0.577 vs IGE: 0.897/0.813 vs FE: 0.879/0.769 | Germany matched case-control study, 92 per cohort | 2024 |  | https://doi.org/10.1186/s42466-024-00323-6 (lappe2024amulticentermatched pages 1-2) |
| Quality of life & costs | QOLIE-31 and stigma | QOLIE-31: TSC 57.7 vs IGE 66.6 vs FE 57.6; rESS stigma: TSC 3.97 vs IGE 1.48 vs FE 2.45 | Germany matched case-control study | 2024 |  | https://doi.org/10.1186/s42466-024-00323-6 (lappe2024amulticentermatched pages 1-2) |
| Quality of life & costs | Depression/adverse-event burden | NDDI-E 13.1 vs IGE 11.2; LAEP 42.7 vs IGE 37.5 | Germany matched case-control study | 2024 |  | https://doi.org/10.1186/s42466-024-00323-6 (lappe2024amulticentermatched pages 1-2) |
| Quality of life & costs | Direct costs | Mean total direct costs: TSC €7,602 (median €2,620) vs IGE €1,919 vs FE €2,598 | Germany matched case-control study | 2024 |  | https://doi.org/10.1186/s42466-024-00323-6 (lappe2024amulticentermatched pages 1-2) |
| Quality of life & costs | Indirect productivity costs | Mean over 3 months: TSC €7,185 (median €11,925) vs IGE €3,599 vs FE €5,082 | Germany matched case-control study | 2024 |  | https://doi.org/10.1186/s42466-024-00323-6 (lappe2024amulticentermatched pages 1-2, lappe2024amulticentermatched pages 10-11) |
| Quality of life & costs | Unemployment | 60% in TSC vs 23% in IGE vs 34% in FE | Germany matched case-control study | 2024 |  | https://doi.org/10.1186/s42466-024-00323-6 (lappe2024amulticentermatched pages 1-2, lappe2024amulticentermatched pages 10-11) |


*Table: This table compiles high-yield quantitative findings for tuberous sclerosis complex across epidemiology, genetics, diagnostics, treatment, and burden of illness. It is useful as a compact evidence summary for knowledge-base population and citation tracking.*

---

## 1. Disease information

### 1.1 What is the disease?
- **Definition:** TSC is described as “a rare multisystem disorder caused by heterozygous loss-of-function pathogenic variants in the tumour suppressor genes TSC1 and TSC2” leading to **mTORC1 hyperactivation** and benign tumors in multiple organs, plus frequent epilepsy (conte2024therapeuticapproachesto pages 1-2).
- **Alternative definition (genetics-focused):** TSC is the “prototypical mTORopathy,” where variants in TSC1/TSC2 disrupt the TSC protein complex, a negative regulator of the mechanistic target of rapamycin pathway (man2024thegeneticsof pages 1-2).

### 1.2 Key identifiers (available from retrieved evidence)
- **MONDO:** MONDO:0001734 (man2024thegeneticsof pages 1-2)
- **ICD-10 code used in epidemiology studies:** **Q85.1** (ascertainment code in Shizuoka and JMDC claims studies) (kishida2025epidemiologicalinsightsand pages 1-2, okanishi2024diagnosticflowanalysis pages 2-4)

**Not retrieved in current tool run:** OMIM/Orphanet/MeSH/ICD-11 identifiers and canonical synonym lists from those databases. (The present report therefore cites primary/review literature and claims-based ICD-10 mapping, but cannot provide authoritative OMIM/Orphanet IDs without additional retrieval.)

### 1.3 Synonyms / alternative names
Commonly used naming in the retrieved literature includes:
- “tuberous sclerosis complex” (TSC) (man2024thegeneticsof pages 1-2, conte2024therapeuticapproachesto pages 1-2)
- “tuberous sclerosis” (used in some clinical/claims contexts) (kishida2025epidemiologicalinsightsand pages 1-2)

### 1.4 Evidence sources
This report integrates:
- **Aggregated disease-level resources and cohorts** (claims database epidemiology; multicenter real-world therapeutic outcome study) (cockerell2023effectivenessandsafety pages 1-2, okanishi2024diagnosticflowanalysis pages 4-5, kishida2025epidemiologicalinsightsand pages 1-2)
- **Reviews** synthesizing clinical genetics and management (man2024thegeneticsof pages 1-2, conte2024therapeuticapproachesto pages 1-2, monich2024tuberoussclerosiscomplex pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
- **Primary genetic causes:** Inactivating/pathogenic variants in **TSC1** and **TSC2** (racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 1-2).
- **Inheritance:** Autosomal dominant; review-level synthesis notes approximately one-third inherited and approximately two-thirds de novo and/or mosaic in aggregate (man2024thegeneticsof pages 1-2).

**Abstract quote (Genetics review, 2024):** TSC is “characterized by the development of benign tumors in multiple organs” and “pathogenic variants in TSC1 or TSC2 disrupt the TSC protein complex, a negative regulator of the mTOR pathway.” (man2024thegeneticsof pages 1-2)

### 2.2 Risk factors
- **Genetic risk:** Presence of pathogenic **TSC1/TSC2** variants. Variant location/domain in TSC2 is associated with severity in review synthesis (man2024thegeneticsof pages 1-2).
- **Somatic mosaicism / undetected variants:** ~**15%** of patients have **no mutation identified** by conventional testing, with many presumed due to somatic TSC1/TSC2 variants (man2024thegeneticsof pages 1-2).

### 2.3 Protective factors
No specific protective genetic variants or environmental protective factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
No clear gene–environment interactions were identified in the retrieved evidence set.

---

## 3. Phenotypes (clinical manifestations)

TSC manifests across the CNS, kidney, skin, heart, lungs, and other organs (conte2024therapeuticapproachesto pages 1-2, monich2024tuberoussclerosiscomplex pages 1-2). A subset of phenotype frequency estimates from recent sources is listed below.

### 3.1 Neurologic phenotypes
1. **Epilepsy**
   - **Type:** symptom/clinical syndrome
   - **Frequency:** reported **62–93%** in a 2024 therapeutic review (conte2024therapeuticapproachesto pages 1-2).
   - **Drug-resistance:** “pharmacoresistant epilepsy… affecting approximately two-thirds of patients” (2024 review) (racioppi2024prenatalmtorinhibitors pages 1-2).
   - **HPO suggestions:** HP:0001250 (Seizures); HP:0012469 (Infantile spasms) (conceptually aligned with reported early epilepsy burden) (conte2024therapeuticapproachesto pages 1-2, racioppi2024prenatalmtorinhibitors pages 2-3).

2. **Neurodevelopmental and neuropsychiatric involvement (TAND, autism, intellectual disability)**
   - **Type:** behavioral/psychiatric + developmental
   - **Frequency:** about **half** with intellectual disability and a **similar proportion** with autism spectrum disorder (racioppi2024prenatalmtorinhibitors pages 1-2). TAND is described as affecting **~90%** across the lifetime (racioppi2024prenatalmtorinhibitors pages 2-3).
   - **HPO suggestions:** HP:0000717 (Autism); HP:0001249 (Intellectual disability); HP:0001263 (Global developmental delay).

3. **CNS lesions**
   - **Type:** imaging/pathology findings
   - Includes cortical tubers, subependymal nodules, radial migration lines, and SEGA (racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 1-2).
   - **SEGA prevalence:** “up to 20% among TSC patients” (conte2024therapeuticapproachesto pages 1-2).
   - **HPO suggestions:** HP:0009720 (Cortical tuber); HP:0009718 (Subependymal nodule); HP:0006787 (Subependymal giant cell astrocytoma).

### 3.2 Renal phenotypes
- **Renal angiomyolipomas (AMLs), renal cysts, RCC risk** are emphasized as clinically important; a nephrology review notes kidney involvement includes AML and cystic disease and can lead to bleeding/pain/renal function loss (monich2024tuberoussclerosiscomplex pages 1-2).
- **HPO suggestions:** HP:0006770 (Renal angiomyolipoma); HP:0000107 (Renal cysts).

### 3.3 Pulmonary phenotypes
- **LAM**: “incidence of about 30% in patients with TSC” (review) (conte2024therapeuticapproachesto pages 1-2).
- **HPO suggestions:** HP:0004297 (Lymphangioleiomyomatosis).

### 3.4 Cardiac phenotypes
- **Cardiac rhabdomyoma** is a key prenatal/early-life marker, often prompting prenatal suspicion of TSC (racioppi2024prenatalmtorinhibitors pages 1-2). In a Japanese claims cohort diagnosed <2 years, cardiac rhabdomyoma was present in **54.8%** (okanishi2024diagnosticflowanalysis pages 5-7).
- **HPO suggestions:** HP:0009729 (Cardiac rhabdomyoma).

### 3.5 Skin phenotypes
- Common features include facial angiofibromas, hypomelanotic macules, shagreen patches, and ungual fibromas (diagnostic criteria table) (jurca2023tuberoussclerosistype media b5f360a7).
- **HPO suggestions:** HP:0000957 (Facial angiofibroma); HP:0001010 (Hypopigmented skin lesions); HP:0000976 (Shagreen patch); HP:0009728 (Ungual fibromas).

### Quality-of-life impact (recent quantitative evidence)
Adults with **TSC-related epilepsy** have substantially reduced generic QoL compared with other epilepsy types, with EQ-5D-3L index (TTO) **0.705** and EQ-VAS **0.577** reported in a 2024 German matched case–control study (lappe2024amulticentermatched pages 1-2).

---

## 4. Genetic / molecular information

### 4.1 Causal genes
- **TSC1** and **TSC2** are causal tumor suppressor genes; heterozygous loss-of-function variants lead to TSC (conte2024therapeuticapproachesto pages 1-2, man2024thegeneticsof pages 1-2).

### 4.2 Pathogenic variants and molecular diagnostic yield
- A 2024 cohort study identified pathogenic alterations in **106/116 (91%)** individuals with definite clinical diagnosis, with **TSC2** representing **83%** of solved cases and **TSC1** **17%** (dufneralmeida2024molecularandfunctional pages 1-2).
- **No mutation identified (NMI):** ~**15%** by conventional testing, frequently hypothesized to represent somatic/mosaic TSC1/TSC2 variants (man2024thegeneticsof pages 1-2).

### 4.3 Somatic vs germline; two-hit model
- Mosaicism is emphasized as a cause of negative conventional genetic testing and milder phenotypes in reviews (man2024thegeneticsof pages 1-2, dufneralmeida2024molecularandfunctional pages 1-2).

### 4.4 Mechanistic pathway (current consensus)
A mechanistic chain supported by 2024 evidence:
1. **TSC1/TSC2 loss of function** disrupts the TSC1/2 complex (dufneralmeida2024molecularandfunctional pages 1-2).
2. The complex is a **GAP** for **RHEB**; inactivation increases **RHEB-GTP** (dufneralmeida2024molecularandfunctional pages 1-2).
3. Increased RHEB-GTP activates **mTORC1**, elevating downstream phosphorylation and increasing anabolic metabolism/cell growth (dufneralmeida2024molecularandfunctional pages 1-2).
4. Tissue-level consequences: hamartomas and CNS malformations/lesions, epilepsy, kidney tumors (conte2024therapeuticapproachesto pages 1-2, man2024thegeneticsof pages 1-2, monich2024tuberoussclerosiscomplex pages 1-2).

**Direct quote (mechanism, 2024 study):** “Inactivation of the TSC1/2 results in increased levels of RHEB-GTP, activation of TORC1 kinase activity… thus leading to up-regulation of anabolic metabolism and excessive cell growth.” (dufneralmeida2024molecularandfunctional pages 1-2)

### 4.5 Modifier genes, epigenetics, chromosomal abnormalities
Not established from the retrieved evidence set. (The report therefore cannot reliably list validated modifier loci or epigenetic signatures for TSC without additional retrieval.)

---

## 5. Environmental information
TSC is primarily a monogenic disorder; no specific environmental triggers, lifestyle factors, or infectious causes were identified in the retrieved evidence set (man2024thegeneticsof pages 1-2, conte2024therapeuticapproachesto pages 1-2).

---

## 6. Mechanism / pathophysiology (expanded)

### 6.1 Molecular pathways
- Central pathway: **mTORC1 signaling** dysregulated by TSC1/TSC2 LOF (dufneralmeida2024molecularandfunctional pages 1-2, conte2024therapeuticapproachesto pages 1-2).

**GO term suggestions (biological process):**
- GO:0008283 (cell population proliferation)
- GO:0006412 (translation) / GO:0006091 (generation of precursor metabolites and energy) as downstream readouts of anabolic metabolism (supported conceptually by “up-regulation of anabolic metabolism”) (dufneralmeida2024molecularandfunctional pages 1-2)
- GO:0010506 (regulation of autophagy) as a canonical mTOR-regulated process (not explicitly stated in retrieved excerpts; include as hypothesis-level annotation)

### 6.2 Cellular processes
- Dysregulated growth and differentiation (“cell proliferation, growth, and differentiation” framed in therapeutic review) (conte2024therapeuticapproachesto pages 1-2).

### 6.3 Cell types (CL suggestions)
Based on organs and lesions described:
- CL:0000540 (neuron) and CL:0000127 (astrocyte) for CNS involvement and glial components of tubers/SEGAs (CNS lesion context) (conte2024therapeuticapproachesto pages 1-2).
- CL:0000887 (smooth muscle cell) as a plausible LAM-relevant cell type (LAM mentioned but not mechanistically detailed in retrieved excerpts) (conte2024therapeuticapproachesto pages 1-2).

### 6.4 Causal chain to clinical manifestations (examples)
- **Epilepsy / neurodevelopment:** TSC1/2 LOF → mTORC1 hyperactivation → altered brain development and cortical lesions (tubers) → early-onset seizures; early seizures contribute to neurodevelopmental impairment (review synthesis emphasizes neurologic burden and early window concepts) (racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 1-2).
- **Renal AML:** mTORC1 hyperactivation in renal tissues → AML growth → bleeding risk and kidney function impairment; everolimus reduces AML size and bleeding risk in trial syntheses and real-world data (monich2024tuberoussclerosiscomplex pages 1-2, monich2024tuberoussclerosiscomplex pages 5-7).

---

## 7. Anatomical structures affected

### 7.1 Organ-level involvement (with UBERON suggestions)
- **Brain** (UBERON:0000955): cortical tubers, SEN, SEGA, epilepsy (conte2024therapeuticapproachesto pages 1-2, racioppi2024prenatalmtorinhibitors pages 1-2).
- **Kidney** (UBERON:0002113): renal angiomyolipomas, cysts, RCC risk (monich2024tuberoussclerosiscomplex pages 1-2).
- **Heart** (UBERON:0000948): cardiac rhabdomyomas (racioppi2024prenatalmtorinhibitors pages 1-2, okanishi2024diagnosticflowanalysis pages 5-7).
- **Lung** (UBERON:0002048): lymphangioleiomyomatosis (LAM) (conte2024therapeuticapproachesto pages 1-2).
- **Skin** (UBERON:0002097): angiofibromas, hypomelanotic macules, shagreen patch, ungual fibromas (jurca2023tuberoussclerosistype media b5f360a7).

### 7.2 Subcellular localization (GO cellular component suggestions)
Not explicitly specified in retrieved evidence; mechanistic elements imply cytosolic signaling complexes:
- GO:0005829 (cytosol)
- GO:0016020 (membrane) (RHEB signaling context; not explicitly stated in excerpts)

---

## 8. Temporal development

### 8.1 Onset
- TSC can present **prenatally**, often with **cardiac rhabdomyomas** (racioppi2024prenatalmtorinhibitors pages 1-2).
- Early-life diagnosis (<2 years) in claims data has median diagnosis age **5 months** (Japan cohort 2) (okanishi2024diagnosticflowanalysis pages 5-7).

### 8.2 Progression
Course is lifelong and multisystem; claims and real-world treatment studies imply need for ongoing surveillance and long-term therapy monitoring (monich2024tuberoussclerosiscomplex pages 1-2, cockerell2023effectivenessandsafety pages 1-2).

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent quantitative data)
- **Incidence** (review ranges): 1:6,000–1:10,000 live births (conte2024therapeuticapproachesto pages 1-2, monich2024tuberoussclerosiscomplex pages 1-2) and 1:5,800–1:13,520 live births (man2024thegeneticsof pages 1-2).
- **Regional prevalence (Japan, Shizuoka claims database):** adjusted prevalence **10.2 per 100,000** using ICD-10 Q85.1 (April 2012–Sep 2020) (kishida2025epidemiologicalinsightsand pages 1-2, kishida2025epidemiologicalinsightsand pages 2-4).
- **Age-specific prevalence** reported for Shizuoka 2019 shows higher prevalence in youth (e.g., male 0–19: 18.29/100,000; female 0–19: 15.38/100,000) (kishida2025epidemiologicalinsightsand pages 2-4).

### 9.2 Inheritance pattern and penetrance
- Autosomal dominant inheritance is consistent across recent sources (man2024thegeneticsof pages 1-2, conte2024therapeuticapproachesto pages 1-2, monich2024tuberoussclerosiscomplex pages 1-2).

### 9.3 Demographics
- Shizuoka cohort: sex distribution approximately balanced (48.2% male, 51.8% female in one analytic subset) with marked age effects and higher prevalence in young males in some analyses (kishida2025epidemiologicalinsightsand pages 1-2, kishida2025epidemiologicalinsightsand pages 2-4).

---

## 10. Diagnostics

### 10.1 Clinical criteria
A diagnostic criteria table was retrieved as an image (Table 2) listing major and minor features and genetic criteria.

- **Rule (as summarized in the figure extraction):** Definite diagnosis can be made with **two major** features, or **one major + ≥2 minor** features, or identification of a pathogenic **TSC1/TSC2** variant (jurca2023tuberoussclerosistype media b5f360a7).

### 10.2 Genetic testing (utility)
- Molecular genetic diagnosis “confirms the clinical diagnosis” and supports surveillance (dufneralmeida2024molecularandfunctional pages 1-2).
- Diagnostic yield in a recent cohort was **91%** (106/116) (dufneralmeida2024molecularandfunctional pages 1-2).
- Conventional testing may miss ~15% due to mosaicism/undetected variants (man2024thegeneticsof pages 1-2).

### 10.3 Real-world diagnostic delay and the role of TSC clinics (2024)
A 2024 Japanese claims analysis quantified diagnostic delay:
- Median time-to-diagnosis for **TSC-specific** manifestations was **1 month** vs **11 months** for more non-specific manifestations (p=0.0035) (okanishi2024diagnosticflowanalysis pages 4-5).
- For epilepsy, care at a facility with a **TSC clinic** shortened median time-to-diagnosis (**11.5 vs 19.0 months**, p=0.0379) (okanishi2024diagnosticflowanalysis pages 5-7).

---

## 11. Outcome / prognosis (burden, morbidity)

### 11.1 Major morbidity/mortality themes
A 2024 therapeutic review states that “brain tumours, sudden unexpected death from epilepsy, and respiratory conditions are the three leading causes of morbidity and mortality” (conte2024therapeuticapproachesto pages 1-2).

### 11.2 Quality of life and socioeconomic burden (2024)
A 2024 German matched case–control analysis provides quantified burden in adults with TSC-related epilepsy:
- EQ-5D-3L: TTO **0.705**; VAS **0.577** (lower than other epilepsy cohorts) (lappe2024amulticentermatched pages 1-2).
- Costs: mean total direct costs **€7,602** (median €2,620) and indirect productivity costs **€7,185** over 3 months (median €11,925) (lappe2024amulticentermatched pages 1-2).
- Unemployment: **60%** in TSC cohort (lappe2024amulticentermatched pages 1-2).

---

## 12. Treatment

### 12.1 Pharmacotherapy: mTOR inhibitors (everolimus/sirolimus)
**Mechanism:** mTOR inhibitors counteract mTORC1 hyperactivation due to TSC1/TSC2 loss (conte2024therapeuticapproachesto pages 1-2, monich2024tuberoussclerosiscomplex pages 1-2).

**Real-world effectiveness and safety (Dec 2023):** Multicenter Norway/Denmark cohort (N=64) treated with everolimus:
- **Epilepsy:** ≥50% seizure reduction in **31%** (14/45) (cockerell2023effectivenessandsafety pages 4-6).
- **Renal AML:** response (≥30% LD reduction) ~**35–38%** with most others stable (cockerell2023effectivenessandsafety pages 4-6).
- **SEGA:** example volume reductions **71%, 43%, 48%** after long-term treatment (cockerell2023effectivenessandsafety pages 6-7).
- **Adverse events:** 95% experienced AEs; stomatitis/oral ulceration 63%; URTI 38%; grade 3–4 AEs 36%; discontinuation 14% (9/64) (cockerell2023effectivenessandsafety pages 1-2, cockerell2023effectivenessandsafety pages 7-9).

**Randomized trial evidence summarized in 2024 nephrology review:** EXIST-2 AML response **42%** vs 0% placebo; extension response increased to **54%**, with ~97% showing some AML reduction (monich2024tuberoussclerosiscomplex pages 5-7).

**MAXO suggestions:**
- Everolimus/sirolimus therapy: MAXO:0000748 (mTOR inhibitor therapy) (suggested; ontology mapping should be verified).
- Embolization/nephrectomy for hemorrhage/complications: MAXO terms for embolization/nephrectomy (not retrieved directly, but surgical reserve for hemorrhage described) (monich2024tuberoussclerosiscomplex pages 1-2).

### 12.2 Epilepsy-specific therapy (including early/preventive concepts)
- Vigabatrin is described as first-line for early-onset seizures/infantile spasms in a 2024 review and is linked to high spasm control (review statement) (racioppi2024prenatalmtorinhibitors pages 2-3).

### 12.3 Surgical and interventional
- For kidney manifestations, mTOR inhibitors are “primary therapeutic option,” with nephrectomy/embolization reserved for complications such as severe renal hemorrhage (monich2024tuberoussclerosiscomplex pages 1-2).

### 12.4 Experimental / ongoing clinical trials (ClinicalTrials.gov)
Trials retrieved in the tool run include:
- **NCT04987463:** rapamycin vs vigabatrin prevention of TSC symptoms in infants (phase 2/3) (clinical trials search result list)
- **NCT05534672:** placebo-controlled rapamycin in drug-resistant epilepsy associated with TSC (phase 3; recruiting) (clinical trials search result list)
- Multiple topical rapamycin trials for facial angiofibromas (e.g., NCT01526356, NCT03140449) (clinical trials search result list)

---

## 13. Prevention

### 13.1 Primary prevention
Not currently feasible for monogenic TSC except via reproductive options; no population-level primary prevention strategies were identified in the retrieved evidence.

### 13.2 Secondary prevention (early detection and early intervention)
- Prenatal detection of cardiac rhabdomyomas can trigger early TSC evaluation (racioppi2024prenatalmtorinhibitors pages 1-2).
- Dedicated **TSC clinics** may shorten time to diagnosis for epilepsy presentations (okanishi2024diagnosticflowanalysis pages 5-7).

### 13.3 Tertiary prevention
- Surveillance and timely treatment of kidney and CNS tumors and seizure control reduce complications (supported by nephrology and therapeutic reviews emphasizing monitoring and mTOR inhibitor treatment) (monich2024tuberoussclerosiscomplex pages 1-2, conte2024therapeuticapproachesto pages 1-2).

---

## 14. Other species / natural disease
Not addressed in the retrieved evidence set.

---

## 15. Model organisms
The prenatal mTOR inhibitor review reports **three prenatal mouse studies** and human pregnancy case reports/series (10 treated pregnant women) evaluating prenatal mTOR inhibitor exposure and rhabdomyoma reduction (racioppi2024prenatalmtorinhibitors pages 1-2). Additional organism models (e.g., conditional Tsc1/Tsc2 mice, zebrafish, iPSC-derived models) were not retrieved in this tool run.

---

## Recent developments & real-world implementations (2023–2024 emphasis)

1. **Real-world everolimus effectiveness and toxicity quantification (2023):** multicenter observational outcomes provide practical estimates of seizure response (31%), AML shrinkage/stability, high AE burden (95%), and discontinuation (14%), underscoring the need for “close follow-up” in routine care (cockerell2023effectivenessandsafety pages 1-2).
2. **Health-system pathways for earlier diagnosis (2024):** claims-based analysis shows diagnostic delay is substantial for non-specific presentations and that specialty TSC clinics shorten time-to-diagnosis for epilepsy (p=0.0379), supporting center-of-excellence models (okanishi2024diagnosticflowanalysis pages 5-7).
3. **Nephrology perspective (2024):** reinforces shift toward mTOR inhibitors as first-line for renal manifestations and reserves invasive procedures for refractory complications (monich2024tuberoussclerosiscomplex pages 1-2).
4. **Prenatal/early mTOR inhibition research direction (2024):** early intervention strategies are being explored to reduce prenatal rhabdomyomas and potentially influence neurologic outcomes, but safety and neurodevelopmental benefit remain uncertain (racioppi2024prenatalmtorinhibitors pages 1-2).

---

## Limitations of this tool run (data gaps)
- **OMIM/Orphanet/MeSH/ICD-11 codes** were not retrieved; thus identifiers and synonyms may be incomplete.
- **PMIDs** were not available in the retrieved snippets for most sources; DOIs and journal metadata are provided.
- **Modifier genes, epigenetic signatures, omics profiles, and comprehensive model organism inventories** were not available in the current evidence set.

---

## Key source URLs (with publication dates)
- Cockerell et al. *Orphanet J Rare Dis* (Dec 2023): https://doi.org/10.1186/s13023-023-02982-1 (cockerell2023effectivenessandsafety pages 1-2)
- Man et al. *Genes* (Published 4 Mar 2024): https://doi.org/10.3390/genes15030332 (man2024thegeneticsof pages 1-2)
- Monich et al. *Brazilian Journal of Nephrology* (Published 05 Jul 2024): https://doi.org/10.1590/2175-8239-jbn-2024-0013en (monich2024tuberoussclerosiscomplex pages 1-2)
- Okanishi et al. *Orphanet J Rare Dis* (Dec 2024): https://doi.org/10.1186/s13023-024-03460-y (okanishi2024diagnosticflowanalysis pages 5-7)
- Conte et al. *Biomolecules* (21 Sep 2024): https://doi.org/10.3390/biom14091190 (conte2024therapeuticapproachesto pages 1-2)
- Racioppi et al. *J Clin Med* (23 Oct 2024): https://doi.org/10.3390/jcm13216335 (racioppi2024prenatalmtorinhibitors pages 1-2)
- Dufner‑Almeida et al. *Genes* (03 Nov 2024): https://doi.org/10.3390/genes15111432 (dufneralmeida2024molecularandfunctional pages 1-2)
- Lappe et al. *Neurological Research and Practice* (May 2024): https://doi.org/10.1186/s42466-024-00323-6 (lappe2024amulticentermatched pages 1-2)
- Kishida et al. *Orphanet J Rare Dis* (May 2025): https://doi.org/10.1186/s13023-025-03799-w (kishida2025epidemiologicalinsightsand pages 1-2)


References

1. (man2024thegeneticsof pages 1-2): Alice Man, Matteo Di Scipio, Shan Grewal, Yujin Suk, Elisabetta Trinari, Resham Ejaz, and Robyn Whitney. The genetics of tuberous sclerosis complex and related mtoropathies: current understanding and future directions. Genes, 15:332, Mar 2024. URL: https://doi.org/10.3390/genes15030332, doi:10.3390/genes15030332. This article has 47 citations.

2. (conte2024therapeuticapproachesto pages 1-2): Elena Conte, Brigida Boccanegra, Giorgia Dinoi, Michael Pusch, Annamaria De Luca, Antonella Liantonio, and Paola Imbrici. Therapeutic approaches to tuberous sclerosis complex: from available therapies to promising drug targets. Biomolecules, 14:1190, Sep 2024. URL: https://doi.org/10.3390/biom14091190, doi:10.3390/biom14091190. This article has 19 citations.

3. (racioppi2024prenatalmtorinhibitors pages 1-2): Giacomo Racioppi, Martina Proietti Checchi, Giorgia Sforza, Alessandra Voci, Luigi Mazzone, Massimiliano Valeriani, and Romina Moavero. Prenatal mtor inhibitors in tuberous sclerosis complex: current insights and future directions. Journal of Clinical Medicine, 13:6335, Oct 2024. URL: https://doi.org/10.3390/jcm13216335, doi:10.3390/jcm13216335. This article has 8 citations.

4. (dufneralmeida2024molecularandfunctional pages 1-2): Luiz Gustavo Dufner-Almeida, Laís F. M. Cardozo, Mariana R. Schwind, Danielly Carvalho, Juliana Paula G. Almeida, Andrea Maria Cappellano, Thiago G. P. Alegria, Santoesha Nanhoe, Mark Nellist, Maria Rita Passos-Bueno, Silvana Chiavegatto, Nasjla S. Silva, Sérgio Rosemberg, Ana Paula A. Pereira, Sérgio Antônio Antoniuk, and Luciana A. Haddad. Molecular and functional assessment of tsc1 and tsc2 in individuals with tuberous sclerosis complex. Genes, 15:1432, Nov 2024. URL: https://doi.org/10.3390/genes15111432, doi:10.3390/genes15111432. This article has 9 citations.

5. (monich2024tuberoussclerosiscomplex pages 1-2): Aline Grosskopf Monich, John J. Bissler, and Fellype Carvalho Barreto. Tuberous sclerosis complex and the kidneys: what nephrologists need to know. Brazilian Journal of Nephrology, Sep 2024. URL: https://doi.org/10.1590/2175-8239-jbn-2024-0013en, doi:10.1590/2175-8239-jbn-2024-0013en. This article has 2 citations.

6. (kishida2025epidemiologicalinsightsand pages 1-2): Satoshi Kishida, Eiji Nakatani, Takeshi Usui, Shuhei Fujimoto, Seiichiro Yamamoto, and Yoshiki Miyachi. Epidemiological insights and healthcare challenges of tuberous sclerosis complex in shizuoka prefecture: a retrospective cohort study. Orphanet Journal of Rare Diseases, May 2025. URL: https://doi.org/10.1186/s13023-025-03799-w, doi:10.1186/s13023-025-03799-w. This article has 2 citations and is from a peer-reviewed journal.

7. (kishida2025epidemiologicalinsightsand pages 2-4): Satoshi Kishida, Eiji Nakatani, Takeshi Usui, Shuhei Fujimoto, Seiichiro Yamamoto, and Yoshiki Miyachi. Epidemiological insights and healthcare challenges of tuberous sclerosis complex in shizuoka prefecture: a retrospective cohort study. Orphanet Journal of Rare Diseases, May 2025. URL: https://doi.org/10.1186/s13023-025-03799-w, doi:10.1186/s13023-025-03799-w. This article has 2 citations and is from a peer-reviewed journal.

8. (kishida2025epidemiologicalinsightsand pages 5-6): Satoshi Kishida, Eiji Nakatani, Takeshi Usui, Shuhei Fujimoto, Seiichiro Yamamoto, and Yoshiki Miyachi. Epidemiological insights and healthcare challenges of tuberous sclerosis complex in shizuoka prefecture: a retrospective cohort study. Orphanet Journal of Rare Diseases, May 2025. URL: https://doi.org/10.1186/s13023-025-03799-w, doi:10.1186/s13023-025-03799-w. This article has 2 citations and is from a peer-reviewed journal.

9. (racioppi2024prenatalmtorinhibitors pages 2-3): Giacomo Racioppi, Martina Proietti Checchi, Giorgia Sforza, Alessandra Voci, Luigi Mazzone, Massimiliano Valeriani, and Romina Moavero. Prenatal mtor inhibitors in tuberous sclerosis complex: current insights and future directions. Journal of Clinical Medicine, 13:6335, Oct 2024. URL: https://doi.org/10.3390/jcm13216335, doi:10.3390/jcm13216335. This article has 8 citations.

10. (jurca2023tuberoussclerosistype media b5f360a7): Claudia Maria Jurca, Kinga Kozma, Codruta Diana Petchesi, Dana Carmen Zaha, Ioan Magyar, Mihai Munteanu, Lucian Faur, Aurora Jurca, Dan Bembea, Emilia Severin, and Alexandru Daniel Jurca. Tuberous sclerosis, type ii diabetes mellitus and the pi3k/akt/mtor signaling pathways—case report and literature review. Genes, 14:433, Feb 2023. URL: https://doi.org/10.3390/genes14020433, doi:10.3390/genes14020433. This article has 23 citations.

11. (okanishi2024diagnosticflowanalysis pages 4-5): Tohru Okanishi, Ikuo Fujimori, Mariko Yamada, Takumi Tajima, Mari Wataya-Kaneda, Kuniaki Seyama, and Takashi Hatano. Diagnostic flow analysis of tuberous sclerosis complex in japan: a retrospective claims database study. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03460-y, doi:10.1186/s13023-024-03460-y. This article has 2 citations and is from a peer-reviewed journal.

12. (okanishi2024diagnosticflowanalysis pages 1-2): Tohru Okanishi, Ikuo Fujimori, Mariko Yamada, Takumi Tajima, Mari Wataya-Kaneda, Kuniaki Seyama, and Takashi Hatano. Diagnostic flow analysis of tuberous sclerosis complex in japan: a retrospective claims database study. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03460-y, doi:10.1186/s13023-024-03460-y. This article has 2 citations and is from a peer-reviewed journal.

13. (okanishi2024diagnosticflowanalysis pages 7-9): Tohru Okanishi, Ikuo Fujimori, Mariko Yamada, Takumi Tajima, Mari Wataya-Kaneda, Kuniaki Seyama, and Takashi Hatano. Diagnostic flow analysis of tuberous sclerosis complex in japan: a retrospective claims database study. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03460-y, doi:10.1186/s13023-024-03460-y. This article has 2 citations and is from a peer-reviewed journal.

14. (okanishi2024diagnosticflowanalysis pages 5-7): Tohru Okanishi, Ikuo Fujimori, Mariko Yamada, Takumi Tajima, Mari Wataya-Kaneda, Kuniaki Seyama, and Takashi Hatano. Diagnostic flow analysis of tuberous sclerosis complex in japan: a retrospective claims database study. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03460-y, doi:10.1186/s13023-024-03460-y. This article has 2 citations and is from a peer-reviewed journal.

15. (cockerell2023effectivenessandsafety pages 1-2): Ine Cockerell, Jakob Christensen, Christina E. Hoei-Hansen, Lotte Holst, Mikkel Grenaa Frederiksen, Aart Imran Issa-Epe, Bård Nedregaard, Ragnar Solhoff, Ketil Heimdal, Cecilie Johannessen Landmark, Caroline Lund, and Terje Nærland. Effectiveness and safety of everolimus treatment in patients with tuberous sclerosis complex in real-world clinical practice. Orphanet Journal of Rare Diseases, Dec 2023. URL: https://doi.org/10.1186/s13023-023-02982-1, doi:10.1186/s13023-023-02982-1. This article has 26 citations and is from a peer-reviewed journal.

16. (cockerell2023effectivenessandsafety pages 4-6): Ine Cockerell, Jakob Christensen, Christina E. Hoei-Hansen, Lotte Holst, Mikkel Grenaa Frederiksen, Aart Imran Issa-Epe, Bård Nedregaard, Ragnar Solhoff, Ketil Heimdal, Cecilie Johannessen Landmark, Caroline Lund, and Terje Nærland. Effectiveness and safety of everolimus treatment in patients with tuberous sclerosis complex in real-world clinical practice. Orphanet Journal of Rare Diseases, Dec 2023. URL: https://doi.org/10.1186/s13023-023-02982-1, doi:10.1186/s13023-023-02982-1. This article has 26 citations and is from a peer-reviewed journal.

17. (cockerell2023effectivenessandsafety pages 2-4): Ine Cockerell, Jakob Christensen, Christina E. Hoei-Hansen, Lotte Holst, Mikkel Grenaa Frederiksen, Aart Imran Issa-Epe, Bård Nedregaard, Ragnar Solhoff, Ketil Heimdal, Cecilie Johannessen Landmark, Caroline Lund, and Terje Nærland. Effectiveness and safety of everolimus treatment in patients with tuberous sclerosis complex in real-world clinical practice. Orphanet Journal of Rare Diseases, Dec 2023. URL: https://doi.org/10.1186/s13023-023-02982-1, doi:10.1186/s13023-023-02982-1. This article has 26 citations and is from a peer-reviewed journal.

18. (cockerell2023effectivenessandsafety pages 6-7): Ine Cockerell, Jakob Christensen, Christina E. Hoei-Hansen, Lotte Holst, Mikkel Grenaa Frederiksen, Aart Imran Issa-Epe, Bård Nedregaard, Ragnar Solhoff, Ketil Heimdal, Cecilie Johannessen Landmark, Caroline Lund, and Terje Nærland. Effectiveness and safety of everolimus treatment in patients with tuberous sclerosis complex in real-world clinical practice. Orphanet Journal of Rare Diseases, Dec 2023. URL: https://doi.org/10.1186/s13023-023-02982-1, doi:10.1186/s13023-023-02982-1. This article has 26 citations and is from a peer-reviewed journal.

19. (cockerell2023effectivenessandsafety pages 7-9): Ine Cockerell, Jakob Christensen, Christina E. Hoei-Hansen, Lotte Holst, Mikkel Grenaa Frederiksen, Aart Imran Issa-Epe, Bård Nedregaard, Ragnar Solhoff, Ketil Heimdal, Cecilie Johannessen Landmark, Caroline Lund, and Terje Nærland. Effectiveness and safety of everolimus treatment in patients with tuberous sclerosis complex in real-world clinical practice. Orphanet Journal of Rare Diseases, Dec 2023. URL: https://doi.org/10.1186/s13023-023-02982-1, doi:10.1186/s13023-023-02982-1. This article has 26 citations and is from a peer-reviewed journal.

20. (cockerell2023effectivenessandsafety pages 10-12): Ine Cockerell, Jakob Christensen, Christina E. Hoei-Hansen, Lotte Holst, Mikkel Grenaa Frederiksen, Aart Imran Issa-Epe, Bård Nedregaard, Ragnar Solhoff, Ketil Heimdal, Cecilie Johannessen Landmark, Caroline Lund, and Terje Nærland. Effectiveness and safety of everolimus treatment in patients with tuberous sclerosis complex in real-world clinical practice. Orphanet Journal of Rare Diseases, Dec 2023. URL: https://doi.org/10.1186/s13023-023-02982-1, doi:10.1186/s13023-023-02982-1. This article has 26 citations and is from a peer-reviewed journal.

21. (monich2024tuberoussclerosiscomplex pages 5-7): Aline Grosskopf Monich, John J. Bissler, and Fellype Carvalho Barreto. Tuberous sclerosis complex and the kidneys: what nephrologists need to know. Brazilian Journal of Nephrology, Sep 2024. URL: https://doi.org/10.1590/2175-8239-jbn-2024-0013en, doi:10.1590/2175-8239-jbn-2024-0013en. This article has 2 citations.

22. (lappe2024amulticentermatched pages 1-2): Lisa Lappe, Christoph Hertzberg, Susanne Knake, Markus Knuf, Felix von Podewils, Laurent M. Willems, Stjepana Kovac, Johann Philipp Zöllner, Matthias Sauter, Gerhard Kurlemann, Thomas Mayer, Astrid Bertsche, Klaus Marquard, Sascha Meyer, Hannah Schäfer, Charlotte Thiels, Bianca Zukunft, Susanne Schubert-Bast, Jens-Peter Reese, Felix Rosenow, and Adam Strzelczyk. A multicenter, matched case–control analysis comparing burden of illness among patients with tuberous sclerosis complex related epilepsy, generalized idiopathic epilepsy, and focal epilepsy in germany. Neurological Research and Practice, May 2024. URL: https://doi.org/10.1186/s42466-024-00323-6, doi:10.1186/s42466-024-00323-6. This article has 8 citations and is from a peer-reviewed journal.

23. (lappe2024amulticentermatched pages 10-11): Lisa Lappe, Christoph Hertzberg, Susanne Knake, Markus Knuf, Felix von Podewils, Laurent M. Willems, Stjepana Kovac, Johann Philipp Zöllner, Matthias Sauter, Gerhard Kurlemann, Thomas Mayer, Astrid Bertsche, Klaus Marquard, Sascha Meyer, Hannah Schäfer, Charlotte Thiels, Bianca Zukunft, Susanne Schubert-Bast, Jens-Peter Reese, Felix Rosenow, and Adam Strzelczyk. A multicenter, matched case–control analysis comparing burden of illness among patients with tuberous sclerosis complex related epilepsy, generalized idiopathic epilepsy, and focal epilepsy in germany. Neurological Research and Practice, May 2024. URL: https://doi.org/10.1186/s42466-024-00323-6, doi:10.1186/s42466-024-00323-6. This article has 8 citations and is from a peer-reviewed journal.

24. (okanishi2024diagnosticflowanalysis pages 2-4): Tohru Okanishi, Ikuo Fujimori, Mariko Yamada, Takumi Tajima, Mari Wataya-Kaneda, Kuniaki Seyama, and Takashi Hatano. Diagnostic flow analysis of tuberous sclerosis complex in japan: a retrospective claims database study. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03460-y, doi:10.1186/s13023-024-03460-y. This article has 2 citations and is from a peer-reviewed journal.
