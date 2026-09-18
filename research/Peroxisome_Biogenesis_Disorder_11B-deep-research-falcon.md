---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T17:01:56.515999'
end_time: '2026-09-02T17:15:35.315406'
duration_seconds: 818.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Peroxisome Biogenesis Disorder 11B
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 31
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Peroxisome_Biogenesis_Disorder_11B-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome Biogenesis Disorder 11B
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 11B** covering all of the
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
- **Disease Name:** Peroxisome Biogenesis Disorder 11B
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 11B** covering all of the
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


# Peroxisome Biogenesis Disorder 11B (PEX13-related Zellweger spectrum disorder)

## Scope and evidence grading

Peroxisome biogenesis disorder 11B (PBD11B) is an **ultra-rare, autosomal-recessive PEX13-related Zellweger spectrum disorder (ZSD)**. Because only about **22 affected individuals and 20 variant types** had been reported worldwide by 2024, reliable PEX13-specific prevalence, phenotype-frequency, penetrance, survival, and treatment-response estimates do not exist. This report therefore distinguishes **PEX13-specific human evidence** from broader **ZSD-wide evidence** and experimental evidence from cells or animals. The primary sources retrieved did not consistently expose PMID metadata; DOI links and publication dates are supplied rather than inventing PMIDs.

| Domain | PEX13-specific finding | Evidence type | Key source/date |
|---|---|---|---|
| Identity and inheritance | Peroxisome biogenesis disorder 11B is **PEX13-related Zellweger spectrum disorder**, caused by biallelic germline **PEX13** variants and inherited in an autosomal-recessive manner. | Human genetic; PEX13-specific | Borgia et al., July 2022, [DOI](https://doi.org/10.1186/s13023-022-02415-5); Su et al., November 2024, [DOI](https://doi.org/10.1002/mgg3.2315) (su2024severezellwegerspectrum pages 1-2, borgia2022genotype–phenotypecorrelationsand pages 1-2) |
| Reported case count | A 2024 review counted **22 reported patients worldwide** and approximately **20 variant types**, demonstrating extreme rarity. This is a literature case count, not a population-prevalence estimate. | Human literature review; PEX13-specific | Su et al., November 2024, [DOI](https://doi.org/10.1002/mgg3.2315) (su2024severezellwegerspectrum pages 4-6) |
| Representative variants | Reported alleles include **c.493G>C (p.Ala165Pro)**, **c.880C>T (p.Arg294Trp)**, **p.Trp313Gly**, **p.Trp313Ter**, **p.Gly324Arg**, truncating variants, and partial or large deletions. p.Arg294Trp recurred in three of five families in a 2022 series. | Human genetic plus functional or computational; PEX13-specific | Borgia et al., July 2022, [DOI](https://doi.org/10.1186/s13023-022-02415-5); Su et al., November 2024, [DOI](https://doi.org/10.1002/mgg3.2315) (borgia2022genotype–phenotypecorrelationsand pages 6-9, su2024severezellwegerspectrum pages 4-6, krause2006identificationofnovel pages 3-4) |
| Core mechanism | PEX13 is a peroxisomal-membrane docking and translocation factor for PEX5/PEX14-mediated matrix-protein import. Pathogenic variants impair PEX13 self-association or partner binding, reducing PTS1 or PTS2 import and functional peroxisomes; secondary mitochondrial dysfunction may contribute. | Human cells, structural biology, computational modeling, and mouse experiments | Krause et al., October 2013, [DOI](https://doi.org/10.1093/hmg/ddt238); Borgia et al., July 2022, [DOI](https://doi.org/10.1186/s13023-022-02415-5) (krause2013functionalanalysisof pages 1-2, borgia2022genotype–phenotypecorrelationsand pages 11-13, borgia2022genotype–phenotypecorrelationsand pages 1-2) |
| 2024 mechanistic advance | Structural work showed that the PEX13 SH3 domain and proximal **FxxxF** motif regulate binding to PEX5 WxxxF/Y motifs and PEX14. PEX14 bound the PEX13 FxxxF motif with a dissociation constant of **9.2 micromolar**. | In vitro biochemical and structural; PEX13-specific | Gaussmann et al., April 2024, [DOI](https://doi.org/10.1038/s41467-024-47605-w) (gaussmann2024modulationofperoxisomal pages 3-4, gaussmann2024modulationofperoxisomal pages 11-12, gaussmann2024modulationofperoxisomal pages 1-2) |
| Phenotype | PEX13-related disease ranges from severe neonatal multisystem illness to childhood progressive neurologic disease. Findings include hypotonia, seizures, developmental delay or regression, spasticity, leukodystrophy, hearing or vision impairment, feeding or respiratory difficulty, and hepatic or renal involvement. Frequencies cannot be estimated reliably from the small reported population. | Human clinical; PEX13-specific | Borgia et al., July 2022, [DOI](https://doi.org/10.1186/s13023-022-02415-5); Su et al., November 2024, [DOI](https://doi.org/10.1002/mgg3.2315) (borgia2022genotype–phenotypecorrelationsand pages 6-9, su2024severezellwegerspectrum pages 2-4, borgia2022genotype–phenotypecorrelationsand pages 2-4) |
| Diagnostics | Diagnosis combines plasma very-long-chain fatty acids, especially C26:0 and the C26:0/C22:0 ratio, with phytanic and pristanic acids, pipecolic acid, bile-acid intermediates, plasmalogens, and molecular confirmation by a PEX panel or exome or genome sequencing. Normal or mildly abnormal VLCFA does **not** exclude PEX13 disease. | PEX13 cases plus ZSD-wide diagnostic evidence | Borgia et al., July 2022, [DOI](https://doi.org/10.1186/s13023-022-02415-5); Bose et al., June 2022, [DOI](https://doi.org/10.3390/cells11121891); Su et al., November 2024, [DOI](https://doi.org/10.1002/mgg3.2315) (su2024severezellwegerspectrum pages 2-4, bose2022characterizationofseverity pages 1-2, borgia2022genotype–phenotypecorrelationsand pages 13-15) |
| Prognosis | PEX13-specific prognosis is genotype-dependent and incompletely quantified. Severe homozygous disease can cause early death; the 2024 p.Ala165Pro case died at **14 months**. Hypomorphic genotypes may permit survival into later childhood with progressive disability. ZSD-wide survival estimates are not PEX13-specific. | Human case reports with ZSD-wide contextual evidence | Su et al., November 2024, [DOI](https://doi.org/10.1002/mgg3.2315); Bose et al., June 2022, [DOI](https://doi.org/10.3390/cells11121891) (su2024severezellwegerspectrum pages 2-4, bose2022characterizationofseverity pages 12-13, bose2022characterizationofseverity pages 9-10) |
| Treatment and trials | No curative or established PEX13-specific disease-modifying therapy exists. Care is supportive and may include antiseizure treatment, feeding support, hearing and vision services, rehabilitation, liver and adrenal surveillance, and respiratory care. Current ZSD studies are not PEX13-specific; recruiting **NCT06190626** follows retinopathy in 30 participants, while evidence for cholic acid, betaine, and hydroxychloroquine remains limited or conflicting. | Clinical management and ZSD-wide trials; not PEX13-specific | ClinicalTrials.gov, 2023, [NCT06190626](https://clinicaltrials.gov/study/NCT06190626); Bose et al., June 2022, [DOI](https://doi.org/10.3390/cells11121891) (NCT06190626 chunk 1, bose2022characterizationofseverity pages 2-3) |


*Table: Compact evidence summary for PEX13-related peroxisome biogenesis disorder 11B. It distinguishes disease-specific observations from broader Zellweger spectrum disorder evidence and highlights recent mechanistic and clinical developments.*

## 1. Disease information

PBD11B is a Mendelian disorder in which biallelic pathogenic variants in **PEX13** impair peroxisomal matrix-protein import. The resulting peroxisomal dysfunction causes a variable multisystem phenotype ranging from severe neonatal cerebro-hepato-renal disease to a predominantly neurologic childhood disorder with progressive spasticity and leukodystrophy. In 2024, Su et al. stated that only 22 PEX13-related cases had been reported worldwide, emphasizing that published knowledge is based chiefly on individual families and aggregated case literature—not population EHR cohorts. (su2024severezellwegerspectrum pages 1-2, borgia2022genotype–phenotypecorrelationsand pages 1-2, su2024severezellwegerspectrum pages 4-6)

**Identifiers and names**

- Disease names: *peroxisome biogenesis disorder 11B*, *PEX13-related Zellweger spectrum disorder*, *PEX13 deficiency*, and historically *Zellweger syndrome caused by PEX13 deficiency*.
- Gene: **PEX13**, OMIM gene **601789**; reference transcript used in recent reports: **NM_002618.3**. (su2024severezellwegerspectrum pages 1-2)
- Disease-level OMIM, MONDO, Orphanet, MeSH, ICD-10, and ICD-11 identifiers were not recoverable from the primary full-text evidence and should be verified directly against the current releases before database ingestion. ZSD is generally coded under broader peroxisomal-disorder categories because no PEX13-specific ICD code is established.
- Data provenance: individual case reports/series, patient fibroblasts and muscle, literature-level ZSD meta-analysis, and observational registries. It is not derived from a representative population sample.

## 2. Etiology

### Causal factors

The established cause is **biallelic germline PEX13 dysfunction**. PEX13 encodes an integral peroxisomal membrane component of the PEX5–PEX13–PEX14 docking/translocation machinery. Loss or alteration of this component impairs import of PTS1- and/or PTS2-bearing matrix enzymes. (jiang2025modellingperoxisomaldisorders pages 11-13, krause2013functionalanalysisof pages 1-2)

### Genetic risk

- Affected individuals are homozygous or compound heterozygous for pathogenic/likely pathogenic PEX13 alleles.
- Reported classes include missense, nonsense, frameshift, partial-gene deletion, and an approximately 147-kb deletion. Representative alleles include **c.493G>C (p.Ala165Pro)**, **c.880C>T (p.Arg294Trp)**, **p.Trp313Gly**, **p.Trp313Ter**, **p.Gly324Arg**, and truncating/deletion alleles. (borgia2022genotype–phenotypecorrelationsand pages 6-9, su2024severezellwegerspectrum pages 4-6, borgia2022genotype–phenotypecorrelationsand pages 2-4)
- The recurrent p.Arg294Trp allele occurred in three of five families in the 2022 series. It is not established as a population-wide founder allele. (borgia2022genotype–phenotypecorrelationsand pages 1-2)
- Consanguinity is an important family-level risk: three of five families in the 2022 series were consanguineous, and the 2024 p.Ala165Pro patient was born to first-cousin parents. (su2024severezellwegerspectrum pages 1-2, borgia2022genotype–phenotypecorrelationsand pages 6-9)
- Family history may be negative because carrier parents are clinically unaffected.

No validated susceptibility loci, modifier genes, genetic protective alleles, anticipation, or PEX13-specific germline-mosaicism cases have been established. Residual PEX13 function probably modifies severity, but genotype–phenotype prediction remains imperfect.

### Environmental, protective, and gene–environment factors

No toxin, infection, lifestyle, diet, sex, or occupational exposure causes PBD11B. There are no validated environmental protective factors. Fever, fasting, illness, anesthesia, and nutritional stress may exacerbate metabolic vulnerability in peroxisomal disease, but direct PEX13-patient evidence is inadequate. Thus, these should be treated as clinical stressors rather than etiologic factors.

## 3. Phenotypes

PEX13-specific frequencies cannot be estimated reliably from 22 heterogeneous published cases. Suggested HPO annotations are therefore qualitative.

| Phenotype | Characterization in PEX13 disease | Suggested HPO term |
|---|---|---|
| Hypotonia | Commonly neonatal/infantile; severe in classic disease | Hypotonia, **HP:0001252** |
| Developmental delay/regression | Global delay, absent milestones, or later loss of motor/language skills; variable severity | Global developmental delay, **HP:0001263**; Developmental regression, **HP:0002376** |
| Seizures | Neonatal or infantile in severe disease; variable in milder disease | Seizure, **HP:0001250** |
| Spasticity/tetraparesis | Progressive childhood manifestation in neurologically predominant disease | Spasticity, **HP:0001257** |
| Leukodystrophy | Progressive posterior/periventricular, internal-capsule, corpus-callosal, brainstem, and cerebellar abnormalities reported | Leukodystrophy, **HP:0002415** |
| Hearing impairment | Usually sensorineural; may be early presenting feature | Sensorineural hearing impairment, **HP:0000407** |
| Visual impairment | Myopia, nystagmus, retinal/optic abnormalities, or reduced vision | Visual impairment, **HP:0000505**; Myopia, **HP:0000545**; Nystagmus, **HP:0000639** |
| Feeding difficulty/failure to thrive | Especially in severe infantile disease | Feeding difficulties, **HP:0011968**; Failure to thrive, **HP:0001508** |
| Hepatic disease | Hepatomegaly, transaminase/bile-acid abnormalities, dysfunction | Hepatomegaly, **HP:0002240**; Elevated transaminases, **HP:0002910** |
| Respiratory difficulty | Neonatal dyspnea, apnea, aspiration risk, or respiratory compromise secondary to hypotonia | Respiratory distress, **HP:0002098**; Apnea, **HP:0002104** |
| Dysmorphism | Prominent forehead and other variable craniofacial findings | Abnormal facial shape, **HP:0001999** |
| Biochemical abnormalities | Elevated C26:0/C22:0, phytanic/pristanic acids, pipecolic acid and bile-acid intermediates; abnormalities can be mild or absent | Increased VLCFA level, **HP:0008166** |

The 2022 cohort documented hypotonia, weakness, sensory impairment, progressive spasticity, developmental regression, and leukodystrophy. One child progressed to wheelchair dependence by approximately 7–9 years and had spastic tetraparesis, dystonia, ataxia, dysarthria, nystagmus, tremor, and mild cognitive regression. (borgia2022genotype–phenotypecorrelationsand pages 6-9, borgia2022genotype–phenotypecorrelationsand pages 1-2)

The 2024 p.Ala165Pro infant had neonatal hypotonia and respiratory compromise, seizures by three months, profound developmental impairment, hearing and visual dysfunction, hepatomegaly, biochemical abnormalities, and death at 14 months. (su2024severezellwegerspectrum pages 1-2, su2024severezellwegerspectrum pages 2-4)

**ZSD-wide—not PEX13-specific—context:** in a natural-history cohort, severe ZSD showed seizures and hypotonia in 100% of evaluated patients, MRI abnormalities in 95%, feeding difficulty in 90%, liver dysfunction in 94.4%, renal microcysts in 79%, and cardiac abnormalities in 81.3%. Intermediate ZSD commonly involved hypotonia, developmental delay, vision loss, feeding difficulty, failure to thrive, liver disease, and adrenal insufficiency. These values must not be assigned directly to PBD11B. (bose2022characterizationofseverity pages 10-12, bose2022characterizationofseverity pages 9-10)

Quality of life is strongly affected by sensory loss, impaired communication, feeding dependence, seizures, reduced mobility, and caregiver burden. However, no validated PEX13-specific EQ-5D, SF-36, or PROMIS dataset exists. NCT03440905 enrolled 92 caregivers and used symptom, Pediatric Inventory for Parents, and Family Quality of Life surveys, but available registry text did not report outcome values. (NCT03440905 chunk 1)

## 4. Genetic and molecular information

**PEX13** lies on chromosome 2 and contains four exons in the cited clinical report. Its protein includes an N-terminal region required for peroxisomal localization, a transmembrane region, a proximal FxxxF motif, and a C-terminal SH3 domain; the recent clinical paper described Peroxin-13_N at residues 117–254 and SH3_PEX13_eumet at 276–333. (su2024severezellwegerspectrum pages 4-6, krause2013functionalanalysisof pages 1-2)

Pathogenic alleles are germline and primarily produce **loss or severe reduction of function**, not gain of function or dominant-negative disease. Consequences differ by allele:

- **p.Trp313Gly:** disrupts PEX13 homooligomerization and selectively impairs PTS1 import while preserving PTS2 import in the studied system. (krause2013functionalanalysisof pages 1-2)
- **p.Arg294Trp:** computationally predicted to alter dimerization and reduce accessibility/stability of the PEX13–PEX14 module; patient cells show reduced PEX13-positive peroxisomes and mitochondrial abnormalities. (borgia2022genotype–phenotypecorrelationsand pages 11-13, borgia2022genotype–phenotypecorrelationsand pages 1-2)
- **p.Gly324Arg:** predicted to disrupt folding and formation of the PEX13–PEX14–PEX5 complex. (borgia2022genotype–phenotypecorrelationsand pages 11-13)
- **p.Ala165Pro:** classified likely pathogenic in the 2024 report and associated homozygously with severe neonatal disease. (su2024severezellwegerspectrum pages 2-4)

Variant-specific gnomAD/TOPMed frequencies and ClinVar review status were not available in the retrieved primary texts and require direct variant-by-variant database queries using a normalized transcript. No established modifier gene, disease-specific epigenetic signature, recurrent aneuploidy, or balanced chromosomal rearrangement is known. Large deletions can cause disease when they disrupt PEX13, but routine PBD11B is a sequence-level recessive disorder.

## 5. Environmental information

Environmental toxins, radiation, smoking, alcohol, diet, and infectious agents are **not established causes**. PBD11B is not transmissible or zoonotic. Environmental and lifestyle data are clinically relevant mainly for avoiding secondary complications—for example, malnutrition, aspiration, prolonged fasting, and unmanaged infection—not for altering the inherited causal lesion.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic PEX13 variants lead to** absent, unstable, mislocalized, or interaction-defective PEX13 at the peroxisomal membrane.
2. **Defective PEX13 leads to** impaired PEX13 homooligomerization and/or disturbed binding among PEX13, PEX14, and the PEX5 cargo receptor.
3. **Docking/translocation failure leads to** deficient import of PTS1 and, depending on allele, PTS2 matrix proteins into PMP70/ABCD3-positive membrane “ghosts.”
4. **Loss of matrix enzymes leads to** impaired VLCFA and branched-chain fatty-acid oxidation, reduced ether-phospholipid/plasmalogen synthesis, abnormal bile-acid intermediates, and disturbed redox homeostasis.
5. **PEX13 loss also leads to** accumulation of ubiquitinated PEX5 and increased peroxisomal ROS, which recruit autophagy machinery and increase pexophagy; this branch is demonstrated in cells and zebrafish but remains incompletely proven in patients. (demers2023pex13preventspexophagy pages 14-15, demers2023pex13preventspexophagy pages 6-7)
6. **Peroxisomal metabolic/redox failure leads to** secondary mitochondrial mislocalization, impaired membrane potential, abnormal cristae, oxidative stress, and apoptosis; the complete sequence is supported by patient cells and mouse brain but is partly inferred in humans. (maxwell2003pex13inactivationin pages 6-8, borgia2022genotype–phenotypecorrelationsand pages 13-15)
7. **Lipid imbalance, oxidative injury, and defective organelle cooperation lead to** abnormal neuronal migration/development, dysmyelination or leukodystrophy, neuronal loss, gliosis, hepatic lipid accumulation, renal developmental abnormalities, and sensory-organ dysfunction.
8. **Tissue injury leads to** neonatal hypotonia, seizures, developmental failure or regression, progressive spasticity, hearing/vision loss, liver disease, feeding/respiratory compromise, and—in severe disease—early death.

### Molecular details and recent research

PEX13 is part of the matrix-protein docking/translocation module. PEX5 carries PTS1 cargo and binds PEX13/PEX14; PEX7 supports PTS2 import. Pex13-null mouse cells retained membrane structures but failed to import matrix proteins: post-organellar catalase increased from **18% ±1% to 81%**, C26:0/C22:0 rose **9-fold in liver, 6.5-fold in brain, and 50-fold in fibroblasts**, phytanic/pristanic oxidation fell **50–100-fold**, and liver C16:0 and C18:0 plasmalogens fell approximately **20-fold and 3-fold**. Wild-type PEX13 re-expression restored PTS1 and PTS2 import. (maxwell2003pex13inactivationin pages 6-8)

A major **2024 structural advance** showed that the PEX13 SH3 domain binds a proximal intramolecular **FxxxF** motif, regulating access to noncanonical binding surfaces for PEX5 WxxxF/Y motifs. PEX14 binds the PEX13 FxxxF motif with **KD 9.2 μM**, releasing or remodeling this autoinhibitory arrangement. The data support dynamic or sequential receptor handover rather than a rigid, stable PEX5–PEX13–PEX14 ternary complex. (gaussmann2024modulationofperoxisomal pages 3-4, gaussmann2024modulationofperoxisomal pages 11-12, gaussmann2024modulationofperoxisomal pages 1-2)

A short exact statement from the 2024 abstract is: **“Import of proteins into peroxisomes depends on PEX5, PEX13 and PEX14.”** The authors further concluded that the interaction network “modulates peroxisomal matrix import.” (gaussmann2024modulationofperoxisomal pages 1-2)

A **2023 pexophagy study** found that PEX13 loss caused ubiquitinated PEX5 accumulation and elevated ROS, jointly promoting selective autophagic loss of peroxisomes. Wild-type PEX13, but not W313G or I326T, rescued starvation-associated peroxisome loss in HeLa cells. In maternal-zygotic pex13-null zebrafish, approximately **90–95% of more than 400 larvae died at 9–11 days post-fertilization**; chloroquine restored peroxisome-membrane structures but not matrix import or hepatic lipid accumulation. Human PEX13 mRNA partially rescued the dark-liver phenotype. (demers2023pex13preventspexophagy pages 14-15, demers2023pex13preventspexophagy pages 6-7)

### Suggested ontology annotations

- GO biological process: peroxisome organization; protein import into peroxisome matrix; fatty-acid beta-oxidation; ether-lipid biosynthetic process; reactive-oxygen-species metabolic process; selective autophagy of peroxisome; nervous-system development.
- GO cellular component: **peroxisomal membrane (GO:0005778)**, peroxisome, PEX13–PEX14 docking complex, mitochondrion.
- Cell Ontology candidates: neuron (**CL:0000540**), astrocyte (**CL:0000127**), microglial cell (**CL:0000129**), hepatocyte (**CL:0000182**), renal epithelial cell, Purkinje cell (**CL:0000121**), cerebellar granule cell, fibroblast (**CL:0000057**), retinal photoreceptor, and retinal pigment epithelial cell.

No PEX13-patient single-cell, spatial-transcriptomic, or integrated multi-omics study was identified. Available molecular profiling consists principally of targeted lipid/biochemical assays, histology, imaging, mitochondrial functional measurements, and structural biology.

## 7. Anatomical structures affected

**Primary systems:** central and peripheral nervous systems, liver, eye/retina, auditory system, skeletal muscle, and—particularly in severe ZSD—kidney and adrenal gland. Brain involvement includes cerebral and cerebellar white matter, cortex, corpus callosum, internal capsule, brainstem, basal ganglia, and cerebellar/dentate pathways. (borgia2022genotype–phenotypecorrelationsand pages 6-9, su2024severezellwegerspectrum pages 2-4)

**Tissue/cell level:** neurons and myelinating systems are central to developmental regression, spasticity, and leukodystrophy. Mouse models implicate cerebellar granule-cell migration, Purkinje-layer development, astrocytes, and microglia. Hepatocytes accumulate lipid; renal glomerular development is delayed in null mice; skeletal muscle can show abnormal mitochondrial distribution. (maxwell2003pex13inactivationin pages 6-8, borgia2022genotype–phenotypecorrelationsand pages 13-15)

**Subcellular level:** the initiating compartment is the peroxisomal membrane and matrix-import machinery, with secondary mitochondrial and autophagosome involvement. Suggested anatomy terms include UBERON:0000955 brain, UBERON:0002107 liver, UBERON:0002113 kidney, UBERON:0000966 retina, UBERON:0002037 cerebellum, and UBERON:0002240 spinal cord. No consistent lateralization is reported; involvement is generally bilateral/systemic.

## 8. Temporal development

Severe PBD11B begins prenatally or neonatally, with hypotonia, poor feeding, respiratory compromise, seizures, dysmorphism, and liver dysfunction. Less severe disease may present in infancy or childhood with developmental delay, hearing/visual impairment, then progressive motor regression, spasticity, dystonia, ataxia, and leukodystrophy. (su2024severezellwegerspectrum pages 1-2, borgia2022genotype–phenotypecorrelationsand pages 6-9)

The course is chronic and generally progressive, not relapsing-remitting. Severe disease may be fatal in infancy; partial-function alleles can permit survival into later childhood or beyond but with progressive disability. No spontaneous remission is documented. Prenatal development and early infancy are critical periods because peroxisomes are required for neuronal migration, membrane-lipid synthesis, and organ maturation. Early recognition permits anticipatory management but currently does not reverse the molecular defect.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two carrier parents, each pregnancy has a 25% probability of an affected child, 50% probability of a carrier, and 25% probability of inheriting neither familial allele. Penetrance for truly biallelic severe loss-of-function genotypes appears high, but expressivity is markedly variable. Anticipation is not expected.

The often-cited ZSD cumulative incidence is approximately **1 in 50,000 births**, but this is for all causal PEX genes, not PEX13. PEX1 accounts for nearly two-thirds of ZSD, whereas PEX13 is exceptionally rare. A 2024 review found only 22 PEX13 cases worldwide; that count cannot be converted into incidence or prevalence because of underdiagnosis, publication bias, and unknown denominator. (su2024severezellwegerspectrum pages 4-6, bose2022characterizationofseverity pages 1-2)

Both sexes are affected; the 2022 series included three males and three females, consistent with autosomal inheritance rather than a sex effect. No reliable ethnicity-specific prevalence or carrier frequency is available. Reported families span Europe, the Middle East, North America, and China. Consanguinity increases the probability of homozygosity but is not required. (borgia2022genotype–phenotypecorrelationsand pages 6-9, borgia2022genotype–phenotypecorrelationsand pages 2-4)

## 10. Diagnostics

### Recommended workflow

1. **Clinical suspicion:** neonatal hypotonia/seizures/liver disease, or childhood developmental regression, spasticity, sensory impairment, and leukodystrophy.
2. **Biochemical testing:** plasma VLCFAs including C26:0, C24:0/C22:0 and C26:0/C22:0; C26:0-lysophosphatidylcholine where available; phytanic and pristanic acids; pipecolic acid; plasma/urine C27 bile-acid intermediates DHCA and THCA; erythrocyte plasmalogens; liver function and coagulation; ACTH/cortisol surveillance.
3. **Molecular confirmation:** a comprehensive peroxisomal/PBD multigene panel or trio WES/WGS with copy-number calling. Confirm candidate variants and segregation by Sanger sequencing or an orthogonal assay.
4. **Functional confirmation when needed:** fibroblast catalase/PTS1 immunofluorescence, matrix-import assay, plasmalogen synthesis, VLCFA oxidation, and complementation studies.

A critical caveat is that VLCFAs may be minimally abnormal or normal in some PEX13 patients despite severe neurologic disease; normal VLCFA alone must not exclude the diagnosis. (su2024severezellwegerspectrum pages 4-6, borgia2022genotype–phenotypecorrelationsand pages 13-15)

**Imaging and functional evaluation:** brain MRI for cortical malformation, delayed myelination/leukodystrophy, corpus-callosal, cerebellar, brainstem, or basal-ganglia abnormalities; EEG for seizures; BAEP/audiology; ophthalmologic examination, OCT, electroretinography and visual fields; renal and liver ultrasonography; echocardiography when indicated. MRI severity does not necessarily track clinical severity. (su2024severezellwegerspectrum pages 4-6, su2024severezellwegerspectrum pages 2-4)

**Genetic-test roles:** WES and panels are high-yield for sequence variants; WGS is useful for noncoding and structural variants and can improve deletion detection. CMA may detect large PEX13 deletions but is not a first-line standalone test for this recessive sequence disorder. Karyotype, FISH, mitochondrial DNA, and repeat-expansion tests have no routine role unless the phenotype suggests another diagnosis.

**Differential diagnoses:** other PEX-gene ZSDs; D-bifunctional protein deficiency/HSD17B4 disease; acyl-CoA oxidase-1 deficiency; X-linked adrenoleukodystrophy; rhizomelic chondrodysplasia punctata; isolated bile-acid synthesis disorders; mitochondrial encephalopathy; congenital disorders of glycosylation; and other leukodystrophies. Molecular testing is required because clinical and biochemical overlap is substantial.

There are no universally adopted PEX13-specific clinical criteria. Routine population newborn screening for ZSD/PBD11B is not established. C26:0-LPC and bile-acid-metabolite approaches are investigational screening possibilities.

## 11. Outcome and prognosis

PEX13-specific prognosis depends on residual function and cannot be summarized by a validated survival curve. Severe homozygous disease can lead to death in infancy; the 2024 p.Ala165Pro patient died at 14 months despite supportive care. Other patients survive into childhood with progressive spasticity, sensory loss, leukodystrophy, and dependence for mobility and daily activities. (borgia2022genotype–phenotypecorrelationsand pages 6-9, su2024severezellwegerspectrum pages 2-4)

For context only, a ZSD-wide cohort reported survival at age 0–1 years of **36.1% severe, 75.0% intermediate, and 95.8% mild**; at age 8–9 years it was **0%, 54.6%, and 85.6%**, respectively. In the severe natural-history group, 95.7% died by age two. These estimates must not be represented as PEX13-specific. (bose2022characterizationofseverity pages 12-13, bose2022characterizationofseverity pages 9-10)

Potential adverse prognostic indicators across ZSD include seizures, abnormal EEG, renal cortical microcysts, cardiac abnormalities, elevated C26:0, severe plasmalogen deficiency, feeding/respiratory compromise, and early multisystem involvement. In ZSD-wide modeling, C26:0 values of **1.08 μg/mL** and **5.18 μg/mL** marked equal predicted probabilities between mild/intermediate and intermediate/severe categories, respectively; these are research thresholds, not validated PBD11B clinical cutoffs. (bose2022characterizationofseverity pages 16-17)

## 12. Treatment

No curative or approved PEX13-specific disease-modifying treatment exists. Current care is multidisciplinary and supportive:

- seizures: individualized antiseizure medication, such as levetiracetam in the 2024 case;
- nutrition: feeding assessment, aspiration precautions, high-calorie support, gastrostomy/jejunostomy when appropriate, and fat-soluble-vitamin replacement if deficient;
- liver: liver tests, coagulation, bile acids, ultrasound, and management of cholestasis; ursodeoxycholic acid was used symptomatically in one case but is not proven to alter PBD11B progression;
- adrenal: periodic ACTH/cortisol assessment and glucocorticoid replacement if insufficiency is confirmed;
- hearing/vision: hearing aids or cochlear evaluation, low-vision services, refraction, retinal monitoring;
- motor/communication: physical, occupational, speech and augmentative-communication therapy; mobility and contracture-management devices; baclofen may be used for spasticity;
- respiratory/palliative care: secretion and aspiration management, ventilation when indicated, vaccinations and prompt infection treatment, and family-centered goals-of-care planning. (borgia2022genotype–phenotypecorrelationsand pages 6-9, su2024severezellwegerspectrum pages 2-4)

Suggested NCIt intervention concepts include Anticonvulsant Therapy, Enteral Nutrition, Gastrostomy, Physical Therapy, Occupational Therapy, Speech Therapy, Hearing Aid, Cochlear Implantation, Glucocorticoid Therapy, Mechanical Ventilation, and Palliative Care; current NCIt codes should be validated at ingestion.

**Evidence for proposed systemic therapies is weak:** a randomized DHA trial in ZSD showed no benefit; cholic-acid reports are conflicting; betaine and hydroxychloroquine/pexophagy inhibition remain experimental; and isolated liver-transplant reports cannot establish neurologic benefit or long-term survival. (bose2022characterizationofseverity pages 2-3)

Current ZSD/PBD studies are not PEX13-specific:

- **NCT06190626**, recruiting observational retinopathy study, target n=30, annual ophthalmic and peroxisomal assessments through an estimated 2029 completion. (NCT06190626 chunk 1)
- **NCT01668186**, recruiting longitudinal PBD natural-history study, listed enrollment 244.
- **NCT03440905**, completed caregiver symptom/QoL survey, n=92. (NCT03440905 chunk 1)
- **NCT03856866**, completed phase 2 hydroxychloroquine pexophagy study, n=3.
- **NCT01838941**, completed phase 3 betaine study, n=12.
- **NCT03115086**, active-not-recruiting Cholbam/cholic-acid registry, n=55.

No response rate can be assigned to PBD11B from these studies, and no gene therapy, CRISPR, RNA therapy, or cell therapy has reached established clinical use.

## 13. Prevention

The inherited biochemical defect cannot presently be prevented by lifestyle change, vaccination, or prophylactic medication.

**Primary prevention at family level:** genetic counseling, identification of both familial PEX13 alleles, carrier testing of adult relatives, partner testing where appropriate, preimplantation genetic testing for monogenic disease, and prenatal diagnosis by chorionic-villus sampling or amniocentesis. Donor gametes are another reproductive option.

**Secondary prevention:** cascade testing and early biochemical/molecular diagnosis in at-risk newborns or siblings. Population newborn screening is not standard. Early diagnosis supports seizure control, nutrition, sensory intervention, adrenal surveillance, and complication prevention.

**Tertiary prevention:** aspiration precautions, nutritional support, physiotherapy to limit contractures, seizure management, hearing/vision support, liver/renal/adrenal monitoring, immunization according to routine schedules, and rapid treatment of intercurrent illness.

## 14. Other species and natural disease

No well-documented naturally occurring veterinary counterpart specifically caused by biallelic PEX13 variants was identified. PBD11B is not infectious and has no zoonotic or cross-species transmission.

PEX13 and the peroxisomal import machinery are evolutionarily conserved across eukaryotes. Experimental orthologs include mouse **Pex13** (*Mus musculus*, NCBI Taxonomy 10090) and zebrafish **pex13** (*Danio rerio*, Taxonomy 7955). Conserved rescue is demonstrated by partial correction of the zebrafish phenotype with human PEX13 mRNA. (demers2023pex13preventspexophagy pages 6-7)

## 15. Model organisms

### Mouse

A constitutive **Pex13 knockout** reproduces major severe ZSD features: defective PTS1/PTS2 import, profound lipid abnormalities, hypotonia, failure to feed, cortical disorganization, neuronal degeneration, hepatic lipid droplets, abnormal mitochondrial cristae, delayed glomerular development, and neonatal death. Wild-type PEX13 complementation restores import in deficient cells. Its limitation is early lethality, which restricts study of later progressive disease. (jiang2025modellingperoxisomaldisorders pages 11-13, maxwell2003pex13inactivationin pages 6-8)

A brain-restricted conditional knockout survives postnatally—most died by approximately 35 days—and shows impaired cerebellar fissure/layer formation, granule-cell migration and Purkinje-layer development, motor/reflex deficits, astrogliosis, microgliosis, ROS elevation, mitochondrial dysfunction, and enhanced neuronal apoptosis. It models neurologic pathogenesis but not systemic liver/kidney disease.

A germ-cell-specific Pex13 knockout causes spermatogenic arrest at the round-spermatid stage and altered testicular lipids. This establishes a tissue-specific role but is not a full clinical PBD11B model.

### Zebrafish

CRISPR maternal-zygotic **pex13-null** zebrafish show matrix-import failure, reduced peroxisomes, hepatic lipid accumulation, and 90–95% mortality at 9–11 days post-fertilization. Chloroquine restores membrane-organelle counts but not matrix function, distinguishing enhanced pexophagy from the underlying import defect. Human PEX13 mRNA partially rescues hepatic phenotype. Advantages include live imaging and drug screening; limitations include maternal contribution, model-dependent survival, and species-specific lipid metabolism. (jiang2025modellingperoxisomaldisorders pages 11-13, demers2023pex13preventspexophagy pages 6-7)

### Cellular and structural models

Patient fibroblasts, HEK293/HeLa knockout or knockdown cells, FRET/co-immunoprecipitation systems, matrix-import reporters, and purified-protein NMR/crystallography are the most direct tools for allele-specific functional classification. They demonstrate peroxisome number/size changes, PEX13 self-association, PEX5 ubiquitination, pexophagy, and the FxxxF–SH3 interaction network, but cannot reproduce organ development or long-term neurodegeneration. (krause2013functionalanalysisof pages 1-2, demers2023pex13preventspexophagy pages 14-15, gaussmann2024modulationofperoxisomal pages 3-4)

## Key conclusions and knowledge gaps

PBD11B is an exceptionally rare, recessive **PEX13 matrix-import disorder** with a continuous phenotype from lethal infantile multisystem disease to progressive childhood neurologic disease. The strongest recent advances are the 2023 demonstration that PEX13 restrains ubiquitinated-PEX5/ROS-driven pexophagy and the 2024 structural definition of the PEX13 FxxxF–SH3–PEX5–PEX14 interaction network. (demers2023pex13preventspexophagy pages 14-15, gaussmann2024modulationofperoxisomal pages 3-4)

The most important database caveats are: (1) published case counts cannot support population prevalence or phenotype percentages; (2) normal VLCFA testing does not exclude PEX13 disease; (3) broad ZSD outcome statistics must not be treated as PEX13-specific; and (4) no intervention has yet demonstrated genotype-specific disease modification. Priority research needs include an international PEX13 registry, standardized longitudinal severity measures, variant-level functional assays, natural-history biomarkers, patient-derived neural/hepatic models, and therapies that restore matrix import without merely increasing nonfunctional peroxisomal membrane structures.

References

1. (su2024severezellwegerspectrum pages 1-2): Ling Su, Min‐Zhi Peng, Xiao‐Dan Chen, Shuang Wu, and Li Liu. Severe zellweger spectrum disorder due to a novel missense variant in the pex13 gene: a case report and the literature review. Molecular Genetics & Genomic Medicine, Nov 2024. URL: https://doi.org/10.1002/mgg3.2315, doi:10.1002/mgg3.2315. This article has 3 citations and is from a peer-reviewed journal.

2. (borgia2022genotype–phenotypecorrelationsand pages 1-2): Paola Borgia, Simona Baldassari, Nicoletta Pedemonte, Ebba Alkhunaizi, Gianluca D’Onofrio, Domenico Tortora, Elisa Calì, Paolo Scudieri, Ganna Balagura, Ilaria Musante, Maria Cristina Diana, Marina Pedemonte, Maria Stella Vari, Michele Iacomino, Antonella Riva, Roberto Chimenz, Giuseppe D. Mangano, Mohammad Hasan Mohammadi, Mehran Beiraghi Toosi, Farah Ashrafzadeh, Shima Imannezhad, Ehsan Ghayoor Karimiani, Andrea Accogli, Maria Cristina Schiaffino, Mohamad Maghnie, Miguel Angel Soler, Karl Echiverri, Charles K. Abrams, Pasquale Striano, Sara Fortuna, Reza Maroofian, Henry Houlden, Federico Zara, Chiara Fiorillo, and Vincenzo Salpietro. Genotype–phenotype correlations and disease mechanisms in pex13-related zellweger spectrum disorders. Orphanet Journal of Rare Diseases, Jul 2022. URL: https://doi.org/10.1186/s13023-022-02415-5, doi:10.1186/s13023-022-02415-5. This article has 8 citations and is from a peer-reviewed journal.

3. (su2024severezellwegerspectrum pages 4-6): Ling Su, Min‐Zhi Peng, Xiao‐Dan Chen, Shuang Wu, and Li Liu. Severe zellweger spectrum disorder due to a novel missense variant in the pex13 gene: a case report and the literature review. Molecular Genetics & Genomic Medicine, Nov 2024. URL: https://doi.org/10.1002/mgg3.2315, doi:10.1002/mgg3.2315. This article has 3 citations and is from a peer-reviewed journal.

4. (borgia2022genotype–phenotypecorrelationsand pages 6-9): Paola Borgia, Simona Baldassari, Nicoletta Pedemonte, Ebba Alkhunaizi, Gianluca D’Onofrio, Domenico Tortora, Elisa Calì, Paolo Scudieri, Ganna Balagura, Ilaria Musante, Maria Cristina Diana, Marina Pedemonte, Maria Stella Vari, Michele Iacomino, Antonella Riva, Roberto Chimenz, Giuseppe D. Mangano, Mohammad Hasan Mohammadi, Mehran Beiraghi Toosi, Farah Ashrafzadeh, Shima Imannezhad, Ehsan Ghayoor Karimiani, Andrea Accogli, Maria Cristina Schiaffino, Mohamad Maghnie, Miguel Angel Soler, Karl Echiverri, Charles K. Abrams, Pasquale Striano, Sara Fortuna, Reza Maroofian, Henry Houlden, Federico Zara, Chiara Fiorillo, and Vincenzo Salpietro. Genotype–phenotype correlations and disease mechanisms in pex13-related zellweger spectrum disorders. Orphanet Journal of Rare Diseases, Jul 2022. URL: https://doi.org/10.1186/s13023-022-02415-5, doi:10.1186/s13023-022-02415-5. This article has 8 citations and is from a peer-reviewed journal.

5. (krause2006identificationofnovel pages 3-4): Cindy Krause, Hendrik Rosewich, Melissa Thanos, and Jutta Gärtner. Identification of novel mutations in pex2, pex6, pex10, pex12, and pex13 in zellweger spectrum patients. Human Mutation, 27:1157-1157, Nov 2006. URL: https://doi.org/10.1002/humu.9462, doi:10.1002/humu.9462. This article has 61 citations and is from a domain leading peer-reviewed journal.

6. (krause2013functionalanalysisof pages 1-2): Cindy Krause, Hendrik Rosewich, Andrew Woehler, and Jutta Gärtner. Functional analysis of pex13 mutation in a zellweger syndrome spectrum patient reveals novel homooligomerization of pex13 and its role in human peroxisome biogenesis. Human molecular genetics, 22 19:3844-57, Oct 2013. URL: https://doi.org/10.1093/hmg/ddt238, doi:10.1093/hmg/ddt238. This article has 42 citations and is from a domain leading peer-reviewed journal.

7. (borgia2022genotype–phenotypecorrelationsand pages 11-13): Paola Borgia, Simona Baldassari, Nicoletta Pedemonte, Ebba Alkhunaizi, Gianluca D’Onofrio, Domenico Tortora, Elisa Calì, Paolo Scudieri, Ganna Balagura, Ilaria Musante, Maria Cristina Diana, Marina Pedemonte, Maria Stella Vari, Michele Iacomino, Antonella Riva, Roberto Chimenz, Giuseppe D. Mangano, Mohammad Hasan Mohammadi, Mehran Beiraghi Toosi, Farah Ashrafzadeh, Shima Imannezhad, Ehsan Ghayoor Karimiani, Andrea Accogli, Maria Cristina Schiaffino, Mohamad Maghnie, Miguel Angel Soler, Karl Echiverri, Charles K. Abrams, Pasquale Striano, Sara Fortuna, Reza Maroofian, Henry Houlden, Federico Zara, Chiara Fiorillo, and Vincenzo Salpietro. Genotype–phenotype correlations and disease mechanisms in pex13-related zellweger spectrum disorders. Orphanet Journal of Rare Diseases, Jul 2022. URL: https://doi.org/10.1186/s13023-022-02415-5, doi:10.1186/s13023-022-02415-5. This article has 8 citations and is from a peer-reviewed journal.

8. (gaussmann2024modulationofperoxisomal pages 3-4): Stefan Gaussmann, Rebecca Peschel, Julia Ott, Krzysztof M. Zak, Judit Sastre, Florent Delhommel, Grzegorz M. Popowicz, Job Boekhoven, Wolfgang Schliebs, Ralf Erdmann, and Michael Sattler. Modulation of peroxisomal import by the pex13 sh3 domain and a proximal fxxxf binding motif. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47605-w, doi:10.1038/s41467-024-47605-w. This article has 16 citations and is from a highest quality peer-reviewed journal.

9. (gaussmann2024modulationofperoxisomal pages 11-12): Stefan Gaussmann, Rebecca Peschel, Julia Ott, Krzysztof M. Zak, Judit Sastre, Florent Delhommel, Grzegorz M. Popowicz, Job Boekhoven, Wolfgang Schliebs, Ralf Erdmann, and Michael Sattler. Modulation of peroxisomal import by the pex13 sh3 domain and a proximal fxxxf binding motif. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47605-w, doi:10.1038/s41467-024-47605-w. This article has 16 citations and is from a highest quality peer-reviewed journal.

10. (gaussmann2024modulationofperoxisomal pages 1-2): Stefan Gaussmann, Rebecca Peschel, Julia Ott, Krzysztof M. Zak, Judit Sastre, Florent Delhommel, Grzegorz M. Popowicz, Job Boekhoven, Wolfgang Schliebs, Ralf Erdmann, and Michael Sattler. Modulation of peroxisomal import by the pex13 sh3 domain and a proximal fxxxf binding motif. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47605-w, doi:10.1038/s41467-024-47605-w. This article has 16 citations and is from a highest quality peer-reviewed journal.

11. (su2024severezellwegerspectrum pages 2-4): Ling Su, Min‐Zhi Peng, Xiao‐Dan Chen, Shuang Wu, and Li Liu. Severe zellweger spectrum disorder due to a novel missense variant in the pex13 gene: a case report and the literature review. Molecular Genetics & Genomic Medicine, Nov 2024. URL: https://doi.org/10.1002/mgg3.2315, doi:10.1002/mgg3.2315. This article has 3 citations and is from a peer-reviewed journal.

12. (borgia2022genotype–phenotypecorrelationsand pages 2-4): Paola Borgia, Simona Baldassari, Nicoletta Pedemonte, Ebba Alkhunaizi, Gianluca D’Onofrio, Domenico Tortora, Elisa Calì, Paolo Scudieri, Ganna Balagura, Ilaria Musante, Maria Cristina Diana, Marina Pedemonte, Maria Stella Vari, Michele Iacomino, Antonella Riva, Roberto Chimenz, Giuseppe D. Mangano, Mohammad Hasan Mohammadi, Mehran Beiraghi Toosi, Farah Ashrafzadeh, Shima Imannezhad, Ehsan Ghayoor Karimiani, Andrea Accogli, Maria Cristina Schiaffino, Mohamad Maghnie, Miguel Angel Soler, Karl Echiverri, Charles K. Abrams, Pasquale Striano, Sara Fortuna, Reza Maroofian, Henry Houlden, Federico Zara, Chiara Fiorillo, and Vincenzo Salpietro. Genotype–phenotype correlations and disease mechanisms in pex13-related zellweger spectrum disorders. Orphanet Journal of Rare Diseases, Jul 2022. URL: https://doi.org/10.1186/s13023-022-02415-5, doi:10.1186/s13023-022-02415-5. This article has 8 citations and is from a peer-reviewed journal.

13. (bose2022characterizationofseverity pages 1-2): Mousumi Bose, Christine Yergeau, Yasmin D’Souza, David D. Cuthbertson, Melisa J. Lopez, Alyssa K. Smolen, and Nancy E. Braverman. Characterization of severity in zellweger spectrum disorder by clinical findings: a scoping review, meta-analysis and medical chart review. Jun 2022. URL: https://doi.org/10.3390/cells11121891, doi:10.3390/cells11121891. This article has 49 citations.

14. (borgia2022genotype–phenotypecorrelationsand pages 13-15): Paola Borgia, Simona Baldassari, Nicoletta Pedemonte, Ebba Alkhunaizi, Gianluca D’Onofrio, Domenico Tortora, Elisa Calì, Paolo Scudieri, Ganna Balagura, Ilaria Musante, Maria Cristina Diana, Marina Pedemonte, Maria Stella Vari, Michele Iacomino, Antonella Riva, Roberto Chimenz, Giuseppe D. Mangano, Mohammad Hasan Mohammadi, Mehran Beiraghi Toosi, Farah Ashrafzadeh, Shima Imannezhad, Ehsan Ghayoor Karimiani, Andrea Accogli, Maria Cristina Schiaffino, Mohamad Maghnie, Miguel Angel Soler, Karl Echiverri, Charles K. Abrams, Pasquale Striano, Sara Fortuna, Reza Maroofian, Henry Houlden, Federico Zara, Chiara Fiorillo, and Vincenzo Salpietro. Genotype–phenotype correlations and disease mechanisms in pex13-related zellweger spectrum disorders. Orphanet Journal of Rare Diseases, Jul 2022. URL: https://doi.org/10.1186/s13023-022-02415-5, doi:10.1186/s13023-022-02415-5. This article has 8 citations and is from a peer-reviewed journal.

15. (bose2022characterizationofseverity pages 12-13): Mousumi Bose, Christine Yergeau, Yasmin D’Souza, David D. Cuthbertson, Melisa J. Lopez, Alyssa K. Smolen, and Nancy E. Braverman. Characterization of severity in zellweger spectrum disorder by clinical findings: a scoping review, meta-analysis and medical chart review. Jun 2022. URL: https://doi.org/10.3390/cells11121891, doi:10.3390/cells11121891. This article has 49 citations.

16. (bose2022characterizationofseverity pages 9-10): Mousumi Bose, Christine Yergeau, Yasmin D’Souza, David D. Cuthbertson, Melisa J. Lopez, Alyssa K. Smolen, and Nancy E. Braverman. Characterization of severity in zellweger spectrum disorder by clinical findings: a scoping review, meta-analysis and medical chart review. Jun 2022. URL: https://doi.org/10.3390/cells11121891, doi:10.3390/cells11121891. This article has 49 citations.

17. (NCT06190626 chunk 1): Nancy Braverman. Longitudinal Prospective Natural History Study of Retinopathy in Zellweger Spectrum Disorder. McGill University Health Centre/Research Institute of the McGill University Health Centre. 2023. ClinicalTrials.gov Identifier: NCT06190626

18. (bose2022characterizationofseverity pages 2-3): Mousumi Bose, Christine Yergeau, Yasmin D’Souza, David D. Cuthbertson, Melisa J. Lopez, Alyssa K. Smolen, and Nancy E. Braverman. Characterization of severity in zellweger spectrum disorder by clinical findings: a scoping review, meta-analysis and medical chart review. Jun 2022. URL: https://doi.org/10.3390/cells11121891, doi:10.3390/cells11121891. This article has 49 citations.

19. (jiang2025modellingperoxisomaldisorders pages 11-13): Chenxing S. Jiang and Michael Schrader. Modelling peroxisomal disorders in zebrafish. Jan 2025. URL: https://doi.org/10.3390/cells14020147, doi:10.3390/cells14020147. This article has 4 citations.

20. (bose2022characterizationofseverity pages 10-12): Mousumi Bose, Christine Yergeau, Yasmin D’Souza, David D. Cuthbertson, Melisa J. Lopez, Alyssa K. Smolen, and Nancy E. Braverman. Characterization of severity in zellweger spectrum disorder by clinical findings: a scoping review, meta-analysis and medical chart review. Jun 2022. URL: https://doi.org/10.3390/cells11121891, doi:10.3390/cells11121891. This article has 49 citations.

21. (NCT03440905 chunk 1):  Proxy-Reported Symptoms and Quality of Life Survey in Zellweger Spectrum Disorders. University of South Florida. 2018. ClinicalTrials.gov Identifier: NCT03440905

22. (demers2023pex13preventspexophagy pages 14-15): Nicholas D. Demers, Victoria Riccio, Doo Sin Jo, Sushil Bhandari, Kelsey B. Law, Weifang Liao, Choy Kim, G. Angus McQuibban, Seong-Kyu Choe, Dong-Hyung Cho, and Peter K. Kim. Pex13 prevents pexophagy by regulating ubiquitinated pex5 and peroxisomal ros. Jan 2023. URL: https://doi.org/10.1080/15548627.2022.2160566, doi:10.1080/15548627.2022.2160566. This article has 66 citations and is from a domain leading peer-reviewed journal.

23. (demers2023pex13preventspexophagy pages 6-7): Nicholas D. Demers, Victoria Riccio, Doo Sin Jo, Sushil Bhandari, Kelsey B. Law, Weifang Liao, Choy Kim, G. Angus McQuibban, Seong-Kyu Choe, Dong-Hyung Cho, and Peter K. Kim. Pex13 prevents pexophagy by regulating ubiquitinated pex5 and peroxisomal ros. Jan 2023. URL: https://doi.org/10.1080/15548627.2022.2160566, doi:10.1080/15548627.2022.2160566. This article has 66 citations and is from a domain leading peer-reviewed journal.

24. (maxwell2003pex13inactivationin pages 6-8): Megan Maxwell, Jonas Bjorkman, Tam Nguyen, Peter Sharp, John Finnie, Carol Paterson, Ian Tonks, Barbara C. Paton, Graham F. Kay, and Denis I. Crane. Pex13 inactivation in the mouse disrupts peroxisome biogenesis and leads to a zellweger syndrome phenotype. Molecular and Cellular Biology, 23:5947-5957, Aug 2003. URL: https://doi.org/10.1128/mcb.23.16.5947-5957.2003, doi:10.1128/mcb.23.16.5947-5957.2003. This article has 134 citations and is from a domain leading peer-reviewed journal.

25. (bose2022characterizationofseverity pages 16-17): Mousumi Bose, Christine Yergeau, Yasmin D’Souza, David D. Cuthbertson, Melisa J. Lopez, Alyssa K. Smolen, and Nancy E. Braverman. Characterization of severity in zellweger spectrum disorder by clinical findings: a scoping review, meta-analysis and medical chart review. Jun 2022. URL: https://doi.org/10.3390/cells11121891, doi:10.3390/cells11121891. This article has 49 citations.

## Artifacts

- [Edison artifact artifact-00](Peroxisome_Biogenesis_Disorder_11B-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005778` (1 mention) - the report calls it "GO cellular component: **peroxisomal membrane"; GO calls it **peroxisomal membrane**

Every term resolved, and every label the report gave matched.