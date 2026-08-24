---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-05T21:45:36.965520'
end_time: '2026-08-05T21:56:55.580867'
duration_seconds: 678.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: FG Syndrome 4
  mondo_id: ''
  category: Mendelian
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
  path: FG_Syndrome_4-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FG Syndrome 4
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FG Syndrome 4** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
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
- **Disease Name:** FG Syndrome 4
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FG Syndrome 4** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# FG Syndrome 4: Disease Characteristics Research Report

**Scope and critical curation note.** FG syndrome 4 (FGS4) is an exceptionally sparsely documented historical FG-syndrome subtype. Current disease databases map it to **MONDO:0010318** and associate it with **CASK**. However, most modern clinical and mechanistic evidence concerns the broader spectrum of **CASK-related disorders**, not cohorts explicitly diagnosed as FGS4. Accordingly, this report labels evidence as either **direct FGS4 evidence** or **broader CASK-spectrum evidence**; frequencies from the latter should not be entered as FGS4-specific frequencies without qualification. Open Targets identifies CASK as the sole associated target, with an association score of 0.80 and predominantly genetic support. (OpenTargets Search: FG syndrome 4)

| Domain | FG syndrome 4-specific finding | Broader CASK-spectrum context (clearly labeled) | Suggested ontology/identifier | Evidence caveat |
|---|---|---|---|---|
| Disease entity | FG syndrome 4 is a rare Mendelian/X-linked neurodevelopmental disorder entity linked to **CASK**; Open Targets maps **FG syndrome 4** to **MONDO:0010318** with one associated target, **CASK** (OpenTargets Search: FG syndrome 4) | **Broader CASK spectrum:** CASK-related disorders include MICPCH, X-linked intellectual disability, epilepsy, congenital nystagmus, hearing impairment, and other neurodevelopmental phenotypes (mori2023diverseclinicalphenotypes pages 1-2) | **MONDO:0010318**; **CASK / ENSG00000147044** | Direct FG syndrome 4-specific literature is sparse; much modern interpretation relies on broader CASK-disorder evidence (OpenTargets Search: FG syndrome 4, mori2023diverseclinicalphenotypes pages 1-2) |
| Causal gene | Historical FGS4 locus was mapped to **Xp11.4-p11.3** and is now supported as a **CASK**-associated entity (OpenTargets Search: FG syndrome 4) | **Broader CASK spectrum:** CASK is an X-chromosomal gene at **Xp11.4** encoding a MAGUK-family multidomain scaffold/atypical kinase (hayashi2017comprehensiveinvestigationof pages 1-2, mori2023diverseclinicalphenotypes pages 1-2, tibbe2021functionalanalysisof pages 1-2) | **CASK / ENSG00000147044**; locus label **Xp11.4-p11.3** | Gene assignment is strong at disease-platform level, but FGS4 nosology historically overlapped with other FG syndromes (OpenTargets Search: FG syndrome 4) |
| Inheritance | **X-linked inheritance** is the best-supported inheritance model for FG syndrome 4 via CASK (OpenTargets Search: FG syndrome 4) | **Broader CASK spectrum:** severe phenotypes often occur in hemizygous males; heterozygous females more commonly survive with variable severity influenced by X-inactivation; many cases are de novo (hayashi2017comprehensiveinvestigationof pages 1-2, mukherjee2022thenonlinearpath pages 3-5, mori2023diverseclinicalphenotypes pages 5-7) | Inheritance label: **X-linked** | Sex-specific expression and severity are inferred largely from broader CASK cohorts rather than FG syndrome 4-only case series (hayashi2017comprehensiveinvestigationof pages 1-2, mori2023diverseclinicalphenotypes pages 5-7) |
| Core phenotype | FG syndrome 4 is best understood as a syndromic neurodevelopmental disorder with intellectual/developmental impairment and neurologic abnormalities due to CASK dysfunction (OpenTargets Search: FG syndrome 4) | **Broader CASK spectrum:** intellectual disability in 96.1% of males and 93.5% of females; microcephaly/MICPCH in 76.0% of males and 87.7% of females; epilepsy in 54.1% of males vs 36.1% of females (mori2023diverseclinicalphenotypes pages 5-7) | HPO suggestions: **Intellectual disability**, **Global developmental delay**, **Microcephaly**, **Seizure**, **Nystagmus** | These percentages are from aggregated CASK-related disorder reviews, not FG syndrome 4-specific cohorts (mori2023diverseclinicalphenotypes pages 5-7) |
| Neuroimaging/anatomy | FG syndrome 4 likely belongs within the CASK-linked hindbrain/pontocerebellar phenotype spectrum rather than a purely dysmorphic FG syndrome concept (OpenTargets Search: FG syndrome 4, mori2023diverseclinicalphenotypes pages 1-2) | **Broader CASK spectrum:** pontocerebellar hypoplasia on MRI is common; in one 41-patient MICPCH cohort, brain MRI confirmed pontocerebellar hypoplasia in all patients studied; progressive microcephaly is characteristic (hayashi2017comprehensiveinvestigationof pages 2-3, mori2023diverseclinicalphenotypes pages 8-9) | UBERON suggestions: **cerebellum**, **pons**, **brainstem** | MRI findings are firmly established for CASK-related MICPCH, but not necessarily reported in every FG syndrome 4-labeled case (hayashi2017comprehensiveinvestigationof pages 2-3, mori2023diverseclinicalphenotypes pages 8-9) |
| Additional phenotypes | FG syndrome 4 can include ophthalmologic and movement-related manifestations under the CASK-linked phenotype umbrella (OpenTargets Search: FG syndrome 4, mori2023diverseclinicalphenotypes pages 1-2) | **Broader CASK spectrum:** dystonia, scoliosis, growth retardation, optic atrophy, deafness/hearing loss, hypotonia, and congenital nystagmus are recurrent findings; in a 13-patient series, phenotype included psychomotor retardation, severe intellectual disability, progressive microcephaly, dystonia, mild dysmorphism, scoliosis, and frequent ophthalmologic anomalies/deafness/epilepsy (hayashi2017comprehensiveinvestigationof pages 2-3, mukherjee2022thenonlinearpath pages 3-5) | HPO suggestions: **Hypotonia**, **Dystonia**, **Scoliosis**, **Sensorineural hearing impairment**, **Optic atrophy** | Feature frequencies vary by cohort composition and sex; direct FG syndrome 4 frequency estimates are unavailable (hayashi2017comprehensiveinvestigationof pages 2-3, martin2025theneurodevelopmentalspectrum pages 1-2) |
| Variant classes | FG syndrome 4 is associated with pathogenic **germline CASK variants**; altered gene product sequence is the current platform-level consequence annotation (OpenTargets Search: FG syndrome 4) | **Broader CASK spectrum:** nonsense, frameshift, missense, splice, and copy-number variants are all reported; one MICPCH cohort identified 23 point mutations and 9 copy-number variants among 41 patients; all tested parental samples but one were de novo (hayashi2017comprehensiveinvestigationof pages 2-3, mori2023diverseclinicalphenotypes pages 1-2, mori2023diverseclinicalphenotypes pages 5-7) | Variant class labels: **missense**, **frameshift**, **nonsense**, **splice-site**, **copy-number variant** | No single recurrent FG syndrome 4 founder variant is established from current retrieved evidence (hayashi2017comprehensiveinvestigationof pages 2-3, mori2023diverseclinicalphenotypes pages 5-7) |
| Molecular mechanism | FG syndrome 4 is mechanistically attributable to loss or disruption of **CASK** function in neuronal development and synaptic systems (OpenTargets Search: FG syndrome 4) | **Broader CASK spectrum:** CASK is a multidomain scaffold/atypical kinase with CaMK, L27, PDZ, SH3, and GuK domains; it binds neurexin, liprin-α, SAP97, Tbr1, CINAP and others; disease-associated missense variants can impair neurexin binding/oligomerization and alter transcriptional or receptor-trafficking functions (mukherjee2022thenonlinearpath pages 8-9, mukherjee2022thenonlinearpath pages 6-8, pan2021missensemutationsin pages 4-6, pan2021missensemutationsin pages 9-11, tibbe2021functionalanalysisof pages 1-2) | GO suggestions: **synapse organization**, **protein localization to synapse**, **regulation of transcription**, **receptor trafficking** | Mechanistic conclusions derive mainly from broader CASK molecular studies rather than FGS4-labeled patient studies (mukherjee2022thenonlinearpath pages 8-9, pan2021missensemutationsin pages 4-6, tibbe2021functionalanalysisof pages 1-2) |
| Pathophysiology chain | Upstream event: pathogenic CASK variant; intermediate effects: altered scaffolding/protein interactions and neuronal growth regulation; downstream manifestations: developmental delay, microcephaly, pontocerebellar hypoplasia, seizures, visual/oculomotor abnormalities (OpenTargets Search: FG syndrome 4, mori2023diverseclinicalphenotypes pages 1-2) | **Broader CASK spectrum:** evidence supports non-cell-autonomous postnatal brain growth defects, cerebellar granule-cell vulnerability, altered excitatory/inhibitory balance, and possible metabolic/mitochondrial stress contributions (mukherjee2022thenonlinearpath pages 6-8, mukherjee2022thenonlinearpath pages 8-9, mukherjee2022thenonlinearpath pages 5-6) | GO suggestions: **postnatal brain development**, **neuron death**, **synaptic signaling**; CL suggestions: **cerebellar granule cell**, **Purkinje cell**, **retinal ganglion cell** | Causal chain remains incompletely resolved; synaptic dysfunction alone may be insufficient to explain degeneration (mukherjee2022thenonlinearpath pages 8-9, mukherjee2022thenonlinearpath pages 6-8) |
| Diagnosis | Suspect FG syndrome 4 in individuals with X-linked/syndromic neurodevelopmental disorder features and confirm by **molecular testing of CASK** (OpenTargets Search: FG syndrome 4) | **Broader CASK spectrum:** diagnosis commonly uses exome/genome sequencing or copy-number analysis; CASK screening is especially relevant in microcephaly with pontocerebellar hypoplasia; MRI is supportive; parental testing helps establish de novo status and counseling (hayashi2017comprehensiveinvestigationof pages 1-2, hayashi2017comprehensiveinvestigationof pages 2-3) | Testing identifiers: **CASK sequencing**, **copy-number analysis**, **brain MRI** | No disease-specific consensus diagnostic criteria for FG syndrome 4 were identified in retrieved evidence (hayashi2017comprehensiveinvestigationof pages 1-2, hayashi2017comprehensiveinvestigationof pages 2-3) |
| Differential diagnosis | FG syndrome 4 should be distinguished from other historically named FG syndromes and from other pontocerebellar hypoplasia disorders (OpenTargets Search: FG syndrome 4) | **Broader CASK spectrum:** differential diagnosis includes other genetic causes of MICPCH/PCH and neurodevelopmental disorders with microcephaly, seizures, or nystagmus; genetic heterogeneity in MICPCH includes non-CASK genes such as ITPR1, RELN, DYNC1H1, DCTN1, HDAC2, MARCKS, HS3ST5 (hayashi2017comprehensiveinvestigationof pages 1-2) | Disease labels: **FG syndrome 1 (MED12-related)** vs **FG syndrome 4 (CASK-related)**; broader label **pontocerebellar hypoplasia** | Historical nomenclature can mislead; older FG labels do not always map cleanly to current molecular nosology (OpenTargets Search: FG syndrome 4, hayashi2017comprehensiveinvestigationof pages 1-2) |
| Treatment/management | No FG syndrome 4-specific disease-modifying therapy was identified in retrieved evidence | **Broader CASK spectrum:** management is supportive/symptomatic and multidisciplinary, including developmental therapies, seizure management, hearing/vision support, orthopedic monitoring (e.g., scoliosis), nutrition, and genetic counseling; PCH reviews state treatment is still symptomatic (hayashi2017comprehensiveinvestigationof pages 2-3, martin2025theneurodevelopmentalspectrum pages 1-2) | NCIT suggestions by label: **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Anticonvulsant Therapy**, **Genetic Counseling** | Management recommendations are inferred from CASK/PCH practice patterns; no controlled FG syndrome 4 treatment trials were found (hayashi2017comprehensiveinvestigationof pages 2-3, martin2025theneurodevelopmentalspectrum pages 1-2) |
| Prognosis | FG syndrome 4 prognosis is undefined due to rarity and sparse direct follow-up data | **Broader CASK spectrum:** severity is highly variable; hemizygous males with null variants may be very severe or lethal, whereas heterozygous females can survive with lifelong disability; one cohort showed only 6/41 could walk and 3/41 could speak, underscoring substantial morbidity (hayashi2017comprehensiveinvestigationof pages 2-3, mukherjee2022thenonlinearpath pages 3-5) | Outcome labels: **lifelong neurodevelopmental disability**, **variable severity** | No robust disease-specific survival curves, life expectancy estimates, or mortality rates were identified (hayashi2017comprehensiveinvestigationof pages 2-3, mukherjee2022thenonlinearpath pages 3-5) |
| Epidemiology | No reliable prevalence or incidence estimate for **FG syndrome 4** was identified in retrieved evidence | **Broader CASK spectrum:** disease is rare and likely under-ascertained; published cohorts are small and enriched for severe neurodevelopmental referral populations (hayashi2017comprehensiveinvestigationof pages 1-2, martin2025theneurodevelopmentalspectrum pages 1-2) | MONDO entity: **MONDO:0010318** | Absence of epidemiologic estimates should be treated as a knowledge gap, not evidence of extreme rarity thresholding (hayashi2017comprehensiveinvestigationof pages 1-2, martin2025theneurodevelopmentalspectrum pages 1-2) |
| Environment/prevention | No established environmental risk, protective factor, infectious trigger, or gene-environment interaction was identified for FG syndrome 4 | **Broader CASK spectrum:** prevention is primarily genetic/reproductive—family testing when indicated, recurrence-risk counseling, and consideration of prenatal or preimplantation testing after familial variant identification (supported by de novo but occasionally inherited/mosaic contexts) (hayashi2017comprehensiveinvestigationof pages 2-3) | Prevention labels: **genetic counseling**, **prenatal testing** (label only) | This is a Mendelian disorder; non-genetic prevention evidence was not found in retrieved sources (hayashi2017comprehensiveinvestigationof pages 2-3) |
| Clinical trials / real-world implementation | No FG syndrome 4- or CASK-specific interventional therapeutic trial was retrieved | **Broader CASK spectrum:** a broad observational genotype-first registry, **Simons Searchlight** (**NCT01238250**), is recruiting and may capture natural-history/phenotype data across rare neurodevelopmental genetic disorders | **NCT01238250** | Observational registry participation is not evidence of efficacy for any therapy (OpenTargets Search: FG syndrome 4) |
| Model organisms | No FG syndrome 4-specific animal model named as such was identified | **Broader CASK spectrum:** Cask-null mice die within hours of birth; Cask heterozygous females recapitulate microcephaly, cerebellar hypoplasia, optic nerve hypoplasia, scoliosis, and occasional seizures; post-developmental deletion causes cerebellar degeneration and ataxia; Drosophila and C. elegans models show conserved but partial phenotypes (mukherjee2022thenonlinearpath pages 5-6, mukherjee2022thenonlinearpath pages 3-5, mukherjee2022thenonlinearpath pages 6-8) | Model labels: **mouse**, **Drosophila**, **C. elegans** | Models capture major neurodevelopmental aspects but incompletely reproduce human phenotypic breadth and sex-specific mosaic biology (mukherjee2022thenonlinearpath pages 5-6, mukherjee2022thenonlinearpath pages 3-5, mukherjee2022thenonlinearpath pages 6-8) |
| Recent developments (2023-2024) | For FG syndrome 4 specifically, recent advances mainly come through the broader CASK literature rather than disease-specific series | **Broader CASK spectrum:** 2023 review quantified sex-stratified phenotype frequencies and domain–phenotype relationships; 2024 work highlighted splicing-dependent structural plasticity and vertebrate-specific exon effects; 2024 reviews summarized broader CASK mechanisms (mori2023diverseclinicalphenotypes pages 1-2, mori2023diverseclinicalphenotypes pages 5-7) | Recent-source markers: **2023 review**, **2024 mechanistic study** | These are important for interpretation, but not direct therapeutic breakthroughs for FG syndrome 4 (mori2023diverseclinicalphenotypes pages 1-2, mori2023diverseclinicalphenotypes pages 5-7) |


*Table: This table condenses high-yield knowledge-base facts for FG syndrome 4, clearly separating direct FG syndrome 4 evidence from broader CASK-related disorder evidence. It is useful for curation because the disease-specific literature is sparse and much current understanding is inferred from the larger CASK clinical and mechanistic spectrum.*

## 1. Disease information

### Definition

FGS4 is a rare, Mendelian, X-linked syndromic neurodevelopmental disorder historically mapped to **Xp11.4–p11.3** and now linked to pathogenic variation in **CASK**, encoding calcium/calmodulin-dependent serine protein kinase. The modern molecular interpretation places FGS4 within the broader CASK-related neurodevelopmental spectrum, which includes X-linked intellectual disability, congenital nystagmus, epilepsy, and microcephaly with pontine and cerebellar hypoplasia (MICPCH). (OpenTargets Search: FG syndrome 4, mori2023diverseclinicalphenotypes pages 1-2)

It must not be conflated with **classic FG syndrome/FG syndrome 1**, which is MED12-related. Historical FG-syndrome classification was phenotype based and genetically heterogeneous; consequently, older FGS labels do not always map cleanly to current molecular diagnoses.

### Identifiers and synonyms

- **MONDO:** MONDO:0010318.
- **Causal gene association:** **CASK**, Ensembl **ENSG00000147044**, chromosome Xp11.4. (OpenTargets Search: FG syndrome 4)
- **Common names:** FG syndrome 4; FGS4; FG syndrome type 4; CASK-related FG syndrome.
- **Broader—but not strictly synonymous—terms:** CASK-related disorder; CASK-related intellectual disability; X-linked intellectual disability with or without nystagmus; MICPCH.
- **OMIM/Orphanet/MeSH/ICD-10/ICD-11:** No independently verified FGS4-specific entries or codes were recovered in the retrieved evidence. Generic intellectual-disability, congenital-malformation, microcephaly, epilepsy, or pontocerebellar-hypoplasia codes may be used clinically, but they are not specific identifiers for FGS4.

The evidence summarized here is **aggregated disease-level literature and database evidence**, not individual EHR data. Some primary studies report individual patients or small cohorts.

## 2. Etiology

### Causal factors and genetic risk

The primary cause is a **germline pathogenic CASK variant**. Reported CASK disease alleles across the broader spectrum include nonsense, frameshift, splice-site, missense, intragenic deletion/duplication, and larger Xp11.4 copy-number variants. Loss-of-function alleles generally reduce or eliminate functional protein; missense alleles may be hypomorphic or selectively disrupt particular molecular interactions. (hayashi2017comprehensiveinvestigationof pages 2-3, mori2023diverseclinicalphenotypes pages 1-2, mori2023diverseclinicalphenotypes pages 5-7)

In a 2017 study of 41 patients selected for intellectual disability and MICPCH, 32 had CASK abnormalities—23 point variants and nine copy-number variants. The paper reports a **90.2% overall molecular identification rate**, including non-CASK candidate diagnoses, rather than a 90.2% CASK rate. Parental testing showed that all assessed variants except one were de novo. (hayashi2017comprehensiveinvestigationof pages 1-2, hayashi2017comprehensiveinvestigationof pages 2-3)

Sex and X-chromosome constitution strongly influence severity. Hemizygous males have all cells exposed to the variant and severe null alleles may be perinatal lethal. Heterozygous females are mosaics through X-chromosome inactivation and often survive with variable disease. Somatic mosaicism can attenuate disease in males. (mukherjee2022thenonlinearpath pages 3-5, mori2023diverseclinicalphenotypes pages 5-7)

### Environmental, lifestyle, infectious, and protective factors

No reproducible environmental toxin, infection, diet, lifestyle exposure, or occupational factor is known to cause or materially modify FGS4. No validated protective CASK allele, modifier gene, protective exposure, or gene–environment interaction was identified. Family history is relevant only through inheritance or parental germline/somatic mosaicism. These negative findings are consistent with a highly penetrant Mendelian developmental disorder, but formal gene–environment studies are lacking.

## 3. Phenotypes

Direct FGS4 frequency data are unavailable. The following estimates derive from aggregated **CASK-related disorder** literature and should be curated with that qualifier.

- **Intellectual disability/global developmental delay:** 96.1% of males and 93.5% of females in the 2023 review. Severity ranges from mild to profound, but severe impairment predominates in MICPCH cohorts. Suggested HPO: *Intellectual disability*, *Global developmental delay*, *Delayed speech and language development*. (mori2023diverseclinicalphenotypes pages 5-7)
- **Microcephaly/MICPCH:** 76.0% of males and 87.7% of females in the same review. Head growth may be normal or mildly reduced at birth and become progressively abnormal postnatally; prenatal onset is reported in some patients. Suggested HPO: *Microcephaly*, *Progressive microcephaly*, *Pontocerebellar hypoplasia*, *Cerebellar hypoplasia*, *Pontine hypoplasia*. (mori2023diverseclinicalphenotypes pages 5-7, mori2023diverseclinicalphenotypes pages 8-9)
- **Epilepsy:** 54.1% of males versus 36.1% of females, a reported sex difference of p=0.0198. Onset and seizure type are variable; severe males may have early refractory epilepsy. Suggested HPO: *Seizure*, *Epileptic encephalopathy*, with seizure-subtype terms assigned case by case. (mukherjee2022thenonlinearpath pages 3-5, mori2023diverseclinicalphenotypes pages 5-7)
- **Motor impairment:** hypotonia, dystonia, impaired coordination, delayed or absent walking, and sometimes later spasticity. In the 41-person MICPCH cohort, only 6 walked and 3 spoke, illustrating severe functional morbidity in an ascertainment-enriched cohort. Suggested HPO: *Muscular hypotonia*, *Dystonia*, *Motor delay*, *Gait abnormality*. (hayashi2017comprehensiveinvestigationof pages 2-3)
- **Ophthalmologic/oculomotor disease:** congenital nystagmus, optic atrophy or optic-nerve hypoplasia, glaucoma, megalocornea, and cerebral visual impairment are reported. Nystagmus has incomplete penetrance and has been associated mechanistically with C-terminal CASK–FRMD7 interactions. Suggested HPO: *Congenital nystagmus*, *Optic atrophy*, *Optic nerve hypoplasia*, *Glaucoma*, *Megalocornea*. (mukherjee2022thenonlinearpath pages 3-5)
- **Hearing impairment:** sensorineural hearing loss is recurrent. Suggested HPO: *Sensorineural hearing impairment*. (hayashi2017comprehensiveinvestigationof pages 2-3, martin2025theneurodevelopmentalspectrum pages 1-2)
- **Growth and musculoskeletal findings:** growth retardation, scoliosis, and occasionally contractures or FG-like congenital anomalies. Suggested HPO: *Growth delay*, *Scoliosis*.
- **Behavioral/neuropsychiatric phenotype:** autistic traits or autism-spectrum diagnoses and sleep difficulties occur in the broader CASK spectrum. Quantitative FGS4-specific data are unavailable. Suggested HPO: *Autistic behavior*, *Sleep disturbance*. (mori2023diverseclinicalphenotypes pages 1-2, martin2025theneurodevelopmentalspectrum pages 1-2)
- **Facial dysmorphism:** generally mild and variable in CASK cohorts; historical FG-like gestalt is insufficient for molecular diagnosis.

Symptoms are congenital or begin in infancy/childhood. The condition is lifelong. Developmental disability is generally stable, while head-growth deceleration and cerebellar degeneration can be progressive. Epilepsy may be episodic or chronic. No validated FGS4-specific EQ-5D, SF-36, PROMIS, or other quality-of-life study was found; nevertheless, impaired communication, mobility, vision, hearing, feeding, and seizure burden can substantially limit daily functioning.

## 4. Genetic and molecular information

### Gene and variants

**CASK** encodes an X-linked multidomain membrane-associated guanylate kinase-family protein. Its principal domains are an N-terminal atypical CaMK domain, two L27 domains, PDZ, SH3, and guanylate-kinase-like domains. (mukherjee2022thenonlinearpath pages 5-6, mori2023diverseclinicalphenotypes pages 1-2, tibbe2021functionalanalysisof pages 1-2)

Broader CASK studies support the following genotype–phenotype tendencies:

- Nonsense and frameshift alleles usually cause loss of function and are overrepresented among affected females; severe constitutive null alleles are poorly tolerated in males.
- Missense alleles can disrupt selected binding partners and may permit survival in males. Five experimentally studied variants were **p.Arg489Trp, p.Met507Ile, p.Gly521Val, p.Asn798Tyr, and p.Val849Ala**. (pan2021missensemutationsin pages 4-6)
- Missense variants associated with intellectual disability and epilepsy occur throughout the protein, whereas variants associated with microcephaly/MICPCH appear more domain restricted. (mori2023diverseclinicalphenotypes pages 1-2)
- Copy-number variants can remove part or all of CASK and sometimes neighboring genes, complicating attribution.

Variants are principally **germline**, although somatic mosaic variants occur. Population allele frequencies for individual FGS4 alleles were not recovered; fully penetrant severe variants are expected to be absent or extremely rare in population databases. No founder allele, anticipation, or established modifier gene is known. Female expression is influenced by X-inactivation, but no validated disease-specific methylation episignature was identified.

**HGNC ID, ClinVar accessions, exact HGVS sequence for the reported FGS4 splice variant, and allele frequencies should be added only after direct ClinVar/HGNC transcript verification.** They were not available in the retrieved full-text evidence and should not be inferred.

## 5. Environmental information

No causal environmental exposure, lifestyle factor, or infectious agent applies. Smoking, alcohol, diet, exercise, pollution, radiation, and occupational exposure have not been shown to determine disease occurrence. Maternal exposures could independently affect neurodevelopment but are not recognized causes of FGS4. CTD-like chemical–gene associations should not be promoted to disease-risk factors without human evidence.

## 6. Mechanism and pathophysiology

### Upstream-to-downstream causal model

1. **Pathogenic CASK variation** causes haploinsufficiency, complete loss, or selective impairment of a functional domain.
2. **Protein interaction and localization defects** disturb CASK scaffolding at presynaptic and postsynaptic sites and in the nucleus/cytoplasm. Important partners include neurexin, liprin-α, Mint1, Veli/Lin7, SAP97, syndecan, SynCAM, TBR1, CINAP, FRMD7, and CNTNAP2. (mukherjee2022thenonlinearpath pages 8-9, mukherjee2022thenonlinearpath pages 6-8, tibbe2021functionalanalysisof pages 1-2)
3. **Synaptic and transcriptional consequences** include impaired neurexin binding and neurexin-induced CASK oligomerization, altered active-zone organization, NMDA/AMPA receptor trafficking, and altered TBR1-associated regulation of **RELN** and **GRIN2B/NR2B**. (mukherjee2022thenonlinearpath pages 5-6, pan2021missensemutationsin pages 4-6, pan2021missensemutationsin pages 9-11)
4. **Network/cellular consequences** include altered excitatory–inhibitory balance, impaired postnatal brain growth, and vulnerability of cerebellar granule cells. Heterozygous mouse proteomics found more than 500 differentially expressed proteins, including 99 mitochondrial proteins, supporting additional cytoskeletal, translational/chaperone, and metabolic components. (mukherjee2022thenonlinearpath pages 8-9)
5. **Tissue-level effects** include disproportionate hindbrain and cerebellar injury, optic-nerve hypoplasia, microcephaly, and—in severe males—brainstem dysfunction affecting respiration and swallowing. These produce developmental disability, ataxia/motor impairment, epilepsy, nystagmus, and sensory deficits. (mukherjee2022thenonlinearpath pages 3-5, mukherjee2022thenonlinearpath pages 8-9)

### Important expert interpretation

A simple “loss of synaptic CASK function causes maldevelopment” model is inadequate. Cask-null mice can show largely normal initial brain lamination and synaptic ultrastructure, while heterozygous animals develop postnatal abnormalities. Cell-specific deletion from Purkinje cells, retinal ganglion cells, or granule-cell precursors does not independently reproduce degeneration. This supports **non-cell-autonomous, tissue-level pathogenesis** and later neurodegeneration rather than a pure neuronal migration defect. (mukherjee2022thenonlinearpath pages 6-8, mukherjee2022thenonlinearpath pages 5-6)

The 2022 review’s central caution is that CASK molecular functions and clinical pathology have a “highly complex relationship”; mechanistic annotations should therefore separate demonstrated interactions from proven disease-causal pathways. (mukherjee2022thenonlinearpath pages 6-8)

### Ontology suggestions

- **GO biological process:** synapse organization; regulation of synaptic vesicle exocytosis; receptor localization to synapse; regulation of transcription by RNA polymerase II; postnatal brain development; regulation of neuron death; regulation of mitochondrial metabolism.
- **GO molecular function:** protein-domain-specific binding; scaffold protein binding; protein serine/threonine kinase activity; neurexin binding.
- **GO cellular component:** presynaptic active zone; postsynaptic density; neuronal nucleus; cytosol; plasma membrane.
- **Cell Ontology labels:** neuron; cerebellar granule cell; Purkinje cell; retinal ganglion cell; excitatory neuron; inhibitory neuron. Exact CL identifiers should be ontology-validated before ingestion.

No validated FGS4-specific single-cell, spatial-transcriptomic, lipidomic, or metabolomic signature was found. Human induced cortical excitatory-neuron models exist in the broader CASK field, but no clinical omics biomarker is established.

## 7. Anatomical structures affected

The **central nervous system** is primary, especially:

- cerebellum, particularly the granule-cell layer;
- pons and brainstem;
- cerebral cortex and broader forebrain networks;
- optic nerve and visual pathways;
- auditory pathways.

Secondary systems include skeletal muscle/motor apparatus, spine, eyes, ears, and—depending on phenotype—feeding and respiratory systems. MRI may show pontocerebellar hypoplasia, with cerebellar involvement generally greater than pontine involvement. In the 2017 selected MICPCH cohort, all patients had MRI-confirmed pontocerebellar hypoplasia. (hayashi2017comprehensiveinvestigationof pages 2-3)

Suggested UBERON labels are *brain*, *cerebral cortex*, *cerebellum*, *cerebellar granule layer*, *pons*, *brainstem*, *optic nerve*, *retina*, *inner ear*, and *spinal column*. No consistent lateralization is established; findings are generally bilateral or diffuse.

## 8. Temporal development

Onset is congenital or early pediatric. Microcephaly may be prenatal but often becomes more conspicuous postnatally. Developmental delay, hypotonia, hearing loss, or nystagmus may be evident in infancy; seizures can begin in infancy or childhood. (hayashi2017comprehensiveinvestigationof pages 2-3, mori2023diverseclinicalphenotypes pages 8-9)

The course is chronic and lifelong. Head growth deceleration and cerebellar injury may progress, whereas many congenital structural abnormalities remain stable. Experimental post-developmental deletion causes granule-layer atrophy beginning around two months in mice, supporting a continuing requirement for CASK and a degenerative component. (mukherjee2022thenonlinearpath pages 6-8)

No accepted FGS4 staging system, remission pattern, or sharply defined intervention window exists. Early childhood is nonetheless a practical critical period for hearing/vision correction, seizure control, communication support, nutrition, and habilitative therapy.

## 9. Inheritance and population

Inheritance is **X-linked**. Hemizygous males are often more severely affected by loss-of-function alleles, while heterozygous females show variable expressivity because of cellular mosaicism from X-inactivation. In the 2023 aggregation, intellectual-disability frequencies were similar by sex, but epilepsy was significantly more common in males. (mori2023diverseclinicalphenotypes pages 5-7)

Many cases are de novo. Recurrence risk is usually low after a proven de novo event but is not zero because parental germline or low-level somatic mosaicism may be missed. In inherited families, a heterozygous mother may transmit the allele to 50% of pregnancies; outcome differs by fetal sex, variant effect, and X-inactivation. Female penetrance and severity are variable rather than predictably complete. Anticipation and consanguinity are not characteristic. (hayashi2017comprehensiveinvestigationof pages 2-3)

No reliable FGS4 prevalence, incidence, carrier frequency, geographic concentration, founder effect, ethnic enrichment, or population sex ratio is available. Referral cohorts are not suitable for population estimation.

## 10. Diagnostics

### Recommended approach

1. **Clinical assessment:** developmental history, three-generation pedigree, growth and serial head circumference, neurologic examination, dysmorphology, vision/hearing, feeding, and musculoskeletal examination.
2. **Brain MRI:** assess pons, cerebellar hemispheres/vermis, cortex, white matter, ventricles, and optic structures.
3. **EEG** for seizures or regression; audiology/ABR and formal ophthalmology regardless of obvious symptoms.
4. **Genetic testing:** trio exome or genome sequencing is efficient because of phenotypic and locus heterogeneity. Analysis must include CASK single-nucleotide and indel variants and copy-number calling.
5. If phenotype strongly indicates CASK disease, use **CASK sequencing plus deletion/duplication analysis**. Chromosomal microarray is useful for Xp11.4 deletions/duplications but misses most sequence variants.
6. Confirm variants orthogonally when needed and test parents, including mosaic-sensitive testing where recurrence counseling depends on it.

Karyotyping and FISH have limited resolution and are appropriate mainly for a suspected large rearrangement. Mitochondrial DNA and repeat-expansion testing are not first-line. RNA sequencing can clarify a suspected splice variant or VUS but is not a routine validated diagnostic biomarker. No enzyme assay, blood metabolite, biopsy feature, liquid biopsy, or disease-specific biochemical marker is diagnostic.

### Differential diagnosis

- MED12-related FG syndrome 1 and other historical FG syndromes;
- other pontocerebellar hypoplasias, including TSEN54-related disease;
- ITPR1-, RELN-, DYNC1H1-, and DCTN1-related disorders;
- other causes of syndromic X-linked intellectual disability, congenital nystagmus, microcephaly, epilepsy, or cerebellar hypoplasia. The 2017 study also identified or considered HDAC2, MARCKS, and HS3ST5 among non-CASK candidates, illustrating MICPCH heterogeneity. (hayashi2017comprehensiveinvestigationof pages 1-2)

No standardized FGS4 clinical diagnostic criteria were found; molecular confirmation is preferred. There is no population or newborn screening program. Cascade testing is appropriate after identifying a familial variant.

## 11. Outcome and prognosis

FGS4-specific survival curves, mortality rates, and life-expectancy estimates do not exist. Prognosis is highly variable and depends on variant class, sex, mosaicism, brainstem involvement, epilepsy, feeding/respiratory complications, and degree of developmental impairment.

Severe hemizygous null alleles may cause fetal or neonatal death or profound encephalopathy. Brainstem thinning can impair respiratory and swallowing reflexes, increasing risk of central respiratory failure, aspiration, airway infection, and pneumonia. An autopsied male with a p.Arg27Ter allele had a brain approximately 60% of expected weight and an extremely hypoplastic hindbrain. (mukherjee2022thenonlinearpath pages 3-5)

Surviving females and males with hypomorphic or mosaic variants may live into adulthood but commonly require lifelong support. Morbidity includes limited speech and mobility, epilepsy, visual/hearing impairment, scoliosis, feeding difficulties, and dependence in activities of daily living. No validated prognostic biomarker or prediction model exists.

## 12. Treatment and real-world implementation

There is **no approved disease-modifying, gene, RNA, cell, or targeted therapy** for FGS4/CASK-related disease. Treatment is individualized and supportive:

- antiseizure medication selected by seizure type and EEG;
- early physical, occupational, speech/language, feeding, and augmentative-communication therapy;
- hearing aids or cochlear evaluation as indicated;
- ophthalmologic treatment and visual-access interventions;
- nutritional and swallowing assessment, aspiration prevention, and gastrostomy when clinically required;
- orthopedic surveillance and treatment of scoliosis/contractures;
- management of sleep, constipation, respiratory problems, and behavioral distress;
- palliative/supportive planning in severe brainstem disease;
- clinical genetics and reproductive counseling.

Suggested NCIt intervention labels include *Anticonvulsant Therapy*, *Physical Therapy*, *Occupational Therapy*, *Speech Therapy*, *Hearing Aid*, *Gastrostomy*, and *Genetic Counseling*; exact NCIt codes should be terminology-validated before database loading.

No response rates, comparative treatment trials, CASK-specific pharmacogenomic recommendations, or treatment algorithm supported by controlled evidence were found. A search identified no FGS4/CASK-specific interventional trial. **Simons Searchlight, NCT01238250**, is a recruiting observational genotype-first registry relevant to rare neurodevelopmental disorders; it does not test therapeutic efficacy.

## 13. Prevention

Primary prevention by lifestyle modification, vaccination, environmental remediation, or medication is not applicable. Secondary and tertiary prevention consist of:

- early molecular diagnosis;
- seizure recognition and treatment;
- hearing and vision screening;
- feeding/aspiration, respiratory, and scoliosis surveillance;
- early developmental intervention.

After identifying a familial pathogenic variant, reproductive options include prenatal diagnosis and preimplantation genetic testing. Counseling must discuss variable female expression, potentially severe male disease, and residual recurrence risk from parental mosaicism. Population carrier screening and newborn screening are not established.

## 14. Other species and natural disease

No naturally occurring veterinary disease that is a validated homolog of human FGS4 was identified. CASK is evolutionarily conserved across vertebrates and invertebrates, but experimental ortholog disruption should not be described as naturally occurring FG syndrome. There is no infectious transmission, zoonotic potential, or cross-species contagion.

Relevant experimental taxa include:

- *Mus musculus*—NCBI Taxonomy 10090;
- *Drosophila melanogaster*—7227;
- *Caenorhabditis elegans*—6239.

Exact orthologous NCBI Gene IDs and any OMIA/VBO entries require dedicated database validation.

## 15. Model organisms and advanced models

### Mouse

Constitutive **Cask-null mice** die within hours of birth, exhibit central respiratory failure, increased thalamic neuronal death, and cleft palate with approximately 80% penetrance. Initial brain lamination and synaptic ultrastructure are comparatively preserved, highlighting limitations of equating early structure with later disease. (mukherjee2022thenonlinearpath pages 5-6, mukherjee2022thenonlinearpath pages 3-5)

**Cask+/− female mice** express approximately 50% of normal CASK and reproduce major human features: postnatal microcephaly, cerebellar and optic-nerve hypoplasia, scoliosis, impaired coordination, and occasional seizures. They are useful for studying female mosaic disease but show milder behavioral and electrophysiologic phenotypes than many severely affected humans. (mukherjee2022thenonlinearpath pages 6-8, mukherjee2022thenonlinearpath pages 5-6)

Conditional and cell-specific deletions demonstrate that loss from Purkinje cells or retinal ganglion cells alone is insufficient to cause their death, whereas post-developmental broad deletion eventually causes cerebellar granule-cell degeneration and ataxia. These models support a non-cell-autonomous mechanism and continuing postnatal requirement for CASK. (mukherjee2022thenonlinearpath pages 6-8)

### Invertebrates

CASK-null *C. elegans* show vulval abnormalities through the LET-23/EGF pathway but little neuronal phenotype. *Drosophila* CASK loss reduces locomotion without major neuromuscular-junction, motor-neuron, or premotor-neuropil abnormalities. These models reveal conserved functions but incompletely recapitulate human hindbrain disease. (mukherjee2022thenonlinearpath pages 3-5)

### Cellular and structural models

Co-immunoprecipitation, bimolecular fluorescence complementation, molecular modeling, and patient-variant expression studies show that disease-associated variants can disrupt SAP97, TBR1/CINAP, and neurexin interactions. One study concluded that cooperative PDZ–SH3–GK activity is required for neurexin binding and oligomerization. (pan2021missensemutationsin pages 4-6, pan2021missensemutationsin pages 9-11)

Human fetal brain expresses at least seven CASK transcript variants, four not then represented as known GenBank variants; alternative splicing changes partner affinity, particularly SAP97 binding. This makes transcript choice an important consideration for functional variant assays. (tibbe2021functionalanalysisof pages 1-2)

## Recent developments, 2023–2024

The most informative 2023 synthesis quantified sex-stratified manifestations and emphasized domain–phenotype relationships: intellectual disability affected approximately 94–96%, microcephaly/MICPCH 76–88%, and epilepsy 36% of females versus 54% of males in aggregated CASK reports. Its abstract states that CASK disorders are characterized by “MICPCH, epilepsy, congenital nystagmus, and neurodevelopmental disorders.” Published August 2023; DOI: https://doi.org/10.3390/genes14081656. (mori2023diverseclinicalphenotypes pages 1-2, mori2023diverseclinicalphenotypes pages 5-7)

A 2024 study, published online in April, used conditional mouse deletion and human variants to show that adult Cask loss can produce progressive cerebellar degeneration and that alternatively spliced vertebrate-specific exons may create region-dependent structural and functional plasticity. DOI: https://doi.org/10.1136/jmg-2023-109747. This advances mechanism and variant interpretation, but it is not yet a therapeutic breakthrough.

## Evidence limitations and curation recommendations

1. Preserve **FGS4** as the MONDO entity but attach a strong note that modern evidence is largely CASK-spectrum evidence.
2. Do not assign MICPCH cohort frequencies directly to FGS4 without an evidence qualifier.
3. Record variant-level assertions only after transcript-specific ClinVar/HGVS verification.
4. Mark prevalence, incidence, life expectancy, validated biomarkers, environmental risks/protectors, disease-specific clinical criteria, and controlled treatment outcomes as **unknown/not available**, rather than zero.
5. Treat CASK–neurexin, CASK–TBR1/GRIN2B, receptor trafficking, mitochondrial/metabolic stress, and non-cell-autonomous degeneration as complementary hypotheses with different evidence levels—not as one fully proven linear pathway.

### Key publications

- Mori T, Zhou M, Tabuchi K. *Diverse Clinical Phenotypes of CASK-Related Disorders and Multiple Functional Domains of CASK Protein*. **Genes**. Published August 2023. DOI: https://doi.org/10.3390/genes14081656. (mori2023diverseclinicalphenotypes pages 1-2)
- Hayashi S, et al. *Comprehensive investigation of CASK mutations and other genetic etiologies in 41 patients with intellectual disability and MICPCH*. **PLOS ONE**. Published August 2017. DOI: https://doi.org/10.1371/journal.pone.0181791. (hayashi2017comprehensiveinvestigationof pages 1-2, hayashi2017comprehensiveinvestigationof pages 2-3)
- Pan YE, et al. *Missense mutations in CASK…interfere with neurexin binding and neurexin-induced oligomerization*. **Journal of Neurochemistry**. Published May 2021. DOI: https://doi.org/10.1111/jnc.15215. (pan2021missensemutationsin pages 4-6)
- Tibbe D, et al. *Functional analysis of CASK transcript variants expressed in human brain*. **PLOS ONE**. Published June 2021. DOI: https://doi.org/10.1371/journal.pone.0253223. (tibbe2021functionalanalysisof pages 1-2)
- Mukherjee K, LaConte LEW, Srivastava S. *The Non-Linear Path from Gene Dysfunction to Genetic Disease: Lessons from the MICPCH Mouse Model*. **Cells**. Published March 2022. DOI: https://doi.org/10.3390/cells11071131. (mukherjee2022thenonlinearpath pages 6-8, mukherjee2022thenonlinearpath pages 8-9)
- Patel PA, et al. *Genetic evidence for splicing-dependent structural and functional plasticity in CASK protein*. **Journal of Medical Genetics**. Published April 2024. DOI: https://doi.org/10.1136/jmg-2023-109747.

References

1. (OpenTargets Search: FG syndrome 4): Open Targets Query (FG syndrome 4, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (mori2023diverseclinicalphenotypes pages 1-2): Takuma Mori, Mengyun Zhou, and Katsuhiko Tabuchi. Diverse clinical phenotypes of cask-related disorders and multiple functional domains of cask protein. Genes, 14:1656, Aug 2023. URL: https://doi.org/10.3390/genes14081656, doi:10.3390/genes14081656. This article has 17 citations.

3. (hayashi2017comprehensiveinvestigationof pages 1-2): Shin Hayashi, Daniela Tiaki Uehara, Kousuke Tanimoto, Seiji Mizuno, Yasutsugu Chinen, Shinobu Fukumura, Jun-ichi Takanashi, Hitoshi Osaka, Nobuhiko Okamoto, and Johji Inazawa. Comprehensive investigation of cask mutations and other genetic etiologies in 41 patients with intellectual disability and microcephaly with pontine and cerebellar hypoplasia (micpch). PLOS ONE, 12:e0181791, Aug 2017. URL: https://doi.org/10.1371/journal.pone.0181791, doi:10.1371/journal.pone.0181791. This article has 81 citations and is from a peer-reviewed journal.

4. (tibbe2021functionalanalysisof pages 1-2): Debora Tibbe, Yingzhou Edward Pan, Carsten Reißner, Frederike L. Harms, and Hans-Jürgen Kreienkamp. Functional analysis of cask transcript variants expressed in human brain. PLoS ONE, 16:e0253223, Jun 2021. URL: https://doi.org/10.1371/journal.pone.0253223, doi:10.1371/journal.pone.0253223. This article has 16 citations and is from a peer-reviewed journal.

5. (mukherjee2022thenonlinearpath pages 3-5): Konark Mukherjee, Leslie E. W. LaConte, and Sarika Srivastava. The non-linear path from gene dysfunction to genetic disease: lessons from the micpch mouse model. Cells, 11:1131, Mar 2022. URL: https://doi.org/10.3390/cells11071131, doi:10.3390/cells11071131. This article has 7 citations.

6. (mori2023diverseclinicalphenotypes pages 5-7): Takuma Mori, Mengyun Zhou, and Katsuhiko Tabuchi. Diverse clinical phenotypes of cask-related disorders and multiple functional domains of cask protein. Genes, 14:1656, Aug 2023. URL: https://doi.org/10.3390/genes14081656, doi:10.3390/genes14081656. This article has 17 citations.

7. (hayashi2017comprehensiveinvestigationof pages 2-3): Shin Hayashi, Daniela Tiaki Uehara, Kousuke Tanimoto, Seiji Mizuno, Yasutsugu Chinen, Shinobu Fukumura, Jun-ichi Takanashi, Hitoshi Osaka, Nobuhiko Okamoto, and Johji Inazawa. Comprehensive investigation of cask mutations and other genetic etiologies in 41 patients with intellectual disability and microcephaly with pontine and cerebellar hypoplasia (micpch). PLOS ONE, 12:e0181791, Aug 2017. URL: https://doi.org/10.1371/journal.pone.0181791, doi:10.1371/journal.pone.0181791. This article has 81 citations and is from a peer-reviewed journal.

8. (mori2023diverseclinicalphenotypes pages 8-9): Takuma Mori, Mengyun Zhou, and Katsuhiko Tabuchi. Diverse clinical phenotypes of cask-related disorders and multiple functional domains of cask protein. Genes, 14:1656, Aug 2023. URL: https://doi.org/10.3390/genes14081656, doi:10.3390/genes14081656. This article has 17 citations.

9. (martin2025theneurodevelopmentalspectrum pages 1-2): Jessica Martin, Alkistis Mavrogalou-Foti, Josefine Eck, Laura Hattersley, and Kate Baker. The neurodevelopmental spectrum of cask-related disorder. Journal of Neurodevelopmental Disorders, Oct 2025. URL: https://doi.org/10.1186/s11689-025-09643-3, doi:10.1186/s11689-025-09643-3. This article has 6 citations and is from a peer-reviewed journal.

10. (mukherjee2022thenonlinearpath pages 8-9): Konark Mukherjee, Leslie E. W. LaConte, and Sarika Srivastava. The non-linear path from gene dysfunction to genetic disease: lessons from the micpch mouse model. Cells, 11:1131, Mar 2022. URL: https://doi.org/10.3390/cells11071131, doi:10.3390/cells11071131. This article has 7 citations.

11. (mukherjee2022thenonlinearpath pages 6-8): Konark Mukherjee, Leslie E. W. LaConte, and Sarika Srivastava. The non-linear path from gene dysfunction to genetic disease: lessons from the micpch mouse model. Cells, 11:1131, Mar 2022. URL: https://doi.org/10.3390/cells11071131, doi:10.3390/cells11071131. This article has 7 citations.

12. (pan2021missensemutationsin pages 4-6): Yingzhou Edward Pan, Debora Tibbe, Frederike Leonie Harms, Carsten Reißner, Kerstin Becker, Bri Dingmann, Ghayda Mirzaa, Anja A. Kattentidt‐Mouravieva, Moneef Shoukier, Shagun Aggarwal, Markus Missler, Kerstin Kutsche, and Hans‐Jürgen Kreienkamp. Missense mutations in cask, coding for the calcium‐/calmodulin‐dependent serine protein kinase, interfere with neurexin binding and neurexin‐induced oligomerization. Journal of Neurochemistry, 157:1331-1350, May 2021. URL: https://doi.org/10.1111/jnc.15215, doi:10.1111/jnc.15215. This article has 25 citations and is from a domain leading peer-reviewed journal.

13. (pan2021missensemutationsin pages 9-11): Yingzhou Edward Pan, Debora Tibbe, Frederike Leonie Harms, Carsten Reißner, Kerstin Becker, Bri Dingmann, Ghayda Mirzaa, Anja A. Kattentidt‐Mouravieva, Moneef Shoukier, Shagun Aggarwal, Markus Missler, Kerstin Kutsche, and Hans‐Jürgen Kreienkamp. Missense mutations in cask, coding for the calcium‐/calmodulin‐dependent serine protein kinase, interfere with neurexin binding and neurexin‐induced oligomerization. Journal of Neurochemistry, 157:1331-1350, May 2021. URL: https://doi.org/10.1111/jnc.15215, doi:10.1111/jnc.15215. This article has 25 citations and is from a domain leading peer-reviewed journal.

14. (mukherjee2022thenonlinearpath pages 5-6): Konark Mukherjee, Leslie E. W. LaConte, and Sarika Srivastava. The non-linear path from gene dysfunction to genetic disease: lessons from the micpch mouse model. Cells, 11:1131, Mar 2022. URL: https://doi.org/10.3390/cells11071131, doi:10.3390/cells11071131. This article has 7 citations.

## Artifacts

- [Edison artifact artifact-00](FG_Syndrome_4-deep-research-falcon_artifacts/artifact-00.md)