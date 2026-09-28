---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T11:51:16.092183'
end_time: '2026-08-27T11:58:09.817219'
duration_seconds: 413.73
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Constitutional Mismatch Repair Deficiency
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 12
  verified: 10
  not_found: 0
  unverifiable: 2
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Constitutional_Mismatch_Repair_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Constitutional Mismatch Repair Deficiency
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Constitutional Mismatch Repair Deficiency** covering all of the
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
- **Disease Name:** Constitutional Mismatch Repair Deficiency
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Constitutional Mismatch Repair Deficiency** covering all of the
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


# Constitutional Mismatch Repair Deficiency (CMMRD): comprehensive disease-characteristics report

## Executive summary

Constitutional mismatch repair deficiency is an ultrarare, autosomal-recessive, highly penetrant cancer-predisposition syndrome caused by **biallelic germline pathogenic variants in MLH1, MSH2, MSH6, or PMS2**. Unlike Lynch syndrome, in which one defective allele predisposes mainly to adult cancers, CMMRD causes mismatch-repair failure throughout normal tissues and frequently produces brain tumors, gastrointestinal cancers, and hematologic malignancies during childhood. The best contemporary natural-history dataset—an international cohort of 201 patients—reported 339 cancers in 97% of patients, 90% cumulative cancer incidence by age 18, and a median diagnostic age of 8.9 years. CNS tumors accounted for 51% of malignancies and had the poorest 10-year survival, 39%. (ercan2024clinicalandbiological pages 1-2)

The most consequential recent developments are: (1) quantitative constitutional microsatellite-instability assays such as LOGIC; (2) genotype-specific recognition of hypomorphic, later-onset CMMRD; (3) structured international surveillance; and (4) immune-checkpoint inhibition for hypermutated tumors. In a 2023 prospective pediatric nivolumab study, best overall response was 50% and two-year overall survival was 50%, with four durable complete remissions, including three malignant gliomas. (das2023efficacyofnivolumab pages 2-3, das2023efficacyofnivolumab pages 8-9)

| domain | key quantitative findings | principal recent source (author/year/journal/DOI or PMID) | ontology suggestions |
|---|---|---|---|
| Genetics / etiology | CMMRD is caused by biallelic germline pathogenic variants in mismatch repair genes **MLH1, MSH2, MSH6, PMS2**; median diagnosis age **8.9 years** in a 201-patient cohort; **PMS2 >60%** of cases, **MSH6 20-30%**, **MLH1/MSH2 10-20%**; consanguinity reported in **39-45%** of families; birth prevalence estimated at approximately **1 in 1,000,000** (ercan2024clinicalandbiological pages 1-2, shuen2025developmentofa pages 110-114, vasen2026theimpactof pages 1-2) | Ercan et al., 2024, *Lancet Oncology*, DOI: 10.1016/S1470-2045(24)00026-3; Vasen et al., 2026, *Familial Cancer*, DOI: 10.1007/s10689-026-00584-x | Gene: **MLH1, MSH2, MSH6, PMS2**; GO: **DNA mismatch repair**; MONDO: constitutional mismatch repair deficiency; HP: **Autosomal recessive inheritance** |
| Major phenotype / natural history | In the IRRDC cohort (**n=201**), **97%** developed cancer with **339 cancers** total and **90% cumulative incidence by age 18**; spectrum: **CNS 51%**, **gastrointestinal 22%**, **hematological 18%**, **other 9%**; median interval between multiple cancers **1.9 years**; dermatologic manifestations in **93%**; CNS tumors had the poorest outcome with **39% 10-year survival** vs **67%** hematologic and **89%** GI cancers (ercan2024clinicalandbiological pages 1-2) | Ercan et al., 2024, *Lancet Oncology*, PMID: **38552658**, DOI: 10.1016/S1470-2045(24)00026-3 | HP: **Cafe-au-lait macules**, **Brain neoplasm**, **Colorectal carcinoma**, **Lymphoma**, **Multiple primary neoplasms**; UBERON: **brain**, **colon**, **small intestine**, **hematopoietic system** |
| Diagnosis | Germline testing for biallelic pathogenic/likely pathogenic MMR variants is the diagnostic gold standard; non-neoplastic tissue IHC showing complete MMR protein loss has reported **>90% sensitivity** and approximately **100% specificity**; LOGIC assay was **100% sensitive and specific** in childhood cancers (**N=376**) and outperformed MSI panel (**14% sensitivity**), IHC (**86%**), and TMB (**80%**); blood/saliva DNA distinguished CMMRD from other syndromes (**n=277**) (shuen2025developmentofa pages 23-26, vasen2026theimpactof pages 6-8) | Chung et al., 2023, *Journal of Clinical Oncology*, DOI: 10.1200/JCO.21.02873; summarized in Vasen et al., 2026, *Familial Cancer*, DOI: 10.1007/s10689-026-00584-x | GO: **microsatellite instability**, **DNA mismatch repair**; HP: **Abnormality of DNA repair**; NCIT: **Immunohistochemistry**, **Whole exome sequencing**, **Whole genome sequencing** |
| Surveillance | Consensus surveillance includes **CBC every 6 months from age 1**, optional **abdominal ultrasound every 6 months from age 1**, **brain MRI every 6-12 months from age 2** (or from diagnosis/first year in some protocols), **ileocolonoscopy annually from age 6-8**, **upper endoscopy/videocapsule annually from age 8-10**, **whole-body MRI annually from age 6** or at diagnosis, and **annual gynecologic/urologic screening from age 20**; surveillance participation was associated with **79% 4-year survival** versus **15%** in non-participants, and digestive surveillance achieved **100% 5-year survival** in reported experience (shuen2025developmentofa pages 114-117, shuen2025developmentofa pages 23-26, shuen2025developmentofa pages 110-114, vasen2026theimpactof pages 6-8) | C4CMMRD/IRRDC guidance summarized in Shuen, 2025; Vasen et al., 2026, *Familial Cancer*, DOI: 10.1007/s10689-026-00584-x | NCIT: **Magnetic Resonance Imaging**, **Colonoscopy**, **Upper Gastrointestinal Endoscopy**, **Complete Blood Count**; UBERON: **brain**, **colon**, **stomach**, **small intestine**, **whole body** |
| Treatment | Immune checkpoint blockade is the major recent advance. In pediatric hypermutant/MMRD cancers treated with nivolumab (**NCT02992964**), best overall response was **50%** and **2-year OS 50%**; **4** children, including **3** with refractory malignant gliomas, achieved complete remission at median follow-up **37 months**; in registry data, objective responses were **64%** for CNS tumors and **100%** for non-CNS solid tumors with nivolumab or pembrolizumab. Temozolomide resistance is a recurring concern in MMR-deficient gliomas (das2023efficacyofnivolumab pages 2-3, das2023efficacyofnivolumab pages 8-9, vasen2026theimpactof pages 8-9) | Das et al., 2023, *Clinical Cancer Research*, DOI: 10.1158/1078-0432.CCR-23-0411; Vasen et al., 2026, *Familial Cancer*, DOI: 10.1007/s10689-026-00584-x | NCIT: **Nivolumab**, **Pembrolizumab**, **Immune Checkpoint Inhibitor Therapy**; GO: **adaptive immune response**, **T cell mediated cytotoxicity** |
| Evidence gaps / limitations | Important gaps remain in standardized confirmation of hypomorphic variants and genotype-phenotype mismatches; PMS2 testing is complicated by pseudogene interference and a high VUS burden (**49%** cited in summary evidence); some older 'likely CMMRD' categories are being abandoned in favor of conclusive molecular/functional evidence; surveillance and treatment evidence remains largely observational and registry-based, with limited prospective pediatric trial data (shuen2025developmentofa pages 110-114, vasen2026theimpactof pages 6-8, vasen2026theimpactof pages 1-2) | Gallon et al., 2024, *NPJ Precision Oncology*, DOI: 10.1038/s41698-024-00603-z; Vasen et al., 2026, *Familial Cancer*, DOI: 10.1007/s10689-026-00584-x | NCIT: **Variant of Uncertain Significance**; GO: **DNA repair**; HP: **Variable expressivity** |


*Table: This table summarizes the most actionable evidence already gathered for constitutional mismatch repair deficiency across genetics, phenotype, diagnosis, surveillance, treatment, and current evidence limitations. It is useful as a compact scaffold for a disease knowledge base entry and ontology mapping.*

## 1. Disease information

### Definition and category

CMMRD is a **hereditary DNA-repair disorder and pediatric cancer-predisposition syndrome**. Constitutional loss of MMR activity generates replication errors in normal and neoplastic cells, creating microsatellite instability (MSI), high or ultrahigh tumor mutational burden (TMB), and multiple early primary cancers. Birth prevalence is commonly estimated at approximately **1 per 1,000,000**, although ascertainment is incomplete and prevalence is substantially higher in populations with frequent consanguinity or founder alleles. More than 300 affected individuals had been published by recent consortium review. (vasen2026theimpactof pages 1-2, shuen2025developmentofa pages 6-12)

### Identifiers and synonyms

* **Preferred name:** constitutional mismatch repair deficiency.
* **Synonyms:** CMMRD; constitutional mismatch-repair deficiency syndrome; biallelic mismatch repair deficiency, BMMRD; biallelic MMR deficiency; childhood cancer syndrome; Turcot syndrome type 1 is an older, narrower designation and should not replace CMMRD.
* **OMIM phenotypic series:** entries reported for gene-defined CMMRD include **#276300, #619096, #619097, and #619101**. (munteanu2025genotypephenotypecorrelationsin pages 1-2)
* **MONDO:** use the current MONDO concept for *constitutional mismatch repair deficiency syndrome*; the exact accession should be verified against the live MONDO release before database ingestion because ontology accessions can change.
* **Orphanet:** an Orphanet CMMRD/BMMRD entity exists, but its live ORPHA accession was not independently verified in the retrieved primary literature.
* **ICD-10/ICD-11:** no sufficiently specific universal CMMRD code is established in the retrieved evidence. Coding generally combines genetic susceptibility/DNA-repair disorder and each active neoplasm. CMMRD should not be represented solely as Lynch syndrome.
* **MeSH:** no dedicated MeSH descriptor was verified; use terms for DNA mismatch repair, hereditary neoplastic syndromes, microsatellite instability, and the relevant tumors.

This report is based on **aggregated disease-level resources, international registries, published cohorts, guidelines, and trials**, not individual EHR data.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factors

The necessary upstream cause is biallelic—homozygous or compound-heterozygous—germline loss or severe reduction of function in **PMS2, MSH6, MLH1, or MSH2**. PMS2 accounts for over 60% of reported families, MSH6 for approximately 20–30%, and MLH1/MSH2 together for roughly 10–20%. MLH1/MSH2 disease tends to begin earlier and have worse survival than PMS2/MSH6 disease. Truncating or frameshift alleles generally confer more severe outcomes than missense/hypomorphic alleles. (ercan2024clinicalandbiological pages 1-2, shuen2025developmentofa pages 110-114)

### Genetic risk factors

* Two pathogenic or likely pathogenic variants **in trans** are the principal risk determinant.
* Each sibling of an affected child has, under standard Mendelian assumptions, a 25% probability of CMMRD, 50% probability of heterozygous Lynch-syndrome carrier status, and 25% probability of inheriting neither familial variant.
* Hypomorphic alleles may retain partial MMR function and produce attenuated or adult-onset disease resembling Lynch syndrome. Examples reported in 2024 include homozygous **MSH6 c.3226C>T, p.(Arg1076Cys)** and **MLH1 c.306G>A, p.(Glu102=)**; the latter caused leaky exon-3 skipping. Constitutional MSI resolved the apparent genotype–phenotype conflict.
* Consanguinity is reported in approximately **39–45%** of families. Homozygosity in apparently non-consanguineous families may reflect founder alleles. (shuen2025developmentofa pages 110-114, munteanu2025genotypephenotypecorrelationsin pages 1-2)

### Environmental and lifestyle factors

No environmental exposure, infection, diet, smoking behavior, or occupational agent is known to cause CMMRD. Age is a determinant of accumulated replication errors rather than an external cause. Lifestyle effects on penetrance have not been quantified sufficiently to recommend CMMRD-specific dietary or exercise interventions beyond general health guidance.

Treatment can modify downstream mutagenesis. Alkylating therapy, particularly temozolomide in glioma, may select MMR-deficient clones and amplify mutation burden; MMR-deficient tumor cells can also be intrinsically resistant because cytotoxic recognition of alkylator-induced mismatches requires functional MMR. This interaction argues for molecularly informed treatment selection rather than assuming that hypermutation makes all therapies effective.

### Protective factors

No validated protective germline allele or environmental intervention prevents the constitutional defect. The demonstrable protective interventions are **secondary prevention through surveillance**, prompt removal of premalignant GI lesions, and early tumor treatment. Prenatal diagnosis and preimplantation genetic testing can prevent recurrence in future pregnancies but do not treat an affected individual. (vasen2026theimpactof pages 6-8)

## 3. Phenotypes and quality-of-life burden

The 2024 IRRDC cohort provides the strongest frequency estimates: among 201 patients, 97% developed 339 cancers; cumulative incidence reached 90% by age 18; and multiple cancers were separated by a median of only 1.9 years. Tumor distribution was CNS 51%, GI 22%, hematologic 18%, and other malignancies 9%. Dermatologic findings occurred in 93%. (ercan2024clinicalandbiological pages 1-2)

### Major phenotypes

1. **CNS tumors—clinical sign/structural disease.** Predominantly high-grade glioma, with other gliomas and occasional embryonal tumors. Typical brain-tumor diagnosis is around age nine; severity is usually high and progression can be rapid. Suggested HPO: *Brain neoplasm*, *High-grade glioma*, *Headache*, *Seizure*, *Focal neurologic deficit*. Suggested UBERON: brain, cerebral hemisphere, brainstem, cerebellum. CNS tumors caused the poorest outcome: 39% 10-year survival from diagnosis. (vasen2026theimpactof pages 1-2, ercan2024clinicalandbiological pages 1-2)

2. **Gastrointestinal neoplasia—clinical/pathologic manifestation.** Adenomas, polyposis-like burden, colorectal carcinoma, and small-intestinal or upper-GI cancers can occur in childhood or adolescence. GI tumors represented 22% of cancers; later-onset PMS2-CMMRD appears relatively enriched for GI disease. Suggested HPO: *Gastrointestinal neoplasm*, *Colorectal carcinoma*, *Intestinal polyposis*, *Gastrointestinal hemorrhage*, *Abdominal pain*. GI-cancer 10-year survival was 89% in the international cohort. (ercan2024clinicalandbiological pages 1-2, munteanu2025genotypephenotypecorrelationsin pages 1-2)

3. **Hematologic malignancy—laboratory/clinical manifestation.** T-cell lymphoblastic lymphoma is particularly characteristic; leukemia and other lymphomas occur, often at very young ages. Suggested HPO: *Lymphoma*, *Leukemia*, *Anemia*, *Thrombocytopenia*, *Lymphadenopathy*. Hematologic cancers represented 18%, with 67% 10-year survival. An early series documented hematologic malignancy between 14 months and six years. (ercan2024clinicalandbiological pages 1-2, wimmer2017connectionsbetweenconstitutional pages 4-6)

4. **NF1-like pigmentary phenotype—physical sign.** Multiple café-au-lait macules, altered pigmentation, axillary/intertriginous freckling, and occasional neurofibroma-like lesions commonly precede cancer. Suggested HPO: *Café-au-lait macule* (HP:0000957), *Axillary freckling*, *Abnormal skin pigmentation*, *Neurofibroma*. Dermatologic signs in 93% make them clinically valuable but not specific. (ercan2024clinicalandbiological pages 1-2, wimmer2017connectionsbetweenconstitutional pages 4-6)

5. **Multiple primary malignancies—temporal phenotype.** Synchronous or metachronous tumors are a defining burden. Recent review estimates synchronous cancers in as many as 25%, with approximately two years to a new malignancy. Suggested HPO: *Multiple primary neoplasms*. (vasen2026theimpactof pages 8-9)

6. **Other tumors.** Sarcomas, embryonal tumors, and assorted Lynch-spectrum malignancies occur less often. Suggested HPO should be assigned at histology/site level rather than using a nonspecific cancer term.

### Quality of life

No validated CMMRD-specific EQ-5D, SF-36, or PROMIS population estimates were identified. Expected burden is nevertheless profound: repeated anesthesia and imaging, six- to twelve-month surveillance, colonoscopy from early childhood, major surgery, neurocognitive effects of CNS tumors and therapy, endocrine/neurologic sequelae, chronic fear of another cancer, interrupted schooling, and familial grief. Quality-of-life effects should be recorded as an evidence gap rather than inferred as quantified outcomes.

## 4. Genetic and molecular information

### Causal genes and proteins

* **MSH2–MSH6 (MutSα):** recognizes base substitutions and small insertion/deletion loops.
* **MLH1–PMS2 (MutLα):** coordinates excision, resynthesis, and repair after mismatch recognition.
* Loss of either binding partner may destabilize its partner and create paired IHC loss patterns.

Suggested GO annotations include **DNA mismatch repair (GO:0006298)**, mismatch recognition, postreplicative DNA repair, DNA repair complex, and maintenance of genome stability.

### Variant classes and interpretation

Pathogenic CMMRD variants include nonsense, frameshift, essential splice, exon-level deletion/duplication, structural, and functionally damaging missense variants. Their origin is **germline**; additional somatic variants drive each tumor. A VUS is not diagnostic without segregation, RNA/protein/function, constitutional MSI, or other compelling evidence. Approximately 30% VUS burden has been reported in diagnostic series, and PMS2 is particularly difficult, with a cited VUS rate of 49%. PMS2CL and other pseudogene sequences require long-range PCR, locus-specific NGS, or validated hybrid methods to avoid false assignment. (shuen2025developmentofa pages 110-114, shuen2025developmentofa pages 114-117, shuen2025developmentofa pages 23-26)

Population frequencies of individual causal alleles vary and must be retrieved variant-by-variant from the current gnomAD release. Fully penetrant severe biallelic genotypes are expected to be rare; allele frequency alone cannot classify hypomorphic or founder variants.

### Modifier genes and chromosomal abnormalities

Acquired polymerase-proofreading mutations in **POLE/POLD1** can convert an already hypermutated tumor to an ultrahypermutated state. Genotype, residual MMR activity, variant class, affected organ, treatment history, and age modify expression. No separate, clinically validated constitutional modifier-gene panel is established. Recurrent aneuploidy or translocation is not the primary cause; copy-number variants disrupting an MMR gene can, however, constitute one causal allele.

### Epigenetics and omics

CMMRD-associated high-grade gliomas have distinctive methylation and hypomethylation patterns, supporting classification as replication-repair-deficient tumors rather than ordinary adult glioblastoma. Molecularly, all cancers in the 2024 international cohort showed high mutation burdens and characteristic mutational signatures. Constitutional instability differs by tissue—reported as GI greater than blood greater than brain—and increases longitudinally, suggesting a quantitative molecular clock. (ercan2024clinicalandbiological pages 1-2, vasen2026theimpactof pages 6-8)

Routine diagnostic transcriptomics, proteomics, metabolomics, lipidomics, single-cell, or spatial-transcriptomic tests are not established. RNA sequencing is useful selectively for splice variants. No reproducible systemic metabolic or lipidomic signature is currently suitable for knowledge-base assertion.

## 5. Environmental information

CMMRD is neither infectious nor environmentally acquired and has no zoonotic transmission. Environmental toxicants, pollution, alcohol, smoking, diet, and exercise have not been shown to alter penetrance sufficiently for disease-specific estimates. Ionizing radiation and mutagenic chemotherapy warrant individualized risk–benefit review because patients already have deficient genome maintenance, but necessary radiotherapy is not categorically contraindicated. Vaccination should follow routine schedules unless active cancer therapy or immunosuppression requires modification.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream inherited defect:** both alleles of an MMR gene are defective in the germ line.
2. **Protein-complex failure:** deficient MutSα or MutLα impairs recognition or excision of polymerase replication errors.
3. **Constitutional genomic instability:** base substitutions and insertion/deletion loops accumulate, particularly at microsatellites.
4. **Driver acquisition:** proliferative tissues acquire oncogenic and tumor-suppressor mutations; somatic POLE/POLD1 proofreading defects may cause ultrahypermutation.
5. **Clonal evolution:** neural progenitors/glial cells, intestinal epithelial stem cells, and lymphoid precursors transform, accounting for CNS, GI, and hematologic predominance.
6. **Immune consequence:** high mutation burden generates neoantigens and can recruit activated CD8-positive T cells, creating susceptibility to PD-1 blockade. Responses are heterogeneous because antigen presentation, tumor lineage, CNS microenvironment, regulatory T cells, steroid exposure, and IDH-associated immune suppression can counteract immunogenicity.
7. **Clinical outcome:** early, recurrent, synchronous, or metachronous malignancy produces neurologic, GI, hematologic, and systemic manifestations. (shuen2025developmentofa pages 6-12, shuen2025developmentofa pages 34-37, das2023efficacyofnivolumab pages 2-3)

Suggested GO terms: DNA mismatch repair; DNA replication; response to DNA damage stimulus; somatic mutation; regulation of cell cycle; apoptotic process; antigen processing and presentation; adaptive immune response; T-cell-mediated cytotoxicity. Suggested Cell Ontology concepts: neural stem/progenitor cell, astrocyte lineage cell, intestinal epithelial stem cell, colonocyte, enterocyte, thymocyte, T lymphocyte, B lymphocyte, hematopoietic stem/progenitor cell, CD8-positive alpha-beta T cell.

### Experimental vulnerabilities

WRN helicase inhibition is synthetically lethal in MSI-high cells: repeat-derived secondary structures stall replication forks and, without WRN resolution, undergo MUS81–EME1 cleavage and p53/PUMA-dependent apoptosis. ATR inhibition and combined ATR/WRN/PD-1 strategies remain preclinical. These are mechanistically compelling but are not approved CMMRD therapies. (shuen2025developmentofa pages 34-37)

## 7. Anatomical structures affected

Primary organs are the **brain/CNS**, colon and rectum, small intestine, stomach/upper GI tract, bone marrow, thymus, lymph nodes, spleen, and skin. Other solid-organ involvement is tumor-dependent. Suggested UBERON mappings include brain, cerebral cortex, brainstem, cerebellum, colon, rectum, small intestine, stomach, bone marrow, thymus, lymph node, spleen, and skin.

At tissue level, affected populations include glial/neural progenitors, intestinal crypt stem cells and epithelium, and lymphoid progenitors. At subcellular level, MMR functions principally in the **nucleus** at newly replicated chromatin; suggested GO cellular components are nucleus, chromosome, replication fork, and mismatch-repair complex. Lateralization is not intrinsic: CNS tumors can be unilateral or midline depending on tumor site, while GI and hematologic disease is not meaningfully lateralized.

## 8. Temporal development and course

The defect is congenital, but clinical onset is typically pediatric and often insidious until cancer symptoms emerge. Mean/median first-cancer age is approximately nine to ten years; about 80–90% develop cancer by age 18. Hematologic disease may occur in infancy or early childhood, CNS tumors commonly around school age, and GI carcinoma more often in later childhood/adolescence. Hypomorphic genotypes can delay onset into adulthood. (vasen2026theimpactof pages 1-2, ercan2024clinicalandbiological pages 1-2, shuen2025developmentofa pages 6-12)

CMMRD is lifelong, progressive at the predisposition level, and characterized by repeated tumor episodes rather than continuous activity of a single disease. Remission is tumor- and therapy-induced, but remission from one cancer does not remove the risk of another. Critical intervention windows begin at molecular diagnosis—ideally before the first cancer—and after every cancer diagnosis, when staging should actively search for synchronous tumors.

## 9. Inheritance and population

Inheritance is **autosomal recessive**, with high but genotype- and age-dependent penetrance. In the largest cohort, 97% had cancer and cumulative incidence reached 90% by age 18, approaching complete lifetime penetrance. Expressivity is highly variable, particularly for PMS2/MSH6 and hypomorphic alleles. Genetic anticipation is not established. Germline mosaicism is possible in principle but is not a recognized major mechanism.

The estimated prevalence is about one birth per million, but no robust population-based incidence per 100,000 person-years is available. Consanguinity and founder effects produce geographic clustering; CMMRD should nevertheless be considered in every ancestry. No consistent biological sex predominance is established. In a high-consanguinity Pakistani pediatric high-grade-glioma cohort published after the requested 2023–2024 priority window, 15/47 (31.9%) tested positive for CMMRD, illustrating enrichment in selected populations rather than general prevalence.

Parents and many relatives are heterozygous MMR-variant carriers and require Lynch-syndrome counseling and adult surveillance. Carrier frequency is gene-, ancestry-, and variant-specific; it should not be inferred from the CMMRD birth-prevalence estimate.

## 10. Diagnostics

### When to suspect CMMRD

Suspect CMMRD in a child or young adult with high-grade glioma, T-lymphoblastic lymphoma, early GI adenoma/carcinoma, multiple primary cancers, marked tumor hypermutation, constitutional MSI, NF1-like pigmentary findings without an explanatory NF1/SPRED1 variant, consanguinity, or parents with cancers compatible with Lynch syndrome. C4CMMRD clinical scoring historically used a threshold of at least three points to trigger testing, but contemporary practice seeks conclusive molecular/functional confirmation. (shuen2025developmentofa pages 114-117, shuen2025developmentofa pages 23-26)

### Recommended testing workflow

1. **Pretest genetic counseling and paired blood/tumor review.** Document three-generation pedigree, consanguinity, pathology, prior therapies, and pigmentary findings.
2. **Tumor testing:** IHC for MLH1, PMS2, MSH2, and MSH6; MSI by NGS or PCR; and tumor sequencing/TMB. Conventional adult colorectal MSI panels can be insensitive in pediatric/CNS CMMRD tumors and must not exclude the diagnosis.
3. **Germline multigene panel:** sequence and deletion/duplication analysis of all four genes, not only the protein absent by IHC. Confirm that variants are in trans through parental testing. Use locus-specific PMS2 methods.
4. **Ancillary confirmation:** MMR IHC in normal tissue, constitutional MSI from blood/saliva, lymphoblastoid-cell functional assays, methylating-agent tolerance, or low-pass WGS/LOGIC where available.
5. **RNA studies:** resolve suspected splice variants or hypomorphic alleles.
6. **WES/WGS:** useful after negative/inconclusive panels, for structural/deep-intronic variants and alternative syndromes. WGS may simultaneously support constitutional MSI analysis. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion assays are not first-line unless another diagnosis is suspected.

Normal-tissue IHC has reported sensitivity above 90% and specificity near 100%, but missense proteins may retain staining. Germline biallelic P/LP variants remain the central diagnostic standard. In 376 childhood cancers, the 2023 LOGIC assay was reported as 100% sensitive and specific, compared with sensitivities of 14% for a conventional MSI panel, 86% for IHC, and 80% for TMB; it also distinguished CMMRD from other predisposition syndromes using blood/saliva DNA in 277 individuals. (shuen2025developmentofa pages 23-26, vasen2026theimpactof pages 6-8)

The authors’ key abstract conclusion was: **“LOGIC was a robust tool for the diagnosis of MMRD in multiple cancer types and in normal tissues.”** This assay remains specialized rather than universally available.

### Differential diagnosis

* **Lynch syndrome:** monoallelic variant, predominantly adult-onset tumors, no generalized constitutional MMR deficiency.
* **NF1 or Legius syndrome:** pigmentary findings with NF1/SPRED1 alteration; lacks constitutional MSI and the characteristic CMMRD tumor spectrum.
* **Polymerase-proofreading-associated polyposis/POLE-POLD1 disorder:** hypermutation/polyposis without biallelic MMR variants.
* **Familial adenomatous polyposis/MUTYH-associated polyposis:** different polyp pattern and causal genes.
* **Li–Fraumeni syndrome:** broad childhood tumor spectrum from TP53, generally without constitutional MSI/MMR-protein loss.
* Other DNA-repair disorders, immunodeficiency-associated lymphoma, and sporadic pediatric cancer.

## 11. Outcome and prognosis

The 201-patient IRRDC cohort provides current benchmarks: 10-year survival from tumor diagnosis was **39% for CNS**, **67% for hematologic**, **89% for GI**, and **96% for other tumors**. Survival by age 15 was reported as 0% for MSH2, 19% for MLH1, 49% for MSH6, and 63% for PMS2 genotypes, although these estimates may be affected by small gene-specific samples and ascertainment. (ercan2024clinicalandbiological pages 1-2)

Prognostic factors include causal gene, residual protein function, truncating versus missense variant, age and type of first cancer, CNS involvement, stage/resectability, synchronous malignancy, polymerase-proofreading status, TMB/MSI pattern, immune microenvironment, and access to surveillance and immunotherapy. Surveillance has been associated with 79% four-year survival versus 15% without program participation; digestive surveillance achieved 100% five-year survival in reported consortium experience. These nonrandomized data are vulnerable to lead-time and ascertainment bias but strongly support surveillance. (vasen2026theimpactof pages 6-8)

Long-term morbidity includes neurologic and cognitive disability, endocrine effects, GI surgery consequences, marrow toxicity, immune-related adverse events, and repeated-cancer burden. Recovery from an individual cancer is possible; cure of the inherited predisposition is not currently possible.

## 12. Treatment

### General strategy

Management should occur through a multidisciplinary pediatric/AYA cancer-predisposition team. Treat each tumor according to histology, stage, resectability, molecular profile, previous therapy, and competing synchronous cancer, while recognizing MMR-associated drug resistance and eligibility for tumor-agnostic immunotherapy.

* **Surgery:** maximal safe resection of CNS tumors; endoscopic polypectomy and segmental or more extensive bowel surgery according to burden; diagnostic/therapeutic surgery for other solid tumors. Suggested NCIT: *Surgical Resection*, *Polypectomy*, *Colectomy*.
* **Radiotherapy:** used when oncologically indicated, especially for CNS disease, with individualized discussion of late effects and second malignancies. Suggested NCIT: *Radiation Therapy*.
* **Chemotherapy:** histology-specific regimens remain relevant, particularly for hematologic malignancies. Temozolomide efficacy can be reduced in MMR-deficient glioma; treatment should not be selected reflexively without molecular review.
* **Supportive care:** antiemetics, analgesia, nutrition, seizure control, infection prophylaxis, transfusion support, rehabilitation, neuropsychology, fertility preservation, and psychosocial care.

### Immune-checkpoint inhibition

PD-1 inhibitors—principally **nivolumab** and **pembrolizumab**—are the most important targeted treatment because hypermutation creates neoantigens. In NCT02992964, patients aged at least 12 months but under 25 years with refractory MMRD and/or TMB ≥5 mutations/Mb received nivolumab 3 mg/kg every two weeks for up to 24 months. Best overall response was 50%, versus an initial objective response of 20%, illustrating delayed immune responses; two-year OS was 50% (95% CI 27–93). Four children, including three with refractory malignant glioma, were in complete remission at median 37-month follow-up. All five responders were MMR deficient, and responders had greater CD8-positive T-cell clonality/diversity. (das2023efficacyofnivolumab pages 2-3, das2023efficacyofnivolumab pages 8-9)

The abstract’s central conclusion was: **“Nivolumab resulted in durable responses and prolonged survival … in refractory hypermutated cancers including malignant gliomas.”** Registry experience subsequently reported objective responses of 64% in CNS tumors and 100% in non-CNS solid tumors treated with nivolumab or pembrolizumab, although registry selection and small samples limit comparison. (vasen2026theimpactof pages 8-9)

Suggested NCIT terms: *Nivolumab*, *Pembrolizumab*, *Atezolizumab*, *PD-1 Inhibitor*, *Immune Checkpoint Inhibitor Therapy*. Toxicities include dermatitis, colitis, hepatitis, pneumonitis, thyroiditis and other endocrinopathies, neurologic toxicity, and rare severe autoimmune disease. CMMRD-associated autoimmune susceptibility deserves careful baseline assessment and monitoring. (shuen2025developmentofa pages 34-37)

### Trials and experimental treatment

* **NCT02992964:** nivolumab pilot in pediatric hypermutant cancers; phase I/II; terminated after small enrollment but generated the published efficacy cohort.
* **NCT05770102 (DETERMINE arm 02):** recruiting phase II/III platform arm of atezolizumab for high-TMB, MSI-high, or proven CMMRD cancers; planned enrollment 30.
* **NCT05722886:** recruiting DETERMINE master protocol; planned enrollment 825 across molecularly defined rare cancers.
* **NCT02359565:** active, not recruiting phase I pembrolizumab study in younger patients with recurrent/refractory CNS tumors, including hypermutated brain tumors; enrollment 71.
* **NCT04500548:** nivolumab plus ipilimumab 3CI study; withdrawn with zero enrollment.
* WRN or ATR inhibition, combined DNA-damage/ICI therapy, neoantigen/frameshift-peptide vaccines, and MMR-independent alkylators remain experimental. (shuen2025developmentofa pages 34-37)

No gene replacement, CRISPR correction, RNA therapy, or preventive hematopoietic cell therapy is established. Pharmacogenomic management presently centers on tumor MMR/TMB/MSI and somatic drivers rather than CYP-based CMMRD-specific dosing.

## 13. Prevention and surveillance

### Primary prevention

The inherited defect cannot currently be reversed. Prevention focuses on genetic counseling, cascade testing, avoidance of tobacco and unnecessary mutagenic exposure, and reproductive options. For known familial variants, prenatal testing and preimplantation genetic testing are technically feasible. Heterozygous relatives should receive Lynch-syndrome management. (vasen2026theimpactof pages 6-8)

### Secondary prevention: consensus surveillance

Schedules vary slightly between C4CMMRD, ERN GENTURIS, AACR, and local protocols; individualization is essential.

* Clinical review and neurologic examination: every six months from diagnosis.
* **CBC:** every six months from age one for leukemia/hematologic disease.
* **Abdominal ultrasound:** every six months from age one is optional because sensitivity is limited.
* **Brain MRI:** every six months from diagnosis/approximately age two through age 20; some protocols permit six- to twelve-month intervals.
* **Ileocolonoscopy:** annually beginning at age six to eight; shorten to six months when polyps are found.
* **Upper GI endoscopy and video-capsule small-bowel examination:** annually beginning around age eight to ten.
* **Whole-body MRI:** baseline at diagnosis and, in some protocols, annually from age six.
* **Gynecologic examination with transvaginal ultrasound:** annually from age 20, adapted to maturity and preference.
* **Urinalysis/urine cytology or other urologic review:** annually from age 20, recognizing limited evidence.

Presymptomatic detection has been associated with five-year survival of 72% versus 33% for symptom-detected brain tumors and 100% versus 81% for GI cancers. (shuen2025developmentofa pages 114-117, shuen2025developmentofa pages 23-26, shuen2025developmentofa pages 110-114)

### Tertiary prevention

After any cancer, continue full surveillance rather than site-limited follow-up because the median interval to another primary is approximately two years. Monitor treatment-related neurologic, endocrine, cardiac, GI, fertility, immune, and psychosocial complications. There is no CMMRD-specific prophylactic medication or vaccine in standard practice.

## 14. Other species and natural disease

CMMRD is a human syndrome; no common naturally occurring veterinary counterpart with comparable surveillance relevance was established in the retrieved evidence. Orthologous MMR genes are deeply conserved in mammals and model organisms. Suggested taxa for comparative annotations include **Homo sapiens (NCBI Taxon 9606)** and **Mus musculus (10090)**. Dogs and other mammals can develop sporadic or hereditary MMR-deficient tumors, but these should not automatically be labeled natural CMMRD without demonstrated biallelic germline loss.

There is no infectious transmission, zoonotic potential, or cross-species contagion.

## 15. Model organisms and experimental systems

### Available models

* **Mouse:** germline, constitutive, and tissue-conditional Mlh1, Msh2, Msh6, or Pms2 knockout models; combinations with oncogenic drivers or polymerase-proofreading defects model lymphoma, intestinal neoplasia, and replication-repair-deficient glioma.
* **Cellular:** patient-derived lymphoblastoid cells, fibroblasts, tumor cultures, engineered MMR-knockout lines, and organoids. These support functional variant classification, methylating-agent tolerance, MSI quantification, drug screening, and synthetic-lethality studies.
* **Invertebrate/yeast:** conserved MMR systems in Saccharomyces, Drosophila, and C. elegans permit mechanistic studies, but they do not reproduce the complete human tumor spectrum.

### Recapitulation and limitations

Models reproduce constitutional replication errors, MSI, elevated mutation burden, lymphoid or intestinal tumor susceptibility, and treatment resistance. They incompletely reproduce the human distribution and timing of pediatric CNS, GI, and hematologic cancers; complete loss of some genes may produce species-specific viability or tumor spectra. Human immune-checkpoint response also depends on HLA/neoantigen and tumor-microenvironment features absent from many models.

Primary applications include pathogenicity assessment, mutational-signature analysis, identification of POLE/POLD1-driven ultrahypermutation, immunotherapy biomarkers, and WRN/ATR synthetic lethality. Relevant resources include MGI, IMPC, KOMP, IMSR/MMRRC, Cellosaurus, ATCC, and patient-derived model repositories.

## Evidence appraisal and knowledge gaps

The 2024 IRRDC study is the strongest available natural-history source but remains an international referral cohort rather than a population-based registry. Most surveillance estimates are observational and susceptible to lead-time bias. Immunotherapy evidence is encouraging but comes from small prospective and registry cohorts. Variant-specific penetrance, population carrier frequencies, sex effects, quality-of-life metrics, metabolomic/proteomic biomarkers, standardized adult surveillance, and natural veterinary disease remain insufficiently characterized.

Authoritative source details include Ercan et al., *Lancet Oncology*, published May 2024, PMID **38552658**, DOI/URL: https://doi.org/10.1016/S1470-2045(24)00026-3; Chung et al., *Journal of Clinical Oncology*, published February 2023, DOI/URL: https://doi.org/10.1200/JCO.21.02873; Das et al., *Clinical Cancer Research*, published May 2023, DOI/URL: https://doi.org/10.1158/1078-0432.CCR-23-0411; Gallon et al., *NPJ Precision Oncology*, published May 2024, DOI/URL: https://doi.org/10.1038/s41698-024-00603-z; and Guerrini-Rousseau et al., *Familial Cancer*, published July 2024, DOI/URL: https://doi.org/10.1007/s10689-024-00403-1.

References

1. (ercan2024clinicalandbiological pages 1-2): Ayse Bahar Ercan, Melyssa Aronson, Nicholas R Fernandez, Yuan Chang, Adrian Levine, Zhihui Amy Liu, Logine Negm, Melissa Edwards, Vanessa Bianchi, Lucie Stengs, Jiil Chung, Abeer Al-Battashi, Agnes Reschke, Alex Lion, Alia Ahmad, Alvaro Lassaletta, Alyssa T Reddy, Amir F Al-Darraji, Amish C Shah, An Van Damme, Anne Bendel, Aqeela Rashid, Ashley S Margol, Bethany L Kelly, Bojana Pencheva, Brandie Heald, Brianna Lemieux-Anglin, Bruce Crooks, Carl Koschmann, Catherine Gilpin, Christopher C Porter, David Gass, David Samuel, David S Ziegler, Deborah T Blumenthal, Dennis John Kuo, Dima Hamideh, Donald Basel, Dong-Anh Khuong-Quang, Duncan Stearns, Enrico Opocher, Fernando Carceller, Hagit Baris Feldman, Helen Toledano, Ira Winer, Isabelle Scheers, Ivana Fedorakova, Jack M Su, Jaime Vengoechea, Jaroslav Sterba, Jeffrey Knipstein, Jordan R Hansford, Julieta Rita Gonzales-Santos, Kanika Bhatia, Kevin J Bielamowicz, Khurram Minhas, Kim E Nichols, Kristina A Cole, Lynette Penney, Magnus Aasved Hjort, Magnus Sabel, Maria Joao Gil-da-Costa, Matthew J Murray, Matthew Miller, Maude L Blundell, Maura Massimino, Maysa Al-Hussaini, Mazin F Al-Jadiry, Melanie A Comito, Michael Osborn, Michael P Link, Michal Zapotocky, Mithra Ghalibafian, Najma Shaheen, Naureen Mushtaq, Nicolas Waespe, Nobuko Hijiya, Noemi Fuentes-Bolanos, Olfat Ahmad, Omar Chamdine, Paromita Roy, Pavel N Pichurin, Per Nyman, Rachel Pearlman, Rebecca C Auer, Reghu K Sukumaran, Rejin Kebudi, Rina Dvir, Robert Raphael, Ronit Elhasid, Rose B McGee, Rose Chami, Ryan Noss, Ryuma Tanaka, Salmo Raskin, Santanu Sen, Scott Lindhorst, Sebastien Perreault, Shani Caspi, Shazia Riaz, Shlomi Constantini, Sophie Albert, Stanley Chaleff, Stefan Bielack, Stefano Chiaravalli, Stuart Louis Cramer, Sumita Roy, Suzanne Cahn, Suzanne Penna, Syed Ahmer Hamid, Tariq Ghafoor, Uzma Imam, Valerie Larouche, Vanan Magimairajan Issai, William D Foulkes, Yi Yen Lee, Paul C Nathan, Yosef E Maruvka, Mary-Louise C Greer, Carol Durno, Adam Shlien, Birgit Ertl-Wagner, Anita Villani, David Malkin, Cynthia Hawkins, Eric Bouffet, Anirban Das, and Uri Tabori. Clinical and biological landscape of constitutional mismatch-repair deficiency syndrome: an international replication repair deficiency consortium cohort study. May 2024. URL: https://doi.org/10.1016/s1470-2045(24)00026-3, doi:10.1016/s1470-2045(24)00026-3. This article has 91 citations and is from a highest quality peer-reviewed journal.

2. (das2023efficacyofnivolumab pages 2-3): Anirban Das, Uri Tabori, Lauren C. Sambira Nahum, Natalie B. Collins, Rebecca Deyell, Rina Dvir, Cecile Faure-Conter, Timothy E. Hassall, Jane E. Minturn, Melissa Edwards, Elissa Brookes, Vanessa Bianchi, Adrian Levine, Simone C. Stone, Sumedha Sudhaman, Santiago Sanchez Ramirez, Ayse B. Ercan, Lucie Stengs, Jill Chung, Logine Negm, Gad Getz, Yosef E. Maruvka, Birgit Ertl-Wagner, Pamela S. Ohashi, Trevor Pugh, Cynthia Hawkins, Eric Bouffet, and Daniel A. Morgenstern. Efficacy of nivolumab in pediatric cancers with high mutation burden and mismatch repair deficiency. Clinical Cancer Research, 29:4770-4783, May 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-0411, doi:10.1158/1078-0432.ccr-23-0411. This article has 77 citations and is from a highest quality peer-reviewed journal.

3. (das2023efficacyofnivolumab pages 8-9): Anirban Das, Uri Tabori, Lauren C. Sambira Nahum, Natalie B. Collins, Rebecca Deyell, Rina Dvir, Cecile Faure-Conter, Timothy E. Hassall, Jane E. Minturn, Melissa Edwards, Elissa Brookes, Vanessa Bianchi, Adrian Levine, Simone C. Stone, Sumedha Sudhaman, Santiago Sanchez Ramirez, Ayse B. Ercan, Lucie Stengs, Jill Chung, Logine Negm, Gad Getz, Yosef E. Maruvka, Birgit Ertl-Wagner, Pamela S. Ohashi, Trevor Pugh, Cynthia Hawkins, Eric Bouffet, and Daniel A. Morgenstern. Efficacy of nivolumab in pediatric cancers with high mutation burden and mismatch repair deficiency. Clinical Cancer Research, 29:4770-4783, May 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-0411, doi:10.1158/1078-0432.ccr-23-0411. This article has 77 citations and is from a highest quality peer-reviewed journal.

4. (shuen2025developmentofa pages 110-114): AY Shuen. Development of a diagnostic functional assay for constitutional mismatch repair deficiency. Unknown journal, 2025.

5. (vasen2026theimpactof pages 1-2): Hans F. A. Vasen, Katharina Wimmer, Mariëtte van Kouwen, Léa Guerrini-Rousseau, Daniela Gattini, Lucie Stengs, Uri Tabori, Chrystelle Colas, and Anirban Das. The impact of international care networks on the clinical management of constitutional mismatch repair deficiency (cmmrd): a review of recent developments. Jun 2026. URL: https://doi.org/10.1007/s10689-026-00584-x, doi:10.1007/s10689-026-00584-x. This article has 0 citations and is from a peer-reviewed journal.

6. (shuen2025developmentofa pages 23-26): AY Shuen. Development of a diagnostic functional assay for constitutional mismatch repair deficiency. Unknown journal, 2025.

7. (vasen2026theimpactof pages 6-8): Hans F. A. Vasen, Katharina Wimmer, Mariëtte van Kouwen, Léa Guerrini-Rousseau, Daniela Gattini, Lucie Stengs, Uri Tabori, Chrystelle Colas, and Anirban Das. The impact of international care networks on the clinical management of constitutional mismatch repair deficiency (cmmrd): a review of recent developments. Jun 2026. URL: https://doi.org/10.1007/s10689-026-00584-x, doi:10.1007/s10689-026-00584-x. This article has 0 citations and is from a peer-reviewed journal.

8. (shuen2025developmentofa pages 114-117): AY Shuen. Development of a diagnostic functional assay for constitutional mismatch repair deficiency. Unknown journal, 2025.

9. (vasen2026theimpactof pages 8-9): Hans F. A. Vasen, Katharina Wimmer, Mariëtte van Kouwen, Léa Guerrini-Rousseau, Daniela Gattini, Lucie Stengs, Uri Tabori, Chrystelle Colas, and Anirban Das. The impact of international care networks on the clinical management of constitutional mismatch repair deficiency (cmmrd): a review of recent developments. Jun 2026. URL: https://doi.org/10.1007/s10689-026-00584-x, doi:10.1007/s10689-026-00584-x. This article has 0 citations and is from a peer-reviewed journal.

10. (shuen2025developmentofa pages 6-12): AY Shuen. Development of a diagnostic functional assay for constitutional mismatch repair deficiency. Unknown journal, 2025.

11. (munteanu2025genotypephenotypecorrelationsin pages 1-2): Cătălin Vasile Munteanu, Diana Luisa Lighezan, Alexandru Capcelea, Adela Chiriță-Emandi, and Adrian Pavel Trifa. Genotype-phenotype correlations in pms2-associated constitutional mismatch repair deficiency: a systematic literature review. Oncology Reviews, Nov 2025. URL: https://doi.org/10.3389/or.2025.1679576, doi:10.3389/or.2025.1679576. This article has 1 citations.

12. (wimmer2017connectionsbetweenconstitutional pages 4-6): K. Wimmer, T. Rosenbaum, and L. Messiaen. Connections between constitutional mismatch repair deficiency syndrome and neurofibromatosis type 1. Clinical Genetics, 91:507-519, Apr 2017. URL: https://doi.org/10.1111/cge.12904, doi:10.1111/cge.12904. This article has 144 citations and is from a peer-reviewed journal.

13. (shuen2025developmentofa pages 34-37): AY Shuen. Development of a diagnostic functional assay for constitutional mismatch repair deficiency. Unknown journal, 2025.

## Artifacts

- [Edison artifact artifact-00](Constitutional_Mismatch_Repair_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 2 |
| References weighed for topical relevance | 10 |
| On topic | 5 |
| Off topic | 0 |

10 of 12 references resolved; the rest could not be looked up either way.