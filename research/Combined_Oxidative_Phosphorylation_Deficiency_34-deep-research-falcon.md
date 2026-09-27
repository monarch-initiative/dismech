---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-09T11:06:19.785585'
end_time: '2026-09-09T11:25:52.972243'
duration_seconds: 1173.19
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Combined Oxidative Phosphorylation Deficiency 34
  mondo_id: MONDO:0054741
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
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 43
  verified: 43
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0054741
    reported_labels:
    - if available
    ontology_label: combined oxidative phosphorylation deficiency 34
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Combined_Oxidative_Phosphorylation_Deficiency_34-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Deficiency 34
- **MONDO ID:** MONDO:0054741 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Deficiency 34** covering all of the
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
- **Disease Name:** Combined Oxidative Phosphorylation Deficiency 34
- **MONDO ID:** MONDO:0054741 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Deficiency 34** covering all of the
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


# Combined Oxidative Phosphorylation Deficiency 34: research report

## Executive summary

Combined oxidative phosphorylation deficiency 34 (COXPD34) is an ultra-rare, autosomal-recessive nuclear mitochondrial translation disorder caused by biallelic **MRPS7** variants. MRPS7/uS7m is a component of the mitochondrial 28S small ribosomal subunit that binds mitochondrial 12S rRNA. Defective MRPS7 destabilizes the small subunit, impairs translation of mtDNA-encoded oxidative-phosphorylation proteins, and produces combined respiratory-chain deficiency. The best-established manifestations are congenital or childhood sensorineural hearing loss, lactic acidemia, hypoglycemia, progressive hepatic and renal dysfunction, and—in females surviving to reproductive age—premature ovarian insufficiency (POI)/Perrault-spectrum disease. Evidence remains exceptionally limited: four clinically affected females from two unrelated families have been described, only three of whom were molecularly documented in the cited reports. Consequently, prevalence, penetrance, robust phenotype frequencies, survival rates, and genotype–phenotype relationships are unknown. (kline2022integralroleof pages 2-4, menezes2015mutationinmitochondrial pages 2-3, menezes2015mutationinmitochondrial pages 1-2)

The foundational primary report was published online **2 January 2015**: Menezes et al., *Human Molecular Genetics* 24:2297–2307, PMID **25556185**, DOI/URL: https://doi.org/10.1093/hmg/ddu747. Its abstract states: “Pulse labeling of mitochondrial protein synthesis products revealed impaired mitochondrial protein synthesis in patient fibroblasts,” and wild-type MRPS7 rescued respiratory-chain activity and 12S-rRNA abundance. (menezes2015mutationinmitochondrial pages 1-2)

An independent report published **14 November 2022** expanded the phenotype to syndromic POI/Perrault syndrome: Kline et al., *Genes* 13:2113, DOI/URL: https://doi.org/10.3390/genes13112113. Its abstract states: “This second independent report validates that variants in MRPS7 are a cause of syndromic POI/Perrault syndrome.” (kline2022integralroleof pages 1-2)

| Evidence unit / publication | Genotype | Patient count | Core phenotype and onset | Key biochemical / pathology evidence | Outcome / treatment | Evidence type and limitations |
|---|---|---:|---|---|---|---|
| Menezes et al., *Human Molecular Genetics* (published January 2, 2015); PMID: 25556185; DOI: [10.1093/hmg/ddu747](https://doi.org/10.1093/hmg/ddu747) | Homozygous **MRPS7** c.550A>G, p.(Met184Val), rs115047866; affected sisters homozygous, parents and unaffected sister heterozygous | 2 affected sisters | Both had profound congenital bilateral sensorineural deafness and childhood lactic acidemia. P1 developed recurrent emesis and failure to thrive in infancy, hypoglycemia <0.5 mmol/L and lactate 4.1 mmol/L at 13 months, then progressive hepatic and renal failure. P2 had intermittent childhood hyperlactatemia/hypoglycemia, mild learning difficulties, failed puberty, primary hypogonadism at 16 years, mildly elevated TSH (6.75 mIU/L), and primary adrenal failure. | Liver respiratory-chain activities were deficient in complexes I, III, and IV: P1/P2 complex I 7/6 (reference 10–21), complex III 7.4/4.5 (9–14), and complex IV 0.2/1.1 (1.1–1.6) nmol/min/mg or /min/mg as reported. P1 muscle complex III was 11.6 (14–67); other muscle activities were largely preserved. P2 renal biopsy at 13 years showed tubular atrophy/dilatation and giant mitochondria up to 5.5 μm versus normal 0.5–1.0 μm, with increased matrix and reduced cristae. P1 fibroblasts showed near-absent MRPS7, reduced 12S rRNA, impaired mitochondrial translation, reduced OXPHOS proteins, complexes I/IV dysfunction, mitochondrial-network fragmentation, and significantly reduced ATP production (P<0.003). Wild-type—but not mutant—MRPS7 restored 12S rRNA and respiratory-chain activity. | P1 received resuscitation, antibiotics, nutritional support, ventilation, and hemofiltration; a left parieto-occipital infarct precluded transplantation, and she died at 14 years 5 months after intensive support was withdrawn. P2 received cochlear implantation, estrogen replacement, and low-dose hydrocortisone; later follow-up reported combined liver–renal transplantation at 25 years with a positive outcome. | Human familial case series plus patient-fibroblast rescue experiments; strongest direct causal evidence. Only one family, no controlled treatment data, ancestry not specified, and marked intrafamilial variability limit frequency and prognostic inference. Historical allele estimates were heterozygosity 0.002 in dbSNP and 0.67% in an in-house CAG dataset, not current gnomAD frequencies. (menezes2015mutationinmitochondrial pages 1-2, menezes2015mutationinmitochondrial pages 2-3, menezes2015mutationinmitochondrial pages 3-4, menezes2015mutationinmitochondrial pages 6-7) |
| Kline et al., *Genes* (published November 14, 2022); DOI: [10.3390/genes13112113](https://doi.org/10.3390/genes13112113) — proband | Compound heterozygous **MRPS7** c.373A>T, p.(Lys125*) and c.536G>A, p.(Arg179His), demonstrated in trans; both classified likely pathogenic by the authors | 1 molecularly characterized proband | Sensorineural hearing loss diagnosed at 9 years; normal puberty followed by secondary amenorrhea and premature ovarian insufficiency diagnosed at 25 years; Hashimoto disease. FSH 102 IU/L, LH 34 IU/L, estradiol 29 pg/mL, AMH 0.15 ng/mL, TSH 12.89 mIU/L, and anti-TPO 102 IU/mL. | Ultrasound at 25 years showed small ovaries: right 18×4.5 mm with two microfollicles and left 14×6 mm without visible follicles. Karyotype/microarray showed 46,XX; FMR1-premutation and ovarian-autoantibody testing were negative. p.(Lys125*) was predicted to undergo nonsense-mediated decay; structural modeling predicted p.(Arg179His) would disrupt interactions with Glu153 and Asp176. No patient-cell functional assay was reported. | Hashimoto disease was described as well managed. Bone mineral density was not osteoporotic. No disease-modifying therapy or treatment-response data were reported; the authors highlighted potential benefits of early hormone replacement or oocyte collection for mitochondrial-disease-associated POI generally. | Human single-case report with WES, Sanger validation, phasing, clinical endocrine testing, and computational modeling. Independent allelic replication supports causality, but lack of functional validation, parental DNA, longitudinal outcome, and disease-specific treatment evidence limits interpretation. (kline2022integralroleof pages 4-5, kline2022integralroleof pages 5-8, kline2022integralroleof pages 1-2, kline2022integralroleof pages 8-9) |
| Kline et al. (2022) — clinically affected sister of the new proband | Presumed familial MRPS7-related disease; sister’s genotype was not reported | 1 clinically affected sister | Congenital hearing loss and POI diagnosed at 21 years | No biochemical, imaging, histopathologic, or functional data reported | Treatment and outcome not reported | Human phenotype-only familial evidence; cannot independently confirm genotype, mechanism, or biochemical COXPD34. (kline2022integralroleof pages 4-5, kline2022integralroleof pages 5-8) |
| Combined published human evidence through 2022 | Three reported disease-associated alleles: c.550A>G p.(Met184Val), c.373A>T p.(Lys125*), and c.536G>A p.(Arg179His) | 4 clinically affected females across 2 unrelated families; 3 molecularly documented in the cited reports | Sensorineural hearing loss occurred in all 4 reported individuals; ovarian insufficiency/hypogonadism was documented in the 3 who survived to an assessable reproductive age. Severe progressive hepatorenal disease was documented in the original sisters; biochemical combined OXPHOS deficiency was demonstrated only in that family. | Direct functional evidence is confined to p.(Met184Val) patient fibroblasts. The nearby p.(Arg179His) and p.(Met184Val) residues lie within the predicted ribosomal-protein S7 domain (codons 82–234), which interacts with 12S rRNA. | No curative or genotype-specific therapy and no controlled treatment response have been reported. Organ transplantation and endocrine, adrenal, auditory, nutritional, renal, and intensive supportive interventions were used in individual patients. | Ultra-small, ascertainment-biased literature; percentages are descriptive rather than population estimates. Penetrance, prevalence, incidence, carrier frequency, sex ratio, survival rates, and robust genotype–phenotype correlations remain unknown. (kline2022integralroleof pages 2-4, kline2022integralroleof pages 9-10) |


*Table: Disease-specific clinical, genetic, biochemical, and functional evidence for MRPS7-related combined oxidative phosphorylation deficiency 34. The table highlights the very small evidence base, exact reported measurements, outcomes, and major limitations.*

## 1. Disease information

### Definition and identifiers

COXPD34 is a Mendelian mitochondrial disorder in which defective mitochondrial protein synthesis causes deficiency of multiple OXPHOS complexes rather than an isolated respiratory-complex defect.

- **MONDO:** MONDO:0054741.
- **OMIM phenotype:** **617872**, Combined oxidative phosphorylation deficiency 34.
- **Causal gene:** **MRPS7**, mitochondrial ribosomal protein S7; OMIM gene **611974**; Ensembl target ENSG00000125445.
- **Common names/synonyms:** combined oxidative phosphorylation deficiency 34; COXPD34; MRPS7-related mitochondrial disease; MRPS7 deficiency. Phenotypic labels include MRPS7-related syndromic POI, MRPS7-related Perrault syndrome, and congenital sensorineural deafness with progressive hepatic/renal failure and lactic acidemia.
- **Orphanet, MeSH, ICD-10/ICD-11:** no disease-specific identifiers were established in the retrieved evidence. In clinical coding, broader mitochondrial-metabolism, hearing-loss, renal, hepatic, and ovarian-insufficiency codes may be needed; these are not equivalent to a dedicated COXPD34 code.

Open Targets associates MONDO:0054741 with MRPS7 and cites PMID 25556185. This is consistent with the primary literature and corrects a potential nomenclature pitfall: **COXPD34 is MRPS7-related, not GATB-related**. (OpenTargets Search: Combined oxidative phosphorylation deficiency 34, webb2020mitochondrialtranslationdefects pages 12-13)

### Evidence provenance

The disease definition is aggregated at the disease-resource level, but virtually all phenotype and natural-history knowledge comes from individual patients in two published families rather than registries, EHR-scale cohorts, or epidemiologic studies. The original family contributed two affected sisters; the second report described one molecularly characterized woman and one similarly affected sister whose genotype was not reported. (kline2022integralroleof pages 2-4, kline2022integralroleof pages 5-8)

## 2. Etiology

### Causal factor

The primary cause is **germline biallelic MRPS7 dysfunction**, inherited autosomal recessively. MRPS7 encodes uS7m, a nuclear-encoded structural protein of the mitochondrial small ribosomal subunit. No infectious, toxic, lifestyle, or environmental primary cause is established. (webb2020mitochondrialtranslationdefects pages 12-13, menezes2015mutationinmitochondrial pages 1-2)

### Genetic risk factors

Three disease-associated alleles are reported:

1. **c.550A>G, p.(Met184Val), rs115047866**, homozygous in the original affected sisters and heterozygous in both parents and an unaffected sister. The 2015 paper classified it as pathogenic after segregation, biochemical studies, protein modeling, and wild-type rescue. Historical databases reported dbSNP heterozygosity 0.002 and an in-house CAG frequency of 0.67%; these are not substitutes for a current ancestry-stratified gnomAD frequency. (menezes2015mutationinmitochondrial pages 2-3, menezes2015mutationinmitochondrial pages 3-4)
2. **c.373A>T, p.(Lys125*)**, a nonsense allele classified likely pathogenic in the 2022 report. It lies in exon 4 of 5 and was predicted to trigger nonsense-mediated decay, producing loss of function. (kline2022integralroleof pages 5-8, kline2022integralroleof pages 8-9)
3. **c.536G>A, p.(Arg179His)**, a missense allele classified likely pathogenic in the 2022 report. Modeling predicted loss of salt-bridge/hydrogen-bond interactions involving Glu153 and Asp176. The two variants were experimentally phased in trans. (kline2022integralroleof pages 8-9)

The 2022 filtering pipeline considered alleles with MAF below 0.005 in 1000 Genomes and gnomAD, but exact current population frequencies for its two variants were not given in the retrieved text. Both p.Arg179His and p.Met184Val lie within the predicted S7 domain (codons 82–234). (kline2022integralroleof pages 4-5, kline2022integralroleof pages 9-10)

### Environmental risk, protective factors, and gene–environment interaction

No validated environmental risk or protective factor is known. In the severe original patient, acute febrile illness/presumed bacterial peritonitis preceded terminal hepatorenal decompensation. The authors considered—but did not demonstrate—that antibiotics could have interfered with mitochondrial translation; they instead emphasized unsupervised disease progression and unknown genetic/environmental modifiers. This is hypothesis-level evidence, not an established gene–environment interaction. Gentamicin exposure deserves caution because aminoglycosides can be ototoxic and inhibit bacterial-like mitochondrial translation, but no MRPS7-specific sensitivity has been demonstrated. (menezes2015mutationinmitochondrial pages 2-3, menezes2015mutationinmitochondrial pages 6-7)

No protective MRPS7 alleles, modifier genes, diet, supplements, exercise program, or avoidance strategy has been shown to alter penetrance or progression.

## 3. Phenotypes

Because only four clinically affected females are known, frequencies below are **descriptive fractions of published cases, not population estimates**.

- **Sensorineural hearing loss:** 4/4 reported individuals; congenital and profound in the original sisters and the second proband’s sister, diagnosed at age 9 in the second proband. Severity ranged from childhood-onset to profound congenital bilateral deafness. Suggested HPO: **Sensorineural hearing impairment (HP:0000407)**; **Congenital sensorineural hearing impairment (HP:0008527)**; bilateral/profound qualifiers where appropriate. Cochlear implantation produced satisfactory speech acquisition in the original family. (kline2022integralroleof pages 5-8, menezes2015mutationinmitochondrial pages 2-2, menezes2015mutationinmitochondrial pages 3-4)
- **Lactic acidemia/hyperlactatemia:** reported in both original sisters; one documented level was 4.1 mmol/L at 13 months. It was intermittent and later mostly normal in the milder sister. Suggested HPO: **Lactic acidosis (HP:0003128)**; **Increased circulating lactate concentration (HP:0002151)**. (menezes2015mutationinmitochondrial pages 2-2, menezes2015mutationinmitochondrial pages 3-4)
- **Hypoglycemia:** documented in both original sisters during childhood; one severe episode was below 0.5 mmol/L. It later resolved spontaneously in the milder sister. Suggested HPO: **Hypoglycemia (HP:0001943)**; episodic qualifier. (menezes2015mutationinmitochondrial pages 2-2, menezes2015mutationinmitochondrial pages 3-4)
- **Hepatic disease:** both original sisters had liver pathology/biochemical deficiency and progressive hepatic dysfunction; one developed terminal liver failure and the other later underwent liver transplantation. Histology included hepatocyte swelling, mild steatosis, mild portal/Disse-space expansion, and grade 1–2 iron accumulation. Suggested HPO: **Hepatic failure (HP:0001399)**, **Hepatomegaly (HP:0002240)**, **Hepatic steatosis (HP:0001397)**, abnormal liver morphology. (menezes2015mutationinmitochondrial pages 2-2, menezes2015mutationinmitochondrial pages 2-3)
- **Renal disease:** progressive renal dysfunction affected both original sisters. Biopsy showed tubular atrophy/dilatation, protein casts, and giant mitochondria up to 5.5 μm. Suggested HPO: **Renal insufficiency (HP:0000083)**, **Renal tubular atrophy (HP:0000092)**, abnormal renal-tubule morphology. (menezes2015mutationinmitochondrial pages 2-3)
- **POI/hypogonadism:** present in all three females who survived long enough for reproductive assessment. Presentations included failed puberty/primary hypogonadism and primary amenorrhea, or normal puberty followed by secondary amenorrhea and POI at ages 21–25. Suggested HPO: **Primary ovarian insufficiency (HP:0008209)**, **Primary amenorrhea (HP:0000786)**, **Secondary amenorrhea (HP:0000869)**, **Delayed puberty (HP:0000823)**, **Hypergonadotropic hypogonadism (HP:0000830)**. (kline2022integralroleof pages 5-8, kline2022integralroleof pages 9-10)
- **Endocrine abnormalities:** primary adrenal failure was diagnosed in one original sister by short Synacthen testing; mild TSH elevation occurred in that patient. The 2022 proband had Hashimoto disease, TSH 12.89 mIU/L, and anti-TPO 102 IU/mL. Whether autoimmune thyroid disease is integral to MRPS7 deficiency is unresolved. Suggested HPO: **Primary adrenal insufficiency (HP:0008207)**, **Hypothyroidism (HP:0000821)**, **Elevated serum TSH (HP:0002925)**. (kline2022integralroleof pages 5-8, menezes2015mutationinmitochondrial pages 3-4)
- **Growth/neurodevelopment:** recurrent emesis and failure to thrive occurred in the severe original patient. Her motor/cognitive development remained normal at 4.5 years. The milder sister had mild learning difficulties; encephalopathy occurred secondary to organ failure rather than as a proven primary neurodegenerative phenotype. Suggested HPO: **Failure to thrive (HP:0001508)**, **Recurrent vomiting (HP:0002013)**, **Mild intellectual disability/learning disability** as clinically appropriate, **Encephalopathy (HP:0001298)** with secondary-cause annotation. (menezes2015mutationinmitochondrial pages 2-2, menezes2015mutationinmitochondrial pages 2-3, menezes2015mutationinmitochondrial pages 3-4)
- **Laboratory/pathologic OXPHOS phenotype:** combined complexes I, III, and IV deficiency in liver and reduced complexes I/IV in fibroblasts; ATP production was significantly reduced (P<0.003). Suggested HPO: **Abnormality of mitochondrial metabolism (HP:0012103)** and **Combined oxidative phosphorylation defect** where locally available. (menezes2015mutationinmitochondrial pages 2-3, menezes2015mutationinmitochondrial pages 6-7)

### Functional and quality-of-life burden

Profound hearing loss affects communication and education; cochlear implantation improved speech acquisition. Ovarian insufficiency causes infertility and requires endocrine/fertility counseling. Hepatorenal failure led to dialysis-level support, transplantation, encephalopathy, prolonged intensive care, and death in one patient. No EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life instrument has been reported. (menezes2015mutationinmitochondrial pages 2-2, menezes2015mutationinmitochondrial pages 2-3, menezes2015mutationinmitochondrial pages 3-4)

## 4. Genetic and molecular information

- **Gene:** MRPS7; OMIM 611974; protein uS7m/MRPS7; UniProt **Q9Y2R9**. It is a nuclear gene; variants are constitutional/germline, not somatic. (menezes2015mutationinmitochondrial pages 7-8)
- **Variant classes:** one nonsense predicted loss-of-function allele and two missense alleles predicted or demonstrated to destabilize protein/small-subunit function.
- **Functional consequence:** predominantly **loss of function**. p.Met184Val caused near-total absence of MRPS7 protein in fibroblasts, reduced 12S rRNA, defective mitochondrial translation, and reduced respiratory-chain activity. Wild-type—but not mutant—complementation rescued molecular and biochemical abnormalities, arguing against gain of function or dominant-negative action. (menezes2015mutationinmitochondrial pages 3-4, menezes2015mutationinmitochondrial pages 6-7)
- **Chromosomal abnormalities:** none causal. The original affected sisters shared an approximately 1-Mb run of homozygosity at 17q25.1, possibly reflecting remote shared ancestry, although the parents reported no consanguinity. The 2022 proband had a normal 46,XX complement by karyotype/microarray. (menezes2015mutationinmitochondrial pages 3-4, kline2022integralroleof pages 4-5)
- **Modifier genes:** none identified. Intrafamilial severity variability implies possible modifiers but provides no specific locus.
- **Epigenetics:** no disease-specific DNA-methylation, chromatin, or histone-modification signature is reported.

ClinVar submissions for the 2022 alleles were reported as **SCV002574697–SCV002574698**. (kline2022integralroleof pages 10-12)

## 5. Environmental information

No toxin, radiation, pollution, occupation, smoking, alcohol, diet, exercise pattern, or infectious agent causes COXPD34. Intercurrent infection/metabolic stress may plausibly precipitate decompensation, as in other mitochondrial disorders, but only a single acute terminal episode is documented here. No zoonotic or transmissible component exists. The appropriate knowledge-base representation is therefore “not established/not applicable,” rather than absence being interpreted as proof of no effect. (menezes2015mutationinmitochondrial pages 2-3, kline2022integralroleof pages 2-4)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic germline MRPS7 pathogenic variants lead to reduced abundance or structural instability of uS7m**; near-total protein loss was demonstrated for p.Met184Val, while p.Lys125* loss and p.Arg179His destabilization are predicted. (kline2022integralroleof pages 8-9, menezes2015mutationinmitochondrial pages 6-7)
2. **Defective uS7m leads to unstable assembly of the mitochondrial 28S small subunit and defective binding/incorporation of 12S rRNA.** MRPS7’s S7 domain interacts with the 3′ head of 12S rRNA; reduced 12S but preserved 16S rRNA was demonstrated in patient fibroblasts. (kline2022integralroleof pages 9-10, menezes2015mutationinmitochondrial pages 3-4)
3. **Small-subunit instability leads to 12S-rRNA degradation and impaired mitochondrial translation.** Pulse-labeling and reduced MT-CO1/MT-CO2 demonstrated reduced synthesis/abundance of mtDNA-encoded products. (menezes2015mutationinmitochondrial pages 1-2, menezes2015mutationinmitochondrial pages 6-7)
4. **Deficient synthesis of mtDNA-encoded subunits leads to defective assembly/activity of multiple OXPHOS complexes**, principally I, III, and IV. Complex II is nuclear encoded and comparatively preserved. (menezes2015mutationinmitochondrial pages 2-3, menezes2015mutationinmitochondrial pages 6-7)
5. **Combined OXPHOS dysfunction leads to reduced ATP generation, compensatory mitochondrial proliferation/network fragmentation, and lactate accumulation.** Reduced ATP production and fragmented fibroblast mitochondrial networks were demonstrated; tissue-energy failure is the downstream interpretation. (menezes2015mutationinmitochondrial pages 3-4, menezes2015mutationinmitochondrial pages 6-7)
6. **Energy failure in high-demand tissues leads to cochlear dysfunction, hepatocellular injury, renal tubular mitochondrial enlargement/dysfunction, episodic hypoglycemia, and systemic lactic acidemia.** The organ-specific link is strongly supported clinically and biochemically, although exact tissue-selectivity mechanisms remain unresolved. (menezes2015mutationinmitochondrial pages 2-2, menezes2015mutationinmitochondrial pages 2-3)
7. **Branch A—ovary:** mitochondrial translation/OXPHOS insufficiency is inferred to reduce oocyte/granulosa-cell energy support and increase oxidative stress, leading to follicular atresia, depletion of viable oocytes, and POI. This branch is biologically plausible and supported by the reproductive phenotype, but it was not directly tested in MRPS7 patient ovarian tissue. (kline2022integralroleof pages 9-10)
8. **Branch B—advanced organ failure:** progressive hepatic and renal dysfunction leads to metabolic encephalopathy and critical illness; in one patient a cerebral infarct during decompensation precluded transplantation and preceded death. (menezes2015mutationinmitochondrial pages 2-3)

### Pathways and processes

The primary pathway is mitochondrial gene expression/translation feeding OXPHOS, not canonical Wnt, MAPK, PI3K–AKT, or mTOR signaling. Relevant GO suggestions include **mitochondrial translation (GO:0032543)**, **mitochondrial ribosome assembly (GO:0061668)**, **mitochondrial respiratory-chain complex assembly (GO:0033108)**, **oxidative phosphorylation (GO:0006119)**, **ATP metabolic process (GO:0046034)**, and **cellular response to oxidative stress (GO:0034599)**. The 2024 review emphasizes that mtDNA encodes 13 OXPHOS subunits and that mitochondrial-translation disorders are frequently multisystemic because high-energy-demand tissues are vulnerable. (antolinezfernandez2024molecularpathwaysin pages 1-2)

Relevant cellular compartments are **mitochondrial matrix (GO:0005759)**, **mitochondrial small ribosomal subunit (GO:0005763)**, **mitochondrial ribosome (GO:0005761)**, **mitochondrial inner membrane (GO:0005743)**, and respiratory-chain complexes I/III/IV.

Suggested cell ontology targets include **renal tubular epithelial cell**, **hepatocyte (CL:0000182)**, **cochlear hair cell**, **oocyte (CL:0000023)**, **ovarian granulosa cell (CL:0000501)**, and fibroblast for the experimental model. Exact CL identifiers should be validated against the current ontology release before database ingestion.

### Molecular profiling and advanced technologies

Disease-specific profiling is limited to targeted immunoblotting, qPCR, radiolabeled translation assays, enzymology, ATP measurement, and mitochondrial imaging in fibroblasts. There is no COXPD34-specific bulk transcriptome, unbiased proteome, metabolome, lipidome, single-cell, spatial-transcriptomic, or multi-omic dataset. Recent 2024 work in broader mitochondrial cohorts showed that fibroblast mass-spectrometry proteomics can classify biochemical/genetic groups and aid VUS interpretation, but this is an emerging diagnostic application, not validated specifically for MRPS7. Likewise, a 2024 French cohort found 397 molecularly confirmed cases across 172 genes and supported WES/WGS over panels for possible mitochondrial disease; MRPS7-specific performance was not provided. (rouzier2024primarymitochondrialdisorders pages 1-2, rouzier2024primarymitochondrialdisorders pages 8-11)

## 7. Anatomical structures affected

- **Primary organs:** inner ear/cochlea; liver; kidney, particularly renal tubules; ovary.
- **Secondary/variable systems:** adrenal and thyroid endocrine axes; central nervous system during metabolic/organ failure; gastrointestinal/nutritional system through recurrent emesis and failure to thrive.
- **Tissues/cells:** cochlear sensory epithelium/hair cells, hepatocytes, renal tubular epithelial cells, ovarian follicles/oocytes/granulosa cells. Direct disease histology exists for liver, muscle, and kidney; ovarian and cochlear cellular mechanisms are inferred.
- **Subcellular:** mitochondrial matrix, 28S small mitoribosomal subunit, 12S rRNA, inner-membrane OXPHOS machinery.

Suggested UBERON terms include **cochlea (UBERON:0001844)**, **liver (UBERON:0002107)**, **kidney (UBERON:0002113)**, **renal tubule (UBERON:0001231)**, **ovary (UBERON:0000992)**, **adrenal gland (UBERON:0002369)**, and **brain (UBERON:0000955)**. Hearing loss was bilateral; no consistent lateralized organ disease is known. (menezes2015mutationinmitochondrial pages 2-2, menezes2015mutationinmitochondrial pages 2-3)

## 8. Temporal development

COXPD34 spans a congenital-to-adult continuum:

- **Congenital/infantile phase:** congenital deafness; infancy-onset vomiting, failure to thrive, hypoglycemia, and lactic acidemia in severe disease.
- **Childhood phase:** hearing impairment, intermittent metabolic abnormalities, mild learning difficulty in one patient, and emerging liver/renal dysfunction.
- **Adolescent phase:** potentially rapid decompensation with hepatorenal failure; one death occurred at 14 years 5 months. Failed puberty/primary hypogonadism was diagnosed at 16 in another patient.
- **Young-adult phase:** progressive organ dysfunction may culminate in combined liver–kidney transplantation; milder patients may present with POI at ages 21–25 after congenital/childhood hearing loss. (kline2022integralroleof pages 5-8, kline2022integralroleof pages 9-10, menezes2015mutationinmitochondrial pages 2-3, menezes2015mutationinmitochondrial pages 3-4)

The course is chronic and variably progressive, with episodic metabolic crises. Spontaneous biochemical improvement is possible—childhood hypoglycemia resolved and lactate often normalized in one patient—but this is not remission of the underlying genetic disorder. Critical periods include infancy during metabolic stress, adolescence during organ decline, and pre-/peripuberty for endocrine surveillance and fertility preservation. No validated staging system exists.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. In the original family, both affected sisters were homozygous and both parents plus an unaffected sister were heterozygous. The second proband’s two variants were confirmed in trans, although parental DNA was unavailable. (menezes2015mutationinmitochondrial pages 2-3, kline2022integralroleof pages 8-9)

For two carrier parents, standard Mendelian counseling gives a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability per pregnancy, assuming both parental variants and phase are confirmed. Penetrance among biallelic individuals cannot be estimated. Expressivity is clearly variable—even within one family—but anticipation, germline mosaicism, and founder effects are unreported. A shared 17q25.1 homozygous segment raises possible remote common ancestry for the original parents; there was no acknowledged consanguinity. (menezes2015mutationinmitochondrial pages 3-4)

Disease-specific prevalence, incidence, carrier frequency, sex ratio, ethnic enrichment, and geographic distribution are unknown. All reported affected individuals were female, but this reflects an extremely small sample and ascertainment through POI; it cannot establish female predominance. For context only, a 2024 French study cites primary mitochondrial disease prevalence of at least 20 per 100,000 and estimated lifetime risk of 48.4 per 100,000 for 249 recessive mitochondrial disorders combined; these figures must not be assigned to COXPD34. (rouzier2024primarymitochondrialdisorders pages 1-2)

## 10. Diagnostics

### Recommended approach

1. **Clinical suspicion:** bilateral sensorineural hearing loss plus unexplained lactic acidemia, hypoglycemia, liver/renal dysfunction, or female POI/failed puberty should prompt consideration of MRPS7 disease.
2. **Baseline laboratory assessment:** plasma lactate, glucose, blood gas, liver enzymes/synthetic function, renal function/electrolytes, urinalysis; consider plasma amino acids, acylcarnitines, urine organic acids, and endocrine testing. These tests support mitochondrial disease but are not specific.
3. **System surveillance:** audiology; abdominal ultrasound; renal and hepatic assessment; ECG/echocardiography despite no established cardiomyopathy in reported MRPS7 patients; neurologic examination and brain MRI/EEG if encephalopathy or seizures occur.
4. **Reproductive/endocrine assessment:** pubertal progression, menstrual history, FSH, LH, estradiol, AMH, TSH/free T4, thyroid antibodies where indicated, and adrenal testing when clinically suspected. The 2022 proband met POI criteria with menstrual disturbance and FSH above 20 mIU/mL on two occasions. (kline2022integralroleof pages 4-5)
5. **First-line molecular testing:** trio WES or WGS including nuclear mitochondrial genes and mtDNA analysis is preferred for a heterogeneous presentation. A comprehensive mitochondrial/hearing-loss/Perrault panel including MRPS7 is reasonable where exome/genome testing is unavailable. Recent cohort evidence favors WES/WGS over limited panels for “possible” mitochondrial disease. (rouzier2024primarymitochondrialdisorders pages 1-2, rouzier2024primarymitochondrialdisorders pages 8-11)
6. **Variant confirmation:** Sanger confirmation, parental segregation/phasing, population-frequency assessment, ACMG/AMP classification, and ClinVar review.
7. **Functional confirmation for novel/VUS alleles:** patient fibroblast MRPS7 immunoblot, 12S-versus-16S rRNA qPCR, mitochondrial translation pulse-labeling, OXPHOS protein/complex assessment, respiratory-chain enzymology, ATP or oxygen-consumption assays, and ideally wild-type complementation. The original study’s rescue experiments constitute the disease-specific reference assay. (menezes2015mutationinmitochondrial pages 1-2, menezes2015mutationinmitochondrial pages 6-7)

### Biopsy/pathology

Muscle may be deceptively mild or normal: original muscle oxidative stains were unremarkable and most respiratory activities were preserved, whereas liver showed severe combined deficiency. Therefore, a normal muscle study does not exclude COXPD34. Liver or kidney biopsy should be clinically driven, not routine solely for diagnosis. Renal electron microscopy may reveal giant mitochondria and reduced cristae. (menezes2015mutationinmitochondrial pages 2-3)

### Tests generally not indicated

CMA/karyotype can exclude chromosomal causes of POI but does not diagnose sequence-level MRPS7 disease. FISH and repeat-expansion testing have no disease-specific role. mtDNA testing helps exclude alternative mitochondrial etiologies but COXPD34 is nuclear encoded. The original study found no common mtDNA mutation, mt-tRNA^Leu(UUR) defect, or large mtDNA rearrangement. (menezes2015mutationinmitochondrial pages 2-3)

### Differential diagnosis

Major differentials include Perrault-spectrum genes (**CLPP, HARS2, LARS2, ERAL1, RMND1, PRORP, TWNK, TFAM, HSD17B4, PEX6, GGPS1**), other mitoribosomal disorders (**MRPS2, MRPS14, MRPS16, MRPS22, MRPS23, MRPS25, MRPS34, MRPS39, MRPL3/12/24/44**), mtDNA-related deafness, Alström syndrome, mitochondrial depletion syndromes, POLG-spectrum disease, primary hepatic/renal metabolic disorders, autoimmune POI, FMR1 premutation, and gonadotoxic/acquired causes. The second proband had normal 46,XX testing, negative FMR1-premutation testing, and negative ovarian autoantibodies. (kline2022integralroleof pages 2-4, kline2022integralroleof pages 4-5)

### Screening

COXPD34 is not an established population newborn-screening condition and lacks a validated dried-blood-spot biomarker or proven presymptomatic disease-modifying treatment. Appropriate screening is targeted: cascade testing of relatives, early audiology, metabolic/organ surveillance in biallelic children, and pubertal/ovarian monitoring in affected females.

## 11. Outcome and prognosis

No 5- or 10-year survival data, life-expectancy estimates, mortality rates, or validated prognostic biomarkers exist. Observed outcomes range from death at 14 years 5 months after progressive hepatorenal failure to survival into adulthood with successful combined liver–renal transplantation, and to relatively mild adult Perrault-spectrum disease without reported major hepatic/renal involvement. (kline2022integralroleof pages 5-8, kline2022integralroleof pages 9-10, menezes2015mutationinmitochondrial pages 2-3)

Potential adverse prognostic indicators—based only on the original family—include early persistent lactic acidemia/hypoglycemia, failure to thrive, progressive hepatic and renal biochemical abnormalities, and encephalopathy. Genotype alone is not currently predictive: homozygous p.Met184Val produced markedly different severity in sisters. Morbidity includes deafness, infertility/endocrine replacement needs, chronic organ failure, learning difficulties, hospitalization, dialysis/intensive support, and transplantation. Recovery of established multisystem disease is not documented, although organ replacement and symptom-directed treatments can substantially improve function.

## 12. Treatment

There is **no approved MRPS7-targeted or disease-modifying treatment**, no controlled trial, and no relevant COXPD34-specific NCT identified in the clinical-trial search.

### Documented real-world interventions

- **Cochlear implantation** improved speech acquisition and was tolerated in the original sisters. Suggested NCIt intervention concept: *Cochlear Implantation*. (menezes2015mutationinmitochondrial pages 2-2, menezes2015mutationinmitochondrial pages 3-4)
- **Estrogen/hormone replacement** produced a good endocrine response in the patient with failed puberty/primary hypogonadism. Suggested NCIt: *Hormone Replacement Therapy* and *Estrogen Therapy*. (menezes2015mutationinmitochondrial pages 3-4)
- **Hydrocortisone replacement** was used for primary adrenal failure. Suggested NCIt: *Hydrocortisone Therapy*.
- **Nutrition/metabolic-crisis support:** avoidance of prolonged fasting, prompt glucose-containing fluids during catabolism, correction of hypoglycemia/acidosis, and specialist nutrition are rational general mitochondrial-care measures; only nasogastric renourishment and acute resuscitation are directly reported. (menezes2015mutationinmitochondrial pages 2-3)
- **Renal/hepatic support:** hemofiltration was used during critical illness; one patient later had combined liver–renal transplantation with a positive reported outcome. Suggested NCIt: *Hemofiltration*, *Kidney Transplantation*, and *Liver Transplantation*. (kline2022integralroleof pages 9-10, menezes2015mutationinmitochondrial pages 2-3)
- **Rehabilitation:** audiology, speech/language therapy, educational support, physical/occupational therapy as needed, and fertility/endocrine counseling.

No evidence supports a specific “mitochondrial cocktail,” coenzyme Q10, riboflavin, thiamine, antioxidants, ketogenic diet, immunotherapy, stem-cell treatment, gene therapy, RNA therapy, or CRISPR treatment in COXPD34. Pharmacogenomic dosing rules do not exist. The in-vitro rescue by wild-type MRPS7 provides proof of causal reversibility at the cellular level, not a currently deliverable human gene therapy. (menezes2015mutationinmitochondrial pages 1-2)

A practical management algorithm is: molecular confirmation → multidisciplinary mitochondrial/audiology/hepatology/nephrology/endocrinology assessment → crisis-prevention plan and longitudinal organ surveillance → early hearing rehabilitation → pubertal/ovarian surveillance and fertility preservation discussion → transplant evaluation for progressive organ failure.

## 13. Prevention

The mutation cannot currently be prevented by lifestyle modification.

- **Primary prevention:** carrier testing for the reproductive partner of a known carrier; prenatal diagnosis or preimplantation genetic testing for a confirmed familial genotype; donor gametes or adoption according to patient preference and local regulation.
- **Secondary prevention:** cascade testing of siblings/relatives; early audiology; serial liver, kidney, glucose/lactate, pubertal, ovarian, thyroid, and adrenal assessment. Earlier recognition may prevent delayed cochlear rehabilitation, adrenal crisis, or missed fertility-preservation opportunities.
- **Tertiary prevention:** avoid prolonged fasting/dehydration, provide rapid treatment during infection or surgery, review potentially mitochondrial-toxic medications, manage hearing and endocrine deficiencies, and monitor organ decline before irreversible decompensation.

No vaccine prevents COXPD34; routine immunization is nevertheless important to reduce infectious stress. Genetic counseling should emphasize autosomal-recessive recurrence risk, uncertain prognosis, and substantial intrafamilial variability. Early oocyte/embryo preservation may be considered before ovarian reserve is lost, but no MRPS7-specific success data exist. (kline2022integralroleof pages 9-10)

## 14. Other species and natural disease

MRPS7 is evolutionarily conserved and mitoribosomal small-subunit biology is shared broadly across eukaryotes. However, no naturally occurring companion-animal, livestock, or wildlife syndrome directly homologous to human MRPS7-related COXPD34 was identified. Accordingly:

- **Natural veterinary disease/breed association:** none established.
- **Zoonotic transmission:** not applicable.
- **Cross-species transmission:** not applicable.
- **Comparative relevance:** conservation supports variant interpretation and model development, but does not by itself establish a natural animal disease.

Species and ortholog NCBI Gene/Taxon identifiers should be obtained directly from the current NCBI/Alliance release before database ingestion rather than inferred from the clinical papers.

## 15. Model organisms

### Established disease model

The only direct COXPD34 model is **primary patient fibroblasts carrying homozygous p.Met184Val**. These recapitulated near-absent MRPS7, reduced 12S rRNA, defective mitochondrial translation, lower MT-CO1/MT-CO2 and OXPHOS proteins, complexes I/IV dysfunction, reduced ATP production, and mitochondrial-network fragmentation. Lentiviral wild-type complementation rescued 12S rRNA and respiratory-chain activity, making this a strong causal and assay-development model. Limitations are the use of one patient line, fibroblast rather than cochlear/hepatic/renal/ovarian cells, and incomplete recapitulation of tissue-specific disease. (menezes2015mutationinmitochondrial pages 3-4, menezes2015mutationinmitochondrial pages 6-7)

### Unavailable models

No peer-reviewed MRPS7 COXPD34-specific knock-in/knockout mouse, rat, zebrafish, Drosophila, C. elegans, yeast disease model, patient iPSC, organoid, or CRISPR screen was identified. Generic mitoribosomal and ERAL1/CLPP models support the importance of small-subunit assembly and fertility but are not MRPS7 disease models. The 2024 review notes that mitochondrial-translation animal models frequently show tissue-specific and sometimes incomplete recapitulation, reinforcing the need for genotype-matched models. (antolinezfernandez2024molecularpathwaysin pages 1-2, antolinezfernandez2024molecularpathwaysin pages 14-15)

Priority future systems are: p.Met184Val and p.Arg179His knock-in mice or zebrafish; MRPS7-null/conditional tissue models; patient-derived iPSC cochlear hair cells, hepatocytes, renal-tubule organoids, and granulosa/oocyte-like cells; and isogenic CRISPR-corrected controls.

## Evidence assessment and 2023–2024 research context

No new COXPD34-specific patient series was identified for 2023–2024. The most relevant recent advances are field-level: a **24 May 2024** review synthesized how mitoribosome and mitochondrial-translation defects impair OXPHOS and preferentially injure high-energy tissues; a **2024 French cohort** of more than 2,000 suspected cases supported broad WES/WGS-based diagnosis; and **2024 patient-fibroblast proteomics** illustrated how loss of associated mitoribosomal subunits can help resolve VUS. These developments strengthen the diagnostic framework but do not change COXPD34 treatment or provide disease-specific epidemiology. (rouzier2024primarymitochondrialdisorders pages 1-2, rouzier2024primarymitochondrialdisorders pages 8-11, antolinezfernandez2024molecularpathwaysin pages 1-2)

The evidence hierarchy is therefore: **(1)** strong human familial segregation plus patient-cell rescue for p.Met184Val; **(2)** independent human allelic replication with clinical concordance for p.Lys125*/p.Arg179His; **(3)** mechanistic inference for tissue selectivity and ovarian injury; and **(4)** no direct evidence for disease-specific drugs, advanced therapies, natural animal disease, or population statistics.

References

1. (kline2022integralroleof pages 2-4): Brianna L. Kline, Sylvie Jaillard, Katrina M. Bell, Shabnam Bakhshalizadeh, Gorjana Robevska, Jocelyn van den Bergen, Jérôme Dulon, Katie L. Ayers, John Christodoulou, Michel C. Tchan, Philippe Touraine, Andrew H. Sinclair, and Elena J. Tucker. Integral role of the mitochondrial ribosome in supporting ovarian function: mrps7 variants in syndromic premature ovarian insufficiency. Nov 2022. URL: https://doi.org/10.3390/genes13112113, doi:10.3390/genes13112113. This article has 19 citations.

2. (menezes2015mutationinmitochondrial pages 2-3): Minal J. Menezes, Yiran Guo, Jianguo Zhang, Lisa G. Riley, Sandra T. Cooper, David R. Thorburn, Jiankang Li, Daoyuan Dong, Zhijun Li, Joseph Glessner, Ryan L. Davis, Carolyn M. Sue, Stephen I. Alexander, Susan Arbuckle, Paul Kirwan, Brendan J. Keating, Xun Xu, Hakon Hakonarson, and John Christodoulou. Mutation in mitochondrial ribosomal protein s7 (mrps7) causes congenital sensorineural deafness, progressive hepatic and renal failure and lactic acidemia. Human molecular genetics, 24 8:2297-307, Jan 2015. URL: https://doi.org/10.1093/hmg/ddu747, doi:10.1093/hmg/ddu747. This article has 62 citations and is from a domain leading peer-reviewed journal.

3. (menezes2015mutationinmitochondrial pages 1-2): Minal J. Menezes, Yiran Guo, Jianguo Zhang, Lisa G. Riley, Sandra T. Cooper, David R. Thorburn, Jiankang Li, Daoyuan Dong, Zhijun Li, Joseph Glessner, Ryan L. Davis, Carolyn M. Sue, Stephen I. Alexander, Susan Arbuckle, Paul Kirwan, Brendan J. Keating, Xun Xu, Hakon Hakonarson, and John Christodoulou. Mutation in mitochondrial ribosomal protein s7 (mrps7) causes congenital sensorineural deafness, progressive hepatic and renal failure and lactic acidemia. Human molecular genetics, 24 8:2297-307, Jan 2015. URL: https://doi.org/10.1093/hmg/ddu747, doi:10.1093/hmg/ddu747. This article has 62 citations and is from a domain leading peer-reviewed journal.

4. (kline2022integralroleof pages 1-2): Brianna L. Kline, Sylvie Jaillard, Katrina M. Bell, Shabnam Bakhshalizadeh, Gorjana Robevska, Jocelyn van den Bergen, Jérôme Dulon, Katie L. Ayers, John Christodoulou, Michel C. Tchan, Philippe Touraine, Andrew H. Sinclair, and Elena J. Tucker. Integral role of the mitochondrial ribosome in supporting ovarian function: mrps7 variants in syndromic premature ovarian insufficiency. Nov 2022. URL: https://doi.org/10.3390/genes13112113, doi:10.3390/genes13112113. This article has 19 citations.

5. (menezes2015mutationinmitochondrial pages 3-4): Minal J. Menezes, Yiran Guo, Jianguo Zhang, Lisa G. Riley, Sandra T. Cooper, David R. Thorburn, Jiankang Li, Daoyuan Dong, Zhijun Li, Joseph Glessner, Ryan L. Davis, Carolyn M. Sue, Stephen I. Alexander, Susan Arbuckle, Paul Kirwan, Brendan J. Keating, Xun Xu, Hakon Hakonarson, and John Christodoulou. Mutation in mitochondrial ribosomal protein s7 (mrps7) causes congenital sensorineural deafness, progressive hepatic and renal failure and lactic acidemia. Human molecular genetics, 24 8:2297-307, Jan 2015. URL: https://doi.org/10.1093/hmg/ddu747, doi:10.1093/hmg/ddu747. This article has 62 citations and is from a domain leading peer-reviewed journal.

6. (menezes2015mutationinmitochondrial pages 6-7): Minal J. Menezes, Yiran Guo, Jianguo Zhang, Lisa G. Riley, Sandra T. Cooper, David R. Thorburn, Jiankang Li, Daoyuan Dong, Zhijun Li, Joseph Glessner, Ryan L. Davis, Carolyn M. Sue, Stephen I. Alexander, Susan Arbuckle, Paul Kirwan, Brendan J. Keating, Xun Xu, Hakon Hakonarson, and John Christodoulou. Mutation in mitochondrial ribosomal protein s7 (mrps7) causes congenital sensorineural deafness, progressive hepatic and renal failure and lactic acidemia. Human molecular genetics, 24 8:2297-307, Jan 2015. URL: https://doi.org/10.1093/hmg/ddu747, doi:10.1093/hmg/ddu747. This article has 62 citations and is from a domain leading peer-reviewed journal.

7. (kline2022integralroleof pages 4-5): Brianna L. Kline, Sylvie Jaillard, Katrina M. Bell, Shabnam Bakhshalizadeh, Gorjana Robevska, Jocelyn van den Bergen, Jérôme Dulon, Katie L. Ayers, John Christodoulou, Michel C. Tchan, Philippe Touraine, Andrew H. Sinclair, and Elena J. Tucker. Integral role of the mitochondrial ribosome in supporting ovarian function: mrps7 variants in syndromic premature ovarian insufficiency. Nov 2022. URL: https://doi.org/10.3390/genes13112113, doi:10.3390/genes13112113. This article has 19 citations.

8. (kline2022integralroleof pages 5-8): Brianna L. Kline, Sylvie Jaillard, Katrina M. Bell, Shabnam Bakhshalizadeh, Gorjana Robevska, Jocelyn van den Bergen, Jérôme Dulon, Katie L. Ayers, John Christodoulou, Michel C. Tchan, Philippe Touraine, Andrew H. Sinclair, and Elena J. Tucker. Integral role of the mitochondrial ribosome in supporting ovarian function: mrps7 variants in syndromic premature ovarian insufficiency. Nov 2022. URL: https://doi.org/10.3390/genes13112113, doi:10.3390/genes13112113. This article has 19 citations.

9. (kline2022integralroleof pages 8-9): Brianna L. Kline, Sylvie Jaillard, Katrina M. Bell, Shabnam Bakhshalizadeh, Gorjana Robevska, Jocelyn van den Bergen, Jérôme Dulon, Katie L. Ayers, John Christodoulou, Michel C. Tchan, Philippe Touraine, Andrew H. Sinclair, and Elena J. Tucker. Integral role of the mitochondrial ribosome in supporting ovarian function: mrps7 variants in syndromic premature ovarian insufficiency. Nov 2022. URL: https://doi.org/10.3390/genes13112113, doi:10.3390/genes13112113. This article has 19 citations.

10. (kline2022integralroleof pages 9-10): Brianna L. Kline, Sylvie Jaillard, Katrina M. Bell, Shabnam Bakhshalizadeh, Gorjana Robevska, Jocelyn van den Bergen, Jérôme Dulon, Katie L. Ayers, John Christodoulou, Michel C. Tchan, Philippe Touraine, Andrew H. Sinclair, and Elena J. Tucker. Integral role of the mitochondrial ribosome in supporting ovarian function: mrps7 variants in syndromic premature ovarian insufficiency. Nov 2022. URL: https://doi.org/10.3390/genes13112113, doi:10.3390/genes13112113. This article has 19 citations.

11. (OpenTargets Search: Combined oxidative phosphorylation deficiency 34): Open Targets Query (Combined oxidative phosphorylation deficiency 34, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

12. (webb2020mitochondrialtranslationdefects pages 12-13): Bryn D. Webb, George A. Diaz, and Pankaj Prasun. Mitochondrial translation defects and human disease. Journal of translational genetics and genomics, 4:71-80, May 2020. URL: https://doi.org/10.20517/jtgg.2020.11, doi:10.20517/jtgg.2020.11. This article has 29 citations.

13. (menezes2015mutationinmitochondrial pages 2-2): Minal J. Menezes, Yiran Guo, Jianguo Zhang, Lisa G. Riley, Sandra T. Cooper, David R. Thorburn, Jiankang Li, Daoyuan Dong, Zhijun Li, Joseph Glessner, Ryan L. Davis, Carolyn M. Sue, Stephen I. Alexander, Susan Arbuckle, Paul Kirwan, Brendan J. Keating, Xun Xu, Hakon Hakonarson, and John Christodoulou. Mutation in mitochondrial ribosomal protein s7 (mrps7) causes congenital sensorineural deafness, progressive hepatic and renal failure and lactic acidemia. Human molecular genetics, 24 8:2297-307, Jan 2015. URL: https://doi.org/10.1093/hmg/ddu747, doi:10.1093/hmg/ddu747. This article has 62 citations and is from a domain leading peer-reviewed journal.

14. (menezes2015mutationinmitochondrial pages 7-8): Minal J. Menezes, Yiran Guo, Jianguo Zhang, Lisa G. Riley, Sandra T. Cooper, David R. Thorburn, Jiankang Li, Daoyuan Dong, Zhijun Li, Joseph Glessner, Ryan L. Davis, Carolyn M. Sue, Stephen I. Alexander, Susan Arbuckle, Paul Kirwan, Brendan J. Keating, Xun Xu, Hakon Hakonarson, and John Christodoulou. Mutation in mitochondrial ribosomal protein s7 (mrps7) causes congenital sensorineural deafness, progressive hepatic and renal failure and lactic acidemia. Human molecular genetics, 24 8:2297-307, Jan 2015. URL: https://doi.org/10.1093/hmg/ddu747, doi:10.1093/hmg/ddu747. This article has 62 citations and is from a domain leading peer-reviewed journal.

15. (kline2022integralroleof pages 10-12): Brianna L. Kline, Sylvie Jaillard, Katrina M. Bell, Shabnam Bakhshalizadeh, Gorjana Robevska, Jocelyn van den Bergen, Jérôme Dulon, Katie L. Ayers, John Christodoulou, Michel C. Tchan, Philippe Touraine, Andrew H. Sinclair, and Elena J. Tucker. Integral role of the mitochondrial ribosome in supporting ovarian function: mrps7 variants in syndromic premature ovarian insufficiency. Nov 2022. URL: https://doi.org/10.3390/genes13112113, doi:10.3390/genes13112113. This article has 19 citations.

16. (antolinezfernandez2024molecularpathwaysin pages 1-2): Álvaro Antolínez-Fernández, Paula Esteban-Ramos, Miguel Ángel Fernández-Moreno, and Paula Clemente. Molecular pathways in mitochondrial disorders due to a defective mitochondrial protein synthesis. Frontiers in Cell and Developmental Biology, May 2024. URL: https://doi.org/10.3389/fcell.2024.1410245, doi:10.3389/fcell.2024.1410245. This article has 18 citations.

17. (rouzier2024primarymitochondrialdisorders pages 1-2): Cécile Rouzier, Emmanuelle Pion, Annabelle Chaussenot, Céline Bris, Samira Ait‐El‐Mkadem Saadi, Valérie Desquiret‐Dumas, Naïg Gueguen, Konstantina Fragaki, Patrizia Amati‐Bonneau, Giulia Barcia, Pauline Gaignard, Julie Steffann, Alessandra Pennisi, Jean‐Paul Bonnefont, Elise Lebigot, Sylvie Bannwarth, Bruno Francou, Benoit Rucheton, Damien Sternberg, Marie‐Laure Martin‐Negrier, Aurélien Trimouille, Gaëlle Hardy, Stéphane Allouche, Cécile Acquaviva‐Bourdain, Cécile Pagan, Anne‐Sophie Lebre, Pascal Reynier, Mireille Cossee, Shahram Attarian, Véronique Paquis‐Flucklinger, and Vincent Procaccio. Primary mitochondrial disorders and mimics: insights from a large french cohort. Annals of Clinical and Translational Neurology, 11:1478-1491, May 2024. URL: https://doi.org/10.1002/acn3.52062, doi:10.1002/acn3.52062. This article has 16 citations and is from a peer-reviewed journal.

18. (rouzier2024primarymitochondrialdisorders pages 8-11): Cécile Rouzier, Emmanuelle Pion, Annabelle Chaussenot, Céline Bris, Samira Ait‐El‐Mkadem Saadi, Valérie Desquiret‐Dumas, Naïg Gueguen, Konstantina Fragaki, Patrizia Amati‐Bonneau, Giulia Barcia, Pauline Gaignard, Julie Steffann, Alessandra Pennisi, Jean‐Paul Bonnefont, Elise Lebigot, Sylvie Bannwarth, Bruno Francou, Benoit Rucheton, Damien Sternberg, Marie‐Laure Martin‐Negrier, Aurélien Trimouille, Gaëlle Hardy, Stéphane Allouche, Cécile Acquaviva‐Bourdain, Cécile Pagan, Anne‐Sophie Lebre, Pascal Reynier, Mireille Cossee, Shahram Attarian, Véronique Paquis‐Flucklinger, and Vincent Procaccio. Primary mitochondrial disorders and mimics: insights from a large french cohort. Annals of Clinical and Translational Neurology, 11:1478-1491, May 2024. URL: https://doi.org/10.1002/acn3.52062, doi:10.1002/acn3.52062. This article has 16 citations and is from a peer-reviewed journal.

19. (antolinezfernandez2024molecularpathwaysin pages 14-15): Álvaro Antolínez-Fernández, Paula Esteban-Ramos, Miguel Ángel Fernández-Moreno, and Paula Clemente. Molecular pathways in mitochondrial disorders due to a defective mitochondrial protein synthesis. Frontiers in Cell and Developmental Biology, May 2024. URL: https://doi.org/10.3389/fcell.2024.1410245, doi:10.3389/fcell.2024.1410245. This article has 18 citations.

## Artifacts

- [Edison artifact artifact-00](Combined_Oxidative_Phosphorylation_Deficiency_34-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0054741` (3 mentions) - the report calls it "if available"; MONDO calls it **combined oxidative phosphorylation deficiency 34**
