---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-05T21:56:37.656319'
end_time: '2026-08-05T22:07:27.596624'
duration_seconds: 649.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: TRAPPC12-Related Encephalopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: TRAPPC12-Related_Encephalopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TRAPPC12-Related Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TRAPPC12-Related Encephalopathy** covering all of the
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
- **Disease Name:** TRAPPC12-Related Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TRAPPC12-Related Encephalopathy** covering all of the
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


# TRAPPC12-Related Encephalopathy: Disease-Characteristics Research Report

## Executive summary

TRAPPC12-related encephalopathy is an ultra-rare autosomal-recessive neurodevelopmental/neurodegenerative disorder caused by biallelic pathogenic variants in **TRAPPC12**, a metazoan TRAPPIII-complex subunit involved in COPII-associated ER-to-Golgi trafficking. The best-established phenotype combines congenital or acquired microcephaly, profound developmental impairment or regression, hypotonia evolving with appendicular spasticity, dystonia/myoclonus, hearing and visual impairment, epilepsy in some patients, dysphagia, scoliosis, and a characteristic MRI pattern of severe cortical atrophy, corpus-callosum agenesis/hypoplasia, pons hypoplasia, ventriculomegaly, and abnormal white-matter signal. Later reports expanded the spectrum to milder encephalopathy without epilepsy or microcephaly and to severe fetal hydrocephalus. Evidence remains limited to a handful of families, patient fibroblasts, and engineered cell lines; no disease-specific therapy, guideline, epidemiologic study, clinical trial, animal disease model, or validated biomarker is established. (hall2024trappopathiesseveremultisystem pages 12-14, milev2017mutationsintrappc12 pages 1-2, yucesan2023functionalcharacterizationof pages 1-4)

The following table summarizes the most knowledge-base-ready findings.

| Domain | Summary | Ontology term suggestions | Key evidence |
|---|---|---|---|
| Definition / names | Ultra-rare Mendelian neurodevelopmental disorder caused by biallelic TRAPPC12 variants, first linked in 2017 to progressive childhood encephalopathy with Golgi dysfunction. Names used in the literature include **TRAPPC12-related encephalopathy**, **progressive encephalopathy with brain atrophy and spasticity (PEBAS)**, and **early-onset progressive encephalopathy–hearing loss–pons hypoplasia–brain atrophy syndrome**. MIM/OMIM association reported in the literature: **614139**. MONDO, Orphanet, ICD, MeSH: **not established from retrieved sources**. | MONDO: not established; HP: Neurodevelopmental abnormality [suggest HP:0012759] | (milev2017mutationsintrappc12 pages 1-2, yucesan2023functionalcharacterizationof pages 1-4, hall2024trappopathiesseveremultisystem pages 12-14) |
| Inheritance | **Autosomal recessive** / biallelic disease. Discovery cohort included one consanguineous family and one non-consanguineous family. | HP: Autosomal recessive inheritance (suggest HP:0000007) | (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3) |
| Gene and aliases | Causal gene: **TRAPPC12**. Reported aliases: **TTC15, TRAMM, CGI-87**. TRAPPC12 is a **TRAPPIII-specific subunit** involved in vesicle trafficking; it has **no yeast ortholog** in retrieved mechanistic studies. | HGNC gene symbol: TRAPPC12; GO CC suggestions: ER exit site, ER-Golgi intermediate compartment, Golgi apparatus | (zhao2017mammaliantrappiiicomplex pages 1-2, sacher2019trappopathiesanemerging pages 24-28, yucesan2023functionalcharacterizationof pages 1-4) |
| Established variants | Discovery cohort variants: **c.145delG (p.Glu49Argfs*14)** homozygous; **c.360dupC (p.Glu121Argfs*7)** and **c.1880C>T (p.Ala627Val)** compound heterozygous. Additional reported variant from later Turkish report/preprint: **c.679T>G (p.Phe227Val)** homozygous. 2024 review states ClinVar lists **21 pathogenic/likely pathogenic variants** including frameshift, nonsense, and splicing variants, but complete curated list was not extracted here. | SO terms suggested: frameshift_variant, missense_variant, splice_region_variant; HP: Homozygosity / Compound heterozygosity not typically HPO-coded | (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 3-5, yucesan2023functionalcharacterizationof pages 1-4, hall2024trappopathiesseveremultisystem pages 12-14) |
| Hallmark phenotypes and discovery-cohort frequencies | In the original 3-patient cohort: severe global developmental delay **3/3**, regression **3/3**, truncal hypotonia **3/3**, appendicular spasticity **3/3**, dystonia/myoclonus **3/3**, hearing loss/failed otoacoustic screening **3/3**, scoliosis **3/3**, dysphagia/reflux **3/3**, severe disability **3/3**; microcephaly **3/3** (acquired in 1, congenital in 2); epilepsy **2/3**; West syndrome **1/3**; optic pathway/visual abnormalities **3/3**; neurogenic bladder **1/3**. Later reports broaden phenotype to milder disease and fetal hydrocephalus/ventriculomegaly. | HP suggestions: Global developmental delay HP:0001263; Developmental regression HP:0002376; Hypotonia HP:0001252; Spasticity HP:0001257; Dystonia HP:0001332; Myoclonus HP:0001336; Sensorineural/mixed hearing impairment HP:0000407; Microcephaly HP:0000252; Seizure HP:0001250; West syndrome/Infantile spasms HP:0012469; Scoliosis HP:0002650; Dysphagia HP:0002015; Optic atrophy HP:0000648 | (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3, sacher2019trappopathiesanemerging pages 24-28, yucesan2023functionalcharacterizationof pages 1-4) |
| MRI / neuroimaging signature | Discovery cohort imaging signature: severe cortical/supratentorial atrophy **3/3**, ventriculomegaly **3/3**, prominent extra-axial spaces **3/3**, increased T2 cortical white matter signal **3/3**, severe pons hypoplasia **3/3**, agenesis or severe thinning of corpus callosum **3/3**, relatively spared basal ganglia **3/3**, mild cerebellar hypoplasia **2/3**, small optic chiasm **2/3**. One patient had progressive ventriculomegaly beyond expected cortical volume loss; later literature mentions severe hydrocephalus/hydrocephaly in some cases. | HP suggestions: Cerebral atrophy HP:0002059; Ventriculomegaly HP:0002119; Abnormal corpus callosum morphology / Agenesis HP:0001274 / HP:0001273; Pontine hypoplasia HP:0007366; Cerebellar hypoplasia HP:0001321; Delayed myelination / abnormal white matter signal HP:0012448 | (milev2017mutationsintrappc12 pages 3-5, milev2017mutationsintrappc12 pages 2-3, hall2024trappopathiesseveremultisystem pages 12-14) |
| Mechanism / pathophysiology | Best-supported mechanism is **loss of TRAPPC12 protein leading to Golgi fragmentation and delayed ER-to-Golgi trafficking**. Patient fibroblasts showed fragmented Golgi rescued by wild-type TRAPPC12; trafficking into and through the Golgi was delayed. Independent cell studies place TRAPPC12 at **ER exit sites and ERGIC**, where it promotes **Sec13/Sec31 COPII outer-coat recruitment**. Additional roles include **mitosis/kinetochore function** and **ciliogenesis via OFD1**, but the human encephalopathy phenotype is most directly linked to membrane-trafficking defects. | GO BP suggestions: vesicle-mediated transport, ER to Golgi vesicle-mediated transport, COPII-coated vesicle budding, protein localization to Golgi, ciliogenesis, mitotic chromosome congression; GO CC: ER exit site, ERGIC, Golgi apparatus, kinetochore, primary cilium | (milev2017mutationsintrappc12 pages 3-5, zhao2017mammaliantrappiiicomplex pages 1-2, sacher2019trappopathiesanemerging pages 24-28, zhang2020distinctrolesof pages 1-2) |
| Diagnostics | Diagnosis in published cases relied on **exome sequencing/WES** with segregation confirmation by **Sanger sequencing**. Supportive tests included **brain MRI**, **EEG** (hypsarrhythmia in the West syndrome case), newborn **otoacoustic emission hearing screening**, and clinical neurologic assessment. One case had extensive metabolic workup negative except **moderately elevated CSF lactate 3.2 mM**. No validated disease-specific biochemical biomarker is established. | NCIT/LOINC-style suggestions not established; HP: Hypsarrhythmia HP:0010849; Abnormal CSF lactate HP:0025435 | (milev2017mutationsintrappc12 pages 2-3, milev2017mutationsintrappc12 pages 1-2) |
| Treatment / management | **No disease-modifying therapy established.** Published management is supportive/symptom-directed: seizure management, feeding support including **G-tube dependence** in 2 patients, hearing evaluation, and multidisciplinary neurologic/rehabilitative care. No TRAPPC12-specific interventional clinical trials were identified. | NCIT suggestions: Supportive care; Gastrostomy; Anticonvulsant therapy; Physical therapy; Speech/feeding therapy | (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3) |
| Epidemiology / population | **Extremely rare**; only a small number of families/cases reported in the retrieved literature. No validated prevalence or incidence estimate. Discovery paper cites progressive childhood encephalopathy overall at **0.60 per 1,000 live births**, but that figure applies to the broad syndrome class, **not specifically to TRAPPC12-related disease**. No established founder effect, penetrance estimate, carrier frequency for the disease overall, sex ratio, or geographic distribution. Variant-specific population note: p.Phe227Val observed **2/237,118 gnomAD exome alleles** in heterozygous state in the 2023 preprint. | MONDO/epidemiology ontology: not established | (milev2017mutationsintrappc12 pages 1-2, yucesan2023functionalcharacterizationof pages 1-4) |
| Prognosis | Available data suggest **early-onset, progressive, high-morbidity encephalopathy** with severe long-term disability. In the discovery cohort, **1/3 died at 4 years 9 months** (presumed respiratory insufficiency). Later reports indicate phenotypic expansion to milder forms without epilepsy or without microcephaly in some cases, so prognosis appears variable but generally serious. Formal survival curves, life expectancy, and QoL studies are **not established**. | HP suggestions: Progressive neurologic deterioration HP:0002344; Respiratory insufficiency HP:0002093 | (milev2017mutationsintrappc12 pages 2-3, yucesan2023functionalcharacterizationof pages 1-4, hall2024trappopathiesseveremultisystem pages 12-14) |
| Evidence gaps | No confirmed MONDO/Orphanet/ICD identifier from retrieved sources; no disease-specific guidelines; no controlled treatment studies; no prevalence/incidence study; no penetrance/expressivity quantification; no established modifier genes; no epigenetic, transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial, iPSC, organoid, or animal disease model specific to TRAPPC12 retrieved here; no validated preventive intervention beyond genetic counseling/testing in at-risk families. | Suggested annotations: “not established” where identifier or evidence is unavailable | (hall2024trappopathiesseveremultisystem pages 12-14, yucesan2023functionalcharacterizationof pages 1-4, zhao2017mammaliantrappiiicomplex pages 1-2) |


*Table: This table provides a concise knowledge-base style summary of TRAPPC12-related encephalopathy, emphasizing established human genetic and clinical evidence while clearly marking identifiers and data elements that are not yet established.*

## Evidence scope and caution

The strongest human evidence is the 2017 discovery report describing three affected children from two unrelated families. Exact percentages below therefore largely use **n=3**, and should not be interpreted as stable population frequencies. Two 2020 reports broadened the phenotype; a February 9, 2023 preprint functionally studied one previously reported Turkish patient; and a December 2024 review summarized the TRAPPopathy literature and ClinVar landscape. The retrieved sources contain aggregated disease-level interpretation derived from individual cases and patient-derived cells—not EHR-scale evidence, registries, or population cohorts. (hall2024trappopathiesseveremultisystem pages 12-14, milev2017mutationsintrappc12 pages 1-2, yucesan2023functionalcharacterizationof pages 4-7)

---

## 1. Disease information

### Definition and current understanding

The disorder is a biallelic **TRAPPC12**-associated, early-onset progressive encephalopathy with severe neurodevelopmental impairment and structural brain abnormalities. The discovery paper defined progressive childhood encephalopathy as progressive CNS dysfunction with broad morbidity and mortality and concluded: **“Here, we report that variants in TRAPPC12 result in progressive childhood encephalopathy.”** It further observed that all three patient fibroblast lines had a fragmented Golgi and delayed transport from the ER to and through the Golgi. (milev2017mutationsintrappc12 pages 1-2)

### Names and identifiers

- **Preferred descriptive name:** TRAPPC12-related encephalopathy.
- **Published alternatives:** progressive childhood encephalopathy and Golgi dysfunction; progressive encephalopathy with brain atrophy and spasticity (**PEBAS**); early-onset progressive encephalopathy–hearing loss–pons hypoplasia–brain atrophy syndrome; TRAPPC12-related childhood encephalopathy.
- **OMIM/MIM:** **614139** is used in the retrieved literature for the TRAPPC12/PEBAS entry. The gene is also explicitly identified as TRAPPC12 (MIM 614139) in the discovery report. (milev2017mutationsintrappc12 pages 1-2, yucesan2023functionalcharacterizationof pages 1-4)
- **MONDO:** no confidently verified disease-specific MONDO identifier was retrieved; do not populate one without direct MONDO validation.
- **Orphanet, ICD-10, ICD-11, MeSH:** no disease-specific identifiers were established in the retrieved evidence. Broad codes for genetic encephalopathy, developmental disorder, epilepsy, microcephaly, or cerebral atrophy would be nonspecific and should not be represented as disease-equivalent identifiers.
- **Category:** Mendelian, autosomal recessive; part of the broader group termed **TRAPPopathies**. (sacher2019trappopathiesanemerging pages 24-28, hall2024trappopathiesseveremultisystem pages 12-14)

### Core publications

1. Milev et al., *American Journal of Human Genetics*, **August 3, 2017**, “Mutations in TRAPPC12 Manifest in Progressive Childhood Encephalopathy and Golgi Dysfunction,” DOI/URL: https://doi.org/10.1016/j.ajhg.2017.07.006. This is the landmark gene–disease report. (milev2017mutationsintrappc12 pages 1-2)
2. Aslanger et al., *Neuropediatrics* 51:430–434, **2020**, “Expanding Clinical Phenotype of TRAPPC12-Related Childhood Encephalopathy: Two Cases and Review of Literature,” DOI: https://doi.org/10.1055/s-0040-1710526. Bibliographic details are recorded in the 2023 report. (yucesan2023functionalcharacterizationof pages 7-11)
3. Gass et al., *Birth Defects Research* 112:1028–1034, **2020**, “Hydrocephaly associated with compound heterozygous alterations in TRAPPC12,” DOI: https://doi.org/10.1002/bdr2.1699. (yucesan2023functionalcharacterizationof pages 4-7, yucesan2023functionalcharacterizationof pages 7-11)
4. Yucesan et al., preprint posted **February 9, 2023**, DOI/URL: https://doi.org/10.21203/rs.3.rs-2552844/v1. (yucesan2023functionalcharacterizationof pages 1-4)
5. Hall et al., *International Journal of Molecular Sciences* 25:13329, **December 2024**, DOI/URL: https://doi.org/10.3390/ijms252413329. (hall2024trappopathiesseveremultisystem pages 12-14)

---

## 2. Etiology

### Causal factor

The primary cause is **germline biallelic pathogenic or likely pathogenic variation in TRAPPC12**. The discovery cohort demonstrated homozygous or compound-heterozygous segregation in affected children, absence or marked loss of full-length TRAPPC12 protein, cellular dysfunction, and rescue of Golgi morphology by wild-type TRAPPC12. Together, these data support a predominantly **loss-of-function/hypomorphic** mechanism rather than gain of function. (milev2017mutationsintrappc12 pages 5-8, milev2017mutationsintrappc12 pages 3-5)

### Genetic risk factors

Risk is determined principally by inheriting two deleterious alleles. Consanguinity increases the probability that both parents carry the same rare allele, but is not required: one discovery family was consanguineous and one was not. (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3)

### Environmental, infectious, and lifestyle risks

No TRAPPC12-specific toxin, infection, diet, lifestyle, occupation, age-related exposure, or other environmental cause has been demonstrated. General acquired causes of childhood encephalopathy—hypoxia, hemorrhage, and toxins—are differential etiologies rather than factors known to modify genetically confirmed TRAPPC12 disease. (milev2017mutationsintrappc12 pages 1-2)

### Protective factors, modifiers, and gene–environment interaction

No protective TRAPPC12 variants, modifier genes, environmental protective factors, or reproducible gene–environment interactions have been reported. No evidence shows that avoiding a particular exposure changes penetrance or progression.

---

## 3. Phenotypes

### Neurologic and developmental manifestations

In the original three-patient cohort, severe global developmental delay, regression, truncal hypotonia, appendicular spasticity, dystonia and/or myoclonus, microcephaly, and severe disability occurred in **3/3 (100%)**. Microcephaly was congenital in two and acquired in one. Epilepsy occurred in **2/3 (67%)**, while West syndrome with hypsarrhythmia occurred in **1/3 (33%)**. One patient presented with flexion seizures and loss of smiling/visual tracking at five months; the two sisters had congenital/prenatal abnormalities and made small developmental gains before plateauing. (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3)

Suggested HPO terms include:

- Global developmental delay — **HP:0001263**
- Developmental regression — **HP:0002376**
- Severe intellectual/developmental disability — **HP:0010864** where clinically confirmed
- Hypotonia — **HP:0001252**
- Spasticity — **HP:0001257**; spastic quadriplegia — **HP:0002510**
- Dystonia — **HP:0001332**
- Myoclonus — **HP:0001336**
- Seizure — **HP:0001250**
- Infantile spasms — **HP:0012469**
- Hypsarrhythmia — **HP:0010849**
- Microcephaly — **HP:0000252**

### Hearing, vision, feeding, and musculoskeletal manifestations

All three original patients failed otoacoustic-emission screening or had documented hearing impairment (**3/3**). Visual abnormalities occurred in **3/3**: optic atrophy, optic-nerve pallor, enlarged cup-to-disc ratio, or cortical visual impairment. Scoliosis and dysphagia/reflux occurred in **3/3**; two were gastrostomy-dependent. Other reported findings included neurogenic bladder (1/3), neonatal hypertension (1/3), vocal-cord paralysis (1/3), hip subluxation (1/3), and polyhydramnios (1/3). (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3)

Suggested HPO terms: hearing impairment **HP:0000365**, optic atrophy **HP:0000648**, cortical visual impairment **HP:0100704**, scoliosis **HP:0002650**, dysphagia **HP:0002015**, gastroesophageal reflux **HP:0002020**, neurogenic bladder **HP:0000011**, and hip subluxation **HP:0030043**.

### Neuroimaging

The original cohort showed a highly consistent MRI signature:

- Severe cortical atrophy: **3/3**
- Ventriculomegaly: **3/3**
- Prominent extra-axial spaces: **3/3**
- Simplified frontal gyri: **3/3**
- Increased T2 signal in cortical white matter: **3/3**
- Severe pons hypoplasia: **3/3**
- Agenesis or severe thinning of the corpus callosum: **3/3**
- Relative basal-ganglia sparing: **3/3**
- Mild cerebellar hypoplasia: **2/3**
- Small optic chiasm: **2/3**. (milev2017mutationsintrappc12 pages 3-5)

Documented volume loss between three days and 11 months in one child supports true progression, not merely congenital hypoplasia. A later child with p.Phe227Val had mild cortical but severe cerebellar atrophy, demonstrating broader radiologic expressivity. Compound-heterozygous fetal cases with ventriculomegaly/hydrocephaly, interhemispheric cysts, and polydactyly suggest a severe prenatal end of the spectrum, although the ciliogenesis connection remains mechanistically suggestive rather than proven in those fetuses. (milev2017mutationsintrappc12 pages 3-5, yucesan2023functionalcharacterizationof pages 4-7)

Suggested HPO terms: cerebral atrophy **HP:0002059**, ventriculomegaly **HP:0002119**, agenesis of corpus callosum **HP:0001273**, pontine hypoplasia **HP:0007366**, cerebellar hypoplasia **HP:0001321**, and abnormal cerebral white matter signal **HP:0030890**.

### Laboratory abnormalities

Extensive metabolic testing in the first patient was negative except moderately elevated CSF lactate, **3.2 mM** against a stated normal value below **2.1 mM**. This isolated result is neither sensitive nor specific and is not a validated disease biomarker. (milev2017mutationsintrappc12 pages 2-3)

### Quality-of-life effects

No EQ-5D, SF-36, PROMIS, caregiver-burden, or disease-specific quality-of-life study exists. Nevertheless, profound motor and developmental disability, absent or minimal psychomotor development, hearing/visual impairment, epilepsy, spastic quadriplegia, dysphagia requiring gastrostomy, and scoliosis imply major dependence in mobility, communication, feeding, and self-care. This is a clinical inference from functional manifestations, not a measured patient-reported outcome. (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3)

---

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** TRAPPC12, chromosome 2 in the hg19 coordinates reported by the discovery study.
- **Transcript used in the discovery report:** NM_016030.5; the 2023 report used NM_016030.6.
- **Protein aliases:** trafficking protein particle complex subunit 12; **TTC15**, **TRAMM** (“trafficking of membranes and mitosis”), and **CGI-87**.
- **Gene MIM identifier:** 614139 in the retrieved sources.
- **HGNC ID:** not independently verified in the retrieved material and should be added only after direct HGNC validation.
- **Complex:** metazoan TRAPPIII; TRAPPC12 has no yeast ortholog. (sacher2019trappopathiesanemerging pages 24-28, zhao2017mammaliantrappiiicomplex pages 1-2)

### Reported disease variants

1. **NM_016030.5:c.145delG; p.Glu49Argfs*14**, homozygous. It was absent from 49,094 ExAC individuals and an 850-exome Muslim-Arab internal database at the time of publication. Both parents were heterozygous. (milev2017mutationsintrappc12 pages 2-3)
2. **c.360dupC; p.Glu121Argfs*7** plus **c.1880C>T; p.Ala627Val**, compound heterozygous in two sisters. The father carried the frameshift and mother the missense allele. In the discovery-era gnomAD data, p.Ala627Val occurred twice among 246,176 alleles; no affected homozygote was reported. (milev2017mutationsintrappc12 pages 3-5)
3. **NM_016030.6:c.679T>G; p.Phe227Val**, rs1312522735, homozygous in a Turkish patient; both parents were obligate carriers. It appeared in **2/237,118 gnomAD exome alleles**, allele frequency approximately **8.43×10⁻⁶**, with no homozygote. In-silico evidence was conflicting—13 tools predicted pathogenicity and 11 benignity—but patient-cell protein loss and organelle abnormalities supplied functional evidence. (yucesan2023functionalcharacterizationof pages 4-7, yucesan2023functionalcharacterizationof pages 1-4)
4. A 2024 review reported **21 ClinVar pathogenic/likely pathogenic variants**, including frameshift, nonsense, and splicing alleles. This is a database count, not 21 clinically independent patients, and should be refreshed directly from ClinVar before production use. (hall2024trappopathiesseveremultisystem pages 12-14)

All reported disease alleles are germline. No somatic TRAPPC12 encephalopathy has been described. No large recurrent deletion, translocation, inversion, aneuploidy, repeat expansion, or mitochondrial lesion is established as the cause.

### Functional consequences

Full-length TRAPPC12 was absent in all three discovery-cohort fibroblast lines, including cells carrying p.Ala627Val in trans with a frameshift. The alanine lies at position 8 of the third tetratricopeptide-repeat domain, where substitution by bulky valine was predicted to destabilize protein structure. Proteasome inhibition did not restore detectable protein in those cells. For p.Phe227Val, two antibodies also showed absent or extremely low TRAPPC12 and loss of the approximately 35-kDa CGI-87 product. (milev2017mutationsintrappc12 pages 5-8, yucesan2023functionalcharacterizationof pages 4-7)

The most appropriate molecular classification is therefore **loss of protein/function**, with possible residual activity in some missense genotypes. No dominant-negative or gain-of-function mechanism has been demonstrated.

### Modifier and epigenetic information

No validated modifier gene, DNA-methylation signature, histone modification, chromatin alteration, or disease-specific epigenomic profile is available.

---

## 5. Environmental information

No environmental toxin, radiation exposure, pollution source, occupational exposure, smoking, alcohol, diet, exercise pattern, or infectious agent is known to cause or trigger TRAPPC12-related encephalopathy. The disease is not infectious or zoonotic. Environmental management may reduce secondary complications—such as aspiration or respiratory infection—but does not prevent the inherited molecular defect.

---

## 6. Mechanism and pathophysiology

### Best-supported causal chain

**Biallelic deleterious TRAPPC12 variants → absent/unstable TRAPPC12 protein → impaired TRAPPIII/COPII interface and ER-exit-site function → defective Sec13/Sec31 outer-coat recruitment, dispersed ERGIC/Golgi, and delayed ER-to-Golgi and intra-/post-Golgi cargo transit → disturbed delivery and homeostasis of membrane/secreted proteins in highly polarized, trafficking-dependent neural cells → abnormal brain development plus progressive neuronal dysfunction/atrophy → developmental regression, spasticity, movement disorder, sensory impairment, and epilepsy.**

The upstream steps through trafficking delay are experimentally demonstrated. The neuron-specific link from cargo-trafficking failure to regional brain atrophy remains a strong biologic inference, because no patient-neuron or animal model has yet traced that full chain. (milev2017mutationsintrappc12 pages 3-5, zhao2017mammaliantrappiiicomplex pages 1-2)

### ER-to-Golgi trafficking and COPII biology

TRAPPC12 localizes to ER exit sites and the ER–Golgi intermediate compartment. It binds the assembled Sec13/Sec31A tetramer—not either protein alone—and promotes recruitment of the COPII outer coat. TRAPPC12-null HeLa/HEK293T systems showed dispersed ERGIC/Golgi and delayed transport of VSV-G and other cargo. The primary mechanistic abstract states: **“TRAPPIII positively modulated the assembly of COPII outer layer during COPII vesicle formation.”** (zhao2017mammaliantrappiiicomplex pages 1-2, zhao2017mammaliantrappiiicomplex pages 8-9)

In patient fibroblasts, the Golgi was fragmented, arrival of VSVG-GFP and RUSH cargo at the Golgi was delayed, and VSVG remained in the Golgi longer. Expression of wild-type TRAPPC12 restored a compact, ribbon-like Golgi, providing a direct rescue experiment linking genotype to organelle phenotype. (milev2017mutationsintrappc12 pages 5-8, milev2017mutationsintrappc12 pages 3-5)

Suggested GO annotations include ER-to-Golgi vesicle-mediated transport **GO:0006888**, vesicle-mediated transport **GO:0016192**, COPII-coated vesicle budding **GO:0090114**, Golgi organization **GO:0007030**, ER exit site, ERGIC, and Golgi apparatus **GO:0005794**.

### TRAPPIII and Rab signaling

Mammalian TRAPPIII is a guanine-nucleotide-exchange complex with Rab1 specificity; Rab1 regulates early secretory trafficking and autophagy. Structural work places TRAPPC12/TRAPPC13 on one peripheral arm of metazoan TRAPPIII, while Rab1 engages the complex elsewhere. TRAPPC12 should therefore be regarded as a complex subunit facilitating architecture/localization rather than a stand-alone enzyme. (yucesan2023functionalcharacterizationof pages 4-7, yucesan2023functionalcharacterizationof pages 1-4)

### Mitosis

TRAPPC12/TRAMM also localizes to chromosomes and kinetochores during mitosis and supports kinetochore stability, CENP-E recruitment, chromosome congression, and spindle-checkpoint progression. Patient fibroblasts showed increased prophase-to-anaphase time. However, experts have judged trafficking dysfunction more likely than mitotic delay to account for the principal neurologic phenotype; direct developmental proof is lacking. (sacher2019trappopathiesanemerging pages 24-28, milev2017mutationsintrappc12 pages 5-8)

Suggested GO terms: chromosome congression **GO:0051310**, kinetochore organization **GO:0051383**, mitotic spindle-assembly checkpoint **GO:0007094**, and kinetochore **GO:0000776**.

### Autophagy

TRAPPIII participates in autophagy and Rab1/ATG9-related membrane traffic. TRAPPC12 depletion has been associated experimentally with altered autophagosome abundance/flux, but disease-specific autophagic failure has not been demonstrated in patient neural tissue. Autophagy should therefore be annotated as a plausible associated process, not the established proximal cause of encephalopathy. (zhao2017mammaliantrappiiicomplex pages 1-2)

Suggested GO term: macroautophagy **GO:0016236**.

### Ciliogenesis

TRAPPC12 interacts with OFD1. In hTERT-RPE1 cells, depletion increased primary-cilium length because TRAPPC12 was required for ciliary disassembly. This provides a plausible mechanistic context for fetal hydrocephalus, polydactyly, and interhemispheric cysts, but no direct rescue or causal demonstration has connected altered ciliary length to human TRAPPC12 brain disease. (zhang2020distinctrolesof pages 1-2, yucesan2023functionalcharacterizationof pages 4-7)

Suggested GO terms: cilium assembly **GO:0060271**, cilium disassembly **GO:0061512**, primary cilium **GO:0072372**, and centriolar satellite **GO:0034451**.

### Molecular profiling and advanced technologies

No disease-specific transcriptomics, quantitative proteomics, metabolomics, lipidomics, single-cell analysis, spatial transcriptomics, multi-omics integration, patient iPSC-neuron study, cerebral organoid, or genome-wide CRISPR screen was retrieved. Nile-red imaging showed altered neutral-lipid-droplet distribution in p.Phe227Val fibroblasts, but this is an imaging phenotype—not a validated lipidomic signature. (yucesan2023functionalcharacterizationof pages 4-7)

---

## 7. Anatomical structures affected

### Organ and system level

The **central nervous system** is primary. Structures repeatedly affected include cerebral cortex and subcortical white matter, corpus callosum, pons, optic nerves/chiasm, and—variably—cerebellum. The cochlear/auditory system, visual system, bulbar feeding pathways, spinal/upper-motor-neuron system, and musculoskeletal system are clinically involved. Secondary complications include scoliosis, hip subluxation, neurogenic bladder, dysphagia/reflux, and respiratory insufficiency. (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 3-5)

Suggested UBERON terms: brain **UBERON:0000955**, cerebral cortex **UBERON:0000956**, corpus callosum **UBERON:0002336**, pons **UBERON:0000988**, cerebellum **UBERON:0002037**, optic nerve **UBERON:0000962**, and spinal cord **UBERON:0002240**.

### Tissue and cell level

No histopathologic patient-brain or single-cell study identifies one selectively vulnerable cell population. Neurons are biologically plausible primary targets because of their polarization and exceptional dependence on membrane trafficking, with oligodendrocytes potentially implicated by reduced myelination/white-matter signal. These remain inferred cell types rather than experimentally confirmed targets.

Suggested CL terms for hypothesis-driven annotation: neuron **CL:0000540**, cortical neuron **CL:0002609**, motor neuron **CL:0000100**, oligodendrocyte **CL:0000128**, and neural progenitor cell **CL:0011020**.

### Subcellular structures

Experimentally involved compartments are the ER, ER exit sites, COPII vesicles, ERGIC, Golgi apparatus, cytoplasmic vesicles/lipid droplets, kinetochores, centriolar satellites, and primary cilia. No lateralization pattern is established; imaging abnormalities are generally bilateral/diffuse. (zhang2020distinctrolesof pages 1-2, milev2017mutationsintrappc12 pages 3-5, zhao2017mammaliantrappiiicomplex pages 1-2, yucesan2023functionalcharacterizationof pages 4-7)

---

## 8. Temporal development

Onset is prenatal, neonatal, or early infantile. Examples include prenatal corpus-callosum agenesis, neonatal jitteriness or hearing-screen failure, and infantile spasms/regression at five months. The course is chronic and usually progressive: initial limited gains may plateau, followed by worsening atrophy, spasticity, seizures, feeding impairment, and severe lifelong disability. No standardized stages have been developed. (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3)

There is no evidence of spontaneous remission. Seizures may be controlled symptomatically in individual patients, but no publication demonstrates reversal of the underlying encephalopathy. Prenatal brain development and the first year—when cortical volume loss was documented—are likely critical vulnerability periods. This timing is observational, not evidence for a proven therapeutic window. (milev2017mutationsintrappc12 pages 3-5)

---

## 9. Inheritance and population

### Inheritance

Inheritance is **autosomal recessive**. For two confirmed carrier parents, standard Mendelian counseling assigns each pregnancy a 25% affected, 50% carrier, and 25% non-carrier probability, assuming both parental variants are fully pathogenic and no unusual mosaicism. Both sexes are affected. (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3)

Penetrance appears high for clearly damaging biallelic genotypes in the few reported families, but formal penetrance cannot be estimated. Expressivity is variable: severe congenital disease, progressive infantile PEBAS, and milder disease without epilepsy or microcephaly have been described. No anticipation, germline mosaicism, or established founder effect has been reported. (hall2024trappopathiesseveremultisystem pages 12-14, yucesan2023functionalcharacterizationof pages 1-4)

### Epidemiology

No disease-specific prevalence, incidence, carrier frequency, geographic distribution, or sex-ratio estimate exists. The discovery paper’s figure of **0.60 per 1,000 live births** concerns progressive childhood encephalopathy overall and must not be attributed to TRAPPC12-related disease. (milev2017mutationsintrappc12 pages 1-2)

Reported families include Palestinian and mixed European/Native American backgrounds, as well as Turkish cases. These observations do not establish ethnic enrichment. Consanguinity aided identification in one family, but compound heterozygosity in an unrelated non-consanguineous family demonstrates that consanguinity is not necessary. (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3, yucesan2023functionalcharacterizationof pages 4-7)

---

## 10. Diagnostics

### Clinical suspicion

Consider TRAPPC12 testing in a child or fetus with combinations of severe developmental delay/regression, microcephaly, hearing loss, hypotonia plus appendicular spasticity/dystonia, seizures, dysphagia, and MRI evidence of cortical atrophy, pons hypoplasia, corpus-callosum agenesis/hypoplasia, or unexplained hydrocephalus. The discovery authors specifically recommended evaluation in sequencing data for neonatal encephalopathy, hearing loss, pontocerebellar hypoplasia, and brain-atrophy disorders. (milev2017mutationsintrappc12 pages 5-8)

### Recommended evaluation

1. **Brain MRI**, including assessment of cortical volume, myelination/white-matter signal, corpus callosum, pons, cerebellum, ventricles, optic chiasm, and interval progression.
2. **EEG** for seizures or regression; hypsarrhythmia supports infantile spasms but is not disease-specific.
3. **Formal audiology**, even after failed neonatal otoacoustic-emission screening.
4. Ophthalmology/neuro-ophthalmology for optic atrophy and cortical visual impairment.
5. Swallowing and nutritional evaluation; respiratory, orthopedic, rehabilitation, and bladder assessments according to symptoms.
6. Routine biochemical/metabolic testing to exclude treatable mimics; no TRAPPC12-specific enzyme or metabolite assay exists. (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3)

### Genetic testing strategy

- **First-line:** trio WES or WGS for an unexplained complex encephalopathy, or a comprehensive neurodevelopmental/epilepsy/brain-atrophy/pontocerebellar-hypoplasia panel that includes TRAPPC12.
- Confirm candidate variants and phase/segregation by parental testing; Sanger confirmation was used in the foundational study.
- Ensure analysis detects single-nucleotide variants, small indels, splice variants, and exon-level copy-number changes. WGS may improve detection of noncoding splice, structural, or poorly covered variants, although no comparative TRAPPC12 WGS-yield study exists.
- If only one pathogenic allele is found, pursue deletion/duplication analysis, genome sequencing, and—where available—RNA studies.
- CMA may identify broad chromosomal causes in the differential but is not sufficient to exclude biallelic sequence-level TRAPPC12 disease. Karyotyping, FISH, mtDNA testing, and repeat-expansion assays are not specifically indicated unless the phenotype or initial results suggest an alternative diagnosis.
- Protein immunoblotting and fibroblast Golgi/trafficking assays remain research-level functional tests, not validated clinical diagnostics. (milev2017mutationsintrappc12 pages 3-5, milev2017mutationsintrappc12 pages 2-3, yucesan2023functionalcharacterizationof pages 4-7)

### Differential diagnosis

The differential includes congenital infection or hypoxic-ischemic injury; mitochondrial and metabolic encephalopathies; pontocerebellar hypoplasias; tubulinopathies; congenital disorders of glycosylation; hereditary spasticity/brain-atrophy syndromes; and other TRAPPopathies involving TRAPPC4, TRAPPC6B, TRAPPC9, TRAPPC10, TRAPPC11, or TRAPPC2L. The combination of hearing loss, pons hypoplasia, callosal agenesis, and prominent supratentorial atrophy is especially suggestive but not pathognomonic. (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 5-8)

### Screening

TRAPPC12 is not part of established biochemical newborn screening, and there is no validated dried-blood-spot biomarker or population DNA-screening program. Targeted cascade testing is appropriate for relatives of a molecularly confirmed proband. Carrier, prenatal, and preimplantation testing become technically feasible after familial variants are established.

---

## 11. Outcome and prognosis

The disorder generally carries high neurologic morbidity. In the three-patient discovery cohort, all had severe disability and regression; two required gastrostomy, and one developed neurogenic bladder. One of three died at **4 years 9 months**, reportedly from presumed respiratory insufficiency. This single death cannot provide a mortality rate or life-expectancy estimate. (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3)

Later cases demonstrate variable severity, including survival to nine years with milder cortical atrophy and absence of epilepsy or microcephaly. Genotypes causing complete protein loss or early truncation may plausibly be more severe, but the patient count is too small for a validated genotype–prognosis rule. No five- or ten-year survival statistics, prognostic model, validated prognostic biomarker, recovery-rate study, or formal quality-of-life dataset exists. (yucesan2023functionalcharacterizationof pages 4-7, yucesan2023functionalcharacterizationof pages 1-4)

Potential complications include refractory epilepsy, aspiration and malnutrition, contractures and scoliosis, hip instability, respiratory insufficiency, visual/hearing disability, and total dependence for daily activities. Recovery of lost developmental function has not been documented; supportive interventions may preserve comfort, positioning, communication, nutrition, and prevent secondary complications.

---

## 12. Treatment

### Current practice

There is **no approved or evidence-based disease-modifying treatment**. Management is individualized and supportive:

- Standard antiseizure therapy selected by seizure type; infantile spasms require urgent specialist treatment according to general pediatric epilepsy standards.
- Gastroesophageal-reflux, swallowing, nutrition, and aspiration management; enteral feeding/gastrostomy when oral feeding is unsafe or inadequate.
- Physical and occupational therapy, positioning, stretching, orthotics, tone/spasticity management, and orthopedic surveillance.
- Speech/communication therapy and augmentative communication.
- Hearing aids or other audiologic intervention when appropriate; low-vision/cortical-visual-impairment services.
- Respiratory monitoring, airway clearance, vaccination, and infection management; sleep and secretion assessment where indicated.
- Palliative-care involvement for severe progressive disease and shared decision-making.

Gastrostomy dependence in two original patients documents real-world feeding support, but no study reports comparative response rates or adverse-event frequencies. (milev2017mutationsintrappc12 pages 1-2, milev2017mutationsintrappc12 pages 2-3)

Suggested NCIT intervention concepts include **Supportive Care**, **Anticonvulsant Therapy**, **Gastrostomy**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Hearing Aid**, **Orthopedic Procedure**, and **Palliative Care**; exact NCIT codes should be verified directly before database import.

### Advanced and experimental therapies

No TRAPPC12-specific gene-replacement, gene-editing, cell, antisense, siRNA, mRNA, small-molecule, targeted, or immunotherapy has entered clinical evaluation. No relevant interventional ClinicalTrials.gov study was identified. The successful rescue of patient-cell Golgi morphology by wild-type TRAPPC12 supplies proof of biological reversibility at the cellular level, but it is not preclinical evidence of CNS delivery, developmental rescue, safety, or patient benefit. (milev2017mutationsintrappc12 pages 5-8)

No TRAPPC12-specific pharmacogenomic guidance or treatment algorithm exists.

---

## 13. Prevention

Primary lifestyle or environmental prevention is not applicable to an inherited biallelic disorder. The principal preventive strategy is **genetic counseling**:

- Confirm both familial variants and parental phase.
- Offer targeted carrier testing to at-risk adult relatives.
- Discuss prenatal diagnosis by chorionic-villus sampling or amniocentesis and preimplantation genetic testing for monogenic disease where legally and locally available.
- Use targeted fetal imaging, while recognizing that a normal early scan cannot exclude later progressive disease.

Secondary prevention consists of early molecular diagnosis, hearing/vision assessment, seizure surveillance, feeding evaluation, and developmental intervention. Tertiary prevention targets aspiration, malnutrition, respiratory infection, contractures, scoliosis, pressure injury, and caregiver burden. No vaccine, prophylactic medication, public-health intervention, or behavioral modification prevents TRAPPC12 disease itself.

---

## 14. Other species and natural disease

No naturally occurring TRAPPC12-related encephalopathy was identified in companion animals, livestock, or wildlife, and no breed association or VBO identifier is established. TRAPPC12 is metazoan-specific in the reviewed cell-biology literature and has **no yeast ortholog**, limiting direct yeast disease modeling. (zhao2017mammaliantrappiiicomplex pages 1-2)

No zoonotic or cross-species transmission is relevant because this is a germline genetic disorder. Ortholog-specific NCBI Gene and NCBI Taxonomy identifiers were not established in the retrieved evidence and should be sourced directly before annotation.

---

## 15. Model organisms and experimental systems

### Patient-derived human cells

Primary skin fibroblasts from all three discovery patients are the most disease-relevant models. They reproduced absent TRAPPC12 protein, fragmented Golgi, delayed ER-to-Golgi and through-Golgi trafficking, and mitotic delay; wild-type TRAPPC12 rescued Golgi morphology. Fibroblasts from the p.Phe227Val patient showed absent protein, disrupted Golgi integrity, enlarged ER-associated cell architecture, and altered neutral-lipid-vesicle distribution. These systems directly model patient genotype but cannot reproduce neuronal circuitry, developmental timing, brain regional selectivity, seizures, or behavior. (milev2017mutationsintrappc12 pages 5-8, milev2017mutationsintrappc12 pages 3-5, yucesan2023functionalcharacterizationof pages 4-7)

### Engineered cell models

- **HeLa and HEK293T CRISPR-knockout cells:** used to assess COPII assembly, Sec13/Sec31 recruitment, ERGIC/Golgi organization, and secretory trafficking. They establish molecular mechanism but are transformed/non-neural cells. (zhao2017mammaliantrappiiicomplex pages 10-11, zhao2017mammaliantrappiiicomplex pages 8-9)
- **HeLa RNAi/depletion models:** demonstrated Golgi fragmentation, chromosome-congression failure, kinetochore defects, and altered CENP-E recruitment. (sacher2019trappopathiesanemerging pages 24-28)
- **hTERT-RPE1 cells:** demonstrated TRAPPC12–OFD1 interaction and increased ciliary length/impaired disassembly after depletion. This is useful for ciliogenesis but does not establish that ciliary dysfunction causes encephalopathy. (zhang2020distinctrolesof pages 1-2)
- **CCD1079Sk control fibroblasts:** used against p.Phe227Val patient fibroblasts in the 2023 functional report. (yucesan2023functionalcharacterizationof pages 1-4)

No TRAPPC12-specific mouse, rat, zebrafish, Drosophila, *C. elegans*, iPSC-neuron, cerebral-organoid, conditional knockout, knock-in, or humanized disease model was retrieved. Mouse and other animal phenotypes reported for **TRAPPC10** or other TRAPP genes must not be attributed to TRAPPC12.

---

## Recent developments and expert assessment

The key 2023 development was functional analysis of homozygous p.Phe227Val, showing that a nontruncating variant could nevertheless produce nearly absent protein and marked Golgi/ER abnormalities while causing a clinically milder phenotype. Its abstract reports: **“Protein expression showed an absence in the TRAPPC12 protein and an uncharacterized protein fragment (CGI-87).”** Because this was a preprint in the retrieved record, conclusions should be weighted below peer-reviewed primary studies until final publication is verified. (yucesan2023functionalcharacterizationof pages 4-7, yucesan2023functionalcharacterizationof pages 1-4)

The December 2024 review characterized TRAPPC12 disease as a spectrum of neurological symptoms and noted 21 ClinVar pathogenic/likely pathogenic variants. Its central expert conclusion is that, beyond membrane-trafficking defects in fibroblasts, the pathophysiology remains poorly understood. This appropriately defines the current field: gene–disease validity and ER–Golgi dysfunction are convincing, while selective neural vulnerability, genotype–phenotype relationships, natural history, biomarkers, and therapeutic tractability remain unresolved. (hall2024trappopathiesseveremultisystem pages 12-14)

## Knowledge-base conclusions

1. **High-confidence:** biallelic TRAPPC12 variants cause an autosomal-recessive encephalopathy; loss of protein, Golgi fragmentation, and delayed ER-to-Golgi trafficking are experimentally established.
2. **Moderate-confidence:** the core phenotype includes severe developmental impairment/regression, microcephaly, hypotonia/spasticity, movement disorder, hearing impairment, and a pons–callosum–cortical-atrophy MRI signature.
3. **Variable features:** epilepsy, West syndrome, cerebellar atrophy, hydrocephalus, and microcephaly are not obligatory across later cases.
4. **Mechanistically plausible but not proven as the clinical driver:** altered mitosis, autophagy, and ciliogenesis.
5. **Not established:** disease-specific prevalence, penetrance, founder alleles, modifier genes, biomarkers, natural-history stages, formal QoL or survival estimates, animal disease models, guidelines, clinical trials, and disease-modifying therapy.

For production curation, ClinVar, HGNC, MONDO, HPO, GO, UBERON, CL, NCIT, and current OMIM records should be re-queried directly to validate live identifiers and variant classifications; database counts and classifications can change after the publication dates represented here.

References

1. (hall2024trappopathiesseveremultisystem pages 12-14): Riley Hall, Vallari Sawant, Jinchao Gu, Tim Sikora, Ben Rollo, Silvia Velasco, Jinkuk Kim, Nava Segev, John Christodoulou, and Nicole J. Van Bergen. Trappopathies: severe multisystem disorders caused by variants in genes of the transport protein particle (trapp) complexes. International Journal of Molecular Sciences, 25:13329, Dec 2024. URL: https://doi.org/10.3390/ijms252413329, doi:10.3390/ijms252413329. This article has 8 citations.

2. (milev2017mutationsintrappc12 pages 1-2): Miroslav P. Milev, Megan E. Grout, Djenann Saint-Dic, Yong-Han Hank Cheng, Ian A. Glass, Christopher J. Hale, David S. Hanna, Michael O. Dorschner, Keshika Prematilake, Avraham Shaag, Orly Elpeleg, Michael Sacher, Dan Doherty, and Simon Edvardson. Mutations in trappc12 manifest in progressive childhood encephalopathy and golgi dysfunction. American journal of human genetics, 101 2:291-299, Aug 2017. URL: https://doi.org/10.1016/j.ajhg.2017.07.006, doi:10.1016/j.ajhg.2017.07.006. This article has 61 citations and is from a highest quality peer-reviewed journal.

3. (yucesan2023functionalcharacterizationof pages 1-4): Emrah Yucesan, Beyza Goncu, Gozde Yesil, and Ayca Dilruba Aslanger. Functional characterization of a missense mutation in the trappc12 gene presenting with progressive encephalopathy with brain atrophy and spasticity phenotype without microcephaly and epilepsy. Unknown journal, Feb 2023. URL: https://doi.org/10.21203/rs.3.rs-2552844/v1, doi:10.21203/rs.3.rs-2552844/v1.

4. (milev2017mutationsintrappc12 pages 2-3): Miroslav P. Milev, Megan E. Grout, Djenann Saint-Dic, Yong-Han Hank Cheng, Ian A. Glass, Christopher J. Hale, David S. Hanna, Michael O. Dorschner, Keshika Prematilake, Avraham Shaag, Orly Elpeleg, Michael Sacher, Dan Doherty, and Simon Edvardson. Mutations in trappc12 manifest in progressive childhood encephalopathy and golgi dysfunction. American journal of human genetics, 101 2:291-299, Aug 2017. URL: https://doi.org/10.1016/j.ajhg.2017.07.006, doi:10.1016/j.ajhg.2017.07.006. This article has 61 citations and is from a highest quality peer-reviewed journal.

5. (zhao2017mammaliantrappiiicomplex pages 1-2): Shan Zhao, Chun Man Li, Xiao Min Luo, Gavin Ka Yu Siu, Wen Jia Gan, Lin Zhang, William K. K. Wu, Hsiao Chang Chan, and Sidney Yu. Mammalian trappiii complex positively modulates the recruitment of sec13/31 onto copii vesicles. Scientific Reports, Feb 2017. URL: https://doi.org/10.1038/srep43207, doi:10.1038/srep43207. This article has 44 citations and is from a peer-reviewed journal.

6. (sacher2019trappopathiesanemerging pages 24-28): Michael Sacher, Nassim Shahrzad, Hiba Kamel, and Miroslav P. Milev. Trappopathies: an emerging set of disorders linked to variations in the genes encoding transport protein particle (trapp)‐associated proteins. Traffic, 20:26-5, Sep 2019. URL: https://doi.org/10.1111/tra.12615, doi:10.1111/tra.12615. This article has 106 citations and is from a peer-reviewed journal.

7. (milev2017mutationsintrappc12 pages 3-5): Miroslav P. Milev, Megan E. Grout, Djenann Saint-Dic, Yong-Han Hank Cheng, Ian A. Glass, Christopher J. Hale, David S. Hanna, Michael O. Dorschner, Keshika Prematilake, Avraham Shaag, Orly Elpeleg, Michael Sacher, Dan Doherty, and Simon Edvardson. Mutations in trappc12 manifest in progressive childhood encephalopathy and golgi dysfunction. American journal of human genetics, 101 2:291-299, Aug 2017. URL: https://doi.org/10.1016/j.ajhg.2017.07.006, doi:10.1016/j.ajhg.2017.07.006. This article has 61 citations and is from a highest quality peer-reviewed journal.

8. (zhang2020distinctrolesof pages 1-2): Caiyun Zhang, Chunman Li, Gavin Ka Yu Siu, Xiaomin Luo, and Sidney Yu. Distinct roles of trappc8 and trappc12 in ciliogenesis via their interactions with ofd1. Frontiers in Cell and Developmental Biology, Mar 2020. URL: https://doi.org/10.3389/fcell.2020.00148, doi:10.3389/fcell.2020.00148. This article has 15 citations.

9. (yucesan2023functionalcharacterizationof pages 4-7): Emrah Yucesan, Beyza Goncu, Gozde Yesil, and Ayca Dilruba Aslanger. Functional characterization of a missense mutation in the trappc12 gene presenting with progressive encephalopathy with brain atrophy and spasticity phenotype without microcephaly and epilepsy. Unknown journal, Feb 2023. URL: https://doi.org/10.21203/rs.3.rs-2552844/v1, doi:10.21203/rs.3.rs-2552844/v1.

10. (yucesan2023functionalcharacterizationof pages 7-11): Emrah Yucesan, Beyza Goncu, Gozde Yesil, and Ayca Dilruba Aslanger. Functional characterization of a missense mutation in the trappc12 gene presenting with progressive encephalopathy with brain atrophy and spasticity phenotype without microcephaly and epilepsy. Unknown journal, Feb 2023. URL: https://doi.org/10.21203/rs.3.rs-2552844/v1, doi:10.21203/rs.3.rs-2552844/v1.

11. (milev2017mutationsintrappc12 pages 5-8): Miroslav P. Milev, Megan E. Grout, Djenann Saint-Dic, Yong-Han Hank Cheng, Ian A. Glass, Christopher J. Hale, David S. Hanna, Michael O. Dorschner, Keshika Prematilake, Avraham Shaag, Orly Elpeleg, Michael Sacher, Dan Doherty, and Simon Edvardson. Mutations in trappc12 manifest in progressive childhood encephalopathy and golgi dysfunction. American journal of human genetics, 101 2:291-299, Aug 2017. URL: https://doi.org/10.1016/j.ajhg.2017.07.006, doi:10.1016/j.ajhg.2017.07.006. This article has 61 citations and is from a highest quality peer-reviewed journal.

12. (zhao2017mammaliantrappiiicomplex pages 8-9): Shan Zhao, Chun Man Li, Xiao Min Luo, Gavin Ka Yu Siu, Wen Jia Gan, Lin Zhang, William K. K. Wu, Hsiao Chang Chan, and Sidney Yu. Mammalian trappiii complex positively modulates the recruitment of sec13/31 onto copii vesicles. Scientific Reports, Feb 2017. URL: https://doi.org/10.1038/srep43207, doi:10.1038/srep43207. This article has 44 citations and is from a peer-reviewed journal.

13. (zhao2017mammaliantrappiiicomplex pages 10-11): Shan Zhao, Chun Man Li, Xiao Min Luo, Gavin Ka Yu Siu, Wen Jia Gan, Lin Zhang, William K. K. Wu, Hsiao Chang Chan, and Sidney Yu. Mammalian trappiii complex positively modulates the recruitment of sec13/31 onto copii vesicles. Scientific Reports, Feb 2017. URL: https://doi.org/10.1038/srep43207, doi:10.1038/srep43207. This article has 44 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](TRAPPC12-Related_Encephalopathy-deep-research-falcon_artifacts/artifact-00.md)