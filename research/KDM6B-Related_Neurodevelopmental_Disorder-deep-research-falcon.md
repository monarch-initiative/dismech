---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-15T08:32:58.653301'
end_time: '2026-08-15T08:42:13.045682'
duration_seconds: 554.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: KDM6B-Related Neurodevelopmental Disorder
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: KDM6B-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KDM6B-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KDM6B-Related Neurodevelopmental Disorder** covering all of the
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
- **Disease Name:** KDM6B-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KDM6B-Related Neurodevelopmental Disorder** covering all of the
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


# KDM6B-Related Neurodevelopmental Disorder: Comprehensive Research Report

## Executive summary

KDM6B-related neurodevelopmental disorder (KDM6B-NDD), sometimes called **Stolerman syndrome**, is a rare Mendelian chromatinopathy caused predominantly by heterozygous loss-of-function or function-impairing variants in **KDM6B/JMJD3**, an H3K27me2/3 histone demethylase. The best current human dataset comprises 85 individuals carrying 71 likely pathogenic variants. Developmental abnormalities were found in essentially all, with intellectual disability (ID) in 63%, autism spectrum disorder (ASD) in 61%, other behavioral problems in 60%, hypotonia in 57%, and neonatal feeding difficulty or gastroesophageal reflux in 51%. Expression is highly variable; most ID is mild, recognizable facial gestalt is absent, and 11% inherited the variant from a mildly affected or apparently unaffected parent. (rots2024clinicalepigeneticsof pages 85-87, rots2024clinicalepigeneticsof pages 79-82)

Recent 2024 experimental work strengthens the biological model: Kdm6b is required for hippocampal neural-stem-cell maintenance, while brain mosaic knockout disrupts NMDA-receptor-mediated transmission and plasticity and produces cognitive, social, and repetitive-behavior phenotypes in mice. These findings are mechanistically important but do not yet establish a human biomarker or treatment. (brauer2024impactofkdm6b pages 9-10, gil2024chromatinregulatorkdm6b pages 1-5, gil2024chromatinregulatorkdm6b pages 11-14)

| Domain | Best-supported finding/statistic | Suggested ontology terms | Evidence type/strength |
|---|---|---|---|
| Identifiers / naming | OMIM names the condition **“Neurodevelopmental disorder with coarse facies and mild distal skeletal abnormalities” (OMIM #618505)**, but the larger 85-person cohort argues coarse facies/distal skeletal findings are **rare and not typical**; “**KDM6B-related neurodevelopmental disorder**” is the more accurate disease label. Initial disease-defining report described **12 unrelated patients** with de novo KDM6B variants. (stolerman2019geneticvariantsin pages 1-2, rots2024clinicalepigeneticsof pages 85-87) | OMIM: 618505; MONDO: not confirmed from available sources; NCIT: neurodevelopmental disorder; HPO: HP:0001263 Global developmental delay; HP:0001249 Intellectual disability | Human cohort data; strong for naming revision, moderate for formal identifier set |
| Genetics / inheritance | Disease is caused by **heterozygous pathogenic/likely pathogenic KDM6B variants**; in the expanded cohort **64/85 (75%) were de novo** and **9/85 (11%) inherited** from mildly affected or apparently unaffected parents, indicating **high but incomplete penetrance/variable expressivity**. KDM6B is constrained for LoF (**pLI=1, LOEUF=0.14; earlier gnomAD o/e 0.06, 90% CI 0.03–0.14**), supporting haploinsufficiency/functional loss. (rots2024clinicalepigeneticsof pages 79-82, rots2024clinicalepigeneticsof pages 85-87, stolerman2019geneticvariantsin pages 10-11) | HGNC: KDM6B; inheritance: autosomal dominant; SO: loss_of_function_variant, missense_variant, stop_gained, frameshift_variant | Human genetic cohort + population constraint; strong |
| Variant classes / protein regions | **71 different KDM6B variants** were considered likely pathogenic across **85 individuals**. Pathogenicity is strongest for variants disrupting the **JmjC catalytic region** or **Zn-containing domain**; some linker/surface missense changes were reclassified as **VUS** in functional assays. Truncating variants in the last/penultimate exons may **escape NMD** yet still cause loss of function by removing the Zn-containing domain. (rots2024clinicalepigeneticsof pages 79-82, rots2024clinicalepigeneticsof pages 85-87, stolerman2019geneticvariantsin pages 10-11) | SO: missense_variant, frameshift_variant, nonsense_variant; GO: GO:0032454 histone demethylase activity; protein region terms: JmjC domain, zinc-binding domain | Human cohort + Drosophila functional assay; moderate-strong |
| Core neurodevelopmental phenotype | In the 85-person pathogenic/likely pathogenic cohort, neurodevelopmental abnormalities were present in **all assessed individuals**; developmental delay was present in **all except two**. **ID 63%**, usually mild; **ASD 61%**; **other behavioral problems 60%**. (rots2024clinicalepigeneticsof pages 79-82) | HPO: HP:0001263, HP:0001249, HP:0000717 Autism, HP:0000708 Behavioral abnormality | Human cohort; strong |
| Neurologic features | **Hypotonia 57%**, **sleep disturbance 32%**, **movement disorders 24%** (gait abnormality, dystonia-like movements, spasticity, hypertonia, toe walking), **seizures 13%**. Psychotic disorder was reported in **4/20 (20%)** individuals aged ≥12 years. (rots2024clinicalepigeneticsof pages 79-82, rots2024clinicalepigeneticsof pages 85-87) | HPO: HP:0001252 Hypotonia; HP:0002360 Sleep disturbance; HP:0100022 Movement disorder; HP:0001250 Seizure; HP:0000709 Psychosis | Human cohort; strong for frequencies, moderate for age-related psychiatric risk |
| Growth / craniofacial / musculoskeletal | Postnatal overgrowth features occurred in **30%**; **macrocephaly 26%**, **tall stature 8%**, **increased weight 14%**, **increased birth weight 16% (10/63)**. Dysmorphism is usually **mild/variable with no recognizable gestalt**. Limb/skeletal findings: **broad fingers/hands or broad toes/feet 20%**, **spine curvature 13%**, **toe syndactyly 9%**, **short fingers/toes 9%**. (rots2024clinicalepigeneticsof pages 79-82, rots2024clinicalepigeneticsof pages 85-87) | HPO: HP:0000256 Macrocephaly; HP:0000098 Tall stature; HP:0001159 Syndactyly; HP:0001165 Brachydactyly; HP:0000928 Abnormality of the vertebral column | Human cohort; strong |
| GI / feeding / congenital anomalies | **Neonatal feeding difficulty or GERD 51%**, **constipation 18%**. Congenital anomalies: **heart defects 13%**, **genitourinary anomalies 10%**, **cleft lip/palate 4%**. (rots2024clinicalepigeneticsof pages 79-82) | HPO: HP:0011968 Feeding difficulties; HP:0002019 Gastroesophageal reflux; HP:0002019/HP:0001508 Constipation; HP:0001627 Abnormal heart morphology; HP:0000078 Abnormality of the genital system; HP:0000175 Cleft palate | Human cohort; strong |
| Sex distribution / modifiers | Cohort shows a **male bias (~75%)**; authors hypothesize a possible **female protective effect** and contribution from **other genetic/environmental modifiers**, but no definitive modifier genes are established. (rots2024clinicalepigeneticsof pages 85-87) | PATO: male-biased frequency; HPO: variable expressivity | Human cohort observation; moderate |
| Molecular mechanism | KDM6B/JMJD3 is an **H3K27me2/3 demethylase** that counteracts Polycomb repression to regulate developmental gene expression. Human disorder is best explained by **loss of function / reduced function**, not a clearly established dominant-negative mechanism. (stolerman2019geneticvariantsin pages 2-2, stolerman2019geneticvariantsin pages 10-11, swahari2019histonedemethylasesin pages 3-4) | GO: GO:0032454 histone demethylase activity; GO:0016575 histone deacetylation? not applicable; GO:0045664 regulation of neuron differentiation; GO:0006357 regulation of transcription by RNA polymerase II | Human genetics + mechanistic review; strong for upstream mechanism |
| Cellular / systems pathophysiology | Recent models show Kdm6b is required for **dentate gyrus neural stem-cell establishment and maintenance**; deletion causes **precocious neuronal differentiation**, depletion of NSCs, and transcriptomic disruption on **scRNA-seq**. In mosaic brain KO mice, Kdm6b loss causes **reduced excitatory synaptic transmission, impaired NMDAR-dependent LTP, altered NR2A/NR2B balance**, and autism-like/social/cognitive phenotypes. (gil2024chromatinregulatorkdm6b pages 1-5, gil2024chromatinregulatorkdm6b pages 11-14, brauer2024impactofkdm6b pages 9-10, brauer2024impactofkdm6b pages 1-2) | GO: neurogenesis, neuron differentiation, synaptic plasticity, NMDA receptor signaling; CL: neural stem cell, neuroblast, excitatory neuron; UBERON: hippocampus, dentate gyrus, cerebellum | Mouse in vivo + scRNA-seq/electrophysiology; moderate-strong |
| Anatomy most affected | Highest-confidence affected system is the **central nervous system**, especially **cortex/hippocampus/dentate gyrus** and likely broader neural circuits; secondary involvement includes **GI**, **cardiac**, **genitourinary**, and **musculoskeletal** systems. (rots2024clinicalepigeneticsof pages 79-82, gil2024chromatinregulatorkdm6b pages 1-5, brauer2024impactofkdm6b pages 9-10) | UBERON: brain, hippocampus, dentate gyrus, cerebellum, heart, gastrointestinal tract, urinary system; CL: neural stem cell, cerebellar granule neuron | Human phenotype + mouse mechanism; moderate-strong |
| Diagnostics | Current diagnosis is primarily **genomic**: **WES/WGS** or NDD/autism/ID panels including KDM6B; **CMA**, Fragile X testing, and metabolic testing were used in early workups; parental testing is important for de novo status. Disease is **unlikely to be recognized clinically alone** because dysmorphism is mild/variable. (stolerman2019geneticvariantsin pages 8-9, stolerman2019geneticvariantsin pages 6-7, stolerman2019geneticvariantsin pages 9-10, rots2024clinicalepigeneticsof pages 85-87) | NCIT: Whole Exome Sequencing, Chromosomal Microarray Analysis; HPO-based phenotyping; ACMG/AMP variant classification | Human clinical cohort; strong for sequencing-based diagnosis |
| Epigenomic diagnostics | A **validated KDM6B-specific DNA methylation episignature** was **not established in the available disease-specific sources**. Recent chromatinopathy literature supports episignatures as a general approach for variant interpretation, but this remains an evidence gap for KDM6B in the accessible dataset. (rots2024clinicalepigeneticsof pages 85-87, jaarsveld2023delineationofa pages 6-8) | EFO/OBI: DNA methylation profiling; epigenetic biomarker | Indirect/general chromatinopathy evidence; weak for KDM6B-specific use |
| Management / real-world care | No disease-modifying therapy is established. Reported care is **supportive and multidisciplinary**: **physical, occupational, and speech therapy**, special education, management of constipation/GERD/feeding problems, and treatment of spasticity in some cases (including **botulinum toxin** in one report). Awareness of adolescent/adult psychiatric risk may affect follow-up. (stolerman2019geneticvariantsin pages 8-9, stolerman2019geneticvariantsin pages 8-8, rots2024clinicalepigeneticsof pages 79-82, rots2024clinicalepigeneticsof pages 85-87) | NCIT: Physical Therapy, Occupational Therapy, Speech Therapy, Special Education, Botulinum Toxin Therapy | Human case/cohort care data; moderate |
| Trials / registries | No interventional disease-specific trials were identified. **Simons Searchlight (NCT01238250)** is a **recruiting observational registry** that explicitly includes **KDM6B**, collects longitudinal medical/behavioral/developmental data, and aims to improve care for rare genetic NDDs. (NCT01238250 chunk 1, NCT01238250 chunk 2) | NCIT: Observational Study; ClinicalTrials.gov: NCT01238250 | Registry evidence; strong for data collection, not treatment efficacy |
| Prognosis / epidemiology | Natural history remains incompletely defined. Available evidence supports a **lifelong neurodevelopmental disorder** with usually **mild ID when present**, variable ASD/behavioral burden, and possible later **psychotic disorders**. No robust prevalence, incidence, life-expectancy, or disease-specific mortality estimates were found. Early GeneDx ascertainment found **12/10,619 exomes (0.12%)** among tested DD/ID cases, which is **not population prevalence**. (stolerman2019geneticvariantsin pages 9-10, rots2024clinicalepigeneticsof pages 79-82, rots2024clinicalepigeneticsof pages 85-87) | HPO: chronic neurodevelopmental course; epidemiology terms unavailable | Limited cohort evidence; moderate for course, weak for prevalence/survival |
| Prevention / counseling | No primary prevention is known for the disorder itself. Best-supported prevention-related measures are **genetic counseling**, **recurrence-risk assessment based on de novo vs inherited status**, and consideration of **family testing/cascade testing** when a familial variant is found. (rots2024clinicalepigeneticsof pages 79-82, rots2024clinicalepigeneticsof pages 85-87) | NCIT: Genetic Counseling; prenatal/preimplantation testing terms if familial variant known | Inference from Mendelian inheritance pattern; moderate |
| Major evidence gaps | Key gaps: no confirmed population prevalence/incidence; no standardized diagnostic criteria beyond molecular diagnosis; no established **KDM6B episignature** in the accessible disease-specific literature; no disease-specific biomarkers; no interventional trials; sparse adult outcome, QoL, and survival data; no confirmed modifier genes or protective environmental factors. (rots2024clinicalepigeneticsof pages 85-87, rots2024clinicalepigeneticsof pages 79-82, stolerman2019geneticvariantsin pages 9-10, jaarsveld2023delineationofa pages 6-8) | Evidence gap / no ontology term needed | Cross-source synthesis; strong as a gap assessment |


*Table: This table summarizes the most clinically and mechanistically supported findings for KDM6B-related neurodevelopmental disorder, emphasizing quantified human cohort data and clearly marking areas where evidence is still lacking.*

## 1. Disease information

### Definition and identifiers

KDM6B-NDD is a congenital-onset, lifelong neurodevelopmental disorder characterized primarily by developmental delay, variable ID, ASD or other behavioral/psychiatric manifestations, and variably associated neurologic, feeding, growth, and congenital abnormalities. It belongs to the **Mendelian disorders of the epigenetic machinery/chromatinopathies**.

* **OMIM phenotype:** **618505**, *Neurodevelopmental disorder with coarse facies and mild distal skeletal abnormalities*.
* **Gene:** **KDM6B**, also known as **JMJD3**; gene OMIM **611577**.
* **Chromosomal location:** 17p13.1.
* **Synonyms:** KDM6B-related neurodevelopmental disorder; KDM6B-related NDD; Stolerman syndrome; neurodevelopmental disorder with coarse facies and mild distal skeletal abnormalities.
* **MONDO, Orphanet, MeSH, ICD-10/ICD-11:** a disease-specific identifier/code could not be verified in the retrieved authoritative literature. Until formally mapped, broader codes for genetic neurodevelopmental disorder, developmental delay, ID, or ASD should not be represented as disease-specific identifiers.

The OMIM title derives from the initial 12-person series. Investigators studying the expanded cohort caution that coarse facies and distal skeletal abnormalities are uncommon and that the title may mislead clinicians; **KDM6B-related neurodevelopmental disorder** is consequently the preferable descriptive name. (stolerman2019geneticvariantsin pages 1-2, rots2024clinicalepigeneticsof pages 85-87)

### Evidence provenance

The foundational report was an international, clinician-assembled series of 12 unrelated individuals identified largely by clinical whole-exome sequencing (WES), with phenotypes abstracted from records, photographs, and clinician correspondence. The expanded analysis comprised 85 molecularly selected individuals—73 newly evaluated and the original 12—with detailed data unavailable for 16 research-cohort participants. Thus, the principal evidence is **aggregated disease-level research based on individual clinical records**, not a population-based EHR study. (stolerman2019geneticvariantsin pages 2-2, rots2024clinicalepigeneticsof pages 79-82)

**Foundational abstract quotation:** “We have identified a number of de novo alterations in the KDM6B gene via whole exome sequencing (WES) in a cohort of 12 unrelated patients with developmental delay, intellectual disability, dysmorphic facial features, and other clinical findings.” Stolerman et al., *American Journal of Medical Genetics A*, July 2019, DOI: [10.1002/ajmg.a.61173](https://doi.org/10.1002/ajmg.a.61173). (stolerman2019geneticvariantsin pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The established cause is a **germline heterozygous pathogenic or likely pathogenic KDM6B variant**. Most variants arise de novo, but inherited disease occurs. The dominant mechanism is reduced KDM6B function—usually haploinsufficiency or functional loss from truncating or critical-domain missense variants—rather than infection, toxin exposure, or a demonstrated dominant-negative mechanism. In the 85-person cohort, 64/85 (75%) variants were confirmed de novo and nine were inherited. (rots2024clinicalepigeneticsof pages 85-87, rots2024clinicalepigeneticsof pages 79-82)

### Genetic risk factors

* Protein-truncating variants, including nonsense and frameshift alleles, are strongly implicated.
* Missense variants require domain-aware interpretation; variants affecting the JmjC catalytic region or core residues of the zinc-containing domain have the strongest functional support.
* Some late truncations escape nonsense-mediated decay but delete the critical zinc-containing domain and still cause functional loss.
* Population constraint supports dosage sensitivity: the expanded analysis reports pLI=1 and LOEUF=0.14; the earlier study reported loss-of-function observed/expected ratio 0.06 (90% CI 0.03–0.14). Missense variation overall is less constrained, making functional/domain evidence especially important. (rots2024clinicalepigeneticsof pages 85-87, stolerman2019geneticvariantsin pages 10-11)

Examples from the initial report include c.2684del, c.3085dup, c.3862_3865del, c.1085_1088del, c.3730G>T, and c.3992A>G (p.Asn1331Ser). These examples should not be treated as recurrent hotspots; the expanded cohort contained 71 different variants. (stolerman2019geneticvariantsin pages 6-7, rots2024clinicalepigeneticsof pages 79-82)

### Modifiers and environmental factors

No validated modifier gene, protective allele, environmental risk factor, infectious trigger, toxin, diet, or lifestyle factor has been established. The approximately 3:1 male bias prompted a hypothesis of a female protective effect, but this remains inferential. A severe individual carrying pathogenic variants in both **KDM6B** and **HNRNPU** illustrates how a second diagnosis may intensify phenotype, but HNRNPU is not an established general modifier. Authors propose that genetic background and environmental factors contribute to expressivity; no specific gene–environment interaction has been demonstrated. (rots2024clinicalepigeneticsof pages 85-87)

## 3. Phenotypic spectrum

The most reliable frequencies come from the expanded pathogenic/likely pathogenic cohort; denominators vary by available data. Severe ID was reported in only two individuals, one of whom also had an HNRNPU diagnosis. (rots2024clinicalepigeneticsof pages 79-82)

### Neurodevelopmental and behavioral phenotypes

* **Developmental delay:** 72/77, 94%; speech-language, motor, or global; generally evident in infancy or early childhood. Suggested HPO: **HP:0001263 Global developmental delay**, **HP:0000750 Delayed speech and language development**, **HP:0001270 Motor delay**.
* **Neurodevelopmental problems:** 66/74, 89% in the table’s age-qualified analysis.
* **Intellectual disability:** 40/64, 63%; usually mild and variable. HPO: **HP:0001249**.
* **Autism:** 46/76, 61%. HPO: **HP:0000717 Autism**.
* **Other behavioral problems:** 44/73, 60%, including attention and social/behavioral difficulties. HPO: **HP:0000708 Behavioral abnormality**, with ADHD/anxiety terms where clinically diagnosed.
* **Psychotic disorder:** 4/20, 20% among those aged ≥12 years. The denominator is small and enriched by ascertainment; this is a surveillance signal, not a population risk estimate. HPO: **HP:0000709 Psychosis**. (rots2024clinicalepigeneticsof pages 85-87, rots2024clinicalepigeneticsof pages 79-82)

### Neurologic phenotypes

* **Hypotonia:** 40/70, 57%; occasionally severe enough to prompt muscle biopsy or myopathy-panel testing. HPO: **HP:0001252**.
* **Sleep disturbance:** 21/66, 32%. HPO: **HP:0002360**.
* **Movement disorder:** 16/67, 24%; gait abnormalities, dystonia-like movement, spasticity, hypertonia, and toe walking. Two improved over time; one required botulinum toxin for spasticity. HPO: **HP:0100022**, **HP:0001257 Spasticity**, **HP:0002066 Gait abnormality**, **HP:0001332 Dystonia**.
* **Seizures:** 9/69, 13%. HPO: **HP:0001250**. EEG abnormalities have been described, but routine EEG is not supported in asymptomatic individuals. (stolerman2019geneticvariantsin pages 8-9, rots2024clinicalepigeneticsof pages 79-82)

### Growth, gastrointestinal, and congenital phenotypes

* Postnatal overgrowth: approximately 30%; macrocephaly 26%, increased weight 14%, tall stature 8%, and increased birth weight 10/63 (16%). Most had normal growth and none had short stature in the expanded cohort. Suggested HPO: **HP:0000256 Macrocephaly**, **HP:0000098 Tall stature**, **HP:0004324 Increased body weight**.
* Neonatal feeding difficulty or GERD: 33/65, 51%; severe cases required nasogastric feeding or neonatal intensive care. HPO: **HP:0011968 Feeding difficulties**, **HP:0002020 Gastroesophageal reflux**.
* Constipation: 11/61, 18%, sometimes chronic and a major care burden. HPO: **HP:0002019**.
* Congenital heart disease: 13%; genitourinary anomalies: 10%; cleft lip/palate: 4%. Suggested HPO: **HP:0001627 Abnormal heart morphology**, **HP:0000078 Genitourinary abnormality**, **HP:0000175 Cleft palate**, **HP:0410030 Cleft lip**.
* Musculoskeletal findings include broad hands/fingers or feet/toes (20%), spinal curvature (13%), toe syndactyly (9%), and short digits (9%). HPO: **HP:0001159 Syndactyly**, **HP:0001165 Brachydactyly**, **HP:0000928 Vertebral-column abnormality**. (rots2024clinicalepigeneticsof pages 79-82)

Dysmorphic features are usually mild and inconsistent—prominent forehead/bridge, broad mouth, large ears, round or coarse face, prognathism, and epicanthal folds were reported—but no diagnostic facial gestalt exists. (stolerman2019geneticvariantsin pages 9-10, rots2024clinicalepigeneticsof pages 85-87)

### Functional and quality-of-life effects

Speech, learning, adaptive function, social communication, feeding, mobility, sleep, and bowel management can materially affect daily life. Some individuals require special education and lifelong developmental services. Nevertheless, no disease-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or adaptive-function natural-history dataset was found; per-phenotype quality-of-life estimates are unavailable. (stolerman2019geneticvariantsin pages 8-9, stolerman2019geneticvariantsin pages 8-8, rots2024clinicalepigeneticsof pages 79-82)

## 4. Genetic and molecular information

### Gene and protein

KDM6B/JMJD3 encodes a nuclear chromatin regulator that removes di- and trimethyl groups from lysine 27 of histone H3. The gene has 22 exons in the transcript used in the original report (NM_001080424.1). Functionally important C-terminal regions include the **JmjC catalytic domain**, helical elements, and a zinc-binding motif required for cofactor interaction and protein stability. (stolerman2019geneticvariantsin pages 6-7, stolerman2019geneticvariantsin pages 2-2)

Suggested annotations include **GO:0032454 histone demethylase activity**, **GO:0071558 histone H3-K27 demethylation**, nuclear chromatin, and regulation of transcription. The iron/2-oxoglutarate-dependent JmjC reaction implicates iron(II) and 2-oxoglutarate as biochemical cofactors, but no disease-specific cofactor deficiency has been shown.

### Variant interpretation

The initial 2019 variants were conservatively reported as VUS because the gene–disease relationship was new. Subsequent recurrence, de novo enrichment, population constraint, and functional assays established the disorder. Current classification should apply ACMG/AMP criteria with careful attention to de novo status, loss-of-function mechanism, domain location, population frequency, phenotype, and functional data. (stolerman2019geneticvariantsin pages 1-2, rots2024clinicalepigeneticsof pages 85-87)

Functional analysis showed strong loss of function for p.Cys1575Ser, which directly disrupts a zinc-binding cysteine; p.Arg1566Ser and p.Glu1570Gln had moderate effects. Conversely, linker or surface variants with minimal functional effects remained VUS. This demonstrates that not every rare KDM6B missense variant is causal. (rots2024clinicalepigeneticsof pages 85-87)

Pathogenic alleles are expected to be ultra-rare or absent from population databases. Exact gnomAD allele frequencies must be checked by variant and transcript at interpretation time; the cohort sources do not provide a frequency for every allele. Disease-causing variants are usually constitutional germline variants. Somatic KDM6B changes in cancer are outside this disorder’s definition.

### Chromosomal abnormalities and epigenetic information

Deletions encompassing KDM6B have been reported, but at least seven described deletions also included neighboring genes, preventing attribution of the full phenotype solely to KDM6B. CMA remains appropriate when a copy-number disorder is suspected. (stolerman2019geneticvariantsin pages 10-11)

KDM6B directly regulates the repressive H3K27me2/3 chromatin state. A clinically validated, disease-specific peripheral-blood DNA-methylation episignature was **not established in the retrieved KDM6B literature**. Methylation profiling is promising across chromatinopathies but should not currently be presented as a validated KDM6B diagnostic test.

## 5. Environmental information

No causal environmental exposure, lifestyle behavior, occupational exposure, infectious agent, immune trigger, or nutritional deficiency is recognized. Smoking, alcohol, exercise, and diet have not been linked to penetrance or severity. Standard avoidance of known prenatal neurotoxins is good general health practice but is not KDM6B-specific prevention. The disorder is not infectious or transmissible.

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream:** germline reduction of KDM6B dosage or catalytic/structural function → abnormal persistence or targeting of repressive H3K27me2/3 and disruption of catalytic-independent protein interactions.

**Intermediate:** altered developmental transcription in neural progenitors and postmitotic neurons → premature neuronal differentiation and depletion of neural-stem-cell pools, impaired maturation of synaptic gene programs, and altered glutamatergic transmission.

**Downstream:** disturbed circuit formation and plasticity—particularly hippocampal/dentate-gyrus, cortical, and cerebellar programs → developmental delay, cognitive impairment, ASD/behavioral phenotypes, hypotonia/movement abnormalities, and seizures in a subset. The exact mapping from each cellular defect to each human feature remains incomplete. (brauer2024impactofkdm6b pages 9-10, gil2024chromatinregulatorkdm6b pages 1-5, gil2024chromatinregulatorkdm6b pages 11-14, swahari2019histonedemethylasesin pages 3-4)

### Neural differentiation and stem-cell maintenance

KDM6B removes H3K27me3 from bivalent chromatin and facilitates neural-lineage programs; evidence includes cooperation with SMAD3 during TGF-β-dependent differentiation and regulation at promoters and enhancers. Suggested GO terms: **neurogenesis**, **regulation of neuron differentiation**, **neural stem-cell maintenance**, and **chromatin organization**. Suggested CL terms: **CL:0000047 neural stem cell**, neural progenitor cell, neuroblast, excitatory neuron, and cerebellar granule neuron. (swahari2019histonedemethylasesin pages 3-4)

A February 2024 mouse preprint used conditional deletion, scRNA-seq, transcriptomics, and CUT&RUN. Embryonic deletion left adult dentate gyri essentially devoid of neural stem cells because of precocious differentiation. Acute adult deletion increased TBR2-positive intermediate progenitors by 28% and neuroblasts by 43%, followed by a 25% reduction in adult neural stem cells at 30 days. Only a subset of downregulated maintenance genes gained promoter H3K27me3, supporting additional catalytic-independent functions. Metabolic expression shifted from glycolytic toward oxidative programs, but no validated human metabolomic signature exists. (gil2024chromatinregulatorkdm6b pages 1-5, gil2024chromatinregulatorkdm6b pages 11-14)

**Direct abstract quotation:** “Conditional deletion of Kdm6b in embryonic DG precursors results in an adult hippocampus that is essentially devoid of NSCs, and hippocampal-dependent behaviors are defective.” Gil et al., bioRxiv, posted February 2024, DOI: [10.1101/2024.02.20.581302](https://doi.org/10.1101/2024.02.20.581302). This was a preprint in the retrieved source and should be weighted accordingly. (gil2024chromatinregulatorkdm6b pages 1-5)

### Synaptic function and plasticity

The September 2024 peer-reviewed mosaic knockout study found reduced excitatory postsynaptic-current frequency, impaired NMDA-receptor-mediated transmission and LTP, slower NMDA-current decay, and a shift from NR2A toward NR2B-containing receptors. Proposed downstream nodes include PSD95 and NMDAR localization/composition. Mice showed hyperactivity, repetitive behavior, social deficits, and cognitive impairment. Suggested GO terms: **chemical synaptic transmission**, **regulation of NMDA receptor activity**, **long-term potentiation**, **learning or memory**, and **synapse organization**. (brauer2024impactofkdm6b pages 9-10, brauer2024impactofkdm6b pages 1-2)

**Direct abstract quotation:** “KDM6B mosaic knockout display abnormalities in hippocampal excitatory synaptic transmission decreasing NMDA receptor mediated synaptic transmission and plasticity.” Brauer et al., *Scientific Reports*, September 2024, DOI: [10.1038/s41598-024-70728-5](https://doi.org/10.1038/s41598-024-70728-5). (brauer2024impactofkdm6b pages 1-2)

Earlier mouse/cell evidence shows that cerebellar Kdm6b loss impairs late expression of glutamate and GABA receptor subunits, while excitatory-neuron deletion dysregulates VGLUT1/2 and synaptic structure. KDM6B is strongly activity inducible and participates in BDNF transcription and neuronal survival. These mechanisms are plausible contributors, not clinical biomarkers. (brauer2024impactofkdm6b pages 1-2, swahari2019histonedemethylasesin pages 4-6, swahari2019histonedemethylasesin pages 7-9)

### Immune, metabolic, and tissue-damage mechanisms

KDM6B regulates inflammatory transcription in several contexts, but chronic inflammation, autoimmunity, immunodeficiency, oxidative injury, fibrosis, or a primary metabolic defect has not been demonstrated in KDM6B-NDD. No disease-specific proteomic, metabolomic, or lipidomic signature has been validated. No human single-cell or spatial-transcriptomic study specific to KDM6B-NDD was identified.

## 7. Anatomical structures affected

The **central nervous system** is primary. Human manifestations implicate distributed cortical and subcortical networks; mechanistic evidence is strongest for the **hippocampus**, especially the **dentate gyrus**, and for cerebellar granule-neuron maturation. Suggested UBERON terms: **UBERON:0000955 brain**, **UBERON:0002421 hippocampal formation**, **UBERON:0001885 dentate gyrus**, **UBERON:0002037 cerebellum**, and cerebral cortex. (brauer2024impactofkdm6b pages 9-10, gil2024chromatinregulatorkdm6b pages 1-5)

Secondary systems include gastrointestinal tract, heart, genitourinary tract, craniofacial structures, spine, hands, and feet. No consistent lateralization is reported. At the subcellular level, the principal compartment is the **nucleus/chromatin**, with downstream involvement of excitatory synapses and postsynaptic densities. Suggested GO cellular components: nucleus, chromatin, synapse, postsynaptic density, and glutamatergic synapse.

## 8. Temporal development and natural history

Onset is congenital or early pediatric and usually insidious: feeding difficulty, hypotonia, or delayed milestones commonly emerge in infancy, followed by speech, learning, ASD, and behavioral manifestations. The condition is chronic and lifelong, not relapsing-remitting. Most cognitive impairment is mild, but expressivity ranges from subtle learning problems to substantial disability. (rots2024clinicalepigeneticsof pages 85-87, rots2024clinicalepigeneticsof pages 79-82)

No formal stages exist. Some movement abnormalities may improve—two cohort members had resolution—whereas developmental and adaptive vulnerabilities generally persist. Psychosis may emerge in adolescence or adulthood; its observed 20% frequency among 20 participants aged ≥12 years requires replication. Critical intervention windows have not been experimentally defined, although standard neurodevelopmental practice favors prompt early therapy. (rots2024clinicalepigeneticsof pages 85-87, rots2024clinicalepigeneticsof pages 79-82)

## 9. Inheritance and population

Inheritance is **autosomal dominant**. De novo occurrence predominates, but 9/85 individuals inherited variants maternally (five) or paternally (four) from mildly affected or apparently unaffected parents. This demonstrates reduced penetrance or very subtle expression and mandates parental molecular testing rather than reliance on reported family history. Expressivity is markedly variable. Anticipation, founder variants, and a systematic role for consanguinity are not established. Germline mosaicism was not quantified, but it remains a residual recurrence possibility after an apparently de novo result. (rots2024clinicalepigeneticsof pages 85-87, rots2024clinicalepigeneticsof pages 79-82)

The approximately 75% male proportion may indicate ascertainment effects or female protection. No ethnic, geographic, or founder enrichment is established. A 2024 Pakistani report of a biallelic in-frame duplication is not sufficient to redefine the well-supported dominant disorder model.

Population prevalence and incidence are unknown. The initial GeneDx search identified 12 affected individuals among 10,619 DD/ID-indication exomes (0.12%); this is a diagnostic-cohort yield, not population prevalence. (stolerman2019geneticvariantsin pages 9-10)

## 10. Diagnostics

### Recommended approach

1. **Clinical assessment:** developmental, neurologic, behavioral/psychiatric, growth, feeding/GI, congenital anomaly, and three-generation family histories; standardized developmental/IQ and ASD evaluation where indicated.
2. **First-line genomic testing:** trio WES or WGS is preferred for unexplained syndromic NDD; alternatively use a comprehensive ID/ASD/developmental-delay panel containing KDM6B. Trio testing materially strengthens de novo evidence.
3. **Copy-number analysis:** CMA remains useful, particularly when WES does not reliably detect CNVs. Genome sequencing may unify SNV/indel and structural-variant detection where validated.
4. **Variant confirmation and segregation:** orthogonal confirmation according to laboratory policy and parental testing. Interpret against the clinically relevant transcript and current ClinVar/gnomAD evidence.
5. **Phenotype-driven tests:** MRI for focal neurologic signs, regression, abnormal head growth, or seizures; EEG for suspected seizures; swallow/feeding assessment, GI evaluation, echocardiography, renal imaging, ophthalmology, or orthopedic evaluation only when clinically indicated.

The original diagnostic workups used WES, CMA, Fragile-X analysis, neurodevelopmental panels, and metabolic screening. One patient was tested for **RAI1/Smith–Magenis syndrome**, illustrating phenotypic overlap. The broad and mild dysmorphism means molecular testing—not facial recognition—is decisive. (stolerman2019geneticvariantsin pages 9-10, stolerman2019geneticvariantsin pages 6-7, stolerman2019geneticvariantsin pages 8-9, rots2024clinicalepigeneticsof pages 85-87)

Karyotyping and FISH are not routine unless a rearrangement is suspected. Mitochondrial, repeat-expansion, biopsy, proteomic, metabolomic, or liquid-biopsy testing has no established KDM6B-specific role. RNA sequencing may eventually clarify splice or expression VUS, but no validated disease-specific assay was found. A negative methylation assay cannot currently exclude KDM6B-NDD.

### Differential diagnosis

The broad differential includes other chromatinopathies and syndromic NDDs, particularly KDM6A-related Kabuki syndrome, KDM2B-related NDD, CHD8-related NDD, SETD1A-related NDD, Kleefstra syndrome/EHMT1, Wiedemann–Steiner syndrome/KMT2A, Coffin–Siris/BAF-complex disorders, DNMT3A-related Tatton-Brown–Rahman syndrome, NSD1-related Sotos syndrome, and EZH2-related Weaver syndrome. RAI1-related Smith–Magenis syndrome, Fragile X syndrome, CNV disorders, and primary neuromuscular disease may be considered according to sleep/behavior, overgrowth, dysmorphism, hypotonia, or movement presentation. Broad sequencing is more efficient than serial phenotype-driven single-gene testing.

### Screening

KDM6B-NDD is not part of newborn screening. Population carrier screening is inappropriate for a predominantly de novo dominant condition. Cascade testing is appropriate when a familial pathogenic variant is identified. Prenatal or preimplantation testing is technically possible once the familial variant is known, after counseling regarding variable expressivity and reduced penetrance.

## 11. Outcome and prognosis

No disease-specific survival rate, mortality rate, or life-expectancy estimate exists. Available reports do not indicate a characteristic degenerative or fatal course, but adult ascertainment is limited. Prognosis is driven principally by cognitive/adaptive level, communication, ASD/behavioral or psychiatric burden, seizures, movement impairment, feeding/GI morbidity, and congenital anomalies. (rots2024clinicalepigeneticsof pages 85-87, rots2024clinicalepigeneticsof pages 79-82)

Most reported ID is mild, and some movement abnormalities improve, but full neurodevelopmental “recovery” should not be expected. Speech, occupational, educational, and behavioral interventions may improve function without correcting the molecular cause. No prognostic biomarker or reliable genotype–phenotype correlation has been identified. (stolerman2019geneticvariantsin pages 8-8, rots2024clinicalepigeneticsof pages 85-87)

## 12. Treatment and current applications

There is no approved disease-modifying, gene, RNA, cell, or targeted epigenetic therapy. Current real-world care is individualized and multidisciplinary:

* early developmental intervention; speech-language, occupational, and physical therapy; augmentative communication and special education as needed;
* evidence-based ASD, ADHD, anxiety, sleep, or psychosis care through developmental pediatrics/psychiatry;
* standard antiseizure treatment for epilepsy;
* feeding therapy, nutrition support, reflux treatment, and constipation management;
* PT/orthopedics/rehabilitation for hypotonia, gait, contracture, scoliosis, or spasticity; botulinum toxin helped one reported patient’s spasticity;
* routine management of cardiac, genitourinary, palatal, or other congenital anomalies. (stolerman2019geneticvariantsin pages 8-9, stolerman2019geneticvariantsin pages 8-8, rots2024clinicalepigeneticsof pages 85-87, rots2024clinicalepigeneticsof pages 79-82)

Suggested NCIT intervention concepts include **Speech Therapy**, **Occupational Therapy**, **Physical Therapy**, **Behavioral Therapy**, **Special Education**, **Anticonvulsant Therapy**, **Nutritional Support**, and **Botulinum Toxin Therapy**. No KDM6B-specific pharmacogenomic guidance or response-rate evidence exists.

Although epigenetic enzymes are pharmacologically tractable, inhibiting KDM6B would be mechanistically concerning in a loss-of-function disorder. Results from other chromatinopathies cannot be directly translated, and broad prenatal/postnatal chromatin manipulation may have cell- and developmental-stage-specific toxicity.

### Trials and registries

No interventional KDM6B-specific trial was identified. **Simons Searchlight, NCT01238250**, explicitly enrolls people with pathogenic/likely pathogenic KDM6B variants. It is a recruiting, prospective, family-based observational registry collecting annual medical, behavioral, learning, developmental, and biospecimen data; it is not a treatment trial. ClinicalTrials.gov: [NCT01238250](https://clinicaltrials.gov/study/NCT01238250). (NCT01238250 chunk 1, NCT01238250 chunk 2)

## 13. Prevention

Primary prevention through lifestyle, vaccination, or environmental modification is unavailable. Secondary/tertiary prevention consists of timely molecular diagnosis, early developmental intervention, seizure recognition, feeding and aspiration assessment when indicated, constipation treatment, orthopedic monitoring, and age-appropriate behavioral/psychiatric surveillance. (rots2024clinicalepigeneticsof pages 85-87, rots2024clinicalepigeneticsof pages 79-82)

Genetic counseling should explain dominant inheritance, the predominance of de novo variants, variable expression, and apparently unaffected transmitting parents. For an affected heterozygous individual, each pregnancy has a theoretical 50% transmission probability, but phenotype cannot be predicted reliably. For parents negative in blood after a de novo diagnosis, recurrence is low but not zero because of possible germline mosaicism. Prenatal diagnosis and PGT-M are options when the familial variant is known.

## 14. Other species and natural disease

No naturally occurring veterinary syndrome confidently equivalent to human KDM6B-NDD was identified, and there is no zoonotic potential or cross-species transmission. Orthologous **Kdm6b** is evolutionarily conserved in mouse, and functional conservation is also exploited in Drosophila assays. Species taxon suggestions are **Homo sapiens NCBI Taxon 9606**, **Mus musculus 10090**, **Drosophila melanogaster 7227**, and **Danio rerio 7955**. Exact ortholog NCBI Gene and breed-ontology identifiers should be retrieved from their live databases before knowledge-base ingestion.

## 15. Model organisms and advanced technologies

### Mouse models

* **Constitutive knockout:** complete loss is neonatal/embryonic lethal because of respiratory-network deficits, limiting its fidelity for viable heterozygous human disease.
* **Heterozygous models:** reproduce hyperactivity and social/cognitive abnormalities but may vary by sex and background.
* **Conditional neural-stem-cell deletion:** demonstrates premature differentiation, failure to establish/maintain dentate-gyrus stem cells, and hippocampal behavioral deficits. scRNA-seq, bulk transcriptomics, and CUT&RUN provide cell-state and chromatin evidence. (gil2024chromatinregulatorkdm6b pages 1-5, gil2024chromatinregulatorkdm6b pages 11-14)
* **Postnatal CRISPR mosaic brain knockout:** produces repetitive behavior, social and cognitive deficits, and NMDAR/LTP abnormalities. Limitations include broad, non-cell-specific mosaic targeting and incomplete knockout. (brauer2024impactofkdm6b pages 9-10, brauer2024impactofkdm6b pages 1-2)
* **Cerebellar granule-neuron conditional knockout:** impairs late maturation and synaptic receptor-gene programs while early neuronal markers are relatively preserved. (swahari2019histonedemethylasesin pages 4-6, swahari2019histonedemethylasesin pages 7-9)

### Drosophila and cellular systems

Drosophila gain-of-function assays have been useful for discriminating damaging zinc-domain variants from linker/surface VUS. Their limitation is that overexpression may not reproduce human heterozygous haploinsufficiency, and the assay may miss N-terminal interaction defects. Human patient-derived iPSC neurons or organoids would offer higher translational relevance, but no mature KDM6B-NDD iPSC/organoid platform was identified in the retrieved evidence. (rots2024clinicalepigeneticsof pages 85-87)

## 2023–2024 developments and expert interpretation

1. The expanded 85-person analysis replaced a narrow dysmorphology-centered picture with a genotype-first spectrum dominated by developmental delay, mild ID, ASD, behavioral problems, hypotonia, and feeding/GI concerns. It also established inherited disease and highlighted adolescent psychosis surveillance. (rots2024clinicalepigeneticsof pages 85-87, rots2024clinicalepigeneticsof pages 79-82)
2. The 2024 dentate-gyrus study connected KDM6B to neural-stem-cell maintenance using scRNA-seq and CUT&RUN and suggested both demethylase-dependent and independent functions. (gil2024chromatinregulatorkdm6b pages 1-5, gil2024chromatinregulatorkdm6b pages 11-14)
3. The 2024 mosaic knockout study provided peer-reviewed electrophysiologic evidence linking KDM6B loss to NMDAR composition, LTP, cognition, and ASD-like behaviors. (brauer2024impactofkdm6b pages 9-10, brauer2024impactofkdm6b pages 1-2)
4. Experts caution that domain location alone is insufficient for missense classification; functional evidence showed several presumed damaging linker variants had minimal effects and should remain VUS. (rots2024clinicalepigeneticsof pages 85-87)

## Evidence limitations and knowledge-base cautions

The disorder remains underascertained and recently defined. Frequencies are referral-cohort estimates with variable denominators, not population risks. Adult natural history, life expectancy, quantitative quality of life, penetrance, sex effects, and variant-specific prognosis are unresolved. No validated KDM6B blood episignature, fluid biomarker, human single-cell atlas, spatial transcriptomic dataset, disease-specific treatment trial, or proven protective factor was identified. Mouse behavioral findings should be annotated as model evidence rather than human clinical manifestations. Finally, the OMIM phenotype name should be retained as an identifier-linked synonym but not used to imply that coarse facies or distal skeletal abnormalities are obligatory.

References

1. (rots2024clinicalepigeneticsof pages 85-87): Dmitrijs Rots. Clinical epigenetics of mendelian neurodevelopmental disorders. ArXiv, Nov 2024. URL: https://doi.org/10.54195/9789493296831, doi:10.54195/9789493296831. This article has 0 citations.

2. (rots2024clinicalepigeneticsof pages 79-82): Dmitrijs Rots. Clinical epigenetics of mendelian neurodevelopmental disorders. ArXiv, Nov 2024. URL: https://doi.org/10.54195/9789493296831, doi:10.54195/9789493296831. This article has 0 citations.

3. (brauer2024impactofkdm6b pages 9-10): Bastian Brauer, Carlos Ancatén-González, Constanza Ahumada-Marchant, Rodrigo C. Meza, Nicolas Merino-Veliz, Gino Nardocci, Lorena Varela-Nallar, Gloria Arriagada, Andrés E. Chávez, and Fernando J. Bustos. Impact of kdm6b mosaic brain knockout on synaptic function and behavior. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70728-5, doi:10.1038/s41598-024-70728-5. This article has 9 citations and is from a peer-reviewed journal.

4. (gil2024chromatinregulatorkdm6b pages 1-5): Eugene Gil, Sung Jun Hong, David Wu, Dae Hwi Park, Ryan N. Delgado, Martina Malatesta, Sajad Hamid Ahanger, Karin Lin, Saul Villeda, and Daniel A. Lim. Chromatin regulator kdm6b is required for the establishment and maintenance of neural stem cells in mouse hippocampus. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.20.581302, doi:10.1101/2024.02.20.581302. This article has 4 citations.

5. (gil2024chromatinregulatorkdm6b pages 11-14): Eugene Gil, Sung Jun Hong, David Wu, Dae Hwi Park, Ryan N. Delgado, Martina Malatesta, Sajad Hamid Ahanger, Karin Lin, Saul Villeda, and Daniel A. Lim. Chromatin regulator kdm6b is required for the establishment and maintenance of neural stem cells in mouse hippocampus. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.20.581302, doi:10.1101/2024.02.20.581302. This article has 4 citations.

6. (stolerman2019geneticvariantsin pages 1-2): Elliot S. Stolerman, Elizabeth Francisco, Jennifer L. Stallworth, Julie R. Jones, Kristin G. Monaghan, Jennifer Keller‐Ramey, Richard Person, Ingrid M. Wentzensen, Kirsty McWalter, Boris Keren, Benedicte Heron, Caroline Nava, Delphine Heron, Katherine Kim, Barbara Burton, Fatima Al‐Musafri, Lauren O'Grady, Inderneel Sahai, Luis F. Escobar, Marije Meuwissen, Edwin Reyniers, Frank Kooy, Yves Lacassie, Meral Gunay‐Aygun, Krista Sondergaard Schatz, Ron Hochstenbach, Petra J.G. Zwijnenburg, Quinten Waisfisz, Marjon van Slegtenhorst, Grazia M.S. Mancini, and Raymond J. Louie. Genetic variants in the kdm6b gene are associated with neurodevelopmental delays and dysmorphic features. American Journal of Medical Genetics Part A, 179:1276-1286, Jul 2019. URL: https://doi.org/10.1002/ajmg.a.61173, doi:10.1002/ajmg.a.61173. This article has 59 citations.

7. (stolerman2019geneticvariantsin pages 10-11): Elliot S. Stolerman, Elizabeth Francisco, Jennifer L. Stallworth, Julie R. Jones, Kristin G. Monaghan, Jennifer Keller‐Ramey, Richard Person, Ingrid M. Wentzensen, Kirsty McWalter, Boris Keren, Benedicte Heron, Caroline Nava, Delphine Heron, Katherine Kim, Barbara Burton, Fatima Al‐Musafri, Lauren O'Grady, Inderneel Sahai, Luis F. Escobar, Marije Meuwissen, Edwin Reyniers, Frank Kooy, Yves Lacassie, Meral Gunay‐Aygun, Krista Sondergaard Schatz, Ron Hochstenbach, Petra J.G. Zwijnenburg, Quinten Waisfisz, Marjon van Slegtenhorst, Grazia M.S. Mancini, and Raymond J. Louie. Genetic variants in the kdm6b gene are associated with neurodevelopmental delays and dysmorphic features. American Journal of Medical Genetics Part A, 179:1276-1286, Jul 2019. URL: https://doi.org/10.1002/ajmg.a.61173, doi:10.1002/ajmg.a.61173. This article has 59 citations.

8. (stolerman2019geneticvariantsin pages 2-2): Elliot S. Stolerman, Elizabeth Francisco, Jennifer L. Stallworth, Julie R. Jones, Kristin G. Monaghan, Jennifer Keller‐Ramey, Richard Person, Ingrid M. Wentzensen, Kirsty McWalter, Boris Keren, Benedicte Heron, Caroline Nava, Delphine Heron, Katherine Kim, Barbara Burton, Fatima Al‐Musafri, Lauren O'Grady, Inderneel Sahai, Luis F. Escobar, Marije Meuwissen, Edwin Reyniers, Frank Kooy, Yves Lacassie, Meral Gunay‐Aygun, Krista Sondergaard Schatz, Ron Hochstenbach, Petra J.G. Zwijnenburg, Quinten Waisfisz, Marjon van Slegtenhorst, Grazia M.S. Mancini, and Raymond J. Louie. Genetic variants in the kdm6b gene are associated with neurodevelopmental delays and dysmorphic features. American Journal of Medical Genetics Part A, 179:1276-1286, Jul 2019. URL: https://doi.org/10.1002/ajmg.a.61173, doi:10.1002/ajmg.a.61173. This article has 59 citations.

9. (swahari2019histonedemethylasesin pages 3-4): Vijay Swahari and Anne E West. Histone demethylases in neuronal differentiation, plasticity, and disease. Current Opinion in Neurobiology, 59:9-15, Dec 2019. URL: https://doi.org/10.1016/j.conb.2019.02.009, doi:10.1016/j.conb.2019.02.009. This article has 45 citations and is from a peer-reviewed journal.

10. (brauer2024impactofkdm6b pages 1-2): Bastian Brauer, Carlos Ancatén-González, Constanza Ahumada-Marchant, Rodrigo C. Meza, Nicolas Merino-Veliz, Gino Nardocci, Lorena Varela-Nallar, Gloria Arriagada, Andrés E. Chávez, and Fernando J. Bustos. Impact of kdm6b mosaic brain knockout on synaptic function and behavior. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70728-5, doi:10.1038/s41598-024-70728-5. This article has 9 citations and is from a peer-reviewed journal.

11. (stolerman2019geneticvariantsin pages 8-9): Elliot S. Stolerman, Elizabeth Francisco, Jennifer L. Stallworth, Julie R. Jones, Kristin G. Monaghan, Jennifer Keller‐Ramey, Richard Person, Ingrid M. Wentzensen, Kirsty McWalter, Boris Keren, Benedicte Heron, Caroline Nava, Delphine Heron, Katherine Kim, Barbara Burton, Fatima Al‐Musafri, Lauren O'Grady, Inderneel Sahai, Luis F. Escobar, Marije Meuwissen, Edwin Reyniers, Frank Kooy, Yves Lacassie, Meral Gunay‐Aygun, Krista Sondergaard Schatz, Ron Hochstenbach, Petra J.G. Zwijnenburg, Quinten Waisfisz, Marjon van Slegtenhorst, Grazia M.S. Mancini, and Raymond J. Louie. Genetic variants in the kdm6b gene are associated with neurodevelopmental delays and dysmorphic features. American Journal of Medical Genetics Part A, 179:1276-1286, Jul 2019. URL: https://doi.org/10.1002/ajmg.a.61173, doi:10.1002/ajmg.a.61173. This article has 59 citations.

12. (stolerman2019geneticvariantsin pages 6-7): Elliot S. Stolerman, Elizabeth Francisco, Jennifer L. Stallworth, Julie R. Jones, Kristin G. Monaghan, Jennifer Keller‐Ramey, Richard Person, Ingrid M. Wentzensen, Kirsty McWalter, Boris Keren, Benedicte Heron, Caroline Nava, Delphine Heron, Katherine Kim, Barbara Burton, Fatima Al‐Musafri, Lauren O'Grady, Inderneel Sahai, Luis F. Escobar, Marije Meuwissen, Edwin Reyniers, Frank Kooy, Yves Lacassie, Meral Gunay‐Aygun, Krista Sondergaard Schatz, Ron Hochstenbach, Petra J.G. Zwijnenburg, Quinten Waisfisz, Marjon van Slegtenhorst, Grazia M.S. Mancini, and Raymond J. Louie. Genetic variants in the kdm6b gene are associated with neurodevelopmental delays and dysmorphic features. American Journal of Medical Genetics Part A, 179:1276-1286, Jul 2019. URL: https://doi.org/10.1002/ajmg.a.61173, doi:10.1002/ajmg.a.61173. This article has 59 citations.

13. (stolerman2019geneticvariantsin pages 9-10): Elliot S. Stolerman, Elizabeth Francisco, Jennifer L. Stallworth, Julie R. Jones, Kristin G. Monaghan, Jennifer Keller‐Ramey, Richard Person, Ingrid M. Wentzensen, Kirsty McWalter, Boris Keren, Benedicte Heron, Caroline Nava, Delphine Heron, Katherine Kim, Barbara Burton, Fatima Al‐Musafri, Lauren O'Grady, Inderneel Sahai, Luis F. Escobar, Marije Meuwissen, Edwin Reyniers, Frank Kooy, Yves Lacassie, Meral Gunay‐Aygun, Krista Sondergaard Schatz, Ron Hochstenbach, Petra J.G. Zwijnenburg, Quinten Waisfisz, Marjon van Slegtenhorst, Grazia M.S. Mancini, and Raymond J. Louie. Genetic variants in the kdm6b gene are associated with neurodevelopmental delays and dysmorphic features. American Journal of Medical Genetics Part A, 179:1276-1286, Jul 2019. URL: https://doi.org/10.1002/ajmg.a.61173, doi:10.1002/ajmg.a.61173. This article has 59 citations.

14. (jaarsveld2023delineationofa pages 6-8): Richard H. van Jaarsveld, Jack Reilly, Marie-Claire Cornips, Michael A. Hadders, Emanuele Agolini, Priyanka Ahimaz, Kwame Anyane-Yeboa, Severine Audebert Bellanger, Ellen van Binsbergen, Marie-Jose van den Boogaard, Elise Brischoux-Boucher, Raymond C. Caylor, Andrea Ciolfi, Ton A.J. van Essen, Paolo Fontana, Saskia Hopman, Maria Iascone, Margaret M. Javier, Erik-Jan Kamsteeg, Jennifer Kerkhof, Jun Kido, Hyung-Goo Kim, Tjitske Kleefstra, Fortunato Lonardo, Abbe Lai, Dorit Lev, Michael A. Levy, M.E. Suzanne Lewis, Angie Lichty, Marcel M.A.M. Mannens, Naomichi Matsumoto, Idit Maya, Haley McConkey, Andre Megarbane, Vincent Michaud, Evelina Miele, Marcello Niceta, Antonio Novelli, Roberta Onesimo, Rolph Pfundt, Bernt Popp, Eloise Prijoles, Raissa Relator, Sylvia Redon, Dmitrijs Rots, Karen Rouault, Ken Saida, Jolanda Schieving, Marco Tartaglia, Romano Tenconi, Kevin Uguen, Nienke Verbeek, Christopher A. Walsh, Keren Yosovich, Christopher J. Yuskaitis, Giuseppe Zampino, Bekim Sadikovic, Mariëlle Alders, and Renske Oegema. Delineation of a kdm2b-related neurodevelopmental disorder and its associated dna methylation signature. Genetics in Medicine, 25:49-62, Jan 2023. URL: https://doi.org/10.1016/j.gim.2022.09.006, doi:10.1016/j.gim.2022.09.006. This article has 40 citations and is from a highest quality peer-reviewed journal.

15. (stolerman2019geneticvariantsin pages 8-8): Elliot S. Stolerman, Elizabeth Francisco, Jennifer L. Stallworth, Julie R. Jones, Kristin G. Monaghan, Jennifer Keller‐Ramey, Richard Person, Ingrid M. Wentzensen, Kirsty McWalter, Boris Keren, Benedicte Heron, Caroline Nava, Delphine Heron, Katherine Kim, Barbara Burton, Fatima Al‐Musafri, Lauren O'Grady, Inderneel Sahai, Luis F. Escobar, Marije Meuwissen, Edwin Reyniers, Frank Kooy, Yves Lacassie, Meral Gunay‐Aygun, Krista Sondergaard Schatz, Ron Hochstenbach, Petra J.G. Zwijnenburg, Quinten Waisfisz, Marjon van Slegtenhorst, Grazia M.S. Mancini, and Raymond J. Louie. Genetic variants in the kdm6b gene are associated with neurodevelopmental delays and dysmorphic features. American Journal of Medical Genetics Part A, 179:1276-1286, Jul 2019. URL: https://doi.org/10.1002/ajmg.a.61173, doi:10.1002/ajmg.a.61173. This article has 59 citations.

16. (NCT01238250 chunk 1):  Online Study of People Who Have Genetic Changes and Features of Autism: Simons Searchlight. Simons Searchlight. 2010. ClinicalTrials.gov Identifier: NCT01238250

17. (NCT01238250 chunk 2):  Online Study of People Who Have Genetic Changes and Features of Autism: Simons Searchlight. Simons Searchlight. 2010. ClinicalTrials.gov Identifier: NCT01238250

18. (swahari2019histonedemethylasesin pages 4-6): Vijay Swahari and Anne E West. Histone demethylases in neuronal differentiation, plasticity, and disease. Current Opinion in Neurobiology, 59:9-15, Dec 2019. URL: https://doi.org/10.1016/j.conb.2019.02.009, doi:10.1016/j.conb.2019.02.009. This article has 45 citations and is from a peer-reviewed journal.

19. (swahari2019histonedemethylasesin pages 7-9): Vijay Swahari and Anne E West. Histone demethylases in neuronal differentiation, plasticity, and disease. Current Opinion in Neurobiology, 59:9-15, Dec 2019. URL: https://doi.org/10.1016/j.conb.2019.02.009, doi:10.1016/j.conb.2019.02.009. This article has 45 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](KDM6B-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.