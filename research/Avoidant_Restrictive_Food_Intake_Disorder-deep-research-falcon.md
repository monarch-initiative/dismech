---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-29T23:12:09.099914'
end_time: '2026-07-29T23:20:30.857107'
duration_seconds: 501.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Avoidant Restrictive Food Intake Disorder
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Avoidant_Restrictive_Food_Intake_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Avoidant Restrictive Food Intake Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Avoidant Restrictive Food Intake Disorder** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
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
- **Disease Name:** Avoidant Restrictive Food Intake Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Avoidant Restrictive Food Intake Disorder** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Avoidant/Restrictive Food Intake Disorder (ARFID): Disease Characteristics Report

## Executive summary

Avoidant/restrictive food intake disorder (ARFID) is a psychiatric feeding/eating disorder in which persistent restriction of food quantity or variety causes clinically important nutritional, growth, medical, supplement-dependence, or psychosocial consequences **without restriction being driven primarily by weight or shape concerns**. The three canonical presentations—sensory sensitivity, lack of interest/low appetite, and fear of aversive consequences—are dimensions that frequently overlap rather than mutually exclusive subtypes. In a 2024 UK/Republic of Ireland surveillance study of 319 clinically diagnosed young people, the largest class was a combined sensory/lack-of-interest presentation (38.2%). (fonseca2024avoidantrestrictivefood pages 1-2, sanchezcerezo2024subtypesofavoidantrestrictive pages 1-2)

Current understanding favors a multifactorial developmental disorder involving sensory processing, appetite/homeostatic signaling, fear learning/negative valence, neurodevelopmental vulnerability, medical experiences, and family/environmental reinforcement. No monogenic cause, pathogenic variant, diagnostic molecular biomarker, or disease-specific drug has been established. Treatment is therefore individualized and multidisciplinary, with nutritional rehabilitation plus exposure-based cognitive-behavioral therapy or family-based treatment providing the most promising evidence. Most efficacy evidence nevertheless remains from case series, uncontrolled studies, and recently completed trials whose definitive results are not yet widely published. (fonseca2024avoidantrestrictivefood pages 13-14, fonseca2024avoidantrestrictivefood pages 12-13, fonseca2024avoidantrestrictivefood pages 4-6)

The following table summarizes the highest-yield evidence.

| Domain | Best current evidence | Evidence strength/limitations | Key source metadata |
|---|---|---|---|
| Definition & identifiers | ARFID is a DSM-5/ICD-11 feeding/eating disorder defined by persistent restriction/avoidance causing inability to meet nutritional/energy needs with weight/growth effects, nutritional deficiency, supplement/enteral dependence, or psychosocial impairment, without body-image disturbance; MeSH term present in ClinicalTrials derived metadata: “Avoidant Restrictive Food Intake Disorder” (fonseca2024avoidantrestrictivefood pages 1-2, sanchezcerezo2024subtypesofavoidantrestrictive pages 1-2, NCT06110806 chunk 2) | Strong consensus on nosology; MONDO/OMIM not established in retrieved evidence; mostly disease-level aggregated resources rather than EHR-derived data | Fonseca et al., *J Eat Disord* 2024, published Jun 2024, DOI: https://doi.org/10.1186/s40337-024-01021-z; Sanchez-Cerezo et al., *eClinicalMedicine* 2024, Feb 2024, DOI: https://doi.org/10.1016/j.eclinm.2024.102440; ClinicalTrials.gov NCT06110806 posted 2023-11-01 (fonseca2024avoidantrestrictivefood pages 1-2, sanchezcerezo2024subtypesofavoidantrestrictive pages 1-2, NCT06110806 chunk 2) |
| Diagnostic presentations & 2024 latent classes | Core presentations: sensory sensitivity, lack of interest/low appetite, fear of aversive consequences; 2024 UK/ROI surveillance LCA of 319 cases identified 4 classes: Fear 7.2% (n=23), Lack of Interest 25.1% (n=80), Sensory 29.5% (n=94), Combined 38.2% (n=122) (fonseca2024avoidantrestrictivefood pages 1-2, sanchezcerezo2024subtypesofavoidantrestrictive pages 1-2) | Strongest recent empirical subtype evidence in pediatric secondary care; may not generalize to adults/community samples | Sanchez-Cerezo et al., *eClinicalMedicine* 2024, Feb 2024, DOI above; Fonseca et al. 2024 review (fonseca2024avoidantrestrictivefood pages 1-2, sanchezcerezo2024subtypesofavoidantrestrictive pages 1-2) |
| Epidemiology | Recent review summarizes prevalence estimates around 0.5–5% in children/adults; pediatric surveillance incidence in Canada reported as 2.02 per 100,000 ages 5–18 years (95% CI 1.76–2.31); mean age often 11.1–14.6 years; males comprise roughly 21–50% in clinical samples (fonseca2024avoidantrestrictivefood pages 2-4, sanchezcerezo2024subtypesofavoidantrestrictive pages 2-3) | Estimates highly heterogeneous by setting and method; no robust incidence data for adults in retrieved evidence | Fonseca et al., *J Eat Disord* 2024; Sanchez-Cerezo et al., *eClinicalMedicine* 2024 (fonseca2024avoidantrestrictivefood pages 2-4, sanchezcerezo2024subtypesofavoidantrestrictive pages 2-3) |
| Etiology, risk factors & comorbidity | Multifactorial model: predisposing neurodevelopmental/medical factors (ASD, ADHD, GI/neurologic disorders, food allergy), precipitating events (vomiting, choking, abdominal pain, bullying, bereavement, medication start), and perpetuating family/behavioral factors; anxiety disorders common (9.1–72%); ASD frequently co-occurs, especially sensory/combined presentations (fonseca2024avoidantrestrictivefood pages 4-6, sanchezcerezo2024subtypesofavoidantrestrictive pages 2-3, nocerino2024developmentandmanagement pages 4-6) | Mostly observational and review-level evidence; causal direction often unclear; protective factors not well established in retrieved literature | Fonseca et al. 2024; Sanchez-Cerezo et al. 2024; Nocerino et al., *Nutrients* 2024, Sep 2024, DOI: https://doi.org/10.3390/nu16173034 (fonseca2024avoidantrestrictivefood pages 4-6, sanchezcerezo2024subtypesofavoidantrestrictive pages 2-3, nocerino2024developmentandmanagement pages 4-6) |
| Genetics | No monogenic cause established. Review evidence cites a Swedish twin study showing important genetic contribution/high heritability; one review notes a reported locus near **ZSWIM6**, but this was not primary-source validated in retrieved accessible texts. Large-scale ARFID genetics infrastructure is expanding via EDGI2 (tomaszek2025unravelingtheconnections pages 2-4) | Genetic architecture remains early-stage; retrieved evidence does not support causal genes, ClinVar variants, or penetrance estimates for ARFID | Tomaszek et al., *Nutrients* 2025, Jan 2025, DOI: https://doi.org/10.3390/nu17030486; EDGI2 protocol, *BMC Psychiatry* 2025, DOI: https://doi.org/10.1186/s12888-025-06777-5 (not context-cited in table cells beyond accessible ID) (tomaszek2025unravelingtheconnections pages 2-4) |
| Mechanisms / pathophysiology | Best current model is 3-dimensional: altered sensory processing, appetite/homeostatic dysregulation, and negative valence/fear circuitry. Hypothesized regions/signals include insula, orbitofrontal cortex, hypothalamus, amygdala, anterior cingulate, and gut-brain hormones (ghrelin, PYY, CCK, GLP-1). ARFID severity is linked to lower anticipatory pleasure, especially lack-of-interest phenotype; depression partly explains anhedonia findings (fonseca2024avoidantrestrictivefood pages 1-2, fonseca2024avoidantrestrictivefood pages 6-7, dolan2023anticipatoryandconsummatory pages 1-2, dolan2023anticipatoryandconsummatory pages 8-9) | Human evidence is still limited and partly hypothesis-driven; little validated omics or pathway-level molecular profiling; no disease-specific GO/CL mappings directly established in retrieved sources | Fonseca et al. 2024 review; Dolan et al., *J Eat Disord* 2023, Nov 2023, DOI: https://doi.org/10.1186/s40337-023-00921-w (fonseca2024avoidantrestrictivefood pages 1-2, fonseca2024avoidantrestrictivefood pages 6-7, dolan2023anticipatoryandconsummatory pages 1-2, dolan2023anticipatoryandconsummatory pages 8-9) |
| Phenotypes, complications & QoL | Complications include malnutrition, growth delay, enteral dependence, hospitalization, hypokalemia, fatigue, lethargy, presyncope, constipation, cold intolerance, hypothermia, dry skin, lanugo, alopecia, bradycardia, orthostatic tachycardia, hypotension, pubertal delay/amenorrhea, lower bone mineral density, oral-motor and speech delays; selective eating also impairs social/emotional development and increases family conflict (fonseca2024avoidantrestrictivefood pages 9-10, fonseca2024avoidantrestrictivefood pages 10-12, nocerino2024developmentandmanagement pages 4-6) | Strong clinical face validity; frequency estimates for individual complications are sparse; QoL often described qualitatively rather than with standardized ARFID-specific metrics in retrieved evidence | Fonseca et al. 2024; Nocerino et al. 2024 (fonseca2024avoidantrestrictivefood pages 9-10, fonseca2024avoidantrestrictivefood pages 10-12, nocerino2024developmentandmanagement pages 4-6) |
| Diagnostics & assessment tools | Diagnosis remains clinical/DSM-based with exclusion of food unavailability, cultural practice, anorexia/bulimia, and other medical/psychiatric explanations. PARDI has Cronbach α 0.77–0.89 and diagnostic reliability κ=0.75; NIAS total α=0.84, ω=0.90. Trials also use PARDI-AR-Q, EDA-5, labs (thyroid, celiac), anthropometrics, and sometimes fMRI (fonseca2024avoidantrestrictivefood pages 9-10, sanchezcerezo2024subtypesofavoidantrestrictive pages 3-4, NCT05954728 chunk 1) | Good early psychometrics for screening/interview tools; no universal gold-standard biomarker; diagnostic workup must exclude medical mimics | Fonseca et al. 2024; Sanchez-Cerezo et al. 2024; ClinicalTrials.gov NCT05954728 (fonseca2024avoidantrestrictivefood pages 9-10, sanchezcerezo2024subtypesofavoidantrestrictive pages 3-4, NCT05954728 chunk 1) |
| Treatment | Multidisciplinary care is standard. Nutritional rehabilitation prioritizes weight restoration and adequacy of macro/micronutrients, with cautious temporary enteral support when necessary. Psychological approaches with best current support are CBT-AR and family-based treatment (FBT-ARFID). Review-level evidence describes significant reductions in ARFID severity, increased food variety, and weight gain in CBT-AR proof-of-concept studies; small FBT case series also report weight gain and reduced anxiety (fonseca2024avoidantrestrictivefood pages 13-14, fonseca2024avoidantrestrictivefood pages 10-12, fonseca2024avoidantrestrictivefood pages 12-13) | Evidence base still dominated by case series, pilot studies, and nonrandomized designs; no FDA-approved medication for ARFID | Fonseca et al. 2024, DOI above (fonseca2024avoidantrestrictivefood pages 13-14, fonseca2024avoidantrestrictivefood pages 10-12, fonseca2024avoidantrestrictivefood pages 12-13) |
| Pharmacotherapy | Adjunctive medications reported include olanzapine, mirtazapine, fluoxetine, cyproheptadine, and buspirone. Review cites mirtazapine-associated BMI change rising from 0.10 to 0.23/week after initiation and notes olanzapine may improve appetite, anxiety, and rigidity; all evidence is case-based/small series (fonseca2024avoidantrestrictivefood pages 12-13, fonseca2024avoidantrestrictivefood pages 13-14) | Very low-certainty evidence; no approved drug and no definitive randomized placebo-controlled data in retrieved sources | Fonseca et al., *J Eat Disord* 2024 (fonseca2024avoidantrestrictivefood pages 12-13, fonseca2024avoidantrestrictivefood pages 13-14) |
| Clinical trials / implementation | Key active/completed trials include: Stanford FBT-ARFID efficacy/mechanism RCT vs non-specific care, ages 6–12, n=98, completed (NCT04450771); earlier Stanford crossover FBT feasibility trial, ages 5–12, n=28, completed (NCT03778216); MGH COUNTERACT RCT of CBT-AR vs nutrition counseling, ages 10–18, n=53, completed (NCT05954728); MGH CBT-AR pilot single-group, ages 10–65, n=35, completed (NCT02963220); Mount Sinai MBIE family-based interoceptive exposure, actual n=12, terminated for risk-mitigation-plan disagreement (NCT06110806) (NCT04450771 chunk 1, NCT03778216 chunk 1, NCT05954728 chunk 1, NCT02963220 chunk 1, NCT06110806 chunk 1) | Strong signal of growing implementation research; many results still pending publication or limited to protocol/trial registry detail | ClinicalTrials.gov: NCT04450771, NCT03778216, NCT05954728, NCT02963220, NCT06110806 (NCT04450771 chunk 1, NCT03778216 chunk 1, NCT05954728 chunk 1, NCT02963220 chunk 1, NCT06110806 chunk 1) |
| Natural disease in other species / models | No recognized naturally occurring veterinary ARFID entity or validated full-disorder animal model was identified in retrieved evidence; at most, component traits such as sensory aversion, appetite regulation, fear conditioning, or gut-brain signaling can be modeled separately | Important negative finding; avoids over-interpreting feeding phenotypes in animals as DSM-defined ARFID | No disease-specific comparative biology source identified in retrieved ARFID literature (fonseca2024avoidantrestrictivefood pages 1-2, fonseca2024avoidantrestrictivefood pages 14-15) |


*Table: This compact table summarizes the best available current evidence for avoidant/restrictive food intake disorder across definition, subtypes, epidemiology, mechanisms, diagnostics, treatment, and trials. It emphasizes where evidence is strongest and where important limitations remain.*

## 1. Disease information

### Definition and scope

DSM-5 introduced ARFID in 2013 as the successor to and expansion of “feeding disorder of infancy or early childhood.” It includes children, adolescents, and adults. Criterion A requires an eating/feeding disturbance with persistent failure to meet nutritional or energy needs and at least one of: significant weight loss or failure to grow appropriately; significant nutritional deficiency; dependence on oral supplements or enteral feeding; or marked interference with psychosocial functioning. Restriction cannot be adequately explained by unavailable food or culturally sanctioned practice, cannot occur exclusively during anorexia nervosa or bulimia nervosa, and is not driven by body-weight or shape disturbance. If another medical or psychiatric disorder is present, restriction must exceed what that condition ordinarily explains and independently require clinical attention. (fonseca2024avoidantrestrictivefood pages 1-2, sanchezcerezo2024subtypesofavoidantrestrictive pages 1-2, sanchezcerezo2024subtypesofavoidantrestrictive pages 3-4)

**Direct abstract wording:** Sanchez-Cerezo et al. described ARFID as “persistent disturbance in feeding or eating” causing inability to meet nutritional/energy needs, while emphasizing that it “is not associated with concerns about gaining weight nor with a preoccupation about body weight, shape, or size.” The study was published in *eClinicalMedicine* in February 2024; DOI: https://doi.org/10.1016/j.eclinm.2024.102440. (sanchezcerezo2024subtypesofavoidantrestrictive pages 1-2)

### Identifiers and synonyms

- **MeSH:** Avoidant Restrictive Food Intake Disorder, **D000080146**. (NCT06110806 chunk 2)
- **ICD-11:** ARFID is recognized as a feeding or eating disorder; the commonly used ICD-11 code is **6B83**.
- **ICD-10-CM:** **F50.82**, Avoidant/restrictive food intake disorder.
- **DSM-5/DSM-5-TR:** Avoidant/restrictive food intake disorder.
- **MONDO:** A stable MONDO identifier was not verified in the retrieved authoritative material; populate only after direct confirmation from the current MONDO release.
- **OMIM/Orphanet:** No disease-specific entry is expected because ARFID is neither an established Mendelian disease nor conventionally classified as a rare genetic disorder.
- **Synonyms:** avoidant/restrictive food intake disorder; avoidant restrictive food intake disorder; ARFID; historically, selective eating disorder. “Picky eating,” food neophobia, infantile anorexia, and pediatric feeding disorder overlap clinically but are not synonyms unless full diagnostic criteria are met. (fonseca2024avoidantrestrictivefood pages 1-2, nocerino2024developmentandmanagement pages 4-6)

The evidence summarized here is aggregated disease-level literature and trial-registry data, not individual EHR-derived patient data. Individual case reports and clinical cohorts contribute to treatment evidence but should not be treated as population estimates.

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal framework

ARFID has no single necessary or sufficient cause. A useful model separates:

1. **Predisposing factors:** sensory hyperresponsivity, anxiety temperament, ASD, ADHD, GI or neurologic disease, food allergy, and possibly inherited appetite or taste sensitivity.
2. **Precipitating factors:** choking, vomiting, abdominal pain, allergic reaction or fear of one, painful oral/GI procedures, medication initiation, bullying, bereavement, or other stressful events.
3. **Perpetuating factors:** conditioned fear and avoidance, relief following food refusal, provision of only preferred foods, reduced exposure to novel foods, parental distress or coercive mealtime interactions, malnutrition-associated early satiety/GI dysmotility, and social withdrawal. In one retrospective cohort summarized by the 2024 review, 71.4% reported an identifiable trigger. (fonseca2024avoidantrestrictivefood pages 4-6)

Food allergy illustrates a plausible gene–environment/medical–behavioral pathway: a genuine adverse reaction produces heightened threat expectancy; avoidance generalizes beyond the allergen to tolerated foods; parental anxiety and limited dietary exposure reinforce fear; and reduced variety produces deficiency and psychosocial impairment. This is clinical observational evidence, not proof that allergy independently causes ARFID. (nocerino2024developmentandmanagement pages 4-6)

### Genetic risk

A Swedish twin study published in 2023 reported substantial heritability for a **broad pediatric ARFID phenotype**, with nonshared environmental effects also contributing. However, the broad phenotype did not fully represent all fear-of-aversive-consequence cases, so it should not be interpreted as the heritability of DSM-5 ARFID in its entirety. Recent reviews mention a chromosome-5 signal near **ZSWIM6**, but a causal locus or clinically actionable variant has not been validated in the retrieved primary evidence. (tomaszek2025unravelingtheconnections pages 2-4, sanchezcerezo2024subtypesofavoidantrestrictive pages 9-10)

Accordingly:

- **Causal genes/pathogenic variants:** none established.
- **Inheritance:** complex, multifactorial/polygenic—not Mendelian.
- **Penetrance, carrier frequency, anticipation, founder effects, germline mosaicism:** not applicable or unknown.
- **ClinVar/ClinGen testing:** no ARFID-specific clinically validated gene or panel.
- **Modifier genes/epigenetics:** no replicated ARFID-specific modifiers or epigenetic signature.
- **Somatic variants/chromosomal abnormalities:** not features of idiopathic ARFID.

### Environmental and lifestyle risks

There is no established toxin, pollutant, radiation, occupational exposure, infection, smoking, alcohol, or exercise exposure that specifically causes ARFID. Relevant “environmental” factors are mainly developmental and experiential: limited early food exposure, adverse feeding experiences, food insecurity as a diagnostic alternative rather than ARFID, family accommodation, and culturally mediated food availability. Food restriction due solely to poverty, famine, neglect, religious observance, or another culturally sanctioned practice excludes ARFID. (sanchezcerezo2024subtypesofavoidantrestrictive pages 3-4)

### Protective factors

No genetic protective variant is established. Plausible but incompletely tested protective factors include responsive feeding, repeated noncoercive exposure to varied foods, prompt treatment of pain/allergy/GI disease, accurate allergy education, predictable meals, avoidance of unnecessary elimination diets, parental self-efficacy, and early multidisciplinary intervention. These should be annotated as expert-informed prevention strategies, not proven primary-prevention effects.

## 3. Phenotypes

### Core behavioral phenotypes

1. **Sensory sensitivity:** rejection based on texture, taste, smell, temperature, color, appearance, brand, or foods touching. It often begins early and may remain stable without intervention. Suggested HPO concepts: **Feeding difficulties (HP:0011968)**, abnormal eating behavior, and sensory hypersensitivity; exact current HPO IDs should be validated before ingestion.
2. **Lack of interest/low appetite:** little hunger, early satiety, forgetting to eat, small bites, slow or prolonged meals, and low anticipatory reward. Suggested HPO: **Poor appetite (HP:0004396)** and feeding difficulties.
3. **Fear of aversive consequences:** acute or subacute avoidance following choking, vomiting, pain, allergic reaction, or invasive procedures; fear may generalize to entire food groups or settings. Suggested HPO: feeding difficulties, anxiety, vomiting, dysphagia/choking where actually present.
4. **Mixed/combined presentation:** common and clinically important. In 319 UK/ROI cases aged 5–18, classes were Fear 7.2% (23), Lack of Interest 25.1% (80), Sensory 29.5% (94), and Combined 38.2% (122). Younger age, male sex, eating distress, weight loss, and ASD distinguished class membership. (sanchezcerezo2024subtypesofavoidantrestrictive pages 9-10, sanchezcerezo2024subtypesofavoidantrestrictive pages 1-2)

A Swiss school study summarized in the 2024 paper found ARFID features in 3.2%; among these children, 39% reported lack of interest, 60% sensory sensitivity, 15% fear, and 15% multiple presentations. Because dimensions overlap, percentages need not sum to 100%. (sanchezcerezo2024subtypesofavoidantrestrictive pages 2-3)

### Physical and laboratory phenotypes

Depending on diet and severity, findings include weight loss or faltering growth, underweight, anemia, hypokalemia, micronutrient deficiencies, fatigue, lethargy, impaired memory, presyncope, constipation, cold intolerance, hypothermia, dry skin, lanugo, alopecia, bradycardia, orthostatic tachycardia/hypotension, delayed puberty, amenorrhea, and low bone mineral density. Oral-motor or speech delay may occur when children have had little experience chewing complex textures. (fonseca2024avoidantrestrictivefood pages 9-10, fonseca2024avoidantrestrictivefood pages 10-12)

Deficiencies depend more on foods omitted than on BMI. Restriction of grains risks inadequate carbohydrate and fiber; animal products/dairy/legumes can reduce protein, riboflavin, B12, iron, selenium, and zinc; fish avoidance can reduce vitamin D and omega-3 intake; fruit/vegetable avoidance can reduce vitamin C and folate; and broad fat restriction can reduce vitamins A, D, E, and K. Normal or high body weight therefore does not exclude significant nutritional deficiency. (fonseca2024avoidantrestrictivefood pages 12-13)

### Psychosocial and quality-of-life phenotypes

Patients may be unable to eat at school, restaurants, celebrations, or with peers; may carry preferred foods everywhere; experience tantrums or severe distress; and have excessively long meals, school impairment, restricted peer relationships, and family conflict. These impairments can satisfy Criterion A even without underweight. Standardized ARFID-specific quality-of-life data remain sparse; trials use measures such as the Clinical Impairment Assessment, SF-36, Strengths and Difficulties Questionnaire, and pediatric generic quality-of-life scales. (fonseca2024avoidantrestrictivefood pages 10-12, sanchezcerezo2024subtypesofavoidantrestrictive pages 3-4, NCT04450771 chunk 2)

## 4. Genetic and molecular information

No causal gene, HGNC-annotated pathogenic variant, ACMG/AMP classification, allele frequency, protein loss/gain of function, or diagnostic structural variant is established for ARFID. WES, WGS, CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are **not routine ARFID tests**. They are appropriate only when syndromic features, intellectual disability, congenital anomalies, neurologic findings, or another suspected genetic disorder independently warrant investigation.

Molecular profiling is preliminary. There is no replicated disease-defining transcriptomic, proteomic, metabolomic, lipidomic, epigenomic, single-cell, spatial-transcriptomic, multi-omic, or CRISPR-screen signature. This negative annotation is important: ARFID is currently diagnosed phenotypically, not molecularly.

## 5. Environmental information

No infectious agent or zoonotic transmission is implicated. GI disease, food allergy, pain, vomiting and choking are medical/environmental triggers rather than infectious etiologies. Restrictive diets prescribed for legitimate disease can become disproportionate and impairing; clinicians should distinguish medically necessary avoidance from generalized fear and restriction exceeding medical requirements. In GI populations, reported ARFID-screen positivity varies substantially—approximately 40% in some disorder-of-gut–brain-interaction samples, 17% in IBD, and 6–24% in neurogastroenterology settings—although these figures are not general-population prevalence and may be inflated by symptom overlap or screening methods. (che2025avoidantrestrictivefoodintake pages 13-15)

## 6. Mechanism and pathophysiology

### Three-dimensional model

**Sensory pathway:** inherited/developmental sensory responsivity and altered integration of taste, smell, touch, and visual food cues → intense aversive experience → selective refusal → reduced exposure and nutritional variety → reinforcement of sensory avoidance. Candidate systems include gustatory/olfactory pathways and insular sensory integration. Taste-receptor variation such as **TAS2R**-family bitter sensitivity is biologically plausible but not an established ARFID cause. (fonseca2024avoidantrestrictivefood pages 4-6, fonseca2024avoidantrestrictivefood pages 6-7)

**Homeostatic/appetite pathway:** reduced hunger, early satiation, or low food reward → inadequate meal initiation/maintenance → low intake and growth/weight consequences. Candidate structures include hypothalamus, brainstem, insula, and orbitofrontal reward networks. Preliminary endocrine studies have examined ghrelin, peptide YY, cholecystokinin, and GLP-1; findings are inconsistent and may reflect malnutrition rather than upstream disease. A cited study found higher fasting CCK in full/subthreshold ARFID than controls after adjustment, while low-weight ARFID showed lower meal-related total ghrelin than anorexia nervosa. These remain research findings, not biomarkers. (fonseca2024avoidantrestrictivefood pages 6-7)

**Negative-valence/fear pathway:** adverse event → amygdala/anterior-cingulate threat learning → anticipatory anxiety and autonomic arousal → avoidance → immediate relief (negative reinforcement) → generalization and chronic restriction. Exposure-based therapies directly target this causal loop. (fonseca2024avoidantrestrictivefood pages 6-7)

A 2023 human study of 71 participants aged 10–23 with full/subthreshold ARFID and 33 controls found lower anticipatory and consummatory pleasure, but group differences disappeared after controlling for depression or removing food items. Within ARFID, greater severity and lack-of-interest symptoms remained associated with lower anticipatory pleasure. Thus, generalized anhedonia is not established; food-specific reward and comorbid depression are important confounders. DOI: https://doi.org/10.1186/s40337-023-00921-w, published November 2023. (dolan2023anticipatoryandconsummatory pages 1-2, dolan2023anticipatoryandconsummatory pages 8-9)

Suggested ontology annotations, treated as mechanistic hypotheses rather than proven disease pathways:

- **GO biological processes:** sensory perception of taste; sensory perception of smell; feeding behavior; regulation of appetite; response to food; associative learning; fear response; energy homeostasis.
- **Cell Ontology:** neuron, sensory neuron, neuroendocrine cell, enteroendocrine cell. No ARFID-specific pathogenic cell type is established.
- **Anatomy:** hypothalamus, insular cortex, orbitofrontal cortex, amygdala, anterior cingulate cortex, brainstem, and GI tract.

## 7. Anatomical structures affected

ARFID is a functional psychiatric/behavioral syndrome, not a focal tissue lesion. The **central nervous system** mediates sensory, reward, appetite, and threat processes. The **oral cavity/pharynx/esophagus/GI tract** may be sites of triggering sensations or comorbid disease. Secondary consequences involve bone, endocrine/reproductive, cardiovascular, integumentary, hematologic, and GI systems through malnutrition.

Suggested UBERON mappings include brain (**UBERON:0000955**), hypothalamus (**UBERON:0001898**), amygdala, insular cortex, anterior cingulate cortex, oral cavity, pharynx, esophagus, stomach, small intestine, and bone tissue. There is no expected lateralization. No specific organelle or GO cellular-component defect is known.

## 8. Temporal development

Onset is commonly pediatric and may be insidious for sensory/lack-of-interest presentations or abrupt after an aversive event for fear-based ARFID. Clinical cohorts often have mean ages around 11.1–14.6 years, but onset can occur in infancy/childhood and persistence into adulthood is well documented. Sensory refusal was more common at younger ages in a 207-patient surveillance sample: 66.7% at 5–9 years, 38.6% at 10–14, and 22.2% at 15–18. (fonseca2024avoidantrestrictivefood pages 2-4, fonseca2024avoidantrestrictivefood pages 6-7)

Course is heterogeneous—stable, progressive, fluctuating, or event-triggered—and no validated disease staging system exists. Compared with anorexia nervosa, ARFID often begins younger and may require longer hospitalization or more enteral support despite similar BMI. Long-term remission, relapse, and transition-to-other-eating-disorder estimates remain inadequately characterized. Comorbidity and entrenched avoidance plausibly predict a more difficult course. (fonseca2024avoidantrestrictivefood pages 10-12, fonseca2024avoidantrestrictivefood pages 14-15)

## 9. Inheritance and population epidemiology

General-population prevalence is commonly summarized as approximately **0.5–5%**, but estimates range from 0.3% to 64% across highly dissimilar community, GI, feeding-clinic, and eating-disorder samples. The only incidence study highlighted in the recent reviews identified **2.02 cases per 100,000 persons aged 5–18 years** presenting to pediatricians (95% CI 1.76–2.31). These figures demonstrate methodological heterogeneity rather than true geographic differences. (fonseca2024avoidantrestrictivefood pages 2-4, sanchezcerezo2024subtypesofavoidantrestrictive pages 2-3)

Clinical samples include more boys than classic adolescent eating-disorder cohorts, but ARFID affects all sexes. Reported male proportions range approximately 21–50%. Boys in one surveillance sample had more sensory refusal than girls—51.2% versus 31.5%, *p*=0.007—whereas fear presentations often skew female. ASD is reported in roughly 13–50% in some clinical literature, while broader reviews report ranges from 8.2% to 54.8%; ascertainment strongly affects these estimates. Anxiety disorders are reported in 9.1–72%. (fonseca2024avoidantrestrictivefood pages 2-4, tomaszek2025unravelingtheconnections pages 2-4, fonseca2024avoidantrestrictivefood pages 4-6, sanchezcerezo2024subtypesofavoidantrestrictive pages 2-3)

There is no established ethnic restriction, endemic region, founder variant, consanguinity effect, carrier state, or population-specific penetrance.

## 10. Diagnostics

### Clinical diagnosis and workup

Diagnosis requires history from patient and caregivers, dietary assessment, growth-chart review, anthropometry, physical examination, psychosocial-functional assessment, and evaluation of body-image motivation. Clinicians should document which Criterion-A consequence is present and characterize all three dimensions rather than forcing one subtype.

Recommended tests are individualized, not diagnostic biomarkers: CBC; electrolytes, renal and hepatic indices; calcium, magnesium and phosphate; glucose; iron/ferritin; B12/folate; vitamin D and other micronutrients suggested by the excluded foods; inflammatory testing where indicated; TSH/free T4; and celiac serology. ECG is appropriate with bradycardia, syncope, electrolyte disturbance, severe malnutrition, or QT-risk medication. Bone-age or DXA assessment may be indicated with growth/puberty delay, prolonged amenorrhea, fractures, or chronic undernutrition. Imaging, endoscopy, swallow study, allergy testing, or motility studies should be driven by clinical indications—not used routinely to “confirm” ARFID. The COUNTERACT trial, for example, required normal thyroid testing and negative celiac screening to exclude medical explanations. (NCT05954728 chunk 1)

### Instruments

- **PARDI:** semistructured diagnostic/severity interview covering the three profiles; reported internal consistency α=0.77–0.89 and diagnostic reliability κ=0.75.
- **PARDI-AR-Q:** 32-item self/parent questionnaire used for dimensional symptom assessment.
- **NIAS:** nine-item screen with sensory, appetite, and fear subscales; reported total α=0.84 and ω=0.90. It is a screen, not a stand-alone diagnosis.
- **EDA-5**, Eating Disorder Examination ARFID module, and EDY-Q are additional approaches depending on age and setting. (fonseca2024avoidantrestrictivefood pages 9-10, NCT05954728 chunk 1)

### Differential diagnosis

Exclude anorexia nervosa/atypical AN and bulimia nervosa; food insecurity or cultural/religious restriction; developmentally typical picky eating; food allergy/celiac disease/eosinophilic esophagitis; inflammatory or structural GI disease; dysphagia and oral-motor disorders; gastroparesis and disorders of gut–brain interaction; endocrine/metabolic disease; malignancy or chronic infection; medication adverse effects; depression-related appetite loss; OCD contamination fears; specific phobia of choking/vomiting; psychosis; ASD-associated selectivity not independently meeting ARFID impairment criteria; rumination disorder; and pica. Another disorder can coexist when restriction is disproportionate and independently impairing. (sanchezcerezo2024subtypesofavoidantrestrictive pages 3-4)

There is no asymptomatic newborn, carrier, prenatal, or cascade screening program.

## 11. Outcome and prognosis

ARFID can produce substantial morbidity through malnutrition, growth failure, electrolyte disturbance, cardiovascular instability, delayed puberty, low bone density, dependence on supplements/tubes, and social or educational disability. Severe refeeding carries risk of potentially fatal refeeding syndrome and requires electrolyte and clinical monitoring. (fonseca2024avoidantrestrictivefood pages 9-10, fonseca2024avoidantrestrictivefood pages 12-13)

Disease-specific mortality, five- or ten-year survival, and life-expectancy estimates are unavailable. Death is biologically possible from severe malnutrition or refeeding complications, but no robust ARFID-specific mortality rate should be entered. Recovery is possible—especially with early, presentation-matched treatment—but long-term remission and relapse probabilities are not well quantified. Potential adverse prognostic factors include severe nutritional compromise, prolonged illness, multiple presentations, ASD/anxiety/OCD/trauma comorbidity, persistent pain or GI disease, tube dependence, family accommodation, and limited specialist access. No prognostic molecular biomarker exists.

## 12. Treatment

### Treatment algorithm

1. **Triage medical stability:** hospitalize or use higher care for severe bradycardia, hypotension/orthostasis, hypothermia, syncope, serious electrolyte abnormalities, acute food refusal/dehydration, suicidality, or severe malnutrition.
2. **Restore nutrition:** begin with accepted foods and oral supplements to stabilize energy intake; monitor refeeding risk; add targeted micronutrients.
3. **Treat maintaining mechanism:** graded sensory exposure and food chaining; interoceptive/appetite work and scheduled eating for lack of interest; exposure/response prevention for fear.
4. **Mobilize caregivers and environment:** structured meals, reduction of accommodation, school plans, and caregiver coaching.
5. **Treat comorbidity and relapse risk:** address anxiety, OCD, depression, ASD-related needs, allergy, pain, and GI disease without reinforcing unnecessary avoidance.

A multidisciplinary team may include pediatrics/adolescent medicine, psychiatry/psychology, dietetics, nursing, occupational or speech-language therapy, gastroenterology, and allergy specialists. (nocerino2024developmentandmanagement pages 9-11, fonseca2024avoidantrestrictivefood pages 10-12)

### Psychological interventions

**CBT-AR** is a modular four-stage treatment: psychoeducation/early change, treatment planning, mechanism-focused exposure, and relapse prevention. Youth and adult proof-of-concept studies reported reductions in PARDI severity, increased dietary variety, and weight gain among underweight participants; adult anxiety/depression did not consistently improve. The original MGH pilot enrolled 35 participants aged 10–65 for 20–30 outpatient sessions, but it was uncontrolled. (fonseca2024avoidantrestrictivefood pages 13-14, NCT02963220 chunk 1)

**FBT-ARFID** externalizes the disorder, empowers caregivers, and focuses behaviorally on changing eating. The Stanford efficacy trial randomized 98 medically stable children aged 6–12 at 75–88% expected body weight to 14 sessions of FBT-ARFID or time-matched nonspecific care over four months, with expected body weight and parental self-efficacy as primary outcomes. This is stronger design evidence, but registry completion does not itself establish superiority until analyzed results are published. Protocol PMID: **36460266**; trial: https://clinicaltrials.gov/study/NCT04450771. (NCT04450771 chunk 1, NCT04450771 chunk 2)

Suggested MAXO mappings: cognitive behavioral therapy; family therapy; exposure therapy; dietary counseling; nutritional supplementation; enteral tube feeding; weight monitoring; laboratory monitoring; electrocardiography; psychiatric assessment. Exact MAXO identifiers should be checked against the current ontology release.

### Nutrition and enteral support

Dietetic treatment calculates energy/fluid needs, repairs macro- and micronutrient gaps, schedules meals, and gradually expands variety. Oral nutrition is preferred. Enteral feeding can be lifesaving but should generally be medically necessary, goal-directed, and temporary; prolonged use may reduce expectations for oral eating and reinforce avoidance. (fonseca2024avoidantrestrictivefood pages 12-13, fonseca2024avoidantrestrictivefood pages 10-12)

### Pharmacotherapy

No medication is FDA-approved specifically for ARFID. Drugs are adjuncts for appetite, anxiety, nausea, rigidity, or comorbidity—not substitutes for nutritional/behavioral treatment. Small reports describe mirtazapine, cyproheptadine, low-dose olanzapine, SSRIs, and buspirone. A small mirtazapine report found mean weekly BMI change increased from 0.10 before treatment to 0.23 after initiation, but confounding and absence of randomization preclude an efficacy claim. Olanzapine may increase appetite and reduce rigidity but has metabolic and neurologic risks. There is no ARFID-specific pharmacogenomic guidance. (fonseca2024avoidantrestrictivefood pages 13-14, fonseca2024avoidantrestrictivefood pages 12-13)

### Recent and ongoing implementation research

- **NCT05954728 COUNTERACT:** double-masked, randomized CBT-AR versus dietitian nutrition counseling; ages 10–18; actual *n*=53; 15 weeks; outcomes include food neophobia, PARDI, diet, and food-cue fMRI. https://clinicaltrials.gov/study/NCT05954728. (NCT05954728 chunk 1)
- **NCT04450771:** FBT-ARFID versus nonspecific care; *n*=98; completed; results publication pending in the retrieved record. https://clinicaltrials.gov/study/NCT04450771. (NCT04450771 chunk 1)
- **NCT03778216:** randomized crossover feasibility trial of FBT-ARFID in ages 5–12; *n*=28. https://clinicaltrials.gov/study/NCT03778216. (NCT03778216 chunk 1)
- **NCT02963220:** single-group CBT-AR pilot; *n*=35; ages 10–65. Adult outcome paper PMID **34423319**. https://clinicaltrials.gov/study/NCT02963220. (NCT02963220 chunk 1, NCT02963220 chunk 2)
- **NCT06110806:** 20-session family-based mindfulness/interoceptive exposure; only 12 enrolled and the trial was terminated because of failure to agree on a risk-mitigation plan—not demonstrated inefficacy. https://clinicaltrials.gov/study/NCT06110806. (NCT06110806 chunk 1)

No gene, cell, RNA, targeted molecular, immunologic, or surgical therapy is indicated.

## 13. Prevention

**Primary prevention:** evidence is insufficient for a population program. Reasonable strategies include responsive/noncoercive feeding, varied age-appropriate exposure, prompt management of pain/dysphagia/allergy, avoidance of unnecessary elimination diets, and caregiver education after choking or allergic events.

**Secondary prevention:** screen high-risk groups—children with faltering growth, extreme selectivity, ASD/ADHD, anxiety, emetophobia, food allergy, eosinophilic/GI disease, prolonged tube feeding, or marked mealtime distress—and confirm diagnosis early with clinical interview. School and primary-care growth monitoring may detect consequences before severe malnutrition.

**Tertiary prevention:** monitor growth, diet and micronutrients; prevent refeeding syndrome; minimize prolonged tube dependence; maintain food exposures and relapse plans; address family accommodation and school participation; and monitor bone, pubertal, cardiovascular, and psychiatric complications. There is no vaccine, chemoprophylaxis, carrier screening, or reproductive genetic counseling specific to ARFID.

## 14. Other species and natural disease

No naturally occurring veterinary disorder equivalent to DSM-defined ARFID was identified. Animals can exhibit neophobia, conditioned taste aversion, sensory selectivity, low appetite, or post-traumatic feeding avoidance, but cannot reproduce the full human diagnosis, particularly self-reported motivation and psychosocial-impairment criteria. Therefore, no NCBI Taxon, VBO breed, orthologous causal gene, zoonotic transmission, or comparative Mendelian-disease annotation should be assigned specifically to ARFID.

## 15. Model organisms

There is no validated whole-disorder mouse, rat, zebrafish, invertebrate, organoid, or iPSC model. Component models—conditioned taste aversion, bitter-taste sensitivity, fear conditioning, altered appetite hormones, sensory hypersensitivity, or developmental restricted exposure—may test individual mechanisms. Their major limitation is poor construct validity for heterogeneous human motivations, family interactions, culture, language, and functional impairment. No ARFID-specific knockout, knock-in, humanized model, CRISPR screen, or model-organism repository entry was established in the retrieved evidence.

## Evidence appraisal and knowledge-base cautions

The most authoritative recent synthesis retrieved was Fonseca et al., published June 2024 in *Journal of Eating Disorders*, DOI: https://doi.org/10.1186/s40337-024-01021-z. Its conclusion appropriately states that assessment tools and treatments “are still in the process of development and validation.” (fonseca2024avoidantrestrictivefood pages 14-15)

The strongest 2024 primary phenotyping evidence is Sanchez-Cerezo et al.’s national active-surveillance latent-class analysis. Its finding that the combined presentation was most common argues against encoding the three presentations as mutually exclusive disease subtypes. (sanchezcerezo2024subtypesofavoidantrestrictive pages 1-2)

For database population, claims should be graded as follows:

- **Established:** clinical diagnostic criteria; absence of weight/shape motivation; heterogeneous dimensional presentations; nutritional and psychosocial consequences.
- **Moderately supported:** associations with ASD, anxiety, ADHD, GI disease and food allergy; sensory/fear/appetite maintenance mechanisms; benefit of structured multidisciplinary care.
- **Preliminary:** specific neural-circuit and appetite-hormone abnormalities; treatment-response magnitudes; genetic loci.
- **Not established/not applicable:** monogenic causal genes, pathogenic variants, molecular biomarkers, disease-specific omics signatures, approved pharmacotherapy, validated animal model, mortality rate, or population screening program.

References

1. (fonseca2024avoidantrestrictivefood pages 1-2): Natasha K. O. Fonseca, Vitória D. Curtarelli, Juliana Bertoletti, Karla Azevedo, Tiago M. Cardinal, Júlia D. Moreira, and Luciana C. Antunes. Avoidant restrictive food intake disorder: recent advances in neurobiology and treatment. Journal of Eating Disorders, Jun 2024. URL: https://doi.org/10.1186/s40337-024-01021-z, doi:10.1186/s40337-024-01021-z. This article has 71 citations and is from a peer-reviewed journal.

2. (sanchezcerezo2024subtypesofavoidantrestrictive pages 1-2): Javier Sanchez-Cerezo, Josephine Neale, Nikita Julius, Tim Croudace, Richard M. Lynn, Lee D. Hudson, and Dasha Nicholls. Subtypes of avoidant/restrictive food intake disorder in children and adolescents: a latent class analysis. eClinicalMedicine, 68:102440, Feb 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102440, doi:10.1016/j.eclinm.2024.102440. This article has 54 citations and is from a peer-reviewed journal.

3. (fonseca2024avoidantrestrictivefood pages 13-14): Natasha K. O. Fonseca, Vitória D. Curtarelli, Juliana Bertoletti, Karla Azevedo, Tiago M. Cardinal, Júlia D. Moreira, and Luciana C. Antunes. Avoidant restrictive food intake disorder: recent advances in neurobiology and treatment. Journal of Eating Disorders, Jun 2024. URL: https://doi.org/10.1186/s40337-024-01021-z, doi:10.1186/s40337-024-01021-z. This article has 71 citations and is from a peer-reviewed journal.

4. (fonseca2024avoidantrestrictivefood pages 12-13): Natasha K. O. Fonseca, Vitória D. Curtarelli, Juliana Bertoletti, Karla Azevedo, Tiago M. Cardinal, Júlia D. Moreira, and Luciana C. Antunes. Avoidant restrictive food intake disorder: recent advances in neurobiology and treatment. Journal of Eating Disorders, Jun 2024. URL: https://doi.org/10.1186/s40337-024-01021-z, doi:10.1186/s40337-024-01021-z. This article has 71 citations and is from a peer-reviewed journal.

5. (fonseca2024avoidantrestrictivefood pages 4-6): Natasha K. O. Fonseca, Vitória D. Curtarelli, Juliana Bertoletti, Karla Azevedo, Tiago M. Cardinal, Júlia D. Moreira, and Luciana C. Antunes. Avoidant restrictive food intake disorder: recent advances in neurobiology and treatment. Journal of Eating Disorders, Jun 2024. URL: https://doi.org/10.1186/s40337-024-01021-z, doi:10.1186/s40337-024-01021-z. This article has 71 citations and is from a peer-reviewed journal.

6. (NCT06110806 chunk 2): Robyn Sysko. Family-Based Interoceptive Exposure for Avoidant Restrictive Food Intake Disorder. Icahn School of Medicine at Mount Sinai. 2023. ClinicalTrials.gov Identifier: NCT06110806

7. (fonseca2024avoidantrestrictivefood pages 2-4): Natasha K. O. Fonseca, Vitória D. Curtarelli, Juliana Bertoletti, Karla Azevedo, Tiago M. Cardinal, Júlia D. Moreira, and Luciana C. Antunes. Avoidant restrictive food intake disorder: recent advances in neurobiology and treatment. Journal of Eating Disorders, Jun 2024. URL: https://doi.org/10.1186/s40337-024-01021-z, doi:10.1186/s40337-024-01021-z. This article has 71 citations and is from a peer-reviewed journal.

8. (sanchezcerezo2024subtypesofavoidantrestrictive pages 2-3): Javier Sanchez-Cerezo, Josephine Neale, Nikita Julius, Tim Croudace, Richard M. Lynn, Lee D. Hudson, and Dasha Nicholls. Subtypes of avoidant/restrictive food intake disorder in children and adolescents: a latent class analysis. eClinicalMedicine, 68:102440, Feb 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102440, doi:10.1016/j.eclinm.2024.102440. This article has 54 citations and is from a peer-reviewed journal.

9. (nocerino2024developmentandmanagement pages 4-6): Rita Nocerino, Caterina Mercuri, Vincenzo Bosco, Vincenza Giordano, Silvio Simeone, Assunta Guillari, and Teresa Rea. Development and management of avoidant/restrictive food intake disorder and food neophobia in pediatric patients with food allergy: a comprehensive review. Nutrients, 16:3034, Sep 2024. URL: https://doi.org/10.3390/nu16173034, doi:10.3390/nu16173034. This article has 16 citations.

10. (tomaszek2025unravelingtheconnections pages 2-4): Natalia Tomaszek, Agata Dominika Urbaniak, Daniel Bałdyga, Kamila Chwesiuk, Stefan Modzelewski, and Napoleon Waszkiewicz. Unraveling the connections: eating issues, microbiome, and gastrointestinal symptoms in autism spectrum disorder. Nutrients, 17:486, Jan 2025. URL: https://doi.org/10.3390/nu17030486, doi:10.3390/nu17030486. This article has 36 citations.

11. (fonseca2024avoidantrestrictivefood pages 6-7): Natasha K. O. Fonseca, Vitória D. Curtarelli, Juliana Bertoletti, Karla Azevedo, Tiago M. Cardinal, Júlia D. Moreira, and Luciana C. Antunes. Avoidant restrictive food intake disorder: recent advances in neurobiology and treatment. Journal of Eating Disorders, Jun 2024. URL: https://doi.org/10.1186/s40337-024-01021-z, doi:10.1186/s40337-024-01021-z. This article has 71 citations and is from a peer-reviewed journal.

12. (dolan2023anticipatoryandconsummatory pages 1-2): Sarah C. Dolan, P. Evelyna Kambanis, Casey M. Stern, Kendra R. Becker, Lauren Breithaupt, Julia Gydus, Sarah Smith, Madhusmita Misra, Nadia Micali, Elizabeth A. Lawson, Kamryn T. Eddy, and Jennifer J. Thomas. Anticipatory and consummatory pleasure in avoidant/restrictive food intake disorder. Journal of Eating Disorders, Nov 2023. URL: https://doi.org/10.1186/s40337-023-00921-w, doi:10.1186/s40337-023-00921-w. This article has 13 citations and is from a peer-reviewed journal.

13. (dolan2023anticipatoryandconsummatory pages 8-9): Sarah C. Dolan, P. Evelyna Kambanis, Casey M. Stern, Kendra R. Becker, Lauren Breithaupt, Julia Gydus, Sarah Smith, Madhusmita Misra, Nadia Micali, Elizabeth A. Lawson, Kamryn T. Eddy, and Jennifer J. Thomas. Anticipatory and consummatory pleasure in avoidant/restrictive food intake disorder. Journal of Eating Disorders, Nov 2023. URL: https://doi.org/10.1186/s40337-023-00921-w, doi:10.1186/s40337-023-00921-w. This article has 13 citations and is from a peer-reviewed journal.

14. (fonseca2024avoidantrestrictivefood pages 9-10): Natasha K. O. Fonseca, Vitória D. Curtarelli, Juliana Bertoletti, Karla Azevedo, Tiago M. Cardinal, Júlia D. Moreira, and Luciana C. Antunes. Avoidant restrictive food intake disorder: recent advances in neurobiology and treatment. Journal of Eating Disorders, Jun 2024. URL: https://doi.org/10.1186/s40337-024-01021-z, doi:10.1186/s40337-024-01021-z. This article has 71 citations and is from a peer-reviewed journal.

15. (fonseca2024avoidantrestrictivefood pages 10-12): Natasha K. O. Fonseca, Vitória D. Curtarelli, Juliana Bertoletti, Karla Azevedo, Tiago M. Cardinal, Júlia D. Moreira, and Luciana C. Antunes. Avoidant restrictive food intake disorder: recent advances in neurobiology and treatment. Journal of Eating Disorders, Jun 2024. URL: https://doi.org/10.1186/s40337-024-01021-z, doi:10.1186/s40337-024-01021-z. This article has 71 citations and is from a peer-reviewed journal.

16. (sanchezcerezo2024subtypesofavoidantrestrictive pages 3-4): Javier Sanchez-Cerezo, Josephine Neale, Nikita Julius, Tim Croudace, Richard M. Lynn, Lee D. Hudson, and Dasha Nicholls. Subtypes of avoidant/restrictive food intake disorder in children and adolescents: a latent class analysis. eClinicalMedicine, 68:102440, Feb 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102440, doi:10.1016/j.eclinm.2024.102440. This article has 54 citations and is from a peer-reviewed journal.

17. (NCT05954728 chunk 1): Jennifer Thomas. Cognitive-behavioral Therapy vs. Nutrition Counseling for Avoidant/Restrictive Food Intake Disorder. Massachusetts General Hospital. 2024. ClinicalTrials.gov Identifier: NCT05954728

18. (NCT04450771 chunk 1): James Dale Lock. Confirming the Efficacy/Mechanism of Family Therapy for Children With Low Weight ARFID. Stanford University. 2020. ClinicalTrials.gov Identifier: NCT04450771

19. (NCT03778216 chunk 1): James Dale Lock. Treating Avoidant/Restrictive Food Intake Disorder (ARFID) Using Family-Based Treatment. Stanford University. 2017. ClinicalTrials.gov Identifier: NCT03778216

20. (NCT02963220 chunk 1): Jennifer Thomas. Cognitive-Behavioral Therapy for Avoidant/Restrictive Food Intake Disorder: A Treatment Development and Pilot Study. Massachusetts General Hospital. 2016. ClinicalTrials.gov Identifier: NCT02963220

21. (NCT06110806 chunk 1): Robyn Sysko. Family-Based Interoceptive Exposure for Avoidant Restrictive Food Intake Disorder. Icahn School of Medicine at Mount Sinai. 2023. ClinicalTrials.gov Identifier: NCT06110806

22. (fonseca2024avoidantrestrictivefood pages 14-15): Natasha K. O. Fonseca, Vitória D. Curtarelli, Juliana Bertoletti, Karla Azevedo, Tiago M. Cardinal, Júlia D. Moreira, and Luciana C. Antunes. Avoidant restrictive food intake disorder: recent advances in neurobiology and treatment. Journal of Eating Disorders, Jun 2024. URL: https://doi.org/10.1186/s40337-024-01021-z, doi:10.1186/s40337-024-01021-z. This article has 71 citations and is from a peer-reviewed journal.

23. (sanchezcerezo2024subtypesofavoidantrestrictive pages 9-10): Javier Sanchez-Cerezo, Josephine Neale, Nikita Julius, Tim Croudace, Richard M. Lynn, Lee D. Hudson, and Dasha Nicholls. Subtypes of avoidant/restrictive food intake disorder in children and adolescents: a latent class analysis. eClinicalMedicine, 68:102440, Feb 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102440, doi:10.1016/j.eclinm.2024.102440. This article has 54 citations and is from a peer-reviewed journal.

24. (NCT04450771 chunk 2): James Dale Lock. Confirming the Efficacy/Mechanism of Family Therapy for Children With Low Weight ARFID. Stanford University. 2020. ClinicalTrials.gov Identifier: NCT04450771

25. (che2025avoidantrestrictivefoodintake pages 13-15): Yunqiu Che, Shuhua Li, Xiaju Hu, Hongyan Hu, Can Zhang, and Chaozhu He. Avoidant/restrictive food intake disorder in adult patients with gastrointestinal diseases: a concept analysis using evolutionary approach. Risk Management and Healthcare Policy, 18:2063-2080, Jun 2025. URL: https://doi.org/10.2147/rmhp.s520802, doi:10.2147/rmhp.s520802. This article has 6 citations and is from a peer-reviewed journal.

26. (nocerino2024developmentandmanagement pages 9-11): Rita Nocerino, Caterina Mercuri, Vincenzo Bosco, Vincenza Giordano, Silvio Simeone, Assunta Guillari, and Teresa Rea. Development and management of avoidant/restrictive food intake disorder and food neophobia in pediatric patients with food allergy: a comprehensive review. Nutrients, 16:3034, Sep 2024. URL: https://doi.org/10.3390/nu16173034, doi:10.3390/nu16173034. This article has 16 citations.

27. (NCT02963220 chunk 2): Jennifer Thomas. Cognitive-Behavioral Therapy for Avoidant/Restrictive Food Intake Disorder: A Treatment Development and Pilot Study. Massachusetts General Hospital. 2016. ClinicalTrials.gov Identifier: NCT02963220

## Artifacts

- [Edison artifact artifact-00](Avoidant_Restrictive_Food_Intake_Disorder-deep-research-falcon_artifacts/artifact-00.md)