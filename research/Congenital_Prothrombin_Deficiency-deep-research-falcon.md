---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T19:51:11.726924'
end_time: '2026-09-05T20:01:37.532294'
duration_seconds: 625.81
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Prothrombin Deficiency
  mondo_id: MONDO:0013361
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 22
  verified: 20
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.048
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013361
    reported_labels:
    - if available
    ontology_label: congenital prothrombin deficiency
  unresolved_terms:
  - HP:0001020
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Congenital_Prothrombin_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Prothrombin Deficiency
- **MONDO ID:** MONDO:0013361 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Congenital Prothrombin Deficiency** covering all of the
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
- **Disease Name:** Congenital Prothrombin Deficiency
- **MONDO ID:** MONDO:0013361 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Congenital Prothrombin Deficiency** covering all of the
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


# Congenital Prothrombin Deficiency: Comprehensive Disease-Characteristics Report

## Executive summary

Congenital prothrombin deficiency is an ultra-rare, usually autosomal-recessive bleeding disorder caused by biallelic pathogenic variants in **F2**, which encodes the vitamin-K-dependent zymogen prothrombin (factor II). It comprises quantitative **hypoprothrombinemia** and qualitative **dysprothrombinemia**. Estimated prevalence is approximately **1 per 2,000,000**, although ascertainment is incomplete and prevalence is higher in populations with substantial consanguinity. Complete F2 deficiency has not been documented in living humans and is considered incompatible with survival. Clinical expression ranges from incidental coagulation-test abnormalities to neonatal or childhood mucosal, soft-tissue, gastrointestinal, joint, intracranial, surgical, and obstetric hemorrhage. Diagnosis rests on prolonged PT and aPTT, reduced factor-II coagulant activity, antigen measurement, exclusion of acquired causes, and molecular confirmation. There is no generally available specific factor-II concentrate; bleeding and procedures are managed mainly with prothrombin-complex concentrate (PCC), or fresh-frozen plasma (FFP) when PCC is unavailable. Evidence remains dominated by case reports, small series, expert reviews, and model-organism studies rather than prospective trials. (castaman2017diagnosisandtreatment pages 10-11, menegatti2020clinicalandlaboratory pages 1-2, lancellotti12009congenitalprothrombindeficiency pages 2-4)

The following table provides a compact knowledge-base representation; the narrative afterward supplies qualification and mechanistic detail.

| Knowledge-base field | Curated summary | Ontology / evidence |
|---|---|---|
| Disease definition | Ultra-rare inherited bleeding disorder caused by reduced quantity or impaired function of coagulation factor II (prothrombin). Complete prothrombin absence has not been observed in humans and is considered incompatible with survival. | **MONDO:** MONDO:0013361. Reviews: DOI [10.1055/s-0029-1225759](https://doi.org/10.1055/s-0029-1225759), June 2009; DOI [10.3390/jcm6040045](https://doi.org/10.3390/jcm6040045), April 2017. (castaman2017diagnosisandtreatment pages 10-11, lancellotti12009congenitalprothrombindeficiency pages 2-4) |
| Identifiers and synonyms | **Synonyms:** congenital factor II deficiency; hereditary factor II deficiency; congenital prothrombin deficiency; hypoprothrombinemia; dysprothrombinemia. **OMIM, Orphanet, MeSH, ICD-10/ICD-11:** exact identifiers were not verified in the gathered evidence and should be curated directly from those resources. | MONDO:0013361; disease-target entry in Open Targets. (OpenTargets Search: congenital prothrombin deficiency-F2) |
| Epidemiology and inheritance | Estimated prevalence approximately **1 in 2,000,000** for severe homozygous/compound-heterozygous deficiency. Predominantly **autosomal recessive**, affecting both sexes; prevalence is higher where consanguinity is common. Penetrance and carrier frequency are not reliably quantified. | ClinGen classifies the **F2–disease** relationship as **Definitive** with AR inheritance. DOI [10.1016/j.thromres.2019.09.006](https://doi.org/10.1016/j.thromres.2019.09.006), December 2020. (OpenTargets Search: congenital prothrombin deficiency-F2, menegatti2020clinicalandlaboratory pages 1-2) |
| Causal gene and protein | **F2**, ENSG00000180210, encodes vitamin-K-dependent prothrombin, the zymogen of thrombin. The protein contains a signal peptide, propeptide, Gla domain, kringle 1 and 2 domains, and a serine-protease domain; factor Xa cleavage at Arg273 and Arg322 generates active thrombin. | **Target:** F2/coagulation factor II, thrombin; chromosome 11p11–q12. Suggested GO: blood coagulation (**GO:0007596**), fibrin clot formation (**GO:0072378**), proteolysis (**GO:0006508**). (OpenTargets Search: congenital prothrombin deficiency-F2, lancellotti12009congenitalprothrombindeficiency pages 2-4, grzegorski2020disruptionofthe pages 1-2) |
| Biochemical subtypes | **Type I—hypoprothrombinemia:** factor II activity and antigen are both reduced. **Type II—dysprothrombinemia:** activity is reduced while antigen is normal or near normal. Activity-based severity used in reviews: **severe <5%**, **moderate 5–10%**, **mild >10%**. | Suggested phenotypic/laboratory concept: reduced coagulation factor II activity. Classification and thresholds derive mainly from expert reviews rather than validated prospective criteria. (lancellotti12009congenitalprothrombindeficiency pages 2-4) |
| Representative pathogenic variants | Germline biallelic variants include missense, in-frame deletion, frameshift, splice-region, and other loss-of-function alleles. Examples include **Arg271Cys** with factor II activity **10.2%** and severe bleeding; **Ala362Thr (Prothrombin Vellore 1)** near catalytic His363/Cys364; Arg−1Gln affecting the furin-recognition sequence; Arg457Gln enriched among reported Puerto Rican cases; and compound Prothrombin Edmonton R−4Q plus a deletion. Population allele frequencies and current ClinVar classifications were not established here and require variant-level curation. | Primary molecular study: DOI [10.1111/j.1538-7836.2005.01402.x](https://doi.org/10.1111/j.1538-7836.2005.01402.x), July 2005. Historical F2 variant PMIDs include **1421398, 1349838, 3567158, 3801671, 22028381, 6405779, 1354985, 7792730, 3771562, 2719946**. (jayandharan2005moleculargeneticsof pages 6-7, OpenTargets Search: congenital prothrombin deficiency-F2, wong2006severeprothrombindeficiency pages 6-6) |
| Hallmark phenotypes | Variable, lifelong bleeding diathesis: easy bruising (**HP:0000978**), hematoma (**HP:0001020**), epistaxis (**HP:0000421**), oral/gingival bleeding (**HP:0000225**, suggested), menorrhagia (**HP:0000132**), prolonged postsurgical bleeding (**HP:0004846**), gastrointestinal hemorrhage (**HP:0002239**), hemarthrosis (**HP:0005261**), muscle hemorrhage (**HP:0012233**, suggested), and intracranial hemorrhage (**HP:0002170**). Menorrhagia was reported in approximately **20% of homozygous women** in one review. Frequency estimates for other manifestations are unavailable because cohorts are extremely small. | Severe disease may present neonatally or in childhood; mild disease can first appear after dental extraction, surgery, trauma, menstruation, or childbirth. Clinical variability occurs even among individuals sharing a variant. (lancellotti12009congenitalprothrombindeficiency pages 2-4) |
| Diagnostic signature | Both **PT and aPTT are typically prolonged**, reflecting a common-pathway defect; confirm using a one-stage factor II activity assay. Measure prothrombin antigen to distinguish type I from type II and use mixing studies to exclude an inhibitor. Evaluate vitamin-K status, liver disease, anticoagulant exposure, disseminated intravascular coagulation, and deficiencies of factors V, X, or fibrinogen. Confirm inherited disease with **F2 sequencing plus deletion/duplication analysis**; WES/WGS is useful when single-gene testing is negative or the phenotype is atypical. | Imaging is complication-directed, not diagnostic. CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are ordinarily not indicated unless another syndrome is suspected. (menegatti2020clinicalandlaboratory pages 1-2, lancellotti12009congenitalprothrombindeficiency pages 2-4) |
| Treatment and hemostatic targets | For major bleeding or invasive procedures, use **prothrombin-complex concentrate (PCC) 20–30 IU/kg**, repeating according to factor level and clinical response. Suggested factor II target is **20–30%** for hemostasis and **30–40% for major surgery**. If PCC is unavailable, **fresh-frozen plasma 15–20 mL/kg** may be used, with fluid-overload risk. Antifibrinolytics and local hemostatic measures may supplement replacement for mucosal/dental bleeding. No specific purified factor II concentrate is generally available. | Suggested NCIt concepts: Prothrombin Complex Concentrate; Fresh Frozen Plasma Transfusion; Antifibrinolytic Therapy. PCC contains other vitamin-K-dependent factors and therefore carries thrombotic risk; management should be directed by a specialist bleeding-disorders center. (castaman2017diagnosisandtreatment pages 10-11) |
| Prognosis and temporal course | Lifelong, nonprogressive biochemical deficiency with episodic spontaneous or provoked bleeding. Prognosis is generally favorable when bleeding is recognized and replacement is available, but severe gastrointestinal, intracranial, neonatal, perioperative, or obstetric hemorrhage can be fatal or disabling. No robust survival rate, mortality rate, life-expectancy estimate, or disease-specific quality-of-life dataset is available. | Prognosis is influenced by residual factor II activity, functional variant effect, prior bleeding phenotype, treatment access, and exposure to trauma, surgery, pregnancy, or anticoagulants. (castaman2017diagnosisandtreatment pages 10-11, lancellotti12009congenitalprothrombindeficiency pages 2-4) |
| Model organisms | **Mouse (Mus musculus; NCBI Taxon 10090):** F2 knockout causes embryonic hemorrhage, approximately **50% mortality by embryonic day 10.5**, and fatal postnatal hemorrhage in survivors. **Zebrafish (Danio rerio; Taxon 7955):** kringle-1-disrupting f2 mutation impairs secondary hemostasis; internal hemorrhage begins around one month and **23/24 homozygotes died by 90 days**. **Medaka (Oryzias latipes; Taxon 8090):** genome-edited thrombin-deficient mutants show markedly delayed coagulation. | Mouse models establish the survival requirement for prothrombin; fish models permit study of severe hypomorphic deficiency beyond embryogenesis. Zebrafish DOI [10.1038/s41598-020-60840-7](https://doi.org/10.1038/s41598-020-60840-7), March 2020. (grzegorski2020disruptionofthe pages 4-6, grzegorski2020disruptionofthe pages 1-2) |
| Evidence gaps and current research | There are no large natural-history cohorts, validated genotype-based prognostic models, disease-specific patient-reported outcome studies, approved gene/RNA/cell therapies, or confirmed disease-specific interventional trials in the gathered evidence. Recent work includes small sequencing studies—e.g., **12 southeastern Iranian patients** in 2023—and broader 2024 reviews emphasizing that management advances remain limited for rare bleeding disorders. Single-cell, spatial, transcriptomic, proteomic, metabolomic, lipidomic, and epigenomic disease signatures are unavailable or not established. | Iranian study: DOI [10.34172/cjmb.2023.10](https://doi.org/10.34172/cjmb.2023.10), February 2023. Absence of identified trials means “no trial found,” not proof that none exists. (samarkhazan2023determinationoffactor pages 6-6) |


*Table: Concise knowledge-base summary of congenital prothrombin deficiency, including genetics, phenotypes, diagnostics, treatment targets, models, ontology suggestions, and major evidence gaps.*

## 1. Disease information

### Definition and classification

Congenital prothrombin deficiency is an inherited defect of secondary hemostasis caused by deficient quantity or function of factor II. Two biochemical classes are recognized:

* **Type I, hypoprothrombinemia:** concordantly reduced factor-II activity and prothrombin antigen.
* **Type II, dysprothrombinemia:** reduced activity despite normal or near-normal antigen, indicating a dysfunctional circulating protein.

The distinction is laboratory-biochemical rather than a separate etiologic disease classification. Reviews often classify residual activity as **severe <5%**, **moderate 5–10%**, and **mild >10%**, but these thresholds are not prospectively validated diagnostic criteria. (lancellotti12009congenitalprothrombindeficiency pages 2-4)

### Identifiers and synonyms

* **MONDO:** MONDO:0013361.
* **Causal target:** F2; Ensembl **ENSG00000180210**; approved name “coagulation factor II, thrombin.” Open Targets identifies F2 as the sole associated target and ClinGen’s Hemostasis/Thrombosis Gene Curation Expert Panel classifies the gene–disease relationship as **Definitive** with autosomal-recessive inheritance. (OpenTargets Search: congenital prothrombin deficiency-F2)
* **Common names:** congenital prothrombin deficiency, congenital factor II deficiency, hereditary factor II deficiency, hypoprothrombinemia, and dysprothrombinemia.
* **Coding caveat:** exact current OMIM, Orphanet, MeSH, ICD-10, and ICD-11 identifiers were not verified in the retrieved source text. These should be imported directly from the respective controlled terminologies rather than inferred. Broad ICD coding commonly groups this disorder under “hereditary deficiency of other clotting factors,” but jurisdiction-specific verification is required.

This report synthesizes **aggregated disease-level resources**, reviews, and published patient cohorts/case studies. It is not derived from an individual EHR.

## 2. Etiology, risk, protection, and environment

### Primary cause

The disease is caused by germline **F2** variants that reduce prothrombin synthesis, secretion, stability, activation, substrate recognition, or catalytic/procoagulant performance. Homozygous and compound-heterozygous states generally cause clinically important deficiency; heterozygotes are usually asymptomatic or mildly affected. Complete absence appears lethal. (OpenTargets Search: congenital prothrombin deficiency-F2, lancellotti12009congenitalprothrombindeficiency pages 2-4, jayandharan2005moleculargeneticsof pages 6-7)

### Genetic risk factors

The principal risk factor is inheriting two pathogenic F2 alleles. Family history and parental consanguinity increase prior probability. Representative mechanisms include missense substitutions, in-frame deletions, frameshift alleles, splice abnormalities, and deletions. Examples include **Arg271Cys**, associated in one primary study with factor-II activity of 10.2% and severe bleeding; **Ala362Thr/Prothrombin Vellore 1**, adjacent to catalytic His363/Cys364; an **Arg−1Gln** processing-site substitution; **Arg457Gln** in reported Puerto Rican families; and Prothrombin Edmonton R−4Q in compound heterozygosity with a deletion. (jayandharan2005moleculargeneticsof pages 6-7, wong2006severeprothrombindeficiency pages 6-6)

The common **F2 G20210A** thrombophilia allele is mechanistically and clinically distinct: it raises prothrombin and predisposes to thrombosis rather than causing congenital factor-II deficiency. Antithrombin-resistant dysprothrombin variants can also produce thrombosis and should not automatically be grouped with bleeding-causing F2 loss of function.

### Environmental and gene–environment interactions

No toxin, infection, diet, occupation, or lifestyle exposure causes the congenital disorder. Environmental and physiological challenges modify bleeding expression: trauma, dental work, surgery, menstruation, pregnancy/childbirth, and anticoagulant or antiplatelet exposure can reveal otherwise mild disease. Vitamin-K deficiency, liver disease, disseminated intravascular coagulation, and vitamin-K antagonists lower factor II through acquired mechanisms and can amplify bleeding, but are differential diagnoses rather than causes of congenital F2 deficiency.

No validated protective genetic variant, modifier gene, diet, or lifestyle intervention prevents congenital deficiency. Practical protection consists of avoiding unnecessary trauma and drugs that impair hemostasis, correcting superimposed vitamin-K deficiency, and providing planned hemostatic cover. Evidence for epigenetic modifiers or reproducible gene–environment interactions is unavailable.

## 3. Phenotypes

The phenotype is a variable, lifelong bleeding diathesis. Severe disease may become evident neonatally or in childhood; milder disease may remain unrecognized until surgery, dental extraction, menarche, childbirth, or trauma. Bleeding is episodic rather than anatomically progressive. Individuals carrying the same variant may differ clinically. (lancellotti12009congenitalprothrombindeficiency pages 2-4)

Suggested HPO annotations include:

* easy bruising/ecchymosis — **HP:0000978**;
* hematoma — **HP:0001020**;
* epistaxis — **HP:0000421**;
* gingival/oral bleeding — **HP:0000225** or the closest current HPO bleeding term;
* menorrhagia/heavy menstrual bleeding — **HP:0000132**;
* prolonged postoperative bleeding — **HP:0004846**;
* gastrointestinal hemorrhage — **HP:0002239**;
* hemarthrosis — **HP:0005261**;
* muscle hemorrhage — **HP:0012233**, subject to ontology-version verification;
* intracranial hemorrhage — **HP:0002170**;
* prolonged PT and prolonged aPTT — use current HPO laboratory terms after terminology validation;
* reduced factor-II activity — a specific laboratory ontology concept may be preferable if HPO granularity is inadequate.

Recurrent mucocutaneous and gynecologic bleeding predominates in severe deficiency; hemarthrosis and muscle bleeding are less common than in severe hemophilia. Reviews also document gastrointestinal and intracranial hemorrhage and bleeding after surgery or dental extraction. Menorrhagia was estimated in approximately **20% of homozygous women** in one review, but reliable frequencies for most manifestations do not exist because patient numbers are extremely small. (castaman2017diagnosisandtreatment pages 10-11, lancellotti12009congenitalprothrombindeficiency pages 2-4)

Quality-of-life burdens plausibly include activity restriction, anxiety around procedures, iron deficiency from mucosal or menstrual loss, hospital attendance, and reproductive-health burden. However, no disease-specific EQ-5D, SF-36, PROMIS, or validated patient-reported-outcome dataset was identified.

## 4. Genetic and molecular information

### Gene and protein

**F2** lies on chromosome 11p11–q12 and encodes prothrombin, a liver-synthesized vitamin-K-dependent plasma glycoprotein. The precursor contains a signal peptide, propeptide, γ-carboxyglutamate (**Gla**) domain, two kringle domains, and a serine-protease region that becomes thrombin’s A and catalytic B chains. Factor Xa within the prothrombinase complex cleaves prothrombin at Arg273 and Arg322 to generate thrombin. (castaman2017diagnosisandtreatment pages 10-11, lancellotti12009congenitalprothrombindeficiency pages 2-4, grzegorski2020disruptionofthe pages 1-2)

Suggested annotations include **HGNC:3535** for F2, subject to direct HGNC verification; **GO:0007596** blood coagulation; **GO:0072378** blood coagulation, fibrin-clot formation; **GO:0006508** proteolysis; and plasma/extracellular-space cellular-component terms. Relevant chemicals include vitamin K and calcium ions; exact ChEBI identifiers should be checked against the current release.

### Variant interpretation

Disease-causing variants are germline. Current pathogenicity and population frequency must be curated variant by variant from ClinVar and gnomAD using a normalized transcript and HGVS expression; historical protein numbering is inconsistent because publications may count or exclude the signal peptide/propeptide. Consequently, synonymous names such as Ala362Thr versus mature/full-length numbering should not be merged without transcript-level reconciliation.

A 2005 Indian study identified four missense variants and one in-frame deletion, with none predicted to abolish protein completely. Functional/structural analysis suggested that Prothrombin Vellore 1 disrupts the conserved active-site environment and that Arg−1Gln impairs precursor processing. This illustrates why F2 variants may produce combined quantitative and qualitative abnormalities. (jayandharan2005moleculargeneticsof pages 6-7)

A recent 2023 study sequenced **12 southeastern Iranian patients** and reported an exon-7 substitution in three and an exon-14 frameshift caused by thymine insertion at positions 1760–1761 in one. The authors did not establish a statistically significant mutation–clinical-symptom relationship, emphasizing the limitations of very small cohorts. Publication: February 2023; DOI: https://doi.org/10.34172/cjmb.2023.10. (samarkhazan2023determinationoffactor pages 6-6)

No established chromosomal syndrome, recurrent aneuploidy, somatic F2 mechanism, repeat expansion, mitochondrial defect, or disease-specific epigenetic lesion is recognized. No consistently validated modifier gene or protective allele has been established.

## 5. Environmental information

Environmental exposures are not etiologic. The clinically relevant external factors are hemostatic stressors and iatrogenic modifiers: trauma, surgery, invasive dental procedures, childbirth, anticoagulants, antiplatelet drugs, and possibly NSAIDs. Liver dysfunction or poor vitamin-K availability may superimpose acquired hypoprothrombinemia. No infectious agent or zoonotic transmission applies.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic F2 mutation leads to** reduced synthesis/secretion/stability of prothrombin, or production of dysfunctional prothrombin.
2. **Reduced circulating functional prothrombin leads to** inadequate factor-Xa/prothrombinase-mediated conversion of prothrombin to thrombin.
3. **Reduced thrombin generation leads to** impaired fibrinogen cleavage and reduced fibrin formation.
4. **Reduced thrombin generation also leads to** weaker platelet activation, deficient amplification through factors V, VIII, and XI, and reduced factor-XIII activation.
5. **These defects result in** a weak, slowly forming, inadequately stabilized hemostatic clot.
6. **Hemostatic challenge then leads to** prolonged mucosal, soft-tissue, surgical, menstrual, gastrointestinal, joint, muscle, intracranial, or obstetric bleeding.
7. **Branch—quantitative disease:** defective transcription, processing, secretion, or stability **results in** low activity and low antigen.
8. **Branch—qualitative disease:** impaired activation, substrate recognition, or catalytic function **results in** low activity despite normal or near-normal antigen.
9. **Inferred survival constraint:** near-total loss of thrombin generation **leads to** developmental/perinatal hemorrhage and lethality, supported strongly by mouse and fish models but not directly demonstrable in humans. (lancellotti12009congenitalprothrombindeficiency pages 2-4, grzegorski2020disruptionofthe pages 4-6, grzegorski2020disruptionofthe pages 1-2)

This is the common coagulation pathway, not a canonical Wnt/MAPK/mTOR disease. Upstream processes are F2 expression, vitamin-K-dependent γ-carboxylation, secretion, and prothrombinase activation; downstream processes are thrombin-dependent fibrin formation, platelet activation, coagulation amplification, and clot stabilization.

A zebrafish kringle-1 mutation provides direct mechanistic evidence. A 14-bp genomic deletion caused abnormal splicing; **98.8%** of mutant reads used a cryptic acceptor to produce a 45-bp in-frame deletion, and homozygous embryos showed a **45%** transcript reduction. Engineered human Δ15 prothrombin had impaired secretion, approximately threefold slower activation, and reduced fibrinogen cleavage despite preserved activity against a small synthetic substrate. Thus, normal amidolytic activity does not guarantee physiological clotting function. (grzegorski2020disruptionofthe pages 4-6, grzegorski2020disruptionofthe pages 7-9)

Principal cells are hepatocytes, which synthesize prothrombin; platelets, which assemble prothrombinase and respond to thrombin; and vascular endothelial cells, whose injury initiates hemostasis. Suggested Cell Ontology terms are **CL:0000182 hepatocyte**, **CL:0000233 platelet**, and **CL:0000115 endothelial cell**. No primary inflammatory, autoimmune, apoptotic, energetic-metabolic, or infectious mechanism is established.

Disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omics signatures have not been established. No disease-focused CRISPR therapeutic screen was identified; genome editing has instead been used to create fish models.

## 7. Anatomical structures affected

The defect is systemic and circulatory rather than confined to one organ. Primary functional compartments are liver—site of synthesis—and blood/plasma—site of prothrombin circulation and coagulation. Suggested UBERON terms include liver **UBERON:0002107**, blood **UBERON:0000178**, blood vessel **UBERON:0001981**, and bone joint **UBERON:0000982**, subject to release verification.

Secondary injury may affect skin/subcutis, nasal and oral mucosa, uterus/endometrium, gastrointestinal tract, skeletal muscle, joints, and brain, depending on hemorrhage. There is no intrinsic lateralization; lesions may be unilateral, bilateral, or multifocal according to the bleeding event.

At subcellular level, synthesis and processing involve hepatocyte rough endoplasmic reticulum and Golgi; mature prothrombin acts in extracellular plasma and on phospholipid membrane surfaces. Relevant GO cellular-component terms include extracellular region/plasma and endoplasmic-reticulum/Golgi compartments.

## 8. Temporal development

The genetic lesion is congenital and lifelong. Severe surviving cases can manifest in the neonatal period or childhood; moderate/mild cases may first present in adolescence or adulthood after a challenge. The biochemical deficiency is generally stable and nonprogressive, while bleeding is episodic and exposure-dependent. There are no formal stages or spontaneous molecular remission. Apparent clinical remission means absence of bleeding between challenges, not correction of F2 deficiency.

Critical periods include delivery/neonatal life, childhood trauma, menarche and reproductive years, pregnancy/childbirth, and invasive procedures. Planned replacement before procedures is the principal intervention window.

## 9. Inheritance and population

Inheritance is predominantly **autosomal recessive**; ClinGen regards the F2 relationship as definitive. Biallelic disease affects males and females, and population prevalence is estimated near **1:2,000,000** for severe deficiency. Incidence per 100,000 person-years is not established. Consanguinity increases prevalence, and reported geographic clusters often reflect ascertainment or founder alleles rather than environmental endemicity. (OpenTargets Search: congenital prothrombin deficiency-F2, menegatti2020clinicalandlaboratory pages 1-2)

Expressivity is variable, including among individuals with the same mutation. Penetrance for severe biallelic loss is probably high but is not quantified; heterozygous penetrance is low and may be challenge-dependent. Anticipation is not expected. Germline mosaicism is theoretically possible but not established as a recurrent mechanism.

Arg457Gln has linked reported Puerto Rican kindreds, while variants described in India and southeastern Iran indicate regional/founder effects. Robust carrier frequencies by ancestry are unavailable. Under Hardy–Weinberg assumptions, a disease prevalence of 1/2,000,000 would imply an aggregate pathogenic-allele frequency near 1/1,414 and carrier frequency near 1/707, but this is only a rough model and should **not** replace empirical screening data.

## 10. Diagnostics

### Laboratory approach

1. Document personal and family bleeding history using a standardized bleeding-assessment tool where possible.
2. Obtain CBC/platelets, PT/INR, aPTT, fibrinogen, thrombin time as appropriate, liver tests, and medication/vitamin-K history.
3. Congenital factor-II deficiency usually prolongs **both PT and aPTT**, because F2 is in the common pathway.
4. Perform mixing studies if an inhibitor is possible; correction supports a deficiency.
5. Confirm reduced factor-II coagulant activity using a one-stage assay, with attention to reagent sensitivity and anticoagulant interference.
6. Measure prothrombin antigen: low activity plus low antigen supports hypoprothrombinemia; low activity with normal/near-normal antigen supports dysprothrombinemia.
7. Exclude acquired vitamin-K deficiency, warfarin effect, liver disease, DIC, massive transfusion/dilution, and acquired inhibitors.
8. Confirm with **F2 sequencing** and deletion/duplication analysis; test parents/relatives for segregation when feasible. (menegatti2020clinicalandlaboratory pages 1-2, lancellotti12009congenitalprothrombindeficiency pages 2-4)

Single-gene testing or a hereditary-bleeding-disorder panel is first line. WES/WGS can identify deep intronic, structural, or alternative diagnoses after negative targeted testing, but interpretation should remain anchored to activity/antigen results. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion tests are not routine. RNA studies can clarify suspected splice defects but are not established general diagnostics.

Imaging is complication-directed: head CT/MRI for suspected intracranial hemorrhage; ultrasound/CT for abdominal bleeding; musculoskeletal ultrasound or MRI for muscle/joint hemorrhage. Biopsy and electrophysiological testing have no routine diagnostic role.

### Differential diagnosis

Distinguish from deficiencies of factors V or X, combined vitamin-K-dependent factor deficiency, fibrinogen disorders, severe liver disease, vitamin-K deficiency/warfarin exposure, DIC, lupus anticoagulant or a specific inhibitor, and preanalytical coagulation-sample error. A normal factor-II antigen with low activity suggests dysprothrombinemia; proportionate reductions in factors II, VII, IX, and X suggest vitamin-K deficiency, warfarin effect, or combined vitamin-K-dependent factor deficiency rather than isolated F2 disease.

There is no population newborn-screening program. Appropriate strategies are cascade testing in known families, partner testing where relevant, prenatal diagnosis after familial-variant identification, and preimplantation genetic testing after counseling.

## 11. Outcome and prognosis

No reliable 5-year/10-year survival, mortality rate, or life-expectancy estimate exists. With recognition and access to replacement, many patients can achieve effective hemostasis and normal or near-normal life participation. Severe gastrointestinal, intracranial, neonatal, surgical, or obstetric hemorrhage can nevertheless cause death or permanent disability. Prognosis depends on residual functional activity, variant mechanism, previous bleeding phenotype, access to specialist treatment, and exposure to hemostatic challenges. (castaman2017diagnosisandtreatment pages 10-11, lancellotti12009congenitalprothrombindeficiency pages 2-4)

Potential morbidity includes anemia, joint or muscle damage after recurrent deep bleeding, neurological disability after intracranial hemorrhage, procedure avoidance, reproductive complications, and treatment-related thrombosis or fluid overload. No validated molecular prognostic biomarker exists beyond factor-II activity/antigen and personal bleeding history.

## 12. Treatment

### Replacement and adjunctive care

For clinically important bleeding or invasive procedures, expert reviews recommend **PCC 20–30 IU/kg**, repeated according to clinical response and measured factor-II level. Suggested targets are approximately **20–30%** for hemostasis and **30–40% for major surgery**. PCC is practical because it contains factor II, but also supplies factors VII, IX, and X; repeated dosing can accumulate long-half-life factors and create thrombotic risk. (castaman2017diagnosisandtreatment pages 10-11)

When PCC is unavailable, **FFP 15–20 mL/kg** can replace factor II, although larger volumes create fluid-overload and transfusion risks. A purified, generally available specific factor-II concentrate is lacking. (castaman2017diagnosisandtreatment pages 10-11)

Tranexamic acid or another antifibrinolytic can be considered for oral, nasal, menstrual, or dental bleeding, alongside local pressure, suturing, topical hemostatic materials, and dental planning. Antifibrinolytics do not correct the common-pathway defect and are inadequate alone for major bleeding. Iron replacement and menstrual suppression may be useful supportive interventions. Desmopressin is not a factor-II replacement and has no disease-specific mechanistic rationale.

Suggested NCIt intervention concepts include **Prothrombin Complex Concentrate**, **Fresh Frozen Plasma Transfusion**, **Tranexamic Acid**, **Antifibrinolytic Therapy**, and perioperative hemostatic management; exact NCIt codes require terminology lookup.

### Strategy by setting

* **Minor mucosal/dental bleeding:** local measures ± antifibrinolytic; add PCC/FFP based on severity and previous phenotype.
* **Major bleeding:** urgent PCC, monitor factor-II activity and clinical hemostasis; use FFP if PCC is unavailable.
* **Major surgery:** multidisciplinary plan, raise factor II to approximately 30–40%, repeat based on half-life, levels, wound hemostasis, and thrombosis risk.
* **Pregnancy/delivery:** individualized hematology–obstetric plan; assess activity and bleeding history, arrange replacement for delivery and postpartum risk, and avoid neuraxial procedures unless coagulation has been adequately corrected. Disease-specific pregnancy outcome data are sparse.
* **Long-term prophylaxis:** may be considered after recurrent severe bleeding, but evidence is limited to case experience; routine schedules are not standardized.

No approved gene, cell, RNA, or F2-targeted replacement therapy was identified. No disease-specific interventional ClinicalTrials.gov study was found in the tool search; retrieved studies concerned unrelated acquired coagulation settings. This means no relevant trial was identified, not proof that none exists globally.

Recent expert reviews conclude that although epidemiology, genetics, and diagnosis of rare bleeding disorders have advanced, management remains constrained by limited factor products and sparse trial evidence. Interest is growing in rebalancing agents that enhance coagulation or inhibit natural anticoagulant pathways, but this is not established therapy for congenital prothrombin deficiency.

## 13. Prevention

Primary prevention of the mutation is not possible through vaccination, diet, or environmental modification. Reproductive options include autosomal-recessive risk counseling, cascade carrier testing, prenatal diagnosis, and preimplantation genetic testing when familial variants are known. For two confirmed carriers, each pregnancy has a 25% probability of biallelic disease, 50% probability of carrier status, and 25% probability of inheriting neither familial allele.

Secondary prevention consists of early diagnosis in relatives, documenting the disorder in emergency records, and obtaining a baseline factor-II activity and individualized bleeding plan. Tertiary prevention includes planned perioperative replacement, early treatment of bleeding, avoidance of unnecessary aspirin/NSAIDs and anticoagulants, dental prevention, iron monitoring, and postpartum surveillance. Immunization has no disease-specific role, although standard vaccines should not be withheld; pressure after injections and an individualized route may be appropriate in severe bleeding disorders.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart specific to F2 deficiency was identified. Therefore, breed associations, VBO terms, veterinary prevalence, and zoonotic transmission are unavailable or not applicable. F2 orthologs and thrombin function are strongly conserved among vertebrates. Relevant taxa include **Mus musculus** (NCBI Taxon 10090), **Danio rerio** (7955), and **Oryzias latipes** (8090). This is a genetic coagulation disorder and has no zoonotic potential.

## 15. Model organisms

### Mouse

Homozygous F2 disruption causes embryonic hemorrhage, approximately **50% mortality by embryonic day 10.5**, and fatal neonatal/postnatal hemorrhage in survivors. The model establishes that complete prothrombin loss has developmental and survival consequences beyond ordinary provoked bleeding. Its limitation is early lethality, which restricts study of chronic adult disease. Transgenic prothrombin expression can rescue aspects of lethality. (grzegorski2020disruptionofthe pages 1-2, lancellotti12009congenitalprothrombindeficiency pages 7-8)

### Zebrafish

A targeted kringle-1-domain f2 lesion allows normal development into the mid-juvenile period but prevents occlusive arterial and venous thrombosis after endothelial injury. Internal hemorrhage begins around one month; **23 of 24 homozygotes died by 90 days**. Bleeding occurred around the head, jaw, muscle, fins, heart, and abdomen. The model separates relatively preserved thrombocyte attachment/primary hemostasis from severely defective thrombin-dependent secondary hemostasis and permits in-vivo study beyond stages lethal in mice. Species-specific blood pressure, aquatic development, and lack of birth trauma limit direct translation. Publication: March 2020; DOI: https://doi.org/10.1038/s41598-020-60840-7. (grzegorski2020disruptionofthe pages 4-6, grzegorski2020disruptionofthe pages 7-9, grzegorski2020disruptionofthe pages 1-2)

The paper’s abstract states that mutants “develop normally into the mid-juvenile stage but demonstrate complete mortality by 2 months of age primarily due to internal hemorrhage,” and that engineered human prothrombin showed “a severe reduction in secretion, thrombin generation, and fibrinogen cleavage.” These are model-organism and in-vitro human-protein findings, respectively, not clinical treatment evidence. (grzegorski2020disruptionofthe pages 1-2)

### Medaka

Genome-edited thrombin-deficient medaka remain viable and show markedly retarded blood coagulation, including an effect in heterozygotes. This model is experimentally convenient but does not reproduce the mammalian lethality or the full human genotype–phenotype spectrum.

## Recent developments and evidence assessment

The most disease-specific 2023 development located was sequencing of 12 Iranian patients, which added candidate exon-7 and exon-14 variants but lacked power for genotype–phenotype conclusions. Broader 2023–2024 literature has focused on perioperative management and the continuing therapeutic limitations across rare inherited bleeding disorders rather than on disease-specific trials. Consequently, older landmark molecular and animal studies remain essential to current understanding.

Evidence quality is highest for **F2 causality** and the central biochemical mechanism, supported by definitive ClinGen curation, human segregation/functional studies, and knockout models. Evidence is moderate for diagnostic activity/antigen classification and PCC/FFP practice, based on expert reviews and accumulated clinical experience. Evidence is low for phenotype frequencies, pregnancy outcomes, prophylaxis schedules, quality of life, survival, pharmacogenomics, and advanced therapies because prospective congenital-prothrombin-deficiency cohorts are absent. (OpenTargets Search: congenital prothrombin deficiency-F2, castaman2017diagnosisandtreatment pages 10-11, menegatti2020clinicalandlaboratory pages 1-2, jayandharan2005moleculargeneticsof pages 6-7)

## Key cited publications and URLs

* Lancellotti S, De Cristofaro R. **Congenital Prothrombin Deficiency.** *Seminars in Thrombosis and Hemostasis.* June 2009;35:367–381. DOI: https://doi.org/10.1055/s-0029-1225759. (lancellotti12009congenitalprothrombindeficiency pages 2-4)
* Castaman G, Linari S. **Diagnosis and Treatment of von Willebrand Disease and Rare Bleeding Disorders.** *Journal of Clinical Medicine.* April 2017;6:45. DOI: https://doi.org/10.3390/jcm6040045. (castaman2017diagnosisandtreatment pages 10-11)
* Menegatti M, Palla R. **Clinical and laboratory diagnosis of rare coagulation disorders.** *Thrombosis Research.* December 2020;196:603–608. DOI: https://doi.org/10.1016/j.thromres.2019.09.006. (menegatti2020clinicalandlaboratory pages 1-2)
* Jayandharan G et al. **Molecular genetics of hereditary prothrombin deficiency in Indian patients: identification of a novel Ala362→Thr mutation.** *Journal of Thrombosis and Haemostasis.* July 2005. DOI: https://doi.org/10.1111/j.1538-7836.2005.01402.x. (jayandharan2005moleculargeneticsof pages 6-7)
* Grzegorski SJ et al. **Disruption of the kringle 1 domain of prothrombin leads to late onset mortality in zebrafish.** *Scientific Reports.* March 2020;10:4049. DOI: https://doi.org/10.1038/s41598-020-60840-7. (grzegorski2020disruptionofthe pages 4-6, grzegorski2020disruptionofthe pages 1-2)
* Samarkhazan HS et al. **Determination of Factor II Codons Genotype in Southeastern Iranian Patients With Hereditary Deficiency of Factor II.** February 2023;10(2):61–66. DOI: https://doi.org/10.34172/cjmb.2023.10. (samarkhazan2023determinationoffactor pages 6-6)

PMIDs explicitly linked by the retrieved Open Targets evidence to historical F2 variant literature include **1421398, 1349838, 3567158, 3801671, 22028381, 6405779, 1354985, 7792730, 3771562, and 2719946**; exact mapping of each PMID to normalized HGVS variants should be verified before variant-level knowledge-base ingestion. (OpenTargets Search: congenital prothrombin deficiency-F2)

References

1. (castaman2017diagnosisandtreatment pages 10-11): Giancarlo Castaman and Silvia Linari. Diagnosis and treatment of von willebrand disease and rare bleeding disorders. Journal of Clinical Medicine, 6:45, Apr 2017. URL: https://doi.org/10.3390/jcm6040045, doi:10.3390/jcm6040045. This article has 122 citations.

2. (menegatti2020clinicalandlaboratory pages 1-2): Marzia Menegatti and Roberta Palla. Clinical and laboratory diagnosis of rare coagulation disorders (rcds). Thrombosis research, 196:603-608, Dec 2020. URL: https://doi.org/10.1016/j.thromres.2019.09.006, doi:10.1016/j.thromres.2019.09.006. This article has 28 citations and is from a peer-reviewed journal.

3. (lancellotti12009congenitalprothrombindeficiency pages 2-4): Stefano Lancellotti1 and Raimondo De Cristofaro1. Congenital prothrombin deficiency. Semin Thromb Hemost, 35:367-381, Jun 2009. URL: https://doi.org/10.1055/s-0029-1225759, doi:10.1055/s-0029-1225759. This article has 92 citations.

4. (OpenTargets Search: congenital prothrombin deficiency-F2): Open Targets Query (congenital prothrombin deficiency-F2, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (grzegorski2020disruptionofthe pages 1-2): Steven J. Grzegorski, Zhilian Hu, Yang Liu, Xinge Yu, Allison C. Ferguson, Hasam Madarati, Alexander P. Friedmann, Deepak Reyon, Paul Y. Kim, Colin A. Kretz, J. Keith Joung, and Jordan A. Shavit. Disruption of the kringle 1 domain of prothrombin leads to late onset mortality in zebrafish. Mar 2020. URL: https://doi.org/10.1038/s41598-020-60840-7, doi:10.1038/s41598-020-60840-7. This article has 29 citations and is from a peer-reviewed journal.

6. (jayandharan2005moleculargeneticsof pages 6-7): G. JAYANDHARAN, A. VISWABANDYA, S. BAIDYA, S.C. NAIR, R.V. SHAJI, M. CHANDY, and A. SRIVASTAVA. Molecular genetics of hereditary prothrombin deficiency in indian patients: identification of a novel ala362→thr (prothrombin vellore 1) mutation. Jul 2005. URL: https://doi.org/10.1111/j.1538-7836.2005.01402.x, doi:10.1111/j.1538-7836.2005.01402.x. This article has 29 citations and is from a peer-reviewed journal.

7. (wong2006severeprothrombindeficiency pages 6-6): A. Y. Wong, J. Hewitt, B. J. Clarke, David M. Hudson, Michael J. Krisinger, N. Dower, and Ross T. A. MacGillivray. Severe prothrombin deficiency caused by prothrombin‐edmonton (r‐4q) combined with a previously undetected deletion. Journal of Thrombosis and Haemostasis, 4:2623-2628, Dec 2006. URL: https://doi.org/10.1111/j.1538-7836.2006.02235.x, doi:10.1111/j.1538-7836.2006.02235.x. This article has 16 citations and is from a peer-reviewed journal.

8. (grzegorski2020disruptionofthe pages 4-6): Steven J. Grzegorski, Zhilian Hu, Yang Liu, Xinge Yu, Allison C. Ferguson, Hasam Madarati, Alexander P. Friedmann, Deepak Reyon, Paul Y. Kim, Colin A. Kretz, J. Keith Joung, and Jordan A. Shavit. Disruption of the kringle 1 domain of prothrombin leads to late onset mortality in zebrafish. Mar 2020. URL: https://doi.org/10.1038/s41598-020-60840-7, doi:10.1038/s41598-020-60840-7. This article has 29 citations and is from a peer-reviewed journal.

9. (samarkhazan2023determinationoffactor pages 6-6): Hamed Soleimani Samarkhazan, Shaban Alizadeh, Ziba Majidi, Zahra Kashani Khatib, and Majid Naderi. Determination of factor ii codons genotype in southeastern iranian patients with hereditary deficiency of factor ii. Crescent Journal of Medical and Biological Sciences, 10(2):61-66, Feb 2023. URL: https://doi.org/10.34172/cjmb.2023.10, doi:10.34172/cjmb.2023.10. This article has 3 citations.

10. (grzegorski2020disruptionofthe pages 7-9): Steven J. Grzegorski, Zhilian Hu, Yang Liu, Xinge Yu, Allison C. Ferguson, Hasam Madarati, Alexander P. Friedmann, Deepak Reyon, Paul Y. Kim, Colin A. Kretz, J. Keith Joung, and Jordan A. Shavit. Disruption of the kringle 1 domain of prothrombin leads to late onset mortality in zebrafish. Mar 2020. URL: https://doi.org/10.1038/s41598-020-60840-7, doi:10.1038/s41598-020-60840-7. This article has 29 citations and is from a peer-reviewed journal.

11. (lancellotti12009congenitalprothrombindeficiency pages 7-8): Stefano Lancellotti1 and Raimondo De Cristofaro1. Congenital prothrombin deficiency. Semin Thromb Hemost, 35:367-381, Jun 2009. URL: https://doi.org/10.1055/s-0029-1225759, doi:10.1055/s-0029-1225759. This article has 92 citations.

## Artifacts

- [Edison artifact artifact-00](Congenital_Prothrombin_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013361` (4 mentions) - the report calls it "if available"; MONDO calls it **congenital prothrombin deficiency**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001020` (2 mentions) - HP does not contain this term