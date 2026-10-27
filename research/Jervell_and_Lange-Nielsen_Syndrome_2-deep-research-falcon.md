---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T14:39:37.841079'
end_time: '2026-09-06T14:51:45.841987'
duration_seconds: 728.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Jervell and Lange-Nielsen Syndrome 2
  mondo_id: MONDO:0012871
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 0
  quotes_valid: 0
  quotes_not_checkable: 1
  relevance_assessed: 7
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 33
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0012871
    reported_labels:
    - if available
    ontology_label: Jervell and Lange-Nielsen syndrome 2
  labels_variant: 1
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
  path: Jervell_and_Lange-Nielsen_Syndrome_2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Jervell and Lange-Nielsen Syndrome 2
- **MONDO ID:** MONDO:0012871 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Jervell and Lange-Nielsen Syndrome 2** covering all of the
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
- **Disease Name:** Jervell and Lange-Nielsen Syndrome 2
- **MONDO ID:** MONDO:0012871 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Jervell and Lange-Nielsen Syndrome 2** covering all of the
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


# Jervell and Lange-Nielsen Syndrome 2 (JLNS2): Disease Characteristics Report

## Executive summary

Jervell and Lange-Nielsen syndrome type 2 (JLNS2) is an exceptionally rare, autosomal-recessive cardio-auditory channelopathy caused by **biallelic pathogenic loss-of-function variants in KCNE1**. Its defining manifestations are congenital, usually profound bilateral sensorineural hearing loss and delayed ventricular repolarization, manifested by QT prolongation and susceptibility to torsades de pointes, syncope, cardiac arrest, and sudden cardiac death. JLNS2 must be distinguished from **KCNQ1-related JLNS1** and from heterozygous KCNE1-associated long-QT syndrome type 5 (LQT5/Romano-Ward syndrome). Available evidence suggests that the cardiac phenotype of JLNS2 is, on average, milder than JLNS1, but individual patients can still have life-threatening arrhythmias. The largest clearly subtype-separated cohort identified contained only 19 JLNS2 patients, illustrating the limited evidence base. (roberts2020aninternationalmulticenter pages 1-5, faridi2019mutationalandphenotypic pages 1-3)

| Domain | JLNS2-specific finding | Key quantitative data | Evidence type/source |
|---|---|---|---|
| Identity | Jervell and Lange-Nielsen syndrome type 2 is the recessive, cardio-auditory **KCNE1** channelopathy; identifiers include **MONDO:0012871** and **OMIM:612347**. It is distinct from KCNQ1-related JLNS1 and heterozygous KCNE1-associated LQT5/Romano-Ward syndrome. | Open Targets associates MONDO:0012871 most strongly with KCNE1 (association score 0.769). | Aggregated disease/target resources and human genetic literature (OpenTargets Search: Jervell and Lange-Nielsen syndrome 2-KCNE1, faridi2019mutationalandphenotypic pages 1-3) |
| Cause and inheritance | **Biallelic germline loss-of-function KCNE1 variants**—homozygous or compound heterozygous—cause autosomal-recessive JLNS2. Heterozygous loss-of-function carriers may have a normal QT interval; some heterozygous missense variants instead cause incompletely penetrant LQT5, sometimes through dominant-negative effects. | Recurrence risk for two carrier parents: 25% affected, 50% carrier, and 25% unaffected/non-carrier per pregnancy. Heterozygous KCNE1-family-member ECG penetrance in a multicenter LQT5 study was 20.7% (29/140), but this is not JLNS2 penetrance. | Human pedigrees, functional interpretation, and international cohort (roberts2020aninternationalmulticenter pages 1-5, faridi2019mutationalandphenotypic pages 1-3, faridi2019mutationalandphenotypic pages 6-8) |
| Core phenotype | Defining manifestations are **congenital bilateral profound sensorineural hearing loss** and QT prolongation caused by delayed ventricular repolarization. Possible episodic consequences include exertion- or emotion-triggered torsades de pointes, syncope, seizure-like events, ventricular fibrillation, cardiac arrest, and sudden death. | The defining hearing phenotype is congenital and generally profound; robust JLNS2-specific percentages for individual manifestations are unavailable. | Human families and clinical cohorts (roberts2020aninternationalmulticenter pages 1-5, faridi2019mutationalandphenotypic pages 1-3, theodore2024icdimplantin pages 1-3) |
| Relative frequency | JLNS2 is much less common than KCNQ1-related JLNS1. Historical summaries estimate KCNE1 in approximately 10% of JLNS, but contemporary cohorts suggest a smaller fraction. | Approximate historical distribution: JLNS1 90%, JLNS2 10%. KCNE1 accounted for 1/52 sequenced patients (1.9%) in a 2025 Egyptian preprint and approximately 5% in a cited earlier cohort. | Aggregated historical evidence and cohort/preprint; estimates vary with ascertainment and ancestry (vojdani2019mutationscreeningof pages 7-10, hataba2025themutationalspectrum pages 14-17, rieraUnknownyearjervellandlangenielsen pages 1-3) |
| Relative severity | Available evidence indicates **KCNE1-related JLNS2 is generally milder cardiologically than KCNQ1-related JLNS1**, although life-threatening arrhythmia remains possible and small samples limit precision. | International cohort: definite arrhythmic events in 2/19 JLNS2 patients (10.5%); versus the overall heterozygous KCNE1 cohort, HR 1.7 (95% CI 0.3–10.8; p=0.590). One report cites approximately sixfold higher arrhythmic-event risk in KCNQ1-related JLNS than KCNE1-related disease. | International multicenter human cohort and secondary comparison (roberts2020aninternationalmulticenter pages 1-5, qiu2020jervellandlangenielsen pages 5-7) |
| Pathogenic variants | Reported JLNS2 alleles include nonsense/null and missense variants. Well-documented homozygous nonsense alleles include **KCNE1 c.50G>A (p.Trp17\*)**, **c.51G>A (p.Trp17\*)**, and **c.138C>A (p.Tyr46\*)**. Variant interpretation must distinguish pathogenic biallelic loss from common polymorphisms such as p.Ser38Gly. | A 2019 review noted only four previously associated JLNS variants before adding three homozygous nonsense alleles; the catalog is therefore sparse. No universal disease allele frequency is established. | Human pedigrees, segregation, and variant review (faridi2019mutationalandphenotypic pages 1-3, faridi2019mutationalandphenotypic pages 6-8, vojdani2019mutationscreeningof pages 4-7) |
| Cardiac mechanism | KCNE1/minK is the regulatory β-subunit of the KCNQ1/Kv7.1 complex generating the slowly activating delayed-rectifier potassium current **I-Ks**. Biallelic loss reduces repolarizing K⁺ current, prolongs cardiomyocyte action-potential duration, produces QT prolongation, and increases early-afterdepolarization/torsades susceptibility, especially under adrenergic stress. | KCNE1 is a 130-amino-acid, single-pass transmembrane protein. KCNE1-associated current reductions are often more modest than severe KCNQ1 defects, consistent with the milder average JLNS2 cardiac phenotype. | Human genetics plus electrophysiologic/channel-biology evidence (roberts2020aninternationalmulticenter pages 1-5, vojdani2019mutationscreeningof pages 7-10, rieraUnknownyearjervellandlangenielsen pages 12-15) |
| Cochlear mechanism | Apical KCNQ1–KCNE1 channels in **stria vascularis marginal cells** secrete K⁺ into scala-media endolymph. KCNE1 deficiency disrupts K⁺ homeostasis and the positive endocochlear potential needed to drive hair-cell mechanotransduction, resulting in congenital sensorineural deafness; secondary strial and sensory-cell degeneration may contribute. | No reliable human JLNS2-specific endocochlear-potential measurements or cell-loss percentages are available. | Mechanistic review and mouse-based inner-ear evidence; human phenotype supplies clinical concordance (rieraUnknownyearjervellandlangenielsen pages 12-15, faridi2019mutationalandphenotypic pages 12-14) |
| Diagnosis | Suspect JLNS2 in any child with congenital profound bilateral hearing loss plus QTc prolongation, unexplained exertional/emotional syncope, seizure-like events, or family history of sudden death. Evaluate serial 12-lead ECG/QTc, T-wave morphology, Holter/exercise response, electrolytes and acquired causes, formal audiology, and molecular confirmation of **two pathogenic/likely pathogenic KCNE1 alleles in trans**. | JLNS overall usually has QTc >500 ms; this threshold is supportive, not independently diagnostic and not JLNS2-specific. | Clinical diagnostic literature and disease reviews (rieraUnknownyearjervellandlangenielsen pages 6-9, rieraUnknownyearjervellandlangenielsen pages 1-3, theodore2024icdimplantin pages 3-4) |
| Genetic testing | Use a validated LQTS/cardio-auditory or comprehensive hearing-loss panel containing **KCNE1 and KCNQ1**, with sequencing plus deletion/duplication analysis. If negative despite a convincing phenotype, consider CNV-sensitive exome/genome analysis and reanalysis; test parents for phase and cascade-test relatives. | CNVs can be missed by sequence-only assays. In 2024 literature plus an internal channelopathy cohort, CNVs were reported across 140 patients, supporting dedicated CNV detection, although this was not a JLNS2-specific yield estimate. | Diagnostic reviews and aggregated channelopathy studies (rieraUnknownyearjervellandlangenielsen pages 3-6) |
| Management | Treat the cardiac phenotype according to congenital-LQTS guidance: nonselective β-blockade—typically nadolol or propranolol—plus strict avoidance of QT-prolonging drugs, prompt correction of hypokalemia/hypomagnesemia, fever/dehydration management, individualized exercise precautions, and an emergency plan. Consider **LCSD** for events despite adequate β-blockade or β-blocker intolerance and an **ICD** after cardiac arrest or for persistent high-risk disease. | JLNS2-specific drug-response rates are unavailable. Historical poor outcomes on β-blocker monotherapy largely derive from mixed, predominantly KCNQ1-related JLNS and should not be assigned directly to JLNS2. | LQTS guidelines/reviews extrapolated to JLNS2, supplemented by JLNS cases (rieraUnknownyearjervellandlangenielsen pages 6-9, theodore2024icdimplantin pages 1-3, theodore2024icdimplantin pages 3-4) |
| Hearing intervention | Early audiologic rehabilitation and **cochlear implantation** can restore useful auditory access when hearing aids are inadequate. Implantation requires multidisciplinary cardiology–anesthesia planning, continuation of protective therapy when feasible, electrolyte control, avoidance of QT-prolonging anesthetic combinations, continuous monitoring, and immediate defibrillation capability. | Good auditory outcomes are reported, but subtype-specific response percentages are lacking. Life-threatening perioperative arrhythmia has been reported in JLNS, especially around anesthesia/emergence. | Human case series/reports; most do not genotype-separate JLNS2 from JLNS1 (qiu2020jervellandlangenielsen pages 5-7, theodore2024icdimplantin pages 1-3) |
| Prognosis | Hearing loss is lifelong but functionally treatable; cardiac risk is lifelong and episodic. JLNS2 appears less malignant on average than JLNS1, but sudden cardiac arrest remains possible, so genotype alone must not justify withholding clinical surveillance or treatment when QT prolongation is present. | Best subtype-specific cohort: 10.5% definite arrhythmic events (2/19), with wide uncertainty. JLNS-wide estimates such as 50% experiencing events before age three or high childhood mortality mainly reflect mixed/predominantly JLNS1 cohorts. | International JLNS2 cohort plus historical mixed-JLNS natural history (roberts2020aninternationalmulticenter pages 1-5, rieraUnknownyearjervellandlangenielsen pages 3-6, rieraUnknownyearjervellandlangenielsen pages 1-3) |
| Models | **Kcne1-null mice** reproduce bilateral deafness/endocochlear dysfunction and provide mechanistic evidence, but their cardiac phenotype is relatively mild because murine ventricular repolarization differs from humans. Patient-specific JLNS iPSC-cardiomyocyte studies demonstrate reduced I-Ks, prolonged action potentials, adrenergic/drug sensitivity, and pharmacologic rescue, but the landmark model used **KCNQ1**, not KCNE1, and therefore models JLNS1 rather than JLNS2 directly. | No well-validated KCNE1-JLNS2 patient-derived iPSC, organoid, or single-cell disease model was identified in the reviewed evidence. | Knockout mouse and KCNQ1-JLNS iPSC experimental studies; indirect for human JLNS2 cardiac severity (zhang2014recessivecardiacphenotypes pages 1-2, faridi2019mutationalandphenotypic pages 12-14) |
| Evidence gaps | JLNS2 evidence is constrained by very small cohorts, historical mixing of JLNS1 and JLNS2, changing KCNE1 variant classification, and limited functional testing. Disease-specific incidence, penetrance, sex effects, founder alleles, modifier genes, quality-of-life measures, treatment-effect estimates, epigenomic/omics signatures, and approved gene/RNA therapies remain undetermined. | Largest clearly subtype-separated clinical cohort identified: **19 JLNS2 patients**. No JLNS2-specific interventional clinical trial was established in the reviewed evidence. | Evidence synthesis and international cohort (roberts2020aninternationalmulticenter pages 1-5, faridi2019mutationalandphenotypic pages 6-8, zhang2014recessivecardiacphenotypes pages 1-2) |


*Table: Compact evidence matrix separating biallelic KCNE1-related JLNS2 from KCNQ1-related JLNS1 and heterozygous LQT5. It highlights quantitative findings, clinical implications, model limitations, and major knowledge gaps.*

## 1. Disease information

**Definition.** JLNS2 is a Mendelian disorder in which biallelic KCNE1 deficiency impairs the KCNQ1–KCNE1 slowly activating delayed-rectifier potassium channel, affecting both ventricular repolarization and cochlear potassium homeostasis. Faridi et al. describe the syndrome as a “cardio-auditory syndrome characterized by congenital profound sensorineural deafness and a prolonged QT interval that can cause ventricular arrhythmias and sudden cardiac death.” [Human genetic/review evidence; published December 2019; PMID **30461122**; DOI/URL: https://doi.org/10.1002/humu.23689]. (faridi2019mutationalandphenotypic pages 1-3)

**Identifiers and names.** 

- MONDO: **MONDO:0012871**.
- OMIM phenotype: **612347**.
- Causal gene: **KCNE1**, HGNC:6240; NCBI Gene: 3753; Ensembl: ENSG00000180509.
- Synonyms: *Jervell and Lange-Nielsen syndrome type 2*, *JLNS2*, *Jervell-Lange Nielsen syndrome 2*, *KCNE1-related Jervell and Lange-Nielsen syndrome*, and *recessive KCNE1-associated cardio-auditory syndrome*.
- Parent disease concepts include Jervell and Lange-Nielsen syndrome (MONDO:0002441) and familial long-QT syndrome. Open Targets ranks KCNE1 as the principal supported target for MONDO:0012871; low-scoring neighboring-gene associations should not be interpreted as additional causal genes. (OpenTargets Search: Jervell and Lange-Nielsen syndrome 2-KCNE1)
- No dedicated, universally used JLNS2-specific ICD-10 or MeSH code was identified. Coding ordinarily uses broader congenital long-QT syndrome and sensorineural hearing-loss categories. ICD-11 similarly does not reliably separate the molecular subtype in routine records.

This report synthesizes **aggregated disease-level resources, published families, registries, and experimental models**. It is not based on an individual EHR. Case reports are identified where used.

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Primary cause

The necessary initiating lesion is generally two germline pathogenic or likely pathogenic **KCNE1** alleles in trans—homozygous or compound heterozygous. KCNE1 encodes minK, a 130-amino-acid single-pass membrane regulatory subunit of the KCNQ1/Kv7.1 channel complex. Biallelic null or severe loss-of-function alleles cause JLNS2; some heterozygous missense alleles can instead produce incompletely penetrant LQT5 through dominant-negative or other functional effects. Heterozygous null carriers may have a normal QT interval. (roberts2020aninternationalmulticenter pages 1-5, faridi2019mutationalandphenotypic pages 1-3, faridi2019mutationalandphenotypic pages 6-8)

### Risk factors

- **Genetic:** biallelic pathogenic KCNE1 variants, parental carrier status, consanguinity, and family history of congenital deafness, unexplained syncope, or sudden death. Consanguinity increases the probability that a rare allele is inherited identically by descent but is not itself mechanistic. (vojdani2019mutationscreeningof pages 7-10, hataba2025themutationalspectrum pages 14-17)
- **Arrhythmia triggers/modifiers:** exertion, acute emotion/adrenergic activation, electrolyte depletion—especially hypokalemia or hypomagnesemia—and QT-prolonging medications can expose reduced repolarization reserve. Anesthesia, emergence, postoperative stress, and interacting medicines are particularly relevant during cochlear implantation. These factors trigger cardiac events; they do not cause the inherited syndrome. (qiu2020jervellandlangenielsen pages 5-7, theodore2024icdimplantin pages 1-3, theodore2024icdimplantin pages 3-4)
- **Age/sex:** severe events may begin in early childhood. No robust JLNS2-specific sex effect is established. A recent mixed-JLNS Egyptian cohort found no sex-related QTc difference, but only one KCNE1-positive patient precluded subtype analysis. (hataba2025themutationalspectrum pages 14-17)

### Protective factors

No protective KCNE1 allele has been validated for JLNS2. Clinically protective measures include effective nonselective beta-blockade, avoidance of QT-prolonging drugs, maintenance of potassium and magnesium, prompt treatment of vomiting/dehydration, and escalation to left cardiac sympathetic denervation (LCSD) or an implantable cardioverter-defibrillator (ICD) when indicated. These reduce event risk rather than reverse the genotype. (rieraUnknownyearjervellandlangenielsen pages 6-9, theodore2024icdimplantin pages 1-3)

No disease-specific effects of diet, smoking, alcohol, occupational exposure, infection, radiation, or toxins are established. There is no infectious cause and no vaccine prevention strategy.

## 3. Phenotypes

| Phenotype | Type, onset, course, and frequency | Suggested HPO term |
|---|---|---|
| Bilateral profound sensorineural hearing loss | Clinical sign; congenital/prelingual, usually severe-to-profound and permanent; defining phenotype, although rigorous JLNS2 frequency estimates are unavailable | Bilateral sensorineural hearing impairment, **HP:0008619**; congenital sensorineural hearing impairment, **HP:0008527**; profound hearing impairment, **HP:0012715** |
| Prolonged QTc | ECG abnormality; congenital, persistent but quantitatively variable; defining cardiac manifestation. JLNS generally often has QTc >500 ms, but this is not an absolute JLNS2 criterion | Prolonged QT interval, **HP:0001657** |
| Torsades/polymorphic ventricular tachycardia | Episodic clinical/electrophysiologic event, often adrenergically triggered; frequency is unknown specifically for JLNS2 | Ventricular tachycardia, **HP:0004756** |
| Syncope | Episodic symptom, often during exercise or emotion; may begin in early childhood | Syncope, **HP:0001279**; exercise-induced syncope, **HP:0012665** |
| Seizure-like episodes | Behavioral/neurologic appearance caused by cerebral hypoperfusion rather than primary epilepsy in many cases | Seizure, **HP:0001250**, annotated cautiously; cerebral hypoperfusion is the mechanism |
| Ventricular fibrillation/cardiac arrest/sudden death | Severe episodic complication | Ventricular fibrillation, **HP:0001663**; cardiac arrest, **HP:0001695**; sudden cardiac death, **HP:0001645** |
| T-wave abnormalities/alternans | ECG sign indicating electrical instability | Abnormal T-wave, **HP:0005135**; T-wave alternans where supported |
| Fetal/neonatal bradycardia | Occasional presenting sign in JLNS, not quantified for JLNS2 | Bradycardia, **HP:0001662** |

In an international study, definite arrhythmic events occurred in **2/19 JLNS2 patients (10.5%)**. The hazard ratio versus the overall heterozygous KCNE1 cohort was 1.7 (95% CI 0.3–10.8; p=0.590), emphasizing both a comparatively mild average phenotype and very wide uncertainty. [Human multicenter cohort; February 2020; PMID **31983240**; DOI: https://doi.org/10.1161/CIRCULATIONAHA.119.043114]. (roberts2020aninternationalmulticenter pages 1-5)

Hearing loss compromises speech, language development, education, communication, and social participation. Cardiac uncertainty, exercise restrictions, recurrent syncope, ICD shocks, and fear of sudden death can affect daily functioning. No JLNS2-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life dataset was identified.

## 4. Genetic and molecular information

**Causal gene.** KCNE1 is the only established causal gene for the type-2 entity. KCNQ1 causes JLNS1, not JLNS2. Open Targets cites supporting literature including PMIDs **9354802**, **10400998**, **16414944**, **30461122**, and **31983240**. (OpenTargets Search: Jervell and Lange-Nielsen syndrome 2-KCNE1)

**Reported pathogenic variants.** Well-supported homozygous nonsense alleles include **NM_000219.5:c.50G>A (p.Trp17Ter)**, **c.51G>A (p.Trp17Ter)**, and **c.138C>A (p.Tyr46Ter)**. These predict early truncation/nonsense-mediated loss or absence of functional minK and segregated with JLNS2 in families initially ascertained for apparently nonsyndromic deafness. The abstract states: “heterozygotes for loss-of-function variants of KCNE1 may have normal QT intervals while biallelic null alleles are associated with JLNS2.” (faridi2019mutationalandphenotypic pages 1-3)

Reported classes include nonsense, missense, splice-altering, frameshift, and potentially exon-level deletion/duplication variants. Classification must be variant-specific under ACMG/AMP criteria and should integrate allele frequency, segregation, phase, phenotype, and functional data. Common polymorphisms—such as **p.Ser38Gly/rs1805127**—must not be labeled causal merely because they occur in a JLNS patient. (faridi2019mutationalandphenotypic pages 6-8, vojdani2019mutationscreeningof pages 4-7)

Pathogenic JLNS2 variants are germline, not somatic. They are expected to be absent or extremely rare in population databases, but no single JLNS2-wide allele frequency is meaningful. A 2020 study found rare KCNE1 variants collectively much more common in gnomAD than expected for monogenic LQT5, demonstrating that rarity alone is insufficient evidence of pathogenicity. (roberts2020aninternationalmulticenter pages 1-5)

**Modifiers.** Reduced repolarization reserve and adrenergic state modify expression. No modifier gene is definitively validated specifically for JLNS2. Candidate LQTS modifiers and channel-interacting proteins should not yet be entered as causal genes. No reproducible disease-specific methylation, histone, chromatin, or other epigenetic signature is known. Large chromosomal rearrangements are not characteristic, although intragenic KCNE1 CNVs are diagnostically possible.

## 5. Environmental information

JLNS2 is not environmentally caused. Non-genetic factors affect **event probability**: QT-prolonging medicines, drug interactions, electrolyte disturbance, starvation/vomiting, dehydration, intense exertion, sudden emotional stress, and perioperative sympathetic surges can aggravate delayed repolarization. No infectious agent, pollution exposure, occupational toxin, smoking pattern, diet, or alcohol exposure has a proven etiologic role. (qiu2020jervellandlangenielsen pages 5-7, theodore2024icdimplantin pages 1-3)

Relevant chemical ontology annotations include potassium ion (**CHEBI:29103**) and magnesium ion (**CHEBI:18420**). Drug annotations should use the exact chemical entity and CredibleMeds risk category rather than treating “QT-prolonging drug” as one compound.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic KCNE1 loss-of-function variants lead to** absent, truncated, mistrafficked, or dysfunctional minK subunits.
2. **Defective minK leads to** impaired assembly, membrane expression, gating, or regulation of KCNQ1–KCNE1 channels and reduced **I-Ks** current.
3. **Cardiac branch:** reduced I-Ks in ventricular cardiomyocytes **leads to** slower phase-3 repolarization and prolonged action-potential duration.
4. Prolonged action potentials **result in** QTc prolongation and reduced repolarization reserve.
5. Adrenergic stress, QT-prolonging drugs, or electrolyte depletion **can then lead to** early afterdepolarizations and spatial/temporal dispersion of repolarization; this step is strongly supported by general LQTS electrophysiology but is partly inferred for individual JLNS2 variants.
6. Triggered activity and re-entry **lead to** torsades de pointes/polymorphic ventricular tachycardia, syncope, ventricular fibrillation, cardiac arrest, or sudden death.
7. **Cochlear branch:** defective KCNQ1–KCNE1 channels on the apical membrane of stria-vascularis marginal cells **lead to** impaired K⁺ secretion into scala-media endolymph.
8. Impaired K⁺ homeostasis **results in** failure of the positive endocochlear potential required for hair-cell mechanotransduction.
9. Reduced electrochemical drive, with secondary strial or sensory-cell degeneration demonstrated mainly in models, **leads to** congenital profound sensorineural deafness. (roberts2020aninternationalmulticenter pages 1-5, rieraUnknownyearjervellandlangenielsen pages 12-15, faridi2019mutationalandphenotypic pages 12-14)

This is an ion-channel/homeostatic disorder, not primarily an inflammatory, immune, neoplastic, fibrotic, or metabolic disease. Suggested GO annotations include voltage-gated potassium-channel activity (**GO:0005249**), potassium-ion transmembrane transport (**GO:0071805**), regulation of membrane potential (**GO:0042391**), ventricular cardiac-muscle-cell action-potential repolarization (**GO:0099622**), and sensory perception of sound (**GO:0007605**). Cellular-component terms include plasma membrane (**GO:0005886**) and voltage-gated potassium-channel complex (**GO:0008076**).

Relevant cell types are ventricular cardiomyocytes (**CL:0000746**), cochlear hair cells, and stria-vascularis marginal epithelial cells; the latter lacks consistently used high-granularity CL coverage and may require an ontology extension. No JLNS2-specific transcriptomic, proteomic, metabolomic, lipidomic, spatial-transcriptomic, single-cell, or multi-omic disease signature was identified.

## 7. Anatomical structures affected

The primary organs are the **heart** and **inner ear**. The heart is usually structurally normal; dysfunction is electrical, centered on ventricular myocardium and cardiomyocyte sarcolemma. Suggested anatomy terms include heart (**UBERON:0000948**), cardiac ventricle (**UBERON:0002082**), myocardium (**UBERON:0002349**), inner ear (**UBERON:0001846**), cochlea (**UBERON:0001844**), cochlear duct/scala media, stria vascularis, and organ of Corti. Hearing loss is ordinarily bilateral without lateralization. Secondary nervous-system manifestations—collapse/syncope or convulsive movements—result from transient cerebral hypoperfusion rather than primary brain pathology. (faridi2019mutationalandphenotypic pages 1-3, rieraUnknownyearjervellandlangenielsen pages 12-15)

## 8. Temporal development

Hearing loss is congenital, bilateral, and lifelong. QT prolongation is congenital, but arrhythmic manifestations are intermittent and may first appear in infancy or childhood. A mixed, predominantly JLNS1 historical cohort had mean QTc **557±65 ms**, with 50% experiencing a cardiac event before age three; more than half of untreated children were reported to die before age 15. These severe figures must **not** be assigned directly to JLNS2, which appears less malignant. (rieraUnknownyearjervellandlangenielsen pages 3-6, rieraUnknownyearjervellandlangenielsen pages 1-3)

There is no remission of the genotype or deafness. Cardiac event risk can be markedly reduced by sustained treatment, while cochlear implantation can improve auditory function without repairing the molecular defect. Childhood is a critical period for ECG recognition, speech/language intervention, family screening, and protection during anesthesia.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two heterozygous carrier parents, each pregnancy has a 25% probability of an affected child, 50% probability of a carrier, and 25% probability of a child inheriting neither familial allele. Genetic anticipation is not expected. Germline mosaicism has not emerged as a characteristic mechanism. Expressivity is variable, particularly for QTc and arrhythmic events; penetrance of congenital profound deafness appears high for severe biallelic loss, but an exact JLNS2 estimate is unavailable. (roberts2020aninternationalmulticenter pages 1-5, faridi2019mutationalandphenotypic pages 1-3)

JLNS overall has been estimated at approximately **1 per 200,000 to 1 per 1,000,000**, with higher prevalence in founder or consanguineous populations. JLNS2 is only a fraction of this total. Historical summaries assigned about 10% of JLNS to KCNE1, whereas contemporary subtype data include 19 international patients and only 1 KCNE1 case among 52 sequenced Egyptian patients; therefore, precise prevalence and incidence cannot be calculated. Both sexes are affected. (roberts2020aninternationalmulticenter pages 1-5, vojdani2019mutationscreeningof pages 7-10, hataba2025themutationalspectrum pages 14-17)

No universally established JLNS2 founder variant, sex ratio, annual incidence, or carrier frequency was identified. Consanguinity enriches homozygosity: a 2025 Egyptian JLNS preprint reported consanguinity in 76.2% of families with complete information, but 51/52 sequenced patients had KCNQ1 disease, limiting relevance to JLNS2. (hataba2025themutationalspectrum pages 14-17)

## 10. Diagnostics

**Clinical workflow.** Every child with congenital severe/profound bilateral sensorineural hearing loss should have a 12-lead ECG with manually verified QTc. Conversely, a child with QT prolongation and syncope/seizure-like events should undergo formal audiology. Assessment should include T-wave morphology, resting and serial ECGs, Holter monitoring and exercise/recovery testing where appropriate, electrolytes, medication review, three-generation pedigree, and evaluation for acquired QT prolongation. A QTc commonly exceeding 500 ms is highly supportive in the classic syndrome, but diagnosis must integrate phenotype and genotype. (rieraUnknownyearjervellandlangenielsen pages 6-9, rieraUnknownyearjervellandlangenielsen pages 1-3, theodore2024icdimplantin pages 3-4)

**Molecular confirmation.** Use a validated congenital-LQTS/cardio-auditory or comprehensive hearing-loss panel containing at least **KCNE1 and KCNQ1**, with sequencing and deletion/duplication analysis. Confirm two pathogenic/likely pathogenic KCNE1 variants in trans by parental testing. CNV-sensitive analysis is important because sequence-only assays can miss exon-level deletions or duplications. WES/WGS is useful when panel testing is negative, for noncoding/structural variants and phenocopies, but does not replace careful KCNE1 interpretation. CMA, karyotype, FISH, mitochondrial, and repeat-expansion testing are not routine unless another phenotype indicates them. (rieraUnknownyearjervellandlangenielsen pages 3-6)

**Differential diagnosis:** JLNS1 (biallelic KCNQ1); heterozygous LQT5/Romano-Ward syndrome without congenital profound deafness; nonsyndromic genetic deafness such as GJB2-related DFNB1; Pendred, Usher, Waardenburg, and branchio-oto-renal syndromes; acquired drug/electrolyte-related long QT; catecholaminergic polymorphic ventricular tachycardia; epilepsy; and coincidental deafness plus another LQTS genotype. (rieraUnknownyearjervellandlangenielsen pages 6-9)

There is no routine biochemical, biopsy, imaging, liquid-biopsy, proteomic, or metabolomic diagnostic test. Echocardiography is useful to exclude structural disease rather than confirm JLNS2.

## 11. Outcome and prognosis

Untreated JLNS as a whole has historically carried high childhood mortality, but JLNS2-specific outcome estimates are substantially less severe and much less precise. The best subtype-separated multicenter evidence found definite arrhythmic events in 10.5% (2/19). The authors concluded that low penetrance of KCNE1-associated QT prolongation aligns with the relatively mild phenotype observed in JLNS2. This must not be interpreted as benignity: sudden cardiac arrest remains possible, and treatment decisions should follow the measured phenotype and event history. (roberts2020aninternationalmulticenter pages 1-5)

Poor prognostic indicators in mixed JLNS include very prolonged QTc, early syncope, prior cardiac arrest, T-wave alternans, events despite adherent beta-blockade, and exposure to avoidable triggers. No validated JLNS2-specific prognostic biomarker or survival calculator exists. Hearing disability is permanent but auditory and communication outcomes can improve substantially with early cochlear implantation and rehabilitation. No reliable JLNS2-specific 5- or 10-year survival statistic is available.

## 12. Treatment and real-world implementation

1. **Nonselective beta-blocker therapy**—usually nadolol or propranolol—is first-line for clinically manifest congenital LQTS, with weight-adjusted specialist dosing and adherence monitoring. This recommendation is extrapolated from congenital-LQTS guidance because no JLNS2 randomized trial exists. Suggested NCIt concept: beta-adrenergic blocking agent (**NCIT:C29576**). (rieraUnknownyearjervellandlangenielsen pages 6-9, theodore2024icdimplantin pages 1-3)
2. **Trigger control:** remove QT-prolonging medicines, correct potassium/magnesium deficiency, manage vomiting/dehydration promptly, individualize exercise restrictions, provide a medical-alert plan, and train family members in CPR/AED use. (rieraUnknownyearjervellandlangenielsen pages 1-3, theodore2024icdimplantin pages 3-4)
3. **LCSD:** consider for recurrent syncope/arrhythmia despite adequate beta-blockade or when beta-blockers are not tolerated; it is not a cure and therapy generally continues. Suggested NCIt annotation: sympathetic denervation procedure.
4. **ICD:** indicated after resuscitated cardiac arrest and considered for recurrent events or persistently extreme risk despite optimal therapy. Device complications and inappropriate shocks are important in small children; implantation must be individualized. A 2024 case described a six-year-old with QTc 600 ms and recurrent exercise/emotion-triggered syncope despite beta-blockade who received an ICD, with LCSD planned if events recurred. This case was not molecularly separated as JLNS2. (theodore2024icdimplantin pages 1-3, theodore2024icdimplantin pages 3-4)
5. **Hearing treatment:** hearing aids may be insufficient for profound loss; early cochlear implantation plus speech-language and audiologic rehabilitation is the principal functional intervention. Cardiology, electrophysiology, anesthesia, and otology teams should coordinate perioperative care, continue protective therapy where feasible, avoid QT-prolonging combinations, maintain electrolytes, monitor continuously, and have external defibrillation immediately available. Life-threatening postoperative arrhythmia has been documented in JLNS after cochlear implantation. (qiu2020jervellandlangenielsen pages 5-7)

No approved KCNE1 gene replacement, CRISPR therapy, antisense oligonucleotide, siRNA, mRNA, cell therapy, or JLNS2-specific targeted drug exists. A search of active ClinicalTrials.gov records found broader LQTS monitoring, registry, and cascade-screening studies, but no clearly JLNS2-specific interventional trial. The 2023 precision-medicine literature emphasizes patient-specific iPSC cardiomyocytes, genome editing, and high-throughput drug testing as future approaches rather than current care. (zhang2014recessivecardiacphenotypes pages 1-2)

## 13. Prevention

Primary prevention of a de novo inherited phenotype through lifestyle is not possible. **Reproductive prevention/options** include carrier testing, genetic counseling, partner testing in at-risk communities, prenatal diagnosis by chorionic-villus sampling or amniocentesis after familial variants are known, and preimplantation genetic testing for monogenic disease. (rieraUnknownyearjervellandlangenielsen pages 12-15)

Secondary prevention consists of ECG screening in congenital deafness, cascade testing of relatives, newborn hearing screening linked to cardiology referral when syndromic disease is suspected, and presymptomatic treatment of genetically/phenotypically affected relatives. Tertiary prevention comprises beta-blockade, avoidance measures, LCSD/ICD when indicated, and emergency preparedness. Population newborn DNA screening for JLNS2 is not standard. Immunization and infectious prophylaxis are not applicable.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart or zoonotic transmission was identified. The mechanism is evolutionarily conserved in mammals through orthologous **Kcne1/Kcnq1** channel complexes. Relevant taxa include human (*Homo sapiens*, NCBI Taxonomy **9606**) and laboratory mouse (*Mus musculus*, **10090**). There is no infectious transmission, cross-species contagion, or breed-specific VBO annotation.

## 15. Model organisms and advanced research

**Kcne1-null mouse.** This is the principal direct genetic model. Homozygous disruption reproduces bilateral sensorineural deafness, strial/endolymphatic abnormalities, and impaired endocochlear physiology. It is useful for cochlear potassium transport and tissue pathology. Its cardiac phenotype is comparatively mild, limiting translation because murine ventricular repolarization differs materially from human repolarization. (faridi2019mutationalandphenotypic pages 12-14)

**Cell systems.** Heterologous expression in Xenopus oocytes or mammalian cells measures KCNE1 effects on KCNQ1 current, gating, trafficking, and dominant-negative behavior. Such assays are essential because computational prediction alone is unreliable and there is no simple clinical biochemical test of KCNE1 function. (faridi2019mutationalandphenotypic pages 6-8)

**iPSC models.** Landmark JLNS iPSC-cardiomyocyte research demonstrated absent/reduced I-Ks, prolonged action and field potentials, abnormal adrenergic responses, proarrhythmic drug sensitivity, and pharmacologic rescue. However, that study modeled **KCNQ1-related JLNS1**, not KCNE1-related JLNS2, so it provides proof of platform rather than direct subtype evidence. [Experimental human iPSC evidence; December 2014; DOI: https://doi.org/10.1073/pnas.1419553111]. (zhang2014recessivecardiacphenotypes pages 1-2)

No validated JLNS2-specific organoid, patient-derived iPSC series, CRISPR screen, spatial-transcriptomic dataset, or multi-omic signature was found through 2024. Recent 2023–2024 developments are therefore chiefly improvements in broad LQTS precision modeling, pediatric management, CNV detection, and cochlear cell biology rather than a new JLNS2 therapy. The central research priorities are international genotype-confirmed registries, systematic functional classification of KCNE1 variants, direct KCNE1 patient-iPSC models, subtype-specific treatment outcomes, and safe dual-organ gene-delivery strategies.

## Evidence limitations

JLNS2 is frequently pooled with JLNS1, older reports predate modern variant-classification standards, and severe historical outcome estimates largely reflect KCNQ1-predominant cohorts. The 19-patient international JLNS2 series remains the strongest subtype-separated clinical evidence identified. Consequently, incidence, penetrance, variant-specific risk, sex effects, quality of life, treatment response, and survival cannot presently be estimated with high precision. Statements derived from mixed JLNS, generic congenital LQTS, KCNQ1 models, or mouse experiments have been explicitly labeled rather than presented as direct JLNS2 evidence.

References

1. (roberts2020aninternationalmulticenter pages 1-5): Jason D. Roberts, S. Yukiko Asaki, Andrea Mazzanti, J. Martijn Bos, Izabela Tuleta, Alison R. Muir, Lia Crotti, Andrew D. Krahn, Valentina Kutyifa, M. Benjamin Shoemaker, Christopher L. Johnsrude, Takeshi Aiba, Luciana Marcondes, Anwar Baban, Sharmila Udupa, Brynn Dechert, Peter Fischbach, Linda M. Knight, Eric Vittinghoff, Deni Kukavica, Birgit Stallmeyer, John R. Giudicessi, Carla Spazzolini, Keiko Shimamoto, Rafik Tadros, Julia Cadrin-Tourigny, Henry J. Duff, Christopher S. Simpson, Thomas M. Roston, Yanushi D. Wijeyeratne, Imane El Hajjaji, Maisoon D. Yousif, Lorne J. Gula, Peter Leong-Sit, Nikhil Chavali, Andrew P. Landstrom, Gregory M. Marcus, Sven Dittmann, Arthur A. M. Wilde, Elijah R. Behr, Jacob Tfelt-Hansen, Melvin M. Scheinman, Marco V. Perez, Juan Pablo Kaski, Robert M. Gow, Fabrizio Drago, Peter F. Aziz, Dominic J. Abrams, Michael H. Gollob, Jonathan R. Skinner, Wataru Shimizu, Elizabeth S. Kaufman, Dan M. Roden, Wojciech Zareba, Peter J. Schwartz, Eric Schulze-Bahr, Susan P. Etheridge, Silvia G. Priori, and Michael J. Ackerman. An international multicenter evaluation of type 5 long qt syndrome. Feb 2020. URL: https://doi.org/10.1161/circulationaha.119.043114, doi:10.1161/circulationaha.119.043114. This article has 64 citations and is from a highest quality peer-reviewed journal.

2. (faridi2019mutationalandphenotypic pages 1-3): Rabia Faridi, Risa Tona, Alessandra Brofferio, Michael Hoa, Rafal Olszewski, Isabelle Schrauwen, Muhammad Z.K. Assir, Akhtar A. Bandesha, Asma A. Khan, Atteeq U. Rehman, Carmen Brewer, Wasim Ahmed, Suzanne M. Leal, Sheikh Riazuddin, Steven E. Boyden, and Thomas B. Friedman. Mutational and phenotypic spectra of kcne1 deficiency in jervell and lange‐nielsen syndrome and romano‐ward syndrome. Human Mutation, 40:162-176, Dec 2019. URL: https://doi.org/10.1002/humu.23689, doi:10.1002/humu.23689. This article has 47 citations and is from a domain leading peer-reviewed journal.

3. (OpenTargets Search: Jervell and Lange-Nielsen syndrome 2-KCNE1): Open Targets Query (Jervell and Lange-Nielsen syndrome 2-KCNE1, 29 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (faridi2019mutationalandphenotypic pages 6-8): Rabia Faridi, Risa Tona, Alessandra Brofferio, Michael Hoa, Rafal Olszewski, Isabelle Schrauwen, Muhammad Z.K. Assir, Akhtar A. Bandesha, Asma A. Khan, Atteeq U. Rehman, Carmen Brewer, Wasim Ahmed, Suzanne M. Leal, Sheikh Riazuddin, Steven E. Boyden, and Thomas B. Friedman. Mutational and phenotypic spectra of kcne1 deficiency in jervell and lange‐nielsen syndrome and romano‐ward syndrome. Human Mutation, 40:162-176, Dec 2019. URL: https://doi.org/10.1002/humu.23689, doi:10.1002/humu.23689. This article has 47 citations and is from a domain leading peer-reviewed journal.

5. (theodore2024icdimplantin pages 1-3): TJ Theodore and PGKM Dhilipan. Icd implant in 6-year-old with jervell and lange-nielsen (jln) syndrome. Unknown journal, 2024.

6. (vojdani2019mutationscreeningof pages 7-10): Samaneh Vojdani, Susan Amirsalari, Saman Milanizadeh, Fatemeh Molaei, Mohammad Ajalloueyane, Arezoo Khosravi, Leila Hamzehzadeh, Mohammad Mehdi Ghasemi, Mohammad Reza Talee, and Mohammad Reza Abbaszadegan. Mutation screening of kcnq1 and kcne1 genes in iranian patients with jervell and lange-nielsen syndrome. Fetal and Pediatric Pathology, 38:273-281, Apr 2019. URL: https://doi.org/10.1080/15513815.2019.1585500, doi:10.1080/15513815.2019.1585500. This article has 15 citations and is from a peer-reviewed journal.

7. (hataba2025themutationalspectrum pages 14-17): Aya Hataba, M. Allouba, Mariam Fathy, A. Afify, E. Ahmed, M. Riad, Mohamed Elmaghawry, Youssef M. El Bayoumy, Amany Elleithy, A. Mahfouz, Jodie Ingles, A. Galal, Sohila Rabie, M. Allam, S. Halawa, Nour Elsadek, B. Samy, H. Kassem, O. Kamel, Yasmine Aguib, Magdi H. Yacoub, Magdi Kamel, Yasmine Yacoub, and Aguib. The mutational spectrum of jervell and lange-nielsen syndrome: insights from highly consanguineous families. MedRxiv, Oct 2025. URL: https://doi.org/10.1101/2025.10.22.25336867, doi:10.1101/2025.10.22.25336867. This article has 0 citations.

8. (rieraUnknownyearjervellandlangenielsen pages 1-3): ARP Riera. Jervell and lange-nielsen syndrome (jlns)-2010. Unknown journal, Unknown year.

9. (qiu2020jervellandlangenielsen pages 5-7): Yue Qiu, Sen Chen, Xia Wu, Wen-Juan Zhang, Wen Xie, Yuan Jin, Le Xie, Kai Xu, Xue Bai, Hui-Min Zhang, Xiao-Zhou Liu, Xiao-Hui Wang, Yu Sun, and Wei-Jia Kong. Jervell and lange-nielsen syndrome due to a novel compound heterozygous kcnq1 mutation in a chinese family. Neural Plasticity, 2020:1-8, May 2020. URL: https://doi.org/10.1155/2020/3569359, doi:10.1155/2020/3569359. This article has 14 citations and is from a peer-reviewed journal.

10. (vojdani2019mutationscreeningof pages 4-7): Samaneh Vojdani, Susan Amirsalari, Saman Milanizadeh, Fatemeh Molaei, Mohammad Ajalloueyane, Arezoo Khosravi, Leila Hamzehzadeh, Mohammad Mehdi Ghasemi, Mohammad Reza Talee, and Mohammad Reza Abbaszadegan. Mutation screening of kcnq1 and kcne1 genes in iranian patients with jervell and lange-nielsen syndrome. Fetal and Pediatric Pathology, 38:273-281, Apr 2019. URL: https://doi.org/10.1080/15513815.2019.1585500, doi:10.1080/15513815.2019.1585500. This article has 15 citations and is from a peer-reviewed journal.

11. (rieraUnknownyearjervellandlangenielsen pages 12-15): ARP Riera. Jervell and lange-nielsen syndrome (jlns)-2010. Unknown journal, Unknown year.

12. (faridi2019mutationalandphenotypic pages 12-14): Rabia Faridi, Risa Tona, Alessandra Brofferio, Michael Hoa, Rafal Olszewski, Isabelle Schrauwen, Muhammad Z.K. Assir, Akhtar A. Bandesha, Asma A. Khan, Atteeq U. Rehman, Carmen Brewer, Wasim Ahmed, Suzanne M. Leal, Sheikh Riazuddin, Steven E. Boyden, and Thomas B. Friedman. Mutational and phenotypic spectra of kcne1 deficiency in jervell and lange‐nielsen syndrome and romano‐ward syndrome. Human Mutation, 40:162-176, Dec 2019. URL: https://doi.org/10.1002/humu.23689, doi:10.1002/humu.23689. This article has 47 citations and is from a domain leading peer-reviewed journal.

13. (rieraUnknownyearjervellandlangenielsen pages 6-9): ARP Riera. Jervell and lange-nielsen syndrome (jlns)-2010. Unknown journal, Unknown year.

14. (theodore2024icdimplantin pages 3-4): TJ Theodore and PGKM Dhilipan. Icd implant in 6-year-old with jervell and lange-nielsen (jln) syndrome. Unknown journal, 2024.

15. (rieraUnknownyearjervellandlangenielsen pages 3-6): ARP Riera. Jervell and lange-nielsen syndrome (jlns)-2010. Unknown journal, Unknown year.

16. (zhang2014recessivecardiacphenotypes pages 1-2): Miao Zhang, Cristina D’Aniello, Arie O. Verkerk, Eva Wrobel, Stefan Frank, Dorien Ward-van Oostwaard, Ilaria Piccini, Christian Freund, Jyoti Rao, Guiscard Seebohm, Douwe E. Atsma, Eric Schulze-Bahr, Christine L. Mummery, Boris Greber, and Milena Bellin. Recessive cardiac phenotypes in induced pluripotent stem cell models of jervell and lange-nielsen syndrome: disease mechanisms and pharmacological rescue. Proceedings of the National Academy of Sciences, 111:E5383-E5392, Dec 2014. URL: https://doi.org/10.1073/pnas.1419553111, doi:10.1073/pnas.1419553111. This article has 230 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Jervell_and_Lange-Nielsen_Syndrome_2-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 0 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1002/humu.23689`: "cardio-auditory syndrome characterized by congenital profound sensorineural deafness and a prolonged QT interval that can cause ventricular arrhythmias and sudden cardiac death."
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012871` (5 mentions) - the report calls it "if available"; MONDO calls it **Jervell and Lange-Nielsen syndrome 2**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0002441` (1 mention) - the report calls it "Parent disease concepts include Jervell and Lange-Nielsen syndrome"; MONDO calls it **Jervell and Lange-Nielsen syndrome**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.