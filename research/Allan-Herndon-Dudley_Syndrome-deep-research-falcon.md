---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T17:47:49.851786'
end_time: '2026-07-31T17:55:59.643036'
duration_seconds: 489.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Allan-Herndon-Dudley Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Allan-Herndon-Dudley_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Allan-Herndon-Dudley Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Allan-Herndon-Dudley Syndrome** covering all of the
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
- **Disease Name:** Allan-Herndon-Dudley Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Allan-Herndon-Dudley Syndrome** covering all of the
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


# Allan–Herndon–Dudley Syndrome (MCT8 Deficiency): Comprehensive Disease-Characteristics Report

**Scope and evidence cutoff.** This report emphasizes authoritative guidance and literature available through 2024, supplemented by current ClinicalTrials.gov records retrieved for this review. Evidence labels distinguish human cohorts, guidelines, trials, postmortem studies, animal models, and in-vitro systems. Because AHDS is ultra-rare, many management recommendations rest on observational cohorts, uncontrolled trials, and expert consensus rather than randomized outcome trials.

## Executive summary

Allan–Herndon–Dudley syndrome (AHDS), increasingly termed **monocarboxylate transporter 8 deficiency (MCT8 deficiency)**, is an X-linked Mendelian neurodevelopmental and endocrine disorder caused by pathogenic loss-of-function variants in **SLC16A2**. Defective MCT8 prevents adequate thyroid-hormone transport across brain barriers and into selected neural cells, producing severe developmental cerebral hypothyroidism. At the same time, elevated circulating T3 produces peripheral thyrotoxicosis, malnutrition, muscle wasting, and cardiovascular abnormalities. The characteristic biochemical pattern is high T3, low or low-normal T4, low reverse T3, and normal or mildly elevated TSH. (grijotamartinez2020mct8deficiencythe pages 1-2, persani20242024europeanthyroid pages 5-6)

The largest natural-history data indicate profound motor and cognitive disability, frequent dysphagia and underweight, and median survival of approximately 35 years. Early underweight and failure to acquire head control predict higher childhood mortality. Tiratricol/TRIAC is the most advanced targeted treatment and is strongly recommended in the 2024 European Thyroid Association (ETA) guideline to control peripheral thyrotoxicosis; however, no human regimen has yet definitively rescued the neurocognitive phenotype. The critical therapeutic window probably begins prenatally and declines during the first three years. (geest2021monocarboxylatetransporter8 pages 6-7, persani20242024europeanthyroid pages 13-14, bauer2024unmetpatientneeds pages 6-7)

A compact, knowledge-base-oriented summary follows.

| Domain | Curated finding | Quantitative evidence | Suggested ontology/identifier | Evidence type |
|---|---|---:|---|---|
| Disease identity | Allan-Herndon-Dudley syndrome, also termed MCT8 deficiency, is an ultra-rare disorder of thyroid hormone transport caused by SLC16A2 dysfunction (OpenTargets Search: Allan-Herndon-Dudley syndrome-SLC16A2, geest2021monocarboxylatetransporter8 pages 1-2) | Open Targets disease-target score 0.853; ~320 clinical cases described worldwide in reviews (vancamp2020monocarboxylatetransporter8 pages 1-2) | MONDO:0010354; OMIM:300523; MeSH:C537047; SLC16A2 | Aggregated disease resource + review |
| Synonyms | Common synonyms include Allan-Herndon-Dudley syndrome, AHDS, MCT8 deficiency, monocarboxylate transporter 8 deficiency (bauer2024unmetpatientneeds pages 1-2, geest2021monocarboxylatetransporter8 pages 1-2) | — | MONDO:0010354; OMIM:300523 | Review/guideline |
| Etiology | Caused by pathogenic loss-of-function variants in SLC16A2 encoding monocarboxylate transporter 8 (MCT8), a thyroid hormone transporter (grijotamartinez2020mct8deficiencythe pages 1-2, geest2021monocarboxylatetransporter8 pages 1-2) | ~150 pathogenic variants reported; ~250 families in one review (moran2022geneticdisordersof pages 4-5, geest2021monocarboxylatetransporter8 pages 5-6) | SLC16A2; MCT8 | Human genetics + review |
| Inheritance | Usually X-linked, predominantly affecting males; rare affected females occur with skewed X-inactivation or chromosomal rearrangements (moran2022geneticdisordersof pages 4-5, bauer2024unmetpatientneeds pages 5-6) | A carrier mother has a 50% risk of transmitting the mutant allele to sons; skewed X-inactivation described in rare females (bauer2024unmetpatientneeds pages 5-6) | X-linked inheritance; SLC16A2 | Human clinical/genetic counseling review |
| Variant spectrum | Variant classes include large deletions, truncating/frameshift/nonsense variants, and missense variants; pathogenicity of many missense variants requires functional testing (geest2021monocarboxylatetransporter8 pages 5-6, persani20242024europeanthyroid pages 5-6) | C-terminal missense variants beyond Met574 may be better tolerated in some cases (geest2021monocarboxylatetransporter8 pages 10-11) | SLC16A2 | Human genetics + functional in vitro |
| Core mechanism | Loss of MCT8 reduces T3/T4 transport across brain barriers and into neural cells, causing cerebral hypothyroidism with simultaneous peripheral thyrotoxicosis from elevated circulating T3 (grijotamartinez2020mct8deficiencythe pages 1-2, geest2021monocarboxylatetransporter8 pages 4-5) | Postmortem human cortex showed ~50% reduction in cerebral T3/T4 in cited review summary (geest2021monocarboxylatetransporter8 pages 4-5, salaslucia2024impairedt3uptake pages 1-2) | SLC16A2; HP:0001252 Hypotonia; HP:0001290 Generalized hypotonia | Human postmortem + model + review |
| Laboratory signature | Characteristic thyroid hormone “fingerprint”: high T3, low/low-normal T4, low reverse T3, TSH normal or mildly elevated; elevated T3/rT3 ratio is especially characteristic (persani20242024europeanthyroid pages 5-6, bauer2024unmetpatientneeds pages 3-5) | Elevated T3 in 95%; low free T4 in 89%; low total T4 in 90%; low rT3 in 91%; TSH within age-specific range in 89% (geest2021monocarboxylatetransporter8 pages 5-6) | HP:0031508 Increased circulating triiodothyronine level; HP:0011787 Decreased circulating thyroxine level | Human cohort + guideline |
| Neonatal laboratory pattern | Standard newborn screening usually misses the disorder because T3 is not yet elevated in the neonatal period; low rT3 may be an earlier clue (bauer2024unmetpatientneeds pages 7-8, bauer2024unmetpatientneeds pages 3-5) | In 8 patients with T4-based newborn screening data, 88% had total T4 below the 20th percentile, but none were identified by newborn screening (geest2021monocarboxylatetransporter8 pages 5-6) | Newborn screening limitation; SLC16A2 | Human cohort + review |
| Major neurologic phenotype | Severe intellectual and motor disability with hypotonia, spasticity, dystonia, poor head control, lack of speech, and often inability to sit/walk (geest2021monocarboxylatetransporter8 pages 5-6, persani20242024europeanthyroid pages 13-14) | In a 24-patient cohort: hypotonia 100%, spasticity 71%, dystonia 75%, MRI hypomyelination 19/24; in a larger cohort only 4/77 developed walking abilities (geest2021monocarboxylatetransporter8 pages 5-6, geest2021monocarboxylatetransporter8 pages 6-7) | HP:0001252 Hypotonia; HP:0001257 Spasticity; HP:0001332 Dystonia; HP:0001263 Global developmental delay | Human cohort |
| Seizures and movement phenomena | Seizures occur in a minority; exaggerated startle/paroxysmal nonepileptic events and choreiform/dystonic manifestations are recognized (moran2022geneticdisordersof pages 4-5, bauer2024unmetpatientneeds pages 3-5) | Seizures in ~25% in review summary; exaggerated startle/paroxysmal nonepileptic events in 11 patients in one movement-disorder summary (moran2022geneticdisordersof pages 4-5, bauer2024unmetpatientneeds pages 3-5) | HP:0001250 Seizure; HP:0001336 Myoclonus (if present); HP:0001332 Dystonia | Human cohort/review |
| MRI/myelin phenotype | Brain MRI often shows delayed myelination/hypomyelination, especially in early childhood, with uncertainty over delayed versus permanent hypomyelination (vancamp2020monocarboxylatetransporter8 pages 1-2, bauer2024unmetpatientneeds pages 5-6) | Majority of patients abnormal in infancy; 19/24 with hypomyelination in one cohort (geest2021monocarboxylatetransporter8 pages 5-6) | HP:0002188 Delayed CNS myelination | Human MRI cohort + review |
| Peripheral/nutritional phenotype | Low body weight, muscle wasting/hypotrophic musculature, feeding problems, reflux, constipation, and swallowing impairment reflect peripheral thyrotoxicosis plus neurologic disability (persani20242024europeanthyroid pages 13-14, bauer2024unmetpatientneeds pages 5-6) | Underweight in 71%; hypotrophic musculature in 84%; impaired swallowing in 71% in the international cohort (geest2021monocarboxylatetransporter8 pages 5-6) | HP:0004325 Decreased body weight; HP:0002015 Dysphagia; HP:0002020 Gastroesophageal reflux | Human cohort |
| Cardiovascular phenotype | Tachycardia, PACs/arrhythmia, systolic hypertension, and conduction abnormalities are common and clinically important (persani20242024europeanthyroid pages 13-14, geest2021monocarboxylatetransporter8 pages 6-7) | Resting tachycardia 31%; elevated systolic blood pressure 53%; premature atrial contractions 76% (geest2021monocarboxylatetransporter8 pages 6-7) | HP:0001649 Tachycardia; HP:0011675 Arrhythmia; HP:0000822 Hypertension | Human cohort |
| Skeletal/orthopedic phenotype | Scoliosis, hip subluxation, osteoporosis, and later spasticity contribute substantially to disability (persani20242024europeanthyroid pages 13-14, bauer2024unmetpatientneeds pages 5-6) | Quantitative prevalence not consistently reported in retrieved sources | HP:0002650 Scoliosis; HP:0002827 Hip dislocation; HP:0000939 Osteoporosis | Guideline + review |
| Onset and course | Symptoms usually become apparent after 2–4 months of age; developmental abilities plateau far below age expectations and disease is lifelong/progressive in disability burden (bauer2024unmetpatientneeds pages 3-5, geest2021monocarboxylatetransporter8 pages 6-7) | First symptoms around 4 months; median age at diagnosis 24 months (IQR 12.0–60.0); median delay from symptoms to diagnosis 18 months (IQR 7.8–63.0) (moran2022geneticdisordersof pages 4-5, bauer2024unmetpatientneeds pages 3-5) | Congenital/pediatric neurodevelopmental disorder; HP:0001263 | Human cohort + review |
| Prognosis | Life expectancy is substantially reduced, with childhood deaths often related to pulmonary infection/aspiration and possibly sudden cardiac death (moran2022geneticdisordersof pages 4-5, geest2021monocarboxylatetransporter8 pages 6-7) | Median survival 35 years; ~30% mortality in childhood in review summary; approximately 50% of severely affected patients may die in childhood (moran2022geneticdisordersof pages 4-5, geest2021monocarboxylatetransporter8 pages 6-7) | OMIM:300523 | Human cohort + review |
| Mortality predictors | Early underweight and absent head control are major markers of poor prognosis (geest2021monocarboxylatetransporter8 pages 1-2, geest2021monocarboxylatetransporter8 pages 6-7) | Both linked to higher mortality; being underweight at 1–3 years and no head control before 1.5 years strongly associated with early death (geest2021monocarboxylatetransporter8 pages 6-7) | HP:0004325 Decreased body weight; HP:0001252 Hypotonia | Human cohort |
| Diagnosis | Diagnostic workup combines clinical phenotype, thyroid profile, MRI, and confirmatory SLC16A2 sequencing; VUS assessment should include segregation, functional assays, and structural modeling (persani20242024europeanthyroid pages 5-6, bauer2024unmetpatientneeds pages 3-5) | 2024 ETA recommends sequencing in any male with major biochemical criteria plus developmental delay, hypomyelination, movement disorder, primitive reflexes, or family history (persani20242024europeanthyroid pages 5-6) | SLC16A2 sequencing; MONDO:0010354 | Guideline |
| Differential diagnosis | Key differentials include cerebral palsy, Pelizaeus-Merzbacher(-like) disease, MECP2 duplication, mitochondrial disease, and RTHα; tachycardia/failure to thrive favor MCT8 deficiency over RTHα (bauer2024unmetpatientneeds pages 3-5) | RTHα is the closest biochemical mimic among thyroid disorders in retrieved review table (bauer2024unmetpatientneeds pages 3-5) | THRA; MECP2 | Review |
| Genetic counseling/prevention | Cascade testing, carrier testing for at-risk female relatives, prenatal diagnosis, and preimplantation genetic testing are feasible once a family variant is known (persani20242024europeanthyroid pages 5-6, bauer2024unmetpatientneeds pages 7-8) | Prenatal SLC16A2 testing recommended/considered for at-risk male fetuses in positive families (persani20242024europeanthyroid pages 5-6) | SLC16A2; prenatal testing | Guideline + review |
| Supportive care | Multidisciplinary care is essential: neurology, endocrinology, gastroenterology/nutrition, cardiology, physical/speech/occupational therapy, orthopedics, and social work/case management (bauer2024unmetpatientneeds pages 5-6, persani20242024europeanthyroid pages 13-14) | In one registry survey only 19% had a pediatric gastroenterologist, 31% had dietary advice, 12.5% of those with feeding problems had a feeding tube, and 1 in 5 lacked regular physical therapy (bauer2024unmetpatientneeds pages 5-6) | NCIT supportive care terms not assigned here; HP:0011968 Feeding difficulties | Registry/review |
| Tiratricol/TRIAC evidence | TRIAC is the leading targeted therapy; it enters cells independently of MCT8 and improves peripheral thyrotoxicosis, with possible greater neurodevelopmental benefit if started very early (persani20242024europeanthyroid pages 5-6, bauer2024unmetpatientneeds pages 6-7) | Phase 2 Triac Trial I: 46 enrolled, 45 with follow-up, 40 completed 12 months; long-term cohort n=67 (27 trial + 40 compassionate use), 90% achieved target T3 range; improvements in weight, heart rate/rhythm, blood pressure, SHBG/creatinine markers (bauer2024unmetpatientneeds pages 6-7, NCT02060474 chunk 2) | Tiratricol / TRIAC / 3,3',5-triiodothyroacetic acid | Human clinical trial + real-world follow-up |
| Tiratricol status and current implementation | 2024 ETA recommends TRIAC (strong recommendation); expanded access and ongoing early-life/withdrawal studies support real-world implementation (persani20242024europeanthyroid pages 5-6, NCT05911399 chunk 1, NCT05579327 chunk 1, NCT02396459 chunk 1) | Target serum T3 1.4–2.5 nmol/L; Triac Trial II enrolled 22 children ≤30 months; ReTRIACt phase 3 completed with actual enrollment 20; US expanded access posted 2023-06-22 (persani20242024europeanthyroid pages 5-6, NCT05579327 chunk 1, NCT02396459 chunk 1) | NCT02396459; NCT05579327; NCT05911399 | Guideline + ClinicalTrials.gov |
| DITPA evidence | DITPA lowers serum T3/TSH and can cross the BBB independently of MCT8, but published human neurologic benefit has been limited (geest2021monocarboxylatetransporter8 pages 7-9, bauer2024unmetpatientneeds pages 6-7) | Compassionate use in 4 children normalized T3 and TSH but no clear neurocognitive improvement; median treatment 38.5 months (range 26–40) in one review summary (geest2021monocarboxylatetransporter8 pages 7-9) | DITPA / 3,5-diiodothyropropionic acid | Human compassionate use + preclinical |
| LT4/PTU and conventional thyroid therapy | Postnatal levothyroxine monotherapy is not recommended; LT4+PTU can reduce peripheral thyrotoxicosis but not neurologic deficits and PTU has important toxicity risks (persani20242024europeanthyroid pages 5-6, geest2021monocarboxylatetransporter8 pages 6-7) | LT4+PTU reported in 5 patients; PTU carries severe hepatotoxicity/agranulocytosis risk (geest2021monocarboxylatetransporter8 pages 6-7, bauer2024unmetpatientneeds pages 5-6) | Levothyroxine; propylthiouracil | Human case series + guideline |
| Chemical chaperone approach | Sodium/glycerol phenylbutyrate aims to rescue selected misfolded MCT8 mutants by improving membrane trafficking; human efficacy remains unproven (bauer2024unmetpatientneeds pages 7-8, NCT05019417 chunk 1) | Prospective GPB trial planned for up to 6 genetically confirmed patients (NCT05019417) (NCT05019417 chunk 1) | NCT05019417 | Preclinical + trial registration |
| Gene therapy | AAV-mediated SLC16A2/Mct8 delivery is a promising preclinical strategy, especially targeting BBB/endothelium, but remains preclinical (bauer2024unmetpatientneeds pages 7-8, maitykumar2022validationofmct8oatp1c1 pages 8-9) | IV AAV9-hMCT8 and AAV-BR1-Mct8 increased brain T3 in mice; no human trial identified in retrieved sources (bauer2024unmetpatientneeds pages 7-8) | SLC16A2 gene therapy | Preclinical animal |
| Principal animal model | Mct8/Oatp1c1 double-knockout mouse best recapitulates human disease, unlike Mct8 single knockout which lacks the full cerebral phenotype (maitykumar2022validationofmct8oatp1c1 pages 1-2, geest2021monocarboxylatetransporter8 pages 7-9) | dKO mice show decreased life expectancy, central hypothyroidism, peripheral hyperthyroidism, impaired myelination, impaired motor abilities, and peripheral tissue thyrotoxicosis (maitykumar2022validationofmct8oatp1c1 pages 1-2) | Mct8/Oatp1c1 dKO mouse | Animal model |
| Additional models | Zebrafish and patient-derived iPSC/cerebral organoid systems are useful for mechanism and therapeutic screening (geest2021monocarboxylatetransporter8 pages 7-9, salaslucia2024impairedt3uptake pages 1-2) | TRIAC completely rescued myelination in mct8-/- zebrafish larvae in review summary; human organoids showed D3 activity ~18.4 ± 7.7 vs 5.3 ± 3.1 pmol/mg/h in MCT8-deficient COs (~30% of WT) (geest2021monocarboxylatetransporter8 pages 7-9, salaslucia2024impairedt3uptake pages 4-5) | Zebrafish mct8-/-; iPSC cerebral organoid | Animal + human in vitro |
| Advanced human model insight | 2024 cerebral organoids directly showed impaired T3 uptake/action, smaller rosettes, thinner cortical units, and rescue of T3-responsive genes by DITPA/TRIAC (salaslucia2024impairedt3uptake pages 1-2, salaslucia2024impairedt3uptake pages 4-5) | MCT8-deficient CO D3 activity 5.3 ± 3.1 pmol/mg/h vs control 18.4 ± 7.7; selective MCT8 inhibitor reduced WT D3 activity to 4.4 ± 3.0 (salaslucia2024impairedt3uptake pages 4-5) | Human iPSC-derived cerebral organoid | Human in vitro |
| Quality-of-life and caregiver burden | Disease burden is high for patients and families; caregiver QoL/economic-burden study has been completed but results were not retrieved here (NCT06060197 chunk 1, bauer2024unmetpatientneeds pages 8-9) | Caregiver study enrolled 21 participants across multiple countries (NCT06060197 chunk 1) | NCT06060197 | Observational study/registry |


*Table: This table condenses high-confidence disease facts for Allan-Herndon-Dudley syndrome/MCT8 deficiency, including identifiers, molecular cause, clinical signature, prognosis, diagnostics, therapies, and key research models. It is designed for rapid knowledge-base curation with quantitative evidence and cited evidence types.*

## 1. Disease information

### Definition and identifiers

AHDS is a syndromic X-linked intellectual-developmental disorder caused by deficient cellular thyroid-hormone transport. “MCT8 deficiency” is now preferred in some clinical literature because it identifies the molecular defect and avoids an eponym. (geest2021monocarboxylatetransporter8 pages 1-2, geest2021monocarboxylatetransporter8 pages 5-6)

* **MONDO:** MONDO:0010354.
* **OMIM:** #300523.
* **MeSH:** C537047, Allan-Herndon-Dudley syndrome.
* **Causal target:** **SLC16A2**, Ensembl ENSG00000147100; Open Targets recognizes one strongly associated target, with an association score of approximately 0.853. (OpenTargets Search: Allan-Herndon-Dudley syndrome-SLC16A2)
* **Common synonyms:** Allan–Herndon–Dudley syndrome; AHDS; MCT8 deficiency; monocarboxylate transporter 8 deficiency; thyroid-hormone transporter defect.
* **Orphanet/ICD:** A specific ORPHA identifier and dedicated ICD-10/ICD-11 code were not established from the retrieved primary evidence. In routine coding, broader rare genetic neurodevelopmental or thyroid-hormone transport categories may therefore be used; these should not be treated as disease-specific identifiers without local verification.

The information summarized here is **aggregated disease-level evidence**, principally multicenter cohorts, guidelines, reviews, trial registries, and experimental studies—not individual EHR-derived data. Individual case reports contribute to rare presentations and prenatal-treatment observations.

## 2. Etiology, risk, protection, and environment

### Causal factor

The primary and sufficient cause is a **germline pathogenic variant in SLC16A2**, located at Xq13.2 and encoding the membrane transporter MCT8. MCT8 facilitates transport of T3 and T4 across cell membranes, particularly the blood–brain barrier and selected neural-cell membranes. Loss of transport function creates tissue-specific thyroid-hormone deprivation and excess. (geest2021monocarboxylatetransporter8 pages 4-5, geest2021monocarboxylatetransporter8 pages 5-6)

### Risk factors

* **Genetic:** hemizygosity for a pathogenic SLC16A2 allele in males. Variant classes include whole-gene or multiexon deletions, frameshift, nonsense, splice-altering, and pathogenic missense variants. Approximately 150 distinct disease-associated variants in roughly 250 families had been reported by 2021. (geest2021monocarboxylatetransporter8 pages 5-6)
* **Family history:** a heterozygous carrier has a 50% probability of transmitting the variant in each pregnancy; sons inheriting it are generally affected, while daughters are usually carriers.
* **Sex:** males are overwhelmingly affected because the disorder is X-linked. Rare symptomatic females have been reported with skewed X-inactivation or X-chromosomal rearrangement. (moran2022geneticdisordersof pages 4-5, bauer2024unmetpatientneeds pages 5-6)
* **De novo occurrence/germline mosaicism:** possible; absence of family history does not exclude AHDS. (bauer2024unmetpatientneeds pages 5-6)

No reproducible environmental, infectious, toxic, occupational, dietary, smoking, or lifestyle cause is known. Consanguinity is not intrinsically relevant to this X-linked condition. No GWAS susceptibility architecture is expected for a monogenic disorder.

### Protective and modifier factors

No validated protective allele, modifier gene, diet, or lifestyle intervention prevents disease in a person carrying a fully pathogenic allele. **Residual MCT8 transport activity** can moderate severity: truncating variants and large deletions generally produce severe disease, whereas some missense variants retain transport. Not every rare missense change is pathogenic, and C-terminal substitutions beyond Met574 of the long isoform may be tolerated. Functional assays are therefore important. (beheshti2022allanherndondudleysyndromea pages 1-2, geest2021monocarboxylatetransporter8 pages 5-6, geest2021monocarboxylatetransporter8 pages 10-11)

There is no established gene–environment interaction. Nutrition, aspiration prevention, cardiac surveillance, and therapy can modify complications and survival but do not alter the inherited cause.

## 3. Phenotypes

### Neurologic and developmental phenotype

Symptoms are generally absent or nonspecific at birth and emerge at approximately 2–4 months, with hypotonia, poor head control, delayed milestones, and poor weight gain. Development is chronically and severely impaired. In a large cohort, motor and cognitive scores plateaued at a developmental age well below 12 months despite a median chronological evaluation age of 6.4 years. Only 4 of 77 individuals in the larger international cohort acquired walking. (geest2021monocarboxylatetransporter8 pages 6-7, bauer2024unmetpatientneeds pages 3-5)

Key findings and suggested HPO annotations are:

* **Global developmental delay/severe intellectual disability:** almost universal, severe, lifelong; **HP:0001263**, **HP:0001249**.
* **Central hypotonia and poor head control:** early and severe; hypotonia occurred in 100% of a 24-person cohort; **HP:0001252**, **HP:0001290**.
* **Spasticity/spastic quadriplegia:** frequently emerges later as hypotonia evolves; 71% in one cohort; **HP:0001257**.
* **Dystonia and mixed movement disorder:** 75% in one cohort; may include chorea, athetosis, bradykinesia, paroxysmal dyskinesia, and exaggerated startle; **HP:0001332**, with more specific movement terms as documented. (geest2021monocarboxylatetransporter8 pages 5-6, bauer2024unmetpatientneeds pages 3-5)
* **Absent or profoundly impaired speech:** common; **HP:0001344**/appropriate expressive-language term.
* **Seizures:** approximately 25%, generally less frequent than the movement disorder; **HP:0001250**. (moran2022geneticdisordersof pages 4-5)
* **Persistent primitive reflexes:** characteristic clinical clue; **HP:0002496** where applicable.

Quality-of-life effects are profound: most patients are nonverbal, wheelchair-dependent, and reliant on caregivers for all activities of daily living. Caregiver priorities in a 22-person survey were developmental gains (100%), head control (59%), sitting (50%), weight gain (36%), expressive language (32%), dysphagia or reflux improvement (27% each), and reduced dystonia/spasticity (18%). (bauer2024unmetpatientneeds pages 6-7)

### Neuroimaging and myelin

MRI commonly shows diffuse delayed myelination or hypomyelination, particularly in deep anterior white matter before age five; 19/24 patients in one series were affected, and approximately half had global cerebral atrophy. Some conventional MRI studies suggest improvement with age, whereas postmortem and advanced imaging indicate persistent microstructural myelin abnormalities. The most accurate current interpretation is **developmentally delayed and potentially incomplete myelination**, with heterogeneity by age and method. Suggested HPO: **HP:0002188, delayed CNS myelination**. (vancamp2020monocarboxylatetransporter8 pages 1-2, geest2021monocarboxylatetransporter8 pages 5-6, bauer2024unmetpatientneeds pages 5-6)

### Endocrine, nutritional, and gastrointestinal phenotype

Peripheral thyrotoxicosis causes hypermetabolism superimposed on neurologic feeding impairment.

* **Low body weight/failure to thrive:** underweight in 71%; **HP:0004325**, **HP:0001508**.
* **Hypotrophic musculature/muscle wasting:** 84%; **HP:0003202**.
* **Dysphagia/impaired swallowing:** 71%, with aspiration risk; **HP:0002015**.
* **Feeding difficulty, gastroesophageal reflux, gastroparesis, constipation:** common; **HP:0011968**, **HP:0002020**, **HP:0002019**.
* **Increased sweating and heat production:** compatible with systemic T3 excess; **HP:0000975** where documented.

The characteristic laboratory abnormalities in the international cohort were elevated T3 in 95%, low free T4 in 89%, low total T4 in 90%, low rT3 in 91%, and age-normal TSH in 89%; all tested patients had a high T3:rT3 ratio. (geest2021monocarboxylatetransporter8 pages 5-6)

### Cardiovascular, respiratory, and skeletal phenotype

Premature atrial contractions occurred in 76%, elevated systolic blood pressure in 53%, and resting tachycardia in 31%. Conduction abnormalities and sudden death raise concern for arrhythmic mortality. Suggested HPO: **HP:0001649 tachycardia**, **HP:0000822 hypertension**, and the specific arrhythmia term documented by ECG. (geest2021monocarboxylatetransporter8 pages 6-7, persani20242024europeanthyroid pages 13-14)

Recurrent pulmonary infection and aspiration pneumonia are major complications. Scoliosis, hip subluxation/dislocation, and osteoporosis develop from abnormal tone, immobility, malnutrition, and endocrine effects. Suggested terms include **HP:0002650 scoliosis**, **HP:0002827 hip dislocation**, and **HP:0000939 osteoporosis**. (persani20242024europeanthyroid pages 13-14)

## 4. Genetic and molecular information

### Gene and protein

* **Gene:** SLC16A2; approved protein name monocarboxylate transporter 8/MCT8.
* **Disease mechanism:** germline loss of function or marked reduction in thyroid-hormone transport.
* **Origin:** constitutional/germline, not a somatic cancer mechanism.
* **Variant spectrum:** deletions, frameshift and nonsense truncation, splice variants, in-frame indels, and missense variants. Population frequencies should be assessed variant-by-variant in gnomAD; pathogenic severe alleles are expected to be absent or extremely rare. No single allele frequency can characterize the disease.
* **Classification:** apply ACMG/AMP criteria using phenotype, segregation, absence from population databases, predicted consequence, and functional transport evidence. ETA recommends that an SLC16A2 VUS be evaluated with family segregation, testing in transfected or patient-derived cells, and structural modeling; computational prediction alone is insufficient. (persani20242024europeanthyroid pages 5-6)

### Genotype–phenotype relationship

Large deletions and truncating variants generally confer severe disease. Missense variants range from complete loss to appreciable residual function and can produce milder phenotypes. Functional testing in an appropriate cell system is essential because some overexpression systems misclassify membrane trafficking or residual transport. Chemical-chaperone responsiveness is likewise mutation-specific. (geest2021monocarboxylatetransporter8 pages 7-9, geest2021monocarboxylatetransporter8 pages 5-6)

No independently validated modifier gene or disease-specific epigenetic signature is established. Rare structural rearrangements involving the X chromosome can cause disease in females by disrupting SLC16A2 or altering X-inactivation. Genetic anticipation is not a feature.

## 5. Environmental information

AHDS is not caused by toxins, radiation, pollution, occupation, lifestyle, or an infectious agent. Environmental and care-related factors instead influence complications: inadequate caloric intake and dysphagia worsen underweight; immobility worsens skeletal health; aspiration promotes pneumonia; and delayed recognition postpones supportive and targeted therapy. No vaccine, anti-infective prophylaxis, or exposure avoidance prevents the molecular disease.

## 6. Mechanism and pathophysiology

### Upstream causal chain

**Pathogenic SLC16A2 allele → absent/reduced MCT8 protein or membrane transport → impaired T3/T4 transfer across brain endothelium and selected neural membranes → intracellular thyroid-hormone deficiency during fetal and postnatal brain development → deficient nuclear thyroid-receptor signaling → abnormal progenitor proliferation/differentiation, neuronal migration, axonal maturation, synaptogenesis, oligodendrocyte maturation, and myelination → severe motor, cognitive, and movement disorder.** (salaslucia2024impairedt3uptake pages 1-2, geest2021monocarboxylatetransporter8 pages 4-5)

Human postmortem evidence is especially important: fetal and 11-year-old brain showed delayed cortical/cerebellar development, altered Purkinje-cell dendritogenesis, low MBP, and impaired axonal maturation; cerebral T3 and T4 were approximately 50% lower. These findings demonstrate prenatal onset and argue against complete spontaneous neural recovery. (geest2021monocarboxylatetransporter8 pages 4-5)

Suggested GO biological processes include thyroid hormone transport, response to thyroid hormone, regulation of transcription by RNA polymerase II, neurogenesis, neuron differentiation, axonogenesis, synapse organization, oligodendrocyte differentiation, and CNS myelination. Relevant cell types include brain microvascular endothelial cells, neurons, neural progenitors, oligodendrocyte precursor cells, mature oligodendrocytes, astrocytes, tanycytes, Purkinje neurons, and pituitary folliculostellate cells. High-confidence CL mappings should be curated against the current Cell Ontology release rather than inferred from names alone.

### Peripheral thyrotoxicosis and biochemical signature

Outside the CNS, alternative thyroid-hormone transporters permit uptake of elevated serum T3. MCT8 deficiency may trap T4 in renal proximal-tubule cells, increase DIO1 activity and T4-to-T3 conversion, and contribute to high serum T3 with low T4/rT3. Altered thyroidal secretion and hypothalamic–pituitary feedback may also contribute. The renal mechanism is compelling in mice but is not fully resolved in humans. (geest2021monocarboxylatetransporter8 pages 4-5, geest2021monocarboxylatetransporter8 pages 5-6)

Downstream excess T3 signaling drives increased catabolism, low weight, muscle loss, tachycardia, blood-pressure abnormalities, high SHBG, low cholesterol/creatinine, and enhanced bone turnover. This explains the paradox of a hypothyroid brain within a systemically thyrotoxic organism.

### Molecular profiling and 2024 development

Patient-derived cerebral organoids provided direct human, species-relevant evidence in 2024. MCT8-deficient organoids had smaller neural rosettes, thinner cortical units, impaired T3 transport, reduced T3-responsive transcription, and altered genes involved in cortical development, migration, astrocyte biology, myelin, neurotransmission, ion channels, and extracellular matrix. D3-mediated T3 metabolism was 5.3 ± 3.1 pmol/mg/h versus 18.4 ± 7.7 in controls—about 30% of wild type. TRIAC and DITPA restored induction or repression of T3-responsive genes despite nonfunctional MCT8. (salaslucia2024impairedt3uptake pages 4-5, salaslucia2024impairedt3uptake pages 1-2, salaslucia2024impairedt3uptake pages 9-10)

Direct abstract statement: “**MCT8-deficient COs represent a species-specific relevant preclinical model that can be utilized to screen drugs with potential benefits as personalized therapeutics for patients with AHDS.**” [Salas-Lucia et al., published February 20, 2024; DOI: https://doi.org/10.1172/jci.insight.174645]. (salaslucia2024impairedt3uptake pages 1-2)

No mature disease-specific single-cell atlas, spatial-transcriptomic dataset, proteomic signature, lipidomic biomarker, or integrated human multi-omic classifier was identified. The organoid RNA-seq work is currently the clearest advanced molecular-profiling evidence.

## 7. Anatomical structures affected

### Organ and tissue levels

* **Primary:** CNS—cerebral cortex, white matter, basal ganglia/dopaminergic circuits, corticospinal pathways, cerebellum/Purkinje cells, and brain barriers.
* **Secondary/peripheral:** skeletal muscle, heart and conduction system, kidney, liver, bone, gastrointestinal tract, lungs through aspiration, and thyroid/hypothalamic–pituitary axis.
* **Suggested UBERON concepts:** brain, cerebral cortex, cerebral white matter, basal ganglion, cerebellum, blood–brain barrier, spinal cord, skeletal muscle tissue, heart, kidney, liver, bone, esophagus, stomach, and lung. Exact IDs should be resolved against the current UBERON release during ingestion.

At the subcellular level, MCT8 is a multi-pass **plasma-membrane** transporter. Missense variants may cause misfolding, defective membrane trafficking, instability, or impaired substrate transport. Relevant GO cellular components are plasma membrane, blood–brain-barrier endothelial membrane, axon, neuronal cell body, myelin sheath, and nucleus downstream of thyroid-receptor signaling. There is no characteristic lateralization; CNS and systemic effects are bilateral/diffuse.

## 8. Temporal development

AHDS is congenital genetically and pathophysiologically, with prenatal brain vulnerability, but clinical signs often become recognizable only after 2–4 months. Median diagnosis was 24 months (IQR 12–60), with an 18-month median symptom-to-diagnosis delay (IQR 7.8–63). (bauer2024unmetpatientneeds pages 3-5)

The course is chronic and lifelong. A useful clinical staging framework is:

1. **Prenatal/neonatal:** impaired neural thyroid signaling; routine screening usually negative.
2. **Early infancy:** hypotonia, poor head control, feeding difficulty, failure to thrive.
3. **Childhood:** severe milestone limitation, dystonia, evolving spasticity, hypomyelination, increasing nutritional and orthopedic burden.
4. **Adolescence/adulthood:** persistent profound disability, contractures/scoliosis, low weight, cardiopulmonary complications, and premature mortality.

There is no spontaneous remission. Some conventional MRI myelination appearances improve, but functional recovery is usually very limited. The critical treatment period begins during fetal neurogenesis and likely declines across the first three years, whereas peripheral thyrotoxicosis remains treatable at any age. (persani20242024europeanthyroid pages 13-14, bauer2024unmetpatientneeds pages 6-7)

## 9. Inheritance and population

AHDS is X-linked and predominantly affects males. Penetrance in males with clearly loss-of-function alleles appears high, but expressivity varies with residual transport. Heterozygous females are usually asymptomatic or mildly affected because of random X-inactivation; skewed X-inactivation or structural X abnormalities can cause overt disease. (bauer2024unmetpatientneeds pages 5-6)

Published epidemiology is imprecise. Earlier reviews cited fewer than one case per million and approximately 320 diagnosed patients; genetic/natural-history analyses suggest approximately **1 per 70,000 males**, indicating substantial underdiagnosis. No reliable annual incidence, population carrier frequency, ethnic enrichment, endemic geography, or broad founder effect has been established. (grijotamartinez2020mct8deficiencythe pages 1-2, moran2022geneticdisordersof pages 4-5)

There is no evidence for anticipation. Germline mosaicism is possible. Geographic case distribution largely reflects access to pediatric neurology, endocrine testing, sequencing, and specialist networks rather than biologic restriction.

## 10. Diagnostics

### Clinical and laboratory diagnosis

The 2024 ETA guideline recommends full neurologic and physical assessment plus age-adjusted serum **free/total T3, free/total T4, rT3, and TSH**. Major criteria are the characteristic biochemical pattern plus global developmental delay, hypomyelination, movement disorder, persistent primitive reflexes, or family history. (persani20242024europeanthyroid pages 5-6)

Useful additional tests include:

* SHBG, creatinine, CK, cholesterol, and ALT as peripheral thyroid-action markers.
* Nutritional assessment and serial weight, every three months in infants/children.
* ECG, Holter/telemetry, blood pressure, and echocardiography where indicated.
* Swallow evaluation and videofluoroscopic study for aspiration.
* Brain MRI for myelination and atrophy.
* EEG for suspected seizures—not for most paroxysmal dystonia/startle events by default.
* Spine/hip radiography and DXA for orthopedic/bone complications. (persani20242024europeanthyroid pages 13-14)

### Genetic testing strategy

1. **Known familial variant:** targeted SLC16A2 testing.
2. **Classic biochemical/clinical presentation:** SLC16A2 sequencing plus deletion/duplication analysis.
3. **Nonspecific developmental disorder:** neurodevelopmental, leukodystrophy, or thyroid-signaling panel that explicitly includes SLC16A2.
4. **Unresolved case:** WES or WGS with copy-number analysis; WGS can additionally detect regulatory/intergenic and complex structural variants.
5. CMA can detect large Xq13 deletions but does not exclude sequence-level disease. Karyotyping/FISH are reserved for suspected rearrangements, especially affected females. Mitochondrial and repeat-expansion testing are not disease-specific. (bauer2024unmetpatientneeds pages 5-6)

RNA studies or patient-cell transport assays can clarify splice variants and VUSs. Proteomics, metabolomics, epigenomics, and liquid biopsy are not established diagnostic methods.

### Differential diagnosis

Important alternatives include cerebral palsy, Pelizaeus–Merzbacher and Pelizaeus–Merzbacher-like disorders, MECP2 duplication syndrome, mitochondrial disease, other leukodystrophies, congenital hypothyroidism, and resistance to thyroid hormone alpha. RTHα is the closest biochemical mimic, but tends toward bradycardia and skeletal dysplasia, whereas MCT8 deficiency produces tachycardia, hypermetabolism, and failure to thrive. (bauer2024unmetpatientneeds pages 3-5)

### Screening

Routine TSH- or T4-based newborn screening misses AHDS because T3 elevation develops later. Among eight patients with historical T4 newborn-screening data, 88% had T4 below the 20th percentile but none was identified; TSH screening would also have been negative. Low neonatal rT3 and an elevated T3:rT3 ratio are candidate biomarkers, but rT3 availability and assay standardization limit implementation. (geest2021monocarboxylatetransporter8 pages 5-6, bauer2024unmetpatientneeds pages 3-5)

## 11. Outcome and prognosis

Median survival in the international natural-history cohort was approximately **35 years**. About 30% die in childhood in published summaries; among the most severely affected, childhood mortality approached 50%. Pulmonary infection, aspiration pneumonia, and sudden death—possibly arrhythmic—are major causes. (moran2022geneticdisordersof pages 4-5, geest2021monocarboxylatetransporter8 pages 6-7)

Early underweight at ages 1–3 and failure to acquire head control by 1.5 years are adverse prognostic markers. These reflect peripheral thyrotoxicosis/nutritional compromise and neurologic severity, respectively. No validated molecular prognostic biomarker beyond residual variant function is established. (geest2021monocarboxylatetransporter8 pages 6-7)

Recovery to independent function is uncommon. Morbidity includes lifelong dependence, absent speech and ambulation in most, dysphagia, malnutrition, aspiration, contractures, scoliosis, osteoporosis, sleep disturbance, and repeated specialist/hospital care. A completed 21-caregiver multinational study measured economic burden, EQ-5D-5L, PedsQL Family Impact, and proxy patient QoL, but numerical results were not available in the retrieved record. [NCT06060197, posted September 29, 2023; https://clinicaltrials.gov/study/NCT06060197]. (NCT06060197 chunk 1)

## 12. Treatment

### Current strategy and expert guidance

Treatment should combine control of peripheral thyrotoxicosis with intensive multidisciplinary supportive care. The 2024 ETA guideline strongly recommends **TRIAC/tiratricol** and weakly recommends **DITPA**; postnatal levothyroxine monotherapy is not recommended. TRIAC or DITPA should be titrated toward serum T3 of **1.4–2.5 nmol/L**, unless dose-related toxicity intervenes. Assay cross-reactivity with TRIAC can distort immunoassay T3; LC-MS/MS is preferred where available. (persani20242024europeanthyroid pages 5-6, persani20242024europeanthyroid pages 13-14)

### Tiratricol/TRIAC

TRIAC (3,3′,5-triiodothyroacetic acid; tiratricol) enters cells independently of MCT8 and activates thyroid receptors. In Triac Trial I, 46 were enrolled, 45 had follow-up, and 40 completed 12 months. Serum T3 fell and body weight, heart rate/rhythm, blood pressure, SHBG, and creatinine improved. Benefits persisted during extension treatment; serious drug-related adverse events were not observed, although transient biochemical thyrotoxicosis occurred in a small subset. Neurologic improvement was not proven overall, but younger children showed a favorable trend. [PMID 31377265; published July 31, 2019; DOI: https://doi.org/10.1016/S2213-8587(19)30155-X]. (geest2021monocarboxylatetransporter8 pages 7-9, NCT02060474 chunk 2)

A long-term combined cohort of 67 patients found 60/67 (90%) maintained T3 within target, including patients treated beyond two years. A four-patient Argentine real-world series reported lower T3 in all, weight gain in two malnourished children, and improvements in tone/development, but uncontrolled observations cannot establish neurologic efficacy. (bauer2024unmetpatientneeds pages 6-7)

Relevant trials/implementation:

* **NCT02060474, Triac Trial I:** completed phase II, n=46. https://clinicaltrials.gov/study/NCT02060474. (NCT02060474 chunk 1)
* **NCT02396459, Triac Trial II:** open-label phase II, n=22 boys treated by ≤30 months, assessing GMFM-88, Bayley-III, HINE, thyroid and cardiac outcomes through five years. https://clinicaltrials.gov/study/NCT02396459. (NCT02396459 chunk 1, NCT02396459 chunk 2)
* **NCT05579327, ReTRIACt:** randomized quadruple-masked phase III withdrawal study, actual n=20, designed to test whether stopping tiratricol causes T3 rebound. https://clinicaltrials.gov/study/NCT05579327. (NCT05579327 chunk 1)
* **NCT05911399:** U.S. expanded-access program, using 350-µg tablets orally or by PEG/NG/jejunal tube. https://clinicaltrials.gov/study/NCT05911399. (NCT05911399 chunk 1)

Suggested NCIT intervention concepts: tiratricol/thyroid-hormone analog therapy, oral drug administration, enteral-tube administration, physical therapy, occupational therapy, speech-language therapy, nutritional support, and genetic counseling; exact NCIT codes should be resolved against the current NCIT release.

### DITPA

DITPA (3,5-diiodothyropropionic acid) bypasses MCT8 and binds thyroid receptors, but has substantially weaker TRβ affinity than T3. Four children treated compassionately for a median 38.5 months normalized T3 and TSH and showed some peripheral improvement, but no neurocognitive benefit. It remains less strongly supported than TRIAC. (geest2021monocarboxylatetransporter8 pages 7-9, bauer2024unmetpatientneeds pages 6-7)

### Conventional thyroid drugs

Levothyroxine alone can further increase T3 and worsen peripheral thyrotoxicosis without entering the MCT8-dependent brain. LT4 plus PTU reduced T3, heart rate, and SHBG and improved weight in five reported patients but did not improve neurodevelopment. PTU carries clinically important risks of agranulocytosis and severe hepatic failure; the 2024 guidance therefore favors analog therapy. (geest2021monocarboxylatetransporter8 pages 6-7, bauer2024unmetpatientneeds pages 5-6)

### Supportive and rehabilitative care

Care should include endocrinology, neurology, clinical genetics, cardiology, gastroenterology/nutrition, respiratory care, orthopedics, physiotherapy, occupational therapy, speech/augmentative communication, swallowing therapy, social work, and palliative-care expertise when appropriate. Interventions include calorie optimization, gastrostomy when oral feeding is unsafe/inadequate, reflux/constipation management, aspiration precautions, vaccination and prompt respiratory treatment, dystonia/spasticity management, seizure therapy when present, positioning/assistive devices, scoliosis/hip surveillance, and sleep support. Evidence for specific symptomatic regimens in AHDS is limited. (persani20242024europeanthyroid pages 13-14, bauer2024unmetpatientneeds pages 5-6)

Registry evidence reveals implementation gaps: only 19% had pediatric gastroenterology involvement, 31% received dietitian advice, 12.5% of those reporting feeding problems had a feeding tube, 6% had pediatric cardiology involvement, and one in five did not receive regular physical therapy. (bauer2024unmetpatientneeds pages 5-6)

### Experimental therapeutics

* **Glycerol phenylbutyrate:** intended as a chemical chaperone for selected misfolded MCT8 variants. NCT05019417 proposed up to six patients with escalating Ravicti dosing, but registry status was unknown and efficacy is unproven. https://clinicaltrials.gov/study/NCT05019417. (NCT05019417 chunk 1)
* **Gene therapy:** IV AAV9-hMCT8 and BBB-targeted AAV-BR1-Mct8 increase brain T3 and improve motor phenotypes in mice. No human gene-therapy trial was identified. (maitykumar2022validationofmct8oatp1c1 pages 8-9, bauer2024unmetpatientneeds pages 7-8)
* **Sobetirome/Sob-AM2:** MCT8-independent thyromimetics reach fetal brain in mice, but maternal Sob-AM2 was associated with spontaneous abortions; not ready for clinical use. (bauer2024unmetpatientneeds pages 8-9)
* **Prenatal treatment:** one intra-amniotic high-dose LT4 case beginning at gestational week 17 suggested possible benefit; prenatal DITPA has been explored under compassionate-access protocols. These remain experimental and should occur only in specialist research settings. (geest2021monocarboxylatetransporter8 pages 9-10, persani20242024europeanthyroid pages 13-14)

No pharmacogenomic dosing guideline, cell therapy, immunotherapy, surgery that modifies the molecular disease, or approved CRISPR/RNA therapy exists.

## 13. Prevention

There is no lifestyle or environmental primary prevention after conception because AHDS is genetic. Primary prevention at the family level consists of genetic counseling, carrier testing, reproductive planning, preimplantation genetic testing, and prenatal diagnosis once a familial variant is known. ETA suggests SLC16A2 testing by chorionic-villus sampling or amniocentesis in an at-risk male fetus. (persani20242024europeanthyroid pages 5-6)

Secondary prevention is early recognition through family cascade testing, developmental surveillance, complete thyroid testing including T3/rT3, and rapid genetic confirmation. Universal newborn screening is not currently established. Tertiary prevention includes aspiration reduction, nutritional support, cardiac monitoring, bone/orthopedic surveillance, vaccination, rehabilitation, and targeted reduction of T3 excess. There is no disease-specific immunization or antimicrobial prophylaxis.

## 14. Other species and natural disease

The causal pathway is evolutionarily conserved, but no well-established, naturally occurring veterinary counterpart was identified in the retrieved evidence. Accordingly, breed-specific VBO terms, animal incidence, and veterinary management cannot be assigned. The condition is neither infectious nor zoonotic and has no cross-species transmission.

Orthologs include murine **Slc16a2/Mct8** and zebrafish **slc16a2/mct8**. Species differ substantially in compensatory brain transporters—especially murine Oatp1c1—which explains why ordinary Mct8-null mice do not reproduce the severe human neurologic phenotype. (maitykumar2022validationofmct8oatp1c1 pages 1-2)

## 15. Model organisms and experimental systems

### Mouse

The **Mct8 single-knockout mouse** reproduces the abnormal serum thyroid profile and impaired cerebral T3 entry but has relatively preserved brain development because Oatp1c1 transports T4 into the murine brain. It is useful for endocrine and renal mechanism studies but limited for human neurologic translation. (maitykumar2022validationofmct8oatp1c1 pages 1-2)

The **Mct8/Oatp1c1 double-knockout mouse** is the principal mammalian model. A 2022 CRISPR-generated line showed reduced survival, central hypothyroidism, peripheral hyperthyroidism, impaired myelination and motor performance, and excessive thyroid action in liver, adipose tissue, muscle, and bone. Viral restoration of Mct8 increased CNS T3 and improved motor function. Direct abstract statement: “**Mct8/Oatp1c1 dKO mice mimic key hallmarks of the AHDS**.” [Published October 18, 2022; DOI: https://doi.org/10.1016/j.molmet.2022.101616]. (maitykumar2022validationofmct8oatp1c1 pages 1-2, maitykumar2022validationofmct8oatp1c1 pages 8-9)

### Zebrafish

The **mct8−/− zebrafish** develops hypomyelination and is useful for rapid developmental and drug screening. TRIAC completely rescued myelination and DITPA partially restored it in larval studies; Mct8 transgene expression also rescued the phenotype. (geest2021monocarboxylatetransporter8 pages 7-9)

### Human cellular models

Patient-derived iPSC blood–brain-barrier models demonstrate reduced transendothelial T3 transport, directly supporting MCT8’s barrier role. Neural and oligodendroglial systems permit variant-functional assays and testing of analogs or chemical chaperones. (geest2021monocarboxylatetransporter8 pages 4-5)

The 2024 patient-derived cerebral organoid model is currently the strongest human developmental platform. It captures neural-progenitor, cortical, astroglial, and oligodendroglial abnormalities, supports RNA-seq profiling, and demonstrates MCT8-independent rescue of thyroid-responsive transcription by TRIAC and DITPA. Limitations include organoid heterogeneity, incomplete maturation and vasculature, and supraphysiologic T3 exposure. (salaslucia2024impairedt3uptake pages 4-5, salaslucia2024impairedt3uptake pages 9-10)

## Evidence gaps and curation cautions

1. Prevalence ranges from historical diagnosed-case estimates below 1/million to modeled estimates near 1/70,000 males; underdiagnosis is likely.
2. Phenotype frequencies depend on ascertainment and age. The 24-person neurologic cohort overrepresented milder ambulant cases relative to the larger cohort.
3. No controlled evidence proves neurodevelopmental rescue in humans; apparent early-treatment gains require confirmation.
4. Variant pathogenicity must not be inferred from rarity or prediction alone.
5. Exact ORPHA, ICD, HGNC, GO, CL, UBERON, CHEBI, and NCIT identifiers not directly verified in the retrieved authoritative records should be resolved against current ontology releases before database ingestion.
6. No robust disease-specific epigenomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or natural-veterinary disease resource was identified.

## Priority references

* Persani L, et al. **2024 European Thyroid Association Guidelines on diagnosis and management of genetic disorders of thyroid hormone transport, metabolism and action.** *European Thyroid Journal*. Published July 2024. DOI: https://doi.org/10.1530/ETJ-24-0125. (persani20242024europeanthyroid pages 5-6, persani20242024europeanthyroid pages 13-14)
* Bauer AJ, et al. **Unmet patient needs in monocarboxylate transporter 8 deficiency: a review.** *Frontiers in Pediatrics*. Published July 2024. DOI: https://doi.org/10.3389/fped.2024.1444919. (bauer2024unmetpatientneeds pages 1-2, bauer2024unmetpatientneeds pages 5-6)
* Salas-Lucia F, et al. **Impaired T3 uptake and action in MCT8-deficient cerebral organoids underlie Allan-Herndon-Dudley syndrome.** *JCI Insight*. Published February 20, 2024. DOI: https://doi.org/10.1172/jci.insight.174645. (salaslucia2024impairedt3uptake pages 1-2)
* Groeneweg S, et al. **Disease characteristics of MCT8 deficiency: an international retrospective multicentre cohort study.** *Lancet Diabetes & Endocrinology*. 2020;8:594–605. DOI: https://doi.org/10.1016/S2213-8587(20)30153-4. (geest2021monocarboxylatetransporter8 pages 9-10)
* Groeneweg S, et al. **Effectiveness and safety of TRIAC in children and adults with MCT8 deficiency.** *Lancet Diabetes & Endocrinology*. Published July 31, 2019. PMID: 31377265. DOI: https://doi.org/10.1016/S2213-8587(19)30155-X. (NCT02060474 chunk 2)
* Maity-Kumar G, et al. **Validation of Mct8/Oatp1c1 dKO mice as a model organism for AHDS.** *Molecular Metabolism*. Published October 18, 2022. DOI: https://doi.org/10.1016/j.molmet.2022.101616. (maitykumar2022validationofmct8oatp1c1 pages 1-2)
* van Geest FS, et al. **MCT8 deficiency: from pathophysiological understanding to therapy development.** *Frontiers in Endocrinology*. Published September 2021. DOI: https://doi.org/10.3389/fendo.2021.723750. (geest2021monocarboxylatetransporter8 pages 1-2)
* Vancamp P, et al. **MCT8 deficiency: delayed or permanent hypomyelination?** *Frontiers in Endocrinology*. Published May 2020. DOI: https://doi.org/10.3389/fendo.2020.00283. (vancamp2020monocarboxylatetransporter8 pages 1-2)

References

1. (grijotamartinez2020mct8deficiencythe pages 1-2): Carmen Grijota-Martínez, Soledad Bárez-López, David Gómez-Andrés, and Ana Guadaño-Ferraz. Mct8 deficiency: the road to therapies for a rare disease. Frontiers in Neuroscience, Apr 2020. URL: https://doi.org/10.3389/fnins.2020.00380, doi:10.3389/fnins.2020.00380. This article has 55 citations and is from a peer-reviewed journal.

2. (persani20242024europeanthyroid pages 5-6): Luca Persani, Patrice Rodien, Carla Moran, W Edward Visser, Stefan Groeneweg, Robin Peeters, Samuel Refetoff, Mark Gurnell, Paolo Beck-Peccoz, and Krishna Chatterjee. 2024 european thyroid association guidelines on diagnosis and management of genetic disorders of thyroid hormone transport, metabolism and action. European Thyroid Journal, Jul 2024. URL: https://doi.org/10.1530/etj-24-0125, doi:10.1530/etj-24-0125. This article has 55 citations and is from a peer-reviewed journal.

3. (geest2021monocarboxylatetransporter8 pages 6-7): Ferdy S. van Geest, Nilhan Gunhanlar, Stefan Groeneweg, and W. Edward Visser. Monocarboxylate transporter 8 deficiency: from pathophysiological understanding to therapy development. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.723750, doi:10.3389/fendo.2021.723750. This article has 42 citations.

4. (persani20242024europeanthyroid pages 13-14): Luca Persani, Patrice Rodien, Carla Moran, W Edward Visser, Stefan Groeneweg, Robin Peeters, Samuel Refetoff, Mark Gurnell, Paolo Beck-Peccoz, and Krishna Chatterjee. 2024 european thyroid association guidelines on diagnosis and management of genetic disorders of thyroid hormone transport, metabolism and action. European Thyroid Journal, Jul 2024. URL: https://doi.org/10.1530/etj-24-0125, doi:10.1530/etj-24-0125. This article has 55 citations and is from a peer-reviewed journal.

5. (bauer2024unmetpatientneeds pages 6-7): Andrew J. Bauer, Bethany Auble, Amy L. Clark, Tina Y. Hu, Amber Isaza, Kyle P. McNerney, Daniel L. Metzger, Lindsey Nicol, Samuel R. Pierce, and Richard Sidlow. Unmet patient needs in monocarboxylate transporter 8 (mct8) deficiency: a review. Frontiers in Pediatrics, Jul 2024. URL: https://doi.org/10.3389/fped.2024.1444919, doi:10.3389/fped.2024.1444919. This article has 12 citations.

6. (OpenTargets Search: Allan-Herndon-Dudley syndrome-SLC16A2): Open Targets Query (Allan-Herndon-Dudley syndrome-SLC16A2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (geest2021monocarboxylatetransporter8 pages 1-2): Ferdy S. van Geest, Nilhan Gunhanlar, Stefan Groeneweg, and W. Edward Visser. Monocarboxylate transporter 8 deficiency: from pathophysiological understanding to therapy development. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.723750, doi:10.3389/fendo.2021.723750. This article has 42 citations.

8. (vancamp2020monocarboxylatetransporter8 pages 1-2): Pieter Vancamp, Barbara A. Demeneix, and Sylvie Remaud. Monocarboxylate transporter 8 deficiency: delayed or permanent hypomyelination? Frontiers in Endocrinology, May 2020. URL: https://doi.org/10.3389/fendo.2020.00283, doi:10.3389/fendo.2020.00283. This article has 47 citations.

9. (bauer2024unmetpatientneeds pages 1-2): Andrew J. Bauer, Bethany Auble, Amy L. Clark, Tina Y. Hu, Amber Isaza, Kyle P. McNerney, Daniel L. Metzger, Lindsey Nicol, Samuel R. Pierce, and Richard Sidlow. Unmet patient needs in monocarboxylate transporter 8 (mct8) deficiency: a review. Frontiers in Pediatrics, Jul 2024. URL: https://doi.org/10.3389/fped.2024.1444919, doi:10.3389/fped.2024.1444919. This article has 12 citations.

10. (moran2022geneticdisordersof pages 4-5): Carla Moran, Nadia Schoenmakers, W. Edward Visser, Erik Schoenmakers, Maura Agostini, and Krishna Chatterjee. Genetic disorders of thyroid development, hormone biosynthesis and signalling. Clinical Endocrinology, 97:502-514, Sep 2022. URL: https://doi.org/10.1111/cen.14817, doi:10.1111/cen.14817. This article has 77 citations and is from a peer-reviewed journal.

11. (geest2021monocarboxylatetransporter8 pages 5-6): Ferdy S. van Geest, Nilhan Gunhanlar, Stefan Groeneweg, and W. Edward Visser. Monocarboxylate transporter 8 deficiency: from pathophysiological understanding to therapy development. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.723750, doi:10.3389/fendo.2021.723750. This article has 42 citations.

12. (bauer2024unmetpatientneeds pages 5-6): Andrew J. Bauer, Bethany Auble, Amy L. Clark, Tina Y. Hu, Amber Isaza, Kyle P. McNerney, Daniel L. Metzger, Lindsey Nicol, Samuel R. Pierce, and Richard Sidlow. Unmet patient needs in monocarboxylate transporter 8 (mct8) deficiency: a review. Frontiers in Pediatrics, Jul 2024. URL: https://doi.org/10.3389/fped.2024.1444919, doi:10.3389/fped.2024.1444919. This article has 12 citations.

13. (geest2021monocarboxylatetransporter8 pages 10-11): Ferdy S. van Geest, Nilhan Gunhanlar, Stefan Groeneweg, and W. Edward Visser. Monocarboxylate transporter 8 deficiency: from pathophysiological understanding to therapy development. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.723750, doi:10.3389/fendo.2021.723750. This article has 42 citations.

14. (geest2021monocarboxylatetransporter8 pages 4-5): Ferdy S. van Geest, Nilhan Gunhanlar, Stefan Groeneweg, and W. Edward Visser. Monocarboxylate transporter 8 deficiency: from pathophysiological understanding to therapy development. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.723750, doi:10.3389/fendo.2021.723750. This article has 42 citations.

15. (salaslucia2024impairedt3uptake pages 1-2): Federico Salas-Lucia, Sergio Escamilla, Antonio C. Bianco, Alexandra Dumitrescu, and Samuel Refetoff. Impaired t3 uptake and action in mct8-deficient cerebral organoids underlie allan-herndon-dudley syndrome. JCI Insight, Feb 2024. URL: https://doi.org/10.1172/jci.insight.174645, doi:10.1172/jci.insight.174645. This article has 21 citations and is from a domain leading peer-reviewed journal.

16. (bauer2024unmetpatientneeds pages 3-5): Andrew J. Bauer, Bethany Auble, Amy L. Clark, Tina Y. Hu, Amber Isaza, Kyle P. McNerney, Daniel L. Metzger, Lindsey Nicol, Samuel R. Pierce, and Richard Sidlow. Unmet patient needs in monocarboxylate transporter 8 (mct8) deficiency: a review. Frontiers in Pediatrics, Jul 2024. URL: https://doi.org/10.3389/fped.2024.1444919, doi:10.3389/fped.2024.1444919. This article has 12 citations.

17. (bauer2024unmetpatientneeds pages 7-8): Andrew J. Bauer, Bethany Auble, Amy L. Clark, Tina Y. Hu, Amber Isaza, Kyle P. McNerney, Daniel L. Metzger, Lindsey Nicol, Samuel R. Pierce, and Richard Sidlow. Unmet patient needs in monocarboxylate transporter 8 (mct8) deficiency: a review. Frontiers in Pediatrics, Jul 2024. URL: https://doi.org/10.3389/fped.2024.1444919, doi:10.3389/fped.2024.1444919. This article has 12 citations.

18. (NCT02060474 chunk 2): W. Edward Visser. Thyroid Hormone Analog Therapy in MCT8 Deficiency: Triac Trial Patients. Erasmus Medical Center. 2014. ClinicalTrials.gov Identifier: NCT02060474

19. (NCT05911399 chunk 1):  Expanded Access Program for Tiratricol in Patients With Monocarboxylate Transporter 8 Deficiency. Rare Thyroid Therapeutics International AB. ClinicalTrials.gov Identifier: NCT05911399

20. (NCT05579327 chunk 1):  Withdrawal of Tiratricol Treatment in Males With Monocarboxylate Transporter 8 Deficiency (MCT8 Deficiency). Rare Thyroid Therapeutics International AB. 2023. ClinicalTrials.gov Identifier: NCT05579327

21. (NCT02396459 chunk 1):  Triac Trial II in MCT8 Deficiency Patients. Rare Thyroid Therapeutics International AB. 2020. ClinicalTrials.gov Identifier: NCT02396459

22. (geest2021monocarboxylatetransporter8 pages 7-9): Ferdy S. van Geest, Nilhan Gunhanlar, Stefan Groeneweg, and W. Edward Visser. Monocarboxylate transporter 8 deficiency: from pathophysiological understanding to therapy development. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.723750, doi:10.3389/fendo.2021.723750. This article has 42 citations.

23. (NCT05019417 chunk 1): Amnon Zung. Glycerol-Phenylbutyrate Treatment in Children With MCT Mutation (Allan-Herndon- Dudley Syndrome). Kaplan Medical Center. 2021. ClinicalTrials.gov Identifier: NCT05019417

24. (maitykumar2022validationofmct8oatp1c1 pages 8-9): Gandhari Maity-Kumar, Lisa Ständer, Meri DeAngelis, Sooyeon Lee, Anna Molenaar, Lore Becker, Lillian Garrett, Oana V. Amerie, Sabine M. Hoelter, Wolfgang Wurst, Helmut Fuchs, Annette Feuchtinger, Valerie Gailus-Durner, Cristina Garcia-Caceres, Ahmed E. Othman, Caroline Brockmann, Vanessa I. Schöffling, Katja Beiser, Heiko Krude, Piotr A. Mroz, Susanna Hofmann, Jan Tuckermann, Richard D. DiMarchi, Martin Hrabe de Angelis, Matthias H. Tschöp, Paul T. Pfluger, and Timo D. Müller. Validation of mct8/oatp1c1 dko mice as a model organism for the allan-herndon-dudley syndrome. Molecular Metabolism, 66:101616, Dec 2022. URL: https://doi.org/10.1016/j.molmet.2022.101616, doi:10.1016/j.molmet.2022.101616. This article has 14 citations and is from a domain leading peer-reviewed journal.

25. (maitykumar2022validationofmct8oatp1c1 pages 1-2): Gandhari Maity-Kumar, Lisa Ständer, Meri DeAngelis, Sooyeon Lee, Anna Molenaar, Lore Becker, Lillian Garrett, Oana V. Amerie, Sabine M. Hoelter, Wolfgang Wurst, Helmut Fuchs, Annette Feuchtinger, Valerie Gailus-Durner, Cristina Garcia-Caceres, Ahmed E. Othman, Caroline Brockmann, Vanessa I. Schöffling, Katja Beiser, Heiko Krude, Piotr A. Mroz, Susanna Hofmann, Jan Tuckermann, Richard D. DiMarchi, Martin Hrabe de Angelis, Matthias H. Tschöp, Paul T. Pfluger, and Timo D. Müller. Validation of mct8/oatp1c1 dko mice as a model organism for the allan-herndon-dudley syndrome. Molecular Metabolism, 66:101616, Dec 2022. URL: https://doi.org/10.1016/j.molmet.2022.101616, doi:10.1016/j.molmet.2022.101616. This article has 14 citations and is from a domain leading peer-reviewed journal.

26. (salaslucia2024impairedt3uptake pages 4-5): Federico Salas-Lucia, Sergio Escamilla, Antonio C. Bianco, Alexandra Dumitrescu, and Samuel Refetoff. Impaired t3 uptake and action in mct8-deficient cerebral organoids underlie allan-herndon-dudley syndrome. JCI Insight, Feb 2024. URL: https://doi.org/10.1172/jci.insight.174645, doi:10.1172/jci.insight.174645. This article has 21 citations and is from a domain leading peer-reviewed journal.

27. (NCT06060197 chunk 1):  MCT8 Deficiency Caregiver Study. Rare Thyroid Therapeutics International AB. 2022. ClinicalTrials.gov Identifier: NCT06060197

28. (bauer2024unmetpatientneeds pages 8-9): Andrew J. Bauer, Bethany Auble, Amy L. Clark, Tina Y. Hu, Amber Isaza, Kyle P. McNerney, Daniel L. Metzger, Lindsey Nicol, Samuel R. Pierce, and Richard Sidlow. Unmet patient needs in monocarboxylate transporter 8 (mct8) deficiency: a review. Frontiers in Pediatrics, Jul 2024. URL: https://doi.org/10.3389/fped.2024.1444919, doi:10.3389/fped.2024.1444919. This article has 12 citations.

29. (beheshti2022allanherndondudleysyndromea pages 1-2): Ramin Beheshti, Justen M. Aprile, and Charles Lee. Allan-herndon-dudley syndrome: a novel pathogenic variant of the slc16a2 gene. Cureus, Jan 2022. URL: https://doi.org/10.7759/cureus.21771, doi:10.7759/cureus.21771. This article has 8 citations.

30. (salaslucia2024impairedt3uptake pages 9-10): Federico Salas-Lucia, Sergio Escamilla, Antonio C. Bianco, Alexandra Dumitrescu, and Samuel Refetoff. Impaired t3 uptake and action in mct8-deficient cerebral organoids underlie allan-herndon-dudley syndrome. JCI Insight, Feb 2024. URL: https://doi.org/10.1172/jci.insight.174645, doi:10.1172/jci.insight.174645. This article has 21 citations and is from a domain leading peer-reviewed journal.

31. (NCT02060474 chunk 1): W. Edward Visser. Thyroid Hormone Analog Therapy in MCT8 Deficiency: Triac Trial Patients. Erasmus Medical Center. 2014. ClinicalTrials.gov Identifier: NCT02060474

32. (NCT02396459 chunk 2):  Triac Trial II in MCT8 Deficiency Patients. Rare Thyroid Therapeutics International AB. 2020. ClinicalTrials.gov Identifier: NCT02396459

33. (geest2021monocarboxylatetransporter8 pages 9-10): Ferdy S. van Geest, Nilhan Gunhanlar, Stefan Groeneweg, and W. Edward Visser. Monocarboxylate transporter 8 deficiency: from pathophysiological understanding to therapy development. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.723750, doi:10.3389/fendo.2021.723750. This article has 42 citations.

## Artifacts

- [Edison artifact artifact-00](Allan-Herndon-Dudley_Syndrome-deep-research-falcon_artifacts/artifact-00.md)