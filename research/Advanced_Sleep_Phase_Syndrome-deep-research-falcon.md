---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T06:43:31.744820'
end_time: '2026-08-01T06:53:31.489041'
duration_seconds: 599.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Advanced Sleep Phase Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Advanced_Sleep_Phase_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Advanced Sleep Phase Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Advanced Sleep Phase Syndrome** covering all of the
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
- **Disease Name:** Advanced Sleep Phase Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Advanced Sleep Phase Syndrome** covering all of the
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


# Advanced Sleep Phase Syndrome: Disease Characteristics Report

## Executive summary

**Advanced sleep phase syndrome (ASPS)** is the older name for **advanced sleep–wake phase disorder (ASWPD)**, an intrinsic circadian rhythm sleep–wake disorder in which the principal sleep episode is stably advanced—usually by at least 2 hours—relative to desired or socially required times. Typical sleep occurs around 18:00–21:00, with awakening around 02:00–05:00. A diagnosis requires distress or functional impairment; an extreme “morning lark” who functions well is an advanced chronotype, not necessarily affected by ASWPD. Familial advanced sleep phase (FASP/FASPS) denotes the inherited phenotype and is usually autosomal dominant. (sun2022treatmentofcircadian pages 5-6, ashbrook2020geneticsofthe pages 4-5, auger2015clinicalpracticeguideline pages 9-10)

The best-established biology involves the core circadian transcription–translation feedback loop (TTFL). Rare variants affecting **PER2, CSNK1D, CRY2, PER3,** and **TIMELESS** can alter clock-protein phosphorylation, stability, nuclear localization, intrinsic period, or light entrainment. However, only a small number of families have been studied, penetrance can be incomplete, and environmental light schedules can mask or amplify the phenotype. (lane2023geneticsofcircadian pages 6-7, kurien2019timelessmutationalters pages 1-2)

The principal evidence-based treatment is correctly timed **evening bright-light therapy**, but the American Academy of Sleep Medicine (AASM) recommendation is only **WEAK FOR**, based on very-low-quality evidence. No disease-modifying drug, gene therapy, or approved genotype-specific treatment exists. (auger2015clinicalpracticeguideline pages 9-10)

---

## 1. Disease information

### Definition and identifiers

* **Preferred clinical name:** advanced sleep–wake phase disorder (ASWPD).
* **Synonyms:** advanced sleep phase syndrome/disorder (ASPS/ASPD), familial advanced sleep phase syndrome (FASPS), familial advanced sleep phase (FASP), advanced sleep phase type circadian rhythm sleep disorder.
* **MONDO:** **MONDO:0015609**, “advanced sleep phase syndrome.” Open Targets recognizes this entity but returned no curated disease–target associations, illustrating that absence from an aggregation platform does not negate the primary genetic literature. (OpenTargets Search: advanced sleep phase syndrome)
* **MeSH:** the broader concept **D020178, Sleep Disorders, Circadian Rhythm** is used in ClinicalTrials.gov indexing. (NCT00246454 chunk 1)
* **ICD-10-CM:** commonly coded **G47.22**, circadian rhythm sleep disorder, advanced sleep phase type. This code was not independently verified in the retrieved primary literature and should be checked against the deployment jurisdiction.
* **ICD-11:** classified under circadian rhythm sleep–wake disorders; the exact local extension/code should be verified against the current ICD-11 browser.
* **OMIM:** familial forms are represented as genetically heterogeneous FASPS entries; because exact OMIM disease-number mapping was not directly retrieved, OMIM numbers should not be populated without database verification.
* **Orphanet:** no independently verified dedicated Orphanet identifier was recovered.

This report primarily uses **aggregated disease-level resources, guidelines, primary family studies, and observational cohorts**, not individual EHR data. Family reports necessarily contain individual-level phenotyping, but the ClinicalTrials.gov records provide aggregated protocol information. (NCT00246454 chunk 1, NCT04690504 chunk 1)

### Key source quotation

The landmark PER2 report describes FASPS as “**an autosomal dominant circadian rhythm variant; affected individuals are ‘morning larks’ with a 4-hour advance of the sleep, temperature, and melatonin rhythms**.” Science, February 2001; DOI: [10.1126/science.1057499](https://doi.org/10.1126/science.1057499); PMID 11232563. (toh2001anhper2 pages 1-2)

---

## 2. Etiology

### Causal factors

ASWPD is etiologically heterogeneous:

1. **Rare Mendelian disease:** typically autosomal-dominant FASP caused by variants in core clock or clock-regulatory genes.
2. **Non-Mendelian advanced chronotype:** an extreme of polygenic sleep-timing variation.
3. **Age-associated phase advance:** earlier circadian timing becomes more common with aging and does not always constitute a disorder.
4. **Environmental/behavioral reinforcement:** morning light, insufficient evening light, rigid early schedules, and reduced evening activity can stabilize an advanced phase. (sun2022treatmentofcircadian pages 5-6, ashbrook2020geneticsofthe pages 4-5, lane2023geneticsofcircadian pages 6-7)

### Risk factors

* **Genetic:** pathogenic or candidate variants in **PER2, CSNK1D, CRY2, PER3,** and **TIMELESS**. A 2023 authoritative review also lists **CRY1** among rare variants implicated across advanced or delayed SWPD, but CRY1 is better established for delayed phase and should not automatically be annotated as an ASWPD-causal gene. (lane2023geneticsofcircadian pages 6-7)
* **Family history:** strongly increases suspicion of FASP, especially when multiple generations show very early sleep and wake times.
* **Age:** advanced sleep timing becomes increasingly common with age; this is a risk for the phenotype but not proof of Mendelian disease. (ashbrook2020geneticsofthe pages 4-5)
* **Sex:** one review reports higher prevalence in men, but robust population estimates are lacking. (sun2022treatmentofcircadian pages 5-6)
* **Light environment:** disproportionate early-day light and inadequate evening light favor phase advance. The effect depends on circadian timing, not simply total illumination.

### Protective factors

No validated **genetic protective allele** has been established. Potential environmental countermeasures include adequate evening light, avoiding excessive early-morning light when a delay is desired, regular sleep timing, and aligning work/social obligations with the patient’s biological schedule. These are management principles rather than proven primary prevention.

### Gene–environment interaction

Clock variants may change intrinsic period or the phase-resetting response to light. The 2023 genetics review emphasizes that implicated variants may be incompletely penetrant and their effects “masked by environmental factors”; controlled light and sleep schedules may therefore reveal phenotypes missed in ordinary conditions. (lane2023geneticsofcircadian pages 6-7)

---

## 3. Phenotypes

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Advanced sleep onset | Behavioral/physiological; commonly 18:00–21:00; stable and chronic | **HP:0002367, Abnormality of sleep**; use a local extension for advanced sleep phase |
| Early awakening | Symptom; commonly 02:00–05:00; may be perceived as terminal insomnia | **HP:0002367**; **HP:0100785, Insomnia** when applicable |
| Excessive evening sleepiness | Symptom; worsens when remaining awake for social or occupational demands | **HP:0002329, Drowsiness** or **HP:0002189, Excessive daytime sleepiness** with timing qualifier |
| Sleep-maintenance/early-morning insomnia | Symptom when attempting conventional hours | **HP:0100785, Insomnia** |
| Normal sleep on preferred schedule | Distinguishing clinical feature; sleep quality and quantity improve when unrestricted | No disease HPO term; record as contextual qualifier |
| Advanced melatonin rhythm | Laboratory/physiological phase marker | **HP:0012686, Abnormality of circadian rhythm** where supported |
| Advanced core-temperature rhythm | Physiological sign | **HP:0012686** |
| Social/occupational impairment | Functional consequence: curtailed evening activity, inability to meet family/work schedules, or sleep loss when resisting early sleep | **HP:0031473, Impaired social interactions** only if clinically documented; otherwise ICF coding is preferable |

Symptoms must persist for **at least 3 months**, and objective records should demonstrate a stable advance. Severity varies from benign morning preference to clinically important evening sleepiness, insomnia, and schedule-related sleep restriction. Sleep itself is usually consolidated and normal when the patient follows the preferred schedule. (dodson2010therapeuticsforcircadian pages 4-5, sun2022treatmentofcircadian pages 5-6, auger2015clinicalpracticeguideline pages 9-10)

Frequency estimates for individual symptoms are unavailable; most literature consists of small families, clinic cohorts, or elderly samples. Disease-specific EQ-5D, SF-36, or PROMIS estimates were not identified.

---

## 4. Genetic and molecular information

The variant evidence is summarized below. “Established” here means replicated functional evidence in the source family/model, not necessarily a current ClinGen gene–disease validity classification.

| Gene | Variant / protein change | Human evidence | Functional consequence | Model evidence | Confidence / caveat |
|---|---|---|---|---|---|
| **PER2** | **S662G** | Landmark FASPS family study localized disease to chromosome 2qter and identified a serine-to-glycine change in the CKIε-binding region of hPER2; autosomal dominant segregation reported in the original family (toh2001anhper2 pages 1-2) | Causes **hypophosphorylation by CKIε in vitro**; interpreted as altering clock timing/period and producing phase advance (toh2001anhper2 pages 1-2) | Animal-model details not directly verified in gathered evidence; later reviews state rare advanced-SWPD variants were functionally linked to phosphorylation changes in mice, but not variant-specific here (lane2023geneticsofcircadian pages 6-7) | **Established** FASPS gene/variant pair; exact HGVS genomic/cDNA notation not verified in gathered evidence |
| **CSNK1D** | **T44A** | Included by reviews as a rare Mendelian advanced-SWPD / FASP gene; familial autosomal dominant evidence is referenced in review literature, but the primary report was not directly retrieved here (dodson2010therapeuticsforcircadian pages 4-5, lane2023geneticsofcircadian pages 6-7) | Review-level evidence indicates altered circadian phosphorylation biology and shortened physiological circadian cycle, but variant-specific mechanism was **not directly verified in gathered evidence** (sun2022treatmentofcircadian pages 5-6, lane2023geneticsofcircadian pages 6-7) | Review-level statement notes functional links to phosphorylation changes in mice for rare advanced-SWPD variants broadly; **T44A-specific model details not directly verified here** (lane2023geneticsofcircadian pages 6-7) | **Established gene, variant included as likely established candidate**, but this table cannot verify the exact primary-study details beyond review support |
| **CRY2** | **A260T** | Review and PNAS background text identify **CRY2** as a prior FASP gene; exact A260T variant is commonly cited for FASP, but the primary human report was **not directly retrieved** in gathered evidence (lane2023geneticsofcircadian pages 6-7, kurien2019timelessmutationalters pages 1-2) | Background text states prior FASP mutations in negative regulators share **PER/CRY instability** and derepression of BMAL1/CLOCK; applying that specifically to A260T is **inference from review/background, not directly verified here** (kurien2019timelessmutationalters pages 1-2) | No A260T-specific animal/cellular model details directly verified in gathered evidence | **Candidate/likely established variant in field**, but variant-specific human and mechanistic details were not directly verified in the retrieved primary evidence |
| **PER3** | **P415A / H417R** | Review/background sources state **PER3** mutations have been reported in FASP; a 2024 paper on **PER2/PER3 variants** was unobtainable, and exact primary evidence for the double substitution was not directly retrieved (lane2023geneticsofcircadian pages 6-7, kurien2019timelessmutationalters pages 1-2) | PNAS background states prior FASP mutations in PER2/CRY2/PER3 show **instability of PER and CRY**, causing derepression of BMAL1/CLOCK and shortened period, but **PER3 P415A/H417R-specific mechanism was not directly verified** (kurien2019timelessmutationalters pages 1-2) | No PER3 P415A/H417R-specific model evidence directly verified in gathered evidence | **Candidate/field-recognized association**, but the specific variant-level evidence remains indirect in this evidence set |
| **TIMELESS** | **R1081X** | PNAS primary study reports a **small family with two FASP individuals and one non-FASP subject**; mutation in **human TIMELESS** reported as causing FASP (kurien2019timelessmutationalters pages 6-7, kurien2019timelessmutationalters pages 1-2) | Prevents TIM nuclear accumulation, causes **exclusive cytoplasmic localization**, **lower stability**, **reduced affinity for CRY2**, weakened CLOCK-BMAL1 repression, and destabilization of the **PER/CRY complex**; alters light entrainment with preserved organismal period (kurien2019timelessmutationalters pages 6-7, kurien2019timelessmutationalters pages 1-2) | **CRISPR mutant mice** recapitulated advanced sleep phase with altered photic entrainment and normal circadian period; shortened period seen in CRISPR-generated cells and MEFs (kurien2019timelessmutationalters pages 6-7, kurien2019timelessmutationalters pages 1-2) | **Established but rare**; family was small and variant was reported absent from public databases as of the study period; strongest evidence among newer genes in gathered set |


*Table: This table summarizes established and candidate familial advanced sleep phase genes and variants requested by the user, separating directly verified evidence from review-level or indirect support. It is useful for distinguishing high-confidence variant-mechanism pairs from associations that require primary-source confirmation.*

### Interpretation cautions

* **PER2 p.Ser662Gly (S662G):** germline missense variant in the CKIε-binding region; caused hypophosphorylation in vitro and segregated as a highly penetrant autosomal-dominant trait in the original family. (toh2001anhper2 pages 1-2)
* **TIMELESS p.Arg1081Ter (R1081X):** germline nonsense variant identified in a very small family; absent from public genome databases at the investigators’ 2018 cutoff. It causes protein instability and abnormal cytoplasmic retention rather than a conventional simple loss-of-function phenotype. (kurien2019timelessmutationalters pages 6-7, kurien2019timelessmutationalters pages 1-2)
* **CSNK1D T44A, CRY2 A260T, and PER3 P415A/H417R:** field-recognized FASP variants, but variant-level ClinVar classification, HGVS transcripts, and present-day gnomAD frequencies were not directly verified in the retrieved evidence. They should be curated from ClinVar/gnomAD against a specified transcript before knowledge-base ingestion.
* **Somatic variants:** not implicated; reported FASP variants are inherited germline variants.
* **Chromosomal abnormalities, repeat expansions, mitochondrial variants, and large recurrent CNVs:** no established role.
* **Modifier genes/epigenetics:** no validated modifier or disease-specific methylation signature is established.

The 2023 review warns that only limited families have been studied and recommends requiring variants in multiple unrelated affected individuals plus statistical segregation before confidently assigning a new gene. (lane2023geneticsofcircadian pages 6-7)

---

## 5. Environmental information

No toxin, infection, radiation exposure, pollution source, smoking pattern, diet, or occupational chemical exposure is known to cause Mendelian FASP. **Light is the dominant environmental zeitgeber**. Morning light tends to advance the clock, whereas appropriately timed evening light delays it. Shift work and transmeridian travel can mimic or obscure phase disorders; both were exclusion criteria in major observational protocols. (NCT00246454 chunk 1, NCT04690504 chunk 1)

Alcohol, caffeine, exercise, and irregular schedules can alter sleep expression but are not established primary causes. Infectious agents and zoonotic transmission are **not applicable**.

---

## 6. Mechanism and pathophysiology

### Core causal chain

**Clock-gene variant → altered phosphorylation/protein stability or light entrainment → abnormal PER/CRY negative feedback on CLOCK–BMAL1 → shortened or differently entrained circadian oscillation → early melatonin/temperature/sleep-propensity phase → evening sleepiness and early awakening → impairment when social time conflicts with biological time.** (toh2001anhper2 pages 1-2, kurien2019timelessmutationalters pages 1-2)

In the canonical TTFL, CLOCK–BMAL1 activates circadian genes, including **PER** and **CRY**. PER/CRY complexes accumulate, enter the nucleus, and repress CLOCK–BMAL1. Their phosphorylation, turnover, and nuclear transport determine period and phase.

* **PER2 S662G:** impaired CKIε-dependent phosphorylation alters clock timing. (toh2001anhper2 pages 1-2)
* **TIMELESS R1081X:** prevents nuclear TIM accumulation, reduces CRY2 affinity, destabilizes the PER/CRY complex, and weakens repression of CLOCK–BMAL1. Unlike classic short-period variants, mutant mice show an advanced phase and abnormal photic entrainment with a normal organismal free-running period. (kurien2019timelessmutationalters pages 6-7, kurien2019timelessmutationalters pages 1-2)

### Upstream versus downstream

* **Upstream:** germline clock variant and retinal light input.
* **Intermediate:** SCN TTFL kinetics, kinase activity, PER/CRY stability, and phase-response behavior.
* **Downstream:** advanced pineal melatonin secretion, body-temperature nadir, sleep propensity, endocrine/autonomic rhythms, and behavior.
* **Clinical endpoint:** mismatch between biological night and desired social schedule.

### Cells, tissues, and ontology suggestions

* **Primary cells:** SCN circadian pacemaker neurons—suggest **CL:0000540 neuron**, with an SCN-specific extension; intrinsically photosensitive retinal ganglion cells (**CL:0000740 retinal ganglion cell**) provide photic input; pinealocytes produce melatonin.
* **GO biological processes:** circadian rhythm (**GO:0007623**), regulation of circadian rhythm (**GO:0042752**), entrainment of circadian clock by photoperiod (**GO:0043153**), protein phosphorylation (**GO:0006468**), transcriptional repression.
* **GO cellular components:** nucleus (**GO:0005634**), cytoplasm (**GO:0005737**), transcription regulator complex.

There is no established disease-specific immune activation, inflammation, tissue destruction, fibrosis, apoptosis, or metabolic-storage defect. Transcriptomic, proteomic, metabolomic, lipidomic, single-cell, and spatial signatures remain investigational rather than diagnostic.

---

## 7. Anatomical structures affected

ASWPD is primarily a **functional nervous-system timing disorder**, not a destructive lesion.

* **Central pacemaker:** suprachiasmatic nucleus of the anterior hypothalamus—suggest **UBERON:0002034 hypothalamus**, with SCN subdivision where supported.
* **Input pathway:** retina → retinohypothalamic tract → SCN; suggest **UBERON:0000966 retina**.
* **Output:** pineal gland/melatonin, autonomic and endocrine timing; suggest **UBERON:0001905 pineal body**.
* **Subcellular compartments:** nucleus and cytoplasm, particularly for PER/CRY/TIMELESS trafficking.
* **Lateralization:** none; circuitry is bilateral/systemic.

No structural MRI, histopathology, or biopsy abnormality is expected.

---

## 8. Temporal development

Onset is variable. Mendelian FASP can appear in childhood or early adulthood and often remains lifelong; age-associated advanced phase is predominantly later-life. Onset is generally chronic/insidious rather than acute. There are no formal stages or end-stage disease. Expression can fluctuate with season, light exposure, work schedule, retirement, and treatment adherence. (ashbrook2020geneticsofthe pages 4-5, lane2023geneticsofcircadian pages 6-7)

There is no established spontaneous remission rate. Phase delay achieved with light or scheduling may relapse after treatment stops because the underlying circadian tendency persists. Critical intervention windows are defined by **circadian phase**: mistimed light can shift the clock in the wrong direction.

---

## 9. Inheritance and population

### Epidemiology

Estimates vary because advanced chronotype, early awakening in older adults, and diagnostically impaired ASWPD are often conflated.

* A 2023 genetics review reports ICSD-defined advanced SWPD prevalence **up to 0.21%**. (lane2023geneticsofcircadian pages 6-7)
* Another synthesis estimates **at least 0.04% (1 in 2,500)**, based on approximately one in eight people with advanced sleep phase meeting disorder criteria. (ashbrook2020geneticsofthe pages 4-5)
* Reviews citing broader or older samples report **1–7%**, and an elderly survey reported early waking in **20%**; these figures should not be interpreted as genetically confirmed FASP prevalence. (sun2022treatmentofcircadian pages 5-6)
* Incidence per 100,000 person-years is unknown.

### Inheritance

Familial cases usually show **autosomal-dominant** inheritance. The original PER2 family was described as highly penetrant, but penetrance across genes and families is not quantified and may be age- and environment-dependent. Expressivity is variable. Anticipation, germline mosaicism, consanguinity effects, carrier frequency, and reproducible founder effects have not been established. (lane2023geneticsofcircadian pages 6-7, toh2001anhper2 pages 1-2)

No robust ethnic, geographic, or sex-ratio estimates exist. Existing pedigrees are too small and ancestrally limited to support population-specific conclusions.

---

## 10. Diagnostics

### Clinical criteria and workflow

1. Document a stable major sleep episode at least **2 hours earlier** than required or desired.
2. Confirm evening sleepiness and/or early-morning or maintenance insomnia causing distress or functional impairment.
3. Confirm duration **≥3 months**.
4. Establish that sleep quality and duration improve when the patient follows the naturally early schedule.
5. Record sleep diary plus wrist actigraphy for **≥7 days, preferably 14**, including work and free days.
6. Exclude another sleep, medical, neurologic, psychiatric, medication-related, occupational, or environmental explanation. (sun2022treatmentofcircadian pages 5-6, auger2015clinicalpracticeguideline pages 9-10)

**DLMO:** serial salivary or plasma melatonin under dim light can document an advanced biological phase. A completed 2024 biomarker study defined salivary DLMO as the time melatonin rose above **3 pg/mL**, with hourly samples beginning 7 hours before usual bedtime. (NCT04690504 chunk 1)

**Actigraphy:** useful for objective longitudinal timing; polysomnography is not routinely diagnostic but can exclude sleep apnea, periodic limb movements, or other sleep disorders.

### Differential diagnosis

* Normal extreme morning chronotype without impairment.
* Age-related early sleep timing.
* Major depression with terminal insomnia—sleep is often nonrestorative and the entire circadian phase need not be advanced.
* Primary insomnia.
* Insufficient sleep syndrome.
* Obstructive sleep apnea, restless legs syndrome, periodic limb-movement disorder.
* Medication/substance effects.
* Shift-work disorder, jet lag, irregular sleep–wake rhythm disorder, and non-24-hour sleep–wake rhythm disorder.
* Dementia-related fragmented sleep and sundowning.

### Genetic testing

Testing is most appropriate for a strongly familial, extreme, early-onset phenotype. A circadian-rhythm gene panel or exome/genome sequencing should include **PER2, CSNK1D, CRY2, PER3,** and **TIMELESS**, with cautious interpretation. Sequence and copy-number analysis is preferable to karyotyping or FISH. WES/WGS may identify novel variants, but segregation, population frequency, functional data, and ACMG/AMP classification are essential. CMA, mitochondrial sequencing, and repeat-expansion testing have no routine indication unless another phenotype suggests them.

Cascade testing is reasonable only after a pathogenic/likely pathogenic familial variant is established. Predictive testing of asymptomatic minors requires counseling because an early chronotype may not produce disease-level impairment.

### Emerging diagnostics

The completed **NCT04690504** study enrolled 50 adults and compared single-blood-sample proteomic and 15-transcript “body time” estimates with melatonin phase, demonstrating a current real-world attempt to make circadian phenotyping more accessible. Results establishing clinical validity were not available in the retrieved record. [ClinicalTrials.gov NCT04690504](https://clinicaltrials.gov/study/NCT04690504), completed July 1, 2024. (NCT04690504 chunk 1)

---

## 11. Outcome and prognosis

ASWPD is not known to shorten life expectancy or directly increase mortality. Five- or ten-year survival statistics are therefore not applicable. Morbidity is primarily functional: evening sleepiness, curtailed social participation, occupational incompatibility, insomnia when resisting the preferred schedule, and secondary sleep deprivation. Normal sleep duration and quality are often restored when schedules are aligned with biological time. (ashbrook2020geneticsofthe pages 4-5, auger2015clinicalpracticeguideline pages 9-10)

Prognosis is generally good when schedule accommodation is feasible. Persistent genetic or age-related phase tendency means treatment often requires ongoing behavioral/light management. No validated molecular prognostic biomarker exists.

---

## 12. Treatment

### Practical strategy

1. Confirm true circadian advance rather than insomnia or depression.
2. Where feasible, accommodate the naturally early schedule.
3. If phase delay is desired, use **evening light**, timed relative to DLMO/bedtime, and maintain a consistent delayed sleep–wake schedule.
4. Monitor symptoms and timing with diary/actigraphy; adjust to avoid paradoxical phase advance.
5. Treat comorbid insomnia, mood disorder, sleep apnea, or medication effects separately.

### Evening light therapy

A clinical review recommends at least **5,000 lux for approximately 2 hours in the evening/night**, but tolerance may be poor in older adults. (sun2022treatmentofcircadian pages 5-6)

The AASM guideline gives light therapy in adults with ASWPD a **WEAK FOR** recommendation with **VERY LOW** cumulative evidence. Its only identified randomized ASWPD trial included **47 participants**, mean age **70.0 ± 6.4 years**, and compared 28 days of broad-spectrum evening light (~265 lux for 2–3 hours, ending 1 hour before bedtime) with ~2-lux red light; no significant post-treatment group difference was found. (auger2015clinicalpracticeguideline pages 9-10)

Suggested ontology: **NCIT:C15407 Phototherapy**; light itself may be represented with an appropriate radiation/physical-agent term rather than CHEBI.

### Scheduling and behavioral care

Prescribed sleep scheduling has only case-report support; one 62-year-old maintained desired times at 5-month follow-up after chronotherapy. AASM issued **no recommendation** because evidence was insufficient. Timed exercise and strategic light avoidance also received no recommendation. (auger2015clinicalpracticeguideline pages 9-10)

Sleep hygiene supports regularity but is not a stand-alone circadian treatment. CBT-I may help comorbid conditioned insomnia but does not correct the clock variant itself.

### Melatonin and hypnotics

Evidence for melatonin in ASWPD is inadequate. In theory, carefully timed morning melatonin could delay circadian phase, but morning dosing may cause sleepiness and safety concerns; it is not supported by an AASM ASWPD recommendation. Evening melatonin would generally advance phase and may worsen ASWPD. (dodson2010therapeuticsforcircadian pages 4-5)

Hypnotics may suppress early-morning insomnia without correcting circadian phase. Disease-specific efficacy data are absent. Older adults face falls, confusion, amnesia, dependence, and next-day impairment; benzodiazepines and sedating antihistamines are particularly problematic. (auger2015clinicalpracticeguideline pages 9-10)

Suggested terms: **NCIT:C101216 Melatonin** where actually administered; melatonin is **CHEBI:16796**. There is no established pharmacogenomic guidance.

### Advanced and experimental therapies

No approved gene therapy, CRISPR therapy, RNA therapy, cell therapy, surgery, immunotherapy, or disease-specific targeted drug exists. The current translational emphasis is on phase biomarkers and personalized timing rather than molecular correction.

### Trials and implementations

* **NCT00246454:** completed observational Northwestern/NHLBI study of familial delayed and advanced sleep phase; **156 participants**, 2003–March 27, 2024. Participants underwent questionnaires/actigraphy, with sleep measured over one night and circadian profiles over three days. ASPS inclusion required morning type and advanced melatonin onset. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT00246454). (NCT00246454 chunk 1)
* **NCT04690504:** completed prospective biomarker-validation study, **50 participants**, comparing DLMO with transcriptomic/proteomic phase estimates. (NCT04690504 chunk 1)

No retrieved trial establishes a recent disease-specific drug response rate.

---

## 13. Prevention

Primary prevention of a germline FASP variant is not possible after conception. There is no vaccine, prophylactic medication, newborn screen, or population-screening program.

* **Primary:** maintain an appropriate light–dark schedule in genetically susceptible people; avoid chronic reinforcement of unwanted phase advance.
* **Secondary:** identify familial extreme morningness early when it causes school, work, or social impairment; use diary/actigraphy and targeted DLMO.
* **Tertiary:** prevent chronic sleep restriction, falls from sedating drugs, occupational impairment, and mood consequences by schedule accommodation and correctly timed light.
* **Genetic counseling:** explain autosomal-dominant transmission in established families, uncertain penetrance, variable impairment, and limitations of variant interpretation. Prenatal or preimplantation testing is technically possible after identification of a clearly pathogenic familial variant but is rarely proportionate for this generally manageable, non-lethal phenotype.

---

## 14. Other species and natural disease

No naturally occurring veterinary syndrome directly homologous to human FASP was established in the retrieved evidence. There is no zoonotic potential or cross-species transmission.

Circadian clock genes are strongly evolutionarily conserved. **PER2, CRY proteins, casein kinase 1δ, and TIMELESS orthologues** occur in mouse and other model species, enabling mechanistic comparison. Species-specific sleep architecture and light-response curves limit direct translation.

---

## 15. Model organisms

### Mouse

The strongest newer model is the **CRISPR TIMELESS R1081X knock-in mouse**. It recapitulated advanced sleep–wake phase and altered sensitivity to light pulses while retaining a normal organismal period. CRISPR-mutant cells and mouse embryonic fibroblasts showed a shortened period, illustrating that cellular period and whole-animal behavior need not align perfectly. (kurien2019timelessmutationalters pages 6-7, kurien2019timelessmutationalters pages 1-2)

This model is useful for separating **phase-response/entrainment defects** from pure period shortening. Limitations include the small human source family, nocturnal mouse behavior, and species-specific light processing.

### Cellular systems

HEK293T and U2OS cells, CRISPR-engineered cells, and mouse embryonic fibroblasts have been used to evaluate TIM localization, stability, CLOCK–BMAL1 repression, and PER/CRY destabilization. PER2 S662G was assessed by in-vitro phosphorylation assays. (kurien2019timelessmutationalters pages 6-7, toh2001anhper2 pages 1-2)

### Invertebrates

Drosophila established the conserved conceptual framework for period and timeless genes, but mammalian TIMELESS is not functionally identical to Drosophila Tim. Human disease inference therefore requires mammalian validation. (kurien2019timelessmutationalters pages 1-2)

---

## Recent developments and evidence gaps

The most authoritative recent synthesis, published in **Nature Reviews Genetics in 2023**, places ASWPD within a spectrum ranging from polygenic chronotype to rare Mendelian disease and emphasizes diverse-population sequencing, rigorous segregation, controlled phenotyping, and caution about incomplete penetrance. DOI: [10.1038/s41576-022-00519-z](https://doi.org/10.1038/s41576-022-00519-z). (lane2023geneticsofcircadian pages 6-7)

The principal 2024 implementation development was completion of observational studies attempting to validate convenient transcriptomic/proteomic circadian-phase biomarkers and characterize familial phase disorders. These do not yet replace diary, actigraphy, or DLMO. (NCT00246454 chunk 1, NCT04690504 chunk 1)

Major gaps are: reliable incidence and population prevalence; ancestry-diverse pedigrees; ClinGen-level gene validity; quantified penetrance; prospective natural history; ASWPD-specific quality-of-life instruments; adequately powered, phase-marker-guided light trials; and controlled studies of combination treatment. The evidence base remains much smaller than for delayed sleep–wake phase disorder, so precise treatment claims should remain conservative.

References

1. (sun2022treatmentofcircadian pages 5-6): Shi-Yu Sun and Gui-Hai Chen. Treatment of circadian rhythm sleep–wake disorders. Jun 2022. URL: https://doi.org/10.2174/1570159x19666210907122933, doi:10.2174/1570159x19666210907122933. This article has 128 citations and is from a peer-reviewed journal.

2. (ashbrook2020geneticsofthe pages 4-5): Liza H. Ashbrook, Andrew D. Krystal, Ying-Hui Fu, and Louis J. Ptáček. Genetics of the human circadian clock and sleep homeostat. Neuropsychopharmacology, 45:45-54, Aug 2020. URL: https://doi.org/10.1038/s41386-019-0476-7, doi:10.1038/s41386-019-0476-7. This article has 182 citations and is from a highest quality peer-reviewed journal.

3. (auger2015clinicalpracticeguideline pages 9-10): R. Robert Auger, Helen J. Burgess, Jonathan S. Emens, Ludmila V. Deriy, Sherene M. Thomas, and Katherine M. Sharkey. Clinical practice guideline for the treatment of intrinsic circadian rhythm sleep-wake disorders: advanced sleep-wake phase disorder (aswpd), delayed sleep-wake phase disorder (dswpd), non-24-hour sleep-wake rhythm disorder (n24swd), and irregular sleep-wake rhythm disorder (iswrd). an update for 20. Journal of clinical sleep medicine : JCSM : official publication of the American Academy of Sleep Medicine, 11 10:1199-236, Oct 2015. URL: https://doi.org/10.5664/jcsm.5100, doi:10.5664/jcsm.5100. This article has 627 citations.

4. (lane2023geneticsofcircadian pages 6-7): Jacqueline M. Lane, Jingyi Qian, Emmanuel Mignot, Susan Redline, Frank A. J. L. Scheer, and Richa Saxena. Genetics of circadian rhythms and sleep in human health and disease. Nature Reviews Genetics, 24:4-20, Aug 2023. URL: https://doi.org/10.1038/s41576-022-00519-z, doi:10.1038/s41576-022-00519-z. This article has 289 citations and is from a domain leading peer-reviewed journal.

5. (kurien2019timelessmutationalters pages 1-2): Philip Kurien, Pei-Ken Hsu, Jacy Leon, David Wu, Thomas McMahon, Guangsen Shi, Ying Xu, Anna Lipzen, Len A. Pennacchio, Christopher R. Jones, Ying-Hui Fu, and Louis J. Ptáček. Timeless mutation alters phase responsiveness and causes advanced sleep phase. Proceedings of the National Academy of Sciences, 116:12045-12053, May 2019. URL: https://doi.org/10.1073/pnas.1819110116, doi:10.1073/pnas.1819110116. This article has 96 citations and is from a highest quality peer-reviewed journal.

6. (OpenTargets Search: advanced sleep phase syndrome): Open Targets Query (advanced sleep phase syndrome, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (NCT00246454 chunk 1): Phyllis Zee. Circadian Rhythms and Sleep in Familial DSPS and ASPS. Northwestern University. 2003. ClinicalTrials.gov Identifier: NCT00246454

8. (NCT04690504 chunk 1): Jeanne Duffy. Validation of Circadian Biomarkers in Patients With Sleep Disorders. Brigham and Women's Hospital. 2021. ClinicalTrials.gov Identifier: NCT04690504

9. (toh2001anhper2 pages 1-2): Kong L. Toh, Christopher R. Jones, Yan He, Erik J. Eide, William A. Hinz, David M. Virshup, Louis J. Ptáček, and Ying-Hui Fu. An h <i>per2</i> phosphorylation site mutation in familial advanced sleep phase syndrome. Feb 2001. URL: https://doi.org/10.1126/science.1057499, doi:10.1126/science.1057499. This article has 1190 citations and is from a highest quality peer-reviewed journal.

10. (dodson2010therapeuticsforcircadian pages 4-5): Ehren R. Dodson and Phyllis C. Zee. Therapeutics for circadian rhythm sleep disorders. Sleep medicine clinics, 5 4:701-715, Dec 2010. URL: https://doi.org/10.1016/j.jsmc.2010.08.001, doi:10.1016/j.jsmc.2010.08.001. This article has 187 citations and is from a peer-reviewed journal.

11. (kurien2019timelessmutationalters pages 6-7): Philip Kurien, Pei-Ken Hsu, Jacy Leon, David Wu, Thomas McMahon, Guangsen Shi, Ying Xu, Anna Lipzen, Len A. Pennacchio, Christopher R. Jones, Ying-Hui Fu, and Louis J. Ptáček. Timeless mutation alters phase responsiveness and causes advanced sleep phase. Proceedings of the National Academy of Sciences, 116:12045-12053, May 2019. URL: https://doi.org/10.1073/pnas.1819110116, doi:10.1073/pnas.1819110116. This article has 96 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Advanced_Sleep_Phase_Syndrome-deep-research-falcon_artifacts/artifact-00.md)