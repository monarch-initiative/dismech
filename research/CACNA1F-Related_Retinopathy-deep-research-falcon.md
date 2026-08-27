---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-13T20:32:00.453045'
end_time: '2026-07-13T20:55:17.784558'
duration_seconds: 1397.33
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: CACNA1F-Related Retinopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 72
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CACNA1F-Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CACNA1F-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CACNA1F-Related Retinopathy** covering all of the
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
- **Disease Name:** CACNA1F-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CACNA1F-Related Retinopathy** covering all of the
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


# CACNA1F-Related Retinopathy — Comprehensive Disease Characteristics Report (Mendelian)

## Target Disease
- **Disease name:** CACNA1F-Related Retinopathy
- **Category:** Mendelian (X-linked)
- **MONDO ID:** Not identified in retrieved full-text evidence (see “Key identifiers” below).

---

## 1. Disease Information

### Overview (what is the disease?)
CACNA1F-related retinopathy is an X-linked inherited retinal disorder caused by pathogenic variants in **CACNA1F**, encoding the **Cav1.4 L-type voltage-gated calcium channel** α1F subunit expressed at the **photoreceptor ribbon synapse**. Clinically, CACNA1F variants produce a spectrum spanning **non-progressive synaptic transmission disorders** (classically incomplete congenital stationary night blindness) through to **progressive cone–rod dystrophy phenotypes**, with substantial phenotypic overlap and heterogeneity. (marziali2023opticnerveinvolvement pages 1-6, wygledowskapromienska2024alandislandeye pages 1-2, mahmood2021anovelsplicesite pages 5-8)

### Key disease entities and OMIM identifiers (available in retrieved sources)
The CACNA1F phenotypic spectrum is explicitly summarized in recent clinical genetics/ophthalmology papers:
- **CACNA1F gene:** MIM **300110** (wygledowskapromienska2024alandislandeye pages 1-2, marziali2023opticnerveinvolvement pages 1-6, mahmood2021anovelsplicesite pages 1-2)
- **X-linked congenital stationary night blindness type 2A (CSNB2A / iCSNB):** OMIM **300071** (wygledowskapromienska2024alandislandeye pages 1-2, schaare2023concomitantcalciumchannelopathies pages 1-2)
- **Åland Island eye disease (AIED):** OMIM **300600** (wygledowskapromienska2024alandislandeye pages 1-2, schaare2023concomitantcalciumchannelopathies pages 1-2)
- **X-linked cone–rod dystrophy type 3 (CORDX3):** OMIM **300476** (wygledowskapromienska2024alandislandeye pages 1-2)

### Synonyms and alternative names
- **CSNB2A:** “incomplete CSNB,” “Miyake incomplete CSNB,” “iCSNB” (marziali2023opticnerveinvolvement pages 1-6)
- **AIED:** also referred to as “Forsius-Eriksson syndrome” in the CACNA1F spectrum literature (marziali2023opticnerveinvolvement pages 14-20)
- Cross-spectrum wording: “CACNA1F-associated retinopathy/oculopathy” has been proposed to reflect allelic overlap between entities (mahmood2021anovelsplicesite pages 5-8)

### Other identifiers (Orphanet, ICD-10/ICD-11, MeSH, MONDO)
These identifiers were **not present** in the retrieved full-text evidence set and are therefore **not reported here** to avoid hallucination.

### Evidence source type
The information in this report is derived from:
- **Aggregated disease-level resources in peer-reviewed reviews/case series**, plus
- **Primary human cohorts/case series** and **animal model studies** (mouse; plus mentions of rat/zebrafish models) (marziali2023opticnerveinvolvement pages 6-10, leahy2021opticatrophyand pages 3-6, laird2023mouseallconeretina pages 1-2, maddox2024anonconductingrole pages 1-2).

---

## 2. Etiology

### Disease causal factors
- **Primary cause:** Germline pathogenic variants in **CACNA1F** (X chromosome, Xp11.23) encoding the pore-forming α1F subunit of Cav1.4 L-type voltage-gated calcium channels at the first retinal synapse (photoreceptor → bipolar/horizontal cells). (marziali2023opticnerveinvolvement pages 1-6, ganglberger2025exploringthepotential pages 1-2)

### Risk factors
- **Genetic:** Hemizygous pathogenic CACNA1F variants in males are the main causal risk factor (X-linked inheritance). (mahmood2021anovelsplicesite pages 1-2, marziali2023opticnerveinvolvement pages 1-6)
- **Sex:** Marked male predominance is reported in literature reviews; one review cohort reported **87% male** among CACNA1F cases. (schaare2023concomitantcalciumchannelopathies pages 12-14)

### Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### Gene–environment interactions
No gene–environment interaction evidence specific to CACNA1F-related retinopathy was identified in the retrieved evidence. Mechanistic papers acknowledge that differential symptoms may involve “genomic and environmental deviations,” but without specific, testable GxE claims. (heigl2023characterizationoftwo pages 1-2)

---

## 3. Phenotypes

### Core phenotype profile (human)
CACNA1F-related retinopathy classically involves impaired signaling from photoreceptors to bipolar cells, producing a characteristic ERG pattern (electronegative/negative). Across cohorts, common features include reduced visual acuity, myopia (often high), nystagmus, variable nyctalopia and/or photophobia, and sometimes optic disc pallor/inner retinal thinning on OCT. (leahy2021opticatrophyand pages 3-6, marziali2023opticnerveinvolvement pages 6-10, wygledowskapromienska2024alandislandeye pages 1-2)

### Quantitative cohort data (selected)
**Leahy et al. 2021 (Genes; Feb 2021; DOI: https://doi.org/10.3390/genes12030330)** analyzed **22** molecularly confirmed CACNA1F-retinopathy subjects and reported: 
- Mean VA **0.42 LogMAR**; myopia in **15/22 (68%)**, mean **−6.32 D**; abnormal color vision in **6/21**; optic disc pallor in **21/22**; mean macular **GCL-IPL 55.00 µm** vs **84.57 µm** in controls (p << 0.001). (leahy2021opticatrophyand pages 1-2, leahy2021opticatrophyand pages 3-6, leahy2021opticatrophyand pages 6-7)

**Marziali et al. 2023 (Ophthalmic Genetics; Dec 2023; DOI: https://doi.org/10.1080/13816810.2022.2132514)** multicenter series of **12** patients emphasized long follow-up and stability:
- Mean follow-up **11.63 years** (range **6–18**), persistent myopia (reported as progressive high myopia in some), and **low pRNFL thickness in all patients**, with longitudinal stability in those tracked. (marziali2023opticnerveinvolvement pages 6-10, marziali2023opticnerveinvolvement pages 20-27)

### Phenotype characteristics (onset, course, frequency)
- **Onset:** Often congenital/early childhood for CSNB2A/AIED; CORDX3 is described as progressive and often begins in adulthood in spectrum reviews, although overlap is common. (wygledowskapromienska2024alandislandeye pages 1-2)
- **Course:** CSNB2A/AIED are usually described as non-progressive/stationary, but there is a spectrum including progressive phenotypes (CORDX3, X-linked retinitis pigmentosa-like presentations). (marziali2023opticnerveinvolvement pages 1-6, wygledowskapromienska2024alandislandeye pages 1-2, calderon2025anewphenotypic pages 5-7)
- **Phenotypic heterogeneity:** Frequently emphasized; genotype–phenotype correlations are weak/unclear in multiple sources. (mahmood2021anovelsplicesite pages 2-5, schaare2023concomitantcalciumchannelopathies pages 12-14)

### HPO term suggestions (non-exhaustive)
- Nyctalopia **HP:0000662**
- Photophobia **HP:0000613**
- Reduced visual acuity **HP:0007663**
- Myopia **HP:0000545** / High myopia **HP:0011003**
- Nystagmus **HP:0000639**
- Strabismus **HP:0000486**
- Abnormal electroretinogram **HP:0000556** (for electronegative ERG pattern)
- Optic disc pallor / optic atrophy **HP:0000648 / HP:0000649**
- Foveal hypoplasia **HP:0007368**
- Retinoschisis **HP:0007668** (reported within AIED spectrum case) (wygledowskapromienska2024alandislandeye pages 1-2)

### Quality-of-life impact
Direct validated QoL instruments (EQ-5D/SF-36/PROMIS) were not reported in the retrieved evidence set. Functional impact is indirectly supported by persistent reduced VA, myopia, and photophobia/nyctalopia affecting daily vision. (leahy2021opticatrophyand pages 3-6, marziali2023opticnerveinvolvement pages 1-6)

---

## 4. Genetic/Molecular Information

### Causal gene
- **CACNA1F** (Cav1.4 α1F subunit; Xp11.23; OMIM/MIM 300110) (marziali2023opticnerveinvolvement pages 1-6)

### Pathogenic variant spectrum
CACNA1F-associated disease includes diverse variant types (missense, nonsense, splice-site, indel, structural changes), with a large and growing allelic spectrum:
- One paper reports **“230 variants associated with CSNB2A,”** with subsets specific to AIED and shared between conditions. (mahmood2021anovelsplicesite pages 2-5)
- A review/case report also notes **“around 260 variants”** reported for AIED/CSNB2A spectrum disorders. (mahmood2021anovelsplicesite pages 1-2)
- Intronic/synonymous variants contribute non-trivially (reported “at least 4%” in one excerpt). (mahmood2021anovelsplicesite pages 8-8)

**Examples of recently reported variants with functional/clinical evidence:**
- **Splice-altering CACNA1F variant** investigated with functional splicing assays (midigene/RT-PCR in HEK293) leading to reclassification under ACMG/AMP/ClinGen frameworks: **NM_005183.4:c.2576+4_2576+5del**, producing “multimodal splice defect” with both in-frame insertion and frameshift outcomes. (ridgeway2024novelsplicealteringvariants pages 16-17)

### Variant functional consequences (mechanistic examples)
- **Voltage sensor/gating charge substitutions** (e.g., Arg964Gly; Arg1288Leu) can reduce expression and alter activation/inactivation; molecular dynamics suggested possible **ω-currents** (gating pore currents) as a proposed pathogenic mechanism. (heigl2023characterizationoftwo pages 1-2)

### Modifier genes / modifying factors
Evidence for specific modifier genes in CACNA1F disease was not identified in the retrieved full texts; however, multiple papers propose **unknown disease-modifying factors** to explain variability (including potential splice isoform effects). (wygledowskapromienska2024alandislandeye pages 1-2, calderon2025anewphenotypic pages 2-5)

### Epigenetic information / chromosomal abnormalities
No CACNA1F-specific epigenetic disease mechanism evidence was identified in the retrieved sources.

---

## 5. Environmental Information
No environmental, lifestyle, toxin, or infectious triggers were identified as causal contributors in the retrieved evidence set.

---

## 6. Mechanism / Pathophysiology

### Current mechanistic understanding (key concepts)
Cav1.4 channels are localized to photoreceptor synaptic terminals at ribbon synapses, where they provide Ca2+ influx that triggers vesicle fusion and glutamate release to downstream neurons.
- A review describes Cav1.4 channels clustering “beneath the synaptic ribbon” to enable Ca2+-dependent synaptic release, and notes that CACNA1F variants produce retinal disorders with variable loss- vs gain-of-function channel phenotypes. (ganglberger2025exploringthepotential pages 1-2)
- A cone-focused mechanistic study emphasizes a **non-conducting role**: Cav1.4 protein contributes to synaptogenesis, and compensatory currents (Cav3) can support photopic vision under some non-conducting Cav1.4 conditions. (maddox2024anonconductingrole pages 1-2)

### Causal chain (from gene to clinical manifestation)
1. **CACNA1F pathogenic variant** alters Cav1.4 channel abundance, biophysics, or synaptic localization (heigl2023characterizationoftwo pages 1-2, ganglberger2025exploringthepotential pages 1-2)
2. **Photoreceptor ribbon synapse dysfunction**: impaired Ca2+ signaling and/or abnormal ribbon maturation/architecture; errors in synaptic wiring, sprouting, ectopic synapses (zanetti2021functionofcone pages 1-2, ganglberger2025exploringthepotential pages 9-10)
3. **Defective photoreceptor→bipolar transmission** produces **electronegative ERG pattern** (reduced b-wave relative to a-wave), reflecting bipolar cell pathway dysfunction (leahy2021opticatrophyand pages 1-2, marziali2023opticnerveinvolvement pages 1-6)
4. **Clinical phenotype**: reduced VA, myopia, nystagmus, nyctalopia and/or photophobia; in some cohorts, optic disc pallor and inner retinal thinning (GCL-IPL and/or pRNFL/GCC) (leahy2021opticatrophyand pages 3-6, marziali2023opticnerveinvolvement pages 6-10, leahy2021opticatrophyand pages 7-8)

### Cell types (CL term suggestions)
- Photoreceptor cell (rod and cone) **CL:0000210 (photoreceptor cell)** (general)
- Bipolar cell **CL:0000740 (retinal bipolar neuron)** (general)
- Horizontal cell (retinal) **CL:0000741 (retinal horizontal cell)** (general)
- Retinal ganglion cell **CL:0000745** (general; implicated by GCC thinning metrics)

### Tissue/anatomy (UBERON suggestions)
- Retina **UBERON:0000966**
- Outer plexiform layer **UBERON:0001854** (photoreceptor synaptic layer; implied by ribbon synapse localization) (ganglberger2025exploringthepotential pages 9-10)
- Optic nerve **UBERON:0000953** (optic nerve involvement reported clinically) (marziali2023opticnerveinvolvement pages 6-10)

### GO biological process suggestions (non-exhaustive)
- Synaptic transmission, glutamatergic
- Calcium ion transmembrane transport
- Photoreceptor cell synapse organization
- Regulation of neurotransmitter secretion

### Immune involvement
Not supported in retrieved evidence.

### Molecular profiling (transcriptomics/proteomics/metabolomics)
No CACNA1F disease-specific omics signatures were identified in the retrieved evidence set.

---

## 7. Anatomical Structures Affected

### Organ/system level
- **Primary organ:** eye (retina); visual system. (ganglberger2025exploringthepotential pages 1-2)
- **Optic nerve/inner retina involvement:** pRNFL and GCC thinning, optic disc pallor/atrophy described in CACNA1F cohorts. (marziali2023opticnerveinvolvement pages 6-10, leahy2021opticatrophyand pages 7-8)

### Tissue/cell level
- Photoreceptor terminals and their postsynaptic partners at ribbon synapses (bipolar and horizontal cells). (ganglberger2025exploringthepotential pages 1-2, maddox2024anonconductingrole pages 1-2)

### Subcellular level
- Presynaptic active zone and ribbon synapse architecture (ribbon-associated channel clustering). (ganglberger2025exploringthepotential pages 1-2)

---

## 8. Temporal Development

### Onset
- CSNB2A/AIED: typically congenital or early childhood, with symptoms such as nystagmus, nyctalopia/photophobia, and high myopia in early life. (wygledowskapromienska2024alandislandeye pages 1-2, leahy2021opticatrophyand pages 3-6)

### Progression
- Stationary vs progressive spectrum: non-progressive forms (CSNB2A/AIED) contrasted with progressive phenotypes (CORDX3; XLRP-like). (wygledowskapromienska2024alandislandeye pages 1-2, marziali2023opticnerveinvolvement pages 1-6)
- Optic nerve metrics may be stable over follow-up (pRNFL stability). (marziali2023opticnerveinvolvement pages 6-10)

### Critical periods
Developmental mechanistic work indicates Cav1.4 is important for ribbon maturation after early postnatal stages in mice; this suggests timing constraints for some interventions, though human critical windows were not established in retrieved sources. (ganglberger2025exploringthepotential pages 6-9)

---

## 9. Inheritance and Population

### Inheritance pattern
- **X-linked recessive** inheritance is repeatedly documented. (wygledowskapromienska2024alandislandeye pages 1-2, marziali2023opticnerveinvolvement pages 1-6)

### Sex ratio and carrier phenotypes
- A literature review summarizing 54 CACNA1F patients reported **87% male** and **13% female**. (schaare2023concomitantcalciumchannelopathies pages 12-14)
- Female carriers are often asymptomatic but mild features (e.g., latent nystagmus, color vision disturbance, ERG abnormalities) are reported. (mahmood2021anovelsplicesite pages 1-2, marziali2023opticnerveinvolvement pages 1-6)

### Penetrance/expressivity
- Expressivity is variable across allelic conditions; multiple sources emphasize lack of clear genotype–phenotype correlation and possible modifying factors. (mahmood2021anovelsplicesite pages 2-5, wygledowskapromienska2024alandislandeye pages 1-2)

### Epidemiology
- A case report/review cited an estimated **birth prevalence of AIED ~1 in 22,000 live-born males** (secondary reporting within a case report; not independently validated in retrieved evidence set). (calderon2025anewphenotypic pages 1-2)
- Robust prevalence/incidence estimates for CACNA1F-related retinopathy overall were not identified in retrieved evidence.

---

## 10. Diagnostics

### Key diagnostic concept
**Electrophysiology is central.** Multiple sources emphasize full-field ERG as the key diagnostic test, especially when clinical symptoms are atypical.

### Clinical tests and findings
- **Full-field ERG (ISCEV):** pathognomonic **electronegative/negative ERG** pattern (Schubert–Bornschein), reflecting bipolar cell pathway dysfunction. (marziali2023opticnerveinvolvement pages 1-6, durajczyk2025congenitalstationarynight pages 10-12, leahy2021opticatrophyand pages 1-2)
- **ON–OFF ERG:** differentiates complete vs incomplete CSNB based on ON vs ON+OFF bipolar cell dysfunction patterns. (durajczyk2025congenitalstationarynight pages 10-12)
- **OCT:** may show inner retinal thinning (GCL-IPL) and/or reduced pRNFL/GCC thickness; foveal hypoplasia, retinoschisis can be present in spectrum cases. (leahy2021opticatrophyand pages 7-8, marziali2023opticnerveinvolvement pages 6-10, wygledowskapromienska2024alandislandeye pages 1-2)
- **mfERG / pVEP:** used as adjuncts in CSNB cases (cone system dysfunction, prolonged peak times/latencies). (durajczyk2025congenitalstationarynight pages 12-14, durajczyk2025congenitalstationarynight pages 5-10)

### Diagnostic yield / genetic testing strategy
- A Swedish IRD cohort re-investigation (322-gene NGS panel) achieved **65%** overall molecular diagnostic yield, with **CACNA1F accounting for ~3%** among prevalent solved genes reported. (areblom2023adescriptionof pages 1-2)
- Diagnostic modalities used in CACNA1F cohorts include **WES** and custom targeted NGS panels. (marziali2023opticnerveinvolvement pages 6-10)

### Differential diagnosis (electronegative ERG)
A CSNB review highlights that electronegative ERG has a differential including unilateral causes (ischemia, siderosis) and bilateral causes (autoimmune retinopathy, vitamin A deficiency, photoreceptor dystrophies), supporting the need for careful interpretation and genetic confirmation. (durajczyk2025congenitalstationarynight pages 10-12)

### Diagnostic pitfall (photophobia without night blindness)
A case series emphasizes that **photophobia can be the presenting symptom**, making CACNA1F-CSNB2 harder to recognize unless extended ffERG is performed. (marziali2023opticnerveinvolvement pages 1-6)

---

## 11. Outcome / Prognosis

### Visual prognosis
- Cohort data indicate persistent reduced VA and high myopia are common, with evidence for stable clinical course in some domains (e.g., stable BCVA and stable pRNFL over years in a multicenter series). (marziali2023opticnerveinvolvement pages 6-10, marziali2023opticnerveinvolvement pages 10-14)

### Morbidity and disability
Formal disability/QoL scales were not retrieved; functional limitation is supported by reduced acuity and refractive error burden. (leahy2021opticatrophyand pages 3-6)

### Mortality
No disease-specific mortality is expected or reported in the retrieved evidence.

---

## 12. Treatment

### Current real-world management
Direct guidelines for supportive care (e.g., refractive correction, low-vision support) were not described in the retrieved evidence set; such interventions are standard in inherited retinal disease care but are not cited here.

### Emerging/experimental therapeutics

#### Gene therapy and gene-based strategies (preclinical; expert review)
A 2025 review focused on Cav1.4-related retinal channelopathies describes several experimental gene-based strategies (preclinical), while emphasizing major translational barriers:
- Strategies discussed include **β2 subunit augmentation** (smaller gene; potentially AAV-packable) to help restore Cav1.4 channel protein in loss-of-function contexts. (ganglberger2025exploringthepotential pages 12-13)
- Experimental attempts include in vivo electroporation to reintroduce Cav1.4α1 with partial functional recovery in animal models, and other synapse-restoration approaches, but the review notes limitations such as low transfection efficiency, small sample sizes, and complications. (ganglberger2025exploringthepotential pages 13-15)
- A central limitation is **CACNA1F gene size exceeding single-AAV packaging**, motivating dual-AAV approaches and other delivery innovations; the authors conclude approaches are not yet ready for routine clinical translation. (ganglberger2025exploringthepotential pages 15-16)

#### Pharmacologic approaches (hypothesis-level, preclinical)
In a Cav1.4-IT mouse study, acute reduction of Ca2+ influx by calcium channel blockade did not rescue synaptic transmission deficits, but the authors propose that **long-term low-dose Ca2+ channel blocker treatment might reduce Ca2+ toxicity** without major loss of ganglion cell responses. (zanetti2021functionofcone pages 1-2)

### Clinical trials
In the clinical trial searches performed, **no CACNA1F-specific retinal interventional trials were identified**. One retrieved trial involving Cav1.4 addressed psoriasis immunology rather than retinal disease (NCT04459780, not cited in mechanistic/retinal evidence).

### MAXO suggestions (management actions; non-exhaustive)
- Genetic testing **MAXO:0000127** (general)
- Low vision rehabilitation **MAXO:0000662** (general)
- Gene therapy procedure **MAXO:0001001** (general; experimental/preclinical context)

---

## 13. Prevention

### Primary prevention
Not applicable for a Mendelian X-linked disorder (no environmental prevention identified in retrieved evidence).

### Secondary prevention
- **Genetic counseling** and cascade testing are supported indirectly by the X-linked inheritance pattern and carrier state discussion. (mahmood2021anovelsplicesite pages 1-2, wygledowskapromienska2024alandislandeye pages 1-2)

---

## 14. Other Species / Natural Disease
The retrieved evidence set mentions multi-species research models (rat, zebrafish), but does not document naturally occurring veterinary disease caused by CACNA1F variants.

---

## 15. Model Organisms

### Mouse models (key examples)
- **Cav1.4 KO**: severe synaptic defects and functional blindness, often more severe than human disease. (maddox2024anonconductingrole pages 1-2, ganglberger2025exploringthepotential pages 6-9)
- **G369i KI (non-conducting Cav1.4)**: preserves photopic visual behavior despite synaptic abnormalities, supporting non-conducting roles and homeostatic plasticity. (maddox2024anonconductingrole pages 1-2)
- **I756T / Cav1.4-IT KI (gain-of-function)**: produces ERG abnormalities similar to human CSNB2 with impaired cone pathways and sprouting. (zanetti2021functionofcone pages 1-2)
- **Cone-rich “Conefull” crosses**: Conefull:α1F KO vs Conefull:α2δ4 KO recapitulate severe vs milder cone synaptopathy phenotypes and enable cone-pathway-focused mechanistic studies. (laird2023mouseallconeretina pages 1-2)

### Other species
- A Cav1.4 review summarizes **rat** models (e.g., p.R981X) and **zebrafish cacna1fa** models showing cone ERG and vision loss phenotypes. (ganglberger2025exploringthepotential pages 4-6)

---

## Summary Table (phenotypic spectrum and quantitative markers)
The following table compiles key disease entities, diagnostic hallmarks, and quantitative cohort findings useful for a disease knowledge base entry.

| Phenotype/entity (with OMIM) | Typical onset/course | Key symptoms/signs (HPO suggestions inline) | Key diagnostic tests/findings (ERG/OCT) | Quantitative data (VA, refractive error, OCT thickness, frequencies) | Key citations (DOI/URL and year) |
|---|---|---|---|---|---|
| **CSNB2A / incomplete CSNB (OMIM #300071)** | Congenital or early-childhood onset; classically non-progressive/stationary, though phenotypic variability is recognized across CACNA1F-associated disease (marziali2023opticnerveinvolvement pages 1-6, mahmood2021anovelsplicesite pages 1-2, mahmood2021anovelsplicesite pages 5-8) | Nyctalopia **[HP:0000662]**, reduced visual acuity **[HP:0007663]**, myopia/high myopia **[HP:0000545/HP:0011003]**, nystagmus **[HP:0000639]**, strabismus **[HP:0000486]**, photophobia **[HP:0000613]**, red-green color vision defect/dyschromatopsia **[HP:0000654]** (leahy2021opticatrophyand pages 1-2, leahy2021opticatrophyand pages 3-6, mahmood2021anovelsplicesite pages 1-2) | Full-field ERG shows the characteristic **electronegative/negative Schubert-Bornschein pattern** with preserved or relatively preserved a-wave and reduced b-wave, indicating bipolar cell dysfunction; OCT may show inner retinal thinning/GCL-IPL loss and sometimes fundus changes mainly related to myopia (wygledowskapromienska2024alandislandeye pages 1-2, marziali2023opticnerveinvolvement pages 1-6, leahy2021opticatrophyand pages 6-7) | In a molecularly confirmed cohort, mean distance VA **0.42 LogMAR**; myopia in **15/22 (68%)**, mean spherical equivalent **−6.32 D**; abnormal color vision in **6/21**; mean GCL-IPL thickness **55.00 µm** vs **84.57 µm** in controls; optic disc pallor in **21/22** (leahy2021opticatrophyand pages 1-2, leahy2021opticatrophyand pages 3-6, leahy2021opticatrophyand pages 7-8) | Leahy 2021, doi:10.3390/genes12030330, https://doi.org/10.3390/genes12030330 (leahy2021opticatrophyand pages 1-2, leahy2021opticatrophyand pages 3-6, leahy2021opticatrophyand pages 7-8); Mahmood 2021, doi:10.3390/genes12020171, https://doi.org/10.3390/genes12020171 (mahmood2021anovelsplicesite pages 1-2); Schaare 2023, doi:10.3390/genes14020400, https://doi.org/10.3390/genes14020400 (schaare2023concomitantcalciumchannelopathies pages 1-2) |
| **Åland Island eye disease (AIED) (OMIM #300600)** | Early-childhood onset; traditionally considered an incomplete/non-progressive CACNA1F disorder overlapping strongly with iCSNB/CSNB2A (mahmood2021anovelsplicesite pages 1-2, mahmood2021anovelsplicesite pages 5-8) | Nystagmus **[HP:0000639]**, low visual acuity **[HP:0007663]**, high myopia **[HP:0011003]**, protan/red-green color vision defect **[HP:0000654]**, retinal hypopigmentation/ocular hypopigmentation **[HP:0011508]**, iris transillumination **[HP:0001088]**, foveal hypoplasia **[HP:0007368]**, nyctalopia **[HP:0000662]** (wygledowskapromienska2024alandislandeye pages 1-2, mahmood2021anovelsplicesite pages 1-2) | ffERG: attenuated dark-adapted a-waves with **abolished b-waves** producing a **negative ERG**; OCT can show **retinoschisis** and **foveal hypoplasia**; phenotype may be electrophysiologically indistinguishable from CSNB2A in some patients (wygledowskapromienska2024alandislandeye pages 1-2, mahmood2021anovelsplicesite pages 5-8) | Case-level data: 57-year-old man with symptoms since early childhood had bilateral high myopia, diffuse retinal thinning/hypopigmentation, retinoschisis in one eye, foveal hypoplasia in the other; DA 3.0 a-waves attenuated and b-waves abolished; pathogenic hemizygous **c.4051C>T** stop-gain variant reported (wygledowskapromienska2024alandislandeye pages 1-2) | Wyględowska-Promieńska 2024, doi:10.3390/ijms25052928, https://doi.org/10.3390/ijms25052928 (wygledowskapromienska2024alandislandeye pages 1-2); Mahmood 2021, doi:10.3390/genes12020171, https://doi.org/10.3390/genes12020171 (mahmood2021anovelsplicesite pages 1-2, mahmood2021anovelsplicesite pages 5-8); Schaare 2023, doi:10.3390/genes14020400, https://doi.org/10.3390/genes14020400 (schaare2023concomitantcalciumchannelopathies pages 1-2) |
| **CORDX3 / X-linked cone-rod dystrophy type 3 (OMIM #300476)** | Often progressive and may present later than stationary forms; adult-onset/progressive decline in refraction, acuity, color vision, and fields is described, but some recent reports include earlier-onset/high-myopia presentations (wygledowskapromienska2024alandislandeye pages 1-2, marziali2023opticnerveinvolvement pages 1-6) | Decreased visual acuity **[HP:0007663]**, high myopia **[HP:0011003]**, dyschromatopsia/color vision defect **[HP:0000654]**, photophobia **[HP:0000613]**, visual field abnormality **[HP:0001123]**, macular outer retinal abnormality/atrophy **[HP:0007754]** (wygledowskapromienska2024alandislandeye pages 1-2, calderon2025anewphenotypic pages 5-7) | ERG in cone-rod dystrophy presentations may show markedly reduced/non-recordable photopic responses with reduced scotopic responses; OCT/fundus may show macular outer retinal structural abnormalities; genetic confirmation is essential because phenotype overlaps other IRDs (calderon2025anewphenotypic pages 5-7, calderon2025anewphenotypic pages 2-5) | Family study reported 2 X-linked CORD probands with **CACNA1F** variants (**c.2201del**, **c.245G>A**), both with **high myopia** and macular outer structural abnormalities; broader reviews note progressive deterioration in acuity, color vision, and visual fields in CORDX3 (wygledowskapromienska2024alandislandeye pages 1-2, calderon2025anewphenotypic pages 5-7) | Wyględowska-Promieńska 2024, doi:10.3390/ijms25052928, https://doi.org/10.3390/ijms25052928 (wygledowskapromienska2024alandislandeye pages 1-2); Calderon 2025, doi:10.7759/cureus.82577, https://doi.org/10.7759/cureus.82577 (calderon2025anewphenotypic pages 5-7, calderon2025anewphenotypic pages 2-5); Schaare 2023, doi:10.3390/genes14020400, https://doi.org/10.3390/genes14020400 (schaare2023concomitantcalciumchannelopathies pages 1-2) |
| **CACNA1F-related disease with optic nerve involvement** | Early-onset/congenital phenotype with optic nerve changes that appear largely **stable over time** rather than progressive optic neuropathy (marziali2023opticnerveinvolvement pages 10-14, marziali2023opticnerveinvolvement pages 6-10, marziali2023opticnerveinvolvement pages 20-27) | Optic disc pallor/optic atrophy **[HP:0000648/HP:0000649]**, reduced peripapillary RNFL **[suggested retinal nerve fiber layer thinning]**, ganglion cell complex thinning **[HP:0031610-like inner retinal thinning]**, reduced visual acuity **[HP:0007663]**, myopia **[HP:0000545]**, occasional foveal hypoplasia **[HP:0007368]** (leahy2021opticatrophyand pages 1-2, marziali2023opticnerveinvolvement pages 6-10, marziali2023opticnerveinvolvement pages 20-27) | SD-OCT shows **bilateral low pRNFL and GCC/GCL thickness**; ffERG remains pathognomonic with electronegative dark-adapted responses; MRI can be unremarkable, supporting retinal/optic pathway structural involvement without gross intracranial abnormality (marziali2023opticnerveinvolvement pages 6-10, marziali2023opticnerveinvolvement pages 20-27) | Multicenter series: **12 patients**, mean follow-up **11.63 years** (range **6–18**); myopia ranged from **−6.00 D to −21.00 D** in some cases; visual acuity examples **0.2–0.7 LogMAR** and longitudinally stable; pRNFL low in **all patients** with stability over **1–6 years** in those followed serially. Separate 22-subject cohort: optic disc pallor in **21/22**, mean pRNFL **68.67 µm**, temporal RNFL **51.33 µm**, mean GCL-IPL **54.50–55.00 µm** (marziali2023opticnerveinvolvement pages 6-10, marziali2023opticnerveinvolvement pages 20-27, leahy2021opticatrophyand pages 7-8, leahy2021opticatrophyand pages 1-2) | Marziali 2023, doi:10.1080/13816810.2022.2132514, https://doi.org/10.1080/13816810.2022.2132514 (marziali2023opticnerveinvolvement pages 10-14, marziali2023opticnerveinvolvement pages 6-10, marziali2023opticnerveinvolvement pages 20-27); Leahy 2021, doi:10.3390/genes12030330, https://doi.org/10.3390/genes12030330 (leahy2021opticatrophyand pages 1-2, leahy2021opticatrophyand pages 7-8) |


*Table: This table summarizes the major CACNA1F-related retinal disease entities, highlighting their clinical overlap and the most useful quantitative findings from ERG and OCT studies. It is useful for comparing stationary and progressive presentations and for identifying features that support diagnosis.*

---

## Notes on evidence limitations
- **PMID limitation:** Many retrieved sources are available via DOI/URL in the evidence set; PubMed IDs were not provided in the tool outputs and are therefore not asserted.
- **Ontology IDs:** MONDO/Orphanet/ICD/MeSH identifiers were not extractable from the retrieved full texts; only OMIM IDs were available.
- **Population epidemiology:** High-quality population prevalence/incidence data for CACNA1F-related retinopathy were not identified in the retrieved evidence set.


References

1. (marziali2023opticnerveinvolvement pages 1-6): Elisa Marziali, Filip Van Den Broeck, Sara Bargiacchi, Pina Fortunato, Roberto Caputo, Andrea Sodi, Julie De Zaeytijd, Vittoria Murro, Dario Pasquale Mucciolo, Dario Giorgio, Ilaria Passerini, Viviana Palazzo, Francesca Peluso, Elfride de Baere, Christina Zeitz, Bart P. Leroy, Jacopo Secci, and Giacomo M. Bacci. Optic nerve involvement in cacna1f-related disease: observations from a multicentric case series. Ophthalmic Genetics, 44:152-162, Dec 2023. URL: https://doi.org/10.1080/13816810.2022.2132514, doi:10.1080/13816810.2022.2132514. This article has 3 citations and is from a peer-reviewed journal.

2. (wygledowskapromienska2024alandislandeye pages 1-2): Dorota Wyględowska-Promieńska, Marta Świerczyńska, Dorota Śpiewak, Dorota Pojda-Wilczek, Agnieszka Tronina, Mariola Dorecka, and Adrian Smędowski. Aland island eye disease with retinoschisis in the clinical spectrum of cacna1f-associated retinopathy—a case report. International Journal of Molecular Sciences, 25:2928, Mar 2024. URL: https://doi.org/10.3390/ijms25052928, doi:10.3390/ijms25052928. This article has 4 citations.

3. (mahmood2021anovelsplicesite pages 5-8): Usman Mahmood, Cécile Méjécase, Syed M. A. Ali, Mariya Moosajee, and Igor Kozak. A novel splice-site variant in cacna1f causes a phenotype synonymous with åland island eye disease and incomplete congenital stationary night blindness. Genes, 12:171, Jan 2021. URL: https://doi.org/10.3390/genes12020171, doi:10.3390/genes12020171. This article has 20 citations.

4. (mahmood2021anovelsplicesite pages 1-2): Usman Mahmood, Cécile Méjécase, Syed M. A. Ali, Mariya Moosajee, and Igor Kozak. A novel splice-site variant in cacna1f causes a phenotype synonymous with åland island eye disease and incomplete congenital stationary night blindness. Genes, 12:171, Jan 2021. URL: https://doi.org/10.3390/genes12020171, doi:10.3390/genes12020171. This article has 20 citations.

5. (schaare2023concomitantcalciumchannelopathies pages 1-2): Donna Schaare, Sara M. Sarasua, Laina Lusk, Shridhar Parthasarathy, Liangjiang Wang, Ingo Helbig, and Luigi Boccuto. Concomitant calcium channelopathies involving cacna1a and cacna1f: a case report and review of the literature. Genes, 14:400, Feb 2023. URL: https://doi.org/10.3390/genes14020400, doi:10.3390/genes14020400. This article has 5 citations.

6. (marziali2023opticnerveinvolvement pages 14-20): Elisa Marziali, Filip Van Den Broeck, Sara Bargiacchi, Pina Fortunato, Roberto Caputo, Andrea Sodi, Julie De Zaeytijd, Vittoria Murro, Dario Pasquale Mucciolo, Dario Giorgio, Ilaria Passerini, Viviana Palazzo, Francesca Peluso, Elfride de Baere, Christina Zeitz, Bart P. Leroy, Jacopo Secci, and Giacomo M. Bacci. Optic nerve involvement in cacna1f-related disease: observations from a multicentric case series. Ophthalmic Genetics, 44:152-162, Dec 2023. URL: https://doi.org/10.1080/13816810.2022.2132514, doi:10.1080/13816810.2022.2132514. This article has 3 citations and is from a peer-reviewed journal.

7. (marziali2023opticnerveinvolvement pages 6-10): Elisa Marziali, Filip Van Den Broeck, Sara Bargiacchi, Pina Fortunato, Roberto Caputo, Andrea Sodi, Julie De Zaeytijd, Vittoria Murro, Dario Pasquale Mucciolo, Dario Giorgio, Ilaria Passerini, Viviana Palazzo, Francesca Peluso, Elfride de Baere, Christina Zeitz, Bart P. Leroy, Jacopo Secci, and Giacomo M. Bacci. Optic nerve involvement in cacna1f-related disease: observations from a multicentric case series. Ophthalmic Genetics, 44:152-162, Dec 2023. URL: https://doi.org/10.1080/13816810.2022.2132514, doi:10.1080/13816810.2022.2132514. This article has 3 citations and is from a peer-reviewed journal.

8. (leahy2021opticatrophyand pages 3-6): Kate E Leahy, Tom Wright, Monika K Grudzinska Pechhacker, Isabelle Audo, Anupreet Tumber, Erika Tavares, Heather MacDonald, Jeff Locke, Cynthia VandenHoven, Christina Zeitz, Elise Heon, J Raymond Buncic, and Ajoy Vincent. Optic atrophy and inner retinal thinning in cacna1f-related congenital stationary night blindness. Genes, 12:330, Feb 2021. URL: https://doi.org/10.3390/genes12030330, doi:10.3390/genes12030330. This article has 17 citations.

9. (laird2023mouseallconeretina pages 1-2): Joseph G. Laird, Ariel Kopel, Colten K. Lankford, and Sheila A. Baker. Mouse all-cone retina models of cav1.4 synaptopathy. Frontiers in Molecular Neuroscience, Apr 2023. URL: https://doi.org/10.3389/fnmol.2023.1155955, doi:10.3389/fnmol.2023.1155955. This article has 2 citations.

10. (maddox2024anonconductingrole pages 1-2): J Wesley Maddox, Gregory J Ordemann, Juan de la Rosa Vázquez, Angie Huang, Christof Gault, Serena R Wisner, Kate Randall, Daiki Futagi, Nihal A Salem, R Dayne Mayfield, Boris V Zemelman, Steven H DeVries, Mrinalini Hoon, and Amy Lee. A non-conducting role of the cav1.4 ca2+ channel drives homeostatic plasticity at the cone photoreceptor synapse. eLife, Nov 2024. URL: https://doi.org/10.7554/elife.94908.4, doi:10.7554/elife.94908.4. This article has 7 citations and is from a domain leading peer-reviewed journal.

11. (ganglberger2025exploringthepotential pages 1-2): Matthias Ganglberger and Alexandra Koschak. Exploring the potential for gene therapy in cav1.4-related retinal channelopathies. Channels, Mar 2025. URL: https://doi.org/10.1080/19336950.2025.2480089, doi:10.1080/19336950.2025.2480089. This article has 0 citations and is from a peer-reviewed journal.

12. (schaare2023concomitantcalciumchannelopathies pages 12-14): Donna Schaare, Sara M. Sarasua, Laina Lusk, Shridhar Parthasarathy, Liangjiang Wang, Ingo Helbig, and Luigi Boccuto. Concomitant calcium channelopathies involving cacna1a and cacna1f: a case report and review of the literature. Genes, 14:400, Feb 2023. URL: https://doi.org/10.3390/genes14020400, doi:10.3390/genes14020400. This article has 5 citations.

13. (heigl2023characterizationoftwo pages 1-2): Thomas Heigl, Michael A. Netzer, Lucia Zanetti, Matthias Ganglberger, Monica L. Fernández-Quintero, and Alexandra Koschak. Characterization of two pathological gating-charge substitutions in cav1.4 l-type calcium channels. Channels, Mar 2023. URL: https://doi.org/10.1080/19336950.2023.2192360, doi:10.1080/19336950.2023.2192360. This article has 2 citations and is from a peer-reviewed journal.

14. (leahy2021opticatrophyand pages 1-2): Kate E Leahy, Tom Wright, Monika K Grudzinska Pechhacker, Isabelle Audo, Anupreet Tumber, Erika Tavares, Heather MacDonald, Jeff Locke, Cynthia VandenHoven, Christina Zeitz, Elise Heon, J Raymond Buncic, and Ajoy Vincent. Optic atrophy and inner retinal thinning in cacna1f-related congenital stationary night blindness. Genes, 12:330, Feb 2021. URL: https://doi.org/10.3390/genes12030330, doi:10.3390/genes12030330. This article has 17 citations.

15. (leahy2021opticatrophyand pages 6-7): Kate E Leahy, Tom Wright, Monika K Grudzinska Pechhacker, Isabelle Audo, Anupreet Tumber, Erika Tavares, Heather MacDonald, Jeff Locke, Cynthia VandenHoven, Christina Zeitz, Elise Heon, J Raymond Buncic, and Ajoy Vincent. Optic atrophy and inner retinal thinning in cacna1f-related congenital stationary night blindness. Genes, 12:330, Feb 2021. URL: https://doi.org/10.3390/genes12030330, doi:10.3390/genes12030330. This article has 17 citations.

16. (marziali2023opticnerveinvolvement pages 20-27): Elisa Marziali, Filip Van Den Broeck, Sara Bargiacchi, Pina Fortunato, Roberto Caputo, Andrea Sodi, Julie De Zaeytijd, Vittoria Murro, Dario Pasquale Mucciolo, Dario Giorgio, Ilaria Passerini, Viviana Palazzo, Francesca Peluso, Elfride de Baere, Christina Zeitz, Bart P. Leroy, Jacopo Secci, and Giacomo M. Bacci. Optic nerve involvement in cacna1f-related disease: observations from a multicentric case series. Ophthalmic Genetics, 44:152-162, Dec 2023. URL: https://doi.org/10.1080/13816810.2022.2132514, doi:10.1080/13816810.2022.2132514. This article has 3 citations and is from a peer-reviewed journal.

17. (calderon2025anewphenotypic pages 5-7): Ricardo A Murati Calderon and Natalio Izquierdo. A new phenotypic expression in a patient with a mutation in the cacna1f gene. Cureus, Apr 2025. URL: https://doi.org/10.7759/cureus.82577, doi:10.7759/cureus.82577. This article has 2 citations.

18. (mahmood2021anovelsplicesite pages 2-5): Usman Mahmood, Cécile Méjécase, Syed M. A. Ali, Mariya Moosajee, and Igor Kozak. A novel splice-site variant in cacna1f causes a phenotype synonymous with åland island eye disease and incomplete congenital stationary night blindness. Genes, 12:171, Jan 2021. URL: https://doi.org/10.3390/genes12020171, doi:10.3390/genes12020171. This article has 20 citations.

19. (mahmood2021anovelsplicesite pages 8-8): Usman Mahmood, Cécile Méjécase, Syed M. A. Ali, Mariya Moosajee, and Igor Kozak. A novel splice-site variant in cacna1f causes a phenotype synonymous with åland island eye disease and incomplete congenital stationary night blindness. Genes, 12:171, Jan 2021. URL: https://doi.org/10.3390/genes12020171, doi:10.3390/genes12020171. This article has 20 citations.

20. (ridgeway2024novelsplicealteringvariants pages 16-17): Anna R. Ridgeway, Ciara Shortall, Laura K. Finnegan, Róisín Long, Evan Matthews, Adrian Dockery, Ella Kopčić, Laura Whelan, Claire Kirk, Giuliana Silvestri, Jacqueline Turner, David J. Keegan, Sophia Millington-Ward, Naomi Chadderton, Emma Duignan, Paul F. Kenna, and G. Jane Farrar. Novel splice-altering variants in the chm and cacna1f genes causative of x-linked choroideremia and cone dystrophy. Genes, 16:25, Dec 2024. URL: https://doi.org/10.3390/genes16010025, doi:10.3390/genes16010025. This article has 2 citations.

21. (calderon2025anewphenotypic pages 2-5): Ricardo A Murati Calderon and Natalio Izquierdo. A new phenotypic expression in a patient with a mutation in the cacna1f gene. Cureus, Apr 2025. URL: https://doi.org/10.7759/cureus.82577, doi:10.7759/cureus.82577. This article has 2 citations.

22. (zanetti2021functionofcone pages 1-2): Lucia Zanetti, Irem Kilicarslan, Michael Netzer, Norbert Babai, Hartwig Seitter, and Alexandra Koschak. Function of cone and cone-related pathways in cav1.4 it mice. Scientific Reports, Feb 2021. URL: https://doi.org/10.1038/s41598-021-82210-7, doi:10.1038/s41598-021-82210-7. This article has 13 citations and is from a peer-reviewed journal.

23. (ganglberger2025exploringthepotential pages 9-10): Matthias Ganglberger and Alexandra Koschak. Exploring the potential for gene therapy in cav1.4-related retinal channelopathies. Channels, Mar 2025. URL: https://doi.org/10.1080/19336950.2025.2480089, doi:10.1080/19336950.2025.2480089. This article has 0 citations and is from a peer-reviewed journal.

24. (leahy2021opticatrophyand pages 7-8): Kate E Leahy, Tom Wright, Monika K Grudzinska Pechhacker, Isabelle Audo, Anupreet Tumber, Erika Tavares, Heather MacDonald, Jeff Locke, Cynthia VandenHoven, Christina Zeitz, Elise Heon, J Raymond Buncic, and Ajoy Vincent. Optic atrophy and inner retinal thinning in cacna1f-related congenital stationary night blindness. Genes, 12:330, Feb 2021. URL: https://doi.org/10.3390/genes12030330, doi:10.3390/genes12030330. This article has 17 citations.

25. (ganglberger2025exploringthepotential pages 6-9): Matthias Ganglberger and Alexandra Koschak. Exploring the potential for gene therapy in cav1.4-related retinal channelopathies. Channels, Mar 2025. URL: https://doi.org/10.1080/19336950.2025.2480089, doi:10.1080/19336950.2025.2480089. This article has 0 citations and is from a peer-reviewed journal.

26. (calderon2025anewphenotypic pages 1-2): Ricardo A Murati Calderon and Natalio Izquierdo. A new phenotypic expression in a patient with a mutation in the cacna1f gene. Cureus, Apr 2025. URL: https://doi.org/10.7759/cureus.82577, doi:10.7759/cureus.82577. This article has 2 citations.

27. (durajczyk2025congenitalstationarynight pages 10-12): Magdalena Durajczyk and Wojciech Lubiński. Congenital stationary night blindness (csnb)—case reports and review of current knowledge. Feb 2025. URL: https://doi.org/10.3390/jcm14041238, doi:10.3390/jcm14041238. This article has 9 citations.

28. (durajczyk2025congenitalstationarynight pages 12-14): Magdalena Durajczyk and Wojciech Lubiński. Congenital stationary night blindness (csnb)—case reports and review of current knowledge. Feb 2025. URL: https://doi.org/10.3390/jcm14041238, doi:10.3390/jcm14041238. This article has 9 citations.

29. (durajczyk2025congenitalstationarynight pages 5-10): Magdalena Durajczyk and Wojciech Lubiński. Congenital stationary night blindness (csnb)—case reports and review of current knowledge. Feb 2025. URL: https://doi.org/10.3390/jcm14041238, doi:10.3390/jcm14041238. This article has 9 citations.

30. (areblom2023adescriptionof pages 1-2): Maria Areblom, Sten Kjellström, Sten Andréasson, Anders Öhberg, Lotta Gränse, and Ulrika Kjellström. A description of the yield of genetic reinvestigation in patients with inherited retinal dystrophies and previous inconclusive genetic testing. Genes, 14:1413, Jul 2023. URL: https://doi.org/10.3390/genes14071413, doi:10.3390/genes14071413. This article has 8 citations.

31. (marziali2023opticnerveinvolvement pages 10-14): Elisa Marziali, Filip Van Den Broeck, Sara Bargiacchi, Pina Fortunato, Roberto Caputo, Andrea Sodi, Julie De Zaeytijd, Vittoria Murro, Dario Pasquale Mucciolo, Dario Giorgio, Ilaria Passerini, Viviana Palazzo, Francesca Peluso, Elfride de Baere, Christina Zeitz, Bart P. Leroy, Jacopo Secci, and Giacomo M. Bacci. Optic nerve involvement in cacna1f-related disease: observations from a multicentric case series. Ophthalmic Genetics, 44:152-162, Dec 2023. URL: https://doi.org/10.1080/13816810.2022.2132514, doi:10.1080/13816810.2022.2132514. This article has 3 citations and is from a peer-reviewed journal.

32. (ganglberger2025exploringthepotential pages 12-13): Matthias Ganglberger and Alexandra Koschak. Exploring the potential for gene therapy in cav1.4-related retinal channelopathies. Channels, Mar 2025. URL: https://doi.org/10.1080/19336950.2025.2480089, doi:10.1080/19336950.2025.2480089. This article has 0 citations and is from a peer-reviewed journal.

33. (ganglberger2025exploringthepotential pages 13-15): Matthias Ganglberger and Alexandra Koschak. Exploring the potential for gene therapy in cav1.4-related retinal channelopathies. Channels, Mar 2025. URL: https://doi.org/10.1080/19336950.2025.2480089, doi:10.1080/19336950.2025.2480089. This article has 0 citations and is from a peer-reviewed journal.

34. (ganglberger2025exploringthepotential pages 15-16): Matthias Ganglberger and Alexandra Koschak. Exploring the potential for gene therapy in cav1.4-related retinal channelopathies. Channels, Mar 2025. URL: https://doi.org/10.1080/19336950.2025.2480089, doi:10.1080/19336950.2025.2480089. This article has 0 citations and is from a peer-reviewed journal.

35. (ganglberger2025exploringthepotential pages 4-6): Matthias Ganglberger and Alexandra Koschak. Exploring the potential for gene therapy in cav1.4-related retinal channelopathies. Channels, Mar 2025. URL: https://doi.org/10.1080/19336950.2025.2480089, doi:10.1080/19336950.2025.2480089. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CACNA1F-Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md)