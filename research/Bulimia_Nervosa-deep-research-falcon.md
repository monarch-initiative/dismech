---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-29T23:12:15.149479'
end_time: '2026-07-29T23:19:56.590799'
duration_seconds: 461.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bulimia Nervosa
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Bulimia_Nervosa-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bulimia Nervosa
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Bulimia Nervosa** covering all of the
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
- **Disease Name:** Bulimia Nervosa
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Bulimia Nervosa** covering all of the
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


# Bulimia Nervosa: Disease Characteristics Research Report

## Executive summary

Bulimia nervosa (BN) is a psychiatric eating disorder defined by recurrent, objectively large binge-eating episodes with loss of control, recurrent inappropriate compensatory behavior, and excessive influence of weight or shape on self-evaluation. Under DSM-5-style criteria, binge eating and compensation occur at least weekly for 3 months and do not occur exclusively during anorexia nervosa. BN is usually episodic or relapsing, often begins in adolescence, and can occur at any body mass index; consequently, visual recognition is unreliable. Current understanding is that BN is multifactorial and polygenic rather than a single-gene disorder. Psychological vulnerability, sociocultural pressures, trauma, dieting, and altered reward/inhibitory-control circuitry interact to produce and perpetuate binge–purge cycles. (yu2023efficacyofpharmacotherapies pages 1-2, wilson2024bulimianervosaand pages 1-2, donnelly2018neuroimaginginbulimia pages 1-2, barakat2023riskfactorsfor pages 7-8)

The strongest evidence-based treatment for adults is eating-disorder-focused cognitive behavioral therapy, commonly CBT-E. Family-based treatment is particularly important for adolescents. Fluoxetine is the best-established medication and is generally adjunctive rather than a replacement for psychotherapy. Medical monitoring is essential because vomiting, laxative or diuretic misuse, fasting, and excessive exercise may produce electrolyte, cardiac, gastrointestinal, dental, and endocrine complications. (yu2023efficacyofpharmacotherapies pages 1-2, gkintoni2024clinicalinterventionstrategies pages 30-31, alharbi2024effectivetreatmentapproaches pages 5-6)

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Bulimia nervosa.
* **Abbreviation/synonym:** BN; historically “bulimia.” “Binge–purge eating disorder” is descriptive but is not the preferred controlled label.
* **Category:** Feeding or eating disorder; psychiatric disease.
* **MONDO:** **MONDO:0005452**, confirmed by the Open Targets disease record. No associated molecular targets were returned, consistent with the absence of a validated single causal target. (OpenTargets Search: bulimia nervosa)
* **ICD-10-CM:** **F50.2**, bulimia nervosa.
* **ICD-11:** **6B81**, bulimia nervosa.
* **MeSH:** *Bulimia Nervosa*.
* **OMIM/Orphanet:** No appropriate Mendelian OMIM phenotype or rare-disease Orphanet entry is established for ordinary BN; assigning one would incorrectly imply monogenic or rare-disease causation.

These are aggregated disease-level definitions. They are not individual-patient EHR observations, although ICD/SNOMED labels can be instantiated in EHRs.

### Diagnostic concept

A binge includes unusually large food consumption in a discrete interval and subjective loss of control. Compensation can include self-induced vomiting, laxative or diuretic misuse, fasting, or excessive exercise. Weight/shape overvaluation is required, and BN is differentiated from binge-eating disorder by recurrent compensation and from anorexia nervosa binge–purge type by the absence of persistently significantly low weight meeting AN criteria. (yu2023efficacyofpharmacotherapies pages 1-2, wilson2024bulimianervosaand pages 1-2, wilson2024bulimianervosaand pages 2-3)

## 2. Etiology

### Causal and risk factors

BN has no single sufficient cause. Evidence supports interacting genetic susceptibility, developmental and psychiatric vulnerability, environmental exposure, and learned behavioral reinforcement. A 2023 rapid review grouped eating-disorder risks into genetics; microbiota/autoimmune factors; childhood exposures; personality and psychiatric comorbidity; sex/gender; socioeconomic and minority-related factors; body image/social influence; and elite sport. It emphasized that association does not necessarily establish causality. (barakat2023riskfactorsfor pages 7-8)

**Genetic susceptibility.** Family/twin literature supports moderate heritability, but the retrieved evidence does not justify a precise BN-specific estimate. Candidate associations have been reported in dopamine- and serotonin-related neuroendocrine receptors, glucocorticoid-pathway genes, and the serotonin-transporter-linked polymorphic region, 5-HTTLPR. These are susceptibility findings—not ACMG-pathogenic variants—and are not suitable for clinical prediction. Binge-type eating disorders show genetic overlap with ADHD, while BN also shares genomic liability with overweight/obesity. (barakat2023riskfactorsfor pages 7-8)

**Environmental/developmental risks.** Childhood maltreatment or trauma, body dissatisfaction, internalization of thin/appearance ideals, appearance-focused social media, dieting or restraint, weight stigma, mood/anxiety symptoms, impulsivity, and family/social stress are associated risks. Autoimmune or autoinflammatory disease in childhood was associated with a reported **73% increase in BN risk**, although confounding and mechanisms remain uncertain. (butler2021theroleof pages 10-12, barakat2023riskfactorsfor pages 7-8)

**Gene–environment interaction.** Reported examples include maltreatment interacting with glucocorticoid-receptor pathway polymorphisms or 5-HTTLPR. Lower cortisol following maltreatment has been reported in BN relative to controls, suggesting stress-axis calibration may mediate vulnerability. These findings remain observational and are not actionable biomarkers. (barakat2023riskfactorsfor pages 7-8)

### Protective factors

No reproducible protective allele is established. Plausible environmental protection includes positive body image, reduced appearance-based social comparison, media literacy, supportive family/peer relationships, flexible eating, avoidance of restrictive dieting, early recognition, and rapid access to evidence-based care. These should be treated as prevention targets rather than proven disease-specific protective mechanisms.

## 3. Phenotypes

### Core behavioral and psychiatric phenotypes

* Recurrent binge eating with loss of control—episodic and variable in frequency.
* Self-induced vomiting or other compensation: laxatives/diuretics, fasting, or driven exercise.
* Overvaluation of body weight/shape, body dissatisfaction, dietary restraint, shame, secrecy, and impaired emotion regulation.
* Depression, anxiety, self-harm, suicidality, and substance-use symptoms are important comorbid phenotypes. Review estimates include mood disorders in **43%**, anxiety disorders in **53%**, and lifetime mood disorder in **80–90%**, but estimates vary substantially by sample and definition. (yu2023efficacyofpharmacotherapies pages 1-2, donnelly2018neuroimaginginbulimia pages 1-2)

### Physical signs, manifestations, and laboratory abnormalities

Vomiting may cause dental enamel erosion, caries, pharyngeal trauma, salivary-gland enlargement, reflux or other gastrointestinal symptoms, dehydration, and electrolyte/acid–base abnormalities. Severe electrolyte disturbance can precipitate weakness, syncope, QT abnormalities, or arrhythmia. Menstrual irregularity can occur, although it is less diagnostically central than in restrictive disorders. Normal or high weight does not exclude serious medical instability. (wilson2024bulimianervosaand pages 1-2, wilson2024bulimianervosaand pages 2-3, alharbi2024effectivetreatmentapproaches pages 5-6)

Suggested HPO mappings include **Binge eating**, **Self-induced vomiting**, **Abnormality of electrolyte homeostasis**, **Hypokalemia**, **Dehydration**, **Cardiac arrhythmia**, **Dental erosion**, **Salivary-gland enlargement**, **Menstrual irregularity**, **Anxiety**, and **Depressive symptom**. Exact term IDs should be validated against the current HPO release before ingestion.

### Severity, progression, and quality of life

DSM severity is based on weekly compensatory-event frequency: mild 1–3, moderate 4–7, severe 8–13, and extreme ≥14, with clinical judgment allowing adjustment for disability. Course is commonly fluctuating or relapsing. Individual phenotypes impair school/work attendance, relationships, finances, concentration, self-esteem, and social eating. The evidence base uses inconsistent remission and recovery definitions, limiting precise cross-study estimates.

## 4. Genetic and molecular information

BN should be annotated as **multifactorial/polygenic**, not Mendelian. There are no established causal genes, pathogenic germline variants, recurrent chromosomal abnormalities, founder mutations, carrier frequencies, penetrance estimates, anticipation, or germline mosaicism relevant to routine BN. Correspondingly, Open Targets returned **zero disease–target associations** for MONDO:0005452. (OpenTargets Search: bulimia nervosa)

Reported candidate loci in serotonergic, dopaminergic, and glucocorticoid signaling are association-level observations. They should not be labeled pathogenic or likely pathogenic under ACMG/AMP criteria. No validated modifier gene or clinically useful pharmacogenomic marker exists for selecting CBT or fluoxetine specifically in BN. (barakat2023riskfactorsfor pages 7-8)

Epigenetic evidence specific to BN is sparse and confounded by trauma, diet, medication, smoking, adiposity, and illness state. No methylation signature is validated diagnostically. WGS, WES, gene panels, CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are therefore **not indicated for uncomplicated BN**; they are reserved for syndromic presentations suggesting another disorder.

## 5. Environmental information

There is no infectious cause and no evidence supporting vaccination, antimicrobial treatment, or zoonotic control. No toxin, radiation, or occupational exposure is established as a specific cause. Relevant exposures are predominantly psychosocial and behavioral: restrictive dieting, weight cycling, appearance pressure, social-media comparison, bullying/weight stigma, trauma, elite sports emphasizing leanness, and family or peer reinforcement. Alcohol, nicotine, stimulant, or other substance use may coexist and can increase medical and behavioral risk. (barakat2023riskfactorsfor pages 7-8)

## 6. Mechanism and pathophysiology

### Integrated causal model

A defensible causal chain is: polygenic/developmental vulnerability plus appearance, trauma, or dieting exposures → negative affect, restraint, altered interoception and reward valuation → food restriction and heightened cue salience → loss-of-control binge → acute distress and fear of weight gain → purging/fasting/exercise, which provides short-term negative reinforcement → renewed restriction and repeated cycles. Recurrent purging then produces downstream electrolyte, dental, salivary, gastrointestinal, and cardiovascular injury.

### Neural circuitry and signaling

Human neuroimaging studies report reduced activity in frontostriatal control circuits and abnormal responses in the insula, amygdala, middle frontal gyrus, orbitofrontal cortex, and anterior cingulate cortex. These findings support impaired inhibitory control, altered reward sensitivity, food-cue attentional bias, and emotion/interoceptive dysregulation. Greater binge/bulimic frequency correlates with more pronounced neural alteration. However, a systematic review found substantial methodological heterogeneity and small samples, so no imaging pattern is diagnostic or demonstrably causal. (donnelly2018neuroimaginginbulimia pages 1-2)

Suggested processes include GO concepts related to **regulation of feeding behavior**, **dopamine receptor signaling**, **serotonin receptor signaling**, **response to stress**, **reward learning**, and **behavioral response inhibition**. Relevant cells include excitatory and inhibitory neurons, dopaminergic neurons, serotonergic neurons, and peripheral T lymphocytes; current evidence does not support a BN-specific cellular lesion.

### Gut–brain, metabolic, and immune findings

Microbiome/metabolite differences have been reported across eating disorders and binge–purge versus restricting patterns, but small, mixed-diagnosis samples and diet/adiposity confounding prevent a BN-specific signature. These findings are hypothesis-generating, not grounds for probiotics or fecal transplantation as standard treatment.

BN does **not** show a consistent systemic inflammatory-cytokine phenotype: meta-analysis found no reliable IL-6 or TNF-α difference; PBMC production of IFN-γ, IL-1β, IL-6, and TNF-α was also not consistently altered. A cohort of 76 obese BN patients showed higher IL-1β, IL-6, and TNF-α, plausibly attributable to adiposity. Lower CD4/CD8 ratios and reduced CD2, CD3, CD4, CD8, and CD57 have been reported, but confounding and replication limitations preclude an immune biomarker. (butler2021theroleof pages 10-12)

No validated transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omic diagnostic signature exists for BN.

## 7. Anatomical structures affected

The primary functional system is the central nervous system, especially frontostriatal, salience, reward, and emotion-regulation networks. Secondary injury involves teeth/enamel, oral mucosa and pharynx, salivary glands, esophagus and gastrointestinal tract, kidneys through volume/electrolyte disturbance, heart through electrolyte-mediated conduction abnormalities, and reproductive/endocrine systems. (wilson2024bulimianervosaand pages 1-2, donnelly2018neuroimaginginbulimia pages 1-2, alharbi2024effectivetreatmentapproaches pages 5-6)

Suggested UBERON annotations are brain, cerebral cortex, insula, amygdala, orbitofrontal cortex, anterior cingulate cortex, striatum, tooth enamel, salivary gland, pharynx, esophagus, stomach, kidney, and heart. Lateralization is not a defining feature. Subcellular pathology is not established; synaptic and receptor signaling are implicated functionally rather than through a known organelle defect.

## 8. Temporal development

Onset is typically adolescent to young-adult and often insidious, beginning with dieting, shape concern, or episodic bingeing. One review reported average onset at **16–17 years**, whereas a 2024 disparities review cited median onset at **12.4 years**; the discrepancy reflects different samples and ascertainment and should not be collapsed into one value. (yu2023efficacyofpharmacotherapies pages 1-2, wilson2024bulimianervosaand pages 1-2)

The disease is episodic or relapsing-remitting and can become chronic. Diagnostic crossover with anorexia nervosa or other specified eating disorders occurs. Early treatment is a key opportunity because repeated cycles become behaviorally reinforced and medical complications accumulate. Remission may be spontaneous or treatment-induced, but relapse prevention and follow-up remain necessary.

## 9. Inheritance and population

Lifetime prevalence estimates vary by diagnostic threshold and survey. Recent reviews cite approximately **0.9–3% overall**, **1.5–3% in females**, and **0.5% to >1% in males**; 12-month prevalence around **0.4%** has been reported. These values should be represented as ranges rather than a universal estimate. (yu2023efficacyofpharmacotherapies pages 1-2, wilson2024bulimianervosaand pages 1-2)

Females are diagnosed more often, but BN occurs in males, gender-diverse people, all racial/ethnic groups, and across body sizes and socioeconomic strata. Research samples have often been **80–100% female and 80–100% White**, meaning apparent demographic gradients partly reflect ascertainment and access bias. Older adults, males, and racial minorities remain underrepresented. (wilson2024bulimianervosaand pages 1-2, wilson2024bulimianervosaand pages 2-3)

Inheritance is polygenic/multifactorial with incomplete, probabilistic expression. Mendelian penetrance, carrier frequency, consanguinity, anticipation, founder effects, and geographic variant distributions are not applicable.

## 10. Diagnostics

### Clinical assessment

Diagnosis is made by confidential clinical interview using DSM-5-TR or ICD-11 criteria. Assessment should characterize objective and subjective binges, loss of control, each compensatory method, weekly frequency/duration, shape/weight overvaluation, dietary restraint, exercise, medications/substances, menstrual history, self-harm/suicide risk, and comorbidity. Collateral family information is useful in adolescents.

Screening instruments such as SCOFF can identify possible eating disorders but cannot establish BN. There is no newborn, carrier, prenatal, genomic, or population laboratory screen.

### Medical evaluation

Physical assessment should include weight trajectory rather than BMI alone, pulse, blood pressure including orthostasis, temperature, hydration, oral/dental and salivary examination, and signs of self-induced vomiting. Depending on severity and purging method, tests commonly include CBC, electrolytes, bicarbonate, renal function, glucose, magnesium, phosphate, liver tests, urinalysis, pregnancy testing when relevant, and ECG. Electrolyte abnormality, dehydration, and arrhythmia are indications for urgent escalation or hospitalization. (alharbi2024effectivetreatmentapproaches pages 5-6)

No blood, imaging, electrophysiological, biopsy, genetic, or omics biomarker confirms BN. MRI/PET/fMRI are research tools, not diagnostic tests. (donnelly2018neuroimaginginbulimia pages 1-2)

### Differential diagnosis

Important alternatives include binge-eating disorder, anorexia nervosa binge–purge type, purging disorder/OSFED, avoidant-restrictive food intake disorder, mood or bipolar illness with appetite change, substance-induced behavior, gastrointestinal disease, endocrine disease, and neurologic conditions. The decisive distinctions are low-weight AN status, presence/absence of recurrent compensation, objective binge criteria, and weight/shape psychopathology.

## 11. Outcome and prognosis

Recovery is possible, including after prolonged illness. One narrative review cited remission approaching **80% with proper treatment**, but this should be interpreted cautiously because outcome definitions and follow-up periods vary. CBT effects are generally moderate, and long-term maintenance is less certain. (wilson2024bulimianervosaand pages 2-3, donnelly2018neuroimaginginbulimia pages 1-2)

BN carries elevated mortality through suicide and medical complications. A 2024 review cited standardized mortality ratios of approximately **1.5–2.5** and an **eightfold greater suicide-death risk** than the general population. These are population-level estimates, not individual predictions. (wilson2024bulimianervosaand pages 1-2)

Adverse prognostic features include severe/frequent binge–purge behavior, suicidality, substance use, trauma/PTSD, mood/anxiety comorbidity, medical instability, longer untreated duration, and poor treatment access. A striking **85–94%** reportedly delay or never seek treatment, making under-detection a major real-world determinant of outcome. (wilson2024bulimianervosaand pages 1-2)

## 12. Treatment

### Treatment strategy and current implementation

Care should be multidisciplinary and least restrictive while medically safe: medical assessment and stabilization → collaborative nutritional rehabilitation and regular eating → evidence-based psychotherapy → adjunct medication where appropriate → relapse prevention and comorbidity treatment. About **5%** of patients were estimated to require inpatient care; dehydration, electrolyte disturbance, arrhythmia, severe self-harm, or psychiatric decompensation are key indications. Partial-hospital programs commonly provide 7–10 hours/day of structured treatment. (alharbi2024effectivetreatmentapproaches pages 5-6)

**Psychotherapy.** CBT/CBT-E is first-line for adults and targets irregular eating, restraint, binge–purge reinforcement, cognitive distortions, and weight/shape overvaluation. Guided self-help can improve access for less complex cases. Interpersonal therapy is an alternative when CBT is unavailable or unsuitable. DBT-informed approaches may help prominent emotion dysregulation, though they are not generally superior to BN-focused CBT. Suggested MAXO annotations: cognitive behavioral therapy, psychotherapy, nutritional counseling, family therapy, and behavioral intervention. (gkintoni2024clinicalinterventionstrategies pages 30-31, wilson2024bulimianervosaand pages 2-3)

**Adolescents.** Family-based treatment for BN is strongly supported. One synthesis reported remission of **39% with FBT versus 20% with CBT and 18% with supportive psychotherapy**. In an RCT of 109 adolescents aged 12–18, abstinence was **39.4% with FBT-BN versus 19.7% with CBT-A** at completion and **44.0% versus 25.4%** at 6 months. (alharbi2024effectivetreatmentapproaches pages 5-6)

**Pharmacotherapy.** Fluoxetine, an SSRI, has the strongest regulatory and trial evidence for adult BN and is usually used at 60 mg/day when appropriate. It may reduce bingeing, vomiting, and depressive symptoms but should generally complement psychotherapy. A 2023 meta-analysis of 33 studies covering 11 drugs found modest effects versus placebo: binge episodes SMD **−0.40** (95% CI −0.61 to −0.19), vomiting SMD **−0.16** (−0.30 to −0.03), depressive symptoms SMD **−0.32** (−0.51 to −0.13), and weight WMD **−3.05 kg** (−5.97 to −0.13). The evidence included SSRIs, TCAs, MAOIs, topiramate, lithium, and fenfluramine; this does not make all options clinically advisable. (yu2023efficacyofpharmacotherapies pages 1-2)

Bupropion is generally avoided because purging/electrolyte disturbance increases seizure risk. TCAs and MAOIs have greater safety/tolerability burdens. Topiramate has some efficacy but cognitive, metabolic, and teratogenic concerns. No medication is FDA-approved specifically for pediatric BN. No validated genotype-guided therapy, gene/cell/RNA therapy, immunotherapy, or surgery exists. (gkintoni2024clinicalinterventionstrategies pages 30-31)

**Experimental/current trials.** Retrieved ClinicalTrials.gov records illustrate current directions: MDMA-assisted therapy, NCT07542145, phase 1, recruiting, n=40; group therapy, NCT06063278, completed, n=100; eating-related inhibition/valuation, NCT05995496, recruiting, n=150; smartphone aftercare, NCT05728021, n=172; eating-related neurofeedback, NCT05614024, recruiting, n=30; web intervention, NCT04876196, completed, n=152; neurobiology study, NCT04225221, phase 2, completed, n=10; lisdexamfetamine, NCT03397446, phase 2, terminated, n=23; PET-guided serotonergic treatment, NCT02359513, phase 4, completed, n=51; and rTMS, NCT01530906, status uncertain, n=60. These are investigational and do not establish efficacy.

### Access and disparities

The evidence base underrepresents males, older adults, racial/ethnic minorities, and diverse body sizes. Digital CBT, guided self-help, primary-care screening, and stepped care are real-world attempts to close access gaps, but digital delivery still requires suicide and medical-risk pathways. (wilson2024bulimianervosaand pages 1-2, wilson2024bulimianervosaand pages 2-3)

## 13. Prevention

**Primary prevention:** school/community programs promoting media literacy, body functionality and diversity, reduced weight stigma, flexible eating, and avoidance of restrictive dieting; safeguards in leanness-focused sports; and trauma-informed environments. No vaccine or prophylactic drug applies.

**Secondary prevention:** targeted screening in adolescents, athletes, people presenting with dental erosion, recurrent electrolyte disturbance, depression/anxiety, self-harm, or weight-control behaviors; confidential questioning and rapid referral. Because most affected people do not promptly seek care, case finding is a high priority. (wilson2024bulimianervosaand pages 1-2)

**Tertiary prevention:** relapse plans, continued meal regularity, monitoring for renewed purging, electrolyte/renal/cardiac surveillance when indicated, dental care, suicide prevention, and integrated treatment of mood, anxiety, PTSD, and substance-use disorders. Genetic counseling is not routinely indicated because risk is polygenic and non-deterministic.

## 14. Other species and natural disease

No well-established naturally occurring animal disease is homologous to human BN, and BN is not infectious, transmissible, or zoonotic. Animals can exhibit binge-like consumption or compensatory restriction, but the human syndrome requires subjective loss of control and weight/shape overvaluation, which cannot be directly established in animals. Therefore, veterinary breed, VBO, natural-disease gene, and cross-species transmission fields should be recorded as **not applicable/not established**.

## 15. Model organisms

Rodent binge-eating models use intermittent access to palatable high-fat/high-sugar food, food restriction/refeeding, stress, or limited-access paradigms. They are useful for studying reward, dopamine, serotonin, opioid/endocannabinoid signaling, stress, and candidate drugs. Their central limitation for BN is that rats and mice lack an emetic response; purging must be modeled indirectly through restriction or exercise. They also cannot recapitulate human body-image cognition, shame, or sociocultural influences. Consequently, these are models of components—especially binge behavior—not complete models of BN.

Human fMRI/PET paradigms, ecological momentary assessment, smartphone monitoring, and experimentally controlled meal tasks have higher face validity for cognitive control and cue reactivity. No validated BN organoid, iPSC, humanized genetic model, or single causal-gene knockout exists.

## Ontology-ready summary

The following table provides compact knowledge-base annotations. Terms explicitly marked “suggested” require verification against the current ontology release before production ingestion.

| Domain | Recommended terms/IDs | Evidence-backed annotation | Caveat |
|---|---|---|---|
| Disease identifier | MONDO: **MONDO_0005452**; ICD-10: **F50.2**; ICD-11: **6B81**; MeSH: **Bulimia Nervosa** | BN is a psychiatric eating disorder characterized by recurrent binge eating with compensatory behaviors; DSM-style features summarized in recent BN reviews and pharmacotherapy meta-analysis (yu2023efficacyofpharmacotherapies pages 1-2, wilson2024bulimianervosaand pages 1-2, wilson2024bulimianervosaand pages 2-3) | MONDO exact match supported by Open Targets context; ICD/MeSH listed as standard identifiers but not directly validated in supplied abstracts; treat as standard ontology mappings (OpenTargets Search: bulimia nervosa) |
| Synonyms / labels | **Bulimia nervosa**; **BN**; suggested synonym: **binge-purge eating disorder** | Literature consistently uses “bulimia nervosa (BN)” as the preferred label (yu2023efficacyofpharmacotherapies pages 1-2, wilson2024bulimianervosaand pages 1-2) | Alternative names beyond BN abbreviation are suggested/unverified in supplied evidence |
| Core phenotype | Suggested HPO: **binge eating** [suggested/unverified HPO ID]; **self-induced vomiting** [suggested/unverified HPO ID] | Core syndrome includes recurrent binge eating plus inappropriate compensatory behaviors such as self-induced vomiting, laxative/diuretic misuse, fasting, or excessive exercise (yu2023efficacyofpharmacotherapies pages 1-2, wilson2024bulimianervosaand pages 1-2, wilson2024bulimianervosaand pages 2-3) | Exact HPO IDs were not supplied by the evidence set |
| Electrolyte phenotype | Suggested HPO: **Electrolyte abnormality** [suggested/unverified HPO ID]; **Hypokalemia** [suggested/unverified HPO ID] | Purging-related medical complications include electrolyte imbalance; hospitalization indications include dehydration, electrolyte abnormalities, and arrhythmias (wilson2024bulimianervosaand pages 1-2, alharbi2024effectivetreatmentapproaches pages 5-6) | Hypokalemia is well known clinically but not quantified in supplied extracts; exact HPO IDs not supplied |
| Oral/dental phenotype | Suggested HPO: **Dental erosion** [suggested/unverified HPO ID] | Dental erosion is repeatedly cited as a complication of recurrent vomiting/purging (wilson2024bulimianervosaand pages 1-2, wilson2024bulimianervosaand pages 2-3) | Exact HPO ID not supplied |
| Salivary phenotype | Suggested HPO: **Salivary gland enlargement** [suggested/unverified HPO ID] | Salivary gland hypertrophy/enlargement is described among purging-related complications (wilson2024bulimianervosaand pages 1-2, wilson2024bulimianervosaand pages 2-3) | Exact HPO ID not supplied |
| Reproductive phenotype | Suggested HPO: **Menstrual irregularity** [suggested/unverified HPO ID] | Menstrual irregularities are reported among medical complications in BN reviews (wilson2024bulimianervosaand pages 2-3) | Less emphasized than in restrictive EDs; exact HPO ID not supplied |
| Cardiac phenotype | Suggested HPO: **Arrhythmia** [suggested/unverified HPO ID] | Cardiac arrhythmias are a recognized medical risk, especially in the context of dehydration/electrolyte disturbance from purging (alharbi2024effectivetreatmentapproaches pages 5-6) | Exact HPO ID not supplied |
| Psychiatric comorbidity phenotype | Suggested HPO: **Anxiety** [suggested/unverified HPO ID]; **Depression** [suggested/unverified HPO ID] | Anxiety and mood disorders are common; meta-analysis/reviews cite anxiety disorders ~53%, mood disorders ~43%, and lifetime mood disorder burden up to 80–90% in BN cohorts (yu2023efficacyofpharmacotherapies pages 1-2, donnelly2018neuroimaginginbulimia pages 1-2) | Percentages reflect review-level synthesis and may vary across diagnostic criteria/sample ascertainment |
| Anatomy | UBERON suggested: **brain**; **frontostriatal circuitry** [structure/system mapping suggested]; **gastrointestinal tract**; **tooth/teeth**; **salivary gland**; **heart** | Neuroimaging review implicates frontostriatal circuits, insula, amygdala, orbitofrontal/anterior cingulate regions; purging complications involve GI tract, teeth, salivary glands, and heart (donnelly2018neuroimaginginbulimia pages 1-2, wilson2024bulimianervosaand pages 1-2, alharbi2024effectivetreatmentapproaches pages 5-6) | Exact UBERON IDs were not provided in evidence; “frontostriatal circuitry” may need post-coordination rather than a single UBERON term |
| Cellular component / cell type | CL suggested: **neuron**; **peripheral blood mononuclear cell**; **T cell** | BN neurobiology centers on neuronal circuits; immune studies reported altered CD2/CD3/CD4/CD8/CD57 and lower CD4/CD8 ratios, including PBMC-based cytokine studies (butler2021theroleof pages 10-12) | Exact CL IDs not supplied; immune findings are less consistent than neural findings |
| Biological process | GO suggested: **reward processing** [suggested/unverified GO term mapping]; **inhibitory control** [suggested/unverified GO term mapping]; **serotonin signaling**; **dopamine signaling**; **immune response** | Reviews implicate altered reward sensitivity, food-related attentional bias, impaired inhibitory control, and serotonergic/dopaminergic pathways; immune-response changes are mixed but T-cell alterations reported (donnelly2018neuroimaginginbulimia pages 1-2, barakat2023riskfactorsfor pages 7-8, butler2021theroleof pages 10-12) | “Reward processing” and “inhibitory control” may require nearest GO-process approximations rather than exact labels |
| Genetics / inheritance | Suggested annotation: **multifactorial, polygenic psychiatric disorder** | BN is described as multifactorial with genetic predisposition, environmental factors, and psychological traits; risk review cites serotonin/dopamine receptor-related polymorphisms, glucocorticoid pathway variants, and 5-HTTLPR involvement (yu2023efficacyofpharmacotherapies pages 1-2, barakat2023riskfactorsfor pages 7-8) | No single causal gene/variant is established for routine clinical use in supplied evidence |
| Gene–environment interaction | Suggested annotation: **childhood trauma × glucocorticoid/5-HTTLPR risk background** | Childhood trauma/abuse interacting with glucocorticoid receptor polymorphisms and 5-HTTLPR is reported as increasing BN risk; lower cortisol after maltreatment was noted in BN cases vs controls (barakat2023riskfactorsfor pages 7-8) | Evidence is review-level and not sufficient for deterministic biomarker use |
| Immune / inflammatory annotation | Suggested annotation: **immune dysregulation with inconsistent cytokine signal; T-cell alterations reported** | BN does not show a consistent pro-inflammatory cytokine signature across studies, but reduced CD4/CD8 ratios and lower T-cell markers have been reported (butler2021theroleof pages 10-12) | Confounding by adiposity, comorbidity, treatment, and illness severity limits interpretation |
| Neurobiology | Suggested annotation: **frontostriatal hypoactivity; aberrant insula/amygdala/OFC/ACC responses** | Neuroimaging synthesis found frontostriatal hypoactivity, altered inhibitory control, and abnormal responses to food/disorder-related cues; illness severity correlates with greater neural changes (donnelly2018neuroimaginginbulimia pages 1-2) | Evidence base is heterogeneous and often underpowered |
| Epidemiology / onset | Suggested annotation: **adolescent onset; female predominance** | Reviews cite average onset around 16–17 years and median onset around 12.4 years; lifetime prevalence estimates include ~1.5% in females and 0.5% in males, with treatment non-engagement/delay in 85–94% (yu2023efficacyofpharmacotherapies pages 1-2, wilson2024bulimianervosaand pages 1-2) | Onset/prevalence values vary by source, age window, and ascertainment method |
| Prognosis / outcomes | Suggested annotation: **remission possible; relapse and mortality remain concerns** | Review-level evidence suggests remission is achievable, with one review citing up to 80% remission with proper treatment; suicide risk and SMR elevations are noted (wilson2024bulimianervosaand pages 1-2, wilson2024bulimianervosaand pages 2-3) | Outcome definitions are inconsistent across studies |
| MAXO treatment concepts | MAXO suggested: **cognitive behavioral therapy (CBT/CBT-E)**; **family-based therapy (FBT)**; **nutritional therapy**; **electrolyte monitoring**; **electrocardiographic monitoring (ECG)** | CBT is consistently first-line; FBT has supportive evidence in adolescents; nutritional therapy and medical monitoring are part of standard care; hospitalization may be required for dehydration/electrolyte disturbance/arrhythmia (gkintoni2024clinicalinterventionstrategies pages 30-31, wilson2024bulimianervosaand pages 2-3, alharbi2024effectivetreatmentapproaches pages 5-6) | Exact MAXO IDs were not supplied in evidence |
| Pharmacotherapy | Suggested term: **fluoxetine**; broader classes: **SSRIs**, **TCAs**, **MAOIs**, **topiramate** | Meta-analysis of 33 studies found modest benefit of pharmacotherapy for binge frequency, vomiting frequency, weight, and depressive symptoms; SSRIs/fluoxetine are commonly referenced in guideline-style reviews (yu2023efficacyofpharmacotherapies pages 1-2) | Medication effects are modest overall; exact preferred agent hierarchy depends on guideline context |
| Diagnostic workup | Suggested terms: **clinical interview/DSM criteria**, **electrolytes**, **ECG**, **medical assessment for purging complications** | Diagnosis is clinical, based on binge eating plus compensatory behaviors occurring at least weekly for 3 months; medical workup should assess dehydration, electrolyte abnormalities, and arrhythmias (yu2023efficacyofpharmacotherapies pages 1-2, wilson2024bulimianervosaand pages 2-3, alharbi2024effectivetreatmentapproaches pages 5-6) | No validated BN-specific molecular biomarker is established in supplied evidence |


*Table: This compact table organizes bulimia nervosa into ontology-ready disease, phenotype, anatomy, mechanism, and treatment annotations using only evidence available in the retrieved context. It is useful as a starting point for knowledge-base population, while clearly marking suggested or unverified ontology IDs where the supplied evidence did not provide exact identifiers.*

## Evidence appraisal and authoritative interpretation

The most reliable current conclusion is that BN is a clinically diagnosed, polygenic and environmentally responsive psychiatric syndrome—not a monogenic, inflammatory, infectious, or biomarker-defined disease. Evidence is strongest for CBT/CBT-E, adolescent FBT, adjunctive fluoxetine, and active medical monitoring. Genetic candidates, microbiome changes, cytokines, neuroimaging, and other omics remain mechanistic research signals rather than clinical tests or treatment-selection biomarkers. (OpenTargets Search: bulimia nervosa, yu2023efficacyofpharmacotherapies pages 1-2, donnelly2018neuroimaginginbulimia pages 1-2, butler2021theroleof pages 10-12, barakat2023riskfactorsfor pages 7-8)

Representative exact abstract language includes: **“BN is characterized by recurrent binge eating episodes with inappropriate compensatory behaviors”** in the 2023 pharmacotherapy synthesis, and the neuroimaging review concluded that **“heterogenous”** studies prevented robust conclusions regarding precise neurobiology. The 2024 disparities review’s central real-world warning is that older adults, males, and racial minorities remain systematically underrepresented. (yu2023efficacyofpharmacotherapies pages 1-2, wilson2024bulimianervosaand pages 1-2, donnelly2018neuroimaginginbulimia pages 1-2)

### Key recent sources and URLs

* Yu S, et al. *Efficacy of pharmacotherapies for bulimia nervosa: a systematic review and meta-analysis.* **December 2023.** https://doi.org/10.1186/s40360-023-00713-7 (yu2023efficacyofpharmacotherapies pages 1-2)
* Wilson K, Kagabo R. *Bulimia nervosa and treatment-related disparities: a review.* **August 2024.** https://doi.org/10.3389/fpsyg.2024.1386347 (wilson2024bulimianervosaand pages 1-2, wilson2024bulimianervosaand pages 2-3)
* Gkintoni E, et al. *Clinical intervention strategies and family dynamics in adolescent eating disorders.* **July 2024.** https://doi.org/10.3390/jcm13144084 (gkintoni2024clinicalinterventionstrategies pages 30-31)
* Alharbi Y, et al. *Effective treatment approaches for eating disorders in children and adolescents.* **November 2024.** https://doi.org/10.7759/cureus.74003 (alharbi2024effectivetreatmentapproaches pages 5-6)
* Barakat S, et al. *Risk factors for eating disorders: findings from a rapid review.* **January 2023.** https://doi.org/10.1186/s40337-022-00717-4 (barakat2023riskfactorsfor pages 7-8)
* Donnelly B, et al. *Neuroimaging in bulimia nervosa and binge eating disorder: a systematic review.* **February 2018.** https://doi.org/10.1186/s40337-018-0187-1 (donnelly2018neuroimaginginbulimia pages 1-2)
* Butler MJ, et al. *The role of the gut microbiome, immunity, and neuroinflammation in the pathophysiology of eating disorders.* **February 2021.** https://doi.org/10.3390/nu13020500 (butler2021theroleof pages 10-12)

PMIDs were not exposed in the retrieved full-text metadata and therefore are not fabricated here; DOI URLs are supplied as stable primary identifiers.

References

1. (yu2023efficacyofpharmacotherapies pages 1-2): Sijie Yu, Yuhan Zhang, Chongkai Shen, and Fei Shao. Efficacy of pharmacotherapies for bulimia nervosa: a systematic review and meta-analysis. BMC Pharmacology and Toxicology, Dec 2023. URL: https://doi.org/10.1186/s40360-023-00713-7, doi:10.1186/s40360-023-00713-7. This article has 23 citations.

2. (wilson2024bulimianervosaand pages 1-2): Kim Wilson and Robert Kagabo. Bulimia nervosa and treatment-related disparities: a review. Frontiers in Psychology, Aug 2024. URL: https://doi.org/10.3389/fpsyg.2024.1386347, doi:10.3389/fpsyg.2024.1386347. This article has 13 citations and is from a peer-reviewed journal.

3. (donnelly2018neuroimaginginbulimia pages 1-2): Brooke Donnelly, Stephen Touyz, Phillipa Hay, Amy Burton, Janice Russell, and Ian Caterson. Neuroimaging in bulimia nervosa and binge eating disorder: a systematic review. Journal of Eating Disorders, Feb 2018. URL: https://doi.org/10.1186/s40337-018-0187-1, doi:10.1186/s40337-018-0187-1. This article has 177 citations and is from a peer-reviewed journal.

4. (barakat2023riskfactorsfor pages 7-8): Sarah Barakat, S. McLean, E. Bryant, Ân H. Lê, P. Marks, Phillip Sarah Robert Leah Emma Susan Belinda Shannon Bronn Aouad Barakat Boakes Brennan Bryant Byrne Caldwell, P. Aouad, Sarah Barakat, R. Boakes, L. Brennan, S. Byrne, Belinda Caldwell, S. Calvert, B. Carroll, D. Castle, I. Caterson, Belinda Chelius, Lyn Chiem, S. Clarke, J. Conti, Lexi Crouch, Genevieve Dammery, Natasha Dzajkovski, J. Fardouly, Carmen Felicia, John Feneley, Amber-Marie Firriolo, N. Foroughi, M. Fuller-Tyszkiewicz, A. Fursland, V. Gonzalez-Arce, Bethanie Gouldthorp, Kelly Griffin, S. Griffiths, A. Hambleton, A. Hannigan, Melissa Hart, S. Hart, P. Hay, I. Hickie, Francis Kay-Lambkin, R. King, M. Kohn, E. Koreshe, I. Krug, Ân H. Lê, Jake Linardon, Randall Long, Amanda Long, S. Madden, S. Maguire, D. Maloney, S. McLean, Thy Meddick, J. Miskovic-Wheatley, Deborah Mitchison, R. O’Kearney, S. Ong, R. Paterson, S. Paxton, Melissa J Pehlivan, G. Pépin, A. Phillipou, J. Piccone, R. Pinkus, Bronwyn C Raykos, P. Rhodes, E. Rieger, Sarah Rodan, Karen Rockett, J. Russell, H. Russell, Fiona Salter, Susan S. Sawyer, Beth. Shelton, Urvashnee Singh, Sophie Smith, Evelyn Smith, K. Spielman, S. Squire, J. Thomson, M. Tiggemann, S. Touyz, Ranjani Utpala, L. Vartanian, Andrew Wallis, W. Ward, Sarah Wells, E. Wertheim, S. Wilksch, and Michelle Williams. Risk factors for eating disorders: findings from a rapid review. Journal of Eating Disorders, Jan 2023. URL: https://doi.org/10.1186/s40337-022-00717-4, doi:10.1186/s40337-022-00717-4. This article has 580 citations and is from a peer-reviewed journal.

5. (gkintoni2024clinicalinterventionstrategies pages 30-31): Evgenia Gkintoni, Elias Kourkoutas, Stephanos P. Vassilopoulos, and Maria Mousi. Clinical intervention strategies and family dynamics in adolescent eating disorders: a scoping review for enhancing early detection and outcomes. Jul 2024. URL: https://doi.org/10.3390/jcm13144084, doi:10.3390/jcm13144084. This article has 45 citations.

6. (alharbi2024effectivetreatmentapproaches pages 5-6): Yara Alharbi, Fatema Saleh, and Khaled A Shahat. Effective treatment approaches for eating disorders in children and adolescents: a review article. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.74003, doi:10.7759/cureus.74003. This article has 7 citations.

7. (OpenTargets Search: bulimia nervosa): Open Targets Query (bulimia nervosa, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (wilson2024bulimianervosaand pages 2-3): Kim Wilson and Robert Kagabo. Bulimia nervosa and treatment-related disparities: a review. Frontiers in Psychology, Aug 2024. URL: https://doi.org/10.3389/fpsyg.2024.1386347, doi:10.3389/fpsyg.2024.1386347. This article has 13 citations and is from a peer-reviewed journal.

9. (butler2021theroleof pages 10-12): Michael J. Butler, Alexis A. Perrini, and Lisa A. Eckel. The role of the gut microbiome, immunity, and neuroinflammation in the pathophysiology of eating disorders. Nutrients, 13:500, Feb 2021. URL: https://doi.org/10.3390/nu13020500, doi:10.3390/nu13020500. This article has 109 citations.

## Artifacts

- [Edison artifact artifact-00](Bulimia_Nervosa-deep-research-falcon_artifacts/artifact-00.md)