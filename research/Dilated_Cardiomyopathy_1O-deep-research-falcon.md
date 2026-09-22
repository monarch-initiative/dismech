---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T20:29:31.480487'
end_time: '2026-09-03T20:47:23.651015'
duration_seconds: 1072.17
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dilated Cardiomyopathy 1O
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 57
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 7
  verified: 7
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0000948
    reported_labels:
    - Suggested UBERON concepts:** heart
    ontology_label: heart
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dilated_Cardiomyopathy_1O-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1O
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1O** covering all of the
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
- **Disease Name:** Dilated Cardiomyopathy 1O
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1O** covering all of the
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


# Dilated Cardiomyopathy 1O (CMD1O): Disease-Characteristics Research Report

## Executive summary and evidence warning

Dilated cardiomyopathy 1O (CMD1O) is the historical designation for an adult-onset dilated-cardiomyopathy/ventricular-arrhythmia phenotype attributed to heterozygous variants in **ABCC9**, which encodes the cardiac ATP-sensitive potassium-channel regulatory subunit SUR2A. Its identifiers are **MONDO:0012062** and **OMIM #608569**. The foundational report found only two ABCC9 variants among 323 people with idiopathic DCM, although both altered channel behavior in functional assays. Modern evidence appraisal is therefore crucial: a 2024 review reports the autosomal-dominant ABCC9–DCM relationship as **ClinGen Limited**, not Strong or Definitive. CMD1O should consequently be represented as a historically asserted, biologically plausible but incompletely validated Mendelian disease entity—not as an unqualified, firmly established monogenic diagnosis. (bienengraeber2004abcc9mutationsidentified pages 2-2, micolonghi2024unveilingthespectrum pages 25-26, micolonghi2024unveilingthespectrum pages 8-9)

The strongest disease-specific evidence remains Bienengraeber et al., *Nature Genetics*, online 21 March 2004/April 2004, DOI [10.1038/ng1329](https://doi.org/10.1038/ng1329), PMID **15034580**. The authors’ abstract states: “Scanning of genomic DNA from individuals with heart failure and rhythm disturbances due to idiopathic dilated cardiomyopathy identified two mutations in ABCC9,” and concludes that defective pore regulation is “a mechanism for channel dysfunction and susceptibility to dilated cardiomyopathy.” The wording “susceptibility” is appropriate given the limited human-genetic evidence. (bienengraeber2004abcc9mutationsidentified pages 2-2, bienengraeber2004abcc9mutationsidentified pages 1-2)

| Domain | Best-supported finding | Evidence type | Confidence/caveat |
|---|---|---|---|
| Identifiers | Dilated cardiomyopathy 1O (CMD1O); **MONDO:0012062**; **OMIM 608569**. | Aggregated disease databases | Stable historical identifiers; no dedicated ICD-10/ICD-11 code. (OpenTargets Search: Dilated cardiomyopathy 1O, olson2010humankatpchannelopathies pages 5-6) |
| Gene/protein | **ABCC9** (MIM 601439) encodes SUR2; cardiac SUR2A partners with Kir6.2/KCNJ11 in ATP-sensitive K⁺ channels. | Database, biochemical | Gene–protein relationship is established; gene–CMD1O causality is less certain. (olson2010humankatpchannelopathies pages 5-6, micolonghi2024unveilingthespectrum pages 8-9) |
| Original variants/cases | A 323-patient DCM screen found heterozygous **c.4537G>A (p.Ala1513Thr)** in a woman diagnosed at 40 and **c.4570_4572delTTAinsAAAT (p.Leu1524fs)** in a man diagnosed at 55; neither occurred in 500 controls. | Human case-level genetics | Only two index cases; limited segregation and no robust independent replication. (bienengraeber2004abcc9mutationsidentified pages 2-2, bienengraeber2004abcc9mutationsidentified pages 1-2) |
| Clinical validity | Modern review classifies the autosomal-dominant **ABCC9–DCM** relationship as **ClinGen Limited**. | Expert curation/database review | ABCC9 findings should not independently establish diagnosis or direct predictive testing without rigorous variant-level evidence. (micolonghi2024unveilingthespectrum pages 25-26) |
| Core phenotype | Severe LV dilation and systolic dysfunction with ventricular tachycardia; reported LVEFs were 15% and 23%, and both index cases developed fatal or severe heart failure. | Human case reports | Adult-onset observations only; penetrance, phenotype frequencies, and full spectrum are unknown. (bienengraeber2004abcc9mutationsidentified pages 2-2, olson2010humankatpchannelopathies pages 5-6) |
| Proposed mechanism | Variants flank the SUR2A ATPase pocket, disturb nucleotide-dependent conformational cycling, and impair KATP metabolic-signal decoding and pore gating. | In vitro electrophysiology/biochemistry | Functional effect demonstrated; causal path from channel dysfunction to human DCM remains incompletely proven. (bienengraeber2004abcc9mutationsidentified pages 2-2, bienengraeber2004abcc9mutationsidentified pages 1-2) |
| Models | SUR2 loss causes cardiac dysfunction in mice and ventricular enlargement/dysfunction in zebrafish; KATP-deficient mice develop stress-induced calcium/calcineurin-dependent remodeling. | Mouse and zebrafish | Supportive but not exact CMD1O-variant models; related KCNJ11 knockout evidence is indirect. (kane2006kcnj11geneknockout pages 1-2, smeland2019abcc9relatedintellectualdisability pages 1-2, kane2005cardiackatpchannels pages 10-10) |
| Contradictory/context evidence | Adult cardiomyocyte-specific SUR2 deletion increased glucose uptake and protected mice from ischemia–reperfusion injury. | Conditional mouse model | Shows tissue-, age-, and stress-dependent effects; global deletion is confounded by vascular dysfunction and vasospasm. (aubert2019deletionofsulfonylurea pages 1-2) |
| Diagnosis | Establish the DCM phenotype using history/pedigree, ECG, biomarkers, echocardiography and CMR; exclude coronary/loading and acquired causes, then use a curated cardiomyopathy panel with counseling and segregation analysis. | Clinical guidelines | An ABCC9 VUS is non-diagnostic; cascade testing is appropriate only for a convincingly pathogenic familial variant. (sorella2025diagnosisandmanagement pages 2-3, sorella2025diagnosisandmanagement pages 12-13, micolonghi2024unveilingthespectrum pages 25-26) |
| Treatment | Treat manifest HFrEF with ARNI/ACEi/ARB, evidence-based β-blocker, MRA and SGLT2 inhibitor; add diuretics for congestion and consider ICD/CRT, LVAD or transplantation by standard criteria. | Guideline extrapolation | General DCM/HFrEF care, not genotype-specific CMD1O evidence. (badger2023summaryandcomparison pages 9-11, badger2023summaryandcomparison pages 11-12, sorella2025diagnosisandmanagement pages 12-13) |
| Targeted therapy/trials | No ABCC9-specific approved therapy or CMD1O clinical trial was identified; KATP modulators remain mechanistic/preclinical concepts. | Trial search and pharmacology review | Absence of retrieved trials is not proof that none exists globally; channel modulation may have opposing tissue-specific effects. (aubert2019deletionofsulfonylurea pages 1-2, nichols2023personalizedtherapeuticsfor pages 4-6) |


*Table: A compact, database-oriented summary of CMD1O identity, foundational human evidence, current gene-validity concerns, mechanism, models, diagnosis, and treatment.*

---

## 1. Disease information

### Definition

CMD1O denotes DCM associated historically with ABCC9/SUR2A dysfunction. DCM itself is defined by left-ventricular, or sometimes biventricular, dilatation with global or regional systolic dysfunction that is not adequately explained by coronary artery disease or abnormal loading from hypertension, valve disease, or congenital heart disease. Ventricular arrhythmia—particularly ventricular tachycardia—was prominent in the original CMD1O cases. (olson2010humankatpchannelopathies pages 5-6, sorella2025diagnosisandmanagement pages 1-2, sorella2025diagnosisandmanagement pages 2-3)

### Identifiers and synonyms

- **MONDO:** MONDO:0012062.
- **OMIM phenotype:** #608569.
- **Gene:** ABCC9; OMIM gene **601439**; Ensembl ENSG00000069431.
- **Preferred/synonymous labels:** dilated cardiomyopathy 1O; cardiomyopathy, dilated, 1O; CMD1O; DCM1O; ABCC9-related dilated cardiomyopathy.
- **MeSH:** use the parent concept *Cardiomyopathy, Dilated*; no uniquely specific CMD1O MeSH descriptor was identified.
- **ICD-10-CM:** use the general DCM code **I42.0**; there is no CMD1O-specific code.
- **ICD-11:** classify under dilated cardiomyopathy; no ABCC9/CMD1O-specific code was verified.

Open Targets maps MONDO:0012062 to ABCC9, but database association is not equivalent to definitive clinical validity. (OpenTargets Search: Dilated cardiomyopathy 1O)

### Provenance

The disease entry derives from **aggregated disease-level resources plus published research subjects**, not longitudinal EHR-derived characterization. The defining human evidence comprises two index cases and one clinically affected father; recent statistics cited below concern DCM generally and must not be interpreted as CMD1O-specific. (bienengraeber2004abcc9mutationsidentified pages 2-2, bienengraeber2004abcc9mutationsidentified pages 1-2)

---

## 2. Etiology

### Causal assertion and genetic risk

The historical causal assertion is heterozygous ABCC9 dysfunction affecting SUR2A-dependent cardiac KATP channels. In the original screen of 323 affected individuals, two exon-38 variants were found:

1. **c.4537G>A, p.Ala1513Thr** (reported originally as A1513T).
2. **c.4570_4572delTTAinsAAAT**, producing a frameshift beginning at Leu1524, four abnormal terminal residues, and premature termination (reported as Fs1524; exact modern protein HGVS should be transcript-validated).

Neither occurred among 500 unrelated controls. Both were germline heterozygous variants. The affected woman’s father also had severe DCM, supporting vertical transmission, but DNA-based segregation was unavailable; the affected man had no reported family history. (bienengraeber2004abcc9mutationsidentified pages 2-2, bienengraeber2004abcc9mutationsidentified pages 1-2, olson2010humankatpchannelopathies pages 5-6)

**Interpretive qualification:** the variants are historically described as disease mutations, but contemporary pathogenicity should be reassessed using the current MANE transcript, population frequency, ClinVar submissions, segregation, phenotype specificity, and ACMG/AMP criteria. The current gene–disease relationship is only **Limited**; a VUS in ABCC9 must not be used to diagnose CMD1O or predict disease in relatives. The 2024 review tabulated nine ClinVar P/LP entries but 712 VUS, illustrating the interpretive uncertainty. (micolonghi2024unveilingthespectrum pages 25-26)

### Environmental and acquired risk factors

No environmental exposure has been demonstrated specifically in CMD1O. Mechanistically, impaired KATP metabolic sensing is expected to become consequential under increased energetic or hemodynamic demand. Related knockout models were relatively mild at baseline but developed calcium overload, arrhythmia, maladaptive remodeling, heart failure, and death during exercise, adrenergic stress, or experimental hypertension. Thus, hypertension and intense physiological stress are plausible “second hits,” but this remains inference rather than demonstrated CMD1O epidemiology. (kane2006kcnj11geneknockout pages 1-2, olson2010humankatpchannelopathies pages 5-6, kane2005cardiackatpchannels pages 10-10)

For DCM generally, relevant acquired contributors include alcohol, anthracyclines and other cardiotoxic therapies, pregnancy/peripartum stress, myocarditis, tachyarrhythmia, metabolic disease, and hypertension. These should be sought because finding an ABCC9 variant does not establish that it caused the phenotype. General DCM data also show adverse interaction with diabetes: in 1,152 nonischemic-DCM patients, 13% had type 2 diabetes; annual death/transplant events were 10.2% versus 5.7%, and adjusted risk was HR 1.61. (li2024theimpactof pages 1-2)

### Protective factors

No protective ABCC9 allele is established for CMD1O. Reasonable environmental protection is extrapolated from DCM/HF care: blood-pressure control, avoidance of cardiotoxins and heavy alcohol, treatment of diabetes and sleep-disordered breathing, vaccination and prompt infection care where appropriate, moderate prescribed exercise rather than unassessed high-intensity exertion, and early treatment of ventricular dysfunction. These reduce general cardiac stress but have not been tested specifically in CMD1O.

---

## 3. Phenotypes

The tiny disease-specific sample precludes valid percentages. Frequencies should be recorded as **observed in the original cases**, not as population estimates.

| Phenotype | Type and characteristics | Disease-specific observation | Suggested HPO term |
|---|---|---|---|
| Dilated cardiomyopathy | Structural/functional sign; adult onset; severe and progressive | Present in both index cases and affected father | Dilated cardiomyopathy, **HP:0001644** |
| LV dilatation | Imaging sign | LVEDD 65 mm in the male; 89 mm in the female; 81 mm in her father | Left ventricular dilatation |
| Severe LV systolic dysfunction | Imaging/functional abnormality | LVEF 23%, 15%, and 13%, respectively | Decreased left ventricular ejection fraction |
| Ventricular tachycardia | Electrophysiological sign; potentially episodic and life-threatening | Reported in both index cases | Ventricular tachycardia, **HP:0004756** |
| Heart failure | Clinical syndrome; progressive | Male died at 60; affected father died at 55; female required intensive therapy | Congestive heart failure, **HP:0001635** |
| Cardiomegaly/ventricular enlargement | Imaging/physical sign | Consequence of marked dilation | Cardiomegaly, **HP:0001640** |
| Exercise intolerance, dyspnea, fatigue, edema | Symptoms expected from severe HFrEF | Not systematically quantified in the defining report | Exercise intolerance; dyspnea; fatigue; peripheral edema |

The male was diagnosed at 55 and died of HF at 60. The female was diagnosed at 40; her father was diagnosed at 54 and died at 55. This supports adult onset with severe expression, but does not exclude preclinical disease or other ages of onset. Quality-of-life effects were not measured with EQ-5D, SF-36, Kansas City Cardiomyopathy Questionnaire, or another instrument; severe HFrEF and ventricular tachycardia would nevertheless be expected to impair exertion, employment, driving, and psychosocial well-being. (bienengraeber2004abcc9mutationsidentified pages 2-2, bienengraeber2004abcc9mutationsidentified pages 1-2)

Neurologic, myopathic, and white-matter phenotypes belong principally to **biallelic ABCC9-related intellectual disability and myopathy syndrome (AIMS)**, not classical heterozygous CMD1O. A 2024 *Brain* study added nine individuals from seven families with homozygous loss-of-function variants; heterozygous parents generally lacked a conserved phenotype. AIMS should not be conflated with CMD1O, although occasional older heterozygotes had cardiac disease. DOI [10.1093/brain/awae010](https://doi.org/10.1093/brain/awae010), published January 2024. (efthymiou2024novellossoffunctionvariants pages 2-4, efthymiou2024novellossoffunctionvariants pages 8-9)

---

## 4. Genetic and molecular information

### Gene/protein

- **Gene:** ABCC9, ATP-binding cassette subfamily C member 9.
- **Protein:** sulfonylurea receptor 2 (SUR2); cardiac alternative terminal exon usage generates SUR2A.
- **Cardiac channel:** hetero-octameric KATP complex comprising four SUR2A regulatory subunits and four Kir6.2 pore subunits encoded by **KCNJ11**.
- **Cellular location:** predominantly cardiomyocyte sarcolemma/plasma membrane; SUR2-containing channels also occur in vascular smooth muscle, creating tissue-specific effects.

### Variant consequences

Both original variants lie in evolutionarily conserved C-terminal sequence near the SUR2A catalytic ATPase pocket/Walker A region. Recombinant studies showed disturbed nucleotide-dependent conformational cycling and compromised metabolic-signal decoding. Reduced surface expression was reported, although pore conduction itself remained possible; the key defect was regulatory/catalytic gating rather than a simple absence of potassium permeability. (bienengraeber2004abcc9mutationsidentified pages 2-2, bienengraeber2004abcc9mutationsidentified pages 1-2)

The proposed effect is best described as **disruptive/loss-of-regulatory function**. A dominant-negative mechanism was not conclusively demonstrated. Population allele frequencies were not supplied beyond absence in 500 historical controls; current gnomAD frequencies should be checked against a transcript-normalized HGVS representation before clinical interpretation.

### Related ABCC9 allelic disorders

- **Biallelic loss of function:** AIMS, with developmental impairment, myopathy/fatigability, CNS abnormalities, and sometimes cardiac systolic dysfunction. The 2024 study functionally confirmed nonfunctional channels for severe truncating/splice variants. (efthymiou2024novellossoffunctionvariants pages 2-4, efthymiou2024novellossoffunctionvariants pages 8-9)
- **Heterozygous gain of function:** Cantú syndrome, characterized by hypertrichosis, vascular dilation, hypotension, and cardiomegaly; this is mechanistically opposite to proposed CMD1O loss of metabolic gating. (nichols2023personalizedtherapeuticsfor pages 4-6)

No validated CMD1O-specific modifier gene, protective allele, recurrent chromosomal abnormality, germline-mosaicism series, or epigenetic signature was identified. No evidence supports a somatic origin.

---

## 5. Environmental information

There is no CMD1O-specific toxin, infectious agent, occupational exposure, diet, or lifestyle association. The practical etiologic work-up should nevertheless assess alcohol, cocaine or stimulants, cardiotoxic chemotherapy, immune-checkpoint inhibitors, pregnancy, endocrine and nutritional abnormalities, sustained tachycardia, hypertension, and myocarditis. Viral infection can trigger myocarditis and a DCM phenotype, but no pathogen is intrinsic to CMD1O.

The most defensible gene–environment model is that defective KATP metabolic–electrical coupling lowers myocardial stress tolerance, while hemodynamic, ischemic, adrenergic, or metabolic stress supplies the second hit. This is strongly supported in related channel-deficient animals but remains **inferred** for the two human CMD1O variants. (kane2006kcnj11geneknockout pages 1-2, kane2005cardiackatpchannels pages 10-10)

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous C-terminal ABCC9 variant **leads to** altered SUR2A abundance and/or ATPase-domain conformational cycling.
2. Altered SUR2A catalysis **results in** defective Mg-nucleotide-dependent regulation of the Kir6.2 potassium pore and impaired decoding of the ATP/ADP state. (bienengraeber2004abcc9mutationsidentified pages 2-2, olson2010humankatpchannelopathies pages 5-6)
3. Impaired KATP gating **leads to** failure to adapt action-potential duration and contractile work to energetic demand, particularly during adrenergic, ischemic, exercise, or pressure stress; this human step is mechanistically supported but partly inferred. (kane2006kcnj11geneknockout pages 1-2, olson2010humankatpchannelopathies pages 5-6)
4. Failed metabolic–electrical adaptation **results in** excessive calcium entry/overload and electrical instability; related KCNJ11-null mice demonstrate a calcium/calcineurin-dependent, cyclosporine-sensitive pathway. Extrapolation to ABCC9-CMD1O is indirect. (kane2006kcnj11geneknockout pages 1-2)
5. Calcium dysregulation and repeated energetic stress **lead to two branches**:
   - **Electrical branch:** abnormal repolarization and triggered/re-entrant activity **result in** ventricular tachycardia and risk of sudden death.
   - **Mechanical branch:** cardiomyocyte injury and maladaptive remodeling **result in** chamber dilatation, declining contractility, HFrEF, and secondary fibrosis.
6. Progressive low-output and congestive physiology **leads to** exercise intolerance, neurohormonal activation, pulmonary/systemic congestion, advanced HF, transplantation, or death.

### Processes, pathways, and ontology suggestions

- **Upstream:** ATP/ADP sensing, ATP hydrolysis, KATP-channel gating, potassium transport, membrane repolarization.
- **Intermediate:** cardiac action-potential regulation, excitation–contraction coupling, calcium-ion homeostasis, calcineurin signaling, energetic adaptation.
- **Downstream:** cardiomyocyte injury, hypertrophic/remodeling response, fibrosis, chamber dilation, systolic dysfunction, arrhythmogenesis.
- **Suggested GO biological processes:** ATP-sensitive potassium-channel activity/regulation; potassium-ion transmembrane transport; regulation of membrane potential; cardiac action-potential regulation; cellular response to hypoxia; calcium-ion homeostasis; cardiac muscle contraction; regulation of heart growth; response to mechanical stimulus.
- **Suggested GO cellular components:** plasma membrane; sarcolemma; ATP-sensitive potassium-channel complex; nucleotide-binding domain.
- **Suggested Cell Ontology terms:** cardiac muscle cell/cardiomyocyte; ventricular cardiac muscle cell; vascular smooth-muscle cell; cardiac fibroblast (downstream remodeling); endothelial cell.

### Conflicting/context-dependent findings

Complete or tissue-selective SUR2 loss is not uniformly harmful. Adult cardiomyocyte-specific deletion in mice increased glucose uptake, shifted metabolism toward glycolysis, and protected against ischemia–reperfusion injury. Global deletion also affects vascular KATP channels and can cause hypertension, coronary vasospasm, bradycardia, and sudden death, potentially producing chronic preconditioning. These findings show that developmental timing, cell type, stressor, isoform, and degree of channel dysfunction matter; they weaken any simplistic claim that all ABCC9 loss directly causes DCM. (aubert2019deletionofsulfonylurea pages 1-2)

No CMD1O-specific human myocardial transcriptomic, proteomic, metabolomic, lipidomic, methylomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omic study was found. Related KATP-deficient-heart proteomics cannot be treated as a CMD1O molecular signature.

---

## 7. Anatomical structures affected

- **Primary organ/system:** heart/cardiovascular system.
- **Primary chamber:** left ventricle; biventricular involvement is possible in DCM generally but was not characterized in the original cases.
- **Tissue:** myocardium/cardiac muscle tissue.
- **Primary cell:** ventricular cardiomyocyte.
- **Secondary structures:** atria, conduction system, and ventricular electrical substrate; lungs, liver, kidneys, and peripheral tissues can be affected secondarily through congestion or low output.
- **Subcellular localization:** cardiomyocyte sarcolemma, KATP-channel complex, cytosol-facing nucleotide-binding domains; downstream calcium-handling machinery and mitochondria are functionally implicated but not shown as primary ABCC9 lesion sites.
- **Suggested UBERON concepts:** heart (UBERON:0000948), myocardium, left ventricle (UBERON:0002084), cardiac muscle tissue, cardiac conduction system.
- **Lateralization:** not applicable; the disease is not unilateral, although left-ventricular involvement predominates.

---

## 8. Temporal development

The observed onset was insidious adult onset at 40–55 years. The course was chronic and progressive: severe dilation and systolic dysfunction were present at diagnosis, and two affected men died from HF within one to five years. There are insufficient data to define presymptomatic, early, intermediate, or genotype-specific progression rates. (bienengraeber2004abcc9mutationsidentified pages 2-2)

A practical staged model extrapolated from DCM is: genotype-positive/phenotype-negative; subtle ECG, strain, dilation, or scar abnormality; overt DCM/HFrEF; ventricular arrhythmia or decompensated HF; and end-stage HF. CMR and strain imaging may detect intermediate disease, while ECG and echocardiography remain central to serial screening. (sorella2025diagnosisandmanagement pages 2-3, gigli2025pathophysiologyofdilated pages 4-6)

Recovery is possible in DCM generally but is not documented for CMD1O. In a 2025 Japanese first-onset DCM cohort, 82/121 patients (68%) achieved LVEF ≥40% with ≥10-point improvement at a median 208 days; the rate was 89.5% in 2018–2022 versus 48.4% in 2007–2017. These treatment-era figures are not genotype-specific and should not be used as CMD1O penetrance or recovery estimates. (wanezaki2025recenttrendsin pages 1-2)

---

## 9. Inheritance and population

### Inheritance

The asserted CMD1O model is **autosomal dominant**, based mainly on heterozygous variants and father–daughter disease in one family. Penetrance is unknown and likely age- and stress-dependent if the association is genuine. Expressivity appears variable, but the sample is too small for inference. No anticipation, founder effect, consanguinity contribution, carrier frequency, or germline mosaicism has been established. (bienengraeber2004abcc9mutationsidentified pages 2-2, micolonghi2024unveilingthespectrum pages 25-26)

This is distinct from autosomal-recessive AIMS, in which affected individuals carry biallelic ABCC9 loss-of-function variants and heterozygous parents are generally unaffected. (efthymiou2024novellossoffunctionvariants pages 2-4, efthymiou2024novellossoffunctionvariants pages 8-9)

### Epidemiology

There is **no CMD1O-specific prevalence, incidence, sex ratio, geographic distribution, or ancestry estimate**. Two variants among 323 selected DCM cases must not be converted into population prevalence.

General contemporary DCM estimates provide context only. Recent analyses estimate prevalence around 1 in 220–250, although methodology produces values from approximately 59 to 280 per 100,000 and incidence around 3.6–7 per 100,000 person-years. (cheema2025trendsanddisparities pages 1-2, ramoslopez2026epidemiologyofnonischaemic pages 3-5)

A 2025 meta-analysis of 99 studies and 37,525 participants found a female proportion of 0.30 and male:female ratio of 2.38:1; genetically identified DCM remained male-predominant at 2.22:1. Sex-specific imaging reduced the apparent disparity, suggesting both biological penetrance differences and underdiagnosis in women. These data are general DCM, not ABCC9-specific. DOI [10.1161/CIRCULATIONAHA.124.070872](https://doi.org/10.1161/CIRCULATIONAHA.124.070872), February 2025. (bergan2025systematicreviewmetaanalysis pages 1-2)

---

## 10. Diagnostics

### Clinical diagnostic approach

1. **Confirm the phenotype:** history, examination, three-to-four-generation pedigree, 12-lead ECG, ambulatory rhythm monitoring, transthoracic echocardiography, and CMR.
2. **Measure severity/complications:** BNP or NT-proBNP, high-sensitivity troponin, renal function, electrolytes, liver profile, blood count, thyroid function, iron studies, and other phenotype-directed tests.
3. **Exclude mimics/secondary causes:** ischemic heart disease, hypertension/loading disease, valve or congenital disease, myocarditis, alcohol/toxins, tachycardia-mediated dysfunction, endocrine/metabolic disease, neuromuscular disease, and pregnancy-related disease.
4. **Characterize tissue:** CMR for volumes, function, edema and late gadolinium enhancement. Endomyocardial biopsy is reserved for selected cases in which noninvasive testing fails and a biopsy-defined diagnosis would alter treatment. (sorella2025diagnosisandmanagement pages 2-3)
5. **Assess arrhythmia:** ECG, Holter/patch monitoring, exercise testing when safe, and electrophysiology evaluation when indicated.

Current guideline synthesis identifies consensus for BNP/troponin, multimodality imaging, genetic counseling, and advanced-HF management. (sorella2025diagnosisandmanagement pages 1-2, sorella2025diagnosisandmanagement pages 2-3)

### Genetic testing

Use a phenotype-focused, evidence-curated cardiomyopathy/arrhythmia panel rather than ABCC9-only testing. Sequence and deletion/duplication analysis of high-evidence DCM genes should be prioritized. ABCC9 may be included as a Limited-evidence gene, but interpretation must be conservative. WES or WGS is reasonable after a negative panel when syndromic features, atypical inheritance, structural variation, or a strong family history remains unexplained. WGS may detect noncoding and structural variants, but clinical interpretation—not sequencing capacity—is the limiting step.

CMA, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion assays are not routine for isolated CMD1O; use them only when the phenotype suggests a chromosomal, mitochondrial, or repeat disorder. RNA sequencing can clarify suspected splice variants where relevant tissue or validated surrogate cells are available, but it is not an established CMD1O diagnostic.

A pathogenic/likely pathogenic familial variant should prompt counseling and targeted cascade testing. Genotype-positive relatives require longitudinal ECG and imaging; phenotype-negative relatives who test negative for a convincingly causal familial variant can generally be discharged from variant-specific surveillance. An **ABCC9 VUS must not drive cascade predictive testing**. (sorella2025diagnosisandmanagement pages 12-13, gigli2025pathophysiologyofdilated pages 4-6, micolonghi2024unveilingthespectrum pages 25-26)

### Differential diagnosis

Key alternatives include TTN-, LMNA-, FLNC-, DSP-, RBM20-, PLN-, BAG3-, SCN5A-, and sarcomeric DCM; arrhythmogenic cardiomyopathy; myocarditis; ischemic, alcoholic, chemotherapy-related, peripartum, tachycardia-induced, mitochondrial, and neuromuscular cardiomyopathies; cardiac sarcoidosis; hemochromatosis; and Fabry disease. Distinguishing evidence comes from pedigree, extracardiac findings, variant validity, coronary assessment, CMR scar distribution, inflammation, and targeted laboratory/biopsy findings.

---

## 11. Outcome and prognosis

CMD1O-specific survival curves do not exist. Two severe deaths—at 55 and 60 years—are subject to profound ascertainment bias and cannot establish life expectancy. Ventricular tachycardia, very low LVEF, advanced HF, and family history of sudden death are clinically adverse features. (bienengraeber2004abcc9mutationsidentified pages 2-2)

General DCM prognostic evidence includes:

- In 1,272 DCM patients with LVEF ≤35%, LGE ≥7.5% predicted SCD/aborted SCD with adjusted HR 4.11; combining LGE ≥7.5% with LVEF ≤20% gave a 7.12-fold risk and 4.8% annual event rate. (zhou2025prognosisandrisk pages 1-2)
- In the United States, 184,073 DCM-associated deaths occurred during 1999–2023; age-adjusted mortality fell from 5.19 to 2.34 per 100,000. In 2023 it was 3.4 in men and 1.38 in women. These are death-certificate data for all DCM, not CMD1O. (cheema2025trendsanddisparities pages 1-2)
- Reverse remodeling predicts a better course, but recovery is remission rather than proof of cure; continued surveillance is appropriate in genetic or arrhythmic disease.

Potential complications include progressive HFrEF, ventricular tachycardia/fibrillation, sudden cardiac death, atrial arrhythmia, functional mitral regurgitation, intracardiac thrombus and embolism, pulmonary hypertension, renal/hepatic dysfunction, hospitalization, LVAD, and transplantation.

---

## 12. Treatment

No treatment has been validated specifically for ABCC9-CMD1O. Management follows DCM/HFrEF and ventricular-arrhythmia guidelines.

### Pharmacotherapy

- **ARNI** (sacubitril/valsartan), or ACE inhibitor/ARB when ARNI is unsuitable.
- Evidence-based **beta-blocker**.
- **Mineralocorticoid-receptor antagonist**.
- **SGLT2 inhibitor**, regardless of diabetes status.
- **Loop diuretic** for congestion; add a thiazide-type agent selectively for resistant edema.
- Consider ivabradine, hydralazine/isosorbide dinitrate, digoxin, or vericiguat according to rhythm, blood pressure, renal function, symptoms, and guideline indications.

The four foundational classes should generally be introduced promptly at tolerated doses rather than waiting to maximize one before starting the next. In DAPA-HF and EMPEROR-Reduced, SGLT2 inhibitors reduced primary endpoints by 26% and 25%, respectively; these are HFrEF trial data, not CMD1O-specific results. (badger2023summaryandcomparison pages 9-11, badger2023summaryandcomparison pages 11-12)

Anticoagulation is not routine solely for DCM; use it for atrial fibrillation according to thromboembolic risk, documented LV thrombus, prior embolism, or another standard indication.

### Devices and advanced care

- **ICD:** secondary prevention after malignant ventricular arrhythmia/cardiac arrest; primary prevention after optimized therapy according to LVEF, symptoms, scar, genotype and individualized competing-risk assessment.
- **CRT:** strongest conventional indication is symptomatic HF, LVEF ≤35%, sinus rhythm, left-bundle-branch block, and QRS ≥150 ms; benefit is less certain with narrower QRS or non-LBBB morphology. (badger2023summaryandcomparison pages 11-12)
- **Catheter ablation:** for recurrent ventricular tachycardia when indicated.
- **LVAD/MCS and transplantation:** for advanced NYHA III–IV HF refractory to medical and device therapy. MCS may bridge to transplantation or serve as selected destination therapy. (sorella2025diagnosisandmanagement pages 12-13)

### Targeted and experimental therapy

KATP openers or inhibitors are **not established CMD1O therapy**. Available modulators can affect pancreatic, vascular, skeletal-muscle, and cardiac channel combinations differently; the context-dependent mouse results make empiric channel manipulation unsafe outside research. Preclinical glibenclamide work largely concerns gain-of-function Cantú syndrome, not CMD1O. No ABCC9-directed gene therapy, ASO, RNA therapy, CRISPR treatment, or CMD1O-specific interventional trial was identified in the ClinicalTrials.gov search. (aubert2019deletionofsulfonylurea pages 1-2, nichols2023personalizedtherapeuticsfor pages 4-6)

Suggested NCIt intervention mappings include angiotensin-receptor neprilysin inhibitor therapy, beta-adrenergic blocking-agent therapy, mineralocorticoid-receptor antagonist therapy, SGLT2-inhibitor therapy, diuretic therapy, implantable cardioverter-defibrillator placement, cardiac-resynchronization therapy, ventricular-assist-device placement, catheter ablation, and heart transplantation.

---

## 13. Prevention

### Primary prevention

The genetic lesion itself cannot currently be prevented after conception. At-risk families should receive genetic counseling, but reproductive decisions require explicit discussion that the ABCC9–DCM relationship is Limited. Where a familial variant is independently classified as pathogenic/likely pathogenic with persuasive segregation, prenatal diagnosis or preimplantation genetic testing may be technically possible; it should not be offered for a VUS as though disease were certain.

Reduce modifiable myocardial stress: control hypertension and diabetes, avoid smoking and illicit stimulants, avoid heavy alcohol, review cardiotoxic drugs, maintain healthy weight, and use individualized exercise advice. Influenza, COVID-19, and pneumococcal vaccination are appropriate according to national HF guidance; no vaccine prevents CMD1O itself.

### Secondary prevention

- Clinical screening of first-degree relatives with history, ECG and echocardiography; add CMR and rhythm monitoring when indicated.
- Targeted cascade testing only for a convincingly pathogenic familial variant.
- Repeat surveillance for genotype-positive/phenotype-negative relatives because penetrance may be age dependent. (sorella2025diagnosisandmanagement pages 12-13, gigli2025pathophysiologyofdilated pages 4-6)

### Tertiary prevention

Optimize foundational HFrEF therapy, treat congestion, monitor electrolytes/renal function, manage arrhythmias, consider ICD/CRT, provide cardiac rehabilitation, and refer early for advanced-HF assessment. Regular moderate activity is encouraged in stable HF, whereas high-intensity competitive exercise requires individualized arrhythmic-risk assessment. (badger2023summaryandcomparison pages 9-11)

---

## 14. Other species and natural disease

No naturally occurring, breed-defined veterinary equivalent of human CMD1O was identified. Accordingly, no VBO breed term, animal prevalence, zoonotic potential, or cross-species transmission applies. CMD1O is noninfectious and not zoonotic.

Relevant orthologues include mouse **Abcc9** (*Mus musculus*, NCBI Taxonomy 10090) and zebrafish **abcc9** (*Danio rerio*, Taxonomy 7955). Conservation of SUR2-containing KATP channels supports comparative study, but experimentally engineered disease is not evidence of naturally occurring veterinary CMD1O.

---

## 15. Model organisms

### Mouse

- SUR2/Abcc9 loss models show fatigability and cardiac dysfunction, supporting a role in muscle and myocardial physiology. Global models are complicated by vascular dysfunction, hypertension, coronary vasospasm, bradycardia, and sudden death. (smeland2019abcc9relatedintellectualdisability pages 1-2)
- Related **Kcnj11/Kir6.2-null** mice are informative for channel-complex failure: baseline findings may be mild, whereas exercise or hypertension produces calcium overload, arrhythmia, calcineurin-dependent remodeling, HF, and death. This is pathway-level, not variant-specific, evidence. (kane2006kcnj11geneknockout pages 1-2)
- Adult cardiomyocyte-specific SUR2 deletion can instead enhance glucose uptake and protect against ischemia–reperfusion injury, demonstrating model and stress dependence. (aubert2019deletionofsulfonylurea pages 1-2)

### Zebrafish

Abcc9 loss causes reduced activity, ventricular enlargement, and cardiac dysfunction; zebrafish cardiomyocytes and vascular smooth muscle possess broadly comparable KATP-channel composition and metabolic sensitivity. However, fish channels respond differently to some openers such as pinacidil and minoxidil, limiting pharmacologic translation. (smeland2019abcc9relatedintellectualdisability pages 1-2)

### Cellular systems

HEK293/recombinant-channel assays co-expressing SUR2A variants with Kir6.2 demonstrated abnormal gating or complete loss of current for severe loss-of-function alleles. Such systems provide strong molecular-function evidence but lack myocardial architecture, neurohormonal signaling, developmental context, vascular effects, and chronic loading.

No published patient-specific iPSC-cardiomyocyte, engineered-heart-tissue, cardiac-organoid, or knock-in model of p.Ala1513Thr/Fs1524 was identified. Such models, combined with isogenic correction and mechanical/metabolic stress, would be especially valuable for resolving the Limited gene–disease validity.

---

## Evidence-based knowledge-base conclusion

CMD1O should be entered with **MONDO:0012062**, OMIM **608569**, and candidate causal gene **ABCC9**, but with a prominent **Limited clinical-validity flag**. The best-supported phenotype is severe adult-onset DCM with ventricular tachycardia; the best-supported mechanism is disruption of SUR2A-dependent KATP metabolic gating. Yet the human evidence consists essentially of two historical index variants, limited segregation, and no disease-specific natural-history cohort. Current diagnosis and treatment should therefore be phenotype driven, should investigate stronger DCM genes and acquired causes, and should not treat an ABCC9 VUS as diagnostic. Recent AIMS studies strengthen the biological importance of ABCC9 loss but establish a distinct recessive multisystem disorder rather than independently proving dominant CMD1O. (efthymiou2024novellossoffunctionvariants pages 2-4, micolonghi2024unveilingthespectrum pages 25-26, micolonghi2024unveilingthespectrum pages 8-9)

### Key dated sources

1. Bienengraeber M, et al. “ABCC9 mutations identified in human dilated cardiomyopathy disrupt catalytic KATP channel gating.” *Nature Genetics*. Online 21 March 2004; issue April 2004. PMID **15034580**. [https://doi.org/10.1038/ng1329](https://doi.org/10.1038/ng1329). (bienengraeber2004abcc9mutationsidentified pages 2-2)
2. Olson TM, Terzic A. “Human KATP channelopathies: diseases of metabolic homeostasis.” *Pflügers Archiv*. 2010. [https://doi.org/10.1007/s00424-009-0771-y](https://doi.org/10.1007/s00424-009-0771-y). (olson2010humankatpchannelopathies pages 5-6)
3. Jordan E, et al. “Evidence-Based Assessment of Genes in Dilated Cardiomyopathy.” *Circulation*. 2021;144:7–19. PMID **33947203**. [https://doi.org/10.1161/CIRCULATIONAHA.120.053033](https://doi.org/10.1161/CIRCULATIONAHA.120.053033). This expert curation supports caution with low-evidence DCM genes.
4. Efthymiou S, et al. “Novel loss-of-function variants expand ABCC9-related intellectual disability and myopathy syndrome.” *Brain*. Published January 2024;147:1822–1836. [https://doi.org/10.1093/brain/awae010](https://doi.org/10.1093/brain/awae010). (efthymiou2024novellossoffunctionvariants pages 2-4)
5. Micolonghi C, et al. “Unveiling the Spectrum of Minor Genes in Cardiomyopathies.” *International Journal of Molecular Sciences*. 11 September 2024. [https://doi.org/10.3390/ijms25189787](https://doi.org/10.3390/ijms25189787). Reports ABCC9–DCM as ClinGen Limited. (micolonghi2024unveilingthespectrum pages 25-26)
6. Sorella A, et al. “Diagnosis and management of dilated cardiomyopathy.” Accepted 13 December and online 14 December 2024; *European Heart Journal—Quality of Care & Clinical Outcomes* 2025. [https://doi.org/10.1093/ehjqcco/qcae109](https://doi.org/10.1093/ehjqcco/qcae109). (sorella2025diagnosisandmanagement pages 1-2, sorella2025diagnosisandmanagement pages 2-3)
7. Li Y, et al. Nonischemic DCM and diabetes prospective cohort. *Cardiovascular Diabetology*. February 2024. [https://doi.org/10.1186/s12933-024-02134-0](https://doi.org/10.1186/s12933-024-02134-0). (li2024theimpactof pages 1-2)
8. Bergan N, et al. DCM sex-ratio meta-analysis. *Circulation*. February 2025. [https://doi.org/10.1161/CIRCULATIONAHA.124.070872](https://doi.org/10.1161/CIRCULATIONAHA.124.070872). (bergan2025systematicreviewmetaanalysis pages 1-2)

References

1. (bienengraeber2004abcc9mutationsidentified pages 2-2): Martin Bienengraeber, Timothy M Olson, Vitaliy A Selivanov, Eva C Kathmann, Fearghas O'Cochlain, Fan Gao, Amy B Karger, Jeffrey D Ballew, Denice M Hodgson, Leonid V Zingman, Yuan-Ping Pang, Alexey E Alekseev, and Andre Terzic. Abcc9 mutations identified in human dilated cardiomyopathy disrupt catalytic katp channel gating. Nature Genetics, 36:382-387, Apr 2004. URL: https://doi.org/10.1038/ng1329, doi:10.1038/ng1329. This article has 506 citations and is from a highest quality peer-reviewed journal.

2. (micolonghi2024unveilingthespectrum pages 25-26): Caterina Micolonghi, Federica Perrone, Marco Fabiani, Silvia Caroselli, Camilla Savio, Antonio Pizzuti, Aldo Germani, Vincenzo Visco, Simona Petrucci, Speranza Rubattu, and Maria Piane. Unveiling the spectrum of minor genes in cardiomyopathies: a narrative review. Sep 2024. URL: https://doi.org/10.3390/ijms25189787, doi:10.3390/ijms25189787. This article has 11 citations.

3. (micolonghi2024unveilingthespectrum pages 8-9): Caterina Micolonghi, Federica Perrone, Marco Fabiani, Silvia Caroselli, Camilla Savio, Antonio Pizzuti, Aldo Germani, Vincenzo Visco, Simona Petrucci, Speranza Rubattu, and Maria Piane. Unveiling the spectrum of minor genes in cardiomyopathies: a narrative review. Sep 2024. URL: https://doi.org/10.3390/ijms25189787, doi:10.3390/ijms25189787. This article has 11 citations.

4. (bienengraeber2004abcc9mutationsidentified pages 1-2): Martin Bienengraeber, Timothy M Olson, Vitaliy A Selivanov, Eva C Kathmann, Fearghas O'Cochlain, Fan Gao, Amy B Karger, Jeffrey D Ballew, Denice M Hodgson, Leonid V Zingman, Yuan-Ping Pang, Alexey E Alekseev, and Andre Terzic. Abcc9 mutations identified in human dilated cardiomyopathy disrupt catalytic katp channel gating. Nature Genetics, 36:382-387, Apr 2004. URL: https://doi.org/10.1038/ng1329, doi:10.1038/ng1329. This article has 506 citations and is from a highest quality peer-reviewed journal.

5. (OpenTargets Search: Dilated cardiomyopathy 1O): Open Targets Query (Dilated cardiomyopathy 1O, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (olson2010humankatpchannelopathies pages 5-6): Timothy M. Olson and Andre Terzic. Human katp channelopathies: diseases of metabolic homeostasis. Pflugers Archiv, 460:295-306, Dec 2010. URL: https://doi.org/10.1007/s00424-009-0771-y, doi:10.1007/s00424-009-0771-y. This article has 155 citations.

7. (kane2006kcnj11geneknockout pages 1-2): Garvan C. Kane, Atta Behfar, Roy B. Dyer, D. Fearghas O'Cochlain, Xiao-Ke Liu, Denice M. Hodgson, Santiago Reyes, Takashi Miki, Susumu Seino, and Andre Terzic. Kcnj11 gene knockout of the kir6.2 katp channel causes maladaptive remodeling and heart failure in hypertension. Human molecular genetics, 15 15:2285-97, Aug 2006. URL: https://doi.org/10.1093/hmg/ddl154, doi:10.1093/hmg/ddl154. This article has 134 citations and is from a domain leading peer-reviewed journal.

8. (smeland2019abcc9relatedintellectualdisability pages 1-2): Marie F. Smeland, Conor McClenaghan, Helen I. Roessler, Sanne Savelberg, Geir Åsmund Myge Hansen, Helene Hjellnes, Kjell Arne Arntzen, Kai Ivar Müller, Andreas Rosenberger Dybesland, Theresa Harter, Monica Sala-Rabanal, Chris H. Emfinger, Yan Huang, Soma S. Singareddy, Jamie Gunn, David F. Wozniak, Attila Kovacs, Maarten Massink, Federico Tessadori, Sarah M. Kamel, Jeroen Bakkers, Maria S. Remedi, Marijke Van Ghelue, Colin G. Nichols, and Gijs van Haaften. Abcc9-related intellectual disability myopathy syndrome is a katp channelopathy with loss-of-function mutations in abcc9. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12428-7, doi:10.1038/s41467-019-12428-7. This article has 56 citations and is from a highest quality peer-reviewed journal.

9. (kane2005cardiackatpchannels pages 10-10): G. Kane, Xiao‐Ke Liu, S. Yamada, T. Olson, and A. Terzic. Cardiac katp channels in health and disease. Journal of molecular and cellular cardiology, 38 6:937-43, Jun 2005. URL: https://doi.org/10.1016/j.yjmcc.2005.02.026, doi:10.1016/j.yjmcc.2005.02.026. This article has 260 citations and is from a domain leading peer-reviewed journal.

10. (aubert2019deletionofsulfonylurea pages 1-2): Gregory Aubert, David Y. Barefield, Alexis R. Demonbreun, Mohun Ramratnam, Katherine S. Fallon, James L. Warner, Ann E. Rossi, Michele Hadhazy, Jonathan C. Makielski, and Elizabeth M. McNally. Deletion of sulfonylurea receptor 2 in the adult myocardium enhances cardiac glucose uptake and is cardioprotective. JACC: Basic to Translational Science, 4:251-268, Apr 2019. URL: https://doi.org/10.1016/j.jacbts.2018.11.012, doi:10.1016/j.jacbts.2018.11.012. This article has 11 citations.

11. (sorella2025diagnosisandmanagement pages 2-3): Anna Sorella, Kristian Galanti, Lorena Iezzi, Sabina Gallina, Selma F Mohammed, Neha Sekhri, Mohammed Majid Akhtar, Sanjay K Prasad, Choudhary Anwar Ahmed Chahal, Fabrizio Ricci, and Mohammed Yunus Khanji. Diagnosis and management of dilated cardiomyopathy: a systematic review of clinical practice guidelines and recommendations. European Heart Journal. Quality of Care & Clinical Outcomes, 11:206-222, Dec 2025. URL: https://doi.org/10.1093/ehjqcco/qcae109, doi:10.1093/ehjqcco/qcae109. This article has 45 citations.

12. (sorella2025diagnosisandmanagement pages 12-13): Anna Sorella, Kristian Galanti, Lorena Iezzi, Sabina Gallina, Selma F Mohammed, Neha Sekhri, Mohammed Majid Akhtar, Sanjay K Prasad, Choudhary Anwar Ahmed Chahal, Fabrizio Ricci, and Mohammed Yunus Khanji. Diagnosis and management of dilated cardiomyopathy: a systematic review of clinical practice guidelines and recommendations. European Heart Journal. Quality of Care & Clinical Outcomes, 11:206-222, Dec 2025. URL: https://doi.org/10.1093/ehjqcco/qcae109, doi:10.1093/ehjqcco/qcae109. This article has 45 citations.

13. (badger2023summaryandcomparison pages 9-11): Sarah Badger, James McVeigh, and Praveen Indraratna. Summary and comparison of the 2022 acc/aha/hfsa and 2021 esc heart failure guidelines. Cardiology and Therapy, 12:571-588, Aug 2023. URL: https://doi.org/10.1007/s40119-023-00328-3, doi:10.1007/s40119-023-00328-3. This article has 12 citations and is from a peer-reviewed journal.

14. (badger2023summaryandcomparison pages 11-12): Sarah Badger, James McVeigh, and Praveen Indraratna. Summary and comparison of the 2022 acc/aha/hfsa and 2021 esc heart failure guidelines. Cardiology and Therapy, 12:571-588, Aug 2023. URL: https://doi.org/10.1007/s40119-023-00328-3, doi:10.1007/s40119-023-00328-3. This article has 12 citations and is from a peer-reviewed journal.

15. (nichols2023personalizedtherapeuticsfor pages 4-6): Colin G. Nichols. Personalized therapeutics for k<sub>atp</sub>-dependent pathologies. Jan 2023. URL: https://doi.org/10.1146/annurev-pharmtox-051921-123023, doi:10.1146/annurev-pharmtox-051921-123023. This article has 31 citations and is from a highest quality peer-reviewed journal.

16. (sorella2025diagnosisandmanagement pages 1-2): Anna Sorella, Kristian Galanti, Lorena Iezzi, Sabina Gallina, Selma F Mohammed, Neha Sekhri, Mohammed Majid Akhtar, Sanjay K Prasad, Choudhary Anwar Ahmed Chahal, Fabrizio Ricci, and Mohammed Yunus Khanji. Diagnosis and management of dilated cardiomyopathy: a systematic review of clinical practice guidelines and recommendations. European Heart Journal. Quality of Care & Clinical Outcomes, 11:206-222, Dec 2025. URL: https://doi.org/10.1093/ehjqcco/qcae109, doi:10.1093/ehjqcco/qcae109. This article has 45 citations.

17. (li2024theimpactof pages 1-2): Yangjie Li, Hong Xian, Yuanwei Xu, Weihao Li, Jiajun Guo, Ke Wan, Jie Wang, Ziqian Xu, Qing Zhang, Yuchi Han, Jiayu Sun, and Yucheng Chen. The impact of type 2 diabetes mellitus on the clinical profile, myocardial fibrosis, and prognosis in non-ischemic dilated cardiomyopathy: a prospective cohort study. Cardiovascular Diabetology, Feb 2024. URL: https://doi.org/10.1186/s12933-024-02134-0, doi:10.1186/s12933-024-02134-0. This article has 16 citations and is from a peer-reviewed journal.

18. (efthymiou2024novellossoffunctionvariants pages 2-4): Stephanie Efthymiou, Marcello Scala, Vini Nagaraj, Katarzyna Ochenkowska, Fenne L Komdeur, Robin A Liang, Mohamed S Abdel-Hamid, Tipu Sultan, Tuva Barøy, Marijke Van Ghelue, Barbara Vona, Reza Maroofian, Faisal Zafar, Fowzan S Alkuraya, Maha S Zaki, Mariasavina Severino, Kingsley C Duru, Robert C Tryon, Lin Vigdis Brauteset, Morad Ansari, Mark Hamilton, Mieke M van Haelst, Gijs van Haaften, Federico Zara, Henry Houlden, Éric Samarut, Colin G Nichols, Marie F Smeland, and Conor McClenaghan. Novel loss-of-function variants expand abcc9-related intellectual disability and myopathy syndrome. Brain, 147:1822-1836, Jan 2024. URL: https://doi.org/10.1093/brain/awae010, doi:10.1093/brain/awae010. This article has 18 citations and is from a highest quality peer-reviewed journal.

19. (efthymiou2024novellossoffunctionvariants pages 8-9): Stephanie Efthymiou, Marcello Scala, Vini Nagaraj, Katarzyna Ochenkowska, Fenne L Komdeur, Robin A Liang, Mohamed S Abdel-Hamid, Tipu Sultan, Tuva Barøy, Marijke Van Ghelue, Barbara Vona, Reza Maroofian, Faisal Zafar, Fowzan S Alkuraya, Maha S Zaki, Mariasavina Severino, Kingsley C Duru, Robert C Tryon, Lin Vigdis Brauteset, Morad Ansari, Mark Hamilton, Mieke M van Haelst, Gijs van Haaften, Federico Zara, Henry Houlden, Éric Samarut, Colin G Nichols, Marie F Smeland, and Conor McClenaghan. Novel loss-of-function variants expand abcc9-related intellectual disability and myopathy syndrome. Brain, 147:1822-1836, Jan 2024. URL: https://doi.org/10.1093/brain/awae010, doi:10.1093/brain/awae010. This article has 18 citations and is from a highest quality peer-reviewed journal.

20. (gigli2025pathophysiologyofdilated pages 4-6): Marta Gigli, Davide Stolfo, Marco Merlo, Gianfranco Sinagra, Matthew R. G. Taylor, and Luisa Mestroni. Pathophysiology of dilated cardiomyopathy: from mechanisms to precision medicine. Nature reviews. Cardiology, 22:183-198, Oct 2025. URL: https://doi.org/10.1038/s41569-024-01074-2, doi:10.1038/s41569-024-01074-2. This article has 98 citations.

21. (wanezaki2025recenttrendsin pages 1-2): Masahiro Wanezaki, Tetsu Watanabe, Atsushi Iizuka, Tomoki Kobayashi, Shunsuke Edamura, Takayuki Sugai, Harutoshi Tamura, Satoshi Nishiyama, Ryuhei Yamaguchi, Naoaki Hashimoto, Yoichiro Otaki, Daisuke Kutsuzawa, Shigehiko Kato, Takanori Arimoto, Shunsuke Inoue, Toshiyuki Ko, Seitaro Nomura, Issei Komuro, and Masafumi Watanabe. Recent trends in achievement rates and time required for left ventricular reverse remodeling in dilated cardiomyopathy. Feb 2025. URL: https://doi.org/10.1253/circrep.cr-24-0148, doi:10.1253/circrep.cr-24-0148. This article has 0 citations and is from a peer-reviewed journal.

22. (cheema2025trendsanddisparities pages 1-2): Zian Zafar Cheema, Mohammad Atout, Taha Kassim Dohadwala, Ahmed Talaat Deiab, Aya Abouayana, Hazim Mesmar, Asmaa Hasan, Amaad Alam Shah, Muhammad Babar Mahmood, Daniel James Lewis, Hasan Ahmed, Maryam Shahzad, Mushood Ahmed, Nabeel Ahmed, Raheel Ahmed, and Syed Khurram M. Gardezi. Trends and disparities in dilated cardiomyopathy related mortality among adults in the united states: a cdc wonder analysis (1999–2023). PLOS One, 20(10):e0333525, Oct 2025. URL: https://doi.org/10.1371/journal.pone.0333525, doi:10.1371/journal.pone.0333525. This article has 3 citations and is from a peer-reviewed journal.

23. (ramoslopez2026epidemiologyofnonischaemic pages 3-5): Noemí Ramos-López, Fernando Domínguez, Juan Pablo Ochoa, Enrique Lara-Pezzi, and Pablo Garcia-Pavia. Epidemiology of non-ischaemic dilated cardiomyopathy. Nature Reviews Cardiology, May 2026. URL: https://doi.org/10.1038/s41569-026-01300-z, doi:10.1038/s41569-026-01300-z. This article has 0 citations and is from a domain leading peer-reviewed journal.

24. (bergan2025systematicreviewmetaanalysis pages 1-2): Natalie Bergan, Ishika Prachee, Lara Curran, Kathryn A. McGurk, Chang Lu, Antonio de Marvao, Wenjia Bai, Brian P. Halliday, John Gregson, Declan P. O’Regan, James S. Ware, and Upasana Tayal. Systematic review, meta-analysis, and population study to determine the biologic sex ratio in dilated cardiomyopathy. Feb 2025. URL: https://doi.org/10.1161/circulationaha.124.070872, doi:10.1161/circulationaha.124.070872. This article has 21 citations and is from a highest quality peer-reviewed journal.

25. (zhou2025prognosisandrisk pages 1-2): Di Zhou, Leyi Zhu, Shuang Li, Weichun Wu, Baiyan Zhuang, Jing Xu, Wenjing Yang, Jian He, Yining Wang, Yuhui Zhang, Guanshu Liu, Xiaoxin Sun, Qiang Zhang, Zhongzhao Teng, Arlene Sirajuddin, Andrew E. Arai, Shihua Zhao, and Minjie Lu. Prognosis and risk stratification in dilated cardiomyopathy with lvef≤35%: cardiac mri insights for better outcomes. Circulation. Cardiovascular Imaging, 18:e017246-e017246, Mar 2025. URL: https://doi.org/10.1161/circimaging.124.017246, doi:10.1161/circimaging.124.017246. This article has 9 citations.

## Artifacts

- [Edison artifact artifact-00](Dilated_Cardiomyopathy_1O-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0000948` (1 mention) - the report calls it "Suggested UBERON concepts:** heart"; UBERON calls it **heart**