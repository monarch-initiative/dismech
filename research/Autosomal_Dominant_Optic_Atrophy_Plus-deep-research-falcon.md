---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-22T10:55:28.107014'
end_time: '2026-06-22T11:10:18.663044'
duration_seconds: 890.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Optic Atrophy Plus
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Optic_Atrophy_Plus-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Optic Atrophy Plus
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Optic Atrophy Plus** covering all of the
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
- **Disease Name:** Autosomal Dominant Optic Atrophy Plus
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Optic Atrophy Plus** covering all of the
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


# Comprehensive Research Report: Autosomal Dominant Optic Atrophy Plus (DOA Plus)

## Target Disease
- **Disease Name:** Autosomal Dominant Optic Atrophy Plus (DOA Plus, ADOA Plus, Syndromic DOA)
- **OMIM ID:** 165500 (DOA), 125250 (DOA Plus)
- **Category:** Mendelian inherited optic neuropathy

| Category | Key details | Evidence |
|---|---|---|
| Disease name / core definition | **Autosomal Dominant Optic Atrophy Plus (DOA plus, ADOA plus)** is the syndromic/multisystem form of OPA1-related dominant optic atrophy, characterized by progressive retinal ganglion cell and optic nerve degeneration with extra-ocular manifestations. Reviews describe DOA as **OMIM 165500** and DOA plus as **OMIM 125250**. Synonyms/related names include **dominant optic atrophy**, **autosomal dominant optic atrophy**, **Kjer type optic atrophy/Kjer syndrome**, and **syndromic DOA / ADOA plus**. | (wong2023opa1dominantoptic pages 1-3, zanfardino2024opa1mutationaffects pages 1-2, sampige2025ittakestwo pages 1-2) |
| Disease identifiers / classification | OMIM identifiers explicitly reported in the evidence: **DOA = 165500**; **ADOA plus = 125250**. The disease is a **Mendelian inherited optic neuropathy** and part of the broader hereditary optic neuropathy group. No MONDO, Orphanet, ICD-10/11, or MeSH identifier was directly available in the retrieved evidence set. | (wong2023opa1dominantoptic pages 1-3, zanfardino2024opa1mutationaffects pages 1-2, zeppieri2025isolatedandsyndromic pages 1-2, lee2024hereditaryopticneuropathies pages 1-2) |
| Primary causal gene | **OPA1** (chromosome **3q28–q29/3q29**) is the major disease gene; multiple reviews report that **60–90%** of autosomal dominant optic atrophy cases are due to OPA1 variants, with one review citing **70–90%** and another **60–80%**. OPA1 encodes a mitochondrial dynamin-like GTPase in the inner mitochondrial membrane involved in mitochondrial fusion, cristae structure, oxidative phosphorylation support, mtDNA maintenance, mitophagy, and apoptosis regulation. | (wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2, amore2021therapeuticoptionsin pages 1-2) |
| Molecular mechanism of DOA plus vs isolated DOA | DOA plus is enriched for **missense variants in the dynamin/GTPase domain** that are thought to act via **dominant-negative effects**, whereas many truncating/deletion/splice variants act through **haploinsufficiency**. A 2025 mechanistic study contrasted **c.1034G>A** with **c.1305+2delGT**, showing the missense variant caused >**60%** mitochondrial fragmentation with greater ROS, cytochrome c release, and apoptosis, versus ~**20%** fragmentation for the splice/deletion model. | (nitta2024drosophilamodelto pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2, zanfardino2024opa1mutationaffects pages 1-2) |
| Representative pathogenic / likely pathogenic variants reported in evidence | Examples include **c.2708_2711delTTAG (OPA1delTTAG)**, described as a common recurrent pathogenic deletion; **R445H** (classic DOA-plus-associated missense variant); **c.1034G>A (p.Arg345Gln)**; **c.1305+2delGT**; **~69.86 kb deletion** encompassing OPA1; **V465F** and **V560F**; pediatric cohort variant **c.1406_1407del (p.Thr469LysfsTer16)** newly reported in 2023; fibroblast study variant **p.His42Tyr** in an ADOA plus patient. Variant classes include missense, frameshift deletion, splice-site, and larger copy-number deletion. | (nitta2024drosophilamodelto pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2, zhang2025opa1mutationsin pages 1-2, arruti2023opa1dominantoptic pages 1-2, zanfardino2024opa1mutationaffects pages 1-2) |
| Inheritance / penetrance / expressivity | Inheritance is **autosomal dominant**. Penetrance is **incomplete** but high; one study cited in a 2025 paper estimated **88% lifetime penetrance** for OPA1 mutation carriers. Expressivity is **markedly variable**, both interfamilial and intrafamilial, ranging from asymptomatic or isolated optic atrophy to severe multisystem disease. | (yao2025contrastingpathophysiologicalmechanisms pages 1-2, wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2, strachan2021theroleof pages 1-2) |
| Frequency of DOA plus among OPA1 carriers | Multisystem involvement occurs in about **20%** of OPA1 mutation carriers/patients with DOA according to multiple recent reviews and model papers. One 2021 review cites approximately **25%** with extra-ocular symptoms. | (wong2023opa1dominantoptic pages 1-3, nitta2024drosophilamodelto pages 1-2, strachan2021theroleof pages 1-2) |
| Typical ocular phenotype | Core ocular phenotype includes **bilateral, insidious, progressive visual loss**, usually beginning in childhood; **dyschromatopsia/color vision defects**; **central or centrocecal scotoma**; **temporal optic disc pallor**; **RNFL thinning**, especially in the papillomacular bundle; and **ganglion cell layer thinning** on OCT. | (wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2, lee2024hereditaryopticneuropathies pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2) |
| Age of onset / clinical course | Typical onset is in the **first or second decade of life**, often **early childhood**, with slow progression. Pediatric data: in 11 children with confirmed OPA1 mutations, mean baseline visual acuity was **0.40 logMAR (right eye)** and **0.44 logMAR (left eye)** and remained largely unchanged over follow-up. Some reviews note onset can vary from birth to adulthood in broader ADOA. | (arruti2023opa1dominantoptic pages 1-2, wong2023opa1dominantoptic pages 1-3, sampige2025ittakestwo pages 1-2) |
| Key extra-ocular phenotypes in DOA plus | Frequently reported extra-ocular manifestations include **sensorineural hearing loss/deafness**, **peripheral neuropathy**, **myopathy**, **ataxia**, **spastic paraplegia**, **chronic progressive external ophthalmoplegia (CPEO)**, **multiple sclerosis-like illness**, **parkinsonism**, **dementia**, and less commonly **cardiomyopathy**. | (wong2023opa1dominantoptic pages 1-3, nitta2024drosophilamodelto pages 1-2, strachan2021theroleof pages 1-2, affortit2024thehumanopa1delttag pages 1-2) |
| Hearing-loss phenotype | Hearing loss is the best-established extra-ocular feature and is often **auditory neuropathy spectrum disorder (ANSD)**. In the 2024 mouse study, deafness was described as affecting **about 20% of all DOA plus** cases/patients in background discussion. In a 2026 hearing-loss cohort of **18,475** Japanese patients, **10 individuals from 8 families** carried OPA1 variants; hearing loss was typically **post-lingual**, **progressive**, and **mild-to-moderate**, with missense variants tending toward **DOA-plus phenotypes and ANSD**. | (affortit2024thehumanopa1delttag pages 1-2, kawakita2026frequencyandhearing pages 1-2) |
| Quantitative ophthalmic findings from pediatric OPA1 cohort | In 11 pediatric patients: mean first-visit **RNFL thickness 81.6 µm (right), 80.5 µm (left)**; mean **ganglion cell layer 52.5 µm (right), 52.4 µm (left)**; mean **central macular thickness 229.5 µm (right), 233.5 µm (left)**; **9/11** had bilateral temporal disc pallor; the most common visual field defect was **centrocecal scotoma**. | (arruti2023opa1dominantoptic pages 1-2) |
| Diagnostic workup | Diagnosis is based on **neuro-ophthalmic examination** plus **OCT**, **visual field testing**, and **electrophysiology** (e.g., VEP; for hearing, **ABR/ASSR** with preserved **DPOAEs** in ANSD). Molecular confirmation uses **targeted gene panels**, **whole-exome sequencing**, or **sequence/CNV analysis** of OPA1. Family history is often present but not universal. | (arruti2023opa1dominantoptic pages 1-2, zeppieri2025isolatedandsyndromic pages 1-2, lee2024hereditaryopticneuropathies pages 1-2, kawakita2026frequencyandhearing pages 1-2, zhang2025opa1mutationsin pages 1-2) |
| Diagnostic genetics examples from evidence | Pediatric sequencing identified **7 different OPA1 mutations in 11 children**; **8/11** had a positive family history. Research studies used **WES**, targeted sequencing, and Sanger validation; large deletions/CNVs were also detected, showing the need for methods that capture both SNVs/indels and structural variants. | (arruti2023opa1dominantoptic pages 1-2, zhang2025opa1mutationsin pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2) |
| Pathophysiology summary | OPA1 dysfunction disrupts **mitochondrial inner membrane fusion**, **cristae architecture**, **OXPHOS/bioenergetics**, **mtDNA maintenance**, and **quality control/mitophagy**. Downstream effects include **mitochondrial fragmentation**, **membrane-potential loss**, **ROS increase**, **cytochrome c release**, **apoptosis**, and in some models **impaired autophagic flux** and **premature senescence**. | (wong2023opa1dominantoptic pages 1-3, zanfardino2024opa1mutationaffects pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2, zhang2025opa1mutationsin pages 1-2, dotto2021dominantopticatrophy pages 1-2) |
| Recent mechanistic developments (2023–2024 priority) | Recent studies expanded disease modeling and mechanisms: **patient-derived iPSC lines** from two DOA patients were generated in 2023 for RGC modeling; a **Drosophila model** in 2024 distinguished **loss-of-function** from **dominant-negative** OPA1 variants; a 2024 fibroblast study linked ADOA plus to **reduced autophagy and premature senescence**; a 2024 mouse model showed adult-onset progressive **auditory neuropathy** with **>40% reduction in Opa1 mRNA**, age-related **mtDNA depletion**, oxidative stress, mitophagy, and impaired autophagic flux. | (zanfardino2024opa1mutationaffects pages 1-2, nitta2024drosophilamodelto pages 1-2, affortit2024thehumanopa1delttag pages 1-2) |
| Biomarker / translational findings | In chronic hereditary optic neuropathy, serum studies reported elevated **sNfL** and **GFAP** in ADOA and LHON, supporting ongoing neurodegeneration; OCT showed ganglion cell/RNFL loss. These biomarkers are promising but not yet established as disease-specific clinical diagnostics for DOA plus. | (rufa2025serumneuronalglial pages 1-8) |
| Current management | Present management remains largely **supportive**: low-vision rehabilitation/visual aids, genetic counseling, ophthalmic surveillance, and management of syndromic complications such as hearing rehabilitation. For OPA1-related hearing loss/ANSD, hearing aids may provide limited benefit; in one 2026 cohort, **5 patients** had limited hearing-aid benefit and **1 cochlear implant** recipient achieved good speech perception. | (lee2024hereditaryopticneuropathies pages 1-2, kawakita2026frequencyandhearing pages 1-2) |
| Pharmacologic therapy under investigation | There is **no approved disease-specific therapy** for DOA/DOA plus. **Idebenone** has preliminary/off-label evidence in OPA1-related DOA; reviews note a “possible beneficial effect” but evidence remains limited and not definitive. Experimental small molecules include **paromomycin**, which rescued mitochondrial fragmentation from **c.1034G>A** in vitro in 2025 proof-of-concept work. | (amore2021therapeuticoptionsin pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2, sampige2025ittakestwo pages 1-2) |
| Advanced / pipeline therapeutics | Investigational strategies include **antisense oligonucleotide TANGO/STK-002** to augment wild-type OPA1 output, **gene replacement**, **CRISPR/gene editing**, mitochondrial-targeted antioxidants/peptides, **NAD+ boosters/metabolic support**, and **mitophagy/fission-fusion modulators**. These are early-stage and not standard of care. | (sampige2025ittakestwo pages 1-2, wong2023opa1dominantoptic pages 1-3) |
| Prognosis / burden | Visual prognosis is often poor and lifelong; one review notes **half of all DOA patients fail driving standards and are registered legally blind**. DOA plus adds morbidity through hearing impairment and neurological/muscular complications, contributing to reduced quality of life. | (wong2023opa1dominantoptic pages 1-3) |


*Table: This table summarizes the main clinical, genetic, mechanistic, diagnostic, and treatment features of Autosomal Dominant Optic Atrophy Plus using the retrieved evidence. It is useful as a compact reference for disease knowledge base curation and report drafting.*

## 1. Disease Information

### Overview
Autosomal Dominant Optic Atrophy Plus (DOA Plus) is the syndromic/multisystem form of OPA1-related dominant optic atrophy, characterized by progressive retinal ganglion cell and optic nerve degeneration with extra-ocular manifestations (wong2023opa1dominantoptic pages 1-3). DOA Plus represents approximately 20% of all OPA1 mutation carriers, extending beyond isolated optic atrophy to include multisystem involvement (wong2023opa1dominantoptic pages 1-3, nitta2024drosophilamodelto pages 1-2).

### Key Identifiers
- **OMIM:** 165500 (DOA), 125250 (DOA Plus)
- **Synonyms:** Dominant optic atrophy, autosomal dominant optic atrophy (ADOA), Kjer type optic atrophy, Kjer syndrome, syndromic DOA
- **Classification:** Mendelian hereditary optic neuropathy (zeppieri2025isolatedandsyndromic pages 1-2, lee2024hereditaryopticneuropathies pages 1-2)

Note: MONDO, Orphanet, ICD-10/ICD-11, and MeSH identifiers were not available in the retrieved evidence.

### Information Source
The information in this report is derived from aggregated disease-level resources, including peer-reviewed primary literature, systematic reviews, and clinical studies published 2021-2026, with prioritization of 2023-2024 sources as requested.

## 2. Etiology

### Disease Causal Factors

**Primary Genetic Cause:**
The OPA1 gene (chromosome 3q28-q29/3q29) is the major causal gene, accounting for 60-90% of autosomal dominant optic atrophy cases (wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2). OPA1 encodes a ubiquitously expressed mitochondrial dynamin-like GTPase protein localized to the inner mitochondrial membrane (wong2023opa1dominantoptic pages 1-3, maresca2021molecularmechanismsbehind pages 1-3).

**Mechanistic Basis:**
OPA1 is essential for mitochondrial inner membrane fusion, cristae structure maintenance, oxidative phosphorylation support, mitochondrial DNA (mtDNA) maintenance, mitophagy regulation, and apoptosis control (maresca2021molecularmechanismsbehind pages 1-3, amore2021therapeuticoptionsin pages 1-2). Dysfunction in these processes leads to selective vulnerability of retinal ganglion cells (wong2023opa1dominantoptic pages 1-3, strachan2021theroleof pages 1-2).

### Risk Factors

**Genetic Risk Factors:**

*Variant Type and Location:*
The severity and phenotypic spectrum of DOA correlate strongly with variant type and location. Missense mutations in the dynamin/GTPase domain are enriched in DOA Plus and thought to act via dominant-negative effects, whereas truncating mutations (deletions, splice-site, frameshift) typically cause haploinsufficiency (nitta2024drosophilamodelto pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2, zanfardino2024opa1mutationaffects pages 1-2).

A 2025 mechanistic study contrasted two mutations: the missense variant c.1034G>A (p.Arg345Gln) caused >60% mitochondrial fragmentation with greater reactive oxygen species (ROS), cytochrome c release, and apoptosis, versus the splice-site variant c.1305+2delGT which caused ~20% fragmentation (yao2025contrastingpathophysiologicalmechanisms pages 1-2).

*Representative Pathogenic Variants:*
- c.2708_2711delTTAG (OPA1delTTAG): Common recurrent pathogenic deletion
- R445H: Classic DOA Plus-associated missense variant
- c.1034G>A (p.Arg345Gln): GTPase domain missense
- c.1305+2delGT: Splice-site variant
- V465F and V560F: Domain-specific mutations studied in 2025
- c.1406_1407del (p.Thr469LysfsTer16): Newly reported in 2023 pediatric cohort
- p.His42Tyr: ADOA Plus patient fibroblast study variant
- ~69.86 kb deletion encompassing entire OPA1 gene
(nitta2024drosophilamodelto pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2, zhang2025opa1mutationsin pages 1-2, arruti2023opa1dominantoptic pages 1-2, zanfardino2024opa1mutationaffects pages 1-2)

*Modifier Genes:*
While OPA1 is the primary causative gene, recent studies have identified additional genes associated with autosomal optic atrophy, including OPA3, OPA4, TMEM126A/OPA7, SCL25A46, MCAT, RTN4IP1/OPA10, WFS1, ACO2/OPA9, and AFG3L2, though these account for a minority of cases (strachan2021theroleof pages 1-2, zeppieri2025isolatedandsyndromic pages 1-2).

**Environmental Risk Factors:**
No specific environmental risk factors were documented in the retrieved evidence for DOA Plus. The disease is primarily genetically determined.

**Age and Sex:**
Typical onset is in the first or second decade of life, often in early childhood (arruti2023opa1dominantoptic pages 1-2, wong2023opa1dominantoptic pages 1-3). Sex distribution was not systematically reported in the retrieved literature for DOA Plus specifically.

### Protective Factors
No genetic or environmental protective factors were identified in the retrieved evidence for DOA Plus.

### Gene-Environment Interactions
No specific gene-environment interactions were documented in the retrieved evidence for DOA Plus.

## 3. Phenotypes

### Core Ocular Phenotype

**Primary Visual Manifestations:**
- Bilateral, insidious, progressive visual loss beginning in childhood
- Dyschromatopsia/impaired color vision (classically tritanopia/blue-yellow defect)
- Central or centrocecal scotomas on visual field testing
- Temporal optic disc pallor on funduscopy
- Retinal nerve fiber layer (RNFL) thinning, especially in papillomacular bundle
- Ganglion cell layer (GCL) thinning on optical coherence tomography (OCT)
(wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2, lee2024hereditaryopticneuropathies pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2)

**Quantitative OCT Findings (Pediatric Cohort, n=11):**
In a 2023 pediatric study, mean baseline measurements included:
- RNFL thickness: 81.6 µm (right eye), 80.5 µm (left eye)
- Ganglion cell layer: 52.5 µm (right eye), 52.4 µm (left eye)
- Central macular thickness: 229.5 µm (right eye), 233.5 µm (left eye)
- 9/11 patients showed bilateral temporal disc pallor
- Most common visual field defect: centrocecal scotoma
(arruti2023opa1dominantoptic pages 1-2)

**Suggested HPO Terms for Ocular Phenotype:**
- HP:0000618 (Blindness)
- HP:0000529 (Progressive visual loss)
- HP:0000543 (Optic disc pallor)
- HP:0007663 (Reduced visual acuity)
- HP:0000639 (Nystagmus) - when present
- HP:0000613 (Photophobia) - when present

### Extra-Ocular Phenotypes in DOA Plus

**Sensorineural Hearing Loss/Deafness:**
Hearing loss is the most established and common extra-ocular feature, affecting approximately 20% of DOA Plus patients. It frequently manifests as auditory neuropathy spectrum disorder (ANSD) (affortit2024thehumanopa1delttag pages 1-2, kawakita2026frequencyandhearing pages 1-2).

In a 2026 cohort of 18,475 Japanese patients with hearing loss, 10 individuals from 8 families carried OPA1 variants. Hearing loss was typically:
- Post-lingual onset
- Progressive course
- Mild-to-moderate severity
- Associated with ANSD phenotype in missense variant carriers
- 5 patients obtained limited benefit from hearing aids
- 1 cochlear implant recipient achieved good speech perception
(kawakita2026frequencyandhearing pages 1-2)

A 2024 mouse model (Opa1delTTAG) demonstrated adult-onset progressive auditory neuropathy with:
- >40% reduction in Opa1 mRNA (haploinsufficiency mechanism)
- Selective loss of sensory inner hair cells
- Progressive degeneration of axons and myelin sheaths of spiral ganglion neurons
- Age-related mtDNA depletion
- Increased oxidative stress and mitophagy
- Impaired autophagic flux
(affortit2024thehumanopa1delttag pages 1-2)

**Peripheral Neuropathy:**
Progressive peripheral neuropathy is frequently reported in DOA Plus (wong2023opa1dominantoptic pages 1-3, strachan2021theroleof pages 1-2).

**Myopathy:**
Muscle weakness and myopathy are common manifestations (wong2023opa1dominantoptic pages 1-3, nitta2024drosophilamodelto pages 1-2).

**Ataxia:**
Cerebellar ataxia affects a subset of DOA Plus patients (wong2023opa1dominantoptic pages 1-3, strachan2021theroleof pages 1-2).

**Chronic Progressive External Ophthalmoplegia (CPEO):**
Progressive limitation of eye movements due to extraocular muscle involvement (wong2023opa1dominantoptic pages 1-3, chen2023mitochondriaandthe pages 1-2).

**Neurological Complications:**
- Multiple sclerosis-like illness
- Parkinsonism
- Dementia
(wong2023opa1dominantoptic pages 1-3, nitta2024drosophilamodelto pages 1-2)

**Cardiomyopathy:**
Cardiac involvement is less common but reported in DOA Plus (wong2023opa1dominantoptic pages 1-3).

**Suggested HPO Terms for Extra-Ocular Phenotypes:**
- HP:0000407 (Sensorineural hearing impairment)
- HP:0009830 (Peripheral neuropathy)
- HP:0003701 (Proximal muscle weakness/Myopathy)
- HP:0001251 (Ataxia)
- HP:0000602 (Ophthalmoplegia)
- HP:0002071 (Abnormality of extrapyramidal motor function) - for Parkinsonism
- HP:0000726 (Dementia)
- HP:0001638 (Cardiomyopathy)

### Phenotype Characteristics

**Age of Onset:**
Typical onset in first or second decade of life, often early childhood (arruti2023opa1dominantoptic pages 1-2, wong2023opa1dominantoptic pages 1-3). However, expressivity is variable - some patients experience visual loss from birth, while others remain asymptomatic or develop symptoms in adulthood (sampige2025ittakestwo pages 1-2).

**Severity:**
Visual acuity ranges from normal to detection of hand movements only. In a 2023 pediatric cohort, mean baseline visual acuity was 0.40 logMAR (right eye) and 0.44 logMAR (left eye), remaining largely unchanged over follow-up (arruti2023opa1dominantoptic pages 1-2).

**Progression:**
Disease course is insidious and progressive. Visual impairment is typically bilateral and worsens over time. Half of all DOA patients fail driving standards and are registered as legally blind (wong2023opa1dominantoptic pages 1-3).

**Frequency:**
DOA Plus affects approximately 20% of OPA1 mutation carriers, with the remaining 80% presenting with isolated optic atrophy (wong2023opa1dominantoptic pages 1-3, nitta2024drosophilamodelto pages 1-2, strachan2021theroleof pages 1-2).

### Quality of Life Impact
DOA carries a significant detrimental impact on quality of life, with high rates of psychological distress and great societal costs. DOA Plus adds additional morbidity through hearing impairment, neurological, and muscular complications, further reducing quality of life (wong2023opa1dominantoptic pages 1-3, kawakita2026frequencyandhearing pages 1-2).

## 4. Genetic/Molecular Information

### Causal Genes

**Primary Gene:**
- **OPA1** (OMIM 605290, chromosome 3q29)
- Gene structure: Spans >90 kbp genomic DNA, composed of 30 exons (alternative reports: 31 exons)
- Alternative splicing generates 8 different isoforms
- Translated to Long (L-OPA1, ~120 kDa) and Short (S-OPA1, ~80 kDa) forms
(wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2, maresca2021molecularmechanismsbehind pages 1-3)

**Additional Genes:**
While OPA1 accounts for 60-90% of cases, other genes associated with autosomal optic atrophy include OPA3, OPA4, TMEM126A/OPA7, SCL25A46, MCAT, RTN4IP1/OPA10, WFS1, ACO2/OPA9, and AFG3L2 (strachan2021theroleof pages 1-2, zeppieri2025isolatedandsyndromic pages 1-2).

### Pathogenic Variants

**Variant Distribution:**
More than 500 variants in OPA1 are thought to be pathogenic. Of these:
- 28% are missense (mostly in GTPase domain)
- 24% cause aberrant splicing
- 22% cause frameshifts
- Additional variants include nonsense, deletions, insertions, and copy number variants
(wong2023opa1dominantoptic pages 1-3, strachan2021theroleof pages 1-2)

**Variant Classification:**
Three variants from the 2026 hearing-loss cohort were classified as pathogenic or likely pathogenic, while five were variants of uncertain significance (VUS) (kawakita2026frequencyandhearing pages 1-2).

**Allele Frequency:**
Specific population allele frequencies were not systematically reported in the retrieved evidence.

**Somatic vs Germline:**
All documented OPA1 variants associated with DOA/DOA Plus are germline mutations (wong2023opa1dominantoptic pages 1-3, yao2025contrastingpathophysiologicalmechanisms pages 1-2).

**Functional Consequences:**

*Haploinsufficiency Mechanism:*
Many truncating mutations (deletions, splice-site, frameshift) result in reduced OPA1 protein levels, causing disease through haploinsufficiency. The mouse Opa1delTTAG model demonstrated >40% reduction in Opa1 mRNA levels, supporting this mechanism (affortit2024thehumanopa1delttag pages 1-2, nitta2024drosophilamodelto pages 1-2).

*Dominant-Negative Mechanism:*
Missense mutations, particularly in the GTPase domain, are thought to exert dominant-negative effects. These mutant proteins can oligomerize with wild-type OPA1, disrupting normal function more severely than simple haploinsufficiency (nitta2024drosophilamodelto pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2, zanfardino2024opa1mutationaffects pages 1-2).

A 2024 Drosophila study successfully distinguished loss-of-function from dominant-negative mutations, demonstrating that DOA Plus mutations suppressed rescue by wild-type OPA1, supporting dominant-negative action (nitta2024drosophilamodelto pages 1-2).

### Modifier Genes
While not extensively characterized in the retrieved evidence, the variable expressivity of DOA/DOA Plus suggests the involvement of genetic modifiers, though specific genes were not identified.

### Epigenetic Information
No specific epigenetic modifications (DNA methylation, histone modifications) were documented in the retrieved evidence for DOA Plus.

### Chromosomal Abnormalities
Large-scale deletions encompassing the OPA1 gene have been identified, including a ~69.86 kb deletion in the 3q29 region (yao2025contrastingpathophysiologicalmechanisms pages 1-2).

## 5. Environmental Information

No specific environmental factors, lifestyle factors, or infectious agents contributory to DOA Plus were identified in the retrieved evidence. The disease is primarily genetically determined.

## 6. Mechanism / Pathophysiology

### Molecular Pathways

**OPA1 Function in Mitochondrial Homeostasis:**
OPA1 is a multifunctional protein central to mitochondrial homeostasis, regulating:
1. Mitochondrial inner membrane fusion
2. Cristae architecture and remodeling
3. Oxidative phosphorylation (OXPHOS) efficiency
4. Mitochondrial DNA maintenance
5. Mitophagy and quality control
6. Apoptosis regulation
(maresca2021molecularmechanismsbehind pages 1-3, amore2021therapeuticoptionsin pages 1-2, dotto2021dominantopticatrophy pages 1-2)

**Disrupted Pathways in DOA Plus:**

*Mitochondrial Dynamics:*
OPA1 dysfunction disrupts the balance between mitochondrial fusion and fission, leading to excessive fragmentation. The extent of fragmentation correlates with variant type: missense variants in the GTPase domain cause >60% fragmentation, while truncating variants cause ~20% fragmentation (yao2025contrastingpathophysiologicalmechanisms pages 1-2).

*OXPHOS Dysfunction:*
Impaired cristae structure and fusion directly compromise OXPHOS efficiency, reducing ATP production. This is particularly detrimental to metabolically active retinal ganglion cells (maresca2021molecularmechanismsbehind pages 1-3, amore2021therapeuticoptionsin pages 1-2).

*mtDNA Maintenance:*
OPA1 is essential for mtDNA stability. Age-related mtDNA depletion was documented in the Opa1delTTAG mouse model (affortit2024thehumanopa1delttag pages 1-2).

### Cellular Processes

**Mitochondrial Fragmentation:**
Depending on variant type, 20-60% of mitochondria become fragmented in OPA1-deficient cells (yao2025contrastingpathophysiologicalmechanisms pages 1-2, zhang2025opa1mutationsin pages 1-2).

**Membrane Potential Loss:**
OPA1 mutations cause deficits in mitochondrial membrane potential maintenance, with domain-specific effects. The BSE domain mutation V560F caused greater membrane potential deficits than the GTPase domain mutation V465F (zhang2025opa1mutationsin pages 1-2).

**ROS Production:**
Increased reactive oxygen species generation occurs secondary to OXPHOS dysfunction and mitochondrial fragmentation (yao2025contrastingpathophysiologicalmechanisms pages 1-2, affortit2024thehumanopa1delttag pages 1-2).

**Apoptosis:**
OPA1 mutations lead to:
- Cytochrome c release from mitochondria
- Increased cell death under apoptotic stimuli
- Domain-specific effects (BSE mutations cause earlier apoptosis than GTPase mutations)
(zhang2025opa1mutationsin pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2)

**Autophagy and Mitophagy:**
A 2024 fibroblast study from an ADOA Plus patient demonstrated:
- Disrupted mitochondrial network
- Altered mitochondrial dynamics
- Reduced autophagic response
- Impaired autophagic flux
- Enhanced mitophagy response (observed in some models)
(zanfardino2024opa1mutationaffects pages 1-2, affortit2024thehumanopa1delttag pages 1-2)

**Cellular Senescence:**
A novel 2024 finding identified premature senescence in ADOA Plus patient fibroblasts, suggesting a previously unexplored role of OPA1 in cellular aging (zanfardino2024opa1mutationaffects pages 1-2).

### Protein Dysfunction

**Structural Impact:**
Protein structure prediction using AlphaFold2 revealed that:
- Missense variant c.1034G>A (p.Arg345Gln) caused minimal secondary structure alteration
- Splice-site variant c.1305+2delGT resulted in loss of amino acids 411-435, significantly affecting normal secondary structure
(yao2025contrastingpathophysiologicalmechanisms pages 1-2)

**Domain-Specific Effects:**
- GTPase domain mutations (e.g., V465F) impair mitochondrial fusion and cell survival
- BSE α-helix domain mutations (e.g., V560F) cause greater deficits in membrane potential, earlier apoptosis, and distinct molecular pathway changes
(zhang2025opa1mutationsin pages 1-2)

**OPA1 Isoform Processing:**
OPA1 exists as Long (L-OPA1) and Short (S-OPA1) forms. The balance between these forms is critical for function, with mutations affecting processing and stoichiometry (arruti2023opa1dominantoptic pages 1-2, strachan2021theroleof pages 1-2).

### Metabolic Changes

**Energy Metabolism:**
OXPHOS deficiency leads to reduced ATP production, particularly affecting high-energy-demand cells like retinal ganglion cells and neurons (maresca2021molecularmechanismsbehind pages 1-3, amore2021therapeuticoptionsin pages 1-2).

**Oxidative Stress:**
Increased ROS production causes oxidative stress, contributing to cellular damage (yao2025contrastingpathophysiologicalmechanisms pages 1-2, affortit2024thehumanopa1delttag pages 1-2).

### Immune System Involvement
No specific immune system involvement was documented in the retrieved evidence for DOA Plus.

### Tissue Damage Mechanisms

**Selective RGC Vulnerability:**
Retinal ganglion cells are particularly vulnerable to mitochondrial dysfunction due to:
- High metabolic demands
- Long, unmyelinated intra-retinal axonal segments
- Energy dependence for maintaining membrane potential and axonal transport
(maresca2021molecularmechanismsbehind pages 1-3, strachan2021theroleof pages 1-2, rufa2025serumneuronalglial pages 1-8)

**Progressive Degeneration:**
In DOA Plus, degeneration extends beyond RGCs to:
- Auditory neurons (inner hair cells, spiral ganglion neurons)
- Peripheral nerves
- Muscle tissue
- Central nervous system structures
(affortit2024thehumanopa1delttag pages 1-2, kawakita2026frequencyandhearing pages 1-2)

### Biochemical Abnormalities

**Enzyme/Protein Dysfunction:**
OPA1 is a GTPase enzyme. Mutations in the GTPase domain directly impair GTPase activity, compromising fusion activity (zhang2025opa1mutationsin pages 1-2, wong2023opa1dominantoptic pages 1-3).

**Mitochondrial Protein Import:**
The N-terminal mitochondrial targeting sequence (MTS) facilitates OPA1 import. Mutations affecting this region may impair protein localization (zanfardino2024opa1mutationaffects pages 1-2).

### Molecular Profiling

**Transcriptomics:**
Gene set variation analysis and enrichment analysis revealed distinct molecular signatures associated with different OPA1 mutations (V465F vs V560F), indicating domain-specific transcriptional responses (zhang2025opa1mutationsin pages 1-2).

RNA sequencing in ADOA Plus fibroblasts identified altered gene expression patterns related to autophagy, mitophagy, and senescence (zanfardino2024opa1mutationaffects pages 1-2).

**Proteomics:**
Not systematically addressed in the retrieved evidence.

**Metabolomics/Lipidomics:**
Not systematically addressed in the retrieved evidence.

### Advanced Technologies

**Single-Cell Analysis:**
Not reported in the retrieved evidence for DOA Plus.

**iPSC-Derived Models:**
Patient-derived induced pluripotent stem cell (iPSC) lines were generated from two DOA patients in 2023 for RGC differentiation and disease modeling, enabling correlation of cellular phenotypes with clinical features (zanfardino2024opa1mutationaffects pages 1-2, dotto2021dominantopticatrophy pages 1-2).

**Functional Genomics:**
Not systematically reported in the retrieved evidence.

### Causal Chain Summary

The pathogenic cascade in DOA Plus proceeds as follows:

1. **Initial trigger:** OPA1 gene mutation (missense, truncating, or deletion)
2. **Protein-level effect:** Reduced OPA1 function (haploinsufficiency) or dominant-negative interference
3. **Mitochondrial dysfunction:** Impaired fusion → mitochondrial fragmentation → disrupted cristae → OXPHOS deficiency
4. **Cellular consequences:** ATP depletion, ROS production, membrane potential loss, mtDNA instability, impaired autophagy, premature senescence
5. **Cell death:** Cytochrome c release → apoptosis of vulnerable neurons
6. **Tissue-level manifestation:** RGC degeneration → optic atrophy; auditory neuron loss → hearing impairment; peripheral nerve/muscle degeneration → neuropathy/myopathy
7. **Clinical outcome:** Progressive vision loss, deafness, neurological symptoms

**Suggested Ontology Terms:**

*GO Biological Processes:*
- GO:0000266 (mitochondrial fission)
- GO:0008053 (mitochondrial fusion)
- GO:0006915 (apoptotic process)
- GO:0000422 (autophagy of mitochondrion/mitophagy)
- GO:0006119 (oxidative phosphorylation)
- GO:0007569 (cell aging)

*GO Cellular Components:*
- GO:0005743 (mitochondrial inner membrane)
- GO:0005739 (mitochondrion)
- GO:0005759 (mitochondrial matrix)

*Cell Types (CL Terms):*
- CL:0000740 (retinal ganglion cell)
- CL:0000199 (mechanoreceptor cell) - for auditory hair cells
- CL:0000540 (neuron)
- CL:0000187 (muscle cell)

## 7. Anatomical Structures Affected

### Organ Level

**Primary Organ:**
- Eye (optic nerve, retina) - universally affected in DOA/DOA Plus

**Secondary Organ Involvement (DOA Plus):**
- Inner ear (cochlea, spiral ganglion)
- Peripheral nervous system
- Skeletal muscle
- Central nervous system (cerebellum, basal ganglia, cerebral cortex)
- Heart (cardiomyopathy in subset of cases)
(wong2023opa1dominantoptic pages 1-3, affortit2024thehumanopa1delttag pages 1-2, kawakita2026frequencyandhearing pages 1-2)

**Body Systems:**
- Visual system
- Auditory system
- Peripheral nervous system
- Central nervous system
- Musculoskeletal system
- Cardiovascular system (less commonly)

### Tissue and Cell Level

**Specific Tissue Types:**
- Nervous tissue (retinal neurons, auditory neurons, peripheral nerves, central neurons)
- Muscle tissue (skeletal muscle, extraocular muscles)
- Sensory tissue (retinal tissue, inner ear sensory epithelium)

**Specific Cell Populations:**

*Retinal Cells:*
- Retinal ganglion cells (RGCs) - primary target (CL:0000740)
- Preferential loss in papillomacular bundle

*Auditory System:*
- Inner hair cells (sensory mechanoreceptor cells) - selective loss in Opa1delTTAG mice (affortit2024thehumanopa1delttag pages 1-2)
- Spiral ganglion neurons - progressive degeneration of axons and myelin sheaths (affortit2024thehumanopa1delttag pages 1-2)
- Outer hair cells - relatively preserved (ANSD phenotype)

*Other Cell Types:*
- Peripheral nerve neurons (sensory and motor neurons)
- Skeletal muscle myocytes
- Central nervous system neurons (cerebellar, basal ganglia, cortical)
- Cardiac myocytes (in cardiomyopathy cases)

### Subcellular Level

**Cellular Compartments:**

*Mitochondria (GO:0005739):*
- Inner mitochondrial membrane (GO:0005743) - OPA1 localization
- Mitochondrial cristae - structural abnormalities
- Intermembrane space - cytochrome c release
- Mitochondrial matrix (GO:0005759)

*Other Compartments:*
- Nucleus - for gene expression changes
- Cytoplasm - for fragmented mitochondria
- Axons - particularly vulnerable in RGCs due to energy demands

### Localization

**Anatomical Sites (UBERON Terms):**

*Ocular:*
- UBERON:0000970 (eye)
- UBERON:0000941 (optic nerve)
- UBERON:0000966 (retina)
- UBERON:0001789 (optic disc)

*Auditory:*
- UBERON:0001844 (cochlea)
- UBERON:0002768 (spiral ganglion)

*Nervous System:*
- UBERON:0000122 (peripheral nervous system)
- UBERON:0002037 (cerebellum)
- UBERON:0001851 (basal ganglia)

*Other:*
- UBERON:0001134 (skeletal muscle tissue)
- UBERON:0000948 (heart)

**Lateralization:**
Bilateral involvement is characteristic for both optic atrophy and hearing loss in DOA Plus (wong2023opa1dominantoptic pages 1-3, kawakita2026frequencyandhearing pages 1-2).

## 8. Temporal Development

### Onset

**Age of Onset:**
Typical onset in the first or second decade of life, often in early childhood for optic atrophy (arruti2023opa1dominantoptic pages 1-2, wong2023opa1dominantoptic pages 1-3). However, expressivity is variable - onset can range from birth to adulthood (sampige2025ittakestwo pages 1-2).

For hearing loss in DOA Plus, onset is typically post-lingual (kawakita2026frequencyandhearing pages 1-2).

**Onset Pattern:**
Insidious, chronic onset for optic atrophy. Visual loss is gradual and progressive rather than acute (wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2).

### Progression

**Disease Stages:**
Formal staging systems were not described in the retrieved evidence. However, progression can be characterized as:
- Early: Mild visual impairment, subclinical extra-ocular involvement
- Intermediate: Moderate visual loss, emergence of extra-ocular symptoms
- Advanced: Severe visual impairment to blindness, multisystem involvement in DOA Plus

**Progression Rate:**
Slow, progressive course. In the 2023 pediatric cohort, mean visual acuity remained unchanged over the follow-up period (0.40 and 0.44 logMAR at baseline and end of study), suggesting stability in some cases, though long-term progression is documented (arruti2023opa1dominantoptic pages 1-2).

Hearing loss in DOA Plus is progressive (kawakita2026frequencyandhearing pages 1-2).

**Disease Course Pattern:**
Progressive (wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2, kawakita2026frequencyandhearing pages 1-2).

**Disease Duration:**
Chronic, lifelong condition (wong2023opa1dominantoptic pages 1-3).

### Patterns

**Remission:**
No spontaneous or treatment-induced remission was documented in the retrieved evidence.

**Critical Periods:**
Early childhood represents a critical period for diagnosis and genetic counseling. Early identification allows for appropriate interventions and family planning (arruti2023opa1dominantoptic pages 1-2).

## 9. Inheritance and Population

### Epidemiology

**Prevalence:**
- General estimates: 1:12,000 to 1:50,000
- Denmark: 1:10,000 (due to founder effect)
- North East England: 1:25,000
(wong2023opa1dominantoptic pages 1-3, sampige2025ittakestwo pages 1-2, lee2024hereditaryopticneuropathies pages 1-2)

**Incidence:**
Not systematically reported in the retrieved evidence.

### Genetic Inheritance

**Inheritance Pattern:**
Autosomal dominant (wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2, zeppieri2025isolatedandsyndromic pages 1-2).

**Penetrance:**
Incomplete but high. One study estimated 88% lifetime penetrance for OPA1 mutation carriers (yao2025contrastingpathophysiologicalmechanisms pages 1-2, wong2023opa1dominantoptic pages 1-3).

**Expressivity:**
Markedly variable, both interfamilial and intrafamilial. Visual acuities range from normal to hand movements only. Some carriers remain asymptomatic, while others develop severe multisystem disease (yao2025contrastingpathophysiologicalmechanisms pages 1-2, wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2).

**Genetic Anticipation:**
Not documented in the retrieved evidence for DOA Plus.

**Germline Mosaicism:**
Not systematically addressed in the retrieved evidence.

**Founder Effects:**
Denmark exhibits a higher prevalence (1:10,000) due to founder effects (sampige2025ittakestwo pages 1-2).

**Consanguinity:**
Not addressed in the retrieved evidence.

**Carrier Frequency:**
Not systematically reported in the retrieved evidence.

### Population Demographics

**Affected Populations:**
In the 2026 hearing-loss cohort of 18,475 Japanese patients, 10 individuals from 8 families carried OPA1 variants, suggesting rarity in this population (kawakita2026frequencyandhearing pages 1-2). European populations appear more commonly affected based on prevalence estimates (wong2023opa1dominantoptic pages 1-3, sampige2025ittakestwo pages 1-2).

**Geographic Distribution:**
Higher prevalence in Denmark due to founder effects. Geographic distribution of specific variants was not systematically addressed.

**Sex Ratio:**
Not systematically reported in the retrieved evidence, though one hearing-loss cohort noted 13/14 individuals were male (kawakita2026frequencyandhearing pages 1-2).

**Age Distribution:**
Primarily affects children and young adults, with onset typically in the first or second decade (wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2).

## 10. Diagnostics

### Clinical Tests

**Laboratory Tests:**
- Serum neurofilament light chain (sNfL): Elevated in DOA and LHON, supporting ongoing neurodegeneration (rufa2025serumneuronalglial pages 1-8)
- Serum glial fibrillary acidic protein (sGFAP): Elevated in hereditary optic neuropathies (rufa2025serumneuronalglial pages 1-8)
- Serum growth differentiation factor-15 (sGDF-15): Mitochondrial damage marker (rufa2025serumneuronalglial pages 1-8)

Note: These biomarkers are research tools and not yet established as clinical diagnostics.

**Biomarkers:**
No disease-specific biomarkers for DOA Plus are currently in clinical use.

**Imaging Studies:**

*Optical Coherence Tomography (OCT):*
- Demonstrates RNFL thinning, particularly temporally
- Shows ganglion cell layer thinning
- Quantifies macular thickness
- Essential diagnostic and monitoring tool
(wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2, rufa2025serumneuronalglial pages 1-8)

*OCT Angiography:*
- Shows reduced blood flow in temporal region of optic disc (wong2023opa1dominantoptic pages 1-3)

**Functional Tests:**

*Visual Field Testing:*
- Demonstrates central or centrocecal scotomas
- Pattern deviation analysis
(wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2)

*Visual Acuity Assessment:*
- Quantifies degree of visual impairment
- Monitors progression

**Electrophysiology:**

*Visual Evoked Potentials (VEP):*
- Assesses functional integrity of optic nerve pathway
(zeppieri2025isolatedandsyndromic pages 1-2)

*Auditory Tests (for DOA Plus):*
- Auditory brainstem response (ABR): Abnormal in ANSD
- Auditory steady-state response (ASSR): Abnormal in ANSD
- Distortion product otoacoustic emissions (DPOAEs): Preserved in ANSD, indicating intact outer hair cell function
(kawakita2026frequencyandhearing pages 1-2)

**Biopsy/Pathology:**
Skin fibroblast biopsy for mitochondrial function studies and cell-based modeling (zanfardino2024opa1mutationaffects pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2).

### Genetic Testing

**Overview:**
Molecular genetic testing is essential for definitive diagnosis. Multiple approaches are used:

**Whole Exome Sequencing (WES):**
Identified OPA1 variants in research studies. WES is effective for detecting point mutations and small indels (zhang2025opa1mutationsin pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2).

**Gene Panels:**
Targeted sequencing of deafness-related genes (158 genes in one study) or hereditary optic neuropathy panels (kawakita2026frequencyandhearing pages 1-2, zeppieri2025isolatedandsyndromic pages 1-2).

**Single Gene Testing:**
Direct sequencing of OPA1 in suspected cases (arruti2023opa1dominantoptic pages 1-2).

**Chromosomal Microarray/CNV Analysis:**
Necessary to detect large deletions encompassing OPA1 (e.g., ~69.86 kb deletion) (yao2025contrastingpathophysiologicalmechanisms pages 1-2).

**Sequence/Splice-Site Analysis:**
Identifies missense, nonsense, frameshift, and splice-site mutations (arruti2023opa1dominantoptic pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2).

**Sanger Sequencing:**
Used for validation of variants identified by WES or panels (zhang2025opa1mutationsin pages 1-2).

**Examples from Evidence:**
- Pediatric cohort: Identified 7 different OPA1 mutations in 11 children, including one novel variant c.1406_1407del (arruti2023opa1dominantoptic pages 1-2)
- 8/11 pediatric patients had positive family history (arruti2023opa1dominantoptic pages 1-2)

### Clinical Criteria

**Diagnostic Criteria:**
Diagnosis is based on:
1. Clinical presentation: bilateral optic atrophy, progressive vision loss, characteristic fundus and visual field findings
2. OCT demonstration of RNFL and GCL thinning
3. Molecular genetic confirmation of pathogenic OPA1 variant
4. Family history (often positive but not universal)
(wong2023opa1dominantoptic pages 1-3, arruti2023opa1dominantoptic pages 1-2, zeppieri2025isolatedandsyndromic pages 1-2)

**Differential Diagnosis:**
Must distinguish from:
- Leber hereditary optic neuropathy (LHON) - acute onset, maternal inheritance, specific mtDNA mutations
- Glaucoma - elevated intraocular pressure, different disc appearance
- Compressive optic neuropathies
- Inflammatory optic neuropathies
- Other hereditary optic neuropathies (OPA3, ACO2, WFS1, etc.)
(zeppieri2025isolatedandsyndromic pages 1-2, strachan2021theroleof pages 1-2)

### Screening

**Newborn Screening:**
Not currently part of standard newborn screening panels.

**Carrier Screening:**
Genetic testing of at-risk family members is recommended for genetic counseling and family planning (arruti2023opa1dominantoptic pages 1-2, sampige2025ittakestwo pages 1-2).

**Cascade Screening:**
Testing of relatives of affected individuals is appropriate (arruti2023opa1dominantoptic pages 1-2).

## 11. Outcome/Prognosis

### Survival and Mortality

**Life Expectancy:**
DOA/DOA Plus is not typically life-limiting, though severe multisystem involvement in DOA Plus could potentially affect lifespan (not systematically quantified in retrieved evidence).

**Disease-Specific Mortality:**
No specific mortality data were reported in the retrieved evidence for DOA Plus.

### Morbidity and Function

**Morbidity:**
Visual impairment is the universal morbidity. Half of all DOA patients fail driving standards and are registered as legally blind (wong2023opa1dominantoptic pages 1-3).

DOA Plus adds significant morbidity through:
- Hearing impairment requiring rehabilitation
- Neurological dysfunction (ataxia, neuropathy)
- Muscle weakness
- Potential cognitive decline
(wong2023opa1dominantoptic pages 1-3, kawakita2026frequencyandhearing pages 1-2)

**Disability:**
Progressive visual disability leads to:
- Inability to drive
- Occupational limitations
- Reduced independence
- High rates of psychological distress
- Great societal costs
(wong2023opa1dominantoptic pages 1-3)

**Quality of Life:**
DOA carries a significant detrimental impact on quality of life. DOA Plus further reduces QOL through multisystem involvement (wong2023opa1dominantoptic pages 1-3, kawakita2026frequencyandhearing pages 1-2).

### Disease Course

**Complications:**
- Progressive blindness
- Progressive deafness
- Neurological deterioration
- Muscle atrophy
- Cardiac complications (in subset with cardiomyopathy)
(wong2023opa1dominantoptic pages 1-3, kawakita2026frequencyandhearing pages 1-2)

**Recovery Potential:**
Visual loss is typically permanent and irreversible. No spontaneous recovery has been documented (wong2023opa1dominantoptic pages 1-3, amore2021therapeuticoptionsin pages 1-2).

### Prediction

**Prognostic Factors:**
- Variant type: Missense mutations in GTPase domain associated with more severe phenotypes (DOA Plus)
- Age of onset: Earlier onset may correlate with severity
- Family history and penetrance
(nitta2024drosophilamodelto pages 1-2, wong2023opa1dominantoptic pages 1-3)

**Prognostic Biomarkers:**
Elevated sNfL and sGFAP indicate ongoing neurodegeneration but are not established prognostic tools (rufa2025serumneuronalglial pages 1-8).

## 12. Treatment

### Current Management (Supportive)

**Standard of Care:**
Management remains largely supportive, including:
- Low-vision rehabilitation and aids
- Visual aids and magnification devices
- Genetic counseling for affected individuals and families
- Ophthalmologic surveillance with OCT monitoring
- Management of extra-ocular complications in DOA Plus
(lee2024hereditaryopticneuropathies pages 1-2, wong2023opa1dominantoptic pages 1-3, sampige2025ittakestwo pages 1-2)

**Hearing Rehabilitation (DOA Plus):**
- Hearing aids: Provide limited benefit in ANSD phenotype (5 patients in 2026 cohort had limited benefit)
- Cochlear implantation: One patient in 2026 cohort achieved good speech perception
(kawakita2026frequencyandhearing pages 1-2)

### Pharmacotherapy

**Idebenone:**
- A synthetic short-chain analog of coenzyme Q10 with antioxidant properties
- Approved in Europe for LHON in 2015
- For OPA1-related DOA: Preliminary data indicate "possible beneficial effect" but evidence remains limited and not definitive
- Off-label/investigational use in DOA
- Mechanism: Potent intramitochondrial antioxidant, shuttles electrons directly to complex III, bypassing complex I deficiency
(amore2021therapeuticoptionsin pages 1-2, sampige2025ittakestwo pages 1-2, wong2023opa1dominantoptic pages 1-3)

**Other Investigational Small Molecules:**
- Paromomycin: 2025 proof-of-concept study showed rescue of mitochondrial fragmentation induced by c.1034G>A mutation in vitro (yao2025contrastingpathophysiologicalmechanisms pages 1-2)
- EPI-743, elamipretide (mtp-131), estrogen-related compounds, rapamycin, miRNA-based therapies: Under investigation for LHON, potential future application to DOA (amore2021therapeuticoptionsin pages 1-2)

### Advanced Therapeutics

**Gene Therapy:**

*TANGO (Targeted Augmentation of Nuclear Gene Output):*
- Novel antisense oligonucleotide approach (STK-002)
- Delivered intravitreally
- Mechanism: ASO binds to nonsense-mediated decay exons on pre-mRNA transcribed from wild-type OPA1 gene, preserving wild-type gene products
- Variant-agnostic approach (addresses haploinsufficiency)
- Early-stage development for DOA
(sampige2025ittakestwo pages 1-2, wong2023opa1dominantoptic pages 1-3)

*Gene Replacement:*
- Under investigation for DOA
- Similar to LHON gene therapy approaches using AAV2 vectors for intravitreal injection
- Expected to be developed following LHON precedent
(amore2021therapeuticoptionsin pages 1-2, sampige2025ittakestwo pages 1-2)

*Gene Editing:*
- CRISPR-based approaches under investigation
- Potential for correcting specific mutations
- Preclinical stage
(sampige2025ittakestwo pages 1-2)

**Metabolic/Mitochondrial Modulators:**
- Mitochondria-targeted peptides and antioxidants
- NAD+ boosters/metabolic support
- Mitophagy modulators
- Fission-fusion modulators
- All investigational, not in clinical use
(sampige2025ittakestwo pages 1-2)

**Cell-Based Regenerative Therapy:**
- Stem cell-based approaches for RGC regeneration
- Very early stage of investigation
- iPSC-derived RGCs provide research tools
(sampige2025ittakestwo pages 1-2, dotto2021dominantopticatrophy pages 1-2)

### Treatment Outcomes

**Response Rates:**
No established efficacy data for disease-modifying therapies in DOA Plus. Idebenone data primarily from LHON trials (amore2021therapeuticoptionsin pages 1-2).

**Adverse Events:**
Not systematically reported for DOA-specific therapies in the retrieved evidence.

### Treatment Strategy

Currently, no treatment algorithms or combination therapy protocols are established for DOA Plus. Management focuses on symptomatic relief and genetic counseling (wong2023opa1dominantoptic pages 1-3, sampige2025ittakestwo pages 1-2).

**Suggested MAXO Terms:**
- MAXO:0000127 (genetic counseling)
- MAXO:0000058 (pharmaceutical therapy) - for idebenone
- MAXO:0001479 (gene therapy) - investigational
- MAXO:0000011 (rehabilitation therapy)

## 13. Prevention

### Primary Prevention

No primary prevention strategies are available for genetically determined DOA Plus.

### Secondary Prevention

**Screening Programs:**
Genetic screening of at-risk family members allows for:
- Early diagnosis
- Anticipatory guidance
- Appropriate interventions (e.g., timely hearing aids)
- Family planning decisions
(arruti2023opa1dominantoptic pages 1-2, sampige2025ittakestwo pages 1-2)

### Tertiary Prevention

Management of complications:
- Visual rehabilitation to maximize remaining vision
- Hearing rehabilitation to optimize communication
- Monitoring for neurological/cardiac complications
- Occupational therapy for functional adaptation
(wong2023opa1dominantoptic pages 1-3, kawakita2026frequencyandhearing pages 1-2)

### Genetic Counseling

**Counseling:**
Genetic counseling is essential for:
- Risk assessment for family members
- Family planning guidance
- Discussion of inheritance patterns (autosomal dominant, 88% penetrance, variable expressivity)
- Options for prenatal/preimplantation genetic diagnosis
(arruti2023opa1dominantoptic pages 1-2, sampige2025ittakestwo pages 1-2, wong2023opa1dominantoptic pages 1-3)

**Reproductive Options:**
Discussed in genetic counseling sessions but not detailed in the retrieved evidence for DOA Plus specifically.

## 14. Other Species / Natural Disease

### Taxonomy

No naturally occurring disease in other species was documented in the retrieved evidence. However, OPA1 orthologs exist across species (see Model Organisms section below).

### Zoonotic Potential

Not applicable - DOA Plus is a genetic disease, not infectious.

## 15. Model Organisms

### Model Types and Systems

**Yeast Models (Saccharomyces cerevisiae, Schizosaccharomyces pombe):**
- Orthologs: MGM1 (S. cerevisiae), MSP1 (S. pombe)
- Applications: Drug screening (>2,500 drugs tested), functional validation of human OPA1 variants
- Chimeric constructs: Mgm1-OPA1 chimeric proteins functionally rescue yeast phenotypes
- Validation: OPA1 mutations cause mtDNA loss, mitochondrial fragmentation, reduced respiratory capacity, impaired oxidative growth
- Drug discovery: Identified compounds (e.g., 6 drugs) that rescue oxidative growth phenotype and reduce mtDNA instability
(dotto2021dominantopticatrophy pages 1-2, strachan2021theroleof pages 1-2)

**Drosophila melanogaster (Fruit Fly):**
- Gene: dOPA1
- 2024 Study: Loss-of-function mutations mimic optic nerve degeneration observed in DOA
- Human OPA1 rescue: Expression of human OPA1 rescues dOPA1 mutant phenotype, demonstrating functional conservation
- Distinction of mechanisms: Successfully distinguishes loss-of-function from dominant-negative mutations
- DOA Plus modeling: DOA Plus mutations suppress wild-type rescue, confirming dominant-negative action
- Applications: Guides initial treatment strategies, screens therapeutic approaches
(nitta2024drosophilamodelto pages 1-2)

**Mouse Models:**

*Opa1delTTAG Model (2024):*
- Mutation: Human recurrent OPA1delTTAG mutation
- Phenotype: Recapitulates DOA Plus syndrome
- Auditory phenotype: Adult-onset progressive auditory neuropathy
  - >40% reduction in Opa1 mRNA (haploinsufficiency)
  - Selective loss of sensory inner hair cells
  - Progressive degeneration of axons and myelin sheaths of spiral ganglion neurons
  - Age-related mtDNA depletion
  - Increased oxidative stress
  - Enhanced mitophagy
  - Impaired autophagic flux
- Applications: Studying mechanisms of OPA1-linked ANSD, testing therapeutic interventions
(affortit2024thehumanopa1delttag pages 1-2)

*Other Mouse Models:*
- Various conditional, knockout, and knock-in models referenced but not detailed in the retrieved evidence
- Used for studying optic nerve pathology, mitochondrial dynamics, therapeutic testing
(dotto2021dominantopticatrophy pages 1-2, strachan2021theroleof pages 1-2)

**Patient-Derived iPSC Lines:**
- 2023 Study: Generated iPSC lines from two DOA patients with distinct OPA1 mutations and clinical pathologies
- Applications: Differentiation to RGCs for disease modeling, correlation of cellular phenotypes with clinical features, drug screening
- Advantages: Human genetic background, relevant cell type, patient-specific
(dotto2021dominantopticatrophy pages 1-2)

**Cell Culture Models:**

*Primary Neurons:*
- Primary cortical neurons from mice: Assess mitochondrial morphology, membrane potential, cytochrome c release, cell viability
- Advantages: Relevant cell type (neurons), appropriate for studying domain-specific mutation effects
(zhang2025opa1mutationsin pages 1-2)

*Cell Lines:*
- HeLa cells: Widely used for mitochondrial dynamics studies, transfection with OPA1 constructs
- N2a cells (neuroblastoma): Neuronal-like cell line for mechanistic studies
- RGC5 cells: Retinal ganglion cell line (though authenticity debated in field)
- Patient fibroblasts: Mitochondrial function studies, senescence phenotyping, autophagy assays
(zhang2025opa1mutationsin pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2, zanfardino2024opa1mutationaffects pages 1-2)

### Phenotype Recapitulation

**Yeast:**
- Recapitulates: Mitochondrial fragmentation, mtDNA instability, respiratory deficiency
- Limitations: Lacks multicellular complexity, optic nerve, neuronal cell types

**Drosophila:**
- Recapitulates: Optic nerve degeneration
- Successfully distinguishes haploinsufficiency from dominant-negative mechanisms
- Limitations: Invertebrate system, anatomical differences

**Mouse:**
- Recapitulates: Optic atrophy (various models), auditory neuropathy (Opa1delTTAG), mitochondrial dysfunction
- Advantages: Mammalian system, relevant anatomy, testable for therapeutics
- Limitations: Not all aspects of human DOA Plus captured in single model

**iPSCs:**
- Recapitulates: Patient-specific genetic background, can differentiate to RGCs
- Advantages: Human cells, disease-relevant genotype
- Limitations: In vitro system, artificial differentiation protocols

### Model Limitations

General limitations across models include:
- Difficulty fully recapitulating multisystem DOA Plus phenotype in single model
- Variable penetrance and expressivity not easily modeled
- Long-term disease progression challenging to study in short-lived organisms
(dotto2021dominantopticatrophy pages 1-2, strachan2021theroleof pages 1-2)

### Research Applications

Models are used for:
- Understanding pathogenic mechanisms (fusion, OXPHOS, apoptosis, autophagy)
- Distinguishing haploinsufficiency from dominant-negative effects
- Screening therapeutic compounds
- Testing gene therapy approaches
- Studying genotype-phenotype correlations
- Developing biomarkers
(dotto2021dominantopticatrophy pages 1-2, nitta2024drosophilamodelto pages 1-2, affortit2024thehumanopa1delttag pages 1-2, yao2025contrastingpathophysiologicalmechanisms pages 1-2)

---

## Summary and Conclusions

Autosomal Dominant Optic Atrophy Plus is a multisystem mitochondrial disorder caused primarily by mutations in the OPA1 gene, affecting approximately 20% of OPA1 mutation carriers. The disease extends beyond isolated optic atrophy to include extra-ocular manifestations, most commonly sensorineural hearing loss (often ANSD), peripheral neuropathy, myopathy, ataxia, and neurological complications. 

Current understanding emphasizes the dual pathogenic mechanisms of haploinsufficiency (truncating mutations) versus dominant-negative effects (missense mutations in the GTPase domain), which correlate with disease severity. Recent advances (2023-2026) include patient-derived iPSC models, Drosophila functional models distinguishing LOF from dominant-negative mutations, and a mouse model demonstrating progressive auditory neuropathy with detailed mechanistic insights.

While no disease-modifying therapies are currently approved, emerging therapeutic strategies including TANGO antisense oligonucleotides, gene replacement, gene editing, and mitochondrial modulators offer promise. Management currently focuses on supportive care, genetic counseling, and rehabilitation. The prognosis remains guarded, with half of DOA patients experiencing legal blindness and DOA Plus adding substantial morbidity through multisystem involvement.

References

1. (wong2023opa1dominantoptic pages 1-3): David C. S. Wong, Joshua P. Harvey, Neringa Jurkute, Sara M. Thomasy, Mariya Moosajee, Patrick Yu-Wai-Man, and Michael J. Gilhooley. Opa1 dominant optic atrophy: pathogenesis and therapeutic targets. Journal of Neuro-Ophthalmology, 43:464-474, Apr 2023. URL: https://doi.org/10.1097/wno.0000000000001830, doi:10.1097/wno.0000000000001830. This article has 28 citations and is from a peer-reviewed journal.

2. (zanfardino2024opa1mutationaffects pages 1-2): Paola Zanfardino, Alessandro Amati, Stefano Doccini, Sharon N Cox, Apollonia Tullo, Giovanna Longo, Annamaria D’Erchia, Ernesto Picardi, Claudia Nesti, Filippo M Santorelli, and Vittoria Petruzzella. Opa1 mutation affects autophagy and triggers senescence in autosomal dominant optic atrophy plus fibroblasts. Human molecular genetics, 33:768-786, Jan 2024. URL: https://doi.org/10.1093/hmg/ddae008, doi:10.1093/hmg/ddae008. This article has 13 citations and is from a domain leading peer-reviewed journal.

3. (sampige2025ittakestwo pages 1-2): Ritu Sampige, Lyra E.A. Seaborn, Molly Pluenneke, Annika Jyothi, Sophie Saland, Chisom M. Chinedu-Obi, Caroline Keehn, and Andrew G. Lee. It takes two to tango: potential novel therapies for autosomal dominant optic atrophy. Frontiers in Ophthalmology, Nov 2025. URL: https://doi.org/10.3389/fopht.2025.1688232, doi:10.3389/fopht.2025.1688232. This article has 0 citations.

4. (zeppieri2025isolatedandsyndromic pages 1-2): Marco Zeppieri, Caterina Gagliano, Marco Di Maita, Alessandro Avitabile, Giuseppe Gagliano, Edoardo Dammino, Daniele Tognetto, Maria Francesca Cordeiro, and Fabiana D’Esposito. Isolated and syndromic genetic optic neuropathies: a review of genetic and phenotypic heterogeneity. International Journal of Molecular Sciences, 26:3892, Apr 2025. URL: https://doi.org/10.3390/ijms26083892, doi:10.3390/ijms26083892. This article has 5 citations.

5. (lee2024hereditaryopticneuropathies pages 1-2): Samuel K. Lee, Caroline Mura, Nicolas J. Abreu, Janet C. Rucker, Steven L. Galetta, Laura J. Balcer, and Scott N. Grossman. Hereditary optic neuropathies: an updated review. Journal of Clinical &amp; Translational Ophthalmology, 2:64-78, Jun 2024. URL: https://doi.org/10.3390/jcto2030006, doi:10.3390/jcto2030006. This article has 4 citations.

6. (arruti2023opa1dominantoptic pages 1-2): Natalia Arruti, Patricia Rodríguez-Solana, María Nieves-Moreno, Marta Guerrero-Carretero, Ángela del Pozo, Victoria E. F. Montaño, Fernando Santos-Simarro, Emi Rikeros-Orozco, Luna Delgado-Mora, Elena Vallespín, and Susana Noval. Opa1 dominant optic atrophy: diagnostic approach in the pediatric population. Current Issues in Molecular Biology, 45:465-478, Jan 2023. URL: https://doi.org/10.3390/cimb45010030, doi:10.3390/cimb45010030. This article has 6 citations.

7. (yao2025contrastingpathophysiologicalmechanisms pages 1-2): Shi-Qi Yao, Jia-Jian Liang, Hui Zhou, Shaoying Tan, Yingjie Cao, Chong-Bo Chen, Ciyan Xu, Ruixi Wang, Tai-Ping Li, Fang-Fang Zhao, Yun Wang, Han-Jie He, Dan Zhang, Meng Wang, Lifang Liu, Patrick Yu-Wai-Man, Shihui Wei, and Ling-Ping Cen. Contrasting pathophysiological mechanisms of opa1 mutations in autosomal dominant optic atrophy. Cell Death Discovery, May 2025. URL: https://doi.org/10.1038/s41420-025-02442-8, doi:10.1038/s41420-025-02442-8. This article has 4 citations and is from a peer-reviewed journal.

8. (amore2021therapeuticoptionsin pages 1-2): Giulia Amore, Martina Romagnoli, Michele Carbonelli, Piero Barboni, Valerio Carelli, and Chiara La Morgia. Therapeutic options in hereditary optic neuropathies. Drugs, 81:57-86, Nov 2021. URL: https://doi.org/10.1007/s40265-020-01428-3, doi:10.1007/s40265-020-01428-3. This article has 92 citations and is from a domain leading peer-reviewed journal.

9. (nitta2024drosophilamodelto pages 1-2): Yohei Nitta, Jiro Osaka, Ryuto Maki, Satoko Hakeda-Suzuki, Emiko Suzuki, Satoshi Ueki, Takashi Suzuki, and Atsushi Sugie. Drosophila model to clarify the pathological significance of opa1 in autosomal dominant optic atrophy. eLife, Aug 2024. URL: https://doi.org/10.7554/elife.87880, doi:10.7554/elife.87880. This article has 3 citations and is from a domain leading peer-reviewed journal.

10. (zhang2025opa1mutationsin pages 1-2): Kexuan Zhang, Wenqing Zhang, Lin Zhang, Xiaorong Hou, Runyi Tian, Zhengmao Hu, Lili Yin, and Zhonghua Hu. Opa1 mutations in dominant optic atrophy: domain-specific defects in mitochondrial fusion and apoptotic regulation. Journal of Translational Medicine, Apr 2025. URL: https://doi.org/10.1186/s12967-025-06471-w, doi:10.1186/s12967-025-06471-w. This article has 1 citations and is from a peer-reviewed journal.

11. (strachan2021theroleof pages 1-2): Elin L. Strachan, Delphi Mac White-Begg, John Crean, Alison L. Reynolds, Breandán N. Kennedy, and Niamh C. O’Sullivan. The role of mitochondria in optic atrophy with autosomal inheritance. Frontiers in Neuroscience, Nov 2021. URL: https://doi.org/10.3389/fnins.2021.784987, doi:10.3389/fnins.2021.784987. This article has 15 citations and is from a peer-reviewed journal.

12. (affortit2024thehumanopa1delttag pages 1-2): Corentin Affortit, Carolanne Coyat, Anissa Rym Saidia, Jean-Charles Ceccato, Majida Charif, Emmanuelle Sarzi, Frédéric Flamant, Romain Guyot, Chantal Cazevieille, Jean-Luc Puel, Guy Lenaers, and Jing Wang. The human opa1delttag mutation induces adult onset and progressive auditory neuropathy in mice. Cellular and Molecular Life Sciences: CMLS, Feb 2024. URL: https://doi.org/10.1007/s00018-024-05115-4, doi:10.1007/s00018-024-05115-4. This article has 10 citations.

13. (kawakita2026frequencyandhearing pages 1-2): Masayuki Kawakita, Hideaki Moteki, Shin-ya Nishio, Yumiko Kobayashi, Mika Adachi, Takayuki Okano, Hiroshi Yamazaki, Jun Nakayama, Shinya Ohira, Takashi Ishino, Yutaka Takumi, and Shin-ichi Usami. Frequency and hearing loss phenotypes of opa1 variants in a cohort of 18,475 patients with hearing impairment. Genes, 17:341, Mar 2026. URL: https://doi.org/10.3390/genes17030341, doi:10.3390/genes17030341. This article has 0 citations.

14. (dotto2021dominantopticatrophy pages 1-2): Valentina Del Dotto and Valerio Carelli. Dominant optic atrophy (doa): modeling the kaleidoscopic roles of opa1 in mitochondrial homeostasis. Frontiers in Neurology, Jun 2021. URL: https://doi.org/10.3389/fneur.2021.681326, doi:10.3389/fneur.2021.681326. This article has 23 citations and is from a peer-reviewed journal.

15. (rufa2025serumneuronalglial pages 1-8): Alessandra Rufa, Domenico Plantone, Alessia Bargagli, Delia Righi, Tommaso Bacci, Valeria Serchi, Guido Primiano, Gian Nicola Gallus, Diego Lopergolo, Elena Pretegiani, Francesca Rosini, Sara Locci, Gian Marco Tosi, and Nicola De Stefano. Serum neuronal, glial and mitochondrial markers in autosomal dominant optic atrophy and leber hereditary optic neuropathy. Brain Communications, Jan 2025. URL: https://doi.org/10.1093/braincomms/fcaf446, doi:10.1093/braincomms/fcaf446. This article has 0 citations and is from a peer-reviewed journal.

16. (maresca2021molecularmechanismsbehind pages 1-3): Alessandra Maresca and Valerio Carelli. Molecular mechanisms behind inherited neurodegeneration of the optic nerve. Biomolecules, 11:496, Mar 2021. URL: https://doi.org/10.3390/biom11040496, doi:10.3390/biom11040496. This article has 20 citations.

17. (chen2023mitochondriaandthe pages 1-2): Benson S. Chen, Joshua P. Harvey, Michael J. Gilhooley, Neringa Jurkute, and Patrick Yu-Wai-Man. Mitochondria and the eye—manifestations of mitochondrial diseases and their management. Eye, 37:2416-2425, Apr 2023. URL: https://doi.org/10.1038/s41433-023-02523-x, doi:10.1038/s41433-023-02523-x. This article has 42 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Optic_Atrophy_Plus-deep-research-falcon_artifacts/artifact-00.md)