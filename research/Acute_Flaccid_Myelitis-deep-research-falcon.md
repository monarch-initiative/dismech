---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-16T10:34:56.461000'
end_time: '2026-05-16T10:49:58.498717'
duration_seconds: 902.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Flaccid Myelitis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Acute_Flaccid_Myelitis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Flaccid Myelitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Flaccid Myelitis** covering all of the
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
- **Disease Name:** Acute Flaccid Myelitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Flaccid Myelitis** covering all of the
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


# Acute Flaccid Myelitis (AFM) — Comprehensive Disease Characteristics Report

**Target disease:** Acute flaccid myelitis (AFM)

**Summary (current understanding):** AFM is a rare, severe neurologic syndrome (often pediatric) characterized by acute flaccid limb weakness with spinal cord gray-matter–predominant lesions on MRI, clinically resembling poliomyelitis. In the United States, AFM incidence showed large peaks in 2014/2016/2018 and remained lower in 2019–2022, despite renewed EV-D68 circulation in 2022 without a commensurate AFM surge, emphasizing unresolved determinants of neuroinvasion and paralytic risk. (whitehouse2024surveillanceforacute pages 1-2, kidd2020vitalsignsclinical pages 1-2, messacar2024multimodalsurveillancemodel pages 3-5)

---

## 1. Disease Information

### 1.1 Disease overview and definition
CDC surveillance definitions used in recent U.S. reports define **confirmed AFM** as **acute flaccid limb weakness** with **MRI demonstrating a spinal cord lesion largely restricted to gray matter spanning ≥1 vertebral segment**. (whitehouse2024surveillanceforacute pages 1-2, kidd2020vitalsignsclinical pages 1-2)

A recent European case report restates the CDC framing as **“an acute-onset flaccid weakness of one or more limbs”** with MRI evidence of gray-matter involvement and no clear alternative diagnosis. (rodesch2024afirstcase pages 1-3)

### 1.2 Key identifiers
* **MONDO ID:** Not available from the retrieved evidence set (not found in the sources accessed for this report).
* **ICD/MeSH/Orphanet/OMIM:** Not available from the retrieved evidence set.

### 1.3 Synonyms and alternative names
* AFM is repeatedly described as **“poliomyelitis-like”** or **“polio-like”** paralysis/illness in clinical and rehabilitation literature. (doi2024midtermoutcomesof pages 1-2, aguglia2023contemporaryenterovirusd68isolates pages 1-2)
* Related umbrella term: **acute flaccid paralysis (AFP)**; AFM can be considered AFP with spinal cord gray-matter myelitis. (rodesch2024afirstcase pages 3-5)

### 1.4 Evidence source type (individual vs aggregated)
This report integrates both:
* **Aggregated public-health surveillance/clinical series** (CDC MMWR surveillance; Colorado multimodal surveillance; surgical cohort; rehabilitation case series). (whitehouse2024surveillanceforacute pages 1-2, messacar2024multimodalsurveillancemodel pages 3-5, doi2024midtermoutcomesof pages 1-2, neighbors2024transcutaneousspinalcord pages 5-8)
* **Individual patient-level case report** (Belgium EV-D68-associated AFM). (rodesch2024afirstcase pages 1-3)

---

## 2. Etiology

### 2.1 Disease causal factors
**Infectious association (dominant current model):** AFM is strongly associated with **non-polio enteroviruses**, particularly **enterovirus D68 (EV-D68)**, based on epidemiologic correlation with outbreak years and frequent detection in non-sterile sites (especially respiratory specimens), while pathogen detection in CSF is uncommon. (murphy2021acuteflaccidmyelitis pages 1-2, kidd2020vitalsignsclinical pages 1-2, whitehouse2024surveillanceforacute pages 1-2)

CDC surveillance indicates that AFM peaks (2014/2016/2018) were linked to EV-D68 circulation, while post-2018 counts remained low; reasons remain uncertain. (whitehouse2024surveillanceforacute pages 1-2)

**Multi-pathogen reality:** Non–EV-D68 enteroviruses have also been identified in confirmed AFM patients (e.g., EV-A71 and other enteroviruses/echoviruses/cox­sackie types), and coinfections can occur. (whitehouse2024surveillanceforacute pages 5-6, whitehouse2024surveillanceforacute pages 6-7)

### 2.2 Risk factors (supported by recent surveillance)
* **Age:** AFM predominates in children; e.g., in the U.S. 2018 peak year, **94%** of confirmed cases were **<18 years**, with median age **5.3 years**. (whitehouse2024surveillanceforacute pages 4-5)
* **Seasonality:** In 2018, **86%** of U.S. confirmed cases had onset during **August–November**. (kidd2020vitalsignsclinical pages 1-2)
* **Recent febrile/respiratory prodrome:** In 2018, **92%** reported prodromal fever and/or respiratory illness, beginning a median of **6 days** before weakness onset. (kidd2020vitalsignsclinical pages 1-2)

### 2.3 Protective factors
No validated genetic or environmental protective factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
No specific, reproducible gene–environment interaction evidence was identified in the retrieved evidence set.

---

## 3. Phenotypes

### 3.1 Core neurologic phenotype
**Acute limb weakness/paralysis** is the defining clinical phenotype. CDC describes AFM as “characterized by the acute onset of limb weakness or paralysis.” (kidd2020vitalsignsclinical pages 1-2)

**Distribution of weakness varies by outbreak year:** In the U.S. 2018 peak year, **upper limb involvement** was common (**84%**), while later years showed relatively more **lower limb** involvement and lower rates of classic peak-year features. (whitehouse2024surveillanceforacute pages 4-5, whitehouse2024surveillanceforacute pages 1-2)

### 3.2 Common symptoms/signs during evaluation (example: U.S. 2018)
In 2018 confirmed U.S. cases, common findings included:
* **Gait difficulty:** 52%
* **Neck or back pain:** 47%
* **Fever at evaluation:** 35%
* **Limb pain:** 34% (kidd2020vitalsignsclinical pages 1-2)

### 3.3 Laboratory phenotype
**CSF pleocytosis** is common in peak-year AFM, with year-to-year variation; CDC surveillance reports CSF pleocytosis of **87%** in 2018 (183/210) versus **42–49%** in 2019–2021 and **68%** in 2022 (28/41). (whitehouse2024surveillanceforacute pages 4-5)

### 3.4 Quality-of-life impact
AFM is associated with high morbidity and incomplete neurologic recovery, with long-term disability common in clinical reviews and cohort summaries. (murphy2021acuteflaccidmyelitis pages 1-2, vawterlee2021acuteflaccidmyelitis pages 2-3)

### 3.5 Suggested HPO terms (candidate mappings)
The retrieved evidence supports, at minimum:
* **Acute flaccid paralysis / acute limb weakness** (HP:0002015 *or conceptually similar*)
* **Gait disturbance** (HP:0001288)
* **Neck pain / back pain** (HP:0000467 / HP:0003418)
* **Respiratory failure / need for mechanical ventilation** (HP:0002878)
* **CSF pleocytosis** (HP:0002180)

(*Note:* HPO identifiers are provided as common standard mappings; confirm exact HPO IDs/labels in the current HPO release before database ingestion.)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes / pathogenic variants
AFM is not established as a monogenic disorder in the retrieved evidence set; the dominant evidence supports an **infectious-triggered neuroinflammatory/anterior horn cell injury syndrome** rather than a single-gene etiology. (murphy2021acuteflaccidmyelitis pages 1-2)

### 4.2 Modifier genes / host susceptibility
No specific host genetic modifiers were identified in the retrieved evidence set.

### 4.3 Epigenetics / chromosomal abnormalities
No AFM-specific epigenetic or chromosomal-abnormality evidence was identified in the retrieved evidence set.

---

## 5. Environmental Information

### 5.1 Infectious agents (primary environmental exposure)
**Enteroviruses, particularly EV-D68**, are the best-supported associated infectious agents across surveillance and mechanistic modeling. (whitehouse2024surveillanceforacute pages 1-2, kidd2020vitalsignsclinical pages 1-2, aguglia2023contemporaryenterovirusd68isolates pages 1-2)

### 5.2 Other environmental/lifestyle factors
No toxin/radiation/pollution or lifestyle risk factor evidence was identified in the retrieved evidence set.

---

## 6. Mechanism / Pathophysiology

### 6.1 Current mechanistic model (causal chain)
1) **Preceding viral illness** (often respiratory/febrile) occurs days before neurologic onset in many peak-year cases. (kidd2020vitalsignsclinical pages 1-2)
2) **Neurotropic infection and/or immune-mediated injury** targets spinal cord gray matter (anterior horn/motor neuron regions), producing the MRI signature and motor deficits. (whitehouse2024surveillanceforacute pages 1-2, aguglia2023contemporaryenterovirusd68isolates pages 1-2)
3) **Secondary immune-mediated injury is likely important:** Human spinal cord organoid data show sustained EV-D68 infection with limited cytopathic effects, implying that infection alone may not explain neuronal loss in vivo.

### 6.2 Human spinal cord organoid evidence (recent development)
Aguglia et al. (mBio, 2023-08) emphasize the need for human CNS models because **“humans are the only natural hosts for enterovirus infections”** and enteroviruses “do not routinely infect other animal species.” (aguglia2023contemporaryenterovirusd68isolates pages 1-2, aguglia2023contemporaryenterovirusd68isolates pages 5-8)

Key findings from the organoid model:
* **Strain specificity:** Contemporary (post-2014) EV-D68 isolates infect spinal cord organoids, whereas a historic strain (Fermon) does not productively infect. (aguglia2023contemporaryenterovirusd68isolates pages 2-5, aguglia2023contemporaryenterovirusd68isolates pages 5-8)
* **Persistence without marked lysis:** Infected organoids **“produce extracellular virus for at least 2 weeks without appreciable cytopathic effect”** and maintain morphology, with less apoptosis than a comparator enterovirus (echovirus 11). (aguglia2023contemporaryenterovirusd68isolates pages 1-2, aguglia2023contemporaryenterovirusd68isolates pages 8-10)
* **Immune contribution hypothesis:** The authors note that in vitro models lack migratory innate/adaptive immune cells and that this limitation may allow persistence without the injury patterns seen in vivo, supporting a role for immune-mediated secondary damage in AFM. (aguglia2023contemporaryenterovirusd68isolates pages 8-10, aguglia2023contemporaryenterovirusd68isolates pages 10-12)

### 6.3 Suggested ontology mappings
* **UBERON (anatomy):** spinal cord (UBERON:0002240); cervical spinal cord (UBERON:0002726); anterior horn/ventral gray matter region (concept-level mapping) (rodesch2024afirstcase pages 1-3)
* **CL (cell types):** spinal motor neuron (CL:0000100); astrocyte (CL:0000127); oligodendrocyte precursor cell (CL:0002453) as relevant to organoid and EV-D68 tropism work (aguglia2023contemporaryenterovirusd68isolates pages 2-5, dabilla2025strainspecifictropismand pages 9-10)
* **GO biological processes (candidates):** neuroinflammatory response; leukocyte chemotaxis; motor neuron apoptotic process; response to virus; cytokine-mediated signaling pathway (supported conceptually by immune/viral pathogenesis framing and apoptosis/cytokine discussion in organoid work) (aguglia2023contemporaryenterovirusd68isolates pages 8-10)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
* **Primary system:** Central nervous system—**spinal cord**, particularly **gray matter** involvement on MRI; often cervical cord involvement reported in case literature. (whitehouse2024surveillanceforacute pages 1-2, rodesch2024afirstcase pages 1-3)
* **Secondary/complications:** Respiratory failure requiring ventilatory support is common in severe cases. (whitehouse2024surveillanceforacute pages 5-6, kidd2020vitalsignsclinical pages 1-2)

### 7.2 Tissue/cell level
* **Spinal cord gray matter** and motor neuron regions are implicated by imaging criteria and neuroanatomic pattern (anterior horn–predominant lesions). (whitehouse2024surveillanceforacute pages 1-2, vawterlee2021acuteflaccidmyelitis pages 2-3)

---

## 8. Temporal Development

### 8.1 Onset and course
* **Onset pattern:** Acute/subacute, with rapid progression over days; peak-year cases often follow a viral prodrome by ~1 week. (kidd2020vitalsignsclinical pages 1-2, rodesch2024afirstcase pages 3-5)

### 8.2 Recovery window
Rehabilitation literature indicates recovery is often incomplete; functional gains are most robust in the first year but can continue to ~18 months, with persistent proximal weakness/atrophy common. (ide2021acuteflaccidmyelitis. pages 11-13)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent statistics)
**United States (CDC surveillance):**
* Confirmed AFM cases: **238 (2018)**; **47 (2019)**; **33 (2020)**; **28 (2021)**; **47 (2022)**. (whitehouse2024surveillanceforacute pages 1-2)

**U.S. 2018 clinical severity:**
* **98% hospitalized**, **54% ICU**, **23% required intubation/mechanical ventilation**. (kidd2020vitalsignsclinical pages 1-2)

**Colorado 2022 (EV-D68 outbreak monitoring + AFM burden):**
* Among **529** EV/RV-positive respiratory specimens tested, **121 (22.9%)** were EV-D68-positive, peaking at **78.6% weekly positivity** in late August 2022. (messacar2024multimodalsurveillancemodel pages 3-5)
* AFM remained uncommon during this EV-D68 respiratory outbreak (Colorado CDC-classified suspected AFM cases in 2022: **4**, versus **17** in 2018). (messacar2024multimodalsurveillancemodel pages 5-7)

### 9.2 Sex ratio and geographic distribution
Not available from the retrieved evidence set.

---

## 10. Diagnostics

### 10.1 Diagnostic criteria (CDC-based)
* Clinical: acute onset flaccid limb weakness.
* Imaging: MRI spinal lesion predominantly in gray matter spanning ≥1 vertebral segment. (whitehouse2024surveillanceforacute pages 1-2, kidd2020vitalsignsclinical pages 1-2)

### 10.2 Imaging findings
* MRI hallmark: spinal cord gray-matter–predominant lesions, often longitudinally extensive early.
* Example case (Belgium, EV-D68-associated): cervical cord central gray matter T2 hyperintensity (C2–C7) with posterior brainstem involvement. (rodesch2024afirstcase pages 1-3)

### 10.3 CSF and virologic testing
* CSF pleocytosis is common in peak-year cases (e.g., 87% in 2018 in CDC surveillance summaries). (whitehouse2024surveillanceforacute pages 4-5)
* Etiologic agent detection is typically from **non-sterile sites** (respiratory/stool) rather than CSF; CDC notes EV/RV RT-PCR often requires sequencing for typing because assays may not distinguish EVs from rhinoviruses without additional testing. (whitehouse2024surveillanceforacute pages 1-2, kidd2020vitalsignsclinical pages 1-2)

### 10.4 Electrodiagnostics (EMG/NCS)
Rehabilitation review describes a pattern consistent with motor neuronopathy/neuropathy with relative preservation of sensory conduction in most cases. (ide2021acuteflaccidmyelitis. pages 11-13)

### 10.5 Differential diagnosis
A complete differential is not enumerated in the retrieved evidence set; however, case and protocol literature emphasizes the need for prompt workup to distinguish AFM from other causes of acute flaccid paralysis. (rodesch2024afirstcase pages 1-3, vawterlee2021acuteflaccidmyelitis pages 2-3)

---

## 11. Outcome / Prognosis

### 11.1 Short-term severity (hospital course)
Across U.S. surveillance summaries (2018–2022), severe disease was frequent: ICU admission **54%**, respiratory support **27%**, mechanical ventilation **23%**. (whitehouse2024surveillanceforacute pages 5-6)

### 11.2 Long-term disability and recovery
AFM frequently results in incomplete recovery and long-term sequelae (residual weakness, atrophy, and other neurological/musculoskeletal impacts), as summarized in a major clinical review. (murphy2021acuteflaccidmyelitis pages 1-2)

Case-level prognosis can be poor: the Belgium EV-D68-associated case had persistent proximal arm paresis with shoulder atrophy years later (as summarized in the report excerpt), and authors emphasize poor functional prognosis. (rodesch2024afirstcase pages 3-5)

### 11.3 Prognostic factor example (upper extremity)
In a surgical referral cohort, **“none of the patients with M0 shoulder abduction at the 6-month evaluation recovered M1 or better”**, supporting the use of 6-month post-onset strength as a decision point for surgical reconstruction consideration. (doi2024midtermoutcomesof pages 12-13, doi2024midtermoutcomesof pages 11-12)

---

## 12. Treatment

### 12.1 Acute pharmacologic/immunomodulatory therapies (current practice; evidence gaps)
CDC surveillance documents real-world use (not efficacy) of:
* **Steroids alone:** 23%
* **IVIG alone:** 23%
* **Steroids + IVIG:** 34%
* **Plasma exchange (PLEX):** 13% (whitehouse2024surveillanceforacute pages 5-6)

Case literature emphasizes absence of evidence-based guidelines and that management is largely supportive, with controversial corticosteroid use and variable IVIG response. (rodesch2024afirstcase pages 3-5)

**Suggested MAXO terms (candidates):** intravenous immunoglobulin therapy; therapeutic plasma exchange; systemic corticosteroid therapy; supportive respiratory care.

### 12.2 Rehabilitation and real-world implementations (including 2024 innovations)
**Comprehensive rehabilitation** is consistently emphasized as central to functional improvement and quality of life, even without proven disease-modifying therapy. (murphy2021acuteflaccidmyelitis pages 1-2, ide2021acuteflaccidmyelitis. pages 11-13)

**2024 development—neuromodulation-assisted gait rehab:** A 4-child case series used **transcutaneous spinal cord stimulation (TSS)** paired with intensive gait training (22 sessions over 5–8 weeks). Feasibility/safety: **98.48% session completion** and **no significant adverse events**; walking endurance improved (6MWT increased by +98.3 m, +68 m, +9.4 m, +49.4 m; 3/4 exceeded MCID). (neighbors2024transcutaneousspinalcord pages 5-8, neighbors2024transcutaneousspinalcord pages 1-2)

**Suggested MAXO terms (candidates):** physical therapy; gait training; transcutaneous spinal cord stimulation; body-weight–supported treadmill training.

### 12.3 Surgical and interventional management
A 2024 cohort study reports nerve transfers, muscle/tendon transfers, and free muscle transfers for persistent deficits; elbow and hand reconstructions showed more consistent outcomes than shoulder reconstructions. (doi2024midtermoutcomesof pages 1-2)

**Suggested MAXO terms (candidates):** nerve transfer surgery; tendon transfer; free functional muscle transfer; orthopedic reconstruction.

### 12.4 Clinical trials / registries
**NCT03499366** (ClinicalTrials.gov; first posted 2018-04-17; last update posted 2018-05-11): European pediatric AFM-EV-D68 follow-up study targeting ~40 participants with EV-D68 PCR positivity and MRI-confirmed myelitis, assessing functional outcomes including Hammersmith Functional Motor Scale at 1–3 years and secondary outcomes including ventilator/ICU days and quality of life. (NCT03499366 chunk 1)

---

## 13. Prevention

### 13.1 Primary prevention
No licensed EV-D68 vaccine or AFM-specific preventive therapy is supported in the retrieved evidence set; prevention is currently focused on public health surveillance/early warning and infection control during enterovirus circulation periods. (rodesch2024afirstcase pages 3-5, messacar2024multimodalsurveillancemodel pages 3-5)

### 13.2 Public health implementations (2024 evidence)
A 2024 Colorado program illustrates **multimodal surveillance** (syndromic ED asthma visits, EV-D68 RT-PCR confirmation, wastewater testing) enabling real-time preparedness actions including provider outreach and surge planning. (messacar2024multimodalsurveillancemodel pages 7-8, messacar2024multimodalsurveillancemodel pages 3-5)

---

## 14. Other Species / Natural Disease
No naturally occurring non-human AFM equivalent was identified in the retrieved evidence set.

---

## 15. Model Organisms

### 15.1 Human organoid models (high relevance to AFM)
Human spinal cord organoids provide a multicellular CNS model for EV-D68 neurotropism; contemporary EV-D68 strains infect and persist with modest cytopathic effect, supporting investigation of immune-mediated injury mechanisms and antiviral testing. (aguglia2023contemporaryenterovirusd68isolates pages 1-2, aguglia2023contemporaryenterovirusd68isolates pages 8-10)

### 15.2 Animal models (limited detail in retrieved evidence)
The organoid paper notes limitations of mouse models (often requiring neonatal or immunosuppressed mice, intracranial inoculation, or mouse-adapted viruses), reinforcing why complementary human models are needed. (aguglia2023contemporaryenterovirusd68isolates pages 1-2)

---

# Key evidence table

| Topic/Section | Key finding (with key numbers) | Population/Setting | Year | Source (first author, journal) | PMID if available | URL |
|---|---|---|---|---|---|---|
| Surveillance / epidemiology | U.S. confirmed AFM cases: 238 in 2018; then 47 (2019), 33 (2020), 28 (2021), 47 (2022). Confirmed AFM requires acute flaccid limb weakness plus MRI spinal cord lesion largely restricted to gray matter spanning ≥1 vertebral segment. 2018 cases were 94% aged <18 years; median age 5.3 years. ICU admission 54%, respiratory support 27%, mechanical ventilation 23%. EV-D68 detected in 37 cases in 2018; lower in later years. (whitehouse2024surveillanceforacute pages 1-2, whitehouse2024surveillanceforacute pages 5-6, whitehouse2024surveillanceforacute pages 4-5) | United States national AFM surveillance, 2018–2022 | 2024 | Whitehouse, MMWR |  | https://www.cdc.gov/mmwr/volumes/73/ss/ss7304a1.htm |
| Clinical characteristics | Among 238 confirmed AFM patients in 2018, median age was 5.3 years; 86% had onset during Aug–Nov; 92% had prodromal fever/respiratory illness beginning median 6 days before weakness; common findings: gait difficulty 52%, neck/back pain 47%, limb pain 34%; 98% hospitalized, 54% ICU, 23% intubated/mechanically ventilated. (kidd2020vitalsignsclinical pages 1-2) | United States confirmed AFM patients during 2018 peak year | 2020 | Kidd, MMWR |  | https://doi.org/10.15585/mmwr.mm6931e3 |
| Recent surveillance development | Multimodal Colorado EV-D68/AFM surveillance combined syndromic, clinical PCR, and wastewater data. From Jun 15–Nov 3, 2022, 529 EV/RV-positive respiratory specimens were tested and 121/529 (22.9%) were EV-D68-positive; peak weekly positivity 78.6% in late Aug 2022. Wastewater detection preceded the syndromic alarm by ~1 month/1–2 weeks depending on analytic layer. Colorado had 4 suspected AFM cases in 2022 versus 17 in 2018. (messacar2024multimodalsurveillancemodel pages 5-7, messacar2024multimodalsurveillancemodel pages 3-5, messacar2024multimodalsurveillancemodel pages 7-8) | Colorado, USA pediatric hospital/public-health surveillance during 2022 EV-D68 outbreak | 2024 | Messacar, Emerging Infectious Diseases |  | https://doi.org/10.3201/eid3003.231223 |
| Etiology / overall review | AFM is strongly associated with non-polio enteroviruses, especially EV-D68; direct virus detection in CSF is uncommon, but epidemiology, animal models, and CSF antibody studies support causality. Long-term recovery is often incomplete with residual weakness, atrophy, and neurologic/musculoskeletal sequelae; rehabilitation and selected nerve-transfer surgery may improve function. (murphy2021acuteflaccidmyelitis pages 1-2) | International review of human clinical, laboratory, and model-organism evidence | 2021 | Murphy, The Lancet |  | https://doi.org/10.1016/S0140-6736(20)32723-9 |
| Rehabilitation / outcomes | AFM rehab review notes electrodiagnostics usually show motor neuronopathy/neuropathy with preserved sensory conduction. Recovery is often poor; some series reported full recovery in only 10% or 41%. Greatest recovery generally occurs within 12 months, but gains may continue to 18 months. Supportive multidisciplinary rehab, ABRT, ventilatory management, diaphragmatic pacing, and nerve transfer surgery are discussed. (ide2021acuteflaccidmyelitis. pages 11-13) | Rehabilitation literature and AFM cohorts, largely pediatric | 2021 | Ide, PM&R Clinics of North America |  | https://doi.org/10.1016/j.pmr.2021.02.004 |
| Novel rehabilitation intervention | In a 4-patient pediatric case series, 22 sessions over 5–8 weeks of transcutaneous spinal cord stimulation (TSS) plus gait training were feasible and safe. Session completion was 98.48%; no significant adverse events. 6MWT improved by +98.3 m, +68 m, +9.4 m, and +49.4 m; 3/4 exceeded MCID. WISCI-II improved clinically in 2/4 participants. (neighbors2024transcutaneousspinalcord pages 3-5, neighbors2024transcutaneousspinalcord pages 5-8, neighbors2024transcutaneousspinalcord pages 1-2) | Four children with incomplete SCI secondary to AFM | 2024 | Neighbors, Children |  | https://doi.org/10.3390/children11091116 |
| Surgical reconstruction / prognosis | Retrospective cohort of 39 AFM patients (50 upper extremities). Recovery assessed at median 3, 6, and 37 months. Key prognostic result: none of the patients with M0 shoulder abduction at 6 months later recovered M1 or better. Twenty-seven patients (29 extremities) underwent reconstruction (nerve transfer, muscle-tendon transfer, free muscle transfer). Elbow/hand outcomes were more consistent than shoulder outcomes. (doi2024midtermoutcomesof pages 1-2, doi2024midtermoutcomesof pages 11-12, doi2024midtermoutcomesof pages 2-4) | AFM upper-extremity paralysis, 2011–2019 surgical referral cohort | 2024 | Doi, JBJS Open Access |  | https://doi.org/10.2106/JBJS.OA.23.00143 |
| Case report / diagnostic illustration | First reported Belgium AFM case linked to EV-D68: 4-year-old with acute right upper-limb palsy. MRI showed central gray matter T2 hyperintensity in cervical cord C2–C7 with posterior brainstem involvement; nasopharyngeal PCR positive for EV-D68; CSF enterovirus PCR negative. Authors note poor functional prognosis and no evidence-based treatment guideline. (rodesch2024afirstcase pages 3-5, rodesch2024afirstcase pages 1-3) | Single pediatric case, Belgium | 2024 | Rodesch, Case Reports in Neurology |  | https://doi.org/10.1159/000535316 |
| Prospective follow-up study / trial registry | ClinicalTrials.gov follow-up study of pediatric AFM associated with EV-D68 planned functional follow-up using Hammersmith Functional Motor Scale at 1–3 years; secondary outcomes include MRC scores, ACTIVLIM, PedsQL, ICU/mechanical ventilation duration, deaths, and complete recovery. Enrollment target 40; start date 2018-04-09. (NCT03499366 chunk 1) | European children <18 years with AFM, EV-D68 PCR positivity, MRI-confirmed myelitis | 2018 | Pfeiffer, ClinicalTrials.gov (NCT03499366) |  | https://clinicaltrials.gov/study/NCT03499366 |


*Table: This table summarizes high-yield evidence on acute flaccid myelitis across surveillance, etiology, diagnostics, rehabilitation, surgery, and follow-up research. It is designed to support a disease knowledge base entry with recent statistics, clinically actionable findings, and source links.*

---

## Expert opinion / authoritative analysis (from retrieved sources)
* CDC MMWR guidance emphasizes clinician vigilance for AFM in children with acute flaccid limb weakness and the importance of collecting adequate specimens for enterovirus testing. (whitehouse2024surveillanceforacute pages 1-2, kidd2020vitalsignsclinical pages 1-2)
* A major clinical review highlights persistent gaps: infrequent direct pathogen detection in CSF and a need for improved diagnostics and pathogenesis-driven therapeutics/prevention. (murphy2021acuteflaccidmyelitis pages 1-2)

---

## Notes on evidence gaps (for knowledge base curation)
* **Ontology identifiers (MONDO/MeSH/Orphanet/OMIM/ICD-10/ICD-11):** not retrievable from the current evidence set; recommended to supplement via MONDO/MeSH browsers and ICD crosswalks.
* **Genetic susceptibility/variants:** not supported in retrieved sources; AFM currently best represented as a syndrome with infectious association and immune-mediated injury.
* **Differential diagnosis and biomarker specificity:** only partially covered; additional guideline-level sources would be needed for a complete differential and test performance metrics.



References

1. (whitehouse2024surveillanceforacute pages 1-2): ER Whitehouse. Surveillance for acute flaccid myelitis―united states, 2018–2022. Unknown journal, 2024.

2. (kidd2020vitalsignsclinical pages 1-2): Sarah Kidd, Adriana Lopez, W. Allan Nix, Gloria Anyalechi, Megumi Itoh, Eileen Yee, M. Steven Oberste, and Janell Routh. Vital signs: clinical characteristics of patients with confirmed acute flaccid myelitis, united states, 2018. Morbidity and Mortality Weekly Report, 69:1031-1038, Aug 2020. URL: https://doi.org/10.15585/mmwr.mm6931e3, doi:10.15585/mmwr.mm6931e3. This article has 24 citations.

3. (messacar2024multimodalsurveillancemodel pages 3-5): K. Messacar, Shannon Matzinger, Kevin Berg, Kirsten Weisbeck, Molly Butler, Nicholas J Pysnack, Hai Nguyen-Tran, Emily Spence Davizon, Laura Bankers, Sarah A. Jung, Meghan C Birkholz, Allison Wheeler, and Samuel R. Dominguez. Multimodal surveillance model for enterovirus d68 respiratory disease and acute flaccid myelitis among children in colorado, usa, 2022. Emerging Infectious Diseases, 30:423-431, Mar 2024. URL: https://doi.org/10.3201/eid3003.231223, doi:10.3201/eid3003.231223. This article has 22 citations and is from a domain leading peer-reviewed journal.

4. (rodesch2024afirstcase pages 1-3): Marine Rodesch, Claudine Sculier, Valentina Lolli, Gauthier Remiche, Iris Delpire, Christophe Fricx, Françoise Vermeulen, and Florence Christiaens. A first case of acute flaccid myelitis related to enterovirus d68 in belgium: case report. Case Reports in Neurology, 16:41-47, Jan 2024. URL: https://doi.org/10.1159/000535316, doi:10.1159/000535316. This article has 4 citations and is from a peer-reviewed journal.

5. (doi2024midtermoutcomesof pages 1-2): Kazuteru Doi, Yasunori Hattori, Sotetsu Sakamoto, Dawn Sinn Yii Chia, Vijayendrasingh Gour, and Jun Sasaki. Midterm outcomes of surgical reconstruction and spontaneous recovery of upper-extremity paralysis following acute flaccid myelitis. JBJS Open Access, Apr 2024. URL: https://doi.org/10.2106/jbjs.oa.23.00143, doi:10.2106/jbjs.oa.23.00143. This article has 1 citations.

6. (aguglia2023contemporaryenterovirusd68isolates pages 1-2): Gabrielle Aguglia, Carolyn B. Coyne, Terence S. Dermody, John V. Williams, and Megan Culler Freeman. Contemporary enterovirus-d68 isolates infect human spinal cord organoids. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.01058-23, doi:10.1128/mbio.01058-23. This article has 22 citations and is from a domain leading peer-reviewed journal.

7. (rodesch2024afirstcase pages 3-5): Marine Rodesch, Claudine Sculier, Valentina Lolli, Gauthier Remiche, Iris Delpire, Christophe Fricx, Françoise Vermeulen, and Florence Christiaens. A first case of acute flaccid myelitis related to enterovirus d68 in belgium: case report. Case Reports in Neurology, 16:41-47, Jan 2024. URL: https://doi.org/10.1159/000535316, doi:10.1159/000535316. This article has 4 citations and is from a peer-reviewed journal.

8. (neighbors2024transcutaneousspinalcord pages 5-8): Elizabeth Neighbors, Lia Brunn, Agostina Casamento-Moran, and Rebecca Martin. Transcutaneous spinal cord stimulation enables recovery of walking in children with acute flaccid myelitis. Children, 11:1116, Sep 2024. URL: https://doi.org/10.3390/children11091116, doi:10.3390/children11091116. This article has 2 citations.

9. (murphy2021acuteflaccidmyelitis pages 1-2): Olwen C Murphy, Kevin Messacar, Leslie Benson, Riley Bove, Jessica L Carpenter, Thomas Crawford, Janet Dean, Roberta DeBiasi, Jay Desai, Matthew J Elrick, Raquel Farias-Moeller, Grace Y Gombolay, Benjamin Greenberg, Matthew Harmelink, Sue Hong, Sarah E Hopkins, Joyce Oleszek, Catherine Otten, Cristina L Sadowsky, Teri L Schreiner, Kiran T Thakur, Keith Van Haren, Carolina M Carballo, Pin Fee Chong, Amary Fall, Vykuntaraju K Gowda, Jelte Helfferich, Ryutaro Kira, Ming Lim, Eduardo L Lopez, Elizabeth M Wells, E Ann Yeh, Carlos A Pardo, Andrea Salazar-Camelo, Divakar Mithal, Molly Wilson-Murphy, Andrea Bauer, Colyn Watkins, Mark Abzug, Samuel Dominguez, Craig Press, Michele Yang, Nusrat Ahsan, Leigh Ramos-Platt, Emmanuelle Tiongson, Mitchel Seruya, Ann Tilton, Elana Katz, Matthew Kirschen, Apurva Shah, Erlinda Ulloa, Sabrina Yum, Lileth Mondok, Megan Blaufuss, Amy Rosenfeld, Wendy Vargas, Jason Zucker, Anusha Yeshokumar, Allison Navis, Kristen Chao, Kaitlin Hagen, Michelle Melicosta, Courtney Porter, Margaret Tunney, Richard Scheuermann, Priya Duggal, Andrew Pekosz, Amy Bayliss, Meghan Moore, Allan Belzberg, Melania Bembea, Caitlin O'Brien, Rebecca Riggs, Jessica Nance, Aaron Milstone, Jessica Rice, Maria A. Garcia-Dominguez, Eoin Flanagan, Jan-Mendelt Tillema, Glendaliz Bosques, Sonal Bhatia, Eliza Gordon-Lipkin, Dawn Deike, Gadi Revivo, Dan Zlotolow, Gabrielle deFiebre, Peggy Lazerow, Timothy Lotze, Ari Bitnun, Kristen Davidge, Jiri Vajsar, Amy Moore, Chamindra Konersman, Kendall Nash, Jonathan Strober, Nalin Gupta, Charles Chiu, Michael Sweeney, William Jackson, Dennis Simon, Kavita Thakkar, Jonathan Cheng, John Luce, Suman Das, Matthew Vogt, NgocHanh Vu, Jacqueline Gofshteyn, Naila Makhani, and Payal Patel. Acute flaccid myelitis: cause, diagnosis, and management. The Lancet, 397:334-346, Jan 2021. URL: https://doi.org/10.1016/s0140-6736(20)32723-9, doi:10.1016/s0140-6736(20)32723-9. This article has 195 citations and is from a highest quality peer-reviewed journal.

10. (whitehouse2024surveillanceforacute pages 5-6): ER Whitehouse. Surveillance for acute flaccid myelitis―united states, 2018–2022. Unknown journal, 2024.

11. (whitehouse2024surveillanceforacute pages 6-7): ER Whitehouse. Surveillance for acute flaccid myelitis―united states, 2018–2022. Unknown journal, 2024.

12. (whitehouse2024surveillanceforacute pages 4-5): ER Whitehouse. Surveillance for acute flaccid myelitis―united states, 2018–2022. Unknown journal, 2024.

13. (vawterlee2021acuteflaccidmyelitis pages 2-3): Marissa Vawter-Lee, Katrina Peariso, Mary Frey, Priya Bolikal, Joshua K. Schaffzin, Ann Schwentker, William T. O’Brien, Ronine Zamor, and Benjamin T. Kerrey. Acute flaccid myelitis: a multidisciplinary protocol to optimize diagnosis and evaluation. Journal of Child Neurology, 36:421-431, Dec 2021. URL: https://doi.org/10.1177/0883073820975230, doi:10.1177/0883073820975230. This article has 10 citations and is from a peer-reviewed journal.

14. (aguglia2023contemporaryenterovirusd68isolates pages 5-8): Gabrielle Aguglia, Carolyn B. Coyne, Terence S. Dermody, John V. Williams, and Megan Culler Freeman. Contemporary enterovirus-d68 isolates infect human spinal cord organoids. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.01058-23, doi:10.1128/mbio.01058-23. This article has 22 citations and is from a domain leading peer-reviewed journal.

15. (aguglia2023contemporaryenterovirusd68isolates pages 2-5): Gabrielle Aguglia, Carolyn B. Coyne, Terence S. Dermody, John V. Williams, and Megan Culler Freeman. Contemporary enterovirus-d68 isolates infect human spinal cord organoids. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.01058-23, doi:10.1128/mbio.01058-23. This article has 22 citations and is from a domain leading peer-reviewed journal.

16. (aguglia2023contemporaryenterovirusd68isolates pages 8-10): Gabrielle Aguglia, Carolyn B. Coyne, Terence S. Dermody, John V. Williams, and Megan Culler Freeman. Contemporary enterovirus-d68 isolates infect human spinal cord organoids. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.01058-23, doi:10.1128/mbio.01058-23. This article has 22 citations and is from a domain leading peer-reviewed journal.

17. (aguglia2023contemporaryenterovirusd68isolates pages 10-12): Gabrielle Aguglia, Carolyn B. Coyne, Terence S. Dermody, John V. Williams, and Megan Culler Freeman. Contemporary enterovirus-d68 isolates infect human spinal cord organoids. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.01058-23, doi:10.1128/mbio.01058-23. This article has 22 citations and is from a domain leading peer-reviewed journal.

18. (dabilla2025strainspecifictropismand pages 9-10): Nathânia Dábilla, Sarah Maya, Colton McNinch, Taylor Eddens, Patrick T. Dolan, and Megan Culler Freeman. Strain-specific tropism and transcriptional responses of enterovirus d68 infection in human spinal cord organoids. Frontiers in Microbiology, Nov 2025. URL: https://doi.org/10.3389/fmicb.2025.1698639, doi:10.3389/fmicb.2025.1698639. This article has 6 citations and is from a peer-reviewed journal.

19. (ide2021acuteflaccidmyelitis. pages 11-13): William Ide, Michelle Melicosta, and Melissa K. Trovato. Acute flaccid myelitis. Physical medicine and rehabilitation clinics of North America, 32 3:477-491, Aug 2021. URL: https://doi.org/10.1016/j.pmr.2021.02.004, doi:10.1016/j.pmr.2021.02.004. This article has 15 citations and is from a peer-reviewed journal.

20. (messacar2024multimodalsurveillancemodel pages 5-7): K. Messacar, Shannon Matzinger, Kevin Berg, Kirsten Weisbeck, Molly Butler, Nicholas J Pysnack, Hai Nguyen-Tran, Emily Spence Davizon, Laura Bankers, Sarah A. Jung, Meghan C Birkholz, Allison Wheeler, and Samuel R. Dominguez. Multimodal surveillance model for enterovirus d68 respiratory disease and acute flaccid myelitis among children in colorado, usa, 2022. Emerging Infectious Diseases, 30:423-431, Mar 2024. URL: https://doi.org/10.3201/eid3003.231223, doi:10.3201/eid3003.231223. This article has 22 citations and is from a domain leading peer-reviewed journal.

21. (doi2024midtermoutcomesof pages 12-13): Kazuteru Doi, Yasunori Hattori, Sotetsu Sakamoto, Dawn Sinn Yii Chia, Vijayendrasingh Gour, and Jun Sasaki. Midterm outcomes of surgical reconstruction and spontaneous recovery of upper-extremity paralysis following acute flaccid myelitis. JBJS Open Access, Apr 2024. URL: https://doi.org/10.2106/jbjs.oa.23.00143, doi:10.2106/jbjs.oa.23.00143. This article has 1 citations.

22. (doi2024midtermoutcomesof pages 11-12): Kazuteru Doi, Yasunori Hattori, Sotetsu Sakamoto, Dawn Sinn Yii Chia, Vijayendrasingh Gour, and Jun Sasaki. Midterm outcomes of surgical reconstruction and spontaneous recovery of upper-extremity paralysis following acute flaccid myelitis. JBJS Open Access, Apr 2024. URL: https://doi.org/10.2106/jbjs.oa.23.00143, doi:10.2106/jbjs.oa.23.00143. This article has 1 citations.

23. (neighbors2024transcutaneousspinalcord pages 1-2): Elizabeth Neighbors, Lia Brunn, Agostina Casamento-Moran, and Rebecca Martin. Transcutaneous spinal cord stimulation enables recovery of walking in children with acute flaccid myelitis. Children, 11:1116, Sep 2024. URL: https://doi.org/10.3390/children11091116, doi:10.3390/children11091116. This article has 2 citations.

24. (NCT03499366 chunk 1): Helle Cecilie Viekilde Pfeiffer. European Paediatric AFM Associated With EV-D68 Follow-up Study.. Oslo University Hospital. 2018. ClinicalTrials.gov Identifier: NCT03499366

25. (messacar2024multimodalsurveillancemodel pages 7-8): K. Messacar, Shannon Matzinger, Kevin Berg, Kirsten Weisbeck, Molly Butler, Nicholas J Pysnack, Hai Nguyen-Tran, Emily Spence Davizon, Laura Bankers, Sarah A. Jung, Meghan C Birkholz, Allison Wheeler, and Samuel R. Dominguez. Multimodal surveillance model for enterovirus d68 respiratory disease and acute flaccid myelitis among children in colorado, usa, 2022. Emerging Infectious Diseases, 30:423-431, Mar 2024. URL: https://doi.org/10.3201/eid3003.231223, doi:10.3201/eid3003.231223. This article has 22 citations and is from a domain leading peer-reviewed journal.

26. (neighbors2024transcutaneousspinalcord pages 3-5): Elizabeth Neighbors, Lia Brunn, Agostina Casamento-Moran, and Rebecca Martin. Transcutaneous spinal cord stimulation enables recovery of walking in children with acute flaccid myelitis. Children, 11:1116, Sep 2024. URL: https://doi.org/10.3390/children11091116, doi:10.3390/children11091116. This article has 2 citations.

27. (doi2024midtermoutcomesof pages 2-4): Kazuteru Doi, Yasunori Hattori, Sotetsu Sakamoto, Dawn Sinn Yii Chia, Vijayendrasingh Gour, and Jun Sasaki. Midterm outcomes of surgical reconstruction and spontaneous recovery of upper-extremity paralysis following acute flaccid myelitis. JBJS Open Access, Apr 2024. URL: https://doi.org/10.2106/jbjs.oa.23.00143, doi:10.2106/jbjs.oa.23.00143. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Acute_Flaccid_Myelitis-deep-research-falcon_artifacts/artifact-00.md)
