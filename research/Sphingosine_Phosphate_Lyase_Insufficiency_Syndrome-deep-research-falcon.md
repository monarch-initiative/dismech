---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T19:02:10.165899'
end_time: '2026-09-05T19:10:14.768532'
duration_seconds: 484.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Sphingosine Phosphate Lyase Insufficiency Syndrome
  mondo_id: MONDO:0033203
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
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 24
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0033203
    reported_labels:
    - if available
    ontology_label: nephrotic syndrome 14
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Sphingosine_Phosphate_Lyase_Insufficiency_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sphingosine Phosphate Lyase Insufficiency Syndrome
- **MONDO ID:** MONDO:0033203 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Sphingosine Phosphate Lyase Insufficiency Syndrome** covering all of the
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
- **Disease Name:** Sphingosine Phosphate Lyase Insufficiency Syndrome
- **MONDO ID:** MONDO:0033203 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Sphingosine Phosphate Lyase Insufficiency Syndrome** covering all of the
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


# Sphingosine-1-phosphate lyase insufficiency syndrome (SPLIS): comprehensive disease-characteristics report

## Executive summary

Sphingosine-1-phosphate lyase insufficiency syndrome (SPLIS) is an ultra-rare, autosomal-recessive inborn error of sphingolipid metabolism caused by biallelic loss-of-function variants in **SGPL1**. Its core manifestations are early steroid-resistant nephrotic syndrome (SRNS), primary adrenal insufficiency, immune dysfunction, neurologic disease, and ichthyosis, but expressivity ranges from lethal prenatal disease to isolated childhood neuropathy or adrenal insufficiency. The strongest natural-history evidence is a September 2024 retrospective cohort of 76 molecularly confirmed patients: kidney involvement occurred in 78%, adrenal insufficiency in 63%, end-stage kidney disease (ESKD) in 35%, hypothyroidism in 33%, and lymphopenia in 30%; overall survival at last report was 50%. Early nephropathy, prenatal disease, and absence of transplantation predicted poor outcome, whereas homozygous p.Arg222Gln and kidney transplantation were associated with longer survival. These are observational associations, not randomized treatment effects. (keller2024factorsinfluencingsurvival pages 1-2, keller2024naturalhistoryof pages 5-8, keller2024factorsinfluencingsurvival pages 12-14)

| Domain | Best current finding/statistic | Evidence type | Key source/date/DOI |
|---|---|---|---|
| Definition and cause | SPLIS, also called nephrotic syndrome type 14 (NPHS14), is an ultra-rare autosomal-recessive sphingolipid-metabolism disorder caused by biallelic inactivating **SGPL1** variants. SGPL1 encodes the pyridoxal-5′-phosphate-dependent sphingosine-1-phosphate lyase. | Human genetic cohorts; biochemical studies | Lovric et al., March 2017, DOI: [10.1172/JCI89626](https://doi.org/10.1172/JCI89626); Sedillo et al., published online October 30, 2023, DOI: [10.1016/j.gimo.2023.100840](https://doi.org/10.1016/j.gimo.2023.100840) (sedillo2024prevalenceestimateof pages 1-3, lovric2017mutationsinsphingosine1phosphate pages 1-2) |
| Modeled prevalence | Estimated worldwide prevalence: **0.015 per 100,000** (95% CI 0.010–0.021), corresponding to approximately **11,707 affected people worldwide**. This is a population-genetic model, not observed case prevalence. | Population-genetic modeling using curated variants and gnomAD v2.1.1 | Sedillo et al., Genetics in Medicine Open, 2024; online October 30, 2023; DOI: [10.1016/j.gimo.2023.100840](https://doi.org/10.1016/j.gimo.2023.100840) (sedillo2024prevalenceestimateof pages 1-3, sedillo2024prevalenceestimateofa pages 1-3) |
| Major phenotype frequencies | In the 76-patient cohort: **kidney involvement 78%**, **primary adrenal insufficiency 63%**, **ESKD 35%**, **hypothyroidism 33%**, and **lymphopenia 30%**. Presentation ranged from prenatal disease to age 15 years; 54% presented in the first year. | Worldwide retrospective cross-sectional natural-history cohort | Keller et al., September 2024, DOI: [10.1186/s13023-024-03311-w](https://doi.org/10.1186/s13023-024-03311-w) (keller2024factorsinfluencingsurvival pages 1-2, keller2024naturalhistoryof pages 5-8) |
| Survival and early-onset risk | Overall survival at last report was **50%**. Among non-transplanted patients with nephropathy, diagnosis before age one identified a high-risk group: fewer than 30% were alive two years after diagnosis and 17% were alive at last report; mean age at death among deceased cohort members was 7.5 months. Prenatal presentations were also associated with early mortality. | Human natural-history cohort | Keller et al., September 2024, DOI: [10.1186/s13023-024-03311-w](https://doi.org/10.1186/s13023-024-03311-w) (keller2024factorsinfluencingsurvival pages 1-2, keller2024naturalhistoryof pages 5-8, keller2024factorsinfluencingsurvival pages 12-14) |
| Genotype and prognosis | Homozygous **p.Arg222Gln (R222Q)** was associated with better survival: reported survival was approximately **85%**, and median age at last report among non-transplanted patients was 6.8 years versus 1.9 years for other genotypes. This association is prognostic, not proof that R222Q alone determines outcome. | Human genotype–phenotype association | Keller et al., 2024, DOI: [10.1186/s13023-024-03311-w](https://doi.org/10.1186/s13023-024-03311-w) (keller2024naturalhistoryof pages 5-8, keller2024naturalhistoryof pages 14-18, keller2024naturalhistoryof pages 18-25) |
| Kidney transplantation | Kidney transplantation significantly extended survival relative to dialysis or palliative care. Median age at last report was 8 years after transplantation, 4.4 years with dialysis, and 1.3 years with palliative care; dialysis did not show a significant survival benefit over palliative care in the reported analysis. | Retrospective treatment-outcome comparison; nonrandomized | Keller et al., September 2024, DOI: [10.1186/s13023-024-03311-w](https://doi.org/10.1186/s13023-024-03311-w) (keller2024naturalhistoryof pages 14-18, keller2024factorsinfluencingsurvival pages 12-14, keller2024naturalhistoryof pages 18-25) |
| Core mechanism | Loss of ER-localized S1P-lyase activity blocks irreversible cleavage of S1P into hexadecenal and ethanolamine phosphate, disturbing sphingolipid homeostasis. Patient samples show increased S1P/sphingosine; fibroblasts can retain less than 10% of normal activity. Downstream mechanisms include abnormal S1P-receptor signaling, impaired mesangial migration, podocyte injury, immune-cell trafficking defects, and altered steroidogenesis; several organ-specific links remain partly inferred. | Human biochemical, cellular, mouse, yeast, and Drosophila evidence | Janecke et al., April 2017, DOI: [10.1002/humu.23192](https://doi.org/10.1002/humu.23192); Lovric et al., March 2017, DOI: [10.1172/JCI89626](https://doi.org/10.1172/JCI89626) (lovric2017mutationsinsphingosine1phosphate pages 10-11, janecke2017deficiencyofthe pages 11-15, choi2019sphingosinephosphatelyase pages 5-6, choi2019sphingosinephosphatelyase pages 4-5) |
| Diagnostic approach | Molecular confirmation requires **biallelic pathogenic or likely pathogenic SGPL1 variants**, typically detected by exome/genome sequencing or an SGPL1-containing nephrotic-syndrome/adrenal-insufficiency panel. Supporting assessments include proteinuria, serum albumin/lipids, kidney function and biopsy, cortisol/ACTH and mineralocorticoid testing, lymphocyte subsets, neurologic evaluation/MRI, and sphingolipid or enzyme assays where available. | Human cohort practice; observational biomarker development | Keller et al., 2024, DOI: [10.1186/s13023-024-03311-w](https://doi.org/10.1186/s13023-024-03311-w); NCT06669949 (keller2024naturalhistoryof pages 5-8, NCT06669949 chunk 1, NCT06669949 chunk 2) |
| Observational research | Two recruiting UCSF records were identified: **NCT04885179**, an international registry with estimated enrollment of 120, and **NCT06669949**, a three-year natural-history study with estimated enrollment of 28. They collect clinical, imaging, pathological and biospecimen data; neither assigns an investigational treatment. | Prospective observational studies/registries | [NCT04885179](https://clinicaltrials.gov/study/NCT04885179), started April 22, 2025; [NCT06669949](https://clinicaltrials.gov/study/NCT06669949), started April 22, 2025 (NCT06669949 chunk 1, NCT04885179 chunk 1, NCT06669949 chunk 3, NCT06669949 chunk 2) |


*Table: Compact summary of the strongest current evidence on SPLIS genetics, epidemiology, manifestations, prognosis, mechanism, diagnosis, transplantation, and ongoing observational research. Modeled estimates and nonrandomized clinical associations are explicitly distinguished from directly observed outcomes.*

## 1. Disease information

### Definition and identifiers

SPLIS is a recessive metabolic disorder in which deficient sphingosine-1-phosphate lyase prevents the terminal, irreversible degradation of sphingosine-1-phosphate (S1P). It is multisystemic rather than solely a nephrotic syndrome. (keller2024factorsinfluencingsurvival pages 1-2, janecke2017deficiencyofthe pages 11-15)

* **MONDO:** MONDO:0033203, represented in Open Targets as **nephrotic syndrome 14**.
* **OMIM phenotype:** **617575**, nephrotic syndrome, type 14.
* **Causal gene:** **SGPL1**, OMIM **603729**; HGNC **10817**; Ensembl **ENSG00000166224**.
* **Common names:** sphingosine-1-phosphate lyase insufficiency syndrome; sphingosine phosphate lyase insufficiency syndrome; SGPL1 deficiency; S1P-lyase deficiency; nephrotic syndrome 14/NPHS14; steroid-resistant nephrotic syndrome type 14; RENI syndrome; familial SRNS with adrenal insufficiency. (OpenTargets Search: Sphingosine phosphate lyase insufficiency syndrome-SGPL1, keller2024factorsinfluencingsurvival pages 1-2, sedillo2024prevalenceestimateof pages 1-3)
* **ICD/MeSH:** no uniquely specific ICD-10, ICD-11, or MeSH code was established in the retrieved evidence. Component manifestations are coded separately. A knowledge base should not assign an unverified disease-specific ICD code.

The available evidence is predominantly **aggregated disease-level information** assembled from published cases, clinician questionnaires, medical records, and treating-provider reports—not population-scale EHR surveillance. Individual case reports remain important because fewer than 100 clinically recognized patients had been reported by 2024. (sedillo2024prevalenceestimateofa pages 3-4, keller2024factorsinfluencingsurvival pages 2-4)

### Foundational literature

The disease was delineated in three independent 2017 reports linking recessive SGPL1 variants to nephrosis, adrenal disease, and neurologic/immune phenotypes. PubMed records cited by Open Targets include **PMID 28181337, PMID 28165339, and PMID 28165343**. The principal mechanistic paper is Lovric et al., *Journal of Clinical Investigation*, March 2017, DOI [10.1172/JCI89626](https://doi.org/10.1172/JCI89626); Janecke et al., *Human Mutation*, April 2017, DOI [10.1002/humu.23192](https://doi.org/10.1002/humu.23192). (OpenTargets Search: Sphingosine phosphate lyase insufficiency syndrome-SGPL1, janecke2017deficiencyofthe pages 11-15, lovric2017mutationsinsphingosine1phosphate pages 1-2)

A representative abstract statement from the 2024 natural-history study is: **“SPLIS is caused by inactivating mutations in SGPL1, encoding the pyridoxal 5′-phosphate-dependent enzyme sphingosine-1-phosphate lyase, which catalyzes the final step of sphingolipid metabolism.”** (keller2024factorsinfluencingsurvival pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Cause

The primary cause is **germline biallelic inactivation of SGPL1**. No infectious, toxic, occupational, radiation, or lifestyle cause is known. S1P lyase is an endoplasmic-reticulum integral membrane enzyme requiring pyridoxal-5′-phosphate (PLP; active vitamin B6) and irreversibly cleaves S1P into hexadecenal and ethanolamine phosphate. (janecke2017deficiencyofthe pages 11-15, choi2019sphingosinephosphatelyase pages 4-5)

### Risk factors

* **Genetic:** two pathogenic/likely pathogenic SGPL1 alleles; consanguinity and an affected sibling increase prior probability. In the 76-person cohort, 61% had reported consanguinity and 56% had a family history. (keller2024naturalhistoryof pages 5-8)
* **Variant-dependent severity:** residual enzyme activity plausibly modifies severity. Homozygous p.Arg222Gln was associated with better survival, whereas no homozygous p.Arg222Trp or p.Ser346Ile patient in that cohort survived. These associations require validation and should not be treated as deterministic. (keller2024naturalhistoryof pages 5-8, keller2024naturalhistoryof pages 18-25)
* **Non-genetic:** no reproducible environmental risk factor has been demonstrated. Marked intrafamilial variability suggests unidentified genetic, environmental, developmental, or stochastic modifiers. (sedillo2024prevalenceestimateof pages 1-3, sedillo2024prevalenceestimateofa pages 1-3)

### Protective factors

No inherited protective allele is established. Kidney transplantation and perhaps residual SGPL1 activity are associated with improved survival after disease develops, but are not primary prevention. Pyridoxine responsiveness may be genotype-dependent, particularly for PLP-binding-domain missense variants, but human evidence remains anecdotal or ex vivo. (keller2024naturalhistoryof pages 14-18, keller2024factorsinfluencingsurvival pages 12-14)

## 3. Phenotypes

The following frequencies derive from the best available 76-patient retrospective cohort and may be biased toward severe recognized disease. (keller2024naturalhistoryof pages 5-8)

* **Renal:** proteinuria, congenital/infantile nephrotic syndrome, usually steroid-resistant, FSGS or diffuse mesangial sclerosis, progressive CKD/ESKD. Kidney involvement: **78%**; ESKD: **35%**. Progression from proteinuria to ESKD ranged from under one month to five years. Suggested HPO: **HP:0000100 Nephrotic syndrome**, **HP:0000097 Focal segmental glomerulosclerosis**, **HP:0000093 Proteinuria**, **HP:0003774 End-stage renal disease**. (keller2024factorsinfluencingsurvival pages 1-2, yang2023steroidresistantnephroticsyndrome pages 6-7, choi2019sphingosinephosphatelyase pages 4-5)
* **Endocrine:** primary adrenal insufficiency, sometimes isolated glucocorticoid deficiency and sometimes combined mineralocorticoid deficiency; congenital adrenal calcification/hemorrhage; hypothyroidism; male hypogonadism/gonadal dysgenesis, cryptorchidism or micropenis. Adrenal insufficiency affected **63%** in the 76-person cohort. A 2022 synthesis found glucocorticoid insufficiency in **64% of 50 reported patients**, with approximately one-third of those also having mineralocorticoid deficiency; mild primary hypothyroidism affected about one-third. Suggested HPO: **HP:0000846 Adrenal insufficiency**, **HP:0001943 Hypoglycemia**, **HP:0000821 Hypothyroidism**, **HP:0000028 Cryptorchidism**, **HP:0000054 Micropenis**. (keller2024factorsinfluencingsurvival pages 1-2, keller2024naturalhistoryof pages 5-8)
* **Immune/hematologic:** lymphopenia, reduced CD4/CD8 T and B cells, poor stimulation responses, recurrent bacterial—often gastrointestinal—infections, and sepsis. Lymphopenia occurred in **30%** of the 76-person cohort; earlier literature suggested severe immune dysfunction in approximately half of reported cases, likely reflecting ascertainment differences. Suggested HPO: **HP:0001888 Lymphopenia**, **HP:0002719 Recurrent infections**, **HP:0002721 Immunodeficiency**. (choi2019sphingosinephosphatelyase pages 5-6, keller2024naturalhistoryof pages 5-8, choi2019sphingosinephosphatelyase pages 4-5)
* **Neurologic/developmental:** peripheral axonal neuropathy, lower-limb weakness, seizures, developmental delay, microcephaly, deafness, strabismus, corpus-callosum or basal-ganglia abnormalities. Severity ranges from absent to progressive neurologic disease or isolated late-childhood neuropathy. Suggested HPO: **HP:0009830 Peripheral neuropathy**, **HP:0001250 Seizure**, **HP:0001263 Global developmental delay**, **HP:0000252 Microcephaly**, **HP:0000365 Hearing impairment**, **HP:0000486 Strabismus**. (keller2024factorsinfluencingsurvival pages 1-2, sedillo2024prevalenceestimateofa pages 3-4, yang2023steroidresistantnephroticsyndrome pages 6-7)
* **Skin:** ichthyosis, acanthosis, and skin-barrier abnormalities. Suggested HPO: **HP:0008064 Ichthyosis** and **HP:0000956 Acanthosis nigricans**. (keller2024factorsinfluencingsurvival pages 1-2, keller2024naturalhistoryof pages 1-5)
* **Prenatal/general:** hydrops fetalis, fetal loss, oligohydramnios or polyhydramnios, edema, increased nuchal translucency, fetal-growth abnormalities, failure to thrive, hypercholesterolemia, and skeletal/thoracic abnormalities. Prenatal findings occurred in **22%** of the cohort and identified a very high-risk group. Suggested HPO: **HP:0001789 Hydrops fetalis**, **HP:0001508 Failure to thrive**, **HP:0003124 Hypercholesterolemia**. (keller2024naturalhistoryof pages 5-8, keller2024factorsinfluencingsurvival pages 12-14)

No validated SPLIS-specific EQ-5D, SF-36, PROMIS, or other quality-of-life dataset was found. Nevertheless, dialysis/transplantation, hormone replacement, recurrent infection, weakness, sensory loss, developmental disability, and skin disease impose major functional burdens. Current prospective studies include formal quality-of-life and neurodevelopmental assessments. (NCT04885179 chunk 1, NCT06669949 chunk 2)

## 4. Genetic and molecular information

**SGPL1** is the only established causal gene. Disease alleles include missense, nonsense, frameshift, in-frame deletion, canonical and noncanonical splice variants. More than two dozen pathogenic alleles had been curated by 2024; the 76-patient cohort contained 45 genotypes. Recurrent variants included **p.Arg222Gln, p.Tyr416Cys, p.Arg340Trp, p.Ser346Ile, and p.Arg222Trp**, collectively accounting for 75% of that cohort. p.Arg222Gln was homozygous in about one-quarter of earlier reported cases and in 13/76 (17%) of the natural-history cohort. (sedillo2024prevalenceestimateofa pages 3-4, keller2024naturalhistoryof pages 5-8, keller2024naturalhistoryof pages 14-18)

All established disease variants are **germline**. Studied parents were generally healthy heterozygotes; no confirmed de novo mechanism was known. Functional consequences include absent/reduced protein, reduced enzyme activity, abnormal intracellular localization, and failure to complement SGPL1-deficient yeast or Drosophila. Patient fibroblasts can have less than 10% of normal lyase activity. (sedillo2024prevalenceestimateof pages 1-3, choi2019sphingosinephosphatelyase pages 5-6, lovric2017mutationsinsphingosine1phosphate pages 1-2)

Variant-level ACMG classification and gnomAD allele frequency must be retrieved from the current ClinVar/gnomAD record for each HGVS allele; no single population frequency applies to “SPLIS.” Structural chromosomal abnormalities, somatic variants, repeat expansions, mitochondrial variants, epigenetic disease signatures, and validated modifier genes are not established. Intrafamilial variability indicates that modifiers probably exist, but none can currently be annotated as causal. (sedillo2024prevalenceestimateof pages 1-3)

## 5. Environmental information

No toxin, radiation, pollution, smoking, alcohol, diet, occupational exposure, or infectious agent is known to cause SPLIS. Infection is an important **complication** of immune dysfunction rather than the initiating etiology. Adequate vitamin B6 status could theoretically affect residual function of this PLP-dependent enzyme, but this is not evidence that dietary deficiency causes SPLIS. No zoonotic or transmissible component exists. (keller2024naturalhistoryof pages 14-18, lovric2017mutationsinsphingosine1phosphate pages 11-14)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic SGPL1 loss-of-function variants lead to** deficient or mislocalized ER-resident S1P-lyase protein and reduced PLP-dependent catalytic activity. (choi2019sphingosinephosphatelyase pages 5-6, choi2019sphingosinephosphatelyase pages 4-5)
2. **Reduced S1P-lyase activity leads to** failure of irreversible S1P cleavage into hexadecenal and ethanolamine phosphate. (janecke2017deficiencyofthe pages 11-15)
3. **Blocked terminal sphingolipid degradation leads to** accumulation and redistribution of S1P, sphingosine, ceramides, and other upstream sphingoid intermediates; loss of downstream products may additionally impair autophagic flux, although that branch is less directly established in SPLIS patients. (keller2024factorsinfluencingsurvival pages 1-2, lovric2017mutationsinsphingosine1phosphate pages 10-11, janecke2017deficiencyofthe pages 11-15)
4. **Abnormal lipid composition and S1P gradients lead to** receptor-dependent and intracellular signaling disturbance, including altered S1PR1/S1PR3 signaling, reduced RAC1/CDC42 activity, abnormal migration, immune-cell egress, inflammatory/fibrogenic signaling, calcium handling, mitochondrial stress, and membrane/vesicular dysfunction. Several links are inferred from cellular or animal models. (lovric2017mutationsinsphingosine1phosphate pages 10-11, lovric2017mutationsinsphingosine1phosphate pages 11-14, choi2019sphingosinephosphatelyase pages 4-5)
5. **In glomerular podocytes and mesangial cells, these disturbances lead to** foot-process effacement, defective mesangial migration/vascular maturation, filtration-barrier failure, proteinuria, SRNS/FSGS, and ESKD. (lovric2017mutationsinsphingosine1phosphate pages 10-11, choi2019sphingosinephosphatelyase pages 5-6)
6. **Branch A—adrenal cortex:** altered lipid homeostasis and developmental/steroidogenic organization **lead to** deficient steroidogenic-enzyme expression and cortical zonation in mice; this plausibly results in human glucocorticoid/mineralocorticoid failure and adrenal calcification, but the complete human causal chain is not proven. (choi2019sphingosinephosphatelyase pages 6-8)
7. **Branch B—immune system:** loss of tissue-to-blood S1P gradients **leads to** impaired thymic lymphocyte egress and altered leukocyte migration, resulting in lymphopenia, functional immunodeficiency, recurrent infection, and sepsis. (lovric2017mutationsinsphingosine1phosphate pages 11-14, choi2019sphingosinephosphatelyase pages 4-5)
8. **Branch C—nervous system and muscle:** sphingolipid/ceramide accumulation and mitochondrial oxidative stress are inferred to **lead to** axonal, neuromuscular, and CNS dysfunction; direct patient-tissue proof remains limited. (sedillo2024prevalenceestimateofa pages 3-4, choi2019sphingosinephosphatelyase pages 5-6)
9. **Multiorgan injury leads to** growth failure, endocrine crises, dialysis dependence, disability, and premature death. (keller2024factorsinfluencingsurvival pages 1-2, keller2024factorsinfluencingsurvival pages 12-14)

### Molecular profiling and ontology suggestions

Human blood and fibroblasts show increased S1P and sphingosine. Some blood ceramides, dihydroceramides, sphingomyelins, and monohexosylceramides were decreased, showing that SPLIS is not simply uniform lipid “storage.” Drosophila nephrocytes accumulated C16 sphingosine, C14 sphingadiene, and C16 ceramide. Plasma S1P and absolute lymphocyte count are being developed as biomarkers. No validated disease-wide transcriptomic, proteomic, single-cell, spatial-transcriptomic, or integrated multi-omic signature was identified. (lovric2017mutationsinsphingosine1phosphate pages 10-11, janecke2017deficiencyofthe pages 11-15, NCT06669949 chunk 1)

Suggested GO terms include **sphingolipid catabolic process**, **sphingosine-1-phosphate metabolic process**, **lymphocyte migration/egress**, **regulation of cell migration**, **small-GTPase-mediated signaling**, **angiogenesis**, **glomerular filtration**, **steroid biosynthetic process**, **mitochondrial organization**, and **response to oxidative stress**. Relevant cellular components include **endoplasmic-reticulum membrane** and plasma-membrane lipid rafts. Suggested CL concepts include podocyte, glomerular mesangial cell, adrenal cortical cell, T lymphocyte, B lymphocyte, dendritic cell, peripheral neuron, fibroblast, and epithelial cell.

## 7. Anatomical structures affected

Primary organs are the **kidney/glomerulus**, **adrenal cortex**, immune/lymphoid tissues, peripheral and central nervous systems, and skin. Secondary involvement can include thyroid, gonads, retina, heart, lung, skeleton, gastrointestinal tract, and hematopoietic system. (keller2024factorsinfluencingsurvival pages 1-2, choi2019sphingosinephosphatelyase pages 5-6)

At tissue/cell level, strongest evidence implicates glomerular podocytes and mesangial cells, adrenal cortical zones, lymphocytes and thymic dendritic cells, peripheral neurons, and keratinocyte/skin-barrier compartments. Mouse renal expression is strong in podocytes and mesangial cells but limited in glomerular endothelium. No consistent lateralization is reported. Suggested UBERON concepts include kidney, renal glomerulus, adrenal gland/cortex, thymus, peripheral nerve, brain/basal ganglia, skin, thyroid gland, and testis. (choi2019sphingosinephosphatelyase pages 5-6, choi2019sphingosinephosphatelyase pages 6-8)

## 8. Temporal development

Onset ranges from prenatal disease to approximately 15 years; **54%** of the 76 patients presented in the first year. Prenatal hydrops, fetal demise, adrenal calcification, and early infantile nephropathy constitute the most severe developmental end. Later presentations may be isolated adrenal insufficiency, renal disease, or peripheral neuropathy. (sedillo2024prevalenceestimateofa pages 3-4, keller2024naturalhistoryof pages 5-8)

The renal course is chronic and generally progressive. Among later-diagnosed patients in one analysis, all six progressed to ESKD within 24–60 months; infantile cases could progress in under six months or over 11–60 months. Remission of the genetic disease is not established. Kidney transplantation replaces renal function but does not constitute proven systemic cure. The first year of life is therefore a critical period for diagnosis, adrenal-crisis prevention, infection surveillance, and transplant planning. (keller2024factorsinfluencingsurvival pages 12-14)

## 9. Inheritance and population

Inheritance is **autosomal recessive**, with a 25% recurrence risk for each pregnancy when both parents are confirmed carriers. Penetrance among individuals with two severe alleles appears high, but organ-specific penetrance and age at onset are variable. Expressivity is markedly variable, including within families. Anticipation is not described; germline mosaicism has not been established. (sedillo2024prevalenceestimateof pages 1-3, sedillo2024prevalenceestimateofa pages 1-3)

A 2024 population-genetic study estimated prevalence at **0.015 per 100,000** (95% CI 0.010–0.021), equivalent to about **11,707 people worldwide**. This is a modeled genotype prevalence, not a count of diagnosed living patients, and greatly exceeds the fewer than 100 recognized clinical cases. Estimates were higher in some East Asian, Finnish, Turkish, and Iranian populations; Turkish/Iranian estimates were approximately 0.046–0.078 per 100,000. (sedillo2024prevalenceestimateofa pages 3-4, sedillo2024prevalenceestimateofa pages 1-3)

The 76-person cohort was geographically and ethnically diverse. No reliable incidence, sex ratio, age-standardized prevalence, carrier frequency, or universally accepted founder-effect estimate is available. Consanguinity was common but is not required. (keller2024naturalhistoryof pages 5-8)

## 10. Diagnostics

### Recommended approach

1. Suspect SPLIS in congenital/infantile SRNS, especially with adrenal insufficiency, adrenal calcification, ichthyosis, lymphopenia/infections, neuropathy, genital anomalies, or an affected sibling.
2. Measure urine protein/creatinine, serum albumin, creatinine/eGFR, electrolytes and lipids; assess morning cortisol, ACTH, renin, aldosterone, glucose, thyroid function, and gonadal hormones as age-appropriate.
3. Perform CBC with differential, lymphocyte subsets, immunoglobulins, and functional immune testing when indicated.
4. Evaluate hearing, vision, development and peripheral nerves; obtain brain MRI when neurologic signs occur. Basal-ganglia abnormalities have been reported.
5. Confirm with sequencing demonstrating **biallelic pathogenic/likely pathogenic SGPL1 variants**, preferably through a congenital/SRNS or adrenal-insufficiency panel, WES, or WGS. Include copy-number and splice analysis when routine sequencing is nondiagnostic. (keller2024factorsinfluencingsurvival pages 1-2, keller2024naturalhistoryof pages 5-8, yang2023steroidresistantnephroticsyndrome pages 6-7)

Renal biopsy may show FSGS or diffuse mesangial sclerosis, but it is not specific. Plasma/urine sphingolipid profiles and fibroblast S1P-lyase activity provide biochemical support where available; they are not yet standardized population-screening tests. Skin fibroblasts are being used for enzyme assays, therapeutic testing, neuronal reprogramming, and iPSC research. (choi2019sphingosinephosphatelyase pages 4-5, NCT06669949 chunk 3, NCT06669949 chunk 2)

WES and WGS are useful because SPLIS is phenotypically heterogeneous; CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line unless another diagnosis is suspected. Cascade testing of parents and siblings is appropriate. No validated newborn-screening program or consensus diagnostic criteria exist.

### Differential diagnosis

Important alternatives include congenital nephrotic syndromes due to **NPHS1, NPHS2, WT1, LAMB2, PLCE1** and other podocyte genes; isolated familial glucocorticoid deficiency; congenital adrenal hyperplasia; X-linked adrenal hypoplasia; triple-A syndrome; mitochondrial/adrenal-neurologic disorders; Schimke immuno-osseous dysplasia; and other sphingolipidoses. The combination of SRNS, adrenal insufficiency, ichthyosis/immune or neurologic disease, and biallelic SGPL1 variants distinguishes SPLIS.

## 11. Outcome and prognosis

Overall survival at last report in the 76-patient cohort was **50%**. Among patients with nephropathy diagnosed before age one and not transplanted, fewer than 30% were alive two years after diagnosis and 17% were alive at last report; another cohort analysis found only 6/32 (19%) living versus 15/22 (68%) when renal disease was diagnosed at or after one year. Mean age of death among deceased patients was 7.5 months. (keller2024factorsinfluencingsurvival pages 1-2, keller2024naturalhistoryof pages 5-8, keller2024naturalhistoryof pages 18-25)

Major adverse prognostic factors are prenatal presentation, nephropathy in infancy, rapid ESKD, severe multisystem involvement, infection/sepsis, and non-transplant management of kidney failure. Homozygous p.Arg222Gln and kidney transplantation correlate with longer survival. Median age at last report was 8 years after transplantation, 4.4 years with dialysis, and 1.3 years with palliative care; transplantation significantly outperformed dialysis and palliative care, while dialysis did not show a significant survival advantage over palliation in the retrospective analysis. Confounding by patient selection is unavoidable. (keller2024naturalhistoryof pages 14-18, keller2024factorsinfluencingsurvival pages 12-14, keller2024naturalhistoryof pages 18-25)

No robust 5- or 10-year survival curve, standardized disability outcome, life-expectancy estimate, or validated prognostic biomarker is yet available. Plasma S1P and lymphocyte count are candidates under prospective study. (NCT06669949 chunk 1)

## 12. Treatment and current implementation

There is no approved disease-modifying therapy or consensus SPLIS-specific guideline. Care is multidisciplinary and phenotype-directed.

* **Adrenal replacement:** physiologic glucocorticoid replacement, mineralocorticoid and salt replacement when deficient, stress dosing, and emergency hydrocortisone education. Suggested NCIT concepts: corticosteroid therapy; hormone replacement therapy.
* **Renal:** edema/proteinuria management, nutrition, blood-pressure and thrombosis-risk management, dialysis for ESKD, and early evaluation for **kidney transplantation**. Transplantation has the strongest observational survival signal and is a real-world implementation. Suggested NCIT: kidney transplantation; renal dialysis. (keller2024naturalhistoryof pages 14-18, keller2024factorsinfluencingsurvival pages 12-14)
* **Immune/infectious:** prompt antimicrobial therapy, immunoglobulin replacement when clinically indicated, vaccination individualized to immune status, and sepsis prevention. Suggested NCIT: intravenous immunoglobulin therapy; anti-infective therapy.
* **Neurologic/developmental:** seizure treatment, audiology, physical/occupational/speech therapy, mobility support, and developmental services.
* **Endocrine/nutrition/skin:** thyroid or sex-hormone replacement when deficient; nutrition support; emollients and dermatologic treatment.
* **Pyridoxine:** mechanistically rational because SPL is PLP-dependent. Ex vivo improvement and anecdotal clinical benefit have been reported, and unpublished R222Q knock-in mouse observations were cited in the natural-history study. Dose, efficacy, genotype selection, and neurotoxicity monitoring have not been established by controlled trials; it remains off-label/experimental. (keller2024naturalhistoryof pages 1-5, keller2024naturalhistoryof pages 14-18)
* **Gene therapy:** SGPL1 replacement is preclinical. AAV9-SGPL1 has demonstrated target engagement in a mouse lung-fibrosis model, but that is not a SPLIS efficacy trial and cannot establish human benefit.

No disease-specific pharmacogenomic rule, approved RNA therapy, CRISPR treatment, cell therapy, or immunotherapy exists.

### Trials and registries

Two recruiting UCSF studies were retrieved, both observational:

* [NCT04885179](https://clinicaltrials.gov/study/NCT04885179), international registry, estimated enrollment 120, started April 22, 2025; records longitudinal clinical/genetic outcomes and physician-initiated vitamin-B6 exposure without assigning treatment. (NCT04885179 chunk 1)
* [NCT06669949](https://clinicaltrials.gov/study/NCT06669949), three-year natural-history study, estimated enrollment 28, started April 22, 2025; includes renal, endocrine, neurologic, immune, imaging, quality-of-life, sphingolipid, fibroblast, and iPSC assessments. (NCT06669949 chunk 1, NCT06669949 chunk 3, NCT06669949 chunk 2)

No interventional SPLIS trial was identified among the retrieved ClinicalTrials.gov records.

## 13. Prevention

The molecular defect cannot presently be prevented by vaccination, lifestyle change, or environmental avoidance.

* **Primary prevention/reproductive options:** genetic counseling; parental carrier confirmation; cascade testing; prenatal diagnosis by chorionic-villus sampling or amniocentesis; and preimplantation genetic testing for a known familial genotype.
* **Secondary prevention:** early testing of at-risk siblings and infants with congenital nephrosis or adrenal calcification; prospective renal, adrenal, immune, thyroid, neurologic, auditory, and growth surveillance. Population newborn screening is not established.
* **Tertiary prevention:** adrenal stress-dosing plans, infection prevention, early ESKD/transplant planning, thrombosis and nutrition management, skin care, rehabilitation, and avoidance of prolonged ineffective immunosuppression for genetically determined SRNS.

For two carrier parents, counseling should communicate a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability per pregnancy.

## 14. Other species and natural disease

No well-characterized naturally occurring veterinary SPLIS syndrome, breed predisposition, zoonotic transmission, or cross-species infectious susceptibility was identified. The mechanism is evolutionarily conserved, as demonstrated by functional complementation across yeast, Drosophila, mouse, and human SGPL1 systems. Relevant taxa include **Homo sapiens (NCBI Taxon 9606), Mus musculus (10090), Drosophila melanogaster (7227), Caenorhabditis elegans (6239), and Saccharomyces cerevisiae (4932)**. (lovric2017mutationsinsphingosine1phosphate pages 11-14, lovric2017mutationsinsphingosine1phosphate pages 1-2)

## 15. Model organisms and experimental systems

* **Mouse Sgpl1 knockout/partial-deficiency models:** reproduce failure to thrive, early death, proteinuria, glomerular hemorrhage/swelling, podocyte foot-process effacement, immune/lymphocyte abnormalities, skin and skeletal phenotypes, and disturbed adrenal zonation/steroidogenic-enzyme expression. Complete knockout is more severe than many human genotypes and may obscure chronic manifestations. (janecke2017deficiencyofthe pages 11-15, lovric2017mutationsinsphingosine1phosphate pages 11-14, choi2019sphingosinephosphatelyase pages 6-8)
* **Drosophila Sply-null nephrocytes:** show reduced foot-process density, defective albumin uptake/vesicular transport, reduced viability, altered lipid droplets, and sphingoid/ceramide accumulation. Wild-type Sply rescues the phenotype; disease-associated human variants do not fully rescue it. This is a strong functional-variant system but does not model mammalian adrenal physiology. (lovric2017mutationsinsphingosine1phosphate pages 10-11, lovric2017mutationsinsphingosine1phosphate pages 11-14)
* **Yeast dpl1Δ complementation:** wild-type human SGPL1 restores growth while disease alleles fail, providing rapid evidence of functional loss; tissue phenotypes cannot be modeled. (lovric2017mutationsinsphingosine1phosphate pages 1-2, lovric2017mutationsinsphingosine1phosphate pages 2-3)
* **Cellular models:** patient fibroblasts demonstrate low enzyme activity, abnormal protein localization, lipid abnormalities, and impaired migration. SGPL1-silenced rat mesangial cells show reduced RAC1/CDC42 activity and migration, partially rescued by an S1PR1/S1PR3 antagonist. (lovric2017mutationsinsphingosine1phosphate pages 10-11, choi2019sphingosinephosphatelyase pages 5-6)
* **C. elegans spl-1 RNAi:** causes disordered muscle fibers, impaired motility, sphingoid-base/ceramide accumulation, abnormal mitochondria, and increased reactive oxygen species; N-acetylcysteine improved locomotion and muscle organization. This 2024 result is hypothesis-generating and does not support clinical NAC use in SPLIS.
* **iPSC/neuronal models:** prospective natural-history protocols collect fibroblasts for reprogramming and neuronal studies; mature disease-specific organoid, single-cell, or spatial-omics findings were not identified. (NCT06669949 chunk 3)

## Evidence limitations and expert interpretation

The disease literature remains dominated by case reports and retrospective aggregation. Frequencies therefore describe recognized patients rather than unbiased population penetrance. The modeled prevalence of approximately 11,707 affected people contrasts sharply with fewer than 100 diagnosed reports, plausibly reflecting underdiagnosis, fetal loss, unrecognized mild disease, uncertain variant penetrance, and assumptions inherent in Hardy–Weinberg modeling. (sedillo2024prevalenceestimateofa pages 3-4, sedillo2024prevalenceestimateofa pages 1-3)

The most defensible current expert interpretation is that SPLIS should be considered whenever **genetic SRNS and adrenal insufficiency coexist**, but neither manifestation is obligatory. Early comprehensive genetic testing is clinically actionable because it can curtail ineffective immunosuppression, trigger adrenal and immune surveillance, enable family testing, and accelerate transplantation planning. Mechanistic evidence firmly establishes SGPL1 loss, disordered sphingolipid metabolism, podocyte/mesangial injury, and impaired immune-cell trafficking; organ-specific pathways in the adrenal gland and nervous system remain incompletely resolved. Prospective registries, standardized lipid/enzyme biomarkers, and genotype-stratified trials—especially of pyridoxine and gene replacement—are the principal research priorities. (keller2024factorsinfluencingsurvival pages 1-2, lovric2017mutationsinsphingosine1phosphate pages 10-11, choi2019sphingosinephosphatelyase pages 6-8, NCT04885179 chunk 1)

References

1. (keller2024factorsinfluencingsurvival pages 1-2): Nancy Keller, Julian Midgley, Ehtesham Khalid, Harry Lesmana, Georgie Mathew, Christine Mincham, Norbert Teig, Zubair Khan, Indu Khosla, Sam Mehr, Tulay Guran, Kathrin Buder, Hong Xu, Khalid Alhasan, Gonul Buyukyilmaz, Nicole Weaver, and Julie D. Saba. Factors influencing survival in sphingosine phosphate lyase insufficiency syndrome: a retrospective cross-sectional natural history study of 76 patients. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03311-w, doi:10.1186/s13023-024-03311-w. This article has 8 citations and is from a peer-reviewed journal.

2. (keller2024naturalhistoryof pages 5-8): Nancy Keller, Julian Midgley, Ehtesham Khalid, Harry Lesmana, Georgie Mathew, Christine Mincham, Norbert Teig, Zubair Khan, Indu Khosla, Sam Mehr, Tulay Guran, Kathrin Buder, Hong Xu, Khalid Alhasan, Gonul Buyukyilmaz, Nicole Weaver, and Julie D. Saba. Natural history of sphingosine phosphate lyase insufficiency syndrome: a retrospective cross-sectional study of 76 patients. Feb 2024. URL: https://doi.org/10.21203/rs.3.rs-3678833/v1, doi:10.21203/rs.3.rs-3678833/v1.

3. (keller2024factorsinfluencingsurvival pages 12-14): Nancy Keller, Julian Midgley, Ehtesham Khalid, Harry Lesmana, Georgie Mathew, Christine Mincham, Norbert Teig, Zubair Khan, Indu Khosla, Sam Mehr, Tulay Guran, Kathrin Buder, Hong Xu, Khalid Alhasan, Gonul Buyukyilmaz, Nicole Weaver, and Julie D. Saba. Factors influencing survival in sphingosine phosphate lyase insufficiency syndrome: a retrospective cross-sectional natural history study of 76 patients. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03311-w, doi:10.1186/s13023-024-03311-w. This article has 8 citations and is from a peer-reviewed journal.

4. (sedillo2024prevalenceestimateof pages 1-3): JC Sedillo, C Badduke, and SJ Schrodi. Prevalence estimate of sphingosine phosphate lyase insufficiency syndrome in. Unknown journal, 2024.

5. (lovric2017mutationsinsphingosine1phosphate pages 1-2): Svjetlana Lovric, Sara Goncalves, Heon Yung Gee, Babak Oskouian, Honnappa Srinivas, Won-Il Choi, Shirlee Shril, Shazia Ashraf, Weizhen Tan, Jia Rao, Merlin Airik, David Schapiro, Daniela A. Braun, Carolin E. Sadowski, Eugen Widmeier, Tilman Jobst-Schwan, Johanna Magdalena Schmidt, Vladimir Girik, Guido Capitani, Jung H. Suh, Noëlle Lachaussée, Christelle Arrondel, Julie Patat, Olivier Gribouval, Monica Furlano, Olivia Boyer, Alain Schmitt, Vincent Vuiblet, Seema Hashmi, Rainer Wilcken, Francois P. Bernier, A. Micheil Innes, Jillian S. Parboosingh, Ryan E. Lamont, Julian P. Midgley, Nicola Wright, Jacek Majewski, Martin Zenker, Franz Schaefer, Navina Kuss, Johann Greil, Thomas Giese, Klaus Schwarz, Vilain Catheline, Denny Schanze, Ingolf Franke, Yves Sznajer, Anne S. Truant, Brigitte Adams, Julie Désir, Ronald Biemann, York Pei, Elisabet Ars, Nuria Lloberas, Alvaro Madrid, Vikas R. Dharnidharka, Anne M. Connolly, Marcia C. Willing, Megan A. Cooper, Richard P. Lifton, Matias Simons, Howard Riezman, Corinne Antignac, Julie D. Saba, and Friedhelm Hildebrandt. Mutations in sphingosine-1-phosphate lyase cause nephrosis with ichthyosis and adrenal insufficiency. Journal of Clinical Investigation, 127:912–928, Mar 2017. URL: https://doi.org/10.1172/jci89626, doi:10.1172/jci89626. This article has 236 citations and is from a highest quality peer-reviewed journal.

6. (sedillo2024prevalenceestimateofa pages 1-3): JC Sedillo, C Badduke, and SJ Schrodi. Prevalence estimate of sphingosine phosphate lyase insufficiency syndrome in. Unknown journal, 2024.

7. (keller2024naturalhistoryof pages 14-18): Nancy Keller, Julian Midgley, Ehtesham Khalid, Harry Lesmana, Georgie Mathew, Christine Mincham, Norbert Teig, Zubair Khan, Indu Khosla, Sam Mehr, Tulay Guran, Kathrin Buder, Hong Xu, Khalid Alhasan, Gonul Buyukyilmaz, Nicole Weaver, and Julie D. Saba. Natural history of sphingosine phosphate lyase insufficiency syndrome: a retrospective cross-sectional study of 76 patients. Feb 2024. URL: https://doi.org/10.21203/rs.3.rs-3678833/v1, doi:10.21203/rs.3.rs-3678833/v1.

8. (keller2024naturalhistoryof pages 18-25): Nancy Keller, Julian Midgley, Ehtesham Khalid, Harry Lesmana, Georgie Mathew, Christine Mincham, Norbert Teig, Zubair Khan, Indu Khosla, Sam Mehr, Tulay Guran, Kathrin Buder, Hong Xu, Khalid Alhasan, Gonul Buyukyilmaz, Nicole Weaver, and Julie D. Saba. Natural history of sphingosine phosphate lyase insufficiency syndrome: a retrospective cross-sectional study of 76 patients. Feb 2024. URL: https://doi.org/10.21203/rs.3.rs-3678833/v1, doi:10.21203/rs.3.rs-3678833/v1.

9. (lovric2017mutationsinsphingosine1phosphate pages 10-11): Svjetlana Lovric, Sara Goncalves, Heon Yung Gee, Babak Oskouian, Honnappa Srinivas, Won-Il Choi, Shirlee Shril, Shazia Ashraf, Weizhen Tan, Jia Rao, Merlin Airik, David Schapiro, Daniela A. Braun, Carolin E. Sadowski, Eugen Widmeier, Tilman Jobst-Schwan, Johanna Magdalena Schmidt, Vladimir Girik, Guido Capitani, Jung H. Suh, Noëlle Lachaussée, Christelle Arrondel, Julie Patat, Olivier Gribouval, Monica Furlano, Olivia Boyer, Alain Schmitt, Vincent Vuiblet, Seema Hashmi, Rainer Wilcken, Francois P. Bernier, A. Micheil Innes, Jillian S. Parboosingh, Ryan E. Lamont, Julian P. Midgley, Nicola Wright, Jacek Majewski, Martin Zenker, Franz Schaefer, Navina Kuss, Johann Greil, Thomas Giese, Klaus Schwarz, Vilain Catheline, Denny Schanze, Ingolf Franke, Yves Sznajer, Anne S. Truant, Brigitte Adams, Julie Désir, Ronald Biemann, York Pei, Elisabet Ars, Nuria Lloberas, Alvaro Madrid, Vikas R. Dharnidharka, Anne M. Connolly, Marcia C. Willing, Megan A. Cooper, Richard P. Lifton, Matias Simons, Howard Riezman, Corinne Antignac, Julie D. Saba, and Friedhelm Hildebrandt. Mutations in sphingosine-1-phosphate lyase cause nephrosis with ichthyosis and adrenal insufficiency. Journal of Clinical Investigation, 127:912–928, Mar 2017. URL: https://doi.org/10.1172/jci89626, doi:10.1172/jci89626. This article has 236 citations and is from a highest quality peer-reviewed journal.

10. (janecke2017deficiencyofthe pages 11-15): Andreas R. Janecke, Ruijuan Xu, Elisabeth Steichen-Gersdorf, Siegfried Waldegger, Andreas Entenmann, Thomas Giner, Iris Krainer, Lukas A Huber, Michael W Hess, Yaacov Frishberg, Hila Barash, Shay Tzur, Nira Schreyer-Shafir, Rivka Sukenik-Halevy, Tania Zehavi, Annick Raas-Rothschild, Cungui Mao, and Thomas Müller. Deficiency of the sphingosine‐1‐phosphate lyase sgpl1 is associated with congenital nephrotic syndrome and congenital adrenal calcifications. Human Mutation, 38:365-372, Apr 2017. URL: https://doi.org/10.1002/humu.23192, doi:10.1002/humu.23192. This article has 103 citations and is from a domain leading peer-reviewed journal.

11. (choi2019sphingosinephosphatelyase pages 5-6): Youn-Jeong Choi and Julie D. Saba. Sphingosine phosphate lyase insufficiency syndrome (splis): a novel inborn error of sphingolipid metabolism. Advances in biological regulation, 71:128-140, Jan 2019. URL: https://doi.org/10.1016/j.jbior.2018.09.004, doi:10.1016/j.jbior.2018.09.004. This article has 61 citations and is from a peer-reviewed journal.

12. (choi2019sphingosinephosphatelyase pages 4-5): Youn-Jeong Choi and Julie D. Saba. Sphingosine phosphate lyase insufficiency syndrome (splis): a novel inborn error of sphingolipid metabolism. Advances in biological regulation, 71:128-140, Jan 2019. URL: https://doi.org/10.1016/j.jbior.2018.09.004, doi:10.1016/j.jbior.2018.09.004. This article has 61 citations and is from a peer-reviewed journal.

13. (NCT06669949 chunk 1):  Natural History of Sphingosine Phosphate Lyase Insufficiency Syndrome (SPLIS). University of California, San Francisco. 2025. ClinicalTrials.gov Identifier: NCT06669949

14. (NCT06669949 chunk 2):  Natural History of Sphingosine Phosphate Lyase Insufficiency Syndrome (SPLIS). University of California, San Francisco. 2025. ClinicalTrials.gov Identifier: NCT06669949

15. (NCT04885179 chunk 1):  SPL Insufficiency Syndrome (SPLIS)/NPHS14: a SPLIS Observational Study and Patient Registry (International). University of California, San Francisco. 2025. ClinicalTrials.gov Identifier: NCT04885179

16. (NCT06669949 chunk 3):  Natural History of Sphingosine Phosphate Lyase Insufficiency Syndrome (SPLIS). University of California, San Francisco. 2025. ClinicalTrials.gov Identifier: NCT06669949

17. (OpenTargets Search: Sphingosine phosphate lyase insufficiency syndrome-SGPL1): Open Targets Query (Sphingosine phosphate lyase insufficiency syndrome-SGPL1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

18. (sedillo2024prevalenceestimateofa pages 3-4): JC Sedillo, C Badduke, and SJ Schrodi. Prevalence estimate of sphingosine phosphate lyase insufficiency syndrome in. Unknown journal, 2024.

19. (keller2024factorsinfluencingsurvival pages 2-4): Nancy Keller, Julian Midgley, Ehtesham Khalid, Harry Lesmana, Georgie Mathew, Christine Mincham, Norbert Teig, Zubair Khan, Indu Khosla, Sam Mehr, Tulay Guran, Kathrin Buder, Hong Xu, Khalid Alhasan, Gonul Buyukyilmaz, Nicole Weaver, and Julie D. Saba. Factors influencing survival in sphingosine phosphate lyase insufficiency syndrome: a retrospective cross-sectional natural history study of 76 patients. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03311-w, doi:10.1186/s13023-024-03311-w. This article has 8 citations and is from a peer-reviewed journal.

20. (yang2023steroidresistantnephroticsyndrome pages 6-7): Siying Yang, Yonghua He, Jianhua Zhou, Huiqing Yuan, and Liru Qiu. Steroid-resistant nephrotic syndrome associated with certain sgpl1 variants in a family: case report and literature review. Frontiers in Pediatrics, Feb 2023. URL: https://doi.org/10.3389/fped.2023.1079758, doi:10.3389/fped.2023.1079758. This article has 11 citations.

21. (keller2024naturalhistoryof pages 1-5): Nancy Keller, Julian Midgley, Ehtesham Khalid, Harry Lesmana, Georgie Mathew, Christine Mincham, Norbert Teig, Zubair Khan, Indu Khosla, Sam Mehr, Tulay Guran, Kathrin Buder, Hong Xu, Khalid Alhasan, Gonul Buyukyilmaz, Nicole Weaver, and Julie D. Saba. Natural history of sphingosine phosphate lyase insufficiency syndrome: a retrospective cross-sectional study of 76 patients. Feb 2024. URL: https://doi.org/10.21203/rs.3.rs-3678833/v1, doi:10.21203/rs.3.rs-3678833/v1.

22. (lovric2017mutationsinsphingosine1phosphate pages 11-14): Svjetlana Lovric, Sara Goncalves, Heon Yung Gee, Babak Oskouian, Honnappa Srinivas, Won-Il Choi, Shirlee Shril, Shazia Ashraf, Weizhen Tan, Jia Rao, Merlin Airik, David Schapiro, Daniela A. Braun, Carolin E. Sadowski, Eugen Widmeier, Tilman Jobst-Schwan, Johanna Magdalena Schmidt, Vladimir Girik, Guido Capitani, Jung H. Suh, Noëlle Lachaussée, Christelle Arrondel, Julie Patat, Olivier Gribouval, Monica Furlano, Olivia Boyer, Alain Schmitt, Vincent Vuiblet, Seema Hashmi, Rainer Wilcken, Francois P. Bernier, A. Micheil Innes, Jillian S. Parboosingh, Ryan E. Lamont, Julian P. Midgley, Nicola Wright, Jacek Majewski, Martin Zenker, Franz Schaefer, Navina Kuss, Johann Greil, Thomas Giese, Klaus Schwarz, Vilain Catheline, Denny Schanze, Ingolf Franke, Yves Sznajer, Anne S. Truant, Brigitte Adams, Julie Désir, Ronald Biemann, York Pei, Elisabet Ars, Nuria Lloberas, Alvaro Madrid, Vikas R. Dharnidharka, Anne M. Connolly, Marcia C. Willing, Megan A. Cooper, Richard P. Lifton, Matias Simons, Howard Riezman, Corinne Antignac, Julie D. Saba, and Friedhelm Hildebrandt. Mutations in sphingosine-1-phosphate lyase cause nephrosis with ichthyosis and adrenal insufficiency. Journal of Clinical Investigation, 127:912–928, Mar 2017. URL: https://doi.org/10.1172/jci89626, doi:10.1172/jci89626. This article has 236 citations and is from a highest quality peer-reviewed journal.

23. (choi2019sphingosinephosphatelyase pages 6-8): Youn-Jeong Choi and Julie D. Saba. Sphingosine phosphate lyase insufficiency syndrome (splis): a novel inborn error of sphingolipid metabolism. Advances in biological regulation, 71:128-140, Jan 2019. URL: https://doi.org/10.1016/j.jbior.2018.09.004, doi:10.1016/j.jbior.2018.09.004. This article has 61 citations and is from a peer-reviewed journal.

24. (lovric2017mutationsinsphingosine1phosphate pages 2-3): Svjetlana Lovric, Sara Goncalves, Heon Yung Gee, Babak Oskouian, Honnappa Srinivas, Won-Il Choi, Shirlee Shril, Shazia Ashraf, Weizhen Tan, Jia Rao, Merlin Airik, David Schapiro, Daniela A. Braun, Carolin E. Sadowski, Eugen Widmeier, Tilman Jobst-Schwan, Johanna Magdalena Schmidt, Vladimir Girik, Guido Capitani, Jung H. Suh, Noëlle Lachaussée, Christelle Arrondel, Julie Patat, Olivier Gribouval, Monica Furlano, Olivia Boyer, Alain Schmitt, Vincent Vuiblet, Seema Hashmi, Rainer Wilcken, Francois P. Bernier, A. Micheil Innes, Jillian S. Parboosingh, Ryan E. Lamont, Julian P. Midgley, Nicola Wright, Jacek Majewski, Martin Zenker, Franz Schaefer, Navina Kuss, Johann Greil, Thomas Giese, Klaus Schwarz, Vilain Catheline, Denny Schanze, Ingolf Franke, Yves Sznajer, Anne S. Truant, Brigitte Adams, Julie Désir, Ronald Biemann, York Pei, Elisabet Ars, Nuria Lloberas, Alvaro Madrid, Vikas R. Dharnidharka, Anne M. Connolly, Marcia C. Willing, Megan A. Cooper, Richard P. Lifton, Matias Simons, Howard Riezman, Corinne Antignac, Julie D. Saba, and Friedhelm Hildebrandt. Mutations in sphingosine-1-phosphate lyase cause nephrosis with ichthyosis and adrenal insufficiency. Journal of Clinical Investigation, 127:912–928, Mar 2017. URL: https://doi.org/10.1172/jci89626, doi:10.1172/jci89626. This article has 236 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Sphingosine_Phosphate_Lyase_Insufficiency_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0033203` (2 mentions) - the report calls it "if available"; MONDO calls it **nephrotic syndrome 14**