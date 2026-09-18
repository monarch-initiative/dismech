---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T10:07:26.303170'
end_time: '2026-09-01T10:13:51.250610'
duration_seconds: 384.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Leukoencephalopathy with vanishing white matter 5 (EIF2B5-related
    vanishing white matter disease)
  mondo_id: MONDO:0957873
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 10
  verified: 9
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0957873
    reported_labels:
    - if available
    ontology_label: leukoencephalopathy with vanishing white matter 5
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Leukoencephalopathy_With_Vanishing_White_Matter_5-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leukoencephalopathy with vanishing white matter 5 (EIF2B5-related vanishing white matter disease)
- **MONDO ID:** MONDO:0957873 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leukoencephalopathy with vanishing white matter 5 (EIF2B5-related vanishing white matter disease)** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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
- **Disease Name:** Leukoencephalopathy with vanishing white matter 5 (EIF2B5-related vanishing white matter disease)
- **MONDO ID:** MONDO:0957873 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leukoencephalopathy with vanishing white matter 5 (EIF2B5-related vanishing white matter disease)** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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


# EIF2B5-related leukoencephalopathy with vanishing white matter

## Executive summary

EIF2B5-related vanishing white matter disease (VWM5) is an autosomal-recessive, stress-sensitive leukodystrophy caused by biallelic pathogenic variants in **EIF2B5**, which encodes the catalytic ε-subunit of eukaryotic translation initiation factor 2B (eIF2B). The disorder is dominated by progressive cerebellar and pyramidal dysfunction, with episodes of abrupt neurologic deterioration after fever, infection, seizures, or head trauma. MRI shows diffuse cerebral white-matter signal abnormality followed by rarefaction and cystic disappearance. Astrocyte dysfunction, secondary failure of oligodendrocyte maturation, and maladaptive integrated stress response (ISR) signaling are central to current pathophysiologic models. No curative treatment is established, but the oral eIF2B activator fosigotifator is in Phase 1b/2 testing, while astrocyte-targeted gene addition and variant-specific base editing produced partial rescue in 2024 mouse studies. (knaap2022therapytrialdesign pages 2-4, herstine2024evaluationofsafety pages 1-2, bock2024invivobase pages 1-2, NCT05757141 chunk 1)

The following table provides a compact, knowledge-base-oriented summary.

| domain | curated finding | suggested ontology/identifier | evidence type |
|---|---|---|---|
| Disease identity | EIF2B5-related vanishing white matter disease is a Mendelian leukodystrophy within the broader vanishing white matter spectrum; MONDO lists the gene-specific entity as leukoencephalopathy with vanishing white matter 5. (OpenTargets Search: vanishing white matter disease-EIF2B5, trevisan2021anelevenyearhistory pages 1-3) | MONDO:0957873; OMIM:603896; suggested MeSH: Leukoencephalopathies | Aggregated disease ontology + human clinical literature |
| Gene / molecular lesion | Disease is caused by biallelic pathogenic variants in **EIF2B5**, encoding eIF2B epsilon, a catalytic subunit of the eIF2B guanine nucleotide exchange factor complex. EIF2B5 is the most commonly mutated VWM gene. (OpenTargets Search: vanishing white matter disease-EIF2B5, trevisan2021anelevenyearhistory pages 1-3, bock2024invivobase pages 1-2) | EIF2B5; ENSG00000145191; suggested HGNC: EIF2B5 | Disease-gene curation + human/mouse molecular studies |
| Inheritance | Inheritance is **autosomal recessive** with stress-sensitive neurologic deterioration. (knaap2022therapytrialdesign pages 1-2, trevisan2021anelevenyearhistory pages 1-3, herstine2024evaluationofsafety pages 1-2) | suggested HPO inheritance term: Autosomal recessive inheritance | Human clinical / expert review |
| Synonyms | Common names include **vanishing white matter disease (VWM)** and **childhood ataxia with central nervous system hypomyelination (CACH/CACH-VWM)**. (trevisan2021anelevenyearhistory pages 1-3) | suggested synonym set for KB: VWM; VWMD; CACH | Human clinical literature |
| Clinical onset / course | Onset ranges from antenatal life to adulthood/senescence; ~90% of patients present before age 18 and ~60% before age 4. In ~85% the course is chronic with superimposed episodic deteriorations; stress-provoked worsening is common. (knaap2022therapytrialdesign pages 2-4, knaap2022therapytrialdesign pages 1-2) | suggested HPO: Infantile onset; Childhood onset; Adult onset; Progressive neurologic deterioration | Natural-history synthesis / expert consensus |
| Stress triggers | Febrile or afebrile infections, minor head trauma, seizures, and other physiologic stressors can precipitate major neurologic decline. (knaap2022therapytrialdesign pages 1-2, herstine2024evaluationofsafety pages 1-2) | suggested HPO: Stress-induced neurologic deterioration | Human clinical / expert review |
| Hallmark neurologic phenotypes | Core manifestations include cerebellar ataxia, spasticity, gait impairment, seizures, motor decline, and sometimes cognitive/behavioral changes; adult cases may be milder and more variable. (knaap2022therapytrialdesign pages 2-4, knaap2022therapytrialdesign pages 1-2, trevisan2021anelevenyearhistory pages 1-3) | suggested HPO: Ataxia; Spasticity; Abnormal gait; Seizure; Developmental regression; Cognitive impairment | Human clinical / natural-history evidence |
| Extra-neurologic phenotypes | Ovarian failure/premature ovarian insufficiency is a recognized associated feature in affected females in the EIF2B-related disease spectrum. (english2022a(dis)integratedstress pages 18-19) | suggested HPO: Premature ovarian insufficiency | Human clinical / review evidence |
| MRI signature | Brain MRI is characteristically diffuse cerebral white-matter abnormality with increased T2 signal, progressive rarefaction and cystic degeneration, often with relative sparing of U-fibers; this pattern is considered highly characteristic/pathognomonic. (knaap2022therapytrialdesign pages 2-4, trevisan2021anelevenyearhistory pages 1-3) | suggested UBERON: cerebral white matter; corpus callosum; frontal lobe white matter; suggested RadLex term: leukoencephalopathy pattern | Human imaging / expert consensus |
| Anatomy affected | Primary pathology involves CNS white matter, especially telencephalic white matter; gray matter can be involved to a lesser degree, while some regions such as brainstem may be relatively spared. (man2024proteomicdissectionof pages 1-2) | suggested UBERON: brain white matter; telencephalon; cerebellum; brainstem; corpus callosum | Human neuropathology + mouse proteomics |
| Key cell types | Astrocytes are the primary affected cell type, with secondary impairment of oligodendrocytes and axons; impaired astrocyte maturation can precede pathology and inhibit oligodendrocyte maturation. (man2024proteomicdissectionof pages 1-2, herstine2024evaluationofsafety pages 1-2, bock2024invivobase pages 1-2) | suggested CL: astrocyte; oligodendrocyte; oligodendrocyte precursor cell | Human, mouse, and cellular mechanistic evidence |
| Core mechanism | EIF2B5 variants reduce eIF2B guanine nucleotide exchange activity and dysregulate the **integrated stress response (ISR)**, causing abnormal translational control under stress and constitutive downstream ISR activation. (man2024proteomicdissectionof pages 1-2, hanson2024eif2blocalizationand pages 1-2, bock2024invivobase pages 1-2) | suggested GO: translation initiation; guanine nucleotide exchange factor activity; integrated stress response; response to endoplasmic reticulum stress | Human/mouse molecular mechanism |
| Cellular pathology | Demonstrated downstream changes include elevated ATF4/CHOP stress signaling, immature/dysmorphic astrocytes, abnormal Bergmann glia, disrupted myelin, and clustering of oligodendrocyte progenitor cells. (terumitsu‐tsujita2020glialpathologyin pages 1-2, bock2024invivobase pages 1-2) | suggested GO: cellular response to stress; myelination; glial cell differentiation; oligodendrocyte differentiation | Mouse pathology / mechanistic evidence |
| Molecular profiling | 2024 proteomics showed region- and time-dependent dysregulation: cerebellum and cortex were altered before overt pathology, corpus callosum after onset, and some brainstem changes were transient/possibly compensatory. (man2024proteomicdissectionof pages 1-2) | suggested GO: proteostasis; metabolic process; oligodendrocyte differentiation | Mouse proteomics cross-referenced to human brain data |
| Variant / genotype-phenotype notes | EIF2B5 accounts for a majority of VWM cases; severity generally inversely correlates with age at onset, but molecular severity does not always map perfectly onto measured eIF2B functional impairment. (english2022a(dis)integratedstress pages 18-19, trevisan2021anelevenyearhistory pages 1-3) | suggested annotation: genotype-phenotype correlation, variable expressivity | Human clinical + mechanistic review |
| Diagnostic approach | Diagnosis integrates clinical syndrome, characteristic MRI, and molecular confirmation of biallelic EIF2B variants; current studies and trials require clinical, molecular, and MRI-consistent diagnosis. (trevisan2021anelevenyearhistory pages 1-3, NCT05757141 chunk 1, NCT05757141 chunk 2) | suggested NCIT: Magnetic Resonance Imaging; Molecular Genetic Testing; Whole Exome Sequencing; Whole Genome Sequencing | Human clinical practice / trial eligibility criteria |
| Current management | Standard care remains supportive/symptomatic with emphasis on preventing or rapidly managing stressors that trigger decompensation; no established curative therapy is yet available. (knaap2022therapytrialdesign pages 1-2, herstine2024evaluationofsafety pages 1-2) | suggested NCIT: Supportive Care; Physical Therapy; Seizure Management; Genetic Counseling | Expert review / current clinical management |
| Current interventional trial | **Fosigotifator (ABBV-CLS-7262)** is in an open-label Phase 1b/2 trial enrolling adult and pediatric VWM participants; objectives include safety, tolerability, PK, and exploratory efficacy. (NCT05757141 chunk 1, NCT05757141 chunk 2) | NCT05757141; Drug: Fosigotifator | ClinicalTrials.gov registry evidence |
| 2024 gene therapy advance | A 2024 mouse study found astrocyte-targeted **AAV9-EIF2B5** supplementation improved body weight, motor function/gait, mean life expectancy, and showed evidence of attenuated demyelination; the gfaABC(1)D promoter construct performed best. (herstine2024evaluationofsafety pages 8-11, herstine2024evaluationofsafety pages 1-2) | suggested NCIT: Adeno-Associated Virus Vector Gene Therapy | Preclinical mouse intervention |
| 2024 base-editing advance | A 2024 mouse study used neonatal intracerebroventricular AAV delivery of split adenine base editors, achieving mean cortical correction of **45.9% ± 5.9%** for Eif2b5 R191H and partial phenotypic rescue, highlighting promise and delivery/precision limitations. (bock2024invivobase pages 1-2) | suggested NCIT: Base Editing; Genome Editing | Preclinical mouse genome-editing study |
| 2024 pharmacology signal | Not all ISR-modulating or repurposed agents are equally promising: lithium showed limited efficacy and side effects in animal models, whereas pridopidine produced only subtle motor benefit in mice. (witkamp2024lithiumeffectsin pages 1-2) | suggested NCIT: Drug Repositioning; Integrated Stress Response Modulation | Preclinical pharmacology |
| Experimental platforms / models | Useful models include Eif2b5 mutant mice (e.g., R191H, I98M), zebrafish eif2b5 mutants, patient-derived iPSC astrocytes, and human post-mortem organotypic brain slice cultures. (terumitsu‐tsujita2020glialpathologyin pages 1-2, herstine2024evaluationofsafety pages 1-2) | suggested NCBI Taxon: Mus musculus; Danio rerio; suggested Cellosaurus/iPSC annotations | Model organism and ex vivo systems |


*Table: This table condenses core knowledge-base facts for EIF2B5-related vanishing white matter disease, including identifiers, phenotypes, mechanisms, diagnostics, and emerging therapies. It is designed to support structured curation and ontology mapping.*

## 1. Disease information

### Definition and identifiers

VWM5 is the **EIF2B5-specific** member of the broader EIF2B-related VWM spectrum. Important identifiers are:

- **MONDO:** MONDO:0957873, “leukoencephalopathy with vanishing white matter 5.” The broader VWM concept is MONDO:0800448.
- **OMIM:** **603896**, conventionally used for VWM/CACH. Gene-specific database records should be distinguished from the umbrella clinical phenotype.
- **Gene:** **EIF2B5**, Ensembl **ENSG00000145191**, approved name “eukaryotic translation initiation factor 2B subunit epsilon.” Open Targets reports curated EIF2B5–VWM5 evidence supported by ClinGen-style gene curation and publications including PMIDs **11704758, 11835386, 12325082, 12707859, 15136690, 17646634, 18266750, 19158808, 21484434, 25457085, 25655951, 25843247,** and **29995139**. (OpenTargets Search: vanishing white matter disease-EIF2B5)
- **MeSH:** no uniquely specific VWM5 descriptor was identified; the trial registry maps the condition under **Leukoencephalopathies (D056784)** and Neurodegenerative Diseases (D019636).
- **ICD-10/ICD-11:** no disease-specific billing code was established from the retrieved evidence; it is generally represented under inherited/metabolic leukoencephalopathy or leukodystrophy categories. A local terminology service should verify jurisdiction-specific coding.

Synonyms include **vanishing white matter disease**, **VWM/VWMD**, **childhood ataxia with central nervous system hypomyelination**, **CACH**, **CACH/VWM**, **myelinopathia centralis diffusa**, and **EIF2B-related disorder**. The gene-specific label should not be interpreted as a clinically separate syndrome from VWM caused by EIF2B1–EIF2B4; it denotes molecular subtype.

This report synthesizes **aggregated disease-level resources, cohorts, expert consensus, individual case reports, human tissue, patient-derived cells, and model-organism evidence**. It is not based on an individual EHR. The 2021 adult report, for example, is single-patient evidence and should not be used to estimate population frequencies. (trevisan2021anelevenyearhistory pages 5-6, trevisan2021anelevenyearhistory pages 1-3)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The necessary initiating lesion is usually a pair of germline pathogenic or likely pathogenic **EIF2B5** alleles. EIF2B5 variants account for approximately **65–70%** of molecularly diagnosed VWM across onset groups, although the exact proportion depends on ascertainment. Variants in EIF2B1–EIF2B4 cause clinically overlapping VWM but not the gene-specific VWM5 entity. (trevisan2021anelevenyearhistory pages 1-3)

Pathogenic alleles are generally **hypomorphic/partial loss-of-function** rather than complete null alleles. They may reduce catalytic guanine-nucleotide exchange, destabilize the eIF2B decamer, impair assembly, or alter stress-dependent regulation. Importantly, measured loss of GEF activity does not invariably predict clinical severity; some severe alleles have little detectable effect in particular biochemical assays. (english2022a(dis)integratedstress pages 18-19, bock2024invivobase pages 1-2)

### Risk and modifier factors

- **Genetic:** biallelic pathogenic EIF2B5 variants and family history are primary risk factors. Allelic severity contributes to phenotype, but intrafamilial variability indicates additional genetic, developmental, or environmental modifiers.
- **Environmental/physiologic precipitants:** febrile and afebrile infection, fever, minor head trauma, seizures, anesthesia or surgery, and severe fright or other physiologic stress can precipitate deterioration. These do not cause the Mendelian disorder; they expose deficient stress-response reserve. (knaap2022therapytrialdesign pages 1-2, herstine2024evaluationofsafety pages 1-2)
- **Age:** earlier onset predicts a more severe course at the group level. It is a prognostic factor, not an acquired cause.
- **Sex:** both sexes are affected. Females may additionally develop premature ovarian insufficiency; no robust sex difference in neurologic incidence was established.
- **Lifestyle/toxins:** no reproducible smoking, alcohol, diet, occupational, pollutant, radiation, or toxin risk factor is known.
- **Infectious agents:** no pathogen is etiologic. Common infections act as nonspecific stress triggers.

No validated **protective allele**, diet, supplement, or lifestyle exposure has been established. Practical protection consists of reducing avoidable stressors, promptly treating fever/infection, preventing head injury, maintaining vaccination, and carefully planning surgery/anesthesia. These measures reduce triggering risk but cannot prevent inherited disease.

## 3. Phenotypes

Frequency values apply to the overall EIF2B-related VWM spectrum unless explicitly gene-specific; sufficiently powered EIF2B5-only frequency tables are unavailable.

- **Stress-sensitive neurologic deterioration** — chronic progression with acute episodes after stress; **85%** have chronic disease plus episodic exacerbations and approximately 15% chronic progression alone. Exacerbating courses occurred in 84% with onset before 12 months, 88% at 1–<2 years, 93% at 2–<4 years, and 59% in adult-onset disease. Episodes may recover completely or partially, leave permanent deficits, or cause coma/death. Suggested HPO: *episodic neurologic deterioration*, *developmental regression*. (knaap2022therapytrialdesign pages 2-4, knaap2022therapytrialdesign pages 1-2, man2024proteomicdissectionof pages 1-2)
- **Cerebellar ataxia and gait impairment** — cardinal motor manifestations, typically progressive and often worsened stepwise after episodes. Suggested HPO: **Ataxia (HP:0001251)**, *cerebellar ataxia*, **abnormal gait (HP:0001288)**.
- **Spasticity/pyramidal dysfunction** — variable, progressive limb stiffness, hyperreflexia, weakness, and eventual loss of ambulation. Suggested HPO: **Spasticity (HP:0001257)**, *hyperreflexia*, *pyramidal signs*.
- **Motor developmental regression/weakness** — especially severe in infantile disease; impacts mobility, transfers, self-care, and caregiver burden. Suggested HPO: *motor regression*, **muscle weakness (HP:0001324)**.
- **Seizures** — variable rather than universal; seizures may themselves trigger deterioration. Suggested HPO: **Seizure (HP:0001250)**.
- **Cognitive and psychiatric manifestations** — cognitive decline is often less prominent than motor decline in childhood but may dominate adult disease, with dementia, behavioral, or psychiatric symptoms. The documented 52-year-old EIF2B5 patient had two transient aphasic episodes 11 years apart and no cognitive decline, illustrating variable expressivity. Suggested HPO: *cognitive impairment*, *dementia*, *behavioral abnormality*, *aphasia*. (trevisan2021anelevenyearhistory pages 5-6, trevisan2021anelevenyearhistory pages 1-3)
- **Optic atrophy/visual dysfunction** — recognized but variably present. Suggested HPO: **Optic atrophy (HP:0000648)**.
- **Dysarthria, dysphagia, sphincter dysfunction** — later manifestations in some patients; they compromise communication, nutrition, aspiration safety, and independence. Suggested HPO: *dysarthria*, *dysphagia*, *urinary incontinence*.
- **Premature ovarian insufficiency/ovarian dysgenesis** — an important female extra-neurologic phenotype, sometimes producing the ovarioleukodystrophy presentation. Suggested HPO: **Premature ovarian insufficiency (HP:0008209)**. (english2022a(dis)integratedstress pages 18-19)

No disease-specific EQ-5D, SF-36, or PROMIS norms were identified. Nevertheless, progressive loss of walking, speech, feeding, continence, and cognition implies substantial quality-of-life and caregiver effects. Quantitative patient-reported outcome data remain a research gap.

## 4. Genetic and molecular information

**EIF2B5** encodes eIF2Bε, one of two catalytic subunits in the heterodecameric eIF2B complex. The complex contains two copies each of eIF2Bα–ε; ε directly contributes GEF activity that converts eIF2-GDP to eIF2-GTP. (hanson2024eif2blocalizationand pages 1-2, bock2024invivobase pages 1-2)

Reported pathogenic classes include predominantly **missense variants**, with nonsense, frameshift, and splice-disrupting alleles also represented in clinical databases. Examples include **c.584G>A (p.Arg195His)**, associated with severe early-onset/Cree leukoencephalopathy, and the adult case's compound variants **c.592G>A (p.Glu198Lys)** and **c.1360C>T (p.Pro454Ser)**. Variant interpretation must be transcript-specific and follow ACMG/AMP criteria; a variant should not be called pathogenic from phenotype alone. (trevisan2021anelevenyearhistory pages 1-3, bock2024invivobase pages 1-2)

The variants are constitutional **germline** alleles, not recurrent somatic drivers. Population frequencies are allele-specific; no reliable aggregate carrier frequency or gnomAD estimate was available in the retrieved corpus. Pathogenic alleles are expected to be rare and compatible with recessive inheritance. VUSs require segregation, population, computational, RNA, and preferably functional evidence.

No clinically validated modifier gene or protective EIF2B5 allele is established. No reproducible disease-specific DNA methylation signature, histone alteration, or large recurrent chromosomal rearrangement is known. CMA, karyotype, and FISH therefore have low first-line yield unless another genomic syndrome is suspected.

## 5. Environmental information

No environmental toxin, infectious organism, dietary pattern, smoking behavior, or occupational exposure is known to generate VWM5. The relevant environmental biology is **triggering**, not causation: infection, fever, trauma, seizures, and perioperative stress impose a translational/proteostatic load on genetically vulnerable cells. Viral infection, oxidative stress, and heme deprivation are examples of stressors that normally engage eIF2B-regulated ISR signaling. (herstine2024evaluationofsafety pages 1-2)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic EIF2B5 hypomorphic variants lead to** reduced catalytic activity, impaired assembly, or reduced stability of the eIF2B decamer.
2. **Defective eIF2B leads to** inadequate recycling of eIF2-GDP into active eIF2-GTP and reduced availability of translation-initiation ternary complexes.
3. **Cellular stress leads to** PERK, PKR, GCN2, or HRI phosphorylation of eIF2α at Ser51; phosphorylated eIF2 competitively inhibits already-compromised eIF2B.
4. **Combined genetic and stress-dependent inhibition leads to** excessive or prolonged suppression of bulk translation with selective translation of ISR transcripts such as **ATF4** and **CHOP/DDIT3**.
5. **Chronic ISR dysregulation leads to** abnormal astrocyte differentiation, maturation, morphology, and homeostatic function; this glial selectivity is demonstrated, while its complete molecular basis remains incompletely resolved.
6. **Dysfunctional astrocytes lead to** impaired oligodendrocyte maturation and myelin maintenance; this non-cell-autonomous link is supported by coculture and animal evidence.
7. **Astrocyte/oligodendrocyte dysfunction leads to** paucity and rarefaction of myelin, axonal abnormalities, cavitation, and cystic disappearance of cerebral white matter.
8. **White-matter tract and cerebellar network failure leads to** ataxia, spasticity, weakness, seizures, cognitive/psychiatric manifestations, and progressive disability.
9. **Superimposed fever, infection, trauma, or seizures leads to** abrupt ISR demand beyond cellular reserve, resulting in episodic rapid deterioration, incomplete recovery, coma, or death. (herstine2024evaluationofsafety pages 1-2, hanson2024eif2blocalizationand pages 1-2, man2024proteomicdissectionof pages 1-2, bock2024invivobase pages 1-2)

The proximal biochemical process is **translation initiation/GEF dysfunction**, not a classic substrate-accumulating metabolic enzyme deficiency. ER stress, altered mitochondrial function, oxidative stress, amino-acid metabolism, and lipid/myelin metabolism are downstream or interacting processes. In the Eif2b5-I98M mouse, reduced GEF activity accompanies elevated ATF4 and CHOP, forebrain astrocytic GFAP abnormalities, displaced Bergmann glia, disrupted spinal-cord myelin, and clustered oligodendrocyte precursor cells. (terumitsu‐tsujita2020glialpathologyin pages 1-2)

The role of classical neuroinflammation appears secondary; VWM is not primarily autoimmune, and profound white-matter loss may occur without proportionate reactive gliosis. No disease-defining autoantibody or immune deficiency is known.

### 2024 molecular profiling

Quantitative proteomics in the **2b5ho** mouse found that cerebellar and cortical proteomes were abnormal before overt pathology, corpus-callosum changes appeared after pathology onset, and brainstem changes were transient, suggesting region-dependent compensation. Mouse changes partially overlapped human VWM brain proteomes. The authors' exact abstract conclusion was: **“the 2b5ho mouse brain proteome is affected in a region- and time-dependent manner.”** This is strong discovery evidence but does not yet establish which proteins are causal biomarkers. Published May 2024; DOI: https://doi.org/10.1007/s00018-024-05258-4. (man2024proteomicdissectionof pages 1-2)

A September 2024 cellular study showed cell-type-specific eIF2B-body composition and localization and divergent responses to chronic ISR and ISRIB. Its abstract states that **“a chronic ISR exerts cell-type specific differences.”** These data help explain selective glial vulnerability but were obtained in cell systems rather than a clinical cohort. DOI: https://doi.org/10.1016/j.isci.2024.110851. (hanson2024eif2blocalizationand pages 1-2)

Suggested GO annotations include *translation initiation*, *regulation of translational initiation*, *guanine nucleotide exchange factor activity*, *integrated stress response signaling*, *cellular response to ER stress*, *glial-cell differentiation*, *oligodendrocyte differentiation*, and *myelination*. Suggested Cell Ontology entities include **astrocyte**, **Bergmann glial cell**, **oligodendrocyte**, **oligodendrocyte precursor cell**, and secondarily **neuron/axon**.

## 7. Anatomical structures affected

The primary organ is the **central nervous system**. Cerebral/telencephalic white matter—often frontal and periventricular regions and the corpus callosum—is most severely affected. U-fibers may be relatively spared, particularly earlier. Cerebellar white matter and spinal-cord tracts can be involved; brainstem is often relatively preserved. Gray matter is affected less severely than white matter. Disease is generally diffuse and bilateral rather than unilateral. (man2024proteomicdissectionof pages 1-2, trevisan2021anelevenyearhistory pages 1-3)

Suggested UBERON terms are *brain white matter*, *cerebral hemisphere white matter*, *corpus callosum*, *cerebellar white matter*, *brainstem*, and *spinal cord white matter*. At the tissue level, nervous tissue, myelin, astroglial networks, oligodendroglial lineage, and axons are implicated. Relevant subcellular compartments include the **cytosol**, where eIF2B bodies and translation initiation operate, ribosomal/translation complexes, and ER-associated stress-signaling compartments. Suggested GO cellular components include *cytosol*, *eIF2B complex*, *ribosome*, *myelin sheath*, and *endoplasmic reticulum*.

## 8. Temporal development

Onset ranges from antenatal disease to senescence. Approximately **90%** present before 18 years and **60%** before four years. Expert stratification uses <12 months, 1–<2 years, 2–<4 years, 4–<8 years, 8–<18 years, and ≥18 years. (knaap2022therapytrialdesign pages 2-4, knaap2022therapytrialdesign pages 1-2)

- Antenatal/early infantile disease is usually rapidly progressive; median death was approximately **9 months** in the summarized natural-history data.
- Classic onset at 2–4 years commonly begins after initially normal or near-normal development, with ataxia and spasticity; median loss of walking was approximately **3 years** and median death approximately **9 years**.
- Later childhood/adolescent disease is heterogeneous.
- Adult-onset disease may progress slowly with motor, cognitive, psychiatric, ovarian, or stroke-like manifestations; reported median death was approximately **37 years**, but individual survival is highly variable. (knaap2022therapytrialdesign pages 2-4)

VWM is chronic and lifelong. Acute episodes may show partial or complete remission, but accumulated deficits usually produce a stepwise-progressive trajectory. Critical vulnerability windows include febrile illness, trauma, seizures, and surgery/anesthesia. Early-onset disease is prognostically more predictable; later-onset disease is less predictable.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two confirmed heterozygous parents, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial variant. Penetrance is high for clearly pathogenic biallelic genotypes but can be age-dependent; expressivity is markedly variable. No anticipation is expected. Parental mosaicism is theoretically possible but is not a characteristic mechanism.

Consanguinity increases the probability of homozygosity for rare alleles. The **EIF2B5 p.Arg195His** founder allele causes severe Cree leukoencephalopathy in Indigenous Cree populations and is explicitly recognized in current trial eligibility. Founder effects do not imply that VWM is restricted to any ethnicity. (bock2024invivobase pages 1-2, NCT05757141 chunk 1)

The exact worldwide prevalence and annual incidence remain unknown. VWM is rare and likely underdiagnosed, especially in adults. No robust overall carrier frequency, sex ratio departure from 1:1, or population-wide incidence per 100,000 was established. These should be recorded as **unknown**, not zero.

## 10. Diagnostics

### Clinical and imaging diagnosis

Suspect VWM in a patient with progressive ataxia/spasticity, relatively preserved early development, stress-provoked neurologic regression, ovarian insufficiency, or a compatible adult psychiatric/cognitive syndrome. MRI typically shows diffuse, symmetric cerebral white-matter T2 hyperintensity followed by rarefaction and cystic degeneration approaching CSF signal, with relative U-fiber and brainstem sparing. (knaap2022therapytrialdesign pages 2-4, trevisan2021anelevenyearhistory pages 1-3)

Definitive diagnosis combines:

1. compatible clinical phenotype;
2. characteristic brain MRI; and
3. **biallelic pathogenic/likely pathogenic variants in one EIF2B gene**, specifically EIF2B5 for VWM5.

The ongoing fosigotifator trial likewise requires clinical, molecular, and MRI-consistent diagnoses. (NCT05757141 chunk 1)

Routine blood, urine, and CSF studies are often nonspecific. CSF asialotransferrin:transferrin ratio has been proposed as a screening biomarker, but genetic confirmation is preferred. EEG, EMG, nerve-conduction testing, ophthalmologic testing, swallowing assessment, and endocrine/reproductive evaluation are directed by phenotype rather than diagnostic in isolation.

### Genetic testing strategy

A leukodystrophy panel containing **EIF2B1, EIF2B2, EIF2B3, EIF2B4, and EIF2B5**, or exome/genome sequencing with deletion/duplication analysis, is appropriate. Targeted familial-variant testing is suitable when variants are known. WES has broad utility in genetically heterogeneous white-matter disease; WGS can identify noncoding, structural, or poorly captured variants and was studied as first-line testing in LeukoSEQ. CMA, karyotype, FISH, mtDNA, and repeat-expansion testing are not routine VWM5 tests unless the differential indicates them.

Differential diagnoses include Alexander disease, metachromatic leukodystrophy, Krabbe disease, X-linked adrenoleukodystrophy, AARS2-related leukodystrophy/ovarioleukodystrophy, CSF1R-related leukoencephalopathy, mitochondrial leukodystrophies, POLR3-related disease, hypomyelinating disorders, toxic/metabolic leukoencephalopathy, multiple sclerosis, and vascular white-matter disease. Progressive cystic rarefaction plus stress sensitivity strongly favors VWM.

There is no universal newborn screening. At-risk relatives should receive cascade molecular testing; prenatal diagnosis and preimplantation genetic testing are possible after familial variants are established.

## 11. Outcome and prognosis

No reliable population-level 5- or 10-year survival percentage is available. Prognosis is driven principally by **age at onset, genotype severity, baseline function, and occurrence of stress-provoked episodes**. Episodic deterioration predicts a worse course independently of onset age. Infantile disease commonly causes early death; adult disease may remain stable for years or progress unpredictably. (knaap2022therapytrialdesign pages 2-4, trevisan2021anelevenyearhistory pages 5-6)

Major morbidity includes loss of ambulation and self-care, spasticity, dysphagia/aspiration, seizures, communication impairment, cognitive or psychiatric disability, and premature ovarian insufficiency. Recovery from an acute episode may be complete, partial, or absent, but there is no established reversal of chronic white-matter loss. Respiratory complications, aspiration, infection, seizures, and severe neurologic decompensation can contribute to death.

No validated prognostic blood biomarker is in routine use. MRI burden, motor scales, onset age, genotype, and episode history are currently more practical. The absence of validated intermediate biomarkers and unpredictability of later-onset disease are major clinical-trial challenges. (knaap2022therapytrialdesign pages 1-2)

## 12. Treatment

### Current care

No approved disease-modifying therapy was established in the reviewed clinical evidence. Management is multidisciplinary and supportive: physical and occupational therapy; speech/communication and swallowing therapy; mobility and seating aids; treatment of spasticity, seizures, pain, dystonia, reflux, constipation, and respiratory complications; nutritional support; reproductive-endocrine care; psychosocial support; and palliative care when appropriate. Suggested NCIT interventions include *Supportive Care*, *Physical Therapy*, *Occupational Therapy*, *Speech Therapy*, *Anticonvulsant Therapy*, *Enteral Nutrition*, and *Genetic Counseling*.

Patients should have individualized fever/infection and seizure action plans. Surgery and anesthesia require careful risk–benefit assessment, temperature control, hydration, analgesia, and avoidance of unnecessary physiologic stress.

### Clinical development

**Fosigotifator (ABBV-CLS-7262)** is an oral investigational eIF2B activator in **NCT05757141**, a nonrandomized, open-label Phase 1b/2 study. The study began March 13, 2023 and plans approximately **50** participants aged ≥6 months across adult and pediatric cohorts. It evaluates safety, tolerability, pharmacokinetics, and exploratory efficacy over a long follow-up. Registry URL: https://clinicaltrials.gov/study/NCT05757141. Recruitment status in the retrieved June 2026-verified record was recruiting; no efficacy results were yet available. (NCT05757141 chunk 1, NCT05757141 chunk 2)

### 2024 preclinical advances

- **Astrocyte-targeted AAV9-EIF2B5 gene supplementation:** treatment of Eif2b5 mouse models improved weight, motor function/gait, survival, and demyelination measures. The modified **gfaABC(1)D** astrocyte promoter gave the strongest rescue. Diffusion MRI fractional anisotropy was **0.427** in treated mice versus **0.403** untreated and **0.523** wild type. The exact abstract claim was **“significant rescue in body weight, motor function, gait normalization, life extension”** with evidence of attenuated demyelination. Published June 2024; DOI: https://doi.org/10.1016/j.ymthe.2024.03.034. This remains mouse evidence, not established human therapy. (herstine2024evaluationofsafety pages 8-11, herstine2024evaluationofsafety pages 1-2)
- **Adenine base editing:** neonatal intracerebroventricular AAV delivery corrected **45.9% ± 5.9%** of Eif2b5-R191H alleles in cortex, slightly increased mature astrocytes, partially normalized ISR in females, and improved female weight and grip strength, but did not rescue locomotion. Bystander editing and inadequate delivery to deep regions and oligodendrocytes remain barriers. Published May 2024; DOI: https://doi.org/10.1016/j.ymthe.2024.03.009. (bock2024invivobase pages 1-2)
- **Lithium:** improved motor behavior in mutant zebrafish but failed to provide convincing mouse benefit, increased some ISR transcripts paradoxically, and caused significant polydipsia. The authors concluded it was not a preferred development candidate. Published January 2024; DOI: https://doi.org/10.3389/fnins.2024.1275744. (witkamp2024lithiumeffectsin pages 1-2)
- **ISRIB/2BAct-class activators:** prior biochemical and mouse evidence shows that eIF2B activators can stabilize selected mutant complexes, restore residual activity, normalize ISR markers, and improve pathology. Response may depend on whether an allele destabilizes the complex or directly impairs catalysis; this is a potential genotype-guided treatment principle, not yet clinical pharmacogenomics. (knaap2022therapytrialdesign pages 13-13, herstine2024evaluationofsafety pages 1-2)

No surgical correction, stem-cell transplant, approved ASO/siRNA, immunotherapy, or clinically validated combination therapy currently exists.

## 13. Prevention

**Primary prevention:** inherited disease cannot be prevented after conception by lifestyle change. Reproductive options include carrier testing in at-risk families, partner testing, genetic counseling, prenatal diagnosis, donor gametes, and preimplantation genetic testing.

**Secondary prevention:** cascade testing can identify presymptomatic biallelic relatives. Early molecular diagnosis enables anticipatory care and avoidance of diagnostic delay, but no population newborn-screening program was identified.

**Tertiary prevention:** vaccination, infection precautions, prompt fever treatment, head protection, seizure control, safe anesthesia planning, hydration, and rapid evaluation after neurologic decline may reduce avoidable episodes and complications. Vaccines prevent triggering infections rather than VWM itself. No preventive medication has proven efficacy.

## 14. Other species and natural disease

No established naturally occurring veterinary counterpart, breed-specific syndrome, zoonotic transmission, or cross-species infectious risk was identified. VWM is not contagious. Orthologous **Eif2b5** function is evolutionarily conserved in vertebrates, enabling mouse and zebrafish modeling. Relevant taxa are **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)**, and **Danio rerio (7955)**. Veterinary relevance is principally comparative and experimental rather than a recognized common natural animal disease.

## 15. Model organisms and experimental systems

- **Eif2b5 mutant mice:** R132H, R191H, and I98M models span mild-to-severe disease. The spontaneous **I98M** homozygote shows small size, abnormal gait, infertility, seizures, shortened survival, elevated ATF4/CHOP, astrocyte/Bergmann-glia abnormalities, myelin disruption, and OPC clustering. These models reproduce ISR and glial pathology and support pharmacology, gene therapy, editing, imaging, and biomarker studies. Limitations include mutation-specific severity, imperfect reproduction of human lifespan/episodic triggers, and uneven vector delivery. (terumitsu‐tsujita2020glialpathologyin pages 1-2, herstine2024evaluationofsafety pages 1-2)
- **2b5ho mouse:** useful for temporal and regional proteomics; it only **partly** reproduces the human brain proteome, so shared changes are candidates rather than automatically causal human mechanisms. (man2024proteomicdissectionof pages 1-2)
- **Zebrafish eif2b5 mutants:** enable rapid developmental and motor screening; lithium's zebrafish benefit did not translate convincingly to mice, illustrating species-dependent pharmacology. (witkamp2024lithiumeffectsin pages 1-2)
- **Patient fibroblasts and iPSC-derived astrocytes:** useful for stress assays, ISR/mitochondrial phenotyping, and drug screening. They model patient genotype but lack intact white-matter architecture, vasculature, and long-range glial interactions.
- **Human post-mortem organotypic brain slices:** preserve multicellular white-matter architecture and can evaluate vector tropism and pathology, but donor variability, post-mortem effects, finite culture duration, and absence of systemic physiology limit interpretation.

## Evidence appraisal and key gaps

The strongest clinical evidence comes from expert natural-history synthesis, characteristic MRI–genotype correlations, and longstanding human genetic observations. Mechanistic confidence is highest for partial eIF2B dysfunction, ISR dysregulation, and primary astrocyte/secondary oligodendrocyte involvement. Evidence for specific downstream metabolic, immune, epigenetic, or modifier pathways is less mature. The most important 2024 advances—proteomics, AAV gene addition, and base editing—remain preclinical. Fosigotifator is the leading real-world disease-modifying clinical implementation, but efficacy data are not yet available. Major knowledge gaps include precise incidence/prevalence, EIF2B5-only phenotype frequencies, validated fluid biomarkers, standardized quality-of-life outcomes, long-term treatment effects, protective modifiers, and human safety/efficacy of gene or editing therapy.

References

1. (knaap2022therapytrialdesign pages 2-4): Marjo S. van der Knaap, Joshua L. Bonkowsky, Adeline Vanderver, Raphael Schiffmann, Ingeborg Krägeloh-Mann, Enrico Bertini, Genevieve Bernard, Seyed Ali Fatemi, Nicole I. Wolf, Elise Saunier-Vivar, Robert Rauner, Hanka Dekker, Pieter van Bokhoven, Peter van de Ven, and Prisca S. Leferink. Therapy trial design in vanishing white matter. Apr 2022. URL: https://doi.org/10.1212/nxg.0000000000000657, doi:10.1212/nxg.0000000000000657. This article has 35 citations.

2. (herstine2024evaluationofsafety pages 1-2): Jessica A. Herstine, Pi-Kai Chang, Sergiy Chornyy, Tamara J. Stevenson, Alex C. Sunshine, Ksenia Nokhrina, Jessica Rediger, Julia Wentz, Tatyana A. Vetter, Erika Scholl, Caleb Holaway, Nettie K. Pyne, Anna Bratasz, Stewart Yeoh, Kevin M. Flanigan, Joshua L. Bonkowsky, and Allison M. Bradbury. Evaluation of safety and early efficacy of aav gene therapy in mouse models of vanishing white matter disease. Jun 2024. URL: https://doi.org/10.1016/j.ymthe.2024.03.034, doi:10.1016/j.ymthe.2024.03.034. This article has 14 citations and is from a highest quality peer-reviewed journal.

3. (bock2024invivobase pages 1-2): Desirée Böck, Ilma M. Revers, Anastasia S.J. Bomhof, Anne E.J. Hillen, Claire Boeijink, Lucas Kissling, Sabina Egli, Miguel A. Moreno-Mateos, Marjo S. van der Knaap, Niek P. van Til, and Gerald Schwank. In vivo base editing of a pathogenic eif2b5 variant improves vanishing white matter phenotypes in mice. May 2024. URL: https://doi.org/10.1016/j.ymthe.2024.03.009, doi:10.1016/j.ymthe.2024.03.009. This article has 9 citations and is from a highest quality peer-reviewed journal.

4. (NCT05757141 chunk 1):  An Open-Label Exploratory Study of Fosigotifator in Participants With Vanishing White Matter Disease. Calico Life Sciences LLC. 2023. ClinicalTrials.gov Identifier: NCT05757141

5. (OpenTargets Search: vanishing white matter disease-EIF2B5): Open Targets Query (vanishing white matter disease-EIF2B5, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (trevisan2021anelevenyearhistory pages 1-3): Lucia Trevisan, Matteo Grazzini, Annalia Cianflone, Andrea Accogli, Cinzia Finocchi, Elisabetta Capello, Laura Saitta, Marina Grandis, Luca Roccatagliata, and Paola Mandich. An eleven-year history of vanishing white matter disease in an adult patient with no cognitive decline and eif2b5 mutations. a case report. Neurocase, 27:452-456, Nov 2021. URL: https://doi.org/10.1080/13554794.2021.1999984, doi:10.1080/13554794.2021.1999984. This article has 6 citations and is from a peer-reviewed journal.

7. (knaap2022therapytrialdesign pages 1-2): Marjo S. van der Knaap, Joshua L. Bonkowsky, Adeline Vanderver, Raphael Schiffmann, Ingeborg Krägeloh-Mann, Enrico Bertini, Genevieve Bernard, Seyed Ali Fatemi, Nicole I. Wolf, Elise Saunier-Vivar, Robert Rauner, Hanka Dekker, Pieter van Bokhoven, Peter van de Ven, and Prisca S. Leferink. Therapy trial design in vanishing white matter. Apr 2022. URL: https://doi.org/10.1212/nxg.0000000000000657, doi:10.1212/nxg.0000000000000657. This article has 35 citations.

8. (english2022a(dis)integratedstress pages 18-19): Alyssa M. English, Katelyn M. Green, and Stephanie L. Moon. A (dis)integrated stress response: genetic diseases of eif2α regulators. Wiley Interdisciplinary Reviews: RNA, Aug 2022. URL: https://doi.org/10.1002/wrna.1689, doi:10.1002/wrna.1689. This article has 36 citations.

9. (man2024proteomicdissectionof pages 1-2): Jodie H. K. Man, Parand Zarekiani, Peter Mosen, Mike de Kok, Donna O. Debets, Marjolein Breur, Maarten Altelaar, Marjo S. van der Knaap, and Marianna Bugiani. Proteomic dissection of vanishing white matter pathogenesis. Cellular and Molecular Life Sciences: CMLS, May 2024. URL: https://doi.org/10.1007/s00018-024-05258-4, doi:10.1007/s00018-024-05258-4. This article has 1 citations.

10. (hanson2024eif2blocalizationand pages 1-2): Filipe M. Hanson, Madalena I. Ribeiro de Oliveira, Alison K. Cross, K. Elizabeth Allen, and Susan G. Campbell. Eif2b localization and its regulation during the integrated stress response is cell-type specific. Sep 2024. URL: https://doi.org/10.1016/j.isci.2024.110851, doi:10.1016/j.isci.2024.110851. This article has 7 citations and is from a peer-reviewed journal.

11. (terumitsu‐tsujita2020glialpathologyin pages 1-2): Mika Terumitsu‐Tsujita, Hiroki Kitaura, Ikuo Miura, Yuji Kiyama, Fumiko Goto, Yoshiko Muraki, Shiho Ominato, Norikazu Hara, Anna Simankova, Norihisa Bizen, Kazuhiro Kashiwagi, Takuhiro Ito, Yasuko Toyoshima, Akiyoshi Kakita, Toshiya Manabe, Shigeharu Wakana, Hirohide Takebayashi, and Hironaka Igarashi. Glial pathology in a novel spontaneous mutant mouse of the eif2b5 gene: a vanishing white matter disease model. Journal of Neurochemistry, 154:25-40, Oct 2020. URL: https://doi.org/10.1111/jnc.14887, doi:10.1111/jnc.14887. This article has 26 citations and is from a domain leading peer-reviewed journal.

12. (NCT05757141 chunk 2):  An Open-Label Exploratory Study of Fosigotifator in Participants With Vanishing White Matter Disease. Calico Life Sciences LLC. 2023. ClinicalTrials.gov Identifier: NCT05757141

13. (herstine2024evaluationofsafety pages 8-11): Jessica A. Herstine, Pi-Kai Chang, Sergiy Chornyy, Tamara J. Stevenson, Alex C. Sunshine, Ksenia Nokhrina, Jessica Rediger, Julia Wentz, Tatyana A. Vetter, Erika Scholl, Caleb Holaway, Nettie K. Pyne, Anna Bratasz, Stewart Yeoh, Kevin M. Flanigan, Joshua L. Bonkowsky, and Allison M. Bradbury. Evaluation of safety and early efficacy of aav gene therapy in mouse models of vanishing white matter disease. Jun 2024. URL: https://doi.org/10.1016/j.ymthe.2024.03.034, doi:10.1016/j.ymthe.2024.03.034. This article has 14 citations and is from a highest quality peer-reviewed journal.

14. (witkamp2024lithiumeffectsin pages 1-2): Diede Witkamp, Ellen Oudejans, Leoni Hoogterp, Gino V. Hu-A-Ng, Kathryn A. Glaittli, Tamara J. Stevenson, Marleen Huijsmans, Truus E. M. Abbink, Marjo S. van der Knaap, and Joshua L. Bonkowsky. Lithium: effects in animal models of vanishing white matter are not promising. Frontiers in Neuroscience, Jan 2024. URL: https://doi.org/10.3389/fnins.2024.1275744, doi:10.3389/fnins.2024.1275744. This article has 3 citations and is from a peer-reviewed journal.

15. (trevisan2021anelevenyearhistory pages 5-6): Lucia Trevisan, Matteo Grazzini, Annalia Cianflone, Andrea Accogli, Cinzia Finocchi, Elisabetta Capello, Laura Saitta, Marina Grandis, Luca Roccatagliata, and Paola Mandich. An eleven-year history of vanishing white matter disease in an adult patient with no cognitive decline and eif2b5 mutations. a case report. Neurocase, 27:452-456, Nov 2021. URL: https://doi.org/10.1080/13554794.2021.1999984, doi:10.1080/13554794.2021.1999984. This article has 6 citations and is from a peer-reviewed journal.

16. (knaap2022therapytrialdesign pages 13-13): Marjo S. van der Knaap, Joshua L. Bonkowsky, Adeline Vanderver, Raphael Schiffmann, Ingeborg Krägeloh-Mann, Enrico Bertini, Genevieve Bernard, Seyed Ali Fatemi, Nicole I. Wolf, Elise Saunier-Vivar, Robert Rauner, Hanka Dekker, Pieter van Bokhoven, Peter van de Ven, and Prisca S. Leferink. Therapy trial design in vanishing white matter. Apr 2022. URL: https://doi.org/10.1212/nxg.0000000000000657, doi:10.1212/nxg.0000000000000657. This article has 35 citations.

## Artifacts

- [Edison artifact artifact-00](Leukoencephalopathy_With_Vanishing_White_Matter_5-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 10 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957873` (3 mentions) - the report calls it "if available"; MONDO calls it **leukoencephalopathy with vanishing white matter 5**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.