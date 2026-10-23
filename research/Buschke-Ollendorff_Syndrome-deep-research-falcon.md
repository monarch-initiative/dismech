---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T17:58:29.856732'
end_time: '2026-09-05T18:07:14.349992'
duration_seconds: 524.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Buschke-Ollendorff Syndrome
  mondo_id: MONDO:0008157
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 19
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0008157
    reported_labels:
    - if available
    ontology_label: Buschke-Ollendorff syndrome
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Buschke-Ollendorff_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Buschke-Ollendorff Syndrome
- **MONDO ID:** MONDO:0008157 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Buschke-Ollendorff Syndrome** covering all of the
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
- **Disease Name:** Buschke-Ollendorff Syndrome
- **MONDO ID:** MONDO:0008157 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Buschke-Ollendorff Syndrome** covering all of the
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


# Buschke–Ollendorff Syndrome: Disease Characteristics Research Report

## Executive summary

Buschke–Ollendorff syndrome (BOS) is a rare autosomal-dominant genodermatosis/sclerosing bone dysplasia defined by connective-tissue nevi together with osteopoikilosis. It is usually caused by heterozygous germline loss-of-function variants in **LEMD3**, encoding the inner-nuclear-membrane protein MAN1. MAN1 normally restrains BMP and activin/TGF-β signaling through receptor-regulated SMADs; haploinsufficiency therefore perturbs connective-tissue and bone homeostasis. Typical disease is benign, variably expressed, and often recognized from childhood skin lesions or incidental periarticular “spotted bone” lesions on radiographs. No disease-modifying therapy or validated BOS-specific clinical trial exists; care is symptom-directed. (mumm2007deactivatinggermlinemutations pages 1-2, hellemans2004lossoffunctionmutationsin pages 1-2, frost2020modelingbasedboneformation pages 1-7, hellemans2004lossoffunctionmutationsin pages 4-5)

| Knowledge-base field | Curated summary | Ontology / representative data | Evidence |
|---|---|---|---|
| Identity and identifiers | Buschke–Ollendorff syndrome (BOS) is a rare Mendelian genodermatosis and sclerosing bone dysplasia defined by connective-tissue nevi with osteopoikilosis. Melorheostosis may coexist, but sporadic melorheostosis is genetically distinct. Synonyms include dermatofibrosis lenticularis disseminata with osteopoikilosis and dermato-osteopoikilosis. | MONDO:0008157; OMIM/MIM 166700 | (mumm2007deactivatinggermlinemutations pages 1-2, hellemans2004lossoffunctionmutationsin pages 1-2, korman2016mutationinlemd3 pages 1-2) |
| Defining phenotype | Usually asymmetrical, non-tender, flesh-colored to yellow papules, nodules, or cobblestone plaques representing elastoma, collagenoma, or mixed connective-tissue nevi. Radiographs show multiple small, round or ovoid, generally symmetric periarticular sclerotic bone islands, especially in epiphyses, metaphyses, pelvis, carpal bones, and tarsal bones. | Suggested HPO: Connective tissue nevus; Collagenoma; Osteopoikilosis (HP:0005681); Melorheostosis (HP:0005781); Arthralgia (HP:0002829); Joint contracture (HP:0001371) | (mumm2007deactivatinggermlinemutations pages 1-2, brodbeck2016thebuschke–ollendorffsyndrome pages 1-3, tan2025clinicalandhistopathological pages 1-2) |
| Causal gene and inheritance | Heterozygous germline loss-of-function variants in **LEMD3** (MAN1) cause autosomal-dominant BOS through haploinsufficiency. Expression is highly variable within families, and not every clinically affected family has an identifiable coding variant. No reliable genotype–phenotype correlation is established. | **LEMD3**; ENSG00000174106. Representative variants: c.1323C>A, p.Tyr441Ter; c.332_333insTC; c.1863G>A, p.Trp621Ter; c.2203C>T, p.Arg735Ter. Reported classes include nonsense, frameshift, splice-disrupting, and larger deletion variants. | (OpenTargets Search: Buschke-Ollendorff syndrome-LEMD3, korman2016mutationinlemd3 pages 2-4, mumm2007deactivatinggermlinemutations pages 1-2, steensel2008buschkeollendorfsyndromereport pages 1-2) |
| Mechanism | MAN1 is an integral inner-nuclear-membrane protein whose C-terminal region binds receptor-regulated SMADs. Loss of MAN1-mediated antagonism increases BMP and TGF-β/activin signaling. This plausibly promotes abnormal dermal extracellular-matrix accumulation and focal osteogenesis. Human bone biopsies support activation of bone-lining cells and modeling-based formation of compact lamellar bone, although the complete tissue-selective causal chain remains unresolved. | Suggested GO: inner nuclear membrane (GO:0005637); BMP signaling pathway (GO:0030509); TGF-β receptor signaling pathway (GO:0007179); SMAD protein signal transduction (GO:0060395); ossification (GO:0001503); extracellular-matrix organization (GO:0030198). Suggested CL: fibroblast (CL:0000057); osteoblast (CL:0000062). | (hellemans2004lossoffunctionmutationsin pages 1-2, hellemans2004lossoffunctionmutationsin pages 4-5, frost2020modelingbasedboneformation pages 1-7) |
| Onset and course | Connective-tissue nevi most often begin congenitally, in infancy, or during childhood, but delayed adult presentation occurs. Lesions may enlarge slowly. Osteopoikilosis is developmental, persistent, and commonly detected incidentally. Severity ranges from asymptomatic disease to uncommon pain, contracture, deformity, or restricted motion. | Suggested HPO onset: Congenital onset (HP:0003577); Infantile onset (HP:0003593); Childhood onset (HP:0011463). Course: chronic and usually stable or slowly progressive. | (mumm2007deactivatinggermlinemutations pages 1-2, korman2016mutationinlemd3 pages 1-2, tan2025clinicalandhistopathological pages 1-2) |
| Diagnosis | Diagnosis integrates dermatologic examination, characteristic plain radiographs, family history, and, when needed, skin biopsy and germline **LEMD3** sequencing with deletion/duplication analysis. Histology may show thick disorganized elastic fibers, dense collagen bundles, mixed lesions, or mucin. Important differentials include isolated osteopoikilosis, osteoblastic metastases, mastocytosis, tuberous-sclerosis shagreen patch, familial or eruptive collagenoma, papular elastorrhexis, morphea, and melorheostosis. | Genetic marker: pathogenic or likely pathogenic germline **LEMD3** variant. Suggested procedures: radiography; skin biopsy; sequence analysis; copy-number analysis. | (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3, tan2025clinicalandhistopathological pages 1-2, steensel2008buschkeollendorfsyndromereport pages 1-2, mumm2007deactivatinggermlinemutations pages 1-2) |
| Epidemiology | Frequently cited occurrence is approximately 1 in 20,000, but this is an estimate rather than a robust population-registry measurement. BOS-specific incidence, sex ratio, ethnic differences, carrier frequency, and geographic variation remain undetermined. | Rare disease; no validated population-stratified prevalence dataset | (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3, frost2020modelingbasedboneformation pages 1-7, tan2025clinicalandhistopathological pages 1-2) |
| Treatment and prognosis | No disease-modifying or genotype-directed therapy is established. Most asymptomatic patients require reassurance and observation. Management is individualized and may include analgesia or physical therapy for musculoskeletal symptoms, dermatologic procedures for troublesome nevi, and orthopedic intervention for substantial deformity, contracture, or impingement. Prognosis and life expectancy are generally normal because typical osteopoikilosis and skin lesions are benign. | Suggested NCIT intervention concepts: Observation; Genetic Counseling; Analgesic Therapy; Physical Therapy; Surgical Procedure | (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3, korman2016mutationinlemd3 pages 2-4) |
| Evidence gaps | No validated protective or environmental risk factors, gene–environment interaction, epigenomic signature, circulating biomarker, formal staging system, disease-specific quality-of-life instrument, pharmacogenomic guidance, approved targeted therapy, or relevant interventional clinical trial was identified. No faithful animal model recapitulates the combined human skin-and-bone phenotype. Inconsistent fibroblast signaling and absent genotype–phenotype correlation limit mechanistic prediction. | Research priorities: longitudinal natural-history registry; standardized phenotyping; lesional single-cell and spatial profiling; functional variant assays; tissue-specific models | (korman2016mutationinlemd3 pages 4-6, korman2016mutationinlemd3 pages 2-4, hellemans2004lossoffunctionmutationsin pages 4-5) |


*Table: A knowledge-base-ready synopsis of BOS identity, phenotype, genetics, mechanism, diagnosis, course, management, and major evidence gaps, with ontology suggestions and representative LEMD3 variants.*

## Evidence scope and currency

The strongest evidence comprises the 2004 gene-discovery study, subsequent familial sequencing studies, human cellular assays, and a 2020 two-patient bone-biopsy study. The 2023–2024 literature mainly updates the wider biology of high-bone-mass and BMP/TGF-β disorders rather than providing new BOS cohorts. A 2024 neuropsychological report is a single preprint and cannot establish neurodevelopmental manifestations as part of classic BOS. A small 2025 dermatology case series is included as post-2024 supporting evidence because it supplies unusually useful onset and histopathology data, but its estimates should not be generalized as population frequencies. (frost2020modelingbasedboneformation pages 1-7, tan2025clinicalandhistopathological pages 1-2)

---

## 1. Disease information

### Definition and identifiers

BOS is the syndromic coexistence of **connective-tissue nevi**—elastic, collagenous, or mixed—with **osteopoikilosis**, a developmental sclerosing bone dysplasia characterized by multiple small bone islands. Melorheostosis can occasionally coexist, but isolated sporadic melorheostosis is not synonymous with BOS. (mumm2007deactivatinggermlinemutations pages 1-2, hellemans2004lossoffunctionmutationsin pages 1-2)

* **MONDO:** MONDO:0008157.
* **OMIM/MIM:** 166700.
* **Causal disease-target association:** Open Targets identifies **LEMD3** (ENSG00000174106) as the single associated target, based on five evidence records and literature including PMID **15489854** and **17223882**. (OpenTargets Search: Buschke-Ollendorff syndrome-LEMD3)
* **Orphanet:** BOS is represented in Orphanet, but an exact ORPHA number was not independently recoverable from the retrieved primary literature; it should be verified directly against the current Orphanet nomenclature release before ingestion.
* **ICD-10/ICD-11:** No retrieved evidence established a dedicated BOS code. In practice it may be represented under broader congenital skin/connective-tissue or osteodysplasia categories; a broad code should not be treated as disease-specific.
* **MeSH:** No dedicated BOS descriptor was verified; “Osteopoikilosis” and broader connective-tissue-nevus terminology are commonly used for indexing.

**Synonyms:** Buschke–Ollendorff syndrome; Buschke-Ollendorf syndrome; dermato-osteopoikilosis; dermatofibrosis lenticularis disseminata with osteopoikilosis; osteopoikilosis with connective-tissue nevi. Juvenile elastoma and dermatofibrosis lenticularis disseminata describe cutaneous components rather than exact synonyms in every patient. (mumm2007deactivatinggermlinemutations pages 1-2, hellemans2004lossoffunctionmutationsin pages 1-2, steensel2008buschkeollendorfsyndromereport pages 1-2)

This report summarizes **aggregated disease-level resources and published patients/families**, not EHR-derived individual-level data.

> Primary-literature definition: the foundational study described BOS as an autosomal-dominant disorder combining osteopoikilosis with “disseminated connective-tissue nevi.” Publication: 17 October 2004; DOI: https://doi.org/10.1038/ng1453; PMID: 15489854. (hellemans2004lossoffunctionmutationsin pages 1-2)

---

## 2. Etiology

### Causal factors and genetic risk

The principal cause is a heterozygous **germline loss-of-function LEMD3 variant**, producing MAN1 haploinsufficiency. Reported classes include nonsense, frameshift, splice-disrupting, and larger deletion variants. Representative familial variants include c.1323C>A, p.Tyr441Ter; c.332_333insTC; and c.1863G>A, reported as p.Trp620Ter or p.Trp621Ter because of transcript/numbering differences. (mumm2007deactivatinggermlinemutations pages 1-2, steensel2008buschkeollendorfsyndromereport pages 1-2, korman2016mutationinlemd3 pages 4-6, korman2016mutationinlemd3 pages 2-4)

Family history is therefore the major risk factor. Each child of a heterozygous affected person has a theoretical **50% transmission probability**, but phenotype cannot be predicted reliably because penetrance of individual components and expressivity are variable. Relatives carrying the same variant may have BOS, isolated osteopoikilosis, skin lesions alone, or minimal/no recognized manifestations. (korman2016mutationinlemd3 pages 2-4, hellemans2004lossoffunctionmutationsin pages 1-2)

### Environmental, infectious, and lifestyle factors

No toxin, radiation exposure, infection, diet, smoking behavior, occupation, or other environmental exposure is established as a cause or modifier of classic BOS. Trauma may bring a skeletal lesion to clinical attention but is not demonstrated to cause the Mendelian disorder. No validated gene–environment interaction has been reported.

### Protective factors

No protective LEMD3 allele, modifier locus, lifestyle intervention, diet, or prophylactic exposure has been demonstrated. Population-database rarity of loss-of-function alleles is useful for pathogenicity assessment but is not evidence of a protective genotype.

---

## 3. Phenotypes

### Core manifestations

| Phenotype | Type and characteristics | Onset/course and frequency evidence | Suggested HPO |
|---|---|---|---|
| Connective-tissue nevi | Non-tender flesh-colored, yellowish, or red papules/nodules; may coalesce into cobblestone plaques. Histologically elastoma, collagenoma, or mixed lesions | Commonly congenital, infantile, or childhood; usually slowly enlarging and persistent. A 2025 small series reported 23% before age 1 and one onset at 47 years, but this is not a population estimate | Connective tissue nevus; collagenoma; abnormal elastic tissue |
| Osteopoikilosis | Multiple 1–5-mm round/ovoid, generally symmetric periarticular sclerotic foci, especially epiphyses/metaphyses, pelvis, carpus, and tarsus | Developmental and lifelong; often asymptomatic and incidentally detected | **HP:0005681** Osteopoikilosis |
| Melorheostosis | Asymmetric flowing cortical hyperostosis, classically “dripping candle wax” | Uncommon in BOS; may cause pain, deformity, or restricted motion. Sporadic melorheostosis is genetically distinct | **HP:0005781** Melorheostosis |
| Musculoskeletal pain/arthralgia | Subjective pain around involved bones or joints | Minority manifestation; osteopoikilosis literature estimates arthralgia/synovitis in approximately 15–20%, but this cannot be assumed to be BOS-specific | **HP:0002829** Arthralgia; bone pain |
| Contracture/deformity | Restricted motion, skin contracture, thumb or limb deformity in severe localized disease | Rare and variable; may progress sufficiently to require orthopedic correction | **HP:0001371** Joint contracture; limited joint mobility |
| Dermal fibrosis/morphea-like change | Dense collagen, sclerotic plaques, occasionally lichen-sclerosus-like change | Rare association; adult-onset generalized morphea has been reported but is not a defining phenotype | Scleroderma; abnormality of skin morphology |

The osteopoikilosis pattern and childhood skin lesions are documented in multiple human families. One infant developed a firm abdominal eruption at three months, while another had infantile lesions that became widespread and pruritic by age five. (mumm2007deactivatinggermlinemutations pages 1-2, korman2016mutationinlemd3 pages 1-2, tan2025clinicalandhistopathological pages 1-2)

### Histopathology and laboratory findings

Skin biopsies are heterogeneous: elastic fibers may be thickened, enlarged, and haphazard; collagenomas show hypocellular dense interlacing collagen; mixed lesions and interstitial mucin occur. Thus, a normal or non-classic elastic stain does not exclude BOS. Bone biopsy can show thickened cortex/trabeculae and compact lamellar sclerotic nodules without woven bone. Routine blood chemistry and bone-turnover markers are usually normal. (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3, frost2020modelingbasedboneformation pages 1-7, tan2025clinicalandhistopathological pages 1-2)

### Neurobehavioral phenotype

Intellectual disability, attention, language, coordination, and learning difficulties were described in a 2024 single-child preprint. This is hypothesis-generating only. Developmental delay is better established in **large 12q14 deletions involving additional genes** than in isolated heterozygous LEMD3 loss of function; neurodevelopmental findings should therefore trigger evaluation for a larger copy-number variant or another diagnosis.

### Quality of life

No BOS-specific EQ-5D, SF-36, PROMIS, or validated natural-history study was found. Most patients have little functional impairment, but visible nevi may create cosmetic/psychosocial burden, while pain, contracture, deformity, or restricted motion can affect mobility and daily activities. Severe impairment is case-based rather than quantified. (mumm2007deactivatinggermlinemutations pages 1-2, brodbeck2016thebuschke–ollendorffsyndrome pages 1-3)

---

## 4. Genetic and molecular information

### Gene and protein

* **Gene:** LEMD3, approved symbol; aliases **MAN1** and LEM domain-containing protein 3.
* **Genomic locus:** chromosome 12q14 region.
* **Ensembl:** ENSG00000174106. (OpenTargets Search: Buschke-Ollendorff syndrome-LEMD3)
* **Protein:** approximately 60-kDa integral inner-nuclear-membrane protein containing a LEM domain, two transmembrane segments, and a C-terminal SMAD-interacting/RNA-recognition-like region. (korman2016mutationinlemd3 pages 1-2, korman2016mutationinlemd3 pages 4-6)

### Variant interpretation

Truncating variants that remove the C-terminal SMAD-binding region are consistent with loss of function and haploinsufficiency. For example, c.1863G>A p.Trp620/621Ter is predicted to remove the second transmembrane helix, DNA-binding region, and R-SMAD-interacting domain. Functional experiments showed that disease-associated truncating variants failed to suppress TGF-β signaling. (korman2016mutationinlemd3 pages 4-6, hellemans2004lossoffunctionmutationsin pages 4-5)

Variant classification should nevertheless be performed under ACMG/AMP criteria using the correct transcript, segregation, population frequency, predicted nonsense-mediated decay, and ClinVar assertions. Exact gnomAD frequencies were not present in the retrieved literature and should be queried variant by variant; pathogenic truncating alleles are expected to be very rare or absent. The causal variants are **constitutional/germline**, not established somatic drivers. No obligatory somatic “second hit” was detected in sampled BOS skin fibroblasts. (hellemans2004lossoffunctionmutationsin pages 1-2)

### Genotype–phenotype relationship and modifiers

No reliable genotype–phenotype correlation exists. Identical variants can produce isolated osteopoikilosis, full BOS, or highly variable skin and skeletal involvement. No validated modifier gene, protective allele, anticipation, founder mutation, or epigenetic signature is known. Large 12q14 deletions may produce additional short-stature or neurodevelopmental phenotypes because neighboring genes are deleted; these are contiguous-gene disorders, not ordinary BOS.

---

## 5. Environmental information

Environmental toxins, pollution, radiation, occupational exposures, diet, exercise, alcohol, smoking, and infectious agents have no demonstrated etiologic role. BOS is neither contagious nor zoonotic. Environmental avoidance cannot prevent a constitutional LEMD3 variant. Symptom-sensitive activity modification may be appropriate for painful orthopedic disease, but this is tertiary management rather than primary prevention.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous germline loss-of-function variant in **LEMD3** **leads to** reduced functional MAN1 dosage at the inner nuclear membrane. (hellemans2004lossoffunctionmutationsin pages 1-2, hellemans2004lossoffunctionmutationsin pages 4-5)
2. Loss of the MAN1 C-terminal SMAD-interacting function **leads to** reduced binding/sequestration or regulation of receptor-activated SMAD1/2/3 and reduced cooperation with pathway-terminating machinery. (korman2016mutationinlemd3 pages 4-6, hellemans2004lossoffunctionmutationsin pages 4-5)
3. Reduced MAN1 antagonism **results in** increased or prolonged BMP and activin/TGF-β transcriptional signaling; disease-associated truncations fail to suppress TGF-β-responsive reporters. (steensel2008buschkeollendorfsyndromereport pages 1-2, hellemans2004lossoffunctionmutationsin pages 4-5)
4. **Bone branch:** dysregulated BMP/TGF-β signaling in osteogenic-lineage cells **is inferred to lead to** focal activation of bone-lining/osteoblast cells and modeling-based lamellar bone formation. (frost2020modelingbasedboneformation pages 1-7)
5. This focal modeling **results in** compact lamellar sclerotic nodules and radiographic osteopoikilosis; melorheostosis-like hyperostosis occurs less often. (frost2020modelingbasedboneformation pages 1-7)
6. **Skin branch:** dysregulated TGF-β/BMP signaling in dermal fibroblast/connective-tissue lineages **is inferred to lead to** altered collagen, elastic-fiber, and mucin deposition. Direct consistency across BOS fibroblast experiments is incomplete. (korman2016mutationinlemd3 pages 2-4, tan2025clinicalandhistopathological pages 1-2, korman2016mutationinlemd3 pages 4-6)
7. Extracellular-matrix accumulation **results in** collagenoma, elastoma, mixed connective-tissue nevi, and occasional fibrotic contracture. (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3, tan2025clinicalandhistopathological pages 1-2)

### Molecular and cellular detail

The strongest functional evidence is from human/cell-line experiments. The MAN1 C terminus binds the MH2 domains of SMAD1 and SMAD2. Overexpressed MAN1 reduced BMP4-induced **SMAD6, SMAD7, ID2, and ID3** expression in HEK293T cells and suppressed a TGF-β-responsive reporter in HepG2 cells; pathogenic truncations did not. An affected person’s fibroblasts showed haploinsufficiency and increased ID3 after TGF-β stimulation. However, other fibroblast studies did not consistently reproduce pathway changes, so tissue specificity remains unresolved. (korman2016mutationinlemd3 pages 4-6, hellemans2004lossoffunctionmutationsin pages 4-5)

The 2020 human histomorphometry study found normal overall remodeling but focal replacement of trabecular architecture by modeling-based compact lamellar bone, supporting bone-lining-cell activation rather than generalized high turnover. In two women, bone-turnover markers and lumbar BMD were normal, hip BMD was higher, and NaF-PET/CT showed irregular skeletal uptake. The tiny sample precludes prevalence or prognostic inference. DOI: https://doi.org/10.1016/j.bone.2020.115313, June 2020. (frost2020modelingbasedboneformation pages 1-7)

### Ontology suggestions

* **GO biological process:** GO:0030509 BMP signaling pathway; GO:0007179 TGF-β receptor signaling pathway; GO:0060395 SMAD protein signal transduction; GO:0001503 ossification; GO:0045778 positive regulation of ossification; GO:0030198 extracellular-matrix organization.
* **GO cellular component:** GO:0005637 nuclear envelope; inner nuclear membrane; nucleus.
* **Cell Ontology:** CL:0000057 fibroblast; CL:0000062 osteoblast; bone-lining cell; CL:0000137 osteocyte; mesenchymal stromal cell.

No BOS-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, multi-omic, or CRISPR-screen dataset was identified. These are major research gaps rather than negative biological findings.

---

## 7. Anatomical structures affected

**Primary organs:** skin and skeleton. Skin lesions favor trunk, abdomen, buttocks, thighs, and extremities and are often asymmetric. Skeletal lesions favor cancellous bone around joints—epiphyses/metaphyses of long bones, pelvis, carpal and tarsal bones. (mumm2007deactivatinggermlinemutations pages 1-2, tan2025clinicalandhistopathological pages 1-2)

**Tissue/cell level:** dermal connective tissue, fibroblasts, collagen and elastic-fiber matrix; trabecular/cortical bone, bone-lining cells, osteoblast lineage, and osteocytes. Bone marrow failure is not characteristic, distinguishing BOS from severe osteopetrosis. (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3, frost2020modelingbasedboneformation pages 1-7)

**Subcellular level:** MAN1 resides in the inner nuclear membrane/nuclear envelope, where its nucleoplasmic C terminus regulates SMAD signaling. (korman2016mutationinlemd3 pages 1-2, hellemans2004lossoffunctionmutationsin pages 4-5)

Suggested anatomy terms include **UBERON:0002097 skin of body**, dermis, bone tissue, appendicular skeleton, pelvis, carpal bone, and tarsal bone. Disease is commonly bilaterally/symmetrically distributed in bone but cutaneous disease can be markedly asymmetric; melorheostosis is usually segmental/asymmetric.

---

## 8. Temporal development

BOS is a chronic developmental disorder. Skin lesions most often arise congenitally, in infancy, or childhood, then remain stable or enlarge slowly; delayed adult cutaneous presentation is documented. Osteopoikilosis is lifelong and may not be found until an unrelated radiograph. There is no accepted staging system, end stage, relapsing-remitting pattern, or critical therapeutic window. (mumm2007deactivatinggermlinemutations pages 1-2, korman2016mutationinlemd3 pages 1-2, tan2025clinicalandhistopathological pages 1-2)

Spontaneous clearance is not a recognized general pattern. Treatment may improve symptoms or remove individual lesions but does not reverse the constitutional predisposition. Earlier recognition is valuable chiefly to avoid biopsy or oncologic workup of benign bone islands and to enable family counseling. (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3)

---

## 9. Inheritance and population

### Inheritance

Inheritance is **autosomal dominant**, with variable penetrance of skin and skeletal components and marked intrafamilial expressivity. Anticipation is not reported. Germline mosaicism is theoretically possible for any de novo variant but is not an established recurrent BOS mechanism. Consanguinity is not a risk factor for this dominant disorder. (korman2016mutationinlemd3 pages 2-4, mumm2007deactivatinggermlinemutations pages 1-2, hellemans2004lossoffunctionmutationsin pages 1-2)

### Epidemiology

The frequently cited occurrence is approximately **1 in 20,000** (about 5 per 100,000), but this is an imprecise estimate rather than a modern registry-derived BOS prevalence. BOS-specific incidence, sex ratio, age distribution, carrier frequency, ethnic enrichment, founder effects, and geographic variation remain unknown. Ascertainment is probably incomplete because osteopoikilosis is often asymptomatic and skin findings can be subtle or absent. (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3, frost2020modelingbasedboneformation pages 1-7, tan2025clinicalandhistopathological pages 1-2)

---

## 10. Diagnostics

### Practical diagnostic approach

1. **Clinical examination:** document connective-tissue papules, nodules, plaques, distribution, pain, contracture, and family history.
2. **Plain radiographs:** hands/wrists, pelvis, knees, ankles, or symptomatic sites usually show numerous small, homogeneous, symmetric periarticular bone islands. CT can define atypical lesions; routine PET/MRI is unnecessary in typical asymptomatic disease.
3. **Skin biopsy:** reserve for atypical lesions; use routine histology plus elastic-fiber stains. Collagenous, elastic, mixed, or mucin-rich findings are possible. (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3, tan2025clinicalandhistopathological pages 1-2)
4. **Genetic confirmation:** sequence **LEMD3** coding exons and splice boundaries; contemporary testing should add deletion/duplication analysis. Familial studies historically used blood-derived DNA PCR/Sanger sequencing. A negative coding test does not categorically exclude a convincing phenotype. (steensel2008buschkeollendorfsyndromereport pages 1-2, korman2016mutationinlemd3 pages 2-4, mumm2007deactivatinggermlinemutations pages 1-2)
5. **Broader testing:** use a sclerosing-bone-dysplasia panel or WES/WGS when phenotype is atypical or LEMD3 testing is negative. Use chromosomal microarray when short stature, developmental delay, congenital anomalies, or dysmorphism suggests a 12q14 deletion. Karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not routine.

There is no validated blood/urine biomarker, enzyme assay, electrophysiologic test, liquid biopsy, or omics diagnostic. Routine bone chemistry and turnover markers may be normal. (frost2020modelingbasedboneformation pages 1-7)

### Differential diagnosis

* **Isolated osteopoikilosis:** same skeletal pattern without connective-tissue nevi.
* **Osteoblastic metastases:** generally irregular/asymmetric, axial-predominant, and clinically contextual; unlike the uniform periarticular distribution of osteopoikilosis.
* **Osteopathia striata/osteopetrosis:** linear striations or generalized dense bone rather than discrete bone islands.
* **Melorheostosis:** flowing cortical hyperostosis; sporadic cases generally lack germline LEMD3 variants. (mumm2007deactivatinggermlinemutations pages 1-2)
* **Tuberous-sclerosis shagreen patch, familial/eruptive collagenoma, nevus anelasticus, papular elastorrhexis, and pseudoxanthoma elasticum:** distinguished by systemic findings, lesion morphology, histology, radiographs, and genetics.
* **Morphea/systemic sclerosis:** inflammatory/sclerotic evolution, autoantibodies, Raynaud phenomenon, sclerodactyly, or organ involvement support alternatives; BOS nevi are hamartomatous. Negative systemic-sclerosis serology and absence of sclerodactyly aided one reported differential. (korman2016mutationinlemd3 pages 1-2)

No formal society diagnostic criteria or population/newborn screening program exists. Cascade clinical and genetic evaluation is appropriate after identifying a familial pathogenic variant.

---

## 11. Outcome and prognosis

Typical BOS is benign and does not appear to shorten life expectancy. No disease-specific mortality, five-/ten-year survival statistic, or excess cancer risk is established. Most morbidity is cosmetic or orthopedic. Complications include pain, joint restriction, contracture, deformity, nerve or joint impingement when melorheostosis is present, and diagnostic harm from mistaking bone islands for metastases. (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3, frost2020modelingbasedboneformation pages 1-7)

No validated prognostic biomarker exists. Neither variant class nor lesion burden reliably predicts outcome. Melorheostosis, progressive contracture, and functional deformity indicate greater morbidity; isolated radiographic osteopoikilosis generally requires no intervention. Quality-of-life and disability outcomes have not been systematically quantified.

---

## 12. Treatment

### Standard management

There is no approved disease-modifying, gene-directed, RNA, cell, or targeted therapy for BOS.

* **Observation and reassurance:** preferred for asymptomatic skin and bone lesions; **NCIT suggestions:** Observation, Clinical Monitoring.
* **Pain management:** simple analgesics/NSAIDs when clinically appropriate; **NCIT:** Analgesic Therapy.
* **Physical/occupational therapy:** maintain range of motion and function in painful or contracture-prone disease; **NCIT:** Physical Therapy, Occupational Therapy.
* **Dermatologic treatment:** excision or selected laser/procedural treatment may be considered for painful, function-limiting, or cosmetically distressing lesions, but recurrence/scarring and sparse outcome evidence should be discussed.
* **Orthopedic treatment:** corrective osteotomy, excision/decompression, or contracture surgery only for major deformity, impingement, or functional loss. A reported thumb deformity improved after corrective osteotomy. **NCIT:** Surgical Procedure, Osteotomy. (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3)
* **Morphea-like inflammatory disease:** treat according to morphea severity rather than as routine BOS. One exceptional case received PUVA, calcitriol, hydroxychloroquine, mycophenolate, and topical agents with slow partial improvement; this is not evidence for treating ordinary BOS. (korman2016mutationinlemd3 pages 2-4)
* **Genetic counseling:** explain 50% transmission risk and unpredictable expressivity; **NCIT:** Genetic Counseling.

No BOS-specific response rate, comparative treatment study, pharmacogenomic guidance, or relevant interventional NCT trial was identified. Bisphosphonate reports relate mainly to symptomatic melorheostosis and do not establish efficacy for osteopoikilosis or connective-tissue nevi.

---

## 13. Prevention

**Primary prevention:** no lifestyle, vaccine, drug, or environmental measure prevents a germline LEMD3 disorder. Reproductive options after identifying a familial pathogenic variant include prenatal diagnosis and preimplantation genetic testing, following nondirective counseling.

**Secondary prevention:** no population or newborn screening is recommended. Targeted cascade testing and radiographic/dermatologic evaluation can identify relatives and prevent unnecessary oncologic investigations.

**Tertiary prevention:** monitor symptomatic patients for pain, reduced motion, contracture, deformity, or nerve/joint impingement; intervene with rehabilitation or orthopedic care before fixed disability. Immunization, antimicrobial prophylaxis, and environmental remediation have no BOS-specific role.

---

## 14. Other species and natural disease

No well-established naturally occurring BOS equivalent was identified in companion animals, livestock, or wildlife. Accordingly, no breed association, VBO term, veterinary prevalence, cross-species transmission, or zoonotic potential can be assigned. **LEMD3/MAN1 function is evolutionarily conserved**, but experimental perturbation in other species should not be mislabeled as spontaneous BOS.

---

## 15. Model organisms

No model faithfully reproduces the combined human skin-nevus/osteopoikilosis phenotype.

* **Mouse:** complete Lemd3 disruption causes severe developmental/vascular abnormalities and embryonic lethality, demonstrating essential MAN1 function but limiting its usefulness for adult BOS. Published work further indicates that a heterozygous gene-trap mouse does not reproduce human osteopoikilosis; species dosage sensitivity is therefore a major limitation.
* **Drosophila:** MAN1 loss produces tissue-specific developmental defects and enhanced BMP-related phenotypes. These models establish conserved pathway antagonism but cannot model human bone or dermal connective-tissue architecture.
* **Zebrafish/Xenopus:** MAN1 perturbation has been used to study BMP/TGF-β signaling and embryogenesis. Such developmental models are mechanistically informative but not validated BOS models.
* **Cellular systems:** HEK293T and HepG2 reporter assays and patient fibroblasts demonstrate SMAD binding and pathway repression/loss of repression. Inconsistent patient-fibroblast results and lack of the bone microenvironment limit prediction of clinical severity. (korman2016mutationinlemd3 pages 4-6, hellemans2004lossoffunctionmutationsin pages 4-5)
* **Human tissue model:** the two-patient 2020 bone-biopsy study is presently more disease-proximal than most animal work, implicating modeling-based lamellar bone formation and activated bone-lining cells. (frost2020modelingbasedboneformation pages 1-7)

Priority models include isogenic patient-derived iPSC osteoblast/fibroblast systems, tissue-specific heterozygous knock-in mice, and skin–bone organoid or spatial single-cell studies.

---

## Key publications and direct abstract-level statements

1. **Hellemans et al., Nature Genetics, 17 October 2004.** “Loss-of-function mutations in LEMD3 result in osteopoikilosis, Buschke-Ollendorff syndrome and melorheostosis.” DOI: https://doi.org/10.1038/ng1453; PMID: **15489854**. Functional evidence showed MAN1 interaction with BMP- and activin/TGF-β-activated SMADs and antagonism of both pathways. (hellemans2004lossoffunctionmutationsin pages 1-2, hellemans2004lossoffunctionmutationsin pages 4-5)
2. **Mumm et al., Journal of Bone and Mineral Research, February 2007.** The study’s central conclusion was that deactivating germline LEMD3 mutations cause osteopoikilosis and BOS “but not sporadic melorheostosis.” DOI: https://doi.org/10.1359/jbmr.061102; PMID: **17223882**. (mumm2007deactivatinggermlinemutations pages 1-2)
3. **Brodbeck et al., BMC Research Notes, June 2016.** Abstract conclusion: in atypical osteocutaneous presentations, the authors recommended LEMD3 screening and emphasized that correct diagnosis can spare “expensive investigations” and provide reassurance about the disease’s benign nature. DOI: https://doi.org/10.1186/s13104-016-2095-2. (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3)
4. **Frost et al., Bone, June 2020.** Human biopsies supported modeling-based conversion of trabecular to compact lamellar bone in sclerotic areas. DOI: https://doi.org/10.1016/j.bone.2020.115313. (frost2020modelingbasedboneformation pages 1-7)
5. **Tan et al., Acta Dermato-Venereologica, 8 April 2025.** This recent small series broadened the recognized histology to collagenoma, elastoma, mixed lesions, and mucin deposition and documented onset from infancy to late adulthood. DOI: https://doi.org/10.2340/actadv.v105.42531. (tan2025clinicalandhistopathological pages 1-2)

## Knowledge-base cautions

The often-quoted 1:20,000 figure is not a robust registry prevalence; feature percentages from small case series should not be interpreted as penetrance estimates. Classic BOS should not automatically include intellectual disability, generalized morphea, or sporadic melorheostosis. A pathogenic LEMD3 variant strongly supports diagnosis, but variable expression and occasional mutation-negative families mean that genotype must be interpreted with the osteocutaneous phenotype. The mechanistic link from enhanced SMAD signaling to tissue-selective lesions remains partly inferred, despite strong molecular evidence that MAN1 antagonizes BMP/TGF-β signaling. (korman2016mutationinlemd3 pages 2-4, hellemans2004lossoffunctionmutationsin pages 1-2, tan2025clinicalandhistopathological pages 1-2, korman2016mutationinlemd3 pages 4-6)

References

1. (mumm2007deactivatinggermlinemutations pages 1-2): Steven Mumm, Deborah Wenkert, Xiafang Zhang, William H McAlister, Richard J Mier, and Michael P Whyte. Deactivating germline mutations in <i>lemd3</i> cause osteopoikilosis and buschke-ollendorff syndrome, but not sporadic melorheostosis. Feb 2007. URL: https://doi.org/10.1359/jbmr.061102, doi:10.1359/jbmr.061102. This article has 112 citations and is from a highest quality peer-reviewed journal.

2. (hellemans2004lossoffunctionmutationsin pages 1-2): Jan Hellemans, Olena Preobrazhenska, Andy Willaert, Philippe Debeer, Peter C M Verdonk, Teresa Costa, Katrien Janssens, Bjorn Menten, Nadine Van Roy, Stefan J T Vermeulen, Ravi Savarirayan, Wim Van Hul, Filip Vanhoenacker, Danny Huylebroeck, Anne De Paepe, Jean-Marie Naeyaert, Jo Vandesompele, Frank Speleman, Kristin Verschueren, Paul J Coucke, and Geert R Mortier. Loss-of-function mutations in lemd3 result in osteopoikilosis, buschke-ollendorff syndrome and melorheostosis. Oct 2004. URL: https://doi.org/10.1038/ng1453, doi:10.1038/ng1453. This article has 585 citations and is from a highest quality peer-reviewed journal.

3. (frost2020modelingbasedboneformation pages 1-7): M. Frost, E.T. Rahbek, C. Ejersted, P.F. Høilund-Carlsen, A. Bygum, J.S. Thomsen, C.M. Andreasen, T.L. Andersen, and A.L. Frederiksen. Modeling-based bone formation transforms trabeculae to cortical bone in the sclerotic areas in buschke-ollendorff syndrome. a case study of two females with lemd3 variants. Jun 2020. URL: https://doi.org/10.1016/j.bone.2020.115313, doi:10.1016/j.bone.2020.115313. This article has 13 citations and is from a domain leading peer-reviewed journal.

4. (hellemans2004lossoffunctionmutationsin pages 4-5): Jan Hellemans, Olena Preobrazhenska, Andy Willaert, Philippe Debeer, Peter C M Verdonk, Teresa Costa, Katrien Janssens, Bjorn Menten, Nadine Van Roy, Stefan J T Vermeulen, Ravi Savarirayan, Wim Van Hul, Filip Vanhoenacker, Danny Huylebroeck, Anne De Paepe, Jean-Marie Naeyaert, Jo Vandesompele, Frank Speleman, Kristin Verschueren, Paul J Coucke, and Geert R Mortier. Loss-of-function mutations in lemd3 result in osteopoikilosis, buschke-ollendorff syndrome and melorheostosis. Oct 2004. URL: https://doi.org/10.1038/ng1453, doi:10.1038/ng1453. This article has 585 citations and is from a highest quality peer-reviewed journal.

5. (korman2016mutationinlemd3 pages 1-2): Benjamin Korman, Jun Wei, Anne Laumann, Polly Ferguson, and John Varga. Mutation in lemd3 (man1) associated with osteopoikilosis and late-onset generalized morphea: a new buschke-ollendorf syndrome variant. Case Reports in Dermatological Medicine, 2016:1-9, Jun 2016. URL: https://doi.org/10.1155/2016/2483041, doi:10.1155/2016/2483041. This article has 13 citations.

6. (brodbeck2016thebuschke–ollendorffsyndrome pages 1-3): Michael Brodbeck, Q. Yousif, P. A. Diener, M. Zweier, and J. Gruenert. The buschke–ollendorff syndrome: a case report of simultaneous osteo-cutaneous malformations in the hand. BMC Research Notes, Jun 2016. URL: https://doi.org/10.1186/s13104-016-2095-2, doi:10.1186/s13104-016-2095-2. This article has 11 citations and is from a peer-reviewed journal.

7. (tan2025clinicalandhistopathological pages 1-2): Yidong Tan, Jinxiang Yang, Xuanyi Chen, Zhirong Yao, and Jianying Liang. Clinical and histopathological characteristics of buschke–ollendorff syndrome: a case series. Acta Dermato-Venereologica, 105:adv42531, Apr 2025. URL: https://doi.org/10.2340/actadv.v105.42531, doi:10.2340/actadv.v105.42531. This article has 1 citations and is from a domain leading peer-reviewed journal.

8. (OpenTargets Search: Buschke-Ollendorff syndrome-LEMD3): Open Targets Query (Buschke-Ollendorff syndrome-LEMD3, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

9. (korman2016mutationinlemd3 pages 2-4): Benjamin Korman, Jun Wei, Anne Laumann, Polly Ferguson, and John Varga. Mutation in lemd3 (man1) associated with osteopoikilosis and late-onset generalized morphea: a new buschke-ollendorf syndrome variant. Case Reports in Dermatological Medicine, 2016:1-9, Jun 2016. URL: https://doi.org/10.1155/2016/2483041, doi:10.1155/2016/2483041. This article has 13 citations.

10. (steensel2008buschkeollendorfsyndromereport pages 1-2): Michel van Geel, Valerie L.R.M. Verstraeten, G.P.H. Lucker, and Maurice A.M. van Steensel. Buschke-ollendorf syndrome: report of a case and a brief molecular overview. The Open Dermatology Journal, 02(1):05-08, Jan 2008. URL: https://doi.org/10.2174/1874372200802010005, doi:10.2174/1874372200802010005. This article has 0 citations.

11. (korman2016mutationinlemd3 pages 4-6): Benjamin Korman, Jun Wei, Anne Laumann, Polly Ferguson, and John Varga. Mutation in lemd3 (man1) associated with osteopoikilosis and late-onset generalized morphea: a new buschke-ollendorf syndrome variant. Case Reports in Dermatological Medicine, 2016:1-9, Jun 2016. URL: https://doi.org/10.1155/2016/2483041, doi:10.1155/2016/2483041. This article has 13 citations.

## Artifacts

- [Edison artifact artifact-00](Buschke-Ollendorff_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008157` (3 mentions) - the report calls it "if available"; MONDO calls it **Buschke-Ollendorff syndrome**