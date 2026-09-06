---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T22:04:07.491541'
end_time: '2026-08-26T22:21:40.914917'
duration_seconds: 1053.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Isolated Growth Hormone Deficiency
  mondo_id: ''
  category: Endocrine
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
reference_validation:
  total_references: 12
  verified: 11
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.083
  relevance_assessed: 11
  on_topic: 5
  unresolved_references:
  - DOI:10.17458/per.vol16.2018.dd.geneticmutationsghigf
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Isolated_Growth_Hormone_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Isolated Growth Hormone Deficiency
- **MONDO ID:**  (if available)
- **Category:** Endocrine

## Research Objectives

Please provide a comprehensive research report on **Isolated Growth Hormone Deficiency** covering all of the
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
- **Disease Name:** Isolated Growth Hormone Deficiency
- **MONDO ID:**  (if available)
- **Category:** Endocrine

## Research Objectives

Please provide a comprehensive research report on **Isolated Growth Hormone Deficiency** covering all of the
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


# Isolated Growth Hormone Deficiency: Comprehensive Disease-Characteristics Report

## Executive summary

Isolated growth hormone deficiency (IGHD) is deficient secretion or biological availability of pituitary growth hormone (GH) without another pituitary hormone deficiency at presentation. It is the most common childhood pituitary hormone deficiency, with an estimated incidence of **1 per 4,000–10,000 live births**; only **3–30%** of cases are familial, and most childhood cases are classified as idiopathic. Congenital genetic, structural, acquired, and idiopathic forms all occur. The cardinal pediatric phenotype is proportionate postnatal short stature with reduced height velocity and delayed skeletal maturation. Neonatal disease may instead present with hypoglycemia, prolonged jaundice, or micropenis. Diagnosis remains probabilistic because stimulated GH cutoffs are assay- and protocol-dependent, obesity suppresses test responses, and many children labeled idiopathic do not remain GH deficient when retested after growth completion. Recombinant human GH (rhGH; somatropin) is effective, while weekly long-acting preparations are increasingly used to reduce injection burden. Recent 2023–2024 work has expanded the **GH1** variant spectrum, quantified dental abnormalities, developed transcriptomic response predictors, and evaluated oral GH secretagogues and oral macimorelin diagnostic testing. (ibba2024isolatedgrowthhormone pages 1-2, ibba2024isolatedgrowthhormone pages 8-9)

The following table provides a compact structured summary for knowledge-base ingestion.

| Domain/subtype | Key gene or feature | Inheritance/mechanism | Defining phenotype/diagnostic clue | Suggested ontology terms | Evidence note |
|---|---|---|---|---|---|
| Disease entity | Isolated growth hormone deficiency (IGHD) | Pituitary GH deficiency occurring as congenital/genetic, acquired, or idiopathic isolated deficiency | Short stature, reduced growth velocity, delayed bone age; neonatal cases may show hypoglycemia/jaundice/micropenis | MONDO: isolated congenital growth hormone deficiency (MONDO_0000050); HPO: Short stature, Delayed bone age, Hypoglycemia, Micropenis; UBERON: pituitary gland, hypothalamus | Incidence ~1:4,000-10,000 live births; most cases idiopathic; familial 3-30% (ibba2024isolatedgrowthhormone pages 1-2, ibba2024isolatedgrowthhormone pages 2-4) |
| IGHD IA | **GH1** | Autosomal recessive; usually homozygous GH1 deletion/null variants causing absent GH production | Early severe short stature, often height < -4.5 SDS; undetectable GH; anti-GH antibodies/tachyphylaxis may occur with therapy | MONDO: isolated growth hormone deficiency type IA (MONDO_0009876); HPO: Short stature, Growth delay; GO: growth hormone secretion; CL: somatotroph; UBERON: anterior pituitary gland | 6.7 kb GH1 deletion reported as most frequent classic lesion; severe phenotype emphasized across reviews (domene2018geneticmutationsin pages 7-8, ibba2024isolatedgrowthhormone pages 4-5) |
| IGHD IB | **GH1** | Autosomal recessive; biallelic nonsense/frameshift/splice variants with residual GH | Milder growth failure than IA; low but detectable GH; generally good response to rhGH | MONDO: isolated growth hormone deficiency type IB (MONDO_0013006); HPO: Short stature, Delayed bone age; CL: somatotroph | Novel homozygous GH1 p.Tyr54* reported in 2023 cohort; immune tolerance better than IA (ozturk2023phenotypegenotypecorrelationsof pages 1-2, ozturk2023phenotypegenotypecorrelationsof pages 2-2) |
| IGHD II | **GH1** | Autosomal dominant; often splice-site or exon 3-skipping/dominant-negative mechanism | Variable short stature with low but detectable GH and low IGF-1; may progress to MPHD; MRI often normal or anterior pituitary hypoplasia | MONDO: isolated growth hormone deficiency type II (MONDO_0008250); HPO: Short stature, Delayed bone age, Pituitary hypoplasia; GO: mRNA splicing, growth hormone secretion; CL: somatotroph | 2024 Chinese series: mean age 4.64 y, mean height -3.95 SDS, peak GH 2.83 ng/mL; first-year height gain 1.79 SDS on rhGH (huang2024theclinicaland pages 1-2) |
| IGHD III | **SOX3** or **BTK** | X-linked; developmental pituitary defects or BTK-related exon skipping with immune phenotype | IGHD or MPHD, sometimes ectopic posterior pituitary, intellectual disability, abnormal immune function/agammaglobulinemia | HPO: Short stature, Agammaglobulinemia, Intellectual disability, Ectopic posterior pituitary; UBERON: posterior pituitary gland | X-linked form recognized in current review; may not remain purely isolated clinically (ibba2024isolatedgrowthhormone pages 4-5, ibba2024isolatedgrowthhormone pages 10-12) |
| IGHD IV | **GHRHR** | Autosomal recessive; impaired GHRH receptor signaling in somatotrophs | Pituitary hypoplasia, severe short stature, very low baseline/stimulated GH, low IGF-1/IGFBP-3; good response to rhGH | HPO: Pituitary hypoplasia, Short stature; GO: G protein-coupled receptor signaling pathway, growth hormone secretion; CL: somatotroph | Includes classic c.57+1G>A and other receptor-defect mechanisms; little/lit mouse is homologous mechanistic model (domene2018geneticmutationsin pages 7-8, ibba2024isolatedgrowthhormone pages 4-5, domene2018geneticmutationsin pages 8-9) |
| IGHD V | **RNPC3** | Autosomal recessive; defective minor spliceosome mRNA processing | Severe postnatal growth retardation, undetectable GH, low/undetectable IGF-1 and IGFBP-3, anterior pituitary hypoplasia; females may develop ovarian insufficiency | HPO: Postnatal growth retardation, Pituitary hypoplasia, Ovarian insufficiency; GO: mRNA splicing, via spliceosome; UBERON: anterior pituitary gland | RNPC3 is an established disease gene in MONDO_0000050 resources and reviews (OpenTargets Search: isolated growth hormone deficiency-GH1,GHRHR,RNPC3, ibba2024isolatedgrowthhormone pages 4-5) |
| Other rare genetic cause | **GHSR** | AD or AR loss-of-function affecting ghrelin receptor activity | Familial short stature/partial IGHD with low GH responses | HPO: Short stature; GO: ghrelin receptor signaling pathway, regulation of growth hormone secretion | 2024 Egyptian series found pathogenic **GHRHR** p.Arg357Cys in one case and novel **GHSR** c.1043dup p.Ser349Leufs*6 in another; 90% underweight, 50% anemia, 80% hypovitaminosis D in the 10-patient cohort (ammar2024screeningofghsr pages 1-2) |
| Broader pituitary-development genes | **PROP1, HESX1, SOX3, OTX2, GLI2, LHX3, LHX4, POU1F1** | Mostly developmental transcription-factor defects; usually MPHD spectrum but can present as isolated GHD | Extreme short stature, family history, or structural pituitary anomalies prompt testing beyond GH1/GHRHR | GO: pituitary gland development; CL: pituitary endocrine cell; UBERON: pituitary gland | These genes are important differential/extended panel targets rather than core isolated-disease genes (ibba2024isolatedgrowthhormone pages 1-2, ozturk2023phenotypegenotypecorrelationsof pages 1-2) |
| Core diagnostics | Auxology + biochemistry + dynamic testing | Diagnostic process integrates phenotype, IGF-1/IGFBP-3, GH stimulation tests, and MRI | Height < -2 SDS; reduced height velocity; delayed bone age; classic approach uses inadequate response to 2 GH stimulation tests | HPO: Short stature, Delayed bone age; UBERON: pituitary gland; term: growth hormone stimulation test | GHST cutoffs remain assay/test dependent and vary ~3-10 µg/L across centers; recent guidelines still recommend GHST in most children (ibba2024isolatedgrowthhormone pages 2-4, ibba2024isolatedgrowthhormone pages 1-2) |
| Diagnostic confounders | BMI, puberty, assay variability | Obesity lowers peak stimulated GH; puberty status affects interpretation; sex-steroid priming reduces false positives | Consider priming in prepubertal boys >11 y and girls >10 y; interpret low IGF-1 in context | term: body mass index; HPO: Delayed puberty | Meta-analysis of 58 studies (n=5,135): each 1-point BMI SDS increase lowered peak GH by 11.6%; proposed lower BMI-adjusted cutoffs (abawi2021impactofbody pages 1-3) |
| MRI/anatomy | Pituitary MRI | Structural assessment of hypothalamic-pituitary region after biochemical diagnosis | Pituitary hypoplasia most common; also PSIS and ectopic posterior pituitary; normal MRI does not exclude genetic IGHD | HPO: Pituitary hypoplasia, Ectopic posterior pituitary, Pituitary stalk interruption syndrome; UBERON: hypothalamus, pituitary stalk | MRI is recommended after confirmation; reduced pituitary volume alone is not diagnostic (ibba2024isolatedgrowthhormone pages 4-5, ibba2024isolatedgrowthhormone pages 1-2) |
| Genetic testing workflow | Panel/MLPA/WES | Start with targeted testing when family history, extreme short stature, or anatomical anomalies; MLPA useful for deletions/duplications | Useful especially for **GH1**, **GHRHR**, **GHSR**, and extended pituitary-development genes | term: next-generation sequencing panel; term: MLPA; term: whole exome sequencing | 25-gene panel with 99.2% coverage used in 2023 GH1 cohort; genetic testing specifically indicated by current review in familial/anatomic/extreme cases (ozturk2023phenotypegenotypecorrelationsof pages 1-2, ibba2024isolatedgrowthhormone pages 4-5) |
| Daily standard therapy | Somatropin (rhGH) | Replacement therapy restoring GH action and IGF-1 generation | Improves short-term height gain, adult height, body composition; monitor IGF-1, thyroid/adrenal function, headaches/SCFE | NCIT: Somatropin; GO: JAK-STAT cascade involved in growth hormone signaling pathway | Suggested starting dose 22-35 µg/kg/day (0.16-0.24 mg/kg/week); first-year response and adherence predict outcome (ibba2024isolatedgrowthhormone pages 5-6, ranke2021shortandlongterm pages 9-10) |
| Weekly long-acting GH | Somatrogon, somapacitan, lonapegsomatropin; also Jintrolong, Eutropin Plus in specific markets | Extended half-life/fusion, albumin-binding, prodrug, or PEGylated formulations | Less injection burden; efficacy and safety generally non-inferior to daily GH in pediatric GHD | NCIT terms if available not asserted; term: long-acting growth hormone replacement | Current review lists approvals since 2021 for somatrogon/somapacitan/lonapegsomatropin; same efficacy/safety as daily hGH in cited trials/reviews (ibba2024isolatedgrowthhormone pages 6-8) |
| Emerging therapy | LUM-201 (ibutamoren analog/oral GH secretagogue program) | Oral GH secretagogue strategy requiring residual pituitary function; not replacement | Trials enroll idiopathic pediatric GHD with delayed bone age and partial GH reserve rather than severe absent pituitary function | term: growth hormone secretagogue | OraGrowtH210 (NCT04614337) randomized 104 children; OraGrowtH212 (NCT04806854) active, PK/PD, estimated n=24; excludes maximal stimulated GH ≤3 ng/mL/organic disease (NCT04614337 chunk 1, NCT04806854 chunk 1) |
| Emerging diagnostic tool | Macimorelin GH stimulation test | Oral ghrelin agonist as diagnostic GHST | Pediatric phase 3 evaluates diagnostic accuracy/repeatability against clonidine and arginine | term: Macimorelin; term: growth hormone stimulation test | DETECT trial NCT04786873 completed in 2024, actual enrollment 101, crossover diagnostic design (NCT04786873 chunk 1) |
| Key mechanisms | Hypothalamic GHRH/somatostatin; pituitary somatotroph; hepatic IGF-1 axis | Upstream hypothalamic control -> pituitary GH secretion -> GHR/JAK2/STAT5B signaling -> IGF1/IGFBP3/ALS -> growth plate and metabolic effects | Mechanistically explains linear growth failure, altered body composition, and low IGF-1 | GO: growth hormone secretion; GO: JAK-STAT cascade involved in growth hormone signaling pathway; CL: somatotroph; UBERON: liver, growth plate | Mechanistic chain supported by recent reviews and classic models including little mouse and GH1 splicing models (ranke2018growthhormone—pastpresent pages 5-6, tidblad2022thehistoryphysiology pages 2-3, ranke2018growthhormone—pastpresent pages 6-7, domene2018geneticmutationsin pages 8-9) |


*Table: This compact table summarizes isolated growth hormone deficiency subtypes, core diagnostics, treatments, and mechanistic annotations for structured knowledge-base use. It prioritizes supported identifiers and recent evidence, including 2023-2024 cohorts and active/emerging clinical applications.*

## 1. Disease information

### Definition and scope

IGHD is a deficiency of GH production or secretion in which other anterior-pituitary axes are initially intact. “Isolated” describes the hormonal phenotype, not necessarily the cause: disease can be congenital, acquired, or idiopathic, and some patients—especially those with dominant **GH1** or pituitary-development variants—subsequently develop multiple pituitary hormone deficiency (MPHD). Consequently, longitudinal endocrine reassessment is essential. (ibba2024isolatedgrowthhormone pages 1-2, ozturk2023phenotypegenotypecorrelationsof pages 2-2, ibba2024isolatedgrowthhormone pages 8-9)

### Identifiers and synonyms

* **MONDO:** isolated congenital growth hormone deficiency, **MONDO:0000050**; type IA, **MONDO:0009876**; type IB, **MONDO:0013006**; type II, **MONDO:0008250**. Open Targets links MONDO:0000050 most strongly to **GH1**, **RNPC3**, and **GHRHR**. (OpenTargets Search: isolated growth hormone deficiency-GH1,GHRHR,RNPC3)
* **OMIM phenotypes:** IGHD IA **262400**; IGHD IB **612781**; IGHD II **173100**; IGHD III **307200**; GHRHR-related IGHD/“type IV” **618157**. Relevant genes include **GH1 139250**, **GHRHR 139191**, and **GHSR 601898**. (ammar2024screeningofghsr pages 1-2)
* **MeSH:** *Dwarfism, Pituitary*, **D004393**, is used in ClinicalTrials.gov indexing, although “dwarfism” is increasingly avoided in person-centered clinical language. (NCT04806854 chunk 1)
* **Common synonyms:** isolated GHD, IGHD, isolated somatotropin deficiency, isolated pituitary GH deficiency, congenital isolated GHD, familial isolated GHD, and historical “pituitary dwarfism.”
* **ICD:** routine billing commonly places GHD under ICD-10-CM **E23.0, hypopituitarism**; that code is not specific for isolated disease. ICD-11 similarly classifies it within hypopituitarism/pituitary hypofunction; local extensions should be verified before database deployment.

This report primarily synthesizes **aggregated disease-level resources and published cohorts**, not individual EHR records. The 2023–2024 GH1, Egyptian genetics, and dental studies are patient-level research cohorts but are reported here only in aggregate. (huang2024theclinicaland pages 1-2, ammar2024screeningofghsr pages 1-2, torlinskawalkowiak2023developmentalenameldefects pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factors

1. **Congenital genetic disease:** pathogenic variants affecting GH synthesis/secretion (**GH1**), hypothalamic signaling (**GHRHR**, occasionally **GHSR**), minor-spliceosome function (**RNPC3**), or pituitary development (**SOX3**, **BTK**, and occasionally **POU1F1, PROP1, HESX1, OTX2, GLI2, LHX3/LHX4, SOX2**).
2. **Congenital structural disease:** pituitary hypoplasia, ectopic posterior pituitary, pituitary stalk interruption syndrome (PSIS), or broader midline malformations.
3. **Acquired disease:** hypothalamic/pituitary tumors, cranial radiotherapy, CNS infection, traumatic brain injury, infiltrative or autoimmune disease, and pituitary surgery. In adults, tumors, surgery, trauma, and radiotherapy predominate. (ibba2024isolatedgrowthhormone pages 1-2, ammar2024screeningofghsr pages 1-2)
4. **Idiopathic IGHD:** no demonstrable genetic or structural cause; this is the largest pediatric category, but false-positive stimulation testing contributes to diagnostic heterogeneity. (ranke2018growthhormone—pastpresent pages 8-9, ibba2024isolatedgrowthhormone pages 1-2)

### Risk factors

* **Genetic:** family history, consanguinity for recessive disease, X-linked pedigree, or extreme early short stature. Affected relatives may show variable expressivity in dominant GH1 disease. (ozturk2023phenotypegenotypecorrelationsof pages 1-2, ozturk2023phenotypegenotypecorrelationsof pages 2-2)
* **Clinical/environmental:** cranial irradiation, CNS tumor, severe head trauma, infection, or surgery are causal exposures rather than lifestyle susceptibility factors. Cancer survivors can develop endocrine deficits decades after irradiation, supporting lifelong surveillance. (ibba2024isolatedgrowthhormone pages 1-2)
* **Diagnostic modifiers—not causes:** obesity, undernutrition, age, sex steroids, pubertal delay, assay choice, and stimulation agent alter measured GH or IGF-1. A 58-study meta-analysis containing **5,135 children** found that every one-unit increase in BMI SDS reduced stimulated peak GH by **11.6%** (95% CI 8.3–14.8%), creating an overdiagnosis risk. (abawi2021impactofbody pages 1-3)

No reproducible **protective genetic alleles**, diets, lifestyles, toxins, occupational exposures, smoking effects, infectious triggers, or formal gene–environment interactions have been established for inherited IGHD. Adequate nutrition and treatment of systemic disease prevent phenocopies but do not prevent a pathogenic GH-axis genotype. GHSR-null mice resist diet-induced obesity, but that experimental observation is not evidence for a protective human IGHD intervention. (domene2018geneticmutationsin pages 8-9)

## 3. Phenotypes

### Neonatal and infant disease

Intrauterine growth is usually normal because fetal growth is relatively GH independent, although birth length can be slightly reduced. Neonatal manifestations include recurrent hypoglycemia, prolonged jaundice, lethargy, poor weight gain, frontal bossing, midface hypoplasia, micropenis or genital underdevelopment in males, single central maxillary incisor, and ocular or other midline abnormalities. Severe hypoglycemia can be life-threatening, although isolated disease is often less dramatic than MPHD. Suggested HPO annotations include **Short stature, Hypoglycemia, Prolonged neonatal jaundice, Micropenis, Frontal bossing, Midface retrusion, Single maxillary central incisor**, and **Poor weight gain**. (ibba2024isolatedgrowthhormone pages 1-2, ibba2024isolatedgrowthhormone pages 2-4)

### Childhood and adolescence

The core phenotype is **proportionate short stature**—height below −2 SDS—with slow growth velocity, downward crossing of height centiles, delayed bone age, preserved or increased weight-for-height, truncal adiposity, immature facial appearance, depressed nasal bridge, delayed dentition, and sometimes delayed puberty. The disease is generally chronic and progressively increases the height deficit if untreated rather than being episodic. Suggested HPO terms include **Proportionate short stature, Growth delay, Delayed skeletal maturation, Delayed dentition, Truncal obesity**, and **Delayed puberty**. (ibba2024isolatedgrowthhormone pages 2-4, ammar2024screeningofghsr pages 1-2)

Genetic severity varies. Type IA commonly produces height below **−4.5 SDS**, absent GH, and very early growth failure. Types IB and II retain measurable GH and range from mild to severe. In a 2024 Chinese IGHD-II series of six children, mean age was **4.64 ± 1.15 years**, mean height **−3.95 ± 1.41 SDS**, and mean stimulated peak GH **2.83 ± 2.46 ng/mL**; four had a family history of short stature. (ibba2024isolatedgrowthhormone pages 4-5, huang2024theclinicaland pages 1-2)

A 2023 cross-sectional study found dental anomalies in **33% of 33 children with isolated GHD versus 4% of 68 controls** (p<0.001): hypodontia occurred in **18%**, and microdontia/macrodontia in **21%**. Developmental enamel defects were not significantly enriched (**58% versus 48%**). Suggested HPO terms are **Hypodontia, Microdontia, Macrodontia**, and **Abnormality of dental enamel**; routine dental assessment is reasonable. (torlinskawalkowiak2023developmentalenameldefects pages 1-2)

### Adult and quality-of-life phenotype

Persistent childhood-onset GHD can adversely affect fat/lean-mass distribution, bone acquisition, exercise capacity, cardiac function, lipid metabolism, and quality of life. However, transition studies are heterogeneous, and isolated idiopathic childhood GHD frequently fails confirmation on adult retesting. Adult symptom attribution therefore requires biochemical reconfirmation rather than assuming lifelong disease. (ranke2018growthhormone—pastpresent pages 8-9, ahmid2016growthhormonedeficiency pages 1-3)

Disease-specific EQ-5D or SF-36 statistics for genetically confirmed IGHD remain limited. The dominant pediatric burden comprises short-stature-related psychosocial effects and repeated injections; weekly GH trials explicitly measure interference with daily, social, leisure, and travel activities. (NCT03831880 chunk 1)

## 4. Genetic and molecular information

### Major genes and subtype architecture

* **IGHD IA—GH1, autosomal recessive:** homozygous deletions or other biallelic null variants eliminate GH. Classic deletion sizes include 6.7, 7.0, 7.6, and 45 kb; the 6.7-kb deletion accounts for an estimated **70–80%** of homozygous deletion cases in historical series. Absent endogenous GH prevents immune tolerance, permitting neutralizing anti-GH antibodies and treatment tachyphylaxis. (domene2018geneticmutationsin pages 7-8, ozturk2023phenotypegenotypecorrelationsof pages 2-2)
* **IGHD IB—GH1, autosomal recessive:** biallelic nonsense, frameshift, or splice variants permit low/bio-inactive GH and usually preserve treatment responsiveness. A 2023 report identified novel homozygous **c.162C>G, p.Tyr54***. (ozturk2023phenotypegenotypecorrelationsof pages 1-2)
* **IGHD II—GH1, autosomal dominant:** splice-site, splice-enhancer, missense, nonsense, and structural variants. IVS3 defects commonly skip exon 3 and produce a 17.5-kDa GH isoform that disrupts secretory-vesicle maturation and injures somatotrophs—a dominant-negative mechanism with variable expressivity. Six 2024 families carried Exon2-5del, **c.334T>C, c.291+1G>A, c.291+2T>A**, and 1.5- or 1.7-kb deletions; four variants were novel. (domene2018geneticmutationsin pages 7-8, huang2024theclinicaland pages 1-2)
* **IGHD III—SOX3 or BTK, X-linked:** may include MPHD, ectopic posterior pituitary, intellectual disability, immune dysfunction, and BTK-related agammaglobulinemia. This category is biologically heterogeneous and may not remain strictly isolated. (ibba2024isolatedgrowthhormone pages 10-12, ibba2024isolatedgrowthhormone pages 4-5)
* **GHRHR-related/type IV, autosomal recessive:** loss of receptor signaling causes somatotroph under-stimulation and pituitary hypoplasia. The recurrent **c.57+1G>A** splice variant causes intron retention and premature termination; signal-peptide variants can block receptor trafficking to the cell surface. (domene2018geneticmutationsin pages 7-8, ibba2024isolatedgrowthhormone pages 10-12)
* **RNPC3-related/type V, autosomal recessive:** defective U12-type minor-spliceosome processing produces severe postnatal growth failure, absent GH, low IGF-1/IGFBP-3, anterior-pituitary hypoplasia, low-normal prolactin, and sometimes ovarian insufficiency. Primary evidence is PMID **24480542**. (OpenTargets Search: isolated growth hormone deficiency-GH1,GHRHR,RNPC3, ibba2024isolatedgrowthhormone pages 4-5)
* **GHSR:** rare dominant or recessive loss-of-function variants reduce ghrelin-receptor constitutive/ligand-dependent signaling. A 2024 Egyptian cohort identified **GHRHR NM_000823.4:c.1069C>T, p.Arg357Cys** and novel **GHSR NM_198407.2:c.1043dup, p.Ser349Leufs*6** in separate patients. (ammar2024screeningofghsr pages 1-2)

Variants are germline; there is no established somatic IGHD category. Pathogenic deletions and truncating/splice variants should be classified using ACMG/AMP evidence, segregation, phenotype, functional data, and population frequency. Exact gnomAD frequencies are variant-specific and should be pulled at ingestion time; causal severe-IGHD alleles are generally absent or exceptionally rare. The cited 2023 panel study used ACMG classification, ClinVar/dbSNP/HGMD review, and segregation testing. (ozturk2023phenotypegenotypecorrelationsof pages 1-2)

No consistently validated human **modifier gene**, protective allele, anticipation, or epigenetic signature is ready for clinical annotation. Dominant GH1 disease shows incomplete/variable expression, and digenic pituitary-development interactions are plausible, but evidence remains family- and model-specific. Germline mosaicism is theoretically possible but not a prominent documented feature. Founder GHRHR mutations occur in geographically isolated/consanguineous populations, so local carrier frequencies can be much higher than global frequencies.

## 5. Environmental and lifestyle information

There is no evidence that ordinary diet, exercise, smoking, alcohol, pollution, occupational exposure, or a specific infectious agent causes hereditary IGHD. CNS infection, trauma, tumors, surgery, and ionizing radiation can cause **acquired isolated GHD** by damaging hypothalamic GHRH neurons, the pituitary stalk, or somatotrophs. Chronic malnutrition, renal disease, inflammation, hypothyroidism, and glucocorticoid exposure alter GH/IGF-1 physiology and must be treated or excluded as mimics. Exercise, nutrition, gonadal steroids, thyroid hormone, ghrelin, glucocorticoids, and systemic illness modulate secretion but do not constitute established inherited-disease prevention targets. (ibba2024isolatedgrowthhormone pages 1-2, ibba2024isolatedgrowthhormone pages 2-4, ammar2024screeningofghsr pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream regulation:** hypothalamic GHRH stimulates and somatostatin inhibits anterior-pituitary somatotrophs; ghrelin/GHSR augments secretion. GH is released in pulses and is regulated by IGF-1 negative feedback. **GHRHR/GHSR defects** reduce somatotroph stimulation; developmental-gene defects reduce pituitary/somatotroph formation; **GH1** variants abolish synthesis, generate inactive hormone, or exert dominant-negative secretory toxicity; **RNPC3** disrupts minor-intron splicing. (ranke2018growthhormone—pastpresent pages 5-6, tidblad2022thehistoryphysiology pages 2-3)

**Downstream signaling:** circulating GH binds dimeric GHR, activates JAK2 and STAT5B, and drives hepatic and tissue transcription of **IGF1, IGFBP3, IGFALS**, and related targets. IGF-1 circulates largely in an IGF-1–IGFBP-3–ALS ternary complex. Reduced GH therefore lowers IGF-1 bioavailability and direct GH action. (ranke2018growthhormone—pastpresent pages 5-6, ranke2018growthhormone—pastpresent pages 6-7)

**Clinical translation:** reduced GH/IGF-1 signaling decreases recruitment and proliferation of growth-plate progenitors/chondrocytes and hypertrophic-cell expansion, causing slow longitudinal growth and delayed skeletal maturation. Reduced lipolysis and protein anabolism contribute to truncal adiposity and low lean mass; impaired osteoblast/chondrocyte stimulation compromises bone accrual. GH also influences tooth-cell differentiation through BMP2/BMP4 and TGF-family signaling. (ibba2024isolatedgrowthhormone pages 5-6, tidblad2022thehistoryphysiology pages 2-3, torlinskawalkowiak2023developmentalenameldefects pages 1-2)

Suggested annotations include **GO: growth hormone secretion; regulation of growth hormone secretion; JAK–STAT cascade involved in growth hormone signaling; insulin-like growth factor receptor signaling; chondrocyte proliferation; endochondral ossification; lipid catabolic process; skeletal-system development; mRNA splicing via spliceosome**. Relevant CL terms are **somatotroph, hepatocyte, chondrocyte, osteoblast, hypothalamic neurosecretory neuron**, and **adipocyte**.

### Immune, tissue damage, and omics

IGHD is not ordinarily inflammatory or autoimmune. Immune involvement is subtype-specific in **BTK-related X-linked agammaglobulinemia**, and anti-GH antibodies can neutralize replacement in type IA. Dominant 17.5-kDa GH can cause somatotroph loss/apoptosis and anterior-pituitary hypoplasia. (ozturk2023phenotypegenotypecorrelationsof pages 2-2, domene2018geneticmutationsin pages 8-9)

A 2024 study reported that pretreatment blood transcriptomic signatures predicted first-year response to daily rhGH or weekly somapacitan, but external validation is required. Disease-specific proteomics, metabolomics, lipidomics, single-cell atlases, spatial transcriptomics, CRISPR screens, and integrated multi-omics are not yet mature clinical tools. (ibba2024isolatedgrowthhormone pages 12-13, ibba2024isolatedgrowthhormone pages 5-6)

## 7. Anatomical structures affected

* **Primary:** hypothalamus, pituitary stalk, and anterior pituitary/somatotroph population. Suggested UBERON terms: **hypothalamus, pituitary stalk, pituitary gland, anterior lobe of pituitary gland**.
* **Secondary targets:** liver (IGF-1/IGFBP-3/ALS production), epiphyseal growth plate, bone, skeletal muscle, adipose tissue, heart, and developing teeth.
* **Subcellular:** plasma membrane GHRHR/GHSR/GHR; ER/Golgi and secretory granules for GH folding/trafficking; cytosolic JAK2/STAT5B; nucleus for target transcription; spliceosome for RNPC3 disease.
* **Imaging:** pituitary hypoplasia is the most frequent abnormality; PSIS and ectopic posterior pituitary are less common. A small pituitary alone is not diagnostic, and **GH1/GHRHR disease can have a normal MRI**. There is no relevant lateralization. (ibba2024isolatedgrowthhormone pages 4-5)

## 8. Temporal development and natural history

Congenital disease begins biologically at birth but commonly becomes clinically obvious at **2–4 years**, when postnatal growth decelerates. Severe IA or structural disease can present neonatally. Untreated disease produces chronic, progressive height deficit and delayed maturation; it is not relapsing-remitting. Puberty may be delayed but fertility is usually preserved in genuinely isolated disease. (ammar2024screeningofghsr pages 1-2, torlinskawalkowiak2023developmentalenameldefects pages 1-2)

The principal intervention window is before major growth-plate senescence; younger treatment initiation and longer therapy predict better adult height. Therapy generally continues until growth velocity is below **2 cm/year** and/or bone maturation is complete. Idiopathic isolated cases should then be retested because many normalize; proven genetic/structural severe disease is more likely permanent. Type II and developmental-gene cases require surveillance for evolving TSH, ACTH, gonadotropin, or prolactin deficits. (ranke2018growthhormone—pastpresent pages 8-9, ranke2021shortandlongterm pages 9-10, ibba2024isolatedgrowthhormone pages 8-9, ibba2024isolatedgrowthhormone pages 5-6)

## 9. Inheritance and population characteristics

Incidence estimates are **1:4,000–10,000 live births**; a UK estimate for congenital childhood-onset GHD was approximately **1:3,500–4,000**. Robust IGHD-specific point prevalence and annual incidence by country, ethnicity, or sex are unavailable. Referral and treatment are male-skewed: in one 10,125-child referral cohort, only **35%** were female, and GH stimulation testing occurred in **13.1% of males versus 10.6% of females**, suggesting ascertainment bias rather than biological sex restriction. (ibba2024isolatedgrowthhormone pages 1-2, ahmid2016growthhormonedeficiency pages 1-3)

Inheritance is AR for IA, IB, GHRHR-related IV, and RNPC3-related V; AD for II and some GHSR disease; and X-linked for III. Penetrance and expressivity are especially variable in AD GH1 disease. Consanguinity increases recessive-disease probability. No anticipation is known. Carrier frequency and variant geography must be calculated per allele/population; no defensible universal carrier rate exists. (ozturk2023phenotypegenotypecorrelationsof pages 1-2, ibba2024isolatedgrowthhormone pages 4-5)

## 10. Diagnostics

### Clinical and biochemical workflow

1. Confirm serial auxology: height below −2 SDS, height relative to mid-parental target, reduced growth velocity, and centile crossing. A fall in height SDS exceeding **0.25 over one year** is a strong growth-disorder signal; height velocity above −1 SDS makes severe non-acquired GHD less likely. Obtain left-hand/wrist bone age. (ranke2021shortandlongterm pages 3-4)
2. Exclude systemic/nutritional/endocrine causes with history, examination, CBC, inflammatory/renal/hepatic testing as indicated, thyroid testing, celiac screening, and nutritional assessment.
3. Measure age-, sex-, and puberty-adjusted **IGF-1** and **IGFBP-3**. IGF-1 below −2 SDS supports GHD, but a normal result does not exclude it; IGFBP-3 is relatively more useful under age three. In an 800-subject study, the best IGF-1 threshold was **−1.5 SDS**, sensitivity **67.61%**, specificity **62.62%**, and AUC **0.69**; performance was poorer for idiopathic GHD (AUC **0.63**) than organic/genetic disease (**0.75**). (ibba2020igf1forthe pages 1-2, ibba2024isolatedgrowthhormone pages 2-4)
4. In most children, require inadequate responses to **two different GH stimulation tests**—for example clonidine, arginine, glucagon, or insulin tolerance testing where safe. Cutoffs vary approximately **3–10 µg/L**; a modern guideline/study threshold of 7 µg/L is common, but results must be interpreted with the assay and agent rather than as a universal biological boundary. Basal random GH is generally useless because secretion is pulsatile. (ibba2024isolatedgrowthhormone pages 2-4, ibba2020igf1forthe pages 1-2, tran2023somatropinforgrowth pages 35-37)
5. Account for BMI and puberty. The BMI meta-analysis proposed, for nominal cutoffs of 5, 7, 10, and 20 µg/L, overweight-child cutoffs of **4.6, 6.5, 9.3, 18.6** and obesity cutoffs of **4.3, 6.0, 8.6, 17.3 µg/L**, respectively; these are evidence-based proposals, not universally adopted standards. Sex-steroid priming is recommended before testing prepubertal boys older than 11 and girls older than 10 to reduce false positives. (abawi2021impactofbody pages 1-3, ibba2024isolatedgrowthhormone pages 1-2)
6. Obtain hypothalamic–pituitary MRI after biochemical confirmation to detect tumor, hypoplasia, PSIS, or ectopic posterior pituitary. MRI may reasonably precede GHST in very young children in whom testing is unreliable or hazardous. (ibba2024isolatedgrowthhormone pages 4-5)

### Exceptions and neonatal diagnosis

Formal GHST is unnecessary when auxological evidence coexists with a structural hypothalamic-pituitary lesion and at least one other pituitary deficit. In neonates with hypoglycemia, GH ≤5 ng/mL together with another pituitary deficiency or the classical MRI triad strongly supports diagnosis. A dried-blood-spot GH below 7 µg/L plus recurrent hypoglycemia/MPHD/significant malformation showed high reliability in one study, but newborn-card testing is not validated for population screening. (ibba2024isolatedgrowthhormone pages 2-4, tran2023somatropinforgrowth pages 35-37)

### Genetic testing

Testing is most indicated for severe/extreme early short stature, family history, consanguinity, normal MRI with severe biochemical disease, structural/midline abnormalities, immune findings, or evolving MPHD. A practical sequence is: **GH1 deletion/duplication analysis (MLPA/CNV) plus sequencing; GHRHR; GHSR; RNPC3; SOX3/BTK when phenotype suggests; then a broader pituitary/short-stature panel or trio WES/WGS**. A 2023 study used a 25-gene panel with **99.2% coverage**, followed by MLPA and segregation testing. CMA is useful for syndromic structural disease/CNVs; karyotype is appropriate for Turner syndrome in girls. FISH, mitochondrial sequencing, repeat-expansion testing, biopsy, electrophysiology, and liquid biopsy are not routine IGHD tests. (ibba2024isolatedgrowthhormone pages 4-5, ozturk2023phenotypegenotypecorrelationsof pages 1-2)

### Differential diagnosis

Exclude familial short stature, constitutional delay of growth and puberty, small-for-gestational-age growth failure, malnutrition, celiac/inflammatory/renal disease, hypothyroidism, glucocorticoid excess, psychosocial deprivation, Turner syndrome, SHOX deficiency, Noonan/3M syndromes, skeletal dysplasia, GH insensitivity (**GHR, STAT5B, IGF1, IGFALS**), and chronic medication effects. GH neurosecretory dysfunction—low spontaneous secretion but normal stimulated peak—remains controversial. (ranke2018growthhormone—pastpresent pages 8-9)

There is no population newborn screening. Cascade testing and targeted testing of relatives are appropriate after a pathogenic familial variant is identified.

## 11. Outcome and prognosis

IGHD is treatable and is not ordinarily directly lethal. Disease-specific 5- or 10-year survival estimates are not meaningful. Prognosis chiefly concerns adult height, metabolic/body-composition health, bone acquisition, treatment burden, and evolution to MPHD. Historical rhGH-era patients starting near **−2.9 height SDS** achieved final height around **−1.4 SDS**; modern earlier daily treatment often reaches the lower-normal target range. Favorable predictors are younger age, taller baseline/target height, longer treatment, appropriate dose, adherence, and strong first-year response. (ranke2021shortandlongterm pages 9-10)

In the 2024 IGHD-II series, four treated children gained **1.21 ± 0.30 height SDS at six months** and **1.79 ± 0.15 SDS at one year**, illustrating high responsiveness in a small genetic cohort. Poor response may be defined operationally as first-year height-SDS gain below **0.4** or height velocity below −1 SDS relative to age/sex treatment targets. (huang2024theclinicaland pages 1-2, ibba2024isolatedgrowthhormone pages 5-6)

Long-term untreated persistent GHD may impair body composition, skeletal health, exercise capacity, and quality of life. Evidence for transition-age GH benefits is inconsistent, so persistent deficiency should be confirmed before indefinite adult therapy. (ahmid2016growthhormonedeficiency pages 1-3)

## 12. Treatment and current implementation

### Daily rhGH

Subcutaneous recombinant human GH (somatropin) is standard of care. A suggested pediatric starting dose is **22–35 µg/kg/day** or **0.16–0.24 mg/kg/week**, individualized by weight, growth velocity, response, adherence, and IGF-1. Review every 3–6 months; maintain IGF-1 in the age-/sex-appropriate range and monitor thyroid and adrenal function because GH can unmask central hypothyroidism or adrenal insufficiency. Routine pubertal dose escalation is not recommended. Suggested NCIT intervention terms are **Somatropin** and **Recombinant Human Growth Hormone Therapy**. (ibba2024isolatedgrowthhormone pages 5-6)

Treatment increases growth rate and adult height, lowers fat mass, increases lean/bone mass, stimulates skeletal IGF-1, chondrocytes, osteoblasts, and bone remodeling. Type IB, II, GHRHR, and RNPC3 disease generally responds well; IA can develop neutralizing antibodies and tachyphylaxis. There is no established pharmacogenomic dosing guideline, although genotype informs permanence and antibody risk. (ibba2024isolatedgrowthhormone pages 4-5, ibba2024isolatedgrowthhormone pages 5-6)

### Weekly long-acting GH

Approved pediatric weekly products include:

* **Somatrogon**, a GH–hCG-carboxy-terminal-peptide fusion, first approved in Australia in 2021 and subsequently in Europe, the United States, Canada, Japan, and other jurisdictions.
* **Somapacitan**, an albumin-binding GH analog, first approved in Europe in 2021 and subsequently in multiple countries.
* **Lonapegsomatropin**, a transiently PEG-bound prodrug, FDA-approved in 2021.
* **Jintrolong**, PEGylated GH approved in China since 2014.
* **Eutropin Plus/LBO3002**, a depot formulation available in South Korea.

Trials and meta-analyses generally find non-inferior growth and broadly similar short-term safety to daily rhGH, with lower injection burden; post-marketing surveillance remains necessary. A Pfizer crossover study, **NCT03831880**, enrolled 87 children to compare somatrogon versus daily Genotropin treatment burden. (ibba2024isolatedgrowthhormone pages 6-8, NCT03831880 chunk 1)

### Safety

Common or important monitored events include transient headache, intracranial hypertension, slipped capital femoral epiphysis, scoliosis progression during rapid growth, edema/arthralgia, glucose intolerance, and rare pancreatitis or sleep-apnea exacerbation. New primary malignancy has not been shown to increase in otherwise low-risk GHD children; concern is greater for secondary neoplasms in previously irradiated cancer survivors. The KIGS cohort included **83,803 treated children** and found no unexpected safety signal. SAGhE analyses did not establish a consistent dose-related mortality association, although continued surveillance is appropriate. (ibba2024isolatedgrowthhormone pages 8-9, ibba2024isolatedgrowthhormone pages 6-8)

### Experimental and diagnostic trials

* **LUM-201**, an oral GH secretagogue, is intended for selected idiopathic pediatric GHD with residual pituitary reserve—not severe absent secretion or organic disease. Phase 2 **OraGrowtH210, NCT04614337**, randomized **104** children among 0.8, 1.6, or 3.2 mg/kg/day and daily rhGH; **OraGrowtH212, NCT04806854**, studies 1.6 versus 3.2 mg/kg/day and GH pulsatility in approximately **24** children. (NCT04806854 chunk 1, NCT04614337 chunk 1)
* **Macimorelin:** phase 3 **DETECT, NCT04786873**, completed June 13, 2024, enrolled **101** patients aged 2–<18 years and compared two oral macimorelin GHSTs with arginine and clonidine, assessing ROC AUC, sensitivity, specificity, and repeatability. It was diagnostic, not therapeutic. (NCT04786873 chunk 1)
* **Y-shaped PEGylated somatropin, NCT04513171:** completed phase 2/3 study of **434** prepubertal children, comparing weekly 100–140 µg/kg with daily Norditropin; 52-week height velocity was the phase 3 primary endpoint. (NCT04513171 chunk 1)

No gene, cell, RNA, CRISPR, surgical, or immunotherapy is established for hereditary IGHD. Surgery/radiotherapy applies only to an underlying acquired lesion, not hormone deficiency itself. Nutrition, psychosocial support, dental care, and adherence support are useful adjuncts.

## 13. Prevention

* **Primary prevention:** inherited IGHD generally cannot be prevented. Avoid unnecessary cranial irradiation and optimize CNS-tumor/trauma care where possible. Vaccines or antimicrobial prophylaxis have no IGHD-specific role.
* **Secondary prevention:** serial height measurement and growth-velocity surveillance permit early recognition; targeted monitoring is warranted after cranial irradiation, CNS tumors, trauma, or in affected families. There is no universal newborn screen.
* **Genetic prevention options:** counseling, cascade testing, carrier testing for a known familial AR variant, prenatal diagnosis, and preimplantation genetic testing may be offered with nondirective counseling.
* **Tertiary prevention:** timely rhGH, adherence support, IGF-1 and thyroid/adrenal monitoring, orthopedic/ophthalmologic review when symptomatic, dental screening, and transition retesting reduce permanent short stature, metabolic morbidity, and treatment complications. (ibba2024isolatedgrowthhormone pages 5-6, torlinskawalkowiak2023developmentalenameldefects pages 1-2)

## 14. Other species and natural disease

Relevant taxa include **Mus musculus** (NCBI Taxon 10090) and **Danio rerio** (7955). Robust retrieved evidence supports experimental/spontaneous models rather than a well-curated naturally occurring veterinary counterpart. Claims of breed-specific canine, feline, cattle, or chicken IGHD should therefore be verified in OMIA/VBO before knowledge-base inclusion. The disorder is noninfectious and nonzoonotic; transmission is genetic, not cross-species. (domene2018geneticmutationsin pages 8-9, domene2018geneticmutationsin pages 7-8)

## 15. Model organisms

* **Little/lit mouse:** spontaneous homozygous **Ghrhr p.Asp60Gly** abolishes ligand binding, lowers GH and IGF-1, and causes severe recessive dwarfism, closely modeling GHRHR-related IGHD. It is useful for testing hypothalamic–somatotroph signaling and replacement; limitations include species-specific growth dynamics. (domene2018geneticmutationsin pages 8-9)
* **17.5-kDa GH transgenic mouse:** models dominant exon-3-skipping GH1 disease, with abnormal secretory vesicles, somatotroph loss, and anterior-pituitary hypoplasia. It is particularly informative for dominant-negative cellular toxicity. (domene2018geneticmutationsin pages 8-9)
* **Ghrh-targeted and somatotroph-ablation mice:** isolate the consequences of absent hypothalamic ligand or GH-producing cells. Snell/Pou1f1 and Ames/Prop1 mice model MPHD rather than pure IGHD and therefore have hypothyroidism, infertility, or other confounders. (domene2018geneticmutationsin pages 16-17, domene2018geneticmutationsin pages 5-7)
* **Ghsr knockout mice:** have modestly reduced IGF-1/body weight but are not profoundly dwarf, illustrating that human GHSR disease is often partial and that receptor redundancy/species differences matter. (domene2018geneticmutationsin pages 8-9)
* **Zebrafish vizzini gh1 mutant:** has persistent small size, severe growth retardation, and increased adiposity, reproducing growth and metabolic aspects of IGHD. Zebrafish btk knockdown causes broader embryonic abnormalities and is less specific. (domene2018geneticmutationsin pages 7-8)

Useful resources are MGI/IMSR/MMRRC for mice and ZFIN for zebrafish. These models robustly reproduce impaired growth and selected metabolic/pituitary features but do not fully capture human psychosocial burden, pubertal timing, antibody formation, adult-height outcomes, or heterogeneous idiopathic disease.

## Evidence gaps and interpretation cautions

The 2024 disease-specific review states directly that GHST accuracy remains debated because of “**arbitrarily established cut-off, non-physiological test procedures, variability in the type of stimulation test and type of assay**.” It also concludes that “**IGHD may progress to MPHD**,” justifying long-term pituitary surveillance. (ibba2024isolatedgrowthhormone pages 1-2, ibba2024isolatedgrowthhormone pages 8-9)

Major unresolved areas are: validated diagnostic cutoffs adjusted simultaneously for assay, agent, BMI, age, and puberty; population-specific prevalence and carrier frequencies; prospective quality-of-life and cardiovascular outcomes in molecularly confirmed IGHD; robust genotype-specific treatment algorithms; long-term comparative safety of weekly GH; validated transcriptomic response prediction; and disease-specific single-cell, spatial, proteomic, metabolomic, or epigenomic datasets. The evidence base is strongest for auxology, GH1/GHRHR mechanisms, replacement efficacy, and short-term LAGH non-inferiority, and weaker for idiopathic partial GHD and lifelong adult treatment.

## Key recent sources and links

* Ibba A, et al. **“Isolated Growth Hormone Deficiency.”** Published **8 August 2024**. https://doi.org/10.3390/endocrines5030025 (ibba2024isolatedgrowthhormone pages 1-2)
* Huang X, et al. **GH1 variants and IGHD II in six families.** Published **7 October 2024**. https://doi.org/10.3389/fendo.2024.1363050 (huang2024theclinicaland pages 1-2)
* Ammar THA, et al. **GHSR, GHRHR, and GH1 screening in Egyptian IGHD.** Published **2024**. https://doi.org/10.1186/s43042-024-00480-y (ammar2024screeningofghsr pages 1-2)
* Öztürk AP, et al. **GH1 phenotype–genotype correlations.** Published online **14 June 2023**. https://doi.org/10.1159/000531113 (ozturk2023phenotypegenotypecorrelationsof pages 1-2)
* Torlińska-Walkowiak N, et al. **Dental anomalies in isolated GHD.** Published **September 2023**. https://doi.org/10.1038/s41598-023-41892-x (torlinskawalkowiak2023developmentalenameldefects pages 1-2)
* ClinicalTrials.gov: **NCT04786873** (pediatric macimorelin), **NCT04614337** and **NCT04806854** (LUM-201), **NCT04513171** (weekly PEGylated GH). (NCT04513171 chunk 1, NCT04806854 chunk 1, NCT04786873 chunk 1, NCT04614337 chunk 1)

References

1. (ibba2024isolatedgrowthhormone pages 1-2): Anastasia Ibba, Chiara Guzzetti, Lavinia Sanfilippo, and Sandro Loche. Isolated growth hormone deficiency. Endocrines, 5:341-353, Aug 2024. URL: https://doi.org/10.3390/endocrines5030025, doi:10.3390/endocrines5030025. This article has 2 citations.

2. (ibba2024isolatedgrowthhormone pages 8-9): Anastasia Ibba, Chiara Guzzetti, Lavinia Sanfilippo, and Sandro Loche. Isolated growth hormone deficiency. Endocrines, 5:341-353, Aug 2024. URL: https://doi.org/10.3390/endocrines5030025, doi:10.3390/endocrines5030025. This article has 2 citations.

3. (ibba2024isolatedgrowthhormone pages 2-4): Anastasia Ibba, Chiara Guzzetti, Lavinia Sanfilippo, and Sandro Loche. Isolated growth hormone deficiency. Endocrines, 5:341-353, Aug 2024. URL: https://doi.org/10.3390/endocrines5030025, doi:10.3390/endocrines5030025. This article has 2 citations.

4. (domene2018geneticmutationsin pages 7-8): S. Domené and H. Domené. Genetic mutations in the gh/igf axis. Pediatric endocrinology reviews : PER, 16 Suppl 1:39-62, Sep 2018. URL: https://doi.org/10.17458/per.vol16.2018.dd.geneticmutationsghigf, doi:10.17458/per.vol16.2018.dd.geneticmutationsghigf. This article has 20 citations.

5. (ibba2024isolatedgrowthhormone pages 4-5): Anastasia Ibba, Chiara Guzzetti, Lavinia Sanfilippo, and Sandro Loche. Isolated growth hormone deficiency. Endocrines, 5:341-353, Aug 2024. URL: https://doi.org/10.3390/endocrines5030025, doi:10.3390/endocrines5030025. This article has 2 citations.

6. (ozturk2023phenotypegenotypecorrelationsof pages 1-2): A. Öztürk, A. Aslanger, F. Baş, G. Toksoy, V. Karaman, Gulandam Bagırova, S. Poyrazoglu, Z. Uyguner, F. Darendeliler, and Zehra Yavaş Abalı. Phenotype-genotype correlations of gh1 gene variants in patients with isolated growth hormone deficiency or multiple pituitary hormone deficiency. Hormone Research in Pædiatrics, 97:126-133, Jun 2023. URL: https://doi.org/10.1159/000531113, doi:10.1159/000531113. This article has 7 citations.

7. (ozturk2023phenotypegenotypecorrelationsof pages 2-2): A. Öztürk, A. Aslanger, F. Baş, G. Toksoy, V. Karaman, Gulandam Bagırova, S. Poyrazoglu, Z. Uyguner, F. Darendeliler, and Zehra Yavaş Abalı. Phenotype-genotype correlations of gh1 gene variants in patients with isolated growth hormone deficiency or multiple pituitary hormone deficiency. Hormone Research in Pædiatrics, 97:126-133, Jun 2023. URL: https://doi.org/10.1159/000531113, doi:10.1159/000531113. This article has 7 citations.

8. (huang2024theclinicaland pages 1-2): Xiaozhen Huang, Hong Chen, Huakun Shangguan, Wenyong Wu, Zhuanzhuan Ai, Zhifeng Chen, and Ruimin Chen. The clinical and genetic aspects of six individuals with gh1 variants and isolated growth hormone deficiency type ii. Frontiers in Endocrinology, Oct 2024. URL: https://doi.org/10.3389/fendo.2024.1363050, doi:10.3389/fendo.2024.1363050. This article has 4 citations.

9. (ibba2024isolatedgrowthhormone pages 10-12): Anastasia Ibba, Chiara Guzzetti, Lavinia Sanfilippo, and Sandro Loche. Isolated growth hormone deficiency. Endocrines, 5:341-353, Aug 2024. URL: https://doi.org/10.3390/endocrines5030025, doi:10.3390/endocrines5030025. This article has 2 citations.

10. (domene2018geneticmutationsin pages 8-9): S. Domené and H. Domené. Genetic mutations in the gh/igf axis. Pediatric endocrinology reviews : PER, 16 Suppl 1:39-62, Sep 2018. URL: https://doi.org/10.17458/per.vol16.2018.dd.geneticmutationsghigf, doi:10.17458/per.vol16.2018.dd.geneticmutationsghigf. This article has 20 citations.

11. (OpenTargets Search: isolated growth hormone deficiency-GH1,GHRHR,RNPC3): Open Targets Query (isolated growth hormone deficiency-GH1,GHRHR,RNPC3, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

12. (ammar2024screeningofghsr pages 1-2): Tamer H. A. Ammar, Ghada M. M. Al-Ettribi, Maha M. A. Abo Hashish, Tarek M. Farid, Amany A. Abou-Elalla, and Manal M. Thomas. Screening of ghsr, ghrhr, gh1 genes in isolated growth hormone deficiency disease in egyptian patients. Egyptian Journal of Medical Human Genetics, Feb 2024. URL: https://doi.org/10.1186/s43042-024-00480-y, doi:10.1186/s43042-024-00480-y. This article has 11 citations and is from a peer-reviewed journal.

13. (abawi2021impactofbody pages 1-3): Ozair Abawi, Dieuwertje Augustijn, Sanne E. Hoeks, Yolanda B. de Rijke, and Erica L. T. van den Akker. Impact of body mass index on growth hormone stimulation tests in children and adolescents: a systematic review and meta-analysis. Critical Reviews in Clinical Laboratory Sciences, 58:576-595, Aug 2021. URL: https://doi.org/10.1080/10408363.2021.1956423, doi:10.1080/10408363.2021.1956423. This article has 40 citations and is from a peer-reviewed journal.

14. (ibba2024isolatedgrowthhormone pages 5-6): Anastasia Ibba, Chiara Guzzetti, Lavinia Sanfilippo, and Sandro Loche. Isolated growth hormone deficiency. Endocrines, 5:341-353, Aug 2024. URL: https://doi.org/10.3390/endocrines5030025, doi:10.3390/endocrines5030025. This article has 2 citations.

15. (ranke2021shortandlongterm pages 9-10): Michael B. Ranke. Short and long-term effects of growth hormone in children and adolescents with gh deficiency. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.720419, doi:10.3389/fendo.2021.720419. This article has 86 citations.

16. (ibba2024isolatedgrowthhormone pages 6-8): Anastasia Ibba, Chiara Guzzetti, Lavinia Sanfilippo, and Sandro Loche. Isolated growth hormone deficiency. Endocrines, 5:341-353, Aug 2024. URL: https://doi.org/10.3390/endocrines5030025, doi:10.3390/endocrines5030025. This article has 2 citations.

17. (NCT04614337 chunk 1):  Phase 2 Study of LUM-201 in Children With Growth Hormone Deficiency (OraGrowtH210 Trial). Lumos Pharma. 2020. ClinicalTrials.gov Identifier: NCT04614337

18. (NCT04806854 chunk 1):  PK and PD Study of LUM-201 in Children With Idiopathic Growth Hormone Deficiency: (OraGrowtH212). Lumos Pharma. 2021. ClinicalTrials.gov Identifier: NCT04806854

19. (NCT04786873 chunk 1):  A Research Study of How Well Macimorelin Works to Find Out if Children Have a Lack of Growth Hormone and How Safe it is. AEterna Zentaris. 2021. ClinicalTrials.gov Identifier: NCT04786873

20. (ranke2018growthhormone—pastpresent pages 5-6): MB Ranke and JM Wit. Growth hormone—past, present and future. Unknown journal, 2018.

21. (tidblad2022thehistoryphysiology pages 2-3): Anders Tidblad. The history, physiology and treatment safety of growth hormone. Jun 2022. URL: https://doi.org/10.1111/apa.15948, doi:10.1111/apa.15948. This article has 54 citations and is from a peer-reviewed journal.

22. (ranke2018growthhormone—pastpresent pages 6-7): MB Ranke and JM Wit. Growth hormone—past, present and future. Unknown journal, 2018.

23. (torlinskawalkowiak2023developmentalenameldefects pages 1-2): Natalia Torlińska-Walkowiak, Katarzyna A. Majewska, Anna Sowińska, Andrzej Kędzia, and Justyna Opydo-Szymaczek. Developmental enamel defects and dental anomalies of number and size in children with growth hormone deficiency. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-41892-x, doi:10.1038/s41598-023-41892-x. This article has 22 citations and is from a peer-reviewed journal.

24. (ranke2018growthhormone—pastpresent pages 8-9): MB Ranke and JM Wit. Growth hormone—past, present and future. Unknown journal, 2018.

25. (ahmid2016growthhormonedeficiency pages 1-3): M. Ahmid, C. Perry, Syed Faisal Ahmed, and M. Shaikh. Growth hormone deficiency during young adulthood and the benefits of growth hormone replacement. Endocrine Connections, 5:R1-R11, May 2016. URL: https://doi.org/10.1530/ec-16-0024, doi:10.1530/ec-16-0024. This article has 44 citations and is from a peer-reviewed journal.

26. (NCT03831880 chunk 1):  Patient Perception of Treatment Burden in Weekly Versus Daily Growth Hormone Injections in Children With GHD. Pfizer. 2019. ClinicalTrials.gov Identifier: NCT03831880

27. (ibba2024isolatedgrowthhormone pages 12-13): Anastasia Ibba, Chiara Guzzetti, Lavinia Sanfilippo, and Sandro Loche. Isolated growth hormone deficiency. Endocrines, 5:341-353, Aug 2024. URL: https://doi.org/10.3390/endocrines5030025, doi:10.3390/endocrines5030025. This article has 2 citations.

28. (ranke2021shortandlongterm pages 3-4): Michael B. Ranke. Short and long-term effects of growth hormone in children and adolescents with gh deficiency. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.720419, doi:10.3389/fendo.2021.720419. This article has 86 citations.

29. (ibba2020igf1forthe pages 1-2): Anastasia Ibba, Francesca Corrias, Chiara Guzzetti, Letizia Casula, Mariacarolina Salerno, Natascia di Iorgi, Gianluca Tornese, Giuseppa Patti, Giorgio Radetti, Mohamad Maghnie, Marco Cappa, and Sandro Loche. Igf1 for the diagnosis of growth hormone deficiency in children and adolescents: a reappraisal. Nov 2020. URL: https://doi.org/10.1530/ec-20-0347, doi:10.1530/ec-20-0347. This article has 56 citations and is from a peer-reviewed journal.

30. (tran2023somatropinforgrowth pages 35-37): Khai Tran and Alexandra Grobelna. Somatropin for growth hormone deficiency. Canadian Journal of Health Technologies, Aug 2023. URL: https://doi.org/10.51731/cjht.2023.708, doi:10.51731/cjht.2023.708. This article has 2 citations.

31. (NCT04513171 chunk 1):  Safety and Efficacy of Y-shape Pegylated Somatropin in Growth Hormone Deficiency Children. Xiamen Amoytop Biotech Co., Ltd.. 2018. ClinicalTrials.gov Identifier: NCT04513171

32. (domene2018geneticmutationsin pages 16-17): S. Domené and H. Domené. Genetic mutations in the gh/igf axis. Pediatric endocrinology reviews : PER, 16 Suppl 1:39-62, Sep 2018. URL: https://doi.org/10.17458/per.vol16.2018.dd.geneticmutationsghigf, doi:10.17458/per.vol16.2018.dd.geneticmutationsghigf. This article has 20 citations.

33. (domene2018geneticmutationsin pages 5-7): S. Domené and H. Domené. Genetic mutations in the gh/igf axis. Pediatric endocrinology reviews : PER, 16 Suppl 1:39-62, Sep 2018. URL: https://doi.org/10.17458/per.vol16.2018.dd.geneticmutationsghigf, doi:10.17458/per.vol16.2018.dd.geneticmutationsghigf. This article has 20 citations.

## Artifacts

- [Edison artifact artifact-00](Isolated_Growth_Hormone_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.17458/per.vol16.2018.dd.geneticmutationsghigf` (9 mentions) - Identifier did not resolve to a record