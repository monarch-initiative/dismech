---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T13:21:02.723727'
end_time: '2026-08-19T13:25:03.253621'
duration_seconds: 240.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SLC12A5-Related Developmental and Epileptic Encephalopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 11
  num_turns: 17
  total_cost_usd: 1.7378702000000001
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 18
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 14
  on_topic: 5
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SLC12A5-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SLC12A5-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I'll research SLC12A5-Related Developmental and Epileptic Encephalopathy now and compile the full report.

I now have sufficient material to compile the comprehensive report.

# SLC12A5-Related Developmental and Epileptic Encephalopathy: Comprehensive Research Report

## 1. Disease Information

**Overview.** SLC12A5-related disease is a severe, early-infantile developmental and epileptic encephalopathy (DEE) caused by biallelic (autosomal recessive) loss-of-function variants in *SLC12A5*, the gene encoding the neuron-specific potassium-chloride cotransporter KCC2. The canonical, most severe presentation is **epilepsy of infancy with migrating focal seizures (EIMFS)** — formerly called "malignant migrating partial seizures of infancy (MMPSI)" — characterized by onset of intractable, multifocal, migrating seizures typically before 6 months of age, accompanied by developmental delay or regression, hypotonia, and postnatal microcephaly (Stödberg et al. 2015, PMID:26333769; GeneReviews NBK537476). A milder heterozygous-variant spectrum has also been reported in idiopathic generalized epilepsy, febrile seizures, autism, and schizophrenia, though causality there is less firmly established (Kahle lab, PMC4600830).

**Key identifiers:**
- **Gene:** *SLC12A5* (HGNC:13818), chromosome 20q13.12, 24 exons, NCBI Gene ID 57468
- **Protein:** KCC2 (K-Cl cotransporter 2 / SLC12A5), UniProt Q9H2X9, 1139 amino acids, ~126 kDa
- **OMIM gene:** *606726 (SLC12A5)
- **OMIM phenotype:** #616645 — Developmental and Epileptic Encephalopathy 34 (DEE34), also historically "EIEE34" (early infantile epileptic encephalopathy 34)
- **Orphanet:** ORPHA:293181 (Epilepsy of infancy with migrating focal seizures)
- **Inheritance:** Autosomal recessive (biallelic — homozygous or compound heterozygous)
- **GeneReviews:** NBK537476 — "SLC12A5-Related Epilepsy of Infancy with Migrating Focal Seizures"
- **MONDO:** corresponds to DEE34 (recommend cross-checking exact MONDO CURIE against OMIM 616645 mapping)

**Synonyms:** SLC12A5-EIMFS; EIEE34; DEE34; KCC2-related epileptic encephalopathy; KCC2 deficiency disorder; (historically) malignant migrating partial seizures of infancy (MMPSI) when caused by SLC12A5.

**Evidence basis:** Nearly all published data derive from aggregated case series/case reports (fewer than 20 published individuals across all reports as of 2024–2026) plus mechanistic cellular/animal-model studies — this is a very rare, individually-reported-patient literature rather than large-registry epidemiology.

Sources: [GeneReviews SLC12A5-EIMFS](https://www.ncbi.nlm.nih.gov/books/NBK537476/), [OMIM #616645](https://omim.org/entry/616645), [OMIM *606726](https://www.omim.org/entry/606726), [Nature Communications 2015](https://www.nature.com/articles/ncomms9038)

---

## 2. Etiology

**Disease causal factor:** Biallelic loss-of-function pathogenic variants (homozygous or compound heterozygous) in *SLC12A5*, encoding KCC2. This is a purely monogenic, Mendelian etiology — no infectious, toxic, or acquired trigger is implicated in the primary disease process.

**Genetic risk factors:**
- Missense, splice-site, and in-frame deletion variants have been reported; missense predominates (GeneReviews NBK537476).
- Recent case reports (Hamze et al. 2026, *Epilepsia*) describe compound heterozygous variants that impair both the canonical **chloride-extrusion function** of KCC2 and separate **chloride-independent developmental functions** of KCC2 (e.g., structural/scaffolding roles in synapse and dendritic spine maturation), broadening the molecular mechanism spectrum beyond simple transport loss-of-function.
- A specific missense variant, **p.(R231H)** in transmembrane domain 4 (TM4) — the first pathogenic missense variant described in that domain — was identified in a Finnish patient from consanguineous parents and functionally characterized (PMC11039960, 2024).
- Consanguinity is a recognized risk factor given the recessive, biallelic requirement (illustrated in the R231H homozygous case).
- Heterozygous *SLC12A5* variants (distinct from the biallelic DEE34 mechanism) have been separately associated with **idiopathic generalized epilepsy (IGE)** and **febrile seizures**, and rare regulatory-domain/CpG-site variants (e.g., R952H, R1049C) with **autism spectrum disorder and schizophrenia** (PMC4600830) — these represent a different, milder, likely partial-penetrance/susceptibility mechanism, not the severe biallelic DEE34 phenotype.

**Environmental risk factors:** None specifically established; this is a monogenic disorder. No known toxin, infection, or lifestyle exposure modifies risk.

**Protective factors:** No specific genetic or environmental protective factors are documented in the literature.

**Gene-environment interaction:** Not established/reported for this ultra-rare monogenic condition.

Sources: [PMC11039960 (R231H variant)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11039960/), [Hamze et al. 2026 Epilepsia](https://onlinelibrary.wiley.com/doi/10.1002/epi.70258), [PMC4600830 (regulatory variants, autism/schizophrenia)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4600830/)

---

## 3. Phenotypes

**Core seizure phenotype (symptoms/signs):**
- Onset before 6 months of age; **median seizure onset 1.5 months, mean 1.8 months** (range: 1 day–4 months) in the published GeneReviews cohort of 9 children (NBK537476).
- Some biallelic cases present even more acutely, with **bilateral migratory focal seizures within the first 24 hours of life** in severe neonatal-onset presentations.
- Initial seizure semiology: focal motor seizures with prominent **head and eye deviation**, apnea, and autonomic features (facial flushing, salivation).
- Seizures become **multifocal, "migrating"** across cortical regions (the defining EIMFS electroclinical signature) and are typically **pharmacoresistant** to standard anti-seizure medications (ASMs).
- Suggested HPO terms: **HP:0032792** (migrating seizures — if available) or more generally **HP:0002133** (focal-onset seizure), **HP:0011097** (epileptic spasm, if present), **HP:0002197** (generalized-onset seizure for later evolution), **HP:0032799** (developmental regression with seizures pattern), **HP:0011451** (drug-resistant epilepsy), **HP:0032207** (apneic episode/autonomic seizure feature).

**Developmental/neurological phenotype:**
- **Developmental delay in all affected children**; **developmental regression** (loss of previously acquired skills) at seizure onset in a majority (5/9 in the GeneReviews cohort).
- **Profound intellectual disability** in the most severely affected (e.g., developmental age of 2 months at chronological age 2 years in the R231H case).
- **Axial hypotonia** — a recurrent, near-universal feature (HP:0008936 Hypotonia; HP:0002490 Axial hypotonia).
- **Extrapyramidal features** reported in some neonatal-onset cases (dystonia/dyskinetic movements) — HP:0002071 (extrapyramidal motor findings).
- **Postnatal microcephaly** in most patients — HP:0005484.
- Variable outcomes: some children achieve independent ambulation (ages 2.9–4 years) or single words (by age 6); others remain profoundly disabled or die in early childhood.

**Neuroimaging findings:**
- Nonspecific: delayed myelination, thin corpus callosum, cerebral atrophy — HP:0002119 (Ventriculomegaly), HP:0002079 (Hypoplasia of the corpus callosum), HP:0002505 (Loss of ambulation, later stage), HP:0012444 (Brain atrophy).
- One autopsy case (R231H, deceased at 4y5m) showed agenesis of the corpus callosum, markedly enlarged lateral ventricles, and scarcity of white matter — an extreme end of the imaging spectrum.

**Systemic/secondary complications:**
- Recurrent aspiration pneumonia and respiratory infections (a leading cause of death — one child died at 2.5 years from respiratory infection; the R231H patient died at 4y5m from pneumonia).
- Feeding difficulties requiring gastrostomy.
- Osteopenia (reported in the R231H case, likely related to immobility/anticonvulsant use).

**Frequency/severity notes:** Given the very small published cohort (fewer than 20 confirmed cases in aggregate across all reports as of 2026), formal frequency percentages (e.g., "80% of patients") are not statistically robust; qualitative descriptors ("most," "all," "some") are used throughout the primary literature rather than quantitative frequency bands.

**Quality of life impact:** Severely affected — profound intellectual disability, non-ambulation in many cases, high caregiver burden, and reduced life expectancy in the most severe neonatal-onset cases. No disease-specific EQ-5D/SF-36 data are published; QoL burden is inferred from the DEE literature generally (comparable to other severe infantile DEEs).

Sources: [GeneReviews NBK537476](https://www.ncbi.nlm.nih.gov/books/NBK537476/), [PMC11039960](https://pmc.ncbi.nlm.nih.gov/articles/PMC11039960/), [Hamze et al. 2026](https://onlinelibrary.wiley.com/doi/10.1002/epi.70258)

---

## 4. Genetic/Molecular Information

**Causal gene:** *SLC12A5* (HGNC:13818; OMIM *606726), chromosome 20q13.12, 24 exons.

**Variant spectrum:**
- Primarily **missense** variants; also splice-site variants (e.g., ClinVar RCV001230522 c.2787+6G>A; RCV000652718 c.3126-6C>A — both classified in association with DEE34) and in-frame deletions.
- Notable characterized variant: **c.692G>A, p.(R231H)** — homozygous, in TM4, first pathogenic missense variant in that transmembrane domain, from consanguineous Finnish parents (PMC11039960).
- Compound heterozygous genotypes reported combining variants that separately impair chloride-transport function and chloride-independent (developmental/structural) KCC2 functions (Hamze et al. 2026).
- Original Stödberg et al. 2015 cohort (PMID:26333769) established **recessive loss-of-function** as the mechanism via biallelic variants in multiple unrelated families, functionally validated in vitro.
- Saitsu et al. 2016 (Scientific Reports, PMC4951812) independently identified biallelic *SLC12A5* mutations causing impaired KCC2 function in migrating focal seizures with severe developmental delay.

**Variant classification (ACMG/ClinVar):** Multiple variants classified as Pathogenic or Likely Pathogenic in ClinVar in association with "Developmental and epileptic encephalopathy, 34." Functional data (electrophysiology, surface expression) have been used to reclassify VUS variants as pathogenic (e.g., R231H, originally VUS, reclassified pathogenic per ACMG criteria after functional study — PMC11039960).

**Allele frequency:** Pathogenic *SLC12A5* DEE34 variants are extremely rare/private in population databases (gnomAD), consistent with an ultra-rare severe recessive DEE; no specific population allele-frequency statistics for individual pathogenic variants were retrieved in this search, but the extreme rarity of the disease (estimated prevalence 0.11/100,000 children — see Epidemiology) implies very low carrier frequency.

**Functional consequences (loss of function):**
- **Decreased KCC2 surface/membrane expression** — R231H showed ~5-fold lower membrane-bound fluorescence vs. wild type.
- **Reduced protein glycosylation** and **impaired post-translational trafficking**.
- **Enhanced ER-associated degradation (ERAD)** — R231H "undergoes ERAD more efficiently than wild-type."
- **Impaired chloride extrusion**: gramicidin-perforated patch-clamp shows depolarized glycine-receptor reversal potential (E_Gly) — wild-type median −79.5 mV vs. R231H −58.5 mV vs. mock (no KCC2) −49.5 mV (p=0.0329) — indicating substantially but not completely abolished transport function.
- **Reduced ion (K+) flux**: NH4+/pHluorin flux assay showed 52% reduction in acidification rate for R231H vs. wild-type (p=0.00067).
- Net result: elevated intracellular chloride, depolarizing (excitatory) GABA_A responses, impaired synaptic inhibition, and neuronal hyperexcitability.

**Epigenetic/regulatory variation:** Regulatory-domain or CpG-site variants in *SLC12A5* (distinct from coding loss-of-function) reported in autism and schizophrenia cohorts (PMC4600830) — a separate, milder mechanistic category from DEE34.

**Modifier genes:** None specifically established for *SLC12A5*-DEE34.

**Chromosomal abnormalities:** Not a copy-number/structural-variant disease mechanism — point mutations and small indels/splice variants predominate; no recurrent CNV etiology reported.

Ontology suggestions: **HGNC:13818** (SLC12A5); **GO:1902476** (chloride transmembrane transport) / **GO:0055064** (chloride ion homeostasis); **GO:0008511** (sodium:potassium:chloride symporter activity — for family context) or more precisely potassium:chloride symporter activity; **CHEBI:17996** (chloride).

Sources: [Stödberg 2015](https://www.nature.com/articles/ncomms9038), [Saitsu 2016 PMC4951812](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4951812/), [PMC11039960](https://pmc.ncbi.nlm.nih.gov/articles/PMC11039960/), [Hamze 2026](https://onlinelibrary.wiley.com/doi/10.1002/epi.70258)

---

## 5. Environmental Information

No specific environmental, lifestyle, or infectious contributory factors are documented for the primary (biallelic) *SLC12A5*-DEE34 disease process — this is a purely monogenic disorder. Secondary environmental factors are relevant only to disease *complications* (e.g., recurrent aspiration pneumonia as a cause of mortality relates to hypotonia/dysphagia rather than being a disease cause). No infectious agent is implicated in etiology.

---

## 6. Mechanism / Pathophysiology

**Core causal chain:**
1. **Trigger:** Biallelic loss-of-function *SLC12A5* variant → reduced KCC2 protein synthesis, trafficking, membrane insertion, and/or transport activity (molecular scale).
2. **Molecular consequence:** Impaired KCC2-mediated K+-Cl− cotransport → failure to extrude intracellular chloride against its electrochemical gradient (KCC2 normally uses the outward K+ gradient set by Na+/K+-ATPase to drive Cl− out of neurons).
3. **Cellular consequence:** Elevated intraneuronal [Cl−] → depolarizing shift in the GABA_A/glycine receptor reversal potential (E_GABA/E_Gly) → **GABA and glycine signaling become excitatory rather than inhibitory** (the classic "GABA excitatory shift").
4. **Circuit consequence:** Loss of fast synaptic inhibition → neuronal hyperexcitability, hypersynchronization, and failure of seizure termination mechanisms (KCC2 chloride transport also contributes to terminating ictal activity, per PMC7986536).
5. **Developmental consequence (chloride-independent arm, per Hamze et al. 2026):** KCC2 additionally serves structural/scaffolding roles (via its large intracellular C-terminal domain interacting with cytoskeletal and synaptic proteins) important for dendritic spine and excitatory synapse maturation; variants disrupting this arm independently impair neurodevelopment, compounding the chloride-transport deficit.
6. **Clinical manifestation:** Neonatal/early-infantile onset migrating, multifocal, pharmacoresistant seizures, developmental arrest/regression, hypotonia, and progressive encephalopathy.

**Molecular pathway:** Cation-chloride cotransporter (CCC) family signaling; KCC2 is the principal neuronal Cl− extruder, counterbalanced developmentally by NKCC1 (SLC12A2, the Cl− importer) — the NKCC1-to-KCC2 developmental switch underlies the well-known perinatal shift from depolarizing to hyperpolarizing GABA action. In *SLC12A5*-DEE34, this maturational switch fails or is incomplete.

**Protein dysfunction:** KCC2 misfolding/reduced glycosylation → ER retention and enhanced ER-associated degradation (ERAD) → reduced surface expression; for missense variants retaining some surface expression (e.g., R231H), residual but markedly reduced transport activity persists (partial/hypomorphic loss of function rather than complete null).

**Cellular processes:** Impaired GABAergic/glycinergic inhibitory neurotransmission; secondary effects on interneuron circuit maturation — conditional Kcc2 knockout in GABAergic neurons in mice causes an imbalance of cortical interneuron subtypes (excess somatostatin+ neurons in layer 5, reduced parvalbumin+ neurons in layers 2/3 and 6) (PMC8966887), suggesting KCC2 loss disrupts interneuron network assembly, not merely acute inhibition.

**Immune involvement:** Not a primary mechanism, though downstream KCC2 inhibition/neuronal hyperexcitability has been linked in unrelated contexts to complement (C1q)-dependent extrinsic apoptotic signaling (PMC12399595) — relevance to SLC12A5-DEE34 specifically is not established and should be treated as a tangential mechanistic note, not disease-specific evidence.

**Suggested GO terms:** GO:0006821 (chloride transport), GO:0034765 (regulation of ion transmembrane transport), GO:0007214 (gamma-aminobutyric acid signaling pathway), GO:0060080 (inhibitory postsynaptic potential), GO:0050804 (modulation of chemical synaptic transmission).
**Suggested CL terms:** CL:0000540 (neuron), CL:0000601 (GABAergic interneuron), CL:0000679 (glutamatergic neuron, as postsynaptic partner).

Sources: [Journal of Molecular Neuroscience 2022](https://link.springer.com/article/10.1007/s12031-022-02041-7), [PMC6873151](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6873151/), [PMC7986536 (KCC2 and ictal termination)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7986536/), [PMC8966887 (conditional Kcc2 KO, interneuron imbalance)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8966887/), [Hamze 2026](https://onlinelibrary.wiley.com/doi/10.1002/epi.70258)

---

## 7. Anatomical Structures Affected

**Organ level:** Central nervous system (brain) is the primary and essentially exclusive site of disease; KCC2 is neuron-specific (not expressed in most peripheral tissues). Secondary/complication-level organ involvement includes the respiratory system (aspiration pneumonia) and skeletal system (osteopenia, likely secondary to immobility).

**Body systems:** Nervous system (primary); musculoskeletal (secondary, hypotonia-related); respiratory (secondary, aspiration risk).

**Tissue/cell level:** Cortical and subcortical neurons broadly; particular relevance to **GABAergic interneurons** (given KCC2's centrality to GABAergic inhibitory signaling) and to postsynaptic neurons receiving GABAergic/glycinergic input generally. Corpus callosum white matter is structurally affected (thin/agenesis on imaging).

**Subcellular level:** Plasma membrane (KCC2 is a 12-transmembrane-domain integral membrane transporter); large intracellular C-terminal cytoplasmic domain (site of chloride-independent structural/scaffolding interactions); endoplasmic reticulum (site of misfolding/ERAD for trafficking-defective variants).

**Anatomical ontology suggestions:** UBERON:0000955 (brain), UBERON:0001872 (cerebral cortex), UBERON:0002336 (corpus callosum), CL:0000601 (GABAergic interneuron); GO Cellular Component: GO:0005886 (plasma membrane), GO:0005783 (endoplasmic reticulum), GO:0043005 (neuron projection).

**Localization:** Bilateral, diffuse/multifocal cortical involvement (consistent with the "migrating" multifocal seizure semiology, implying no single fixed epileptogenic focus but rather a global susceptibility to hyperexcitability).

---

## 8. Temporal Development

**Onset:** Neonatal to early infantile — median 1.5 months, mean 1.8 months, range 1 day to 4 months in the largest published case series; some biallelic cases present within the first 24 hours of life. Onset pattern is typically **acute/subacute**, often abrupt.

**Progression:**
- Rapid evolution from focal to multifocal, migrating, drug-resistant seizures within weeks of onset.
- Developmental trajectory: either static delay from birth or **regression** (loss of previously acquired skills) coinciding with seizure onset in the majority of reported cases.
- Disease course is generally **progressive/static-severe** rather than truly relapsing-remitting, though seizure burden can fluctuate with treatment response (e.g., partial response to ketogenic diet or potassium bromide in some).
- No formal staging system exists (unlike, e.g., cancer staging) — severity is generally described qualitatively (mild/attenuated vs. severe neonatal-onset).

**Patterns:**
- No spontaneous remission reported; some children show treatment-associated partial seizure reduction (ketogenic diet, potassium bromide) without full seizure freedom.
- The **first months of life represent a critical developmental window** — this is biologically consistent with the normal developmental NKCC1-to-KCC2 chloride-transporter switch that occurs perinatally in humans; disruption of KCC2 function during this exact window is thought to be maximally deleterious, which may explain the strict early-infantile onset window of EIMFS phenotypes.

Sources: [GeneReviews NBK537476](https://www.ncbi.nlm.nih.gov/books/NBK537476/)

---

## 9. Inheritance and Population

**Epidemiology:**
- SLC12A5-EIMFS is exceedingly rare. EIMFS overall (all genetic causes combined) was estimated at a prevalence of **0.11 per 100,000 children in the UK** (non-population-based estimate). *SLC12A5* accounts for only a small fraction of EIMFS cases — the most common EIMFS gene is **KCNT1** (~27% of a 135-case genetic cohort), with *SCN2A* second (~7%); *SLC12A5* is one of several rarer causal genes (alongside *SCN1A*, *SCN8A*, *PLCB1*, *SLC25A22*, *TBC1D24*, and 16p11.2 duplication, plus more recently described genes *GABRA1*, *GABRB1*, *ATP1A3*, *CDKL5*, *PIGA*, *ITPA*, *AIMP1*, *KARS*, *WWOX*).
- For context, DEE overall (all causes) has a cumulative incidence of ~169/100,000 children and point prevalence of ~112/100,000 children — underscoring that *SLC12A5*-DEE34 represents a very small subset of this broader category.
- Fewer than 20 genetically confirmed *SLC12A5*-DEE34 patients have been published in aggregate across all case series as of the 2026 literature.

**Inheritance pattern:** Autosomal recessive. Each sibling of an affected individual has a 25% chance of being affected, 50% chance of being an asymptomatic carrier, and 25% chance of being unaffected. Parents are typically unaffected heterozygous carriers.

**Penetrance:** Full penetrance is assumed for biallelic loss-of-function variants based on published cases (no reported unaffected biallelic carriers), though the very small sample size limits confidence in this estimate.

**Expressivity:** Variable — clinical severity ranges from profound neonatal-onset encephalopathy with early death to somewhat milder courses with eventual acquisition of ambulation or single words, suggesting genotype-dependent (hypomorphic vs. null) variable expressivity.

**Consanguinity:** A recognized contributing factor for homozygous presentations (e.g., the Finnish R231H case arose from consanguineous parents).

**Founder effects / population-specific variants:** Not specifically documented for *SLC12A5*-DEE34 in the literature retrieved; each family generally carries private variants.

**Sex ratio:** No sex predilection reported (autosomal, not X-linked).

**Carrier frequency:** Not established at a population level given the extreme rarity and diversity of pathogenic alleles (essentially private variants rather than a small recurrent set).

Sources: [GeneReviews NBK537476](https://www.ncbi.nlm.nih.gov/books/NBK537476/), [Epidemiology of DEE, Neurology 2023, PMID:36581463](https://pubmed.ncbi.nlm.nih.gov/36581463/), [PMC6878841 (KCNT1 EIMFS landscape)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6878841/)

---

## 10. Diagnostics

**Genetic testing (primary diagnostic modality):**
- **Exome or genome sequencing is the preferred first-tier approach**, given the broad genetic heterogeneity of EIMFS (many candidate genes) — GeneReviews explicitly recommends this over single-gene testing.
- Diagnosis requires identification of **biallelic pathogenic/likely pathogenic *SLC12A5* variants**.
- Functional validation (electrophysiology, surface trafficking assays) can be used to reclassify variants of uncertain significance, as demonstrated for p.(R231H).
- Multi-gene epilepsy panels covering EIMFS-associated genes (*KCNT1*, *SCN2A*, *SCN1A*, *SCN8A*, *PLCB1*, *SLC25A22*, *TBC1D24*, *SLC12A5*, *GABRA1*, *GABRB1*, *ATP1A3*, *CDKL5*, *PIGA*, and others) are a reasonable alternative when exome/genome sequencing is unavailable.

**EEG:**
- Interictal: multifocal spikes.
- Ictal: characteristic **migrating** pattern — seizure activity involving varying cortical areas over time with clinical-EEG correlation (the defining electroclinical signature of EIMFS, common to all genetic causes).

**Neuroimaging (MRI):** Nonspecific findings — delayed myelination, thin/absent corpus callosum, cerebral atrophy, enlarged ventricles in severe cases.

**Clinical diagnostic criteria:** EIMFS is a clinically defined electroclinical syndrome (onset <6 months, migrating multifocal seizures, developmental delay/regression) that requires genetic testing to identify the specific causal gene, since the electroclinical phenotype is shared across multiple genetic etiologies.

**Differential diagnosis:** Other EIMFS-causing genes (see above), particularly **KCNT1** (most common cause, ~27%) and *SCN2A*; broader neonatal/infantile DEE differentials include other early-infantile epileptic encephalopathies (e.g., Ohtahara syndrome genes, *STXBP1*, *KCNQ2*).

**Screening:** No population newborn-screening or carrier-screening program exists specifically for *SLC12A5*, given its extreme rarity; testing is reactive (diagnostic) rather than population-screening based. Prenatal and preimplantation genetic testing become available once familial variants are identified in an affected proband.

Suggested ontology: **NCIT:C63846** or similar for "Whole Exome Sequencing"; **LOINC** codes for EEG and MRI brain studies would be assigned per standard clinical coding, not disease-specific.

Sources: [GeneReviews NBK537476](https://www.ncbi.nlm.nih.gov/books/NBK537476/), [PMC11039960](https://pmc.ncbi.nlm.nih.gov/articles/PMC11039960/)

---

## 11. Outcome/Prognosis

**Survival/mortality:** Mortality is significant in the most severely affected. Reported deaths: one child died at age 2.5 years from respiratory infection complications; the R231H homozygous patient died at 4 years 5 months from pneumonia. Other reported patients survive into childhood/early adulthood (ages 3–22 years in the GeneReviews cohort) with varying functional status.

**Morbidity/function:** Profound to severe intellectual disability is typical; motor outcomes range from non-ambulation to independent ambulation achieved late (ages 2.9–4 years) in less severely affected children; some achieve single-word speech by age 6.

**Complications:** Recurrent aspiration pneumonia/respiratory infections (leading cause of death), feeding difficulties/failure to thrive (often requiring gastrostomy), osteopenia, progressive encephalopathy.

**Recovery potential:** No cure or disease-modifying therapy exists; developmental gains are possible during periods of improved seizure control but the underlying encephalopathy is not reversible with current treatments.

**Prognostic factors:** Disease severity appears to correlate with the degree of residual KCC2 function retained by the specific variant(s) (null/complete loss-of-function vs. hypomorphic variants retaining partial transport activity), and possibly with whether chloride-independent developmental KCC2 functions are also disrupted (per Hamze et al. 2026) — though formal genotype-phenotype correlation studies with adequate sample size are not yet available given the rarity of the disorder.

Sources: [GeneReviews NBK537476](https://www.ncbi.nlm.nih.gov/books/NBK537476/), [PMC11039960](https://pmc.ncbi.nlm.nih.gov/articles/PMC11039960/)

---

## 12. Treatment

**Pharmacotherapy (anti-seizure medications):**
- **No specific/disease-modifying treatment exists.** GeneReviews states plainly: "There are no specific treatments for seizures in SLC12A5-EIMFS. In general, seizures in EIMFS are resistant to most ASM."
- Documented ASM trials with limited/no efficacy in reported cases: phenytoin, phenobarbital, midazolam, ketamine, sodium thiopental, levetiracetam, topiramate, lacosamide, lidocaine (from the R231H case, largely ineffective).
- Modest benefit reported with **levetiracetam, rufinamide, and stiripentol** in some EIMFS patients generally (GeneReviews); note these are general EIMFS management options, not *SLC12A5*-specific evidence in all cases.
- **Potassium bromide**: achieved partial response in the R231H patient (40 mg/kg/day at age 2 years), reducing focal tonic-clonic seizures from >10/day to a few per day — the most clearly documented partial-responder therapy in the literature reviewed.

**Dietary therapy:**
- **Ketogenic diet**: reported to produce seizure reduction in some individuals; however in the R231H case it was discontinued after 3.5 months due to lack of response — response is variable.

**Investigational/mechanism-targeted approaches (not yet clinical for SLC12A5-DEE34 specifically):**
- **NKCC1 inhibition (bumetanide)**: The broader chloride-cotransporter therapeutic literature has explored bumetanide (an NKCC1 inhibitor) to rebalance the NKCC1/KCC2 ratio and restore inhibitory GABA signaling in various neurodevelopmental/epilepsy conditions (autism, schizophrenia, fragile X, Down syndrome); this has NOT been reported as a validated *SLC12A5*-DEE34-specific therapy in the literature retrieved, and its rationale is somewhat paradoxical for KCC2 loss-of-function (bumetanide blocks Cl− import via NKCC1, but the core defect here is impaired Cl− export via KCC2 — theoretically bumetanide could still help by reducing the chloride load that a deficient KCC2 cannot clear, but empirical human data for this specific gene were not found).
- **KCC2-activating small molecules**: Under active pharmaceutical development (patent literature: "KCC2 expression enhancing compounds," US11331313 and US12053465) but not yet in clinical use; reviewed in "Development of KCC2 therapeutics to treat neurological disorders" (PMC11666659) and "The Expanding Therapeutic Potential of Neuronal KCC2" (PMC7016893). These represent a rational future precision-therapy direction directly targeting the causal deficiency but are preclinical/early-stage.

**Supportive/rehabilitative care:**
- Physical therapy for hypotonia.
- Swallowing assessment and gastrostomy for feeding difficulties.
- Preventive respiratory care given high pneumonia/aspiration risk.
- Early intervention and developmental therapy programs.

**Experimental treatments:** No *SLC12A5*-DEE34-specific registered clinical trials were identified in this search; KCC2-targeted small-molecule programs remain preclinical.

Suggested NCIT terms: NCIT:C15632 (Chemotherapy — n/a here), NCIT:C15986 (Pharmacotherapy, for ASMs and potassium bromide), NCIT:C15447 (Dietary Intervention, for ketogenic diet), NCIT:C15302 (Physical Therapy), NCIT:C15315 (Rehabilitation), NCIT:C15329 (Surgical Procedure, for gastrostomy placement).

Sources: [GeneReviews NBK537476](https://www.ncbi.nlm.nih.gov/books/NBK537476/), [PMC11039960](https://pmc.ncbi.nlm.nih.gov/articles/PMC11039960/), [PMC11666659 (KCC2 therapeutics development)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11666659/), [PMC7016893 (KCC2 therapeutic potential)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7016893/)

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (no modifiable risk factor); the only "primary prevention" available is reproductive: **genetic counseling and carrier testing** for families with a known affected proband, plus **prenatal diagnosis or preimplantation genetic testing (PGT)** once familial pathogenic variants are identified.

**Secondary prevention:** Early genetic diagnosis (via exome/genome sequencing) allows earlier prognostic counseling and avoidance of a prolonged, costly "diagnostic odyssey," though it does not currently alter seizure outcomes given the lack of disease-modifying therapy.

**Genetic counseling:** Standard autosomal recessive counseling applies — 25% recurrence risk for future pregnancies of carrier parents; extended family carrier testing can be offered once the familial variants are known.

**Screening:** No population-based newborn or carrier screening program exists for *SLC12A5* given its rarity; this remains a reactive, proband-driven diagnostic pathway.

**Public health/behavioral/prophylaxis:** Not applicable — this is a non-preventable monogenic disorder; management focuses on secondary complication prevention (aspiration precautions, respiratory infection prophylaxis) rather than primary disease prevention.

---

## 14. Other Species / Natural Disease

No naturally occurring *SLC12A5*/KCC2-deficient disease has been reported in non-human species (e.g., no OMIA entry for a spontaneous veterinary KCC2 disorder was identified in this search). KCC2 orthologs are broadly conserved across vertebrates (mouse *Slc12a5*, MGI:1862037), and the gene's fundamental role in neuronal chloride homeostasis is evolutionarily conserved, but disease relevance in non-human species comes exclusively from **engineered/induced models** (see Section 15), not natural disease.

---

## 15. Model Organisms

**Mouse models (the dominant model system):**
- **Complete Kcc2 knockout mice** (Hübner et al. 2001; Woo et al. 2002): homozygous null mice exhibit **frequent generalized seizures and die shortly after birth** — demonstrating that complete loss of KCC2 is perinatally lethal in mice, consistent with KCC2's essential role in establishing inhibitory GABA/glycine signaling.
- **Kcc2b isoform-specific knockout**: mice lacking the neuron-specific KCC2b splice isoform (while retaining the KCC2a isoform expressed more broadly/earlier) survive longer but **die in the third postnatal week from seizures** — this partial/isoform-specific model better approximates a survivable, seizure-prone phenotype useful for mechanistic study (Tao et al., and related isoform-specific knockout literature).
- **Heterozygous Kcc2+/− mice**: show altered seizure threshold and increased susceptibility to chemoconvulsant-induced seizures without the severe neonatal lethality of the homozygous null — modeling milder/partial KCC2 deficiency states, potentially relevant to the heterozygous IGE/febrile-seizure-associated human variants.
- **Conditional (GABAergic-neuron-specific) Kcc2 knockout mice** (PMC8966887, Frontiers in Molecular Neuroscience 2022): early seizures, failure to thrive, premature death in the second/third postnatal week; underlying **imbalance of cortical interneuron subtypes** — excess somatostatin+ interneurons in cortical layer 5, decreased parvalbumin+ interneurons in layers 2/3 and 6 — providing a developmental circuit-level mechanistic link between KCC2 loss and cortical hyperexcitability distinct from the acute chloride-transport deficit alone.

**Model characteristics and fidelity:**
- These knockout models **recapitulate the core human phenotype** of severe, early-onset, lethal/near-lethal seizures with loss of GABAergic inhibition, supporting strong construct and face validity for the acute chloride-dysregulation mechanism.
- **Limitation:** complete knockouts are more severe and more rapidly lethal than most human cases (which, as compound heterozygotes or hypomorphic homozygotes, typically retain partial KCC2 function and survive infancy), so complete-null mouse models likely overrepresent the most extreme end of the human phenotypic spectrum; isoform-specific and conditional models better approximate survivable human disease.
- Human-specific developmental timing (the NKCC1-to-KCC2 perinatal switch occurs at different relative developmental stages in mouse vs. human) is a recognized **HUMAN_MODEL_MISMATCH**-type caveat: the precise correspondence between mouse postnatal age and human gestational/neonatal timing for KCC2 maturation is not one-to-one, which should be considered when interpreting knockout-model timing as directly analogous to human neonatal-onset EIMFS.

**Cellular/heterologous expression models:**
- HEK293/other heterologous cell systems expressing wild-type vs. mutant KCC2 (used for R231H functional characterization): gramicidin-perforated patch-clamp (E_Gly reversal potential), NH4+/pHluorin flux assays, and surface immunolabeling — these are the primary **in vitro functional validation platforms** used across nearly all published *SLC12A5* variant characterization studies (Stödberg 2015, Saitsu 2016, PMC11039960).

**Resources:** MGI:1862037 (mouse *Slc12a5* gene record, Jackson Laboratory Mouse Genome Informatics).

Sources: [PMC8966887](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8966887/), [Nature Scientific Reports 2017](https://www.nature.com/articles/s41598-017-00196-7), [MGI:1862037](https://www.informatics.jax.org/marker/MGI:1862037), [PMC11039960](https://pmc.ncbi.nlm.nih.gov/articles/PMC11039960/)

---

## Summary Table: Key Evidence-Ready Citations

| Topic | PMID/Reference | Key Finding |
|---|---|---|
| Original disease description | PMID:26333769 (Stödberg 2015, Nat Commun) | Recessive LOF *SLC12A5* variants cause EIMFS; functional loss of KCC2 transport demonstrated |
| Independent confirmation | PMC4951812 (Saitsu 2016, Sci Rep) | Biallelic *SLC12A5* mutations impair KCC2 function in migrating focal seizures + severe DD |
| Recent variant/mechanism study | PMC11039960 (2024) | p.(R231H) TM4 variant; detailed electrophysiology/trafficking functional data; ACMG reclassification |
| Expanded mechanistic spectrum | Hamze et al. 2026, *Epilepsia*, doi:10.1002/epi.70258 | Compound het variants disrupt both Cl−-dependent and Cl−-independent KCC2 functions |
| Clinical synopsis/management | GeneReviews NBK537476 | Comprehensive clinical, diagnostic, and management summary (9-patient cohort) |
| Disease/gene identifiers | OMIM #616645 (DEE34); OMIM *606726 (SLC12A5) | Formal phenotype/gene MIM entries |
| Mouse knockout mechanism | Hübner 2001; Woo 2002; PMC8966887 | Kcc2-null perinatal lethal seizures; conditional KO shows interneuron subtype imbalance |
| Heterozygous variant spectrum | PMC4600830 | Regulatory/CpG variants linked to autism, schizophrenia, IGE, febrile seizures |
| EIMFS genetic landscape/differential | PMC6878841 | KCNT1 most common (27%) EIMFS gene; SLC12A5 one of several rarer causes |

---

**Notes on data gaps:** This is an ultra-rare disorder with a published literature base of well under 20 confirmed cases; formal quantitative frequency data (phenotype penetrance percentages, precise prevalence/incidence, standardized QoL scores) are largely unavailable and should be represented in a knowledge base as qualitative/descriptive rather than fabricated numeric estimates. Ontology term suggestions above (particularly specific HPO codes) should be verified against current HPO/OAK term lookups before curation, as exact CURIEs for some described features (e.g., "migrating seizures") may require confirmation of the precise current term ID and label.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.