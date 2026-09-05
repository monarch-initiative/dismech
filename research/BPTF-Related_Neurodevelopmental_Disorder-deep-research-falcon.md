---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-15T08:33:10.418419'
end_time: '2026-08-15T08:40:47.422885'
duration_seconds: 457.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: BPTF-Related Neurodevelopmental Disorder
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: BPTF-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BPTF-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **BPTF-Related Neurodevelopmental Disorder** covering all of the
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
- **Disease Name:** BPTF-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **BPTF-Related Neurodevelopmental Disorder** covering all of the
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


# BPTF-Related Neurodevelopmental Disorder: Comprehensive Disease-Characteristics Report

## Executive summary and evidence limits

BPTF-related neurodevelopmental disorder is a rare Mendelian chromatin-remodeling disorder, conventionally named **neurodevelopmental disorder with dysmorphic facies and distal limb anomalies (NEDDFL)**. It results primarily from heterozygous loss-of-function variants in **BPTF** and is best understood as an autosomal-dominant haploinsufficiency disorder. Developmental/intellectual disability, speech-language delay, postnatal microcephaly, and recognizable but variable dysmorphism form the core phenotype; motor delay, hypotonia, growth impairment, seizures, mild brain abnormalities, ophthalmologic findings, scoliosis, and distal-limb anomalies broaden the spectrum. The evidence base remains small: the landmark 2017 study described ten unrelated individuals, and the major 2021 expansion reported approximately 25–26 affected individuals with 20 distinct variants. Consequently, frequencies below are cohort proportions—not population estimates—and are vulnerable to referral and ascertainment bias. (glinton2021phenotypicexpansionof pages 1-3, stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 3-4)

Recent disease-specific literature is sparse. Important 2023 and 2024 reports concern growth-hormone use and epilepsy, respectively, but their full text was unavailable in the retrieved corpus; they are therefore flagged without extrapolating outcomes. No disease-specific interventional trial was identified. The strongest mechanistic development is the 2022 forebrain-specific mouse model and its RNA-sequencing analysis. (zapata2022generationofa pages 1-2)

## 1. Disease information

### Definition and nomenclature

**Preferred name:** BPTF-related neurodevelopmental disorder.  
**Established alternative name:** neurodevelopmental disorder with dysmorphic facies and distal limb anomalies.  
**Abbreviation:** NEDDFL.  
**Category:** Mendelian, syndromic neurodevelopmental disorder/chromatinopathy.

The 2021 abstract defines NEDDFL as being “defined primarily by developmental delay/intellectual disability, speech delay, postnatal microcephaly, and dysmorphic features” and resulting from heterozygous variants in dosage-sensitive **BPTF**. (glinton2021phenotypicexpansionof pages 1-3)

### Identifiers

- **OMIM phenotype:** **617755**, NEDDFL.
- **Gene/locus:** **BPTF**, chromosome **17q24.2**.
- **MONDO:** a disease-specific MONDO accession could not be verified from the retrieved primary literature; do not assign one without direct MONDO lookup.
- **Orphanet:** no disease-specific Orpha code was verified.
- **ICD-10/ICD-11 and MeSH:** no specific code/descriptor was identified. Coding generally requires broader categories for developmental/intellectual disability, microcephaly, epilepsy, or congenital malformations.

The source data are **aggregated disease-level data from published case series and experimental studies**, not an EHR-derived natural-history cohort. Individual-patient observations underlie the aggregate proportions. (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 3-4)

## 2. Etiology

### Causal factor

The primary cause is a **heterozygous germline pathogenic variant or deletion affecting BPTF**. The leading mechanism is reduced dosage—**haploinsufficiency**—rather than infection, toxin exposure, autoimmunity, or a metabolic enzyme defect. The 2017 cohort contained eight loss-of-function and two missense variants; the expanded cohort was dominated by frameshift, nonsense, splice, and exon-level loss variants. (glinton2021phenotypicexpansionof pages 3-4, stankiewicz2017haploinsufficiencyofthe pages 1-2)

### Genetic risk

A pathogenic BPTF allele is itself the principal risk factor. Most initially reported variants were de novo, but the 2021 study documented four inherited changes, including transmission from non-mosaic affected parents, demonstrating vertical autosomal-dominant transmission and variable expressivity. (glinton2021phenotypicexpansionof pages 3-4)

No validated modifier gene, susceptibility locus, protective allele, founder mutation, ancestry enrichment, or carrier-frequency estimate is established. Missense and some inherited variants have been associated with milder presentations, but this is not yet a validated genotype–phenotype rule. (glinton2021phenotypicexpansionof pages 12-13, glinton2021phenotypicexpansionof pages 3-4)

### Environmental and protective factors

No causal environmental, occupational, lifestyle, dietary, or infectious exposure has been demonstrated. No genetic or environmental protective factor has been reported. There is likewise no disease-specific gene–environment interaction literature. These are evidence gaps, not evidence that environmental influences can never affect clinical functioning.

## 3. Phenotypes

The most reproducible phenotype data are summarized below. Differences between quoted frequencies reflect different denominators, missing data, and whether the calculation concerned the novel cohort or all available individuals.

### Neurodevelopmental and neurologic features

- **Developmental delay/intellectual disability:** 10/10 in the 2017 cohort and approximately 88% in the 2021 expanded cohort. Severity is variable; onset is infancy/childhood and impairment is generally chronic. Suggested terms: **HP:0001263 Global developmental delay**, **HP:0001249 Intellectual disability**. (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 3-4)
- **Speech-language delay:** 10/10 in 2017 and approximately 85% in 2021. This is among the most consistent, functionally important manifestations. Suggested term: **HP:0000750 Delayed speech and language development**. (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 3-4)
- **Motor delay:** approximately 69% in the expanded cohort. Suggested term: **HP:0001270 Motor delay**. (glinton2021phenotypicexpansionof pages 3-4)
- **Hypotonia:** history in approximately 38%. Suggested term: **HP:0001252 Hypotonia**. (glinton2021phenotypicexpansionof pages 4-5)
- **Microcephaly:** postnatal microcephaly occurred in 7/9 in 2017. The expanded-study extractions report 42% in one denominator and 60% at assessment in another, while 40% had microcephaly at birth. The safest conclusion is that microcephaly is common but neither universal nor always strictly postnatal. Suggested terms: **HP:0000252 Microcephaly** and, only where serial measurements document it, **HP:0000253 Progressive microcephaly**. (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 4-5)
- **Seizures/EEG abnormalities:** six expanded-cohort participants had a seizure history requiring treatment; two additional individuals had electrographic abnormalities without reported clinical seizures. Suggested terms: **HP:0001250 Seizure**, **HP:0010843 Abnormality of the EEG**. (glinton2021phenotypicexpansionof pages 4-5)
- **Brain MRI:** among 13 imaged individuals, 8 MRIs were normal and 5 showed mild structural abnormalities. Thus, a normal MRI does not exclude the disorder. Suggested term: **HP:0410263 Abnormal brain MRI** when applicable. (glinton2021phenotypicexpansionof pages 4-5)

### Growth, craniofacial, skeletal, and ocular features

- **Short stature:** approximately 25%; **decreased weight/poor weight gain:** approximately 53%. Suggested terms: **HP:0004322 Short stature**, **HP:0004325 Decreased body weight/Poor weight gain**, with exact HPO chosen to match the measured phenotype. (glinton2021phenotypicexpansionof pages 4-5)
- **Dysmorphism:** 9/10 in 2017; 77% in one 2021 aggregate, while all 20 individuals with detailed available dysmorphology data had mild dysmorphism. Recurrent descriptions include a prominent nasal ridge, bulbous nasal tip, and pointed chin. Suggested umbrella term: **HP:0001999 Facial dysmorphism**, supplemented by feature-specific terms. (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 4-5, glinton2021phenotypicexpansionof pages 9-10)
- **Distal-limb/skeletal abnormalities:** cutaneous syndactyly, sandal gap, limb-length discrepancy, delayed bone age, and scoliosis occur variably. Suggested terms include **HP:0001159 Syndactyly** and **HP:0002650 Scoliosis**. (glinton2021phenotypicexpansionof pages 9-10, glinton2021phenotypicexpansionof pages 1-3)
- **Ophthalmologic complications:** reported as an expanded component of the phenotype, but precise frequencies and diagnoses were unavailable in the extracted evidence. Use **HP:0000478 Abnormality of the eye** only as a parent term pending patient-specific coding. (glinton2021phenotypicexpansionof pages 1-3)

### Behavioral, laboratory, and quality-of-life data

No consistent disease-specific psychiatric or behavioral profile, biochemical laboratory signature, validated patient-reported outcome, EQ-5D/SF-36 dataset, or formal quality-of-life study was identified. Nevertheless, cognitive, speech, motor, seizure, and visual impairments predict substantial effects on communication, education, independence, and caregiver burden. That functional interpretation is clinically reasonable but has not been quantified specifically for NEDDFL.

## 4. Genetic and molecular information

### Gene and variant spectrum

**BPTF** encodes bromodomain PHD finger transcription factor, the largest subunit of the nucleosome-remodeling factor (**NURF**) complex. In 2017, ten unrelated individuals carried eight loss-of-function and two missense variants; eight variants were confirmed de novo and two had unresolved parental origin. (stankiewicz2017haploinsufficiencyofthe pages 1-2)

The expanded study reported 20 distinct variants: **9 frameshift, 4 nonsense, 3 splice, 2 in-frame deletion, 1 missense, and 1 single-exon deletion**. Reported ACMG classifications were 11 pathogenic, 7 likely pathogenic, and 2 VUS. Four causative changes were inherited and fourteen were de novo in the available summary. Appropriate Sequence Ontology classes include `frameshift_variant`, `stop_gained`, `splice_donor_variant`, `splice_acceptor_variant`, `inframe_deletion`, `missense_variant`, and `exon_loss_variant`. (glinton2021phenotypicexpansionof pages 3-4)

Variants are germline in the constitutional disorder. Somatic BPTF alterations studied in cancer should not be conflated with NEDDFL. Population frequencies were not available in the retrieved evidence; pathogenic loss-of-function variants are expected to be very rare, but every candidate requires direct gnomAD/ClinVar evaluation using its exact HGVS expression.

### Functional consequence and epigenetics

The best-supported consequence is **loss of function and haploinsufficiency**. BPTF recognizes **H3K4me3** through its PHD finger and **H4K16ac** through its bromodomain, helping recruit/position the NURF ATP-dependent remodeling machinery at chromatin. The disorder is therefore an epigenetic chromatin-remodeling disease, although no validated diagnostic DNA-methylation episignature was identified. (glinton2021phenotypicexpansionof pages 1-3)

No dominant-negative or gain-of-function disease mechanism, modifier gene, or reproducible human methylomic signature has been established. Large deletions involving 17q24.2 may produce broader contiguous-gene phenotypes and require CNV interpretation rather than automatic attribution solely to BPTF.

## 5. Environmental information

No toxin, radiation, pollution, occupational exposure, smoking, diet, alcohol, exercise pattern, or infectious agent is known to cause or trigger this Mendelian disorder. Lifestyle measures remain relevant to general health and management of secondary complications but are not primary prevention for a pathogenic germline BPTF variant. There is no zoonotic or transmissible component.

## 6. Mechanism and pathophysiology

### Causal chain

The most defensible causal model is:

1. **Upstream genetic lesion:** heterozygous BPTF loss-of-function/deletion lowers functional BPTF dosage.
2. **Chromatin-level defect:** impaired NURF targeting/remodeling alters nucleosome positioning and transcriptional accessibility at developmentally regulated loci.
3. **Neural-progenitor consequences:** altered fate-determining transcription factors, prolonged progenitor cell cycle, and increased apoptosis reduce neuronal output.
4. **Corticogenesis defect:** impaired neuronal maturation and specification, reduced deep-layer neurons, and disrupted cortical lamination produce cortical hypoplasia.
5. **Clinical manifestations:** impaired cortical growth and circuit development plausibly generate microcephaly, developmental/intellectual disability, speech delay, motor impairment, and seizure susceptibility. (glinton2021phenotypicexpansionof pages 1-3, zapata2022generationofa pages 1-2)

In the 2022 mouse study, forebrain-specific Bptf loss produced “severe cortical hypoplasia”; prolonged progenitor cycling and high cell death reduced neuronal output, while lamination and acquisition of neuronal identities such as CTIP2-positive fates were impaired. RNA-seq showed dysregulation of fate-determining transcription factors and pathways involving neural development, apoptotic signaling, and amino-acid biosynthesis; dysregulated genes were enriched for MYC-binding sites, consistent with BPTF–MYC transcriptional cooperation. (zapata2022generationofa pages 1-2)

### Suggested functional ontology

- **GO:0006338** chromatin remodeling
- **GO:0042393** histone binding
- **GO:0006357** regulation of transcription by RNA polymerase II
- **GO:0022008** neurogenesis
- **GO:0007399** nervous system development
- **GO:0006915** apoptotic process
- **GO:0051301** cell division
- **GO:0008652** cellular amino-acid biosynthetic process
- **GO:0005634** nucleus
- **GO:0000785** chromatin

Suggested cell annotations are neural progenitor cell, radial glial/neural stem cell, cortical projection neuron, deep-layer cortical neuron, and generic neuron (**CL:0000540**); subtype accessions should be checked against the current Cell Ontology release.

### Molecular profiling and advanced technologies

Disease-relevant molecular profiling currently consists principally of **mouse forebrain bulk RNA-seq**. No robust human patient-brain transcriptome, proteome, metabolome, lipidome, single-cell atlas, spatial-transcriptomic dataset, organoid study, or clinical multi-omics signature was identified. The 2021 clinical authors noted the absence of a well-validated functional assay and suggested RNA-seq or proteomics might help resolve difficult variants, particularly missense variants; this remains investigational rather than standard diagnosis. (glinton2021phenotypicexpansionof pages 12-13)

There is no evidence that immune dysregulation, chronic inflammation, ischemia, fibrosis, mitochondrial failure, or a discrete metabolic block is a primary mechanism. Altered amino-acid-biosynthesis pathways in knockout mouse RNA-seq are downstream expression findings, not proof of a treatable human metabolic deficiency. (zapata2022generationofa pages 1-2)

## 7. Anatomical structures affected

The principal organ system is the **central nervous system**, especially the developing forebrain/cerebral cortex. Suggested anatomy terms include **UBERON:0000955 brain**, **UBERON:0001890 cerebral cortex**, and a current UBERON term for telencephalon/forebrain. Human imaging can be normal or show mild abnormalities, whereas complete forebrain-specific knockout in mice produces marked cortical hypoplasia. (zapata2022generationofa pages 1-2, glinton2021phenotypicexpansionof pages 4-5)

Secondary systems include craniofacial structures, distal limbs/skeleton, eyes, and general somatic growth. The relevant tissue is nervous tissue; implicated cells are neural progenitors and differentiating/mature cortical neurons. The main subcellular compartment is nuclear chromatin. Findings are not described as unilateral or lateralized.

## 8. Temporal development

The disorder is developmental, with congenital or early-childhood onset. Growth restriction or microcephaly may be present at birth, whereas some individuals develop postnatal microcephaly. Delayed milestones and language become evident in infancy or early childhood. (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 4-5)

The course is chronic and lifelong rather than episodic or relapsing-remitting. Published ages extended from 23 months to 55 years in the expanded cohort, demonstrating adult survival. There is no validated staging system, progression rate, remission pattern, or defined end stage. Early childhood is likely the most important intervention window for speech, motor, educational, visual, and seizure services, but no study has quantified a critical therapeutic period. (glinton2021phenotypicexpansionof pages 3-4)

## 9. Inheritance and population

Inheritance is **autosomal dominant**. Most pathogenic variants arise de novo, although affected-parent transmission is established. When a parent carries the variant, the theoretical transmission probability is 50% per pregnancy; actual phenotype severity cannot be predicted reliably because expressivity is variable. For an apparently de novo variant, recurrence risk is low but not zero because parental germline mosaicism cannot be excluded by routine blood testing. (glinton2021phenotypicexpansionof pages 3-4)

Penetrance has not been quantified. Anticipation, founder effects, consanguinity effects, population-specific variants, and carrier frequency are not established. Both sexes are affected; one summary reported 14 males and 11 females, with no evidence for sex-linked inheritance. The published sample spans childhood through middle adulthood. (glinton2021phenotypicexpansionof pages 3-4)

No prevalence, incidence, geographic clustering, ancestry excess, or registry-derived epidemiologic estimate is available. It should be represented as an ultra-rare disorder of unknown prevalence rather than assigning a numerical rate.

## 10. Diagnostics

### Recommended genomic approach

There are no formal NEDDFL diagnostic criteria. Diagnosis requires a compatible phenotype plus molecular confirmation.

1. **First-line broad testing:** trio exome sequencing or genome sequencing for unexplained syndromic developmental delay/intellectual disability, ideally with copy-number calling.
2. **CNV testing:** chromosomal microarray remains useful for exon/gene or larger 17q24.2 deletions and was used in foundational ascertainment. Genome sequencing may combine sequence and structural-variant detection.
3. **Panel testing:** a neurodevelopmental disorder/intellectual-disability or chromatinopathy panel should include BPTF and provide validated deletion/duplication analysis.
4. **Single-gene testing:** most appropriate when the phenotype is strongly suggestive or for familial segregation, prenatal diagnosis, and cascade testing.
5. **Variant interpretation:** apply ACMG/AMP criteria, parental testing, phenotype match, population frequency, predicted loss of function, transcript relevance, and CNV boundaries. A BPTF missense VUS alone does not establish diagnosis. (glinton2021phenotypicexpansionof pages 12-13, stankiewicz2017haploinsufficiencyofthe pages 1-2)

Karyotyping and FISH have low sensitivity for small sequence variants and are reserved for suspected large rearrangements or confirmation. Mitochondrial DNA and repeat-expansion testing are not disease-specific tests. RNA sequencing may help establish splice effects; proteomics and epigenomics remain investigational. (glinton2021phenotypicexpansionof pages 12-13)

### Clinical evaluation after diagnosis

Recommended baseline assessment, extrapolated from the observed spectrum, includes detailed developmental/neuropsychological and speech-language evaluation; serial height, weight, and head circumference; neurologic examination; EEG for suspected seizures; brain MRI when neurologically indicated; ophthalmology; hearing assessment; musculoskeletal examination for scoliosis and limb anomalies; and review of feeding/nutrition. These are pragmatic surveillance recommendations, not evidence-based NEDDFL guidelines.

There is no blood, urine, enzyme, biopsy, metabolite, protein, or circulating biomarker diagnostic for the syndrome.

### Differential diagnosis

Consider other chromatin-remodeling/chromatin-reader disorders, syndromic intellectual disability with microcephaly, copy-number syndromes involving 17q24, and growth disorders. Phenotypic overlap can include Silver–Russell syndrome: a cited adult with BPTF disruption was initially given that diagnosis. Distinction depends on genomic testing rather than facial gestalt alone. (glinton2021phenotypicexpansionof pages 13-13)

No newborn population screening or general-population carrier screening is available. Cascade testing is appropriate once a familial pathogenic variant is established.

## 11. Outcome and prognosis

No survival curve, disease-specific mortality rate, or life-expectancy estimate exists. Survival into adulthood—including an individual aged 55 years—has been documented, but the literature is too small to conclude that life expectancy is normal. (glinton2021phenotypicexpansionof pages 3-4)

Long-term morbidity is primarily neurodevelopmental and functional: communication limitations, intellectual disability, motor delay/hypotonia, epilepsy in a subset, growth impairment, ocular complications, and orthopedic issues. Recovery to a premorbid state is not expected because the condition reflects altered development; nevertheless, function can improve with therapy, education, communication supports, and control of secondary complications. No validated prognostic biomarker or genotype-based outcome calculator exists.

## 12. Treatment and real-world implementation

There is **no approved disease-modifying, gene, RNA, cell, epigenetic, or targeted therapy** for BPTF-related neurodevelopmental disorder. Management is individualized and multidisciplinary:

- early developmental intervention and special education;
- speech-language therapy, including augmentative and alternative communication where needed;
- physical and occupational therapy for hypotonia, motor delay, mobility, and adaptive skills;
- standard antiseizure treatment guided by seizure type and EEG;
- ophthalmologic correction/treatment;
- nutritional and feeding support;
- orthopedic surveillance and treatment for scoliosis or limb-related functional problems;
- psychosocial and family support.

Suggested NCIT concepts include Genetic Counseling, Supportive Care, Speech Therapy, Physical Therapy, Occupational Therapy, Anticonvulsant Therapy, and Vagus Nerve Stimulation; current NCIT identifiers should be validated during ingestion.

Case-level antiseizure implementations in the 2021 cohort included sodium valproate, levetiracetam, and a vagal nerve stimulator. These observations show real-world use but do not establish comparative efficacy or syndrome-specific response rates. (glinton2021phenotypicexpansionof pages 4-5)

A 2023 publication, **Wu and Chen, “The effect of growth hormone treatment in children with novel BPTF gene variants: a report of two cases and literature review,” Molecular Genetics & Genomic Medicine**, DOI [10.1002/mgg3.2066](https://doi.org/10.1002/mgg3.2066), was identified. Because direct outcome data were unavailable in the retrieved evidence, growth hormone should not be portrayed as established NEDDFL therapy; its use would require conventional endocrinologic evaluation and individualized risk–benefit review.

A 2024 epilepsy-focused report, **Ferretti et al., “Epilepsy as a novel phenotype of BPTF-related disorders,” Pediatric Neurology**, DOI [10.1016/j.pediatrneurol.2024.06.001](https://doi.org/10.1016/j.pediatrneurol.2024.06.001), indicates growing characterization of seizure phenotypes, but detailed statistics could not be verified here.

No BPTF/NEDDFL-specific interventional ClinicalTrials.gov study or treatment algorithm was identified. Pharmacogenomic guidance specific to BPTF is absent.

## 13. Prevention

There is no lifestyle, medication, vaccine, or environmental intervention that prevents a de novo pathogenic BPTF variant. Primary prevention is therefore limited to informed reproductive options when a familial variant is known: genetic counseling, prenatal diagnosis, and preimplantation genetic testing for monogenic disease. Secondary prevention consists of early molecular diagnosis and prompt developmental, communication, vision, nutritional, orthopedic, and epilepsy evaluation. Tertiary prevention aims to reduce complications and maximize function through ongoing multidisciplinary care.

For confirmed de novo cases, parental testing informs recurrence counseling but cannot eliminate residual germline-mosaicism risk. For inherited variants, cascade testing can identify relatives who may benefit from clinical evaluation and reproductive counseling. (glinton2021phenotypicexpansionof pages 3-4)

## 14. Other species and natural disease

No naturally occurring BPTF-associated veterinary disease, affected breed, zoonotic potential, or cross-species transmission was identified. Orthologous developmental function is conserved experimentally in vertebrates. Relevant taxa are **Danio rerio (NCBI Taxonomy 7955)** and **Mus musculus (NCBI Taxonomy 10090)**. Species-specific Bptf gene identifiers should be obtained directly from the current NCBI Gene/Alliance records before database ingestion.

## 15. Model organisms

### Zebrafish

CRISPR-Cas9 disruption of **bptf** in F0 zebrafish caused reduced head size, increased TUNEL-positive apoptosis, altered phospho-histone-H3 proliferation measures, and abnormal craniofacial patterning, including increased ceratohyal angle. This recapitulates the human microcephaly/craniofacial axis and supports a developmental loss-of-function mechanism. Limitations include F0 mosaicism, uncertain allele dosage, and incomplete modeling of cognition and speech. (stankiewicz2017haploinsufficiencyofthe pages 1-2)

### Mouse

The 2022 **Emx1-Cre forebrain-specific Bptf conditional knockout** survived into adulthood but was smaller and had severe cortical hypoplasia, prolonged progenitor cycling, increased cell death, reduced neuronal output, disturbed lamination, fewer deep-layer neurons, and impaired neuronal maturation. It is a strong mechanistic model for corticogenesis and transcriptomic studies. Its major limitation is that biallelic tissue-specific ablation is more severe and spatially restricted than constitutional human heterozygous haploinsufficiency; heterozygous mice reportedly had much smaller effects. (glinton2021phenotypicexpansionof pages 1-3, zapata2022generationofa pages 1-2)

No validated patient-derived iPSC, brain-organoid, rat, Drosophila, C. elegans, or naturally occurring animal model was identified in the retrieved disease-specific evidence.

## Recent research and authoritative interpretation

The field’s current interpretation is that BPTF-related NDD belongs to the broader class of dosage-sensitive chromatinopathies. Human genetics strongly supports haploinsufficiency, while zebrafish and mouse experiments connect the genetic lesion to apoptosis, progenitor dysfunction, reduced neuronal production, and impaired cortical fate specification. The major unresolved translational challenge is that the severe knockout models do not precisely reproduce the variable heterozygous human phenotype. Human cellular models and variant-sensitive functional assays are priorities, particularly for missense and inherited variants. (zapata2022generationofa pages 1-2, glinton2021phenotypicexpansionof pages 12-13)

The most important recent developments are therefore phenotypic rather than therapeutic: recognition of inherited disease and milder expression, expanded seizure and ophthalmologic phenotypes, exploratory growth-hormone treatment, and mechanistic forebrain RNA-seq. No precision therapy has reached clinical implementation.

## Key primary sources and abstract quotations

1. **Stankiewicz et al.** “Haploinsufficiency of the Chromatin Remodeler BPTF Causes Syndromic Developmental and Speech Delay, Postnatal Microcephaly, and Dysmorphic Features.” *American Journal of Human Genetics* 101:503–515. Published October 2017. DOI: [10.1016/j.ajhg.2017.08.014](https://doi.org/10.1016/j.ajhg.2017.08.014). Landmark human cohort plus zebrafish validation: ten unrelated individuals, 8 loss-of-function and 2 missense variants, with DD/ID and speech delay in 10/10. (stankiewicz2017haploinsufficiencyofthe pages 1-2)

2. **Glinton et al.** “Phenotypic expansion of the BPTF-related neurodevelopmental disorder with dysmorphic facies and distal limb anomalies.” *American Journal of Medical Genetics Part A* 185:1366–1378. Published January 2021. DOI: [10.1002/ajmg.a.62102](https://doi.org/10.1002/ajmg.a.62102). Abstract quotation: “To expand the NEDDFL phenotypic spectrum, we describe the clinical features in 25 novel individuals with 20 distinct, clinically relevant variants in BPTF, including four individuals with inherited changes in BPTF.” It further reports “mild brain abnormalities, seizures, scoliosis, and a variety of ophthalmologic complications.” (glinton2021phenotypicexpansionof pages 1-3)

3. **Zapata, Yan, and Picketts.** “Generation of a mouse model of the neurodevelopmental disorder with dysmorphic facies and distal limb anomalies (NEDDFL) syndrome.” *Human Molecular Genetics* 31:3405–3421. Published May 2022. DOI: [10.1093/hmg/ddac119](https://doi.org/10.1093/hmg/ddac119). Abstract quotation: “Prolonged progenitor cell cycle length and a high incidence of cell death reduced neuronal output.” The authors also report disrupted cortical lamination, neuronal maturation defects, and RNA-seq pathway changes. (zapata2022generationofa pages 1-2)

## Knowledge-base-ready summary

The following artifact consolidates evidence-supported disease, phenotype, mechanism, diagnostic, treatment, anatomy, and model annotations, while explicitly marking unverified identifiers and unknown fields.

| domain | evidence-based finding | suggested ontology terms | evidence strength/limitations |
|---|---|---|---|
| Disease name/definition | BPTF-related neurodevelopmental disorder is also called neurodevelopmental disorder with dysmorphic facies and distal limb anomalies (NEDDFL); core syndrome includes developmental delay/intellectual disability, speech delay, postnatal microcephaly, and dysmorphic features due to heterozygous BPTF variants (glinton2021phenotypicexpansionof pages 1-3, stankiewicz2017haploinsufficiencyofthe pages 1-2) | OMIM:617755; MONDO: not verified/uncertain; disease label: NEDDFL | Strong human cohort evidence from 2017 and 2021; MONDO/Orphanet identifier not verified in available evidence |
| Synonyms | BPTF-related neurodevelopmental disorder; NEDDFL; neurodevelopmental disorder with dysmorphic facies and distal limb anomalies (glinton2021phenotypicexpansionof pages 1-3, zapata2022generationofa pages 1-2) | Exact synonym mapping pending external ontology verification | Strong for naming in literature; formal synonym list incomplete in available context |
| Evidence source type | Data are aggregated from published human case series/cohorts and model-organism studies, not EHR-derived datasets in the available evidence (stankiewicz2017haploinsufficiencyofthe pages 1-2, zapata2022generationofa pages 1-2) | ECO:0000218 expert assertion supported by traceable author statement (suggested) | Strong for published-source provenance; no registry-scale natural history dataset identified |
| Causal gene/locus | Causal gene is BPTF on chromosome 17q24.2; disease is associated with heterozygous pathogenic variants and haploinsufficiency (stankiewicz2017haploinsufficiencyofthe pages 1-2) | HGNC:BPTF; UBERON not applicable; Sequence Ontology terms: frameshift_variant, stop_gained, splice_acceptor_variant/splice_donor_variant, inframe_deletion, missense_variant | Strong for gene-disease validity; exact HGNC ID not provided in available context |
| Protein/complex | BPTF is the largest subunit of the nucleosome remodeling factor (NURF) chromatin-remodeling complex (glinton2021phenotypicexpansionof pages 1-3, zapata2022generationofa pages 1-2) | GO:0006338 chromatin remodeling; GO:0030674 protein-containing complex (general); NURF complex term suggested if curated externally | Strong mechanistic consensus; exact GO complex accession for NURF not verified here |
| Molecular mechanism | Current best-supported mechanism is BPTF haploinsufficiency causing dysregulated chromatin remodeling and transcription during neurodevelopment (glinton2021phenotypicexpansionof pages 1-3, glinton2021phenotypicexpansionof pages 3-4, stankiewicz2017haploinsufficiencyofthe pages 1-2, zapata2022generationofa pages 1-2) | HP:0000006 Autosomal dominant inheritance; GO:0006357 regulation of transcription by RNA polymerase II; GO:0006338 chromatin remodeling | Strong for loss-of-function/haploinsufficiency; no evidence for protective variants or environmental triggers |
| Chromatin-reader biology | BPTF binds H3K4me3 through its PHD finger and H4K16ac through its bromodomain, supporting an epigenetic reader/remodeler role (glinton2021phenotypicexpansionof pages 1-3) | GO:0042393 histone binding; GO:0016568 chromatin modification (broad); CHEBI terms for modified histones could be added in curation | Moderate-strong mechanistic evidence; largely inferred from molecular studies summarized in clinical paper |
| Core phenotype: developmental delay/intellectual disability | Reported in 10/10 individuals in the 2017 cohort and 88% in the 2021 cohort (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 3-4) | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability | Strong replicated cohort evidence; severity spectrum incompletely quantified |
| Core phenotype: speech delay | Reported in 10/10 individuals in 2017 and 85% in 2021 (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 3-4) | HP:0000750 Delayed speech and language development | Strong replicated cohort evidence |
| Core phenotype: postnatal microcephaly | Reported in 7/9 individuals in 2017; 42% in 2021 cohort summary; 60% microcephaly at assessment in one detailed 2021 extraction; 40% had microcephaly at birth in that extraction (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 3-4, glinton2021phenotypicexpansionof pages 4-5) | HP:0000252 Microcephaly; HP:0000253 Progressive microcephaly (suggested where postnatal worsening documented) | Strong that microcephaly is common; exact frequency varies with denominator/definition across summaries |
| Core phenotype: dysmorphic features | Dysmorphic features were present in 9/10 in 2017 and 77% in one 2021 summary; all 20 individuals with available detailed dysmorphology data reportedly had mild dysmorphic features in another 2021 extraction (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 3-4, glinton2021phenotypicexpansionof pages 4-5) | HP:0001999 Facial dysmorphism; phenotype-specific HPOs may include pointed chin, bulbous nose, prominent nasal ridge | Strong that dysmorphism is common; exact aggregate frequency varies by denominator and ascertainment |
| Core phenotype: motor delay | Motor delay reported in 69% of 2021 cohort (glinton2021phenotypicexpansionof pages 3-4) | HP:0001270 Motor delay | Moderate-strong; not explicitly quantified in 2017 extraction |
| Core phenotype: hypotonia | Hypotonia/history of hypotonia reported in 38% of 2021 cohort (glinton2021phenotypicexpansionof pages 3-4, glinton2021phenotypicexpansionof pages 4-5) | HP:0001252 Hypotonia | Moderate-strong cohort evidence |
| Additional neurologic phenotype: seizures/EEG abnormalities | Seizures/EEG abnormalities were newly emphasized in 2021; 6 patients had seizure history requiring treatment, and 2 had electrographic abnormalities only (glinton2021phenotypicexpansionof pages 4-5, glinton2021phenotypicexpansionof pages 1-3) | HP:0001250 Seizure; HP:0010843 Abnormality of the EEG | Moderate evidence from expanded cohort; 2024 epilepsy-focused paper identified bibliographically but not available in accessible full text |
| Neuroimaging | In 2021, MRI was normal in 8/13 imaged individuals and mildly abnormal in 5/13, indicating variable and often subtle brain structural findings (glinton2021phenotypicexpansionof pages 4-5, glinton2021phenotypicexpansionof pages 1-3) | HP:0410263 Abnormal brain MRI; UBERON:0000955 brain | Moderate evidence; exact MRI anomaly types not fully extractable from available context |
| Skeletal/limb phenotype | Distal limb anomalies are part of the syndrome label; reported findings include scoliosis, cutaneous syndactyly, sandal-gap anomalies, limb-length discrepancy, and delayed bone age in some individuals (glinton2021phenotypicexpansionof pages 9-10, glinton2021phenotypicexpansionof pages 1-3) | HP:0001159 Syndactyly; HP:0002650 Scoliosis; HP:0010687 Abnormality of the digits | Moderate evidence; frequencies not fully extractable |
| Ophthalmologic phenotype | Ophthalmologic complications were reported in the expanded 2021 cohort (glinton2021phenotypicexpansionof pages 1-3) | HP:0000478 Abnormality of the eye | Moderate evidence; exact eye findings and frequencies not fully extractable |
| Growth phenotype | Short stature occurred in 25%, decreased weight in 53%, and microcephaly/growth restriction were also observed in 2021 extraction (glinton2021phenotypicexpansionof pages 4-5) | HP:0004322 Short stature; HP:0004325 Poor weight gain | Moderate evidence; 2023 growth-hormone report was identified bibliographically but direct outcome details were unavailable |
| Age at onset/course | Typical onset is congenital/early childhood with neurodevelopmental manifestations recognized in infancy or childhood; published ages ranged from 2.1-13 years in 2017 and 23 months-55 years in 2021, supporting lifelong persistence (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 3-4) | HP:0003577 Congenital onset; HP:0011463 Childhood onset | Strong for pediatric onset and chronic course; no formal staging system identified |
| Variant spectrum | 2017: 8 loss-of-function and 2 missense variants among 10 unrelated individuals. 2021: 20 distinct variants including 9 frameshift, 4 nonsense, 3 splicing, 2 in-frame deletions, 1 missense, and 1 single-exon deletion; ACMG classes included pathogenic, likely pathogenic, and 2 VUS (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 3-4) | Sequence Ontology: frameshift_variant, stop_gained, splice_region/splice_donor/splice_acceptor, inframe_deletion, missense_variant, exon_loss_variant | Strong for predominance of truncating variants; exact HGVS list incomplete in accessible evidence |
| Inheritance | Predominantly autosomal dominant. Initial reports were mostly de novo; 2021 provided first non-mosaic affected-parent transmissions, showing inherited causative variants also occur (glinton2021phenotypicexpansionof pages 3-4, stankiewicz2017haploinsufficiencyofthe pages 1-2) | HP:0000006 Autosomal dominant inheritance; HP:0025352 De novo mutation (suggested annotation at variant level) | Strong for AD inheritance with variable expressivity; penetrance not quantified |
| Penetrance/expressivity | Expressivity appears variable, with milder phenotypes noted especially for some missense/inherited cases; penetrance remains not established from available data (glinton2021phenotypicexpansionof pages 12-13, glinton2021phenotypicexpansionof pages 3-4) | HP:0003828 Variable expressivity | Moderate evidence for variability; penetrance unknown |
| Population/epidemiology | No reliable prevalence or incidence estimates were identified in the available evidence; published literature consists of rare case series/families (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 3-4) | Orphan disease; MONDO/Orphanet prevalence pending verification | Major evidence gap |
| Sex distribution | 2021 cohort included 14 males and 11 females in the extracted summary, arguing against a strong sex-limited pattern (glinton2021phenotypicexpansionof pages 3-4) | PATO sex terms not necessary | Moderate evidence; one extracted count sums to 25 despite cohort described as 26, indicating source-summary inconsistency |
| Diagnostics: clinical | Diagnosis is suspected from syndromic NDD with speech delay, microcephaly, dysmorphic facies, and distal limb anomalies, with supportive MRI/EEG findings when present (glinton2021phenotypicexpansionof pages 1-3, glinton2021phenotypicexpansionof pages 4-5, stankiewicz2017haploinsufficiencyofthe pages 1-2) | HPO set above; NCIT:C159866 Genetic Testing (broad suggested term) | Strong for phenotype-guided suspicion; no formal consensus clinical criteria identified |
| Diagnostics: genetic testing | WES and chromosomal microarray were used in the landmark cohort; later cohorts identified sequence variants and single-exon deletions, supporting exome/genome sequencing plus CNV analysis as useful approaches (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 4-5) | NCIT:C101294 Whole Exome Sequencing; NCIT:C63420 Comparative Genomic Hybridization/array-based CNV analysis (suggested broad mapping) | Strong practical evidence from case ascertainment; no disease-specific testing guideline located |
| Functional/omics diagnostics | 2021 authors noted lack of well-validated functional assays and suggested RNA-seq or proteomics may have diagnostic utility for difficult variants such as missense changes (glinton2021phenotypicexpansionof pages 12-13) | NCIT:C153191 RNA Sequencing; NCIT:C20085 Proteomic Profiling (suggested) | Hypothesis-level/author opinion rather than established clinical standard |
| Differential diagnosis | Differential includes other syndromic neurodevelopmental disorders/chromatinopathies and cases initially labeled as other growth syndromes; one cited 2019 adult case had initially been diagnosed with Silver-Russell syndrome (glinton2021phenotypicexpansionof pages 13-13) | Broad category: chromatinopathy | Limited direct evidence in available context |
| Treatment/supportive care | No disease-modifying therapy is established. Reported management is supportive and symptom-directed: developmental therapies, educational support, seizure management, and routine multidisciplinary surveillance (inferred from seizure treatments and chronic NDD features) (glinton2021phenotypicexpansionof pages 4-5) | NCIT:C15604 Supportive Care; NCIT:C21072 Physical Therapy; NCIT:C17733 Occupational Therapy; NCIT:C12453 Speech Therapy | Moderate evidence for supportive approach; formal treatment algorithms absent |
| Seizure treatment examples | Reported anti-seizure interventions in 2021 cohort included sodium valproate, levetiracetam, and vagal nerve stimulator use in individual patients (glinton2021phenotypicexpansionof pages 4-5) | NCIT:C29511 Sodium Valproate; NCIT:C1570 Levetiracetam; NCIT:C99939 Vagus Nerve Stimulation | Case-level evidence only; no response rates or syndrome-specific efficacy data |
| Growth hormone | A 2023 report on growth hormone treatment in children with novel BPTF variants was identified bibliographically but not accessible in full text here, so efficacy/safety cannot be reliably summarized (from search history noted in conversation) | NCIT:C1772 Somatropin/Growth Hormone (if later curated) | Explicit evidence gap in accessible corpus |
| Prognosis/outcomes | Available evidence suggests a chronic lifelong neurodevelopmental disorder with survival into adulthood documented (age up to 55 years in 2021 cohort), but no formal survival, mortality, or quality-of-life statistics were identified (glinton2021phenotypicexpansionof pages 3-4) | ICF/quality-of-life terms could be added later | Major gap: no natural-history or mortality study found |
| Environmental factors | No established environmental, infectious, lifestyle, or protective factors were identified; disease is currently understood as primarily Mendelian/genetic (stankiewicz2017haploinsufficiencyofthe pages 1-2, zapata2022generationofa pages 1-2) | Not established | Strong negative statement based on absence in current literature context |
| Gene-environment interaction | No BPTF-specific gene-environment interaction data were identified (stankiewicz2017haploinsufficiencyofthe pages 1-2, zapata2022generationofa pages 1-2) | Not established | Evidence gap |
| Primary anatomy | Central nervous system/brain, especially forebrain and cerebral cortex, are the primary affected structures based on human phenotype and mouse modeling (zapata2022generationofa pages 1-2) | UBERON:0000955 brain; UBERON:0001890 cerebral cortex; UBERON:0001891 telencephalon/forebrain suggested | Strong convergent human/model evidence |
| Cell types implicated | Neural progenitor cells and cortical neurons are implicated; mouse data show prolonged progenitor cell cycle, reduced neuronal output, and impaired deep-layer neuron maturation including Ctip2+ neurons (zapata2022generationofa pages 1-2) | CL:0011115 neural progenitor cell (suggested); CL:0000540 neuron; CL:cortical neuron/deep-layer cortical projection neuron suggested | Strong model evidence; exact CL IDs for all cortical subtypes should be curator-verified |
| Cellular processes | Upstream defect involves impaired chromatin remodeling/transcriptional regulation; downstream effects include prolonged progenitor cell cycle, apoptosis, disrupted neuronal fate specification, cortical lamination defects, and reduced neuronal maturation (zapata2022generationofa pages 1-2) | GO:0006338 chromatin remodeling; GO:0051301 cell division; GO:0006915 apoptotic process; GO:0022008 neurogenesis; GO:0007417 central nervous system development; GO:0007399 nervous system development | Strong mouse mechanistic evidence; direct human tissue confirmation lacking |
| Subcellular localization | Disease mechanism is centered in the nucleus/chromatin compartment, consistent with a chromatin-remodeling transcription factor (glinton2021phenotypicexpansionof pages 1-3, zapata2022generationofa pages 1-2) | GO:0005634 nucleus; GO:0000785 chromatin | Strong general mechanistic inference |
| Molecular profiling | Mouse forebrain RNA-seq identified altered expression of fate-determining transcription factors and pathways related to neural development, apoptotic signaling, and amino acid biosynthesis; dysregulated genes were enriched for Myc binding sites (zapata2022generationofa pages 1-2) | GO:0009880 embryonic pattern specification; GO:0043066 negative regulation of apoptotic process/related apoptosis terms; GO:0008652 cellular amino acid biosynthetic process | Strong model evidence; no human transcriptomic signature established |
| Expert mechanistic interpretation | Available studies support a causal chain from BPTF loss-of-function to NURF dysfunction, altered chromatin accessibility/transcription in developing cortex, reduced progenitor fitness and neuronal specification, then microcephaly/intellectual disability/speech delay (glinton2021phenotypicexpansionof pages 1-3, zapata2022generationofa pages 1-2) | Pathway annotation can center on chromatin remodeling and corticogenesis | Strong synthesis from human genetics plus mouse model |
| Animal model: zebrafish | CRISPR/Cas9 F0 zebrafish bptf disruption caused reduced head size, increased apoptosis, altered proliferation, and abnormal craniofacial patterning (stankiewicz2017haploinsufficiencyofthe pages 1-2) | NCBITaxon:7955 Danio rerio | Strong experimental support for developmental role; F0 mosaic model limitations |
| Animal model: mouse | Forebrain-specific Bptf conditional knockout mice were viable to adulthood but smaller and showed severe cortical hypoplasia, prolonged progenitor cell cycle, high cell death, disrupted cortical lamination, reduced deep-layer neurons, and neuronal maturation defects (zapata2022generationofa pages 1-2) | NCBITaxon:10090 Mus musculus | Strong disease-relevant mechanistic model; conditional knockout is more severe than human heterozygous state |
| Natural disease in other species | No naturally occurring veterinary BPTF-related disorder was identified in available evidence (stankiewicz2017haploinsufficiencyofthe pages 1-2, zapata2022generationofa pages 1-2) | Not established | Evidence gap |
| Clinical trials | No disease-specific interventional clinical trials were identified in the available search results (clinical trial search in conversation) | Not established | Evidence gap |
| Prevention/genetic counseling | Prevention is limited to reproductive/genetic counseling, with recurrence risk depending on whether a variant is de novo or inherited from an affected parent; cascade testing may be relevant once a familial variant is known (glinton2021phenotypicexpansionof pages 3-4) | NCIT:C15280 Genetic Counseling | Moderate evidence from inheritance data; no formal counseling guideline identified |
| Unknown/not established fields | Prevalence, incidence, penetrance, founder effects, carrier frequency, environmental modifiers, protective factors, standardized diagnostic criteria, prognostic biomarkers, disease-specific QoL measures, and targeted molecular therapies are not established in the available evidence (stankiewicz2017haploinsufficiencyofthe pages 1-2, glinton2021phenotypicexpansionof pages 12-13, glinton2021phenotypicexpansionof pages 3-4) | Mark as unknown/not established in KB | Important to preserve as explicit negatives/gaps rather than infer unsupported claims |


*Table: This table summarizes knowledge-base-ready findings for BPTF-related neurodevelopmental disorder/NEDDFL, including core phenotypes, mechanism, diagnostics, inheritance, and model evidence. It also flags important unknowns and limitations where the available evidence is sparse or unverified.*

## Critical data gaps

The following should remain explicitly **unknown/not established** in a production knowledge base: disease-specific MONDO and Orphanet identifiers unless separately verified; prevalence and incidence; penetrance; ancestry or geographic effects; founder variants; quantitative quality of life; standardized diagnostic criteria; longitudinal natural history; life expectancy; prognostic biomarkers; validated episignature; human single-cell/spatial/multi-omics profiles; treatment response rates; and disease-modifying or preventive therapy. Apparent precision beyond the small published cohorts would be misleading.

References

1. (glinton2021phenotypicexpansionof pages 1-3): Kevin E. Glinton, Anna C. E. Hurst, Kevin M. Bowling, Ingrid Cristian, Devon Haynes, Dusit Adstamongkonkul, Oskar Schnappauf, David B. Beck, Carole Brewer, Aditi Shah Parikh, Deepali N. Shinde, Alan Donaldson, Ariel Brautbar, Saskia Koene, Arie van Haeringen, Amélie Piton, Yline Capri, Margherita Furlan, Elena Gardella, Rikke Steensbjerre Møller, Irma van de Beek, Linda Zuurbier, Phillis Lakeman, Allan Bayat, Julian Martinez, Rebecca Signer, Pernille M. Torring, Morten Buch Engelund, Karen W. Gripp, Louise Amlie‐Wolf, Lindsay B. Henderson, Alina T. Midro, Eugeniusz Tarasów, Beata Stasiewicz‐Jarocka, Diana Moskal‐Jasinska, Paul Vos, Felix Boschann, Corinna Stoltenburg, Oliver Puk, Inger‐Lise Mero, Kristine Lossius, Cyril Mignot, Boris Keren, Johanna C. Acosta Guio, Ignacio Briceño, Alberto Gomez, Yaping Yang, and Pawel Stankiewicz. Phenotypic expansion of the bptf‐related neurodevelopmental disorder with dysmorphic facies and distal limb anomalies. American Journal of Medical Genetics. Part a, 185:1366-1378, Jan 2021. URL: https://doi.org/10.1002/ajmg.a.62102, doi:10.1002/ajmg.a.62102. This article has 33 citations and is from a peer-reviewed journal.

2. (stankiewicz2017haploinsufficiencyofthe pages 1-2): Paweł Stankiewicz, Tahir N. Khan, Przemyslaw Szafranski, Leah Slattery, Haley Streff, Francesco Vetrini, Jonathan A. Bernstein, Chester W. Brown, Jill A. Rosenfeld, Surya Rednam, Sarah Scollon, Katie L. Bergstrom, Donald W. Parsons, Sharon E. Plon, Marta W. Vieira, Caio R.D.C. Quaio, Wagner A.R. Baratela, Johanna C. Acosta Guio, Ruth Armstrong, Sarju G. Mehta, Patrick Rump, Rolph Pfundt, Raymond Lewandowski, Erica M. Fernandes, Deepali N. Shinde, Sha Tang, Juliane Hoyer, Christiane Zweier, André Reis, Carlos A. Bacino, Rui Xiao, Amy M. Breman, Janice L. Smith, Nicholas Katsanis, Bret Bostwick, Bernt Popp, Erica E. Davis, and Yaping Yang. Haploinsufficiency of the chromatin remodeler bptf causes syndromic developmental and speech delay, postnatal microcephaly, and dysmorphic features. American journal of human genetics, 101 4:503-515, Oct 2017. URL: https://doi.org/10.1016/j.ajhg.2017.08.014, doi:10.1016/j.ajhg.2017.08.014. This article has 113 citations and is from a highest quality peer-reviewed journal.

3. (glinton2021phenotypicexpansionof pages 3-4): Kevin E. Glinton, Anna C. E. Hurst, Kevin M. Bowling, Ingrid Cristian, Devon Haynes, Dusit Adstamongkonkul, Oskar Schnappauf, David B. Beck, Carole Brewer, Aditi Shah Parikh, Deepali N. Shinde, Alan Donaldson, Ariel Brautbar, Saskia Koene, Arie van Haeringen, Amélie Piton, Yline Capri, Margherita Furlan, Elena Gardella, Rikke Steensbjerre Møller, Irma van de Beek, Linda Zuurbier, Phillis Lakeman, Allan Bayat, Julian Martinez, Rebecca Signer, Pernille M. Torring, Morten Buch Engelund, Karen W. Gripp, Louise Amlie‐Wolf, Lindsay B. Henderson, Alina T. Midro, Eugeniusz Tarasów, Beata Stasiewicz‐Jarocka, Diana Moskal‐Jasinska, Paul Vos, Felix Boschann, Corinna Stoltenburg, Oliver Puk, Inger‐Lise Mero, Kristine Lossius, Cyril Mignot, Boris Keren, Johanna C. Acosta Guio, Ignacio Briceño, Alberto Gomez, Yaping Yang, and Pawel Stankiewicz. Phenotypic expansion of the bptf‐related neurodevelopmental disorder with dysmorphic facies and distal limb anomalies. American Journal of Medical Genetics. Part a, 185:1366-1378, Jan 2021. URL: https://doi.org/10.1002/ajmg.a.62102, doi:10.1002/ajmg.a.62102. This article has 33 citations and is from a peer-reviewed journal.

4. (zapata2022generationofa pages 1-2): Gerardo Zapata, Keqin Yan, and David J Picketts. Generation of a mouse model of the neurodevelopmental disorder with dysmorphic facies and distal limb anomalies (neddfl) syndrome. Human molecular genetics, 31:3405-3421, May 2022. URL: https://doi.org/10.1093/hmg/ddac119, doi:10.1093/hmg/ddac119. This article has 14 citations and is from a domain leading peer-reviewed journal.

5. (glinton2021phenotypicexpansionof pages 12-13): Kevin E. Glinton, Anna C. E. Hurst, Kevin M. Bowling, Ingrid Cristian, Devon Haynes, Dusit Adstamongkonkul, Oskar Schnappauf, David B. Beck, Carole Brewer, Aditi Shah Parikh, Deepali N. Shinde, Alan Donaldson, Ariel Brautbar, Saskia Koene, Arie van Haeringen, Amélie Piton, Yline Capri, Margherita Furlan, Elena Gardella, Rikke Steensbjerre Møller, Irma van de Beek, Linda Zuurbier, Phillis Lakeman, Allan Bayat, Julian Martinez, Rebecca Signer, Pernille M. Torring, Morten Buch Engelund, Karen W. Gripp, Louise Amlie‐Wolf, Lindsay B. Henderson, Alina T. Midro, Eugeniusz Tarasów, Beata Stasiewicz‐Jarocka, Diana Moskal‐Jasinska, Paul Vos, Felix Boschann, Corinna Stoltenburg, Oliver Puk, Inger‐Lise Mero, Kristine Lossius, Cyril Mignot, Boris Keren, Johanna C. Acosta Guio, Ignacio Briceño, Alberto Gomez, Yaping Yang, and Pawel Stankiewicz. Phenotypic expansion of the bptf‐related neurodevelopmental disorder with dysmorphic facies and distal limb anomalies. American Journal of Medical Genetics. Part a, 185:1366-1378, Jan 2021. URL: https://doi.org/10.1002/ajmg.a.62102, doi:10.1002/ajmg.a.62102. This article has 33 citations and is from a peer-reviewed journal.

6. (glinton2021phenotypicexpansionof pages 4-5): Kevin E. Glinton, Anna C. E. Hurst, Kevin M. Bowling, Ingrid Cristian, Devon Haynes, Dusit Adstamongkonkul, Oskar Schnappauf, David B. Beck, Carole Brewer, Aditi Shah Parikh, Deepali N. Shinde, Alan Donaldson, Ariel Brautbar, Saskia Koene, Arie van Haeringen, Amélie Piton, Yline Capri, Margherita Furlan, Elena Gardella, Rikke Steensbjerre Møller, Irma van de Beek, Linda Zuurbier, Phillis Lakeman, Allan Bayat, Julian Martinez, Rebecca Signer, Pernille M. Torring, Morten Buch Engelund, Karen W. Gripp, Louise Amlie‐Wolf, Lindsay B. Henderson, Alina T. Midro, Eugeniusz Tarasów, Beata Stasiewicz‐Jarocka, Diana Moskal‐Jasinska, Paul Vos, Felix Boschann, Corinna Stoltenburg, Oliver Puk, Inger‐Lise Mero, Kristine Lossius, Cyril Mignot, Boris Keren, Johanna C. Acosta Guio, Ignacio Briceño, Alberto Gomez, Yaping Yang, and Pawel Stankiewicz. Phenotypic expansion of the bptf‐related neurodevelopmental disorder with dysmorphic facies and distal limb anomalies. American Journal of Medical Genetics. Part a, 185:1366-1378, Jan 2021. URL: https://doi.org/10.1002/ajmg.a.62102, doi:10.1002/ajmg.a.62102. This article has 33 citations and is from a peer-reviewed journal.

7. (glinton2021phenotypicexpansionof pages 9-10): Kevin E. Glinton, Anna C. E. Hurst, Kevin M. Bowling, Ingrid Cristian, Devon Haynes, Dusit Adstamongkonkul, Oskar Schnappauf, David B. Beck, Carole Brewer, Aditi Shah Parikh, Deepali N. Shinde, Alan Donaldson, Ariel Brautbar, Saskia Koene, Arie van Haeringen, Amélie Piton, Yline Capri, Margherita Furlan, Elena Gardella, Rikke Steensbjerre Møller, Irma van de Beek, Linda Zuurbier, Phillis Lakeman, Allan Bayat, Julian Martinez, Rebecca Signer, Pernille M. Torring, Morten Buch Engelund, Karen W. Gripp, Louise Amlie‐Wolf, Lindsay B. Henderson, Alina T. Midro, Eugeniusz Tarasów, Beata Stasiewicz‐Jarocka, Diana Moskal‐Jasinska, Paul Vos, Felix Boschann, Corinna Stoltenburg, Oliver Puk, Inger‐Lise Mero, Kristine Lossius, Cyril Mignot, Boris Keren, Johanna C. Acosta Guio, Ignacio Briceño, Alberto Gomez, Yaping Yang, and Pawel Stankiewicz. Phenotypic expansion of the bptf‐related neurodevelopmental disorder with dysmorphic facies and distal limb anomalies. American Journal of Medical Genetics. Part a, 185:1366-1378, Jan 2021. URL: https://doi.org/10.1002/ajmg.a.62102, doi:10.1002/ajmg.a.62102. This article has 33 citations and is from a peer-reviewed journal.

8. (glinton2021phenotypicexpansionof pages 13-13): Kevin E. Glinton, Anna C. E. Hurst, Kevin M. Bowling, Ingrid Cristian, Devon Haynes, Dusit Adstamongkonkul, Oskar Schnappauf, David B. Beck, Carole Brewer, Aditi Shah Parikh, Deepali N. Shinde, Alan Donaldson, Ariel Brautbar, Saskia Koene, Arie van Haeringen, Amélie Piton, Yline Capri, Margherita Furlan, Elena Gardella, Rikke Steensbjerre Møller, Irma van de Beek, Linda Zuurbier, Phillis Lakeman, Allan Bayat, Julian Martinez, Rebecca Signer, Pernille M. Torring, Morten Buch Engelund, Karen W. Gripp, Louise Amlie‐Wolf, Lindsay B. Henderson, Alina T. Midro, Eugeniusz Tarasów, Beata Stasiewicz‐Jarocka, Diana Moskal‐Jasinska, Paul Vos, Felix Boschann, Corinna Stoltenburg, Oliver Puk, Inger‐Lise Mero, Kristine Lossius, Cyril Mignot, Boris Keren, Johanna C. Acosta Guio, Ignacio Briceño, Alberto Gomez, Yaping Yang, and Pawel Stankiewicz. Phenotypic expansion of the bptf‐related neurodevelopmental disorder with dysmorphic facies and distal limb anomalies. American Journal of Medical Genetics. Part a, 185:1366-1378, Jan 2021. URL: https://doi.org/10.1002/ajmg.a.62102, doi:10.1002/ajmg.a.62102. This article has 33 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](BPTF-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.