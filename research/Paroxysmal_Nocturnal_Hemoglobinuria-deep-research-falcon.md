---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-24T16:12:58.776328'
end_time: '2026-07-24T16:26:25.944096'
duration_seconds: 807.17
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Paroxysmal Nocturnal Hemoglobinuria
  mondo_id: ''
  category: Hematologic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Paroxysmal_Nocturnal_Hemoglobinuria-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Paroxysmal Nocturnal Hemoglobinuria
- **MONDO ID:**  (if available)
- **Category:** Hematologic

## Research Objectives

Please provide a comprehensive research report on **Paroxysmal Nocturnal Hemoglobinuria** covering all of the
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
- **Disease Name:** Paroxysmal Nocturnal Hemoglobinuria
- **MONDO ID:**  (if available)
- **Category:** Hematologic

## Research Objectives

Please provide a comprehensive research report on **Paroxysmal Nocturnal Hemoglobinuria** covering all of the
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


# Paroxysmal Nocturnal Hemoglobinuria: Disease-Characteristics Report

## Executive summary

Paroxysmal nocturnal hemoglobinuria (PNH) is a rare, acquired, non-Mendelian clonal hematopoietic stem-cell disorder. A somatic loss-of-function mutation—usually in **PIGA**—prevents biosynthesis of the glycosylphosphatidylinositol (GPI) anchor. Consequently, affected blood cells lack GPI-anchored complement regulators, especially **CD55/decay-accelerating factor** and **CD59**, and become susceptible to complement-mediated injury. The defining clinical spectrum comprises chronic or episodic intravascular hemolysis, thrombosis, and variable bone-marrow failure. Modern complement inhibitors have greatly improved survival, but residual anemia, breakthrough hemolysis, infection risk, adherence, marrow failure, and access remain important unmet needs. (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2, versino2024complementinhibitionin pages 2-2, colden2022insightsintothe pages 1-3)

The following table provides a compact knowledge-base summary; ontology accessions marked for validation should be checked directly against the current source ontology before production ingestion.

| Domain | Key facts | Suggested ontology mappings* | Key evidence |
|---|---|---|---|
| Identity / identifiers | Paroxysmal nocturnal hemoglobinuria (PNH) is a rare, acquired clonal hematopoietic stem-cell disorder characterized by complement-mediated hemolysis, thrombophilia, and variable bone-marrow failure; disease-level information here is derived from aggregated literature/registry resources rather than individual EHRs. Common synonyms: PNH; paroxysmal nocturnal haemoglobinuria. MONDO/OMIM/Orphanet/MeSH/ICD identifiers should be independently validated before KB ingestion if exact accession is required. | MONDO: PNH **[validate exact accession]**; MeSH: **[validate]**; ICD-10/11: **[validate]** | (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2, apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2, colden2022insightsintothe pages 1-3) |
| Cause / etiology | Primary cause is acquired somatic loss-of-function mutation of **PIGA** in hematopoietic stem cells on Xp22.1, causing GPI-anchor deficiency. PIGA mutation is necessary but often considered insufficient alone for overt disease; clonal expansion is linked to immune-mediated marrow failure context, especially aplastic anemia. No Mendelian inheritance pattern for classic PNH. | Gene: **PIGA**; CL: hematopoietic stem cell **[validate exact CL term]** | (versino2024complementinhibitionin pages 1-2, apostolidou2025paroxysmalnocturnalhemoglobinuria pages 2-4, versino2024complementinhibitionin pages 2-3, colden2022insightsintothe pages 1-3, chen2021advancesinthe pages 1-3) |
| Core mechanism / pathophysiology | Loss of GPI anchors removes complement regulators **CD55/DAF** and **CD59** from RBCs (and other blood cells), permitting alternative-pathway amplification, terminal complement activation, and MAC-mediated intravascular hemolysis. Upstream C3 deposition also drives extravascular hemolysis under C5 blockade. Free hemoglobin scavenges nitric oxide, contributing to smooth-muscle dystonia, vasospasm, platelet activation, endothelial dysfunction, thrombosis, renal injury, and pulmonary hypertension. | GO: complement activation, alternative pathway **[validate]**; GO: membrane attack complex assembly **[validate]**; GO: hemolysis **[validate]**; GO: nitric oxide metabolic process **[validate]**; CL: erythrocyte **[validate]**, platelet **[validate]**, neutrophil **[validate]**; UBERON: bone marrow **[validate]**, blood **[validate]**, kidney **[validate]**, lung vasculature **[validate]** | (versino2024complementinhibitionin pages 3-4, risitano2008paroxysmalnocturnalhemoglobinuria pages 3-4, versino2024complementinhibitionin pages 2-3, apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2, hillmen2024navigatingthecomplement pages 7-9) |
| Major phenotypes with frequencies | Registry baseline burden (untreated at enrollment): fatigue **80.9–81%**, dyspnea **45.3%**, hemoglobinuria **45.0%**, abdominal pain **35.2%**, impaired renal function **42.8%**, high disease activity **51.6%**, bone-marrow failure **62.6%**, RBC transfusion history **61.3%**, major adverse vascular events **18.8%**; thrombosis may affect up to **40%** in some series/reviews and can be the first manifestation, often at unusual venous sites. QoL study (China): anxiety/depression problems **81.5%**, pain/discomfort **69.9%**, mean EQ-5D-5L utility **0.76**, EQ-VAS **62.61**. | HPO: fatigue **[validate]**; dyspnea **[validate]**; hemoglobinuria **[validate]**; abdominal pain **[validate]**; anemia **[validate]**; thrombosis **[validate]**; bone marrow hypocellularity/failure **[validate]**; renal insufficiency **[validate]**; pulmonary hypertension **[validate]** | (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2, schrezenmeier2020baselineclinicalcharacteristics pages 1-2, schrezenmeier2020baselineclinicalcharacteristics pages 3-5, yu2024healthrelatedqualityof pages 1-2) |
| Diagnosis | Gold standard is high-sensitivity flow cytometry demonstrating GPI-deficient populations across ≥2 blood cell lineages, typically using **FLAER** with lineage markers for granulocytes/monocytes and CD55/CD59 or related markers on RBCs. In the APPLY/APPOINT trial population, diagnostic eligibility required flow-confirmed affected red-cell and white-cell populations ≥10%. Screening is particularly relevant in aplastic anemia and unexplained persistent cytopenias. | MAXO: flow cytometry assay **[validate]**; CL: granulocyte **[validate]**, monocyte **[validate]**, erythrocyte **[validate]** | (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 2-4, almakadi2025clinicalcharacteristicsand pages 4-6, latour2024oraliptacopanmonotherapy pages 1-4) |
| Epidemiology / population | Reported prevalence ranges roughly **10–20 per million** globally; some reviews cite **13–38 per million**. Incidence is commonly **1–1.5 per million/year**; some sources report **0.08–0.57 per 100,000 person-years**. Median age at diagnosis/onset is typically **35–40 years**; no strong sex predilection is consistently observed. Italian real-world analysis estimated prevalence **17.6 per million** adults (Dec 2021) and incidence **1.5 per million/year**. | MONDO: PNH **[validate]** | (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2, apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2, schrezenmeier2020baselineclinicalcharacteristics pages 3-5, yu2024healthrelatedqualityof pages 1-2) |
| Current therapies | Complement inhibition is standard of care for hemolytic PNH. Established agents: **eculizumab** (anti-C5; FDA 2007), **ravulizumab** (long-acting anti-C5; every 8 weeks), **pegcetacoplan** (C3 inhibitor; approved 2021), **iptacopan** (oral factor B inhibitor; FDA Dec 6, 2023), **danicopan** (factor D inhibitor; add-on/novel proximal inhibitor), and **crovalimab** (anti-C5; approved in 2024 in some jurisdictions per recent reviews). Supportive care includes RBC transfusion, anticoagulation when indicated, immunosuppressive therapy for marrow failure, and vaccination against encapsulated bacteria before complement inhibition; allogeneic HSCT remains the only curative option for selected fit patients, especially with severe marrow failure. | MAXO: complement inhibition therapy **[validate]**; monoclonal antibody therapy **[validate]**; blood transfusion **[validate]**; anticoagulation therapy **[validate]**; hematopoietic stem-cell transplantation **[validate]**; CHEBI/drug mappings **[validate separately]** | (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2, apostolidou2025paroxysmalnocturnalhemoglobinuria pages 6-8, perry2025theadvancinglandscape pages 3-4, schrezenmeier2020baselineclinicalcharacteristics pages 3-5, apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2) |
| 2023–2024 advances | **Iptacopan** phase 3 (APPLY-PNH, APPOINT-PNH; NEJM 2024): in anti-C5-treated patients, **51/60** achieved Hb increase ≥2 g/dL without transfusion and **42/60** achieved Hb ≥12 g/dL without transfusion vs **0/35** on continued anti-C5; in complement-inhibitor–naive patients, **31/33** achieved Hb increase ≥2 g/dL without transfusion. **59/62** iptacopan-treated vs **14/35** anti-C5-treated patients avoided transfusion in APPLY; in APPOINT, no patients required transfusion. Reviews summarize ravulizumab as noninferior to eculizumab with fewer breakthrough hemolysis events and pegcetacoplan as superior to eculizumab for persistent anemia in PEGASUS, with PRINCE supporting first-line use. | MAXO: oral small-molecule therapy **[validate]**; complement factor B inhibition **[validate]**; complement C3 inhibition **[validate]** | (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 6-8, perry2025theadvancinglandscape pages 3-4, latour2024oraliptacopanmonotherapy pages 1-4, hillmen2024navigatingthecomplement pages 7-9) |
| Prognosis / outcomes | Pre-complement era mortality was substantial; some retrospective analyses cited ~**35% 5-year mortality** and ~**50% 10-year mortality**. Complement inhibition markedly improves survival and reduces thrombosis. Review data cite **5-year survival 95.5%** with eculizumab and thrombotic events decreasing from **5.6 to 0.8 per 100 patient-years**. Thrombosis remains the leading cause of death in untreated disease and still occurs at lower frequency in the complement-inhibitor era. | HPO: reduced survival **[validate]**; thrombosis **[validate]**; chronic kidney disease **[validate]** | (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2, perry2025theadvancinglandscape pages 3-4, risitano2008paroxysmalnocturnalhemoglobinuria pages 3-4) |
| Model systems / comparative biology | Mouse and rhesus macaque PIGA-loss models recapitulate GPI-AP-deficient blood cells, shortened erythrocyte lifespan, and complement sensitivity, but generally **do not develop full human clinical hemolysis/thrombosis** or sustained clonal expansion. These models suggest **PIGA mutation alone is insufficient** and that immune context/secondary factors are important. No strong evidence from collected sources for a naturally occurring veterinary analog was identified. | CL: hematopoietic stem/progenitor cell **[validate]**; GO: erythrocyte homeostasis **[validate]** | (colden2022insightsintothe pages 1-3, chen2021advancesinthe pages 1-3) |
| Important gaps / caution flags | Exact disease identifiers (MONDO/OMIM/Orphanet/MeSH/ICD/HPO/GO/CL/UBERON/MAXO accessions) were not directly verified in the collected evidence and should be checked against the source ontologies before production use. Recent literature mentions additional somatic mutations and clonal hematopoiesis in marrow-failure contexts, but no robust disease-specific modifier set with validated clinical effect was established from the collected evidence. Omics/single-cell/spatial transcriptomic evidence was not clearly available in the retrieved material. | All exact accession numbers: **independent validation required** | (versino2024complementinhibitionin pages 2-3, colden2022insightsintothe pages 1-3, chen2021advancesinthe pages 1-3) |


*Table: This compact table summarizes core disease facts for paroxysmal nocturnal hemoglobinuria, including cause, mechanism, phenotypes, diagnosis, epidemiology, treatment advances, prognosis, and model systems. It also flags ontology mappings and identifiers that should be independently validated before database ingestion.*

## 1. Disease information

### Definition, identifiers, and synonyms

**Preferred name:** paroxysmal nocturnal hemoglobinuria. **Synonyms:** paroxysmal nocturnal haemoglobinuria, PNH, Marchiafava–Micheli disease, and Strübing–Marchiafava disease. The historical name is imperfect: hemolysis is not necessarily paroxysmal, nocturnal, or accompanied by visible hemoglobinuria.

Commonly assigned identifiers are **OMIM 300818**, **Orphanet ORPHA:447**, **ICD-10-CM D59.5**, and **MeSH D006457**. A commonly used MONDO mapping is **MONDO:0012727**, but all identifiers—particularly the current ICD-11 and MONDO releases—should be verified against the live terminology service before database release.

This report concerns **aggregated disease-level evidence** from peer-reviewed studies, international registries, consensus literature, and trials. It is not derived from an individual patient’s EHR. The International PNH Registry analysis included 4,439 patients and is therefore population-level observational evidence. (schrezenmeier2020baselineclinicalcharacteristics pages 1-2)

## 2. Etiology, risks, and protective factors

### Primary cause

Classic PNH is caused by an **acquired somatic**, not inherited, loss-of-function mutation in **PIGA**, an X-linked gene at Xp22. PIGA participates in the first step of GPI-anchor synthesis in the endoplasmic reticulum. Because only one active X chromosome is present in each hematopoietic cell, a single somatic hit can produce the phenotype. Hundreds of private mutations have been reported—including small insertions/deletions, substitutions, nonsense, frameshift, and splice-altering lesions—with no dominant hotspot; one sequencing series found 26 PIGA mutations among 33 patients and identified exon 2 as the most frequently affected region. (versino2024complementinhibitionin pages 2-3, chen2021advancesinthe pages 1-3)

PIGA mutation is **necessary but generally insufficient** for clinically overt PNH. Tiny GPI-deficient populations, approximately 0.001–0.005%, can occur in healthy people, whereas expanded clones occur in nearly half of patients with immune-mediated acquired aplastic anemia. The leading “escape” model proposes that autoreactive T-cell pressure suppresses normal hematopoiesis while GPI-deficient hematopoietic stem/progenitor cells enjoy relative survival—not an autonomous proliferative advantage. Mouse and macaque experiments support this interpretation because mutant cells reconstitute hematopoiesis but do not progressively dominate. (colden2022insightsintothe pages 1-3)

### Risk and modifier factors

* **Strong clinical context:** acquired aplastic anemia and other immune-mediated marrow-failure states. Clone evolution can occur during recovery after immunosuppression. (colden2022insightsintothe pages 1-3)
* **Clone size:** larger granulocyte clones generally correlate with hemolysis, high disease activity, and thrombosis, although clinically important events occur even with clones below 10%. (schrezenmeier2020baselineclinicalcharacteristics pages 1-2)
* **Physiologic complement-amplifying conditions:** infection, trauma, surgery, pregnancy, and other inflammatory states can precipitate pharmacodynamic breakthrough hemolysis. (versino2024complementinhibitionin pages 1-2, hillmen2024navigatingthecomplement pages 7-9)
* **Additional somatic variants:** exploratory studies have reported variants in genes including **TET2, CUX1, SUZ12, RBPJ, MUC4, MLL2/KMT2D**, and others. Their causal or prognostic roles are not sufficiently validated for routine PNH risk stratification. RBPJ knockdown increased apoptosis and reduced proliferation in patient-derived cells in vitro, but in-vivo confirmation is lacking. (chen2021advancesinthe pages 1-3)
* **Thrombophilia alleles:** factor V Leiden and MTHFR polymorphisms have been examined, but a disease-modifying causal effect remains unproven. (risitano2008paroxysmalnocturnalhemoglobinuria pages 3-4)

No reproducible dietary, lifestyle, occupational, toxin, infectious-agent, or environmental cause has been established. There are likewise no validated inherited protective alleles or lifestyle measures that prevent acquisition of PNH. Avoiding infection and promptly treating complement-amplifying conditions reduces complications rather than preventing the initial clone.

## 3. Phenotypes

PNH may present from childhood to late adulthood but is predominantly an adult-onset disease, with median diagnosis around 35–40 years. Severity is highly variable; manifestations are chronic with episodic exacerbations. (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2, yu2024healthrelatedqualityof pages 1-2)

### Principal phenotypes and suggested HPO annotations

* **Coombs-negative intravascular hemolytic anemia:** anemia, reticulocytosis, elevated LDH and indirect bilirubin, low haptoglobin, plasma-free hemoglobin, and hemoglobinuria/hemosiderinuria. Suggested HPO: *Hemolytic anemia*, *Intravascular hemolysis*, *Reticulocytosis*, *Elevated lactate dehydrogenase*, *Hemoglobinuria*. (versino2024complementinhibitionin pages 3-4)
* **Fatigue and exercise intolerance:** fatigue occurred in 80.9–81% of registry patients; dyspnea occurred in 45.3%. Suggested HPO: *Fatigue*, *Exercise intolerance*, *Dyspnea*. (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2, schrezenmeier2020baselineclinicalcharacteristics pages 3-5)
* **Hemoglobinuria:** reported by 45.0%; it may be episodic and is neither required nor always nocturnal. Suggested HPO: *Hemoglobinuria*. (schrezenmeier2020baselineclinicalcharacteristics pages 3-5)
* **Smooth-muscle dystonia:** abdominal pain (35.2%), dysphagia, esophageal spasm, and erectile dysfunction arise largely from nitric-oxide depletion. Suggested HPO: *Abdominal pain*, *Dysphagia*, *Erectile dysfunction*. (versino2024complementinhibitionin pages 3-4, schrezenmeier2020baselineclinicalcharacteristics pages 3-5)
* **Thrombosis:** venous events predominate and frequently involve unusual sites—hepatic/Budd–Chiari, portal, mesenteric, splenic, or cerebral veins. Thrombosis may be the first manifestation and historically affected up to approximately 40% of patients. Suggested HPO: *Venous thrombosis*, *Budd-Chiari syndrome*, *Cerebral venous thrombosis*. (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2)
* **Bone-marrow failure/cytopenias:** aplastic anemia, pancytopenia, neutropenia, and thrombocytopenia may precede, accompany, or follow hemolytic PNH. Bone-marrow failure was recorded in 62.6% of the large registry cohort. Suggested HPO: *Bone marrow hypocellularity*, *Pancytopenia*, *Thrombocytopenia*, *Neutropenia*. (schrezenmeier2020baselineclinicalcharacteristics pages 1-2)
* **Renal disease:** acute kidney injury during hemolytic crises and chronic impairment from repeated hemoglobin filtration, hemosiderin deposition, tubular injury, and vascular dysfunction; registry impaired renal function was 42.8%. Suggested HPO: *Renal insufficiency*, *Acute kidney injury*, *Hemosiderinuria*. (schrezenmeier2020baselineclinicalcharacteristics pages 1-2, apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2)
* **Pulmonary/vascular disease:** pulmonary hypertension and dyspnea can follow NO depletion, hemolysis, and thromboembolism. Suggested HPO: *Pulmonary hypertension*. (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2)

Clinical categories include classic hemolytic PNH, PNH associated with another marrow disorder, subclinical PNH, and a proposed ahemolytic/“white PNH” phenotype with a sizable clone but little biochemical hemolysis. Clone-size boundaries are descriptive rather than absolute treatment criteria. (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 2-4)

### Quality of life

A 2024 Chinese cross-sectional study of 329 patients found anxiety/depression problems in 81.5%, pain/discomfort in 69.9%, mean EQ-5D-5L utility 0.76, and mean EQ-VAS 62.61. Anemia symptoms, back pain, hemoglobinuria, thrombosis, sex, and income influenced HRQoL. Diagnostic burden is also substantial: fewer than 40% have historically been diagnosed within 12 months of symptom onset, while 24% waited at least five years. (yu2024healthrelatedqualityof pages 1-2)

## 4. Genetic and molecular information

**Causal gene:** **PIGA**; the relevant lesions are somatic variants in a multipotent hematopoietic stem cell. They are absent from the constitutional germline in ordinary PNH and therefore should not be interpreted using population carrier frequency or Mendelian penetrance concepts. Germline PIGA variants instead cause a distinct congenital disorder of GPI-anchor biosynthesis, not classic PNH.

Most pathogenic PNH variants produce partial or complete loss of function. **Type III cells** completely lack GPI-anchored proteins and are much more complement-sensitive; **type II cells** retain partial expression; **type I cells** are phenotypically normal. Flow cytometry—not germline variant classification—is the clinically decisive assay. (kelly2025pharmacologicaltherapiesin pages 1-2, versino2024complementinhibitionin pages 3-4)

No recurrent chromosomal abnormality defines PNH. Cytogenetic or myeloid-gene abnormalities may indicate associated MDS or clonal evolution and should be interpreted as comorbidity/modification rather than the defining lesion. WES/WGS may detect PIGA or secondary variants but is not first-line diagnostic testing.

Epigenetic, single-cell, spatial-transcriptomic, proteomic, metabolomic, and lipidomic signatures are not sufficiently standardized for clinical annotation. Current omics work is chiefly exploratory; no omics-based diagnostic has displaced flow cytometry.

## 5. Environmental information

PNH is not caused by a pathogen, toxin, diet, smoking, alcohol, radiation, or occupation. Infection, surgery, trauma, and pregnancy can increase complement activation and trigger hemolysis in an existing clone. These are **triggers/modifiers**, not primary causes. There is no zoonotic transmission or infectious reservoir. (versino2024complementinhibitionin pages 1-2, hillmen2024navigatingthecomplement pages 7-9)

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. A somatic **PIGA** lesion occurs in a hematopoietic stem cell.
2. Defective ER GPI-anchor synthesis prevents surface attachment of nearly 150 GPI-linked proteins.
3. Descendant erythrocytes, granulocytes, monocytes, and platelets lack CD55 and CD59.
4. CD55 loss impairs decay of C3/C5 convertases; CD59 loss permits C5b-9 membrane-attack-complex assembly.
5. Constitutive alternative-pathway “tick-over,” factor B/factor D amplification, and terminal complement activation lyse PNH erythrocytes. (versino2024complementinhibitionin pages 2-3, colden2022insightsintothe pages 1-3)

### Downstream injury

Intravascular hemolysis releases free hemoglobin, which scavenges nitric oxide. NO depletion causes vasoconstriction and smooth-muscle dystonia, explaining abdominal pain, dysphagia, erectile dysfunction, fatigue, and part of the pulmonary hypertension phenotype. Hemoglobin/iron filtration causes renal tubular hemosiderosis and dysfunction. (risitano2008paroxysmalnocturnalhemoglobinuria pages 3-4, apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2)

Thrombosis is multifactorial: complement-mediated platelet and endothelial activation, procoagulant microparticles, leukocyte activation, tissue-factor and inflammatory signaling, impaired fibrinolysis—including possible loss of GPI-anchored uPAR—and NO depletion reinforce coagulation. The complement and coagulation systems form a bidirectional amplification loop. (risitano2008paroxysmalnocturnalhemoglobinuria pages 3-4, fattizzo2026thrombosisinparoxysmal pages 1-2, apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2)

Under C5 blockade, C3 fragments may accumulate on surviving PNH erythrocytes and mark them for hepatic/splenic phagocytosis, causing **C3-mediated extravascular hemolysis**. Proximal inhibitors at C3, factor B, or factor D address this mechanism. (kelly2025pharmacologicaltherapiesin pages 1-2, hillmen2024navigatingthecomplement pages 7-9)

Suggested annotations include GO *GPI-anchor biosynthetic process*, *complement activation, alternative pathway*, *membrane attack complex assembly*, *erythrocyte homeostasis*, *nitric oxide metabolic process*, and *blood coagulation*; CL *hematopoietic stem cell*, *erythrocyte*, *monocyte*, *neutrophil*, *platelet*, *endothelial cell*, and *macrophage*.

## 7. Anatomical structures affected

The primary compartment is **bone marrow hematopoiesis** and circulating blood. Directly affected cell lineages include erythrocytes, granulocytes, monocytes, and platelets. Secondary organs include the kidney, liver and splanchnic venous system, cerebral veins, lungs/pulmonary vasculature, spleen, and gastrointestinal tract. No lateralization applies. Subcellular compartments include the ER/Golgi GPI-biosynthetic pathway, plasma membrane, extracellular complement cascade, and MAC. Suggested UBERON mappings: bone marrow, blood, kidney, liver, spleen, lung, pulmonary artery, portal vein, hepatic vein, and cerebral venous system.

## 8. Temporal development

Onset is usually insidious in young-to-middle adulthood, although pediatric and geriatric disease occurs. The clone may remain small and asymptomatic, expand during immune marrow failure, produce chronic hemolysis with episodic crises, regress, or coexist with persistent aplasia. Small clones should be monitored because clinical burden is not zero: among clones below 10%, registry rates were 9.7% for hemolysis, 10.2% for major adverse vascular events, and 9.1% for high disease activity. (schrezenmeier2020baselineclinicalcharacteristics pages 1-2)

PNH is generally chronic. Spontaneous clonal contraction/remission can occur, but the timing is unpredictable. Critical intervention windows include active hemolysis, new thrombosis, pregnancy, major surgery, infection, transfusion dependence, and worsening marrow failure.

## 9. Inheritance, epidemiology, and population

PNH has **no Mendelian inheritance pattern**, carrier state, anticipation, founder effect, consanguinity association, or conventional germline penetrance. Familial recurrence is not expected, and routine cascade or reproductive genetic screening is inappropriate for classic PNH.

Reported estimates vary with ascertainment: prevalence is commonly 10–20 per million, with broader estimates of 13–38 per million; incidence is often approximately 1–1.5 per million/year. A 2024 review cited incidence 0.08–0.57 per 100,000 person-years and prevalence about 38 per million. There is no consistent sex, race, ethnicity, or geographic predilection, although ascertainment and access differ markedly. (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2, yu2024healthrelatedqualityof pages 1-2)

In the 4,439-patient registry, 51.6% had high disease activity, 18.8% a major adverse vascular event, 62.6% marrow failure, 61.3% prior RBC transfusion, and 42.8% impaired renal function. (schrezenmeier2020baselineclinicalcharacteristics pages 1-2)

## 10. Diagnostics

### Recommended approach

**High-sensitivity multiparameter flow cytometry on peripheral blood is the diagnostic gold standard.** Demonstrate deficient GPI-linked proteins in at least two lineages. Granulocyte/monocyte assays commonly combine **FLAER** with CD24, CD14, CD157, CD15, CD45, and/or CD64; RBC assays use CD235a gating with CD59 and sometimes CD55. Granulocyte and monocyte clone sizes best estimate the stem-cell clone because transfusion and hemolysis can underestimate RBC clones. (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 2-4, almakadi2025clinicalcharacteristicsand pages 4-6)

Initial laboratory evaluation includes CBC/differential, reticulocytes, blood smear, LDH, bilirubin, haptoglobin, plasma-free hemoglobin, urinalysis, renal function, iron indices, and direct antiglobulin testing. Bone-marrow aspirate/biopsy and cytogenetic/myeloid NGS evaluation are indicated when aplastic anemia, MDS, or unexplained cytopenias are suspected.

Screen appropriate patients with acquired aplastic anemia; unexplained Coombs-negative hemolysis; hemoglobinuria; unexplained cytopenias; MDS with hypocellularity; thrombosis at unusual sites; or thrombosis accompanied by hemolysis/cytopenia. Historical Ham and sucrose-lysis tests are obsolete except in legacy reports.

### Differential diagnosis

Exclude autoimmune hemolytic anemia, hereditary membrane/enzyme defects, microangiopathic hemolysis, cold-antibody disease, mechanical hemolysis, march hemoglobinuria, infection-associated hemolysis, and other marrow-failure/MDS syndromes. PNH is distinguished by a reproducible GPI-deficient clone across blood lineages.

WES, WGS, single-gene sequencing, CMA, FISH, karyotyping, mtDNA, and repeat-expansion tests are not routine confirmatory tests for PNH. Population, newborn, carrier, prenatal, and preimplantation screening are not indicated.

## 11. Outcomes and prognosis

Before complement inhibition, thrombosis was the leading cause of death and retrospective estimates included approximately 35% five-year mortality and 50% ten-year mortality. Contemporary complement therapy has transformed prognosis; a review cited 95.5% five-year survival with eculizumab and reduction in thrombotic events from 5.6 to 0.8 per 100 patient-years. (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2, perry2025theadvancinglandscape pages 3-4)

Poor prognostic factors include prior thrombosis, large/expanding clone, severe hemolysis, transfusion dependence, renal impairment, pulmonary hypertension, persistent cytopenias, severe aplastic anemia, MDS/AML evolution, and inadequate complement control. Residual anemia may reflect extravascular hemolysis, breakthrough intravascular hemolysis, iron deficiency, renal dysfunction, or marrow failure.

## 12. Treatment and recent developments

### Complement-directed therapy

* **Eculizumab**, anti-C5 monoclonal antibody, FDA-approved in 2007, suppresses MAC-mediated intravascular hemolysis and substantially reduces transfusion, thrombosis, renal injury, and mortality. Limitations are intravenous dosing every two weeks, C3-mediated extravascular hemolysis, and breakthrough hemolysis. Suggested MAXO: complement-inhibitor therapy; monoclonal-antibody therapy. (versino2024complementinhibitionin pages 2-2, perry2025theadvancinglandscape pages 3-4)
* **Ravulizumab**, recycled long-acting anti-C5 antibody, permits approximately eight-week dosing. Phase III studies established noninferiority to eculizumab; review data report transfusion avoidance of 73.6% versus 66.1% and breakthrough hemolysis of 4.0% versus 10.7%. (perry2025theadvancinglandscape pages 3-4)
* **Pegcetacoplan**, subcutaneous C3/C3b inhibitor approved in 2021, inhibits proximal and terminal activation and controls both intravascular and C3-mediated extravascular hemolysis. PEGASUS showed superiority to eculizumab for persistent anemia; PRINCE supported use in complement-inhibitor-naïve disease. Injection-site reactions are common. (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 6-8, hillmen2024navigatingthecomplement pages 7-9)
* **Iptacopan**, oral factor-B inhibitor, received FDA approval on 6 December 2023. In 2024 APPLY-PNH, 51/60 patients switching from anti-C5 achieved a ≥2-g/dL hemoglobin increase and 42/60 reached hemoglobin ≥12 g/dL without transfusion, versus 0/35 continuing anti-C5. In APPOINT-PNH, 31/33 untreated patients achieved a ≥2-g/dL increase without transfusion. Transfusion avoidance was 59/62 versus 14/35 in APPLY; no APPOINT patient required transfusion. Headache was the most frequent adverse event. Trials: NCT04558918 and NCT04820530; published 14 March 2024, DOI https://doi.org/10.1056/NEJMoa2308695. (latour2024oraliptacopanmonotherapy pages 1-4)
* **Danicopan**, oral factor-D inhibitor, is used as add-on therapy to anti-C5 in selected patients with clinically significant extravascular hemolysis/residual anemia. It targets alternative-pathway amplification while preserving established terminal blockade. (versino2024complementinhibitionin pages 1-2)
* **Crovalimab**, a recycling subcutaneous anti-C5 antibody, showed noninferiority to eculizumab in the COMMODORE program and offers less frequent administration. (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 6-8)

All complement inhibitors increase susceptibility to invasive infection—especially **Neisseria meningitidis** and, depending on the breadth of blockade, other encapsulated bacteria such as pneumococcus and *Haemophilus influenzae*. Vaccination should precede treatment when feasible; urgent therapy should not be delayed when clinically necessary, but antibiotic prophylaxis and local regulatory guidance should then be followed. Vaccination does not eliminate risk, so fever or meningococcal symptoms require emergency evaluation. (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 6-8)

### Treatment strategy

Treat clinically significant hemolysis, symptomatic anemia, thrombosis, organ injury, transfusion dependence, or high disease activity—not clone size alone. A C5 inhibitor remains appropriate for robust intravascular control; proximal inhibition is attractive for residual C3-mediated anemia or oral/subcutaneous convenience. There was no universally accepted evidence-based first-line algorithm in 2024; selection should incorporate marrow reserve, hemolysis type, thrombosis history, adherence, pregnancy, infection risk, route, availability, and cost. (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2)

Supportive measures include phenotype-matched RBC transfusion, folate and iron replacement when deficient, treatment of infection, renal support, and careful avoidance of unnecessary corticosteroids. Anticoagulation is indicated for acute thrombosis, generally together with complement inhibition; duration should be individualized. Registry baseline use included transfusion in 61.3%, anticoagulation in 20.2%, and immunosuppression in 38.8%. (schrezenmeier2020baselineclinicalcharacteristics pages 3-5)

**Allogeneic hematopoietic stem-cell transplantation** is the only established curative therapy but carries substantial treatment-related morbidity and mortality. It is generally reserved for severe marrow failure, clonal evolution/MDS, or selected refractory disease rather than uncomplicated complement-responsive hemolysis. Suggested MAXO: hematopoietic stem-cell transplantation. (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2)

No validated pharmacogenomic genotype currently selects among complement inhibitors. PIGA variant class itself does not determine drug choice.

### Pregnancy

Pregnancy raises hemolytic and thrombotic risk and requires specialist hematology–maternal-fetal care. A systematic review of 190 pregnancies found fetal survival of 82% with eculizumab versus 69% without it; miscarriage was twice as frequent without treatment, and preterm delivery occurred in 32% versus 44%. Evidence was predominantly observational/case-series level, so confounding remains. (manning2025paroxysmalnocturnalhaemoglobinuria pages 1-3)

## 13. Prevention

There is no primary prevention for the spontaneous somatic PIGA event. No population, newborn, carrier, or family screening program is appropriate.

Secondary prevention consists of timely flow-cytometric testing in high-risk clinical contexts, serial clone monitoring in aplastic anemia/MDS, and early treatment of active hemolysis or thrombosis. Tertiary prevention comprises complement inhibition, vaccination, infection education, thrombosis management, renal monitoring, perioperative planning, and management of pregnancy and inflammatory triggers. Genetic counseling should explain the acquired, non-heritable nature of classic PNH rather than offer familial predictive testing.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart of human clonal PNH was identified. PIGA and the GPI-anchor pathway are evolutionarily conserved, but classic PNH is not zoonotic and has no cross-species transmission. Mouse **Piga** and rhesus **PIGA** are the principal orthologous experimental targets; exact NCBI Gene and taxon identifiers should be validated directly before database ingestion.

## 15. Model organisms

Conditional/chimeric **Piga-knockout mice**, erythroid-specific knockout models, and CRISPR-edited rhesus macaques generate GPI-AP-deficient lineages. They reproduce shortened erythrocyte survival and increased complement sensitivity, making them useful for studying GPI biology, immune selection, and complement therapeutics. However, they generally fail to develop the sustained clone expansion, overt hemolysis, and thrombosis characteristic of human PNH. (colden2022insightsintothe pages 1-3, chen2021advancesinthe pages 1-3)

This limitation is mechanistically informative: the dedicated animal-model review concludes that “the PIG-A mutation is one of the several conditions required for PNH, but it alone is not enough to cause PNH.” Likewise, the 2022 review states that mutant cells “have no intrinsic growth advantage and do not clonally expand over time.” These are review-abstract quotations synthesizing mouse and nonhuman-primate evidence, not direct human clinical findings. (colden2022insightsintothe pages 1-3, chen2021advancesinthe pages 1-3)

Cellular systems include patient-derived CD59-negative blood/HSPC populations, engineered PIGA-null cell lines, and complement-sensitive erythroid assays. Their limitations include absence of marrow immune selection, whole-organism complement–coagulation interactions, and thrombosis. MGI, IMSR/MMRRC, NCBI Gene, and nonhuman-primate research repositories are appropriate model-resource starting points.

## Evidence limitations and authoritative interpretation

The strongest human evidence comprises flow-confirmed clinical cohorts, the International PNH Registry, randomized complement-inhibitor trials, and recent expert reviews. Exact phenotype frequencies vary with referral pattern, clone threshold, therapy exposure, and geographic access. The 2024 expert position is that terminal inhibitors dramatically improve survival, whereas proximal inhibitors improve residual anemia and quality of life; nevertheless, long-term comparative effectiveness and first-line selection require more real-world data. (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2)

Mechanistic statements about immune escape, secondary mutations, platelet/endothelial pathways, and animal models combine human observational, in-vitro, and model-organism evidence and should not all be assigned equal causal certainty. Robust PNH-specific spatial transcriptomic, single-cell atlas, epigenomic, lipidomic, or clinically validated multi-omic signatures remain unavailable in the retrieved evidence.

References

1. (panse2024paroxysmalnocturnalhemoglobinuria pages 1-2): Jens Peter Panse, Britta Höchsmann, and Jörg Schubert. Paroxysmal nocturnal hemoglobinuria, pathophysiology, diagnostics, and treatment. Transfusion Medicine and Hemotherapy, 51:310-320, Aug 2024. URL: https://doi.org/10.1159/000540474, doi:10.1159/000540474. This article has 14 citations and is from a peer-reviewed journal.

2. (versino2024complementinhibitionin pages 2-2): Francesco Versino and Bruno Fattizzo. Complement inhibition in paroxysmal nocturnal hemoglobinuria: from biology to therapy. International Journal of Laboratory Hematology, 46:43-54, Apr 2024. URL: https://doi.org/10.1111/ijlh.14281, doi:10.1111/ijlh.14281. This article has 33 citations and is from a peer-reviewed journal.

3. (colden2022insightsintothe pages 1-3): Melissa A. Colden, Sushant Kumar, Bolormaa Munkhbileg, and Daria V. Babushok. Insights into the emergence of paroxysmal nocturnal hemoglobinuria. Frontiers in Immunology, Jan 2022. URL: https://doi.org/10.3389/fimmu.2021.830172, doi:10.3389/fimmu.2021.830172. This article has 46 citations and is from a peer-reviewed journal.

4. (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 1-2): Elisavet Apostolidou, Vasileios Georgoulis, Dimitrios Leonardos, Eleni Kapsali, and Eleftheria Hatzimichael. Paroxysmal nocturnal hemoglobinuria: unraveling its molecular pathogenesis and advancing targeted therapeutic strategies. Diseases, Sep 2025. URL: https://doi.org/10.3390/diseases13090298, doi:10.3390/diseases13090298. This article has 4 citations.

5. (versino2024complementinhibitionin pages 1-2): Francesco Versino and Bruno Fattizzo. Complement inhibition in paroxysmal nocturnal hemoglobinuria: from biology to therapy. International Journal of Laboratory Hematology, 46:43-54, Apr 2024. URL: https://doi.org/10.1111/ijlh.14281, doi:10.1111/ijlh.14281. This article has 33 citations and is from a peer-reviewed journal.

6. (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 2-4): Elisavet Apostolidou, Vasileios Georgoulis, Dimitrios Leonardos, Eleni Kapsali, and Eleftheria Hatzimichael. Paroxysmal nocturnal hemoglobinuria: unraveling its molecular pathogenesis and advancing targeted therapeutic strategies. Diseases, Sep 2025. URL: https://doi.org/10.3390/diseases13090298, doi:10.3390/diseases13090298. This article has 4 citations.

7. (versino2024complementinhibitionin pages 2-3): Francesco Versino and Bruno Fattizzo. Complement inhibition in paroxysmal nocturnal hemoglobinuria: from biology to therapy. International Journal of Laboratory Hematology, 46:43-54, Apr 2024. URL: https://doi.org/10.1111/ijlh.14281, doi:10.1111/ijlh.14281. This article has 33 citations and is from a peer-reviewed journal.

8. (chen2021advancesinthe pages 1-3): Yingying Chen and Fu Rong. Advances in the creation of animal models of paroxysmal nocturnal hemoglobinuria. Hematology, 26:491-496, Jan 2021. URL: https://doi.org/10.1080/16078454.2021.1945244, doi:10.1080/16078454.2021.1945244. This article has 7 citations and is from a peer-reviewed journal.

9. (versino2024complementinhibitionin pages 3-4): Francesco Versino and Bruno Fattizzo. Complement inhibition in paroxysmal nocturnal hemoglobinuria: from biology to therapy. International Journal of Laboratory Hematology, 46:43-54, Apr 2024. URL: https://doi.org/10.1111/ijlh.14281, doi:10.1111/ijlh.14281. This article has 33 citations and is from a peer-reviewed journal.

10. (risitano2008paroxysmalnocturnalhemoglobinuria pages 3-4): A. Risitano and B. Rotoli. Paroxysmal nocturnal hemoglobinuria: pathophysiology, natural history and treatment options in the era of biological agents. Biologics : Targets & Therapy, 2:205-222, Jun 2008. URL: https://doi.org/10.2147/btt.s1420, doi:10.2147/btt.s1420. This article has 134 citations.

11. (hillmen2024navigatingthecomplement pages 7-9): Peter Hillmen, Regina Horneff, Michael Yeh, Martin Kolev, and Pascal Deschatelets. Navigating the complement pathway to optimize pnh treatment with pegcetacoplan and other currently approved complement inhibitors. International Journal of Molecular Sciences, 25:9477, Aug 2024. URL: https://doi.org/10.3390/ijms25179477, doi:10.3390/ijms25179477. This article has 21 citations.

12. (schrezenmeier2020baselineclinicalcharacteristics pages 1-2): Hubert Schrezenmeier, Alexander Röth, David J. Araten, Yuzuru Kanakura, Loree Larratt, Jamile M. Shammo, Amanda Wilson, Gilda Shayan, and Jaroslaw P. Maciejewski. Baseline clinical characteristics and disease burden in patients with paroxysmal nocturnal hemoglobinuria (pnh): updated analysis from the international pnh registry. Annals of Hematology, 99:1505-1514, May 2020. URL: https://doi.org/10.1007/s00277-020-04052-z, doi:10.1007/s00277-020-04052-z. This article has 197 citations and is from a peer-reviewed journal.

13. (schrezenmeier2020baselineclinicalcharacteristics pages 3-5): Hubert Schrezenmeier, Alexander Röth, David J. Araten, Yuzuru Kanakura, Loree Larratt, Jamile M. Shammo, Amanda Wilson, Gilda Shayan, and Jaroslaw P. Maciejewski. Baseline clinical characteristics and disease burden in patients with paroxysmal nocturnal hemoglobinuria (pnh): updated analysis from the international pnh registry. Annals of Hematology, 99:1505-1514, May 2020. URL: https://doi.org/10.1007/s00277-020-04052-z, doi:10.1007/s00277-020-04052-z. This article has 197 citations and is from a peer-reviewed journal.

14. (yu2024healthrelatedqualityof pages 1-2): Huaxin Yu, Shengnan Duan, Pei Wang, Rong Fu, Zixuan Lv, Yuchi Yu, Pu Miao, Junwei Shi, Niekun Zhuang, Huiying Hu, Ni Yuan, and Sijia Che. Health-related quality of life and influencing factors of patients with paroxysmal nocturnal hemoglobinuria in china. Orphanet Journal of Rare Diseases, May 2024. URL: https://doi.org/10.1186/s13023-024-03178-x, doi:10.1186/s13023-024-03178-x. This article has 4 citations and is from a peer-reviewed journal.

15. (almakadi2025clinicalcharacteristicsand pages 4-6): Mohammed Almakadi, Noura AlHashim, Murtadha Al-Khabori, Hazzaa Alzahrani, Hani Yousif Osman, Mervat Mattar, and Ahmed Sabah. Clinical characteristics and management of paroxysmal nocturnal hemoglobinuria in the middle east: a narrative review. Clinical and Experimental Medicine, Aug 2025. URL: https://doi.org/10.1007/s10238-025-01834-5, doi:10.1007/s10238-025-01834-5. This article has 0 citations and is from a peer-reviewed journal.

16. (latour2024oraliptacopanmonotherapy pages 1-4): Régis Peffault de Latour, Alexander Röth, Austin G. Kulasekararaj, Bing Han, Phillip Scheinberg, Jaroslaw P. Maciejewski, Yasutaka Ueda, Carlos M. de Castro, Eros Di Bona, Rong Fu, Li Zhang, Morag Griffin, Saskia M.C. Langemeijer, Jens Panse, Hubert Schrezenmeier, Wilma Barcellini, Vitor A.Q. Mauad, Philippe Schafhausen, Suzanne Tavitian, Eloise Beggiato, Lee Ping Chew, Anna Gaya, Wei-Han Huang, Jun Ho Jang, Toshio Kitawaki, Abdullah Kutlar, Rosario Notaro, Vinod Pullarkat, Jörg Schubert, Louis Terriou, Michihiro Uchiyama, Lily Wong Lee Lee, Eng-Soo Yap, Flore Sicre de Fontbrune, Luana Marano, Ferras Alashkar, Shreyans Gandhi, Roochi Trikha, Chen Yang, Hui Liu, Richard J. Kelly, Britta Höchsmann, Cécile Kerloeguen, Partha Banerjee, Rafael Levitch, Rakesh Kumar, Zhixin Wang, Christine Thorburn, Samopriyo Maitra, Shujie Li, Aurelie Verles, Marion Dahlke, and Antonio M. Risitano. Oral iptacopan monotherapy in paroxysmal nocturnal hemoglobinuria. New England Journal of Medicine, 390:994-1008, Mar 2024. URL: https://doi.org/10.1056/nejmoa2308695, doi:10.1056/nejmoa2308695. This article has 142 citations and is from a highest quality peer-reviewed journal.

17. (apostolidou2025paroxysmalnocturnalhemoglobinuria pages 6-8): Elisavet Apostolidou, Vasileios Georgoulis, Dimitrios Leonardos, Eleni Kapsali, and Eleftheria Hatzimichael. Paroxysmal nocturnal hemoglobinuria: unraveling its molecular pathogenesis and advancing targeted therapeutic strategies. Diseases, Sep 2025. URL: https://doi.org/10.3390/diseases13090298, doi:10.3390/diseases13090298. This article has 4 citations.

18. (perry2025theadvancinglandscape pages 3-4): Cameron Perry, Xinyu von Buttlar, and Swapna Thota. The advancing landscape of paroxysmal nocturnal hemoglobinuria treatment. Turkish Journal of Hematology, 42:74-81, Apr 2025. URL: https://doi.org/10.4274/tjh.galenos.2025.2025.0054, doi:10.4274/tjh.galenos.2025.2025.0054. This article has 2 citations.

19. (kelly2025pharmacologicaltherapiesin pages 1-2): Richard J. Kelly, Matthew Holt, and Jeff Szer. Pharmacological therapies in paroxysmal nocturnal haemoglobinuria: focus on complement inhibition. Drugs, 85:1413-1428, Sep 2025. URL: https://doi.org/10.1007/s40265-025-02235-4, doi:10.1007/s40265-025-02235-4. This article has 3 citations and is from a domain leading peer-reviewed journal.

20. (fattizzo2026thrombosisinparoxysmal pages 1-2): Bruno Fattizzo and Christoph Q. Schmidt. Thrombosis in paroxysmal nocturnal hemoglobinuria in the complement inhibitor era: mechanisms, risk stratification, and clinical management. International Journal of Hematology, Mar 2026. URL: https://doi.org/10.1007/s12185-026-04190-6, doi:10.1007/s12185-026-04190-6. This article has 1 citations and is from a peer-reviewed journal.

21. (manning2025paroxysmalnocturnalhaemoglobinuria pages 1-3): James E. Manning, Etienne Ciantar, Morag Griffin, and Richard J. Kelly. Paroxysmal nocturnal haemoglobinuria in pregnancy–a systematic review with meta analysis. Annals of Hematology, 104:2517-2525, Apr 2025. URL: https://doi.org/10.1007/s00277-025-06353-7, doi:10.1007/s00277-025-06353-7. This article has 7 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Paroxysmal_Nocturnal_Hemoglobinuria-deep-research-falcon_artifacts/artifact-00.md)