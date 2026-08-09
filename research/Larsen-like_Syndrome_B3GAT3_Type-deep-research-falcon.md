---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:08:27.848772'
end_time: '2026-08-01T17:17:11.761340'
duration_seconds: 523.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Larsen-like Syndrome B3GAT3 Type
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Larsen-like_Syndrome_B3GAT3_Type-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Larsen-like Syndrome B3GAT3 Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Larsen-like Syndrome B3GAT3 Type** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
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
- **Disease Name:** Larsen-like Syndrome B3GAT3 Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Larsen-like Syndrome B3GAT3 Type** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Larsen-like syndrome, B3GAT3 type: comprehensive disease-characteristics report

## Executive summary and evidence limits

Larsen-like syndrome, B3GAT3 type is an ultra-rare autosomal-recessive glycosaminoglycan (GAG) **linkeropathy** caused by biallelic pathogenic variants in **B3GAT3**. It is best regarded as a phenotypic continuum—also called **B3GAT3-related disorder**—rather than a narrowly uniform syndrome. Cardinal manifestations are congenital skeletal dysplasia, joint laxity and dislocations, contractures or radioulnar synostosis, short stature, craniofacial dysmorphism, osteopenia or fractures, and variable congenital cardiovascular disease. Severe alleles can cause craniosynostosis, marked bone fragility, and death in infancy. (baasanjav2011faultyinitiationof pages 2-3, yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 10-12)

The evidence base is exceptionally small. The 2019 synthesis comprised approximately **26 patients from 13 families**, 11 reportedly consanguineous. Consequently, frequencies below are descriptive counts from variant-stratified case series, not stable population estimates. Most knowledge comes from individual patients and pedigrees rather than EHR cohorts, registries, randomized trials, or epidemiologic surveillance. (ritelli2019furtherdefiningthe pages 10-12)

| Domain | Evidence-backed finding | Suggested ontology/identifier | Evidence type/limitations |
|---|---|---|---|
| Disease identifiers / nomenclature | Rare autosomal recessive linkeropathy caused by biallelic **B3GAT3** variants; originally proposed as **“Larsen-like syndrome, B3GAT3 type”** and now often grouped under **B3GAT3-related disorder/linkeropathy**. MONDO association available. OMIM phenotype cited in review literature as **245600**. (OpenTargets Search: Larsen-like syndrome B3GAT3 type-B3GAT3, baasanjav2011faultyinitiationof pages 2-3, ritelli2019furtherdefiningthe pages 10-12) | MONDO:0009511; OMIM:245600; disease label: Larsen-like syndrome, B3GAT3 type | Aggregated disease-resource plus primary case reports/reviews; naming varies across papers and severity spectrum overlaps ABS/SGS/GO-like presentations. |
| Evidence provenance | Knowledge derives from **aggregated disease-level literature and curated resources**, but core evidence is from **individual case reports/series** and small family-based cohorts, not EHR-scale datasets. (baasanjav2011faultyinitiationof pages 2-3, ritelli2019furtherdefiningthe pages 10-12, ritelli2019furtherdefiningthe pages 1-3) | Evidence type labels: human case report; family study; review | Very small sample sizes; ascertainment and publication bias likely. |
| Causal gene | **B3GAT3** encodes **beta-1,3-glucuronyltransferase 3 / GlcAT-I**, the enzyme that adds the terminal glucuronic acid of the common proteoglycan linker tetrasaccharide. (OpenTargets Search: Larsen-like syndrome B3GAT3 type-B3GAT3, baasanjav2011faultyinitiationof pages 2-3, mizumoto2018defectsinbiosynthesis pages 9-10) | HGNC gene symbol: B3GAT3; protein label: GlcAT-I | Strong gene-disease validity from multiple families, functional assays, and curated target-disease association. |
| Inheritance | **Autosomal recessive** inheritance with affected individuals typically carrying **biallelic** variants; many reported families are consanguineous. (baasanjav2011faultyinitiationof pages 2-3, yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 10-12) | Inheritance term: autosomal recessive | Based on small pedigrees; penetrance appears high for biallelic pathogenic variants but is not formally quantified. |
| Pathogenic variant spectrum | Reported variants include homozygous **c.830G>A p.Arg277Gln**, **c.419C>T p.Pro140Leu**, **c.416C>T p.Thr139Met**, **c.245C>T p.Pro82Leu**, **c.667G>A p.Gly223Ser**, and compound heterozygous **c.1A>G p.Met1? / c.671T>A p.Leu224Gln**; most are missense/hypomorphic. (ritelli2019furtherdefiningthe pages 8-10, ritelli2019furtherdefiningthe pages 10-12) | Variant class labels: missense; start-loss; compound heterozygous; homozygous | Review synthesis included ~26 patients/13 families; some variants lacked direct fibroblast functional testing. |
| Core mechanism | B3GAT3 deficiency impairs completion of the **Xyl-Gal-Gal-GlcA** linker region, disrupting synthesis of **chondroitin sulfate (CS), dermatan sulfate (DS), and heparan sulfate (HS)** chains on proteoglycans. Patient fibroblasts showed markedly reduced GlcAT-I activity and reduced surface GAG chains. (baasanjav2011faultyinitiationof pages 2-3, mizumoto2018defectsinbiosynthesis pages 9-10, baasanjav2011faultyinitiationof pages 8-10, baasanjav2011faultyinitiationof pages 6-7) | GO: glycosaminoglycan biosynthetic process; proteoglycan biosynthetic process; Golgi apparatus | Direct biochemical evidence exists for p.Arg277Gln; mechanistic extrapolation to some later variants is partly review-based. |
| Protein dysfunction / subcellular localization | GlcAT-I normally localizes to the **cis/cis-medial Golgi**; mutant p.Arg277Gln showed reduced protein abundance, loss of normal Golgi localization, and residual activity consistent with a **hypomorphic loss-of-function** effect. (baasanjav2011faultyinitiationof pages 6-7) | GO cellular component: cis-Golgi network / Golgi apparatus | Directly shown for one variant in fibroblasts/recombinant assays; not established for every allele. |
| Functional quantitative data | In patient fibroblasts with p.Arg277Gln, **GlcAT-I activity was reduced to ~3–5% of control**, with **CS chains ~65%** and **HS chains ~53%** of control levels. (baasanjav2011faultyinitiationof pages 6-7, baasanjav2011faultyinitiationof pages 8-10) | Laboratory phenotype labels: reduced glucuronyltransferase activity; decreased cell-surface CS/HS | Single-family biochemical dataset; no standardized clinical biomarker thresholds. |
| Genotype-phenotype correlation | Severity appears to vary by variant/domain: **p.Gly223Ser** is associated with a particularly severe infantile craniosynostosis/bone fragility phenotype; **p.Pro140Leu** may have prominent skeletal disease with less cardiac involvement. (yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 10-12, mizumoto2018defectsinbiosynthesis pages 9-10) | Genotype-phenotype association label | Correlations are suggestive only because each genotype is represented by very few patients. |
| Major phenotype group: skeletal / joints | Core musculoskeletal findings include **short stature**, **joint hypermobility/laxity**, **multiple joint dislocations**, **elbow abnormalities**, **radioulnar synostosis**, **foot deformity**, **kyphoscoliosis/scoliosis**, **osteopenia**, and sometimes **fractures**. (baasanjav2011faultyinitiationof pages 2-3, yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 14-16, ritelli2019furtherdefiningthe pages 8-10) | HPO suggestions: Short stature; Joint hypermobility; Joint dislocation; Radioulnar synostosis; Scoliosis; Kyphosis; Osteopenia; Fractures; Talipes/clubfoot | Frequencies in reviews are variant-stratified and tiny; pooled percentages are unstable. |
| Major phenotype group: craniofacial | Frequent craniofacial features include **midface hypoplasia**, **depressed nasal bridge**, **micrognathia**, **downslanting palpebral fissures**, **short/webbed neck**, **blue sclerae**, **prominent/proptotic eyes**, and in severe cases **craniosynostosis**. (baasanjav2011faultyinitiationof pages 2-3, yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 14-16, ritelli2019furtherdefiningthe pages 8-10) | HPO suggestions: Midface retrusion/hypoplasia; Depressed nasal bridge; Micrognathia; Downslanting palpebral fissures; Blue sclerae; Craniosynostosis; Webbed neck | Some features are concentrated in severe allelic subsets rather than universal across B3GAT3 disease. |
| Major phenotype group: cardiovascular | Cardiovascular involvement is a notable distinguishing feature, including **bicuspid aortic valve**, **mitral valve prolapse**, **septal defects**, **aortic root dilatation**, and broader congenital heart disease. (baasanjav2011faultyinitiationof pages 2-3, ritelli2019furtherdefiningthe pages 3-5, ritelli2019furtherdefiningthe pages 14-16) | HPO suggestions: Bicuspid aortic valve; Mitral valve prolapse; Atrial septal defect; Aortic root dilatation; Congenital heart defect | Cardiac burden appears enriched relative to some other linkeropathies, but exact prevalence remains uncertain. |
| Major phenotype group: connective tissue / skin / other | Additional reported findings include **pectus abnormality**, **peculiar fingers** (long/slender/tapered/broad/arachnodactylous), **hypotonia**, low bone mineral density, ophthalmic abnormalities, and occasional developmental delay; cognition may be normal in some families. (ritelli2019furtherdefiningthe pages 3-5, ritelli2019furtherdefiningthe pages 14-16, ritelli2019furtherdefiningthe pages 8-10, baasanjav2011faultyinitiationof pages 6-7) | HPO suggestions: Pectus excavatum/carinatum; Arachnodactyly; Hypotonia; Low bone mineral density; Strabismus; Refractive error | Heterogeneous and incompletely reported across studies. |
| Anatomy affected | Primary systems affected are **skeletal/connective tissue** and **cardiovascular**; secondary involvement can include craniofacial bones, eyes, and growth/endocrine features. (baasanjav2011faultyinitiationof pages 2-3, ritelli2019furtherdefiningthe pages 3-5, ritelli2019furtherdefiningthe pages 14-16) | UBERON suggestions: skeleton; joint; cartilage; heart valve; aorta; craniofacial skeleton | Organ mapping is inferred from clinical phenotypes and tissue expression rather than systematic pathology series. |
| Tissue / cell types / biological process | Relevant tissues/cells include **cartilage/chondrocytes**, **osteoblast-lineage cells**, **fibroblasts**, and **aortic/valvular connective tissues**. Mouse expression data showed B3gat3 in heart, aorta, bone, and osteoblasts. (baasanjav2011faultyinitiationof pages 6-7, holmborn2012ontheroles pages 1-2, holmborn2012ontheroles pages 8-9) | CL suggestions: chondrocyte; osteoblast; fibroblast. GO suggestions: extracellular matrix organization; cartilage development; skeletal system development; heart valve development; glycosaminoglycan biosynthesis | Cell-type evidence is partly indirect; human single-cell/spatial data were not found. |
| Onset / temporal development | Disease is typically **congenital or neonatal/early childhood onset** with structural anomalies apparent prenatally or at birth in severe cases and progressive orthopedic burden during childhood in survivors. (baasanjav2011faultyinitiationof pages 2-3, yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 3-5) | Onset term: congenital onset / neonatal onset | Natural history remains poorly defined because of few longitudinal cohorts. |
| Diagnostics | Diagnosis currently relies on **phenotype recognition plus molecular testing** (single-gene analysis, gene panels, trio exome sequencing, or broader genomic testing), with segregation confirmation. Cardiac imaging and skeletal radiography are important supportive assessments. (ritelli2019furtherdefiningthe pages 3-5, yauy2018b3gat3relateddisorderwith pages 6-6, baasanjav2011faultyinitiationof pages 3-4) | Diagnostic labels: exome sequencing; gene panel; Sanger confirmation; echocardiography; skeletal radiography | No consensus formal diagnostic criteria or validated standalone biochemical clinical test were identified. |
| Differential diagnosis | Differential diagnoses discussed in the literature include **classic Larsen syndrome**, **CHST3-related autosomal recessive Larsen syndrome**, **Antley-Bixler syndrome**, **Shprintzen-Goldberg syndrome**, **geroderma osteodysplastica**, **spondylodysplastic EDS**, **musculocontractural EDS**, **Noonan syndrome**, **Desbuquois syndrome**, and **otopalatodigital syndrome type II**. (yauy2018b3gat3relateddisorderwith pages 6-6, ritelli2019furtherdefiningthe pages 3-5, baasanjav2011faultyinitiationof pages 8-10) | Differential diagnosis labels as listed | Differential framing comes from case-report clinical reasoning, not guideline-based algorithms. |
| Management / real-world implementation | Management is **supportive and multidisciplinary**: orthopedic surveillance/intervention for dislocations, scoliosis, instability, and fractures; cardiology surveillance/intervention for structural heart disease; rehabilitation/physical therapy; pain management; ophthalmology follow-up; and genetic counseling. Reported real-world interventions include **atrial septal defect repair**, pulmonary hypertension management, and **bisphosphonate treatment** for low bone mineral density in an adolescent patient. (ritelli2019furtherdefiningthe pages 3-5) | NCIT suggestions: Physical Therapy; Orthopedic Procedure; Cardiac Surgical Procedure; Genetic Counseling; Bisphosphonate Therapy | Evidence is limited to case-based management; no standardized treatment algorithm specific to B3GAT3 disease. |
| Pharmacotherapy / advanced therapeutics | **No disease-modifying pharmacotherapy, gene therapy, RNA therapy, or targeted molecular treatment** specific to B3GAT3-related disease was found. (ritelli2019furtherdefiningthe pages 3-5, yauy2018b3gat3relateddisorderwith pages 6-6) | NCIT suggestions if supportive only: Bisphosphonate Therapy; Analgesic Therapy | Negative evidence based on available literature/trial search, not proof of absence of off-label use anywhere. |
| Prognosis | Prognosis is **highly variable**. Severe **p.Gly223Ser** cases showed infantile lethality, with reports that all described patients died before age 1 year; other individuals survive into adolescence/adulthood with chronic orthopedic and cardiac morbidity. (yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 10-12, ritelli2019furtherdefiningthe pages 3-5) | Prognosis labels: variable severity; infantile lethal subset | No survival curves or formal prognostic models exist. |
| Epidemiology / population | Ultra-rare disorder with **no robust prevalence or incidence estimates** identified. Reported families include multiple consanguineous pedigrees; one severe recurrent variant cohort involved families of **Moroccan origin**. (yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 10-12) | Epidemiology label: ultra-rare Mendelian disease | Published population data are case-based only; no registry-derived denominator. |
| Protective/environmental factors | **No established environmental risk factors, protective factors, or gene-environment interactions** specific to this Mendelian disorder were identified. (baasanjav2011faultyinitiationof pages 2-3, ritelli2019furtherdefiningthe pages 10-12) | Not established | Absence reflects evidence gap, not demonstrated nonexistence. |
| Clinical trials | Literature and trial search found **no disease-specific interventional clinical trials** for Larsen-like syndrome, B3GAT3 type. (OpenTargets Search: Larsen-like syndrome B3GAT3 type-B3GAT3) | ClinicalTrials.gov / ICTRP status: none found | Search-negative result; trials could emerge later under broader linkeropathy terminology. |
| Other species / natural disease | **No confirmed naturally occurring veterinary/nonhuman disease** equivalent was identified from the retrieved evidence. (OpenTargets Search: Larsen-like syndrome B3GAT3 type-B3GAT3) | Not established | Evidence gap; available literature focused on engineered models. |
| Model organisms | The clearest direct model is **engineered zebrafish b3gat3 mutant (b3gat3hi307)**. Mutants showed near-abolished CS production with residual HS, undersulfated CS, and abnormal pharyngeal cartilage morphology/ECM, supporting a mechanism in cartilage morphogenesis. (holmborn2012ontheroles pages 1-2, holmborn2012ontheroles pages 8-9) | Model labels: zebrafish mutant; engineered loss-of-function model | Useful mechanistically but does not capture the full human multisystem/cardiac spectrum. |
| Model-mechanism insight | Zebrafish work suggests that when linker-region biosynthesis is impaired, **HS biosynthesis is relatively prioritized over CS**, and defective CS-rich cartilage ECM contributes to malformed cartilage. (holmborn2012ontheroles pages 1-2, holmborn2012ontheroles pages 8-9) | GO suggestions: cartilage morphogenesis; extracellular matrix assembly; heparan sulfate/chondroitin sulfate biosynthesis | Model inference; not directly measured in human tissues beyond fibroblast GAG assays. |
| Recent developments (2023-2024) | No major new disease-specific patient cohort or therapy was found in 2023-2024 from the retrieved search. The main recent advance is a **2024 pathway-level model** emphasizing flux between HSPG/CSPG biosynthesis and how linkeropathy phenotypes may arise from preferential HSPG over CSPG production. (OpenTargets Search: Larsen-like syndrome B3GAT3 type-B3GAT3) | Pathway label: HSPG/CSPG biosynthesis model | Recent literature is mainly review/conceptual rather than new clinical intervention evidence. |


*Table: This compact table summarizes the main evidence-backed knowledge-base facts for Larsen-like syndrome, B3GAT3 type, including identifiers, mechanism, phenotype spectrum, diagnosis, management, prognosis, and models. It also highlights key limitations: very small family-based cohorts, unstable frequency estimates, and the absence of disease-modifying therapy or disease-specific trials.*

## 1. Disease information

### Definition and identifiers

* **Preferred label:** Larsen-like syndrome, B3GAT3 type.
* **Broader/current label:** B3GAT3-related disorder or B3GAT3-related linkeropathy.
* **MONDO:** **MONDO:0009511**.
* **OMIM phenotype:** **245600** (historically Larsen syndrome/“Larsen-like syndrome, B3GAT3 type” in the cited literature).
* **Causal gene:** **B3GAT3**, encoding beta-1,3-glucuronyltransferase 3 (GlcAT-I); Ensembl ENSG00000149541.
* **MeSH/Orphanet/ICD-10/ICD-11:** no disease-specific identifier was established in the retrieved evidence. Coding will generally require a broader congenital skeletal dysplasia/connective-tissue category plus manifestations. A specific code should not be inferred without direct terminology-service verification. Open Targets supports the MONDO–B3GAT3 association with five evidence records and foundational PMIDs including **21763480, 24668659, 25893793, 26086840, 27604308, and 27871226**. (OpenTargets Search: Larsen-like syndrome B3GAT3 type-B3GAT3)

The defining report was Baasanjav et al., published **15 July 2011** in *American Journal of Human Genetics* (PMID **21763480**; DOI/URL: https://doi.org/10.1016/j.ajhg.2011.05.021). Its central conclusion was that faulty proteoglycan synthesis causes cardiac and joint defects, and the authors proposed “Larsen-like syndrome, B3GAT3 type.” (baasanjav2011faultyinitiationof pages 2-3)

## 2. Etiology, risk, and protective factors

The disease is caused by **germline biallelic B3GAT3 variants** and is inherited autosomal recessively. The original pedigree carried homozygous **NM_012200.3:c.830G>A, p.(Arg277Gln)**. The variant segregated with disease, affected a conserved substrate-binding residue, and was absent from 294 population-matched and 850 Berlin blood-donor chromosomes in the original study. (baasanjav2011faultyinitiationof pages 6-7, baasanjav2011faultyinitiationof pages 3-4)

Other reported alleles include **c.419C>T (p.Pro140Leu), c.416C>T (p.Thr139Met), c.245C>T (p.Pro82Leu), c.667G>A (p.Gly223Ser), c.481C>T (p.Arg161Trp), c.889C>T (p.Arg297Trp)**, and compound-heterozygous **c.1A>G (predicted start loss)/c.671T>A (p.Leu224Gln)**. Most reported disease alleles are missense and appear hypomorphic, although direct functional confirmation is not available for every allele. (ritelli2019furtherdefiningthe pages 8-10, ritelli2019furtherdefiningthe pages 10-12)

Consanguinity increases the probability that both parents carry the same rare allele but is not itself causal. The severe p.Gly223Ser series involved healthy first-cousin parents of Moroccan origin; the variant frequency was reported as approximately **8×10⁻⁶ in ExAC**. No validated susceptibility loci, modifier genes, protective alleles, environmental risk or protective factors, infectious triggers, lifestyle effects, or gene–environment interactions have been demonstrated. (yauy2018b3gat3relateddisorderwith pages 2-4)

## 3. Phenotypes

### Musculoskeletal and growth manifestations

The core phenotype begins congenitally or in early childhood and includes short stature, generalized or distal joint hypermobility, multiple dislocations (shoulder, elbow, hip, knee, and proximal radioulnar joints), elbow contractures, radioulnar synostosis, kyphosis/scoliosis, foot deformities, metaphyseal abnormalities, delayed bone age, osteopenia, and variably fractures. Orthopedic burden can progress with growth even though the initiating developmental defect is congenital. Suggested HPO terms include **Short stature; Joint hypermobility; Joint dislocation; Congenital hip dislocation; Radioulnar synostosis; Joint contracture; Scoliosis; Kyphosis; Osteopenia; Low bone mineral density; Multiple fractures; Talipes equinovarus; Hallux valgus; and Pes planus**. (baasanjav2011faultyinitiationof pages 2-3, ritelli2019furtherdefiningthe pages 3-5, ritelli2019furtherdefiningthe pages 8-10, baasanjav2011faultyinitiationof pages 6-7)

In the p.Gly223Ser severe subgroup, reported frequencies included radioulnar synostosis **6/6 postnatal patients**, contractures **100%**, foot deformity **100%**, neonatal fractures **67%**, long fingers **67%**, and joint dislocation approximately **60%**. These numbers must not be generalized to all B3GAT3 genotypes. (yauy2018b3gat3relateddisorderwith pages 2-4)

### Craniofacial, ocular, and cutaneous manifestations

Reported findings include midface hypoplasia, depressed nasal bridge, frontal bossing or broad forehead, hypertelorism or prominent eyes, downslanting palpebral fissures, micrognathia, small mouth, long philtrum, low-set ears, short/webbed neck, blue sclerae, refractive error, strabismus, and occasionally cleft palate or bifid uvula. Craniosynostosis is especially associated with severe presentations. Suggested HPO terms include **Midface retrusion; Depressed nasal bridge; Frontal bossing; Hypertelorism; Proptosis; Downslanting palpebral fissures; Micrognathia; Blue sclerae; Craniosynostosis; Strabismus; Refractive error; Webbed neck; Cleft palate; and Bifid uvula**. (yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 14-16, ritelli2019furtherdefiningthe pages 8-10, baasanjav2011faultyinitiationof pages 3-4)

### Cardiovascular manifestations

Congenital cardiovascular disease is an important clue and includes bicuspid aortic valve, aortic-valve dysplasia, mitral-valve prolapse, atrial or ventricular septal defects, pulmonary hypertension, and aortic-root dilatation. Suggested HPO terms are **Bicuspid aortic valve; Mitral valve prolapse; Atrial septal defect; Ventricular septal defect; Pulmonary hypertension; and Aortic root dilatation**. Cardiovascular disease is enriched in B3GAT3 linkeropathy relative to several related linkeropathies but is not universal. (baasanjav2011faultyinitiationof pages 2-3, ritelli2019furtherdefiningthe pages 3-5, ritelli2019furtherdefiningthe pages 14-16)

### Neurologic, developmental, and quality-of-life effects

Neonatal hypotonia and delayed gross-motor development can occur, often plausibly secondary to skeletal disease and instability. The reported Italian girl walked at age three and had chronic myalgia and severe foot pain; by contrast, the original family had normal mental and motor development. Developmental delay is therefore variable, and a primary behavioral phenotype is not established. Chronic pain, impaired mobility, recurrent dislocations, spinal deformity, fractures, surgery, and cardiac disease are expected to impair daily function, but no disease-specific EQ-5D, SF-36, PROMIS, or other quantitative quality-of-life study was found. Suggested HPO terms include **Hypotonia; Delayed gross motor development; Musculoskeletal pain; and Abnormality of cardiovascular system**. (ritelli2019furtherdefiningthe pages 3-5, baasanjav2011faultyinitiationof pages 6-7)

## 4. Genetic and molecular information

**B3GAT3/GlcAT-I** transfers the fourth sugar, glucuronic acid, to the common **Xyl–Gal–Gal–GlcA** linker through which chondroitin sulfate (CS), dermatan sulfate (DS), and heparan sulfate (HS) chains attach to proteoglycan core proteins. GlcAT-I functions in the Golgi and forms a dimer; Arg277 is positioned in the acceptor/substrate-interaction domain. (mizumoto2018defectsinbiosynthesis pages 9-10, baasanjav2011faultyinitiationof pages 6-7, baasanjav2011faultyinitiationof pages 3-4)

For p.Arg277Gln, patient fibroblasts had only **3–5% of control GlcAT-I activity**. The mutant protein showed reduced abundance and loss of normal cis/cis-medial-Golgi localization, while recombinant mutant enzyme retained similarly reduced catalytic activity despite comparable protein loading. The allele is therefore a hypomorphic loss-of-function allele involving both catalytic dysfunction and reduced protein stability/localization. Cell-surface CS and HS were approximately **65% and 53% of control**, respectively, and immature DS proteoglycans were detected. (baasanjav2011faultyinitiationof pages 8-10, baasanjav2011faultyinitiationof pages 6-7)

All known disease variants are germline; no somatic disease mechanism is recognized. No established modifier gene, disease-specific methylation signature, chromosomal rearrangement, repeat expansion, mitochondrial defect, or large structural abnormality was identified. ACMG classification should be performed separately for each variant using segregation, population frequency, computational evidence, functional data, and current ClinVar submissions; the literature’s “likely pathogenic” designation should not automatically be transferred to every laboratory context. Functional effects of p.Arg161Trp and p.Arg297Trp, for example, were not tested in patient fibroblasts. (ritelli2019furtherdefiningthe pages 3-5, ritelli2019furtherdefiningthe pages 8-10)

## 5. Environmental information

No toxin, radiation, pollution, occupational exposure, diet, smoking, alcohol, exercise pattern, or infectious agent is known to cause or trigger this disorder. It is a congenital Mendelian condition. Environmental and rehabilitative factors may alter complication burden and function, but they have not been studied as etiologic or protective factors. Vaccination and infection-control measures follow routine standards rather than a B3GAT3-specific protocol.

## 6. Mechanism and pathophysiology

The best-supported causal chain is:

**biallelic B3GAT3 dysfunction → reduced/mislocalized Golgi GlcAT-I → incomplete proteoglycan linker tetrasaccharides → reduced or abnormal CS/DS/HS chains → impaired extracellular-matrix assembly and altered presentation of morphogens/growth factors → defective cartilage morphogenesis, endochondral ossification, connective-tissue mechanics, and cardiac-valve/aortic development → dislocations, contractures, short stature, bone fragility, craniofacial abnormalities, and cardiovascular malformations.** (baasanjav2011faultyinitiationof pages 2-3, baasanjav2011faultyinitiationof pages 8-10, baasanjav2011faultyinitiationof pages 6-7, holmborn2012ontheroles pages 1-2)

The upstream lesion is linker synthesis; downstream effects include extracellular-matrix insufficiency and disturbed signaling. Proteoglycans act as structural molecules and co-receptors for BMP, Hedgehog, Wnt, and FGF-family signals, although a specific signaling pathway has not been proven to account for every human manifestation. Relevant suggested GO terms are **glycosaminoglycan biosynthetic process; proteoglycan biosynthetic process; extracellular matrix organization; cartilage development; endochondral ossification; skeletal system development; heart valve development; and Golgi apparatus organization**. Relevant cellular compartments are **Golgi apparatus, cis-Golgi/cis-medial Golgi, cell surface, and extracellular matrix**. (baasanjav2011faultyinitiationof pages 6-7, holmborn2012ontheroles pages 1-2)

Candidate cell types are **chondrocyte (CL term label), osteoblast, fibroblast, valvular interstitial cell, vascular smooth-muscle cell**, and related mesenchymal progenitors. Direct human single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, epigenomic, organoid, iPSC, or CRISPR-screen datasets specific to this disease were not found. Mouse tissue assays showed B3gat3 expression in heart, aorta, bone, and osteoblast cultures, but this is supportive expression evidence rather than a complete disease atlas. (baasanjav2011faultyinitiationof pages 6-7)

A 2024 pathway review proposed that substrate preference and pathway flux can privilege HSPG over CSPG synthesis when the common linker pathway is constrained. This is consistent with zebrafish b3gat3 mutants retaining substantial HS while nearly abolishing CS, but it remains a pathway-level model rather than a tested human therapy. Publication: Ouidja et al., **December 2024**, DOI https://doi.org/10.1042/EBC20240106. (OpenTargets Search: Larsen-like syndrome B3GAT3 type-B3GAT3, holmborn2012ontheroles pages 1-2, holmborn2012ontheroles pages 8-9)

## 7. Anatomical structures affected

Primary sites are cartilage, bone, joints, spine, craniofacial skeleton, tendons/ligaments and other connective tissues, heart valves, septa, and aortic root. Suggested UBERON labels include **cartilage; bone tissue; joint; vertebral column; craniofacial skeleton; heart valve; interatrial septum; aortic root; tendon; and ligament**. Disease can be bilateral and generalized; radioulnar synostosis and limb/joint abnormalities are commonly bilateral, but strict lateralization is not universal. At the subcellular level, the Golgi is the principal biosynthetic compartment and the extracellular matrix is the major downstream affected compartment. (baasanjav2011faultyinitiationof pages 2-3, ritelli2019furtherdefiningthe pages 14-16, baasanjav2011faultyinitiationof pages 6-7)

## 8. Temporal development

Onset is congenital, prenatal, neonatal, or early childhood. Severe disease can be detected prenatally through fractures, craniosynostosis, limb abnormalities, or other skeletal findings. Survivors have a chronic lifelong disorder: congenital dislocations and malformations may be relatively fixed, whereas scoliosis, pain, instability, osteopenia, mobility restriction, and cardiovascular complications may progress. There is no recognized relapsing-remitting course or spontaneous molecular remission. Early vulnerability corresponds to embryonic cartilage, bone, craniofacial, and cardiovascular development; practical intervention windows concern early recognition of cervical instability, cardiac disease, dislocations, and bone fragility rather than reversal of the biochemical defect. (yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 3-5, baasanjav2011faultyinitiationof pages 6-7)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For a couple in whom both partners carry the same pathogenic B3GAT3 allele, each pregnancy has the conventional 25% affected, 50% carrier, and 25% non-carrier probability. Expressivity is markedly variable across alleles; formal penetrance, carrier frequency, sex ratio, incidence, and prevalence have not been quantified. No anticipation mechanism is expected, and germline mosaicism has not been established. (yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 10-12)

The disease is ultra-rare and reported across multiple ancestries. Moroccan families recur in the p.Gly223Ser series, but the data are insufficient to prove a population founder effect. Consanguinity was present in most early families and facilitates homozygosity for rare alleles. There is no evidence of sex-limited expression. (yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 10-12)

## 10. Diagnostics

### Clinical and imaging evaluation

Suspect B3GAT3-related disease when congenital joint dislocations or contractures coexist with short stature/skeletal dysplasia, radioulnar synostosis, characteristic craniofacial findings, osteopenia/fractures, and congenital cardiac disease. Baseline assessment should include a skeletal survey or targeted radiographs; spine and cervical-instability imaging when indicated; echocardiography with aortic-root measurements; ophthalmologic examination; growth and developmental assessment; and bone-density evaluation in appropriate children or adults. These evaluations characterize manifestations but are not individually diagnostic. (ritelli2019furtherdefiningthe pages 3-5, ritelli2019furtherdefiningthe pages 8-10, baasanjav2011faultyinitiationof pages 3-4)

GlcAT-I activity and cellular GAG analysis are research-supportive biomarkers, not validated routine diagnostic thresholds. Routine blood and urine chemistry may be nonspecific. Biopsy is not ordinarily required. (baasanjav2011faultyinitiationof pages 8-10, baasanjav2011faultyinitiationof pages 6-7)

### Genetic testing

A practical sequence is: (1) a skeletal-dysplasia/connective-tissue disorder panel containing **B3GAT3, B4GALT7, B3GALT6, XYLT1, XYLT2, CHST3, CHST14, DSE, FLNB, POR, FGFR2, CYP26B1**, and phenotype-relevant genes; or (2) trio WES/WGS where the phenotype is atypical; followed by orthogonal confirmation and parental segregation. WES identified the severe p.Gly223Ser disorder, while panel and Sanger testing confirmed additional patients. Copy-number analysis should be included when sequencing is negative. CMA/karyotype may be appropriate for a syndromic child but will not detect most reported B3GAT3 missense alleles. FISH, mitochondrial sequencing, and repeat-expansion testing are not disease-specific tests. (yauy2018b3gat3relateddisorderwith pages 2-4, yauy2018b3gat3relateddisorderwith pages 6-6, ritelli2019furtherdefiningthe pages 3-5)

Differential diagnoses include FLNB-related classic Larsen syndrome, CHST3-related recessive Larsen phenotype, B4GALT7/B3GALT6 spondylodysplastic EDS, XYLT1/XYLT2 linkeropathies, Desbuquois dysplasia, musculocontractural EDS, Antley-Bixler syndrome, Shprintzen-Goldberg syndrome, geroderma osteodysplastica, Noonan syndrome, and otopalatodigital syndrome type II. In prenatal or craniosynostosis/bone-fragility presentations, B3GAT3 should be considered alongside **POR, FGFR2, and CYP26B1**. (yauy2018b3gat3relateddisorderwith pages 6-6, baasanjav2011faultyinitiationof pages 8-10)

No validated population newborn screen exists. Cascade testing of relatives and targeted carrier, prenatal, or preimplantation testing are possible once familial pathogenic variants are known.

## 11. Outcome and prognosis

Prognosis is allele- and severity-dependent. In the reported p.Gly223Ser cohort, all described patients died before one year, indicating a severe infantile-lethal subgroup; reported complications included neonatal fractures, craniosynostosis, contractures, and cardiovascular abnormalities. Other genotypes permit survival into adolescence and adulthood, but with chronic orthopedic disability, pain, spinal disease, low bone density, recurrent operations, and cardiac surveillance needs. (yauy2018b3gat3relateddisorderwith pages 2-4, ritelli2019furtherdefiningthe pages 3-5)

No population survival curve, five- or ten-year survival statistic, mortality rate, validated prognostic score, or prognostic biomarker exists. Potential adverse indicators inferred from cases include severe neonatal fractures, respiratory/diaphragmatic involvement, major congenital heart disease, pulmonary hypertension, craniosynostosis, and cervical instability. Recovery from the underlying disorder is not expected, although correction of individual dislocations, deformities, instability, or cardiac lesions may improve function and risk.

## 12. Treatment and current implementation

There is **no approved disease-modifying treatment** and no disease-specific interventional trial was identified. Care is multidisciplinary and manifestation-directed:

* **Orthopedics/spine:** surveillance and individualized reduction, stabilization, casting/bracing, or reconstructive surgery for dislocations, contractures, scoliosis, foot deformity, and cervical instability.
* **Cardiology/cardiothoracic care:** serial echocardiography and intervention for septal defects, valve disease, aortic dilatation, or pulmonary hypertension. An affected adolescent underwent atrial-septal-defect repair.
* **Bone health:** nutrition, vitamin D/calcium sufficiency, fall/fracture prevention, and specialist-guided antiresorptive treatment. Bisphosphonate therapy was used in one patient with low bone mineral density, but no response rate or B3GAT3-specific efficacy estimate exists.
* **Rehabilitation:** cautious physical and occupational therapy, mobility aids, pain management, and avoidance of maneuvers that provoke dislocation or threaten an unstable cervical spine.
* **Ophthalmology, growth/endocrinology, respiratory care, and developmental services** according to manifestations.
* **Genetic counseling** for recurrence risk and reproductive options. (ritelli2019furtherdefiningthe pages 3-5)

Suggested NCIT intervention labels include **Genetic Counseling, Physical Therapy, Occupational Therapy, Orthopedic Surgical Procedure, Cardiac Surgical Procedure, Echocardiography, and Bisphosphonate Therapy**. No B3GAT3-specific pharmacogenomic recommendation, gene replacement, genome editing, antisense, siRNA, mRNA, cell therapy, immunotherapy, or targeted small molecule has entered established clinical use.

## 13. Prevention

Primary prevention by lifestyle or vaccination is not applicable to occurrence of this recessive genetic disorder. Reproductive prevention options are voluntary carrier/cascade testing, genetic counseling, prenatal diagnosis, and preimplantation genetic testing after familial variants are established. Secondary prevention consists of early molecular diagnosis and surveillance for cardiac disease, cervical instability, progressive scoliosis, dislocation, hearing/vision issues, low bone density, and fracture. Tertiary prevention includes rehabilitation, injury avoidance, bone-health measures, timely orthopedic/cardiac intervention, and peri-anesthetic attention to airway and cervical-spine abnormalities. No public-health environmental intervention or chemoprophylaxis is specific to B3GAT3 disease.

## 14. Other species and natural disease

No verified naturally occurring B3GAT3-equivalent veterinary disease, breed association, zoonotic transmission, or cross-species infectious susceptibility was found. The condition is noninfectious and has no zoonotic potential. Comparative evidence comes from engineered laboratory models rather than natural animal cases.

## 15. Model organisms

The most direct model is the engineered **b3gat3hi307 zebrafish** (*Danio rerio*; NCBI Taxonomy 7955). Mutants have reduced common-linker availability, near-abolition of CS biosynthesis, retention of roughly half-normal HS production, altered CS sulfation, and abnormal pharyngeal-cartilage morphology. The study concluded that “HS biosynthesis is prioritized over CS biosynthesis” under linker limitation; impaired CS particularly disrupted extracellular matrix around chondrocytes, whereas HS defects more strongly affected chondrocyte intercalation. Publication: Holmborn et al., **28 September 2012**, *Journal of Biological Chemistry*, DOI https://doi.org/10.1074/jbc.M112.401646. (holmborn2012ontheroles pages 1-2, holmborn2012ontheroles pages 8-9)

This model is useful for cartilage morphogenesis, GAG flux, extracellular-matrix biology, and candidate-rescue studies. Limitations include developmental-stage and species differences and incomplete reproduction of human valve, aortic, neurologic, and long-term orthopedic disease. Retrieved mouse evidence primarily documented B3gat3 tissue expression rather than a fully characterized disease-equivalent model; claims about a definitive mouse phenocopy should therefore be avoided. (baasanjav2011faultyinitiationof pages 6-7)

## Research outlook and expert analysis

The principal expert consensus is that B3GAT3 disease belongs to a **continuum bridging skeletal dysplasia and Ehlers-Danlos–like connective-tissue disease**, rather than several completely separate syndromes. The strongest research priorities are international natural-history aggregation, standardized variant curation, longitudinal cardiac and skeletal outcomes, validated GAG biomarkers, allele-specific functional assays, and human chondrocyte/valvular iPSC models. The 2023–2024 search found no major new disease-specific patient cohort or therapeutic study; recent progress is predominantly conceptual glycobiology rather than clinical translation. (ritelli2019furtherdefiningthe pages 10-12, ritelli2019furtherdefiningthe pages 1-3, OpenTargets Search: Larsen-like syndrome B3GAT3 type-B3GAT3)

### Key primary and review sources

1. Baasanjav S, et al. “Faulty initiation of proteoglycan synthesis causes cardiac and joint defects.” *Am J Hum Genet.* **15 July 2011**;89:15–27. PMID: **21763480**. https://doi.org/10.1016/j.ajhg.2011.05.021. Direct human pedigree, biochemical, cellular, and recombinant-enzyme evidence. (baasanjav2011faultyinitiationof pages 2-3, baasanjav2011faultyinitiationof pages 6-7)
2. Yauy K, et al. “B3GAT3-related disorder with craniosynostosis and bone fragility due to a unique mutation.” *Genet Med.* **February 2018**;20:269–274. https://doi.org/10.1038/gim.2017.109. Direct severe-phenotype human series. (yauy2018b3gat3relateddisorderwith pages 2-4, yauy2018b3gat3relateddisorderwith pages 6-6)
3. Ritelli M, et al. “Further Defining the Phenotypic Spectrum of B3GAT3 Mutations and Literature Review on Linkeropathy Syndromes.” *Genes.* **August 2019**;10:631. https://doi.org/10.3390/genes10090631. New human case plus aggregated review. (ritelli2019furtherdefiningthe pages 10-12, ritelli2019furtherdefiningthe pages 3-5)
4. Holmborn K, et al. “On the Roles and Regulation of Chondroitin Sulfate and Heparan Sulfate in Zebrafish Pharyngeal Cartilage Morphogenesis.” *J Biol Chem.* **28 September 2012**;287:33905–33916. https://doi.org/10.1074/jbc.M112.401646. Engineered zebrafish evidence. (holmborn2012ontheroles pages 1-2, holmborn2012ontheroles pages 8-9)

Quoted abstract language should be interpreted in context. The 2019 review states: “The term linkeropathies (LKs) refers to a group of rare heritable connective tissue disorders,” and concludes that they form “a phenotypic continuum bridging EDS and skeletal disorders.” The zebrafish study’s abstract-level conclusion is that “HS biosynthesis is prioritized over CS biosynthesis.” These statements summarize review/model interpretations and do not substitute for patient-level outcome data. (ritelli2019furtherdefiningthe pages 1-3, holmborn2012ontheroles pages 1-2)

References

1. (baasanjav2011faultyinitiationof pages 2-3): Sevjidmaa Baasanjav, Lihadh Al-Gazali, Taishi Hashiguchi, Shuji Mizumoto, Bjoern Fischer, Denise Horn, Dominik Seelow, Bassam R. Ali, Samir A.A. Aziz, Ruth Langer, Ahmed A.H. Saleh, Christian Becker, Gudrun Nürnberg, Vincent Cantagrel, Joseph G. Gleeson, Delphine Gomez, Jean-Baptiste Michel, Sigmar Stricker, Tom H. Lindner, Peter Nürnberg, Kazuyuki Sugahara, Stefan Mundlos, and Katrin Hoffmann. Faulty initiation of proteoglycan synthesis causes cardiac and joint defects. American journal of human genetics, 89 1:15-27, Jul 2011. URL: https://doi.org/10.1016/j.ajhg.2011.05.021, doi:10.1016/j.ajhg.2011.05.021. This article has 152 citations and is from a highest quality peer-reviewed journal.

2. (yauy2018b3gat3relateddisorderwith pages 2-4): Kevin Yauy, Frederic Tran Mau-Them, Marjolaine Willems, Christine Coubes, Patricia Blanchet, Christian Herlin, Ikram Taleb Arrada, Elodie Sanchez, Jean-Michel Faure, Marie-Pascale Le Gac, Olivier Prodhomme, Anne Boland, Vincent Meyer, Jean-Baptiste Rivière, Yannis Duffourd, Jean-François Deleuze, Thomas Guignard, Guillaume Captier, Mouna Barat-Houari, and David Genevieve. B3gat3-related disorder with craniosynostosis and bone fragility due to a unique mutation. Genetics in Medicine, 20:269-274, Feb 2018. URL: https://doi.org/10.1038/gim.2017.109, doi:10.1038/gim.2017.109. This article has 35 citations and is from a highest quality peer-reviewed journal.

3. (ritelli2019furtherdefiningthe pages 10-12): Marco Ritelli, Valeria Cinquina, Edoardo Giacopuzzi, Marina Venturini, Nicola Chiarelli, and Marina Colombi. Further defining the phenotypic spectrum of b3gat3 mutations and literature review on linkeropathy syndromes. Genes, 10:631, Aug 2019. URL: https://doi.org/10.3390/genes10090631, doi:10.3390/genes10090631. This article has 47 citations.

4. (OpenTargets Search: Larsen-like syndrome B3GAT3 type-B3GAT3): Open Targets Query (Larsen-like syndrome B3GAT3 type-B3GAT3, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (ritelli2019furtherdefiningthe pages 1-3): Marco Ritelli, Valeria Cinquina, Edoardo Giacopuzzi, Marina Venturini, Nicola Chiarelli, and Marina Colombi. Further defining the phenotypic spectrum of b3gat3 mutations and literature review on linkeropathy syndromes. Genes, 10:631, Aug 2019. URL: https://doi.org/10.3390/genes10090631, doi:10.3390/genes10090631. This article has 47 citations.

6. (mizumoto2018defectsinbiosynthesis pages 9-10): Shuji Mizumoto. Defects in biosynthesis of glycosaminoglycans cause hereditary bone, skin, heart, immune, and neurological disorders. Trends in Glycoscience and Glycotechnology, 30:E67-E89, May 2018. URL: https://doi.org/10.4052/tigg.1812.2e, doi:10.4052/tigg.1812.2e. This article has 14 citations and is from a peer-reviewed journal.

7. (ritelli2019furtherdefiningthe pages 8-10): Marco Ritelli, Valeria Cinquina, Edoardo Giacopuzzi, Marina Venturini, Nicola Chiarelli, and Marina Colombi. Further defining the phenotypic spectrum of b3gat3 mutations and literature review on linkeropathy syndromes. Genes, 10:631, Aug 2019. URL: https://doi.org/10.3390/genes10090631, doi:10.3390/genes10090631. This article has 47 citations.

8. (baasanjav2011faultyinitiationof pages 8-10): Sevjidmaa Baasanjav, Lihadh Al-Gazali, Taishi Hashiguchi, Shuji Mizumoto, Bjoern Fischer, Denise Horn, Dominik Seelow, Bassam R. Ali, Samir A.A. Aziz, Ruth Langer, Ahmed A.H. Saleh, Christian Becker, Gudrun Nürnberg, Vincent Cantagrel, Joseph G. Gleeson, Delphine Gomez, Jean-Baptiste Michel, Sigmar Stricker, Tom H. Lindner, Peter Nürnberg, Kazuyuki Sugahara, Stefan Mundlos, and Katrin Hoffmann. Faulty initiation of proteoglycan synthesis causes cardiac and joint defects. American journal of human genetics, 89 1:15-27, Jul 2011. URL: https://doi.org/10.1016/j.ajhg.2011.05.021, doi:10.1016/j.ajhg.2011.05.021. This article has 152 citations and is from a highest quality peer-reviewed journal.

9. (baasanjav2011faultyinitiationof pages 6-7): Sevjidmaa Baasanjav, Lihadh Al-Gazali, Taishi Hashiguchi, Shuji Mizumoto, Bjoern Fischer, Denise Horn, Dominik Seelow, Bassam R. Ali, Samir A.A. Aziz, Ruth Langer, Ahmed A.H. Saleh, Christian Becker, Gudrun Nürnberg, Vincent Cantagrel, Joseph G. Gleeson, Delphine Gomez, Jean-Baptiste Michel, Sigmar Stricker, Tom H. Lindner, Peter Nürnberg, Kazuyuki Sugahara, Stefan Mundlos, and Katrin Hoffmann. Faulty initiation of proteoglycan synthesis causes cardiac and joint defects. American journal of human genetics, 89 1:15-27, Jul 2011. URL: https://doi.org/10.1016/j.ajhg.2011.05.021, doi:10.1016/j.ajhg.2011.05.021. This article has 152 citations and is from a highest quality peer-reviewed journal.

10. (ritelli2019furtherdefiningthe pages 14-16): Marco Ritelli, Valeria Cinquina, Edoardo Giacopuzzi, Marina Venturini, Nicola Chiarelli, and Marina Colombi. Further defining the phenotypic spectrum of b3gat3 mutations and literature review on linkeropathy syndromes. Genes, 10:631, Aug 2019. URL: https://doi.org/10.3390/genes10090631, doi:10.3390/genes10090631. This article has 47 citations.

11. (ritelli2019furtherdefiningthe pages 3-5): Marco Ritelli, Valeria Cinquina, Edoardo Giacopuzzi, Marina Venturini, Nicola Chiarelli, and Marina Colombi. Further defining the phenotypic spectrum of b3gat3 mutations and literature review on linkeropathy syndromes. Genes, 10:631, Aug 2019. URL: https://doi.org/10.3390/genes10090631, doi:10.3390/genes10090631. This article has 47 citations.

12. (holmborn2012ontheroles pages 1-2): Katarina Holmborn, Judith Habicher, Zsolt Kasza, Anna S. Eriksson, Beata Filipek-Gorniok, Sandeep Gopal, John R. Couchman, Per E. Ahlberg, Malgorzata Wiweger, Dorothe Spillmann, Johan Kreuger, and Johan Ledin. On the roles and regulation of chondroitin sulfate and heparan sulfate in zebrafish pharyngeal cartilage morphogenesis. Journal of Biological Chemistry, 287:33905-33916, Sep 2012. URL: https://doi.org/10.1074/jbc.m112.401646, doi:10.1074/jbc.m112.401646. This article has 71 citations and is from a domain leading peer-reviewed journal.

13. (holmborn2012ontheroles pages 8-9): Katarina Holmborn, Judith Habicher, Zsolt Kasza, Anna S. Eriksson, Beata Filipek-Gorniok, Sandeep Gopal, John R. Couchman, Per E. Ahlberg, Malgorzata Wiweger, Dorothe Spillmann, Johan Kreuger, and Johan Ledin. On the roles and regulation of chondroitin sulfate and heparan sulfate in zebrafish pharyngeal cartilage morphogenesis. Journal of Biological Chemistry, 287:33905-33916, Sep 2012. URL: https://doi.org/10.1074/jbc.m112.401646, doi:10.1074/jbc.m112.401646. This article has 71 citations and is from a domain leading peer-reviewed journal.

14. (yauy2018b3gat3relateddisorderwith pages 6-6): Kevin Yauy, Frederic Tran Mau-Them, Marjolaine Willems, Christine Coubes, Patricia Blanchet, Christian Herlin, Ikram Taleb Arrada, Elodie Sanchez, Jean-Michel Faure, Marie-Pascale Le Gac, Olivier Prodhomme, Anne Boland, Vincent Meyer, Jean-Baptiste Rivière, Yannis Duffourd, Jean-François Deleuze, Thomas Guignard, Guillaume Captier, Mouna Barat-Houari, and David Genevieve. B3gat3-related disorder with craniosynostosis and bone fragility due to a unique mutation. Genetics in Medicine, 20:269-274, Feb 2018. URL: https://doi.org/10.1038/gim.2017.109, doi:10.1038/gim.2017.109. This article has 35 citations and is from a highest quality peer-reviewed journal.

15. (baasanjav2011faultyinitiationof pages 3-4): Sevjidmaa Baasanjav, Lihadh Al-Gazali, Taishi Hashiguchi, Shuji Mizumoto, Bjoern Fischer, Denise Horn, Dominik Seelow, Bassam R. Ali, Samir A.A. Aziz, Ruth Langer, Ahmed A.H. Saleh, Christian Becker, Gudrun Nürnberg, Vincent Cantagrel, Joseph G. Gleeson, Delphine Gomez, Jean-Baptiste Michel, Sigmar Stricker, Tom H. Lindner, Peter Nürnberg, Kazuyuki Sugahara, Stefan Mundlos, and Katrin Hoffmann. Faulty initiation of proteoglycan synthesis causes cardiac and joint defects. American journal of human genetics, 89 1:15-27, Jul 2011. URL: https://doi.org/10.1016/j.ajhg.2011.05.021, doi:10.1016/j.ajhg.2011.05.021. This article has 152 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Larsen-like_Syndrome_B3GAT3_Type-deep-research-falcon_artifacts/artifact-00.md)