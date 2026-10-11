---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-09T15:31:31.573208'
end_time: '2026-10-09T15:53:10.400855'
duration_seconds: 1298.83
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hardikar Syndrome
  mondo_id: MONDO:0012997
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 15
  verified: 15
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0012997
    reported_labels:
    - if available
    ontology_label: cholestasis-pigmentary retinopathy-cleft palate syndrome
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hardikar_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hardikar Syndrome
- **MONDO ID:** MONDO:0012997 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hardikar Syndrome** covering all of the
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
- **Disease Name:** Hardikar Syndrome
- **MONDO ID:** MONDO:0012997 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hardikar Syndrome** covering all of the
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


# Hardikar syndrome: disease-characteristics research report

**Scope and evidence standard.** Hardikar syndrome is exceptionally rare. Most disease-specific knowledge comes from individual clinical reports and a small molecularly characterized series, not population registries or electronic-health-record cohorts. The principal molecular study is Li and colleagues, published online in 2020 and in *Genetics in Medicine* in April 2021, PMID **33244166**. A 2026 case report and literature review provides a more recent synthesis but includes a patient whose variant remains of uncertain significance. The 2024 article by Strong and colleagues, *“Novel insights into the phenotypic spectrum and pathogenesis of Hardikar syndrome”* ([DOI:10.1016/j.gim.2024.101222](https://doi.org/10.1016/j.gim.2024.101222)), was identified bibliographically but its primary text could not be examined here; no experimental results are attributed to it below. (li2021denovolossoffunction pages 1-2, kahy2026anovelintronic pages 2-5, kahy2026anovelintronic pages 1-2)

## 1. Disease information

Hardikar syndrome is a congenital, multisystem Mendelian disorder classically combining orofacial clefting, pigmentary retinal abnormalities, hepatobiliary disease, intestinal malrotation, and urinary-tract anomalies. Neurodevelopment is often relatively preserved, although that characterization should not be extended uncritically to every person with a **MED12** variant. The identifying disease record is **MONDO:0012997**, indexed by Open Targets as **“cholestasis-pigmentary retinopathy-cleft palate syndrome”**; **MIM 301068** denotes Hardikar syndrome, while **MIM 300188** denotes its causal gene, **MED12**. Useful alternative names are *Hardikar syndrome*, *MED12-related Hardikar syndrome*, and *cholestasis–pigmentary retinopathy–cleft palate syndrome*. The disease-specific Orphanet, MeSH, and ICD-10/ICD-11 codes could not be verified from the available sources; they should not be inferred from broader cholestasis codes. (OpenTargets Search: Hardikar syndrome, poley2008hardikarsyndromenew pages 1-3, kahy2026anovelintronic pages 1-2)

The evidence is **patient-derived**, subsequently summarized at disease level. For context, a 2026 review assembled **33 individuals from 12 reports**, added one DECIPHER record and its own case, and analyzed **35 individuals**; its two original, molecularly unconfirmed historical cases were excluded. These are literature-ascertained observations, not 35 independent prospective observations or a prevalence denominator. The review’s newly reported **MED12 c.3868-5C>G** case is clinically suggestive but **not a genetically established Hardikar case**, because the variant is a VUS. (kahy2026anovelintronic pages 2-5, kahy2026anovelintronic pages 1-2, kahy2026anovelintronic pages 16-18)

## 2. Etiology: causal, risk, protective, and environmental factors

The strongest disease-specific cause is a **heterozygous, usually de novo, germline loss-of-function variant in X-linked MED12** in an affected female. The seven women investigated by Li and colleagues had nonsense or frameshift variants; exceptional mosaicism occurs. An X-linked dominant model with predominantly female recognition is supported, but whether all severe male loss-of-function genotypes are embryonically lethal is an inference, not an established penetrance measurement. **MED12 missense variants can cause different MED12-related disorders**—including FG, Lujan–Fryns, and Ohdo syndromes—and must not automatically be classified as Hardikar syndrome. (li2021denovolossoffunction pages 1-2, li2021denovolossoffunction pages 4-5, plassche2021med12related(neuro)developmentaldisorders pages 1-3, plassche2021med12related(neuro)developmentaldisorders pages 3-5)

No disease-specific environmental, infectious, dietary, lifestyle, occupational, or age-related initiating risk factor has been established. No protective allele, modifier gene, preventive exposure, or demonstrated gene–environment interaction has been established. Skewed X-chromosome inactivation is a plausible **endogenous modifier of expression**, but measurements in blood cannot establish inactivation patterns in liver or brain. **KDM6A** and **KMT2D** arise in a proposed transcriptional-network comparison with Kabuki syndrome; they are **not validated Hardikar causal or modifier genes**. (li2021denovolossoffunction pages 6-7, plassche2021med12related(neuro)developmentaldisorders pages 3-5)

## 3. Phenotypes and effects on functioning

The congenital structural phenotype is heterogeneous. Clefts can affect feeding and speech; intestinal malrotation can cause neonatal obstruction; urinary malformations can entail operations and recurrent infection. Cholestatic disease can produce jaundice, itching, nutritional impairment, growth failure, fibrosis, and occasionally hepatic failure. Retinal pigmentation need not imply early loss of vision: one reported child retained unaffected vision at age four. Bilateral sensorineural hearing loss requiring cochlear implants was reported in another child. Aortic coarctation or dilation and carotid/cerebral vascular abnormalities warrant attention; they are not present in every case. These statements describe observed cases, **not established per-phenotype percentages**. No syndrome-specific EQ-5D, SF-36, or PROMIS estimates were identified. (li2021denovolossoffunction pages 4-5, li2021denovolossoffunction pages 6-7, li2021denovolossoffunction pages 3-4, poley2008hardikarsyndromenew pages 1-3)

The following table gives phenotype-level **HPO suggestions whose identifiers were explicitly reported in the retrieved clinical review**. Onset and progression refer to observed cases, not a validated natural-history staging system. (kahy2026anovelintronic pages 5-6, kahy2026anovelintronic pages 2-5)

| Observed phenotype | Evidence-informed onset/course and impact | Verified HPO ID | Frequency |
|---|---|---|---|
| Cleft lip and/or palate | Congenital, generally stable structural anomaly; may impair feeding, speech, hearing, and facial development and require staged surgical repair. (poley2008hardikarsyndromenew pages 1-3, li2021denovolossoffunction pages 3-4) | Cleft lip — HP:0410030; cleft palate — HP:0000175 | Not reliably established; published cases only; characteristic but not universal. |
| Pigmentary retinopathy | Congenital or recognized in childhood; may remain stable with preserved vision, but longitudinal ophthalmic surveillance is warranted. (li2021denovolossoffunction pages 4-5, kahy2026anovelintronic pages 5-6) | HP:0000580 | Not reliably established; published cases only; characteristic but not universal. |
| Cholestasis | Usually neonatal or infantile; severity ranges from persistent biochemical disease to progressive jaundice, pruritus, malnutrition, portal hypertension, and liver failure. (poley2008hardikarsyndromenew pages 1-3, kahy2026anovelintronic pages 15-16) | HP:0001396 | Not reliably established; published cases only; recurrent core manifestation. |
| Biliary atresia | Congenital hepatobiliary malformation presenting in infancy; may cause severe obstructive liver disease and require surgical or transplant evaluation. (li2021denovolossoffunction pages 3-4, kahy2026anovelintronic pages 5-6) | HP:0005912 | Not reliably established; published cases only; not universal. |
| Absent gallbladder | Congenital imaging or operative finding; may accompany severe biliary maldevelopment and cholestasis. The 2026 example carried a MED12 VUS and is supportive, not genetically definitive. (li2021denovolossoffunction pages 4-5, kahy2026anovelintronic pages 15-16) | HP:0011467 | Not reliably established; published cases only; rare reported phenotype. |
| Intestinal malrotation | Congenital; may cause neonatal intestinal obstruction and require a Ladd procedure, with substantial acute surgical morbidity. (poley2008hardikarsyndromenew pages 1-3) | HP:0002566 | Not reliably established; published cases only; characteristic but not universal. |
| Choledochal cyst | Congenital biliary anomaly; may coexist with progressive cholestasis and cirrhosis and has been identified during liver transplantation. (poley2008hardikarsyndromenew pages 3-4, poley2008hardikarsyndromenew pages 1-3) | HP:0100890 | Not reliably established; published cases only; rare reported phenotype. |
| Hepatic fibrosis | Begins in infancy in severe cases and may progress to bridging fibrosis or cirrhosis, impairing growth and liver function. (poley2008hardikarsyndromenew pages 1-3, kahy2026anovelintronic pages 15-16) | HP:0001395 | Not reliably established; published cases only; severity is variable. |
| Hepatic failure | Advanced outcome of progressive hepatobiliary disease; may necessitate liver transplantation and can be fatal without timely treatment. The 2026 VUS case must not be counted as molecularly confirmed. (poley2008hardikarsyndromenew pages 1-3, kahy2026anovelintronic pages 15-16) | HP:0001399 | Not reliably established; published cases only; severe but not universal. |
| Hydronephrosis | Congenital urinary-tract manifestation; may reflect obstruction or ectopic/abnormal ureters and predispose to recurrent infection and renal procedures. (poley2008hardikarsyndromenew pages 3-4, kahy2026anovelintronic pages 5-6) | HP:0000126 | Not reliably established; published cases only; not universal. |
| Vesicoureteral reflux | Congenital urinary dysfunction; increases urinary-tract infection risk and may require urologic surveillance or intervention. (li2021denovolossoffunction pages 6-7, kahy2026anovelintronic pages 5-6) | HP:0000076 | Not reliably established; published cases only; not universal. |
| Hearing impairment | Congenital or childhood-onset, including severe bilateral sensorineural loss; may delay speech and require cochlear implantation. (li2021denovolossoffunction pages 3-4, kahy2026anovelintronic pages 5-6) | HP:0000365 | Not reliably established; published cases only; rare reported phenotype. |
| Congenital diaphragmatic hernia | Prenatal or neonatal structural anomaly with potential respiratory compromise; represents an expanded phenotype rather than a defining feature. (kahy2026anovelintronic pages 1-2, kahy2026anovelintronic pages 5-6) | HP:0000776 | Not reliably established; published cases only; rare and not universal. |


*Table: Compact phenotype annotations for Hardikar syndrome using HPO identifiers explicitly reported in the case-review literature. Frequencies remain unquantified because evidence comes from small, ascertainment-biased published cases; the 2026 MED12 VUS case is not treated as genetically confirmed.*

Additional reported signs include preauricular pits/tags, ptosis, malformed external ears, failure to thrive, patent ductus arteriosus, ventricular septal defect, ectopic ureters, imperforate anus, vaginal atresia, and, in later phenotype summaries, diaphragmatic or pulmonary anomalies. Some affected individuals have normal cognition, but developmental impairment occurs across the wider **MED12-related** spectrum; disease attribution requires careful clinical and variant review. (li2021denovolossoffunction pages 6-7, li2021denovolossoffunction pages 3-4, poley2008hardikarsyndromenew pages 3-4, plassche2021med12related(neuro)developmentaldisorders pages 3-5, kahy2026anovelintronic pages 1-2)

## 4. Genetic and molecular information

**Gene:** **MED12**, mediator complex subunit 12, at **Xq13.1**; Open Targets lists Ensembl **ENSG00000184634**. The MED12 HGNC numeric identifier and an NCBI Gene identifier were not independently checked and are deliberately not assigned here. The 2021 clinically ascertained series reported the following seven variant descriptions, in its study numbering: **c.322C>T, p.(Arg108\*)**; **c.2207_2210del, p.(Thr736Ilefs\*43)**; **c.2663dup, p.(Leu889Profs\*11)**; **c.4903_4906delinsCCAGCA, p.(Val1635Profs\*61)**; **c.5111G>A, p.(Trp1704\*)**; **c.5622C>A, p.(Tyr1874\*)**; and **c.6169C>T, p.(Gln2057\*)**. These were described as pathogenic loss-of-function changes, predominantly de novo, with predicted nonsense-mediated decay; one early-stop finding was suspected to be mosaic in leukocytes. These are **patient germline/developmental variants, not tumor-somatic driver claims**. Exact population-allele frequencies for this set were not established from the retrieved evidence. (li2021denovolossoffunction pages 4-5, plassche2021med12related(neuro)developmentaldisorders pages 3-5)

For the seven-patient study, six individuals underwent X-inactivation assessment; **five informative individuals** showed skewing, with **four particularly extreme ratios of 97:3–99:1**. One assay was uninformative. These observations support a dosage-related hypothesis but do **not** prove which allele is expressed in each embryonic organ. An individual early-stop variant reportedly occurred in a mosaic patient; mosaic allele fraction and X-inactivation estimates must not be conflated. (li2021denovolossoffunction pages 4-5, li2021denovolossoffunction pages 5-6, li2021denovolossoffunction pages 6-7)

**Important variant-classification counterexample:** in the July 2026 report, trio follow-up identified de novo **NM_005120.3:c.3868-5C>G**, absent from the investigated population databases. Its predicted splice-acceptor effect had **SpliceAI Δ = 0.60**, but patient RNA and protein studies were unavailable; the authors **retained VUS classification**. It must not enter a knowledge base as a proven pathogenic splice allele or as measured MED12 loss of function. A de novo **intragenic MED12 deletion** was also identified in the review’s DECIPHER case; this supports considering copy-number analysis when sequence testing is unrevealing. No Hardikar-specific repeat expansion, mitochondrial defect, established epigenetic signature, or validated large recurrent chromosomal syndrome was identified. (kahy2026anovelintronic pages 2-5, kahy2026anovelintronic pages 15-16, kahy2026anovelintronic pages 16-18)

## 5. Environmental information

Hardikar syndrome is **not an infection or intoxication** and has no established causative environmental exposure. Prenatal imaging may be normal despite subsequent severe disease, as illustrated by the 2026 clinically suggestive case; that observation does not establish an environmental cause. Infectious complications may arise **downstream** of illness or treatment needs: recurrent urinary infections occurred in the 2008 case, while the 2026 child died with *Pasteurella multocida* sepsis during advanced liver disease. The latter patient’s MED12 variant remains a VUS; neither infection proves primary immunodeficiency due to Hardikar syndrome. No applicable causal pathogen NCBI Taxon or preventive chemical ChEBI identifier is justified. (poley2008hardikarsyndromenew pages 3-4, kahy2026anovelintronic pages 1-2, kahy2026anovelintronic pages 15-16)

## 6. Mechanism and pathophysiology

**Ordered causal chain—evidence level shown at each step:**

1. **Pathogenic MED12 truncation or deletion leads to reduced functional MED12 dosage**; transcript decay was *predicted* for the seven reported variants rather than quantified in every affected organ. **[Human genetic evidence; tissue-level molecular consequence inferred.]** (li2021denovolossoffunction pages 4-5, plassche2021med12related(neuro)developmentaldisorders pages 3-5)
2. **Reduced MED12 leads to altered Mediator-dependent transcriptional regulation** through the MED12–MED13–cyclin C–CDK8 kinase module and its connections to transcription factors and RNA polymerase II. **[Established MED12 biology; the complete effect in Hardikar embryonic tissues remains inferred.]** (plassche2021med12related(neuro)developmentaldisorders pages 1-3, plassche2021med12related(neuro)developmentaldisorders pages 3-5, rocha2010med12isessential pages 1-2)
3. **Altered transcriptional regulation leads to disturbed developmental cell specification and organogenesis**. **Branch A:** zebrafish *med12* disruption impairs **Sox32/sox17- and her5-associated endodermal programs**, plausibly contributing to digestive/hepatobiliary malformations. **Branch B:** animal and cell experiments implicate **SOX9, Wnt/β-catenin, and Wnt/planar-cell-polarity signaling**, plausibly contributing to craniofacial, cardiac, and axial malformations. **[Direct experimental evidence in models; organ-by-organ causal assignment in patients inferred.]** (plassche2021med12related(neuro)developmentaldisorders pages 5-6, rocha2010med12isessential pages 1-2, shin2008multiplerolesfor pages 1-2)
4. **Abnormal organ development leads to congenital clefts, malrotation, biliary-tract and urinary defects, retinal changes, and variable cardiovascular anomalies.** The specific cellular lesion responsible for each individual human feature has **not** been demonstrated. **[Human phenotype observed; connection to individual model pathways inferred.]** (li2021denovolossoffunction pages 1-2, poley2008hardikarsyndromenew pages 1-3, li2021denovolossoffunction pages 3-4)
5. **Biliary maldevelopment or impaired bile flow results in cholestasis**, which in severe cases **leads to** ductular changes, fibrosis/cirrhosis, pruritus, malnutrition, portal hypertension, and possible liver failure. This last progression is directly supported by serial human clinical observations and biopsies; a universal course is not established. **[Human clinical and pathology evidence.]** (poley2008hardikarsyndromenew pages 1-3, poley2008hardikarsyndromenew pages 3-4, kahy2026anovelintronic pages 15-16)

**What is established versus hypothesized.** MED12 is a **nuclear transcriptional regulator**, not a proven missing bile-acid transporter, ion channel, or metabolic enzyme in this syndrome. In primary zebrafish experiments, *shiri/med12* mutants showed liver/pancreas defects and altered endodermal **her5** expression; *med12* modulated Sox32-driven **sox17** expression. Mouse Med12 hypomorphs had impaired canonical Wnt and Wnt/PCP signaling, neural-tube-closure and cardiac defects; null embryos failed gastrulation. Cellular studies summarized in the MED12 review implicated β-catenin, SOX9, REST, and Hedgehog pathway regulation, **but effects of particular MED12 missense alleles in other disorders must not be assigned directly to Hardikar truncations**. An early analogy to **JAG1/Notch**-related Alagille syndrome was explicitly speculation, **not a demonstrated JAG1/Notch lesion in Hardikar syndrome**. (plassche2021med12related(neuro)developmentaldisorders pages 5-6, poley2008hardikarsyndromenew pages 4-6, plassche2021med12related(neuro)developmentaldisorders pages 7-10, rocha2010med12isessential pages 1-2, shin2008multiplerolesfor pages 1-2)

**Annotation suggestions, not validated disease-specific mechanism IDs:** GO biological-process labels *RNA polymerase II-mediated transcription*, *embryonic organ development*, *endoderm development*, *canonical Wnt signaling*, *planar-cell-polarity signaling*, and *bile-duct development*; cellular-component label *nucleus*. Candidate CL cell labels are *endodermal progenitor cell*, *cholangiocyte*, *hepatocyte*, *retinal pigment epithelial cell*, and *neural crest cell*. These refer to implicated tissues or plausible embryonic precursors: there is **no patient-cell atlas establishing that MED12 dysfunction selectively targets each listed cell type**. No validated Hardikar-specific transcriptomic, proteomic, metabolomic, lipidomic, methylation, single-cell, spatial-omics, or CRISPR-screen signature was substantiated in the accessible primary clinical studies. The 2021 expert review **proposed** isogenic iNeuron modeling; a proposal is not a completed Hardikar functional assay. (plassche2021med12related(neuro)developmentaldisorders pages 1-3, plassche2021med12related(neuro)developmentaldisorders pages 3-5, plassche2021med12related(neuro)developmental pages 10-12, shin2008multiplerolesfor pages 1-2)

## 7. Anatomical structures affected

**Primary sites:** liver and biliary tree, gallbladder, gut/foregut, lip/palate, retina, and urinary/genital tract. **Additional reported sites:** heart and great vessels, carotid or cerebral vessels, external and inner ear, diaphragm, and lungs. The strongest demonstrated tissue pathology is **portal fibrosis with bile-duct proliferation** in the transplanted child and **interlobular bile-duct paucity with portal fibrosis** in the clinically suggestive 2026 VUS case; these findings are not identical and should not be collapsed into one obligatory lesion. Suggestions for UBERON labels, pending identifier validation, are *liver*, *intrahepatic bile duct*, *extrahepatic bile duct*, *gallbladder*, *small intestine*, *lip*, *palate*, *retina*, *kidney*, *ureter*, *aorta*, and *diaphragm*. The relevant MED12 subcellular annotation is *nucleus/Mediator complex*, not mitochondrion or lysosome. Clefting can be **bilateral**—the 2008 child had bilateral cleft lip and palate—but universal symmetry or laterality cannot be asserted. (poley2008hardikarsyndromenew pages 1-3, poley2008hardikarsyndromenew pages 4-6, plassche2021med12related(neuro)developmentaldisorders pages 3-5, kahy2026anovelintronic pages 15-16)

## 8. Temporal development

The anatomical defects arise **prenatally** and are recognized prenatally, neonatally, or in childhood depending on the feature and investigation. Hepatobiliary illness may first present as neonatal cholestasis; severe disease **may progress** over months or years, whereas many structural malformations are persistent but not intrinsically progressive after birth. In the 2008 child, biopsy showed bile-duct changes and fibrosis at approximately **one month**, cirrhosis was documented at **7.5 months**, and liver transplant occurred at **24 months**; she was active at **eight years**. A 2026 clinically suggestive child developed portal-hypertension complications and died at **three years eight months** before transplantation, but her MED12 VUS prevents treating this as a confirmed molecular-natural-history endpoint. There are **no validated early/intermediate/late stages**, progression rates, remission probabilities, or critical-period intervention trials. An embryonic vulnerability window of approximately **30–70 gestational days** was proposed in 2008, not clinically validated. (poley2008hardikarsyndromenew pages 1-3, poley2008hardikarsyndromenew pages 3-4, poley2008hardikarsyndromenew pages 4-6, kahy2026anovelintronic pages 15-16)

## 9. Inheritance and population epidemiology

**Inheritance:** an X-linked, predominantly female phenotype associated with heterozygous MED12 loss-of-function variants; most molecularly characterized cases arose de novo, while reports of mosaicism and maternal transmission caution against assuming every family has zero recurrence risk. **Penetrance, age-specific penetrance, reproductive fitness, carrier frequency, anticipation, founder alleles, ancestry-specific risks, consanguinity effects, and empirical germline-mosaic recurrence risk are unknown.** Genetic counseling should consider parental testing and residual mosaicism rather than substitute a purported syndrome-specific percentage. (li2021denovolossoffunction pages 4-5, kahy2026anovelintronic pages 2-5, kahy2026anovelintronic pages 1-2)

**Incidence and prevalence are unknown.** Li and colleagues studied **seven genetically characterized females** in 2021; the 2026 review’s **35 analyzed entries** reflect case compilation with molecular-certainty differences, not cases per 100,000. Its abstract states **34 previously reported cases** before its new case. Published female predominance is not a measurable population male:female ratio. Cases reported from different families and locations do not establish geographic clustering, founder effects, or racial predisposition. (li2021denovolossoffunction pages 1-2, kahy2026anovelintronic pages 2-5, kahy2026anovelintronic pages 1-2)

## 10. Diagnostics

**Clinical recognition and differential.** Concurrent neonatal/infantile cholestasis, cleft lip/palate or unusual retinal findings, malrotation, urinary anomalies, and cardiovascular lesions should prompt assessment for Hardikar syndrome. Investigate clinically urgent alternatives including **biliary atresia**, **Alagille syndrome (JAG1/NOTCH2-related)**, progressive familial intrahepatic cholestasis, and mitochondrial hepatopathies; CHARGE, 22q11.2 deletion, and Kabuki syndrome may overlap with aspects of the malformation pattern. No validated formal diagnostic score or unique biochemical biomarker was identified. (li2021denovolossoffunction pages 5-6, poley2008hardikarsyndromenew pages 4-6, kahy2026anovelintronic pages 16-18)

**Tests actually used or supported by cases:** conjugated bilirubin, liver enzymes and cholestasis evaluation; abdominal ultrasonography to examine liver, gallbladder, and bile ducts; specialist-directed imaging/assessment for intestinal malrotation and urinary abnormalities; echocardiography and vascular imaging; detailed ophthalmology and audiology. Liver biopsy has shown cholestasis, bile-duct pathology, and fibrosis but is **not pathognomonic**. One published case’s conjugated bilirubin increased from **1.4 mg/dL at 1.5 months to 14.0 mg/dL at 22 months**, then fell to **0.2 mg/dL after transplantation**. No Hardikar-specific EEG, EMG, ECG electrophysiological pattern or validated disease-specific LOINC assay was identified. (li2021denovolossoffunction pages 6-7, poley2008hardikarsyndromenew pages 1-3, poley2008hardikarsyndromenew pages 3-4, kahy2026anovelintronic pages 15-16)

**Genetic approach:** trio **whole-exome sequencing (WES)** or appropriately analyzed genome sequencing that covers **MED12**, followed by interpretation of variant class, phenotype, segregation, and possible mosaicism; ensure that the assay can assess splice-region changes and **copy-number variation**. Targeted MED12 sequencing may be reasonable for a highly characteristic phenotype or known familial allele. Chromosomal microarray is useful for alternative chromosomal diagnoses or detectable deletions but does not replace sequence analysis; a normal karyotype or FISH result does not exclude MED12 sequence variation. WGS may help where WES misses noncoding or structural changes, but disease-specific comparative diagnostic-yield data are unavailable. Transcript testing or a minigene assay could help resolve a plausible splice VUS; **in-silico splice prediction is not equivalent to functional validation**. No established disease-specific RNA-seq, proteomic, metabolomic, epigenomic, or liquid-biopsy clinical test was found. (poley2008hardikarsyndromenew pages 3-4, kahy2026anovelintronic pages 2-5, kahy2026anovelintronic pages 15-16, kahy2026anovelintronic pages 16-18)

## 11. Outcomes and prognosis

Prognosis is **variable and insufficiently quantified**: published reports include survival into school age after liver transplantation, progressive early cirrhosis, and a **fatal unprovoked intracranial hemorrhage at age 21** in the 2021 series. The 2026 VUS case ended in fatal sepsis amid advanced liver disease, but is not a molecularly confirmed prognostic observation. There are **no reliable five-/ten-year survival rates, average life expectancy, standardized disability rates, validated quality-of-life measures, or prognostic biomarkers**. Clinical features with obvious potential prognostic importance include severity of cholestasis/portal hypertension and cardiovascular or cerebrovascular lesions; predictive performance has not been measured. Treatment of hepatic disease cannot be assumed to reverse extrahepatic congenital anomalies. (li2021denovolossoffunction pages 1-2, poley2008hardikarsyndromenew pages 1-3, poley2008hardikarsyndromenew pages 3-4, kahy2026anovelintronic pages 15-16)

## 12. Treatment and current real-world implementation

There is **no demonstrated MED12-directed, disease-modifying pharmacotherapy**. Care is multidisciplinary and lesion-directed; the NCIT labels below are **suggested intervention mappings**, not independently verified NCIT numeric codes. In one primary report, **Ladd procedure** treated malrotation, **ureterostomies** and later reconstructive urinary operations managed complex urogenital defects, **gastrostomy** supported feeding, and **living-related-donor liver transplantation** at two years treated end-stage liver disease. Jaundice resolved and growth improved after transplantation, but urinary infections recurred. Cleft repair and cochlear implantation were documented elsewhere in the clinical series. Candidate NCIT intervention labels include *Liver Transplantation*, *Ladd Procedure*, *Cleft Lip Repair*, *Cleft Palate Repair*, *Gastrostomy*, *Ureterostomy*, *Cochlear Implantation*, *Echocardiography*, *Magnetic Resonance Angiography*, and *Genetic Counseling*; verify exact vocabulary entries before database ingestion. (li2021denovolossoffunction pages 3-4, poley2008hardikarsyndromenew pages 1-3, poley2008hardikarsyndromenew pages 3-4)

Nutritional support and fat-soluble vitamins were given in the transplanted child; **ursodeoxycholic acid did not improve that individual’s cholestasis**, and this single response must not be represented as a controlled treatment comparison. Consider transplant assessment for severe progressive liver disease according to specialist practice. No Hardikar-specific efficacy percentage, comparative transplant rate, adverse-event rate, pharmacogenomic regimen, gene therapy, cell therapy, antisense/RNA therapy, targeted immunotherapy, or intervention trial/NCT identifier was identified by the disease-specific trial searches. This means **not found in the searched registry**, not proof that no unregistered intervention has ever occurred. Suggested chemical labels such as *ursodeoxycholic acid* and *fat-soluble vitamins* should receive ChEBI IDs only after independent vocabulary verification. (poley2008hardikarsyndromenew pages 1-3, poley2008hardikarsyndromenew pages 3-4)

## 13. Prevention, surveillance, and counseling

A de novo developmental disorder has **no established lifestyle modification, vaccine, exposure avoidance, or primary pharmacological prophylaxis that prevents the underlying syndrome**. Secondary prevention is timely recognition of organ complications and a molecular diagnosis where possible. Li and colleagues recommend coordinated ophthalmologic evaluation, echocardiography and serial cardiovascular assessment, **carotid imaging and head/neck MRA**, audiology, and hepatic, gastrointestinal, and genitourinary evaluation; their suggested serial schedules are **case-series expert recommendations**, not prospectively validated screening intervals. Manage nutrition and cholestasis and correct obstructive or vascular problems to reduce tertiary morbidity. Offer reproductive counseling and variant-specific familial testing when a pathogenic variant is confirmed; prenatal or preimplantation testing is technically conceivable for a known familial pathogenic allele, but there is no established population newborn or carrier-screening program for Hardikar syndrome. A VUS alone should not be treated as a definitive predictive familial test. (li2021denovolossoffunction pages 6-7, kahy2026anovelintronic pages 16-18)

## 14. Natural disease in other species and comparative biology

The human syndrome is documented in **Homo sapiens, NCBI Taxon 9606**. No naturally occurring veterinary **Hardikar syndrome**, affected breed/VBO designation, animal prevalence, animal-to-human transmission, or zoonotic potential was substantiated. Vertebrate conservation is supported instead by experimental *Med12/med12* perturbations in mouse and zebrafish. Accordingly, a zebrafish embryo with disrupted *med12* is a **comparative developmental model**, not a naturally occurring veterinary diagnosis. Species-level experimental phenotype similarities do not establish the complete human multi-organ syndrome in another species. (li2021denovolossoffunction pages 4-5, wang2006asubunitof pages 1-2, rocha2010med12isessential pages 1-2, shin2008multiplerolesfor pages 1-2)

## 15. Model organisms and research applications

**Zebrafish, *Danio rerio* (NCBI Taxon 7955):** the experimentally characterized *shiri/med12* mutant has endodermal and liver/pancreas abnormalities linked to altered **her5** and Sox32/**sox17** regulation. The *motionless/med12* mutant impairs selected monoaminergic neurons and cranial sensory ganglia; delivery of human MED12 RNA rescued aspects of the mutant phenotype. The *kohtalo/med12* mutant reduces hindbrain boundary-cell formation and proliferation. These are distinct experimental alleles/phenotypes and should not be merged into a single engineered Hardikar organism. **Mouse, *Mus musculus* (NCBI Taxon 10090):** Med12 hypomorphic embryos showed defects in neural-tube closure, axis elongation, somitogenesis and heart formation, together with impaired Wnt and Wnt/PCP signaling; null embryos could not complete gastrulation. These models establish developmental roles but do not reproduce the full human retinal–biliary–cleft–urinary phenotype or faithfully mimic mosaic heterozygous human X inactivation. No validated animal knock-in of a specific human Hardikar allele was established in the accessible studies. Candidate model-resource entry points are **ZFIN** and **MGI**, subject to allele-specific record checks. (wang2006asubunitof pages 1-2, rocha2010med12isessential pages 1-2, hong2011thetranscriptionalmediator pages 1-2, shin2008multiplerolesfor pages 1-2)

### Evidence quotations, dates, and primary-source links

- **Human clinical, Poley and Proud, 2008** ([DOI:10.1002/ajmg.a.32266](https://doi.org/10.1002/ajmg.a.32266)): abstract: “Hardikar syndrome (HS) is a disorder of multiple anomalies predominantly characterized by cleft lip/palate, liver and biliary tract disease, intestinal malrotation, obstructive uropathy, and retinopathy.” The same abstract describes “the need for liver transplantation.” (poley2008hardikarsyndromenew pages 1-3)
- **Human genetic, Li and colleagues, published online 2020; issue April 2021**, PMID **33244166** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/33244166/); [DOI:10.1038/s41436-020-01031-7](https://doi.org/10.1038/s41436-020-01031-7)): the article’s title accurately summarizes its central finding, “De novo loss-of-function variants in X-linked MED12 are associated with Hardikar syndrome in females.” The reviewed evidence documents seven affected women and seven truncating variants; a longer verbatim abstract quotation could not be checked against directly readable publisher full text. (li2021denovolossoffunction pages 1-2, li2021denovolossoffunction pages 4-5)
- **Model-organism, Shin and colleagues, 2008** ([DOI:10.1016/j.ydbio.2008.02.031](https://doi.org/10.1016/j.ydbio.2008.02.031)): abstract: “shiri encodes Med12, a regulatory subunit of the transcriptional Mediator complex”; mutant embryos had liver and pancreatic developmental defects. (shin2008multiplerolesfor pages 1-2)
- **Model-organism, Rocha and colleagues, 2010** ([DOI:10.1242/dev.053660](https://doi.org/10.1242/dev.053660)): abstract: “the Wnt/planar cell polarity pathway is disrupted and ... canonical Wnt/β-catenin signaling is impaired” in Med12 hypomorphic mouse embryos. This is mouse evidence, **not direct measurement in Hardikar patients**. (rocha2010med12isessential pages 1-2)
- **Human clinical and literature synthesis, El Kahy and colleagues, published 9 July 2026** ([DOI:10.3390/genes17070787](https://doi.org/10.3390/genes17070787)): abstract: “The identified MED12 variant is classified as a variant of uncertain significance (VUS).” Its tabulated case compilation is informative but should not be used to imply population prevalence or to promote that variant to pathogenic. (kahy2026anovelintronic pages 2-5, kahy2026anovelintronic pages 1-2, kahy2026anovelintronic pages 16-18)

**Knowledge-base confidence statement:** The **MED12–Hardikar association and congenital multisystem phenotype** have strong human case-series support; the **particular organ-specific transcriptional pathways** remain largely cross-species mechanistic inference; exact phenotype frequencies, epidemiology, biomarker performance, and treatment response rates remain **unestablished**. (li2021denovolossoffunction pages 1-2, kahy2026anovelintronic pages 2-5, rocha2010med12isessential pages 1-2, kahy2026anovelintronic pages 1-2)

References

1. (li2021denovolossoffunction pages 1-2): Dong Li, Alanna Strong, Kaitlyn M. Shen, David Cassiman, Maria Van Dyck, Natalia Duarte Linhares, Eugenia Ribeiro Valadares, Tiancheng Wang, Sergio D.J. Pena, Jaak Jaeken, Samantha Vergano, Elaine Zackai, Anne Hing, Penny Chow, Arupa Ganguly, Tasja Scholz, Tatjana Bierhals, Deindl Philipp, Hakon Hakonarson, and Elizabeth Bhoj. De novo loss-of-function variants in x-linked med12 are associated with hardikar syndrome in females. Genetics in Medicine, 23:637-644, Apr 2021. URL: https://doi.org/10.1038/s41436-020-01031-7, doi:10.1038/s41436-020-01031-7. This article has 44 citations and is from a highest quality peer-reviewed journal.

2. (kahy2026anovelintronic pages 2-5): Nabil El Kahy, Adib Moukarzel, Nada Assaf, Riwa Chdid, Romy Moussallem, Nabiha Salem, and Alain Chebly. A novel intronic variant in med12 associated with a predominantly hepatobiliary phenotype suggestive of hardikar syndrome: a case report and literature review. Genes, 17:787, Jul 2026. URL: https://doi.org/10.3390/genes17070787, doi:10.3390/genes17070787. This article has 0 citations.

3. (kahy2026anovelintronic pages 1-2): Nabil El Kahy, Adib Moukarzel, Nada Assaf, Riwa Chdid, Romy Moussallem, Nabiha Salem, and Alain Chebly. A novel intronic variant in med12 associated with a predominantly hepatobiliary phenotype suggestive of hardikar syndrome: a case report and literature review. Genes, 17:787, Jul 2026. URL: https://doi.org/10.3390/genes17070787, doi:10.3390/genes17070787. This article has 0 citations.

4. (OpenTargets Search: Hardikar syndrome): Open Targets Query (Hardikar syndrome, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (poley2008hardikarsyndromenew pages 1-3): J. Rainer Poley and Virginia K. Proud. Hardikar syndrome: new features. American Journal of Medical Genetics Part A, 146A:2473-2479, Oct 2008. URL: https://doi.org/10.1002/ajmg.a.32266, doi:10.1002/ajmg.a.32266. This article has 16 citations.

6. (kahy2026anovelintronic pages 16-18): Nabil El Kahy, Adib Moukarzel, Nada Assaf, Riwa Chdid, Romy Moussallem, Nabiha Salem, and Alain Chebly. A novel intronic variant in med12 associated with a predominantly hepatobiliary phenotype suggestive of hardikar syndrome: a case report and literature review. Genes, 17:787, Jul 2026. URL: https://doi.org/10.3390/genes17070787, doi:10.3390/genes17070787. This article has 0 citations.

7. (li2021denovolossoffunction pages 4-5): Dong Li, Alanna Strong, Kaitlyn M. Shen, David Cassiman, Maria Van Dyck, Natalia Duarte Linhares, Eugenia Ribeiro Valadares, Tiancheng Wang, Sergio D.J. Pena, Jaak Jaeken, Samantha Vergano, Elaine Zackai, Anne Hing, Penny Chow, Arupa Ganguly, Tasja Scholz, Tatjana Bierhals, Deindl Philipp, Hakon Hakonarson, and Elizabeth Bhoj. De novo loss-of-function variants in x-linked med12 are associated with hardikar syndrome in females. Genetics in Medicine, 23:637-644, Apr 2021. URL: https://doi.org/10.1038/s41436-020-01031-7, doi:10.1038/s41436-020-01031-7. This article has 44 citations and is from a highest quality peer-reviewed journal.

8. (plassche2021med12related(neuro)developmentaldisorders pages 1-3): Stijn R. van de Plassche and Arjan P. M. de Brouwer. Med12-related (neuro)developmental disorders: a question of causality. Genes, 12 5:663, Apr 2021. URL: https://doi.org/10.3390/genes12050663, doi:10.3390/genes12050663. This article has 28 citations.

9. (plassche2021med12related(neuro)developmentaldisorders pages 3-5): Stijn R. van de Plassche and Arjan P. M. de Brouwer. Med12-related (neuro)developmental disorders: a question of causality. Genes, 12 5:663, Apr 2021. URL: https://doi.org/10.3390/genes12050663, doi:10.3390/genes12050663. This article has 28 citations.

10. (li2021denovolossoffunction pages 6-7): Dong Li, Alanna Strong, Kaitlyn M. Shen, David Cassiman, Maria Van Dyck, Natalia Duarte Linhares, Eugenia Ribeiro Valadares, Tiancheng Wang, Sergio D.J. Pena, Jaak Jaeken, Samantha Vergano, Elaine Zackai, Anne Hing, Penny Chow, Arupa Ganguly, Tasja Scholz, Tatjana Bierhals, Deindl Philipp, Hakon Hakonarson, and Elizabeth Bhoj. De novo loss-of-function variants in x-linked med12 are associated with hardikar syndrome in females. Genetics in Medicine, 23:637-644, Apr 2021. URL: https://doi.org/10.1038/s41436-020-01031-7, doi:10.1038/s41436-020-01031-7. This article has 44 citations and is from a highest quality peer-reviewed journal.

11. (li2021denovolossoffunction pages 3-4): Dong Li, Alanna Strong, Kaitlyn M. Shen, David Cassiman, Maria Van Dyck, Natalia Duarte Linhares, Eugenia Ribeiro Valadares, Tiancheng Wang, Sergio D.J. Pena, Jaak Jaeken, Samantha Vergano, Elaine Zackai, Anne Hing, Penny Chow, Arupa Ganguly, Tasja Scholz, Tatjana Bierhals, Deindl Philipp, Hakon Hakonarson, and Elizabeth Bhoj. De novo loss-of-function variants in x-linked med12 are associated with hardikar syndrome in females. Genetics in Medicine, 23:637-644, Apr 2021. URL: https://doi.org/10.1038/s41436-020-01031-7, doi:10.1038/s41436-020-01031-7. This article has 44 citations and is from a highest quality peer-reviewed journal.

12. (kahy2026anovelintronic pages 5-6): Nabil El Kahy, Adib Moukarzel, Nada Assaf, Riwa Chdid, Romy Moussallem, Nabiha Salem, and Alain Chebly. A novel intronic variant in med12 associated with a predominantly hepatobiliary phenotype suggestive of hardikar syndrome: a case report and literature review. Genes, 17:787, Jul 2026. URL: https://doi.org/10.3390/genes17070787, doi:10.3390/genes17070787. This article has 0 citations.

13. (kahy2026anovelintronic pages 15-16): Nabil El Kahy, Adib Moukarzel, Nada Assaf, Riwa Chdid, Romy Moussallem, Nabiha Salem, and Alain Chebly. A novel intronic variant in med12 associated with a predominantly hepatobiliary phenotype suggestive of hardikar syndrome: a case report and literature review. Genes, 17:787, Jul 2026. URL: https://doi.org/10.3390/genes17070787, doi:10.3390/genes17070787. This article has 0 citations.

14. (poley2008hardikarsyndromenew pages 3-4): J. Rainer Poley and Virginia K. Proud. Hardikar syndrome: new features. American Journal of Medical Genetics Part A, 146A:2473-2479, Oct 2008. URL: https://doi.org/10.1002/ajmg.a.32266, doi:10.1002/ajmg.a.32266. This article has 16 citations.

15. (li2021denovolossoffunction pages 5-6): Dong Li, Alanna Strong, Kaitlyn M. Shen, David Cassiman, Maria Van Dyck, Natalia Duarte Linhares, Eugenia Ribeiro Valadares, Tiancheng Wang, Sergio D.J. Pena, Jaak Jaeken, Samantha Vergano, Elaine Zackai, Anne Hing, Penny Chow, Arupa Ganguly, Tasja Scholz, Tatjana Bierhals, Deindl Philipp, Hakon Hakonarson, and Elizabeth Bhoj. De novo loss-of-function variants in x-linked med12 are associated with hardikar syndrome in females. Genetics in Medicine, 23:637-644, Apr 2021. URL: https://doi.org/10.1038/s41436-020-01031-7, doi:10.1038/s41436-020-01031-7. This article has 44 citations and is from a highest quality peer-reviewed journal.

16. (rocha2010med12isessential pages 1-2): Pedro P. Rocha, Manuela Scholze, Wilfrid Bleiß, and Heinrich Schrewe. Med12 is essential for early mouse development and for canonical wnt and wnt/pcp signaling. Development, 137:2723-2731, Aug 2010. URL: https://doi.org/10.1242/dev.053660, doi:10.1242/dev.053660. This article has 205 citations and is from a domain leading peer-reviewed journal.

17. (plassche2021med12related(neuro)developmentaldisorders pages 5-6): Stijn R. van de Plassche and Arjan P. M. de Brouwer. Med12-related (neuro)developmental disorders: a question of causality. Genes, 12 5:663, Apr 2021. URL: https://doi.org/10.3390/genes12050663, doi:10.3390/genes12050663. This article has 28 citations.

18. (shin2008multiplerolesfor pages 1-2): Chong Hyun Shin, Won-Suk Chung, Sung-Kook Hong, Elke A. Ober, Heather Verkade, Holly A. Field, Jan Huisken, and Didier Y. R. Stainier. Multiple roles for med12 in vertebrate endoderm development. Developmental biology, 317 2:467-79, May 2008. URL: https://doi.org/10.1016/j.ydbio.2008.02.031, doi:10.1016/j.ydbio.2008.02.031. This article has 76 citations and is from a peer-reviewed journal.

19. (poley2008hardikarsyndromenew pages 4-6): J. Rainer Poley and Virginia K. Proud. Hardikar syndrome: new features. American Journal of Medical Genetics Part A, 146A:2473-2479, Oct 2008. URL: https://doi.org/10.1002/ajmg.a.32266, doi:10.1002/ajmg.a.32266. This article has 16 citations.

20. (plassche2021med12related(neuro)developmentaldisorders pages 7-10): Stijn R. van de Plassche and Arjan P. M. de Brouwer. Med12-related (neuro)developmental disorders: a question of causality. Genes, 12 5:663, Apr 2021. URL: https://doi.org/10.3390/genes12050663, doi:10.3390/genes12050663. This article has 28 citations.

21. (plassche2021med12related(neuro)developmental pages 10-12): S van de Plassche and A de Brouwer. Med12-related (neuro) developmental disorders: a question of causality. genes 2021, 12, 663. Unknown journal, 2021.

22. (wang2006asubunitof pages 1-2): Xiaoqun Wang, Nan Yang, Etsuko Uno, Robert G. Roeder, and Su Guo. A subunit of the mediator complex regulates vertebrate neuronal development. Proceedings of the National Academy of Sciences, 103:17284-17289, Nov 2006. URL: https://doi.org/10.1073/pnas.0605414103, doi:10.1073/pnas.0605414103. This article has 97 citations and is from a highest quality peer-reviewed journal.

23. (hong2011thetranscriptionalmediator pages 1-2): Sung-Kook Hong and Igor B. Dawid. The transcriptional mediator component med12 is required for hindbrain boundary formation. PLoS ONE, 6:e19076, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0019076, doi:10.1371/journal.pone.0019076. This article has 19 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Hardikar_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012997` (2 mentions) - the report calls it "if available"; MONDO calls it **cholestasis-pigmentary retinopathy-cleft palate syndrome**