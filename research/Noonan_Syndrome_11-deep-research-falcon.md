---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-18T09:43:46.950707'
end_time: '2026-08-18T09:52:49.898789'
duration_seconds: 542.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Noonan Syndrome 11 NS11 the MRAS-related form of Noonan syndrome OMIM
    618499 MONDO:0032786 caused by germline activating missense variants in the MRAS
    gene encoding the RAS-family GTPase M-Ras. NOT LZTR1-related Noonan syndrome and
    NOT any other numbered Noonan syndrome type.
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
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 4
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Noonan_Syndrome_11-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Noonan Syndrome 11 NS11 the MRAS-related form of Noonan syndrome OMIM 618499 MONDO:0032786 caused by germline activating missense variants in the MRAS gene encoding the RAS-family GTPase M-Ras. NOT LZTR1-related Noonan syndrome and NOT any other numbered Noonan syndrome type.
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Noonan Syndrome 11 NS11 the MRAS-related form of Noonan syndrome OMIM 618499 MONDO:0032786 caused by germline activating missense variants in the MRAS gene encoding the RAS-family GTPase M-Ras. NOT LZTR1-related Noonan syndrome and NOT any other numbered Noonan syndrome type.** covering all of the
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
- **Disease Name:** Noonan Syndrome 11 NS11 the MRAS-related form of Noonan syndrome OMIM 618499 MONDO:0032786 caused by germline activating missense variants in the MRAS gene encoding the RAS-family GTPase M-Ras. NOT LZTR1-related Noonan syndrome and NOT any other numbered Noonan syndrome type.
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Noonan Syndrome 11 NS11 the MRAS-related form of Noonan syndrome OMIM 618499 MONDO:0032786 caused by germline activating missense variants in the MRAS gene encoding the RAS-family GTPase M-Ras. NOT LZTR1-related Noonan syndrome and NOT any other numbered Noonan syndrome type.** covering all of the
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


# Noonan syndrome 11 (MRAS-related): disease-characteristics report

## Scope and evidence standard

This report concerns **only Noonan syndrome 11 (NS11) caused by germline activating MRAS variants**. It does not describe LZTR1-related Noonan syndrome or any other numbered Noonan syndrome. NS11 is exceptionally rare; consequently, the evidence base consists primarily of a few human cases, cell-functional studies, and structural/biochemical work. Statements labeled “general Noonan/RASopathy care” are clinical extrapolations, not MRAS-specific outcome evidence.

| domain | MRAS-specific established finding | evidence type/source | certainty or key limitation |
|---|---|---|---|
| Disease identity | Noonan syndrome 11 is the MRAS-related Noonan syndrome entity; key identifiers include OMIM 618499 and MONDO:0032786 | Aggregated disease-gene resource plus literature-linked target-disease evidence (OpenTargets Search: Noonan syndrome 11-MRAS) | High confidence for disease-gene mapping; sparse primary patient literature compared with other Noonan genes |
| Causal gene | The causal gene is **MRAS** (muscle RAS oncogene homolog), encoding the RAS-family small GTPase M-Ras | Human gene-disease association evidence and primary case reports (OpenTargets Search: Noonan syndrome 11-MRAS, higgins2017elucidationofmrasmediated pages 1-2) | High confidence |
| Reported pathogenic variants | Reported NS11 missense activating variants include **p.Gly23Val**, **p.Thr68Ile**, and **p.Gln71Arg** | Human case report and mechanistic/structural studies referencing NS variants (higgins2017elucidationofmrasmediated pages 1-2, bonsor2024rasandshoc2 pages 6-8, young2018shoc2–mras–pp1complexpositively pages 5-6) | p.Gly23Val and p.Thr68Ile are directly documented in the 2017 human report; p.Gln71Arg is strongly supported by later mechanistic literature but was not detailed in the retrieved human case excerpt |
| Inheritance | Reported human cases were **de novo**; disease mechanism is consistent with **autosomal dominant** transmission if inherited | Human trio/genotype-negative cohort evidence (higgins2017elucidationofmrasmediated pages 1-2, higgins2017elucidationofmrasmediated pages 8-9, higgins2017elucidationofmrasmediated pages 9-11) | Very small number of directly retrieved patients limits penetrance/segregation estimates |
| Molecular effect | NS11 is caused by **germline activating missense variants** producing **gain-of-function/constitutive activation** of MRAS | Human functional studies and structural/biochemical studies (higgins2017elucidationofmrasmediated pages 1-2, bonsor2024rasandshoc2 pages 6-8, higgins2017elucidationofmrasmediated pages 9-11, young2018shoc2–mras–pp1complexpositively pages 5-6) | High confidence for GOF mechanism |
| Core phenotype | Phenotype is dominated by **congenital or early-onset cardiac hypertrophy/HCM**, often with additional congenital heart disease, plus classic Noonan features such as distinctive facies, short stature, hypotonia/developmental delay, and learning difficulties | Direct human clinical evidence from reported patients (higgins2017elucidationofmrasmediated pages 1-2, higgins2017elucidationofmrasmediated pages 8-9, higgins2017elucidationofmrasmediated pages 2-4, higgins2017elucidationofmrasmediated pages 9-11) | High confidence that cardiac disease is prominent; exact frequency estimates remain uncertain because very few cases are available |
| Cardiac manifestations | Reported findings include **biventricular/left ventricular hypertrophy**, **outflow tract obstruction**, **pulmonary valve stenosis**, and **atrial septal defect**; one patient required **surgical myectomy** in childhood | Direct human clinical case data (higgins2017elucidationofmrasmediated pages 2-4, higgins2017elucidationofmrasmediated pages 11-12, higgins2017elucidationofmrasmediated pages 9-11) | Strong case-level evidence, but no MRAS-specific natural-history cohort |
| Development/growth | Reported non-cardiac findings include **short stature**, **global developmental delay**, **delayed walking/language**, **intellectual/learning difficulties**, **joint hypermobility**, **pectus excavatum**, **hypotonia**, and characteristic facies | Direct human clinical evidence (higgins2017elucidationofmrasmediated pages 8-9, higgins2017elucidationofmrasmediated pages 2-4, higgins2017elucidationofmrasmediated pages 6-8) | Frequencies cannot be robustly estimated from retrieved data |
| Signaling mechanism | Pathogenic MRAS variants enhance formation/function of the **SHOC2-MRAS-PP1C** holophosphatase complex, promoting **RAF inhibitory-site (S259/CR2-pS) dephosphorylation**, RAF activation, and downstream **ERK/MAPK** signaling | Biochemical, structural, and cell-based mechanistic evidence (bonsor2024rasandshoc2 pages 6-8, higgins2017elucidationofmrasmediated pages 9-11, young2018shoc2–mras–pp1complexpositively pages 5-6) | High mechanistic confidence; much evidence derives from in vitro/structural systems rather than patient tissue |
| Diagnostic approach | Diagnosis is established by **sequencing-based molecular testing**: WES/trio analysis identified one de novo case, and targeted sequencing of genotype-negative RASopathy patients with cardiac hypertrophy found another | Human diagnostic evidence (higgins2017elucidationofmrasmediated pages 1-2, higgins2017elucidationofmrasmediated pages 2-4, higgins2017elucidationofmrasmediated pages 9-11) | High confidence that MRAS should be included in RASopathy/HCM genomic testing; no MRAS-specific biomarker beyond genotype |
| Population frequency | Reported pathogenic variants are **ultra-rare/absent in population databases**; one 2017 report noted absence from >280,000 gnomAD alleles | Human genetic case evidence (higgins2017elucidationofmrasmediated pages 2-4) | Variant-level rarity supported; disease prevalence/incidence for MRAS-NS11 specifically is not established |
| Epidemiology | **No established MRAS-specific prevalence, incidence, sex ratio, founder effect, anticipation, or mosaicism data** were identified in retrieved evidence | Evidence-gap assessment from available literature context (higgins2017elucidationofmrasmediated pages 1-2, higgins2017elucidationofmrasmediated pages 9-11) | Major limitation: ultra-rare condition with only a handful of published cases in retrieved sources |
| Treatment | **No established MRAS-specific targeted therapy** has been proven in clinical practice; current care is syndrome-/phenotype-directed, especially cardiac management | Human case outcomes plus general RASopathy management context (higgins2017elucidationofmrasmediated pages 2-4, faienza2024cardiacphenotypeand pages 7-8) | Important limitation: treatment evidence is extrapolated largely from broader RASopathy/Noonan care, not MRAS-only cohorts |
| Trial landscape | **MEKinRAS (NCT06555237)** is a recruiting phase 2 trial of **trametinib** for RASopathy-associated HCM, but the registry does **not explicitly state MRAS-related NS11-specific eligibility or enrollment** | ClinicalTrials.gov registry evidence (NCT06555237 chunk 1) | Potential relevance to MRAS-HCM is indirect; not an MRAS-specific interventional study |
| Evidence base overall | The MRAS-specific evidence base remains **small but coherent**: rare de novo activating missense variants, recurrent severe cardiac phenotype, and a convergent SHOC2-MRAS-PP1C/RAF-ERK mechanism | Integrated human genetic, functional, structural, and registry evidence (higgins2017elucidationofmrasmediated pages 1-2, higgins2017elucidationofmrasmediated pages 9-11, bonsor2024rasandshoc2 pages 6-8, young2018shoc2–mras–pp1complexpositively pages 5-6, NCT06555237 chunk 1) | Main limitation is very limited patient count and lack of MRAS-specific long-term outcome studies |


*Table: This table summarizes the compact, MRAS-specific evidence base for Noonan syndrome 11, emphasizing what is directly established versus what remains uncertain. It is useful for separating firm gene/mechanism/phenotype findings from gaps in prevalence and treatment data.*

## 1. Disease information

**Definition.** NS11 is a congenital, lifelong RASopathy caused by heterozygous activating missense variants in **MRAS**, encoding the small RAS-family GTPase M-Ras. It combines a Noonan-pattern developmental phenotype—characteristic craniofacial appearance, growth impairment, skeletal findings and neurodevelopmental delay—with particularly prominent congenital or early-childhood cardiac hypertrophy/hypertrophic cardiomyopathy (HCM). Open Targets links MONDO:0032786 specifically to MRAS (ENSG00000158186), supported by the primary MRAS literature (including PMID 28289718). (OpenTargets Search: Noonan syndrome 11-MRAS)

**Identifiers and names.** 

- **OMIM:** 618499, *Noonan syndrome 11*.
- **MONDO:** MONDO:0032786, *Noonan syndrome 11*.
- **Causal-gene identity:** MRAS; Open Targets approved name “muscle RAS oncogene homolog.” (OpenTargets Search: Noonan syndrome 11-MRAS)
- **Common synonyms:** MRAS-related Noonan syndrome; MRAS-mediated Noonan syndrome; Noonan syndrome associated with MRAS; NS11.
- **Orphanet/MeSH/ICD:** no retrieved subtype-specific Orphanet, MeSH, ICD-10 or ICD-11 code was established. Coding generally falls under broader Noonan-syndrome/congenital-malformation categories; such codes do not uniquely identify MRAS-NS11.

The evidence combines **individual-level case reports/series** with aggregated disease resources. It is not derived from an EHR-scale cohort or population registry.

## 2. Etiology, risk and protective factors

The primary and sufficient cause is a **germline heterozygous activating MRAS missense variant**. The initially reported affected individuals carried de novo p.Gly23Val or p.Thr68Ile substitutions; later mechanistic literature recognizes p.Gln71Arg as another NS-associated constitutively active allele. (higgins2017elucidationofmrasmediated pages 1-2, bonsor2024rasandshoc2 pages 6-8)

The first p.Gly23Val case was identified through trio whole-exome sequencing (WES), and the variant was absent from more than 280,000 gnomAD alleles. Screening 109 unrelated genotype-negative patients with suspected RASopathy and cardiac hypertrophy identified the second de novo variant, p.Thr68Ile—approximately 0.9% of that highly selected cohort, not a population prevalence estimate. (higgins2017elucidationofmrasmediated pages 2-4, higgins2017elucidationofmrasmediated pages 9-11, higgins2017elucidationofmrasmediated pages 6-8)

**Risk factors.** The relevant risk is genetic: a pathogenic MRAS allele in the germline. Most directly documented cases were de novo, so absence of family history does not materially reduce risk in a clinically suggestive child. If an affected person transmits the allele, the expected Mendelian recurrence risk is 50% per pregnancy, although MRAS-specific penetrance cannot yet be quantified. Parental germline mosaicism remains theoretically possible but has not been quantified.

**Environmental, lifestyle, infectious and gene–environment factors.** No evidence establishes toxins, diet, smoking, occupation, infection, parental age or other environmental exposures as causes or modifiers of NS11. There are likewise no validated genetic or environmental protective factors. These are evidence gaps, not evidence of absolute absence.

## 3. Phenotypes

### MRAS-specific human observations

The directly documented phenotype is dominated by early cardiac disease. One female with p.Gly23Val had biventricular/left-ventricular hypertrophy beginning in infancy, biventricular outflow obstruction and surgical myectomy at age eight. She also had short stature, a long/dysmorphic face, low-set posteriorly rotated ears, global developmental delay and cognitive disability. (higgins2017elucidationofmrasmediated pages 2-4)

The p.Thr68Ile-positive female had cardiac hypertrophy, pulmonary-valve stenosis and an atrial septal defect, with ptosis, low-set posteriorly angulated ears, pectus excavatum, redundant palmar soft tissue/wrinkling, joint hypermobility and hypotonia. Development was delayed: independent walking at 2.5 years, sign language at 15 months, spoken words at four years and special-education support by kindergarten. (higgins2017elucidationofmrasmediated pages 8-9, higgins2017elucidationofmrasmediated pages 11-12)

Suggested phenotype annotations include:

| Phenotype | Type/course | Suggested HPO term |
|---|---|---|
| Hypertrophic cardiomyopathy/cardiac hypertrophy | Congenital or infantile; severity variable and potentially progressive/obstructive | HP:0001639; cardiac hypertrophy HP:0001712 |
| Left/biventricular outflow obstruction | Clinical/imaging sign; may require surgery | HP:0001698 or more specific obstruction term |
| Pulmonary-valve stenosis | Congenital structural cardiac sign | HP:0001642 |
| Atrial septal defect | Congenital structural cardiac sign | HP:0001631 |
| Short stature | Growth manifestation, childhood | HP:0004322 |
| Global developmental delay | Neurodevelopmental sign, early childhood | HP:0001263 |
| Intellectual/learning disability | Cognitive/functional manifestation | HP:0001249; HP:0001328 where appropriate |
| Hypotonia | Neuromuscular sign, infancy/childhood | HP:0001252 |
| Ptosis/hypertelorism/low-set ears | Dysmorphic signs | HP:0000508; HP:0000316; HP:0000369 |
| Pectus excavatum | Skeletal manifestation | HP:0000767 |
| Joint hypermobility | Musculoskeletal sign | HP:0001382 |

Because the published denominator is extremely small, percentages should not be calculated as stable NS11 frequencies. The strongest qualitative association is **cardiac hypertrophy/HCM**, while developmental, facial, growth and skeletal findings show variable expression. Disease-specific EQ-5D, SF-36, PROMIS or caregiver-burden data do not exist. Nevertheless, obstructive HCM, surgery, developmental delay and special-education needs plainly create substantial functional burden at the individual level. (higgins2017elucidationofmrasmediated pages 8-9, higgins2017elucidationofmrasmediated pages 2-4)

## 4. Genetic and molecular information

**Gene.** MRAS is the sole established causal gene for NS11. Open Targets identifies only MRAS as an associated target for MONDO:0032786. (OpenTargets Search: Noonan syndrome 11-MRAS)

**Variant class and origin.** Established disease alleles are germline, heterozygous missense variants with gain-of-function effects—not truncating loss-of-function alleles, chromosomal rearrangements or somatic-only mutations. Directly reported variants include:

- **p.Gly23Val**, reported as c.68G>T in detailed text; de novo and absent from >280,000 population alleles. The retrieved source contained one inconsistent predicted cDNA notation, so clinical reporting should use the transcript-specific laboratory HGVS record rather than infer it from the protein change. (higgins2017elucidationofmrasmediated pages 1-2, higgins2017elucidationofmrasmediated pages 2-4)
- **c.203C>T (p.Thr68Ile)**; de novo. (higgins2017elucidationofmrasmediated pages 8-9, higgins2017elucidationofmrasmediated pages 11-12)
- **p.Gln71Arg (Q71R)**; recognized in later structural/mechanistic studies as a constitutively active NS allele. (bonsor2024rasandshoc2 pages 6-8)

ClinVar classifications should be checked against the current transcript and submission date during implementation. Functional evidence strongly supports pathogenic/gain-of-function interpretation for these recurrent mechanistically coherent alleles, but this report should not substitute for current laboratory ACMG/AMP adjudication.

**Modifiers, epigenetics and chromosome abnormalities.** No validated modifier gene, MRAS-NS11 episignature, disease-specific methylation profile or recurrent large chromosomal abnormality has been established. No founder allele, anticipation or carrier-frequency estimate is available.

## 5. Environmental information

NS11 is not an infectious, toxic or lifestyle-mediated disease. No causal pathogen, occupational exposure, pollutant, radiation exposure, diet, alcohol or smoking association is known. Routine healthy lifestyle measures remain relevant to general cardiovascular health but do not prevent the germline disorder.

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. A germline activating substitution changes MRAS nucleotide-state regulation and/or effector interactions.
2. G23V, T68I and Q71R favor the constitutively active, GTP-bound state. Wild-type MRAS shares about 50% sequence identity with canonical RAS proteins but normally binds/activates RAF less efficiently; the disease alleles overcome normal control. (bonsor2024rasandshoc2 pages 6-8)
3. GTP-bound MRAS assembles the **SHOC2–MRAS–PP1C** holophosphatase at the plasma membrane. SHOC2 acts as scaffold and PP1C as catalytic phosphatase.
4. The complex dephosphorylates RAF’s conserved inhibitory CR2 site—classically CRAF Ser259/BRAF Ser365—releasing 14-3-3-mediated inhibition and facilitating RAF activation/dimerization.
5. RAF activates MEK and ERK, changing developmental gene expression, cell proliferation, differentiation and growth.
6. Dysregulated signaling in developing myocardium and other embryonic tissues produces HCM/structural heart disease, dysmorphism, impaired linear growth and neurodevelopmental abnormalities.

Cell experiments showed p.Gly23Val produced approximately fourfold greater GTP loading at five minutes and 40-fold greater loading at 30 minutes after EGF stimulation than wild-type MRAS, with increased ERK phosphorylation and serum-response-element transcription. (higgins2017elucidationofmrasmediated pages 1-2, higgins2017elucidationofmrasmediated pages 8-9, higgins2017elucidationofmrasmediated pages 9-11)

Young et al. summarized the biochemical result directly: germline MRAS/SHOC2/PPP1CB mutations enhance ternary-complex formation, which “specifically dephosphorylates an inhibitory site on RAF kinases, activating downstream signaling.” Their experiments further distinguish G23V, which can promote direct RAF binding and holophosphatase assembly, from T68I, which preferentially enhances SHOC2–PP1 interaction/RAF-phosphatase function. (young2018shoc2–mras–pp1complexpositively pages 5-6)

The 2024 structural review concludes that G23V, T68I and Q71R place MRAS in a constitutively active GTP-bound state, with Q71R adding contacts to SHOC2; measured complex affinities are in the low-nanomolar range. (bonsor2024rasandshoc2 pages 6-8, bonsor2024rasandshoc2 pages 19-20)

**Suggested GO annotations:** small GTPase-mediated signal transduction (GO:0007264); Ras protein signal transduction (GO:0007265); MAPK cascade (GO:0000165); positive regulation of ERK1/2 cascade (GO:0070374); protein dephosphorylation (GO:0006470); regulation of protein serine/threonine phosphatase activity; heart development (GO:0007507); cardiac muscle-cell development and proliferation.

**Likely relevant cell types:** cardiomyocyte (CL:0000746), cardiac fibroblast (CL:0000746-adjacent ontology mapping should be verified), endocardial/endothelial cells, neural progenitors and growth-plate chondrocytes. Direct NS11 single-cell evidence is absent; these are mechanistically plausible annotation targets, not demonstrated cell-selective lesions.

**Subcellular components:** plasma membrane (GO:0005886), cytosol (GO:0005829), protein-containing complex (GO:0032991), SHOC2–MRAS–PP1C complex where a dedicated ontology term is unavailable.

No NS11-specific metabolic, immune, inflammatory, oxidative-stress, transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic or multi-omic signature has been established. The available molecular profiling consists principally of targeted signaling assays and protein structures.

## 7. Anatomical structures affected

The **heart** is the best-supported primary organ, involving ventricular myocardium and potentially pulmonary valve/septa/outflow tracts. Suggested annotations are heart (UBERON:0000948), myocardium (UBERON:0002349), cardiac ventricle (UBERON:0002082), interventricular/atrial septal structures, pulmonary valve and ventricular outflow tract.

Secondary systems include craniofacial structures, skeleton/chest wall, joints, central nervous system/neurodevelopment and the somatic growth axis. No consistent lateralization is described. At subcellular level, disease originates in membrane-associated RAS signaling rather than a primary mitochondrial, lysosomal or endoplasmic-reticulum disorder.

## 8. Temporal development and natural history

Onset is **prenatal/congenital or early pediatric**, even if molecular diagnosis occurs later. Cardiac hypertrophy may be recognized in infancy and can progress to obstruction requiring childhood intervention. Developmental delay becomes apparent as milestones are missed; short stature emerges over childhood. (higgins2017elucidationofmrasmediated pages 8-9, higgins2017elucidationofmrasmediated pages 2-4)

NS11 is lifelong. There is no validated staging system, remission pattern, median progression rate or MRAS-specific longitudinal cohort. Critical windows include prenatal cardiac development, infancy for detection of HCM/feeding and developmental difficulties, early childhood for intervention, and later childhood/adulthood for arrhythmia, obstruction and heart-failure surveillance.

## 9. Inheritance and population

Inheritance is **autosomal dominant**, with most published cases arising de novo. Expressivity is variable, but penetrance cannot be estimated. Genetic anticipation is not expected for a missense RASopathy and has not been reported. Germline mosaicism, founder effects, consanguinity effects and geographic clustering have not been demonstrated.

There is no reliable NS11-specific prevalence, incidence, sex ratio, age distribution or ancestry enrichment. Both initially described patients were female and of European descent, but that observation is far too small and ascertainment-biased to infer demographic risk. (higgins2017elucidationofmrasmediated pages 9-11)

General Noonan/RASopathy prevalence estimates must not be assigned to NS11. The 109-person selected screening cohort yielded one additional MRAS case, but it consisted specifically of genotype-negative RASopathy patients with cardiac hypertrophy and therefore cannot estimate prevalence. (higgins2017elucidationofmrasmediated pages 6-8)

## 10. Diagnostics

### Clinical evaluation

Suspect NS11 when a child has Noonan-pattern dysmorphism and developmental/growth abnormalities together with **early or severe HCM**, particularly after common RASopathy genes are negative. Baseline evaluation should include physical/dysmorphology examination, three-generation pedigree, growth parameters, developmental assessment, ECG and echocardiography. Cardiac MRI/Holter monitoring is selected according to HCM severity, rhythm symptoms and image quality.

### Molecular confirmation

Preferred testing is a comprehensive **RASopathy panel including MRAS**, or an HCM/congenital-heart-disease panel that includes MRAS when syndromic features are present. Trio WES is useful when panel testing is negative and proved diagnostic in the discovery case. Genome sequencing can detect coding variants plus classes missed by exome/panel testing, but no recurrent NS11 structural variant is known. Sanger/orthogonal confirmation and parental testing establish de novo status. (higgins2017elucidationofmrasmediated pages 1-2, higgins2017elucidationofmrasmediated pages 2-4)

CMA, karyotype and FISH are not confirmatory for an MRAS missense disorder, but CMA may be appropriate when developmental anomalies suggest a copy-number differential. Mitochondrial, repeat-expansion and liquid-biopsy testing are not indicated for NS11 itself. There is no validated serum, enzyme, metabolomic or epigenomic diagnostic biomarker beyond the molecular variant.

### Differential diagnosis

Differentials include other molecular RASopathies—especially RIT1-, RAF1-, PTPN11-, SOS1-, KRAS-, SHOC2- and PPP1CB-related disease—and nonsyndromic sarcomeric HCM. NS11 is distinguished by a pathogenic activating **MRAS** allele, not phenotype alone. LZTR1-related Noonan syndrome is explicitly a different disease mechanism and must not be labeled NS11.

No newborn population screen exists. Cascade testing is appropriate after a familial pathogenic variant is identified; testing apparently unaffected parents also informs recurrence counseling.

## 11. Outcome and prognosis

No MRAS-specific five- or ten-year survival, life expectancy, mortality rate or validated prognostic model exists. Prognosis is likely driven chiefly by HCM severity, ventricular obstruction, arrhythmia and heart failure, but this is reasoned from the observed phenotype and broader HCM/RASopathy practice, not an NS11 survival cohort.

Documented morbidity includes childhood myectomy, developmental disability, special-education need, hypotonia and short stature. (higgins2017elucidationofmrasmediated pages 8-9, higgins2017elucidationofmrasmediated pages 2-4) No MRAS-specific tumor-risk estimate or evidence-based cancer-surveillance protocol has been established. Likewise, no disease-specific patient-reported outcome data exist.

## 12. Treatment

There is **no approved MRAS-specific disease-modifying therapy**. Management is multidisciplinary and phenotype-directed.

### Cardiac treatment

General RASopathy/HCM practice uses non-vasodilating beta-blockers for symptoms/obstruction; disopyramide may be added for left-ventricular outflow-tract obstruction. Severe symptomatic obstruction refractory to medication may require septal myectomy; advanced heart failure or refractory arrhythmia may warrant transplantation. These are general recommendations, although childhood myectomy has been used in an MRAS case. (higgins2017elucidationofmrasmediated pages 2-4, faienza2024cardiacphenotypeand pages 7-8)

Suggested NCIt intervention mappings include echocardiography (C16525), electrocardiography, beta-adrenergic blocker therapy, antiarrhythmic therapy, septal myectomy/cardiac surgery and heart transplantation; exact current NCIt codes should be verified during database ingestion.

### Developmental and supportive care

Early developmental evaluation, physical/occupational/speech therapy, individualized education, nutritional/feeding support and hearing/vision assessment should follow general Noonan care. Orthopedic, endocrine/growth, renal and hemostatic evaluations should be driven by examination and standard Noonan guidance. Evidence for these measures is not MRAS-specific.

### Targeted/experimental therapy

MEK inhibition is biologically rational because the causal pathway culminates in RAF–MEK–ERK hyperactivation, but efficacy and long-term safety in MRAS-NS11 are unproven. **NCT06555237 (MEKinRAS)** is a recruiting phase 2 randomized trial begun August 1, 2024, targeting 40 patients aged 0–18 years with genetically confirmed RASopathy and echocardiographic HCM. It compares trametinib 0.025 mg/kg orally once daily plus beta-blocker/disopyramide against standard therapy, measuring echocardiographic hypertrophy, NT-proBNP and high-sensitivity troponin I through 12 months. The Warsaw registry does not explicitly document an MRAS subgroup or MRAS-positive enrollment. (NCT06555237 chunk 1)

There is no established MRAS-directed gene therapy, CRISPR therapy, ASO, siRNA, cell therapy or immunotherapy. Structural studies identify the SHOC2–MRAS–PP1C interface as a potential drug target, but this remains preclinical and is largely being developed in oncology. (bonsor2024rasandshoc2 pages 6-8)

## 13. Prevention

Primary prevention by diet, vaccination or environmental modification is impossible because NS11 is germline genetic. Reproductive options after identification of a familial pathogenic variant include genetic counseling, prenatal diagnosis and preimplantation genetic testing. For a proven heterozygous affected parent, the theoretical recurrence probability is 50% per conception; after an apparently de novo case, recurrence is low but not zero because of possible parental germline mosaicism.

Secondary prevention consists of early molecular diagnosis and cardiac/developmental surveillance. Tertiary prevention includes prompt management of HCM/outflow obstruction, arrhythmias, developmental needs and other detected complications. There is no NS11-specific prophylactic medication or public-health screening program.

## 14. Other species and natural disease

MRAS signaling is evolutionarily conserved, and orthologs exist in standard vertebrate model species. However, no well-established naturally occurring veterinary disorder equivalent to human MRAS-NS11, breed association, zoonotic potential or cross-species transmission was identified. NS11 is not transmissible.

## 15. Model organisms and experimental systems

The strongest models are **in vitro biochemical and cellular systems**, not a validated whole-animal NS11 model. HEK293T/17 and related transfected-cell assays demonstrated enhanced GTP loading, ERK phosphorylation and transcriptional signaling by mutant MRAS. (higgins2017elucidationofmrasmediated pages 8-9, higgins2017elucidationofmrasmediated pages 9-11)

Purified-protein, crystallographic and cryo-EM studies define the SHOC2–MRAS–PP1C complex and effects of G23V, T68I and Q71R. These models provide high mechanistic resolution but cannot reproduce organism-level cardiomyopathy, development, penetrance or treatment toxicity. (bonsor2024rasandshoc2 pages 6-8, young2018shoc2–mras–pp1complexpositively pages 5-6)

No retrieved evidence established a knock-in mouse, rat, zebrafish, Drosophila, organoid or patient-derived iPSC model that comprehensively recapitulates MRAS-NS11. Such models—especially heterozygous variant-specific cardiomyocyte/iPSC and mouse or zebrafish knock-ins—remain important priorities for natural-history and therapeutic studies.

## Key evidence limitations and interpretation

1. **Very small patient numbers:** apparent phenotype frequencies are unstable and should remain qualitative.
2. **Ascertainment bias:** discovery focused on genotype-negative patients with cardiac hypertrophy, enriching the apparent HCM association.
3. **Mechanistic strength exceeds clinical depth:** biochemical causality is strong, but longitudinal prognosis, penetrance and treatment response remain poorly defined.
4. **No 2023–2024 MRAS-specific clinical cohort was retrieved:** recent work chiefly refines protein structure and therapeutic hypotheses rather than expanding natural history.
5. **General Noonan recommendations are not genotype-specific evidence:** cardiac and multidisciplinary care should be individualized, especially because severe HCM appears prominent in NS11.

## Principal publications and URLs

- Higgins EM et al. **“Elucidation of MRAS-mediated Noonan syndrome with cardiac hypertrophy.”** *JCI Insight*. Published March 2017. PMID **28289718**. DOI/URL: https://doi.org/10.1172/jci.insight.91225. The report identified de novo MRAS variants and concluded that mutant MRAS enhanced RAS/MAPK signaling. (higgins2017elucidationofmrasmediated pages 1-2, higgins2017elucidationofmrasmediated pages 2-4)
- Young LC et al. **“SHOC2–MRAS–PP1 complex positively regulates RAF activity and contributes to Noonan syndrome pathogenesis.”** *PNAS*. Published October 2018. PMID **30348783**. DOI/URL: https://doi.org/10.1073/pnas.1720352115. Abstract-level conclusion: the variants enhance a ternary complex that dephosphorylates inhibitory RAF and activates downstream signaling. (young2018shoc2–mras–pp1complexpositively pages 5-6)
- Motta M et al. **“Activating MRAS mutations cause Noonan syndrome associated with hypertrophic cardiomyopathy.”** *Human Molecular Genetics*. Published online 2019; volume publication July 2020. DOI/URL: https://doi.org/10.1093/hmg/ddz108; literature databases associated with the MRAS–NS11 record include PMID **31108500**. This is the key expanded human-genetic study, although complete patient-level tables were not retrievable in the present evidence set. (OpenTargets Search: Noonan syndrome 11-MRAS)
- Bonsor DA, Simanshu DK. **“RAS and SHOC2 Roles in RAF Activation and Therapeutic Considerations.”** *Annual Review of Cancer Biology*. Published June 2024. DOI/URL: https://doi.org/10.1146/annurev-cancerbio-062822-030450. This recent authoritative structural review identifies G23V, T68I and Q71R as constitutively active MRAS alleles. (bonsor2024rasandshoc2 pages 6-8)
- Faienza MF et al. **“Cardiac Phenotype and Gene Mutations in RASopathies.”** *Genes*. Published August 2024. DOI/URL: https://doi.org/10.3390/genes15081015. Its treatment discussion is RASopathy-wide rather than MRAS-specific. (faienza2024cardiacphenotypeand pages 7-8)
- ClinicalTrials.gov. **MEKinRAS, NCT06555237.** Registered/started 2024: https://clinicaltrials.gov/study/NCT06555237. It is potentially relevant to NS11-associated HCM but is not an MRAS-specific trial. (NCT06555237 chunk 1)

References

1. (OpenTargets Search: Noonan syndrome 11-MRAS): Open Targets Query (Noonan syndrome 11-MRAS, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (higgins2017elucidationofmrasmediated pages 1-2): Erin M. Higgins, J. Martijn Bos, Heather Mason-Suares, David J. Tester, Jaeger P. Ackerman, Calum A. MacRae, Katia Sol-Church, Karen W. Gripp, Raul Urrutia, and Michael J. Ackerman. Elucidation of mras-mediated noonan syndrome with cardiac hypertrophy. JCI Insight, Mar 2017. URL: https://doi.org/10.1172/jci.insight.91225, doi:10.1172/jci.insight.91225. This article has 111 citations and is from a domain leading peer-reviewed journal.

3. (bonsor2024rasandshoc2 pages 6-8): Daniel A. Bonsor and Dhirendra K. Simanshu. Ras and shoc2 roles in raf activation and therapeutic considerations. Jun 2024. URL: https://doi.org/10.1146/annurev-cancerbio-062822-030450, doi:10.1146/annurev-cancerbio-062822-030450. This article has 16 citations and is from a peer-reviewed journal.

4. (young2018shoc2–mras–pp1complexpositively pages 5-6): Lucy C. Young, Nicole Hartig, Isabel Boned del Río, Sibel Sari, Benjamin Ringham-Terry, Joshua R. Wainwright, Greg G. Jones, Frank McCormick, and Pablo Rodriguez-Viciana. Shoc2–mras–pp1 complex positively regulates raf activity and contributes to noonan syndrome pathogenesis. Proceedings of the National Academy of Sciences, 115:E10576-E10585, Oct 2018. URL: https://doi.org/10.1073/pnas.1720352115, doi:10.1073/pnas.1720352115. This article has 106 citations and is from a highest quality peer-reviewed journal.

5. (higgins2017elucidationofmrasmediated pages 8-9): Erin M. Higgins, J. Martijn Bos, Heather Mason-Suares, David J. Tester, Jaeger P. Ackerman, Calum A. MacRae, Katia Sol-Church, Karen W. Gripp, Raul Urrutia, and Michael J. Ackerman. Elucidation of mras-mediated noonan syndrome with cardiac hypertrophy. JCI Insight, Mar 2017. URL: https://doi.org/10.1172/jci.insight.91225, doi:10.1172/jci.insight.91225. This article has 111 citations and is from a domain leading peer-reviewed journal.

6. (higgins2017elucidationofmrasmediated pages 9-11): Erin M. Higgins, J. Martijn Bos, Heather Mason-Suares, David J. Tester, Jaeger P. Ackerman, Calum A. MacRae, Katia Sol-Church, Karen W. Gripp, Raul Urrutia, and Michael J. Ackerman. Elucidation of mras-mediated noonan syndrome with cardiac hypertrophy. JCI Insight, Mar 2017. URL: https://doi.org/10.1172/jci.insight.91225, doi:10.1172/jci.insight.91225. This article has 111 citations and is from a domain leading peer-reviewed journal.

7. (higgins2017elucidationofmrasmediated pages 2-4): Erin M. Higgins, J. Martijn Bos, Heather Mason-Suares, David J. Tester, Jaeger P. Ackerman, Calum A. MacRae, Katia Sol-Church, Karen W. Gripp, Raul Urrutia, and Michael J. Ackerman. Elucidation of mras-mediated noonan syndrome with cardiac hypertrophy. JCI Insight, Mar 2017. URL: https://doi.org/10.1172/jci.insight.91225, doi:10.1172/jci.insight.91225. This article has 111 citations and is from a domain leading peer-reviewed journal.

8. (higgins2017elucidationofmrasmediated pages 11-12): Erin M. Higgins, J. Martijn Bos, Heather Mason-Suares, David J. Tester, Jaeger P. Ackerman, Calum A. MacRae, Katia Sol-Church, Karen W. Gripp, Raul Urrutia, and Michael J. Ackerman. Elucidation of mras-mediated noonan syndrome with cardiac hypertrophy. JCI Insight, Mar 2017. URL: https://doi.org/10.1172/jci.insight.91225, doi:10.1172/jci.insight.91225. This article has 111 citations and is from a domain leading peer-reviewed journal.

9. (higgins2017elucidationofmrasmediated pages 6-8): Erin M. Higgins, J. Martijn Bos, Heather Mason-Suares, David J. Tester, Jaeger P. Ackerman, Calum A. MacRae, Katia Sol-Church, Karen W. Gripp, Raul Urrutia, and Michael J. Ackerman. Elucidation of mras-mediated noonan syndrome with cardiac hypertrophy. JCI Insight, Mar 2017. URL: https://doi.org/10.1172/jci.insight.91225, doi:10.1172/jci.insight.91225. This article has 111 citations and is from a domain leading peer-reviewed journal.

10. (faienza2024cardiacphenotypeand pages 7-8): Maria Felicia Faienza, Giovanni Meliota, Donatella Mentino, Romina Ficarella, Mattia Gentile, Ugo Vairo, and Gabriele D’amato. Cardiac phenotype and gene mutations in rasopathies. Genes, 15:1015, Aug 2024. URL: https://doi.org/10.3390/genes15081015, doi:10.3390/genes15081015. This article has 16 citations.

11. (NCT06555237 chunk 1):  MEK Inhibitors for the Treatment of Hypertrophic Cardiomyopathy in Patients With RASopathies. Medical University of Warsaw. 2024. ClinicalTrials.gov Identifier: NCT06555237

12. (bonsor2024rasandshoc2 pages 19-20): Daniel A. Bonsor and Dhirendra K. Simanshu. Ras and shoc2 roles in raf activation and therapeutic considerations. Jun 2024. URL: https://doi.org/10.1146/annurev-cancerbio-062822-030450, doi:10.1146/annurev-cancerbio-062822-030450. This article has 16 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Noonan_Syndrome_11-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.