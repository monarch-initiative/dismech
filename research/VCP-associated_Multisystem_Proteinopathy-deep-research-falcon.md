---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-22T19:46:11.003418'
end_time: '2026-04-22T20:00:07.049472'
duration_seconds: 836.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: VCP-Associated Multisystem Proteinopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** VCP-Associated Multisystem Proteinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **VCP-Associated Multisystem Proteinopathy** covering all of the
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
- **Disease Name:** VCP-Associated Multisystem Proteinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **VCP-Associated Multisystem Proteinopathy** covering all of the
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


# VCP-Associated Multisystem Proteinopathy (VCP-MSP / MSP1 / IBMPFD): Disease Characteristics Research Report

**Scope note (evidence limitations):** The tool-retrieved corpus strongly supports clinical spectrum, natural history, management guidance (2023), and mechanistic/therapeutic research advances (2024). However, authoritative *database identifiers* (Orphanet, MeSH, ICD-10/ICD-11) were not directly retrievable in the current evidence set; they are therefore flagged as *not available from this evidence* rather than inferred.

---

## 1. Disease Information

### 1.1 Definition and overview
VCP-associated multisystem proteinopathy (VCP-MSP; often MSP1) is a **progressive, autosomal dominant** disorder caused by pathogenic variants in **VCP (p97)**, characterized by variable combinations of **inclusion body myopathy**, **Paget disease of bone (PDB)**, **frontotemporal dementia (FTD)**, and less commonly **motor neuron disease/ALS** and **parkinsonism**. This pleiotropy and variable expressivity make clinical prediction challenging. (pontifex2024valosincontainingprotein(vcp) pages 1-2, shmara2023prevalenceoffrontotemporal pages 1-2, schiava2022genotype–phenotypecorrelationsin pages 3-4)

**Primary literature abstract quote (management guideline):** “**Ninety percent of patients with VCP-associated MSP have myopathy**…” (roy2023provisionalpracticerecommendation pages 1-2)

### 1.2 Key identifiers
- **OMIM/MIM:** IBMPFD / VCP disease is referenced as **MIM 167320** (primary literature mention). (iannibelli2023vcprelatedmyopathya pages 1-2)
- **MONDO:** OpenTargets evidence (outside the citable context set) suggests MONDO disease entities exist for the IBMPFD spectrum, but **MONDO IDs are not citable from the present evidence snippets**.
- **Orphanet / ICD-10 / ICD-11 / MeSH:** **Not available from the present tool-retrieved evidence**.

### 1.3 Synonyms and alternative names
Common synonyms used in the literature include:
- **MSP1** / “multisystem proteinopathy-1” (robinson2024elevatedvcpatpase pages 1-3)
- **IBMPFD** (“inclusion body myopathy with Paget disease of bone and frontotemporal dementia”) (iannibelli2023vcprelatedmyopathya pages 1-2, shmara2023prevalenceoffrontotemporal pages 1-2)
- **VCP disease** (pontifex2024valosincontainingprotein(vcp) pages 1-2, shmara2023prevalenceoffrontotemporal pages 1-2)

### 1.4 Evidence source type
Most disease-level statements below are derived from **aggregated cohorts, multicenter retrospective datasets, and patient registries**, supplemented by **case series** and **cell-model mechanistic studies**. Examples include a multicentre retrospective cohort (n=255) (schiava2022genotype–phenotypecorrelationsin pages 3-4, schiava2022genotype–phenotypecorrelationsin pages 4-6), a large family-based cohort (n=231) (alobeidi2018genotype‐phenotypestudyin pages 1-5), and a patient registry (n=59) (ikenaga2020phenotypicdiversityin pages 1-2).

---

## 2. Etiology

### 2.1 Primary causal factors
**Genetic cause:** Pathogenic **heterozygous VCP variants** cause VCP-MSP, typically via **missense** variants; mutational hotspots include residues around **155 and 159**. (pontifex2024valosincontainingprotein(vcp) pages 1-2, shmara2023prevalenceoffrontotemporal pages 1-2)

**Abstract quote (review):** “**VCP variants cause multisystem proteinopathy**…” and VCP is “crucial to… protein quality control… autophagy… stress granule formation and clearance…” (pontifex2024valosincontainingprotein(vcp) pages 1-2)

### 2.2 Risk factors
- **Family history / autosomal dominant inheritance** is the main risk factor because disease is driven by pathogenic germline VCP variants. (shmara2023prevalenceoffrontotemporal pages 1-2, schiava2022genotype–phenotypecorrelationsin pages 3-4)
- **Variant-specific risk modulation:** For example, in a Hispanic kindred series with **p.R159H**, FTD was unusually prevalent while PDB was rare compared with historical cohorts, suggesting genotype-by-ancestry or background modifiers. (shmara2023prevalenceoffrontotemporal pages 1-2)

### 2.3 Protective factors
No validated protective genetic or environmental factors were identified in the retrieved evidence. Variant-level effects on ATPase activity may influence severity/onset but are not “protective” in the usual epidemiologic sense. (robinson2024elevatedvcpatpase pages 1-3, mahsom2023anautosomaldominantchildhoodonset pages 1-3)

### 2.4 Gene–environment interactions
No direct gene–environment interaction evidence was retrieved.

---

## 3. Phenotypes (with suggested HPO terms)

### 3.1 Core phenotype domains
The core phenotype includes:

#### A) Myopathy (inclusion body myopathy / limb-girdle pattern)
- **Frequency:** ~90% in large cohorts/registries (e.g., 168/187 symptomatic; 89.8%). (alobeidi2018genotype‐phenotypestudyin pages 5-7, alobeidi2018genotype‐phenotypestudyin pages 1-5)
- **Age of onset:** mean ~43 years (range 20–70) in the 231-individual cohort. (alobeidi2018genotype‐phenotypestudyin pages 5-7)
- **Typical onset pattern:** slowly progressive weakness; in a multicentre cohort, weakness was the initial symptom in **90.7%** and was slowly progressive in **89.1%**. (schiava2022genotype–phenotypecorrelationsin pages 4-6)
- **Suggested HPO:** HP:0003323 (Progressive muscle weakness), HP:0002650 (Skeletal muscle atrophy), HP:0003198 (Myopathy), HP:0002355 (Muscle weakness), HP:0000007 (Autosomal dominant inheritance—phenotype context), HP:0003677 (Gower sign) (clinical reports), HP:0003227 (Scapular winging) (schiava2022genotype–phenotypecorrelationsin pages 4-6, roy2023provisionalpracticerecommendation pages 5-7)

#### B) Paget disease of bone (PDB)
- **Frequency:** 42.4% in the 231-individual cohort; 28.2% in a 255-patient multicentre dataset. (alobeidi2018genotype‐phenotypestudyin pages 5-7, schiava2022genotype–phenotypecorrelationsin pages 3-4)
- **Age of onset:** mean ~41.2 years (range 23–65). (alobeidi2018genotype‐phenotypestudyin pages 5-7)
- **Suggested HPO:** HP:0002653 (Osteitis deformans), HP:0002755 (Abnormal bone remodeling), HP:0002676 (Bone pain)

#### C) Frontotemporal dementia / cognitive impairment
- **Frequency:** ~29–30% in the 231-individual cohort; 14.3% FTD in the multicentre dataset summary; cognitive impairment 25.5% with FTD the most common cognitive pattern among those impaired. (alobeidi2018genotype‐phenotypestudyin pages 7-10, schiava2022genotype–phenotypecorrelationsin pages 3-4, schiava2022genotype–phenotypecorrelationsin pages 4-6)
- **Age of onset:** mean ~55.9 years (range 30–86). (alobeidi2018genotype‐phenotypestudyin pages 7-10)
- **Suggested HPO:** HP:0000741 (Dementia), HP:0002145 (Frontotemporal dementia), HP:0000716 (Depression) / HP:0000739 (Anxiety) where present (not quantified here)

#### D) Motor neuron disease / ALS phenotype
- **Frequency:** ~8.6–9% in cohort data. (alobeidi2018genotype‐phenotypestudyin pages 7-10, shmara2023prevalenceoffrontotemporal pages 1-2)
- **Suggested HPO:** HP:0007354 (Amyotrophic lateral sclerosis), HP:0001324 (Muscle fasciculations), HP:0001761 (Spasticity)

### 3.2 Respiratory and bulbar involvement (important for morbidity)
A large multicentre cohort found substantial respiratory burden: **dyspnoea on exertion 25.3%**, **nocturnal hypoventilation 15.6%**, **FVC <80% in 52.6%** of tested individuals, and noninvasive ventilation use in subsets. (schiava2022genotype–phenotypecorrelationsin pages 4-6)

Registry data also highlight dyspnea/dysphagia as meaningful patient-reported problems (dyspnea on exertion 42%; dysphagia 22%). (ikenaga2020phenotypicdiversityin pages 1-2)

Suggested HPO: HP:0002094 (Dyspnea), HP:0010535 (Nocturnal hypoventilation), HP:0002093 (Respiratory insufficiency), HP:0002015 (Dysphagia).

### 3.3 Quality of life impact
Patient-reported functional limitations are common; in a registry cohort, sit-to-stand difficulty (72%), walking difficulty (67%), and stair climbing difficulty (85%) were reported, and 59% rated QOL “more than good.” (ikenaga2020phenotypicdiversityin pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **Gene:** **VCP** (valosin containing protein; p97), encoding an AAA+ ATPase. (pontifex2024valosincontainingprotein(vcp) pages 1-2, iannibelli2023vcprelatedmyopathya pages 1-2)

### 4.2 Pathogenic variant classes and functional consequences
- **Variant class:** Predominantly **heterozygous missense** variants in VCP-MSP cohorts; multicenter variant-classification work reports nearly all evaluated variants were missense (with rare small indel). (schiava2023clinicalclassificationof pages 1-2)
- **Functional consequence:** Many MSP-associated variants show **elevated (“hyperactive”) basal ATPase activity**, consistent with a gain-of-function/hyperactivity model for many variants. (robinson2024elevatedvcpatpase pages 1-3, schiava2023clinicalclassificationof pages 1-2)

**2023 variant-classification study (clinical + functional):** 19 novel/uncharacterized variants were evaluated with a **6-item clinical scoring system** (ROC-derived cutoff **≥3** for “high likelihood disease-associated”) and compared with ATPase and in silico data. Thirteen of 19 increased ATPase activity; 18/19 were in the N and D1 domains. (schiava2023clinicalclassificationof pages 1-2, schiava2023clinicalclassificationof pages 6-7)

### 4.3 Emerging genotype–biochemistry–phenotype correlation (2024)
A 2024 Neurology Genetics analysis found **intrinsic VCP ATPase activity inversely correlated with age at onset** across common variants.
- Example: **R155C** had **earliest onset 38.15 ± 9.78 years** and high ATPase activity (~399% WT); **R93C** had later onset (51.15 ± 6.67 years) and lower ATPase (still elevated; ~310% WT). (robinson2024elevatedvcpatpase pages 3-4)
- Reported correlation: **r = −0.94 (p = 0.01)** across five variants for ATPase activity vs age at onset. (robinson2024elevatedvcpatpase pages 1-3)

Interpretation: ATPase activity may be a **variant-severity proxy** and could support classification of uncertain variants, but exceptions exist (e.g., VCP variants with normal or reduced ATPase linked to other phenotypes). (robinson2024elevatedvcpatpase pages 4-5)

### 4.4 Distinct childhood-onset VCP disorder (important differential within “VCP-related disease”)
A 2023 AJHG study described an autosomal-dominant **childhood-onset neurodevelopmental disorder** (DD/ID, hypotonia, macrocephaly) due to heterozygous VCP variants, mostly de novo; functional studies showed **most variants decreased ATPase activity**, contrasting with MSP-associated hyperactivity, suggesting a distinct pathomechanism (loss-of-function/haploinsufficiency or hypomorphic VCP). (mahsom2023anautosomaldominantchildhoodonset pages 1-3, mahsom2023anautosomaldominantchildhoodonset pages 12-13)

---

## 5. Environmental Information
No disease-specific environmental/lifestyle/infectious triggers were identified in the retrieved evidence.

---

## 6. Mechanism / Pathophysiology (with GO/CL suggestions)

### 6.1 Current mechanistic understanding (conceptual model)
VCP/p97 is a **multifunctional AAA+ ATPase** that helps maintain proteostasis across multiple pathways (UPS, ERAD, autophagy/mitophagy/lysophagy, stress granules, and DNA damage responses). Disruption of these pathways by pathogenic VCP variants can drive accumulation of ubiquitinated proteins and protein aggregates/inclusions across tissues (muscle, bone, brain). (pontifex2024valosincontainingprotein(vcp) pages 1-2, schiava2022genotype–phenotypecorrelationsin pages 3-4)

**GO biological process suggestions:**
- GO:0006511 (ubiquitin-dependent protein catabolic process)
- GO:0006914 (autophagy)
- GO:0030433 (ubiquitin-dependent ERAD pathway)
- GO:0016236 (macroautophagy)
- GO:0070848 (response to proteasome inhibitor)

**GO cellular component suggestions:**
- GO:0005829 (cytosol)
- GO:0005634 (nucleus)
- GO:0005773 (vacuole) / lysosome-related compartments

**Cell ontology (CL) suggestions (relevant affected cell types):**
- CL:0000187 (muscle cell / myocyte)
- CL:0000092 (osteoclast)
- CL:0000540 (neuron)
- CL:0000047 (motor neuron)

### 6.2 2024 mechanistic advance: nuclear proteostasis defects + ubiquitinated intranuclear inclusions
A 2024 JCI study proposed a shared MSP pathology across tissues: **ubiquitinated intranuclear inclusions in myocytes, osteoclasts, and neurons**, and showed MSP variants reduce nuclear VCP, impairing nuclear clearance of TDP-43 aggregates. (phan2024vcpactivatorreverses pages 1-2, phan2024vcpactivatorreverses pages 2-4)

**Primary abstract quote (2024 JCI):** “We found that these diseases exhibit a common pathologic feature: **ubiquitinated intranuclear inclusions affecting myocytes, osteoclasts, and neurons**… cells harboring MSP variants… exhibited decreased clearance of insoluble intranuclear TDP-43 aggregates.” (phan2024vcpactivatorreverses pages 1-2)

### 6.3 Therapeutic-development implication (2024): VCP activation to enhance TDP-43 clearance
In the same 2024 JCI study, four small molecules (UP109, UP158, UP163, UP12) were identified as **VCP activators** (primarily increasing D2 ATPase activity). Pharmacologic VCP activation (notably **UP109**) enhanced clearance of insoluble intranuclear TDP-43 aggregates in cell and iPSC-derived neuron models carrying pathogenic VCP variants. (phan2024vcpactivatorreverses pages 10-13, phan2024vcpactivatorreverses pages 1-2)

This is notable because it contrasts with a parallel line of thinking that **inhibiting hyperactive VCP ATPase** could help some MSP variants; together, these studies suggest **directionality of VCP modulation may depend on which VCP function/subcellular compartment is limiting** and which variant mechanism predominates. (robinson2024elevatedvcpatpase pages 4-5, phan2024vcpactivatorreverses pages 1-2)

---

## 7. Anatomical Structures Affected (UBERON suggestions)

**Primary organs/systems affected:**
- **Skeletal muscle** (primary disability driver). (schiava2022genotype–phenotypecorrelationsin pages 4-6, alobeidi2018genotype‐phenotypestudyin pages 1-5)
- **Bone** (Paget disease lesions; often axial skeleton/pelvis). (alobeidi2018genotype‐phenotypestudyin pages 5-7, columbres2024bonescanfindings pages 1-2)
- **Brain** (FTD; TDP-43 pathology). (shmara2023prevalenceoffrontotemporal pages 1-2, phan2024vcpactivatorreverses pages 1-2)
- **Respiratory system** (ventilatory insufficiency; FVC decline). (schiava2022genotype–phenotypecorrelationsin pages 3-4, schiava2022genotype–phenotypecorrelationsin pages 4-6)
- **Heart** (less common but clinically relevant). (roy2023provisionalpracticerecommendation pages 2-3)

**UBERON suggestions:** UBERON:0002374 (skeletal muscle), UBERON:0001474 (bone tissue), UBERON:0000955 (brain), UBERON:0002048 (lung), UBERON:0000948 (heart), UBERON:0000970 (spinal cord).

---

## 8. Temporal Development (onset and progression)

- **Typical onset:** Adult onset is common; mean age at onset ~45.6 ± 9.3 years in a multicentre cohort. (schiava2022genotype–phenotypecorrelationsin pages 3-4)
- **Diagnostic delay:** Mean **7.7 ± 6 years**. (schiava2022genotype–phenotypecorrelationsin pages 3-4)
- **Progression/disability:** Full-time wheelchair use in **19.1%**, median **8.5 years** from onset to full-time wheelchair use. (schiava2022genotype–phenotypecorrelationsin pages 3-4)
- **Respiratory decline as a progression marker:** **FVC <50%** predicted was associated with becoming a full-time wheelchair user; **FVC <70%** and wheelchair dependence were associated with death. (schiava2022genotype–phenotypecorrelationsin pages 3-4)

---

## 9. Inheritance and Population

### 9.1 Inheritance
- **Autosomal dominant** inheritance is repeatedly described across cohorts and clinical reports. (shmara2023prevalenceoffrontotemporal pages 1-2, schiava2022genotype–phenotypecorrelationsin pages 3-4)

### 9.2 Epidemiology
A UK-based estimate reported a **prevalence ~0.66 per 100,000** for IBMPFD/VCP disease. (schiava2022genotype–phenotypecorrelationsin pages 3-4)

### 9.3 Population/genotype observations
- A Hispanic family series with **p.R159H** reported a phenotype skewed toward FTD (72%) with low PDB (3%), emphasizing ancestry/background as a factor in observed expressivity. (shmara2023prevalenceoffrontotemporal pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical evaluation
Given pleiotropy, evaluation commonly includes neuromuscular exam plus screening for bone disease and cognition, and respiratory/cardiac assessment. (roy2023provisionalpracticerecommendation pages 5-7, roy2023provisionalpracticerecommendation pages 2-3)

### 10.2 Laboratory tests / biomarkers
- **CK:** often normal or mildly elevated; in one cohort median CK at onset 254 UI/L (subset), and guidelines note CK often normal/mildly elevated. (schiava2022genotype–phenotypecorrelationsin pages 4-6, roy2023provisionalpracticerecommendation pages 3-5)
- **Alkaline phosphatase (ALP):** can be elevated in PDB but may be insensitive (e.g., bone scan study found only 1 active PDB patient with elevated ALP). (columbres2024bonescanfindings pages 8-9, columbres2024bonescanfindings pages 5-8)

### 10.3 Imaging
- **Muscle MRI** is helpful to characterize distribution and rule out mimics; common finding is fatty replacement in calves/quadriceps/hamstrings. (roy2023provisionalpracticerecommendation pages 2-3, roy2023provisionalpracticerecommendation pages 3-5)
- **Bone imaging for PDB:** A 2024 study supports Tc-99m bone scan as a sensitive screening tool in MSP1. In 12 VCP-MSP1 patients, 2 previously undiagnosed PDB cases were detected by bone scan and confirmed radiographically; common involved sites included thoracic spine/ribs, pelvis, shoulder, and calvarium. (columbres2024bonescanfindings pages 1-2)

### 10.4 Electrodiagnostics
EMG/NCS patterns are heterogeneous and can be myopathic, neurogenic, or mixed; thus supportive rather than definitive. (roy2023provisionalpracticerecommendation pages 3-5)

### 10.5 Muscle biopsy and pathology
Muscle biopsy may show rimmed vacuoles and ubiquitin/TDP-43-positive inclusions, but sensitivity is limited.
- Rimmed vacuoles present in ~40% in large series and cited guidelines. (roy2023provisionalpracticerecommendation pages 3-5, iannibelli2023vcprelatedmyopathya pages 10-10)

### 10.6 Genetic testing (definitive)
Consensus recommendations emphasize genetic confirmation.

**Abstract quote (2023 practice recommendation):** “**Genetic testing is the only definitive way to diagnose VCP myopathy**…” (roy2023provisionalpracticerecommendation pages 1-2)

Testing strategy:
- Single-variant testing when a familial pathogenic variant is known; otherwise multi-gene panels for undifferentiated myopathy (with inclusion of VCP and related MSP genes). (roy2023provisionalpracticerecommendation pages 1-2, roy2023provisionalpracticerecommendation pages 5-7)
- Variant interpretation support: a 2023 multicenter effort proposed a clinical scoring + ATPase framework for novel VCP variants. (schiava2023clinicalclassificationof pages 1-2)

### 10.7 Differential diagnosis (examples)
Because VCP myopathy can mimic limb-girdle dystrophies and inclusion body myositis, workup typically includes evaluation for other inherited myopathies and acquired IBM (biopsy interpretation and genetics). (roy2023provisionalpracticerecommendation pages 1-2, roy2023provisionalpracticerecommendation pages 3-5)

---

## 11. Outcome / Prognosis

- **Disability:** Wheelchair dependence is common over time (median 8.5 years to full-time wheelchair use among those who become full-time users). (schiava2022genotype–phenotypecorrelationsin pages 3-4)
- **Respiratory involvement:** Common and prognostically important, with FVC thresholds associated with disability and death. (schiava2022genotype–phenotypecorrelationsin pages 3-4, schiava2022genotype–phenotypecorrelationsin pages 4-6)
- **Mortality drivers:** Respiratory failure and cardiomyopathy are repeatedly emphasized as major causes of death in VCP-MSP; the multicentre dataset formally links respiratory impairment markers (FVC) and wheelchair dependence to death. (schiava2022genotype–phenotypecorrelationsin pages 3-4)

---

## 12. Treatment

### 12.1 Current standard management (real-world implementation)
There is **no approved disease-modifying therapy** for VCP-MSP myopathy; management is supportive and multidisciplinary.

**Evidence from 2023 consensus recommendations:**
- “Management… is supportive—there is no approved disease-modifying therapy…” (roy2023provisionalpracticerecommendation pages 5-7)
- Pulmonary and cardiac screening and referral are recommended; mobility aids and PT/OT/speech support may be needed. (roy2023provisionalpracticerecommendation pages 5-7, roy2023provisionalpracticerecommendation pages 2-3)

**MAXO suggestions (supportive actions):**
- MAXO:0000011 (physical therapy)
- MAXO:0000012 (occupational therapy)
- MAXO:0000472 (respiratory monitoring)
- MAXO:0000598 (noninvasive ventilation)
- MAXO:0001020 (genetic counseling)

### 12.2 Management of Paget disease of bone
Bisphosphonate therapy is noted as effective for PDB-related symptoms and complication prevention in the 2024 bone scan study discussion context. (columbres2024bonescanfindings pages 1-2)

**MAXO suggestions:** MAXO:0000410 (bisphosphonate therapy), MAXO:0000498 (bone scintigraphy), MAXO:0000127 (radiography).

### 12.3 Experimental / emerging therapeutic strategies
**A) VCP activity modulation (precision-mechanism dependent):**
- **VCP activation (2024):** UP109 and related compounds improved nuclear TDP-43 aggregate clearance in MSP models, motivating a “VCP activator” approach for nuclear proteostasis defects. (phan2024vcpactivatorreverses pages 10-13, phan2024vcpactivatorreverses pages 1-2)
- **VCP inhibition (2024 correlation paper):** Higher ATPase hyperactivity correlates with earlier onset, and authors suggest ATPase inhibition “may be therapeutic” for hyperactive variants, highlighting mechanistic heterogeneity and the need for careful target validation. (robinson2024elevatedvcpatpase pages 1-3, robinson2024elevatedvcpatpase pages 4-5)

### 12.4 Clinical trials and registries (real-world implementation)
- **NCT04823143** (Natural History Study of Patients With VCP-related Disease): completed prospective observational study (start **2021-03-18**; completion listed **2025-08-31**; last update **2026-03**), n=44, hybrid remote/onsite visits, endpoints include FVC and multiple functional and patient-reported measures (PROMIS, Neuro-QOL, ROADS, EAT-10, etc.). (NCT04823143 chunk 1)
  - URL: https://clinicaltrials.gov/study/NCT04823143 (trial record)
- **NCT01353430** (UC Irvine characterization of IBMPFD): observational, recruiting; includes MRI and bone scan in subsets. (NCT01353430 chunk 1)
  - URL: https://clinicaltrials.gov/study/NCT01353430 (trial record)

---

## 13. Prevention

No primary prevention is currently available because disease is genetic; prevention focuses on **genetic counseling** and **cascade testing**.
- Genetic counseling is recommended prior to presymptomatic testing. (roy2023provisionalpracticerecommendation pages 5-7)

**MAXO suggestions:** MAXO:0001020 (genetic counseling), MAXO:0000125 (predictive genetic testing), MAXO:0000130 (cascade screening).

---

## 14. Other Species / Natural Disease
No naturally occurring non-human disease evidence was retrieved in the current tool context.

---

## 15. Model Organisms
Model-organism evidence was not retrieved in a citable form in the current evidence snippets; consequently, no specific models are asserted here.

---

## Recent quantitative summary (cross-study)
The following table consolidates key quantitative findings (frequencies, onset, respiratory and disability metrics) from major cohorts, registries, and a recent PDB imaging study.

| Study (year, journal) | Cohort size | Myopathy % | PDB % | FTD/dementia % | ALS % | Mean age at onset (overall and/or per feature) | Diagnostic delay | Respiratory involvement metrics | Wheelchair dependence metrics | Notable genotype-phenotype findings | DOI/URL |
|---|---:|---:|---:|---:|---:|---|---|---|---|---|---|
| Schiava et al. (2022, *J Neurol Neurosurg Psychiatry*) | 255 total; 234 symptomatic (+12 asymptomatic carriers reported in excerpt) | 90.7% initial symptom was muscle weakness (205/226); 50% had symmetric lower-limb weakness at onset | 28.2% (64/227) | Cognitive impairment 25.5% (59/231); FTD was most common cognitive pattern (33/59); FTD 14.3% also reported in cohort summary | NR | Mean age at assessment 56.8 ± 9.6 y; mean age at onset 45.6 ± 9.3 y; disease progression 11.3 ± 6.9 y; p.Arg155Cys onset 37.8 ± 7.6 y | 7.7 ± 6 y | Ventilatory insufficiency 40.3%; dyspnea on exertion 25.3% (56/221); nocturnal hypoventilation 15.6% (34/218); FVC <80% in 52.6% (61/116); FVC <50% risk factor for full-time wheelchair use; FVC <70% associated with death | 19.1% full-time wheelchair users; median time from onset to wheelchair 8.5 y | 57 variants, 18 novel; p.Arg155His most frequent (~28.6%); p.Arg155Cys associated with earlier onset and more axial/upper-limb weakness, scapular winging, cognitive impairment | 10.1136/jnnp-2022-328921; https://doi.org/10.1136/jnnp-2022-328921 (schiava2022genotype–phenotypecorrelationsin pages 3-4, schiava2022genotype–phenotypecorrelationsin pages 4-6) |
| Al-Obeidi et al. (2018, *Clinical Genetics*) | 231 total from 36 families; 187 symptomatic, 44 presymptomatic carriers | 89.8% of symptomatic (168/187); isolated myopathy in 36% | 42.4% (79 individuals) | ~29–30% dementia/FTD | ~8.6–9% | Myopathy mean onset 43 y (range 20–70); PDB mean onset 41.2 y (range 23–65); FTD mean onset 55.9 y (range 30–86) | NR | NR in snippet | NR | No clear overall genotype-phenotype correlation; R159C lacked PDB in this cohort and had later myopathy onset (~57 y); most mutations clustered in exon 5 (~83%) | 10.1111/cge.13095; https://doi.org/10.1111/cge.13095 (alobeidi2018genotype‐phenotypestudyin pages 5-7, alobeidi2018genotype‐phenotypestudyin pages 7-10, alobeidi2018genotype‐phenotypestudyin pages 1-5) |
| Shmara et al. (2023, *Neurology Genetics*) | 5 Hispanic families; 11 detailed patients + 28 additional affected extended-family members | 39% | 3% | 72% | 8% | IBM onset usually in 30s–40s; FTD typically 45–64 y but occurs earlier in VCP disease | Qualitative delay noted; no numeric value in excerpt | Respiratory and cardiac involvement can lead to death in 40s–60s | NR | p.R159H showed atypical phenotype with FTD particularly frequent in females and much lower PDB prevalence than historical cohorts | 10.1212/NXG.0000000000200037; https://doi.org/10.1212/nxg.0000000000200037 (shmara2023prevalenceoffrontotemporal pages 1-2) |
| Ikenaga et al. (2020, *Orphanet J Rare Dis*) | 59 registry participants (28 males, 31 females); 22 clinically evaluated at conference | 90% self-reported inclusion body myopathy | 29% | 14% dementia | 3% | NR | NR | Dyspnea on exertion 42%; dysphagia 22% | Functional impact: sit-to-stand difficulty 72%, walking 67%, stair climbing 85% | Registry captured broad phenotypic diversity; one patient reported parkinsonism | 10.1186/s13023-020-01551-0; https://doi.org/10.1186/s13023-020-01551-0 (ikenaga2020phenotypicdiversityin pages 1-2) |
| Columbres et al. (2024, *Scientific Reports*) | 12 VCP-MSP1 patients (6F/6M); 4 with known PDB+myopathy, 6 myopathy-only, 2 presymptomatic carriers | 50% myopathy-only at enrollment; 33% known myopathy+PDB | 33% known at visit; 2 additional occult PDB cases detected by bone scan (total imaging-detected PDB/ Paget-like lesions ≥50%) | NR | NR | NR | NR | Bone-scan screening study; no respiratory metrics reported | NR | Tc-99m bone scan identified 2 previously undiagnosed PDB cases; common uptake sites among PDB cases: thoracic spine/ribs 75%, pelvis 75%, shoulder 75%, calvarium 15% | 10.1038/s41598-024-54526-7; https://doi.org/10.1038/s41598-024-54526-7 (columbres2024bonescanfindings pages 1-2, columbres2024bonescanfindings pages 2-3, columbres2024bonescanfindings pages 3-4) |


*Table: This table compiles the main quantitative clinical and natural history metrics for VCP-associated multisystem proteinopathy across key cohort and registry studies. It is useful for comparing frequencies, onset, respiratory burden, disability progression, and variant-specific patterns across the best-supported evidence snippets.*

---

## Expert synthesis / analysis (evidence-grounded)

1) **Clinical heterogeneity is the rule**, not the exception: large datasets show a myopathy-predominant presentation with variable PDB and FTD penetrance and meaningful respiratory morbidity. (schiava2022genotype–phenotypecorrelationsin pages 3-4, schiava2022genotype–phenotypecorrelationsin pages 4-6)

2) **Respiratory function (FVC) is a major prognostic axis**: FVC thresholds were associated with disability (wheelchair use) and death in a large multicentre cohort, suggesting FVC is both clinically actionable and trial-relevant. (schiava2022genotype–phenotypecorrelationsin pages 3-4)

3) **The field is actively moving toward mechanism-informed therapy**:
   - A 2024 study links hyperactive ATPase to earlier onset, arguing for ATPase normalization strategies (often conceptualized as inhibition). (robinson2024elevatedvcpatpase pages 1-3)
   - Another 2024 study identifies nuclear proteostasis defects and demonstrates that **VCP activation** can promote nuclear TDP-43 aggregate clearance, supporting a complementary approach. (phan2024vcpactivatorreverses pages 1-2)

Together, these findings imply that “VCP modulation” likely requires **variant- and compartment-aware stratification** rather than a single-direction intervention.


References

1. (pontifex2024valosincontainingprotein(vcp) pages 1-2): Carly S. Pontifex, Mashiat Zaman, Roberto D. Fanganiello, Timothy E. Shutt, and Gerald Pfeffer. Valosin-containing protein (vcp): a review of its diverse molecular functions and clinical phenotypes. International Journal of Molecular Sciences, 25:5633, May 2024. URL: https://doi.org/10.3390/ijms25115633, doi:10.3390/ijms25115633. This article has 23 citations.

2. (shmara2023prevalenceoffrontotemporal pages 1-2): Alyaa Shmara, Liliane Gibbs, Ryan Patrick Mahoney, Kyle Hurth, Vanessa S. Goodwill, Alicia Cuber, Regina Im, Donald P. Pizzo, Jerry Brown, Christina Laukaitis, Shalini Mahajan, and Virginia Kimonis. Prevalence of frontotemporal dementia in females of 5 hispanic families with r159h vcp multisystem proteinopathy. Neurology Genetics, Feb 2023. URL: https://doi.org/10.1212/nxg.0000000000200037, doi:10.1212/nxg.0000000000200037. This article has 12 citations.

3. (schiava2022genotype–phenotypecorrelationsin pages 3-4): Marianela Schiava, Chiseko Ikenaga, Rocío Nur Villar-Quiles, Marta Caballero-Ávila, Ana Topf, Ichizo Nishino, Virginia Kimonis, Bjarne Udd, Benedikt Schoser, Edmar Zanoteli, Paulo Victor Sgobbi Souza, Giorgio Tasca, Thomas Lloyd, Adolfo Lopez-de Munain, Carmen Paradas, Elena Pegoraro, Aleksandra Nadaj-Pakleza, Jan De Bleecker, Umesh Badrising, Alicia Alonso-Jiménez, Anna Kostera-Pruszczyk, Francesc Miralles, Jin-Hong Shin, Jorge Alfredo Bevilacqua, Montse Olivé, Matthias Vorgerd, Rudi Kley, Stefen Brady, Timothy Williams, Cristina Domínguez-González, George K Papadimas, Jodi Warman-Chardon, Kristl G Claeys, Marianne de Visser, Nuria Muelas, Pascal LaForet, Edoardo Malfatti, Lindsay N Alfano, Sruthi S Nair, Georgios Manousakis, Hani A Kushlaf, Matthew B Harms, Christopher Nance, Alba Ramos-Fransi, Carmelo Rodolico, Channa Hewamadduma, Hakan Cetin, Jorge García-García, Endre Pál, Maria Elena Farrugia, Phillipa J Lamont, Colin Quinn, Velina Nedkova-Hristova, Stojan Peric, Sushan Luo, Anders Oldfors, Kate Taylor, Stuart Ralston, Tanya Stojkovic, Conrad Weihl, and Jordi Diaz-Manera. Genotype–phenotype correlations in valosin-containing protein disease: a retrospective muticentre study. Journal of Neurology, Neurosurgery &amp; Psychiatry, 93:1099-1111, Jul 2022. URL: https://doi.org/10.1136/jnnp-2022-328921, doi:10.1136/jnnp-2022-328921. This article has 44 citations.

4. (roy2023provisionalpracticerecommendation pages 1-2): Bhaskar Roy, Allison Peck, Teresinha Evangelista, Gerald Pfeffer, Leo Wang, Jordi Diaz‐Manera, Manisha Korb, Matthew P. Wicklund, Margherita Milone, Miriam Freimer, Hani Kushlaf, Rocio‐Nur Villar‐Quiles, Tanya Stojkovic, Merrilee Needham, Johanna Palmio, Thomas E. Lloyd, Benison Keung, Tahseen Mozaffar, Conrad Chris Weihl, and Virginia Kimonis. Provisional practice recommendation for the management of myopathy in vcp‐associated multisystem proteinopathy. Annals of Clinical and Translational Neurology, 10:686-695, Apr 2023. URL: https://doi.org/10.1002/acn3.51760, doi:10.1002/acn3.51760. This article has 8 citations and is from a peer-reviewed journal.

5. (iannibelli2023vcprelatedmyopathya pages 1-2): Eliana Iannibelli, S. Gibertini, M. Cheli, F. Blàsevich, Andrea Cavaliere, G. Riolo, A. Ruggieri, and L. Maggi. Vcp-related myopathy: a case series and a review of literature. Acta Myologica, 42:2-13, Mar 2023. URL: https://doi.org/10.36185/2532-1900-244, doi:10.36185/2532-1900-244. This article has 11 citations and is from a peer-reviewed journal.

6. (robinson2024elevatedvcpatpase pages 1-3): Sarah E. Robinson, Andrew R. Findlay, Shan Li, Feng Wang, Marianela Schiava, Jil Daw, Jordi Diaz-Manera, Tsui-Fen Chou, and Conrad C. Weihl. Elevated vcp atpase activity correlates with disease onset in multisystem proteinopathy-1. Neurology Genetics, Oct 2024. URL: https://doi.org/10.1212/nxg.0000000000200191, doi:10.1212/nxg.0000000000200191. This article has 7 citations.

7. (schiava2022genotype–phenotypecorrelationsin pages 4-6): Marianela Schiava, Chiseko Ikenaga, Rocío Nur Villar-Quiles, Marta Caballero-Ávila, Ana Topf, Ichizo Nishino, Virginia Kimonis, Bjarne Udd, Benedikt Schoser, Edmar Zanoteli, Paulo Victor Sgobbi Souza, Giorgio Tasca, Thomas Lloyd, Adolfo Lopez-de Munain, Carmen Paradas, Elena Pegoraro, Aleksandra Nadaj-Pakleza, Jan De Bleecker, Umesh Badrising, Alicia Alonso-Jiménez, Anna Kostera-Pruszczyk, Francesc Miralles, Jin-Hong Shin, Jorge Alfredo Bevilacqua, Montse Olivé, Matthias Vorgerd, Rudi Kley, Stefen Brady, Timothy Williams, Cristina Domínguez-González, George K Papadimas, Jodi Warman-Chardon, Kristl G Claeys, Marianne de Visser, Nuria Muelas, Pascal LaForet, Edoardo Malfatti, Lindsay N Alfano, Sruthi S Nair, Georgios Manousakis, Hani A Kushlaf, Matthew B Harms, Christopher Nance, Alba Ramos-Fransi, Carmelo Rodolico, Channa Hewamadduma, Hakan Cetin, Jorge García-García, Endre Pál, Maria Elena Farrugia, Phillipa J Lamont, Colin Quinn, Velina Nedkova-Hristova, Stojan Peric, Sushan Luo, Anders Oldfors, Kate Taylor, Stuart Ralston, Tanya Stojkovic, Conrad Weihl, and Jordi Diaz-Manera. Genotype–phenotype correlations in valosin-containing protein disease: a retrospective muticentre study. Journal of Neurology, Neurosurgery &amp; Psychiatry, 93:1099-1111, Jul 2022. URL: https://doi.org/10.1136/jnnp-2022-328921, doi:10.1136/jnnp-2022-328921. This article has 44 citations.

8. (alobeidi2018genotype‐phenotypestudyin pages 1-5): Ebaa Al-Obeidi, Sejad Al-Tahan, Abhilasha Surampalli, N. Goyal, Annabel K. Wang, Andreas Hermann, M. Omizo, Charles D. Smith, T. Mozaffar, and V. Kimonis. Genotype‐phenotype study in patients with valosin‐containing protein mutations associated with multisystem proteinopathy. Clinical Genetics, 93:119-125, Jan 2018. URL: https://doi.org/10.1111/cge.13095, doi:10.1111/cge.13095. This article has 159 citations and is from a peer-reviewed journal.

9. (ikenaga2020phenotypicdiversityin pages 1-2): Chiseko Ikenaga, Andrew R. Findlay, Michelle Seiffert, Allison Peck, Nathan Peck, Nicholas E. Johnson, Jeffrey M. Statland, and Conrad C. Weihl. Phenotypic diversity in an international cure vcp disease registry. Orphanet Journal of Rare Diseases, Sep 2020. URL: https://doi.org/10.1186/s13023-020-01551-0, doi:10.1186/s13023-020-01551-0. This article has 24 citations and is from a peer-reviewed journal.

10. (mahsom2023anautosomaldominantchildhoodonset pages 1-3): Annelise Y. Mah-Som, Jil Daw, Diana Huynh, Mengcheng Wu, Benjamin C. Creekmore, William Burns, Steven A. Skinner, Øystein L. Holla, Marie F. Smeland, Marc Planes, Kevin Uguen, Sylvia Redon, Tatjana Bierhals, Tasja Scholz, Jonas Denecke, Martin A. Mensah, Henrike L. Sczakiel, Heidelis Tichy, Sarah Verheyen, Jasmin Blatterer, Elisabeth Schreiner, Jenny Thies, Christina Lam, Christine G. Spaeth, Loren Pena, Keri Ramsey, Vinodh Narayanan, Laurie H. Seaver, Diana Rodriguez, Alexandra Afenjar, Lydie Burglen, Edward B. Lee, Tsui-Fen Chou, Conrad C. Weihl, and Marwan S. Shinawi. An autosomal-dominant childhood-onset disorder associated with pathogenic variants in vcp. The American Journal of Human Genetics, 110:1959-1975, Nov 2023. URL: https://doi.org/10.1016/j.ajhg.2023.10.007, doi:10.1016/j.ajhg.2023.10.007. This article has 8 citations.

11. (alobeidi2018genotype‐phenotypestudyin pages 5-7): Ebaa Al-Obeidi, Sejad Al-Tahan, Abhilasha Surampalli, N. Goyal, Annabel K. Wang, Andreas Hermann, M. Omizo, Charles D. Smith, T. Mozaffar, and V. Kimonis. Genotype‐phenotype study in patients with valosin‐containing protein mutations associated with multisystem proteinopathy. Clinical Genetics, 93:119-125, Jan 2018. URL: https://doi.org/10.1111/cge.13095, doi:10.1111/cge.13095. This article has 159 citations and is from a peer-reviewed journal.

12. (roy2023provisionalpracticerecommendation pages 5-7): Bhaskar Roy, Allison Peck, Teresinha Evangelista, Gerald Pfeffer, Leo Wang, Jordi Diaz‐Manera, Manisha Korb, Matthew P. Wicklund, Margherita Milone, Miriam Freimer, Hani Kushlaf, Rocio‐Nur Villar‐Quiles, Tanya Stojkovic, Merrilee Needham, Johanna Palmio, Thomas E. Lloyd, Benison Keung, Tahseen Mozaffar, Conrad Chris Weihl, and Virginia Kimonis. Provisional practice recommendation for the management of myopathy in vcp‐associated multisystem proteinopathy. Annals of Clinical and Translational Neurology, 10:686-695, Apr 2023. URL: https://doi.org/10.1002/acn3.51760, doi:10.1002/acn3.51760. This article has 8 citations and is from a peer-reviewed journal.

13. (alobeidi2018genotype‐phenotypestudyin pages 7-10): Ebaa Al-Obeidi, Sejad Al-Tahan, Abhilasha Surampalli, N. Goyal, Annabel K. Wang, Andreas Hermann, M. Omizo, Charles D. Smith, T. Mozaffar, and V. Kimonis. Genotype‐phenotype study in patients with valosin‐containing protein mutations associated with multisystem proteinopathy. Clinical Genetics, 93:119-125, Jan 2018. URL: https://doi.org/10.1111/cge.13095, doi:10.1111/cge.13095. This article has 159 citations and is from a peer-reviewed journal.

14. (schiava2023clinicalclassificationof pages 1-2): Marianela Schiava, Chiseko Ikenaga, Ana Topf, Marta Caballero-Ávila, Tsui-Fen Chou, Shan Li, Feng Wang, Jil Daw, Tanya Stojkovic, Rocio Villar-Quiles, Ichizo Nishino, Michio Inoue, Yukako Nishimori, Yoshihiko Saito, Masahisa Katsuno, Seiya Noda, Chihiro Ito, Mieko Otsuka, Sruthi Nahir, Georgios Manousakis, David Walk, Colin Quinn, Lindsay Alfano, Zarife Sahenk, Giorgio Tasca, Mauro Monforte, Mario Sabatelli, Giulia Bisogni, Anders Oldfors, Anna Rydeliu, Endre Pal, Carmen Paradas, Beatriz Velez, Jan L. De Bleecker, Maria Elena Farugia, Cheryl Longman, Matthew B. Harms, Stuart Ralston, Edmar Zanoteli, Andre Macedo Serafim da Silva, Javier Sotoca, Raul Juntas-Morales, Jorge Bevilacqua, Mireya Balart, Stuart Talbot, Volker Straub, Michela Guglieri, Chiara Marini-Bettolo, Jordi Diaz-Manera, and Conrad Chris Weihl. Clinical classification of variants in the valosin-containing protein gene associated with multisystem proteinopathy. Neurology Genetics, Oct 2023. URL: https://doi.org/10.1212/nxg.0000000000200093, doi:10.1212/nxg.0000000000200093. This article has 10 citations.

15. (schiava2023clinicalclassificationof pages 6-7): Marianela Schiava, Chiseko Ikenaga, Ana Topf, Marta Caballero-Ávila, Tsui-Fen Chou, Shan Li, Feng Wang, Jil Daw, Tanya Stojkovic, Rocio Villar-Quiles, Ichizo Nishino, Michio Inoue, Yukako Nishimori, Yoshihiko Saito, Masahisa Katsuno, Seiya Noda, Chihiro Ito, Mieko Otsuka, Sruthi Nahir, Georgios Manousakis, David Walk, Colin Quinn, Lindsay Alfano, Zarife Sahenk, Giorgio Tasca, Mauro Monforte, Mario Sabatelli, Giulia Bisogni, Anders Oldfors, Anna Rydeliu, Endre Pal, Carmen Paradas, Beatriz Velez, Jan L. De Bleecker, Maria Elena Farugia, Cheryl Longman, Matthew B. Harms, Stuart Ralston, Edmar Zanoteli, Andre Macedo Serafim da Silva, Javier Sotoca, Raul Juntas-Morales, Jorge Bevilacqua, Mireya Balart, Stuart Talbot, Volker Straub, Michela Guglieri, Chiara Marini-Bettolo, Jordi Diaz-Manera, and Conrad Chris Weihl. Clinical classification of variants in the valosin-containing protein gene associated with multisystem proteinopathy. Neurology Genetics, Oct 2023. URL: https://doi.org/10.1212/nxg.0000000000200093, doi:10.1212/nxg.0000000000200093. This article has 10 citations.

16. (robinson2024elevatedvcpatpase pages 3-4): Sarah E. Robinson, Andrew R. Findlay, Shan Li, Feng Wang, Marianela Schiava, Jil Daw, Jordi Diaz-Manera, Tsui-Fen Chou, and Conrad C. Weihl. Elevated vcp atpase activity correlates with disease onset in multisystem proteinopathy-1. Neurology Genetics, Oct 2024. URL: https://doi.org/10.1212/nxg.0000000000200191, doi:10.1212/nxg.0000000000200191. This article has 7 citations.

17. (robinson2024elevatedvcpatpase pages 4-5): Sarah E. Robinson, Andrew R. Findlay, Shan Li, Feng Wang, Marianela Schiava, Jil Daw, Jordi Diaz-Manera, Tsui-Fen Chou, and Conrad C. Weihl. Elevated vcp atpase activity correlates with disease onset in multisystem proteinopathy-1. Neurology Genetics, Oct 2024. URL: https://doi.org/10.1212/nxg.0000000000200191, doi:10.1212/nxg.0000000000200191. This article has 7 citations.

18. (mahsom2023anautosomaldominantchildhoodonset pages 12-13): Annelise Y. Mah-Som, Jil Daw, Diana Huynh, Mengcheng Wu, Benjamin C. Creekmore, William Burns, Steven A. Skinner, Øystein L. Holla, Marie F. Smeland, Marc Planes, Kevin Uguen, Sylvia Redon, Tatjana Bierhals, Tasja Scholz, Jonas Denecke, Martin A. Mensah, Henrike L. Sczakiel, Heidelis Tichy, Sarah Verheyen, Jasmin Blatterer, Elisabeth Schreiner, Jenny Thies, Christina Lam, Christine G. Spaeth, Loren Pena, Keri Ramsey, Vinodh Narayanan, Laurie H. Seaver, Diana Rodriguez, Alexandra Afenjar, Lydie Burglen, Edward B. Lee, Tsui-Fen Chou, Conrad C. Weihl, and Marwan S. Shinawi. An autosomal-dominant childhood-onset disorder associated with pathogenic variants in vcp. The American Journal of Human Genetics, 110:1959-1975, Nov 2023. URL: https://doi.org/10.1016/j.ajhg.2023.10.007, doi:10.1016/j.ajhg.2023.10.007. This article has 8 citations.

19. (phan2024vcpactivatorreverses pages 1-2): Jessica M. Phan, Benjamin C. Creekmore, Aivi T. Nguyen, Darya D. Bershadskaya, Nabil F. Darwich, Carolyn N. Mann, and Edward B. Lee. Vcp activator reverses nuclear proteostasis defects and enhances tdp-43 aggregate clearance in multisystem proteinopathy models. The Journal of Clinical Investigation, May 2024. URL: https://doi.org/10.1172/jci169039, doi:10.1172/jci169039. This article has 13 citations.

20. (phan2024vcpactivatorreverses pages 2-4): Jessica M. Phan, Benjamin C. Creekmore, Aivi T. Nguyen, Darya D. Bershadskaya, Nabil F. Darwich, Carolyn N. Mann, and Edward B. Lee. Vcp activator reverses nuclear proteostasis defects and enhances tdp-43 aggregate clearance in multisystem proteinopathy models. The Journal of Clinical Investigation, May 2024. URL: https://doi.org/10.1172/jci169039, doi:10.1172/jci169039. This article has 13 citations.

21. (phan2024vcpactivatorreverses pages 10-13): Jessica M. Phan, Benjamin C. Creekmore, Aivi T. Nguyen, Darya D. Bershadskaya, Nabil F. Darwich, Carolyn N. Mann, and Edward B. Lee. Vcp activator reverses nuclear proteostasis defects and enhances tdp-43 aggregate clearance in multisystem proteinopathy models. The Journal of Clinical Investigation, May 2024. URL: https://doi.org/10.1172/jci169039, doi:10.1172/jci169039. This article has 13 citations.

22. (columbres2024bonescanfindings pages 1-2): Rod Carlo Columbres, Sarosh Din, Liliane Gibbs, and Virginia Kimonis. Bone scan findings of paget’s disease of bone in patients with vcp multisystem proteinopathy 1. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-54526-7, doi:10.1038/s41598-024-54526-7. This article has 4 citations and is from a peer-reviewed journal.

23. (roy2023provisionalpracticerecommendation pages 2-3): Bhaskar Roy, Allison Peck, Teresinha Evangelista, Gerald Pfeffer, Leo Wang, Jordi Diaz‐Manera, Manisha Korb, Matthew P. Wicklund, Margherita Milone, Miriam Freimer, Hani Kushlaf, Rocio‐Nur Villar‐Quiles, Tanya Stojkovic, Merrilee Needham, Johanna Palmio, Thomas E. Lloyd, Benison Keung, Tahseen Mozaffar, Conrad Chris Weihl, and Virginia Kimonis. Provisional practice recommendation for the management of myopathy in vcp‐associated multisystem proteinopathy. Annals of Clinical and Translational Neurology, 10:686-695, Apr 2023. URL: https://doi.org/10.1002/acn3.51760, doi:10.1002/acn3.51760. This article has 8 citations and is from a peer-reviewed journal.

24. (roy2023provisionalpracticerecommendation pages 3-5): Bhaskar Roy, Allison Peck, Teresinha Evangelista, Gerald Pfeffer, Leo Wang, Jordi Diaz‐Manera, Manisha Korb, Matthew P. Wicklund, Margherita Milone, Miriam Freimer, Hani Kushlaf, Rocio‐Nur Villar‐Quiles, Tanya Stojkovic, Merrilee Needham, Johanna Palmio, Thomas E. Lloyd, Benison Keung, Tahseen Mozaffar, Conrad Chris Weihl, and Virginia Kimonis. Provisional practice recommendation for the management of myopathy in vcp‐associated multisystem proteinopathy. Annals of Clinical and Translational Neurology, 10:686-695, Apr 2023. URL: https://doi.org/10.1002/acn3.51760, doi:10.1002/acn3.51760. This article has 8 citations and is from a peer-reviewed journal.

25. (columbres2024bonescanfindings pages 8-9): Rod Carlo Columbres, Sarosh Din, Liliane Gibbs, and Virginia Kimonis. Bone scan findings of paget’s disease of bone in patients with vcp multisystem proteinopathy 1. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-54526-7, doi:10.1038/s41598-024-54526-7. This article has 4 citations and is from a peer-reviewed journal.

26. (columbres2024bonescanfindings pages 5-8): Rod Carlo Columbres, Sarosh Din, Liliane Gibbs, and Virginia Kimonis. Bone scan findings of paget’s disease of bone in patients with vcp multisystem proteinopathy 1. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-54526-7, doi:10.1038/s41598-024-54526-7. This article has 4 citations and is from a peer-reviewed journal.

27. (iannibelli2023vcprelatedmyopathya pages 10-10): Eliana Iannibelli, S. Gibertini, M. Cheli, F. Blàsevich, Andrea Cavaliere, G. Riolo, A. Ruggieri, and L. Maggi. Vcp-related myopathy: a case series and a review of literature. Acta Myologica, 42:2-13, Mar 2023. URL: https://doi.org/10.36185/2532-1900-244, doi:10.36185/2532-1900-244. This article has 11 citations and is from a peer-reviewed journal.

28. (NCT04823143 chunk 1): Lindsay Alfano. Natural History Study of Patients With VCP-related Disease. Nationwide Children's Hospital. 2021. ClinicalTrials.gov Identifier: NCT04823143

29. (NCT01353430 chunk 1): Virginia Kimonis. Characterization of Inclusion Body Myopathy Associated With Paget's Disease of Bone and Frontotemporal Dementia (IBMPFD). University of California, Irvine. 2007. ClinicalTrials.gov Identifier: NCT01353430

30. (columbres2024bonescanfindings pages 2-3): Rod Carlo Columbres, Sarosh Din, Liliane Gibbs, and Virginia Kimonis. Bone scan findings of paget’s disease of bone in patients with vcp multisystem proteinopathy 1. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-54526-7, doi:10.1038/s41598-024-54526-7. This article has 4 citations and is from a peer-reviewed journal.

31. (columbres2024bonescanfindings pages 3-4): Rod Carlo Columbres, Sarosh Din, Liliane Gibbs, and Virginia Kimonis. Bone scan findings of paget’s disease of bone in patients with vcp multisystem proteinopathy 1. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-54526-7, doi:10.1038/s41598-024-54526-7. This article has 4 citations and is from a peer-reviewed journal.
