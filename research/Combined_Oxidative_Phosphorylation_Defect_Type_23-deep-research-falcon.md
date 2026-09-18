---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T11:27:13.697889'
end_time: '2026-09-08T11:40:13.527749'
duration_seconds: 779.83
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Defect Type 23
  mondo_id: MONDO:0014525
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 46
  verified: 44
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014525
    reported_labels:
    - if available
    ontology_label: combined oxidative phosphorylation defect type 23
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  - MIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Combined_Oxidative_Phosphorylation_Defect_Type_23-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 23
- **MONDO ID:** MONDO:0014525 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 23** covering all of the
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
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 23
- **MONDO ID:** MONDO:0014525 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 23** covering all of the
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


# Combined Oxidative Phosphorylation Defect Type 23 (COXPD23)

## Executive summary

Combined oxidative phosphorylation defect/deficiency type 23 (COXPD23) is an ultrarare, autosomal-recessive mitochondrial translation disorder caused by biallelic germline variants in **GTPBP3**. Defective GTPBP3-dependent wobble-uridine modification of selected mitochondrial tRNAs compromises mitochondrial protein synthesis and respiratory-chain function. The characteristic clinical triad is **hyperlactatemia/lactic acidosis, cardiomyopathy, and encephalopathy**, but severity ranges from fatal neonatal heart failure to a more slowly progressive childhood neurodevelopmental disorder. In the largest systematic synthesis available in the requested 2023–2024 window (18 patients), hyperlactatemia occurred in 100%, cardiomyopathy in 72%, and abnormal brain MRI in 61%; these percentages are highly vulnerable to publication and ascertainment bias. (zhang2023pathogenicityanalysisof pages 1-2, zhang2023pathogenicityanalysisof pages 4-7)

The evidence base remains exceptionally small. Most knowledge comes from individual patients, the original 11-patient study, three Chinese cases, and a 2023 literature synthesis—not registries or population cohorts. No validated disease-specific diagnostic criteria, approved disease-modifying treatment, prevalence estimate, or COXPD23-specific interventional trial was identified.

| Field | High-confidence finding | Suggested ontology/identifier | Evidence / limitations |
|---|---|---|---|
| Disease identity | Combined oxidative phosphorylation deficiency/defect type 23 (COXPD23), a nuclear-encoded mitochondrial translation disorder | **MONDO:0014525**; **EFO:0009033** | Disease naming is consistent across aggregated disease resources and clinical literature. (OpenTargets Search: combined oxidative phosphorylation defect type 23, zhang2023pathogenicityanalysisof pages 1-2) |
| OMIM identifiers | The **disease** identifier is **OMIM #616198**; **MIM 608536** identifies the causal **GTPBP3 gene**, not the disease | OMIM:616198; MIM:608536 | Some publications incorrectly label COXPD23 itself as OMIM 608536; database curation should preserve the disease–gene distinction. (yan2021novelmutationsin pages 1-2, magistrati2023modopathiescausedby pages 11-12) |
| Causal gene | Biallelic germline variants in **GTPBP3**, encoding mitochondrial GTP-binding protein 3 | HGNC symbol: **GTPBP3**; Ensembl: **ENSG00000130299** | OpenTargets identifies GTPBP3 as the sole associated target for EFO:0009033; causal association was established in the original patient cohort. (OpenTargets Search: combined oxidative phosphorylation defect type 23, martinezzamora2015defectiveexpressionof pages 2-3) |
| Inheritance | Autosomal recessive; affected individuals are homozygous or compound heterozygous, while parents are generally unaffected heterozygous carriers | Suggested HPO: **HP:0000007 Autosomal recessive inheritance** | Supported by segregation in multiple families; penetrance among individuals with confirmed pathogenic biallelic variants appears high, but formal penetrance estimates are unavailable. (yan2021novelmutationsin pages 2-4, zhang2023pathogenicityanalysisof pages 2-4) |
| Core metabolic phenotype | Persistent or episodic hyperlactatemia/lactic acidosis occurred in **18/18 (100%)** patients in the 2023 synthesis | Suggested HPO: **HP:0002151 Increased circulating lactate concentration**; **HP:0003128 Lactic acidosis** | Frequency derives from only 18 published patients and is vulnerable to ascertainment bias. Reported lactate values include approximately 3–29 mmol/L. (zhang2023pathogenicityanalysisof pages 4-7, zhang2023pathogenicityanalysisof pages 10-11) |
| Cardiac phenotype | Cardiomyopathy occurred in **72%** of the 18-patient synthesis, usually hypertrophic cardiomyopathy/ventricular hypertrophy; dilated cardiomyopathy, reduced contractility, arrhythmia, heart failure, and Wolff–Parkinson–White syndrome have also been reported | Suggested HPO: **HP:0001639 Hypertrophic cardiomyopathy**; **HP:0001644 Dilated cardiomyopathy**; **HP:0001635 Congestive heart failure**; UBERON: **UBERON:0000948 heart**; CL suggestion: **CL:0000746 cardiac muscle cell** | Cardiac failure and arrhythmia are enriched in severe infantile disease; congestive heart failure is a major reported cause of early death. (zhang2023pathogenicityanalysisof pages 9-10, zhang2023pathogenicityanalysisof pages 11-13, zhang2023pathogenicityanalysisof pages 4-7) |
| Neurologic and developmental phenotype | Developmental delay, intellectual disability, hypotonia, fatigability/weakness, seizures, impaired coordination, feeding difficulty, visual impairment, and occasional hearing impairment form a variable encephalomyopathic spectrum | Suggested HPO: **HP:0001263 Global developmental delay**; **HP:0001252 Muscular hypotonia**; **HP:0001250 Seizure**; **HP:0001324 Muscle weakness**; **HP:0002015 Dysphagia**; **HP:0000505 Visual impairment** | Individual manifestations are not universal. Developmental delay was significantly enriched in the mild/surviving group in the small 2023 comparison. (zhang2023pathogenicityanalysisof pages 9-10, zhang2023pathogenicityanalysisof pages 2-4, zhang2023pathogenicityanalysisof pages 4-7) |
| Neuroimaging | Abnormal brain MRI occurred in **61%** of the 18-patient synthesis; recurrent bilateral lesions involve the thalami, brainstem/midbrain, dentate nuclei/cerebellum, and occasionally corticospinal tracts, producing a Leigh-like pattern | Suggested HPO: **HP:0002072 Cerebral MRI abnormality**; **HP:0002435 Molar tooth sign** is **not** appropriate; anatomical suggestions: **UBERON:0001897 dorsal thalamus**, **UBERON:0002298 brainstem**, **UBERON:0002037 cerebellum** | No pathognomonic imaging pattern or formal radiologic criterion exists; MRI may be normal or undocumented. (yan2021novelmutationsin pages 7-8, zhang2023pathogenicityanalysisof pages 4-7, zhang2023pathogenicityanalysisof pages 10-11) |
| Temporal course | Two broad observational forms are described: severe neonatal/infantile metabolic decompensation with rapid cardiac deterioration and death, and milder childhood encephalocardiomyopathy with survival into the second decade or beyond | Suggested HPO: **HP:0003623 Neonatal onset**; **HP:0003593 Infantile onset**; **HP:0011463 Childhood onset** | Mean onset in the 18-patient review was **1.7 years**. Severe disease was defined retrospectively, not by validated staging criteria. (zhang2023pathogenicityanalysisof pages 1-2, yan2021novelmutationsin pages 7-8, zhang2023pathogenicityanalysisof pages 11-13) |
| Genotype–phenotype signal | Homozygosity was more frequent in severe disease (**5/7; 71.43%**) than mild disease (**2/11; 18.18%**, p=0.0491); severe variants tended to disrupt the N-terminal or TrmE-type G domain | GTPBP3 TrmE-type GTP-binding domain: residues approximately 249–416 | This is a hypothesis-generating association based on 18 patients; variants in the same region can yield different severities, so genotype alone is not prognostic. (zhang2023pathogenicityanalysisof pages 13-15, zhang2023pathogenicityanalysisof pages 4-7, yan2021novelmutationsin pages 7-8) |
| Molecular lesion | Loss or reduction of GTPBP3 activity impairs MTO1/GTPBP3-dependent 5-taurinomethyl modification of wobble uridine U34 in selected mitochondrial tRNAs | Suggested GO: **GO:0006399 tRNA metabolic process**; **GO:0006400 tRNA modification**; cellular component: **GO:0005739 mitochondrion** | GTPBP3/MTO1 modifies mt-tRNAs for Leu(UUR), Trp, Glu, Gln, and Lys; the exact chemical endpoint differs among substrates, including τm5U and τm5s2U. (yan2021novelmutationsin pages 4-6, magistrati2023modopathiescausedby pages 11-12, martinezzamora2015defectiveexpressionof pages 2-3) |
| Downstream mechanism | U34 hypomodification leads to inaccurate/inefficient codon decoding, defective mitochondrial translation, reduced respiratory-chain complex I and IV function, impaired oxidative phosphorylation, ATP depletion, and increased oxidative stress | Suggested GO: **GO:0032543 mitochondrial translation**; **GO:0006119 oxidative phosphorylation**; **GO:0006120 mitochondrial electron transport, NADH to ubiquinone**; **GO:0006979 response to oxidative stress** | Demonstrated in patient fibroblasts and GTPBP3 knockout/knockdown cells. Cellular silencing reduced ATP by approximately 40–50% and increased mitochondrial superoxide by about 28%; tissue injury downstream is biologically compelling but partly inferred. (yan2021novelmutationsin pages 4-6, yan2021novelmutationsin pages 6-7, martinezzamora2015defectiveexpressionof pages 8-10) |
| Adaptive cellular responses | Energy failure activates AMPK-dependent retrograde signaling, increases glycolytic and fatty-acid-oxidation programs and UCP2, and promotes mitochondrial fragmentation/autophagic flux | Suggested GO: **GO:0006914 autophagy**; **GO:0007005 mitochondrion organization**; **GO:0006096 glycolytic process**; **GO:0032007 negative regulation of TOR signaling** | Primarily based on stable-silencing cell models rather than affected human tissues; immune-mediated pathology has not been established. (yan2021novelmutationsin pages 6-7, martinezzamora2015defectiveexpressionof pages 8-10) |
| Main diagnostic approach | Clinical suspicion from lactic acidosis plus cardiomyopathy and/or encephalopathy should prompt nuclear mitochondrial-disease panel or trio WES/WGS with **GTPBP3** analysis, parental segregation, and ACMG/AMP classification | Genetic marker: biallelic **GTPBP3** variants; suggested HPO bundle: HP:0003128 + HP:0001639 + HP:0001263 | Sequencing has been the decisive test. WGS may detect coding, splice, CNV, and mitochondrial-genome alternatives; CMA, karyotype, FISH, and repeat-expansion testing are not first-line for this single-gene disorder. (zhang2023pathogenicityanalysisof pages 2-4, zhang2023pathogenicityanalysisof pages 11-13, yan2021novelmutationsin pages 2-4) |
| Supporting diagnostics | Blood/CSF lactate, blood gas, alanine, CK/CK-MB, BNP, plasma amino acids/acylcarnitines, urine organic acids, echocardiography/ECG, brain MRI, EEG, and respiratory-chain enzymology can characterize disease | Suggested HPO: **HP:0003348 Hyperalaninemia**; **HP:0003256 Elevated serum creatine kinase**; anatomical suggestions: UBERON heart/brain/skeletal muscle | Biomarkers are nonspecific and may be normal except for lactate. Muscle biopsy often shows severe complexes I and IV deficiency but normal muscle or fibroblast testing does not exclude COXPD23. (magistrati2023modopathiescausedby pages 11-12, martinezzamora2015defectiveexpressionof pages 2-3, yan2021novelmutationsin pages 2-4) |
| Treatment status | No approved disease-modifying treatment and no COXPD23-specific registered interventional trial were identified; current care is supportive and organ-directed | Suggested NCIT interventions: **C15313 Supportive Care**, **C16210 Mechanical Ventilation**, **C15953 Physical Therapy**; supplement mappings should be curated separately | Thiamine, riboflavin, coenzyme Q10, L-carnitine, and vitamins C/E have been used empirically without demonstrated sustained benefit in reported COXPD23 cases. Cardiac, seizure, nutritional, respiratory, and rehabilitative care should be individualized. (obyrne2018thegenotypicand pages 16-18, yan2021novelmutationsin pages 2-4) |
| Epidemiology | Disease-specific prevalence, incidence, carrier frequency, sex ratio, and geographic distribution are unknown; published cases span multiple ancestries | Orphan/ultrarare Mendelian disease; no validated population-rate identifier | Approximately 18 patients had been systematically summarized by 2023, but published-case counts are not prevalence estimates. Consanguinity occurs in some families but is not required. (zhang2023pathogenicityanalysisof pages 1-2, zhang2023pathogenicityanalysisof pages 11-13, yan2021novelmutationsin pages 7-8) |
| Prevention and counseling | Molecular confirmation enables parental carrier testing, cascade testing, 25% recurrence-risk counseling, prenatal diagnosis, and preimplantation genetic testing when familial pathogenic variants are known | Suggested HPO: **HP:0034340 Carrier of genetic disorder**; intervention concepts: genetic counseling, prenatal genetic testing, preimplantation genetic testing | These options follow autosomal-recessive genetics; no environmental, dietary, infectious, or vaccine-based primary prevention is established for COXPD23. (yan2021novelmutationsin pages 2-4, zhang2023pathogenicityanalysisof pages 1-2) |
| Model systems | Models include patient fibroblasts, stable GTPBP3-silenced cells, GTPBP3-knockout cells, and a **gtpbp3**-deficient zebrafish model that develops hypertrophic cardiomyopathy and abnormal mitochondrial tRNA metabolism | Cell suggestions: fibroblast **CL:0000057**, cardiomyocyte **CL:0000746**; organism: *Danio rerio*, NCBI Taxon **7955** | Cellular models reproduce translation/OXPHOS defects and adaptive stress responses; zebrafish supports cardiac causality. As of the 2023–2024 evidence window, no widely established COXPD23-specific mouse natural-history model or patient organoid platform was reported. (martinezzamora2015defectiveexpressionof pages 8-10, zhang2023pathogenicityanalysisof pages 13-15) |


*Table: High-confidence identifiers, phenotypes, mechanism, diagnostic approach, treatment status, and model systems for GTPBP3-related combined oxidative phosphorylation deficiency 23. Suggested ontology mappings and major evidence limitations are explicitly marked.*

## 1. Disease information

**Definition.** COXPD23 is a nuclear-encoded mitochondrial “modopathy”: loss of a mitochondrial RNA-modifying enzyme produces defective mitochondrial translation and combined oxidative-phosphorylation dysfunction. The causal association was established in 2014 in 11 individuals from nine families (Kopajtich et al., *American Journal of Human Genetics*, December 2014; **PMID: 25434004**). OpenTargets independently maps the disease to GTPBP3 as its sole associated target. (OpenTargets Search: combined oxidative phosphorylation defect type 23, martinezzamora2015defectiveexpressionof pages 2-3)

**Identifiers and names.** Recommended identifiers are **MONDO:0014525**, **EFO:0009033**, and **OMIM #616198**. A recurring curation pitfall is that **MIM 608536 denotes GTPBP3**, not the disease. Synonyms include “combined oxidative phosphorylation deficiency 23,” “combined oxidative phosphorylation defect type 23,” “COXPD23,” and “GTPBP3-related mitochondrial disease.” No specific MeSH descriptor or dedicated ICD-10/ICD-11 code was established in the retrieved evidence; broader mitochondrial-metabolism codes are therefore used clinically and should not be treated as disease-specific identifiers. (OpenTargets Search: combined oxidative phosphorylation defect type 23, yan2021novelmutationsin pages 1-2, magistrati2023modopathiescausedby pages 11-12)

**Evidence granularity.** Published evidence is predominantly patient-level case-series information subsequently aggregated into disease-level reviews. It is not derived from EHR-scale cohorts, prospective registries, or population surveillance.

## 2. Etiology, risk, protection, and gene–environment interaction

The necessary cause is **biallelic pathogenic or likely pathogenic GTPBP3 variation**. Reported alleles include missense, nonsense, frameshift, splice, start-loss, and small in-frame deletion variants. Healthy parents typically carry one allele, establishing autosomal-recessive inheritance. (yan2021novelmutationsin pages 2-4, zhang2023pathogenicityanalysisof pages 7-8)

The 2023 analysis assembled 35 disease-associated variants—18 missense, 11 frameshift, three nonsense, two splice, and one in-frame deletion. Loss-of-function variants comprised 16/35 (45.7%), compared with 20/225 (8.9%) among rare population variants after filtering (p<0.0001), supporting loss of function as a major mechanism. This comparison does **not** mean that every listed ClinVar allele is definitively pathogenic; classification must be performed per variant and transcript using current ACMG/AMP criteria. (zhang2023pathogenicityanalysisof pages 11-13, zhang2023pathogenicityanalysisof pages 4-7)

No environmental, infectious, occupational, lifestyle, age-, or sex-dependent cause has been demonstrated. Consanguinity raises the probability of homozygosity but is not required. No validated protective GTPBP3 allele, dietary factor, epigenetic modifier, or gene–environment interaction is known. Taurine is a biochemical substrate of the modification pathway, but evidence does not establish dietary taurine deficiency as a cause of COXPD23 or supplementation as disease prevention. Cellular taurine observations should not be translated into a clinical recommendation.

A possible ancestry-associated allele is **c.689A>C (p.Gln230Pro)**: the 2023 analysis reported frequencies of 0.0002744 in Han Chinese, 0.0001089 in East Asians, and absence from other represented groups, while five Chinese patients carrying it shared relatively mild, surviving phenotypes. The numbers are too small to establish a founder effect or reliable prognostic association. (zhang2023pathogenicityanalysisof pages 10-11)

## 3. Phenotypes

The best quantitative dataset contained only 18 affected individuals: hyperlactatemia **18/18 (100%)**, cardiomyopathy **72%**, and abnormal brain MRI **61%**. Mean reported onset was 1.7 years. Seven patients were retrospectively classified as severe and 11 as mild. (zhang2023pathogenicityanalysisof pages 4-7)

* **Metabolic:** persistent or decompensating hyperlactatemia/lactic acidosis (HP:0002151; HP:0003128), metabolic acidosis (HP:0001942), and sometimes hyperalaninemia (HP:0003348). Reported lactate values extended approximately from 3 to 29 mmol/L. Urine may show lactate, 3-hydroxybutyrate, 3-methylglutaconate, or 3-hydroxyglutarate, but profiles can be normal. (zhang2023pathogenicityanalysisof pages 10-11, yan2021novelmutationsin pages 2-4)
* **Cardiac:** hypertrophic cardiomyopathy/left- or biventricular hypertrophy (HP:0001639), less commonly dilated cardiomyopathy (HP:0001644), impaired contractility, arrhythmia (HP:0011675), Wolff–Parkinson–White pattern, myocardial injury, and congestive heart failure (HP:0001635). Arrhythmia and heart failure were significantly enriched in severe disease; heart failure is the principal documented cause of infant death. (zhang2023pathogenicityanalysisof pages 9-10, zhang2023pathogenicityanalysisof pages 11-13, zhang2023pathogenicityanalysisof pages 4-7)
* **Neurologic/developmental:** global developmental delay (HP:0001263), intellectual disability (HP:0001249), hypotonia (HP:0001252), weakness/fatigability (HP:0001324), ataxic or poorly coordinated gait, seizures (HP:0001250), hyporeactivity, feeding difficulty, visual impairment, and occasional hearing impairment. Developmental delay was more prominent in surviving “mild” cases, probably because severely affected infants die before it can be assessed. (zhang2023pathogenicityanalysisof pages 9-10, zhang2023pathogenicityanalysisof pages 2-4)
* **Imaging:** bilateral thalamic, midbrain/brainstem, cerebellar dentate, and occasionally corticospinal-tract abnormalities produce a **Leigh-like** pattern (general MRI abnormality, HP:0002072). Diffusion restriction and persistence without radiologic improvement have been documented. (yan2021novelmutationsin pages 7-8, yan2021novelmutationsin pages 2-4)
* **Growth and behavior:** short stature and impaired language acquisition have occurred, but no reproducible primary psychiatric or behavioral syndrome is established.

Onset and severity vary from metabolic collapse in the first days of life to childhood or, in isolated newer observations, later cardiac presentation. Manifestations may be chronically stable, progressive, or episodically decompensating. No phenotype-specific quality-of-life instrument, EQ-5D, SF-36, or PROMIS dataset exists. Nevertheless, impaired mobility, communication, feeding, vision, seizure control, and cardiac exercise tolerance imply major effects on daily function.

## 4. Genetic and molecular information

**Gene.** GTPBP3 lies at **19p13.11** and encodes a 492-amino-acid mitochondrial GTPase/tRNA-modifying protein. OpenTargets gives Ensembl **ENSG00000130299**. Suggested annotation is HGNC symbol **GTPBP3**; gene MIM **608536**. Its reported regions include a mitochondrial targeting peptide (approximately residues 1–81), N-terminal domain, central helical regions, and a TrmE-type GTP-binding domain at approximately residues 249–416. Conserved G motifs bind guanine nucleotide and Mg²⁺ and mediate GTP hydrolysis/conformational cycling. (OpenTargets Search: combined oxidative phosphorylation defect type 23, zhang2023pathogenicityanalysisof pages 13-15)

Illustrative variants include c.32_33delinsGTG (p.Gln11Argfs*98), c.413C>T (p.Ala138Val), c.424G>A (p.Glu142Lys), c.509_510del (p.Glu170Glyfs*42), c.544G>T (reported as p.Gly182Ter), c.673G>A (p.Glu225Lys), c.689A>C (p.Gln230Pro), c.785A>C (p.Gln262Pro), c.934_957del (p.Gly312_Val319del), c.964G>C (p.Ala322Pro), and c.1102dupC (p.Arg368Profs*22). The Chinese series classified several truncating or segregating alleles as likely pathogenic while p.Gln262Pro and p.Glu142Lys initially retained uncertainty, illustrating why literature labels should not replace current ClinVar/ACMG reassessment. (yan2021novelmutationsin pages 4-6, zhang2023pathogenicityanalysisof pages 7-8, yan2021novelmutationsin pages 2-4)

The variants are constitutional/germline, not somatic cancer variants. Frameshift, nonsense, and canonical splice alleles are expected to cause nonsense-mediated decay or truncated protein; missense alleles can impair stability, GTPase activity, tRNA recognition, or catalytic function. Disease alleles are generally absent or extremely rare in population databases; examples in the 2023 table ranged from undetected to approximately 6.4×10⁻⁴, but frequency must be checked against the precise transcript, ancestry, and current gnomAD release. (zhang2023pathogenicityanalysisof pages 11-13, zhang2023pathogenicityanalysisof pages 7-8)

A tentative genotype–phenotype signal exists: homozygous variants occurred in 5/7 severe cases (71.43%) versus 2/11 mild cases (18.18%; p=0.0491), and severe alleles tended to affect the N terminus or G domain. This is underpowered and not suitable for individual prognostication. No validated modifier gene, disease-specific methylation signature, chromosomal rearrangement, or pathogenic large-scale cytogenetic abnormality is known. (zhang2023pathogenicityanalysisof pages 4-7, zhang2023pathogenicityanalysisof pages 10-11)

## 5. Environmental information

COXPD23 is not caused by toxins, radiation, pollution, occupation, smoking, alcohol, diet, or infection. Intercurrent illness, fasting, dehydration, surgery, or prolonged physiologic stress may plausibly precipitate metabolic decompensation in mitochondrial disease, but COXPD23-specific effect sizes have not been measured. There is no zoonotic or transmissible component.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic GTPBP3 loss-of-function or damaging missense variants lead to** reduced abundance, GTPase activity, or catalytic function of mitochondrial GTPBP3.
2. **Defective GTPBP3–MTO1 activity leads to** deficient 5-taurinomethyl modification of wobble uridine U34 in selected mt-tRNAs.
3. **U34 hypomodification leads to** inefficient or inaccurate mitochondrial codon decoding and, in some substrates, altered tRNA stability/aminoacylation.
4. **Defective decoding leads to** reduced synthesis of mtDNA-encoded respiratory-chain subunits.
5. **Reduced mitochondrial translation leads to** defective assembly/activity of OXPHOS complexes, especially complexes I and IV; complex II, which is entirely nuclear encoded, is relatively spared.
6. **OXPHOS failure leads to** reduced oxygen consumption, membrane potential, and ATP, with increased electron leak and mitochondrial superoxide.
7. **Energy failure leads to** AMPK-mediated metabolic adaptation, increased glycolytic reliance, altered fatty-acid oxidation/UCP2, and autophagic or mitophagic responses.
8. **Greater glycolytic reliance leads to** pyruvate-to-lactate flux and systemic hyperlactatemia/lactic acidosis.
9. **ATP deficiency and oxidative stress in high-demand tissues lead to** cardiomyocyte dysfunction/hypertrophy and neuronal network injury; this tissue-level link is strongly biologically supported but partly inferred rather than longitudinally demonstrated in patients.
10. **Cardiac injury branches to** arrhythmia, contractile failure, and fatal CHF, while **neural injury branches to** developmental delay, hypotonia, seizures, visual dysfunction, and Leigh-like MRI lesions.

GTPBP3 and MTO1 use taurine and 5,10-methylenetetrahydrofolate, with GTP, K⁺, FAD, and reducing equivalents in the modification pathway. The relevant mt-tRNAs include Leu(UUR), Trp, Glu, Gln, and Lys; products include τm⁵U in Leu(UUR)/Trp and predominantly τm⁵s²U in Glu/Gln/Lys. These wobble modifications promote cognate purine-ending codon recognition and suppress near-cognate decoding. (zhang2026molecularpathogenesisand pages 1-5, magistrati2023modopathiescausedby pages 11-12, martinezzamora2015defectiveexpressionof pages 2-3)

In knockout cells, τm⁵U was absent from mt-tRNA-Leu(UUR) and mt-tRNA-Trp, with reduced mitochondrial translation, oxygen consumption, complex-I proteins, and complex-I activity. Stable knockdown reduced ATP by approximately 40–50%, increased mitochondrial superoxide by about 28%, activated AMPK, nearly doubled UCP2, and increased autophagic flux. Complex I was markedly reduced, complex IV was relatively preserved in that knockdown system, and complex V ATPase increased—possibly to maintain membrane potential by reverse operation. (yan2021novelmutationsin pages 4-6, yan2021novelmutationsin pages 6-7, martinezzamora2015defectiveexpressionof pages 8-10)

Patient fibroblasts show variable biochemical severity: three of four studied individuals had severely reduced mitochondrial translation, while the fourth had no detectable translation defect despite death from cardiac failure. Most muscle biopsies in the original cohort showed severe complex-I and IV deficiencies, but an atypical patient had normal muscle respiratory-complex activity. Therefore, a normal fibroblast or muscle result does not exclude disease. (magistrati2023modopathiescausedby pages 11-12, martinezzamora2015defectiveexpressionof pages 2-3)

Suggested GO terms include mitochondrial tRNA modification (**GO:0006400**), mitochondrial translation (**GO:0032543**), oxidative phosphorylation (**GO:0006119**), mitochondrial electron transport/NADH to ubiquinone (**GO:0006120**), response to oxidative stress (**GO:0006979**), autophagy (**GO:0006914**), and mitochondrion organization (**GO:0007005**). Relevant cell suggestions are cardiomyocyte (**CL:0000746**), neuron (**CL:0000540**), skeletal muscle cell/myocyte, and fibroblast (**CL:0000057**). No COXPD23-specific single-cell, spatial-transcriptomic, patient-tissue proteomic, lipidomic, or integrated multi-omic dataset was identified for 2023–2024.

## 7. Anatomical structures affected

The primary organs are the **heart** (UBERON:0000948), **brain**, and skeletal muscle. Within the brain, recurrent sites are the dorsal thalamus, midbrain/brainstem, cerebellum/dentate nucleus, and corticospinal pathways. Cardiac disease is generally diffuse rather than lateralized; brain lesions are typically bilateral and symmetric. Secondary respiratory, nutritional, and systemic metabolic consequences can arise from heart failure, hypotonia, dysphagia, or acidosis. (yan2021novelmutationsin pages 7-8, zhang2023pathogenicityanalysisof pages 11-13)

At the cellular level, energy-demanding cardiomyocytes and neurons are the most clinically evident targets. At the subcellular level, the initiating compartment is the **mitochondrial matrix/mitochondrial RNA-translation apparatus** (GO:0005739, mitochondrion), followed by respiratory-chain dysfunction in the inner mitochondrial membrane (GO:0005743). No primary immune-cell target or inflammatory disease mechanism has been demonstrated.

## 8. Temporal development

The median onset is not reliably established; the 18-case synthesis reported a **mean of 1.7 years**. Homozygous cases began earlier on average than compound heterozygotes (0.3 versus 2.7 years), but this result is based on very small numbers. (zhang2023pathogenicityanalysisof pages 4-7)

A pragmatic—not validated—course classification is:

* **Severe neonatal/infantile form:** acute metabolic decompensation, marked lactate elevation, cardiac injury, arrhythmia/CHF, rapid deterioration, and death before one year.
* **Milder childhood form:** chronic hyperlactatemia with developmental encephalopathy, hypotonia/fatigability, seizures, visual abnormalities, and often cardiomyopathy; survival into the second decade or longer is possible.

One neonate died on day 4 despite intensive supportive care, whereas published patients were alive at ages 3, 10, and 17 years. Stable disease without meaningful improvement over 6–8 months was documented in two Chinese children. No formal stages, remission criteria, or validated critical therapeutic window exist, although early recognition of cardiac involvement is clinically important. (yan2021novelmutationsin pages 7-8, zhang2023pathogenicityanalysisof pages 11-13, yan2021novelmutationsin pages 2-4)

## 9. Inheritance and population

Inheritance is autosomal recessive. For two carrier parents, each conception has a theoretical 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele. Formal penetrance estimates are unavailable, but pathogenic biallelic genotypes appear highly penetrant. Expressivity is markedly variable. Anticipation is not expected; germline mosaicism has not been specifically documented but cannot be categorically excluded.

Disease-specific prevalence, incidence, carrier frequency, sex ratio, and mortality rate are unknown. Cases have been reported in Romanian, Turkish, Arab, Indian, Japanese, Chinese, and other families, with both sexes affected. Published case count is not a prevalence estimate. Consanguinity contributed to homozygous disease in some families, whereas the Chinese compound-heterozygous cases had unrelated parents. (zhang2023pathogenicityanalysisof pages 1-2, yan2021novelmutationsin pages 7-8)

## 10. Diagnostics

**Clinical suspicion.** Persistent or unexplained lactate elevation together with infantile/childhood cardiomyopathy and neurologic or developmental abnormalities should prompt evaluation for a mitochondrial translation disorder.

**Recommended testing sequence:**

1. Measure blood lactate/pyruvate, blood gas, glucose, ammonia, alanine and other amino acids, acylcarnitines, urine organic acids, CK/CK-MB, troponin where appropriate, BNP/NT-proBNP, liver/renal indices, and consider CSF lactate. These support mitochondrial dysfunction but are nonspecific.
2. Perform ECG, echocardiography and, when indicated, ambulatory rhythm monitoring; brain MRI with diffusion imaging and MR spectroscopy may identify Leigh-like lesions/lactate.
3. Use a comprehensive nuclear mitochondrial-disease/mitochondrial-cardiomyopathy panel containing **GTPBP3**, or preferably trio WES/WGS where phenotype is broad. Confirm variants and phase by Sanger or equivalent segregation testing and classify using current ACMG/AMP criteria. The 2023 case used trio WES plus proband WGS, CNV analysis, and mitochondrial-genome analysis. (zhang2023pathogenicityanalysisof pages 2-4, zhang2023pathogenicityanalysisof pages 11-13)
4. If sequencing is unresolved, RNA sequencing may reveal cryptic splice defects; muscle biopsy with respiratory-chain enzymology, histochemistry, blue-native PAGE, or mitochondrial translation assays can provide functional evidence. These are adjuncts rather than exclusion tests.

WGS can capture noncoding/splice variants, small CNVs, and alternative mtDNA diagnoses. CMA, karyotyping, FISH, repeat-expansion testing, and isolated mtDNA testing are not primary tests for confirmed GTPBP3 disease, although mtDNA analysis is relevant to the broader differential. Differential diagnoses include other mt-tRNA modification disorders (**MTO1/COXPD10, TRMU, TRMT10C, NSUN3**), mitochondrial translation defects, pyruvate-metabolism disorders, respiratory-chain assembly defects, mitochondrial cardiomyopathies, and genetically diverse Leigh/Leigh-like syndromes.

No population newborn screen exists. Targeted familial testing is suitable for carriers, siblings, prenatal diagnosis, and preimplantation testing once both familial pathogenic alleles are established.

## 11. Outcome and prognosis

No 5- or 10-year survival curve or life-expectancy estimate exists. Prognosis is dominated by age at onset and cardiac severity. Neonatal metabolic decompensation, arrhythmia, severe cardiomyopathy, and CHF indicate high early mortality; later-onset developmental disease may remain stable enough for survival into adolescence. Homozygosity and severe G-domain disruption are candidate risk markers, not validated prognostic biomarkers. (zhang2023pathogenicityanalysisof pages 9-10, zhang2023pathogenicityanalysisof pages 4-7)

Long-term morbidity includes intellectual and motor disability, impaired speech, hypotonia/weakness, gait instability, seizures, visual dysfunction, feeding limitations, and chronic cardiac disease. Recovery is uncommon in reported cases; two treated children showed no significant improvement over short follow-up. No disease-specific quality-of-life or disability-scale data are available. (yan2021novelmutationsin pages 2-4)

## 12. Treatment and current implementation

There is **no approved disease-modifying treatment** and no COXPD23-specific interventional trial was identified. Current implementation is supportive, multidisciplinary care:

* acute correction of acidosis, fluids and glucose tailored to metabolic status, respiratory support/mechanical ventilation, and intensive treatment of heart failure;
* cardiology surveillance and standard management of cardiomyopathy/arrhythmia, individualized to hemodynamics;
* antiseizure treatment chosen with mitochondrial safety considerations;
* nutrition and feeding support, avoidance of prolonged fasting, and physical, occupational, speech, and visual rehabilitation.

Reported “mitochondrial cocktail” components include thiamine, riboflavin, coenzyme Q10, L-carnitine, and vitamins C/E. In three Chinese patients these measures did not prevent neonatal death or produce significant improvement at 6–8 months. Consequently, their use is empiric, not evidence of efficacy. (yan2021novelmutationsin pages 2-4)

Suggested NCIT mappings include Supportive Care (**C15313**), Mechanical Ventilation (**C16210**), and Physical Therapy (**C15953**); drug and supplement concepts should be mapped individually. There is no established pharmacogenomic algorithm, surgery specific to COXPD23, cell therapy, RNA therapy, immunotherapy, or clinically available gene therapy.

As a post-2024 research note, a 2026 preclinical study reported variant knock-in mouse models and AAV-mediated GTPBP3 rescue in cells and animals. This is promising proof of concept but is outside the requested evidence window and is not a human treatment. (zhang2026molecularpathogenesisand pages 1-5, zhang2026molecularpathogenesisand pages 15-18)

## 13. Prevention

Because the initiating lesion is inherited, lifestyle modification cannot prevent disease in a child who has inherited pathogenic biallelic variants. Primary reproductive prevention consists of genetic counseling, parental and cascade carrier testing, preimplantation genetic testing, or prenatal molecular diagnosis for known familial variants. Secondary prevention means early molecular diagnosis and prospective cardiac, neurologic, nutritional, hearing/vision, and metabolic surveillance. Tertiary prevention focuses on avoiding fasting/dehydration, rapidly treating intercurrent illness and metabolic crises, controlling seizures and arrhythmias, and preserving nutrition and mobility. These surveillance measures are reasonable mitochondrial-care extrapolations; no COXPD23-specific trial has quantified benefit. Vaccination has no disease-specific preventive mechanism, although routine immunization may reduce infection-triggered metabolic stress.

## 14. Other species and natural disease

No naturally occurring veterinary GTPBP3 syndrome, affected breed, wildlife reservoir, zoonotic transmission, or cross-species infectious susceptibility was identified. GTPBP3 function is evolutionarily conserved from bacterial MnmE-like systems through vertebrates, supporting comparative mechanistic studies. Relevant laboratory taxa include *Danio rerio* (**NCBI Taxon 7955**) and, in newer work, *Mus musculus* (**Taxon 10090**). This is a genetic metabolic disorder and is not transmissible between species.

## 15. Model organisms and experimental systems

* **Patient fibroblasts:** demonstrate variably impaired mitochondrial translation and respiratory-chain activity; limitation—fibroblast biochemistry may be normal despite severe cardiac disease. (martinezzamora2015defectiveexpressionof pages 2-3)
* **Stable GTPBP3-silenced and knockout human cells:** reproduce loss of mt-tRNA modification, reduced OCR/ATP/membrane potential, complex-I deficiency, ROS, AMPK activation, metabolic rewiring, mitochondrial fragmentation, and autophagic flux. They are useful for pathway and rescue assays but do not reproduce organ-level development. (yan2021novelmutationsin pages 4-6, martinezzamora2015defectiveexpressionof pages 8-10)
* **gtpbp3-deficient zebrafish:** reported to develop hypertrophic cardiomyopathy with aberrant mitochondrial tRNA metabolism, supporting cardiac causality and offering an in-vivo developmental model. Species-specific physiology and allele dosage limit direct prognostic translation. (zhang2023pathogenicityanalysisof pages 13-15)
* **Yeast/comparative modopathy systems:** useful for testing conserved RNA-modification function and private variants, although mitochondrial genetic-code and substrate differences limit exact phenotypic equivalence. The 2023 review emphasizes that many disease alleles are private and therefore require functional model validation. (magistrati2023modopathiescausedby pages 11-12)
* **Emerging mouse models:** variant knock-in models and AAV rescue were reported after the requested 2023–2024 window; they should be treated as preclinical research rather than current application. (zhang2026molecularpathogenesisand pages 1-5)

## Recent developments and authoritative interpretation

The principal 2023 advance was quantitative synthesis of 18 patients and 35 clinical variants. Its abstract states: **“hyperlactatemia and cardiomyopathy were critical clinical features”** and reports average onset at 1.7 years. The study also identified enrichment of loss-of-function alleles and generated a tentative severe-versus-mild genotype–phenotype framework. Published February 2023; DOI: https://doi.org/10.3390/genes14030552. (zhang2023pathogenicityanalysisof pages 1-2, zhang2023pathogenicityanalysisof pages 4-7)

A 2023 mitochondrial-RNA-modopathy review summarized the original cohort as: all 11 patients had lactic acidosis, nine had cardiomyopathy, and six had neurologic manifestations; it also emphasized that mitochondrial RNA modifications are indispensable for efficient and accurate mitochondrial protein synthesis. Published January 2023; DOI: https://doi.org/10.3390/ijms24032178. (magistrati2023modopathiescausedby pages 11-12)

A 2024 report, **“Biallelic variants in GTPBP3: new patients, phenotypic spectrum, and outcome,”** appeared in *Annals of Clinical and Translational Neurology* (February 2024; DOI: https://doi.org/10.1002/acn3.51980). Full-text patient-level details were not retrievable in the present evidence set, so no unsupported frequencies or outcomes from that paper are asserted here.

The most defensible expert interpretation is that COXPD23 is a continuum rather than two truly discrete diseases. The “severe” and “mild” labels are useful for description but were derived retrospectively from a tiny, publication-biased cohort. Likewise, normal respiratory-chain testing in one tissue does not refute molecularly confirmed disease, and no individual variant should be called prognostic solely from its protein-domain location. (martinezzamora2015defectiveexpressionof pages 2-3, zhang2023pathogenicityanalysisof pages 11-13, zhang2023pathogenicityanalysisof pages 4-7)

### Principal references

1. Kopajtich R, et al. *Mutations in GTPBP3 cause a mitochondrial translation defect associated with hypertrophic cardiomyopathy, lactic acidosis, and encephalopathy.* **2014; PMID: 25434004**.
2. Yan H-M, et al. *Novel Mutations in the GTPBP3 Gene…* **July 2021**. DOI: https://doi.org/10.3389/fgene.2021.611226. The abstract states that the main features included **“lactic acidosis, myocardial damage, and neurologic symptoms.”** (yan2021novelmutationsin pages 1-2)
3. Zhang Q, et al. *Pathogenicity Analysis… and Systematic Literature Review.* **February 2023**. DOI: https://doi.org/10.3390/genes14030552. (zhang2023pathogenicityanalysisof pages 1-2)
4. Magistrati M, et al. *Modopathies Caused by Mutations in Genes Encoding for Mitochondrial RNA Modifying Enzymes.* **January 2023**. DOI: https://doi.org/10.3390/ijms24032178. (magistrati2023modopathiescausedby pages 11-12)
5. Nardecchia F, et al. *Biallelic variants in GTPBP3: new patients, phenotypic spectrum, and outcome.* **February 2024**. DOI: https://doi.org/10.1002/acn3.51980.

**Knowledge-base caution:** ontology terms above are suggested mappings, not assertions that every patient exhibits each phenotype. Quantitative frequencies should retain the denominator and publication-year metadata because the underlying sample is only 18 patients and is not population representative.

References

1. (zhang2023pathogenicityanalysisof pages 1-2): Qin Zhang, Qianqian Ouyang, Jingjing Xiang, Hong Li, Haitao Lv, and Yu An. Pathogenicity analysis of a novel variant in gtpbp3 causing mitochondrial disease and systematic literature review. Genes, 14:552, Feb 2023. URL: https://doi.org/10.3390/genes14030552, doi:10.3390/genes14030552. This article has 11 citations.

2. (zhang2023pathogenicityanalysisof pages 4-7): Qin Zhang, Qianqian Ouyang, Jingjing Xiang, Hong Li, Haitao Lv, and Yu An. Pathogenicity analysis of a novel variant in gtpbp3 causing mitochondrial disease and systematic literature review. Genes, 14:552, Feb 2023. URL: https://doi.org/10.3390/genes14030552, doi:10.3390/genes14030552. This article has 11 citations.

3. (OpenTargets Search: combined oxidative phosphorylation defect type 23): Open Targets Query (combined oxidative phosphorylation defect type 23, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (yan2021novelmutationsin pages 1-2): Hui-ming Yan, Zhi-mei Liu, Bei Cao, Victor Wei Zhang, Yi-duo He, Zheng-jun Jia, Hui Xi, Jing Liu, Fang Fang, and Hua Wang. Novel mutations in the gtpbp3 gene for mitochondrial disease and characteristics of related phenotypic spectrum: the first three cases from china. Frontiers in Genetics, Jul 2021. URL: https://doi.org/10.3389/fgene.2021.611226, doi:10.3389/fgene.2021.611226. This article has 20 citations and is from a peer-reviewed journal.

5. (magistrati2023modopathiescausedby pages 11-12): Martina Magistrati, Alexandru Ionut Gilea, Camilla Ceccatelli Berti, Enrico Baruffini, and Cristina Dallabona. Modopathies caused by mutations in genes encoding for mitochondrial rna modifying enzymes: molecular mechanisms and yeast disease models. International Journal of Molecular Sciences, 24:2178, Jan 2023. URL: https://doi.org/10.3390/ijms24032178, doi:10.3390/ijms24032178. This article has 15 citations.

6. (martinezzamora2015defectiveexpressionof pages 2-3): A Martinez-Zamora, S Meseguer, and JM Esteve. Defective expression of the mitochondrial-trna modifying enzyme gtpbp3 triggers ampk-mediated adaptive responses involving complex i assembly factors …. Unknown journal, 2015.

7. (yan2021novelmutationsin pages 2-4): Hui-ming Yan, Zhi-mei Liu, Bei Cao, Victor Wei Zhang, Yi-duo He, Zheng-jun Jia, Hui Xi, Jing Liu, Fang Fang, and Hua Wang. Novel mutations in the gtpbp3 gene for mitochondrial disease and characteristics of related phenotypic spectrum: the first three cases from china. Frontiers in Genetics, Jul 2021. URL: https://doi.org/10.3389/fgene.2021.611226, doi:10.3389/fgene.2021.611226. This article has 20 citations and is from a peer-reviewed journal.

8. (zhang2023pathogenicityanalysisof pages 2-4): Qin Zhang, Qianqian Ouyang, Jingjing Xiang, Hong Li, Haitao Lv, and Yu An. Pathogenicity analysis of a novel variant in gtpbp3 causing mitochondrial disease and systematic literature review. Genes, 14:552, Feb 2023. URL: https://doi.org/10.3390/genes14030552, doi:10.3390/genes14030552. This article has 11 citations.

9. (zhang2023pathogenicityanalysisof pages 10-11): Qin Zhang, Qianqian Ouyang, Jingjing Xiang, Hong Li, Haitao Lv, and Yu An. Pathogenicity analysis of a novel variant in gtpbp3 causing mitochondrial disease and systematic literature review. Genes, 14:552, Feb 2023. URL: https://doi.org/10.3390/genes14030552, doi:10.3390/genes14030552. This article has 11 citations.

10. (zhang2023pathogenicityanalysisof pages 9-10): Qin Zhang, Qianqian Ouyang, Jingjing Xiang, Hong Li, Haitao Lv, and Yu An. Pathogenicity analysis of a novel variant in gtpbp3 causing mitochondrial disease and systematic literature review. Genes, 14:552, Feb 2023. URL: https://doi.org/10.3390/genes14030552, doi:10.3390/genes14030552. This article has 11 citations.

11. (zhang2023pathogenicityanalysisof pages 11-13): Qin Zhang, Qianqian Ouyang, Jingjing Xiang, Hong Li, Haitao Lv, and Yu An. Pathogenicity analysis of a novel variant in gtpbp3 causing mitochondrial disease and systematic literature review. Genes, 14:552, Feb 2023. URL: https://doi.org/10.3390/genes14030552, doi:10.3390/genes14030552. This article has 11 citations.

12. (yan2021novelmutationsin pages 7-8): Hui-ming Yan, Zhi-mei Liu, Bei Cao, Victor Wei Zhang, Yi-duo He, Zheng-jun Jia, Hui Xi, Jing Liu, Fang Fang, and Hua Wang. Novel mutations in the gtpbp3 gene for mitochondrial disease and characteristics of related phenotypic spectrum: the first three cases from china. Frontiers in Genetics, Jul 2021. URL: https://doi.org/10.3389/fgene.2021.611226, doi:10.3389/fgene.2021.611226. This article has 20 citations and is from a peer-reviewed journal.

13. (zhang2023pathogenicityanalysisof pages 13-15): Qin Zhang, Qianqian Ouyang, Jingjing Xiang, Hong Li, Haitao Lv, and Yu An. Pathogenicity analysis of a novel variant in gtpbp3 causing mitochondrial disease and systematic literature review. Genes, 14:552, Feb 2023. URL: https://doi.org/10.3390/genes14030552, doi:10.3390/genes14030552. This article has 11 citations.

14. (yan2021novelmutationsin pages 4-6): Hui-ming Yan, Zhi-mei Liu, Bei Cao, Victor Wei Zhang, Yi-duo He, Zheng-jun Jia, Hui Xi, Jing Liu, Fang Fang, and Hua Wang. Novel mutations in the gtpbp3 gene for mitochondrial disease and characteristics of related phenotypic spectrum: the first three cases from china. Frontiers in Genetics, Jul 2021. URL: https://doi.org/10.3389/fgene.2021.611226, doi:10.3389/fgene.2021.611226. This article has 20 citations and is from a peer-reviewed journal.

15. (yan2021novelmutationsin pages 6-7): Hui-ming Yan, Zhi-mei Liu, Bei Cao, Victor Wei Zhang, Yi-duo He, Zheng-jun Jia, Hui Xi, Jing Liu, Fang Fang, and Hua Wang. Novel mutations in the gtpbp3 gene for mitochondrial disease and characteristics of related phenotypic spectrum: the first three cases from china. Frontiers in Genetics, Jul 2021. URL: https://doi.org/10.3389/fgene.2021.611226, doi:10.3389/fgene.2021.611226. This article has 20 citations and is from a peer-reviewed journal.

16. (martinezzamora2015defectiveexpressionof pages 8-10): A Martinez-Zamora, S Meseguer, and JM Esteve. Defective expression of the mitochondrial-trna modifying enzyme gtpbp3 triggers ampk-mediated adaptive responses involving complex i assembly factors …. Unknown journal, 2015.

17. (obyrne2018thegenotypicand pages 16-18): James J. O'Byrne, Maja Tarailo-Graovac, Aisha Ghani, Michael Champion, Charu Deshpande, Ali Dursun, Riza K. Ozgul, Peter Freisinger, Ian Garber, Tobias B. Haack, Rita Horvath, Ivo Barić, Ralf A. Husain, Leo A.J. Kluijtmans, Urania Kotzaeridou, Andrew A. Morris, Colin J. Ross, Saikat Santra, Jan Smeitink, Mark Tarnopolsky, Saskia B. Wortmann, Johannes A. Mayr, Michaela Brunner-Krainz, Holger Prokisch, Wyeth W. Wasserman, Ron A. Wevers, Udo F. Engelke, Richard J. Rodenburg, Teck Wah Ting, Robert McFarland, Robert W. Taylor, Ramona Salvarinova, and Clara D.M. van Karnebeek. The genotypic and phenotypic spectrum of mto1 deficiency. Molecular Genetics and Metabolism, 123:28-42, Jan 2018. URL: https://doi.org/10.1016/j.ymgme.2017.11.003, doi:10.1016/j.ymgme.2017.11.003. This article has 41 citations and is from a peer-reviewed journal.

18. (zhang2023pathogenicityanalysisof pages 7-8): Qin Zhang, Qianqian Ouyang, Jingjing Xiang, Hong Li, Haitao Lv, and Yu An. Pathogenicity analysis of a novel variant in gtpbp3 causing mitochondrial disease and systematic literature review. Genes, 14:552, Feb 2023. URL: https://doi.org/10.3390/genes14030552, doi:10.3390/genes14030552. This article has 11 citations.

19. (zhang2026molecularpathogenesisand pages 1-5): Yong Zhang, Shi-Ying Yao, Jing Li, Tingting Yu, Hao Liu, Nanlin Zhu, Gui-Xin Peng, Wen-Qiang Zheng, Chun-Rui Ma, En-Duo Wang, Cui Song, and Xiao-Long Zhou. Molecular pathogenesis and gene therapy-based intervention of gtpbp3-related mitochondrial disease. Nature Communications, Apr 2026. URL: https://doi.org/10.1038/s41467-026-71750-z, doi:10.1038/s41467-026-71750-z. This article has 2 citations and is from a highest quality peer-reviewed journal.

20. (zhang2026molecularpathogenesisand pages 15-18): Yong Zhang, Shi-Ying Yao, Jing Li, Tingting Yu, Hao Liu, Nanlin Zhu, Gui-Xin Peng, Wen-Qiang Zheng, Chun-Rui Ma, En-Duo Wang, Cui Song, and Xiao-Long Zhou. Molecular pathogenesis and gene therapy-based intervention of gtpbp3-related mitochondrial disease. Nature Communications, Apr 2026. URL: https://doi.org/10.1038/s41467-026-71750-z, doi:10.1038/s41467-026-71750-z. This article has 2 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Combined_Oxidative_Phosphorylation_Defect_Type_23-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014525` (3 mentions) - the report calls it "if available"; MONDO calls it **combined oxidative phosphorylation defect type 23**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001639` (3 mentions) - the report calls it "Cardiac:** hypertrophic cardiomyopathy/left- or biventricular hypertrophy"; HP calls it **Hypertrophic cardiomyopathy**
- `HP:0001263` (3 mentions) - the report calls it "Neurologic/developmental:** global developmental delay"; HP calls it **Global developmental delay**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MIM`.