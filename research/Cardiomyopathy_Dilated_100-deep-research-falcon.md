---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T10:30:56.415575'
end_time: '2026-08-27T10:45:29.824458'
duration_seconds: 873.41
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cardiomyopathy Dilated 100
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 5
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Cardiomyopathy_Dilated_100-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiomyopathy Dilated 100
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cardiomyopathy Dilated 100** covering all of the
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
- **Disease Name:** Cardiomyopathy Dilated 100
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cardiomyopathy Dilated 100** covering all of the
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


# Cardiomyopathy, Dilated, 100 (DCM100): Research Report

## Executive summary and evidence limits

**Cardiomyopathy, dilated, 100 (DCM100)** is an exceptionally rare Mendelian form of familial dilated cardiomyopathy associated with **VEZF1** (vascular endothelial zinc finger 1). The exact disease is indexed as **MONDO:0859381**; OpenTargets links it to VEZF1 through the 2023 defining report, PMID **36657711**. It must not be confused with the distinct, autosomal-recessive **RPL3L-associated neonatal DCM**. (OpenTargets Search: Cardiomyopathy Dilated 100)

The disease-specific evidence base is currently very small. One family report establishes the association, while most mechanistic information comes from human myocardial-expression datasets, zebrafish knockdown, and cultured rodent cardiomyocytes. Accordingly, claims below are labeled **DCM100-specific**, **supportive experimental evidence**, or **generic-DCM extrapolation**. Exact pedigree details, the reported HGVS variant, patient-level phenotype, OMIM number, penetrance, and variant frequency could not be verified from the accessible full text and are therefore not invented.

The following table provides the most compact knowledge-base representation.

| Field | Finding | Evidence scope | Suggested ontology terms | Key citation |
|---|---|---|---|---|
| Exact disease name / synonyms | **Cardiomyopathy, dilated, 100**; shorthand **DCM100**. Distinct from generic dilated cardiomyopathy and distinct from recessive **RPL3L**-associated neonatal DCM. | DCM100-specific for exact name; comparison to RPL3L based on separate literature mapping. | MONDO:0859381 | (OpenTargets Search: Cardiomyopathy Dilated 100) |
| MONDO ID | **MONDO:0859381** for “cardiomyopathy, dilated, 100”. | DCM100-specific | MONDO:0859381 | (OpenTargets Search: Cardiomyopathy Dilated 100) |
| Causal gene | **VEZF1** (vascular endothelial zinc finger 1). OpenTargets maps VEZF1 as the associated target for this disease with literature support from PMID **36657711**. | DCM100-specific | Gene symbol: VEZF1 | (OpenTargets Search: Cardiomyopathy Dilated 100) |
| Protein role | VEZF1 is a **zinc-finger transcription factor** implicated in regulation of cardiac structure/function and angiogenic programs; in cardiomyocytes it regulates expression of contraction/cardiomyopathy-related genes including **MYH7** and interacts with **TEAD1**. | Gene/mechanism evidence relevant to DCM100; mostly experimental, not all from human DCM100 patients. | GO:0006355 regulation of DNA-templated transcription; GO:0060048 cardiac muscle contraction; GO:0001525 angiogenesis | (paavola2020vezf1regulatescardiac pages 1-2, paavola2020vezf1regulatescardiac pages 5-7, paavola2020vezf1regulatescardiac pages 7-8, paavola2020vezf1regulatescardiac pages 11-12) |
| Inheritance | **Autosomal dominant** pattern is most likely for DCM100 because the defining publication is titled **“VEZF1 loss-of-function mutation underlying familial dilated cardiomyopathy”** and describes a familial DCM gene-disease relationship; exact pedigree details were not recoverable here. | DCM100-specific but partially inferred from defining publication metadata | HP:0000006 Autosomal dominant inheritance | (OpenTargets Search: Cardiomyopathy Dilated 100) |
| Defining human evidence | Defining report: **Shi HY, Xie MS, Guo YH, et al. “VEZF1 loss-of-function mutation underlying familial dilated cardiomyopathy.” European Journal of Medical Genetics. 2023; DOI: 10.1016/j.ejmg.2023.104705; PMID: 36657711.** Exact variant HGVS, family size, and frequencies were not available in recovered context and should not be invented. | DCM100-specific | NCIT: C16612 Genetic Finding | (OpenTargets Search: Cardiomyopathy Dilated 100) |
| Core phenotype | Dilated cardiomyopathy phenotype is expected: **left ventricular dilatation and systolic dysfunction**, progressing to heart failure/arrhythmic risk as in familial DCM. Direct DCM100-specific phenotypic granularity beyond this was not recoverable in current context. | Mixed: DCM100-specific at disease label; generic DCM for detailed phenotype framing | HP:0001644 Dilated cardiomyopathy; HP:0001670 Abnormal cardiac ventricle morphology; HP:0001638 Cardiomyopathy; HP:0005162 Reduced ejection fraction | (OpenTargets Search: Cardiomyopathy Dilated 100, mcnally2017dilatedcardiomyopathygenetic pages 2-3) |
| Mechanistic chain | Proposed chain: **VEZF1 loss-of-function → altered transcriptional control in cardiomyocytes → reduced MYH7/β-MHC and dysregulation of other contraction-related genes → impaired compensatory growth and reduced contractile reserve → ventricular dysfunction / DCM phenotype**. Vezf1 also binds **TEAD1** and affects an **MCAT** site in the Myh7 promoter. | Mechanism is experimental and supportive, not direct proof from all DCM100 patients | GO:0006357 regulation of transcription by RNA polymerase II; GO:0060048 cardiac muscle contraction; GO:0003015 heart process | (paavola2020vezf1regulatescardiac pages 5-7, paavola2020vezf1regulatescardiac pages 7-8, paavola2020vezf1regulatescardiac pages 8-9, paavola2020vezf1regulatescardiac pages 11-12) |
| Primary anatomy / cell type / subcellular localization | Primary organ/tissue: **heart / myocardium**, especially **left ventricle**. Key cell types: **cardiomyocytes** and likely **endothelial cells**. VEZF1 is described as a **nuclear protein**. | Mostly mechanism/model evidence; anatomy aligns with DCM100 disease concept | UBERON:0000948 heart; UBERON:0002084 myocardium; UBERON:0002082 cardiac ventricle; UBERON:0002080 left ventricle; CL:0002494 cardiomyocyte; CL:0000115 endothelial cell; GO:0005634 nucleus | (paavola2020vezf1regulatescardiac pages 1-2, paavola2020vezf1regulatescardiac pages 4-5, paavola2020vezf1regulatescardiac pages 9-11) |
| Diagnostic approach | No DCM100-specific diagnostic guideline was recovered. Practical approach is **generic hereditary DCM workup** plus molecular confirmation: clinical exam/family history, **ECG**, **echocardiography**, **CMR**, natriuretic peptides/heart-failure biomarkers, and **multigene cardiomyopathy testing including VEZF1** if available. Generic DCM criteria cited include **LVEF <45% or FS <25%** with increased LV size. | Mostly extrapolated from generic DCM | NCIT: C38043 Electrocardiography; NCIT: C16576 Echocardiography; NCIT: C16809 Magnetic Resonance Imaging; NCIT: C47809 Genetic Testing | (mcnally2017dilatedcardiomyopathygenetic pages 2-3) |
| Treatment status | **No DCM100-specific targeted therapy** was identified. Management should follow **guideline-directed therapy for dilated cardiomyopathy/heart failure**, with consideration of arrhythmia prevention, ICD/CRT when indicated, advanced HF therapies, and transplantation in end-stage disease. | Extrapolated from generic DCM; not DCM100-specific | NCIT: C101526 Heart Failure Management; NCIT: C173520 Implantable Cardioverter Defibrillator Placement; NCIT: C80450 Cardiac Resynchronization Therapy; NCIT: C15202 Heart Transplantation | (mcnally2017dilatedcardiomyopathygenetic pages 2-3) |
| Epidemiology | **Ultra-rare / not established** for DCM100 specifically. No prevalence, incidence, sex ratio, or carrier frequency for DCM100 were recoverable. Familial DCM more broadly accounts for roughly **30–50%** of DCM, with identifiable genetic causes in about **40% of familial cases** in the cited review. | DCM100-specific data unavailable; generic DCM/familial DCM figures extrapolated | NCIT: C25190 Prevalence | (mcnally2017dilatedcardiomyopathygenetic pages 2-3) |
| Model systems | **Zebrafish Vezf1 knockdown** reduces cardiac growth and blunts β-adrenergic stress-induced contractile response; **rat cardiomyocytes** with Vezf1 silencing show reduced shortening, reduced **β-MHC/MYH7**, increased skeletal α-actin, and TEAD1 interaction; expression is decreased in diseased human myocardium and post-MI mouse hearts. | Mechanistic/model evidence supportive of DCM100 biology | CL:0002494 cardiomyocyte; GO:0060048 cardiac muscle contraction; GO:0001525 angiogenesis | (paavola2020vezf1regulatescardiac pages 1-2, paavola2020vezf1regulatescardiac pages 4-5, paavola2020vezf1regulatescardiac pages 5-7, paavola2020vezf1regulatescardiac pages 7-8, paavola2020vezf1regulatescardiac pages 8-9, paavola2020vezf1regulatescardiac pages 9-11, paavola2020vezf1regulatescardiac pages 11-12) |


*Table: This table summarizes the highest-confidence facts currently recoverable for Cardiomyopathy, Dilated, 100, clearly separating disease-specific findings from broader DCM extrapolations. It is designed for direct knowledge-base ingestion with ontology suggestions and context-ID citations.*

## 1. Disease information

### Definition

DCM is a myocardial disorder characterized by ventricular—usually left-ventricular—dilatation and systolic dysfunction not adequately explained by abnormal loading conditions or coronary disease. Historical research criteria include fractional shortening **<25%** or left-ventricular ejection fraction **<45%**, together with LV end-diastolic diameter **>117%** of the value predicted for age and body-surface area. DCM100 denotes the VEZF1-associated familial subtype, rather than all DCM. (mcnally2017dilatedcardiomyopathygenetic pages 2-3)

### Identifiers and synonyms

- **Preferred name:** Cardiomyopathy, dilated, 100
- **Synonyms:** Dilated cardiomyopathy 100; DCM100; VEZF1-related dilated cardiomyopathy
- **MONDO:** **MONDO:0859381**
- **Causal gene:** **VEZF1**, Ensembl **ENSG00000136451**
- **Defining publication:** Shi HY et al., *VEZF1 loss-of-function mutation underlying familial dilated cardiomyopathy*, *European Journal of Medical Genetics*, 2023; DOI: https://doi.org/10.1016/j.ejmg.2023.104705; PMID: https://pubmed.ncbi.nlm.nih.gov/36657711/ (OpenTargets Search: Cardiomyopathy Dilated 100)
- **OMIM/Orphanet:** an exact disease-level number was not independently recoverable from the available evidence.
- **ICD-10:** DCM generally maps to **I42.0**, but this is not specific to DCM100.
- **ICD-11/MeSH:** use the broader dilated-cardiomyopathy concepts; no subtype-specific code was verified.

The evidence is an **aggregated disease-level synthesis** based on a published family, experimental studies, and databases—not individual EHR data.

## 2. Etiology and risk factors

### Causal factor

The defining human report attributes familial DCM to a **VEZF1 loss-of-function mutation**. The familial title and disease classification support autosomal-dominant transmission, but exact segregation counts and the variant’s HGVS description require confirmation from the original article before clinical use. OpenTargets records one disease–target evidence item tied to PMID 36657711. (OpenTargets Search: Cardiomyopathy Dilated 100)

### Genetic and environmental risk

The principal established DCM100 risk is carriage of the familial VEZF1 variant. No independently replicated susceptibility loci, modifier genes, founder allele, carrier frequency, germline mosaicism, anticipation, or population-specific enrichment have been reported for this subtype in the retrieved evidence.

No DCM100-specific environmental risk or protective factor has been established. For DCM generally, myocardial stressors—viral myocarditis, alcohol, cardiotoxic drugs, pregnancy, endocrine/metabolic disease, sustained tachyarrhythmia, and hemodynamic overload—may precipitate or worsen ventricular dysfunction. Applying these as VEZF1 gene–environment interactions is biologically plausible but **unproven**.

Experimental data provide one candidate interaction: Vezf1-deficient zebrafish had a disproportionately impaired response to **β-adrenergic stress**, suggesting that reduced VEZF1 limits cardiac contractile reserve under increased demand. This is a model-organism observation, not demonstrated penetrance modification in human carriers. (paavola2020vezf1regulatescardiac pages 2-3, paavola2020vezf1regulatescardiac pages 8-9)

## 3. Phenotypes

The confidently assignable phenotype is dilated cardiomyopathy with ventricular systolic dysfunction. The accessible evidence does not support reliable DCM100-specific frequencies, onset ages, sex differences, or extracardiac manifestations.

Suggested terms include:

- **Dilated cardiomyopathy — HP:0001644**: defining structural/functional phenotype.
- **Reduced left-ventricular ejection fraction — HP:0012664** or the current HPO equivalent used by the target database.
- **Left-ventricular dilatation — HP:0001711**.
- **Congestive heart failure — HP:0001635**: possible advanced manifestation.
- **Cardiomegaly — HP:0001640**, **dyspnea — HP:0002094**, **exercise intolerance — HP:0003546**, **fatigue — HP:0012378**, **peripheral edema — HP:0012398**, and **cardiac arrhythmia — HP:0011675**: clinically plausible generic DCM manifestations, but not confirmed as frequencies in DCM100.

DCM can impair exercise capacity, schooling or employment, sleep, independence, and psychosocial well-being. No DCM100-specific EQ-5D, SF-36, KCCQ, or pediatric quality-of-life data exist in the retrieved literature.

## 4. Genetic and molecular information

### Gene and protein

**VEZF1** encodes a highly conserved nuclear C2H2 zinc-finger transcription factor with six zinc-finger motifs and a proline-rich transactivation domain. It is expressed in endothelial cells and adult cardiomyocytes and participates in angiogenesis, cardiac growth, and transcriptional control of contractile genes. (paavola2020vezf1regulatescardiac pages 1-2, paavola2020vezf1regulatescardiac pages 11-12)

### Variant evidence

The defining publication reports a loss-of-function mutation segregating with familial DCM. However, the following could not be independently recovered and should remain null fields pending inspection of the original article:

- HGVS genomic/cDNA/protein nomenclature;
- missense, nonsense, frameshift, or splice class;
- ClinVar classification and accession;
- gnomAD/TOPMed frequency;
- ACMG/AMP criteria;
- number of carriers and affected relatives;
- functional effect of the specific human allele.

The presumed origin is **germline**, given familial Mendelian transmission. There is no evidence that DCM100 is somatic. No validated modifier gene, pathogenic copy-number change, methylation signature, or disease-specific chromosomal abnormality is established.

## 5. Environmental information

No toxin, infection, radiation, occupational exposure, diet, smoking behavior, alcohol exposure, or pathogen has been shown to cause **DCM100**. These should be captured only as general DCM differential etiologies or possible secondary stressors—not as causes of the VEZF1 subtype.

Reasonable risk-reduction practice is avoidance of cardiotoxic exposures, recreational stimulants, heavy alcohol consumption, and unsupervised extreme exercise after cardiomyopathy is recognized. This is generic cardiomyopathy care rather than evidence for primary prevention of VEZF1 disease.

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. **Upstream genetic event:** reduced VEZF1 function.
2. **Transcriptional dysregulation:** altered VEZF1–TEAD1 regulation of muscle genes, including **MYH7/β-myosin heavy chain**, ATP1A2, TCAP, ACTA1, MYH11, and troponin genes.
3. **Contractile-unit imbalance:** reduced MYH7/β-MHC with increased skeletal α-actin lowers the myosin/actin ratio.
4. **Cellular phenotype:** reduced cardiomyocyte growth and shortening with impaired compensatory response to adrenergic/hemodynamic stress.
5. **Organ phenotype:** reduced contractile reserve, ventricular systolic dysfunction, remodeling, and DCM/heart failure. (paavola2020vezf1regulatescardiac pages 5-7, paavola2020vezf1regulatescardiac pages 7-8, paavola2020vezf1regulatescardiac pages 8-9, paavola2020vezf1regulatescardiac pages 9-11)

In neonatal rat cardiomyocytes, VEZF1 silencing significantly altered **1,144 transcripts** at FDR <0.05; 28 were increased and 53 decreased by more than twofold. Enrichment implicated muscle contraction and DCM pathways. Zebrafish Vezf1 knockdown reduced ventricular-myosin-heavy-chain expression by **92%** and impaired the stress-induced increase in ejection performance without changing calcium-transient kinetics. These findings argue for altered contractile-gene transcription rather than a primary calcium-handling defect. (paavola2020vezf1regulatescardiac pages 5-7, paavola2020vezf1regulatescardiac pages 7-8, paavola2020vezf1regulatescardiac pages 8-9)

Promoter experiments showed that VEZF1 knockdown reduced β-MHC reporter activity by **52–80%**. VEZF1 co-immunoprecipitated with TEAD1, and an MCAT element in the MYH7 promoter partly mediated the response. (paavola2020vezf1regulatescardiac pages 7-8, paavola2020vezf1regulatescardiac pages 9-11, paavola2020vezf1regulatescardiac pages 11-12)

### Vascular and epigenetic dimensions

VEZF1 also regulates vasculogenesis and angiogenesis. Zebrafish knockdown altered axial-vessel geometry and stress-induced intersegmental-vessel formation. Endothelial signaling may therefore contribute, but cardiomyocyte-autonomous effects are supported by isolated-cell experiments. (paavola2020vezf1regulatescardiac pages 4-5, paavola2020vezf1regulatescardiac pages 11-12)

VEZF1 has previously been implicated in regulation of **DNMT3B** and DNA methylation, but no DCM100-specific epigenomic signature has been demonstrated. Likewise, no disease-specific proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or CRISPR-screen dataset was found.

### Suggested ontology annotations

- **GO biological process:** regulation of DNA-templated transcription; cardiac muscle contraction; regulation of heart contraction; cardiac muscle-cell development; angiogenesis; response to adrenergic stimulus.
- **GO cellular component:** nucleus (**GO:0005634**), transcription-regulator complex, sarcomere (**GO:0030017**) downstream.
- **Cell Ontology:** cardiomyocyte (**CL:0002494**), ventricular cardiomyocyte, endothelial cell (**CL:0000115**), cardiac fibroblast as a downstream remodeling cell.

## 7. Anatomical structures affected

The primary organ is the **heart (UBERON:0000948)**, particularly **myocardium (UBERON:0002084)** and **left ventricle (UBERON:0002080)**. Cardiomyocytes are the principal effector cells; cardiac endothelial cells may contribute through vascular and paracrine regulation. VEZF1 acts in the nucleus, while downstream damage involves sarcomeres and the contractile apparatus. (paavola2020vezf1regulatescardiac pages 1-2, paavola2020vezf1regulatescardiac pages 9-11, paavola2020vezf1regulatescardiac pages 11-12)

Secondary involvement in advanced DCM can include lungs, liver, kidneys, and systemic venous tissues through low cardiac output and congestion. These are complications of heart failure, not primary VEZF1 target organs. Lateralization is not applicable.

## 8. Temporal development

The DCM100-specific onset distribution is unknown. Generic inherited DCM may be clinically silent before progressive LV enlargement, reduced systolic function, symptomatic heart failure, arrhythmia, or sudden death. In genetic DCM, ventricular enlargement may precede measurable functional decline, and strain abnormalities may precede dimensional changes in relatives. (mcnally2017dilatedcardiomyopathygenetic pages 2-3)

A practical course model is:

1. genotype-positive/phenotype-negative;
2. subtle strain or ECG abnormality;
3. LV enlargement with mild systolic dysfunction;
4. symptomatic DCM/HFrEF;
5. advanced heart failure, malignant arrhythmia, mechanical support, or transplantation.

Spontaneous or treatment-associated reverse remodeling occurs in generic DCM, but no remission rate or critical intervention window is known for DCM100.

## 9. Inheritance and population

The available human evidence supports **familial autosomal-dominant inheritance**. Each child of a heterozygous carrier would therefore have a theoretical **50% transmission probability**, although disease penetrance may be incomplete or age-dependent. Actual DCM100 penetrance and expressivity have not been quantified.

No subtype-specific prevalence, incidence, carrier frequency, founder effect, ethnic enrichment, geographic distribution, sex ratio, or age distribution is known. DCM100 should presently be considered **ultra-rare**. In DCM overall, familial disease is estimated in approximately **30–50%** of cases, and an identifiable genetic cause is found in roughly **40%** of familial cases; these values must not be assigned to VEZF1 specifically. (mcnally2017dilatedcardiomyopathygenetic pages 2-3)

## 10. Diagnostics

### Clinical evaluation

The phenotype should be established independently of genotype through:

- history, three-generation pedigree, physical examination, and exclusion of ischemic/loading causes;
- **12-lead ECG** and ambulatory monitoring for conduction disease and atrial/ventricular arrhythmia;
- **transthoracic echocardiography** for LV dimensions, ejection fraction, fractional shortening, valve regurgitation, and strain;
- **cardiac MRI** for chamber volumes, function, edema, and fibrosis/late gadolinium enhancement;
- BNP or NT-proBNP and troponin as severity/injury markers;
- laboratory exclusion of thyroid, metabolic, infectious, inflammatory, toxic, and nutritional causes where clinically indicated. CMR fibrosis has prognostic value in broader DCM. (mcnally2017dilatedcardiomyopathygenetic pages 2-3)

Endomyocardial biopsy is not routine for genetic DCM but may be appropriate when myocarditis, infiltrative disease, storage disease, or a treatment-changing inflammatory diagnosis is suspected.

### Genetic testing

A contemporary strategy is a validated cardiomyopathy panel with deletion/duplication analysis, ensuring **VEZF1** coverage if the laboratory recognizes the gene–disease relationship. Exome or genome sequencing is appropriate when panel testing is negative, especially in multiplex families; RNA studies may clarify splice variants. A VUS must not be used for predictive testing or irreversible management decisions.

Once a pathogenic familial variant is confirmed, offer targeted cascade testing to first-degree relatives. Genotype-positive relatives require longitudinal ECG and imaging surveillance. If the causal variant remains uncertain, first-degree relatives should still receive phenotype screening because familial DCM may be clinically silent. (mcnally2017dilatedcardiomyopathygenetic pages 2-3)

CMA, karyotyping, FISH, mitochondrial-genome testing, and repeat-expansion testing are not first-line for isolated DCM100 unless syndromic findings suggest another diagnosis.

### Differential diagnosis

Exclude ischemic cardiomyopathy, myocarditis, tachycardia-induced cardiomyopathy, toxic/alcohol-related disease, peripartum cardiomyopathy, endocrine/nutritional disease, mitochondrial/metabolic cardiomyopathy, neuromuscular disease, congenital heart disease, and other genetic DCM genes such as TTN, LMNA, FLNC, DSP, RBM20, BAG3, and PLN.

## 11. Outcome and prognosis

No DCM100-specific survival, transplant-free survival, sudden-death rate, recovery rate, or validated prognostic biomarker is available. Prognosis should therefore be based on the observed phenotype rather than the VEZF1 label alone.

Generic adverse markers include severe LV dysfunction or dilatation, persistent symptoms, ventricular arrhythmia, conduction disease, syncope, fibrosis on CMR, severe mitral regurgitation, rising natriuretic peptides, and failure to reverse remodel. DCM can lead to chronic disability, recurrent hospitalization, thromboembolism, progressive pump failure, ventricular arrhythmia, sudden cardiac death, ventricular-assist-device implantation, or transplantation. Disease-specific quality-of-life statistics are unavailable.

## 12. Treatment

There is **no approved VEZF1-targeted therapy**, gene therapy, RNA therapy, or DCM100-specific clinical trial. Treatment is phenotype-directed and extrapolated from DCM/HFrEF practice:

- neurohormonal heart-failure therapy appropriate to age and physiology: ACE inhibitor/ARB or ARNI, evidence-based β-blocker, mineralocorticoid-receptor antagonist, and an SGLT2 inhibitor in eligible patients;
- loop diuretic for congestion;
- anticoagulation only for standard indications such as atrial fibrillation, intracardiac thrombus, or embolism—not solely for the genotype;
- antiarrhythmic therapy, catheter ablation, or pacing where indicated;
- ICD for guideline-defined sudden-death prevention and CRT for qualifying ventricular dysfunction/electrical dyssynchrony;
- temporary or durable mechanical circulatory support and heart transplantation for refractory advanced failure.

Pediatric prescribing requires specialist dosing and recognition that much evidence is extrapolated from adults. No pharmacogenomic interaction with VEZF1 is known.

Suggested NCIt concepts include heart-failure therapy, beta-adrenergic blocking agent therapy, angiotensin-receptor/neprilysin inhibitor therapy, diuretic therapy, implantable cardioverter-defibrillator placement, cardiac resynchronization therapy, ventricular-assist-device therapy, and heart transplantation.

Experimental cell therapies investigated in generic nonischemic DCM cannot be considered DCM100 treatment. ClinicalTrials.gov searches identified broad pediatric/DCM studies, but none selected patients by VEZF1 genotype.

## 13. Prevention

### Primary prevention

The inherited variant itself cannot currently be prevented after conception. Avoidance of cardiotoxins and treatment of hypertension, arrhythmia, infection, endocrine disease, and other myocardial stressors are prudent but unproven as VEZF1-specific preventive measures.

### Secondary prevention

The most actionable intervention is **family identification and surveillance**: genetic counseling, cascade testing for a confirmed pathogenic variant, periodic ECG/ambulatory monitoring and echocardiography or CMR, and early treatment of ventricular dysfunction. Reproductive options may include prenatal diagnosis or preimplantation genetic testing once a clearly pathogenic familial variant is established.

### Tertiary prevention

Guideline-directed heart-failure therapy, rhythm surveillance, vaccination according to routine schedules, exercise counseling, prompt management of decompensation, and devices when indicated aim to prevent hospitalization, embolism, sudden death, and end-stage failure. There is no DCM100-specific immunization or chemoprophylaxis.

## 14. Other species and natural disease

No naturally occurring VEZF1-related DCM100 has been established in companion animals, livestock, or wildlife, and no breed-specific VBO annotation is justified. The disorder is not infectious and has no zoonotic or cross-species transmission.

Relevant experimental taxa are **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)**, **Rattus norvegicus (10116)**, and **Danio rerio (7955)**. VEZF1 function is evolutionarily conserved across vertebrates. (paavola2020vezf1regulatescardiac pages 1-2)

## 15. Model organisms and advanced research

### Zebrafish

Morpholino-mediated Vezf1 depletion produced reduced cardiomyocyte growth, pericardial enlargement, vascular abnormalities, and impaired β-adrenergic augmentation of contractility. Co-injection of Vezf1 mRNA rescued vascular phenotypes, supporting knockdown specificity. Calcium-transient kinetics were preserved, while ventricular MHC expression fell markedly. Limitations include transient morpholino knockdown, embryonic physiology, and absence of the exact human allele. (paavola2020vezf1regulatescardiac pages 4-5, paavola2020vezf1regulatescardiac pages 5-7, paavola2020vezf1regulatescardiac pages 8-9)

### Rodent cardiomyocytes and mice

VEZF1 knockdown in neonatal and adult rat ventricular cardiomyocytes reduced cell growth, shortening, MYH7/β-MHC expression, and β-MHC promoter activity; it increased skeletal α-actin and altered the contractile transcriptome. These experiments support a cardiomyocyte-autonomous transcriptional mechanism. (paavola2020vezf1regulatescardiac pages 5-7, paavola2020vezf1regulatescardiac pages 7-8, paavola2020vezf1regulatescardiac pages 9-11)

Vezf1-null mice are embryonically lethal with major vascular defects, making a conventional null model unsuitable for adult DCM natural history. A conditional cardiomyocyte-specific knock-in of the human DCM100 variant would be more informative. (paavola2020vezf1regulatescardiac pages 2-3)

### Human tissues

Across two human heart-failure expression datasets, VEZF1 expression was approximately **20–25% lower** in idiopathic cardiomyopathy and **16–25% lower** in ischemic cardiomyopathy than controls. In a separate autopsy series, expression was **43% lower** in ischemic-heart-disease sudden-death hearts. These observations show association with diseased myocardium but do not prove that acquired reduction causes DCM100. (paavola2020vezf1regulatescardiac pages 4-5)

### Priority research needs

1. Independent VEZF1 families and rigorous ClinGen-level replication.
2. Public deposition and expert classification of the defining variant.
3. Longitudinal penetrance and genotype–phenotype studies.
4. Patient-derived iPSC cardiomyocytes and isogenic correction.
5. Variant-specific knock-in mouse or zebrafish models.
6. Single-cell and spatial transcriptomics separating cardiomyocyte from endothelial effects.
7. ChIP-seq/CUT&RUN mapping of VEZF1–TEAD1 targets.
8. Rescue studies testing whether restoration of VEZF1 or MYH7 normalizes contractility.

## Key abstract quotations and source appraisal

- The 2020 mechanistic paper states: **“We demonstrate a role for Vezf1 in regulation of compensatory cardiac growth and cardiomyocyte contractile function.”** This is supported by zebrafish and cultured-cell experiments, not by a DCM100 clinical cohort. (paavola2020vezf1regulatescardiac pages 1-2)
- Its principal mechanistic finding was that VEZF1 knockdown regulates contraction/DCM-related genes and identifies **MYH7/β-MHC as a key target**, with TEAD1 as a binding partner. (paavola2020vezf1regulatescardiac pages 1-2, paavola2020vezf1regulatescardiac pages 7-8)
- The defining 2023 human paper is titled **“VEZF1 loss-of-function mutation underlying familial dilated cardiomyopathy.”** Its PMID and disease–gene linkage are verified, but exact abstract wording and patient-level data were not recoverable in the accessible corpus. (OpenTargets Search: Cardiomyopathy Dilated 100)

## Overall interpretation

DCM100 is best regarded as a **provisional-to-emerging, ultra-rare VEZF1-associated autosomal-dominant DCM subtype** supported by one familial report and biologically coherent experimental evidence. VEZF1 connects endothelial biology with cardiomyocyte transcription, particularly the TEAD1–MYH7 contractile program. Nevertheless, the present evidence does not justify subtype-specific estimates of penetrance, prognosis, variant frequency, or treatment response. Clinical care should therefore combine confirmation of the familial molecular finding with standard hereditary-DCM phenotyping, cascade screening, longitudinal surveillance, and guideline-directed heart-failure and arrhythmia management. (OpenTargets Search: Cardiomyopathy Dilated 100, paavola2020vezf1regulatescardiac pages 1-2, mcnally2017dilatedcardiomyopathygenetic pages 2-3)

References

1. (OpenTargets Search: Cardiomyopathy Dilated 100): Open Targets Query (Cardiomyopathy Dilated 100, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (paavola2020vezf1regulatescardiac pages 1-2): Jere Paavola, Tarja Alakoski, Johanna Ulvila, Teemu Kilpiö, Juuso Sirén, Sanni Perttunen, Suneeta Narumanchi, Hong Wang, Ruizhu Lin, Katja Porvari, Juhani Junttila, Heikki Huikuri, Katariina Immonen, Päivi Lakkisto, Johanna Magga, Ilkka Tikkanen, and Risto Kerkelä. Vezf1 regulates cardiac structure and contractile function. EBioMedicine, 51:102608, Jan 2020. URL: https://doi.org/10.1016/j.ebiom.2019.102608, doi:10.1016/j.ebiom.2019.102608. This article has 22 citations and is from a peer-reviewed journal.

3. (paavola2020vezf1regulatescardiac pages 5-7): Jere Paavola, Tarja Alakoski, Johanna Ulvila, Teemu Kilpiö, Juuso Sirén, Sanni Perttunen, Suneeta Narumanchi, Hong Wang, Ruizhu Lin, Katja Porvari, Juhani Junttila, Heikki Huikuri, Katariina Immonen, Päivi Lakkisto, Johanna Magga, Ilkka Tikkanen, and Risto Kerkelä. Vezf1 regulates cardiac structure and contractile function. EBioMedicine, 51:102608, Jan 2020. URL: https://doi.org/10.1016/j.ebiom.2019.102608, doi:10.1016/j.ebiom.2019.102608. This article has 22 citations and is from a peer-reviewed journal.

4. (paavola2020vezf1regulatescardiac pages 7-8): Jere Paavola, Tarja Alakoski, Johanna Ulvila, Teemu Kilpiö, Juuso Sirén, Sanni Perttunen, Suneeta Narumanchi, Hong Wang, Ruizhu Lin, Katja Porvari, Juhani Junttila, Heikki Huikuri, Katariina Immonen, Päivi Lakkisto, Johanna Magga, Ilkka Tikkanen, and Risto Kerkelä. Vezf1 regulates cardiac structure and contractile function. EBioMedicine, 51:102608, Jan 2020. URL: https://doi.org/10.1016/j.ebiom.2019.102608, doi:10.1016/j.ebiom.2019.102608. This article has 22 citations and is from a peer-reviewed journal.

5. (paavola2020vezf1regulatescardiac pages 11-12): Jere Paavola, Tarja Alakoski, Johanna Ulvila, Teemu Kilpiö, Juuso Sirén, Sanni Perttunen, Suneeta Narumanchi, Hong Wang, Ruizhu Lin, Katja Porvari, Juhani Junttila, Heikki Huikuri, Katariina Immonen, Päivi Lakkisto, Johanna Magga, Ilkka Tikkanen, and Risto Kerkelä. Vezf1 regulates cardiac structure and contractile function. EBioMedicine, 51:102608, Jan 2020. URL: https://doi.org/10.1016/j.ebiom.2019.102608, doi:10.1016/j.ebiom.2019.102608. This article has 22 citations and is from a peer-reviewed journal.

6. (mcnally2017dilatedcardiomyopathygenetic pages 2-3): Elizabeth M. McNally and Luisa Mestroni. Dilated cardiomyopathy: genetic determinants and mechanisms. Circulation Research, 121:731–748, Sep 2017. URL: https://doi.org/10.1161/circresaha.116.309396, doi:10.1161/circresaha.116.309396. This article has 995 citations and is from a highest quality peer-reviewed journal.

7. (paavola2020vezf1regulatescardiac pages 8-9): Jere Paavola, Tarja Alakoski, Johanna Ulvila, Teemu Kilpiö, Juuso Sirén, Sanni Perttunen, Suneeta Narumanchi, Hong Wang, Ruizhu Lin, Katja Porvari, Juhani Junttila, Heikki Huikuri, Katariina Immonen, Päivi Lakkisto, Johanna Magga, Ilkka Tikkanen, and Risto Kerkelä. Vezf1 regulates cardiac structure and contractile function. EBioMedicine, 51:102608, Jan 2020. URL: https://doi.org/10.1016/j.ebiom.2019.102608, doi:10.1016/j.ebiom.2019.102608. This article has 22 citations and is from a peer-reviewed journal.

8. (paavola2020vezf1regulatescardiac pages 4-5): Jere Paavola, Tarja Alakoski, Johanna Ulvila, Teemu Kilpiö, Juuso Sirén, Sanni Perttunen, Suneeta Narumanchi, Hong Wang, Ruizhu Lin, Katja Porvari, Juhani Junttila, Heikki Huikuri, Katariina Immonen, Päivi Lakkisto, Johanna Magga, Ilkka Tikkanen, and Risto Kerkelä. Vezf1 regulates cardiac structure and contractile function. EBioMedicine, 51:102608, Jan 2020. URL: https://doi.org/10.1016/j.ebiom.2019.102608, doi:10.1016/j.ebiom.2019.102608. This article has 22 citations and is from a peer-reviewed journal.

9. (paavola2020vezf1regulatescardiac pages 9-11): Jere Paavola, Tarja Alakoski, Johanna Ulvila, Teemu Kilpiö, Juuso Sirén, Sanni Perttunen, Suneeta Narumanchi, Hong Wang, Ruizhu Lin, Katja Porvari, Juhani Junttila, Heikki Huikuri, Katariina Immonen, Päivi Lakkisto, Johanna Magga, Ilkka Tikkanen, and Risto Kerkelä. Vezf1 regulates cardiac structure and contractile function. EBioMedicine, 51:102608, Jan 2020. URL: https://doi.org/10.1016/j.ebiom.2019.102608, doi:10.1016/j.ebiom.2019.102608. This article has 22 citations and is from a peer-reviewed journal.

10. (paavola2020vezf1regulatescardiac pages 2-3): Jere Paavola, Tarja Alakoski, Johanna Ulvila, Teemu Kilpiö, Juuso Sirén, Sanni Perttunen, Suneeta Narumanchi, Hong Wang, Ruizhu Lin, Katja Porvari, Juhani Junttila, Heikki Huikuri, Katariina Immonen, Päivi Lakkisto, Johanna Magga, Ilkka Tikkanen, and Risto Kerkelä. Vezf1 regulates cardiac structure and contractile function. EBioMedicine, 51:102608, Jan 2020. URL: https://doi.org/10.1016/j.ebiom.2019.102608, doi:10.1016/j.ebiom.2019.102608. This article has 22 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Cardiomyopathy_Dilated_100-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.