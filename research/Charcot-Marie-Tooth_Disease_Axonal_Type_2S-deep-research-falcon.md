---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T19:02:28.438724'
end_time: '2026-09-05T19:11:11.047429'
duration_seconds: 522.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Charcot-Marie-Tooth Disease Axonal Type 2S
  mondo_id: MONDO:0014511
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 38
  verified: 36
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014511
    reported_labels:
    - if available
    ontology_label: Charcot-Marie-Tooth disease axonal type 2S
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0023055
    ontology_label: obsolete signal initiation by peptide hormone
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Charcot-Marie-Tooth_Disease_Axonal_Type_2S-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease Axonal Type 2S
- **MONDO ID:** MONDO:0014511 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Axonal Type 2S** covering all of the
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
- **Disease Name:** Charcot-Marie-Tooth Disease Axonal Type 2S
- **MONDO ID:** MONDO:0014511 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Axonal Type 2S** covering all of the
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


# Charcot–Marie–Tooth Disease, Axonal Type 2S (CMT2S)

## Executive summary

Charcot–Marie–Tooth disease type 2S (CMT2S) is an ultra-rare, autosomal-recessive, hereditary motor-and-sensory **axonal neuropathy** caused by biallelic pathogenic variants in **IGHMBP2**. It usually begins in childhood with length-dependent distal weakness and wasting, sensory loss, areflexia, gait impairment, and foot deformity, and then progresses slowly proximally. Severe early diaphragmatic paralysis favors the allelic disorder spinal muscular atrophy with respiratory distress type 1 (SMARD1), but the two conditions form an overlapping IGHMBP2-related spectrum rather than an absolute binary. The foundational CMT2S association is Cottenie et al., *American Journal of Human Genetics*, published 6 November 2014, PMID **25439726**, DOI [10.1016/j.ajhg.2014.10.002](https://doi.org/10.1016/j.ajhg.2014.10.002). (tian2023exploringtherelationship pages 1-2, NCT05152823 chunk 1)

The strongest recent advances are: dedicated CMT2S knock-in/deletion mouse models in 2023; systematic genotype–phenotype synthesis in 2023; new human IGHMBP2 cases in 2024; RNA-seq/Ribo-seq evidence in 2024 linking IGHMBP2 loss to translational suppression and chronic integrated-stress-response activation; and an ongoing phase I/IIa intrathecal AAV9–IGHMBP2 trial, NCT05152823. No disease-modifying treatment has yet been established as clinically effective. (tran2024anovelighmbp2 pages 5-6, tian2023exploringtherelationship pages 1-2, NCT05152823 chunk 1, park2024ighmbp2deletionsuppresses pages 1-2, martin2023clinicallyrelevantmouse pages 1-2)

The following evidence map distinguishes CMT2S-specific findings from evidence extrapolated from broader CMT or SMARD1.

| Domain | Best-supported finding | Evidence type | Key quantitative detail | Source/year/DOI or PMID |
|---|---|---|---|---|
| Disease identity | Charcot–Marie–Tooth disease axonal type 2S (CMT2S) is a rare hereditary motor-and-sensory axonal neuropathy; identifiers include **OMIM 616155** and **MONDO:0014511**. | Aggregated disease-level resource plus human genetics | Open Targets associates MONDO:0014511 with one causal target, **IGHMBP2**. | Open Targets/MONDO; Cottenie et al., 2014, PMID: **25439726**, DOI: [10.1016/j.ajhg.2014.10.002](https://doi.org/10.1016/j.ajhg.2014.10.002) (OpenTargets Search: Charcot-Marie-Tooth disease type 2S-IGHMBP2, NCT05152823 chunk 1) |
| Etiology and inheritance | CMT2S is caused by **biallelic germline pathogenic variants in IGHMBP2** and follows autosomal-recessive inheritance; heterozygous carriers are generally unaffected. | CMT2S-specific human genetics, supported by mouse segregation | Vietnamese patients were homozygous or compound heterozygous; heterozygous E365del mice lacked the homozygous phenotype. | Tran et al., 2024, DOI: [10.3389/fped.2024.1165492](https://doi.org/10.3389/fped.2024.1165492); Martin et al., 2023, DOI: [10.1093/hmg/ddac283](https://doi.org/10.1093/hmg/ddac283) (tran2024anovelighmbp2 pages 5-6, martin2023clinicallyrelevantmouse pages 2-4) |
| Allelic spectrum | Missense, nonsense/truncating, splice-altering, frameshift, and small-deletion variants are reported. CMT2S and SMARD1 form an allelic spectrum, and identical genotypes can yield different phenotypes; complete loss of function is more strongly associated with SMARD1. | Human cases plus systematic review | The 2023 review included **52 articles**, identified **6 hotspot variants**, and found that two truncating variants in trans were associated with SMARD1. | Tian et al., 2023, DOI: [10.3389/fnins.2023.1252075](https://doi.org/10.3389/fnins.2023.1252075) (tian2023exploringtherelationship pages 8-9, tian2023exploringtherelationship pages 1-2) |
| Core phenotype | Typical CMT2S involves juvenile/early-onset, slowly progressive, length-dependent distal weakness and wasting, distal sensory loss, gait impairment, and reduced or absent tendon reflexes; weakness may spread proximally. Respiratory failure is usually absent, unlike SMARD1, although rare later diaphragmatic weakness has been reported. | CMT2S-specific human clinical evidence | Reported onset is commonly after age **1 year** and often before age **10 years**; frequencies cannot be estimated reliably from the small published cohorts. | Tran et al., 2024, DOI: [10.3389/fped.2024.1165492](https://doi.org/10.3389/fped.2024.1165492); Tian et al., 2023, DOI: [10.3389/fnins.2023.1252075](https://doi.org/10.3389/fnins.2023.1252075) (tran2024anovelighmbp2 pages 5-6, tian2023exploringtherelationship pages 8-9, tian2023exploringtherelationship pages 1-2) |
| Electrophysiology | CMT2S is primarily an **axonal** neuropathy: motor and sensory response amplitudes are reduced, while conduction velocities are relatively preserved or normal unless axon loss is advanced. | CMT2S-specific human evidence and concordant mouse evidence | The E365del mouse had progressive axon loss without altered conduction velocity; Y918C mice also developed motor-and-sensory axonal degeneration but showed conduction-velocity effects. | Tran et al., 2024, DOI: [10.3389/fped.2024.1165492](https://doi.org/10.3389/fped.2024.1165492); Martin et al., 2023, DOI: [10.1093/hmg/ddac283](https://doi.org/10.1093/hmg/ddac283) (tran2024anovelighmbp2 pages 5-6, martin2023clinicallyrelevantmouse pages 1-2) |
| Epidemiology | CMT2S is ultra-rare; no robust population-based incidence or prevalence study is available. The often-cited general CMT prevalence of approximately 1 in 2,500 must not be assigned to CMT2S. | Review estimate; limited subtype-specific evidence | Estimated CMT2S prevalence: **<1 per 1,000,000 worldwide**. | Smieszek et al., 2025, DOI: [10.1016/j.omtn.2025.102479](https://doi.org/10.1016/j.omtn.2025.102479) (smieszek2025potentialasobasedpersonalized pages 1-2) |
| 2023 disease models | CRISPR-generated homozygous **Ighmbp2 p.Glu365del** and human-allele knock-in **p.Tyr918Cys** mice are the first dedicated CMT2S mouse models; both reproduce progressive motor-and-sensory axonal degeneration and motor deficits. | CMT2S-specific mouse models | E365del mice showed about **50% sensory-axon loss** and **31% motor-axon loss** by 20 weeks; motor deficits appeared by 6 weeks and mechanical allodynia by 12 weeks, without reduced survival. | Martin et al., 2023, DOI: [10.1093/hmg/ddac283](https://doi.org/10.1093/hmg/ddac283) (martin2023clinicallyrelevantmouse pages 1-2, martin2023clinicallyrelevantmouse pages 2-4) |
| 2024 molecular mechanism | IGHMBP2 is a cytoplasmic SF1 DNA/RNA helicase associated with ribosomes, pre-rRNA-processing factors, elongation factors, and tRNA species. Experimental deletion reduces global translation and chronically activates the integrated stress response, including ATF4 upregulation; relevance to patient neurons remains inferential. | Human K562-cell CRISPR knockout; not direct CMT2S tissue evidence | Full deletion slowed proliferation, modestly suppressed translation, altered the transcriptome/translatome, and produced reversible basal ISR activation; a **122-gene ATF4 target set** did not reach significant enrichment. | Park et al., published **21 May 2024**, DOI: [10.26508/lsa.202302554](https://doi.org/10.26508/lsa.202302554) (park2024ighmbp2deletionsuppresses pages 1-2, park2024ighmbp2deletionsuppresses pages 8-9) |
| Current management | No approved disease-modifying therapy is established for CMT2S. Current care is extrapolated mainly from broader CMT practice: individualized physical and occupational therapy, stretching and moderate exercise, ankle–foot orthoses, mobility aids, pain management, and orthopedic correction of fixed deformity. | Broader-CMT clinical evidence; not CMT2S-specific | A 2024 real-practice study of **37** mixed-CMT patients found short-term improvement after 3 weeks of intensive rehabilitation, but benefits were lost by 12 months; an AFO meta-analysis included **15 studies**, with pooled effects not statistically significant. | Ferraro et al., 2024, DOI: [10.1007/s10072-023-06998-0](https://doi.org/10.1007/s10072-023-06998-0); Kim et al., 2024, DOI: [10.1002/jfa2.70003](https://doi.org/10.1002/jfa2.70003) |
| Clinical gene therapy | **NCT05152823** is evaluating a single intrathecal dose of an AAV9 vector carrying human IGHMBP2 in genetically confirmed IGHMBP2-related disease, including CMT2S. It is experimental and has no posted efficacy result in the cited record. | CMT2S/SMARD1 human interventional trial | Open-label, single-group **phase I/IIa** study; estimated **10 participants**, ages **2 months–14 years**; primary safety follow-up **3 years**; status verified September 2025: enrolling by invitation. | ClinicalTrials.gov, first posted **10 December 2021**, [NCT05152823](https://clinicaltrials.gov/study/NCT05152823) (NCT05152823 chunk 1) |
| Translational qualification | AAV9-IGHMBP2 rescue in SMARD1 mice and patient-derived IGHMBP2-disorder neurons supports gene-replacement plausibility, but SMARD1-model efficacy cannot be treated as demonstrated CMT2S clinical benefit. | SMARD1 mouse and mixed SMARD1/CMT2S in-vitro extrapolation | Patient-derived induced neurons showed shortened neurites and variable improvement after IGHMBP2 restoration; clinical benefit and durability remain unknown. | Sierra-Delgado et al., 2023, DOI: [10.3390/biology12060867](https://doi.org/10.3390/biology12060867); NCT05152823 (NCT05152823 chunk 2, NCT05152823 chunk 1) |


*Table: Compact evidence map distinguishing disease-specific human and mouse findings from broader CMT care evidence and SMARD1-based mechanistic extrapolation. It highlights the strongest quantitative findings and the current experimental status of IGHMBP2 gene therapy.*

## 1. Disease information

### Definition and identifiers

CMT2S is a genetic peripheral neuropathy characterized pathologically and electrophysiologically by degeneration/loss of motor and sensory axons rather than primary demyelination. Open Targets maps **MONDO:0014511** (“Charcot-Marie-Tooth disease axonal type 2S”) to the single established target **IGHMBP2** (Ensembl ENSG00000132740), supported by the foundational human-genetics publication PMID 25439726. (OpenTargets Search: Charcot-Marie-Tooth disease type 2S-IGHMBP2)

* **MONDO:** MONDO:0014511.
* **OMIM disease:** **616155**.
* **OMIM gene:** **IGHMBP2, 600502**.
* **Gene:** IGHMBP2, immunoglobulin mu DNA-binding protein 2; historical protein name SIP1.
* **Common names:** Charcot–Marie–Tooth disease type 2S; CMT2S; Charcot–Marie–Tooth disease, axonal, type 2S; autosomal-recessive CMT2S; IGHMBP2-related axonal neuropathy; hereditary motor and sensory neuropathy due to IGHMBP2.
* **Orphanet:** A CMT2S-specific ORPHA number was not verified in the retrieved evidence; it should not be inferred from SMARD1’s ORPHA:98920.
* **ICD-10-CM:** No subtype-specific code was verified; CMT is generally represented under G60.0, hereditary motor and sensory neuropathy.
* **ICD-11/MeSH:** No CMT2S-specific identifier was verified. The trial’s indexed MeSH concept concerns the related SMARD1 phenotype, not CMT2S specifically. (NCT05152823 chunk 1)

The report synthesizes **aggregated disease resources**, published case series/families, experimental models, and a trial registry. It is not derived from an individual EHR. Because cohorts are very small, most phenotype frequencies cannot be generalized reliably.

## 2. Etiology

### Causal and genetic risk factors

The necessary causal factor is normally **two pathogenic germline IGHMBP2 alleles**, either homozygous or compound heterozygous. The 2024 Vietnamese study evaluated eight patients with IGHMBP2-related disease: three were homozygous and five compound heterozygous, while parents were carriers. Reported variants included c.1235+3A>G, c.1334A>C (p.His445Pro), c.1574T>C (p.Leu525Pro), c.1813C>T (p.Arg605Ter), and c.2362C>T (p.Arg788Ter). (tran2024anovelighmbp2 pages 5-6)

Consanguinity increases the probability that both parents carry the same rare allele but is not mechanistically required. Family history may be absent because of recessive inheritance. Heterozygous carriers are generally asymptomatic; concordantly, heterozygous E365del mice did not show the homozygous neuropathy phenotype. (martin2023clinicallyrelevantmouse pages 2-4)

### Modifiers, protective factors, and gene–environment interaction

Residual IGHMBP2 abundance/function appears important: partial loss is more often compatible with CMT2S, whereas profound or complete loss—particularly two truncating alleles in trans—is strongly associated with SMARD1. A 2023 systematic review searched through 1 April 2023, included **52 articles**, found six hotspot variants, and reported that truncating variants in trans were all associated with SMARD1. This is a probabilistic relationship, not a deterministic rule. (tian2023exploringtherelationship pages 1-2)

Identical variants can nevertheless yield markedly different outcomes. In the 2024 Vietnamese series, individuals with c.1235+3A>G/c.1334A>C had either fatal infantile SMARD1 or CMT2S without respiratory distress, supporting modifier genes, expression differences, or other unidentified factors. (tran2024anovelighmbp2 pages 5-6)

ABT1 and linked tRNA-Tyr genes modify disease severity in mice, but no clinically validated human modifier or protective allele is established. No reproducible environmental risk or protective factor, infection, diet, smoking effect, toxin, occupational exposure, or formal gene–environment interaction has been demonstrated for CMT2S. Avoidance of neurotoxic exposures is prudent clinical practice but does not prevent the inherited molecular lesion. (park2024ighmbp2deletionsuppresses pages 1-2, park2024ighmbp2deletionsuppresses pages 8-9)

## 3. Phenotypes

The core phenotype is chronic, length-dependent motor-and-sensory neuropathy. Onset has often been reported after age one and before age ten, although both earlier and later presentations occur. Severity varies from ambulant childhood disease to severe disability; reliable percentages are unavailable. (tran2024anovelighmbp2 pages 5-6, tian2023exploringtherelationship pages 1-2)

| Phenotype | Characteristics and suggested HPO annotation |
|---|---|
| Distal limb weakness | Usually lower limbs first; slowly progressive, potentially spreading proximally. **HP:0002460, Distal muscle weakness**; **HP:0009055, Generalized distal muscle weakness**. |
| Distal muscle atrophy | Feet/lower legs and later hands; neurogenic. **HP:0008944, Distal amyotrophy**. |
| Sensory loss | Length-dependent distal loss, potentially spreading proximally. **HP:0000763, Sensory neuropathy**; **HP:0002936, Distal sensory impairment**. |
| Reduced/absent reflexes | Common clinical sign. **HP:0001284, Areflexia**; **HP:0001315, Reduced tendon reflexes**. |
| Gait disorder/foot drop | Tripping, falls, steppage gait, impaired running or stair climbing. **HP:0001288, Gait disturbance**; **HP:0003376, Steppage gait**; **HP:0009536, Foot drop**. |
| Foot deformity | Pes cavus/cavovarus and contracture may emerge with chronic muscle imbalance. **HP:0001761, Pes cavus**; **HP:0008110, Equinovarus deformity**. |
| Scoliosis | Variable and sometimes severe. **HP:0002650, Scoliosis**. |
| Axonal neuropathy | Low compound muscle and sensory action-potential amplitudes with relatively preserved conduction velocity. **HP:0003477, Peripheral axonal neuropathy**. |
| Respiratory involvement | Usually absent in classic CMT2S; severe infantile diaphragmatic paralysis points to SMARD1. Rare late diaphragmatic weakness means respiratory surveillance should be symptom-driven. **HP:0002791, Hypoventilation** and **HP:0009113, Diaphragmatic paralysis** only when documented. |

The disease impairs walking, balance, endurance, hand function, schooling/work, independence, and social participation; falls, fatigue, pain, and orthotic or mobility-aid needs can reduce quality of life. No CMT2S-specific EQ-5D, SF-36, PROMIS, or phenotype-frequency dataset was found. A detailed 2025 patient report illustrates severity but not population frequency: foot inversion began at approximately three months, weakness became proximal, and by 11 years the patient had recurrent falls and impaired ambulation. (smieszek2025potentialasobasedpersonalized pages 1-2)

Behavioral or primary psychiatric changes are not defining. Intellectual disability should prompt consideration of an expanded phenotype, a second diagnosis, or another neuropathy gene rather than automatic assignment to CMT2S.

## 4. Genetic and molecular information

### Gene and protein

**IGHMBP2** lies on chromosome 11q13 and contains 15 exons. It encodes a 993-amino-acid, ubiquitously expressed superfamily-1 ATP-dependent DNA/RNA helicase that unwinds GC-rich duplex RNA in the 5′→3′ direction. It contains ATPase/helicase and zinc-finger-related functional regions and associates predominantly with cytoplasmic translation machinery. (tran2024anovelighmbp2 pages 5-6, tian2023exploringtherelationship pages 1-2, park2024ighmbp2deletionsuppresses pages 1-2, martin2023clinicallyrelevantmouse pages 1-2)

Suggested annotations include **GO:0004386 helicase activity**, **GO:0003723 RNA binding**, **GO:0005524 ATP binding**, **GO:0034061 DNA helicase activity**, **GO:0006412 translation**, and **GO:0008380 RNA splicing**. Exact HGNC numeric ID was not verified in the retrieved evidence and should be sourced directly from HGNC before database loading.

### Pathogenic variants

Missense, nonsense, frameshift, splice-site, small in-frame deletion, and larger disruptive variants have been reported. The foundational paper’s title provides the exact abstract-level statement: **“Truncating and missense mutations in IGHMBP2 cause Charcot-Marie Tooth disease type 2.”** (tian2023exploringtherelationship pages 8-9, NCT05152823 chunk 1)

Variants are germline, not somatic. The predominant mechanism is loss or reduction of protein function through altered helicase activity, protein instability, abnormal splicing, frameshift, or nonsense-mediated decay. A deep intronic/cryptic splice variant can create an aberrant acceptor, disrupt the reading frame, and trigger nonsense-mediated decay. (smieszek2025potentialasobasedpersonalized pages 1-2)

Variant-level ACMG classification and gnomAD/TOPMed frequencies must be checked individually using the precise transcript and genome build. Ultra-rarity and segregation support pathogenicity but do not alone establish it. No recurrent chromosomal aneuploidy, translocation, inversion, or copy-number mechanism is established as characteristic. No disease-specific epigenetic signature is validated.

## 5. Environmental information

CMT2S is a monogenic inherited disease. No infectious agent, radiation exposure, pollutant, diet, alcohol use, smoking pattern, or occupational exposure is known to cause it. Environmental and lifestyle variables may alter function or complications—exercise conditioning, falls, obesity, orthopedic strain, and exposure to neurotoxic medicines—but are not established causes. No quantitative CMT2S-specific exposure study was found.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic IGHMBP2 variants lead to** reduced abundance or function of ATP-dependent IGHMBP2 helicase.
2. **Reduced IGHMBP2 function leads to** disturbed RNA metabolism, including translation-associated, pre-rRNA/tRNA-related, mRNA-processing, and potentially THO-complex-dependent mRNA-export functions; the relative contribution of each pathway in human CMT2S remains incompletely resolved. (park2024ighmbp2deletionsuppresses pages 1-2, park2024ighmbp2deletionsuppresses pages 8-9)
3. **Translation/RNA-homeostasis disturbance leads to** modest global translational suppression and chronic ATF4-associated integrated stress response in IGHMBP2-knockout human cells; extrapolation to patient peripheral neurons is currently inferred. (park2024ighmbp2deletionsuppresses pages 1-2)
4. **Chronic neuronal RNA/proteostasis stress is inferred to lead to** impaired axonal maintenance and local protein synthesis, especially in long peripheral motor and sensory neurons.
5. **Impaired axonal maintenance leads to** progressive length-dependent motor- and sensory-axon degeneration; dedicated mouse models directly demonstrate this step. (martin2023clinicallyrelevantmouse pages 1-2, martin2023clinicallyrelevantmouse pages 2-4)
6. **Motor-axon and neuromuscular-junction loss leads to** denervation, distal muscle wasting, weakness, foot imbalance/deformity, and gait impairment.
7. **Sensory-axon loss leads to** distal sensory impairment and altered nociception; E365del mice also show mechanical allodynia. (martin2023clinicallyrelevantmouse pages 2-4)
8. **Branch—when residual IGHMBP2 function is extremely low, the lesion more often leads to** spinal α-motor-neuron loss and diaphragmatic paralysis/SMARD1 rather than classic CMT2S; genotype alone does not perfectly determine this branch. (tran2024anovelighmbp2 pages 5-6, tian2023exploringtherelationship pages 1-2)

### Cellular and molecular detail

The 2024 human K562 CRISPR study used polysome profiling, nascent-protein synthesis, RNA-seq, Ribo-seq, and ATF4 reporters. Full deletion slowed proliferation, modestly reduced global translation, changed the transcriptome/translatome, and produced basal chronic ISR activation. Its exact abstract statement is: **“IGHMBP2 knockout cells demonstrate basal, chronic ISR activation.”** The response was low-grade and reversible; CHOP induction was not detected, suggesting a pro-survival rather than overtly apoptotic program. A 122-gene ATF4 set did not reach significant enrichment, emphasizing that effect sizes were modest. (park2024ighmbp2deletionsuppresses pages 1-2, park2024ighmbp2deletionsuppresses pages 8-9)

Suggested processes/cells:

* **GO:** translation (GO:0006412), response to endoplasmic-reticulum stress (GO:0034976), integrated stress response, axon maintenance (GO:0023055), axon degeneration (GO:0030516), neuromuscular-junction development (GO:0007528), peripheral nervous system development (GO:0007422).
* **CL:** motor neuron (**CL:0000100**), sensory neuron (**CL:0000101**), alpha motor neuron where available, skeletal muscle cell/myocyte (**CL:0000187**), Schwann cell (**CL:0002573**). Axons—not Schwann-cell myelin—are the primary lesion in CMT2S.

No validated CMT2S-specific metabolomic, lipidomic, methylomic, spatial-transcriptomic, or single-cell patient-tissue signature was found. RNA-seq/Ribo-seq evidence currently comes from engineered cells rather than affected human nerves. (park2024ighmbp2deletionsuppresses pages 1-2)

## 7. Anatomical structures affected

The principal system is the **peripheral nervous system**, especially long motor and sensory axons to distal limbs, with secondary denervation of skeletal muscle and neuromuscular junctions. The process is generally bilateral and approximately symmetric, though severity may differ between sides.

Suggested locations are peripheral nerve (**UBERON:0000010**), spinal nerve, lower-limb peripheral nerve, upper-limb peripheral nerve, skeletal muscle (**UBERON:0001134**), neuromuscular junction, foot, lower leg, and hand. Relevant subcellular compartments include cytoplasm (**GO:0005737**), ribosome (**GO:0005840**), axon (**GO:0030424**), and presynaptic/neuromuscular-junction compartments. The diaphragm is usually spared in classic CMT2S but can be involved in the broader IGHMBP2 spectrum.

## 8. Temporal development

Onset is usually insidious and pediatric/juvenile, commonly after infancy and often before ten years. Early manifestations include delayed or abnormal walking, foot inversion/deformity, tripping, falls, distal weakness, and absent reflexes. Disease is chronic and generally slowly progressive, with distal-to-proximal spread and possible later hand involvement. (tran2024anovelighmbp2 pages 5-6, tian2023exploringtherelationship pages 1-2)

There are no validated disease stages. A practical clinical framework is: early gait/foot weakness; intermediate established distal weakness, sensory loss, and deformity; and advanced proximal spread, hand involvement, scoliosis, and need for mobility assistance. Remission is not expected. The critical therapeutic window is likely before irreversible axon and motor-unit loss, but this remains inferred rather than proven in humans.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two confirmed heterozygous parents, each pregnancy has a 25% probability of an affected child, 50% of a heterozygous carrier, and 25% of an unaffected non-carrier, assuming conventional Mendelian segregation.

Penetrance for appropriately classified biallelic pathogenic variants appears high, but phenotype and age of onset are variable. Expressivity spans CMT2S, intermediate presentations, and SMARD1. Anticipation is not established. Germline mosaicism has not been quantified. Founder effects may occur in individual consanguineous families, but no globally dominant founder allele or reliable carrier frequency is known.

A later review estimates CMT2S prevalence at **<1 per 1,000,000 worldwide**; no population-based incidence estimate exists. General CMT prevalence—often quoted around 1:2,500—must not be applied to this ultra-rare subtype. Both sexes are affected. Reports span European, Asian, Middle Eastern, and other ancestries, without a demonstrated sex or ethnic predominance. (smieszek2025potentialasobasedpersonalized pages 1-2, martin2023clinicallyrelevantmouse pages 1-2)

## 10. Diagnostics

### Clinical and electrophysiologic evaluation

Diagnosis begins with history, three-generation pedigree, neurologic examination, foot/spine assessment, functional measures, and nerve-conduction studies/EMG. The characteristic electrophysiology is reduced motor and sensory response amplitudes with relatively normal or mildly reduced conduction velocity, supporting axonal rather than primary demyelinating disease. (tran2024anovelighmbp2 pages 5-6, martin2023clinicallyrelevantmouse pages 1-2)

EMG may show chronic neurogenic denervation/reinnervation. Imaging is not diagnostic but may assess spine/foot deformity or alternative causes. Nerve or muscle biopsy is usually unnecessary after molecular confirmation and would be expected to show axonal loss and neurogenic muscle change rather than a unique CMT2S marker.

### Genetic testing strategy

1. Use a comprehensive inherited-neuropathy/CMT panel that includes **IGHMBP2**, or exome/genome sequencing where phenotype is atypical or panel testing is negative.
2. Confirm two variants, phase them in trans through parental testing, and classify them under ACMG/AMP criteria.
3. Use deletion/duplication analysis if sequencing detects only one allele.
4. Use RNA studies when a synonymous, intronic, or suspected splice variant remains unresolved; WGS can identify deep intronic or structural variants missed by WES.
5. Test relatives for cascade screening only after the familial variants are established.

WES identified biallelic variants in the Vietnamese cohort, while prior WGS identified a cryptic splice-site CMT phenotype, demonstrating complementary utility. (tran2024anovelighmbp2 pages 5-6, tian2023exploringtherelationship pages 8-9)

CMA, karyotyping, FISH, mitochondrial-DNA analysis, and repeat-expansion testing are not first-line for a molecularly typical CMT2S case, but may be appropriate if the broader phenotype suggests another diagnosis.

### Differential diagnosis

Important alternatives include other axonal CMT2 forms, hereditary motor neuropathy, hereditary sensory neuropathy, 5q SMA, SMARD1, distal SMA, Friedreich ataxia, hereditary spastic paraplegia, metabolic neuropathy, and acquired inflammatory/toxic neuropathy. Early respiratory failure or diaphragm paralysis strongly favors SMARD1; prominent demyelinating slowing favors CMT1; acquired rapid progression, conduction block, or inflammatory markers warrant evaluation for CIDP/GBS.

There is no newborn biochemical screen or validated circulating biomarker. Prenatal and preimplantation testing are technically possible when familial variants are known.

## 11. Outcome and prognosis

Classic CMT2S is generally less acutely life-threatening than SMARD1, and respiratory failure is usually absent. Nevertheless, progressive weakness can cause substantial lifelong disability, falls, loss of independent ambulation, scoliosis, contractures, chronic pain, fatigue, and reduced participation. No reliable CMT2S-specific survival curve, mortality rate, five- or ten-year survival statistic, or validated prognostic biomarker exists. (tian2023exploringtherelationship pages 1-2)

Residual IGHMBP2 function, variant combination, age at onset, rate of motor decline, scoliosis, and respiratory involvement are plausible prognostic factors, but genotype–phenotype prediction remains imprecise. Rare later diaphragmatic weakness justifies pulmonary assessment when orthopnea, weak cough, sleep-disordered breathing, or declining vital capacity occurs. (tian2023exploringtherelationship pages 8-9)

## 12. Treatment

### Current clinical management

There is no established curative or approved CMT2S-specific pharmacotherapy. Care is multidisciplinary and mainly extrapolated from broader CMT practice:

* individualized physiotherapy with stretching, balance, aerobic conditioning, and non-excessive strengthening;
* occupational therapy and energy-conservation/adaptive strategies;
* custom ankle–foot orthoses, footwear, canes, walkers, or wheelchairs;
* treatment of neuropathic or musculoskeletal pain;
* surveillance and management of contractures, cavovarus feet, scoliosis, falls, and respiratory symptoms;
* orthopedic tendon transfer, osteotomy, fusion, or scoliosis surgery for function-limiting fixed deformity after specialist assessment.

Suggested NCIt intervention concepts include **Physical Therapy**, **Occupational Therapy**, **Orthotic Device**, **Pain Management**, **Orthopedic Surgery**, **Genetic Counseling**, and **Gene Therapy**; NCIt identifiers should be verified against the current release before ingestion.

Broader-CMT real-world evidence remains modest. A 2024 retrospective study included **37** mild/moderate CMT patients—28 demyelinating, eight axonal, one mixed—and used 2–4 hours/day, five days/week for three weeks. Outcomes improved immediately but gains were lost by 12 months, so the results are not CMT2S-specific or evidence of disease modification. A 2024 AFO review included 15 studies; pooled gait effects were small-to-moderate but statistically non-significant because of small, heterogeneous samples, supporting individualized fitting rather than a universal device. 

### Experimental gene therapy

ClinicalTrials.gov **NCT05152823**, “Phase I/IIa Intrathecal Gene Delivery Clinical Trial for IGHMBP2-Related Diseases,” is an open-label, single-group study of one intrathecal dose of AAV9 carrying IGHMBP2. It includes genetically confirmed SMARD1 or CMT2S, requires two pathogenic variants, enrolls ages two months to 14 years, and has an estimated sample of ten. The primary endpoint is unacceptable grade III-or-higher treatment-related toxicity over three years; functional endpoints include GRO, 100-m timed testing, and RULM according to age/ambulatory status. The study began 4 November 2021; the record was verified September 2025 as enrolling by invitation, with estimated primary completion July 2028. No efficacy result was posted in the retrieved record. (NCT05152823 chunk 1)

Patient-derived induced neurons exhibit shortened neurites and variable improvement after AAV9-mediated IGHMBP2 restoration, supporting biological plausibility but not clinical efficacy. A later splice-correction ASO study reported >50% protein increase and improved in-vitro NMJ behavior for one personalized variant; this is mutation-specific preclinical evidence, not a general CMT2S treatment. (smieszek2025potentialasobasedpersonalized pages 1-2)

No established CMT2S pharmacogenomic guidance, cell therapy, immunotherapy, or combination regimen exists.

## 13. Prevention

Primary prevention by lifestyle change or vaccination is not possible because the initiating lesion is inherited. Reproductive prevention options after identification of familial variants include genetic counseling, partner/carrier testing, prenatal diagnosis, and preimplantation genetic testing. Cascade testing permits earlier recognition of biallelic relatives and clarifies carrier status.

Secondary prevention consists of early molecular diagnosis and early rehabilitation/orthotic management before fixed deformity and severe axon loss. Tertiary prevention includes fall prevention, stretching to reduce contractures, appropriate footwear/AFOs, weight and activity management, spine/foot surveillance, and symptom-triggered pulmonary assessment. There is no population newborn-screening program, vaccine, environmental-control program, or prophylactic medication specific to CMT2S.

## 14. Other species and natural disease

The relevant experimental ortholog is mouse **Ighmbp2** in *Mus musculus* (NCBI Taxon **10090**). The human taxon is *Homo sapiens* (**9606**). No well-established naturally occurring veterinary disease specifically equivalent to human CMT2S was identified in the retrieved literature; therefore no breed/VBO annotation or zoonotic transmission applies. CMT2S is not infectious and has no zoonotic potential.

Cross-species conservation is strong enough that engineered mouse alleles reproduce motor-and-sensory axon degeneration, but species differences in lifespan, axon length, dosage, and respiratory biology limit direct clinical translation.

## 15. Model organisms and experimental systems

### Dedicated CMT2S mouse models

Martin et al. generated homozygous CRISPR **Ighmbp2 c.1093_1095del, p.Glu365del (E365del)** mice and a human-allele knock-in **p.Tyr918Cys (Y918C)** model. The abstract states that these models showed **“progressive peripheral motor and sensory axonal degeneration.”** Both had motor deficits; E365del mice developed mechanical allodynia. (martin2023clinicallyrelevantmouse pages 1-2)

E365del mice developed hindquarter paresis/wasting at two to three months, rotarod deficits by six weeks, and allodynia by 12 weeks. At 20 weeks they had about **50% fewer femoral sensory axons**—404±50 versus 794±96—and approximately **31% fewer motor axons**—342.3±47 versus 496±28.3. Conduction velocity remained preserved, matching an axonal phenotype, and survival did not differ from wild type. Heterozygotes were phenotypically normal. (martin2023clinicallyrelevantmouse pages 2-4)

Strengths include recessive inheritance, progressive motor/sensory deficits, axon loss, and CMT2S-relevant electrophysiology. Limitations include engineered alleles, short murine lifespan, incomplete reproduction of human deformity/disability, and inter-model differences—Y918C affected conduction velocity more than E365del.

### Cellular models

Patient fibroblasts, iPSCs, induced motor neurons, and engineered human K562/HeLa cells are useful for variant interpretation, RNA processing, translation, ISR biology, and therapeutic testing. However, K562 cells are not peripheral neurons, and mixed SMARD1/CMT2S patient-neuron studies cannot fully resolve subtype-specific mechanisms. (smieszek2025potentialasobasedpersonalized pages 1-2, park2024ighmbp2deletionsuppresses pages 1-2, park2024ighmbp2deletionsuppresses pages 8-9)

## Evidence limitations and expert interpretation

CMT2S evidence is dominated by small families, referral cohorts, and model systems. Consequently, prevalence, penetrance, phenotype frequencies, survival, and treatment-response rates remain uncertain. The most defensible current interpretation is that IGHMBP2 disease is a continuum governed partly by residual protein function but substantially modified by yet-unresolved biological factors. The discovery that the same genotype can cause fatal SMARD1 in one child and non-respiratory CMT2S in another makes phenotype prediction from sequence alone unsafe. (tran2024anovelighmbp2 pages 5-6)

The 2024 translational/ISR study is mechanistically important but does not prove that ATF4 activation is the principal lesion in patient axons. Conversely, the dedicated CMT2S mice provide direct evidence that biallelic Ighmbp2 dysfunction is sufficient for progressive motor-and-sensory axon loss. The phase I/IIa AAV9 trial is the leading real-world disease-modifying implementation, but it remains experimental and presently supplies a safety framework rather than proof of benefit. (NCT05152823 chunk 1, park2024ighmbp2deletionsuppresses pages 1-2, martin2023clinicallyrelevantmouse pages 1-2)

## Key primary and recent sources

1. Cottenie E, et al. “Truncating and missense mutations in IGHMBP2 cause Charcot-Marie Tooth disease type 2.” *Am J Hum Genet.* Published 6 November 2014;95:590–601. PMID **25439726**. DOI: [10.1016/j.ajhg.2014.10.002](https://doi.org/10.1016/j.ajhg.2014.10.002). (NCT05152823 chunk 1)
2. Martin PB, et al. “Clinically relevant mouse models of Charcot–Marie–Tooth type 2S.” *Human Molecular Genetics.* 2023;32:1276–1288; online 22 November 2022. DOI: [10.1093/hmg/ddac283](https://doi.org/10.1093/hmg/ddac283). (martin2023clinicallyrelevantmouse pages 1-2, martin2023clinicallyrelevantmouse pages 2-4)
3. Tian Y, et al. “Exploring the relationship between IGHMBP2 gene mutations and SMARD1 and CMT2S: a systematic review.” *Front Neurosci.* Published 17 November 2023. DOI: [10.3389/fnins.2023.1252075](https://doi.org/10.3389/fnins.2023.1252075). (tian2023exploringtherelationship pages 1-2)
4. Tran VK, et al. “A novel IGHMBP2 variant and clinical diversity in Vietnamese SMARD1 and CMT2S patients.” *Front Pediatr.* February 2024. DOI: [10.3389/fped.2024.1165492](https://doi.org/10.3389/fped.2024.1165492). Exact abstract conclusion: **“The presence of three patients with the same genotype but distinct clinical outcomes suggested the interaction of variants and other factors including relating modified genes.”** (tran2024anovelighmbp2 pages 5-6)
5. Park J, et al. “IGHMBP2 deletion suppresses translation and activates the integrated stress response.” *Life Sci Alliance.* Published online 21 May 2024. DOI: [10.26508/lsa.202302554](https://doi.org/10.26508/lsa.202302554). (park2024ighmbp2deletionsuppresses pages 1-2, park2024ighmbp2deletionsuppresses pages 8-9)
6. ClinicalTrials.gov. “Gene Therapy for IGHMBP2-Related Diseases.” First posted 10 December 2021. [NCT05152823](https://clinicaltrials.gov/study/NCT05152823). (NCT05152823 chunk 1)

References

1. (tian2023exploringtherelationship pages 1-2): Yuan Tian, Jinfang Xing, Ying Shi, and Enwu Yuan. Exploring the relationship between ighmbp2 gene mutations and spinal muscular atrophy with respiratory distress type 1 and charcot-marie-tooth disease type 2s: a systematic review. Frontiers in Neuroscience, Nov 2023. URL: https://doi.org/10.3389/fnins.2023.1252075, doi:10.3389/fnins.2023.1252075. This article has 15 citations and is from a peer-reviewed journal.

2. (NCT05152823 chunk 1): Megan Waldrop. Gene Therapy for IGHMBP2-Related Diseases. Megan Waldrop. 2021. ClinicalTrials.gov Identifier: NCT05152823

3. (tran2024anovelighmbp2 pages 5-6): Van Khanh Tran, My Ha Cao, Thi Thanh Hai Nguyen, Phuong Thi Le, Hai Anh Tran, Dung Chi Vu, Ha Thu Nguyen, Mai Thi Phương Nguyen, The-Hung Bui, Thanh Binh Nguyen, Thanh Van Ta, and Thinh Huy Tran. A novel ighmbp2 variant and clinical diversity in vietnamese smard1 and cmt2s patients. Frontiers in Pediatrics, Feb 2024. URL: https://doi.org/10.3389/fped.2024.1165492, doi:10.3389/fped.2024.1165492. This article has 7 citations.

4. (park2024ighmbp2deletionsuppresses pages 1-2): Jesslyn Park, Hetvee Desai, José M Liboy-Lugo, Sohyun Gu, Ziad Jowhar, Albert Xu, and Stephen N Floor. Ighmbp2 deletion suppresses translation and activates the integrated stress response. May 2024. URL: https://doi.org/10.26508/lsa.202302554, doi:10.26508/lsa.202302554. This article has 10 citations and is from a peer-reviewed journal.

5. (martin2023clinicallyrelevantmouse pages 1-2): Paige B Martin, Sarah E Holbrook, Amy N Hicks, Timothy J Hines, Laurent P Bogdanik, Robert W Burgess, and Gregory A Cox. Clinically relevant mouse models of charcot-marie-tooth type 2s. Human molecular genetics, 32:1276-1288, Nov 2023. URL: https://doi.org/10.1093/hmg/ddac283, doi:10.1093/hmg/ddac283. This article has 17 citations and is from a domain leading peer-reviewed journal.

6. (OpenTargets Search: Charcot-Marie-Tooth disease type 2S-IGHMBP2): Open Targets Query (Charcot-Marie-Tooth disease type 2S-IGHMBP2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (martin2023clinicallyrelevantmouse pages 2-4): Paige B Martin, Sarah E Holbrook, Amy N Hicks, Timothy J Hines, Laurent P Bogdanik, Robert W Burgess, and Gregory A Cox. Clinically relevant mouse models of charcot-marie-tooth type 2s. Human molecular genetics, 32:1276-1288, Nov 2023. URL: https://doi.org/10.1093/hmg/ddac283, doi:10.1093/hmg/ddac283. This article has 17 citations and is from a domain leading peer-reviewed journal.

8. (tian2023exploringtherelationship pages 8-9): Yuan Tian, Jinfang Xing, Ying Shi, and Enwu Yuan. Exploring the relationship between ighmbp2 gene mutations and spinal muscular atrophy with respiratory distress type 1 and charcot-marie-tooth disease type 2s: a systematic review. Frontiers in Neuroscience, Nov 2023. URL: https://doi.org/10.3389/fnins.2023.1252075, doi:10.3389/fnins.2023.1252075. This article has 15 citations and is from a peer-reviewed journal.

9. (smieszek2025potentialasobasedpersonalized pages 1-2): Sandra Smieszek, Bartlomiej Przychodzen, Christina Tyner, Caroline Johnson, Haimeng Bai, Jennifer M. Kwon, D. Walker Hagan, Caitlyn Niccum, Rocky Brighton, Kenneth Hawkins, Romy Aiken, Ahmad Nawaz, Xiufang Guo, James Hickman, Christos M. Polymeropoulos, Gunther Birznieks, and Mihael H. Polymeropoulos. Potential aso-based personalized treatment for charcot-marie-tooth disease type 2s. Molecular Therapy Nucleic Acids, 36:102479, Mar 2025. URL: https://doi.org/10.1016/j.omtn.2025.102479, doi:10.1016/j.omtn.2025.102479. This article has 8 citations and is from a peer-reviewed journal.

10. (park2024ighmbp2deletionsuppresses pages 8-9): Jesslyn Park, Hetvee Desai, José M Liboy-Lugo, Sohyun Gu, Ziad Jowhar, Albert Xu, and Stephen N Floor. Ighmbp2 deletion suppresses translation and activates the integrated stress response. May 2024. URL: https://doi.org/10.26508/lsa.202302554, doi:10.26508/lsa.202302554. This article has 10 citations and is from a peer-reviewed journal.

11. (NCT05152823 chunk 2): Megan Waldrop. Gene Therapy for IGHMBP2-Related Diseases. Megan Waldrop. 2021. ClinicalTrials.gov Identifier: NCT05152823

## Artifacts

- [Edison artifact artifact-00](Charcot-Marie-Tooth_Disease_Axonal_Type_2S-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014511` (5 mentions) - the report calls it "if available"; MONDO calls it **Charcot-Marie-Tooth disease axonal type 2S**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0023055` (obsolete signal initiation by peptide hormone) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006412` (2 mentions) - the report calls it "GO:** translation"; GO calls it **translation**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.