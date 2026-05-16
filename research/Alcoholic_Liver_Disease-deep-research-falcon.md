---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T15:22:37.681743'
end_time: '2026-05-12T15:45:02.476081'
duration_seconds: 1344.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alcoholic Liver Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
artifact_count: 1
artifacts:
- filename: artifact-00.md
  path: Alcoholic_Liver_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alcoholic Liver Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Alcoholic Liver Disease** covering all of the
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
- **Disease Name:** Alcoholic Liver Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Alcoholic Liver Disease** covering all of the
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


# Comprehensive Research Report: Alcoholic Liver Disease (Alcohol-Associated Liver Disease)

## Target disease
- **Disease name (preferred in recent literature):** Alcohol-associated liver disease (**ALD**) (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, mackowiak2024alcoholassociatedliverdisease pages 1-2)
- **Legacy/related terms:** alcoholic liver disease; alcohol-related liver disease; ArLD (hong2024alcoholrelatedliverdisease pages 1-2, alvaradotapias2024alcoholassociatedliverdisease pages 1-3)
- **Disease category:** complex / multifactorial exposure-related disease (alcohol plus modifiers) (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, israelsenUnknownyearmetaldfromconcept pages 7-10)
- **MONDO ID:** Not identified in the retrieved evidence set (knowledge-base crosswalk needed).

## 1. Disease information (concepts, identifiers, synonyms)

### 1.1 Concise overview and spectrum definition
Alcohol-associated liver disease (ALD) is a spectrum of liver injury caused by chronic harmful alcohol exposure, ranging from **steatosis** to **steatohepatitis**, progressive **fibrosis**, **cirrhosis**, and **hepatocellular carcinoma (HCC)** (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, mackowiak2024alcoholassociatedliverdisease pages 1-2). Alcohol-associated hepatitis (AH) is an acute, severe inflammatory manifestation within this spectrum, described as presenting with **sudden jaundice and liver failure** (alvaradotapias2024alcoholassociatedliverdisease pages 1-3).

### 1.2 Key identifiers / coding
- **ICD-10:** Alcoholic liver disease is coded under **K70.*** (examples explicitly listed in retrieved sources: **K70.0–K70.4, K70.9**) (manthey2025identifyinglevelsof pages 1-2, kubina2025meta‐analysiseffectsof pages 23-23).
- **ICD-11 / MeSH / OMIM / Orphanet:** Not extracted from the retrieved evidence set (additional targeted database lookup required). An expert consensus statement discusses **ICD-11 AUD criteria** (dependence requires “2 or more of 3 symptoms”) but does not provide ICD-11 liver-disease codes (lee2024designingclinicaltrials pages 3-5).

### 1.3 Current nomenclature: ALD within the 2023 “steatotic liver disease (SLD)” framework
Recent multisociety consensus reframed fatty liver disorders under **SLD** and subclassified into **MASLD**, **MetALD (MASLD + increased alcohol)**, and **ALD** (lee2024nationalprevalenceestimates pages 1-2, alvaradotapias2024alcoholassociatedliverdisease pages 1-3). A Nature Reviews Gastroenterology & Hepatology expert panel describes Delphi thresholds defining ALD as alcohol consumption exceeding **420 g/week (men)** or **350 g/week (women)** and MetALD as intermediate alcohol exposure ranges (lee2024designingclinicaltrials pages 3-5).

### 1.4 Aggregated resource vs individual patient evidence
Most disease definitions, staging concepts, and global burden estimates in this report come from **aggregated disease-level resources** (reviews and Global Burden of Disease [GBD] analyses) (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, danpanichkul2025globalepidemiologyof pages 1-5). Administrative coding use-cases reflect **EHR-derived** approaches based on ICD-10 codes (manthey2025identifyinglevelsof pages 1-2).

| Concept | Preferred term / definition | Common synonyms / legacy names | ICD-10 / coding | ICD-11 / AUD note | NHANES prevalence under 2023 SLD nomenclature | Notes (URL; publication date) |
|---|---|---|---|---|---|---|
| Disease entity | **Alcohol-associated liver disease (ALD)** is the current preferred term in recent hepatology literature; within the 2023 steatotic liver disease (SLD) framework, ALD is a subclass of SLD distinct from MASLD and MetALD (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, lee2024designingclinicaltrials pages 3-5) | Alcoholic liver disease; alcohol-related liver disease; ArLD; ALD (legacy and regional usage varies) (hong2024alcoholrelatedliverdisease pages 1-2, alvaradotapias2024alcoholassociatedliverdisease pages 1-3) | ICD-10 alcoholic liver disease code family **K70.***; examples cited in available sources include **K70.0–K70.4, K70.9** (manthey2025identifyinglevelsof pages 1-2, kubina2025meta‐analysiseffectsof pages 23-23) | Expert consensus paper notes ICD-11 criteria for alcohol dependence/AUD require **2 or more of 3 symptoms**; used as clinical context rather than liver-disease code mapping (lee2024designingclinicaltrials pages 3-5) | Not a prevalence row by itself | Alvarado-Tapias et al. 2024: https://doi.org/10.3350/cmh.2024.0709 ; Oct 2024. Lee et al. 2024 consensus statement: https://doi.org/10.1038/s41575-024-00936-x ; Jun 2024. |
| SLD umbrella term | **Steatotic liver disease (SLD)** is the umbrella nomenclature adopted by multisociety consensus, encompassing MASLD, MetALD, ALD, and etiology-specific/cryptogenic SLD (lee2024nationalprevalenceestimates pages 1-2, alvaradotapias2024alcoholassociatedliverdisease pages 1-3) | Fatty liver disease spectrum (legacy framing) (lee2024designingclinicaltrials pages 3-5, alvaradotapias2024alcoholassociatedliverdisease pages 1-3) | No specific ICD-10 range provided in available evidence for SLD umbrella term | Delphi consensus on future ICD harmonization for SLD published, but no explicit ICD-11 liver-code mapping provided in available evidence (lee2024designingclinicaltrials pages 3-5) | **34.2%** (95% CI **31.9%–36.5%**) (lee2024nationalprevalenceestimates pages 1-2) | Lee et al. 2024 NHANES analysis: https://doi.org/10.1097/hep.0000000000000604 ; Sep 2024. |
| Metabolic subclass | **Metabolic dysfunction-associated steatotic liver disease (MASLD)** (lee2024designingclinicaltrials pages 3-5, lee2024nationalprevalenceestimates pages 1-2) | NAFLD showed ~99% overlap with MASLD in NHANES analysis (lee2024nationalprevalenceestimates pages 1-2) | No specific ICD-10 range provided in available evidence | In trial-consensus context, alcohol thresholds help distinguish MASLD from MetALD/ALD (lee2024designingclinicaltrials pages 3-5) | **31.3%** (95% CI **29.2%–33.4%**) (lee2024nationalprevalenceestimates pages 1-2) | Lee et al. 2024 NHANES analysis: https://doi.org/10.1097/hep.0000000000000604 ; Sep 2024. |
| Overlap subclass | **MetALD** = MASLD plus increased alcohol intake; consensus thresholds cited as women **140–350 g/week** and men **210–420 g/week** in one expert statement (lee2024designingclinicaltrials pages 3-5) | Metabolic dysfunction- and alcohol-associated liver disease; metabolic and alcohol-associated liver disease (alvaradotapias2024alcoholassociatedliverdisease pages 1-3) | No specific ICD-10 range provided in available evidence | Relevant as a nomenclature and trial-stratification category rather than a distinct ICD-11 code in available evidence (lee2024designingclinicaltrials pages 3-5) | **2.0%** (95% CI **1.6%–2.9%**) (lee2024nationalprevalenceestimates pages 1-2) | Lee et al. 2024 NHANES analysis: https://doi.org/10.1097/hep.0000000000000604 ; Sep 2024. Lee et al. 2024 consensus statement: https://doi.org/10.1038/s41575-024-00936-x ; Jun 2024. |
| Alcohol subclass | **ALD** within SLD nomenclature; Delphi/expert statement defined ALD as alcohol consumption exceeding **420 g/week (men)** or **350 g/week (women)**, with or without cardiometabolic risk factors (lee2024designingclinicaltrials pages 3-5) | Alcohol-associated liver disease; alcoholic liver disease; alcohol-related liver disease (hong2024alcoholrelatedliverdisease pages 1-2, alvaradotapias2024alcoholassociatedliverdisease pages 1-3) | ICD-10 **K70.*** family applies to alcoholic liver disease diagnoses in administrative coding (manthey2025identifyinglevelsof pages 1-2, kubina2025meta‐analysiseffectsof pages 23-23) | ICD-11 AUD/dependence criteria mentioned in consensus/trial-design paper; no explicit ICD-11 ALD code supplied in available evidence (lee2024designingclinicaltrials pages 3-5) | **0.7%** (95% CI **0.5%–0.9%**) (lee2024nationalprevalenceestimates pages 1-2) | Lee et al. 2024 NHANES analysis: https://doi.org/10.1097/hep.0000000000000604 ; Sep 2024. Manthey et al. 2025 ICD-10 EHR usage: https://doi.org/10.1186/s13011-025-00670-w ; Sep 2025. |
| Administrative/EHR coding note | In EHR work, severe alcohol-related disease burden category explicitly included alcoholic liver disease diagnoses | Alcoholic liver cirrhosis and related alcohol-specific organ disease codes in EHR severity work (manthey2025identifyinglevelsof pages 1-2) | **K70; K70.0–K70.4; K70.9** specifically listed in available evidence (manthey2025identifyinglevelsof pages 1-2, kubina2025meta‐analysiseffectsof pages 23-23) | ICD-10 was the basis of the cited EHR classification; authors note different jurisdictions may use ICD-11, but mapping not provided here (manthey2025identifyinglevelsof pages 1-2) | Not applicable | Manthey et al. 2025: https://doi.org/10.1186/s13011-025-00670-w ; Sep 2025. Hagström et al. 2024 ICD consensus: https://doi.org/10.1097/hc9.0000000000000386 ; Feb 2024. |


*Table: This table summarizes current naming conventions, coding references, and U.S. NHANES prevalence estimates relevant to Alcoholic Liver Disease / Alcohol-associated liver disease within the 2023 steatotic liver disease framework. It is useful for aligning legacy terminology, ICD coding, and modern subclassification terms in a disease knowledge base.*

## 2. Etiology

### 2.1 Primary causal factors
The necessary upstream causal exposure is **harmful alcohol consumption**; however, ALD development and progression are heterogeneous and depend on host susceptibility and co-exposures (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, israelsenUnknownyearmetaldfromconcept pages 7-10).

### 2.2 Risk factors
#### Alcohol exposure intensity and pattern
Clinical trial consensus emphasizes careful quantification of alcohol exposure (standard drinks converted to grams), as thresholds and definitions vary across studies (lee2024designingclinicaltrials pages 1-2).

#### Genetic risk factors (susceptibility/modifier loci)
Human genetic studies and reviews identify common modifier variants that increase risk of steatosis and/or progressive outcomes (fibrosis/cirrhosis/HCC), especially under metabolic or alcohol stress.
- **PNPLA3 I148M (rs738409):** Reported to increase liver fat and increase risk of fibrosis/cirrhosis/HCC, with stronger effects under obesity/T2D and alcohol exposure (israelsenUnknownyearmetaldfromconcept pages 7-10). Proposed mechanism: variant accumulates on lipid droplets and impairs triglyceride breakdown by blocking ATGL access (israelsenUnknownyearmetaldfromconcept pages 7-10).
- **TM6SF2 E167K (rs58542926):** Increases hepatic fat and risk of advanced disease; mechanistically linked to reduced VLDL secretion (israelsenUnknownyearmetaldfromconcept pages 7-10). Quantitative associations reported in an omics review include OR ~1.38 for steatosis/fibrosis and higher ORs for more severe steatosis/fibrosis grades (bourganou2025unravelingmetabolicdysfunctionassociated pages 9-11).
- **MBOAT7 rs641738 C>T:** A modest-risk variant that reduces phosphatidylinositol remodeling and is associated with higher risk of steatosis/inflammation/fibrosis/HCC; knockout mice show increased hepatic triglycerides and fibrosis (bourganou2025unravelingmetabolicdysfunctionassociated pages 9-11).
- **HSD17B13 rs72613567 (T>TA):** A loss-of-function splice variant commonly described as **protective** against progressive liver disease outcomes (fibrosis/cirrhosis/HCC) and associated with lower aminotransferases; one review notes ~25% per-allele risk reduction for fibrosis/cirrhosis/HCC (israelsenUnknownyearmetaldfromconcept pages 7-10), and another review summarizes larger reductions reported in some cohorts (e.g., ~30%–49% reductions) (bourganou2025unravelingmetabolicdysfunctionassociated pages 9-11). JCI review notes HSD17B13 variants are associated with reduced risk for cirrhosis/HCC in ALD (mackowiak2024alcoholassociatedliverdisease pages 8-9).
- **Alcohol metabolism genes:** Population variation in **ALDH2** activity is highlighted in East Asian populations (30–40% with inactive ALDH2 polymorphisms), affecting acetaldehyde handling (mackowiak2024alcoholassociatedliverdisease pages 8-9). Another review summarizes that functional variants in **ADH1B** and **ALDH2** can reduce alcohol intake and are associated with substantially lower ALD risk (israelsenUnknownyearmetaldfromconcept pages 7-10).

#### Environmental/clinical risk modifiers
ALD pathogenesis and progression are influenced by co-factors such as sex, obesity/metabolic dysfunction, and the gut microbiome (d’arcangelo2026oxidativestressand pages 15-16, israelsenUnknownyearmetaldfromconcept pages 7-10). A U.S. mortality study also highlights concurrent societal shifts and obesity as contributors to worsening ALD burden in high-risk subgroups (pan2025alcoholassociatedliverdisease pages 1-2).

### 2.3 Protective factors
- **Genetic:** HSD17B13 loss-of-function variants are repeatedly described as hepatoprotective (israelsenUnknownyearmetaldfromconcept pages 7-10, mackowiak2024alcoholassociatedliverdisease pages 8-9, bourganou2025unravelingmetabolicdysfunctionassociated pages 9-11).
- **Behavioral:** Alcohol abstinence is the most effective intervention to improve prognosis across ALD stages (alvaradotapias2024alcoholassociatedliverdisease pages 1-3).

### 2.4 Gene–environment interaction (GxE)
The effect of key variants (notably PNPLA3) is reported to be **amplified by obesity, type 2 diabetes, and alcohol** exposure (israelsenUnknownyearmetaldfromconcept pages 7-10). Recent genetics reviews also emphasize that genetic risk “is not fixed” and can be modulated by diet/exercise/alcohol intake (wang2025geneticinsightsinto pages 1-2).

## 3. Phenotypes (clinical spectrum; HPO suggestions)

### 3.1 Core phenotypes across the ALD spectrum
Key clinical–pathologic phenotypes include:
- **Hepatic steatosis** (fatty liver) (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, mackowiak2024alcoholassociatedliverdisease pages 1-2)
- **Steatohepatitis** (inflammation plus steatosis) (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, mackowiak2024alcoholassociatedliverdisease pages 1-2)
- **Fibrosis → cirrhosis → portal hypertension/complications** (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, alvaradotapias2024alcoholassociatedliverdisease pages 3-4)
- **Alcohol-associated hepatitis (AH):** acute jaundice and liver failure; histologic ASH features include steatosis, inflammatory infiltration, hepatocyte ballooning, and Mallory–Denk bodies (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, mackowiak2024alcoholassociatedliverdisease pages 1-2)

**Frequency:** AH has been described as occurring in ~4–8% of heavy drinkers in one recent review (kasuga2025currentinsightsinto pages 1-2). Progression to cirrhosis is estimated in **8–20%** of patients with fibrosis in a recent ALD natural history review (alvaradotapias2024alcoholassociatedliverdisease pages 1-3).

### 3.2 Lab and imaging abnormalities (phenotype-type: laboratory)
Standard diagnostic/monitoring labs include AST/ALT, bilirubin, GGT, ALP, platelets and indices derived from these (e.g., FIB-4), with AST/ALT ratio patterns often used clinically for suspicion of AH/advanced ALD (rama2026novelbiomarkersfor pages 5-6, rama2026novelbiomarkersfor pages 6-8).

### 3.3 Suggested HPO terms (non-exhaustive; for knowledge-base mapping)
(These are ontology suggestions; not all are explicitly enumerated in the cited sources.)
- Jaundice (HP:0000952)
- Hyperbilirubinemia (HP:0002904)
- Hepatic steatosis (HP:0001397)
- Hepatitis (HP:0012115)
- Elevated hepatic transaminases (HP:0002910)
- Liver cirrhosis (HP:0001394)
- Portal hypertension (HP:0000124)
- Ascites (HP:0001541)
- Hepatic encephalopathy (HP:0002326)
- Hepatocellular carcinoma (HP:0001402)

## 4. Genetic / molecular information

### 4.1 “Causal genes” vs modifier genes
ALD is not typically monogenic; instead, **common variants act as modifiers** of susceptibility and progression in the setting of alcohol exposure and other environmental risks (israelsenUnknownyearmetaldfromconcept pages 7-10, israelsenUnknownyearmetaldfromconcept pages 1-7). Key modifier genes supported in the retrieved evidence include **PNPLA3**, **TM6SF2**, **MBOAT7**, and **HSD17B13** (israelsenUnknownyearmetaldfromconcept pages 7-10, bourganou2025unravelingmetabolicdysfunctionassociated pages 9-11).

### 4.2 Pathogenic / protective variants (selected)
- **PNPLA3 rs738409 (I148M):** risk modifier for steatosis and progressive outcomes; interacts with metabolic and alcohol exposures (israelsenUnknownyearmetaldfromconcept pages 7-10).
- **TM6SF2 rs58542926 (E167K):** risk modifier via lipid export/VLDL mechanisms (israelsenUnknownyearmetaldfromconcept pages 7-10, bourganou2025unravelingmetabolicdysfunctionassociated pages 9-11).
- **MBOAT7 rs641738 (C>T):** modest-risk modifier impacting phospholipid remodeling (bourganou2025unravelingmetabolicdysfunctionassociated pages 9-11).
- **HSD17B13 rs72613567 (T>TA):** protective loss-of-function splice variant (israelsenUnknownyearmetaldfromconcept pages 7-10, bourganou2025unravelingmetabolicdysfunctionassociated pages 9-11).
- **ALDH2 functional polymorphisms:** common inactive variants in East Asians (30–40%) affect acetaldehyde handling and may modify toxicity risk (mackowiak2024alcoholassociatedliverdisease pages 8-9).

### 4.3 Epigenetic information
A 2024 review highlights epigenetic abnormalities as part of ALD pathogenesis (hong2024alcoholrelatedliverdisease pages 1-2), and biomarker reviews discuss exploratory epigenomic profiling (e.g., genome-wide methylation/ChIP-seq) as emerging but not yet clinically standardized (rama2026novelbiomarkersfor pages 14-15).

## 5. Environmental information

### 5.1 Lifestyle/environmental drivers
- **Alcohol consumption:** primary driver; consensus documents emphasize rigorous quantification in grams and recognition of heterogeneous thresholds across studies (lee2024designingclinicaltrials pages 1-2).
- **Microbiome and gut permeability:** “leaky gut” and dysbiosis with PAMP/LPS translocation are repeatedly described in AH pathogenesis (alvaradotapias2024alcoholassociatedliverdisease pages 3-4, kasuga2025currentinsightsinto pages 1-2).
- **Metabolic comorbidity:** overlapping metabolic dysfunction contributes additively/superadditively to fibrosis risk in patients with steatotic liver disease and alcohol exposure (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, israelsenUnknownyearmetaldfromconcept pages 7-10).

## 6. Mechanism / pathophysiology (current understanding)

### 6.1 High-level causal chain (exposure → cellular injury → clinical disease)
1) **Alcohol absorption and metabolism** generates toxic intermediates (acetaldehyde) and perturbs mitochondrial lipid oxidation, driving steatosis and hepatocyte stress (kasuga2025currentinsightsinto pages 1-2, mackowiak2024alcoholassociatedliverdisease pages 1-2).
2) **Oxidative and ER stress** lead to lipid peroxidation, macromolecular damage, and activation of regulated cell death pathways (apoptosis, necroptosis, pyroptosis, ferroptosis) (d’arcangelo2026oxidativestressand pages 1-2, mackowiak2024alcoholassociatedliverdisease pages 1-2).
3) **Gut barrier dysfunction** increases portal influx of microbial PAMPs (e.g., LPS) and, together with hepatocyte DAMPs, triggers innate immune activation and systemic inflammation (alvaradotapias2024alcoholassociatedliverdisease pages 3-4, kasuga2025currentinsightsinto pages 1-2).
4) **Inflammation** driven by Kupffer cells/macrophages and neutrophils (including NETosis) amplifies injury; severe AH is characterized by neutrophil predominance and high cytokine signaling (e.g., TNFα, IL-1β) (d’arcangelo2026oxidativestressand pages 1-2, kasuga2025currentinsightsinto pages 1-2).
5) Persistent injury promotes **hepatic stellate cell activation**, extracellular matrix deposition and fibrosis/cirrhosis, with risk of HCC (d’arcangelo2026oxidativestressand pages 1-2, alvaradotapias2024alcoholassociatedliverdisease pages 3-4).

### 6.2 Key pathways/cellular processes (GO suggestions)
Evidence-supported processes include:
- Response to oxidative stress; reactive oxygen species metabolic process; lipid peroxidation (d’arcangelo2026oxidativestressand pages 1-2)
- Toll-like receptor signaling pathway; inflammatory response; cytokine-mediated signaling pathway (d’arcangelo2026oxidativestressand pages 1-2, kasuga2025currentinsightsinto pages 1-2)
- Regulation of apoptotic process; necroptotic process; pyroptotic process; ferroptosis (d’arcangelo2026oxidativestressand pages 1-2, mackowiak2024alcoholassociatedliverdisease pages 1-2)
- Extracellular matrix organization / fibrogenesis; wound healing (d’arcangelo2026oxidativestressand pages 1-2, alvaradotapias2024alcoholassociatedliverdisease pages 3-4)

### 6.3 Cell types involved (CL suggestions)
- Hepatocyte; Kupffer cell (liver-resident macrophage); neutrophil; monocyte-derived macrophage; hepatic stellate cell; intestinal epithelial cell/enterocyte (d’arcangelo2026oxidativestressand pages 1-2, alvaradotapias2024alcoholassociatedliverdisease pages 3-4, kasuga2025currentinsightsinto pages 1-2).

### 6.4 Recent developments (prioritizing 2023–2024)
- **Multi-omics emphasis:** A 2024 JCI review notes “new insights… utilizing the study of multiomics and other cutting-edge approaches,” and frames translation toward therapeutic targets (mackowiak2024alcoholassociatedliverdisease pages 1-2).
- **Consensus trial-design:** A 2024 Nature Reviews Gastroenterology & Hepatology expert panel provides consensus on clinical trial design integrating liver outcomes and alcohol use endpoints, including the updated SLD nomenclature context (lee2024designingclinicaltrials pages 3-5).

## 7. Anatomical structures affected (UBERON/GO-CC suggestions)

### 7.1 Organ/tissue level
- **Primary organ:** liver (UBERON:0002107)
- **Key liver compartments/cell populations:** hepatocytes, hepatic stellate cells, Kupffer cells; involvement of the **gut–liver axis** implicates intestinal epithelium as a contributing site (alvaradotapias2024alcoholassociatedliverdisease pages 3-4, kasuga2025currentinsightsinto pages 1-2).

### 7.2 Subcellular compartments (GO-CC suggestions; evidence-supported themes)
- Mitochondrion; endoplasmic reticulum; lipid droplet (mitochondrial/ER stress and lipid droplet biology are highlighted; lipid-droplet localization is central for PNPLA3/HSD17B13 biology) (israelsenUnknownyearmetaldfromconcept pages 7-10, mackowiak2024alcoholassociatedliverdisease pages 1-2).

## 8. Temporal development

### 8.1 Onset and course
ALD is typically chronic and insidious, but AH represents an acute decompensating event with severe short-term outcomes (alvaradotapias2024alcoholassociatedliverdisease pages 1-3, kasuga2025currentinsightsinto pages 1-2).

### 8.2 Staging and severity (AH)
Severe alcohol-associated hepatitis is often defined using **Maddrey’s discriminant function ≥32** or **MELD ≥20** in recent reviews (kumar2026emergingtherapeuticregimens pages 5-6). Short-term mortality in severe AH is repeatedly reported at **~20%–50%** (hong2024alcoholrelatedliverdisease pages 1-2, kasuga2025currentinsightsinto pages 1-2).

## 9. Inheritance and population

ALD is a **multifactorial** disease with **polygenic modifier** effects and strong environmental dependence (israelsenUnknownyearmetaldfromconcept pages 7-10). Allele frequencies and population differences are highlighted for alcohol metabolism genes, e.g., inactive ALDH2 variants in East Asian populations (mackowiak2024alcoholassociatedliverdisease pages 8-9).

## 10. Diagnostics (current practice and emerging)

### 10.1 Clinical assessment and routine biomarkers
Routine labs (AST, ALT, bilirubin, GGT, ALP, platelets) are standard but have limited specificity; AST/ALT ratio patterns are supportive for AH/advanced disease suspicion (rama2026novelbiomarkersfor pages 5-6).

### 10.2 Non-invasive fibrosis staging: elastography and serum panels
A recent biomarker review summarizes validated elastography thresholds and practical caveats:
- **Vibration-controlled transient elastography (VCTE):** validated cutoffs of **~12.1 kPa for ≥F3** and **~18.6 kPa for F4**, AUROCs ~0.90–0.91; LSM <8–10 kPa helps rule out advanced fibrosis; interpret with AST/bilirubin since inflammation can inflate stiffness and LSM may fall after abstinence (rama2026novelbiomarkersfor pages 6-8).
- **2D shear-wave elastography** diagnostic performance is also reported (e.g., 88% sensitivity/95% specificity for advanced fibrosis with suggested cutoffs) (rama2026novelbiomarkersfor pages 6-8).
- **ELF test:** described as having high accuracy for advanced fibrosis and can outperform APRI/FIB-4, with reported AUROC ~0.92–0.94 (rama2026novelbiomarkersfor pages 5-6).
- **Pro-C3 / ADAPT:** Pro-C3 is highlighted as a predictor of outcomes and used in composite algorithms for advanced fibrosis detection (rama2026novelbiomarkersfor pages 17-18).

### 10.3 Alcohol exposure biomarkers
**Phosphatidylethanol (PEth)** is emphasized as an objective marker of recent alcohol intake; one review notes ≥200 ng/mL indicates regular high intake and that adding PEth can increase ALD detection “3–4×” compared with self-report alone (rama2026novelbiomarkersfor pages 5-6).

### 10.4 Emerging mechanistic biomarkers and multi-omics
Reviews highlight emerging biomarkers reflecting cell death (CK-18 fragments), fibrogenesis (Pro-C3), genetic risk (PNPLA3/TM6SF2/HSD17B13 and PRS), and gut dysbiosis signatures/metabolites (SCFAs, bile acids, TMAO; reduced Faecalibacterium prausnitzii and Akkermansia muciniphila) (rama2026novelbiomarkersfor pages 1-3, rama2026novelbiomarkersfor pages 8-9).

## 11. Outcome / prognosis

### 11.1 Severe AH prognosis
Severe alcohol-associated hepatitis has “short-term mortality rate of **20%–50%**” in developed countries in a recent review (quoted from abstract) (kasuga2025currentinsightsinto pages 1-2).

### 11.2 ALD mortality trends (real-world implementation and statistics)
- **United States (1999–2022):** In a JAMA Network Open analysis of **436,814 ALD-related deaths**, age-adjusted mortality doubled **6.71 → 12.53 per 100,000**, accelerating in 2018–2022 (APC **8.94%**) with disproportionate increases among women, ages 25–44, and American Indian/Alaska Native populations (pan2025alcoholassociatedliverdisease pages 1-2).
- **Global (GBD 2021; 2000–2021):** A 2025 analysis reports **3.02 million prevalent ALD cases** in 2021 (+38.68% since 2000) and **132,030 prevalent alcohol-attributable primary liver cancer cases** (+94.12%) (danpanichkul2025globalepidemiologyof pages 1-5).

## 12. Treatment

### 12.1 Foundational management (standard of care)
- **Alcohol abstinence:** described as “the most effective way to improve prognosis across all stages of ALD” (quoted from abstract) (alvaradotapias2024alcoholassociatedliverdisease pages 1-3). Multidisciplinary care integrating AUD treatment is emphasized (adekunle2023therapeutictargetsin pages 1-2).
- **Corticosteroids (severe AH):** described as “the only evidence-based pharmacologic treatment” in one severe AH review, with limited efficacy and substantial non-response (kasuga2025currentinsightsinto pages 1-2). Another review notes response rates ~50–60% among eligible patients by day-7 Lille score, with many contraindications (ineligibility 40–50%) (adekunle2023therapeutictargetsin pages 1-2).
- **Nutrition therapy:** enteral nutrition strategies and caloric/protein targets are summarized for severe AH in Clinics in Liver Disease, including associations between inadequate intake and lower survival, and guidance to initiate enteral nutrition early when needed (hardesty2024currentpharmacotherapyand pages 4-6).
- **Liver transplantation:** ALD is now the leading indication for liver transplant in the U.S.; early LT is discussed as a salvage option for steroid-refractory severe AH but remains limited by selection protocols and donor/ethical constraints (pan2025alcoholassociatedliverdisease pages 1-2, kasuga2025currentinsightsinto pages 1-2).

### 12.2 Experimental / targeted therapies and clinical trials (selected)
A recent ALD natural-history/therapy review tabulates “Emerging treatment options” (Table 2) including anti-inflammatory, apoptosis/cell death, bile-acid signaling, microbiome, and regenerative approaches, with trial identifiers (alvaradotapias2024alcoholassociatedliverdisease media 15159c76).

**Selected trials and interventions (with registry IDs when available in retrieved evidence):**
- **IL-1β inhibition (Canakinumab):** **NCT03775109** (listed in Table 2) (alvaradotapias2024alcoholassociatedliverdisease media 15159c76).
- **IL-1 receptor antagonist (Anakinra):** **NCT04072822** (listed in Table 2); other clinical evidence indicates anakinra-based approaches have had mixed or unfavorable results in at least one trial (stopped early due to worsening MELD) (alvaradotapias2024alcoholassociatedliverdisease media 15159c76, d’arcangelo2026oxidativestressand pages 12-13).
- **FXR agonist (Obeticholic acid):** **NCT02039219** (Table 2) (alvaradotapias2024alcoholassociatedliverdisease media 15159c76).
- **Caspase inhibitor (Emricasan / IDN-6556):** **NCT01912404** (Table 2); the ClinicalTrials.gov record describes a phase 2 trial terminated early with only 5 enrolled due to concerns of high systemic drug levels, precluding meaningful analysis (alvaradotapias2024alcoholassociatedliverdisease media 15159c76, NCT01912404 chunk 1).
- **Gut–liver axis modulation with IgG-enriched bovine colostrum:** **NCT02473341** phase 3 adjunct trial (NCT02473341 chunk 1).

### 12.3 Suggested MAXO terms (examples)
(ontology suggestions)
- Alcohol abstinence counseling (MAXO:0000508)
- Corticosteroid therapy (MAXO:0000746)
- Enteral nutrition (MAXO:0000660)
- Liver transplantation (MAXO:0001175)
- Elastography (MAXO:0000976)

## 13. Prevention

Public-health burden analyses emphasize urgent prevention measures; major preventable levers include reducing harmful alcohol consumption and implementing targeted interventions in high-risk groups (danpanichkul2025globalepidemiologyof pages 1-5, pan2025alcoholassociatedliverdisease pages 1-2). Primary and secondary prevention in practice includes:
- **Primary prevention:** population alcohol control policies (pricing/availability/marketing restrictions) and AUD prevention/treatment integration (supported as urgent in GBD-based epidemiology work) (danpanichkul2025globalepidemiologyof pages 1-5).
- **Secondary prevention:** non-invasive fibrosis screening (VCTE/serum panels) in at-risk drinkers and monitoring with objective alcohol biomarkers (PEth) to detect relapse or underreported intake (rama2026novelbiomarkersfor pages 6-8, rama2026novelbiomarkersfor pages 5-6).

## 14. Other species / natural disease
Not systematically covered in the retrieved evidence set.

## 15. Model organisms / experimental models
A 2024 JCI review notes the importance of preclinical models and describes introduction of **binge ethanol intake into chronically ethanol-fed mice** to model disease features (mackowiak2024alcoholassociatedliverdisease pages 1-2). A 2023 Hepatology paper uses the **NIAAA chronic + binge ethanol feeding model** and demonstrates that adipose lipolysis is important for ethanol-induced hepatic steatosis and lipid peroxidation, providing a mechanistic mouse model example (hong2024alcoholrelatedliverdisease pages 1-2).

## Key statistics summary (selected)
- **NHANES (2017–Mar 2020) U.S. prevalence under SLD nomenclature:** SLD 34.2%, MASLD 31.3%, MetALD 2.0%, ALD 0.7% (lee2024nationalprevalenceestimates pages 1-2).
- **GBD 2021 global counts (2021):** 3.02 million prevalent ALD cases and 132,030 prevalent alcohol-attributable primary liver cancer cases (danpanichkul2025globalepidemiologyof pages 1-5).
- **U.S. mortality trend (1999–2022):** ALD age-adjusted mortality 6.71 → 12.53 per 100,000; 436,814 ALD deaths (pan2025alcoholassociatedliverdisease pages 1-2).
- **Severe AH short-term mortality:** 20%–50% (kasuga2025currentinsightsinto pages 1-2).

## Evidence limitations (in this tool-based evidence set)
- MONDO and MeSH identifiers, ICD-11 liver-disease code mappings, OMIM/Orphanet IDs, and comprehensive phenotype frequency distributions were not found in the retrieved texts and would require targeted database queries beyond the current evidence set.
- Several mechanistic and treatment details are best supported by recent reviews; primary mechanistic studies (PMID-first extraction) were not comprehensively retrieved here.


References

1. (alvaradotapias2024alcoholassociatedliverdisease pages 1-3): Edilmar Alvarado-Tapias, Elisa Pose, Jordi Gratacós, Ana Clemente-Sánchez, Hugo Hugo López-Pelayo, and Ramón Bataller. Alcohol-associated liver disease: natural history, management and novel targeted therapies. Clinical and Molecular Hepatology, 31:S112-S133, Oct 2024. URL: https://doi.org/10.3350/cmh.2024.0709, doi:10.3350/cmh.2024.0709. This article has 32 citations.

2. (mackowiak2024alcoholassociatedliverdisease pages 1-2): Bryan Mackowiak, Yaojie Fu, Luca Maccioni, and Bin Gao. Alcohol-associated liver disease. The Journal of Clinical Investigation, Feb 2024. URL: https://doi.org/10.1172/jci176345, doi:10.1172/jci176345. This article has 352 citations.

3. (hong2024alcoholrelatedliverdisease pages 1-2): Xiao Hong, Shuo-Wen Huang, He Jiang, Qing Ma, Jiang Qiu, Qihan Luo, Chunlu Cao, Yiyang Xu, Fuzhe Chen, Yufan Chen, Chunfeng Sun, Haozhe Fu, Yiming Liu, Changyu Li, Fangming Chen, and Ping Qiu. Alcohol-related liver disease (ald): current perspectives on pathogenesis, therapeutic strategies, and animal models. Frontiers in Pharmacology, Nov 2024. URL: https://doi.org/10.3389/fphar.2024.1432480, doi:10.3389/fphar.2024.1432480. This article has 34 citations.

4. (israelsenUnknownyearmetaldfromconcept pages 7-10): M Israelsen, E Trépo, A Krag, and S Stender. Metald: from concept to clinic, genetic factors and clinical outcomes. Unknown journal, Unknown year.

5. (manthey2025identifyinglevelsof pages 1-2): Jakob Manthey, Carolin Kilian, Ludwig Kraus, Ingo Schäfer, Anna Schranz, and Bernd Schulte. Identifying levels of alcohol use disorder severity in electronic health records. Substance Abuse Treatment, Prevention, and Policy, Sep 2025. URL: https://doi.org/10.1186/s13011-025-00670-w, doi:10.1186/s13011-025-00670-w. This article has 2 citations and is from a peer-reviewed journal.

6. (kubina2025meta‐analysiseffectsof pages 23-23): Matthew Kubina, Vitchapong Prasitsumrit, Jarell Tan, Joo Wei Ethan Quek, Dhiraj Peddu, Ankit Mishra, Pojsakorn Danpanichkul, Jake P. Mann, Eric Trépo, Stephan Buch, Daniel Q. Huang, Cheng Han Ng, Mark D. Muthiah, Yu Jun Wong, Karn Wijarnpreecha, and Vincent L. Chen. Meta‐analysis: effects of steatotic liver disease‐associated genetic risk alleles on longitudinal outcomes. Alimentary Pharmacology &amp; Therapeutics, 62:244-276, Jun 2025. URL: https://doi.org/10.1111/apt.70256, doi:10.1111/apt.70256. This article has 11 citations and is from a highest quality peer-reviewed journal.

7. (lee2024designingclinicaltrials pages 3-5): Brian P. Lee, Katie Witkiewitz, Jessica Mellinger, Frank A. Anania, Ramon Bataller, Thomas G. Cotter, Brenda Curtis, Srinivasan Dasarathy, Kelly S. DeMartini, Ivan Diamond, Nancy Diazgranados, Andrea F. DiMartini, Daniel E. Falk, Anne C. Fernandez, Margarita N. German, Patrick S. Kamath, Kelley M. Kidwell, Lorenzo Leggio, Raye Litten, Alexandre Louvet, Michael R. Lucey, Mary E. McCaul, Arun J. Sanyal, Ashwani K. Singal, Norman L. Sussman, Norah A. Terrault, Mark R. Thursz, Elizabeth C. Verna, Svetlana Radaeva, Laura E. Nagy, and Mack C. Mitchell. Designing clinical trials to address alcohol use and alcohol-associated liver disease: an expert panel consensus statement. Nature reviews. Gastroenterology & hepatology, 21:626-645, Jun 2024. URL: https://doi.org/10.1038/s41575-024-00936-x, doi:10.1038/s41575-024-00936-x. This article has 52 citations.

8. (lee2024nationalprevalenceestimates pages 1-2): Brian P. Lee, Jennifer L. Dodge, and Norah A. Terrault. National prevalence estimates for steatotic liver disease and subclassifications using consensus nomenclature. Hepatology, 79:666-673, Sep 2024. URL: https://doi.org/10.1097/hep.0000000000000604, doi:10.1097/hep.0000000000000604. This article has 207 citations and is from a highest quality peer-reviewed journal.

9. (danpanichkul2025globalepidemiologyof pages 1-5): Pojsakorn Danpanichkul, Luis Antonio Díaz, Kanokphong Suparan, Primrose Tothanarungroj, Supapitch Sirimangklanurak, Thanida Auttapracha, Hanna L. Blaney, Banthoon Sukphutanan, Yanfang Pang, Siwanart Kongarin, Francisco Idalsoaga, Eduardo Fuentes-López, Lorenzo Leggio, Mazen Noureddin, Trenton M. White, Alexandre Louvet, Philippe Mathurin, Rohit Loomba, Patrick S. Kamath, Jürgen Rehm, Jeffrey V. Lazarus, Karn Wijarnpreecha, and Juan Pablo Arab. Global epidemiology of alcohol-related liver disease, liver cancer, and alcohol use disorder, 2000–2021. Clinical and Molecular Hepatology, 31:525-547, Jan 2025. URL: https://doi.org/10.3350/cmh.2024.0835, doi:10.3350/cmh.2024.0835. This article has 57 citations.

10. (lee2024designingclinicaltrials pages 1-2): Brian P. Lee, Katie Witkiewitz, Jessica Mellinger, Frank A. Anania, Ramon Bataller, Thomas G. Cotter, Brenda Curtis, Srinivasan Dasarathy, Kelly S. DeMartini, Ivan Diamond, Nancy Diazgranados, Andrea F. DiMartini, Daniel E. Falk, Anne C. Fernandez, Margarita N. German, Patrick S. Kamath, Kelley M. Kidwell, Lorenzo Leggio, Raye Litten, Alexandre Louvet, Michael R. Lucey, Mary E. McCaul, Arun J. Sanyal, Ashwani K. Singal, Norman L. Sussman, Norah A. Terrault, Mark R. Thursz, Elizabeth C. Verna, Svetlana Radaeva, Laura E. Nagy, and Mack C. Mitchell. Designing clinical trials to address alcohol use and alcohol-associated liver disease: an expert panel consensus statement. Nature reviews. Gastroenterology & hepatology, 21:626-645, Jun 2024. URL: https://doi.org/10.1038/s41575-024-00936-x, doi:10.1038/s41575-024-00936-x. This article has 52 citations.

11. (bourganou2025unravelingmetabolicdysfunctionassociated pages 9-11): Maria V. Bourganou, Maria Eleni Chondrogianni, Ioannis Kyrou, Christina-Maria Flessa, Antonios Chatzigeorgiou, Evangelos Oikonomou, Vaia Lambadiari, Harpal S. Randeva, and Eva Kassi. Unraveling metabolic dysfunction-associated steatotic liver disease through the use of omics technologies. International Journal of Molecular Sciences, 26:1589, Feb 2025. URL: https://doi.org/10.3390/ijms26041589, doi:10.3390/ijms26041589. This article has 28 citations.

12. (mackowiak2024alcoholassociatedliverdisease pages 8-9): Bryan Mackowiak, Yaojie Fu, Luca Maccioni, and Bin Gao. Alcohol-associated liver disease. The Journal of Clinical Investigation, Feb 2024. URL: https://doi.org/10.1172/jci176345, doi:10.1172/jci176345. This article has 352 citations.

13. (d’arcangelo2026oxidativestressand pages 15-16): Francesca D’Arcangelo, Neil Rajoriya, and Patricia F. Lalor. Oxidative stress and alcohol-related hepatitis: a role for future therapies. Antioxidants, 15:493, Apr 2026. URL: https://doi.org/10.3390/antiox15040493, doi:10.3390/antiox15040493. This article has 0 citations.

14. (pan2025alcoholassociatedliverdisease pages 1-2): Chun-Wei Pan, Yazan Abboud, Amit S. Chitnis, Wei Zhang, Ashwani K. Singal, and Robert J Wong. Alcohol-associated liver disease mortality. JAMA Network Open, 8:e2514857, Jun 2025. URL: https://doi.org/10.1001/jamanetworkopen.2025.14857, doi:10.1001/jamanetworkopen.2025.14857. This article has 26 citations and is from a peer-reviewed journal.

15. (wang2025geneticinsightsinto pages 1-2): Qianchang Wang, Zhe Wang, Minzhe Hu, Fangfeng Liu, and Zhengjian Wang. Genetic insights into alcohol-associated liver disease: integrative transcriptome-wide analysis identifies novel susceptibility genes. Frontiers in Medicine, Jul 2025. URL: https://doi.org/10.3389/fmed.2025.1623367, doi:10.3389/fmed.2025.1623367. This article has 2 citations.

16. (alvaradotapias2024alcoholassociatedliverdisease pages 3-4): Edilmar Alvarado-Tapias, Elisa Pose, Jordi Gratacós, Ana Clemente-Sánchez, Hugo Hugo López-Pelayo, and Ramón Bataller. Alcohol-associated liver disease: natural history, management and novel targeted therapies. Clinical and Molecular Hepatology, 31:S112-S133, Oct 2024. URL: https://doi.org/10.3350/cmh.2024.0709, doi:10.3350/cmh.2024.0709. This article has 32 citations.

17. (kasuga2025currentinsightsinto pages 1-2): Ryosuke Kasuga, Po‐Sung Chu, Takanori Kanai, and Nobuhiro Nakamoto. Current insights into pathogenesis and anti‐inflammatory treatment strategies for severe alcohol‐associated hepatitis: focus on neutrophil‐targeted therapies. Hepatology Research, 55:785-94, May 2025. URL: https://doi.org/10.1111/hepr.14206, doi:10.1111/hepr.14206. This article has 1 citations and is from a peer-reviewed journal.

18. (rama2026novelbiomarkersfor pages 5-6): Kaanthi Rama, Vinay Jahagirdar, Francisco Idalsoaga, Hanna Blaney, S. Fisher Rhoads, Luis Antonio Díaz, Marco Arrese, and Juan Pablo Arab. Novel biomarkers for alcohol-associated liver disease and their implications across clinical settings. Clinical and Molecular Hepatology, 32:443-463, Apr 2026. URL: https://doi.org/10.3350/cmh.2025.0921, doi:10.3350/cmh.2025.0921. This article has 3 citations.

19. (rama2026novelbiomarkersfor pages 6-8): Kaanthi Rama, Vinay Jahagirdar, Francisco Idalsoaga, Hanna Blaney, S. Fisher Rhoads, Luis Antonio Díaz, Marco Arrese, and Juan Pablo Arab. Novel biomarkers for alcohol-associated liver disease and their implications across clinical settings. Clinical and Molecular Hepatology, 32:443-463, Apr 2026. URL: https://doi.org/10.3350/cmh.2025.0921, doi:10.3350/cmh.2025.0921. This article has 3 citations.

20. (israelsenUnknownyearmetaldfromconcept pages 1-7): M Israelsen, E Trépo, A Krag, and S Stender. Metald: from concept to clinic, genetic factors and clinical outcomes. Unknown journal, Unknown year.

21. (rama2026novelbiomarkersfor pages 14-15): Kaanthi Rama, Vinay Jahagirdar, Francisco Idalsoaga, Hanna Blaney, S. Fisher Rhoads, Luis Antonio Díaz, Marco Arrese, and Juan Pablo Arab. Novel biomarkers for alcohol-associated liver disease and their implications across clinical settings. Clinical and Molecular Hepatology, 32:443-463, Apr 2026. URL: https://doi.org/10.3350/cmh.2025.0921, doi:10.3350/cmh.2025.0921. This article has 3 citations.

22. (d’arcangelo2026oxidativestressand pages 1-2): Francesca D’Arcangelo, Neil Rajoriya, and Patricia F. Lalor. Oxidative stress and alcohol-related hepatitis: a role for future therapies. Antioxidants, 15:493, Apr 2026. URL: https://doi.org/10.3390/antiox15040493, doi:10.3390/antiox15040493. This article has 0 citations.

23. (kumar2026emergingtherapeuticregimens pages 5-6): Rahul Kumar, Sakktivel Elangovan, and Sumeet K. Asrani. Emerging therapeutic regimens as alternatives to glucocorticoids for severe alcohol-associated hepatitis: a comprehensive review. Clinical and Molecular Hepatology, 32:599-619, Apr 2026. URL: https://doi.org/10.3350/cmh.2025.1163, doi:10.3350/cmh.2025.1163. This article has 0 citations.

24. (rama2026novelbiomarkersfor pages 17-18): Kaanthi Rama, Vinay Jahagirdar, Francisco Idalsoaga, Hanna Blaney, S. Fisher Rhoads, Luis Antonio Díaz, Marco Arrese, and Juan Pablo Arab. Novel biomarkers for alcohol-associated liver disease and their implications across clinical settings. Clinical and Molecular Hepatology, 32:443-463, Apr 2026. URL: https://doi.org/10.3350/cmh.2025.0921, doi:10.3350/cmh.2025.0921. This article has 3 citations.

25. (rama2026novelbiomarkersfor pages 1-3): Kaanthi Rama, Vinay Jahagirdar, Francisco Idalsoaga, Hanna Blaney, S. Fisher Rhoads, Luis Antonio Díaz, Marco Arrese, and Juan Pablo Arab. Novel biomarkers for alcohol-associated liver disease and their implications across clinical settings. Clinical and Molecular Hepatology, 32:443-463, Apr 2026. URL: https://doi.org/10.3350/cmh.2025.0921, doi:10.3350/cmh.2025.0921. This article has 3 citations.

26. (rama2026novelbiomarkersfor pages 8-9): Kaanthi Rama, Vinay Jahagirdar, Francisco Idalsoaga, Hanna Blaney, S. Fisher Rhoads, Luis Antonio Díaz, Marco Arrese, and Juan Pablo Arab. Novel biomarkers for alcohol-associated liver disease and their implications across clinical settings. Clinical and Molecular Hepatology, 32:443-463, Apr 2026. URL: https://doi.org/10.3350/cmh.2025.0921, doi:10.3350/cmh.2025.0921. This article has 3 citations.

27. (adekunle2023therapeutictargetsin pages 1-2): Ayooluwatomiwa Deborah Adekunle, Adeyinka Adejumo, and Ashwani K. Singal. Therapeutic targets in alcohol-associated liver disease: progress and challenges. Therapeutic Advances in Gastroenterology, Jan 2023. URL: https://doi.org/10.1177/17562848231170946, doi:10.1177/17562848231170946. This article has 10 citations and is from a peer-reviewed journal.

28. (hardesty2024currentpharmacotherapyand pages 4-6): Josiah E. Hardesty and Craig J. McClain. Current pharmacotherapy and nutrition therapy of alcohol-associated liver disease. Clinics in Liver Disease, 28:731-745, Nov 2024. URL: https://doi.org/10.1016/j.cld.2024.06.018, doi:10.1016/j.cld.2024.06.018. This article has 2 citations and is from a peer-reviewed journal.

29. (alvaradotapias2024alcoholassociatedliverdisease media 15159c76): Edilmar Alvarado-Tapias, Elisa Pose, Jordi Gratacós, Ana Clemente-Sánchez, Hugo Hugo López-Pelayo, and Ramón Bataller. Alcohol-associated liver disease: natural history, management and novel targeted therapies. Clinical and Molecular Hepatology, 31:S112-S133, Oct 2024. URL: https://doi.org/10.3350/cmh.2024.0709, doi:10.3350/cmh.2024.0709. This article has 32 citations.

30. (d’arcangelo2026oxidativestressand pages 12-13): Francesca D’Arcangelo, Neil Rajoriya, and Patricia F. Lalor. Oxidative stress and alcohol-related hepatitis: a role for future therapies. Antioxidants, 15:493, Apr 2026. URL: https://doi.org/10.3390/antiox15040493, doi:10.3390/antiox15040493. This article has 0 citations.

31. (NCT01912404 chunk 1):  Study of IDN-6556 in Patients With Severe Alcoholic Hepatitis and Contraindications to Steroid Therapy. Conatus Pharmaceuticals Inc.. 2013. ClinicalTrials.gov Identifier: NCT01912404

32. (NCT02473341 chunk 1): Prof. Sandeep S Sidhu. Gut-Liver Axis Modulation With IgG-Enriched Immunotherapy in Severe Alcohol-Associated Hepatitis. Dayanand Medical College and Hospital. 2017. ClinicalTrials.gov Identifier: NCT02473341

## Artifacts

- [Edison artifact artifact-00](Alcoholic_Liver_Disease-deep-research-falcon_artifacts/artifact-00.md)