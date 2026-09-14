---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T14:09:09.816411'
end_time: '2026-09-06T14:20:32.104217'
duration_seconds: 682.29
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: LDLR-Related Familial Hypercholesterolemia
  mondo_id: MONDO:0007750
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 51
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  quotes_not_checkable: 1
  relevance_assessed: 16
  on_topic: 9
  validator_version: 0.2.1
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0007750
    reported_labels:
    - if available
    - association score 0.877
    ontology_label: hypercholesterolemia, familial, 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: LDLR-Related_Familial_Hypercholesterolemia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** LDLR-Related Familial Hypercholesterolemia
- **MONDO ID:** MONDO:0007750 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **LDLR-Related Familial Hypercholesterolemia** covering all of the
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
- **Disease Name:** LDLR-Related Familial Hypercholesterolemia
- **MONDO ID:** MONDO:0007750 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **LDLR-Related Familial Hypercholesterolemia** covering all of the
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


# LDLR-Related Familial Hypercholesterolemia

## Scope and evidence conventions

This report concerns **familial hypercholesterolemia type 1 caused by germline pathogenic variants in LDLR**, not the broader phenotypic category that also includes APOB-, PCSK9-, APOE-, and LDLRAP1-related disease or polygenic hypercholesterolemia. Many epidemiologic and therapeutic studies enroll clinical FH or HoFH without reporting gene-specific results; these are explicitly labeled **broad-FH evidence** and should not be entered as LDLR-specific penetrance or treatment estimates.

The evidence base consists principally of aggregated disease resources, human cohorts and trials, recent authoritative reviews, and model-organism studies—not individual-patient EHR data. The principal recent sources are Di Taranto and Fortunato (published 6 February 2023; DOI [10.3390/ijms24043224](https://doi.org/10.3390/ijms24043224)), Abifadel and Boileau (2023; DOI [10.1111/joim.13577](https://doi.org/10.1111/joim.13577)), Fularski et al. (January 2024; DOI [10.3390/ijms25031637](https://doi.org/10.3390/ijms25031637)), and the 2024 pediatric PCSK9-inhibitor meta-analysis (published 8 October 2024; DOI [10.3390/medicina60101646](https://doi.org/10.3390/medicina60101646)). (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, taranto2023geneticheterogeneityof pages 1-2, abifadel2023geneticandmolecular pages 1-2, xiao2024efficacyandsafety pages 1-2)

| Domain | Key knowledge-base fact/statistic | Evidence type and scope | Source/date | DOI or URL |
|---|---|---|---|---|
| Identity | LDLR-related familial hypercholesterolemia 1 is MONDO:0007750; LDLR is the strongest associated target in the retrieved Open Targets record (score 0.877). | Aggregated disease-target evidence; LDLR-specific. | Open Targets, accessed 2026-09-06 (OpenTargets Search: familial hypercholesterolemia-LDLR) | https://platform.opentargets.org/ |
| Prevalence | Broad HeFH prevalence estimates cluster near 1:250-1:313. These figures include non-LDLR forms of FH. | Meta-analysis and review; broad FH, so application to LDLR-related disease is approximate. | Di Taranto and Fortunato, Feb 2023; Humphries and Futema, Apr 2025 (humphries2025geneticdeterminantsof pages 1-2, taranto2023geneticheterogeneityof pages 1-2) | https://doi.org/10.3390/ijms24043224; https://doi.org/10.1111/ahg.12594 |
| Causal contribution | Pathogenic LDLR variants account for approximately 90-95% of monogenic FH in cited reviews; estimates vary with ascertainment and testing strategy. | Aggregated genetic evidence; LDLR-specific attribution within broad monogenic FH. | Fularski et al., Jan 2024; Kalwick and Roth, Feb 2025 (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, kalwick2025acomprehensivereview pages 1-3) | https://doi.org/10.3390/ijms25031637; https://doi.org/10.3390/nu17040659 |
| Inheritance | One germline pathogenic LDLR allele generally causes heterozygous FH; two pathogenic alleles cause homozygous or compound-heterozygous LDLR-FH. Each child of a heterozygote has an approximately 50% chance of inheriting the variant. | Human genetic evidence; LDLR-specific, although HoFH can also arise from other genes. | Abifadel and Boileau, Oct 2023; Fularski et al., Jan 2024 (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, abifadel2023geneticandmolecular pages 1-2) | https://doi.org/10.1111/joim.13577; https://doi.org/10.3390/ijms25031637 |
| Variant classes | LDLR defects can impair receptor synthesis or transport, LDL binding, clathrin-mediated internalization, or receptor recycling. Null alleles abolish function and generally produce more severe disease than receptor-defective alleles. Copy-number changes may constitute about 10% of causal variants; deep-intronic variants may require WGS. | Molecular and genetic review; LDLR-specific, but the 10% estimate is cohort-dependent. | Fularski et al., Jan 2024 (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5) | https://doi.org/10.3390/ijms25031637 |
| Mechanism | Reduced hepatocyte-surface LDLR activity impairs receptor-mediated LDL uptake, elevates LDL-C from birth, and increases cumulative arterial LDL exposure. PCSK9-mediated lysosomal degradation further reduces LDLR recycling. | Established molecular mechanism; LDLR-specific, with PCSK9 acting as a pathway regulator. | Fularski et al., Jan 2024; Abifadel and Boileau, Oct 2023 (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, abifadel2023geneticandmolecular pages 1-2) | https://doi.org/10.3390/ijms25031637; https://doi.org/10.1111/joim.13577 |
| Phenotypes | Core findings include lifelong elevated LDL-C, tendon or cutaneous xanthomas, xanthelasma, corneal arcus, progressive premature atherosclerosis, coronary heart disease, and increased cardiovascular morbidity and mortality. | Clinical review; broad FH but strongly applicable to LDLR-FH. | Abifadel and Boileau, Oct 2023; Fularski et al., Jan 2024 (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, abifadel2023geneticandmolecular pages 1-2) | https://doi.org/10.1111/joim.13577; https://doi.org/10.3390/ijms25031637 |
| Severe natural history | In severe untreated HoFH, coronary disease and aortic stenosis may occur by age 20, death may occur by age 30, and myocardial infarction can occur before age 10. | Clinical review; broad HoFH and not restricted to biallelic LDLR disease. | Fularski et al., Jan 2024 (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5) | https://doi.org/10.3390/ijms25031637 |
| Diagnosis | Diagnosis integrates repeated fasting LDL-C measurements, premature ASCVD or family history, tendon xanthomas or corneal arcus, and exclusion of secondary causes. Dutch Lipid Clinic Network categories are definite above 8, probable 6-8, and possible 3-5 points. | Clinical diagnostic framework; broad FH. | Fularski et al., Jan 2024 (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4) | https://doi.org/10.3390/ijms25031637 |
| Molecular testing | Testing should include LDLR and other canonical FH genes plus deletion-duplication analysis; WGS can identify deep-intronic or structural variants. A negative test does not exclude clinical FH. | Clinical genetics review; LDLR testing within a broad FH differential. | Fularski et al., Jan 2024; Humphries and Futema, Apr 2025 (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, humphries2025geneticdeterminantsof pages 1-2) | https://doi.org/10.3390/ijms25031637; https://doi.org/10.1111/ahg.12594 |
| Cascade screening | Once a familial pathogenic variant is known, first-degree relatives should receive targeted variant testing and lipid measurement; their prior risk is approximately 50% under dominant inheritance. | Guideline and review evidence; LDLR-specific when the familial variant is in LDLR. | Fularski et al., Jan 2024; Abifadel and Boileau, Oct 2023 (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, abifadel2023geneticandmolecular pages 1-2) | https://doi.org/10.3390/ijms25031637; https://doi.org/10.1111/joim.13577 |
| Screening implementation | Childhood programs reported approximately 91% acceptance among Slovenian five-year-olds using opt-out screening and approximately 60% participation in a West Virginia school program. | Real-world implementation summarized in a review; broad FH. | Gidding, Oct 2023 (gidding2023childhoodscreeningfor pages 4-6) | https://doi.org/10.1016/j.jacc.2023.07.028 |
| Pediatric statins | A 20-year cohort of 214 children reported mean LDL-C reduction from 237.3 to 160.7 mg/dL, or 32%; 20% attained LDL-C below 100 mg/dL. By age 39, cardiovascular events were 1% versus 26% and cardiovascular death was 0% versus 7% compared with affected parents. | Human longitudinal cohort; broad genetically confirmed FH and probably predominantly LDLR, but not exclusively LDLR-specific. | Luirink et al., Oct 2019 | https://doi.org/10.1056/NEJMoa1816454 |
| Pediatric PCSK9 antibodies | A 2024 meta-analysis of nine studies, including three RCTs with 320 children, found LDL-C reduction of 37.92% (95% CI 32.78-43.06), apoB reduction of 33.67%, and Lp(a) reduction of 16.94%. Responses were consistent in HeFH but highly variable in HoFH. | Systematic review and meta-analysis; broad pediatric FH; treatment is mechanistically LDLR-dependent. | Xiao et al., Oct 8, 2024 (xiao2024efficacyandsafety pages 5-8, xiao2024efficacyandsafety pages 1-2, xiao2024efficacyandsafety pages 4-5) | https://doi.org/10.3390/medicina60101646 |
| Apheresis | One LDL-apheresis procedure conventionally lowers LDL-C by more than 60%. Weekly treatment can regress xanthomas, slow atherosclerosis, and improve survival; initiation before age 6-7 years is recommended for severe HoFH where available. | Clinical review and real-world practice; broad HoFH, not LDLR-specific. | Tokgozoglu and Kayikcioglu, Sep 2021 (tokgozoglu2021familialhypercholesterolemiaglobal pages 9-10) | https://doi.org/10.1007/s11886-021-01565-5 |
| Lifestyle interaction | Among carriers of pathogenic variants in LDLR, APOB, or PCSK9, estimated CAD risk by age 75 ranged from 35% with a favorable lifestyle to 66% with an unfavorable lifestyle. | Human case-control and cohort evidence; broad FH-gene carriers, not LDLR-specific. | Fahed et al., Mar 2022 | https://doi.org/10.1001/jamanetworkopen.2022.2687 |
| Sex disparity | Across 25 real-world studies with 129,441 participants, women were less likely to receive lipid-lowering therapy (OR 0.74, 95% CI 0.66-0.85) or attain LDL-C below 2.5 mmol/L (OR 0.85, 95% CI 0.74-0.97); fixed-dose trial response did not differ by sex. | Systematic review and meta-analysis; broad FH, not LDLR-specific. | Iatan et al., Jul 2024 (iatan2024sexdifferencesin pages 8-8) | https://doi.org/10.1093/eurheartj/ehae417 |
| Mouse model | Ldlr-null mice model impaired LDL clearance and diet-accelerated atherosclerosis, but murine lipoprotein metabolism differs from that of humans and a cholesterol-rich diet is often needed for severe disease. | Genetic model-organism evidence; LDLR-specific model, summarized from retrieved model literature. | Contemporary model reviews | https://www.informatics.jax.org/ |
| Rabbit model | Naturally occurring LDLR-deficient Watanabe heritable hyperlipidemic rabbits and the WHHLMI strain develop LDL-rich hypercholesterolemia, coronary atherosclerosis, vulnerable plaques, and myocardial infarction; lipoprotein physiology is more human-like than in mice. | Natural and genetic animal model; LDLR-specific model. | Established comparative-model literature | https://doi.org/10.1590/1414-431X20209557 |
| Nonhuman-primate model | Six genome-edited LDLR-knockout cynomolgus monkeys had severe hyperlipidemia resembling biallelic LDLR-FH, elevated VLDL and LDL, decreased HDL, periocular xanthoma by one year, and strong resistance to lipid-lowering medication. | Primary genome-edited model-organism study; LDLR-specific. | Sato et al., Sep 2023 | https://doi.org/10.1038/s41598-023-42763-1 |


*Table: Compact evidence map for LDLR-related familial hypercholesterolemia, distinguishing LDLR-specific findings from evidence generalized from broader FH or HoFH populations. It summarizes identity, genetics, clinical features, diagnosis, interventions, disparities, and experimental models.*

## 1. Disease information

**Definition.** LDLR-related FH is a congenital, lifelong disorder of LDL clearance caused by reduced quantity or function of the hepatocyte low-density-lipoprotein receptor. One pathogenic allele generally produces heterozygous FH (HeFH); biallelic pathogenic variants produce severe homozygous or compound-heterozygous LDLR-FH. Persistent LDL-cholesterol elevation causes cumulative arterial cholesterol exposure, premature atherosclerotic cardiovascular disease (ASCVD), and, in severe biallelic disease, childhood xanthomas and early coronary or aortic-root disease. LDLR variants account for approximately **90–95% of molecularly defined monogenic FH**, although estimates vary by ascertainment. (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, kalwick2025acomprehensivereview pages 1-3)

**Identifiers and synonyms.** Recommended identifiers are **MONDO:0007750**, “hypercholesterolemia, familial, 1”; **OMIM #143890**, familial hypercholesterolemia 1; causal gene **LDLR, OMIM *606945**; and MeSH **Familial Hypercholesterolemia**. Broader FH maps to MONDO:0005439, while homozygous FH has MONDO:0018328; neither should replace MONDO:0007750 in an LDLR-specific record. Open Targets identifies LDLR as the strongest associated target for MONDO:0007750 (association score 0.877). Common names include *LDLR-related familial hypercholesterolemia*, *familial hypercholesterolemia type 1*, *autosomal dominant hypercholesterolemia type 1*, *LDL-receptor deficiency*, *HeFH due to LDLR*, and *biallelic/homozygous LDLR-FH*. (OpenTargets Search: familial hypercholesterolemia-LDLR)

ICD coding is less gene-specific: **ICD-10-CM E78.01** denotes familial hypercholesterolemia, while ICD-11 generally classifies it among genetic disorders of lipoprotein metabolism. ICD codes should therefore be paired with the molecular diagnosis rather than treated as LDLR-specific identifiers.

## 2. Etiology, risk, protection, and gene–environment interaction

The initiating cause is a **germline loss-of-function LDLR variant**. De novo variants occur but are uncommon; most cases segregate in families. Null alleles, which produce no functional receptor, generally cause higher LDL-C and greater ASCVD burden than receptor-defective alleles retaining residual function. Copy-number variants may represent roughly 10% of molecular diagnoses in some series, and deep-intronic defects may be missed unless RNA studies or genome sequencing are used. (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5)

**Genetic severity factors** include biallelic LDLR variants, null/null genotypes, high polygenic LDL-C burden, elevated Lp(a), and variants affecting interacting pathways. PCSK9 is a mechanistic modifier: increased PCSK9 activity promotes lysosomal LDLR degradation, whereas PCSK9 loss-of-function preserves receptor abundance and lowers LDL-C and coronary risk. Modifier and polygenic effects explain part—but not all—of variable expressivity. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, taranto2023geneticheterogeneityof pages 1-2)

**Environmental/lifestyle factors** do not cause LDLR-FH but alter realized ASCVD risk. Smoking, hypertension, diabetes, obesity, physical inactivity, and diets rich in saturated/trans fat add to lifelong LDL burden. In 10,175 case-control and 39,920 cohort participants carrying pathogenic variants in LDLR, APOB, or PCSK9, projected CAD risk by age 75 ranged from **35% with a favorable lifestyle to 66% with an unfavorable lifestyle**. This is compelling gene–environment evidence, but it was not reported separately for LDLR. Its abstract conclusion states that “a favorable lifestyle is associated with a lower risk of coronary artery disease in carriers and noncarriers.” DOI: [10.1001/jamanetworkopen.2022.2687](https://doi.org/10.1001/jamanetworkopen.2022.2687). 

Protective factors include early diagnosis, lifelong adherence to LDL-lowering treatment, avoidance of tobacco, regular physical activity, healthy weight, and a dietary pattern low in saturated fat and rich in fiber and unsaturated fat. These reduce downstream risk but do not normalize receptor function. PCSK9 loss-of-function and other LDL-lowering alleles are plausible genetic protectors. No infectious, occupational, radiation, or toxin exposure is an established primary cause.

## 3. Phenotypes

| Phenotype | Type, onset, course, frequency | Suggested HPO term |
|---|---|---|
| Elevated LDL-C | Laboratory abnormality; present from birth, persistent and usually severe; universal defining feature | **HP:0003124 Hypercholesterolemia** |
| Premature atherosclerosis/CAD | Usually subclinical in childhood in HeFH, clinically progressive in adulthood; childhood or adolescence in severe biallelic disease | **HP:0002621 Atherosclerosis**, **HP:0001677 Coronary artery atherosclerosis** |
| Tendon xanthomas | Physical sign; age-dependent, uncommon in adequately treated children, more frequent with severe or longstanding disease | **HP:0005039 Xanthomatosis**, tendon-xanthoma child term if supported locally |
| Cutaneous/planar or tuberous xanthomas | Particularly characteristic of severe biallelic disease; may appear in early childhood | **HP:0000991 Xanthoma** |
| Corneal arcus | Usually age-dependent; arcus before age 45 is diagnostically informative | **HP:0001084 Corneal arcus** |
| Xanthelasma | Variable and nonspecific; more likely with prolonged hypercholesterolemia | **HP:0001114 Xanthelasma** |
| Myocardial infarction/angina | Downstream clinical complication; adult-premature in HeFH, potentially childhood in null/null LDLR-FH | **HP:0001658 Myocardial infarction**, **HP:0001681 Angina pectoris** |
| Aortic-root/valvular disease | Especially severe HoFH; progressive supravalvular/aortic-root atherosclerosis and calcific aortic stenosis | **HP:0001646 Aortic stenosis** |
| Carotid/peripheral/cerebrovascular disease | Variable downstream manifestations of systemic atherosclerosis | **HP:0002635 Cerebral ischemia**, **HP:0004417 Peripheral arterial stenosis** |

Reviews consistently describe elevated LDL-C, tendon/skin xanthomas, xanthelasma, corneal arcus, and premature progressive ASCVD. In untreated severe HoFH, coronary disease and aortic stenosis may occur by age 20, death may occur by age 30, and myocardial infarction has occurred before age 10; these figures describe broad HoFH and should not be assigned to every biallelic LDLR genotype. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, abifadel2023geneticandmolecular pages 1-2)

Quality-of-life effects derive less from isolated hypercholesterolemia than from anxiety about inherited risk, polypharmacy, injectable treatment, apheresis schedules, dietary burden, ASCVD disability, and financial/access barriers. Robust LDLR-genotype-specific EQ-5D or SF-36 estimates were not identified; broad HoFH evidence should therefore not be entered as LDLR-specific QoL data.

## 4. Genetic and molecular information

**Gene.** LDLR is located at **19p13.2** and encodes the LDL receptor, a cell-surface transmembrane glycoprotein highly expressed by hepatocytes. Recommended identifiers are **HGNC:6547**, **NCBI Gene 3949**, and **Ensembl ENSG00000130164**.

**Variant spectrum.** Disease-causing variants include missense, nonsense, frameshift, canonical and noncanonical splice variants, promoter defects, in-frame indels, exon-level deletions/duplications, and larger structural rearrangements. Classic functional classes are: (1) absent synthesis; (2) defective ER-to-Golgi transport; (3) impaired APOB-containing LDL binding; (4) impaired clustering/internalization in clathrin-coated pits; and (5) abnormal endosomal dissociation or receptor recycling. Most are loss-of-function; dominant-negative behavior is not the usual mechanism. All are constitutional/germline rather than somatic. (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5)

**Classification.** Variants should be interpreted under ACMG/AMP criteria supplemented by ClinGen FH specifications, segregation, population frequency, LDLR activity assays, cell-surface abundance, LDL binding/uptake, and RNA studies. Pathogenic/likely pathogenic variants establish molecular LDLR-FH; a VUS does not. Clinically encountered pathogenic alleles are usually absent or extremely rare in gnomAD. A single universal allele-frequency cutoff is inappropriate because founder alleles can be locally enriched.

**Recent functional genomics.** A major post-2024 advance tested approximately **17,000 nearly all-possible LDLR coding variants** for cell-surface abundance and LDL uptake. Functional scores correlated with prospective human hyperlipidemia and improved inference when combined with polygenic scores. This 2026 Science study is beyond the requested 2023–2024 priority window but represents the current frontier; DOI [10.1126/science.ady7186](https://doi.org/10.1126/science.ady7186). Its abstract states that the maps “provide evidence for interpreting clinical variants.” (tabet2026thefunctionallandscape pages 1-3)

No recurrent aneuploidy, translocation, mitochondrial defect, repeat expansion, or somatic mosaic mechanism characterizes this disease. Large LDLR deletions/duplications are relevant; conventional karyotyping is not. Disease-specific DNA methylation, histone, single-cell, spatial-transcriptomic, proteomic, or metabolomic signatures are not validated diagnostic entities. Altered plasma LDL lipidomics is a direct biochemical consequence, not a unique omics classifier.

## 5. Environmental information

LDLR-FH is not caused by infection, pollution, radiation, or occupational exposure. Secondary hypercholesterolemia can intensify or mimic the phenotype and should be sought: hypothyroidism, nephrotic syndrome, cholestatic liver disease, uncontrolled diabetes, obesity, pregnancy, and LDL-raising drugs. Diet and exercise usually produce modest LDL changes relative to the inherited defect but materially affect total cardiovascular risk. Smoking is especially avoidable because it acts downstream on endothelial injury and thrombosis. No vaccine or antimicrobial prevention is applicable.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A germline pathogenic **LDLR** variant **leads to** absent, reduced, mislocalized, binding-defective, internalization-defective, or recycling-defective LDL receptor.
2. Reduced functional LDLR at the hepatocyte surface **results in** impaired receptor-mediated uptake of circulating APOB-100-containing LDL.
3. Impaired hepatic clearance **leads to** elevated plasma LDL-C from birth; biallelic/null variants **result in** the greatest elevation.
4. Lifelong elevated LDL-C **causes** increased arterial entry and retention of APOB-containing particles in the subendothelial extracellular matrix.
5. Retained LDL **undergoes** oxidative/enzymatic modification and **induces** endothelial activation, chemokine expression, and monocyte recruitment.
6. Monocyte-derived macrophages **internalize** modified LDL through scavenger pathways, **forming** foam cells and fatty streaks.
7. Persistent lipid retention and unresolved inflammation **lead to** smooth-muscle migration/proliferation, extracellular-matrix deposition, necrotic-core formation, and plaque calcification.
8. Plaque growth **results in** coronary, carotid, aortic-root, and peripheral stenosis; plaque disruption and thrombosis **cause** acute coronary syndrome, myocardial infarction, stroke, or sudden death.
9. **Branch:** extracellular cholesterol deposition in tendons, skin, and cornea **causes** xanthomas and corneal arcus.
10. **Branch in severe biallelic disease:** extreme LDL exposure at the aortic root/valve **leads to** supravalvular disease and calcific aortic stenosis. The exact patient-level rate is genotype- and treatment-dependent.

This chain is established through human genetics, receptor biochemistry, pathology, and model systems. LDLR mediates cell-surface endocytosis; PCSK9 binding diverts LDLR toward lysosomal degradation rather than recycling. Accordingly, statins, PCSK9 antibodies, and inclisiran require at least some residual receptor capacity, whereas ANGPTL3 inhibition, MTP inhibition, and apheresis act substantially independently of LDLR. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5, bourbon2026thespectrumof pages 8-10)

Suggested annotations include **GO:0006897 endocytosis**, **GO:0006869 lipid transport**, **GO:0008203 cholesterol metabolic process**, **GO:0034383 low-density lipoprotein particle clearance**, **GO:0006954 inflammatory response**, and **GO:0043277 apoptotic cell clearance**. Principal cell types are **hepatocyte (CL:0000182)**, vascular endothelial cell, arterial smooth-muscle cell, circulating monocyte, and macrophage/foam cell. Relevant compartments include **plasma membrane (GO:0005886)**, clathrin-coated pit, endosome, lysosome, endoplasmic reticulum, and Golgi apparatus.

## 7. Anatomical structures affected

The primary biochemical organ is the **liver**, particularly hepatocytes that normally clear most circulating LDL. Clinical injury occurs in the **arterial system**: coronary arteries and myocardium, aortic root and aortic valve, carotid and cerebral arteries, and peripheral arteries. Secondary cholesterol deposits affect Achilles and hand extensor tendons, pressure-bearing skin, eyelids, and peripheral cornea. Suggested terms include **UBERON:0002107 liver**, **UBERON:0000948 heart**, **UBERON:0001621 coronary artery**, **UBERON:0001496 ascending aorta**, **UBERON:0002137 aortic valve**, **UBERON:0001619 carotid artery**, **UBERON:0001769 cornea**, and **UBERON:0000979 Achilles tendon**. Findings are generally systemic/bilateral rather than lateralized.

## 8. Temporal development

The molecular and biochemical disease begins **congenitally**: LDL-C is elevated from birth and exposure accumulates continuously. HeFH often remains clinically silent through childhood, with subclinical endothelial or carotid changes preceding adult premature ASCVD. Biallelic/null disease may produce xanthomas in early childhood and coronary/aortic disease during childhood or adolescence. The course is chronic and progressive without treatment; spontaneous remission does not occur. Treatment lowers current LDL-C and future risk but does not erase prior cumulative exposure.

The critical intervention window is childhood, before substantial plaque develops. In a 20-year follow-up of 214 children with genetically confirmed FH in 98%, LDL-C fell from 237.3 to 160.7 mg/dL (32%). By age 39, cardiovascular events were **1% in treated offspring versus 26% in affected parents**, and cardiovascular mortality was **0% versus 7%**. The study concluded that childhood statins “slowed the progression of carotid intima-media thickness and reduced the risk of cardiovascular disease in adulthood” (NEJM, 17 October 2019; DOI [10.1056/NEJMoa1816454](https://doi.org/10.1056/NEJMoa1816454); PMID 31618540). This cohort was broad genetic FH, not an exclusively reported LDLR subgroup.

## 9. Inheritance and population

Inheritance is **autosomal dominant with gene-dose/semi-dominant severity**: each child of a heterozygous affected person has a 50% risk. Biallelic disease can result from homozygosity, compound heterozygosity, or, rarely, double heterozygosity across FH genes. Penetrance for elevated LDL-C is high but not literally complete; ASCVD penetrance is strongly age-, sex-, treatment-, allele-, Lp(a)-, and lifestyle-dependent. Expressivity is variable. Anticipation is not established. Germline mosaicism is possible in principle but is not a recognized major contributor.

Broad-FH meta-analyses estimate HeFH near **1:250–1:313**; one recent review cites approximately 1:280 carriers and HoFH near 3 per million. These are not LDLR-only prevalence estimates. Ethnicity-specific broad-FH estimates range from approximately 1:400 in Asian populations to 1:192 in Black/brown groups, partly reflecting ascertainment and founder effects. (humphries2025geneticdeterminantsof pages 1-2, taranto2023geneticheterogeneityof pages 1-2)

Founder variants produce substantially higher local prevalence in French Canadians, Afrikaners, Lebanese Christian groups, Ashkenazi Jews, Finns, and other isolates. Consanguinity increases the probability of biallelic disease. Both sexes inherit LDLR variants equally, but realized disease and care differ. A 2024 meta-analysis of 25 real-world studies (129,441 participants) found women less likely than men to receive lipid-lowering treatment (OR **0.74**, 95% CI 0.66–0.85) or reach LDL-C below 2.5 mmol/L (OR **0.85**, 95% CI 0.74–0.97), although fixed-dose trial response did not differ; men had approximately twice the relative risk of major cardiovascular events. This is broad-FH evidence. DOI [10.1093/eurheartj/ehae417](https://doi.org/10.1093/eurheartj/ehae417), July 2024. (iatan2024sexdifferencesin pages 8-8)

## 10. Diagnostics

Diagnosis combines: (1) at least two lipid measurements when clinically stable; (2) age-specific untreated LDL-C; (3) personal/family premature ASCVD; (4) tendon xanthomas or premature corneal arcus; (5) exclusion of secondary causes; and (6) molecular testing. Adult suspicion is high around untreated LDL-C ≥190 mg/dL (4.9 mmol/L); pediatric thresholds are lower and must be interpreted with family history. Dutch Lipid Clinic Network categories are **definite >8**, **probable 6–8**, and **possible 3–5** points. A pathogenic variant confirms molecular FH, but a negative result does not exclude clinical FH. (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, humphries2025geneticdeterminantsof pages 1-2)

**Recommended genetic workflow:** sequence LDLR, APOB, PCSK9, and—according to phenotype/inheritance—LDLRAP1 and phenocopy genes such as ABCG5, ABCG8, LIPA, and CYP27A1; include LDLR deletion/duplication analysis. Test the known familial variant directly in relatives. WES is useful when panels are negative or the phenotype is atypical but may miss CNVs and deep-intronic changes. WGS can identify structural and deep-intronic variants; RNA analysis may demonstrate aberrant splicing. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine unless another indication exists. (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4, taranto2023geneticheterogeneityof pages 1-2)

Differential diagnoses include polygenic hypercholesterolemia, APOB-/PCSK9-/APOE-related FH, autosomal-recessive LDLRAP1 disease, sitosterolemia, lysosomal-acid-lipase deficiency, cerebrotendinous xanthomatosis, familial combined hyperlipidemia, and secondary hypercholesterolemia. Lp(a) should be measured because its cholesterol contributes to measured LDL-C and independently raises risk.

**Screening.** Cascade testing of first-degree relatives is the most efficient LDLR-specific strategy because each has approximately 50% prior risk. Universal or child–parent screening can identify otherwise silent families. Real-world programs summarized in 2023 reported approximately **91% acceptance** among Slovenian five-year-olds using opt-out screening and about **60% participation** in a West Virginia school program. (gidding2023childhoodscreeningfor pages 4-6)

## 11. Outcome and prognosis

Untreated prognosis is dominated by premature coronary disease. Older natural-history estimates suggest untreated CHD by age 50 in approximately 50% of men and by age 60 in 30% of women with FH; these historical broad-FH figures predate modern combination therapy. Null alleles, biallelic disease, higher cumulative LDL-C, elevated Lp(a), smoking, diabetes, hypertension, existing ASCVD, and delayed treatment worsen prognosis. (humphries2025geneticdeterminantsof pages 1-2)

Treatment can dramatically normalize the trajectory: the long-term pediatric cohort showed carotid-intima–media-thickness progression similar to unaffected siblings and markedly fewer events than affected parents, although only 20% reached LDL-C below 100 mg/dL. Recovery from established infarction, stenosis, or calcific valve disease is incomplete; the practical goal is lifelong biochemical control and prevention of new events.

## 12. Treatment

Treatment is genotype-informed but risk-driven. Lifestyle therapy accompanies rather than replaces medication.

1. **High-intensity statin**—inhibits HMG-CoA reductase, activates SREBP2, and increases LDLR expression. First-line for HeFH; effect is reduced in receptor-null HoFH. Monitor transaminases and symptoms of myopathy. Suggested NCIT concept: *HMG-CoA Reductase Inhibitor Therapy*.
2. **Ezetimibe**—inhibits intestinal NPC1L1 cholesterol absorption and adds approximately 15–25% LDL-C lowering in typical FH practice. Suggested NCIT: *Ezetimibe Therapy*.
3. **PCSK9 monoclonal antibodies**—evolocumab or alirocumab preserve surface LDLR; response therefore depends on residual receptor function. A 2024 pediatric meta-analysis of nine studies, including three RCTs with 320 children, estimated LDL-C reduction of **37.92%** (95% CI 32.78–43.06), apoB reduction of **33.67%**, and Lp(a) reduction of **16.94%**. Effects were consistent in HeFH but highly variable in HoFH, and agents were generally well tolerated. (xiao2024efficacyandsafety pages 5-8, xiao2024efficacyandsafety pages 1-2)
4. **Inclisiran**—GalNAc-siRNA suppressing hepatic PCSK9 synthesis; twice-yearly maintenance dosing improves convenience but remains LDLR-dependent. Pediatric HeFH and HoFH phase 3 programs are active or recently completed; cardiovascular-outcome evidence and genotype-specific pediatric evidence remain less mature than LDL-C evidence.
5. **Bempedoic acid**—ATP-citrate-lyase inhibitor used in adults needing additional oral therapy or with statin intolerance; LDL lowering is substantially LDLR-mediated.
6. **Lomitapide**—MTP inhibitor that reduces VLDL assembly and LDL production independently of LDLR; reserved for HoFH. Important harms include diarrhea, transaminase elevation, hepatic steatosis, drug interactions, and teratogenic risk; a very-low-fat diet and liver monitoring are required.
7. **Evinacumab**—ANGPTL3 monoclonal antibody that lowers LDL-C largely independently of LDLR, making it especially valuable in null/null HoFH. Phase 3 programs include NCT03399786, NCT03409744, and pediatric NCT04233918. Access and intravenous administration remain limitations.
8. **Lipoprotein apheresis**—direct extracorporeal removal; one procedure conventionally lowers LDL-C by **>60%**, but rebound creates a saw-tooth exposure pattern. Weekly/biweekly therapy can regress xanthomas, slow atherosclerosis, and improve survival. In severe childhood HoFH, initiation before approximately age 6–7 is recommended where feasible. (tokgozoglu2021familialhypercholesterolemiaglobal pages 9-10)
9. **Liver transplantation**—replaces the principal organ expressing LDLR and can markedly normalize LDL clearance, but operative risk and lifelong immunosuppression restrict it to exceptional refractory biallelic disease.
10. **Pregnancy**—preconception counseling is essential. Statins and several systemic agents are usually stopped during pregnancy according to jurisdiction and individual risk; bile-acid sequestrants and apheresis are established non-systemic options. Severe HoFH requires specialist management.

Combination escalation—statin → ezetimibe → PCSK9-directed therapy, followed by LDLR-independent treatment or apheresis in severe biallelic disease—is standard. Pediatric evidence supports early statins; PCSK9 antibodies are added when targets remain unmet. Suggested CHEBI entities include cholesterol (**CHEBI:16113**) and low-density-lipoprotein cholesterol as the measured analyte; suggested NCIT intervention terms include statin therapy, cholesterol-absorption-inhibitor therapy, monoclonal-antibody therapy, siRNA therapy, therapeutic apheresis, and liver transplantation.

**Experimental therapy.** Liver-directed LDLR gene replacement, ex-vivo corrected hepatocytes, mRNA delivery, and genome editing remain investigational. Most current in-vivo editing programs reduce PCSK9 or ANGPTL3 rather than repair the diverse LDLR alleles. The 2023 literature identified PCSK9 inhibition, inclisiran, and gene therapy as leading research hotspots. (bourbon2026thespectrumof pages 8-10, taranto2023geneticheterogeneityof pages 1-2)

## 13. Prevention

Primary genetic prevention is not possible after conception. Reproductive options include genetic counseling, familial-variant prenatal testing, and preimplantation genetic testing, with nondirective counseling. Secondary prevention consists of universal/opportunistic lipid screening, molecular confirmation, cascade testing, and treatment before arterial injury. Tertiary prevention comprises intensive LDL-C lowering, tobacco avoidance, blood-pressure/diabetes management, antiplatelet therapy when otherwise indicated, and surveillance/treatment of coronary and aortic-valve disease.

There is no vaccine. Population priorities are clinician and public awareness, laboratory flagging of very high LDL-C, EHR case-finding, guaranteed cascade-testing pathways, pediatric screening, access to lipid specialists, and equitable availability of combination drugs and apheresis.

## 14. Other species and natural disease

LDLR orthologues and receptor-mediated LDL clearance are strongly conserved across mammals. Naturally occurring **Watanabe heritable hyperlipidemic rabbits** (*Oryctolagus cuniculus*, NCBI Taxon 9986) have LDLR deficiency, LDL-rich hypercholesterolemia, tendon/skin lesions, and spontaneous atherosclerosis. The selectively bred WHHLMI strain develops vulnerable coronary plaques and myocardial infarction and has been important in statin development. Rabbits better reproduce human LDL-dominant lipoprotein physiology than ordinary mice.

Naturally occurring LDLR-related hypercholesterolemia has also been described in some companion-animal families, but breed-specific evidence is too sparse for confident VBO annotations. The condition is inherited, not transmissible or zoonotic.

## 15. Model organisms

**Ldlr−/− mouse** (*Mus musculus*, Taxon 10090) is the standard high-throughput genetic model for LDL clearance, atherogenesis, inflammation, and therapeutic testing. It often requires a Western/cholesterol-rich diet for severe lesions; murine HDL-dominant physiology and limited spontaneous plaque rupture constrain translation.

**WHHL/WHHLMI rabbit** provides more human-like LDL-rich plasma and spontaneous coronary disease, but breeding, cost, and genetic manipulation are less convenient than in mice.

**LDLR-null hamster** more closely models human lipoprotein handling and diet-induced coronary atherosclerosis than mice. **Zebrafish** support developmental and high-throughput lipid studies but incompletely reproduce human coronary disease.

A major recent model advance was six CRISPR-edited **LDLR-knockout cynomolgus monkeys** (*Macaca fascicularis*, Taxon 9541). All had confirmed LDLR mutations, markedly elevated cholesterol/triglycerides, elevated VLDL/LDL, reduced HDL, periocular xanthoma by one year, and strong resistance to lipid-lowering medication—closely approximating biallelic LDLR-FH. The authors concluded that the phenotype was “similar to that of homozygous FH patients” (Scientific Reports, September 2023; DOI [10.1038/s41598-023-42763-1](https://doi.org/10.1038/s41598-023-42763-1)). Its limitations are cost, ethics, small sample size, and complete knockout being more severe than many human missense genotypes.

Cellular systems include patient fibroblasts, LDLR-null hepatoma cells, iPSC-derived hepatocyte-like cells, and CRISPR knock-in cells. These quantify LDLR maturation, surface abundance, LDL binding/uptake, endocytosis, and recycling and are especially important for resolving missense/splice VUS.

## Knowledge-base cautions and gaps

* Enter **MONDO:0007750 + a pathogenic/likely pathogenic LDLR variant** for the gene-specific disorder; do not equate every clinical FH or HoFH case with LDLR disease.
* Frequencies of individual manifestations, allele-specific penetrance, and treatment effects are often unavailable because cohorts combine causal genes.
* Disease-specific epigenetic, single-cell, spatial, proteomic, and metabolomic biomarkers are not clinically validated.
* The strongest evidence supports LDL-C concentration and cumulative exposure as biomarkers, LDLR genotype/residual activity as severity and treatment-response modifiers, and early sustained LDL lowering as the principal determinant of improved prognosis.

References

1. (fularski2024unveilingfamilialhypercholesterolemia—review pages 2-4): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 30 citations.

2. (taranto2023geneticheterogeneityof pages 1-2): Maria Donata Di Taranto and Giuliana Fortunato. Genetic heterogeneity of familial hypercholesterolemia: repercussions for molecular diagnosis. Feb 2023. URL: https://doi.org/10.3390/ijms24043224, doi:10.3390/ijms24043224. This article has 54 citations.

3. (abifadel2023geneticandmolecular pages 1-2): Marianne Abifadel and Catherine Boileau. Genetic and molecular architecture of familial hypercholesterolemia. Oct 2023. URL: https://doi.org/10.1111/joim.13577, doi:10.1111/joim.13577. This article has 189 citations and is from a domain leading peer-reviewed journal.

4. (xiao2024efficacyandsafety pages 1-2): Guoguang Xiao, Shan Gao, Yongmei Xie, Zhiling Wang, and Min Shu. Efficacy and safety of evolocumab and alirocumab as pcsk9 inhibitors in pediatric patients with familial hypercholesterolemia: a systematic review and meta-analysis. Medicina, 60(10):1646, Oct 2024. URL: https://doi.org/10.3390/medicina60101646, doi:10.3390/medicina60101646. This article has 10 citations.

5. (OpenTargets Search: familial hypercholesterolemia-LDLR): Open Targets Query (familial hypercholesterolemia-LDLR, 34 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (humphries2025geneticdeterminantsof pages 1-2): Steve Eric Humphries and Marta Futema. Genetic determinants of the familial hypercholesterolaemia phenotype. Annals of Human Genetics, 89:293-304, Apr 2025. URL: https://doi.org/10.1111/ahg.12594, doi:10.1111/ahg.12594. This article has 10 citations and is from a peer-reviewed journal.

7. (kalwick2025acomprehensivereview pages 1-3): Megan Kalwick and Mendel Roth. A comprehensive review of the genetics of dyslipidemias and risk of atherosclerotic cardiovascular disease. Feb 2025. URL: https://doi.org/10.3390/nu17040659, doi:10.3390/nu17040659. This article has 13 citations.

8. (fularski2024unveilingfamilialhypercholesterolemia—review pages 4-5): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 30 citations.

9. (gidding2023childhoodscreeningfor pages 4-6): Samuel S. Gidding. Childhood screening for familial hypercholesterolemia: jacc review topic of the week. Journal of the American College of Cardiology, 82 15:1558-1563, Oct 2023. URL: https://doi.org/10.1016/j.jacc.2023.07.028, doi:10.1016/j.jacc.2023.07.028. This article has 11 citations and is from a highest quality peer-reviewed journal.

10. (xiao2024efficacyandsafety pages 5-8): Guoguang Xiao, Shan Gao, Yongmei Xie, Zhiling Wang, and Min Shu. Efficacy and safety of evolocumab and alirocumab as pcsk9 inhibitors in pediatric patients with familial hypercholesterolemia: a systematic review and meta-analysis. Medicina, 60(10):1646, Oct 2024. URL: https://doi.org/10.3390/medicina60101646, doi:10.3390/medicina60101646. This article has 10 citations.

11. (xiao2024efficacyandsafety pages 4-5): Guoguang Xiao, Shan Gao, Yongmei Xie, Zhiling Wang, and Min Shu. Efficacy and safety of evolocumab and alirocumab as pcsk9 inhibitors in pediatric patients with familial hypercholesterolemia: a systematic review and meta-analysis. Medicina, 60(10):1646, Oct 2024. URL: https://doi.org/10.3390/medicina60101646, doi:10.3390/medicina60101646. This article has 10 citations.

12. (tokgozoglu2021familialhypercholesterolemiaglobal pages 9-10): Lale Tokgozoglu and Meral Kayikcioglu. Familial hypercholesterolemia: global burden and approaches. Current Cardiology Reports, 23:1-13, Sep 2021. URL: https://doi.org/10.1007/s11886-021-01565-5, doi:10.1007/s11886-021-01565-5. This article has 126 citations and is from a peer-reviewed journal.

13. (iatan2024sexdifferencesin pages 8-8): Iulia Iatan, Leo E Akioyamen, Isabelle Ruel, Amanda Guerin, Lindsay Hales, Thais Coutinho, Liam R Brunham, and Jacques Genest. Sex differences in treatment of familial hypercholesterolaemia: a meta-analysis. European Heart Journal, 45:3231-3250, Jul 2024. URL: https://doi.org/10.1093/eurheartj/ehae417, doi:10.1093/eurheartj/ehae417. This article has 44 citations and is from a highest quality peer-reviewed journal.

14. (tabet2026thefunctionallandscape pages 1-3): Daniel R. Tabet, Atina G. Coté, Megan C. Lancaster, Jochen Weile, Ashyad Rayhan, Iosifina Fotiadou, Nishka Kishore, Roujia Li, Da Kuang, Jennifer J. Knapp, Carmela S. Carrero, Olivia Taverniti, Anna Axakova, Jack M. P. Castelli, Mohammad M. Islam, Shahin Sowlati-Hashjin, Aanshi Gandhi, Ranim Maaieh, Michael Garton, Kenneth Matreyek, Douglas M. Fowler, Mafalda Bourbon, Simon G. Pfisterer, Andrew M. Glazer, Brett M. Kroncke, Victoria N. Parikh, Euan A. Ashley, Joshua W. Knowles, Melina Claussnitzer, Elizabeth T. Cirulli, Robert A. Hegele, Dan M. Roden, Calum A. MacRae, and Frederick P. Roth. The functional landscape of coding variation in the familial hypercholesterolemia gene <i>ldlr</i>. Science, 391(6787):eady7186-eady7186, Feb 2026. URL: https://doi.org/10.1126/science.ady7186, doi:10.1126/science.ady7186. This article has 41 citations and is from a highest quality peer-reviewed journal.

15. (bourbon2026thespectrumof pages 8-10): M. Bourbon, A. C. Alves, J. R. Chora, A. J. Hooper, and M. Abifadel. The spectrum of genetic causes of familial hypercholesterolemia phenotype. Jul 2026. URL: https://doi.org/10.1007/s11883-026-01435-x, doi:10.1007/s11883-026-01435-x. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](LDLR-Related_Familial_Hypercholesterolemia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 16 |
| On topic | 9 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1056/NEJMoa1816454`: "slowed the progression of carotid intima-media thickness and reduced the risk of cardiovascular disease in adulthood"
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007750` (6 mentions) - the report calls it "if available", "association score 0.877"; MONDO calls it **hypercholesterolemia, familial, 1**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0007750` - called "if available", "association score 0.877"