---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T14:40:11.425453'
end_time: '2026-09-06T14:52:08.816297'
duration_seconds: 717.39
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Idiopathic Hypereosinophilic Syndrome
  mondo_id: MONDO:0011895
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 63
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 3
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0011895
    reported_labels:
    - if available
    ontology_label: idiopathic hypereosinophilic syndrome
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Idiopathic_Hypereosinophilic_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Idiopathic Hypereosinophilic Syndrome
- **MONDO ID:** MONDO:0011895 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Idiopathic Hypereosinophilic Syndrome** covering all of the
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
- **Disease Name:** Idiopathic Hypereosinophilic Syndrome
- **MONDO ID:** MONDO:0011895 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Idiopathic Hypereosinophilic Syndrome** covering all of the
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


# Idiopathic Hypereosinophilic Syndrome: Disease-Characteristics Report

**Scope and evidence date.** This report focuses on idiopathic hypereosinophilic syndrome (iHES), not the broader group of all hypereosinophilic syndromes. Evidence available through 2024 is prioritized; selected 2025–2026 findings are clearly labeled as later developments. Many publications combine HES subtypes, so phenotype frequencies from mixed cohorts should not be interpreted as iHES-specific. PMID values were not present in the retrieved records; DOI and ClinicalTrials.gov URLs are therefore supplied rather than risking incorrect PMID assignment.

## Executive summary

iHES is an exclusion-defined, heterogeneous disorder in which persistent blood or tissue hypereosinophilia causes organ damage, but no reactive, autoimmune, lymphocytic-variant, or clonal/neoplastic cause can be established. Current ICC criteria require peripheral eosinophils ≥1.5 × 10⁹/L and ≥10% of leukocytes, attributable tissue injury, generally normal marrow morphology apart from eosinilia, and no defining clonal genetic abnormality. The old six-month waiting requirement is obsolete when organ injury demands prompt treatment. (caminati2024managingpatientswith pages 2-3, wang2023theinternationalconsensus pages 8-8)

The skin, respiratory tract, gastrointestinal tract, and cardiovascular system are most often involved. Cardiac inflammation, intracardiac thrombosis, endomyocardial fibrosis, thromboembolism, and neurologic injury are the most consequential complications. Corticosteroids remain first-line therapy; mepolizumab 300 mg subcutaneously every four weeks is the best-supported and, as of 2024, only biologic specifically approved for HES. (wang2023theinternationalconsensus pages 8-9, ezekwe2024biologicsinhypereosinophilic pages 3-4, jackson2022eosinophilsandeosinophilic pages 3-4)

| Domain | Key current finding | Quantitative data | Evidence type/year | Source DOI or NCT |
|---|---|---|---|---|
| Definition / ICC criteria | iHES requires persistent peripheral-blood hypereosinophilia, eosinophil-attributable tissue damage or dysfunction, exclusion of reactive, autoimmune, neoplastic, and lymphocytic-variant causes, generally normal marrow apart from eosinophilia, and no defining clonal genetic abnormality. | AEC ≥1.5 × 10⁹/L and eosinophils ≥10%; persistence commonly confirmed on ≥2 measurements at least 2 weeks apart. | International consensus classification, 2023; society statement, 2024 (wang2023theinternationalconsensus pages 8-8, caminati2024managingpatientswith pages 2-3) | [10.1002/ajh.26966](https://doi.org/10.1002/ajh.26966); [10.3390/cells13141180](https://doi.org/10.3390/cells13141180) |
| Epidemiology / prognosis | Population incidence is poorly characterized. After overt hematopoietic neoplasia is excluded, iHES is usually relatively indolent, but cardiac and thrombotic disease can be life-threatening. Adverse factors include age >60 years, cardiac involvement, anemia or thrombocytopenia, lymphopenia, high neutrophil-to-lymphocyte ratio, and hepatosplenomegaly. | Older population estimate for HES: 0.36 new cases per million person-years; long-term disease-related mortality in iHES: approximately 10%–15%; cytopenias: approximately 10%–20%. | Guideline, 2023; ICC-era review, 2023 (groh2023frenchguidelinesfor pages 5-7, wang2023theinternationalconsensus pages 8-9) | [10.1186/s13023-023-02696-4](https://doi.org/10.1186/s13023-023-02696-4); [10.1002/ajh.26966](https://doi.org/10.1002/ajh.26966) |
| Diagnostic exclusion genetics | Molecularly defined myeloid/lymphoid neoplasms and CEL-NOS must be excluded. Testing may use RT-PCR, FISH, karyotyping, targeted NGS, or RNA sequencing; flow cytometry and T-cell-receptor studies assess L-HES. Somatic CHIP variants require cautious interpretation and do not alone establish CEL. | Test for rearrangements involving **PDGFRA, PDGFRB, FGFR1, JAK2, FLT3**, and **ETV6::ABL1**; context-dependent testing includes **BCR::ABL1, KIT, JAK2 V617F, CALR**, and **MPL**. TCR clonality occurs in about 50% of L-HES and 17%–27% of otherwise unexplained eosinophilia. | Consensus/guideline and molecular-diagnostic review, 2023–2024 (nguyen2024clinicalandtherapeutic pages 9-10, wang2023theinternationalconsensus pages 8-8, caminati2024managingpatientswith pages 8-10, nguyen2024clinicalandtherapeutic pages 5-7) | [10.1002/ajh.26966](https://doi.org/10.1002/ajh.26966); [10.3390/cells13141180](https://doi.org/10.3390/cells13141180); [10.3390/cancers16071383](https://doi.org/10.3390/cancers16071383) |
| Major organ phenotypes | Most often involves skin, gastrointestinal tract, lungs/upper airways, and cardiovascular system; neurologic, muscular, joint, and endocrine disease is less frequent. Complications include myocarditis, intracardiac thrombus, endomyocardial fibrosis, pulmonary infiltrates/fibrosis, dermatitis or urticaria, enteritis/colitis, embolic stroke, and peripheral neuropathy. | Broad HES evidence reports cutaneous presentation in approximately 37%, cardiovascular complications in 5%, and neurologic complications in 4%; these estimates are not iHES-specific. | Clinical reviews/cohort synthesis, 2021–2025 (mora2025mepolizumabforhypereosinophilic pages 1-2, wang2023theinternationalconsensus pages 8-9, valent2021eosinophilsandeosinophilassociated pages 6-8, jackson2022eosinophilsandeosinophilic pages 3-4) | [10.1007/s00281-021-00863-y](https://doi.org/10.1007/s00281-021-00863-y); [10.1002/ajh.26966](https://doi.org/10.1002/ajh.26966) |
| Mepolizumab phase 3 | Add-on mepolizumab is the only biologic approved for HES as of 2024. In PDGFRA-negative, non-myeloid HES, it reduced clinical flares and improved most assessed symptom domains without a new safety signal. | 300 mg SC every 4 weeks for 32 weeks; 108 participants; approximately 50% reduction in patients experiencing flares versus placebo; symptom improvement in 5 of 6 domains. | Randomized, double-blind phase 3 trial; evidence summarized in 2024 (ezekwe2024biologicsinhypereosinophilic pages 3-4, NCT02836496 chunk 1) | [NCT02836496](https://clinicaltrials.gov/study/NCT02836496); [10.1016/j.iac.2024.07.003](https://doi.org/10.1016/j.iac.2024.07.003) |
| Benralizumab phase 2 / status through 2024 | Benralizumab depletes IL-5Rα-positive eosinophils through antibody-dependent cellular cytotoxicity. Phase 2 results supported hematologic and clinical activity in refractory PDGFRA-negative HES, but it remained investigational for HES through 2024; phase 3 NATRON was ongoing. | 30 mg SC every 4 weeks; >50% AEC reduction in 9/10 versus 3/10 placebo recipients; 17/19 showed hematologic or clinical improvement. JAK2-mutated cases did not respond, and all L-HES cases relapsed in the reported small study. | Randomized phase 2 plus extension; 2024 status review (ezekwe2024biologicsinhypereosinophilic pages 3-4) | [NCT04191304](https://clinicaltrials.gov/study/NCT04191304); [10.1016/j.iac.2024.07.003](https://doi.org/10.1016/j.iac.2024.07.003) |
| Post-2024 real-world iHES | **Later evidence:** a small retrospective iHES cohort found marked eosinophil suppression, elimination of recorded flares, improved pulmonary function, and substantial corticosteroid sparing with mepolizumab or benralizumab. The uncontrolled sample does not establish comparative efficacy. | n=11; mepolizumab 300 mg/month (n=8) or benralizumab 30 mg every 4 weeks (n=3); median AEC 3,000→50/µL at 12 months (p=0.0002); flares 11/11→0/11; mean FEV₁ gain 857±594 mL in 8 patients with asthma; 82% discontinued oral corticosteroids; no treatment-related adverse events reported. | Retrospective real-world cohort, published 2025; treatment period 2019–2023 (papaioannou2025biologicagentsin pages 4-6, papaioannou2025biologicagentsin pages 1-2) | [10.3390/ph18040543](https://doi.org/10.3390/ph18040543) |
| Major evidence gaps | iHES remains an exclusion-defined and probably biologically heterogeneous syndrome. No reproducible causal germline variant, protective factor, validated iHES-specific molecular signature, epigenetic lesion, or robust gene–environment interaction has been established. Prospective natural-history, ancestry-stratified epidemiology, standardized quality-of-life, pediatric, comparative-effectiveness, and long-term safety data remain limited. | Open Targets listed 0 disease–target associations for MONDO:0011895 at search time; contemporary statements describe the prospective nonmalignant HES burden as unknown. | Database result and expert statements, 2024–2025 (OpenTargets Search: idiopathic hypereosinophilic syndrome, caminati2024managingpatientswith pages 2-3, longhino2025clinicalandimmunological pages 1-2) | [Open Targets](https://platform.opentargets.org/); [10.3390/cells13141180](https://doi.org/10.3390/cells13141180) |


*Table: Concise evidence map of current iHES definition, diagnostic exclusions, clinical burden, prognosis, biologic-treatment data, and major knowledge gaps. Post-2024 findings are explicitly separated from evidence available through 2024.*

## 1. Disease information

### Definition and classification

- **Hypereosinophilia (HE):** absolute eosinophil count (AEC) ≥1.5 × 10⁹/L. Contemporary statements usually confirm persistence on at least two measurements separated by ≥2 weeks; moderate HE is 1.5–5.0 × 10⁹/L and severe HE is >5.0 × 10⁹/L. (caminati2024managingpatientswith pages 2-3)
- **HES:** HE plus organ damage or dysfunction attributable to eosinophilic infiltration or eosinophil-derived products.
- **iHES:** HES for which no reactive, autoimmune, neoplastic, or lymphocytic-variant cause is found after adequate investigation. It is a diagnosis of exclusion rather than a single molecular disease. (wang2023theinternationalconsensus pages 8-8)
- **HE of unknown significance (HEus):** unexplained HE without attributable organ damage; it is not iHES. (caminati2024managingpatientswith pages 2-3)

**Important boundaries:** FIP1L1::PDGFRA-positive disease and other tyrosine-kinase-fusion disorders are myeloid/lymphoid neoplasms, not iHES. Lymphocytic-variant HES has an aberrant cytokine-producing T-cell population. Reactive HES has a recognizable trigger such as infection, drug exposure, allergy, autoimmune disease, or malignancy. EGPA requires a vasculitic clinical context and is not classified as iHES. Organ-restricted eosinophilic disorders lack systemic HES involvement. (roufosse2007hypereosinophilicsyndromes pages 1-2, nguyen2024clinicalandtherapeutic pages 9-10, wang2023theinternationalconsensus pages 8-8)

### Identifiers and synonyms

- **MONDO:** MONDO:0011895, *idiopathic hypereosinophilic syndrome*, confirmed in Open Targets, although no associated target was returned at search time. (OpenTargets Search: idiopathic hypereosinophilic syndrome)
- **Common labels:** idiopathic HES, iHES, HES-I, idiopathic hypereosinophilic syndrome.
- **Coding caution:** ICD and MeSH resources often code the broader HES category rather than the rigorously exclusion-defined idiopathic subtype. ICD-10-CM commonly uses **D72.11, hypereosinophilic syndrome**; local verification is recommended before using it as an iHES-specific identifier. A uniquely verified OMIM entry was not identified, consistent with the absence of a defined Mendelian cause.
- The evidence summarized here is **aggregated disease-level literature and trial evidence**, not individual EHR-derived data, except where retrospective clinical cohorts are explicitly described.

## 2. Etiology

iHES has **no established initiating cause**. “Idiopathic” should be assigned only after excluding secondary/reactive and clonal conditions. No reproducible causal germline variant, susceptibility locus, inheritance pattern, founder allele, or protective allele is established. Somatic variants associated with clonal hematopoiesis may occur, especially with age, but do not by themselves prove chronic eosinophilic leukemia. (wang2023theinternationalconsensus pages 8-8, nguyen2024clinicalandtherapeutic pages 9-10)

Potential environmental or infectious causes—medications, helminths, fungi, allergic exposures, and infections—are differential diagnoses rather than demonstrated risk factors for genuine iHES. Drug-associated eosinophilia often begins 2–8 weeks after exposure; implicated classes include antibiotics, antiepileptics, NSAIDs, sulfonamides, allopurinol, immune-checkpoint inhibitors, and occasionally dupilumab. Identifying such a trigger reclassifies the condition as reactive rather than idiopathic. (groh2023frenchguidelinesfor pages 5-7)

No validated lifestyle risk or protective factor involving smoking, diet, alcohol, exercise, occupation, or pollution is known. Likewise, no robust iHES-specific gene–environment interaction has been demonstrated. Apparent associations with atopy or infection require caution because they can represent alternative diagnoses.

## 3. Phenotypes

Clinical expression is adult-predominant but can occur at any age. Severity ranges from mild chronic symptoms to rapidly fatal cardiac, thrombotic, or neurologic disease. AEC magnitude correlates imperfectly with severity; activation state and tissue infiltration matter more. (roufosse2007hypereosinophilicsyndromes pages 1-2, groh2023frenchguidelinesfor pages 5-7)

- **Laboratory:** persistent eosinophilia—suggest **HP:0001880, Eosinophilia**. Recent molecularly evaluated cohorts had median AECs around 3.0–3.9 × 10⁹/L. Mild cytopenias occur in approximately 10%–20%, but prominent anemia, thrombocytopenia, blasts, or dysplasia should raise concern for neoplasia. (wang2023theinternationalconsensus pages 8-9)
- **Skin:** pruritus, eczema/dermatitis, urticaria, angioedema, erythroderma, nodules, or ulceration; generally fluctuating or relapsing. Suggested HPO: **Pruritus, Urticaria, Eczema, Angioedema, Erythroderma**. Mixed-HES evidence estimates cutaneous presentation near 37%, not specifically iHES. (mora2025mepolizumabforhypereosinophilic pages 1-2, jackson2022eosinophilsandeosinophilic pages 3-4)
- **Respiratory:** cough, dyspnea, asthma-like disease, pulmonary infiltrates, pleural effusion, and eventually fibrosis. Suggested HPO: **Dyspnea, Cough, Pulmonary infiltrates, Pleural effusion, Pulmonary fibrosis, Asthma**. (papaioannou2025biologicagentsin pages 1-2, jackson2022eosinophilsandeosinophilic pages 3-4)
- **Gastrointestinal:** abdominal pain, diarrhea, enteritis, colitis, or eosinophilic gastroenteritis. Suggested HPO: **Abdominal pain, Diarrhea, Gastrointestinal inflammation**. (roufosse2007hypereosinophilicsyndromes pages 1-2, jackson2022eosinophilsandeosinophilic pages 3-4)
- **Cardiovascular:** myocarditis, pericarditis, intracavitary thrombus, endomyocardial fibrosis, valvular entrapment/regurgitation, arrhythmia, and heart failure. Suggested HPO: **Myocarditis, Pericarditis, Intracardiac thrombus, Endomyocardial fibrosis, Cardiac arrhythmia, Heart failure**. Broad recent HES estimates place cardiovascular complications near 5%, but historic cohorts were substantially higher and subtype ascertainment differs. (mora2025mepolizumabforhypereosinophilic pages 1-2, valent2021eosinophilsandeosinophilassociated pages 6-8, jackson2022eosinophilsandeosinophilic pages 3-4)
- **Neurologic/vascular:** embolic stroke, encephalitis, peripheral neuropathy, arterial or venous thrombosis. Suggested HPO: **Ischemic stroke, Encephalitis, Peripheral neuropathy, Venous thrombosis, Arterial thrombosis**. Mixed-HES neurologic complication estimates near 4% are not iHES-specific. (mora2025mepolizumabforhypereosinophilic pages 1-2, valent2021eosinophilsandeosinophilassociated pages 6-8)
- **Other:** hepatomegaly, splenomegaly, ocular inflammation, musculoskeletal and endocrine involvement are reported but less common. Hepatosplenomegaly or cytopenias should also prompt renewed evaluation for clonal disease. (roufosse2007hypereosinophilicsyndromes pages 1-2, wang2023theinternationalconsensus pages 8-9)

Symptoms, chronic glucocorticoid exposure, diagnostic delay, fatigue, organ dysfunction, and fear of relapse impair daily function. The 2024 SIAAIC statement calls the quality-of-life effect substantial, but validated iHES-specific EQ-5D, SF-36, or PROMIS norms and per-phenotype effect sizes remain unavailable. (caminati2024managingpatientswith pages 2-3)

## 4. Genetic and molecular information

There is **no accepted causal gene or pathogenic variant for iHES**, no Mendelian inheritance, and therefore no meaningful iHES carrier frequency, penetrance, anticipation, or founder effect. Open Targets returned zero disease–target associations for MONDO:0011895, emphasizing the current evidence gap rather than proving absence of biology. (OpenTargets Search: idiopathic hypereosinophilic syndrome)

Molecular findings that **exclude** iHES include rearrangements involving **PDGFRA, PDGFRB, FGFR1, JAK2, FLT3**, and **ETV6::ABL1**. Context-specific testing includes **BCR::ABL1, KIT, JAK2 V617F, CALR**, and **MPL**. CEL-NOS may harbor mutations in **ASXL1, DNMT3A, EZH2, TET2, SRSF2, SETBP1**, or **CBL**, accompanied by supportive morphology. These are somatic neoplastic or CHIP-associated findings, not established iHES variants. (nguyen2024clinicalandtherapeutic pages 9-10, caminati2024managingpatientswith pages 8-10)

No validated iHES-specific modifier gene, DNA-methylation signature, histone alteration, chromosomal abnormality, metabolomic signature, lipidomic profile, or spatial/single-cell atlas was established through 2024. A 2025 pilot of 21 patients found elevated eosinophil cationic protein and κ free light chains and correlations with AEC and steroid use, but these remain exploratory biomarkers rather than causal molecular lesions. (longhino2025clinicalandimmunological pages 1-2)

## 5. Environmental information

Environmental, occupational, dietary, smoking, alcohol, or exercise exposures have not been shown to cause iHES. Diagnostic assessment must nevertheless investigate travel, helminth exposure—especially *Strongyloides* before corticosteroids—new drugs, supplements, allergic disease, immunocompromise, and malignancy. A positive causal exposure generally changes the diagnosis to secondary/reactive eosinophilia. (taurisano2025hypereosinophiliaclinicaland pages 6-7, groh2023frenchguidelinesfor pages 5-7, nguyen2024clinicalandtherapeutic pages 5-7)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **An unknown initiating lesion or dysregulated immune stimulus** leads to excessive eosinophil production, survival, or activation; this initiating step is **inferred and undefined in iHES**.
2. Increased **IL-5–IL-5Rα**, with contributions from IL-3 and GM-CSF, leads to eosinophil-lineage differentiation, marrow release, priming, and prolonged survival. (nguyen2024clinicalandtherapeutic pages 4-5, valent2021eosinophilsandeosinophilassociated pages 4-5)
3. IL-4/IL-13/TNF-driven eotaxins **CCL11, CCL24, and CCL26** acting through **CCR3** lead to eosinophil chemotaxis into target tissues. (nguyen2024clinicalandtherapeutic pages 4-5, valent2021eosinophilsandeosinophilassociated pages 4-5)
4. Tissue accumulation and activation lead to degranulation and extracellular deposition of **MBP1/2, ECP, eosinophil peroxidase, and EDN**, plus cytokines, leukotrienes, prostaglandins, and DNA traps. (taurisano2025hypereosinophiliaclinicaland pages 1-2, valent2021eosinophilsandeosinophilassociated pages 4-5)
5. These mediators lead to epithelial/endothelial injury and branch into: **(a)** inflammation, edema, bronchoconstriction, mucus production and tissue dysfunction; **(b)** platelet/endothelial activation, PAI-2 activity and antifibrinolysis leading to thrombosis; and **(c)** fibroblast activation, TGF signaling and remodeling leading to fibrosis. Some organ-specific links are mechanistically inferred from broader eosinophil biology rather than demonstrated uniquely in iHES. (valent2021eosinophilsandeosinophilassociated pages 6-8, valent2021eosinophilsandeosinophilassociated pages 8-10)
6. Persistent injury leads to myocarditis/endomyocardial fibrosis and heart failure; pulmonary infiltrates/fibrosis; dermatitis; enteritis/colitis; microvascular injury, thromboembolism, stroke, or neuropathy. (valent2021eosinophilsandeosinophilassociated pages 6-8, jackson2022eosinophilsandeosinophilic pages 3-4)

**Upstream processes:** eosinophilopoiesis, cytokine signaling, survival and trafficking. **Downstream processes:** degranulation, oxidative/cytotoxic injury, inflammation, coagulation, thrombosis, remodeling and fibrosis.

Suggested GO biological-process terms include **eosinophil differentiation**, **eosinophil migration**, **eosinophil activation**, **leukocyte chemotaxis**, **cytokine-mediated signaling pathway**, **inflammatory response**, **blood coagulation**, **wound healing**, and **fibroblast proliferation**. Suggested Cell Ontology terms include **eosinophil (CL:0000771)**, eosinophil progenitor, **CD4-positive T cell**, type-2 innate lymphoid cell, mast cell, basophil, natural-killer cell, fibroblast, endothelial cell, and platelet. Cytokine-producing cells can include TH2 cells, ILC2s, mast cells, mesenchymal cells, basophils, NK cells, and eosinophils themselves. (nguyen2024clinicalandtherapeutic pages 4-5, groh2023frenchguidelinesfor pages 2-4)

No iHES-specific energy-metabolic defect, organelle dysfunction, autophagy lesion, or reproducible epigenomic/multi-omic mechanism is established.

## 7. Anatomical structures affected

Primary systems are hematopoietic/bone marrow and circulating blood, followed by skin, lung and upper airways, gastrointestinal tract, heart/endocardium/myocardium, vascular endothelium, and central or peripheral nervous systems. Suggested UBERON concepts include **bone marrow, blood, skin, lung, bronchus, gastrointestinal tract, heart, myocardium, endocardium, blood vessel, brain**, and **peripheral nerve**. (nguyen2024clinicalandtherapeutic pages 5-7, wang2023theinternationalconsensus pages 8-9)

At tissue level, eosinophils infiltrate epithelium, lamina propria, interstitium, myocardium/endocardium, and perivascular or neural tissues. Histology may show intact eosinophils or only extracellular MBP/EPX after cytolysis. Relevant GO cellular components include **eosinophil granule**, secretory granule lumen, extracellular region, plasma membrane/IL-5 receptor complex, and nucleus for extracellular DNA-trap formation. Lateralization is not characteristic; pulmonary, cutaneous, vascular, and neurologic lesions may be focal, multifocal, unilateral, or bilateral depending on the affected organ. (caminati2024managingpatientswith pages 2-3, valent2021eosinophilsandeosinophilassociated pages 4-5)

## 8. Temporal development

Onset is commonly young-to-middle adulthood but spans pediatric to geriatric ages. It is usually subacute or insidious, although myocarditis, thrombosis, or neurologic injury may present acutely. The course is heterogeneous—chronic persistent, fluctuating, episodic, or relapsing during treatment taper. (roufosse2007hypereosinophilicsyndromes pages 1-2, groh2023frenchguidelinesfor pages 5-7)

There is no formal staging system. A useful clinical sequence is: uncomplicated HE → symptomatic eosinophilic infiltration → reversible organ dysfunction → thrombotic/fibrotic irreversible damage. This is a management framework, not validated staging. Remission is usually treatment-induced; spontaneous durable remission is insufficiently quantified. The key therapeutic window is before cardiac thrombosis/fibrosis or permanent neurologic injury. Current experts emphasize simultaneous etiologic investigation and organ-damage assessment rather than waiting months to satisfy historical duration criteria. (groh2023frenchguidelinesfor pages 5-7, nguyen2024clinicalandtherapeutic pages 5-7)

## 9. Inheritance and population

The population incidence and prevalence of iHES are unknown. An older estimate for all HES was approximately **0.36 new cases per million persons per year**, which should not be treated as iHES-specific. Historic HES series reported a male:female ratio of 4–9:1, but this was strongly influenced by the nearly male-restricted FIP1L1::PDGFRA neoplasm; contemporary iHES should not be assumed to share that ratio. (roufosse2007hypereosinophilicsyndromes pages 1-2, groh2023frenchguidelinesfor pages 5-7)

No consistent ethnic, ancestry, geographic, consanguinity, or familial enrichment is established for iHES. Because no causal germline lesion is defined, inheritance, penetrance, mosaicism, carrier frequency, prenatal testing, and cascade genetic screening are not applicable.

## 10. Diagnostics

### Current diagnostic criteria

1. Confirm persistent PB HE—typically AEC ≥1.5 × 10⁹/L on two occasions ≥2 weeks apart; ICC additionally uses ≥10% eosinophils.
2. Demonstrate organ damage/dysfunction attributable to eosinophils or eosinophil products.
3. Exclude reactive, infectious, allergic, drug-related, autoimmune/vasculitic, and malignant causes.
4. Exclude L-HES and clonal/neoplastic eosinophilia.
5. Show marrow that is generally normal apart from increased eosinophils and no defining clonal molecular abnormality. (wang2023theinternationalconsensus pages 8-8, caminati2024managingpatientswith pages 2-3)

### Recommended work-up

- **Initial tests:** serial CBC/differential and smear; renal/hepatic chemistry; inflammatory markers; immunoglobulins/IgE; medication, travel, infection, allergy and immune-deficiency assessment; *Strongyloides* IgG and stool parasite testing where epidemiologically appropriate. (taurisano2025hypereosinophiliaclinicaland pages 6-7, nguyen2024clinicalandtherapeutic pages 5-7)
- **Hematologic evaluation:** bone-marrow aspirate/biopsy, morphology, fibrosis and blast assessment; flow cytometry; karyotype; FISH/PCR for FIP1L1::PDGFRA and other kinase fusions; targeted myeloid NGS or RNA sequencing when standard testing is negative. (nguyen2024clinicalandtherapeutic pages 9-10, caminati2024managingpatientswith pages 8-10)
- **L-HES:** T-cell immunophenotyping and TCR rearrangement. Typical clues are an sCD3−CD4+ population, elevated IL-4/IL-5, IgE and TARC. TCR clonality alone is not specific: it occurs in roughly 17%–27% of otherwise unexplained eosinophilia, while only about half of L-HES shows demonstrable clonality. (nguyen2024clinicalandtherapeutic pages 9-10, caminati2024managingpatientswith pages 8-10)
- **Organ staging:** troponin, ECG and echocardiography; cardiac MRI if myocarditis/fibrosis is suspected; chest CT and pulmonary-function tests; PET/CT where malignancy or organomegaly is a concern; GI endoscopy/biopsy, skin biopsy, neurologic examination/EMG or organ-specific imaging as indicated. (nguyen2024clinicalandtherapeutic pages 5-7)
- **Tissue HE:** extensive infiltration, >20% eosinophils among marrow nucleated cells, or marked extracellular eosinophil-protein deposition can support tissue involvement. (caminati2024managingpatientswith pages 2-3)

The differential includes parasitic infection, drug reaction/DRESS, allergy/atopy, ABPA, autoimmune disease, EGPA, eosinophilic GI or pulmonary disease, adrenal insufficiency, solid tumor/lymphoma, systemic mastocytosis, L-HES, MLN with tyrosine-kinase fusion, CEL-NOS, AML, and other MPN/MDS entities. Population screening, newborn screening, and screening of asymptomatic relatives are not indicated.

## 11. Outcome and prognosis

After overt hematopoietic neoplasia is excluded, iHES is often indolent, but long-term disease-related mortality is estimated at **10%–15%**. Poorer prognosis is associated with age >60 years, cardiac involvement, anemia or thrombocytopenia, lymphopenia, high neutrophil-to-lymphocyte ratio, and hepatosplenomegaly. (wang2023theinternationalconsensus pages 8-9)

Major causes of morbidity are irreversible heart failure/endomyocardial fibrosis, intracardiac or systemic thrombosis, stroke, pulmonary fibrosis, neuropathy, chronic GI disease, recurrent flares, and treatment toxicity. Cardiac injury is the most important preventable threat. Historic survival estimates are not applicable to modern molecularly classified iHES because older cohorts mixed neoplastic and idiopathic disorders. (roufosse2007hypereosinophilicsyndromes pages 1-2, wilkins2005hypereosinophilicsyndromean pages 1-2)

## 12. Treatment

### Strategy

- **Urgent organ-threatening disease:** initiate systemic glucocorticoids promptly while etiologic work-up continues. Corticosteroids usually lower AEC and improve dysfunction rapidly; taper after clinical control and AEC <1.5 × 10⁹/L. Approximately 20% are resistant or intolerant. (wang2023theinternationalconsensus pages 8-9)
- **Steroid-dependent/refractory iHES:** favor eosinophil-targeted biologic therapy, especially mepolizumab. Conventional alternatives include hydroxyurea, interferon-α, cyclosporine, methotrexate or other immunosuppressants, selected according to phenotype and toxicity. Alemtuzumab and allogeneic transplantation are reserved for exceptional refractory disease because of substantial risk. (curtis2016hypereosinophilicsyndrome pages 10-11, nguyen2024clinicalandtherapeutic pages 17-19)
- **Genotype-directed correction:** imatinib is highly effective for PDGFRA/PDGFRB-rearranged disease, but such patients do **not** have iHES. Empiric imatinib has limited relevance after comprehensive negative molecular testing.

### Biologics and trials

- **Mepolizumab**—anti-IL-5; suggested NCIt concept: *Mepolizumab*. In phase 3 NCT02836496, 108 patients received 300 mg SC every four weeks for 32 weeks; it reduced clinical flares by approximately 50% versus placebo and improved five of six symptom domains without a new safety signal. It was the only HES-approved biologic as of 2024. (ezekwe2024biologicsinhypereosinophilic pages 3-4, NCT02836496 chunk 1)
- **Benralizumab**—anti-IL-5Rα with NK-cell-mediated antibody-dependent cytotoxicity; suggested NCIt concept: *Benralizumab*. A small phase 2 study found >50% AEC reduction in 9/10 treated versus 3/10 placebo patients, with hematologic/clinical improvement in 17/19 during extension. It remained investigational for HES through 2024; phase 3 NATRON was NCT04191304. (ezekwe2024biologicsinhypereosinophilic pages 3-4)
- **Depemokimab**, long-acting anti-IL-5, is being tested every six months in phase 3 NCT05334368; efficacy results were not available in the retrieved 2024-era evidence. (ezekwe2024biologicsinhypereosinophilic pages 3-4)
- **Dupilumab**, anti-IL-4Rα, is being studied as add-on therapy for persistent symptoms despite eosinophil-depleting biologics in phase 2 NCT06477653. It is not established or approved as primary iHES therapy, and IL-4R blockade can itself be associated with blood eosinophilia. (NCT06477653 chunk 1, ezekwe2024biologicsinhypereosinophilic pages 9-10)

**Later real-world development (published 2025):** among 11 carefully investigated iHES patients, mepolizumab 300 mg/month or benralizumab 30 mg every four weeks reduced median AEC from 3,000 to 50/µL at 12 months, eliminated observed flares, allowed 82% to discontinue oral steroids, and improved mean FEV₁ by 857 ± 594 mL in eight patients with asthma; no treatment-related adverse events were reported. The uncontrolled, very small cohort cannot establish comparative efficacy. (papaioannou2025biologicagentsin pages 4-6, papaioannou2025biologicagentsin pages 1-2)

There is no validated pharmacogenomic dosing algorithm, gene therapy, RNA therapy, routine surgery, or approved cell therapy for iHES. Surgery is complication-directed—for example, valve or thrombotic sequelae—not disease-modifying. Rehabilitation, pulmonary therapy, cardiac care, thrombosis management, vaccination, bone protection and infection-risk mitigation should be individualized.

## 13. Prevention

No primary prevention exists because the initiating cause is unknown. There is no iHES vaccine, carrier screening, prenatal test, or population-screening program.

Secondary prevention consists of early recognition of persistent HE, prompt exclusion of *Strongyloides* and drug causes, and simultaneous screening for cardiac, pulmonary, neurologic and thrombotic injury. Tertiary prevention includes maintaining eosinophil control, minimizing cumulative corticosteroid exposure, cardiac surveillance, managing thrombosis according to standard indications, and monitoring for relapse and treatment toxicity. Early eosinophil-lowering therapy is intended to prevent irreversible organ damage. (groh2023frenchguidelinesfor pages 5-7, wang2023theinternationalconsensus pages 8-9)

## 14. Other species and natural disease

No naturally occurring animal disorder is established as a faithful ortholog of human iHES. Dogs, cats, horses, and other species can develop eosinophilic syndromes, but these are heterogeneous veterinary conditions and cannot be mapped directly to MONDO:0011895 without species-specific evidence. There is no zoonotic transmission. Relevant conserved genes/pathways include **IL5, IL5RA, CCR3, CCL11**, GATA factors, and the β-common cytokine-receptor pathway, but conservation of eosinophil biology does not establish shared idiopathic etiology.

## 15. Model organisms

- **IL-5-transgenic mice** (*Mus musculus*, NCBI Taxon 10090) develop marked, lineage-selective eosinophilia—reported as ≥65- to 265-fold above littermates—with eosinophils in marrow, spleen, lung, lymphoid tissue and gut. These models demonstrate that IL-5 is sufficient for eosinophil differentiation and expansion. Their major limitation is that some animals remain macroscopically well apart from splenomegaly, showing that eosinophilia alone does not fully reproduce human iHES organ injury.
- **FIP1L1-PDGFRA plus IL-5 models** produce HES/CEL-like disease and demonstrate cooperation between a myeloid oncogenic driver and cytokine signaling. They model neoplastic eosinophilia, not idiopathic HES.
- **Eosinophil-deficient mice** can have normal lifespan without spontaneous illness, helping evaluate eosinophil function but not modeling HES. (wilkins2005hypereosinophilicsyndromean pages 2-4, jackson2022eosinophilsandeosinophilic pages 3-4)

These systems are useful for eosinophilopoiesis, trafficking, granule-mediated injury, fibrosis, thrombosis and therapeutic target validation. None recreates the unknown initiating lesion or full phenotypic heterogeneity of iHES. No validated iHES-specific zebrafish, Drosophila, organoid, patient-derived iPSC, or CRISPR-screen model was identified.

## Authoritative interpretation and evidence gaps

Current expert consensus is that the most urgent practical problems are diagnostic delay, incomplete phenotyping, and failure to detect silent organ injury—not simply the eosinophil count. A multidisciplinary “two-track” approach should investigate etiology and organ damage simultaneously. (caminati2024managingpatientswith pages 2-3, groh2023frenchguidelinesfor pages 5-7, nguyen2024clinicalandtherapeutic pages 5-7)

The central conceptual limitation is that iHES is likely a residual category containing several undiscovered endotypes. Accordingly, absence of a recognized fusion or reactive trigger does not prove a single shared mechanism. Prospective natural-history cohorts, ancestry-stratified epidemiology, standardized patient-reported outcomes, pediatric data, serial tissue and single-cell profiling, and head-to-head biologic studies remain major unmet needs.

### Selected exact abstract quotations

> “Hypereosinophilic syndrome (HES) encompasses a heterogeneous and complex group of different subtypes within the wider group of hypereosinophilic disorders.” — Caminati et al., published July 2024, DOI: https://doi.org/10.3390/cells13141180. (caminati2024managingpatientswith pages 2-3)

> “HE may be associated with tissue or organ damage and, in this case, the disorder is classified as hypereosinophilic syndrome (HES).” — Stella et al., published January 2021, DOI: https://doi.org/10.3390/ijms22020486. (nguyen2024clinicalandtherapeutic pages 4-5)

> “Mepolizumab is identified as the only biologic with regulatory approval for HES.” — evidence synthesis from Ezekwe et al., published November 2024, DOI: https://doi.org/10.1016/j.iac.2024.07.003. (ezekwe2024biologicsinhypereosinophilic pages 3-4)

These quotations support broad HES concepts; they should not be used to imply a known iHES-specific causal lesion.

References

1. (caminati2024managingpatientswith pages 2-3): Marco Caminati, Luisa Brussino, Matilde Carlucci, Palma Carlucci, Lucia Federica Carpagnano, Cristiano Caruso, Lorenzo Cosmi, Simona D’Amore, Stefano Del Giacco, Aikaterini Detoraki, Mario Di Gioacchino, Andrea Matucci, Ilaria Mormile, Francescopaolo Granata, Gabriella Guarnieri, Mauro Krampera, Matteo Maule, Eustachio Nettis, Stefania Nicola, Silvia Noviello, Fabrizio Pane, Cristina Papayannidis, Paola Parronchi, Girolamo Pelaia, Erminia Ridolo, Francesca Wanda Rossi, Gianenrico Senna, Massimo Triggiani, Angelo Vacca, Emanuele Vivarelli, Alessandra Vultaggio, and Amato de Paulis. Managing patients with hypereosinophilic syndrome: a statement from the italian society of allergy, asthma, and clinical immunology (siaaic). Jul 2024. URL: https://doi.org/10.3390/cells13141180, doi:10.3390/cells13141180. This article has 28 citations.

2. (wang2023theinternationalconsensus pages 8-8): Sa A. Wang, Attilio Orazi, Jason Gotlib, Andreas Reiter, Alexandar Tzankov, Robert P. Hasserjian, Daniel A. Arber, and Ayalew Tefferi. The international consensus classification of eosinophilic disorders and systemic mastocytosis. American Journal of Hematology, 98:1286-1306, Jun 2023. URL: https://doi.org/10.1002/ajh.26966, doi:10.1002/ajh.26966. This article has 75 citations and is from a domain leading peer-reviewed journal.

3. (wang2023theinternationalconsensus pages 8-9): Sa A. Wang, Attilio Orazi, Jason Gotlib, Andreas Reiter, Alexandar Tzankov, Robert P. Hasserjian, Daniel A. Arber, and Ayalew Tefferi. The international consensus classification of eosinophilic disorders and systemic mastocytosis. American Journal of Hematology, 98:1286-1306, Jun 2023. URL: https://doi.org/10.1002/ajh.26966, doi:10.1002/ajh.26966. This article has 75 citations and is from a domain leading peer-reviewed journal.

4. (ezekwe2024biologicsinhypereosinophilic pages 3-4): Ejiofor Ezekwe, Andrew L. Weskamp, Luke M. Pittman, and Amy D. Klion. Biologics in hypereosinophilic syndrome and eosinophilic granulomatosis with polyangiitis. Nov 2024. URL: https://doi.org/10.1016/j.iac.2024.07.003, doi:10.1016/j.iac.2024.07.003. This article has 7 citations and is from a peer-reviewed journal.

5. (jackson2022eosinophilsandeosinophilic pages 3-4): David J. Jackson, Praveen Akuthota, and Florence Roufosse. Eosinophils and eosinophilic immune dysfunction in health and disease. European Respiratory Review, 31:210150, Jan 2022. URL: https://doi.org/10.1183/16000617.0150-2021, doi:10.1183/16000617.0150-2021. This article has 146 citations and is from a peer-reviewed journal.

6. (groh2023frenchguidelinesfor pages 5-7): Matthieu Groh, Julien Rohmer, Nicolas Etienne, Wadih Abou Chahla, Antoine Baudet, Aurélie Chan Hew Wai, Cécile Chenivesse, Irena Clisson Rusek, Vincent Cottin, Matthieu Decamp, Pascal De Groote, Fanny Delahousse, Nicolas Duployez, Stanislas Faguer, Frédéric Gottrand, Florent Huang, Thierry Leblanc, Antoine Magnan, Thierry Martin, Geoffrey Mortuaire, Antoine Néel, Luc Paris, Arnaud Petit, Julien Rossignol, Nicolas Schleinitz, Juliette Soret-Dulphy, Delphine Staumont-Salle, Benjamin Terrier, Louis Terriou, Jean-François Viallard, Guillaume Lefèvre, and Jean-Emmanuel Kahn. French guidelines for the etiological workup of eosinophilia and the management of hypereosinophilic syndromes. Orphanet Journal of Rare Diseases, Apr 2023. URL: https://doi.org/10.1186/s13023-023-02696-4, doi:10.1186/s13023-023-02696-4. This article has 56 citations and is from a peer-reviewed journal.

7. (nguyen2024clinicalandtherapeutic pages 9-10): Lynh Nguyen, Aditi Saha, Andrew Kuykendall, and Ling Zhang. Clinical and therapeutic intervention of hypereosinophilia in the era of molecular diagnosis. Cancers, 16:1383, Mar 2024. URL: https://doi.org/10.3390/cancers16071383, doi:10.3390/cancers16071383. This article has 14 citations.

8. (caminati2024managingpatientswith pages 8-10): Marco Caminati, Luisa Brussino, Matilde Carlucci, Palma Carlucci, Lucia Federica Carpagnano, Cristiano Caruso, Lorenzo Cosmi, Simona D’Amore, Stefano Del Giacco, Aikaterini Detoraki, Mario Di Gioacchino, Andrea Matucci, Ilaria Mormile, Francescopaolo Granata, Gabriella Guarnieri, Mauro Krampera, Matteo Maule, Eustachio Nettis, Stefania Nicola, Silvia Noviello, Fabrizio Pane, Cristina Papayannidis, Paola Parronchi, Girolamo Pelaia, Erminia Ridolo, Francesca Wanda Rossi, Gianenrico Senna, Massimo Triggiani, Angelo Vacca, Emanuele Vivarelli, Alessandra Vultaggio, and Amato de Paulis. Managing patients with hypereosinophilic syndrome: a statement from the italian society of allergy, asthma, and clinical immunology (siaaic). Jul 2024. URL: https://doi.org/10.3390/cells13141180, doi:10.3390/cells13141180. This article has 28 citations.

9. (nguyen2024clinicalandtherapeutic pages 5-7): Lynh Nguyen, Aditi Saha, Andrew Kuykendall, and Ling Zhang. Clinical and therapeutic intervention of hypereosinophilia in the era of molecular diagnosis. Cancers, 16:1383, Mar 2024. URL: https://doi.org/10.3390/cancers16071383, doi:10.3390/cancers16071383. This article has 14 citations.

10. (mora2025mepolizumabforhypereosinophilic pages 1-2): Elvira Mora, María Laura Fox, Angelina Lemes, Beatriz Velasco, and Jesús María Hernández-Rivas. Mepolizumab for hypereosinophilic syndrome: effectiveness and safety from real-world evidence. Frontiers in Immunology, Nov 2025. URL: https://doi.org/10.3389/fimmu.2025.1704077, doi:10.3389/fimmu.2025.1704077. This article has 2 citations and is from a peer-reviewed journal.

11. (valent2021eosinophilsandeosinophilassociated pages 6-8): Peter Valent, Lina Degenfeld-Schonburg, Irina Sadovnik, Hans-Peter Horny, Michel Arock, Hans-Uwe Simon, Andreas Reiter, and Bruce S. Bochner. Eosinophils and eosinophil-associated disorders: immunological, clinical, and molecular complexity. Seminars in Immunopathology, 43:423-438, May 2021. URL: https://doi.org/10.1007/s00281-021-00863-y, doi:10.1007/s00281-021-00863-y. This article has 83 citations and is from a domain leading peer-reviewed journal.

12. (NCT02836496 chunk 1):  Efficacy and Safety Study of Mepolizumab in Subjects With Severe Hypereosinophilic Syndrome (HES). GlaxoSmithKline. 2017. ClinicalTrials.gov Identifier: NCT02836496

13. (papaioannou2025biologicagentsin pages 4-6): Ourania Papaioannou, Fotios Sampsonas, Panagiota Tsiri, Vasilina Sotiropoulou, Ioannis Christopoulos, Dimitrios Komninos, and Argyrios Tzouvelekis. Biologic agents in idiopathic hypereosinophilic syndrome. Apr 2025. URL: https://doi.org/10.3390/ph18040543, doi:10.3390/ph18040543. This article has 0 citations.

14. (papaioannou2025biologicagentsin pages 1-2): Ourania Papaioannou, Fotios Sampsonas, Panagiota Tsiri, Vasilina Sotiropoulou, Ioannis Christopoulos, Dimitrios Komninos, and Argyrios Tzouvelekis. Biologic agents in idiopathic hypereosinophilic syndrome. Apr 2025. URL: https://doi.org/10.3390/ph18040543, doi:10.3390/ph18040543. This article has 0 citations.

15. (OpenTargets Search: idiopathic hypereosinophilic syndrome): Open Targets Query (idiopathic hypereosinophilic syndrome, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

16. (longhino2025clinicalandimmunological pages 1-2): David Longhino, Ilaria Baglivo, Maria Antonietta Zavarella, Stefania Colantuono, Chiara Laface, Gabriele Lucca, Laura Bruno, Fabio Romano Selvi, Vincenzo Patella, Aikaterini Detoraki, Rosa Buonagura, Caterina Tatarelli, Barbara Moscatelli, Serena D’Avelli, Elisabetta Abruzzese, Elisabetta Greco, Antonio Gasbarrini, Livio Pagano, Marianna Criscuolo, Sabrina Giammarco, and Cristiano Caruso. Clinical and immunological biomarkers in hypereosinophilic syndrome: the second step after diagnostic algorithms. Frontiers in Medicine, Jul 2025. URL: https://doi.org/10.3389/fmed.2025.1600728, doi:10.3389/fmed.2025.1600728. This article has 1 citations.

17. (roufosse2007hypereosinophilicsyndromes pages 1-2): Florence E Roufosse, Michel Goldman, and Elie Cogan. Hypereosinophilic syndromes. Orphanet Journal of Rare Diseases, 2:37-37, Sep 2007. URL: https://doi.org/10.1186/1750-1172-2-37, doi:10.1186/1750-1172-2-37. This article has 264 citations and is from a peer-reviewed journal.

18. (taurisano2025hypereosinophiliaclinicaland pages 6-7): Giusi Taurisano, Maria Clara Ruffi, Silvia Canalis, and Giulia Anna Maria Luigia Costanzo. Hypereosinophilia: clinical and therapeutic approach in 2025. Current Opinion in Allergy and Clinical Immunology, 25:258-268, May 2025. URL: https://doi.org/10.1097/aci.0000000000001078, doi:10.1097/aci.0000000000001078. This article has 14 citations and is from a peer-reviewed journal.

19. (nguyen2024clinicalandtherapeutic pages 4-5): Lynh Nguyen, Aditi Saha, Andrew Kuykendall, and Ling Zhang. Clinical and therapeutic intervention of hypereosinophilia in the era of molecular diagnosis. Cancers, 16:1383, Mar 2024. URL: https://doi.org/10.3390/cancers16071383, doi:10.3390/cancers16071383. This article has 14 citations.

20. (valent2021eosinophilsandeosinophilassociated pages 4-5): Peter Valent, Lina Degenfeld-Schonburg, Irina Sadovnik, Hans-Peter Horny, Michel Arock, Hans-Uwe Simon, Andreas Reiter, and Bruce S. Bochner. Eosinophils and eosinophil-associated disorders: immunological, clinical, and molecular complexity. Seminars in Immunopathology, 43:423-438, May 2021. URL: https://doi.org/10.1007/s00281-021-00863-y, doi:10.1007/s00281-021-00863-y. This article has 83 citations and is from a domain leading peer-reviewed journal.

21. (taurisano2025hypereosinophiliaclinicaland pages 1-2): Giusi Taurisano, Maria Clara Ruffi, Silvia Canalis, and Giulia Anna Maria Luigia Costanzo. Hypereosinophilia: clinical and therapeutic approach in 2025. Current Opinion in Allergy and Clinical Immunology, 25:258-268, May 2025. URL: https://doi.org/10.1097/aci.0000000000001078, doi:10.1097/aci.0000000000001078. This article has 14 citations and is from a peer-reviewed journal.

22. (valent2021eosinophilsandeosinophilassociated pages 8-10): Peter Valent, Lina Degenfeld-Schonburg, Irina Sadovnik, Hans-Peter Horny, Michel Arock, Hans-Uwe Simon, Andreas Reiter, and Bruce S. Bochner. Eosinophils and eosinophil-associated disorders: immunological, clinical, and molecular complexity. Seminars in Immunopathology, 43:423-438, May 2021. URL: https://doi.org/10.1007/s00281-021-00863-y, doi:10.1007/s00281-021-00863-y. This article has 83 citations and is from a domain leading peer-reviewed journal.

23. (groh2023frenchguidelinesfor pages 2-4): Matthieu Groh, Julien Rohmer, Nicolas Etienne, Wadih Abou Chahla, Antoine Baudet, Aurélie Chan Hew Wai, Cécile Chenivesse, Irena Clisson Rusek, Vincent Cottin, Matthieu Decamp, Pascal De Groote, Fanny Delahousse, Nicolas Duployez, Stanislas Faguer, Frédéric Gottrand, Florent Huang, Thierry Leblanc, Antoine Magnan, Thierry Martin, Geoffrey Mortuaire, Antoine Néel, Luc Paris, Arnaud Petit, Julien Rossignol, Nicolas Schleinitz, Juliette Soret-Dulphy, Delphine Staumont-Salle, Benjamin Terrier, Louis Terriou, Jean-François Viallard, Guillaume Lefèvre, and Jean-Emmanuel Kahn. French guidelines for the etiological workup of eosinophilia and the management of hypereosinophilic syndromes. Orphanet Journal of Rare Diseases, Apr 2023. URL: https://doi.org/10.1186/s13023-023-02696-4, doi:10.1186/s13023-023-02696-4. This article has 56 citations and is from a peer-reviewed journal.

24. (wilkins2005hypereosinophilicsyndromean pages 1-2): H. Jeffrey Wilkins, Martin M. Crane, Kelly Copeland, and William V. Williams. Hypereosinophilic syndrome: an update. American Journal of Hematology, 80:148-157, Oct 2005. URL: https://doi.org/10.1002/ajh.20423, doi:10.1002/ajh.20423. This article has 151 citations and is from a domain leading peer-reviewed journal.

25. (curtis2016hypereosinophilicsyndrome pages 10-11): Casey Curtis and Princess Ogbogu. Hypereosinophilic syndrome. Clinical Reviews in Allergy & Immunology, 50:240-251, Oct 2016. URL: https://doi.org/10.1007/s12016-015-8506-7, doi:10.1007/s12016-015-8506-7. This article has 234 citations and is from a peer-reviewed journal.

26. (nguyen2024clinicalandtherapeutic pages 17-19): Lynh Nguyen, Aditi Saha, Andrew Kuykendall, and Ling Zhang. Clinical and therapeutic intervention of hypereosinophilia in the era of molecular diagnosis. Cancers, 16:1383, Mar 2024. URL: https://doi.org/10.3390/cancers16071383, doi:10.3390/cancers16071383. This article has 14 citations.

27. (NCT06477653 chunk 1):  Dupilumab as Add-On Therapy for Hypereosinophilic Syndrome With Partial Clinical Response to Eosinophil-Depleting Biologic Agents. National Institute of Allergy and Infectious Diseases (NIAID). 2025. ClinicalTrials.gov Identifier: NCT06477653

28. (ezekwe2024biologicsinhypereosinophilic pages 9-10): Ejiofor Ezekwe, Andrew L. Weskamp, Luke M. Pittman, and Amy D. Klion. Biologics in hypereosinophilic syndrome and eosinophilic granulomatosis with polyangiitis. Nov 2024. URL: https://doi.org/10.1016/j.iac.2024.07.003, doi:10.1016/j.iac.2024.07.003. This article has 7 citations and is from a peer-reviewed journal.

29. (wilkins2005hypereosinophilicsyndromean pages 2-4): H. Jeffrey Wilkins, Martin M. Crane, Kelly Copeland, and William V. Williams. Hypereosinophilic syndrome: an update. American Journal of Hematology, 80:148-157, Oct 2005. URL: https://doi.org/10.1002/ajh.20423, doi:10.1002/ajh.20423. This article has 151 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Idiopathic_Hypereosinophilic_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011895` (5 mentions) - the report calls it "if available"; MONDO calls it **idiopathic hypereosinophilic syndrome**