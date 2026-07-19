---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T09:53:49.444041'
end_time: '2026-06-30T10:08:55.042047'
duration_seconds: 905.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mixed Neuronal-Glial Tumor
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 44
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Mixed_Neuronal-Glial_Tumor-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Mixed_Neuronal-Glial_Tumor-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mixed Neuronal-Glial Tumor
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Mixed Neuronal-Glial Tumor** covering all of the
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
- **Disease Name:** Mixed Neuronal-Glial Tumor
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Mixed Neuronal-Glial Tumor** covering all of the
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


# Comprehensive Research Report: Mixed Neuronal-Glial Tumor

## 1. Disease Information

### Overview
Mixed neuronal-glial tumors (also termed glioneuronal tumors) are a heterogeneous group of rare primary central nervous system (CNS) neoplasms composed of both neuronal and glial cell populations in varying proportions (crainic2023rareneuronalglial pages 1-2). They represent less than 2% of all primary CNS tumors and predominantly affect children and young adults, with a strong predilection for the temporal and frontal lobes and a frequent association with epilepsy (crainic2023rareneuronalglial pages 1-2, vaz2022uncommonglioneuronaltumors pages 1-4). The 2021 WHO Classification of Tumors of the Central Nervous System (CNS5, 5th edition) reorganized these tumors into one of six families: "Glioneuronal and neuronal tumors," alongside closely related entities in the "Pediatric-type diffuse low-grade gliomas" and "Circumscribed astrocytic gliomas" families (bale2022the2021who pages 1-2, bale2022the2021who pages 2-3).

### Key Identifiers
- **MONDO ID:** MONDO:0016729 (mixed neuronal-glial tumor) (OpenTargets Search: mixed neuronal-glial tumor,ganglioglioma,glioneuronal tumor)
- **ICD-O-3 codes:** Multiple codes apply depending on subtype (e.g., 9505/1 for ganglioglioma, 9413/0 for DNET)
- **MeSH:** Glioneuronal tumors / Neuronal and mixed neuronal-glial tumors
- **Common Synonyms:** Glioneuronal tumor, mixed glioneuronal neoplasm, neuronal-glial tumor

### Subtypes per WHO 2021 Classification
The following table provides a comprehensive overview of subtypes, grades, molecular features, histopathology, age of onset, and clinical presentation:

| Tumor type | WHO 2021 status / grade | Key molecular alterations | Characteristic histology / IHC markers | Typical age of onset | Common clinical presentation |
|---|---|---|---|---|---|
| Ganglioglioma | CNS WHO grade 1 | **BRAF p.V600E** most common; less often **FGFR1**, **KRAS**, **NF1**, **H3-3A/H3 K27M**, **RAF1** alterations; MAPK-pathway activation (pereira2026molecularfeaturesin pages 1-2, pereira2026molecularfeaturesin pages 2-4, crainic2023rareneuronalglial pages 6-8) | Dysmorphic neuronal cells with neoplastic glial component; eosinophilic granular bodies, lymphocytic infiltrates, CD34+ ramified cells; neuronal cells synaptophysin+/chromogranin A+; glial cells GFAP+/OLIG2+; Ki-67 usually <3% (crainic2023rareneuronalglial pages 6-8, vaz2022uncommonglioneuronaltumors pages 1-4) | Usually childhood to young adulthood (vaz2022uncommonglioneuronaltumors pages 1-4, crainic2023rareneuronalglial pages 1-2) | Long-standing focal epilepsy/seizures, often temporal lobe; headaches less common (crainic2023rareneuronalglial pages 1-2, vaz2022uncommonglioneuronaltumors pages 1-4) |
| Dysembryoplastic neuroepithelial tumor (DNET) | CNS WHO grade 1 | **FGFR1** alterations in >75%; **BRAF p.V600E** in <1/3; MAPK-pathway altered (crainic2023rareneuronalglial pages 6-8, kobow2021moleculardiagnosticsin pages 2-4) | Specific glioneuronal element with columns of oligodendroglia-like cells in myxoid matrix and “floating neurons”; Olig2+ oligodendroglia-like cells; floating neurons NeuN+/synaptophysin+ (crainic2023rareneuronalglial pages 6-8) | Usually children/adolescents and young adults (crainic2023rareneuronalglial pages 1-2) | Drug-resistant epilepsy, often cortical/temporal lesions (crainic2023rareneuronalglial pages 1-2, xie2023lowgradeepilepsyassociatedneuroepithelial pages 2-3) |
| Papillary glioneuronal tumor | CNS WHO grade 1 | **SLC44A1::PRKCA** fusion characteristic; occasional **PDGFRA** alterations reported (crainic2023rareneuronalglial pages 4-5, vaz2022uncommonglioneuronaltumors pages 4-6) | Pseudopapillary / papillary architecture with GFAP+/S100+ glial lining cells and synaptophysin+/neuronal nuclear protein+ interpapillary neuronal elements; OLIG2+ oligodendrocyte-like cells may be present (vaz2022uncommonglioneuronaltumors pages 4-6) | Mostly young adults (crainic2023rareneuronalglial pages 4-5) | Seizures and/or headaches from circumscribed supratentorial mass (crainic2023rareneuronalglial pages 4-5, crainic2023rareneuronalglial pages 1-2) |
| Rosette-forming glioneuronal tumor (RGNT) | CNS WHO grade 1 | **FGFR1** hotspot mutations, often with **PIK3CA**, **PIK3R1**, or **NF1** co-alterations (crainic2023rareneuronalglial pages 4-5, vaz2022uncommonglioneuronaltumors pages 6-7) | Neurocytic rosettes and perivascular pseudorosettes with astrocytic component; neuronal cells synaptophysin+/MAP2+/NSE+; glial cells GFAP+/OLIG2+/S100+ (vaz2022uncommonglioneuronaltumors pages 6-7) | Typically children/young adults (vaz2022uncommonglioneuronaltumors pages 1-4, crainic2023rareneuronalglial pages 4-5) | Headache, ataxia, hydrocephalus, posterior fossa / fourth-ventricle symptoms rather than epilepsy (vaz2022uncommonglioneuronaltumors pages 6-7, crainic2023rareneuronalglial pages 4-5) |
| Diffuse leptomeningeal glioneuronal tumor (DLGNT) | CNS WHO grade 1 in WHO 2021; methylation subclasses MC-1 and MC-2 described (vaz2022uncommonglioneuronaltumors pages 6-7, singh2023currentstatusof pages 3-4) | Frequently **KIAA1549::BRAF** fusion; also 1p loss and MAPK-pathway alterations; molecular subclassing by methylation clinically relevant (vaz2022uncommonglioneuronaltumors pages 6-7, singh2023currentstatusof pages 3-4, bent2025updatedeanoguideline pages 3-4) | Oligodendroglial-like cells in leptomeningeal/desmoplastic or myxoid background; OLIG2+, S100+, MAP2+ in oligodendroglial cells, GFAP+ astrocytic component (vaz2022uncommonglioneuronaltumors pages 6-7) | Mainly pediatric, but can occur across ages (singh2023currentstatusof pages 3-4, rio2024newcnstumor pages 2-4) | Signs of diffuse leptomeningeal disease: hydrocephalus, cranial/spinal symptoms, multifocal neurologic deficits; epilepsy less typical (vaz2022uncommonglioneuronaltumors pages 6-7) |
| Myxoid glioneuronal tumor (MGT/MGNT) | CNS WHO grade 1 | Recurrent **PDGFRA p.K385** mutation; DNT-like methylation profile (bale2022the2021who pages 8-9, capper2023eanoguidelineon pages 11-12) | Oligodendrocyte-like cells in prominent myxoid/mucin-rich stroma with floating neurons and sometimes neurocytic rosettes; strong MAP2/synaptophysin in neuronal component, often GFAP-negative (bale2022the2021who pages 5-6, vaz2022uncommonglioneuronaltumors pages 6-7, bale2022the2021who pages 8-9) | Usually children and young adults (bale2022the2021who pages 8-9) | Seizures or headaches; often septum pellucidum / periventricular lesion discovered on imaging (bale2022the2021who pages 8-9, rio2024newcnstumor pages 2-4) |
| Diffuse glioneuronal tumor with oligodendroglioma-like features and nuclear clusters (DGONC) | Provisional new type in WHO 2021 glioneuronal/neuronal family | Distinct methylation class; recurrent **monosomy 14** / chromosome 14 methylome abnormality (bale2022the2021who pages 1-2, xie2023lowgradeepilepsyassociatedneuroepithelial pages 2-3, bale2022the2021who pages 8-9) | Diffuse tumor with oligodendroglioma-like perinuclear halos and clustered nuclei; synaptophysin+/NeuN+/MAP2+/Olig2+, usually GFAP− or limited GFAP (crainic2023rareneuronalglial pages 5-6, bale2022the2021who pages 3-5) | Predominantly pediatric / young patients (bale2022the2021who pages 1-2, xie2023lowgradeepilepsyassociatedneuroepithelial pages 2-3) | Seizures and focal neurologic symptoms depending on cortical location (bale2022the2021who pages 3-5, xie2023lowgradeepilepsyassociatedneuroepithelial pages 2-3) |
| Desmoplastic infantile ganglioglioma (DIG) | CNS WHO grade 1 | Molecular drivers less consistently defined than other entities; belongs to infantile glioneuronal spectrum in WHO 2021 (vaz2022uncommonglioneuronaltumors pages 1-4, rio2024newcnstumor pages 2-4) | Desmoplastic stroma with astroglial and neuronal/ganglion cell elements; glial cells GFAP+, neuronal cells synaptophysin+ (vaz2022uncommonglioneuronaltumors pages 1-4, rio2024newcnstumor pages 2-4) | Infancy, usually within first 2 years of life (vaz2022uncommonglioneuronaltumors pages 1-4) | Macrocephaly, enlarging head circumference, seizures, signs of raised intracranial pressure from large superficial cystic/solid mass (vaz2022uncommonglioneuronaltumors pages 1-4, rio2024newcnstumor pages 2-4) |
| Polymorphous low-grade neuroepithelial tumor of the young (PLNTY) | Pediatric-type diffuse low-grade glioma in WHO 2021 (not in glioneuronal family, but overlaps clinically/pathologically with LEATs) (bale2022the2021who pages 1-2, rio2024newcnstumor pages 2-4) | MAPK-pathway altered; **BRAF p.V600E**, **FGFR2/FGFR3** fusions and related FGFR-family alterations (singh2023currentstatusof pages 3-4, bale2022the2021who pages 3-5, bale2022the2021who pages 8-9) | Oligodendroglioma-like / polymorphous infiltrative tumor; strong CD34 expression; strong MAP2 and synaptophysin, mostly GFAP-negative; may show perivascular pseudorosettes (bale2022the2021who pages 3-5, bale2022the2021who pages 8-9) | Children, adolescents, young adults (bale2022the2021who pages 1-2, bale2022the2021who pages 8-9) | Epileptogenic cortical tumor with chronic focal seizures (singh2023currentstatusof pages 3-4, bale2022the2021who pages 8-9) |
| Multinodular and vacuolating neuronal tumor (MVNT) | CNS WHO grade 1 | MAPK-pathway alterations reported; recognized as new WHO 2021 neuronal/glioneuronal-type entity (bale2022the2021who pages 1-2, xie2023lowgradeepilepsyassociatedneuroepithelial pages 2-3) | Multinodular lesion composed of vacuolated neuronal cells; HuC/HuD+, OLIG2+, α-internexin+, weak/negative synaptophysin and neurofilament in some cells (vaz2022uncommonglioneuronaltumors pages 8-9, bale2022the2021who pages 5-6) | Often adults, but can occur across a wide age range (bale2022the2021who pages 5-6, rio2024newcnstumor pages 2-4) | Often incidental; may present with seizures or headaches (bale2022the2021who pages 5-6, vaz2022uncommonglioneuronaltumors pages 8-9) |
| Anaplastic ganglioglioma | CNS WHO grade 3 | May harbor **BRAF p.V600E** and occasionally **H3** alterations; MAPK-driven biology in subset (vaz2022uncommonglioneuronaltumors pages 1-4, vaz2022uncommonglioneuronaltumors pages 4-6) | Dysplastic neuronal cells plus anaplastic glial component, increased cellularity, pleomorphism, frequent mitoses, microvascular proliferation, necrosis; GFAP+/synaptophysin+/CD34+ pattern retained in components (vaz2022uncommonglioneuronaltumors pages 1-4, vaz2022uncommonglioneuronaltumors pages 4-6) | Children to adults (vaz2022uncommonglioneuronaltumors pages 1-4, crainic2023rareneuronalglial pages 6-8) | Seizures, progressive focal deficits, mass effect; more aggressive course than grade 1 ganglioglioma (crainic2023rareneuronalglial pages 6-8, vaz2022uncommonglioneuronaltumors pages 1-4) |
| Central neurocytoma | CNS WHO grade 2 | No single pathognomonic alteration routinely used in WHO; molecular heterogeneity reported (vaz2022uncommonglioneuronaltumors pages 8-9, rio2024newcnstumor pages 2-4) | Uniform round neurocytic cells with scant cytoplasm and neurocytic rosettes; synaptophysin+ and neuron-specific enolase+; OLIG2− (vaz2022uncommonglioneuronaltumors pages 8-9) | Young adults (median around 30 years) (crainic2023rareneuronalglial pages 4-5) | Intraventricular mass causing headache, hydrocephalus, visual symptoms; seizures less common (crainic2023rareneuronalglial pages 4-5, vaz2022uncommonglioneuronaltumors pages 8-9) |
| Extraventricular neurocytoma | CNS WHO grade 2 | **FGFR1::TACC1** fusion in about two-thirds in one series/reviewed cohort (crainic2023rareneuronalglial pages 4-5) | Neurocytic tumor outside ventricles; synaptophysin+ neuronal phenotype, similar to central neurocytoma but extraventricular location (crainic2023rareneuronalglial pages 4-5, rio2024newcnstumor pages 2-4) | Young adults (median around 30 years) (crainic2023rareneuronalglial pages 4-5) | Seizures and headaches are common (crainic2023rareneuronalglial pages 4-5) |


*Table: This table summarizes major mixed neuronal-glial and closely related neuroepithelial tumor subtypes relevant to the WHO 2021 CNS classification, with practical emphasis on grade, molecular drivers, pathology, age, and presentation. It is useful as a quick reference for disease characterization and knowledge-base curation.*

---

## 2. Etiology

### Disease Causal Factors
Mixed neuronal-glial tumors are primarily driven by somatic genetic alterations, particularly those activating the mitogen-activated protein kinase (MAPK) signaling pathway. Gene expression studies have identified alterations in the RAS–RAF–MAPK and PI3K–AKT–mTOR signaling pathways, which affect cell proliferation, differentiation, autophagy, protein synthesis, and cell survival (kobow2021moleculardiagnosticsin pages 2-4). Experimental evidence demonstrates that BRAF V600E mutations in neural progenitors during embryonic development can reproduce ganglioglioma histopathological features and lead to epileptic seizures (kobow2021moleculardiagnosticsin pages 2-4). The tumors are generally considered developmental or hamartomatous neoplasms arising from aberrant neurodevelopment rather than from acquired environmental exposures.

### Genetic Risk Factors
- **BRAF V600E:** The most common somatic alteration, present in approximately 36.94% of gangliogliomas (528 of 1360 cases in a systematic review of 43 studies) (pereira2026molecularfeaturesin pages 1-2, pereira2026molecularfeaturesin pages 2-4). This glutamic acid-to-valine substitution causes constitutive activation of the serine/threonine kinase domain, promoting oncogenic transformation (pereira2026molecularfeaturesin pages 4-5).
- **FGFR1:** FGFR1 hotspot mutations (N546K and K656E) are the fifth most prevalent alteration in LGG/MNGT; among driver-unknown samples, up to 12% harbor these mutations (engelhardt2022frequentfgfr1hotspot pages 1-2). FGFR1 alterations are present in >75% of DNETs (crainic2023rareneuronalglial pages 6-8).
- **NF1/PTPN11/KRAS:** A subgroup of gangliogliomas with PTPN11/KRAS/NF1 alterations has been identified, showing adverse clinical outcomes and atypical histopathological features, with only 38% achieving Engel I seizure outcome compared to 85% for BRAF V600E-only gangliogliomas (pereira2026molecularfeaturesin pages 8-9).
- **Neurofibromatosis type 1 (NF1):** Germline NF1 mutations predispose to various glioneuronal tumors.

### Environmental and Lifestyle Risk Factors
No specific environmental or lifestyle risk factors have been consistently identified for mixed neuronal-glial tumors. These tumors are not associated with known carcinogen exposures, ionizing radiation, or infectious agents based on current evidence. The primary etiologic mechanism appears to be somatic genetic alteration during neural development.

### Gene-Environment Interactions
No well-established gene-environment interactions have been documented for this tumor group. The predominantly somatic, developmental nature of the underlying genetic alterations suggests limited environmental modulation.

---

## 3. Phenotypes

### Primary Phenotypes

**Seizures / Epilepsy (HP:0001250)**
- **Type:** Symptom (neurological)
- **Characteristics:** Drug-resistant focal epilepsy is the hallmark presentation; seizures are present in the vast majority of cases, often with onset at a young age and a long-term history (crainic2023rareneuronalglial pages 1-2, vaz2022uncommonglioneuronaltumors pages 1-4). Ganglioglioma and DNET have been informally termed "epileptomas" due to their extremely high epileptogenic potential (crainic2023rareneuronalglial pages 1-2).
- **Onset:** Childhood to young adulthood
- **Severity:** Often medically refractory (drug-resistant)
- **Frequency:** >80% of gangliogliomas and DNETs

**Headache (HP:0002315)**
- **Type:** Symptom
- **Characteristics:** Less common than seizures; may present in tumors causing mass effect or hydrocephalus
- **Frequency:** Variable, more common in posterior fossa tumors (RGNT) and central neurocytoma

**Focal neurological deficits (HP:0007340)**
- **Type:** Clinical sign
- **Characteristics:** Depend on tumor location; may include motor weakness, sensory changes, visual field deficits
- **Onset:** Variable; more common in aggressive subtypes (anaplastic ganglioglioma)

**Hydrocephalus (HP:0000238)**
- **Type:** Clinical sign
- **Characteristics:** Seen particularly with intraventricular tumors (central neurocytoma) and leptomeningeal spread (DLGNT)

**Macrocephaly (HP:0000256)**
- **Type:** Physical manifestation
- **Characteristics:** Particularly relevant to desmoplastic infantile ganglioglioma presenting in infancy

**Quality of Life Impact:** Chronic epilepsy significantly impairs quality of life, including cognitive development in children, educational achievement, employment, driving ability, and psychosocial functioning. Successful surgical resection with seizure freedom provides the greatest quality-of-life benefit.

---

## 4. Genetic/Molecular Information

### Causal Genes and Pathogenic Variants
OpenTargets disease-target association analysis identified 8 key targets for mixed neuronal-glial tumor (MONDO:0016729), with PTEN (score 0.66), BRAF (score 0.63), FGFR1 (score 0.48), H3-3A (score 0.42), NTRK3 (score 0.38), IDH1 (score 0.37), ETV6 (score 0.37), and MUTYH (score 0.34) as the top associations (OpenTargets Search: mixed neuronal-glial tumor,ganglioglioma,glioneuronal tumor).

**BRAF (HGNC:1097; ENSG00000157764):**
- V600E missense mutation: most frequent alteration in gangliogliomas at 36.32–36.94% (pereira2026molecularfeaturesin pages 1-2, pereira2026molecularfeaturesin pages 2-4)
- Additional variants: duplications, in-frame insertions, and fusions including KIAA1549::BRAF (pereira2026molecularfeaturesin pages 2-4)
- Somatic origin; constitutive activation of MAPK/ERK pathway
- ClinVar: RCV000515781 for BRAF-mixed neuronal-glial tumor association

**FGFR1 (HGNC:3688; ENSG00000077782):**
- Hotspot mutations N546K and K656E; present in 1.18% of gangliogliomas but dominant in DNETs (>75%) (engelhardt2022frequentfgfr1hotspot pages 1-2, pereira2026molecularfeaturesin pages 1-2, crainic2023rareneuronalglial pages 6-8)
- FGFR activation phosphorylates kinase domains to activate Ras/Raf/MEK and PI3K-Akt pathways (engelhardt2022frequentfgfr1hotspot pages 1-2)

**FGFR1::TACC1 fusion:** Reported in approximately two-thirds of extraventricular neurocytomas (crainic2023rareneuronalglial pages 4-5)

**SLC44A1::PRKCA fusion:** Characteristic of papillary glioneuronal tumor (crainic2023rareneuronalglial pages 4-5, crainic2023rareneuronalglial pages 5-6, vaz2022uncommonglioneuronaltumors pages 4-6)

**PDGFRA p.K385 mutation:** Defining alteration for myxoid glioneuronal tumor (capper2023eanoguidelineon pages 11-12, bale2022the2021who pages 8-9)

### Epigenetic Information
DNA methylation profiling has emerged as a critical diagnostic tool for classifying glioneuronal tumors. The DKFZ/Heidelberg CNS tumor classifier uses machine learning-based methylation analysis to distinguish tumor subtypes, and methylation classification confirmed or refined morphological diagnoses in a significant proportion of cases (singh2023currentstatusof pages 3-4). DLGNT shows two molecular subclasses (MC-1 and MC-2) based on distinct methylation profiles with different age presentations and survival outcomes (singh2023currentstatusof pages 3-4). DGONC is defined by a distinct methylation class associated with monosomy 14 (bale2022the2021who pages 1-2, xie2023lowgradeepilepsyassociatedneuroepithelial pages 2-3, bale2022the2021who pages 8-9).

### Chromosomal Abnormalities
- **1p deletion:** Characteristic of DLGNT
- **Monosomy 14:** Defining feature of DGONC (bale2022the2021who pages 1-2, bale2022the2021who pages 8-9)
- **Chromosome 12 gains, NF1 CNV losses:** Identified in PTPN11-altered gangliogliomas (pereira2026molecularfeaturesin pages 8-9)

---

## 5. Environmental Information

No specific environmental toxins, radiation exposures, or lifestyle factors have been established as causative or contributory for mixed neuronal-glial tumors based on current evidence. No infectious agents have been implicated in the pathogenesis of these tumors.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways
The central pathogenic mechanism involves constitutive activation of the **RAS–RAF–MEK–ERK (MAPK)** signaling cascade (kobow2021moleculardiagnosticsin pages 2-4, pereira2026molecularfeaturesin pages 4-5). BRAF V600E mutations cause constitutive kinase activation, leading to uncontrolled cell proliferation and oncogenic transformation. BRAF inhibitors work by selectively binding to V600E-mutated B-Raf proteins and preventing MEK activation (pereira2026molecularfeaturesin pages 4-5).

The **PI3K–AKT–mTOR** pathway also plays a role, particularly through co-mutations in PIK3CA and PIK3R1 observed in rosette-forming glioneuronal tumors (crainic2023rareneuronalglial pages 4-5). FGFR1 activation simultaneously stimulates both Ras/Raf/MEK and PI3K-Akt cascades (engelhardt2022frequentfgfr1hotspot pages 1-2).

**Relevant GO terms:**
- GO:0000165 (MAPK cascade)
- GO:0043066 (negative regulation of apoptotic process)
- GO:0008284 (positive regulation of cell population proliferation)
- GO:0048015 (phosphatidylinositol-mediated signaling)

### Cellular Processes
- Cell proliferation driven by constitutive MAPK activation
- Aberrant neural progenitor differentiation during development
- Epileptogenesis through cortical involvement and association with focal cortical dysplasia (FCD) (kobow2021moleculardiagnosticsin pages 2-4)

**Relevant CL terms:**
- CL:0000540 (neuron)
- CL:0000127 (astrocyte)
- CL:0000128 (oligodendrocyte)
- CL:0002319 (neural cell)

### Causal Chain
Somatic mutation (e.g., BRAF V600E) in neural progenitor during embryonic development → constitutive MAPK/ERK pathway activation → aberrant cell proliferation and differentiation → formation of mixed neuronal-glial neoplasm in cortex → cortical disruption and epileptogenic zone formation → drug-resistant focal epilepsy (kobow2021moleculardiagnosticsin pages 2-4).

---

## 7. Anatomical Structures Affected

### Primary Organs
- **Brain (UBERON:0000955):** Primary site of involvement
- **Cerebral cortex (UBERON:0000956):** Most common location, especially temporal lobe
- **Temporal lobe (UBERON:0001871):** Predilection site for ganglioglioma and DNET (vaz2022uncommonglioneuronaltumors pages 1-4)
- **Fourth ventricle / Posterior fossa:** Common site for RGNT (crainic2023rareneuronalglial pages 4-5)
- **Septum pellucidum / Lateral ventricle:** Characteristic for myxoid glioneuronal tumor (bale2022the2021who pages 8-9)
- **Leptomeninges (UBERON:0000016):** Involved in DLGNT
- **Spinal cord (UBERON:0002240):** Can be involved in DLGNT and rare glioneuronal tumors

### Tissue and Cell Level
- **Neuronal cells:** Dysmorphic ganglion cells (ganglioglioma), floating neurons (DNET), neurocytic rosettes (RGNT)
- **Glial cells:** Astrocytic (GFAP+) and oligodendroglial (OLIG2+) components
- **Progenitor cells:** CD34+ ramified cells characteristically present (vaz2022uncommonglioneuronaltumors pages 1-4)

---

## 8. Temporal Development

### Onset
- **Typical age:** Predominantly childhood to young adulthood (crainic2023rareneuronalglial pages 1-2, vaz2022uncommonglioneuronaltumors pages 1-4)
- **Desmoplastic infantile ganglioglioma:** Presents in infancy, usually first 2 years of life
- **Onset pattern:** Typically insidious, with chronic seizures developing over months to years before diagnosis

### Progression
- **Most subtypes (WHO grade 1):** Slow-growing, indolent biological behavior with long-term seizure history (crainic2023rareneuronalglial pages 1-2)
- **Anaplastic ganglioglioma (WHO grade 3):** More aggressive course with potential for rapid progression (crainic2023rareneuronalglial pages 6-8, vaz2022uncommonglioneuronaltumors pages 1-4)
- **Disease course:** Generally stable or slowly progressive; recurrence possible, particularly with subtotal resection

---

## 9. Inheritance and Population

### Epidemiology
According to the CBTRUS Statistical Report (2014–2018), neuronal and mixed neuronal-glial tumors had an annual average of 58 cases and 5-year total of 290 cases in the United States, with an age-adjusted incidence rate (AAAIR) of 0.05 per 100,000 population (95% CI: 0.04–0.06) (ostrom2021cbtrusstatisticalreport pages 50-51). These tumors represent less than 2% of all primary CNS tumors (crainic2023rareneuronalglial pages 1-2).

### Population Demographics
- **Age distribution:** Predominantly affects children, adolescents, and young adults
- **Sex ratio:** Most subtypes show no strong sex predilection, though some series report slight male predominance
- **Geographic distribution:** No documented geographic clustering; reported worldwide
- **Inheritance:** Almost exclusively somatic (non-hereditary) mutations. No Mendelian inheritance pattern. Rare association with NF1 (autosomal dominant predisposition syndrome).

---

## 10. Diagnostics

### Clinical Tests

**Imaging (MAXO:0000387 - imaging study):**
- MRI is the cornerstone of neuroimaging. Gangliogliomas typically appear as cortical/subcortical cystic-solid lesions with enhancement. DNETs often show cortical "bubbly" T2-hyperintense lesions without mass effect. Genotype-neuroimaging correlations have been identified: BRAF V600E tumors show indistinct borders with iso-T1/high-T2 signal (93.8% sensitivity, 100% specificity), while FGFR1-mutant tumors show sharp borders with very high T2 signal and diffuse mass effect (100% sensitivity and specificity) (iijima2024genotyperelevantneuroimagingfeatures pages 9-9).

**Histopathology and Immunohistochemistry:**
- Ganglioglioma: Synaptophysin+/Chromogranin A+ neuronal cells, GFAP+/OLIG2+ glial cells, eosinophilic granular bodies, CD34+ stellate cells, Ki67 <3% (crainic2023rareneuronalglial pages 6-8, vaz2022uncommonglioneuronaltumors pages 1-4)
- DNET: "Floating neurons" in myxoid matrix, NeuN+/synaptophysin+ neurons, Olig2+ oligodendroglia-like cells (crainic2023rareneuronalglial pages 6-8)
- RGNT: Synaptophysin+/MAP2+/NSE+ neurocytic rosettes, GFAP+/OLIG2+/S100+ glial component (vaz2022uncommonglioneuronaltumors pages 6-7)

**Molecular/Genetic Testing:**
The EANO guideline recommends next-generation sequencing (NGS) panel diagnostics rather than sequential target-specific testing, given the low prevalence (<5%) of individual targets in CNS tumors (capper2023eanoguidelineon pages 3-4). DNA methylation profiling using the DKFZ/Heidelberg classifier is increasingly essential for accurate subtyping (singh2023currentstatusof pages 3-4). The 2023 EANO molecular diagnostic tools guideline systematically reviews methods including NGS for DNA and RNA, methylome profiling, and immunohistochemistry for marker assessment (capper2023eanoguidelineon pages 3-4).

### Differential Diagnosis
Key differential diagnoses include: pilocytic astrocytoma, oligodendroglioma (IDH-mutant, 1p/19q-codeleted), pleomorphic xanthoastrocytoma, angiocentric glioma, focal cortical dysplasia, and diffuse low-grade glioma (vaz2022uncommonglioneuronaltumors pages 4-6, bale2022the2021who pages 3-5).

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Ganglioglioma (WHO grade 1):** 10-year survival exceeds 80% with complete surgical resection (crainic2023rareneuronalglial pages 6-8). Gross total resection (GTR) improves both overall survival and seizure control compared to subtotal resection (STR) (crainic2023rareneuronalglial pages 6-8).
- **Ganglioglioma with PTPN11/KRAS/NF1 alterations:** Significantly worse seizure outcomes (38% Engel I) compared to BRAF V600E-only gangliogliomas (85% Engel I), suggesting a clinically relevant adverse subgroup (pereira2026molecularfeaturesin pages 8-9).
- **DLGNT:** Prognosis varies by methylation subclass; MC-1 and MC-2 have different survival outcomes (singh2023currentstatusof pages 3-4).
- **Anaplastic ganglioglioma (WHO grade 3):** More aggressive clinical course with shorter survival.

### Prognostic Factors
- Extent of surgical resection (GTR vs. STR)
- Tumor location (temporal lobe more favorable than infratentorial) (crainic2023rareneuronalglial pages 6-8)
- Molecular subgroup (BRAF V600E-only more favorable; PTPN11/KRAS/NF1 subgroup worse) (pereira2026molecularfeaturesin pages 8-9)
- Ki67/MIB1 proliferation index (>2% associated with recurrence risk) (vaz2022uncommonglioneuronaltumors pages 9-10)
- WHO grade (grade 1 vs. grade 3)
- CDKN2A/B deletion status

---

## 12. Treatment

### Surgical Management (MAXO:0000004 - surgical procedure)
Gross total resection is the cornerstone of treatment and is considered curative for most WHO grade 1 glioneuronal tumors (crainic2023rareneuronalglial pages 1-2, crainic2023rareneuronalglial pages 6-8). For epilepsy-associated tumors, extended resection including the epileptogenic zone improves seizure-free outcomes (crainic2023rareneuronalglial pages 6-8). Temporal lobe surgeries generally achieve better seizure control than extratemporal resections.

### Targeted Therapies (MAXO:0001525 - targeted therapy)
The following table summarizes the molecular targets and therapeutic options:

| Target/Gene | Alteration Type | Frequency in tumor subtype | Associated tumor subtype(s) | Targeted therapy options | ESCAT classification / guideline status | Clinical trial evidence (NCT) |
|---|---|---|---|---|---|---|
| **BRAF** | **p.V600E missense hotspot** | Ganglioglioma ~36.3–36.9%; DNET **<1/3** of cases; PLNTY subset; broader mixed neuronal-glial tumor association in OpenTargets (pereira2026molecularfeaturesin pages 1-2, pereira2026molecularfeaturesin pages 2-4, crainic2023rareneuronalglial pages 6-8, bale2022the2021who pages 8-9, OpenTargets Search: mixed neuronal-glial tumor,ganglioglioma,glioneuronal tumor) | Ganglioglioma, anaplastic ganglioglioma, DNET, PLNTY, other LEAT/glioneuronal tumors | **Dabrafenib + trametinib**; **vemurafenib**; other BRAF inhibitors; BRAF/MEK combination preferred for progressive/recurrent disease after standard care (crainic2023rareneuronalglial pages 18-19, pereira2026molecularfeaturesin pages 4-5, capper2023eanoguidelineon pages 2-3, capper2023eanoguidelineon pages 9-10) | **Standard-of-care target in recurrent CNS tumors/glioneuronal tumors per EANO**; highest actionability among reviewed targets (capper2023eanoguidelineon pages 2-3, bent2025updatedeanoguideline pages 1-2, capper2023eanoguidelineon pages 9-10) | **NCT02684058** (dabrafenib + trametinib, pediatric BRAF V600 tumors); pediatric long-term follow-up **NCT03975829** |
| **BRAF** | **KIAA1549::BRAF fusion / other BRAF fusions** | Common in some low-grade glioma/glioneuronal contexts; reported in DLGNT and pilocytic-spectrum tumors; not a dominant alteration in classic ganglioglioma (engelhardt2022frequentfgfr1hotspot pages 1-2, vaz2022uncommonglioneuronaltumors pages 6-7, bent2025updatedeanoguideline pages 3-4) | Diffuse leptomeningeal glioneuronal tumor (DLGNT), pilocytic-spectrum tumors, some mixed neuronal-glial tumors | **MEK inhibitors** or **type II RAF inhibitors** considered, preferably in trials for recurrent disease (capper2023eanoguidelineon pages 9-10) | Therapeutically relevant in selected entities including **DLGNT**; EANO update notes growing relevance of fusion testing (bent2025updatedeanoguideline pages 3-4) | No subtype-specific dedicated trial identified here; may be captured in basket/brain tumor molecular trials |
| **FGFR1** | **Hotspot mutation (N546K, K656E), mutation/duplication/fusion spectrum** | **>75% in DNET** overall FGFR1-altered spectrum; only ~1.18% in ganglioglioma; in driver-unknown LGG/MNGT, FGFR1 N546/K656 mutations in **12%** (13/108) (crainic2023rareneuronalglial pages 6-8, engelhardt2022frequentfgfr1hotspot pages 1-2, pereira2026molecularfeaturesin pages 1-2) | DNET, RGNT, some mixed neuronal-glial tumors, pilocytic-spectrum tumors | **FGFR inhibitors** (investigational; modest activity so far); molecular testing recommended when targeted options sought (capper2023eanoguidelineon pages 2-3, capper2023eanoguidelineon pages 11-12) | **ESCAT IIB** for FGFR alterations in glioneuronal tumors such as **RGNT/DNET** per EANO (capper2023eanoguidelineon pages 11-12) | **NCT05267106** (pemigatinib in FGFR1-3 altered primary CNS tumors; terminated) |
| **NTRK1/2/3** | **Gene fusions** | Rare; OpenTargets supports NTRK3 association with mixed neuronal-glial tumor/ganglioglioma (OpenTargets Search: mixed neuronal-glial tumor,ganglioglioma,glioneuronal tumor) | Rare glioneuronal tumors, mixed neuronal-glial tumors, ganglioglioma subset | **Larotrectinib**, **entrectinib** for fusion-positive recurrent disease, ideally in trials/registries (capper2023eanoguidelineon pages 2-3, capper2023eanoguidelineon pages 6-7, capper2023eanoguidelineon pages 11-12) | **ESCAT IIB**; EANO recommends testing in patients who exhausted standard therapy and are fit for targeted treatment (capper2023eanoguidelineon pages 2-3, capper2023eanoguidelineon pages 3-4, capper2023eanoguidelineon pages 11-12) | No mixed neuronal-glial subtype-specific NCT identified here; typically basket trial enrollment |
| **PRKCA** | **Fusion (especially SLC44A1::PRKCA)** | Characteristic / recurrent driver rather than population-frequency estimate provided (crainic2023rareneuronalglial pages 4-5, crainic2023rareneuronalglial pages 5-6, vaz2022uncommonglioneuronaltumors pages 4-6) | Papillary glioneuronal tumor (PGNT) | No established approved matched therapy in current EANO guidance; primarily **diagnostic biomarker** | Not assigned as an actionable standard target in cited EANO therapeutic recommendations; clinical benefit not established (capper2023eanoguidelineon pages 2-3) | No specific trial identified here |
| **PDGFRA** | **p.K385 mutation** | Defining recurrent alteration for myxoid glioneuronal tumor (MGT) (capper2023eanoguidelineon pages 11-12, xie2023lowgradeepilepsyassociatedneuroepithelial pages 2-3, bale2022the2021who pages 8-9) | Myxoid glioneuronal tumor | Currently mainly **diagnostic**; no standard targeted therapy established in cited guidance | Used as a **diagnostic marker** in EANO/WHO-era classification rather than validated therapeutic target (capper2023eanoguidelineon pages 11-12, bale2022the2021who pages 8-9) | No specific trial identified here |
| **H3-3A (H3F3A)** | **Histone H3 alterations (e.g., H3 K27M in rare cases)** | Rare in ganglioglioma (~0.74% in one systematic review context); OpenTargets association present (pereira2026molecularfeaturesin pages 2-4, OpenTargets Search: mixed neuronal-glial tumor,ganglioglioma,glioneuronal tumor) | Rare ganglioglioma/anaplastic ganglioglioma and mixed neuronal-glial tumors | No established targeted therapy in current glioneuronal standard care; investigational approaches only | Not a proven predictive target for routine targeted treatment in current EANO update (bent2025updatedeanoguideline pages 1-2) | No specific trial identified here |
| **PTEN** | **Loss / pathway alteration** | OpenTargets association present but no direct evidence count in cited dataset; may contribute to BRAFi resistance biology (OpenTargets Search: mixed neuronal-glial tumor,ganglioglioma,glioneuronal tumor, pereira2026molecularfeaturesin pages 4-5) | Mixed neuronal-glial tumor, resistant BRAF-mutant glioneuronal tumors | No established matched therapy in this disease context; relevant to resistance and PI3K/AKT/mTOR biology | Not validated as routine actionable target in current EANO guidance for glioneuronal tumors (bent2025updatedeanoguideline pages 1-2) | No specific trial identified here |
| **NF1 / KRAS / PTPN11 / other RAS-MAPK genes** | **Somatic mutation / CNV gain / pathway activation** | Defined adverse-outcome subgroup in ganglioglioma; exact subgroup small (8 PTPN11-altered GG in one series) (kobow2021moleculardiagnosticsin pages 2-4, pereira2026molecularfeaturesin pages 8-9, engelhardt2022frequentfgfr1hotspot pages 1-2) | Ganglioglioma with atypical histology/adverse seizure outcome; RGNT may carry NF1 co-alterations | No established approved subtype-specific therapy; **MAPK-pathway inhibitors** considered biologically relevant/investigational (pereira2026molecularfeaturesin pages 8-9, crainic2023rareneuronalglial pages 6-8) | Not established as standard actionable targets; testing may be considered when trials/advanced molecular profiling are pursued (capper2023eanoguidelineon pages 2-3, capper2023eanoguidelineon pages 9-10) | **NCT04923126** (mirdametinib in low-grade glioma; includes MAPK-pathway disease context) |
| **PIK3CA / PIK3R1** | **Co-mutations / PI3K pathway activation** | Reported as co-alterations in RGNT and some glioneuronal tumors; no robust prevalence estimate here (crainic2023rareneuronalglial pages 4-5, vaz2022uncommonglioneuronaltumors pages 6-7) | Rosette-forming glioneuronal tumor, some mixed neuronal-glial tumors | No established approved targeted therapy in this indication; pathway relevance mainly mechanistic | Not established as routine actionable target in current EANO recommendations for glioneuronal tumors (capper2023eanoguidelineon pages 2-3, bent2025updatedeanoguideline pages 1-2) | No specific trial identified here |
| **ETV6** | **Fusion partner in NTRK3-related events / association in OpenTargets** | Rare; OpenTargets association only in current evidence set (OpenTargets Search: mixed neuronal-glial tumor,ganglioglioma,glioneuronal tumor) | Rare mixed neuronal-glial tumors / ganglioglioma-related fusion-positive cases | If part of **ETV6::NTRK3**, therapy would follow **NTRK inhibitor** pathway (larotrectinib/entrectinib) | Follows **NTRK fusion** actionability rather than ETV6 alone (capper2023eanoguidelineon pages 2-3, capper2023eanoguidelineon pages 11-12) | Basket trial/registry approach; no specific subtype trial identified here |
| **IDH1** | **Mutation** | Rare / generally not characteristic; OpenTargets association exists but classic glioneuronal tumors are usually IDH-wildtype (OpenTargets Search: mixed neuronal-glial tumor,ganglioglioma,glioneuronal tumor, pereira2026molecularfeaturesin pages 2-4, crainic2023rareneuronalglial pages 6-8) | Rare atypical ganglioglioma or misclassified tumors | No established role in routine therapy for classic mixed neuronal-glial tumors | More relevant to differential diagnosis than to standard targeted treatment in this entity group (bent2025updatedeanoguideline pages 1-2) | No specific trial identified here |
| **MUTYH** | **Association only in OpenTargets** | No supporting evidence count in cited OpenTargets dataset (OpenTargets Search: mixed neuronal-glial tumor,ganglioglioma,glioneuronal tumor) | Mixed neuronal-glial tumor | None established | No therapeutic actionability established | None identified |


*Table: This table summarizes the main molecular alterations linked to mixed neuronal-glial tumors and maps them to current or emerging targeted treatment options. It emphasizes where evidence is strongest—especially for BRAF V600E—and where alterations are primarily diagnostic rather than therapeutically validated.*

**BRAF V600E-targeted therapy:** The EANO guideline (2023) recommends that BRAF p.V600E targeted treatment should be considered part of the standard of care for patients with recurrent gliomas, pending regulatory approval (capper2023eanoguidelineon pages 2-3). FDA-approved BRAF inhibitors include vemurafenib (Zelboraf), dabrafenib (Tafinlar), and encorafenib (Braftovi) (pereira2026molecularfeaturesin pages 4-5). Combination BRAF/MEK inhibitor therapy (e.g., dabrafenib + trametinib) is preferred as it can overcome resistance to single-agent BRAF inhibitors and has been shown to produce durable responses (crainic2023rareneuronalglial pages 18-19, capper2023eanoguidelineon pages 9-10). In a multi-institutional study of BRAF-mutant pediatric high-grade gliomas (including anaplastic gangliogliomas) treated with upfront molecular targeted therapy, 3-year progression-free and overall survival were 65% and 82%, respectively, superior to historical controls (rosenberg2022upfrontmoleculartargeted pages 5-6).

**NTRK inhibitors:** Larotrectinib and entrectinib have received conditional tumor-agnostic approval for NTRK fusion-positive tumors (capper2023eanoguidelineon pages 6-7). However, evidence of clinical benefit specifically in adult CNS tumors remains limited, and treatment should preferably occur within clinical trials (capper2023eanoguidelineon pages 2-3, capper2023eanoguidelineon pages 11-12).

**FGFR inhibitors:** Clinical trials have evaluated FGFR inhibitors (e.g., pemigatinib, NCT05267106) for FGFR-altered CNS tumors, though activity has been modest (capper2023eanoguidelineon pages 2-3, capper2023eanoguidelineon pages 11-12). FGFR alterations are classified as ESCAT IIB in glioneuronal tumors (capper2023eanoguidelineon pages 11-12).

### Radiotherapy (MAXO:0000015 - radiation therapy)
Radiotherapy is reserved for subtotal resection of aggressive tumors, tumors in eloquent brain areas, or recurrent disease (crainic2023rareneuronalglial pages 6-8, talloa2022brafandmek pages 10-11). Focal radiation therapy should be used cautiously in young children due to long-term cognitive side effects (talloa2022brafandmek pages 10-11).

### Chemotherapy
Temozolomide has limited evidence for improving survival but may be considered for anaplastic features or inoperable recurrent tumors (crainic2023rareneuronalglial pages 6-8). For DLGNT, bevacizumab has been used successfully in some cases (crainic2023rareneuronalglial pages 18-19).

### Clinical Trials
- **NCT02684058:** Dabrafenib + trametinib in pediatric BRAF V600 mutation-positive LGG/relapsed HGG (Phase 2, completed, 151 participants)
- **NCT04923126:** Mirdametinib (MEK inhibitor) in children/adolescents/young adults with low-grade glioma (Phase 1/2, recruiting, 132 participants)
- **NCT05267106:** Pemigatinib (FGFR inhibitor) in FGFR1-3 altered primary CNS tumors (Phase 2, terminated, 83 participants)
- **NCT05259605:** EORTC observational study assessing treatment and outcome using WHO 2021 classification (recruiting, 1650 participants)

---

## 13. Prevention

### Primary Prevention
No established primary prevention strategies exist for mixed neuronal-glial tumors. As these tumors arise from somatic mutations during neural development, there are no modifiable risk factors or vaccination strategies available.

### Secondary Prevention (Early Detection)
- Early neuroimaging (MRI) evaluation in children presenting with new-onset seizures
- Genetic counseling for families with NF1 or other cancer predisposition syndromes
- Epilepsy monitoring and evaluation for surgical candidacy in drug-resistant cases

### Tertiary Prevention
- Post-surgical surveillance imaging to monitor for recurrence
- Long-term epilepsy follow-up and anti-seizure medication management
- Neurocognitive monitoring and rehabilitation, particularly in pediatric patients

---

## 14. Other Species / Natural Disease

Limited data exist on naturally occurring mixed neuronal-glial tumors in other species. Ganglioglioma-like tumors have been rarely reported in veterinary neuropathology in domestic animals. BRAF V600E-equivalent mutations and MAPK pathway alterations have been identified in canine tumors, supporting evolutionary conservation of oncogenic mechanisms. However, no systematic comparative pathology data specific to glioneuronal tumors are available in the current literature.

---

## 15. Model Organisms

### Genetic Models
Experimental models have demonstrated that expression of BRAF V600E in neural progenitors during embryonic development reproduces ganglioglioma histopathological features and leads to epileptic seizures (kobow2021moleculardiagnosticsin pages 2-4). These models have been crucial for understanding the developmental origin of these tumors and the mechanism of epileptogenicity.

- **Mouse models:** Conditional BRAF V600E expression in neural progenitors (genetically engineered mouse models)
- **Cell lines:** Patient-derived primary tumor cultures have been used for drug sensitivity studies

### Model Limitations
- Difficulty recapitulating the mixed neuronal-glial phenotype in full
- Limited availability of immortalized cell lines due to the low-grade, slow-growing nature of most subtypes
- Differences between murine and human neural development may affect translational relevance

---

## Summary

Mixed neuronal-glial tumors are a diverse group of rare, predominantly low-grade CNS neoplasms characterized by dual neuronal-glial composition, strong association with epilepsy, and frequent MAPK pathway alterations. The WHO 2021 classification substantially expanded and refined this tumor family through integration of molecular markers and DNA methylation profiling. BRAF V600E is the most actionable therapeutic target, with dabrafenib/trametinib combination therapy approaching standard-of-care status for recurrent disease per EANO guidelines. Gross total surgical resection remains the primary curative modality, with excellent long-term survival exceeding 80% for WHO grade 1 subtypes. Ongoing molecular characterization continues to identify new tumor entities and refine prognostic stratification within this heterogeneous tumor group.

References

1. (crainic2023rareneuronalglial pages 1-2): Nicolas Crainic, Julia Furtner, Johan Pallud, Franck Bielle, Giuseppe Lombardi, Roberta Rudà, and Ahmed Idbaih. Rare neuronal, glial and glioneuronal tumours in adults. Cancers, 15:1120, Feb 2023. URL: https://doi.org/10.3390/cancers15041120, doi:10.3390/cancers15041120. This article has 7 citations.

2. (vaz2022uncommonglioneuronaltumors pages 1-4): A. Vaz, M.S. Cavalcanti, E.B. da Silva Junior, R. Ramina, and B.C. de Almeida Teixeira. Uncommon glioneuronal tumors: a radiologic and pathologic synopsis. American Journal of Neuroradiology, 43:1080-1089, May 2022. URL: https://doi.org/10.3174/ajnr.a7465, doi:10.3174/ajnr.a7465. This article has 25 citations and is from a peer-reviewed journal.

3. (bale2022the2021who pages 1-2): Tejus A. Bale and Marc K. Rosenblum. The 2021 who classification of tumors of the central nervous system: an update on pediatric low‐grade gliomas and glioneuronal tumors. Brain Pathology, Feb 2022. URL: https://doi.org/10.1111/bpa.13060, doi:10.1111/bpa.13060. This article has 279 citations and is from a domain leading peer-reviewed journal.

4. (bale2022the2021who pages 2-3): Tejus A. Bale and Marc K. Rosenblum. The 2021 who classification of tumors of the central nervous system: an update on pediatric low‐grade gliomas and glioneuronal tumors. Brain Pathology, Feb 2022. URL: https://doi.org/10.1111/bpa.13060, doi:10.1111/bpa.13060. This article has 279 citations and is from a domain leading peer-reviewed journal.

5. (OpenTargets Search: mixed neuronal-glial tumor,ganglioglioma,glioneuronal tumor): Open Targets Query (mixed neuronal-glial tumor,ganglioglioma,glioneuronal tumor, 20 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (pereira2026molecularfeaturesin pages 1-2): Benedito Jamilson Araújo Pereira, Sueli Mieko Oba-Shinjo, Ivy Karoline Herculano de Azevedo, Yuri Reis Casal, Wen Hung Tzu, Antônio Nogueira de Almeida, Wellingson Silva Paiva, and Suely Kazue Nagahashi Marie. Molecular features in gangliogliomas: a systematic review. Child's Nervous System, Feb 2026. URL: https://doi.org/10.1007/s00381-026-07170-7, doi:10.1007/s00381-026-07170-7. This article has 1 citations.

7. (pereira2026molecularfeaturesin pages 2-4): Benedito Jamilson Araújo Pereira, Sueli Mieko Oba-Shinjo, Ivy Karoline Herculano de Azevedo, Yuri Reis Casal, Wen Hung Tzu, Antônio Nogueira de Almeida, Wellingson Silva Paiva, and Suely Kazue Nagahashi Marie. Molecular features in gangliogliomas: a systematic review. Child's Nervous System, Feb 2026. URL: https://doi.org/10.1007/s00381-026-07170-7, doi:10.1007/s00381-026-07170-7. This article has 1 citations.

8. (crainic2023rareneuronalglial pages 6-8): Nicolas Crainic, Julia Furtner, Johan Pallud, Franck Bielle, Giuseppe Lombardi, Roberta Rudà, and Ahmed Idbaih. Rare neuronal, glial and glioneuronal tumours in adults. Cancers, 15:1120, Feb 2023. URL: https://doi.org/10.3390/cancers15041120, doi:10.3390/cancers15041120. This article has 7 citations.

9. (kobow2021moleculardiagnosticsin pages 2-4): Katja Kobow, Stéphanie Baulac, Andreas von Deimling, and Jeong Ho Lee. Molecular diagnostics in drug‐resistant focal epilepsy define new disease entities. Brain Pathology, Jul 2021. URL: https://doi.org/10.1111/bpa.12963, doi:10.1111/bpa.12963. This article has 25 citations and is from a domain leading peer-reviewed journal.

10. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 2-3): Mingguo Xie, Xiongfei Wang, Zejun Duan, and Guoming Luan. Low-grade epilepsy-associated neuroepithelial tumors: tumor spectrum and diagnosis based on genetic alterations. Frontiers in Neuroscience, Jan 2023. URL: https://doi.org/10.3389/fnins.2022.1071314, doi:10.3389/fnins.2022.1071314. This article has 30 citations and is from a peer-reviewed journal.

11. (crainic2023rareneuronalglial pages 4-5): Nicolas Crainic, Julia Furtner, Johan Pallud, Franck Bielle, Giuseppe Lombardi, Roberta Rudà, and Ahmed Idbaih. Rare neuronal, glial and glioneuronal tumours in adults. Cancers, 15:1120, Feb 2023. URL: https://doi.org/10.3390/cancers15041120, doi:10.3390/cancers15041120. This article has 7 citations.

12. (vaz2022uncommonglioneuronaltumors pages 4-6): A. Vaz, M.S. Cavalcanti, E.B. da Silva Junior, R. Ramina, and B.C. de Almeida Teixeira. Uncommon glioneuronal tumors: a radiologic and pathologic synopsis. American Journal of Neuroradiology, 43:1080-1089, May 2022. URL: https://doi.org/10.3174/ajnr.a7465, doi:10.3174/ajnr.a7465. This article has 25 citations and is from a peer-reviewed journal.

13. (vaz2022uncommonglioneuronaltumors pages 6-7): A. Vaz, M.S. Cavalcanti, E.B. da Silva Junior, R. Ramina, and B.C. de Almeida Teixeira. Uncommon glioneuronal tumors: a radiologic and pathologic synopsis. American Journal of Neuroradiology, 43:1080-1089, May 2022. URL: https://doi.org/10.3174/ajnr.a7465, doi:10.3174/ajnr.a7465. This article has 25 citations and is from a peer-reviewed journal.

14. (singh2023currentstatusof pages 3-4): Jyotsna Singh, Saumya Sahu, Trishala Mohan, Swati Mahajan, Mehar C Sharma, Chitra Sarkar, and Vaishali Suri. Current status of dna methylation profiling in neuro-oncology as a diagnostic support tool: a review. Neuro-oncology practice, 10 6:518-526, Jul 2023. URL: https://doi.org/10.1093/nop/npad040, doi:10.1093/nop/npad040. This article has 11 citations and is from a peer-reviewed journal.

15. (bent2025updatedeanoguideline pages 3-4): Martin J van den Bent, Enrico Franceschi, Mehdi Touat, Pim J French, Ahmed Idbaih, Giuseppe Lombardi, Roberta Rudà, Leonille Schweizer, David Capper, Marc Sanson, Pieter Wesseling, Michael Weller, Marica Eoli, Elena Anghileri, Franck Bielle, Phillipp Euskirchen, Marjolein Geurts, Patrick Y Wen, and Matthias Preusser. Updated eano guideline on rational molecular testing of gliomas, glioneuronal, and neuronal tumors in adults for targeted therapy selection—update 1. Neuro-Oncology, 27:331-337, Oct 2025. URL: https://doi.org/10.1093/neuonc/noae213, doi:10.1093/neuonc/noae213. This article has 27 citations and is from a domain leading peer-reviewed journal.

16. (rio2024newcnstumor pages 2-4): Ramiro José del Río, Santiago Ezequiel Cicutti, Daniel C. Moreira, and Javier Danilo Gonzalez Ramos. New cns tumor classification: the importance in pediatric neurosurgical practice. Surgical Neurology International, 15:130, Apr 2024. URL: https://doi.org/10.25259/sni\_681\_2023, doi:10.25259/sni\_681\_2023. This article has 2 citations and is from a peer-reviewed journal.

17. (bale2022the2021who pages 8-9): Tejus A. Bale and Marc K. Rosenblum. The 2021 who classification of tumors of the central nervous system: an update on pediatric low‐grade gliomas and glioneuronal tumors. Brain Pathology, Feb 2022. URL: https://doi.org/10.1111/bpa.13060, doi:10.1111/bpa.13060. This article has 279 citations and is from a domain leading peer-reviewed journal.

18. (capper2023eanoguidelineon pages 11-12): David Capper, Guido Reifenberger, Pim J French, Leonille Schweizer, Michael Weller, Mehdi Touat, Simone P Niclou, Philipp Euskirchen, Christine Haberler, Monika E Hegi, Sebastian Brandner, Emilie Le Rhun, Roberta Rudà, Marc Sanson, Ghazaleh Tabatabai, Felix Sahm, Patrick Y Wen, Pieter Wesseling, Matthias Preusser, and Martin J van den Bent. Eano guideline on rational molecular testing of gliomas, glioneuronal, and neuronal tumors in adults for targeted therapy selection. Neuro-Oncology, 25:813-826, Jan 2023. URL: https://doi.org/10.1093/neuonc/noad008, doi:10.1093/neuonc/noad008. This article has 129 citations and is from a domain leading peer-reviewed journal.

19. (bale2022the2021who pages 5-6): Tejus A. Bale and Marc K. Rosenblum. The 2021 who classification of tumors of the central nervous system: an update on pediatric low‐grade gliomas and glioneuronal tumors. Brain Pathology, Feb 2022. URL: https://doi.org/10.1111/bpa.13060, doi:10.1111/bpa.13060. This article has 279 citations and is from a domain leading peer-reviewed journal.

20. (crainic2023rareneuronalglial pages 5-6): Nicolas Crainic, Julia Furtner, Johan Pallud, Franck Bielle, Giuseppe Lombardi, Roberta Rudà, and Ahmed Idbaih. Rare neuronal, glial and glioneuronal tumours in adults. Cancers, 15:1120, Feb 2023. URL: https://doi.org/10.3390/cancers15041120, doi:10.3390/cancers15041120. This article has 7 citations.

21. (bale2022the2021who pages 3-5): Tejus A. Bale and Marc K. Rosenblum. The 2021 who classification of tumors of the central nervous system: an update on pediatric low‐grade gliomas and glioneuronal tumors. Brain Pathology, Feb 2022. URL: https://doi.org/10.1111/bpa.13060, doi:10.1111/bpa.13060. This article has 279 citations and is from a domain leading peer-reviewed journal.

22. (vaz2022uncommonglioneuronaltumors pages 8-9): A. Vaz, M.S. Cavalcanti, E.B. da Silva Junior, R. Ramina, and B.C. de Almeida Teixeira. Uncommon glioneuronal tumors: a radiologic and pathologic synopsis. American Journal of Neuroradiology, 43:1080-1089, May 2022. URL: https://doi.org/10.3174/ajnr.a7465, doi:10.3174/ajnr.a7465. This article has 25 citations and is from a peer-reviewed journal.

23. (pereira2026molecularfeaturesin pages 4-5): Benedito Jamilson Araújo Pereira, Sueli Mieko Oba-Shinjo, Ivy Karoline Herculano de Azevedo, Yuri Reis Casal, Wen Hung Tzu, Antônio Nogueira de Almeida, Wellingson Silva Paiva, and Suely Kazue Nagahashi Marie. Molecular features in gangliogliomas: a systematic review. Child's Nervous System, Feb 2026. URL: https://doi.org/10.1007/s00381-026-07170-7, doi:10.1007/s00381-026-07170-7. This article has 1 citations.

24. (engelhardt2022frequentfgfr1hotspot pages 1-2): Sophie Engelhardt, Felix Behling, Rudi Beschorner, Franziska Eckert, Patricia Kohlhof, Marcos Tatagiba, Ghazaleh Tabatabai, Martin U. Schuhmann, Martin Ebinger, and Jens Schittenhelm. Frequent fgfr1 hotspot alterations in driver-unknown low-grade glioma and mixed neuronal-glial tumors. Journal of Cancer Research and Clinical Oncology, 148:857-866, Jan 2022. URL: https://doi.org/10.1007/s00432-021-03906-x, doi:10.1007/s00432-021-03906-x. This article has 25 citations and is from a peer-reviewed journal.

25. (pereira2026molecularfeaturesin pages 8-9): Benedito Jamilson Araújo Pereira, Sueli Mieko Oba-Shinjo, Ivy Karoline Herculano de Azevedo, Yuri Reis Casal, Wen Hung Tzu, Antônio Nogueira de Almeida, Wellingson Silva Paiva, and Suely Kazue Nagahashi Marie. Molecular features in gangliogliomas: a systematic review. Child's Nervous System, Feb 2026. URL: https://doi.org/10.1007/s00381-026-07170-7, doi:10.1007/s00381-026-07170-7. This article has 1 citations.

26. (ostrom2021cbtrusstatisticalreport pages 50-51): Quinn T Ostrom, Gino Cioffi, Kristin Waite, Carol Kruchko, and Jill S Barnholtz-Sloan. Cbtrus statistical report: primary brain and other central nervous system tumors diagnosed in the united states in 2014-2018. Neuro-oncology, 23 Supplement_3:iii1-iii105, Oct 2021. URL: https://doi.org/10.1093/neuonc/noab200, doi:10.1093/neuonc/noab200. This article has 1958 citations and is from a domain leading peer-reviewed journal.

27. (iijima2024genotyperelevantneuroimagingfeatures pages 9-9): Keiya Iijima, Hiroyuki Fujii, Fumio Suzuki, Kumiko Murayama, Yu-ichi Goto, Yuko Saito, Terunori Sano, Hiroyoshi Suzuki, Hajime Miyata, Yukio Kimura, Takuma Nakashima, Hiromichi Suzuki, Masaki Iwasaki, and Noriko Sato. Genotype-relevant neuroimaging features in low-grade epilepsy-associated tumors. Frontiers in Neurology, Jul 2024. URL: https://doi.org/10.3389/fneur.2024.1419104, doi:10.3389/fneur.2024.1419104. This article has 2 citations and is from a peer-reviewed journal.

28. (capper2023eanoguidelineon pages 3-4): David Capper, Guido Reifenberger, Pim J French, Leonille Schweizer, Michael Weller, Mehdi Touat, Simone P Niclou, Philipp Euskirchen, Christine Haberler, Monika E Hegi, Sebastian Brandner, Emilie Le Rhun, Roberta Rudà, Marc Sanson, Ghazaleh Tabatabai, Felix Sahm, Patrick Y Wen, Pieter Wesseling, Matthias Preusser, and Martin J van den Bent. Eano guideline on rational molecular testing of gliomas, glioneuronal, and neuronal tumors in adults for targeted therapy selection. Neuro-Oncology, 25:813-826, Jan 2023. URL: https://doi.org/10.1093/neuonc/noad008, doi:10.1093/neuonc/noad008. This article has 129 citations and is from a domain leading peer-reviewed journal.

29. (vaz2022uncommonglioneuronaltumors pages 9-10): A. Vaz, M.S. Cavalcanti, E.B. da Silva Junior, R. Ramina, and B.C. de Almeida Teixeira. Uncommon glioneuronal tumors: a radiologic and pathologic synopsis. American Journal of Neuroradiology, 43:1080-1089, May 2022. URL: https://doi.org/10.3174/ajnr.a7465, doi:10.3174/ajnr.a7465. This article has 25 citations and is from a peer-reviewed journal.

30. (crainic2023rareneuronalglial pages 18-19): Nicolas Crainic, Julia Furtner, Johan Pallud, Franck Bielle, Giuseppe Lombardi, Roberta Rudà, and Ahmed Idbaih. Rare neuronal, glial and glioneuronal tumours in adults. Cancers, 15:1120, Feb 2023. URL: https://doi.org/10.3390/cancers15041120, doi:10.3390/cancers15041120. This article has 7 citations.

31. (capper2023eanoguidelineon pages 2-3): David Capper, Guido Reifenberger, Pim J French, Leonille Schweizer, Michael Weller, Mehdi Touat, Simone P Niclou, Philipp Euskirchen, Christine Haberler, Monika E Hegi, Sebastian Brandner, Emilie Le Rhun, Roberta Rudà, Marc Sanson, Ghazaleh Tabatabai, Felix Sahm, Patrick Y Wen, Pieter Wesseling, Matthias Preusser, and Martin J van den Bent. Eano guideline on rational molecular testing of gliomas, glioneuronal, and neuronal tumors in adults for targeted therapy selection. Neuro-Oncology, 25:813-826, Jan 2023. URL: https://doi.org/10.1093/neuonc/noad008, doi:10.1093/neuonc/noad008. This article has 129 citations and is from a domain leading peer-reviewed journal.

32. (capper2023eanoguidelineon pages 9-10): David Capper, Guido Reifenberger, Pim J French, Leonille Schweizer, Michael Weller, Mehdi Touat, Simone P Niclou, Philipp Euskirchen, Christine Haberler, Monika E Hegi, Sebastian Brandner, Emilie Le Rhun, Roberta Rudà, Marc Sanson, Ghazaleh Tabatabai, Felix Sahm, Patrick Y Wen, Pieter Wesseling, Matthias Preusser, and Martin J van den Bent. Eano guideline on rational molecular testing of gliomas, glioneuronal, and neuronal tumors in adults for targeted therapy selection. Neuro-Oncology, 25:813-826, Jan 2023. URL: https://doi.org/10.1093/neuonc/noad008, doi:10.1093/neuonc/noad008. This article has 129 citations and is from a domain leading peer-reviewed journal.

33. (bent2025updatedeanoguideline pages 1-2): Martin J van den Bent, Enrico Franceschi, Mehdi Touat, Pim J French, Ahmed Idbaih, Giuseppe Lombardi, Roberta Rudà, Leonille Schweizer, David Capper, Marc Sanson, Pieter Wesseling, Michael Weller, Marica Eoli, Elena Anghileri, Franck Bielle, Phillipp Euskirchen, Marjolein Geurts, Patrick Y Wen, and Matthias Preusser. Updated eano guideline on rational molecular testing of gliomas, glioneuronal, and neuronal tumors in adults for targeted therapy selection—update 1. Neuro-Oncology, 27:331-337, Oct 2025. URL: https://doi.org/10.1093/neuonc/noae213, doi:10.1093/neuonc/noae213. This article has 27 citations and is from a domain leading peer-reviewed journal.

34. (capper2023eanoguidelineon pages 6-7): David Capper, Guido Reifenberger, Pim J French, Leonille Schweizer, Michael Weller, Mehdi Touat, Simone P Niclou, Philipp Euskirchen, Christine Haberler, Monika E Hegi, Sebastian Brandner, Emilie Le Rhun, Roberta Rudà, Marc Sanson, Ghazaleh Tabatabai, Felix Sahm, Patrick Y Wen, Pieter Wesseling, Matthias Preusser, and Martin J van den Bent. Eano guideline on rational molecular testing of gliomas, glioneuronal, and neuronal tumors in adults for targeted therapy selection. Neuro-Oncology, 25:813-826, Jan 2023. URL: https://doi.org/10.1093/neuonc/noad008, doi:10.1093/neuonc/noad008. This article has 129 citations and is from a domain leading peer-reviewed journal.

35. (rosenberg2022upfrontmoleculartargeted pages 5-6): Tom Rosenberg, Kee Kiat Yeo, Audrey Mauguen, Sanda Alexandrescu, Sanjay P Prabhu, Jessica W Tsai, Seth Malinowski, Mrinal Joshirao, Karishma Parikh, Sameer Farouk Sait, Marc K Rosenblum, Jamal K Benhamida, George Michaiel, Hung N Tran, Sonika Dahiya, Kara Kachurak, Gregory K Friedman, Julie I Krystal, Michael A Huang, Ashley S Margol, Karen D Wright, Dolly Aguilera, Tobey J MacDonald, Susan N Chi, and Matthias A Karajannis. Upfront molecular targeted therapy for the treatment of braf-mutant pediatric high-grade glioma. Neuro-oncology, 24:1964-1975, Apr 2022. URL: https://doi.org/10.1093/neuonc/noac096, doi:10.1093/neuonc/noac096. This article has 62 citations and is from a domain leading peer-reviewed journal.

36. (talloa2022brafandmek pages 10-11): Dario Talloa, Silvia Triarico, Pierpaolo Agresti, Stefano Mastrangelo, Giorgio Attinà, Alberto Romano, Palma Maurizi, and Antonio Ruggiero. Braf and mek targeted therapies in pediatric central nervous system tumors. Cancers, 14:4264, Aug 2022. URL: https://doi.org/10.3390/cancers14174264, doi:10.3390/cancers14174264. This article has 34 citations.

## Artifacts

- [Edison artifact artifact-00](Mixed_Neuronal-Glial_Tumor-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Mixed_Neuronal-Glial_Tumor-deep-research-falcon_artifacts/artifact-01.md)