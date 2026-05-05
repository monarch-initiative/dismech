---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T18:26:49.282885'
end_time: '2026-05-04T18:48:12.760591'
duration_seconds: 1283.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fibromuscular Dysplasia
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Fibromuscular Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Fibromuscular Dysplasia** covering all of the
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
- **Disease Name:** Fibromuscular Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Fibromuscular Dysplasia** covering all of the
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


## Fibromuscular Dysplasia (FMD) — Disease Characteristics Research Report

### Executive summary
Fibromuscular dysplasia (FMD) is an idiopathic, systemic, non-inflammatory, non-atherosclerotic arteriopathy that affects small-to-medium muscular arteries and is characterized by angiographic focal or multifocal stenotic lesions; it is associated with hypertension and major cerebrovascular/cardiovascular events and commonly co-occurs with aneurysm, dissection, and tortuosity across multiple vascular beds. Consensus guidance emphasizes imaging-confirmed diagnosis (≥1 focal or multifocal lesion), at least one-time brain-to-pelvis vascular imaging to map multisite disease and screen for aneurysm/dissection, and medical management focusing on antiplatelet therapy (aspirin 75–100 mg/day when not contraindicated) and blood pressure control. Recent genetic studies support a polygenic basis with reproducible common risk loci (PHACTR1, LRP1, ATP2B1, LIMA1; plus SLC24A3 by TWAS), and 2024 systems-genetics work proposes network-level “key driver” genes (e.g., UBR4) with functional testing in fibroblasts and vascular smooth muscle cell models. (gornik2019firstinternationalconsensus pages 9-10, persu2022currentprogressin pages 2-3, georges2021geneticinvestigationof pages 1-2, d’escamard2024integrativegeneregulatory pages 1-13)

---

## 1. Disease information

### 1.1 What is the disease? (concise overview)
A foundational definition used in recent reviews describes FMD as “an idiopathic, segmental, non-atherosclerotic and non-inflammatory disease of the musculature of arterial walls, leading to stenosis of small and medium-sized arteries” and causing complications including hypertension, stroke, dissections, aneurysms, and ischemia in multiple vascular territories. (monaco2018genomicsoffibromuscular pages 1-3)

The 2019 First International Consensus describes FMD as a non-atherosclerotic arterial disease with abnormal cellular proliferation and distorted arterial wall architecture and recommends classifying lesions by angiographic appearance as focal or multifocal. (gornik2019firstinternationalconsensus pages 2-4)

### 1.2 Key identifiers
The retrieved evidence set contains limited explicit ontology/coding identifiers. It does include a MONDO identifier for multifocal FMD from OpenTargets-derived content, but did not include MeSH/ICD/OMIM/Orphanet identifiers in the extracted full text. (monaco2018genomicsoffibromuscular pages 1-3)

| Identifier type | Value | Synonyms / alternate names supported by provided evidence | Evidence / citation IDs |
|---|---|---|---|
| Disease name | Fibromuscular dysplasia | FMD; non-atherosclerotic, non-inflammatory arterial disease / arteriopathy | (huart2023fromfibromusculardysplasia pages 1-2, gornik2019firstinternationalconsensus pages 2-4) |
| MONDO (general disease) | not found in provided sources | Fibromuscular dysplasia | (gornik2019firstinternationalconsensus pages 2-4) |
| MONDO (specific subtype) | MONDO_0859151 | Fibromuscular dysplasia, multifocal | (monaco2018genomicsoffibromuscular pages 1-3) |
| MeSH | not found in provided sources | FMD | (gornik2019firstinternationalconsensus pages 2-4) |
| ICD-10 | not found in provided sources | FMD | (gornik2019firstinternationalconsensus pages 2-4) |
| ICD-11 | not found in provided sources | FMD | (gornik2019firstinternationalconsensus pages 2-4) |
| Orphanet | not found in provided sources | FMD | (gornik2019firstinternationalconsensus pages 2-4) |
| OMIM | not found in provided sources | FMD | (gornik2019firstinternationalconsensus pages 2-4) |
| Angiographic subtype | Multifocal FMD | “string of beads”; classic multifocal phenotype; corresponds roughly to medial histology / medial fibroplasia in older terminology | (huart2023fromfibromusculardysplasia pages 1-2, persu2022currentprogressin pages 2-3, gornik2019firstinternationalconsensus media 968288f3) |
| Angiographic subtype | Focal FMD | focal stenosis; tubular or focal stenosis; corresponds roughly to intimal histology / intimal fibroplasia in older terminology | (huart2023fromfibromusculardysplasia pages 1-2, persu2022currentprogressin pages 2-3, gornik2019firstinternationalconsensus media 968288f3) |
| Historical histopathology term | Medial fibroplasia | older histopathologic terminology linked to multifocal disease pattern | (huart2023fromfibromusculardysplasia pages 1-2, persu2022currentprogressin pages 2-3) |
| Historical histopathology term | Intimal fibroplasia | older histopathologic terminology linked to focal disease pattern | (huart2023fromfibromusculardysplasia pages 1-2, persu2022currentprogressin pages 2-3) |
| Related lesion / subtype discussed in provided evidence | Carotid web | atypical fibromuscular dysplasia subtype; intimal FMD; carotid web | (zedde2025fibromusculardysplasiaand pages 17-17) |


*Table: This table summarizes disease identifiers and supported terminology for fibromuscular dysplasia using only the evidence available in the retrieved sources. It highlights where identifiers were not present in the provided evidence and distinguishes current angiographic subtypes from older histopathologic terms.*

**Notes on missing identifiers:** ICD-10/ICD-11, MeSH, OMIM, and Orphanet identifiers were not present in the provided full-text evidence snippets; thus they cannot be asserted here without additional targeted database queries beyond the current tool state. (gornik2019firstinternationalconsensus pages 2-4)

### 1.3 Common synonyms / alternative names
Consensus and review literature consistently uses: **fibromuscular dysplasia**, **FMD**, and angiographic subtypes **multifocal FMD (“string of beads”)** and **focal FMD**. (huart2023fromfibromusculardysplasia pages 1-2, persu2022currentprogressin pages 2-3)

A related lesion discussed in neurologic literature is an **arterial diaphragm/web** (including carotid bulb diaphragm), described as an endoluminal web with intimal fibroplasia; this overlaps conceptually with “carotid web” described as intimal-type FMD in other sources, though carotid web-specific literature in this retrieval set is largely outside 2023–2024 primary FMD guidelines. (touze2019fibromusculardysplasiaand pages 14-18, zedde2025fibromusculardysplasiaand pages 17-17)

### 1.4 Evidence source type
Most epidemiology/phenotype statements below come from **aggregated disease-level resources** (international consensus and major registries) rather than individual-patient EHR. Example: the 2019 consensus reports US Registry and European/International Registry tables. (gornik2019firstinternationalconsensus pages 7-9)

---

## 2. Etiology

### 2.1 Disease causal factors (current understanding)
FMD is considered idiopathic with multifactorial contributions. A high-quality 2022 review states that “a variety of genetic, mechanical, and hormonal factors play a role in the pathogenesis of FMD,” and that it is “probable” that FMD involves a combination of genetic and environmental factors. (persu2022currentprogressin pages 2-3)

### 2.2 Risk factors

#### 2.2.1 Genetic risk factors
**Common-variant susceptibility (polygenic):**
* **PHACTR1 locus (rs9349379)** was the first genome-wide significant susceptibility locus reported, supporting a “complex genetic pattern of inheritance.” In the 2016 PLoS Genetics study, the authors conclude: “We report the first susceptibility locus for FMD…,” identifying **rs9349379** intronic to **PHACTR1** with **OR 1.39** and **P = 7.4×10−10** (multi-cohort total 1,154 cases and 3,895 controls). (kiando2016phactr1isa pages 1-2)
* A larger 2021 GWAS meta-analysis (six studies; **1,556 FMD cases and 7,100 controls**) reported four robust loci (**PHACTR1, LRP1, ATP2B1, LIMA1**) and one additional locus by artery TWAS (**SLC24A3**). It emphasized pathways “related to actin cytoskeleton and intracellular calcium homeostasis, central to vascular contraction.” (georges2021geneticinvestigationof pages 1-2)

**Evidence for functional effects and relevant cell types:** The 2016 PHACTR1 study detected PHACTR1 expression in **endothelium and smooth muscle cells** and observed higher expression in rs9349379-A carriers in primary fibroblasts; zebrafish knockdown produced vascular dilation. (kiando2016phactr1isa pages 1-2)

**Rare variation / syndromic overlap (in reviews):** A 2022 genetics-focused review notes rare variation signals implicating impaired prostacyclin signaling and fibrillar collagens, consistent with a mixed architecture of common and rare genetic contributors (review-level statement; not a single variant assertion in this evidence extract). (georges2022thecomplexgenetic pages 11-13)

#### 2.2.2 Environmental and lifestyle risk factors
A clear, quantified association exists between **smoking history** and intracranial aneurysm among women with FMD in the US Registry.
* In Lather et al. (JAMA Neurology; published online **2017-07-17**, print **Sep 2017**), among women with intracranial aneurysm (IA), **53.8%** had a smoking history vs **28.9%** without IA (**P < .001**). (lather2017prevalenceofintracranial pages 5-6, lather2017prevalenceofintracranial pages 1-2)

#### 2.2.3 Demographic risk factor (sex)
FMD shows strong female predominance across major registries: in the 2019 consensus tables, women were **94.7%** of the US Registry and **83.3%** of the European/International Registry. (gornik2019firstinternationalconsensus pages 7-9)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence extracts; the genetics literature in this retrieval set focuses on susceptibility. (georges2021geneticinvestigationof pages 1-2)

### 2.4 Gene–environment interactions
The retrieved evidence does not provide a formal gene–environment interaction analysis for FMD. However, the strong smoking–intracranial aneurysm association in FMD cohorts and polygenic architecture indicate this is a plausible area for future research. (lather2017prevalenceofintracranial pages 5-6, georges2021geneticinvestigationof pages 1-2)

---

## 3. Phenotypes

### 3.1 Core vascular phenotypes
**Angiographic patterns:** multifocal (“string of beads”) and focal stenosis. Multifocal FMD predominates in registry data. (gornik2019firstinternationalconsensus pages 9-10)

**Non-stenotic vascular manifestations associated with FMD:** aneurysm, dissection, tortuosity. In a 2023 review, dissection is reported in ~15–20% and aneurysm in ~20–25% of FMD cases (range across cohorts). (huart2023fromfibromusculardysplasia pages 1-2)

**Visual reference (angiographic subtypes):** international consensus figure showing multifocal vs focal patterns in renal and carotid arteries. (gornik2019firstinternationalconsensus media 968288f3, gornik2019firstinternationalconsensus media 561bacbf)

### 3.2 Common symptoms and neurologic manifestations
A 2019 JAMA Neurology systematic review notes headaches (often migraine) are common—reported “in up to 70% of patients”—and that cerebrovascular FMD is often asymptomatic but can present with TIA/ischemic stroke, SAH, and more rarely intracranial hemorrhage. (touze2019fibromusculardysplasiaand pages 6-11)

In ARCADIA-POL (Hypertension 2020; n=129), symptom frequencies included headaches **38.8%**, dizziness **37.2%**, pulsatile tinnitus **15.5%**, and stroke **9.3%**. (warcholcelinska2020geneticstudyof pages 1-2)

### 3.3 Phenotype characteristics and suggested HPO terms
Below are common phenotypes with evidence-based frequencies where available and suggested HPO terms.

1) **Hypertension (renovascular/secondary)**
* Frequency: US Registry **67.3%**, European/International **73.7%**, ARCADIA-POL **87.6%**. (gornik2019firstinternationalconsensus pages 7-9, warcholcelinska2020geneticstudyof pages 1-2)
* Typical onset: adult (registry mean age at diagnosis 45.8–53.3 years, with younger in ARCADIA-POL). (gornik2019firstinternationalconsensus pages 7-9, warcholcelinska2020geneticstudyof pages 1-2)
* Suggested HPO: **HP:0000822 (Hypertension)**

2) **Headache / migraine-type headaches**
* Frequency: US Registry headache **69.4%**; systematic review “up to 70%”; ARCADIA-POL headaches **38.8%** (likely different ascertainment). (gornik2019firstinternationalconsensus pages 7-9, touze2019fibromusculardysplasiaand pages 6-11, warcholcelinska2020geneticstudyof pages 1-2)
* Suggested HPO: **HP:0002315 (Headache)**; **HP:0002076 (Migraine)**

3) **Pulsatile tinnitus**
* ARCADIA-POL: 15.5%. (warcholcelinska2020geneticstudyof pages 1-2)
* Systematic review notes pulsatile tinnitus among most common presenting symptoms. (touze2019fibromusculardysplasiaand pages 11-14)
* Suggested HPO: **HP:0030794 (Pulsatile tinnitus)**

4) **Cervical artery dissection**
* Systematic review excerpt: carotid and vertebral dissections occur in ~16% and ~5% of all FMD patients, respectively (as summarized in the review). (touze2019fibromusculardysplasiaand pages 11-14)
* Suggested HPO: **HP:0025517 (Carotid artery dissection)**; **HP:0031113 (Vertebral artery dissection)**

5) **Intracranial aneurysm**
* Women with FMD (US Registry, imaged): IA prevalence **12.9%** (86/669). (lather2017prevalenceofintracranial pages 3-4, lather2017prevalenceofintracranial pages 1-2)
* Suggested HPO: **HP:0004944 (Intracranial aneurysm)**

6) **Stroke / TIA / SAH**
* Registry rates: stroke **10.1%** (US) vs **7.7%** (EU); TIA **12.3%** (US) vs **3.5%** (EU); SAH **2.2%** (US) vs **3.5%** (EU). (gornik2019firstinternationalconsensus pages 7-9)
* Suggested HPO: **HP:0001297 (Stroke)**; **HP:0002326 (Transient ischemic attack)**; **HP:0002139 (Subarachnoid hemorrhage)**

### 3.4 Quality of life impact
Direct QoL instruments (e.g., SF-36, EQ-5D, PROMIS) were not captured in the retrieved evidence snippets; however, the high prevalence of chronic symptoms (headache, pulsatile tinnitus) and occurrence of stroke/dissection/aneurysm implies substantial QoL burden. Explicit QoL statistics require additional targeted retrieval. (touze2019fibromusculardysplasiaand pages 6-11)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
FMD is generally not a monogenic disorder in most cases; the strongest evidence supports **polygenic susceptibility** with reproducible common-variant loci rather than single-gene causation in unselected adult cohorts. (georges2021geneticinvestigationof pages 1-2, kiando2016phactr1isa pages 1-2)

### 4.2 Pathogenic/susceptibility variants and loci (human)
* **PHACTR1 (rs9349379)**: susceptibility locus (OR ~1.39–1.44 across studies). (kiando2016phactr1isa pages 1-2, georges2021geneticinvestigationof pages 1-2)
* **LRP1, ATP2B1, LIMA1**: additional robust loci from GWAS meta-analysis. (georges2021geneticinvestigationof pages 1-2)
* **SLC24A3**: implicated by transcriptome-wide association in arteries. (georges2021geneticinvestigationof pages 1-2)

**Mechanistic interpretation from GWAS:** target genes implicated in “actin cytoskeleton and intracellular calcium homeostasis,” consistent with altered vascular smooth muscle contraction biology. (georges2021geneticinvestigationof pages 1-2)

### 4.3 Modifier genes / rare variant hypotheses
A 2022 genetics review highlights rare variation signals in prostacyclin signaling and fibrillar collagens (review-level synthesis). (georges2022thecomplexgenetic pages 11-13)

### 4.4 Epigenetics and chromosomal abnormalities
No epigenetic signatures or chromosomal abnormalities were identified in the retrieved evidence extracts. (d’escamard2024integrativegeneregulatory pages 1-13)

---

## 5. Environmental information

### 5.1 Lifestyle factors
**Smoking:** strongly associated with intracranial aneurysm among women with FMD in the US Registry (53.8% with IA vs 28.9% without; P < .001). (lather2017prevalenceofintracranial pages 5-6)

### 5.2 Infectious agents
No infectious etiology is supported in the retrieved evidence. (gornik2019firstinternationalconsensus pages 2-4)

---

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic understanding (integrated)
**Lesion biology:** Histopathologic descriptions (fibrosis, cellular hyperplasia, distorted architecture) are summarized in 2022 review literature, with phenotype expansion to aneurysm, dissection, and tortuosity. (persu2022currentprogressin pages 2-3)

**Vascular-cell process hypotheses supported by genetics:** GWAS/TWAS results implicate genes involved in actin cytoskeleton regulation and intracellular calcium handling, consistent with altered vascular contraction. (georges2021geneticinvestigationof pages 1-2)

**Endothelial/smooth muscle involvement:** PHACTR1 expression in endothelium and smooth muscle with functional perturbations in zebrafish supports a developmental/structural vascular component. (kiando2016phactr1isa pages 1-2)

### 6.2 Recent developments (2024 priority): network drivers and experimental validation
**d’Escamard et al., Nature Cardiovascular Research (Sep 2024; DOI https://doi.org/10.1038/s44161-024-00533-w)** applied integrative gene regulatory network analysis and tested **UBR4** as a candidate driver.
* **In vitro**: UBR4 knockdown in immortalized human fibroblasts with RNA-seq/qRT-PCR profiling. (d’escamard2024integrativegeneregulatory pages 1-13)
* **In vivo**: VSMC-targeted **Ubr4** knockout (Sm22α-Ubr4KO) with vascular histopathology (elastic lamina structure, collagen content), immune-cell staining, proteomics, and physiological phenotyping. (d’escamard2024integrativegeneregulatory pages 13-24)

**Interpretation:** This study represents a shift from association-only genetics toward experimentally interrogating gene-network drivers that may influence extracellular matrix/elastic lamina integrity and vascular-wall remodeling in relevant vascular wall cell types (fibroblasts, VSMCs). (d’escamard2024integrativegeneregulatory pages 13-24)

### 6.3 Suggested GO and CL terms
**Cell types (CL):**
* Vascular smooth muscle cell (**CL:0000192**)
* Endothelial cell (**CL:0000115**)
* Fibroblast (**CL:0000057**)
* T cell (for CD3+ infiltration) (**CL:0000084**) (d’escamard2024integrativegeneregulatory pages 13-24)

**Processes (GO Biological Process):**
* Actin cytoskeleton organization (**GO:0030036**) (GWAS pathway interpretation) (georges2021geneticinvestigationof pages 1-2)
* Calcium ion homeostasis (**GO:0055074**) (GWAS pathway interpretation) (georges2021geneticinvestigationof pages 1-2)
* Extracellular matrix organization (**GO:0030198**) (histology/collagen findings) (d’escamard2024integrativegeneregulatory pages 13-24)
* Regulation of vascular smooth muscle contraction (**GO:1904545**, close proxy) (georges2021geneticinvestigationof pages 1-2)

---

## 7. Anatomical structures affected

### 7.1 Organ level / vascular beds
Consensus and registry data emphasize renal and cervico-cephalic (extracranial carotid/vertebral) involvement as most common, with multisite disease frequent. (gornik2019firstinternationalconsensus pages 2-4, gornik2019firstinternationalconsensus pages 9-10)

In ARCADIA-POL, vascular beds involved included renal (84.5%), cerebrovascular (26.4%), visceral (15.5%), and lower extremity (11.6%). (warcholcelinska2020geneticstudyof pages 1-2)

Systematic review emphasizes cerebrovascular FMD typically involves the cervical internal carotid and vertebral arteries (high proportions, e.g., carotid involvement ~95% and vertebral involvement ~60–85% in reviewed literature). (touze2019fibromusculardysplasiaand pages 6-11)

**Suggested UBERON terms (examples):**
* Renal artery (**UBERON:0001198**)
* Internal carotid artery (**UBERON:0000945**)
* Vertebral artery (**UBERON:0001639**)
* Intracranial artery (**UBERON:0000946**, generic) (touze2019fibromusculardysplasiaand pages 6-11)

### 7.2 Tissue and cell level
FMD is a disease of the arterial wall involving smooth muscle and connective tissue layers, with network/mechanistic data implicating vascular smooth muscle cells and fibroblasts and evidence of immune-cell infiltration in experimental models. (kiando2016phactr1isa pages 1-2, d’escamard2024integrativegeneregulatory pages 13-24)

### 7.3 Localization / pattern
Multifocal lesions are typically mid-to-distal in affected arteries (“string-of-beads” pattern), and focal stenosis can occur as a single short/tubular lesion; multifocal and focal may coexist in some patients. (huart2023fromfibromusculardysplasia pages 1-2, touze2019fibromusculardysplasiaand pages 24-30)

---

## 8. Temporal development

### 8.1 Onset
Registry mean ages at diagnosis are typically mid-adulthood (US Registry ~53 years; European/International ~46 years), with focal disease often detected earlier (“usually discovered before 30 years of age” in the consensus excerpt). (gornik2019firstinternationalconsensus pages 7-9, gornik2019firstinternationalconsensus pages 9-10)

### 8.2 Progression
Longitudinal progression is an active research area; PROFILE (NCT02961868) explicitly measures imaging-confirmed progression over 3 years. (NCT02961868 chunk 1)

---

## 9. Inheritance and population

### 9.1 Epidemiology
Reliable population incidence estimates are not provided in the retrieved evidence. However, prevalence estimates from imaging-screened kidney donor cohorts are cited in reviews (~3% in one genetics paper summary and 3–6% in kidney donors in a genomics review), reflecting detection of clinically silent lesions. (georges2021geneticinvestigationof pages 1-2, monaco2018genomicsoffibromuscular pages 1-3)

**Sex ratio:** Strong female predominance in registries (US 94.7% women; EU 83.3%; ARCADIA-POL 80.6%). (gornik2019firstinternationalconsensus pages 7-9, warcholcelinska2020geneticstudyof pages 1-2)

**Multifocal vs focal distribution:** US Registry multifocal 76.0%, focal 2.4%; European/International multifocal 71.9%, focal 28.1%. (gornik2019firstinternationalconsensus pages 9-10)

### 9.2 Inheritance pattern
Familial cases are uncommon (“<5%” in multiple sources). (kiando2016phactr1isa pages 1-2, touze2019fibromusculardysplasiaand pages 6-11)

---

## 10. Diagnostics

### 10.1 Diagnostic criteria (consensus-based)
A key diagnostic principle is that **at least one multifocal or focal arterial lesion must be present** to confirm FMD; **aneurysm, dissection, or tortuosity alone is not sufficient** for diagnosis. (persu2022currentprogressin pages 2-3)

### 10.2 Imaging modalities
* **CTA/MRA:** CTA is described as “the initial test of choice for suspected FMD” in the consensus excerpt, and CTA or contrast-enhanced MRA are recommended for brain-to-pelvis mapping at least once. (gornik2019firstinternationalconsensus pages 9-10, gornik2019firstinternationalconsensus pages 12-14)
* **Catheter angiography (DSA):** remains the “gold standard,” but generally reserved for cases where it will impact management due to invasiveness. (gornik2019firstinternationalconsensus pages 9-10)
* **Duplex ultrasound:** can be useful but has limitations, particularly for detecting classic beading and is operator dependent. (gornik2019firstinternationalconsensus pages 12-14)

### 10.3 Differential diagnosis
Consensus documents emphasize excluding atherosclerosis, inflammatory vasculopathies, arterial spasm, and inherited arteriopathies that can mimic FMD. (gornik2019firstinternationalconsensus pages 2-4)

### 10.4 Genetic testing
No guideline-level recommendation for routine clinical genetic testing is supported in the retrieved excerpts. Genetic testing is used in research registries (blood sampling for genetics/biomarkers in FEIRI and PROFILE). (NCT04804683 chunk 1, NCT02961868 chunk 1)

---

## 11. Outcome / prognosis

### 11.1 Vascular complications and event risks
Major complications include aneurysm and dissection. Registry estimates include:
* US Registry: aneurysm 22.7%, dissection 28.1%. (gornik2019firstinternationalconsensus pages 9-10)
* European/International Registry: aneurysm 20.0%, dissection 3.4% (likely influenced by ascertainment/imaging differences). (gornik2019firstinternationalconsensus pages 9-10)

For intracranial aneurysm specifically, among women with FMD who had intracranial imaging, prevalence was 12.9%, and aneurysm features suggested potentially higher-risk anatomy/size distributions (e.g., ≥5 mm in 43.2% of patients with aneurysm data). (lather2017prevalenceofintracranial pages 1-2)

### 11.2 Prognostic factors
Smoking is strongly associated with intracranial aneurysm in women with FMD, suggesting a modifiable risk factor relevant to prognosis for hemorrhagic complications. (lather2017prevalenceofintracranial pages 5-6)

Formal survival/life expectancy statistics were not available in the retrieved evidence extracts. (gornik2019firstinternationalconsensus pages 2-4)

---

## 12. Treatment

### 12.1 Pharmacotherapy (medical management)
**Antiplatelet therapy:** The 2019 international consensus states that “in the absence of contraindication, antiplatelet therapy (i.e. aspirin 75–100 mg daily) is reasonable.” (gornik2019firstinternationalconsensus pages 12-14)

A 2019 neurologic systematic review similarly suggests low-dose aspirin (75–100 mg/day) is reasonable to reduce thromboembolic complications in cerebrovascular FMD, and states acute ischemic stroke care should follow standard eligibility for thrombolysis/thrombectomy. (touze2019fibromusculardysplasiaand pages 14-18)

**Blood pressure management:** The consensus advises managing blood pressure according to standard hypertension guidelines (e.g., ACC/AHA 2017, ESC/ESH), not a unique FMD-specific target in the excerpt. (gornik2019firstinternationalconsensus pages 12-14)

**MAXO suggestions:**
* Antiplatelet therapy (**MAXO:0000464**, approximate)
* Blood pressure control (**MAXO:0000933**, approximate)

(Exact MAXO IDs are provided as plausible mappings; confirm in MAXO for ontology ingestion.)

### 12.2 Endovascular/surgical interventions
Consensus excerpts and neurologic review emphasize endovascular therapy is generally reserved for selected patients, such as symptomatic stenosis despite optimal medical therapy or ruptured intracranial aneurysm; the 2019 consensus includes a protocol for catheter angiography and percutaneous angioplasty for renal FMD (protocol mentioned in abstract). (touze2019fibromusculardysplasiaand pages 1-6, gornik2019firstinternationalconsensus pages 12-14)

**MAXO suggestions:**
* Percutaneous transluminal angioplasty (**MAXO:0000503**, approximate)
* Endovascular procedure for aneurysm repair (**MAXO:0000507**, approximate)

### 12.3 Experimental / trials
Key ClinicalTrials.gov studies retrieved include:
* **NCT04804683 (FEIRI)**: recruiting registry with biosampling for genetic and biomarker discovery; target enrollment 5,000; 10-year outcome horizon. (NCT04804683 chunk 1)
* **NCT02961868 (PROFILE)**: completed prospective imaging follow-up; n=340; primary endpoint “Progression of fibromuscular dysplasia lesions confirmed by imaging” at 3 years; includes genetics (GWAS) and biomarker sampling. (NCT02961868 chunk 1)
* **NCT02799186 (DISCO)**: completed; enrollment ~200; systematic CT/MRI angiography screening for FMD in SCAD/coronary hematoma patients plus genetic sampling; includes 1-year morbi-mortality endpoint. (NCT02799186 chunk 1)

---

## 13. Prevention

### 13.1 Primary prevention
No established primary prevention exists due to unclear causation, but **smoking avoidance/cessation** is supported as likely beneficial given strong association with intracranial aneurysm among women with FMD. (lather2017prevalenceofintracranial pages 5-6)

### 13.2 Secondary prevention (screening / early detection)
Consensus recommends **one-time brain-to-pelvis imaging** (CTA or contrast-enhanced MRA) to detect additional FMD lesions, aneurysms, and dissections, which functions as secondary prevention by identifying lesions requiring surveillance or intervention. (gornik2019firstinternationalconsensus pages 12-14)

### 13.3 Tertiary prevention
Antiplatelet therapy and BP control aim to prevent thromboembolic and hypertensive complications; restriction of endovascular intervention to selected cases reflects risk–benefit balancing. (gornik2019firstinternationalconsensus pages 12-14, touze2019fibromusculardysplasiaand pages 14-18)

---

## 14. Other species / natural disease
No naturally occurring veterinary FMD analogs or cross-species transmission considerations were identified in the retrieved evidence. (gornik2019firstinternationalconsensus pages 2-4)

---

## 15. Model organisms
The strongest model-organism evidence in this retrieval set is from the 2024 UBR4 work and the 2016 PHACTR1 work:
* **Mouse:** VSMC-targeted Ubr4 knockout models with vascular histopathology and proteomics. (d’escamard2024integrativegeneregulatory pages 13-24)
* **Zebrafish:** phactr1 knockdown causing dilated vessels, suggesting subtle impaired vascular development. (kiando2016phactr1isa pages 1-2)

---

## Recent developments and real-world implementation (2023–2024 priority)

### 2024: Systems genetics / omics-driven mechanism discovery
d’Escamard et al. (Sep 2024) integrates gene regulatory networks with functional experiments in fibroblasts and VSMCs, proposing network drivers (e.g., UBR4) that may shape vascular-wall structure (elastic lamina/collagen) and immune-cell infiltration patterns—an example of translation from association genetics to experimentally testable mechanisms. (d’escamard2024integrativegeneregulatory pages 13-24)

### 2023: Implementation gap in comprehensive vascular screening
In a real-world SCAD cohort (157 patients, 2005–2019), comprehensive head-to-pelvis imaging remained low (10–18%), yet comprehensive imaging yielded much higher FMD detection (**63% vs 15%** with partial imaging). This demonstrates an implementation gap between consensus-style recommendations for broad vascular evaluation and actual clinical practice, with direct consequences for diagnosing multisite FMD and associated aneurysms. (feldbaum2023managementofspontaneous pages 3-4)

---

## Key statistics (selected)
| Cohort / source (year) | N | % women | Mean age at diagnosis | Hypertension % | Headache % | Stroke / TIA / SAH % | Multifocal vs focal % | Multivessel % | Aneurysm % | Dissection % | Key notes |
|---|---:|---:|---|---:|---:|---|---|---:|---:|---:|---|
| US Registry for FMD, per First International Consensus (2019) | 1885 analyzed | 94.7% (gornik2019firstinternationalconsensus pages 7-9) | 53.3 ± 12.8 y (gornik2019firstinternationalconsensus pages 7-9) | 67.3% (1253/1862) (gornik2019firstinternationalconsensus pages 7-9) | 69.4% (1274/1837) (gornik2019firstinternationalconsensus pages 7-9) | Stroke 10.1%; TIA 12.3%; SAH 2.2% (gornik2019firstinternationalconsensus pages 7-9) | Multifocal 76.0%; focal 2.4% (gornik2019firstinternationalconsensus pages 9-10) | 55.1% (1038/1885) (gornik2019firstinternationalconsensus pages 9-10) | 22.7% (406/1790) (gornik2019firstinternationalconsensus pages 9-10) | 28.1% (514/1828) (gornik2019firstinternationalconsensus pages 9-10) | Renal lesions found in 66.1% of imaged patients; cerebrovascular lesions in 80.4% of imaged patients; registry data likely influenced by incomplete brain-to-pelvis imaging (gornik2019firstinternationalconsensus pages 9-10) |
| European/International FMD Registry, per First International Consensus (2019) | 609 analyzed | 83.3% (gornik2019firstinternationalconsensus pages 7-9) | 45.8 ± 15.8 y (gornik2019firstinternationalconsensus pages 7-9) | 73.7% (gornik2019firstinternationalconsensus pages 7-9) | Pending / not reported in excerpt (gornik2019firstinternationalconsensus pages 7-9) | Stroke 7.7%; TIA 3.5%; SAH 3.5% (gornik2019firstinternationalconsensus pages 7-9) | Multifocal 71.9%; focal 28.1% (gornik2019firstinternationalconsensus pages 9-10) | 31.2% (190/609) (gornik2019firstinternationalconsensus pages 9-10) | 20.0% (122/609) (gornik2019firstinternationalconsensus pages 9-10) | 3.4% (21/609) (gornik2019firstinternationalconsensus pages 9-10) | Renal lesions in 91.9% of imaged patients; cerebrovascular lesions in 58.6% of imaged patients; lower dissection prevalence than US registry likely reflects ascertainment/imaging differences (gornik2019firstinternationalconsensus pages 9-10, gornik2019firstinternationalconsensus pages 7-9) |
| ARCADIA-POL cohort, Hypertension (2020) | 129 | 80.6% (warcholcelinska2020geneticstudyof pages 1-2) | 42.7 ± 14.2 y (warcholcelinska2020geneticstudyof pages 1-2) | 87.6% (113/129) (warcholcelinska2020geneticstudyof pages 1-2) | 38.8% (warcholcelinska2020geneticstudyof pages 1-2) | Stroke 9.3%; TIA not reported; SAH not reported (warcholcelinska2020geneticstudyof pages 1-2) | Multifocal 85.3%; focal not reported separately (warcholcelinska2020geneticstudyof pages 1-2) | 32.6% multisite disease (≥2 vascular beds) (warcholcelinska2020geneticstudyof pages 1-2) | 24.0% (31/129) (warcholcelinska2020geneticstudyof pages 1-2) | 12.4% (16/129) (warcholcelinska2020geneticstudyof pages 1-2) | Vascular beds involved: renal 84.5%, cerebrovascular 26.4%, visceral 15.5%, lower extremity 11.6%; pulsatile tinnitus 15.5%; median affected beds 1 (IQR 1–2) (warcholcelinska2020geneticstudyof pages 1-2) |
| Women with FMD and intracranial imaging, US Registry / Lather et al. JAMA Neurology (2017) | 669 imaged women | 100% women by study design (lather2017prevalenceofintracranial pages 1-2) | Not reported in excerpt | Not reported for IA subgroup prevalence analysis | Not reported for IA subgroup prevalence analysis | Prior SAH excluded UIA prevalence gives 11.1%; among women with IA, SAH more common (18.0% vs 1.5%) (lather2017prevalenceofintracranial pages 5-6, lather2017prevalenceofintracranial pages 3-4) | Not reported | Not reported | Intracranial aneurysm prevalence 12.9% (86/669; 95% CI 10.3–15.9); unruptured IA 11.1% (66/593) (lather2017prevalenceofintracranial pages 3-4, lather2017prevalenceofintracranial pages 1-2) | Not reported overall; arterial dissection associated in table excerpts (lather2017prevalenceofintracranial pages 3-4) | Smoking strongly associated with IA: 53.8% with IA vs 28.9% without; multiple aneurysms in 30.2%; supports one-time intracranial aneurysm screening in FMD workup (lather2017prevalenceofintracranial pages 5-6, lather2017prevalenceofintracranial pages 1-2, gornik2019firstinternationalconsensus pages 12-14) |


*Table: This table summarizes core epidemiology, vascular-bed involvement, and complication frequencies for fibromuscular dysplasia across major registry and cohort sources. It is useful for comparing how phenotype distributions and vascular complications vary by study design and ascertainment.*

---

## Limitations of this report (evidence-bound)
1) ICD-10/ICD-11, MeSH, OMIM, and Orphanet identifiers were not present in the retrieved full-text evidence; thus these identifiers are flagged as not found rather than inferred. (gornik2019firstinternationalconsensus pages 2-4)
2) Incidence estimates and formal QoL metrics were not available in the retrieved excerpts.
3) Some mechanistic pathway statements (e.g., endothelin/prostacyclin/TGF-β) are referenced in reviews, but the most direct mechanistic evidence in this evidence set comes from GWAS pathway mapping and the 2024 UBR4 systems-genetics study. (georges2021geneticinvestigationof pages 1-2, d’escamard2024integrativegeneregulatory pages 13-24)

---

## Key references (URLs and publication dates from retrieved evidence)
* Gornik HL et al. **First International Consensus on the diagnosis and management of fibromuscular dysplasia**. *Vascular Medicine*. **Jan 2019**. https://doi.org/10.1177/1358863x18821816 (gornik2019firstinternationalconsensus pages 12-14)
* d’Escamard V et al. **Integrative gene regulatory network analysis discloses key driver genes of fibromuscular dysplasia**. *Nature Cardiovascular Research*. **Sep 2024**. https://doi.org/10.1038/s44161-024-00533-w (d’escamard2024integrativegeneregulatory pages 1-13)
* Huart J et al. **From fibromuscular dysplasia to arterial dissection and back**. *American Journal of Hypertension*. **Jun 2023**. https://doi.org/10.1093/ajh/hpad056 (huart2023fromfibromusculardysplasia pages 1-2)
* Feldbaum E et al. **Management of spontaneous coronary artery dissection: Trends over time**. *Vascular Medicine*. **Apr 2023**. https://doi.org/10.1177/1358863x231155305 (feldbaum2023managementofspontaneous pages 3-4)
* Lather HD et al. **Prevalence of Intracranial Aneurysm in Women With Fibromuscular Dysplasia**. *JAMA Neurology*. Published online **2017-07-17**; Issue **Sep 2017**. https://doi.org/10.1001/jamaneurol.2017.1333 (lather2017prevalenceofintracranial pages 1-2)
* Touzé E et al. **Fibromuscular Dysplasia and Its Neurologic Manifestations: A Systematic Review**. *JAMA Neurology*. **Feb 2019**. https://doi.org/10.1001/jamaneurol.2018.2848 (touze2019fibromusculardysplasiaand pages 1-6)
* Georges A et al. **Genetic investigation of fibromuscular dysplasia identifies risk loci and shared genetics with common cardiovascular diseases**. *Nature Communications*. **May 2021**. https://doi.org/10.1038/s41467-021-26174-2 (georges2021geneticinvestigationof pages 1-2)
* Kiando SR et al. **PHACTR1 Is a Genetic Susceptibility Locus for Fibromuscular Dysplasia**. *PLOS Genetics*. **Oct 2016**. https://doi.org/10.1371/journal.pgen.1006367 (kiando2016phactr1isa pages 1-2)
* ARCADIA/PROFILE trial record **NCT02961868**. ClinicalTrials.gov. (Start Nov 2009; completed Jan 2018). (NCT02961868 chunk 1)
* FEIRI registry record **NCT04804683**. ClinicalTrials.gov. (Posted Mar 2021; recruiting). (NCT04804683 chunk 1)


References

1. (gornik2019firstinternationalconsensus pages 9-10): Heather L Gornik, Alexandre Persu, David Adlam, Lucas S Aparicio, Michel Azizi, Marion Boulanger, Rosa Maria Bruno, Peter de Leeuw, Natalia Fendrikova-Mahlay, James Froehlich, Santhi K Ganesh, Bruce H Gray, Cathlin Jamison, Andrzej Januszewicz, Xavier Jeunemaitre, Daniella Kadian-Dodov, Esther SH Kim, Jason C Kovacic, Pamela Mace, Alberto Morganti, Aditya Sharma, Andrew M Southerland, Emmanuel Touzé, Patricia van der Niepen, Jiguang Wang, Ido Weinberg, Scott Wilson, Jeffrey W Olin, and Pierre-Francois Plouin. First international consensus on the diagnosis and management of fibromuscular dysplasia. Vascular Medicine, 24:164-189, Jan 2019. URL: https://doi.org/10.1177/1358863x18821816, doi:10.1177/1358863x18821816. This article has 561 citations and is from a peer-reviewed journal.

2. (persu2022currentprogressin pages 2-3): Alexandre Persu, Piotr Dobrowolski, Heather L Gornik, Jeffrey W Olin, David Adlam, Michel Azizi, Pierre Boutouyrie, Rosa Maria Bruno, Marion Boulanger, Jean-Baptiste Demoulin, Santhi K Ganesh, Tomasz J. Guzik, Magdalena Januszewicz, Jason C Kovacic, Mariusz Kruk, Peter de Leeuw, Bart L Loeys, Marco Pappaccogli, Melanie H A M Perik, Emmanuel Touzé, Patricia Van der Niepen, Daan J L Van Twist, Ewa Warchoł-Celińska, Aleksander Prejbisz, and Andrzej Januszewicz. Current progress in clinical, molecular, and genetic aspects of adult fibromuscular dysplasia. Cardiovascular research, 118:65-83, Mar 2022. URL: https://doi.org/10.1093/cvr/cvab086, doi:10.1093/cvr/cvab086. This article has 52 citations and is from a domain leading peer-reviewed journal.

3. (georges2021geneticinvestigationof pages 1-2): A. Georges, Min-Lee Yang, T. Berrandou, Mark K. Bakker, O. Dikilitas, S. Kiando, Lijiang Ma, Benjamin A. Satterfield, Sebanti Sengupta, Mengyao Yu, J. Deleuze, D. Dupré, Kristina L. Hunker, Sergiy Kyryachenko, Lu Liu, Ines Sayoud-Sadeg, L. Amar, C. Brummett, D. Coleman, Valentina d’Escamard, P. de Leeuw, Natalia Fendrikova-Mahlay, Daniella Kadian-Dodov, Jun Z. Li, A. Lorthioir, M. Pappaccogli, A. Prejbisz, W. Śmigielski, J. Stanley, M. Zawistowski, Xiang Zhou, S. Zöllner, P. de Leeuw, P. Amouyel, M. D. De Buyzere, S. Debette, P. Dobrowolski, W. Drygas, H. Gornik, J. Olin, J. Piwoński, E. Rietzschel, Y. Ruigrok, M. Vikkula, Ewa Warchol Celinska, A. Januszewicz, I. Kullo, M. Azizi, X. Jeunemaître, A. Persu, J. Kovacic, S. Ganesh, and N. Bouatia-Naji. Genetic investigation of fibromuscular dysplasia identifies risk loci and shared genetics with common cardiovascular diseases. Nature Communications, 12:186-187, May 2021. URL: https://doi.org/10.1038/s41467-021-26174-2, doi:10.1038/s41467-021-26174-2. This article has 80 citations and is from a highest quality peer-reviewed journal.

4. (d’escamard2024integrativegeneregulatory pages 1-13): Valentina d’Escamard, Daniella Kadian-Dodov, Lijiang Ma, Sizhao Lu, Annette King, Yang Xu, Shouneng Peng, Bhargravi V′Gangula, Yu Zhou, Allison Thomas, Katherine C. Michelis, Emir Bander, Rihab Bouchareb, Adrien Georges, Aya Nomura-Kitabayashi, Robert J. Wiener, Kevin D. Costa, Elena Chepurko, Vadim Chepurko, Marika Fava, Temo Barwari, Anelechi Anyanwu, Farzan Filsoufi, Sander Florman, Nabila Bouatia-Naji, Lukas E. Schmidt, Manuel Mayr, Michael G. Katz, Ke Hao, Mary C. M. Weiser-Evans, Johan L. M. Björkegren, Jeffrey W. Olin, and Jason C. Kovacic. Integrative gene regulatory network analysis discloses key driver genes of fibromuscular dysplasia. Nature Cardiovascular Research, 3:1098-1122, Sep 2024. URL: https://doi.org/10.1038/s44161-024-00533-w, doi:10.1038/s44161-024-00533-w. This article has 9 citations and is from a peer-reviewed journal.

5. (monaco2018genomicsoffibromuscular pages 1-3): Silvia Di Monaco, Adrien Georges, Jean-Philippe Lengelé, Miikka Vikkula, and Alexandre Persu. Genomics of fibromuscular dysplasia. International Journal of Molecular Sciences, 19:1526, May 2018. URL: https://doi.org/10.3390/ijms19051526, doi:10.3390/ijms19051526. This article has 51 citations.

6. (gornik2019firstinternationalconsensus pages 2-4): Heather L Gornik, Alexandre Persu, David Adlam, Lucas S Aparicio, Michel Azizi, Marion Boulanger, Rosa Maria Bruno, Peter de Leeuw, Natalia Fendrikova-Mahlay, James Froehlich, Santhi K Ganesh, Bruce H Gray, Cathlin Jamison, Andrzej Januszewicz, Xavier Jeunemaitre, Daniella Kadian-Dodov, Esther SH Kim, Jason C Kovacic, Pamela Mace, Alberto Morganti, Aditya Sharma, Andrew M Southerland, Emmanuel Touzé, Patricia van der Niepen, Jiguang Wang, Ido Weinberg, Scott Wilson, Jeffrey W Olin, and Pierre-Francois Plouin. First international consensus on the diagnosis and management of fibromuscular dysplasia. Vascular Medicine, 24:164-189, Jan 2019. URL: https://doi.org/10.1177/1358863x18821816, doi:10.1177/1358863x18821816. This article has 561 citations and is from a peer-reviewed journal.

7. (huart2023fromfibromusculardysplasia pages 1-2): Justine Huart, Maria S Stoenoiu, Marialuisa Zedde, Rosario Pascarella, David Adlam, and Alexandre Persu. From fibromuscular dysplasia to arterial dissection and back. American journal of hypertension, 36:573-585, Jun 2023. URL: https://doi.org/10.1093/ajh/hpad056, doi:10.1093/ajh/hpad056. This article has 21 citations and is from a peer-reviewed journal.

8. (gornik2019firstinternationalconsensus media 968288f3): Heather L Gornik, Alexandre Persu, David Adlam, Lucas S Aparicio, Michel Azizi, Marion Boulanger, Rosa Maria Bruno, Peter de Leeuw, Natalia Fendrikova-Mahlay, James Froehlich, Santhi K Ganesh, Bruce H Gray, Cathlin Jamison, Andrzej Januszewicz, Xavier Jeunemaitre, Daniella Kadian-Dodov, Esther SH Kim, Jason C Kovacic, Pamela Mace, Alberto Morganti, Aditya Sharma, Andrew M Southerland, Emmanuel Touzé, Patricia van der Niepen, Jiguang Wang, Ido Weinberg, Scott Wilson, Jeffrey W Olin, and Pierre-Francois Plouin. First international consensus on the diagnosis and management of fibromuscular dysplasia. Vascular Medicine, 24:164-189, Jan 2019. URL: https://doi.org/10.1177/1358863x18821816, doi:10.1177/1358863x18821816. This article has 561 citations and is from a peer-reviewed journal.

9. (zedde2025fibromusculardysplasiaand pages 17-17): Marialuisa Zedde, Maria Simona Stoenoiu, Alexandre Persu, and Rosario Pascarella. Fibromuscular dysplasia and intracranial aneurysms: a narrative review of a dangerous and underestimated association. Journal of Clinical Medicine, 14:8080, Nov 2025. URL: https://doi.org/10.3390/jcm14228080, doi:10.3390/jcm14228080. This article has 0 citations.

10. (touze2019fibromusculardysplasiaand pages 14-18): Emmanuel Touzé, Andrew M. Southerland, Marion Boulanger, Paul-Emile Labeyrie, Michel Azizi, Nabila Bouatia-Naji, Stéphanie Debette, Heather L. Gornik, Shazam M. Hussain, Xavier Jeunemaitre, Julien Joux, Adam Kirton, Claire Le Hello, Jennifer J. Majersik, J. Mocco, Alexandre Persu, Aditya Sharma, Bradford B. Worrall, Jeffrey W. Olin, and Pierre-François Plouin. Fibromuscular dysplasia and its neurologic manifestations: a systematic review. JAMA Neurology, 76:217–226, Feb 2019. URL: https://doi.org/10.1001/jamaneurol.2018.2848, doi:10.1001/jamaneurol.2018.2848. This article has 94 citations and is from a highest quality peer-reviewed journal.

11. (gornik2019firstinternationalconsensus pages 7-9): Heather L Gornik, Alexandre Persu, David Adlam, Lucas S Aparicio, Michel Azizi, Marion Boulanger, Rosa Maria Bruno, Peter de Leeuw, Natalia Fendrikova-Mahlay, James Froehlich, Santhi K Ganesh, Bruce H Gray, Cathlin Jamison, Andrzej Januszewicz, Xavier Jeunemaitre, Daniella Kadian-Dodov, Esther SH Kim, Jason C Kovacic, Pamela Mace, Alberto Morganti, Aditya Sharma, Andrew M Southerland, Emmanuel Touzé, Patricia van der Niepen, Jiguang Wang, Ido Weinberg, Scott Wilson, Jeffrey W Olin, and Pierre-Francois Plouin. First international consensus on the diagnosis and management of fibromuscular dysplasia. Vascular Medicine, 24:164-189, Jan 2019. URL: https://doi.org/10.1177/1358863x18821816, doi:10.1177/1358863x18821816. This article has 561 citations and is from a peer-reviewed journal.

12. (kiando2016phactr1isa pages 1-2): Soto Romuald Kiando, Nathan R. Tucker, Luis-Jaime Castro-Vega, Alexander Katz, Valentina D’Escamard, Cyrielle Tréard, Daniel Fraher, Juliette Albuisson, Daniella Kadian-Dodov, Zi Ye, Erin Austin, Min-Lee Yang, Kristina Hunker, Cristina Barlassina, Daniele Cusi, Pilar Galan, Jean-Philippe Empana, Xavier Jouven, Anne-Paule Gimenez-Roqueplo, Patrick Bruneval, Esther Soo Hyun Kim, Jeffrey W. Olin, Heather L. Gornik, Michel Azizi, Pierre-François Plouin, Patrick T. Ellinor, Iftikhar J. Kullo, David J. Milan, Santhi K. Ganesh, Pierre Boutouyrie, Jason C. Kovacic, Xavier Jeunemaitre, and Nabila Bouatia-Naji. Phactr1 is a genetic susceptibility locus for fibromuscular dysplasia supporting its complex genetic pattern of inheritance. PLOS Genetics, 12:e1006367, Oct 2016. URL: https://doi.org/10.1371/journal.pgen.1006367, doi:10.1371/journal.pgen.1006367. This article has 224 citations and is from a domain leading peer-reviewed journal.

13. (georges2022thecomplexgenetic pages 11-13): Adrien Georges and Nabila Bouatia-Naji. The complex genetic basis of fibromuscular dysplasia, a systemic arteriopathy associated with multiple forms of cardiovascular disease. Clinical Science (London, England : 1979), 136:1241-1255, Aug 2022. URL: https://doi.org/10.1042/cs20210990, doi:10.1042/cs20210990. This article has 18 citations.

14. (lather2017prevalenceofintracranial pages 5-6): Henry D. Lather, Heather L. Gornik, Jeffrey W. Olin, Xiaokui Gu, Steven T. Heidt, Esther S. H. Kim, Daniella Kadian-Dodov, Aditya Sharma, Bruce Gray, Michael R. Jaff, Yung-Wei Chi, Pamela Mace, Eva Kline-Rogers, and James B. Froehlich. Prevalence of intracranial aneurysm in women with fibromuscular dysplasia: a report from the us registry for fibromuscular dysplasia. JAMA Neurology, 74:1081–1087, Sep 2017. URL: https://doi.org/10.1001/jamaneurol.2017.1333, doi:10.1001/jamaneurol.2017.1333. This article has 86 citations and is from a highest quality peer-reviewed journal.

15. (lather2017prevalenceofintracranial pages 1-2): Henry D. Lather, Heather L. Gornik, Jeffrey W. Olin, Xiaokui Gu, Steven T. Heidt, Esther S. H. Kim, Daniella Kadian-Dodov, Aditya Sharma, Bruce Gray, Michael R. Jaff, Yung-Wei Chi, Pamela Mace, Eva Kline-Rogers, and James B. Froehlich. Prevalence of intracranial aneurysm in women with fibromuscular dysplasia: a report from the us registry for fibromuscular dysplasia. JAMA Neurology, 74:1081–1087, Sep 2017. URL: https://doi.org/10.1001/jamaneurol.2017.1333, doi:10.1001/jamaneurol.2017.1333. This article has 86 citations and is from a highest quality peer-reviewed journal.

16. (gornik2019firstinternationalconsensus media 561bacbf): Heather L Gornik, Alexandre Persu, David Adlam, Lucas S Aparicio, Michel Azizi, Marion Boulanger, Rosa Maria Bruno, Peter de Leeuw, Natalia Fendrikova-Mahlay, James Froehlich, Santhi K Ganesh, Bruce H Gray, Cathlin Jamison, Andrzej Januszewicz, Xavier Jeunemaitre, Daniella Kadian-Dodov, Esther SH Kim, Jason C Kovacic, Pamela Mace, Alberto Morganti, Aditya Sharma, Andrew M Southerland, Emmanuel Touzé, Patricia van der Niepen, Jiguang Wang, Ido Weinberg, Scott Wilson, Jeffrey W Olin, and Pierre-Francois Plouin. First international consensus on the diagnosis and management of fibromuscular dysplasia. Vascular Medicine, 24:164-189, Jan 2019. URL: https://doi.org/10.1177/1358863x18821816, doi:10.1177/1358863x18821816. This article has 561 citations and is from a peer-reviewed journal.

17. (touze2019fibromusculardysplasiaand pages 6-11): Emmanuel Touzé, Andrew M. Southerland, Marion Boulanger, Paul-Emile Labeyrie, Michel Azizi, Nabila Bouatia-Naji, Stéphanie Debette, Heather L. Gornik, Shazam M. Hussain, Xavier Jeunemaitre, Julien Joux, Adam Kirton, Claire Le Hello, Jennifer J. Majersik, J. Mocco, Alexandre Persu, Aditya Sharma, Bradford B. Worrall, Jeffrey W. Olin, and Pierre-François Plouin. Fibromuscular dysplasia and its neurologic manifestations: a systematic review. JAMA Neurology, 76:217–226, Feb 2019. URL: https://doi.org/10.1001/jamaneurol.2018.2848, doi:10.1001/jamaneurol.2018.2848. This article has 94 citations and is from a highest quality peer-reviewed journal.

18. (warcholcelinska2020geneticstudyof pages 1-2): Ewa Warchol-Celinska, Takiy Berrandou, Aleksander Prejbisz, Adrien Georges, Delia Dupré, Magdalena Januszewicz, Elzbieta Florczak, Katarzyna Jozwik-Plebanek, Piotr Dobrowolski, Witold Smigielski, Wojciech Drygas, Jacek Kadziela, Adam Witkowski, Marek Kabat, Malgorzata Szczerbo-Trojanowska, Marco Pappaccogli, Alexandre Persu, Xavier Jeunemaitre, Andrzej Januszewicz, and Nabila Bouatia-Naji. Genetic study of <i>phactr1</i> and fibromuscular dysplasia, meta-analysis and effects on clinical features of patients. Hypertension, Jul 2020. URL: https://doi.org/10.1161/hypertensionaha.120.14793, doi:10.1161/hypertensionaha.120.14793. This article has 19 citations and is from a domain leading peer-reviewed journal.

19. (touze2019fibromusculardysplasiaand pages 11-14): Emmanuel Touzé, Andrew M. Southerland, Marion Boulanger, Paul-Emile Labeyrie, Michel Azizi, Nabila Bouatia-Naji, Stéphanie Debette, Heather L. Gornik, Shazam M. Hussain, Xavier Jeunemaitre, Julien Joux, Adam Kirton, Claire Le Hello, Jennifer J. Majersik, J. Mocco, Alexandre Persu, Aditya Sharma, Bradford B. Worrall, Jeffrey W. Olin, and Pierre-François Plouin. Fibromuscular dysplasia and its neurologic manifestations: a systematic review. JAMA Neurology, 76:217–226, Feb 2019. URL: https://doi.org/10.1001/jamaneurol.2018.2848, doi:10.1001/jamaneurol.2018.2848. This article has 94 citations and is from a highest quality peer-reviewed journal.

20. (lather2017prevalenceofintracranial pages 3-4): Henry D. Lather, Heather L. Gornik, Jeffrey W. Olin, Xiaokui Gu, Steven T. Heidt, Esther S. H. Kim, Daniella Kadian-Dodov, Aditya Sharma, Bruce Gray, Michael R. Jaff, Yung-Wei Chi, Pamela Mace, Eva Kline-Rogers, and James B. Froehlich. Prevalence of intracranial aneurysm in women with fibromuscular dysplasia: a report from the us registry for fibromuscular dysplasia. JAMA Neurology, 74:1081–1087, Sep 2017. URL: https://doi.org/10.1001/jamaneurol.2017.1333, doi:10.1001/jamaneurol.2017.1333. This article has 86 citations and is from a highest quality peer-reviewed journal.

21. (d’escamard2024integrativegeneregulatory pages 13-24): Valentina d’Escamard, Daniella Kadian-Dodov, Lijiang Ma, Sizhao Lu, Annette King, Yang Xu, Shouneng Peng, Bhargravi V′Gangula, Yu Zhou, Allison Thomas, Katherine C. Michelis, Emir Bander, Rihab Bouchareb, Adrien Georges, Aya Nomura-Kitabayashi, Robert J. Wiener, Kevin D. Costa, Elena Chepurko, Vadim Chepurko, Marika Fava, Temo Barwari, Anelechi Anyanwu, Farzan Filsoufi, Sander Florman, Nabila Bouatia-Naji, Lukas E. Schmidt, Manuel Mayr, Michael G. Katz, Ke Hao, Mary C. M. Weiser-Evans, Johan L. M. Björkegren, Jeffrey W. Olin, and Jason C. Kovacic. Integrative gene regulatory network analysis discloses key driver genes of fibromuscular dysplasia. Nature Cardiovascular Research, 3:1098-1122, Sep 2024. URL: https://doi.org/10.1038/s44161-024-00533-w, doi:10.1038/s44161-024-00533-w. This article has 9 citations and is from a peer-reviewed journal.

22. (touze2019fibromusculardysplasiaand pages 24-30): Emmanuel Touzé, Andrew M. Southerland, Marion Boulanger, Paul-Emile Labeyrie, Michel Azizi, Nabila Bouatia-Naji, Stéphanie Debette, Heather L. Gornik, Shazam M. Hussain, Xavier Jeunemaitre, Julien Joux, Adam Kirton, Claire Le Hello, Jennifer J. Majersik, J. Mocco, Alexandre Persu, Aditya Sharma, Bradford B. Worrall, Jeffrey W. Olin, and Pierre-François Plouin. Fibromuscular dysplasia and its neurologic manifestations: a systematic review. JAMA Neurology, 76:217–226, Feb 2019. URL: https://doi.org/10.1001/jamaneurol.2018.2848, doi:10.1001/jamaneurol.2018.2848. This article has 94 citations and is from a highest quality peer-reviewed journal.

23. (NCT02961868 chunk 1):  Cohort Follow-up of Patients With Renal or Craniocervical Fibromuscular Dysplasia. Assistance Publique - Hôpitaux de Paris. 2009. ClinicalTrials.gov Identifier: NCT02961868

24. (gornik2019firstinternationalconsensus pages 12-14): Heather L Gornik, Alexandre Persu, David Adlam, Lucas S Aparicio, Michel Azizi, Marion Boulanger, Rosa Maria Bruno, Peter de Leeuw, Natalia Fendrikova-Mahlay, James Froehlich, Santhi K Ganesh, Bruce H Gray, Cathlin Jamison, Andrzej Januszewicz, Xavier Jeunemaitre, Daniella Kadian-Dodov, Esther SH Kim, Jason C Kovacic, Pamela Mace, Alberto Morganti, Aditya Sharma, Andrew M Southerland, Emmanuel Touzé, Patricia van der Niepen, Jiguang Wang, Ido Weinberg, Scott Wilson, Jeffrey W Olin, and Pierre-Francois Plouin. First international consensus on the diagnosis and management of fibromuscular dysplasia. Vascular Medicine, 24:164-189, Jan 2019. URL: https://doi.org/10.1177/1358863x18821816, doi:10.1177/1358863x18821816. This article has 561 citations and is from a peer-reviewed journal.

25. (NCT04804683 chunk 1): PERSU Alexandre. European/International FMD Registry and Initiative. Cliniques universitaires Saint-Luc- Université Catholique de Louvain. 2021. ClinicalTrials.gov Identifier: NCT04804683

26. (touze2019fibromusculardysplasiaand pages 1-6): Emmanuel Touzé, Andrew M. Southerland, Marion Boulanger, Paul-Emile Labeyrie, Michel Azizi, Nabila Bouatia-Naji, Stéphanie Debette, Heather L. Gornik, Shazam M. Hussain, Xavier Jeunemaitre, Julien Joux, Adam Kirton, Claire Le Hello, Jennifer J. Majersik, J. Mocco, Alexandre Persu, Aditya Sharma, Bradford B. Worrall, Jeffrey W. Olin, and Pierre-François Plouin. Fibromuscular dysplasia and its neurologic manifestations: a systematic review. JAMA Neurology, 76:217–226, Feb 2019. URL: https://doi.org/10.1001/jamaneurol.2018.2848, doi:10.1001/jamaneurol.2018.2848. This article has 94 citations and is from a highest quality peer-reviewed journal.

27. (NCT02799186 chunk 1):  The Study of the Prevalence Fibromuscular Dysplasia in Patient With Haematoma or Spontaneous Coronary Artery Dissection.. University Hospital, Clermont-Ferrand. 2016. ClinicalTrials.gov Identifier: NCT02799186

28. (feldbaum2023managementofspontaneous pages 3-4): Elliot Feldbaum, Elizabeth W Thompson, Tessa S Cook, Monika Sanghavi, Robert L Wilensky, Paul N Fiorilli, and Jennifer Lewey. Management of spontaneous coronary artery dissection: trends over time. Vascular Medicine (London, England), 28:131-138, Apr 2023. URL: https://doi.org/10.1177/1358863x231155305, doi:10.1177/1358863x231155305. This article has 31 citations.