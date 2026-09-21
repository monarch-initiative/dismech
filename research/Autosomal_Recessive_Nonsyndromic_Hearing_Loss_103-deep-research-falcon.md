---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T11:30:58.059219'
end_time: '2026-08-28T11:42:28.752132'
duration_seconds: 690.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 103
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_103-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 103
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 103** covering all of the
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
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 103
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 103** covering all of the
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


# Research report: Autosomal recessive nonsyndromic hearing loss 103 (DFNB103)

## Executive summary

Autosomal recessive nonsyndromic hearing loss 103 (DFNB103) is an ultra-rare, usually childhood-onset, progressive sensorineural hearing disorder caused by biallelic loss-of-function variants in **CLIC5**. The best-characterized manifestations are bilateral hearing loss and, in some families, progressive vestibular dysfunction or areflexia. A single Turkish patient had possible mild renal involvement, but a consistent renal syndrome has not been established. The strongest population enrichment is in the Sakha Republic (Yakutia), where the founder variant **CLIC5 c.1121G>A, p.(Trp374Ter)** was found in 26 of 238 GJB2-negative patients and produced marked regional clustering. Mechanistically, CLIC5 stabilizes plasma-membrane–actin linkages at the base of cochlear and vestibular hair-cell stereocilia through a protein network containing radixin, taperin, PTPRQ, MYO6, and GRXCR2. Loss of this function causes stereocilia disorganization and fusion, hair-cell degeneration, and progressive auditory/vestibular failure. There is no approved disease-modifying treatment or human DFNB103 trial; management is audiologic and vestibular rehabilitation. Mouse AAV gene replacement reported in 2025 provides strong but still preclinical proof of concept. (pshennikova2019…novelnonsense pages 1-2, seco2015progressivehearingloss pages 1-2, salles2014clic5stabilizesmembrane‐actin pages 1-3, hahn2025aavgenetherapy pages 10-12)

The following table provides a compact curation summary.

| Knowledge-base field | Summary | Ontology / identifier suggestions | Key evidence |
|---|---|---|---|
| Identity / identifiers | **Autosomal recessive nonsyndromic hearing loss 103 (DFNB103)** is a rare Mendelian form of progressive sensorineural hearing loss caused by **biallelic CLIC5 variants**. Disease-level information is derived from **aggregated literature case reports/series and cohort studies**, not EHR data. **OMIM phenotype:** 616042 (reported in secondary sources/snippets; verify directly in OMIM before database ingestion). **MONDO:** not verified here. **Orphanet / ICD-10 / ICD-11 / MeSH:** no disease-specific identifier verified in available evidence. Historical literature may refer to the mapped region as **DFNB102** before phenotype naming was stabilized; use caution in synonym mapping. | MONDO: unverified; HP:0000365 Hearing impairment; HP:0000407 Sensorineural hearing impairment | (pshennikova2019…novelnonsense pages 1-2, seco2015progressivehearingloss pages 1-2) |
| Causal gene and inheritance | **CLIC5** (chloride intracellular channel 5), **OMIM gene 607293**; inheritance is **autosomal recessive** with segregation shown in Turkish and Cameroonian families and homozygosity/founder enrichment in Yakutia. Functional disease mechanism is most consistent with **loss of function**. | HGNC: CLIC5; HP:0000007 Autosomal recessive inheritance; SO:0002054 loss_of_function_variant | (pshennikova2019…novelnonsense pages 1-2, seco2015progressivehearingloss pages 1-2, adadey2022cellbasedanalysisof pages 8-10) |
| Established human variants | Established disease-associated human variants reported in available evidence: **c.96T>A (p.Cys32\*)**, homozygous nonsense, Turkish family; **c.1121G>A (p.Trp374\*)**, homozygous nonsense, Yakutian founder-enriched juvenile DFNB103; **c.224T>C (p.Leu75Pro)** plus **c.63+1G>A**, compound heterozygous in a Cameroonian multiplex family. Variant classes represented: **nonsense, splice-donor, missense**. Germline origin. | Sequence Ontology: nonsense_variant, splice_donor_variant, missense_variant; ACMG class: pathogenic/likely pathogenic (case-level interpretation should be confirmed in ClinVar/ACMG source) | (pshennikova2019…novelnonsense pages 1-2, seco2015progressivehearingloss pages 1-2, ott2023anovelrole pages 2-3, adadey2022cellbasedanalysisof pages 8-10) |
| Core phenotypes | Core phenotype is **bilateral, predominantly symmetric, progressive sensorineural hearing loss** of variable severity. Additional features reported in at least one family: **vestibular areflexia / vestibular dysfunction** with balance problems; **possible mild renal dysfunction** in one Turkish patient. No consistent extra-auditory syndrome has yet been established across families. | HP:0008619 Progressive hearing impairment; HP:0000407 Sensorineural hearing impairment; HP:0002315 Areflexia of the vestibular system; HP:0002172 Postural instability; HP:0012594 Abnormality of urine albumin excretion | (seco2015progressivehearingloss pages 1-2, seco2015progressivehearingloss pages 2-5, pshennikova2019…novelnonsense pages 1-2) |
| Onset / course | Turkish family: **onset in early childhood**, progressing from **mild** to **severe/profound before the second decade**. Yakutian series: among **26/238 GJB2-negative** patients homozygous for p.Trp374\*, onset varied **0–8 years** in the discovery family and was **postlingual in most patients (19/26)** with mean onset **9.7 ± 0.6 years**; audiology in **13/26** showed progressive SNHL ranging from mild to profound. | HP:0011463 Childhood onset; HP:0003593 Infantile onset / congenital onset if applicable in some cases; HP:0003676 Progressive; HP:0012716 Bilateral sensorineural hearing impairment | (seco2015progressivehearingloss pages 1-2, pshennikova2019…novelnonsense pages 1-2) |
| Mechanism / pathophysiology | CLIC5A is highly expressed at the **base of cochlear and vestibular hair-cell stereocilia** and functions in a complex with **RDX (radixin), TPRN (taperin), PTPRQ, MYO6**, and functionally with **GRXCR2** to stabilize **membrane–actin filament linkages**. Loss of CLIC5 causes **mislocalization/reduction of basal stereocilia proteins**, reduced **ERM/radixin phosphorylation**, stereocilia fusion, and eventual hair-cell dysfunction/degeneration, producing progressive auditory and vestibular deficits. Cell assays show mutant CLIC5A can form **perinuclear aggregates** and fail to support **filopodia-like protrusions**, supporting cytoskeletal dysfunction. | GO:0032420 stereocilium organization; GO:0007015 actin filament organization; GO:0005929 cilium / GO:0036064 ciliary basal body-plasma membrane docking (ciliary work extrapolative); CL:0000589 auditory hair cell; CL:0009062 vestibular hair cell; UBERON:0001858 organ of Corti; UBERON:0001717 utricle of membranous labyrinth | (salles2014clic5stabilizesmembrane‐actin pages 1-3, adadey2022cellbasedanalysisof pages 8-10, ott2023anovelrole pages 2-3) |
| Anatomy / cell types | Primary anatomy affected: **inner ear**, especially **cochlear and vestibular sensory epithelia**. Relevant structures/cells include **hair bundles/stereocilia**, **inner hair cells**, **outer hair cells**, and **vestibular hair cells**. Subcellular localization is strongest at the **basal region of stereocilia**. CLIC5 is also expressed in other tissues including kidney-related structures, but clinically consistent non-auditory disease remains unproven. | UBERON:0000044 cochlea; UBERON:0000947 inner ear; UBERON:0001987 vestibular system; GO:0032420 stereocilium; CL:0000589 auditory hair cell; CL:0000602 inner hair cell; CL:0000601 outer hair cell | (seco2015progressivehearingloss pages 1-2, salles2014clic5stabilizesmembrane‐actin pages 1-3, hahn2025aavgenetherapy pages 17-18) |
| Epidemiology / population data | Ultra-rare globally; no robust global prevalence/incidence estimate identified in available evidence. Strongest quantitative population data come from **Yakutia**: **26/238 (10.9%)** of GJB2-negative patients carried homozygous **c.1121G>A (p.Trp374\*)**; estimated average DFNB103 prevalence **0.27 ± 0.053 per 10,000** in Yakutia, with a reported maximum in **Eveno-Bytantaysky district of 31.39 ± 10.46 per 10,000**. Geographic enrichment suggests a **founder effect**. Seco et al. found no additional pathogenic CLIC5 variants among **213** mainly Dutch/Spanish arNSHI patients screened, supporting rarity in those populations. | Population/founder annotation; HP:0032113 Founder effect (term label to verify in ontology implementation) | (pshennikova2019…novelnonsense pages 1-2, seco2015progressivehearingloss pages 1-2, seco2015progressivehearingloss pages 5-6) |
| Diagnostics | Recommended diagnostic approach from available disease-specific evidence: phenotype-confirming **audiometry**, evaluation for **vestibular dysfunction** (e.g., rotatory/electronystagmography in reported family), exclusion of conductive/anatomic causes including **temporal-bone CT**, and **molecular testing**. For genetics, **WES** identified the Yakutian founder variant; targeted testing for known regional founder alleles may be efficient in enriched populations; otherwise include **CLIC5 on comprehensive hereditary hearing-loss panels**. No disease-specific biomarker or imaging signature beyond standard audiovestibular assessment was identified. | LOINC/functional audiology terms not verified here; HP:0000365, HP:0001751 Vestibular dysfunction; NCIT: Whole Exome Sequencing; NCIT: Genetic Testing | (seco2015progressivehearingloss pages 1-2, pshennikova2019…novelnonsense pages 1-2) |
| Current care / real-world management | No **approved DFNB103-specific pharmacotherapy** or gene therapy is currently established in humans in available evidence. Real-world care is therefore **supportive and rehabilitative**, following standard monogenic hearing-loss practice: early **audiologic follow-up**, **hearing aids** when useful, **cochlear implantation** if hearing becomes severe/profound and candidacy criteria are met, plus **vestibular rehabilitation/safety counseling** for balance dysfunction. Because progression can occur in childhood, serial monitoring is important. | NCIT: Hearing Aid Device; NCIT: Cochlear Implantation; NCIT: Rehabilitation; HP management terms as above | (seco2015progressivehearingloss pages 1-2, seco2015progressivehearingloss pages 5-6) |
| Experimental therapy / latest research | **No human DFNB103 interventional trial** was identified in the available ClinicalTrials.gov search. Recent/preclinical advances: **2023** zebrafish study showed isoform-specific Clic5 roles in **ciliogenesis**, **ERM phosphorylation**, and **Wnt-signaling dysregulation**; **2022** cell assays functionally supported pathogenicity of African variants; **2025** mouse study showed **AAV2/9-PHP.B Clic5** delivered by **P0 utricle injection** restored localization and preserved hearing/balance in Clic5-deficient mice. Reported quantitative details include **1.2 µL ssAAV.Clic5 at 1.69 × 10^14 gc/mL** and self-complementary AAV efficacy at lower titer, but this remains **preclinical**. | NCIT: Gene Therapy; CHEBI/viral vector terms not mapped here; evidence type = mouse / zebrafish / cell | (hahn2025aavgenetherapy pages 1-2, hahn2025aavgenetherapy pages 10-12, ott2023anovelrole pages 2-3, adadey2022cellbasedanalysisof pages 8-10) |
| Key evidence limitations | Evidence base is **small**: a few families/case series, one regional prevalence study, and substantial mechanistic reliance on **mouse, zebrafish, and cell** models. Several identifiers (MONDO/Orphanet/ICD/MeSH) were **not directly verified** in the available sources. Some clinical features such as **renal involvement** and degree of **vestibular penetrance** remain uncertain because they were not consistent across all reported families. Human natural history, penetrance, carrier frequency, and treatment-outcome data remain limited. | Evidence tags: human case report/series, cohort, mouse model, zebrafish model, cell assay | (seco2015progressivehearingloss pages 1-2, pshennikova2019…novelnonsense pages 1-2, ott2023anovelrole pages 2-3, adadey2022cellbasedanalysisof pages 8-10) |


*Table: This table summarizes the key disease knowledge-base facts for CLIC5-related DFNB103, including identity, variants, phenotype, mechanism, Yakutian epidemiology, diagnostics, and therapy status. It is designed as a concise, citation-backed artifact for structured curation.*

## 1. Disease information

### Definition and identifiers

DFNB103 is a Mendelian autosomal-recessive form of nonsyndromic sensorineural hearing loss attributable to biallelic **CLIC5** variants. The original report described the locus as **DFNB102** during mapping; subsequent disease nomenclature uses **DFNB103**, so these labels should not automatically be treated as separate diseases when curating older literature. (seco2015progressivehearingloss pages 1-2, seco2015progressivehearingloss pages 2-5)

* **Preferred name:** Autosomal recessive nonsyndromic hearing loss 103.
* **Synonyms:** DFNB103; deafness, autosomal recessive 103; CLIC5-related hearing loss; CLIC5-related autosomal-recessive deafness; progressive autosomal-recessive deafness 103.
* **OMIM phenotype:** **616042**, reported for DFNB103 in the retrieved literature.
* **Causal-gene OMIM:** **CLIC5, 607293**; cytogenetic location **6p21.1**. (pshennikova2019…novelnonsense pages 1-2)
* **MONDO:** no disease-specific MONDO identifier was verified from the retrieved authoritative text; it should therefore be left unresolved rather than inferred.
* **Orphanet:** no dedicated identifier verified.
* **ICD-10/ICD-11 and MeSH:** no genotype-specific code verified. In clinical systems the condition is generally represented under hereditary or sensorineural hearing-loss categories rather than a DFNB103-specific billing code.

The evidence is aggregated disease-level information from pedigrees, case series, cohort screening, and experimental models—not individual-level EHR data.

## 2. Etiology

### Causal factors and genetic risk

The primary cause is inheritance of two damaging germline **CLIC5** alleles. Established reports include:

1. **c.96T>A, p.(Cys32Ter)**, homozygous nonsense variant in two affected siblings from a consanguineous Turkish family. It segregated with disease and was absent from 222 Turkish control alleles, the Exome Variant Server, and a 1,302-exome local database. The premature stop is predicted to cause severe loss of function, although nonsense-mediated decay was not demonstrated in lymphoblastoid cells. (seco2015progressivehearingloss pages 1-2, seco2015progressivehearingloss pages 2-5)
2. **c.1121G>A, p.(Trp374Ter)**, homozygous nonsense variant in Yakutia. This truncates CLIC5 at residue 374 and is strongly enriched regionally, consistent with a founder effect. (pshennikova2019…novelnonsense pages 1-2)
3. **c.224T>C, p.(Leu75Pro)** in trans with **c.63+1G>A**, a missense plus canonical splice-donor combination in three affected members of a Cameroonian multiplex family. Cell experiments support functional disruption by p.Leu75Pro. (ott2023anovelrole pages 2-3, adadey2022cellbasedanalysisof pages 8-10)

All are germline variants. No somatic disease mechanism, repeat expansion, aneuploidy, or recurrent pathogenic chromosomal rearrangement is established.

### Environmental, protective, and gene–environment factors

No environmental exposure, infectious agent, lifestyle factor, sex-specific factor, or gene–environment interaction is known to cause DFNB103. Noise, ototoxic drugs, meningitis, and congenital infection remain important alternative or additive causes of hearing loss, but they are not demonstrated components of this Mendelian disorder. Avoidance of noise and ototoxic exposure is sensible hearing preservation, not primary prevention of the genotype.

No validated protective allele or modifier gene has been reported. **RDX, TPRN, PTPRQ, MYO6,** and **GRXCR2** are mechanistic partners and plausible modifiers, but human modifier effects have not been proven. (adadey2022cellbasedanalysisof pages 8-10, salles2014clic5stabilizesmembrane‐actin pages 1-3)

## 3. Phenotypes

### Auditory phenotype

The core manifestation is bilateral, predominantly symmetric, progressive sensorineural hearing loss. In the Turkish siblings, hearing loss began in early childhood, initially mild and most evident at middle/high frequencies, and advanced to severe or profound loss before the second decade. The discovery article states directly: **“The hearing loss … had an onset in early childhood and progressed from mild to severe or even profound before the second decade.”** (seco2015progressivehearingloss pages 1-2)

In Yakutia, the discovery family contained five affected people with onset from birth to eight years. Across 26 p.Trp374Ter-homozygous patients, 19/26 had postlingual onset, averaging **9.7 ± 0.6 years**. Audiometry in 13/26 showed predominantly symmetric, progressive sensorineural loss ranging from mild to profound. These figures should not be interpreted as universal frequencies because the cohort was regionally and genetically ascertained. (pshennikova2019…novelnonsense pages 1-2)

Suggested HPO terms include **Sensorineural hearing impairment (HP:0000407)**, **Progressive hearing impairment (HP:0008619)**, **Bilateral sensorineural hearing impairment**, **Childhood onset (HP:0011463)**, and **Postlingual hearing loss**.

### Vestibular and other findings

Both Turkish siblings developed balance difficulty, including trouble walking in darkness and cycling. Rotatory testing demonstrated vestibular areflexia at ages 16 and 11 years. Early motor milestones were normal, indicating that vestibular deterioration may emerge after initially normal development. Suggested terms are **Vestibular dysfunction**, **Bilateral vestibular areflexia**, and **Postural instability**. (seco2015progressivehearingloss pages 2-5)

One sibling had repeated elevated urine albumin/creatinine ratios of **9.2 and 3.8 mg/mmol** (reference <2.5), mildly elevated blood pressure, but normal estimated glomerular filtration rate (**114 mL/min/1.73 m²**). This was considered possible early nephropathy, not proven CLIC5-related renal disease. The other sibling had normal renal findings, and no consistent renal phenotype is established in later families. (seco2015progressivehearingloss pages 2-5)

No consistent dysmorphism, thyroid disease, intellectual disability, retinal disease, or other syndromic feature has been documented. Quality-of-life effects have not been quantified with EQ-5D, SF-36, or PROMIS in DFNB103. Expected impacts include impaired speech access, education, communication, localization of sound, and mobility/safety when vestibular dysfunction is present.

## 4. Genetic and molecular information

**CLIC5** encodes chloride intracellular channel protein 5, with CLIC5A and CLIC5B isoforms. Despite its name and reported membrane-channel properties, the disease-relevant evidence strongly supports a structural/signaling role for CLIC5A in actin-rich stereocilia. CLIC5A occurs in soluble and membrane-associated forms, interacts with actin and ERM-family proteins, and is concentrated at the stereocilia base. (adadey2022cellbasedanalysisof pages 8-10, salles2014clic5stabilizesmembrane‐actin pages 1-3)

The disease mechanism is predominantly **loss of function**. Nonsense and essential splice variants are expected to abolish or markedly reduce functional protein. In transfected cells, p.Leu75Pro CLIC5A accumulated as perinuclear aggregates instead of showing the diffuse cytoplasmic distribution of wild type; mutant-expressing cells also lacked the thin filopodia-like projections induced by wild-type CLIC5A. This provides in-vitro functional support but does not alone quantify clinical pathogenicity. (adadey2022cellbasedanalysisof pages 8-10)

Population allele frequencies should be retrieved variant-by-variant from the current gnomAD release before production ingestion. The discovery p.Cys32Ter variant was absent from the historical control resources tested, while p.Trp374Ter is regionally enriched in Yakutia. ClinVar classifications and HGNC identifiers were not directly available in the retrieved evidence and should not be inferred from case reports alone.

No reproducible epigenetic abnormality, disease-specific methylation signature, somatic mosaicism, germline mosaicism, anticipation, or pathogenic large chromosomal abnormality is known.

## 5. Environmental information

Environmental toxins, radiation, pollution, occupation, smoking, alcohol, diet, and infectious organisms are not established etiologic factors. They may independently worsen hearing and should be assessed during differential diagnosis. There is no vaccine, antimicrobial prophylaxis, dietary intervention, or environmental remediation specific to DFNB103.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream trigger:** biallelic damaging CLIC5 variants reduce or eliminate functional CLIC5A.
2. **Molecular complex failure:** normal CLIC5 associates with **RDX, TPRN, PTPRQ, MYO6**, and functionally with **GRXCR2** at the stereociliary taper. It promotes/stabilizes active phosphorylated ERM proteins and links the plasma membrane to the actin core. (salles2014clic5stabilizesmembrane‐actin pages 1-3, waddell2016clic5maintainslifelong pages 1-5)
3. **Cellular structural defect:** loss of CLIC5 causes early mislocalization of RDX/PTPRQ/TPRN and weakens membrane–actin coupling. In jitterbug mice, stereocilia fusion is detectable by postnatal day 10, followed by dysmorphic bundles and progressive hair-cell degeneration. (salles2014clic5stabilizesmembrane‐actin pages 1-3)
4. **Physiological defect:** disordered hair bundles cannot maintain normal mechanosensory architecture and sound-evoked transduction. Equivalent injury in vestibular hair cells disrupts balance sensing.
5. **Clinical manifestation:** progressive sensorineural hearing loss, with vestibular areflexia in at least some genotypes/families. (seco2015progressivehearingloss pages 1-2, salles2014clic5stabilizesmembrane‐actin pages 1-3)

Suggested GO biological-process annotations are **stereocilium organization**, **actin filament organization**, **plasma membrane–actin cytoskeleton organization**, **sensory perception of sound**, **mechanosensory behavior**, and **protein phosphorylation**. Relevant cellular components are **stereocilium (GO:0032420)**, **actin cytoskeleton**, **plasma membrane**, and **hair bundle**. Relevant Cell Ontology concepts are auditory inner hair cell, auditory outer hair cell, and vestibular hair cell.

### Recent mechanistic developments

A 2023 zebrafish study found isoform-specific roles: Clic5a contributed to the glomerular filtration barrier, whereas Clic5b localized to pronephric cilia. Clic5b deficiency impaired ciliogenesis and produced otolith deposition abnormalities, laterality defects, hydrocephalus, and pronephric cysts, with altered cilia-dependent Wnt components and reduced ERM activation. This broadens CLIC5 biology but should not be equated directly with human DFNB103, whose reproducible phenotype remains auditory/vestibular. (ott2023anovelrole pages 2-3)

No disease-specific human single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or integrated multi-omic signature is established. Available molecular profiling consists mainly of tissue expression, localization, interaction, and perturbation studies.

## 7. Anatomical structures affected

The primary organ is the **inner ear**, involving:

* cochlea and organ of Corti;
* inner and outer auditory hair cells;
* vestibular sensory epithelia and vestibular hair cells;
* stereociliary hair bundles, particularly the basal taper region where CLIC5 is concentrated. (salles2014clic5stabilizesmembrane‐actin pages 1-3)

Suggested anatomy annotations include **inner ear (UBERON:0001846; verify release)**, **cochlea (UBERON:0001848; verify release)**, organ of Corti, utricle, saccule, and semicircular-duct sensory epithelium. Suggested cellular-component annotation is **stereocilium (GO:0032420)**. Disease is usually bilateral; consistent anatomical asymmetry or structural temporal-bone malformation has not been reported.

Kidney involvement remains uncertain. CLIC5 has experimentally demonstrated renal and ciliary functions, but this does not establish the kidney as a consistently affected organ in human DFNB103. (ott2023anovelrole pages 2-3, seco2015progressivehearingloss pages 2-5)

## 8. Temporal development

DFNB103 is chronic and lifelong. Onset ranges from congenital/infantile in a minority of reported Yakutian cases to childhood or postlingual juvenile onset in most characterized patients. Progression is usually gradual rather than acute, episodic, fluctuating, or relapsing. Severity may evolve from mild loss to severe/profound deafness during childhood or adolescence. (pshennikova2019…novelnonsense pages 1-2, seco2015progressivehearingloss pages 1-2)

No formal staging system exists. A practical clinical sequence is: normal or mildly impaired early hearing → progressive threshold elevation → severe/profound hearing loss, with later vestibular difficulty in susceptible individuals. There is no spontaneous remission. Childhood auditory development is a critical intervention period because delayed audibility can impair speech and language even when onset is postlingual.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two carrier parents, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial variant. Both sexes are expected to be affected equally.

Penetrance appears high for biallelic truncating alleles in reported families, but the number of families is too small to estimate penetrance precisely. Expressivity is variable in age at onset, severity, and vestibular involvement. Anticipation is not expected. Consanguinity aided discovery in the Turkish family and can increase the probability that a rare allele is inherited homozygously. (seco2015progressivehearingloss pages 1-2)

Global prevalence and incidence are unknown. In Yakutia, homozygous p.Trp374Ter occurred in **26/238 (10.9%)** GJB2-negative hearing-loss patients. Estimated prevalence was **0.27 ± 0.053 per 10,000** across Yakutia and **31.39 ± 10.46 per 10,000** in Eveno-Bytantaysky district, a striking regional founder concentration. Conversely, screening of 213 predominantly Dutch/Spanish autosomal-recessive nonsyndromic hearing-loss patients found no additional pathogenic CLIC5 variants, indicating that CLIC5 is not a common cause in those populations. (seco2015progressivehearingloss pages 5-6, pshennikova2019…novelnonsense pages 1-2, seco2015progressivehearingloss pages 1-2)

Carrier frequency is not established globally and will differ substantially by ancestry and founder population.

## 10. Diagnostics

### Clinical evaluation

Evaluation should include otoscopy, air- and bone-conduction pure-tone audiometry, age-appropriate speech testing, tympanometry, otoacoustic emissions, and auditory brainstem responses when behavioral testing is unreliable. Serial audiograms are essential because progression is a defining feature. Vestibular history and testing—video head-impulse testing, calorics, vestibular-evoked myogenic potentials, or rotatory-chair testing—are appropriate when balance symptoms occur. The discovery study used electronystagmography/rotatory testing and temporal-bone CT to exclude alternative anatomical causes. (seco2015progressivehearingloss pages 1-2, seco2015progressivehearingloss pages 2-5)

Renal blood pressure, urinalysis, and urine albumin/creatinine assessment may be considered at baseline, particularly for truncating variants, but evidence is insufficient to mandate a DFNB103 renal surveillance guideline.

### Genetic testing strategy

1. Use a comprehensive hereditary-hearing-loss panel that includes **CLIC5**, with sequencing and copy-number analysis.
2. In Yakutian/Even populations, targeted p.Trp374Ter testing is efficient, but a negative result does not exclude another hearing-loss gene.
3. If panel testing is negative, trio or family-based exome/genome sequencing is appropriate; WES identified the Yakutian variant. (pshennikova2019…novelnonsense pages 1-2)
4. Confirm candidate variants by orthogonal sequencing, phase compound heterozygous alleles, and test segregation.
5. Interpret variants under ACMG/AMP criteria using population frequency, predicted consequence, segregation, phenotype, and functional evidence.

CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line DFNB103 assays unless the broader phenotype suggests another diagnosis. RNA analysis can clarify splice variants. There is no validated blood biomarker, metabolomic assay, biopsy criterion, or liquid biopsy.

Differential diagnosis includes other progressive recessive nonsyndromic hearing-loss genes—especially **GJB2, STRC, OTOF, MYO15A, MYO6, TPRN, RDX, PTPRQ,** and **GRXCR2**—as well as Usher syndrome, enlarged vestibular aqueduct/Pendred spectrum, congenital CMV, meningitis, ototoxicity, and noise-induced loss.

## 11. Outcome and prognosis

DFNB103 is not known to shorten life expectancy or cause disease-specific mortality. Morbidity arises from progressive auditory disability and, where present, vestibular impairment. Untreated severe hearing loss can affect language access, education, employment, social participation, and safety. Vestibular areflexia may impair mobility in darkness or on uneven surfaces. Disease-specific survival statistics, standardized quality-of-life scores, and validated prognostic calculators do not exist.

The strongest prognostic indicator is serial measured hearing trajectory. Genotype–phenotype relationships remain preliminary: p.Trp374Ter commonly produced juvenile/postlingual progressive loss in Yakutia, while p.Cys32Ter caused early-childhood progression with vestibular areflexia in the Turkish siblings. These observations are not sufficient for deterministic individual prediction. (pshennikova2019…novelnonsense pages 1-2, seco2015progressivehearingloss pages 1-2)

## 12. Treatment

### Current care

There is no approved CLIC5-targeted drug, RNA therapy, genome editor, or gene therapy. Standard treatment is individualized:

* prompt hearing-aid fitting for aidable mild-to-severe loss;
* remote-microphone and educational accommodations;
* speech-language, auditory-verbal, or sign-language support according to patient goals;
* cochlear-implant evaluation for severe/profound loss with insufficient aided speech access;
* vestibular physiotherapy, fall-prevention measures, and mobility counseling;
* continued audiologic surveillance because thresholds can deteriorate rapidly during childhood.

Suggested NCIT intervention concepts are **Hearing Aid**, **Cochlear Implantation**, **Audiologic Rehabilitation**, **Speech Therapy**, **Vestibular Rehabilitation**, and **Genetic Counseling**. No DFNB103-specific pharmacogenomic relationship is known.

### Experimental therapy

A 2025 mouse study delivered wild-type **Clic5** by utricular injection at postnatal day 0 using single-stranded or self-complementary AAV2/9-PHP.B. A reported ssAAV regimen used **1.2 μL at 1.69×10^14 genome copies/mL**. Treatment restored CLIC5 at the hair-bundle base, limited stereocilia degeneration, and preserved auditory and vestibular function through 12 weeks. Self-complementary AAV achieved comparable recovery at a lower titer—reported as **1.52×10^13 gc/mL**—which may reduce dose-related toxicity. (hahn2025aavgenetherapy pages 10-12, hahn2025aavgenetherapy pages 17-18, hahn2025aavgenetherapy pages 1-2)

This is compelling model-organism proof of concept, not evidence of human efficacy or safety. Neonatal mouse delivery, inner-ear scaling, surgical route, immune responses, durability, genotype-specific windows, and treatment after established degeneration remain translational barriers. No relevant human DFNB103 interventional trial or NCT identifier was found.

## 13. Prevention

The inherited genotype cannot currently be prevented by lifestyle modification.

* **Primary/reproductive prevention:** genetic counseling, carrier testing of relatives, partner testing, prenatal diagnosis, and preimplantation genetic testing for a known familial variant.
* **Secondary prevention:** newborn hearing screening alone may miss later-onset DFNB103; molecular diagnosis and scheduled audiometry permit detection before substantial language-access loss.
* **Tertiary prevention:** early amplification/implant assessment, communication support, vestibular rehabilitation, fall prevention, and avoidance of unnecessary ototoxic exposure can reduce disability.

Vaccination is not disease-specific, although routine immunization against causes of acquired meningitis helps prevent competing acquired hearing loss. Cascade testing is especially relevant in founder populations.

## 14. Other species and natural disease

No naturally occurring veterinary DFNB103 syndrome with established breed prevalence was identified. CLIC5 orthologues are conserved across vertebrates. The principal naturally arising comparative model is the **jitterbug mouse**, carrying a spontaneous recessive 97-bp intragenic **Clic5** deletion that causes exon-5 skipping, frameshift, premature termination, absent CLIC5 protein, impaired hearing, vestibular dysfunction, dysmorphic stereocilia, and progressive hair-cell degeneration. (salles2014clic5stabilizesmembrane‐actin pages 1-3)

Relevant taxonomy identifiers are **Mus musculus, NCBI Taxonomy 10090**; **Danio rerio, 7955**; and **Drosophila melanogaster, 7227**. These models have no zoonotic or cross-species-transmission implications.

## 15. Model organisms

### Mouse

The homozygous **Clic5 jitterbug** mouse closely recapitulates human auditory and vestibular disease. CLIC5 is normally present in cochlear and vestibular stereocilia; mutants show progressive stereocilia fusion from approximately postnatal day 10, mislocalization of RDX/PTPRQ/TPRN, hair-cell degeneration, hearing impairment, and balance abnormalities. Its advantages are mammalian inner-ear anatomy and a progressive therapeutic window; limitations include neonatal cochlear maturation, compressed timescale, and uncertain correspondence between mouse and human treatment timing. (salles2014clic5stabilizesmembrane‐actin pages 1-3)

The model has been used for localization, biochemical interaction, longitudinal pathology, modifier-network studies, and AAV gene replacement. The rescue study’s abstract-level conclusion was that treatment produced **“prevention of morphological degeneration and preserving auditory and vestibular function.”** (hahn2025aavgenetherapy pages 10-12, hahn2025aavgenetherapy pages 1-2)

### Zebrafish

Isoform-specific clic5 knockdown models revealed glomerular and ciliary functions. Clic5b deficiency caused defective ciliogenesis, abnormal otolith deposition, laterality defects, hydrocephalus, and pronephric cysts, with Wnt and ERM abnormalities. Zebrafish are useful for developmental imaging and rapid functional studies, but their otic anatomy and duplicated isoform biology limit direct extrapolation to progressive human cochlear disease. (ott2023anovelrole pages 2-3)

### Cellular and biochemical systems

Transfected-cell assays distinguish wild-type CLIC5A distribution and membrane protrusion formation from p.Leu75Pro aggregation and cytoskeletal defects. Co-immunoprecipitation/localization approaches demonstrate interactions with ERM proteins, taperin, PTPRQ, MYO6, and GRXCR2. These systems define molecular effects but cannot reproduce cochlear mechanics, tonotopy, or long-term hair-cell degeneration. (adadey2022cellbasedanalysisof pages 8-10, salles2014clic5stabilizesmembrane‐actin pages 1-3)

## Evidence assessment and knowledge gaps

The human evidence base remains small: one deeply phenotyped Turkish sibship, a Yakutian founder cohort, a Cameroonian multiplex family, and limited additional reports. Consequently, penetrance, vestibular frequency, renal significance, variant-specific prognosis, global prevalence, carrier frequency, and treatment outcomes are uncertain. The proposed membrane–actin mechanism is strong because human genetics converges with mouse pathology, biochemical interactions, and cell assays. In contrast, renal/ciliary and Wnt findings are biologically credible but not yet established as routine human manifestations. (ott2023anovelrole pages 2-3, adadey2022cellbasedanalysisof pages 8-10, pshennikova2019…novelnonsense pages 1-2, seco2015progressivehearingloss pages 1-2)

## Key publications and URLs

* Seco CZ et al. **Progressive hearing loss and vestibular dysfunction caused by a homozygous nonsense mutation in CLIC5.** *European Journal of Human Genetics.* Published online **30 April 2014**; print 2015. DOI/URL: https://doi.org/10.1038/ejhg.2014.83. (seco2015progressivehearingloss pages 1-2)
* Salles FT et al. **CLIC5 stabilizes membrane-actin filament linkages at the base of hair cell stereocilia…** *Cytoskeleton.* **January 2014.** DOI/URL: https://doi.org/10.1002/cm.21159. (salles2014clic5stabilizesmembrane‐actin pages 1-3)
* Pshennikova VG et al. **A novel nonsense mutation c.1121G>A (p.Trp374*)… in Yakutia.** *Medical Genetics.* **2019;18(10):36–48.** DOI/URL: https://doi.org/10.25557/2073-7998.2019.10.36-48. (pshennikova2019…novelnonsense pages 1-2)
* Adadey SM et al. **Cell-based analysis of CLIC5A and SLC12A2 variants…** *Frontiers in Genetics.* **August 2022.** DOI/URL: https://doi.org/10.3389/fgene.2022.924904. (adadey2022cellbasedanalysisof pages 8-10)
* Ott E et al. **A novel role for the chloride intracellular channel protein Clic5 in ciliary function.** *Scientific Reports.* **October 2023.** DOI/URL: https://doi.org/10.1038/s41598-023-44235-y. (ott2023anovelrole pages 2-3)
* Hahn R et al. **AAV gene therapy rescues hearing and balance in a model of CLIC5 deafness.** *EMBO Molecular Medicine.* **August 2025.** DOI/URL: https://doi.org/10.1038/s44321-025-00275-7. This post-2024 paper is included because it is the most important current disease-specific therapeutic development. (hahn2025aavgenetherapy pages 10-12, hahn2025aavgenetherapy pages 1-2)

PMIDs were not consistently present in the retrieved full texts and are therefore not supplied where they could not be verified reliably.

References

1. (pshennikova2019…novelnonsense pages 1-2): VG Pshennikova, GP Romanov, and TM Nikolaeva. … novel nonsense mutation c. 1121g> a (p. trp374*) in the clic5 gene is the main cause of the juvenile autosomal recessive form of deafness (dfnb103) in the arctic …. Unknown journal, 2019.

2. (seco2015progressivehearingloss pages 1-2): Celia Zazo Seco, Anne MM Oonk, María Domínguez-Ruiz, Jos MT Draaisma, Marta Gandía, Jaap Oostrik, Kornelia Neveling, Henricus PM Kunst, Lies H Hoefsloot, Ignacio del Castillo, Ronald JE Pennings, Hannie Kremer, Ronald JC Admiraal, and Margit Schraders. Progressive hearing loss and vestibular dysfunction caused by a homozygous nonsense mutation in clic5. European Journal of Human Genetics, 23:189-194, Apr 2015. URL: https://doi.org/10.1038/ejhg.2014.83, doi:10.1038/ejhg.2014.83. This article has 75 citations and is from a domain leading peer-reviewed journal.

3. (salles2014clic5stabilizesmembrane‐actin pages 1-3): Felipe T. Salles, Leonardo R. Andrade, Soichi Tanda, M'hamed Grati, Kathleen L. Plona, Leona H. Gagnon, Kenneth R. Johnson, Bechara Kachar, and Mark A. Berryman. Clic5 stabilizes membrane‐actin filament linkages at the base of hair cell stereocilia in a molecular complex with radixin, taperin, and myosin vi. Cytoskeleton, 71:61-78, Jan 2014. URL: https://doi.org/10.1002/cm.21159, doi:10.1002/cm.21159. This article has 82 citations and is from a peer-reviewed journal.

4. (hahn2025aavgenetherapy pages 10-12): Roni Hahn, Shahar Taiber, Olga Shubina-Oleinik, Gwenaëlle S G Géléoc, Jeffrey R Holt, and Karen B Avraham. Aav gene therapy rescues hearing and balance in a model of clic5 deafness. EMBO Molecular Medicine, Aug 2025. URL: https://doi.org/10.1038/s44321-025-00275-7, doi:10.1038/s44321-025-00275-7. This article has 6 citations and is from a highest quality peer-reviewed journal.

5. (adadey2022cellbasedanalysisof pages 8-10): Samuel Mawuli Adadey, Edmond Wonkam-Tingang, Leonardo Alves de Souza Rios, Elvis Twumasi Aboagye, Kevin Esoh, Noluthando Manyisa, Carmen De Kock, Gordon A. Awandare, Shaheen Mowla, and Ambroise Wonkam. Cell-based analysis of clic5a and slc12a2 variants associated with hearing impairment in two african families. Frontiers in Genetics, Aug 2022. URL: https://doi.org/10.3389/fgene.2022.924904, doi:10.3389/fgene.2022.924904. This article has 2 citations and is from a peer-reviewed journal.

6. (ott2023anovelrole pages 2-3): Elisabeth Ott, Sylvia Hoff, Lara Indorf, Franck Anicet Ditengou, Julius Müller, Gina Renschler, Soeren S. Lienkamp, Albrecht Kramer-Zucker, Carsten Bergmann, and Daniel Epting. A novel role for the chloride intracellular channel protein clic5 in ciliary function. Scientific Reports, Oct 2023. URL: https://doi.org/10.1038/s41598-023-44235-y, doi:10.1038/s41598-023-44235-y. This article has 9 citations and is from a peer-reviewed journal.

7. (seco2015progressivehearingloss pages 2-5): Celia Zazo Seco, Anne MM Oonk, María Domínguez-Ruiz, Jos MT Draaisma, Marta Gandía, Jaap Oostrik, Kornelia Neveling, Henricus PM Kunst, Lies H Hoefsloot, Ignacio del Castillo, Ronald JE Pennings, Hannie Kremer, Ronald JC Admiraal, and Margit Schraders. Progressive hearing loss and vestibular dysfunction caused by a homozygous nonsense mutation in clic5. European Journal of Human Genetics, 23:189-194, Apr 2015. URL: https://doi.org/10.1038/ejhg.2014.83, doi:10.1038/ejhg.2014.83. This article has 75 citations and is from a domain leading peer-reviewed journal.

8. (hahn2025aavgenetherapy pages 17-18): Roni Hahn, Shahar Taiber, Olga Shubina-Oleinik, Gwenaëlle S G Géléoc, Jeffrey R Holt, and Karen B Avraham. Aav gene therapy rescues hearing and balance in a model of clic5 deafness. EMBO Molecular Medicine, Aug 2025. URL: https://doi.org/10.1038/s44321-025-00275-7, doi:10.1038/s44321-025-00275-7. This article has 6 citations and is from a highest quality peer-reviewed journal.

9. (seco2015progressivehearingloss pages 5-6): Celia Zazo Seco, Anne MM Oonk, María Domínguez-Ruiz, Jos MT Draaisma, Marta Gandía, Jaap Oostrik, Kornelia Neveling, Henricus PM Kunst, Lies H Hoefsloot, Ignacio del Castillo, Ronald JE Pennings, Hannie Kremer, Ronald JC Admiraal, and Margit Schraders. Progressive hearing loss and vestibular dysfunction caused by a homozygous nonsense mutation in clic5. European Journal of Human Genetics, 23:189-194, Apr 2015. URL: https://doi.org/10.1038/ejhg.2014.83, doi:10.1038/ejhg.2014.83. This article has 75 citations and is from a domain leading peer-reviewed journal.

10. (hahn2025aavgenetherapy pages 1-2): Roni Hahn, Shahar Taiber, Olga Shubina-Oleinik, Gwenaëlle S G Géléoc, Jeffrey R Holt, and Karen B Avraham. Aav gene therapy rescues hearing and balance in a model of clic5 deafness. EMBO Molecular Medicine, Aug 2025. URL: https://doi.org/10.1038/s44321-025-00275-7, doi:10.1038/s44321-025-00275-7. This article has 6 citations and is from a highest quality peer-reviewed journal.

11. (waddell2016clic5maintainslifelong pages 1-5): BB Waddell. Clic5 maintains lifelong structural integrity of sensory stereocilia by promoting radixin phosphorylation in hair cells of the inner ear. Unknown journal, 2016.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_103-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.