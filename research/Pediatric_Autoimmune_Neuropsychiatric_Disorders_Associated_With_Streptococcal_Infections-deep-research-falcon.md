---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-25T10:54:31.225400'
end_time: '2026-07-25T11:06:58.540990'
duration_seconds: 747.32
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pediatric Autoimmune Neuropsychiatric Disorders Associated with Streptococcal
    Infections
  mondo_id: ''
  category: Autoimmune
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
  path: Pediatric_Autoimmune_Neuropsychiatric_Disorders_Associated_With_Streptococcal_Infections-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pediatric Autoimmune Neuropsychiatric Disorders Associated with Streptococcal Infections
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Pediatric Autoimmune Neuropsychiatric Disorders Associated with Streptococcal Infections** covering all of the
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
- **Disease Name:** Pediatric Autoimmune Neuropsychiatric Disorders Associated with Streptococcal Infections
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Pediatric Autoimmune Neuropsychiatric Disorders Associated with Streptococcal Infections** covering all of the
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


# Pediatric Autoimmune Neuropsychiatric Disorders Associated with Streptococcal Infections (PANDAS)

## Executive summary

PANDAS is a **proposed pediatric, post-infectious neuropsychiatric syndrome** characterized by abrupt-onset obsessive-compulsive disorder (OCD) and/or tics, an episodic course, and a temporal association with group A streptococcal (GAS; *Streptococcus pyogenes*) infection. It is generally treated as a streptococcus-associated subset of pediatric acute-onset neuropsychiatric syndrome (PANS). The construct remains controversial: the clinical phenotype is recognized, but a uniquely autoimmune etiology, reliable GAS–flare relationship, and validated diagnostic biomarker have not been established in all affected children. The 2024 Delphi consensus therefore describes PANDAS as a clinical diagnosis requiring careful exclusion of neurologic, psychiatric, infectious, metabolic, and systemic autoimmune alternatives. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 1-2, wilbur2019pandaspansinchildhood pages 1-1, grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16)

The best-supported routine interventions are evidence-based OCD/tic care—especially cognitive-behavioral therapy with exposure and response prevention (CBT/ERP), cautious use of selective serotonin-reuptake inhibitors (SSRIs), and standard antibiotic treatment of **documented active GAS infection**. Long-term antibiotic prophylaxis, corticosteroids, intravenous immunoglobulin (IVIG), therapeutic plasma exchange (TPE), and other immunotherapies have inconsistent or low-certainty evidence and should not be regarded as universally established treatment. Tonsillectomy is not supported as PANDAS therapy. (wilbur2019pandaspansinchildhood pages 3-4, wilbur2019pandaspansinchildhood pages 4-4, wilbur2019pandaspansinchildhood pages 5-6, wilbur2019pandaspansinchildhood pages 4-5)

The table below summarizes the evidence hierarchy.

| Domain | Best-supported finding | Evidence type/sample | Confidence/limitation |
|---|---|---|---|
| Definition/diagnosis | PANDAS is best understood as a **clinical syndrome** within the broader PANS construct: abrupt onset OCD and/or tics, childhood onset (3 years to puberty), episodic dramatic exacerbations, temporal association with GAS infection, and neurologic abnormalities such as motor hyperactivity or choreiform movements. No definitive confirmatory test exists. Established practice: clinical diagnosis after excluding alternative neurologic/psychiatric disease. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16, grandinetti2024pediatricacuteonsetneuropsychiatric pages 1-2, wilbur2019pandaspansinchildhood pages 1-1) | 2024 Delphi consensus; prior review of working definitions | **Moderate** for use as current clinical framework; **low-to-moderate** for nosologic certainty because autoimmune causality remains debated. |
| Epidemiology | Male predominance is repeatedly reported: ~59.9% male in a 2022 systematic review and ~65% male in survey/cross-sectional data; male:female ratio reported as 3.33:1. Typical onset is prepubertal, around 6.3 years for tics and 7.4 years for OCD; children 5-12 years appear most susceptible. True incidence/prevalence remain uncertain and likely undermeasured. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 3-4, grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16) | Consensus synthesis of cross-sectional/survey/systematic-review data | **Moderate** for age/sex pattern; **low** for population incidence/prevalence due to lack of robust population-based studies. |
| Pathophysiology | Leading hypothesis: GAS triggers molecular mimicry and post-infectious neuroimmune responses. Human/in vitro data show PANDAS-associated sera/monoclonal antibodies can enhance **dopamine D1 receptor** signaling; D1R autoantibodies discriminated PANDAS/PANS cohorts from controls with ~72%, 93%, and 79.5% accuracy in separate cohorts, whereas D2R more strongly characterized Sydenham chorea. Proposed chain: recurrent GAS -> anti-GAS/anti-neuronal immunity -> dopaminergic signaling changes and basal-ganglia inflammation. (menendez2024dopaminereceptorautoantibody pages 1-2, menendez2024dopaminereceptorautoantibody pages 4-5, grandinetti2024pediatricacuteonsetneuropsychiatric pages 3-4) | Human serum/monoclonal antibody study; consensus review | **Moderate** for biologic plausibility; **low-to-moderate** for direct causality in routine patients because biomarkers are not universally validated and conflict-of-interest concerns exist in parts of the biomarker literature. |
| Biomarkers | No circulating biomarker or autoantibody panel is currently pathognomonic. The Cunningham/Moleculera panel may provide auxiliary information, but sensitivity/specificity and clinical utility remain unclear. MRI/EEG abnormalities can occur but are not diagnostic. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 8-9, grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16, wilbur2019pandaspansinchildhood pages 5-6) | Consensus statement; review evidence | **High** that no validated diagnostic biomarker exists; major limitation is poor standardization and lack of prospective validation. |
| Prognosis | Course is usually **relapsing-remitting**, but a substantial minority have chronic/progressive illness. In a Swedish PANS follow-up (n=34, median 3.3 years), 2 remitted, 20 were relapsing-remitting, and 12 had chronic-static/progressive course. Consensus synthesis states roughly one-third chronic-progressive and two-thirds relapsing-remitting; OCD (62%) and tics (50%) were common follow-up symptoms. In a prior PANDAS longitudinal cohort, 72% had at least one exacerbation, 12% had clinically significant OCD at follow-up, and 9% had chronic-progressive course. (gromark2022atwotofiveyear pages 1-2, grandinetti2024pediatricacuteonsetneuropsychiatric pages 12-13) | Longitudinal cohort studies; consensus synthesis | **Moderate** because follow-up data exist but sample sizes are small and combine PANS/PANDAS constructs. |
| Acute GAS treatment | When **active GAS infection is documented**, standard anti-streptococcal treatment is recommended; this is the most established infectious-disease intervention. Small prospective data cited in consensus report suggest OCD symptoms may rapidly improve after eradication therapy in new-onset PANDAS, but evidence base is small. Children with psychiatric symptoms but no evidence of GAS should not routinely receive antibiotics. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 12-13, wilbur2019pandaspansinchildhood pages 5-6) | Consensus/guideline-style recommendations; small prospective studies | **Moderate** for treating documented GAS infection; **low** for expecting consistent neuropsychiatric remission from antibiotics alone. |
| CBT/SSRIs | Best-supported symptomatic therapy is standard OCD care: CBT/ERP and SSRIs. Response rates appear similar to non-PANDAS pediatric OCD. Small PANDAS CBT data: n=7 with symptom improvement; 3/6 in remission at 3 months. Survey/retrospective evidence and consensus place CBT/SSRIs as first-line symptomatic treatment. (wilbur2019pandaspansinchildhood pages 3-4, wilbur2019pandaspansinchildhood pages 5-6, grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16) | Small interventional study; reviews/consensus | **Moderate** for use in practice because evidence is extrapolated from pediatric OCD and supported by small PANDAS studies. |
| Prophylactic antibiotics | Evidence is inconsistent and insufficient for routine prophylaxis. A randomized placebo-controlled crossover trial (n=37) found penicillin prophylaxis did **not** reduce exacerbation rates or tic/OCD severity; a noncontrolled 12-month study (n=23) reported 96% fewer GAS infections and 61% fewer neuropsychiatric exacerbations. Reviews and clinical guidance do **not** recommend routine prophylactic antibiotics. (wilbur2019pandaspansinchildhood pages 3-4, wilbur2019pandaspansinchildhood pages 5-6, gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20) | One randomized trial; one uncontrolled study; reviews | **Low-to-moderate** because results conflict and better-controlled data are lacking. |
| Steroids/NSAIDs | Anti-inflammatory therapy is used selectively, not as universal standard care. Retrospective evidence suggests corticosteroids shortened flares by ~3.5 weeks; consensus notes evidence for NSAIDs/steroids is scarce and they should be individualized, generally under specialist oversight. (wilbur2019pandaspansinchildhood pages 3-4, grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16, gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20) | Retrospective study; expert consensus | **Low** due to nonrandomized evidence and uncertain patient selection. |
| IVIG/PLEX | Immunomodulation remains **investigational/specialist care**. Earlier controlled trial data suggested improvement with IVIG or plasma exchange in severe cases, but a later randomized double-blind IVIG trial in 35 children found no significant difference vs placebo at 6 weeks; longer-term improvements occurred across groups and may reflect natural history. Open-label studies in PANS show improvement (e.g., 10-child 2022 trial; 2024 study of 10 boys with improved psychometric scores and reduced pro-inflammatory monocytes), but these do not resolve efficacy. PLEX retrospective severe-PANS series reported ~65% improvement at 6 months and 78% at longer follow-up. (wilbur2019pandaspansinchildhood pages 4-4, wilbur2019pandaspansinchildhood pages 4-5, NCT01281969 chunk 1, gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20) | Randomized trials plus open-label/retrospective studies | **Low-to-moderate** for efficacy; strongest limitation is placebo response, spontaneous improvement, small samples, and heterogeneity. |
| Tonsillectomy | Not supported as effective treatment. Larger retrospective/prospective studies found no meaningful differences in OCD/tic severity, GAS titers, or remission between surgery and no surgery; consensus and reviews do not recommend routine tonsillectomy/adenoidectomy for PANDAS. (wilbur2019pandaspansinchildhood pages 4-4, wilbur2019pandaspansinchildhood pages 5-6, grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16) | Retrospective and prospective observational studies | **Moderate** for concluding lack of supportive evidence; absence of randomized trials remains a limitation. |
| Genetics/familial predisposition | No monogenic cause is established. Family autoimmunity is enriched: ~20% of first-degree relatives had at least one serious autoimmune diagnosis; rheumatic fever history was reported in 3% of mothers, 1% of fathers, and 14% of grandparents in one survey synthesis. Exploratory WES in severe PANS identified variants in 11 genes (including PLCG2, NLRC4, CACNA1B, SHANK3, GRIN2A, RAG1, SYNGAP1), but these are susceptibility candidates, not diagnostic PANDAS genes. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 3-4, grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16) | Family-history surveys; exploratory WES in severe PANS | **Low-to-moderate** for susceptibility signal; **low** for clinical genetic testing utility in PANDAS today. |
| Animal models | Recurrent intranasal GAS mouse models support a mechanistic neuroimmune pathway: GAS-specific Th17 cells from NALT/tonsil-associated immunity can enter the brain, with BBB breakdown, IgG deposition, microglial activation, and loss of excitatory synaptic proteins in the absence of viable CNS bacteria. Important limitation: pathology localized strongly to olfactory-connected regions, with **no extensive basal ganglia BBB damage** observed, so model recapitulation is incomplete. (dileepan2016groupastreptococcus pages 1-2, dileepan2016groupastreptococcus pages 11-12) | Human tonsil immunology plus recurrent-GAS mouse model | **Moderate** for biologic plausibility; **low-to-moderate** for full disease fidelity to human PANDAS. |


*Table: This table summarizes the strongest currently available evidence across diagnosis, mechanisms, treatment, prognosis, genetics, and models for PANDAS. It separates routine clinical practice from investigational or hypothesis-driven areas and highlights the main limitations of the evidence base.*

## 1. Disease information

### Definition and relationship to PANS

The current working PANDAS criteria are:

1. OCD and/or a tic disorder;
2. onset between age 3 years and puberty;
3. abrupt, dramatic onset or an episodic course with sudden exacerbations;
4. temporal association between onset/exacerbation and GAS infection; and
5. neurologic abnormalities during exacerbation, particularly motor hyperactivity or choreiform movements.

PANS is broader: it requires abrupt OCD or severely restricted food intake plus acute symptoms in at least two ancillary domains, but does not require GAS. Consequently, not every PANS case is PANDAS, and tics alone satisfy the historical PANDAS framework but not the core PANS criterion. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16)

**Direct abstract quote, 2024 consensus:** “PANDAS and PANS are broad diagnoses that encompass a range of sudden-onset neuropsychiatric symptoms in children.” The authors also conclude that “more randomized and controlled trials are needed.” Publication: October 2024; DOI/URL: https://doi.org/10.3389/fimmu.2024.1420663. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 1-2)

### Identifiers and synonyms

* **Preferred label:** Pediatric autoimmune neuropsychiatric disorders associated with streptococcal infections.
* **Acronym:** PANDAS.
* **Broader/related entities:** PANS; pediatric infection-triggered autoimmune neuropsychiatric disorders (PITAND/PITANDS); post-streptococcal neuropsychiatric syndrome; autoimmune basal-ganglia encephalitis is a mechanistic description, not an interchangeable diagnosis.
* **MONDO:** No stable, independently verified PANDAS MONDO identifier was recovered in the searched disease-target resource; the entity should not be assigned an unverified code. A knowledge base may represent it provisionally under PANS/post-streptococcal autoimmune neurologic disease with an exact synonym.
* **OMIM/Orphanet:** No established Mendelian OMIM phenotype or clearly verified Orphanet disease record was identified; PANDAS is not a monogenic disorder.
* **ICD-10/ICD-11:** No unique PANDAS code is established in the evidence reviewed. Coding ordinarily uses the manifested disorder—OCD, tic disorder, anxiety, feeding disorder—and documented streptococcal infection, rather than implying a confirmed autoimmune mechanism.
* **MeSH:** Literature is generally indexed through obsessive-compulsive disorder, tic disorders, streptococcal infections, child, and autoimmune diseases rather than a consistently used dedicated heading.

The information summarized here is **aggregated disease-level evidence** from cohorts, trials, consensus documents, and mechanistic studies—not individual-patient EHR data.

## 2. Etiology, risk, and protective factors

### Causal and triggering factors

A recent GAS infection is the defining proposed trigger. GAS can be symptomatic or asymptomatic; therefore, a single positive throat swab may indicate infection or carriage, while a single elevated antistreptolysin-O (ASO) or anti-DNase-B value documents immune exposure but does not establish the date of infection or prove causation of neuropsychiatric symptoms. The hypothesized causal sequence is GAS exposure → adaptive anti-streptococcal immunity → molecular mimicry/cellular inflammation in a susceptible child → altered corticostriatal function → acute OCD/tics. This chain is biologically plausible but incompletely proven in humans. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 12-13, grandinetti2024pediatricacuteonsetneuropsychiatric pages 3-4, dileepan2016groupastreptococcus pages 1-2)

### Risk factors

* **Age:** The highest reported susceptibility is approximately 5–12 years; mean onset is about 6.3 years for tics and 7.4 years for OCD.
* **Sex:** Studies synthesized by the 2024 consensus reported 59.9–65% male and, in one cross-sectional sample, a male:female ratio of 3.33:1. These are referral/cohort estimates, not population rates.
* **Repeated GAS exposure:** Recurrent mucosal infection could amplify anti-GAS antibodies and GAS-specific Th17 memory responses.
* **Family autoimmunity:** One survey synthesis reported serious autoimmune disease in 20% of first-degree relatives; rheumatic-fever history occurred in 3% of mothers, 1% of fathers, and at least one grandparent in 14% of families.
* **Pre-existing neurodevelopmental vulnerability:** Some severe-PANS sequencing cohorts showed overlap with autism, epilepsy, or synaptic disorders, but this is not specific to PANDAS. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 3-4)

### Protective factors and gene–environment interaction

No replicated protective allele, diet, supplement, probiotic, or lifestyle intervention has been shown to prevent PANDAS. The 2024 consensus found no clinical evidence that probiotics prevent relapses. Ordinary infection-control measures and timely guideline-based treatment of confirmed GAS are reasonable, but they have not been proven to prevent the syndrome. The proposed gene–environment model is **polygenic/heterogeneous susceptibility plus childhood GAS exposure**, rather than Mendelian inheritance. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 12-13)

## 3. Phenotypes

The hallmark is a change from baseline over approximately 24–48 hours, rather than ordinary gradual development of childhood OCD or tics. Severity ranges from mild impairment to inability to attend school, eat, sleep independently, or perform activities of daily living.

| Phenotype | Characteristics and suggested HPO annotation |
|---|---|
| OCD | Core symptom; abrupt contamination fears, checking, intrusive thoughts, reassurance seeking, or rituals. **HP:0000722 Obsessive-compulsive behavior**. |
| Motor/vocal tics | Core historical criterion; episodic and fluctuating. **HP:0100033 Tics**. |
| Choreiform movements | Fine “piano-playing” finger/toe movements may occur; frank chorea requires evaluation for Sydenham chorea. **HP:0002072 Chorea**. |
| Anxiety/separation anxiety | Frequently acute and disabling. **HP:0000739 Anxiety**; separation anxiety lacks a sufficiently specific universally used HPO term. |
| Emotional lability/irritability/aggression | Abrupt mood swings, rage, oppositional behavior. **HP:0000712 Emotional lability**, **HP:0000737 Irritability**. |
| Behavioral/developmental regression | Baby talk, loss of independence, clinginess. **HP:0002376 Developmental regression**. |
| Restricted eating | Often contamination, choking, vomiting, or sensory driven; more central to PANS than historical PANDAS. **HP:0004395 Malnutrition** or **HP:0008872 Feeding difficulties** where clinically applicable. |
| Cognitive/school decline | Attention, working memory, graphomotor and handwriting deterioration. **HP:0007018 Attention deficit**, **HP:0002354 Memory impairment**. |
| Sensory/motor abnormalities | Sensory hypersensitivity, restlessness, clumsiness. **HP:0000733 Stereotypic behavior** only where appropriate; record the specific sensory modality rather than overgeneralizing. |
| Sleep disturbance | Insomnia, night waking, altered sleep schedule. **HP:0100785 Insomnia**. |
| Urinary symptoms | Frequency, urgency, and new enuresis. **HP:0000017 Nocturnal enuresis**, **HP:0000015 Bladder dysfunction**. |
| Somatic symptoms | Fatigue, pain, headache, and autonomic complaints are reported but nonspecific. **HP:0012378 Fatigue**, **HP:0002315 Headache**. |

In a Swedish cohort followed for a median 3.3 years, follow-up symptoms included OCD in 62%, tics in 50%, anxiety and hyperactivity/impulsivity in 35% each, behavioral difficulties in 32%, and sleep disturbance, depression, and fatigue in 29% each. Acute symptoms can severely impair school attendance, family functioning, nutrition, sleep, and independence. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 12-13, gromark2022atwotofiveyear pages 1-2)

## 4. Genetic and molecular information

There is **no established causal PANDAS gene, pathogenic variant class, chromosomal abnormality, inheritance pattern, carrier frequency, or clinically indicated PANDAS gene panel**. Therefore, ACMG classification, penetrance, anticipation, mosaicism, founder effects, and variant-specific population frequencies are not applicable at present.

Exploratory exome sequencing in 386 US and 10 European severe-PANS cases reported variants across **PPM1D, SGCE, PLCG2, NLRC4, CACNA1B, SHANK3, CHEK2/CHK2, GRIN2A, RAG1, GABRG2, and SYNGAP1**. These genes span immune/microglial regulation and neuronal synaptic function. They should be regarded as heterogeneous candidate findings—not validated PANDAS genes and not evidence that variants in these genes caused PANDAS. Approximately 50% of that severe cohort had overlap with a pre-existing neurodevelopmental condition, creating substantial ascertainment and interpretation issues. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 3-4)

No reproducible PANDAS-specific DNA-methylation, histone, chromatin, structural-genomic, or germline-versus-somatic signature is established. WES/WGS/CMA should be reserved for conventional indications such as developmental delay, epilepsy, dysmorphism, intellectual disability, or a strong monogenic-disease suspicion—not used to confirm PANDAS.

## 5. Environmental and infectious information

The relevant infectious agent is **GAS, *Streptococcus pyogenes*** (NCBI Taxonomy: 1314). Pharyngitis, scarlet fever, skin infection, household/classroom exposure, and asymptomatic carriage are possible contexts. Other infections are relevant principally to the broader PANS differential, not to strict PANDAS. No credible association with smoking, alcohol, occupational exposure, radiation, pollution, toxin, exercise, or a particular diet is established.

Psychosocial stress may aggravate symptoms or perpetuate functional impairment but is not a demonstrated primary cause. Gut/oral microbiome and oxidative-stress hypotheses remain exploratory; they do not support commercial microbiome testing or probiotic treatment as established PANDAS care. (matera2025pediatricacuteonsetneuropsychiatric pages 2-3, grandinetti2024pediatricacuteonsetneuropsychiatric pages 12-13)

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. **Upstream trigger:** repeated GAS infection activates tonsillar/nasopharyngeal B- and T-cell responses.
2. **Molecular mimicry:** antibodies against the GAS group-A carbohydrate epitope N-acetyl-β-D-glucosamine (GlcNAc) may cross-react with neuronal antigens and dopamine receptors.
3. **Neurovascular access:** GAS-specific Th17 cells and cytokines—especially IL-17A—may impair endothelial tight junctions and blood–brain barrier (BBB) integrity.
4. **Central inflammation:** entry of lymphocytes and IgG can activate microglia and alter synaptic proteins.
5. **Circuit dysfunction:** D1/D2 dopamine-receptor signaling and cortico-striato-thalamo-cortical circuits become dysregulated, producing OCD, tics, affective lability, and movement abnormalities.

This sequence integrates human serology/in-vitro signaling and animal data; it is not yet a universally demonstrated causal pathway in patients. (menendez2024dopaminereceptorautoantibody pages 1-2, menendez2024dopaminereceptorautoantibody pages 4-5, dileepan2016groupastreptococcus pages 11-12, dileepan2016groupastreptococcus pages 1-2)

### 2024 dopamine-receptor study

Menendez et al., published September 26, 2024 in *JCI Insight*, found that patient serum antibodies and patient-derived monoclonal antibodies activated D1-receptor G-protein and β-arrestin signaling and enhanced dopamine-mediated signaling. D1R-antibody ROC accuracy for distinguishing PANDAS/PANS from controls was 72% in one cohort, 93% in a well-characterized PANDAS cohort without choreiform movements, and 79.5% in the largest combined cohort. D2R antibodies better characterized Sydenham chorea. These results support biological plausibility but do not by themselves validate a clinical diagnostic assay; the paper also reports a relevant commercial conflict of interest involving an author and Moleculera Biosciences. DOI/URL: https://doi.org/10.1172/jci.insight.164762. (menendez2024dopaminereceptorautoantibody pages 1-2, menendez2024dopaminereceptorautoantibody pages 4-5)

**Direct abstract quote:** “Our findings suggest that AAb-mediated D1R signaling may contribute to the pathogenesis of neuropsychiatric sequelae.” The wording “may contribute” is important: it does not establish necessity, specificity, or population-wide causality. (menendez2024dopaminereceptorautoantibody pages 1-2)

### Th17–BBB–microglial evidence

In recurrent intranasal GAS-exposed mice, GAS-specific Th17 cells migrated from nasal-associated lymphoid tissue into brain regions, accompanied by BBB breakdown, IgG deposition, microglial activation, and loss of excitatory synaptic proteins despite absence of viable bacteria in CNS tissue. Human tonsils from 28 naturally exposed individuals contained GAS-responsive IL-17A-producing CD4 T cells. However, mouse pathology was concentrated in olfactory-connected regions and did **not** show extensive basal-ganglia BBB damage, limiting fidelity to human PANDAS. Publication: *Journal of Clinical Investigation*, January 2016; DOI: https://doi.org/10.1172/JCI80792; PMID 26690792. (dileepan2016groupastreptococcus pages 11-12, dileepan2016groupastreptococcus pages 1-2)

Suggested ontology mappings include **GO:0006955 immune response**, **GO:0006954 inflammatory response**, **GO:0034341 response to interferon-gamma**, **GO:0071346 cellular response to interferon-gamma**, **GO:0007165 signal transduction**, **GO:0007268 chemical synaptic transmission**, and **GO:0001525 angiogenesis** only where directly measured. Relevant cell types are **CL:0000899 T-helper 17 cell**, **CL:0000129 microglial cell**, **CL:0000115 endothelial cell**, **CL:0000236 B cell**, and dopaminergic neurons. Relevant chemicals include dopamine (**CHEBI:18243**) and IL-17A as a protein entity rather than a CHEBI chemical.

### Molecular profiling

Current profiling is small-scale rather than diagnostic. Reported findings include inflammatory cytokines, activated myeloid populations, receptor autoantibodies, and imaging changes. No replicated clinical transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omic signature can diagnose human PANDAS. A 2024 open-label IVIG study of ten boys found reduced pro-inflammatory monocytes/dendritic cells alongside improved psychiatric scores, but without a control group it cannot distinguish treatment effect from time, regression to the mean, or concomitant care.

## 7. Anatomical structures affected

The hypothesized primary system is the **central nervous system**, especially cortico-striato-thalamo-cortical circuitry:

* basal ganglia/striatum—caudate nucleus and putamen;
* thalamus;
* amygdala and connected limbic circuitry;
* frontal cortical networks;
* cerebral microvascular endothelium/BBB; and
* microglia and dopaminergic synapses.

A study of 34 PANS patients showed increased diffusion measures, particularly in deep gray matter including thalamus, basal ganglia, and amygdala. PET research has suggested bilateral caudate neuroinflammation, but imaging is neither specific nor required. No consistent lateralization is established. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 8-9, grandinetti2024pediatricacuteonsetneuropsychiatric pages 3-4)

Suggested terms: **UBERON:0002420 basal ganglion**, **UBERON:0001873 caudate nucleus**, **UBERON:0001874 putamen**, **UBERON:0001897 dorsal plus ventral thalamus**, **UBERON:0001876 amygdala**, **UBERON:0000120 blood-brain barrier**; **GO:0005886 plasma membrane**, **GO:0005911 cell-cell junction**, and **GO:0045202 synapse**.

## 8. Temporal development

Onset is pediatric and classically explosive, often progressing from absent/minimal symptoms to maximum severity within 24–48 hours. The subsequent course may be monophasic, relapsing-remitting, chronic-static, or progressive.

In 33 longitudinally followed PANDAS patients, 72% experienced at least one later exacerbation, 12% had clinically significant OCD at follow-up, and 9% had a chronic-progressive course. In the 34-patient Swedish PANS cohort, followed for 2–5 years (median 3.3), two remitted, 20 were relapsing-remitting, and 12 were chronic-static/progressive. Earlier onset and greater baseline impairment characterized the latter group. Complete remission was uncommon, although mean symptom severity and functioning improved. DOI: https://doi.org/10.1007/s10578-021-01135-4; PMID 33547531. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 12-13, gromark2022atwotofiveyear pages 1-2)

There is no validated disease staging system. “Flare” generally means a clinically meaningful exacerbation lasting at least 24 hours, although studies use inconsistent definitions. Early intervention is important for nutrition, suicidality, school loss, family accommodation, and functional decline, but no proven immunologic “critical window” has been established.

## 9. Inheritance and population epidemiology

PANDAS is best considered **multifactorial**, with incomplete and undefined susceptibility rather than autosomal dominant, recessive, X-linked, or mitochondrial inheritance. Penetrance, carrier frequency, anticipation, consanguinity effects, and founder mutations are unknown/not applicable.

True incidence and prevalence per 100,000 are **not established**. Available studies are affected by referral bias, inconsistent criteria, retrospective attribution of GAS exposure, asymptomatic carriage, and overlap with common childhood OCD/tic disorders. Reported male predominance and prepubertal onset are more reliable than any population prevalence estimate. Large-scale prospective population studies are explicitly needed. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 3-4)

No robust ethnic or geographic predilection is established. Apparent geographic variation is likely influenced by GAS circulation, rheumatic-fever epidemiology, referral practices, awareness, and access to specialty clinics.

## 10. Diagnostics

### Clinical approach

PANDAS is a **diagnosis of pattern plus exclusion**, not a positive laboratory diagnosis. Evaluation should document exact onset chronology, prior baseline, OCD/tic phenomenology, functional change, infections and exposures, medication/substance history, neurologic examination, psychiatric risk, family autoimmunity, and developmental history.

### GAS testing

During a compatible acute presentation, obtain a properly collected throat swab with rapid antigen/NAAT and/or culture according to local guidelines. Skin culture is appropriate when lesions are present. ASO and anti-DNase-B titers can support preceding GAS exposure, especially when paired acute/convalescent titers rise, but a single titer cannot date infection or establish that GAS caused the psychiatric syndrome. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16)

### Additional tests

CBC, metabolic panel, inflammatory markers, thyroid studies, urinalysis, toxicology, autoimmune testing, infectious studies, EEG, MRI, CSF, or metabolic/genetic tests should be **clinically targeted**, not applied as a universal commercial panel. MRI is most appropriate for focal deficits, severe headache, cognitive decline, psychosis, or suspected encephalitis/vasculitis. EEG may be useful for seizures or encephalopathy; abnormalities were reported in 7/42 PANDAS patients (16%), but are nonspecific. Lumbar puncture is appropriate when altered consciousness, seizures, psychosis, MRI/EEG abnormalities, or autoimmune/infectious encephalitis is suspected. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 8-9)

### Biomarkers

No pathognomonic antibody exists. The commercial Cunningham/Autoimmune Brain Panel measures anti-D1R, anti-D2R, anti-β-tubulin, anti-lysoganglioside antibodies and CaMKII activity, but pediatric sensitivity, specificity, predictive value, interlaboratory reproducibility, and added clinical utility remain insufficiently established. It should not independently diagnose PANDAS or determine immunotherapy. (wilbur2019pandaspansinchildhood pages 3-4, grandinetti2024pediatricacuteonsetneuropsychiatric pages 8-9)

### Differential diagnosis

Priority exclusions include ordinary pediatric OCD, Tourette/chronic tic disorders, anxiety, autism-related rigidity, ADHD, eating disorders/ARFID, medication or stimulant effects, seizures, autoimmune encephalitis including anti-NMDA-receptor encephalitis, Sydenham chorea/acute rheumatic fever, systemic lupus/vasculitis, thyroid disease, Wilson disease, post-infectious encephalopathy, CNS infection, and functional neurologic disorder. Red flags—encephalopathy, seizures, persistent focal deficits, frank chorea, autonomic instability, psychosis, catatonia, fever, or systemic inflammation—require urgent neurologic/infectious/autoimmune evaluation rather than presumptive PANDAS treatment.

There is no asymptomatic population, newborn, prenatal, carrier, or genetic screening program.

## 11. Outcome and prognosis

PANDAS is not known to shorten life expectancy, and disease-specific mortality rates are unavailable. Its burden is morbidity: severe anxiety/OCD, nutritional compromise, family disruption, school absence, loss of independence, sleep disturbance, and occasionally suicidality or aggression.

Most longitudinally observed children improve, but relapse is common and a minority remain chronically impaired. In the Swedish follow-up, only 15% retained clinically significant OCD despite rare complete remission; 38% received a new neurodevelopmental diagnosis, including ADHD in 26%, autism in 9%, and intellectual disability in 3%. These findings may reflect recognition of pre-existing vulnerabilities rather than PANDAS causing those disorders. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 12-13)

No validated prognostic biomarker exists. Earlier onset, greater baseline impairment, frequent/prolonged flares, comorbid neurodevelopmental disease, and delayed access to effective psychiatric/supportive care may predict a more difficult course, but models require prospective validation.

## 12. Treatment and real-world implementation

### Practical hierarchy

**1. Stabilize and treat the phenotype.** Assess suicidality, aggression, dehydration, malnutrition, sleep loss, and inability to function. Use CBT/ERP, family-based behavioral support, school accommodations, and cautious psychiatric pharmacotherapy. Small PANDAS CBT data showed improvement in seven children and remission in 3/6 assessed at three months; broader pediatric OCD evidence is much stronger. SSRIs are generally started low and titrated slowly because behavioral activation is a concern in acutely ill children. (wilbur2019pandaspansinchildhood pages 3-4, wilbur2019pandaspansinchildhood pages 5-6)

Suggested MAXO mappings: **MAXO:0000073 cognitive behavioral therapy** where available in the implementation ontology; exposure/response prevention should be retained as a textual subtype; medication administration and psychiatric assessment should use the corresponding current MAXO release terms after validation.

**2. Treat documented GAS normally.** Use guideline-concordant penicillin/amoxicillin or an appropriate alternative based on allergy and local recommendations. Children without evidence of bacterial infection should not automatically receive antibiotics. A small 12-child prospective series reported rapid OCD improvement after GAS eradication, but sample size and lack of controls preclude firm neuropsychiatric efficacy conclusions. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 12-13)

**3. Do not assume prophylaxis works.** In an n=37 randomized crossover study, penicillin prophylaxis did not reduce exacerbations or tic/OCD severity. An uncontrolled n=23 study reported 96% fewer GAS infections and 61% fewer neuropsychiatric exacerbations on penicillin or azithromycin; without placebo control, causality is uncertain. Routine prophylaxis is therefore not supported, although specialists may individualize decisions in exceptional recurrent, well-documented GAS-linked cases. (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20, wilbur2019pandaspansinchildhood pages 3-4)

**4. Anti-inflammatory treatment is selective.** A retrospective n=98 analysis associated corticosteroids with flares shorter by approximately 3.5 weeks. NSAIDs and short steroid courses are used by specialty programs, but randomized evidence is inadequate. Infection, metabolic, psychiatric, and bone/gastrointestinal risks must be considered. (wilbur2019pandaspansinchildhood pages 3-4)

**5. IVIG/TPE remain specialist or investigational interventions.** The early n=30 trial found significant one-month improvement with IVIG or TPE versus placebo. A later randomized double-blind study of 35 children found no significant IVIG–placebo response difference at six weeks, despite substantial later improvement across groups. The NIH phase-3 study, NCT01281969, enrolled 48 participants and tested IVIG 2 g/kg over two days against saline with CY-BOCS at six weeks; the registry itself acknowledges insufficient prior evidence. (NCT01281969 chunk 1, wilbur2019pandaspansinchildhood pages 4-4, wilbur2019pandaspansinchildhood pages 4-5)

Open-label evidence remains hypothesis-generating. A 2024 study of ten male PANS patients receiving six IVIG infusions reported improvement on all psychometric scales and reductions in inflammatory monocytes, but lacked a control group. TPE retrospective data in 35 severe patients reported approximately 65% improvement at six months and 78% at longer follow-up. IVIG risks include headache, aseptic meningitis, hemolysis, thrombosis, renal injury, and infusion reactions; TPE requires central access in many children and carries bleeding, infection, hypotension, electrolyte, and line-related risks. (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20)

**6. Other immunotherapies and surgery.** Rituximab and mycophenolate lack adequate PANDAS trial evidence. Two larger tonsillectomy studies—retrospective n=43 and prospective n=120, including 56 surgical patients—found no meaningful benefit in OCD/tics, GAS titers, or remission. Tonsillectomy should be performed only for ordinary otolaryngologic indications, not solely for PANDAS. (wilbur2019pandaspansinchildhood pages 4-4)

### Selected clinical trials

* **NCT01617083:** completed randomized double-blind 4-week azithromycin-versus-placebo trial followed by 8-week open-label treatment; 47 enrolled. Primary outcome: CY-BOCS. The trial was explicitly designed because earlier antibiotic studies were small and mixed. (NCT01617083 chunk 1)
* **NCT01281969:** completed NIH randomized, quadruple-masked phase-3 IVIG trial; 48 enrolled; IVIG 2 g/kg over two days versus saline. (NCT01281969 chunk 1)
* Registry searches also identified ongoing observational biomarker/natural-history programs, emphasizing that current development is focused more on patient stratification and biomarkers than on a validated targeted therapy.

There is no established pharmacogenomic, gene, cell, RNA, or genotype-guided therapy for PANDAS.

## 13. Prevention

* **Primary:** No PANDAS vaccine exists. Apply ordinary GAS prevention—hand hygiene, respiratory etiquette, avoidance of sharing utensils during infection, and appropriate evaluation of symptomatic close contacts. GAS vaccination remains investigational generally.
* **Secondary:** Promptly assess abrupt OCD/tics, document infection objectively, and treat confirmed GAS according to standard guidelines. There is no evidence-based screening of asymptomatic children or relatives.
* **Tertiary:** Maintain relapse plans, CBT/ERP skills, school accommodations, nutrition/sleep support, and rapid reassessment for documented infection or neurologic red flags.
* **Not established:** routine antibiotic prophylaxis, probiotics, tonsillectomy, dietary regimens, supplements, or pre-emptive immunotherapy. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 12-13, wilbur2019pandaspansinchildhood pages 5-6)

Genetic counseling is not routinely required because there is no Mendelian PANDAS genotype. Families should instead receive empiric counseling that familial autoimmune/neuropsychiatric clustering may indicate susceptibility but does not predict deterministic transmission.

## 14. Other species and natural disease

No recognized naturally occurring PANDAS-equivalent disease has been established in companion animals, livestock, or wildlife. PANDAS itself is not zoonotic and is not transmitted as a neuropsychiatric syndrome. GAS is a human-adapted pathogen; the relevant cross-species work consists of induced laboratory models rather than natural veterinary disease. Consequently, breed ontology, veterinary carrier frequency, and natural-disease ortholog annotations are not applicable.

## 15. Model organisms

### Recurrent intranasal GAS mouse model

Repeated intranasal GAS exposure expands GAS-specific Th17 cells in nasal-associated lymphoid tissue and produces CNS T-cell entry, BBB disruption, IgG deposition, microglial activation, and reduced excitatory synaptic proteins without viable CNS bacteria. It is useful for studying mucosal immunity, IL-17A, neurovascular permeability, and antibody access to brain. Its principal limitation is that injury predominates in olfactory-connected regions rather than showing extensive basal-ganglia pathology, and murine NALT is not anatomically identical to human tonsils/adenoids. (dileepan2016groupastreptococcus pages 11-12, dileepan2016groupastreptococcus pages 1-2)

### GAS-antigen rat and transgenic antibody models

Lewis rats immunized with GAS antigens develop abnormal movements/repetitive behavior, anti-neuronal antibodies, and antibody deposition in striatum, thalamus, and frontal cortex; some behavioral effects were alleviated by the D2 antagonist haloperidol. Transgenic mouse B cells expressing human Sydenham-chorea monoclonal-antibody variable genes produce antineuronal antibodies targeting dopaminergic basal-ganglia neurons. These models support molecular mimicry and receptor signaling, but more closely overlap Sydenham chorea/basal-ganglia encephalitis than the full heterogeneous PANDAS phenotype. (menendez2024dopaminereceptorautoantibody pages 1-2)

No validated zebrafish, *Drosophila*, *C. elegans*, organoid, iPSC, or naturally occurring genetic model recapitulates the complete syndrome.

## Overall expert assessment and knowledge-base recommendation

PANDAS should be represented as a **clinically defined, GAS-associated acute-onset pediatric neuropsychiatric syndrome with disputed autoimmune specificity**, not as a proven monogenic autoimmune encephalitis. The knowledge base should distinguish:

* **established:** abrupt phenotype, need for differential diagnosis, treatment of confirmed GAS, CBT/ERP and standard psychiatric care;
* **supported but unvalidated:** molecular mimicry, D1R autoantibody signaling, Th17/BBB/microglial pathways, basal-ganglia involvement;
* **investigational/low certainty:** commercial antibody panels, antibiotic prophylaxis, steroids/NSAIDs as disease modification, IVIG, TPE, and other immunosuppression;
* **not supported as PANDAS-specific care:** tonsillectomy, probiotics, unvalidated diets/supplements, or routine genetic testing.

This cautious classification reflects the authoritative literature’s central conclusion: biologically plausible neuroimmune mechanisms and severely affected patients coexist with small samples, inconsistent criteria, spontaneous fluctuation, referral bias, and few adequately powered randomized trials. (wilbur2019pandaspansinchildhood pages 3-3, grandinetti2024pediatricacuteonsetneuropsychiatric pages 1-2, wilbur2019pandaspansinchildhood pages 5-6, wilbur2019pandaspansinchildhood pages 1-1)

References

1. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 1-2): Roberto Grandinetti, Nicole Mussi, Simone Pilloni, Greta Ramundo, Angela Miniaci, Emanuela Turco, Benedetta Piccolo, Maria Elena Capra, Roberta Forestiero, Serena Laudisio, Giovanni Boscarino, Laura Pedretti, Martina Menoni, Giuditta Pellino, Silvia Tagliani, Andrea Bergomi, Francesco Antodaro, Maria Cristina Cantù, Maria Teresa Bersini, Sandra Mari, Franco Mazzini, Giacomo Biasucci, Agnese Suppiej, and Susanna Esposito. Pediatric acute-onset neuropsychiatric syndrome and pediatric autoimmune neuropsychiatric disorder associated with streptococcal infections: a delphi study and consensus document about definition, diagnostic criteria, treatment and follow-up. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1420663, doi:10.3389/fimmu.2024.1420663. This article has 15 citations and is from a peer-reviewed journal.

2. (wilbur2019pandaspansinchildhood pages 1-1): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

3. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16): Roberto Grandinetti, Nicole Mussi, Simone Pilloni, Greta Ramundo, Angela Miniaci, Emanuela Turco, Benedetta Piccolo, Maria Elena Capra, Roberta Forestiero, Serena Laudisio, Giovanni Boscarino, Laura Pedretti, Martina Menoni, Giuditta Pellino, Silvia Tagliani, Andrea Bergomi, Francesco Antodaro, Maria Cristina Cantù, Maria Teresa Bersini, Sandra Mari, Franco Mazzini, Giacomo Biasucci, Agnese Suppiej, and Susanna Esposito. Pediatric acute-onset neuropsychiatric syndrome and pediatric autoimmune neuropsychiatric disorder associated with streptococcal infections: a delphi study and consensus document about definition, diagnostic criteria, treatment and follow-up. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1420663, doi:10.3389/fimmu.2024.1420663. This article has 15 citations and is from a peer-reviewed journal.

4. (wilbur2019pandaspansinchildhood pages 3-4): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

5. (wilbur2019pandaspansinchildhood pages 4-4): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

6. (wilbur2019pandaspansinchildhood pages 5-6): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

7. (wilbur2019pandaspansinchildhood pages 4-5): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

8. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 3-4): Roberto Grandinetti, Nicole Mussi, Simone Pilloni, Greta Ramundo, Angela Miniaci, Emanuela Turco, Benedetta Piccolo, Maria Elena Capra, Roberta Forestiero, Serena Laudisio, Giovanni Boscarino, Laura Pedretti, Martina Menoni, Giuditta Pellino, Silvia Tagliani, Andrea Bergomi, Francesco Antodaro, Maria Cristina Cantù, Maria Teresa Bersini, Sandra Mari, Franco Mazzini, Giacomo Biasucci, Agnese Suppiej, and Susanna Esposito. Pediatric acute-onset neuropsychiatric syndrome and pediatric autoimmune neuropsychiatric disorder associated with streptococcal infections: a delphi study and consensus document about definition, diagnostic criteria, treatment and follow-up. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1420663, doi:10.3389/fimmu.2024.1420663. This article has 15 citations and is from a peer-reviewed journal.

9. (menendez2024dopaminereceptorautoantibody pages 1-2): Chandra M. Menendez, Jonathan Zuccolo, Susan E. Swedo, Sean Reim, Brian Richmand, Hilla Ben-Pazi, Abraham Kovoor, and Madeleine W. Cunningham. Dopamine receptor autoantibody signaling in infectious sequelae differentiates movement versus neuropsychiatric disorders. JCI Insight, Nov 2024. URL: https://doi.org/10.1172/jci.insight.164762, doi:10.1172/jci.insight.164762. This article has 19 citations and is from a domain leading peer-reviewed journal.

10. (menendez2024dopaminereceptorautoantibody pages 4-5): Chandra M. Menendez, Jonathan Zuccolo, Susan E. Swedo, Sean Reim, Brian Richmand, Hilla Ben-Pazi, Abraham Kovoor, and Madeleine W. Cunningham. Dopamine receptor autoantibody signaling in infectious sequelae differentiates movement versus neuropsychiatric disorders. JCI Insight, Nov 2024. URL: https://doi.org/10.1172/jci.insight.164762, doi:10.1172/jci.insight.164762. This article has 19 citations and is from a domain leading peer-reviewed journal.

11. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 8-9): Roberto Grandinetti, Nicole Mussi, Simone Pilloni, Greta Ramundo, Angela Miniaci, Emanuela Turco, Benedetta Piccolo, Maria Elena Capra, Roberta Forestiero, Serena Laudisio, Giovanni Boscarino, Laura Pedretti, Martina Menoni, Giuditta Pellino, Silvia Tagliani, Andrea Bergomi, Francesco Antodaro, Maria Cristina Cantù, Maria Teresa Bersini, Sandra Mari, Franco Mazzini, Giacomo Biasucci, Agnese Suppiej, and Susanna Esposito. Pediatric acute-onset neuropsychiatric syndrome and pediatric autoimmune neuropsychiatric disorder associated with streptococcal infections: a delphi study and consensus document about definition, diagnostic criteria, treatment and follow-up. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1420663, doi:10.3389/fimmu.2024.1420663. This article has 15 citations and is from a peer-reviewed journal.

12. (gromark2022atwotofiveyear pages 1-2): Caroline Gromark, Eva Hesselmark, Ida Gebel Djupedal, Maria Silverberg, AnnaCarin Horne, Robert A. Harris, Eva Serlachius, and David Mataix-Cols. A two-to-five year follow-up of a pediatric acute-onset neuropsychiatric syndrome cohort. Child Psychiatry and Human Development, 53:354-364, Feb 2022. URL: https://doi.org/10.1007/s10578-021-01135-4, doi:10.1007/s10578-021-01135-4. This article has 58 citations and is from a peer-reviewed journal.

13. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 12-13): Roberto Grandinetti, Nicole Mussi, Simone Pilloni, Greta Ramundo, Angela Miniaci, Emanuela Turco, Benedetta Piccolo, Maria Elena Capra, Roberta Forestiero, Serena Laudisio, Giovanni Boscarino, Laura Pedretti, Martina Menoni, Giuditta Pellino, Silvia Tagliani, Andrea Bergomi, Francesco Antodaro, Maria Cristina Cantù, Maria Teresa Bersini, Sandra Mari, Franco Mazzini, Giacomo Biasucci, Agnese Suppiej, and Susanna Esposito. Pediatric acute-onset neuropsychiatric syndrome and pediatric autoimmune neuropsychiatric disorder associated with streptococcal infections: a delphi study and consensus document about definition, diagnostic criteria, treatment and follow-up. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1420663, doi:10.3389/fimmu.2024.1420663. This article has 15 citations and is from a peer-reviewed journal.

14. (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20): Antonella Gagliano, Alessandra Carta, Marcello G Tanca, and Stefano Sotgiu. Pediatric acute-onset neuropsychiatric syndrome: current perspectives. Neuropsychiatric Disease and Treatment, 19:1221-1250, May 2023. URL: https://doi.org/10.2147/ndt.s362202, doi:10.2147/ndt.s362202. This article has 60 citations and is from a peer-reviewed journal.

15. (NCT01281969 chunk 1):  Intravenous Immunoglobulin for PANDAS. National Institute of Mental Health (NIMH). 2011. ClinicalTrials.gov Identifier: NCT01281969

16. (dileepan2016groupastreptococcus pages 1-2): Thamotharampillai Dileepan, Erica D. Smith, Daniel Knowland, Martin Hsu, Maryann Platt, Peter Bittner-Eddy, Brenda Cohen, Peter Southern, Elizabeth Latimer, Earl Harley, Dritan Agalliu, and P. Patrick Cleary. Group a streptococcus intranasal infection promotes cns infiltration by streptococcal-specific th17 cells. The Journal of clinical investigation, 126 1:303-17, Dec 2016. URL: https://doi.org/10.1172/jci80792, doi:10.1172/jci80792. This article has 173 citations.

17. (dileepan2016groupastreptococcus pages 11-12): Thamotharampillai Dileepan, Erica D. Smith, Daniel Knowland, Martin Hsu, Maryann Platt, Peter Bittner-Eddy, Brenda Cohen, Peter Southern, Elizabeth Latimer, Earl Harley, Dritan Agalliu, and P. Patrick Cleary. Group a streptococcus intranasal infection promotes cns infiltration by streptococcal-specific th17 cells. The Journal of clinical investigation, 126 1:303-17, Dec 2016. URL: https://doi.org/10.1172/jci80792, doi:10.1172/jci80792. This article has 173 citations.

18. (matera2025pediatricacuteonsetneuropsychiatric pages 2-3): Mariarosaria Matera, Valentina Biagioli, Maria Teresa Illiceto, Chiara Maria Palazzi, Ilaria Cavecchia, Andrea Manzi, Sebastian Lugli, Laura Pennazzi, Martina Meocci, Fausto Andrea Pedaci, and Alexander Bertuccioli. Pediatric acute-onset neuropsychiatric syndromes and the gut-oral-brain axis: a narrative review of emerging microbiome-immune interactions and therapeutic perspectives. Frontiers in Immunology, Nov 2025. URL: https://doi.org/10.3389/fimmu.2025.1726630, doi:10.3389/fimmu.2025.1726630. This article has 6 citations and is from a peer-reviewed journal.

19. (NCT01617083 chunk 1):  Antibiotic Treatment Trial for the PANDAS/PANS Phenotype. University of South Florida. 2012. ClinicalTrials.gov Identifier: NCT01617083

20. (wilbur2019pandaspansinchildhood pages 3-3): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Pediatric_Autoimmune_Neuropsychiatric_Disorders_Associated_With_Streptococcal_Infections-deep-research-falcon_artifacts/artifact-00.md)