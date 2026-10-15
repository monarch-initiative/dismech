---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-12T16:29:32.536040'
end_time: '2026-09-12T16:41:02.140791'
duration_seconds: 689.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Spastic Paraplegia 3A
  mondo_id: MONDO:0008437
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 61
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 9
  validator_version: 0.2.1
term_validation:
  total_terms: 46
  verified: 46
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 4
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0008437
    reported_labels:
    - if available
    ontology_label: hereditary spastic paraplegia 3A
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hereditary_Spastic_Paraplegia_3A-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Spastic Paraplegia 3A
- **MONDO ID:** MONDO:0008437 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Spastic Paraplegia 3A** covering all of the
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
- **Disease Name:** Hereditary Spastic Paraplegia 3A
- **MONDO ID:** MONDO:0008437 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Spastic Paraplegia 3A** covering all of the
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


# Hereditary Spastic Paraplegia 3A (SPG3A): Disease-Characteristics Report

**Scope.** This report summarizes evidence available through 2024, prioritizing disease-specific human studies and distinguishing them from general hereditary spastic paraplegia (HSP) guidance and preclinical findings. Database identifiers should be revalidated against the release used by the target knowledge base. PMIDs are included only where verified in the retrieved evidence; DOI links are supplied otherwise.

## Executive summary

SPG3A is a rare Mendelian upper-motor-neuron disorder caused by pathogenic variants in **ATL1**, which encodes the endoplasmic-reticulum (ER) membrane fusogen atlastin-1. The usual phenotype is autosomal-dominant, childhood-onset “pure” HSP: bilateral lower-limb spasticity, hyperreflexia, extensor plantar responses, gait impairment, and variable weakness or urinary symptoms. Onset commonly occurs at 1–3 years, the reported mean is approximately 4.6 years, progression is usually slow, and most affected people remain ambulatory. In 2024, three exceptional cases expanded the spectrum to severe disease beginning before seven months and supported rare autosomal-recessive inheritance from biallelic ATL1 variants. (rudenskaya2020clinicalmolecularand pages 1-2, hamamiechaar2024patientswithcomplex pages 1-2, hamamiechaar2024patientswithcomplex pages 2-4)

The strongest mechanistic model is that mutation-specific impairment of GTP-dependent ATL1-mediated ER membrane fusion disturbs the continuous tubular ER network in long axons. Downstream defects include abnormal axon growth, transport, and swellings. Human stem-cell work additionally implicates defective astrocyte lipid-droplet biology and astrocyte-to-neuron cholesterol transfer. However, a universal dominant-negative mechanism has not been established; loss-of-function, dominant-negative, dosage-dependent, and variant-specific effects may coexist. (mou2020impairedlipidmetabolism pages 1-2, sonda2021ermorphologyin pages 5-6, crosby2021reconstitutionofhuman pages 1-2)

There is no approved disease-modifying therapy or SPG3A-specific treatment trial. Current care is multidisciplinary and symptomatic. (maccora2024nonpharmacologicaltreatmentof pages 1-2, bellofatto2019managementofhereditary pages 1-2)

| Domain | Finding | Evidence type | Source/date/DOI |
|---|---|---|---|
| 2024 phenotypic expansion | Three unrelated individuals had severe onset before 7 months with axial hypotonia, spastic quadriplegia, dystonia, seizures, and intellectual disability. Variants were de novo heterozygous p.(Lys406Glu), homozygous p.(Arg403Glufs*3), and homozygous p.(Tyr367His); asymptomatic heterozygous parents in the latter two families support rare autosomal-recessive SPG3A. (hamamiechaar2024patientswithcomplex pages 1-2, hamamiechaar2024patientswithcomplex pages 2-4) | Human case series | Hamamie-Chaar et al.; July 2024; [DOI: 10.1007/s00415-024-12565-0](https://doi.org/10.1007/s00415-024-12565-0) |
| Clinical frequency and penetrance | In Russia, SPG3A comprised 7.2% of 195 HSP families, 13.6% of 103 molecularly resolved families, and 16.9% of dominant forms. Among 14 SPG3A families, incomplete penetrance or subclinical disease occurred in five; 3 of 6 electrophysiologically tested patients had subclinical axonal polyneuropathy. (rudenskaya2020clinicalmolecularand pages 1-2) | Human cohort | Rudenskaya et al.; March 2020; [DOI: 10.25692/acen.2020.1.5](https://doi.org/10.25692/acen.2020.1.5) |
| Variant spectrum | In 122 Russian HSP probands, ATL1-related disease was found in 10 (8.2%), all familial. All ten variants were missense; most occurred in hotspot exons 4, 7, 8, and 12, and two were novel. (kadnikova2019mutationalspectrumof pages 1-2) | Human molecular cohort | Kadnikova et al.; October 2019; [DOI: 10.1038/s41598-019-50911-9](https://doi.org/10.1038/s41598-019-50911-9) |
| Classic epidemiology and course | SPG3A represents approximately 10%–15% of dominant uncomplicated HSP and more than 75% of early-onset dominant cases. Typical onset is in the first decade—often age 1–3 years, with a reported mean of 4.6 years—and progression is generally slow with preserved ambulation; cerebral palsy is a recurrent initial misdiagnosis. (rudenskaya2020clinicalmolecularand pages 1-2, hamamiechaar2024patientswithcomplex pages 1-2, bick1993uncomplicated(pure)hereditary pages 1-3) | Aggregated human clinical evidence | GeneReviews-derived overview; Rudenskaya et al. 2020; Hamamie-Chaar et al. 2024 |
| Causal gene and ER fusion | ATL1 encodes neuronally enriched atlastin-1, an ER-membrane dynamin-like GTPase. GTP-dependent dimerization, three-helix-bundle crossover, and amphipathic-helix insertion drive homotypic ER-membrane fusion; purified human ATL1 directly catalyzes GTP-dependent lipid mixing. The relative contributions of loss of function, dominant-negative action, and other mutation-specific effects remain unresolved. (sonda2021ermorphologyin pages 5-6, crosby2021reconstitutionofhuman pages 1-2) | Biochemical, structural, and cellular evidence | Crosby et al.; November 2021; [DOI: 10.1083/jcb.202107070](https://doi.org/10.1083/jcb.202107070); Sonda et al.; October 2021; [DOI: 10.3390/cells10112870](https://doi.org/10.3390/cells10112870) |
| Astrocyte–neuron lipid mechanism | Isogenic ATL1-A161P and patient-derived ATL1-P342S models showed impaired axonal outgrowth and transport and axonal swellings. ATL1-mutant astrocytes had smaller lipid droplets and defective cholesterol transfer, causing neuronal cholesterol deficiency; cholesterol, control-conditioned medium, or the NR1H2/LXR agonist GW3965 rescued axonal abnormalities. (mou2020impairedlipidmetabolism pages 1-2) | Human hPSC/iPSC-derived cortical neurons and astrocytes; experimental rescue | Mou et al.; December 2020; [DOI: 10.1186/s40478-020-01088-0](https://doi.org/10.1186/s40478-020-01088-0) |
| Neuromuscular-junction model | Autologous iPSC-derived lower-motor-neuron and myotube cultures from three SPG3A and two SPG4 patients produced fewer, less-complex neuromuscular junctions; HSP neurons showed axonal swellings and acetylated α-tubulin accumulation. Findings are preclinical and were not separately quantified for SPG3A in the cited summary. (costamagna2022autologousipscderivedhuman pages 1-2) | Human patient-derived iPSC microfluidic model | Costamagna et al.; 24 October 2022; [DOI: 10.3390/cells11213351](https://doi.org/10.3390/cells11213351) |
| Current treatment | No therapy is proven to halt, reverse, or prevent SPG3A progression. Current HSP care is individualized and symptomatic: physiotherapy, stretching, orthoses, mobility aids, oral baclofen, tizanidine or dantrolene, focal botulinum toxin, intrathecal baclofen for severe refractory spasticity, and bladder-directed therapy such as oxybutynin. Evidence is predominantly general HSP evidence rather than SPG3A-specific trials. (maccora2024nonpharmacologicaltreatmentof pages 1-2, bellofatto2019managementofhereditary pages 1-2, toft2017clinicalandgenetic pages 6-8) | Systematic reviews and clinical-management evidence | Maccora et al.; online 16 November 2023 / 2024 issue; [DOI: 10.1007/s10072-023-07200-1](https://doi.org/10.1007/s10072-023-07200-1); Bellofatto et al.; 22 January 2019; [DOI: 10.3389/fneur.2019.00003](https://doi.org/10.3389/fneur.2019.00003) |


*Table: Highest-value clinical, genetic, mechanistic, model-system, and treatment evidence for ATL1-related hereditary spastic paraplegia 3A. The table distinguishes human observations from preclinical findings and flags the absence of disease-modifying therapy.*

## 1. Disease information

### Definition and nomenclature

SPG3A is a genetic neurodevelopmental/neurodegenerative disorder in which length-dependent dysfunction and degeneration of corticospinal upper-motor-neuron axons produces progressive or relatively static spastic paraparesis. It is also called **spastic paraplegia type 3A**, **ATL1-related hereditary spastic paraplegia**, **autosomal-dominant spastic paraplegia type 3**, and **atlastin-1–related HSP**. The “pure” designation means that corticospinal manifestations predominate; “complex” SPG3A includes additional neurologic findings such as neuropathy, dystonia, seizures, or intellectual disability. (denton2015modellinghereditaryspastic pages 13-17, hamamiechaar2024patientswithcomplex pages 1-2, bick1993uncomplicated(pure)hereditary pages 1-3)

### Identifiers

- **MONDO:** MONDO:0008437. Open Targets maps this disease to ATL1/ENSG00000198513 with five evidence records, including PMIDs 11685207, 21194679, 21336785, 22340599, and 23483706. (OpenTargets Search: Hereditary spastic paraplegia 3A-ATL1)
- **OMIM phenotype:** **182600**, Spastic paraplegia 3A, autosomal dominant.
- **Gene:** **ATL1**; approved name *atlastin GTPase 1*; commonly cited OMIM gene entry **606439**; Ensembl **ENSG00000198513**. (OpenTargets Search: Hereditary spastic paraplegia 3A-ATL1)
- **Orphanet:** SPG3A is represented within rare hereditary spastic paraplegia resources; the exact ORPHA record should be release-validated before ingestion.
- **ICD-10-CM:** **G11.4**, hereditary spastic paraplegia, a group-level rather than SPG3A-specific code.
- **ICD-11/MeSH/SNOMED CT:** these generally represent HSP at the group level; no universally used SPG3A-specific billing code was established in the retrieved literature.

The evidence summarized here is **aggregated disease-level evidence** from cohorts, case series, reviews, databases, and experimental studies—not individual EHR data.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The primary cause is a **germline pathogenic ATL1 variant**. Most recognized disease is caused by a heterozygous variant and follows autosomal-dominant inheritance. De novo heterozygous variants occur. Rare homozygous missense or truncating variants have produced severe recessive presentations, although the size of this evidence base remains small. (khan2014evidenceforautosomal pages 5-5, rudenskaya2020clinicalmolecularand pages 1-2, hamamiechaar2024patientswithcomplex pages 1-2)

### Genetic risk factors

A pathogenic allele, an affected parent, or a family history of early-onset spastic gait is the dominant risk factor. In one Russian series, all ten ATL1 diagnoses were familial; another series included a de novo case and incomplete/subclinical penetrance in five of 14 families. (rudenskaya2020clinicalmolecularand pages 1-2, kadnikova2019mutationalspectrumof pages 1-2)

Most reported variants are missense substitutions, enriched in exons 4, 7, 8, and 12 and affecting the GTPase or three-helix-bundle machinery. Nevertheless, deletions, insertions, splice variants, exon deletions, and frameshift variants are documented. (kadnikova2019mutationalspectrumof pages 1-2, sonda2021ermorphologyin pages 5-6)

### Environmental and protective factors

No toxin, infection, diet, occupation, smoking exposure, or lifestyle factor is established as a cause of SPG3A. No validated protective human allele or environmental exposure is known. Exercise and rehabilitation preserve mobility and prevent secondary complications but have not been shown to prevent the molecular disease. Likewise, cholesterol supplementation and LXR activation are experimental cellular rescues, not proven protective interventions in humans. (mou2020impairedlipidmetabolism pages 1-2, maccora2024nonpharmacologicaltreatmentof pages 1-2)

No robust SPG3A gene–environment interaction has been demonstrated. Apparent variability is currently attributed primarily to variant-specific biology, penetrance, genetic background, age, and ascertainment.

## 3. Phenotypes

### Core phenotype and suggested HPO annotations

- **Lower-limb spasticity**—clinical sign, usually bilateral and symmetric; **HP:0001257**.
- **Spastic paraplegia/paraparesis**—sign and functional manifestation; **HP:0001278**.
- **Lower-limb weakness**—symptom/sign; **HP:000腿 weakness concept should be mapped to the current HPO release**, commonly represented as lower-limb muscle weakness.
- **Hyperreflexia**—sign; **HP:0001347**.
- **Extensor plantar response/Babinski sign**—sign; **HP:0003487**.
- **Abnormal/spastic or scissoring gait**—sign; **HP:0001288** and **HP:0002066**, subject to release validation.
- **Urinary urgency or bladder dysfunction**—symptom; **HP:0000012**/more specific current term.
- **Distal sensory impairment or axonal polyneuropathy**—laboratory/clinical sign; **HP:0000763** and **HP:0003477**.

Classic SPG3A begins in the first decade, often at 1–3 years, and has a reported mean onset of 4.6 years. It is generally mild-to-moderate, pure, and slowly progressive, with preserved ambulation. Early-onset disease may plateau and resemble spastic diplegic cerebral palsy. (rudenskaya2020clinicalmolecularand pages 1-2, hamamiechaar2024patientswithcomplex pages 1-2, bick1993uncomplicated(pure)hereditary pages 1-3)

In the Russian clinical series, most of 25 examined patients had early-onset uncomplicated HSP with slow progression. Subclinical axonal polyneuropathy occurred in **3/6** electrophysiologically tested patients. (rudenskaya2020clinicalmolecularand pages 1-2)

### Complex and exceptional phenotypes

Suggested terms include axial hypotonia (**HP:0008936**), spastic quadriplegia (**HP:0002510**), dystonia (**HP:0001332**), seizures (**HP:0001250**), intellectual disability (**HP:0001249**), global developmental delay (**HP:0001263**), dysarthria (**HP:0001260**), dysphagia (**HP:0002015**), delayed myelination (**HP:0012448**), and skeletal deformity/scoliosis (**HP:0002650**).

The 2024 report described three unrelated children with onset before seven months, early axial hypotonia followed by progressive limb spasticity, and severe complex disease. Features included tetraplegia, dystonia, seizures, intellectual disability, dysarthria, swallowing problems, and profound motor dependence. Two had initially been diagnosed with cerebral palsy. In the collaborating French databases, none of **96** previously confirmed ATL1 cases had comparably severe disease in the first year, underscoring its exceptional nature. (hamamiechaar2024patientswithcomplex pages 1-2, hamamiechaar2024patientswithcomplex pages 2-4)

### Quality of life

Gait limitation, falls, fatigue, painful spasms, contractures, bladder symptoms, and dependence on mobility aids can impair education, employment, self-care, and participation. Formal SPG3A-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life statistics were not identified. General HSP reviews conclude that lifespan is usually preserved while disability and quality-of-life impairment accumulate with severity. (awuah2024hereditaryspasticparaplegia pages 1-2, bick1993uncomplicated(pure)hereditary pages 1-3)

## 4. Genetic and molecular information

### Gene and protein

**ATL1** encodes atlastin-1, a neuronally enriched, integral ER-membrane dynamin-like GTPase. The protein contains an N-terminal GTPase domain, three-helix-bundle domain, two closely spaced transmembrane segments, and a C-terminal amphipathic region. It interacts functionally with other ER-shaping HSP proteins, including spastin, REEP1, and reticulon-2. (toft2017clinicalandgenetic pages 6-8, sonda2021ermorphologyin pages 5-6, crosby2021reconstitutionofhuman pages 1-2)

Suggested molecular annotations include **GTPase activity** (GO:0003924), **GTP binding** (GO:0005525), **endoplasmic-reticulum membrane** (GO:0005789), **membrane fusion** (GO:0061025), **ER organization** (GO:0007029), and **homotypic membrane fusion** using the most specific current GO term.

### Variant spectrum and classification

Examples supported by human evidence include:

- **p.Arg415Trp:** recurrent in four Russian families; incomplete penetrance has been observed for some recurrent ATL1 alleles. (rudenskaya2020clinicalmolecularand pages 1-2)
- **c.353G>A, p.Arg118Gln:** homozygous missense change at a conserved GTPase-domain residue, proposed to cause recessive SPG3A. (khan2014evidenceforautosomal pages 5-5)
- **c.1216A>G, p.Lys406Glu:** de novo heterozygous missense change in the three-helix-bundle region, associated with severe very-early-onset disease. (hamamiechaar2024patientswithcomplex pages 2-4)
- **c.1207del, p.Arg403Glufs*3:** homozygous frameshift, with asymptomatic heterozygous parents. (hamamiechaar2024patientswithcomplex pages 1-2, hamamiechaar2024patientswithcomplex pages 2-4)
- **c.1099T>C, p.Tyr367His:** homozygous missense variant, also with asymptomatic heterozygous parents. (hamamiechaar2024patientswithcomplex pages 1-2, hamamiechaar2024patientswithcomplex pages 2-4)

In 122 Russian HSP probands, ten had ATL1 diagnoses; all ten variants were missense, most in hotspot exons 4, 7, 8, or 12, and two were novel. A related 14-family analysis found nine missense variants, four novel. (rudenskaya2020clinicalmolecularand pages 1-2, kadnikova2019mutationalspectrumof pages 1-2)

Clinical classification must use current ClinVar submissions and ACMG/AMP criteria at the individual-variant level. Pathogenicity should not be inferred solely from rarity or an ATL1 location. Disease-causing variants are expected to be absent or extremely rare in population databases, but the retrieved evidence did not supply reliable allele frequencies for each variant. Variants are germline; no somatic ATL1 mechanism is established.

### Functional consequence, modifiers, epigenetics, and structural variation

Many variants impair GTP binding/hydrolysis, oligomerization, membrane insertion, or fusion. A dominant-negative model is plausible because ATL1 functions as a dimer, but experiments have not supported one mechanism for all variants. Some behave as partial loss-of-function alleles, and dosage effects are evident in models. (sonda2021ermorphologyin pages 5-6, damiani2024pluripotentstemcells pages 3-3)

No clinically validated human modifier gene, epigenetic signature, methylation biomarker, anticipation mechanism, or recurrent pathogenic chromosomal rearrangement is established. ATL1 exon-level copy-number changes are possible but appear much less prominent than missense variants. Germline mosaicism is theoretically relevant to apparently de novo cases but was not quantified.

## 5. Environmental information

SPG3A is not infectious, toxic, nutritional, occupational, radiation-induced, or zoonotic. Environmental exposures do not presently form part of causal classification or risk stratification. Lifestyle management—regular activity, stretching, healthy weight, fall prevention, and avoidance of deconditioning—targets secondary disability rather than ATL1 pathogenesis. (maccora2024nonpharmacologicaltreatmentof pages 1-2, toft2017clinicalandgenetic pages 6-8)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A germline pathogenic **ATL1** variant **leads to** mutation-specific alteration of atlastin-1 abundance, GTPase-cycle dynamics, dimerization, membrane engagement, or fusogenic activity.
2. Altered atlastin-1 **leads to** deficient or dysregulated GTP-dependent homotypic fusion of ER tubules and disturbed tubular-ER topology; this step is biochemically demonstrated for ATL1 function, but the magnitude and direction of dysfunction vary by allele. (sonda2021ermorphologyin pages 5-6, crosby2021reconstitutionofhuman pages 1-2)
3. Abnormal ER topology **results in** impaired maintenance of the continuous axonal ER network and perturbed interactions with microtubules, membrane trafficking, and organelle/lipid homeostasis; the direct disease-causal linkage remains partly inferred. (toft2017clinicalandgenetic pages 6-8, sonda2021ermorphologyin pages 5-6)
4. **Neuron-autonomous branch:** ER and cytoskeletal dysfunction **leads to** reduced axonal outgrowth, impaired axonal transport, axonal swellings, dendritic abnormalities, and synaptic/NMJ defects. (mou2020impairedlipidmetabolism pages 1-2, costamagna2022autologousipscderivedhuman pages 1-2, damiani2024pluripotentstemcells pages 2-3)
5. **Glial branch:** ATL1 dysfunction in astrocytes **leads to** altered proteolipid expression, smaller lipid droplets, and impaired cholesterol export; this **results in** cholesterol deficiency in cortical projection neurons. (mou2020impairedlipidmetabolism pages 1-2)
6. Convergent transport, trophic, membrane, and lipid defects **lead to** preferential dysfunction and distal degeneration of exceptionally long corticospinal axons; selective vulnerability is strongly supported, but the exact terminal injury pathway is inferred. (denton2015modellinghereditaryspastic pages 13-17, mou2020impairedlipidmetabolism pages 1-2)
7. Loss of descending corticospinal control **results in** bilateral lower-limb hyperreflexia, spasticity, weakness, Babinski signs, and gait impairment. (bick1993uncomplicated(pure)hereditary pages 1-3, meyyazhagan2022hereditaryspasticparaplegia pages 1-2)

### Molecular detail and recent research

Single-molecule work published in March 2024 refined the atlastin cycle: GTP binding forms a loose crossover dimer, GTP hydrolysis tightens it to drive fusion, and phosphate release promotes disassembly and recycling. Two disease mutations impaired activity through distinct structural effects, supporting allele-specific mechanisms ([DOI 10.1038/s41467-024-46919-z](https://doi.org/10.1038/s41467-024-46919-z)). The earlier human reconstitution study directly demonstrated GTP-dependent lipid mixing by purified ATL1 and identified C-terminal autoinhibition. (crosby2021reconstitutionofhuman pages 1-2)

An exact abstract statement from the reconstitution study is: **“purified atlastin1 and atlastin2 are capable of fusion catalysis.”** (crosby2021reconstitutionofhuman pages 1-2)

The most disease-specific multi-lineage profiling comes from human pluripotent-cell models. ATL1-A161P and patient-derived ATL1-P342S cortical neurons had reduced axonal growth, impaired transport, and swellings. Mutant astrocytes exhibited dysregulated proteolipid expression and smaller lipid droplets, with deficient cholesterol transfer to neurons. Cholesterol, control-astrocyte conditioned medium, and the NR1H2/LXR agonist **GW3965** rescued cellular abnormalities. This is compelling preclinical evidence, not evidence of clinical efficacy. (mou2020impairedlipidmetabolism pages 1-2)

Suggested GO terms: ER organization (GO:0007029), membrane fusion (GO:0061025), axon development (GO:0061564), axonal transport (GO:0098930), cholesterol transport (GO:0030301), lipid-droplet organization (current GO release), neuron projection maintenance (GO:0031175), and synapse organization (GO:0050808). Suggested cell types are corticospinal neuron/upper motor neuron, cortical projection neuron (**CL:0010012**, release validation required), astrocyte (**CL:0000127**), lower motor neuron (**CL:0000100**), and skeletal-muscle cell (**CL:0000188**).

No validated SPG3A-specific immune, inflammatory, metabolomic, proteomic, epigenomic, single-cell, or spatial-transcriptomic signature has entered clinical use.

## 7. Anatomical structures affected

The primary system is the central nervous system, particularly bilateral long corticospinal tracts and their cortical projection neurons. Distal corticospinal axons in the thoracic spinal cord are especially vulnerable; demyelination, where present, is considered secondary to axonal injury. Peripheral axons may be subclinically involved. (denton2015modellinghereditaryspastic pages 13-17, rudenskaya2020clinicalmolecularand pages 1-2)

Suggested annotations include nervous system (**UBERON:0001016**), cerebral cortex (**UBERON:0000956**), spinal cord (**UBERON:0002240**), corticospinal tract (current UBERON/FMA mapping), thoracic spinal cord, lower limb (**UBERON:0002103**), skeletal muscle (**UBERON:0001134**), and neuromuscular junction (**UBERON:0001015**, release validation required).

Subcellular structures include tubular ER/ER membrane (GO:0005783/GO:0005789), axon (GO:0030424), growth cone (GO:0030426), microtubule cytoskeleton (GO:0015630), lipid droplet (GO:0005811), and synapse (GO:0045202). Disease is usually bilateral and symmetric rather than lateralized. (mou2020impairedlipidmetabolism pages 1-2, costamagna2022autologousipscderivedhuman pages 1-2)

## 8. Temporal development

Typical onset is insidious during infancy or childhood, usually before age ten and often at 1–3 years. Progression is slow and may become nearly static after an early developmental presentation. Adult onset is possible but uncommon. (rudenskaya2020clinicalmolecularand pages 1-2, bick1993uncomplicated(pure)hereditary pages 1-3)

There is no validated staging system. A practical functional description is: early toe walking/stiff gait; intermediate increasing spasticity, falls, contractures, or bladder symptoms; and advanced need for aids or wheelchair in severely affected individuals. Typical SPG3A patients often remain ambulatory, whereas the rare severe 2024 cases never achieved independent walking or retained only a few assisted steps. (hamamiechaar2024patientswithcomplex pages 1-2, hamamiechaar2024patientswithcomplex pages 2-4)

The disease is lifelong, with no true spontaneous remission. Childhood may be a critical intervention window because contracture prevention and gait preservation are easier before fixed deformities develop, but a molecular therapeutic window has not been defined.

## 9. Inheritance and population

### Epidemiology

Reliable population prevalence and incidence specific to SPG3A are unavailable. General HSP prevalence is reported as **0.1–9.6 per 100,000**; one review cited an overall incidence estimate of **3.6 per 100,000**, but this is not SPG3A-specific. (awuah2024hereditaryspasticparaplegia pages 1-2, meyyazhagan2022hereditaryspasticparaplegia pages 1-2)

SPG3A has been estimated at **2–3% of all HSP**, **8–10% of familial dominant HSP**, approximately **10–15% of dominant uncomplicated HSP**, and more than **75% of early-onset dominant uncomplicated HSP**. Ascertainment and population differences explain part of the range. (kadnikova2019mutationalspectrumof pages 1-2, bick1993uncomplicated(pure)hereditary pages 1-3)

Recent cohort statistics include:

- Russia: **10/122 (8.2%)** HSP probands had ATL1 variants. (kadnikova2019mutationalspectrumof pages 1-2)
- Expanded Russian analysis: **14/195 families (7.2%)**, **14/103 molecularly resolved families (13.6%)**, and **16.9% of dominant forms**. (rudenskaya2020clinicalmolecularand pages 1-2)
- A 1,550-index-case HSP panel cohort found ATL1 among genes accounting individually for more than 1% of all cases; the overall panel yield was 30.7%, not an SPG3A-specific yield.

### Mendelian features

Classical inheritance is autosomal dominant, giving each child of a heterozygous affected individual a 50% transmission probability. Penetrance is high overall but incomplete and allele-/age-dependent; five of 14 Russian families contained subclinical carriers. Sex-dependent penetrance has been reported, but no stable male:female ratio is established. (khan2014evidenceforautosomal pages 5-5, rudenskaya2020clinicalmolecularand pages 1-2, toft2017clinicalandgenetic pages 6-8)

Rare autosomal-recessive SPG3A is supported by homozygous variants and unaffected heterozygous parents. Its frequency is unknown and evidence remains limited to small numbers of families. (khan2014evidenceforautosomal pages 5-5, hamamiechaar2024patientswithcomplex pages 1-2)

Expressivity is variable, including within families. Genetic anticipation is not established. Founder effects, carrier frequency, and effects of consanguinity have not been quantified globally. No ethnic group is intrinsically protected; cases occur worldwide.

## 10. Diagnostics

### Clinical evaluation

Suspect SPG3A in a child with chronic, symmetric spastic gait, corticospinal signs, normal or near-normal cognition, and a dominant family history—particularly when labeled as cerebral palsy despite progression, affected relatives, or no perinatal insult. Fink-style HSP criteria emphasize progressive symmetric spastic gait, family history, corticospinal signs, and exclusion of alternative causes. (maccora2024nonpharmacologicaltreatmentof pages 1-2)

Neurologic examination should assess tone, strength, reflexes, plantar responses, gait, joint range, sensation, bladder function, cognition, speech/swallowing, dystonia, seizures, and family history. MRI brain and spine exclude structural, inflammatory, vascular, and demyelinating mimics; imaging is often normal in pure HSP. EMG/nerve-conduction studies are useful when neuropathy is suspected and may identify subclinical involvement. (rudenskaya2020clinicalmolecularand pages 1-2, toft2017clinicalandgenetic pages 6-8)

No blood, urine, enzyme, biopsy, pathology, or fluid biomarker is diagnostic. Neurofilament light and other neurodegeneration markers remain investigational and are not validated for SPG3A.

### Genetic testing strategy

1. Use an **NGS HSP/spastic-ataxia panel** containing ATL1, SPAST, REEP1, KIF1A, KIF5A, SPG11, SPG7, and relevant mimics, with validated copy-number analysis.
2. Confirm reportable variants by an orthogonal method where required and test parents/relatives for segregation, de novo status, penetrance, or phase.
3. If negative, use exome or genome sequencing with CNV, splice, and reanalysis capability. A 1,550-case study supported panel-first testing and found that exome sequencing after a negative panel could raise theoretical yield toward 50% in a selected subset. General cohort evidence also shows that NGS can miss deep-intronic, regulatory, repeat, or structural lesions. (toft2017clinicalandgenetic pages 16-18)
4. Single-gene ATL1 sequencing is reasonable where the phenotype and pedigree are highly characteristic, but broad panels better address overlap.

CMA, karyotyping, and FISH are not first-line for isolated classic SPG3A. Mitochondrial DNA and repeat-expansion testing are phenotype-directed. RNA sequencing may help resolve suspected splice variants but is not routine. Population newborn screening is unavailable.

### Differential diagnosis

Important alternatives include spastic diplegic cerebral palsy, SPG4 and other HSPs, multiple sclerosis, structural/compressive spinal disease, vitamin B12 deficiency, adrenomyeloneuropathy/ABCD1 disease, Friedreich ataxia, ARSACS, primary lateral sclerosis, dopa-responsive dystonia, leukodystrophy, and metabolic disease. (toft2017clinicalandgenetic pages 16-18, toft2017clinicalandgenetic pages 6-8)

## 11. Outcome and prognosis

Typical SPG3A has slow progression, preserved cognition, and long-term ambulation; lifespan is generally not shortened. There are no robust SPG3A-specific 5- or 10-year survival, mortality, or life-expectancy estimates. (hamamiechaar2024patientswithcomplex pages 1-2, awuah2024hereditaryspasticparaplegia pages 1-2, bick1993uncomplicated(pure)hereditary pages 1-3)

Morbidity arises from gait limitation, falls, weakness, fatigue, pain/spasms, urinary urgency, contractures, scoliosis, and eventual aid dependence. Severe biallelic or de novo presentations can include profound developmental disability, dysphagia, seizures, and wheelchair dependence. (hamamiechaar2024patientswithcomplex pages 1-2, hamamiechaar2024patientswithcomplex pages 2-4)

Likely prognostic factors include age and severity at onset, complex neurologic features, variant-specific residual function, and early development of fixed orthopedic deformity. There is no validated molecular prognostic biomarker or SPG3A risk calculator. Recovery from the genetic disorder is not expected, although function can improve with symptom treatment and rehabilitation.

## 12. Treatment

### Present standard of care

No treatment halts or reverses ATL1 disease. Evidence is almost entirely extrapolated from mixed-HSP cohorts rather than SPG3A-specific trials. A 2019 systematic review found only 27 eligible treatment reports—17 pharmacologic, five physical-therapy, and five surgical—and concluded that the evidence base was inadequate. (bellofatto2019managementofhereditary pages 1-2)

- **Physical therapy and exercise:** individualized stretching, strengthening, balance, aerobic conditioning, gait training, and home programs. Suggested NCIT concepts: Physical Therapy, Exercise Therapy, Rehabilitation Therapy.
- **Orthotics and mobility technology:** ankle-foot orthoses, canes, walkers, wheelchairs, and fall-prevention adaptations. NCIT: Orthopedic Device, Assistive Device.
- **Oral antispasticity drugs:** baclofen, tizanidine, or dantrolene, titrated to function. Weakness and sedation can worsen gait. NCIT: Pharmacologic Therapy; Muscle Relaxant Therapy. (toft2017clinicalandgenetic pages 6-8)
- **Focal botulinum toxin A:** for function-limiting focal spasticity, combined with stretching/therapy. NCIT: Botulinum Toxin Therapy.
- **Intrathecal baclofen:** an option for severe generalized spasticity refractory to oral therapy after a screening trial. NCIT: Intrathecal Drug Administration.
- **Bladder management:** timed voiding, urologic assessment, and agents such as oxybutynin when appropriate. NCIT: Anticholinergic Therapy.
- **Orthopedic intervention:** contracture or deformity procedures, including selected tendon surgery, only after multidisciplinary assessment. (maccora2024nonpharmacologicaltreatmentof pages 1-2, toft2017clinicalandgenetic pages 6-8)

Gabapentin failed to show significant improvement in the best-designed study included in the 2019 HSP review. Evidence for physical and surgical approaches was low-to-moderate quality. (bellofatto2019managementofhereditary pages 1-2)

### Experimental and advanced therapeutics

GW3965/LXR activation restored lipid-droplet and cholesterol-transfer defects and rescued axonal degeneration in human SPG3A stem-cell models. Direct cholesterol exposure also rescued cellular transport and swelling phenotypes. These findings do **not** justify off-label human use because efficacy, dosage, blood–brain-barrier exposure, and safety are untested clinically. (mou2020impairedlipidmetabolism pages 1-2)

Gene replacement, allele-selective silencing, RNA therapy, and CRISPR correction remain conceptual/preclinical. Dominant disease may require variant-specific suppression plus replacement rather than simple gene augmentation; rare recessive loss-of-function disease could present a different therapeutic problem. No retrieved ClinicalTrials.gov record represented a disease-modifying SPG3A-specific interventional trial.

No established ATL1 pharmacogenomic rule or genotype-directed approved therapy exists.

## 13. Prevention

Primary lifestyle prevention is impossible because SPG3A is germline genetic disease. Vaccination, antimicrobial prophylaxis, and environmental regulation are not disease-specific measures.

**Genetic primary prevention/family planning** may include preconception counseling, parental testing, cascade testing, preimplantation genetic testing for a known familial pathogenic variant, chorionic-villus sampling, or amniocentesis. Counseling must address incomplete penetrance, variable expressivity, de novo disease, and rare recessive inheritance. (toft2017clinicalandgenetic pages 16-18, rudenskaya2020clinicalmolecularand pages 1-2, hamamiechaar2024patientswithcomplex pages 1-2)

**Secondary prevention** consists of early recognition—especially among children diagnosed with atypical cerebral palsy—and prompt rehabilitation before contractures develop. Predictive testing of asymptomatic adult relatives should follow formal genetic counseling. Testing minors is generally appropriate when surveillance or childhood intervention has potential benefit.

**Tertiary prevention** includes stretching, activity, orthoses, fall prevention, bladder surveillance, osteoporosis-risk management where mobility is reduced, and monitoring for scoliosis, contracture, dysphagia, and neuropathy. There is no population carrier-screening or newborn-screening program.

## 14. Other species and natural disease

Orthologs are conserved across mammals and major laboratory species, including *Mus musculus* (NCBI Taxon **10090**), *Rattus norvegicus* (**10116**), *Danio rerio* (**7955**), *Drosophila melanogaster* (**7227**), and *Caenorhabditis elegans* (**6239**). Species-specific NCBI Gene IDs should be populated directly from the current NCBI Orthologs release.

No well-established naturally occurring ATL1-linked veterinary disease or breed predisposition equivalent to human SPG3A was identified. Therefore VBO breed annotations, veterinary prevalence, and cross-species transmission are unavailable/not applicable. SPG3A has no zoonotic potential.

## 15. Model organisms and experimental systems

### Human stem-cell models

Isogenic ATL1-A161P hESCs and ATL1-P342S patient iPSCs reproduce reduced axon growth, impaired transport, swellings, astrocyte lipid-droplet defects, and defective cholesterol transfer. Genetic correction and pharmacologic rescue strengthen causal inference. Their limitations include immature cells, absence of lifelong circuitry and biomechanics, and uncertain translation of compound exposure. (mou2020impairedlipidmetabolism pages 1-2)

A 2022 microfluidic model generated autologous lower motor neurons and myotubes from three SPG3A and two SPG4 patients. HSP cultures formed fewer and less-complex NMJs and showed axonal swellings and acetylated α-tubulin accumulation. Because some outcomes were pooled across genotypes, they should not all be entered as uniquely SPG3A-specific. (costamagna2022autologousipscderivedhuman pages 1-2)

### Drosophila

Atlastin knockdown/knockout causes fragmented neuronal or muscular ER, synaptic bouton abnormalities, impaired crawling/climbing, microtubule disorganization, reduced survival, and developmental defects. CRISPR knock-in variants R214C, C350R, M383T, and R192Q produced different residual-activity/severity patterns, supporting mutation-specific rather than uniform dominant-negative action. (damiani2024pluripotentstemcells pages 3-3, vivarelli2025wingsofdiscovery pages 7-8)

### Zebrafish

ATL1 morphants show reduced larval motility and increased spinal-motor-axon branching. Overexpression can alter ventral development, likely through BMP-pathway effects. Zebrafish are useful for rapid developmental and compound studies but lack a mammalian corticospinal tract. (damiani2024pluripotentstemcells pages 2-3)

### Rodent neuronal systems

ATL1 knockdown in mouse cortical neurons impairs axon growth and dendritic branching. Wild-type and R217Q perturbations have produced dendritic-segment or spine/protein-synthesis abnormalities in cortical or hippocampal cultures. Whole-animal SPG models often have weaker motor phenotypes than human disease, limiting natural-history and efficacy prediction. (damiani2024pluripotentstemcells pages 2-3)

### Recommended resource links

- MONDO: https://monarchinitiative.org/disease/MONDO:0008437
- OMIM: https://omim.org/entry/182600
- NCBI Gene ATL1: https://www.ncbi.nlm.nih.gov/gene/?term=ATL1
- ClinVar ATL1: https://www.ncbi.nlm.nih.gov/clinvar/?term=ATL1%5Bgene%5D
- GTR: https://www.ncbi.nlm.nih.gov/gtr/all/tests/?term=ATL1
- Orphanet: https://www.orpha.net/
- HPO: https://hpo.jax.org/
- ClinicalTrials.gov: https://clinicaltrials.gov/search?cond=Hereditary%20Spastic%20Paraplegia

## Evidence limitations and knowledge-base cautions

1. Most treatment, quality-of-life, prognosis, and biomarker evidence is HSP-wide rather than SPG3A-specific.
2. Published phenotype frequencies are strongly affected by referral and family ascertainment.
3. Severe recessive SPG3A is supported by only a few families and should be represented as an emerging, rare inheritance mechanism—not coequal in frequency with dominant disease.
4. ATL1 variant mechanism is heterogeneous; do not annotate all pathogenic variants automatically as dominant-negative or complete loss-of-function.
5. Experimental cholesterol/LXR rescue is preclinical and must not be represented as an established treatment.
6. Exact HPO, GO, CL, UBERON, ORPHA, SNOMED CT, ICD-11, HGNC, NCBI Gene, and NCIT accessions should be programmatically validated against the knowledge base’s ontology release before production ingestion.

References

1. (rudenskaya2020clinicalmolecularand pages 1-2): G. Rudenskaya, V. Kadnikova, Christian Beetz, Tatyana N. Proskokova, I. Sermyagina, Anna A. Stepanova, Valery P. Fedotov, E. Dadaly, Darya M. Guseva, Тatiana V. Markova, and O. P. Ryzhkova. Clinical, molecular, and genetic characteristics of the hereditary spastic paraplegia type 3. №1 (2020), Mar 2020. URL: https://doi.org/10.25692/acen.2020.1.5, doi:10.25692/acen.2020.1.5. This article has 0 citations.

2. (hamamiechaar2024patientswithcomplex pages 1-2): Angélique Hamamie-Chaar, Mathilde Renaud, Pinar Gençpinar, Ange-Line Bruel, Christophe Philippe, Julien Maraval, Caroline Racine, Nawale Hadouiri, Laetitia Lambert, Emmanuelle Schmitt, Guillaume Banneau, Armand Hocquel, Christel Thauvin-Robinet, Laurence Faivre, and Quentin Thomas. Patients with complex and very-early-onset atl1-related spastic paraplegia offer insights on genotype/phenotype correlations and support for autosomal recessive forms of spg3a. Journal of Neurology, 271:6343-6348, Jul 2024. URL: https://doi.org/10.1007/s00415-024-12565-0, doi:10.1007/s00415-024-12565-0. This article has 4 citations and is from a domain leading peer-reviewed journal.

3. (hamamiechaar2024patientswithcomplex pages 2-4): Angélique Hamamie-Chaar, Mathilde Renaud, Pinar Gençpinar, Ange-Line Bruel, Christophe Philippe, Julien Maraval, Caroline Racine, Nawale Hadouiri, Laetitia Lambert, Emmanuelle Schmitt, Guillaume Banneau, Armand Hocquel, Christel Thauvin-Robinet, Laurence Faivre, and Quentin Thomas. Patients with complex and very-early-onset atl1-related spastic paraplegia offer insights on genotype/phenotype correlations and support for autosomal recessive forms of spg3a. Journal of Neurology, 271:6343-6348, Jul 2024. URL: https://doi.org/10.1007/s00415-024-12565-0, doi:10.1007/s00415-024-12565-0. This article has 4 citations and is from a domain leading peer-reviewed journal.

4. (mou2020impairedlipidmetabolism pages 1-2): Yongchao Mou, Yi Dong, Zhenyu Chen, Kyle R. Denton, Michael O. Duff, Craig Blackstone, Su-Chun Zhang, and Xue-Jun Li. Impaired lipid metabolism in astrocytes underlies degeneration of cortical projection neurons in hereditary spastic paraplegia. Acta Neuropathologica Communications, Dec 2020. URL: https://doi.org/10.1186/s40478-020-01088-0, doi:10.1186/s40478-020-01088-0. This article has 42 citations and is from a peer-reviewed journal.

5. (sonda2021ermorphologyin pages 5-6): Sonia Sonda, Diana Pendin, and Andrea Daga. Er morphology in the pathogenesis of hereditary spastic paraplegia. Cells, 10:2870, Oct 2021. URL: https://doi.org/10.3390/cells10112870, doi:10.3390/cells10112870. This article has 21 citations.

6. (crosby2021reconstitutionofhuman pages 1-2): Daniel Crosby, Melissa R. Mikolaj, Sarah B. Nyenhuis, Samantha Bryce, Jenny E. Hinshaw, and Tina H. Lee. Reconstitution of human atlastin fusion activity reveals autoinhibition by the c terminus. The Journal of Cell Biology, Nov 2021. URL: https://doi.org/10.1083/jcb.202107070, doi:10.1083/jcb.202107070. This article has 23 citations.

7. (maccora2024nonpharmacologicaltreatmentof pages 1-2): Simona Maccora, Angelo Torrente, Vincenzo Di Stefano, Antonino Lupica, Salvatore Iacono, Laura Pilati, Antonia Pignolo, and Filippo Brighina. Non-pharmacological treatment of hereditary spastic paraplegia: a systematic review. Neurological Sciences, 45:963-976, Nov 2024. URL: https://doi.org/10.1007/s10072-023-07200-1, doi:10.1007/s10072-023-07200-1. This article has 10 citations and is from a peer-reviewed journal.

8. (bellofatto2019managementofhereditary pages 1-2): Marta Bellofatto, Giovanna De Michele, Aniello Iovino, Alessandro Filla, and Filippo M. Santorelli. Management of hereditary spastic paraplegia: a systematic review of the literature. Frontiers in Neurology, Jan 2019. URL: https://doi.org/10.3389/fneur.2019.00003, doi:10.3389/fneur.2019.00003. This article has 104 citations and is from a peer-reviewed journal.

9. (kadnikova2019mutationalspectrumof pages 1-2): V. A. Kadnikova, G. E. Rudenskaya, A. A. Stepanova, I. G. Sermyagina, and O. P. Ryzhkova. Mutational spectrum of spast (spg4) and atl1 (spg3a) genes in russian patients with hereditary spastic paraplegia. Scientific Reports, Oct 2019. URL: https://doi.org/10.1038/s41598-019-50911-9, doi:10.1038/s41598-019-50911-9. This article has 34 citations and is from a peer-reviewed journal.

10. (bick1993uncomplicated(pure)hereditary pages 1-3): S Bick and GM Mirzaa. Uncomplicated (pure) hereditary spastic paraplegia overview. Unknown journal, 1993.

11. (costamagna2022autologousipscderivedhuman pages 1-2): Domiziana Costamagna, Valérie Casters, Marc Beltrà, Maurilio Sampaolesi, Anja Van Campenhout, Els Ortibus, Kaat Desloovere, and Robin Duelen. Autologous ipsc-derived human neuromuscular junction to model the pathophysiology of hereditary spastic paraplegia. Cells, 11:3351, Oct 2022. URL: https://doi.org/10.3390/cells11213351, doi:10.3390/cells11213351. This article has 7 citations.

12. (toft2017clinicalandgenetic pages 6-8): A Toft. Clinical and genetic characterization of hereditary spastic paraplegia. Unknown journal, 2017.

13. (denton2015modellinghereditaryspastic pages 13-17): K Denton. Modelling hereditary spastic paraplegias using human pluripotent stem cells. Unknown journal, 2015.

14. (OpenTargets Search: Hereditary spastic paraplegia 3A-ATL1): Open Targets Query (Hereditary spastic paraplegia 3A-ATL1, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

15. (khan2014evidenceforautosomal pages 5-5): Tahir Naeem Khan, Joakim Klar, Muhammad Tariq, Shehla Anjum Baig, Naveed Altaf Malik, Raja Yousaf, Shahid Mahmood Baig, and Niklas Dahl. Evidence for autosomal recessive inheritance in spg3a caused by homozygosity for a novel atl1 missense mutation. European Journal of Human Genetics, 22:1180-1184, Jan 2014. URL: https://doi.org/10.1038/ejhg.2014.5, doi:10.1038/ejhg.2014.5. This article has 59 citations and is from a domain leading peer-reviewed journal.

16. (awuah2024hereditaryspasticparaplegia pages 1-2): Wireko Andrew Awuah, Joecelyn Kirani Tan, Anastasiia D Shkodina, Tomas Ferreira, Favour Tope Adebusoye, Adele Mazzoleni, Jack Wellington, Lian David, Ellie Chilcott, Helen Huang, Toufik Abdul-Rahman, Vallabh Shet, Oday Atallah, Jacob Kalmanovich, Riaz Jiffry, Divine Elizabeth Madhu, Kateryna Sikora, Oleksii Kmyta, and Mykhailo Yu Delva. Hereditary spastic paraplegia: novel insights into the pathogenesis and management. SAGE Open Medicine, Dec 2024. URL: https://doi.org/10.1177/20503121231221941, doi:10.1177/20503121231221941. This article has 31 citations.

17. (damiani2024pluripotentstemcells pages 3-3): Devid Damiani, Matteo Baggiani, Stefania Della Vecchia, Valentina Naef, and Filippo Maria Santorelli. Pluripotent stem cells as a preclinical cellular model for studying hereditary spastic paraplegias. International Journal of Molecular Sciences, 25:2615, Feb 2024. URL: https://doi.org/10.3390/ijms25052615, doi:10.3390/ijms25052615. This article has 12 citations.

18. (damiani2024pluripotentstemcells pages 2-3): Devid Damiani, Matteo Baggiani, Stefania Della Vecchia, Valentina Naef, and Filippo Maria Santorelli. Pluripotent stem cells as a preclinical cellular model for studying hereditary spastic paraplegias. International Journal of Molecular Sciences, 25:2615, Feb 2024. URL: https://doi.org/10.3390/ijms25052615, doi:10.3390/ijms25052615. This article has 12 citations.

19. (meyyazhagan2022hereditaryspasticparaplegia pages 1-2): Arun Meyyazhagan and Antonio Orlacchio. Hereditary spastic paraplegia: an update. International Journal of Molecular Sciences, 23:1697, Feb 2022. URL: https://doi.org/10.3390/ijms23031697, doi:10.3390/ijms23031697. This article has 203 citations.

20. (toft2017clinicalandgenetic pages 16-18): A Toft. Clinical and genetic characterization of hereditary spastic paraplegia. Unknown journal, 2017.

21. (vivarelli2025wingsofdiscovery pages 7-8): Rachele Vivarelli, Chiara Vantaggiato, Maria Teresa Bassi, Filippo Maria Santorelli, and Maria Marchese. Wings of discovery: using drosophila to decode hereditary spastic paraplegia and ataxias. Sep 2025. URL: https://doi.org/10.3390/cells14181466, doi:10.3390/cells14181466. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Hereditary_Spastic_Paraplegia_3A-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008437` (4 mentions) - the report calls it "if available"; MONDO calls it **hereditary spastic paraplegia 3A**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007029` (2 mentions) - the report calls it "ER organization"; GO calls it **endoplasmic reticulum organization**, and lists "ER organisation" among its other names