---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T18:09:45.858358'
end_time: '2026-08-01T18:20:31.120062'
duration_seconds: 645.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ZNF407-Related Neurodevelopmental Disorder
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: ZNF407-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ZNF407-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ZNF407-Related Neurodevelopmental Disorder** covering all of the
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
- **Disease Name:** ZNF407-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ZNF407-Related Neurodevelopmental Disorder** covering all of the
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


# ZNF407-Related Neurodevelopmental Disorder: Research Report

## Executive summary and evidence limits

ZNF407-related neurodevelopmental disorder is an ultra-rare, autosomal-recessive Mendelian disorder caused by biallelic pathogenic variants in **ZNF407**, which encodes a large C2H2 zinc-finger transcriptional regulator. Its best-supported clinical features are developmental delay/intellectual disability, severe speech and motor delay, postnatal short stature or failure to thrive, hypotonia, ocular abnormalities, characteristic facial dysmorphism, and variable distal-limb or orthopedic abnormalities. The foundational evidence is a 2014 report of two affected brothers; a 2020 publication expanded the allelic and phenotypic spectrum. Open Targets currently maps ZNF407 to **MONDO:0859198**, “short stature, impaired intellectual development, microcephaly, hypotonia, and ocular anomalies,” citing PMID **24907849**, PMID **32737394**, and newer evidence including PMID **39024449**. This MONDO term is presently the most specific retrievable identifier (kambouris2014mutationsinzinc pages 1-2, OpenTargets Search: -ZNF407).

The evidence base remains very small. Exact phenotype frequencies below therefore refer primarily to the original two-person family and should not be interpreted as population-level estimates. No disease-specific guideline, biomarker, natural-history registry, interventional trial, or validated neural animal/iPSC model was identified.

| domain | evidence-backed finding | suggested ontology terms/IDs | evidence type/strength |
|---|---|---|---|
| disease label | ZNF407-related neurodevelopmental disorder is an ultra-rare Mendelian disorder associated with biallelic pathogenic variation in **ZNF407**; Open Targets links ZNF407 to **MONDO:0859198 short stature, impaired intellectual development, microcephaly, hypotonia, and ocular anomalies** (OpenTargets Search: -ZNF407) | MONDO:0859198 | Human disease-gene aggregation + primary case report; moderate for disease validity, limited cohort size |
| inheritance | Available human evidence supports **autosomal recessive** inheritance with affected individuals homozygous for ZNF407 variants in a consanguineous family; unaffected relatives/carrier fetus were heterozygous or unaffected (kambouris2014mutationsinzinc pages 1-2, kambouris2014mutationsinzinc pages 2-4) | Autosomal recessive inheritance; biallelic ZNF407 | Primary human segregation evidence; strong within one pedigree |
| causal gene/variant | Foundational report identified **ZNF407 c.C5054G (p.S1685W)** at 18q23, absent from public variant databases available at the time and from 400 ethnically matched control chromosomes; later literature cited additional biallelic ZNF407 cases and other missense alleles (kambouris2014mutationsinzinc pages 1-2, kambouris2014mutationsinzinc pages 6-7, kambouris2014mutationsinzinc pages 4-6) | ZNF407 | Primary human molecular evidence for p.S1685W; expanded allelic spectrum supported by secondary/database evidence |
| neurodevelopmental phenotype | Severe developmental/cognitive disability was present in both reported brothers: delayed sitting, delayed independent walking, delayed/very limited speech, and lack of toilet training at assessment (kambouris2014mutationsinzinc pages 2-4) | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability; HP:0000750 Delayed speech and language development; HP:0001270 Motor delay | Primary human clinical evidence; strong for original family |
| growth phenotype | Both boys had postnatal growth restriction with height below the 3rd percentile and weight around the 3rd percentile; failure-to-thrive was emphasized in the abstract (kambouris2014mutationsinzinc pages 1-2, kambouris2014mutationsinzinc pages 2-4) | HP:0004322 Short stature; HP:0001508 Failure to thrive | Primary human clinical evidence; strong for 2/2 original cases |
| neurologic phenotype | Hypotonia with exaggerated deep tendon reflexes was reported in both affected individuals; gait was awkward with bent knees in the older child (kambouris2014mutationsinzinc pages 2-4) | HP:0001252 Hypotonia; HP:0006808 Increased deep tendon reflexes; HP:0002317 Unsteady gait | Primary human clinical evidence; strong for original family |
| ocular phenotype | Bilateral ptosis, epicanthic folds, and strabismus were reported; later disease naming also includes ocular anomalies (kambouris2014mutationsinzinc pages 2-4, OpenTargets Search: -ZNF407) | HP:0000508 Ptosis; HP:0000286 Epicanthus; HP:0000486 Strabismus | Primary human clinical evidence + curated disease aggregation; moderate |
| craniofacial phenotype | Recurrent facial dysmorphism included synophrys, midface hypoplasia, downturned mouth corners, thin upper vermilion border, and prominent ears with overfolding/absent lobules (kambouris2014mutationsinzinc pages 2-4, kambouris2014mutationsinzinc pages 1-2) | HP:0000664 Synophrys; HP:0000340 Short philtrum/not established; HP:0011800 Midface retrusion; HP:0002714 Downturned corners of mouth; HP:0010807 Thin upper vermilion border; HP:0000411 Prominent ear | Primary human clinical evidence; moderate-strong |
| musculoskeletal phenotype | Skeletal findings included bilateral 5th-finger camptodactyly, short 4th metatarsals with overriding toes, proximal thumb insertion, persistent fetal pads, limited knee mobility/awkward bent-knee gait, femoral subluxation, dysplastic acetabulum, and mild kyphosis (kambouris2014mutationsinzinc pages 1-2, kambouris2014mutationsinzinc pages 2-4) | HP:0004209 Camptodactyly of finger; HP:0010511 Short metatarsal; HP:0001841 2-4 toe syndactyly/not established; HP:0002808 Kyphosis; HP:0001382 Joint hypermobility/limited mobility not firmly assigned | Primary human clinical evidence; moderate |
| neuroimaging and ancillary testing | Brain MRI was normal in both reported cases; karyotype, array CGH, echocardiogram, abdominal ultrasound, and hearing testing were normal where performed (kambouris2014mutationsinzinc pages 2-4) | Normal brain MRI; no specific ontology term required | Primary human diagnostic evidence; moderate |
| molecular mechanism | The p.S1685W substitution lies in the linker between zinc fingers 18 and 19, disrupts an H-bond with E1683, increases linker flexibility, and is predicted to reduce zinc finger-DNA complex formation and downstream transcriptional control during fetal brain development (kambouris2014mutationsinzinc pages 1-2, kambouris2014mutationsinzinc pages 4-6, kambouris2014mutationsinzinc pages 6-7) | GO:0003700 DNA-binding transcription factor activity; GO:0006355 regulation of DNA-templated transcription | Primary in silico structural modeling anchored to human variant; moderate mechanistic evidence |
| gene/protein biology | ZNF407 is a multi-zinc-finger transcription factor with nuclear relevance; mRNA/protein expression was reported across multiple tissues including adult, embryonic, and fetal CNS/PNS in the 2014 paper (kambouris2014mutationsinzinc pages 6-7) | GO:0005634 nucleus; GO:0003677 DNA binding | Mixed evidence (human expression/database statements); moderate |
| ortholog/functional biology | Mouse **Zfp407** is nuclear in adipocytes, participates in a **PPARγ/RXRα** complex, and showed **7,313** ChIP-seq peaks, with ~50.4% overlap with PPARγ peaks and 64.8% overlap among the top 1,000 peaks; this supports transcription-factor function but is not a disease-specific neural model (charrier2024molecularregulationof pages 1-2, charrier2024molecularregulationof pages 2-4, charrier2024molecularregulationof pages 5-7) | GO:0005634 nucleus; GO:0006351 transcription, DNA-templated | Non-disease ortholog/cellular evidence; supportive but indirect for neurodevelopmental disorder |
| diagnosis | Best-supported diagnosis is genomic: exome/genome sequencing in patients with syndromic developmental delay/intellectual disability, followed by segregation testing; homozygosity mapping was informative in the consanguineous family, while karyotype/CMA/MRI were non-diagnostic in the original cases (kambouris2014mutationsinzinc pages 2-4, kambouris2014mutationsinzinc pages 1-2) | HP:0001263 Global developmental delay; ZNF407 single-gene analysis/WES | Primary human diagnostic workflow evidence; moderate |
| management | No disease-specific therapy or trials were identified. Current care is supportive: developmental therapies, rehabilitation, educational support, orthopedic monitoring/intervention as needed, and clinical genetics follow-up with reproductive counseling (kambouris2014mutationsinzinc pages 2-4) | Supportive care; genetic counseling | Inference from phenotype + absence of disease-specific interventional evidence; low-directness but clinically standard |
| prevention/family planning | Because evidence supports autosomal recessive inheritance, recurrence-risk counseling, carrier testing of relatives, prenatal diagnosis, and possibly preimplantation genetic testing are relevant where a familial pathogenic variant is known; prenatal testing identified an unaffected heterozygous fetus in the original pedigree (kambouris2014mutationsinzinc pages 2-4) | Genetic counseling; carrier testing; prenatal diagnosis | Primary pedigree evidence + standard Mendelian practice; moderate |
| epidemiology | No robust prevalence or incidence estimates were identified; evidence indicates an ultra-rare disorder with only a very small number of published families/patients (kambouris2014mutationsinzinc pages 1-2, OpenTargets Search: -ZNF407) | Rare disease | Sparse human literature; low |
| prognosis | Long-term natural history, survival, adult outcomes, penetrance, and genotype-phenotype correlations remain poorly defined; available childhood data suggest chronic, lifelong neurodevelopmental disability without evidence of neurodegeneration in the original report (kambouris2014mutationsinzinc pages 2-4) | Chronic neurodevelopmental disorder | Very limited longitudinal evidence; low |
| major evidence gaps | Major gaps include: lack of large cohorts, no validated prevalence estimates, no standardized diagnostic criteria, no disease-specific biomarkers, no neural iPSC/animal disease model, no treatment trials, and limited access to the 2020 expanded cohort details despite bibliographic confirmation (OpenTargets Search: -ZNF407) | Evidence gap annotation | Strong confidence in absence of evidence from searches; low for any omitted unpublished data |


*Table: This table condenses the strongest currently retrievable evidence for ZNF407-related neurodevelopmental disorder into knowledge-base-ready findings. It highlights core disease definition, inheritance, phenotype, mechanism, diagnostic approach, management, and the most important current evidence gaps.*

## 1. Disease information

### Definition and identifiers

The disorder is a syndromic neurodevelopmental condition in which biallelic ZNF407 dysfunction disrupts transcriptional regulation during development. The original designation was **“autosomal recessive cognitive impairment syndrome”**; subsequent usage includes **“ZNF407-related neurodevelopmental disorder,” “biallelic ZNF407 neurodevelopmental disorder,”** and the phenotype-based title **“short stature, impaired intellectual development, microcephaly, hypotonia, and ocular anomalies.”** The 2014 study described it as a “unique autosomal recessive cognitive impairment syndrome” (kambouris2014mutationsinzinc pages 1-2).

* **MONDO:** MONDO:0859198.
* **Gene:** ZNF407, zinc finger protein 407; Ensembl ENSG00000215421.
* **Cytogenetic location:** 18q23.
* **OMIM/Orphanet:** A separate confidently verified disease-number entry was not available in the retrieved evidence. The 2014 report was published in *Orphanet Journal of Rare Diseases*, but this does not itself establish an ORPHA identifier.
* **ICD-10/ICD-11:** No disease-specific code was identified. Coding would ordinarily use broader intellectual-developmental-disorder, developmental-delay, hypotonia, short-stature, or congenital-anomaly categories.
* **MeSH:** No dedicated disease heading was identified; broader headings include Intellectual Disability, Neurodevelopmental Disorders, and Zinc Finger Proteins.

Evidence is mainly **aggregated disease-level information derived from published, deeply phenotyped individual patients and families**, rather than EHR-scale cohorts. Open Targets provides an aggregated gene–disease association supported by literature and ClinVar records (OpenTargets Search: -ZNF407).

### Key primary publications

1. Kambouris et al., *Orphanet Journal of Rare Diseases*, published June 2014, DOI [10.1186/1750-1172-9-80](https://doi.org/10.1186/1750-1172-9-80), PMID **24907849**. Verbatim abstract conclusion: “**ZNF407 is a transcription factor with an essential role in brain development**” (kambouris2014mutationsinzinc pages 1-2).
2. Zahra et al., *Journal of Human Genetics*, published online July 2020, DOI [10.1038/s10038-020-0812-0](https://doi.org/10.1038/s10038-020-0812-0), PMID **32737394**. Its title documents the expanded phenotype: “**Biallelic ZNF407 mutations in a neurodevelopmental disorder with ID, short stature and variable microcephaly, hypotonia, ocular anomalies and facial dysmorphism**” (OpenTargets Search: -ZNF407).
3. Charrier et al., *PLOS ONE*, published May 23, 2024, DOI [10.1371/journal.pone.0294003](https://doi.org/10.1371/journal.pone.0294003). This is mechanistic ortholog evidence in adipocytes, not a clinical disease study (charrier2024molecularregulationof pages 1-2).

## 2. Etiology

### Causal factors and genetic risk

The established cause is **germline biallelic ZNF407 variation**, with autosomal-recessive segregation. In the original consanguineous Qatari family, both affected brothers were homozygous for **c.5054C>G, p.(Ser1685Trp)** as reported in the study’s transcript notation. The variant segregated with disease; an unaffected fetus identified by amniocentesis was heterozygous and remained unaffected after birth. The variant was absent from the then-current 1000 Genomes/dbSNP resources and from 400 ethnically matched control chromosomes (kambouris2014mutationsinzinc pages 4-6, kambouris2014mutationsinzinc pages 2-4).

Two heterozygous de novo variants, **p.(Tyr460Cys)** and **p.(Pro1195Ala)**, had been observed independently in patients with intellectual impairment, and a translocation disrupting intron 3 had been associated with reduced isoform-1 transcript, intellectual impairment, and autism. These observations support dosage sensitivity or broader allelic heterogeneity, but they do **not** establish that heterozygous variants cause the same recessive syndrome (kambouris2014mutationsinzinc pages 6-7).

Consanguinity increases the probability that two carriers of the same rare allele have an affected child, but it is not itself a biological cause. Family history of an affected sibling is the principal identifiable risk factor. For two heterozygous parents, the standard per-pregnancy probabilities are 25% affected, 50% carrier, and 25% unaffected/non-carrier, assuming complete penetrance of the familial pathogenic genotype.

### Environmental, infectious, and protective factors

No environmental toxin, lifestyle exposure, infectious agent, maternal-age effect, sex-specific susceptibility, or gene–environment interaction has been demonstrated. The original pregnancies and deliveries were described as uneventful, supporting a constitutional genetic rather than acquired cause (kambouris2014mutationsinzinc pages 2-4). No protective allele, diet, medication, or exposure has been validated. Avoiding consanguinity can lower the chance that partners share the same rare recessive allele at a population level, but it is not disease-specific biological protection.

## 3. Phenotypes

### Core phenotype and frequencies in the original family

Both reported brothers had severe developmental/cognitive disability, severe motor and speech delay, postnatal growth restriction, hypotonia with brisk reflexes, ptosis, epicanthal folds, synophrys, strabismus, midface hypoplasia, downturned mouth corners, a thin upper vermilion, and prominent abnormal ears. Thus, these findings were **2/2 in the original cohort**, but the denominator is too small for reliable syndrome-wide frequency estimates (kambouris2014mutationsinzinc pages 2-4).

* **Developmental delay/intellectual disability:** HP:0001263, HP:0001249. The older boy sat at 3 years, walked at 4–5 years, began very limited speech at 8 years, and had a Leiter-R Brief IQ of 36. The younger boy, aged 5, could sit but only attempted to pull to stand, babbled infrequently, and had severe impairment on the Vineland scale. Neither was toilet trained at assessment. Severity was severe and functionally consequential (kambouris2014mutationsinzinc pages 2-4).
* **Motor delay:** HP:0001270; **delayed walking:** HP:0002066. Pediatric onset, severe, apparently chronic.
* **Speech/language delay:** HP:0000750; **severely limited speech:** HP:0001344. Pediatric onset and severe.
* **Hypotonia:** HP:0001252; **hyperreflexia:** HP:0001347. Both were present in both brothers, indicating mixed central motor findings rather than a proven peripheral neuromuscular disorder (kambouris2014mutationsinzinc pages 2-4).
* **Short stature:** HP:0004322; **failure to thrive:** HP:0001508. At 11 years, height was 124 cm, below the third percentile, and weight 27 kg, at the third percentile. At 5 years, height was 95 cm, below the third percentile, and weight 15 kg, at the third percentile. Birth measurements were reportedly normal, suggesting postnatal growth restriction (kambouris2014mutationsinzinc pages 2-4).
* **Microcephaly:** HP:0000252. Head circumference was normal in the two original patients, while the 2020 disease description explicitly reports **variable microcephaly**. It is therefore not obligatory (kambouris2014mutationsinzinc pages 2-4, OpenTargets Search: -ZNF407).
* **Ptosis:** HP:0000508; **epicanthus:** HP:0000286; **strabismus:** HP:0000486. Bilateral and childhood-onset in both original cases.
* **Facial dysmorphism:** synophrys HP:0000664, midface retrusion/hypoplasia HP:0011800, downturned mouth corners HP:0002714, thin upper lip vermilion HP:0000219, prominent ears HP:0000411, and abnormal pinnae/earlobes. These are diagnostic clues, not pathognomonic findings (kambouris2014mutationsinzinc pages 1-2).
* **Camptodactyly:** HP:0012385, especially fifth finger; **short fourth metatarsal:** HP:0010743; **overriding toes:** HP:0001845; **persistent fetal pads:** HP:0011831; proximal thumb insertion and limited knee mobility were also described (kambouris2014mutationsinzinc pages 2-4).
* **Orthopedic abnormalities:** femoral/hip subluxation, acetabular dysplasia, and mild kyphosis occurred in the younger child; HP:0002827, HP:0008807, and HP:0002808 may be considered after patient-level verification (kambouris2014mutationsinzinc pages 2-4).
* **Gait abnormality:** HP:0001288. The older child walked awkwardly with bent knees.

### Negative or variable findings

Brain MRI was structurally normal in both brothers. Karyotype, array-CGH, echocardiography, and abdominal ultrasonography were normal; auditory evoked potentials were normal in the older child. No consistent seizures, biochemical abnormality, immune dysfunction, metabolic crisis, or organ failure was reported in the foundational family (kambouris2014mutationsinzinc pages 2-4).

### Quality-of-life impact

No EQ-5D, SF-36, PROMIS, or disease-specific QoL study exists. Nevertheless, the documented severe adaptive impairment, delayed mobility, minimal speech, and absent toilet independence imply major effects on communication, self-care, education, mobility, and caregiver burden. This is a clinical inference from functional data, not a validated QoL measurement (kambouris2014mutationsinzinc pages 2-4).

## 4. Genetic and molecular information

### Gene and protein

**ZNF407** encodes a large C2H2 zinc-finger protein. The 2014 canonical annotation described a 2,248-amino-acid, approximately 247-kDa protein containing 22 zinc fingers and three alternatively spliced isoforms. Isoform 3 lacks zinc fingers 18–22; consequently, p.S1685W affects two of the three described isoforms (kambouris2014mutationsinzinc pages 4-6).

Suggested annotations include **GO:0003700** DNA-binding transcription factor activity, **GO:0003677** DNA binding, **GO:0006355** regulation of DNA-templated transcription, **GO:0005634** nucleus, and **GO:0006357** regulation of transcription by RNA polymerase II. These should be treated as functional annotation suggestions rather than disease-specific experimentally validated GO assertions.

### Variant interpretation

The foundational p.S1685W allele is a **germline homozygous missense variant**. Evidence supporting pathogenicity includes segregation, rarity, conservation, damaging in-silico predictions, location in a functionally constrained zinc-finger linker, and structural modeling. No patient-derived transcriptional assay was reported, so the precise functional class is best described as **predicted loss or severe impairment of DNA-binding/transcriptional-regulatory function**, not definitively proven complete loss of function (kambouris2014mutationsinzinc pages 4-6, kambouris2014mutationsinzinc pages 6-7).

Current ClinVar classifications must be checked against the exact transcript and genome build at implementation time. Historical absence from databases should not be substituted for a current gnomAD frequency. The retrieved evidence did not provide a current gnomAD allele count or a comprehensive list of the 2020 cohort’s HGVS variants.

### Structural variation

A translocation breakpoint in intron 3 reportedly reduced ZNF407 isoform-1 transcript and was associated with nonsyndromic intellectual impairment and autism. Larger 18q23 deletions encompassing ZNF407 and neighboring genes have broader, contiguous-gene phenotypes, including congenital aural atresia; these should not be equated with the biallelic single-gene disorder (kambouris2014mutationsinzinc pages 6-7).

No validated modifier gene, protective allele, disease-specific DNA-methylation episignature, histone abnormality, or recurrent founder variant was identified.

## 5. Environmental information

No causal or modifying environmental exposure is established. Smoking, alcohol, diet, exercise, pollution, occupational exposures, radiation, and infection have no demonstrated role in this Mendelian syndrome. Open Targets lists other statistical associations involving ZNF407, including smoking behavior, but these are distinct traits and do not show that smoking contributes to the recessive neurodevelopmental disorder (OpenTargets Search: -ZNF407).

## 6. Mechanism and pathophysiology

### Disease-specific proposed causal chain

1. A biallelic damaging ZNF407 allele alters a conserved C2H2 zinc-finger region.
2. For p.S1685W, substitution in the linker between zinc fingers 18 and 19 abolishes an H-bond between Ser1685 and Glu1683.
3. Modeling predicts increased linker flexibility and poorer geometric positioning of adjacent fingers on DNA.
4. This is predicted to lower DNA-binding probability and compromise downstream zinc-finger function.
5. Altered transcription of ZNF407 target genes during fetal brain and somatic development is proposed to disturb neurodevelopment, growth, craniofacial patterning, ocular development, and musculoskeletal development.
6. The downstream clinical result is developmental/intellectual disability with hypotonia, growth restriction, dysmorphism, and variable congenital anomalies (kambouris2014mutationsinzinc pages 1-2, kambouris2014mutationsinzinc pages 4-6, kambouris2014mutationsinzinc pages 6-7).

Steps 1–3 have human genetic and structural-model support. Steps 4–6 remain biologically plausible but incompletely validated because the relevant neural target genes and cell types have not been experimentally defined.

### Cellular localization and 2024 mechanistic development

The 2014 report noted ZNF407 mRNA and protein expression across many tissues, including adult, embryonic, and fetal central and peripheral nervous systems, with nuclear and cytoplasmic staining. Tissue-specific expression of the affected isoforms was unknown (kambouris2014mutationsinzinc pages 6-7).

A 2024 study of the mouse ortholog **Zfp407** provided stronger biochemical evidence for transcriptional-cofactor function, albeit in adipocytes rather than neurons. ZFP407 localized to the nucleus, interacted with endogenous PPARγ/RXRα complexes, and produced 7,313 ChIP-seq peaks in differentiated 3T3-L1 cells. Overall, 50.4% of ZFP407 peaks overlapped PPARγ peaks, increasing to 64.8% among the top 1,000 peaks. The authors concluded that ZFP407 likely regulates PPARγ through direct complex formation. GEO accession: **GSE245861** (charrier2024molecularregulationof pages 4-5, charrier2024molecularregulationof pages 1-2, charrier2024molecularregulationof pages 5-7).

This 2024 work also supports roles in adipocyte differentiation, glucose transport, and lipid metabolism: earlier mouse studies summarized therein found that Zfp407 overexpression improved glucose homeostasis, whereas deficiency caused lipodystrophy and worsened insulin resistance. These findings are relevant to general protein biology but do not establish metabolic disease as a feature of affected children (charrier2024molecularregulationof pages 2-4).

### Suggested process, cell, and anatomy terms

* **GO:** GO:0006355 regulation of DNA-templated transcription; GO:0007399 nervous system development; GO:0007417 central nervous system development; GO:0048666 neuron development; GO:0005634 nucleus.
* **CL:** CL:0000540 neuron and CL:0000047 neuronal stem cell may be used as hypotheses for developmental mechanism; no disease-specific cell-type experiment validates them. CL:0000136 adipocyte is directly supported for the ortholog biochemical work.
* **UBERON:** UBERON:0000955 brain, UBERON:0001017 central nervous system, UBERON:0000019 camera-type eye, UBERON:0002107 liver or adipose annotations should not be assigned as diseased tissues without patient evidence.

No disease-specific neuronal transcriptome, proteome, metabolome, lipidome, single-cell atlas, spatial-transcriptomic study, CRISPR screen, or multi-omics integration was identified. No immune, inflammatory, degenerative, oxidative-stress, or metabolic-tissue-damage mechanism is established.

## 7. Anatomical structures affected

The primary affected system is the **nervous system**, inferred from severe neurodevelopmental dysfunction despite normal conventional MRI. Relevant sites are the brain/CNS (UBERON:0000955; UBERON:0001017), but no reproducible regional lesion or lateralization is known. Functional disruption likely occurs at cellular or circuit levels rather than producing a gross structural malformation detectable by routine MRI (kambouris2014mutationsinzinc pages 2-4).

Secondary developmental involvement includes the eyes/extraocular apparatus, craniofacial structures, distal limbs, hip/acetabulum, knees, and axial skeleton. Findings are generally bilateral—ptosis, epicanthi, strabismus, short fourth metatarsals, and some hand abnormalities—without known cerebral lateralization. At the subcellular level, the **nucleus** is the best-supported compartment for transcriptional function (GO:0005634), although older tissue staining also reported some cytoplasmic positivity (charrier2024molecularregulationof pages 5-7, kambouris2014mutationsinzinc pages 6-7).

## 8. Temporal development

Onset is congenital or early pediatric and likely begins prenatally at the molecular level. Birth growth parameters can be normal, while developmental delays and postnatal short stature become evident in infancy or childhood. The two original patients had severe milestone delay by early childhood (kambouris2014mutationsinzinc pages 2-4).

The available evidence is compatible with a **chronic, lifelong developmental encephalopathy**, not an acute, episodic, relapsing, or proven neurodegenerative condition. No formal disease stages, progression rate, remission pattern, or adult natural history have been defined. Early childhood is the most plausible intervention window for speech, motor, feeding, educational, and adaptive therapies because neurodevelopmental plasticity is greatest then, but no ZNF407-specific critical-period study exists.

## 9. Inheritance and population

Inheritance is autosomal recessive. Segregation in the original consanguineous family was strong: two affected homozygous brothers, heterozygous parents, and an unaffected heterozygous fetus/child (kambouris2014mutationsinzinc pages 2-4). Penetrance appears high for the reported biallelic genotype but cannot be quantified. Expressivity is variable, particularly for microcephaly and orthopedic findings. No anticipation is expected or reported. Germline mosaicism remains theoretically possible but has not been documented.

Prevalence, incidence, carrier frequency, founder effect, geographic distribution, and sex ratio are unknown. Published families include Middle Eastern/South Asian ancestry and consanguinity, but there is no evidence that the disorder is biologically restricted to any ethnicity. Both original patients were male; this is insufficient to infer sex bias. The absence of population estimates and the tiny literature indicate an ultra-rare disorder rather than a calculable prevalence (kambouris2014mutationsinzinc pages 1-2, OpenTargets Search: -ZNF407).

## 10. Diagnostics

### Recommended approach

Diagnosis requires identification of **biallelic pathogenic/likely pathogenic ZNF407 variants** compatible with phenotype and recessive inheritance.

1. Perform clinical assessment including growth, head circumference, developmental and adaptive testing, neurologic/ophthalmologic examination, dysmorphology, and musculoskeletal assessment.
2. Use trio **whole-exome sequencing** or **whole-genome sequencing**, or a comprehensive neurodevelopmental/intellectual-disability panel that includes ZNF407. WGS is preferable when exome sequencing is negative and a deep-intronic, regulatory, or structural variant is suspected.
3. Confirm candidate variants and phase by parental segregation testing. Homozygosity mapping is particularly useful in consanguineous families.
4. Apply current ACMG/AMP criteria with transcript-specific HGVS nomenclature and current ClinVar/gnomAD review.
5. Use chromosomal microarray to identify pathogenic CNVs or 18q abnormalities, but recognize that CMA will generally not detect single-nucleotide ZNF407 variants. The original patients had normal array-CGH and karyotypes (kambouris2014mutationsinzinc pages 2-4, kambouris2014mutationsinzinc pages 1-2).

Single-gene sequencing is reasonable for familial cascade/prenatal testing or when the phenotype and family history are highly specific. Karyotyping or FISH is reserved for suspected balanced rearrangement; mitochondrial and repeat-expansion tests are not specifically indicated. No diagnostic enzyme assay, metabolite, circulating protein, histopathologic signature, EEG pattern, or MRI biomarker is known.

RNA sequencing could theoretically demonstrate aberrant splicing or reduced transcript from splice/structural variants, but there is no validated disease assay or established accessible tissue. No methylation episignature or liquid biopsy is available.

### Differential diagnosis

Differentials include other recessive zinc-finger transcription-factor disorders—especially ZNF142-related disorder—as well as Coffin–Siris/BAF-complex disorders, Kabuki syndrome, KBG syndrome, White–Sutton syndrome, 18q deletion syndrome, congenital disorders with ptosis and camptodactyly, and nonspecific syndromic intellectual disability. Distinguishing evidence is the biallelic ZNF407 genotype; normal MRI and normal routine metabolic/cytogenetic investigations do not exclude the condition.

No population newborn screening is available. Cascade carrier testing is appropriate after establishing familial pathogenic variants.

## 11. Outcome and prognosis

No survival curve, mortality rate, life-expectancy estimate, or adult-outcome cohort exists. The original affected children were alive at ages 5 and 11. No life-threatening visceral involvement was identified in that family, but the sample is too small to conclude that life expectancy is normal (kambouris2014mutationsinzinc pages 2-4).

Expected morbidity centers on intellectual/adaptive disability, communication impairment, delayed or abnormal mobility, dependence in activities of daily living, short stature, visual/ocular problems, and orthopedic complications. Full neurodevelopmental recovery is unlikely, but functional gains may occur with therapy. No molecular prognostic biomarker or validated genotype–phenotype predictor exists. Variant class, residual isoform function, early developmental severity, mobility, feeding, and orthopedic burden are reasonable clinical considerations but remain unvalidated prognostic factors.

## 12. Treatment

There is no approved disease-modifying therapy, gene therapy, RNA therapy, cell therapy, or genotype-specific pharmacotherapy. The ClinicalTrials.gov search identified no relevant ZNF407 trial. Treatment is therefore multidisciplinary and symptom-directed:

* early developmental intervention and individualized education;
* speech-language therapy, including augmentative and alternative communication;
* physical therapy for hypotonia, delayed gait, contracture prevention, and balance;
* occupational therapy for fine motor skills, self-care, and adaptive equipment;
* ophthalmologic management of ptosis, strabismus, and refractive/visual problems;
* orthopedic surveillance for hip subluxation/dysplasia, kyphosis, camptodactyly, and limited joint mobility, with bracing or surgery when clinically indicated;
* nutritional and growth assessment, with feeding support if needed;
* standard symptomatic management of seizures, sleep, behavioral symptoms, constipation, or pain if these occur—none is a proven defining feature or ZNF407-specific drug target;
* clinical-genetics follow-up and family support.

Suggested NCIT intervention terms include **Genetic Counseling**, **Physical Therapy**, **Occupational Therapy**, **Speech and Language Therapy**, **Supportive Care**, and procedure-specific orthopedic or ophthalmic surgery terms. Exact NCIT codes should be validated against the current thesaurus release before ingestion. No response rates, adverse-event profiles, pharmacogenomic recommendations, or treatment algorithm have been published.

The adipocyte PPARγ/RXRα results should **not** be interpreted as evidence for thiazolidinediones in this disorder. The 2024 study was mechanistic and non-neural, and PPARγ agonists have recognized systemic adverse effects (charrier2024molecularregulationof pages 1-2, charrier2024molecularregulationof pages 2-4).

## 13. Prevention

Primary prevention by lifestyle change or vaccination is not applicable. For known carrier couples, reproductive options include genetic counseling, partner/carrier testing, preimplantation genetic testing for monogenic disease, chorionic-villus sampling or amniocentesis for targeted prenatal diagnosis, and use of donor gametes. The original study demonstrated practical prenatal diagnosis: amniocentesis identified a heterozygous fetus who was unaffected after birth (kambouris2014mutationsinzinc pages 2-4).

Secondary prevention consists of early molecular diagnosis and prompt developmental intervention. Tertiary prevention includes surveillance and therapy to reduce contractures, hip complications, communication deprivation, feeding/growth problems, and preventable visual impairment. Population carrier or newborn screening is not currently justified by available evidence.

## 14. Other species and natural disease

The human gene has a mouse ortholog, **Zfp407**; relevant taxonomy includes *Homo sapiens* NCBI Taxon 9606 and *Mus musculus* NCBI Taxon 10090. No naturally occurring veterinary ZNF407 syndrome, affected breed, zoonosis, or cross-species transmission phenomenon was identified. The condition is genetic and noninfectious, so zoonotic potential is not applicable.

Ortholog conservation supports a conserved transcriptional-regulatory function, but available mouse work primarily concerns adipocyte metabolism rather than a spontaneous neurodevelopmental phenotype (charrier2024molecularregulationof pages 4-5, charrier2024molecularregulationof pages 5-7).

## 15. Model organisms

### Available experimental systems

The clearest experimental system is mouse 3T3-L1 adipocytes expressing ZFP407. Co-immunoprecipitation, subcellular fractionation, reporter assays, mutagenesis, and ChIP-seq establish nuclear localization, PPARγ/RXRα complex participation, and extensive chromatin occupancy. The ChIP-seq dataset is available as GEO **GSE245861** (charrier2024molecularregulationof pages 4-5, charrier2024molecularregulationof pages 1-2, charrier2024molecularregulationof pages 5-7).

Mouse gain- and loss-of-function studies summarized in the 2024 paper show improved glucose homeostasis with overexpression and lipodystrophy/insulin resistance with deficiency. These models are suitable for studying transcriptional cofactor function and metabolism but do not currently recapitulate the human intellectual-disability, ocular, craniofacial, or skeletal syndrome (charrier2024molecularregulationof pages 2-4).

### Missing disease models and priorities

No validated Znf407 knock-in mouse carrying a human disease allele, neural conditional knockout, zebrafish model, Drosophila model, patient-derived iPSC neuron, cerebral organoid, or isogenic CRISPR model was identified. Priority models would include:

1. patient-derived and CRISPR-corrected iPSC cortical neurons/organoids;
2. p.S1685W knock-in mice or neural-progenitor conditional Zfp407 loss;
3. neuronal ChIP-seq/CUT&RUN and RNA-seq to identify direct developmental targets;
4. single-cell developmental profiling to identify vulnerable neural lineages;
5. rescue experiments comparing major human isoforms.

These would test the proposed chain from impaired zinc-finger DNA binding to altered neurodevelopmental transcription and clinical phenotype.

## Knowledge-base conclusions

The disease–gene relationship is supported by recessive human segregation, recurrence in later biallelic cases, variant rarity, and mechanistic plausibility. Nevertheless, pathogenic mechanisms remain incompletely established because the strongest disease-specific functional evidence is structural modeling rather than patient-derived neural experimentation. Phenotypic frequencies, penetrance, prognosis, and treatment effects should therefore be labeled **limited/unknown**, not inferred from two original patients. The 2024 ZFP407 work significantly advances understanding of protein function, but its adipocyte context makes it indirect evidence for neurodevelopmental pathophysiology (charrier2024molecularregulationof pages 1-2, charrier2024molecularregulationof pages 5-7).

### Evidence-source classification

* **Human clinical/genetic:** Kambouris et al. 2014, PMID 24907849; Zahra et al. 2020, PMID 32737394.
* **Structural computational:** homology modeling of p.S1685W in Kambouris et al. 2014.
* **Cellular/model-organism:** mouse ZFP407 experiments in 3T3-L1 adipocytes, Charrier et al. 2024.
* **Aggregated database:** Open Targets/ClinVar-linked disease associations, including MONDO:0859198.
* **Not available:** epidemiologic cohorts, longitudinal natural history, neural disease models, omics biomarkers, treatment trials, and disease-specific clinical guidelines.

References

1. (kambouris2014mutationsinzinc pages 1-2): Marios Kambouris, Rachid C Maroun, Tawfeg Ben-Omran, Yasser Al-Sarraj, Khaoula Errafii, Rehab Ali, Hala Boulos, Patrick A Curmi, and Hatem El-Shanti. Mutations in zinc finger 407 [znf407] cause a unique autosomal recessive cognitive impairment syndrome. Orphanet Journal of Rare Diseases, 9:80-80, Jun 2014. URL: https://doi.org/10.1186/1750-1172-9-80, doi:10.1186/1750-1172-9-80. This article has 21 citations and is from a peer-reviewed journal.

2. (OpenTargets Search: -ZNF407): Open Targets Query (-ZNF407, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (kambouris2014mutationsinzinc pages 2-4): Marios Kambouris, Rachid C Maroun, Tawfeg Ben-Omran, Yasser Al-Sarraj, Khaoula Errafii, Rehab Ali, Hala Boulos, Patrick A Curmi, and Hatem El-Shanti. Mutations in zinc finger 407 [znf407] cause a unique autosomal recessive cognitive impairment syndrome. Orphanet Journal of Rare Diseases, 9:80-80, Jun 2014. URL: https://doi.org/10.1186/1750-1172-9-80, doi:10.1186/1750-1172-9-80. This article has 21 citations and is from a peer-reviewed journal.

4. (kambouris2014mutationsinzinc pages 6-7): Marios Kambouris, Rachid C Maroun, Tawfeg Ben-Omran, Yasser Al-Sarraj, Khaoula Errafii, Rehab Ali, Hala Boulos, Patrick A Curmi, and Hatem El-Shanti. Mutations in zinc finger 407 [znf407] cause a unique autosomal recessive cognitive impairment syndrome. Orphanet Journal of Rare Diseases, 9:80-80, Jun 2014. URL: https://doi.org/10.1186/1750-1172-9-80, doi:10.1186/1750-1172-9-80. This article has 21 citations and is from a peer-reviewed journal.

5. (kambouris2014mutationsinzinc pages 4-6): Marios Kambouris, Rachid C Maroun, Tawfeg Ben-Omran, Yasser Al-Sarraj, Khaoula Errafii, Rehab Ali, Hala Boulos, Patrick A Curmi, and Hatem El-Shanti. Mutations in zinc finger 407 [znf407] cause a unique autosomal recessive cognitive impairment syndrome. Orphanet Journal of Rare Diseases, 9:80-80, Jun 2014. URL: https://doi.org/10.1186/1750-1172-9-80, doi:10.1186/1750-1172-9-80. This article has 21 citations and is from a peer-reviewed journal.

6. (charrier2024molecularregulationof pages 1-2): Alyssa Charrier, Jeremiah Ockunzzi, Leighanne Main, Siddharth V. Ghanta, and David A. Buchner. Molecular regulation of pparγ/rxrα signaling by the novel cofactor zfp407. PLOS ONE, 19:e0294003, May 2024. URL: https://doi.org/10.1371/journal.pone.0294003, doi:10.1371/journal.pone.0294003. This article has 5 citations and is from a peer-reviewed journal.

7. (charrier2024molecularregulationof pages 2-4): Alyssa Charrier, Jeremiah Ockunzzi, Leighanne Main, Siddharth V. Ghanta, and David A. Buchner. Molecular regulation of pparγ/rxrα signaling by the novel cofactor zfp407. PLOS ONE, 19:e0294003, May 2024. URL: https://doi.org/10.1371/journal.pone.0294003, doi:10.1371/journal.pone.0294003. This article has 5 citations and is from a peer-reviewed journal.

8. (charrier2024molecularregulationof pages 5-7): Alyssa Charrier, Jeremiah Ockunzzi, Leighanne Main, Siddharth V. Ghanta, and David A. Buchner. Molecular regulation of pparγ/rxrα signaling by the novel cofactor zfp407. PLOS ONE, 19:e0294003, May 2024. URL: https://doi.org/10.1371/journal.pone.0294003, doi:10.1371/journal.pone.0294003. This article has 5 citations and is from a peer-reviewed journal.

9. (charrier2024molecularregulationof pages 4-5): Alyssa Charrier, Jeremiah Ockunzzi, Leighanne Main, Siddharth V. Ghanta, and David A. Buchner. Molecular regulation of pparγ/rxrα signaling by the novel cofactor zfp407. PLOS ONE, 19:e0294003, May 2024. URL: https://doi.org/10.1371/journal.pone.0294003, doi:10.1371/journal.pone.0294003. This article has 5 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](ZNF407-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md)