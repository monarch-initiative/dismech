---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T06:13:55.731527'
end_time: '2026-08-20T06:23:27.973194'
duration_seconds: 572.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Paraneoplastic Pemphigus
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Paraneoplastic_Pemphigus-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Paraneoplastic Pemphigus
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Paraneoplastic Pemphigus** covering all of the
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
- **Disease Name:** Paraneoplastic Pemphigus
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Paraneoplastic Pemphigus** covering all of the
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


# Paraneoplastic Pemphigus (PNP/PAMS): Disease-Characteristics Research Report

## Executive summary

Paraneoplastic pemphigus (PNP), increasingly termed **paraneoplastic autoimmune multiorgan syndrome (PAMS)**, is an ultra-rare, frequently lethal autoimmune disease caused by neoplasia-associated humoral and cellular immunity against epithelial adhesion proteins. Its signature is severe, persistent panstomatitis with polymorphous skin disease; conjunctival, genital, gastrointestinal, and—most importantly—bronchopulmonary involvement may occur. The principal associated disorders are lymphoproliferative or hematologic neoplasms, especially non-Hodgkin lymphoma, chronic lymphocytic leukemia (CLL), and Castleman disease. The 2023 EADV S2k guideline describes it as a “rare autoimmune disease with mucocutaneous and multi-organ involvement” and emphasizes severe infection and bronchiolitis obliterans as major causes of death. [Published March 2023; DOI/URL: https://doi.org/10.1111/jdv.18931] (antiga2023s2kguidelineson pages 1-3)

Evidence remains dominated by retrospective cohorts, small laboratory series, and case reports. There are no validated universal diagnostic criteria, randomized PNP-specific treatment trials, established monogenic cause, or robust prevention strategy. The most authoritative current clinical source is the 2023 international EADV S2k consensus guideline; a November 2024 oral-PNP scoping review synthesized 87 publications through September 2024. (falco2024oralparaneoplasticpemphigus pages 2-4, antiga2023s2kguidelineson pages 16-19)

## 1. Disease information

### Definition and synonyms

PNP/PAMS is a **neoplasia-associated autoimmune blistering and interface dermatitis syndrome** affecting stratified epithelia and sometimes internal organs. “PNP” emphasizes pemphigus-like acantholysis and anti-keratinocyte antibodies; “PAMS” better captures frequent extracutaneous disease. The disease was defined as a distinct neoplasia-induced autoimmune mucocutaneous disorder by Anhalt et al. in 1990 (PMID: **2247105**). (antiga2023s2kguidelineson pages 16-19, antiga2023s2kguidelineson pages 21-23)

**Synonyms:** paraneoplastic pemphigus; paraneoplastic autoimmune multiorgan syndrome; PNP; PAMS; paraneoplastic autoimmune multiorgan syndrome, epithelial variant. “Paraneoplastic autoimmune multiorgan syndrome” is preferable when airway or other systemic disease is prominent. (antiga2023s2kguidelineson pages 16-19, antiga2023s2kguidelineson pages 21-23)

### Identifiers and coding

* **MONDO:** a dedicated PNP concept exists in MONDO, but the exact current numerical identifier was not independently verified in the retrieved primary literature; it should be resolved directly against the current MONDO release before database ingestion.
* **Orphanet:** dedicated rare-disease entry exists; exact ORPHA number should likewise be API-verified against the current Orphanet nomenclature.
* **MeSH:** *Paraneoplastic Pemphigus* is the preferred disease concept.
* **OMIM:** PNP is acquired rather than Mendelian; no causal OMIM phenotype/gene entry is clinically applicable.
* **ICD-10/ICD-11:** no consistently used PNP-specific billable code was established in the evidence. Cases are generally mapped under pemphigus/other specified pemphigus plus the associated neoplasm and organ complications. Local coding rules should be checked rather than assigning an unverified specific code.

This report primarily uses **aggregated disease-level resources**—guidelines, reviews, and published cohorts—not individual EHR records. Numerical frequencies arise from identifiable retrospective cohorts or laboratory series and should not be interpreted as population-registry estimates.

## 2. Etiology and risk/protective factors

### Causal framework

The necessary clinical context is usually an underlying neoplasm, which promotes loss of immune tolerance and generates autoreactive B- and T-cell responses against epithelial adhesion complexes. Hematologic/lymphoproliferative disease is most characteristic; solid tumors account for approximately **14.8–17%** of cases in retrospective series. Castleman disease has represented up to **56%** in selected, particularly Asian, cohorts and is the leading association in children and adolescents. (antiga2023s2kguidelineson pages 3-5)

A 2024 review reported non-Hodgkin lymphoma in **38.6%**, CLL in **18.4%**, and Castleman disease in **18.4%** of its summarized cases; these proportions differ from Asian and pediatric cohorts because referral geography and case selection strongly influence estimates. About **30%** present with PNP before discovery of the occult neoplasm. (falco2024oralparaneoplasticpemphigus pages 1-2)

### Genetic factors

PNP is **not a monogenic inherited disorder**. There are no established pathogenic germline variants, Mendelian inheritance pattern, penetrance estimate, carrier frequency, founder mutation, anticipation, or indication for WES/WGS as a PNP diagnostic test. Limited reports have proposed HLA susceptibility signals—such as HLA-DRB1 and HLA-C associations—but these are susceptibility observations rather than causal variants and are not validated for screening or treatment selection. Accordingly, ClinVar-style pathogenic-variant classification and population allele frequency are not applicable to PNP itself.

A 2024 tumor-genomic study reported **IL6ST variants as a prognostic biomarker in PNP-associated unicentric Castleman disease**, but this concerns the associated tumor’s genomic profile rather than a germline cause of PNP (J Invest Dermatol. 2024;144:585–592.e1; DOI: https://doi.org/10.1016/j.jid.2023.07.031). This finding is promising but not yet a standard clinical biomarker.

### Environmental, treatment, infectious, and lifestyle factors

No reproducible associations with smoking, alcohol, diet, occupation, pollution, toxins, or exercise have been established. Rare case reports implicate **fludarabine, bendamustine, cyclophosphamide, or radiotherapy** as triggers or exacerbators in patients with relevant neoplasia; causality remains weak because these therapies coexist with the underlying tumor and immune dysregulation. (antiga2023s2kguidelineson pages 3-5)

No bacterial, viral, fungal, or parasitic agent is established as the cause. Infection is primarily a **complication** of barrier failure and immunosuppression, not the initiating etiology. No genetic, dietary, lifestyle, or exposure-related protective factor has been demonstrated, and meaningful gene–environment interaction data are absent.

## 3. Phenotypes

* **Severe erosive oral mucositis/panstomatitis:** nearly universal, usually early, chronic, painful, hemorrhagic, treatment-resistant, and often involving lips, tongue, cheeks, gingiva, palate, pharynx, larynx, or esophagus. Odynophagia and dysphagia can cause major malnutrition requiring enteral feeding. Suggested HPO: stomatitis, oral ulceration, hemorrhagic oral mucosa, dysphagia, odynophagia, feeding difficulty. (antiga2023s2kguidelineson pages 5-7)
* **Polymorphous skin disease:** about **two-thirds** of a 104-patient cohort had skin lesions in addition to mucosal disease. Patterns include pemphigus-like flaccid blistering, pemphigoid-like tense blisters, lichenoid dermatitis, erythema-multiforme-like target lesions, and GVHD/SJS/TEN-like epidermal loss. Palmoplantar lichenoid lesions and relative scalp sparing can be diagnostic clues. Suggested HPO: skin blistering, skin erosion, lichenoid dermatitis, target lesions, erythroderma, nail dystrophy/anonychia. (antiga2023s2kguidelineson pages 3-5)
* **Ocular disease:** approximately **40%** in the 104-patient series; conjunctival hyperemia/erosion, pseudomembranes, symblepharon, forniceal shortening, corneal ulcers, pain, discharge, and reduced acuity may culminate in scarring visual impairment. Early ophthalmology assessment is recommended. (antiga2023s2kguidelineson pages 5-7)
* **Anogenital disease:** erosive or lichenoid genital lesions occurred in **35% (28/79)** in one cohort and **62%** of a 32-child Castleman-associated cohort. Suggested HPO: genital ulceration, mucosal erosion. (antiga2023s2kguidelineson pages 5-7)
* **Bronchopulmonary disease:** reported in **30–90%** across heterogeneous cohorts. Progressive dyspnea, fixed airflow obstruction, bronchiolitis obliterans, bronchiectasis, hypoxemia, and respiratory failure are the principal life-limiting manifestations. Bronchiolitis obliterans caused **40% of deaths among 40 fatal cases** in one retrospective series. Suggested HPO: dyspnea, obstructive lung disease, bronchiolitis obliterans, bronchiectasis, hypoxemia, respiratory failure. (antiga2023s2kguidelineson pages 5-7)
* **Gastrointestinal involvement:** esophageal or intestinal erosions may occur, sometimes without overt symptoms. Evidence consists largely of case reports and small pathology studies. (antiga2023s2kguidelineson pages 5-7)
* **Other autoimmune manifestations:** myasthenia gravis may accompany thymoma, Castleman disease, or other tumors; thyroid, kidney, and smooth-muscle findings are less securely attributable directly to PNP. (antiga2023s2kguidelineson pages 7-10)

Severity is highly variable but frequently severe and progressive. No PNP-specific EQ-5D, SF-36, or validated disease-specific quality-of-life dataset was identified. Nonetheless, pain, inability to eat, visual impairment, disfiguring erosions, hospitalization, respiratory disability, and treatment toxicity imply profound functional and psychosocial burden.

## 4. Genetic and molecular information

There are **no causal PNP genes or ACMG-classifiable PNP variants**. Instead, the molecular annotation should capture autoantigens:

* **EVPL/envoplakin, PPL/periplakin, DSP/desmoplakin I/II, PLEC/plectin, DST/BP230, EPPK1/epiplakin**—plakin/cytolinker proteins.
* **DSG3, DSG1 and DSC1–DSC3**—desmosomal cadherins.
* **A2ML1**—the p170 autoantigen/protease inhibitor.

Reported antibody frequencies are assay-dependent: envoplakin/periplakin up to **88%**, epiplakin **61%**, plectin **57%**, BP230 about one-third, DSG3 about **70%**, DSG1 about one-third, and desmocollins about **62%**. A2ML1 antibodies occur in a substantial subset. (antiga2023s2kguidelineson pages 7-10, antiga2023s2kguidelineson pages 10-12)

Landmark molecular primary studies identified A2ML1 (PMID: **20805888**), envoplakin (PMID: **9284106**), periplakin (PMIDs: **9699741**, **9699735**), and plectin (PMID: **9989789**). Anti-DSG3 antibodies from PNP sera caused acantholysis in neonatal mice (PMID: **9710446**), supporting direct pathogenicity for at least part of the antibody repertoire. (antiga2023s2kguidelineson pages 21-23)

No reproducible PNP-specific DNA methylation, chromosomal abnormality, histone signature, germline structural variant, metabolome, lipidome, single-cell atlas, spatial transcriptome, or multi-omics diagnostic signature has entered clinical use. Tumor-specific genomic or IL-6-pathway observations should not be conflated with an inherited PNP defect.

## 5. Environmental information

PNP is mechanistically linked to neoplasia rather than a conventional environmental exposure. Rare drug/radiotherapy-associated exacerbations are the only reported non-genetic triggers with disease-specific relevance. No causal pathogen, zoonotic transmission, nutritional cause, or validated lifestyle modifier is known. Secondary infection of erosions and opportunistic infection under corticosteroid, cytotoxic, or B-cell-depleting therapy are clinically important downstream exposures. (antiga2023s2kguidelineson pages 3-5, antiga2023s2kguidelineson pages 15-16)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream neoplasm:** a lymphoid/hematologic tumor or, less often, a solid tumor creates abnormal antigen presentation, cytokine signaling, autoreactive lymphocyte expansion, and/or epitope cross-reactivity.
2. **Loss of tolerance:** autoreactive B cells produce IgG against plakins, desmosomal cadherins, and A2ML1; autoreactive T cells, including activated CD8-positive T cells, attack epithelia.
3. **Adhesion failure and cell death:** anti-DSG/anti-desmosomal activity impairs keratinocyte adhesion and produces suprabasal acantholysis. Cytotoxic/interface responses generate basal vacuolar change, dyskeratosis, keratinocyte necrosis, and lichenoid inflammation.
4. **Clinical epithelial injury:** these processes cause panstomatitis, blisters, erosions, targetoid/lichenoid lesions, and ocular or genital ulceration.
5. **Airway injury:** antibody deposition and likely cytotoxic T-cell injury damage bronchial epithelium; epithelial shedding and repair lead to small-airway obliteration, irreversible fibrosis, bronchiectasis, and respiratory failure. Anti-epiplakin and anti-DSG1 have correlated with bronchiolitis obliterans in some cohorts, but the causal antigenic hierarchy remains unresolved. (antiga2023s2kguidelineson pages 7-10, antiga2023s2kguidelineson pages 5-7, antiga2023s2kguidelineson pages 3-5)

Histology may show suprabasal acantholysis, dyskeratotic keratinocytes, basal vacuolar alteration, extensive keratinocyte necrosis, epidermal inflammatory exocytosis, lichenoid lymphocytes, or subepithelial cleavage. Multiple patterns can coexist in one patient; acantholysis, necrosis, and lichenoid dermatitis are suggestive but individually insensitive. (antiga2023s2kguidelineson pages 7-10)

**Suggested GO biological processes:** humoral immune response; T-cell-mediated cytotoxicity; antigen-receptor signaling; cell–cell adhesion; desmosome organization; keratinocyte differentiation; epithelial-cell apoptotic process; inflammatory response; wound healing; tissue fibrosis. **Suggested GO cellular components:** desmosome; cell–cell junction; intermediate filament cytoskeleton; cornified envelope; basement membrane. **Suggested CL terms:** keratinocyte, oral epithelial cell, bronchial epithelial cell, urothelial cell, B lymphocyte/plasma cell, CD8-positive αβ T cell, macrophage, fibroblast. Exact ontology identifiers should be programmatically resolved from current releases.

## 7. Anatomical structures affected

Primary sites are oral and oropharyngeal mucosa, epidermis, conjunctiva, anogenital mucosa, and bronchial/bronchiolar epithelium. Secondary sites include nasal, laryngeal, esophageal and intestinal mucosa; nail apparatus; and, less consistently, other organs in associated autoimmune disease. The injury is generally bilateral or diffuse rather than lateralized. Subcellular disease centers on desmosomes, plakins linking intermediate filaments to junctional complexes, and epithelial basement-membrane-zone interfaces. (antiga2023s2kguidelineson pages 7-10, antiga2023s2kguidelineson pages 5-7)

Suggested UBERON mappings include oral epithelium/oral mucosa, lip, tongue, gingiva, pharynx, larynx, esophagus, epidermis, conjunctiva, cornea, genital mucosa, bronchus, bronchiole, lung, and nail. Mapping should use current UBERON accession lookup rather than text-only inference.

## 8. Temporal development

PNP can occur from childhood through older adulthood, but typical adult presentation is approximately **45–70 years**, with no consistent sex preference. Pediatric disease is strongly enriched for Castleman disease. Oral mucositis is usually an early and persistent sign; skin lesions may arise concurrently or later. In approximately 30%, PNP reveals an occult tumor. (falco2024oralparaneoplasticpemphigus pages 2-4, falco2024oralparaneoplasticpemphigus pages 1-2)

The course is generally chronic and progressive rather than self-limited. Bronchiolitis obliterans may arise later even after other manifestations are recognized and is often irreversible. Tumor resection can induce remission, particularly for localized Castleman disease or thymoma, but control of the malignancy does not reliably terminate established autoimmunity. No validated staging system exists. (antiga2023s2kguidelineson pages 5-7, antiga2023s2kguidelineson pages 3-5)

## 9. Inheritance and population epidemiology

Estimated incidence is **<1 per million persons per year**; PNP constitutes approximately **3–5% of pemphigus**. These are estimates rather than registry-grade global incidence data. (antiga2023s2kguidelineson pages 1-3, falco2024oralparaneoplasticpemphigus pages 1-2)

No Mendelian inheritance, familial penetrance, anticipation, germline mosaicism, founder effect, consanguinity effect, or carrier state is recognized. Both sexes are affected without a consistent predominance. Geographic variation largely reflects associated tumors: Castleman-associated PNP is comparatively frequent in East Asian and pediatric series. (falco2024oralparaneoplasticpemphigus pages 2-4, antiga2023s2kguidelineson pages 3-5)

## 10. Diagnostics

### Recommended diagnostic approach

Diagnosis requires concordance among: (1) severe chronic mucositis and compatible polymorphous skin/systemic disease; (2) compatible histology; (3) tissue-bound and circulating autoantibodies; and (4) investigation for an associated neoplasm. The EADV experts explicitly state that **“there are not generally accepted and validated diagnostic criteria”** and recommend a combined clinical–pathologic–serologic approach. (antiga2023s2kguidelineson pages 12-15)

1. Obtain lesional tissue for routine histology and perilesional skin or mucosa for **direct immunofluorescence (DIF)**.
2. Perform **indirect immunofluorescence (IIF) on rat bladder**, commercial envoplakin ELISA, and DSG1/DSG3 assays as appropriate.
3. If results are discordant but suspicion remains high, refer serum for specialized immunoblotting or immunoprecipitation against envoplakin, periplakin, desmoplakins, desmocollins, and A2ML1.
4. Search for occult neoplasia with history, examination, blood count/differential, hematologic assessment, and age/context-appropriate cross-sectional imaging; hematology/oncology should guide lymph-node, marrow, PET/CT, or tumor-specific procedures.
5. Assess pulmonary symptoms promptly with pulmonology review, spirometry/full pulmonary-function testing, oxygenation, and high-resolution CT where indicated. Conduct early ophthalmologic examination and nutritional assessment.

### Test performance

* DIF showing combined intercellular plus linear/granular basement-membrane IgG/C3 was **97% specific**, but only **27–41% sensitive**. Negative DIF therefore does not exclude PNP. (antiga2023s2kguidelineson pages 7-10)
* Rat-bladder IIF was positive in **86%** in one 22-patient study and **74%** in another 19-patient study, with nearly **100% specificity**. Sensitivity differed by tumor—**92.3%** with Castleman disease versus **60%** with thymoma in one Chinese study. (antiga2023s2kguidelineson pages 10-12)
* Commercial envoplakin ELISA detected **25/31 (81%)** PNP sera with approximately **99% specificity** in one study, but only **63%** in another 19-serum series (method paper PMID: **19737550**). (antiga2023s2kguidelineson pages 10-12, antiga2023s2kguidelineson pages 21-23)
* Immunoprecipitation remains most sensitive in expert laboratories: one 19-serum study reported **95%** sensitivity for radioactive and **100%** for non-radioactive IP, but these methods are technically demanding and poorly standardized. (antiga2023s2kguidelineson pages 12-15)
* Experimental A2ML1 ELISA found antibodies in **61% of 36 sera**, with reported **95% sensitivity** and **88.9% specificity**; it is not commercially routine. (antiga2023s2kguidelineson pages 10-12)

### Differential diagnosis

The principal alternatives are pemphigus vulgaris, mucous-membrane pemphigoid, erythema multiforme major, SJS/TEN, severe drug eruption, lichen planus/lichenoid checkpoint-inhibitor eruption, acute GVHD, and Good syndrome. PNP is favored over pemphigus vulgaris by interface dermatitis, keratinocyte necrosis, basement-membrane deposits, rat-bladder IIF positivity, and antibodies to multiple plakins. Mucous-membrane pemphigoid usually shows subepithelial separation and linear basement-membrane staining without intercellular deposits or rat-bladder reactivity. (antiga2023s2kguidelineson pages 12-15, antiga2023s2kguidelineson pages 15-16)

WES, WGS, CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing have no role in diagnosing PNP itself; they may be appropriate only for characterization of the associated neoplasm. There is no asymptomatic population, newborn, carrier, or cascade-genetic screening program.

## 11. Outcome and prognosis

Historic prognosis is poor. An early series reported **90% of 33 patients dead within two years**. A French multicenter cohort of 53 patients found **49% one-year overall survival and 38% five-year survival**. Severe infection was the leading cause of death, followed by bronchiolitis-obliterans respiratory failure and progression of malignancy. (antiga2023s2kguidelineson pages 3-5)

Adverse prognostic features include extensive mucosal/skin involvement, erythema-multiforme- or TEN-like disease, histologic keratinocyte necrosis, and bronchiolitis obliterans. Long-term morbidity includes painful oral disease, malnutrition, scarring ocular disease, chronic pulmonary limitation, bronchiectasis, and toxicity from prolonged immunosuppression. (antiga2023s2kguidelineson pages 5-7, antiga2023s2kguidelineson pages 3-5)

Complete recovery is possible after resection of a localized associated tumor, but established airway fibrosis often persists. Curative resection has produced remission in **up to half** of selected patients with resectable tumors; this figure should not be generalized to disseminated hematologic malignancy. (antiga2023s2kguidelineson pages 3-5)

## 12. Treatment and real-world implementation

No therapy has high-level PNP-specific trial evidence. Management should be coordinated among dermatology, hematology/oncology, oral medicine, pulmonology, ophthalmology, nutrition, and infectious-disease specialists. (antiga2023s2kguidelineson pages 16-19, antiga2023s2kguidelineson pages 15-16)

* **Treat the neoplasm:** resect unicentric Castleman disease or thymoma when feasible; otherwise use tumor-appropriate systemic therapy. Tumor removal is the intervention most capable of eliminating the upstream trigger in localized disease. Suggested NCIT: surgical resection, thymectomy, Castleman disease treatment. (antiga2023s2kguidelineson pages 15-16)
* **Systemic corticosteroids:** prednisolone approximately **0.5–1.5 mg/kg/day** remains first-line. Skin lesions respond better than stomatitis or bronchiolitis obliterans. Toxicities include severe infection, diabetes, osteoporosis, and Cushing syndrome. Suggested NCIT: corticosteroid therapy/prednisolone treatment. (antiga2023s2kguidelineson pages 15-16)
* **Rituximab:** preferred for lymphoproliferative-associated PNP because it targets both malignant and autoreactive CD20-positive B cells. Responses are inconsistent and delayed; infection and hypogammaglobulinemia require monitoring. Suggested NCIT: rituximab therapy, anti-CD20 monoclonal-antibody therapy. (antiga2023s2kguidelineson pages 16-19)
* **Steroid-sparing agents:** azathioprine, mycophenolate mofetil, cyclosporine, cyclophosphamide, or methotrexate are used in combinations supported mainly by case series. IVIG and plasmapheresis may reduce circulating pathogenic antibody burden. (antiga2023s2kguidelineson pages 15-16)
* **Selected targeted treatments:** alemtuzumab has been used in CLL-associated disease; isolated reports support ibrutinib, tocilizumab, thalidomide, and combined B-/T-cell-directed regimens. Evidence is insufficient for comparative response rates. (antiga2023s2kguidelineson pages 16-19, antiga2023s2kguidelineson pages 15-16)
* **Bronchiolitis obliterans:** frequently refractory to corticosteroids. Tumor control plus multidrug immunosuppression/targeted therapy may be attempted; lung transplantation is a last option for irreversible end-stage respiratory failure. (antiga2023s2kguidelineson pages 16-19, antiga2023s2kguidelineson pages 15-16)
* **Supportive care:** meticulous wound and oral care, analgesia, topical anti-inflammatory therapy, infection surveillance/treatment, vaccination review before major immunosuppression, osteoporosis and metabolic prophylaxis, ocular lubrication/scarring prevention, and early high-calorie nutrition. Severe dysphagia may require nasoenteric feeding or gastrostomy. (antiga2023s2kguidelineson pages 5-7)

A ClinicalTrials.gov search identified no clearly PNP-specific interventional efficacy trial. **NCT06643091**, a small phase-2 nintedanib study in unicentric Castleman disease, was not yet recruiting and is not a PNP treatment trial; it should not be represented as evidence of PNP efficacy.

## 13. Prevention

There is no established primary prevention because neither the tumor-associated breakdown of tolerance nor PNP onset can presently be predicted. Vaccination does not prevent PNP, although indicated non-live immunizations before profound immunosuppression may reduce infectious complications.

**Secondary prevention** consists of recognizing unexplained refractory panstomatitis, rapidly obtaining immunopathology, screening for occult neoplasia, and longitudinally repeating tumor assessment when initial screening is negative. **Tertiary prevention** includes early pulmonary-function surveillance, prompt evaluation of dyspnea, ophthalmology review, nutritional intervention, infection prophylaxis where indicated, and minimizing cumulative glucocorticoid toxicity. (antiga2023s2kguidelineson pages 7-10, antiga2023s2kguidelineson pages 16-19, antiga2023s2kguidelineson pages 5-7)

Genetic counseling, prenatal diagnosis, preimplantation testing, and carrier screening are not applicable because PNP is acquired and non-Mendelian.

## 14. Other species and natural disease

Rare spontaneous **canine** PNP-like disease has been described, including antibodies against envoplakin and periplakin, indicating cross-species conservation of plakin autoantigens. Dogs are *Canis lupus familiaris* (NCBI Taxonomy **9615**). The evidence consists of isolated veterinary reports rather than breed-based epidemiology; no VBO-enriched breed association, heritable canine mutation, zoonotic potential, or transmissibility is established.

Human and canine disease share anti-plakin autoimmunity and epithelial blistering, but the scarcity of veterinary cases prevents reliable comparison of tumor spectrum, airway disease, prognosis, or treatment. PNP is not infectious and has no cross-species transmission risk.

## 15. Model organisms and experimental systems

The strongest functional evidence is the **neonatal-mouse passive-transfer model**, in which affinity-purified anti-DSG3 antibodies from PNP sera caused in-vivo acantholysis (Amagai et al., 1998; PMID: **9710446**). This establishes pathogenic potential for the anti-desmosomal fraction but does not reproduce the associated tumor, chronic mucositis, complex anti-plakin repertoire, cytotoxic interface dermatitis, or bronchiolitis obliterans. (antiga2023s2kguidelineson pages 21-23)

General pemphigus mouse systems—including passive IgG transfer and DSG3-specific B- or T-cell models—are useful for studying antibody-mediated adhesion loss and testing B-cell, antibody, and signaling interventions. A 2023 review describes them as tools for pathomechanistic and preclinical therapeutic studies [published April 2023; DOI: https://doi.org/10.3389/fimmu.2023.1169947]. However, no single established animal model faithfully recapitulates full human PNP/PAMS. In-vitro keratinocyte systems can assess acantholysis and antibody binding but cannot model neoplasia-associated tolerance loss or irreversible small-airway fibrosis.

## Ontology-ready summary

The following table condenses the principal quantitative and ontology-mapping findings while explicitly marking identifiers that require validation against current ontology releases.

| domain | finding/statistic | suggested ontology terms/IDs where confidently known | evidence type/limitations |
|---|---|---|---|
| Disease definition | Rare neoplasia-associated autoimmune blistering/multiorgan disease; also termed paraneoplastic autoimmune multiorgan syndrome (PAMS) (antiga2023s2kguidelineson pages 1-3, antiga2023s2kguidelineson pages 3-5) | MONDO: exact ID unverified; MeSH: exact ID unverified; NCIT: Paraneoplastic Pemphigus exact ID unverified | Guideline/review synthesis; not a primary epidemiology registry |
| Epidemiology | Incidence estimated at **<1 case per million persons/year** (antiga2023s2kguidelineson pages 1-3) | Orphan disease concept; exact Orphanet/ICD/MONDO IDs unverified | Guideline statement; rarity limits precision |
| Epidemiology | Accounts for **~3–5% of pemphigus cases** (falco2024oralparaneoplasticpemphigus pages 1-2) | Disease subclass concept; exact ontology ID unverified | 2024 scoping review; proportion depends on source cohorts |
| Demographics | Predominantly affects adults **45–70 years**; no clear gender predilection reported (falco2024oralparaneoplasticpemphigus pages 1-2, falco2024oralparaneoplasticpemphigus pages 2-4) | HPO: Adult onset exact ID unverified | Review-level summary; age distribution varies by associated tumor |
| Associated neoplasms | Most commonly linked to **lymphoproliferative/hematologic malignancies**; solid tumors less common (antiga2023s2kguidelineson pages 1-3, antiga2023s2kguidelineson pages 3-5) | NCIT: Hematologic malignancy exact ID unverified; solid neoplasm exact ID unverified | Guideline consensus; broad category |
| Associated neoplasms | **Castleman disease** may occur in up to **56%** in some series and is more frequent in Asian cohorts; common in children/adolescents (antiga2023s2kguidelineson pages 3-5) | NCIT: Castleman Disease exact ID unverified | Geographic/ethnic variation noted; estimate not universal |
| Associated neoplasms | Solid tumors reported in **14.8–17%** of patients; epithelial ~9%, mesenchymal ~6% (antiga2023s2kguidelineson pages 3-5) | NCIT: Solid Neoplasm exact ID unverified | Derived from retrospective series; uncommon overall |
| Occult cancer relationship | In **~30%** of cases, PNP/PAMS is the first manifestation of occult malignancy (falco2024oralparaneoplasticpemphigus pages 1-2) | NCIT: Occult Neoplasm exact ID unverified | Scoping review; proportion may differ across cohorts |
| Etiology/mechanism | Both **humoral and cell-mediated autoimmunity** target adhesion complexes and basement membrane zone components of stratified epithelia (antiga2023s2kguidelineson pages 3-5) | GO: immune response exact ID unverified; GO: cell-mediated immunity exact ID unverified; GO: humoral immune response exact ID unverified | Mechanistic synthesis; no single causal gene established |
| Molecular targets | Autoantigens include **envoplakin, periplakin, desmoplakin I/II, plectin, BP230, desmoglein 3, desmoglein 1, desmocollins, A2ML1** (antiga2023s2kguidelineson pages 1-3, antiga2023s2kguidelineson pages 7-10, antiga2023s2kguidelineson pages 10-12, antiga2023s2kguidelineson pages 21-23) | HGNC: EVPL, PPL, DSP, PLEC, DST, DSG3, DSG1, DSC1/2/3, A2ML1 | Strong serologic evidence; heterogeneous patient reactivity |
| Autoantibody frequencies | Envoplakin/periplakin reactivity in **up to 88%**; epiplakin **61%**, plectin **57%**, BP230 about **one-third**; Dsg3 **70%**, Dsg1 about **one-third**, desmocollins **62%** (antiga2023s2kguidelineson pages 7-10, antiga2023s2kguidelineson pages 10-12) | HGNC symbols above; CHEBI not applicable | Review of heterogeneous assay studies; frequencies assay-dependent |
| Histopathology | Characteristic findings: **suprabasal acantholysis, dyskeratotic keratinocytes, basal vacuolar change, keratinocyte necrosis, lichenoid/interface infiltrate**, sometimes subepithelial blistering (antiga2023s2kguidelineson pages 7-10) | HPO: Oral erosions exact ID unverified; GO: keratinocyte apoptosis/necrosis exact ID unverified; UBERON: epidermis exact ID unverified | Diagnostic pathology clue, but sensitivity limited |
| Skin phenotypes | Five major cutaneous patterns: **pemphigus-like, pemphigoid-like, lichen planus-like, erythema multiforme-like, GVHD-like**; about **two-thirds** have skin lesions in addition to mucosal disease (antiga2023s2kguidelineson pages 3-5) | HPO terms exact IDs unverified for blistering rash, lichenoid dermatitis, target lesions | Retrospective classification; polymorphism can complicate coding |
| Oral phenotype | **Nearly all patients** have severe, early, treatment-resistant **erosive oral mucositis/panstomatitis** with hemorrhagic lips; may impair nutrition (antiga2023s2kguidelineson pages 5-7) | HPO: Stomatitis exact ID unverified; Oral ulcer exact ID unverified; Dysphagia exact ID unverified; Odynophagia exact ID unverified | Very consistent clinical feature; frequency described qualitatively |
| Ocular phenotype | Ocular involvement in **~40%** of a 104-patient series; conjunctival erosions/scarring, symblepharon, corneal ulceration, reduced visual acuity (antiga2023s2kguidelineson pages 5-7) | HPO: Conjunctivitis/scarring exact IDs unverified; symblepharon exact ID unverified; UBERON: conjunctiva exact ID unverified | Cohort-derived proportion; phenotype severity variable |
| Genital/anogenital phenotype | Genital lesions in **35% (28/79)** in one retrospective study; **62%** in pediatric Castleman-associated cases (antiga2023s2kguidelineson pages 5-7) | HPO: Genital ulceration exact ID unverified | Frequency varies markedly by age/tumor subgroup |
| Pulmonary phenotype | Respiratory involvement reported in **30–90%**; progressive dyspnea and **bronchiolitis obliterans** can lead to respiratory failure; in one series, bronchiolitis obliterans caused **40%** of deaths among fatal cases (antiga2023s2kguidelineson pages 5-7) | HPO: Dyspnea exact ID unverified; Bronchiolitis obliterans exact ID unverified; UBERON: bronchiole/lung exact IDs unverified | Wide range reflects cohort heterogeneity; major prognostic complication |
| Other organ involvement | Gastrointestinal tract may be involved; myasthenia gravis and other autoimmune organ involvement reported, especially with thymoma/Castleman disease (antiga2023s2kguidelineson pages 7-10, antiga2023s2kguidelineson pages 5-7) | HPO/NCIT exact IDs unverified; UBERON: esophagus, colon, skeletal muscle exact IDs unverified | Mostly case series/case reports; not universal |
| Anatomy/tissues | Primary tissues: **oral mucosa, skin epidermis, conjunctiva, genital mucosa, respiratory epithelium/bronchioles** (antiga2023s2kguidelineson pages 5-7, antiga2023s2kguidelineson pages 7-10) | UBERON exact IDs unverified; tissue class: stratified squamous epithelium exact ID unverified | Ontology mapping feasible but exact IDs not verified here |
| Cell types | Main implicated cells: **keratinocytes**, **urothelial cells** (diagnostic substrate), **lymphocytes including activated CD8+ T cells** in GVHD-like lesions (antiga2023s2kguidelineson pages 7-10, antiga2023s2kguidelineson pages 10-12, antiga2023s2kguidelineson pages 15-16) | CL: keratinocyte exact ID unverified; CL: urothelial cell exact ID unverified; CL: CD8-positive alpha-beta T cell exact ID unverified | Cell-type evidence from pathology/immunology; limited direct single-cell data |
| Diagnostic gold-standard concept | Diagnosis relies on combined **clinical, histopathologic, DIF, serologic** findings plus recognition of underlying neoplasm; no universally validated criteria yet (antiga2023s2kguidelineson pages 12-15, antiga2023s2kguidelineson pages 3-5) | NCIT: Direct Immunofluorescence exact ID unverified; Indirect Immunofluorescence exact ID unverified; ELISA exact ID unverified | Expert-consensus approach; criteria still need prospective validation |
| DIF marker | Combined **intercellular + linear/granular BMZ IgG/C3** pattern was **97% specific** but only **27–41% sensitive** (antiga2023s2kguidelineson pages 7-10) | NCIT exact IDs unverified; UBERON: basement membrane zone exact ID unverified | Specific but insensitive; false negatives occur |
| IIF marker | **Rat bladder epithelium** is the most useful IIF substrate; positivity **86%** in one study, **74%** in another, with near-**100% specificity**; sensitivity may be **92.3%** in Castleman-associated disease but **60%** with thymoma (antiga2023s2kguidelineson pages 10-12) | NCIT: Rat bladder IIF exact ID unverified | Best-supported diagnostic marker; performance varies by tumor subtype |
| ELISA marker | Commercial **envoplakin ELISA** detected antibodies in **25/31 (81%)** sera with **~99% specificity** in one study; 63% positive in another 19-sera series (antiga2023s2kguidelineson pages 10-12, antiga2023s2kguidelineson pages 21-23) | HGNC: EVPL; NCIT: ELISA exact ID unverified | Useful and more accessible than IP/IB; not perfectly sensitive |
| ELISA marker | Anti-**A2ML1** ELISA identified antibodies in **61% of 36** sera with **88.9% specificity** and **95% sensitivity**; not commercially available (antiga2023s2kguidelineson pages 10-12) | HGNC: A2ML1 | Promising assay; limited availability |
| IP/IB marker | **Immunoprecipitation/immunoblotting** have high diagnostic performance; in one 19-sera study, sensitivity was **95%** for radioactive IP and **100%** for non-radioactive IP (antiga2023s2kguidelineson pages 12-15) | NCIT exact IDs unverified | Highly sensitive but specialized, labor-intensive, poorly standardized |
| Differential diagnosis | Key differentials: **pemphigus vulgaris, mucous membrane pemphigoid, severe drug reactions, erythema multiforme major/SJS/TEN, GVHD, lichen planus/lichenoid eruptions, Good syndrome** (antiga2023s2kguidelineson pages 12-15, antiga2023s2kguidelineson pages 15-16) | NCIT exact IDs unverified | Important clinically; differentiation often requires immunopathology |
| Distinguishing features vs PV | PNP/PAMS favored by **interface dermatitis/lichenoid infiltrates**, possible **BMZ deposits on DIF**, **rat bladder IIF positivity**, and additional anti-plakin antibodies (antiga2023s2kguidelineson pages 12-15) | HPO exact IDs unverified | Helpful but overlap exists; isolated anti-desmoplakin not specific |
| Course/onset | Onset can precede cancer diagnosis; oral disease usually early and persistent; pulmonary disease may appear later in the course (antiga2023s2kguidelineson pages 5-7, antiga2023s2kguidelineson pages 3-5) | HPO: adult onset exact ID unverified; chronic course exact ID unverified | Natural history variable and tumor-dependent |
| Prognosis | Historically very poor: early review found **90%** of 33 patients died within **2 years**; French multicenter study reported **1-year survival 49%** and **5-year survival 38%** (antiga2023s2kguidelineson pages 3-5) | NCIT: Overall survival exact ID unverified | Older cohorts; outcomes may evolve with current care |
| Prognostic factors | Worse prognosis linked to **erythema multiforme/TEN-like lesions**, **keratinocyte necrosis**, extensive mucocutaneous disease, and **bronchiolitis obliterans** (antiga2023s2kguidelineson pages 3-5, antiga2023s2kguidelineson pages 15-16) | HPO exact IDs unverified | Based largely on retrospective studies |
| Mortality causes | Major causes of death: **severe infection** from immunosuppression, **bronchiolitis obliterans-related respiratory failure**, and progression of underlying malignancy (antiga2023s2kguidelineson pages 3-5, antiga2023s2kguidelineson pages 16-19) | NCIT exact IDs unverified | Cause-of-death distributions from retrospective cohorts |
| First-line treatment | **Systemic corticosteroids** (prednisolone **0.5–1.5 mg/kg/day**) remain first-line; cutaneous lesions respond better than mucositis/bronchiolitis obliterans (antiga2023s2kguidelineson pages 1-3, antiga2023s2kguidelineson pages 15-16) | NCIT: Prednisolone exact ID unverified; systemic corticosteroid exact ID unverified | Standard practice despite lack of controlled trials |
| Steroid-sparing therapy | Common adjuncts: **azathioprine, mycophenolate mofetil, cyclosporine, cyclophosphamide, methotrexate**, sometimes **IVIG** (antiga2023s2kguidelineson pages 15-16, falco2024oralparaneoplasticpemphigus pages 2-4) | NCIT exact IDs unverified for each drug | Evidence mainly case series/reports |
| Targeted/biologic therapy | For B-cell malignancy-associated disease, **rituximab** is preferred; **alemtuzumab**, **tocilizumab**, **ibrutinib**, **plasmapheresis**, and **thalidomide** have sporadic supportive evidence (antiga2023s2kguidelineson pages 16-19, antiga2023s2kguidelineson pages 15-16) | NCIT exact IDs unverified: Rituximab, Alemtuzumab, Tocilizumab, Ibrutinib, Plasmapheresis, Thalidomide | No robust response-rate trials in gathered evidence |
| Tumor-directed treatment | Treating/resecting the underlying tumor is recommended; curative surgery for resectable tumors such as **Castleman disease** or **thymoma** may lead to remission in **up to half** of patients (antiga2023s2kguidelineson pages 3-5, antiga2023s2kguidelineson pages 15-16) | NCIT: Surgical resection exact ID unverified; Castleman disease, thymoma exact IDs unverified | Benefit most evident in resectable localized tumors |
| Supportive care | Severe oral disease may require **nutritional support**, nasoenteric tube or gastrostomy; multidisciplinary dermatology-oncology/pulmonology/ophthalmology care recommended (antiga2023s2kguidelineson pages 5-7, antiga2023s2kguidelineson pages 16-19, antiga2023s2kguidelineson pages 15-16) | NCIT exact IDs unverified | Practical management guidance, not trial-derived |
| Prevention/screening | No established primary prevention; in suspected cases without known cancer, **oncologic screening** and extended follow-up are recommended to search for occult malignancy (antiga2023s2kguidelineson pages 7-10, antiga2023s2kguidelineson pages 3-5) | NCIT: Cancer screening exact ID unverified | Secondary prevention focused on early tumor detection |
| Genetics | No established monogenic causal germline etiology identified in gathered evidence; disease is primarily **paraneoplastic/autoimmune** rather than inherited (antiga2023s2kguidelineson pages 3-5, antiga2023s2kguidelineson pages 1-3) | HGNC/OMIM causal gene: none established from gathered evidence | Absence of evidence in retrieved sources; does not exclude susceptibility loci |
| Susceptibility genetics | Review-level statement cites possible HLA associations, but exact primary evidence was not gathered/validated here; use with caution (malik2021anupdatedreview pages 4-6) | HLA terms/IDs unverified | Low-confidence in this artifact because not confirmed from primary evidence gathered |
| Environmental/drug triggers | Rare reports of triggering/exacerbation by **fludarabine, bendamustine, cyclophosphamide**, or **radiotherapy** (antiga2023s2kguidelineson pages 3-5) | CHEBI/NCIT exact IDs unverified | Anecdotal/case-report level evidence |
| Infectious/protective factors | No specific infectious cause or protective factors established in gathered evidence (antiga2023s2kguidelineson pages 3-5, antiga2023s2kguidelineson pages 15-16) | Not applicable | Important negative finding based on current retrieved evidence |
| Animal/natural disease | Canine natural disease with **envoplakin/periplakin** as target antigens is reported in cited literature, but full source text was not gathered here (cited in retrieved search context) | NCBI Taxon: dog exact ID unverified; HGNC ortholog mapping not verified | Low-confidence mention only; primary details not extracted in evidence set |
| Experimental models | Passive-transfer evidence supports pathogenicity of **anti-Dsg3** antibodies causing acantholysis in neonatal mice; pemphigus mouse models discussed in 2023 review context (antiga2023s2kguidelineson pages 21-23) | NCBITaxon: mouse exact ID unverified; HGNC: DSG3 | Primary PMID available from reference list (9710446); model details limited in gathered text |


*Table: This table condenses the gathered evidence on paraneoplastic pemphigus/paraneoplastic autoimmune multiorgan syndrome into ontology-ready disease facts. It highlights clinical features, molecular targets, diagnostics, associated neoplasms, treatments, and prognosis while clearly marking where exact ontology identifiers were not verified.*

## Key evidence and research gaps

The 2024 diagnostic review states that exact AIBD diagnosis depends on “the clinical appearance combined with the detection of tissue-bound and circulating autoantibodies” and identifies envoplakin as the major antigen-specific marker for PNP [published June 2024; DOI: https://doi.org/10.3389/fimmu.2024.1363032]. This supports a multimodal rather than single-test diagnosis. (antiga2023s2kguidelineson pages 12-15, antiga2023s2kguidelineson pages 10-12)

The most important unresolved issues are: prospective validation of diagnostic criteria; standardized anti-plakin/A2ML1 assays; biomarkers predicting bronchiolitis obliterans; contemporary tumor-stratified survival estimates; controlled evaluation of rituximab and combination regimens; PNP-specific quality-of-life measures; and models integrating neoplasia, B-/T-cell autoimmunity, mucositis, and airway fibrosis. The EADV guideline itself emphasizes that its consensus criteria require “validation by large multicentric prospective investigations.” (antiga2023s2kguidelineson pages 16-19)

### Principal recent sources

1. Antiga E, et al. **S2k guidelines on the management of paraneoplastic pemphigus/paraneoplastic autoimmune multiorgan syndrome.** *J Eur Acad Dermatol Venereol.* Published March 2023; 37:1118–1134. DOI/URL: https://doi.org/10.1111/jdv.18931. (antiga2023s2kguidelineson pages 1-3)
2. De Falco D, Messina S, Petruzzi M. **Oral Paraneoplastic Pemphigus: A Scoping Review on Pathogenetic Mechanisms and Histo-Serological Profile.** *Antibodies.* Published November 2024;13:95. DOI/URL: https://doi.org/10.3390/antib13040095. (falco2024oralparaneoplasticpemphigus pages 2-4, falco2024oralparaneoplasticpemphigus pages 1-2)
3. van Beek N, et al. **State-of-the-art diagnosis of autoimmune blistering diseases.** *Front Immunol.* Published June 2024;15:1363032. DOI/URL: https://doi.org/10.3389/fimmu.2024.1363032. (antiga2023s2kguidelineson pages 12-15, antiga2023s2kguidelineson pages 10-12)
4. Anhalt GJ, et al. **Paraneoplastic pemphigus: an autoimmune mucocutaneous disease associated with neoplasia.** *N Engl J Med.* 1990;323:1729–1735. PMID: **2247105**. (antiga2023s2kguidelineson pages 21-23)
5. Amagai M, et al. **Antibodies against desmoglein 3…cause acantholysis in vivo in neonatal mice.** *J Clin Invest.* 1998;102:775–782. PMID: **9710446**. (antiga2023s2kguidelineson pages 21-23)

References

1. (antiga2023s2kguidelineson pages 1-3): Emiliano Antiga, Rikke Bech, Roberto Maglie, Giovanni Genovese, Luca Borradori, Barbara Bockle, Marzia Caproni, Frédéric Caux, Nisha Suyien Chandran, Alberto Corrà, Francesco D'Amore, Maryam Daneshpazhooh, Dipankar De, Dario Didona, Marian Dmochowski, Kossara Drenovska, Jan Ehrchen, Claudio Feliciani, Matthias Goebeler, Richard Groves, Claudia Günther, Sanjeev Handa, Silke C. Hofmann, Barbara Horvath, Dimitrios Ioannidis, Hana Jedlickova, Cezary Kowalewski, Khalaf Kridin, Pascal Joly, Yen Loo Lim, Branka Marinovic, Emanual Maverakis, Joost Meijer, Aikaterini Patsatsi, Carlo Pincelli, Catherine Prost, Jane Setterfield, Eli Sprecher, Dusan Skiljevic, Kaisa Tasanen, Soner Uzun, Nina Van Beek, Snejina Vassileva, Artem Vorobyev, Igor Vujic, Gang Wang, Mingyue Wang, Katarzyna Wozniak, Savas Yayli, Giovanna Zambruno, Takashi Hashimoto, Enno Schmidt, José Manuel Mascarò, and Angelo Valerio Marzano. S2k guidelines on the management of paraneoplastic pemphigus/paraneoplastic autoimmune multiorgan syndrome initiated by the european academy of dermatology and venereology (eadv). Journal of the European Academy of Dermatology and Venereology, 37:1118-1134, Mar 2023. URL: https://doi.org/10.1111/jdv.18931, doi:10.1111/jdv.18931. This article has 78 citations and is from a domain leading peer-reviewed journal.

2. (falco2024oralparaneoplasticpemphigus pages 2-4): Domenico De Falco, Sabrina Messina, and Massimo Petruzzi. Oral paraneoplastic pemphigus: a scoping review on pathogenetic mechanisms and histo-serological profile. Antibodies, 13:95, Nov 2024. URL: https://doi.org/10.3390/antib13040095, doi:10.3390/antib13040095. This article has 8 citations.

3. (antiga2023s2kguidelineson pages 16-19): Emiliano Antiga, Rikke Bech, Roberto Maglie, Giovanni Genovese, Luca Borradori, Barbara Bockle, Marzia Caproni, Frédéric Caux, Nisha Suyien Chandran, Alberto Corrà, Francesco D'Amore, Maryam Daneshpazhooh, Dipankar De, Dario Didona, Marian Dmochowski, Kossara Drenovska, Jan Ehrchen, Claudio Feliciani, Matthias Goebeler, Richard Groves, Claudia Günther, Sanjeev Handa, Silke C. Hofmann, Barbara Horvath, Dimitrios Ioannidis, Hana Jedlickova, Cezary Kowalewski, Khalaf Kridin, Pascal Joly, Yen Loo Lim, Branka Marinovic, Emanual Maverakis, Joost Meijer, Aikaterini Patsatsi, Carlo Pincelli, Catherine Prost, Jane Setterfield, Eli Sprecher, Dusan Skiljevic, Kaisa Tasanen, Soner Uzun, Nina Van Beek, Snejina Vassileva, Artem Vorobyev, Igor Vujic, Gang Wang, Mingyue Wang, Katarzyna Wozniak, Savas Yayli, Giovanna Zambruno, Takashi Hashimoto, Enno Schmidt, José Manuel Mascarò, and Angelo Valerio Marzano. S2k guidelines on the management of paraneoplastic pemphigus/paraneoplastic autoimmune multiorgan syndrome initiated by the european academy of dermatology and venereology (eadv). Journal of the European Academy of Dermatology and Venereology, 37:1118-1134, Mar 2023. URL: https://doi.org/10.1111/jdv.18931, doi:10.1111/jdv.18931. This article has 78 citations and is from a domain leading peer-reviewed journal.

4. (antiga2023s2kguidelineson pages 21-23): Emiliano Antiga, Rikke Bech, Roberto Maglie, Giovanni Genovese, Luca Borradori, Barbara Bockle, Marzia Caproni, Frédéric Caux, Nisha Suyien Chandran, Alberto Corrà, Francesco D'Amore, Maryam Daneshpazhooh, Dipankar De, Dario Didona, Marian Dmochowski, Kossara Drenovska, Jan Ehrchen, Claudio Feliciani, Matthias Goebeler, Richard Groves, Claudia Günther, Sanjeev Handa, Silke C. Hofmann, Barbara Horvath, Dimitrios Ioannidis, Hana Jedlickova, Cezary Kowalewski, Khalaf Kridin, Pascal Joly, Yen Loo Lim, Branka Marinovic, Emanual Maverakis, Joost Meijer, Aikaterini Patsatsi, Carlo Pincelli, Catherine Prost, Jane Setterfield, Eli Sprecher, Dusan Skiljevic, Kaisa Tasanen, Soner Uzun, Nina Van Beek, Snejina Vassileva, Artem Vorobyev, Igor Vujic, Gang Wang, Mingyue Wang, Katarzyna Wozniak, Savas Yayli, Giovanna Zambruno, Takashi Hashimoto, Enno Schmidt, José Manuel Mascarò, and Angelo Valerio Marzano. S2k guidelines on the management of paraneoplastic pemphigus/paraneoplastic autoimmune multiorgan syndrome initiated by the european academy of dermatology and venereology (eadv). Journal of the European Academy of Dermatology and Venereology, 37:1118-1134, Mar 2023. URL: https://doi.org/10.1111/jdv.18931, doi:10.1111/jdv.18931. This article has 78 citations and is from a domain leading peer-reviewed journal.

5. (antiga2023s2kguidelineson pages 3-5): Emiliano Antiga, Rikke Bech, Roberto Maglie, Giovanni Genovese, Luca Borradori, Barbara Bockle, Marzia Caproni, Frédéric Caux, Nisha Suyien Chandran, Alberto Corrà, Francesco D'Amore, Maryam Daneshpazhooh, Dipankar De, Dario Didona, Marian Dmochowski, Kossara Drenovska, Jan Ehrchen, Claudio Feliciani, Matthias Goebeler, Richard Groves, Claudia Günther, Sanjeev Handa, Silke C. Hofmann, Barbara Horvath, Dimitrios Ioannidis, Hana Jedlickova, Cezary Kowalewski, Khalaf Kridin, Pascal Joly, Yen Loo Lim, Branka Marinovic, Emanual Maverakis, Joost Meijer, Aikaterini Patsatsi, Carlo Pincelli, Catherine Prost, Jane Setterfield, Eli Sprecher, Dusan Skiljevic, Kaisa Tasanen, Soner Uzun, Nina Van Beek, Snejina Vassileva, Artem Vorobyev, Igor Vujic, Gang Wang, Mingyue Wang, Katarzyna Wozniak, Savas Yayli, Giovanna Zambruno, Takashi Hashimoto, Enno Schmidt, José Manuel Mascarò, and Angelo Valerio Marzano. S2k guidelines on the management of paraneoplastic pemphigus/paraneoplastic autoimmune multiorgan syndrome initiated by the european academy of dermatology and venereology (eadv). Journal of the European Academy of Dermatology and Venereology, 37:1118-1134, Mar 2023. URL: https://doi.org/10.1111/jdv.18931, doi:10.1111/jdv.18931. This article has 78 citations and is from a domain leading peer-reviewed journal.

6. (falco2024oralparaneoplasticpemphigus pages 1-2): Domenico De Falco, Sabrina Messina, and Massimo Petruzzi. Oral paraneoplastic pemphigus: a scoping review on pathogenetic mechanisms and histo-serological profile. Antibodies, 13:95, Nov 2024. URL: https://doi.org/10.3390/antib13040095, doi:10.3390/antib13040095. This article has 8 citations.

7. (antiga2023s2kguidelineson pages 5-7): Emiliano Antiga, Rikke Bech, Roberto Maglie, Giovanni Genovese, Luca Borradori, Barbara Bockle, Marzia Caproni, Frédéric Caux, Nisha Suyien Chandran, Alberto Corrà, Francesco D'Amore, Maryam Daneshpazhooh, Dipankar De, Dario Didona, Marian Dmochowski, Kossara Drenovska, Jan Ehrchen, Claudio Feliciani, Matthias Goebeler, Richard Groves, Claudia Günther, Sanjeev Handa, Silke C. Hofmann, Barbara Horvath, Dimitrios Ioannidis, Hana Jedlickova, Cezary Kowalewski, Khalaf Kridin, Pascal Joly, Yen Loo Lim, Branka Marinovic, Emanual Maverakis, Joost Meijer, Aikaterini Patsatsi, Carlo Pincelli, Catherine Prost, Jane Setterfield, Eli Sprecher, Dusan Skiljevic, Kaisa Tasanen, Soner Uzun, Nina Van Beek, Snejina Vassileva, Artem Vorobyev, Igor Vujic, Gang Wang, Mingyue Wang, Katarzyna Wozniak, Savas Yayli, Giovanna Zambruno, Takashi Hashimoto, Enno Schmidt, José Manuel Mascarò, and Angelo Valerio Marzano. S2k guidelines on the management of paraneoplastic pemphigus/paraneoplastic autoimmune multiorgan syndrome initiated by the european academy of dermatology and venereology (eadv). Journal of the European Academy of Dermatology and Venereology, 37:1118-1134, Mar 2023. URL: https://doi.org/10.1111/jdv.18931, doi:10.1111/jdv.18931. This article has 78 citations and is from a domain leading peer-reviewed journal.

8. (antiga2023s2kguidelineson pages 7-10): Emiliano Antiga, Rikke Bech, Roberto Maglie, Giovanni Genovese, Luca Borradori, Barbara Bockle, Marzia Caproni, Frédéric Caux, Nisha Suyien Chandran, Alberto Corrà, Francesco D'Amore, Maryam Daneshpazhooh, Dipankar De, Dario Didona, Marian Dmochowski, Kossara Drenovska, Jan Ehrchen, Claudio Feliciani, Matthias Goebeler, Richard Groves, Claudia Günther, Sanjeev Handa, Silke C. Hofmann, Barbara Horvath, Dimitrios Ioannidis, Hana Jedlickova, Cezary Kowalewski, Khalaf Kridin, Pascal Joly, Yen Loo Lim, Branka Marinovic, Emanual Maverakis, Joost Meijer, Aikaterini Patsatsi, Carlo Pincelli, Catherine Prost, Jane Setterfield, Eli Sprecher, Dusan Skiljevic, Kaisa Tasanen, Soner Uzun, Nina Van Beek, Snejina Vassileva, Artem Vorobyev, Igor Vujic, Gang Wang, Mingyue Wang, Katarzyna Wozniak, Savas Yayli, Giovanna Zambruno, Takashi Hashimoto, Enno Schmidt, José Manuel Mascarò, and Angelo Valerio Marzano. S2k guidelines on the management of paraneoplastic pemphigus/paraneoplastic autoimmune multiorgan syndrome initiated by the european academy of dermatology and venereology (eadv). Journal of the European Academy of Dermatology and Venereology, 37:1118-1134, Mar 2023. URL: https://doi.org/10.1111/jdv.18931, doi:10.1111/jdv.18931. This article has 78 citations and is from a domain leading peer-reviewed journal.

9. (antiga2023s2kguidelineson pages 10-12): Emiliano Antiga, Rikke Bech, Roberto Maglie, Giovanni Genovese, Luca Borradori, Barbara Bockle, Marzia Caproni, Frédéric Caux, Nisha Suyien Chandran, Alberto Corrà, Francesco D'Amore, Maryam Daneshpazhooh, Dipankar De, Dario Didona, Marian Dmochowski, Kossara Drenovska, Jan Ehrchen, Claudio Feliciani, Matthias Goebeler, Richard Groves, Claudia Günther, Sanjeev Handa, Silke C. Hofmann, Barbara Horvath, Dimitrios Ioannidis, Hana Jedlickova, Cezary Kowalewski, Khalaf Kridin, Pascal Joly, Yen Loo Lim, Branka Marinovic, Emanual Maverakis, Joost Meijer, Aikaterini Patsatsi, Carlo Pincelli, Catherine Prost, Jane Setterfield, Eli Sprecher, Dusan Skiljevic, Kaisa Tasanen, Soner Uzun, Nina Van Beek, Snejina Vassileva, Artem Vorobyev, Igor Vujic, Gang Wang, Mingyue Wang, Katarzyna Wozniak, Savas Yayli, Giovanna Zambruno, Takashi Hashimoto, Enno Schmidt, José Manuel Mascarò, and Angelo Valerio Marzano. S2k guidelines on the management of paraneoplastic pemphigus/paraneoplastic autoimmune multiorgan syndrome initiated by the european academy of dermatology and venereology (eadv). Journal of the European Academy of Dermatology and Venereology, 37:1118-1134, Mar 2023. URL: https://doi.org/10.1111/jdv.18931, doi:10.1111/jdv.18931. This article has 78 citations and is from a domain leading peer-reviewed journal.

10. (antiga2023s2kguidelineson pages 15-16): Emiliano Antiga, Rikke Bech, Roberto Maglie, Giovanni Genovese, Luca Borradori, Barbara Bockle, Marzia Caproni, Frédéric Caux, Nisha Suyien Chandran, Alberto Corrà, Francesco D'Amore, Maryam Daneshpazhooh, Dipankar De, Dario Didona, Marian Dmochowski, Kossara Drenovska, Jan Ehrchen, Claudio Feliciani, Matthias Goebeler, Richard Groves, Claudia Günther, Sanjeev Handa, Silke C. Hofmann, Barbara Horvath, Dimitrios Ioannidis, Hana Jedlickova, Cezary Kowalewski, Khalaf Kridin, Pascal Joly, Yen Loo Lim, Branka Marinovic, Emanual Maverakis, Joost Meijer, Aikaterini Patsatsi, Carlo Pincelli, Catherine Prost, Jane Setterfield, Eli Sprecher, Dusan Skiljevic, Kaisa Tasanen, Soner Uzun, Nina Van Beek, Snejina Vassileva, Artem Vorobyev, Igor Vujic, Gang Wang, Mingyue Wang, Katarzyna Wozniak, Savas Yayli, Giovanna Zambruno, Takashi Hashimoto, Enno Schmidt, José Manuel Mascarò, and Angelo Valerio Marzano. S2k guidelines on the management of paraneoplastic pemphigus/paraneoplastic autoimmune multiorgan syndrome initiated by the european academy of dermatology and venereology (eadv). Journal of the European Academy of Dermatology and Venereology, 37:1118-1134, Mar 2023. URL: https://doi.org/10.1111/jdv.18931, doi:10.1111/jdv.18931. This article has 78 citations and is from a domain leading peer-reviewed journal.

11. (antiga2023s2kguidelineson pages 12-15): Emiliano Antiga, Rikke Bech, Roberto Maglie, Giovanni Genovese, Luca Borradori, Barbara Bockle, Marzia Caproni, Frédéric Caux, Nisha Suyien Chandran, Alberto Corrà, Francesco D'Amore, Maryam Daneshpazhooh, Dipankar De, Dario Didona, Marian Dmochowski, Kossara Drenovska, Jan Ehrchen, Claudio Feliciani, Matthias Goebeler, Richard Groves, Claudia Günther, Sanjeev Handa, Silke C. Hofmann, Barbara Horvath, Dimitrios Ioannidis, Hana Jedlickova, Cezary Kowalewski, Khalaf Kridin, Pascal Joly, Yen Loo Lim, Branka Marinovic, Emanual Maverakis, Joost Meijer, Aikaterini Patsatsi, Carlo Pincelli, Catherine Prost, Jane Setterfield, Eli Sprecher, Dusan Skiljevic, Kaisa Tasanen, Soner Uzun, Nina Van Beek, Snejina Vassileva, Artem Vorobyev, Igor Vujic, Gang Wang, Mingyue Wang, Katarzyna Wozniak, Savas Yayli, Giovanna Zambruno, Takashi Hashimoto, Enno Schmidt, José Manuel Mascarò, and Angelo Valerio Marzano. S2k guidelines on the management of paraneoplastic pemphigus/paraneoplastic autoimmune multiorgan syndrome initiated by the european academy of dermatology and venereology (eadv). Journal of the European Academy of Dermatology and Venereology, 37:1118-1134, Mar 2023. URL: https://doi.org/10.1111/jdv.18931, doi:10.1111/jdv.18931. This article has 78 citations and is from a domain leading peer-reviewed journal.

12. (malik2021anupdatedreview pages 4-6): Ali M. Malik, Sarah Tupchong, Simo Huang, Abhirup Are, Sylvia Hsu, and Kiran Motaparthi. An updated review of pemphigus diseases. Oct 2021. URL: https://doi.org/10.3390/medicina57101080, doi:10.3390/medicina57101080. This article has 179 citations.

## Artifacts

- [Edison artifact artifact-00](Paraneoplastic_Pemphigus-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.