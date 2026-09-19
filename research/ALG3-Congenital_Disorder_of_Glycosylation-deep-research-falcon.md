---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T12:44:10.168242'
end_time: '2026-08-01T12:51:28.156705'
duration_seconds: 437.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ALG3-congenital disorder of glycosylation
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
  path: ALG3-Congenital_Disorder_of_Glycosylation-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ALG3-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALG3-congenital disorder of glycosylation** covering all of the
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
- **Disease Name:** ALG3-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALG3-congenital disorder of glycosylation** covering all of the
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


# ALG3-congenital disorder of glycosylation: comprehensive disease-characteristics report

## Executive summary

ALG3-congenital disorder of glycosylation (ALG3-CDG) is an ultra-rare, autosomal-recessive disorder of endoplasmic-reticulum N-linked glycosylation caused by biallelic pathogenic variants in **ALG3**. Deficient ALG3 α-1,3-mannosyltransferase activity prevents normal extension of the dolichol-linked oligosaccharide beyond Man5GlcNAc2, producing truncated lipid-linked oligosaccharides, protein hypoglycosylation, and severe congenital multisystem disease. Neurologic, ocular, skeletal, feeding, growth, endocrine, immune, renal, cardiac, and coagulation abnormalities have all been documented. Approximately 40 affected individuals had been reported by the largest 2021 cohort, so frequency, survival, penetrance, and genotype–phenotype estimates remain imprecise. No disease-modifying treatment or ALG3-CDG-specific clinical trial was identified; management is supportive and surveillance-based. (alsharhan2021expandingthephenotype pages 3-5, alsharhan2021expandingthephenotype pages 6-8, alsharhan2021expandingthephenotype pages 1-3)

The following table summarizes the most actionable knowledge-base annotations.

| Domain | Knowledge-base finding | Quantitative evidence | Suggested ontology terms | Evidence type/source |
|---|---|---|---|---|
| Disease identifiers | Rare Mendelian CDG caused by ALG3 deficiency; also called ALG3-CDG, CDG-Id, CDGS-IV/CDBS-IV; MONDO disease-target association available | ~40 reported individuals by 2021; first reported in 1995 (alsharhan2021expandingthephenotype pages 3-5, alsharhan2021expandingthephenotype pages 6-8, himmelreich2019novelvariantsand pages 1-2, OpenTargets Search: ALG3-congenital disorder of glycosylation-ALG3) | MONDO:0010998; congenital disorder of glycosylation; autosomal recessive inheritance (HP:0000007) | Human cohort/review + Open Targets disease record (alsharhan2021expandingthephenotype pages 3-5, himmelreich2019novelvariantsand pages 1-2, OpenTargets Search: ALG3-congenital disorder of glycosylation-ALG3) |
| Inheritance / etiology | Primary cause is biallelic germline pathogenic variants in ALG3 encoding ER alpha-1,3-mannosyltransferase | 11 novel variants in 10 new individuals in 2021 cohort; 4 additional biochemically confirmed variants in 2019 cohort (alsharhan2021expandingthephenotype pages 3-5, himmelreich2019novelvariantsand pages 1-2) | ALG3; protein N-linked glycosylation (GO:0006487); endoplasmic reticulum membrane | Human molecular genetics (alsharhan2021expandingthephenotype pages 3-5, himmelreich2019novelvariantsand pages 1-2) |
| Hallmark neurologic phenotype | Severe multisystem disease with prominent neurologic involvement including epilepsy, microcephaly, hypotonia, developmental delay/intellectual disability | Nijmegen scores averaged 31 in 8 evaluated individuals; seizures often intractable (alsharhan2021expandingthephenotype pages 6-8, alsharhan2021expandingthephenotype pages 5-6) | Seizure (HP:0001250); Microcephaly (HP:0000252); Hypotonia (HP:0001252); Global developmental delay (HP:0001263); Intellectual disability (HP:0001249) | Human cohort/case series (alsharhan2021expandingthephenotype pages 3-5, alsharhan2021expandingthephenotype pages 6-8, alsharhan2021expandingthephenotype pages 5-6) |
| Ocular phenotype | Frequent ophthalmic disease including strabismus/optic atrophy; severe cases may include retinal ganglion cell loss, optic nerve hypoplasia, cataracts, chorioretinal dystrophy | Ocular findings described as among most frequent in cohort; optic nerve hypoplasia highlighted in literature review (alsharhan2021expandingthephenotype pages 5-6, farolfi2021alg3cdgapatient pages 4-5) | Strabismus (HP:0000486); Optic atrophy (HP:0000648); Optic nerve hypoplasia (HP:0000609); Congenital cataract (HP:0000519); Nystagmus (HP:0000639) | Human case series/case report (alsharhan2021expandingthephenotype pages 5-6, farolfi2021alg3cdgapatient pages 4-5) |
| Skeletal / congenital anomalies | Skeletal anomalies and contractures are common; clubfeet, scoliosis, arthrogryposis, hip dysplasia reported | Skeletal abnormalities in 8/10 in 2021 cohort (alsharhan2021expandingthephenotype pages 5-6) | Arthrogryposis multiplex congenita (HP:0002804); Talipes equinovarus (HP:0001762); Scoliosis (HP:0002650); Joint contracture (HP:0001371) | Human cohort (alsharhan2021expandingthephenotype pages 5-6) |
| Feeding / GI / growth | Feeding difficulties and failure to thrive are common; some require tube feeding | GI problems in 8/10; feeding difficulties 6/8; failure to thrive 4/8; tube feeding 3/8 (alsharhan2021expandingthephenotype pages 5-6) | Feeding difficulties (HP:0011968); Failure to thrive (HP:0001508) | Human cohort (alsharhan2021expandingthephenotype pages 5-6) |
| Expanded phenotype | Endocrine, immunologic, renal, cardiac, and neural tube defect features broaden current disease understanding | Endocrine abnormalities in >50%; recurrent infections/immunodeficiency in 75% (6/8); mild aortic root dilatation in 4 subjects; renal anomalies reported (alsharhan2021expandingthephenotype pages 6-8, alsharhan2021expandingthephenotype pages 1-3) | Hypothyroidism (HP:0000821); Adrenal insufficiency (HP:0000846); Immunodeficiency (HP:0002721); Recurrent infections (HP:0002719); Aortic root dilatation (HP:0002616); Renal cyst (HP:0000107) | Human cohort (alsharhan2021expandingthephenotype pages 6-8, alsharhan2021expandingthephenotype pages 1-3) |
| Biochemical mechanism | Loss of ALG3 function blocks addition of mannose to Man5GlcNAc2-PP-dolichol in ER, causing substrate accumulation and truncated LLOs with deficient N-glycan extension | Accumulation of Man5GlcNAc2-PP-dolichol; reduced mature Glc3Man9GlcNAc2-PP-dolichol; reduced Man9GlcNAc2 and increased Man0-4GlcNAc2 in plasma (himmelreich2019novelvariantsand pages 1-2, himmelreich2019novelvariantsand pages 6-7, alsharhan2021expandingthephenotype pages 5-6) | Protein N-linked glycosylation (GO:0006487); dolichol-linked oligosaccharide biosynthetic process; endoplasmic reticulum (GO:0005783) | Human biochemical/molecular studies (himmelreich2019novelvariantsand pages 1-2, himmelreich2019novelvariantsand pages 6-7, alsharhan2021expandingthephenotype pages 5-6) |
| Diagnostic biomarkers | Type I carbohydrate-deficient transferrin profile is a key screen; plasma N-glycan profiling shows a pattern considered distinctive for ALG3-CDG | Elevated disialotransferrin 24.12 ± 0.41% (normal 5.0-13.5%) and reduced tetrasialotransferrin 26.9 ± 1.24% (normal 30.0-55.0%) in 2019 cohort; increased mono:di-glycosylated ratio in 2021 cohort (himmelreich2019novelvariantsand pages 6-7, alsharhan2021expandingthephenotype pages 5-6) | Abnormal transferrin glycosylation; carbohydrate-deficient transferrin; N-glycan biosynthetic defect | Human clinical biochemistry (himmelreich2019novelvariantsand pages 6-7, alsharhan2021expandingthephenotype pages 5-6, alsharhan2021expandingthephenotype pages 1-3) |
| Diagnostic methods | Diagnosis is established by molecular testing plus biochemical confirmation; useful methods include serum transferrin IEF/capillary electrophoresis, plasma protein N-glycan MS, and LLO analysis | Diagnostic delay of 4-33 years in 50% of cases in one cohort (alsharhan2021expandingthephenotype pages 5-6) | Whole exome sequencing; gene panel testing; serum transferrin isoelectric focusing | Human clinical diagnostics (alsharhan2021expandingthephenotype pages 3-5, himmelreich2019novelvariantsand pages 1-2, alsharhan2021expandingthephenotype pages 5-6, alsharhan2021expandingthephenotype pages 10-11) |
| Management | No curative disease-specific therapy established; care is supportive and multidisciplinary with recommended baseline endocrine, renal, cardiac, and immunologic evaluation | Hormone replacement used in 2 subjects; PT/OT used for contractures; seizures often refractory to multiple AEDs; ketogenic diet noted as successful in affected twins in cited literature (alsharhan2021expandingthephenotype pages 6-8, alsharhan2021expandingthephenotype pages 5-6, alsharhan2021expandingthephenotype pages 10-11) | Supportive care; physical therapy; occupational therapy; antiepileptic therapy | Human cohort/case-based management evidence (alsharhan2021expandingthephenotype pages 6-8, alsharhan2021expandingthephenotype pages 5-6, alsharhan2021expandingthephenotype pages 10-11) |
| Prognosis / mortality | Course is congenital and often severe, but survival into adulthood is possible with variable neurodevelopment; early lethality occurs in a subset | 3 deaths reported among 10 newly described individuals in 2021 article context (stillbirth, neonatal death, death at 1 year from multiorgan failure); one review/case paper states almost half die before or during neonatal period (alsharhan2021expandingthephenotype pages 3-5, farolfi2021alg3cdgapatient pages 4-5) | Multisystem disorder; developmental disability | Human cohort/case report (alsharhan2021expandingthephenotype pages 3-5, farolfi2021alg3cdgapatient pages 4-5) |
| Recent developments (2023-2024) | Broader CDG field emphasizes multi-omics and unmet need for targeted therapies; 2024 sources suggest cardiac screening relevance and preclinical glycosylation-directed therapy, but not validated ALG3-specific treatment | 2023 review: 163 CDG genetic defects / 193 phenotypes; no ALG3-specific interventional trial retrieved; one 2024 cardiomyopathy paper included a patient with ALG3-CDG (search results) (OpenTargets Search: ALG3-congenital disorder of glycosylation-ALG3) | Multi-omics; natural history; cardiomyopathy screening | Authoritative review/Open Targets + targeted literature search (OpenTargets Search: ALG3-congenital disorder of glycosylation-ALG3) |
| Evidence gaps | No established environmental or infectious causes, no confirmed protective factors, no robust penetrance estimates, no validated natural-history registry specific to ALG3-CDG, and no clearly established animal model/natural disease in other species retrieved here | Clinical trials search returned no relevant ALG3-specific interventional trials; model-organism evidence in retrieved set was indirect/general rather than validated ALG3-specific disease model | Not available / not established | Explicit gap from targeted searches and available evidence set (OpenTargets Search: ALG3-congenital disorder of glycosylation-ALG3) |


*Table: This table condenses the most actionable knowledge-base facts for ALG3-congenital disorder of glycosylation, including identifiers, core phenotypes, molecular mechanism, diagnostics, management, prognosis, and key evidence gaps. It is designed to support structured disease annotation while keeping direct human evidence separate from broader CDG context.*

## Evidence framework and limitations

Claims below are labeled by evidence type: **human clinical**, **human biochemical**, **cellular/in vitro**, or **general CDG evidence**. The strongest disease-specific evidence comes from small case series published in 2019 and 2021. The most recent ALG3-specific mechanistic paper found in the search was a 2024 study of deficient glycan extension and ER stress, but its full text was unavailable to the evidence extractor; it is therefore identified as an emerging source rather than used for unsupported quantitative claims. No robust population cohort, randomized trial, validated ALG3-specific quality-of-life instrument, or disease-specific natural-history registry analysis was retrieved.

---

## 1. Disease information

### Definition

ALG3-CDG is a monogenic congenital disorder of N-glycosylation. The disease results from loss of ALG3-dependent addition of mannose to the dolichol-linked Man5GlcNAc2 precursor in the ER. The resulting generalized protein hypoglycosylation produces a predominantly neurodevelopmental but broadly multisystem phenotype. (alsharhan2021expandingthephenotype pages 3-5, himmelreich2019novelvariantsand pages 1-2)

### Identifiers and names

- **MONDO:** **MONDO:0010998**.
- **OMIM phenotype:** **601110**, reported in the ALG3-CDG literature. This should not be confused with the separate gene-entry identifier used by some databases. (alsharhan2021expandingthephenotype pages 3-5)
- **Gene:** **ALG3**, Ensembl **ENSG00000214160**; approved name “ALG3 alpha-1,3-mannosyltransferase.” Open Targets associates this single target with MONDO:0010998. (OpenTargets Search: ALG3-congenital disorder of glycosylation-ALG3)
- **Common names:** ALG3-CDG; congenital disorder of glycosylation type Id; CDG-Id; CDGS-IV; carbohydrate-deficient glycoprotein syndrome type IV; CDBS-IV. (alsharhan2021expandingthephenotype pages 3-5, himmelreich2019novelvariantsand pages 1-2)
- **Orphanet, MeSH, ICD-10/ICD-11:** a disease-specific code was not verified in the retrieved evidence. In clinical coding, it may fall under broader congenital glycosylation/metabolic-disorder categories; a database implementation should not assign an unverified specific code.

The evidence is **aggregated disease-level literature**, supplemented by individual case and family reports. It is not derived from a population-scale EHR dataset.

### Key abstract quotation

The largest disease-specific series states: “Individuals with ALG3-CDG frequently exhibit severe neurological involvement (epilepsy, microcephaly, and hypotonia), ocular anomalies, dysmorphic features, skeletal anomalies, and feeding difficulties.” Alsharhan et al., *Journal of Inherited Metabolic Disease*, published March 2021, DOI: https://doi.org/10.1002/jimd.12367. (alsharhan2021expandingthephenotype pages 1-3)

---

## 2. Etiology

### Causal factor

The primary cause is **biallelic germline pathogenic or likely pathogenic ALG3 variants**, producing autosomal-recessive deficiency of ER α-1,3-mannosyltransferase. Variant classes include missense, nonsense, frameshift, and splice-region variants. Reported pathogenic changes are enriched in predicted transmembrane regions, consistent with disruption of an integral ER membrane enzyme. (alsharhan2021expandingthephenotype pages 3-5, himmelreich2019novelvariantsand pages 1-2)

Illustrative biochemically confirmed variants include **c.350G>C (p.Arg117Pro), c.1263G>A (p.Trp421Ter), c.1037A>G (p.Asn346Ser), c.296+4A>G**, and **c.160_196del**. Another patient carried variants in trans, **c.116del p.(Pro39Argfs*40)** and **c.1060C>T p.(Arg354Cys)**, classified as pathogenic under ACMG criteria in that report. (himmelreich2019novelvariantsand pages 1-2, farolfi2021alg3cdgapatient pages 4-5)

### Risk factors

- **Established genetic risk:** two disease-causing ALG3 alleles; parental consanguinity increases the probability of homozygosity in autosomal-recessive families.
- **Family history:** affected siblings or known carrier parents confer the expected Mendelian recurrence risk.
- **Environmental, lifestyle, occupational, infectious, age, or sex risk factors:** none established. These factors do not cause the inherited enzymatic defect.
- **Modifier genes:** none validated.
- **Somatic causation:** not supported; the reported disease alleles are constitutional/germline.

### Protective factors and gene–environment interaction

No protective allele, diet, exposure, or reproducible gene–environment interaction has been established. Supportive nutrition may reduce secondary malnutrition but does not correct the primary glycosylation defect. Environmental modifiers of seizure burden, infection frequency, or nutritional status may affect morbidity, but these are not proven disease-specific interactions.

---

## 3. Phenotypes

Phenotype estimates are vulnerable to ascertainment bias and small denominators. Onset is generally prenatal, neonatal, or early infantile, although diagnosis may be delayed into adulthood.

### Neurologic and developmental

- **Global developmental delay/intellectual disability**—usually severe but variable; some adults in one cohort had neurocognitive abilities corresponding approximately to ages 7–9 years. Suggested terms: **HP:0001263**, **HP:0001249**.
- **Epilepsy**, often nonfebrile and drug-resistant; multiple antiseizure medications and sometimes ketogenic diet have been used. **HP:0001250**.
- **Hypotonia**, sometimes with later hypertonia. **HP:0001252**; hypertonia **HP:0001276**.
- **Microcephaly.** **HP:0000252**.
- **Brain abnormalities:** cortical atrophy, cerebellar vermis hypoplasia, and neural-tube defects have been reported. Suggested terms: cerebral cortical atrophy **HP:0002120**; cerebellar vermis hypoplasia **HP:0001320**; neural-tube defect **HP:0045005**.

The mean Nijmegen CDG severity score was **31**, in the severe range, among eight assessed individuals in the 2021 cohort. (alsharhan2021expandingthephenotype pages 6-8, alsharhan2021expandingthephenotype pages 5-6)

### Ophthalmic

Strabismus and optic atrophy are prominent. Optic-nerve hypoplasia, retinal ganglion-cell loss, inner-retinal thinning, nystagmus, congenital cataracts, corneal opacity, chorioretinal dystrophy, and severe visual impairment have also been described. Suggested HPO terms include **HP:0000486** (strabismus), **HP:0000648** (optic atrophy), **HP:0000609** (optic-nerve hypoplasia), **HP:0000519** (congenital cataract), and **HP:0000639** (nystagmus). (alsharhan2021expandingthephenotype pages 5-6, farolfi2021alg3cdgapatient pages 4-5)

### Musculoskeletal and congenital anomalies

Skeletal abnormalities occurred in **8/10** members of the 2021 cohort. Findings include arthrogryposis, joint contractures, clubfeet/talipes, scoliosis, and hip dysplasia. Suggested terms: **HP:0002804**, **HP:0001371**, **HP:0001762**, **HP:0002650**, and **HP:0001385**. These manifestations may be congenital and can materially limit mobility and activities of daily living. (alsharhan2021expandingthephenotype pages 5-6)

### Feeding, gastrointestinal, and growth

Gastrointestinal or feeding problems affected **8/10**; among eight with detailed data, **6/8** had feeding difficulty, **4/8** failure to thrive, and **3/8** required tube feeding. Suggested terms: feeding difficulty **HP:0011968**, failure to thrive **HP:0001508**, and tube feeding dependence where applicable. (alsharhan2021expandingthephenotype pages 5-6)

### Endocrine, immune, renal, cardiac, and hematologic

- Endocrine abnormalities occurred in **more than half** of the 2021 cohort and included central hypothyroidism, adrenal insufficiency, growth-hormone deficiency, panhypopituitarism, and hypoglycemia. Suggested terms: **HP:0000821**, **HP:0000846**, **HP:0000824**, and **HP:0001943**. Hormone replacement was required in affected individuals. (alsharhan2021expandingthephenotype pages 6-8, alsharhan2021expandingthephenotype pages 5-6)
- Recurrent infections or immunodeficiency occurred in **6/8 (75%)** of sufficiently characterized subjects. Suggested terms: **HP:0002719** and **HP:0002721**. (alsharhan2021expandingthephenotype pages 6-8)
- Renal findings include nephromegaly, cystic kidneys, and duplex kidney. Suggested terms include nephromegaly **HP:0000105**, renal cyst **HP:0000107**, and duplex collecting system where applicable. (alsharhan2021expandingthephenotype pages 6-8)
- Mild aortic-root dilatation was reported in **four subjects**; cardiomyopathy and vascular-anatomy abnormalities have also been reported. Suggested term: **HP:0002616**. (alsharhan2021expandingthephenotype pages 6-8, himmelreich2019novelvariantsand pages 1-2)
- Coagulation abnormalities include low antithrombin III, reduced factor XI, prolonged activated partial thromboplastin time, and other glycoprotein-related abnormalities. (alsharhan2021expandingthephenotype pages 5-6)

### Quality of life

No ALG3-CDG-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study was retrieved. Nevertheless, severe developmental disability, refractory epilepsy, visual impairment, feeding-tube dependence, contractures, recurrent infections, and multispecialty surveillance imply major effects on independence, education, mobility, communication, family caregiving, and health-care utilization.

---

## 4. Genetic and molecular information

**ALG3** encodes a 438-amino-acid, approximately **50.1-kDa**, integral ER membrane α-1,3-mannosyltransferase. It is the first dolichol-phosphate-mannose-dependent mannosyltransferase acting on the luminal phase of N-glycan precursor assembly. (himmelreich2019novelvariantsand pages 1-2)

Reported disease alleles include missense, nonsense, frameshift, deletion, and splice-region variants. Functional consequences are predominantly **loss of function or marked reduction in enzymatic competence**, although measured ALG3 protein abundance can vary and protein quantity alone does not establish normal catalytic function. In the 2019 study, patient-specific protein abundance ranged from **14.3% to 122.4% of control**, illustrating that pathogenicity may reflect abnormal structure or catalytic activity rather than simple absence. (himmelreich2019novelvariantsand pages 6-7)

The 2021 cohort added **11 novel variants in 10 individuals**, and the 2019 study added four biochemically confirmed variants. Population allele frequencies were not available in the extracted evidence; disease-causing alleles are expected to be rare, but each variant should be checked directly in the current gnomAD release before knowledge-base ingestion. (alsharhan2021expandingthephenotype pages 3-5, himmelreich2019novelvariantsand pages 1-2)

No validated modifier gene, disease-specific methylation signature, recurrent pathogenic chromosomal rearrangement, anticipation mechanism, or repeat expansion has been established. Large deletions involving ALG3 could theoretically cause disease if biallelic or paired with a pathogenic sequence variant, but this was not demonstrated in the retrieved cohort evidence.

---

## 5. Environmental information

ALG3-CDG is not caused by toxins, radiation, pollution, occupation, smoking, alcohol, diet, or infection. No infectious trigger or zoonotic transmission exists. Diet and medical exposures can alter secondary complications—for example nutritional status or seizure control—but do not create or reverse the congenital enzymatic lesion. Thus, environmental and lifestyle fields should be annotated **“not established as etiologic”**, not “absent in every patient.”

---

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. **Biallelic ALG3 dysfunction** reduces ER α-1,3-mannosyltransferase activity.
2. ALG3 fails to transfer mannose from dolichol-phosphate-mannose to **Man5GlcNAc2-PP-dolichol**.
3. Man5GlcNAc2-PP-dolichol accumulates, while mature **Glc3Man9GlcNAc2-PP-dolichol** falls.
4. The oligosaccharyltransferase system receives an undersized precursor, resulting in inefficient site occupancy and transfer of truncated glycans.
5. Plasma and cellular glycoproteins show hypoglycosylation and deficient extension beyond Man5GlcNAc2.
6. Dysfunction of many glycoproteins across developing brain, eye, endocrine organs, skeleton, immune system, liver/coagulation system, kidney, and heart produces the multisystem phenotype. (alsharhan2021expandingthephenotype pages 3-5, himmelreich2019novelvariantsand pages 1-2, himmelreich2019novelvariantsand pages 6-7)

No normal pathway can extend the ALG3-deficient precursor to Man8GlcNAc2 or Man9GlcNAc2 without the missing ALG3 reaction. Plasma studies accordingly show reduced Man9GlcNAc2 and altered small high-mannose species. (alsharhan2021expandingthephenotype pages 6-8, alsharhan2021expandingthephenotype pages 5-6)

### Downstream cellular processes

The best-supported processes are defective protein N-linked glycosylation, impaired glycoprotein folding/trafficking, and altered glycoprotein stability or function. A 2024 study titled *Deficient glycan extension and endoplasmic reticulum stresses in ALG3-CDG* identifies ER stress as an active recent research direction, but quantitative findings were not available in the retrieved full-text evidence and should not yet be converted into patient-level frequency claims.

Suggested GO annotations include:

- **GO:0006487**—protein N-linked glycosylation;
- **GO:0005783**—endoplasmic reticulum;
- ER membrane and dolichol-linked oligosaccharide biosynthetic process;
- protein folding and ER quality-control processes, where supported experimentally.

Relevant cell types are broad rather than a uniquely targeted lineage. Suggested CL labels include neuron, retinal ganglion cell, skeletal muscle cell/myocyte, chondrocyte, hepatocyte, endocrine cell, renal epithelial cell, cardiomyocyte, and immune lymphoid/myeloid cells. These are mechanistic annotation suggestions based on affected tissues; direct single-cell validation is lacking.

### Molecular profiling and advanced technology

Plasma N-glycomics is the strongest disease-specific molecular-profile evidence: increased small high-mannose species, reduced Man9GlcNAc2, and combined deficiency of hybrid glycans/glycan extension beyond Man5GlcNAc2 were described as distinctive for ALG3-CDG. No disease-specific single-cell RNA sequencing, spatial transcriptomics, lipidomics, integrated multi-omics, organoid, or CRISPR-screen dataset was retrieved. (alsharhan2021expandingthephenotype pages 1-3, alsharhan2021expandingthephenotype pages 5-6)

---

## 7. Anatomical structures affected

### Organ and system level

- **Central nervous system:** cerebral cortex, cerebellar vermis, and broader developing brain.
- **Eye and visual pathways:** retina, retinal ganglion cells, optic nerve/anterior optic pathways, lens, cornea, and ocular motor apparatus.
- **Musculoskeletal system:** joints, spine, feet, hips, skeletal muscle, and connective tissues.
- **Endocrine system:** hypothalamic-pituitary axes, thyroid, adrenal, and growth-regulatory pathways.
- **Gastrointestinal/nutritional system:** oropharyngeal feeding function and growth.
- **Immune/hematologic system:** immunoglobulin/immune function and glycosylated coagulation proteins.
- **Kidney and urinary tract:** renal parenchyma and collecting-system development.
- **Cardiovascular system:** aortic root, myocardium, and vascular anatomy. (alsharhan2021expandingthephenotype pages 6-8, himmelreich2019novelvariantsand pages 1-2, farolfi2021alg3cdgapatient pages 4-5)

Suggested UBERON labels include brain (**UBERON:0000955**), cerebral cortex (**UBERON:0000956**), cerebellum (**UBERON:0002037**), eye (**UBERON:0000970**), retina (**UBERON:0000966**), optic nerve (**UBERON:0000941**), kidney (**UBERON:0002113**), heart (**UBERON:0000948**), and pituitary gland (**UBERON:0000007**).

### Subcellular localization

The primary compartment is the **endoplasmic-reticulum membrane**; the affected substrate is a dolichol-linked oligosaccharide assembled on the ER membrane. Lateralization is generally bilateral/systemic rather than intrinsically unilateral.

---

## 8. Temporal development

ALG3-CDG is **congenital**, with pathogenic glycosylation impairment present from embryonic development. Prenatal or neonatal manifestations may include neural-tube defects, congenital contractures, clubfeet, dysmorphism, ocular abnormalities, growth problems, or neonatal multisystem failure. Neurologic and feeding abnormalities usually become apparent in infancy or early childhood.

The course is chronic and lifelong among survivors. Developmental impairment may remain severe; epilepsy can be persistent and refractory; orthopedic contractures and scoliosis may progress; endocrine, immune, renal, and cardiac abnormalities may be detected later through surveillance. Diagnosis was delayed by **4–33 years in 50%** of one cohort, demonstrating that congenital onset does not ensure early recognition. (alsharhan2021expandingthephenotype pages 5-6)

No validated disease stages, remission pattern, or quantitative progression model exists. The prenatal and early postnatal periods are critical because glycosylation is essential to organogenesis, while early childhood offers a practical window for seizure treatment, nutritional support, hormone replacement, visual assessment, and prevention of orthopedic complications.

---

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two confirmed heterozygous carrier parents, each pregnancy has the standard 25% affected, 50% carrier, and 25% unaffected/non-carrier probabilities, assuming both variants are fully disease-causing.

By 2021, the literature contained approximately **40 reported individuals**; a separate ophthalmic review counted **43 subjects and 33 variants**, likely reflecting differences in publication timing or inclusion criteria. This is a case count, not prevalence. Reliable incidence, prevalence per 100,000, carrier frequency, sex ratio, penetrance, or life-table estimates are unavailable. (alsharhan2021expandingthephenotype pages 6-8, farolfi2021alg3cdgapatient pages 4-5)

Affected individuals have been reported across multiple geographic and ancestral backgrounds, including European, Middle Eastern, Asian, Caribbean, and other families. No single founder allele or population-specific founder effect was established in the retrieved evidence. Consanguinity can enrich homozygous alleles but is not necessary; compound heterozygous disease is well documented. (farolfi2021alg3cdgapatient pages 4-5)

Penetrance is presumed high for clearly deleterious biallelic alleles, but formal estimates are absent. Expressivity is variable. Anticipation is not expected. Germline mosaicism has not been established but remains a general residual counseling consideration after an apparently de novo event.

---

## 10. Diagnostics

### Recommended workflow

1. **Clinical suspicion:** congenital or early-onset multisystem disease with severe developmental delay, epilepsy, microcephaly/hypotonia, ocular disease, contractures/clubfeet, feeding failure, endocrine abnormalities, recurrent infections, renal anomalies, or cardiac disease.
2. **Biochemical screening:** serum transferrin isoelectric focusing, capillary electrophoresis, or mass-spectrometric transferrin glycoform analysis. ALG3-CDG usually gives a **type-I pattern**, indicating deficient glycan-site occupancy/assembly.
3. **Molecular testing:** a CDG/multisystem disease panel, exome sequencing, or genome sequencing demonstrating two pathogenic/likely pathogenic ALG3 variants in trans.
4. **Biochemical confirmation:** plasma protein N-glycan profiling by mass spectrometry and, where available, fibroblast lipid-linked oligosaccharide analysis.
5. **Family testing:** parental segregation and cascade testing. (alsharhan2021expandingthephenotype pages 3-5, himmelreich2019novelvariantsand pages 1-2, himmelreich2019novelvariantsand pages 6-7)

In the 2019 cohort, disialotransferrin was **24.12 ± 0.41%** versus a reference interval of **5.0–13.5%**, and tetrasialotransferrin was **26.9 ± 1.24%** versus **30.0–55.0%**. Fibroblast phosphomannomutase activity was normal, helping distinguish ALG3-CDG from PMM2-CDG. LLO analysis showed Man5GlcNAc2-PP-dolichol accumulation. (himmelreich2019novelvariantsand pages 6-7)

### Genetic-test utility

- **Panel or WES:** appropriate first-line molecular approaches when the phenotype is recognizable or broadly multisystem.
- **WGS:** useful after negative panel/WES, especially for noncoding, structural, complex, or poorly captured variants.
- **Single-gene sequencing:** appropriate when biochemical profiling strongly points to ALG3.
- **Deletion/duplication analysis:** consider if only one pathogenic allele is identified.
- **CMA, karyotype, FISH, mitochondrial DNA, and repeat-expansion testing:** not primary tests for isolated suspected ALG3-CDG, although CMA may be appropriate for an unresolved syndromic phenotype.
- **RNA studies:** potentially useful for splice variants or variants of uncertain significance; not a routine validated disease-specific diagnostic.

### Imaging and organ assessment

Brain MRI, ophthalmologic examination with optical coherence tomography when feasible, EEG, echocardiography, renal ultrasound, endocrine testing, immunologic assessment, coagulation studies, growth/nutritional evaluation, and orthopedic assessment are guided by the phenotype. The 2021 authors specifically recommend baseline and ongoing **endocrine, renal, cardiac, and immunologic evaluation**. (alsharhan2021expandingthephenotype pages 1-3)

### Differential diagnosis

Important differentials include PMM2-CDG, ALG1-CDG, ALG2-CDG, ALG6-CDG, ALG8-CDG, ALG9-CDG, ALG12-CDG, DPAGT1-CDG, DPM-pathway disorders, and other congenital syndromes featuring arthrogryposis, optic-nerve hypoplasia, epilepsy, or abnormal transferrin glycosylation. The ALG3-associated LLO and plasma N-glycan signature provides discrimination from many type-I CDGs.

### Screening

ALG3-CDG is not part of routine population newborn screening. Targeted familial carrier testing, cascade testing, prenatal molecular diagnosis, and preimplantation genetic testing are feasible after familial variants are established.

---

## 11. Outcome and prognosis

Prognosis is highly variable but often serious. Survival into adulthood—up to **37 years** in the 2021 series—is documented, while stillbirth, neonatal death, and death at one year from multiorgan failure also occurred. One ophthalmic review stated that almost half of reported subjects died before or during the neonatal period, but this estimate is strongly susceptible to small-sample and publication bias and should not be treated as a population survival rate. (alsharhan2021expandingthephenotype pages 3-5, farolfi2021alg3cdgapatient pages 4-5)

No valid 5- or 10-year survival estimates, life expectancy, mortality rate, or standardized disability-adjusted-life-year data exist. Major morbidity arises from severe neurodevelopmental disability, refractory epilepsy, visual impairment, feeding and growth failure, contractures, endocrine deficiency, recurrent infections, coagulation abnormalities, renal disease, and cardiac complications.

Potentially adverse prognostic indicators—based on clinical reasoning rather than validated models—include prenatal structural anomalies, neonatal multisystem failure, severe brain malformations, refractory seizures, profound feeding failure, major cardiomyopathy, adrenal insufficiency, immunodeficiency, and recurrent serious infection. No validated molecular prognostic biomarker or genotype-based survival model exists.

---

## 12. Treatment

### Current standard: supportive multidisciplinary care

There is no approved curative or disease-modifying therapy. Treatment should be individualized and may include:

- antiseizure medications; ketogenic diet may be considered for drug-resistant epilepsy under specialist supervision, although response is inconsistent and evidence in ALG3-CDG is case-based;
- enteral nutritional support, feeding therapy, and management of aspiration or growth failure;
- thyroid, glucocorticoid, growth-hormone, or other endocrine replacement when deficiency is documented;
- physical and occupational therapy, stretching, orthoses, and orthopedic surgery when indicated for contractures, clubfeet, hip disease, or scoliosis;
- visual habilitation and management of cataract or other treatable ocular disease;
- treatment and prevention of infections based on immunologic assessment;
- cardiology, nephrology, hematology, and coagulation management based on organ findings. (alsharhan2021expandingthephenotype pages 6-8, alsharhan2021expandingthephenotype pages 5-6, alsharhan2021expandingthephenotype pages 10-11)

Suggested NCIt intervention concepts include **Supportive Care**, **Anticonvulsant Therapy**, **Ketogenic Diet**, **Enteral Nutrition**, **Hormone Replacement Therapy**, **Physical Therapy**, **Occupational Therapy**, **Orthopedic Surgery**, and **Genetic Counseling**. Exact NCIt identifiers should be resolved against the current NCIt release.

### Experimental therapies and recent research

No ALG3-CDG-specific interventional trial or NCT identifier was retrieved. No gene replacement, CRISPR editing, RNA therapy, enzyme replacement, or cell therapy has reached established clinical use.

A 2024 preclinical study reported that liposome-encapsulated mannose-1-phosphate improved global N-glycosylation across selected CDG cellular systems, but this should not be interpreted as clinical efficacy for ALG3-CDG; ALG3 acts downstream of mannose-1-phosphate supply, and disease-specific benefit requires direct experimental confirmation. Likewise, the 2024 ER-stress study may reveal downstream therapeutic targets, but it does not establish an approved treatment.

No response rate, comparative effectiveness estimate, or ALG3-specific pharmacogenomic recommendation exists.

---

## 13. Prevention

Primary prevention through lifestyle change or vaccination is not applicable to a constitutive autosomal-recessive disorder. Reproductive prevention options include genetic counseling, carrier testing of relatives, partner testing, preimplantation genetic testing, chorionic-villus sampling, amniocentesis, or appropriately validated noninvasive approaches after familial variants are known.

Secondary prevention consists of earlier recognition through transferrin glycoform testing and molecular diagnosis in symptomatic children or at-risk relatives. Tertiary prevention includes seizure control, adequate nutrition, aspiration precautions, contracture management, endocrine replacement, vaccination and infection planning, and surveillance of renal, cardiac, immune, visual, and coagulation complications. (alsharhan2021expandingthephenotype pages 1-3)

No disease-specific population screening, vaccine, chemoprophylaxis, or environmental intervention is established.

---

## 14. Other species and natural disease

No naturally occurring ALG3-CDG-equivalent disease in companion animals, livestock, or wildlife was identified in the retrieved literature. Consequently, no breed-specific VBO annotation or veterinary prevalence can be assigned. The disorder is not infectious and has no zoonotic or cross-species transmission potential.

ALG3 orthologs and the dolichol-linked oligosaccharide pathway are evolutionarily conserved in eukaryotes, especially yeast and mammals. This conservation supports mechanistic comparison, but orthology should not be conflated with naturally occurring veterinary disease. Species-specific NCBI Gene and Taxon identifiers should be pulled directly from current NCBI records during database ingestion.

---

## 15. Model organisms and experimental systems

### Available systems

- **Patient fibroblasts:** the most disease-proximal experimental system used to measure LLO accumulation, glycosylation, phosphomannomutase activity, and ALG3 protein abundance. (himmelreich2019novelvariantsand pages 1-2, himmelreich2019novelvariantsand pages 6-7)
- **Yeast ALG-pathway models:** *Saccharomyces cerevisiae* ALG mutants are historically important for dissecting dolichol-linked oligosaccharide assembly and testing functional complementation. Their strengths are pathway conservation and tractable genetics; limitations include lack of human neurodevelopment, endocrine organs, and complex tissue phenotypes.
- **Engineered cellular models:** suitable for variant complementation, glycoproteomic analysis, ER-stress assays, and therapeutic screening.

No well-validated ALG3-CDG mouse, rat, zebrafish, Drosophila, *C. elegans*, organoid, or patient-derived iPSC model that recapitulates the full human phenotype was established in the retrieved evidence. Model-database searches should therefore treat any ALG3 knockout phenotype as pathway evidence until disease-specific phenotypic concordance is demonstrated.

### Research applications and limitations

Cellular and yeast models can define residual enzyme activity, LLO composition, N-glycan extension, ER stress, and variant pathogenicity. They cannot directly model intellectual disability, epilepsy, visual behavior, pituitary dysfunction, or survival. Future priorities include conditional mammalian models, patient-derived neural/retinal organoids, and isogenic CRISPR-corrected iPSC pairs.

---

## Recent developments and expert interpretation

A 2023 state-of-the-art review characterized CDG as a rapidly expanding field in which multi-omics has accelerated gene discovery and mechanistic resolution, while targeted therapy remains the central unmet need. It reported **163 known CDG genetic defects encompassing 193 phenotypes**, underscoring how exceptionally sparse the subtype-specific ALG3 evidence remains. Francisco et al., *Orphanet Journal of Rare Diseases*, published October 2023, DOI: https://doi.org/10.1186/s13023-023-02879-z.

The most authoritative ALG3-specific management opinion remains the 2021 recommendation for baseline and ongoing endocrine, renal, cardiac, and immunologic evaluation. This is biologically plausible and directly derived from newly recognized organ involvement, but it remains expert cohort-based guidance rather than a randomized or consensus-guideline-tested schedule. (alsharhan2021expandingthephenotype pages 1-3)

The disease’s most useful emerging biomarker is not merely a generic type-I transferrin profile but the more specific plasma N-glycan combination of truncated extension beyond Man5GlcNAc2 and deficient hybrid glycans. The authors’ abstract describes this spectrum as “unique to ALG3-CDG,” making it a valuable orthogonal confirmation tool for variant interpretation. (alsharhan2021expandingthephenotype pages 1-3)

## Priority knowledge gaps

1. Population prevalence, incidence, carrier frequency, and unbiased survival estimates.
2. Prospective natural history and standardized patient-reported outcomes.
3. Variant-level residual activity and robust genotype–phenotype relationships.
4. Validated surveillance intervals and evidence-based treatment pathways.
5. Disease-specific animal, iPSC, neural, and retinal models.
6. Clinical translation of glycan-directed, ER-stress-modifying, gene, or RNA therapies.
7. Systematic single-cell, spatial, proteomic, metabolomic, and glycoproteomic profiling.

Overall, the evidence supports ALG3-CDG as a congenital, autosomal-recessive ER glycosylation disorder with a recognizable biochemical signature and severe but variable multisystem phenotype. The strongest immediate real-world application is combined biochemical–genomic diagnosis followed by proactive multidisciplinary surveillance; disease-modifying therapy remains an unmet research objective.

References

1. (alsharhan2021expandingthephenotype pages 3-5): Hind Alsharhan, Bobby G. Ng, Earnest James Paul Daniel, Jennifer Friedman, Eniko K. Pivnick, Amal Al‐Hashem, Eissa Ali Faqeih, Pengfei Liu, Nicole M. Engelhardt, Kierstin N. Keller, Jie Chen, Pamela A. Mazzeo, Jill A. Rosenfeld, Michael J. Bamshad, Deborah A. Nickerson, Kimiyo M. Raymond, Hudson H. Freeze, Miao He, Andrew C. Edmondson, and Christina Lam. Expanding the phenotype, genotype and biochemical knowledge of <scp>alg3‐cdg</scp>. Journal of Inherited Metabolic Disease, 44:987-1000, Mar 2021. URL: https://doi.org/10.1002/jimd.12367, doi:10.1002/jimd.12367. This article has 24 citations and is from a peer-reviewed journal.

2. (alsharhan2021expandingthephenotype pages 6-8): Hind Alsharhan, Bobby G. Ng, Earnest James Paul Daniel, Jennifer Friedman, Eniko K. Pivnick, Amal Al‐Hashem, Eissa Ali Faqeih, Pengfei Liu, Nicole M. Engelhardt, Kierstin N. Keller, Jie Chen, Pamela A. Mazzeo, Jill A. Rosenfeld, Michael J. Bamshad, Deborah A. Nickerson, Kimiyo M. Raymond, Hudson H. Freeze, Miao He, Andrew C. Edmondson, and Christina Lam. Expanding the phenotype, genotype and biochemical knowledge of <scp>alg3‐cdg</scp>. Journal of Inherited Metabolic Disease, 44:987-1000, Mar 2021. URL: https://doi.org/10.1002/jimd.12367, doi:10.1002/jimd.12367. This article has 24 citations and is from a peer-reviewed journal.

3. (alsharhan2021expandingthephenotype pages 1-3): Hind Alsharhan, Bobby G. Ng, Earnest James Paul Daniel, Jennifer Friedman, Eniko K. Pivnick, Amal Al‐Hashem, Eissa Ali Faqeih, Pengfei Liu, Nicole M. Engelhardt, Kierstin N. Keller, Jie Chen, Pamela A. Mazzeo, Jill A. Rosenfeld, Michael J. Bamshad, Deborah A. Nickerson, Kimiyo M. Raymond, Hudson H. Freeze, Miao He, Andrew C. Edmondson, and Christina Lam. Expanding the phenotype, genotype and biochemical knowledge of <scp>alg3‐cdg</scp>. Journal of Inherited Metabolic Disease, 44:987-1000, Mar 2021. URL: https://doi.org/10.1002/jimd.12367, doi:10.1002/jimd.12367. This article has 24 citations and is from a peer-reviewed journal.

4. (himmelreich2019novelvariantsand pages 1-2): Nastassja Himmelreich, Bianca Dimitrov, Virginia Geiger, Matthias Zielonka, Anna‐Marlen Hutter, Lars Beedgen, Andreas Hüllen, Maximilian Breuer, Verena Peters, Kai‐Christian Thiemann, Georg F. Hoffmann, Irmgard Sinning, Thierry Dupré, Sandrine Vuillaumier‐Barrot, Catherine Barrey, Jonas Denecke, Wolfgang Kölfen, Gesche Düker, Rainer Ganschow, Michael J. Lentze, Stuart Moore, Nathalie Seta, Andreas Ziegler, and Christian Thiel. Novel variants and clinical symptoms in four new alg3‐cdg patients, review of the literature, and identification of aagrp‐alg3 as a novel alg3 variant with alanine and glycine‐rich n‐terminus. Human Mutation, 40:938-951, May 2019. URL: https://doi.org/10.1002/humu.23764, doi:10.1002/humu.23764. This article has 28 citations and is from a domain leading peer-reviewed journal.

5. (OpenTargets Search: ALG3-congenital disorder of glycosylation-ALG3): Open Targets Query (ALG3-congenital disorder of glycosylation-ALG3, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (alsharhan2021expandingthephenotype pages 5-6): Hind Alsharhan, Bobby G. Ng, Earnest James Paul Daniel, Jennifer Friedman, Eniko K. Pivnick, Amal Al‐Hashem, Eissa Ali Faqeih, Pengfei Liu, Nicole M. Engelhardt, Kierstin N. Keller, Jie Chen, Pamela A. Mazzeo, Jill A. Rosenfeld, Michael J. Bamshad, Deborah A. Nickerson, Kimiyo M. Raymond, Hudson H. Freeze, Miao He, Andrew C. Edmondson, and Christina Lam. Expanding the phenotype, genotype and biochemical knowledge of <scp>alg3‐cdg</scp>. Journal of Inherited Metabolic Disease, 44:987-1000, Mar 2021. URL: https://doi.org/10.1002/jimd.12367, doi:10.1002/jimd.12367. This article has 24 citations and is from a peer-reviewed journal.

7. (farolfi2021alg3cdgapatient pages 4-5): Martina Farolfi, Anna Cechova, Nina Ondruskova, Jana Zidkova, Bohdan Kousal, Hana Hansikova, Tomas Honzik, and Petra Liskova. Alg3-cdg: a patient with novel variants and review of the genetic and ophthalmic findings. BMC Ophthalmology, Jun 2021. URL: https://doi.org/10.1186/s12886-021-02013-2, doi:10.1186/s12886-021-02013-2. This article has 14 citations and is from a peer-reviewed journal.

8. (himmelreich2019novelvariantsand pages 6-7): Nastassja Himmelreich, Bianca Dimitrov, Virginia Geiger, Matthias Zielonka, Anna‐Marlen Hutter, Lars Beedgen, Andreas Hüllen, Maximilian Breuer, Verena Peters, Kai‐Christian Thiemann, Georg F. Hoffmann, Irmgard Sinning, Thierry Dupré, Sandrine Vuillaumier‐Barrot, Catherine Barrey, Jonas Denecke, Wolfgang Kölfen, Gesche Düker, Rainer Ganschow, Michael J. Lentze, Stuart Moore, Nathalie Seta, Andreas Ziegler, and Christian Thiel. Novel variants and clinical symptoms in four new alg3‐cdg patients, review of the literature, and identification of aagrp‐alg3 as a novel alg3 variant with alanine and glycine‐rich n‐terminus. Human Mutation, 40:938-951, May 2019. URL: https://doi.org/10.1002/humu.23764, doi:10.1002/humu.23764. This article has 28 citations and is from a domain leading peer-reviewed journal.

9. (alsharhan2021expandingthephenotype pages 10-11): Hind Alsharhan, Bobby G. Ng, Earnest James Paul Daniel, Jennifer Friedman, Eniko K. Pivnick, Amal Al‐Hashem, Eissa Ali Faqeih, Pengfei Liu, Nicole M. Engelhardt, Kierstin N. Keller, Jie Chen, Pamela A. Mazzeo, Jill A. Rosenfeld, Michael J. Bamshad, Deborah A. Nickerson, Kimiyo M. Raymond, Hudson H. Freeze, Miao He, Andrew C. Edmondson, and Christina Lam. Expanding the phenotype, genotype and biochemical knowledge of <scp>alg3‐cdg</scp>. Journal of Inherited Metabolic Disease, 44:987-1000, Mar 2021. URL: https://doi.org/10.1002/jimd.12367, doi:10.1002/jimd.12367. This article has 24 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](ALG3-Congenital_Disorder_of_Glycosylation-deep-research-falcon_artifacts/artifact-00.md)