---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T09:50:58.055306'
end_time: '2026-06-30T10:05:32.143996'
duration_seconds: 874.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Granular Cell Tumor
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Granular_Cell_Tumor-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Granular_Cell_Tumor-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Granular Cell Tumor
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Granular Cell Tumor** covering all of the
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
- **Disease Name:** Granular Cell Tumor
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Granular Cell Tumor** covering all of the
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


# Comprehensive Research Report: Granular Cell Tumor (GCT)

---

## 1. Disease Information

### Overview

Granular cell tumor (GCT) is a rare neuroectodermal soft tissue neoplasm derived principally from Schwann cells of the peripheral nervous system (franca2021whole‐exomesequencingreveals pages 1-4, moniruddin2023granularcelltumors pages 1-3). First described in 1926, GCTs were originally termed "granular cell myoblastoma" based on the erroneous belief that they originated from skeletal muscle; they are now recognized as neural in origin based on immunohistochemical and ultrastructural evidence showing S-100 protein positivity and features consistent with Schwann cell differentiation (torrado2023antiangiogenicsinmalignant pages 1-2, moniruddin2023granularcelltumors pages 1-3). GCTs represent approximately 0.5% of all soft tissue sarcomas and are overwhelmingly benign (~98%), with only approximately 2% classified as malignant (torrado2023antiangiogenicsinmalignant pages 1-2, moniruddin2023granularcelltumors pages 1-3).

### Key Identifiers

- **MONDO IDs:** MONDO:0006235 (granular cell tumor), MONDO:0003250 (benign granular cell tumor), MONDO:0002291 (cutaneous granular cell tumor), MONDO:0003251 (esophageal granular cell tumor), MONDO:0003256 (neurohypophysis granular cell tumor) (OpenTargets Search: granular cell tumor)
- **ICD-10:** D21 (other benign neoplasms of connective and soft tissue), site-specific coding depending on anatomical location
- **MeSH:** Granular Cell Tumor (D016586)
- **Synonyms:** Abrikossoff tumor, granular cell myoblastoma (historical), granular cell schwannoma, granular cell neurofibroma (torrado2023antiangiogenicsinmalignant pages 1-2, moniruddin2023granularcelltumors pages 1-3)

The following table provides a summary of core disease characteristics:

| Category | Granular Cell Tumor (GCT) summary |
|---|---|
| Disease name | Granular cell tumor (GCT) |
| MONDO identifiers | MONDO:0006235 granular cell tumor; MONDO:0003250 benign granular cell tumor; MONDO:0002291 cutaneous granular cell tumor; MONDO:0003251 esophageal granular cell tumor; MONDO:0003256 neurohypophysis granular cell tumor (OpenTargets Search: granular cell tumor) |
| Other identifiers | ICD-10 and MeSH were not established in the retrieved evidence set; use MONDO above and site-specific coding in implementation workflows when needed (OpenTargets Search: granular cell tumor) |
| Common synonyms | Abrikossoff tumor; granular cell myoblastoma; granular cell schwannoma; granular cell neurofibroma (historical/alternative usage in literature) (torrado2023antiangiogenicsinmalignant pages 1-2, moniruddin2023granularcelltumors pages 1-3) |
| Evidence source type | Primarily aggregated disease-level reviews plus case series/case reports and tumor sequencing studies; not EHR-derived in the retrieved evidence set (franca2021whole‐exomesequencingreveals pages 1-4, torrado2023antiangiogenicsinmalignant pages 1-2, moniruddin2023granularcelltumors pages 4-5) |
| Cell of origin / current understanding | Usually a Schwann-cell-derived neuroectodermal soft tissue neoplasm; neural GCTs are typically S100-positive. Rare non-neural GCTs are described and are often S100-negative/vimentin-positive (franca2021whole‐exomesequencingreveals pages 1-4, moniruddin2023granularcelltumors pages 4-5, moniruddin2023granularcelltumors pages 1-3) |
| Frequency / epidemiology | Ultra-rare tumor; estimated at ~0.5% of all soft tissue sarcomas. Most tumors are benign (~98%); malignant tumors are rare (~2%). Female predominance is consistently reported; peak incidence is usually in the 4th-6th decades, though cases occur across ages (torrado2023antiangiogenicsinmalignant pages 1-2, moniruddin2023granularcelltumors pages 1-3) |
| Key genetic alterations | Recurrent loss-of-function alterations in ATP6AP1, ATP6AP2, and ATP6V0C are a major molecular signature; V-ATPase pathway disruption is reported in up to ~72% of GCTs. Oral GCT sequencing also identified ATP6AP1 frameshift c.746_749del p.P249Hfs*4 and ATP6V1A p.D290N, plus variants in lysosomal/autophagosomal genes (franca2021whole‐exomesequencingreveals pages 1-4, franca2021whole‐exomesequencingreveals pages 4-6, torrado2023antiangiogenicsinmalignant pages 4-6, torrado2023antiangiogenicsinmalignant pages 2-4, franca2021whole‐exomesequencingreveals pages 11-15) |
| Key immunohistochemistry markers | Typical positive markers: S100, SOX10, CD68, inhibin, nestin, calretinin; additional reported positivity includes NSE, CD57, CD63/NKI-C3, vimentin. Myogenic and melanocytic markers are generally negative or only focally positive in rare cases (torrado2023antiangiogenicsinmalignant pages 2-4, palicelli2022s100immunohistochemicalpositivity pages 6-8, torrado2023antiangiogenicsinmalignant pages 1-2) |
| Histopathology | Non-encapsulated/infiltrative nests or sheets of polygonal cells with abundant eosinophilic granular cytoplasm; PAS-positive, diastase-resistant lysosomal granules; Pustulo-ovoid bodies of Milian; overlying pseudoepitheliomatous hyperplasia may occur (moniruddin2023granularcelltumors pages 1-3, torrado2023antiangiogenicsinmalignant pages 2-4, moniruddin2023granularcelltumors pages 3-4) |
| Classification system | Fanburg-Smith criteria: necrosis, mitotic activity >2/10 HPF, spindle cells, nuclear pleomorphism, vesicular nuclei with prominent nucleoli, and high nuclear-to-cytoplasmic ratio. 0 criteria = benign; 1-2 = atypical; ≥3 = malignant. Ki-67 is usually <5% in benign, 5-10% in atypical, and ~10-50% in malignant GCTs (torrado2023antiangiogenicsinmalignant pages 2-4, moniruddin2023granularcelltumors pages 5-6) |
| Primary anatomical sites | Can arise almost anywhere; commonly superficial soft tissues, especially skin/subcutis and head and neck. Frequent sites include tongue/oral cavity, gastrointestinal tract (especially esophagus), thoracic wall, upper extremities, breast, and less often internal organs (franca2021whole‐exomesequencingreveals pages 1-4, torrado2023antiangiogenicsinmalignant pages 1-2, moniruddin2023granularcelltumors pages 4-5, moniruddin2023granularcelltumors pages 1-3) |
| Clinical presentation | Usually a slow-growing, firm, small (often 5 mm-2 cm), painless/asymptomatic nodule or submucosal swelling; lesions are often solitary, but multifocal disease can occur (franca2021whole‐exomesequencingreveals pages 1-4, moniruddin2023granularcelltumors pages 4-5, moniruddin2023granularcelltumors pages 1-3) |
| Treatment options | Standard treatment for localized/resectable disease is complete surgical excision with negative margins. For unresectable/metastatic malignant GCT, evidence is limited; pazopanib is the best-supported systemic option in recent literature. Cytotoxic chemotherapy has generally shown limited activity; isolated reports describe disease control with PI3K inhibitors or pazopanib-based combinations (moniruddin2023granularcelltumors pages 5-6, torrado2023antiangiogenicsinmalignant pages 6-8, torrado2023antiangiogenicsinmalignant pages 1-2, torrado2023antiangiogenicsinmalignant pages 2-4, torrado2023antiangiogenicsinmalignant pages 8-9) |
| Pazopanib data | In the 2023 review of advanced malignant GCT, pazopanib produced disease control in 8/10 reported patients (80%) and objective RECIST response in 4/10 (40%); median time on therapy was ~7 months (torrado2023antiangiogenicsinmalignant pages 6-8, torrado2023antiangiogenicsinmalignant pages 1-2) |
| Prognosis: benign GCT | Generally excellent after complete excision; recurrence reported at ~2-8% with clear margins, increasing to ~20% with positive margins in some series/reviews (moniruddin2023granularcelltumors pages 5-6) |
| Prognosis: malignant/metastatic GCT | Aggressive course. Local recurrence up to ~32%; metastases in about half of malignant cases, often within 2 years; lungs and bone are common metastatic sites. Reported mortality is ~39% within 3 years for malignant GCT, and median overall survival for metastatic disease is ~10 months (torrado2023antiangiogenicsinmalignant pages 2-4, moniruddin2023granularcelltumors pages 5-6) |


*Table: This table summarizes the core disease characteristics of granular cell tumor, including identifiers, biology, pathology, clinical presentation, treatment, and prognosis. It is useful as a compact reference for disease knowledge base curation.*

---

## 2. Etiology

### Disease Causal Factors

GCTs arise from Schwann cells of peripheral nerves. The molecular hallmark is **loss-of-function mutations in vacuolar ATPase (V-ATPase) component genes**, particularly ATP6AP1, ATP6AP2, and ATP6V0C, which are found in approximately 72% of neural GCTs (moniruddin2023granularcelltumors pages 4-5, torrado2023antiangiogenicsinmalignant pages 2-4, torrado2023antiangiogenicsinmalignant pages 1-2). These mutations disrupt endosomal pH regulation, leading to impaired lysosomal acidification and the characteristic accumulation of intracytoplasmic lysosomal granules (franca2021whole‐exomesequencingreveals pages 1-4, franca2021whole‐exomesequencingreveals pages 6-8). Ultrastructurally, the granules are considered autophagosomes or autophagolysosomes consistent with myelin accumulation (franca2021whole‐exomesequencingreveals pages 1-4).

A rare non-neural variant of GCT exists that is S-100 negative and vimentin-positive, suggesting a mesenchymal rather than neural origin (moniruddin2023granularcelltumors pages 1-3).

### Risk Factors

- **Genetic risk factors:** GCTs can be associated with genetic syndromes including LEOPARD syndrome, neurofibromatosis type 1, Noonan syndrome, and Watson syndrome, highlighting the relevance of RAS-MAPK pathway germline variants (torrado2023antiangiogenicsinmalignant pages 1-2, torrado2023antiangiogenicsinmalignant pages 8-9).
- **Environmental risk factors:** No specific environmental, occupational, or lifestyle risk factors have been identified for GCT.
- **Sex:** Female predominance with male-to-female ratios reported as 2:3 to 1:2 (moniruddin2023granularcelltumors pages 1-3).
- **Race/ethnicity:** GCTs are more common in individuals of African descent (moniruddin2023granularcelltumors pages 1-3).
- **Age:** Peak incidence between the 3rd and 6th decades of life, with median age around 32 years in oral GCT series, though they can occur at any age (franca2021whole‐exomesequencingreveals pages 4-6, moniruddin2023granularcelltumors pages 1-3).

### Gene-Environment Interactions

No significant gene-environment interactions have been established for GCT. The disease appears driven primarily by somatic genetic events in V-ATPase pathway genes.

---

## 3. Phenotypes

### Clinical Presentation

GCTs typically present as firm, skin-colored to brownish-red nodules that are usually small (5 mm to 2 cm), slow-growing, and often asymptomatic (moniruddin2023granularcelltumors pages 1-3). Lesions are usually solitary, though multifocal presentations can occur. Submucosal lesions, particularly in the tongue and esophagus, may appear yellowish and smooth-surfaced (moniruddin2023granularcelltumors pages 4-5).

### Phenotype Characteristics

- **Subcutaneous/dermal nodule** (HP:0001072 - Nodular skin lesion): Most common presentation; firm, painless, small; mild functional impact unless in sensitive locations.
- **Oral/tongue mass** (HP:0010280 - Stomatitis or oral lesion): May cause discomfort during eating or speaking in larger lesions; the tongue is the single most common intra-oral site.
- **Dysphagia** (HP:0002015): When GCT involves the esophagus; can significantly impact quality of life.
- **Airway obstruction** (HP:0002781 - Upper airway obstruction): When GCT involves the larynx; potentially life-threatening in pediatric cases.
- **Pseudoepitheliomatous hyperplasia of overlying epithelium** (HP:0000966): A histologic feature that can mimic squamous cell carcinoma clinically and histologically.

### Features of Malignancy

Features suggesting malignancy include tumor size >3 cm, local tissue destruction, infiltrative edges, frequent mitoses, and large vesicular nuclei (moniruddin2023granularcelltumors pages 4-5).

---

## 4. Genetic/Molecular Information

### Causal Genes

The primary molecular signature of GCT involves recurrent inactivating somatic mutations in V-ATPase component genes:

- **ATP6AP1** (Xq28): V-ATPase accessory protein 1; frameshift and loss-of-function mutations including c.746_749del (p.P249Hfs*4) (franca2021whole‐exomesequencingreveals pages 4-6, franca2021whole‐exomesequencingreveals pages 11-15)
- **ATP6AP2** (Xp11.4): V-ATPase accessory protein 2; loss-of-function mutations (moniruddin2023granularcelltumors pages 4-5, torrado2023antiangiogenicsinmalignant pages 2-4)
- **ATP6V0C**: V-ATPase V0 subunit c; inactivating mutations (torrado2023antiangiogenicsinmalignant pages 2-4, torrado2023antiangiogenicsinmalignant pages 4-6)
- **ATP6V1A**: Novel nonsynonymous variant c.G868A (p.D290N) in the catalytic subunit, located in the ATP-Synt_ab functional domain (franca2021whole‐exomesequencingreveals pages 4-6, franca2021whole‐exomesequencingreveals pages 11-15)

### Additional Genetic Alterations

In malignant GCTs specifically, alterations in **TP53** and **PIK3CA** have been reported, distinguishing them from benign tumors (torrado2023antiangiogenicsinmalignant pages 4-6). Additional mutations have been identified in TGFβ pathway genes (TGFBR1, TGFBR2, LTBP2) and MAPK pathway genes (MAP3K15) (torrado2023antiangiogenicsinmalignant pages 4-6). Whole-exome sequencing of oral GCTs has also revealed variants in genes involved in lysosomal biology, including ABCA8, ABCC6, AGAP3, ATG9A, CTSB, DNAJC13, GALC, NPC1, SLC15A3, SLC31A2, and TMEM104 (franca2021whole‐exomesequencingreveals pages 1-4, franca2021whole‐exomesequencingreveals pages 8-11).

The following table details the molecular pathways implicated in GCT pathogenesis:

| Pathway/Gene | Type of Alteration | Functional Consequence | Frequency in GCTs | Therapeutic Relevance |
|---|---|---|---|---|
| **ATP6AP1** | Recurrent somatic loss-of-function; frameshift variants reported | Impairs V-ATPase accessory function, disrupts endosomal/lysosomal acidification, promotes lysosomal/autophagosomal granule accumulation characteristic of GCT | Part of the recurrent V-ATPase gene set present in ~72% of GCTs; individual-gene frequency varies (torrado2023antiangiogenicsinmalignant pages 1-2, torrado2023antiangiogenicsinmalignant pages 2-4, franca2021whole‐exomesequencingreveals pages 4-6) | Core diagnostic molecular feature; mechanistic rationale for targeting downstream RTK signaling, especially pazopanib-sensitive kinase networks (torrado2023antiangiogenicsinmalignant pages 1-2) |
| **ATP6AP2** | Recurrent somatic loss-of-function | V-ATPase dysfunction with abnormal vesicle acidification; enhances oncogenic signaling downstream of lysosomal stress | Part of the recurrent V-ATPase gene set present in ~72% of GCTs (moniruddin2023granularcelltumors pages 4-5, torrado2023antiangiogenicsinmalignant pages 2-4, torrado2023antiangiogenicsinmalignant pages 1-2) | Supports targeted therapy rationale via downstream PDGFR-β/SFK/STAT5 activation; also useful diagnostically (torrado2023antiangiogenicsinmalignant pages 1-2, torrado2023antiangiogenicsinmalignant pages 6-8) |
| **ATP6V0C** | Recurrent inactivating/loss-of-function mutation | Disrupts V-ATPase proton pump function and lysosomal homeostasis | Included among recurrent V-ATPase alterations in up to ~72% of GCTs (torrado2023antiangiogenicsinmalignant pages 2-4, torrado2023antiangiogenicsinmalignant pages 4-6, franca2021whole‐exomesequencingreveals pages 4-6) | Supports pathway-based targeting of consequences of V-ATPase dysfunction rather than direct current gene-specific therapy (torrado2023antiangiogenicsinmalignant pages 4-6, franca2021whole‐exomesequencingreveals pages 6-8) |
| **PDGFR-β** | Increased phosphorylation/activation downstream of V-ATPase loss | Promotes oncogenic signaling, proliferation, and survival in Schwann-lineage tumor cells | Activation described as a downstream event in V-ATPase-mutant GCTs; prevalence not independently quantified (torrado2023antiangiogenicsinmalignant pages 4-6, torrado2023antiangiogenicsinmalignant pages 2-4, torrado2023antiangiogenicsinmalignant pages 1-2) | Major proposed kinase target; likely contributor to pazopanib activity in advanced/malignant GCT (torrado2023antiangiogenicsinmalignant pages 1-2, torrado2023antiangiogenicsinmalignant pages 8-9) |
| **SFK / Src family kinases** | Increased phosphorylation/activation | Enhances pro-oncogenic signaling downstream of ATP6AP1/2 loss | Activation described in V-ATPase-altered GCTs; exact frequency not separately reported (torrado2023antiangiogenicsinmalignant pages 4-6, torrado2023antiangiogenicsinmalignant pages 8-9, torrado2023antiangiogenicsinmalignant pages 1-2) | Provides rationale for kinase-directed therapy; dasatinib has been tried clinically but reported ineffective in isolated cases (torrado2023antiangiogenicsinmalignant pages 6-8, torrado2023antiangiogenicsinmalignant pages 4-6) |
| **STAT5a/b** | Increased signaling/phosphorylation | Supports proliferation and survival signaling downstream of lysosomal/V-ATPase dysfunction | Activation reported mechanistically; exact frequency not separately reported (torrado2023antiangiogenicsinmalignant pages 4-6, torrado2023antiangiogenicsinmalignant pages 8-9, torrado2023antiangiogenicsinmalignant pages 2-4) | Potential downstream vulnerability, though no established STAT5-targeted regimen exists for GCT (torrado2023antiangiogenicsinmalignant pages 4-6, torrado2023antiangiogenicsinmalignant pages 1-2) |
| **PI3K/AKT/mTOR pathway** | Pathway activation, especially in malignant GCT | Promotes cell survival, proliferation, motility, and aggressive behavior | Implicated particularly in malignant GCT; population frequency not established (torrado2023antiangiogenicsinmalignant pages 4-6) | Clinical relevance supported by a reported PI3K inhibitor achieving ~9 months disease control in one advanced case (torrado2023antiangiogenicsinmalignant pages 6-8, torrado2023antiangiogenicsinmalignant pages 8-9) |
| **TP53** | Alterations in malignant GCT | Associated with malignant progression and biologic aggressiveness | Reported in malignant GCTs; uncommon in benign conventional GCT; exact frequency not established (torrado2023antiangiogenicsinmalignant pages 4-6) | May help distinguish malignant biology; no GCT-specific targeted therapy established (torrado2023antiangiogenicsinmalignant pages 4-6) |
| **PIK3CA** | Alterations in malignant GCT | Activates PI3K signaling and may contribute to progression/aggressiveness | Reported in malignant GCTs; exact frequency not established (torrado2023antiangiogenicsinmalignant pages 4-6) | Supports consideration of PI3K-pathway inhibition in selected advanced cases (torrado2023antiangiogenicsinmalignant pages 6-8, torrado2023antiangiogenicsinmalignant pages 8-9, torrado2023antiangiogenicsinmalignant pages 4-6) |
| **TGFβ pathway (TGFBR1/TGFBR2)** | Mutations/alterations | Suggests additional pathway dysregulation contributing to tumorigenesis | Reported as additional alterations; frequency not established (torrado2023antiangiogenicsinmalignant pages 4-6) | Currently mainly biologic/interpretive relevance; no standard targeted use in GCT (torrado2023antiangiogenicsinmalignant pages 4-6) |
| **MAPK pathway (including MAP3K15)** | Mutations/alterations | May contribute to tumorigenesis and overlap with syndromic RAS-MAPK biology | Reported as additional alterations; frequency not established (torrado2023antiangiogenicsinmalignant pages 4-6, torrado2023antiangiogenicsinmalignant pages 8-9) | Supports exploration of MAPK-directed combinations; MEK-inhibitor combinations with pazopanib have been discussed experimentally in sarcoma contexts (torrado2023antiangiogenicsinmalignant pages 13-14, torrado2023antiangiogenicsinmalignant pages 8-9) |


*Table: This table summarizes the main genetic alterations and signaling pathways implicated in granular cell tumor pathogenesis, with their functional effects and therapeutic implications. It is useful for linking recurrent V-ATPase defects to downstream targetable signaling in malignant or advanced disease.*

### Somatic vs. Germline Origin

The V-ATPase mutations in GCTs are **somatic** in origin. However, germline mutations in RAS-MAPK pathway genes (as seen in Noonan syndrome, LEOPARD syndrome, and neurofibromatosis) create a predisposition to GCT development (torrado2023antiangiogenicsinmalignant pages 1-2, torrado2023antiangiogenicsinmalignant pages 8-9).

---

## 5. Environmental Information

No specific environmental factors, toxins, lifestyle factors, or infectious agents have been identified as contributing to GCT development. The disease appears driven primarily by somatic genetic alterations.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

The central pathogenic mechanism of GCT involves **V-ATPase dysfunction** caused by loss-of-function mutations in ATP6AP1/AP2/ATP6V0C genes (torrado2023antiangiogenicsinmalignant pages 2-4, torrado2023antiangiogenicsinmalignant pages 1-2, franca2021whole‐exomesequencingreveals pages 6-8). V-ATPases are multisubunit enzymes responsible for acidifying intracellular compartments and transporting protons across the plasma membrane (franca2021whole‐exomesequencingreveals pages 6-8). When these proton pumps are impaired in Schwann cells, a cascade of pathological events occurs:

1. **Lysosomal dysfunction:** Decreased lysosomal acidification leads to impaired degradation of intracellular substrates, resulting in the characteristic accumulation of autophagosomes/autophagolysosomes containing myelin material — the granules that define GCTs (franca2021whole‐exomesequencingreveals pages 1-4, franca2021whole‐exomesequencingreveals pages 6-8, franca2021whole‐exomesequencingreveals pages 8-11).

2. **Downstream oncogenic signaling:** V-ATPase dysfunction leads to increased phosphorylation and activation of PDGFR-β, Src family kinases (SFKs), and STAT5a/b, promoting oncogenic signaling, cell proliferation, and survival (torrado2023antiangiogenicsinmalignant pages 4-6, torrado2023antiangiogenicsinmalignant pages 8-9, torrado2023antiangiogenicsinmalignant pages 2-4, torrado2023antiangiogenicsinmalignant pages 1-2).

3. **Transcription factor activation:** Lysosomal inhibition activates transcription factors MITF, TFE3, and TFEB (torrado2023antiangiogenicsinmalignant pages 4-6).

4. **S100 protein-mediated proliferation:** S100 protein released from damaged Schwann cells activates migration and cell proliferation, reinforcing tumor growth (torrado2023antiangiogenicsinmalignant pages 2-4).

5. **PI3K/AKT/mTOR pathway:** Activated by upstream receptor tyrosine kinases (EGFR, HER2, RET, MET, VEGFR), this pathway promotes cell survival, proliferation, and motility, particularly in malignant GCTs (torrado2023antiangiogenicsinmalignant pages 4-6).

### Suggested GO Terms
- GO:0006914 (autophagy)
- GO:0007041 (lysosomal transport)
- GO:0015078 (proton transmembrane transporter activity)
- GO:0005764 (lysosome — Cellular Component)
- GO:0000421 (autophagosome membrane — Cellular Component)

### Cell Types Involved
- CL:0002573 (Schwann cell) — primary cell of origin
- CL:0000540 (neuron) — associated tissue context

---

## 7. Anatomical Structures Affected

### Organ Level

GCTs can develop at virtually any anatomical site. The most common locations include (franca2021whole‐exomesequencingreveals pages 1-4, torrado2023antiangiogenicsinmalignant pages 1-2, moniruddin2023granularcelltumors pages 4-5, moniruddin2023granularcelltumors pages 1-3):

- **Skin and subcutaneous tissue** (30-40% of cases): Especially the upper body, head and neck (UBERON:0002097 — skin of body)
- **Oral cavity/tongue** (most common single intra-oral site): UBERON:0001723 — tongue
- **Gastrointestinal tract** (especially esophagus): UBERON:0001043 — esophagus
- **Breast**: UBERON:0000310 — breast
- **Respiratory tract** (larynx, bronchi): UBERON:0001737 — larynx
- **Sellar/pituitary region** (neurohypophysis): UBERON:0002198 — neurohypophysis
- **Other sites:** thoracic wall, upper extremities, biliary tract, vulva, orbit, perianal region

### Tissue and Cell Level

- **Affected tissue:** Peripheral nerve sheath tissue, soft tissue (UBERON:0003714 — neural tissue)
- **Primary cell population:** Schwann cells (CL:0002573)
- **Subcellular compartments:** Lysosomes (GO:0005764), autophagosomes (GO:0005776), endosomes

---

## 8. Temporal Development

### Onset

- **Typical age of onset:** Third to sixth decades of life (peak in fourth decade); can occur at any age including pediatric (torrado2023antiangiogenicsinmalignant pages 1-2, franca2021whole‐exomesequencingreveals pages 4-6, moniruddin2023granularcelltumors pages 1-3)
- **Onset pattern:** Insidious/chronic; typically slow-growing over months to years

### Progression

- **Benign GCTs:** Stable or slowly progressive; rarely transform to malignancy
- **Malignant GCTs:** Aggressive course with local recurrence rates up to 32% and metastases in approximately half of patients, typically within 2 years (moniruddin2023granularcelltumors pages 5-6)
- **Metastatic sites:** Lungs and bones are the most common (torrado2023antiangiogenicsinmalignant pages 2-4)

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence:** Ultra-rare; GCTs constitute approximately 0.5% of all soft tissue sarcomas (torrado2023antiangiogenicsinmalignant pages 1-2)
- **Sex ratio:** Female predominance (male:female approximately 2:3 to 1:2) (moniruddin2023granularcelltumors pages 1-3)
- **Racial distribution:** More common in African-American/Black populations (moniruddin2023granularcelltumors pages 1-3)
- **Age distribution:** Broad range (10-61+ years in one oral GCT series), median ~32 years, peak in 4th-6th decades (franca2021whole‐exomesequencingreveals pages 4-6, moniruddin2023granularcelltumors pages 1-3)

### Genetic Aspects

GCTs are typically sporadic with somatic mutations. However, syndromic associations exist with LEOPARD syndrome, neurofibromatosis, Noonan syndrome, and Watson syndrome, all involving germline RAS-MAPK pathway mutations (torrado2023antiangiogenicsinmalignant pages 1-2, torrado2023antiangiogenicsinmalignant pages 8-9). Multifocal GCTs have been reported and may suggest an underlying genetic predisposition.

---

## 10. Diagnostics

### Histopathology

The gold standard for diagnosis is histopathological examination of biopsy or excision specimens. Key features include (moniruddin2023granularcelltumors pages 1-3, torrado2023antiangiogenicsinmalignant pages 2-4, moniruddin2023granularcelltumors pages 3-4):

- Non-encapsulated, infiltrative nests or sheets of large polygonal/polyhedral cells
- Abundant eosinophilic, finely or coarsely granular cytoplasm (PAS-positive, diastase-resistant)
- Small, uniform, centrally or eccentrically placed nuclei
- **Pustulo-ovoid bodies of Milian** — large eosinophilic granules with clear halos, pathognomonic
- Overlying pseudoepitheliomatous hyperplasia (can mimic squamous cell carcinoma)
- Rare mitotic figures in benign tumors

### Immunohistochemistry Panel

Neural GCTs are characteristically positive for (torrado2023antiangiogenicsinmalignant pages 2-4, palicelli2022s100immunohistochemicalpositivity pages 6-8, torrado2023antiangiogenicsinmalignant pages 1-2):

- **S-100 protein** (consistently positive — most important marker)
- **SOX10** (positive)
- **CD68** (positive)
- **Inhibin-alpha** (positive)
- **Nestin** (positive)
- **Calretinin** (positive)
- **NSE (neuron-specific enolase)** and **CD57** (positive)
- **CD63/NKI-C3** (positive)
- **TFE3** (positive)
- **Vimentin** (positive)
- **Myogenic markers** (desmin, SMA): typically negative
- **Melanocytic markers** (Melan-A, HMB-45): negative or only rarely focal

Non-neural GCTs are S-100 negative but vimentin-positive (moniruddin2023granularcelltumors pages 1-3).

### Fanburg-Smith Classification (Malignancy Grading)

The Fanburg-Smith system evaluates six histologic criteria (torrado2023antiangiogenicsinmalignant pages 2-4, moniruddin2023granularcelltumors pages 5-6):
1. Necrosis
2. Increased mitotic count (>2 per 10 HPF)
3. Spindled tumor cells
4. Nuclear pleomorphism
5. Vesicular nuclei with prominent nucleoli
6. High nuclear-to-cytoplasmic ratio

- **0 criteria:** Benign
- **1-2 criteria:** Atypical
- **≥3 criteria:** Malignant

### Ki-67 Proliferation Index

- Benign GCT: <5%
- Atypical GCT: 5-10%
- Malignant GCT: 10-50% (torrado2023antiangiogenicsinmalignant pages 2-4)

### Molecular Diagnostics

Sequencing for ATP6AP1 and ATP6AP2 mutations can be used diagnostically, particularly to distinguish atypical GCT from melanoma in challenging cases. These mutations are considered pathognomonic for GCT (torrado2023antiangiogenicsinmalignant pages 1-2).

### Imaging

GCTs typically appear as well-defined submucosal or subcutaneous masses on ultrasound, CT, and MRI. Endoscopic ultrasound is particularly useful for esophageal GCTs.

### Differential Diagnosis

- Congenital granular cell epulis (S-100 negative, unlike GCT) (cheung2020congenitalgranularcell pages 1-3)
- Adult rhabdomyoma (may be S-100 positive; desmin-positive unlike GCT) (palicelli2022s100immunohistochemicalpositivity pages 6-8)
- Malignant melanoma
- Squamous cell carcinoma (due to overlying pseudoepitheliomatous hyperplasia)
- Alveolar soft part sarcoma
- Other nerve sheath tumors (schwannoma, neurofibroma)

---

## 11. Outcome / Prognosis

### Benign GCT

- Excellent prognosis after complete surgical excision
- Recurrence rate: 2-8% with clear margins; up to 20% with positive margins (moniruddin2023granularcelltumors pages 5-6)
- Long-term follow-up recommended at least annually for 2 years (moniruddin2023granularcelltumors pages 5-6)

### Malignant GCT

- Aggressive behavior with poor prognosis
- Local recurrence rate: up to 32% (moniruddin2023granularcelltumors pages 5-6)
- Metastasis: approximately 50% of malignant cases, typically within 2 years, most commonly to lungs and bones (torrado2023antiangiogenicsinmalignant pages 2-4, moniruddin2023granularcelltumors pages 5-6)
- Mortality: approximately 39% within 3 years (moniruddin2023granularcelltumors pages 5-6)
- Median overall survival for metastatic disease: approximately 10 months (torrado2023antiangiogenicsinmalignant pages 2-4)

---

## 12. Treatment

### Surgical Treatment (MAXO:0000004 — surgical procedure)

Complete surgical excision with wide negative margins is the standard of care for all resectable GCTs and is curative for the vast majority of benign tumors (moniruddin2023granularcelltumors pages 5-6, torrado2023antiangiogenicsinmalignant pages 2-4). Margin status is critical: positive margins are associated with significantly higher recurrence rates (moniruddin2023granularcelltumors pages 5-6).

### Systemic Therapy for Advanced/Metastatic GCT

#### Pazopanib (MAXO:0000058 — pharmacotherapy)

Pazopanib, a multi-tyrosine kinase inhibitor targeting VEGFR, PDGFR, and c-KIT, is the best-supported systemic therapy for advanced malignant GCT. In a 2023 systematic review of 10 case reports (torrado2023antiangiogenicsinmalignant pages 6-8, torrado2023antiangiogenicsinmalignant pages 1-2):
- **Disease control rate:** 80% (8/10 patients)
- **Objective RECIST response rate:** 40% (4/10 patients)
- **Median time on therapy:** 7 months
- This response rate (40%) substantially exceeds the approximately 6% overall response rate seen with pazopanib in other soft tissue sarcoma subtypes (torrado2023antiangiogenicsinmalignant pages 8-9)

The rationale for pazopanib activity in GCT is linked to the enhanced PDGFR-β phosphorylation resulting from ATP6AP1/AP2 loss-of-function mutations (torrado2023antiangiogenicsinmalignant pages 8-9, torrado2023antiangiogenicsinmalignant pages 1-2).

#### Chemotherapy

GCTs are generally chemo-resistant. Limited reports describe responses to (moniruddin2023granularcelltumors pages 5-6, torrado2023antiangiogenicsinmalignant pages 8-9):
- Gemcitabine plus paclitaxel
- Carboplatin plus etoposide
However, five previously treated patients who received standard cytotoxic chemotherapy (carboplatin/paclitaxel with cetuximab, gemcitabine/docetaxel, doxorubicin/ifosfamide) showed no objective responses (torrado2023antiangiogenicsinmalignant pages 6-8).

#### Other Targeted Therapies

- **PI3K inhibitors:** Disease control for 9 months reported in one patient (torrado2023antiangiogenicsinmalignant pages 6-8, torrado2023antiangiogenicsinmalignant pages 8-9)
- **Pazopanib plus crizotinib:** Disease control for 4 months in one patient (torrado2023antiangiogenicsinmalignant pages 6-8)
- **Dasatinib:** Reported as ineffective in one case (torrado2023antiangiogenicsinmalignant pages 6-8)
- **Megestrol:** Reported as ineffective in one case (torrado2023antiangiogenicsinmalignant pages 6-8)

#### Investigational Combination Strategies

Potential combination strategies under discussion include (torrado2023antiangiogenicsinmalignant pages 13-14, torrado2023antiangiogenicsinmalignant pages 8-9):
- Pazopanib plus trametinib (MEK inhibitor)
- Pazopanib plus abexinostat (HDAC inhibitor)
- Immunotherapy combinations (nivolumab with sunitinib; axitinib with pembrolizumab)

### Treatment Strategy

No standardized treatment guidelines exist for metastatic GCT due to its ultra-rare nature. Current evidence supports pazopanib as the preferred systemic option for advanced disease (torrado2023antiangiogenicsinmalignant pages 1-2, torrado2023antiangiogenicsinmalignant pages 2-4). Clinical trial participation is encouraged for patients with unresectable or metastatic disease.

---

## 13. Prevention

No specific primary or secondary prevention strategies exist for GCT. There are no established screening programs, given the sporadic nature and rarity of the disease. For patients with syndromic associations (Noonan syndrome, neurofibromatosis), general cancer surveillance protocols should be followed. Genetic counseling may be relevant for patients with multifocal GCTs to evaluate for underlying syndromic predisposition (torrado2023antiangiogenicsinmalignant pages 1-2).

---

## 14. Other Species / Natural Disease

### Veterinary Relevance

GCTs have been reported in domestic animals, notably testicular granular cell tumors in domestic rabbits (*Oryctolagus cuniculus*). GCTs are uncommon in veterinary pathology and have not been extensively characterized at the molecular level in animals. Comparative pathology studies on peripheral nerve sheath tumors in domestic animals describe Schwann cell-derived lesions in dogs and cats, though GCT-specific data in these species is very limited (OpenTargets Search: granular cell tumor).

---

## 15. Model Organisms

No established in vivo animal models (knockout, knock-in, or transgenic) have been developed specifically for GCT. The molecular study of GCTs relies almost exclusively on human clinical specimens, including formalin-fixed paraffin-embedded tissue subjected to whole-exome sequencing and immunohistochemistry (franca2021whole‐exomesequencingreveals pages 1-4, franca2021whole‐exomesequencingreveals pages 4-6). The identification of ATP6AP1/AP2 as driver genes could theoretically enable future model development through conditional knockout approaches in Schwann cell lineage, but such models have not yet been reported in the literature.

---

## Summary

Granular cell tumor is an ultra-rare neuroectodermal neoplasm of Schwann cell origin characterized by a pathognomonic molecular signature of loss-of-function mutations in V-ATPase component genes (ATP6AP1, ATP6AP2, ATP6V0C), present in approximately 72% of cases (moniruddin2023granularcelltumors pages 4-5, torrado2023antiangiogenicsinmalignant pages 1-2). These mutations cause impaired lysosomal acidification and downstream activation of PDGFR-β, SFK, and STAT5 signaling pathways (torrado2023antiangiogenicsinmalignant pages 4-6, torrado2023antiangiogenicsinmalignant pages 2-4). The vast majority of GCTs are benign and curable by surgical excision, while the rare malignant variant carries a poor prognosis with median overall survival of approximately 10 months in the metastatic setting (torrado2023antiangiogenicsinmalignant pages 2-4). Pazopanib represents the most promising systemic therapy for advanced disease, with an 80% disease control rate and 40% objective response rate in reported cases (torrado2023antiangiogenicsinmalignant pages 6-8, torrado2023antiangiogenicsinmalignant pages 1-2). Future research should focus on developing formal clinical trials for pazopanib in GCT, exploring PI3K/mTOR-directed therapy, and creating preclinical models to further elucidate the biology of this rare tumor.

References

1. (franca2021whole‐exomesequencingreveals pages 1-4): Josiane Alves França, Tenzin Gayden, Eric Bareke, Jean Nunes Santos, Sílvia Ferreira de Sousa, Luciana Bastos‐Rodrigues, Jacek Majewski, Nada Jabado, Ricardo Santiago Gomez, and Carolina Cavalieri Gomes. Whole‐exome sequencing reveals novel vacuolar atpase genes’ variants and variants in genes involved in lysosomal biology and autophagosomal formation in oral granular cell tumors. Dec 2021. URL: https://doi.org/10.1111/jop.13148, doi:10.1111/jop.13148. This article has 13 citations and is from a domain leading peer-reviewed journal.

2. (moniruddin2023granularcelltumors pages 1-3): ABM Moniruddin, Halima Khatun Doly, Shakila Jannat, Tanvirul Hasan, and MA Rouf. Granular cell tumors. KYAMC Journal, 14:96-101, Oct 2023. URL: https://doi.org/10.3329/kyamcj.v14i02.68561, doi:10.3329/kyamcj.v14i02.68561. This article has 0 citations.

3. (torrado2023antiangiogenicsinmalignant pages 1-2): Carlos Torrado, Melisa Camaño, Nadia Hindi, Justo Ortega, Alberto R. Sevillano, Gema Civantos, David S. Moura, Alessandra Dimino, and Javier Martín-Broto. Antiangiogenics in malignant granular cell tumors: review of the literature. Cancers, 15:5187, Oct 2023. URL: https://doi.org/10.3390/cancers15215187, doi:10.3390/cancers15215187. This article has 4 citations.

4. (OpenTargets Search: granular cell tumor): Open Targets Query (granular cell tumor, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (moniruddin2023granularcelltumors pages 4-5): ABM Moniruddin, Halima Khatun Doly, Shakila Jannat, Tanvirul Hasan, and MA Rouf. Granular cell tumors. KYAMC Journal, 14:96-101, Oct 2023. URL: https://doi.org/10.3329/kyamcj.v14i02.68561, doi:10.3329/kyamcj.v14i02.68561. This article has 0 citations.

6. (franca2021whole‐exomesequencingreveals pages 4-6): Josiane Alves França, Tenzin Gayden, Eric Bareke, Jean Nunes Santos, Sílvia Ferreira de Sousa, Luciana Bastos‐Rodrigues, Jacek Majewski, Nada Jabado, Ricardo Santiago Gomez, and Carolina Cavalieri Gomes. Whole‐exome sequencing reveals novel vacuolar atpase genes’ variants and variants in genes involved in lysosomal biology and autophagosomal formation in oral granular cell tumors. Dec 2021. URL: https://doi.org/10.1111/jop.13148, doi:10.1111/jop.13148. This article has 13 citations and is from a domain leading peer-reviewed journal.

7. (torrado2023antiangiogenicsinmalignant pages 4-6): Carlos Torrado, Melisa Camaño, Nadia Hindi, Justo Ortega, Alberto R. Sevillano, Gema Civantos, David S. Moura, Alessandra Dimino, and Javier Martín-Broto. Antiangiogenics in malignant granular cell tumors: review of the literature. Cancers, 15:5187, Oct 2023. URL: https://doi.org/10.3390/cancers15215187, doi:10.3390/cancers15215187. This article has 4 citations.

8. (torrado2023antiangiogenicsinmalignant pages 2-4): Carlos Torrado, Melisa Camaño, Nadia Hindi, Justo Ortega, Alberto R. Sevillano, Gema Civantos, David S. Moura, Alessandra Dimino, and Javier Martín-Broto. Antiangiogenics in malignant granular cell tumors: review of the literature. Cancers, 15:5187, Oct 2023. URL: https://doi.org/10.3390/cancers15215187, doi:10.3390/cancers15215187. This article has 4 citations.

9. (franca2021whole‐exomesequencingreveals pages 11-15): Josiane Alves França, Tenzin Gayden, Eric Bareke, Jean Nunes Santos, Sílvia Ferreira de Sousa, Luciana Bastos‐Rodrigues, Jacek Majewski, Nada Jabado, Ricardo Santiago Gomez, and Carolina Cavalieri Gomes. Whole‐exome sequencing reveals novel vacuolar atpase genes’ variants and variants in genes involved in lysosomal biology and autophagosomal formation in oral granular cell tumors. Dec 2021. URL: https://doi.org/10.1111/jop.13148, doi:10.1111/jop.13148. This article has 13 citations and is from a domain leading peer-reviewed journal.

10. (palicelli2022s100immunohistochemicalpositivity pages 6-8): Andrea Palicelli, Antonio Ramponi, Guido Valente, Renzo Boldorini, Annalisa Balbo Mussetto, and Magda Zanelli. S-100 immunohistochemical positivity in rhabdomyoma: an underestimated potential diagnostic pitfall in routine practice. Diagnostics, 12:892, Apr 2022. URL: https://doi.org/10.3390/diagnostics12040892, doi:10.3390/diagnostics12040892. This article has 6 citations.

11. (moniruddin2023granularcelltumors pages 3-4): ABM Moniruddin, Halima Khatun Doly, Shakila Jannat, Tanvirul Hasan, and MA Rouf. Granular cell tumors. KYAMC Journal, 14:96-101, Oct 2023. URL: https://doi.org/10.3329/kyamcj.v14i02.68561, doi:10.3329/kyamcj.v14i02.68561. This article has 0 citations.

12. (moniruddin2023granularcelltumors pages 5-6): ABM Moniruddin, Halima Khatun Doly, Shakila Jannat, Tanvirul Hasan, and MA Rouf. Granular cell tumors. KYAMC Journal, 14:96-101, Oct 2023. URL: https://doi.org/10.3329/kyamcj.v14i02.68561, doi:10.3329/kyamcj.v14i02.68561. This article has 0 citations.

13. (torrado2023antiangiogenicsinmalignant pages 6-8): Carlos Torrado, Melisa Camaño, Nadia Hindi, Justo Ortega, Alberto R. Sevillano, Gema Civantos, David S. Moura, Alessandra Dimino, and Javier Martín-Broto. Antiangiogenics in malignant granular cell tumors: review of the literature. Cancers, 15:5187, Oct 2023. URL: https://doi.org/10.3390/cancers15215187, doi:10.3390/cancers15215187. This article has 4 citations.

14. (torrado2023antiangiogenicsinmalignant pages 8-9): Carlos Torrado, Melisa Camaño, Nadia Hindi, Justo Ortega, Alberto R. Sevillano, Gema Civantos, David S. Moura, Alessandra Dimino, and Javier Martín-Broto. Antiangiogenics in malignant granular cell tumors: review of the literature. Cancers, 15:5187, Oct 2023. URL: https://doi.org/10.3390/cancers15215187, doi:10.3390/cancers15215187. This article has 4 citations.

15. (franca2021whole‐exomesequencingreveals pages 6-8): Josiane Alves França, Tenzin Gayden, Eric Bareke, Jean Nunes Santos, Sílvia Ferreira de Sousa, Luciana Bastos‐Rodrigues, Jacek Majewski, Nada Jabado, Ricardo Santiago Gomez, and Carolina Cavalieri Gomes. Whole‐exome sequencing reveals novel vacuolar atpase genes’ variants and variants in genes involved in lysosomal biology and autophagosomal formation in oral granular cell tumors. Dec 2021. URL: https://doi.org/10.1111/jop.13148, doi:10.1111/jop.13148. This article has 13 citations and is from a domain leading peer-reviewed journal.

16. (franca2021whole‐exomesequencingreveals pages 8-11): Josiane Alves França, Tenzin Gayden, Eric Bareke, Jean Nunes Santos, Sílvia Ferreira de Sousa, Luciana Bastos‐Rodrigues, Jacek Majewski, Nada Jabado, Ricardo Santiago Gomez, and Carolina Cavalieri Gomes. Whole‐exome sequencing reveals novel vacuolar atpase genes’ variants and variants in genes involved in lysosomal biology and autophagosomal formation in oral granular cell tumors. Dec 2021. URL: https://doi.org/10.1111/jop.13148, doi:10.1111/jop.13148. This article has 13 citations and is from a domain leading peer-reviewed journal.

17. (torrado2023antiangiogenicsinmalignant pages 13-14): Carlos Torrado, Melisa Camaño, Nadia Hindi, Justo Ortega, Alberto R. Sevillano, Gema Civantos, David S. Moura, Alessandra Dimino, and Javier Martín-Broto. Antiangiogenics in malignant granular cell tumors: review of the literature. Cancers, 15:5187, Oct 2023. URL: https://doi.org/10.3390/cancers15215187, doi:10.3390/cancers15215187. This article has 4 citations.

18. (cheung2020congenitalgranularcell pages 1-3): Justin M. Cheung and Juan Putra. Congenital granular cell epulis: classic presentation and its differential diagnosis. Head and Neck Pathology, 14:208-211, Mar 2020. URL: https://doi.org/10.1007/s12105-019-01025-1, doi:10.1007/s12105-019-01025-1. This article has 52 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Granular_Cell_Tumor-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Granular_Cell_Tumor-deep-research-falcon_artifacts/artifact-01.md)