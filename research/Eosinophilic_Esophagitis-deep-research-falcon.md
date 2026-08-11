---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T18:50:25.578197'
end_time: '2026-07-05T19:06:04.205005'
duration_seconds: 938.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Eosinophilic Esophagitis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 49
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Eosinophilic_Esophagitis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Eosinophilic_Esophagitis-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Eosinophilic Esophagitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Eosinophilic Esophagitis** covering all of the
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
- **Disease Name:** Eosinophilic Esophagitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Eosinophilic Esophagitis** covering all of the
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


# Comprehensive Research Report: Eosinophilic Esophagitis (EoE)

## 1. Disease Information

### Overview
Eosinophilic esophagitis (EoE) is a chronic, immune-mediated inflammatory disease of the esophagus characterized clinically by symptoms of esophageal dysfunction and histologically by eosinophil-predominant inflammation of the esophageal squamous epithelium (farah2025thedynamicevolution pages 2-4, gautam2026eosinophilicesophagitismechanisms pages 1-2). EoE is now recognized as a leading cause of dysphagia and food impaction in both children and adults, with its incidence and prevalence rising significantly over the past three decades (gautam2026eosinophilicesophagitismechanisms pages 1-2). The condition is classified as a type 2 inflammatory disease driven primarily by food allergen-mediated immune responses (farah2025thedynamicevolution pages 4-5, khokhar2022eosinophilicesophagitisimmune pages 1-2).

### Key Identifiers
- **MONDO ID:** MONDO_0005361 (OpenTargets Search: eosinophilic esophagitis)
- **ICD-10:** K20.0
- **ICD-11:** DA22.0
- **MeSH:** D057765
- **OMIM:** 610247 (Eosinophilic Esophagitis)
- **Orphanet:** ORPHA:73247

### Common Synonyms
- EoE
- Allergic esophagitis
- Eosinophilic oesophagitis
- Primary eosinophilic esophagitis

### Data Source
The information in this report is derived from aggregated disease-level resources including systematic reviews, meta-analyses, clinical guidelines (ACG 2025, ESPGHAN 2024), genome-wide association studies, clinical trials, and the OpenTargets database.

---

## 2. Etiology

### Disease Causal Factors
EoE results from a complex interplay of genetic predisposition, environmental exposures, epithelial barrier dysfunction, and abnormal type 2 immune responses (gautam2026eosinophilicesophagitismechanisms pages 1-2). The disease is fundamentally a food allergen-driven condition, confirmed by the universal response to elemental formula diets that eliminate all intact food proteins (low2024reviewarticleemerging pages 4-6). Key causal factors include:

- **Genetic susceptibility:** GWAS have identified multiple susceptibility loci including 5q22 (TSLP/WDR36), 2p23 (CAPN14), 11q13 (LRRC32/C11orf30), and 12q13 (STAT6), with recent expansions to 24 loci and 90 candidate genes (khokhar2022eosinophilicesophagitisimmune pages 1-2, low2024reviewarticleemerging pages 4-6, trimarchi2026multitraitanalysisof pages 10-11).
- **Environmental triggers:** Dietary allergens (milk, wheat, eggs, soy), aeroallergens, Westernized diet, poor water quality, and high particulate air pollution (farah2025thedynamicevolution pages 2-4, farah2025thedynamicevolution pages 4-5).
- **Epithelial barrier dysfunction:** Loss of structural proteins (E-cadherin, claudins, desmoglein-1, filaggrin) and reduced SPINK7 protease inhibitor levels facilitate allergen penetration (farah2025thedynamicevolution pages 4-5, bertin2026theimmunearchitecture pages 4-6).

### Risk Factors

**Genetic Risk Factors:**
- Polymorphisms at TSLP (5q22) enhancing Th2 polarization (farah2025thedynamicevolution pages 2-4, gautam2026eosinophilicesophagitismechanisms pages 1-2)
- CAPN14 variants (2p23) disrupting epithelial barrier function (khokhar2022eosinophilicesophagitisimmune pages 1-2, gautam2026eosinophilicesophagitismechanisms pages 1-2)
- STAT6 variants (12q13) affecting IL-4/IL-13 signaling (sato2023geneticandmolecular pages 3-4)
- Filaggrin (FLG) loss-of-function variants increasing allergen penetration susceptibility (farah2025thedynamicevolution pages 4-5)
- DSG1 and DSP variants linked to familial EoE through desmosomal disruption (gautam2026eosinophilicesophagitismechanisms pages 1-2)
- Individuals with risk variants at both TSLP and IL4 loci show 3.7-fold increased odds of developing EoE (gautam2026eosinophilicesophagitismechanisms pages 1-2)
- African ancestry-specific loci at 1p22.3, 9p13.3, and 12q24.23 (sato2023geneticandmolecular pages 3-4)
- Male-specific association at SCARB2 (12q24.31) (trimarchi2026multitraitanalysisof pages 10-11)

**Environmental Risk Factors:**
- Westernized diets with processed foods and preservatives (farah2025thedynamicevolution pages 2-4)
- Poor water quality and high particulate air pollution (farah2025thedynamicevolution pages 2-4)
- Gut microbiome disruptions from maternal antibiotic use during pregnancy (farah2025thedynamicevolution pages 2-4)
- Acid suppression in infancy (farah2025thedynamicevolution pages 2-4)
- Seasonal symptom variations related to aeroallergen exposure (farah2025thedynamicevolution pages 4-5)
- Male sex (3:1 male-to-female ratio) (farah2025thedynamicevolution pages 2-4, bertin2026theimmunearchitecture pages 2-4)
- White/Caucasian ethnicity (bertin2026theimmunearchitecture pages 2-4)
- History of atopic diseases (asthma, allergic rhinitis, eczema, food allergies) (farah2025thedynamicevolution pages 2-4)

### Gene-Environment Interactions
The disease is multifactorial with only 2.4% concordance in non-twin siblings, despite familial clustering, suggesting substantial environmental influences on disease expression (low2024reviewarticleemerging pages 4-6). The rising incidence is outpacing endoscopy and biopsy rates, suggesting environmental factors are major contributors to EoE pathogenesis beyond diagnostic awareness alone (low2024reviewarticleemerging pages 4-6). EoE associates with both Mendelian genetic conditions (PHTS, hyper-IgE syndromes, SAM syndrome) and connective tissue disorders with increased TGF-β signaling (sato2023geneticandmolecular pages 3-4).

---

## 3. Phenotypes

### Clinical Symptoms

**Adults and Adolescents:**
- **Dysphagia** (especially to solids): Cardinal symptom; HP:0002015 (farah2025thedynamicevolution pages 2-4, bertin2026theimmunearchitecture pages 2-4)
- **Food impaction** (food bolus requiring emergency endoscopy in 33–54% of adult patients): HP:0030217 (bertin2026theimmunearchitecture pages 2-4)
- **Heartburn/chest pain:** HP:0040279 (savarino2024eosinophilicesophagitisin pages 3-6)
- **Nausea:** HP:0002018 (savarino2024eosinophilicesophagitisin pages 3-6)

**Children:**
- **Feeding difficulties/food avoidance:** HP:0011968 (pasta2025endoscopicmanagementof pages 2-4, pasta2025endoscopicmanagementof pages 1-2)
- **Vomiting:** HP:0002013 (pasta2025endoscopicmanagementof pages 2-4, bertin2026theimmunearchitecture pages 2-4)
- **Regurgitation:** HP:0002020 (bertin2026theimmunearchitecture pages 2-4)
- **Failure to thrive:** HP:0001508 (savarino2024eosinophilicesophagitisin pages 3-6, pasta2025endoscopicmanagementof pages 1-2)
- **Abdominal pain:** HP:0002027 (savarino2024eosinophilicesophagitisin pages 3-6)

### Histological Features
- **Eosinophilic esophageal infiltration** (≥15 eos/HPF diagnostic threshold): HP:0410018 (farah2025thedynamicevolution pages 2-4)
- **Basal zone hyperplasia:** HP:0011024 (khokhar2022eosinophilicesophagitisimmune pages 1-2, musburger2025currentandemerging pages 3-4)
- **Dilated intercellular spaces (DIS):** (khokhar2022eosinophilicesophagitisimmune pages 1-2, khokhar2022eosinophilicesophagitisimmune pages 3-5)
- **Lamina propria fibrosis:** HP:0025578 (farah2025thedynamicevolution pages 5-7)
- **Eosinophilic microabscesses:** (musburger2025currentandemerging pages 3-4)

### Endoscopic Features (EREFS Score)
- **Linear furrows** (48%): Most predictive of active inflammation (farah2025thedynamicevolution pages 5-7, musburger2025currentandemerging pages 3-4)
- **White exudates/plaques** (indicating eosinophil clusters): (pasta2025endoscopicmanagementof pages 2-4, farah2025thedynamicevolution pages 5-7)
- **Concentric rings/trachealization** (44%): Indicates chronic remodeling (farah2025thedynamicevolution pages 5-7, musburger2025currentandemerging pages 3-4)
- **Esophageal strictures** (21–40%): (musburger2025currentandemerging pages 3-4)
- **Mucosal edema** with pallor/loss of vascular markings: (pasta2025endoscopicmanagementof pages 2-4)
- **Normal-appearing esophagus** in 7–32% of patients: (pasta2025endoscopicmanagementof pages 2-4, pasta2025endoscopicmanagementof pages 1-2)
- **Crepe paper effect** (59%): (musburger2025currentandemerging pages 3-4)

### Symptom Characteristics
- **Age of onset:** Variable—can present in infancy through adulthood; diagnosis peaks in early adulthood (bertin2026theimmunearchitecture pages 2-4)
- **Symptom progression:** Progressive; untreated disease carries ~9% annual increase in stricture risk (pasta2025endoscopicmanagementof pages 2-4, pasta2025endoscopicmanagementof pages 1-2)
- **Severity:** Variable from mild dysphagia to severe fibrostenotic disease requiring emergency intervention (pasta2025endoscopicmanagementof pages 2-4)

### Quality of Life Impact
EoE significantly impacts quality of life, with the greatest negative effects on dysphagia-related anxiety, social activities involving food, and maintaining friendships (savarino2024eosinophilicesophagitisin pages 3-6). Diagnostic delays averaging 3 years are common, attributed to delayed referral, postponed endoscopy, and inadequate biopsy evaluation (savarino2024eosinophilicesophagitisin pages 3-6).

---

## 4. Genetic/Molecular Information

### GWAS Susceptibility Loci

The following table summarizes the major genetic susceptibility loci identified for EoE through genome-wide association studies:

| Chromosomal Locus | Gene(s) | Function/Role | Evidence Source |
|---|---|---|---|
| 5q22 | **TSLP**, **WDR36** | **TSLP** encodes thymic stromal lymphopoietin, an epithelial alarmin that promotes allergic/Th2 polarization, activates dendritic cells and ILC2s, and is strongly implicated in EoE initiation; **WDR36** is co-localized at the susceptibility locus and repeatedly recovered in GWAS/OpenTargets associations. This is one of the most reproducible EoE loci. | Established locus in GWAS and reviews (khokhar2022eosinophilicesophagitisimmune pages 1-2, low2024reviewarticleemerging pages 4-6, sato2023geneticandmolecular pages 3-4, gautam2026eosinophilicesophagitismechanisms pages 1-2, OpenTargets Search: eosinophilic esophagitis) |
| 2p23 | **CAPN14** | Encodes calpain-14, an esophagus-enriched protease induced by IL-13; contributes to epithelial barrier dysfunction, desmosomal destabilization, and EoE-specific epithelial remodeling. One of the most disease-specific EoE loci. | Established locus in GWAS and mechanistic studies (khokhar2022eosinophilicesophagitisimmune pages 1-2, low2024reviewarticleemerging pages 4-6, sato2023geneticandmolecular pages 3-4, gautam2026eosinophilicesophagitismechanisms pages 1-2, OpenTargets Search: eosinophilic esophagitis) |
| 11q13 | **LRRC32**, **C11orf30/EMSY** | Associated with epithelial and immune regulation; repeatedly identified across EoE genetic studies and also linked to broader atopic susceptibility. Often cited as a reproducible shared atopy/EoE locus. | Established locus in GWAS/meta-analysis (khokhar2022eosinophilicesophagitisimmune pages 1-2, low2024reviewarticleemerging pages 4-6, gautam2026eosinophilicesophagitismechanisms pages 1-2) |
| 12q13 | **STAT6** | Central transcription factor downstream of IL-4/IL-13 signaling; regulates Th2 effector programs and eosinophilic inflammation. Variants may also influence treatment-related phenotypes such as PPI response. | Established locus and functional relevance in EoE (khokhar2022eosinophilicesophagitisimmune pages 1-2, sato2023geneticandmolecular pages 3-4) |
| 16p13 | **CLEC16A**, **DEXI** | Reproducible susceptibility region identified in more recent genetic studies/meta-analyses; likely contributes to immune regulation and shared atopic disease architecture rather than being EoE-exclusive. | Reproducible susceptibility locus in recent reviews/meta-analysis (low2024reviewarticleemerging pages 4-6, trimarchi2026multitraitanalysisof pages 14-15) |
| 15q23 | **SMAD3** | Encodes a key mediator of TGF-β signaling, linking genetic susceptibility to remodeling/fibrostenotic biology and tissue fibrosis in EoE. | Additional genome-wide significant locus from newer GWAS/meta-analysis (low2024reviewarticleemerging pages 4-6, sato2023geneticandmolecular pages 3-4) |
| Additional validated/implicated loci | **DSG1**, **DSP**, **FLG** and other barrier genes | Not always the lead GWAS locus in summary tables, but repeatedly implicated as susceptibility or familial-risk genes affecting epithelial integrity, allergen penetration, and barrier failure. | Barrier-gene evidence from human genetics and mechanistic reviews (gautam2026eosinophilicesophagitismechanisms pages 1-2, farah2025thedynamicevolution pages 4-5) |
| Recent GWAS expansion | 8 risk loci with 11 independent variants in EoE GWAS | Newer analyses expanded the map beyond the classic loci, identifying additional signals including loci near **GATA3** and **IL4R**, reinforcing overlap with type 2 immunity and atopic disease genetics. | Expanded GWAS findings (trimarchi2026multitraitanalysisof pages 14-15, trimarchi2026multitraitanalysisof pages 10-11) |
| Recent MTAG expansion | 24 loci; ~90 candidate genes | Multi-trait analysis with related atopic diseases substantially expanded susceptibility architecture to **24 loci** with **90 candidate genes**, showing shared genetic basis with asthma, allergic rhinitis, and atopic dermatitis, and supporting polygenic risk modeling. | MTAG expansion/preprint summary (trimarchi2026multitraitanalysisof pages 14-15, trimarchi2026multitraitanalysisof pages 10-11) |


*Table: This table summarizes the main established and newly expanded genetic susceptibility loci for eosinophilic esophagitis, emphasizing how classic barrier and type 2 immunity genes have been extended by recent GWAS/MTAG analyses to a broader polygenic architecture.*

### Key Molecular Targets (OpenTargets)
OpenTargets (MONDO_0005361) identifies the following validated disease-target associations for EoE (OpenTargets Search: eosinophilic esophagitis):
- **TSLP** (thymic stromal lymphopoietin; ENSG00000145777): Association score 0.44
- **WDR36** (WD repeat domain 36; ENSG00000134987): Association score 0.41
- **NR3C1** (glucocorticoid receptor; ENSG00000113580): Association score 0.41
- **IL13** (interleukin 13; ENSG00000169194): Association score 0.39
- **CAPN14** (calpain 14; ENSG00000214711): Association score 0.38
- **IL4R** (interleukin 4 receptor; ENSG00000077238): Association score 0.37
- **IL5** (interleukin 5; ENSG00000113525): Association score 0.33

### EoE Transcriptome and Molecular Profiling
The EoE transcriptome, established through gene expression profiling of esophageal biopsies, reveals characteristic dysregulation of epithelial differentiation genes (DSG1, FLG, CAPN14), type 2 effector molecules (CCL26/eotaxin-3, POSTN, SPINK7), and remodeling mediators (TGFB1, COL1A1) (dsilva2026insightsintothe pages 1-2). Expression profiling has identified an EoE Diagnostic Panel that enables molecular-level diagnosis and monitoring (dsilva2026insightsintothe pages 1-2).

**Single-Cell RNA Sequencing Findings:**
Single-cell RNA sequencing of ~14,000 esophageal cells has identified 8 distinct cell clusters and revealed increased clonality of pathogenic GPR15+ Th2 cells enriched in dairy-triggered EoE (uchida2022modelsandtools pages 2-3). Single-cell analyses have uncovered remarkable cellular heterogeneity including distinct cellular subsets, epithelial cell states associated with barrier dysfunction and proliferation, activated fibroblasts, and spatial organization of inflammatory microenvironments (dsilva2026insightsintothe pages 1-2).

**Epigenetic Changes:**
Epigenetic studies have uncovered changes in DNA methylation and chromatin structure affecting gene expression in EoE pathology, including aberrant CDX2 expression linked to methyl-CpG binding proteins, suggesting epigenetic contributions to esophageal epithelial remodeling and metaplasia-like processes. Suppressed zinc-related pathways (MT1X, MT1F, MT2A) indicate barrier dysfunction through zinc transporter dysregulation.

### Genetic Inheritance
EoE exhibits complex, polygenic inheritance with increased familial clustering. Only 2.4% concordance in non-twin siblings suggests that while genetic susceptibility is important, environmental factors substantially modulate disease expression (low2024reviewarticleemerging pages 4-6). GWAS identified 31 genetic risk loci, with most variants being non-coding (36.7% intergenic, 42.4% intronic), suggesting involvement of regulatory elements (khokhar2022eosinophilicesophagitisimmune pages 1-2). Sex-specific genetic variants have been identified, and recent MTAG analyses demonstrate a polygenic risk score with OR of 11.57 in the top versus bottom decile (trimarchi2026multitraitanalysisof pages 10-11).

---

## 5. Environmental Information

### Environmental Factors
- Westernized diets with processed foods and preservatives (farah2025thedynamicevolution pages 2-4)
- Poor water quality and high particulate air pollution (farah2025thedynamicevolution pages 2-4)
- Early-life acid suppression therapy (farah2025thedynamicevolution pages 2-4)
- Maternal antibiotic use during pregnancy disrupting gut microbiome (farah2025thedynamicevolution pages 2-4)
- Seasonal aeroallergen exposure influencing symptom flares (farah2025thedynamicevolution pages 4-5)

### Lifestyle Factors
- Dietary allergen exposure, particularly milk, wheat, eggs, soy, tree nuts, and seafood (farah2025thedynamicevolution pages 4-5, musburger2025currentandemerging pages 3-4)
- Western dietary patterns associated with increased disease prevalence (farah2025thedynamicevolution pages 2-4)

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

**Type 2 Inflammatory Cascade:**
The central pathogenic mechanism involves a type 2 (Th2)-driven immune response. Upon allergen exposure, esophageal epithelial cells release alarmins—TSLP, IL-33, and IL-25—which activate dendritic cells and group 2 innate lymphoid cells (ILC2s) (farah2025thedynamicevolution pages 4-5, bertin2026theimmunearchitecture pages 4-6). This triggers production of IL-4, IL-5, and IL-13, the key effector cytokines:
- **IL-13** plays the central pathobiological role, driving eotaxin-3 (CCL26) expression, impairing epithelial barrier function by suppressing barrier proteins (filaggrin, claudins, DSG1), and upregulating CAPN14, which destabilizes desmosomal junctions (bertin2026theimmunearchitecture pages 7-9, farah2025thedynamicevolution pages 4-5).
- **IL-5** promotes eosinophil proliferation, survival, maturation, bone marrow release, and trafficking to the esophagus (farah2025thedynamicevolution pages 4-5, ariasgonzalez2024fibrousremodelingin pages 1-2).
- **IL-4** promotes Th2 differentiation, inhibits apoptosis, and drives B cell class switching to IgE and IgG4 (ariasgonzalez2024fibrousremodelingin pages 1-2, imam2026theroleof pages 5-5).

GO terms: GO:0006955 (immune response), GO:0045087 (innate immune response), GO:0002286 (T-helper 2 type immune response), GO:0006954 (inflammatory response).

**Epithelial Barrier Dysfunction:**
Barrier dysfunction is central to EoE pathogenesis. Loss of structural proteins (E-cadherin, claudins, desmoglein-1, SPINK7) weakens tight junctions and facilitates allergen penetration (farah2025thedynamicevolution pages 4-5, bertin2026theimmunearchitecture pages 4-6). IL-13-driven upregulation of calpain-14 destabilizes desmosomal junctions, while SPINK7 loss amplifies protease activity and TSLP production, creating barrier-to-alarmin feedback loops (bertin2026theimmunearchitecture pages 4-6).

GO terms: GO:0045104 (intermediate filament cytoskeleton organization), GO:0016337 (single organismal cell-cell adhesion).

**ILC2-Areg-EGFR Signaling:**
ILC2s serve as a critical bridge between epithelial alarmin signals and adaptive Th2 responses, producing amphiregulin (Areg) that binds EGFR on basal cells, triggering ERK1/2 and AKT signaling and causing pathological epithelial hyperproliferation and thickening (bertin2026theimmunearchitecture pages 7-9).

### Tissue Remodeling and Fibrosis
Chronic inflammation causes progressive tissue remodeling including fibrosis, angiogenesis, and smooth muscle hypertrophy. TGF-β1 upregulation mediates fibroblast activation and extracellular matrix deposition, causing esophageal stiffening and stricture formation. Periostin (POSTN), upregulated by IL-13, enhances fibrosis and eosinophil recruitment (farah2025thedynamicevolution pages 4-5, ariasgonzalez2024fibrousremodelingin pages 1-2). Epithelial-mesenchymal transition (EMT) and collagen deposition contribute to esophageal strictures proportional to a patient's age and untreated disease duration (ariasgonzalez2024fibrousremodelingin pages 1-2).

GO terms: GO:0030198 (extracellular matrix organization), GO:0001525 (angiogenesis).

### Eosinophil Effector Functions
Eosinophil degranulation releases major basic protein (MBP), eosinophil cationic protein (ECP), eosinophil peroxidase (EPO), and eosinophil-derived neurotoxin (EDN), causing epithelial damage and oxidative stress (bertin2026theimmunearchitecture pages 7-9). Eosinophils also produce TGF-β and ATRA, promoting Treg differentiation as a regulatory counter-circuit (bertin2026theimmunearchitecture pages 7-9).

### Cell Types Involved
- Eosinophils: CL:0000771
- Th2 cells: CL:0000546
- ILC2s (group 2 innate lymphoid cells): CL:0001069
- Mast cells: CL:0000097
- Basophils: CL:0000767
- Dendritic cells: CL:0000451
- Esophageal epithelial cells: CL:0002252
- Fibroblasts: CL:0000057
- B cells/plasma cells: CL:0000236/CL:0000786

---

## 7. Anatomical Structures Affected

### Primary Organ
- **Esophagus** (UBERON:0001043): The primary and often sole organ affected, with inflammation spanning the esophageal squamous epithelium and potentially deeper layers (farah2025thedynamicevolution pages 2-4, ariasgonzalez2024fibrousremodelingin pages 1-2).

### Tissue and Cellular Level
- **Esophageal squamous epithelium** (UBERON:0006920): Eosinophilic infiltration, basal zone hyperplasia, dilated intercellular spaces (khokhar2022eosinophilicesophagitisimmune pages 1-2, khokhar2022eosinophilicesophagitisimmune pages 3-5)
- **Lamina propria** (UBERON:0000030): Fibrosis and inflammatory cell infiltration (farah2025thedynamicevolution pages 5-7)
- **Subepithelial connective tissue:** Collagen deposition and fibrosis (ariasgonzalez2024fibrousremodelingin pages 1-2)
- **Smooth muscle layers:** Hypertrophy in chronic disease (farah2025thedynamicevolution pages 4-5)

### Localization
- Disease affects the entire esophagus but biopsies should be obtained from both proximal and distal regions to account for patchy distribution of inflammation (farah2025thedynamicevolution pages 2-4).

---

## 8. Temporal Development

### Onset
- **Typical age of onset:** Can occur at any age from infancy to late adulthood; incidence rises during adolescence and peaks in early adulthood (bertin2026theimmunearchitecture pages 2-4)
- **Onset pattern:** Chronic and insidious, often with diagnostic delays averaging 3 years (savarino2024eosinophilicesophagitisin pages 3-6)

### Progression
- **Disease course:** Chronic, progressive if untreated, with a ~9% annual increase in esophageal stricture risk (pasta2025endoscopicmanagementof pages 2-4, pasta2025endoscopicmanagementof pages 1-2)
- **Stages:** Inflammatory (early) → fibrostenotic (advanced), with adults displaying more subepithelial fibrosis and esophageal narrowing than children (musburger2025currentandemerging pages 3-4)
- **Duration:** Chronic lifelong disease requiring maintenance therapy (farah2025thedynamicevolution pages 10-12)
- **Remission patterns:** Treatment-induced remission is achievable but disease recurs upon treatment cessation in most patients (farah2025thedynamicevolution pages 10-12)

---

## 9. Inheritance and Population

### Epidemiology
- **Global incidence:** 5.3 per 100,000 person-years (farah2025thedynamicevolution pages 2-4, bertin2026theimmunearchitecture pages 2-4, low2024reviewarticleemerging pages 1-3)
- **Global prevalence:** 40.0 per 100,000 persons, representing an 800% increase from 1976–2001 to 2017–2022 (bertin2026theimmunearchitecture pages 2-4)
- **Prevalence in Western countries:** Exceeds 1 in 1,000 individuals (bertin2026theimmunearchitecture pages 2-4)
- **European incidence:** 3.64 per 100,000 person-years (nationwide) to 7.16 (regional/center-based studies), with significant increases over the last 30 years
- **Danish incidence:** Increased from 3.9 to 11.7 per 100,000 person-years between 2011 and 2018
- **US prevalence estimates:** Range from 1 per 1,000 to >150 per 100,000 (pasta2025endoscopicmanagementof pages 1-2)
- **Italy prevalence:** Estimated at 41 per 100,000 (savarino2024eosinophilicesophagitisin pages 3-6)

### Population Demographics
- **Sex ratio:** Approximately 3:1 male-to-female predominance (farah2025thedynamicevolution pages 2-4, bertin2026theimmunearchitecture pages 2-4); male prevalence 53.8 per 100,000 versus female 20.1 per 100,000 (savarino2024eosinophilicesophagitisin pages 3-6)
- **Ethnicity:** Predominantly affects white/Caucasian individuals; African ancestry-specific risk loci identified (sato2023geneticandmolecular pages 3-4, bertin2026theimmunearchitecture pages 2-4)
- **Age distribution:** Higher incidence in adults than children; children have approximately one-quarter the incidence of adults aged 40–64 years (bertin2026theimmunearchitecture pages 2-4)
- **Comorbidities:** Most frequently associated with rhinitis, asthma, food allergy, and gastroesophageal reflux disease (farah2025thedynamicevolution pages 2-4)

### Genetic Inheritance
- **Pattern:** Complex polygenic/multifactorial (khokhar2022eosinophilicesophagitisimmune pages 1-2, sato2023geneticandmolecular pages 3-4)
- **Concordance:** Only 2.4% in non-twin siblings (low2024reviewarticleemerging pages 4-6)
- **Familial clustering:** Present, with increased risk in second-degree relatives (khokhar2022eosinophilicesophagitisimmune pages 1-2)
- **Mendelian associations:** PHTS, hyper-IgE syndromes, SAM syndrome (sato2023geneticandmolecular pages 3-4)

---

## 10. Diagnostics

### Clinical Diagnostic Criteria
Diagnosis requires: (1) symptoms of esophageal dysfunction, (2) eosinophil-predominant inflammation with ≥15 eosinophils per high-power field on esophageal biopsy, and (3) exclusion of other causes of esophageal eosinophilia (farah2025thedynamicevolution pages 2-4, musburger2025currentandemerging pages 3-4). At least six biopsies from multiple esophageal sites are recommended to account for patchy inflammation (farah2025thedynamicevolution pages 2-4).

### Endoscopic Assessment
The EoE Endoscopic Reference Score (EREFS) standardizes endoscopic evaluation across five domains: Edema, Rings, Exudates, Furrows, and Strictures (farah2025thedynamicevolution pages 5-7). Functional lumen imaging probe (FLIP) panometry and high-resolution manometry (HRM) provide additional assessment of fibrostenotic features.

### Histological Assessment
The EoE Histological Scoring System evaluates inflammatory activity including eosinophilic infiltration density, basal zone hyperplasia, dilated intercellular spaces, eosinophilic microabscesses, papillary elongation, and lamina propria fibrosis (farah2025thedynamicevolution pages 5-7, musburger2025currentandemerging pages 3-4).

### Biomarkers
- **Peak eosinophil count (PEC):** Gold standard histologic measure (farah2025thedynamicevolution pages 2-4)
- **Serum biomarkers:** No single serum biomarker has sufficient sensitivity; 49 serum proteins tested without reliable diagnostic capacity (savarino2024eosinophilicesophagitisin pages 3-6)
- **TSLP and periostin:** Show promise as potential biomarkers but require further validation (farah2025thedynamicevolution pages 5-7)
- **Extracellular matrix proteins (CTX-III, PRO-C3, PRO-C6):** Potential surrogate biomarkers for fibrosis assessment
- **TSLP-responsive memory CD4+ T cells:** TSLP-induced STAT5 phosphorylation in circulating CD4+ T cells correlates with esophageal eosinophil counts, providing a basis for a blood-based diagnostic test
- **Eosinophil-derived mediators (ECP, EDN, EPO, MBP):** Investigated as non-invasive biomarkers

### Emerging Diagnostic Tools
- Esophageal string test and Cytosponge for non-invasive monitoring
- Transnasal endoscopy for non-sedated assessment
- EndoFlip for assessing esophageal distensibility

### Differential Diagnosis
Conditions to exclude: GERD, proton pump inhibitor-responsive esophageal eosinophilia (now integrated into EoE), eosinophilic gastroenteritis, Crohn's disease involving the esophagus, pill esophagitis, infection, hypereosinophilic syndrome, and achalasia.

---

## 11. Outcome/Prognosis

### Disease Course
EoE is a chronic, progressive disease that, if left untreated, leads to esophageal remodeling with fibrosis and stricture formation. The risk of strictures increases by approximately 9% annually without treatment (pasta2025endoscopicmanagementof pages 2-4, pasta2025endoscopicmanagementof pages 1-2). Esophageal stricture formation is proportional to a patient's age and untreated disease duration (ariasgonzalez2024fibrousremodelingin pages 1-2).

### Morbidity
- Food bolus impaction precipitates emergency endoscopy in 33–54% of adult patients (bertin2026theimmunearchitecture pages 2-4)
- 25% of patients have a history of esophageal dilations; 30% report EoE-related emergency room visits in the preceding year (savarino2024eosinophilicesophagitisin pages 3-6)
- Approximately 58% of patients undergoing dilation require repeated procedures within the first year (farah2025thedynamicevolution pages 12-13)

### Mortality
EoE is not typically associated with significant mortality. Epidemiological evidence suggests that EoE patients do not develop esophageal malignancy, and EoE-associated epithelial remodeling may actually limit esophageal carcinogenesis.

### Quality of Life
Quality of life impacts include dysphagia-related anxiety, impaired social activities involving food, and difficulty maintaining friendships (EoE Impact Questionnaire scores 1.6–2.2 on 1–5 scale) (savarino2024eosinophilicesophagitisin pages 3-6). Heartburn was the most commonly reported symptom (69%) among surveyed patients.

---

## 12. Treatment

The following table provides a comprehensive summary of current and emerging treatment options for EoE:

| Treatment Category | Specific Agent/Approach | Mechanism of Action | Histologic Remission Rate (%) | Regulatory Status | Key Notes |
|---|---|---|---|---|---|
| Acid suppression / anti-inflammatory therapy (MAXO: proton pump inhibitor administration) | Proton pump inhibitors (PPIs; e.g., omeprazole, esomeprazole) | Reduce acid exposure and also exert anti-inflammatory effects, including suppression of Th2-associated inflammatory signaling beyond acid suppression | 41.7% in meta-analytic data; ~45–50.5% in recent reviews/real-world summaries | Used off-label but guideline-recommended first-line therapy for EoE | Clinical response reported around 60.8–71%; long-term histologic response ~60% in some cohorts; often first pharmacologic option (bertin2026theimmunearchitecture pages 10-12, farah2025thedynamicevolution pages 10-12, musburger2025currentandemerging pages 6-7, low2024reviewarticleemerging pages 9-11) |
| Topical corticosteroid (MAXO: topical corticosteroid therapy) | Budesonide oral suspension (BOS; Eohilia) | Local glucocorticoid anti-inflammatory effect in esophageal mucosa via NR3C1 signaling | 53.1% | FDA-approved in the US for induction treatment in adolescents/adults; formulation-specific approval noted in recent reviews | Maintenance remission reported up to 83.3% at lower doses; adverse effects include esophageal candidiasis (farah2025thedynamicevolution pages 10-12, musburger2025currentandemerging pages 6-7) |
| Topical corticosteroid (MAXO: topical corticosteroid therapy) | Budesonide orodispersible tablet (BOT; Jorveza) | Local glucocorticoid anti-inflammatory effect optimized for esophageal contact time | Up to 93% | Approved in Europe/Canada/Australia for adults in recent reviews | Sustained remission ~75% at 48 weeks; among the highest efficacy topical options reported (bertin2026theimmunearchitecture pages 10-12, bertin2026theimmunearchitecture pages 12-14) |
| Topical corticosteroid (MAXO: topical corticosteroid therapy) | Fluticasone swallowed from inhaler / esophagus-targeted preparation | Local glucocorticoid anti-inflammatory effect in esophageal epithelium | 64–71% | Commonly used off-label; guideline-recommended topical steroid option | Histologic remission superior to placebo; candidiasis reported in ~5–30% with topical steroids overall (musburger2025currentandemerging pages 6-7, low2024reviewarticleemerging pages 9-11) |
| Biologic therapy (MAXO: monoclonal antibody therapy) | Dupilumab (anti-IL-4Rα) | Blocks IL-4/IL-13 signaling through IL4Rα, targeting core type 2 inflammatory pathway | 59–60% at 24 weeks; 100% in long-term open-label extension reported in review summary | FDA-approved for EoE since 2022; label expanded in 2024 to younger children; also approved in Europe/Canada per reviews | First disease-specific biologic for EoE; particularly useful in refractory disease and patients with atopic comorbidities; marked eosinophil reduction (~96%) reported (bertin2026theimmunearchitecture pages 10-12, bertin2026theimmunearchitecture pages 12-14, farah2025thedynamicevolution pages 12-13, musburger2025currentandemerging pages 3-4) |
| Dietary therapy (MAXO: dietary modification) | Single-food elimination diet (often milk-first approach) | Removes food antigen triggers driving esophageal type 2 inflammation | 44–54% | Guideline-recommended first-line non-pharmacologic therapy | Less restrictive than broader elimination diets; requires serial endoscopy/biopsy to confirm remission and identify triggers (bertin2026theimmunearchitecture pages 10-12, bertin2026theimmunearchitecture pages 12-14, musburger2025currentandemerging pages 3-4) |
| Dietary therapy (MAXO: elimination diet) | Empiric multi-food elimination diet (e.g., 2-food, 4-food, 6-food elimination) | Sequential removal of common food allergens | Variable within broader dietary range; higher than 1-food approaches but below elemental diet in most summaries | Guideline-recommended first-line option | Common targets include dairy, wheat, egg, soy/legumes, nuts, fish/shellfish; adherence burden is substantial (bertin2026theimmunearchitecture pages 12-14, musburger2025currentandemerging pages 3-4) |
| Dietary therapy (MAXO: elemental diet) | Elemental amino-acid formula diet | Complete removal of intact food antigens | 90–94% | Effective but limited by palatability, cost, and practicality | Highest remission rates among dietary therapies; often reserved for selected or refractory cases (bertin2026theimmunearchitecture pages 10-12, bertin2026theimmunearchitecture pages 12-14) |
| Endoscopic/mechanical therapy (MAXO: esophageal dilation) | Esophageal dilation for fibrostenotic disease | Mechanically disrupts strictures and increases luminal diameter; does not treat inflammation | Histologic remission: not applicable | Standard adjunctive interventional approach | Symptomatic relief ~85–95%; often targets 15–18 mm luminal diameter; repeat dilations common; perforation risk ~0.38%; should be combined with anti-inflammatory treatment (bertin2026theimmunearchitecture pages 12-14, farah2025thedynamicevolution pages 12-13) |
| Emerging biologic (MAXO: monoclonal antibody therapy) | Cendakimab (anti-IL-13) | Selectively blocks IL-13, aiming to reduce epithelial dysfunction, eotaxin-3 induction, and remodeling | 28.6% vs 2.2% placebo in review summary | Investigational / not broadly approved for EoE | Mechanistically attractive because IL-13 is central to EoE biology; under active clinical development (bertin2026theimmunearchitecture pages 12-14) |
| Emerging biologic (MAXO: monoclonal antibody therapy) | Tezepelumab (anti-TSLP) | Blocks epithelial alarmin TSLP upstream of Th2 polarization and eosinophilic inflammation | Not established in the cited summaries | Investigational | Rationale is strong given TSLP genetic and mechanistic evidence in EoE, but robust remission data were not provided in the retrieved summaries (bertin2026theimmunearchitecture pages 4-6, musburger2025currentandemerging pages 3-4) |
| Emerging biologic (MAXO: monoclonal antibody therapy) | Benralizumab (anti-IL-5Rα) | Depletes eosinophils by targeting IL-5 receptor alpha | Not recommended / no consistent efficacy for routine EoE treatment in recent reviews | Investigational; not approved for EoE | Despite a compelling eosinophil-depleting mechanism, recent reviews summarize insufficient clinical benefit for routine use in EoE (bertin2026theimmunearchitecture pages 12-14, musburger2025currentandemerging pages 3-4) |


*Table: This table summarizes current and emerging treatment options for eosinophilic esophagitis, including mechanisms, remission rates, regulatory status, and practical notes. It is useful for comparing first-line therapies, procedural management, and biologic pipeline agents in one place.*

### Treatment Strategy
The ACG 2025 Clinical Guideline and AGA/JTF guidelines recommend proton pump inhibitors, topical steroids, empiric diet elimination, dupilumab, and esophageal dilation as treatment options (bertin2026theimmunearchitecture pages 10-12, farah2025thedynamicevolution pages 10-12, low2024reviewarticleemerging pages 9-11). Treatment selection should be individualized based on disease phenotype, severity, and patient preference (bertin2026theimmunearchitecture pages 10-12).

**First-line options:** PPIs or swallowed topical corticosteroids, with corticosteroids highlighted as most potent for severe cases (farah2025thedynamicevolution pages 10-12). Dietary elimination is also recommended as a first-line non-pharmacologic option (musburger2025currentandemerging pages 3-4).

**Second-line/refractory disease:** Dupilumab is recommended for patients failing first-line treatment, particularly those with atopic comorbidities. It is approved for patients aged ≥1 year (FDA expanded 2024) or ≥12 years (EMA) (farah2025thedynamicevolution pages 12-13, musburger2025currentandemerging pages 3-4).

**Maintenance therapy:** Recommended for all treatment approaches given disease recurrence upon cessation (farah2025thedynamicevolution pages 10-12, low2024reviewarticleemerging pages 9-11).

### Current Clinical Trials
Active recruiting Phase 3 trials include:
- **NCT06596252:** Once daily vs. twice daily budesonide orodispersible tablets for EoE remission induction (Dr. Falk Pharma; n=308)
- **NCT07112378:** Dupilumab in small children (1–11 years) with EoE (Regeneron; n=20)

Active Phase 2 trials include:
- **NCT06705387:** Dupilumab vs. topical corticosteroid effectiveness comparison in stenotic EoE (n=72)
- **NCT05608681:** EP-104GI (novel formulation) in adults with EoE (Eupraxia Pharmaceuticals; n=117)
- **NCT05485155:** Zemaira (alpha-1 antitrypsin) pilot study in EoE (Cincinnati Children's; n=15)

### Emerging Biologics
- **Cendakimab** (anti-IL-13): Achieved 28.6% histologic remission vs. 2.2% placebo (bertin2026theimmunearchitecture pages 12-14)
- **Tezepelumab** (anti-TSLP): Investigational, targeting upstream alarmin pathway
- **Dectrekumab** (anti-IL-13): Under investigation
- Other agents investigated but showing insufficient efficacy include anti-IL-5 agents (mepolizumab, reslizumab, benralizumab), anti-IgE (omalizumab), and anti-Siglec-8 (lirentelimab) (bertin2026theimmunearchitecture pages 12-14)

MAXO terms: MAXO:0000874 (proton pump inhibitor administration), MAXO:0000753 (dietary modification), MAXO:0001298 (monoclonal antibody therapy), MAXO:0000004 (surgical procedure).

---

## 13. Prevention

### Primary Prevention
No established primary prevention strategies exist, but modifiable risk factors include:
- Avoiding unnecessary early-life acid suppression therapy (farah2025thedynamicevolution pages 2-4)
- Judicious antibiotic use during pregnancy (farah2025thedynamicevolution pages 2-4)
- Attention to environmental pollutant exposure (farah2025thedynamicevolution pages 2-4)

### Secondary Prevention
- Early diagnosis and treatment to prevent fibrostenotic progression
- Monitoring of patients with atopic comorbidities who are at increased risk
- At least six biopsies from multiple esophageal sites for diagnostic accuracy (farah2025thedynamicevolution pages 2-4)

### Tertiary Prevention
- Maintenance therapy to prevent disease relapse and progressive fibrostenosis
- Monitoring with clinical, endoscopic, and histologic assessments (bertin2026theimmunearchitecture pages 10-12)
- Esophageal dilation for fibrostenotic complications combined with anti-inflammatory therapy (farah2025thedynamicevolution pages 12-13)

---

## 14. Other Species / Natural Disease

### Comparative Biology
No naturally occurring EoE analogue has been documented in veterinary medicine. However, eosinophilic esophagitis-like conditions can be experimentally induced in multiple species for research purposes. A novel swine biomedical research model for EoE has been developed using intraperitoneal sensitization and oral challenge with hen egg white protein, producing esophageal eosinophilia (>15 eosinophils/0.24 mm²), systemic Th2/IgE responses, local eotaxin-1 expression, and endoscopic findings including linear furrows and white exudates consistent with human EoE hallmarks.

---

## 15. Model Organisms

### Mouse Models
Multiple murine models have been developed spanning five major categories (dsilva2026insightsintothe pages 2-4):

1. **Allergen-driven models:** Aspergillus fumigatus intranasal exposure (first established model, 2001); OVA-alum sensitization with intragastric challenge; house dust mite exposure (jackson2025mousemodelsof pages 9-11, uchida2022modelsandtools pages 1-2)

2. **Chemical/hapten models:** Oxazolone (OXA) producing robust EoE phenotypes with esophageal eosinophilia, epithelial thickening, and collagen deposition, showing ~25% overlap with human EoE genetic signatures (jackson2025mousemodelsof pages 9-11)

3. **Cytokine overexpression models:** IL-13, IL-33, and IL-18 administration or transgenic overexpression; IL-33 produces EoE-like phenotype in an IL-13-dependent manner (jackson2025mousemodelsof pages 14-16, uchida2022modelsandtools pages 1-2)

4. **Spontaneous genetic models:** Nik⁻/⁻ mice developing severe eosinophilia with basal cell hyperplasia, mucosal thickening, and increased collagen deposition; Tgfbr1M318R/+ variant model recapitulating EoE clinically, immunologically, histologically, and transcriptionally, correlating best with human EoEe2 endotype (jackson2025mousemodelsof pages 14-16, dsilva2026insightsintothe pages 11-13)

5. **Barrier disruption models:** SDS detergent exposure inducing eosinophilia, barrier changes, and increased IL-33 expression (jackson2025mousemodelsof pages 9-11)

### Phenotype Recapitulation
Key features recapitulated across models include: lamina propria eosinophilia, intraepithelial eosinophilia, subepithelial fibrosis, basal cell hyperplasia, epithelial thickening, multi-cellular inflammation, epithelial barrier dysfunction, angiogenesis, neuronal remodeling, and epithelial transcriptomic remodeling (dsilva2026insightsintothe pages 11-13). No single model fully recapitulates all aspects of human disease (dsilva2026insightsintothe pages 2-4).

### Model Limitations
- Most models use inbred strains (C57BL/6, BALB/c) differing in baseline immune polarization (dsilva2026insightsintothe pages 14-16)
- Single-antigen models do not replicate polyvalent sensitization to multiple food antigens seen in human EoE (dsilva2026insightsintothe pages 14-16)
- Mouse and human esophageal anatomy differ significantly (keratinized vs. non-keratinized epithelium)
- Most models lack assessment of disease-relevant functional outcomes such as esophageal motility

### Swine Model
A novel swine model using sensitization with hen egg white protein produces systemic Th2/IgE responses, local eotaxin-1 expression, esophageal eosinophilia (>15 eos/0.24 mm²), and endoscopic findings (linear furrows, white exudates) closely matching human EoE.

---

## Summary

Eosinophilic esophagitis is a chronic, immune-mediated disease of growing global significance, with incidence and prevalence increasing dramatically over the past three decades (bertin2026theimmunearchitecture pages 2-4). The disease results from complex interactions between genetic susceptibility (24+ GWAS loci, 90 candidate genes), environmental triggers, epithelial barrier dysfunction, and type 2 inflammatory responses driven by the IL-4/IL-13/TSLP axis (khokhar2022eosinophilicesophagitisimmune pages 1-2, trimarchi2026multitraitanalysisof pages 10-11, farah2025thedynamicevolution pages 4-5). Diagnosis requires endoscopy with biopsies demonstrating ≥15 eosinophils/HPF, and management involves a growing therapeutic armamentarium including PPIs, topical corticosteroids, dietary elimination, and biologics (bertin2026theimmunearchitecture pages 10-12). The FDA approval of dupilumab in 2022 represented a landmark advance as the first disease-specific biologic, achieving 59–60% histologic remission versus 5–6% with placebo (bertin2026theimmunearchitecture pages 10-12, farah2025thedynamicevolution pages 12-13). Emerging therapies targeting IL-13, TSLP, and other pathways offer promise for more personalized, mechanism-based treatment strategies (bertin2026theimmunearchitecture pages 12-14). Critical unmet needs include development of validated non-invasive biomarkers for diagnosis and monitoring, long-term safety data for biologics, and personalized approaches to address the heterogeneous nature of this disease (savarino2024eosinophilicesophagitisin pages 3-6, gautam2026eosinophilicesophagitismechanisms pages 1-2).

References

1. (farah2025thedynamicevolution pages 2-4): Amir Farah, Tarek Assaf, Jawad Hindy, Wisam Abboud, Mostafa Mahamid, Edoardo Vincenzo Savarino, and Amir Mari. The dynamic evolution of eosinophilic esophagitis. Diagnostics, 15:240, Jan 2025. URL: https://doi.org/10.3390/diagnostics15030240, doi:10.3390/diagnostics15030240. This article has 14 citations.

2. (gautam2026eosinophilicesophagitismechanisms pages 1-2): Ravi Gautam and Melanie A. Ruffner. Eosinophilic esophagitis: mechanisms of disease and approach to treatment. Current Allergy and Asthma Reports, Mar 2026. URL: https://doi.org/10.1007/s11882-026-01253-w, doi:10.1007/s11882-026-01253-w. This article has 2 citations and is from a peer-reviewed journal.

3. (farah2025thedynamicevolution pages 4-5): Amir Farah, Tarek Assaf, Jawad Hindy, Wisam Abboud, Mostafa Mahamid, Edoardo Vincenzo Savarino, and Amir Mari. The dynamic evolution of eosinophilic esophagitis. Diagnostics, 15:240, Jan 2025. URL: https://doi.org/10.3390/diagnostics15030240, doi:10.3390/diagnostics15030240. This article has 14 citations.

4. (khokhar2022eosinophilicesophagitisimmune pages 1-2): Dilawar Khokhar, Sahiti Marella, Gila Idelman, Joy W. Chang, Mirna Chehade, and Simon P. Hogan. Eosinophilic esophagitis: immune mechanisms and therapeutic targets. Jul 2022. URL: https://doi.org/10.1111/cea.14196, doi:10.1111/cea.14196. This article has 56 citations and is from a domain leading peer-reviewed journal.

5. (OpenTargets Search: eosinophilic esophagitis): Open Targets Query (eosinophilic esophagitis, 13 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (low2024reviewarticleemerging pages 4-6): Eric E. Low and Evan S. Dellon. Review article: emerging insights into the epidemiology, pathophysiology, diagnostic and therapeutic aspects of eosinophilic oesophagitis and other eosinophilic gastrointestinal diseases. Alimentary Pharmacology & Therapeutics, 59:322-340, Dec 2024. URL: https://doi.org/10.1111/apt.17845, doi:10.1111/apt.17845. This article has 41 citations and is from a highest quality peer-reviewed journal.

7. (trimarchi2026multitraitanalysisof pages 10-11): Michael P. Trimarchi, Bahram Namjou-Khales, Netali Ben-Baruch Morgenstern, Mark Rochman, Xiaoting Chen, Garrett Osswald, John Besse, Molly Shook, Julie Caldwell, Michael Lape, Tetsuo Shota, Matthew T. Weirauch, Melanie Ruffner, Gregory Constantine, Lisa J. Martin, Leah C. Kottyan, Marc E. Rothenberg, and Consortium of Eosinophilic Gastrointestinal Disease Researchers. Multi-trait analysis of gwas expands eosinophilic esophagitis genetic susceptibility and polygenic risk scores. Research Square, May 2026. URL: https://doi.org/10.21203/rs.3.rs-6630283/v2, doi:10.21203/rs.3.rs-6630283/v2. This article has 2 citations.

8. (bertin2026theimmunearchitecture pages 4-6): Luisa Bertin, Federico Caldart, Alberto Barchi, Niccolò Seregni, Andrea Pasta, Francesco Calabrese, Elisa Marabotto, Amir Mari, Amir Farah, Emma Sirinic, Andrea Sorge, Matteo Ghisa, Javier Chahuán, Vincenzo Savarino, and Edoardo Vincenzo Savarino. The immune architecture of eosinophilic esophagitis: mechanisms, therapeutic targets, and precision management. ImmunoTargets and Therapy, Volume 15:1-27, May 2026. URL: https://doi.org/10.2147/itt.s510865, doi:10.2147/itt.s510865. This article has 0 citations.

9. (sato2023geneticandmolecular pages 3-4): Hiroki Sato, Kasumi Osonoi, Colby S. Sharlin, and Tetsuo Shoda. Genetic and molecular contributors in eosinophilic esophagitis. Current Allergy and Asthma Reports, 23:255-266, Apr 2023. URL: https://doi.org/10.1007/s11882-023-01075-0, doi:10.1007/s11882-023-01075-0. This article has 17 citations and is from a peer-reviewed journal.

10. (bertin2026theimmunearchitecture pages 2-4): Luisa Bertin, Federico Caldart, Alberto Barchi, Niccolò Seregni, Andrea Pasta, Francesco Calabrese, Elisa Marabotto, Amir Mari, Amir Farah, Emma Sirinic, Andrea Sorge, Matteo Ghisa, Javier Chahuán, Vincenzo Savarino, and Edoardo Vincenzo Savarino. The immune architecture of eosinophilic esophagitis: mechanisms, therapeutic targets, and precision management. ImmunoTargets and Therapy, Volume 15:1-27, May 2026. URL: https://doi.org/10.2147/itt.s510865, doi:10.2147/itt.s510865. This article has 0 citations.

11. (savarino2024eosinophilicesophagitisin pages 3-6): Edoardo Vincenzo Savarino, Giovanni Barbara, Maria Beatrice Bilò, Nicola De Bortoli, Antonio Di Sabatino, Salvatore Oliva, Roberto Penagini, Francesca Racca, Annalisa Tortora, Filippo Rumi, and Americo Cicchetti. Eosinophilic esophagitis in adults and adolescents: epidemiology, diagnostic challenges, and management strategies for a type 2 inflammatory disease. Therapeutic Advances in Gastroenterology, Jan 2024. URL: https://doi.org/10.1177/17562848241249570, doi:10.1177/17562848241249570. This article has 29 citations and is from a peer-reviewed journal.

12. (pasta2025endoscopicmanagementof pages 2-4): Andrea Pasta, Francesco Calabrese, Manuele Furnari, Edoardo Vincenzo Savarino, Pierfrancesco Visaggi, Giorgia Bodini, Elena Formisano, Patrizia Zentilin, Edoardo Giovanni Giannini, and Elisa Marabotto. Endoscopic management of eosinophilic esophagitis: a narrative review on diagnosis and treatment. Journal of Clinical Medicine, 14:3756, May 2025. URL: https://doi.org/10.3390/jcm14113756, doi:10.3390/jcm14113756. This article has 13 citations.

13. (pasta2025endoscopicmanagementof pages 1-2): Andrea Pasta, Francesco Calabrese, Manuele Furnari, Edoardo Vincenzo Savarino, Pierfrancesco Visaggi, Giorgia Bodini, Elena Formisano, Patrizia Zentilin, Edoardo Giovanni Giannini, and Elisa Marabotto. Endoscopic management of eosinophilic esophagitis: a narrative review on diagnosis and treatment. Journal of Clinical Medicine, 14:3756, May 2025. URL: https://doi.org/10.3390/jcm14113756, doi:10.3390/jcm14113756. This article has 13 citations.

14. (musburger2025currentandemerging pages 3-4): Brooke G. Musburger, Maria Gonzalez Echeandia, Elias L. Suskind, David L. Suskind, Hengqi Betty Zheng, and Dominique Mark. Current and emerging therapies for eosinophilic esophagitis (eoe): a comprehensive review. Pharmaceutics, 17:753, Jun 2025. URL: https://doi.org/10.3390/pharmaceutics17060753, doi:10.3390/pharmaceutics17060753. This article has 4 citations.

15. (khokhar2022eosinophilicesophagitisimmune pages 3-5): Dilawar Khokhar, Sahiti Marella, Gila Idelman, Joy W. Chang, Mirna Chehade, and Simon P. Hogan. Eosinophilic esophagitis: immune mechanisms and therapeutic targets. Jul 2022. URL: https://doi.org/10.1111/cea.14196, doi:10.1111/cea.14196. This article has 56 citations and is from a domain leading peer-reviewed journal.

16. (farah2025thedynamicevolution pages 5-7): Amir Farah, Tarek Assaf, Jawad Hindy, Wisam Abboud, Mostafa Mahamid, Edoardo Vincenzo Savarino, and Amir Mari. The dynamic evolution of eosinophilic esophagitis. Diagnostics, 15:240, Jan 2025. URL: https://doi.org/10.3390/diagnostics15030240, doi:10.3390/diagnostics15030240. This article has 14 citations.

17. (trimarchi2026multitraitanalysisof pages 14-15): Michael P. Trimarchi, Bahram Namjou-Khales, Netali Ben-Baruch Morgenstern, Mark Rochman, Xiaoting Chen, Garrett Osswald, John Besse, Molly Shook, Julie Caldwell, Michael Lape, Tetsuo Shota, Matthew T. Weirauch, Melanie Ruffner, Gregory Constantine, Lisa J. Martin, Leah C. Kottyan, Marc E. Rothenberg, and Consortium of Eosinophilic Gastrointestinal Disease Researchers. Multi-trait analysis of gwas expands eosinophilic esophagitis genetic susceptibility and polygenic risk scores. Research Square, May 2026. URL: https://doi.org/10.21203/rs.3.rs-6630283/v2, doi:10.21203/rs.3.rs-6630283/v2. This article has 2 citations.

18. (dsilva2026insightsintothe pages 1-2): Anish Dsilva and Ariel Munitz. Insights into the pathogenesis of eosinophilic esophagitis using mouse models. Myeloid Cells, Jan 2026. URL: https://doi.org/10.70401/mc.2026.0003, doi:10.70401/mc.2026.0003. This article has 0 citations.

19. (uchida2022modelsandtools pages 2-3): Amiko M. Uchida, Gabrielle Ro, John J. Garber, Kathryn A. Peterson, and June L. Round. Models and tools for investigating eosinophilic esophagitis at the bench. Frontiers in Immunology, Jul 2022. URL: https://doi.org/10.3389/fimmu.2022.943518, doi:10.3389/fimmu.2022.943518. This article has 6 citations and is from a peer-reviewed journal.

20. (bertin2026theimmunearchitecture pages 7-9): Luisa Bertin, Federico Caldart, Alberto Barchi, Niccolò Seregni, Andrea Pasta, Francesco Calabrese, Elisa Marabotto, Amir Mari, Amir Farah, Emma Sirinic, Andrea Sorge, Matteo Ghisa, Javier Chahuán, Vincenzo Savarino, and Edoardo Vincenzo Savarino. The immune architecture of eosinophilic esophagitis: mechanisms, therapeutic targets, and precision management. ImmunoTargets and Therapy, Volume 15:1-27, May 2026. URL: https://doi.org/10.2147/itt.s510865, doi:10.2147/itt.s510865. This article has 0 citations.

21. (ariasgonzalez2024fibrousremodelingin pages 1-2): Laura Arias-González, Leticia Rodríguez-Alcolado, Emilio J. Laserna-Mendieta, Pilar Navarro, Alfredo J. Lucendo, and Elena Grueso-Navarro. Fibrous remodeling in eosinophilic esophagitis: clinical facts and pathophysiological uncertainties. International Journal of Molecular Sciences, 25:927, Jan 2024. URL: https://doi.org/10.3390/ijms25020927, doi:10.3390/ijms25020927. This article has 21 citations.

22. (imam2026theroleof pages 5-5): Manal Bel Imam, Hang Du, Özge Ardicli, Jenne Meinema, and Willem van de Veen. The role of b cells and antibodies in eosinophilic esophagitis. Inflammatory Intestinal Diseases, 11:105-122, Feb 2026. URL: https://doi.org/10.1159/000551065, doi:10.1159/000551065. This article has 0 citations.

23. (farah2025thedynamicevolution pages 10-12): Amir Farah, Tarek Assaf, Jawad Hindy, Wisam Abboud, Mostafa Mahamid, Edoardo Vincenzo Savarino, and Amir Mari. The dynamic evolution of eosinophilic esophagitis. Diagnostics, 15:240, Jan 2025. URL: https://doi.org/10.3390/diagnostics15030240, doi:10.3390/diagnostics15030240. This article has 14 citations.

24. (low2024reviewarticleemerging pages 1-3): Eric E. Low and Evan S. Dellon. Review article: emerging insights into the epidemiology, pathophysiology, diagnostic and therapeutic aspects of eosinophilic oesophagitis and other eosinophilic gastrointestinal diseases. Alimentary Pharmacology & Therapeutics, 59:322-340, Dec 2024. URL: https://doi.org/10.1111/apt.17845, doi:10.1111/apt.17845. This article has 41 citations and is from a highest quality peer-reviewed journal.

25. (farah2025thedynamicevolution pages 12-13): Amir Farah, Tarek Assaf, Jawad Hindy, Wisam Abboud, Mostafa Mahamid, Edoardo Vincenzo Savarino, and Amir Mari. The dynamic evolution of eosinophilic esophagitis. Diagnostics, 15:240, Jan 2025. URL: https://doi.org/10.3390/diagnostics15030240, doi:10.3390/diagnostics15030240. This article has 14 citations.

26. (bertin2026theimmunearchitecture pages 10-12): Luisa Bertin, Federico Caldart, Alberto Barchi, Niccolò Seregni, Andrea Pasta, Francesco Calabrese, Elisa Marabotto, Amir Mari, Amir Farah, Emma Sirinic, Andrea Sorge, Matteo Ghisa, Javier Chahuán, Vincenzo Savarino, and Edoardo Vincenzo Savarino. The immune architecture of eosinophilic esophagitis: mechanisms, therapeutic targets, and precision management. ImmunoTargets and Therapy, Volume 15:1-27, May 2026. URL: https://doi.org/10.2147/itt.s510865, doi:10.2147/itt.s510865. This article has 0 citations.

27. (musburger2025currentandemerging pages 6-7): Brooke G. Musburger, Maria Gonzalez Echeandia, Elias L. Suskind, David L. Suskind, Hengqi Betty Zheng, and Dominique Mark. Current and emerging therapies for eosinophilic esophagitis (eoe): a comprehensive review. Pharmaceutics, 17:753, Jun 2025. URL: https://doi.org/10.3390/pharmaceutics17060753, doi:10.3390/pharmaceutics17060753. This article has 4 citations.

28. (low2024reviewarticleemerging pages 9-11): Eric E. Low and Evan S. Dellon. Review article: emerging insights into the epidemiology, pathophysiology, diagnostic and therapeutic aspects of eosinophilic oesophagitis and other eosinophilic gastrointestinal diseases. Alimentary Pharmacology & Therapeutics, 59:322-340, Dec 2024. URL: https://doi.org/10.1111/apt.17845, doi:10.1111/apt.17845. This article has 41 citations and is from a highest quality peer-reviewed journal.

29. (bertin2026theimmunearchitecture pages 12-14): Luisa Bertin, Federico Caldart, Alberto Barchi, Niccolò Seregni, Andrea Pasta, Francesco Calabrese, Elisa Marabotto, Amir Mari, Amir Farah, Emma Sirinic, Andrea Sorge, Matteo Ghisa, Javier Chahuán, Vincenzo Savarino, and Edoardo Vincenzo Savarino. The immune architecture of eosinophilic esophagitis: mechanisms, therapeutic targets, and precision management. ImmunoTargets and Therapy, Volume 15:1-27, May 2026. URL: https://doi.org/10.2147/itt.s510865, doi:10.2147/itt.s510865. This article has 0 citations.

30. (dsilva2026insightsintothe pages 2-4): Anish Dsilva and Ariel Munitz. Insights into the pathogenesis of eosinophilic esophagitis using mouse models. Myeloid Cells, Jan 2026. URL: https://doi.org/10.70401/mc.2026.0003, doi:10.70401/mc.2026.0003. This article has 0 citations.

31. (jackson2025mousemodelsof pages 9-11): Jazmyne L. Jackson, Abigail J. Staub, Annie D. Fuller, John M. Crespo, Travis H. Bordner, Courtney Worrell, No’ad Shanas, Danielle Waheed, Tatiana A. Karakasheva, Melanie A. Ruffner, Amanda B. Muir, and Kelly A. Whelan. Mouse models of eosinophilic esophagitis: molecular and translational insights. Jul 2025. URL: https://doi.org/10.1152/ajpgi.00396.2024, doi:10.1152/ajpgi.00396.2024. This article has 2 citations.

32. (uchida2022modelsandtools pages 1-2): Amiko M. Uchida, Gabrielle Ro, John J. Garber, Kathryn A. Peterson, and June L. Round. Models and tools for investigating eosinophilic esophagitis at the bench. Frontiers in Immunology, Jul 2022. URL: https://doi.org/10.3389/fimmu.2022.943518, doi:10.3389/fimmu.2022.943518. This article has 6 citations and is from a peer-reviewed journal.

33. (jackson2025mousemodelsof pages 14-16): Jazmyne L. Jackson, Abigail J. Staub, Annie D. Fuller, John M. Crespo, Travis H. Bordner, Courtney Worrell, No’ad Shanas, Danielle Waheed, Tatiana A. Karakasheva, Melanie A. Ruffner, Amanda B. Muir, and Kelly A. Whelan. Mouse models of eosinophilic esophagitis: molecular and translational insights. Jul 2025. URL: https://doi.org/10.1152/ajpgi.00396.2024, doi:10.1152/ajpgi.00396.2024. This article has 2 citations.

34. (dsilva2026insightsintothe pages 11-13): Anish Dsilva and Ariel Munitz. Insights into the pathogenesis of eosinophilic esophagitis using mouse models. Myeloid Cells, Jan 2026. URL: https://doi.org/10.70401/mc.2026.0003, doi:10.70401/mc.2026.0003. This article has 0 citations.

35. (dsilva2026insightsintothe pages 14-16): Anish Dsilva and Ariel Munitz. Insights into the pathogenesis of eosinophilic esophagitis using mouse models. Myeloid Cells, Jan 2026. URL: https://doi.org/10.70401/mc.2026.0003, doi:10.70401/mc.2026.0003. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Eosinophilic_Esophagitis-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Eosinophilic_Esophagitis-deep-research-falcon_artifacts/artifact-01.md)