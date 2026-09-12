---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-18T21:13:47.883259'
end_time: '2026-08-18T21:27:33.610110'
duration_seconds: 825.73
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Infantile-Onset Pompe Disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 6
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Infantile-Onset_Pompe_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infantile-Onset Pompe Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Infantile-Onset Pompe Disease** covering all of the
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
- **Disease Name:** Infantile-Onset Pompe Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Infantile-Onset Pompe Disease** covering all of the
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


# Infantile-Onset Pompe Disease: Disease-Characteristics Research Report

## Executive summary

Infantile-onset Pompe disease (IOPD) is the severe, early-onset end of the autosomal-recessive **GAA** deficiency spectrum. Near-absent lysosomal acid α-glucosidase activity causes glycogen accumulation, lysosomal and autophagic dysfunction, and rapidly progressive cardiomyopathy, generalized hypotonia, bulbar weakness, and respiratory failure. Without disease-specific treatment, classic IOPD is usually fatal during the first year of life. Enzyme-replacement therapy (ERT), newborn screening, and CRIM-guided immune-tolerance induction have transformed survival, although long-term survivors retain substantial skeletal-muscle, bulbar, auditory, respiratory, and possibly central-nervous-system morbidity. The most authoritative recent clinical synthesis is the November 2024 MetabERN pathway (DOI: [10.1186/s13023-024-03373-w](https://doi.org/10.1186/s13023-024-03373-w)). (parenti2024theeuropeanreference pages 2-4, moschetti2024mutationspectrumof pages 1-2, prater2012theemergingphenotype pages 1-3)

The following table provides a compact knowledge-base summary; the narrative below expands and qualifies each field.

| Domain | Summary | Key ontology mappings | Quantitative details | Evidence source(s) |
|---|---|---|---|---|
| Definition / IDs | Infantile-onset Pompe disease (IOPD; classic/atypical infantile acid maltase deficiency) is the severe early-onset form of glycogen storage disease type II, a lysosomal storage disorder caused by acid alpha-glucosidase deficiency with glycogen accumulation, especially in cardiac and skeletal muscle. Disease-level information here is from aggregated literature/guidelines, not individual EHRs. | MONDO: glycogen storage disease II = **MONDO:0009290**; Orphanet: **365**; MeSH/ICD not confidently extracted here; UBERON: heart **UBERON:0000948**, skeletal muscle tissue **UBERON:0001134**, diaphragm **UBERON:0001103**, lysosome (GO CC) **GO:0005764** | MetabERN notes atypical infantile presentation may occur after 6 months but within first 2 years; untreated classic IOPD is typically fatal within the first year. | Parenti et al., 2024; Moschetti et al., 2024 (parenti2024theeuropeanreference pages 2-4, moschetti2024mutationspectrumof pages 1-2) |
| Cause and inheritance | Primary cause is **biallelic pathogenic variants in GAA** causing markedly reduced/absent lysosomal acid alpha-glucosidase activity. Inheritance is **autosomal recessive**. CRIM status is a major treatment-response modifier; CRIM-negative patients lack endogenous GAA protein and are at higher risk of anti-ERT immune responses. Environmental causes are not established. | Gene: **GAA**; GO BP: glycogen catabolic process **GO:0005980**, autophagy **GO:0006914**; CL: skeletal muscle cell **CL:0000187**, cardiomyocyte **CL:0000746** | MetabERN cites **648** documented disease-associated variants (as of Dec 2020); a 2024 review reports **>911** disease-associated GAA variants; about **one-third** of infantile Pompe patients are CRIM-negative. | Parenti et al., 2024; Moschetti et al., 2024; Open Targets GAA-disease association (parenti2024theeuropeanreference pages 2-4, moschetti2024mutationspectrumof pages 1-2, OpenTargets Search: Pompe disease-GAA) |
| Hallmark phenotypes | Core manifestations: hypertrophic cardiomyopathy, generalized hypotonia/floppy infant phenotype, respiratory insufficiency, feeding difficulty, motor delay/regression, macroglossia, hepatomegaly; long-term survivors may show persistent gross motor weakness, dysphagia/aspiration risk, motor speech deficits, hearing loss, osteopenia, and GERD. | HPO: cardiomyopathy **HP:0001638**, hypertrophic cardiomyopathy **HP:0001639**, hypotonia **HP:0001252**, respiratory insufficiency **HP:0002093**, hepatomegaly **HP:0002240**, macroglossia **HP:0000158**, dysphagia **HP:0002015**, hearing impairment **HP:0000365**, delayed gross motor development **HP:0002194** | In a long-term survivor series, **11** IOPD survivors had median age **8.0 y** (range **5.4–12.0**); **7/11** were independently ambulatory. | Prater et al., 2012; Parenti et al., 2024; Moschetti et al., 2024 (prater2012theemergingphenotype pages 1-3, parenti2024theeuropeanreference pages 2-4, moschetti2024mutationspectrumof pages 2-3) |
| Mechanism / pathophysiology | Upstream defect: GAA loss causes lysosomal glycogen accumulation. Downstream cascade: lysosomal enlargement, rupture/leakage of glycogen into cytoplasm, impaired autophagic flux, secondary accumulation of autophagic material, mitochondrial dysfunction and oxidative stress, culminating in cardiac, skeletal, smooth-muscle, and neural dysfunction. CNS involvement is increasingly recognized but incompletely corrected by standard ERT. | GO BP: lysosomal transport **GO:0007041** (broadly relevant), autophagy **GO:0006914**, response to oxidative stress **GO:0006979**; GO CC: lysosome **GO:0005764**; CL: motor neuron **CL:0000100**, endothelial cell **CL:0000115** | Gene-therapy review notes cross-correction may require only about **1–10%** of normal enzyme activity for effective substrate clearance in LSD paradigms. | Uribe-Carretero et al., 2024; Moschetti et al., 2024; Leon-Astudillo et al., 2023 (uribecarretero2024lysosomaldysfunctionconnecting pages 14-16, moschetti2024mutationspectrumof pages 2-3, leonastudillo2023currentavenuesof pages 11-12) |
| Diagnosis | Typical workflow: first-line enzyme testing on dried blood spot (DBS), then confirmatory enzyme assay in leukocytes/fibroblasts and **GAA** sequencing; CRIM status assessment is important before/at ERT initiation. Supportive tests commonly include CK and disease biomarkers such as urinary/plasma glucose tetrasaccharide (Glc4/Hex4), plus ECG/echocardiography and respiratory evaluation. | HPO/lab-related: elevated creatine kinase not mapped here with confidence; UBERON: blood **UBERON:0000178**, skin fibroblast culture not ontologized here | In one older long-term cohort, diagnostic enzyme activity in fibroblasts/muscle was **<1%** of control mean; an Italian diagnostic cohort screened **2934** subjects and identified **39** symptomatic PD patients with two causative mutations plus **22** GVUS cases. | Moschetti et al., 2024; Prater et al., 2012 (moschetti2024mutationspectrumof pages 2-3, prater2012theemergingphenotype pages 1-3) |
| Epidemiology | Pompe disease frequency varies by population and ascertainment method; newborn screening (NBS) generally yields higher observed birth prevalence than historical clinical diagnosis. Certain founder/pseudodeficiency backgrounds complicate interpretation in some populations. | MONDO:0009290; no additional population ontology asserted | MetabERN: overall incidence about **1:40,000–1:146,000**; in NBS countries **1:8,684–1:23,596**; Taiwan about **1:17,000**; French Guiana about **1:2,000**. Population-genetic study: global **GAA** carrier frequency **1.3%**; common variant c.-32-13T>G AF **0.0033** globally (mostly relevant to LOPD/carrier screening, not specific to IOPD). | Parenti et al., 2024; Choi et al., 2024 (parenti2024theeuropeanreference pages 2-4, OpenTargets Search: Pompe disease-GAA) |
| Current treatment | Standard of care is **enzyme replacement therapy (ERT)** with alglucosidase alfa initiated as early as possible; prophylactic immune tolerance induction (ITI) is used particularly for CRIM-negative IOPD. Multidisciplinary supportive care includes cardiology, pulmonology/ventilation, nutrition/swallow management, PT/OT/speech therapy, and monitoring of antibody titers and biomarkers. Avalglucosidase alfa is an emerging/next-generation option under pediatric study rather than established universal standard for IOPD. | NCIT terms not asserted confidently; GO/CL/UBERON as above for affected systems | Long-term survivor cohort: biweekly ERT at cumulative doses **20–40 mg/kg**; all survivors had cardiac improvement and low/undetectable antibody titers. Avalglucosidase pediatric trial records: Mini-COMET **NCT03019406**, planned enrollment **22**; Baby-COMET **NCT04910776**, enrollment **17**. | Prater et al., 2012; Unnisa et al., 2022; ClinicalTrials.gov records (prater2012theemergingphenotype pages 1-3, unnisa2022genetherapydevelopments pages 2-3, OpenTargets Search: Pompe disease-GAA) |
| Prognosis | Natural history is rapidly progressive and often lethal in infancy without therapy. ERT has markedly improved survival and ventilator-free survival, but residual disease remains common in long-term survivors, especially musculoskeletal, bulbar, auditory, and possibly CNS complications. Prognosis is modified by CRIM status, age at treatment start, antibody response, and likely residual enzyme activity/genotype. | HPO: progressive muscle weakness **HP:0003323** (broad), respiratory failure **HP:0002878** | Pre-ERT prognosis commonly death by age **<2 y**; Moschetti review states classic untreated fatality often within **1 year**. In the survivor cohort, **11** long-term survivors were alive at school age with persistent morbidity. | Moschetti et al., 2024; Prater et al., 2012; Kishnani et al., 2007 referenced in retrieved literature (moschetti2024mutationspectrumof pages 1-2, prater2012theemergingphenotype pages 1-3) |
| Screening / prevention | Secondary prevention is most important: **newborn screening** enables presymptomatic or very early treatment and CRIM-guided planning. Primary prevention of disease occurrence is not available; genetic counseling, carrier testing, cascade testing, prenatal diagnosis, and preimplantation testing are relevant for at-risk families. | No extra ontology confidently asserted | Northeast Italy screened about **250,000** neonates: **126** positives (**0.051%**), **51** confirmed affected, **40%** PPV, overall incidence **1:4,874** across 4 LSDs; **3 IOPD** infants were immediately treated. China NBGS cohort screened **22,687** newborns with **6.0%** carriers, **0.13%** initial positives, and **15** presymptomatic LSD diagnoses overall. | Gragnaniello et al., 2023; Wang et al., 2025 (gragnaniello2023lightandshadows pages 1-2, wang2025effectofnewborn pages 1-2) |
| Emerging therapies / models | Experimental directions include next-generation ERT (avalglucosidase alfa), AAV- and lentiviral-based gene therapy, liver- and muscle-directed delivery, CNS-targeted/intrathecal approaches, substrate reduction (e.g., GYS1 inhibition), and even **in utero ERT** proof-of-concept. Key models include **Gaa−/− mouse**, naturally occurring Japanese quail disease, and large-animal models. | Model systems not ontology-mapped here; GO: glycogen biosynthetic process **GO:0005978** relevant to substrate reduction concept | In utero ERT case: single treated fetus with normal cardiac and age-appropriate motor function at **13 months**. Muscle-directed gene therapy review cites AAV8 liver-directed study in **4** LOPD subjects and ongoing pediatric avalglucosidase trial **NCT03019406**. Animal-model review summarized **42** GSD animal models total, including **26** genetically modified mouse models and **15** naturally occurring models; Pompe-relevant naturally occurring models include quail and large animals. | Cohen et al., 2022; Leon-Astudillo et al., 2023; Almodóvar-Payá et al., 2020; Ullman et al., 2024 (preclinical Pompe mouse substrate reduction) (cohen2022inuteroenzymereplacement pages 12-14, leonastudillo2023currentavenuesof pages 11-12, unnisa2022genetherapydevelopments pages 2-3, OpenTargets Search: Pompe disease-GAA) |


*Table: This table condenses key disease-knowledge-base fields for infantile-onset Pompe disease, including identifiers, genetics, phenotypes, mechanisms, diagnostics, epidemiology, treatment, and emerging translational research. It is designed as a compact reference with ontology suggestions, quantitative details, and cited evidence sources.*

## 1. Disease information

### Definition and classification

Pompe disease—glycogen storage disease type II—is a lysosomal glycogen-storage disorder caused by deficiency of acid α-glucosidase. **Classic IOPD** generally presents in the first weeks or months with hypertrophic cardiomyopathy and profound generalized hypotonia. “Non-classic” or atypical infantile Pompe disease presents in infancy, sometimes after six months but within approximately two years, and may have less prominent cardiomyopathy. This report treats IOPD as a clinical subtype of the broader Pompe disease entity rather than a genetically separate disorder. (parenti2024theeuropeanreference pages 2-4, moschetti2024mutationspectrumof pages 2-3, moschetti2024mutationspectrumof pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0009290, glycogen storage disease II. The available source maps this broad entity rather than a distinct IOPD-only MONDO record.
- **OMIM:** #232300, glycogen storage disease II/Pompe disease; causal gene **GAA**, OMIM *606800.
- **Orphanet:** ORPHA:365, glycogen storage disease due to acid maltase deficiency.
- **ICD-10-CM:** E74.02, Pompe disease.
- **ICD-11:** generally classified under glycogen-storage diseases/inborn errors of carbohydrate metabolism; local coding-browser verification is advised before database ingestion.
- **MeSH:** Glycogen Storage Disease Type II.
- **Synonyms:** Pompe disease, acid maltase deficiency, acid α-glucosidase deficiency, glycogenosis type II, GSD II, lysosomal glycogen-storage disease, infantile acid maltase deficiency, classic infantile Pompe disease.

Open Targets identifies **GAA** as the dominant disease-associated target for MONDO:0009290 and ORPHA:365, supported by human genetic literature including PMIDs 11071489, 16917947, 20080426, 18429042, 16782080, and 14695532. Other genes returned by broad association searches are not established causes of Pompe disease and should not be entered as causal genes. (OpenTargets Search: Pompe disease-GAA)

### Evidence granularity

The information summarized here is principally **aggregated disease-level evidence** from guidelines, cohorts, trials, and reviews. It is not an extraction from individual electronic health records. Case reports, such as prenatal ERT, are explicitly labeled as single-patient evidence.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The sole established primary cause is **germline biallelic pathogenic or likely pathogenic variation in GAA**, located on chromosome 17q25.3. GAA encodes lysosomal acid α-glucosidase, which hydrolyzes α-1,4- and α-1,6-linked glycogen to glucose. Severe alleles producing minimal or no residual enzyme generally cause IOPD; genotype–phenotype correlation remains imperfect because residual activity, protein production, immune response, and treatment timing modify expression. Variant classes include missense, nonsense, frameshift, canonical and noncanonical splice variants, small insertions/deletions, and exon-level or larger rearrangements. A 2024 review reported more than 911 disease-associated variants, whereas MetabERN cited 648 documented variants as of December 2020, illustrating continued database growth rather than a true discrepancy. (parenti2024theeuropeanreference pages 2-4, moschetti2024mutationspectrumof pages 1-2)

### Genetic risk and modifiers

- **Autosomal-recessive genotype:** two disease-causing alleles are necessary; heterozygous carriers are generally asymptomatic.
- **Residual GAA activity:** near-absence favors classic IOPD; greater residual activity tends toward later onset.
- **CRIM status:** approximately one-third of infantile patients are reported as CRIM-negative. Absence of endogenous immunologically detectable GAA increases the risk of high, sustained anti-rhGAA antibodies and poor ERT response. Some CRIM-positive patients also develop clinically important antibodies. (parenti2024theeuropeanreference pages 2-4, moschetti2024mutationspectrumof pages 2-3)
- **Treatment-related modifiers:** younger age and lower disease burden at ERT initiation, adequate dosing, and prevention of deleterious antibodies improve outcomes. These are modifiers of prognosis rather than risk of inheriting disease.
- **Founder/population effects:** marked geographic variation, including very high frequency in French Guiana, indicates founder effects. Specific pathogenic and pseudodeficiency alleles also vary by ancestry.

No modifier gene has been validated sufficiently for routine clinical prediction. The weak Open Targets association with **TTN** should not be interpreted as evidence that TTN modifies or causes IOPD. (OpenTargets Search: Pompe disease-GAA)

### Environmental, infectious, lifestyle, and protective factors

There is no credible evidence that toxins, infection, smoking, diet, alcohol, radiation, or occupation cause IOPD. Sex is not a causal risk factor, and both sexes should be affected approximately equally. Family history and consanguinity increase the probability of inheriting two familial alleles but do not alter the molecular mechanism.

No established genetic “protective allele” prevents disease in a person carrying two severe pathogenic alleles. Relative protection is conferred by residual-function genotypes and—clinically—presymptomatic diagnosis, immediate ERT, immune-tolerance induction when indicated, vaccination/infection prevention, respiratory support, safe nutrition, and rehabilitation. There is no established disease-specific gene–environment interaction. Intercurrent respiratory infection, fasting, malnutrition, or prolonged immobility may unmask or worsen limited cardiopulmonary reserve but are downstream stressors, not causes.

## 3. Phenotypes

### Core phenotype map

| Phenotype | Type, onset, course, and frequency | Functional/QoL impact | Suggested HPO |
|---|---|---|---|
| Hypertrophic cardiomyopathy/cardiomegaly | Clinical sign; usually early infancy; severe and progressive untreated; characteristic of classic IOPD | Heart failure, arrhythmia risk, feeding intolerance, reduced endurance | HP:0001639; HP:0001640 |
| Generalized hypotonia | Sign; neonatal/early infantile; severe, progressive | “Floppy infant,” impaired antigravity movement and self-care | HP:0001252; generalized hypotonia HP:0001290 |
| Progressive muscle weakness | Sign; axial, proximal, respiratory and bulbar muscles; nearly universal clinically | Delayed milestones, loss of mobility, dependence for transfers | HP:0003323; HP:0003701 |
| Respiratory muscle weakness/insufficiency | Sign; infancy; progressive; respiratory infection often precipitates decompensation | Sleep-disordered breathing, ventilatory dependence, mortality | HP:0002093; HP:0002878; HP:0002791 |
| Feeding difficulty, dysphagia, weak suck | Symptom/sign; early infancy; common | Aspiration, prolonged meals, tube feeding, poor growth | HP:0011968; HP:0002015; HP:0008872 |
| Macroglossia | Physical manifestation; infancy; characteristic but variable | Airway and feeding burden | HP:0000158 |
| Hepatomegaly | Sign, usually from glycogen and/or cardiac congestion; common | Abdominal distension; usually not primary hepatic failure | HP:0002240 |
| Motor delay/regression | Developmental manifestation; infancy; severe untreated | Loss/failure of sitting, standing, walking | HP:0001270; HP:0002194 |
| Elevated CK/AST/ALT/LDH | Laboratory abnormalities; variable | Supports muscle injury but is not diagnostic | HP:0003236 for elevated CK |
| ECG abnormalities | Short PR interval, high voltages, ventricular hypertrophy patterns | Arrhythmia surveillance and anesthesia implications | HP:0005165; more specific ECG terms as observed |
| Hearing impairment | Particularly evident among ERT-era survivors; sensorineural, conductive, or mixed | Communication and educational effects; hearing aids may be needed | HP:0000365; HP:0000407 |
| Dysarthria/motor-speech disorder | Long-term survivor phenotype | Reduced intelligibility and social participation | HP:0001260 |
| Osteopenia/low bone density | Long-term complication influenced by weakness and reduced loading | Fracture and mobility risk | HP:0000938 |
| GERD | Common supportive-care problem | Pain, aspiration and feeding burden | HP:0002020 |

The 2024 variant review describes severe progressive hypotonia, hypertrophic cardiomyopathy, respiratory insufficiency, and delayed or regressing motor development. The authors’ abstract-level framing is that IOPD includes a severe “floppy baby” phenotype. (moschetti2024mutationspectrumof pages 2-3)

In a human clinical series of 11 ERT-treated long-term survivors, median age was 8.0 years (range 5.4–12.0), seven were independently ambulatory, and all showed sustained cardiac improvement. Nevertheless, motor weakness, speech impairment, hearing loss, dysphagia/aspiration risk, osteopenia, and GERD remained. Thus ERT changes—not eliminates—the phenotype. (prater2012theemergingphenotype pages 1-3)

Disease-specific pediatric quality-of-life estimates remain less standardized than motor, respiratory, and survival endpoints. The practical burden includes repeated lifelong infusions, ventilatory or feeding support, impaired mobility and communication, frequent specialist visits, caregiver time, and uncertainty about long-term neurologic outcomes.

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** GAA; HGNC:4065; Ensembl ENSG00000171298.
- **Protein:** lysosomal acid α-glucosidase/acid maltase; synthesized as a precursor, mannose-6-phosphate–targeted to lysosomes, and proteolytically matured.
- **Origin:** constitutional/germline. Somatic mutation is not a recognized cause.
- **Functional effect:** overwhelmingly loss of function—reduced synthesis, misfolding, defective trafficking or processing, instability, or reduced catalytic activity. Gain-of-function and dominant-negative mechanisms are not established.

### Variant interpretation and testing cautions

Pathogenicity should be assigned using ACMG/AMP criteria integrating allele frequency, segregation, phenotype, enzyme activity, RNA/protein consequences, functional studies, and curated databases. Pseudodeficiency alleles can lower in-vitro activity against assay substrates without clinical Pompe disease, particularly complicating newborn screening. A VUS plus low DBS activity is not sufficient by itself for diagnosis.

The 2024 Italian study screened 2,934 symptomatic subjects, finding 39 with low enzyme activity and two causative GAA variants and 22 with variants of uncertain significance. This demonstrates the need to couple biochemistry with complete genetic interpretation. (moschetti2024mutationspectrumof pages 2-3)

Population allele frequencies are variant-specific. Severe IOPD alleles are individually rare. In a 2024 gnomAD-based analysis across recessive neuromuscular diseases, **GAA had the highest estimated carrier frequency, 1.3%**, and c.-32-13T>G had global allele frequency 0.0033; that splice variant is primarily associated with late-onset disease and should not be used as an IOPD-specific frequency estimate.

### CRIM and epigenetics

CRIM is a protein-expression phenotype, not an independent gene. It may be predicted from well-characterized variants or measured by Western blot/protein methods. CRIM-negative status strongly informs immunomodulation. No reproducible disease-defining DNA-methylation, histone, or chromatin signature is currently used clinically. There is likewise no characteristic chromosomal aneuploidy or translocation; exon-level GAA deletions/duplications are sequence-level structural variants and should be sought when sequencing finds fewer than two explanatory alleles.

## 5. Environmental information

IOPD is not infectious, toxic, occupational, or lifestyle-mediated. No pathogen is causal or transmissible, and there is no zoonotic risk. Respiratory infections can cause acute deterioration because respiratory muscle reserve and airway clearance are poor. Sedentary behavior is generally a consequence of weakness; carefully prescribed activity may preserve function, whereas exhaustion or eccentric overload should be avoided. Adequate calories and protein, aspiration prevention, vaccination, and prompt infection treatment are supportive—not curative—interventions.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic defect:** biallelic GAA loss-of-function.
2. **Biochemical defect:** deficient lysosomal hydrolysis of glycogen to glucose.
3. **Primary storage:** glycogen accumulates in lysosomes of cardiomyocytes, skeletal and smooth muscle cells, vascular cells, and neural populations.
4. **Organelle injury:** lysosomes enlarge; membrane integrity and trafficking deteriorate. Glycogen and cellular debris may escape into cytoplasm.
5. **Autophagic pathology:** impaired autophagosome–lysosome processing produces autophagic buildup that disrupts sarcomeres and can impede uptake/trafficking of infused enzyme.
6. **Secondary injury:** mitochondrial dysfunction, altered calcium/energy homeostasis, oxidative stress, inflammatory signaling, apoptosis and failed regeneration amplify damage.
7. **Tissue manifestations:** cardiomyocyte enlargement causes hypertrophic cardiomyopathy; myofiber destruction causes hypotonia and weakness; diaphragmatic and motor-neuron involvement causes respiratory failure; bulbar and hypoglossal-system involvement contributes to dysphagia and speech/airway dysfunction.

The 2024 MetabERN synthesis explicitly identifies glycogen/autophagic accumulation, mitochondrial dysfunction, and oxidative stress. The 2024 mutation review describes progression from small glycogen-filled lysosomes to enlargement and rupture with cytoplasmic glycogen and muscle damage. (parenti2024theeuropeanreference pages 2-4, moschetti2024mutationspectrumof pages 2-3)

### Relevant ontology suggestions

- **GO biological process:** glycogen catabolic process GO:0005980; autophagy GO:0006914; lysosomal transport GO:0007041; response to oxidative stress GO:0006979; muscle contraction GO:0006936.
- **GO cellular component:** lysosome GO:0005764; autophagosome GO:0005776; mitochondrion GO:0005739; sarcomere GO:0030017.
- **Cell Ontology:** skeletal muscle cell CL:0000187; cardiomyocyte CL:0000746; smooth muscle cell CL:0000192; motor neuron CL:0000100; endothelial cell CL:0000115; macrophage CL:0000235.

### Immunity

Immune involvement is mainly **iatrogenic immunogenicity** to recombinant GAA rather than autoimmunity. CRIM-negative patients recognize rhGAA as foreign and are particularly susceptible to high sustained antibodies, reduced enzyme exposure, and poor clinical response. Prophylactic B-cell/T-cell–directed immune-tolerance induction is therefore a central part of precision care. Approximately one-third of infantile patients may be CRIM-negative. (parenti2024theeuropeanreference pages 2-4, moschetti2024mutationspectrumof pages 2-3)

### Molecular profiling and advanced technologies

Human IOPD-specific single-cell, spatial, proteomic, lipidomic, and metabolomic datasets remain limited. A 2024 single-nucleus/spatial-transcriptomic study was in **late-onset** Pompe muscle, not IOPD; it found increased slow/regenerative fibers and macrophages, early reduction of glycolytic genes, increased lipid/amino-acid metabolism, increased autophagy genes, reduced ribosomal/mitochondrial programs, defective oxidative phosphorylation, and inflammation/apoptosis in vacuolated fibers. These pathways are biologically relevant but should not be entered as directly proven IOPD signatures without validation.

Preclinical multi-omics provides stronger mechanistic than diagnostic evidence. In Pompe mice, selective GYS1 inhibition corrected biochemical, metabolomic, and transcriptomic abnormalities as glycogen was lowered. No omics assay is currently a routine diagnostic standard for IOPD.

## 7. Anatomical structures affected

### Organ and system level

- **Primary:** heart, skeletal muscle, diaphragm and other respiratory muscles, bulbar/oropharyngeal musculature.
- **Additional:** smooth muscle, peripheral and central motor systems, vasculature, liver, hearing apparatus, bone secondarily through immobility/nutrition.
- **Systems:** cardiovascular, neuromuscular, respiratory, gastrointestinal/nutritional, auditory, skeletal, and increasingly recognized CNS involvement.

### Tissue, cell, and subcellular localization

Cardiomyocytes and skeletal myofibers are the major clinically damaged cells; motor neurons, smooth-muscle cells, endothelial cells and pericytes can also store glycogen. The key subcellular compartment is the **lysosome**, with downstream autophagosomal, mitochondrial and sarcomeric disruption. The 2024 review specifically identifies smooth and skeletal muscle, endothelial cells, motor neurons, and heart as involved. (moschetti2024mutationspectrumof pages 2-3)

Suggested UBERON terms include heart UBERON:0000948, skeletal muscle tissue UBERON:0001134, diaphragm UBERON:0001103, tongue UBERON:0001723, liver UBERON:0002107, spinal cord UBERON:0002240, and brainstem UBERON:0002298. Manifestations are generally bilateral/systemic rather than lateralized.

## 8. Temporal development

Classic IOPD is congenital in molecular origin and likely begins prenatally, although obvious clinical signs usually emerge over the first weeks or months. Onset is chronic-progressive rather than episodic. Untreated stages can be conceptualized as: early hypotonia/feeding difficulty and cardiac hypertrophy; progressive motor failure and respiratory infections; then ventilator dependence, heart/respiratory failure, and death. There is no spontaneous remission.

The critical therapeutic window is **before substantial irreversible muscle, motor-neuron, and cardiac injury**. Newborn screening and family-based prenatal diagnosis shift treatment toward this window. The prenatal ERT case supports prenatal substrate accumulation: the investigators opened their abstract with, “organ damage starts in utero.” (cohen2022inuteroenzymereplacement pages 12-14)

ERT induces rapid cardiac improvement more reliably than complete skeletal-muscle recovery. Disease remains lifelong and progressive residual pathology may emerge even when cardiomyopathy resolves.

## 9. Inheritance and population

### Inheritance counseling

Inheritance is autosomal recessive. For two confirmed carrier parents, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of an unaffected non-carrier. Penetrance for two severe IOPD-causing alleles is expected to be high, but age and severity vary. There is no genetic anticipation. Germline mosaicism is theoretically possible but is not a major established contributor; parental testing is still important when variants appear de novo. Consanguinity raises the chance that both parents carry the same rare allele.

### Epidemiology

MetabERN reports historical overall incidence estimates of approximately 1:40,000–1:146,000, compared with approximately 1:8,684–1:23,596 in newborn-screened populations. Reported birth prevalence is around 1:17,000 in Taiwan and as high as 1:2,000 in French Guiana. These figures usually encompass all Pompe phenotypes and should not be mislabeled as IOPD-only incidence. (parenti2024theeuropeanreference pages 2-4)

The 2023 Northeast Italy program screened about 250,000 newborns for four lysosomal disorders. There were 126 screen positives (0.051%), 51 confirmed affected, and a 40% positive predictive value across all four disorders; three infants with IOPD were identified and immediately treated. The combined four-disorder incidence was 1:4,874, not Pompe-specific incidence. (gragnaniello2023lightandshadows pages 1-2)

There is no consistent sex bias. Geographic and ethnic differences reflect allele frequencies, founder effects, pseudodeficiency alleles, screening design, and access to diagnosis.

## 10. Diagnostics

### Recommended diagnostic sequence

1. **Urgent biochemical screening:** GAA activity in dried blood spot, preferably with an inhibitor/assay system that minimizes interference from maltase-glucoamylase.
2. **Confirmation:** repeat enzyme assay in leukocytes, lymphocytes, cultured fibroblasts, or another validated tissue.
3. **Molecular confirmation:** full GAA sequencing with deletion/duplication analysis; familial variant testing where known.
4. **CRIM determination/prediction:** from established genotype or protein testing; do not delay lifesaving ERT while awaiting prolonged work-up.
5. **Baseline staging:** ECG, echocardiography, cardiology review; oxygenation, blood gas where indicated, respiratory-muscle and sleep assessment; swallow/feeding evaluation; hearing assessment; motor/developmental evaluation.

The 2024 Italian review describes sequential DBS/fibroblast/muscle enzyme testing followed by complete GAA sequencing for low or borderline activity. (moschetti2024mutationspectrumof pages 2-3)

### Biomarkers and clinical tests

- **Enzyme:** deficient acid α-glucosidase activity is the principal biochemical marker.
- **Muscle injury:** CK, AST, ALT and LDH are often elevated but nonspecific.
- **Storage:** urinary or plasma glucose tetrasaccharide, Glc4/Hex4, supports diagnosis and longitudinal response; values can be affected by age and other glycogen disorders.
- **Cardiac:** ECG may show short PR and high voltages; echocardiography quantifies hypertrophy and function.
- **Respiratory:** pulse oximetry alone may miss hypoventilation; capnography/blood gases, sleep study, cough strength and age-appropriate pulmonary testing are useful.
- **Electrophysiology:** EMG may show an irritable myopathy but is not required in a biochemically/genetically clear infant.
- **Biopsy:** vacuolated, PAS-positive glycogen-rich myofibers and lysosomal glycogen by electron microscopy; usually unnecessary when enzyme and molecular results are definitive.

### Genomic modalities

Single-gene sequencing plus copy-number analysis is usually sufficient. A neuromuscular/cardiomyopathy panel, WES, or WGS is useful when the presentation is atypical or initial testing is negative; WGS may detect deep-intronic and structural variants. RNA sequencing can resolve suspected splice variants but is adjunctive. CMA, karyotype, FISH, mitochondrial DNA testing, and repeat-expansion testing are not routine unless another diagnosis is suspected.

### Differential diagnosis

Key alternatives include spinal muscular atrophy, congenital muscular dystrophies/myopathies, Danon disease, PRKAG2 cardiomyopathy, mitochondrial disease, fatty-acid oxidation disorders, other glycogenoses, congenital disorders of glycosylation, sepsis, hypothyroidism, and structural/congenital cardiomyopathy. Cardiomyopathy plus marked hypotonia, macroglossia, elevated muscle enzymes, and very low GAA strongly favors IOPD.

### Screening

Newborn screening measures GAA activity in DBS, often followed by second-tier biomarkers and rapid molecular testing. False positives arise from sample quality, pseudodeficiency, heterozygosity, and VUS; detection of late-onset genotypes creates counseling and follow-up challenges. The Italian program’s authors concluded that screening was feasible and effective but emphasized false positives and uncertain/late-onset findings. (gragnaniello2023lightandshadows pages 1-2)

## 11. Outcome and prognosis

### Untreated course

Classic untreated IOPD is rapidly fatal, generally from cardiorespiratory failure during the first year; older natural-history series commonly place death or invasive ventilation by one to two years. The 2024 review characterizes untreated outcome as invariably fatal within one year. (moschetti2024mutationspectrumof pages 1-2)

### Treated course

ERT substantially improves overall and ventilator-free survival, reverses cardiac hypertrophy, and permits motor milestone acquisition in many infants, especially when started presymptomatically. However, there is no reliable single five- or ten-year survival estimate applicable across genotype, CRIM status, start age, dose, and immune-management era.

In the 11-patient survivor cohort, all had cardiac improvement and seven walked independently, but residual weakness, speech and swallowing problems, hearing loss, osteopenia, and GERD were frequent. This is strong evidence that cardiac response does not equal multisystem cure. (prater2012theemergingphenotype pages 1-3)

### Prognostic factors and biomarkers

Favorable factors are diagnosis through newborn/family screening, ERT before irreversible injury, CRIM positivity or successful immune tolerance, low anti-drug antibody titers, lower baseline cardiac/motor burden, and sustained biochemical response. Adverse factors include CRIM negativity without prophylactic immunomodulation, high sustained antibodies, delayed ERT, severe baseline ventilation/feeding dependence, and advanced muscle pathology. Serial LV mass, motor milestones, ventilation status, CK and Glc4/Hex4 are useful response/prognostic measures, but none is a fully validated standalone surrogate for long-term neurologic outcome.

## 12. Treatment

### Disease-specific pharmacotherapy

**Alglucosidase alfa** is recombinant human GAA and the foundational standard of care. It is internalized through the cation-independent mannose-6-phosphate receptor and delivered to lysosomes. A conventional labeled regimen is 20 mg/kg intravenously every two weeks, although expert centers often use higher exposure—commonly 40 mg/kg weekly or every two weeks—in IOPD based on disease severity and emerging outcome data. Exact dosing must follow jurisdictional labeling and specialist protocols. Long-term survivors in one cohort received cumulative biweekly doses of 20–40 mg/kg. (prater2012theemergingphenotype pages 1-3)

**Avalglucosidase alfa** is glycoengineered with additional bis-mannose-6-phosphate moieties to enhance cellular uptake. It is a next-generation ERT with established use in Pompe disease in some jurisdictions and active pediatric/IOPD evaluation. Preclinical Pompe mice achieved stronger skeletal-muscle glycogen reduction and comparable heart/diaphragm clearance at fourfold lower dose than standard rhGAA. (unnisa2022genetherapydevelopments pages 2-3)

Suggested NCIT concepts are *enzyme replacement therapy*, *alglucosidase alfa*, *avalglucosidase alfa*, *intravenous infusion*, *immunosuppressive therapy*, *physical therapy*, *occupational therapy*, *speech therapy*, *mechanical ventilation*, and *enteral nutrition*; identifiers should be validated against the current NCIT release before ingestion.

### Immune-tolerance induction

CRIM status should be established or predicted urgently. CRIM-negative infants generally receive prophylactic immune-tolerance induction at ERT initiation, commonly rituximab, methotrexate, and intravenous immunoglobulin in specialist protocols. Some high-risk CRIM-positive infants may also be considered. Anti-rhGAA IgG titers and clinical/biochemical response require serial monitoring. Established high sustained titers are harder to eradicate than to prevent.

### Supportive and rehabilitative care

- Cardiac monitoring and cautious management of heart failure/arrhythmia; anesthesia requires a metabolic-cardiac team.
- Airway clearance, assisted cough, noninvasive ventilation, escalation to invasive ventilation when necessary, sleep evaluation, and prompt infection treatment.
- Swallow studies, texture adaptation, caloric/protein support, reflux treatment, and nasogastric or gastrostomy feeding when aspiration or growth failure warrants.
- Individualized PT/OT emphasizing positioning, contracture prevention, low-to-moderate submaximal activity, orthoses, mobility aids, and avoidance of overwork weakness.
- Speech-language therapy for feeding, dysarthria and augmentative communication.
- Hearing, vision, bone health, dental, developmental, educational, and psychosocial surveillance.

Surgery is not disease-modifying. Gastrostomy, tracheostomy, orthopedic procedures, and vascular access are supportive interventions selected case by case.

### Adverse effects

ERT can cause infusion-associated reactions, anaphylaxis, pyrexia, rash and antibody formation. Cardiorespiratory instability during infusion is especially consequential in infants with advanced hypertrophic cardiomyopathy. Immunomodulation adds infection, cytopenia and vaccine-response risks.

### Trials and experimental therapy

- **Mini-COMET, NCT03019406:** phase 2 pediatric IOPD study of avalglucosidase alfa in previously alglucosidase-treated patients; 22 participants; active, not recruiting in the retrieved registry record.
- **Baby-COMET, NCT04910776:** phase 3 avalglucosidase study in treatment-naïve IOPD; 17 participants; active, not recruiting.
- **NCT06666413:** phase 4 post-approval avalglucosidase study in Chinese IOPD; 13 planned participants; recruiting in the retrieved record.
- **NCT05017402:** observational study of higher-dose alglucosidase, 36 planned participants.

Gene-therapy platforms include in-vivo AAV liver-, muscle-, and CNS-directed expression and ex-vivo lentiviral HSPC therapy. Potential advantages are continuous enzyme secretion, cross-correction, immune tolerance, and CNS access; limitations include vector immunity, dose-related toxicity, pediatric growth-related dilution, redosing barriers, manufacturing, and uncertain durability. A 2023 review concluded: “Gene therapy for the treatment of patients with Pompe disease is feasible,” while emphasizing vector production, immune reactions and redosing. (leonastudillo2023currentavenuesof pages 11-12)

**Prenatal ERT** remains experimental. In a single CRIM-negative fetus treated in utero and then postnatally, cardiac function and age-appropriate motor development were normal at 13 months, biomarkers were normal, and feeding/growth were satisfactory. Placental pathology showed marked reduction of glycogen storage. This is proof of concept, not efficacy evidence from a controlled trial. DOI: [10.1056/NEJMoa2200587](https://doi.org/10.1056/nejmoa2200587), published December 2022. (cohen2022inuteroenzymereplacement pages 12-14)

**Substrate reduction:** selective muscle glycogen synthase-1 inhibition is preclinical. MZ-101 reduced skeletal-muscle glycogen comparably to ERT in Pompe mice, while combination treatment was additive and normalized muscle glycogen; translation to infants remains unproven.

## 13. Prevention

Primary prevention through lifestyle or vaccination is not possible because the disorder is inherited. Relevant prevention levels are:

- **Primary genetic prevention:** preconception carrier testing in at-risk relatives/populations, genetic counseling, IVF with preimplantation genetic testing, and prenatal diagnosis by chorionic-villus sampling or amniocentesis for known familial variants.
- **Secondary prevention:** newborn screening, rapid confirmatory testing, presymptomatic ERT, and CRIM-guided immune tolerance. This is the most effective strategy for preventing irreversible organ damage.
- **Tertiary prevention:** vaccination, respiratory-infection precautions, airway clearance, aspiration prevention, adequate nutrition, contracture/osteopenia prevention, hearing support, and multidisciplinary surveillance.

Cascade testing should be offered to siblings and extended relatives. There is no disease-specific vaccine or prophylactic medication that prevents inheritance. Standard immunizations are important, but timing may need adjustment around rituximab or other immunosuppression.

## 14. Other species and natural disease

Pompe-like GAA deficiency occurs naturally in several species, including Japanese quail and reported cattle, dogs, cats, and sheep. Orthologous **GAA** is conserved, and the shared pathology is lysosomal glycogen accumulation with skeletal/cardiac muscle disease. Species-specific severity, neuroanatomy, immune responses and lifespan limit direct extrapolation.

A 2020 review catalogued 42 glycogen-storage-disease models overall: 26 genetically modified mouse models, 15 naturally occurring models spanning quail, cats, dogs, sheep, cattle and horses, and one genetically modified zebrafish. These totals cover all GSDs, not Pompe alone; Japanese quail is the best-known spontaneous Pompe model. There is no zoonotic transmission or cross-species contagion.

Suggested taxonomy entries include *Homo sapiens* NCBI Taxon 9606, *Mus musculus* 10090, *Coturnix japonica* 93934, *Canis lupus familiaris* 9615, *Bos taurus* 9913, *Felis catus* 9685, and *Ovis aries* 9940. Breed-specific VBO mapping requires variant-specific veterinary reports.

## 15. Model organisms and experimental systems

### Gaa-knockout mice

The **Gaa−/− mouse** is the principal mammalian model. It reproduces systemic enzyme deficiency, glycogen accumulation, autophagic pathology, skeletal weakness and variable cardiac/respiratory disease. It is extensively used for ERT, AAV, immune-tolerance, glycogen-synthase inhibition and CNS-targeting studies. Limitations include differences from human infant cardiomyopathy, scale, immune responses, vector tropism, and lifespan.

Intrathecal or spinal AAV studies in Pompe mice have produced long-term neurologic/cardiac correction and increased ventilation. Chemogenetic activation of hypoglossal motoneurons has been used to dissect neural contributions to swallowing, speech-related and sleep-disordered-breathing phenotypes. These are model-organism findings, not clinical efficacy evidence. (leonastudillo2023currentavenuesof pages 11-12)

### Large animals and nonhuman primates

Large animals better model systemic delivery, anatomy and dose scaling but are scarce. In AT845 studies, systemic muscle-directed AAV increased GAA, cleared glycogen and improved function in Gaa−/− mice. High-dose treatment in cynomolgus macaques caused anti-human-GAA immune inflammation and cardiac abnormalities, whereas macaque GAA did not, illustrating species-specific xenogeneic immunogenicity and limitations of toxicity prediction.

### Cellular models

Patient fibroblasts, immortalized myoblasts, primary myotubes, CRISPR-engineered cells, and patient-derived iPSC cardiomyocytes/skeletal myocytes model enzyme processing, lysosomal storage, autophagy, cardiomyocyte hypertrophy, variant function and therapeutic rescue. Limitations include immature iPSC phenotypes, absent whole-organ mechanics/innervation, and incomplete modeling of systemic immunity and cross-correction. Muscle organoids and neuromuscular co-cultures are promising but not yet validated diagnostic platforms.

## Recent developments and expert interpretation, 2023–2024

1. **Standardized European pathway:** the November 2024 MetabERN recommendations integrate diagnosis, ERT, immune management, respiratory/nutritional support and follow-up using AGREE II/GRADE methodology. This is the strongest recent authoritative care framework. DOI: [10.1186/s13023-024-03373-w](https://doi.org/10.1186/s13023-024-03373-w). (parenti2024theeuropeanreference pages 2-4, parenti2024theeuropeanreference pages 22-23)
2. **Variant expansion:** the August 2024 GAA review documents continued allelic growth and reinforces paired biochemical/genetic diagnosis and CRIM-informed care. DOI: [10.3390/ijms25179139](https://doi.org/10.3390/ijms25179139). (moschetti2024mutationspectrumof pages 2-3, moschetti2024mutationspectrumof pages 1-2)
3. **Real-world newborn screening:** Northeast Italy’s eight-year report showed operational feasibility at approximately 250,000 births, with three IOPD infants immediately treated, while quantifying false-positive/VUS challenges. Published December 2023; DOI: [10.3390/ijns10010003](https://doi.org/10.3390/ijns10010003). (gragnaniello2023lightandshadows pages 1-2)
4. **Gene therapy maturation:** 2023–2024 reviews conclude that AAV and lentiviral platforms are clinically plausible but remain constrained by immunity, redosing, durability and CNS delivery. DOI: [10.1097/WCO.0000000000001187](https://doi.org/10.1097/wco.0000000000001187). (leonastudillo2023currentavenuesof pages 11-12, unnisa2022genetherapydevelopments pages 18-19)
5. **Mechanism-directed combination therapy:** 2024 preclinical work on selective GYS1 inhibition supports reducing glycogen synthesis alongside replacement of its degradation pathway. This is mechanistically compelling but not yet human IOPD therapy.

## Evidence limitations

IOPD is ultra-rare, so many treatment and long-term phenotype data derive from small, nonrandomized cohorts, historical controls, registry studies, or case reports. Incidence estimates often combine infantile and late-onset Pompe disease. Omics studies are disproportionately based on late-onset muscle or animal models. Exact phenotype frequencies are therefore often qualitative rather than population percentages. Direct quotations above are limited to text available from retrieved abstracts; absence of a PMID in this report means it was not reliably present in the retrieved record, not that the article lacks one.

References

1. (parenti2024theeuropeanreference pages 2-4): Giancarlo Parenti, Simona Fecarotta, Marianna Alagia, Federica Attaianese, Alessandra Verde, Antonietta Tarallo, Vincenza Gragnaniello, Athanasia Ziagaki, Maria Jose’ Guimaraes, Patricio Aguiar, Andreas Hahn, Olga Azevedo, Maria Alice Donati, Beata Kiec-Wilk, Maurizio Scarpa, Nadine A. M. E. van der Beek, Mireja Del Toro Riera, Dominique P. Germain, Hidde Huidekoper, Johanna M. P. van den Hout, Ans T. van der Ploeg, Ivo Baric, Spyros Batzios, Nadia Belmatoug, Andrea Bordugo, Annet M. Bosch, Anais Brassier, Alberto Burlina, David Cassiman, Brigitte Chabrol, Efstathia Chronopoulou, Maria Luz Couce-Pico, Niklas Darin, Anibh M. Das, Francois G. Debray, Patrick Deegan, Luisa M. de Abreu Freire Diogo Matos, Javier De Las Heras Montero, Maja Di Rocco, Dries Dobbelaere, Francois Eyskens, Ana Ferreira, Ana M. Gaspar, Serena Gasperini, Antonio González-Meneses López, Salvatore Grosso, Nathalie Guffon-Fouilhoux, Julia Hennermann, Tarekegn G. Hiwot, Simon Jones, Sandra Kingma, Veroniki Komninaka, Elena Martín-Hernández, Esmeralda Martins, Diana Miclea, György Pfliegler, Esmeralda Rodrigues, Dariusz Rokicki, Dominique Roland, Frank Rutsch, Alessandro Salviati, Ivailo Tournev, Kurt Ullrich, Peter M. van Hasselt, Suresh Vijay, Natalie Weinhold, Peter Witters, and Jiri Zeman. The european reference network for metabolic diseases (metabern) clinical pathway recommendations for pompe disease (acid maltase deficiency, glycogen storage disease type ii). Orphanet Journal of Rare Diseases, Nov 2024. URL: https://doi.org/10.1186/s13023-024-03373-w, doi:10.1186/s13023-024-03373-w. This article has 28 citations and is from a peer-reviewed journal.

2. (moschetti2024mutationspectrumof pages 1-2): Marta Moschetti, Alessia Lo Curto, Miriam Giacomarra, Daniele Francofonte, Carmela Zizzo, Elisa Messina, Giovanni Duro, and Paolo Colomba. Mutation spectrum of gaa gene in pompe disease: current knowledge and results of an italian study. International Journal of Molecular Sciences, 25:9139, Aug 2024. URL: https://doi.org/10.3390/ijms25179139, doi:10.3390/ijms25179139. This article has 9 citations.

3. (prater2012theemergingphenotype pages 1-3): Sean N. Prater, Suhrad G. Banugaria, Stephanie M. DeArmey, Eleanor G. Botha, Erin M. Stege, Laura E. Case, Harrison N. Jones, Chanika Phornphutkul, Raymond Y. Wang, Sarah P. Young, and Priya S. Kishnani. The emerging phenotype of long-term survivors with infantile pompe disease. Sep 2012. URL: https://doi.org/10.1038/gim.2012.44, doi:10.1038/gim.2012.44. This article has 226 citations and is from a highest quality peer-reviewed journal.

4. (OpenTargets Search: Pompe disease-GAA): Open Targets Query (Pompe disease-GAA, 43 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (moschetti2024mutationspectrumof pages 2-3): Marta Moschetti, Alessia Lo Curto, Miriam Giacomarra, Daniele Francofonte, Carmela Zizzo, Elisa Messina, Giovanni Duro, and Paolo Colomba. Mutation spectrum of gaa gene in pompe disease: current knowledge and results of an italian study. International Journal of Molecular Sciences, 25:9139, Aug 2024. URL: https://doi.org/10.3390/ijms25179139, doi:10.3390/ijms25179139. This article has 9 citations.

6. (uribecarretero2024lysosomaldysfunctionconnecting pages 14-16): Elisabet Uribe-Carretero, Verónica Rey, Jose Manuel Fuentes, and Isaac Tamargo-Gómez. Lysosomal dysfunction: connecting the dots in the landscape of human diseases. Biology, 13:34, Jan 2024. URL: https://doi.org/10.3390/biology13010034, doi:10.3390/biology13010034. This article has 15 citations.

7. (leonastudillo2023currentavenuesof pages 11-12): Carmen Leon-Astudillo, Prasad D. Trivedi, Ramon C. Sun, Matthew Gentry, Barry J. Byrne, and Manuela Corti. Current avenues of gene therapy in pompe disease. Jul 2023. URL: https://doi.org/10.1097/wco.0000000000001187, doi:10.1097/wco.0000000000001187. This article has 23 citations and is from a peer-reviewed journal.

8. (unnisa2022genetherapydevelopments pages 2-3): Zeenath Unnisa, John K. Yoon, Jeffrey W. Schindler, Chris Mason, and Niek P. van Til. Gene therapy developments for pompe disease. Biomedicines, 10:302, Jan 2022. URL: https://doi.org/10.3390/biomedicines10020302, doi:10.3390/biomedicines10020302. This article has 71 citations.

9. (gragnaniello2023lightandshadows pages 1-2): Vincenza Gragnaniello, Chiara Cazzorla, Daniela Gueraldi, Andrea Puma, Christian Loro, Elena Porcù, Maria Stornaiuolo, Paolo Miglioranza, Leonardo Salviati, Alessandro P Burlina, and Alberto B Burlina. Light and shadows in newborn screening for lysosomal storage disorders: eight years of experience in northeast italy. International Journal of Neonatal Screening, Dec 2023. URL: https://doi.org/10.3390/ijns10010003, doi:10.3390/ijns10010003. This article has 36 citations.

10. (wang2025effectofnewborn pages 1-2): Xin Wang, Yun Sun, Xian-Wei Guan, Yan-Yun Wang, Dong-Yang Hong, Zhi-Lei Zhang, Ya-Hong Li, Pei-Ying Yang, Tao jiang, and Zheng-feng Xu. Effect of newborn genomic screening for lysosomal storage disorders: a cohort study in china. Genome Medicine, May 2025. URL: https://doi.org/10.1186/s13073-025-01483-z, doi:10.1186/s13073-025-01483-z. This article has 2 citations and is from a highest quality peer-reviewed journal.

11. (cohen2022inuteroenzymereplacement pages 12-14): Jennifer L. Cohen, Pranesh Chakraborty, Karen Fung-Kee-Fung, Marisa E. Schwab, Deeksha Bali, Sarah P. Young, Michael H. Gelb, Hamid Khaledi, Alicia DiBattista, Stacey Smallshaw, Felipe Moretti, Derek Wong, Catherine Lacroix, Dina El Demellawy, Kyle C. Strickland, Jane Lougheed, Anita Moon-Grady, Billie R. Lianoglou, Paul Harmatz, Priya S. Kishnani, and Tippi C. MacKenzie. In utero enzyme-replacement therapy for infantile-onset pompe’s disease. New England Journal of Medicine, 387:2150-2158, Dec 2022. URL: https://doi.org/10.1056/nejmoa2200587, doi:10.1056/nejmoa2200587. This article has 136 citations and is from a highest quality peer-reviewed journal.

12. (parenti2024theeuropeanreference pages 22-23): Giancarlo Parenti, Simona Fecarotta, Marianna Alagia, Federica Attaianese, Alessandra Verde, Antonietta Tarallo, Vincenza Gragnaniello, Athanasia Ziagaki, Maria Jose’ Guimaraes, Patricio Aguiar, Andreas Hahn, Olga Azevedo, Maria Alice Donati, Beata Kiec-Wilk, Maurizio Scarpa, Nadine A. M. E. van der Beek, Mireja Del Toro Riera, Dominique P. Germain, Hidde Huidekoper, Johanna M. P. van den Hout, Ans T. van der Ploeg, Ivo Baric, Spyros Batzios, Nadia Belmatoug, Andrea Bordugo, Annet M. Bosch, Anais Brassier, Alberto Burlina, David Cassiman, Brigitte Chabrol, Efstathia Chronopoulou, Maria Luz Couce-Pico, Niklas Darin, Anibh M. Das, Francois G. Debray, Patrick Deegan, Luisa M. de Abreu Freire Diogo Matos, Javier De Las Heras Montero, Maja Di Rocco, Dries Dobbelaere, Francois Eyskens, Ana Ferreira, Ana M. Gaspar, Serena Gasperini, Antonio González-Meneses López, Salvatore Grosso, Nathalie Guffon-Fouilhoux, Julia Hennermann, Tarekegn G. Hiwot, Simon Jones, Sandra Kingma, Veroniki Komninaka, Elena Martín-Hernández, Esmeralda Martins, Diana Miclea, György Pfliegler, Esmeralda Rodrigues, Dariusz Rokicki, Dominique Roland, Frank Rutsch, Alessandro Salviati, Ivailo Tournev, Kurt Ullrich, Peter M. van Hasselt, Suresh Vijay, Natalie Weinhold, Peter Witters, and Jiri Zeman. The european reference network for metabolic diseases (metabern) clinical pathway recommendations for pompe disease (acid maltase deficiency, glycogen storage disease type ii). Orphanet Journal of Rare Diseases, Nov 2024. URL: https://doi.org/10.1186/s13023-024-03373-w, doi:10.1186/s13023-024-03373-w. This article has 28 citations and is from a peer-reviewed journal.

13. (unnisa2022genetherapydevelopments pages 18-19): Zeenath Unnisa, John K. Yoon, Jeffrey W. Schindler, Chris Mason, and Niek P. van Til. Gene therapy developments for pompe disease. Biomedicines, 10:302, Jan 2022. URL: https://doi.org/10.3390/biomedicines10020302, doi:10.3390/biomedicines10020302. This article has 71 citations.

## Artifacts

- [Edison artifact artifact-00](Infantile-Onset_Pompe_Disease-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.