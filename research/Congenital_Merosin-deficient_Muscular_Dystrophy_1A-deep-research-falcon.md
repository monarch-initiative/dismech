---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T17:55:19.136321'
end_time: '2026-09-05T18:02:48.699623'
duration_seconds: 449.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Merosin-deficient Muscular Dystrophy 1A
  mondo_id: MONDO:0011925
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 38
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0011925
    reported_labels:
    - if available
    ontology_label: congenital merosin-deficient muscular dystrophy 1A
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Congenital_Merosin-deficient_Muscular_Dystrophy_1A-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Merosin-deficient Muscular Dystrophy 1A
- **MONDO ID:** MONDO:0011925 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Merosin-deficient Muscular Dystrophy 1A** covering all of the
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
- **Disease Name:** Congenital Merosin-deficient Muscular Dystrophy 1A
- **MONDO ID:** MONDO:0011925 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Merosin-deficient Muscular Dystrophy 1A** covering all of the
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


# Congenital merosin-deficient muscular dystrophy 1A (MDC1A)

## Executive summary and scope

Congenital merosin-deficient muscular dystrophy 1A is the severe, congenital end of the **LAMA2-related muscular dystrophy (LAMA2-RD)** spectrum. Biallelic germline loss-of-function variants in **LAMA2** cause complete or near-complete deficiency of laminin-α2 (historically “merosin”), destabilizing laminin-211-containing basement membranes in skeletal muscle and peripheral nerve. The typical consequences are neonatal hypotonia, profound axial/proximal weakness, delayed motor milestones, progressive contractures and scoliosis, restrictive respiratory disease, feeding problems, and inability to walk independently. Diffuse cerebral white-matter MRI abnormalities are characteristic, while epilepsy, structural cortical malformations, and intellectual disability occur in clinically important minorities. There is currently no approved disease-modifying treatment; multidisciplinary respiratory, nutritional, orthopedic, cardiac, bone-health, and rehabilitative care is standard. Recent 2023–2024 work has emphasized deep phenotyping, trial-ready outcome measures, CNS involvement, early developmental mechanisms, and genetic/ECM-repair strategies. (sarkozy2020lama2relateddystrophiesclinical pages 1-2, enzmann2024amulticentercrosssectional pages 1-3, camelo2023brainmriabnormalities pages 1-3, bouman2023lama2relatedmuscular pages 1-2)

The following compact table summarizes fields most suitable for direct knowledge-base curation.

| Domain | Curated finding | Key ontology/identifier |
|---|---|---|
| Disease entity | Severe congenital end of the LAMA2-related muscular-dystrophy spectrum, usually associated with complete or near-complete merosin/laminin-α2 deficiency; also called MDC1A or LAMA2-related congenital muscular dystrophy. (nguyen2019currentunderstandingand pages 1-2, sarkozy2020lama2relateddystrophiesclinical pages 1-2) | MONDO:0011925; OMIM phenotype: 607855 |
| Causal gene/protein | Biallelic pathogenic variants in **LAMA2** impair laminin-α2, a component of extracellular-matrix laminin-211 (α2β1γ1). (nguyen2019currentunderstandingand pages 1-2, nguyen2019currentunderstandingand pages 5-6) | LAMA2; OMIM gene: 156225; chromosome 6q22.33 |
| Inheritance | Autosomal recessive, germline Mendelian disease; each pregnancy of two confirmed heterozygous carriers has a 25% affected, 50% carrier and 25% unaffected/non-carrier probability. (nguyen2019currentunderstandingand pages 1-2, sarkozy2020lama2relateddystrophiesclinical pages 1-2) | HP:0000007 Autosomal recessive inheritance |
| Variant spectrum | Nonsense, frameshift, canonical/noncanonical splice and exon-level deletion/CNV alleles predominate in severe disease; complete loss-of-function usually causes absent laminin-α2, although genotype–phenotype exceptions occur. One 2024 cohort review estimated 60–80% single-nucleotide variants and 20–40% exon deletions. (enzmann2024amulticentercrosssectional pages 1-3, nmer2024exploringsplicesitemutations pages 6-7, nguyen2019currentunderstandingand pages 5-6) | ClinVar classification: pathogenic/likely pathogenic under ACMG/AMP; germline |
| Molecular mechanism | Loss of laminin-211 linkage to α-dystroglycan and integrin α7β1 weakens the basement-membrane–sarcolemma–cytoskeleton axis, leading to contraction-associated injury, degeneration and secondary inflammation, fibrosis and defective regeneration. (nguyen2019currentunderstandingand pages 5-6, fernandes2023lama2cmdestablishmentof pages 13-15) | GO:0005604 basement membrane; GO:0031589 cell–substrate adhesion; GO:0007519 skeletal-muscle tissue development |
| Core neuromuscular phenotype | Congenital/early-infantile hypotonia, severe axial and proximal weakness, delayed motor development, reduced spontaneous movement and muscle atrophy; independent walking is uncommon. (sarkozy2020lama2relateddystrophiesclinical pages 1-2, enzmann2024amulticentercrosssectional pages 1-3) | HP:0001252 Hypotonia; HP:0003701 Proximal muscle weakness; HP:0001270 Motor delay; HP:0003202 Skeletal muscle atrophy |
| Orthopedic phenotype | Progressive large-joint contractures, spinal rigidity, scoliosis and hyperlordosis substantially impair positioning, transfers and mobility. (sarkozy2020lama2relateddystrophiesclinical pages 1-2, enzmann2024amulticentercrosssectional pages 1-3, zambon2020lama2‐relatedmusculardystrophy pages 1-2) | HP:0001371 Flexion contracture; HP:0002650 Scoliosis; HP:0003306 Spinal rigidity; HP:0003307 Hyperlordosis |
| Respiratory phenotype | Restrictive respiratory weakness, sleep-related hypoventilation, ineffective cough and recurrent infections may begin in childhood and progress to ventilatory dependence. (bouman2023lama2relatedmuscular pages 1-2, zambon2020lama2‐relatedmusculardystrophy pages 1-2, sarkozy2020lama2relateddystrophiesclinical pages 6-7) | HP:0002093 Respiratory insufficiency; HP:0002104 Apnea/sleep-related hypoventilation—broader mapping; HP:0002205 Recurrent respiratory infections |
| Feeding/growth phenotype | Feeding and swallowing difficulty, silent aspiration, poor weight gain or failure to thrive may require nutritional supplementation or gastrostomy. (enzmann2024amulticentercrosssectional pages 1-3, zambon2020lama2‐relatedmusculardystrophy pages 1-2, sarkozy2020lama2relateddystrophiesclinical pages 6-7) | HP:0011968 Feeding difficulties; HP:0002015 Dysphagia; HP:0001508 Failure to thrive |
| Nervous-system phenotype | Diffuse cerebral white-matter MRI signal abnormalities are characteristic. A minority have cortical malformations, epilepsy or intellectual disability; demyelinating peripheral neuropathy is also recognized. (camelo2023brainmriabnormalities pages 1-3, enzmann2024amulticentercrosssectional pages 1-3, fernandes2023lama2cmdestablishmentof pages 13-15) | HP:0002500 Abnormal cerebral white matter morphology; HP:0001250 Seizure; HP:0001249 Intellectual disability; HP:0007108 Demyelinating peripheral neuropathy |
| Cardiac/bone phenotype | Cardiomyopathy or conduction abnormalities are less dominant than skeletal/respiratory disease but warrant surveillance; reduced bone quality and fragility fractures are important secondary morbidity. (bouman2023lama2relatedmuscular pages 1-2, bouman2023lama2relatedmuscular pages 12-13, zambon2020lama2‐relatedmusculardystrophy pages 1-2) | HP:0001638 Cardiomyopathy—broader; HP:0011675 Arrhythmia—broader; HP:0000938 Osteopenia; HP:0002756 Pathologic fracture |
| Diagnostic evaluation | Confirm with biallelic LAMA2 variants using a neuromuscular panel or exome/genome sequencing with deletion/duplication analysis. RNA studies can resolve suspected splice/deep-intronic variants. (nmer2024exploringsplicesitemutations pages 6-7, enzmann2024amulticentercrosssectional pages 1-3, tan2021naturalhistoryand pages 1-2) | LAMA2 molecular genetic testing; ACMG/AMP variant interpretation |
| Supporting tests | Serum CK is commonly elevated, often above 1,000 IU/L; brain MRI typically shows diffuse T2/FLAIR white-matter abnormalities; muscle biopsy shows dystrophic change and absent/reduced laminin-α2 immunoreactivity. (sarkozy2020lama2relateddystrophiesclinical pages 1-2, enzmann2024amulticentercrosssectional pages 1-3) | HP:0003236 Elevated serum creatine kinase; brain MRI; laminin-α2 immunohistochemistry |
| Motor cohort data | In 116 Chinese LAMA2-CMD patients, 76.3% achieved head control, 92.6% independent sitting and 18.4% walking; median attainment ages were 6, 11 and 27 months, respectively. (tan2021naturalhistoryand pages 1-2) | Motor milestones; MFM-20/32 and CHOP INTEND are broader outcome instruments |
| Multisystem cohort data | In a 2023 cohort of 27 genetically confirmed patients, 85% had respiratory impairment, 37% required ventilation, 62% had fragmented QRS, 25% abnormal LV strain and 14% reduced LVEF; mean MFM-20/32 was 42.0% ± 29.4%. (bouman2023lama2relatedmuscular pages 1-2) | Spirometry/sleep assessment; ECG; echocardiography; MFM-20/32 |
| CNS cohort data | Among 52 Brazilian patients, cortical malformations and epilepsy each occurred in 19.2%, and intellectual disability in 15.4%; LG-domain and null variants correlated with greater CNS involvement. (camelo2023brainmriabnormalities pages 1-3) | Brain MRI; EEG when clinically indicated; HP terms above |
| Longitudinal morbidity | In a pediatric cohort dominated by complete deficiency, 22 patients began nocturnal noninvasive ventilation at median age 11.7 years, FVC declined 2.9 percentage points/year, 20 underwent gastrostomy at median age 10.9 years and seven died at median age 12 years. (zambon2020lama2‐relatedmusculardystrophy pages 1-2) | Forced vital capacity; noninvasive ventilation; gastrostomy |
| Management | No approved disease-modifying therapy is established. Care is multidisciplinary: respiratory surveillance and cough/NIV support, swallowing and nutritional management, physiotherapy and contracture prevention, mobility/assistive technology, scoliosis management, cardiac monitoring, and bone-health optimization. (bouman2023lama2relatedmuscular pages 12-13, sarkozy2020lama2relateddystrophiesclinical pages 6-7, NCT06132750 chunk 1) | NCIT mappings are broader/non-specific: Physical Therapy, Noninvasive Ventilation, Gastrostomy, Spinal Fusion, Genetic Counseling |
| Trials and readiness | Current registered work is predominantly observational: completed infant/toddler retrospective study, 75 participants (NCT04299321); completed LAST STRONG study, 38 participants (NCT04478981); and five-year Extended LAST STRONG study, planned 40 participants (NCT06132750). A seven-adult ex-vivo genetic-correction study was observational rather than therapeutic. (NCT06582537 chunk 1, NCT06132750 chunk 1, NCT04478981 chunk 1, NCT04299321 chunk 1) | NCT04299321; NCT04478981; NCT06132750; NCT06582537 |
| Experimental strategies | Preclinical approaches include mini-agrin/linker proteins, laminin-α1 substitution or activation, LAMA2 correction/exon skipping, CRISPR-based editing and modulation of apoptosis, fibrosis or inflammation; clinical efficacy remains unproven. (nguyen2019currentunderstandingand pages 5-6, gawlik2019earlyskeletalmuscle pages 15-16) | NCIT: Gene Therapy, CRISPR-Cas9 Gene Editing, Antisense Oligonucleotide Therapy—broader/non-specific |
| Mouse models | **Lama2** dy/dy, dy2J/dy2J, dyW/dyW and dy3K/dy3K mice reproduce combinations of muscular dystrophy, weakness, fibrosis and peripheral dysmyelination. Severe dy3K/dy3K and dyW/dyW animals have shortened survival; dy2J/dy2J is milder and useful for longer therapeutic studies. (fernandes2023lama2cmdestablishmentof pages 13-15, gawlik2020afamilyof pages 1-2) | Mus musculus, NCBI Taxon:10090; MGI/IMSR resources |
| Zebrafish/cellular models | Lama2-deficient zebrafish show myofiber detachment with a transient rescue window and laminin-responsive regeneration. CRISPR Lama2-null myoblasts and dyW fetal muscle reveal impaired proliferation/differentiation, oxidative stress, DNA damage and broad transcriptional downregulation; the latter 2024 evidence was a non-peer-reviewed preprint. (martins2024deregulationofmultiple pages 3-6, hall2019cellularrescuein pages 1-2, martins2024deregulationofmultiple pages 1-3) | Danio rerio, NCBI Taxon:7955; C2C12 myoblast model; ZFIN/Cellosaurus resources |


*Table: Compact curation of MDC1A identifiers, genetics, phenotypes, quantitative human evidence, diagnostics, management, trials, and experimental models. Ontology mappings labeled “broader/non-specific” should be validated against the target knowledge-base release.*

## 1. Disease information

**Definition.** MDC1A is an autosomal-recessive congenital muscular dystrophy caused by laminin-α2 deficiency. “LAMA2-related muscular dystrophy” is the preferred spectrum term because partial laminin-α2 deficiency can instead produce milder childhood/adult limb-girdle disease (LGMDR23). The severe congenital entity should not be assumed from the presence of any LAMA2 variant alone; phenotype, residual protein, and allelic context matter. (nguyen2019currentunderstandingand pages 1-2, sarkozy2020lama2relateddystrophiesclinical pages 1-2, nguyen2019currentunderstandingand pages 5-6)

**Identifiers and synonyms.** Curated identifiers include **MONDO:0011925**, **OMIM phenotype 607855**, and **LAMA2 OMIM 156225**. Common names are *merosin-deficient congenital muscular dystrophy type 1A*, *MDC1A*, *LAMA2-related congenital muscular dystrophy*, *LAMA2-CMD*, *laminin-α2-chain-deficient congenital muscular dystrophy*, and historically *congenital muscular dystrophy 1A*. ICD-10 generally places it under congenital muscular dystrophy/other muscular dystrophy rather than assigning an MDC1A-specific code; ICD-11, MeSH, and SNOMED implementations should therefore be checked against the local release rather than inferred from a broad muscular-dystrophy parent. (sarkozy2020lama2relateddystrophiesclinical pages 1-2, fernandes2023lama2cmdestablishmentof pages 13-15)

**Data provenance.** The information here is aggregated disease-level evidence from published cohorts, reviews, and ClinicalTrials.gov. It is not extracted from an identifiable individual EHR. Some cited cohorts used registry or retrospective chart data, notably the Swiss-Reg-NMD cohort and the 75-participant infant/toddler natural-history study. (enzmann2024amulticentercrosssectional pages 1-3, NCT04299321 chunk 1)

## 2. Etiology, risk, protection, and gene–environment interaction

The necessary cause is **biallelic pathogenic LAMA2 variation**. Severe MDC1A is most often associated with nonsense, frameshift, splice-disrupting, or exon-level deletion/CNV alleles that abolish or markedly reduce laminin-α2. A 2024 review/cohort source estimated 60–80% single-nucleotide variants and 20–40% one- or multi-exon deletions. Splice variants may cause exon skipping, cryptic acceptor use, intronic insertion, frameshift, and premature termination. (enzmann2024amulticentercrosssectional pages 1-3, nmer2024exploringsplicesitemutations pages 6-7)

This is a highly penetrant recessive Mendelian disorder, not an environmentally initiated disease. Family history and consanguinity increase the probability that both parents carry the same rare allele but are not mechanistic causes independent of genotype. Sex is not a causal risk factor. No validated toxicant, diet, infection, lifestyle exposure, or occupational factor causes MDC1A; infections, malnutrition, aspiration, and immobility instead modify morbidity after disease onset. Severe pneumonia is a major mortality pathway. (tan2021naturalhistoryand pages 1-2, zambon2020lama2‐relatedmusculardystrophy pages 1-2)

No reproducible **protective human allele** or clinically actionable modifier gene has been established. Residual laminin-α2 expression is generally protective, but exceptions—including severe disease with residual C-terminal protein and occasional milder disease despite complete deficiency—show that it is not a perfect predictor. Experimental modifiers include laminin-α1, mini-agrin, integrin/ECM linkage, dystrophin/β-sarcoglycan status, osteopontin, galectin-3, CTGF/TGF-β, and inflammatory/apoptotic pathways; these remain model evidence rather than validated human protective factors. (nguyen2019currentunderstandingand pages 5-6, gawlik2019earlyskeletalmuscle pages 15-16)

## 3. Phenotypes

**Core neuromuscular phenotype.** Congenital or early-infantile hypotonia (**HP:0001252**), proximal/axial weakness (**HP:0003701**), reduced spontaneous movement, motor delay (**HP:0001270**), muscle atrophy (**HP:0003202**), poor head control, and absent or markedly delayed walking are severe and chronic-progressive. About two-thirds are symptomatic at birth and nearly all remaining severe cases by six months. In 116 Chinese LAMA2-CMD patients, median onset was birth, 75.9% were symptomatic in the first week, 76.3% achieved head control, 92.6% sat independently, and 18.4% walked; median ages were 6, 11, and 27 months. (sarkozy2020lama2relateddystrophiesclinical pages 1-2, tan2021naturalhistoryand pages 1-2)

**Orthopedic manifestations.** Progressive large-joint flexion contractures (**HP:0001371**), spinal rigidity (**HP:0003306**), scoliosis (**HP:0002650**), hyperlordosis (**HP:0003307**), hip deformity, and reduced bone density/pathologic fracture are common and impair transfers, seating, hygiene, sleep, and participation. Motor regression often accelerates with contractures at approximately 6–9 years. In the UK pediatric cohort, scoliosis affected 32 complete-deficiency patients and nine underwent spine surgery. (tan2021naturalhistoryand pages 1-2, zambon2020lama2‐relatedmusculardystrophy pages 1-2)

**Respiratory phenotype.** Restrictive respiratory insufficiency (**HP:0002093**), nocturnal hypoventilation, weak cough, atelectasis, and recurrent respiratory infection (**HP:0002205**) are progressive and major determinants of survival. In Bouman et al.’s 2023 lifespan cohort, 85% had respiratory impairment and 37% needed noninvasive or invasive ventilation. In the UK cohort, 22 complete-deficiency patients began nocturnal noninvasive ventilation at median age 11.7 years, and FVC declined approximately 2.9 percentage points predicted annually. (bouman2023lama2relatedmuscular pages 1-2, zambon2020lama2‐relatedmusculardystrophy pages 1-2)

**Feeding and growth.** Dysphagia (**HP:0002015**), feeding difficulty (**HP:0011968**), silent aspiration, poor weight gain/failure to thrive (**HP:0001508**), and constipation may reduce quality of life and compound respiratory risk. Nineteen complete-deficiency patients in the UK cohort required gastrostomy, at median age 10.9 years. Baseline swallowing assessment is recommended because aspiration may be clinically silent. (zambon2020lama2‐relatedmusculardystrophy pages 1-2, sarkozy2020lama2relateddystrophiesclinical pages 6-7)

**CNS and peripheral nerve.** Diffuse symmetric cerebral white-matter T2/FLAIR abnormalities (**HP:0002500**) are characteristic. In 52 Brazilian patients, 19.2% had cortical malformations, 19.2% epilepsy (**HP:0001250**), and 15.4% intellectual disability (**HP:0001249**); no ambulant patient had cortical malformation or epilepsy. In the 2024 Swiss cohort, 13/14 imaged patients had white-matter changes and 11/14 had additional structural abnormalities. Demyelinating peripheral neuropathy (**HP:0007108**) reflects laminin-211’s Schwann-cell function. (camelo2023brainmriabnormalities pages 1-3, enzmann2024amulticentercrosssectional pages 1-3, fernandes2023lama2cmdestablishmentof pages 13-15)

**Cardiac and bone manifestations.** Cardiomyopathy and conduction abnormalities are less consistent than respiratory disease but are not negligible. In 27 patients, fragmented QRS occurred in 62%, abnormal LV global longitudinal strain in 25%, and reduced LVEF in 14%; reduced bone quality and fragility fractures were also prominent. Suggested mappings are **HP:0001638** (cardiomyopathy, broad), **HP:0011675** (arrhythmia, broad), **HP:0000938** (osteopenia), and **HP:0002756** (pathologic fracture). (bouman2023lama2relatedmuscular pages 1-2, bouman2023lama2relatedmuscular pages 12-13)

These phenotypes markedly limit mobility, self-care, school/work participation, communication endurance, and community access. Published studies use MFM20/32 and generic/pediatric questionnaires, but robust MDC1A-specific EQ-5D/SF-36 utility values were not identified. The mean MFM20/32 in Bouman et al. was 42.0% ±29.4%; accelerometry correlated strongly with MFM (r=−0.928, p<0.01). (bouman2023lama2relatedmuscular pages 1-2, bouman2023lama2relatedmuscular pages 12-13)

## 4. Genetic and molecular information

**Gene.** **LAMA2**, chromosome 6q22.33, contains 65 exons and encodes laminin subunit α2. Laminin-α2 combines with β1 and γ1 chains to form laminin-211. Disease alleles are germline; somatic LAMA2 mutation is not the basis of MDC1A. (nguyen2019currentunderstandingand pages 5-6)

**Variant spectrum and interpretation.** Diagnostic genotypes include homozygous or compound-heterozygous pathogenic/likely pathogenic nonsense, frameshift, splice, missense, in-frame deletion, and exon-level CNV alleles. Variants must be interpreted using ACMG/AMP criteria, segregation, population frequency, predicted loss of function, laminin-α2 immunostaining, and—where relevant—RNA analysis. VUS alone should not be treated as confirmation without supporting evidence. Disease-causing alleles are generally very rare or absent from population databases, but no universal gnomAD frequency applies to all variants. (enzmann2024amulticentercrosssectional pages 1-3, nmer2024exploringsplicesitemutations pages 6-7)

Genotype–phenotype correlation is probabilistic. Null/null alleles usually cause complete deficiency and MDC1A; missense/in-frame alleles and residual protein more often produce a milder limb-girdle phenotype. In the Chinese cohort, nonsense variants represented 56.9% of LAMA2-CMD alleles versus 21.4% in LGMDR23, whereas missense variants represented 12.9% versus 71.4%. CNVs occurred in 26.4% of survivors and 50.0% of nonsurvivors (p=0.029). (tan2021naturalhistoryand pages 1-2)

Examples of population-associated alleles include Chinese recurrent **c.7147C>T (p.Arg2383Ter)**, exon 4 deletion, and **c.5156_5159del (p.Lys1719ArgfsTer5)**; Brazilian **c.1255del (p.Ile419LeufsTer4)** occurred in 11/52 patients (21.15%) and may be a founder allele. LG-domain variants were associated with brain malformation (p=0.016), and null variants with broader CNS involvement. These associations require replication and should not be used deterministically. (camelo2023brainmriabnormalities pages 1-3, tan2021naturalhistoryand pages 1-2)

No established disease-defining epimutation, methylation signature, aneuploidy, translocation, or anticipation mechanism is known. Large intragenic deletions/duplications are relevant, but conventional karyotyping is usually uninformative. Germline mosaicism is theoretically possible and has implications for recurrence counseling, but a disease-specific rate was not identified.

## 5. Environmental information

MDC1A is not attributed to toxins, radiation, pollution, smoking, alcohol, diet, or infectious agents. Environmental and care-related factors influence complications: aspiration and respiratory infections worsen pulmonary decline; immobility, low weight-bearing, inadequate calcium/vitamin D, and reduced sunlight may worsen bone health; inappropriate high-load exercise may increase fatigue or injury. Conversely, vaccination, respiratory physiotherapy, optimized nutrition, safe activity, assisted standing, and infection prevention reduce secondary morbidity but do not prevent the genetic disease. (tan2021naturalhistoryand pages 1-2, bouman2023lama2relatedmuscular pages 12-13, sarkozy2020lama2relateddystrophiesclinical pages 6-7)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic LAMA2 loss-of-function leads to** absent or severely reduced laminin-α2 and therefore defective laminin-211.
2. **Defective laminin-211 leads to** impaired basement-membrane polymerization and weakened binding to α-dystroglycan, α7β1 integrin, agrin/nidogen, and the dystrophin-associated cytoskeleton.
3. **Loss of ECM–sarcolemma–cytoskeleton coupling leads to** contraction-associated myofiber detachment, tearing, and mechanical instability.
4. **Mechanical injury and deficient survival signaling lead to** myofiber degeneration and delayed apoptosis; altered FAK/integrin, calcium, autophagy, and oxidative-stress pathways are implicated mainly by model evidence.
5. **Repeated degeneration leads to** satellite-cell activation followed by inadequate regeneration, inflammatory-cell recruitment, myofibroblast activation, ECM deposition, and fibrosis.
6. **Muscle loss and fibrosis lead to** weakness, contractures, scoliosis, feeding impairment, and restrictive respiratory failure.
7. **In Schwann-cell basement membranes, laminin-211 loss leads to** defective axon sorting, ensheathment, and myelination, resulting in demyelinating neuropathy that adds to weakness.
8. **In the CNS, laminin-α2 deficiency leads to** abnormal white-matter development and, in a minority, cortical malformation; the exact human causal intermediates remain incompletely demonstrated.
9. **Respiratory-muscle weakness plus aspiration/infection leads to** pneumonia, ventilatory dependence, and premature mortality. (nguyen2019currentunderstandingand pages 5-6, hall2019cellularrescuein pages 1-2, fernandes2023lama2cmdestablishmentof pages 13-15)

The laminin-α2 LG1–3 domains interact chiefly with α7β1 integrin, while LG4–5 bind α-dystroglycan and sulfated glycolipids. β-dystroglycan connects to dystrophin and actin. Thus, the primary biochemical abnormality is an extracellular structural/signaling scaffold defect—not an enzyme deficiency or channelopathy. Suggested terms include **GO:0005604 basement membrane**, **GO:0031589 cell–substrate adhesion**, **GO:0007519 skeletal-muscle tissue development**, **GO:0042692 muscle-cell differentiation**, and **GO:0006954 inflammatory response**. (nguyen2019currentunderstandingand pages 5-6, fernandes2023lama2cmdestablishmentof pages 13-15)

**Recent molecular profiling.** A January 24, 2024 bioRxiv preprint used dyW fetal muscle and CRISPR Lama2-null C2C12/myogenic cells. It placed onset at embryonic days 17.5–18.5 and reported reduced myogenic-cell proliferation, G1 arrest, impaired differentiation/fusion, oxidative stress, glutathione depletion, HO-1 increase, fewer mitochondria, DNA-damage foci, reduced autophagy markers, and broad RNA-seq downregulation of differentiation/cytoskeletal genes, including *Myh7, Myh2, Tmem182,* and *Cacna1s*. This is valuable hypothesis-generating mouse/in-vitro evidence, not yet a validated human multi-omic signature. (martins2024deregulationofmultiple pages 3-6, martins2024deregulationofmultiple pages 10-12, martins2024deregulationofmultiple pages 1-3)

Relevant cells include skeletal myofibers (**CL:0000188**), myoblasts (**CL:0000056**), skeletal-muscle satellite cells (**CL:0000594**), Schwann cells (**CL:0002573**), fibroblasts/myofibroblasts, macrophages, and cardiac myocytes (**CL:0000746**). No definitive human single-cell or spatial-transcriptomic atlas specific to MDC1A was established in the retrieved evidence.

## 7. Anatomical structures affected

The primary organ is skeletal muscle (**UBERON:0001134**), especially axial, proximal limb, respiratory, bulbar/masticatory, and neck muscles. Muscle ultrasound in 2023 showed symmetric increased echogenicity, with sternocleidomastoid particularly affected; rectus abdominis, vastus lateralis, and gastrocnemius were proposed imaging targets. Disease is generally bilateral and symmetric rather than lateralized. (bouman2023lama2relatedmuscular pages 1-2, bouman2023lama2relatedmuscular pages 12-13)

Secondary structures include diaphragm and chest-wall musculature; spine and large joints; peripheral nerve/Schwann-cell basal lamina; cerebral white matter; cortex in malformation-positive cases; myocardium and conduction system; bone; and gastrointestinal/oropharyngeal structures involved in swallowing. At subcellular scale, the extracellular basement membrane, sarcolemma, dystrophin-associated glycoprotein complex, integrin focal adhesions, actin cytoskeleton, mitochondria, autophagic machinery, and nuclei under DNA-damage stress are implicated. (nguyen2019currentunderstandingand pages 5-6, martins2024deregulationofmultiple pages 3-6, fernandes2023lama2cmdestablishmentof pages 13-15)

## 8. Temporal development

Onset is congenital, chronic, and usually apparent at birth or within six months. In the 2024 Swiss cohort, all 14 severe CMD cases began before 12 months and 11/14 before six months. Severe weakness and delayed milestones characterize infancy; contractures and scoliosis progress through childhood, often with motor regression around 6–9 years; dysphagia, restrictive ventilation, and orthopedic dependence become major later-childhood/adolescent issues. The disease is lifelong and progressive without spontaneous remission. (enzmann2024amulticentercrosssectional pages 1-3, tan2021naturalhistoryand pages 1-2)

A critical therapeutic window may precede overt damage. Mouse/preprint evidence suggests fetal myogenesis is already disturbed, while zebrafish fibers remain temporarily viable after detachment and can be “re-functionalised” by laminin delivery. Translation of these windows to prenatal or neonatal human intervention remains speculative. (hall2019cellularrescuein pages 1-2, martins2024deregulationofmultiple pages 1-3)

## 9. Inheritance and population

Inheritance is autosomal recessive (**HP:0000007**). For two confirmed carriers, each conception has a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability. Males and females are expected to be affected equally. Penetrance for a clearly pathogenic biallelic genotype is high, but expressivity varies with allele type and residual protein. Anticipation is not expected. (nguyen2019currentunderstandingand pages 1-2, nguyen2019currentunderstandingand pages 5-6)

Published prevalence estimates vary from approximately **0.14/100,000 in Italy to 2.5/100,000 in Sweden**; another review gives 1–9 per million and approximately 4 per 500,000 children. The variation reflects ascertainment, founder alleles, consanguinity, and changing molecular diagnosis rather than a known environmental geography. Incidence and global carrier frequency remain poorly resolved. (nguyen2019currentunderstandingand pages 1-2, enzmann2024amulticentercrosssectional pages 1-3)

Founder effects are documented or suspected in Qatar, China, and Brazil. Consanguinity increases homozygosity and can elevate local prevalence. Carrier frequency should be calculated variant- and ancestry-specifically from validated population databases, not from the disease prevalence alone. (camelo2023brainmriabnormalities pages 1-3, tan2021naturalhistoryand pages 1-2)

## 10. Diagnostics

**Clinical suspicion.** Consider MDC1A in a neonate/infant with hypotonia, axial/proximal weakness, delayed milestones, contractures, elevated CK, and diffuse white-matter MRI signal changes. CK is commonly **>1,000 IU/L**, but CK is supportive rather than diagnostic. EMG is usually myopathic; nerve-conduction studies may reveal demyelinating neuropathy. (sarkozy2020lama2relateddystrophiesclinical pages 1-2, fernandes2023lama2cmdestablishmentof pages 13-15)

**Imaging and pathology.** Brain MRI typically demonstrates diffuse symmetric T2/FLAIR white-matter abnormality; structural malformations require deliberate review. Muscle MRI/ultrasound can document selective fatty replacement or echogenicity and may serve as outcomes. Muscle biopsy shows dystrophic change, fiber-size variation, degeneration/regeneration, fibrosis, and absent or reduced laminin-α2 immunoreactivity. Biopsy remains useful when genetics is unresolved but is no longer mandatory after unequivocal molecular confirmation. (enzmann2024amulticentercrosssectional pages 1-3, camelo2023brainmriabnormalities pages 1-3, bouman2023lama2relatedmuscular pages 12-13)

**Recommended molecular workflow.** Use a congenital-muscular-dystrophy/neuromuscular NGS panel or trio WES with complete **LAMA2** coverage plus exon-level deletion/duplication calling. Confirm variants and segregation. If one allele is missing, consider WGS for intronic/structural variants and RNA sequencing or targeted RT-PCR from muscle/fibroblasts to demonstrate splice effects. CMA, karyotype, FISH, mitochondrial-DNA testing, and repeat-expansion assays are not routine unless another diagnosis is suspected. A 2024 Egyptian series achieved molecular diagnoses in all five suspected merosin-deficient cases using WES with splice/CNV analysis, illustrating utility rather than a universal 100% yield. (nmer2024exploringsplicesitemutations pages 6-7, enzmann2024amulticentercrosssectional pages 1-3)

**Differential diagnosis.** Important alternatives include dystroglycanopathies (*POMT1/2, POMGNT1/2, FKRP, FKTN, GMPPB, B3GALNT2, POMK*), collagen-VI disorders, SELENON-related myopathy, LMNA-related CMD, integrin-α7 deficiency, congenital titinopathy, congenital myopathies, spinal muscular atrophy, Pompe disease, and congenital neuropathies. White-matter abnormalities plus absent laminin-α2 strongly favor LAMA2-RD; prominent eye/cobblestone-brain disease often favors a dystroglycanopathy.

There is no universal newborn biochemical screen. Targeted familial testing, cascade carrier testing, prenatal diagnosis, and preimplantation genetic testing are available after the familial variants are established.

## 11. Outcome and prognosis

Prognosis is variable and has improved with ventilatory, nutritional, and orthopedic care. Independent walking is rare in complete deficiency. Respiratory disease, aspiration, pneumonia, scoliosis, contractures, osteoporosis/fracture, and feeding failure dominate morbidity. In the Chinese series, 24 LAMA2-RD patients died, mostly from severe pneumonia. In the UK complete-deficiency cohort, seven died at a median age of 12 years. An older synthesis estimated that 30% of early-onset patients died in the first decade, but this estimate likely predates modern multidisciplinary care and should not be applied uncritically to current patients. (nguyen2019currentunderstandingand pages 1-2, tan2021naturalhistoryand pages 1-2, zambon2020lama2‐relatedmusculardystrophy pages 1-2)

Adverse prognostic indicators include complete protein deficiency/null alleles, severe early respiratory impairment, recurrent pneumonia/aspiration, rapid contracture and scoliosis progression, poor nutrition, and possibly CNVs. Preserved laminin-α2 and attained ambulation generally indicate milder disease. No FDA-qualified prognostic biomarker exists. MFM20/32, accelerometry, muscle ultrasound/MRI, FVC trajectory, time to NIV/gastrostomy, and cardiac strain are current research outcomes rather than validated surrogate endpoints. (tan2021naturalhistoryand pages 1-2, bouman2023lama2relatedmuscular pages 1-2, zambon2020lama2‐relatedmusculardystrophy pages 1-2)

## 12. Treatment and current implementation

There is **no approved curative or disease-modifying pharmacotherapy**. Standard care is multidisciplinary:

* respiratory surveillance with spirometry, oximetry/capnography and sleep studies; airway clearance, cough-assist, lung-volume recruitment, noninvasive ventilation, and invasive ventilation when necessary;
* swallowing evaluation, texture adaptation, caloric supplementation, reflux/constipation management, and gastrostomy when oral intake or aspiration safety is inadequate;
* gentle range-of-motion therapy, positioning, orthoses, supported standing, wheelchairs and communication/access technology; avoid high-load eccentric exercise;
* serial scoliosis/hip assessment and individualized spinal fusion or other orthopedic surgery;
* ECG and echocardiography, with cardiology-directed standard therapy for LV dysfunction or arrhythmia;
* DEXA/bone monitoring, calcium/vitamin-D optimization, fracture management, and specialist osteoporosis treatment;
* vaccination, prompt infection treatment, psychosocial support, school accommodations, palliative-care involvement when appropriate, and genetic counseling. (bouman2023lama2relatedmuscular pages 12-13, sarkozy2020lama2relateddystrophiesclinical pages 6-7)

Suggested broad NCIT intervention mappings are *Physical Therapy*, *Occupational Therapy*, *Noninvasive Ventilation*, *Mechanical Ventilation*, *Gastrostomy*, *Spinal Fusion*, *Nutritional Support*, and *Genetic Counseling*; exact NCIT codes should be validated against the deployment release.

**Experimental therapies.** Omigapil, an anti-apoptotic compound, reached a phase-1 pharmacokinetic/safety study but has no established efficacy. Preclinical strategies include laminin-111/laminin-α1 substitution, AAV mini-agrin, engineered linker proteins reconnecting laminin to dystroglycan/integrin, LAMA1 activation, LAMA2 exon skipping or correction, CRISPR editing, and modulation of apoptosis, inflammation, fibrosis/TGF-β, autophagy, growth, and calcium pathways. Full-length LAMA2 exceeds ordinary AAV cargo capacity, making replacement technically difficult. (sarkozy2020lama2relateddystrophiesclinical pages 1-2, nguyen2019currentunderstandingand pages 5-6, gawlik2019earlyskeletalmuscle pages 15-16)

The current registered landscape is predominantly trial-readiness research, not therapeutic efficacy testing: **NCT04299321**, completed retrospective infant/toddler natural history, n=75; **NCT04478981**, completed LAST STRONG prospective study, n=38; **NCT06132750**, Extended LAST STRONG, planned n=40 through 2026; and **NCT06582537**, completed seven-adult observational biopsy study of ex-vivo CRISPR correction. **NCT06503367** is an active observational study in children aged 0–5. None administers an approved disease-modifying treatment. (NCT06503367 chunk 2, NCT06582537 chunk 1, NCT06132750 chunk 1, NCT04478981 chunk 1, NCT04299321 chunk 1)

## 13. Prevention

Primary prevention through lifestyle modification or vaccination is impossible because the initiating lesion is inherited. Reproductive prevention options are carrier/cascade testing, genetic counseling, prenatal diagnosis, and preimplantation genetic testing for families with known variants. Population-wide newborn screening is not established. Earlier molecular diagnosis is secondary prevention in the sense that it permits anticipatory respiratory, swallowing, orthopedic, cardiac, and bone surveillance before complications become advanced. (nmer2024exploringsplicesitemutations pages 6-7, sarkozy2020lama2relateddystrophiesclinical pages 6-7)

Tertiary prevention includes immunization against routine respiratory pathogens, aspiration prevention, cough assistance, timely NIV, contracture-prevention therapy, pressure-injury prevention, nutrition optimization, assisted weight-bearing, fracture prevention, and early management of scoliosis and cardiac dysfunction. These measures reduce complications rather than correct laminin deficiency. (bouman2023lama2relatedmuscular pages 12-13, sarkozy2020lama2relateddystrophiesclinical pages 6-7)

## 14. Other species and naturally occurring disease

The disease mechanism is conserved across vertebrates. Relevant taxa include **Mus musculus** (NCBI Taxon 10090) and **Danio rerio** (Taxon 7955), with orthologous *Lama2/lama2*. The retrieved evidence primarily concerns induced or spontaneous laboratory mutants rather than a well-characterized naturally occurring veterinary syndrome. No infectious transmission, zoonotic potential, or cross-species contagion exists. (hall2019cellularrescuein pages 1-2, gawlik2020afamilyof pages 1-2)

Naturally arising dy mouse alleles and engineered derivatives demonstrate that laminin-α2’s roles in muscle basement membrane and Schwann-cell myelination are evolutionarily conserved. Direct equivalence to human prognosis is limited by mouse size, lifespan, allele construction, strain background, and much more rapid disease in severe null models.

## 15. Model organisms and experimental systems

**Mouse models.** The dy-family includes spontaneous **dy/dy**, milder **dy2J/dy2J**, and severe **dyW/dyW** and **dy3K/dy3K** models. They reproduce weakness, myofiber degeneration, inflammation, fibrosis, impaired regeneration, contractures/cachexia, and peripheral dysmyelination. dy3K/dy3K typically survives 3–5 weeks, dyW/dyW approximately 5–16 weeks, whereas dy2J/dy2J commonly survives over one year and is practical for longitudinal therapy studies. Sex effects on weight, CK, hydration, and strength in dy2J mice require sex-stratified experimental design. (fernandes2023lama2cmdestablishmentof pages 13-15, gawlik2020afamilyof pages 1-2)

Severe dy3K muscle shows apoptosis by postnatal day 1 and degeneration, inflammation, and ECM deposition by day 4, with maximal deterioration near day 7; severe masticatory involvement and malnutrition contribute to early death. Models have enabled tests of mini-agrin, laminin-α1, linker proteins, AAV, exon skipping/CRISPR, omigapil, losartan, IGF-1, proteasome/autophagy modulation, and anti-fibrotic strategies. Their unusually rapid course may overestimate effect sizes or demand treatment earlier than is feasible clinically. (gawlik2019earlyskeletalmuscle pages 15-16)

**Zebrafish.** Lama2-deficient zebrafish offer optical live imaging, rapid development, large clutch size, and measurable fiber detachment. Live tracking showed detached fibers can retain sarcolemmal integrity, reattach, extend, and hyper-fuse before delayed death; muscle-specific or systemic laminin delivery restored function and promoted stem-cell-mediated regeneration. Limitations include aquatic biomechanics, developmental timing, and uncertain prediction of human systemic delivery. (hall2019cellularrescuein pages 1-2)

**Cellular systems.** Patient fibroblasts, mesoangioblasts, myoblasts, CRISPR-null C2C12 cells, and potentially patient-derived iPSC myotubes support splice assays, protein localization, ECM adhesion studies, and correction experiments. NCT06582537 collected muscle, skin, and blood from seven adults to study ex-vivo correction; it was observational, not patient treatment. Organoid, single-cell, and spatial models remain emerging rather than clinically validated. (martins2024deregulationofmultiple pages 3-6, NCT06582537 chunk 1)

## Key recent sources and exact abstract language

* **Bouman et al., Neurology Genetics, October 2023**, DOI [10.1212/NXG.0000000000200089](https://doi.org/10.1212/NXG.0000000000200089): “Respiratory function was impaired in 85% of patients,” and the authors advise “routine cardiorespiratory follow-up and optimization of bone quality.” PMID was not present in the retrieved record. (bouman2023lama2relatedmuscular pages 1-2)
* **Camelo et al., Journal of Neuromuscular Diseases, published July 4, 2023**, DOI [10.3233/JND-221638](https://doi.org/10.3233/JND-221638): “10 patients (19.2%) presented with cortical malformations,” “10 patients (19.2%) presented with epilepsy,” and eight (15.4%) had intellectual disability. PMID was not available in the retrieved text. (camelo2023brainmriabnormalities pages 1-3)
* **Enzmann et al., Journal of Neuromuscular Diseases, September 3, 2024**, DOI [10.3233/JND-240023](https://doi.org/10.3233/JND-240023): “All patients classified as CMD had symptoms before 12 months of age and 11/14 before the age of six months.” PMID was not present in the retrieved record. (enzmann2024amulticentercrosssectional pages 1-3)
* **Tan et al., Orphanet Journal of Rare Diseases, July 2021**, DOI [10.1186/s13023-021-01950-x](https://doi.org/10.1186/s13023-021-01950-x): “Motor regression in LAMA2-CMD mainly occurred concurrently with rapid progression of contractures during 6–9 years old.” (tan2021naturalhistoryand pages 1-2)
* **Zambon et al., Annals of Clinical and Translational Neurology, September 2020**, DOI [10.1002/acn3.51172](https://doi.org/10.1002/acn3.51172): a 46-patient pediatric natural-history study documenting FVC decline, ventilation, gastrostomy, scoliosis, and mortality. PMID was not supplied by the retrieved record. (zambon2020lama2‐relatedmusculardystrophy pages 1-2)
* **Martins et al., bioRxiv, posted January 24, 2024**, DOI [10.1101/2024.01.20.576409](https://doi.org/10.1101/2024.01.20.576409): preprint evidence that early disease involves “massive” transcriptional downregulation and defective proliferation/differentiation; this evidence is explicitly non-peer-reviewed. (martins2024deregulationofmultiple pages 3-6, martins2024deregulationofmultiple pages 1-3)

## Evidence limitations

MDC1A is rare, and most cohorts combine severe complete-deficiency disease with milder LAMA2-RD. Frequencies therefore depend on referral patterns, age, genotype, and denominator. There are no randomized efficacy data for a disease-modifying therapy, no validated environmental causal factors, no established protective human variants, and limited disease-specific QoL, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or epigenomic data. Exact PMIDs were not visible in the retrieved documents and are therefore not invented; DOI URLs are provided as stable primary-source links.

References

1. (sarkozy2020lama2relateddystrophiesclinical pages 1-2): Anna Sarkozy, A. Reghan Foley, Alberto A. Zambon, Carsten G. Bönnemann, and Francesco Muntoni. Lama2-related dystrophies: clinical phenotypes, disease biomarkers, and clinical trial readiness. Frontiers in Molecular Neuroscience, Aug 2020. URL: https://doi.org/10.3389/fnmol.2020.00123, doi:10.3389/fnmol.2020.00123. This article has 114 citations.

2. (enzmann2024amulticentercrosssectional pages 1-3): Cornelia Enzmann, L. Steiner, Katarzyna Pospieszny, C. Zweier, Kevin Plattner, Dominique Baumann, Bettina C. Henzi, Elea Galiart, Mirjam Fink, D. Jacquier, G. M. Stettner, P. Ripellino, J. Fluss, Andrea Klein, Dominique Cornelia David Hans H. Andrea Claudia E. Andrea Pa Baumann Enzmann Jacquier Jung Klein Kuehni Mathis, Dominique Baumann, Cornelia Enzmann, D. Jacquier, Hans H. Jung, Andrea Klein, C. E. Kuehni, A. Mathis, P. Ripellino, O. Scheidegger, B. Schreiner, E. I. Schwarz, G. M. Stettner, and A. Tscherter. A multicenter cross-sectional study of the swiss cohort of lama2-related muscular dystrophy. Sep 2024. URL: https://doi.org/10.3233/jnd-240023, doi:10.3233/jnd-240023. This article has 6 citations and is from a peer-reviewed journal.

3. (camelo2023brainmriabnormalities pages 1-3): Clara Gontijo Camelo, Mariana Cunha Artilheiro, Cristiane Araújo Martins Moreno, Suely Fazio Ferraciolli, André Macedo Serafim Silva, Tatiana Ribeiro Fernandes, Leandro Tavares Lucato, Antônio José Rocha, Umbertina Conti Reed, and Edmar Zanoteli. Brain mri abnormalities, epilepsy and intellectual disability in lama2 related dystrophy – a genotype/phenotype correlation. Journal of Neuromuscular Diseases, 10:483-492, May 2023. URL: https://doi.org/10.3233/jnd-221638, doi:10.3233/jnd-221638. This article has 20 citations and is from a peer-reviewed journal.

4. (bouman2023lama2relatedmuscular pages 1-2): Karlijn Bouman, Jan T. Groothuis, Jonne Doorduin, Nens van Alfen, Floris E.A. Udink ten Cate, Frederik M.A. van den Heuvel, Robin Nijveldt, Erik-Jan Kamsteeg, Anne T.M. Dittrich, Jos M.T. Draaisma, Mirian C.H. Janssen, Baziel G.M. van Engelen, Corrie E. Erasmus, and Nicol C. Voermans. <i>lama2</i> -related muscular dystrophy across the life span. Oct 2023. URL: https://doi.org/10.1212/nxg.0000000000200089, doi:10.1212/nxg.0000000000200089. This article has 24 citations.

5. (nguyen2019currentunderstandingand pages 1-2): Quynh Nguyen, Kenji Rowel Q Lim, and Toshifumi Yokota. Current understanding and treatment of cardiac and skeletal muscle pathology in laminin-α2 chain-deficient congenital muscular dystrophy. The Application of Clinical Genetics, 12:113-130, Jul 2019. URL: https://doi.org/10.2147/tacg.s187481, doi:10.2147/tacg.s187481. This article has 68 citations.

6. (nguyen2019currentunderstandingand pages 5-6): Quynh Nguyen, Kenji Rowel Q Lim, and Toshifumi Yokota. Current understanding and treatment of cardiac and skeletal muscle pathology in laminin-α2 chain-deficient congenital muscular dystrophy. The Application of Clinical Genetics, 12:113-130, Jul 2019. URL: https://doi.org/10.2147/tacg.s187481, doi:10.2147/tacg.s187481. This article has 68 citations.

7. (nmer2024exploringsplicesitemutations pages 6-7): Samira Nmer, Amina Ameli, Said Trhanint, Sana Chaouki, Laila Bouguenouch, and Karim Ouldim. Exploring splice-site mutations in lama2-related muscular dystrophies: a comprehensive analysis of genotypic and phenotypic patterns. Jun 2024. URL: https://doi.org/10.7759/cureus.61599, doi:10.7759/cureus.61599. This article has 2 citations.

8. (fernandes2023lama2cmdestablishmentof pages 13-15): DR Fernandes. Lama2-cmd: establishment of a new gene therapy strategy using an in vitro model. Unknown journal, 2023.

9. (zambon2020lama2‐relatedmusculardystrophy pages 1-2): Alberto A. Zambon, Deborah Ridout, Marion Main, Rachael Mein, Rahul Phadke, Francesco Muntoni, and Anna Sarkozy. Lama2‐related muscular dystrophy: natural history of a large pediatric cohort. Annals of Clinical and Translational Neurology, 7:1870-1882, Sep 2020. URL: https://doi.org/10.1002/acn3.51172, doi:10.1002/acn3.51172. This article has 50 citations and is from a peer-reviewed journal.

10. (sarkozy2020lama2relateddystrophiesclinical pages 6-7): Anna Sarkozy, A. Reghan Foley, Alberto A. Zambon, Carsten G. Bönnemann, and Francesco Muntoni. Lama2-related dystrophies: clinical phenotypes, disease biomarkers, and clinical trial readiness. Frontiers in Molecular Neuroscience, Aug 2020. URL: https://doi.org/10.3389/fnmol.2020.00123, doi:10.3389/fnmol.2020.00123. This article has 114 citations.

11. (bouman2023lama2relatedmuscular pages 12-13): Karlijn Bouman, Jan T. Groothuis, Jonne Doorduin, Nens van Alfen, Floris E.A. Udink ten Cate, Frederik M.A. van den Heuvel, Robin Nijveldt, Erik-Jan Kamsteeg, Anne T.M. Dittrich, Jos M.T. Draaisma, Mirian C.H. Janssen, Baziel G.M. van Engelen, Corrie E. Erasmus, and Nicol C. Voermans. <i>lama2</i> -related muscular dystrophy across the life span. Oct 2023. URL: https://doi.org/10.1212/nxg.0000000000200089, doi:10.1212/nxg.0000000000200089. This article has 24 citations.

12. (tan2021naturalhistoryand pages 1-2): Dandan Tan, Lin Ge, Yanbin Fan, Xingzhi Chang, Shuang Wang, Cuijie Wei, Juan Ding, Aijie Liu, Shuo Wang, Xueying Li, Kai Gao, Haipo Yang, Chengli Que, Zhen Huang, Chunde Li, Ying Zhu, Bing Mao, Bo Jin, Ying Hua, Xiaoli Zhang, Bingbing Zhang, Wenhua Zhu, Cheng Zhang, Yanjuan Wang, Yun Yuan, Yuwu Jiang, Anne Rutkowski, Carsten G. Bönnemann, Xiru Wu, and Hui Xiong. Natural history and genetic study of lama2-related muscular dystrophy in a large chinese cohort. Orphanet Journal of Rare Diseases, Jul 2021. URL: https://doi.org/10.1186/s13023-021-01950-x, doi:10.1186/s13023-021-01950-x. This article has 42 citations and is from a peer-reviewed journal.

13. (NCT06132750 chunk 1):  A 5-year Natural History Study in LAMA2-related Muscular Dystrophy and SELENON-related Myopathy.. Radboud University Medical Center. 2023. ClinicalTrials.gov Identifier: NCT06132750

14. (NCT06582537 chunk 1):  LAMA2 Genetic Correction. Maastricht University. 2020. ClinicalTrials.gov Identifier: NCT06582537

15. (NCT04478981 chunk 1):  The Natural History of Patients With Mutations in SEPN1 (SELENON) or LAMA2. Radboud University Medical Center. 2020. ClinicalTrials.gov Identifier: NCT04478981

16. (NCT04299321 chunk 1):  Retrospective Natural History Study of Infants and Toddlers With LAMA2-CMD. Prothelia, Inc.. 2020. ClinicalTrials.gov Identifier: NCT04299321

17. (gawlik2019earlyskeletalmuscle pages 15-16): Kinga I. Gawlik, Zandra Körner, Bruno M. Oliveira, and Madeleine Durbeej. Early skeletal muscle pathology and disease progress in the dy3k/dy3k mouse model of congenital muscular dystrophy with laminin α2 chain-deficiency. Scientific Reports, Oct 2019. URL: https://doi.org/10.1038/s41598-019-50550-0, doi:10.1038/s41598-019-50550-0. This article has 24 citations and is from a peer-reviewed journal.

18. (gawlik2020afamilyof pages 1-2): Kinga I. Gawlik and Madeleine Durbeej. A family of laminin α2 chain-deficient mouse mutants: advancing the research on lama2-cmd. Frontiers in Molecular Neuroscience, Apr 2020. URL: https://doi.org/10.3389/fnmol.2020.00059, doi:10.3389/fnmol.2020.00059. This article has 47 citations.

19. (martins2024deregulationofmultiple pages 3-6): Susana G Martins, Vanessa Ribeiro, Catarina Melo, Cláudia Paulino-Cavaco, Dario Antonini, Sharadha Dayalan Naidu, Fernanda Murtinheira, Inês Fonseca, Bérénice Saget, Mafalda Pita, Diogo R Fernandes, Pedro G dos Santos, Gabriela Rodrigues, Rita Zilhão, Federico Herrera, Albena T Dinkova-Kostova, Ana Rita Carlos, and Sólveig Thorsteinsdóttir. Deregulation of multiple mechanisms shapes the onset of<i>lama2</i>-congenital muscular dystrophy. Jan 2024. URL: https://doi.org/10.1101/2024.01.20.576409, doi:10.1101/2024.01.20.576409. This article has 2 citations.

20. (hall2019cellularrescuein pages 1-2): T. Hall, T. Hall, A. Wood, O. Ehrlich, Mei Li, C. Sonntag, N. Cole, N. Cole, I. Huttner, T. Sztal, T. Sztal, P. Currie, and P. Currie. Cellular rescue in a zebrafish model of congenital muscular dystrophy type 1a. npj Regenerative Medicine, Nov 2019. URL: https://doi.org/10.1038/s41536-019-0084-5, doi:10.1038/s41536-019-0084-5. This article has 30 citations and is from a peer-reviewed journal.

21. (martins2024deregulationofmultiple pages 1-3): Susana G Martins, Vanessa Ribeiro, Catarina Melo, Cláudia Paulino-Cavaco, Dario Antonini, Sharadha Dayalan Naidu, Fernanda Murtinheira, Inês Fonseca, Bérénice Saget, Mafalda Pita, Diogo R Fernandes, Pedro G dos Santos, Gabriela Rodrigues, Rita Zilhão, Federico Herrera, Albena T Dinkova-Kostova, Ana Rita Carlos, and Sólveig Thorsteinsdóttir. Deregulation of multiple mechanisms shapes the onset of<i>lama2</i>-congenital muscular dystrophy. Jan 2024. URL: https://doi.org/10.1101/2024.01.20.576409, doi:10.1101/2024.01.20.576409. This article has 2 citations.

22. (martins2024deregulationofmultiple pages 10-12): Susana G Martins, Vanessa Ribeiro, Catarina Melo, Cláudia Paulino-Cavaco, Dario Antonini, Sharadha Dayalan Naidu, Fernanda Murtinheira, Inês Fonseca, Bérénice Saget, Mafalda Pita, Diogo R Fernandes, Pedro G dos Santos, Gabriela Rodrigues, Rita Zilhão, Federico Herrera, Albena T Dinkova-Kostova, Ana Rita Carlos, and Sólveig Thorsteinsdóttir. Deregulation of multiple mechanisms shapes the onset of<i>lama2</i>-congenital muscular dystrophy. Jan 2024. URL: https://doi.org/10.1101/2024.01.20.576409, doi:10.1101/2024.01.20.576409. This article has 2 citations.

23. (NCT06503367 chunk 2): Anne M. Connolly. Observation Study in Patients Age 0-5 Years With LAMA2-related Congenital Muscular Dystrophy. Nationwide Children's Hospital. 2025. ClinicalTrials.gov Identifier: NCT06503367

## Artifacts

- [Edison artifact artifact-00](Congenital_Merosin-deficient_Muscular_Dystrophy_1A-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011925` (3 mentions) - the report calls it "if available"; MONDO calls it **congenital merosin-deficient muscular dystrophy 1A**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.