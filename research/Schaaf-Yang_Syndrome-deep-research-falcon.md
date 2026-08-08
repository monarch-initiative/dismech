---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-29T22:32:35.963875'
end_time: '2026-07-29T22:40:22.553581'
duration_seconds: 466.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Schaaf-Yang Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Schaaf-Yang_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Schaaf-Yang Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Schaaf-Yang Syndrome** covering all of the
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
- **Disease Name:** Schaaf-Yang Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Schaaf-Yang Syndrome** covering all of the
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


# Schaaf–Yang Syndrome: Comprehensive Disease-Characteristics Report

**Scope and evidence note.** This report prioritizes peer-reviewed human evidence through 2024, especially Castilla‑Vallmanya et al. (published May 2023; DOI [10.1136/jmg-2022-108690](https://doi.org/10.1136/jmg-2022-108690)), supplemented by recent reviews and animal studies. Because Schaaf–Yang syndrome (SYS) is exceptionally rare, much of the evidence comes from aggregated case series, retrospective cohorts, patient-derived fibroblasts, and model organisms rather than controlled trials. PMID values were not available in the retrieved records; DOI links are therefore supplied rather than risking incorrect PMID assignment.

## Executive summary

SYS is a congenital, lifelong Mendelian neurodevelopmental disorder caused principally by a truncating variant affecting the **paternally expressed MAGEL2 allele** in the imprinted 15q11–q13 Prader–Willi region. Its characteristic combination is neonatal hypotonia and feeding/respiratory difficulty, developmental delay or intellectual disability, autism-related features, sleep and hypothalamic-endocrine abnormalities, and distal joint contractures or arthrogryposis. Although it overlaps Prader–Willi syndrome (PWS), severe intellectual disability, autism, and contractures are more characteristic of SYS, whereas classic PWS hyperphagia and obesity affect only a subset of people with SYS. More than 100 affected individuals had been reported by the 2023 synthesis, but population prevalence and incidence remain unknown. (castillavallmanya2023advancinginschaafyang pages 1-2, camerino2024thepivotalrole pages 3-5)

The leading mechanistic model is: **paternal MAGEL2 truncation → impaired endosomal recycling and regulated neuropeptide secretion, plus possible toxic/neomorphic activity of stable nuclear truncated MAGEL2 → disrupted hypothalamic, neuronal, neuromuscular, and endocrine development → multisystem phenotype**. No disease-modifying therapy is established; present care is multidisciplinary and symptom directed. Growth hormone replacement is used in selected deficient patients, while oxytocin remains experimental and is supported mainly by early-life animal studies. (castillavallmanya2023advancinginschaafyang pages 1-1, castillavallmanya2023advancinginschaafyang pages 7-8, schubert2025magel2(patho‐)physiologyand pages 10-11)

The following table provides a compact ontology-ready representation of the evidence.

| Domain | Evidence-backed finding | Suggested ontology/code | Evidence type/strength |
|---|---|---|---|
| Disease identifiers | Schaaf-Yang syndrome (SYS) is a rare Mendelian neurodevelopmental/imprinting disorder; OMIM 615547; Open Targets disease mapping supports MONDO_0014243; overlaps partly with Prader-Willi syndrome but is clinically distinct (OpenTargets Search: Schaaf-Yang syndrome-MAGEL2, castillavallmanya2023advancinginschaafyang pages 1-2) | MONDO: Schaaf-Yang syndrome; OMIM: 615547; category: Mendelian disease; candidate MeSH/Orphanet labels: Schaaf-Yang syndrome | Human peer-reviewed review/original synthesis + curated database association; moderate-strong |
| Synonyms / naming | Common names include Schaaf-Yang syndrome and SYS; older literature may describe a Prader-Willi-like syndrome with arthrogryposis due to MAGEL2 (castillavallmanya2023advancinginschaafyang pages 1-2) | candidate synonyms: SYS; MAGEL2-related Schaaf-Yang syndrome | Human literature synthesis; moderate |
| Causal gene / imprinting | Disease is caused primarily by truncating variants in MAGEL2 on 15q11-q13 affecting the paternally expressed allele; maternal allele is imprinted/silenced, so parental-origin confirmation is clinically important (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 1-1) | Gene: MAGEL2; chromosome region: 15q11-q13; inheritance concept: autosomal dominant with genomic imprinting / paternal expression | Human molecular genetics; strong |
| Variant class | Reported disease-causing variants are predominantly nonsense or frameshift truncating variants; truncated protein lacks the MAGE homology domain (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 1-1) | sequence_variant classes: nonsense_variant; frameshift_variant; truncating variant; loss-of-function with possible neomorphic effect | Human molecular genetics + in vitro functional evidence; strong |
| Pathogenic mechanism summary | MAGEL2 normally participates in retrograde transport and endosomal protein recycling; SYS likely reflects both loss of MAGEL2 function and pathogenic effects of a stable truncated protein (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 1-1, castillavallmanya2023advancinginschaafyang pages 6-6) | GO candidate terms: endosomal transport; retrograde transport, endosome to trans-Golgi network; protein recycling; regulated exocytosis / neuropeptide secretion | Human original research + mechanistic interpretation; moderate-strong |
| Truncated protein behavior | In cell studies, truncated MAGEL2 was stable and shifted from mainly cytoplasmic WT localization to predominantly nuclear localization, supporting a possible neomorphic/toxic mechanism beyond simple haploinsufficiency (castillavallmanya2023advancinginschaafyang pages 1-1, castillavallmanya2023advancinginschaafyang pages 6-6) | GO cellular component candidates: nucleus; cytoplasm; endosome; protein localization abnormality | In vitro functional study; moderate |
| Transcriptomic profile | Patient fibroblasts showed 132 differentially expressed genes, including ncRNAs; HOTAIR was highlighted as upregulated and proposed as a candidate biomarker (castillavallmanya2023advancinginschaafyang pages 1-1, castillavallmanya2023advancinginschaafyang pages 7-8) | biomarker candidates: HOTAIR mRNA; transcriptomic signature; ncRNA dysregulation | Human patient-derived in vitro omics; moderate |
| Metabolomic / biochemical profile | SYS fibroblasts had significantly decreased intracellular glutamine and decreased secretion of amyloid-β1-40 (Aβ1-40); both were proposed as candidate biomarkers, but remain unvalidated clinically (castillavallmanya2023advancinginschaafyang pages 1-1, castillavallmanya2023advancinginschaafyang pages 6-6) | CHEBI candidate: glutamine; biomarker candidates: Aβ1-40 secretion, glutamine level | Human patient-derived in vitro metabolomics; moderate |
| Core phenotype overview | Early-onset phenotype commonly includes neonatal hypotonia, developmental delay/intellectual disability, feeding difficulties, endocrine disturbance, sleep problems, autism spectrum features, and joint contractures/arthrogryposis (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 8-9) | HPO candidates: Neonatal hypotonia; Global developmental delay; Intellectual disability; Feeding difficulties; Autism; Arthrogryposis multiplex congenita / Camptodactyly; Sleep disturbance | Human cohort/literature synthesis; strong |
| Facial dysmorphism frequency | Facial dysmorphism reported in 91.4% (64/70) of cases in compiled cohort data (castillavallmanya2023advancinginschaafyang pages 3-4) | HPO candidate: Abnormal facial shape / Facial dysmorphism | Human compiled cohort frequency; moderate |
| Sleep disturbance frequency | Sleep disturbance reported in 100% (13/13) of cases with available data in compiled cohort review (castillavallmanya2023advancinginschaafyang pages 3-4) | HPO candidate: Sleep disturbance; sleep-disordered breathing candidate | Human compiled cohort frequency; moderate, small denominator |
| Growth hormone deficiency frequency | Growth hormone deficiency reported in 72.7% (16/22) of assessed individuals (castillavallmanya2023advancinginschaafyang pages 3-4) | HPO candidate: Growth hormone deficiency; endocrine abnormality | Human compiled cohort frequency; moderate, small denominator |
| Camptodactyly / contracture frequency | Camptodactyly reported in 50% of compiled cases; contractures/arthrogryposis are a distinguishing SYS feature relative to classic PWS (castillavallmanya2023advancinginschaafyang pages 3-4, castillavallmanya2023advancinginschaafyang pages 1-2) | HPO candidates: Camptodactyly; Arthrogryposis multiplex congenita; Joint contracture | Human cohort + review; moderate-strong |
| Hypogonadism frequency | Hypogonadism reported in 50% (40/80) of compiled cases (castillavallmanya2023advancinginschaafyang pages 3-4) | HPO candidate: Hypogonadism | Human compiled cohort frequency; moderate |
| Other endocrine frequencies | Hypothyroidism 29.6%; hypoglycemia 63.6%; temperature instability 62.9%; diabetes insipidus 29.4% in available compiled data (castillavallmanya2023advancinginschaafyang pages 3-4) | HPO candidates: Hypothyroidism; Hypoglycemia; Temperature instability; Diabetes insipidus | Human compiled cohort frequency; moderate |
| Hormonal/metabolic phenotype | Review evidence notes elevated fasting ghrelin, low IGF-1, increased glucose intolerance/diabetes mellitus prevalence, scoliosis ~33%, abnormal bone mineral density, and that only a minority develop hyperphagia/obesity compared with PWS (camerino2024thepivotalrole pages 3-5, castillavallmanya2023advancinginschaafyang pages 7-8) | HPO candidates: Elevated circulating ghrelin; Low IGF-1; Glucose intolerance; Diabetes mellitus; Scoliosis; Decreased bone mineral density; Hyperphagia; Obesity | Review synthesizing human studies; moderate |
| Neurobehavioral phenotype | Autism spectrum disorder and more severe intellectual disability are emphasized as relatively more common/severe in SYS than in PWS (castillavallmanya2023advancinginschaafyang pages 1-2, camerino2024thepivotalrole pages 3-5) | HPO candidates: Autism; Intellectual disability; Behavioral abnormality | Human review/cohort synthesis; moderate-strong |
| Anatomy: brain / hypothalamus | MAGEL2 is expressed predominantly in brain, especially amygdala and hypothalamic nuclei including suprachiasmatic, paraventricular, and supraoptic nuclei; hypothalamic dysfunction is central to pathophysiology (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 7-8) | UBERON candidates: brain; hypothalamus; amygdala; paraventricular nucleus of hypothalamus; supraoptic nucleus; suprachiasmatic nucleus | Human expression/review evidence; moderate |
| Anatomy: pituitary developmental relevance | Embryonic MAGEL2 transcripts were found in developing hypothalamus/ventral diencephalon and Rathke's pouch, supporting hypothalamo-pituitary developmental involvement and congenital hypopituitarism risk (castillavallmanya2023advancinginschaafyang pages 1-2) | UBERON candidates: Rathke pouch; pituitary gland; ventral diencephalon | Human embryonic expression study; moderate |
| Anatomy: muscle / musculoskeletal system | Hypotonia, high fat mass with low muscle tone, scoliosis, and joint contractures implicate skeletal muscle and musculoskeletal development/function (camerino2024thepivotalrole pages 3-5, schubert2025magel2(patho‐)physiologyand pages 10-11) | UBERON candidates: skeletal muscle tissue; musculoskeletal system; vertebral column; joint | Human review + animal references; moderate |
| Cell types implicated | Most plausible disease-relevant cell types are hypothalamic neuroendocrine neurons and broader central neurons; fibroblasts are currently the main patient-derived experimental cell system; muscle cells are implicated by hypotonia phenotype (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 1-1, schubert2025magel2(patho‐)physiologyand pages 10-11) | CL candidates: neuron; hypothalamic neuroendocrine cell; fibroblast; skeletal muscle cell | Mixed human expression/in vitro/phenotype inference; moderate |
| Upstream-to-downstream causal chain | Paternal MAGEL2 truncation → impaired endosomal recycling / secretory trafficking and altered nuclear localization of truncated protein → hypothalamic neuroendocrine dysfunction and delayed neuronal maturation/synaptic abnormalities → neonatal hypotonia, feeding/respiratory/endocrine abnormalities, developmental delay, autism traits, contractures (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 1-1, castillavallmanya2023advancinginschaafyang pages 7-8) | GO candidates: neuron development; synapse organization; peptide hormone secretion; endosomal transport; regulated exocytosis | Integrative mechanistic model from human and animal evidence; moderate |
| Synaptic / neuronal maturation evidence | Magel2-deficient mice show reduced neurite outgrowth, reduced glutamatergic synapse markers, and delayed neuronal maturation; oxytocin reversed neurite outgrowth abnormalities in culture (schubert2025magel2(patho‐)physiologyand pages 10-11) | GO candidates: neurite development; glutamatergic synaptic transmission; synapse maturation | Animal + in vitro preclinical evidence; moderate |
| Diagnostic approach | Best current diagnostic route is NGS-based sequencing (single gene, panel, exome, genome) detecting MAGEL2 truncating variants, followed by confirmation of paternal origin because maternal allele is imprinted; phenotype-first clues include neonatal hypotonia, feeding issues, contractures, developmental delay/autism, endocrine/sleep abnormalities (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 1-1) | Diagnostic concepts: sequence analysis of MAGEL2; trio exome/genome; parental-origin confirmation; genomic imprinting assessment | Human clinical genetics guidance; strong |
| Differential diagnosis | Major differential diagnoses include Prader-Willi syndrome, congenital hypopituitarism syndromes, and historically Opitz-C syndrome / PWS-like disorders with arthrogryposis (castillavallmanya2023advancinginschaafyang pages 8-9, castillavallmanya2023advancinginschaafyang pages 1-2) | candidate disease terms: Prader-Willi syndrome; congenital hypopituitarism; Opitz-C syndrome | Human literature synthesis; moderate |
| Real-world management | Management is multidisciplinary and symptomatic: neonatal feeding/airway/respiratory support, developmental therapies, autism-informed behavioral care, endocrine evaluation, orthopedic surveillance, and sleep monitoring; recent literature offers practical management guidelines by life stage (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 3-4) | MAXO candidates: respiratory support; feeding support; physical therapy; occupational therapy; speech therapy; endocrine system monitoring; orthopedic monitoring; sleep study | Human peer-reviewed management synthesis; moderate-strong |
| Growth hormone treatment | Growth hormone deficiency is common and patients may benefit from GH therapy; recent literature references retrospective and multi-year follow-up studies, but robust controlled efficacy/safety data remain limited (castillavallmanya2023advancinginschaafyang pages 3-4, castillavallmanya2023advancinginschaafyang pages 7-8, schubert2025magel2(patho‐)physiologyand pages 14-14) | MAXO candidates: growth hormone replacement therapy; endocrine follow-up | Human cohort/review evidence; moderate but incomplete |
| Sleep / respiratory management | Sleep disturbance is common and sleep-disordered breathing/polysomnography have been specifically studied in referenced literature; respiratory and sleep surveillance are therefore reasonable parts of care (castillavallmanya2023advancinginschaafyang pages 3-4, schubert2025magel2(patho‐)physiologyand pages 10-11) | MAXO candidates: polysomnography; sleep-disordered breathing monitoring; respiratory management | Human literature synthesis; moderate |
| Prognosis / mortality | Disease is lifelong; available compiled literature notes 10-13 documented deaths in infancy/childhood, but precise survival estimates and causes-of-death distributions are not yet well established (castillavallmanya2023advancinginschaafyang pages 3-4, castillavallmanya2023advancinginschaafyang pages 8-9) | outcome concepts: childhood mortality; chronic neurodevelopmental disability | Human compiled literature; weak-moderate due to sparse data |
| Prevention / counseling | No primary prevention exists for de novo disease occurrence; for affected families, genetic counseling should address imprinting, recurrence risk, and reproductive options such as prenatal diagnosis or preimplantation genetic testing when a familial pathogenic variant is known (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 1-1) | MAXO candidates: genetic counseling; prenatal molecular diagnosis; preimplantation genetic testing | Standard clinical genetics inference anchored to imprinting mechanism; moderate |
| Animal models | Disease-relevant models include Magel2-deficient mice and Magel2 truncation rat models; they recapitulate selected behavioral, neurodevelopmental, thermoregulatory, and muscle-related phenotypes and are used for mechanistic and therapeutic studies (schubert2025magel2(patho‐)physiologyand pages 10-11, schubert2025magel2(patho‐)physiologyand pages 14-14) | model organism terms: mouse model; rat model; Magel2-deficient; truncation knock-in candidate | Animal/preclinical evidence; moderate |
| Experimental therapeutics | Oxytocin is the best-supported experimental therapeutic concept from preclinical work: early postnatal treatment improved some social/developmental phenotypes in Magel2-deficient models, but optimal window, CNS delivery, and human efficacy remain uncertain (schubert2025magel2(patho‐)physiologyand pages 10-11, schubert2025magel2(patho‐)physiologyand pages 14-14) | CHEBI candidate: oxytocin; MAXO candidate: oxytocin therapy | Animal/preclinical evidence; moderate, not established clinically |
| Clinical trials status | A search retrieved no clearly relevant SYS-specific interventional clinical trials in the available tool output, underscoring a sparse formal trial landscape (OpenTargets Search: Schaaf-Yang syndrome-MAGEL2) | research status concept: no SYS-specific trial captured | Trial registry search snapshot; weak-moderate |
| Explicit knowledge gaps | Major gaps include true prevalence/incidence, validated biomarkers, genotype-phenotype correlations by variant, long-term natural history, adult outcomes, standardized QoL metrics, controlled GH and oxytocin studies, and consensus diagnostic/management guidelines across centers (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 1-1, schubert2025magel2(patho‐)physiologyand pages 10-11) | research gap annotations: epidemiology unknown; biomarker validation needed; natural history study needed | Cross-source synthesis; strong as a gap statement |


*Table: This table summarizes ontology-ready, evidence-backed facts for Schaaf-Yang syndrome across identifiers, mechanisms, phenotypes, diagnostics, management, and models. It is designed as a compact knowledge-base input with explicit evidence strength and clearly marked gaps.*

## 1. Disease information

**Definition and category.** SYS is an imprinting-dependent, autosomal Mendelian neurodevelopmental syndrome associated with pathogenic variation in **MAGEL2**, one of the protein-coding genes in the PWS locus. It is not simply a PWS subtype: the disorders overlap mechanistically and phenotypically but have distinguishable clinical distributions. (castillavallmanya2023advancinginschaafyang pages 1-2)

**Identifiers and names.** Verified identifiers are **OMIM 615547** and **MONDO:0014243**. Open Targets maps MONDO:0014243 to MAGEL2/ENSG00000254585. MAGEL2 itself is OMIM 605283. Common names are *Schaaf–Yang syndrome*, *SYS*, and *MAGEL2-related Schaaf–Yang syndrome*; older descriptions may use “Prader–Willi-like syndrome due to MAGEL2 mutation.” A dedicated ICD-10, ICD-11, or MeSH code was not established in the retrieved evidence; coding generally requires broader congenital-malformation, neurodevelopmental, or genetic-syndrome categories. (OpenTargets Search: Schaaf-Yang syndrome-MAGEL2, castillavallmanya2023advancinginschaafyang pages 1-2)

The evidence is predominantly **aggregated disease-level literature**—case series, compiled cohorts, reviews, and experimental studies—not an individual-patient EHR dataset. Individual case observations contribute to these aggregates. (castillavallmanya2023advancinginschaafyang pages 8-9)

## 2. Etiology, risk, and protective factors

The primary cause is a **germline pathogenic variant on the paternal, transcriptionally active MAGEL2 allele**. MAGEL2 is maternally imprinted; therefore, an identical variant on the normally silent maternal allele may not cause the classic phenotype. Most well-established SYS variants are nonsense or frameshift changes producing a truncated protein, often lacking the C-terminal MAGE homology domain. (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 1-1)

This is not an environmentally acquired, infectious, toxic, or lifestyle-mediated disease. The principal “risk factor” is inheritance or de-novo occurrence of a pathogenic variant on the paternal allele. No validated susceptibility loci, protective alleles, environmental protective factors, or gene–environment interactions are known. Environmental and medical circumstances can nevertheless modify complications—for example, aspiration, undernutrition, untreated sleep-disordered breathing, or endocrine deficiency—but do not cause SYS.

## 3. Phenotypes

Phenotypes begin predominantly **prenatally or neonatally**, are highly variable, and generally persist lifelong. Core suggested HPO annotations include neonatal hypotonia, feeding difficulty, global developmental delay, intellectual disability, autism, joint contracture, camptodactyly, arthrogryposis, sleep disturbance, short stature, hypogonadism, and temperature instability. (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 3-4)

Reported frequencies from compiled literature must be interpreted using their feature-specific denominators:

- Facial dysmorphism: **91.4% (64/70)**.
- Sleep disturbance: **100% (13/13)**; the denominator is small and likely clinically selected.
- Growth-hormone deficiency: **72.7% (16/22)**.
- Camptodactyly: approximately **50%**.
- Hypogonadism: **50% (40/80)**.
- Hypoglycemia: **63.6%**; temperature instability: **62.9%**.
- Hypothyroidism: **29.6%**; diabetes insipidus: **29.4%**.
- Scoliosis: approximately **33%** in a recent review synthesis. (camerino2024thepivotalrole pages 3-5, castillavallmanya2023advancinginschaafyang pages 3-4)

Neonatal hypotonia, weak suck/feeding difficulty, respiratory compromise, and contractures can be severe. Developmental delay and intellectual disability range from moderate to profound; expressive communication and adaptive independence are often substantially affected. Autism spectrum features and behavioral dysregulation are prominent. Sleep abnormalities, including sleep-disordered breathing, further affect daytime behavior and caregiver burden. (castillavallmanya2023advancinginschaafyang pages 1-2, schubert2025magel2(patho‐)physiologyand pages 10-11)

Endocrine/metabolic findings include short stature, low IGF‑1 or growth-hormone deficiency, hypogonadism, elevated fasting ghrelin, abnormal body composition, glucose intolerance/diabetes, and altered bone mineral density. Unlike classic PWS, only a minority develop marked hyperphagia and obesity, although high fat mass can occur despite a lower BMI. (camerino2024thepivotalrole pages 3-5, castillavallmanya2023advancinginschaafyang pages 7-8)

No robust SYS-specific EQ‑5D, SF‑36, or population-level utility estimates were recovered. Quality-of-life effects are inferred from chronic feeding and sleep problems, communication and intellectual disability, restricted mobility from contractures, behavioral symptoms, and intensive caregiver requirements; caregiver burden has been studied, but quantitative scores were unavailable in the retrieved full text. (schubert2025magel2(patho‐)physiologyand pages 10-11)

## 4. Genetic and molecular information

**Gene:** MAGEL2, encoding MAGE family member L2; Open Targets identifier ENSG00000254585. MAGEL2 is a single-exon gene encoding a 1,249-amino-acid protein with an N-terminal proline-rich region and C-terminal MAGE homology domain at approximately residues 1027–1195. (OpenTargets Search: Schaaf-Yang syndrome-MAGEL2, castillavallmanya2023advancinginschaafyang pages 1-2)

**Variant interpretation.** Established SYS variants are predominantly heterozygous germline nonsense or frameshift variants on the paternal allele. Their population frequency should generally be absent or extremely low in reference databases, but exact gnomAD frequencies must be checked variant by variant. Classification should follow ACMG/AMP criteria while explicitly incorporating phenotype, predicted truncation, functional evidence, segregation, and—critically—parental origin. A VUS or missense variant should not automatically be called SYS without compelling evidence. (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 1-1)

The disease mechanism is more complex than ordinary haploinsufficiency. Patient-derived experiments showed that truncated MAGEL2 is synthesized and stable and shifts from predominantly cytoplasmic wild-type localization to predominantly nuclear localization. This supports combined loss of normal endosomal/secretory function and a possible **neomorphic or toxic truncated-protein effect**. Mild phenotypes reported with complete regional deletions further support the possibility that absence and truncation are not biologically equivalent. (castillavallmanya2023advancinginschaafyang pages 1-1, castillavallmanya2023advancinginschaafyang pages 6-6)

No validated modifier genes, protective variants, founder variant, anticipation mechanism, or recurrent population-specific allele has been established. Larger 15q abnormalities involving MAGEL2, NDN, MKRN3, or the full PWS region can produce overlapping but non-identical disorders and should not automatically be labeled sequence-variant SYS. (castillavallmanya2023advancinginschaafyang pages 6-6)

## 5. Environmental information

No toxin, radiation exposure, pollution source, occupation, diet, smoking behavior, alcohol exposure, or infectious agent is known to initiate SYS. There is no zoonotic or transmissible component. Nutrition, airway care, infection prevention, physical activity, and sleep management are clinically important modifiers of morbidity rather than etiologic factors.

## 6. Mechanism and pathophysiology

MAGEL2 normally contributes to **endosomal protein trafficking, retrograde transport, recycling, and neurosecretory function**. Loss of normal function can impair the recycling or secretion machinery required by hypothalamic neurons. The downstream result is dysregulated secretion of neuropeptides and pituitary-regulating hormones governing feeding, growth, reproduction, sleep, temperature, stress responses, and social behavior. (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 7-8)

Patient-fibroblast evidence provides a second mechanism. In seven SYS fibroblast lines versus 11 controls, investigators found decreased secreted amyloid‑β1–40, decreased intracellular glutamine, and **132 differentially expressed genes**, including increased HOTAIR. Truncated MAGEL2 remained stable and accumulated disproportionately in the nucleus. These findings make Aβ1–40 secretion and HOTAIR mRNA candidate biomarkers, but neither is a validated clinical diagnostic test. (castillavallmanya2023advancinginschaafyang pages 1-1)

The authors’ exact abstract conclusion was: **“A truncated MAGEL2 protein is stable and localises mainly in the nucleus, where it might exert a pathogenic neomorphic effect.”** They further stated that **“Aβ1-40 secretion levels and HOTAIR mRNA levels might be promising biomarkers for SYS.”** These are hypotheses supported by patient-derived in-vitro data, not yet prospective clinical biomarkers. (castillavallmanya2023advancinginschaafyang pages 1-1)

Animal evidence adds impaired neurite growth, delayed neuronal maturation, and reduced glutamatergic synapse markers. In Magel2-deficient mouse neurons, oxytocin reversed reduced neurite outgrowth, although it did not normalize every glutamatergic synaptic endpoint. Suggested GO annotations include endosomal transport, retrograde endosome-to-trans-Golgi transport, protein recycling, regulated exocytosis, peptide-hormone secretion, neuron development, neurite morphogenesis, synapse organization, and glutamatergic transmission. (schubert2025magel2(patho‐)physiologyand pages 10-11)

There is no established autoimmune, inflammatory, fibrotic, ischemic, or primary mitochondrial mechanism. No reproducible SYS-specific proteomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omics signature has yet reached clinical validity.

## 7. Anatomical structures affected

The **central nervous system—particularly hypothalamic circuitry—is primary**. MAGEL2 expression is enriched in the brain, including the amygdala and hypothalamic suprachiasmatic, paraventricular, and supraoptic nuclei. Suggested UBERON concepts are brain, hypothalamus, amygdala, suprachiasmatic nucleus, paraventricular nucleus, supraoptic nucleus, pituitary gland, skeletal muscle, joint, and vertebral column. (castillavallmanya2023advancinginschaafyang pages 1-2)

Developmental expression in the hypothalamus, ventral diencephalon, and Rathke pouch supports hypothalamo-pituitary involvement. Secondary systems include skeletal muscle and peripheral joints, respiratory/upper-airway structures, gastrointestinal tract, endocrine organs, skeleton, and reproductive system. Candidate CL annotations are neuron, hypothalamic neuroendocrine cell, pituitary endocrine cell, skeletal muscle cell, and fibroblast—the last being an experimental rather than primary disease-target cell. (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 1-1)

Relevant subcellular compartments are endosomes, recycling endosomes, cytoplasm, nucleus, and secretory vesicles. No consistent lateralization is recognized.

## 8. Temporal development

Onset is congenital, often with prenatal reduced movement or contractures and neonatal hypotonia, weak feeding, and respiratory problems. The course is chronic and lifelong rather than relapsing-remitting. Developmental gains occur, but intellectual, communication, orthopedic, sleep, and endocrine needs commonly persist. (castillavallmanya2023advancinginschaafyang pages 1-2)

There is no validated staging system. Practical stages are neonatal stabilization; infancy/early-childhood feeding, motor, and communication intervention; school-age neurobehavioral, orthopedic, sleep, and endocrine surveillance; and adult support for chronic disability and metabolic complications. Early neural development may be a therapeutic critical period: model data suggest that oxytocin effects depend on timing, while CNS delivery becomes more difficult after blood–brain-barrier maturation. This remains a preclinical expert interpretation, not a human treatment window. (schubert2025magel2(patho‐)physiologyand pages 10-11, schubert2025magel2(patho‐)physiologyand pages 14-14)

## 9. Inheritance and population

Inheritance is best described as **autosomal dominant with parent-of-origin-dependent expression**. A pathogenic variant causes SYS when present on the active paternal allele. Many cases are de novo; familial transmission is possible, including clinically unaffected maternal carriers whose variant can become disease-causing when transmitted through a male in a later generation. Parental testing and phasing are consequently essential.

Penetrance for established paternal truncating variants appears high, but expressivity is markedly variable. Formal penetrance estimates, carrier frequency, germline-mosaicism rate, founder effects, consanguinity effects, ethnic enrichment, geographic variation, sex ratio, prevalence, and annual incidence are unknown. More than 100 patients had been reported by 2023, which is a literature count rather than an epidemiologic prevalence estimate. (castillavallmanya2023advancinginschaafyang pages 1-2)

## 10. Diagnostics

Diagnosis requires molecular confirmation; no biochemical, imaging, histologic, or electrophysiologic test is independently diagnostic.

1. **Clinical suspicion:** neonatal hypotonia/feeding or respiratory difficulty plus distal contractures or arthrogryposis, developmental delay/intellectual disability, autism features, short stature/endocrine abnormalities, and sleep disturbance.
2. **Sequence testing:** trio exome/genome, a neurodevelopmental/arthrogryposis/imprinting-disorder panel containing MAGEL2, or targeted MAGEL2 sequencing.
3. **Parental-origin confirmation:** parental sequencing and phasing should determine whether the variant is on the paternal allele.
4. **Structural/imprinting assessment:** chromosomal microarray may identify 15q copy-number changes but will miss most small truncating variants. PWS methylation testing is useful when PWS is suspected, but a normal PWS methylation result does not exclude sequence-level SYS. Karyotyping and FISH have low yield unless a large rearrangement is suspected.
5. **Baseline phenotyping:** feeding/swallow evaluation; polysomnography when indicated; endocrine tests including glucose, thyroid, IGF‑1/GH-axis and gonadal assessment; orthopedic examination; hearing/vision assessment; and developmental/autism evaluation. (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 3-4)

Main differentials include PWS, congenital myopathies, congenital hypopituitarism, L1CAM-related disease when hydrocephalus/spasticity is present, other arthrogryposis syndromes, and historically Opitz-C/PWS-like disorders. PWS is distinguished molecularly by loss of expression across the paternal PWS region and clinically by more typical later hyperphagia/obesity, small hands/feet, and characteristic facies; SYS more strongly features contractures and autism/severe ID. (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 8-9)

RNA-seq, metabolomics, Aβ1–40, HOTAIR, and glutamine remain research tools. Newborn or population carrier screening is not standard.

## 11. Outcome and prognosis

Reliable five- or ten-year survival rates, median life expectancy, and disease-specific mortality rates do not exist. A 2023 compiled analysis identified approximately **10–13 reported deaths in infancy or childhood**, but publication bias and incomplete follow-up prevent estimation of risk. Severe neonatal respiratory disease, aspiration/feeding complications, gastrointestinal dysmotility or malrotation, sleep-disordered breathing, endocrine crises, and extreme obesity in occasional patients are plausible contributors. (castillavallmanya2023advancinginschaafyang pages 8-9, castillavallmanya2023advancinginschaafyang pages 3-4)

Long-term morbidity includes intellectual and adaptive disability, limited communication, autism-related behavior, mobility restriction from contractures/scoliosis, sleep problems, endocrine deficiency, altered body composition, and caregiver burden. Full recovery is not expected because the genetic neurodevelopmental disorder is lifelong, although feeding, motor function, communication, sleep, growth, and participation may improve with intervention. No validated prognostic biomarker or risk calculator exists.

## 12. Treatment and current applications

There is **no approved disease-modifying or genotype-corrective treatment**. Real-world management is individualized and multidisciplinary:

- Neonatal respiratory support, aspiration prevention, swallowing assessment, and enteral feeding when necessary.
- Physical therapy, stretching/splinting, occupational therapy, speech-language and augmentative communication interventions, and developmental/behavioral services.
- Polysomnography and treatment of obstructive or central sleep-disordered breathing.
- Endocrinology follow-up for growth, thyroid, glucose, adrenal/pituitary, puberty, gonadal function, and bone health.
- Orthopedic surveillance for contractures, hip or foot abnormalities, and scoliosis; surgery is phenotype-specific rather than syndrome-specific.
- Nutritional monitoring without assuming the classic PWS hyperphagia trajectory. (castillavallmanya2023advancinginschaafyang pages 1-2, castillavallmanya2023advancinginschaafyang pages 3-4)

Suggested MAXO terms include genetic counseling, feeding assistance, gastrostomy, respiratory support, polysomnography, physical therapy, occupational therapy, speech therapy, augmentative and alternative communication, growth-hormone replacement, endocrine monitoring, orthopedic surveillance, and scoliosis surgery.

**Growth hormone.** Growth-hormone deficiency is frequent, and retrospective/multiyear reports suggest improved linear growth and possible body-composition benefits in selected patients. However, SYS-specific controlled response rates and comprehensive long-term safety estimates are unavailable. Treatment should follow endocrine confirmation and include glucose, IGF‑1, scoliosis, and sleep/airway surveillance. (castillavallmanya2023advancinginschaafyang pages 3-4, castillavallmanya2023advancinginschaafyang pages 7-8, schubert2025magel2(patho‐)physiologyand pages 14-14)

**Experimental therapy.** Oxytocin can improve social or developmental phenotypes and neurite growth in Magel2-deficient models. Yet no human SYS efficacy has been established; developmental timing, dose, route, CNS penetration, and durability remain unresolved. No gene therapy, ASO, RNA therapy, CRISPR treatment, cell therapy, or immunotherapy is clinically available. The registry search retrieved no clearly relevant SYS-specific interventional trial, so no supported NCT identifier can be reported. (schubert2025magel2(patho‐)physiologyand pages 10-11, schubert2025magel2(patho‐)physiologyand pages 14-14)

## 13. Prevention

There is no lifestyle, vaccine, drug, or environmental intervention that prevents a de-novo MAGEL2 variant. Secondary prevention consists of early molecular diagnosis and prompt feeding, respiratory, developmental, sleep, endocrine, and orthopedic intervention. Tertiary prevention targets aspiration, malnutrition, sleep-related hypoxemia, avoidable contracture, scoliosis progression, diabetes, low bone density, and communication-related behavioral distress.

Genetic counseling should explain parent-of-origin effects, test both parents, consider parental mosaicism where appropriate, and discuss prenatal diagnosis or preimplantation genetic testing when the familial pathogenic variant and informative phase are known. Population newborn screening is not currently justified by an established screening assay or disease-modifying neonatal treatment.

## 14. Other species and natural disease

No validated naturally occurring veterinary counterpart of human SYS was identified. MAGEL2/Magel2 is evolutionarily conserved among mammals, but there is no evidence of breed-specific disease, zoonotic transmission, or cross-species infection. Mouse and rat phenotypes are engineered research models rather than naturally transmissible disease.

## 15. Model organisms

**Mouse models** with paternal Magel2 deficiency reproduce selected neonatal, social, thermoregulatory, neuronal, synaptic, and muscle abnormalities. Primary hippocampal neurons show reduced neurite outgrowth, while developing hippocampus shows delayed maturation and altered glutamatergic synapse markers. Early oxytocin can rescue some—but not all—outcomes. (schubert2025magel2(patho‐)physiologyand pages 10-11)

**Rat truncation models** more closely represent a truncated-protein genotype and show selected behavioral and physiological abnormalities. Their principal value is testing whether truncation differs from complete gene loss and enabling pharmacologic and longitudinal behavioral studies. (schubert2025magel2(patho‐)physiologyand pages 10-11)

Model limitations are substantial: species-specific imprinting and neurodevelopment, variable allele design, incomplete reproduction of severe human intellectual disability and contractures, and uncertain translation of neonatal oxytocin dosing. Patient-derived fibroblasts provide direct human molecular evidence but do not reproduce hypothalamic neuronal physiology. Patient iPSC-derived hypothalamic neurons or organoids, allele-specific models, and single-cell/spatial studies are important unmet research needs.

## Current research priorities and expert assessment

The strongest 2023 advance was recognition that SYS may combine **loss of normal MAGEL2 function with active pathology from a stable truncated protein**, rather than representing simple MAGEL2 haploinsufficiency. The most important translational priorities are prospective natural-history registries, standardized phenotype and quality-of-life measures, variant- and parent-of-origin-resolved genotype–phenotype studies, validation of Aβ1–40/HOTAIR biomarkers, controlled growth-hormone studies, and carefully designed early-development neuropeptide trials. (castillavallmanya2023advancinginschaafyang pages 1-1, castillavallmanya2023advancinginschaafyang pages 6-6, schubert2025magel2(patho‐)physiologyand pages 14-14)

The evidence base remains constrained by small and overlapping cohorts. Feature percentages should therefore be stored with numerator/denominator and ascertainment metadata, not treated as definitive population frequencies. Likewise, candidate biomarkers and oxytocin should remain annotated as **research findings**, whereas molecular diagnosis, multidisciplinary surveillance, rehabilitation, respiratory/feeding support, and treatment of documented endocrine deficiencies represent current clinical practice.

References

1. (castillavallmanya2023advancinginschaafyang pages 1-2): Laura Castilla-Vallmanya, Mónica Centeno-Pla, Mercedes Serrano, Héctor Franco-Valls, Raúl Martínez-Cabrera, Aina Prat-Planas, Elena Rojano, Juan A. G. Ranea, Pedro Seoane, Clara Oliva, Abraham J. Paredes-Fuentes, Rafael Artuch, Daniel Grinberg, Raquel Rabionet, Susanna Balcells, and Roser Urreizti. Advancing in schaaf-yang syndrome pathophysiology: from bedside to subcellular analyses of truncated magel2. Journal of Medical Genetics, 60:406-415, May 2023. URL: https://doi.org/10.1136/jmg-2022-108690, doi:10.1136/jmg-2022-108690. This article has 15 citations and is from a domain leading peer-reviewed journal.

2. (camerino2024thepivotalrole pages 3-5): Claudia Camerino. The pivotal role of oxytocin’s mechanism of thermoregulation in prader-willi syndrome, schaaf-yang syndrome, and autism spectrum disorder. International Journal of Molecular Sciences, 25:2066, Feb 2024. URL: https://doi.org/10.3390/ijms25042066, doi:10.3390/ijms25042066. This article has 8 citations.

3. (castillavallmanya2023advancinginschaafyang pages 1-1): Laura Castilla-Vallmanya, Mónica Centeno-Pla, Mercedes Serrano, Héctor Franco-Valls, Raúl Martínez-Cabrera, Aina Prat-Planas, Elena Rojano, Juan A. G. Ranea, Pedro Seoane, Clara Oliva, Abraham J. Paredes-Fuentes, Rafael Artuch, Daniel Grinberg, Raquel Rabionet, Susanna Balcells, and Roser Urreizti. Advancing in schaaf-yang syndrome pathophysiology: from bedside to subcellular analyses of truncated magel2. Journal of Medical Genetics, 60:406-415, May 2023. URL: https://doi.org/10.1136/jmg-2022-108690, doi:10.1136/jmg-2022-108690. This article has 15 citations and is from a domain leading peer-reviewed journal.

4. (castillavallmanya2023advancinginschaafyang pages 7-8): Laura Castilla-Vallmanya, Mónica Centeno-Pla, Mercedes Serrano, Héctor Franco-Valls, Raúl Martínez-Cabrera, Aina Prat-Planas, Elena Rojano, Juan A. G. Ranea, Pedro Seoane, Clara Oliva, Abraham J. Paredes-Fuentes, Rafael Artuch, Daniel Grinberg, Raquel Rabionet, Susanna Balcells, and Roser Urreizti. Advancing in schaaf-yang syndrome pathophysiology: from bedside to subcellular analyses of truncated magel2. Journal of Medical Genetics, 60:406-415, May 2023. URL: https://doi.org/10.1136/jmg-2022-108690, doi:10.1136/jmg-2022-108690. This article has 15 citations and is from a domain leading peer-reviewed journal.

5. (schubert2025magel2(patho‐)physiologyand pages 10-11): Tim Schubert and Christian P. Schaaf. Magel2 (patho‐)physiology and schaaf–yang syndrome. Developmental Medicine and Child Neurology, 67:35-48, Jul 2025. URL: https://doi.org/10.1111/dmcn.16018, doi:10.1111/dmcn.16018. This article has 28 citations and is from a highest quality peer-reviewed journal.

6. (OpenTargets Search: Schaaf-Yang syndrome-MAGEL2): Open Targets Query (Schaaf-Yang syndrome-MAGEL2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (castillavallmanya2023advancinginschaafyang pages 6-6): Laura Castilla-Vallmanya, Mónica Centeno-Pla, Mercedes Serrano, Héctor Franco-Valls, Raúl Martínez-Cabrera, Aina Prat-Planas, Elena Rojano, Juan A. G. Ranea, Pedro Seoane, Clara Oliva, Abraham J. Paredes-Fuentes, Rafael Artuch, Daniel Grinberg, Raquel Rabionet, Susanna Balcells, and Roser Urreizti. Advancing in schaaf-yang syndrome pathophysiology: from bedside to subcellular analyses of truncated magel2. Journal of Medical Genetics, 60:406-415, May 2023. URL: https://doi.org/10.1136/jmg-2022-108690, doi:10.1136/jmg-2022-108690. This article has 15 citations and is from a domain leading peer-reviewed journal.

8. (castillavallmanya2023advancinginschaafyang pages 8-9): Laura Castilla-Vallmanya, Mónica Centeno-Pla, Mercedes Serrano, Héctor Franco-Valls, Raúl Martínez-Cabrera, Aina Prat-Planas, Elena Rojano, Juan A. G. Ranea, Pedro Seoane, Clara Oliva, Abraham J. Paredes-Fuentes, Rafael Artuch, Daniel Grinberg, Raquel Rabionet, Susanna Balcells, and Roser Urreizti. Advancing in schaaf-yang syndrome pathophysiology: from bedside to subcellular analyses of truncated magel2. Journal of Medical Genetics, 60:406-415, May 2023. URL: https://doi.org/10.1136/jmg-2022-108690, doi:10.1136/jmg-2022-108690. This article has 15 citations and is from a domain leading peer-reviewed journal.

9. (castillavallmanya2023advancinginschaafyang pages 3-4): Laura Castilla-Vallmanya, Mónica Centeno-Pla, Mercedes Serrano, Héctor Franco-Valls, Raúl Martínez-Cabrera, Aina Prat-Planas, Elena Rojano, Juan A. G. Ranea, Pedro Seoane, Clara Oliva, Abraham J. Paredes-Fuentes, Rafael Artuch, Daniel Grinberg, Raquel Rabionet, Susanna Balcells, and Roser Urreizti. Advancing in schaaf-yang syndrome pathophysiology: from bedside to subcellular analyses of truncated magel2. Journal of Medical Genetics, 60:406-415, May 2023. URL: https://doi.org/10.1136/jmg-2022-108690, doi:10.1136/jmg-2022-108690. This article has 15 citations and is from a domain leading peer-reviewed journal.

10. (schubert2025magel2(patho‐)physiologyand pages 14-14): Tim Schubert and Christian P. Schaaf. Magel2 (patho‐)physiology and schaaf–yang syndrome. Developmental Medicine and Child Neurology, 67:35-48, Jul 2025. URL: https://doi.org/10.1111/dmcn.16018, doi:10.1111/dmcn.16018. This article has 28 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Schaaf-Yang_Syndrome-deep-research-falcon_artifacts/artifact-00.md)