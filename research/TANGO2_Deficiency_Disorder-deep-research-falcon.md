---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T01:27:13.194737'
end_time: '2026-07-31T01:39:59.888823'
duration_seconds: 766.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: TANGO2 Deficiency Disorder
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 44
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: TANGO2_Deficiency_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TANGO2 Deficiency Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TANGO2 Deficiency Disorder** covering all of the
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
- **Disease Name:** TANGO2 Deficiency Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TANGO2 Deficiency Disorder** covering all of the
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


# TANGO2 Deficiency Disorder: Disease-Characteristics Research Report

**Scope and evidence note.** This synthesis emphasizes primary human and experimental studies through 2024. The retrieved bibliographic records did not expose PMID fields reliably; therefore, DOI and ClinicalTrials.gov URLs are supplied rather than inferred. Frequency estimates come from selected rare-disease cohorts and should not be interpreted as population prevalence. Short quotations are reproduced only where supported by retrieved abstracts.

## Executive summary

TANGO2 deficiency disorder (TDD) is a rare, autosomal-recessive, multisystem Mendelian disease caused by biallelic pathogenic loss-of-function variants in **TANGO2** at 22q11.21. Its defining combination is neurodevelopmental impairment plus stress-triggered metabolic crises, rhabdomyolysis, QT prolongation, malignant ventricular arrhythmias, and sometimes transient cardiomyopathy. Neurologic deterioration, seizures, ataxia, movement abnormalities, hypothyroidism, feeding problems, and episodic “TANGO2 spells” broaden the phenotype. Illness, fever, fasting, dehydration, reduced food intake, physical exertion, heat, and possibly selected anesthetics can precipitate episodes. The leading immediate threat is arrhythmic cardiac arrest during a metabolic crisis. (heiman2022mitochondrialdysfunctionassociated pages 1-2, miyake2022cardiaccrisescardiac pages 1-2, berat2021clinicalandbiological pages 1-7)

The best-supported mechanistic model is no longer simply a generic primary respiratory-chain disorder. Evidence instead converges on stress-sensitive disruption of lipid/acyl-CoA homeostasis, phosphatidic-acid and glycerolipid metabolism, membrane trafficking, and context-dependent mitochondrial function, causing ROS/lipid peroxidation and energetic/membrane failure in skeletal muscle, cardiomyocytes, and neural tissues. Important uncertainties remain about TANGO2’s exact biochemical activity, subcellular localization, and proposed role in heme transport. (heiman2022mitochondrialdysfunctionassociated pages 1-2, kim2023intrinsicandextrinsic pages 1-3, lujan2023defectsinlipid pages 1-2)

A major 2023–2024 development is convergent evidence for B vitamins: pantothenate/B5 rescues Drosophila and human-cell defects; folate/B9 nearly abolishes arrhythmias in patient-derived cardiomyocytes; and retrospective natural-history observations associate multivitamin/B-complex use with fewer crises. These findings are biologically compelling but not yet validated in randomized clinical trials. (asadi2023vitaminb5a pages 6-8, xu2024folateasa pages 1-2, asadi2023vitaminb5a pages 8-9)

The following table summarizes the principal evidence base.

| domain | strongest finding/statistic | evidence type/sample | source year and DOI/URL | confidence/limitation |
|---|---|---|---|---|
| Identifiers / genetics | TANGO2 deficiency disorder is an autosomal recessive disease caused by biallelic TANGO2 variants; disease mapping available as MONDO_0018820, and phenotype MIM/OMIM 616878 is cited in the literature; common recurrent alleles include the exon 3-9 deletion and c.460G>A (p.Gly154Arg) in some Hispanic/Latino families | Disease database + human clinical genetics; multiple cohorts | 2024 Open Targets disease-target association; 2022 Scientific Reports doi:10.1038/s41598-022-07076-9; 2019 JIMD doi:10.1002/jimd.12156; https://platform.opentargets.org (OpenTargets Search: TANGO2 deficiency disorder-TANGO2, heiman2022mitochondrialdysfunctionassociated pages 1-2, mingirulli2020clinicalpresentationand pages 2-3) | High confidence for gene-disease validity and AR inheritance; variant-frequency details remain cohort-dependent and not population-screened globally |
| 20-patient phenotype cohort | In 20 patients from 14 families, neurodevelopmental delay occurred in 85% (17/20), acute metabolic crises in 85% (17/20), hypothyroidism in 60% (12/20); among crises: rhabdomyolysis 88% (15/17), neurologic symptoms 82% (14/17), cardiac features 71% (12/17) | Human multicenter cohort, n=20 | 2020/2021 J Inherit Metab Dis doi:10.1002/jimd.12314 https://doi.org/10.1002/jimd.12314 (berat2021clinicalandbiological pages 1-7, berat2021clinicalandbiological pages 12-17) | High confidence for broad phenotype spectrum; modest sample size and referral-center ascertainment bias |
| 27-patient cardiac crisis series | In 27 patients across 43 crisis admissions, QTc prolongation occurred in 100% with median QTc 547 ms; ventricular tachycardia in 78%, cardiomyopathy in 70%, cardiac arrest in 74%, mortality 37% (10 deaths; 6 arrhythmia-related) | Human retrospective multicenter cardiac crisis study, n=27 patients / 43 admissions | 2022 Heart Rhythm doi:10.1016/j.hrthm.2022.05.009 https://doi.org/10.1016/j.hrthm.2022.05.009 (miyake2022cardiaccrisescardiac pages 1-2) | High confidence for severity during crises; estimates apply to severe admissions rather than all diagnosed patients |
| 2024 22q11.2 screening implementation | In 435 patients with 22q11.2 deletion syndrome, 21 met symptom-based criteria for TANGO2 testing, 9 underwent sequencing, and 0 were diagnosed with TDD; authors highlight underdiagnosis risk because TANGO2 lies within the deleted interval | Human retrospective multicenter screening study, n=435 | 2024 Am J Med Genet A doi:10.1002/ajmg.a.63778 https://doi.org/10.1002/ajmg.a.63778 (owlett2024multicenterappraisalof pages 1-3) | Moderate confidence; useful implementation evidence, but negative yield may reflect incomplete testing and retrospective design |
| Lipid / acyl-CoA mechanism | TANGO2-deficient cells showed increased lysophosphatidic acid and decreased phosphatidic acid, enlarged lipid droplets, elevated ROS, and nutrient-sensitive worsening; authors propose impaired acyl-CoA availability for LPA-to-PA acylation | Experimental cell biology and lipidomics in HepG2 cells and patient fibroblasts | 2023 eLife doi:10.7554/eLife.85345 https://doi.org/10.7554/eLife.85345 (lujan2023defectsinlipid pages 1-2) | Moderate-high confidence for lipid-homeostasis mechanism; exact primary molecular function of TANGO2 remains unsettled |
| Zebrafish model | tango2 loss caused growth defects, early lethality, smaller myofibers, and increased skeletal-muscle susceptibility to extrinsic stressors; 96% mortality by 3 months was reported in the model summary | Model organism study, zebrafish mutants | 2023 Dis Model Mech doi:10.1242/dmm.050092 https://doi.org/10.1242/dmm.050092 (kim2023intrinsicandextrinsic pages 1-3, kim2023intrinsicandextrinsic pages 3-5) | Moderate confidence; strong for stress-sensitive muscle phenotype, but fish may not capture full human neurocardiac disease |
| Vitamin B5 rescue | Pantothenic acid (vitamin B5) rescued multiple TANGO2-associated defects in Drosophila and restored trafficking defects in human cells; in flies, starvation survival improved to ~25 h at 50% survival versus ~12 h untreated, and heat-induced seizures were reduced by ~95% | Drosophila + human cell rescue experiments | 2023 J Inherit Metab Dis doi:10.1002/jimd.12579 https://doi.org/10.1002/jimd.12579 (asadi2023vitaminb5a pages 6-8, asadi2023vitaminb5a pages 1-3) | Moderate confidence preclinically; no randomized human efficacy trial yet |
| Vitamin B9 iPSC-cardiomyocyte rescue | High-dose folate virtually abolished arrhythmias in patient-derived iPSC-cardiomyocytes; rescue was blocked by methotrexate, supporting an intracellular folate-dependent mechanism | Human iPSC-cardiomyocyte disease model + supportive natural-history observation | 2024 JCI Insight doi:10.1172/jci.insight.171005 https://doi.org/10.1172/jci.insight.171005 (xu2024folateasa pages 1-2) | Moderate confidence for mechanistic antiarrhythmic potential; clinical benefit in patients remains observational, not trial-proven |
| Current study infrastructure | NCT05374616 is a recruiting observational natural-history/biorepository study with planned enrollment of 300 and estimated completion in 2030; primary outcome tracks metabolic and cardiac crises over 10 years | ClinicalTrials.gov observational registry/biorepository | ClinicalTrials.gov NCT05374616 https://clinicaltrials.gov/study/NCT05374616 (NCT05374616 chunk 1) | High confidence for real-world implementation status; non-interventional and not a treatment-efficacy study |


*Table: This table summarizes the strongest available evidence across clinical, mechanistic, therapeutic, and implementation domains for TANGO2 deficiency disorder. It highlights where the evidence is strongest and where major limitations remain.*

## 1. Disease information

### Definition and identifiers

TDD is an **autosomal-recessive metabolic encephalomyopathic and arrhythmia syndrome** caused by biallelic pathogenic variants in **TANGO2**. Open Targets maps it to **MONDO:0018820**, “recurrent metabolic encephalomyopathic crises–rhabdomyolysis–cardiac arrhythmia–intellectual disability syndrome,” associated with TANGO2/ENSG00000183597. The phenotype is cited as **OMIM/MIM 616878**. (OpenTargets Search: TANGO2 deficiency disorder-TANGO2, heiman2022mitochondrialdysfunctionassociated pages 1-2)

Common names include:

- TANGO2 deficiency disorder/disease;
- TANGO2-related disorder;
- TANGO2-related metabolic encephalomyopathic crises;
- metabolic encephalomyopathic crises, recurrent, with rhabdomyolysis, cardiac arrhythmias, and neurodegeneration;
- TANGO2-related metabolic encephalopathy and arrhythmias, sometimes abbreviated TRMEA;
- recurrent metabolic encephalomyopathic crises–rhabdomyolysis–cardiac arrhythmia–intellectual disability syndrome.

No disease-specific ICD-10, ICD-11, or MeSH identifier was established in the retrieved evidence; clinical coding generally requires phenotype-level codes for genetic/metabolic disease, rhabdomyolysis, arrhythmia, epilepsy, developmental disorder, or hypothyroidism. A dedicated SNOMED CT concept was likewise not verified.

**Evidence granularity.** The literature combines individual medical records and biospecimens with aggregated disease-level resources. Human cohorts are retrospective or observational and include 9-, 14-, 20-, 27-, and 73-patient series; experimental evidence comes from patient fibroblasts/myoblasts, HepG2 cells, patient-derived iPSC cardiomyocytes, Drosophila, zebrafish, and mice. (miyake2022cardiaccrisescardiac pages 1-2, berat2021clinicalandbiological pages 12-17, dines2019tango2expandingthe pages 5-6, mingirulli2020clinicalpresentationand pages 1-2, sandkuhler2026crossspeciesevaluationof pages 15-16)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factors

The necessary cause is **biallelic germline pathogenic variation in TANGO2**, usually resulting in absent or severely reduced protein/function. Environmental agents do not independently cause the Mendelian disorder. Rather, they reveal the latent metabolic vulnerability and determine crisis timing and severity. (heiman2022mitochondrialdysfunctionassociated pages 1-2, owlett2024multicenterappraisalof pages 1-3)

### Genetic risk factors

Reported pathogenic classes include multiexon deletions, nonsense, frameshift, canonical splice, small in-frame deletion, and missense variants. Important examples are the recurrent **exon 3–9 deletion**, **c.460G>A (p.Gly154Arg)**, **c.262C>T (p.Arg88\*)**, **c.220A>C (p.Thr74Pro)**, **c.380+1G>A**, and **c.711-3C>G**, the last experimentally associated with aberrant splicing. In one early dataset, the exon 3–9 deletion was prominent among European-ancestry cases, whereas p.Gly154Arg was recurrent in Hispanic/Latino cases; these are ancestry-associated observations, not universal founder-frequency estimates. (berat2021clinicalandbiological pages 12-17, mingirulli2020clinicalpresentationand pages 2-3, dines2019tango2expandingthe pages 5-6, mingirulli2020clinicalpresentationand pages 1-2)

TANGO2 lies in the recurrently deleted 22q11.2/DiGeorge region. A person with a 22q11.2 deletion that removes one TANGO2 allele is at risk of TDD if the remaining allele carries a pathogenic variant. A 2024 multicenter study screened 435 people with 22q11.2 deletion syndrome: 21 met symptom-based testing criteria, 9 underwent sequencing/deletion-duplication analysis, and none was confirmed, illustrating both low absolute yield and the danger of symptom overlap. (owlett2024multicenterappraisalof pages 1-3)

### Environmental and lifestyle risk factors

Established crisis triggers are intercurrent illness—especially febrile or viral illness—fasting, dehydration, reduced intake, heat, and physical exertion. Selected anesthetic exposures and possibly carnitine supplementation were proposed as additional triggers in a 20-patient cohort; these observations require cautious interpretation and specialist review rather than blanket contraindication. (kim2023intrinsicandextrinsic pages 1-3, NCT05374616 chunk 1, berat2021clinicalandbiological pages 1-7)

Smoking, alcohol, pollution, occupational exposure, radiation, and chronic dietary patterns have no demonstrated etiologic role. Infectious organisms are **triggers**, not causal pathogens, and TDD is not communicable.

### Protective factors

Avoiding prolonged fasting and dehydration, prompt treatment of illness, early carbohydrate-containing fluids plus complete nutrition, and avoidance of unnecessary heat/exertional stress during illness are clinically plausible protective measures. Glucose-containing fluids alone did not reliably prevent cardiac crisis; adequate feeding and micronutrient provision appear important. (miyake2022cardiaccrisescardiac pages 8-9)

B-complex or multivitamin supplementation is the leading candidate environmental protective factor. Human support remains observational, while B5 and B9 have direct rescue evidence in model systems. No protective TANGO2 allele or validated modifier gene has been identified. Intrafamilial variability strongly suggests modifiers, but none is established. (heiman2022mitochondrialdysfunctionassociated pages 1-2, xu2024folateasa pages 1-2, asadi2023vitaminb5a pages 8-9)

### Gene–environment causal interaction

A useful causal model is:

**biallelic TANGO2 loss → impaired lipid/acyl-CoA and membrane homeostasis ± mitochondrial/ER–Golgi dysfunction → reduced reserve in muscle, heart, and nervous system → fasting/illness/heat/exertion increases substrate demand and oxidative stress → rhabdomyolysis and metabolic decompensation → QT prolongation/cardiomyopathy → polymorphic VT, cardiac arrest, or death.** (kim2023intrinsicandextrinsic pages 1-3, lujan2023defectsinlipid pages 1-2)

## 3. Phenotypes

### Core phenotype frequencies and characteristics

In a 20-patient cohort, neurodevelopmental delay occurred in **17/20 (85%)**, acute metabolic crises in **17/20 (85%)**, and hypothyroidism in **12/20 (60%)**. Among the 17 with crises, rhabdomyolysis occurred in **15/17 (88%)**, neurologic manifestations in **14/17 (82%)**, and cardiac findings in **12/17 (71%)**. Long QT occurred in 10/17, Brugada-like pattern in 2/17, and arrhythmia in 6/17. (berat2021clinicalandbiological pages 1-7)

Suggested phenotype annotations follow; frequencies are cohort-specific.

- **Global developmental delay/intellectual disability**—usually infancy or childhood onset, variable severity, often progressive or worsened after crises; poor speech is common. Suggested HPO: *Global developmental delay* (HP:0001263), *Intellectual disability* (HP:0001249), *Delayed speech and language development* (HP:0000750). Progressive delay preceded crises in 14/20 in one series. (berat2021clinicalandbiological pages 12-17, mingirulli2020clinicalpresentationand pages 2-3)
- **Developmental regression/neurodegeneration**—episodic or progressive, sometimes crisis-associated; major effects on communication, schooling, independence, and caregiving burden. HPO: *Developmental regression* (HP:0002376), *Neurodevelopmental regression*.
- **Seizures/epilepsy**—childhood onset, variable and occasionally treatment-resistant; generalized and myoclonic forms are reported. HPO: *Seizure* (HP:0001250), *Generalized myoclonic seizure* (HP:0002123). (dołega2024clinicalspectrumdiagnosis pages 4-7)
- **Ataxia, gait abnormality, dysarthria, spasticity, dystonia, hypotonia**—chronic progressive or episodic, causing falls and loss of mobility. HPO: *Ataxia* (HP:0001251), *Gait disturbance* (HP:0001288), *Dysarthria* (HP:0001260), *Spasticity* (HP:0001257), *Dystonia* (HP:0001332), *Muscular hypotonia* (HP:0001252). (dołega2024clinicalspectrumdiagnosis pages 4-7, mingirulli2020clinicalpresentationand pages 2-3)
- **TANGO2 spells**—transient ataxia, weakness, and dyskinesia, often after waking; physical activity, heat, or reduced intake may trigger episodes lasting minutes to hours. Suggested HPO: *Episodic ataxia* (HP:0002131), *Episodic weakness*, *Dyskinesia*. (dołega2024clinicalspectrumdiagnosis pages 4-7)
- **Rhabdomyolysis/myalgia/weakness**—episodic and potentially severe, generally precipitated by metabolic stress. HPO: *Rhabdomyolysis* (HP:0003201), *Myalgia* (HP:0003326), *Muscle weakness* (HP:0001324), *Myoglobinuria* (HP:0002913). Crisis CK has ranged from 419 to 400,000 U/L in reported cohorts; one French case reached 43,670 IU/L. (kim2023intrinsicandextrinsic pages 1-3, berat2021clinicalandbiological pages 12-17, mingirulli2020clinicalpresentationand pages 2-3)
- **Metabolic crisis/encephalopathy**—acute and episodic, with hypoglycemia, lactic/metabolic acidosis, hyperammonemia, elevated transaminases, and sometimes coma. HPO: *Hypoglycemia* (HP:0001943), *Lactic acidosis* (HP:0003128), *Hyperammonemia* (HP:0001987), *Encephalopathy* (HP:0001298), *Elevated serum creatine kinase* (HP:0003236). Baseline metabolic studies may be normal between episodes. (heiman2022mitochondrialdysfunctionassociated pages 1-2, berat2021clinicalandbiological pages 12-17)
- **QT prolongation and ventricular arrhythmia**—episodic, crisis-linked, rapidly life-threatening. HPO: *Prolonged QT interval* (HP:0001657), *Ventricular tachycardia* (HP:0004756), *Torsade de pointes* (HP:0001664), *Cardiac arrest* (HP:0001695). In 43 severe admissions involving 27 patients, QTc prolongation was universal, median QTc **547 ms**, VT occurred in **78%**, and cardiac arrest in **74%**. (miyake2022cardiaccrisescardiac pages 1-2)
- **Cardiomyopathy/ventricular dysfunction**—usually crisis-associated and potentially reversible, but severe cases require ECMO or rarely transplantation. HPO: *Cardiomyopathy* (HP:0001638), *Decreased left ventricular ejection fraction* (HP:0012664). It occurred in **70%** of severe cardiac-crisis admissions. (miyake2022cardiaccrisescardiac pages 1-2)
- **Hypothyroidism/TSH elevation**—chronic, variable, treatable. HPO: *Hypothyroidism* (HP:0000821), *Elevated thyroid-stimulating hormone* (HP:0002925). TSH elevation occurred in 8/9 patients in one series and hypothyroidism in 12/20 in another. (mingirulli2020clinicalpresentationand pages 2-3, berat2021clinicalandbiological pages 1-7)
- **Feeding difficulty**—chronic and functionally important; 8/14 had gastrointestinal/feeding involvement in one cohort, sometimes requiring gastrostomy. HPO: *Feeding difficulties* (HP:0011968), *Gastrostomy tube feeding*. (dines2019tango2expandingthe pages 5-6)
- **Neuroimaging abnormalities**—variable ventriculomegaly, cerebral/white-matter atrophy, white-matter change, or microcephaly. MRI was abnormal in 9/16 in one cohort. HPO: *Cerebral atrophy* (HP:0002059), *Ventriculomegaly* (HP:0002119), *Abnormal cerebral white matter morphology* (HP:0002500), *Progressive microcephaly* (HP:0000253). (berat2021clinicalandbiological pages 12-17)
- **Hearing impairment** is reported but insufficiently quantified. HPO: *Hearing impairment* (HP:0000365). (dołega2024clinicalspectrumdiagnosis pages 4-7)

No validated TDD-specific EQ-5D, SF-36, PROMIS, or quality-of-life dataset was identified. Nevertheless, recurrent ICU admission, neurodevelopmental disability, epilepsy, feeding support, mobility loss, and sudden-death risk imply major patient and caregiver burden.

## 4. Genetic and molecular information

**Causal gene:** **TANGO2**, approved name *transport and Golgi organization 2 homolog*; Ensembl **ENSG00000183597**; chromosome **22q11.21**. The retrieved sources did not provide a verified HGNC numerical identifier, so none is inferred. (OpenTargets Search: TANGO2 deficiency disorder-TANGO2, heiman2022mitochondrialdysfunctionassociated pages 1-2)

Pathogenic variants are constitutional/germline and usually act through **loss of function**. Somatic causation, gain of function, dominant-negative effects, repeat expansions, mitochondrial-DNA variants, and epigenetic silencing are not established. Pathogenic/likely pathogenic classification should be assigned per ACMG/AMP using population rarity, segregation, predicted loss of function, RNA/protein findings, and phenotype concordance; individual ClinVar classifications must be checked against the current record at testing time.

Large deletions can involve exons 3–9 or arise as part of a broader 22q11.2 deletion. This makes copy-number analysis essential. The allele frequency estimates cited in an early clinical report—approximately 0.0013 for the 34-kb exon 3–9 deletion and 0.0026 for p.Gly154Arg—were ancestry-specific database observations and should not be treated as global carrier frequencies. (mingirulli2020clinicalpresentationand pages 2-3)

No validated modifier gene, protective allele, anticipation, or recurrent germline mosaicism mechanism is known. No disease-specific methylation signature or other epigenetic biomarker was identified. Variable expressivity within families is well documented. (heiman2022mitochondrialdysfunctionassociated pages 1-2, dines2019tango2expandingthe pages 5-6)

## 5. Environmental information

No toxin, radiation, pollution, occupational exposure, smoking, alcohol, or pathogen causes TDD. Fever/infection, fasting, dehydration, heat, exertion, and reduced intake are clinically important **precipitants**. Infectious-agent identity is generally less important than the associated catabolic state. Certain anesthetics were proposed as triggers; perioperative planning should therefore involve metabolic, anesthesia, and cardiology specialists. (kim2023intrinsicandextrinsic pages 1-3, berat2021clinicalandbiological pages 1-7)

Ordinary exercise has no demonstrated long-term preventive benefit and vigorous exertion during illness or fasting may be hazardous. Nutritional regularity and avoidance of catabolism are more relevant than a disease-specific macronutrient diet. No evidence supports tobacco/alcohol counseling as disease-specific therapy beyond general health recommendations.

## 6. Mechanism and pathophysiology

### Current mechanistic model

**Upstream:** TANGO2 loss disturbs acyl-CoA/lipid handling and endomembrane organization. In TANGO2-deficient HepG2 cells and patient fibroblasts, lipidomics showed increased lysophosphatidic acid, decreased phosphatidic acid, reduced cardiolipin, and enlarged lipid droplets. The proposed biochemical lesion is insufficient acyl-CoA availability for LPA acylation to PA. (lujan2023defectsinlipid pages 1-2)

**Intermediate:** altered phospholipid and neutral-lipid composition impairs membrane integrity, lipid-droplet catabolism, mitochondrial membranes, ER/SR–Golgi trafficking, and fatty-acid utilization. Patient cells show delayed ER-to-Golgi transport, altered ER morphology, decreased stress oxygen consumption/ATP, impaired oleate or palmitate oxidation in some systems, and increased superoxide/ROS. Proteomics implicates fatty-acid oxidation, amino-acid metabolism, plasma membrane, ER–Golgi, and secretory pathways. (heiman2022mitochondrialdysfunctionassociated pages 1-2, kim2023intrinsicandextrinsic pages 1-3)

**Downstream:** nutrient deprivation or illness intensifies substrate shortage and oxidative stress, causing lipid peroxidation and energetic/membrane failure. Skeletal myofibers undergo necrosis/rhabdomyolysis; cardiomyocytes develop repolarization instability, QT prolongation, ventricular dysfunction, and VT; neural cells likely undergo episodic dysfunction and cumulative injury, producing encephalopathy, seizures, ataxia, and regression. (kim2023intrinsicandextrinsic pages 3-5, lujan2023defectsinlipid pages 1-2)

This framework reconciles conflicting energetic studies: one 20-patient investigation found no evidence of a constitutive primary energetic defect and largely normal baseline acylcarnitines/FGF21, whereas fibroblast and muscle models detect abnormalities under metabolic stress. Thus TDD is best viewed as a **stress-sensitive lipid/membrane homeostasis disorder with secondary, context-dependent mitochondrial dysfunction**, not a proven primary respiratory-chain enzyme deficiency. (berat2021clinicalandbiological pages 12-17, berat2021clinicalandbiological pages 1-7, heiman2022mitochondrialdysfunctionassociated pages 1-2)

### Localization and protein function

TANGO2 has been detected predominantly at mitochondria and at mitochondria–ER–lipid-droplet contact regions in some mammalian systems; other work supports endomembrane, cytosolic, SR, Golgi, or mixed localization. Antibody and fusion-protein limitations contribute to disagreement. A direct acyl-CoA-binding function is plausible but was not definitively established by the 2023 studies retrieved here. Heme trafficking by homologues is an active comparative hypothesis, not yet a settled explanation for human TDD. (heiman2022mitochondrialdysfunctionassociated pages 1-2, kim2023intrinsicandextrinsic pages 3-5, lujan2023defectsinlipid pages 1-2, sandkuhler2026crossspeciesevaluationof pages 15-16)

### Suggested ontology annotations

- **GO biological process:** intracellular lipid transport; phospholipid biosynthetic process; glycerolipid metabolic process; fatty-acid beta-oxidation; ER-to-Golgi vesicle-mediated transport; mitochondrial ATP synthesis; response to oxidative stress; regulation of membrane organization; skeletal-muscle tissue development.
- **GO cellular component:** mitochondrion; mitochondrial membrane; endoplasmic reticulum; Golgi apparatus; lipid droplet; sarcoplasmic reticulum; mitochondrion-associated ER membrane.
- **Cell Ontology:** skeletal muscle fiber/myocyte (**CL:0000187**); cardiomyocyte (**CL:0000746**); fibroblast (**CL:0000057**); neuron (**CL:0000540**); hepatocyte (**CL:0000182**).

### Molecular profiling and advanced technologies

- **Proteomics:** broad changes in mitochondrial fatty-acid oxidation, ER–Golgi, plasma-membrane, amino-acid-metabolism, and secretory proteins. (mingirulli2020clinicalpresentationand pages 1-2, heiman2022mitochondrialdysfunctionassociated pages 1-2)
- **Lipidomics:** increased LPA, decreased PA/cardiolipin, enlarged lipid droplets, glycerolipid abnormalities, and enhanced stress sensitivity. (kim2023intrinsicandextrinsic pages 1-3, lujan2023defectsinlipid pages 1-2)
- **Metabolomics:** no validated diagnostic plasma signature; acylcarnitines and lactate may be normal between crises. (berat2021clinicalandbiological pages 12-17)
- **iPSC electrophysiology/CRISPR:** patient-derived cardiomyocytes recapitulated arrhythmia; wild-type TANGO2 expression or CRISPR correction rescued electrophysiology, supporting causality. (xu2024folateasa pages 1-2)
- No replicated single-cell, spatial-transcriptomic, or integrated human multi-omics atlas was identified through 2024.

Relevant abstract quotation from Lujan et al. (published March 2023): **“Quantitative lipidomics revealed a marked increase in lysophosphatidic acid (LPA) and a concomitant decrease in its biosynthetic precursor phosphatidic acid (PA).”** (lujan2023defectsinlipid pages 1-2)

## 7. Anatomical structures affected

Primary systems are:

- **Nervous system:** brain/cerebral white matter, cerebellar and motor networks; developmental, epileptic, ataxic, and movement phenotypes. Suggested UBERON: brain (**UBERON:0000955**), cerebral white matter (**UBERON:0002437**), cerebellum (**UBERON:0002037**).
- **Skeletal muscle:** recurrent myofiber injury and rhabdomyolysis. UBERON: skeletal muscle tissue (**UBERON:0001134**); CL: skeletal muscle fiber (**CL:0000187**).
- **Heart:** ventricular myocardium and cardiac conduction/repolarization system. UBERON: heart (**UBERON:0000948**), myocardium (**UBERON:0002349**); CL: cardiomyocyte (**CL:0000746**).
- **Thyroid:** frequent hypothyroidism/TSH elevation. UBERON: thyroid gland (**UBERON:0002046**).
- **Kidney:** secondary risk from myoglobinuria and severe rhabdomyolysis rather than proven primary renal disease. UBERON: kidney (**UBERON:0002113**).
- **Liver/metabolic compartment:** transaminase elevation and biochemical decompensation occur during crises; direct chronic hepatopathy is not established.

Subcellular structures include mitochondria, ER/SR, Golgi, lipid droplets, and organelle contact sites. No characteristic lateralization is reported; disease is systemic/bilateral.

## 8. Temporal development

Onset is usually infancy or childhood, reported from **4 months to 8 years**. Neurodevelopmental or muscle abnormalities often precede the first metabolic/cardiac crisis. (dołega2024clinicalspectrumdiagnosis pages 1-4, mingirulli2020clinicalpresentationand pages 2-3)

The course is lifelong and combines:

1. a chronic neurodevelopmental phenotype;
2. intermittent spells and metabolic crises;
3. cumulative or stepwise neurologic regression in some patients;
4. potentially reversible crisis-associated cardiac dysfunction;
5. persistent risk of sudden death.

There is no formal stage system. A practical clinical staging model is **baseline/stable**, **prodromal catabolic illness**, **metabolic/rhabdomyolysis crisis**, and **cardiac crisis/recovery**. Critical intervention windows are the earliest phase of illness or fasting, the onset of CK/QTc elevation, and the period before ventricular ectopy progresses to VT. Spontaneous genetic remission does not occur; crisis manifestations can resolve, but developmental disability generally persists.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Parents are usually heterozygous carriers; each pregnancy has a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability when both parental variants are known. Penetrance for biallelic severe loss-of-function appears high, but age-dependent penetrance for individual manifestations and marked variable expressivity complicate counseling.

Consanguinity can increase risk for homozygous alleles but is not required. Founder/population enrichment has been reported for the exon 3–9 deletion in European-ancestry cases, p.Gly154Arg in Hispanic/Latino cases, and exon 4–6 deletion in some Arab families. These patterns require confirmation in population-scale datasets. (heiman2022mitochondrialdysfunctionassociated pages 1-2, mingirulli2020clinicalpresentationand pages 2-3)

A 2024 paper cited a carrier rate near **1 in 350**; the same review literature estimated prevalence near **1 per million** and approximately 8,000 affected persons worldwide. These figures are uncertain extrapolations, not registry-derived incidence estimates. No reliable annual incidence, sex ratio, or geographic prevalence map exists. Both sexes are affected; no sex-linked mechanism is expected. (owlett2024multicenterappraisalof pages 1-3, dołega2024clinicalspectrumdiagnosis pages 1-4)

There is no repeat-mediated anticipation. Germline mosaicism is theoretically possible for any de novo event but is not a recognized major feature. Cascade testing is appropriate for siblings and extended relatives when familial variants are known.

## 10. Diagnostics

### When to suspect TDD

Suspect TDD in a child with developmental delay, regression, episodic ataxia or weakness, seizures, unexplained CK elevation/rhabdomyolysis, hypoglycemia/lactic acidosis during illness, hypothyroidism, QT prolongation, Brugada-like pattern, or ventricular arrhythmia—especially when several coexist. Consider it specifically in symptomatic individuals with 22q11.2 deletion syndrome. (owlett2024multicenterappraisalof pages 1-3, miyake2022cardiaccrisescardiac pages 1-2)

### Acute clinical testing

During illness/crisis, obtain serial:

- CK, electrolytes including magnesium and calcium, glucose, blood gas/bicarbonate, lactate, ammonia, AST/ALT, renal function, urinalysis/myoglobin;
- continuous ECG/telemetry with repeated QTc assessment;
- echocardiography and ventricular-function monitoring;
- EEG for encephalopathy or seizure;
- brain MRI for regression, focal findings, or unexplained neurologic progression.

Normal baseline acylcarnitines, amino acids, lactate, carnitine, or respiratory-chain studies do **not** exclude TDD. No validated enzyme assay or circulating biomarker exists. Western blot or research fibroblast functional testing can support loss of protein/function but is not the standard definitive test. (berat2021clinicalandbiological pages 12-17, dołega2024clinicalspectrumdiagnosis pages 4-7)

### Genetic testing strategy

1. Use a neurodevelopmental/epilepsy, rhabdomyolysis/metabolic, cardiomyopathy/arrhythmia, or comprehensive Mendelian panel that explicitly includes **TANGO2**.
2. Require both sequence analysis and exon-level deletion/duplication analysis because multiexon deletions are common.
3. If panel testing is negative or phenotype is atypical, use trio WES or WGS with copy-number and structural-variant calling.
4. In a person with 22q11.2 deletion and suggestive features, sequence and assess copy number of the remaining TANGO2 allele.
5. Confirm phase/segregation in parents and apply ACMG/AMP criteria. RNA analysis may clarify splice variants.

Chromosomal microarray can detect a 22q11.2 deletion or sufficiently large TANGO2 deletion but may miss small exon-level or sequence variants. Karyotype and FISH are not adequate stand-alone tests; mtDNA and repeat-expansion testing are not indicated unless the differential independently warrants them.

### Differential diagnosis

Consider fatty-acid oxidation disorders, mitochondrial cytopathies, glycogen-storage/metabolic myopathies, RYR1- and LPIN1-related rhabdomyolysis, PNKD, channelopathies/long-QT syndromes, Brugada syndrome, CPVT, epilepsy syndromes, and primary 22q11.2 deletion syndrome. TDD is distinguished by the combined neurodevelopmental–rhabdomyolysis–metabolic–arrhythmic phenotype and biallelic TANGO2 variants.

There are no universally validated clinical diagnostic criteria independent of molecular confirmation. No routine newborn biochemical screen exists. DNA-first newborn screening has been discussed because TDD lacks a reliable dried-blood-spot biochemical footprint, but evidence and implementation criteria remain insufficient. (dołega2024clinicalspectrumdiagnosis pages 1-4)

## 11. Outcome and prognosis

Population-level survival curves, 5-/10-year survival, and life expectancy are unavailable. Prognosis is highly variable and influenced by crisis frequency, early recognition, nutritional status, and access to intensive cardiac support.

Historical small cohorts demonstrate substantial mortality. In a 14-patient series, **5/14 died**, four primarily from arrhythmia. In the severe cardiac-crisis cohort, **10/27 (37%)** died, six from arrhythmia; these are referral-enriched estimates and overstate risk for all diagnosed patients. (miyake2022cardiaccrisescardiac pages 1-2, dines2019tango2expandingthe pages 5-6)

During severe cardiac crises, cardiomyopathy occurred in 70%, cardiac arrest in 74%, and VT in 78%. ECMO-supported survival from arrhythmia was reported in 5/6 supported patients, suggesting that aggressive escalation can be lifesaving. (miyake2022cardiaccrisescardiac pages 1-2)

Long-term morbidity includes intellectual and speech impairment, epilepsy, ataxia/spasticity/dystonia, mobility limitations, feeding dependence, recurrent hospitalization, and anxiety related to unpredictable crises. Acute kidney injury can follow severe rhabdomyolysis. Prognostic biomarkers beyond clinical trajectory, CK, QTc, ventricular function, and crisis burden are not validated.

## 12. Treatment and real-world implementation

There is no approved curative or genotype-replacing therapy. Care should be coordinated by metabolic genetics, cardiology/electrophysiology, neurology, endocrinology, nutrition, rehabilitation, and intensive care.

### Baseline and preventive management

- Regular meals and avoidance of prolonged fasting/dehydration.
- Written emergency/sick-day plan and early hospital evaluation for fever, reduced intake, weakness, dark urine, seizure, or palpitations.
- B-complex or multivitamin supplementation containing B5 and folate is increasingly used in practice, but dose, formulation, and efficacy are not trial-standardized.
- Periodic ECG, thyroid testing, neurologic/developmental assessment, and individualized CK/cardiac surveillance.

Suggested MAXO concepts: genetic counseling; dietary management; vitamin supplementation; electrocardiographic monitoring; echocardiography; thyroid-function monitoring.

### Acute metabolic/cardiac crisis

Provide prompt dextrose-containing fluids while restoring full enteral or parenteral nutrition, correct electrolytes, monitor CK/renal status, avoid QT-prolonging agents, and use continuous telemetry with frequent echocardiography. Glucose alone may be insufficient. Early nutrition, including micronutrients, is emphasized. (miyake2022cardiaccrisescardiac pages 8-9)

For malignant arrhythmia, reported strategies include IV magnesium, isoproterenol, overdrive atrial pacing, intensive electrolyte correction, and ECMO for refractory instability. Amiodarone and lidocaine were reported as potentially ineffective or aggravating in this specific crisis physiology; drug selection should be directed by a specialist TDD electrophysiology team rather than generic long-QT algorithms. (dołega2024clinicalspectrumdiagnosis pages 4-7, miyake2022cardiaccrisescardiac pages 8-9)

Suggested MAXO concepts: intravenous fluid therapy; glucose administration; electrolyte replacement; continuous cardiac monitoring; temporary cardiac pacing; extracorporeal membrane oxygenation; mechanical ventilation; renal-function monitoring.

### Symptom-directed treatment

- **Epilepsy:** levetiracetam or valproate have been used; selection should account for metabolic and cardiac safety.
- **Spasticity/dystonia:** baclofen, clonazepam, botulinum toxin, plus physical/occupational therapy.
- **Hypothyroidism:** levothyroxine.
- **Feeding/speech/mobility:** nutrition support, gastrostomy when necessary, speech therapy, PT/OT, orthotics and assistive devices.
- **Heart failure during crisis:** conventional ICU inotropes and heart-failure medications are individualized; rare severe cardiomyopathy has required transplantation. (dołega2024clinicalspectrumdiagnosis pages 4-7)

### B-vitamin evidence

**Vitamin B5/pantothenate—preclinical:** In Drosophila, 2–4 mM B5 approximately doubled median starvation survival (~25 versus 12 hours), reduced heat-induced seizures by about 95%, prolonged seizure latency, and improved locomotor/behavioral measures. It restored ER-to-Golgi transport toward control rates in human TANGO2-deficient fibroblasts. The study’s abstract states: **“vitamin B5 specifically improves multiple defects associated with TANGO2 loss-of-function in Drosophila and rescues membrane trafficking defects in human cells.”** (asadi2023vitaminb5a pages 6-8, asadi2023vitaminb5a pages 1-3)

**Folate/B9—iPSC cardiomyocytes:** High-dose folate “virtually abolishes arrhythmias” in patient-derived iPSC cardiomyocytes; methotrexate blocked the benefit, supporting a requirement for intracellular folate metabolism. Wild-type TANGO2 expression and CRISPR correction also rescued the electrophysiologic phenotype. Human clinical support is observational, not randomized. (xu2024folateasa pages 1-2)

The apparently different B5-versus-B9 findings likely reflect assay and tissue specificity: B5 was strongest for fly systemic/trafficking phenotypes, whereas B9 was strongest in cardiomyocyte electrophysiology. A B-complex strategy may therefore be more rational than assuming a single active vitamin, but efficacy, dose, and toxicity require prospective study.

### Experimental therapies and trials

No interventional gene, cell, RNA, CRISPR, or controlled drug trial was identified. **NCT05374616** is a recruiting observational natural-history and biorepository study at Baylor, planned enrollment 300, started May 2018, estimated completion January 2030; it tracks metabolic/cardiac crises and collects blood, saliva, and fibroblasts. URL: https://clinicaltrials.gov/study/NCT05374616. (NCT05374616 chunk 1)

No TDD-specific pharmacogenomic rule is established.

## 13. Prevention

**Primary prevention of inherited disease:** impossible after conception through lifestyle modification. Options for at-risk families include carrier testing, partner testing, preimplantation genetic testing, prenatal diagnosis, donor gametes, and informed reproductive planning.

**Secondary prevention:** cascade testing of siblings/relatives and molecular diagnosis before a first crisis; targeted testing in symptomatic people with 22q11.2 deletion; possible future DNA-first newborn screening. Population newborn screening is not currently established. (owlett2024multicenterappraisalof pages 1-3, dołega2024clinicalspectrumdiagnosis pages 1-4)

**Tertiary prevention:** avoid fasting/dehydration, institute sick-day plans, provide early nutrition and B-complex supplementation under clinical supervision, monitor QTc and thyroid function, treat seizures/movement disorders, and prepare rapid escalation pathways for pacing/ECMO. Vaccination according to routine schedules may indirectly reduce febrile illnesses but is not TDD-specific immunotherapy.

Genetic counseling should explain autosomal-recessive recurrence, variable expressivity, limitations of prognosis, and the need to test deletion/duplication as well as sequence variants.

## 14. Other species and natural disease

No naturally occurring veterinary TANGO2-deficiency syndrome or breed predisposition was established in the retrieved evidence. There is no transmission or zoonotic potential.

Orthologues/homologues have been studied in:

- *Drosophila melanogaster*—NCBI Taxon **7227**;
- *Danio rerio*—Taxon **7955**;
- *Mus musculus*—Taxon **10090**;
- *Caenorhabditis elegans*—Taxon **6239**;
- yeast and bacterial homologues in comparative biochemical work.

Evolutionary conservation supports roles in lipid/endomembrane biology and possibly heme handling, but the homologues are not functionally identical. Orthologue-specific NCBI Gene and VBO identifiers were not verified in the retrieved records and should be sourced directly before database ingestion.

## 15. Model organisms and experimental systems

### Drosophila

Loss-of-function flies reproduce starvation sensitivity, heat-induced seizure susceptibility, impaired climbing/locomotion, learning deficits, and altered behavior. B5 robustly rescues several phenotypes; B3 provides weaker rescue. Advantages are rapid whole-organism stress and supplementation assays; limitations include a non-mammalian heart and incomplete correspondence to human neurodevelopment. (asadi2023vitaminb5a pages 6-8, asadi2023vitaminb5a pages 1-3)

### Zebrafish

Mutants show growth impairment, smaller myofibers, abnormal glycerolipid pathways, stress-induced skeletal-muscle injury, early lethality, and approximately 96% mortality by three months in one model. Tango2 localizes near SR, Golgi, and mitochondria. This model is well suited to rhabdomyolysis, lipidomics, environmental triggers, and high-throughput rescue studies, but does not reproduce every human cardiac/neurodevelopmental feature. (kim2023intrinsicandextrinsic pages 1-3, kim2023intrinsicandextrinsic pages 3-5)

### Mouse

Reported knockout mice have relatively normal development, lifespan, and gross physiology, making them a poor constitutive phenocopy under standard conditions. Stress paradigms, tissue-specific knockouts, or sensitized backgrounds may be needed. (kim2023intrinsicandextrinsic pages 3-5, casey2022glycerolipiddefectsin pages 1-5)

### Human cellular models

Patient fibroblasts and myoblasts permit trafficking, lipidomic, respiration, ROS, and nutrient-stress studies but may not model excitable tissues. Patient-derived iPSC cardiomyocytes reproduce electrophysiologic abnormalities and respond to wild-type gene replacement, CRISPR correction, and folate, making them the most disease-proximal current arrhythmia platform. (xu2024folateasa pages 1-2, heiman2022mitochondrialdysfunctionassociated pages 1-2)

No validated cerebral organoid, skeletal-muscle organoid, single-cell disease atlas, or spatial-transcriptomic model was identified through 2024.

## Evidence-weighted conclusions

1. **Established:** TDD is a biallelic TANGO2 loss-of-function disorder with high-risk stress-triggered rhabdomyolysis and ventricular arrhythmia superimposed on a variable neurodevelopmental syndrome.
2. **Strong clinical signal:** QT prolongation is nearly universal during severe cardiac crises, and VT, cardiac arrest, cardiomyopathy, and mortality are common in crisis-enriched cohorts. (miyake2022cardiaccrisescardiac pages 1-2)
3. **Best current mechanism:** impaired lipid/acyl-CoA and membrane homeostasis with secondary stress-dependent mitochondrial and trafficking dysfunction; a simple primary respiratory-chain defect is inadequate. (berat2021clinicalandbiological pages 1-7, lujan2023defectsinlipid pages 1-2)
4. **Most important recent therapeutic development:** convergent B-vitamin rescue evidence—B5 for systemic/trafficking defects and B9 for cardiomyocyte arrhythmia—plus observational human protection. It is promising but not yet randomized-trial evidence. (asadi2023vitaminb5a pages 6-8, xu2024folateasa pages 1-2)
5. **Knowledge gaps:** true prevalence, penetrance by genotype, modifier genes, prospective treatment effects/doses, validated biomarkers, standardized acute protocols, and faithful mammalian models.

### Key recent sources and URLs

- Xu et al., **June 2024**, *JCI Insight*, “Folate as a potential treatment…” https://doi.org/10.1172/jci.insight.171005. (xu2024folateasa pages 1-2)
- Owlett et al., **June 2024**, *American Journal of Medical Genetics A*, 22q11.2 screening appraisal: https://doi.org/10.1002/ajmg.a.63778. (owlett2024multicenterappraisalof pages 1-3)
- Dołęga et al., **August 2024**, clinical review: https://doi.org/10.12775/qs.2024.21.54001. (dołega2024clinicalspectrumdiagnosis pages 1-4)
- Asadi et al., **2023**, vitamin B5 rescue: https://doi.org/10.1002/jimd.12579. (asadi2023vitaminb5a pages 6-8)
- Lujan et al., **March 2023**, lipid homeostasis: https://doi.org/10.7554/eLife.85345. (lujan2023defectsinlipid pages 1-2)
- Kim et al., **September 2023**, zebrafish/stress susceptibility: https://doi.org/10.1242/dmm.050092. (kim2023intrinsicandextrinsic pages 1-3)
- Miyake et al., **October 2022**, cardiac crises: https://doi.org/10.1016/j.hrthm.2022.05.009. (miyake2022cardiaccrisescardiac pages 1-2)
- Baylor natural-history study: https://clinicaltrials.gov/study/NCT05374616. (NCT05374616 chunk 1)

References

1. (heiman2022mitochondrialdysfunctionassociated pages 1-2): Paige Heiman, Al-Walid Mohsen, Anuradha Karunanidhi, Claudette St Croix, Simon Watkins, Erik Koppes, Richard Haas, Jerry Vockley, and Lina Ghaloul-Gonzalez. Mitochondrial dysfunction associated with tango2 deficiency. Scientific Reports, Feb 2022. URL: https://doi.org/10.1038/s41598-022-07076-9, doi:10.1038/s41598-022-07076-9. This article has 51 citations and is from a peer-reviewed journal.

2. (miyake2022cardiaccrisescardiac pages 1-2): Christina Y. Miyake, Erica J. Lay, Cheyenne M. Beach, Scott R. Ceresnak, Caridad M. Delauz, Taylor S. Howard, Christopher M. Janson, Kate Jardine, Prince J. Kannankeril, Maina Kava, Jeffrey J. Kim, Leonardo Liberman, Scott L. Macicek, Tam Dam Pham, Terry Robertson, Santiago O. Valdes, Gregory Webster, Sara B. Stephens, Diana M. Milewicz, Mahshid Azamian, Saad A. Ehsan, Kimberly M. Houck, Claudia Soler-Alfonso, Kevin E. Glinton, Mustafa Tosur, Na Li, Weiyi Xu, Seema R. Lalani, and Lilei Zhang. Cardiac crises: cardiac arrhythmias and cardiomyopathy during tango2 deficiency related metabolic crises. Heart Rhythm, 19:1673-1681, Oct 2022. URL: https://doi.org/10.1016/j.hrthm.2022.05.009, doi:10.1016/j.hrthm.2022.05.009. This article has 37 citations and is from a peer-reviewed journal.

3. (berat2021clinicalandbiological pages 1-7): Claire‐Marine Bérat, Sebastian Montealegre, Arnaud Wiedemann, Malou Le Corronc Nuzum, Amélie Blondel, Hugo Debruge, Aline Cano, Brigitte Chabrol, Célia Hoebeke, Michel Polak, Athanasia Stoupa, François Feillet, Stéphanie Torre, Nathalie Boddaert, Henri Bruel, Magalie Barth, Lena Damaj, Marie‐Thérèse Abi‐Wardé, Alexandra Afenjar, Jean‐François Benoist, Marine Madrange, Laure Caccavelli, Perrine Renard, Arnaud Hubas, Patrick Nusbaum, Clément Pontoizeau, Stéphanie Gobin, Peter van Endert, Chris Ottolenghi, Alice Maltret, and Pascale de Lonlay. Clinical and biological characterization of 20 patients with <scp>tango2</scp> deficiency indicates novel triggers of metabolic crises and no primary energetic defect. Sep 2020. URL: https://doi.org/10.1002/jimd.12314, doi:10.1002/jimd.12314. This article has 43 citations and is from a peer-reviewed journal.

4. (kim2023intrinsicandextrinsic pages 1-3): Euri S. Kim, Jennifer G. Casey, Brian S. Tao, Arian Mansur, Nishanthi Mathiyalagan, E. Diane Wallace, Brandie M. Ehrmann, and Vandana A. Gupta. Intrinsic and extrinsic regulation of rhabdomyolysis susceptibility by tango2. Disease Models &amp; Mechanisms, Sep 2023. URL: https://doi.org/10.1242/dmm.050092, doi:10.1242/dmm.050092. This article has 14 citations and is from a domain leading peer-reviewed journal.

5. (lujan2023defectsinlipid pages 1-2): Agustin Leonardo Lujan, Ombretta Foresti, Conor Sugden, Nathalie Brouwers, Alex Mateo Farre, Alessio Vignoli, Mahshid Azamian, Alicia Turner, Jose Wojnacki, and Vivek Malhotra. Defects in lipid homeostasis reflect the function of tango2 in phospholipid and neutral lipid metabolism. eLife, Mar 2023. URL: https://doi.org/10.7554/elife.85345, doi:10.7554/elife.85345. This article has 31 citations and is from a domain leading peer-reviewed journal.

6. (asadi2023vitaminb5a pages 6-8): Paria Asadi, Miroslav P. Milev, Djenann Saint‐Dic, Chiara Gamberi, and Michael Sacher. Vitamin b5, a coenzyme a precursor, rescues tango2 deficiency disease‐associated defects in <i>drosophila</i> and human cells. Journal of Inherited Metabolic Disease, 46:358-368, Dec 2023. URL: https://doi.org/10.1002/jimd.12579, doi:10.1002/jimd.12579. This article has 45 citations and is from a peer-reviewed journal.

7. (xu2024folateasa pages 1-2): Weiyi Xu, Yingqiong Cao, Sara B. Stephens, Maria Jose Arredondo, Yifan Chen, William Perez, Liang Sun, Andy C. Yu, Jean J. Kim, Seema R. Lalani, Na Li, Frank T. Horrigan, Francisco Altamirano, Xander H.T. Wehrens, Christina Y. Miyake, and Lilei Zhang. Folate as a potential treatment for lethal ventricular arrhythmias in tango2-deficiency disorder. JCI Insight, Jun 2024. URL: https://doi.org/10.1172/jci.insight.171005, doi:10.1172/jci.insight.171005. This article has 10 citations and is from a domain leading peer-reviewed journal.

8. (asadi2023vitaminb5a pages 8-9): Paria Asadi, Miroslav P. Milev, Djenann Saint‐Dic, Chiara Gamberi, and Michael Sacher. Vitamin b5, a coenzyme a precursor, rescues tango2 deficiency disease‐associated defects in <i>drosophila</i> and human cells. Journal of Inherited Metabolic Disease, 46:358-368, Dec 2023. URL: https://doi.org/10.1002/jimd.12579, doi:10.1002/jimd.12579. This article has 45 citations and is from a peer-reviewed journal.

9. (OpenTargets Search: TANGO2 deficiency disorder-TANGO2): Open Targets Query (TANGO2 deficiency disorder-TANGO2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (mingirulli2020clinicalpresentationand pages 2-3): Nadja Mingirulli, Angela Pyle, Denisa Hathazi, Charlotte L. Alston, Nicolai Kohlschmidt, Gina O'Grady, Leigh Waddell, Frances Evesson, Sandra B. T. Cooper, Christian Turner, Jennifer Duff, Ana Topf, Delia Yubero, Cristina Jou, Andrés Nascimento, Carlos Ortez, Angels García‐Cazorla, Claudia Gross, Maria O'Callaghan, Saikat Santra, Maryanne A. Preece, Michael Champion, Sergei Korenev, Efsthatia Chronopoulou, Majumdar Anirban, Germaine Pierre, Daniel McArthur, Kyle Thompson, Placido Navas, Antonia Ribes, Frederic Tort, Agatha Schlüter, Aurora Pujol, Raquel Montero, Georgia Sarquella, Hanns Lochmüller, Cecilia Jiménez‐Mallebrera, Robert W. Taylor, Rafael Artuch, Janbernd Kirschner, Sarah C. Grünert, Andreas Roos, and Rita Horvath. Clinical presentation and proteomic signature of patients with tango2 mutations. Journal of Inherited Metabolic Disease, 43:297-308, Aug 2019. URL: https://doi.org/10.1002/jimd.12156, doi:10.1002/jimd.12156. This article has 55 citations and is from a peer-reviewed journal.

11. (berat2021clinicalandbiological pages 12-17): Claire‐Marine Bérat, Sebastian Montealegre, Arnaud Wiedemann, Malou Le Corronc Nuzum, Amélie Blondel, Hugo Debruge, Aline Cano, Brigitte Chabrol, Célia Hoebeke, Michel Polak, Athanasia Stoupa, François Feillet, Stéphanie Torre, Nathalie Boddaert, Henri Bruel, Magalie Barth, Lena Damaj, Marie‐Thérèse Abi‐Wardé, Alexandra Afenjar, Jean‐François Benoist, Marine Madrange, Laure Caccavelli, Perrine Renard, Arnaud Hubas, Patrick Nusbaum, Clément Pontoizeau, Stéphanie Gobin, Peter van Endert, Chris Ottolenghi, Alice Maltret, and Pascale de Lonlay. Clinical and biological characterization of 20 patients with <scp>tango2</scp> deficiency indicates novel triggers of metabolic crises and no primary energetic defect. Sep 2020. URL: https://doi.org/10.1002/jimd.12314, doi:10.1002/jimd.12314. This article has 43 citations and is from a peer-reviewed journal.

12. (owlett2024multicenterappraisalof pages 1-3): Laura D. Owlett, Bianca Zapanta, Sarah E. Sandkuhler, Elizabeth G. Ames, Scott E. Hickey, Samuel J. Mackenzie, and Joshua K. Meisner. Multicenter appraisal of comorbid tango2 deficiency disorder in patients with 22q11.2 deletion syndrome. American Journal of Medical Genetics Part A, Jun 2024. URL: https://doi.org/10.1002/ajmg.a.63778, doi:10.1002/ajmg.a.63778. This article has 4 citations.

13. (kim2023intrinsicandextrinsic pages 3-5): Euri S. Kim, Jennifer G. Casey, Brian S. Tao, Arian Mansur, Nishanthi Mathiyalagan, E. Diane Wallace, Brandie M. Ehrmann, and Vandana A. Gupta. Intrinsic and extrinsic regulation of rhabdomyolysis susceptibility by tango2. Disease Models &amp; Mechanisms, Sep 2023. URL: https://doi.org/10.1242/dmm.050092, doi:10.1242/dmm.050092. This article has 14 citations and is from a domain leading peer-reviewed journal.

14. (asadi2023vitaminb5a pages 1-3): Paria Asadi, Miroslav P. Milev, Djenann Saint‐Dic, Chiara Gamberi, and Michael Sacher. Vitamin b5, a coenzyme a precursor, rescues tango2 deficiency disease‐associated defects in <i>drosophila</i> and human cells. Journal of Inherited Metabolic Disease, 46:358-368, Dec 2023. URL: https://doi.org/10.1002/jimd.12579, doi:10.1002/jimd.12579. This article has 45 citations and is from a peer-reviewed journal.

15. (NCT05374616 chunk 1): Seema Lalani. Natural History Study and Establishment of a Biorepository-TANGO2-related Disorder. Baylor College of Medicine. 2018. ClinicalTrials.gov Identifier: NCT05374616

16. (dines2019tango2expandingthe pages 5-6): Jennifer N. Dines, Katie Golden-Grant, Amy LaCroix, Alison M. Muir, Dianne Laboy Cintrón, Kirsty McWalter, Megan T. Cho, Angela Sun, J. Lawrence Merritt, Jenny Thies, Dmitriy Niyazov, Barbara Burton, Katherine Kim, Leah Fleming, Rachel Westman, Peter Karachunski, Joline Dalton, Alice Basinger, Can Ficicioglu, Ingo Helbig, Manuela Pendziwiat, Hiltrud Muhle, Katherine L. Helbig, Almuth Caliebe, René Santer, Kolja Becker, Sharon Suchy, Ganka Douglas, Francisca Millan, Amber Begtrup, Kristin G. Monaghan, and Heather C. Mefford. Tango2: expanding the clinical phenotype and spectrum of pathogenic variants. Genetics in Medicine, 21:601-607, Mar 2019. URL: https://doi.org/10.1038/s41436-018-0137-y, doi:10.1038/s41436-018-0137-y. This article has 67 citations and is from a highest quality peer-reviewed journal.

17. (mingirulli2020clinicalpresentationand pages 1-2): Nadja Mingirulli, Angela Pyle, Denisa Hathazi, Charlotte L. Alston, Nicolai Kohlschmidt, Gina O'Grady, Leigh Waddell, Frances Evesson, Sandra B. T. Cooper, Christian Turner, Jennifer Duff, Ana Topf, Delia Yubero, Cristina Jou, Andrés Nascimento, Carlos Ortez, Angels García‐Cazorla, Claudia Gross, Maria O'Callaghan, Saikat Santra, Maryanne A. Preece, Michael Champion, Sergei Korenev, Efsthatia Chronopoulou, Majumdar Anirban, Germaine Pierre, Daniel McArthur, Kyle Thompson, Placido Navas, Antonia Ribes, Frederic Tort, Agatha Schlüter, Aurora Pujol, Raquel Montero, Georgia Sarquella, Hanns Lochmüller, Cecilia Jiménez‐Mallebrera, Robert W. Taylor, Rafael Artuch, Janbernd Kirschner, Sarah C. Grünert, Andreas Roos, and Rita Horvath. Clinical presentation and proteomic signature of patients with tango2 mutations. Journal of Inherited Metabolic Disease, 43:297-308, Aug 2019. URL: https://doi.org/10.1002/jimd.12156, doi:10.1002/jimd.12156. This article has 55 citations and is from a peer-reviewed journal.

18. (sandkuhler2026crossspeciesevaluationof pages 15-16): Sarah E Sandkuhler, Kayla S Youngs, Laura Owlett, Monica B Bandora, Aaliya Naaz, Euri S Kim, Lili Wang, Andrew P Wojtovich, Vandana A Gupta, Michael Sacher, and Samuel J Mackenzie. Heme’s relevance genuine? re-visiting the roles of tango2 homologs including hrg-9 and hrg-10 in c. elegans. Apr 2026. URL: https://doi.org/10.7554/elife.105418, doi:10.7554/elife.105418.

19. (miyake2022cardiaccrisescardiac pages 8-9): Christina Y. Miyake, Erica J. Lay, Cheyenne M. Beach, Scott R. Ceresnak, Caridad M. Delauz, Taylor S. Howard, Christopher M. Janson, Kate Jardine, Prince J. Kannankeril, Maina Kava, Jeffrey J. Kim, Leonardo Liberman, Scott L. Macicek, Tam Dam Pham, Terry Robertson, Santiago O. Valdes, Gregory Webster, Sara B. Stephens, Diana M. Milewicz, Mahshid Azamian, Saad A. Ehsan, Kimberly M. Houck, Claudia Soler-Alfonso, Kevin E. Glinton, Mustafa Tosur, Na Li, Weiyi Xu, Seema R. Lalani, and Lilei Zhang. Cardiac crises: cardiac arrhythmias and cardiomyopathy during tango2 deficiency related metabolic crises. Heart Rhythm, 19:1673-1681, Oct 2022. URL: https://doi.org/10.1016/j.hrthm.2022.05.009, doi:10.1016/j.hrthm.2022.05.009. This article has 37 citations and is from a peer-reviewed journal.

20. (dołega2024clinicalspectrumdiagnosis pages 4-7): Marcin Dołęga, Piotr Gacka, Olrgierd Dróżdż, Joanna Gołda, Julia Mężyk, and Aleksandra Snopkowska. Clinical spectrum, diagnosis, and management of tango2 deficiency disorder: a comprehensive review. Quality in Sport, 21:54001, Aug 2024. URL: https://doi.org/10.12775/qs.2024.21.54001, doi:10.12775/qs.2024.21.54001. This article has 2 citations.

21. (dołega2024clinicalspectrumdiagnosis pages 1-4): Marcin Dołęga, Piotr Gacka, Olrgierd Dróżdż, Joanna Gołda, Julia Mężyk, and Aleksandra Snopkowska. Clinical spectrum, diagnosis, and management of tango2 deficiency disorder: a comprehensive review. Quality in Sport, 21:54001, Aug 2024. URL: https://doi.org/10.12775/qs.2024.21.54001, doi:10.12775/qs.2024.21.54001. This article has 2 citations.

22. (casey2022glycerolipiddefectsin pages 1-5): Jennifer G Casey, Euri S Kim, Brian S Tao, Arian Mansur, E. Diane Wallace, and Vandana A Gupta. Glycerolipid defects in skeletal muscle contribute to rhabdomyolysis in tango2 deficiency. bioRxiv, Nov 2022. URL: https://doi.org/10.1101/2022.11.12.516274, doi:10.1101/2022.11.12.516274. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](TANGO2_Deficiency_Disorder-deep-research-falcon_artifacts/artifact-00.md)