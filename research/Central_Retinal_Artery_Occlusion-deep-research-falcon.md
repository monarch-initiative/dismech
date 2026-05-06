---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T07:58:09.778942'
end_time: '2026-05-06T08:19:25.767582'
duration_seconds: 1276.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Central Retinal Artery Occlusion
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 65
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Central Retinal Artery Occlusion
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Central Retinal Artery Occlusion** covering all of the
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
- **Disease Name:** Central Retinal Artery Occlusion
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Central Retinal Artery Occlusion** covering all of the
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


# Central Retinal Artery Occlusion (CRAO): Disease Characteristics Research Report

## Executive summary
Central retinal artery occlusion (CRAO) is an acute, usually painless, monocular vision-loss emergency caused by interruption of blood flow through the central retinal artery, producing ischemic injury to the inner retina and carrying substantial near-term risk for systemic vascular events (ischemic stroke, myocardial infarction). Contemporary expert consensus increasingly frames CRAO as “a stroke of the eye,” advocating urgent stroke-center evaluation and aggressive secondary prevention, while definitive, broadly endorsed acute vision-restoring therapy remains unproven and is under active clinical-trial evaluation. (chen2024centralretinalartery pages 1-2, chen2024centralretinalartery pages 4-4, fawzi2020retinalandophthalmic pages 15-17)

## Key quantitative highlights (2023–2024 prioritized)
| Topic | Key data/statistic | Study type/setting | Citation ID | Publication (year; journal) | URL |
|---|---|---|---|---|---|
| Incidence | 10,451 incident CRAO cases; weighted mean incidence 2.10 per 100,000 person-years (95% CI 2.06–2.14) | Nationwide population-based cohort, South Korea HIRA, 2011–2020 | (park2024incidenceratesof pages 2-4, park2024incidenceratesof pages 1-2) | Park et al. 2024; *BMC Ophthalmology* | https://doi.org/10.1186/s12886-024-03397-7 |
| Age/sex pattern | CRAO incidence rose with age, peaked at 80–85 years; male predominance overall (60.6% male; male:female incidence ratio ~1.54) | Nationwide population-based cohort, South Korea HIRA | (park2024incidenceratesof pages 2-4, park2024incidenceratesof pages 1-2, park2024incidenceratesof pages 8-10) | Park et al. 2024; *BMC Ophthalmology* | https://doi.org/10.1186/s12886-024-03397-7 |
| Visual prognosis | 61% of CRAO patients had vision of counting fingers or worse; another review reports most NA-CRAO patients present severely impaired and prognosis is generally poor | Review synthesis of CRAO literature | (chen2024centralretinalartery pages 1-2, tiwari2024areviewof pages 2-3) | Chen et al. 2024; *Eye*; Tiwari et al. 2024; *Cureus* | https://doi.org/10.1038/s41433-024-03029-w ; https://doi.org/10.7759/cureus.55814 |
| Stroke/MACCE risk | Acute cerebral ischemia on MRI reported in 30% of acute CRAO in one study summarized by review; pooled ischemic cerebrovascular disease incidence in CRAO 14.4% (95% CI 11.4–18.0); CRAO predicted MACCE with HR 2.321 (95% CI 1.439–3.744) | Narrative review; systematic review/meta-analysis; retrospective cohort | (liu2023progressincentral pages 1-3, pothikamjorn2025incidenceandrisk pages 4-5) | Liu et al. 2023; *J Int Med Res*; Pothikamjorn et al. 2025; *Scientific Reports* | https://doi.org/10.1177/03000605231198388 ; https://doi.org/10.1038/s41598-025-18419-7 |
| Thrombolysis outcomes | IVT median onset-to-treatment 158 min; ≥2 Snellen-line improvement 25%; 12.5% reached ≥20/100; symptomatic intracranial hemorrhage 1/13 (7.6%). IAT median onset-to-treatment 335 min; ≥2-line improvement 42% in one center. Meta-analysis of IAT: VA improvement 56% vs 32% controls (OR 3.55, 95% CI 1.74–7.24); benefit greater within 6 h (OR 4.60) than beyond 6 h (OR 3.36); 5 symptomatic ICH and 21 ischemic strokes/TIAs among 507 IAT patients | Single-center retrospective stroke-center cohort; systematic review/meta-analysis | (alhayek2024thrombolytictherapyfor pages 1-2, huang2023efficacyandsafety pages 1-3, huang2023efficacyandsafety pages 8-9) | Alhayek et al. 2024; *Neuro-Ophthalmology*; Huang et al. 2023; *Graefe's Arch Clin Exp Ophthalmol* | https://doi.org/10.1080/01658107.2023.2290536 ; https://doi.org/10.1007/s00417-022-05797-1 |
| Actionable acute treatment window | Practical reperfusion windows emphasized: IV thrombolysis generally considered when within 4.5 h; IAT evidence strongest within 6 h; complete reversal may be possible if reperfused within ~97 min and partial up to 240 min in experimental/clinical synthesis | Review/guideline-oriented synthesis and meta-analysis | (chen2024centralretinalartery pages 5-6, chen2024centralretinalartery pages 2-4, huang2023efficacyandsafety pages 1-3) | Chen et al. 2024; *Eye*; Huang et al. 2023; *Graefe's Arch Clin Exp Ophthalmol* | https://doi.org/10.1038/s41433-024-03029-w ; https://doi.org/10.1007/s00417-022-05797-1 |
| Ocular neovascularization | Ocular neovascularization prevalence 2.5–31.6%; mean onset 8.5 weeks after CRAO | Review synthesis | (chen2024centralretinalartery pages 5-6) | Chen et al. 2024; *Eye* | https://doi.org/10.1038/s41433-024-03029-w |
| Key diagnostic imaging frequencies | Fundus findings in CRAO: cherry-red spot 90%, posterior pole retinal opacity 58%, disc pallor 39%, retinal artery attenuation 32%, disc edema 22%, box-carring 19%, visible intra-arterial emboli ~20% | Review summarizing clinical/imaging studies | (chen2024centralretinalartery pages 2-4, tiwari2024areviewof pages 4-6) | Chen et al. 2024; *Eye*; Tiwari et al. 2024; *Cureus* | https://doi.org/10.1038/s41433-024-03029-w ; https://doi.org/10.7759/cureus.55814 |
| Actionable diagnostic workup | Immediate same-day ophthalmic + stroke-style workup recommended: carotid/vascular imaging, cardiac evaluation (echo/Holter), neuroimaging, lipids/HbA1c; in atypical/young cases add thrombophilia/vasculitis testing; in patients >50 urgently exclude GCA with ESR/CRP/FBC and start steroids if suspected | Narrative/review guidance based on guideline-oriented pathways | (chen2024centralretinalartery pages 4-4, daxer2024aetiologydiagnosisand pages 5-7, yu2024retinalarteryocclusion pages 2-4) | Chen et al. 2024; *Eye*; Daxer et al. 2024; *Medicina*; Yu et al. 2024; *J Ophthalmic Vis Res* | https://doi.org/10.1038/s41433-024-03029-w ; https://doi.org/10.3390/medicina60040526 ; https://doi.org/10.18502/jovr.v19i4.16559 |


*Table: This table compiles the most actionable quantitative findings for central retinal artery occlusion, including incidence, prognosis, vascular risk, treatment timing/effects, and diagnostic frequencies. It is useful as a compact evidence map for clinical and knowledge-base curation.*

## 1. Disease information

### 1.1 Concise overview (current understanding)
CRAO is an ophthalmic vascular occlusion characterized by partial or complete obstruction of the central retinal artery (CRA), resulting in acute retinal ischemia and profound vision loss. The American Academy of Ophthalmology (AAO) Preferred Practice Pattern defines CRAO as “partial/complete obstruction of the central retinal artery.” (fawzi2020retinalandophthalmic pages 8-10)

A 2024 clinical review explicitly frames the condition as analogous to brain stroke: “Central retinal artery occlusion (CRAO), like a stroke in the brain, is a critical eye condition that requiring urgent medical attention.” (chen2024centralretinalartery pages 1-2)

### 1.2 Key identifiers
- **ICD-10-CM (examples and laterality-specific codes):** The AAO Preferred Practice Pattern lists ICD-10-CM codes for retinal/ophthalmic artery occlusions, including laterality-coded CRAO entries (e.g., H34.11* series for central RAO depending on laterality) and related subtypes (arterial branch occlusion H34.231; partial retinal artery occlusion H34.211; transient retinal artery occlusion H34.01). (fawzi2020retinalandophthalmic pages 22-26)
- **ICD-10 (Korea HIRA claims study):** CRAO is captured as **H34.1** in a nationwide incidence study using administrative claims. (park2024incidenceratesof pages 1-2)
- **MeSH:** The AAO Preferred Practice Pattern describes its evidence searches using “retinal artery occlusion” as a MeSH major topic (e.g., “retinal artery occlusion”[MeSH Major Topic]). (fawzi2020retinalandophthalmic pages 22-26)
- **MONDO ID:** Not identified in the retrieved primary/secondary literature excerpts in this run; therefore not reportable with evidence-grade traceability here.

### 1.3 Synonyms and alternative names
- Central retinal artery occlusion (CRAO) (fawzi2020retinalandophthalmic pages 8-10)
- Retinal artery occlusion (RAO; umbrella term) (fawzi2020retinalandophthalmic pages 8-10, yu2024retinalarteryocclusion pages 1-2)
- “Stroke of the eye” / ocular analog of cerebral stroke (chen2024centralretinalartery pages 1-2, fawzi2020retinalandophthalmic pages 15-17)
- Historically/related term for transient monocular vision loss: “amaurosis fugax”; *The Lancet* review recommends “retinal TIA” terminology for transient events. (scott2020retinalvascularocclusions pages 3-4)

### 1.4 Evidence-source type
This report synthesizes:
- **Aggregated disease-level resources and guidelines** (AAO Preferred Practice Pattern; reviews) (fawzi2020retinalandophthalmic pages 13-15, chen2024centralretinalartery pages 1-2)
- **Population-level administrative claims epidemiology** (Korea HIRA incidence) (park2024incidenceratesof pages 2-4, park2024incidenceratesof pages 1-2)
- **Cohorts/meta-analyses** for systemic risk and treatment evidence (pothikamjorn2025incidenceandrisk pages 4-5, huang2023efficacyandsafety pages 1-3)
- **ClinicalTrials.gov registry records** for trials (NCT04526951 chunk 1, NCT04965038 chunk 1)

## 2. Etiology

### 2.1 Primary causal factors
CRAO is predominantly a thromboembolic phenomenon. The AAO PPP states central retinal artery occlusions are commonly embolic. (fawzi2020retinalandophthalmic pages 13-15)

A 2024 *Eye* review summarizes embolic/thrombotic occlusion as the most implicated mechanism and notes approximately **55%** of patients in one study had an identifiable embolic source. (chen2024centralretinalartery pages 2-4)

**Arteritic CRAO** is a distinct inflammatory entity, most often due to **giant cell arteritis (GCA)**, requiring urgent systemic therapy to prevent bilateral blindness and other ischemic complications. (daxer2024aetiologydiagnosisand pages 1-2, fawzi2020retinalandophthalmic pages 15-17)

### 2.2 Risk factors (2023–2024 evidence prioritized)
**Atherosclerotic and cardioembolic risk**
- Traditional vascular risk factors (advanced age, male sex, smoking, cardiovascular disease) overlap strongly with ischemic stroke/MI risk factors. (chen2024centralretinalartery pages 2-4)
- Carotid disease is a frequent source: among non-arteritic CRAO patients undergoing cervical vessel imaging, **71%** had an **ipsilateral carotid plaque** in one cohort summarized in a 2024 review. (yu2024retinalarteryocclusion pages 1-2)
- Severe carotid stenosis: one review cites **~18%** of CRAO patients having internal carotid stenosis >80% in a study. (tiwari2024areviewof pages 3-4)

**Atrial fibrillation and cardiac disease**
- A 2025 systematic review/meta-analysis of retinal artery occlusion (RAO) found atrial fibrillation associated with ischemic cerebrovascular disease after RAO (OR **1.32**, 95% CI 1.12–1.55). (pothikamjorn2025incidenceandrisk pages 4-5)
- Narrative review evidence also emphasizes atrial fibrillation and valvular disease as important embolic sources for CRAO. (daxer2024aetiologydiagnosisand pages 2-3)

**Hypercoagulable/hematologic and inflammatory disorders (selected examples)**
Recent reviews highlight CRAO associations with antiphospholipid syndrome and inherited thrombophilias as less common but relevant in younger/atypical cases. (tiwari2024areviewof pages 2-3, tiwari2024areviewof pages 4-6)
- Suggested gene-level entities (risk, not disease-causal for CRAO): **F5** (Factor V Leiden), **PROC**, **PROS1**.

**Inflammation and biomarker evidence (human cohort)**
A 2023 retrospective cohort reported CRAO patients had higher inflammatory markers (median NLR 2.18 vs 1.94; hs-CRP 1.20 vs 0.83 mg/L) and CRAO independently predicted MACCE (HR **2.321**, 95% CI 1.439–3.744). NLR (HR **1.275**) and hs-CRP (HR **1.021**) were also independent predictors. (chen2023sexdifferencesin pages 3-4, chen2023sexdifferencesin pages 2-3)

### 2.3 Protective factors
- **Cilioretinal artery presence** can preserve macular perfusion in some cases (“cilioretinal sparing”), improving the chance of retained central vision. Reported prevalence varies by series (e.g., 5–30% in one review; ~20–25% in another). (chen2024centralretinalartery pages 2-4, tiwari2024areviewof pages 2-3)

### 2.4 Gene–environment interactions
Direct CRAO-specific gene–environment interaction studies were not identified in the retrieved evidence. Clinically, inherited thrombophilia risk (e.g., Factor V Leiden) is typically considered in conjunction with acquired prothrombotic exposures (e.g., smoking, estrogen therapy, systemic inflammation) as part of individualized risk assessment. (chen2024centralretinalartery pages 4-4, tiwari2024areviewof pages 4-6)

## 3. Phenotypes (clinical presentation; HPO suggestions)

### 3.1 Core phenotypes
**Acute symptoms/signs**
- Sudden, painless monocular vision loss (often profound). (chen2024centralretinalartery pages 1-2, fawzi2020retinalandophthalmic pages 8-10)
- Relative afferent pupillary defect (RAPD). (daxer2024aetiologydiagnosisand pages 1-2, fawzi2020retinalandophthalmic pages 10-13)

**Fundus and imaging phenotypes (with frequencies from 2024 review)**
Fundus findings reported in CRAO include: cherry-red spot **90%**, posterior pole retinal opacity **58%**, disc pallor **39%**, retinal artery attenuation **32%**, disc edema **22%**, box-carring **19%**; intra-arterial emboli visible in **~20%**. (chen2024centralretinalartery pages 2-4)

**OCT/OCT-A phenotypes**
- Acute inner retinal hyperreflectivity and thickening evolving to inner retinal thinning/atrophy. (chen2024centralretinalartery pages 4-4, daxer2024aetiologydiagnosisand pages 5-7)
- Paracentral acute middle maculopathy (PAMM) in milder/early cases. (chen2024centralretinalartery pages 2-4)

### 3.2 Subtypes / clinical entities
- Non-arteritic CRAO (most common; typically embolic) vs arteritic CRAO (often GCA). (lakkis2025centralretinalartery pages 3-5, daxer2024aetiologydiagnosisand pages 1-2)
- Incomplete, subtotal, total CRAO classifications used clinically and in imaging-based classification schemes. (chen2024centralretinalartery pages 2-4)

### 3.3 Phenotype characteristics
- **Onset:** acute (seconds to minutes) (fawzi2020retinalandophthalmic pages 10-13)
- **Progression:** rapid ischemic injury; potential reperfusion but typically poor visual recovery (yu2024retinalarteryocclusion pages 1-2)
- **Lateralization:** typically unilateral; bilateral CRAO is uncommon (<2% noted in narrative review). (daxer2024aetiologydiagnosisand pages 2-3)

### 3.4 Quality of life impact
CRAO is associated with severe functional visual impairment (often ≤ counting fingers) and reduced quality of life, consistent with its characterization as catastrophic ophthalmic emergency. (liu2023progressincentral pages 1-3, tiwari2024areviewof pages 2-3)

### 3.5 Suggested HPO terms (non-exhaustive)
- **Sudden visual loss** (HP:0000529)
- **Monocular visual loss** (HP:0030680)
- **Scotoma** (HP:0000587) (central/centrocecal scotomas noted clinically) (chen2024centralretinalartery pages 2-4)
- **Relative afferent pupillary defect** (HP:0000611) (daxer2024aetiologydiagnosisand pages 1-2)
- **Cherry red spot of the macula** (HP:0001103) (daxer2024aetiologydiagnosisand pages 1-2, chen2024centralretinalartery pages 2-4)

## 4. Genetic / molecular information

### 4.1 Causal genes
CRAO is typically **not** a monogenic disorder. No CRAO-causal genes were identified in the retrieved clinical reviews/guidelines.

### 4.2 Pathogenic variants / susceptibility loci
No CRAO-specific pathogenic variants were identified in the retrieved evidence. Genetic testing is not standard for typical older atherosclerotic CRAO.

### 4.3 Modifier genes and molecular risk pathways (clinical relevance)
While CRAO is not genetic in the Mendelian sense, hypercoagulability evaluation in selected patients may involve heritable thrombophilia entities (e.g., Factor V Leiden) as clinical risk modifiers. (chen2024centralretinalartery pages 4-4, tiwari2024areviewof pages 4-6)

### 4.4 Epigenetics / omics
No CRAO-specific epigenomic, transcriptomic, proteomic, or metabolomic signatures were identified in the retrieved evidence. Reviews suggest RAO ocular proteomics remains under-studied. (scott2020retinalvascularocclusions pages 3-4)

## 5. Environmental information

### 5.1 Environmental and lifestyle contributors
Environmental/lifestyle factors align with vascular risk: smoking and cardiometabolic risk factors are repeatedly emphasized in CRAO risk profiles. (chen2024centralretinalartery pages 2-4, lakkis2025centralretinalartery pages 2-3)

### 5.2 Infectious agents
No specific infectious agents were identified as common CRAO triggers in the retrieved evidence; rare infective vegetations are described as uncommon embolic sources in narrative review. (daxer2024aetiologydiagnosisand pages 2-3)

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (trigger → tissue injury → phenotype)
1) **Upstream trigger:** embolus/thrombus (carotid/cardiac) or inflammatory luminal narrowing (GCA) occludes CRA. (chen2024centralretinalartery pages 2-4, daxer2024aetiologydiagnosisand pages 1-2)
2) **Immediate consequence:** abrupt hypoperfusion of inner retina (CRA supplies inner layers), with minimal collateralization at the arteriolar level. (yu2024retinalarteryocclusion pages 1-2, lakkis2025centralretinalartery pages 2-3)
3) **Cellular injury:** rapid ischemic damage; experimental and clinical syntheses emphasize extreme time sensitivity—full reversal may be possible if perfusion restored within ~97 minutes, with partial recovery up to 240 minutes in some summaries; other reviews cite very rapid irreversible injury in complete occlusion scenarios. (chen2024centralretinalartery pages 2-4)
4) **Clinical manifestation:** sudden profound vision loss; fundus whitening and cherry-red spot; OCT evidence of inner retinal edema then atrophy. (chen2024centralretinalartery pages 2-4, daxer2024aetiologydiagnosisand pages 5-7)
5) **Downstream sequelae:** retinal atrophy; in some patients, ocular neovascularization/neovascular glaucoma weeks later. (chen2024centralretinalartery pages 5-6, fawzi2020retinalandophthalmic pages 15-17)

### 6.2 Immune and inflammatory involvement
Inflammation is mechanistically central in arteritic CRAO (GCA) and may contribute to systemic risk, with inflammatory biomarkers (NLR, hs-CRP) predicting MACCE in a CRAO cohort. (chen2023sexdifferencesin pages 2-3, daxer2024aetiologydiagnosisand pages 1-2)

### 6.3 Suggested ontology mappings
**GO biological process (examples)**
- Response to hypoxia (GO:0001666)
- Neuron apoptotic process (GO:0051402)
- Inflammatory response (GO:0006954)
- Angiogenesis (GO:0001525) (for neovascular complications)

**Cell types (CL; examples)**
- Retinal ganglion cell (CL:0000740)
- Retinal endothelial cell (CL:0002395)
- Microglial cell (CL:0000129) (relevant to ischemia models)

## 7. Anatomical structures affected

### 7.1 Organ/tissue/cell targets
- **Primary organ:** eye/retina—inner retinal layers supplied by CRA. (yu2024retinalarteryocclusion pages 1-2)
- **Key structures:** central retinal artery; superficial and deep capillary plexuses (OCT-A flow reduction). (chen2024centralretinalartery pages 4-4)

**UBERON suggestions**
- Retina (UBERON:0000966)
- Central retinal artery (UBERON term exists; exact ID not retrieved in this run)
- Optic nerve head (UBERON:0000972)

### 7.2 Localization
Typically unilateral; bilateral cases are rare. (daxer2024aetiologydiagnosisand pages 2-3)

## 8. Temporal development

### 8.1 Onset
- Acute onset pattern, often sudden. (fawzi2020retinalandophthalmic pages 10-13)

### 8.2 Progression and stages
- Early phase: retinal edema/whitening; OCT inner retinal thickening and hyperreflectivity; sometimes PAMM in milder disease. (chen2024centralretinalartery pages 4-4, chen2024centralretinalartery pages 2-4)
- Chronic phase: inner retinal thinning/atrophy and optic atrophy; possible rubeosis/neovascular complications. (daxer2024aetiologydiagnosisand pages 5-7, fawzi2020retinalandophthalmic pages 15-17)

### 8.3 Critical periods
The therapeutic opportunity is time-limited and analogized to stroke reperfusion windows; multiple sources emphasize very early reperfusion as the key determinant for any chance of meaningful visual rescue. (huang2023efficacyandsafety pages 1-3, chen2024centralretinalartery pages 2-4)

## 9. Inheritance and population

### 9.1 Epidemiology
A 2024 nationwide South Korean claims study (HIRA) reported:
- **10,451** incident CRAO cases (2011–2020)
- Weighted mean CRAO incidence **2.10/100,000 person-years** (95% CI 2.06–2.14)
- Male predominance (60.6% male; male:female incidence ratio ~1.54)
- Incidence rises with age and peaks at ages **80–85 years** (park2024incidenceratesof pages 2-4, park2024incidenceratesof pages 1-2, park2024incidenceratesof pages 8-10)

A 2023 narrative review summarizes similar age-adjusted incidence estimates across countries (e.g., ~1.87–2.7 per 100,000 person-years all ages, markedly higher in >80 years). (liu2023progressincentral pages 1-3)

### 9.2 Demographics
Population-level evidence shows higher incidence in men and steep age gradient with older age groups at highest risk. (park2024incidenceratesof pages 2-4)

### 9.3 Genetic etiology and inheritance
CRAO is predominantly multifactorial (vascular) rather than inherited Mendelian disease.

## 10. Diagnostics

### 10.1 Clinical diagnosis
Diagnosis is based on acute clinical presentation plus fundus and multimodal imaging; early fundus may be subtle, so OCT/OCT-A can assist early detection. (yu2024retinalarteryocclusion pages 2-4, daxer2024aetiologydiagnosisand pages 5-7)

### 10.2 Imaging and functional tests
- **Fundus photography/exam:** cherry-red spot, retinal whitening, arterial attenuation, box-carring, visible embolus (minority). (chen2024centralretinalartery pages 2-4, yu2024retinalarteryocclusion pages 2-4)
- **OCT:** inner retinal hyperreflectivity/thickening acutely; thinning chronically. (daxer2024aetiologydiagnosisand pages 5-7, yu2024retinalarteryocclusion pages 2-4)
- **OCT-A:** reduced flow in superficial/deep plexuses; can quantify reduced vessel density and nonperfusion. (chen2024centralretinalartery pages 4-4, yu2024retinalarteryocclusion pages 4-5)
- **Fluorescein angiography (FFA):** delayed/absent arterial filling; used to classify incomplete/subtotal/total CRAO; helpful if diagnosis uncertain. (chen2024centralretinalartery pages 2-4, daxer2024aetiologydiagnosisand pages 5-7)
- **ERG:** preserved a-wave with reduced/absent b-wave in CRAO (inner retinal dysfunction). (daxer2024aetiologydiagnosisand pages 5-7)

### 10.3 Recommended systemic workup (real-world implementation)
Multiple reviews and the AAO PPP recommend urgent systemic evaluation similar to TIA/stroke pathways, including:
- Carotid/vascular imaging (duplex ultrasound) (chen2024centralretinalartery pages 4-4, daxer2024aetiologydiagnosisand pages 5-7)
- Cardiac evaluation (echocardiography; Holter for paroxysmal AF) (chen2024centralretinalartery pages 4-4, daxer2024aetiologydiagnosisand pages 5-7)
- Neuroimaging due to concurrent cerebral ischemia risk (chen2024centralretinalartery pages 4-4)
- Labs for vascular risk (lipids, HbA1c) and, in younger/atypical cases, hypercoagulability/vasculitis testing (protein C/S, factor V Leiden, antiphospholipid antibodies; ANA/ANCA, etc.). (chen2024centralretinalartery pages 4-4, daxer2024aetiologydiagnosisand pages 5-7)
- In patients >50 with suspected arteritis, urgent ESR/CRP/CBC and immediate corticosteroids when appropriate. (fawzi2020retinalandophthalmic pages 15-17, daxer2024aetiologydiagnosisand pages 5-7)

**Visual evidence (workup table and classification figure):** Chen et al. provide a classification figure and a “suggested history and investigations” table. (chen2024centralretinalartery media 966201bd, chen2024centralretinalartery media 2cd88d0e)

### 10.4 Differential diagnosis
Includes transient monocular visual loss (“retinal TIA”), ocular ischemic syndromes, retinal vein occlusion, optic neuropathies, and inflammatory arteritic ischemia (GCA). (scott2020retinalvascularocclusions pages 3-4, daxer2024aetiologydiagnosisand pages 5-7)

## 11. Outcome / prognosis

### 11.1 Visual outcome
Overall visual prognosis is poor. A 2024 review reports **61%** of CRAO patients have presenting vision of **counting fingers or worse**. (chen2024centralretinalartery pages 1-2)

### 11.2 Ocular complications
Ocular neovascularization risk is clinically important. One 2024 review reports prevalence **2.5–31.6%** with mean onset **8.5 weeks** after CRAO. (chen2024centralretinalartery pages 5-6)

### 11.3 Systemic vascular outcomes
CRAO is associated with increased risk of ischemic stroke and other vascular events.
- A 2025 RAO meta-analysis reported pooled ischemic cerebrovascular disease incidence in CRAO of **14.4%** (95% CI 11.4–18.0). (pothikamjorn2025incidenceandrisk pages 4-5)
- A 2023 CRAO cohort found MACCE incidence higher in CRAO vs controls (23.4% vs 9.9%), with CRAO independently predicting MACCE (HR 2.321). (chen2023sexdifferencesin pages 3-4)

## 12. Treatment

### 12.1 Acute treatments (evidence and expert analysis)
**No universally guideline-endorsed acute vision-restoring therapy**
Reviews repeatedly conclude evidence remains insufficient for a single optimal acute management plan. (chen2024centralretinalartery pages 5-6, yu2024retinalarteryocclusion pages 1-2)

**Conservative maneuvers (limited benefit)**
Common approaches include ocular massage and intraocular pressure lowering (acetazolamide, anterior chamber paracentesis), carbogen, vasodilators, etc., but reviews emphasize absence of convincing benefit over natural history in high-quality trials and an average improvement rate ~15–21% in retrospective series. (liu2023progressincentral pages 5-7, tiwari2024areviewof pages 6-7)

**Thrombolysis (active area; time-window dependent)**
- Intra-arterial thrombolysis meta-analysis (2023): VA improvement **56%** vs **32%** in controls (OR 3.55), with greater benefit within 6 hours (OR 4.60). Safety signals include symptomatic intracranial hemorrhage and ischemic stroke/TIA events. (huang2023efficacyandsafety pages 1-3, huang2023efficacyandsafety pages 8-9)
- Single-center stroke-center experience (2024): IVT used rarely (3.55%); ≥2-line improvement **25%** after IVT; symptomatic intracranial hemorrhage **1/13 (7.6%)**; no 3-month VA difference versus matched conservative controls. (alhayek2024thrombolytictherapyfor pages 1-2)

**Hyperbaric oxygen therapy (HBOT)**
Evidence is mixed: case series report logMAR improvements with complications (e.g., barotrauma), while a recent meta-analytic conclusion cited in a 2024 review is that HBOT “does not improve final visual outcomes” and carries risks. (liu2023progressincentral pages 5-7, chen2024centralretinalartery pages 5-6)

**Laser embolysis (Nd:YAG) and surgical approaches**
Nd:YAG embolysis may help selected patients with visible emboli, but applicability is limited and hemorrhagic complications occur; vitrectomy-based and endovascular/vitreoretinal approaches are emerging but lack robust comparative outcome data in the retrieved excerpts. (liu2023progressincentral pages 5-7, yu2024retinalarteryocclusion pages 10-12)

**Subacute ocular complication management**
Pan-retinal photocoagulation (PRP) ± intravitreal anti-VEGF is recommended for iris/retinal neovascularization per AAO PPP. (fawzi2020retinalandophthalmic pages 13-15)

### 12.2 Secondary prevention (real-world implementation)
Given stroke-equivalent framing, secondary prevention mirrors TIA/minor stroke practice in many pathways. A 2024 review states guidelines support early antiplatelet therapy (e.g., initial dual therapy for 21 days then long-term single agent, typically aspirin 81 mg). (chen2024centralretinalartery pages 5-6)

### 12.3 Clinical trials (ongoing/recent)
**TenCRAOS (NCT04526951)**
- Phase 3, randomized, double-blind, double-dummy; tenecteplase 0.25 mg/kg IV bolus vs aspirin 300 mg within **4.5 hours**.
- Primary outcome: proportion achieving ≤0.7 logMAR at 30 days.
- Outcomes include safety (intracranial hemorrhage, systemic bleeding) and QoL (NEI-VFQ-25; EQ-5D). (NCT04526951 chunk 1)

**REVISION (NCT04965038)**
- Phase 3, randomized, placebo-controlled, quadruple-masked; tenecteplase within **4.5 hours**; enrollment 422.
- Primary outcome: BCVA LogMAR ≤0.5 at 30 days.
- Secondary outcomes: OCTA/FFA perfusion, MRI ischemic lesions, NIHSS/mRS, hemorrhagic complications, mortality. (NCT04965038 chunk 1)

**Selective intra-arterial thrombolysis (NCT05562284)**
- Nonrandomized open-label; super-selective IAT with alteplase vs conservative (including HBOT); symptom duration ≤7 days.
- Primary outcome: Humphrey visual-field indices at 3 months. (NCT05562284 chunk 1)

### 12.4 MAXO suggestions (examples)
- Intravenous thrombolysis (MAXO term: thrombolytic therapy)
- Intra-arterial thrombolysis (MAXO: endovascular thrombolysis)
- Hyperbaric oxygen therapy (MAXO: hyperbaric oxygen therapy)
- Carotid ultrasonography (MAXO: diagnostic ultrasound)
- Dual antiplatelet therapy (MAXO: antiplatelet therapy)
- Pan-retinal photocoagulation (MAXO: photocoagulation therapy)

## 13. Prevention

### 13.1 Primary prevention
Primary prevention aligns with cardiovascular risk reduction (smoking cessation, blood pressure and lipid control, diabetes management) due to shared causal pathways with ischemic stroke. (chen2024centralretinalartery pages 2-4)

### 13.2 Secondary prevention
Urgent stroke-center evaluation and initiation of appropriate antithrombotic therapy and risk-factor management aim to prevent early recurrent ischemic events; AAO PPP emphasizes highest stroke risk in the first 1–4 weeks, especially first 7 days. (fawzi2020retinalandophthalmic pages 13-15, fawzi2020retinalandophthalmic pages 15-17)

### 13.3 Tertiary prevention
Monitoring and treating ocular neovascularization (PRP ± anti-VEGF) reduces risk of neovascular glaucoma. (fawzi2020retinalandophthalmic pages 13-15)

## 14. Other species / natural disease
No naturally occurring CRAO epidemiology in non-human species was identified in the retrieved evidence; the available evidence primarily concerns induced experimental models. 

## 15. Model organisms / experimental models
A 2019 comprehensive review summarizes **88 experiments across six species** (rodents most common; monkeys second) to model RAO/CRAO, with key conclusions:
- **Best anatomical similarity to humans:** nonhuman primates, then pigs. (vestergaard2019animalmodelsused pages 1-2)
- **Most common induction methods:** laser-induced occlusion and arterial ligation/clamping; other methods include raised intraocular pressure, vasoconstrictors, embolization, and endovascular techniques. (vestergaard2019animalmodelsused pages 1-2)
- **Major limitation:** most experimental occlusions last **30–90 minutes** and are followed by reperfusion, whereas human CRAO may be longer lasting; endovascular approaches may produce more permanent occlusion. (vestergaard2019animalmodelsused pages 1-2, vestergaard2019animalmodelsused pages 7-8)

These models are used to study ischemic retinal injury mechanisms, reperfusion biology, inflammatory responses, and candidate neuroprotective/reperfusion interventions, but careful validation and awareness of collateral damage/reperfusion are necessary for translational relevance. (vestergaard2019animalmodelsused pages 8-10)

## Expert opinions and authoritative-source synthesis (interpretation)
1) **Stroke-equivalent framing is now mainstream** in ophthalmology and neuro-ophthalmology: CRAO should be treated as acute retinal arterial ischemia requiring urgent systemic workup at a stroke center. (chen2024centralretinalartery pages 1-2, fawzi2020retinalandophthalmic pages 15-17)
2) **Evidence gap for acute vision rescue remains the main unmet need**: conservative maneuvers are not reliably effective; thrombolysis shows time-dependent signals but is limited by delays, heterogeneity, and safety concerns; multiple phase 3 trials are designed to address this. (huang2023efficacyandsafety pages 1-3, NCT04965038 chunk 1)
3) **Secondary prevention is actionable now**: early vascular evaluation and antithrombotic/risk-factor management are recommended to reduce early stroke risk and longer-term MACCE risk. (chen2024centralretinalartery pages 5-6, chen2023sexdifferencesin pages 3-4)

## URLs and publication dates (selected core sources)
- Chen C. et al. **2024-03**. *Eye*. “Central retinal artery occlusion: a stroke of the eye.” https://doi.org/10.1038/s41433-024-03029-w (chen2024centralretinalartery pages 1-2)
- Park S.H. et al. **2024-03**. *BMC Ophthalmology*. Korea nationwide incidence study. https://doi.org/10.1186/s12886-024-03397-7 (park2024incidenceratesof pages 2-4)
- Huang L. et al. **2023-08**. *Graefe’s Arch Clin Exp Ophthalmol*. IAT meta-analysis. https://doi.org/10.1007/s00417-022-05797-1 (huang2023efficacyandsafety pages 1-3)
- Alhayek N. et al. **2024-01**. *Neuro-Ophthalmology*. Stroke-center thrombolysis experience. https://doi.org/10.1080/01658107.2023.2290536 (alhayek2024thrombolytictherapyfor pages 1-2)
- AAO Preferred Practice Pattern. Fawzi A. et al. **2020-02**. *Ophthalmology*. https://doi.org/10.1016/j.ophtha.2019.09.028 (fawzi2020retinalandophthalmic pages 13-15)
- Chen T. et al. **2023-09**. *Scientific Reports*. MACCE risk and biomarkers. https://doi.org/10.1038/s41598-023-42247-2 (chen2023sexdifferencesin pages 3-4)
- TenCRAOS trial registry: ClinicalTrials.gov NCT04526951 (updated metadata shown in excerpt). https://clinicaltrials.gov/study/NCT04526951 (NCT04526951 chunk 1)
- REVISION trial registry: ClinicalTrials.gov NCT04965038. https://clinicaltrials.gov/study/NCT04965038 (NCT04965038 chunk 1)


References

1. (chen2024centralretinalartery pages 1-2): Celia Chen, Gurfarmaan Singh, Reema Madike, and Sudha Cugati. Central retinal artery occlusion: a stroke of the eye. Eye, 38:2319-2326, Mar 2024. URL: https://doi.org/10.1038/s41433-024-03029-w, doi:10.1038/s41433-024-03029-w. This article has 43 citations and is from a peer-reviewed journal.

2. (chen2024centralretinalartery pages 4-4): Celia Chen, Gurfarmaan Singh, Reema Madike, and Sudha Cugati. Central retinal artery occlusion: a stroke of the eye. Eye, 38:2319-2326, Mar 2024. URL: https://doi.org/10.1038/s41433-024-03029-w, doi:10.1038/s41433-024-03029-w. This article has 43 citations and is from a peer-reviewed journal.

3. (fawzi2020retinalandophthalmic pages 15-17): A. Fawzi, Steven T. Bailey, Jennifer I. Lim, Gui-shang Ying, Robert S. Feder, R. Chuck, Steven P. Dunn, C. Flaxel, S. Gedde, Francis S. Mah, Randall J. Olson, David K. Wallace, and D. Musch. Retinal and ophthalmic artery occlusions preferred practice pattern®. Ophthalmology, 127:P259-P287, Feb 2020. URL: https://doi.org/10.1016/j.ophtha.2019.09.028, doi:10.1016/j.ophtha.2019.09.028. This article has 170 citations and is from a highest quality peer-reviewed journal.

4. (park2024incidenceratesof pages 2-4): Shin Hyeong Park, Bum Jun Kim, Ji Hye Kim, Seung Chan Kim, Rock Bum Kim, and Yong Seop Han. Incidence rates of retinal vascular occlusive diseases from 2011 to 2020 in south korea: a nationwide cohort study. BMC Ophthalmology, Mar 2024. URL: https://doi.org/10.1186/s12886-024-03397-7, doi:10.1186/s12886-024-03397-7. This article has 10 citations and is from a peer-reviewed journal.

5. (park2024incidenceratesof pages 1-2): Shin Hyeong Park, Bum Jun Kim, Ji Hye Kim, Seung Chan Kim, Rock Bum Kim, and Yong Seop Han. Incidence rates of retinal vascular occlusive diseases from 2011 to 2020 in south korea: a nationwide cohort study. BMC Ophthalmology, Mar 2024. URL: https://doi.org/10.1186/s12886-024-03397-7, doi:10.1186/s12886-024-03397-7. This article has 10 citations and is from a peer-reviewed journal.

6. (park2024incidenceratesof pages 8-10): Shin Hyeong Park, Bum Jun Kim, Ji Hye Kim, Seung Chan Kim, Rock Bum Kim, and Yong Seop Han. Incidence rates of retinal vascular occlusive diseases from 2011 to 2020 in south korea: a nationwide cohort study. BMC Ophthalmology, Mar 2024. URL: https://doi.org/10.1186/s12886-024-03397-7, doi:10.1186/s12886-024-03397-7. This article has 10 citations and is from a peer-reviewed journal.

7. (tiwari2024areviewof pages 2-3): Varun Tiwari, Simerjeet Singh J Bagga, Roshan Prasad, and Swapneel Mathurkar. A review of current literature on central retinal artery occlusion: its pathogenesis, clinical management, and treatment. Cureus, Mar 2024. URL: https://doi.org/10.7759/cureus.55814, doi:10.7759/cureus.55814. This article has 12 citations.

8. (liu2023progressincentral pages 1-3): Weishai Liu, Dan Bai, and Lieling Kou. Progress in central retinal artery occlusion: a narrative review. The Journal of International Medical Research, Sep 2023. URL: https://doi.org/10.1177/03000605231198388, doi:10.1177/03000605231198388. This article has 23 citations.

9. (pothikamjorn2025incidenceandrisk pages 4-5): Thananop Pothikamjorn, Chutibhorn Charnnarong, Paweena Susantitaphong, and Supharat Jariyakosol. Incidence and risk factors associated with ischemic cerebrovascular disease in patients with retinal artery occlusion: a systematic review and meta-analysis. Scientific Reports, Sep 2025. URL: https://doi.org/10.1038/s41598-025-18419-7, doi:10.1038/s41598-025-18419-7. This article has 1 citations and is from a peer-reviewed journal.

10. (alhayek2024thrombolytictherapyfor pages 1-2): Nour Alhayek, Jacob M. Sobczak, Aimen Vanood, Cumara B. O’Carroll, Bart M. Demaerschalk, John Chen, and Oana M. Dumitrascu. Thrombolytic therapy for central retinal artery occlusion in an academic multi-site stroke centre. Neuro-Ophthalmology, 48:111-121, Jan 2024. URL: https://doi.org/10.1080/01658107.2023.2290536, doi:10.1080/01658107.2023.2290536. This article has 3 citations and is from a peer-reviewed journal.

11. (huang2023efficacyandsafety pages 1-3): Lele Huang, Yujie Wang, and Ruijun Zhang. Efficacy and safety of intra-arterial thrombolysis in patients with central retinal artery occlusion: a systematic review and meta-analysis. Graefe's Archive for Clinical and Experimental Ophthalmology, 261:103-113, Aug 2023. URL: https://doi.org/10.1007/s00417-022-05797-1, doi:10.1007/s00417-022-05797-1. This article has 20 citations.

12. (huang2023efficacyandsafety pages 8-9): Lele Huang, Yujie Wang, and Ruijun Zhang. Efficacy and safety of intra-arterial thrombolysis in patients with central retinal artery occlusion: a systematic review and meta-analysis. Graefe's Archive for Clinical and Experimental Ophthalmology, 261:103-113, Aug 2023. URL: https://doi.org/10.1007/s00417-022-05797-1, doi:10.1007/s00417-022-05797-1. This article has 20 citations.

13. (chen2024centralretinalartery pages 5-6): Celia Chen, Gurfarmaan Singh, Reema Madike, and Sudha Cugati. Central retinal artery occlusion: a stroke of the eye. Eye, 38:2319-2326, Mar 2024. URL: https://doi.org/10.1038/s41433-024-03029-w, doi:10.1038/s41433-024-03029-w. This article has 43 citations and is from a peer-reviewed journal.

14. (chen2024centralretinalartery pages 2-4): Celia Chen, Gurfarmaan Singh, Reema Madike, and Sudha Cugati. Central retinal artery occlusion: a stroke of the eye. Eye, 38:2319-2326, Mar 2024. URL: https://doi.org/10.1038/s41433-024-03029-w, doi:10.1038/s41433-024-03029-w. This article has 43 citations and is from a peer-reviewed journal.

15. (tiwari2024areviewof pages 4-6): Varun Tiwari, Simerjeet Singh J Bagga, Roshan Prasad, and Swapneel Mathurkar. A review of current literature on central retinal artery occlusion: its pathogenesis, clinical management, and treatment. Cureus, Mar 2024. URL: https://doi.org/10.7759/cureus.55814, doi:10.7759/cureus.55814. This article has 12 citations.

16. (daxer2024aetiologydiagnosisand pages 5-7): Barbara Daxer, Wolfgang Radner, Florian Fischer, Andreea-Liliana Cocoșilă, and Armin Ettl. Aetiology, diagnosis and treatment of arterial occlusions of the retina—a narrative review. Medicina, 60:526, Mar 2024. URL: https://doi.org/10.3390/medicina60040526, doi:10.3390/medicina60040526. This article has 12 citations.

17. (yu2024retinalarteryocclusion pages 2-4): Hannah J. Yu, Sophia Choi, Rodney Guiseppi, and Touka Banaee. Retinal artery occlusion: a review of current management practices. Journal of Ophthalmic and Vision Research, 19:488-507, Dec 2024. URL: https://doi.org/10.18502/jovr.v19i4.16559, doi:10.18502/jovr.v19i4.16559. This article has 7 citations and is from a peer-reviewed journal.

18. (fawzi2020retinalandophthalmic pages 8-10): A. Fawzi, Steven T. Bailey, Jennifer I. Lim, Gui-shang Ying, Robert S. Feder, R. Chuck, Steven P. Dunn, C. Flaxel, S. Gedde, Francis S. Mah, Randall J. Olson, David K. Wallace, and D. Musch. Retinal and ophthalmic artery occlusions preferred practice pattern®. Ophthalmology, 127:P259-P287, Feb 2020. URL: https://doi.org/10.1016/j.ophtha.2019.09.028, doi:10.1016/j.ophtha.2019.09.028. This article has 170 citations and is from a highest quality peer-reviewed journal.

19. (fawzi2020retinalandophthalmic pages 22-26): A. Fawzi, Steven T. Bailey, Jennifer I. Lim, Gui-shang Ying, Robert S. Feder, R. Chuck, Steven P. Dunn, C. Flaxel, S. Gedde, Francis S. Mah, Randall J. Olson, David K. Wallace, and D. Musch. Retinal and ophthalmic artery occlusions preferred practice pattern®. Ophthalmology, 127:P259-P287, Feb 2020. URL: https://doi.org/10.1016/j.ophtha.2019.09.028, doi:10.1016/j.ophtha.2019.09.028. This article has 170 citations and is from a highest quality peer-reviewed journal.

20. (yu2024retinalarteryocclusion pages 1-2): Hannah J. Yu, Sophia Choi, Rodney Guiseppi, and Touka Banaee. Retinal artery occlusion: a review of current management practices. Journal of Ophthalmic and Vision Research, 19:488-507, Dec 2024. URL: https://doi.org/10.18502/jovr.v19i4.16559, doi:10.18502/jovr.v19i4.16559. This article has 7 citations and is from a peer-reviewed journal.

21. (scott2020retinalvascularocclusions pages 3-4): Ingrid U Scott, Peter A Campochiaro, Nancy J Newman, and Valérie Biousse. Retinal vascular occlusions. The Lancet, 396:1927-1940, Dec 2020. URL: https://doi.org/10.1016/s0140-6736(20)31559-2, doi:10.1016/s0140-6736(20)31559-2. This article has 300 citations and is from a highest quality peer-reviewed journal.

22. (fawzi2020retinalandophthalmic pages 13-15): A. Fawzi, Steven T. Bailey, Jennifer I. Lim, Gui-shang Ying, Robert S. Feder, R. Chuck, Steven P. Dunn, C. Flaxel, S. Gedde, Francis S. Mah, Randall J. Olson, David K. Wallace, and D. Musch. Retinal and ophthalmic artery occlusions preferred practice pattern®. Ophthalmology, 127:P259-P287, Feb 2020. URL: https://doi.org/10.1016/j.ophtha.2019.09.028, doi:10.1016/j.ophtha.2019.09.028. This article has 170 citations and is from a highest quality peer-reviewed journal.

23. (NCT04526951 chunk 1): Anne Hege Aamodt. TENecteplase in Central Retinal Artery Occlusion Stuy (TenCRAOS). Oslo University Hospital. 2020. ClinicalTrials.gov Identifier: NCT04526951

24. (NCT04965038 chunk 1):  Early Reperfusion Therapy With Intravenous Thrombolysis for Recovery of VISION in Acute Central Retinal Artery Occlusion. University Hospital Tuebingen. 2022. ClinicalTrials.gov Identifier: NCT04965038

25. (daxer2024aetiologydiagnosisand pages 1-2): Barbara Daxer, Wolfgang Radner, Florian Fischer, Andreea-Liliana Cocoșilă, and Armin Ettl. Aetiology, diagnosis and treatment of arterial occlusions of the retina—a narrative review. Medicina, 60:526, Mar 2024. URL: https://doi.org/10.3390/medicina60040526, doi:10.3390/medicina60040526. This article has 12 citations.

26. (tiwari2024areviewof pages 3-4): Varun Tiwari, Simerjeet Singh J Bagga, Roshan Prasad, and Swapneel Mathurkar. A review of current literature on central retinal artery occlusion: its pathogenesis, clinical management, and treatment. Cureus, Mar 2024. URL: https://doi.org/10.7759/cureus.55814, doi:10.7759/cureus.55814. This article has 12 citations.

27. (daxer2024aetiologydiagnosisand pages 2-3): Barbara Daxer, Wolfgang Radner, Florian Fischer, Andreea-Liliana Cocoșilă, and Armin Ettl. Aetiology, diagnosis and treatment of arterial occlusions of the retina—a narrative review. Medicina, 60:526, Mar 2024. URL: https://doi.org/10.3390/medicina60040526, doi:10.3390/medicina60040526. This article has 12 citations.

28. (chen2023sexdifferencesin pages 3-4): Ting Chen, Yuedan Wang, Xuejie Li, Jiaqing Feng, Hongxia Yang, Ying Li, Hui Feng, and Xuan Xiao. Sex differences in major adverse cardiovascular and cerebrovascular event risk among central retinal artery occlusion patients. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42247-2, doi:10.1038/s41598-023-42247-2. This article has 9 citations and is from a peer-reviewed journal.

29. (chen2023sexdifferencesin pages 2-3): Ting Chen, Yuedan Wang, Xuejie Li, Jiaqing Feng, Hongxia Yang, Ying Li, Hui Feng, and Xuan Xiao. Sex differences in major adverse cardiovascular and cerebrovascular event risk among central retinal artery occlusion patients. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42247-2, doi:10.1038/s41598-023-42247-2. This article has 9 citations and is from a peer-reviewed journal.

30. (fawzi2020retinalandophthalmic pages 10-13): A. Fawzi, Steven T. Bailey, Jennifer I. Lim, Gui-shang Ying, Robert S. Feder, R. Chuck, Steven P. Dunn, C. Flaxel, S. Gedde, Francis S. Mah, Randall J. Olson, David K. Wallace, and D. Musch. Retinal and ophthalmic artery occlusions preferred practice pattern®. Ophthalmology, 127:P259-P287, Feb 2020. URL: https://doi.org/10.1016/j.ophtha.2019.09.028, doi:10.1016/j.ophtha.2019.09.028. This article has 170 citations and is from a highest quality peer-reviewed journal.

31. (lakkis2025centralretinalartery pages 3-5): Toufic Lakkis, Anas Mahmoud Awad Elshoura, Gabriel Andres Soria Behr, Mata Cardenas Eduardo Mauricio, Susana Sil-Zavaleta, Long Yin Cai, and Manju Rai. Central retinal artery occlusion in acute care: current practices and emerging therapies. Cureus, Sep 2025. URL: https://doi.org/10.7759/cureus.92786, doi:10.7759/cureus.92786. This article has 0 citations.

32. (lakkis2025centralretinalartery pages 2-3): Toufic Lakkis, Anas Mahmoud Awad Elshoura, Gabriel Andres Soria Behr, Mata Cardenas Eduardo Mauricio, Susana Sil-Zavaleta, Long Yin Cai, and Manju Rai. Central retinal artery occlusion in acute care: current practices and emerging therapies. Cureus, Sep 2025. URL: https://doi.org/10.7759/cureus.92786, doi:10.7759/cureus.92786. This article has 0 citations.

33. (yu2024retinalarteryocclusion pages 4-5): Hannah J. Yu, Sophia Choi, Rodney Guiseppi, and Touka Banaee. Retinal artery occlusion: a review of current management practices. Journal of Ophthalmic and Vision Research, 19:488-507, Dec 2024. URL: https://doi.org/10.18502/jovr.v19i4.16559, doi:10.18502/jovr.v19i4.16559. This article has 7 citations and is from a peer-reviewed journal.

34. (chen2024centralretinalartery media 966201bd): Celia Chen, Gurfarmaan Singh, Reema Madike, and Sudha Cugati. Central retinal artery occlusion: a stroke of the eye. Eye, 38:2319-2326, Mar 2024. URL: https://doi.org/10.1038/s41433-024-03029-w, doi:10.1038/s41433-024-03029-w. This article has 43 citations and is from a peer-reviewed journal.

35. (chen2024centralretinalartery media 2cd88d0e): Celia Chen, Gurfarmaan Singh, Reema Madike, and Sudha Cugati. Central retinal artery occlusion: a stroke of the eye. Eye, 38:2319-2326, Mar 2024. URL: https://doi.org/10.1038/s41433-024-03029-w, doi:10.1038/s41433-024-03029-w. This article has 43 citations and is from a peer-reviewed journal.

36. (liu2023progressincentral pages 5-7): Weishai Liu, Dan Bai, and Lieling Kou. Progress in central retinal artery occlusion: a narrative review. The Journal of International Medical Research, Sep 2023. URL: https://doi.org/10.1177/03000605231198388, doi:10.1177/03000605231198388. This article has 23 citations.

37. (tiwari2024areviewof pages 6-7): Varun Tiwari, Simerjeet Singh J Bagga, Roshan Prasad, and Swapneel Mathurkar. A review of current literature on central retinal artery occlusion: its pathogenesis, clinical management, and treatment. Cureus, Mar 2024. URL: https://doi.org/10.7759/cureus.55814, doi:10.7759/cureus.55814. This article has 12 citations.

38. (yu2024retinalarteryocclusion pages 10-12): Hannah J. Yu, Sophia Choi, Rodney Guiseppi, and Touka Banaee. Retinal artery occlusion: a review of current management practices. Journal of Ophthalmic and Vision Research, 19:488-507, Dec 2024. URL: https://doi.org/10.18502/jovr.v19i4.16559, doi:10.18502/jovr.v19i4.16559. This article has 7 citations and is from a peer-reviewed journal.

39. (NCT05562284 chunk 1): Ping Fei. Safety and Efficacy After Selective Intra-arterial Thrombolysis for Central Retinal Artery Occlusion. Xinhua Hospital, Shanghai Jiao Tong University School of Medicine. 2022. ClinicalTrials.gov Identifier: NCT05562284

40. (vestergaard2019animalmodelsused pages 1-2): Nanna Vestergaard, Lasse Jørgensen Cehofski, Bent Honoré, Kristian Aasbjerg, and Henrik Vorum. Animal models used to simulate retinal artery occlusion: a comprehensive review. Translational Vision Science &amp; Technology, 8:23, Aug 2019. URL: https://doi.org/10.1167/tvst.8.4.23, doi:10.1167/tvst.8.4.23. This article has 25 citations and is from a peer-reviewed journal.

41. (vestergaard2019animalmodelsused pages 7-8): Nanna Vestergaard, Lasse Jørgensen Cehofski, Bent Honoré, Kristian Aasbjerg, and Henrik Vorum. Animal models used to simulate retinal artery occlusion: a comprehensive review. Translational Vision Science &amp; Technology, 8:23, Aug 2019. URL: https://doi.org/10.1167/tvst.8.4.23, doi:10.1167/tvst.8.4.23. This article has 25 citations and is from a peer-reviewed journal.

42. (vestergaard2019animalmodelsused pages 8-10): Nanna Vestergaard, Lasse Jørgensen Cehofski, Bent Honoré, Kristian Aasbjerg, and Henrik Vorum. Animal models used to simulate retinal artery occlusion: a comprehensive review. Translational Vision Science &amp; Technology, 8:23, Aug 2019. URL: https://doi.org/10.1167/tvst.8.4.23, doi:10.1167/tvst.8.4.23. This article has 25 citations and is from a peer-reviewed journal.