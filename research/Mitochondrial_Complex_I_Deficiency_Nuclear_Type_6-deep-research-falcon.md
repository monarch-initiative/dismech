---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T03:36:42.587791'
end_time: '2026-08-27T03:46:48.617095'
duration_seconds: 606.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mitochondrial Complex I Deficiency, Nuclear Type 6
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 6
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_6-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 6
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 6** covering all of the
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
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 6
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 6** covering all of the
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


# Mitochondrial Complex I Deficiency, Nuclear Type 6

## Executive summary and evidence scope

Mitochondrial complex I deficiency, nuclear type 6 (MC1DN6) is an ultra-rare, autosomal-recessive primary mitochondrial disorder caused by biallelic pathogenic variants in **NDUFS2**, which encodes a core catalytic subunit of respiratory-chain complex I. Its best-established severe presentation is an early-onset Leigh or Leigh-like encephalopathy, although hypomorphic NDUFS2 genotypes can produce a predominantly optic-neuropathy phenotype. The mechanistic chain is: biallelic NDUFS2 dysfunction → impaired complex-I assembly/activity and NADH oxidation → reduced NAD⁺ regeneration, proton pumping, and oxidative phosphorylation → metabolic compensation and lactate accumulation → energy failure in brain, optic nerve, skeletal muscle, and potentially other high-demand tissues.

The evidence base is exceptionally small. Disease-specific prevalence, penetrance, phenotype frequencies, longitudinal survival, validated biomarkers, and treatment-response rates have not been established. Consequently, this report labels evidence as **NDUFS2-specific human**, **NDUFS2 model**, or **extrapolated from Leigh syndrome/complex-I deficiency**. Open Targets lists five foundational PubMed records—PMIDs **9585441, 11220739, 20819849, 22036843, and 22142868**—but the retrieved material did not expose sufficient patient-level text to verify every historical variant and clinical detail independently. Exact variant nomenclature should therefore be imported only after direct ClinVar/OMIM and transcript-level verification. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 6)

| Domain | NDUFS2-specific finding | Suggested ontology/identifier | Evidence strength or caveat |
|---|---|---|---|
| Disease identity | Mitochondrial complex I deficiency, nuclear type 6 is resolved to a disease entity associated with **NDUFS2** | **MONDO:0032611**; disease label: mitochondrial complex I deficiency, nuclear type 6 | Direct disease-target association in Open Targets; disease-level resource rather than single-patient record (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 6) |
| Causal gene | Causal nuclear gene is **NDUFS2** encoding NADH:ubiquinone oxidoreductase core subunit S2, a catalytic/core complex I subunit | **NDUFS2**; Ensembl **ENSG00000158864** | Strong gene-disease support in curated databases; foundational PMIDs listed but not all full case texts were retrievable here (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 6) |
| Inheritance/mechanism | Disease mechanism is **biallelic germline loss-of-function or deleterious missense variation**, consistent with **autosomal recessive** inheritance | Inheritance: **HP:0000007**; germline variant origin | Supported by Open Targets/Gene2Phenotype-style assertions; exact penetrance not available (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 6) |
| Pathophysiology | Defect impairs respiratory-chain **complex I** function and oxidative phosphorylation, causing energy failure in high-demand tissues | GO: mitochondrial respiratory chain complex I (**GO:0005747**); OXPHOS/respiratory electron transport | NDUFS2 is a core catalytic subunit; severe deficiency is biologically plausible and supported by animal/cellular studies, but many mechanistic details come from models rather than NDUFS2 patient series (mcelroy2022reducedexpressionof pages 1-2, scheffler2015mitochondrialdiseaseassociated pages 18-21) |
| Core phenotype: encephalopathy | Reported/expected human phenotype includes **Leigh or Leigh-like encephalopathy** within the complex I deficiency spectrum | **HP:0000007**? no; phenotype term: **Leigh syndrome HP:0000007 not correct**; use **Leigh syndrome** disease mapping plus **encephalopathy HP:0001298** | NDUFS2 is repeatedly linked to Leigh/Leigh-like presentations in reviews and hereditary optic neuropathy literature; exact NDUFS2 case counts not available in retrieved full text (scheffler2015mitochondrialdiseaseassociated pages 18-21) |
| Developmental phenotype | **Developmental delay/regression** is part of the typical severe pediatric complex I/Leigh spectrum attributed to NDUFS2-related disease | **HP:0001263** developmental regression; **HP:0011344** severe global developmental delay | Mostly inferred from Leigh-spectrum literature and NDUFS2-related reports; frequency unknown for nuclear type 6 specifically (scheffler2015mitochondrialdiseaseassociated pages 18-21, ludwig2023contributionofneuroinflammation pages 28-32) |
| Neuromuscular phenotype | **Hypotonia** is a common feature in Leigh/complex I deficiency and expected in NDUFS2 disease | **HP:0001252** hypotonia | Supported at syndrome level; not enough retrieved patient-level data for NDUFS2-specific prevalence (scheffler2015mitochondrialdiseaseassociated pages 18-21, ludwig2023contributionofneuroinflammation pages 28-32) |
| Ophthalmic phenotype | **Optic atrophy/optic neuropathy** can occur in NDUFS2-related disease, including LHON-like optic neuropathy and optic atrophy in reported NDUFS2 literature | **HP:0000648** optic atrophy; **HP:0001138** optic neuropathy | Evidence exists for NDUFS2-associated optic neuropathy, but phenotype breadth ranges from isolated optic neuropathy to Leigh-like disease; exact variant-level mapping incomplete here (ludwig2023contributionofneuroinflammation pages 28-32) |
| Biochemical phenotype | **Lactic acidosis / elevated lactate** is a key metabolic abnormality in Leigh/complex I deficiency | **HP:0002151** increased serum lactate; **HP:0003128** lactic acidosis | Strong at Leigh-spectrum level; NDUFS2 nuclear type 6-specific quantitative biomarker distributions unavailable in retrieved material (scheffler2015mitochondrialdiseaseassociated pages 18-21, ludwig2023contributionofneuroinflammation pages 28-32) |
| Laboratory defect | Hallmark lab abnormality is **isolated mitochondrial complex I enzyme deficiency** in affected tissue/cells | Complex I deficiency; LOINC/SNOMED local mapping as available | Strong disease-class evidence; tissue source often muscle/fibroblasts, but exact assay cutoffs and tissue-specific values for NDUFS2 cases were not retrieved (scheffler2015mitochondrialdiseaseassociated pages 18-21) |
| Diagnostic approach | Recommended workup: clinical suspicion for mitochondrial encephalopathy/Leigh syndrome, serum/CSF lactate and other biomarkers, neuroimaging, respiratory-chain enzymology, then **WES/WGS or mitochondrial disease gene panel including NDUFS2** | NDUFS2 in mitochondrial/OXPHOS/Leigh panels; consider **WES/WGS** | Diagnostic framework is strong for mitochondrial disease broadly, but no NDUFS2-specific consensus guideline was identified (scheffler2015mitochondrialdiseaseassociated pages 18-21, ludwig2023contributionofneuroinflammation pages 28-32) |
| Biomarkers | General mitochondrial biomarkers such as **FGF21** and **GDF15** are used in PMD diagnostics, but no NDUFS2-specific biomarker signature is established | FGF21; GDF15 | Extrapolated from broader PMD practice; not validated specifically for nuclear type 6 in retrieved evidence (mcelroy2022reducedexpressionof pages 6-7) |
| Treatment status | **No approved NDUFS2-specific disease-modifying therapy** was identified; care is supportive and multidisciplinary | NCIT: supportive care; mitochondrial disease management | Strong negative finding from available evidence; disease-specific interventional data absent (scheffler2015mitochondrialdiseaseassociated pages 18-21) |
| Trial landscape | Leigh-spectrum trials have evaluated/are evaluating **vatiquinone (EPI-743)**, **sirolimus/nab-sirolimus**, **elamipretide**, and **TTI-0102**, but inclusion was not NDUFS2-specific in retrieved records | **NCT02352896**, **NCT01721733**, **NCT03747328**, **NCT06990984** | Important caveat: trial eligibility was Leigh-spectrum/genetically confirmed LS, not specifically nuclear type 6; subtype-specific efficacy unknown (NCT02352896 chunk 1, NCT03747328 chunk 1, NCT01721733 chunk 1, NCT06990984 chunk 1) |
| Epidemiology | No robust **prevalence/incidence** estimate for NDUFS2-related nuclear type 6 alone was found | MONDO:0032611 | Major evidence gap; only broader Leigh estimates are available in retrieved evidence (e.g., prevalence around 1/40,000 for Leigh syndrome) (ludwig2023contributionofneuroinflammation pages 28-32) |
| Prognosis | Likely severe, often early-onset pediatric mitochondrial disease; prognosis probably tracks Leigh-spectrum severity | Natural history fields pending disease-specific data | Prognosis for NDUFS2 nuclear type 6 specifically is insufficiently quantified; avoid overgeneralizing from all Leigh syndrome (scheffler2015mitochondrialdiseaseassociated pages 18-21, ludwig2023contributionofneuroinflammation pages 28-32) |
| Model-organism caveat | **Do not equate NDUFS2 disease with the Ndufs4 mouse model**. Ndufs4 models are widely used for Leigh syndrome but represent an accessory-subunit defect, whereas NDUFS2 is a **core catalytic subunit**. Ndufs2 heterozygous mice show no overt healthspan phenotype, indicating dosage sensitivity differs by gene and model | Gene-specific model annotation: **Ndufs2** vs **Ndufs4** | High-value interpretive caveat for translational use; many mechanistic and therapeutic studies use Ndufs4, not Ndufs2 (mcelroy2022reducedexpressionof pages 1-2, mcelroy2022reducedexpressionof pages 6-7) |


*Table: This table summarizes the most reusable disease knowledge-base fields for mitochondrial complex I deficiency, nuclear type 6. It highlights what is directly supported for NDUFS2 and clearly labels where current evidence is extrapolated from broader Leigh syndrome or complex I deficiency literature.*

## 1. Disease information

**Definition.** MC1DN6 is a Mendelian oxidative-phosphorylation disorder in which nuclear-encoded NDUFS2 dysfunction causes isolated or predominant mitochondrial respiratory-chain complex-I deficiency. Nuclear structural-subunit defects generally present neonatally or in early infancy and can cause Leigh syndrome, Leigh-like encephalopathy, encephalomyopathy, or lethal infantile mitochondrial disease. (scheffler2015mitochondrialdiseaseassociated pages 18-21)

**Identifiers and terminology**

- **MONDO:** **MONDO:0032611**.
- **Causal target:** NDUFS2; Ensembl **ENSG00000158864**; approved name *NADH:ubiquinone oxidoreductase core subunit S2*.
- **Common names:** mitochondrial complex I deficiency, nuclear type 6; MC1DN6; NDUFS2-related mitochondrial disease; NDUFS2-related complex-I deficiency.
- **Phenotypic labels:** NDUFS2-related Leigh syndrome/Leigh-like syndrome; recessive NDUFS2-related optic neuropathy for hypomorphic presentations.
- **OMIM/Orphanet:** a stable disease-level OMIM or Orphanet number was not exposed by the retrieved evidence and should be verified directly before database ingestion. Likewise, no uniquely specific ICD-10, ICD-11, or MeSH code was established; broader mitochondrial-metabolism/Leigh syndrome codes are normally used.

The disease identity and gene relationship come from aggregated disease-level resources, not EHR-derived individual-patient data. Open Targets reports one associated target, NDUFS2, with an overall association score of approximately 0.665 and biallelic inheritance assertions. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 6)

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The cause is **biallelic germline variation in NDUFS2**, usually severe missense or loss-of-function alleles. The expected mechanism is loss of normal protein function rather than gain of function or dominant-negative activity. Open Targets records consequences including absent gene product and damaging missense variation and specifies a biallelic autosomal requirement. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 6)

### Risk factors

- **Genetic:** having two pathogenic NDUFS2 alleles is the principal risk factor. Parental consanguinity can increase the probability of homozygosity for a rare recessive allele, although no MC1DN6-specific effect size is available.
- **Family history:** an affected sibling or two carrier parents confers the standard autosomal-recessive recurrence risk of 25% per conception.
- **Environmental/lifestyle:** no toxin, diet, infection, occupation, sex, or lifestyle exposure is known to cause MC1DN6. Fever, fasting, infection, anesthesia, dehydration, and other catabolic stressors may precipitate decompensation in mitochondrial disease, but this is syndrome-level clinical reasoning rather than a demonstrated NDUFS2-specific interaction.

### Protective factors

No protective NDUFS2 allele, modifier gene, diet, drug, or lifestyle intervention has been validated. Ndufs2+/− mice are informative: despite about a 50% reduction in Ndufs2 mRNA, they retained complex-I function and showed no overt healthspan or lifespan impairment. This suggests substantial biological reserve and supports recessive inheritance, but it does not establish protection in humans. (mcelroy2022reducedexpressionof pages 1-2, mcelroy2022reducedexpressionof pages 6-7)

## 3. Phenotypes

Patient numbers are too small for defensible percentages. Frequencies below should therefore be encoded as **reported**, **characteristic of the severe spectrum**, or **unknown**, not as precise proportions.

### Neurologic and developmental

- **Leigh/Leigh-like encephalopathy:** usually infantile or early-childhood onset; severe and progressive. Suggested terms: encephalopathy **HP:0001298**, neurodevelopmental regression **HP:0002376**, global developmental delay **HP:0001263**.
- **Developmental delay followed by regression:** progressive or stepwise, often around metabolic stress. Daily function may deteriorate from independent or assisted motor skills to dependence for mobility, feeding, and communication.
- **Hypotonia and weakness:** **HP:0001252**, muscle weakness **HP:0001324**.
- **Ataxia/dystonia or other movement disorder:** ataxia **HP:0001251**, dystonia **HP:0001332**; exact NDUFS2 frequencies are unknown.
- **Seizures:** **HP:0001250**; EEG abnormalities may accompany encephalopathy, but disease-specific frequency is unavailable.
- **Respiratory dysregulation:** abnormal breathing **HP:0002793**, central hypoventilation **HP:0007110** where documented; this can be life-threatening in Leigh-spectrum disease.

Broader Leigh data—not MC1DN6-specific—describe developmental delay, epilepsy, respiratory abnormalities, ataxia, hypotonia, motor polyneuropathy, and optic atrophy. One synthesis estimated a typical onset near two years and mean survival of approximately two years after onset, but these figures must not be assigned directly to NDUFS2 disease. (ludwig2023contributionofneuroinflammation pages 28-32)

### Ophthalmic

Optic atrophy or an LHON-like optic neuropathy is a recognized NDUFS2-associated phenotype, particularly with compound severe/hypomorphic alleles. Suggested terms are optic atrophy **HP:0000648**, decreased visual acuity **HP:0007663**, and visual impairment **HP:0000505**. Visual loss substantially affects education, orientation, mobility, and independence. The severe Leigh phenotype and nonsyndromic optic-neuropathy phenotype should be represented as a continuum rather than separate causal diseases.

### Metabolic and laboratory

- Elevated blood or CSF lactate: **HP:0002151**; lactic acidosis: **HP:0003128**.
- Reduced complex-I activity in muscle, fibroblasts, or other tested tissue.
- Elevated lactate:pyruvate ratio may indicate impaired NADH oxidation, but neither sensitivity nor specificity is adequate to exclude disease when normal.

Nuclear structural-subunit mutations generally reduce the steady-state amount of active complex I rather than merely lowering the specific activity of intact enzyme. (scheffler2015mitochondrialdiseaseassociated pages 18-21)

### Imaging and quality of life

In a Leigh presentation, MRI is expected to show bilateral, approximately symmetric basal-ganglia and/or brainstem lesions; however, an NDUFS2-specific imaging prevalence could not be established. Suggested anatomy/phenotype terms include abnormal basal-ganglia MRI **HP:0012758**, brainstem abnormality **HP:0002363**, and cerebral/cerebellar atrophy where present. Severe motor, visual, feeding, respiratory, and cognitive impairment implies major family and caregiver burden, but no MC1DN6-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study was found.

## 4. Genetic and molecular information

**Gene:** NDUFS2, a nuclear gene encoding an approximately 49-kDa core complex-I subunit positioned at the matrix–membrane interface. It participates in the quinone-reduction/catalytic region and is not an accessory subunit. (mcelroy2022reducedexpressionof pages 1-2)

**Variant interpretation:** pathogenicity should require biallelic segregation plus ACMG/AMP assessment incorporating rarity, phenotype consistency, predicted/proven protein effect, complex-I enzymology, and functional complementation where available. Historical papers report missense and absent-product mechanisms, but this retrieval did not provide a complete transcript-normalized variant list. Accordingly:

- do not copy legacy residue numbering without confirming the MANE transcript;
- query ClinVar and gnomAD at the time of curation for classification, review status, and ancestry-specific allele frequency;
- retain VUS status unless segregation and functional evidence justify reclassification;
- encode variants as germline, not somatic.

No validated modifier gene, epigenetic signature, recurrent pathogenic copy-number alteration, translocation, inversion, or aneuploidy has been established. A large deletion involving NDUFS2 could theoretically act as one allele, but conventional MC1DN6 is a sequence-level recessive disorder.

## 5. Environmental information

There is no evidence that pollution, radiation, smoking, alcohol, occupational exposure, or an infectious agent causes this Mendelian disease. Environmental factors are relevant primarily as **physiologic stressors** after disease is present. Avoidance of prolonged fasting, dehydration, and known mitochondrial-toxic drugs when alternatives exist is prudent, but not proven to prevent onset. No NDUFS2-specific diet, exercise prescription, microbiome interaction, or toxin-response study was identified.

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. **Biallelic NDUFS2 dysfunction** reduces the abundance or function of a catalytic core subunit.
2. **Complex-I assembly/stability and electron transfer decline.** NADH-to-ubiquinone electron transfer and proton translocation become inefficient.
3. **Redox and bioenergetic failure develops:** NADH accumulates relative to NAD⁺; mitochondrial membrane-potential support and ATP generation fall.
4. **Compensation:** glycolytic flux increases, pyruvate is reduced to lactate to regenerate cytosolic NAD⁺, and amino-acid/TCA metabolism is remodeled.
5. **Tissue injury:** high-demand neurons, glia, retinal ganglion-cell axons, skeletal muscle, myocardium, and respiratory-control circuits cannot maintain ion gradients and biosynthesis; downstream oxidative stress, calcium dysregulation, apoptosis, and neuroinflammation may follow.
6. **Clinical output:** encephalopathy/regression, movement disorder, hypotonia, visual loss, seizures, respiratory dysfunction, and lactic acidosis.

Suggested GO terms include mitochondrial respiratory-chain complex-I assembly **GO:0032981**, mitochondrial electron-transport NADH-to-ubiquinone **GO:0006120**, oxidative phosphorylation **GO:0006119**, ATP metabolic process **GO:0046034**, cellular response to oxidative stress **GO:0034599**, and mitochondrion **GO:0005739**/respiratory-chain complex I **GO:0005747**.

### Cell types and tissues

Suggested Cell Ontology terms include neuron **CL:0000540**, astrocyte **CL:0000127**, oligodendrocyte **CL:0000128**, microglial cell **CL:0000129**, skeletal muscle cell **CL:0000188**, cardiomyocyte **CL:0000746**, and retinal ganglion cell **CL:0000740**. These are biologically plausible target populations, not all directly demonstrated in NDUFS2 patients.

### NDUFS2-specific functional evidence

Conditional Ndufs2 loss in neural stem/progenitor lineages severely inhibited perinatal brain development, impaired progenitor proliferation and neuronal/oligodendroglial differentiation, and caused death before postnatal day 10. Conversely, heterozygous mice with approximately 50% lower transcript retained complex-I function and normal healthspan, demonstrating a nonlinear dosage threshold. (mcelroy2022reducedexpressionof pages 1-2, mcelroy2022reducedexpressionof pages 6-7)

NDUFS2 also contributes to mitochondrial oxygen sensing in pulmonary-artery smooth muscle. This may be mechanistically relevant to respiratory physiology but has not been shown to drive MC1DN6 pulmonary disease.

### Recent research, 2023–2024

Recent Leigh-model work emphasizes cell-type-specific metabolic failure, immune activation, and increasingly sophisticated iPSC/organoid and cryo-EM approaches. However, most prominent 2023–2024 studies use **NDUFS4**, not NDUFS2. NDUFS4 is an accessory-subunit defect and cannot be treated as a gene-specific model of MC1DN6. The distinction is especially important when interpreting rapamycin, hypoxia, cannabidiol, nicotinamide-riboside, or immune-targeting studies.

No MC1DN6-specific single-cell atlas, spatial transcriptomic dataset, patient proteome, lipidome, metabolome, CRISPR screen, or multi-omic natural-history cohort was found. These are major current research gaps.

## 7. Anatomical structures affected

**Primary:** central nervous system, especially basal ganglia and brainstem in Leigh disease; optic nerve/retinal ganglion-cell pathway in optic-neuropathy presentations; skeletal muscle in encephalomyopathic disease.

**Potential secondary involvement:** peripheral nerve, myocardium/conduction system, respiratory muscles, and feeding/swallowing apparatus. Disease-specific frequencies are unknown.

Suggested UBERON terms include brain **UBERON:0000955**, basal ganglion **UBERON:0002420**, brainstem **UBERON:0002298**, cerebellum **UBERON:0002037**, optic nerve **UBERON:0000966**, retina **UBERON:0000966 requires local verification**, skeletal muscle organ **UBERON:0001630**, and heart **UBERON:0000948**. Lesions are classically bilateral/symmetric in Leigh syndrome rather than lateralized. The central subcellular compartment is the mitochondrial inner membrane/matrix-facing peripheral arm of complex I.

## 8. Temporal development

Severe nuclear complex-I structural defects generally begin congenitally, neonatally, or in infancy; hypomorphic NDUFS2 disease may present later with progressive optic neuropathy. The course is chronic and usually progressive, sometimes with acute or stepwise deterioration during catabolic illness. There is no validated MC1DN6 staging system. Practical stages are:

1. presymptomatic/early developmental phase;
2. emerging hypotonia, delay, visual or motor abnormalities;
3. regression and radiographic Leigh lesions;
4. advanced multisystem disability with feeding or respiratory compromise.

Spontaneous durable remission has not been documented. Early molecular diagnosis is the principal intervention window for anticipatory respiratory, nutritional, cardiac, neurologic, and visual surveillance.

## 9. Inheritance and population

Inheritance is autosomal recessive. Male and female individuals should be affected equally. Penetrance for two unequivocally severe alleles is presumed high, but it has not been quantified; expressivity varies with residual activity and allele combination. Anticipation is not expected. Germline mosaicism is theoretically possible but not established. No confirmed founder allele, geographic concentration, ethnicity-specific prevalence, carrier frequency, or sex ratio has been reported.

No incidence or prevalence estimate exists for MC1DN6 itself. A broader Leigh-syndrome estimate of approximately **1 in 40,000** has been cited, and complex-I defects were estimated to account for about **34%** of Leigh cases; neither statistic can be used to calculate MC1DN6 prevalence because NDUFS2 represents only a tiny, unmeasured subset. (ludwig2023contributionofneuroinflammation pages 28-32)

## 10. Diagnostics

### Recommended workflow

1. **Clinical recognition:** developmental delay/regression, hypotonia, dystonia/ataxia, optic atrophy, seizures, respiratory abnormality, or multisystem disease.
2. **Biochemistry:** lactate, pyruvate with ratio, blood gas, glucose, electrolytes, liver enzymes, creatine kinase, amino acids, urine organic acids, acylcarnitines; consider CSF lactate when lumbar puncture is otherwise indicated.
3. **Imaging and physiology:** brain MRI with spectroscopy where available; EEG for seizures; ECG/echocardiography; ophthalmologic examination including OCT and visual evoked potentials; swallowing and respiratory assessment.
4. **Molecular testing:** trio WES or WGS, or a comprehensive nuclear-plus-mtDNA mitochondrial/Leigh panel containing NDUFS2. Confirm candidate variants by orthogonal methods and test parental phase.
5. **Functional confirmation when needed:** complex-I enzymology in muscle or fibroblasts; blue-native PAGE/complexome profiling; oxygen-consumption assays; RNA sequencing for suspected splice variants; complementation in patient cells.

WGS is advantageous for noncoding/splice, copy-number, and structural variants. WES is efficient for coding NDUFS2 variants. Single-gene sequencing is appropriate only when familial variants are known. CMA may detect a deletion but is not first-line for most cases; karyotype, FISH, and repeat-expansion tests have no routine role. **mtDNA sequencing remains important in an undiagnosed Leigh phenotype but does not test the nuclear NDUFS2 cause.**

FGF21 and GDF15 may support a general mitochondrial diagnosis but are neither NDUFS2-specific nor sufficiently sensitive to exclude disease. The central diagnostic endpoint is demonstration of two pathogenic/likely pathogenic NDUFS2 alleles in trans, with phenotype and biochemical consistency.

### Differential diagnosis

The differential includes other nuclear and mtDNA complex-I disorders; SURF1-, NDUFS4-, NDUFV1-, NDUFA2-, and NDUFS6-related disease; pyruvate-dehydrogenase deficiency; biotin-thiamine-responsive basal-ganglia disease; organic acidemias; HIBCH/ECHS1 disease; POLG-related disease; Wilson disease in older patients; hypoxic-ischemic injury; toxic/metabolic encephalopathy; and other hereditary optic neuropathies. A key discriminator is biallelic NDUFS2 variation plus an isolated/predominant complex-I defect.

There is no population newborn screen. Cascade testing, carrier testing of relatives, and testing of apparently unaffected siblings are appropriate after a molecular diagnosis.

## 11. Outcome and prognosis

No NDUFS2-specific 5- or 10-year survival curve, life expectancy, mortality rate, disability scale, or prognostic model exists. Severe neonatal/infantile encephalopathy can be rapidly progressive and fatal, whereas hypomorphic optic-neuropathy presentations may permit survival into adulthood. Prognosis is likely influenced by residual complex-I activity, age at onset, brainstem/respiratory involvement, seizures, feeding safety, cardiomyopathy/conduction disease, and the number and severity of metabolic crises.

Likely long-term morbidity includes motor and cognitive disability, visual loss, dysphagia, aspiration, epilepsy, respiratory insufficiency, contractures, and nutritional failure. Recovery after established neurodegeneration is generally incomplete. Broader Leigh estimates—such as mean survival around two years after symptom onset—must be labeled syndrome-level and not reported as MC1DN6-specific. (ludwig2023contributionofneuroinflammation pages 28-32)

## 12. Treatment and real-world implementation

### Current standard

There is **no approved NDUFS2-targeted or curative therapy**. Real-world management is multidisciplinary and individualized:

- seizure treatment, avoiding valproate where POLG disease has not been excluded;
- enteral nutrition and aspiration prevention when swallowing becomes unsafe;
- physical, occupational, speech, visual, and respiratory therapy;
- treatment of dystonia/spasticity and pain;
- correction of dehydration, hypoglycemia, fever, acidosis, and catabolism during illness;
- cardiac, respiratory, hearing, ophthalmic, nutritional, and neurologic surveillance;
- anesthesia planning and an emergency illness letter.

Empiric “mitochondrial cocktails” may include thiamine, riboflavin, coenzyme Q10, or antioxidants, but no controlled NDUFS2 response rate exists. They should not be represented as disease-modifying therapy. Pharmacogenomic dosing rules specific to NDUFS2 are absent.

Suggested NCIT intervention concepts include supportive care, physical therapy, occupational therapy, speech therapy, respiratory therapy, enteral nutrition, anticonvulsant therapy, and genetic counseling; exact NCIT codes should be resolved in the target terminology service.

### Leigh-spectrum trials—not NDUFS2-specific

- **Vatiquinone/EPI-743, NCT02352896:** completed phase 2 long-term study; 30 children; January 2014–October 2023; oral 15 mg/kg up to 200 mg three times daily. NDUFS2 status and genotype-specific efficacy were not reported in the retrieved record. (NCT02352896 chunk 1)
- **EPI-743, NCT01721733:** completed randomized phase 2B trial; 35 children; 5 or 15 mg/kg three times daily versus placebo, followed by extension. No NDUFS2-stratified result was available. (NCT01721733 chunk 1)
- **Nab-sirolimus, NCT03747328:** phase 2a, withdrawn, **zero enrolled**; therefore no efficacy or safety inference is possible. (NCT03747328 chunk 1)
- **TTI-0102, NCT06990984:** phase 2a, estimated 18 participants, not yet recruiting with an anticipated 2026 start; no results and no NDUFS2-specific stratum. (NCT06990984 chunk 1)

Thus, trial participation may be considered under Leigh-spectrum eligibility, but no intervention currently has demonstrated efficacy specifically in MC1DN6.

## 13. Prevention

The molecular defect cannot be prevented by vaccination, diet, or lifestyle. **Primary genetic prevention** consists of carrier identification, reproductive counseling, prenatal diagnosis, and preimplantation genetic testing for a known familial genotype. For two carrier parents, risks per pregnancy are 25% affected, 50% carrier, and 25% unaffected/non-carrier.

**Secondary prevention** is early molecular diagnosis, cascade testing, and anticipatory surveillance. **Tertiary prevention** includes avoiding prolonged fasting/dehydration, prompt treatment of infection and catabolism, vaccination according to routine schedules, seizure control, aspiration prevention, nutritional support, contracture prevention, and respiratory/cardiac monitoring. Mitochondrial replacement therapy is not relevant to a nuclear NDUFS2 defect because replacing mtDNA does not correct the nuclear genotype.

## 14. Other species and natural disease

NDUFS2 is evolutionarily conserved across eukaryotes, and orthologues are present in standard mammalian and experimental species. No well-characterized naturally occurring companion-animal or wildlife disease equivalent to human MC1DN6 was identified, and there is no zoonotic or cross-species transmission. Veterinary breed predisposition and VBO annotations are therefore unavailable. Any animal phenotype discussed below is experimentally induced, not infectious or naturally transmitted.

## 15. Model organisms

### Ndufs2 models

- **Ndufs2+/− mouse:** approximately 50% lower transcript but no significant complex-I impairment, motor/learning deficit, histopathology, lifespan reduction, or altered metformin sensitivity; subtle cell- and tissue-specific transcriptomic changes occurred. This model supports recessive dosage dependence but poorly recapitulates severe human disease. (mcelroy2022reducedexpressionof pages 1-2, mcelroy2022reducedexpressionof pages 6-7)
- **Conditional neural-lineage knockout:** impaired neural-progenitor ATP production, proliferation, neuronal/oligodendrocyte differentiation, markedly abnormal perinatal brain development, and death before postnatal day 10. It is useful for studying developmental energy dependence but is more complete and tissue-restricted than most human hypomorphic genotypes.
- **Dopaminergic-neuron conditional knockout:** produces progressive parkinsonism and is useful for cell-specific complex-I biology, but it is not a faithful model of infantile MC1DN6.

### Cellular systems

Patient fibroblasts, CRISPR-engineered cells, iPSC-derived neurons, retinal ganglion cells, cardiomyocytes, and brain organoids would be the most genotype-faithful platforms for functional validation and drug screening. No mature NDUFS2 patient-organoid resource or standardized biobank was identified.

### Essential translational caveat

The widely used **Ndufs4−/−** Leigh mouse is not an NDUFS2 model. NDUFS4 is an accessory subunit; NDUFS2 is a catalytic core subunit. Interventions effective in Ndufs4 mice—including metabolic, hypoxic, mTOR, cannabinoid, or immune approaches—should be treated as hypothesis-generating for MC1DN6, not as disease-specific efficacy evidence. The observed normal phenotype of Ndufs2 heterozygotes further demonstrates that results cannot simply be transferred between complex-I genes. (mcelroy2022reducedexpressionof pages 1-2, mcelroy2022reducedexpressionof pages 6-7)

## Evidence gaps and curation recommendations

1. Verify the disease’s OMIM/Orphanet identifiers and all historical NDUFS2 variants directly against current OMIM, ClinVar, MANE, and gnomAD releases.
2. Do not assign Leigh-wide phenotype frequencies, prevalence, or survival estimates to MC1DN6.
3. Capture individual NDUFS2 cases with allele pair, transcript, ancestry, onset, biochemical residual activity, MRI pattern, optic phenotype, and outcome.
4. Establish genotype-matched iPSC neuronal, retinal, and cardiomyocyte models and longitudinal metabolomic/proteomic profiles.
5. Stratify future Leigh trials by causal gene and residual complex-I activity; existing trial records do not establish NDUFS2-specific benefit.

In summary, MC1DN6 is securely linked to recessive NDUFS2 dysfunction, but almost every quantitative clinical field remains underpowered. The most defensible knowledge-base representation is a core catalytic complex-I deficiency with a severe early-onset Leigh-spectrum phenotype and a possible hypomorphic optic-neuropathy presentation, accompanied by explicit low-confidence flags for phenotype frequency, epidemiology, prognosis, and treatment response. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 6, scheffler2015mitochondrialdiseaseassociated pages 18-21)

References

1. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 6): Open Targets Query (Mitochondrial complex I deficiency, nuclear type 6, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (mcelroy2022reducedexpressionof pages 1-2): Gregory S. McElroy, Ram P. Chakrabarty, Karis B. D’Alessandro, Yuan-Shih Hu, Karthik Vasan, Jerica Tan, Joshua S. Stoolman, Samuel E. Weinberg, Elizabeth M. Steinert, Paul A. Reyfman, Benjamin D. Singer, Warren C. Ladiges, Lin Gao, José Lopéz-Barneo, Karen Ridge, G. R. Scott Budinger, and Navdeep S. Chandel. Reduced expression of mitochondrial complex i subunit ndufs2 does not impact healthspan in mice. Scientific Reports, Mar 2022. URL: https://doi.org/10.1038/s41598-022-09074-3, doi:10.1038/s41598-022-09074-3. This article has 36 citations and is from a peer-reviewed journal.

3. (scheffler2015mitochondrialdiseaseassociated pages 18-21): Immo E. Scheffler. Mitochondrial disease associated with complex i (nadh-coq oxidoreductase) deficiency. Journal of Inherited Metabolic Disease, 38:405-415, May 2015. URL: https://doi.org/10.1007/s10545-014-9768-6, doi:10.1007/s10545-014-9768-6. This article has 74 citations and is from a peer-reviewed journal.

4. (ludwig2023contributionofneuroinflammation pages 28-32): K Aguilar Ludwig. Contribution of neuroinflammation to the pathology of the ndufs4 ko mouse model of leigh syndrome. Unknown journal, 2023.

5. (mcelroy2022reducedexpressionof pages 6-7): Gregory S. McElroy, Ram P. Chakrabarty, Karis B. D’Alessandro, Yuan-Shih Hu, Karthik Vasan, Jerica Tan, Joshua S. Stoolman, Samuel E. Weinberg, Elizabeth M. Steinert, Paul A. Reyfman, Benjamin D. Singer, Warren C. Ladiges, Lin Gao, José Lopéz-Barneo, Karen Ridge, G. R. Scott Budinger, and Navdeep S. Chandel. Reduced expression of mitochondrial complex i subunit ndufs2 does not impact healthspan in mice. Scientific Reports, Mar 2022. URL: https://doi.org/10.1038/s41598-022-09074-3, doi:10.1038/s41598-022-09074-3. This article has 36 citations and is from a peer-reviewed journal.

6. (NCT02352896 chunk 1):  Long-Term Safety and Efficacy Evaluation of EPI-743 in Children With Leigh Syndrome. PTC Therapeutics. 2014. ClinicalTrials.gov Identifier: NCT02352896

7. (NCT03747328 chunk 1):  ABI-009 (Nab-sirolimus) in Patients With Genetically-confirmed Leigh or Leigh-like Syndrome. Aadi Bioscience, Inc.. 2022. ClinicalTrials.gov Identifier: NCT03747328

8. (NCT01721733 chunk 1):  Safety and Efficacy Study of EPI-743 in Children With Leigh Syndrome. PTC Therapeutics. 2012. ClinicalTrials.gov Identifier: NCT01721733

9. (NCT06990984 chunk 1):  A Dose-ranging Study of TTI-0102 in Adults and Children With Leigh Syndrome Spectrum (LSS). Thiogenesis Therapeutics, Inc.. 2026. ClinicalTrials.gov Identifier: NCT06990984

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_6-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.