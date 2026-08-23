---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T09:09:34.248483'
end_time: '2026-08-19T09:21:41.547961'
duration_seconds: 727.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MT-ATP6/MT-ATP8-Related Infantile Hypertrophic Cardiomyopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: MT-ATP6_MT-ATP8-Related_Infantile_Hypertrophic_Cardiomyopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MT-ATP6/MT-ATP8-Related Infantile Hypertrophic Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MT-ATP6/MT-ATP8-Related Infantile Hypertrophic Cardiomyopathy** covering all of the
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
- **Disease Name:** MT-ATP6/MT-ATP8-Related Infantile Hypertrophic Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MT-ATP6/MT-ATP8-Related Infantile Hypertrophic Cardiomyopathy** covering all of the
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


# MT-ATP6/MT-ATP8–Related Infantile Hypertrophic Cardiomyopathy

## Executive summary and scope

**MT-ATP6/MT-ATP8–related infantile hypertrophic cardiomyopathy (HCM)** is best treated as an **ultra-rare phenotypic subset of mitochondrial ATP-synthase (complex V) deficiency**, rather than a fully established standalone nosologic entity. The strongest direct association is with **m.8528T>C**, which lies in the overlapping coding region of *MT-ATP8* and *MT-ATP6*. It changes both proteins—ATP8/A6L p.Trp55Arg and the ATP6/subunit-a initiation methionine p.Met1Thr—and has produced prenatal-to-5-month-onset hypertrophic or biventricular cardiomyopathy, heart failure, metabolic crises, feeding failure, hypotonia, and early death. Available cases usually had mutant loads above 90%, although 59% in blood was reported in one patient. Biochemical studies showed markedly reduced ATP6/ATP8 synthesis, complex V abundance, and ATP production. (tauchmannova2024variabilityofclinical pages 5-7)

This distinction matters: common *MT-ATP6* alleles such as m.8993T>G/C and m.9176T>G/C cause a much broader Leigh/NARP spectrum in which cardiomyopathy may occur, but they should not automatically be labeled “MT-ATP6/MT-ATP8-related infantile HCM.” The 2025 natural-history cohort is therefore useful for context, not a prevalence study of the narrowly defined cardiac phenotype.

**Evidence base.** Direct disease-specific evidence consists mainly of individual patients and small case series, supplemented by aggregated variant reviews and a broader 111-person MT-ATP6/8 natural-history cohort. Thus, patient-level frequencies should not be inferred from the case reports, and broader cohort frequencies should not be assumed to describe m.8528T>C specifically.

| Variant | Genes / protein change | Genetic state | Onset / cardiac phenotype | Extracardiac / biochemical features | Functional consequence | Evidence / source |
|---|---|---|---|---|---|---|
| m.8528T>C | Overlapping **MT-ATP8/MT-ATP6** variant; affects A6L **p.Trp55Arg** and ATP6 start codon/subunit a **p.Met1Thr** | Usually **high heteroplasmy >90%**; one reported patient had **59% in blood** | **Directly associated with infantile HCM**: prenatal to 5 months; **hypertrophic cardiomyopathy / biventricular hypertrophy**, heart failure; some cases rapidly progressive and fatal in months | Hypotonia, failure to thrive, feeding difficulties, metabolic crises, 3-methylglutaconic aciduria, hyperketonemia; reported arrhythmia/WPW, pulmonary arterial hypertension, LV noncompaction, anemia, thrombocytopenia, myopathy/progressive weakness | Marked reduction in synthesis of **both ATPase 6 and 8**, reduced complex V levels/assembly-stability, decreased ATP synthesis; review states loss of subunit a is primary driver | Core infantile HCM allele; summarized from 2024 review and cited primary infantile cardiomyopathy reports (tauchmannova2024variabilityofclinical pages 5-7, tauchmannova2024variabilityofclinical pages 8-10, jackson2017anovelmitochondrial pages 15-19) |
| m.8529G>A | Overlapping **MT-ATP8/MT-ATP6** variant; primarily affects **A6L p.Trp55Ter**; nearby allelic comparator | Reported **high heteroplasmy >90%** | **Not a direct infantile HCM allele in available evidence**; later onset (~4 years) with HCM reported in one patient, milder than m.8528T>C | Neuropathy, ataxia, ophthalmoplegia, psychomotor retardation | Decreased ATP synthase stability; unlike m.8528T>C, mainly affects **A6L** rather than causing loss of subunit a | Useful allelic comparison showing overlapping-region variants can differ markedly in severity and age at onset (tauchmannova2024variabilityofclinical pages 8-10, dotto2024variantsinhuman pages 23-24) |
| m.8993T>G | **MT-ATP6**; ATP6 **p.Leu156Arg** | Often **high heteroplasmy**; >90% strongly associated with severe Leigh/MILS spectrum | **Broader MT-ATP6 disease context**; cardiomyopathy can occur, but available evidence does **not** support it as a specific core allele for infantile HCM | Leigh syndrome/MILS, lactic acidosis, developmental delay/regression, seizures, brainstem dysfunction, peripheral neuropathy, optic atrophy; low citrulline in broader MT-ATP6 disease | Impaired ATP synthase assembly, decreased ATP synthesis, abnormal membrane potential; severity tracks with heteroplasmy | Major disease-context allele; common in cohorts, including infantile-onset MT-ATP6/8 disease, but not specific for infantile HCM (uittenbogaard2018novelinsightsinto pages 1-3, ganetzky2019mt‐atp6mitochondrialdisease pages 3-4, carli2025naturalhistoryof pages 5-7) |
| m.8993T>C | **MT-ATP6**; same codon as m.8993T>G with different substitution | Heteroplasmic; higher loads linked to more severe disease | **Broader MT-ATP6 disease context**; review notes cardiomyopathy has been linked, but phenotype is predominantly neurodegenerative and often later than overlapping-region infantile HCM | NARP/Leigh spectrum, variable neurologic disease; biomarkers in MT-ATP6/8 cohorts include lactate elevation, alanine elevation, reduced citrulline | Complex V dysfunction with variable biochemical findings; no single universal assay abnormality | Included to frame broader genotype-phenotype spectrum without over-attributing infantile HCM (tauchmannova2024variabilityofclinical pages 8-10, carli2025naturalhistoryof pages 1-2, ganetzky2019mt‐atp6mitochondrialdisease pages 1-3) |
| m.9176T>G / m.9176T>C | **MT-ATP6** codon 217 variants | Heteroplasmic to homoplasmic; severe disease more likely at high mutant load | **Broader MT-ATP6 disease context**; can be associated with Leigh-spectrum disease and cardiomyopathy/non-neurologic manifestations, but not established here as a defining infantile HCM allele | Newborn-screened MT-ATP6 cases with low citrulline and/or elevated C5-OH included **m.9176T>G**; neurologic phenotypes range from asymptomatic to hypertonia/intellectual disability; hypertrophic cardiomyopathy recognized among MT-ATP6 manifestations overall | ATP synthase dysfunction; therapeutic research includes mitoTALEN targeting of **m.9176T>C** in murine oocytes in experimental prevention studies | Important contextual alleles for diagnosis/screening and experimental therapy, not the core infantile HCM genotype in available evidence (peretz2021prospectivediagnosisof pages 6-8, peretz2021prospectivediagnosisof pages 1-3, dotto2024variantsinhuman pages 23-24) |


*Table: This table summarizes the strongest available genotype-phenotype evidence for MT-ATP6/MT-ATP8-related infantile hypertrophic cardiomyopathy, centered on the overlapping-region m.8528T>C allele. It also places neighboring and common MT-ATP6 alleles in context while distinguishing direct infantile HCM evidence from broader mitochondrial disease associations.*

---

## 1. Disease information

### Definition and terminology

The disorder is a primary mitochondrial cardiomyopathy caused by defective mitochondrial ATP synthase. Suggested synonyms are:

- *MT-ATP6/MT-ATP8 overlapping-region mitochondrial cardiomyopathy*
- *ATP synthase subunit 6/8 deficiency with infantile hypertrophic cardiomyopathy*
- *Complex V deficiency with infantile cardiomyopathy*
- *Rapidly progressive infantile cardiomyopathy due to loss of ATPase 6 and 8 proteins*—the wording used in the 2016 primary report title (DOI: [10.1016/j.ijcard.2016.01.026](https://doi.org/10.1016/j.ijcard.2016.01.026)). The later literature identifies this report as infantile cardiomyopathy with complex V deficiency caused by loss of both ATPase proteins. (tauchmannova2024variabilityofclinical pages 26-27, jackson2017anovelmitochondrial pages 15-19)

### Identifiers

No dedicated **MONDO, OMIM, Orphanet, MeSH, ICD-10, or ICD-11 identifier** for this exact genotype-plus-infantile-HCM entity was established from the retrieved literature. It should therefore be represented as a compositional knowledge-base entity linking:

1. mitochondrial ATP synthase deficiency / primary mitochondrial disease;
2. hypertrophic cardiomyopathy;
3. *MT-ATP6* and *MT-ATP8*;
4. the causal mtDNA variant, especially m.8528T>C.

Relevant broader OMIM phenotypes include **NARP, OMIM 551500**, and **maternally inherited Leigh syndrome, OMIM 516060**, but neither is synonymous with the cardiac entity. The literature also references Leigh syndrome OMIM 256000 in the broader *MT-ATP6* spectrum. (dotto2024variantsinhuman pages 18-20, uittenbogaard2018novelinsightsinto pages 1-3)

Suggested coding: **HCM—I42.2 (ICD-10-CM)** plus a mitochondrial-metabolism code where local coding rules permit; this is pragmatic coding, not a disease-specific identifier.

---

## 2. Etiology

### Causal factors and genetic risk

The primary cause is a **germline mitochondrial-DNA variant** affecting complex V. The core allele, **m.8528T>C**, occurs where *MT-ATP8* and *MT-ATP6* overlap and simultaneously alters two polypeptides. Its high heteroplasmy, dual-protein effect, marked complex V deficiency, and recurrence with early cardiomyopathy provide the strongest causal evidence. (tauchmannova2024variabilityofclinical pages 5-7)

Risk is governed principally by:

- **Mutant heteroplasmy:** higher loads generally predict earlier and more severe disease. Across published *MT-ATP6* cases, affected individuals had much higher heteroplasmy than asymptomatic relatives; younger onset correlated inversely with heteroplasmy (r=−0.37, p=1.6×10⁻⁷). Nevertheless, overlap between affected and unaffected carriers prevents use of a single deterministic threshold. (ganetzky2019mt‐atp6mitochondrialdisease pages 3-4, ganetzky2019mt‐atp6mitochondrialdisease pages 1-3)
- **Tissue distribution:** blood heteroplasmy may not equal myocardium, muscle, urine, or other tissues.
- **Mitochondrial and nuclear background:** severe variation among persons with similar loads implies modifying haplogroup, nuclear-genetic, developmental, and tissue-threshold effects. (peretz2021prospectivediagnosisof pages 6-8, uittenbogaard2018novelinsightsinto pages 1-3)

The m.8993T>G allele illustrates the threshold principle: below approximately 60% can be asymptomatic, 75–90% is often associated with NARP, and >90% with Leigh/MILS, although these are probabilistic rather than absolute boundaries. (uittenbogaard2018novelinsightsinto pages 1-3)

### Environmental, lifestyle, infectious, and protective factors

No toxin, infection, lifestyle exposure, sex, or occupational factor is known to cause this Mendelian mitochondrial disorder. Fever, fasting, dehydration, anesthesia, and intercurrent infection may plausibly precipitate energetic decompensation in mitochondrial disease, but disease-specific interaction estimates were not found. No validated protective allele or environmental factor has been identified.

Early recognition, avoidance of catabolism, and prompt treatment of intercurrent illness are clinically protective strategies rather than primary prevention. In six newborn-screened *MT-ATP6* patients treated prospectively, no metabolic crises or developmental regression occurred, but this uncontrolled observation cannot establish efficacy. (peretz2021prospectivediagnosisof pages 1-3)

---

## 3. Phenotypes

### Core m.8528T>C phenotype

| Phenotype | Characterization | Suggested HPO term |
|---|---|---|
| Hypertrophic/biventricular cardiomyopathy | Prenatal to 5 months; severe and rapidly progressive; defining manifestation | HP:0001639 Hypertrophic cardiomyopathy |
| Heart failure | Infantile, severe; may be fatal | HP:0001635 Congestive heart failure |
| Ventricular hypertrophy | Can involve both ventricles | HP:0001712 Left ventricular hypertrophy; right-ventricular hypertrophy term as applicable |
| Arrhythmia/Wolff–Parkinson–White | Reported in the allelic case spectrum | HP:0011675 Arrhythmia; HP:0001716 WPW syndrome |
| LV noncompaction | Reported but not universal | HP:0011663 Left ventricular noncompaction |
| Pulmonary arterial hypertension | Reported complication | HP:0002092 Pulmonary arterial hypertension |
| Metabolic crisis/acidosis | Episodic deterioration, sometimes with hyperketonemia or hyperammonemia | HP:0001942 Metabolic acidosis; HP:0001987 Hyperammonemia |
| Hypotonia/weakness | Early and potentially progressive | HP:0001252 Hypotonia; HP:0001324 Muscle weakness |
| Feeding difficulty/failure to thrive | Severe infant functional impact | HP:0011968 Feeding difficulties; HP:0001508 Failure to thrive |
| 3-methylglutaconic aciduria | Biochemical abnormality in some cases | HP:0003535 3-methylglutaconic aciduria |
| Cytopenias | Anemia and thrombocytopenia reported | HP:0001903 Anemia; HP:0001873 Thrombocytopenia |

These manifestations and the prenatal-to-five-month onset derive from sparse case reports; two reported infants died within months. They must not be interpreted as reliable percentages. (tauchmannova2024variabilityofclinical pages 5-7)

### Broader MT-ATP6/8 spectrum

The 2025 multicenter cohort included **111 genetically confirmed patients**: 44% had onset before age 1 year, 36% at 1–12 years, and 20% after age 12. CNS, muscle, eye, and heart involvement occurred in 93%, 75%, 46%, and 18%, respectively. Among infantile-onset patients, cardiomyopathy occurred in 29% and HCM in 21%; corresponding cardiomyopathy frequencies were 9% in pediatric-onset and 5% in late-onset groups. These are broader ATP6/8-deficiency statistics, not m.8528T>C-specific estimates. (carli2025naturalhistoryof pages 5-7, carli2025naturalhistoryof pages 1-2)

Neurologic findings include developmental delay/regression, hypotonia, dystonia, spasticity, chorea, ataxia, peripheral neuropathy, seizures, retinitis pigmentosa, optic disease, and Leigh-pattern MRI lesions. In the natural-history cohort, 91% of 86 imaged patients had abnormal MRI; 54% had Leigh-like lesions, 10% cerebellar atrophy, and 21% white-matter abnormalities. Eleven percent were wheelchair-dependent, while 19% of those with walking data never acquired walking. (peretz2021prospectivediagnosisof pages 1-3, carli2025naturalhistoryof pages 2-3)

**Quality of life:** no disease-specific EQ-5D, SF-36, or pediatric quality-of-life dataset was found. Severe heart failure, feeding dependence, hospitalization during metabolic crises, inability to walk, and multisystem impairment imply major patient and caregiver burden.

---

## 4. Genetic and molecular information

### Genes

- ***MT-ATP6***: mitochondrially encoded ATP synthase membrane subunit a/6; part of the proton-translocating F\(_o\) sector.
- ***MT-ATP8***: mitochondrially encoded ATP synthase subunit 8/A6L.
- Both are mtDNA protein-coding genes with a short overlapping coding region.

Suggested annotations: **HGNC symbols MT-ATP6 and MT-ATP8**; GO molecular function/pathway annotations should emphasize proton-transporting ATP synthase activity and oxidative phosphorylation.

### Variant interpretation

**m.8528T>C** is a missense/start-loss–like overlapping variant: ATP8 p.Trp55Arg and ATP6 p.Met1Thr. The latter may disrupt translation initiation, and biochemical data indicate that loss of ATP6/subunit a is the major driver of reduced complex V assembly or stability. Most affected patients had >90% mutant load. (tauchmannova2024variabilityofclinical pages 5-7, tauchmannova2024variabilityofclinical pages 8-10)

**m.8529G>A**, an informative comparator, produces ATP8 p.Trp55Ter but primarily spares ATP6. A >90%-heteroplasmic patient developed HCM and neurologic disease around age four—substantially later than m.8528T>C—supporting the greater severity of losing ATP6/subunit a. (tauchmannova2024variabilityofclinical pages 8-10)

Across the 111-patient cohort, 26 pathogenic variants were identified: 20 in *MT-ATP6*, three in *MT-ATP8*, and three in the overlap. m.8993T>G accounted for 46%, m.8993T>C for 17%, and m.9185T>C for 9%. Median blood heteroplasmy was higher in infantile-onset (92.5%) than pediatric-onset (86.8%) or late-onset disease (80.6%). (carli2025naturalhistoryof pages 5-7)

**Population frequency:** no defensible gnomAD-mtDNA/TOPMed frequency for m.8528T>C was recovered. Given its severity, recurrence only in rare patients, and high heteroplasmy requirement, population carrier frequency cannot be estimated from current reports. mtDNA variants are germline/maternally transmitted or de novo, not somatic cancer mutations in this context.

**Modifiers, epigenetics, and chromosomal abnormalities:** no validated modifier gene, disease-specific methylation signature, chromosomal rearrangement, or anticipation mechanism is established. Apparent generational changes reflect mtDNA bottleneck and heteroplasmy segregation, not classical repeat-expansion anticipation.

---

## 5. Environmental information

No causal pollution, radiation, toxin, diet, smoking, alcohol, or infectious agent is implicated. Environmental stressors can affect demand on an already constrained oxidative-phosphorylation system, but quantitative gene–environment studies specific to this cardiomyopathy are absent. Infection-associated catabolism may unmask or worsen disease; it does not create the pathogenic genotype.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** m.8528T>C alters ATP8 and the ATP6 initiation codon.
2. **Protein/assembly defect:** synthesis of both mitochondrially encoded proteins falls; subunit-a deficiency destabilizes or prevents normal complex V assembly.
3. **Bioenergetic defect:** ATP synthase abundance and ATP-production rate decrease; pathogenic *MT-ATP6* variants may also cause abnormally elevated mitochondrial membrane potential, although biochemical signatures vary by allele. (tauchmannova2024variabilityofclinical pages 5-7, ganetzky2019mt‐atp6mitochondrialdisease pages 3-4)
4. **Cellular compensation/injury:** inadequate oxidative phosphorylation, altered proton utilization, redox imbalance, abnormal calcium handling, and secondary reactive-oxygen-species stress are expected in energy-demanding cardiomyocytes. The literature emphasizes that no single biochemical abnormality is universal across *MT-ATP6* disease. (ganetzky2019mt‐atp6mitochondrialdisease pages 1-3, dotto2024variantsinhuman pages 20-22)
5. **Tissue phenotype:** fetal/infant cardiomyocytes have continuous ATP demand. Energetic insufficiency and maladaptive hypertrophic remodeling produce myocardial thickening, impaired filling/contractility, conduction disease, and heart failure; systemic energy failure produces hypotonia, feeding failure, lactic/metabolic crises, and neurologic injury.

### Ontology suggestions

- **GO biological process:** oxidative phosphorylation (GO:0006119); ATP synthesis coupled proton transport (GO:0015986); mitochondrial ATP synthesis coupled proton transport (GO:0042776); cellular response to oxidative stress (GO:0034599).
- **GO cellular component:** mitochondrion (GO:0005739); mitochondrial inner membrane (GO:0005743); proton-transporting ATP synthase complex (GO:0045259).
- **Cell Ontology:** cardiomyocyte (CL:0000746); ventricular cardiac muscle cell; skeletal muscle cell; neuron; retinal photoreceptor cell.
- **Chemical entities:** ATP (CHEBI:15422), ADP (CHEBI:16761), L-lactic acid/lactate, L-citrulline, L-alanine.

### Molecular profiling gaps

No disease-specific cardiac single-cell atlas, spatial transcriptomic dataset, systematic transcriptomic/proteomic/lipidomic signature, epigenomic study, or CRISPR screen was identified. Available “omics” evidence is principally mtDNA sequencing plus targeted respiratory-chain and metabolite assays. This is a major knowledge gap.

---

## 7. Anatomical structures affected

**Primary organ:** heart, especially ventricular myocardium; both ventricles may be hypertrophied. Suggested terms: **UBERON:0000948 heart**, myocardium, left ventricle, right ventricle; **CL:0000746 cardiomyocyte**.

**Secondary systems:** brain/CNS, peripheral nerves, skeletal muscle, retina/optic system, pulmonary vasculature, liver/metabolic system, and hematopoietic system. In broader ATP6/8 deficiency, CNS and muscle involvement substantially exceed cardiac involvement. (carli2025naturalhistoryof pages 2-3, carli2025naturalhistoryof pages 1-2)

**Subcellular site:** mitochondrial inner membrane and F\(_o\) sector of ATP synthase. No lateralization applies.

---

## 8. Temporal development

The defining cardiac phenotype is **congenital or early infantile**, with reported onset prenatally through five months. Progression may be rapid—from hypertrophy to heart failure, arrhythmia, metabolic decompensation, multiorgan failure, and death within months. (tauchmannova2024variabilityofclinical pages 5-7)

In broader MT-ATP6/8 disease, onset spans birth to 58 years (median one year). Approximately 55% of early-onset patients experienced metabolic acidosis or acute deterioration. The course may therefore combine chronic neurologic/myopathic progression with episodic metabolic crises. (carli2025naturalhistoryof pages 2-3, carli2025naturalhistoryof pages 1-2)

No reproducible spontaneous remission pattern is known. The neonatal period, intercurrent illness, and first metabolic decompensation are likely critical intervention windows, but prospective disease-specific evidence is lacking.

---

## 9. Inheritance and population

### Inheritance

Inheritance is **mitochondrial/maternal** when the mother carries the variant, with marked recurrence-risk uncertainty because the oocyte bottleneck causes wide heteroplasmy segregation. De novo mtDNA events also occur. Fathers do not transmit mtDNA. Penetrance is incomplete and load-/tissue-/age-dependent; expressivity is highly variable. (peretz2021prospectivediagnosisof pages 6-8, ganetzky2019mt‐atp6mitochondrialdisease pages 1-3)

Maternal blood testing alone cannot reliably quantify recurrence risk or exclude low-level/tissue-restricted heteroplasmy. “Germline mosaicism” is better represented here as maternal heteroplasmy across oocytes and tissues. Consanguinity is not a causal feature of mtDNA transmission, although it remains relevant when considering recessive nuclear mitochondrial disorders.

### Epidemiology

No incidence, prevalence, carrier-frequency, founder-effect, geographic enrichment, or ethnicity-specific rate exists for the narrow infantile-HCM phenotype. The 111-person cohort had 55 males and 56 females, consistent with no sex-linked transmission; 44% had infantile onset and 18% had cardiac involvement. These registry data cannot yield population prevalence. (carli2025naturalhistoryof pages 1-2)

---

## 10. Diagnostics

### Recommended workflow

1. **Recognize mitochondrial HCM:** neonatal/infantile HCM plus lactic or metabolic acidosis, hyperammonemia, hypotonia, feeding failure, neurologic abnormalities, unexplained cytopenias, or maternal family history.
2. **Cardiac evaluation:** echocardiography with wall thickness, ventricular function, outflow obstruction, diastolic function and noncompaction assessment; ECG/telemetry for pre-excitation and arrhythmia; BNP/NT-proBNP and troponin as clinically indicated; cardiac MRI when stable and feasible.
3. **Metabolic studies:** blood gas, lactate, pyruvate, glucose, ammonia, liver enzymes, CK, plasma amino acids—especially citrulline and alanine—acylcarnitines including C5-OH, urine organic acids including 3-methylglutaconic acid, ketones, and renal/hepatic function. In the broader cohort, lactate was elevated in 71%, alanine in 49%, and citrulline reduced in 56%. These are supportive, not diagnostic. (carli2025naturalhistoryof pages 1-2)
4. **Genetic confirmation:** high-depth **whole-mitochondrial-genome sequencing with heteroplasmy quantification**, explicitly covering the *MT-ATP8/MT-ATP6* overlap. Test blood promptly, but add urine epithelium, buccal cells, muscle, or available cardiac tissue if suspicion remains high or load appears discordant.
5. **Dual-genome testing:** a cardiomyopathy/mitochondrial panel or genome/exome analysis should assess nuclear mitochondrial and sarcomeric genes concurrently. Exome off-target mtDNA analysis can increase yield but a negative result does not exclude mtDNA disease and may require targeted deep sequencing in another tissue.
6. **Functional confirmation for novel/VUS alleles:** blue-native PAGE/complex V assembly, ATP synthesis, oxygen-consumption rate, membrane potential, respiratory-chain enzymology, and protein/translation studies in fibroblasts, muscle, or cybrids. No single assay is universally abnormal. (ganetzky2019mt‐atp6mitochondrialdisease pages 3-4, ganetzky2019mt‐atp6mitochondrialdisease pages 1-3)

### Newborn screening

Six infants with pathogenic *MT-ATP6* variants were prospectively identified through **low citrulline and/or elevated C5-OH**, then confirmed by mtDNA sequencing. The proposed algorithm combines both markers and confirms abnormalities with plasma amino acids and acylcarnitines. This is an emerging secondary finding, not a universally adopted population screen, and the study involved m.8993T>G or m.9176T>G rather than the core m.8528T>C cardiac allele. (peretz2021prospectivediagnosisof pages 1-3, peretz2021prospectivediagnosisof pages 6-8)

### Differential diagnosis

Exclude sarcomeric HCM; Pompe disease; fatty-acid oxidation defects; glycogen-storage disease; congenital disorders of glycosylation; RASopathies; lysosomal disease; and nuclear mitochondrial cardiomyopathies including *TMEM70*, *ATP5F1E/ATP5E*, *MRPL44*, *MRPS14*, *NDUFB7*, and other OXPHOS assembly/translation defects. Distinguishing clues are maternal inheritance, mtDNA heteroplasmy, multisystem energy failure, low citrulline, lactate elevation, and isolated complex V deficiency.

CMA, karyotype, FISH, and repeat-expansion testing are not first-line unless another phenotype suggests them. WES that ignores mtDNA is insufficient.

---

## 11. Outcome and prognosis

For m.8528T>C infantile cardiomyopathy, prognosis can be poor: rapid progression and death within the first months occurred in at least two reported patients. Reliable 1-, 5-, or 10-year survival rates do not exist. (tauchmannova2024variabilityofclinical pages 5-7)

In the broader 111-patient cohort, 92% were alive at last follow-up, but survival was significantly worse in infantile/pediatric-onset than adult-onset disease (p=0.0349). Seven recorded deaths were attributed variously to pneumonia, respiratory failure, seizures, COVID-19 complications, multiorgan failure, and cardiomyopathy. These aggregate outcomes should not be substituted for prognosis in severe neonatal cardiac disease. (carli2025naturalhistoryof pages 5-7, carli2025naturalhistoryof pages 1-2)

Adverse prognostic features likely include prenatal/neonatal onset, very high heteroplasmy, biventricular disease, declining ventricular function, arrhythmia, recurrent metabolic acidosis, respiratory failure, and multiorgan involvement. No validated cardiac prognostic biomarker exists.

---

## 12. Treatment

### Current clinical management

There is **no approved variant-correcting or disease-specific therapy**. Management should be coordinated by mitochondrial medicine, pediatric cardiology, intensive care, metabolic dietetics, neurology, genetics, and palliative care when appropriate.

- Treat heart failure and arrhythmias according to pediatric physiology and hemodynamics; avoid routine extrapolation from adult HCM.
- Prevent catabolism with adequate calories and prompt glucose-containing fluids during illness when appropriate; correct acidosis, hypoglycemia, electrolyte abnormalities, and hyperammonemia.
- Provide feeding support, respiratory support, physical/occupational therapy, and developmental services.
- Consider mechanical circulatory support or transplantation only through individualized multidisciplinary assessment; systemic mitochondrial disease and neurologic progression strongly influence candidacy. Disease-specific outcome data are absent.

Suggested NCIT intervention concepts include **Supportive Care**, **Nutritional Support**, **Cardiac Monitoring**, **Mechanical Ventilation**, **Hemodialysis** for severe hyperammonemia, and **Heart Transplantation** where applicable.

### Supplements and investigational pharmacology

A newborn-screening cohort received L-citrulline 250 mg/kg/day in two doses, ubiquinol 8 mg/kg/day, and B-complex vitamins; the six patients had no crises or regression during reported follow-up. Because there was no control group and the variants were not m.8528T>C, this is low-level evidence, not proof of benefit for infantile HCM. (peretz2021prospectivediagnosisof pages 1-3, peretz2021prospectivediagnosisof pages 6-8)

Antioxidants, N-acetylcysteine, vitamin-E derivatives, selenium, melatonin, resveratrol, α-ketoglutarate/aspartate, rapamycin/mTOR modulation, and vatiquinone have shown cellular, animal, or broader mitochondrial-disease signals. None has demonstrated cardiac benefit for this genotype. (dotto2024variantsinhuman pages 22-23, dotto2024variantsinhuman pages 31-32, dotto2024variantsinhuman pages 20-22)

The trial search found broader inherited-mitochondrial-disease studies—e.g., vatiquinone NCT05218655 and NCT04378075, elamipretide NCT02976038/NCT05162768, and arginine/citrulline NCT02809170—but no trial specifically enrolling MT-ATP6/MT-ATP8 infantile HCM. Consequently, efficacy cannot be inferred for this disease.

### Advanced therapeutics

Preclinical approaches include:

- allotopic nuclear expression of recoded wild-type ATP6/ATP8;
- mitochondrially targeted modified mRNA;
- mtZFNs and mitoTALENs that selectively reduce mutant mtDNA;
- experimental mitoTALEN targeting of m.9176T>C in murine oocytes.

Cybrid and mouse experiments have shown improved ATP, respiration, membrane potential, or stress growth, but import efficiency, heteroplasmy rebound, off-target cleavage, delivery to heart/CNS, and safety remain unresolved. These are not clinical treatments. (dotto2024variantsinhuman pages 23-24, dotto2024variantsinhuman pages 32-33)

No established pharmacogenomic dosing rule exists for *MT-ATP6*/*MT-ATP8*.

---

## 13. Prevention

**Primary prevention** by lifestyle modification is not possible. Reproductive options after identifying a maternal pathogenic variant include genetic counseling, prenatal diagnosis, preimplantation genetic testing with heteroplasmy assessment, donor oocytes, adoption, and—where legal and available—mitochondrial donation. Heteroplasmy can shift between sampled embryonic cells and later tissues, so residual risk must be explained.

**Secondary prevention** consists of cascade testing of maternal relatives, cardiac screening of carriers, prospective biochemical/developmental surveillance, and rapid evaluation of newborns. Low citrulline plus elevated C5-OH is a potential screening signature, but evidence remains limited to a small cohort. (peretz2021prospectivediagnosisof pages 1-3)

**Tertiary prevention** includes avoiding prolonged fasting/dehydration, maintaining emergency illness plans, early treatment of infection and catabolism, serial echocardiography/ECG, arrhythmia surveillance, nutritional support, vaccination according to standard schedules, and anesthetic planning. Vaccines do not prevent the genetic disease but can reduce infection-triggered decompensation.

---

## 14. Other species and natural disease

No naturally occurring companion-animal, livestock, or wildlife syndrome convincingly homologous to **m.8528T>C infantile HCM** was identified; no VBO breed association or zoonotic relevance applies. ATP synthase structure and oxidative phosphorylation are evolutionarily conserved, making cross-species functional modeling informative, but naturally occurring veterinary disease should be recorded as **not established**.

---

## 15. Model organisms and experimental systems

- **Saccharomyces cerevisiae** (NCBI Taxonomy 4932): genetically tractable ATP6/ATP8 models support structure–function analysis and variant pathogenicity assessment. Limitations include species-specific mitochondrial translation, ATP-synthase architecture, and absence of a mammalian heart. The ATP-synthase review explicitly uses yeast to interpret human mutations against structural data. (dautant2018atpsynthasediseases pages 1-2)
- **Patient fibroblasts/myoblasts:** retain the patient nuclear background and permit respiration, ATP, membrane-potential, translation, and complex-assembly studies; limitations include tissue heteroplasmy differences and low cardiac fidelity.
- **Transmitochondrial cybrids:** isolate mtDNA effects in a standardized nuclear background; useful for m.8993T>G, m.8529G>A, antioxidants, allotopic expression, and nucleases. They cannot reproduce developmental cardiomyopathy or multisystem interactions. (dotto2024variantsinhuman pages 23-24)
- **Murine oocytes and transgenic mice** (Mus musculus, NCBI Taxonomy 10090): used to test heteroplasmy-shifting nucleases and germline-transmission prevention. Delivery, off-target effects, and species-specific mtDNA biology limit translation. (dotto2024variantsinhuman pages 23-24)
- **iPSC-derived cardiomyocytes/organoids:** conceptually well suited to cardiac disease, but no validated m.8528T>C-specific iPSC-cardiomyocyte or cardiac-organoid model was identified.

---

## Recent authoritative developments

1. **2024 systematic ATP-synthase review:** Tauchmannová et al., published August 2024, consolidated the m.8528T>C cases and identified dual ATP8/ATP6 protein loss, high heteroplasmy, and prenatal-to-infantile HCM as the characteristic association. DOI: [10.33549/physiolres.935407](https://doi.org/10.33549/physiolres.935407). (tauchmannova2024variabilityofclinical pages 5-7)
2. **2024 variant/therapy review:** Del Dotto et al., published February 2024, integrated recent complex V structural biology with allotopic expression, modified RNA, and heteroplasmy-shifting nuclease strategies. DOI: [10.3390/ijms25042239](https://doi.org/10.3390/ijms25042239). (dotto2024variantsinhuman pages 23-24)
3. **2025 natural history:** Carli et al. provided the largest multicenter ATP6/8 cohort to date—111 patients, 98 previously unreported—and quantitative onset, organ, biomarker, heteroplasmy, and survival data. DOI: [10.1212/WNL.0000000000213462](https://doi.org/10.1212/WNL.0000000000213462). Although later than the requested 2023–2024 priority period, it is the strongest current disease-level dataset. (carli2025naturalhistoryof pages 5-7, carli2025naturalhistoryof pages 1-2)

## Evidence limitations and knowledge-base recommendations

This entry should be labeled **very low prevalence / prevalence unknown** and **limited clinical evidence**. The narrow disease definition rests predominantly on m.8528T>C case reports; larger cohorts combine neurologic, myopathic, ophthalmic, and cardiac phenotypes across many alleles. No validated prevalence, controlled treatment trial, cardiac natural-history series, quality-of-life study, disease-specific biomarker threshold, single-cell dataset, or dedicated ontology identifier was found.

For knowledge-base implementation, use a compositional record linking **m.8528T>C → MT-ATP8 p.Trp55Arg + MT-ATP6 p.Met1Thr/initiation defect → complex V deficiency → impaired ATP synthesis → infantile hypertrophic/biventricular cardiomyopathy and metabolic decompensation**, and keep broader m.8993/m.9176 evidence in an explicitly labeled “MT-ATP6/8 spectrum” section rather than treating all alleles as equivalent.

References

1. (tauchmannova2024variabilityofclinical pages 5-7): K. Tauchmannová, A. Pecinová, J. Houštěk, and T. Mrázek. Variability of clinical phenotypes caused by isolated defects of mitochondrial atp synthase. Physiological Research, pages S243-S278, Aug 2024. URL: https://doi.org/10.33549/physiolres.935407, doi:10.33549/physiolres.935407. This article has 17 citations and is from a peer-reviewed journal.

2. (tauchmannova2024variabilityofclinical pages 8-10): K. Tauchmannová, A. Pecinová, J. Houštěk, and T. Mrázek. Variability of clinical phenotypes caused by isolated defects of mitochondrial atp synthase. Physiological Research, pages S243-S278, Aug 2024. URL: https://doi.org/10.33549/physiolres.935407, doi:10.33549/physiolres.935407. This article has 17 citations and is from a peer-reviewed journal.

3. (jackson2017anovelmitochondrial pages 15-19): Christopher B. Jackson, Dagmar Hahn, Barbara Schröter, Uwe Richter, Brendan J. Battersby, Thomas Schmitt-Mechelke, Paula Marttinen, Jean-Marc Nuoffer, and André Schaller. A novel mitochondrial atp6 frameshift mutation causing isolated complex v deficiency, ataxia and encephalomyopathy. European journal of medical genetics, 60 6:345-351, Jun 2017. URL: https://doi.org/10.1016/j.ejmg.2017.04.006, doi:10.1016/j.ejmg.2017.04.006. This article has 40 citations and is from a peer-reviewed journal.

4. (dotto2024variantsinhuman pages 23-24): Valentina Del Dotto, Francesco Musiani, Alessandra Baracca, and Giancarlo Solaini. Variants in human atp synthase mitochondrial genes: biochemical dysfunctions, associated diseases, and therapies. Feb 2024. URL: https://doi.org/10.3390/ijms25042239, doi:10.3390/ijms25042239. This article has 49 citations.

5. (uittenbogaard2018novelinsightsinto pages 1-3): Martine Uittenbogaard, Christine A. Brantner, ZiShui Fang, Lee-Jun C. Wong, Andrea Gropman, and Anne Chiaramello. Novel insights into the functional metabolic impact of an apparent de novo m.8993t&gt;g variant in the mt-atp6 gene associated with maternally inherited form of leigh syndrome. Molecular Genetics and Metabolism, 124(1):71-81, May 2018. URL: https://doi.org/10.1016/j.ymgme.2018.03.011, doi:10.1016/j.ymgme.2018.03.011. This article has 32 citations and is from a peer-reviewed journal.

6. (ganetzky2019mt‐atp6mitochondrialdisease pages 3-4): Rebecca D. Ganetzky, Claudia Stendel, Elizabeth M. McCormick, Zarazuela Zolkipli-Cunningham, Amy C. Goldstein, Thomas Klopstock, and Marni J. Falk. Mt‐atp6 mitochondrial disease variants: phenotypic and biochemical features analysis in 218 published cases and cohort of 14 new cases. Human Mutation, 40:499-515, Mar 2019. URL: https://doi.org/10.1002/humu.23723, doi:10.1002/humu.23723. This article has 151 citations and is from a domain leading peer-reviewed journal.

7. (carli2025naturalhistoryof pages 5-7): Sara Carli, Anna Levarlet, Daria Diodato, Enrico Silvio Bertini, Diego Martinelli, Alessandro Malandrini, Diego Lopergolo, Gian Nicola Gallus, Rebecca D. Ganetzky, Chiara La Morgia, Valerio Carelli, Guido Primiano, Cristina Domínguez-González, Pablo Serrano-Lorenzo, Miguel A. Martín, Anna Ardissone, Costanza Lamperti, Valeria Nicoletta, Thomas Klopstock, Felix Distelmaier, Leopold Zeng, Boriana Büchner, Michelangelo Mancuso, Markus Schuelke, Alessandro Prigione, and Caterina Garone. Natural history of patients with mitochondrial atpase deficiency due to pathogenic variants of mt-atp6 and mt-atp8. Neurology, Apr 2025. URL: https://doi.org/10.1212/wnl.0000000000213462, doi:10.1212/wnl.0000000000213462. This article has 21 citations and is from a highest quality peer-reviewed journal.

8. (carli2025naturalhistoryof pages 1-2): Sara Carli, Anna Levarlet, Daria Diodato, Enrico Silvio Bertini, Diego Martinelli, Alessandro Malandrini, Diego Lopergolo, Gian Nicola Gallus, Rebecca D. Ganetzky, Chiara La Morgia, Valerio Carelli, Guido Primiano, Cristina Domínguez-González, Pablo Serrano-Lorenzo, Miguel A. Martín, Anna Ardissone, Costanza Lamperti, Valeria Nicoletta, Thomas Klopstock, Felix Distelmaier, Leopold Zeng, Boriana Büchner, Michelangelo Mancuso, Markus Schuelke, Alessandro Prigione, and Caterina Garone. Natural history of patients with mitochondrial atpase deficiency due to pathogenic variants of mt-atp6 and mt-atp8. Neurology, Apr 2025. URL: https://doi.org/10.1212/wnl.0000000000213462, doi:10.1212/wnl.0000000000213462. This article has 21 citations and is from a highest quality peer-reviewed journal.

9. (ganetzky2019mt‐atp6mitochondrialdisease pages 1-3): Rebecca D. Ganetzky, Claudia Stendel, Elizabeth M. McCormick, Zarazuela Zolkipli-Cunningham, Amy C. Goldstein, Thomas Klopstock, and Marni J. Falk. Mt‐atp6 mitochondrial disease variants: phenotypic and biochemical features analysis in 218 published cases and cohort of 14 new cases. Human Mutation, 40:499-515, Mar 2019. URL: https://doi.org/10.1002/humu.23723, doi:10.1002/humu.23723. This article has 151 citations and is from a domain leading peer-reviewed journal.

10. (peretz2021prospectivediagnosisof pages 6-8): Ryan H. Peretz, Nicholas Ah Mew, Hilary J. Vernon, and Rebecca D. Ganetzky. Prospective diagnosis of mt-atp6-related mitochondrial disease by newborn screening. Sep 2021. URL: https://doi.org/10.1016/j.ymgme.2021.06.007, doi:10.1016/j.ymgme.2021.06.007. This article has 25 citations and is from a peer-reviewed journal.

11. (peretz2021prospectivediagnosisof pages 1-3): Ryan H. Peretz, Nicholas Ah Mew, Hilary J. Vernon, and Rebecca D. Ganetzky. Prospective diagnosis of mt-atp6-related mitochondrial disease by newborn screening. Sep 2021. URL: https://doi.org/10.1016/j.ymgme.2021.06.007, doi:10.1016/j.ymgme.2021.06.007. This article has 25 citations and is from a peer-reviewed journal.

12. (tauchmannova2024variabilityofclinical pages 26-27): K. Tauchmannová, A. Pecinová, J. Houštěk, and T. Mrázek. Variability of clinical phenotypes caused by isolated defects of mitochondrial atp synthase. Physiological Research, pages S243-S278, Aug 2024. URL: https://doi.org/10.33549/physiolres.935407, doi:10.33549/physiolres.935407. This article has 17 citations and is from a peer-reviewed journal.

13. (dotto2024variantsinhuman pages 18-20): Valentina Del Dotto, Francesco Musiani, Alessandra Baracca, and Giancarlo Solaini. Variants in human atp synthase mitochondrial genes: biochemical dysfunctions, associated diseases, and therapies. Feb 2024. URL: https://doi.org/10.3390/ijms25042239, doi:10.3390/ijms25042239. This article has 49 citations.

14. (carli2025naturalhistoryof pages 2-3): Sara Carli, Anna Levarlet, Daria Diodato, Enrico Silvio Bertini, Diego Martinelli, Alessandro Malandrini, Diego Lopergolo, Gian Nicola Gallus, Rebecca D. Ganetzky, Chiara La Morgia, Valerio Carelli, Guido Primiano, Cristina Domínguez-González, Pablo Serrano-Lorenzo, Miguel A. Martín, Anna Ardissone, Costanza Lamperti, Valeria Nicoletta, Thomas Klopstock, Felix Distelmaier, Leopold Zeng, Boriana Büchner, Michelangelo Mancuso, Markus Schuelke, Alessandro Prigione, and Caterina Garone. Natural history of patients with mitochondrial atpase deficiency due to pathogenic variants of mt-atp6 and mt-atp8. Neurology, Apr 2025. URL: https://doi.org/10.1212/wnl.0000000000213462, doi:10.1212/wnl.0000000000213462. This article has 21 citations and is from a highest quality peer-reviewed journal.

15. (dotto2024variantsinhuman pages 20-22): Valentina Del Dotto, Francesco Musiani, Alessandra Baracca, and Giancarlo Solaini. Variants in human atp synthase mitochondrial genes: biochemical dysfunctions, associated diseases, and therapies. Feb 2024. URL: https://doi.org/10.3390/ijms25042239, doi:10.3390/ijms25042239. This article has 49 citations.

16. (dotto2024variantsinhuman pages 22-23): Valentina Del Dotto, Francesco Musiani, Alessandra Baracca, and Giancarlo Solaini. Variants in human atp synthase mitochondrial genes: biochemical dysfunctions, associated diseases, and therapies. Feb 2024. URL: https://doi.org/10.3390/ijms25042239, doi:10.3390/ijms25042239. This article has 49 citations.

17. (dotto2024variantsinhuman pages 31-32): Valentina Del Dotto, Francesco Musiani, Alessandra Baracca, and Giancarlo Solaini. Variants in human atp synthase mitochondrial genes: biochemical dysfunctions, associated diseases, and therapies. Feb 2024. URL: https://doi.org/10.3390/ijms25042239, doi:10.3390/ijms25042239. This article has 49 citations.

18. (dotto2024variantsinhuman pages 32-33): Valentina Del Dotto, Francesco Musiani, Alessandra Baracca, and Giancarlo Solaini. Variants in human atp synthase mitochondrial genes: biochemical dysfunctions, associated diseases, and therapies. Feb 2024. URL: https://doi.org/10.3390/ijms25042239, doi:10.3390/ijms25042239. This article has 49 citations.

19. (dautant2018atpsynthasediseases pages 1-2): Alain Dautant, Thomas Meier, Alexander Hahn, Déborah Tribouillard-Tanvier, Jean-Paul di Rago, and Roza Kucharczyk. Atp synthase diseases of mitochondrial genetic origin. Frontiers in Physiology, Apr 2018. URL: https://doi.org/10.3389/fphys.2018.00329, doi:10.3389/fphys.2018.00329. This article has 157 citations.

## Artifacts

- [Edison artifact artifact-00](MT-ATP6_MT-ATP8-Related_Infantile_Hypertrophic_Cardiomyopathy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.