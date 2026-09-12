---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T13:46:17.024577'
end_time: '2026-08-27T13:55:08.037327'
duration_seconds: 531.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mastocytosis
  mondo_id: MONDO:0007950
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mastocytosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mastocytosis
- **MONDO ID:** MONDO:0007950 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Mastocytosis** covering all of the
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
- **Disease Name:** Mastocytosis
- **MONDO ID:** MONDO:0007950 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Mastocytosis** covering all of the
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


# Mastocytosis: comprehensive disease-characteristics report

**Scope.** This report treats mastocytosis as the disease family represented by **MONDO:0007950**, not as synonymous with mast-cell activation syndrome (MCAS). Evidence is principally aggregated disease-level evidence from classifications, registries, cohorts, trials, and experimental models—not individual-level EHR data. Dates and URLs refer to the cited publications. Where a PMID was not verified in the retrieved record, the DOI is given rather than risking an incorrect PMID.

## Executive summary

Mastocytosis comprises clonal mast-cell neoplasms ranging from usually regressing childhood cutaneous disease to adult systemic mastocytosis (SM) and rapidly lethal mast-cell leukemia. The central lesion is usually a somatic activating **KIT** mutation, especially **KIT c.2447A>T (p.Asp816Val; D816V)** in adult SM. Constitutive KIT signaling promotes mast-cell survival and expansion; released histamine, tryptase, prostaglandins, leukotrienes, and cytokines produce episodic symptoms, while direct tissue infiltration causes cytopenias, organomegaly, malabsorption, osteolysis, and organ failure. Contemporary practice integrates morphology, aberrant mast-cell immunophenotype, serum tryptase, and highly sensitive KIT testing. The leading recent therapeutic advance is selective KIT inhibition with avapritinib; next-generation agents include bezuclastinib and elenestinib. (tremblay2024managementofadvanced pages 1-2, wang2023theinternationalconsensus pages 11-11)

| Domain | Core finding | Quantitative/current evidence | Suggested ontology terms |
|---|---|---|---|
| Disease definition/classification | Mastocytosis is a clonal mast-cell neoplasm with skin-limited and systemic forms; contemporary frameworks recognize CM, SM subtypes, and mast cell sarcoma. WHO 5th edition/ICC differ slightly in subclassification, but both retain indolent vs advanced disease concepts. (arock2018preclinicalhumanmodels pages 1-6, wang2023theinternationalconsensus pages 11-11) | WHO/ICC-recognized entities include CM, BMM, ISM, SSM, ASM, SM-AHN, MCL, mast cell sarcoma; ICC 2023 emphasizes refined morphology/molecular criteria (Wang 2023, DOI:10.1002/ajh.26966). (wang2023theinternationalconsensus pages 11-11) | MONDO:0007950 mastocytosis; MONDO:0019023 cutaneous mastocytosis; MONDO:0016586 systemic mastocytosis; NCIT: Systemic Mastocytosis; HPO: HP:0002444 Mast cell proliferation |
| Core driver genetics | KIT is the dominant disease gene; KIT p.D816V is the major activating mutation in adult SM and causes ligand-independent signaling and mast-cell accumulation/survival. (tremblay2024managementofadvanced pages 1-2, arock2018preclinicalhumanmodels pages 1-6, nedoszytko2021clinicalimpactof pages 1-2) | >90% of patients with mastocytosis harbor a somatic KIT mutation by sensitive testing; KIT p.D816V is present in >90–95% of adult SM in recent reviews. Adult hotspot: exon 17/codon 816. (tremblay2024managementofadvanced pages 1-2, nedoszytko2021clinicalimpactof pages 1-2) | HGNC:6342 KIT; SO:0001583 missense_variant; GO:0004714 transmembrane receptor protein tyrosine kinase activity; GO:0007169 transmembrane receptor protein tyrosine kinase signaling pathway |
| Additional somatic genetics | Advanced SM commonly carries additional myeloid-neoplasm mutations that modify phenotype and prognosis, especially SRSF2/ASXL1/RUNX1 (“S/A/R”) and also TET2, RUNX1, CBL, JAK2, RAS. (arock2018preclinicalhumanmodels pages 22-24, nedoszytko2021clinicalimpactof pages 1-2) | S/A/R high-risk profile is enriched in advanced disease and worse outcomes; male patients had S/A/R-type aberrations in 63% vs 40% of females in ECNM registry analysis. (c.2021cytogeneticandmolecular pages 12-12) | HGNC:11824 TET2; HGNC:10770 SRSF2; HGNC:18357 ASXL1; HGNC:10471 RUNX1; NCIT: Somatic Mutation; GO:0000398 mRNA splicing |
| Germline/modifier genetics | Inherited modifiers exist but are not established primary causes for most cases; hereditary alpha-tryptasemia (TPSAB1 copy gain) is enriched in SM and may amplify mediator-related severity/anaphylaxis risk. (nedoszytko2021clinicalimpactof pages 1-2) | HαT occurs in ~3–6% of general Western populations vs up to 17% of SM patients. Reported germline associations also include IL13, IL6, IL6R, IL31, IL4R, TLR loci. (nedoszytko2021clinicalimpactof pages 1-2) | HGNC:12019 TPSAB1; HP:0040283 Elevated circulating tryptase concentration; NCIT: Germline Mutation |
| Diagnostic criteria | SM diagnosis requires tissue morphology plus minor criteria; current ICC major criterion is dense multifocal mast-cell infiltrates in extracutaneous tissue, with minor criteria spanning atypical morphology, aberrant immunophenotype, KIT activation, and serum tryptase elevation. (wang2023theinternationalconsensus pages 11-11) | Major: multifocal dense infiltrates of ≥15 mast cells in marrow/other extracutaneous organ. Minor: >25% atypical/spindle mast cells; CD25/CD2 and/or CD30 aberrant expression; KIT D816V or other activating KIT mutation; persistent serum tryptase >20 ng/mL. Diagnosis: major + 1 minor, or 3 minor. (wang2023theinternationalconsensus pages 11-11) | NCIT: Bone Marrow Biopsy; LOINC/biomarker: serum tryptase; CL:0000097 mast cell; HP:0033365 Abnormal mast cell morphology |
| B- and C-findings / staging | Disease burden and organ damage stratify SM into indolent/smoldering vs advanced forms. B-findings reflect high burden without overt dysfunction; C-findings define organ damage and need for cytoreduction. (arock2018preclinicalhumanmodels pages 42-44, tremblay2024managementofadvanced pages 1-2) | SSM: ≥2 B-findings; ASM/MCL: C-findings present. Examples include marrow mast-cell burden ≥30% or tryptase ≥200 ng/mL (B); cytopenias, malabsorption, hepatic dysfunction/ascites, hypersplenism, osteolysis/pathologic fractures (C). (arock2018preclinicalhumanmodels pages 42-44) | NCIT: Organ Dysfunction; HPO: HP:0002242 Hepatomegaly; HP:0001744 Splenomegaly; HP:0003277 Osteolysis |
| Phenotypes: mediator-related | Symptoms arise from mast-cell degranulation and mediator release, often fluctuating/episodic and disproportionate to mast-cell burden. (tremblay2024managementofadvanced pages 1-2) | Common manifestations across reviews include pruritus, flushing, abdominal cramping/diarrhea, anaphylaxis, hypotension; pediatric CM review identifies pruritus as most common and anaphylaxis rare but increased with extensive lesions/high tryptase. () | HPO: HP:0000989 Pruritus; HP:0031284 Flushing; HP:0002014 Diarrhea; HP:0100845 Anaphylaxis; GO:0043303 mast cell degranulation |
| Phenotypes: infiltration-related | Tissue infiltration causes organomegaly, marrow dysfunction, skeletal disease, GI malabsorption, and aggressive-organ-damage features. (tremblay2024managementofadvanced pages 1-2, arock2018preclinicalhumanmodels pages 42-44) | Hepatomegaly/splenomegaly occur in ~40% of AdvSM patients in 2024 review; osteoporosis/fragility fractures were present in 35% of an adult regional cohort, including young patients. (tremblay2024managementofadvanced pages 1-2, c.2021cytogeneticandmolecular pages 12-12) | HPO: HP:0002240 Hepatic insufficiency; HP:0001744 Splenomegaly; HP:0000939 Osteoporosis; HP:0002757 Pathologic fracture |
| Epidemiology | Mastocytosis is rare but likely underdiagnosed; recent registry work suggests higher incidence/prevalence than older estimates. (tremblay2024managementofadvanced pages 1-2, c.2021cytogeneticandmolecular pages 12-12) | Sweden 2024: annual incidence 1.56/100,000 (95% CI 1.29–1.87), prevalence 23.9/100,000 (95% CI 22.8–25.0). Verona/Veneto cohort: adult SM prevalence 10.2/100,000 in Veneto and 17.2/100,000 in Verona province; mean incidence 1.09/100,000/year. (c.2021cytogeneticandmolecular pages 12-12) | NCIT: Incidence; NCIT: Prevalence; MONDO:0007950 |
| Demographics/sex effects | Overall sex distribution is near-balanced, but advanced forms—especially SM-AHN—show male predominance and worse outcomes in males. (c.2021cytogeneticandmolecular pages 12-12) | In ECNM registry analysis of 3403 patients, 55.3% were female overall, but SM-AHN was 70% male; organomegaly was 23% in males vs 13% females, skin involvement 71% vs 86%, respectively. (c.2021cytogeneticandmolecular pages 12-12) | PATO: male/female biological sex; HPO: HP:0001744 Splenomegaly; HP:0000951 Skin lesion |
| Pediatric disease | Pediatric mastocytosis is usually cutaneous, often begins in infancy/early childhood, and frequently regresses around puberty; systemic disease is uncommon but follow-up is required. () | Reviews state CM is the commonest childhood form; most children regress spontaneously around puberty, whereas diffuse CM is rarer and more severe. Advanced SM in children is described as sporadic. () | MONDO:0019023 cutaneous mastocytosis; HPO: HP:0011462 Childhood onset; HP:0031284 Flushing; HP:0001009 Macule |
| Pediatric mutation spectrum | Children show a broader KIT spectrum than adults, with lesional KIT mutations that often involve non-D816V sites, including extracellular-domain variants; peripheral blood D816V may be negative despite skin disease. (arock2018preclinicalhumanmodels pages 33-42) | Reported pediatric variants include KIT Del419, ITD501-502, ITD502-503, K509I; lesional D816V can occur, but peripheral blood ASqPCR may be negative in CM. (arock2018preclinicalhumanmodels pages 33-42) | HGNC:6342 KIT; SO:0000667 insertion; SO:1000032 deletion; NCIT: Skin Biopsy |
| Molecular pathophysiology | Upstream driver: constitutive KIT activation. Downstream pathways include STAT5, PI3K/AKT, mTOR, and other kinase networks, promoting survival, proliferation, trafficking, and mediator release. (arock2018preclinicalhumanmodels pages 22-24, arock2018preclinicalhumanmodels pages 1-6) | Reviews synthesize KIT-dependent and KIT-independent signaling in advanced disease; in vitro KIT D816V mast-cell lines support pharmacologic suppression of proliferation and signaling. (arock2018preclinicalhumanmodels pages 22-24, arock2018preclinicalhumanmodels pages 42-44) | GO:0007169 receptor tyrosine kinase signaling; GO:0038128 ERBB/RTK downstream signaling analog; GO:0042127 regulation of cell population proliferation; CL:0000097 mast cell |
| Prognosis | Prognosis spans near-normal survival in indolent disease to very poor survival in leukemic disease; molecular burden and subtype matter. (tremblay2024managementofadvanced pages 2-4, tremblay2024managementofadvanced pages 1-2) | Median OS by subtype in 2024 review: ISM 198 months, SSM 52 months, ASM 41 months, SM-AHN 24 months, MCL 2 months. KIT D816V allele burden reduction ≥25% has been associated with improved OS. (tremblay2024managementofadvanced pages 2-4) | NCIT: Overall Survival; NCIT: Prognostic Factor; NCIT: Mutation Burden |
| Prognostic scoring | Modern risk tools integrate clinical and molecular features rather than morphology alone. (c.2021cytogeneticandmolecular pages 12-12) | IPSM and mutation-adjusted systems such as MARS are referenced as contemporary tools for risk stratification in SM, especially advanced disease. (c.2021cytogeneticandmolecular pages 12-12) | NCIT: Risk Assessment; NCIT: Prognostic Score |
| Symptom-directed treatment | Indolent disease management is largely supportive and anti-mediator focused; trigger avoidance and anaphylaxis preparedness are central. () | Common measures: H1/H2 antihistamines, cromolyn, leukotriene-directed approaches, epinephrine autoinjector for severe reactions; pediatric reviews emphasize avoidance of triggers and ready access to adrenaline. () | NCIT: Histamine H1 Receptor Antagonist; NCIT: Histamine H2 Receptor Antagonist; CHEBI: histamine; NCIT: Epinephrine |
| Midostaurin | Midostaurin is a multikinase inhibitor active against KIT D816V and established for AdvSM. (arock2018preclinicalhumanmodels pages 42-44, c.2021cytogeneticandmolecular pages 12-12) | Preclinical IC50 against mast-cell lines ~0.05–0.3 µM; pivotal clinical study showed meaningful responses in AdvSM, with median OS reported around 20.7 months in one summarized study context. (arock2018preclinicalhumanmodels pages 42-44, c.2021cytogeneticandmolecular pages 12-12) | NCIT: Midostaurin; NCIT: Protein Kinase Inhibitor Therapy |
| Avapritinib | Avapritinib is a selective KIT D816V inhibitor and major recent advance for AdvSM, with molecular and pathologic responses. (tremblay2024managementofadvanced pages 2-4, tremblay2024managementofadvanced pages 10-11) | 2024 review notes improved quality and quantity of life with avapritinib; adverse events summarized as hair color changes 34%, thrombocytopenia 22%, transaminase increases 22%, neutropenia 19%, taste disorder 19%, without reported cognitive or bleeding events in the cited dataset. (tremblay2024managementofadvanced pages 10-11) | NCIT: Avapritinib; NCIT: Tyrosine Kinase Inhibitor Therapy |
| Emerging targeted therapy | Next-generation selective KIT inhibitors are in active development to improve tolerability and sequencing after/around avapritinib. (tremblay2024managementofadvanced pages 2-4, tremblay2024managementofadvanced pages 10-11) | Bezuclastinib/CGT9486 is in phase 2 SUMMIT for indolent/smoldering SM (NCT05186753; 237 planned participants in retrieved trial record). Elenestinib is highlighted in 2024 therapeutic reviews as an emerging agent. (tremblay2024managementofadvanced pages 2-4) | NCIT: Investigational Agent; NCIT: Clinical Trial; NCIT: KIT Inhibitor |
| Transplant / advanced interventions | Allogeneic hematopoietic stem-cell transplantation remains the only potentially curative option for selected very high-risk AdvSM/MCL, but is restricted to fit patients and specialized centers. (tremblay2024managementofadvanced pages 2-4, tremblay2024managementofadvanced pages 1-2) | Persistently poor outcomes in high-risk groups, especially MCL, sustain transplant consideration despite targeted-therapy advances. (tremblay2024managementofadvanced pages 2-4) | NCIT: Allogeneic Hematopoietic Stem Cell Transplantation |
| Diagnostics in practice | Bone marrow evaluation, serum tryptase, flow/IHC immunophenotyping, and highly sensitive KIT testing are the current diagnostic backbone; sensitive assays outperform routine NGS for low-VAF KIT variants. (wang2023theinternationalconsensus pages 11-11) | 2024 KIT-detection review states KIT variants may be “well below the sensitivity of common NGS methods used in routine diagnostic panels,” supporting allele-specific/qPCR-type approaches for diagnosis/follow-up. () | NCIT: Polymerase Chain Reaction; NCIT: Next Generation Sequencing; NCIT: Flow Cytometry; LOINC: serum tryptase |
| Animal/natural disease | Comparative mast-cell neoplasia occurs in dogs, cats, and other mammals; KIT mutations are common across species, but prognostic correlates differ from human mastocytosis. (arock2018preclinicalhumanmodels pages 33-42) | Review notes KIT mutations are common in dog, cat, and human mast-cell neoplasia; in dogs certain KIT mutations correlate with more malignant/lethal disease, whereas in feline and human disease KIT is more useful diagnostically/therapeutically than prognostically. (arock2018preclinicalhumanmodels pages 33-42) | NCBITaxon:9606 human; NCBITaxon:9615 dog; NCBITaxon:9685 cat; OMIA/VBO terms as applicable |
| Experimental models | Human mast-cell lines and xenografts are the principal research models; ROSA KIT D816V and HMC-1 are especially useful for pathway and drug studies. (arock2018preclinicalhumanmodels pages 33-42, arock2018preclinicalhumanmodels pages 1-6) | Available human lines include HMC-1, LAD1/2, LUVA, ROSA, MCPV-1; ROSA KIT D816V can engraft NSG mice and generate an ASM/MCL-like disease, enabling in vivo drug validation. (arock2018preclinicalhumanmodels pages 33-42, arock2018preclinicalhumanmodels pages 1-6) | Cellosaurus: HMC-1; CL:0000097 mast cell; NCBITaxon:10090 mouse; NCIT: Xenograft Model |


*Table: This compact table summarizes the core disease-knowledge domains for mastocytosis, emphasizing current classification, genetics, diagnosis, prognosis, treatment, and model systems. It is designed as a quick-reference scaffold for populating a structured knowledge-base entry.*

## 1. Disease information

### Definition and classification

Mastocytosis is an abnormal clonal accumulation of neoplastic mast cells in skin and/or extracutaneous organs. WHO 5th edition recognizes cutaneous mastocytosis (CM), systemic mastocytosis, and mast-cell sarcoma. SM includes bone-marrow mastocytosis (BMM), indolent SM (ISM), smoldering SM (SSM), aggressive SM (ASM), SM with an associated hematologic neoplasm (SM-AHN), and mast-cell leukemia (MCL); ICC organization differs slightly but preserves the indolent-versus-advanced distinction. Advanced SM conventionally comprises ASM, SM-AHN, and MCL. (tremblay2024managementofadvanced pages 1-2, arock2018preclinicalhumanmodels pages 1-6, wang2023theinternationalconsensus pages 11-11)

**Synonyms/older terms:** mast cell disease; systemic mast-cell disease; urticaria pigmentosa for maculopapular cutaneous mastocytosis (MPCM); telangiectasia macularis eruptiva perstans for a telangiectatic MPCM phenotype; SM-AHN was formerly SM-AHNMD.

**Identifiers:** MONDO:0007950 (mastocytosis), MONDO:0019023 (cutaneous mastocytosis), MONDO:0016586 (systemic mastocytosis), and MONDO:0020332 (SM with associated clonal hematologic non-mast-cell-lineage disease). Useful coding families include ICD-10-CM Q82.2 for mastocytosis and D47.02 for systemic mastocytosis; exact national code/version should be retained because ICD-10 and ICD-11 mappings differ. MeSH uses *Mastocytosis* and narrower cutaneous/systemic concepts. OMIM and Orphanet identifiers should be attached at subtype level rather than assigning one hereditary-disorder number to all mastocytosis.

## 2. Etiology and risk/protective factors

### Causal factors

Most adult SM is an **acquired clonal hematopoietic neoplasm**, not a conventional inherited disorder. KIT D816V produces ligand-independent receptor-tyrosine-kinase activity; a 2024 review estimated KIT D816V in more than 95% of SM when sufficiently sensitive methods are used. Additional myeloid mutations help determine advanced phenotype rather than initiating every case. (tremblay2024managementofadvanced pages 1-2, nedoszytko2021clinicalimpactof pages 1-2)

Pediatric disease has a broader KIT spectrum, including extracellular-domain and insertion/deletion variants such as Del419, ITD501–502, ITD502–503, and occasionally germline K509I. Childhood CM is nevertheless usually sporadic and somatic. (arock2018preclinicalhumanmodels pages 33-42)

### Risk and modifier factors

* **Genetic modifiers:** additional **SRSF2, ASXL1, RUNX1, TET2, CBL, JAK2**, and RAS-pathway lesions are enriched in AdvSM; the SRSF2/ASXL1/RUNX1 (“S/A/R”) profile predicts adverse biology. **TPSAB1** alpha-tryptase copy-number gain causes hereditary alpha-tryptasemia (HαT), found in approximately 3–6% of Western general populations but up to 17% of SM cohorts, and can amplify baseline tryptase and mediator/anaphylaxis phenotypes. Reported cytokine/receptor associations—IL13, IL6, IL6R, IL31, and IL4R—remain modifiers rather than established monogenic causes. (c.2021cytogeneticandmolecular pages 12-12, nedoszytko2021clinicalimpactof pages 1-2)
* **Demography:** mastocytosis affects both sexes. Advanced disease, especially SM-AHN, is disproportionately male: in 3,403 ECNM-registry patients, 55.3% overall were female, but SM-AHN was 70% male. Men more often had organomegaly (23% versus 13%), less often skin involvement (71% versus 86%), and more often high-risk S/A/R abnormalities (63% versus 40%). (c.2021cytogeneticandmolecular pages 12-12)
* **Environment/lifestyle/infection:** no toxin, diet, smoking pattern, occupation, or infectious agent is established as a cause. Heat/cold, friction, alcohol, emotional stress, exercise, Hymenoptera venom, foods, medications, infection, surgery, and anesthesia may **trigger mediator release in an existing clone**, but do not ordinarily create the neoplasm.
* **Protective factors:** no validated protective allele, diet, vaccine, or exposure prevents clonal mastocytosis. Trigger avoidance protects against attacks, not disease acquisition.
* **Gene–environment interaction:** KIT-driven mast cells provide a hyperresponsive cellular substrate; IgE-mediated venom/food exposure or non-IgE physical/pharmacologic stimuli then provoke degranulation. HαT may raise the severity of this downstream response.

## 3. Phenotypes

Two partially independent phenotype axes should be encoded: **mediator release** and **mast-cell infiltration/organ damage**.

* **Skin:** red-brown macules/papules, plaques or mastocytoma; pruritus; flushing; urtication after rubbing (Darier sign); dermographism; infantile blistering and generalized thickening in diffuse CM. Course is episodic and stimulus-sensitive. Suggested HPO: *Pruritus* HP:0000989, *Abnormal blistering of the skin* HP:0008066, *Erythroderma* HP:0001019, *Skin lesion* HP:0000951.
* **Anaphylaxis/cardiovascular:** hypotension, presyncope/syncope, tachycardia, and anaphylaxis, often venom-associated in adults. Suggested HPO: *Anaphylaxis* HP:0100845, *Hypotension* HP:0002615, *Syncope* HP:0001279.
* **Gastrointestinal:** cramping, nausea, reflux, diarrhea, and—in advanced infiltration—malabsorption and weight loss. Suggested HPO: HP:0002027 abdominal pain, HP:0002014 diarrhea, HP:0002024 malabsorption.
* **Skeletal:** osteopenia/osteoporosis, bone pain, fragility fracture, focal osteosclerosis or osteolysis. In a 502-person regional clonal mast-cell cohort, osteoporosis—often with fragility fracture—occurred in 35%. Suggested HPO: HP:0000939 osteoporosis, HP:0002757 pathologic fracture, HP:0003277 osteolysis. (c.2021cytogeneticandmolecular pages 12-12)
* **Hematologic/advanced disease:** anemia, thrombocytopenia or neutropenia from marrow disease; hepatosplenomegaly, portal hypertension/ascites, hypoalbuminemia, lymphadenopathy, and hypersplenism. Hepatomegaly and splenomegaly were each/collectively reported in roughly 40% of AdvSM in a 2024 clinical review. Suggested HPO: HP:0001903 anemia, HP:0001873 thrombocytopenia, HP:0002242 hepatomegaly, HP:0001744 splenomegaly. (tremblay2024managementofadvanced pages 1-2)
* **Neuropsychological/systemic:** fatigue, sleep disturbance, headache, cognitive complaints, anxiety/depression and reduced work/social functioning are reported, although mechanisms and precise frequencies remain less certain than cutaneous/GI phenotypes.

Severity is highly variable. Symptoms may be severe in low-burden ISM because mediator release and tumor burden do not correlate perfectly. Qualitative interviews describe years of unexplained, unpredictable symptoms and substantial family and daily-life burden before diagnosis.

## 4. Genetic and molecular information

**Principal gene:** **KIT** (HGNC:6342; chromosome 4q12; receptor CD117). The canonical adult variant is somatic missense **NM_000222.3:c.2447A>T, p.(Asp816Val)** in the activation loop, a gain-of-function lesion. It is generally absent from population databases because it is acquired and pathogenic; population allele frequency is therefore not a meaningful germline-carrier statistic. (tremblay2024managementofadvanced pages 1-2, arock2018preclinicalhumanmodels pages 1-6)

Other activating KIT substitutions and indels occur, especially in pediatric CM and occasional familial disease. Variant interpretation must incorporate tissue, age, clonality, and function: an activating KIT variant in lesional tissue can be diagnostically relevant even when absent from germline databases. Routine ACMG germline categories alone are insufficient for somatic oncology interpretation.

Additional somatic lesions—TET2, SRSF2, ASXL1, RUNX1, CBL, JAK2 and NRAS/KRAS—modify differentiation, epigenetic state, splicing, signaling, prognosis, and SM-AHN phenotype. Open Targets ranks KIT as the strongest mastocytosis association; TET2, SRSF2, and ETNK1 are linked particularly to SM-AHN. (OpenTargets Search: mastocytosis, nedoszytko2021clinicalimpactof pages 1-2)

**Epigenetics/chromosomes:** TET2 and ASXL1 implicate DNA hydroxymethylation/chromatin regulation, but no diagnostic methylation signature is standard. Cytogenetic abnormalities are mainly a feature of AdvSM/associated neoplasms—10% of males versus 5% of females in one ECNM analysis—not a defining recurrent translocation of mastocytosis. (c.2021cytogeneticandmolecular pages 12-12)

**Inheritance:** most disease is sporadic somatic, so penetrance, carrier frequency, anticipation, consanguinity, and founder effects are generally not applicable. Rare familial KIT-activating variants show autosomal-dominant transmission with variable expressivity. HαT is an autosomal-dominant modifier, not itself mastocytosis.

## 5. Environmental information

No environmental agent or pathogen is known to cause mastocytosis. Record exposures as **attack triggers**: hymenoptera venom; alcohol; temperature change; friction/pressure; exercise; emotional stress; acute infection; radiocontrast; anesthetic/perioperative drugs; opioids and NSAIDs in susceptible individuals. Trigger lists must be individualized—blanket avoidance of all potentially mast-cell-active drugs is not evidence based. Tobacco, diet, exercise and pollution have no established causal association. Vaccination is not etiologic and routine immunization is generally appropriate with individualized precautions after prior severe reactions.

## 6. Mechanism/pathophysiology

**Causal chain:** hematopoietic progenitor acquires activating KIT lesion → constitutive KIT autophosphorylation → persistent RAS–RAF–MAPK, PI3K–AKT–mTOR and JAK/STAT5 signaling → impaired apoptosis plus mast-cell proliferation/survival and tissue homing → (a) increased releasable mediator pool and episodic degranulation, and/or (b) tissue infiltration → clinical manifestations. Secondary myeloid mutations are upstream modifiers of lineage complexity and aggressive transformation; mediator effects and organ damage are downstream outputs. (arock2018preclinicalhumanmodels pages 22-24, arock2018preclinicalhumanmodels pages 1-6)

Mast-cell mediators explain flushing/pruritus (histamine), vasodilation and hypotension (histamine/prostaglandin D2), bronchospasm/GI hypermotility (histamine/leukotrienes), and inflammatory/tissue-remodeling effects (tryptase and cytokines). Marrow replacement causes cytopenias; liver/splenic infiltration causes organomegaly, portal dysfunction and hypersplenism; osteoclast/osteoblast dysregulation produces osteoporosis or osteosclerosis.

Suggested annotations: **CL:0000097 mast cell**; GO:0007169 transmembrane receptor protein-tyrosine-kinase signaling; GO:0043303 mast-cell degranulation; GO:0042127 regulation of cell-population proliferation; GO:0006915 apoptotic process; GO:0038128/PI3K–AKT and GO mTOR/STAT signaling descendants. Relevant compartments include plasma membrane KIT, cytosolic kinase/signaling complexes, nucleus/chromatin, and secretory granules.

Human mast-cell-line experiments support pathway dependence: midostaurin inhibited HMC-1/ROSA models at approximately 0.05–0.3 µM, whereas imatinib and nilotinib had poor activity against D816V (>10 µM). These are **in-vitro pharmacology data**, not clinical dose-equivalence. (arock2018preclinicalhumanmodels pages 42-44)

Single-cell/spatial transcriptomic, proteomic, metabolomic and lipidomic signatures remain research-stage and are not validated diagnostics. NCT06432556 specifically investigates cellular heterogeneity, illustrating current movement toward single-cell characterization.

## 7. Anatomical structures affected

Primary sites are skin (UBERON:0002097), bone marrow (UBERON:0002371), gastrointestinal tract, liver (UBERON:0002107), spleen (UBERON:0002106), lymph nodes, and bone. Blood may carry KIT-mutated multilineage cells even when circulating mast cells are absent. MCL can produce circulating mast cells.

The affected tissue compartment is principally hematopoietic/connective tissue and the targeted population is the neoplastic mast cell (CL:0000097), sometimes within a broader mutated myeloid clone. Lateralization is not characteristic; disease is multifocal/systemic rather than unilateral.

## 8. Temporal development

Pediatric CM usually starts in infancy or early childhood. MPCM and solitary mastocytoma often improve spontaneously around puberty; diffuse CM is rarer, more severe, and associated with infantile blistering and anaphylaxis. Persistent small monomorphic lesions and systemic signs warrant reassessment. (arock2018preclinicalhumanmodels pages 33-42)

Adult SM is chronic and usually insidious. ISM/BMM may remain stable for decades; SSM has higher burden; AdvSM is progressive and defined by organ damage. A practical stage transition is: clonal low-burden disease → high-burden B-findings → C-finding organ damage → leukemic/associated-neoplasm evolution in a minority. There is no AJCC staging system.

Intervention windows include early recognition of anaphylaxis risk, baseline skeletal evaluation, and prompt cytoreduction when C-findings appear. Pediatric regression is spontaneous in many cases; molecular remission is not required to describe cutaneous clinical regression.

## 9. Epidemiology and population

A 2024 Swedish population-based study identified 2,040 adults and estimated annual incidence **1.56/100,000** (95% CI 1.29–1.87) and prevalence **23.9/100,000** (95% CI 22.8–25.0). The authors noted higher comorbidity and lower overall survival than matched controls, while overall prognosis remained favorable; coding inconsistency and under-reporting were limitations. (tremblay2024managementofadvanced pages 1-2)

A multidisciplinary Italian network found adult SM prevalence of **10.2/100,000** in Veneto and **17.2/100,000** in Verona, with incidence **1.09/100,000/year**. Among 431 SM cases, 91.0% were ISM and 54.8% had a bone-marrow-mastocytosis phenotype; venom allergy triggered 50% of diagnostic workups. These data support expert opinion that referral networks uncover substantial underdiagnosis. (c.2021cytogeneticandmolecular pages 12-12)

No reproducible ethnic founder population or endemic geography is established. Available registries are disproportionately European/White, limiting global generalizability.

## 10. Diagnostics

### Current SM criteria

The 2023 ICC major criterion is multifocal dense aggregates of at least **15 tryptase- and/or CD117-positive mast cells** in bone marrow or another extracutaneous organ. Minor criteria are: (1) >25% spindle-shaped/atypical immature mast cells; (2) aberrant CD25, CD2 and/or CD30 expression; (3) KIT D816V or another activating KIT mutation; and (4) persistently elevated basal serum tryptase >20 ng/mL. Diagnosis requires major + at least one minor criterion, or at least three minor criteria. Tryptase must be interpreted cautiously in SM-AHN and adjusted/ contextualized for HαT. (wang2023theinternationalconsensus pages 11-11)

**B-findings** indicate burden without organ failure: examples include marrow mast cells ≥30% and/or tryptase ≥200 ng/mL, organomegaly without dysfunction, and other-lineage abnormalities not meeting AHN criteria. **C-findings** establish organ damage: disease-related cytopenia, hepatic dysfunction/ascites/portal hypertension, hypersplenism, malabsorption with weight loss/hypoalbuminemia, and large osteolytic lesions/pathologic fracture. SSM requires multiple B-findings; ASM requires at least one C-finding attributable to mast-cell infiltration. (arock2018preclinicalhumanmodels pages 42-44)

### Test strategy

1. History/examination, complete blood count, chemistry/liver profile, basal serum tryptase, skin inspection and anaphylaxis history.
2. Highly sensitive peripheral-blood KIT D816V assay where adult SM is suspected. Low variant allele fractions can fall “well below the sensitivity of common” routine NGS panels; allele-specific qPCR or digital PCR is preferred for screening/quantification.
3. Bone-marrow aspirate/trephine with tryptase and CD117 IHC, CD25/CD2/CD30 flow/IHC, morphology, KIT testing, cytogenetics, and a myeloid NGS panel in suspected AdvSM/SM-AHN.
4. Skin biopsy when morphology is atypical; lesional KIT testing can confirm clonality.
5. DEXA and selected skeletal imaging; abdominal ultrasound/CT for organomegaly; targeted endoscopy/biopsy for severe GI disease.

WES/WGS are not first-line because depth at KIT D816 may be inadequate. CMA, mtDNA, repeat-expansion testing, and routine germline panels are not indicated unless another syndrome is suspected. TPSAB1 copy number requires a suitable copy-number assay, often digital PCR.

Differentials include MCAS without mastocytosis, hereditary alpha-tryptasemia, chronic urticaria, carcinoid/pheochromocytoma, hypereosinophilic and myeloid/lymphoid neoplasms with tyrosine-kinase fusions, basophilic leukemia, acute myeloid leukemia, and reactive mast-cell hyperplasia. Population screening/newborn screening is not recommended.

## 11. Outcome and prognosis

ISM generally approaches normal life expectancy, whereas AdvSM compromises survival. A recent review summarized historical median overall survival as ISM **198 months**, SSM **52 months**, ASM **41 months**, SM-AHN **24 months**, and MCL **2 months**; these figures reflect historical heterogeneous cohorts and should not be treated as outcomes under modern selective KIT inhibition. (tremblay2024managementofadvanced pages 2-4)

Adverse factors include advanced subtype/C-findings, older age, cytopenias, elevated alkaline phosphatase, high KIT D816V allele burden, multilineage involvement, SM-AHN, adverse cytogenetics, and S/A/R mutations. Male sex was associated with inferior progression-free and overall survival in the ECNM registry, plausibly because high-risk multi-mutated AdvSM was more frequent. Molecular response—such as ≥25% reduction in KIT D816V allele burden—has correlated with improved survival. IPSM and mutation-adjusted systems such as MARS support risk stratification. (tremblay2024managementofadvanced pages 2-4, c.2021cytogeneticandmolecular pages 12-12)

Morbidity includes recurrent anaphylaxis, fractures, chronic GI symptoms, fatigue, cognitive/affective complaints, work impairment, and treatment toxicity. Recovery is uncommon for adult clonal disease, but durable symptom and molecular control is increasingly achievable.

## 12. Treatment

### Indolent/cutaneous disease

Treatment is phenotype-directed: trigger education; nonsedating H1 antihistamines for skin symptoms; H2 blockade and/or proton-pump inhibition for acid symptoms; oral cromolyn for selected GI symptoms; leukotriene antagonists in selected patients; topical corticosteroids/calcineurin inhibitors or carefully selected phototherapy for troublesome CM; and osteoporosis treatment according to bone guidelines. All patients at material anaphylaxis risk should have an emergency plan and epinephrine autoinjector. Omalizumab is used off-label for recurrent anaphylaxis or refractory mediator symptoms, supported mainly by small studies rather than definitive disease-modifying evidence.

### Advanced disease

* **Avapritinib**—a selective KIT D816V inhibitor—is a major contemporary standard for eligible AdvSM and, in the United States, symptomatic ISM. It can produce pathologic and molecular responses. Reported adverse events in one summarized AdvSM dataset included hair-color change 34%, thrombocytopenia 22%, transaminase elevation 22%, neutropenia 19%, and dysgeusia 19%; bleeding/cognitive risk requires attention across the broader development program, particularly with severe thrombocytopenia. (tremblay2024managementofadvanced pages 10-11)
* **Midostaurin**, a multikinase/KIT inhibitor, remains established for AdvSM. Gastrointestinal toxicity, cytopenias, edema and infection require monitoring. Historical pivotal-study median OS was approximately 20.7 months in the summarized cohort context. (arock2018preclinicalhumanmodels pages 42-44, c.2021cytogeneticandmolecular pages 12-12)
* **Imatinib** is appropriate only for susceptible non-D816V KIT alterations or unknown KIT status in its labeled context; D816V is intrinsically resistant.
* **Cladribine** and interferon-alpha remain options when rapid cytoreduction or KIT inhibitor use is unsuitable. SM-AHN requires treatment of both components.
* **Allogeneic hematopoietic stem-cell transplantation** is the only potentially curative intervention, reserved for selected fit, high-risk AdvSM/MCL patients at expert centers. (tremblay2024managementofadvanced pages 2-4)

Emerging selective KIT inhibitors include **bezuclastinib/CGT9486** (SUMMIT, NCT05186753; phase 2, planned enrollment 237 for indolent/smoldering SM) and **elenestinib/BLU-263**. Other retrieved studies include hydroxychloroquine for cutaneous/indolent disease (NCT05084872), inhaled PA101 (NCT02478957), rupatadine (NCT01481909), omalizumab (NCT01333293), and transplantation (NCT00006413). Trial status should be checked directly at https://clinicaltrials.gov before operational use.

Suggested NCIT terms: *Histamine H1 Receptor Antagonist*, *Histamine H2 Receptor Antagonist*, *Epinephrine*, *Omalizumab*, *Midostaurin*, *Avapritinib*, *Tyrosine Kinase Inhibitor Therapy*, and *Allogeneic Hematopoietic Stem Cell Transplantation*.

## 13. Prevention

There is no proven primary prevention because the usual initiating lesion is somatic and unexplained. No vaccine prevents mastocytosis. Secondary prevention consists of earlier recognition in patients with unexplained anaphylaxis, persistent elevated tryptase, characteristic skin disease, osteoporosis/fracture, or unexplained organomegaly/cytopenia; population-wide screening is unsupported.

Tertiary prevention is clinically important: individualized trigger avoidance, venom immunotherapy when indicated, epinephrine availability, peri-procedural planning based on prior reactions, bone-density surveillance and fracture prevention, and serial CBC/liver/tryptase/KIT-burden monitoring in appropriate SM. Genetic counseling is offered for rare familial KIT disease and HαT, but routine carrier/prenatal screening is not justified.

## 14. Other species and natural disease

Naturally occurring mast-cell neoplasia is important in dogs (**NCBI Taxon 9615**) and cats (**9685**) and has been described in ferrets, horses, cattle and cheetahs. Canine cutaneous mast-cell tumor is common and frequently carries KIT regulatory/juxtamembrane lesions; some predict aggressive behavior. Feline and human KIT status is generally more useful diagnostically and therapeutically than as a stand-alone prognostic marker. Comparative conservation of KIT supports translational studies, but canine MCT is not biologically identical to human SM: human secondary myeloid mutations are not consistently conserved in dogs. (arock2018preclinicalhumanmodels pages 33-42)

These conditions are neoplastic, not infectious; there is no zoonotic transmission. Breed predisposition in dogs reflects germline risk architecture, but should not be projected onto human population risk.

## 15. Model organisms and experimental systems

Human mast-cell lines include **HMC-1**, LAD1/2, LUVA, ROSA and MCPV-1. HMC-1 and ROSA-KIT-D816V are particularly useful for KIT/STAT/PI3K drug studies; limitations include transformed-line adaptation, incomplete mature-tissue phenotype, and lack of human immune/stromal context. (arock2018preclinicalhumanmodels pages 1-6)

ROSA-KIT-D816V cells engrafted into immunodeficient NSG mice produce bone-marrow and splenic mast-cell infiltration resembling ASM/MCL and permit in-vivo drug validation. Reported models used approximately 1×10^6–10×10^6 cells and assessed engraftment at about ten weeks. Limitations include xenogeneic immunity, high experimental clone burden, and failure to reproduce the decades-long natural history of ISM. (arock2018preclinicalhumanmodels pages 33-42)

Naturally occurring canine/feline tumors complement engineered and xenograft systems by preserving spontaneous tumor evolution, but species-specific KIT spectra and secondary mutations constrain direct extrapolation.

## Evidence notes and authoritative-source interpretation

The 2023 ICC emphasizes that SM remains a diagnosis integrating **morphology, immunophenotype, molecular genetics and clinical burden**, rather than a KIT result alone. Its exact major criterion is “multifocal dense infiltrates” of at least 15 mast cells, and its minor criteria explicitly accept D816V **or another activating KIT mutation**. (wang2023theinternationalconsensus pages 11-11)

A 2024 management review characterizes AdvSM as “a rare hematologic malignancy with organ damage and compromised life expectancy” and identifies selective KIT inhibition as the pivotal recent advance while highlighting resistance, sequencing, SM-AHN treatment and MCL as unresolved problems. (tremblay2024managementofadvanced pages 2-4, tremblay2024managementofadvanced pages 1-2)

A genetics review states that HαT is found in “3–6% of general Western populations” but “up to 17%” of patients with SM, supporting its annotation as an inherited severity modifier rather than the primary clonal lesion. (nedoszytko2021clinicalimpactof pages 1-2)

### Key recent sources

* Wang et al. **June 2023**, *American Journal of Hematology*: ICC diagnostic/classification update. https://doi.org/10.1002/ajh.26966 (wang2023theinternationalconsensus pages 11-11)
* Tremblay et al. **September 2024**, *Journal of Blood Medicine*: AdvSM management and emerging therapies. https://doi.org/10.2147/JBM.S366367 (tremblay2024managementofadvanced pages 2-4, tremblay2024managementofadvanced pages 1-2)
* Bergström et al. **February 2024**, *Acta Oncologica*: Swedish population epidemiology. https://doi.org/10.2340/1651-226X.2024.31406
* Pardanani, **May 2023**, *American Journal of Hematology*: adult SM diagnosis, risk stratification and management. https://doi.org/10.1002/ajh.26962
* Cilloni et al. **October 2024**, *International Journal of Molecular Sciences*: low-VAF KIT detection. https://doi.org/10.3390/ijms252010885
* Kluin-Nelemans et al. **January 2021**, *Theranostics*: 3,403-patient ECNM sex/outcome analysis. https://doi.org/10.7150/thno.51872 (c.2021cytogeneticandmolecular pages 12-12)
* Nedoszytko et al. **January 2021**, *International Journal of Molecular Sciences*: inherited/acquired variants. https://doi.org/10.3390/ijms22010411 (nedoszytko2021clinicalimpactof pages 1-2)

**Knowledge gaps:** globally representative epidemiology, validated protective factors, reliable prediction of pediatric persistence, standardized neurocognitive/QoL phenotyping, prospective sequencing after KIT-inhibitor resistance, and clinically validated single-cell/spatial or multi-omic biomarkers remain unavailable.

References

1. (tremblay2024managementofadvanced pages 1-2): Douglas Tremblay, Nicole Wagner, and John Mascarenhas. Management of advanced systemic mastocytosis: clinical challenges. Journal of Blood Medicine, 15:421-433, Sep 2024. URL: https://doi.org/10.2147/jbm.s366367, doi:10.2147/jbm.s366367. This article has 9 citations.

2. (wang2023theinternationalconsensus pages 11-11): Sa A. Wang, Attilio Orazi, Jason Gotlib, Andreas Reiter, Alexandar Tzankov, Robert P. Hasserjian, Daniel A. Arber, and Ayalew Tefferi. The international consensus classification of eosinophilic disorders and systemic mastocytosis. American Journal of Hematology, 98:1286-1306, Jun 2023. URL: https://doi.org/10.1002/ajh.26966, doi:10.1002/ajh.26966. This article has 74 citations and is from a domain leading peer-reviewed journal.

3. (arock2018preclinicalhumanmodels pages 1-6): Michel Arock, Ghaith Wedeh, Gregor Hoermann, Siham Bibi, Cem Akin, Barbara Peter, Karoline V. Gleixner, Karin Hartmann, Joseph H. Butterfield, Dean D. Metcalfe, and Peter Valent. Preclinical human models and emerging therapeutics for advanced systemic mastocytosis. Haematologica, 103:1760-1771, Jul 2018. URL: https://doi.org/10.3324/haematol.2018.195867, doi:10.3324/haematol.2018.195867. This article has 37 citations.

4. (nedoszytko2021clinicalimpactof pages 1-2): Boguslaw Nedoszytko, Michel Arock, Jonathan Lyons, Guillaume Bachelot, Lawrence Schwartz, Andreas Reiter, Mohamad Jawhar, Juliana Schwaab, Magdalena Lange, Georg Greiner, Gregor Hoermann, Marek Niedoszytko, Dean Metcalfe, and Peter Valent. Clinical impact of inherited and acquired genetic variants in mastocytosis. International Journal of Molecular Sciences, 22(1):411, Jan 2021. URL: https://doi.org/10.3390/ijms22010411, doi:10.3390/ijms22010411. This article has 39 citations.

5. (arock2018preclinicalhumanmodels pages 22-24): Michel Arock, Ghaith Wedeh, Gregor Hoermann, Siham Bibi, Cem Akin, Barbara Peter, Karoline V. Gleixner, Karin Hartmann, Joseph H. Butterfield, Dean D. Metcalfe, and Peter Valent. Preclinical human models and emerging therapeutics for advanced systemic mastocytosis. Haematologica, 103:1760-1771, Jul 2018. URL: https://doi.org/10.3324/haematol.2018.195867, doi:10.3324/haematol.2018.195867. This article has 37 citations.

6. (c.2021cytogeneticandmolecular pages 12-12): Hanneke C. Kluin-Nelemans, Mohamad Jawhar, Andreas Reiter, Bjorn van Anrooij, Jason Gotlib, Karin Hartmann, Anja Illerhaus, Hanneke N. G. Oude Elberink, Aleksandra Gorska, Marek Niedoszytko, Magdalena Lange, Luigi Scaffidi, Roberta Zanotti, Patrizia Bonadonna, Cecelia Perkins, Chiara Elena, Luca Malcovati, Khalid Shoumariyeh, Nikolas von Bubnoff, Sabine Müller, Massimo Triggiani, Roberta Parente, Juliana Schwaab, Michael Kundi, Anna Belloni Fortina, Francesca Caroppo, Knut Brockow, Alexander Zink, David Fuchs, Irena Angelova-Fischer, Akif Selim Yavuz, Michael Doubek, Mattias Mattsson, Hans Hagglund, Jens Panse, Anne Simonowski, Vito Sabato, Tanja Schug, Madlen Jentzsch, Christine Breynaert, Judit Várkonyi, Vanessa Kennedy, Olivier Hermine, Julien Rossignol, Michel Arock, Peter Valent, and Wolfgang R. Sperr. Cytogenetic and molecular aberrations and worse outcome for male patients in systemic mastocytosis. Theranostics, 11:292-303, Jan 2021. URL: https://doi.org/10.7150/thno.51872, doi:10.7150/thno.51872. This article has 45 citations and is from a domain leading peer-reviewed journal.

7. (arock2018preclinicalhumanmodels pages 42-44): Michel Arock, Ghaith Wedeh, Gregor Hoermann, Siham Bibi, Cem Akin, Barbara Peter, Karoline V. Gleixner, Karin Hartmann, Joseph H. Butterfield, Dean D. Metcalfe, and Peter Valent. Preclinical human models and emerging therapeutics for advanced systemic mastocytosis. Haematologica, 103:1760-1771, Jul 2018. URL: https://doi.org/10.3324/haematol.2018.195867, doi:10.3324/haematol.2018.195867. This article has 37 citations.

8. (arock2018preclinicalhumanmodels pages 33-42): Michel Arock, Ghaith Wedeh, Gregor Hoermann, Siham Bibi, Cem Akin, Barbara Peter, Karoline V. Gleixner, Karin Hartmann, Joseph H. Butterfield, Dean D. Metcalfe, and Peter Valent. Preclinical human models and emerging therapeutics for advanced systemic mastocytosis. Haematologica, 103:1760-1771, Jul 2018. URL: https://doi.org/10.3324/haematol.2018.195867, doi:10.3324/haematol.2018.195867. This article has 37 citations.

9. (tremblay2024managementofadvanced pages 2-4): Douglas Tremblay, Nicole Wagner, and John Mascarenhas. Management of advanced systemic mastocytosis: clinical challenges. Journal of Blood Medicine, 15:421-433, Sep 2024. URL: https://doi.org/10.2147/jbm.s366367, doi:10.2147/jbm.s366367. This article has 9 citations.

10. (tremblay2024managementofadvanced pages 10-11): Douglas Tremblay, Nicole Wagner, and John Mascarenhas. Management of advanced systemic mastocytosis: clinical challenges. Journal of Blood Medicine, 15:421-433, Sep 2024. URL: https://doi.org/10.2147/jbm.s366367, doi:10.2147/jbm.s366367. This article has 9 citations.

11. (OpenTargets Search: mastocytosis): Open Targets Query (mastocytosis, 28 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

## Artifacts

- [Edison artifact artifact-00](Mastocytosis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.