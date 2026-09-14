---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T09:07:43.687201'
end_time: '2026-08-19T09:20:52.693615'
duration_seconds: 789.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adult-Onset Myasthenia Gravis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 53
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 16
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - DOI:10.3390/jcm13010236
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Adult-Onset_Myasthenia_Gravis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Adult-Onset Myasthenia Gravis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Adult-Onset Myasthenia Gravis** covering all of the
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
- **Disease Name:** Adult-Onset Myasthenia Gravis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Adult-Onset Myasthenia Gravis** covering all of the
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


# Adult-Onset Myasthenia Gravis: Comprehensive Disease-Characteristics Report

**Scope.** This report concerns **acquired adult-onset autoimmune myasthenia gravis (MG)**, not congenital myasthenic syndromes (CMS), Lambert–Eaton myasthenic syndrome, or transient neonatal MG. Evidence is labeled as **human clinical**, **human genetic/computational**, **model-organism**, or **in vitro**. Unless otherwise stated, facts are aggregated disease-level knowledge rather than observations from an individual electronic health record.

## Executive summary

Adult-onset MG is a chronic, heterogeneous, T-cell-dependent, autoantibody-mediated disorder of the **postsynaptic neuromuscular junction (NMJ)**. Its defining manifestation is fluctuating, fatigable weakness affecting ocular, bulbar, axial, limb, and sometimes respiratory muscles. Approximately 80% of generalized cases have acetylcholine-receptor antibodies (AChR-Ab); MuSK antibodies account for about 5%–8% of AChR-negative cases, while LRP4-associated and seronegative disease are less common. The 2024 JCI review accurately summarizes the spectrum as weakness “**ranging from limited ocular muscle involvement to life-threatening respiratory failure**.” [Published June 2024; DOI/URL](https://doi.org/10.1172/JCI179742). (kaminski2024myastheniagravisthe pages 1-2)

The disease is not ordinarily monogenic. HLA and immune-regulatory loci confer polygenic susceptibility, whereas pathogenic germline variants in *CHRNE, RAPSN, DOK7, MUSK, LRP4, AGRN,* and related genes cause CMS and should not be misclassified as causal variants for autoimmune adult-onset MG. Treatment has shifted from nonspecific immunosuppression toward antibody-endotype-directed complement C5 inhibition, FcRn blockade, and B-cell depletion. Nevertheless, conventional therapy, thymectomy in selected AChR-positive disease, and IVIG/plasma exchange in crisis remain central. (OpenTargets Search: myasthenia gravis, kaminski2024myastheniagravisthe pages 1-2, wiendl2023guidelineforthe pages 2-3)

## 1. Disease information

### Definition and classification

MG is an acquired autoimmune disorder in which antibodies against postsynaptic proteins reduce the safety factor for neuromuscular transmission. Clinical classification integrates:

- distribution: ocular versus generalized;
- onset: early-onset versus late-onset, commonly separated at 50 years, although studies use 40–60-year cutoffs;
- antibody: AChR, MuSK, LRP4, or seronegative;
- thymic pathology: thymoma-associated, hyperplastic, or non-thymomatous;
- special trigger: immune-checkpoint-inhibitor-associated MG. (antonioni2023theincidenceof pages 1-2, kaminski2024myastheniagravisthe pages 2-4)

### Identifiers and synonyms

- **MONDO:** adult-onset myasthenia gravis **MONDO:0018324**; parent MG **MONDO:0009688**.
- **ICD-10-CM:** **G70.0**, myasthenia gravis without acute exacerbation; more specific national extensions distinguish exacerbation/crisis.
- **ICD-11:** classified under myasthenia gravis within disorders of the neuromuscular junction.
- **MeSH:** *Myasthenia Gravis*.
- **Orphanet:** myasthenia gravis is represented as a rare autoimmune NMJ disease; national subtype coding varies.
- Common labels: autoimmune MG, acquired MG, adult MG, adult-onset MG, ocular MG, generalized MG (gMG), late-onset MG (LOMG), AChR-MG, MuSK-MG, LRP4-MG, and seronegative MG. “Late-onset” is a subtype rather than a synonym for every adult case.

The reusable ontology mapping is summarized below.

| Domain | Core entity/finding | Suggested ontology identifiers/terms | Evidence/interpretive note |
|---|---|---|---|
| Disease identity | Adult-onset autoimmune myasthenia gravis | MONDO: MONDO_0018324; parent disease MONDO_0009688 myasthenia gravis; ICD-10: G70.0 | Adult-onset MG is an antibody-mediated autoimmune neuromuscular junction disease; age-, antibody-, thymus-, and trigger-based subgroups are clinically meaningful (kaminski2024myastheniagravisthe pages 1-2, wiendl2023guidelineforthe pages 2-3) |
| Classification | Autoimmune, acquired, postsynaptic neuromuscular junction disorder | MeSH: Myasthenia Gravis; category: autoimmune disease; not congenital myasthenic syndrome | Guideline and review distinguish autoimmune MG from congenital myasthenic syndromes; routine knowledge base entry should treat adult-onset MG as acquired disease-level knowledge, not single-patient EHR-derived only (wiendl2023guidelineforthe pages 3-4, wiendl2023guidelineforthe pages 2-3) |
| Synonyms | Adult-onset MG; late-onset MG subset when onset ≥50 years; generalized MG / ocular MG as phenotypic forms | Labels only: adult-onset myasthenia gravis; autoimmune myasthenia gravis | Early- vs late-onset and ocular vs generalized are clinically useful sub-stratifications rather than strict synonyms (kaminski2024myastheniagravisthe pages 2-4, antonioni2023theincidenceof pages 1-2) |
| Core autoantibody endotypes | AChR-MG, MuSK-MG, LRP4-MG, seronegative MG | AChR antibody positive; MuSK antibody positive; LRP4 antibody positive; seronegative MG | About 80% of generalized MG and ~50% of ocular MG have AChR antibodies; MuSK antibodies occur in 5%–8% of AChR-negative patients; LRP4 is less common (kaminski2024myastheniagravisthe pages 1-2, gu2024efficacyandsafety pages 1-2) |
| Phenotype | Fluctuating fatigable weakness | HPO: Muscle weakness; Fatigability | Hallmark symptom complex used diagnostically and in severity scoring (kaminski2024myastheniagravisthe pages 1-2, wiendl2023guidelineforthe pages 3-4) |
| Phenotype | Ptosis | HPO: Ptosis | Common ocular presentation; ocular MG defined by ptosis/diplopia-limited disease (kaminski2024myastheniagravisthe pages 1-2, antonioni2023theincidenceof pages 1-2) |
| Phenotype | Diplopia | HPO: Diplopia | Core ocular manifestation and frequent presenting feature (kaminski2024myastheniagravisthe pages 1-2) |
| Phenotype | Bulbar weakness/dysphagia/dysarthria | HPO: Dysphagia; Dysarthria; Bulbar palsy | Especially prominent in MuSK-MG and severe generalized disease (vakrakou2023immunotherapiesinmuskpositive pages 1-2, kaminski2024myastheniagravisthe pages 1-2) |
| Phenotype | Respiratory insufficiency / myasthenic crisis | HPO: Respiratory insufficiency; Acute respiratory failure | Life-threatening generalized phenotype; crises incorporated into active/refractory disease definitions (kaminski2024myastheniagravisthe pages 1-2, wiendl2023guidelineforthe pages 3-4) |
| Phenotype | Generalized limb/axial weakness | HPO: Proximal muscle weakness; Generalized weakness | Generalized MG may involve ocular, bulbar, axial, limb, and respiratory muscles (kaminski2024myastheniagravisthe pages 1-2, wiendl2023guidelineforthe pages 2-3) |
| Burden/QoL | Persistent fatigue and reduced quality of life | MG-ADL; QMG; MG-QoL15r; EQ-5D-5L | Fatigue can persist even in pharmacologic remission and is associated with lower QoL/depressive symptoms (wiendl2023guidelineforthe pages 17-19, wiendl2023guidelineforthe pages 2-3) |
| Anatomy | Primary anatomical site: neuromuscular junction | UBERON: neuromuscular junction; synapse; skeletal muscle | Disease mechanism centers on the postsynaptic muscle membrane of the NMJ (kaminski2024myastheniagravisthe pages 1-2, kaminski2024myastheniagravisthe pages 2-4) |
| Anatomy | Postsynaptic membrane / motor end plate | UBERON labels: motor end plate; postsynaptic membrane | AChR loss, fold simplification, and MAC injury are localized here (kaminski2024myastheniagravisthe pages 2-4) |
| Anatomy | Thymus involvement in major subgroups | UBERON: thymus | Thymic hyperplasia and thymoma are relevant in AChR-MG; MuSK-MG generally lacks prominent thymic involvement; all patients should be imaged for thymoma (wiendl2023guidelineforthe pages 2-3, vakrakou2023immunotherapiesinmuskpositive pages 1-2) |
| Cell types | Autoreactive B cells / plasmablasts / plasma cells | CL: B cell; plasmablast; plasma cell | B-cell activation and autoantibody production are central upstream mechanisms; rituximab responsiveness supports B-cell contribution (vakrakou2023immunotherapiesinmuskpositive pages 1-2, kaminski2024myastheniagravisthe pages 10-11) |
| Cell types | CD4+ T cells / T follicular helper-like support | CL: T cell; CD4-positive, alpha-beta T cell | MG is T-cell-dependent and antibody-mediated; tolerance failure and T-cell help sustain pathogenic antibodies (kaminski2024myastheniagravisthe pages 1-2) |
| Cell types | Thymic epithelial cells | CL label: thymic epithelial cell | Aberrant thymic biology contributes particularly to AChR-MG and thymoma-associated MG (kaminski2024myastheniagravisthe pages 10-11, seldin2015genomewideassociationstudy pages 1-2) |
| Mechanism | Complement-mediated postsynaptic injury in AChR-MG | GO: complement activation; membrane attack complex assembly | AChR IgG1/IgG3 antibodies activate complement, causing MAC-mediated injury and fold loss; rationale for C5 inhibitors (kaminski2024myastheniagravisthe pages 2-4, wiendl2023guidelineforthe pages 2-3) |
| Mechanism | Antigenic modulation/internalization of AChR | GO: receptor-mediated endocytosis; acetylcholine receptor clustering | Cross-linking promotes AChR endocytosis/degradation, reducing receptor density (kaminski2024myastheniagravisthe pages 2-4) |
| Mechanism | Functional block of ACh binding | GO label: chemical synaptic transmission; acetylcholine receptor activity | Some antibodies directly block AChR function at the binding site (kaminski2024myastheniagravisthe pages 2-4) |
| Mechanism | MuSK-LRP4 signaling disruption | GO labels: receptor signaling pathway; neuromuscular junction development; acetylcholine receptor clustering | MuSK IgG4 antibodies interfere with LRP4-MuSK interaction and impair AChR clustering rather than complement fixation (vakrakou2023immunotherapiesinmuskpositive pages 1-2) |
| Mechanism | FcRn-mediated IgG recycling sustains pathogenic antibodies | Target: FCGRT; GO label: IgG receptor activity / immunoglobulin recycling | FcRn antagonists reduce circulating IgG including pathogenic autoantibodies (wiendl2023guidelineforthe pages 2-3, OpenTargets Search: myasthenia gravis) |
| Mechanism | Impaired neuromuscular transmission | GO: synaptic transmission, cholinergic; muscle contraction | Final common downstream pathway explaining fatigable weakness and decremental physiology (kaminski2024myastheniagravisthe pages 2-4, kaminski2024myastheniagravisthe pages 1-2) |
| Genetics: susceptibility, not monogenic cause | HLA region risk differs by onset subgroup | HLA-DQA1; HLA-DRB1; HLA-B; HLA-A | HLA is the dominant susceptibility region; onset-specific architecture differs between early- and late-onset disease (topaloudi2022myastheniagravisgenomewide pages 8-12, seldin2015genomewideassociationstudy pages 1-2) |
| Genetics: susceptibility, not monogenic cause | TNFRSF11A risk locus | HGNC: TNFRSF11A | Replicated MG susceptibility locus; not a monogenic cause of acquired adult-onset MG (topaloudi2022myastheniagravisgenomewide pages 8-12, seldin2015genomewideassociationstudy pages 1-2) |
| Genetics: susceptibility, not monogenic cause | PTPN22 risk variant (adult-onset association evidence) | HGNC: PTPN22 | Open Targets associates PTPN22 with adult-onset MG; LOMG GWAS found suggestive rs2476601/R620W association (OpenTargets Search: myasthenia gravis, seldin2015genomewideassociationstudy pages 1-2) |
| Genetics: susceptibility, not monogenic cause | CTLA4, TNIP1, CHRNA1, AGRN | HGNC: CTLA4; TNIP1; CHRNA1; AGRN | These genes shape susceptibility architecture/endotypes; AGRN is biologically notable because it encodes an NMJ organizer, but this is still susceptibility rather than direct Mendelian causation for adult autoimmune MG (topaloudi2022myastheniagravisgenomewide pages 4-8, topaloudi2022myastheniagravisgenomewide pages 8-12) |
| Genetics: causal distinction | Adult-onset autoimmune MG is generally not caused by germline pathogenic variants in AChR-clustering genes | Distinguish from congenital myasthenic syndrome genes: CHRNE, RAPSN, DOK7, MUSK, LRP4, AGRN, COLQ, CHAT | These genes are causal in congenital myasthenic syndromes, not typical adult-onset autoimmune MG; important differential annotation in knowledge bases (OpenTargets Search: myasthenia gravis, wiendl2023guidelineforthe pages 2-3) |
| Environment / triggers | Infection, especially SARS-CoV-2, may trigger onset/exacerbation in some cases | Labels only: viral infection; SARS-CoV-2 infection | Epidemiologic and case-based evidence suggests possible triggering, but causality remains uncertain (antonioni2023theincidenceof pages 1-2) |
| Environment / triggers | Immune checkpoint inhibitor-induced MG | Label: checkpoint inhibitor-induced myasthenia gravis | Recognized distinct severe-onset subgroup in modern oncology practice (kaminski2024myastheniagravisthe pages 1-2) |
| Environment / triggers | Medication-related worsening | Labels only: magnesium; selected antibiotics; immune therapies | Guideline/trial eligibility language warns that concurrent medications can worsen weakness; some therapies can induce or unmask MG (NCT06298552 chunk 1, huang2023myastheniagravisnovel pages 1-3) |
| Diagnostics | Diagnostic framework | History of fluctuating fatigable weakness + autoantibodies and/or electrophysiology and/or pharmacologic testing | Guideline-based confirmation pathway; thymic CT/MRI recommended for all patients to evaluate thymoma (wiendl2023guidelineforthe pages 3-4, wiendl2023guidelineforthe pages 2-3) |
| Diagnostics | Electrodiagnostic confirmation in seronegative disease | Repetitive nerve stimulation; single-fiber EMG | In patients without positive serology, repetitive stimulation and single-fiber testing confirm diagnosis in ~90% (kaminski2024myastheniagravisthe pages 1-2) |
| Biomarkers | Serologic biomarkers | AChR antibody; MuSK antibody; LRP4 antibody; total IgG | Core diagnostic and treatment-stratifying biomarkers; total IgG often tracked in FcRn-therapy trials (kaminski2024myastheniagravisthe pages 1-2, NCT06298552 chunk 1) |
| Omics | Predictive metabolomic signature for steroid response | Histidine; free fatty acid (13:0); γ-cholestenol; guanosine | Discovery study from MGTX biospecimens found an AUC of 0.90 for a responder panel; promising but not routine clinical practice yet (sikorski2023serummetabolomicsof pages 1-2) |
| Standard symptomatic treatment | Pyridostigmine (acetylcholinesterase inhibitor) | NCIT label: Pyridostigmine Bromide; target/class: ACHE inhibitor | First-line symptomatic treatment for most MG; may be less useful or problematic in MuSK-MG (wiendl2023guidelineforthe pages 3-4, vakrakou2023immunotherapiesinmuskpositive pages 1-2) |
| Standard immunotherapy | Corticosteroids | NCIT label: Prednisone / glucocorticoid therapy | Foundational disease-modifying therapy for mild/moderate to active disease (wiendl2023guidelineforthe pages 3-4, wiendl2023guidelineforthe pages 9-10) |
| Steroid-sparing immunotherapy | Azathioprine, MMF, tacrolimus, cyclosporine, methotrexate | NCIT labels; classes: antimetabolite, calcineurin inhibitor, antimetabolite antifolate | Used as conventional long-term immunotherapies; azathioprine is the most established standard steroid-sparing agent in guidelines (wiendl2023guidelineforthe pages 9-10) |
| Rescue / crisis therapy | IVIG, plasmapheresis, immunoadsorption | NCIT labels: Immune Globulin; Plasma Exchange | Recommended for impending/manifest myasthenic crisis and severe exacerbation (wiendl2023guidelineforthe pages 3-4) |
| Surgery | Thymectomy for AChR-positive generalized MG and thymoma-associated MG | NCIT label: Thymectomy | MGTX showed better QMG, lower prednisone exposure, less azathioprine use, and fewer hospitalizations versus prednisone alone in nonthymomatous AChR-positive generalized MG (wolfe2016randomizedtrialof pages 1-3, wiendl2023guidelineforthe pages 2-3) |
| Targeted biologic | Eculizumab / ravulizumab / zilucoplan | Target: C5; class: complement inhibitor | Best mechanistic fit for AChR-positive complement-mediated MG; guideline recommends in highly active AChR-positive generalized MG (wiendl2023guidelineforthe pages 2-3, zhong2024initiationresponsemaximized pages 1-2) |
| Targeted biologic | Efgartigimod / rozanolixizumab | Target: FCGRT/FcRn; class: FcRn modulator/antagonist | FcRn blockade lowers pathogenic IgG broadly; major 2023-2024 therapeutic advance with strong trial activity and approvals (wiendl2023guidelineforthe pages 2-3, habib2024efficacyandsafety pages 1-2, NCT06298552 chunk 1) |
| Targeted biologic | Rituximab | Target: CD20; class: B-cell depletion therapy | Particularly effective in MuSK-MG and considered in seronegative/LRP4-positive/highly active disease (wiendl2023guidelineforthe pages 3-4, vakrakou2023immunotherapiesinmuskpositive pages 1-2) |
| Recent trial signal | Rozanolixizumab in MuSK-positive generalized MG | FcRn inhibitor; MuSK-specific subgroup efficacy | In MycarinG MuSK subgroup, MG-ADL improved versus placebo without serious TEAEs or deaths in the subgroup analysis (habib2024efficacyandsafety pages 1-2) |
| Active clinical development | Inebilizumab | Target: CD19; class: B-cell depletion therapy | Phase 3 MINT includes AChR- and MuSK-antibody-positive adults; reflects continued B-cell-targeted development (NCT04524273 chunk 1) |
| Active clinical development | KYV-101 / mivocabtagene autoleucel | Target/class: anti-CD19 CAR-T cell therapy | Phase 2/3 trial in generalized MG after failure of multiple immunosuppressive/immunomodulatory therapies (NCT06193889 chunk 1) |
| Active clinical development | NMD670 | Class: skeletal muscle ClC-1 chloride channel inhibitor / neuromuscular function enhancer | Phase 2b symptom-focused therapy in AChR/MuSK-positive MG (NCT06414954 chunk 1) |
| Prevention / care considerations | Vaccination review, avoidance of precipitants, medication reconciliation | Labels only: vaccination assessment; trigger avoidance | Guideline recommends checking vaccination history before prolonged immunotherapy; tertiary prevention focuses on avoiding crises and treatment complications (wiendl2023guidelineforthe pages 9-10) |


*Table: This table summarizes knowledge-base-ready entities for adult-onset autoimmune myasthenia gravis, including disease identifiers, phenotypes, anatomy, mechanisms, susceptibility genes versus non-causal CMS genes, and treatment targets/classes. It is designed to support ontology mapping and evidence-linked curation.*

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Primary cause

The proximal cause is loss of immune tolerance followed by production of pathogenic antibodies against NMJ proteins. AChR antibodies are usually complement-fixing IgG1/IgG3; MuSK antibodies are predominantly IgG4 and disrupt protein–protein signaling rather than fixing complement. Thymic germinal-center-like reactions and abnormal thymic epithelial biology are important in many AChR-positive cases. (vakrakou2023immunotherapiesinmuskpositive pages 1-2, kaminski2024myastheniagravisthe pages 2-4, wiendl2023guidelineforthe pages 2-3)

### Genetic susceptibility

**Human genetic evidence.** A 2022 GWAS meta-analysis of 1,401 cases and 3,508 controls confirmed *TNFRSF11A* rs4369774 (OR 1.40, *p*=1.09×10⁻¹³), identified HLA-DQA1 rs34481484 (OR 2.11, *p*=3.72×10⁻⁹), and implicated *CTLA4, AGRN,* and *ISG15*. Estimated SNP heritability was 0.37 overall, 0.64 in early-onset and 0.53 in late-onset disease, supporting substantial but non-Mendelian inherited susceptibility. [Published August 2022; DOI/URL](https://doi.org/10.1136/jmedgenet-2021-107953). (topaloudi2022myastheniagravisgenomewide pages 8-12)

A dedicated LOMG GWAS of 532 AChR-positive cases and 2,128 controls found *TNFRSF11A* rs4574025 (OR 1.42, *p*=3.9×10⁻⁷), protective *ZBTB10* rs6998967 (OR 0.53, *p*=8.9×10⁻¹⁰), and suggestive *PTPN22* R620W/rs2476601 association (OR 1.62, *p*=6.5×10⁻⁶). HLA-DQA1*05:01 showed opposite effects in LOMG (OR 0.54) and early-onset MG (OR 2.82), demonstrating that onset-defined subgroups have different immunogenetic architectures. [Published November 10, 2015; DOI/URL](https://doi.org/10.2119/molmed.2015.00232). (seldin2015genomewideassociationstudy pages 1-2)

**Interpretation:** these are susceptibility alleles, not clinically deterministic pathogenic variants. Penetrance, carrier frequency, anticipation, germline mosaicism, consanguinity, and Mendelian recurrence-risk concepts are therefore not applicable in the way they are for CMS. Open Targets specifically links *PTPN22* to adult-onset MG and identifies therapeutically validated targets including **C5, FCGRT,** and **ACHE**; target association should not be equated with germline causation. (OpenTargets Search: myasthenia gravis)

### Non-genetic risk and trigger factors

- **Age and sex:** early adult AChR-MG has a female predominance of about 3:1 and peaks in the third decade; late-onset disease peaks around the sixth decade and has a male predominance (women:men about 2:3). MuSK-MG also has a female bias and often peaks around the fourth decade. (kaminski2024myastheniagravisthe pages 2-4)
- **Thymoma:** a causal immune-tolerance context in a minority of generalized AChR-MG; neoplastic thymic epithelial cells may inadequately express HLA class II and AIRE-dependent self-antigens. Approximately 10% of generalized AChR-positive MG had thymoma in older European series, while one recent Ferrara cohort reported 17%. (antonioni2023theincidenceof pages 1-2, seldin2015genomewideassociationstudy pages 1-2)
- **Infection:** respiratory and systemic infections commonly precipitate exacerbation or crisis. SARS-CoV-2-associated onset has been reported, but a population study concluded that causal evidence remains inconclusive. (antonioni2023theincidenceof pages 1-2)
- **Iatrogenic triggers:** immune-checkpoint inhibitors can induce rapidly severe MG, sometimes with myositis/myocarditis overlap. Magnesium, aminoglycosides, fluoroquinolones, macrolides, neuromuscular blockers, and selected antiarrhythmics or beta-blockers may worsen transmission; associations vary in strength and do not imply that every exposed patient will deteriorate. (kaminski2024myastheniagravisthe pages 2-4)
- **Pregnancy/postpartum:** disease activity may improve, worsen, or remain stable during pregnancy; postpartum exacerbation is recognized. Maternal IgG may cause transient neonatal MG, but this is passive antibody transfer, not inheritance.

### Protective factors

No validated genetic protective variant or diet prevents MG. The *ZBTB10* signal above is statistically protective but is not an actionable intervention. Smoking, alcohol, exercise, specific diets, or supplements have no established primary-preventive effect. Vaccination, infection control, sleep, graded exercise, and medication review are best viewed as tertiary prevention of exacerbation and treatment complications—not prevention of autoimmune onset. (seldin2015genomewideassociationstudy pages 1-2, wiendl2023guidelineforthe pages 17-19)

### Gene–environment interaction

The prevailing model is polygenic immune susceptibility plus a context that disrupts tolerance—thymic pathology, infection, age-related immune remodeling, or checkpoint blockade—followed by autoreactive T/B-cell expansion. Direct, replicated locus-by-exposure interaction estimates remain sparse; most claimed environmental associations are observational or case-based rather than proven G×E effects.

## 3. Phenotypes

| Phenotype and type | Characteristics, course, frequency | QoL/functional effect | Suggested HPO term |
|---|---|---|---|
| Fluctuating fatigable weakness—symptom/sign | Universal defining feature; worsens with repeated use and may improve with rest; minute-to-minute and week-to-month fluctuation | Limits work, mobility, self-care, and exercise | Muscle weakness; Fatigability |
| Ptosis/diplopia—ocular signs | May be unilateral, bilateral, or asymmetric; AChR-Ab present in about 50% of ocular MG | Driving, reading, computer use and depth perception impaired | Ptosis; Diplopia; Ophthalmoplegia |
| Generalized limb/axial weakness—sign | Variable proximal-predominant weakness; episodic or chronic fluctuating course | Falls, impaired transfers, walking and arm elevation | Generalized muscle weakness; Proximal muscle weakness; Axial muscle weakness |
| Bulbar/facial weakness—sign | Dysarthria, dysphagia, chewing fatigue and facial weakness; especially prominent in MuSK-MG | Aspiration risk, altered diet, communication and social participation | Dysphagia; Dysarthria; Facial weakness; Bulbar palsy |
| Neck weakness—sign | Common in MuSK and more severe generalized disease | Head drop, pain, impaired posture | Neck muscle weakness; Head drop |
| Respiratory weakness/crisis—sign/complication | Severe but minority phenotype; acute or subacute ventilatory failure requiring ICU monitoring and often ventilation | Life-threatening; prolonged rehabilitation may follow | Respiratory insufficiency; Acute respiratory failure |
| Persistent non-myasthenic fatigue—symptom | Can persist despite control of objective weakness; about one-third of patients in pharmacological remission reportedly have fatigue syndrome | Associated with lower QoL and depressive symptoms | Fatigue |

These manifestations and frequencies are supported by the 2024 JCI review and 2023 guideline. The guideline emphasizes that fatigue may occur independently of neuromuscular fatigability and that only cross-sectional evidence supports its association with depression and reduced QoL. (kaminski2024myastheniagravisthe pages 1-2, wiendl2023guidelineforthe pages 17-19)

Recommended outcome annotations are **MG-ADL** (0–24), **QMG** (0–39), **MGC**, **MG-QoL15r** (0–30), MGFA class, and post-intervention status. These measure different biological or patient-centered domains and are not interchangeable. (sikorski2023serummetabolomicsof pages 1-2, NCT06298552 chunk 1)

## 4. Genetic and molecular information

### Causal genes and variants

There is **no single causal gene, canonical pathogenic variant, chromosomal abnormality, or inheritance pattern** for ordinary adult autoimmune MG. Accordingly:

- ACMG pathogenic/likely pathogenic/VUS classification, somatic-versus-germline status, population allele frequency, carrier frequency, karyotype, FISH, CMA, repeat-expansion, mitochondrial, WES, and WGS testing are **not routine MG diagnostics**.
- If onset was congenital/childhood, there is a family history, fixed weakness, dysmorphism, episodic apnea, or antibody/electrophysiologic findings are atypical, evaluate CMS genes such as *CHRNE, CHRNA1, CHRNB1, CHRND, RAPSN, DOK7, MUSK, LRP4, AGRN, COLQ, CHAT, GFPT1,* and *SCN4A*. Those variants cause genetic myasthenic syndromes, not acquired autoimmune MG. (OpenTargets Search: myasthenia gravis, wiendl2023guidelineforthe pages 3-4)

### Susceptibility and modifier candidates

*HLA-DRB1, HLA-DQA1, HLA-B, HLA-A, TNFRSF11A, PTPN22, CTLA4, TNIP1, ZBTB10, AGRN,* and *ISG15* are susceptibility candidates. No modifier gene has sufficient evidence for routine severity prediction. Genetic architecture differs by age, sex, antibody status, and thymic pathology. (topaloudi2022myastheniagravisgenomewide pages 4-8, topaloudi2022myastheniagravisgenomewide pages 8-12, seldin2015genomewideassociationstudy pages 1-2)

### Epigenetics and chromosomal changes

Altered miRNA expression, DNA methylation, and lymphocyte/thymic transcriptional programs have been described, but no epigenetic mark is validated for diagnosis or treatment selection. Large chromosomal abnormalities are not characteristic. Thymoma has tumor genomic alterations, but these belong to the neoplasm and are not defining germline lesions of MG.

## 5. Environmental information

No toxin, radiation exposure, pollution source, occupation, diet, smoking pattern, alcohol exposure, or exercise behavior has been established as a necessary or sufficient cause. The most actionable environmental information concerns **exacerbation**:

1. infection, fever, surgery, sleep deprivation and major physiological stress can increase weakness;
2. excessive heat may worsen transmission transiently;
3. medications that impair presynaptic release, postsynaptic responsiveness, or respiratory reserve require review;
4. immune-checkpoint blockade can induce a distinct, rapidly severe autoimmune phenotype;
5. evidence linking SARS-CoV-2 infection or vaccination to new-onset MG remains insufficient for causal population-level inference. In Ferrara, incidence was 2.7/100,000/year in 2008–2018 versus 2.1/100,000 during 2019–2022, a non-significant reduction rather than an increase. [Published December 30, 2023; DOI/URL](https://doi.org/10.3390/jcm13010236). (antonioni2023theincidenceof pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream:** polygenic susceptibility/thymic abnormality or acquired trigger → defective central/peripheral tolerance → autoreactive CD4 T-cell help → B-cell, plasmablast and plasma-cell expansion → pathogenic IgG production.

**Endotype-specific effector stage:**

- **AChR-MG:** IgG1/IgG3 binds clustered nicotinic AChR → classical complement activation and C5 cleavage → C5b-9 membrane-attack-complex injury; antibody cross-linking also accelerates receptor endocytosis (“antigenic modulation”), while a subset directly blocks acetylcholine binding. (kaminski2024myastheniagravisthe pages 2-4)
- **MuSK-MG:** predominantly functionally monovalent IgG4 blocks LRP4–MuSK interaction → impaired MuSK phosphorylation and rapsyn-dependent AChR clustering. Because IgG4 does not efficiently fix complement, C5 inhibitors are mechanistically inappropriate for this endotype. The 2023 review states that IgG4 antibodies exert pathogenicity “**via interfering with the interaction between their targets and binding partners**.” [Published July 2023; DOI/URL](https://doi.org/10.3389/fimmu.2023.1212757). (vakrakou2023immunotherapiesinmuskpositive pages 1-2)
- **LRP4-MG:** antibodies interfere with agrin–LRP4–MuSK signaling; complement contribution is less clearly defined.

**Downstream:** fewer functional AChRs, damaged junctional folds and reduced sodium-channel density → smaller end-plate potentials → repeated activity lowers the end-plate potential below action-potential threshold → progressive failure of muscle-fiber recruitment → fatigable weakness, dysphagia, diplopia, or ventilatory failure. (kaminski2024myastheniagravisthe pages 2-4)

### Relevant ontology suggestions

- **GO biological process:** complement activation; membrane attack complex assembly; receptor-mediated endocytosis; regulation of acetylcholine-receptor clustering; cholinergic synaptic transmission; skeletal-muscle contraction; B-cell activation; T-cell activation; immunoglobulin production.
- **GO cellular component:** neuromuscular junction; postsynaptic membrane; acetylcholine-gated channel complex; membrane attack complex; immunological synapse.
- **Cell Ontology:** B cell, memory B cell, plasmablast, plasma cell, CD4-positive alpha-beta T cell, regulatory T cell, thymic epithelial cell, skeletal-muscle fiber, alpha motor neuron.

### Molecular profiling and advanced technologies

- **Metabolomics/lipidomics—human exploratory:** an MGTX-serum study found higher phospholipids associated with treatment response. Histidine, free fatty acid 13:0, γ-cholestenol and guanosine predicted a strict corticosteroid-response phenotype with AUC 0.90. The authors stress that the panel “**can now undergo validation**”; it is not a clinical biomarker. [Published October 10, 2023; DOI/URL](https://doi.org/10.1371/journal.pone.0287654). (sikorski2023serummetabolomicsof pages 1-2)
- **Single-cell/spatial studies—human research:** thymic and peripheral immune-cell studies identify heterogeneous autoreactive B/T-cell states and germinal-center niches. They refine endotyping but have no approved diagnostic use. (kaminski2024myastheniagravisthe pages 10-10, kaminski2024myastheniagravisthe pages 10-11)
- **Proteomics/transcriptomics:** candidate cytokine, chemokine, complement and B-cell signatures are reported, but inter-cohort validation is incomplete.
- **Functional platforms—in vitro:** cell-based antibody assays and human stem-cell-derived NMJs reproduce native antigen conformation and permit functional/pathogenicity testing and drug screening. (kaminski2024myastheniagravisthe pages 1-2)
- **Spatial transcriptomics, CRISPR screens, routine liquid biopsy:** investigational or not established for adult MG.

## 7. Anatomical structures affected

- **Primary organ/system:** peripheral neuromuscular system; voluntary skeletal muscle is functionally denervated at the NMJ despite structurally intact motor axons.
- **Primary site:** postsynaptic motor end plate/neuromuscular junction—suggested UBERON term labels: neuromuscular junction, skeletal muscle organ, extraocular muscle, diaphragm, pharyngeal muscle and laryngeal muscle.
- **Secondary organ:** thymus—hyperplasia or thymoma in relevant AChR-positive subtypes.
- **Respiratory system:** diaphragm and accessory respiratory muscles are secondarily affected during severe disease; lung parenchyma is not the primary target.
- **Subcellular compartments:** postsynaptic membrane, junctional folds, AChR complex, MuSK–LRP4 signaling complex, and complement membrane-attack complex.
- **Localization/lateralization:** ocular findings are often asymmetric and can alternate; generalized weakness is usually bilateral but not necessarily symmetric. (kaminski2024myastheniagravisthe pages 2-4, kaminski2024myastheniagravisthe pages 1-2)

## 8. Temporal development and natural history

Onset may be insidious, subacute, or—especially after checkpoint inhibitors—rapid. Early adult AChR disease peaks in young women; late-onset disease increasingly affects older men, with the highest recent Ferrara incidence in people over 70. Ocular disease is often operationally classified as persistent ocular MG if it has not generalized for at least two years. (antonioni2023theincidenceof pages 1-2, kaminski2024myastheniagravisthe pages 2-4)

The course is chronic and fluctuating, with exacerbations, treatment-induced remission, pharmacologic remission, minimal manifestations, or persistent active/refractory disease. A 2024 review estimated relapse in 18%–34% and nonresponse to traditional immunosuppressants in about 10%, although definitions and cohorts vary. (zhong2024initiationresponsemaximized pages 1-2)

The greatest risk of ocular-to-generalized conversion is early in the disease course; early disease control and thymectomy, when indicated, represent important intervention windows. Abrupt withdrawal of immunotherapy can cause recurrence or crisis. Spontaneous permanent remission occurs but cannot be predicted reliably; most patients require prolonged monitoring and many require long-term immunotherapy. (wiendl2023guidelineforthe pages 3-4, wiendl2023guidelineforthe pages 9-10)

## 9. Inheritance, epidemiology, and population

### Epidemiology

A meta-analysis cited in the Ferrara population study estimated prevalence at **7.7/100,000** and incidence at **0.5/100,000 person-years**; recent annual incidence estimates commonly range from **0.3 to 3.0/100,000**. A broader 2023 review estimated approximately **700,000 affected worldwide**, median prevalence around **10/100,000**, and regional incidence ranging from about 0.4/100,000 in Norway to 2.1/100,000 in Italy and Taiwan. Differences reflect age structure, ascertainment, diagnostic access and case definitions. (huang2023myastheniagravisnovel pages 1-3, antonioni2023theincidenceof pages 1-2)

Ferrara’s complete-enumeration study identified 106 incident cases in 2008–2018 (**2.7/100,000/year**) and 29 in 2019–2022 (**2.1/100,000/year**), with rising late-onset and declining early-onset disease. (antonioni2023theincidenceof pages 1-2)

### Demographics and inheritance

- Early-onset AChR-MG: women:men approximately 3:1, peak third decade.
- LOMG: male predominance, peak sixth decade and increasing incidence among those over 70.
- MuSK-MG: female-biased, often younger/middle adult onset, bulbar-predominant.
- Thymoma MG: approximately equal sex ratio or slight male bias, peak near fifth decade. (kaminski2024myastheniagravisthe pages 2-4)

Inheritance is **multifactorial/polygenic with low absolute familial recurrence**, variable expression, and incomplete/age-dependent susceptibility—not autosomal dominant, recessive, X-linked, or mitochondrial. Anticipation, carrier screening, founder-mutation screening, and consanguinity effects are not established. Geographic differences in antibody and thymoma distributions occur, but variant-specific geographic prediction is not clinically mature.

## 10. Diagnostics

### Clinical and laboratory workflow

1. Identify fluctuating, fatigable ocular, bulbar, limb, axial, or respiratory weakness with preserved sensation and usually normal reflexes.
2. Test serum **AChR binding antibodies**; where appropriate add blocking/modulating assays or a clustered-AChR cell-based assay.
3. If AChR-negative, test **MuSK-Ab**; then consider **LRP4-Ab** and specialized cell-based assays.
4. Perform low-frequency repetitive nerve stimulation (RNS) and/or single-fiber EMG (SFEMG), targeting clinically involved muscles. The 2024 review reports that RNS/SFEMG confirms approximately **90%** of seronegative clinically suspected cases. (kaminski2024myastheniagravisthe pages 1-2)
5. Chest CT or MRI for **every confirmed patient** to evaluate thymoma. (wiendl2023guidelineforthe pages 3-4)
6. Assess respiratory status during bulbar/generalized deterioration using forced vital capacity, negative inspiratory force, oxygenation and blood gases; normal oxygen saturation does not exclude impending ventilatory failure.
7. Use MGFA class, MG-ADL, QMG, MGC and MG-QoL15r longitudinally.

The guideline’s exact summary is: “**The diagnosis of MG is based on the history and physical findings of fatigable and fluctuating muscle weakness**,” confirmed through autoantibodies, electrophysiology and/or pharmacological testing. [Published 2023; DOI/URL](https://doi.org/10.1177/17562864231213240). (wiendl2023guidelineforthe pages 3-4)

### Imaging, biopsy, genetic and omics tests

- CT/MRI evaluates thymoma but does not diagnose junctional transmission failure.
- Muscle biopsy is generally unnecessary; if performed, it may be normal or nonspecific and is mainly used to investigate myopathy.
- WES/WGS/panels are reserved for suspected CMS or alternative genetic neuromuscular disease.
- CMA, karyotype, FISH, mtDNA and repeat-expansion tests have no routine role.
- Transcriptomic, proteomic, metabolomic and epigenomic tests remain research tools. (sikorski2023serummetabolomicsof pages 1-2, wiendl2023guidelineforthe pages 3-4)

### Differential diagnosis

Important mimics include Lambert–Eaton syndrome (proximal/autonomic symptoms, facilitation, often reduced reflexes), botulism (pupillary/autonomic involvement and descending paralysis), CMS, mitochondrial/chronic progressive external ophthalmoplegia, oculopharyngeal muscular dystrophy, inflammatory or checkpoint-inhibitor myositis, thyroid eye disease, brainstem stroke, multiple sclerosis, motor-neuron disease, cranial neuropathy and functional neurological disorder. MuSK-MG can resemble bulbar-onset motor-neuron disease; ICI-associated MG should prompt simultaneous creatine kinase, troponin, ECG and cardiac evaluation because of myositis/myocarditis overlap.

### Screening

There is no population, newborn, carrier, prenatal, or asymptomatic genetic screening program. Targeted evaluation may be appropriate in thymoma, before/after checkpoint blockade when symptoms arise, or in relatives only if the phenotype suggests CMS rather than autoimmune MG.

## 11. Outcome and prognosis

Modern MG is usually treatable, and most patients achieve substantial control, but complete stable remission is less common than improvement or minimal manifestations. Survival approaches the general population in well-managed patients, although older age, respiratory crisis, aspiration, infection, thymoma, severe bulbar disease, and treatment toxicity increase risk. Contemporary literature does not support a single universal 5- or 10-year survival percentage because cohorts differ markedly.

Morbidity includes fluctuating disability, aspiration, crisis, hospitalization, falls, treatment-associated infection/metabolic disease, anxiety/depression, fatigue and impaired employment. Persistent fatigue can occur in approximately one-third of pharmacologically remitted patients and correlates with poorer QoL. (wiendl2023guidelineforthe pages 17-19)

Poorer prognosis is associated with delayed recognition, severe baseline MGFA class, recurrent crisis, thymoma, older age/comorbidity, MuSK bulbar/respiratory predominance, and insufficient treatment response. AChR antibody concentration alone correlates imperfectly with clinical severity because antibody epitope, subclass and effector mechanism vary. (kaminski2024myastheniagravisthe pages 2-4)

## 12. Treatment

### Staged clinical strategy

1. **Symptomatic:** pyridostigmine (ACHE inhibition; NCIt term label: pyridostigmine bromide), adjusted to function and tolerability. MuSK-MG may respond poorly and can worsen with excessive cholinesterase inhibition.
2. **Conventional disease modification:** prednisone/prednisolone, usually with steroid-sparing azathioprine; alternatives include mycophenolate, tacrolimus, cyclosporine or methotrexate. Evidence for some alternatives is mixed, and onset of benefit is delayed. (wiendl2023guidelineforthe pages 9-10)
3. **Endotype-directed therapy:** C5 inhibitors for complement-mediated AChR-positive gMG; FcRn inhibitors for pathogenic-IgG reduction; rituximab particularly for MuSK-MG.
4. **Crisis/severe exacerbation:** ICU-level respiratory/bulbar surveillance, treatment of precipitant, IVIG or plasma exchange/immunoadsorption, with ventilatory and aspiration support. (wiendl2023guidelineforthe pages 3-4)

### Thymectomy

Thymoma requires complete oncologic thymectomy where feasible. For non-thymomatous AChR-positive generalized MG, MGTX randomized 126 adults aged 18–65 with disease under five years. At three years, thymectomy plus prednisone versus prednisone alone reduced time-weighted QMG (**6.15 vs 8.99**), alternate-day prednisone (**44 vs 60 mg**), azathioprine use (**17% vs 48%**) and exacerbation hospitalization (**9% vs 37%**), all *p*<0.001. The abstract concludes: “**Thymectomy improved clinical outcomes over a 3-year period**.” [Published August 11, 2016; PMID 27509100; DOI/URL](https://doi.org/10.1056/NEJMoa1602489). (wolfe2016randomizedtrialof pages 1-3)

Guidelines recommend early thymectomy—ideally within two years and no later than five years after diagnosis—for suitable 18–65-year-old AChR-positive generalized patients. It is not routinely recommended for MuSK-MG. (wiendl2023guidelineforthe pages 3-4, wiendl2023guidelineforthe pages 2-3)

### Targeted therapies and 2023–2024 developments

- **C5 complement inhibition:** eculizumab, ravulizumab, and zilucoplan prevent terminal complement/MAC injury. Their strongest rationale is AChR-positive gMG. Meningococcal vaccination and infection-risk mitigation are mandatory; breakthrough invasive infection remains possible. Zilucoplan received US approval in October 2023. (gu2024efficacyandsafety pages 1-2, kaminski2024myastheniagravisthe pages 2-4)
- **FcRn blockade:** efgartigimod and rozanolixizumab accelerate pathogenic IgG clearance. IV and subcutaneous efgartigimod formulations and rozanolixizumab expanded practical treatment options during 2023–2024. Typical concerns include headache and infection; FcRn blockade lowers total IgG but is not antigen-specific. (zhong2024initiationresponsemaximized pages 1-2, habib2024efficacyandsafety pages 1-2, wiendl2023guidelineforthe pages 2-3)
- **MuSK-MG:** rituximab is often used earlier because conventional therapy and IVIG may be less effective. Plasma exchange is frequently effective. Rozanolixizumab is approved for AChR- or MuSK-antibody-positive gMG in the US. (vakrakou2023immunotherapiesinmuskpositive pages 1-2, habib2024efficacyandsafety pages 1-2)

In the 21-patient MuSK subgroup of phase III MycarinG, day-43 MG-ADL changes were −7.28 with 7 mg/kg, −4.16 with 10 mg/kg and +2.28 with placebo; differences from placebo were −9.56 and −6.45. Treatment-emergent adverse events occurred in 80.0%, 62.5% and 37.5%, respectively, but there were no serious events or deaths. The small subgroup warrants cautious interpretation. [Published 2024; NCT03971422; DOI/URL](https://doi.org/10.1177/17562864241273036). (habib2024efficacyandsafety pages 1-2)

A 2024 network meta-analysis of 21 RCTs, 13 drugs and 1,657 patients ranked batoclimab highest for QMG/MGC, rozanolixizumab highest for MG-ADL, and eculizumab highest for MG-QoL15r; indirect SUCRA rankings should not be interpreted as head-to-head superiority because populations and regimens differed. [Published October 2024; DOI/URL](https://doi.org/10.1186/s12967-024-05751-1). (gu2024efficacyandsafety pages 1-2)

### Current experimental applications

- **Inebilizumab/CD19 depletion:** phase III MINT, NCT04524273, 238 AChR- or MuSK-positive adults, with MG-ADL at week 26 as primary outcome. (NCT04524273 chunk 1)
- **Efgartigimod in AChR-binding-seronegative gMG:** ADAPT SERON, phase III, NCT06298552, 119 participants. (NCT06298552 chunk 1)
- **NMD670:** phase IIb SYNAPSE-MG, NCT06414954, estimated 84 participants; a muscle chloride-channel-directed symptomatic approach assessed over 21 days. (NCT06414954 chunk 1)
- **Anti-CD19 CAR-T:** KYV-101/mivocabtagene autoleucel, phase II/III KYSA-6, NCT06193889, estimated 66 treatment-refractory participants. This is an experimental immune-reset strategy, not established care. (NCT06193889 chunk 1)
- **Antigen-specific/CAAR-T and RNA/gene approaches:** preclinical or early clinical; no approved gene, RNA, stem-cell, or regenerative therapy exists for autoimmune MG. (vakrakou2023immunotherapiesinmuskpositive pages 1-2, keritam2024aclinicalperspective pages 13-13)

### Rehabilitation and supportive care

Use individualized aerobic and resistance exercise below the threshold that provokes prolonged weakness; respiratory, swallowing, speech, occupational and physical therapy are indicated by phenotype. Manage aspiration risk, nutrition, sleep, mood, osteoporosis, infection risk and steroid metabolic toxicity. Mechanical ptosis aids, prisms or occlusion may help refractory ocular symptoms. (wiendl2023guidelineforthe pages 17-19)

No validated CPIC/PharmGKB genotype-guided treatment algorithm exists. TPMT/NUDT15 testing may guide azathioprine safety according to general pharmacogenetic practice, but it predicts metabolism/toxicity rather than MG response.

## 13. Prevention

- **Primary prevention:** none established; MG is not preventable through routine genetic screening, diet or vaccination.
- **Secondary prevention:** no asymptomatic population screening. Prompt recognition of ptosis, diplopia, bulbar fatigue or respiratory symptoms reduces diagnostic delay.
- **Tertiary prevention:** medication reconciliation; infection prevention; completion of indicated vaccines before prolonged immunotherapy; meningococcal vaccination/prophylaxis for C5 blockade; gradual—not abrupt—immunotherapy taper; perioperative planning; crisis education; swallowing and respiratory monitoring. The guideline specifically recommends assessing and completing vaccination history before prolonged immunotherapy. (wiendl2023guidelineforthe pages 9-10)
- **Immunization:** non-live vaccines are generally appropriate, but timing should account for B-cell-depleting treatment and other immunosuppression. Vaccination-associated MG reports do not outweigh the recognized risk of infection-triggered exacerbation at the population level.
- **Counseling:** ordinary autoimmune MG does not justify carrier or prenatal testing. Counsel women about pregnancy, medication safety, postpartum exacerbation and transient neonatal MG risk.

## 14. Natural disease in other species

Naturally occurring acquired autoimmune MG occurs most importantly in **dogs (*Canis lupus familiaris*; NCBI Taxon 9615)** and more rarely **cats (*Felis catus*; Taxon 9685)**. Dogs develop AChR-antibody-associated focal or generalized weakness; megaesophagus with regurgitation and aspiration pneumonia is particularly important and differs from typical human presentation. Thymoma-associated MG occurs in dogs and cats. Some canine breed predispositions are reported, but breed effects vary geographically and are not equivalent to a single orthologous causal mutation.

The same postsynaptic AChR/complement biology and response to anticholinesterase or immunomodulatory treatment make canine disease comparatively informative. However, prominent canine megaesophagus, breed structure, species-specific immune responses and differences in treatment constrain direct extrapolation. Autoimmune MG is not infectious or zoonotic and has no cross-species transmission risk.

## 15. Model organisms and experimental systems

- **Active experimental autoimmune MG (EAMG):** mice, rats and rabbits immunized with purified AChR or AChR peptides develop AChR antibodies, complement-mediated endplate injury, decrement and weakness. This is useful for tolerance, complement and therapeutic studies but compresses the chronic, heterogeneous human disease into an induced response.
- **Passive-transfer EAMG:** transfer of patient or monoclonal AChR/MuSK antibodies into rodents isolates antibody effector mechanisms and permits causal testing. It does not reproduce thymic initiation, long-term T/B-cell evolution or the full human antibody repertoire.
- **MuSK models:** active immunization or passive IgG transfer reproduces impaired AChR clustering and bulbar/generalized weakness; species and IgG-subclass biology can alter complement and Fc effects.
- **Genetic models:** knockout/knock-in disruption of *Musk, Lrp4, Agrn, Rapsn,* or *Dok7* elucidates NMJ development but models CMS/developmental failure more directly than acquired autoimmunity.
- **In vitro human systems:** clustered-AChR cell assays, myotubes, motor-neuron–muscle co-cultures, iPSC-derived NMJs and microfluidic/organoid-like platforms permit patient-IgG testing and therapeutic screening. The 2024 JCI review notes both “**robust animal models since the 1970s**” and newer human stem-cell-derived NMJ platforms. (kaminski2024myastheniagravisthe pages 1-2)

Relevant resources include MGI, IMPC, IMSR/MMRRC/EMMA for mouse strains, RGD for rats, Cellosaurus for cell lines, and GEO/SRA/Single Cell Portal for omics datasets.

## Evidence limitations and expert interpretation

1. Adult-onset MG is an umbrella of biologically distinct endotypes; aggregate prevalence, response and prognosis estimates should not be applied indiscriminately to AChR-, MuSK-, LRP4-, thymoma-, ICI-associated or seronegative disease.
2. Recent network meta-analyses offer useful indirect comparisons but are vulnerable to heterogeneous enrollment, background therapy, outcome timing and antibody subtype. (gu2024efficacyandsafety pages 1-2, zhong2024initiationresponsemaximized pages 1-2)
3. Antibody positivity supports diagnosis but does not alone establish current activity; titer–severity correlation is imperfect. Conversely, negative conventional serology does not exclude MG. (kaminski2024myastheniagravisthe pages 2-4, kaminski2024myastheniagravisthe pages 1-2)
4. Genetics and omics presently support mechanistic stratification and target discovery, not routine prediction of individual onset, prognosis, or drug choice. The promising metabolomic AUC of 0.90 requires external validation. (topaloudi2022myastheniagravisgenomewide pages 8-12, sikorski2023serummetabolomicsof pages 1-2)
5. The authoritative 2023 guideline considers rapid achievement of complete disease control a central goal while emphasizing antibody status, thymic pathology, age, activity and patient-reported outcomes. Precision biologics should complement—not replace—careful diagnosis, crisis prevention, conventional immunotherapy and rehabilitation. (wiendl2023guidelineforthe pages 3-4, wiendl2023guidelineforthe pages 2-3)

References

1. (kaminski2024myastheniagravisthe pages 1-2): Henry J. Kaminski, Patricia Sikorski, S. Isabel Coronel, and Linda L. Kusner. Myasthenia gravis: the future is here. Jun 2024. URL: https://doi.org/10.1172/jci179742, doi:10.1172/jci179742. This article has 134 citations and is from a highest quality peer-reviewed journal.

2. (OpenTargets Search: myasthenia gravis): Open Targets Query (myasthenia gravis, 31 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (wiendl2023guidelineforthe pages 2-3): Heinz Wiendl, Angela Abicht, Andrew Chan, Adela Della Marina, Tim Hagenacker, Khosro Hekmat, Sarah Hoffmann, Hans-Stefan Hoffmann, Sebastian Jander, Christian Keller, Alexander Marx, Arthur Melms, Nico Melzer, Wolfgang Müller-Felber, Marc Pawlitzki, Jens-Carsten Rückert, Ulrike Schara-Schmidt, Christiane Schneider-Gold, Benedikt Schoser, Bettina Schreiner, Michael Schroeter, Bettina Schubert, Jörn-Peter Sieb, Fritz Zimprich, and Andreas Meisel. Guideline for the management of myasthenic syndromes. Therapeutic Advances in Neurological Disorders, Jan 2023. URL: https://doi.org/10.1177/17562864231213240, doi:10.1177/17562864231213240. This article has 204 citations and is from a peer-reviewed journal.

4. (antonioni2023theincidenceof pages 1-2): Annibale Antonioni, Emanuela Maria Raho, Domenico Carlucci, Elisabetta Sette, Riccardo De Gennaro, Jay Guido Capone, Vittorio Govoni, Ilaria Casetta, Maura Pugliatti, and Enrico Granieri. The incidence of myasthenia gravis in the province of ferrara, italy, in the period of 2008–2022: an update on a 40-year observation and the influence of the covid-19 pandemic. Journal of Clinical Medicine, 13:236, Dec 2023. URL: https://doi.org/10.3390/jcm13010236, doi:10.3390/jcm13010236. This article has 6 citations.

5. (kaminski2024myastheniagravisthe pages 2-4): Henry J. Kaminski, Patricia Sikorski, S. Isabel Coronel, and Linda L. Kusner. Myasthenia gravis: the future is here. Jun 2024. URL: https://doi.org/10.1172/jci179742, doi:10.1172/jci179742. This article has 134 citations and is from a highest quality peer-reviewed journal.

6. (wiendl2023guidelineforthe pages 3-4): Heinz Wiendl, Angela Abicht, Andrew Chan, Adela Della Marina, Tim Hagenacker, Khosro Hekmat, Sarah Hoffmann, Hans-Stefan Hoffmann, Sebastian Jander, Christian Keller, Alexander Marx, Arthur Melms, Nico Melzer, Wolfgang Müller-Felber, Marc Pawlitzki, Jens-Carsten Rückert, Ulrike Schara-Schmidt, Christiane Schneider-Gold, Benedikt Schoser, Bettina Schreiner, Michael Schroeter, Bettina Schubert, Jörn-Peter Sieb, Fritz Zimprich, and Andreas Meisel. Guideline for the management of myasthenic syndromes. Therapeutic Advances in Neurological Disorders, Jan 2023. URL: https://doi.org/10.1177/17562864231213240, doi:10.1177/17562864231213240. This article has 204 citations and is from a peer-reviewed journal.

7. (gu2024efficacyandsafety pages 1-2): Jian Gu, Yue Qiao, Rui Huang, and Shuyan Cong. Efficacy and safety of immunosuppressants and monoclonal antibodies in adults with myasthenia gravis: a systematic review and network meta-analysis. Journal of Translational Medicine, Oct 2024. URL: https://doi.org/10.1186/s12967-024-05751-1, doi:10.1186/s12967-024-05751-1. This article has 14 citations and is from a peer-reviewed journal.

8. (vakrakou2023immunotherapiesinmuskpositive pages 1-2): Aigli G. Vakrakou, Eleni Karachaliou, Elisabeth Chroni, Vasiliki Zouvelou, Dimitrios Tzanetakos, Stavroula Salakou, Marianna Papadopoulou, Socrates Tzartos, Konstantinos Voumvourakis, Constantinos Kilidireas, Sotirios Giannopoulos, Georgios Tsivgoulis, and John Tzartos. Immunotherapies in musk-positive myasthenia gravis; an igg4 antibody-mediated disease. Frontiers in Immunology, Jul 2023. URL: https://doi.org/10.3389/fimmu.2023.1212757, doi:10.3389/fimmu.2023.1212757. This article has 54 citations and is from a peer-reviewed journal.

9. (wiendl2023guidelineforthe pages 17-19): Heinz Wiendl, Angela Abicht, Andrew Chan, Adela Della Marina, Tim Hagenacker, Khosro Hekmat, Sarah Hoffmann, Hans-Stefan Hoffmann, Sebastian Jander, Christian Keller, Alexander Marx, Arthur Melms, Nico Melzer, Wolfgang Müller-Felber, Marc Pawlitzki, Jens-Carsten Rückert, Ulrike Schara-Schmidt, Christiane Schneider-Gold, Benedikt Schoser, Bettina Schreiner, Michael Schroeter, Bettina Schubert, Jörn-Peter Sieb, Fritz Zimprich, and Andreas Meisel. Guideline for the management of myasthenic syndromes. Therapeutic Advances in Neurological Disorders, Jan 2023. URL: https://doi.org/10.1177/17562864231213240, doi:10.1177/17562864231213240. This article has 204 citations and is from a peer-reviewed journal.

10. (kaminski2024myastheniagravisthe pages 10-11): Henry J. Kaminski, Patricia Sikorski, S. Isabel Coronel, and Linda L. Kusner. Myasthenia gravis: the future is here. Jun 2024. URL: https://doi.org/10.1172/jci179742, doi:10.1172/jci179742. This article has 134 citations and is from a highest quality peer-reviewed journal.

11. (seldin2015genomewideassociationstudy pages 1-2): Michael F. Seldin, Omar K. Alkhairy, Annette T. Lee, Janine A. Lamb, Jon Sussman, Ritva Pirskanen-Matell, Fredrik Piehl, Jan J. G. M. Verschuuren, Anna Kostera-Pruszczyk, Piotr Szczudlik, David McKee, Angelina H. Maniaol, Hanne F. Harbo, Benedicte A. Lie, Arthur Melms, Henri-Jean Garchon, Nicholas Willcox, Peter K. Gregersen, and Lennart Hammarstrom. Genome-wide association study of late-onset myasthenia gravis: confirmation of tnfrsf11a and identification of zbtb10 and three distinct hla associations. Molecular Medicine, 21:769-781, Oct 2015. URL: https://doi.org/10.2119/molmed.2015.00232, doi:10.2119/molmed.2015.00232. This article has 86 citations and is from a peer-reviewed journal.

12. (topaloudi2022myastheniagravisgenomewide pages 8-12): Apostolia Topaloudi, Zoi Zagoriti, Alyssa Camille Flint, Melanie Belle Martinez, Zhiyu Yang, Fotis Tsetsos, Yiolanda-Panayiota Christou, George Lagoumintzis, Evangelia Yannaki, Eleni Zamba-Papanicolaou, John Tzartos, Xanthippi Tsekmekidou, Kalliopi Kotsa, Efstratios Maltezos, Nikolaos Papanas, Dimitrios Papazoglou, Ploumis Passadakis, Athanasios Roumeliotis, Stefanos Roumeliotis, Marios Theodoridis, Elias Thodis, Stylianos Panagoutsos, John Yovos, John Stamatoyannopoulos, Konstantinos Poulas, Kleopas Kleopa, Socrates Tzartos, Marianthi Georgitsi, and Peristera Paschou. Myasthenia gravis genome-wide association study implicates agrn as a risk locus. Journal of Medical Genetics, 59:801-809, Aug 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107953, doi:10.1136/jmedgenet-2021-107953. This article has 20 citations and is from a domain leading peer-reviewed journal.

13. (topaloudi2022myastheniagravisgenomewide pages 4-8): Apostolia Topaloudi, Zoi Zagoriti, Alyssa Camille Flint, Melanie Belle Martinez, Zhiyu Yang, Fotis Tsetsos, Yiolanda-Panayiota Christou, George Lagoumintzis, Evangelia Yannaki, Eleni Zamba-Papanicolaou, John Tzartos, Xanthippi Tsekmekidou, Kalliopi Kotsa, Efstratios Maltezos, Nikolaos Papanas, Dimitrios Papazoglou, Ploumis Passadakis, Athanasios Roumeliotis, Stefanos Roumeliotis, Marios Theodoridis, Elias Thodis, Stylianos Panagoutsos, John Yovos, John Stamatoyannopoulos, Konstantinos Poulas, Kleopas Kleopa, Socrates Tzartos, Marianthi Georgitsi, and Peristera Paschou. Myasthenia gravis genome-wide association study implicates agrn as a risk locus. Journal of Medical Genetics, 59:801-809, Aug 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107953, doi:10.1136/jmedgenet-2021-107953. This article has 20 citations and is from a domain leading peer-reviewed journal.

14. (NCT06298552 chunk 1):  A Phase 3 Study to Evaluate the Efficacy and Safety of Efgartigimod IV in Patients With Acetylcholine Receptor Binding Antibody Seronegative Generalized Myasthenia Gravis. argenx. 2024. ClinicalTrials.gov Identifier: NCT06298552

15. (huang2023myastheniagravisnovel pages 1-3): Evelyn Jou-Chen Huang, Meng-Huang Wu, Tsung-Jen Wang, Tsung-Jen Huang, Yan-Rong Li, and Ching-Yu Lee. Myasthenia gravis: novel findings and perspectives on traditional to regenerative therapeutic interventions. Aging and Disease, 14:1070-1092, Dec 2023. URL: https://doi.org/10.14336/ad.2022.1215, doi:10.14336/ad.2022.1215. This article has 23 citations and is from a peer-reviewed journal.

16. (sikorski2023serummetabolomicsof pages 1-2): Patricia Sikorski, Yaoxiang Li, Mehar Cheema, Gil I. Wolfe, Linda L. Kusner, Inmaculada Aban, and Henry J. Kaminski. Serum metabolomics of treatment response in myasthenia gravis. PLOS ONE, 18:e0287654, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0287654, doi:10.1371/journal.pone.0287654. This article has 17 citations and is from a peer-reviewed journal.

17. (wiendl2023guidelineforthe pages 9-10): Heinz Wiendl, Angela Abicht, Andrew Chan, Adela Della Marina, Tim Hagenacker, Khosro Hekmat, Sarah Hoffmann, Hans-Stefan Hoffmann, Sebastian Jander, Christian Keller, Alexander Marx, Arthur Melms, Nico Melzer, Wolfgang Müller-Felber, Marc Pawlitzki, Jens-Carsten Rückert, Ulrike Schara-Schmidt, Christiane Schneider-Gold, Benedikt Schoser, Bettina Schreiner, Michael Schroeter, Bettina Schubert, Jörn-Peter Sieb, Fritz Zimprich, and Andreas Meisel. Guideline for the management of myasthenic syndromes. Therapeutic Advances in Neurological Disorders, Jan 2023. URL: https://doi.org/10.1177/17562864231213240, doi:10.1177/17562864231213240. This article has 204 citations and is from a peer-reviewed journal.

18. (wolfe2016randomizedtrialof pages 1-3): Gil I. Wolfe, Henry J. Kaminski, Inmaculada B. Aban, Greg Minisman, Hui-Chien Kuo, Alexander Marx, Philipp Ströbel, Claudio Mazia, Joel Oger, J. Gabriel Cea, Jeannine M. Heckmann, Amelia Evoli, Wilfred Nix, Emma Ciafaloni, Giovanni Antonini, Rawiphan Witoonpanich, John O. King, Said R. Beydoun, Colin H. Chalk, Alexandru C. Barboi, Anthony A. Amato, Aziz I. Shaibani, Bashar Katirji, Bryan R.F. Lecky, Camilla Buckley, Angela Vincent, Elza Dias-Tosta, Hiroaki Yoshikawa, Márcia Waddington-Cruz, Michael T. Pulley, Michael H. Rivner, Anna Kostera-Pruszczyk, Robert M. Pascuzzi, Carlayne E. Jackson, Guillermo S. Garcia Ramos, Jan J.G.M. Verschuuren, Janice M. Massey, John T. Kissel, Lineu C. Werneck, Michael Benatar, Richard J. Barohn, Rup Tandan, Tahseen Mozaffar, Robin Conwit, Joanne Odenkirchen, Joshua R. Sonett, Alfred Jaretzki, John Newsom-Davis, and Gary R. Cutter. Randomized trial of thymectomy in myasthenia gravis. New England Journal of Medicine, 375:511-522, Aug 2016. URL: https://doi.org/10.1056/nejmoa1602489, doi:10.1056/nejmoa1602489. This article has 789 citations and is from a highest quality peer-reviewed journal.

19. (zhong2024initiationresponsemaximized pages 1-2): Huahua Zhong, Zhijun Li, Xicheng Li, Zongtai Wu, Chong Yan, Sushan Luo, and Chongbo Zhao. Initiation response, maximized therapeutic efficacy, and post-treatment effects of biological targeted therapies in myasthenia gravis: a systematic review and network meta-analysis. Frontiers in Neurology, Oct 2024. URL: https://doi.org/10.3389/fneur.2024.1479685, doi:10.3389/fneur.2024.1479685. This article has 13 citations and is from a peer-reviewed journal.

20. (habib2024efficacyandsafety pages 1-2): Ali A. Habib, Sabrina Sacconi, Giovanni Antonini, Elena Cortés-Vicente, Julian Grosskreutz, Zabeen K. Mahuwala, Renato Mantegazza, Robert M. Pascuzzi, Kimiaki Utsugisawa, John Vissing, Tuan Vu, Heinz Wiendl, Marion Boehnlein, Bernhard Greve, Franz Woltering, and Vera Bril. Efficacy and safety of rozanolixizumab in patients with muscle-specific tyrosine kinase autoantibody-positive generalised myasthenia gravis: a subgroup analysis of the randomised, double-blind, placebo-controlled, adaptive phase iii mycaring study. Therapeutic Advances in Neurological Disorders, Jan 2024. URL: https://doi.org/10.1177/17562864241273036, doi:10.1177/17562864241273036. This article has 12 citations and is from a peer-reviewed journal.

21. (NCT04524273 chunk 1):  Myasthenia Gravis Inebilizumab Trial. Amgen. 2020. ClinicalTrials.gov Identifier: NCT04524273

22. (NCT06193889 chunk 1):  KYSA-6: A Study of Anti-CD19 Chimeric Antigen Receptor T-Cell Therapy, in Patients With Generalized Myasthenia Gravis. Kyverna Therapeutics. 2024. ClinicalTrials.gov Identifier: NCT06193889

23. (NCT06414954 chunk 1):  Safety and Efficacy of 3 Dose Levels of NMD670 in Adult Patients With Myasthenia Gravis. NMD Pharma A/S. 2024. ClinicalTrials.gov Identifier: NCT06414954

24. (kaminski2024myastheniagravisthe pages 10-10): Henry J. Kaminski, Patricia Sikorski, S. Isabel Coronel, and Linda L. Kusner. Myasthenia gravis: the future is here. Jun 2024. URL: https://doi.org/10.1172/jci179742, doi:10.1172/jci179742. This article has 134 citations and is from a highest quality peer-reviewed journal.

25. (keritam2024aclinicalperspective pages 13-13): Omar Keritam, Angela Vincent, Fritz Zimprich, and Hakan Cetin. A clinical perspective on muscle specific kinase antibody positive myasthenia gravis. Frontiers in Immunology, Dec 2024. URL: https://doi.org/10.3389/fimmu.2024.1502480, doi:10.3389/fimmu.2024.1502480. This article has 15 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Adult-Onset_Myasthenia_Gravis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.3390/jcm13010236` (5 mentions) - The Incidence of Myasthenia Gravis in the Province of Ferrara, Italy, in the Period of 2008–2022: An Update on a 40-Year Observation and the Influence of the COVID-19 Pandemic
  - shared terms: clinical

Weighed against this report's own most characteristic terms: `disease`, `clinical`, `genetic`, `treatment`, `gene`, `achr`, `autoimmune`, `guideline`, `generalized`, `risk`, `musk`, `respiratory`, `weakness`, `thymic`, `causal`, `antibody`, `patient`, `effect`, `complement`, `muscle`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.