---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-30T17:16:24.180258'
end_time: '2026-07-30T17:27:23.334690'
duration_seconds: 659.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 131
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Immunodeficiency_131-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 131
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 131** covering all of the
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
- **Disease Name:** Immunodeficiency 131
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 131** covering all of the
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


# Immunodeficiency 131: comprehensive disease-characteristics report

## Executive summary and scope

**Immunodeficiency 131 (MONDO:0976229)** is an ultra-rare, Mendelian inborn error of immunity associated with heterozygous pathogenic variation in **IRF4**, encoding interferon regulatory factor 4. The strongest match to this numbered disease entity is the severe, infantile-onset disorder caused by recurrent **IRF4 c.284C>G (p.Thr95Arg; p.T95R)**, named **multimorphic IRF4 combined immunodeficiency (MICI)**. It was defined in seven affected individuals from six unrelated families in 2023. Open Targets lists IRF4 as the sole associated target for MONDO:0976229 and links the association to PMID **36662884** and subsequent IRF4 reports. (OpenTargets Search: Immunodeficiency 131, fornes2023amultimorphicmutation pages 2-4)

Two other IRF4 allelic disorders must be distinguished from core p.T95R disease:

1. **IRF4 p.Phe359Leu (F359L)** causes a dominant antibody/combined immunodeficiency with childhood hypogammaglobulinemia, defective plasma-cell differentiation, abnormal T-cell subsets, and pigmentation changes; PMID **36917008**.
2. **IRF4 p.Arg98Trp (R98W) haploinsufficiency** confers age-dependent, incompletely penetrant susceptibility to *Tropheryma whipplei* and Whipple disease; PMID **29537367**. (OpenTargets Search: Immunodeficiency 131, thouenon2023aneomorphicmutation pages 1-2, constantine2020recentadvancesin pages 3-4)

Because only seven p.T95R patients were reported in the defining cohort, percentages should not be interpreted as population estimates. Most evidence is aggregated disease-level evidence from research cohorts, pedigrees, and experimental assays—not individual EHR data.

| Domain | Evidence-based finding | Suggested ontology annotations | Best source/date |
|---|---|---|---|
| Identity / identifier | **Immunodeficiency 131** is linked to **IRF4** and represented in Open Targets as **MONDO:0976229**. The best-supported core phenotype for this entry is the 2023 **autosomal dominant combined immunodeficiency caused by recurrent IRF4 p.T95R**, termed **multimorphic IRF4 CID (MICI)**. Distinct **allelic IRF4 disorders** include **F359L dominant primary immunodeficiency/antibody deficiency** and **R98W haploinsufficiency with Whipple disease susceptibility**, which should not be conflated with MICI. (OpenTargets Search: Immunodeficiency 131, fornes2023amultimorphicmutation pages 9-10, fornes2023amultimorphicmutation pages 26-29) | MONDO:0976229; gene: **IRF4**; suggested disease label: combined immunodeficiency | Open Targets disease-target evidence (accessed via tool context; MONDO association) and Fornes et al., *Sci Immunol*, Jan 2023 (OpenTargets Search: Immunodeficiency 131, fornes2023amultimorphicmutation pages 9-10) |
| Causal variant and inheritance | **Core MICI:** recurrent heterozygous **IRF4 c.284C>G (p.T95R)** in the DNA-binding domain; **autosomal dominant**, apparently **fully penetrant** in reported cases; mostly **de novo**, with one mosaic mother reported. Variant absent from control databases in the cited summaries. **Allelic disorders:** **F359L (c.1075T>C)** in the interferon activation domain causes dominant antibody/CID phenotype; **R98W** causes **haploinsufficiency** predisposing to Whipple disease with **incomplete penetrance**. (fornes2023amultimorphicmutation pages 2-4, fornes2023amultimorphicmutation pages 9-10, thouenon2023aneomorphicmutation pages 14-15, constantine2020recentadvancesin pages 3-4) | SO: missense_variant; HP: Autosomal dominant inheritance; gene region suggestion: DNA-binding domain / interferon activation domain | Fornes et al., *Sci Immunol*, Jan 2023; Thouenon et al., *J Exp Med*, Mar 2023; Constantine & Lionakis review, Apr 2020 (fornes2023amultimorphicmutation pages 2-4, thouenon2023aneomorphicmutation pages 14-15, constantine2020recentadvancesin pages 3-4) |
| Cohort and onset | **Core MICI:** **7 patients from 6 unrelated families**, with **very early onset**, often **<1 year**. One detailed proband presented at **11 months** with respiratory failure/infections. **F359L:** **3 patients across 2 generations**; childhood-onset hypogammaglobulinemia, index case symptomatic by **6 months** and diagnosed by **11 months**. **R98W Whipple susceptibility:** kindred data summarized as **4 Whipple disease patients** among **12 heterozygous carriers**; adult onset around **mean 55–58 years**. (fornes2023amultimorphicmutation pages 2-4, jia2023functionalandbiochemical pages 39-44, thouenon2023aneomorphicmutation pages 2-4, constantine2020recentadvancesin pages 3-4) | HP: Infantile onset; HP: Adult onset; HP: Recurrent infections | Fornes et al., Jan 2023; Thouenon et al., Mar 2023; review summarizing Guérin et al., Apr 2020 (fornes2023amultimorphicmutation pages 2-4, thouenon2023aneomorphicmutation pages 2-4, constantine2020recentadvancesin pages 3-4) |
| Infections | **Core MICI:** profound susceptibility to **opportunistic infections**, especially **Pneumocystis jirovecii pneumonia**, severe viral infections (**CMV**, **EBV**), weakly pathogenic mycobacteria including **BCG / Mycobacterium bovis**, recurrent sinopulmonary infection, and chronic diarrhea. **F359L:** recurrent ENT and other infections including **meningococcal infection**, **Giardia lamblia**, **CMV**, **disseminated varicella zoster virus**, fungal infections, **Bartonella henselae**, conjunctivitis, molluscum contagiosum, and onychomycosis/cutaneous fungal disease. **R98W:** predisposition is specifically linked to **Tropheryma whipplei / Whipple disease** and chronic carriage. (fornes2023amultimorphicmutation pages 2-4, jia2023functionalandbiochemical pages 39-44, thouenon2023aneomorphicmutation pages 4-5, constantine2020recentadvancesin pages 3-4) | NCBITaxon: *Pneumocystis jirovecii*, CMV, EBV, *Mycobacterium bovis*, *Giardia lamblia*, *Tropheryma whipplei*; HP: Opportunistic infections; HP: Recurrent respiratory infections | Fornes et al., Jan 2023; Jia thesis summary, Jan 2023; Thouenon et al., Mar 2023; Constantine & Lionakis, Apr 2020 (fornes2023amultimorphicmutation pages 2-4, jia2023functionalandbiochemical pages 39-44, thouenon2023aneomorphicmutation pages 4-5, constantine2020recentadvancesin pages 3-4) |
| Immune phenotype | **Core MICI:** **agammaglobulinemia** or near-complete antibody deficiency with markedly reduced **IgG/IgA/IgM**, reduced **CD19+ B cells**, increased **naïve B cells**, reduced **class-switched memory B cells**, decreased **plasmablasts/plasma cells**, reduced **T\_H17** and **T\_FH** cells, decreased cytokine production, and in one detailed case undetectable vaccine antibodies to tetanus/diphtheria. **F359L:** panhypogammaglobulinemia, very low plasmablast/plasma cell counts, low naïve **CD4/CD8** T cells and increased terminal effector T cells, plus hair/skin pigmentation abnormalities and premature hair graying. **R98W:** in vitro loss of DNA binding/transcription with impaired helper pathways summarized, but classic broad agammaglobulinemia phenotype not emphasized in the cited review summary. (fornes2023amultimorphicmutation pages 2-4, fornes2023amultimorphicmutation pages 9-10, jia2023functionalandbiochemical pages 39-44, thouenon2023aneomorphicmutation pages 14-15, thouenon2023aneomorphicmutation pages 1-2) | HP: Agammaglobulinemia; HP: Hypogammaglobulinemia; HP: Decreased class-switched memory B cells; HP: Decreased plasmablasts; CL: B cell, plasma cell, CD4-positive T cell, T follicular helper cell, T helper 17 cell | Fornes et al., Jan 2023; Jia thesis summary, Jan 2023; Thouenon et al., Mar 2023 (fornes2023amultimorphicmutation pages 2-4, jia2023functionalandbiochemical pages 39-44, thouenon2023aneomorphicmutation pages 14-15) |
| Mechanism | **Core MICI p.T95R:** a **multimorphic** mechanism combining **hypermorph** (higher DNA-binding affinity), **hypomorph** (reduced transcription on canonical IRF4 targets), and **neomorph** (binding to noncanonical DNA sites and altered gene-expression programs). Patient/experimental systems showed altered B-cell maturation, plasma-cell differentiation failure, and reduced T-cell effector programs. **F359L:** **neomorphic / dominant-negative** behavior centered on the interferon activation domain, with selective failure of **ISRE** promoter activation but retained **EICE/AICE** activity; impaired **BLIMP1/XBP1** induction and plasma-cell differentiation. **R98W:** **loss-of-function haploinsufficiency** with defective DNA binding/transcription and incomplete penetrance for Whipple disease. (fornes2023amultimorphicmutation pages 1-2, fornes2023amultimorphicmutation pages 10-12, thouenon2023aneomorphicmutation pages 14-15, thouenon2023aneomorphicmutation pages 1-2, constantine2020recentadvancesin pages 3-4) | GO: DNA-binding transcription factor activity; GO: plasma cell differentiation; GO: immunoglobulin production; GO: T-helper 17 cell differentiation; GO: germinal center formation | Fornes et al., Jan 2023; Thouenon et al., Mar 2023; review summary, Apr 2020 (fornes2023amultimorphicmutation pages 1-2, fornes2023amultimorphicmutation pages 10-12, thouenon2023aneomorphicmutation pages 14-15, constantine2020recentadvancesin pages 3-4) |
| Diagnosis | Evidence supports diagnosis by **genetic testing** identifying heterozygous **IRF4** variants in affected patients, alongside immunophenotyping showing antibody deficiency and B/T-cell abnormalities. In MICI, the paper used extensive **flow cytometry/CyTOF**, **scRNA-seq**, functional lymphocyte assays, and mechanistic assays including **EMSA, HT-SELEX, luciferase, ChIP-seq, surface plasmon resonance**, and single-molecule imaging. In a detailed p.T95R case, immunoglobulins were undetectable (**IgG <0.3 g/L, IgA <0.04 g/L, IgM <0.03 g/L**) with absent tetanus/diphtheria antibodies and 95.2% naïve CD19+ B cells. Standardized disease-specific clinical criteria were **not reported** in the cited evidence. (fornes2023amultimorphicmutation pages 10-12, jia2023functionalandbiochemical pages 39-44) | MAXO suggestion: genetic testing; HP: Abnormality of humoral immunity; LOINC-style concepts: serum immunoglobulin measurement | Fornes et al., Jan 2023; Jia thesis summary, Jan 2023 (fornes2023amultimorphicmutation pages 10-12, jia2023functionalandbiochemical pages 39-44) |
| Treatment | **No disease-specific targeted therapy or interventional trial was identified.** Reported real-world care is supportive and anti-infective. **Core MICI:** detailed p.T95R proband received **IVIG** and **trimethoprim/sulfamethoxazole prophylaxis**; CMV was treated with **ganciclovir**, then **foscarnet** after antiviral resistance (**UL54 L545S, UL97 M460I**) as bridge to **HSCT**. Outcome after HSCT for this proband was not stated in the extracted evidence. **F359L:** patients required **immunoglobulin replacement therapy**. A previously reported separate homozygous IRF4 splice case (not MICI 131 core) died **2 days post-HSCT** at age 2. (jia2023functionalandbiochemical pages 39-44, thouenon2023aneomorphicmutation pages 2-4, thouenon2023aneomorphicmutation pages 4-5) | MAXO: immunoglobulin replacement therapy; antimicrobial prophylaxis; antiviral therapy; hematopoietic stem cell transplantation | Jia thesis summary, Jan 2023; Thouenon et al., Mar 2023 (jia2023functionalandbiochemical pages 39-44, thouenon2023aneomorphicmutation pages 2-4, thouenon2023aneomorphicmutation pages 4-5) |
| Model organism | **Core MICI** has direct model support: a **heterozygous Irf4 T95R knock-in mouse** recapitulated key human features, especially **severe defects in antibody production** at baseline and after immunization and reduced antigen-specific germinal-center responses. No disease-specific natural veterinary condition was identified in the searched evidence. (fornes2023amultimorphicmutation pages 1-2, fornes2023amultimorphicmutation pages 10-12) | NCBITaxon: 10090; CL: germinal center B cell, plasma cell; GO: antibody production | Fornes et al., *Sci Immunol*, Jan 2023 (fornes2023amultimorphicmutation pages 1-2, fornes2023amultimorphicmutation pages 10-12) |
| Evidence gaps | Missing or not clearly reported in the extracted evidence: OMIM number for “Immunodeficiency 131,” prevalence/incidence, sex ratio, long-term survival, formal quality-of-life data, penetrance estimates for **F359L**, variant-specific carrier frequency, established screening guidelines, prenatal/preimplantation counseling studies, environmental/lifestyle risk modifiers beyond pathogen exposure, protective factors, epigenetic biomarkers, and disease-specific clinical trials. Whipple observational studies exist but are **not** genotype-specific therapeutic trials. (jia2023functionalandbiochemical pages 39-44, OpenTargets Search: Immunodeficiency 131) | Suggested annotation: evidence gap / not reported | Evidence synthesis across extracted sources and trial search contexts (jia2023functionalandbiochemical pages 39-44, OpenTargets Search: Immunodeficiency 131) |


*Table: This table summarizes the best-supported evidence for Immunodeficiency 131 as an IRF4-associated disorder, centering on p.T95R multimorphic IRF4 CID while distinguishing the allelic F359L and R98W phenotypes. It also flags where the literature remains sparse or non-specific.*

## 1. Disease information

### Definition

Immunodeficiency 131/MICI is an **autosomal dominant combined immunodeficiency** in which altered IRF4 DNA recognition disrupts both humoral and cellular adaptive immunity. Hallmarks are infantile opportunistic infections, agammaglobulinemia, failed B-cell maturation and plasma-cell differentiation, reduced T-helper 17 and follicular-helper T-cell populations, and impaired cytokine production. (fornes2023amultimorphicmutation pages 2-4, fornes2023amultimorphicmutation pages 1-2)

### Identifiers and names

- **MONDO:** MONDO:0976229, “immunodeficiency 131.”
- **Causal gene:** **IRF4**, Ensembl ENSG00000137265; official name “interferon regulatory factor 4.”
- **Principal synonyms:** multimorphic IRF4 combined immunodeficiency; **MICI**; IRF4 p.T95R-associated autosomal dominant combined immunodeficiency.
- **Related but non-equivalent names:** IRF4 deficiency; IRF4-associated primary immunodeficiency; IRF4 haploinsufficiency; IRF4-associated Whipple-disease susceptibility.
- **OMIM:** a disease-specific OMIM accession for “Immunodeficiency 131” was not securely established in the retrieved evidence and should not be inferred. The retrieved thesis identifies IRF4 itself as OMIM **601900** only indirectly; this should be verified directly in OMIM before database deposition.
- **Orphanet, MeSH, ICD-10/ICD-11:** no dedicated disease-specific codes were identified. Broader coding would generally fall under combined or other specified immunodeficiency, but assigning a specific ICD code without direct coding-authority confirmation is not recommended. (OpenTargets Search: Immunodeficiency 131)

### Key primary sources

- Fornes et al., **January 2023**, *Science Immunology*, DOI: https://doi.org/10.1126/sciimmunol.ade7953, PMID **36662884**.
- Thouenon et al., **March 2023**, *Journal of Experimental Medicine*, DOI: https://doi.org/10.1084/jem.20221292, PMID **36917008**.
- Guérin et al., **2018**, IRF4 haploinsufficiency/Whipple disease, PMID **29537367**. (OpenTargets Search: Immunodeficiency 131, thouenon2023aneomorphicmutation pages 2-4, fornes2023amultimorphicmutation pages 2-4)

A direct quotation from the Fornes et al. abstract captures the principal finding: **“We report a recurrent heterozygous mutation in IRF4, p.T95R, causing an autosomal dominant combined immunodeficiency (CID) in seven patients from six unrelated families.”** The abstract further states that patients had profound opportunistic-infection susceptibility and agammaglobulinemia. (fornes2023amultimorphicmutation pages 1-2)

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factor

The primary cause is a **germline heterozygous IRF4 p.T95R missense variant** in the DNA-binding domain. It is not a conventional simple loss-of-function allele: it simultaneously increases affinity for some DNA, decreases transcription at canonical IRF4 targets, and creates binding to noncanonical sites. This mixed hypermorphic, hypomorphic, and neomorphic behavior explains the term “multimorphic.” (fornes2023amultimorphicmutation pages 9-10, fornes2023amultimorphicmutation pages 1-2)

### Genetic risk

- Carrying p.T95R is the principal known risk factor.
- Most affected individuals had a **de novo** variant; one family had low-level maternal mosaicism, reported as 4 variant reads among 124 reads.
- The variant was absent from referenced control-population databases and was reclassified from VUS to **likely pathogenic** using ACMG evidence PS2, PM2, PP1, PP3, and PP4 in the supporting analysis.
- No established modifier gene, polygenic risk score, founder allele, anticipation, or protective IRF4 allele has been reported. (fornes2023amultimorphicmutation pages 2-4, jia2023functionalandbiochemical pages 57-63)

### Environmental and infectious interaction

Pathogens do not cause the inherited defect but expose its functional consequences. In p.T95R disease, clinically important exposures include *Pneumocystis jirovecii*, CMV, EBV, environmental or vaccine-strain mycobacteria, and common respiratory organisms. In the distinct R98W disorder, exposure to *T. whipplei* is necessary but insufficient: among 12 heterozygotes summarized in the literature, four developed Whipple disease, five were chronic carriers, and others did not show disease, illustrating incomplete penetrance and a strong gene–pathogen interaction. (constantine2020recentadvancesin pages 3-4, fornes2023amultimorphicmutation pages 2-4)

No evidence supports toxins, smoking, alcohol, diet, exercise, occupational exposure, radiation, sex, or age as causal modifiers of MICI. No genetic or lifestyle protective factors are established.

## 3. Phenotypes

### Core p.T95R MICI phenotype

| Phenotype | Type and characteristics | Suggested HPO annotation |
|---|---|---|
| Opportunistic/recurrent infection | Clinical sign; severe, infantile onset, chronic/recurrent; observed across the seven-person defining cohort | Opportunistic infection; Recurrent respiratory infections |
| *P. jirovecii* pneumonia | Infection/respiratory manifestation; prominent presenting infection | Pneumocystis jirovecii pneumonia |
| Agammaglobulinemia | Laboratory abnormality; profound; early onset | **HP:0004432 Agammaglobulinemia** |
| Reduced IgG, IgA, and IgM | Laboratory abnormality; severe | Hypogammaglobulinemia |
| Reduced class-switched memory B cells | Laboratory abnormality | Decreased class-switched memory B-cell count |
| Reduced plasmablasts/plasma cells | Laboratory/cellular abnormality | Decreased circulating plasmablasts |
| Reduced TH17 and TFH populations | Laboratory/cellular abnormality | Abnormal T-cell subset distribution |
| Impaired cytokine production | Functional laboratory abnormality | Abnormal cytokine secretion |
| Chronic diarrhea | Symptom; infectious or immune-related; variable | **HP:0002014 Diarrhea** |
| Recurrent sinopulmonary disease | Clinical sign; early and recurrent | Recurrent upper/lower respiratory infection |

The defining seven patients had profound susceptibility to opportunistic organisms, notably *P. jirovecii*, severe CMV/EBV infection, weakly pathogenic mycobacteria, recurrent sinopulmonary infection, and chronic diarrhea. Their B cells showed impaired maturation, decreased isotype switching, and defective plasma-cell differentiation; T cells had reduced TH17 and TFH compartments and impaired cytokine output. (fornes2023amultimorphicmutation pages 2-4, fornes2023amultimorphicmutation pages 9-10)

One 11-month-old boy had respiratory failure with rhinovirus/enterovirus, *P. jirovecii*, CMV viremia, and ventilator-associated *Escherichia coli* pneumonia. His IgG was **<0.3 g/L**, IgA **<0.04 g/L**, and IgM **<0.03 g/L**; tetanus and diphtheria antibodies were undetectable, and **95.2% of CD19-positive cells were naïve B cells**. (jia2023functionalandbiochemical pages 39-44)

### F359L allelic phenotype

Three patients across two generations had childhood panhypogammaglobulinemia, extremely low plasmablast/plasma-cell counts, reduced naïve CD4/CD8 T cells, increased terminal-effector T cells, recurrent bacterial, viral, parasitic, and fungal infections, premature hair graying, and skin depigmentation. The index patient developed diarrhea and nasopharyngitis at six months and was diagnosed at 11 months. Reported infections included meningococcal disease, *Giardia lamblia*, CMV, disseminated varicella-zoster virus, *Bartonella henselae*, molluscum contagiosum, and cutaneous fungal disease. (thouenon2023aneomorphicmutation pages 2-4, thouenon2023aneomorphicmutation pages 4-5)

### Frequency and quality of life

For p.T95R, severe antibody deficiency and opportunistic-infection susceptibility appear highly consistent in the seven reported patients, but disease-wide percentages cannot be estimated. Formal EQ-5D, SF-36, PROMIS, disability, behavioral, or neuropsychiatric evaluations have not been reported. Nonetheless, recurrent hospitalization, respiratory failure, prolonged antiviral treatment, dependence on immunoglobulin replacement, and possible HSCT imply major effects on childhood functioning and caregiver burden. This last statement is a clinical inference, not a measured quality-of-life result.

## 4. Genetic and molecular information

### Gene

- **Symbol:** IRF4
- **Protein:** interferon regulatory factor 4, a lymphocyte-enriched DNA-binding transcription factor.
- **Primary cellular roles:** B-cell activation and terminal plasma-cell differentiation; immunoglobulin class switching; CD4 T-cell differentiation, including TH17 and TFH programs; cytokine transcription.

### Pathogenic variants and allelic heterogeneity

| Variant | Domain | Inheritance/mechanism | Clinical association |
|---|---|---|---|
| **NM-dependent c.284C>G, p.Thr95Arg (T95R)** | DNA-binding domain | Germline heterozygous AD; multimorphic hypermorph/hypomorph/neomorph | Core MICI/Immunodeficiency 131 |
| **c.1075T>C, p.Phe359Leu (F359L)** | Interferon activation domain | Germline heterozygous AD; neomorphic/dominant-negative on ISRE activity | Antibody/CID with pigmentation abnormalities |
| **p.Arg98Trp (R98W)** | DNA-binding domain | Germline heterozygous haploinsufficiency/LOF; incompletely penetrant | Whipple-disease susceptibility |
| Homozygous splice-disrupting allele | Splicing | Germline biallelic; presumed severe loss of function | Severe infantile CID; limited functional evidence |

For p.T95R, normal total IRF4 mRNA and protein levels show that disease results from **qualitative transcription-factor dysfunction**, not reduced abundance. No somatic origin was reported in affected individuals, although low-level parental germline/somatic mosaicism can permit recurrence. No pathogenic chromosomal rearrangement, copy-number abnormality, repeat expansion, mitochondrial variant, or epigenetic signature is established. (fornes2023amultimorphicmutation pages 2-4, fornes2023amultimorphicmutation pages 26-29)

### Population frequency and classification

The p.T95R allele was absent from control databases in the reported analysis and met likely-pathogenic ACMG criteria. A precise gnomAD allele count/frequency was not supplied in the retrieved evidence; therefore, “absent/ultra-rare in referenced controls” is safer than assigning a numerical frequency. (fornes2023amultimorphicmutation pages 2-4, jia2023functionalandbiochemical pages 57-63)

## 5. Environmental information

No environmental toxin, pollutant, radiation source, dietary exposure, smoking behavior, alcohol use, or occupational factor is known to cause or materially alter MICI. Infectious agents are **clinical triggers**, not etiologic causes. Relevant organisms include *P. jirovecii*, CMV, EBV, BCG/*M. bovis*, common respiratory viruses and bacteria, and—in the R98W allelic disorder—*T. whipplei*. No zoonotic transmission peculiar to IRF4 disease is known. (constantine2020recentadvancesin pages 3-4, fornes2023amultimorphicmutation pages 2-4)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic event:** heterozygous p.T95R changes a conserved residue in the IRF4 DNA-binding domain.
2. **Biophysical alteration:** mutant IRF4 has increased DNA-binding affinity but altered sequence specificity, losing effective regulation at some canonical interferon-stimulated response elements and acquiring noncanonical binding, including GATA-like motifs.
3. **Transcriptional rewiring:** canonical IRF4 gene activation is reduced while an abnormal set of genes is induced.
4. **B-cell consequences:** impaired maturation, class-switch recombination, memory-B-cell development, and terminal plasma-cell differentiation.
5. **T-cell consequences:** reduced TFH and TH17 cells and impaired effector-cytokine production.
6. **System-level consequence:** profound antibody deficiency plus cellular immune dysfunction.
7. **Clinical consequence:** early opportunistic, bacterial, viral, fungal, and mycobacterial infection. (fornes2023amultimorphicmutation pages 9-10, fornes2023amultimorphicmutation pages 1-2, fornes2023amultimorphicmutation pages 10-12)

A direct abstract quotation states: **“The IRF4T95R variant maps to the TF’s DNA binding domain, alters its canonical DNA binding specificities, and results in a simultaneous multimorphic combination of loss, gain, and new functions for IRF4.”** (fornes2023amultimorphicmutation pages 1-2)

### Experimental profiling

The defining study used conventional flow cytometry, CyTOF, single-cell RNA sequencing, in-vitro B- and T-cell differentiation, surface-plasmon resonance, electrophoretic mobility-shift assays, high-throughput SELEX, luciferase reporters, ChIP-seq, single-molecule fluorescence microscopy, and computational motif modeling. These convergent methods establish altered DNA affinity/specificity and downstream immune-cell dysfunction. No validated patient metabolomic, lipidomic, spatial-transcriptomic, proteomic biomarker, or diagnostic epigenetic signature has been reported. (fornes2023amultimorphicmutation pages 10-12)

### Suggested ontology terms

- **GO biological process:** B-cell differentiation; plasma-cell differentiation; immunoglobulin production; isotype switching; germinal-center formation; T-helper 17-cell differentiation; T-follicular-helper-cell differentiation; regulation of cytokine production.
- **GO molecular function:** sequence-specific DNA-binding transcription-factor activity; transcription cis-regulatory-region binding.
- **Cell Ontology:** B cell; naïve B cell; class-switched memory B cell; germinal-center B cell; plasmablast; plasma cell; CD4-positive T cell; TH17 cell; TFH cell.
- **GO cellular component:** nucleus; chromatin; transcription-regulator complex.

These are suggested mappings and should be checked against current ontology releases before production use.

## 7. Anatomical structures affected

The disease is fundamentally hematopoietic/immune rather than a fixed structural malformation.

- **Primary organs/tissues:** blood and lymphoid system; bone marrow-derived B- and T-cell lineages; secondary lymphoid tissues where germinal-center and plasma-cell differentiation occur.
- **Secondary clinical sites:** lungs and respiratory tract through recurrent pneumonia; gastrointestinal tract through chronic diarrhea and opportunistic infection; disseminated involvement during CMV, VZV, mycobacterial, or fungal infection.
- **F359L-specific nonimmune tissues:** hair follicle/melanocyte-associated pigmentation and skin depigmentation.
- **Lateralization:** not applicable.

Suggested UBERON annotations include blood, bone marrow, lymph node, spleen, respiratory tract/lung, and intestine. Suggested cellular annotations are germinal-center B cell, plasmablast, plasma cell, CD4 T cell, TH17 cell, and TFH cell. (thouenon2023aneomorphicmutation pages 2-4, fornes2023amultimorphicmutation pages 2-4)

## 8. Temporal development

### Onset and course

Core p.T95R disease is congenital at the genetic level and usually manifests clinically during **infancy, often before one year**. It is chronic and lifelong unless immune function is corrected by successful hematopoietic transplantation. Infection severity may fluctuate with pathogen exposure and treatment, but antibody and lymphocyte-differentiation defects are persistent. (fornes2023amultimorphicmutation pages 2-4, jia2023functionalandbiochemical pages 39-44)

A practical stage description, not a validated staging system, is:

1. **Preclinical/congenital:** pathogenic variant present; no established newborn-screening marker.
2. **Early clinical:** recurrent respiratory infection, diarrhea, thrush, or opportunistic pneumonia.
3. **Established CID:** agammaglobulinemia, abnormal B/T subsets, recurrent or disseminated infection.
4. **Advanced/complicated:** respiratory failure, chronic viral viremia, antimicrobial resistance, organ damage, or need for HSCT.

There are no validated remission criteria or longitudinal natural-history estimates. In contrast, R98W-associated Whipple disease is an adult-onset, exposure-dependent phenotype, with mean onset reported around 55–58 years. (constantine2020recentadvancesin pages 3-4, jia2023functionalandbiochemical pages 39-44)

## 9. Inheritance and population

### Inheritance

- **Pattern:** autosomal dominant for p.T95R MICI.
- **Penetrance:** described as fully penetrant among reported p.T95R carriers, but the sample is too small for a population estimate.
- **Origin:** predominantly de novo; one mosaic mother demonstrates recurrence risk from parental mosaicism.
- **Expressivity:** severe but clinically variable with respect to infecting organisms and complications.
- **Anticipation:** not reported.
- **Consanguinity/founder effect:** not relevant to the recurrent mostly de novo p.T95R cohort; no founder effect established.
- **Carrier frequency:** unknown and expected to be extremely low.
- **Sex ratio:** not estimable.

### Epidemiology

Only **seven p.T95R patients from six unrelated families** were included in the defining international cohort. No population prevalence, incidence, geographic concentration, ethnic enrichment, sex ratio, or age-distribution estimate exists. Accordingly, the condition should be classified as ultra-rare without assigning cases per 100,000. (fornes2023amultimorphicmutation pages 2-4, fornes2023amultimorphicmutation pages 9-10)

## 10. Diagnostics

### When to suspect MICI

Consider IRF4-associated MICI in an infant with:

- *P. jirovecii* pneumonia or another opportunistic infection;
- agammaglobulinemia despite the presence of circulating B cells;
- markedly naïve-skewed B cells with reduced switched-memory cells and plasmablasts;
- reduced TFH/TH17 cells or impaired T-cell cytokine production;
- CMV/EBV, disseminated viral disease, BCG complication, or weakly pathogenic mycobacterial disease.

### Recommended work-up

1. CBC with differential and lymphocyte count.
2. Serum IgG, IgA, IgM, and IgE.
3. Vaccine-specific antibodies, interpreted before or with awareness of immunoglobulin replacement.
4. Flow cytometry: CD3/CD4/CD8/CD19/NK cells; naïve/memory T cells; naïve, unswitched-memory, switched-memory B cells; plasmablasts.
5. Microbiological testing guided by presentation: *Pneumocystis* PCR/staining, CMV/EBV viral loads, bacterial/fungal cultures, and mycobacterial studies.
6. Molecular testing: an inborn-error-of-immunity panel containing **IRF4**, or trio WES/WGS when panel testing is negative.
7. Confirm by Sanger or orthogonal sequencing and test parents with sufficiently deep sequencing to detect mosaicism. (jia2023functionalandbiochemical pages 39-44, fornes2023amultimorphicmutation pages 10-12)

### Genetic-testing modalities

- **Panel/WES/WGS:** appropriate and preferred.
- **Single-gene IRF4 sequencing:** appropriate where phenotype is strongly suggestive or for familial confirmation.
- **RNA sequencing:** potentially useful for splice variants, but not required for p.T95R.
- **CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing:** not first-line unless another diagnosis is suspected.

### Differential diagnosis

Important alternatives include X-linked SCID and other combined immunodeficiencies; CD40L/CD40 deficiency; ICOS/ICOSL deficiency; IL21/IL21R defects; NFKB1/NFKB2 disorders; activated PI3K-delta syndrome; CVID; congenital HIV or secondary immunodeficiency; and other transcription-factor IEIs. The combination of circulating but developmentally arrested B cells, near-absent immunoglobulin, opportunistic infection, abnormal helper-T-cell compartments, and an IRF4 p.T95R variant is distinguishing.

### Screening

No population or newborn screening program exists. T-cell receptor excision-circle screening might detect some severe T-cell abnormalities but has not been validated for MICI and could miss affected infants. **Cascade testing** is indicated after molecular diagnosis, including sensitive testing for parental mosaicism. Prenatal and preimplantation testing are technically possible once a familial pathogenic variant is established.

## 11. Outcome and prognosis

No five- or ten-year survival rate, life expectancy, mortality rate, formal disability score, or validated prognostic model is available. Prognosis is plausibly driven by age at diagnosis, infection burden, pulmonary injury, persistent CMV/EBV, antimicrobial resistance, depth of antibody/T-cell dysfunction, access to immunoglobulin replacement, and transplant eligibility, but these have not been statistically validated.

Documented morbidity includes respiratory failure, opportunistic pneumonia, chronic viral infection, diarrhea, repeated antimicrobial exposure, and dependence on immunoglobulin replacement. In one p.T95R patient, CMV acquired **UL54 L545S** and **UL97 M460I** resistance variants, requiring foscarnet. A separate homozygous IRF4 splice-deficiency patient—not the core p.T95R entity—died two days after HSCT at age two, illustrating potential severity but not establishing MICI transplant mortality. (jia2023functionalandbiochemical pages 39-44)

## 12. Treatment and current applications

### Supportive and anti-infective management

There is no approved IRF4-directed drug, gene therapy, RNA therapy, or genome-editing treatment. Current management is extrapolated from combined-immunodeficiency care and reported cases:

- **Immunoglobulin replacement** by IVIG or SCIG for profound antibody deficiency.
- **Trimethoprim–sulfamethoxazole prophylaxis** against *P. jirovecii*.
- Prompt pathogen-directed antibacterial, antiviral, antifungal, or antimycobacterial treatment.
- CMV/EBV viral-load surveillance where clinically indicated.
- Avoidance of live vaccines until specialist immunologic assessment.
- Consideration of **allogeneic HSCT** for severe disease, persistent opportunistic infection, or progressive combined immune dysfunction. (thouenon2023aneomorphicmutation pages 2-4, jia2023functionalandbiochemical pages 39-44)

The detailed p.T95R proband received IVIG and trimethoprim–sulfamethoxazole. Ganciclovir was used for CMV, but resistance prompted foscarnet as a bridge to HSCT. The retrieved evidence does not provide a disease-wide response rate or definitive post-HSCT outcome. (jia2023functionalandbiochemical pages 39-44)

### Suggested MAXO annotations

- Immunoglobulin replacement therapy.
- Antimicrobial prophylaxis.
- Antiviral therapy.
- Hematopoietic stem-cell transplantation.
- Flow-cytometric immunophenotyping.
- Molecular genetic testing.
- Pathogen-load monitoring.

### Trials and experimental therapies

No IRF4/MICI-specific interventional clinical trial was identified. ClinicalTrials.gov searches found two completed observational Whipple-disease studies—NCT06776484, enrollment 20, and NCT03350685, enrollment 267—but these are not IRF4-genotype-specific treatment studies. Open Targets identifies IRF4 as the disease target but provides no approved or clinical-stage MICI-targeted drug. (OpenTargets Search: Immunodeficiency 131)

Direct IRF4 augmentation or inhibition would be biologically complex: p.T95R has simultaneous gain, loss, and neomorphic functions, so nonspecific IRF4 activation or suppression could worsen some transcriptional abnormalities. HSCT currently offers the most plausible mechanism-based cellular correction, but evidence remains case-level.

## 13. Prevention

### Primary prevention

The de novo germline disorder cannot generally be prevented through lifestyle modification. For a known familial variant, genetic counseling should explain autosomal-dominant transmission, possible parental mosaicism, and reproductive options including prenatal or preimplantation genetic testing.

### Secondary prevention

- Early genetic testing after sentinel opportunistic infection or profound hypogammaglobulinemia.
- Cascade testing in relatives.
- Early initiation of immunoglobulin replacement and *Pneumocystis* prophylaxis.
- Regular infection and viral-load surveillance tailored to prior pathogens.

### Tertiary prevention

- Prevent recurrent infection and chronic lung injury with replacement immunoglobulin and prophylaxis.
- Avoid live attenuated vaccines unless an immunology specialist determines safety.
- Use household and close-contact vaccination with attention to vaccines capable of shedding.
- Monitor antimicrobial toxicity and resistance.
- Evaluate HSCT before irreversible infection-related organ damage.

No MICI-specific public-health program, behavioral intervention, or environmental remediation strategy exists.

## 14. Other species and natural disease

No naturally occurring IRF4 p.T95R-equivalent immunodeficiency has been established in companion animals, livestock, or wildlife. Therefore, no breed association, veterinary prevalence, zoonotic potential, or cross-species transmission applies. The implicated pathogens are acquired conventionally; the genetic disorder itself is not transmissible.

The orthologous mouse gene is **Irf4** in *Mus musculus* (NCBI Taxonomy **10090**). IRF4’s lymphocyte-regulatory role is evolutionarily conserved, supporting mouse modeling, but an experimentally engineered model should not be described as natural animal disease.

## 15. Model organisms and experimental systems

### Knock-in mouse

A heterozygous **Irf4 T95R knock-in mouse** is the most disease-specific model. It reproduced severe antibody-production defects at baseline and after immunization and showed impaired antigen-specific germinal-center responses, closely matching the human B-cell phenotype. This provides unusually strong in-vivo support for pathogenicity and mechanism. (fornes2023amultimorphicmutation pages 9-10, fornes2023amultimorphicmutation pages 1-2)

A direct abstract quotation states: **“A knock-in mouse model of heterozygous T95R showed a severe defect in antibody production both at the steady state and after immunization with different types of antigens, consistent with the CID observed in these patients.”** (fornes2023amultimorphicmutation pages 1-2)

### Cellular models

Patient B and T cells, transduced lymphoid lines, and reporter systems were used to study differentiation, cytokine production, DNA binding, and promoter activity. These models demonstrated reduced canonical transcription, novel sequence recognition, impaired plasma-cell differentiation, and altered T-cell programs. (fornes2023amultimorphicmutation pages 10-12, jia2023functionalandbiochemical pages 28-34)

### Limitations

The mouse reproduces antibody defects but cannot fully model the human pathogen spectrum, long-term clinical course, or all species-specific transcriptional targets. Cell lines permit mechanistic dissection but do not reproduce multicellular germinal-center architecture or infection physiology.

## Recent developments and expert interpretation

The decisive advances occurred in **2023**, when two independent studies showed that different IRF4-domain variants produce mechanistically distinct dominant immunodeficiencies: p.T95R rewires DNA recognition through a multimorphic mechanism, whereas F359L selectively disrupts ISRE-dependent transcription and plasma-cell differentiation. This establishes IRF4 disease as an **allelic and mechanistic spectrum**, not a single uniform haploinsufficiency syndrome. (thouenon2023aneomorphicmutation pages 14-15, fornes2023amultimorphicmutation pages 1-2)

Research published in 2024 further reinforced IRF4’s central role in plasma-cell identity and immune-cell transcription, but it did not add a comparably sized MICI clinical cohort or a disease-specific treatment trial. Consequently, the 2023 primary reports remain the authoritative sources for Immunodeficiency 131.

## Knowledge gaps and curation cautions

The following remain unavailable or inadequately established: exact prevalence/incidence, sex ratio, population-specific carrier frequency, long-term survival, formal quality-of-life outcomes, standardized diagnostic criteria, validated newborn screening, disease-specific prognostic biomarkers, treatment-response rates, transplant outcomes, natural veterinary disease, protective factors, epigenetic signatures, and targeted clinical trials.

For knowledge-base curation, **p.T95R MICI should be the core representation of Immunodeficiency 131**, while F359L disease and R98W-associated Whipple susceptibility should be retained as distinct IRF4 allelic phenotypes. Assertions based on p.T95R should not automatically be transferred to all IRF4 variants.

References

1. (OpenTargets Search: Immunodeficiency 131): Open Targets Query (Immunodeficiency 131, 21 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (fornes2023amultimorphicmutation pages 2-4): Oriol Fornes, Alicia Jia, Hye Sun Kuehn, Qing Min, Ulrich Pannicke, Nikolai Schleussner, Romane Thouenon, Zhijia Yu, María de los Angeles Astbury, Catherine M. Biggs, Miguel Galicchio, Jorge Alberto Garcia-Campos, Silvina Gismondi, Guadalupe Gonzalez Villarreal, Kyla J. Hildebrand, Manfred Hönig, Jia Hou, Despina Moshous, Stefania Pittaluga, Xiaowen Qian, Jacob Rozmus, Ansgar S. Schulz, Aidé Tamara Staines-Boone, Bijun Sun, Jinqiao Sun, Schauer Uwe, Edna Venegas-Montoya, Wenjie Wang, Xiaochuan Wang, Wenjing Ying, Xiaowen Zhai, Qinhua Zhou, Altuna Akalin, Isabelle André, Thomas F. E. Barth, Bernd Baumann, Anne Brüstle, Gaetan Burgio, Jacinta C. Bustamante, Jean-Laurent Casanova, Marco G. Casarotto, Marina Cavazzana, Loïc Chentout, Ian A. Cockburn, Mariantonia Costanza, Chaoqun Cui, Oliver Daumke, Kate L. Del Bel, Hermann Eibel, Xiaoqian Feng, Vedran Franke, J. Christof M. Gebhardt, Andrea Götz, Stephan Grunwald, Bénédicte Hoareau, Timothy R. Hughes, Eva-Maria Jacobsen, Martin Janz, Arttu Jolma, Chantal Lagresle-Peyrou, Nannan Lai, Yaxuan Li, Susan Lin, Henry Y. Lu, Saul O. Lugo-Reyes, Xin Meng, Peter Möller, Nidia Moreno-Corona, Julie E. Niemela, Gherman Novakovsky, Jareb J. Perez-Caraballo, Capucine Picard, Lucie Poggi, Maria-Emilia Puig-Lombardi, Katrina L. Randall, Anja Reisser, Yohann Schmitt, Sandali Seneviratne, Mehul Sharma, Jennifer Stoddard, Srinivasan Sundararaj, Harry Sutton, Linh Q. Tran, Ying Wang, Wyeth W. Wasserman, Zichao Wen, Wiebke Winkler, Ermeng Xiong, Ally W. H. Yang, Meiping Yu, Lumin Zhang, Hai Zhang, Qian Zhao, Xin Zhen, Anselm Enders, Sven Kracker, Ruben Martinez-Barricarte, Stephan Mathas, Sergio D. Rosenzweig, Klaus Schwarz, Stuart E. Turvey, and Ji-Yang Wang. A multimorphic mutation in irf4 causes human autosomal dominant combined immunodeficiency. Science Immunology, Jan 2023. URL: https://doi.org/10.1126/sciimmunol.ade7953, doi:10.1126/sciimmunol.ade7953. This article has 44 citations and is from a highest quality peer-reviewed journal.

3. (thouenon2023aneomorphicmutation pages 1-2): Romane Thouenon, Loïc Chentout, Nidia Moreno-Corona, Lucie Poggi, Emilia Puig Lombardi, Benedicte Hoareau, Yohann Schmitt, Chantal Lagresle-Peyrou, Jacinta Bustamante, Isabelle André, Marina Cavazzana, Anne Durandy, Jean-Laurent Casanova, Lionel Galicier, Jehane Fadlallah, Alain Fischer, and Sven Kracker. A neomorphic mutation in the interferon activation domain of irf4 causes a dominant primary immunodeficiency. The Journal of Experimental Medicine, Mar 2023. URL: https://doi.org/10.1084/jem.20221292, doi:10.1084/jem.20221292. This article has 19 citations.

4. (constantine2020recentadvancesin pages 3-4): Gregory M. Constantine and Michail S. Lionakis. Recent advances in understanding inherited deficiencies in immunity to infections. F1000Research, 9:243, Apr 2020. URL: https://doi.org/10.12688/f1000research.22036.1, doi:10.12688/f1000research.22036.1. This article has 4 citations and is from a peer-reviewed journal.

5. (fornes2023amultimorphicmutation pages 9-10): Oriol Fornes, Alicia Jia, Hye Sun Kuehn, Qing Min, Ulrich Pannicke, Nikolai Schleussner, Romane Thouenon, Zhijia Yu, María de los Angeles Astbury, Catherine M. Biggs, Miguel Galicchio, Jorge Alberto Garcia-Campos, Silvina Gismondi, Guadalupe Gonzalez Villarreal, Kyla J. Hildebrand, Manfred Hönig, Jia Hou, Despina Moshous, Stefania Pittaluga, Xiaowen Qian, Jacob Rozmus, Ansgar S. Schulz, Aidé Tamara Staines-Boone, Bijun Sun, Jinqiao Sun, Schauer Uwe, Edna Venegas-Montoya, Wenjie Wang, Xiaochuan Wang, Wenjing Ying, Xiaowen Zhai, Qinhua Zhou, Altuna Akalin, Isabelle André, Thomas F. E. Barth, Bernd Baumann, Anne Brüstle, Gaetan Burgio, Jacinta C. Bustamante, Jean-Laurent Casanova, Marco G. Casarotto, Marina Cavazzana, Loïc Chentout, Ian A. Cockburn, Mariantonia Costanza, Chaoqun Cui, Oliver Daumke, Kate L. Del Bel, Hermann Eibel, Xiaoqian Feng, Vedran Franke, J. Christof M. Gebhardt, Andrea Götz, Stephan Grunwald, Bénédicte Hoareau, Timothy R. Hughes, Eva-Maria Jacobsen, Martin Janz, Arttu Jolma, Chantal Lagresle-Peyrou, Nannan Lai, Yaxuan Li, Susan Lin, Henry Y. Lu, Saul O. Lugo-Reyes, Xin Meng, Peter Möller, Nidia Moreno-Corona, Julie E. Niemela, Gherman Novakovsky, Jareb J. Perez-Caraballo, Capucine Picard, Lucie Poggi, Maria-Emilia Puig-Lombardi, Katrina L. Randall, Anja Reisser, Yohann Schmitt, Sandali Seneviratne, Mehul Sharma, Jennifer Stoddard, Srinivasan Sundararaj, Harry Sutton, Linh Q. Tran, Ying Wang, Wyeth W. Wasserman, Zichao Wen, Wiebke Winkler, Ermeng Xiong, Ally W. H. Yang, Meiping Yu, Lumin Zhang, Hai Zhang, Qian Zhao, Xin Zhen, Anselm Enders, Sven Kracker, Ruben Martinez-Barricarte, Stephan Mathas, Sergio D. Rosenzweig, Klaus Schwarz, Stuart E. Turvey, and Ji-Yang Wang. A multimorphic mutation in irf4 causes human autosomal dominant combined immunodeficiency. Science Immunology, Jan 2023. URL: https://doi.org/10.1126/sciimmunol.ade7953, doi:10.1126/sciimmunol.ade7953. This article has 44 citations and is from a highest quality peer-reviewed journal.

6. (fornes2023amultimorphicmutation pages 26-29): Oriol Fornes, Alicia Jia, Hye Sun Kuehn, Qing Min, Ulrich Pannicke, Nikolai Schleussner, Romane Thouenon, Zhijia Yu, María de los Angeles Astbury, Catherine M. Biggs, Miguel Galicchio, Jorge Alberto Garcia-Campos, Silvina Gismondi, Guadalupe Gonzalez Villarreal, Kyla J. Hildebrand, Manfred Hönig, Jia Hou, Despina Moshous, Stefania Pittaluga, Xiaowen Qian, Jacob Rozmus, Ansgar S. Schulz, Aidé Tamara Staines-Boone, Bijun Sun, Jinqiao Sun, Schauer Uwe, Edna Venegas-Montoya, Wenjie Wang, Xiaochuan Wang, Wenjing Ying, Xiaowen Zhai, Qinhua Zhou, Altuna Akalin, Isabelle André, Thomas F. E. Barth, Bernd Baumann, Anne Brüstle, Gaetan Burgio, Jacinta C. Bustamante, Jean-Laurent Casanova, Marco G. Casarotto, Marina Cavazzana, Loïc Chentout, Ian A. Cockburn, Mariantonia Costanza, Chaoqun Cui, Oliver Daumke, Kate L. Del Bel, Hermann Eibel, Xiaoqian Feng, Vedran Franke, J. Christof M. Gebhardt, Andrea Götz, Stephan Grunwald, Bénédicte Hoareau, Timothy R. Hughes, Eva-Maria Jacobsen, Martin Janz, Arttu Jolma, Chantal Lagresle-Peyrou, Nannan Lai, Yaxuan Li, Susan Lin, Henry Y. Lu, Saul O. Lugo-Reyes, Xin Meng, Peter Möller, Nidia Moreno-Corona, Julie E. Niemela, Gherman Novakovsky, Jareb J. Perez-Caraballo, Capucine Picard, Lucie Poggi, Maria-Emilia Puig-Lombardi, Katrina L. Randall, Anja Reisser, Yohann Schmitt, Sandali Seneviratne, Mehul Sharma, Jennifer Stoddard, Srinivasan Sundararaj, Harry Sutton, Linh Q. Tran, Ying Wang, Wyeth W. Wasserman, Zichao Wen, Wiebke Winkler, Ermeng Xiong, Ally W. H. Yang, Meiping Yu, Lumin Zhang, Hai Zhang, Qian Zhao, Xin Zhen, Anselm Enders, Sven Kracker, Ruben Martinez-Barricarte, Stephan Mathas, Sergio D. Rosenzweig, Klaus Schwarz, Stuart E. Turvey, and Ji-Yang Wang. A multimorphic mutation in irf4 causes human autosomal dominant combined immunodeficiency. Science Immunology, Jan 2023. URL: https://doi.org/10.1126/sciimmunol.ade7953, doi:10.1126/sciimmunol.ade7953. This article has 44 citations and is from a highest quality peer-reviewed journal.

7. (thouenon2023aneomorphicmutation pages 14-15): Romane Thouenon, Loïc Chentout, Nidia Moreno-Corona, Lucie Poggi, Emilia Puig Lombardi, Benedicte Hoareau, Yohann Schmitt, Chantal Lagresle-Peyrou, Jacinta Bustamante, Isabelle André, Marina Cavazzana, Anne Durandy, Jean-Laurent Casanova, Lionel Galicier, Jehane Fadlallah, Alain Fischer, and Sven Kracker. A neomorphic mutation in the interferon activation domain of irf4 causes a dominant primary immunodeficiency. The Journal of Experimental Medicine, Mar 2023. URL: https://doi.org/10.1084/jem.20221292, doi:10.1084/jem.20221292. This article has 19 citations.

8. (jia2023functionalandbiochemical pages 39-44): Alicia Jia. Functional and biochemical characterization of novel genetic variants in irak4 and irf4 causing human inborn errors of immunity. Text, Jan 2023. URL: https://doi.org/10.14288/1.0402477, doi:10.14288/1.0402477. This article has 0 citations and is from a peer-reviewed journal.

9. (thouenon2023aneomorphicmutation pages 2-4): Romane Thouenon, Loïc Chentout, Nidia Moreno-Corona, Lucie Poggi, Emilia Puig Lombardi, Benedicte Hoareau, Yohann Schmitt, Chantal Lagresle-Peyrou, Jacinta Bustamante, Isabelle André, Marina Cavazzana, Anne Durandy, Jean-Laurent Casanova, Lionel Galicier, Jehane Fadlallah, Alain Fischer, and Sven Kracker. A neomorphic mutation in the interferon activation domain of irf4 causes a dominant primary immunodeficiency. The Journal of Experimental Medicine, Mar 2023. URL: https://doi.org/10.1084/jem.20221292, doi:10.1084/jem.20221292. This article has 19 citations.

10. (thouenon2023aneomorphicmutation pages 4-5): Romane Thouenon, Loïc Chentout, Nidia Moreno-Corona, Lucie Poggi, Emilia Puig Lombardi, Benedicte Hoareau, Yohann Schmitt, Chantal Lagresle-Peyrou, Jacinta Bustamante, Isabelle André, Marina Cavazzana, Anne Durandy, Jean-Laurent Casanova, Lionel Galicier, Jehane Fadlallah, Alain Fischer, and Sven Kracker. A neomorphic mutation in the interferon activation domain of irf4 causes a dominant primary immunodeficiency. The Journal of Experimental Medicine, Mar 2023. URL: https://doi.org/10.1084/jem.20221292, doi:10.1084/jem.20221292. This article has 19 citations.

11. (fornes2023amultimorphicmutation pages 1-2): Oriol Fornes, Alicia Jia, Hye Sun Kuehn, Qing Min, Ulrich Pannicke, Nikolai Schleussner, Romane Thouenon, Zhijia Yu, María de los Angeles Astbury, Catherine M. Biggs, Miguel Galicchio, Jorge Alberto Garcia-Campos, Silvina Gismondi, Guadalupe Gonzalez Villarreal, Kyla J. Hildebrand, Manfred Hönig, Jia Hou, Despina Moshous, Stefania Pittaluga, Xiaowen Qian, Jacob Rozmus, Ansgar S. Schulz, Aidé Tamara Staines-Boone, Bijun Sun, Jinqiao Sun, Schauer Uwe, Edna Venegas-Montoya, Wenjie Wang, Xiaochuan Wang, Wenjing Ying, Xiaowen Zhai, Qinhua Zhou, Altuna Akalin, Isabelle André, Thomas F. E. Barth, Bernd Baumann, Anne Brüstle, Gaetan Burgio, Jacinta C. Bustamante, Jean-Laurent Casanova, Marco G. Casarotto, Marina Cavazzana, Loïc Chentout, Ian A. Cockburn, Mariantonia Costanza, Chaoqun Cui, Oliver Daumke, Kate L. Del Bel, Hermann Eibel, Xiaoqian Feng, Vedran Franke, J. Christof M. Gebhardt, Andrea Götz, Stephan Grunwald, Bénédicte Hoareau, Timothy R. Hughes, Eva-Maria Jacobsen, Martin Janz, Arttu Jolma, Chantal Lagresle-Peyrou, Nannan Lai, Yaxuan Li, Susan Lin, Henry Y. Lu, Saul O. Lugo-Reyes, Xin Meng, Peter Möller, Nidia Moreno-Corona, Julie E. Niemela, Gherman Novakovsky, Jareb J. Perez-Caraballo, Capucine Picard, Lucie Poggi, Maria-Emilia Puig-Lombardi, Katrina L. Randall, Anja Reisser, Yohann Schmitt, Sandali Seneviratne, Mehul Sharma, Jennifer Stoddard, Srinivasan Sundararaj, Harry Sutton, Linh Q. Tran, Ying Wang, Wyeth W. Wasserman, Zichao Wen, Wiebke Winkler, Ermeng Xiong, Ally W. H. Yang, Meiping Yu, Lumin Zhang, Hai Zhang, Qian Zhao, Xin Zhen, Anselm Enders, Sven Kracker, Ruben Martinez-Barricarte, Stephan Mathas, Sergio D. Rosenzweig, Klaus Schwarz, Stuart E. Turvey, and Ji-Yang Wang. A multimorphic mutation in irf4 causes human autosomal dominant combined immunodeficiency. Science Immunology, Jan 2023. URL: https://doi.org/10.1126/sciimmunol.ade7953, doi:10.1126/sciimmunol.ade7953. This article has 44 citations and is from a highest quality peer-reviewed journal.

12. (fornes2023amultimorphicmutation pages 10-12): Oriol Fornes, Alicia Jia, Hye Sun Kuehn, Qing Min, Ulrich Pannicke, Nikolai Schleussner, Romane Thouenon, Zhijia Yu, María de los Angeles Astbury, Catherine M. Biggs, Miguel Galicchio, Jorge Alberto Garcia-Campos, Silvina Gismondi, Guadalupe Gonzalez Villarreal, Kyla J. Hildebrand, Manfred Hönig, Jia Hou, Despina Moshous, Stefania Pittaluga, Xiaowen Qian, Jacob Rozmus, Ansgar S. Schulz, Aidé Tamara Staines-Boone, Bijun Sun, Jinqiao Sun, Schauer Uwe, Edna Venegas-Montoya, Wenjie Wang, Xiaochuan Wang, Wenjing Ying, Xiaowen Zhai, Qinhua Zhou, Altuna Akalin, Isabelle André, Thomas F. E. Barth, Bernd Baumann, Anne Brüstle, Gaetan Burgio, Jacinta C. Bustamante, Jean-Laurent Casanova, Marco G. Casarotto, Marina Cavazzana, Loïc Chentout, Ian A. Cockburn, Mariantonia Costanza, Chaoqun Cui, Oliver Daumke, Kate L. Del Bel, Hermann Eibel, Xiaoqian Feng, Vedran Franke, J. Christof M. Gebhardt, Andrea Götz, Stephan Grunwald, Bénédicte Hoareau, Timothy R. Hughes, Eva-Maria Jacobsen, Martin Janz, Arttu Jolma, Chantal Lagresle-Peyrou, Nannan Lai, Yaxuan Li, Susan Lin, Henry Y. Lu, Saul O. Lugo-Reyes, Xin Meng, Peter Möller, Nidia Moreno-Corona, Julie E. Niemela, Gherman Novakovsky, Jareb J. Perez-Caraballo, Capucine Picard, Lucie Poggi, Maria-Emilia Puig-Lombardi, Katrina L. Randall, Anja Reisser, Yohann Schmitt, Sandali Seneviratne, Mehul Sharma, Jennifer Stoddard, Srinivasan Sundararaj, Harry Sutton, Linh Q. Tran, Ying Wang, Wyeth W. Wasserman, Zichao Wen, Wiebke Winkler, Ermeng Xiong, Ally W. H. Yang, Meiping Yu, Lumin Zhang, Hai Zhang, Qian Zhao, Xin Zhen, Anselm Enders, Sven Kracker, Ruben Martinez-Barricarte, Stephan Mathas, Sergio D. Rosenzweig, Klaus Schwarz, Stuart E. Turvey, and Ji-Yang Wang. A multimorphic mutation in irf4 causes human autosomal dominant combined immunodeficiency. Science Immunology, Jan 2023. URL: https://doi.org/10.1126/sciimmunol.ade7953, doi:10.1126/sciimmunol.ade7953. This article has 44 citations and is from a highest quality peer-reviewed journal.

13. (jia2023functionalandbiochemical pages 57-63): Alicia Jia. Functional and biochemical characterization of novel genetic variants in irak4 and irf4 causing human inborn errors of immunity. Text, Jan 2023. URL: https://doi.org/10.14288/1.0402477, doi:10.14288/1.0402477. This article has 0 citations and is from a peer-reviewed journal.

14. (jia2023functionalandbiochemical pages 28-34): Alicia Jia. Functional and biochemical characterization of novel genetic variants in irak4 and irf4 causing human inborn errors of immunity. Text, Jan 2023. URL: https://doi.org/10.14288/1.0402477, doi:10.14288/1.0402477. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Immunodeficiency_131-deep-research-falcon_artifacts/artifact-00.md)