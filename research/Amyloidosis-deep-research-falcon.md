---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T18:50:22.344203'
end_time: '2026-07-05T19:21:25.261434'
duration_seconds: 1862.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Amyloidosis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 56
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Amyloidosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Amyloidosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Amyloidosis** covering all of the
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
- **Disease Name:** Amyloidosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Amyloidosis** covering all of the
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


# Comprehensive Research Report: Amyloidosis

## 1. Disease Information

### Overview
Amyloidosis is a heterogeneous group of diseases characterized by the pathological extracellular deposition of insoluble misfolded protein material called "amyloid" in tissues and organs (poli2023hereditarytransthyretinamyloidosis pages 1-2). These amyloid fibrils are ordered structures of 7–13 nm diameter with cross-β-sheet secondary structure that damage tissue organization and induce progressive organ dysfunction (ajmal2023proteinmisfoldingand pages 4-6). Over 30 types of amyloid fibrils have been identified in humans, but the clinically most important systemic forms are immunoglobulin light-chain (AL) amyloidosis, transthyretin (ATTR) amyloidosis (both hereditary/variant [ATTRv] and wild-type [ATTRwt]), and serum amyloid A (AA) amyloidosis (fontana2025thelastdecade pages 1-3, zanwar2023immunoglobulinlightchain pages 1-2).

### Key Identifiers
- **MONDO ID:** MONDO:0019065 (amyloidosis); MONDO:0018634 (hereditary amyloidosis); MONDO:0019438 (AL amyloidosis) (OpenTargets Search: amyloidosis)
- **ICD-10:** E85 (Amyloidosis), with subtypes E85.0–E85.9
- **OMIM:** #105210 (Amyloidosis, hereditary, transthyretin-related); #204900 (Amyloidosis, primary/AL)
- **MeSH:** D000686
- **Orphanet:** ORPHA:69 (Amyloidosis); ORPHA:85443 (AL amyloidosis); ORPHA:271861 (ATTR amyloidosis)

### Synonyms
Common alternative names include: amyloid disease, systemic amyloidosis, primary amyloidosis (AL), secondary amyloidosis (AA), senile systemic amyloidosis (ATTRwt), familial amyloid polyneuropathy (FAP), familial amyloid cardiomyopathy (FAC), and transthyretin-related hereditary amyloidosis.

The following table summarizes the four major systemic amyloidosis types:

| Type | Precursor Protein | Gene(s) | Etiology | Main Organs Affected | Typical Age of Onset | Inheritance | Key Epidemiology | Primary Treatment Approaches |
|---|---|---|---|---|---|---|---|---|
| AL amyloidosis | Monoclonal immunoglobulin light chains (κ or λ) | Immunoglobulin light-chain loci; recurrent plasma-cell cytogenetic abnormalities include t(11;14), 1q21 gain | Clonal plasma-cell disorder with misfolded light-chain production and extracellular fibril deposition; often arises from MGUS/smoldering myeloma and ~10% also meet criteria for multiple myeloma (zanwar2023immunoglobulinlightchain pages 1-2, zerdan2023systemicalamyloidosis pages 1-2, zanwar2023immunoglobulinlightchain pages 6-7) | Heart, kidney, liver, GI tract, peripheral/autonomic nerves, soft tissue; ~70% have multiorgan involvement at diagnosis (zerdan2023systemicalamyloidosis pages 1-2, zanwar2023immunoglobulinlightchain pages 1-2) | Usually adult/older adult; age >65–70 years is adverse prognostic factor (zanwar2023immunoglobulinlightchain pages 6-7, zanwar2023immunoglobulinlightchain pages 1-2) | Not classically inherited; acquired clonal hematologic disease | Incidence ≈1 per 100,000 person-years; ~3,500–4,500 new US cases/year; also reported as ~10 per million/year (zanwar2023immunoglobulinlightchain pages 1-2, zerdan2023systemicalamyloidosis pages 1-2) | First-line daratumumab + bortezomib/cyclophosphamide/dexamethasone (D-VCd); bortezomib-based regimens; selected patients receive autologous stem-cell transplantation; supportive organ care (chompoopong2024amyloidneuropathyfrom pages 10-11, chompoopong2024amyloidneuropathyfrom pages 11-11, dima2023diagnosticandtreatment pages 2-3) |
| ATTR variant (ATTRv, hereditary transthyretin amyloidosis) | Mutant transthyretin | **TTR** (chromosome 18); >140–150 pathogenic variants; key variants include p.Val50Met/Val30Met and p.Val142Ile/Val122Ile (poli2023hereditarytransthyretinamyloidosis pages 2-3, poli2023hereditarytransthyretinamyloidosis pages 1-2, ioannou2023rnatargetingand pages 1-2) | Destabilizing missense TTR variants reduce tetramer stability, causing monomer misfolding and amyloid fibril deposition; phenotype may be neuropathic, cardiac, or mixed (poli2023hereditarytransthyretinamyloidosis pages 2-3, poli2023hereditarytransthyretinamyloidosis pages 1-2, ioannou2023rnatargetingand pages 1-2) | Peripheral/autonomic nerves, heart, GI tract, kidneys, eyes, leptomeninges/CNS (poli2023hereditarytransthyretinamyloidosis pages 4-6, chompoopong2024amyloidneuropathyfrom pages 6-6) | Early-onset in endemic areas often 2nd–5th decade; late-onset usually after 50 years and often 7th–8th decade in non-endemic regions (poli2023hereditarytransthyretinamyloidosis pages 4-6, poli2023hereditarytransthyretinamyloidosis pages 2-3) | Autosomal dominant with incomplete/variable penetrance; parent-of-origin effects reported for Val30Met/Val50Met (poli2023hereditarytransthyretinamyloidosis pages 2-3, chompoopong2024amyloidneuropathyfrom pages 6-6, bhatt2024hereditarytransthyretinamyloidosis pages 1-2) | Global prevalence estimated ~10,186 affected persons (range 5,000–38,000); endemic clusters in Portugal, Sweden, Brazil, Japan; Val122Ile present in ~3–4% of African Americans (poli2023hereditarytransthyretinamyloidosis pages 2-3, bhatt2024hereditarytransthyretinamyloidosis pages 1-2, ioannou2023rnatargetingand pages 1-2) | TTR stabilizers (tafamidis; diflunisal off-label; acoramidis for cardiomyopathy), gene silencers (patisiran, vutrisiran, inotersen, eplontersen), emerging CRISPR gene editing (NTLA-2001), supportive multidisciplinary care (anan2025advancesinthe pages 4-5, dave2024rnainterferencetherapeutics pages 4-5, ioannou2023rnatargetingand pages 1-2) |
| ATTR wild-type (ATTRwt) | Wild-type transthyretin | **TTR** (wild-type sequence) | Age-related destabilization/misfolding of native TTR without pathogenic coding mutation; predominantly cardiac deposition (fontana2025thelastdecade pages 1-3, kim2026autotacmediatedtargeteddegradation pages 4-8, ishida2026crispr–cas3basededitingfor pages 1-2) | Heart (restrictive/infiltrative cardiomyopathy), conduction system; can be associated with carpal tunnel syndrome and other musculoskeletal manifestations in broader ATTR spectrum (fontana2025thelastdecade pages 1-3, chompoopong2024amyloidneuropathyfrom pages 7-7) | Older adults, predominantly elderly men; often >70–80 years (fontana2025thelastdecade pages 1-3, delgado2025epidemiologyoftransthyretin pages 4-6, delgado2025epidemiologyoftransthyretin pages 2-4) | Non-Mendelian; no inherited pathogenic variant required | US ATTR prevalence reported as 6.1/million overall in systematic review; 2-year mortality in wild-type ATTR-CM ~10–30%; autopsy deposits in ~25% of people aged ≥85 years (delgado2025epidemiologyoftransthyretin pages 4-6, delgado2025epidemiologyoftransthyretin pages 1-2, kim2026autotacmediatedtargeteddegradation pages 4-8) | Tafamidis is established disease-modifying therapy; acoramidis now approved for ATTR-CM; investigational/expanding roles for gene silencers and gene editing in cardiomyopathy; supportive HF care/diuretics (anan2025advancesinthe pages 4-5, ang2025emergingnovelgenemodulating pages 10-10, ioannou2023rnatargetingand pages 1-2) |
| AA amyloidosis | Serum amyloid A (SAA) protein | **SAA1** and related SAA loci as susceptibility modifiers; SAA1.1 homozygosity increases risk in some populations (mirioglu2024aaamyloidosisa pages 1-2) | Chronic inflammatory states drive sustained SAA overproduction and secondary fibril deposition; causes include chronic infection, inflammatory arthritis, FMF, immunodeficiency; ~20% idiopathic/unknown cause (mirioglu2024aaamyloidosisa pages 1-2, mirioglu2024aaamyloidosisa pages 4-6) | Kidney predominates; also liver, GI tract, heart less commonly, and other organs depending on inflammatory burden (mirioglu2024aaamyloidosisa pages 1-2, mirioglu2024aaamyloidosisa pages 4-6) | Usually adults, median diagnosis age ~50–70 years (mirioglu2024aaamyloidosisa pages 1-2) | Not usually Mendelian; underlying inflammatory disorders may be genetic (e.g., FMF), and SAA genotype modifies risk (mirioglu2024aaamyloidosisa pages 1-2) | Incidence ~1–2 cases per million person-years in developed countries; now ~2.9% of all amyloidosis cases; slight male predominance (mirioglu2024aaamyloidosisa pages 1-2) | Control underlying inflammation and reduce SAA: biologics such as IL-6 inhibition (tocilizumab), IL-1 inhibition (anakinra), other anti-inflammatory therapy; kidney transplantation for ESRD in selected patients (mirioglu2024aaamyloidosisa pages 1-2, mirioglu2024aaamyloidosisa pages 4-6) |


*Table: This table compares the four major systemic amyloidosis categories across precursor protein, genetics, etiology, organ involvement, onset, epidemiology, and current treatment strategy. It is useful as a compact disease-knowledge-base reference grounded in the gathered evidence.*

---

## 2. Etiology

### Disease Causal Factors

**AL Amyloidosis:** Caused by a clonal non-proliferative plasma cell disorder in which fragments of immunoglobulin light chains (κ or λ) misfold and deposit as amyloid fibrils in tissues. It often arises from pre-malignant conditions such as monoclonal gammopathy of undetermined significance (MGUS) or smoldering myeloma, and approximately 10% of patients also meet criteria for multiple myeloma (zerdan2023systemicalamyloidosis pages 1-2).

**ATTR Amyloidosis (Hereditary):** Caused by autosomal dominant mutations in the TTR gene (chromosome 18q11.2–q12.1), which destabilize the transthyretin tetramer, promoting dissociation into monomers that misfold and aggregate into amyloid fibrils (poli2023hereditarytransthyretinamyloidosis pages 2-3, poli2023hereditarytransthyretinamyloidosis pages 1-2).

**ATTR Amyloidosis (Wild-type):** Results from age-related destabilization of native wild-type TTR protein without pathogenic coding mutations, predominantly causing cardiac deposition in elderly individuals. Autopsy studies revealed myocardial ATTR deposits in approximately 25% of individuals aged ≥85 years (kim2026autotacmediatedtargeteddegradation pages 4-8).

**AA Amyloidosis:** A complication of chronic inflammatory disorders where sustained overproduction of serum amyloid A (SAA) protein leads to fibril deposition. Common causes include chronic infections, inflammatory arthritis, familial Mediterranean fever (FMF), and primary immunodeficiencies. Approximately 20% of cases are idiopathic (mirioglu2024aaamyloidosisa pages 1-2).

### Risk Factors

**Genetic risk factors:**
- TTR gene mutations: Over 150 pathogenic variants identified, predominantly missense. Val30Met (p.Val50Met) is probably the most common worldwide, and Val122Ile (p.Val142Ile) is carried by 3–4% of African Americans (poli2023hereditarytransthyretinamyloidosis pages 2-3, ioannou2023rnatargetingand pages 1-2).
- SAA1.1 homozygosity increases risk for AA amyloidosis in European populations (mirioglu2024aaamyloidosisa pages 1-2).
- Cytogenetic abnormalities in AL amyloidosis: t(11;14) occurs in 40–60% of patients; 1q21 gain in ~50%; trisomies in up to 30% (zanwar2023immunoglobulinlightchain pages 6-7).

**Environmental/demographic risk factors:**
- Advanced age (particularly for ATTRwt and late-onset ATTRv)
- Male sex predominates in ATTR-CM and AA amyloidosis (mirioglu2024aaamyloidosisa pages 1-2, delgado2025epidemiologyoftransthyretin pages 2-4)
- African ancestry (Val122Ile variant prevalence 3.8% in African-descent populations in UK Biobank) (aung2024prevalencecardiacphenotype pages 11-15)
- Sustained chronic inflammation for AA amyloidosis (mirioglu2024aaamyloidosisa pages 1-2)

---

## 3. Phenotypes and Clinical Manifestations

### Cardiac Involvement
Cardiac amyloidosis is the key determinant of survival across all types. In AL amyloidosis, cardiac involvement occurs in approximately 70% of cases, presenting with heart failure, biventricular hypertrophy, restrictive filling pattern, arrhythmias (atrial fibrillation, ventricular tachycardia), AV conduction delays, low voltage on ECG, and poor R-wave progression (dima2023diagnosticandtreatment pages 1-2). Echocardiographic findings include concentric hypertrophy, small LV cavity, diastolic dysfunction, reduced global longitudinal strain with preserved apical strain, and biatrial dilatation (chompoopong2024amyloidneuropathyfrom pages 7-7, zanwar2023immunoglobulinlightchain pages 2-4). Untreated advanced cardiac AL amyloidosis has a median survival of 6 months (fontana2025thelastdecade pages 1-3).

**Suggested HPO terms:** HP:0001638 (Cardiomyopathy); HP:0001635 (Congestive heart failure); HP:0004749 (Atrial flutter/fibrillation); HP:0001712 (Left ventricular hypertrophy)

### Renal Involvement
The kidney is the major affected organ in AA amyloidosis, manifesting as nephrotic-range proteinuria and progressive renal failure (mirioglu2024aaamyloidosisa pages 1-2). In AL amyloidosis, renal involvement presents as nephrotic syndrome without obvious etiology (zanwar2023immunoglobulinlightchain pages 1-2). In ATTRv, approximately one-third of endemic and 6% of non-endemic cases develop nephrotic syndrome (poli2023hereditarytransthyretinamyloidosis pages 4-6).

**Suggested HPO terms:** HP:0000100 (Nephrotic syndrome); HP:0000093 (Proteinuria); HP:0003774 (Stage 5 chronic kidney disease)

### Neurological Manifestations
Amyloid neuropathy is manifested as a length-dependent sensory-predominant neuropathy associated with generalized autonomic failure (chompoopong2024amyloidneuropathyfrom pages 6-6). Small unmyelinated nerves are involved early in early-onset Val30Met ATTRv, whereas other variants and AL amyloidosis present with large- and small-fiber involvement. Carpal tunnel syndrome occurs in two-thirds of ATTRv patients, sometimes preceding diagnosis by 10 years (poli2023hereditarytransthyretinamyloidosis pages 4-6). Neurogenic orthostatic hypotension occurs in 40–60% of ATTRv patients (chompoopong2024amyloidneuropathyfrom pages 6-6). CNS involvement (leptomeningeal amyloidosis) can cause stroke, hemorrhage, cognitive impairment, ataxia, and epilepsy (poli2023hereditarytransthyretinamyloidosis pages 4-6).

**Suggested HPO terms:** HP:0009830 (Peripheral neuropathy); HP:0002459 (Dysautonomia); HP:0012185 (Orthostatic hypotension); HP:0012531 (Pain); HP:0001324 (Muscle weakness)

### Gastrointestinal and Other Manifestations
GI symptoms include premature satiety, gastric distension, nausea, vomiting, diarrhea from malabsorption, and constipation (poli2023hereditarytransthyretinamyloidosis pages 4-6, zanwar2023immunoglobulinlightchain pages 2-4). Hepatomegaly with elevated alkaline phosphatase is common in AL amyloidosis. Classic pathognomonic findings in AL include macroglossia, periorbital ecchymoses ("raccoon eyes"), and musculoskeletal pathologies (zanwar2023immunoglobulinlightchain pages 2-4). Ocular involvement in ATTRv (10% of patients) includes vitreous opacities, glaucoma, and keratoconjunctivitis sicca (poli2023hereditarytransthyretinamyloidosis pages 4-6).

**Suggested HPO terms:** HP:0002240 (Hepatomegaly); HP:0000158 (Macroglossia); HP:0002014 (Diarrhea); HP:0001824 (Weight loss)

---

## 4. Genetic/Molecular Information

### Causal Genes

**TTR (Transthyretin):** HGNC:12405; ENSG00000118271; chromosome 18q12.1. The TTR gene encodes a 127-amino acid protein that functions as a transporter of thyroxine and retinol-binding protein, primarily synthesized in the liver, choroid plexus, and retinal pigment epithelium (poli2023hereditarytransthyretinamyloidosis pages 1-2). Over 140–150 pathogenic variants have been identified, predominantly single-nucleotide substitutions producing missense mutations (poli2023hereditarytransthyretinamyloidosis pages 2-3, kim2026autotacmediatedtargeteddegradation pages 1-4, bhatt2024hereditarytransthyretinamyloidosis pages 1-2).

**Key Pathogenic Variants:**
- **p.Val50Met (Val30Met):** Probably the most common disease-causing variant worldwide; associated with familial amyloid polyneuropathy. Can manifest as early-onset (age <50) with predominant polyneuropathy or late-onset with mixed phenotype. Higher penetrance in Portuguese families versus French and Swedish families (chompoopong2024amyloidneuropathyfrom pages 6-6, ioannou2023rnatargetingand pages 1-2).
- **p.Val142Ile (Val122Ile):** Carried by 3–4% of African Americans and associated with predominant cardiomyopathy. In UK Biobank, prevalence was 4.3% in participants with African ancestry, associated with HR 2.68 for heart failure (ioannou2023rnatargetingand pages 1-2, aung2024prevalencecardiacphenotype pages 11-15).
- **p.Thr80Ala:** Cardiac-predominant or mixed phenotype with earlier onset (~10 years earlier than Val142Ile) (aung2024prevalencecardiacphenotype pages 11-15).

**Inheritance:** Autosomal dominant with incomplete and variable penetrance. Genetic anticipation has been reported in Val30Met families, with shorter disease intervals in mother-to-son transmission (chompoopong2024amyloidneuropathyfrom pages 6-6). Maternal inheritance of Val30Met shows earlier disease onset in offspring, suggesting parental imprinting and possible mitochondrial genome involvement (poli2023hereditarytransthyretinamyloidosis pages 2-3).

**Other Amyloidogenic Genes (from OpenTargets):**
- APP (amyloid beta precursor protein; score 0.86)
- GSN (gelsolin; score 0.85) — causes Finnish-type amyloidosis
- ITM2B (integral membrane protein 2B; score 0.84)
- FGA (fibrinogen alpha chain; score 0.79) — causes hereditary renal amyloidosis
- APOA1 (apolipoprotein A1; score 0.78) — causes hereditary systemic amyloidosis
- CST3 (cystatin C; score 0.73) — causes Icelandic-type cerebral amyloid angiopathy
- LYZ (lysozyme; score 0.72) — causes hereditary systemic amyloidosis
- B2M (beta-2-microglobulin; score 0.67) — causes dialysis-related amyloidosis
- SAA1 (serum amyloid A1) — precursor protein in AA amyloidosis
(OpenTargets Search: amyloidosis)

---

## 5. Mechanism / Pathophysiology

### Protein Misfolding and Amyloid Formation
The fundamental pathological process in all amyloidoses involves protein misfolding and aggregation. Under normal conditions, molecular chaperones guide proteins through energy landscapes to facilitate productive folding and prevent aggregation (louros2023mechanismsandpathology pages 1-4). In amyloidosis, precursor proteins become trapped in local energy minima with non-native structures, exposing hydrophobic patches that promote self-assembly into oligomers, protofibrils, and ultimately insoluble amyloid fibrils (ajmal2023proteinmisfoldingand pages 4-6).

### Specific Mechanisms by Subtype
In ATTR amyloidosis, TTR tetramer destabilization (caused by mutations in ATTRv or aging in ATTRwt) leads to dissociation into monomers that misfold, aggregate abnormally, and deposit in extracellular locations, leading to progressive multiorgan damage (poli2023hereditarytransthyretinamyloidosis pages 2-3). Current therapies include tetramer stabilizers and RNA interference agents, but they do not eliminate pre-existing aggregates, underscoring the need for disease-modifying therapeutics capable of removing pathogenic TTR species (kim2026autotacmediatedtargeteddegradation pages 4-8).

### Toxicity Mechanisms
Toxicity is attributed to both small soluble oligomeric species and fibrillar aggregates. Soluble oligomers cause permeabilization of cellular membranes, impairment of degradation pathways, disruption of synaptic signaling, and mitochondrial dysfunction. Fibrillar toxicity results from mechanical perturbations, sequestration of cellular factors, and inflammatory responses (louros2023mechanismsandpathology pages 16-19). Amyloid fibrils deposit in the endoneurium of peripheral nerves, extensively in dorsal root ganglia and sympathetic ganglia, leading to Schwann cell atrophy and blood–nerve barrier disruption (chompoopong2024amyloidneuropathyfrom pages 6-6).

### Cellular Quality Control
Cells employ the ubiquitin-proteasome system (UPS) as the first-line mechanism for degrading soluble misfolded proteins, while autophagy-lysosome pathways clear insoluble aggregates (ajmal2023proteinmisfoldingand pages 9-11, ajmal2023proteinmisfoldingand pages 8-9, kim2026autotacmediatedtargeteddegradation pages 4-8). When these quality control systems are overwhelmed, accumulation of protein aggregates causes proteotoxicity and cell death (ajmal2023proteinmisfoldingand pages 9-11).

**Suggested GO terms:** GO:0006986 (Response to unfolded protein); GO:0006914 (Autophagy); GO:0030163 (Protein catabolic process); GO:0051082 (Unfolded protein binding); GO:0070841 (Inclusion body assembly)

---

## 6. Anatomical Structures Affected

### Organ Level
- **Heart** (UBERON:0000948): Primary organ in ATTR-CM and frequently in AL. Amyloid fibril deposition in the myocardium causes restrictive cardiomyopathy. Cardiac involvement is the single most important prognostic marker in AL amyloidosis (zanwar2023immunoglobulinlightchain pages 1-2, fontana2025thelastdecade pages 1-3).
- **Kidney** (UBERON:0002113): Major target organ in AA amyloidosis and frequently in AL. Manifests as nephrotic syndrome and progressive renal failure (mirioglu2024aaamyloidosisa pages 1-2, zanwar2023immunoglobulinlightchain pages 1-2).
- **Peripheral nervous system** (UBERON:0000010): Predominantly in ATTRv and AL. Length-dependent sensorimotor polyneuropathy and autonomic neuropathy (poli2023hereditarytransthyretinamyloidosis pages 4-6, chompoopong2024amyloidneuropathyfrom pages 6-6).
- **Liver** (UBERON:0002107): Hepatomegaly in AL amyloidosis; primary source of TTR and SAA synthesis (zanwar2023immunoglobulinlightchain pages 2-4).
- **Gastrointestinal tract** (UBERON:0001555): Motility disorders, malabsorption (poli2023hereditarytransthyretinamyloidosis pages 4-6).
- **Eye** (UBERON:0000970): Vitreous opacities, glaucoma in ATTRv (poli2023hereditarytransthyretinamyloidosis pages 4-6).

### Cell Types Involved
- Cardiomyocytes (CL:0000746): Direct fibril toxicity causes sarcomere disruption and electromechanical uncoupling
- Plasma cells (CL:0000786): Clonal source of amyloidogenic light chains in AL
- Hepatocytes (CL:0000182): Primary site of TTR and SAA synthesis
- Schwann cells (CL:0002573): Atrophy in proximity to amyloid fibrils in nerves
- Macrophages (CL:0000235): Inflammatory response to amyloid deposits

---

## 7. Epidemiology and Population

### Prevalence and Incidence
- **AL amyloidosis:** Incidence approximately 1 per 100,000 person-years (3,500–4,500 new cases annually in the US), also reported as ~10 per million/year (zanwar2023immunoglobulinlightchain pages 1-2, zerdan2023systemicalamyloidosis pages 1-2).
- **ATTR amyloidosis:** Prevalence varies dramatically by geography: 6.1 per million in the US to 232 per million in Portugal (delgado2025epidemiologyoftransthyretin pages 1-2). In endemic sub-regions, prevalence reaches up to 1,631 per million (poli2023hereditarytransthyretinamyloidosis pages 2-3). ATTRwt estimated to affect ~500,000 individuals worldwide (ishida2026crispr–cas3basededitingfor pages 1-2). In the US, 2018 incidence was 3.9 per million person-years overall, rising to 36.6 PMPY in elderly individuals (delgado2025epidemiologyoftransthyretin pages 4-6).
- **AA amyloidosis:** Incidence 1–2 cases per million person-years in developed countries; now represents only ~2.9% of all amyloidosis cases (mirioglu2024aaamyloidosisa pages 1-2).

### Population Demographics
- ATTRwt predominantly affects older males (>70–80 years) (fontana2025thelastdecade pages 1-3, delgado2025epidemiologyoftransthyretin pages 2-4).
- ATTRv Val122Ile: 4.3% prevalence in UK Biobank participants with African ancestry; represents the fourth most common cause of heart failure (11%) in Afro-Caribbeans (aung2024prevalencecardiacphenotype pages 11-15).
- Study populations are predominantly male (56–94%), with mean ages ranging from 52.3 to 83 years (delgado2025epidemiologyoftransthyretin pages 2-4).
- Endemic ATTRv clusters exist in Portugal, Sweden, Brazil, and Japan (poli2023hereditarytransthyretinamyloidosis pages 2-3).

### Mortality
- Two-year mortality risk: 10–30% for wild-type ATTR-CM; 10–50% for variant ATTR-CM (delgado2025epidemiologyoftransthyretin pages 1-2).
- Median survival times across ATTR studies: 12–80 months (delgado2025epidemiologyoftransthyretin pages 4-6).
- AL amyloidosis: Median OS 48.8 months in the European EMN23 study; early mortality 13.4%; stage IIIb patients had median OS of only 4.5–5.0 months (zanwar2023immunoglobulinlightchain pages 6-7).
- Untreated advanced cardiac AL: median survival 6 months (fontana2025thelastdecade pages 1-3).

---

## 8. Diagnostics

### Histopathological Diagnosis
Congo red staining with characteristic apple-green birefringence under polarized light microscopy is the primary diagnostic method. Alternative stains include thioflavin T and sulfated alcian blue (zerdan2023systemicalamyloidosis pages 1-2, zanwar2023immunoglobulinlightchain pages 2-4, mirioglu2024aaamyloidosisa pages 4-6). Electron microscopy reveals rigid, unbranched fibrils of 8–12 nm diameter (mirioglu2024aaamyloidosisa pages 4-6).

### Tissue Sources and Sensitivity
Bone marrow biopsy (56–70% sensitivity) and fat pad aspiration (70–80% sensitivity) performed concurrently achieve 80–90% sensitivity for AL amyloidosis diagnosis (zanwar2023immunoglobulinlightchain pages 2-4). Salivary gland biopsy and periumbilical fat aspiration with Congo red staining show 77–89% sensitivity for AA amyloidosis (mirioglu2024aaamyloidosisa pages 4-6).

### Amyloid Typing
Mass spectrometry-based proteomic assay (laser microdissection/mass spectrometry) is the gold standard for amyloid typing, offering high sensitivity and specificity (zanwar2023immunoglobulinlightchain pages 2-4).

### Cardiac Imaging
- **Bone scintigraphy:** Technetium-99m pyrophosphate (99mTc-PYP) SPECT demonstrates excellent sensitivity (85–97%) and specificity (97–100%) for diagnosing TTR cardiac amyloidosis non-invasively (zanwar2023immunoglobulinlightchain pages 2-4, fontana2025thelastdecade pages 4-6).
- **Cardiac MRI:** Provides tissue characterization with late gadolinium enhancement, native T1 mapping, and extracellular volume (ECV) measurement serving as a surrogate for interstitial amyloid burden (fontana2025thelastdecade pages 4-6).
- **Echocardiography:** Cornerstone first-line imaging showing concentric hypertrophy, restrictive filling, and apical sparing of longitudinal strain (chompoopong2024amyloidneuropathyfrom pages 7-7).

### Staging Systems
The Mayo/Boston staging system for AL amyloidosis uses cardiac biomarkers: troponin I (>0.1 ng/mL) and BNP (>81 pg/mL), with further substratification of stage III based on BNP >700 pg/mL (stage IIIb) (dima2023diagnosticandtreatment pages 2-3, chompoopong2024amyloidneuropathyfrom pages 8-9).

### Genetic Testing
TTR gene sequencing (single-gene or multigene panel) identifies missense, nonsense, and splice-site variants. Testing is recommended for all patients with suspected ATTR amyloidosis and for family members of known carriers (chompoopong2024amyloidneuropathyfrom pages 6-6).

---

## 9. Treatment

### AL Amyloidosis Treatment

**First-line therapy:** Daratumumab (anti-CD38 monoclonal antibody) combined with bortezomib, cyclophosphamide, and dexamethasone (D-VCd) is now standard based on the landmark ANDROMEDA trial. In Asian patients, overall hematologic complete response rate was 58.6% vs. 9.7% with VCd alone (chompoopong2024amyloidneuropathyfrom pages 11-11). Daratumumab achieved clinical remission in 59% of patients, with cardiac improvement in 57% and renal improvement in 57% (chompoopong2024amyloidneuropathyfrom pages 11-11). Real-world UK data with daratumumab-bortezomib-thalidomide-dexamethasone showed 97% overall hematologic response rate and 65% complete response.

**Autologous stem cell transplantation (ASCT):** Effective strategy after high-dose melphalan, improving survival to 48 months in up to 77% of eligible patients, though only ~20% meet eligibility criteria due to frailty, old age, or multiorgan involvement (chompoopong2024amyloidneuropathyfrom pages 10-11).

**Emerging therapies in clinical trials:**
- Teclistamab (bispecific antibody): Phase 2 trials for relapsed/refractory AL (NCT06649695, NCT06935162, NCT07079423)
- Elranatamab: Phase 1/2 trial (NCT06569147)
- CAR-T cell therapy targeting CD19 and BCMA: Phase 1b/2 (NCT07081646)
- Belantamab mafodotin: Phase 1/2 (NCT05145816)
- Dara-VCd plus ASCT vs. Dara-VCd alone: Phase 3 (NCT06022939)

**Suggested MAXO terms:** MAXO:0001001 (Chemotherapy); MAXO:0000068 (Transplantation)

### ATTR Amyloidosis Treatment

**TTR Stabilizers:**
- **Tafamidis:** First FDA-approved disease-modifying therapy for ATTR-CM; demonstrated significant reductions in all-cause mortality and cardiovascular hospitalizations in the ATTR-ACT trial (anan2025advancesinthe pages 4-5).
- **Acoramidis:** FDA-approved TTR stabilizer for ATTR-CM; outperformed placebo in clinical trials (ang2025emergingnovelgenemodulating pages 10-10, dave2024rnainterferencetherapeutics pages 4-5).

**Gene Silencers (RNA-based therapies):**
- **Patisiran (siRNA):** Licensed for ATTR polyneuropathy; early data suggest cardiac benefit (ioannou2023rnatargetingand pages 1-2).
- **Vutrisiran (siRNA):** Licensed for ATTR polyneuropathy (ioannou2023rnatargetingand pages 1-2).
- **Inotersen (ASO):** Significant improvements in neurological function (mNIS+7 difference −19.7, P<0.001) and quality of life; sustained benefits over 5.2 years (dave2024rnainterferencetherapeutics pages 4-5, chompoopong2024amyloidneuropathyfrom pages 11-11).
- **Eplontersen (ASO):** Well-tolerated with significant TTR reduction; improved LVEF by 4.3% in cardiomyopathy subgroup (dave2024rnainterferencetherapeutics pages 4-5).

**Gene Editing:**
- **NTLA-2001 (CRISPR-Cas9):** In Phase 3 clinical trials; has demonstrated durable reductions in serum TTR, with up to 90% sustained plasma TTR reduction over 24 months (ishida2026crispr–cas3basededitingfor pages 1-2).
- **ART001 (CRISPR-Cas9):** A single injection achieved >80% TTR knock-down at doses >0.5 mg/kg, lasting at least 72 weeks without serious adverse events.
- **CRISPR-Cas3:** A mechanistically distinct approach generating long-range deletions; achieved 48.7% hepatic editing and 80.1% serum TTR reduction in mice (ishida2026crispr–cas3basededitingfor pages 1-2).

**Emerging approaches:**
- AUTOTAC-mediated targeted degradation of TTR aggregates (ATC201): Novel bifunctional degrader that reduces intracellular TTR aggregates and improves neuromuscular function in hATTR mouse models (kim2026autotacmediatedtargeteddegradation pages 4-8).
- Anti-amyloid monoclonal antibodies (PRX004, NI006): In Phase 1 trials, designed to clear existing amyloid deposits (anan2025advancesinthe pages 4-5, dave2024rnainterferencetherapeutics pages 7-8).

### AA Amyloidosis Treatment
Management primarily aims to reduce SAA levels by controlling underlying inflammation. Anti-inflammatory biologics including tocilizumab (IL-6 inhibitor) and anakinra (IL-1 receptor antagonist) have dramatically expanded the therapeutic armamentarium (mirioglu2024aaamyloidosisa pages 1-2). Long-term tocilizumab treatment has been associated with disappearance of amyloid deposits from tissues. Kidney transplantation is preferred in patients with kidney failure, with recurrence in allografts becoming rare due to new anti-inflammatory agents (mirioglu2024aaamyloidosisa pages 1-2).

---

## 10. Prognosis and Outcomes

### Prognostic Factors
- Cardiac involvement is the single most important prognostic marker in AL amyloidosis (zanwar2023immunoglobulinlightchain pages 1-2).
- Cardiac biomarkers (NT-proBNP, troponin) drive staging systems (dima2023diagnosticandtreatment pages 2-3, chompoopong2024amyloidneuropathyfrom pages 8-9).
- Cytogenetic abnormalities: t(11;14) associated with poor bortezomib response; 1q21 gain associated with shorter OS (zanwar2023immunoglobulinlightchain pages 6-7).
- Hematologic response: Complete response (negative immunofixation, normal FLC ratio) achieved in 65–80% with first-line therapy is associated with superior outcomes (zanwar2023immunoglobulinlightchain pages 6-7).
- Age >65–70, poor performance status (ECOG >2), and autonomic involvement are adverse prognostic factors (zanwar2023immunoglobulinlightchain pages 6-7).

### Survival
- AL amyloidosis median OS: 48.8 months overall; stage IIIb median OS only 4.5–5.0 months with no improvement despite newer therapies (zanwar2023immunoglobulinlightchain pages 6-7).
- Early mortality in AL: 13.4% and did not improve over time; remained >39% for stage IIIb patients.
- ATTR-CM: 2-year mortality 10–30% (wild-type) and 10–50% (variant) (delgado2025epidemiologyoftransthyretin pages 1-2).
- TTR LP/P variant carriers: HR 2.68 for heart failure; HR 1.98 for all-cause mortality with non-Val142Ile variants (aung2024prevalencecardiacphenotype pages 11-15).

---

## 11. Prevention

### Primary Prevention
For AA amyloidosis, primary prevention involves effective control of underlying inflammatory conditions using biological therapies to suppress SAA production (mirioglu2024aaamyloidosisa pages 1-2).

### Secondary Prevention / Screening
- Cascade genetic screening of family members of ATTRv patients is recommended, given autosomal dominant inheritance and availability of effective therapies (chompoopong2024amyloidneuropathyfrom pages 6-6, poli2023hereditarytransthyretinamyloidosis pages 1-2).
- Screening for ATTR-CM in patients with HFpEF and left ventricular wall thickness ≥12 mm using 99mTc-PYP scintigraphy has been evaluated but faces cost-effectiveness challenges primarily due to high treatment costs (zanwar2023immunoglobulinlightchain pages 2-4).
- Carpal tunnel syndrome tissue screening for amyloid has been proposed as an early detection strategy.

### Genetic Counseling
Genetic counseling is essential for ATTRv families, addressing risk assessment, reproductive planning, and presymptomatic testing. The hATTR Compass Genetic Testing Program identified pathogenic TTR variants in 6.6% of 22,886 referred patients, with only 32% reporting known family history (bhatt2024hereditarytransthyretinamyloidosis pages 1-2).

---

## 12. Animal Models

### Transgenic Mouse Models
- **HM30 transgenic mice:** Mouse TTR knocked out with ectopic overexpression of human TTR V30M; used for studying hereditary ATTR amyloidosis pathogenesis and therapeutic interventions (kim2026autotacmediatedtargeteddegradation pages 4-8).
- **TTR exon-humanized mice:** Used for evaluating CRISPR-Cas3 gene editing approaches; a single LNP-based treatment achieved 48.7% hepatic editing and 80.1% serum TTR reduction (ishida2026crispr–cas3basededitingfor pages 1-2).
- **Mouse models carrying human TTR transgenes:** Used for evaluation of highly modified sgRNA for CRISPR-based TTR knockdown.

### In Vitro Models
- Human iPSC-derived cardiomyocytes, endothelial cells, and fibroblasts seeded on TTR fibrils (WT, V122I, V30M) provide cell-type-specific disease phenotypes including sarcomere disruption, altered calcium handling, and reduced cell viability.
- Choroid plexus organoids model amyloid uptake at the blood-CSF barrier.

---

## 13. Disease-Target Associations (OpenTargets)

OpenTargets analysis identified 12 primary targets associated with amyloidosis (MONDO:0019065), with the highest association scores for:
1. **TTR** (transthyretin) — score 0.90; approved therapies targeting this gene
2. **APP** (amyloid beta precursor protein) — score 0.87
3. **GSN** (gelsolin) — score 0.85
4. **ITM2B** (integral membrane protein 2B) — score 0.84
5. **FGA** (fibrinogen alpha chain) — score 0.79
6. **APOA1** (apolipoprotein A1) — score 0.78
7. **CST3** (cystatin C) — score 0.73
8. **LYZ** (lysozyme) — score 0.72
9. **B2M** (beta-2-microglobulin) — score 0.67
10. **APOE** (apolipoprotein E) — score 0.62

For AL amyloidosis specifically, additional associated targets include CCND1 (cyclin D1), CALCA, INS, NPPA, and SAA1 (OpenTargets Search: amyloidosis).

---

## 14. Summary and Future Directions

Amyloidosis has undergone a dramatic transformation in the past decade, from an underdiagnosed and universally fatal condition to one with expanding diagnostic and therapeutic options. Key advances include non-invasive cardiac scintigraphy for ATTR diagnosis, daratumumab-based regimens revolutionizing AL amyloidosis treatment, and RNA-based gene silencing and CRISPR gene editing therapies fundamentally altering the ATTR treatment landscape (ioannou2023rnatargetingand pages 1-2, ishida2026crispr–cas3basededitingfor pages 1-2). Despite these advances, critical unmet needs remain: early mortality in advanced cardiac AL amyloidosis has not improved (zanwar2023immunoglobulinlightchain pages 6-7), comprehensive epidemiological data from Africa and South America are lacking (delgado2025epidemiologyoftransthyretin pages 8-8), and therapies capable of clearing pre-existing amyloid deposits are still investigational (kim2026autotacmediatedtargeteddegradation pages 4-8). Novel approaches including AUTOTAC-mediated targeted protein degradation, anti-amyloid monoclonal antibodies, bispecific antibodies, and CAR-T cell therapy represent the next frontier in amyloidosis management.

References

1. (poli2023hereditarytransthyretinamyloidosis pages 1-2): Loris Poli, Beatrice Labella, Stefano Cotti Piccinelli, Filomena Caria, Barbara Risi, Simona Damioli, Alessandro Padovani, and Massimiliano Filosto. Hereditary transthyretin amyloidosis: a comprehensive review with a focus on peripheral neuropathy. Frontiers in Neurology, Oct 2023. URL: https://doi.org/10.3389/fneur.2023.1242815, doi:10.3389/fneur.2023.1242815. This article has 103 citations and is from a peer-reviewed journal.

2. (ajmal2023proteinmisfoldingand pages 4-6): Mohammad Rehan Ajmal. Protein misfolding and aggregation in proteinopathies: causes, mechanism and cellular response. Diseases, 11:30, Feb 2023. URL: https://doi.org/10.3390/diseases11010030, doi:10.3390/diseases11010030. This article has 135 citations.

3. (fontana2025thelastdecade pages 1-3): Marianna Fontana, Adam Ioannou, Sarah Cuddy, Sharmila Dorbala, Ahmad Masri, James C. Moon, Vasvi Singh, Olivier Clerc, Mazen Hanna, Fredrick Ruberg, Martha Grogan, Michele Emdin, and Julian Gillmore. The last decade in cardiac amyloidosis. JACC. Cardiovascular imaging, 18:478-499, Jan 2025. URL: https://doi.org/10.1016/j.jcmg.2024.10.011, doi:10.1016/j.jcmg.2024.10.011. This article has 79 citations.

4. (zanwar2023immunoglobulinlightchain pages 1-2): Saurabh Zanwar, Morie A. Gertz, and Eli Muchtar. Immunoglobulin light chain amyloidosis: diagnosis and risk assessment. Journal of the National Comprehensive Cancer Network : JNCCN, 21 1:83-90, Jan 2023. URL: https://doi.org/10.6004/jnccn.2022.7077, doi:10.6004/jnccn.2022.7077. This article has 38 citations.

5. (OpenTargets Search: amyloidosis): Open Targets Query (amyloidosis, 32 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (zerdan2023systemicalamyloidosis pages 1-2): Maroun Bou Zerdan, Lewis Nasr, Farhan Khalid, Sabine Allam, Youssef Bouferraa, Saba Batool, Muhammad Tayyeb, Shubham Adroja, Mahinbanu Mammadii, Faiz Anwer, Shahzad Raza, and Chakra P. Chaulagain. Systemic al amyloidosis: current approach and future direction. Oncotarget, 14:384-394, Apr 2023. URL: https://doi.org/10.18632/oncotarget.28415, doi:10.18632/oncotarget.28415. This article has 57 citations.

7. (zanwar2023immunoglobulinlightchain pages 6-7): Saurabh Zanwar, Morie A. Gertz, and Eli Muchtar. Immunoglobulin light chain amyloidosis: diagnosis and risk assessment. Journal of the National Comprehensive Cancer Network : JNCCN, 21 1:83-90, Jan 2023. URL: https://doi.org/10.6004/jnccn.2022.7077, doi:10.6004/jnccn.2022.7077. This article has 38 citations.

8. (chompoopong2024amyloidneuropathyfrom pages 10-11): Pitcha Chompoopong, Michelle L. Mauermann, Hasan Siddiqi, and Amanda Peltier. Amyloid neuropathy: from pathophysiology to treatment in light‐chain amyloidosis and hereditary transthyretin amyloidosis. Annals of Neurology, 96:423-440, Jun 2024. URL: https://doi.org/10.1002/ana.26965, doi:10.1002/ana.26965. This article has 44 citations and is from a highest quality peer-reviewed journal.

9. (chompoopong2024amyloidneuropathyfrom pages 11-11): Pitcha Chompoopong, Michelle L. Mauermann, Hasan Siddiqi, and Amanda Peltier. Amyloid neuropathy: from pathophysiology to treatment in light‐chain amyloidosis and hereditary transthyretin amyloidosis. Annals of Neurology, 96:423-440, Jun 2024. URL: https://doi.org/10.1002/ana.26965, doi:10.1002/ana.26965. This article has 44 citations and is from a highest quality peer-reviewed journal.

10. (dima2023diagnosticandtreatment pages 2-3): Danai Dima, Sandra Mazzoni, Faiz Anwer, Jack Khouri, Christy Samaras, Jason Valent, and Louis Williams. Diagnostic and treatment strategies for al amyloidosis in an era of therapeutic innovation. May 2023. URL: https://doi.org/10.1200/op.22.00396, doi:10.1200/op.22.00396. This article has 65 citations and is from a peer-reviewed journal.

11. (poli2023hereditarytransthyretinamyloidosis pages 2-3): Loris Poli, Beatrice Labella, Stefano Cotti Piccinelli, Filomena Caria, Barbara Risi, Simona Damioli, Alessandro Padovani, and Massimiliano Filosto. Hereditary transthyretin amyloidosis: a comprehensive review with a focus on peripheral neuropathy. Frontiers in Neurology, Oct 2023. URL: https://doi.org/10.3389/fneur.2023.1242815, doi:10.3389/fneur.2023.1242815. This article has 103 citations and is from a peer-reviewed journal.

12. (ioannou2023rnatargetingand pages 1-2): Adam Ioannou, Marianna Fontana, and Julian D. Gillmore. Rna targeting and gene editing strategies for transthyretin amyloidosis. Biodrugs, 37:127-142, Feb 2023. URL: https://doi.org/10.1007/s40259-023-00577-7, doi:10.1007/s40259-023-00577-7. This article has 102 citations and is from a peer-reviewed journal.

13. (poli2023hereditarytransthyretinamyloidosis pages 4-6): Loris Poli, Beatrice Labella, Stefano Cotti Piccinelli, Filomena Caria, Barbara Risi, Simona Damioli, Alessandro Padovani, and Massimiliano Filosto. Hereditary transthyretin amyloidosis: a comprehensive review with a focus on peripheral neuropathy. Frontiers in Neurology, Oct 2023. URL: https://doi.org/10.3389/fneur.2023.1242815, doi:10.3389/fneur.2023.1242815. This article has 103 citations and is from a peer-reviewed journal.

14. (chompoopong2024amyloidneuropathyfrom pages 6-6): Pitcha Chompoopong, Michelle L. Mauermann, Hasan Siddiqi, and Amanda Peltier. Amyloid neuropathy: from pathophysiology to treatment in light‐chain amyloidosis and hereditary transthyretin amyloidosis. Annals of Neurology, 96:423-440, Jun 2024. URL: https://doi.org/10.1002/ana.26965, doi:10.1002/ana.26965. This article has 44 citations and is from a highest quality peer-reviewed journal.

15. (bhatt2024hereditarytransthyretinamyloidosis pages 1-2): Kunal Bhatt, Diego H. Delgado, Sami Khella, Naresh Bumma, Chafic Karam, Andrew Keller, Andrew M. Rosen, Ana Bozas, Amy Shea, Meghan C. Towne, Linda M. Polfus, Gwendolyn E. Kaeser, Victoria Sanjurjo, and Keyur B. Shah. Hereditary transthyretin amyloidosis in patients referred to a genetic testing program. Journal of the American Heart Association, Dec 2024. URL: https://doi.org/10.1161/jaha.123.033770, doi:10.1161/jaha.123.033770. This article has 14 citations.

16. (anan2025advancesinthe pages 4-5): I. Anan. Advances in the treatment of transthyretin amyloidosis. eGastroenterology, Jul 2025. URL: https://doi.org/10.1136/egastro-2025-100198, doi:10.1136/egastro-2025-100198. This article has 5 citations and is from a peer-reviewed journal.

17. (dave2024rnainterferencetherapeutics pages 4-5): Prashil Dave, Puneet Anand, Azra Kothawala, Prakhyath Srikaram, Dipsa Shastri, Anwar Uddin, Jill Bhavsar, and Andrew Winer. Rna interference therapeutics for hereditary amyloidosis: a narrative review of clinical trial outcomes and future directions. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.62981, doi:10.7759/cureus.62981. This article has 11 citations.

18. (kim2026autotacmediatedtargeteddegradation pages 4-8): Hee Yeon Kim, Daniel Youngjae Park, Eun Hye Cho, Yeon Sung Son, Sung Hyun Kim, Ki Woon Sung, Helena Sofia Martins, Maria João Saraiva, Maria Rosário Almeida, Chang Hoon Ji, and Yong Tae Kwon. Autotac-mediated targeted degradation of transthyretin aggregates ameliorates hereditary transthyretin amyloidosis. bioRxiv, Feb 2026. URL: https://doi.org/10.64898/2026.02.23.707350, doi:10.64898/2026.02.23.707350. This article has 0 citations.

19. (ishida2026crispr–cas3basededitingfor pages 1-2): Saeko Ishida, Yusuke Sato, Keisuke Chosa, Eri Ezawa, Yuko Yamauchi, Masaaki Oyama, Hiroko Kozuka-Hata, Rina Ito, Rikako Sato, Masatoshi Maeki, Tomo-o Ishikawa, Kenichi Yamamura, Kohei Takeshita, Kensuke Yamaguchi, Yuta Kochi, Fumitaka Hashiya, Yiwei Liu, Naoko Abe, Hiroshi Abe, Yoshiki Sekijima, Kazuto Yoshimi, and Tomoji Mashimo. Crispr–cas3-based editing for targeted deletions in a mouse model of transthyretin amyloidosis. Nature Biotechnology, Jan 2026. URL: https://doi.org/10.1038/s41587-025-02949-6, doi:10.1038/s41587-025-02949-6. This article has 6 citations and is from a highest quality peer-reviewed journal.

20. (chompoopong2024amyloidneuropathyfrom pages 7-7): Pitcha Chompoopong, Michelle L. Mauermann, Hasan Siddiqi, and Amanda Peltier. Amyloid neuropathy: from pathophysiology to treatment in light‐chain amyloidosis and hereditary transthyretin amyloidosis. Annals of Neurology, 96:423-440, Jun 2024. URL: https://doi.org/10.1002/ana.26965, doi:10.1002/ana.26965. This article has 44 citations and is from a highest quality peer-reviewed journal.

21. (delgado2025epidemiologyoftransthyretin pages 4-6): Diego Delgado, Firas Dabbous, Nitin Shivappa, Faizan Mazhar, Eric Wittbrodt, Divya Shridharmurthy, and Krister Järbrink. Epidemiology of transthyretin (attr) amyloidosis: a systematic literature review. Orphanet Journal of Rare Diseases, Jan 2025. URL: https://doi.org/10.1186/s13023-025-03547-0, doi:10.1186/s13023-025-03547-0. This article has 46 citations and is from a peer-reviewed journal.

22. (delgado2025epidemiologyoftransthyretin pages 2-4): Diego Delgado, Firas Dabbous, Nitin Shivappa, Faizan Mazhar, Eric Wittbrodt, Divya Shridharmurthy, and Krister Järbrink. Epidemiology of transthyretin (attr) amyloidosis: a systematic literature review. Orphanet Journal of Rare Diseases, Jan 2025. URL: https://doi.org/10.1186/s13023-025-03547-0, doi:10.1186/s13023-025-03547-0. This article has 46 citations and is from a peer-reviewed journal.

23. (delgado2025epidemiologyoftransthyretin pages 1-2): Diego Delgado, Firas Dabbous, Nitin Shivappa, Faizan Mazhar, Eric Wittbrodt, Divya Shridharmurthy, and Krister Järbrink. Epidemiology of transthyretin (attr) amyloidosis: a systematic literature review. Orphanet Journal of Rare Diseases, Jan 2025. URL: https://doi.org/10.1186/s13023-025-03547-0, doi:10.1186/s13023-025-03547-0. This article has 46 citations and is from a peer-reviewed journal.

24. (ang2025emergingnovelgenemodulating pages 10-10): Song Peng Ang, Jia Ee Chia, and Debabrata Mukherjee. Emerging, novel gene-modulating therapies for transthyretin amyloid cardiomyopathy. Heart Failure Reviews, 30:759-770, Mar 2025. URL: https://doi.org/10.1007/s10741-025-10502-5, doi:10.1007/s10741-025-10502-5. This article has 8 citations and is from a peer-reviewed journal.

25. (mirioglu2024aaamyloidosisa pages 1-2): Safak Mirioglu, Omer Uludag, Ozge Hurdogan, Gizem Kumru, Ilay Berke, Stavros A. Doumas, Eleni Frangou, and Ahmet Gul. Aa amyloidosis: a contemporary view. Current Rheumatology Reports, 26:248-259, Apr 2024. URL: https://doi.org/10.1007/s11926-024-01147-8, doi:10.1007/s11926-024-01147-8. This article has 59 citations and is from a peer-reviewed journal.

26. (mirioglu2024aaamyloidosisa pages 4-6): Safak Mirioglu, Omer Uludag, Ozge Hurdogan, Gizem Kumru, Ilay Berke, Stavros A. Doumas, Eleni Frangou, and Ahmet Gul. Aa amyloidosis: a contemporary view. Current Rheumatology Reports, 26:248-259, Apr 2024. URL: https://doi.org/10.1007/s11926-024-01147-8, doi:10.1007/s11926-024-01147-8. This article has 59 citations and is from a peer-reviewed journal.

27. (aung2024prevalencecardiacphenotype pages 11-15): Nay Aung, Hannah L. Nicholls, C. Anwar A. Chahal, Mohammed Y. Khanji, Elisa Rauseo, Sucharitha Chadalavada, Steffen E. Petersen, Patricia B. Munroe, Perry M. Elliott, and Luis R. Lopes. Prevalence, cardiac phenotype, and outcomes of transthyretin variants in the uk biobank population. JAMA Cardiology, 9:964, Nov 2024. URL: https://doi.org/10.1001/jamacardio.2024.2190, doi:10.1001/jamacardio.2024.2190. This article has 21 citations and is from a highest quality peer-reviewed journal.

28. (dima2023diagnosticandtreatment pages 1-2): Danai Dima, Sandra Mazzoni, Faiz Anwer, Jack Khouri, Christy Samaras, Jason Valent, and Louis Williams. Diagnostic and treatment strategies for al amyloidosis in an era of therapeutic innovation. May 2023. URL: https://doi.org/10.1200/op.22.00396, doi:10.1200/op.22.00396. This article has 65 citations and is from a peer-reviewed journal.

29. (zanwar2023immunoglobulinlightchain pages 2-4): Saurabh Zanwar, Morie A. Gertz, and Eli Muchtar. Immunoglobulin light chain amyloidosis: diagnosis and risk assessment. Journal of the National Comprehensive Cancer Network : JNCCN, 21 1:83-90, Jan 2023. URL: https://doi.org/10.6004/jnccn.2022.7077, doi:10.6004/jnccn.2022.7077. This article has 38 citations.

30. (kim2026autotacmediatedtargeteddegradation pages 1-4): Hee Yeon Kim, Daniel Youngjae Park, Eun Hye Cho, Yeon Sung Son, Sung Hyun Kim, Ki Woon Sung, Helena Sofia Martins, Maria João Saraiva, Maria Rosário Almeida, Chang Hoon Ji, and Yong Tae Kwon. Autotac-mediated targeted degradation of transthyretin aggregates ameliorates hereditary transthyretin amyloidosis. bioRxiv, Feb 2026. URL: https://doi.org/10.64898/2026.02.23.707350, doi:10.64898/2026.02.23.707350. This article has 0 citations.

31. (louros2023mechanismsandpathology pages 1-4): Nikolaos N. Louros, J. Schymkowitz, and F. Rousseau. Mechanisms and pathology of protein misfolding and aggregation. Nature Reviews Molecular Cell Biology, 24:912-933, Sep 2023. URL: https://doi.org/10.1038/s41580-023-00647-2, doi:10.1038/s41580-023-00647-2. This article has 270 citations and is from a domain leading peer-reviewed journal.

32. (louros2023mechanismsandpathology pages 16-19): Nikolaos N. Louros, J. Schymkowitz, and F. Rousseau. Mechanisms and pathology of protein misfolding and aggregation. Nature Reviews Molecular Cell Biology, 24:912-933, Sep 2023. URL: https://doi.org/10.1038/s41580-023-00647-2, doi:10.1038/s41580-023-00647-2. This article has 270 citations and is from a domain leading peer-reviewed journal.

33. (ajmal2023proteinmisfoldingand pages 9-11): Mohammad Rehan Ajmal. Protein misfolding and aggregation in proteinopathies: causes, mechanism and cellular response. Diseases, 11:30, Feb 2023. URL: https://doi.org/10.3390/diseases11010030, doi:10.3390/diseases11010030. This article has 135 citations.

34. (ajmal2023proteinmisfoldingand pages 8-9): Mohammad Rehan Ajmal. Protein misfolding and aggregation in proteinopathies: causes, mechanism and cellular response. Diseases, 11:30, Feb 2023. URL: https://doi.org/10.3390/diseases11010030, doi:10.3390/diseases11010030. This article has 135 citations.

35. (fontana2025thelastdecade pages 4-6): Marianna Fontana, Adam Ioannou, Sarah Cuddy, Sharmila Dorbala, Ahmad Masri, James C. Moon, Vasvi Singh, Olivier Clerc, Mazen Hanna, Fredrick Ruberg, Martha Grogan, Michele Emdin, and Julian Gillmore. The last decade in cardiac amyloidosis. JACC. Cardiovascular imaging, 18:478-499, Jan 2025. URL: https://doi.org/10.1016/j.jcmg.2024.10.011, doi:10.1016/j.jcmg.2024.10.011. This article has 79 citations.

36. (chompoopong2024amyloidneuropathyfrom pages 8-9): Pitcha Chompoopong, Michelle L. Mauermann, Hasan Siddiqi, and Amanda Peltier. Amyloid neuropathy: from pathophysiology to treatment in light‐chain amyloidosis and hereditary transthyretin amyloidosis. Annals of Neurology, 96:423-440, Jun 2024. URL: https://doi.org/10.1002/ana.26965, doi:10.1002/ana.26965. This article has 44 citations and is from a highest quality peer-reviewed journal.

37. (dave2024rnainterferencetherapeutics pages 7-8): Prashil Dave, Puneet Anand, Azra Kothawala, Prakhyath Srikaram, Dipsa Shastri, Anwar Uddin, Jill Bhavsar, and Andrew Winer. Rna interference therapeutics for hereditary amyloidosis: a narrative review of clinical trial outcomes and future directions. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.62981, doi:10.7759/cureus.62981. This article has 11 citations.

38. (delgado2025epidemiologyoftransthyretin pages 8-8): Diego Delgado, Firas Dabbous, Nitin Shivappa, Faizan Mazhar, Eric Wittbrodt, Divya Shridharmurthy, and Krister Järbrink. Epidemiology of transthyretin (attr) amyloidosis: a systematic literature review. Orphanet Journal of Rare Diseases, Jan 2025. URL: https://doi.org/10.1186/s13023-025-03547-0, doi:10.1186/s13023-025-03547-0. This article has 46 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Amyloidosis-deep-research-falcon_artifacts/artifact-00.md)