---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T02:27:30.383051'
end_time: '2026-08-27T02:38:56.534623'
duration_seconds: 686.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Leber-like Hereditary Optic Neuropathy, Autosomal Recessive 1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Leber-like_Hereditary_Optic_Neuropathy_Autosomal_Recessive_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leber-like Hereditary Optic Neuropathy, Autosomal Recessive 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leber-like Hereditary Optic Neuropathy, Autosomal Recessive 1** covering all of the
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
- **Disease Name:** Leber-like Hereditary Optic Neuropathy, Autosomal Recessive 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leber-like Hereditary Optic Neuropathy, Autosomal Recessive 1** covering all of the
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


# Leber-like Hereditary Optic Neuropathy, Autosomal Recessive 1

## Executive summary

Leber-like hereditary optic neuropathy, autosomal recessive 1 is **DNAJC30-associated autosomal recessive Leber hereditary optic neuropathy**, commonly abbreviated **LHONAR1**, **arLHON**, or **DNAJC30-LHON**. It is a nuclear-encoded mitochondrial disease that clinically resembles classical, maternally inherited mtDNA-LHON: affected people—predominantly adolescent or young-adult males—develop painless, subacute central visual loss from bilateral retinal-ganglion-cell/optic-nerve degeneration. The defining cause is biallelic pathogenic variants in **DNAJC30**, most often the Eastern/Central European founder variant **NM_032317.3:c.152A>G, p.(Tyr51Cys)**. The strongest mechanistic model is defective repair/turnover of mitochondrial respiratory-chain complex I, causing complex-I deficiency and selective vulnerability of retinal ganglion cells. (OpenTargets Search: Leber-like hereditary optic neuropathy, autosomal recessive 1, kieninger2022dnajc30diseasecausinggene pages 1-2, stenton2022dnajc30defecta pages 1-2)

The disease has incomplete, sex-dependent penetrance, relatively frequent simultaneous bilateral onset, and—compared with mtDNA-LHON—an earlier average onset and better probability of meaningful visual recovery. Idebenone is used clinically, but DNAJC30-specific efficacy evidence remains observational rather than randomized. No DNAJC30-targeted gene therapy or disease-specific interventional trial was identified. (kieninger2022dnajc30diseasecausinggene pages 4-5, stenton2022dnajc30defecta pages 1-2, stenton2022dnajc30defecta pages 3-5)

The following table provides a knowledge-base-oriented synopsis.

| Domain | Evidence-based finding | Quantitative data | Suggested ontology IDs/terms | Evidence limitations |
|---|---|---|---|---|
| Identifiers | Disease resolves to DNAJC30-associated autosomal recessive Leber hereditary optic neuropathy, also called LHONAR1 / arLHON; Open Targets links the entity to MONDO_0958183 and DNAJC30; OMIM phenotype reported as 619382. Information here is disease-level synthesis from published cohorts/case series, not EHR-derived. (OpenTargets Search: Leber-like hereditary optic neuropathy, autosomal recessive 1, kieninger2022dnajc30diseasecausinggene pages 1-2, kieninger2022dnajc30diseasecausinggene pages 1-1) | MONDO:0958183; OMIM:619382 | MONDO:0958183; Leber-like hereditary optic neuropathy, autosomal recessive 1 | Orphanet, ICD, MeSH identifiers were not established in the retrieved evidence set. |
| Gene / variants | Causal gene is DNAJC30. Recurrent founder variant c.152A>G (p.Tyr51Cys) is the predominant disease allele; additional pathogenic/likely pathogenic variants reported include c.610G>T (p.Glu204*), c.230_232del (p.His77del), c.293A>G (p.Tyr98Cys), c.293A>C (p.Tyr98Ser), and c.130_131delTC (p.Ser44ValfsTer8). (OpenTargets Search: Leber-like hereditary optic neuropathy, autosomal recessive 1, major2023casereportmutations pages 1-2, kieninger2022dnajc30diseasecausinggene pages 6-6, kieninger2022dnajc30diseasecausinggene pages 5-6, stenton2022dnajc30defecta pages 1-2, skorczykwerner2023dnajc30genevariants pages 10-11) | c.152A>G accounts for ~90% of disease alleles in Central Europe and ~95% of alleles in the Polish cohort; gnomAD frequency for p.Tyr51Cys reported as 0.12% with no homozygotes reported in Stenton 2022. (kieninger2022dnajc30diseasecausinggene pages 3-4, stenton2022dnajc30defecta pages 1-2, skorczykwerner2023dnajc30genevariants pages 10-11) | HGNC: DNAJC30; Sequence variants as HGVS terms | No ClinVar accession numbers or HGNC numeric gene ID were provided in retrieved contexts. |
| Inheritance | Inheritance is autosomal recessive with biallelic DNAJC30 variants. Penetrance is incomplete and sex-dependent, with marked male predominance among manifesting patients. (stenton2022dnajc30defecta pages 1-2, wiggs2021dnajc30biallelicmutations pages 2-3) | In one Central European cohort, 5/35 patients were female (14.3%), ~6:1 male:female. Two asymptomatic homozygous carriers were reported in Stenton 2022. (kieninger2022dnajc30diseasecausinggene pages 4-5, kieninger2022dnajc30diseasecausinggene pages 6-6, stenton2022dnajc30defecta pages 1-2) | HP:0000007 Autosomal recessive inheritance; HP:0001411 Decreased penetrance | Formal penetrance percentage was not established in retrieved evidence. |
| Epidemiology / population | arLHON due to DNAJC30 is a recurrent cause of inherited optic neuropathy in Central/Eastern Europe and may be particularly common in Poland because of a founder effect. (major2023casereportmutations pages 1-2, kieninger2022dnajc30diseasecausinggene pages 3-4, skorczykwerner2023dnajc30genevariants pages 10-11) | 35/1202 screened Central European patients carried likely pathogenic DNAJC30 variants (2.9% detection rate); DNAJC30 accounted for 7.7% of LHON cases in one database; across European centers, DNAJC30 variants accounted for 4-27% of genetically confirmed LHON in the cited synthesis. (kieninger2022dnajc30diseasecausinggene pages 4-5, kieninger2022dnajc30diseasecausinggene pages 1-1, stenton2022dnajc30defecta pages 3-5) | Population descriptor only; no ontology ID established | No population-based prevalence or incidence per 100,000 was established. Data are referral/cohort based and geographically enriched. |
| Phenotype | Core presentation closely mimics mtDNA-LHON: painless subacute central visual loss, dyschromatopsia, central/cecocentral scotoma, optic disc microangiopathy early and temporal optic atrophy later. Bilateral involvement is the rule at follow-up. (kieninger2022dnajc30diseasecausinggene pages 3-4, kieninger2022dnajc30diseasecausinggene pages 6-6, skorczykwerner2023dnajc30genevariants pages 10-11) | Central/cecocentral field defects 96.6%; papillary microangiopathy 94.1%; temporally accentuated optic atrophy 91.7%; color vision disturbance 68.8%; bilateral onset 40%, unilateral then fellow-eye involvement 60%, all bilateral at follow-up. (kieninger2022dnajc30diseasecausinggene pages 3-4, kieninger2022dnajc30diseasecausinggene pages 6-6) | HP:0000648 Optic atrophy; HP:0000572 Loss of visual acuity; HP:0000555 Visual field defect; HP:0001098 Abnormality of color vision; HP:0007686 Scotoma; HP:0012800 Bilateral visual impairment | Detailed HPO mapping for fundus microangiopathy and OCT/VEP findings was not fully established from retrieved evidence. |
| Onset / course | Typically juvenile-to-young-adult onset, earlier than mtDNA-LHON, with subacute progression and relatively frequent spontaneous or treatment-associated recovery. (kieninger2022dnajc30diseasecausinggene pages 3-4, stenton2022dnajc30defecta pages 1-2, skorczykwerner2023dnajc30genevariants pages 10-11) | Mean/median onset about 18.5-19 years; reported range 9.5-45.1 years in Central Europe; one Polish case onset at 68 years. Median interval between eyes 3.5 weeks (range 1-17) in one subset. Spontaneous complete recovery of remaining vision reported in 45% at median 19 months in one cohort. (kieninger2022dnajc30diseasecausinggene pages 4-5, kieninger2022dnajc30diseasecausinggene pages 3-4, skorczykwerner2023dnajc30genevariants pages 10-11) | HP:0003596 Middle age onset not typical; HP:0011462 Young adult onset; course descriptors not uniquely ontologized here | Staging schema is not established; recovery definitions vary across studies. |
| Mechanism / pathophysiology | DNAJC30 encodes a mitochondrial chaperone implicated in respiratory-chain complex I maintenance/repair/turnover; loss leads to isolated complex I deficiency, impaired ATP-linked bioenergetics and likely increased oxidative stress, producing selective retinal ganglion-cell vulnerability analogous to LHON biology. DNAJC30 also has reported interaction with ATP synthase/complex V. (kieninger2022dnajc30diseasecausinggene pages 1-2, stenton2022dnajc30defecta pages 1-2, wiggs2021dnajc30biallelicmutations pages 2-3) | Near-complete loss of DNAJC30 protein expression reported for the founder variant; patient/Leigh cases showed isolated RCCI deficiency on enzyme analysis. (stenton2022dnajc30defecta pages 1-2, stenton2022dnajc30defecta pages 3-5) | GO:0005747 mitochondrial respiratory chain complex I; GO:0006119 oxidative phosphorylation; GO:0006979 response to oxidative stress; GO:0006091 generation of precursor metabolites and energy | Much downstream ROS/RGC apoptosis detail is inferred from broader LHON biology rather than directly quantified in DNAJC30 patient retina. |
| Anatomy / cells / subcellular location | Primary affected tissue is the optic nerve/retinal ganglion cell pathway. Subcellular localization is mitochondrial, especially respiratory-chain machinery. (kieninger2022dnajc30diseasecausinggene pages 1-2, wiggs2021dnajc30biallelicmutations pages 2-3) | Bilateral optic neuropathy predominates; extraocular manifestations absent in most arLHON cases, but Leigh syndrome and occasional motor features were reported in a minority. (major2023casereportmutations pages 1-2, kieninger2022dnajc30diseasecausinggene pages 6-6, stenton2022dnajc30defecta pages 1-2) | UBERON:0000966 retina; UBERON:0000390 optic nerve; CL:0000705 retinal ganglion cell; GO:0005739 mitochondrion; GO:0005743 mitochondrial inner membrane | No direct retinal histopathology or single-cell localization studies were identified for this disease. |
| Diagnostics | Diagnosis relies on clinical recognition of LHON-like optic neuropathy plus molecular confirmation of biallelic DNAJC30 variants. DNAJC30 screening is recommended in mtDNA-negative LHON, especially in Central/Eastern European patients; because DNAJC30 is single exon, Sanger sequencing can be a practical first test in Poland. (major2023casereportmutations pages 1-2, kieninger2022dnajc30diseasecausinggene pages 1-1, skorczykwerner2023dnajc30genevariants pages 10-11) | Central European detection rate 2.9% (35/1202). In the Polish study, 46 clinically diagnosed LHON patients had DNAJC30 findings and 32 were diagnosed after DNAJC30 testing was introduced locally. (kieninger2022dnajc30diseasecausinggene pages 1-1, skorczykwerner2023dnajc30genevariants pages 10-11) | Diagnostic concepts: molecular genetic testing; ophthalmic exam; visual field testing; OCT/VEP not fully ontologized here | No disease-specific formal diagnostic criteria, biomarker panel, or screening guideline were retrieved. |
| Prognosis | Compared with mtDNA-LHON, DNAJC30 arLHON generally shows better visual prognosis, including higher spontaneous recovery and more favorable idebenone-associated outcomes. (major2023casereportmutations pages 1-2, stenton2022dnajc30defecta pages 1-2, stenton2022dnajc30defecta pages 3-5) | Median visual acuity improved from 1.3 logMAR at nadir to 0.5 logMAR at last visit in one cohort; clinically relevant recovery with idebenone in at least one eye 77% in arLHON versus 43% in mtLHON; spontaneous recovery 69% untreated arLHON versus 30% untreated mtLHON. (kieninger2022dnajc30diseasecausinggene pages 3-4, stenton2022dnajc30defecta pages 3-5) | Outcome terms: visual recovery; optic atrophy | No survival, mortality, or life-expectancy estimates specific to isolated arLHON were established. Leigh-spectrum cases likely have different prognosis. |
| Treatment | No DNAJC30-specific approved therapy exists. Idebenone is the principal disease-directed treatment used in practice by extrapolation from LHON and supported by observational DNAJC30 data suggesting higher recovery rates/shorter recovery time. Low-vision/visual rehabilitation is supportive standard care. MT-ND4 gene therapy trials are not genotype-matched for DNAJC30 disease. (major2023casereportmutations pages 1-2, stenton2022dnajc30defecta pages 3-5, kieninger2022dnajc30diseasecausinggene pages 1-1) | No randomized DNAJC30-specific trial identified; one Central European patient had taken idebenone for 6 months but recovered before treatment initiation; observational cohort comparisons favored idebenone-treated arLHON. (kieninger2022dnajc30diseasecausinggene pages 3-4, stenton2022dnajc30defecta pages 3-5) | NCIT:C952 Idebenone; NCIT terms for low vision rehabilitation/supportive care if used in downstream curation | Evidence is observational and partly extrapolated from mtDNA-LHON; no DNAJC30-targeted interventional trial was retrieved. |
| Prevention / counseling | Primary prevention is not established. Practical prevention focuses on genetic counseling, carrier/family testing, and reproductive counseling for an autosomal recessive condition. General LHON advice on smoking/alcohol avoidance may be reasonable but is extrapolated, not disease-specific evidence. (wiggs2021dnajc30biallelicmutations pages 2-3, kieninger2022dnajc30diseasecausinggene pages 1-1) | Not established quantitatively for DNAJC30 arLHON | HP:0000007 Autosomal recessive inheritance; carrier testing/cascade testing concepts | No disease-specific studies of environmental triggers, protective factors, prenatal screening uptake, or PGT outcomes were retrieved. |
| Other species / natural disease | No naturally occurring veterinary disease equivalent was established from retrieved evidence. (OpenTargets Search: Leber-like hereditary optic neuropathy, autosomal recessive 1) | Not established | NCBI Taxon IDs not established | Evidence absent in retrieved set. |
| Model organisms / experimental systems | Disease mechanism is supported mainly by patient-based biochemical evidence and broader mitochondrial functional studies; no validated DNAJC30-specific optic-neuropathy animal model was established in the retrieved evidence. Leigh-spectrum/digenic observations suggest useful mechanistic complexity but not a dedicated model system. (stenton2022dnajc30defecta pages 1-2, wiggs2021dnajc30biallelicmutations pages 2-3) | Not established | Experimental system concepts: patient fibroblasts; mitochondrial enzyme assay | Model-organism availability, recapitulation fidelity, and resource identifiers were not established from retrieved sources. |


*Table: This table condenses the current evidence base for DNAJC30-associated autosomal recessive Leber hereditary optic neuropathy into knowledge-base-ready domains. It highlights what is well supported by cohort data and what remains unknown or only extrapolated from broader LHON literature.*

## 1. Disease information

### Definition and identifiers

* **Preferred disease name:** Leber-like hereditary optic neuropathy, autosomal recessive 1.
* **Common names:** autosomal recessive Leber hereditary optic neuropathy; recessive LHON; arLHON; LHONAR1; DNAJC30-associated LHON; DNAJC30 optic neuropathy.
* **MONDO:** **MONDO:0958183**.
* **OMIM phenotype:** **619382**.
* **Causal gene:** **DNAJC30**, ENSG00000176410, encoding DnaJ heat-shock-protein-family member C30. Open Targets associates this disease entity with DNAJC30 and cites the discovery and replication literature, including PMID **33465056**. (OpenTargets Search: Leber-like hereditary optic neuropathy, autosomal recessive 1)
* **Orphanet, MeSH, ICD-10 and ICD-11:** no unique disease-specific identifiers were verified in the retrieved evidence. In practice, the disorder may be indexed under LHON, hereditary optic atrophy, or mitochondrial disease, but these broader codes should not be represented as unique LHONAR1 identifiers without terminology-service confirmation.

The evidence is primarily **aggregated disease-level information from published referral cohorts and case series**, with underlying observations derived from individual patients. It is not an EHR-derived population study.

### Key primary sources

* Stenton et al., *Brain*, published February 2022, DOI: [10.1093/brain/awac052](https://doi.org/10.1093/brain/awac052). The abstract states: **“The recent description of biallelic DNAJC30 variants in Leber hereditary optic neuropathy (LHON) and Leigh syndrome challenged the longstanding assumption for LHON to be exclusively maternally inherited.”** (stenton2022dnajc30defecta pages 1-2)
* Kieninger et al., *Journal of Medical Genetics*, online/publication record January 2022, DOI: [10.1136/jmedgenet-2021-108235](https://doi.org/10.1136/jmedgenet-2021-108235). Its abstract reports likely pathogenic variants in **35/1,202 patients (2.9%)**. (kieninger2022dnajc30diseasecausinggene pages 1-1)
* Major et al., *Frontiers in Neurology*, December 2023, DOI: [10.3389/fneur.2023.1292320](https://doi.org/10.3389/fneur.2023.1292320). The abstract describes three Eastern European patients with homozygous p.Tyr51Cys and emphasizes diagnostic screening in molecularly unresolved LHON. (major2023casereportmutations pages 1-2)
* Skorczyk-Werner et al., *International Journal of Molecular Sciences*, December 2023, DOI: [10.3390/ijms242417496](https://doi.org/10.3390/ijms242417496). This is a large Polish DNAJC30-LHON series. (skorczykwerner2023dnajc30genevariants pages 10-11)

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is **biallelic germline pathogenic or likely pathogenic DNAJC30 variants**. This is a Mendelian, autosomal recessive nuclear-genome disorder—not mitochondrial inheritance—although the affected protein operates within mitochondria. (OpenTargets Search: Leber-like hereditary optic neuropathy, autosomal recessive 1, stenton2022dnajc30defecta pages 1-2)

### Genetic risk factors

The major risk genotype in Europe is homozygosity or compound heterozygosity involving **c.152A>G, p.(Tyr51Cys)**. A Central European analysis found this allele on approximately 90% of disease chromosomes; a Polish analysis estimated approximately 95%. Founder-haplotype evidence included a linked 287-bp microsatellite allele on 85% of disease chromosomes versus 12.5% of controls. The founder event has been estimated at approximately 85 generations ago. (kieninger2022dnajc30diseasecausinggene pages 4-5, major2023casereportmutations pages 1-2, skorczykwerner2023dnajc30genevariants pages 10-11)

**Male sex** strongly increases the probability of clinical expression among biallelic carriers. In one 35-patient cohort only 5 patients, or 14.3%, were female, approximating a 6:1 male:female ratio. Nevertheless, females can be affected and sex is a penetrance modifier, not an inheritance rule. (kieninger2022dnajc30diseasecausinggene pages 4-5, kieninger2022dnajc30diseasecausinggene pages 6-6)

Possible second-locus modifiers have been proposed where severe Leigh-spectrum disease co-occurred with heterozygous variants in complex-I genes such as **NDUFS8, NDUFA9, or NDUFS2**. This is emerging digenic evidence rather than a validated clinical risk model. Mitochondrial haplogroup J was reportedly enriched in early DNAJC30 series but did not fully explain penetrance or male bias. (wiggs2021dnajc30biallelicmutations pages 2-3, stenton2022dnajc30defecta pages 3-5)

### Environmental and protective factors

No DNAJC30-specific study established smoking, alcohol, occupational toxins, diet, exercise, infection, or medication exposure as penetrance modifiers. Avoidance of smoking, heavy alcohol use, and mitochondrial toxins is often advised in LHON care, but for LHONAR1 this is **extrapolated from mtDNA-LHON**, not demonstrated gene–environment evidence.

No verified genetic protective allele, diet, supplement, vaccine, or lifestyle intervention prevents disease expression. Asymptomatic homozygotes demonstrate incomplete penetrance, but the protective determinants remain unknown. (stenton2022dnajc30defecta pages 1-2, wiggs2021dnajc30biallelicmutations pages 2-3)

## 3. Phenotypes

The phenotype is an optic neuropathy rather than a primary photoreceptor or retinal-pigment-epithelium dystrophy.

| Manifestation | Type and characteristics | Frequency/data | Suggested HPO |
|---|---|---:|---|
| Reduced central visual acuity | Clinical sign; painless, acute/subacute; severe at nadir but variably recoverable | Median 1.3 logMAR at nadir and 0.5 logMAR at last observation in one cohort | HP:0000572, visual-acuity loss |
| Bilateral visual impairment | Sign; simultaneous or sequential | 40% bilateral at onset; 60% initially unilateral; 100% bilateral by documented follow-up | HP:0012800 |
| Central/cecocentral scotoma | Visual-field abnormality reflecting papillomacular-bundle injury | 96.6% | HP:0007686; HP:0000555 |
| Optic-disc microangiopathy | Early funduscopic sign, including peripapillary telangiectatic/microvascular change | 94.1% | Use an abnormal optic-disc morphology/vasculature term after HPO terminology validation |
| Temporal optic atrophy/pallor | Later physical sign; progressive structural consequence | 91.7% | HP:0000648 |
| Dyschromatopsia | Functional sign; impaired color perception | 68.8% | HP:0001098 |
| Fellow-eye conversion | Temporal feature | Median 3.5 weeks; range 1–17 weeks in one documented subset | Encode as bilateral/sequential involvement rather than a distinct phenotype |

These quantitative findings come principally from the Central European cohort and should not be treated as universal population frequencies. (kieninger2022dnajc30diseasecausinggene pages 4-5, kieninger2022dnajc30diseasecausinggene pages 3-4, kieninger2022dnajc30diseasecausinggene pages 6-6)

OCT is expected to show acute retinal-nerve-fiber-layer swelling followed by thinning, particularly in papillomacular/temporal sectors, and visual evoked potentials may show optic-nerve dysfunction. However, robust DNAJC30-specific OCT and VEP frequency estimates were not available in the retrieved evidence.

Most patients have isolated optic neuropathy. Rare biallelic DNAJC30 presentations include childhood- or adult-onset **Leigh syndrome**, movement/motor manifestations, and proposed digenic complex-I disease. These severe syndromic presentations should be recorded separately from isolated LHONAR1 rather than assumed to be routine disease features. (major2023casereportmutations pages 1-2, stenton2022dnajc30defecta pages 1-2, stenton2022dnajc30defecta pages 3-5)

Central vision loss affects reading, facial recognition, education, employment, driving, and independent navigation. No LHONAR1-specific EQ-5D, SF-36, PROMIS, or vision-related quality-of-life dataset was identified.

## 4. Genetic and molecular information

### Causal gene and protein

**DNAJC30** is a single-exon nuclear gene on chromosome 7q11.23. It encodes a mitochondrial DnaJ/Hsp40-family co-chaperone. Reported functional domains include a conserved J domain and a C-terminal transmembrane region. The protein participates in complex-I maintenance/repair and has also been reported to interact with ATP-synthase/complex V. (kieninger2022dnajc30diseasecausinggene pages 1-2, kieninger2022dnajc30diseasecausinggene pages 5-6, stenton2022dnajc30defecta pages 1-2)

### Reported pathogenic/likely pathogenic variants

* **c.152A>G, p.(Tyr51Cys):** recurrent missense founder allele; dominant contributor to European LHONAR1. Reported gnomAD frequency was approximately 0.12% with no homozygotes in the cited dataset. Functional evidence indicates near-complete loss of DNAJC30 protein. (stenton2022dnajc30defecta pages 1-2)
* **c.230_232del, p.(His77del):** in-frame deletion within the conserved J domain; reported homozygously in two Turkish brothers. (kieninger2022dnajc30diseasecausinggene pages 6-6, kieninger2022dnajc30diseasecausinggene pages 5-6)
* **c.610G>T, p.(Glu204Ter):** nonsense variant upstream of the transmembrane domain. (kieninger2022dnajc30diseasecausinggene pages 6-6, kieninger2022dnajc30diseasecausinggene pages 5-6)
* **c.293A>G, p.(Tyr98Cys):** novel missense variant reported in the 2023 Polish cohort. (skorczykwerner2023dnajc30genevariants pages 10-11)
* **c.293A>C, p.(Tyr98Ser):** ultra-rare missense variant reported in LHONAR1. (skorczykwerner2023dnajc30genevariants pages 10-11)
* **c.130_131delTC, p.(Ser44ValfsTer8):** frameshift allele also reported in Leigh syndrome. (major2023casereportmutations pages 1-2, skorczykwerner2023dnajc30genevariants pages 10-11)
* Other reported rare substitutions include c.232C>T and c.302T>A; variant-level ClinVar assertions should be checked directly before assigning ACMG classes in a production knowledge base. (major2023casereportmutations pages 1-2)

All are presumed or demonstrated **germline** variants. Somatic causation is not supported. Loss of protein or disruption of chaperone-domain function is consistent with loss of function, although the recurrent missense allele may act through protein instability rather than a simple null transcript.

No disease-specific pathogenic chromosomal rearrangement, repeat expansion, or epigenetic lesion is established. DNAJC30 lies within the Williams–Beuren critical region, but heterozygous 7q11.23 deletion is a different genomic disorder and does not establish recessive LHONAR1.

## 5. Environmental information

No infectious agent causes or triggers LHONAR1. No radiation, pollutant, occupational exposure, or lifestyle exposure has been proven causal. Likewise, no disease-specific CTD-style chemical interaction or prospective exposure study was identified. Smoking and excessive alcohol avoidance are prudent mitochondrial-health recommendations but remain indirect for this genotype.

Suggested chemical annotations for broader mechanistic curation include oxygen-derived reactive species (**CHEBI:26523**) and ATP (**CHEBI:15422**); these describe downstream bioenergetic biology, not diagnostic biomarkers.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic DNAJC30 pathogenic variants reduce or abolish functional mitochondrial DNAJC30.
2. **Primary molecular defect:** defective chaperone-dependent repair/turnover of damaged respiratory-chain complex-I subunits permits dysfunctional complex I to accumulate.
3. **Biochemical defect:** isolated complex-I deficiency impairs NADH-linked electron transport, oxidative phosphorylation, and ATP generation; electron leakage is expected to increase oxidative stress.
4. **Cellular stress:** highly energy-dependent retinal ganglion cells, especially those forming the papillomacular bundle, cannot maintain axonal bioenergetics and redox homeostasis.
5. **Tissue injury:** retinal-ganglion-cell dysfunction and subsequent cell/axon loss produce central scotoma, dyschromatopsia, temporal retinal-nerve-fiber loss, and optic atrophy.
6. **Clinical outcome:** painless subacute central visual loss, usually involving both eyes over days to weeks.

Patient and Leigh-spectrum biochemical studies demonstrated isolated respiratory-chain complex-I deficiency; p.Tyr51Cys was associated with near-complete loss of DNAJC30 protein. These are direct DNAJC30 observations. The precise ROS-to-apoptosis sequence in human retinal ganglion cells is principally inferred from broader LHON biology because affected retinal tissue is rarely available. (stenton2022dnajc30defecta pages 1-2, stenton2022dnajc30defecta pages 3-5)

**Suggested GO annotations:** mitochondrion (GO:0005739); mitochondrial inner membrane (GO:0005743); mitochondrial respiratory-chain complex I (GO:0005747); oxidative phosphorylation (GO:0006119); respiratory electron transport chain (GO:0022904); response to oxidative stress (GO:0006979); ATP metabolic process (GO:0046034); protein-folding/chaperone-mediated protein-quality-control terms after gene-specific GO validation.

**Suggested Cell Ontology:** retinal ganglion cell (**CL:0000705**). Other relevant but indirect cells include optic-nerve oligodendrocytes and astrocytes; primary causal injury is neuronal/axonal rather than an established immune-mediated process.

No disease-specific immune, inflammatory, transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic signature has been validated for clinical use. A 2024 LHON epigenetics study concerned mtDNA-ND4/NDUFS4-related biology and should not be attributed specifically to DNAJC30-LHON.

## 7. Anatomical structures affected

* **Primary organ/system:** eye–central nervous system visual pathway.
* **Primary anatomical sites:** retina (**UBERON:0000966**), retinal nerve-fiber layer, optic disc/optic-nerve head, optic nerve (**UBERON:0000390**), particularly papillomacular fibers.
* **Primary cell:** retinal ganglion cell (**CL:0000705**) and its axon.
* **Subcellular compartment:** mitochondrion (**GO:0005739**), mitochondrial inner membrane (**GO:0005743**), respiratory-chain complex I (**GO:0005747**).
* **Laterality:** bilateral; onset may be synchronous or sequential and can initially be asymmetric. (kieninger2022dnajc30diseasecausinggene pages 4-5, kieninger2022dnajc30diseasecausinggene pages 3-4)

Secondary brain involvement is not characteristic of isolated LHONAR1. Basal-ganglia/brainstem disease pertains to the rarer DNAJC30-associated Leigh-spectrum phenotype.

## 8. Temporal development

Typical onset is in adolescence or young adulthood. Central European estimates center around 18.5–19 years, with a 9.5–45.1-year range; a Polish patient with onset at 68 years demonstrates that late onset is possible. (kieninger2022dnajc30diseasecausinggene pages 4-5, skorczykwerner2023dnajc30genevariants pages 10-11)

A practical clinical sequence is:

* **Presymptomatic:** biallelic carrier with normal functional vision; penetrance is incomplete.
* **Acute/subacute phase:** painless central blur and color loss in one or both eyes; disc microangiopathy may be visible.
* **Dynamic phase:** fellow-eye involvement commonly follows within weeks; central/cecocentral scotoma deepens.
* **Atrophic phase:** temporal disc pallor and retinal-nerve-fiber loss emerge.
* **Recovery/stable chronic phase:** some patients recover meaningful acuity over months to years, although central field and color deficits may persist.

In one cohort, spontaneous complete recovery occurred in 45% at a median 19 months. Another synthesis found spontaneous clinically relevant recovery in 69% of untreated arLHON versus 30% of untreated mtDNA-LHON. Definitions and follow-up differed, so these estimates should not be pooled uncritically. (kieninger2022dnajc30diseasecausinggene pages 3-4, stenton2022dnajc30defecta pages 3-5)

There is no validated staging system, remission definition, or proven preclinical intervention window. Biologically, treatment before irreversible ganglion-cell loss is considered preferable.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two heterozygous parents, each pregnancy has the standard theoretical probabilities of 25% biallelic, 50% heterozygous carrier, and 25% inheriting neither familial allele. Because penetrance is incomplete, a biallelic genotype does not guarantee optic neuropathy; male carriers are substantially more likely to manifest disease. Two asymptomatic homozygous carriers were documented in the 2022 Brain series. (stenton2022dnajc30defecta pages 1-2)

No anticipation is expected. Germline mosaicism has not emerged as a characteristic mechanism. Consanguinity can increase the probability of biallelic rare variants, but the common European founder allele permits disease in non-consanguineous families.

Population-based prevalence and annual incidence are unknown. Referral-series statistics include:

* 35/1,202 suspected LHON/optic-atrophy patients, or **2.9%**, in a Central European screen;
* **7.7%** of LHON cases in one diagnostic database;
* **4–27%** of genetically confirmed LHON across cited European centers;
* a 2023 Polish cohort in which DNAJC30-associated disease was reported as more frequent than mtDNA-LHON among tested Polish patients. (kieninger2022dnajc30diseasecausinggene pages 4-5, kieninger2022dnajc30diseasecausinggene pages 1-1, skorczykwerner2023dnajc30genevariants pages 10-11, stenton2022dnajc30defecta pages 3-5)

These are diagnostic yields, not general-population prevalence estimates. Geographic enrichment is strongest in Poland and broader Central/Eastern Europe, including Germany, Austria, Russia, Ukraine, and Romania. (major2023casereportmutations pages 1-2, kieninger2022dnajc30diseasecausinggene pages 1-2)

## 10. Diagnostics

### Clinical evaluation

Recommended evaluation includes best-corrected visual acuity, color vision, automated or kinetic visual fields, dilated fundus examination, optic-disc photography, OCT of the peripapillary RNFL and macular ganglion-cell complex, and—when uncertainty remains—visual evoked potentials/electroretinography. MRI of brain and orbits with contrast is appropriate when inflammation, compression, demyelination, or atypical syndromic disease is suspected.

There is no specific blood metabolite or enzyme biomarker for isolated LHONAR1. Respiratory-chain enzyme testing can demonstrate complex-I deficiency but is not required when phenotype and genotype are definitive.

### Genetic workflow

1. In clinically suspected LHON, test the three common mtDNA variants and preferably sequence the complete mitochondrial genome.
2. If mtDNA testing is negative—or immediately in a population with high founder frequency—test **DNAJC30**, ensuring detection of biallelic sequence variants.
3. A hereditary optic-neuropathy/mitochondrial panel should include DNAJC30 plus relevant differential genes such as **OPA1, OPA3, WFS1, TMEM126A, ACO2, RTN4IP1, NDUFS2, MCAT, MECR**, and other complex-I/optic-atrophy genes.
4. WES or WGS is useful for panel-negative or syndromic cases and can identify second-locus complex-I variants. CNV analysis should accompany broad sequencing where technically appropriate.
5. Confirm segregation and phase in parents; test at-risk siblings and adult relatives with counseling.

Because DNAJC30 is single exon and p.Tyr51Cys dominates Polish cases, the 2023 Polish investigators proposed Sanger sequencing as a cost-efficient first-line local strategy. In genetically heterogeneous populations, a combined mtDNA+nuclear panel is more comprehensive. (major2023casereportmutations pages 1-2, kieninger2022dnajc30diseasecausinggene pages 1-1, skorczykwerner2023dnajc30genevariants pages 10-11)

CMA, karyotyping, FISH, and repeat-expansion testing are not routine for isolated LHONAR1. mtDNA testing remains essential to exclude classical LHON but cannot diagnose nuclear DNAJC30 disease.

### Differential diagnosis

Major differentials are mtDNA-LHON; dominant optic atrophy; recessive optic atrophies; toxic/nutritional optic neuropathy; optic neuritis and multiple-sclerosis-spectrum disease; neuromyelitis optica/MOG-associated disease; compressive/infiltrative optic neuropathy; glaucoma; macular disease; and inherited retinal dystrophy. Painless central/cecocentral loss, sequential bilateral disease, early disc microangiopathy, later temporal pallor, and a biallelic DNAJC30 genotype support LHONAR1.

## 11. Outcome and prognosis

Isolated LHONAR1 is vision-threatening but is not known to reduce life expectancy. Disease-specific mortality and survival statistics are not applicable/available. Leigh-spectrum DNAJC30 disease is clinically distinct and may carry neurological morbidity and mortality not representative of isolated optic neuropathy.

Visual prognosis appears better than in common mtDNA-LHON. One cohort improved from median 1.3 logMAR at nadir to 0.5 logMAR at last assessment. In a comparative observational analysis, 77% of idebenone-treated arLHON patients achieved clinically relevant recovery in at least one eye versus 43% of mtDNA-LHON patients; untreated recovery was 69% versus 30%, respectively. Younger onset, genotype, treatment timing, and residual ganglion-cell reserve may influence outcome, but no validated prognostic calculator exists. (kieninger2022dnajc30diseasecausinggene pages 3-4, stenton2022dnajc30defecta pages 3-5)

Persistent morbidity can include central scotoma, impaired color discrimination, reduced contrast sensitivity, inability to drive/read ordinary print, and educational or occupational disruption. Formal LHONAR1-specific patient-reported-outcome statistics are lacking.

## 12. Treatment

### Idebenone

Idebenone, a short-chain benzoquinone/CoQ analog, can accept electrons upstream of complex III and partly bypass complex-I dysfunction while acting in redox pathways. It is the principal disease-directed pharmacotherapy used for LHON. Suggested ontology: **NCIT:C952**; chemical curation should verify the corresponding ChEBI record.

DNAJC30-specific evidence is favorable but nonrandomized. Stenton and colleagues reported shorter recovery time and 77% clinically relevant recovery in at least one eye among treated arLHON patients. However, substantial spontaneous recovery—69% in untreated arLHON—creates confounding by natural history. One Central European patient received idebenone for six months only after recovery had begun, illustrating why isolated case responses cannot prove efficacy. (kieninger2022dnajc30diseasecausinggene pages 3-4, stenton2022dnajc30defecta pages 3-5)

The commonly used European LHON regimen is 900 mg/day orally in divided doses, continued for at least 12 months or until a sustained plateau after recovery; this regimen is extrapolated from general LHON authorization and consensus practice rather than a DNAJC30-specific randomized trial. Gastrointestinal symptoms and nasopharyngitis are among commonly reported adverse effects in broader idebenone experience. Treatment should be supervised by a mitochondrial/neuro-ophthalmology specialist.

### Supportive care

Low-vision rehabilitation, magnification and electronic reading aids, contrast optimization, orientation/mobility training, educational/workplace accommodations, occupational therapy, and psychosocial support are important real-world interventions. Suggested NCIT concepts include supportive care, rehabilitation therapy, occupational therapy, and genetic counseling after terminology validation.

### Experimental treatment

No DNAJC30 replacement, CRISPR, RNA therapy, cell therapy, or targeted small molecule has established clinical efficacy. MT-ND4 allotopic gene-replacement products such as lenadogene nolparvovec target the mitochondrial **m.11778G>A/MT-ND4** genotype and are **not directly applicable** to DNAJC30-LHON. No recruiting DNAJC30-specific interventional trial was identified by the trial search.

Complex-I bypass with yeast **NDI1** has protected retinal ganglion cells and improved mitochondrial function in experimental rotenone and patient-fibroblast systems, but this is a mutation-agnostic preclinical strategy rather than a validated DNAJC30 model or treatment.

## 13. Prevention

There is no vaccine or pharmacologic primary prophylaxis. Prevention is principally genetic and anticipatory:

* confirm the familial variants and offer cascade testing;
* provide autosomal recessive recurrence counseling;
* discuss prenatal diagnosis or preimplantation genetic testing where desired and legally available;
* monitor biallelic asymptomatic relatives with baseline acuity, color testing, fields, and OCT;
* encourage prompt assessment of new central blur or dyschromatopsia;
* avoid smoking, excessive alcohol, and avoidable mitochondrial-toxic exposures, explicitly recognizing that DNAJC30-specific benefit is unproven.

Population newborn screening is not recommended: prevalence is very low, penetrance is incomplete, onset is usually later, and no proven presymptomatic therapy exists.

## 14. Other species and natural disease

No naturally occurring DNAJC30-associated LHON equivalent was identified in companion animals, livestock, or wildlife, and no breed-specific VBO annotation can currently be recommended. The condition is genetic and noninfectious, with no zoonotic or cross-species transmission.

DNAJC30 is evolutionarily conserved, and ortholog studies can illuminate mitochondrial chaperone biology. However, evidence from Williams–Beuren deletion models or general mitochondrial dysfunction should not be labeled as a natural animal model of LHONAR1.

## 15. Model organisms and research systems

The strongest disease-specific experimental evidence comes from **human patient-derived fibroblasts and mitochondrial biochemical assays**, showing loss of DNAJC30 and isolated complex-I deficiency. These models establish molecular causality but do not reproduce the retinal-ganglion-cell selectivity, bilateral temporal course, or visual recovery of human disease. (stenton2022dnajc30defecta pages 1-2, stenton2022dnajc30defecta pages 3-5)

No well-validated DNAJC30 knockout/knock-in mouse, zebrafish, Drosophila, retinal organoid, or iPSC-derived retinal-ganglion-cell model that recapitulates LHONAR1 was established in the retrieved literature. A priority model would combine homozygous p.Tyr51Cys or a null allele with human iPSC-derived retinal ganglion cells and an in-vivo knock-in system, measuring complex-I turnover, oxygen consumption, ATP, ROS, axonal transport, RNFL thickness, and visual function.

Rotenone-induced complex-I retinal injury and AAV-NDI1 rescue models are useful for testing downstream complex-I bypass, but are induced general models, not genotype-faithful DNAJC30 disease models.

## Evidence appraisal and current research gaps

The best-supported claims are the causal relationship with biallelic DNAJC30 variants, European p.Tyr51Cys founder effect, male-biased incomplete penetrance, LHON-like ocular phenotype, complex-I repair defect, and relatively favorable recovery. Evidence derives from several independent human cohorts and functional studies. (OpenTargets Search: Leber-like hereditary optic neuropathy, autosomal recessive 1, kieninger2022dnajc30diseasecausinggene pages 3-4, stenton2022dnajc30defecta pages 1-2)

Important unresolved issues are: population prevalence and carrier frequency outside Europe; precise age- and sex-specific penetrance; environmental triggers; genotype–phenotype relationships for non-founder alleles; disease-specific OCT and patient-reported outcomes; prospective idebenone effectiveness; biomarkers of reversible versus irreversible ganglion-cell injury; and genotype-faithful retinal models. Recent 2023 studies mainly strengthened the Eastern European founder association and demonstrated the practical diagnostic value of routine DNAJC30 sequencing; no transformative DNAJC30-specific therapeutic development was identified in 2023–2024. (major2023casereportmutations pages 1-2, skorczykwerner2023dnajc30genevariants pages 10-11)

### Bottom line

LHONAR1 should be suspected whenever a patient has an mtDNA-negative LHON phenotype, especially a young male of Central/Eastern European ancestry, synchronous bilateral involvement, or a family pattern inconsistent with maternal transmission. The highest-yield implementation is combined mtDNA and nuclear optic-neuropathy testing that includes DNAJC30, followed by segregation/cascade testing, early consideration of idebenone, and visual rehabilitation. Prognosis is often better than classical mtDNA-LHON, but irreversible central visual disability remains possible and the treatment evidence is not yet randomized.

References

1. (OpenTargets Search: Leber-like hereditary optic neuropathy, autosomal recessive 1): Open Targets Query (Leber-like hereditary optic neuropathy, autosomal recessive 1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (kieninger2022dnajc30diseasecausinggene pages 1-2): Sinja Kieninger, Ting Xiao, Nicole Weisschuh, Susanne Kohl, Klaus Rüther, Peter Michael Kroisel, Tobias Brockmann, Steffi Knappe, Ulrich Kellner, Wolf Lagrèze, Pascale Mazzola, Tobias B Haack, Bernd Wissinger, and Felix Tonagel. <i>dnajc30</i> disease-causing gene variants in a large central european cohort of patients with suspected leber’s hereditary optic neuropathy and optic atrophy. Journal of Medical Genetics, 59(10):1027-1034, Jan 2022. URL: https://doi.org/10.1136/jmedgenet-2021-108235, doi:10.1136/jmedgenet-2021-108235. This article has 35 citations and is from a domain leading peer-reviewed journal.

3. (stenton2022dnajc30defecta pages 1-2): Sarah L. Stenton, Marketa Tesarova, Natalia L. Sheremet, Claudia B. Catarino, Valerio Carelli, Elżbieta Ciara, Kathryn Curry, Martin Engvall, Leah R. Fleming, Peter Freisinger, Katarzyna Iwanicka-Pronicka, Elżbieta Jurkiewicz, Thomas Klopstock, Mary K. Koenig, Hana Kolářová, Bohdan Kousal, Tatiana Krylova, Chiara La Morgia, Lenka Nosková, Dorota Piekutowska-Abramczuk, Sam N. Russo, Viktor Stránecký, Iveta Tóthová, Frank Träisk, and Holger Prokisch. <i>dnajc30</i> defect: a frequent cause of recessive leber hereditary optic neuropathy and leigh syndrome. Brain, 145:1624-1631, Feb 2022. URL: https://doi.org/10.1093/brain/awac052, doi:10.1093/brain/awac052. This article has 51 citations and is from a highest quality peer-reviewed journal.

4. (kieninger2022dnajc30diseasecausinggene pages 4-5): Sinja Kieninger, Ting Xiao, Nicole Weisschuh, Susanne Kohl, Klaus Rüther, Peter Michael Kroisel, Tobias Brockmann, Steffi Knappe, Ulrich Kellner, Wolf Lagrèze, Pascale Mazzola, Tobias B Haack, Bernd Wissinger, and Felix Tonagel. <i>dnajc30</i> disease-causing gene variants in a large central european cohort of patients with suspected leber’s hereditary optic neuropathy and optic atrophy. Journal of Medical Genetics, 59(10):1027-1034, Jan 2022. URL: https://doi.org/10.1136/jmedgenet-2021-108235, doi:10.1136/jmedgenet-2021-108235. This article has 35 citations and is from a domain leading peer-reviewed journal.

5. (stenton2022dnajc30defecta pages 3-5): Sarah L. Stenton, Marketa Tesarova, Natalia L. Sheremet, Claudia B. Catarino, Valerio Carelli, Elżbieta Ciara, Kathryn Curry, Martin Engvall, Leah R. Fleming, Peter Freisinger, Katarzyna Iwanicka-Pronicka, Elżbieta Jurkiewicz, Thomas Klopstock, Mary K. Koenig, Hana Kolářová, Bohdan Kousal, Tatiana Krylova, Chiara La Morgia, Lenka Nosková, Dorota Piekutowska-Abramczuk, Sam N. Russo, Viktor Stránecký, Iveta Tóthová, Frank Träisk, and Holger Prokisch. <i>dnajc30</i> defect: a frequent cause of recessive leber hereditary optic neuropathy and leigh syndrome. Brain, 145:1624-1631, Feb 2022. URL: https://doi.org/10.1093/brain/awac052, doi:10.1093/brain/awac052. This article has 51 citations and is from a highest quality peer-reviewed journal.

6. (kieninger2022dnajc30diseasecausinggene pages 1-1): Sinja Kieninger, Ting Xiao, Nicole Weisschuh, Susanne Kohl, Klaus Rüther, Peter Michael Kroisel, Tobias Brockmann, Steffi Knappe, Ulrich Kellner, Wolf Lagrèze, Pascale Mazzola, Tobias B Haack, Bernd Wissinger, and Felix Tonagel. <i>dnajc30</i> disease-causing gene variants in a large central european cohort of patients with suspected leber’s hereditary optic neuropathy and optic atrophy. Journal of Medical Genetics, 59(10):1027-1034, Jan 2022. URL: https://doi.org/10.1136/jmedgenet-2021-108235, doi:10.1136/jmedgenet-2021-108235. This article has 35 citations and is from a domain leading peer-reviewed journal.

7. (major2023casereportmutations pages 1-2): Toby Charles Major, Eszter Sara Arany, Katherine Schon, Magdolna Simo, Veronika Karcagi, Jelle van den Ameele, Patrick Yu Wai Man, Patrick F. Chinnery, Catarina Olimpio, and Rita Horvath. Case report: mutations in dnajc30 causing autosomal recessive leber hereditary optic neuropathy are common amongst eastern european individuals. Frontiers in Neurology, Dec 2023. URL: https://doi.org/10.3389/fneur.2023.1292320, doi:10.3389/fneur.2023.1292320. This article has 2 citations and is from a peer-reviewed journal.

8. (kieninger2022dnajc30diseasecausinggene pages 6-6): Sinja Kieninger, Ting Xiao, Nicole Weisschuh, Susanne Kohl, Klaus Rüther, Peter Michael Kroisel, Tobias Brockmann, Steffi Knappe, Ulrich Kellner, Wolf Lagrèze, Pascale Mazzola, Tobias B Haack, Bernd Wissinger, and Felix Tonagel. <i>dnajc30</i> disease-causing gene variants in a large central european cohort of patients with suspected leber’s hereditary optic neuropathy and optic atrophy. Journal of Medical Genetics, 59(10):1027-1034, Jan 2022. URL: https://doi.org/10.1136/jmedgenet-2021-108235, doi:10.1136/jmedgenet-2021-108235. This article has 35 citations and is from a domain leading peer-reviewed journal.

9. (kieninger2022dnajc30diseasecausinggene pages 5-6): Sinja Kieninger, Ting Xiao, Nicole Weisschuh, Susanne Kohl, Klaus Rüther, Peter Michael Kroisel, Tobias Brockmann, Steffi Knappe, Ulrich Kellner, Wolf Lagrèze, Pascale Mazzola, Tobias B Haack, Bernd Wissinger, and Felix Tonagel. <i>dnajc30</i> disease-causing gene variants in a large central european cohort of patients with suspected leber’s hereditary optic neuropathy and optic atrophy. Journal of Medical Genetics, 59(10):1027-1034, Jan 2022. URL: https://doi.org/10.1136/jmedgenet-2021-108235, doi:10.1136/jmedgenet-2021-108235. This article has 35 citations and is from a domain leading peer-reviewed journal.

10. (skorczykwerner2023dnajc30genevariants pages 10-11): Anna Skorczyk-Werner, Katarzyna Tońska, Aleksandra Maciejczuk, Katarzyna Nowomiejska, Magdalena Korwin, Monika Ołdak, Anna Wawrocka, and Maciej R. Krawczyński. Dnajc30 gene variants are a frequent cause of a rare disease: leber hereditary optic neuropathy in polish patients. Dec 2023. URL: https://doi.org/10.3390/ijms242417496, doi:10.3390/ijms242417496. This article has 8 citations.

11. (kieninger2022dnajc30diseasecausinggene pages 3-4): Sinja Kieninger, Ting Xiao, Nicole Weisschuh, Susanne Kohl, Klaus Rüther, Peter Michael Kroisel, Tobias Brockmann, Steffi Knappe, Ulrich Kellner, Wolf Lagrèze, Pascale Mazzola, Tobias B Haack, Bernd Wissinger, and Felix Tonagel. <i>dnajc30</i> disease-causing gene variants in a large central european cohort of patients with suspected leber’s hereditary optic neuropathy and optic atrophy. Journal of Medical Genetics, 59(10):1027-1034, Jan 2022. URL: https://doi.org/10.1136/jmedgenet-2021-108235, doi:10.1136/jmedgenet-2021-108235. This article has 35 citations and is from a domain leading peer-reviewed journal.

12. (wiggs2021dnajc30biallelicmutations pages 2-3): Janey L. Wiggs. Dnajc30 biallelic mutations extend mitochondrial complex i–deficient phenotypes to include recessive leber’s hereditary optic neuropathy. Journal of Clinical Investigation, Mar 2021. URL: https://doi.org/10.1172/jci147734, doi:10.1172/jci147734. This article has 22 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Leber-like_Hereditary_Optic_Neuropathy_Autosomal_Recessive_1-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.