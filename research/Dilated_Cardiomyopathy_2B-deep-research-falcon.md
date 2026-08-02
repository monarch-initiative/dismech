---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-02T16:42:11.794743'
end_time: '2026-08-02T16:50:36.978717'
duration_seconds: 505.18
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dilated Cardiomyopathy 2B
  mondo_id: ''
  category: Genetic
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
  path: Dilated_Cardiomyopathy_2B-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 2B
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 2B** covering all of the
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
- **Disease Name:** Dilated Cardiomyopathy 2B
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 2B** covering all of the
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


# Dilated Cardiomyopathy 2B: Comprehensive Disease-Characteristics Report

**Scope and evidence warning.** Dilated cardiomyopathy 2B (DCM2B) is an exceptionally rare proposed Mendelian subtype. Its GATAD1 association derives principally from one family (original report: PMID **21965549**), and a 2023 systematic reassessment placed **GATAD1 among recessive cardiomyopathy genes reported in only a single family**, explicitly stating that replication is required. Consequently, the gene–disease relationship, phenotype frequencies, penetrance, prognosis, and epidemiology are much less secure than for established DCM genes such as TTN or LMNA. Statements below are labeled as **disease-specific**, **general-DCM extrapolation**, or **experimental hypothesis** as appropriate. (OpenTargets Search: Dilated Cardiomyopathy 2B, lipov2023exploringthecomplex pages 6-7)

| domain | best-supported finding | evidence type/year | confidence/limitation |
|---|---|---|---|
| Disease identity | Dilated Cardiomyopathy 2B is represented as MONDO:0013848 and is linked to GATAD1 in disease-target resources. (OpenTargets Search: Dilated Cardiomyopathy 2B) | Curated disease-target aggregation, 2024 access | Moderate confidence for nomenclature; disease validity depends on sparse primary evidence. |
| Causal gene | GATAD1 is the only target associated with this disease in the retrieved authoritative aggregation, with literature support pointing to the original report. (OpenTargets Search: Dilated Cardiomyopathy 2B) | Aggregated genetics evidence citing prior literature | Moderate confidence for gene assignment; association is not broadly replicated. |
| Inheritance | The best-supported inheritance model is autosomal recessive. A 2023 review classifies GATAD1 among genes reported for recessive cardiomyopathy phenotypes but notes it has been identified in a single family only. (lipov2023exploringthecomplex pages 6-7) | Review/meta-analysis, 2023 | Moderate confidence for recessive inheritance; low confidence for overall gene-disease strength because replication is lacking. |
| Human evidence base | Current literature reassessment indicates GATAD1-associated cardiomyopathy remains a single-family observation rather than a repeatedly confirmed disease gene association. (lipov2023exploringthecomplex pages 6-7) | Review/meta-analysis, 2023 | Key limitation: very small human evidence base; penetrance, spectrum, and natural history remain uncertain. |
| Variant | The disease-associated change discussed in recent mechanistic work is the phosphorylation-site missense variant p.Ser102Pro in GATAD1. (rrustemi2024exploringpathogenicmutations pages 102-107, rrustemi2024exploringpathogenicmutations pages 107-112) | Mechanistic follow-up study, 2024 | Moderate confidence that this is the implicated variant in the studied mechanism; founding-report details were not fully retrievable here. |
| Molecular mechanism | 2024 work found that the GATAD1 phosphorylation site mediates interaction with 14-3-3 family proteins and suggests 14-3-3 binding masks a nuclear localization signal, affecting nucleocytoplasmic transport. (rrustemi2024pathogenicmutationsof pages 1-2, rrustemi2024exploringpathogenicmutations pages 102-107, rrustemi2024exploringpathogenicmutations pages 107-112) | Primary mechanistic proteomics/structural study, 2024 | Mechanistically plausible but incomplete; upstream kinase and full in vivo causal chain remain unresolved. |
| Phosphorylation dependence | Phosphorylated wild-type GATAD1 peptide bound 14-3-3 proteins, whereas the S102P variant disrupted this phosphorylation-dependent interaction. (rrustemi2024exploringpathogenicmutations pages 80-87, rrustemi2024exploringpathogenicmutations pages 102-107) | Primary proteomics/biophysics, 2024 | Moderate confidence at peptide/biophysical level; limitation is extrapolation from peptide assays to whole-organ disease. |
| Cellular localization | Recent work suggests loss of phosphorylation-dependent 14-3-3 binding could alter GATAD1 nuclear transport, but engineered iPSC-cardiomyocytes did not show a strong differential localization/proteome phenotype under the tested conditions. (rrustemi2024exploringpathogenicmutations pages 80-87, rrustemi2024exploringpathogenicmutations pages 107-112) | iPSC and cell biology study, 2024 | Low-to-moderate confidence for disease relevance; authors note immature cardiomyocyte state may obscure phenotype. |
| Clinical phenotype | The disease phenotype is dilated cardiomyopathy, i.e., ventricular dilatation with systolic dysfunction; disease-specific phenotypic granularity beyond the founding family is not well established in recent accessible sources. (OpenTargets Search: Dilated Cardiomyopathy 2B, sorella2025diagnosisandmanagement pages 1-2, sorella2025diagnosisandmanagement pages 2-3) | Disease aggregation plus general DCM guideline/review evidence, 2024-2025 | High confidence for broad phenotype label; low confidence for precise GATAD1-specific frequency, onset, arrhythmia burden, or extracardiac spectrum. |
| Diagnostics | No DCM2B-specific diagnostic algorithm was found; current practice should be extrapolated from general DCM guidance using clinical evaluation, ECG, biomarkers, echocardiography, CMR, and genetic counseling/testing. (sorella2025diagnosisandmanagement pages 2-3, sorella2025diagnosisandmanagement pages 12-13) | Guideline/review synthesis, 2025 | High confidence for general DCM workup; not specific to GATAD1-DCM2B. |
| Treatment | No genotype-specific therapy or trial for GATAD1-DCM2B was identified; management is extrapolated from standard DCM/HFrEF care and advanced heart failure pathways when needed. (sorella2025diagnosisandmanagement pages 1-2, sorella2025diagnosisandmanagement pages 12-13) | Guideline/review synthesis, 2025 | High confidence for general management principles; no direct evidence for GATAD1-specific treatment response. |
| Epidemiology | Disease-specific prevalence, incidence, and population distribution for DCM2B are unavailable from the retrieved evidence; even general DCM prevalence figures do not resolve the rarity of this subtype. (lipov2023exploringthecomplex pages 6-7, sorella2025diagnosisandmanagement pages 1-2) | Review/meta-analysis and guideline review, 2023-2025 | Very low confidence for subtype epidemiology because data are essentially unavailable. |
| Clinical trials | No interventional trials specifically targeting GATAD1-associated Dilated Cardiomyopathy 2B were identified in the retrieved searches. (OpenTargets Search: Dilated Cardiomyopathy 2B) | Clinical trial search context / disease-target context | Strong negative finding within retrieved sources, but absence of evidence is not absolute proof of no trials anywhere. |
| Models and functional systems | Functional interpretation currently relies mainly on peptide proteomics, structural studies, heterologous cells, and iPSC-cardiomyocytes; no robust disease-specific animal model evidence was verified in the retrieved primary sources here. (rrustemi2024exploringpathogenicmutations pages 80-87, rrustemi2024exploringpathogenicmutations pages 102-107, rrustemi2024exploringpathogenicmutations pages 107-112) | Experimental mechanistic studies, 2024 | Major limitation: model systems have not yet produced a decisive disease phenotype or fully validated mechanism. |


*Table: This table summarizes the strongest currently retrievable evidence for Dilated Cardiomyopathy 2B, separating what is disease-specific from what is extrapolated from general DCM guidance. It is useful for quickly assessing confidence, limitations, and major evidence gaps around GATAD1-associated disease.*

## 1. Disease information

### Definition
DCM2B is the name assigned to a presumed **autosomal-recessive, GATAD1-associated form of dilated cardiomyopathy**. The defining cardiac phenotype is ventricular—principally left-ventricular—dilatation accompanied by impaired systolic function that is not adequately explained by coronary artery disease, hypertension, valve disease, congenital heart disease, or another abnormal loading condition. That phenotypic definition is the general DCM definition; only the GATAD1 association and recessive designation distinguish DCM2B. (OpenTargets Search: Dilated Cardiomyopathy 2B, sorella2025diagnosisandmanagement pages 1-2, sorella2025diagnosisandmanagement pages 2-3)

### Identifiers and synonyms

- **MONDO:** **MONDO:0013848**.
- **Disease-associated gene:** **GATAD1**, GATA zinc-finger domain containing 1; Ensembl **ENSG00000157259**.
- **Original literature linkage:** PMID **21965549**; Open Targets also points to ClinVar record **RCV000024350**. (OpenTargets Search: Dilated Cardiomyopathy 2B)
- **Common names:** dilated cardiomyopathy 2B; cardiomyopathy, dilated, 2B; DCM2B; GATAD1-related dilated cardiomyopathy; autosomal-recessive GATAD1 cardiomyopathy.
- **OMIM:** The retrieved evidence did not expose a safely verifiable disease-number entry; it should be populated only after direct OMIM verification rather than inferred.
- **Orphanet:** No subtype-specific Orphanet identifier was verified.
- **ICD-10:** No DCM2B-specific code; use the jurisdiction-appropriate dilated-cardiomyopathy code, commonly **I42.0**, plus genetic/family-history coding where applicable.
- **ICD-11/MeSH/SNOMED CT:** These systems describe DCM or genetic cardiomyopathy but no retrieved evidence established a unique DCM2B concept code.

The evidence is **aggregated disease-level information**, ultimately derived from a very small pedigree and experimental studies—not longitudinal EHR-scale patient data. Open Targets finds one associated target, GATAD1, supported by only two evidence records. (OpenTargets Search: Dilated Cardiomyopathy 2B)

## 2. Etiology, risk, and protective factors

### Primary cause
The proposed cause is a **biallelic germline GATAD1 missense variant affecting serine 102**, generally described at protein level as **p.Ser102Pro (S102P)**. The recessive assignment is supported by the original pedigree and later reviews, but independent human replication remains lacking. A 2023 review grouped GATAD1 among 13 proposed recessive cardiomyopathy genes observed in a single family only. (rrustemi2024exploringpathogenicmutations pages 102-107, lipov2023exploringthecomplex pages 6-7)

### Genetic risk

- Highest presumed risk: **biallelic pathogenic GATAD1 variants**, particularly homozygosity for p.Ser102Pro.
- Heterozygous relatives are expected to be carriers under the proposed recessive model, but robust estimates of heterozygote cardiac risk, age-dependent penetrance, or carrier frequency are unavailable.
- Consanguinity/family history can increase the probability that both parents carry the same rare allele, as is typical for single-family recessive discoveries, but exact pedigree statistics could not be independently recovered from the available full text.
- No validated susceptibility loci, polygenic modifiers, founder-frequency estimates, or modifier genes are established specifically for DCM2B.

### Environmental and gene–environment factors
No DCM2B-specific associations have been demonstrated for alcohol, cardiotoxic chemotherapy, pregnancy, viral infection, smoking, nutrition, exercise, occupational exposure, or pollution. These exposures can cause or exacerbate DCM generally and should be investigated clinically, but they must not be presented as proven GATAD1 interactions. General DCM is genetically complex, and secondary stressors can modify penetrance in other genetic forms; analogous modification in DCM2B remains hypothetical. (sorella2025diagnosisandmanagement pages 1-2)

### Protective factors
No protective GATAD1 allele, diet, medication, or exposure has been established. Avoiding recognized myocardial toxins and treating hypertension, metabolic disease, and infection are prudent general cardiovascular measures, not demonstrated primary prevention for this recessive genotype.

## 3. Phenotypes

The only secure phenotype-level designation is **dilated cardiomyopathy with systolic dysfunction**. Detailed frequencies cannot be estimated from a single family.

| Phenotype | Type and expected course | Suggested HPO term | Evidence status |
|---|---|---|---|
| Dilated cardiomyopathy | Clinical diagnosis; likely chronic and progressive | **HP:0001644** | Disease-defining, disease-specific |
| Left-ventricular dilatation | Imaging sign | **HP:0001714** | Core general-DCM feature |
| Reduced LV systolic function/ejection fraction | Imaging/functional abnormality | **HP:0001723** (decreased cardiac function) | Core general-DCM feature |
| Heart failure | Syndrome/signs and symptoms | **HP:0001635** | Expected consequence; subtype frequency unknown |
| Exercise intolerance/fatigue | Symptom | **HP:0003546**, **HP:0012378** | General-DCM extrapolation |
| Dyspnea | Symptom | **HP:0002094** | General-DCM extrapolation |
| Cardiomegaly | Imaging/physical sign | **HP:0001640** | General-DCM extrapolation |
| Arrhythmia/palpitations | Electrophysiological symptom | **HP:0011675**, **HP:0001962** | Possible in DCM generally; DCM2B burden unknown |
| Peripheral edema | Clinical sign | **HP:0012398** | Advanced-heart-failure extrapolation |

**Onset, severity, and progression:** available modern evidence does not support reliable medians, ranges, percentages, or sex differences for DCM2B. Recessive cardiomyopathies as a group tend toward earlier onset and severe outcomes, but GATAD1 was excluded from the 18 “robust” recessive genes because it lacked replication; group statistics therefore should not be assigned directly to DCM2B. (lipov2023exploringthecomplex pages 6-7)

**Quality of life:** no DCM2B-specific EQ-5D, SF-36, KCCQ, or PROMIS study exists in the retrieved evidence. Symptomatic DCM can impair exertion, schooling/employment, sleep, independence, and psychosocial well-being, but this is extrapolation.

## 4. Genetic and molecular information

### Gene and variant

- **Gene:** GATAD1, encoding GATA zinc-finger domain-containing protein 1.
- **Disease variant studied mechanistically:** **p.Ser102Pro**.
- **Variant class:** missense substitution at a phosphorylation site in an intrinsically disordered region.
- **Origin:** presumed constitutional/germline; this is not a somatic-cancer disorder.
- **ACMG/AMP classification:** Open Targets links a ClinVar record, but a current assertion, review status, transcript-specific HGVS expression, and classification should be retrieved directly from ClinVar before knowledge-base ingestion. (OpenTargets Search: Dilated Cardiomyopathy 2B)
- **Population frequency:** no precise gnomAD/TOPMed frequency was established in the retrieved evidence. A genuinely causative allele for this exceptionally rare recessive disorder would be expected to be rare, but expectation is not a substitute for database annotation.

### Functional consequence and 2024 advance
A 2024 Nature Communications study directly examined pathogenic substitutions at phosphorylation sites. Its abstract states: **“We focused on a mutation of a serine phosphorylation site in the transcription factor GATAD1, which causes dilated cardiomyopathy.”** It found that the site mediates phosphorylation-dependent binding to **14-3-3 proteins** and suggested that binding regulates nucleocytoplasmic transport by masking a nuclear-localization signal. (rrustemi2024pathogenicmutationsof pages 1-2)

Biophysical work found no binding of S102P to 14-3-3ε, whereas a phosphorylated S102 peptide bound with an approximate dissociation constant of **3 μM**. These findings support loss of a regulated protein–protein interaction rather than a simple structural loss of a folded catalytic domain. (rrustemi2024exploringpathogenicmutations pages 80-87, rrustemi2024exploringpathogenicmutations pages 102-107)

Important limitations are substantial:

1. The strongest interaction experiments used short peptides and heterologous cells, not an intact human heart.
2. S102 phosphorylation was documented in murine heart tissue but not HEK-293 cells.
3. The responsible kinase is unknown.
4. Wild-type and S102P GATAD1 were predominantly nuclear in engineered iPSC-derived cardiomyocytes, with no major proteomic or localization difference under tested conditions.
5. Immaturity of iPSC cardiomyocytes may conceal an adult or stress-dependent phenotype. (rrustemi2024exploringpathogenicmutations pages 80-87, rrustemi2024exploringpathogenicmutations pages 102-107, rrustemi2024exploringpathogenicmutations pages 107-112)

Accordingly, “loss of function,” “gain of function,” or “dominant negative” is not yet definitively assignable. The best description is **loss of phosphorylation-dependent 14-3-3 interaction with uncertain downstream functional direction**.

### Modifier, epigenetic, and chromosomal data
No DCM2B-specific modifier genes, DNA-methylation signatures, histone marks, chromosomal rearrangements, copy-number variants, or mosaicism have been established. Although GATAD1 is a nuclear regulatory protein and chromatin complexes are important in cardiomyocyte identity, assigning DCM2B to a particular NuRD/CoREST pathway would presently exceed the evidence.

## 5. Environmental information

No toxin, infectious organism, radiation exposure, dietary deficiency, alcohol threshold, or occupational exposure has been causally linked to DCM2B. Standard DCM evaluation should nevertheless exclude ischemic disease, alcohol/toxin exposure, myocarditis, endocrine/metabolic disease, pregnancy-associated cardiomyopathy, tachycardia-mediated dysfunction, and cardiotoxic medication exposure. This is differential etiologic assessment, not evidence that these factors cause GATAD1 disease. (sorella2025diagnosisandmanagement pages 2-3)

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. **Upstream genetic trigger:** biallelic GATAD1 p.Ser102Pro.
2. **Immediate biochemical defect:** serine-to-proline substitution abolishes phosphorylation at residue 102.
3. **Protein-interaction defect:** phosphorylated wild-type GATAD1 binds 14-3-3 family proteins; S102P disrupts this interaction.
4. **Trafficking hypothesis:** 14-3-3 binding masks a nearby nuclear-localization signal and competes with import machinery, potentially altering stimulus- or stage-dependent nucleocytoplasmic transport.
5. **Unknown intermediate:** altered GATAD1 localization or partner selection may dysregulate cardiomyocyte gene programs, proteostasis, sarcomere maintenance, or stress adaptation.
6. **Tissue phenotype:** impaired cardiomyocyte contractility/remodeling could cause ventricular systolic dysfunction and chamber dilatation.
7. **Clinical downstream effects:** heart failure, exercise intolerance, arrhythmia, transplantation, or death may follow in severe DCM.

Only steps 2–4 have meaningful 2024 experimental support; steps 5–7 remain incompletely demonstrated for this genotype. The authors’ summary was that pathogenic phosphorylation-site mutations can alter protein interactions, providing **“insights into potential molecular mechanisms”** rather than proving the complete disease pathway. (rrustemi2024pathogenicmutationsof pages 1-2)

### Suggested ontology annotations

- **GO biological process:** protein phosphorylation (**GO:0006468**); protein localization to nucleus (**GO:0034504**); regulation of transcription by RNA polymerase II (**GO:0006357**, provisional); cardiac muscle contraction (**GO:0060048**); ventricular cardiac muscle tissue morphogenesis (**GO:0055010**); response to mechanical stimulus (**GO:0009612**, provisional).
- **GO cellular component:** nucleus (**GO:0005634**); cytoplasm (**GO:0005737**); nucleoplasm (**GO:0005654**); sarcomere (**GO:0030017**, downstream tissue pathology rather than demonstrated GATAD1 localization).
- **Cell Ontology:** cardiac muscle cell/cardiomyocyte (**CL:0000746**); ventricular cardiac muscle cell (**CL:0002131**); cardiac fibroblast (use current CL lookup before ingestion because fibrosis is general-DCM extrapolation).
- **Biological processes downstream in DCM:** maladaptive remodeling, fibrosis, neurohormonal activation, altered calcium handling, energetic stress, and possible inflammation. None is yet molecularly profiled specifically in DCM2B.

### Molecular profiling and advanced technologies
The 2024 study used peptide-interaction proteomics, SILAC, structural/biophysical validation, heterologous cells, and engineered iPSC-derived cardiomyocytes. No significant global proteomic difference emerged between wild-type and S102P iPSC cardiomyocytes under the tested early differentiation conditions. No disease-specific single-cell atlas, spatial transcriptome, mature-heart RNA-seq, metabolome, lipidome, epigenome, or CRISPR-screen dataset was identified. (rrustemi2024exploringpathogenicmutations pages 80-87, rrustemi2024exploringpathogenicmutations pages 107-112, rrustemi2024pathogenicmutationsof pages 2-3)

## 7. Anatomical structures affected

- **Primary organ/system:** heart; cardiovascular system.
- **Primary chamber:** left ventricle; biventricular involvement is possible in advanced DCM but is not quantified for DCM2B.
- **Tissue:** myocardium/cardiac muscle tissue.
- **Primary cell:** ventricular cardiomyocyte.
- **Secondary cells:** cardiac fibroblasts, endothelial cells, immune cells, and conduction-system cells can participate in general DCM remodeling; subtype-specific involvement is unproven.
- **Subcellular focus:** GATAD1-associated nuclear/nucleocytoplasmic compartments and phosphorylation-dependent protein-interaction machinery; sarcomeres and mitochondria are plausible downstream compartments, not directly established targets.
- **Laterality:** not applicable; cardiomyopathy is not a unilateral disorder.

Suggested anatomy terms include **UBERON:0000948** (heart), **UBERON:0002084** (heart left ventricle), and **UBERON:0002349** (myocardium). Identifier validation against the current ontology release is recommended before production use.

## 8. Temporal development

No robust DCM2B natural-history cohort exists. The disorder should be treated as **chronic and potentially progressive**, with a possible preclinical genotype-positive phase, followed by subtle structural/functional abnormalities, symptomatic systolic heart failure, and potentially advanced disease. Exact onset—from infancy through adulthood—cannot be reliably specified from the retrieved evidence.

Potentially actionable windows are:

1. **Before symptoms:** cascade testing and cardiac surveillance in relatives.
2. **Early phenotype:** initiate evidence-based heart-failure therapy and remove myocardial stressors.
3. **Electrical or fibrotic progression:** CMR/ambulatory rhythm assessment and individualized device evaluation.
4. **Advanced disease:** referral for mechanical circulatory support or transplantation.

Remission/reverse remodeling may occur in DCM generally after therapy, but treatment withdrawal can permit relapse; no GATAD1-specific recovery rate is known.

## 9. Inheritance and population

### Inheritance
The proposed pattern is **autosomal recessive**. For two confirmed heterozygous parents, each pregnancy conventionally carries a 25% probability of an affected child, 50% probability of a heterozygous child, and 25% probability of inheriting neither familial allele. These Mendelian figures assume that the variant is truly pathogenic and fully explanatory.

Penetrance in biallelic carriers, expressivity, anticipation, germline mosaicism, de novo rate, and sex effects are unknown. Anticipation is not expected mechanistically because this is not a repeat-expansion disorder. Consanguinity can elevate recurrence risk by increasing parental sharing of rare alleles. No validated founder effect or ancestry-specific carrier frequency has been established.

### Epidemiology
There are no defensible subtype-specific prevalence or incidence estimates. General DCM prevalence has been estimated at approximately **1:250–1:400**, familial disease at **30–50%**, and identifiable genetic causes at approximately **30–40%**; these figures describe all DCM, not DCM2B. (sorella2025diagnosisandmanagement pages 1-2)

The 2023 recessive-cardiomyopathy analysis found GATAD1 in **one family only**, making geographic distribution, ethnicity effects, sex ratio, age distribution, and carrier frequency unknowable. For context—not subtype prevalence—the same study’s UK Biobank dataset contained 924 DCM cases among 454,162 participants (**0.21%**), but this was not a GATAD1 cohort. (lipov2023exploringthecomplex pages 6-7, lipov2023exploringthecomplex pages 19-24)

## 10. Diagnostics

### Clinical diagnosis
Use a multiparametric cardiomyopathy assessment:

1. Three-generation pedigree, consanguinity, sudden death, heart failure, transplant, neuromuscular disease, toxin/drug exposure, infection, and pregnancy history.
2. Physical examination and **12-lead ECG**; ambulatory monitoring when arrhythmia is suspected.
3. **Transthoracic echocardiography** as first-line assessment of chamber dimensions, ejection fraction, valves, hemodynamics, and right-heart involvement.
4. **Cardiac MRI** for ventricular function and tissue characterization, including edema, scar, and late gadolinium enhancement.
5. Laboratory tests including BNP/NT-proBNP and high-sensitivity troponin, blood count, renal/liver function, electrolytes, thyroid studies, iron studies, and cause-directed testing.
6. Coronary evaluation when ischemic disease is plausible.
7. Endomyocardial biopsy only when a specific inflammatory, infiltrative, or other cause is suspected and cannot be established noninvasively. Current guideline syntheses agree on clinical evaluation, ECG, laboratory testing, TTE, CMR, natriuretic peptides, and troponin. (sorella2025diagnosisandmanagement pages 1-2, sorella2025diagnosisandmanagement pages 2-3)

### Genetic diagnosis

- Begin with genetic counseling and a **validated cardiomyopathy multigene panel** covering established DCM genes and GATAD1, with deletion/duplication analysis where technically supported.
- Because the GATAD1 relationship is limited, variants other than the reported S102P allele require particularly cautious ACMG/AMP interpretation and segregation/functional evidence.
- Exome or genome sequencing is appropriate when the panel is negative, the phenotype is syndromic, recessive inheritance is suspected, or structural/noncoding variants are plausible.
- RNA sequencing may help resolve splice variants but has no established DCM2B diagnostic signature.
- CMA/karyotype/FISH are not first-line for isolated DCM unless congenital anomalies, developmental features, or a chromosomal disorder are suspected.
- Mitochondrial DNA and repeat-expansion testing are phenotype-directed, not routine GATAD1 tests.

Once a pathogenic familial variant is confirmed, offer **targeted cascade testing** to at-risk relatives. Guidelines emphasize phenotype-directed testing, cascade screening, and mandatory counseling, though protocols vary internationally. (sorella2025diagnosisandmanagement pages 12-13)

### Differential diagnosis
Rule out ischemic cardiomyopathy, myocarditis, sarcoidosis, amyloidosis, hemochromatosis, tachycardia-mediated cardiomyopathy, peripartum cardiomyopathy, alcohol/toxin-associated DCM, endocrine/metabolic disease, congenital/valvular disease, and alternative genetic DCM. Distinguish Duchenne/Becker muscular dystrophy, laminopathy, desmosomal disease, mitochondrial disorders, and Barth syndrome when extracardiac features suggest them.

No newborn population screening is established. Family-based genomic and cardiac screening is the appropriate strategy.

## 11. Outcome and prognosis

No GATAD1-specific survival, transplantation, sudden-death, recovery, or quality-of-life estimates are available. Potential DCM complications include progressive HFrEF, ventricular and atrial arrhythmias, conduction disease, thromboembolism, functional mitral regurgitation, pulmonary hypertension, right-heart failure, transplantation, and premature death.

General prognostic markers include baseline and serial LVEF, ventricular volumes, NYHA class, natriuretic peptides, troponin, renal function, CMR fibrosis, ventricular arrhythmia, syncope, genotype, and response to therapy. The 2025 guideline review identifies persistent evidence gaps in the trajectories of genetic versus gene-elusive DCM and in genotype-informed ICD decisions. Thus, prognosis should be individualized rather than inferred from the DCM2B label. (sorella2025diagnosisandmanagement pages 1-2, sorella2025diagnosisandmanagement pages 12-13)

## 12. Treatment

### Current application
There is **no GATAD1-specific approved drug, gene therapy, RNA therapy, cell therapy, or clinical trial** in the retrieved evidence. Treat the phenotype according to contemporary DCM/HFrEF practice:

- foundational HFrEF pharmacotherapy: an ARNI or ACE inhibitor/ARB, evidence-based beta blocker, mineralocorticoid-receptor antagonist, and SGLT2 inhibitor when tolerated;
- diuretics for congestion;
- anticoagulation only for standard indications such as atrial fibrillation, intracardiac thrombus, or prior embolism;
- management of arrhythmias and reversible triggers;
- ICD/CRT according to LVEF, symptoms, conduction pattern, arrhythmia history, fibrosis, and individualized genetic risk—not solely because GATAD1 is present;
- durable mechanical circulatory support and cardiac transplantation for refractory advanced heart failure. Guideline syntheses specifically support transplantation for refractory NYHA III–IV disease and mechanical support in suitable advanced-heart-failure candidates. (sorella2025diagnosisandmanagement pages 12-13)

Suggested NCIt concepts include heart-failure pharmacotherapy, angiotensin-receptor neprilysin inhibitor therapy, beta-blocker therapy, mineralocorticoid-receptor antagonist therapy, SGLT2-inhibitor therapy, diuretic therapy, implantable cardioverter-defibrillator placement, cardiac resynchronization therapy, ventricular-assist-device placement, and heart transplantation. Exact NCIt codes should be resolved against the current release.

### Experimental directions
The 2024 14-3-3/NLS finding offers a research mechanism, not a therapeutic target ready for patients. Candidate future approaches include restoring phosphorylation-dependent interaction, correcting S102P, or normalizing GATAD1 trafficking, but intervention could be hazardous because the kinase, relevant developmental stage, direction of trafficking defect, and downstream transcriptional program remain unknown. (rrustemi2024exploringpathogenicmutations pages 80-87, rrustemi2024exploringpathogenicmutations pages 102-107, rrustemi2024exploringpathogenicmutations pages 107-112)

## 13. Prevention

- **Primary prevention:** the inherited allele cannot presently be pharmacologically prevented. Genetic counseling, reproductive carrier testing, prenatal diagnosis, and preimplantation genetic testing may be considered after confirmation of a pathogenic familial genotype.
- **Secondary prevention:** cascade testing plus periodic ECG and cardiac imaging can detect presymptomatic disease. Exact surveillance intervals should be individualized by age, genotype, family history, and baseline findings.
- **Tertiary prevention:** early guideline-directed therapy, vaccination and infection prevention appropriate for heart-failure patients, avoidance of cardiotoxic substances, rhythm surveillance, and timely device/advanced-heart-failure referral.
- **Behavior:** avoid heavy alcohol and illicit stimulants; use shared decision-making for intense exercise and pregnancy. These are general cardiomyopathy precautions, not proven GATAD1-specific protective interventions.

## 14. Other species and natural disease

No naturally occurring GATAD1-DCM2B syndrome was verified in dog, cat, livestock, or wildlife, and there is no zoonotic or transmissible component. Orthologs almost certainly exist in standard vertebrate models, but NCBI Gene and Taxon identifiers should be directly validated before database loading. Comparative relevance lies in conserved phosphorylation, 14-3-3 interaction, nuclear transport, and cardiac-muscle biology—not in cross-species transmission.

## 15. Model organisms and experimental models

The best-verified systems are **in vitro peptide/protein assays**, HEK-293 cells, and engineered human iPSC-derived cardiomyocytes. PRISMA/SILAC screening compared wild-type, phosphorylated, and mutant peptides; structural and calorimetric experiments established phosphorylation-dependent 14-3-3 binding. (rrustemi2024pathogenicmutationsof pages 2-3, rrustemi2024pathogenicmutationsof pages 1-2)

The iPSC-cardiomyocyte model did **not** show a strong S102P-associated proteome or localization phenotype under the reported conditions. This negative result limits mechanistic confidence but does not exclude a phenotype in older, mechanically loaded, metabolically mature, or stressed cardiomyocytes. Appropriate next-generation models include isogenic matured iPSC-cardiomyocytes, engineered heart tissues, knock-in zebrafish or mice, longitudinal stress testing, nuclear-transport reporters, contractility/calcium assays, and single-cell multi-omics. (rrustemi2024exploringpathogenicmutations pages 80-87, rrustemi2024exploringpathogenicmutations pages 107-112)

Although secondary literature mentions zebrafish work in connection with GATAD1-associated DCM, a disease-specific primary animal-model result was not sufficiently verified in the retrieved full text and should not be used as definitive evidence. This caution is particularly important because a 2023 review still classified GATAD1 as a single-family, replication-requiring association. (lipov2023exploringthecomplex pages 6-7)

## Evidence assessment and expert interpretation

The most important current conclusion is not that DCM2B is fully characterized, but that it is **a plausible, molecularly interesting, yet insufficiently replicated GATAD1-associated recessive cardiomyopathy**. Open Targets preserves the association and founding PMID, while the 2023 systematic analysis explicitly downgrades confidence relative to robust recessive cardiomyopathy genes. (OpenTargets Search: Dilated Cardiomyopathy 2B, lipov2023exploringthecomplex pages 6-7)

The major 2024 development is a coherent biochemical hypothesis: S102 phosphorylation creates a 14-3-3 interaction site, and p.Ser102Pro abolishes this regulated interaction. The study’s abstract states that 14-3-3 binding may affect nucleocytoplasmic transport **“by masking a nuclear localisation signal.”** However, absent replication in new families and absent a decisive cardiomyocyte phenotype, this mechanism should be annotated as **supporting functional evidence**, not proof of causality. (rrustemi2024pathogenicmutationsof pages 1-2, rrustemi2024exploringpathogenicmutations pages 80-87, rrustemi2024exploringpathogenicmutations pages 107-112)

### Priority evidence gaps

1. Independent families with segregating biallelic pathogenic GATAD1 variants.
2. Transcript-specific HGVS and current ClinVar/gnomAD review of p.Ser102Pro.
3. Reliable age-of-onset, penetrance, arrhythmia, transplantation, and survival data.
4. Mature cardiomyocyte and knock-in-animal phenotyping.
5. Identification of the S102 kinase and physiologic stimulus.
6. Direct demonstration connecting altered 14-3-3 binding to contractile failure.
7. Disease-specific transcriptomic, epigenomic, proteomic, and spatial/single-cell profiles.
8. Genotype-specific treatment-response and clinical-trial evidence.

## Key sources

- Open Targets disease–target aggregation for **MONDO:0013848/GATAD1**, citing PMID **21965549** and ClinVar RCV000024350. (OpenTargets Search: Dilated Cardiomyopathy 2B)
- Lipov A, et al. *Exploring the complex spectrum of dominance and recessiveness in genetic cardiomyopathies.* **Nature Cardiovascular Research.** Published October 2023; 2:1078–1094. DOI/URL: https://doi.org/10.1038/s44161-023-00346-3. (lipov2023exploringthecomplex pages 6-7, lipov2023exploringthecomplex pages 19-24)
- Rrustemi T, et al. *Pathogenic mutations of human phosphorylation sites affect protein–protein interactions.* **Nature Communications.** Accepted March 11, 2024; 15:3146. DOI/URL: https://doi.org/10.1038/s41467-024-46794-8. (rrustemi2024pathogenicmutationsof pages 1-2)
- Sorella A, et al. *Diagnosis and management of dilated cardiomyopathy: a systematic review of clinical practice guidelines and recommendations.* **European Heart Journal—Quality of Care & Clinical Outcomes.** DOI/URL: https://doi.org/10.1093/ehjqcco/qcae109. Used only for general-DCM diagnosis, epidemiology, and management extrapolation. (sorella2025diagnosisandmanagement pages 1-2, sorella2025diagnosisandmanagement pages 12-13, sorella2025diagnosisandmanagement pages 2-3)

References

1. (OpenTargets Search: Dilated Cardiomyopathy 2B): Open Targets Query (Dilated Cardiomyopathy 2B, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (lipov2023exploringthecomplex pages 6-7): Alex Lipov, Sean J. Jurgens, Francesco Mazzarotto, Mona Allouba, James P. Pirruccello, Yasmine Aguib, Massimo Gennarelli, Magdi H. Yacoub, Patrick T. Ellinor, Connie R. Bezzina, and Roddy Walsh. Exploring the complex spectrum of dominance and recessiveness in genetic cardiomyopathies. Nature Cardiovascular Research, 2:1078-1094, Oct 2023. URL: https://doi.org/10.1038/s44161-023-00346-3, doi:10.1038/s44161-023-00346-3. This article has 40 citations and is from a peer-reviewed journal.

3. (rrustemi2024exploringpathogenicmutations pages 102-107): Trëndelina Rrustemi. Exploring pathogenic mutations at phosphorylation sites through a peptide-based proteomics screen. Text, Oct 2024. URL: https://doi.org/10.18452/28699, doi:10.18452/28699. This article has 0 citations and is from a peer-reviewed journal.

4. (rrustemi2024exploringpathogenicmutations pages 107-112): Trëndelina Rrustemi. Exploring pathogenic mutations at phosphorylation sites through a peptide-based proteomics screen. Text, Oct 2024. URL: https://doi.org/10.18452/28699, doi:10.18452/28699. This article has 0 citations and is from a peer-reviewed journal.

5. (rrustemi2024pathogenicmutationsof pages 1-2): Trendelina Rrustemi, Katrina Meyer, Yvette Roske, Bora Uyar, Altuna Akalin, Koshi Imami, Yasushi Ishihama, Oliver Daumke, and Matthias Selbach. Pathogenic mutations of human phosphorylation sites affect protein–protein interactions. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46794-8, doi:10.1038/s41467-024-46794-8. This article has 33 citations and is from a highest quality peer-reviewed journal.

6. (rrustemi2024exploringpathogenicmutations pages 80-87): Trëndelina Rrustemi. Exploring pathogenic mutations at phosphorylation sites through a peptide-based proteomics screen. Text, Oct 2024. URL: https://doi.org/10.18452/28699, doi:10.18452/28699. This article has 0 citations and is from a peer-reviewed journal.

7. (sorella2025diagnosisandmanagement pages 1-2): Anna Sorella, Kristian Galanti, Lorena Iezzi, Sabina Gallina, Selma F Mohammed, Neha Sekhri, Mohammed Majid Akhtar, Sanjay K Prasad, Choudhary Anwar Ahmed Chahal, Fabrizio Ricci, and Mohammed Yunus Khanji. Diagnosis and management of dilated cardiomyopathy: a systematic review of clinical practice guidelines and recommendations. European Heart Journal. Quality of Care & Clinical Outcomes, 11:206-222, Dec 2025. URL: https://doi.org/10.1093/ehjqcco/qcae109, doi:10.1093/ehjqcco/qcae109. This article has 44 citations.

8. (sorella2025diagnosisandmanagement pages 2-3): Anna Sorella, Kristian Galanti, Lorena Iezzi, Sabina Gallina, Selma F Mohammed, Neha Sekhri, Mohammed Majid Akhtar, Sanjay K Prasad, Choudhary Anwar Ahmed Chahal, Fabrizio Ricci, and Mohammed Yunus Khanji. Diagnosis and management of dilated cardiomyopathy: a systematic review of clinical practice guidelines and recommendations. European Heart Journal. Quality of Care & Clinical Outcomes, 11:206-222, Dec 2025. URL: https://doi.org/10.1093/ehjqcco/qcae109, doi:10.1093/ehjqcco/qcae109. This article has 44 citations.

9. (sorella2025diagnosisandmanagement pages 12-13): Anna Sorella, Kristian Galanti, Lorena Iezzi, Sabina Gallina, Selma F Mohammed, Neha Sekhri, Mohammed Majid Akhtar, Sanjay K Prasad, Choudhary Anwar Ahmed Chahal, Fabrizio Ricci, and Mohammed Yunus Khanji. Diagnosis and management of dilated cardiomyopathy: a systematic review of clinical practice guidelines and recommendations. European Heart Journal. Quality of Care & Clinical Outcomes, 11:206-222, Dec 2025. URL: https://doi.org/10.1093/ehjqcco/qcae109, doi:10.1093/ehjqcco/qcae109. This article has 44 citations.

10. (rrustemi2024pathogenicmutationsof pages 2-3): Trendelina Rrustemi, Katrina Meyer, Yvette Roske, Bora Uyar, Altuna Akalin, Koshi Imami, Yasushi Ishihama, Oliver Daumke, and Matthias Selbach. Pathogenic mutations of human phosphorylation sites affect protein–protein interactions. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46794-8, doi:10.1038/s41467-024-46794-8. This article has 33 citations and is from a highest quality peer-reviewed journal.

11. (lipov2023exploringthecomplex pages 19-24): Alex Lipov, Sean J. Jurgens, Francesco Mazzarotto, Mona Allouba, James P. Pirruccello, Yasmine Aguib, Massimo Gennarelli, Magdi H. Yacoub, Patrick T. Ellinor, Connie R. Bezzina, and Roddy Walsh. Exploring the complex spectrum of dominance and recessiveness in genetic cardiomyopathies. Nature Cardiovascular Research, 2:1078-1094, Oct 2023. URL: https://doi.org/10.1038/s44161-023-00346-3, doi:10.1038/s44161-023-00346-3. This article has 40 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Dilated_Cardiomyopathy_2B-deep-research-falcon_artifacts/artifact-00.md)