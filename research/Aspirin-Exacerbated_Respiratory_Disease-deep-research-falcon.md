---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T16:19:37.965519'
end_time: '2026-08-27T16:27:40.312723'
duration_seconds: 482.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aspirin-Exacerbated Respiratory Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 9
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Aspirin-Exacerbated_Respiratory_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aspirin-Exacerbated Respiratory Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Aspirin-Exacerbated Respiratory Disease** covering all of the
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
- **Disease Name:** Aspirin-Exacerbated Respiratory Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Aspirin-Exacerbated Respiratory Disease** covering all of the
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


# Aspirin-Exacerbated Respiratory Disease (AERD): Disease-Characteristics Report

## Executive summary

Aspirin-exacerbated respiratory disease (AERD), increasingly termed **NSAID-exacerbated respiratory disease (N-ERD)**, is a chronic, usually adult-onset inflammatory disorder of the unified upper and lower airway. It comprises asthma, chronic rhinosinusitis with nasal polyps (CRSwNP), and reproducible respiratory reactions to aspirin or other strong cyclooxygenase-1 (COX-1) inhibitors. It is a **complex, multifactorial disease—not an IgE allergy to aspirin and not a Mendelian disorder**. Current evidence supports dysregulated arachidonic-acid metabolism superimposed on epithelial and type-2 inflammation, with deficient protective prostaglandin-E signaling and excessive cysteinyl leukotriene and prostaglandin-D2 activity. Mast cells, eosinophils, platelets, basophils, ILC2s, plasma cells, macrophages, and airway epithelial cells form the principal cellular network. (badrani2021cellularinteractionsin pages 1-3, li2019aspirinexacerbatedrespiratory pages 1-3, sehanobish2022newconceptsfor pages 1-3)

AERD affects approximately **0.3–0.9% of the general US population, about 7% of adults with asthma, approximately 15% with severe asthma, and 8–26% of CRSwNP populations**, depending on ascertainment. Diagnosis is clinical when the triad and repeated unequivocal reactions are present; otherwise, supervised aspirin provocation is the reference standard. No blood, urine, genomic, or omics test can currently replace challenge testing. Management is multidisciplinary and combines guideline-based asthma therapy, topical sinonasal corticosteroids and saline irrigation, leukotriene-pathway therapy, endoscopic sinus surgery when indicated, aspirin desensitization followed by maintenance aspirin in selected patients, and phenotype-directed biologics. (li2019aspirinexacerbatedrespiratory pages 1-3, sehanobish2021aspirinactionsin pages 1-2, levy2016contemporarymanagementof pages 1-2, sehanobish2022newconceptsfor pages 9-10)

The following table summarizes the central evidence.

| domain | current understanding/key statistic | evidence type | key source/date/DOI |
|---|---|---|---|
| Definition / prevalence | AERD (also called N-ERD; historically Samter triad) is the adult-onset syndrome of asthma, chronic rhinosinusitis with nasal polyps, and respiratory reactions to COX-1 inhibitors. Estimated prevalence is ~0.3–0.9% in the general US population and ~7% among people with asthma; prevalence is higher in severe asthma, and some cases are likely undiagnosed. (badrani2021cellularinteractionsin pages 1-3, li2019aspirinexacerbatedrespiratory pages 1-3, sehanobish2021aspirinactionsin pages 1-2) | Review synthesis of human epidemiology | Li et al., 2019, *Medical Sciences*, Mar 2019, DOI: 10.3390/medsci7030045; Badrani & Doherty, 2021, DOI: 10.1097/aci.0000000000000712 |
| Mechanism | Core model: COX-1 inhibition lowers protective prostaglandin signaling and is associated with exaggerated cysteinyl leukotriene and PGD2 pathways, epithelial alarmins (IL-33, TSLP), and type-2 cellular circuits involving mast cells, eosinophils, platelets, ILC2s, basophils, and IL-5Rα+ plasma cells. A newer candidate lipid signal, 15-Oxo-ETE, is elevated in AERD nasal polyps. (badrani2021cellularinteractionsin pages 1-3, sehanobish2022newconceptsfor pages 1-3, badrani2021cellularinteractionsin pages 8-9, sehanobish2022newconceptsfor pages 9-10) | Review of human tissue, biomarker, omics, and animal-model data | Sehanobish et al., Nov 2022, *Curr Opin Allergy Clin Immunol*, DOI: 10.1097/aci.0000000000000795; Badrani & Doherty, 2021, DOI: 10.1097/aci.0000000000000712 |
| Diagnosis | Aspirin/NSAID challenge remains the diagnostic standard. Urinary LTE4 is consistently higher in N-ERD/AERD than aspirin-tolerant asthma and tends to rise further after aspirin challenge, but assay/reporting heterogeneity limits stand-alone clinical use. Meta-analysis included 3,376 subjects (1,354 N-ERD, 1,420 ATA, 602 healthy controls); N-ERD vs ATA SMD 0.80 (95% CI 0.72–0.89). (patel2026anarrativereview pages 2-4, sehanobish2022newconceptsfor pages 9-10) | Systematic review/meta-analysis plus review synthesis | Marquette et al., Nov 2022, *Curr Allergy Asthma Rep*, DOI: 10.1007/s11882-022-01049-8 |
| Aspirin desensitization / maintenance | Established multimodal therapy, often paired with sinus surgery. Review-level evidence indicates benefit for sinonasal symptoms, reduced polyp recurrence, improved quality of life, and lower corticosteroid burden in selected patients; biomarkers such as baseline uLTE4/eosinophils may influence response or failure risk. (sehanobish2021aspirinactionsin pages 1-2, levy2016contemporarymanagementof pages 1-2, sehanobish2022newconceptsfor pages 9-10) | Evidence-based review and cohort synthesis | Levy et al., Dec 2016, *Int Forum Allergy Rhinol*, DOI: 10.1002/alr.21826; Sehanobish et al., 2021, DOI: 10.3389/fimmu.2021.695815 |
| Dupilumab | Open-label 6-month study: 23% (7/30) developed complete aspirin tolerance and another 33% (10/30) tolerated higher doses; total polyp score, asthma control, and smell improved, with biomarker reductions including urinary LTE4 in those with increased tolerance. (schneider2023dupilumabincreasesaspirin pages 13-14) | Human interventional trial | Schneider et al., Dec 2023, *Eur Respir J*, DOI: 10.1183/13993003.01335-2022 |
| Omalizumab | Randomized crossover placebo-controlled trial in 16 patients: omalizumab lowered aspirin-challenge urinary LTE4 exposure and 62.5% (10/16) achieved oral aspirin tolerance up to cumulative 930 mg in the omalizumab phase. (sehanobish2022newconceptsfor pages 9-10) | Human randomized controlled trial | Hayashi et al., Jun 2020, *Am J Respir Crit Care Med*, DOI: 10.1164/rccm.201906-1215OC |
| Experimental: GLP-1R axis | Platelets are increasingly viewed as mechanistic contributors. In a murine AERD-like model, liraglutide inhibited lysine-aspirin-induced airway resistance and reduced platelet activation/recruitment; in human AERD platelets in vitro, liraglutide attenuated thromboxane receptor agonist-induced activation. This is mechanistically promising but not yet standard care. (badrani2021cellularinteractionsin pages 1-3) | Mixed animal + human in vitro translational study | Foer et al., Oct 2023, *Journal of Immunology*, DOI: 10.4049/jimmunol.2300102 |
| Experimental: tezepelumab signal | In a severe asthma subgroup analysis, patients with aspirin/NSAID sensitivity had the largest reduction in annualized exacerbation rate with tezepelumab versus placebo: 83% (95% CI 66–91). This supports possible utility in AERD-like severe asthma phenotypes, but the evidence is subgroup rather than AERD-specific prospective trial evidence. (schneider2023dupilumabincreasesaspirin pages 14-14) | Post hoc/subgroup analysis of phase 3 asthma trial | Carr et al., May 2024, *Advances in Therapy*, DOI: 10.1007/s12325-024-02889-8 |
| Model / evidence limitations | AERD is not a monogenic disorder and lacks a single definitive biomarker. Much mechanistic evidence comes from mixed sources—reviews, tissue studies, RNA-seq/single-cell data, in vitro assays, and murine aspirin-challenge models—so causal inference and treatment selection remain imperfect. Reviews also emphasize heterogeneity and variable response to biologics and aspirin therapy. (badrani2021cellularinteractionsin pages 1-3, sehanobish2022newconceptsfor pages 1-3, badrani2021cellularinteractionsin pages 8-9) | Review synthesis across human, omics, in vitro, and animal studies | Badrani & Doherty, 2021, DOI: 10.1097/aci.0000000000000712; Sehanobish et al., Nov 2022, DOI: 10.1097/aci.0000000000000795 |


*Table: This table summarizes the main evidence domains for aspirin-exacerbated respiratory disease, emphasizing current understanding, key quantitative findings, and the level of supporting evidence. It is useful as a compact reference for epidemiology, mechanisms, diagnosis, and established versus emerging therapies.*

## 1. Disease information

### Definition and terminology

The classic triad is:

1. **Asthma**, commonly adult-onset and eosinophilic;
2. **CRSwNP**, generally bilateral and recurrent; and
3. **Acute upper and/or lower respiratory reactions to COX-1-inhibiting NSAIDs**.

Reactions may include nasal obstruction, profuse rhinorrhea, conjunctival symptoms, cough, wheeze, bronchospasm, and occasionally laryngospasm, flushing, gastrointestinal symptoms, or hypotension. Although systemic reactions can resemble anaphylaxis, the canonical mechanism is pharmacologic COX-1 inhibition rather than drug-specific IgE. (li2019aspirinexacerbatedrespiratory pages 1-3, sehanobish2021aspirinactionsin pages 1-2)

**Synonyms:** aspirin-exacerbated respiratory disease; NSAID-exacerbated respiratory disease; N-ERD/NERD; Samter triad/Samter syndrome; aspirin triad; aspirin-sensitive asthma; aspirin-intolerant asthma; aspirin-induced asthma. “N-ERD” is mechanistically broader because cross-reactivity extends beyond aspirin to other strong COX-1 inhibitors.

### Identifiers and ontology mapping

* **MeSH:** *Asthma, Aspirin-Induced* is the closest established descriptor.
* **ICD-10-CM:** no single code completely represents the syndrome. Knowledge bases should compose asthma (J45.-), CRSwNP/nasal polyp (J32.-/J33.-), and adverse-effect or allergy-status coding for aspirin/NSAIDs as appropriate. Coding an aspirin “allergy” alone loses the syndrome’s non-IgE mechanism.
* **ICD-11:** use compositional coding for asthma, chronic rhinosinusitis/nasal polyposis, and NSAID hypersensitivity; local browser releases should be checked because a universally used single AERD stem code is not established.
* **OMIM/Orphanet:** no well-established dedicated Mendelian disease entry is appropriate.
* **MONDO:** a stable dedicated identifier could not be verified from the retrieved authoritative literature; therefore it should be recorded as **unconfirmed**, not inferred.
* Suggested disease-level ontology parentage: complex respiratory disease → asthma phenotype + CRSwNP + nonallergic drug hypersensitivity.

The evidence in this report is predominantly **aggregated disease-level literature**. Primary evidence includes challenge-confirmed clinical cohorts, randomized or open-label intervention studies, surgical cohorts, nasal-polyp and blood specimens, ex-vivo assays, transcriptomics/single-cell analyses, and induced mouse models. It is not derived from an individual patient’s EHR.

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factors

AERD has no single initiating pathogen, toxin, or causal mutation. Disease susceptibility arises from an incompletely resolved interaction among airway epithelial dysfunction, chronic type-2 inflammation, altered eicosanoid metabolism, and pharmacologic exposure to COX-1 inhibitors. Aspirin does not ordinarily create the underlying chronic disease; rather, COX-1 inhibition exposes an already dysregulated lipid-mediator network and precipitates acute reactions. (badrani2021cellularinteractionsin pages 1-3, sehanobish2022newconceptsfor pages 1-3)

### Genetic factors

Reported candidate associations involve **LTC4S, ALOX5, CYSLTR1/CYSLTR2, PTGER2/PTGER4, HLA-DPB1, TBXA2R, MS4A2, ACE**, and genes affecting epithelial integrity and immune-cell interactions. However, associations are population-dependent and often fail replication. For example, a two-stage Mexican Mestizo candidate-gene study found replicated association of **MS4A2 rs573790 CC**, but this is a susceptibility marker—not an ACMG-pathogenic causal variant and not clinically diagnostic. Accordingly:

* no causal gene, OMIM gene–disease relationship, pathogenic variant, inheritance pattern, carrier frequency, or penetrance estimate is established;
* routine WES, WGS, gene panels, single-gene testing, CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are **not indicated for AERD itself**;
* no validated protective allele, founder mutation, anticipation, germline mosaicism, or consanguinity effect is known.

### Demographic and environmental modifiers

Typical onset is in the third or fourth decade; women are more frequently affected, with a reported female:male ratio near **3:2**, and may have earlier or more severe disease. Strong COX-1 inhibitors are the defining acute trigger. Alcohol commonly provokes upper-airway or bronchial symptoms in affected patients, although it is not required for diagnosis. General asthma modifiers—smoking, air pollution, viral infection, occupational irritants, obesity, and poor adherence—may worsen respiratory control, but convincing evidence that they specifically cause AERD is limited. (li2019aspirinexacerbatedrespiratory pages 1-3)

### Protective factors and interaction

Avoiding strong COX-1 inhibitors prevents pharmacologic attacks but does not reliably halt asthma or polyp progression. Selective COX-2 inhibitors are usually better tolerated, but the first dose may warrant supervised administration in highly reactive patients. Leukotriene modifiers attenuate reactions and chronic symptoms. Aspirin desensitization creates a **temporary pharmacologic tolerant state**, maintained only by continuous aspirin exposure; interruption permits resensitization. There is insufficient evidence for a generally protective diet, exercise regimen, microbiome intervention, vitamin, or low-salicylate diet. Dietary salicylates are not equivalent to pharmacologic COX-1 inhibition, and restrictive diets have weak evidence. (sehanobish2021aspirinactionsin pages 1-2, levy2016contemporarymanagementof pages 1-2)

## 3. Phenotypes

### Core phenotype inventory

| Phenotype | Type, onset/course, frequency | Functional impact | Suggested HPO term |
|---|---|---|---|
| Adult-onset asthma | Symptom/sign; usually begins in early-to-middle adulthood; episodic exacerbations on chronic disease; often moderate–severe | Dyspnea, rescue medication, systemic steroids, ED visits and hospitalization | HP:0002099 Asthma; HP:0002098 Respiratory distress; HP:0030828 Wheezing |
| Chronic rhinosinusitis | Sign/symptom; chronic, progressive or fluctuating | Facial pressure, discharge, impaired sleep and productivity | HP:0011109 Chronic sinusitis |
| Bilateral recurrent nasal polyposis | Physical manifestation; high penetrance within classic AERD; recurrent after surgery | Nasal obstruction, repeated surgery, impaired sleep | HP:0100582 Nasal polyposis |
| Hyposmia/anosmia | Symptom; common and frequently severe | Food enjoyment, safety, social and emotional effects | HP:0004408 Abnormality of smell; HP:0000458 Anosmia |
| NSAID-induced rhinorrhea/congestion | Acute provoked symptom, usually within minutes to hours | Restricts analgesic choices; may require monitored challenge | HP:0031417 Rhinorrhea; HP:0001742 Nasal obstruction |
| Bronchospasm/FEV1 fall | Acute clinical/functional sign after COX-1 inhibition | Potentially severe reaction | HP:0025428 Bronchospasm; HP:0002783 Abnormal pulmonary function |
| Blood/tissue eosinophilia | Laboratory/pathology abnormality; common but variable | Correlates imperfectly with severity and biologic eligibility | HP:0001880 Eosinophilia |
| Middle-ear inflammation/hearing symptoms | Secondary manifestation; cohort frequency about 18%, with earlier reports exceeding one-quarter | Poor control and hearing-related disability | HP:0000389 Chronic otitis media; HP:0000365 Hearing impairment |

The disease is heterogeneous: high-type-2, mixed, and lower-type-2 inflammatory clusters have been reported. Atopy is neither necessary nor sufficient. A tertiary-center questionnaire study found good/very-good patient-reported control in **83% for asthma, 58% for nasal polyposis, and only 33% for chronic middle-ear disease**, illustrating that upper-airway and otologic morbidity may dominate quality of life. AERD CRSwNP generally has greater inflammation, worse baseline health-related quality of life, and more revision surgery than aspirin-tolerant CRSwNP. (sehanobish2021aspirinactionsin pages 1-2, levy2016contemporarymanagementof pages 1-2)

## 4. Genetic and molecular information

AERD should be represented as **multifactorial/polygenic susceptibility with no clinically actionable causal genotype**. Reported SNPs are germline association signals; they are not somatic driver variants, do not meet ACMG/AMP pathogenic classification for AERD, and should not be entered as causal alleles. No recurrent aneuploidy, copy-number disorder, translocation, inversion, or chromosomal syndrome is established.

Molecular modifiers include receptor abundance or signaling through **PTGER2/EP2, PTGER4/EP4, CYSLTR1, CYSLTR2, OXGR1/GPR99, CRTH2/PTGDR2, IL4R, IL5RA, ST2/IL1RL1**, and enzymes **PTGS1/COX-1, PTGS2/COX-2, ALOX5/5-LO, LTC4S, HPGDS**, but altered expression or activity is more securely established than pathogenic coding variants. Human studies report reduced COX expression/PGE2 production in polyps and deficient PGE2 production by bronchial fibroblasts; relevant primary studies include PMID **12743569** and **21397936**. (sehanobish2022newconceptsfor pages 9-10)

Epigenetic and microRNA changes have been explored, but no methylation signature or miRNA panel is validated for diagnosis, prognosis, or treatment selection. No AERD-specific pharmacogenomic guideline from CPIC or PharmGKB is established.

## 5. Environmental, lifestyle, and infectious information

* **Defining exposure:** aspirin and nonselective NSAIDs that strongly inhibit COX-1.
* **Alcohol:** frequent non-NSAID symptom trigger; mechanism may involve mast-cell/lipid-mediator pathways, but estimates vary.
* **Smoking/pollution/occupation:** plausible asthma and CRS aggravators; evidence specific to AERD onset is insufficient.
* **Diet:** low-salicylate diets remain experimental and potentially burdensome; no routine recommendation is supported.
* **Exercise:** beneficial for general health and asthma when controlled, but not demonstrated to prevent AERD.
* **Infection:** no bacterium, virus, fungus, or parasite causes AERD. Respiratory infections can exacerbate asthma or sinus disease but do not explain COX-1 cross-reactivity.

## 6. Mechanism and pathophysiology

### Integrated causal chain

**Upstream chronic state:** genetically and environmentally conditioned epithelial barrier/immune dysregulation → chronic sinonasal and bronchial inflammation → reduced protective PGE2 production or EP-receptor responsiveness plus increased 5-LO/LTC4S capacity → constitutively elevated cysteinyl leukotrienes and PGD2. (badrani2021cellularinteractionsin pages 1-3, sehanobish2022newconceptsfor pages 1-3, sehanobish2022newconceptsfor pages 9-10)

**Acute trigger:** aspirin/nonselective NSAID inhibits COX-1 → further loss of PGE2 restraint on eosinophils, mast cells, and 5-LO activity → abrupt amplification of LTC4/LTD4/LTE4 and PGD2 → CysLT-receptor-mediated vascular permeability, mucus secretion, sensory symptoms, and bronchial smooth-muscle contraction. (patel2026anarrativereview pages 2-4, sehanobish2021aspirinactionsin pages 1-2)

**Cellular amplification:** CysLTs and epithelial injury promote **IL-33** release; IL-33 activates mast cells and ILC2s. **TSLP** stimulates mast-cell PGD2 production; PGD2 acting through CRTH2 recruits or activates eosinophils, basophils, Th2 cells, and ILC2s. ILC2/Th2-derived IL-4, IL-5, and IL-13 sustain eosinophilia, IgE/plasma-cell responses, goblet-cell metaplasia, mucus, edema, bronchial hyperresponsiveness, and polyp growth. Platelet–leukocyte aggregates contribute LTC4S activity and inflammatory recruitment. (badrani2021cellularinteractionsin pages 1-3, badrani2021cellularinteractionsin pages 8-9)

**Tissue outcome:** persistent epithelial inflammation, edema, extracellular-matrix remodeling and polyp formation in nasal/paranasal mucosa; bronchial hyperresponsiveness and variable airflow obstruction in lower airways; recurrent acute reactions upon COX-1 inhibition.

### Biochemical and omics findings

* **Lipidomics/metabolomics:** elevated baseline and challenge-induced urinary LTE4; elevated PGD2 metabolites; low lipoxin A4; and increased **15-oxo-ETE** in AERD nasal polyps. (sehanobish2022newconceptsfor pages 1-3)
* **Transcriptomics:** RNA-seq of nasal epithelium has identified altered leukotriene-metabolism and epithelial-response genes. (badrani2021cellularinteractionsin pages 8-9)
* **Single-cell profiling:** IL-5Rα expression is enriched on IgE/IgG4-expressing polyp plasma cells; activated basophils and IL-5Rα-positive plasma cells associate with severe polyposis. A 2024 study further reported a proliferative signature in nasal-polyp antibody-secreting cells, supporting local adaptive-immune activity rather than proving a causal autoantibody. (sehanobish2022newconceptsfor pages 1-3, badrani2021cellularinteractionsin pages 8-9)
* **Macrophages:** persistent pro-inflammatory activation of alveolar monocyte-derived macrophages is a proposed contributor. (sehanobish2022newconceptsfor pages 1-3)
* **Spatial transcriptomics/CRISPR screens:** no clinically mature AERD-specific result was identified.

Suggested annotations include **GO:0006690 eicosanoid metabolic process; GO:0002540 leukotriene production involved in inflammatory response; GO:0006954 inflammatory response; GO:0042098 T-cell proliferation; GO:0032615 interleukin-12 production** (use only where experimentally supported); and cell terms **CL:0000097 mast cell, CL:0000771 eosinophil, CL:0000233 platelet, CL:0001069 group 2 innate lymphoid cell, CL:0000787 memory B cell, CL:0000786 plasma cell, CL:0000235 macrophage, CL:0002633 respiratory airway epithelial cell**.

## 7. Anatomical structures affected

Primary sites are the **nasal cavity, paranasal sinus mucosa, nasal polyps, and bronchial airways**. Suggested UBERON mappings include UBERON:0001707 nasal cavity, UBERON:0001825 paranasal sinus, UBERON:0001988 nasal mucosa, UBERON:0002185 bronchus, and UBERON:0002048 lung. Disease is ordinarily bilateral/diffuse rather than unilateral; unilateral polyposis should prompt an alternative diagnosis. Secondary involvement may include the middle ear and Eustachian tube.

Affected tissues comprise pseudostratified respiratory epithelium, polyp stroma, submucosal vasculature, mucus glands, airway smooth muscle, and resident/infiltrating immune compartments. Relevant subcellular sites include plasma membrane receptors, cytosolic arachidonic-acid enzymes, nuclear transcriptional machinery, and secretory granules of mast cells/eosinophils; there is no defining mitochondrial, lysosomal, or protein-aggregation lesion. Increased sphenoid bone thickness has been reported, probably reflecting chronic inflammatory remodeling (PMID **32660262**). (sehanobish2022newconceptsfor pages 9-10)

## 8. Temporal development

A typical sequence is persistent rhinitis/sinus symptoms, development of asthma, recurrent polyps, and recognition of NSAID reactions, although the order varies. Onset is generally insidious during the third–fourth decades rather than congenital or pediatric. The chronic component is lifelong and progressive/fluctuating; acute drug reactions are episodic. Polyps commonly recur after surgery without sustained anti-inflammatory treatment. Up to 40% of patients in some CRSwNP cohorts may develop or have aspirin sensitivity recognized during follow-up. (li2019aspirinexacerbatedrespiratory pages 1-3, levy2016contemporarymanagementof pages 1-2)

There is no formal staging system analogous to cancer staging. Practical severity domains are asthma control/exacerbations, systemic-corticosteroid burden, endoscopic polyp score, CT Lund–Mackay score, smell function, SNOT-22, prior surgery, and drug-reaction severity. Remission is usually treatment-induced and domain-specific; “cure” is uncommon. Important intervention windows include disease recognition before inadvertent NSAID exposure, postoperative control before rapid polyp regrowth, and biologic or aspirin-therapy escalation before repeated systemic steroid use.

## 9. Inheritance and population epidemiology

AERD prevalence is approximately **0.3–0.9% in the general US population**, **~7% among adults with asthma**, and **~15% among severe asthma**, with estimates of **8–26% among CRSwNP** and approximately 10% among nasal-polyp populations. Challenge-based studies generally detect more disease than history alone; roughly 12% may remain undiagnosed in some asthma settings. (badrani2021cellularinteractionsin pages 1-3, li2019aspirinexacerbatedrespiratory pages 1-3, sehanobish2021aspirinactionsin pages 1-2, levy2016contemporarymanagementof pages 1-2)

Incidence per 100,000 person-years is not reliably established. Women predominate at roughly 3:2. AERD occurs globally; apparent geographic or ethnic differences may reflect referral, NSAID use, diagnostic challenge availability, and genetic background. No robust geographic founder variant is known.

Inheritance is **multifactorial/polygenic with incomplete and poorly quantified familial aggregation**. Mendelian penetrance, carrier status, anticipation, mosaicism, and consanguinity are not applicable.

## 10. Diagnostics

### Clinical criteria and reference testing

A confident clinical diagnosis requires asthma/variable airflow obstruction, objective CRSwNP or chronic eosinophilic sinus disease, and repeated convincing respiratory reactions to at least one—and preferably multiple—COX-1 inhibitors. Where exposure history is absent, ambiguous, or discordant, a **supervised graded aspirin challenge** is the reference standard. Oral challenge is most widely used; nasal lysine-aspirin and bronchial protocols are available in specialized settings. Challenge requires stable asthma, baseline spirometry, trained staff, and rescue capability. (li2019aspirinexacerbatedrespiratory pages 1-3, sehanobish2022newconceptsfor pages 9-10)

Tests should include:

* spirometry with bronchodilator response and serial FEV1 during challenge;
* nasal endoscopy for bilateral polyps;
* sinus CT for extent and surgical planning—not for aspirin sensitivity itself;
* CBC with differential, total IgE, and FeNO for inflammatory phenotyping, not confirmation;
* urinary LTE4 as an adjunctive research/specialty biomarker.

A 2022 meta-analysis included **3,376 participants**—1,354 N-ERD, 1,420 aspirin-tolerant asthma, and 602 healthy controls. Baseline uLTE4 was higher in N-ERD than aspirin-tolerant asthma (SMD **0.80, 95% CI 0.72–0.89**); it rose after aspirin challenge in N-ERD (SMD **0.56, 95% CI 0.26–0.85**) but not meaningfully in aspirin-tolerant asthma (SMD 0.12, 95% CI −0.08–0.33). Heterogeneous assays and thresholds prevent stand-alone diagnosis. (patel2026anarrativereview pages 2-4)

### Pathology and differential diagnosis

Polyps usually show marked eosinophilic/type-2 inflammation, edema, epithelial abnormalities, mast cells and plasma cells, but histology is not specific. Differential diagnoses include aspirin-tolerant eosinophilic CRSwNP with asthma, IgE-mediated single-NSAID allergy, NSAID-induced urticaria/angioedema without airway disease, allergic fungal rhinosinusitis, eosinophilic granulomatosis with polyangiitis, cystic fibrosis, primary ciliary dyskinesia, immunodeficiency, and unilateral neoplasm.

There is no population, newborn, carrier, prenatal, or genetic screening program. Targeted case-finding among adults with severe asthma plus recurrent bilateral polyps is appropriate.

## 11. Outcome and prognosis

AERD generally does not have a defined disease-specific reduction in life expectancy, 5-year survival, or mortality rate. Its major burden is morbidity: severe asthma, systemic corticosteroid exposure, repeated sinus surgery, persistent anosmia, sleep disruption, middle-ear disease, restricted analgesic options, emergency care, and impaired work/social functioning. Compared with aspirin-tolerant asthma or CRSwNP, patients have more corticosteroid use, hospitalizations, lower FEV1, severe recurrent polyposis, and poorer quality of life. (sehanobish2021aspirinactionsin pages 1-2, levy2016contemporarymanagementof pages 1-2)

Poor prognostic features include severe or uncontrolled asthma, high polyp burden, prior revision surgery, persistent eosinophilia/type-2 inflammation, high urinary LTE4, inadequate topical therapy, and failure or intolerance of aspirin maintenance. No biomarker has sufficient validation to predict individual progression. Prognosis improves substantially with coordinated allergy/pulmonology/otolaryngology care, although responses to aspirin therapy and biologics remain heterogeneous.

## 12. Treatment and real-world implementation

### Baseline algorithm

1. Confirm asthma, CRSwNP, and the NSAID-reaction phenotype.
2. Avoid strong COX-1 inhibitors until evaluated; provide written drug-safety guidance and suitable analgesic alternatives.
3. Optimize inhaled corticosteroid-containing asthma treatment, bronchodilators, intranasal corticosteroid, saline irrigation, and short systemic-steroid courses only when necessary.
4. Add a leukotriene receptor antagonist such as **montelukast** or 5-LO inhibitor **zileuton**, especially around challenge/desensitization.
5. Perform endoscopic sinus surgery for obstructive/uncontrolled disease and to improve topical drug access.
6. For persistent disease, choose aspirin desensitization/maintenance, biologic therapy, or both according to asthma/polyp severity, bleeding and gastrointestinal risk, aspirin need, prior response, cost, pregnancy plans, and patient preference.

Suggested NCIt mappings include corticosteroid therapy, leukotriene-receptor antagonist therapy, monoclonal-antibody therapy, aspirin desensitization, endoscopic sinus surgery, and supportive care; exact NCIt concept IDs should be validated against the current NCIt release rather than inferred.

### Aspirin desensitization and aspirin therapy after desensitization

Desensitization followed by uninterrupted daily aspirin can reduce sinonasal symptoms, polyp recurrence, systemic steroid use, asthma morbidity, emergency visits, and repeat surgery in selected patients, especially when performed after adequate sinus surgery. Review-level evidence suggests reduction in polyp recurrence in **more than 70%** of treated patients, although protocols, doses, and outcome definitions vary. (sehanobish2021aspirinactionsin pages 1-2, sehanobish2022newconceptsfor pages 9-10)

A 2023 Chilean prospective cohort of 12 patients treated with sinus surgery, desensitization, and maintenance aspirin found sustained SNOT-22 improvement (p=0.002), reduced polyp score (p=0.001), only three small recurrences, and a **6.6-point Lund–Mackay reduction** (p<0.001) at one year. Adverse effects occurred in **75%**, most often abdominal pain (66.7%), but no participant discontinued during follow-up. This small uncontrolled study supports feasibility, not comparative superiority.

Contraindications or cautions include active peptic ulceration, bleeding disorder, anticoagulation conflicts, uncontrolled asthma, pregnancy, inability to adhere, and prior severe aspirin toxicity. Loss of doses can reverse tolerance.

### Biologics

None is uniquely AERD-approved; use follows severe-asthma and/or CRSwNP indications.

* **Dupilumab** blocks IL-4Rα and therefore IL-4/IL-13 signaling. In a 2023 open-label study, after six months **23% (7/30) achieved complete aspirin tolerance and 33% (10/30) tolerated higher doses**. Total polyp score changed by −2.68±1.84, asthma-control score by +2.34±3.67, and smell score by +11.16±9.54 (all p<0.001). Increased tolerance was associated with lower uLTE4 and reduced eotaxin-1, CCL17, IL-5, IL-17A, and IL-6. The abstract conclusion states: **“Dupilumab improves aspirin hypersensitivity in over 50% of patients.”** (schneider2023dupilumabincreasesaspirin pages 14-14, schneider2023dupilumabincreasesaspirin pages 13-14)
* **Omalizumab** neutralizes free IgE. In a double-blind randomized crossover trial of 16 challenge-confirmed patients, aspirin-challenge uLTE4 exposure fell from a median 80.8 on placebo to 51.1 during omalizumab (p<0.001); **10/16 (62.5%)** tolerated cumulative aspirin doses up to 930 mg. This demonstrates that IgE-pathway modulation can suppress reactions even though AERD is not a conventional aspirin-specific IgE allergy.
* **Mepolizumab** and **benralizumab** target IL-5 or IL-5Rα and can improve eosinophilic asthma and CRSwNP, but AERD response is variable. A 2023 perioperative series reported that mepolizumab did not reliably prevent polyp regrowth; this cautions against assuming that eosinophil depletion controls every AERD pathway.
* **Tezepelumab**, targeting TSLP, reduced annualized exacerbations by **83% (95% CI 66–91)** in the aspirin/NSAID-sensitive subgroup of the 2024 NAVIGATOR severe-asthma analysis. This is hypothesis-supporting subgroup evidence, not an AERD-specific prospective trial.

Expert reviews emphasize that there is no definitive evidence that biologics must always precede aspirin desensitization or vice versa. Dupilumab often provides the broadest simultaneous benefit for smell, polyps, and asthma, whereas aspirin therapy is inexpensive and may be particularly valuable after surgery or when aspirin is required for cardiovascular indications. Choice should be individualized. (sehanobish2022newconceptsfor pages 1-3)

### Current experimental approaches and trials

Retrieved AERD-specific ClinicalTrials.gov records include dupilumab mechanism/efficacy studies **NCT03595488**, **NCT04442256**, and **NCT05031455**; thromboxane-receptor antagonist ifetroban safety **NCT02216357**; low-salicylate diet **NCT01540032/NCT01778465**; nasal microbiome **NCT04375293**; genetics/genomics **NCT04261582**; microRNA **NCT01631773**; IL-5R signaling in upper-airway cells **NCT05672030**; sleep after sinonasal surgery **NCT03627481**; and aspirin therapy/SARS-CoV-2 susceptibility **NCT05797597**. These records include small mechanistic trials and observational studies and do not establish routine care.

A 2023 translational study found that the GLP-1R agonist **liraglutide** reduced lysine-aspirin-induced airway resistance and platelet activation/recruitment in an AERD-like mouse model and attenuated thromboxane-agonist activation in platelets from 31 patients with AERD and 11 controls. This supports the platelet–GLP-1R axis as a candidate target but not off-label clinical treatment. (badrani2021cellularinteractionsin pages 1-3)

Gene therapy, cell therapy, RNA therapeutics, CRISPR treatment, and transplantation have no established role.

## 13. Prevention

**Primary prevention:** no intervention is known to prevent initial disease development. There is no vaccine or validated genetic/lifestyle prevention program.

**Secondary prevention:** recognize the combination of adult-onset asthma, recurrent bilateral polyps, anosmia, and NSAID or alcohol reactions; confirm uncertain cases before inadvertent exposure. Maintain a precise medication record distinguishing cross-reactive COX-1 intolerance from single-drug IgE allergy.

**Tertiary prevention:** avoid unplanned strong COX-1 exposure; use a medical-alert plan; optimize inhaled and topical therapy; control polyps early; use leukotriene modifiers around planned challenge; consider surgery, biologics, or aspirin desensitization to reduce recurrence and steroid toxicity. Patients who have been desensitized require continuous prescribed aspirin and instructions for missed doses. Standard immunizations are appropriate for asthma health but do not prevent AERD.

## 14. Other species and natural disease

No well-characterized naturally occurring veterinary equivalent of the full human AERD triad was identified in dogs, cats, livestock, or wildlife. Consequently, there is no established breed/VBO association, zoonotic transmission, cross-species natural epidemiology, or veterinary carrier state. Aspirin pharmacology and orthologous eicosanoid genes are conserved, but this does not establish naturally occurring AERD. The condition is noninfectious and nontransmissible.

## 15. Model organisms and experimental systems

The principal in-vivo system is an **induced murine AERD-like model**, commonly involving allergic airway inflammation/eosinophilia followed by lysine-aspirin challenge. It can reproduce acute airway-resistance increases, mast-cell activation, platelet recruitment, IL-33 dependence, PGD2/CysLT release, and response to pathway inhibition. Murine work supports a sequence in which LTE4 promotes epithelial IL-33, followed by mast-cell activation and acute bronchoconstriction. (badrani2021cellularinteractionsin pages 1-3)

Genetic knockouts or pathway perturbations involving PGE synthase/EP receptors, leukotriene receptors, IL-33/ST2, mast cells, platelets, or ILC2s are mechanistic models rather than complete disease replicas. Ex-vivo systems include patient platelets, eosinophils, mast cells, nasal epithelial cultures, polyp explants, fibroblasts, and peripheral blood; omics systems include bulk RNA-seq, single-cell RNA-seq, metabolomics, and lipid mediator profiling. (badrani2021cellularinteractionsin pages 8-9, sehanobish2022newconceptsfor pages 9-10)

Limitations are substantial: mice do not spontaneously develop the full adult-onset sequence of asthma, bilateral recurrent polyposis, and human NSAID intolerance; induced sensitization and aspirin dosing differ from clinical disease; and no model captures long-term surgery–polyp recurrence or heterogeneous biologic response. No validated zebrafish, Drosophila, C. elegans, yeast, iPSC, or organoid model currently recapitulates the complete syndrome.

## Evidence-quality conclusions and key gaps

The strongest clinical evidence supports challenge-based diagnosis, uLTE4 as an adjunct rather than replacement biomarker, coordinated upper/lower-airway treatment, postoperative aspirin desensitization in selected patients, and use of asthma/CRSwNP-approved biologics. The most important 2023–2024 developments are dupilumab-associated improvement in aspirin tolerance, the tezepelumab signal in NSAID-sensitive severe asthma, GLP-1R/platelet translational findings, and single-cell evidence of proliferative antibody-secreting cells in AERD polyps. These advances refine endotyping but do not yet provide a curative treatment or definitive molecular diagnostic. (sehanobish2022newconceptsfor pages 1-3, schneider2023dupilumabincreasesaspirin pages 14-14, schneider2023dupilumabincreasesaspirin pages 13-14)

Major unresolved questions include why the syndrome begins in adulthood, which epithelial or immune abnormalities are initiating rather than secondary, how to select aspirin therapy versus a specific biologic, whether combination therapy modifies natural history, and which biomarkers predict durable remission. There remain no validated causal variants, protective variants, AERD-specific mortality estimates, population incidence rates, or natural animal disease models.

References

1. (badrani2021cellularinteractionsin pages 1-3): Jana H. Badrani and Taylor A. Doherty. Cellular interactions in aspirin-exacerbated respiratory disease. Dec 2021. URL: https://doi.org/10.1097/aci.0000000000000712, doi:10.1097/aci.0000000000000712. This article has 17 citations and is from a peer-reviewed journal.

2. (li2019aspirinexacerbatedrespiratory pages 1-3): Kevin L. Li, Andrew Y. Lee, and Waleed M. Abuzeid. Aspirin exacerbated respiratory disease: epidemiology, pathophysiology, and management. Mar 2019. URL: https://doi.org/10.3390/medsci7030045, doi:10.3390/medsci7030045. This article has 80 citations.

3. (sehanobish2022newconceptsfor pages 1-3): Esha Sehanobish, Mohammad Asad, and Elina Jerschow. New concepts for the pathogenesis and management of aspirin-exacerbated respiratory disease. Current Opinion in Allergy and Clinical Immunology, 22:42-48, Nov 2022. URL: https://doi.org/10.1097/aci.0000000000000795, doi:10.1097/aci.0000000000000795. This article has 10 citations and is from a peer-reviewed journal.

4. (sehanobish2021aspirinactionsin pages 1-2): Esha Sehanobish, Mohammad Asad, Mali Barbi, Steven A. Porcelli, and Elina Jerschow. Aspirin actions in treatment of nsaid-exacerbated respiratory disease. Frontiers in Immunology, Jun 2021. URL: https://doi.org/10.3389/fimmu.2021.695815, doi:10.3389/fimmu.2021.695815. This article has 16 citations and is from a peer-reviewed journal.

5. (levy2016contemporarymanagementof pages 1-2): Joshua M. Levy, Luke Rudmik, Anju T. Peters, Sarah K. Wise, Brian W. Rotenberg, and Timothy L. Smith. Contemporary management of chronic rhinosinusitis with nasal polyposis in aspirin‐exacerbated respiratory disease: an evidence‐based review with recommendations. International Forum of Allergy & Rhinology, 6:1273-1283, Dec 2016. URL: https://doi.org/10.1002/alr.21826, doi:10.1002/alr.21826. This article has 75 citations and is from a peer-reviewed journal.

6. (sehanobish2022newconceptsfor pages 9-10): Esha Sehanobish, Mohammad Asad, and Elina Jerschow. New concepts for the pathogenesis and management of aspirin-exacerbated respiratory disease. Current Opinion in Allergy and Clinical Immunology, 22:42-48, Nov 2022. URL: https://doi.org/10.1097/aci.0000000000000795, doi:10.1097/aci.0000000000000795. This article has 10 citations and is from a peer-reviewed journal.

7. (badrani2021cellularinteractionsin pages 8-9): Jana H. Badrani and Taylor A. Doherty. Cellular interactions in aspirin-exacerbated respiratory disease. Dec 2021. URL: https://doi.org/10.1097/aci.0000000000000712, doi:10.1097/aci.0000000000000712. This article has 17 citations and is from a peer-reviewed journal.

8. (patel2026anarrativereview pages 2-4): Preena Ketan Patel, Aagat Sharma Khatiwada, Peter J Andrews, Glenis K Scadding, and Alfonso Luca Pendolino. A narrative review of recent developments in aspirin therapy after desensitization in nsaids-exacerbated respiratory disease. Journal of Inflammation Research, Volume 19:1-23, Aug 2026. URL: https://doi.org/10.2147/jir.s620047, doi:10.2147/jir.s620047. This article has 0 citations and is from a peer-reviewed journal.

9. (schneider2023dupilumabincreasesaspirin pages 13-14): Sven Schneider, Katharina Poglitsch, Christina Morgenstern, Tamara Quint, Katharina Gangl, Christoph Sinz, Tina Bartosik, Nicholas James Campion, David Tianxiang Liu, Lukas David Landegger, Aldine Tu, Victoria Stanek, Marianne Rocha-Hasler, Christine Bangert, and Julia Eckl-Dorna. Dupilumab increases aspirin tolerance in nsaid-exacerbated respiratory disease. The European Respiratory Journal, 61:2201335, Dec 2023. URL: https://doi.org/10.1183/13993003.01335-2022, doi:10.1183/13993003.01335-2022. This article has 43 citations.

10. (schneider2023dupilumabincreasesaspirin pages 14-14): Sven Schneider, Katharina Poglitsch, Christina Morgenstern, Tamara Quint, Katharina Gangl, Christoph Sinz, Tina Bartosik, Nicholas James Campion, David Tianxiang Liu, Lukas David Landegger, Aldine Tu, Victoria Stanek, Marianne Rocha-Hasler, Christine Bangert, and Julia Eckl-Dorna. Dupilumab increases aspirin tolerance in nsaid-exacerbated respiratory disease. The European Respiratory Journal, 61:2201335, Dec 2023. URL: https://doi.org/10.1183/13993003.01335-2022, doi:10.1183/13993003.01335-2022. This article has 43 citations.

## Artifacts

- [Edison artifact artifact-00](Aspirin-Exacerbated_Respiratory_Disease-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.