---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T23:13:18.473445'
end_time: '2026-05-05T23:38:21.989151'
duration_seconds: 1503.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Carotid Artery Occlusion
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Carotid Artery Occlusion
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Carotid Artery Occlusion** covering all of the
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
- **Disease Name:** Carotid Artery Occlusion
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Carotid Artery Occlusion** covering all of the
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


# Carotid Artery Occlusion (CAO): Comprehensive Disease Characteristics Report

## Executive summary
Carotid artery occlusion (CAO)—most commonly occlusion of the extracranial internal carotid artery (ICA)—is typically the end stage of carotid atherosclerotic disease and can cause transient ischemic attack (TIA), ischemic stroke, ocular ischemic syndrome, or remain asymptomatic depending on collateral circulation. Contemporary research emphasizes (i) careful phenotyping of *acute vs non-acute/chronic* occlusions, (ii) improved patient selection using perfusion/hemodynamic markers, and (iii) a shift toward less invasive or hybrid revascularization strategies for selected symptomatic chronic/non-acute ICA occlusion, while optimized medical therapy remains foundational. (zhao2024significanceofatherosclerotic pages 1-2, ren2023recanalizationofchronic pages 8-9, NCT06303414 chunk 2)

## Evidence snapshot table (recent quantitative findings)
| Domain | Key metric (exact number) | Population/study | Year | PMID (if available; otherwise DOI) | URL |
|---|---|---|---|---|---|
| Epidemiology/Risk | Severe baseline asymptomatic carotid artery stenosis (ACAS) prevalence **6.3%**; **1,662/26,384** patients; **1,124 strokes** and **2,484 CVD events** over **~70,000 patient-years**; among PACAS score **≥14** (27.7% of cohort), severe ACAS prevalence **11.4%**, accounting for **56.6%** of incident strokes and **64.9%** of incident CVD events (poorthuis2024predictionofsevere pages 1-2) | REACH validation cohort, Poorthuis et al., *Stroke* | 2024 | DOI: 10.1161/STROKEAHA.123.046894 | https://doi.org/10.1161/strokeaha.123.046894 |
| Epidemiology/Risk | Early recurrence after neurologic index event: **6.4%** at **2–3 days**, **19.5%** at **7 days**, **26.1%** at **14 days**; pooled analysis **5,893** patients, **33,000 patient-years**; benefit greatest when revascularization performed within **2 weeks** (musialek2025strokeriskmanagement pages 28-29) | Symptomatic carotid stenosis, ESC consensus cited systematic review | 2025 | DOI: 10.1093/cvr/cvad135 | https://doi.org/10.1093/cvr/cvad135 |
| Imaging diagnostics | DUS vs CTA for extracranial ICA stenosis **50–94%**: **accuracy 69%**, **sensitivity 89%**, **specificity 63%**; for **70–94%**: **accuracy 84%**, **sensitivity 61%**, **specificity 93%**; CTA inter-observer variation **14%** vs DUS **3%** (daolio2024accuracyofduplex pages 1-2, daolio2024accuracyofduplex pages 4-6, daolio2024accuracyofduplex pages 2-4) | 45 patients, 84 arteries, Daolio et al. | 2024 | DOI: 10.1590/0100-6991e-20243632-en | https://doi.org/10.1590/0100-6991e-20243632-en |
| Imaging diagnostics | CTA meta-analysis for severe ICA stenosis (**70–99%**): **sensitivity 0.93** (95% CI 0.88–0.96), **specificity 0.99** (95% CI 0.96–1.00), **PLR 92.0**, **NLR 0.07**, **DOR 1302**, **AUC 0.98** (zeng2024systematicreviewand pages 1-2, zeng2024systematicreviewand pages 6-6) | 16 studies, **2,368 vascular segments**, Zeng et al. | 2024 | DOI: 10.1186/s12880-024-01390-6 | https://doi.org/10.1186/s12880-024-01390-6 |
| Imaging diagnostics | Color Doppler ultrasound vs DSA: **Kappa 0.823**, **sensitivity 97.67%**, **specificity 88.24%**, **accuracy 95.00%**; MRA vs DSA: **Kappa 0.657**, **sensitivity 97.30%**, **specificity 65.22%**, **accuracy 85.00%** (li2026comparativediagnosticvalue pages 1-2) | 120 patients, Li et al. | 2026 | DOI: 10.11152/mu-4590 | https://doi.org/10.11152/mu-4590 |
| Chronic ICA occlusion revascularization outcomes | Chronic long-segment ICA occlusion recanalization: **overall success 94.3% (82/87)**; endovascular-only **93.0% (40/43)**; hybrid **95.5% (42/44)**; type I **100%**, type II **87.8%**; favorable mRS 0–2 in **79.3%** overall; overall complications **6.9%**; re-occlusion **4.9%** overall, **0%** in type I vs **9.8–11.1%** in type II (ren2023recanalizationofchronic pages 1-2, ren2023recanalizationofchronic pages 7-8, ren2023recanalizationofchronic pages 3-5) | 87 patients, Ren et al., *Scientific Reports* | 2023 | DOI: 10.1038/s41598-023-44406-x | https://doi.org/10.1038/s41598-023-44406-x |
| Chronic ICA occlusion revascularization outcomes | Symptomatic non-acute long-segment ICA occlusion hybrid recanalization: **overall success 97.5% (158/162)**; proximal plaque **99.2% (119/120)**; distal plaque **92.9% (39/42)**; complications **4.2%** proximal and **4.8%** distal; re-occlusion **2.8%** proximal vs **13.3%** distal; medically treated annual ipsilateral ischemic stroke risk **3%**, rising to **10–20%** with severe hemodynamic compromise (zhao2024significanceofatherosclerotic pages 1-2) | 162 patients, Zhao et al., *Scientific Reports* | 2024 | DOI: 10.1038/s41598-024-61938-y | https://doi.org/10.1038/s41598-024-61938-y |
| CAS standards/complications | Recommended independently assessed in-hospital stroke/death risk after CAS: **≤4%** for symptomatic and **≤2%** for asymptomatic disease; 30-day rates should not exceed **6%** symptomatic and **3%** asymptomatic (spiliopoulos2024cirsestandardsof pages 9-10, spiliopoulos2024cirsestandardsof pages 10-11) | CIRSE Standards of Practice on CAS | 2024 | DOI: 10.1007/s00270-024-03707-y | https://doi.org/10.1007/s00270-024-03707-y |
| CAS standards/complications | Transcervical CAS systematic review: **technical success 96.3%**, open conversion **3.0%**, access complications **2.9%**, stroke **1.1–1.2%**, TIA **2.7%**, MI **0.14%**, death **0.41%**; transradial CAS registry: major access complications **0%** vs transfemoral **1.1%**, peri-procedural stroke/death **3.3%** vs **2.4%** (spiliopoulos2024cirsestandardsof pages 9-10) | CAS access-strategy studies summarized in CIRSE guideline | 2024 | DOI: 10.1007/s00270-024-03707-y | https://doi.org/10.1007/s00270-024-03707-y |
| Genetics/molecular | Shared CVD/CeVD/cIMT genetics: **11 colocalized loci**, **12 mapped genes** (**CASZ1, CDKN1A, TWIST1, CDKN2B, ABO, SWAP70, SH2B3, LRCH1, FES, GOSR2, RPRML, LDLR**); genetic correlation **rg ≈ 0.59**; MiXeR estimates **~1.5K** causal variants for CAD, **~1.0K** for atherosclerosis, with **~0.9K shared variants**; methylation signals implicated for **CASZ1** and **LRCH1** (ding2024identificationofshared pages 1-2, ding2024identificationofshared pages 14-15) | Ding et al., *Communications Biology* | 2024 | DOI: 10.1038/s42003-024-07417-6 | https://doi.org/10.1038/s42003-024-07417-6 |
| Genetics/molecular | Diabetes-GWAS markers and carotid plaque: **9 SNPs** associated (**rs4712524, rs1150777, rs10842993, rs2858980, rs9583907, rs1077476, rs7180016, rs4383154, rs9937354**); 9-GRS mean **9.19 ± 1.53** vs **8.62 ± 1.63**; OR per 1.0 increase in 9-GRS **1.30** (95% CI **1.18–1.44**, p=**4.7×10^-7**); 4-GRS mean **4.02 ± 0.81** vs **3.78 ± 0.92**; OR **1.47** (reported 95% CI **1.74–9.40**, p=**6.1×10^-5**) (wu2023associationsofgenetic pages 1-2) | 309 carotid plaque cases, 439 controls, Wu et al. | 2023 | DOI: 10.1186/s12933-023-01787-7 | https://doi.org/10.1186/s12933-023-01787-7 |


*Table: This table compiles the main quantitative findings identified across recent carotid occlusion/stenosis literature, spanning epidemiology, imaging accuracy, chronic ICA occlusion revascularization outcomes, carotid stenting standards, and genetics. It is useful as a compact evidence summary for a disease knowledge base entry.*

---

## 1. Disease Information
### 1.1 Definition and current understanding
**Carotid artery occlusion (CAO)** refers to near-complete or complete obstruction of a carotid artery lumen; in clinical cerebrovascular practice, this most often means **extracranial internal carotid artery occlusion (ICAO)**, sometimes including **common carotid artery (CCA) occlusion**. Definitions vary by imaging modality and clinical context:

* **Angiographic complete occlusion**: ClinicalTrials.gov protocols for symptomatic non-acute CAO define occlusion using **DSA confirmation with mTICI=0**, i.e., no antegrade perfusion through the occluded carotid segment. (NCT06303414 chunk 2)
* **“Non-acute” vs “chronic” occlusion** is operationalized differently across studies:
  * Non-acute ICA occlusion defined as **>7 days** in a hybrid-recanalization cohort. (zhao2024significanceofatherosclerotic pages 1-2)
  * Chronic ICA occlusion defined as **>3 weeks after imaging confirmation** in an endovascular/hybrid recanalization cohort. (ren2023recanalizationofchronic pages 8-9)
  * A clinical trial defines non-acute CAO as occlusion **≥24 hours**. (NCT06303414 chunk 2)

**Key concept:** Clinical consequences depend strongly on collateral flow (circle of Willis/external carotid pathways). Consensus sources note presentations range from asymptomatic to catastrophic depending on collateral capacity. (musialek2025strokeriskmanagement pages 15-16)

### 1.2 Key identifiers (ontologies/codes)
* **MeSH (from trial metadata):** ClinicalTrials.gov records include MeSH identifiers for related interventions/conditions (e.g., “Endarterectomy, Carotid” **D016894**; “Stroke” **D020521**; “Ischemic Attack, Transient” **D002546**; “Cerebral Infarction” **D002544**; “Cerebral Revascularization” **D002548**). (NCT06303414 chunk 2, NCT00029146 chunk 2)
* **MONDO / OMIM / Orphanet identifiers:** Not identified in the retrieved evidence set. This is expected because CAO is typically a phenotype within atherosclerotic or thromboembolic disease rather than a monogenic disorder. (zhao2024significanceofatherosclerotic pages 1-2, ren2023recanalizationofchronic pages 8-9)
* **ICD-10/ICD-11 codes:** Not present in the retrieved sources.

### 1.3 Synonyms / alternative names
Common terms used in recent literature:
* **Internal carotid artery occlusion (ICAO)** / **extracranial ICA occlusion** (zhang2025spontaneousrecanalizationof pages 1-3)
* **Chronic ICA occlusion**, **non-acute ICA occlusion**, **chronic long-segment ICA occlusion** (zhao2024significanceofatherosclerotic pages 1-2, ren2023recanalizationofchronic pages 8-9)
* **Carotid artery disease / carotid atherosclerotic disease** when CAO is treated as the end-stage of stenosis/plaque (musialek2025strokeriskmanagement pages 28-29)

### 1.4 Evidence source type
The evidence synthesized here is from **aggregated disease-level resources**: cohort studies, systematic reviews/meta-analyses, consensus statements, procedure standards, and ClinicalTrials.gov protocols—not individual EHR case extraction. (ren2023recanalizationofchronic pages 8-9, spiliopoulos2024cirsestandardsof pages 5-6, NCT06303414 chunk 2)

---

## 2. Etiology
### 2.1 Primary causal factors
**Atherosclerotic plaque progression with superimposed thrombosis** is the leading cause of extracranial ICA occlusion in older populations, and is conceptually an extreme on the carotid stenosis continuum. Mechanistically, plaques arise via endothelial dysfunction and inflammatory lipid accumulation with fibrous cap formation; advanced lesions can thrombose and occlude. (ismail2023carotidarterystenosis pages 8-10, ren2023recanalizationofchronic pages 8-9)

Non-atherosclerotic etiologies include **carotid dissection** and other less common arteriopathies (examples appear in related occlusion literature and trial inclusion allowing various etiologies). (zhang2025spontaneousrecanalizationof pages 1-3)

### 2.2 Risk factors (representative, evidence-based)
Risk factors align with systemic atherosclerosis and stroke prevention frameworks:
* **Hypertension and diabetes** are common comorbidities in chronic occlusion intervention cohorts (e.g., hypertension 75.7%, diabetes 31.1% reported in a chronic cerebral artery occlusion recanalization cohort that included ICA occlusion cases). (zhao2024significanceofatherosclerotic pages 1-2)
* **Smoking** is both a risk factor for carotid atherosclerotic progression and is a predictor in some recanalization success models; in one chronic occlusion cohort 36.9% had smoking history and smoking history was independently associated with recanalization success. (zhao2024significanceofatherosclerotic pages 1-2)

### 2.3 Protective factors
Direct protective factors specifically for CAO are not consistently quantified in the retrieved 2023–2024 CAO-focused evidence. However, guideline-consensus sources emphasize aggressive risk factor control and modern medical therapy to lower carotid-related stroke risk. (musialek2025strokeriskmanagement pages 57-58)

### 2.4 Gene–environment interactions
Direct gene×environment interaction studies for CAO were not captured in the retrieved set. Nonetheless, several genetic studies implicate pathways (BP regulation, lipid biology, inflammation) whose phenotypic expression is strongly modified by lifestyle and medical therapy, supporting a systems-level G×E view. (ding2024identificationofshared pages 1-2, wu2023associationsofgenetic pages 1-2)

---

## 3. Phenotypes
### 3.1 Core clinical phenotypes and suggested HPO terms
Below are common CAO-associated phenotypes; frequencies are variable and depend on collateral circulation and the presence of embolic sources.

1) **Ischemic stroke / cerebral infarction** (often carotid-territory)
* **Phenotype type:** clinical event
* **HPO:** *Cerebral infarction* (HP:0001344), *Ischemic stroke* (HP:0002140)
* **Notes:** Chronic ICA occlusion is associated with substantial recurrent ipsilateral stroke risk despite medical therapy in historical cohorts (6–20%/year cited) and procedure series cite this as rationale for intervention in selected cases. (ren2023recanalizationofchronic pages 1-2)

2) **Transient ischemic attack (TIA)** including hemodynamic presentations
* **Phenotype type:** symptom complex
* **HPO:** *Transient ischemic attack* (HP:0002326)
* **Special phenotype:** **limb-shaking TIA** is described as hemodynamic, related to carotid stenosis/occlusion and impaired perfusion. (musialek2025strokeriskmanagement pages 15-16)

3) **Ocular ischemic phenomena** (amaurosis fugax/ocular ischemic syndrome)
* **Phenotype type:** symptom/sign
* **HPO:** *Amaurosis fugax* (HP:0001105) (term usage may vary)
* **Notes:** Some carotid stenosis/occlusion cohorts emphasize retinal ischemia as a marker of symptomatic carotid disease. (daolio2024accuracyofduplex pages 2-4)

4) **Hemodynamic impairment / hypoperfusion**
* **Phenotype type:** imaging/physiology abnormality
* **HPO:** *Cerebral hypoperfusion* (closest HPO term may differ by ontology version)
* **Notes:** Non-acute CAO interventional trials require perfusion-confirmed hypoperfusion for enrollment. (NCT06303414 chunk 2)

### 3.2 Temporal phenotype features
* **Onset:** typically **adult/older adult** for atherosclerotic CAO; can be younger in dissection-related occlusion. (zhang2025spontaneousrecanalizationof pages 1-3)
* **Course:** can be **asymptomatic chronic** if collaterals are robust; otherwise **progressive/episodic** ischemic symptoms with hemodynamic instability. (musialek2025strokeriskmanagement pages 15-16)

### 3.3 Quality of life impact
Quality of life impact is driven by stroke disability and recurrent ischemia. Clinical trial outcomes for surgical bypass in symptomatic ICA occlusion include disability and stroke-specific QOL instruments (e.g., Rankin, Barthel, SS-QOL). (NCT00029146 chunk 2)

---

## 4. Genetic / Molecular Information
### 4.1 Causal genes
CAO is **not typically monogenic**; it is usually a downstream vascular phenotype of polygenic atherosclerosis risk, thrombosis risk, or arteriopathy (e.g., dissection, moyamoya-spectrum in selected populations).

### 4.2 Susceptibility loci / candidate genes (recent evidence)
**Shared cardiometabolic genetics relevant to carotid atherosclerosis (proxy: cIMT):** A 2024 multi-trait genetic study identified **11 colocalized loci** mapped to **CASZ1, CDKN1A, TWIST1, CDKN2B, ABO, SWAP70, SH2B3, LRCH1, FES, GOSR2, RPRML, LDLR**, and suggested **methylation of CASZ1 and LRCH1** as potentially causal mediators. Quantitative overlap estimates reported high genetic sharing (rg ≈ 0.59; ~0.9K shared causal variants). (ding2024identificationofshared pages 1-2, ding2024identificationofshared pages 14-15)

**Diabetes-GWAS markers linked to carotid plaque:** A 2023 community-based case–control analysis associated 9 diabetes GWAS SNPs with carotid plaque and reported polygenic risk score odds ratios (e.g., OR 1.30 per 1.0 increase in 9-locus GRS). (wu2023associationsofgenetic pages 1-2)

**Endothelial/plaque biology candidates and epigenetic mechanisms (systematic review):** Endothelial genetics/transcriptomics evidence emphasizes matrix remodeling and plaque progression pathways with candidates including **MMP1** and **ADAM9/15/17**, and highlights flow/shear-stress–driven epigenetic regulation (DNA methylation, chromatin remodeling) and histone deacetylase biology (HDAC9). (richter2025endothelialcellgenetics pages 6-7, richter2025endothelialcellgenetics pages 14-15)

### 4.3 Epigenetics
Epigenetic regulation is implicated at two levels in the retrieved evidence:
* Genetic multi-omics analyses suggesting methylation-mediated pleiotropy (CASZ1, LRCH1). (ding2024identificationofshared pages 1-2, ding2024identificationofshared pages 14-15)
* Endothelial shear-stress–induced epigenetic changes (flow-dependent methylation and chromatin remodeling) in atherosclerosis biology. (richter2025endothelialcellgenetics pages 14-15)

### 4.4 Model organism genetics
Mouse vascular integrity genes (e.g., **COL4A1**) appear in broader cerebrovascular atherosclerosis genetics reviews but were not directly tied to CAO as a discrete phenotype in the retrieved set. (richter2025endothelialcellgenetics pages 11-12)

---

## 5. Environmental Information
### 5.1 Lifestyle and environmental factors
The disease is tightly linked to modifiable atherosclerosis risk factors (smoking, diet, activity) and metabolic disease burden. Intervention cohorts and reviews highlight smoking and cardiometabolic comorbidities as common features. (zhao2024significanceofatherosclerotic pages 1-2, ismail2023carotidarterystenosis pages 8-10)

### 5.2 Infectious agents
No infectious causal triggers were identified in the retrieved evidence set for CAO.

---

## 6. Mechanism / Pathophysiology
### 6.1 Causal chain (upstream → downstream)
1. **Upstream triggers:** dyslipidemia, hypertension, diabetes, smoking → endothelial dysfunction and inflammation. (ismail2023carotidarterystenosis pages 8-10)
2. **Plaque formation and remodeling:** lipid deposition, inflammatory infiltration, extracellular matrix remodeling (MMP/ADAM family), fibrous cap changes → plaque growth and vulnerability. (richter2025endothelialcellgenetics pages 6-7, richter2025endothelialcellgenetics pages 14-15)
3. **Occlusion event:** plaque rupture/erosion and thrombosis or progressive luminal compromise → complete ICA/CCA occlusion. (ren2023recanalizationofchronic pages 8-9)
4. **Downstream ischemia mechanisms:**
   * **Embolic:** artery-to-artery embolism from carotid plaque/thrombus. (musialek2025strokeriskmanagement pages 50-51)
   * **Hemodynamic:** reduced perfusion pressure with inadequate collaterals → hypoperfusion symptoms (e.g., limb-shaking TIA) and watershed infarcts. (musialek2025strokeriskmanagement pages 15-16, NCT06303414 chunk 2)

### 6.2 Cell types (suggested CL terms)
Key involved cell types (by current atherosclerosis biology and retrieved endothelial-focused evidence):
* **Endothelial cell** (CL:0000115) (richter2025endothelialcellgenetics pages 1-2)
* **Vascular smooth muscle cell** (CL:0000192) (implicated by vascular remodeling and gene expression enrichment) (ding2024identificationofshared pages 1-2)
* **Macrophage** (CL:0000235) (ADAM genes upregulated in advanced plaques) (richter2025endothelialcellgenetics pages 14-15)

### 6.3 Suggested GO biological process terms
* **Inflammatory response** (GO:0006954) (richter2025endothelialcellgenetics pages 6-7)
* **Extracellular matrix organization / collagen catabolic process** (e.g., GO:0030198 / GO:0030574) (richter2025endothelialcellgenetics pages 6-7)
* **Response to shear stress / blood flow** (GO:0034616) (richter2025endothelialcellgenetics pages 14-15)

### 6.4 Recent mechanistic developments (2023–2024 emphasis)
* Increasing emphasis on **lesion morphology/location** and recanalization feasibility in chronic/non-acute ICA occlusion, with location-based classification affecting success and re-occlusion risk. (zhao2024significanceofatherosclerotic pages 1-2, ren2023recanalizationofchronic pages 8-9)
* Multi-omics genetics continues to connect carotid intermediate phenotypes (cIMT, plaque) to shared cardiometabolic pathways (BP/lipid biology). (ding2024identificationofshared pages 1-2)

---

## 7. Anatomical Structures Affected
### 7.1 Organ/tissue level (UBERON suggestions)
* **Internal carotid artery** (UBERON:0000945)
* **Common carotid artery** (UBERON:0001456)
* **Brain (ischemic territories)** (UBERON:0000955)
* **Retina/ocular circulation** in ocular ischemic presentations (UBERON:0000966)

### 7.2 Localization and laterality
* Often **unilateral** ICA occlusion; bilateral disease occurs and is clinically high risk. (NCT00029146 chunk 2)
* Long-segment occlusion descriptions use Bouthillier ICA segments (C1–C7) for localization. (zhao2024significanceofatherosclerotic pages 1-2)

---

## 8. Temporal Development
### 8.1 Onset patterns
* **Acute** ICA occlusion may present as large vessel occlusion stroke.
* **Non-acute/chronic** occlusions may present with recurrent TIAs or progressive symptoms, or be incidentally discovered.

Operational definitions in recent chronic/non-acute cohorts: **>7 days** (non-acute) and **>3 weeks** (chronic). (zhao2024significanceofatherosclerotic pages 1-2, ren2023recanalizationofchronic pages 8-9)

### 8.2 Progression and staging
In practice, clinicians distinguish:
* severe stenosis → near-occlusion → occlusion;
* acute thrombotic occlusion vs chronic organized occlusion (recanalization feasibility differs).

---

## 9. Inheritance and Population
### 9.1 Epidemiology (available from retrieved evidence)
Direct population incidence/prevalence of *ICA occlusion* was not captured in the retrieved 2023–2024 primary epidemiology set. However, related high-quality epidemiology for severe asymptomatic carotid stenosis (a major precursor phenotype) is available:
* Severe baseline ACAS prevalence **6.3%** in 26,384 patients (REACH registry validation), with risk concentrated in high PACAS score strata. (poorthuis2024predictionofsevere pages 1-2)

CAO/ICAO recurrence risk under medical therapy is often cited from historical cohorts:
* Annual ipsilateral stroke risk **~3%** in medically treated chronic CAO, increasing to **10–20%** with severe hemodynamic compromise (cited in a 2024 intervention series). (zhao2024significanceofatherosclerotic pages 1-2)

### 9.2 Genetic architecture
The genetic architecture is **polygenic/multifactorial**. Recent multi-trait analyses suggest thousands of causal variants for related atherosclerosis phenotypes and substantial sharing with CAD. (ding2024identificationofshared pages 1-2)

---

## 10. Diagnostics
### 10.1 Imaging-based diagnosis (core modalities)
* **Duplex ultrasound (DUS):** commonly first-line; accuracy varies by stenosis threshold.
  * Example 2024 tertiary-center accuracy study vs CTA reference: accuracy **69%** (50–94% stenosis) and **84%** (70–94% stenosis). (daolio2024accuracyofduplex pages 1-2)
* **CTA:** high accuracy for severe stenosis vs DSA in a 2024 meta-analysis (sensitivity **0.93**, specificity **0.99**, AUC **0.98**). (zeng2024systematicreviewand pages 1-2)
* **MRA:** may overestimate mild stenosis; 2026 study reports moderate agreement with DSA (Kappa **0.657**). (li2026comparativediagnosticvalue pages 1-2)
* **DSA:** invasive reference standard; used for procedural planning and trial enrollment confirmation. (NCT06303414 chunk 2)

**Measurement caveat:** Consensus sources stress that stenosis severity can be center- and modality-dependent; one cited comparison indicates that with DUS, “**1 out of 6 arteries would be reclassified by CTA**.” (musialek2025strokeriskmanagement pages 18-19)

### 10.2 Hemodynamic/perfusion assessment
For symptomatic non-acute CAO intervention selection, protocols require perfusion evidence of hypoperfusion and exclude large new infarcts on MRI DWI/ADC. (NCT06303414 chunk 2)

### 10.3 Differential diagnosis
* Dissection-related occlusion
* Intracranial occlusion patterns (tandem lesions)
* Moyamoya-spectrum disease (RNF213-associated in East Asian ancestry contexts)

---

## 11. Outcome / Prognosis
### 11.1 Natural history (selected quantified estimates)
Chronic ICA occlusion is cited as carrying substantial recurrent stroke risk despite medical therapy:
* Yearly ipsilateral recurrent stroke risk **6–20%** is cited in a 2023 chronic ICA occlusion series as background rationale. (ren2023recanalizationofchronic pages 1-2)

### 11.2 Prognostic modifiers
* **Collateral circulation** adequacy (circle of Willis/external carotid pathways) strongly influences symptom severity and outcome. (musialek2025strokeriskmanagement pages 15-16)
* **Occlusion anatomy/location** predicts technical success and re-occlusion after recanalization (type I vs type II; proximal vs distal plaque). (zhao2024significanceofatherosclerotic pages 1-2, ren2023recanalizationofchronic pages 1-2)

---

## 12. Treatment
### 12.1 Medical therapy (baseline for all patients)
Modern carotid consensus emphasizes aggressive risk factor management (“goal-directed triple medical therapy” plus lifestyle modification), recognizing residual stroke risk remains in selected high-risk patients. (musialek2025strokeriskmanagement pages 57-58)

### 12.2 Surgical/interventional treatments
#### A) Carotid endarterectomy (CEA) and carotid artery stenting (CAS) for stenosis (precursor/related disease)
A 2023 review summarizes that guidelines recommend revascularization in symptomatic stenosis >50% and note comparative trial evidence between CEA and CAS with similar long-term ipsilateral stroke rates but different periprocedural risks; selected numeric trial outcomes are reported (e.g., NASCET perioperative stroke/death 6.5%). (ismail2023carotidarterystenosis pages 8-10)

**CIRSE 2024 CAS SOP (practice standards):**
* Recommends structured procedural technique and embolic protection usage.
* Provides quality thresholds (from ESO expert consensus) suggesting in-hospital stroke/death risk after CAS should not exceed **4% symptomatic** and **2% asymptomatic**, with 30-day rates ≤6% and ≤3% respectively. (spiliopoulos2024cirsestandardsof pages 9-10)

The SOP’s indications/contraindications are captured in the retrieved cropped guideline text images. (spiliopoulos2024cirsestandardsof media 6e47be29, spiliopoulos2024cirsestandardsof media 55399623)

#### B) Revascularization/recanalization for chronic/non-acute ICA occlusion (CAO-specific)
**Hybrid or endovascular recanalization** is increasingly reported in selected symptomatic chronic/non-acute long-segment ICA occlusion cohorts:
* 2023 cohort: overall success **94.3% (82/87)**; complications **6.9%**; re-occlusion **4.9%**. (ren2023recanalizationofchronic pages 3-5)
* 2024 cohort: overall success **97.5% (158/162)**; low reported periprocedural complications (~4–5%); re-occlusion differed by plaque location (2.8% vs 13.3%). (zhao2024significanceofatherosclerotic pages 1-2)

**MAXO suggestions (interventions):**
* Carotid endarterectomy (MAXO:??)
* Carotid artery stenting / endovascular recanalization (MAXO:??)
* Extracranial–intracranial bypass (MAXO:??)

(Exact MAXO IDs were not available in retrieved sources and would require ontology lookup.)

### 12.3 Clinical trials (CAO-specific; ClinicalTrials.gov)
* **NCT03179774 (ERCAO trial; National Taiwan University Hospital)**: rater-blinded RCT of endovascular revascularization + OMT vs OMT alone for chronic CAO; primary endpoints include neurocognitive measures (ADAS-Cog, MMSE, etc.) with safety endpoints including death/ipsilateral stroke within 30 days and up to 1 year. (NCT03179774 chunk 1)
* **NCT06303414 (Xuanwu Hospital, Beijing)**: observational trial of revascularization for symptomatic non-acute CAO; requires DSA-confirmed mTICI=0 occlusion and perfusion-confirmed hypoperfusion; tracks technical success, stroke/death, cranial nerve injury, and re-occlusion (>99%) through 12 months. (NCT06303414 chunk 2)
* **NCT00029146 (COSS)**: EC–IC bypass trial framework for symptomatic ICA occlusion with hemodynamic compromise; includes disability/QOL endpoints at 2 years (Rankin, Barthel, SS-QOL). (NCT00029146 chunk 2)

---

## 13. Prevention
### 13.1 Primary prevention
Risk-factor modification to prevent carotid atherosclerosis progression (BP control, diabetes management, smoking cessation) is central; evidence is consistent with broader stroke prevention consensus emphasizing medical therapy uptake and lifestyle modification. (musialek2025strokeriskmanagement pages 57-58)

### 13.2 Secondary prevention
Selective screening for severe asymptomatic stenosis may be guided by risk models; a 2024 validation study suggests high PACAS risk groups concentrate stroke/CVD events and may support targeted screening strategies. (poorthuis2024predictionofsevere pages 1-2)

### 13.3 Tertiary prevention
In established symptomatic disease, timely revascularization for stenosis can reduce recurrent stroke risk, and selected chronic occlusion patients may be considered for recanalization trials or specialized interventions. (musialek2025strokeriskmanagement pages 28-29, NCT03179774 chunk 1)

---

## 14. Other species / natural disease
Non-human naturally occurring ICA occlusion is reported in veterinary anatomical studies (e.g., Japanese Black cattle ICA occlusion/closure patterns), but this is not a translational disease model for human atherosclerotic CAO. (musialek2025strokeriskmanagement pages 57-58)

---

## 15. Model organisms
Common experimental models relevant to CAO mechanisms (not comprehensively retrieved here) include **bilateral common carotid artery occlusion (BCCAO) in rodents** used for chronic hypoperfusion studies. (musialek2025strokeriskmanagement pages 57-58)

---

## Direct abstract quotes (as required; limited by available abstracts in retrieved set)
* **Poorthuis et al., Stroke (Nov 2024):** “Among **26 384** patients… **1662 (6.3%) had severe baseline ACAS**.” (poorthuis2024predictionofsevere pages 1-2)
* **Zhang et al., PLOS One (Jul 2025; scoping review of ICA occlusion recanalization):** “The proportion of recanalization was reported in 17 cohort studies for a **median of 21.2% (IQR 9.2–37.5%)**.” (zhang2025spontaneousrecanalizationof pages 1-3)
* **ERCAO trial (ClinicalTrials.gov NCT03179774):** protocol states it compares “**endovascular revascularization plus optimal medical therapy**… versus **optimal medical therapy alone**” for chronic CAO with neurocognitive primary endpoints. (NCT03179774 chunk 1)

(Additional verbatim abstract quotes from older landmark RCTs such as NASCET/CREST/ACST were not retrieved as full abstracts in this evidence set; the numeric summaries reported in secondary sources should be verified against primary trial abstracts/PMIDs for a production-grade knowledge base.) (ismail2023carotidarterystenosis pages 8-10)

---

## Notes on evidence gaps vs requested template
* **MONDO/ICD identifiers, MAXO IDs, and some HPO/GO exact IDs** were not present in the retrieved sources and would require direct ontology database lookup.
* **2023–2024 ICAO/CAO population prevalence/incidence** was not captured in retrieved primary epidemiology papers; current evidence here provides (i) severe asymptomatic stenosis epidemiology (2024) and (ii) recurrence risk estimates and intervention cohort outcomes for chronic/non-acute occlusion.



References

1. (zhao2024significanceofatherosclerotic pages 1-2): Tong-Yuan Zhao, Gang-Qin Xu, Jiang-Yu Xue, Wei-Xing Bai, Dong-Yang Cai, Bo-Wen Yang, Wei-Yu Shi, Tian-Xiao Li, and Bu-Lang Gao. Significance of atherosclerotic plaque location in recanalizing non-acute long-segment occlusion of the internal carotid artery. Scientific Reports, May 2024. URL: https://doi.org/10.1038/s41598-024-61938-y, doi:10.1038/s41598-024-61938-y. This article has 4 citations and is from a peer-reviewed journal.

2. (ren2023recanalizationofchronic pages 8-9): Wei Ren, Jiangyu Xue, Tongyuan Zhao, Gangqin Xu, Bowen Yang, Tianxiao Li, and Bulang Gao. Recanalization of chronic long-segment occlusion of the internal carotid artery with endovascular and hybrid surgery. Scientific Reports, Oct 2023. URL: https://doi.org/10.1038/s41598-023-44406-x, doi:10.1038/s41598-023-44406-x. This article has 9 citations and is from a peer-reviewed journal.

3. (NCT06303414 chunk 2):  Revascularization for Symptomatic Non-acute Carotid Artery Occlusion. Xuanwu Hospital, Beijing. 2016. ClinicalTrials.gov Identifier: NCT06303414

4. (poorthuis2024predictionofsevere pages 1-2): MD Michiel H.F. Poorthuis, PhD Steven H.J. Hageman, PhD Aernoud, MD T.L. Fiolet, PhD Jaap Kappelle, PhD Michiel L. Bots, P. Steg, MD Frank L.J. Visseren, PhD Deepak L. Bhatt, and M. M. G. J. D. Md. Prediction of severe baseline asymptomatic carotid stenosis and subsequent risk of stroke and cardiovascular disease. Stroke, 55:2632-2640, Nov 2024. URL: https://doi.org/10.1161/strokeaha.123.046894, doi:10.1161/strokeaha.123.046894. This article has 13 citations and is from a highest quality peer-reviewed journal.

5. (musialek2025strokeriskmanagement pages 28-29): Piotr Musialek, Leo H Bonati, Richard Bulbulia, Alison Halliday, Birgit Bock, Laura Capoccia, Hans-Henning Eckstein, Iris Q Grunwald, Peck Lin Lip, Andre Monteiro, Kosmas I Paraskevas, Anna Podlasek, Barbara Rantner, Kenneth Rosenfield, Adnan H Siddiqui, Henrik Sillesen, Isabelle Van Herzeele, Tomasz J Guzik, Lucia Mazzolai, Victor Aboyans, and Gregory Y H Lip. Stroke risk management in carotid atherosclerotic disease: a clinical consensus statement of the esc council on stroke and the esc working group on aorta and peripheral vascular diseases. Cardiovascular Research, 121:13-43, Aug 2025. URL: https://doi.org/10.1093/cvr/cvad135, doi:10.1093/cvr/cvad135. This article has 51 citations and is from a domain leading peer-reviewed journal.

6. (daolio2024accuracyofduplex pages 1-2): RAUL MUFFATO DAOLIO, LUIZ FERNANDO SANTETTI ZANIN, CAROLINA DUTRA QUEIROZ FLUMIGNAN, NICOLLE CASSOLA, HENRIQUE JORGE GUEDES NETO, JOSÉ EDUARDO MOURÃO SANTOS, JORGE EDUARDO AMORIM, LUÍS CARLOS UTA NAKANO, and RONALD LUIZ GOMES FLUMIGNAN. Accuracy of duplex ultrasonography versus angiotomography for the diagnosis of extracranial internal carotid stenosis. Revista do Colégio Brasileiro de Cirurgiões, May 2024. URL: https://doi.org/10.1590/0100-6991e-20243632-en, doi:10.1590/0100-6991e-20243632-en. This article has 7 citations.

7. (daolio2024accuracyofduplex pages 4-6): RAUL MUFFATO DAOLIO, LUIZ FERNANDO SANTETTI ZANIN, CAROLINA DUTRA QUEIROZ FLUMIGNAN, NICOLLE CASSOLA, HENRIQUE JORGE GUEDES NETO, JOSÉ EDUARDO MOURÃO SANTOS, JORGE EDUARDO AMORIM, LUÍS CARLOS UTA NAKANO, and RONALD LUIZ GOMES FLUMIGNAN. Accuracy of duplex ultrasonography versus angiotomography for the diagnosis of extracranial internal carotid stenosis. Revista do Colégio Brasileiro de Cirurgiões, May 2024. URL: https://doi.org/10.1590/0100-6991e-20243632-en, doi:10.1590/0100-6991e-20243632-en. This article has 7 citations.

8. (daolio2024accuracyofduplex pages 2-4): RAUL MUFFATO DAOLIO, LUIZ FERNANDO SANTETTI ZANIN, CAROLINA DUTRA QUEIROZ FLUMIGNAN, NICOLLE CASSOLA, HENRIQUE JORGE GUEDES NETO, JOSÉ EDUARDO MOURÃO SANTOS, JORGE EDUARDO AMORIM, LUÍS CARLOS UTA NAKANO, and RONALD LUIZ GOMES FLUMIGNAN. Accuracy of duplex ultrasonography versus angiotomography for the diagnosis of extracranial internal carotid stenosis. Revista do Colégio Brasileiro de Cirurgiões, May 2024. URL: https://doi.org/10.1590/0100-6991e-20243632-en, doi:10.1590/0100-6991e-20243632-en. This article has 7 citations.

9. (zeng2024systematicreviewand pages 1-2): Han-Lin Zeng, Fu-Qiang Shao, Xian-Feng Peng, and Chun-Yu Lei. Systematic review and meta-analysis of the diagnostic value of computed tomography angiography for severe internal carotid artery stenosis. BMC Medical Imaging, Aug 2024. URL: https://doi.org/10.1186/s12880-024-01390-6, doi:10.1186/s12880-024-01390-6. This article has 6 citations and is from a peer-reviewed journal.

10. (zeng2024systematicreviewand pages 6-6): Han-Lin Zeng, Fu-Qiang Shao, Xian-Feng Peng, and Chun-Yu Lei. Systematic review and meta-analysis of the diagnostic value of computed tomography angiography for severe internal carotid artery stenosis. BMC Medical Imaging, Aug 2024. URL: https://doi.org/10.1186/s12880-024-01390-6, doi:10.1186/s12880-024-01390-6. This article has 6 citations and is from a peer-reviewed journal.

11. (li2026comparativediagnosticvalue pages 1-2): Wei Li, Jin Wang, Yuan-Zheng Zhu, and Jie Liu. Comparative diagnostic value of carotid colour doppler ultrasound and carotid magnetic resonance angiography in detecting carotid artery stenosis. Medical Ultrasonography, Feb 2026. URL: https://doi.org/10.11152/mu-4590, doi:10.11152/mu-4590. This article has 0 citations.

12. (ren2023recanalizationofchronic pages 1-2): Wei Ren, Jiangyu Xue, Tongyuan Zhao, Gangqin Xu, Bowen Yang, Tianxiao Li, and Bulang Gao. Recanalization of chronic long-segment occlusion of the internal carotid artery with endovascular and hybrid surgery. Scientific Reports, Oct 2023. URL: https://doi.org/10.1038/s41598-023-44406-x, doi:10.1038/s41598-023-44406-x. This article has 9 citations and is from a peer-reviewed journal.

13. (ren2023recanalizationofchronic pages 7-8): Wei Ren, Jiangyu Xue, Tongyuan Zhao, Gangqin Xu, Bowen Yang, Tianxiao Li, and Bulang Gao. Recanalization of chronic long-segment occlusion of the internal carotid artery with endovascular and hybrid surgery. Scientific Reports, Oct 2023. URL: https://doi.org/10.1038/s41598-023-44406-x, doi:10.1038/s41598-023-44406-x. This article has 9 citations and is from a peer-reviewed journal.

14. (ren2023recanalizationofchronic pages 3-5): Wei Ren, Jiangyu Xue, Tongyuan Zhao, Gangqin Xu, Bowen Yang, Tianxiao Li, and Bulang Gao. Recanalization of chronic long-segment occlusion of the internal carotid artery with endovascular and hybrid surgery. Scientific Reports, Oct 2023. URL: https://doi.org/10.1038/s41598-023-44406-x, doi:10.1038/s41598-023-44406-x. This article has 9 citations and is from a peer-reviewed journal.

15. (spiliopoulos2024cirsestandardsof pages 9-10): Stavros Spiliopoulos, Raphaël Blanc, Roberto Gandini, Stefan Müller-Hülsbeck, Wolfgang Reith, and Ornella Moschovaki-Zeiger. Cirse standards of practice on carotid artery stenting. Cardiovascular and Interventional Radiology, 47:705-716, Apr 2024. URL: https://doi.org/10.1007/s00270-024-03707-y, doi:10.1007/s00270-024-03707-y. This article has 18 citations and is from a peer-reviewed journal.

16. (spiliopoulos2024cirsestandardsof pages 10-11): Stavros Spiliopoulos, Raphaël Blanc, Roberto Gandini, Stefan Müller-Hülsbeck, Wolfgang Reith, and Ornella Moschovaki-Zeiger. Cirse standards of practice on carotid artery stenting. Cardiovascular and Interventional Radiology, 47:705-716, Apr 2024. URL: https://doi.org/10.1007/s00270-024-03707-y, doi:10.1007/s00270-024-03707-y. This article has 18 citations and is from a peer-reviewed journal.

17. (ding2024identificationofshared pages 1-2): Kexin Ding, Xueying Qin, Huairong Wang, Kun Wang, Xiaoying Kang, Yao Yu, Yang Liu, Haiying Gong, Tao Wu, Dafang Chen, Yonghua Hu, Tao Wang, and Yiqun Wu. Identification of shared genetic etiology of cardiovascular and cerebrovascular diseases through common cardiometabolic risk factors. Communications Biology, Dec 2024. URL: https://doi.org/10.1038/s42003-024-07417-6, doi:10.1038/s42003-024-07417-6. This article has 10 citations and is from a peer-reviewed journal.

18. (ding2024identificationofshared pages 14-15): Kexin Ding, Xueying Qin, Huairong Wang, Kun Wang, Xiaoying Kang, Yao Yu, Yang Liu, Haiying Gong, Tao Wu, Dafang Chen, Yonghua Hu, Tao Wang, and Yiqun Wu. Identification of shared genetic etiology of cardiovascular and cerebrovascular diseases through common cardiometabolic risk factors. Communications Biology, Dec 2024. URL: https://doi.org/10.1038/s42003-024-07417-6, doi:10.1038/s42003-024-07417-6. This article has 10 citations and is from a peer-reviewed journal.

19. (wu2023associationsofgenetic pages 1-2): Tzu-Wei Wu, Chao-Liang Chou, Chun-Fang Cheng, Shu-Xin Lu, Yih-Jer Wu, and Li-Yu Wang. Associations of genetic markers of diabetes mellitus with carotid atherosclerosis: a community-based case–control study. Cardiovascular Diabetology, Mar 2023. URL: https://doi.org/10.1186/s12933-023-01787-7, doi:10.1186/s12933-023-01787-7. This article has 10 citations and is from a peer-reviewed journal.

20. (musialek2025strokeriskmanagement pages 15-16): Piotr Musialek, Leo H Bonati, Richard Bulbulia, Alison Halliday, Birgit Bock, Laura Capoccia, Hans-Henning Eckstein, Iris Q Grunwald, Peck Lin Lip, Andre Monteiro, Kosmas I Paraskevas, Anna Podlasek, Barbara Rantner, Kenneth Rosenfield, Adnan H Siddiqui, Henrik Sillesen, Isabelle Van Herzeele, Tomasz J Guzik, Lucia Mazzolai, Victor Aboyans, and Gregory Y H Lip. Stroke risk management in carotid atherosclerotic disease: a clinical consensus statement of the esc council on stroke and the esc working group on aorta and peripheral vascular diseases. Cardiovascular Research, 121:13-43, Aug 2025. URL: https://doi.org/10.1093/cvr/cvad135, doi:10.1093/cvr/cvad135. This article has 51 citations and is from a domain leading peer-reviewed journal.

21. (NCT00029146 chunk 2): William Powers. Carotid Occlusion Surgery Study. University of North Carolina, Chapel Hill. 2002. ClinicalTrials.gov Identifier: NCT00029146

22. (zhang2025spontaneousrecanalizationof pages 1-3): Sarah Y. Zhang, Hee Sahng Chung, Brian Dewar, Robert Fahed, Michel Shamy, Risa Shorr, and Dar Dowlatshahi. Spontaneous recanalization of extracranial internal carotid occlusion: a systematic scoping review. PLOS One, 20:e0326261, Jul 2025. URL: https://doi.org/10.1371/journal.pone.0326261, doi:10.1371/journal.pone.0326261. This article has 0 citations and is from a peer-reviewed journal.

23. (spiliopoulos2024cirsestandardsof pages 5-6): Stavros Spiliopoulos, Raphaël Blanc, Roberto Gandini, Stefan Müller-Hülsbeck, Wolfgang Reith, and Ornella Moschovaki-Zeiger. Cirse standards of practice on carotid artery stenting. Cardiovascular and Interventional Radiology, 47:705-716, Apr 2024. URL: https://doi.org/10.1007/s00270-024-03707-y, doi:10.1007/s00270-024-03707-y. This article has 18 citations and is from a peer-reviewed journal.

24. (ismail2023carotidarterystenosis pages 8-10): Aqsa Ismail, Shivani Ravipati, Diana Gonzalez-Hernandez, Hashim Mahmood, Alizay Imran, Eduardo J Munoz, Saad Naeem, Zain U Abdin, and Humza F Siddiqui. Carotid artery stenosis: a look into the diagnostic and management strategies, and related complications. Cureus, May 2023. URL: https://doi.org/10.7759/cureus.38794, doi:10.7759/cureus.38794. This article has 51 citations.

25. (musialek2025strokeriskmanagement pages 57-58): Piotr Musialek, Leo H Bonati, Richard Bulbulia, Alison Halliday, Birgit Bock, Laura Capoccia, Hans-Henning Eckstein, Iris Q Grunwald, Peck Lin Lip, Andre Monteiro, Kosmas I Paraskevas, Anna Podlasek, Barbara Rantner, Kenneth Rosenfield, Adnan H Siddiqui, Henrik Sillesen, Isabelle Van Herzeele, Tomasz J Guzik, Lucia Mazzolai, Victor Aboyans, and Gregory Y H Lip. Stroke risk management in carotid atherosclerotic disease: a clinical consensus statement of the esc council on stroke and the esc working group on aorta and peripheral vascular diseases. Cardiovascular Research, 121:13-43, Aug 2025. URL: https://doi.org/10.1093/cvr/cvad135, doi:10.1093/cvr/cvad135. This article has 51 citations and is from a domain leading peer-reviewed journal.

26. (richter2025endothelialcellgenetics pages 6-7): Kent R. Richter, Patrick King, Mason Masters, Omid Shoraka, Michael T. Bounajem, Leo J. Y. Kim, Sarah Dabb, Sarah Nguyen, Jennifer J. Majersik, Aaron Shoskes, Kendell Clement, Ethan Winkler, Ramesh Grandhi, and Karol P. Budohoski. Endothelial cell genetics in carotid artery atherosclerosis and intracranial atherosclerosis: a systematic review. Stroke: Vascular and Interventional Neurology, Nov 2025. URL: https://doi.org/10.1161/svin.125.001813, doi:10.1161/svin.125.001813. This article has 0 citations.

27. (richter2025endothelialcellgenetics pages 14-15): Kent R. Richter, Patrick King, Mason Masters, Omid Shoraka, Michael T. Bounajem, Leo J. Y. Kim, Sarah Dabb, Sarah Nguyen, Jennifer J. Majersik, Aaron Shoskes, Kendell Clement, Ethan Winkler, Ramesh Grandhi, and Karol P. Budohoski. Endothelial cell genetics in carotid artery atherosclerosis and intracranial atherosclerosis: a systematic review. Stroke: Vascular and Interventional Neurology, Nov 2025. URL: https://doi.org/10.1161/svin.125.001813, doi:10.1161/svin.125.001813. This article has 0 citations.

28. (richter2025endothelialcellgenetics pages 11-12): Kent R. Richter, Patrick King, Mason Masters, Omid Shoraka, Michael T. Bounajem, Leo J. Y. Kim, Sarah Dabb, Sarah Nguyen, Jennifer J. Majersik, Aaron Shoskes, Kendell Clement, Ethan Winkler, Ramesh Grandhi, and Karol P. Budohoski. Endothelial cell genetics in carotid artery atherosclerosis and intracranial atherosclerosis: a systematic review. Stroke: Vascular and Interventional Neurology, Nov 2025. URL: https://doi.org/10.1161/svin.125.001813, doi:10.1161/svin.125.001813. This article has 0 citations.

29. (musialek2025strokeriskmanagement pages 50-51): Piotr Musialek, Leo H Bonati, Richard Bulbulia, Alison Halliday, Birgit Bock, Laura Capoccia, Hans-Henning Eckstein, Iris Q Grunwald, Peck Lin Lip, Andre Monteiro, Kosmas I Paraskevas, Anna Podlasek, Barbara Rantner, Kenneth Rosenfield, Adnan H Siddiqui, Henrik Sillesen, Isabelle Van Herzeele, Tomasz J Guzik, Lucia Mazzolai, Victor Aboyans, and Gregory Y H Lip. Stroke risk management in carotid atherosclerotic disease: a clinical consensus statement of the esc council on stroke and the esc working group on aorta and peripheral vascular diseases. Cardiovascular Research, 121:13-43, Aug 2025. URL: https://doi.org/10.1093/cvr/cvad135, doi:10.1093/cvr/cvad135. This article has 51 citations and is from a domain leading peer-reviewed journal.

30. (richter2025endothelialcellgenetics pages 1-2): Kent R. Richter, Patrick King, Mason Masters, Omid Shoraka, Michael T. Bounajem, Leo J. Y. Kim, Sarah Dabb, Sarah Nguyen, Jennifer J. Majersik, Aaron Shoskes, Kendell Clement, Ethan Winkler, Ramesh Grandhi, and Karol P. Budohoski. Endothelial cell genetics in carotid artery atherosclerosis and intracranial atherosclerosis: a systematic review. Stroke: Vascular and Interventional Neurology, Nov 2025. URL: https://doi.org/10.1161/svin.125.001813, doi:10.1161/svin.125.001813. This article has 0 citations.

31. (musialek2025strokeriskmanagement pages 18-19): Piotr Musialek, Leo H Bonati, Richard Bulbulia, Alison Halliday, Birgit Bock, Laura Capoccia, Hans-Henning Eckstein, Iris Q Grunwald, Peck Lin Lip, Andre Monteiro, Kosmas I Paraskevas, Anna Podlasek, Barbara Rantner, Kenneth Rosenfield, Adnan H Siddiqui, Henrik Sillesen, Isabelle Van Herzeele, Tomasz J Guzik, Lucia Mazzolai, Victor Aboyans, and Gregory Y H Lip. Stroke risk management in carotid atherosclerotic disease: a clinical consensus statement of the esc council on stroke and the esc working group on aorta and peripheral vascular diseases. Cardiovascular Research, 121:13-43, Aug 2025. URL: https://doi.org/10.1093/cvr/cvad135, doi:10.1093/cvr/cvad135. This article has 51 citations and is from a domain leading peer-reviewed journal.

32. (spiliopoulos2024cirsestandardsof media 6e47be29): Stavros Spiliopoulos, Raphaël Blanc, Roberto Gandini, Stefan Müller-Hülsbeck, Wolfgang Reith, and Ornella Moschovaki-Zeiger. Cirse standards of practice on carotid artery stenting. Cardiovascular and Interventional Radiology, 47:705-716, Apr 2024. URL: https://doi.org/10.1007/s00270-024-03707-y, doi:10.1007/s00270-024-03707-y. This article has 18 citations and is from a peer-reviewed journal.

33. (spiliopoulos2024cirsestandardsof media 55399623): Stavros Spiliopoulos, Raphaël Blanc, Roberto Gandini, Stefan Müller-Hülsbeck, Wolfgang Reith, and Ornella Moschovaki-Zeiger. Cirse standards of practice on carotid artery stenting. Cardiovascular and Interventional Radiology, 47:705-716, Apr 2024. URL: https://doi.org/10.1007/s00270-024-03707-y, doi:10.1007/s00270-024-03707-y. This article has 18 citations and is from a peer-reviewed journal.

34. (NCT03179774 chunk 1):  Endovascular Revascularization for Chronic Carotid Artery Occlusion Trial. National Taiwan University Hospital. 2017. ClinicalTrials.gov Identifier: NCT03179774