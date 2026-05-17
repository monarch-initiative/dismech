---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-16T03:23:53.547033'
end_time: '2026-05-16T03:32:20.954002'
duration_seconds: 507.41
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CNS Vasculitis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
artifact_count: 4
artifact_sources:
  edison_answer_artifacts: 4
artifacts:
- filename: artifact-00.md
  path: CNS_Vasculitis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: CNS_Vasculitis-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: CNS_Vasculitis-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: artifact-03.md
  path: CNS_Vasculitis-deep-research-falcon_artifacts/artifact-03.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-03
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CNS Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **CNS Vasculitis** covering all of the
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
- **Disease Name:** CNS Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **CNS Vasculitis** covering all of the
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


## Comprehensive Disease Characteristics Research Report: CNS Vasculitis (Autoimmune Category)

### Scope note (terminology)
In the retrieved evidence, “CNS vasculitis” is used as an umbrella category covering **primary angiitis of the CNS** (PACNS; also called **primary CNS vasculitis**, PCNSV) and **secondary CNS vasculitis** (vasculitis driven by infection, connective tissue disease, systemic vasculitis, malignancy, etc.). Key modern guidance and most quantitative data in 2023–2024 focus on **PACNS/PCNSV** and imaging/biopsy-supported case series/cohorts. (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 2-3, sheikh2024primarycnsvasculitis pages 1-2)

---

## 1. Disease Information

### 1.1 What is the disease? (concise overview)
**Primary angiitis of the CNS (PACNS/PCNSV)** is a **rare inflammatory disorder of CNS blood vessels** that is restricted to the brain/spinal cord/meninges (i.e., no systemic vasculitis) and presents with heterogeneous neurologic syndromes such as headache, encephalopathy, stroke syndromes, and seizures. (pascarella2023europeanstrokeorganisation pages 1-2, sheikh2024primarycnsvasculitis pages 1-2, hoshina2024vasculitisinthe pages 1-2)

**Authoritative definition/clinical framing (ESO guideline, Oct 2023):** PACNS is treated as an *isolated CNS vasculitis* with very low-quality evidence across many diagnostic/treatment questions; histopathology is emphasized as the diagnostic reference standard and there is **no single specific neuroimaging pattern**. (pascarella2023europeanstrokeorganisation pages 1-2)

### 1.2 Key identifiers and codes
Only some coding/identifier systems were explicitly present in the retrieved sources:

- **ICD-9:** 437.4 (reported as used for case identification in a CNS vasculitis cohort). (hoshina2024vasculitisinthe pages 2-3)
- **ICD-10:** I67.7 “Cerebral arteritis, not elsewhere classified” (reported as used for case identification). (hoshina2024vasculitisinthe pages 2-3)

**Not found in retrieved evidence:** MONDO ID, MeSH ID, Orphanet ID, OMIM ID, ICD-11 code. (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 2-3)

### 1.3 Synonyms / alternative names
Common synonyms used in the recent literature include:
- **PACNS** = “Primary angiitis of the central nervous system” (ESO guideline terminology). (pascarella2023europeanstrokeorganisation pages 1-2)
- **PCNSV/PCNSV** = “Primary CNS vasculitis” (used interchangeably in 2024 clinical/imaging series). (sheikh2024primarycnsvasculitis pages 1-2, d’aniello2024thecontributionof pages 1-2)
- Subclassification terms (especially in guidelines): **LV-PACNS** (large/medium vessel predominant) and **SV-PACNS** (small-vessel predominant). (pascarella2023europeanstrokeorganisation pages 1-2)

### 1.4 Evidence source type (patient vs aggregated)
The retrieved evidence is primarily **aggregated disease-level resources** (ESO guideline) plus **retrospective single-center cohorts/series** and imaging-focused case series (human clinical). (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 2-3, d’aniello2024thecontributionof pages 1-2, agarwal2024theroleof pages 11-12)

#### Identifier/synonym summary table
| Concept | Identifier system | Identifier/code | Notes/source |
|---|---|---|---|
| Primary angiitis of the central nervous system | Preferred disease name in guideline/literature | PACNS | Used as the main term in the 2023 European Stroke Organisation guideline title and throughout the retrieved CNS vasculitis literature; primary form is defined as isolated CNS vasculitis without systemic disease (https://doi.org/10.1177/23969873231190431; Oct 2023) (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 1-2) |
| Primary CNS vasculitis | Synonym / literature term | PCNSV | Used synonymously with PACNS in 2024-2026 retrieved studies/reviews; D’Aniello 2024 and Sheikh 2024 use “primary CNS vasculitis/PCNSV” for the primary form (https://doi.org/10.3390/diagnostics14090927; Apr 2024; https://doi.org/10.3389/fneur.2024.1363985; Apr 2024) (sheikh2024primarycnsvasculitis pages 1-2, d’aniello2024thecontributionof pages 1-2) |
| CNS vasculitis | Broad disease term | CNSV | Broad umbrella term covering primary and secondary CNS vasculitis; Hoshina 2024 explicitly stratified cases into primary and secondary CNS vasculitis (https://doi.org/10.1177/19418744231223283; Dec 2024) (hoshina2024vasculitisinthe pages 2-3, hoshina2024vasculitisinthe pages 1-2) |
| Primary CNS vasculitis / primary angiitis of the CNS | Diagnostic category (Birnbaum & Hellmann framework cited in cohort) | Definite / Probable | Hoshina 2024 notes PACNS is “definite” with tissue confirmation and “probable” without biopsy if imaging/CSF are supportive; ESO 2023 emphasizes histopathology as gold standard (https://doi.org/10.1177/19418744231223283; Dec 2024; https://doi.org/10.1177/23969873231190431; Oct 2023) (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 1-2) |
| Large-vessel primary angiitis of the CNS | Guideline subclassification | LV-PACNS | ESO 2023 explicitly distinguishes LV-PACNS from SV-PACNS (https://doi.org/10.1177/23969873231190431; Oct 2023) (pascarella2023europeanstrokeorganisation pages 1-2) |
| Small-vessel primary angiitis of the CNS | Guideline subclassification | SV-PACNS | ESO 2023 explicitly distinguishes SV-PACNS from LV-PACNS (https://doi.org/10.1177/23969873231190431; Oct 2023) (pascarella2023europeanstrokeorganisation pages 1-2) |
| Secondary CNS vasculitis | Disease category / comparator | SCNSV / SACNS | Retrieved sources use both SCNSV and SACNS for vasculitis secondary to infection, connective tissue disease, malignancy, or systemic vasculitis (https://doi.org/10.3390/diagnostics14090927; Apr 2024; https://doi.org/10.3389/fneur.2025.1602427; Oct 2025) (scoppettuolo2025comparisonbetweenprimary pages 1-2, d’aniello2024thecontributionof pages 1-2) |
| Inflammatory cerebral amyloid angiopathy | Primary CNS vasculitis-related entity in cohort | inflammatory CAA | Hoshina 2024 describes inflammatory CAA, including ABRA, as a primary CNS vasculitis entity with distinct biopsy features (https://doi.org/10.1177/19418744231223283; Dec 2024) (hoshina2024vasculitisinthe pages 1-2) |
| Amyloid-beta related angiitis | Synonym / subtype label | ABRA | Included within inflammatory CAA/small-vessel predominant primary CNS vasculitis in retrieved cohort evidence (https://doi.org/10.1212/nxi.0000000000200397; Jul 2025; https://doi.org/10.1177/19418744231223283; Dec 2024) (hoshina2024vasculitisinthe pages 1-2) |
| CNS vasculitis | ICD-9 | 437.4 | Explicitly reported in Hoshina 2024 as an ICD code used for case identification (https://doi.org/10.1177/19418744231223283; Dec 2024) (hoshina2024vasculitisinthe pages 2-3) |
| Cerebral arteritis, not elsewhere classified | ICD-10 | I67.7 | Explicitly reported in Hoshina 2024 as an ICD-10 code used for CNS vasculitis case identification (https://doi.org/10.1177/19418744231223283; Dec 2024) (hoshina2024vasculitisinthe pages 2-3) |
| CNS vasculitis / PACNS | MeSH | not found in retrieved sources | No MeSH identifier was explicitly present in the provided evidence (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 1-2) |
| CNS vasculitis / PACNS | MONDO | not found in retrieved sources | No MONDO identifier was explicitly present in the provided evidence (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 1-2) |
| CNS vasculitis / PACNS | Orphanet | not found in retrieved sources | No Orphanet identifier was explicitly present in the provided evidence (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 1-2) |
| CNS vasculitis / PACNS | OMIM | not found in retrieved sources | No OMIM identifier was explicitly present in the provided evidence (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 1-2) |
| CNS vasculitis / PACNS | ICD-11 | not found in retrieved sources | No ICD-11 code was explicitly present in the provided evidence (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 1-2) |


*Table: This table compiles the disease names, abbreviations, coding systems, and terminology explicitly documented in the retrieved evidence for CNS vasculitis and PACNS/PCNSV. It is useful for normalizing nomenclature and identifying which ontology identifiers were or were not available from the current evidence set.*

---

## 2. Etiology

### 2.1 Disease causal factors
- **Primary CNS vasculitis (PACNS/PCNSV):** by definition, vasculitic inflammation restricted to CNS vessels without an identified systemic cause. (scoppettuolo2025comparisonbetweenprimary pages 1-2, hoshina2024vasculitisinthe pages 1-2)
- **Secondary CNS vasculitis (SCNSV/SACNS):** inflammation of CNS vessels **secondary to another condition**, including infection and connective tissue disease (CTD)-associated causes in 2024 cohort data. (hoshina2024vasculitisinthe pages 2-3, scoppettuolo2025comparisonbetweenprimary pages 1-2)

**Large single-center cohort etiology breakdown (University of Utah, 2011–2022; n=44):**
- Primary CNS vasculitis overall: **56.8%**
  - PACNS: **17/44 (38.6%)**
  - Inflammatory cerebral amyloid angiopathy (CAA; includes ABRA): **8/44 (18.2%)**
- Secondary CNS vasculitis: **43.2%**
  - Infectious: **10/44 (22.7%)**
  - CTD-associated: **6/44 (13.6%)**
  - Systemic vasculitis: **3/44 (6.8%)** (hoshina2024vasculitisinthe pages 1-2)

### 2.2 Risk factors
The retrieved sources emphasize **diagnostic differentiation** rather than enumerating prospective risk factors. However, secondary disease signals are reported:
- **Fever** occurred more often in secondary than primary CNS vasculitis (0% vs 26.3%; p=0.01), supporting infection/CTD suspicion when systemic features are present. (hoshina2024vasculitisinthe pages 2-3)

### 2.3 Protective factors / gene–environment interactions
Not identified in retrieved sources.

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (adult cohorts/series)
Across the recent adult cohort/series literature:
- In a 44-patient CNS vasculitis cohort, common presenting features were **headache (63.6%)**, **altered cognition (43.2%)**, and **focal weakness (38.6%)**. (hoshina2024vasculitisinthe pages 2-3)
- A 2024 PCNSV single-center series emphasizes heterogeneous presentations including **headache, seizures, cognitive impairment**, and delayed diagnosis (median symptom duration 36 weeks before diagnosis in that series). (sheikh2024primarycnsvasculitis pages 1-2)

### 3.2 Imaging-linked phenotypes (high-yield patterns in 2024 imaging studies)
- **Biopsy-proven PCNSV** (n=56): **SWI hemorrhages in 96.4% (54/56)** and **parenchymal enhancement in 96.3% (52/54)**, with dot-linear enhancement being the most prevalent enhancement pattern (87%). (agarwal2024theroleof pages 11-12)
- HR vessel-wall imaging cohort (n=14) included mostly stroke-like presentations (**78.7% stroke-like episodes**). (d’aniello2024thecontributionof pages 2-4)

### 3.3 Quality-of-life / disability signals
In the 2024 PCNSV series (n=5), most patients required walking aids initially and some required them at follow-up, illustrating persistent disability in a subset despite immunotherapy. (sheikh2024primarycnsvasculitis pages 1-2)

### 3.4 Suggested HPO terms
A phenotype-to-HPO mapping table (with frequencies where available from recent cohorts) is provided below.

| Phenotype (plain language) | Suggested HPO term (name; HP:ID if known) | Frequency/statistics | Notes/citations |
|---|---|---:|---|
| Headache | Headache; HP:0002315 | 63.6% in a 44-patient CNS vasculitis cohort; 76.9% in biopsy-confirmed small-vessel PCNSV; in a 5-patient PCNSV series, 1 presented with headache and all reported progressive holocephalic headaches | Common presenting symptom across primary/secondary CNS vasculitis and small-vessel PCNSV; also highlighted as a predictor in PACNS vs ICAD analyses (hoshina2024vasculitisinthe pages 2-3, sheikh2024primarycnsvasculitis pages 1-2, kharal2024predictivevalueof pages 1-2) |
| Altered cognition / encephalopathy / altered mental status | Encephalopathy; HP:0001298 | Altered cognition in 43.2% of 44-patient cohort; altered mental status in 61.5% of sv-PCNSV cohort; encephalopathy significantly associated with PACNS vs ICAD, OR 7.60 | Reflects diffuse CNS dysfunction and is repeatedly emphasized in PACNS presentations (hoshina2024vasculitisinthe pages 2-3, sheikh2024primarycnsvasculitis pages 1-2, kharal2024predictivevalueof pages 1-2) |
| Focal weakness / unilateral weakness | Hemiparesis; HP:0001269 | Focal weakness in 38.6% of 44-patient cohort; unilateral weakness in 2/5 patients in one 2024 series | Typical focal neurologic deficit in PACNS presentations (hoshina2024vasculitisinthe pages 2-3, sheikh2024primarycnsvasculitis pages 1-2) |
| Seizures | Seizure; HP:0001250 | 1/5 patients in Sheikh 2024; PACNS patients had seizures more often than secondary CNS vasculitis in 2025 cohort (40% vs 5%); seizure strongly associated with PACNS vs ICAD, OR 23.00 | Recurrent expert signal for PACNS, especially tumor-like and inflammatory presentations (sheikh2024primarycnsvasculitis pages 1-2, scoppettuolo2025comparisonbetweenprimary pages 1-2, kharal2024predictivevalueof pages 1-2) |
| Cognitive impairment | Cognitive impairment; HP:0100543 | Cognitive changes reported in all 5 patients in Sheikh 2024; cognitive or visual impairment in 2/5 on initial exam | Often accompanies headache/progressive symptoms and contributes to disability (sheikh2024primarycnsvasculitis pages 1-2) |
| Gait abnormality | Abnormality of gait; HP:0001288 | 1/5 in Sheikh 2024 presented with cognitive and gait abnormality | Suggests subcortical or multifocal lesion burden (sheikh2024primarycnsvasculitis pages 1-2) |
| Visual impairment | Visual impairment; HP:0000505 | 2/5 had cognitive or visual impairment on initial exam in Sheikh 2024 | May occur with focal deficits or posterior circulation/optic pathway involvement (sheikh2024primarycnsvasculitis pages 1-2) |
| Stroke-like episodes / acute ischemic events | Stroke; HP:0001297 | 78.7% (11/14) in D’Aniello 2024 imaging cohort presented with stroke-like episodes | CNS vasculitis frequently presents as ischemic cerebrovascular syndrome (d’aniello2024thecontributionof pages 2-4) |
| Transient ischemic attack-like episodes | Transient ischemic attack | 7.1% (1/14) in D’Aniello 2024 imaging cohort | Less common than stroke-like presentation in retrieved evidence (d’aniello2024thecontributionof pages 2-4) |
| Hemorrhagic lesions / intracranial hemorrhage / microhemorrhages | Intracranial hemorrhage; HP:0002170 | SWI hemorrhages in 96.4% (54/56) of biopsy-proven PCNSV; MRI in Sheikh 2024 showed hemorrhage among abnormalities | Hemorrhagic burden, especially microhemorrhages on SWI, is a notable imaging-associated phenotype in biopsy-proven disease (agarwal2024theroleof pages 11-12, sheikh2024primarycnsvasculitis pages 1-2) |
| White matter lesions | Abnormal cerebral white matter morphology | Most MRI lesions in biopsy-proven PCNSV were bilateral diffuse discrete-to-confluent white matter lesions | Frequent radiologic phenotype; frontal lobe predominance reported (agarwal2024theroleof pages 2-3, agarwal2024theroleof pages 11-12) |
| Vasogenic edema | Cerebral edema; HP:0002185 | Reported among MRI abnormalities in Sheikh 2024; edema present in 87% of tumor-like PACNS cases reviewed in 2025 systematic review | Important radiologic manifestation that can mimic tumor/inflammatory lesions (sheikh2024primarycnsvasculitis pages 1-2) |
| Restricted diffusion / acute ischemic injury | Abnormality of brain imaging | DWI abnormalities corresponded to vessel-wall enhancement in 77% of CNS vasculitis patients on VW-MRI study | Suggests active ischemic injury in territories of inflamed vessels (d’aniello2024thecontributionof pages 1-2) |
| Contrast-enhancing brain lesions | Abnormal CNS imaging with contrast enhancement | Parenchymal enhancement in 96.3% (52/54) of biopsy-proven PCNSV; dot-linear pattern 87%, nodular 61.1%, perivascular 25.9%, patchy 16.7% | Strongly supportive MRI pattern in biopsy-proven disease, though not disease-specific (agarwal2024theroleof pages 11-12) |
| Pseudotumoral / tumor-like mass lesions | Abnormality of CNS imaging | 45% of PACNS vs 10% of secondary CNS vasculitis in 2025 cohort; tumor-like PACNS recognized as a rare subtype in 2024 review | Important mimic of glioma/lymphoma; often requires biopsy for diagnosis (scoppettuolo2025comparisonbetweenprimary pages 1-2) |
| Spinal cord involvement | Abnormality of the spinal cord | 15.8% in non-ABRA sv-PCNSV; spinal MRI involvement in 38.3% (12/33) in biopsy-proven PCNSV imaging series | Indicates disease is not always confined to brain parenchyma alone (agarwal2024theroleof pages 11-12) |
| CSF pleocytosis | Cerebrospinal fluid pleocytosis; HP:0003565 | In PACNS vs ICAD, each +1 CSF WBC/µL increased odds of PACNS by 47% (OR 1.47, 95% CI 1.04–2.07); however, 17.4% of sv-PCNSV patients had normal CSF | CSF inflammation supports diagnosis but normal CSF does not exclude disease (kharal2024predictivevalueof pages 1-2, d’aniello2024thecontributionof pages 15-16) |
| Low CSF glucose | Decreased cerebrospinal fluid glucose concentration | More common in secondary CNS vasculitis: 41.2% vs 8.7% in primary disease | Helps suggest secondary, especially infectious, etiologies rather than PACNS (hoshina2024vasculitisinthe pages 2-3) |
| CSF oligoclonal bands | Oligoclonal bands in CSF | 63.6% in secondary CNS vasculitis vs 0 in primary disease in Hoshina 2024 | May help differentiate secondary CNS vasculitis from PACNS in the right context (hoshina2024vasculitisinthe pages 2-3) |
| Fever / systemic inflammatory symptoms | Fever; HP:0001945 | 26.3% in secondary CNS vasculitis vs 0% in primary CNS vasculitis | Systemic features are uncommon in PACNS and may point toward secondary causes (hoshina2024vasculitisinthe pages 2-3, sheikh2024primarycnsvasculitis pages 1-2) |
| Need for walking aid / ambulatory disability | Gait disturbance / impaired mobility | In Sheikh 2024, all but one patient required walking aids initially; after treatment, 2 still required ambulatory aids | Illustrates quality-of-life and disability burden from neurologic deficits (sheikh2024primarycnsvasculitis pages 1-2) |


*Table: This table summarizes reported clinical phenotypes and suggested HPO mappings for CNS vasculitis/PACNS, emphasizing frequencies and distinguishing features from recent cohorts and imaging studies. It is useful for knowledge-base phenotype annotation and for separating primary from secondary CNS vasculitis.*

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes / pathogenic variants
No PACNS/PCNSV causal genes or pathogenic variants were explicitly reported in the retrieved 2023–2024 core sources.

### 4.2 Molecular/histologic signatures (cellular composition)
In pediatric small-vessel CNS vasculitis biopsy material, immune infiltrates included **CD3, CD4, CD8, and CD20** cells as predominant components (T-cell and B-cell rich angiocentric inflammation). (d’aniello2024thecontributionof pages 2-4)

---

## 5. Environmental Information
Not systematically addressed in retrieved 2023–2024 sources; secondary/infectious etiologies are recognized as major environmental/exogenous contributors in “secondary CNS vasculitis” categories. (hoshina2024vasculitisinthe pages 2-3)

---

## 6. Mechanism / Pathophysiology

### 6.1 Current understanding (causal chain)
A consistent mechanistic model across guideline/cohort/imaging evidence is:
1. **Immune-mediated inflammation** targets CNS vessel walls (small, medium, and/or large vessels), often with **transmural involvement** (histopathology emphasized in the ESO guideline). (pascarella2023europeanstrokeorganisation pages 1-2)
2. Vessel wall inflammation leads to **luminal compromise**, endothelial activation, and thrombosis/occlusion, producing **ischemic injury**; small-vessel fragility and inflammation also contribute to **microhemorrhages** detectable on SWI. (sheikh2024primarycnsvasculitis pages 1-2, agarwal2024theroleof pages 11-12)
3. Parenchymal injury manifests as multifocal neurologic deficits (headache/encephalopathy/focal deficits/seizures) and MRI abnormalities (white-matter lesions, diffusion restriction, enhancement). (hoshina2024vasculitisinthe pages 2-3, sheikh2024primarycnsvasculitis pages 1-2, d’aniello2024thecontributionof pages 1-2)

### 6.2 Histopathologic patterns
In a recent CNS vasculitis cohort, histologic phenotypes included **lymphocytic, granulomatous, and necrotizing** patterns. (hoshina2024vasculitisinthe pages 2-3)

### 6.3 Pathophysiology-related imaging biomarkers (2024)
- **Vessel-wall MRI:** CNS vasculitis frequently shows **intense, concentric vessel-wall enhancement** (13/14 had enhancement; 84.6% intense; 92.3% concentric). (d’aniello2024thecontributionof pages 1-2)
- **DWI correlation:** DWI alterations corresponded with vessel-wall enhancement territories in **77%**, consistent with ischemic/hypoperfusion injury downstream of inflamed vessels. (d’aniello2024thecontributionof pages 1-2)
- **SWI microhemorrhages:** extremely common in biopsy-proven PCNSV (96.4%). (agarwal2024theroleof pages 11-12)

### 6.4 Suggested ontology terms (examples)
Because formal ontology IDs were not provided in the sources, the following are *suggested* (not evidence-derived IDs):
- **GO biological processes (suggested):** leukocyte migration; T cell activation; B cell activation; cytokine-mediated signaling; vasculature development/inflammation; endothelial cell activation.
- **CL cell types (suggested):** T cell; CD4-positive T cell; CD8-positive T cell; B cell; endothelial cell.

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary disease is confined to the **central nervous system**: vessels of the **brain**, **spinal cord**, and **meninges/leptomeninges**. (sheikh2024primarycnsvasculitis pages 1-2, d’aniello2024thecontributionof pages 2-4)

### 7.2 Localization patterns (imaging)
- Vessel-wall MRI cohort: enhancement affected the **anterior circulation in 69.2%** of patients and posterior circulation in 15.4%. (d’aniello2024thecontributionof pages 1-2)
- Biopsy-proven PCNSV imaging series: frontal lobe lesions predominated; inferior cerebellar lesions were also frequent; lesions often bilateral and diffuse within white matter. (agarwal2024theroleof pages 11-12)

---

## 8. Temporal Development

### 8.1 Onset and diagnostic delay
PACNS/PCNSV can have **subacute-to-chronic** evolution and diagnostic delay. In a 2024 PCNSV series, symptoms persisted a median **36 weeks** before diagnosis (range 3 weeks to 4 years). (sheikh2024primarycnsvasculitis pages 1-2)

### 8.2 Course patterns
Relapsing disease is recognized; in a biopsy-confirmed small-vessel PCNSV cohort, overall relapse rate was **19%** (2025 evidence, included here due to limited relapse statistics in 2023–2024 sources). (kharal2024predictivevalueof pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
Quantitative incidence was not systematically reported in the 2023 ESO guideline abstract, but a recent cohort-comparison paper cites an **estimated incidence of ~2.4 cases per million person-years** for PACNS (not a 2023–2024 primary epidemiology study; included as a commonly-cited estimate). (scoppettuolo2025comparisonbetweenprimary pages 1-2)

A 2024 single-center cohort provides internal proportions of primary vs secondary etiologies but is not population-based. (hoshina2024vasculitisinthe pages 2-3)

### 9.2 Demographics
- Utah cohort: median age 54; 25% male overall. (hoshina2024vasculitisinthe pages 2-3)
- PCNSV series (n=5): median onset age 31; 80% male (small series; likely not generalizable). (sheikh2024primarycnsvasculitis pages 1-2)

No genetic inheritance pattern is established for PACNS in the retrieved evidence.

---

## 10. Diagnostics

### 10.1 Diagnostic criteria / expert guidance
**ESO 2023 key expert statements (abstract-level):**
- Overall evidence quality is **very low** across many diagnostic/treatment questions.
- **CSF pleocytosis/hyperproteinorrachia** lack evidence as diagnostic tools.
- **Non-invasive vascular imaging** must be interpreted with caution (lack of validation vs DSA/histopathology).
- **No neuroimaging pattern is specific** for PACNS.
- **Multidisciplinary expert-center approach** is recommended. (pascarella2023europeanstrokeorganisation pages 1-2)

### 10.2 Imaging advances and diagnostic performance signals (2024)
Key 2024 developments emphasize **high-resolution vessel-wall MRI** and advanced MRI signatures:
- HR vessel-wall MRI frequently shows **intense, concentric enhancement**, supporting inflammatory vasculopathy evaluation. (d’aniello2024thecontributionof pages 1-2)
- In biopsy-proven PCNSV, **SWI microhemorrhages and dot-linear enhancement patterns** were proposed as minor diagnostic criteria in a large single-center series (56 biopsy-positive). (agarwal2024theroleof pages 11-12)
- Quantitative VWMRI metrics combined with clinical syndrome and CSF WBC can help discriminate PACNS from intracranial atherosclerotic disease: e.g., C/E ratio >1 (OR 115), concentricity ≥50% (OR 55), irregularity <50% (OR 55), seizure (OR 23), encephalopathy (OR 7.6). (kharal2024predictivevalueof pages 1-2)

### 10.3 Biopsy yield in real-world cohorts
- Utah cohort: biopsy confirmed vasculitis in **7/10** biopsied PACNS cases and **4/4** inflammatory CAA cases. (hoshina2024vasculitisinthe pages 2-3)
- Biopsy-proven PCNSV imaging series: 80 biopsies performed, 56 positive (**70%**). (agarwal2024theroleof pages 11-12)

#### Diagnostic modalities table
| Test/modality | What it assesses | Key findings (numbers/ORs/%) | Interpretation/role | Source (URL/date) |
|---|---|---|---|---|
| Cerebrospinal fluid (CSF) analysis | Pleocytosis, protein elevation, hypoglycorrhachia, oligoclonal bands | ESO guideline: hyperproteinorrachia and pleocytosis "do not have evidence supporting their use as diagnostic tools." In Utah cohort (n=44), secondary CNS vasculitis had more low CSF glucose (41.2% vs 8.7%, P=0.02) and unique OCBs (63.6% vs 0, P<0.01); normal CSF can occur. In Kharal 2024, each +1 CSF WBC/µL increased odds of PACNS vs ICAD by 47% (OR 1.47, 95% CI 1.04–2.07). (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 2-3, kharal2024predictivevalueof pages 1-2) | Supportive but nonspecific; useful for differential diagnosis and, with imaging/clinical context, may increase suspicion for PACNS, but cannot confirm or exclude it alone. | ESO guideline: https://doi.org/10.1177/23969873231190431 (Oct 2023); Hoshina et al.: https://doi.org/10.1177/19418744231223283 (Dec 2024); Kharal et al.: https://doi.org/10.1212/cpj.0000000000200321 (Aug 2024) |
| Conventional brain MRI | Parenchymal injury patterns: infarcts, hemorrhage, white-matter lesions, enhancement, edema | ESO guideline: no neuroimaging pattern is specific for PACNS. Utah cohort: MRI abnormal in all cases (100%). D’Aniello 2024: DWI abnormalities matched vessel-wall enhancement territories in 77%. Agarwal 2024 biopsy-proven PCNSV series (n=56): parenchymal enhancement in 96.3% (52/54). (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 2-3, d’aniello2024thecontributionof pages 1-2, agarwal2024theroleof pages 11-12) | Core first-line test to detect CNS injury and guide biopsy/imaging correlation, but findings are not pathognomonic. | ESO guideline: https://doi.org/10.1177/23969873231190431 (Oct 2023); Hoshina et al.: https://doi.org/10.1177/19418744231223283 (Dec 2024); D’Aniello et al.: https://doi.org/10.3390/diagnostics14090927 (Apr 2024); Agarwal et al.: https://doi.org/10.1038/s41598-024-55222-2 (Feb 2024) |
| Diffusion-weighted imaging (DWI) | Acute/subacute ischemic injury and lesion-territory correlation | D’Aniello 2024: DWI alterations corresponded to vessel-wall enhancement in 77% of patients. (d’aniello2024thecontributionof pages 1-2) | May reflect downstream ischemia/hypoperfusion or microembolization in territories of inflamed vessels; useful adjunct to vessel-wall imaging. | https://doi.org/10.3390/diagnostics14090927 (Apr 2024) |
| Digital subtraction angiography (DSA) / vascular imaging | Vessel caliber abnormalities, beading, stenosis/occlusion; medium/large-vessel disease | ESO guideline: non-invasive vascular imaging should be interpreted cautiously because of limited validation and different sensitivities vs DSA/histopathology. Utah cohort: vasculitic changes on vessel imaging in 33/44 (75%); 12 showed large–middle vessel and 21 middle–small vessel patterns. Agarwal 2024: venous-phase pseudophlebitic abnormalities/venulitis in 95%, but few arterial stenoses/occlusions in biopsy-proven small-vessel PCNSV. (pascarella2023europeanstrokeorganisation pages 1-2, hoshina2024vasculitisinthe pages 2-3, agarwal2024theroleof pages 11-12) | Helpful particularly for larger-vessel PACNS, but sensitivity is limited for small-vessel disease; a negative study does not exclude PACNS. | ESO guideline: https://doi.org/10.1177/23969873231190431 (Oct 2023); Hoshina et al.: https://doi.org/10.1177/19418744231223283 (Dec 2024); Agarwal et al.: https://doi.org/10.1038/s41598-024-55222-2 (Feb 2024) |
| High-resolution vessel-wall MRI (VW-MRI/VWI) | Arterial wall thickening and enhancement pattern (concentric vs eccentric; intense vs mild; vessel distribution) | D’Aniello 2024 (n=14): enhancement in 13/14; intense in 84.6%; concentric in 92.3%; anterior circulation in 69.2%, posterior 15.4%, both 15.4%; middle cerebral artery involved in 69.2%. Kharal 2024: C/E ratio >1 (OR 115.00), concentricity ≥50% (OR 55.00), irregularity <50% (OR 55.00) predicted PACNS vs ICAD. Authors note smooth, concentric, diffuse thickening/enhancement is typical, whereas eccentric/focal patterns suggest ICAD. (d’aniello2024thecontributionof pages 1-2, d’aniello2024thecontributionof pages 2-4, kharal2024predictivevalueof pages 1-2) | Promising adjunct for differentiating inflammatory vasculopathy from atherosclerotic disease and for mapping affected territories; still not fully validated as a stand-alone diagnostic test. | D’Aniello et al.: https://doi.org/10.3390/diagnostics14090927 (Apr 2024); Kharal et al.: https://doi.org/10.1212/cpj.0000000000200321 (Aug 2024) |
| Susceptibility-weighted imaging (SWI) / GRE | Microhemorrhages, macrohemorrhages, hemorrhagic burden | Agarwal 2024 biopsy-proven PCNSV series: SWI hemorrhages in 96.4% (54/56); SWI described as five times more sensitive than T2* for hemorrhage detection; microbleeds may persist despite steroid treatment. D’Aniello dataset also reported SWI microbleeds in some PCNSV patients. (agarwal2024theroleof pages 11-12, d’aniello2024thecontributionof pages 8-9) | Particularly valuable in small-vessel PCNSV where microhemorrhages are common; may be a useful minor diagnostic clue in the right clinical setting. | Agarwal et al.: https://doi.org/10.1038/s41598-024-55222-2 (Feb 2024); D’Aniello et al.: https://doi.org/10.3390/diagnostics14090927 (Apr 2024) |
| Contrast-enhanced T1-weighted MRI | Parenchymal, perivascular, leptomeningeal, pachymeningeal enhancement | Agarwal 2024: parenchymal enhancement in 96.3% (52/54); dot-linear pattern 87%, nodular 61.1%, perivascular 25.9%, patchy 16.7%; leptomeningeal enhancement 20.8%; pachymeningeal enhancement 7.6%. (agarwal2024theroleof pages 11-12) | High-yield adjunct in biopsy-proven PCNSV; dot-linear/perivascular enhancement patterns may raise suspicion for PCNSV, especially with hemorrhagic SWI findings. | https://doi.org/10.1038/s41598-024-55222-2 (Feb 2024) |
| Clinical + CSF + quantitative VWMRI model | Composite diagnostic discrimination between PACNS and intracranial atherosclerotic disease (ICAD) | Kharal 2024 (n=59): encephalopathy OR 7.60 (95% CI 1.07–54.09), seizure OR 23.00 (1.77–298.45), headache significant in sensitivity analysis; CSF WBC OR 1.47 per 1 cell/µL; VWMRI metrics had strongest associations (C/E ratio >1 OR 115.00; concentricity ≥50% OR 55.00; irregularity <50% OR 55.00). (kharal2024predictivevalueof pages 1-2) | Suggests PACNS diagnosis is strengthened by integrating syndrome features, inflammatory CSF, and vessel-wall geometry rather than relying on a single test. | https://doi.org/10.1212/cpj.0000000000200321 (Aug 2024) |
| Brain biopsy / histopathology | Direct confirmation of vasculitis and subtype/pattern (lymphocytic, granulomatous, necrotizing; exclusion of mimics) | ESO guideline and D’Aniello 2024: biopsy is the gold standard / required for definite PCNSV. D’Aniello notes biopsy can be nondiagnostic in up to 50% of cases. Hoshina 2024: PACNS biopsy positive in 7/10; inflammatory CAA 4/4. Agarwal 2024: 80 biopsies performed, 56/80 positive (70%) for PCNSV. (pascarella2023europeanstrokeorganisation pages 1-2, d’aniello2024thecontributionof pages 1-2, hoshina2024vasculitisinthe pages 2-3, agarwal2024theroleof pages 11-12) | Reference standard for definite diagnosis, especially crucial in small-vessel disease and tumor-like or mimic-rich presentations; false negatives remain an important limitation. | ESO guideline: https://doi.org/10.1177/23969873231190431 (Oct 2023); D’Aniello et al.: https://doi.org/10.3390/diagnostics14090927 (Apr 2024); Hoshina et al.: https://doi.org/10.1177/19418744231223283 (Dec 2024); Agarwal et al.: https://doi.org/10.1038/s41598-024-55222-2 (Feb 2024) |


*Table: This table summarizes the main 2023-2024 diagnostic tests used in CNS vasculitis/PACNS and the most relevant quantitative findings from recent guideline, cohort, and imaging studies. It is useful for comparing what each modality measures, how strongly it supports diagnosis, and where its limitations lie.*

---

## 11. Outcome / Prognosis

### 11.1 Mortality
In a 2011–2022 CNS vasculitis single-center cohort (n=44), overall mortality was **20.5%** (primary 16.0%, secondary 26.3%). (hoshina2024vasculitisinthe pages 2-3)

### 11.2 Functional outcomes
In the 2024 PCNSV series with median 56-month follow-up (n=5), outcomes varied: some improved, some remained stable, and one deteriorated; mobility aids remained necessary for some patients after treatment. (sheikh2024primarycnsvasculitis pages 1-2)

Robust long-term survival or disability statistics (5-year/10-year) were not available in the retrieved 2023–2024 evidence.

---

## 12. Treatment

### 12.1 Current standard practice (induction/maintenance)
Across guideline and contemporary clinical series, common treatment paradigms include:
- **Induction:** high-dose **corticosteroids**, often with **cyclophosphamide** for severe disease. (sheikh2024primarycnsvasculitis pages 1-2, rice2026primarycentralnervous pages 2-4)
- **Maintenance / steroid-sparing:** **azathioprine**, **methotrexate**, or **mycophenolate mofetil**; **rituximab** is used in some cohorts as maintenance or for refractory disease. (sheikh2024primarycnsvasculitis pages 1-2, hoshina2024vasculitisinthe pages 1-2, rice2026primarycentralnervous pages 2-4)

**ESO 2023 perspective:** treatment recommendations for induction and maintenance reflect substantial uncertainty because controlled trial evidence is sparse. (pascarella2023europeanstrokeorganisation pages 1-2)

### 12.2 Real-world implementation statistics
In the Utah cohort (n=44):
- IV methylprednisolone was predominant induction therapy (**63.6%**).
- Cyclophosphamide was the most used adjunctive therapy.
- Maintenance therapy included cyclophosphamide, rituximab, azathioprine, and mycophenolate (often with prednisone). (hoshina2024vasculitisinthe pages 2-3, hoshina2024vasculitisinthe pages 1-2)

### 12.3 Suggested MAXO terms (examples)
Suggested (not source-derived IDs): systemic glucocorticoid therapy; cyclophosphamide therapy; B-cell depletion therapy (rituximab); immunosuppressive maintenance therapy; plasma exchange; brain biopsy; MRI; cerebral angiography.

#### Treatment summary table
| Treatment/strategy | Phase (induction/maintenance) | Evidence type | Key quantitative outcome | Notes | Source |
|---|---|---|---|---|---|
| Intravenous methylprednisolone | Induction | Single-center retrospective CNS vasculitis cohort (n=44) | Used in 28/44 patients (63.6%); overall cohort mortality 9/44 (20.5%), primary 16.0%, secondary 26.3% | Predominant induction therapy across CNS vasculitis etiologies; outcome figures are cohort-level, not steroid-specific (hoshina2024vasculitisinthe pages 2-3, hoshina2024vasculitisinthe pages 1-2) | Hoshina 2024, Neurohospitalist, published Dec 2024, https://doi.org/10.1177/19418744231223283 (hoshina2024vasculitisinthe pages 2-3, hoshina2024vasculitisinthe pages 1-2) |
| High-dose corticosteroids ± cyclophosphamide | Induction | 2023 European guideline / expert consensus | No pooled effect size established; evidence judged very low quality | ESO guideline states induction recommendations reflect major uncertainty due to sparse evidence; management should be multidisciplinary in expert centers (pascarella2023europeanstrokeorganisation pages 1-2) | Pascarella et al. 2023, European Stroke Journal, Oct 2023, https://doi.org/10.1177/23969873231190431 (pascarella2023europeanstrokeorganisation pages 1-2) |
| Corticosteroids plus cyclophosphamide | Induction | Single-center retrospective PCNSV series (n=5) / narrative clinical update | No formal response rate reported; 2 improved, 2 stable, 1 deteriorated over median 56 months follow-up | Authors describe prompt immunotherapy, typically corticosteroids plus cyclophosphamide, as recommended induction; report states immunotherapy significantly improved clinical and radiologic outcomes, but not with drug-specific percentages (sheikh2024primarycnsvasculitis pages 1-2) | Sheikh et al. 2024, Frontiers in Neurology, Apr 2024, https://doi.org/10.3389/fneur.2024.1363985 (sheikh2024primarycnsvasculitis pages 1-2) |
| Cyclophosphamide as adjunct to steroids | Induction / adjunct | Single-center retrospective CNS vasculitis cohort (n=44) | Most used adjunctive therapy; subgroup use reported as 47.1%, 25%, and 66.7% in cohort summaries | Frequently paired with IV methylprednisolone in real-world practice; exact efficacy by subgroup not isolated in retrieved evidence (hoshina2024vasculitisinthe pages 2-3) | Hoshina 2024, https://doi.org/10.1177/19418744231223283 (hoshina2024vasculitisinthe pages 2-3) |
| Intravenous cyclophosphamide | Induction | Comparative retrospective cohort, PACNS vs secondary CNS vasculitis (20 vs 20) | Nearly half of PACNS patients received IV cyclophosphamide for induction; mortality/relapse/outcomes did not differ between PACNS and SACNS | PACNS showed more seizures and pseudotumoral lesions, but outcome separation by induction regimen was not demonstrated (scoppettuolo2025comparisonbetweenprimary pages 11-12, scoppettuolo2025comparisonbetweenprimary pages 1-2) | Scoppettuolo et al. 2025, Frontiers in Neurology, Oct 2025, https://doi.org/10.3389/fneur.2025.1602427 (scoppettuolo2025comparisonbetweenprimary pages 11-12, scoppettuolo2025comparisonbetweenprimary pages 1-2) |
| Cyclophosphamide within 3 months (“early intensive treatment”) | Early intensive induction | Retrospective biopsy-proven small-vessel PCNSV cohort (n=26; non-ABRA subgroup n=19) | Remission in 12/12 (100%) early-intensive group vs 11/14 (78.6%) escalation group; median time to remission 5 vs 19 months; HR 0.24, 95% CI 0.10–0.63, p<0.005; overall relapse 19% | Strongest quantitative treatment-outcome signal in retrieved evidence; supports earlier aggressive therapy in sv-PCNSV, though from 2025 source | Reddy et al. 2025, Neurology Neuroimmunology & Neuroinflammation, Jul 2025, https://doi.org/10.1212/NXI.0000000000200397 (kharal2024predictivevalueof pages 1-2) |
| Glucocorticoids alone or with azathioprine/mycophenolate/methotrexate (“escalation treatment”) | Initial non-intensive induction / early maintenance | Retrospective biopsy-proven small-vessel PCNSV cohort | Remission achieved in 11/14 (78.6%); slower median time to remission (19 months) than early cyclophosphamide group | Comparator arm in Reddy 2025; suggests less rapid disease control than early intensive cyclophosphamide (kharal2024predictivevalueof pages 1-2) | Reddy et al. 2025, https://doi.org/10.1212/NXI.0000000000200397 (kharal2024predictivevalueof pages 1-2) |
| Azathioprine | Maintenance | Cohort + review/expert opinion | Used as maintenance in real-world cohort; in PACNS/SACNS comparison, azathioprine was the commonest maintenance agent; no regimen-specific remission rate reported | Common steroid-sparing maintenance option after induction; often continued for at least 2 years in expert practice summaries (hoshina2024vasculitisinthe pages 1-2, scoppettuolo2025comparisonbetweenprimary pages 1-2) | Hoshina 2024, https://doi.org/10.1177/19418744231223283; Scoppettuolo 2025, https://doi.org/10.3389/fneur.2025.1602427 (hoshina2024vasculitisinthe pages 1-2, scoppettuolo2025comparisonbetweenprimary pages 1-2) |
| Mycophenolate mofetil | Maintenance | Cohort + review/expert opinion | Used in maintenance; no drug-specific response percentage reported in retrieved evidence | Listed among maintenance/steroid-sparing agents after induction in PCNSV/PACNS (sheikh2024primarycnsvasculitis pages 1-2, hoshina2024vasculitisinthe pages 1-2, rice2026primarycentralnervous pages 2-4, scoppettuolo2025comparisonbetweenprimary pages 1-2) | Sheikh 2024, https://doi.org/10.3389/fneur.2024.1363985; Hoshina 2024, https://doi.org/10.1177/19418744231223283; Rice 2026, https://doi.org/10.1007/s00415-026-13727-y (sheikh2024primarycnsvasculitis pages 1-2, hoshina2024vasculitisinthe pages 1-2, rice2026primarycentralnervous pages 2-4, scoppettuolo2025comparisonbetweenprimary pages 1-2) |
| Methotrexate | Maintenance | Review/expert opinion and clinical series | No quantitative outcome reported in retrieved evidence | Included among less toxic post-induction maintenance immunosuppressants (sheikh2024primarycnsvasculitis pages 1-2, rice2026primarycentralnervous pages 2-4, scoppettuolo2025comparisonbetweenprimary pages 1-2) | Sheikh 2024, https://doi.org/10.3389/fneur.2024.1363985; Rice 2026, https://doi.org/10.1007/s00415-026-13727-y; Scoppettuolo 2025, https://doi.org/10.3389/fneur.2025.1602427 (sheikh2024primarycnsvasculitis pages 1-2, rice2026primarycentralnervous pages 2-4, scoppettuolo2025comparisonbetweenprimary pages 1-2) |
| Rituximab | Maintenance / alternative immunomodulator | Real-world cohort + review/expert opinion | Used in maintenance cohorts; no PACNS-specific response rate quantified in retrieved evidence | Considered a steroid-sparing or refractory-disease option; case-report/series evidence exists, but robust comparative data lacking (hoshina2024vasculitisinthe pages 1-2, rice2026primarycentralnervous pages 2-4, scoppettuolo2025comparisonbetweenprimary pages 1-2) | Hoshina 2024, https://doi.org/10.1177/19418744231223283; Rice 2026, https://doi.org/10.1007/s00415-026-13727-y; Scoppettuolo 2025, https://doi.org/10.3389/fneur.2025.1602427 (hoshina2024vasculitisinthe pages 1-2, rice2026primarycentralnervous pages 2-4, scoppettuolo2025comparisonbetweenprimary pages 1-2) |
| Prednisone with maintenance immunosuppressants | Maintenance / taper | Retrospective cohort | Often used concurrently with cyclophosphamide, rituximab, azathioprine, or mycophenolate; no isolated efficacy estimate | Reflects common real-world tapering strategy after IV steroid induction (hoshina2024vasculitisinthe pages 1-2) | Hoshina 2024, https://doi.org/10.1177/19418744231223283 (hoshina2024vasculitisinthe pages 1-2) |
| Plasma exchange (PLEX) | Adjunct / rescue | Small cohort observation | 2 PACNS cases received PLEX with favorable outcomes | Evidence is anecdotal and insufficient for routine recommendation (hoshina2024vasculitisinthe pages 2-3) | Hoshina 2024, https://doi.org/10.1177/19418744231223283 (hoshina2024vasculitisinthe pages 2-3) |
| Maintenance immunosuppression after remission | Maintenance strategy | Review/expert opinion | No numeric estimate in retrieved excerpt; cited as improving long-term outcomes in prior literature referenced by review | Rice 2026 notes maintenance with azathioprine, methotrexate, or mycophenolate after induction, extrapolated largely from systemic vasculitis evidence (rice2026primarycentralnervous pages 2-4) | Rice & Scolding 2026, Journal of Neurology, Mar 2026, https://doi.org/10.1007/s00415-026-13727-y (rice2026primarycentralnervous pages 2-4) |


*Table: This table summarizes induction, maintenance, and adjunctive treatment strategies for CNS vasculitis/PACNS and the main quantitative outcomes available from the retrieved evidence. It is useful for distinguishing consensus-based practice from the few cohorts that report remission, relapse, and mortality statistics.*

---

## 13. Prevention
No primary prevention strategy is established for PACNS/PCNSV in the retrieved evidence; prevention is largely **secondary/tertiary**, focused on early recognition, exclusion of mimics/secondary causes, and relapse prevention with maintenance immunosuppression (expert practice). (pascarella2023europeanstrokeorganisation pages 1-2, rice2026primarycentralnervous pages 2-4)

---

## 14. Other Species / Natural Disease
No animal/natural disease information was identified in the retrieved sources.

---

## 15. Model Organisms
No model organism systems were described in the retrieved sources.

---

# Recent developments (2023–2024 highlights)

1. **First comprehensive European PACNS guideline using GRADE (Oct 2023):** emphasizes very low evidence quality, non-specific MRI patterns, and the need for expert-center multidisciplinary care and standardized neuroimaging/reporting. (pascarella2023europeanstrokeorganisation pages 1-2)
2. **Rapid growth in vessel-wall MRI evidence (Apr 2024):** intense, concentric enhancement frequently observed in CNS vasculitis, supporting VWI as an adjunct to conventional MRI/MRA/DSA. (d’aniello2024thecontributionof pages 1-2)
3. **Advanced MRI signatures in biopsy-proven PCNSV (Feb 2024):** near-universal SWI hemorrhages and high rates of contrast enhancement with characteristic patterns; proposal to incorporate SWI hemorrhage and dot-linear enhancement as minor diagnostic criteria. (agarwal2024theroleof pages 11-12)
4. **Quantitative VWMRI + CSF/clinical predictors (Aug 2024):** strong ORs for VWMRI geometry metrics and clinical syndromes distinguishing PACNS from intracranial atherosclerosis in a stroke/vasculopathy cohort. (kharal2024predictivevalueof pages 1-2)

---

# Clinical trials and translational pipeline (real-world implementations)

- **NCT03166319 (Mayo Clinic; completed; start 2017-07-24, completion 2020-11-24):** pilot interventional diagnostic study of intracranial HR vessel-wall MRI for suspected PACNS; enrollment 15; repeated MRI/MRA/VWI with gadolinium; imaging read by two neuroradiologists. URL: https://clinicaltrials.gov/study/NCT03166319 (NCT03166319 chunk 1)
- **NCT05168475 BIOVAS (Cambridge University Hospitals NHS Foundation Trust; Phase 2; terminated due to funding withdrawal):** randomized double-blind placebo-controlled modified-crossover trial planning sequential exposure to infliximab, rituximab, tocilizumab and placebo in refractory primary non-ANCA-associated vasculitis including PACNS; enrollment 22; primary endpoint treatment failure up to 720 days defined via BVAS/PVAS modifications. URL: https://clinicaltrials.gov/study/NCT05168475 (NCT05168475 chunk 1)
- **NCT00659776 (OHSU; Phase 2; terminated):** ferumoxytol MRI for CNS inflammation/vascular processes; enrollment 255; diagnostic imaging endpoints and histologic/EM correlation. URL: https://clinicaltrials.gov/study/NCT00659776 (NCT00659776 chunk 1)

---

# Evidence limitations and gaps (explicit)

- **Ontology identifiers (MONDO/MeSH/Orphanet/OMIM/ICD-11)** were not present in the retrieved evidence; they should be added by direct ontology lookup in dedicated resources (e.g., MONDO/Orphanet/MeSH browsers) rather than inferred. (hoshina2024vasculitisinthe pages 2-3)
- Many “classic” PACNS statements rely on older cohorts and expert consensus; the **ESO guideline explicitly characterizes the evidence base as very low quality** for many clinical questions, reinforcing that 2023–2024 advances are primarily in imaging characterization rather than randomized treatment trials. (pascarella2023europeanstrokeorganisation pages 1-2)
- **PMIDs were not provided in the retrieved full-text evidence snippets**; the report therefore cites DOI/URLs and journal metadata from the retrieved sources.

---

# Key cited sources (2023–2024 prioritized)

- Pascarella R, et al. **European Stroke Organisation (ESO) guidelines on PACNS**. *European Stroke Journal*. **Oct 2023**. https://doi.org/10.1177/23969873231190431 (pascarella2023europeanstrokeorganisation pages 1-2)
- D’Aniello S, et al. **Vessel wall MRI in primary/secondary CNS vasculitis**. *Diagnostics*. **Apr 2024**. https://doi.org/10.3390/diagnostics14090927 (d’aniello2024thecontributionof pages 1-2)
- Agarwal S, et al. **SWI and contrast MRI in biopsy-proven PCNSV (case series)**. *Scientific Reports*. **Feb 2024**. https://doi.org/10.1038/s41598-024-55222-2 (agarwal2024theroleof pages 11-12)
- Kharal MMGA, et al. **Clinical/CSF/VWMRI predictors of PACNS vs ICAD**. *Neurology Clinical Practice*. **Aug 2024**. https://doi.org/10.1212/cpj.0000000000200321 (kharal2024predictivevalueof pages 1-2)
- Hoshina Y, et al. **Etiology and outcomes in CNS vasculitis cohort (n=44)**. *The Neurohospitalist*. **Dec 2024**. https://doi.org/10.1177/19418744231223283 (hoshina2024vasculitisinthe pages 2-3)
- Sheikh TS, et al. **Clinical/neuropath/radiologic characteristics of PCNSV (series)**. *Frontiers in Neurology*. **Apr 2024**. https://doi.org/10.3389/fneur.2024.1363985 (sheikh2024primarycnsvasculitis pages 1-2)


References

1. (pascarella2023europeanstrokeorganisation pages 1-2): Rosario Pascarella, Katherina Antonenko, Grégoire Boulouis, Hubert De Boysson, Caterina Giannini, Mirjam R Heldner, Odysseas Kargiotis, Thanh N Nguyen, Claire M Rice, Carlo Salvarani, Antje Schmidt-Pogoda, Daniel Strbian, Salman Hussain, and Marialuisa Zedde. European stroke organisation (eso) guidelines on primary angiitis of the central nervous system (pacns). European Stroke Journal, 8:842-879, Oct 2023. URL: https://doi.org/10.1177/23969873231190431, doi:10.1177/23969873231190431. This article has 59 citations and is from a peer-reviewed journal.

2. (hoshina2024vasculitisinthe pages 2-3): Yoji Hoshina, Alen Delic, Ka-Ho Wong, Stephanie Lyden, Robert Kadish, Tammy L. Smith, Melissa A. Wright, Daisuke Shimura, and Stacey L. Clardy. Vasculitis in the central nervous system: etiology, characteristics, and outcomes in a large single-center cohort. The Neurohospitalist, 14:129-139, Dec 2024. URL: https://doi.org/10.1177/19418744231223283, doi:10.1177/19418744231223283. This article has 6 citations.

3. (sheikh2024primarycnsvasculitis pages 1-2): Tahani Saker Sheikh, Ayal Rozenberg, Goni Merhav, Alla Shifrin, Polina Stein, and Shahar Shelly. Primary cns vasculitis: insights into clinical, neuropathological, and neuroradiological characteristics. Frontiers in Neurology, Apr 2024. URL: https://doi.org/10.3389/fneur.2024.1363985, doi:10.3389/fneur.2024.1363985. This article has 6 citations and is from a peer-reviewed journal.

4. (hoshina2024vasculitisinthe pages 1-2): Yoji Hoshina, Alen Delic, Ka-Ho Wong, Stephanie Lyden, Robert Kadish, Tammy L. Smith, Melissa A. Wright, Daisuke Shimura, and Stacey L. Clardy. Vasculitis in the central nervous system: etiology, characteristics, and outcomes in a large single-center cohort. The Neurohospitalist, 14:129-139, Dec 2024. URL: https://doi.org/10.1177/19418744231223283, doi:10.1177/19418744231223283. This article has 6 citations.

5. (d’aniello2024thecontributionof pages 1-2): Serena D’Aniello, Arianna Rustici, Laura Ludovica Gramegna, Claudia Godi, Laura Piccolo, Mauro Gentile, Andrea Zini, Alessandro Carrozzi, Raffaele Lodi, Caterina Tonon, Massimo Dall’Olio, Luigi Simonetti, Raffaella Chieffo, Nicoletta Anzalone, and Luigi Cirillo. The contribution of vessel wall magnetic resonance imaging to the diagnosis of primary and secondary central nervous system vasculitis. Diagnostics, 14:927, Apr 2024. URL: https://doi.org/10.3390/diagnostics14090927, doi:10.3390/diagnostics14090927. This article has 12 citations.

6. (agarwal2024theroleof pages 11-12): Sushant Agarwal, Leve Joseph Devarajan Sebastian, Shailesh Gaikwad, M. V. Padma Srivastava, M. C. Sharma, Manmohan Singh, Rohit Bhatia, Ayush Agarwal, Jyoti Sharma, Deepa Dash, Vinay Goyal, Achal K. Srivastava, Manjari Tripathi, Vaishali Suri, Mamta B. Singh, Chitra Sarkar, Ashish Suri, Rajesh K. Singh, Deepti Vibha, Awadh K. Pandit, Roopa Rajan, Anu Gupta, A. Elavarasi, Divya M. Radhakrishnan, Animesh Das, Vivek Tandon, Ramesh Doddamani, Ashish Upadhyay, Venugopalan Y. Vishnu, and Ajay Garg. The role of susceptibility-weighted imaging & contrast-enhanced mri in the diagnosis of primary cns vasculitis: a large case series. Scientific Reports, Feb 2024. URL: https://doi.org/10.1038/s41598-024-55222-2, doi:10.1038/s41598-024-55222-2. This article has 13 citations and is from a peer-reviewed journal.

7. (scoppettuolo2025comparisonbetweenprimary pages 1-2): Pasquale Scoppettuolo, Lucie Pothen, Aline van Maanen, Valeria Onofrj, Selda Aydin, Olivier Gheysens, Renaud Lhommel, André Peeters, Vincent van Pesch, and Halil Yildiz. Comparison between primary and secondary central nervous system vasculitis in terms of clinical, biochemical, radiological, histopathological features, and outcomes: a single-center retrospective cohort study. Frontiers in Neurology, Oct 2025. URL: https://doi.org/10.3389/fneur.2025.1602427, doi:10.3389/fneur.2025.1602427. This article has 1 citations and is from a peer-reviewed journal.

8. (d’aniello2024thecontributionof pages 2-4): Serena D’Aniello, Arianna Rustici, Laura Ludovica Gramegna, Claudia Godi, Laura Piccolo, Mauro Gentile, Andrea Zini, Alessandro Carrozzi, Raffaele Lodi, Caterina Tonon, Massimo Dall’Olio, Luigi Simonetti, Raffaella Chieffo, Nicoletta Anzalone, and Luigi Cirillo. The contribution of vessel wall magnetic resonance imaging to the diagnosis of primary and secondary central nervous system vasculitis. Diagnostics, 14:927, Apr 2024. URL: https://doi.org/10.3390/diagnostics14090927, doi:10.3390/diagnostics14090927. This article has 12 citations.

9. (kharal2024predictivevalueof pages 1-2): M. M. G. Abbas Kharal, MD Sidonie E. Ibrikji, MD Youssef M. Farag, Aaron Shoskes PhD, P. DOMatthew, DO Richa Kiczek, MD Muhammad S Sheth, and MD Hussain. Predictive value of clinical, csf and vessel wall mri variables in diagnosing primary angiitis of the cns. Neurology Clinical Practice, Aug 2024. URL: https://doi.org/10.1212/cpj.0000000000200321, doi:10.1212/cpj.0000000000200321. This article has 5 citations.

10. (agarwal2024theroleof pages 2-3): Sushant Agarwal, Leve Joseph Devarajan Sebastian, Shailesh Gaikwad, M. V. Padma Srivastava, M. C. Sharma, Manmohan Singh, Rohit Bhatia, Ayush Agarwal, Jyoti Sharma, Deepa Dash, Vinay Goyal, Achal K. Srivastava, Manjari Tripathi, Vaishali Suri, Mamta B. Singh, Chitra Sarkar, Ashish Suri, Rajesh K. Singh, Deepti Vibha, Awadh K. Pandit, Roopa Rajan, Anu Gupta, A. Elavarasi, Divya M. Radhakrishnan, Animesh Das, Vivek Tandon, Ramesh Doddamani, Ashish Upadhyay, Venugopalan Y. Vishnu, and Ajay Garg. The role of susceptibility-weighted imaging & contrast-enhanced mri in the diagnosis of primary cns vasculitis: a large case series. Scientific Reports, Feb 2024. URL: https://doi.org/10.1038/s41598-024-55222-2, doi:10.1038/s41598-024-55222-2. This article has 13 citations and is from a peer-reviewed journal.

11. (d’aniello2024thecontributionof pages 15-16): Serena D’Aniello, Arianna Rustici, Laura Ludovica Gramegna, Claudia Godi, Laura Piccolo, Mauro Gentile, Andrea Zini, Alessandro Carrozzi, Raffaele Lodi, Caterina Tonon, Massimo Dall’Olio, Luigi Simonetti, Raffaella Chieffo, Nicoletta Anzalone, and Luigi Cirillo. The contribution of vessel wall magnetic resonance imaging to the diagnosis of primary and secondary central nervous system vasculitis. Diagnostics, 14:927, Apr 2024. URL: https://doi.org/10.3390/diagnostics14090927, doi:10.3390/diagnostics14090927. This article has 12 citations.

12. (d’aniello2024thecontributionof pages 8-9): Serena D’Aniello, Arianna Rustici, Laura Ludovica Gramegna, Claudia Godi, Laura Piccolo, Mauro Gentile, Andrea Zini, Alessandro Carrozzi, Raffaele Lodi, Caterina Tonon, Massimo Dall’Olio, Luigi Simonetti, Raffaella Chieffo, Nicoletta Anzalone, and Luigi Cirillo. The contribution of vessel wall magnetic resonance imaging to the diagnosis of primary and secondary central nervous system vasculitis. Diagnostics, 14:927, Apr 2024. URL: https://doi.org/10.3390/diagnostics14090927, doi:10.3390/diagnostics14090927. This article has 12 citations.

13. (rice2026primarycentralnervous pages 2-4): Claire Rice and Neil Scolding. Primary central nervous system vasculitis: an update. Journal of Neurology, Mar 2026. URL: https://doi.org/10.1007/s00415-026-13727-y, doi:10.1007/s00415-026-13727-y. This article has 0 citations and is from a domain leading peer-reviewed journal.

14. (scoppettuolo2025comparisonbetweenprimary pages 11-12): Pasquale Scoppettuolo, Lucie Pothen, Aline van Maanen, Valeria Onofrj, Selda Aydin, Olivier Gheysens, Renaud Lhommel, André Peeters, Vincent van Pesch, and Halil Yildiz. Comparison between primary and secondary central nervous system vasculitis in terms of clinical, biochemical, radiological, histopathological features, and outcomes: a single-center retrospective cohort study. Frontiers in Neurology, Oct 2025. URL: https://doi.org/10.3389/fneur.2025.1602427, doi:10.3389/fneur.2025.1602427. This article has 1 citations and is from a peer-reviewed journal.

15. (NCT03166319 chunk 1): Vance Lehman. Vessel Wall Imaging for Diagnosis and Monitoring of Central Nervous System (CNS) Vasculitis. Mayo Clinic. 2017. ClinicalTrials.gov Identifier: NCT03166319

16. (NCT05168475 chunk 1): David Jayne. Biologics in Refractory Vasculitis: A Trial of Biologic Therapy for Refractory Primary Non-ANCA Associated Vasculitis. Cambridge University Hospitals NHS Foundation Trust. 2021. ClinicalTrials.gov Identifier: NCT05168475

17. (NCT00659776 chunk 1): Edward Neuwelt. MR, Histologic And EM Imaging Of Intravenous Ferumoxytol In Central Nervous System (CNS) Inflammation. Oregon Health and Science University. 2004. ClinicalTrials.gov Identifier: NCT00659776

## Artifacts

- [Edison artifact artifact-00](CNS_Vasculitis-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](CNS_Vasculitis-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](CNS_Vasculitis-deep-research-falcon_artifacts/artifact-02.md)
- [Edison artifact artifact-03](CNS_Vasculitis-deep-research-falcon_artifacts/artifact-03.md)