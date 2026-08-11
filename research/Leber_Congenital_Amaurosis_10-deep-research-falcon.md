---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-26T23:20:06.282965'
end_time: '2026-06-26T23:34:31.135160'
duration_seconds: 864.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Leber Congenital Amaurosis 10
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Leber_Congenital_Amaurosis_10-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Leber_Congenital_Amaurosis_10-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Leber_Congenital_Amaurosis_10-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leber Congenital Amaurosis 10
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leber Congenital Amaurosis 10** covering all of the
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
- **Disease Name:** Leber Congenital Amaurosis 10
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leber Congenital Amaurosis 10** covering all of the
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


# Comprehensive Research Report: Leber Congenital Amaurosis 10 (LCA10)

## 1. Disease Information

### Overview
Leber congenital amaurosis 10 (LCA10) is a severe, autosomal recessive inherited retinal dystrophy caused by biallelic pathogenic variants in the *CEP290* gene (centrosomal protein 290). It represents the most common genetic subtype of Leber congenital amaurosis, accounting for approximately 15–30% of all LCA cases in Caucasian populations and over 20% across multiple cohorts (leroy2021lebercongenitalamaurosis pages 1-2, huang2021leber’scongenitalamaurosis pages 6-7, gong2024infantilenystagmussyndrome—associated pages 4-5). LCA10 typically presents in early infancy with severe visual impairment or blindness, classifying it as one of the most severe forms of inherited retinal degeneration and a leading cause of childhood blindness (leroy2021lebercongenitalamaurosis pages 1-2, leroy2021lebercongenitalamaurosis pages 2-4).

### Key Identifiers

The following table summarizes the core identifiers and defining characteristics of LCA10:

| Field | Value | Notes / Evidence |
|---|---|---|
| Disease name | Leber congenital amaurosis 10 (LCA10) | CEP290-associated subtype of Leber congenital amaurosis; severe inherited retinal degeneration (leroy2021lebercongenitalamaurosis pages 1-2, leroy2021lebercongenitalamaurosis pages 2-4) |
| Disease class | Mendelian inherited retinal disease; ciliopathy | Autosomal recessive retinal ciliopathy caused by biallelic CEP290 loss-of-function variants (leroy2021lebercongenitalamaurosis pages 1-2, huang2021leber’scongenitalamaurosis pages 6-7) |
| OMIM | LCA: **#204000**; **CEP290** gene: **610142** | General LCA OMIM and causal gene OMIM reported in cohort/review sources (zobor2023geneticandclinical pages 1-2, huang2021leber’scongenitalamaurosis pages 6-7) |
| MONDO ID | **MONDO_0018998** | MONDO identifier retrieved for Leber congenital amaurosis in disease-target association context (OpenTargets Search: Leber congenital amaurosis-CEP290) |
| Orphanet | Not confidently established from retrieved evidence | Disease-level rare disease resource exists for LCA broadly, but no subtype-specific Orphanet identifier for LCA10 was confirmed in retrieved sources |
| ICD-10 / ICD-11 | Not confidently established from retrieved evidence | LCA is typically coded within congenital retinal dystrophy/blindness frameworks, but no LCA10-specific ICD code was confirmed in retrieved sources |
| Common synonyms | LCA10; CEP290-associated LCA; CEP290-related retinal degeneration; CEP290-associated inherited retinal degeneration | Synonyms used across review and trial literature (leroy2021lebercongenitalamaurosis pages 1-2, russell2022intravitrealantisenseoligonucleotide pages 1-2, pierce2024geneeditingfor pages 1-3) |
| Causal gene | **CEP290** (centrosomal protein 290) | Top disease-associated target for LCA in Open Targets; encodes a transition-zone/basal body ciliary protein (OpenTargets Search: Leber congenital amaurosis-CEP290, mcdonald2024retinalciliopathiesand pages 7-8, huang2021leber’scongenitalamaurosis pages 6-7) |
| Most common pathogenic variant | **c.2991+1655A>G** (deep intronic; often called IVS26 variant; p.Cys998X consequence via cryptic exon) | Most frequent LCA10-associated variant; creates a cryptic exon and premature stop, reducing normal CEP290 transcript/protein (leroy2021lebercongenitalamaurosis pages 1-2, mcdonald2024retinalciliopathiesand pages 7-8, huang2021leber’scongenitalamaurosis pages 6-7) |
| Inheritance | **Autosomal recessive** | Typically due to biallelic pathogenic CEP290 variants (leroy2021lebercongenitalamaurosis pages 1-2, huang2021leber’scongenitalamaurosis pages 6-7) |
| Estimated prevalence | LCA overall about **1:30,000 to 1:80,000**; ~1:50,000 often cited in Europe/North America | Retrieved evidence provides LCA prevalence range; LCA10 is a major subtype, especially in Caucasian/Northern European cohorts (leroy2021lebercongenitalamaurosis pages 1-2, zobor2023geneticandclinical pages 1-2, huang2021leber’scongenitalamaurosis pages 6-7) |
| Relative frequency within LCA | CEP290 accounts for about **15–30%** of LCA overall; **>20%** in several cohorts; **29%** among LCA cases in one German cohort | Frequency varies by ancestry and cohort (huang2021leber’scongenitalamaurosis pages 6-7, zobor2023geneticandclinical pages 1-2, gong2024infantilenystagmussyndrome—associated pages 4-5) |
| Age at onset | **Congenital / early childhood** | Severe visual impairment usually recognized from birth or in early childhood; often childhood blindness (leroy2021lebercongenitalamaurosis pages 1-2, leroy2021lebercongenitalamaurosis pages 2-4, russell2022intravitrealantisenseoligonucleotide pages 1-2) |
| Core phenotype summary | Severe early-onset cone-rod dystrophy with markedly reduced vision, nystagmus, extinguished or severely reduced ERG, hyperopia/photophobia, progressive photoreceptor degeneration | Common disease-level characteristics across reviews and cohorts (leroy2021lebercongenitalamaurosis pages 2-4, huang2021leber’scongenitalamaurosis pages 6-7) |
| Evidence source type | Aggregated disease-level literature and clinical trial/natural history resources, not EHR-derived | Based on reviews, cohort studies, mechanistic studies, clinical trials, and Open Targets disease-target evidence (OpenTargets Search: Leber congenital amaurosis-CEP290, leroy2021lebercongenitalamaurosis pages 1-2, pierce2024geneeditingfor pages 1-3) |


*Table: This table summarizes the core identifiers and defining characteristics of Leber congenital amaurosis 10, including its causal gene, hallmark variant, inheritance, prevalence, and onset. It is useful as a compact disease knowledge base entry scaffold grounded in the retrieved evidence.*

### Synonyms and Alternative Names
Common synonyms include: LCA10, CEP290-associated LCA, CEP290-related retinal degeneration, CEP290-associated inherited retinal degeneration, and Leber congenital amaurosis type 10 (leroy2021lebercongenitalamaurosis pages 1-2, pierce2024geneeditingfor pages 1-3). The disease information is derived from aggregated disease-level resources including cohort studies, clinical trials, review literature, and curated databases such as OMIM, OpenTargets, and ClinicalTrials.gov.

---

## 2. Etiology

### Disease Causal Factors
LCA10 is a monogenic Mendelian disorder caused exclusively by biallelic loss-of-function mutations in the *CEP290* gene located on chromosome 12q21.32 (huang2021leber’scongenitalamaurosis pages 6-7). There are no known environmental, infectious, or lifestyle contributions to disease causation.

### Genetic Risk Factors
The most common pathogenic variant is the deep intronic mutation **c.2991+1655A>G** (also referred to as the IVS26 variant or p.Cys998X), which is found in **60–89%** of CEP290-related LCA patients depending on the cohort and ancestry (leroy2021lebercongenitalamaurosis pages 1-2, gong2024infantilenystagmussyndrome—associated pages 4-5, coppieters2010geneticscreeningof pages 13-14). This variant creates a cryptic splice donor site within intron 26, generating an aberrant exon containing a premature stop codon. This results in approximately 50% of CEP290 transcripts containing the cryptic exon and producing truncated, nonfunctional protein, while the remaining ~50% are correctly spliced (leroy2021lebercongenitalamaurosis pages 1-2, mcdonald2024retinalciliopathiesand pages 7-8). The reduced CEP290 protein level (~10% correctly spliced mRNA with residual full-length protein) is sufficient for ciliary function in most organs but is inadequate for the highly specialized photoreceptor cilium, explaining the retinal-specific phenotype (mcdonald2024retinalciliopathiesand pages 7-8).

Other pathogenic CEP290 variants include **c.4723A>T** (4–11% frequency), as well as numerous additional missense, nonsense, frameshift, and splice-site mutations at lower frequencies (leroy2021lebercongenitalamaurosis pages 1-2). CEP290 mutations are classified as pathogenic per ACMG/AMP guidelines and are germline in origin. The functional consequence is loss of function.

### Modifier Genes
**AHI1** (Abelson Helper Integration Site 1) has been identified as a potential modifier gene for CEP290-related phenotypes. In a Belgian cohort, two novel heterozygous AHI1 missense variants (p.Asn811Lys and p.His758Pro) were found in CEP290-LCA patients with neurological involvement (coppieters2010geneticscreeningof pages 4-7, coppieters2010geneticscreeningof pages 16-17). AHI1 plays a functional role in ciliogenesis and vesicle trafficking by mediating Rab8a localization, and AHI1 variants may modulate neurological severity in CEP290-related disease (coppieters2010geneticscreeningof pages 16-17).

### Founder Effects
The c.2991+1655A>G variant represents a European founder mutation, with particularly high prevalence in Northern European populations. In a Belgian cohort, CEP290 accounted for 30% of all LCA mutations, with c.2991+1655A>G found in 89% of CEP290-related LCA patients (coppieters2010geneticscreeningof pages 13-14). In a German cohort, CEP290 accounted for 21% of all LCA-associated gene variants and 29% among LCA patients specifically (zobor2023geneticandclinical pages 1-2). CEP290 mutations are notably less prevalent in Chinese and Japanese populations (huang2021leber’scongenitalamaurosis pages 6-7).

### Gene-Environment Interactions
No gene-environment interactions have been established for LCA10. As a purely genetic ciliopathy, the disease course is determined by the nature and severity of the CEP290 mutations.

---

## 3. Phenotypes

LCA10 presents as a severe cone-rod dystrophy with the following characteristic phenotypic features:

| Phenotype | HPO Term | Frequency | Onset | Severity | Progression |
|---|---|---|---|---|---|
| Severe visual impairment/blindness | HP:0000505 | 62–89% | Congenital / early infancy | Severe | Progressive (leroy2021lebercongenitalamaurosis pages 2-4, huang2021leber’scongenitalamaurosis pages 6-7) |
| Nystagmus | HP:0000639 | Very frequent | Infantile | Moderate–severe | May stabilize (leroy2021lebercongenitalamaurosis pages 2-4, coppieters2010geneticscreeningof pages 13-14) |
| Photophobia | HP:0000613 | Frequent | Childhood | Moderate–severe | Stable (leroy2021lebercongenitalamaurosis pages 2-4) |
| High hyperopia | HP:0000540 | Frequent | Congenital / early childhood | Variable | Variable / often stable early (leroy2021lebercongenitalamaurosis pages 2-4) |
| Absent or severely reduced electroretinogram | HP:0000512 | Near-universal | Congenital / early childhood | Severe | Typically persistent (leroy2021lebercongenitalamaurosis pages 2-4, zobor2023geneticandclinical pages 1-2) |
| Oculodigital sign / eye poking | HP:0200026 | Frequent | Childhood | Variable | Variable (leroy2021lebercongenitalamaurosis pages 2-4, coppieters2010geneticscreeningof pages 13-14) |
| Sluggish pupillary reflex | HP:0000654 | Frequent | Congenital | Moderate | Stable (leroy2021lebercongenitalamaurosis pages 2-4) |
| Marbleized / salt-and-pepper fundus | HP:0007722 | Frequent | 1st–2nd decade | Variable | Progressive (leroy2021lebercongenitalamaurosis pages 2-4, coppieters2010geneticscreeningof pages 13-14) |
| Macular cyst-like lesions | HP:0040049 | Frequent | Childhood to adulthood | Variable | Progressive / may fluctuate with degeneration (gong2024infantilenystagmussyndrome—associated pages 4-5) |
| Photoreceptor degeneration | HP:0000510 | Universal | Postnatal | Severe | Progressive (leroy2021lebercongenitalamaurosis pages 1-2, moye2025subciliarylocalizationof pages 1-3, corralserrano2023eupatilinimprovescilia pages 3-6) |
| Cone-rod dystrophy pattern | HP:0000548 | Universal / characteristic | Congenital / early childhood | Severe | Progressive (leroy2021lebercongenitalamaurosis pages 2-4, coppieters2010geneticscreeningof pages 13-14) |


*Table: This table summarizes the core phenotypic features reported for CEP290-associated Leber congenital amaurosis 10, aligned to suggested HPO terms and annotated with typical frequency, onset, severity, and progression. It is useful for knowledge-base curation and phenotype harmonization.*

### Quality of Life Impact
LCA10 has a profound impact on quality of life and development. Most patients experience severe visual impairment from infancy, which significantly affects developmental milestones, educational attainment, independence, and overall well-being (leroy2021lebercongenitalamaurosis pages 1-2, leroy2021lebercongenitalamaurosis pages 5-6). The societal burden includes substantial direct medical costs and indirect costs from loss of productivity and need for supportive services (leroy2021lebercongenitalamaurosis pages 1-2).

---

## 4. Genetic/Molecular Information

### Causal Gene: CEP290
*CEP290* (centrosomal protein 290; OMIM 610142; HGNC:29021; Ensembl ENSG00000198707) is located on chromosome 12q21.32 and encodes a 290 kDa centrosomal protein that localizes to the transition zone of the photoreceptor connecting cilium (huang2021leber’scongenitalamaurosis pages 6-7, OpenTargets Search: Leber congenital amaurosis-CEP290).

### Pathogenic Variants
- **c.2991+1655A>G** (IVS26 variant): Deep intronic founder variant creating a cryptic exon with premature stop codon (p.Cys998X); found in 60–89% of CEP290-LCA patients; classified as pathogenic (leroy2021lebercongenitalamaurosis pages 1-2, coppieters2010geneticscreeningof pages 13-14, mcdonald2024retinalciliopathiesand pages 7-8)
- **c.4723A>T**: Second most common variant (4–11% frequency) (leroy2021lebercongenitalamaurosis pages 1-2)
- Over 150 additional pathogenic variants have been identified in CEP290 across the ciliopathy spectrum, including missense, nonsense, frameshift, and splice-site mutations
- All variants are germline in origin
- Functional consequence: Loss of function

### Allelic Heterogeneity and Pleiotropy
CEP290 mutations cause a spectrum of ciliopathies beyond LCA10, including Joubert syndrome, Senior-Løken syndrome, Meckel-Gruber syndrome, and Bardet-Biedl syndrome (gong2024infantilenystagmussyndrome—associated pages 4-5, huang2021leber’scongenitalamaurosis pages 6-7). The isolated retinal phenotype in LCA10 is attributed to the hypomorphic nature of the common c.2991+1655A>G variant, which permits residual CEP290 function in most organs (gong2024infantilenystagmussyndrome—associated pages 4-5, mcdonald2024retinalciliopathiesand pages 7-8).

### Chromosomal Abnormalities
No large-scale chromosomal abnormalities are associated with LCA10. The disease is caused by point mutations or small insertions/deletions within the CEP290 gene.

---

## 5. Environmental Information

As a monogenic Mendelian ciliopathy, LCA10 has no established environmental, lifestyle, or infectious contributory factors. There are no known environmental protective or risk factors. Environmental exposures, toxins, radiation, diet, and infectious agents do not play a role in disease etiology.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways and Cellular Processes
CEP290 is a structural protein of the ciliary transition zone—the gatekeeping compartment between the inner and outer segments of photoreceptors. Using advanced microscopy, CEP290 has been localized throughout the connecting cilium between doublet microtubules and the ciliary membrane with nine-fold symmetry (moye2025subciliarylocalizationof pages 11-12, moye2025subciliarylocalizationof pages 1-3).

The pathophysiological cascade in LCA10 proceeds as follows:

1. **Initial trigger**: Biallelic CEP290 mutations reduce or eliminate functional CEP290 protein at the photoreceptor connecting cilium (mcdonald2024retinalciliopathiesand pages 7-8, corralserrano2023eupatilinimprovescilia pages 3-6).

2. **Ciliary structural defects**: Loss of CEP290 results in aberrant connecting cilium membrane structure, confinement of the ciliary necklace and Y-links to the proximal connecting cilium, and stunted axonemes with abnormal ciliary vesicles (moye2025subciliarylocalizationof pages 11-12, moye2025subciliarylocalizationof pages 1-3).

3. **Transition zone protein redistribution**: Transition zone proteins AHI1 and NPHP1 are abnormally restricted to the proximal connecting cilium, while other proteins (NPHP8, CEP89) remain unaffected, indicating CEP290 has selective roles in TZ protein spatial distribution (moye2025subciliarylocalizationof pages 1-3).

4. **Impaired protein trafficking**: CEP290 dysfunction disrupts the ciliary gateway, leading to accumulation of rhodopsin and opsins in the outer nuclear layer instead of proper transport to the outer segment (corralserrano2023eupatilinimprovescilia pages 3-6).

5. **Outer segment formation failure**: Outer segment disc formation is inhibited, accompanied by accumulation of extracellular vesicles (moye2025subciliarylocalizationof pages 11-12, moye2025subciliarylocalizationof pages 1-3).

6. **Photoreceptor degeneration**: The combined effects of structural ciliary abnormalities, impaired protein trafficking, and failed outer segment formation result in progressive photoreceptor loss and retinal degeneration (moye2025subciliarylocalizationof pages 11-12, moye2025subciliarylocalizationof pages 1-3, corralserrano2023eupatilinimprovescilia pages 3-6).

### Suggested GO Terms
- GO:0060271 (cilium assembly)
- GO:0032391 (photoreceptor connecting cilium)
- GO:0001750 (photoreceptor outer segment)
- GO:0042462 (eye photoreceptor cell development)
- GO:0046548 (retinal rod cell development)

### Cell Types Involved
- Photoreceptor cells (CL:0000210) — primary cells affected
- Rod photoreceptors (CL:0000604) — develop but rapidly degenerate postnatally
- Cone photoreceptors (CL:0000573) — central cones lost early
- Retinal pigment epithelium cells (CL:0002586) — secondary involvement

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ**: Eye (UBERON:0000970)
- **Specific structure**: Retina (UBERON:0000966), particularly the photoreceptor layer
- **Body system**: Visual/nervous system

### Tissue and Cell Level
- Photoreceptor layer (UBERON:0001787)
- Outer nuclear layer (UBERON:0001789)
- Photoreceptor outer segments (UBERON:0001817)
- Connecting cilium/transition zone of photoreceptors

### Subcellular Level
- Primary cilium (GO:0005929)
- Transition zone (GO:0035869)
- Basal body/centriole (GO:0005814)
- Ciliary membrane (GO:0060170)
- Photoreceptor disc membrane (GO:0097449)

### Localization
- Bilateral, symmetric involvement
- Both eyes affected; foveal architecture may be relatively preserved despite disproportionate vision loss (leroy2021lebercongenitalamaurosis pages 2-4)

---

## 8. Temporal Development

### Onset
- **Typical age of onset**: Congenital to early infancy (leroy2021lebercongenitalamaurosis pages 1-2, leroy2021lebercongenitalamaurosis pages 2-4)
- **Onset pattern**: Insidious/congenital; visual impairment is usually recognized within the first months of life

### Progression
- **Disease course**: Progressive retinal degeneration
- Rod photoreceptors develop but rapidly degenerate postnatally; most patients lose rods by their second decade (leroy2021lebercongenitalamaurosis pages 2-4)
- The retina may initially appear normal, with white flecks or marbleized fundus appearing in the first to second decade, followed by pigmentary retinopathy (leroy2021lebercongenitalamaurosis pages 2-4, coppieters2010geneticscreeningof pages 13-14)
- Severe vision loss (counting fingers or worse) occurs in 62–89% of patients (leroy2021lebercongenitalamaurosis pages 2-4, huang2021leber’scongenitalamaurosis pages 6-7)
- **Disease duration**: Chronic, lifelong
- **Critical periods**: Early childhood represents a window of opportunity for therapeutic intervention before irreversible photoreceptor loss

---

## 9. Inheritance and Population

### Inheritance Pattern
- **Autosomal recessive** (leroy2021lebercongenitalamaurosis pages 1-2, huang2021leber’scongenitalamaurosis pages 6-7)
- Complete penetrance for biallelic pathogenic variants
- Variable expressivity, particularly influenced by specific genotype and modifier genes (gong2024infantilenystagmussyndrome—associated pages 4-5, coppieters2010geneticscreeningof pages 4-7)

### Epidemiology
- **Overall LCA prevalence**: Approximately 1:30,000 to 1:80,000 newborns; ~1:50,000 in Europe and North America (leroy2021lebercongenitalamaurosis pages 1-2, zobor2023geneticandclinical pages 1-2)
- **LCA10 proportion**: CEP290 accounts for 15–30% of LCA cases, making it the most common genetic subtype in Caucasians (huang2021leber’scongenitalamaurosis pages 6-7, zobor2023geneticandclinical pages 1-2)
- **Estimated LCA cases in Germany**: ~2,000 (zobor2023geneticandclinical pages 1-2)
- LCA affects 20% of blind children and accounts for 5% of all inherited retinal diseases (zobor2023geneticandclinical pages 1-2)

### Population Demographics
- **Ethnic distribution**: Highest frequency in Northern European/Caucasian populations; the c.2991+1655A>G variant is a European founder mutation (leroy2021lebercongenitalamaurosis pages 1-2, huang2021leber’scongenitalamaurosis pages 6-7)
- Less prevalent in Chinese and Japanese populations (huang2021leber’scongenitalamaurosis pages 6-7)
- CEP290 was the most common LCA-associated gene in Belgian (30%), German (21–29%), and other European cohorts (coppieters2010geneticscreeningof pages 13-14, zobor2023geneticandclinical pages 1-2)
- Equal sex ratio; no sex predilection documented
- Consanguinity increases risk in populations where it is practiced (coppieters2010geneticscreeningof pages 13-14)

---

## 10. Diagnostics

### Clinical Tests
- **Electroretinography (ERG)**: Severely reduced or extinguished scotopic and photopic responses; often the first objective diagnostic test (leroy2021lebercongenitalamaurosis pages 2-4, zobor2023geneticandclinical pages 1-2)
- **Optical Coherence Tomography (OCT)**: Shows photoreceptor layer thinning with relatively preserved foveal architecture (leroy2021lebercongenitalamaurosis pages 2-4)
- **Fundus Autofluorescence (FAF)**: Abnormal autofluorescence patterns (leroy2021lebercongenitalamaurosis pages 2-4)
- **Full-Field Stimulus Testing (FST)**: Used to measure retinal sensitivity, particularly in clinical trials (pierce2024geneeditingfor pages 1-3)
- **Fundoscopy**: Initially normal; white flecks, salt-and-pepper or marbleized appearance, and pigmentary changes develop over time (leroy2021lebercongenitalamaurosis pages 2-4, coppieters2010geneticscreeningof pages 13-14)

### Genetic Testing
- **Recommended approach**: Targeted next-generation sequencing gene panels for inherited retinal diseases (344+ genes), followed by Sanger sequencing for confirmation; achieves diagnosis in ~84.7% of pediatric IRD cases (leroy2021lebercongenitalamaurosis pages 2-4)
- **Single gene testing**: Direct sequencing of CEP290, particularly for the common c.2991+1655A>G variant
- **Whole exome/genome sequencing**: Useful for cases not resolved by panel testing
- **Note**: The deep intronic c.2991+1655A>G variant may not be detected by standard exome sequencing; dedicated assays or intronic coverage are required

### Differential Diagnosis
- Other LCA subtypes (RPE65-LCA2, GUCY2D-LCA1, CRB1-LCA8, AIPL1-LCA4)
- Early-onset retinitis pigmentosa
- Congenital stationary night blindness
- Achromatopsia
- Other ciliopathies with retinal involvement (Joubert syndrome, Senior-Løken syndrome)

---

## 11. Outcome/Prognosis

### Disease Course and Morbidity
- Most patients experience severe visual impairment or legal blindness by the first decade of life (leroy2021lebercongenitalamaurosis pages 2-4, huang2021leber’scongenitalamaurosis pages 6-7)
- LCA10 is the most severe form of LCA, associated with profoundly impaired vision at an earlier age compared to other subtypes such as LCA2 (leroy2021lebercongenitalamaurosis pages 5-6)
- Life expectancy is typically normal when the disease presents in its isolated retinal form (LCA10 without syndromic features)
- Disease-specific mortality is not elevated for non-syndromic LCA10

### Complications
- Progressive photoreceptor degeneration leading to complete blindness
- Developmental delays due to severe early vision loss
- Potential for syndromic features (renal dysfunction, neurological involvement) in patients with certain CEP290 genotypes (coppieters2010geneticscreeningof pages 13-14)

### Prognostic Factors
- Specific genotype (homozygous c.2991+1655A>G vs. compound heterozygous variants)
- Baseline visual acuity was identified as the only predictor of treatment response in sepofarsen trials (russell2022intravitrealantisenseoligonucleotide pages 6-7)
- Residual photoreceptor count at time of intervention
- Age at treatment initiation

---

## 12. Treatment

### Current Approved Treatments
There are currently **no approved treatments specifically for LCA10** (leroy2021lebercongenitalamaurosis pages 5-6). The only FDA/EMA-approved gene therapy for any LCA subtype is voretigene neparvovec (Luxturna) for RPE65-associated LCA (LCA2).

### Experimental Treatments in Clinical Trials

The following table summarizes the clinical trial landscape for LCA10:

| NCT Number | Trial Name | Therapy | Type | Phase | Enrollment | Status | Sponsor |
|---|---|---|---|---|---:|---|---|
| NCT03872479 | BRILLIANCE | EDIT-101 | CRISPR gene editing | Phase 1/2 | 34 | Unknown / later reported as paused in secondary sources | Editas Medicine, Inc. (pierce2024geneeditingfor pages 1-3, ling2023therapeuticgeneediting pages 8-9, saripalli2026genetherapyand pages 2-4) |
| NCT03140969 | PQ-110-001 | Sepofarsen (QR-110) | Antisense oligonucleotide (ASO) | Phase 1b/2 | 12 | Completed | ProQR Therapeutics (russell2022intravitrealantisenseoligonucleotide pages 1-2, leroy2021lebercongenitalamaurosis pages 6-7) |
| NCT03913143 | ILLUMINATE | Sepofarsen (QR-110) | Antisense oligonucleotide (ASO) | Phase 2/3 | 36 | Active, not recruiting | ProQR Therapeutics (ling2023therapeuticgeneediting pages 8-9) |
| NCT03913130 | Extension study to PQ-110-001 | Sepofarsen | Antisense oligonucleotide (ASO) | Phase 1/2 | 9 | Terminated | Laboratoires Théa (leroy2021lebercongenitalamaurosis pages 6-7) |
| NCT04855045 | Pediatric sepofarsen study | Sepofarsen | Antisense oligonucleotide (ASO) | Phase 2/3 | 15 | Unknown | ProQR Therapeutics (leroy2021lebercongenitalamaurosis pages 6-7) |
| NCT06891443 | HYPERION | Sepofarsen | Antisense oligonucleotide (ASO) | Phase 3 | 32 | Recruiting | Laboratoires Théa (leroy2021lebercongenitalamaurosis pages 6-7) |
| NCT03396042 | Natural History Study of CEP290-Related Retinal Degeneration | None (observational) | Natural history / observational | N/A | 26 | Completed | Editas Medicine, Inc. (leroy2021lebercongenitalamaurosis pages 6-7) |


*Table: This table summarizes the main registered clinical studies for CEP290-associated Leber congenital amaurosis 10, including interventional therapy trials and the natural history study that informed trial design. It is useful for comparing modalities, development stage, recruitment status, and sponsors across the current LCA10 treatment landscape.*

#### EDIT-101 (CRISPR-Cas9 Gene Editing)
EDIT-101 is a CRISPR-Cas9 gene editing therapy delivered via AAV5 subretinal injection, designed to excise or disable the aberrant cryptic exon created by the IVS26 variant in *CEP290*, thereby restoring normal splicing (pierce2024geneeditingfor pages 1-3). The **BRILLIANCE trial** (NCT03872479), a Phase 1–2 open-label study published in the *New England Journal of Medicine* (2024), enrolled 14 participants (12 adults aged 17–63 and 2 children aged 9 and 14). Key findings included:
- No serious treatment-related adverse events or dose-limiting toxicity (pierce2024geneeditingfor pages 1-3)
- 6 participants showed meaningful improvement in cone-mediated vision assessed by FST (pierce2024geneeditingfor pages 1-3)
- 9 participants (64%) showed meaningful improvement in BCVA, red light sensitivity, or mobility test scores (pierce2024geneeditingfor pages 1-3)
- 6 participants showed meaningful improvement in vision-related quality-of-life scores (pierce2024geneeditingfor pages 1-3)
- Suggested MAXO term: MAXO:0001001 (gene therapy)

#### Sepofarsen (QR-110; Antisense Oligonucleotide)
Sepofarsen is an RNA antisense oligonucleotide administered by intravitreal injection that targets the c.2991+1655A>G variant to restore normal CEP290 mRNA splicing (russell2022intravitrealantisenseoligonucleotide pages 1-2). In the Phase 1b/2 trial (NCT03140969) published in *Nature Medicine* (2022), 11 patients received multiple doses:
- 90.9% developed ocular adverse events in the treated eye, mostly mild and dose-dependent (russell2022intravitrealantisenseoligonucleotide pages 1-2)
- 8 of 11 patients developed cataracts, 6 requiring lens replacement (russell2022intravitrealantisenseoligonucleotide pages 1-2)
- Statistically significant improvements in visual acuity and retinal sensitivity were reported (russell2022intravitrealantisenseoligonucleotide pages 1-2, russell2022intravitrealantisenseoligonucleotide pages 6-7)
- 45% of patients gained at least 15 ETDRS letters (saripalli2026genetherapyand pages 2-4, russell2022intravitrealantisenseoligonucleotide pages 6-7)
- The Phase 2/3 **ILLUMINATE trial** (NCT03913143) ultimately failed to meet its primary endpoint of mean change in BCVA at 12 months (ling2023therapeuticgeneediting pages 8-9)
- A new **HYPERION Phase 3 trial** (NCT06891443) is currently recruiting with Laboratoires Théa as sponsor

#### Pharmacological Approaches
Preclinical studies have identified two mutation-agnostic small molecule approaches:
- **Eupatilin** (flavonoid): Improved cilium formation and length in CEP290 LCA10 patient-derived fibroblasts, CEP290 knockout RPE1 cells, and retinal organoids, and reduced rhodopsin retention in the outer nuclear layer (corralserrano2023eupatilinimprovescilia pages 3-6)
- **Taprenepag** (EP2 receptor agonist): EP2-mediated cAMP elevation enhanced ciliogenesis across all CEP290-mutant cell types and in Cep290-deficient mice, promoting photoreceptor outer segment development and partially restoring retinal responses

### Supportive Care
- Low-vision aids and assistive devices
- Orientation and mobility training
- Educational accommodations for visually impaired children
- Genetic counseling for family members
- Suggested MAXO term: MAXO:0000015 (supportive care)

---

## 13. Prevention

### Primary Prevention
- No primary prevention measures exist for LCA10 beyond genetic counseling and reproductive planning
- **Carrier screening**: Recommended for individuals with family history of LCA or known CEP290 carrier status
- **Preimplantation genetic testing (PGT)** and **prenatal testing** are available for families with known CEP290 variants
- Suggested MAXO term: MAXO:0000127 (genetic counseling)

### Secondary Prevention
- Early molecular diagnosis through NGS-based gene panels enables identification of affected individuals and potential enrollment in clinical trials before irreversible photoreceptor loss
- Newborn screening is not currently standard for LCA10

### Genetic Counseling
- For autosomal recessive inheritance, each offspring of two carrier parents has a 25% risk of being affected
- Carrier frequency for c.2991+1655A>G in Northern European populations is not precisely established but is expected to be relatively common given the high proportion of LCA10 among LCA cases

---

## 14. Other Species / Natural Disease

### Comparative Biology
CEP290 is highly conserved across vertebrate species. Mutations in orthologous genes cause retinal degeneration in multiple species:
- **Mouse** (*Mus musculus*, NCBI Taxon: 10090): The *rd16* mouse carries an in-frame deletion in Cep290 resulting in early-onset retinal degeneration with disrupted RPGR interaction (malglaive2023pharmacologicalcampstimulation pages 26-30). Cep290 knockout mice exhibit severe photoreceptor ciliary defects including aberrant connecting cilium membrane, stunted axonemes, and failure of outer segment formation (moye2025subciliarylocalizationof pages 11-12, moye2025subciliarylocalizationof pages 1-3).
- **Zebrafish** (*Danio rerio*, NCBI Taxon: 7955): Zebrafish cep290 mutants exhibit progressive cone photoreceptor degeneration with upregulation of inflammatory and stress-related pathways, but fail to stimulate regeneration despite Müller glia proliferation capacity
- **Human iPSC-derived retinal organoids**: Patient-derived organoids carrying homozygous c.2991+1655A>G show reduced ciliation, shortened cilia, absent CEP290 at the connecting cilium, and impaired outer segment development (mcdonald2024retinalciliopathiesand pages 7-8, corralserrano2023eupatilinimprovescilia pages 3-6)

### Limitations of Animal Models
A humanized mouse model carrying the c.2991+1655A>G intronic mutation failed to exhibit a retinal phenotype due to limited recognition of the cryptic splice site by the mouse spliceosome, necessitating development of fully human-derived model systems (mcdonald2024retinalciliopathiesand pages 7-8).

---

## 15. Model Organisms

### Mouse Models
- **rd16 mouse**: In-frame deletion in Cep290/Nphp6; exhibits early-onset retinal degeneration with disrupted RPGR interaction; recapitulates cone disease with natural disease progression (malglaive2023pharmacologicalcampstimulation pages 26-30)
- **Cep290 knockout mouse**: Complete loss of CEP290 results in ciliogenesis initiation but aberrant connecting cilium membrane, stunted axonemes, abnormal ciliary vesicles, failure of outer segment disc formation, and photoreceptor degeneration (moye2025subciliarylocalizationof pages 11-12, moye2025subciliarylocalizationof pages 1-3)
- **Nphp6 hypomorph mouse**: All-cone model generated to mimic human retinal ciliopathy (malglaive2023pharmacologicalcampstimulation pages 26-30)
- **Humanized c.2991+1655A>G knock-in mouse**: Failed to recapitulate retinal phenotype due to species-specific spliceosome differences (mcdonald2024retinalciliopathiesand pages 7-8)

### Zebrafish Models
- cep290−/− zebrafish exhibit progressive cone photoreceptor loss, microglia activation, inflammation, and upregulation of genes in apoptosis, stress response, and PDGF signaling pathways; rod precursor proliferation occurs but Müller glia-mediated regeneration is not triggered

### Human Cell Models
- Patient-derived iPSC retinal organoids are the gold standard for modeling CEP290-LCA10 pathology, recapitulating reduced ciliation, shortened cilia, absent CEP290 at the connecting cilium, impaired outer segment development, and protein trafficking defects (mcdonald2024retinalciliopathiesand pages 7-8, corralserrano2023eupatilinimprovescilia pages 3-6)

---

## Summary

Leber congenital amaurosis 10 is the most common genetic subtype of LCA, caused by biallelic loss-of-function mutations in *CEP290*, with the deep intronic founder variant c.2991+1655A>G being predominant in European populations (leroy2021lebercongenitalamaurosis pages 1-2, coppieters2010geneticscreeningof pages 13-14). The disease manifests as severe congenital/early-onset cone-rod dystrophy due to failure of photoreceptor ciliary transition zone function, leading to progressive photoreceptor degeneration (moye2025subciliarylocalizationof pages 11-12, moye2025subciliarylocalizationof pages 1-3, corralserrano2023eupatilinimprovescilia pages 3-6). While no approved treatments exist, both CRISPR-Cas9 gene editing (EDIT-101) and antisense oligonucleotide therapy (sepofarsen) have demonstrated promising safety profiles and efficacy signals in clinical trials (pierce2024geneeditingfor pages 1-3, russell2022intravitrealantisenseoligonucleotide pages 1-2, russell2022intravitrealantisenseoligonucleotide pages 6-7). The BRILLIANCE trial published in the *New England Journal of Medicine* (2024) demonstrated that in vivo CRISPR-Cas9 gene editing can safely improve photoreceptor function in LCA10 patients (pierce2024geneeditingfor pages 1-3), and a new Phase 3 trial of sepofarsen (HYPERION, NCT06891443) is currently recruiting. Novel mutation-agnostic pharmacological approaches targeting cAMP-mediated ciliogenesis pathways are also emerging in preclinical development, offering hope for broader therapeutic coverage across the CEP290 mutation spectrum (corralserrano2023eupatilinimprovescilia pages 3-6).

References

1. (leroy2021lebercongenitalamaurosis pages 1-2): Bart P. Leroy, David G. Birch, Jacque L. Duncan, Byron L. Lam, Robert K. Koenekoop, Fernanda B. O. Porto, Stephen R. Russell, and Aniz Girach. Leber congenital amaurosis due to cep290 mutations—severe vision impairment with a high unmet medical need. Retina, 41(5):898-907, Feb 2021. URL: https://doi.org/10.1097/iae.0000000000003133, doi:10.1097/iae.0000000000003133. This article has 70 citations.

2. (huang2021leber’scongenitalamaurosis pages 6-7): Chu-Hsuan Huang, Chung-May Yang, Chang-Hao Yang, Yu-Chih Hou, and Ta-Ching Chen. Leber’s congenital amaurosis: current concepts of genotype-phenotype correlations. Genes, 12:1261, Aug 2021. URL: https://doi.org/10.3390/genes12081261, doi:10.3390/genes12081261. This article has 114 citations.

3. (gong2024infantilenystagmussyndrome—associated pages 4-5): Xiaoming Gong and Richard W. Hertle. Infantile nystagmus syndrome—associated inherited retinal diseases: perspectives from gene therapy clinical trials. Life, 14:1356, Oct 2024. URL: https://doi.org/10.3390/life14111356, doi:10.3390/life14111356. This article has 2 citations.

4. (leroy2021lebercongenitalamaurosis pages 2-4): Bart P. Leroy, David G. Birch, Jacque L. Duncan, Byron L. Lam, Robert K. Koenekoop, Fernanda B. O. Porto, Stephen R. Russell, and Aniz Girach. Leber congenital amaurosis due to cep290 mutations—severe vision impairment with a high unmet medical need. Retina, 41(5):898-907, Feb 2021. URL: https://doi.org/10.1097/iae.0000000000003133, doi:10.1097/iae.0000000000003133. This article has 70 citations.

5. (zobor2023geneticandclinical pages 1-2): Ditta Zobor, Britta Brühwiler, Eberhart Zrenner, Nicole Weisschuh, and Susanne Kohl. Genetic and clinical profile of retinopathies due to disease-causing variants in leber congenital amaurosis (lca)-associated genes in a large german cohort. International Journal of Molecular Sciences, 24:8915, May 2023. URL: https://doi.org/10.3390/ijms24108915, doi:10.3390/ijms24108915. This article has 13 citations.

6. (OpenTargets Search: Leber congenital amaurosis-CEP290): Open Targets Query (Leber congenital amaurosis-CEP290, 8 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (russell2022intravitrealantisenseoligonucleotide pages 1-2): Stephen R. Russell, Arlene V. Drack, Artur V. Cideciyan, Samuel G. Jacobson, Bart P. Leroy, Caroline Van Cauwenbergh, Allen C. Ho, Alina V. Dumitrescu, Ian C. Han, Mitchell Martin, Wanda L. Pfeifer, Elliott H. Sohn, Jean Walshire, Alexandra V. Garafalo, Arun K. Krishnan, Christian A. Powers, Alexander Sumaroka, Alejandro J. Roman, Eva Vanhonsebrouck, Eltanara Jones, Fanny Nerinckx, Julie De Zaeytijd, Rob W. J. Collin, Carel Hoyng, Peter Adamson, Michael E. Cheetham, Michael R. Schwartz, Wilhelmina den Hollander, Friedrich Asmus, Gerard Platenburg, David Rodman, and Aniz Girach. Intravitreal antisense oligonucleotide sepofarsen in leber congenital amaurosis type 10: a phase 1b/2 trial. Nature Medicine, 28:1014-1021, Apr 2022. URL: https://doi.org/10.1038/s41591-022-01755-w, doi:10.1038/s41591-022-01755-w. This article has 155 citations and is from a highest quality peer-reviewed journal.

8. (pierce2024geneeditingfor pages 1-3): Eric A. Pierce, Tomas S. Aleman, Kanishka T. Jayasundera, Bright S. Ashimatey, Keunpyo Kim, Alia Rashid, Michael C. Jaskolka, Rene L. Myers, Byron L. Lam, Steven T. Bailey, Jason I. Comander, Andreas K. Lauer, Albert M. Maguire, and Mark E. Pennesi. Gene editing for <i>cep290</i> -associated retinal degeneration. New England Journal of Medicine, 390:1972-1984, Jun 2024. URL: https://doi.org/10.1056/nejmoa2309915, doi:10.1056/nejmoa2309915. This article has 234 citations and is from a highest quality peer-reviewed journal.

9. (mcdonald2024retinalciliopathiesand pages 7-8): Andrew McDonald and Jan Wijnholds. Retinal ciliopathies and potential gene therapies: a focus on human ipsc-derived organoid models. International Journal of Molecular Sciences, 25:2887, Mar 2024. URL: https://doi.org/10.3390/ijms25052887, doi:10.3390/ijms25052887. This article has 15 citations.

10. (coppieters2010geneticscreeningof pages 13-14): Frauke Coppieters, Ingele Casteels, Françoise Meire, Sarah De Jaegere, Sally Hooghe, Nicole van Regemorter, Hilde Van Esch, Aušra Matulevičienė, Luis Nunes, Valérie Meersschaut, Sophie Walraedt, Lieve Standaert, Paul Coucke, Heidi Hoeben, Hester Y. Kroes, Johan Vande Walle, Thomy de Ravel, Bart P. Leroy, and Elfride De Baere. Genetic screening of lca in belgium: predominance of cep290 and identification of potential modifier alleles in ahi1 of cep290-related phenotypes. Human Mutation, 31:E1709-E1766, Oct 2010. URL: https://doi.org/10.1002/humu.21336, doi:10.1002/humu.21336. This article has 185 citations and is from a domain leading peer-reviewed journal.

11. (coppieters2010geneticscreeningof pages 4-7): Frauke Coppieters, Ingele Casteels, Françoise Meire, Sarah De Jaegere, Sally Hooghe, Nicole van Regemorter, Hilde Van Esch, Aušra Matulevičienė, Luis Nunes, Valérie Meersschaut, Sophie Walraedt, Lieve Standaert, Paul Coucke, Heidi Hoeben, Hester Y. Kroes, Johan Vande Walle, Thomy de Ravel, Bart P. Leroy, and Elfride De Baere. Genetic screening of lca in belgium: predominance of cep290 and identification of potential modifier alleles in ahi1 of cep290-related phenotypes. Human Mutation, 31:E1709-E1766, Oct 2010. URL: https://doi.org/10.1002/humu.21336, doi:10.1002/humu.21336. This article has 185 citations and is from a domain leading peer-reviewed journal.

12. (coppieters2010geneticscreeningof pages 16-17): Frauke Coppieters, Ingele Casteels, Françoise Meire, Sarah De Jaegere, Sally Hooghe, Nicole van Regemorter, Hilde Van Esch, Aušra Matulevičienė, Luis Nunes, Valérie Meersschaut, Sophie Walraedt, Lieve Standaert, Paul Coucke, Heidi Hoeben, Hester Y. Kroes, Johan Vande Walle, Thomy de Ravel, Bart P. Leroy, and Elfride De Baere. Genetic screening of lca in belgium: predominance of cep290 and identification of potential modifier alleles in ahi1 of cep290-related phenotypes. Human Mutation, 31:E1709-E1766, Oct 2010. URL: https://doi.org/10.1002/humu.21336, doi:10.1002/humu.21336. This article has 185 citations and is from a domain leading peer-reviewed journal.

13. (moye2025subciliarylocalizationof pages 1-3): Abigail R. Moye, Michael A. Robichaux, Melina A. Agosto, Alexandre P. Moulin, Alexandra Graff-Meyer, Carlo Rivolta, and Theodore G. Wensel. Sub-ciliary localization of cep290 and effects of its loss in mouse photoreceptors during development. Journal of cell science, Jul 2025. URL: https://doi.org/10.1242/jcs.263869, doi:10.1242/jcs.263869. This article has 6 citations and is from a domain leading peer-reviewed journal.

14. (corralserrano2023eupatilinimprovescilia pages 3-6): JC Corral-Serrano, PE Sladen, D. Ottaviani, FO Rezek, K. Jovanović, D. Athanasiou, J. van der Spuy, BC Mansfield, and ME Cheetham. Eupatilin improves cilia defects in human cep290 ciliopathy models. bioRxiv, Apr 2023. URL: https://doi.org/10.1101/2023.04.12.536565, doi:10.1101/2023.04.12.536565. This article has 36 citations.

15. (leroy2021lebercongenitalamaurosis pages 5-6): Bart P. Leroy, David G. Birch, Jacque L. Duncan, Byron L. Lam, Robert K. Koenekoop, Fernanda B. O. Porto, Stephen R. Russell, and Aniz Girach. Leber congenital amaurosis due to cep290 mutations—severe vision impairment with a high unmet medical need. Retina, 41(5):898-907, Feb 2021. URL: https://doi.org/10.1097/iae.0000000000003133, doi:10.1097/iae.0000000000003133. This article has 70 citations.

16. (moye2025subciliarylocalizationof pages 11-12): Abigail R. Moye, Michael A. Robichaux, Melina A. Agosto, Alexandre P. Moulin, Alexandra Graff-Meyer, Carlo Rivolta, and Theodore G. Wensel. Sub-ciliary localization of cep290 and effects of its loss in mouse photoreceptors during development. Journal of cell science, Jul 2025. URL: https://doi.org/10.1242/jcs.263869, doi:10.1242/jcs.263869. This article has 6 citations and is from a domain leading peer-reviewed journal.

17. (russell2022intravitrealantisenseoligonucleotide pages 6-7): Stephen R. Russell, Arlene V. Drack, Artur V. Cideciyan, Samuel G. Jacobson, Bart P. Leroy, Caroline Van Cauwenbergh, Allen C. Ho, Alina V. Dumitrescu, Ian C. Han, Mitchell Martin, Wanda L. Pfeifer, Elliott H. Sohn, Jean Walshire, Alexandra V. Garafalo, Arun K. Krishnan, Christian A. Powers, Alexander Sumaroka, Alejandro J. Roman, Eva Vanhonsebrouck, Eltanara Jones, Fanny Nerinckx, Julie De Zaeytijd, Rob W. J. Collin, Carel Hoyng, Peter Adamson, Michael E. Cheetham, Michael R. Schwartz, Wilhelmina den Hollander, Friedrich Asmus, Gerard Platenburg, David Rodman, and Aniz Girach. Intravitreal antisense oligonucleotide sepofarsen in leber congenital amaurosis type 10: a phase 1b/2 trial. Nature Medicine, 28:1014-1021, Apr 2022. URL: https://doi.org/10.1038/s41591-022-01755-w, doi:10.1038/s41591-022-01755-w. This article has 155 citations and is from a highest quality peer-reviewed journal.

18. (ling2023therapeuticgeneediting pages 8-9): Jinjie Ling, Laura A. Jenny, Ashley Z Zhou, and Stephen H. Tsang. Therapeutic gene editing in inherited retinal disorders. Cold Spring Harbor perspectives in medicine, 13:a041292, Sep 2023. URL: https://doi.org/10.1101/cshperspect.a041292, doi:10.1101/cshperspect.a041292. This article has 4 citations and is from a peer-reviewed journal.

19. (saripalli2026genetherapyand pages 2-4): Karthik Saripalli. Gene therapy and leber congenital amaurosis: a review of treatments and clinical trials. American Journal of Student Research, pages 143-151, Jan 2026. URL: https://doi.org/10.70251/hyjr2348.41143151, doi:10.70251/hyjr2348.41143151. This article has 0 citations.

20. (leroy2021lebercongenitalamaurosis pages 6-7): Bart P. Leroy, David G. Birch, Jacque L. Duncan, Byron L. Lam, Robert K. Koenekoop, Fernanda B. O. Porto, Stephen R. Russell, and Aniz Girach. Leber congenital amaurosis due to cep290 mutations—severe vision impairment with a high unmet medical need. Retina, 41(5):898-907, Feb 2021. URL: https://doi.org/10.1097/iae.0000000000003133, doi:10.1097/iae.0000000000003133. This article has 70 citations.

21. (malglaive2023pharmacologicalcampstimulation pages 26-30): France de Malglaive, Iris Barny, Shahd Machroub, Lucas Fares-Taie, Ema Cano, Nicolas Goudin, Tania Attie-Bittach, Josseline Kaplan, Isabelle Perrault, Luis Briseno-Roa, Jean-Michel Rozet, and Jean-Philippe Annereau. Pharmacological camp stimulation via prostaglandin receptors rescues ciliary defects in cep290-deficient human and mouse models. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2023.10.06.561156, doi:10.1101/2023.10.06.561156. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](Leber_Congenital_Amaurosis_10-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Leber_Congenital_Amaurosis_10-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Leber_Congenital_Amaurosis_10-deep-research-falcon_artifacts/artifact-02.md)