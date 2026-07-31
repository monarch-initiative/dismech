---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-29T23:12:12.502974'
end_time: '2026-07-29T23:19:02.752961'
duration_seconds: 410.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rumination Disorder
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 7
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Rumination_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rumination Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Rumination Disorder** covering all of the
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
- **Disease Name:** Rumination Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Rumination Disorder** covering all of the
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


# Rumination Disorder (Rumination Syndrome): Disease-Characteristics Report

## Scope and evidence note

This report concerns **rumination disorder/rumination syndrome**, not depressive or anxiety-related cognitive rumination. The condition crosses classification systems: psychiatry describes *rumination disorder* as a feeding/eating disorder, whereas gastroenterology commonly describes *rumination syndrome* as a disorder of gut–brain interaction. The strongest retrieved evidence comprised 2024 expert reviews/consensus statements, primary interventional studies and ClinicalTrials.gov records. Several important 2023–2024 epidemiologic and pediatric articles were indexed but their full text was unavailable to the retrieval system; consequently, unsupported prevalence or outcome estimates are not supplied.

| Domain | Curated finding | Ontology/identifier suggestions | Evidence strength/gap |
|---|---|---|---|
| Definition and nomenclature | Rumination disorder/syndrome is a disorder of gut-brain interaction / feeding-related disorder characterized by recurrent, effortless regurgitation of recently ingested food, typically soon after meals, due to a learned behavioral pattern rather than primary acid reflux or structural disease; literature uses both **rumination disorder** and **rumination syndrome**. It can be mistaken for PPI-refractory GERD and should be distinguished from vomiting, GERD, and supragastric belching (gyawali2024updatestothe pages 3-3, arguero2024pathophysiologyofgastrooesophageal pages 9-10). | Suggested mappings requiring validation: MONDO term for rumination disorder/syndrome; MeSH/ICD-11/DSM-5 terminology alignment; related ontology concepts: disorder of gut-brain interaction, feeding and eating disorder | Moderate-strong clinical/guideline evidence; identifier harmonization remains a curation task |
| Key phenotype | Core phenotype is **postprandial repetitive regurgitation** of recently ingested food, usually effortless and not preceded by retching; episodes are often triggered by habitual abdominal wall contraction and may lessen when contents become acidic (NCT03113682 chunk 1, NCT03062696 chunk 1, gyawali2024updatestothe pages 3-3). | Suggested mappings requiring validation: HPO terms for regurgitation, postprandial symptom exacerbation, nausea/fullness/epigastric discomfort where present | Strong for core symptom; phenotype frequency/severity distributions remain incompletely standardized across cohorts |
| Mechanism / pathophysiology | Current understanding supports a **behavioral-somatic mechanism**: food ingestion is followed by unintentional abdomino-thoracic/abdominal wall contraction with relaxation of esophageal sphincter mechanisms, producing retrograde flow of gastric contents. Breathing-based therapies likely work by interrupting this motor pattern; vagal modulation is under investigation (NCT03912636 chunk 2, NCT02214472 chunk 1, NCT02402946 chunk 1, NCT03113682 chunk 1, NCT03062696 chunk 1). | Suggested mappings requiring validation: GO terms related to motor behavior, muscle contraction, autonomic regulation; CL terms for skeletal muscle cell, enteric neuron, vagal-related autonomic neuron | Moderate mechanistic evidence from physiology and interventional studies; molecular pathway detail is limited |
| Anatomy | Primary affected structures are the **stomach**, **esophagus**, **lower esophageal sphincter region**, **diaphragm**, and **abdominal wall musculature**; the syndrome reflects abnormal coordination across upper GI and respiratory/abdominal motor systems rather than a focal tissue lesion (NCT02214472 chunk 1, NCT02402946 chunk 1, NCT03113396 chunk 1). | Suggested mappings requiring validation: UBERON terms for stomach, esophagus, diaphragm, abdominal wall musculature, lower esophageal sphincter | Moderate evidence from manometric/physiologic studies; no specific histopathologic lesion established |
| Epidemiology | Population burden is recognized globally, but precise prevalence varies by diagnostic framework and ascertainment; recent reviews/meta-analytic work exist but exact pooled estimates were not available in the retrieved evidence set here. Rumination is likely under-recognized and misdiagnosed as reflux-related disease (gyawali2024updatestothe pages 3-3, arguero2024pathophysiologyofgastrooesophageal pages 9-10). | Suggested mappings requiring validation: epidemiology annotation for global distribution, pediatric and adult onset | Evidence gap in this artifact: recent prevalence estimates should be added from primary epidemiology/meta-analysis sources before KB finalization |
| Diagnosis | Diagnosis is primarily **clinical**, supported when needed by **high-resolution impedance manometry** and/or **ambulatory pH-impedance monitoring** to distinguish rumination from GERD and belching disorders. Diagnostic workup should exclude relevant organic disease but avoid excessive low-yield testing (NCT03912636 chunk 2, NCT02214472 chunk 1, gyawali2024updatestothe pages 3-3, arguero2024pathophysiologyofgastrooesophageal pages 9-10). | Suggested mappings requiring validation: diagnostic procedure terms for clinical assessment, high-resolution impedance manometry, ambulatory pH-impedance monitoring | Strong expert-consensus and trial-supportive evidence |
| First-line treatment | **Behavioral therapy** is first-line, especially **diaphragmatic breathing** and structured **cognitive-behavioral therapy for rumination disorder/syndrome (CBT-RD/CBT-RS)** targeting habit reversal and competing responses to abdominal wall contraction (NCT03912636 chunk 2, NCT03113682 chunk 1, NCT03062696 chunk 1, gyawali2024updatestothe pages 3-3, arguero2024pathophysiologyofgastrooesophageal pages 9-10). | Suggested mappings requiring validation: MAXO terms for behavioral therapy, diaphragmatic breathing training, cognitive behavioral therapy, habit reversal | Strongest current treatment evidence; supported by physiologic rationale and interventional studies |
| Adjunct treatment | **Biofeedback** (including EMG-guided biofeedback) has randomized trial support as a nonpharmacologic adjunct. **Baclofen** has been studied in placebo-controlled crossover trials and pediatric investigation as an adjunct when behavioral therapy is insufficient or unavailable (NCT02214472 chunk 1, NCT02402946 chunk 1, NCT03113396 chunk 1). | Suggested mappings requiring validation: MAXO terms for biofeedback, electromyographic biofeedback, baclofen therapy | Moderate evidence; smaller studies/trials, and long-term comparative effectiveness remains limited |
| Genetics / omics | **No monogenic causal gene, pathogenic variant, chromosomal abnormality, validated susceptibility locus, molecular biomarker, transcriptomic signature, proteomic signature, metabolomic signature, or epigenetic marker is established for rumination disorder/syndrome.** No validated germline or somatic genetic testing approach is currently indicated (NCT03113682 chunk 1, NCT03062696 chunk 1, gyawali2024updatestothe pages 3-3, arguero2024pathophysiologyofgastrooesophageal pages 9-10). | Suggested mappings requiring validation: “no established gene-disease association”; “no validated biomarker” annotations | Major evidence gap / likely non-applicable at present |
| Prognosis | Prognosis is generally tied to **recognition and response to behavioral treatment**; chronic symptoms, diagnostic delay, nutritional compromise, psychosocial burden, and reduced quality of life can occur, but disease-specific mortality is not established in available evidence here. Misdiagnosis may prolong morbidity (NCT03113682 chunk 1, NCT03062696 chunk 1, gyawali2024updatestothe pages 3-3, arguero2024pathophysiologyofgastrooesophageal pages 9-10). | Suggested mappings requiring validation: annotations for chronic/relapsing course, quality-of-life impact, nutritional complications | Moderate evidence for morbidity; quantitative long-term natural history remains limited in this evidence set |
| Prevention | There is **no established primary prevention** based on genetics, infection, toxin, or environmental exposure. Practical prevention focuses on **early recognition**, avoidance of unnecessary reflux escalation/surgery, patient education, and prompt access to behavioral therapy to reduce chronicity and complications (gyawali2024updatestothe pages 3-3, arguero2024pathophysiologyofgastrooesophageal pages 9-10). | Suggested mappings requiring validation: secondary prevention via early diagnosis; tertiary prevention via behavioral management and nutritional support | Moderate expert-opinion evidence; no formal public-health prevention program established |
| Environmental / infectious / toxic causes | **No infectious agent, toxin, radiation exposure, pollutant, or occupational exposure has been established as a primary cause.** The disorder is best understood as a learned behavioral/physiologic pattern within gut-brain interaction frameworks (gyawali2024updatestothe pages 3-3, arguero2024pathophysiologyofgastrooesophageal pages 9-10). | Suggested mappings requiring validation: “no established infectious etiology”; “no established toxic etiology” | Evidence gap / negative finding based on current understanding |
| Animal models / other species | **No validated animal model or naturally occurring nonhuman disease model is established for rumination disorder/syndrome**, consistent with the disorder’s human behavioral-physiologic phenotype and reliance on symptom report/manometry-based characterization (NCT03113682 chunk 1, NCT03062696 chunk 1, gyawali2024updatestothe pages 3-3, arguero2024pathophysiologyofgastrooesophageal pages 9-10). | Suggested mappings requiring validation: “no validated model organism” annotation | Major evidence gap / likely non-applicable at present |


*Table: This table summarizes core knowledge-base findings for rumination disorder/syndrome across definition, mechanism, diagnosis, treatment, and evidence gaps. It is designed for rapid curation and explicitly flags domains where no validated genetic, biomarker, infectious, toxic, or animal-model evidence is established.*

## 1. Disease information

### Definition and terminology

Rumination disorder is characterized by recurrent, usually effortless regurgitation of recently ingested food during or soon after eating, followed by rechewing, reswallowing, or expulsion. Episodes commonly occur several times per week and often daily. The regurgitation is generated by a learned or subconscious abdominothoracic motor behavior, not by intentional self-induced vomiting, primary structural disease, or ordinary gastroesophageal reflux. A trial protocol states directly: **“Rumination disorder (RD; also known as ‘rumination syndrome’) is a disordered eating behavior characterized by the repeated regurgitation of food during or soon after eating.”** (NCT03113682 chunk 1)

Synonyms include **rumination syndrome**, **rumination disorder**, **merycism**, and, historically, **psychogenic rumination**. “Infant rumination syndrome” is a pediatric Rome category, but childhood, adolescent, and adult presentations also occur. The term must not be conflated with repetitive negative thinking in mood disorders.

### Identifiers

* **MeSH:** Rumination Syndrome, **D000079562**. MeSH places it under gastrointestinal/digestive disease and feeding-and-eating/mental-disorder hierarchies. (NCT03912636 chunk 2)
* **DSM-5/DSM-5-TR:** Rumination disorder, feeding and eating disorders chapter; commonly coded **307.53 / ICD-10-CM F98.21**.
* **ICD-10-CM:** **F98.21**, Rumination disorder of infancy; this label is narrower than contemporary all-age usage. In some clinical coding contexts, symptom or functional-GI codes may be used.
* **ICD-11:** Classified among feeding or eating disorders; the exact browser code should be verified against the jurisdiction-specific current ICD-11 release before ingestion.
* **Rome IV:** Rumination syndrome is included among functional nausea and vomiting disorders/disorders of gut–brain interaction.
* **MONDO:** A dedicated current MONDO identifier could not be verified from the retrieved source set; do not assign one without direct MONDO validation.
* **OMIM/Orphanet:** No established Mendelian disease entry or orphan-disease entity was identified.

The evidence summarized here is **aggregated disease-level evidence** from consensus papers, reviews, trials, and registries—not individual EHR-derived patient data.

## 2. Etiology, risk factors, and protective factors

### Causal model

No single cause is established. Current understanding favors an **acquired, conditioned behavioral–physiologic pattern**. Meal-related discomfort, stress, prior gastrointestinal illness or vomiting, and heightened attention to digestive sensations may initiate the behavior in some patients, after which negative reinforcement—temporary relief of pressure or discomfort—may maintain it. These are proposed triggers or perpetuating factors, not necessary causes.

Psychiatric and feeding/eating comorbidities may coexist, but the disorder is not simply intentional behavior or proof of a primary psychiatric cause. GERD and other gastrointestinal disorders can also coexist and may provide an initial regurgitation sensation that becomes conditioned.

### Genetic and environmental factors

No causal gene, pathogenic variant, susceptibility locus, inheritance pattern, penetrance estimate, founder effect, carrier frequency, or validated gene–environment interaction has been established. Therefore, ClinVar variant classification, gnomAD allele frequency, germline/somatic origin, and genetic counseling for a rumination-specific mutation are **not applicable at present**.

No toxin, radiation exposure, pollution source, occupational exposure, infectious organism, smoking pattern, alcohol exposure, or dietary constituent is established as a specific cause. Likewise, no genetic protective allele is known. The best-supported practical protective factors are behavioral: early recognition, correct diagnosis, education, and acquisition of a competing postprandial breathing response.

## 3. Phenotypes

### Core and associated manifestations

* **Effortless postprandial regurgitation:** the defining symptom; recently ingested, initially recognizable/non-acidic food returns to the mouth. It often starts during or soon after a meal and may recur until gastric contents become acidic. Lyon Consensus 2.0 characterizes rumination as a subconscious learned postprandial behavior and notes that it may cease as the regurgitate becomes acidic. (gyawali2024updatestothe pages 3-3)
* **Rechewing, reswallowing, or spitting out:** follows regurgitation and is part of the defining behavioral phenotype. (NCT03912636 chunk 1, NCT02214472 chunk 1)
* **Absent nausea or retching in typical episodes:** helps distinguish rumination from vomiting, although nausea, fullness, or epigastric discomfort can coexist. The vagal-tone study measured nausea, fullness, and epigastric discomfort on 0–5 scales, total 0–15, demonstrating their relevance as associated rather than defining symptoms. (NCT03912636 chunk 2)
* **Observable abdominal-wall contraction or “premonitory urge”:** may precede regurgitation; patients may initially be unaware of the contraction.
* **Nutritional/physical consequences:** reduced intake, avoidance of meals, weight loss or poor growth, malnutrition, dehydration, dental erosion, halitosis, and esophageal irritation can occur in severe or prolonged disease. No reliable per-phenotype frequencies were available in the retrieved evidence.
* **Behavioral and psychosocial effects:** embarrassment, school/work disruption, avoidance of eating socially, anxiety around meals, and caregiver burden can substantially impair quality of life.

### Onset, severity, and course

Onset can occur in infancy, childhood, adolescence, or adulthood. Severity ranges from occasional episodes without nutritional compromise to daily, meal-associated regurgitation causing weight loss and hospitalization. The course may be chronic, fluctuating, or relapse after stress or inconsistent practice of competing responses. It is not intrinsically neurodegenerative or progressive.

### Suggested HPO mappings

Suggested mappings, requiring validation against the current HPO release, include **Regurgitation**, **Postprandial symptom exacerbation**, **Feeding difficulties**, **Weight loss**, **Failure to thrive**, **Malnutrition**, **Nausea**, **Abdominal discomfort**, **Dental erosion**, and **Dehydration**. HPO does not fully represent learned behavioral timing and should be supplemented with DSM/Rome annotations and phenotype qualifiers.

## 4. Genetic and molecular information

No rumination-specific causal gene, HGNC association, pathogenic variant, modifier gene, chromosomal abnormality, epigenetic signature, protein dysfunction, or molecular diagnostic biomarker is established. WES, WGS, gene panels, single-gene testing, CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing have **no routine diagnostic role** unless another syndromic diagnosis is suspected.

No validated disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, multi-omic, CRISPR-screen, or RNAi-screen result was identified. Assertions that particular molecular pathways cause the disorder would currently be speculative.

## 5. Environmental information

The relevant “environment” is primarily the meal and behavioral context rather than a toxic exposure. Potential precipitating contexts reported clinically include gastrointestinal illness, vomiting, reflux sensations, surgery, psychosocial stress, and meal-associated discomfort. These associations do not establish causality. No infectious agent is implicated, and the condition is neither communicable nor zoonotic.

## 6. Mechanism and pathophysiology

### Causal chain

The best-supported chain is:

1. **Meal ingestion or postprandial discomfort** provides an internal cue.
2. An initially voluntary or inadvertent behavior becomes a **learned, largely subconscious abdominal-wall/abdominothoracic contraction**.
3. This raises intragastric pressure while gastroesophageal junction resistance falls or the lower esophageal sphincter relaxes.
4. Gastric contents move retrogradely through the esophagus into the mouth.
5. Rechewing, reswallowing, expulsion, or relief of discomfort reinforces the motor habit.
6. Repeated exposure produces nutritional, mucosal, dental, and psychosocial downstream morbidity.

The primary biofeedback trial describes rumination as **“an unperceived, somatic response to food ingestion”** and targets abnormal abdominothoracic muscular activity. (NCT02214472 chunk 1) CBT-RD similarly treats the habitual abdominal-wall contraction by habit reversal, using diaphragmatic breathing as a competing response. (NCT03113682 chunk 1, NCT03062696 chunk 1)

### Upstream versus downstream mechanisms

Upstream components include meal-related sensation, learned cueing, visceral vigilance, and abdominal-wall activation. The motor event—increased abdominal/intragastric pressure coordinated with reduced sphincter resistance—is proximal to retrograde flow. Regurgitation, mucosal exposure, nutritional compromise, dental injury, and psychosocial avoidance are downstream.

Autonomic regulation is under study rather than established. NCT03912636 compared cardiac vagal tone derived from ECG R–R intervals in patients and healthy volunteers and tested diaphragmatic versus slow deep breathing. Its stated hypothesis was that breathing might improve rumination by altering nervous control of the stomach; this is mechanistic investigation, not proof that vagal dysfunction is causal. (NCT03912636 chunk 1, NCT03912636 chunk 2)

There is no established immune, inflammatory, apoptotic, autophagic, fibrotic, oxidative-stress, enzyme-deficiency, receptor-mutation, ion-channel, or metabolic-pathway mechanism.

### Ontology suggestions

Suggested biological-process mappings include **skeletal muscle contraction**, **regulation of digestive-system process**, **autonomic nervous system process**, **esophageal motility**, and **behavioral response to food**; current GO identifiers should be checked before ingestion. Suggested Cell Ontology concepts are **skeletal muscle cell**, **smooth muscle cell**, **enteric neuron**, **sensory neuron**, and **autonomic neuron**. These are participating cell types, not proven primary cellular lesions.

## 7. Anatomical structures affected

The functional circuit involves the **stomach, gastroesophageal junction/lower esophageal sphincter region, esophagus, diaphragm, intercostal musculature, and abdominal-wall muscles**. Secondary injury may affect esophageal and oral/dental tissues. There is no consistent focal histopathologic lesion, lateralization, or disease-specific subcellular compartment.

Suggested UBERON mappings include **stomach**, **esophagus**, **gastroesophageal junction**, **diaphragm**, **abdominal wall**, and **oral cavity**. Relevant tissue classes are skeletal muscle, gastrointestinal smooth muscle, enteric nervous tissue, and esophageal epithelium. Exact UBERON identifiers should be release-validated.

## 8. Temporal development

Episodes typically begin during or shortly after meals and may repeat for up to one or more postprandial hours. The disorder may begin at any age and can be insidious after an initiating illness or stressor. No universally accepted early/intermediate/advanced staging system exists.

Without recognition, the learned behavior may persist for months or years. Remission can occur with effective behavioral retraining; relapse may occur when practice stops or triggers recur. Early diagnosis is therefore a clinically important intervention window, but a precise “critical period” has not been defined.

## 9. Inheritance and population

Rumination disorder is not currently considered a Mendelian disease; inheritance, penetrance, anticipation, mosaicism, consanguinity, and carrier status are not applicable. It occurs internationally and in children and adults of all sexes. No robust ethnic or geographic genetic enrichment is established.

Recent global epidemiology and a 2024 systematic review/meta-analysis were identified during searching, but exact pooled prevalence values could not be verified from accessible full text. The defensible conclusion is that prevalence varies materially with case definition, age, clinical versus community ascertainment, and Rome versus DSM criteria. Under-recognition is likely because patients are frequently labeled as having refractory GERD or vomiting. Lyon Consensus 2.0 specifically warns that rumination can masquerade as PPI-refractory GERD. (gyawali2024updatestothe pages 3-3)

Disease-specific incidence per 100,000 person-years, a stable sex ratio, and age-stratified population rates remain insufficiently established in the retrieved evidence.

## 10. Diagnostics

### Clinical criteria

Diagnosis is primarily clinical. The key history is recurrent return of recently ingested food during or soon after meals, usually effortless, without preceding retching, with rechewing/reswallowing/spitting. The clinician should determine meal timing, taste/acidity, abdominal contraction or urge, duration, nutritional effect, intent, and relationship to body-image or compensatory behavior.

Rome IV criteria are commonly used in gastroenterology; DSM criteria additionally require that repeated regurgitation not be attributable to a gastrointestinal/medical condition, occur outside anorexia nervosa, bulimia nervosa, binge-eating disorder, or ARFID—or warrant separate attention if comorbid—and cause clinically significant impairment. The Rome IV vagal-tone study required clinical criteria plus confirmation by high-resolution impedance manometry. (NCT03912636 chunk 2)

### Testing

* **High-resolution impedance manometry with a postprandial test meal:** best objective confirmatory test in uncertain cases. It can show abdominal-pressure increases and retrograde bolus movement and distinguish rumination from supragastric belching or reflux.
* **Ambulatory pH-impedance monitoring:** useful when GERD remains a concern. Lyon Consensus 2.0 recommends reflux monitoring when behavioral mimics are suspected and emphasizes that treatment differs fundamentally. (gyawali2024updatestothe pages 3-3)
* **Endoscopy, imaging, gastric-emptying studies, or routine laboratories:** not diagnostic; use selectively for alarm features, nutritional consequences, or plausible alternatives.
* **Questionnaires/interviews:** PARDI assesses diagnosis, frequency, and severity and served as the principal outcome in CBT-RD pilots. (NCT03113682 chunk 1, NCT03062696 chunk 1)
* **Biomarkers/omics/genetics:** none validated.

### Differential diagnosis

Major alternatives are GERD, gastroparesis, achalasia and other esophageal motility disorders, gastric outlet obstruction, cyclic vomiting syndrome, functional vomiting, supragastric belching, aerophagia, eating disorders involving intentional purging, and structural or neurologic disease. Rumination is tightly meal-linked, usually effortless, and behaviorally generated; vomiting usually involves nausea, autonomic symptoms, and retching. Supragastric belching involves rapid air influx/expulsion rather than gastric food return. Contemporary GERD experts note that rumination and supragastric belching are often misdiagnosed as reflux hypersensitivity and recommend CBT for rumination. (arguero2024pathophysiologyofgastrooesophageal pages 9-10)

There is no population screening, newborn screening, carrier screening, or asymptomatic genetic testing program.

## 11. Outcome and prognosis

Rumination disorder is generally treatable, especially when recognized and addressed behaviorally. It is not known to reduce life expectancy directly, and disease-specific 5- or 10-year survival statistics are not applicable. Severe untreated disease can nevertheless cause weight loss, poor growth, malnutrition, dehydration, electrolyte disturbance, dental erosion, esophageal irritation, repeated investigations, tube feeding, hospitalization, and substantial educational, occupational, and social disability.

Prognosis is influenced by diagnostic delay, nutritional severity, comorbidity, patient recognition of the premonitory motor response, access to trained behavioral clinicians, and adherence to postprandial practice. No validated molecular prognostic biomarker or mortality model exists. Quantitative long-term remission and relapse rates remain limited and heterogeneous.

## 12. Treatment

### First-line behavioral treatment

Education and **diaphragmatic breathing** are first-line. The patient is taught slow abdominal breathing before or immediately after meals and at the first urge, creating a motor pattern incompatible with forceful abdominal-wall contraction. Repeated coached practice is preferable to merely providing a handout. Lyon Consensus 2.0 states that rumination requires behavioral therapy rather than acid suppression or antireflux surgery. (gyawali2024updatestothe pages 3-3)

Suggested MAXO mappings, subject to current-release validation, are **behavioral therapy**, **breathing exercise**, **diaphragmatic breathing**, **cognitive behavioral therapy**, **habit-reversal training**, **biofeedback**, **nutritional assessment**, and **enteral nutritional support** where medically necessary.

### CBT-RD/CBT-RS

Manualized CBT expands breathing training with functional analysis, awareness training, competing responses, exposure to trigger foods/situations, cognitive work, and relapse prevention. The completed MGH pilot enrolled 10 participants aged ≥10 years for 5–8 weekly sessions; PARDI change through three months was the principal outcome. A parallel Drexel record enrolled seven participants. Neither registry record supplied numerical response or adverse-event results, so efficacy percentages should not be inferred. (NCT03113682 chunk 1, NCT03062696 chunk 1)

### Biofeedback

EMG-guided biofeedback provides real-time feedback on abdominothoracic activity and teaches control after a challenge meal. The randomized participant-masked trial enrolled 24 adults and delivered three sessions in ten days, measuring regurgitations over 28 days. Registry-linked publications report that muscular control reduced regurgitation; the associated primary reports are PMID **24768808** (published January 2015; DOI: https://doi.org/10.1016/j.cgh.2014.04.018) and PMID **27185077** (published July 2016; DOI: https://doi.org/10.1038/ajg.2016.197). (NCT02214472 chunk 1)

A related 24-person trial evaluated a simplified approach not requiring patient-visible EMG guidance. (NCT02402946 chunk 1)

### Pharmacotherapy

No medication corrects an established molecular defect, and drugs are adjunctive rather than first-line.

**Baclofen**, a GABA-B receptor agonist, can reduce transient lower-esophageal-sphincter relaxations and increase gastroesophageal-junction resistance. A randomized triple-masked crossover Phase 4 study enrolled 20 adults receiving baclofen 10 mg three times daily versus placebo for two weeks; symptoms and postprandial HRIM events were compared. The linked primary publication is PMID **29206813**, published January 2018, DOI: https://doi.org/10.1038/ajg.2017.441. (NCT03113396 chunk 1) Sedation, dizziness, weakness, and nausea limit use; withdrawal after prolonged use should be avoided.

A pediatric triple-masked parallel trial, **NCT05975684**, enrolled 50 children aged 4–18 years. Baclofen 0.5 mg/kg/day up to 15 mg/day in three divided doses was added to usual behavioral care for four weeks; the primary endpoint was the proportion with vomiting no more than weekly. The study is completed, but numerical results were not present in the retrieved registry record. (NCT05975684 chunk 1)

Acid suppression treats coexisting GERD or acid-mediated injury, not the core motor habit. Antiemetics and prokinetics generally do not target the mechanism. Tricyclics or other psychotropics may be used for comorbid disorders but lack a validated rumination-specific pharmacogenomic strategy.

### Supportive care and implementation

Assess growth, hydration, electrolytes, dental health, and dietary adequacy. Severe malnutrition may require temporary oral supplements or enteral support while behavioral treatment proceeds. Multidisciplinary pediatric programs may involve gastroenterology, psychology, dietetics, nursing, and occupational/physical therapy. Antireflux surgery is inappropriate for isolated rumination and can worsen diagnostic and therapeutic burden.

### Current research

* **NCT03912636:** completed, 30 participants; compared diaphragmatic, slow deep, and normal breathing and studied cardiac vagal tone. (NCT03912636 chunk 1, NCT03912636 chunk 2)
* **NCT05975684:** completed pediatric baclofen trial, n=50; results not available in the retrieved record. (NCT05975684 chunk 1)
* **NCT06971354:** recruiting in 2025, planned n=40, comparing audiovisual/home-practice biofeedback training with placebo and follow-up to six months. This lies beyond the requested 2023–2024 priority window but represents the latest implementation study identified. (NCT06971354 chunk 1)

Gene therapy, cell therapy, RNA therapy, targeted molecular therapy, immunotherapy, and rumination-specific surgery are not applicable.

## 13. Prevention

No proven primary prevention exists because there is no established infectious, toxic, or genetic cause. Secondary prevention consists of recognizing the characteristic meal-linked pattern early, avoiding repeated low-yield investigations and inappropriate escalation of GERD therapy, and initiating breathing/behavioral treatment promptly. Tertiary prevention includes nutritional surveillance, dental care, management of coexisting GERD or psychiatric illness, and relapse-prevention practice.

There is no vaccine, chemoprophylaxis, genetic carrier screening, prenatal testing, or public-health screening program. Patient and clinician education is the most relevant public-health intervention.

## 14. Other species and natural disease

Rumination in cattle and other ruminant animals is normal cud-chewing physiology and is **not homologous to human rumination disorder**. No naturally occurring veterinary disease with validated equivalence, breed association, orthologous causal gene, or zoonotic transmission was identified. Relevant taxonomy examples such as *Bos taurus* should therefore not be annotated as disease models merely because normal rumination occurs.

## 15. Model organisms

No validated mouse, rat, zebrafish, invertebrate, cellular, organoid, iPSC, knockout, knock-in, transgenic, or humanized model recapitulates the human learned postprandial syndrome. Human experimental systems—postprandial HRIM/impedance, surface EMG, test meals, respiratory maneuvers, symptom diaries, and biofeedback—are the principal mechanistic models. They reproduce the motor event directly but are limited by small samples, referral bias, learned task performance, and imperfect generalization to everyday meals.

## Evidence synthesis and expert assessment

The central expert consensus is that rumination disorder is a **recognizable and treatable behavioral motor disorder**, not refractory acid reflux. The 2024 Lyon Consensus emphasizes behavioral therapy and avoidance of inappropriate antireflux escalation, while a 2024 Nature Reviews analysis notes frequent confusion with reflux hypersensitivity and supports CBT. (gyawali2024updatestothe pages 3-3, arguero2024pathophysiologyofgastrooesophageal pages 9-10) Primary trials converge on the same mechanism: treatment interrupts abnormal abdominal-wall/abdominothoracic activation through diaphragmatic breathing, habit reversal, or biofeedback; baclofen is a secondary option with much smaller evidence volume. (NCT03113396 chunk 1, NCT02214472 chunk 1)

The principal knowledge gaps are reliable incidence, harmonized DSM-versus-Rome prevalence, age- and sex-stratified natural history, long-term comparative treatment effectiveness, validated patient-reported outcomes, and objective predictors of relapse. Molecular genetics, omics, immunology, and animal models currently do not provide clinically actionable information.

References

1. (gyawali2024updatestothe pages 3-3): C Prakash Gyawali, Rena Yadlapati, Ronnie Fass, David Katzka, John Pandolfino, Edoardo Savarino, Daniel Sifrim, Stuart Spechler, Frank Zerbib, Mark R Fox, Shobna Bhatia, Nicola de Bortoli, Yu Kyung Cho, Daniel Cisternas, Chien-Lin Chen, Charles Cock, Albis Hani, Jose Maria Remes Troche, Yinglian Xiao, Michael F Vaezi, and Sabine Roman. Updates to the modern diagnosis of gerd: lyon consensus 2.0. Gut, 73:361-371, Sep 2024. URL: https://doi.org/10.1136/gutjnl-2023-330616, doi:10.1136/gutjnl-2023-330616. This article has 745 citations and is from a highest quality peer-reviewed journal.

2. (arguero2024pathophysiologyofgastrooesophageal pages 9-10): Julieta Argüero and Daniel Sifrim. Pathophysiology of gastro-oesophageal reflux disease: implications for diagnosis and management. Nature reviews. Gastroenterology & hepatology, 21:282-293, Jan 2024. URL: https://doi.org/10.1038/s41575-023-00883-z, doi:10.1038/s41575-023-00883-z. This article has 78 citations.

3. (NCT03113682 chunk 1):  A Study of Cognitive-Behavioral Therapy for Rumination Disorder. Drexel University. 2017. ClinicalTrials.gov Identifier: NCT03113682

4. (NCT03062696 chunk 1): Jennifer Thomas. A Pilot Study of Cognitive-Behavioral Therapy for Rumination Disorder (CBT-RD). Massachusetts General Hospital. 2017. ClinicalTrials.gov Identifier: NCT03062696

5. (NCT03912636 chunk 2):  Role of Vagal Tone in Rumination Syndrome. Queen Mary University of London. 2019. ClinicalTrials.gov Identifier: NCT03912636

6. (NCT02214472 chunk 1):  Treatment of Rumination by Biofeedback - a Randomized Controlled Trial. Hospital Universitari Vall d'Hebron Research Institute. 2013. ClinicalTrials.gov Identifier: NCT02214472

7. (NCT02402946 chunk 1):  Placebo-controlled, Randomized Trial of a Simplified Biofeedback Technique for the Treatment of Rumination. Hospital Universitari Vall d'Hebron Research Institute. 2015. ClinicalTrials.gov Identifier: NCT02402946

8. (NCT03113396 chunk 1): Prof Dr Jan Tack. Baclofen for Rumination. Universitaire Ziekenhuizen KU Leuven. 2012. ClinicalTrials.gov Identifier: NCT03113396

9. (NCT03912636 chunk 1):  Role of Vagal Tone in Rumination Syndrome. Queen Mary University of London. 2019. ClinicalTrials.gov Identifier: NCT03912636

10. (NCT05975684 chunk 1): Peter Lu. Baclofen for Children With Rumination Syndrome. Nationwide Children's Hospital. 2023. ClinicalTrials.gov Identifier: NCT05975684

11. (NCT06971354 chunk 1):  Treatment of Rumination. Hospital Universitari Vall d'Hebron Research Institute. 2025. ClinicalTrials.gov Identifier: NCT06971354

## Artifacts

- [Edison artifact artifact-00](Rumination_Disorder-deep-research-falcon_artifacts/artifact-00.md)