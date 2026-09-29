---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T11:10:22.599293'
end_time: '2026-09-08T11:29:41.400339'
duration_seconds: 1158.8
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Platelet-type Bleeding Disorder 22
  mondo_id: MONDO:0032765
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 13
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032765
    reported_labels:
    - if available
    ontology_label: bleeding disorder, platelet-type, 22
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
  path: Platelet-type_Bleeding_Disorder_22-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Platelet-type Bleeding Disorder 22
- **MONDO ID:** MONDO:0032765 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Platelet-type Bleeding Disorder 22** covering all of the
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
- **Disease Name:** Platelet-type Bleeding Disorder 22
- **MONDO ID:** MONDO:0032765 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Platelet-type Bleeding Disorder 22** covering all of the
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


# Platelet-type Bleeding Disorder 22 (BDPLT22): Comprehensive Disease-Characteristics Report

## Executive summary and evidence boundary

Platelet-type bleeding disorder 22 is an exceptionally rare, autosomal-recessive platelet-function disorder caused by biallelic dysfunction of **EPHB2**, which encodes ephrin type-B receptor 2, a plasma-membrane receptor tyrosine kinase. The defining report described only **two affected siblings from one consanguineous family**, both homozygous for **NM_004442.6:c.2233C>T, p.(Arg745Cys)**. The disorder causes recurrent cutaneous/wound bleeding and, in one patient, chronic gastrointestinal hemorrhage, primarily through defective platelet GPVI- and GPCR-dependent activation rather than absent platelets or a global granule-storage defect. Consequently, every frequency, penetrance, prognosis, and treatment statement must be interpreted in light of an evidence base of n=2. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 5-9)

No disease-specific publication from 2023–2024, independent family, new causal variant, epidemiologic study, clinical trial, or targeted therapy was identified. Recent developments therefore concern broader inherited-platelet-disorder management and contemporary understanding of Eph receptor signaling, not new BDPLT22 patient data.

The following evidence map summarizes established findings and separates them from inference or management extrapolation.

| Domain | Disease-specific finding | Evidence type/strength | Ontology suggestions |
|---|---|---|---|
| Identity | Platelet-type bleeding disorder 22 (BDPLT22); **MONDO:0032765** | Disease-level ontology mapping; rare Mendelian platelet-function disorder | MONDO:0032765; inherited platelet function disorder |
| Gene and variant | **EPHB2**, **NM_004442.6:c.2233C>T**, **p.Arg745Cys (p.R745C)** in the intracellular tyrosine-kinase domain | Established in the discovery family by WES, segregation, patient-platelet studies, and heterologous functional assays (berrou2018amutationof pages 1-5, berrou2018amutationof pages 5-9) | HGNC:3393; GO:0004714 transmembrane receptor protein tyrosine kinase activity; GO:0005886 plasma membrane |
| Inheritance and evidence base | Autosomal recessive: two homozygous affected siblings in one consanguineous family; asymptomatic parents were heterozygous | Strong segregation within one family, but replication across independent families is unavailable (berrou2018amutationof pages 1-5, berrou2018amutationof pages 5-9) | HP:0000007 Autosomal recessive inheritance; germline variant |
| Bleeding phenotype | Recurrent spontaneous subcutaneous bleeding and excessive bleeding after minor wounds; one sibling had chronic gastrointestinal bleeding with iron-requiring anemia; ISTH-BAT scores **11** and **6** | Established human clinical evidence, n=2 (berrou2018amutationof pages 5-9, nurden2020inheritedplateletdiseases pages 6-7) | HP:0000978 Bruising susceptibility; HP:0005261 Gastrointestinal bleeding; HP:0001891 Iron deficiency anemia; HP:0001878 Hemorrhagic diathesis |
| Platelet count and morphology | Platelet count initially normal; later **120×10⁹/L** in one sibling. Elongated, sickle-shaped and heterogeneous platelets, membrane extensions and preplatelet/proplatelet remnants; maximal diameter **3.61±0.84** and **3.72±0.83 μm** versus **2.85±0.15 μm** in controls | Established patient laboratory and electron-microscopy evidence, n=2 (berrou2018amutationof pages 5-9, berrou2018amutationof pages 20-25) | HP:0011873 Abnormal platelet morphology; HP:0001873 Thrombocytopenia; CL:0000233 platelet; CL:0000556 megakaryocyte |
| Agonist responses | Reduced aggregation and secretion after **ADP, collagen, arachidonic acid, U46619/thromboxane-A₂-pathway agonists, thrombin/PAR4 agonism, and convulxin**; ristocetin response, dense-granule number, and platelet ATP/ADP content were normal | Established ex vivo patient-platelet evidence (berrou2018amutationof pages 5-9, berrou2018amutationof pages 20-25) | HP:0003540 Abnormality of platelet aggregation; GO:0070527 platelet aggregation; GO:0030168 platelet activation; CHEBI:16761 ADP; CHEBI:32395 arachidonic acid |
| Functional hemostasis | Defective **integrin αIIbβ3 inside-out activation**, granule secretion, P-selectin exposure, and thrombus formation on collagen under flow; clot retraction, flow-dependent adhesion, and fibrinogen spreading were only mildly affected | Established ex vivo functional evidence; indicates predominant activation rather than severe outside-in-signaling failure (berrou2018amutationof pages 1-5, berrou2018amutationof pages 13-16) | GO:0033628 regulation of cell adhesion mediated by integrin; GO:0002576 platelet degranulation; GO:0072378 blood coagulation, fibrin clot formation |
| Molecular mechanism | p.Arg745Cys impaired EPHB2 autophosphorylation and reduced activation/phosphorylation of **Src/Lyn, Syk, FcRγ, Akt, PLCγ2**, disrupting proximal **GPVI** and GPCR crosstalk | Established in patient platelets and GPVI-expressing RBL-2H3 cells; exact intermediary linking EPHB2 to Src-family kinases remains inferred (berrou2018amutationof pages 1-5, berrou2018amutationof pages 13-16, berrou2018amutationof pages 16-20) | GO:0007169 transmembrane receptor protein tyrosine kinase signaling pathway; GO:0031092 platelet alpha granule membrane; GO:0038083 peptidyl-tyrosine autophosphorylation; CL:0000233 platelet |
| Preserved functions | Ephrin-B1-induced EPHB2 clustering was preserved; PAR4-AP-induced PKC activity and much calcium mobilization were normal, although reduced calcium signaling was reported under some GPVI conditions | Established assay evidence; argues against failure of receptor clustering or a global signaling defect (berrou2018amutationof pages 1-5, berrou2018amutationof pages 13-16, berrou2018amutationof pages 16-20) | GO:0048013 ephrin receptor signaling pathway; GO:0035556 intracellular signal transduction; GO:0051480 cytosolic calcium ion homeostasis |
| Diagnosis | Suspect from lifelong mucocutaneous/wound bleeding with normal or mildly reduced platelet count; document abnormal aggregation/secretion and flow-thrombus phenotypes, then confirm **biallelic EPHB2** variants and familial segregation | Disease-specific phenotype–genotype approach is supported; no validated BDPLT22 diagnostic criteria or biomarker exists (nurden2020inheritedplateletdiseases pages 6-7, berrou2018amutationof pages 1-5, berrou2018amutationof pages 5-9) | ISTH-BAT; HP:0001878 Hemorrhagic diathesis; sequence-variant analysis; platelet aggregation assay |
| Epidemiology and prognosis | Only **two affected siblings from one family** are documented in the foundational evidence; disease-specific prevalence, incidence, penetrance, survival, and long-term outcome estimates are unavailable | Very limited human evidence; population-level estimates would be speculative (nurden2020inheritedplateletdiseases pages 6-7, berrou2018amutationof pages 5-9) | ORPHA/epidemiology mapping unavailable; rare disease |
| Treatment and trials | No BDPLT22-specific approved therapy, response rate, pharmacogenomic recommendation, or interventional trial was identified. Local hemostasis, tranexamic acid, selected desmopressin use, platelet concentrates, or rFVIIa are **extrapolated from general inherited platelet-disorder guidance**, not validated specifically for EPHB2 deficiency | Extrapolated expert guidance; not disease-specific evidence (nurden2020inheritedplateletdiseases pages 10-11) | NCIT:C783 Tranexamic Acid; NCIT:C61737 Desmopressin; NCIT:C15340 Platelet Transfusion; NCIT:C522 Recombinant Factor VIIa |
| Models and omics | Functional modeling used GPVI-expressing **RBL-2H3 rat basophilic leukemia cells** transfected with wild-type or p.Arg745Cys EPHB2. No dedicated p.Arg745Cys knock-in animal, natural veterinary disease, single-cell, spatial, transcriptomic, proteomic, metabolomic, or epigenomic disease study is established | Relevant in-vitro validation; no dedicated organismal BDPLT22 model (berrou2018amutationof pages 1-5, berrou2018amutationof pages 13-16) | CL:0000097 mast cell-like experimental lineage; NCBI Taxon:10116 *Rattus norvegicus*; in-vitro disease model |


*Table: Compact evidence map of the genetic, clinical, laboratory, mechanistic, diagnostic, and therapeutic knowledge for EPHB2-related platelet-type bleeding disorder 22. It separates observations established in the single reported family from inference and management extrapolated from broader inherited platelet disorders.*

## 1. Disease information

### Definition

BDPLT22 is a **Mendelian primary-hemostasis disorder** in which platelet production is broadly preserved but platelet activation, secretion, integrin activation, and thrombus growth are impaired. The foundational article’s abstract states: **“We report the first EPHB2 variant affecting platelets in 2 siblings (P1 and P2) from a consanguineous family with recurrent bleeding and normal platelet counts.”** It concludes that the disorder demonstrates EPHB2 crosstalk with GPVI and GPCR signaling. (berrou2018amutationof pages 1-5)

### Identifiers and synonyms

- **MONDO:** MONDO:0032765, as specified in the query.
- **Preferred name:** Platelet-type bleeding disorder 22.
- **Abbreviation:** BDPLT22.
- **Useful synonyms:** EPHB2-related platelet disorder; EPHB2-related inherited platelet-function disorder; platelet dysfunction due to EPHB2 deficiency; inherited platelet disorder associated with EPHB2 p.Arg745Cys.
- **OMIM:** A distinct numbered OMIM phenotype is implied by the BDPLT22 nomenclature, but its numerical identifier was not recoverable from the retrieved primary or review text and should be verified directly in OMIM before database deposition.
- **Orphanet:** No disorder-specific Orphanet identifier was recovered.
- **ICD-10/ICD-11 and MeSH:** No uniquely specific code/heading was identified. A broader hereditary platelet-function-defect or hemorrhagic-disorder category would be necessary; this should not be represented as a one-to-one disease mapping.

The evidence is **aggregated disease-level literature derived from two individually phenotyped research participants**, not an EHR-derived population dataset. The primary human data include clinical histories, pedigree segregation, ex-vivo platelet assays, microscopy, and sequencing. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 5-9)

## 2. Etiology

### Causal factor and genetic risk

The demonstrated initiating lesion is germline, homozygous **EPHB2 c.2233C>T, p.Arg745Cys**. It substitutes a conserved arginine in the intracellular tyrosine-kinase domain, immediately adjacent to essential Asp746. Both affected siblings were homozygous; both clinically unaffected parents were heterozygous. At publication, ExAC frequency was reported as **<10⁻⁶**, and in-silico tools predicted damage. Segregation, extreme rarity, domain location, patient-platelet abnormalities, and heterologous functional validation collectively support pathogenicity. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 5-9)

The variant is germline rather than somatic. The best-supported molecular consequence is **partial loss of EPHB2 kinase/autophosphorylation function**, not loss of receptor expression or ephrin-induced clustering. No other replicated BDPLT22-causing allele was identified in the retrieved literature. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 13-16)

### Environmental and lifestyle risk factors

No toxin, infection, radiation, diet, smoking exposure, alcohol exposure, occupation, or acquired immune process has been shown to cause BDPLT22. Consanguinity increases the probability that two carriers transmit the same rare recessive allele but is not itself a biological cause.

Factors likely to **unmask or exacerbate bleeding** include trauma, surgery, dental procedures, childbirth, gastrointestinal lesions, and drugs that inhibit platelet function—especially aspirin and nonsteroidal anti-inflammatory drugs. These are general platelet-disorder considerations, not demonstrated EPHB2-specific gene–environment interactions.

### Protective factors and modifiers

No protective EPHB2 allele, modifier gene, epistatic locus, or environmental protective factor has been reported. Avoidance of platelet-inhibiting medication and anticipatory hemostatic planning can reduce complications but do not alter the genotype. No formal gene–environment study exists.

## 3. Phenotypes

The two reported patients were a brother and sister, investigated initially at ages **12 and 15 years**, respectively, and reported as young adults. Both had excessive spontaneous subcutaneous bleeding and disproportionate bleeding after minor wounds. One had chronic gastrointestinal bleeding causing anemia that required iron treatment. ISTH Bleeding Assessment Tool scores were **11** and **6**, supporting clinically significant but variably expressed bleeding. (berrou2018amutationof pages 5-9)

### Clinical and laboratory phenotype annotations

- **Recurrent spontaneous subcutaneous bleeding/bruising:** symptom/sign; childhood recognition; recurrent/episodic; observed in 2/2. Suggested HPO: **Bruising susceptibility (HP:0000978)** and **Hemorrhagic diathesis (HP:0001878)**.
- **Prolonged/excessive bleeding after minor wounds:** symptom/sign; childhood; recurrent with injury; 2/2. Suggested HPO: **Prolonged bleeding after trauma** where available, plus HP:0001878.
- **Gastrointestinal bleeding:** symptom; chronic in 1/2; sufficient to cause anemia. HPO: **Gastrointestinal hemorrhage (HP:0005261)**. (berrou2018amutationof pages 5-9, nurden2020inheritedplateletdiseases pages 6-7)
- **Secondary iron-deficiency anemia:** laboratory/clinical complication in 1/2, treated with iron. HPO: **Iron deficiency anemia (HP:0001891)**.
- **Platelet count:** initially normal in both; one later had mild thrombocytopenia at **120×10⁹/L**. HPO: **Thrombocytopenia (HP:0001873)**, qualified as mild/variable rather than defining. (berrou2018amutationof pages 5-9)
- **Abnormal platelet morphology:** elongated, sickle-shaped and round heterogeneous forms, membrane extensions, barbell-like preplatelets, and megakaryocyte/proplatelet fragments. Mean maximal diameters were **3.61±0.84 μm** and **3.72±0.83 μm**, versus **2.85±0.15 μm** in controls. HPO: **Abnormal platelet morphology (HP:0011873)**. (berrou2018amutationof pages 5-9, berrou2018amutationof pages 20-25)
- **Impaired aggregation and secretion:** laboratory abnormality affecting responses to ADP, collagen, arachidonic acid, U46619/thromboxane-A₂ signaling, thrombin/PAR4 stimulation, and convulxin. Ristocetin response was preserved. HPO: **Abnormality of platelet aggregation (HP:0003540)**. (berrou2018amutationof pages 5-9, berrou2018amutationof pages 20-25)
- **Preserved dense-granule stores:** platelet ATP/ADP content and dense-granule number were normal, arguing against a classic storage-pool deficiency. (berrou2018amutationof pages 5-9)

Frequency estimates above are proportions within two siblings and must not be interpreted as population frequencies. Severity is variable even within the family. The clinical course appears lifelong and exposure-dependent, not neurodegenerative or continuously progressive.

### Quality of life

No EQ-5D, SF-36, PROMIS, school/work-function, pain, or disease-specific quality-of-life measure has been reported. Recurrent bruising, wound bleeding, gastrointestinal blood loss, iron therapy, emergency planning, and procedural risk plausibly impose substantial burden, but quantitative QOL effects remain unknown.

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** EPHB2, ephrin type-B receptor 2.
- **Suggested HGNC identifier:** **HGNC:3393**; verify against HGNC before ingestion.
- **Protein class:** single-pass transmembrane Eph receptor tyrosine kinase.
- **Relevant compartments:** plasma membrane (**GO:0005886**) and cytoplasmic/intracellular kinase domain.
- **Relevant functions/processes:** transmembrane receptor protein tyrosine kinase activity (**GO:0004714**), receptor autophosphorylation (**GO:0038083**), ephrin receptor signaling (**GO:0048013**), platelet activation (**GO:0030168**), and platelet aggregation (**GO:0070527**).

### Pathogenic variant assessment

The sole disease-defining allele is **NM_004442.6:c.2233C>T; p.(Arg745Cys), historically p.R745C**. It is a missense single-nucleotide variant, inherited in homozygous state. The primary report predates or does not provide a formal ClinVar ACMG classification in the retrieved text. For a knowledge base, it is safest to record **“reported disease-causing/pathogenic in the primary study”** rather than assert a current ClinVar classification without direct ClinVar verification. Supporting ACMG-style evidence includes extreme rarity, segregation in a recessive pedigree, critical kinase-domain location, multiple functional defects, and concordant phenotype. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 5-9)

R745C reduced EPHB2 autophosphorylation; in GPVI-expressing RBL-2H3 cells, activation-related phosphorylation of mutant receptor was approximately half that of wild type. Ephrin-B1-induced receptor clustering was retained. Thus, the most defensible consequence is **hypomorphic kinase loss of function**, not complete null function or dominant negativity. (berrou2018amutationof pages 13-16)

No validated modifier genes, disease-specific methylation pattern, histone alteration, chromatin signature, CNV, translocation, inversion, aneuploidy, or other structural variant has been reported.

## 5. Environmental information

BDPLT22 is not an environmentally acquired, lifestyle-mediated, or infectious disease. Environmental exposures primarily modify the probability of a bleeding event. Relevant avoidable exposures include aspirin, NSAIDs, and unnecessary antiplatelet drugs; trauma and invasive procedures require planning. No association exists with pollution, occupational chemicals, ionizing radiation, smoking, alcohol, diet, bacteria, viruses, fungi, or parasites.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Homozygous EPHB2 p.Arg745Cys in the intracellular kinase domain leads to impaired EPHB2 autophosphorylation/kinase signaling.**
2. **Impaired EPHB2 signaling leads to deficient activation of Src-family kinases, especially Src and Lyn; the exact phosphatase/adapter intermediary is inferred rather than demonstrated.**
3. **Deficient Src/Lyn activity leads to reduced FcRγ and Syk phosphorylation in the proximal GPVI pathway.**
4. **Reduced GPVI signaling leads to reduced PLCγ2 and Akt activation and, under GPVI stimulation, impaired calcium-dependent platelet activation.**
5. **In a parallel branch, impaired EPHB2–GPCR crosstalk leads to defective Src activation downstream of PAR4/other GPCR agonists despite preserved PKC activity and largely preserved calcium mobilization in the tested PAR4 condition.**
6. **These signaling defects lead to deficient αIIbβ3 inside-out activation, granule secretion/P-selectin exposure, and amplification by ADP/thromboxane pathways.**
7. **Defective platelet activation leads to reduced aggregation and deficient thrombus growth on collagen under flow.**
8. **Deficient primary hemostatic plug formation results in recurrent cutaneous/wound bleeding and, where a gastrointestinal source is present, chronic gastrointestinal blood loss and anemia.** (berrou2018amutationof pages 1-5, berrou2018amutationof pages 13-16, berrou2018amutationof pages 16-20)

### Mechanistic detail

Patient platelets had markedly impaired phosphorylation of **Lyn, Syk, FcRγ, Akt, and PLCγ2** after GPVI stimulation. The defect was observed without platelet–platelet contact, showing that early EPHB2 support of GPVI signaling does not require ephrin-mediated intercellular clustering. PAR4-activating peptide produced defective Src activation while PKC activity and calcium mobilization were normal in that experimental setting, localizing at least part of the GPCR defect distal or parallel to canonical PKC/Ca²⁺ signaling. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 13-16, berrou2018amutationof pages 16-20)

The abstract provides a concise primary-source statement: **“Most importantly, Lyn, Syk, and FcRγ phosphorylation, the initial steps in glycoprotein VI (GPVI) platelet signaling were drastically impaired in the absence of platelet-platelet contact.”** It further reports that mutant overexpression **“impaired EPHB2 autophosphorylation but had no effect on ephrin ligand-induced EPHB2 clustering.”** (berrou2018amutationof pages 1-5)

Clot retraction, adhesion under flow, and spreading on fibrinogen were only mildly affected, indicating relative preservation of αIIbβ3 outside-in signaling. The dominant defect is therefore upstream platelet activation and integrin inside-out activation, not inability of fibrinogen-bound integrin to support all downstream responses. (berrou2018amutationof pages 1-5)

No evidence supports primary apoptosis, autophagy, immune-mediated destruction, chronic inflammation, fibrosis, oxidative injury, or a defined metabolic block. The abnormal preplatelet/proplatelet forms suggest a possible megakaryocyte fragmentation or platelet-formation contribution, but this is secondary and incompletely defined. No disease-specific transcriptomic, single-cell, spatial, proteomic, metabolomic, lipidomic, epigenomic, CRISPR-screen, or multi-omics dataset was identified.

**Suggested cell terms:** platelet (**CL:0000233**), megakaryocyte (**CL:0000556**). **Additional GO suggestions:** platelet degranulation (**GO:0002576**), positive regulation of platelet activation, protein tyrosine phosphorylation, integrin activation, and intracellular calcium-ion signaling; exact GO identifiers should be ontology-validated at ingestion.

## 7. Anatomical structures affected

The primary biological lesion is in circulating **platelets** of the hematologic/cardiovascular system and likely their bone-marrow precursor, the **megakaryocyte**. Suggested anatomical mappings include blood (**UBERON:0000178**), bone marrow (**UBERON:0002371**), and vascular system/blood vessel lumen. Bleeding can secondarily affect skin/subcutaneous tissue and gastrointestinal tract; these are sites of hemorrhage, not necessarily intrinsically diseased organs. (berrou2018amutationof pages 5-9, berrou2018amutationof pages 20-25)

At the subcellular level, relevant structures are the platelet plasma membrane, intracellular EPHB2 kinase domain, GPVI/FcRγ receptor-signaling complex, αIIbβ3 integrin, α-granules, dense granules, and cytoskeletal/membrane systems involved in preplatelet fragmentation. Dense-granule number was normal. There is no lateralization.

## 8. Temporal development

The genetic defect is congenital, while clinically recognized bleeding occurred by childhood. Platelet investigations at 12 and 15 years imply pediatric onset or recognition. The disorder is expected to be lifelong because the germline genotype persists. Its manifestations are episodic and exposure-dependent—spontaneous bruising or bleeding after trauma/procedures—with possible chronic blood loss from a persistent gastrointestinal source. (berrou2018amutationof pages 5-9)

No formal stages, progression rate, remission pattern, or critical developmental window has been defined. There is no evidence of age-dependent anticipation or progressive organ failure. Critical practical periods include surgery, dental work, menarche/heavy menstruation, pregnancy, delivery, and gastrointestinal disease, although these have not been studied specifically in BDPLT22.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Two homozygous siblings were affected, whereas heterozygous parents were asymptomatic. This supports lack of a major phenotype in simple heterozygotes but is insufficient to establish complete recessive penetrance or exclude subtle laboratory abnormalities. Variable expressivity is suggested by different ISTH-BAT scores and gastrointestinal bleeding in only one sibling. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 5-9)

Only one consanguineous family is documented in the core evidence. Accordingly:

- prevalence and incidence per 100,000 are unknown;
- carrier frequency is unknown;
- no sex ratio can be estimated, despite one affected male and one affected female;
- no geographic, ethnic, founder, or population enrichment can be inferred;
- no genetic anticipation or germline mosaicism has been reported;
- the variant’s reported ExAC MAF was <10⁻⁶. (berrou2018amutationof pages 5-9)

For two carrier parents, standard Mendelian counseling gives a **25% affected, 50% carrier, and 25% non-carrier probability per pregnancy**, assuming full ascertainment of the familial allele. This is a genetic expectation, not a measured penetrance estimate.

## 10. Diagnostics

### Clinical and laboratory approach

1. Document lifelong bleeding history, family structure, consanguinity, medication exposure, and ISTH-BAT score.
2. Obtain CBC, platelet count and indices, blood smear, PT/INR, aPTT, fibrinogen, von Willebrand factor testing, and iron studies where chronic blood loss is suspected.
3. Perform light-transmission aggregometry using ADP, collagen, arachidonic acid, thromboxane-pathway agonist, ristocetin, thrombin/PAR agonists, and convulxin/GPVI agonism where available.
4. Assess secretion by ATP release and/or flow-cytometric P-selectin exposure; assess αIIbβ3 activation using an activation-specific antibody or fibrinogen binding.
5. In a specialist/research laboratory, consider platelet electron microscopy, collagen-flow thrombus assays, and phosphosignaling studies.
6. Confirm with sequencing showing **biallelic EPHB2 variants**, parental phasing/segregation, population-frequency review, and functional interpretation. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 5-9, berrou2018amutationof pages 20-25)

A normal platelet count does not exclude the disorder. Preserved ristocetin aggregation and normal dense-granule number/content help distinguish it from Bernard–Soulier/von Willebrand-related ristocetin defects and classic dense-granule storage-pool deficiency. (berrou2018amutationof pages 5-9)

### Genetic testing

A curated inherited bleeding/platelet-disorder panel that includes **EPHB2** is efficient when the phenotype is platelet-specific. Single-gene EPHB2 testing is appropriate for familial cascade testing once the allele is known. WES was the successful discovery method and remains appropriate for panel-negative cases; WGS may identify noncoding, structural, or poorly captured variants but has no demonstrated BDPLT22-specific yield. RNA sequencing may help evaluate splice or expression variants but is not validated here. CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line unless additional features suggest another diagnosis.

### Differential diagnosis

Important alternatives include von Willebrand disease, Glanzmann thrombasthenia, Bernard–Soulier syndrome, GP6-related platelet dysfunction, P2RY12 deficiency, RASGRP2- or FERMT3-related integrin-activation disorders, thromboxane-pathway defects, storage-pool disorders, ANO6/Scott syndrome, mild thrombocytopenias, coagulation-factor deficiencies, medication-induced platelet dysfunction, liver/renal disease, and acquired immune platelet disorders. EPHB2 disease is distinguished by recessive segregation, the multi-agonist activation/secretion defect, preserved ristocetin response and dense-granule stores, and molecular confirmation. Reviews emphasize that inherited platelet disorders with normal counts can still cause moderate or severe bleeding. (nurden2020inheritedplateletdiseases pages 6-7, nurden2020inheritedplateletdiseases pages 2-3)

No newborn-screening program or population screening is indicated. Cascade testing of adult relatives and targeted prenatal or preimplantation testing can be offered after identification of the familial pathogenic variant.

## 11. Outcome and prognosis

There are no survival curves, mortality rates, life-expectancy estimates, disability measures, longitudinal cohorts, or prognostic models. Neither reported patient was described as having a lethal multisystem syndrome. Available evidence suggests morbidity is dominated by recurrent bleeding, procedural risk, and anemia from chronic blood loss. One patient required iron supplementation for gastrointestinal bleeding. (berrou2018amutationof pages 5-9, nurden2020inheritedplateletdiseases pages 6-7)

Potential complications include severe traumatic or surgical hemorrhage, gastrointestinal bleeding, iron deficiency, transfusion exposure, and—if platelet transfusions become recurrent—alloimmunization. Recovery from an individual bleed is expected with local/systemic hemostasis, but the inherited platelet defect does not remit. Baseline bleeding history, ISTH-BAT score, prior procedural bleeding, lesion site, platelet count, and concomitant antiplatelet drugs are rational prognostic factors, but none is validated specifically for BDPLT22.

## 12. Treatment

### Disease-specific evidence

No EPHB2-directed drug, approved genotype-specific therapy, response-rate study, randomized trial, gene therapy, RNA therapy, cell therapy, or curative intervention has been reported. Iron was used for secondary anemia in one patient, but this treats blood-loss consequences rather than platelet dysfunction. (berrou2018amutationof pages 5-9)

### Extrapolated inherited-platelet-disorder strategy

Management should occur through a hemophilia/hemostasis center and be individualized to bleeding severity and procedure. General guidance recommends minimizing bleeding risks, carrying an emergency information card, and creating multidisciplinary prophylaxis plans for surgery and childbirth. For mild bleeding or lower-risk procedures, local hemostasis plus an antifibrinolytic such as **tranexamic acid** or selected use of **desmopressin** may be considered. Platelet transfusion is used when simpler measures are inadequate or for major bleeding; **recombinant activated factor VII (rFVIIa)** can be considered in severe/refractory circumstances, especially when platelet transfusion is ineffective or problematic. These recommendations are not validated specifically in BDPLT22. (nurden2020inheritedplateletdiseases pages 10-11)

The 2023 treatment review’s abstract describes the current general IPD armamentarium as: **“local hemostatic treatment, tranexamic acid, desmopressin, platelet concentrates, and recombinant activated factor VII.”** It also notes that treatment choice must account for the underlying disorder, bleeding severity/site, age, and sex. However, no EPHB2 patient was treated in a clinical study.

Practical options include:

- local pressure, suturing, topical hemostatic agents, and careful dental/surgical technique;
- tranexamic acid for oral/nasal/menstrual or procedure-associated mucosal bleeding, barring contraindications;
- desmopressin only after specialist assessment or a documented response, because efficacy in EPHB2 deficiency is unknown;
- matched/leukoreduced platelet concentrates for major bleeding or high-risk surgery, balancing alloimmunization and transfusion risks;
- rFVIIa as rescue therapy under expert supervision, not routine prophylaxis;
- iron replacement and investigation/treatment of gastrointestinal or menstrual blood-loss sources.

Suggested NCIT mappings include **Tranexamic Acid**, **Desmopressin**, **Platelet Transfusion**, **Recombinant Factor VIIa**, **Genetic Counseling**, and **Supportive Care**; identifiers should be checked in the current NCIT release.

Hematopoietic stem-cell transplantation is reserved in general guidance for selected young patients with life-threatening, recurrent, treatment-refractory inherited platelet disorders; there is no rationale or outcome evidence supporting it for the two known BDPLT22 patients. Similarly, autologous stem-cell gene therapy, artificial platelets, nanoparticles, and other procoagulants remain future general IPD concepts rather than BDPLT22 applications. (nurden2020inheritedplateletdiseases pages 10-11)

Clinical-trial searches found no relevant BDPLT22 interventional study or NCT identifier.

## 13. Prevention

Primary prevention of the germline disorder is not possible after conception. Reproductive options include carrier testing, cascade testing, genetic counseling, prenatal diagnosis, and preimplantation genetic testing for a confirmed familial allele.

Secondary prevention consists of early recognition in relatives, avoidance of diagnostic delay despite a normal platelet count, and pre-procedure genetic/functional characterization. Tertiary prevention includes avoiding aspirin/NSAIDs and unnecessary antiplatelet agents, using medical-alert documentation, maintaining dental care to reduce invasive procedures, treating iron deficiency, and establishing written emergency, surgical, and pregnancy plans. Multidisciplinary planning is recommended for childbirth and invasive procedures. (nurden2020inheritedplateletdiseases pages 10-11)

Vaccination has no disease-preventive role, although routine immunization remains appropriate. Population screening and public-health environmental interventions are not warranted for a single-family ultra-rare disorder.

## 14. Other species and natural disease

No naturally occurring EPHB2-associated platelet bleeding disorder was identified in companion animals, livestock, or wildlife. There is no zoonotic potential or infectious transmission.

The in-vitro functional system used **RBL-2H3 cells**, derived from rat basophilic leukemia, corresponding to *Rattus norvegicus* (**NCBI Taxon 10116**). This is an engineered signaling model, not natural rat disease. EPHB2/ephrin biology is evolutionarily conserved, and prior mouse studies support roles in platelet activation and thrombus formation, but they do not establish a natural veterinary counterpart or faithfully model human p.Arg745Cys disease. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 13-16)

## 15. Model organisms and experimental systems

The primary study transfected wild-type or R745C human EPHB2 into GPVI-expressing RBL-2H3 cells. The mutant retained ephrin-induced clustering but showed reduced autophosphorylation, validating a kinase-signaling defect independent of the patients’ broader genetic background. This model is useful for receptor phosphorylation, clustering, and GPVI-crosstalk experiments but cannot reproduce human bleeding, platelet biogenesis, vascular flow, or whole-organism pharmacology. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 13-16)

Prior EPHB2/β-galactosidase mouse work showed reduced platelet Akt and PLCγ2 phosphorylation and supports pathway plausibility, but it is not a p.Arg745Cys knock-in or dedicated BDPLT22 model. No zebrafish, Drosophila, C. elegans, yeast, iPSC-megakaryocyte, organoid, conditional knockout, humanized, or CRISPR-corrected model specific to BDPLT22 was identified. (berrou2018amutationof pages 13-16)

High-value future models would include an **Ephb2 Arg745Cys knock-in mouse**, CRISPR-engineered human iPSC-derived megakaryocytes/platelets, and microfluidic vascular-flow systems. These could test platelet formation, signaling dose dependence, bleeding/thrombosis balance, rescue by wild-type EPHB2, and candidate hemostatic therapies.

## Current understanding and research priorities

The strongest expert interpretation is that BDPLT22 reveals an unexpected, clinically important role for EPHB2 as a positive regulator of early GPVI and GPCR signaling. The disease is not simply a failure of classical ephrin-dependent platelet–platelet contact: receptor clustering remains intact, while kinase autophosphorylation and Src-family signaling are impaired. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 16-20)

The main unresolved questions are whether p.Arg745Cys is the only disease allele; how broadly EPHB2 deficiency affects megakaryopoiesis; whether heterozygotes have subclinical platelet phenotypes; which phosphatase/adaptor links EPHB2 to Src/Lyn; and which general IPD therapies are effective and safe in this genotype. Independent families, contemporary ClinVar/gnomAD reassessment, standardized platelet phenotyping, longitudinal outcome collection, and a knock-in model are required before reliable prevalence, penetrance, prognosis, or treatment-response estimates can be made.

## Key references

1. **Berrou E, et al.** “A mutation of the human EPHB2 gene leads to a major platelet functional defect.” *Blood*. Published November 2018;132(19):2067–2077. DOI/URL: https://doi.org/10.1182/blood-2018-04-845644. This is the foundational primary human and functional study. (berrou2018amutationof pages 1-5, berrou2018amutationof pages 5-9)
2. **Nurden P, Stritt S, Favier R, Nurden AT.** “Inherited platelet diseases with normal platelet count: phenotypes, genotypes and diagnostic strategy.” *Haematologica*. Online November 2020;106:337–350. DOI/URL: https://doi.org/10.3324/haematol.2020.248153. This authoritative review contextualizes EPHB2-related disease among inherited platelet-function disorders. (nurden2020inheritedplateletdiseases pages 6-7, nurden2020inheritedplateletdiseases pages 2-3)
3. **Bargehr C, Knöfler R, Streif W.** “Treatment of Inherited Platelet Disorders: Current Status and Future Options.” *Hämostaseologie*. Published August 2023;43:261–270. DOI/URL: https://doi.org/10.1055/a-2080-6602. This is current general IPD guidance; it is not BDPLT22-specific.

References

1. (berrou2018amutationof pages 1-5): Eliane Berrou, Christelle Soukaseum, Rémi Favier, Frédéric Adam, Ziane Elaib, Alexandre Kauskot, Jean-Claude Bordet, Paola Ballerini, Stephane Loyau, Miao Feng, Karine Dias, Abbas Muheidli, Stephane Girault, Alan T. Nurden, Ernest Turro, Willem H. Ouwehand, Cécile V. Denis, Martine Jandrot-Perrus, Jean-Philippe Rosa, Paquita Nurden, and Marijke Bryckaert. A mutation of the human ephb2 gene leads to a major platelet functional defect. Blood, 132 19:2067-2077, Nov 2018. URL: https://doi.org/10.1182/blood-2018-04-845644, doi:10.1182/blood-2018-04-845644. This article has 33 citations and is from a highest quality peer-reviewed journal.

2. (berrou2018amutationof pages 5-9): Eliane Berrou, Christelle Soukaseum, Rémi Favier, Frédéric Adam, Ziane Elaib, Alexandre Kauskot, Jean-Claude Bordet, Paola Ballerini, Stephane Loyau, Miao Feng, Karine Dias, Abbas Muheidli, Stephane Girault, Alan T. Nurden, Ernest Turro, Willem H. Ouwehand, Cécile V. Denis, Martine Jandrot-Perrus, Jean-Philippe Rosa, Paquita Nurden, and Marijke Bryckaert. A mutation of the human ephb2 gene leads to a major platelet functional defect. Blood, 132 19:2067-2077, Nov 2018. URL: https://doi.org/10.1182/blood-2018-04-845644, doi:10.1182/blood-2018-04-845644. This article has 33 citations and is from a highest quality peer-reviewed journal.

3. (nurden2020inheritedplateletdiseases pages 6-7): Paquita Nurden, Simon Stritt, Remi Favier, and Alan T. Nurden. Inherited platelet diseases with normal platelet count: phenotypes, genotypes and diagnostic strategy. Haematologica, 106:337-350, Nov 2020. URL: https://doi.org/10.3324/haematol.2020.248153, doi:10.3324/haematol.2020.248153. This article has 110 citations.

4. (berrou2018amutationof pages 20-25): Eliane Berrou, Christelle Soukaseum, Rémi Favier, Frédéric Adam, Ziane Elaib, Alexandre Kauskot, Jean-Claude Bordet, Paola Ballerini, Stephane Loyau, Miao Feng, Karine Dias, Abbas Muheidli, Stephane Girault, Alan T. Nurden, Ernest Turro, Willem H. Ouwehand, Cécile V. Denis, Martine Jandrot-Perrus, Jean-Philippe Rosa, Paquita Nurden, and Marijke Bryckaert. A mutation of the human ephb2 gene leads to a major platelet functional defect. Blood, 132 19:2067-2077, Nov 2018. URL: https://doi.org/10.1182/blood-2018-04-845644, doi:10.1182/blood-2018-04-845644. This article has 33 citations and is from a highest quality peer-reviewed journal.

5. (berrou2018amutationof pages 13-16): Eliane Berrou, Christelle Soukaseum, Rémi Favier, Frédéric Adam, Ziane Elaib, Alexandre Kauskot, Jean-Claude Bordet, Paola Ballerini, Stephane Loyau, Miao Feng, Karine Dias, Abbas Muheidli, Stephane Girault, Alan T. Nurden, Ernest Turro, Willem H. Ouwehand, Cécile V. Denis, Martine Jandrot-Perrus, Jean-Philippe Rosa, Paquita Nurden, and Marijke Bryckaert. A mutation of the human ephb2 gene leads to a major platelet functional defect. Blood, 132 19:2067-2077, Nov 2018. URL: https://doi.org/10.1182/blood-2018-04-845644, doi:10.1182/blood-2018-04-845644. This article has 33 citations and is from a highest quality peer-reviewed journal.

6. (berrou2018amutationof pages 16-20): Eliane Berrou, Christelle Soukaseum, Rémi Favier, Frédéric Adam, Ziane Elaib, Alexandre Kauskot, Jean-Claude Bordet, Paola Ballerini, Stephane Loyau, Miao Feng, Karine Dias, Abbas Muheidli, Stephane Girault, Alan T. Nurden, Ernest Turro, Willem H. Ouwehand, Cécile V. Denis, Martine Jandrot-Perrus, Jean-Philippe Rosa, Paquita Nurden, and Marijke Bryckaert. A mutation of the human ephb2 gene leads to a major platelet functional defect. Blood, 132 19:2067-2077, Nov 2018. URL: https://doi.org/10.1182/blood-2018-04-845644, doi:10.1182/blood-2018-04-845644. This article has 33 citations and is from a highest quality peer-reviewed journal.

7. (nurden2020inheritedplateletdiseases pages 10-11): Paquita Nurden, Simon Stritt, Remi Favier, and Alan T. Nurden. Inherited platelet diseases with normal platelet count: phenotypes, genotypes and diagnostic strategy. Haematologica, 106:337-350, Nov 2020. URL: https://doi.org/10.3324/haematol.2020.248153, doi:10.3324/haematol.2020.248153. This article has 110 citations.

8. (nurden2020inheritedplateletdiseases pages 2-3): Paquita Nurden, Simon Stritt, Remi Favier, and Alan T. Nurden. Inherited platelet diseases with normal platelet count: phenotypes, genotypes and diagnostic strategy. Haematologica, 106:337-350, Nov 2020. URL: https://doi.org/10.3324/haematol.2020.248153, doi:10.3324/haematol.2020.248153. This article has 110 citations.

## Artifacts

- [Edison artifact artifact-00](Platelet-type_Bleeding_Disorder_22-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032765` (4 mentions) - the report calls it "if available"; MONDO calls it **bleeding disorder, platelet-type, 22**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.
