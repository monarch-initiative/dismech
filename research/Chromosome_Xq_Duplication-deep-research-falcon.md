---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-12T10:09:30.224816'
end_time: '2026-08-12T10:17:56.141972'
duration_seconds: 505.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chromosome Xq Duplication
  mondo_id: ''
  category: Genetic
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
  path: Chromosome_Xq_Duplication-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chromosome Xq Duplication
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Chromosome Xq Duplication** covering all of the
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
- **Disease Name:** Chromosome Xq Duplication
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Chromosome Xq Duplication** covering all of the
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


# Chromosome Xq Duplication: Disease Characteristics Research Report

**Evidence cutoff:** Searches emphasized literature published through 2024 and ClinicalTrials.gov records current in the retrieved registry. **Critical scope note:** “chromosome Xq duplication” is not a single molecular disease. It is an umbrella cytogenomic finding encompassing duplications of different portions of the X-chromosome long arm. Interpretation must retain the exact interval, copy number, orientation, insertion/translocation context, sex, and X-chromosome-inactivation (XCI) pattern. The best-characterized entities are **MECP2 duplication syndrome at Xq28** and **STAG2 dosage-related Xq25 duplication cohesinopathy**.

The following table summarizes the principal entities.

| entity/interval | principal dosage-sensitive genes | characteristic phenotype | inheritance/sex effects | strongest evidence |
|---|---|---|---|---|
| Broad partial Xq duplication (heterogeneous larger duplications across Xq, e.g., Xq23-q26.3) | Interval-dependent; reported neurodevelopmental genes in one 20 Mb Xq23-q26.3 case included **ARHGEF6, PHF6, HPRT1, SLC9A6** | Variable but commonly developmental delay/intellectual disability, short stature, microcephaly, and multiple congenital findings; a 2023 adult female with de novo inverted tandem Xq23-q26.3 duplication had **extremely short stature** and **mild mental deficiency** | Not a single syndrome; phenotype depends on duplicated segment and X-inactivation. Females may be unaffected or variably affected with **skewed/non-random X-inactivation**; males are often more severely affected (pehlivan2024structuralvariantallelic pages 1-2) | 2023 case report delineating de novo inverted tandem Xq23-q26.3 duplication in an adult female; review-style statements that partial Xq duplications are associated with ID/short stature and female phenotype depends on X-inactivation (pehlivan2024structuralvariantallelic pages 1-2) |
| **Xq25 STAG2 duplication cohesinopathy** | **STAG2** is the shortest-region-of-overlap and principal driver; neighboring duplicated genes can include **XIAP, THOC2, GRIA3, SH2D1A** | Intellectual disability (often mild-moderate), behavioral problems, seizures in about one-third, autism in a minority, characteristic facial features; more severe disease with **triplication** | Mainly affects males; female carriers show variable outcomes from normal to borderline or mild ID, with clinically important effects linked to **skewed X-inactivation** | 2015 cohort of **28 affected males** (15 familial, 13 singleton) identified through ~27,000 males tested for neurodevelopmental delay; duplicated intervals **202-746 kb**; behavioral problems **68%**, seizures **32%**, short stature **21%** (kumar2015increasedstag2dosagedefinesa pages 2-2, kumar2015increasedstag2dosagedefinesa pages 2-3, kumar2015increasedstag2dosagedefinesa pages 3-4) |
| **MECP2 duplication syndrome, Xq28 (MRXSL)** | **MECP2** is the major disease-contributing gene; nearby genes may modify severity, especially **RAB39B**, and sometimes **IRAK1, L1CAM, GDI1** | Core phenotype: infantile hypotonia, severe developmental delay/intellectual disability, poor/absent speech, progressive spasticity, recurrent respiratory infections, epilepsy, GI problems, autistic features, dysmorphism; severity worsens with **triplication** and more complex structures | X-linked disorder affecting primarily males; estimated prevalence about **1/100,000 live male births** in one 2024 paper and **1/150,000 males** in a 2022 review. Female carriers often milder due to X-inactivation, but affected females occur. In the 2024 cohort, terminal duplications had more **de novo** events than tandem duplications | 2024 deep-genomic cohort of **137 individuals**: duplication sizes **64.6 kb-16.5 Mb**; structural classes were tandem **48%**, terminal **22%**, inverted triplication **20%**, other complex rearrangements **10%**; genotype-phenotype analyses showed worsening of survival and neurologic severity from tandem to triplication, with MECP2 RNA-protein correlation (pehlivan2024structuralvariantallelic pages 1-2, pehlivan2024structuralvariantallelic pages 20-21). Clinical synthesis review in 2022 summarizes 20 years of phenotype and prevalence (ta2022abriefhistory pages 1-2, ta2022abriefhistory pages 16-17, ta2022abriefhistory pages 10-11) |
| Distal **Xq28 duplications excluding MECP2** (including K/L-mediated and int22h1/int22h2-mediated regions) | Does **not** include **MECP2**; likely multigenic distal Xq28 dosage effects rather than a single confirmed driver | Can resemble MECP2 duplication syndrome: regressive intellectual disability, progressive neurologic disorder/spasticity, epilepsy, recurrent infections, and brain MRI abnormalities | Sex/inheritance effects not established as clearly as classic MECP2 duplication syndrome; evidence is currently based on small case numbers/case reports | 2023 case report of a **17-year-old boy** with a **1.2 Mb distal Xq28 duplication** spanning both K/L-mediated and int22h1/int22h2-mediated regions: epilepsy from age 6, progressive lower-extremity spasticity requiring surgery at 14, recurrent infection, and hypoplasia of corpus callosum/cerebellum/brain stem; authors concluded that **MECP2 alone may not explain all symptoms** of distal Xq28 duplication (akahoshi2023duplicationwithintwo pages 1-2) |


*Table: This table summarizes the main clinically relevant Xq duplication entities discussed in the evidence gathered so far. It distinguishes the broad heterogeneous category from better-defined subtypes such as Xq25/STAG2 and Xq28/MECP2 duplications, which is useful for disease-scope clarification and genotype-phenotype interpretation.*

## 1. Disease information

### Definition and identifiers

A chromosome Xq duplication is a germline copy-number gain involving part of Xq. Large duplications may encompass many genes and produce a contiguous-gene syndrome; smaller recurrent or nonrecurrent gains may define gene-dosage disorders. Clinical effects range from apparently unaffected female carriers to severe congenital or progressive neurodevelopmental disease, particularly in hemizygous males.

The most established subtype is **MECP2 duplication syndrome (MDS)**, also called **X-linked intellectual developmental disorder, Lubs type; MRXSL; Lubs X-linked mental retardation syndrome**, caused by copy-number gain spanning **MECP2** at Xq28. Its established identifier is **OMIM/MIM 300260**; **MECP2** itself is OMIM 300005. The 2024 Genome Medicine paper defines MRXSL as “a neurodevelopmental disorder caused by copy number gains spanning MECP2.” (pehlivan2024structuralvariantallelic pages 1-2)

A second defined subtype is **Xq25 duplication/STAG2 duplication syndrome**, described as an increased-STAG2-dosage cohesinopathy. Broad synonyms include *partial duplication of Xq*, *Xq partial trisomy*, *Xq microduplication syndrome*, and interval-specific terms such as *Xq23–q26.3 duplication* or *distal Xq28 duplication*.

No single disease-specific ICD-10, ICD-11, or MeSH code adequately represents every Xq duplication. Coding normally uses a congenital chromosomal-abnormality/CNV code plus the clinical manifestations. A single umbrella MONDO identifier could not be verified from the retrieved primary literature; database implementation should therefore map the exact named syndrome where available rather than assign the MDS identifier to every Xq gain.

**Data provenance:** Published evidence is aggregated from case reports, cross-sectional case series, laboratory cohorts, and disease reviews—not population EHR surveillance. The major MDS review emphasizes that prior data were cross-sectional and incompletely longitudinal; it called for an international registry and an MDS-specific severity scale. (ta2022abriefhistory pages 16-17)

## 2. Etiology

### Causal factors

The cause is a **constitutional structural variant**, usually a duplication or triplication, generated by genomic rearrangement. In MDS, gains can be tandem, terminal, insertional/translocation-associated, recombinant, inverted triplications, or other complex genomic rearrangements. In 137 affected individuals, sizes ranged from **64.6 kb to 16.5 Mb**: tandem duplications 48%, terminal duplications 22%, inverted triplications 20%, and other complex rearrangements 10%. Among terminal events, 65% were translocations and 23% recombinant chromosomes. (pehlivan2024structuralvariantallelic pages 1-2)

The same cohort found de novo events disproportionately among terminal duplications—65%, compared with 17% among tandem duplications—indicating that rearrangement architecture informs recurrence counseling. (pehlivan2024structuralvariantallelic pages 1-2)

### Genetic risk and modifiers

* **MECP2 copy gain** is the primary causal factor for classic MDS. Triplication and higher RNA/protein dosage generally cause more severe disease. Nearby **RAB39B, GDI1, IRAK1, L1CAM**, and genes introduced or disrupted by translocations can modify particular manifestations.
* **STAG2 copy gain** is the best-supported driver of Xq25 duplication cohesinopathy. In a 28-male cohort, the shortest overlapping gain contained STAG2 alone; some larger gains included **XIAP, THOC2, GRIA3**, or **SH2D1A**. (kumar2015increasedstag2dosagedefinesa pages 2-2, kumar2015increasedstag2dosagedefinesa pages 3-4)
* Distal Xq28 duplications lacking MECP2 can nevertheless produce an MDS-like phenotype, indicating that MECP2 does not explain every distal-Xq28 dosage phenotype. A 2023 report described a 1.2-Mb gain spanning K/L-mediated and int22h1/int22h2-mediated regions without MECP2. (akahoshi2023duplicationwithintwo pages 1-2)
* In females, favorable skewing that preferentially inactivates the duplicated X can be protective; unfavorable or incomplete skewing permits functional disomy and disease. Female STAG2 carriers ranged from normal cognition to borderline or mild intellectual disability. (kumar2015increasedstag2dosagedefinesa pages 2-3, kumar2015increasedstag2dosagedefinesa pages 3-4)

These CNVs are generally too rare and structurally heterogeneous for meaningful population allele frequencies. A pathogenic dosage gain should not be summarized as a conventional SNV allele frequency; classification requires ACMG/ClinGen CNV criteria, gene dosage evidence, inheritance, and phenotype concordance.

### Non-genetic risk, protective factors, and gene–environment interaction

No toxin, diet, infection, lifestyle, occupation, or behavior is known to cause a constitutional Xq duplication. Maternal or paternal age effects are not established. Respiratory infections, immobility, nutrition, and antiseizure-drug adverse effects can modify morbidity or precipitate regression but do not cause the CNV. In the 2024 cohort, regression was attributed to seizure onset in 12 individuals, refractory seizures in 17, infection in six, and antiseizure-medication effects in four. (pehlivan2024structuralvariantallelic pages 13-14)

No validated environmental or genetic “protective variant” has been identified. The main established protective mechanism is favorable XCI in heterozygous females.

## 3. Phenotypes

Phenotype is interval-specific. The following profile applies primarily to MDS, for which the strongest quantitative data exist.

### Core neurodevelopmental phenotype

* **Infantile hypotonia**—congenital/early infancy, common and often later accompanied by appendicular hypertonia or progressive spasticity. Suggested HPO: *Hypotonia* **HP:0001252**, *Spasticity* **HP:0001257**.
* **Global developmental delay and intellectual disability**—usually severe in MDS, mild-to-moderate more often in STAG2 duplication. Suggested HPO: **HP:0001263**, **HP:0001249**.
* **Poor or absent speech** and impaired adaptive function; HPO: *Absent speech* **HP:0001344**, *Delayed speech and language development* **HP:0000750**.
* **Epilepsy**—age-dependent and potentially near-universal in older MDS cohorts. Across 2024 structural groups, observed prevalence was 40–59%; mean/representative onset became earlier with increasing complexity: tandem 8.4 years, other complex 8.2 years, terminal 5.6 years, translocation 4 years 10 months, and triplication under 2 years. Epilepsy is a major cause of regression. HPO: **HP:0001250**. (pehlivan2024structuralvariantallelic pages 20-21, pehlivan2024structuralvariantallelic pages 13-14)
* **Autistic and behavioral features**—in the 2024 cohort, 109/127 (85.8%) had at least one of repetitive movement, poor eye contact, or sensory sensitivity in addition to poor speech. A 2022 synthesis reported formal autism diagnoses in 34/50 (68%), gaze avoidance in 44/61 (72%), impaired social interaction in 38/46 (83%), stereotypies in 158/285 (55%), and bruxism in 102/156 (65%). Suggested HPO: *Autistic behavior* **HP:0000729**, *Stereotypic behavior* **HP:0000733**, *Bruxism* **HP:0003763**. (pehlivan2024structuralvariantallelic pages 13-14, ta2022abriefhistory pages 10-11)

### Other frequent manifestations

* **Recurrent respiratory infections**, often beginning in childhood, are a cardinal source of hospitalization and premature mortality. HPO: *Recurrent respiratory infections* **HP:0002205**.
* **Feeding, chewing, and swallowing difficulty** exceeded 80% across MDS structural groups; tube-feeding need increased with genomic severity. Gastroesophageal reflux and constipation are common. Suggested HPO: *Dysphagia* **HP:0002015**, *Gastroesophageal reflux* **HP:0002020**, *Constipation* **HP:0002019**. (pehlivan2024structuralvariantallelic pages 20-21)
* **Sleep disorders:** insomnia occurred in 62/118 (52.5%) and sleep apnea in 63/114 (55.2%); apnea rose from 48.2% in tandem duplications to 100% in the two triplication subjects with data. Most was obstructive. HPO: *Insomnia* **HP:0100785**, *Obstructive sleep apnea* **HP:0002870**. (pehlivan2024structuralvariantallelic pages 13-14)
* **Dysautonomia** occurred in 105/121 (86.7%), bruxism in 81/112 (72.3%), and high pain tolerance in 85/109 (77.9%) in the 2024 cohort. HPO: *Autonomic nervous system dysfunction* **HP:0002270**, *Reduced sensitivity to pain* **HP:0007328**. (pehlivan2024structuralvariantallelic pages 13-14)
* **Musculoskeletal morbidity:** 49/93 (52.6%) had abnormalities, including fractures (26), osteopenia/osteoporosis (13), scoliosis (13), and contractures (9). Suggested HPO: **HP:0000939** osteoporosis, **HP:0002650** scoliosis, **HP:0001371** contracture. (pehlivan2024structuralvariantallelic pages 13-14)
* **Vision:** 71/117 (60.6%) had predominantly refractive error or strabismus. The 2022 review reported strabismus in 51/73 (70%). HPO: *Strabismus* **HP:0000486**. (pehlivan2024structuralvariantallelic pages 13-14, ta2022abriefhistory pages 10-11)
* **Head growth/dysmorphism:** the review reported microcephaly in 45/195 (23%), macrocephaly in 29/169 (17%), midface hypoplasia in 67/99 (68%), open-mouth appearance in 59/72 (82%), and large ears in 83/133 (62%). Dysmorphism changes with age. (ta2022abriefhistory pages 10-11)
* **Genitourinary abnormalities** include hypogenitalism/micropenis, urinary retention, stones, hydronephrosis, vesicoureteral reflux, and congenital kidney/urinary-tract anomalies; severity was greater in triplication/terminal groups. (pehlivan2024structuralvariantallelic pages 13-14)

### Xq25/STAG2 phenotype

Among 28 affected males, intellectual disability was usually mild-to-moderate, behavioral problems occurred in 68%, seizures in 32%, short stature in 21%, and autism was reported in four. Facial findings included malar flatness (23/27), prognathism (16/26), and full lips (15/26). MRI findings included cerebellar-vermis hypoplasia, thin corpus callosum, and prominent subarachnoid spaces. (kumar2015increasedstag2dosagedefinesa pages 2-3)

### Quality of life

No robust disease-specific EQ-5D or SF-36 dataset was identified. Severe communication and mobility limitations, epilepsy, tube feeding, recurrent hospitalization, sleep disruption, and dependence in activities of daily living imply major patient and caregiver burden. A prospective Ionis natural-history study measured the Quality-of-Life Inventory–Disability alongside communication, adaptive behavior, seizure, EEG, and biomarker outcomes, but published outcome results were not available in the retrieved record. (NCT06014541 chunk 1)

## 4. Genetic and molecular information

### Genes and variants

The causal lesion is a **germline structural CNV**, not typically a somatic mutation. Relevant genes include:

* **MECP2** at Xq28: dosage-sensitive nuclear methylated-DNA reader/transcriptional modulator; increased intact-gene copy number causes MDS.
* **STAG2** at Xq25: cohesin-complex component; increased dosage perturbs transcriptional networks and defines a duplication cohesinopathy. (kumar2015increasedstag2dosagedefinesa pages 2-2)
* Interval-dependent contributors: **RAB39B, GDI1, IRAK1, L1CAM, XIAP, THOC2, GRIA3, SH2D1A, ARHGEF6, PHF6, HPRT1**, and **SLC9A6**.

Variant classes include tandem duplication, insertional duplication, terminal duplication, unbalanced translocation, recombinant X chromosome, duplication–triplication/inverted-duplication structures, and larger cytogenetically visible partial trisomies. Genome position should be stored using the tested reference build and HGVS/ISCN-compatible coordinates.

Partial duplication of only the first two MECP2 exons was found in an otherwise neurologically asymptomatic 12-year-old male, supporting the requirement for an intact dosage gain rather than any overlap with MECP2. (pehlivan2024structuralvariantallelic pages 20-21)

### Expression and epigenetics

MeCP2 binds methylated cytosines, especially CG and CAC contexts, and fine-tunes thousands of neuronal genes. It can repress or activate transcription, alter chromatin, and participate in RNA processing. It is nuclear, ubiquitous, and especially abundant in postnatal neurons. (pehlivan2024structuralvariantallelic pages 1-2, ta2022abriefhistory pages 1-2)

In patient lymphoblastoid cells, duplications generally produced approximately twofold MECP2 RNA and protein, although some exceeded twofold. RNA and protein were correlated (Pearson R=0.6; p<0.05). Triplications had significantly greater MECP2 transcript abundance than duplication classes. (pehlivan2024structuralvariantallelic pages 20-21, pehlivan2024structuralvariantallelic pages 1-2)

XCI is the principal epigenetic modifier in females. Blood XCI may not perfectly represent brain XCI, so it is informative but not determinative.

## 5. Environmental information

No causal environmental, lifestyle, infectious, dietary, radiation, or occupational exposure is established. Infectious agents are complications rather than etiologic triggers. Standard immunization, nutrition, airway care, physical activity within ability, and avoidance of aspiration or prolonged immobility may reduce complications but do not prevent the underlying disease.

## 6. Mechanism and pathophysiology

### MECP2 dosage causal chain

**Structural gain spanning intact MECP2 → increased MECP2 RNA and protein → abnormal binding/modulation across methylated neuronal chromatin → widespread transcriptional and synaptic-network dysregulation → impaired postnatal neuronal maturation and circuit function → hypotonia, developmental impairment, epilepsy, autistic features, and progressive spasticity.** Greater dosage and complex rearrangements add earlier seizures, poorer development, microcephaly, organ abnormalities, and reduced survival. The 2024 authors concluded that “MECP2 is the major disease contributing gene since its dosage and the structure of CNV drive the phenotype.” (pehlivan2024structuralvariantallelic pages 20-21)

Suggested GO terms include **DNA methylation-dependent heterochromatin assembly**, **regulation of transcription by RNA polymerase II**, **chromatin organization**, **regulation of synaptic plasticity**, **neuron maturation**, and **nervous-system development**. Relevant cellular compartments are **nucleus/chromatin** (GO cellular component) and synaptic neuronal networks downstream. Suggested Cell Ontology targets include **neuron (CL:0000540)**, neural progenitor cell, excitatory neuron, inhibitory neuron, and glial cells; the exact vulnerable cell class remains incompletely resolved.

### STAG2 dosage chain

**Xq25 gain → increased STAG2 dosage → altered cohesin stoichiometry/chromatin-loop and transcriptional regulation → dysregulated neurodevelopmental gene networks, including increased OPHN1 expression in studied cells → intellectual disability, behavioral problems, and variably epilepsy/autism.** This is a dosage-gain cohesinopathy, distinct from STAG2 loss-of-function disease. (kumar2015increasedstag2dosagedefinesa pages 2-2)

Suggested GO terms: **sister chromatid cohesion**, **chromosome organization**, **chromatin organization**, **regulation of transcription**, and **nervous-system development**.

### Other systems and omics

Recurrent infections may reflect aspiration, impaired airway clearance, central/neuromuscular dysfunction, and possibly dosage effects of immune-related genes such as IRAK1, but no single immune mechanism explains all patients. No reproducible disease-specific metabolomic, lipidomic, or proteomic signature is established.

The major current multi-omics advance is the 2024 integration of array/short- and long-read WGS, optical mapping, RNA sequencing, protein measurement, and deep HPO phenotyping in 137 individuals. It demonstrated genome-structure-dependent severity and provides a rationale for measuring baseline MECP2 expression before dose-reduction therapy. (pehlivan2024structuralvariantallelic pages 4-5, pehlivan2024structuralvariantallelic pages 1-2)

No sufficiently replicated single-cell or spatial-transcriptomic human MDS atlas was identified.

## 7. Anatomical structures affected

The **central nervous system** is primary: cerebral cortex and distributed neuronal circuits, corticospinal pathways, white matter, corpus callosum, cerebellum, and brainstem. A distal-Xq28 case had hypoplasia of the corpus callosum, cerebellum, and brainstem plus reduced/deep-white-matter abnormalities. (akahoshi2023duplicationwithintwo pages 1-2)

Suggested UBERON concepts include **brain (UBERON:0000955)**, **cerebral cortex (UBERON:0000956)**, corpus callosum, cerebellum **UBERON:0002037**, brainstem **UBERON:0002298**, spinal cord, peripheral skeletal muscle, lung, gastrointestinal tract, kidney/urinary tract, eye, and skeleton.

Secondary systems include respiratory, gastrointestinal, musculoskeletal, genitourinary, ocular, sleep/upper-airway, and autonomic systems. There is no consistent lateralization. At subcellular level, MeCP2 acts primarily in the **nucleus/chromatin**; STAG2 acts in nuclear cohesin complexes.

## 8. Temporal development

The duplication is congenital and lifelong. Hypotonia and developmental delay usually appear in infancy; speech and motor delay become evident in early childhood. Spasticity, epilepsy, scoliosis, contractures, feeding impairment, and loss of skills may emerge or worsen over years. Epilepsy becomes more frequent with age, and its onset is earlier in triplication/complex rearrangements. (pehlivan2024structuralvariantallelic pages 20-21, pehlivan2024structuralvariantallelic pages 13-14)

The course is generally chronic and variably progressive rather than relapsing-remitting. Regression is often linked to epilepsy, refractory seizures, infection, or medication effects. There is no spontaneous molecular remission. Early developmental therapy, prevention of aspiration/infection, and early seizure control represent practical windows for limiting secondary disability.

## 9. Inheritance and population

MDS is an **X-linked genomic disorder** predominantly affecting males. Many tandem duplications are inherited from heterozygous mothers who are asymptomatic or mildly affected because of favorable XCI; de novo and paternal-origin events occur, especially with complex or terminal structures. A 2024 Chinese family had a 14.45-Mb Xq27.1–q28 duplication inherited by an affected boy from a mildly affected mother. (zeng2024geneticanalysisof pages 2-5, zeng2024geneticanalysisof pages 1-2)

For a carrier mother, the theoretical risk per pregnancy is 50% of transmitting the duplicated X; clinical severity is sex- and XCI-dependent. Affected males transmit their X to all daughters and no sons, although survival and reproductive fitness may limit observed transmission. Germline mosaicism is possible but not quantified. No anticipation, founder effect, consanguinity association, or population-specific enrichment is established.

For classic MDS, estimated live-birth prevalence is approximately **0.65/100,000 overall (about 1/150,000)** and approximately **1/100,000 male live births** in the cited Australian estimate; underdiagnosis is likely. (ta2022abriefhistory pages 1-2)

No reliable prevalence or incidence exists for the umbrella category or STAG2 duplication. The STAG2 study found 28 affected males, including 15 from six families and 13 singletons, through systematic/clinical analysis that included approximately 27,000 males with neurodevelopmental delay; this is ascertainment data, not population prevalence. (kumar2015increasedstag2dosagedefinesa pages 2-2)

## 10. Diagnostics

### Recommended approach

1. **Clinical recognition:** congenital hypotonia, severe developmental/speech delay, progressive spasticity, epilepsy, recurrent respiratory infection, GI dysfunction, autism-like behavior, or an X-linked family history.
2. **Chromosomal microarray (CMA):** preferred first-line test for unexplained developmental delay, ID, autism, or congenital anomalies because it defines dosage and approximate coordinates. CMA does not reliably resolve orientation, insertion site, or all complex structures.
3. **Orthogonal confirmation:** MLPA, qPCR, ddPCR, CNV-seq, or another validated dosage assay; test parents.
4. **Karyotype/FISH:** important for large duplications, terminal gains, insertional rearrangements, unbalanced translocations, and reproductive-risk assessment.
5. **WGS/long-read sequencing and optical genome mapping:** useful when breakpoints and structural architecture affect prognosis or trial eligibility. In 2024, apparent tandem gains on array were reclassified as inverted or insertional/complex events using WGS and optical mapping. (pehlivan2024structuralvariantallelic pages 20-21, pehlivan2024structuralvariantallelic pages 4-5)
6. **XCI testing in females:** may help explain phenotype but should not be treated as a brain-specific functional assay.

WES can detect exon-level CNVs but may miss or mischaracterize structural complexity; it should not replace genome-wide CNV analysis. The 2024 pedigree diagnosis combined G-banding, WES, CNV-seq, and family validation. (zeng2024geneticanalysisof pages 1-2)

### Clinical assessment and surveillance

Baseline and periodic evaluations should include developmental/adaptive and communication testing; neurological examination; EEG when seizures or regression are suspected; swallow/feeding and nutritional assessment; respiratory and aspiration history; sleep study when apnea is suspected; orthopedic assessment; vision/hearing; renal/genitourinary evaluation; and brain MRI when seizures, regression, focal signs, or trial criteria warrant it.

There is no biochemical enzyme assay or pathognomonic circulating biomarker. CSF/blood MeCP2, plasma proteomics, EEG/evoked potentials, pupillometry, and disease-severity scales are investigational biomarkers. (NCT06014541 chunk 1)

### Differential diagnosis

Principal differentials include Rett syndrome/MECP2 loss of function, CDKL5 and FOXG1 disorders, Angelman syndrome, Phelan–McDermid syndrome, cerebral palsy, mitochondrial disease, other X-linked ID syndromes, and other Xq CNVs. Distinguishing evidence is an intact-gene copy-number gain spanning the relevant Xq interval. Distal Xq28 duplications lacking MECP2 and Xq25/STAG2 gains should not be mislabeled as classic MDS. (kumar2015increasedstag2dosagedefinesa pages 2-2, akahoshi2023duplicationwithintwo pages 1-2)

No population newborn screening is available. Cascade testing of relatives, prenatal diagnosis by CVS/amniocentesis, and preimplantation genetic testing for a known familial CNV are technically feasible.

## 11. Outcome and prognosis

Prognosis varies greatly with interval, sex, XCI, copy number, structure, epilepsy, infection burden, feeding/respiratory impairment, and associated deletion/translocation. Tandem MECP2 duplications generally had the least severe profile, followed by other complex duplications, terminal/translocation-associated duplications, and triplications. The 2024 analysis found progressively worse survival, developmental level, microcephaly, epilepsy timing, and genitourinary/ocular abnormalities along this gradient. (pehlivan2024structuralvariantallelic pages 1-2)

Classic MDS can cause premature death, often related to recurrent respiratory infection, aspiration, epilepsy, or severe neurologic impairment; historical summaries report deaths before age 25 in severe cases, but no reliable universal five- or ten-year survival percentage exists. (neri2018x‐linkedintellectualdisability pages 4-6, NCT06615206 chunk 1)

Long-term morbidity includes severe communication and adaptive disability, loss of mobility, refractory epilepsy, tube-feeding dependence, recurrent hospitalization, sleep apnea, scoliosis, contractures, osteoporosis/fractures, and caregiver burden. Recovery of the constitutional duplication does not occur; functional gains are possible with rehabilitation and complication control. Disease-specific validated prognostic biomarkers remain investigational.

## 12. Treatment

### Current standard care

No approved curative or CNV-correcting therapy was identified. Management is multidisciplinary and symptom-directed:

* individualized antiseizure therapy and rescue planning;
* vaccination, prompt treatment of infection, airway-clearance support, aspiration assessment, and pulmonology input;
* feeding therapy, reflux/constipation treatment, nutritional support, and gastrostomy when oral intake is unsafe or inadequate;
* physical and occupational therapy, mobility/orthotic aids, and management of spasticity, contractures, scoliosis, and low bone density;
* speech-language therapy and augmentative/alternative communication;
* behavioral, sleep, ophthalmologic, audiologic, urologic/nephrologic, and genetic-counseling support.

A distal-Xq28 case received physical, occupational, and speech therapy; the 2024 Chinese case illustrates acute antibiotic treatment for recurrent severe infection, but neither report establishes disease-specific response rates. (zeng2024geneticanalysisof pages 2-5, akahoshi2023duplicationwithintwo pages 1-2)

Suggested NCIt intervention concepts include **physical therapy**, **occupational therapy**, **speech therapy**, **antiepileptic therapy**, **gastrostomy**, **noninvasive ventilation**, **genetic counseling**, **antisense oligonucleotide therapy**, and **gene therapy**.

### Molecular therapies and 2024 clinical translation

* **ION440/ATTUNE, NCT06430385:** recruiting phase 1/2, randomized, quadruple-blind, sham-controlled multiple-ascending-dose trial of intrathecal ION440 in 48 planned males aged 2–65, followed by open-label extension. It evaluates safety, pharmacokinetics, and pharmacodynamics. Severe terminal/translocation duplications and MECP2 triplications are excluded from Part 1. Registry first posted **28 May 2024**: https://clinicaltrials.gov/study/NCT06430385. (NCT06430385 chunk 1, NCT06430385 chunk 2)
* **HG204/HERO, NCT06615206:** recruiting first-in-human, open-label study of one intracerebroventricular AAV carrying high-fidelity Cas13Y RNA-editing machinery to reduce MECP2 mRNA; planned enrollment is six males aged 2–18. Preclinical registry data report reduced cortical MECP2 RNA/protein, reversal of motor/social abnormalities, and prolonged survival in MDS mice. First posted **26 September 2024**: https://clinicaltrials.gov/study/NCT06615206. (NCT06615206 chunk 1)

These therapies remain experimental; no human efficacy or response-rate conclusion should be inferred from recruitment status. Because some duplication carriers express more than twofold MeCP2, individualized baseline expression and structural classification may be needed to avoid under- or over-suppression. (pehlivan2024structuralvariantallelic pages 20-21)

No established pharmacogenomic prescribing rule, stem-cell therapy, immunotherapy, or surgical cure exists.

## 13. Prevention

The structural event cannot usually be prevented by lifestyle or vaccination.

* **Primary prevention:** genetic counseling and reproductive options for known carriers—prenatal diagnosis, preimplantation genetic testing, donor gametes, or adoption. These reduce recurrence risk but do not alter an established fetal CNV.
* **Secondary prevention:** cascade testing and early molecular diagnosis; early developmental therapy and surveillance before epilepsy, aspiration, malnutrition, sleep apnea, or orthopedic complications become advanced.
* **Tertiary prevention:** vaccination and infection control, aspiration precautions, seizure management, mobility/positioning, bone-health care, nutrition, and respiratory support.

No disease-specific vaccine or prophylactic medication exists. Routine immunization is particularly important because recurrent respiratory infection is a major morbidity.

## 14. Other species and natural disease

No established naturally occurring veterinary syndrome directly equivalent to a human partial Xq duplication was identified. Therefore, breed prevalence, VBO mapping, zoonotic transmission, and cross-species contagion are **not applicable**. The disease is genetic and noninfectious.

Orthologs of MECP2 and cohesin genes including STAG2 are evolutionarily conserved across vertebrates, enabling comparative mechanistic studies. Exact animal NCBI Gene identifiers should be imported directly from NCBI/Alliance rather than inferred from human records.

## 15. Model organisms

The principal models are **transgenic mice overexpressing human or murine Mecp2**, patient-derived lymphoblastoid/fibroblast cells, and potentially iPSC-derived neurons. MeCP2-overexpressing mice reproduce progressive neurologic disease, seizures, spasticity, motor/social abnormalities, and premature death; severity tracks MeCP2 abundance, supporting causal dosage rather than a coincidental neighboring-gene effect. (collins2022rettsyndromeand pages 2-4)

Mouse studies also provide proof of reversibility: reducing MECP2 expression can improve neurological phenotypes and survival, which underlies current ASO and RNA-targeting trials. HG204 preclinical studies reportedly reversed motor/social phenotypes and prolonged survival after intracerebroventricular treatment. (NCT06615206 chunk 1)

Patient lymphoblastoid cells are useful for measuring MECP2 transcript/protein dosage and rearrangement-dependent expression but cannot recapitulate mature brain circuitry. Mouse models cannot fully capture human CNV complexity, female XCI mosaicism, recurrent infection burden, or the contribution of every co-duplicated gene. There is no single model for the broad “Xq duplication” category; models must match the duplicated interval and dosage.

## Evidence limitations and expert interpretation

1. The umbrella label should never replace exact cytogenomic coordinates and gene content.
2. Most phenotype percentages are affected by referral bias, missing data, changing age, and duplicated cases across historical reports. The 2022 review explicitly noted that no prior study supplied a complete longitudinal clinical history. (ta2022abriefhistory pages 16-17)
3. The strongest recent evidence is the 2024 137-person structural/genomic study, but even it is not population-based and some subgroup denominators are small. (pehlivan2024structuralvariantallelic pages 1-2, pehlivan2024structuralvariantallelic pages 13-14)
4. PMIDs were not exposed in the retrieved full-text metadata; DOI URLs and publication dates are therefore supplied rather than risking incorrect PMID assignment.

### Selected primary/recent sources

* Pehlivan D, et al. **Structural variant allelic heterogeneity in MECP2 duplication syndrome provides insight into clinical severity and variability of disease expression.** *Genome Medicine*. Published December 2024. https://doi.org/10.1186/s13073-024-01411-7. Abstract conclusion: “the level of MECP2 is a key determinant of the phenotype,” while rearrangement structure contributes to severity. (pehlivan2024structuralvariantallelic pages 1-2)
* Zeng L, et al. **Genetic analysis of a pedigree with MECP2 duplication syndrome in China.** *BMC Medical Genomics*. Published February 2024. https://doi.org/10.1186/s12920-024-01831-9. (zeng2024geneticanalysisof pages 2-5, zeng2024geneticanalysisof pages 1-2)
* Akahoshi K, et al. **Duplication within two regions distal to MECP2: clinical similarity with MECP2 duplication syndrome.** *BMC Medical Genomics*. Published March 2023. https://doi.org/10.1186/s12920-023-01465-3. The authors concluded that “MECP2 alone may not explain all symptoms” of distal Xq28 duplication. (akahoshi2023duplicationwithintwo pages 1-2)
* Ta D, et al. **A brief history of MECP2 duplication syndrome: 20-years of clinical understanding.** *Orphanet Journal of Rare Diseases*. Published March 2022. https://doi.org/10.1186/s13023-022-02278-w. (ta2022abriefhistory pages 16-17, ta2022abriefhistory pages 1-2)
* Kumar R, et al. **Increased STAG2 dosage defines a novel cohesinopathy with intellectual disability and behavioral problems.** *Human Molecular Genetics*. Published October 2015. https://doi.org/10.1093/hmg/ddv414. (kumar2015increasedstag2dosagedefinesa pages 2-2, kumar2015increasedstag2dosagedefinesa pages 2-3, kumar2015increasedstag2dosagedefinesa pages 3-4)

References

1. (pehlivan2024structuralvariantallelic pages 1-2): Davut Pehlivan, Jesse D. Bengtsson, Sameer S. Bajikar, Christopher M. Grochowski, Ming Yin Lun, Mira Gandhi, Angad Jolly, Alexander J. Trostle, Holly K. Harris, Bernhard Suter, Sukru Aras, Melissa B. Ramocki, Haowei Du, Michele G. Mehaffey, KyungHee Park, Ellen Wilkey, Cemal Karakas, Jesper J. Eisfeldt, Maria Pettersson, Lynn Liu, Marwan S. Shinawi, Virginia E. Kimonis, Wojciech Wiszniewski, Kyle Mckenzie, Timo Roser, Angela M. Vianna-Morgante, Alberto S. Cornier, Ahmed Abdelmoity, James P. Hwang, Shalini N. Jhangiani, Donna M. Muzny, Tadahiro Mitani, Kazuhiro Muramatsu, Shin Nabatame, Daniel G. Glaze, Jawid M. Fatih, Richard A. Gibbs, Zhandong Liu, Anna Lindstrand, Fritz J. Sedlazeck, James R. Lupski, Huda Y. Zoghbi, and Claudia M. B. Carvalho. Structural variant allelic heterogeneity in mecp2 duplication syndrome provides insight into clinical severity and variability of disease expression. Genome Medicine, Dec 2024. URL: https://doi.org/10.1186/s13073-024-01411-7, doi:10.1186/s13073-024-01411-7. This article has 16 citations and is from a highest quality peer-reviewed journal.

2. (kumar2015increasedstag2dosagedefinesa pages 2-2): Raman Kumar, Mark A. Corbett, Bregje W.M. Van Bon, Alison Gardner, Joshua A. Woenig, Lachlan A. Jolly, Evelyn Douglas, Kathryn Friend, Chuan Tan, Hilde Van Esch, Maureen Holvoet, Martine Raynaud, Michael Field, Melanie Leffler, Bartłomiej Budny, Marzena Wisniewska, Magdalena Badura-Stronka, Anna Latos-Bieleńska, Jacqueline Batanian, Jill A. Rosenfeld, Lina Basel-Vanagaite, Corinna Jensen, Melanie Bienek, Guy Froyen, Reinhard Ullmann, Hao Hu, Michael I. Love, Stefan A. Haas, Pawel Stankiewicz, Sau Wai Cheung, Anne Baxendale, Jillian Nicholl, Elizabeth M. Thompson, Eric Haan, Vera M. Kalscheuer, and Jozef Gecz. Increased<i>stag2</i>dosage defines a novel cohesinopathy with intellectual disability and behavioral problems. Human Molecular Genetics, 24:7171-7181, Oct 2015. URL: https://doi.org/10.1093/hmg/ddv414, doi:10.1093/hmg/ddv414. This article has 44 citations and is from a domain leading peer-reviewed journal.

3. (kumar2015increasedstag2dosagedefinesa pages 2-3): Raman Kumar, Mark A. Corbett, Bregje W.M. Van Bon, Alison Gardner, Joshua A. Woenig, Lachlan A. Jolly, Evelyn Douglas, Kathryn Friend, Chuan Tan, Hilde Van Esch, Maureen Holvoet, Martine Raynaud, Michael Field, Melanie Leffler, Bartłomiej Budny, Marzena Wisniewska, Magdalena Badura-Stronka, Anna Latos-Bieleńska, Jacqueline Batanian, Jill A. Rosenfeld, Lina Basel-Vanagaite, Corinna Jensen, Melanie Bienek, Guy Froyen, Reinhard Ullmann, Hao Hu, Michael I. Love, Stefan A. Haas, Pawel Stankiewicz, Sau Wai Cheung, Anne Baxendale, Jillian Nicholl, Elizabeth M. Thompson, Eric Haan, Vera M. Kalscheuer, and Jozef Gecz. Increased<i>stag2</i>dosage defines a novel cohesinopathy with intellectual disability and behavioral problems. Human Molecular Genetics, 24:7171-7181, Oct 2015. URL: https://doi.org/10.1093/hmg/ddv414, doi:10.1093/hmg/ddv414. This article has 44 citations and is from a domain leading peer-reviewed journal.

4. (kumar2015increasedstag2dosagedefinesa pages 3-4): Raman Kumar, Mark A. Corbett, Bregje W.M. Van Bon, Alison Gardner, Joshua A. Woenig, Lachlan A. Jolly, Evelyn Douglas, Kathryn Friend, Chuan Tan, Hilde Van Esch, Maureen Holvoet, Martine Raynaud, Michael Field, Melanie Leffler, Bartłomiej Budny, Marzena Wisniewska, Magdalena Badura-Stronka, Anna Latos-Bieleńska, Jacqueline Batanian, Jill A. Rosenfeld, Lina Basel-Vanagaite, Corinna Jensen, Melanie Bienek, Guy Froyen, Reinhard Ullmann, Hao Hu, Michael I. Love, Stefan A. Haas, Pawel Stankiewicz, Sau Wai Cheung, Anne Baxendale, Jillian Nicholl, Elizabeth M. Thompson, Eric Haan, Vera M. Kalscheuer, and Jozef Gecz. Increased<i>stag2</i>dosage defines a novel cohesinopathy with intellectual disability and behavioral problems. Human Molecular Genetics, 24:7171-7181, Oct 2015. URL: https://doi.org/10.1093/hmg/ddv414, doi:10.1093/hmg/ddv414. This article has 44 citations and is from a domain leading peer-reviewed journal.

5. (pehlivan2024structuralvariantallelic pages 20-21): Davut Pehlivan, Jesse D. Bengtsson, Sameer S. Bajikar, Christopher M. Grochowski, Ming Yin Lun, Mira Gandhi, Angad Jolly, Alexander J. Trostle, Holly K. Harris, Bernhard Suter, Sukru Aras, Melissa B. Ramocki, Haowei Du, Michele G. Mehaffey, KyungHee Park, Ellen Wilkey, Cemal Karakas, Jesper J. Eisfeldt, Maria Pettersson, Lynn Liu, Marwan S. Shinawi, Virginia E. Kimonis, Wojciech Wiszniewski, Kyle Mckenzie, Timo Roser, Angela M. Vianna-Morgante, Alberto S. Cornier, Ahmed Abdelmoity, James P. Hwang, Shalini N. Jhangiani, Donna M. Muzny, Tadahiro Mitani, Kazuhiro Muramatsu, Shin Nabatame, Daniel G. Glaze, Jawid M. Fatih, Richard A. Gibbs, Zhandong Liu, Anna Lindstrand, Fritz J. Sedlazeck, James R. Lupski, Huda Y. Zoghbi, and Claudia M. B. Carvalho. Structural variant allelic heterogeneity in mecp2 duplication syndrome provides insight into clinical severity and variability of disease expression. Genome Medicine, Dec 2024. URL: https://doi.org/10.1186/s13073-024-01411-7, doi:10.1186/s13073-024-01411-7. This article has 16 citations and is from a highest quality peer-reviewed journal.

6. (ta2022abriefhistory pages 1-2): Daniel Ta, Jenny Downs, Gareth Baynam, Andrew Wilson, Peter Richmond, and Helen Leonard. A brief history of mecp2 duplication syndrome: 20-years of clinical understanding. Orphanet Journal of Rare Diseases, Mar 2022. URL: https://doi.org/10.1186/s13023-022-02278-w, doi:10.1186/s13023-022-02278-w. This article has 69 citations and is from a peer-reviewed journal.

7. (ta2022abriefhistory pages 16-17): Daniel Ta, Jenny Downs, Gareth Baynam, Andrew Wilson, Peter Richmond, and Helen Leonard. A brief history of mecp2 duplication syndrome: 20-years of clinical understanding. Orphanet Journal of Rare Diseases, Mar 2022. URL: https://doi.org/10.1186/s13023-022-02278-w, doi:10.1186/s13023-022-02278-w. This article has 69 citations and is from a peer-reviewed journal.

8. (ta2022abriefhistory pages 10-11): Daniel Ta, Jenny Downs, Gareth Baynam, Andrew Wilson, Peter Richmond, and Helen Leonard. A brief history of mecp2 duplication syndrome: 20-years of clinical understanding. Orphanet Journal of Rare Diseases, Mar 2022. URL: https://doi.org/10.1186/s13023-022-02278-w, doi:10.1186/s13023-022-02278-w. This article has 69 citations and is from a peer-reviewed journal.

9. (akahoshi2023duplicationwithintwo pages 1-2): Keiko Akahoshi, Eiji Nakagawa, Yu-ichi Goto, and Ken Inoue. Duplication within two regions distal to mecp2: clinical similarity with mecp2 duplication syndrome. BMC Medical Genomics, Mar 2023. URL: https://doi.org/10.1186/s12920-023-01465-3, doi:10.1186/s12920-023-01465-3. This article has 0 citations and is from a peer-reviewed journal.

10. (pehlivan2024structuralvariantallelic pages 13-14): Davut Pehlivan, Jesse D. Bengtsson, Sameer S. Bajikar, Christopher M. Grochowski, Ming Yin Lun, Mira Gandhi, Angad Jolly, Alexander J. Trostle, Holly K. Harris, Bernhard Suter, Sukru Aras, Melissa B. Ramocki, Haowei Du, Michele G. Mehaffey, KyungHee Park, Ellen Wilkey, Cemal Karakas, Jesper J. Eisfeldt, Maria Pettersson, Lynn Liu, Marwan S. Shinawi, Virginia E. Kimonis, Wojciech Wiszniewski, Kyle Mckenzie, Timo Roser, Angela M. Vianna-Morgante, Alberto S. Cornier, Ahmed Abdelmoity, James P. Hwang, Shalini N. Jhangiani, Donna M. Muzny, Tadahiro Mitani, Kazuhiro Muramatsu, Shin Nabatame, Daniel G. Glaze, Jawid M. Fatih, Richard A. Gibbs, Zhandong Liu, Anna Lindstrand, Fritz J. Sedlazeck, James R. Lupski, Huda Y. Zoghbi, and Claudia M. B. Carvalho. Structural variant allelic heterogeneity in mecp2 duplication syndrome provides insight into clinical severity and variability of disease expression. Genome Medicine, Dec 2024. URL: https://doi.org/10.1186/s13073-024-01411-7, doi:10.1186/s13073-024-01411-7. This article has 16 citations and is from a highest quality peer-reviewed journal.

11. (NCT06014541 chunk 1):  Observational Study to Characterize Biomarkers and Disease Progression in Participants With Methyl CpG Binding Protein 2 (MECP2) Duplication Syndrome. Ionis Pharmaceuticals, Inc.. 2023. ClinicalTrials.gov Identifier: NCT06014541

12. (pehlivan2024structuralvariantallelic pages 4-5): Davut Pehlivan, Jesse D. Bengtsson, Sameer S. Bajikar, Christopher M. Grochowski, Ming Yin Lun, Mira Gandhi, Angad Jolly, Alexander J. Trostle, Holly K. Harris, Bernhard Suter, Sukru Aras, Melissa B. Ramocki, Haowei Du, Michele G. Mehaffey, KyungHee Park, Ellen Wilkey, Cemal Karakas, Jesper J. Eisfeldt, Maria Pettersson, Lynn Liu, Marwan S. Shinawi, Virginia E. Kimonis, Wojciech Wiszniewski, Kyle Mckenzie, Timo Roser, Angela M. Vianna-Morgante, Alberto S. Cornier, Ahmed Abdelmoity, James P. Hwang, Shalini N. Jhangiani, Donna M. Muzny, Tadahiro Mitani, Kazuhiro Muramatsu, Shin Nabatame, Daniel G. Glaze, Jawid M. Fatih, Richard A. Gibbs, Zhandong Liu, Anna Lindstrand, Fritz J. Sedlazeck, James R. Lupski, Huda Y. Zoghbi, and Claudia M. B. Carvalho. Structural variant allelic heterogeneity in mecp2 duplication syndrome provides insight into clinical severity and variability of disease expression. Genome Medicine, Dec 2024. URL: https://doi.org/10.1186/s13073-024-01411-7, doi:10.1186/s13073-024-01411-7. This article has 16 citations and is from a highest quality peer-reviewed journal.

13. (zeng2024geneticanalysisof pages 2-5): Lan Zeng, Hui Zhu, Jin Wang, Qiyan Wang, Ying Pang, Zemin Luo, Ai Chen, Shengfang Qin, and Shuyao Zhu. Genetic analysis of a pedigree with mecp2 duplication syndrome in china. BMC Medical Genomics, Feb 2024. URL: https://doi.org/10.1186/s12920-024-01831-9, doi:10.1186/s12920-024-01831-9. This article has 0 citations and is from a peer-reviewed journal.

14. (zeng2024geneticanalysisof pages 1-2): Lan Zeng, Hui Zhu, Jin Wang, Qiyan Wang, Ying Pang, Zemin Luo, Ai Chen, Shengfang Qin, and Shuyao Zhu. Genetic analysis of a pedigree with mecp2 duplication syndrome in china. BMC Medical Genomics, Feb 2024. URL: https://doi.org/10.1186/s12920-024-01831-9, doi:10.1186/s12920-024-01831-9. This article has 0 citations and is from a peer-reviewed journal.

15. (neri2018x‐linkedintellectualdisability pages 4-6): Giovanni Neri, Charles E. Schwartz, Herbert A. Lubs, and Roger E. Stevenson. X‐linked intellectual disability update 2017. American Journal of Medical Genetics Part A, 176:1375-1388, Jun 2018. URL: https://doi.org/10.1002/ajmg.a.38710, doi:10.1002/ajmg.a.38710. This article has 154 citations.

16. (NCT06615206 chunk 1):  A First-in-Human Clinical Trial to Evaluate the Safety, Tolerability, and Efficacy of a Novel CRISPR RNA-editing Therapy in Patients with Mecp2 Duplication Syndrome, a Rare Orphan Disease (HERO). HuidaGene Therapeutics Co., Ltd.. 2024. ClinicalTrials.gov Identifier: NCT06615206

17. (NCT06430385 chunk 1):  ATTUNE: A Study to Evaluate the Safety, Tolerability, Pharmacokinetics, and Pharmacodynamics of Intrathecally-Administered ION440 in Participants With Methyl CpG Binding Protein 2 (MECP2) Duplication Syndrome (MDS). Ionis Pharmaceuticals, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06430385

18. (NCT06430385 chunk 2):  ATTUNE: A Study to Evaluate the Safety, Tolerability, Pharmacokinetics, and Pharmacodynamics of Intrathecally-Administered ION440 in Participants With Methyl CpG Binding Protein 2 (MECP2) Duplication Syndrome (MDS). Ionis Pharmaceuticals, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06430385

19. (collins2022rettsyndromeand pages 2-4): Bridget E Collins and Jeffrey L Neul. Rett syndrome and mecp2 duplication syndrome: disorders of mecp2 dosage. Neuropsychiatric Disease and Treatment, 18:2813-2835, Nov 2022. URL: https://doi.org/10.2147/ndt.s371483, doi:10.2147/ndt.s371483. This article has 89 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Chromosome_Xq_Duplication-deep-research-falcon_artifacts/artifact-00.md)