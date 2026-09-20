---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T23:24:03.780700'
end_time: '2026-09-04T23:36:53.306540'
duration_seconds: 769.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Familial Expansile Osteolysis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
reference_validation:
  total_references: 11
  verified: 10
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.091
  relevance_assessed: 10
  on_topic: 3
  unresolved_references:
  - "DOI:10.1016/j.bone.2023.116698)\u2014described"
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 21
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Familial_Expansile_Osteolysis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Expansile Osteolysis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Expansile Osteolysis** covering all of the
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
- **Disease Name:** Familial Expansile Osteolysis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Expansile Osteolysis** covering all of the
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


# Familial Expansile Osteolysis: Disease-Characteristics Report

## Executive summary

Familial expansile osteolysis (FEO) is an ultrarare, autosomal-dominant, high-turnover skeletal dysplasia caused by heterozygous exon-1 duplications in **TNFRSF11A**, which encodes receptor activator of NF-κB (**RANK**). Its characteristic sequence is childhood hearing loss, destructive external resorption of permanent teeth, and later progressive focal osteolysis—principally of appendicular long bones—with expansion, pain, deformity, and pathological fracture. Clinical expression is highly variable, including among carriers of the recurrent 18-bp duplication. Most knowledge comes from a few extended pedigrees and case reports rather than registries or controlled trials. The most important recent clinical report, published in May 2023, suggests that early bisphosphonate treatment can suppress turnover and improve bone density, but also demonstrates a substantial risk of prolonged post-zoledronate hypocalcemia. (crone1990theradiographicfeatures pages 1-2, ralston2019rareinheritedforms pages 3-4, craven2023earlyidentificationof pages 3-4, whyte2004heritabledisordersof pages 14-14)

| Domain | Key facts | Evidence |
|---|---|---|
| Definition / identifier | Familial expansile osteolysis (FEO; **OMIM/MIM 174810**) is an ultrarare, progressive, Paget-like skeletal dysplasia characterized by high bone turnover, focal expansile osteolysis, early hearing loss, and permanent-tooth disease. Synonym: hereditary expansile polyostotic osteolytic dysplasia. | (whyte2004heritabledisordersof pages 1-2, whyte2004heritabledisordersofa pages 1-2, ralston2019rareinheritedforms pages 1-3) |
| Causal gene / canonical variant | **TNFRSF11A** (RANK; OMIM 603499), chromosome 18q21.1–q22. Classic FEO is associated with an in-frame exon-1 **18-bp tandem duplication**, legacy notation **84dup18**, which adds six amino acids to the RANK signal peptide. Molecular discovery: Hughes et al., 2000, PMID **10615125**, [DOI](https://doi.org/10.1038/71667). Other exon-1 duplications produce overlapping RANK-associated phenotypes. | (whyte2004heritabledisordersof pages 1-2, ralston2019rareinheritedforms pages 3-4, whyte2014juvenilepagetsdisease pages 14-15) |
| Inheritance | **Autosomal dominant**, caused by a heterozygous germline variant; multigenerational transmission and segregation are established. Penetrance was nearly complete in the Northern Ireland kindred but variable in other families; expression varies markedly even with the recurrent 18-bp duplication. De novo disease is possible, as shown for a related 12-bp RANK duplication. | (crone1990theradiographicfeatures pages 1-2, whyte2004heritabledisordersof pages 2-3, whyte2004heritabledisordersof pages 14-14, craven2023earlyidentificationof pages 3-4) |
| Hallmark phenotypes / frequencies | In the classic Northern Ireland cohort, hearing loss occurred in approximately **95%** and external root resorption/dental abnormalities in **94%**. Hearing loss may begin by age 4 or during the first–second decade and evolve from conductive to mixed loss. Permanent-tooth resorption, mobility, fracture, and premature loss commonly follow; deciduous teeth are typically spared. | (marik2006familialexpansileosteolysis—not pages 1-3, crone1990theradiographicfeatures pages 1-2, whyte2004heritabledisordersofa pages 2-3, whyte2006pagetsdiseaseof pages 4-6) |
| Lesions / progression | Progressive lytic lesions predominantly affect appendicular long bones—especially tibia, radius, fibula, humerus, and femur. Approximately **90%** were appendicular; expansion reached **3.5×** normal diameter. Lesions advanced **6.5–22.2 mm/year** (mean 13.3 mm/year); **12/97 lesions (12.4%)** fractured. Axial/skull disease is uncommon but documented. | (ralston2019rareinheritedforms pages 3-4, crone1990theradiographicfeatures pages 2-5, crone1990theradiographicfeatures pages 1-2, marik2006familialexpansileosteolysis—not pages 3-4) |
| Biochemical markers | Serum alkaline phosphatase and urinary hydroxyproline are commonly elevated; bone-specific ALP, osteocalcin, tartrate-resistant acid phosphatase, urinary deoxypyridinoline, and N-telopeptide may also be increased. Serum calcium, phosphate, and parathyroid hormone are usually normal before antiresorptive treatment. | (marik2006familialexpansileosteolysis—not pages 1-3, crone1990theradiographicfeatures pages 2-5, craven2023earlyidentificationof pages 1-3) |
| Mechanism certainty | **Demonstrated:** abnormal signal-peptide cleavage, reduced surface trafficking, intracellular/ER retention of mutant RANK, impaired RANKL responsiveness, osteoclast dysregulation, and high-turnover osteolysis. **Unresolved:** constitutive gain-of-function NF-κB signaling seen in overexpression systems was not reproduced with stable single-copy expression. A proposed ER-stress/unfolded-protein-response route to ligand-independent NF-κB activation remains incompletely established. | (alonso2021insertionmutationin pages 9-9, ralston2019rareinheritedforms pages 4-6, ralston2019rareinheritedforms pages 3-4, ralston2019rareinheritedforms pages 20-25) |
| Diagnosis | Diagnosis integrates the characteristic hearing–dental–skeletal phenotype, serum/urine turnover markers, radiographs, technetium bone scintigraphy, DXA, dental radiography/CBCT, temporal-bone CT/MRI, and confirmation of a heterozygous exon-1 **TNFRSF11A** duplication. Important differentials include ordinary Paget disease, expansile skeletal hyperphosphatasia, early-onset familial Paget disease, juvenile Paget disease, fibrous dysplasia, bone cysts, and tumors. | (whyte2006pagetsdiseaseof pages 6-10, craven2023earlyidentificationof pages 3-4, whyte2002familialexpansileosteolysis pages 13-15, craven2023earlyidentificationof pages 1-3) |
| Treatment evidence | Evidence is limited to case reports/series and a mouse model. Alendronate **40 mg/day for 5–6 months** mineralized early lesions and improved biochemical markers/osteopenia; one case gained **2.2% lumbar-spine** and **3.0% total-hip BMD**. In 2023, zoledronic acid **0.0125 mg/kg** caused prolonged hypocalcemia (nadir **6.8 mg/dL**), while alendronate **10 mg weekly** maintained marker suppression and improved spine BMD over 22 months. Deafness generally does not respond to bisphosphonates; hearing devices/cochlear implants and multidisciplinary dental/orthopedic care are used. [Whyte et al., PMID 11889411](https://pubmed.ncbi.nlm.nih.gov/11889411/); [Craven et al., DOI](https://doi.org/10.1016/j.bone.2023.116698). | (whyte2006pagetsdiseaseof pages 6-10, craven2023earlyidentificationof pages 3-4, whyte2002familialexpansileosteolysis pages 13-15, craven2023earlyidentificationof pages 1-3) |
| Evidence gaps | No reliable population prevalence, incidence, sex ratio, survival estimate, validated diagnostic criteria, disease-specific quality-of-life study, randomized treatment trial, approved FEO-specific therapy, prognostic model, protective variant, established environmental cause, pharmacogenomic guideline, or human single-cell/multi-omics dataset was identified. Long-term efficacy and optimal timing/dosing of antiresorptives remain unknown. | (marik2006familialexpansileosteolysis—not pages 1-3, whyte2006pagetsdiseaseof pages 6-10, ralston2019rareinheritedforms pages 1-3) |


*Table: Compact evidence summary of the genetic cause, hallmark manifestations, natural history, mechanism, diagnosis, treatment experience, and major knowledge gaps in familial expansile osteolysis.*

## 1. Disease information

**Definition.** FEO is a Mendelian, Paget-like disorder of osteoclast regulation characterized by generalized high bone turnover/osteopenia and progressive focal expansile osteolytic lesions. The classic phenotype includes early deafness, permanent-tooth root resorption and loss, and appendicular skeletal pain, fractures, expansion, and deformity. Advanced lesions can become thin-shelled and largely fat-filled. (whyte2004heritabledisordersof pages 1-2, whyte2004heritabledisordersofa pages 1-2)

**Identifiers and terminology**

- **OMIM/MIM:** 174810.
- **Causal gene:** *TNFRSF11A*, OMIM 603499; chromosome 18q21.1–q22.
- **MONDO:** a dedicated identifier could not be verified from the retrieved evidence and should be resolved directly against the current MONDO release rather than inferred.
- **Orphanet, MeSH, ICD-10/ICD-11:** no disease-specific identifiers were verified. In practice, coding may fall under broader osteolysis, skeletal dysplasia, or other specified bone-disease categories, but such mappings should not be treated as exact equivalents.
- **Synonyms:** familial expansile osteolysis; hereditary expansile polyostotic osteolytic dysplasia; FEO; “excessive RANK effect” in older literature. (whyte2004heritabledisordersof pages 1-2, whyte2004heritabledisordersofa pages 1-2)

The evidence is predominantly **aggregated disease-level literature derived from individual families and patients**, not population EHR data. The principal resources comprise a five-generation Northern Ireland pedigree, American, German, Spanish, and other small kindreds, and isolated cases. (crone1990theradiographicfeatures pages 1-2, whyte2004heritabledisordersof pages 2-3, whyte2004heritabledisordersof pages 14-14)

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is a heterozygous germline duplication within exon 1 of *TNFRSF11A*, altering the RANK signal peptide. Classic FEO is associated with a recurrent in-frame 18-bp duplication, conventionally reported as **84dup18**, adding six amino acids. Hughes et al. identified the molecular lesion in 2000: *Nature Genetics* 24:45–48, PMID **10615125**, [DOI 10.1038/71667](https://doi.org/10.1038/71667). (ralston2019rareinheritedforms pages 3-4, whyte2014juvenilepagetsdisease pages 14-15)

A 2023 patient with an overlapping, relatively mild RANK-duplication phenotype carried **NM_003839.3:c.52_63dup, p.(Cys18_Leu21dup)**; both parents tested negative, supporting a de novo event. This 12-bp allele should be annotated as part of the broader allelic RANK signal-peptide disorder spectrum rather than automatically equated with classic 84dup18 FEO. (craven2023earlyidentificationof pages 3-4)

### Risk factors and modifiers

- **Genetic:** carrying the pathogenic heterozygous duplication is the dominant risk. Family history confers a theoretical 50% transmission probability from a heterozygous affected parent.
- **Expressivity/modification:** severity varies markedly even for the recurrent 18-bp allele. The Spanish kindred had deafness, tooth loss, and osteoporosis but unusually few osteolytic lesions. Specific modifier genes have not been established. (whyte2004heritabledisordersof pages 14-14)
- **Environmental/mechanical:** trauma, fractures, surgery, and possibly pregnancy have coincided with lesion initiation or acceleration, but causality is based on observations rather than controlled evidence. Surgery appeared to accelerate extension across carpal or tarsal joints in two patients; one atypical case worsened after pregnancy and surgery. (crone1990theradiographicfeatures pages 5-6, whyte2006pagetsdiseaseof pages 6-10, marik2006familialexpansileosteolysis—not pages 3-4)
- **Protective factors:** no protective allele, diet, exposure, or lifestyle intervention is established. Bisphosphonates are secondary/tertiary preventive therapy, not protection from inheriting the disorder.
- **Gene–environment interaction:** a plausible model is that abnormal RANK-dependent remodeling renders bone unusually responsive to local mechanical injury, but this remains inferred.

No infectious cause, toxin, radiation exposure, smoking association, alcohol association, or occupational cause is supported.

## 3. Phenotypes

| Phenotype | Characteristics and frequency | Suggested HPO term |
|---|---|---|
| Hearing loss | Often earliest feature; reported as early as age 4 and usually in the first or second decade. Initially conductive, later mixed sensorineural. Approximately 95% in the classic Northern Ireland family. Fibrous replacement/necrosis of the incus is characteristic. | Hearing impairment **HP:0000365**; conductive hearing impairment **HP:0000405**; sensorineural hearing impairment **HP:0000407** |
| External tooth-root resorption | Permanent teeth show cervical/apical external resorption, mobility, fracture, pain, and premature loss, often beginning in adolescence; deciduous teeth generally spared. Dental abnormalities occurred in approximately 94% of screened classic-kindred patients. | Abnormality of dental root; premature loss of teeth **HP:0006480** |
| Focal expansile osteolysis | Usually begins at 15–45 years, although childhood onset and fracture at age 5 are documented. Progressive lysis, cortical thinning, expansion, deformity, and mechanical failure; variable severity. | Osteolysis **HP:0002797**; abnormal bone structure **HP:0011842** |
| Bone pain | Typically localized to active lesions; reported onset 18–44 years in the classic series. | Bone pain **HP:0002653** |
| Pathological fracture | Twelve fractures among 97 lesions (12.4%); fractures generally united normally. | Pathologic fracture **HP:0002756** |
| Limb deformity/bowing | Progressive, particularly tibial bowing and S-shaped deformity; expansion can reach 3.5 times normal diameter. | Bowing of the long bones **HP:0006487** |
| Osteopenia/osteoporosis | Generalized low mass and coarse or “fish-net” trabeculation, particularly in the American phenotype. | Osteopenia **HP:0000938**; osteoporosis **HP:0000939** |
| High bone turnover | Elevated ALP and urinary hydroxyproline; bone ALP, osteocalcin, TRAP, deoxypyridinoline, or N-telopeptide may also be high. Calcium, phosphate, and PTH are usually normal before treatment. | Elevated circulating alkaline phosphatase **HP:0003155** |

Clinical frequencies derive mainly from one family and should not be interpreted as population estimates. In another eight-person dataset, expansile lesions and early deafness each occurred in 75%, while early tooth loss occurred in 12.5%, illustrating variable expressivity. (marik2006familialexpansileosteolysis—not pages 1-3, ralston2019rareinheritedforms pages 3-4, crone1990theradiographicfeatures pages 1-2, whyte2006pagetsdiseaseof pages 4-6)

**Quality of life.** No FEO-specific EQ-5D, SF-36, PROMIS, or utility study was identified. Nevertheless, progressive deafness, tooth loss, pain, fractures, deformity, impaired mobility, dentures, and occasional major orthopedic procedures clearly impose substantial functional and psychosocial burdens. Severe disease has led to disability and amputation. (marik2006familialexpansileosteolysis—not pages 1-3, whyte2004heritabledisordersofa pages 2-3)

## 4. Genetic and molecular information

**Gene:** *TNFRSF11A* (HGNC symbol; RANK protein), encoding the receptor for RANKL and an essential regulator of osteoclast differentiation and survival.

**Variant class:** heterozygous, germline, in-frame tandem duplication affecting the N-terminal signal peptide. The classic allele is 84dup18 in legacy nomenclature. Available literature does not consistently provide transcript-normalized HGVS, ClinVar accession, or ACMG classification; therefore, database implementation should normalize each report against a defined current transcript before merging records. The variants are expected to be extremely rare/absent from general-population databases, but no verified gnomAD frequency was retrieved. (ralston2019rareinheritedforms pages 3-4, ralston2019rareinheritedforms pages 20-25)

Other signal-peptide duplications cause overlapping allelic disorders: 84dup15 (expansile skeletal hyperphosphatasia), 75dup27/78dup27 and related 27-bp alleles (early-onset Paget phenotypes), 87dup15 (juvenile Paget phenotype), and 90dup12 (panostotic expansile bone disease). This genotype–phenotype continuum cautions against assigning disease solely by duplication size. (ralston2019rareinheritedforms pages 20-25)

No established modifier gene, disease-specific epigenetic signature, pathogenic chromosomal rearrangement, somatic driver, or germline-repeat-expansion mechanism was identified.

## 5. Environmental information

FEO is not an environmentally caused or infectious disease. No reproducible toxin, pollutant, diet, exercise, smoking, or alcohol association exists. Mechanical trauma, fractures, orthopedic procedures, and orthodontic manipulation are possible local aggravators, while pregnancy-associated worsening is described in one case; all remain low-level observational evidence. Practical advice to avoid unnecessary skeletal/dental trauma is therefore precautionary rather than evidence from prevention trials. (crone1990theradiographicfeatures pages 5-6, whyte2006pagetsdiseaseof pages 6-10, marik2006familialexpansileosteolysis—not pages 3-4)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous exon-1 *TNFRSF11A* in-frame duplication **leads to** elongation of the RANK signal peptide.
2. Signal-peptide alteration **results in** defective cleavage and impaired trafficking of mutant RANK to the plasma membrane.
3. Defective trafficking **leads to** intracellular, particularly ER/organized smooth-ER, retention and reduced RANKL responsiveness; these steps are experimentally supported. (alonso2021insertionmutationin pages 9-9, ralston2019rareinheritedforms pages 3-4)
4. Intracellular mutant RANK **may lead to** ER stress/unfolded-protein-response-mediated, ligand-independent NF-κB activity; this branch is proposed, not conclusively demonstrated. Constitutive activation seen in transient overexpression was not reproduced with stable single-copy expression. (ralston2019rareinheritedforms pages 4-6, ralston2019rareinheritedforms pages 3-4, ralston2019rareinheritedforms pages 20-25)
5. In heterozygous osteoclast-lineage cells, altered RANK signaling **results in** impaired RANKL-induced formation but paradoxically prolonged osteoclast survival; the latter is demonstrated in the 75dup27 mouse model, not directly for every FEO allele. (alonso2021insertionmutationin pages 1-1)
6. Osteoclast dysregulation **leads to** excessive focal resorption and coupled high-turnover remodeling, reflected by elevated ALP/resorption markers and avid scintigraphic uptake.
7. Persistent resorption exceeding effective replacement **results in** trabecular and cortical loss, marrow fibrosis/vascularity, expansion, and eventual fatty replacement.
8. Structural failure **leads to** pain, bowing, deformity, and pathological fractures.
9. Parallel remodeling abnormalities in the middle-ear ossicles **lead to** early conductive and subsequently mixed deafness, while periodontal/dental-root resorption **leads to** premature permanent-tooth loss. (whyte2004heritabledisordersofa pages 2-3, whyte2006pagetsdiseaseof pages 4-6)

**Cells and pathways:** osteoclast precursors and mature osteoclasts are primary (**CL:0000778 osteoclast**); osteoblasts participate in coupled remodeling (**CL:0000062 osteoblast**). Suggested processes include GO:0030316 osteoclast differentiation, GO:0045453 bone resorption, GO:0046849 bone remodeling, GO:0031295 T-cell-independent?—not recommended here—and GO:0034976 response to endoplasmic-reticulum stress. Relevant signaling includes RANKL–RANK–TRAF6–NF-κB and downstream osteoclastogenesis.

Histology includes abundant osteoclasts and osteoblasts, giant bizarre multinucleated osteoclasts, woven trabeculae, fibrous/vascular marrow, scant matrix, and late fatty replacement. Unlike ordinary Paget disease, a mosaic pattern is uncommon. Historical “viral-like inclusions” in osteoclast nuclei are not evidence of an infectious etiology. (whyte2004heritabledisordersof pages 1-2, crone1990theradiographicfeatures pages 2-5, crone1990theradiographicfeatures pages 5-6)

No FEO-specific human transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omics dataset was identified.

## 7. Anatomical structures affected

The principal system is the skeleton/connective tissue. Approximately 90% of classic lesions were appendicular. Common sites are tibia, radius, fibula, humerus, and femur; lower-limb and distal-to-knee involvement is prominent. Suggested terms include UBERON:0000979 hindlimb, UBERON:0000978 forelimb, and the corresponding individual long-bone terms. (ralston2019rareinheritedforms pages 3-4, crone1990theradiographicfeatures pages 2-5)

Secondary sites include permanent teeth/roots, periodontal structures, temporal bone, and auditory ossicles—especially the incus. Pelvis, spine, skull, ribs, mandible, and girdles are less often affected but cannot be considered universally spared. Right-sided lesions were more frequent in one series (60 right versus 37 left), but bilateral tibial disease became common with age. (crone1990theradiographicfeatures pages 2-5, crone1990theradiographicfeatures pages 5-6)

At tissue level, cortical and trabecular bone and marrow are affected. At subcellular level, the RANK secretory pathway implicates the ER, Golgi, plasma membrane, and NF-κB signaling machinery.

## 8. Temporal development

The usual sequence is insidious childhood hearing impairment, adolescent permanent-tooth disease, and focal skeletal disease from adolescence or adulthood. Bone pain began at 18–44 years and focal radiographic disease at 15–45 years in the classic cohort. Lesions progressed linearly at 6.5–22.2 mm/year, mean 13.3 mm/year, through lytic, expansile, and deforming/mechanical-failure phases. (crone1990theradiographicfeatures pages 2-5, crone1990theradiographicfeatures pages 1-2)

The course is chronic and lifelong, but site-specific activity can become “burnt out.” Childhood onset is documented: one patient fractured at 5, had relative quiescence from 9 to pregnancy at 20, and later accelerated disease. Scintigraphy may become abnormal before radiographs, defining a potential window for monitoring and antiresorptive intervention. No reliable spontaneous-remission rate exists. (crone1990theradiographicfeatures pages 2-5, marik2006familialexpansileosteolysis—not pages 3-4)

## 9. Inheritance and population

Inheritance is autosomal dominant with variable expressivity and probably age-dependent penetrance. The Northern Ireland kindred showed near-complete penetrance: 40 of 90 examined family members were affected, while 51 children of unaffected parents had no signs. Published estimates include 46 affected individuals over five generations in that kindred and 20 affected individuals across four generations in the Spanish family. (crone1990theradiographicfeatures pages 1-2, whyte2004heritabledisordersof pages 2-3, whyte2004heritabledisordersof pages 14-14)

FEO has been reported in Northern Irish, German, American, Spanish, Czech, Australian, and other patients, but the literature remains too sparse for prevalence, incidence, carrier-frequency, sex-ratio, ethnic-risk, or geographic-rate estimates. A 2006 report stated that only three kinships and two unrelated American individuals had been recognized worldwide at that time. No convincing anticipation, founder effect, consanguinity effect, or germline mosaicism rate is established. De novo mutation is biologically and clinically possible. (marik2006familialexpansileosteolysis—not pages 1-3, craven2023earlyidentificationof pages 3-4)

## 10. Diagnostics

### Recommended approach

1. Recognize the combination of early hearing loss, permanent-tooth external root resorption, elevated turnover, and appendicular expansile osteolysis.
2. Measure serum total/bone-specific ALP, calcium, phosphate, creatinine, PTH, and 25-hydroxyvitamin D; consider osteocalcin and serum/urine resorption markers.
3. Obtain targeted radiographs and whole-body technetium bone scintigraphy; use DXA to quantify generalized low bone mass.
4. Perform panoramic dental imaging or CBCT and formal audiology; temporal-bone CT/MRI may define ossicular/inner-ear pathology.
5. Confirm a heterozygous exon-1 *TNFRSF11A* duplication by sequencing with duplication-sensitive analysis and parental/segregation testing. (craven2023earlyidentificationof pages 3-4, craven2023earlyidentificationof pages 1-3)

Single-gene sequencing or a high-turnover bone-dysplasia/Paget panel is efficient when the phenotype is typical. Exome or genome sequencing is appropriate for atypical or panel-negative disease, provided the pipeline detects small tandem duplications. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not first-line tests for classic FEO. No validated RNA, proteomic, metabolomic, epigenomic, or liquid-biopsy diagnostic exists.

**Differential diagnosis:** ordinary Paget disease; early-onset familial Paget disease; expansile skeletal hyperphosphatasia; juvenile Paget disease due to *TNFRSF11B*; panostotic expansile bone disease; fibrous dysplasia; primary bone cysts/tumors; giant-cell lesions; and other hereditary osteolysis syndromes. FEO favors early deafness/root resorption, appendicular advancing lysis without the later dominant sclerotic phase of ordinary Paget disease, and a signal-peptide *TNFRSF11A* duplication. (whyte2006pagetsdiseaseof pages 6-10, craven2023earlyidentificationof pages 3-4, whyte2002familialexpansileosteolysis pages 13-15)

No consensus society diagnostic criteria or population/newborn-screening program exists. Cascade molecular testing is appropriate for at-risk relatives.

## 11. Outcome and prognosis

No survival curve, disease-specific mortality rate, or life-expectancy estimate is available. Morbidity is driven by progressive deafness, tooth loss, pain, deformity, osteoporosis, and fracture. Fractures generally heal, but advanced lesions may be refractory to antiresorptives and can cause profound disability. (crone1990theradiographicfeatures pages 2-5, whyte2006pagetsdiseaseof pages 6-10)

Osteosarcoma has been reported in association with FEO, including metastatic osteosarcoma in one family and a 17-year-old case, but the absolute risk is unknown and causal enrichment cannot be inferred from isolated reports. Any new persistent pain, enlarging mass, or destructive radiographic change warrants urgent oncologic assessment. (whyte2006pagetsdiseaseof pages 4-6)

Probable adverse prognostic features are early skeletal onset, rapid lesion extension, multifocal disease, fracture/deformity, very high turnover, and late fat-filled lesions. These have not been validated in a prognostic model.

## 12. Treatment and real-world implementation

There is no approved disease-specific or curative therapy and no randomized FEO trial. Management is multidisciplinary.

### Antiresorptives

Bisphosphonates are the best-supported pharmacotherapy (**NCIT: Bisphosphonate; Alendronate; Pamidronate; Zoledronic Acid**). Historical calcitonin reduced symptoms without clear radiographic benefit; dichloromethylene diphosphonate was ineffective, and pamidronate produced variable benefit. Oral alendronate 40 mg/day for 5–6 months was associated with early-lesion mineralization, biochemical normalization, and improved osteopenia; one patient gained 2.2% lumbar-spine and 3.0% total-hip BMD, with effects persisting up to two years in some observations. Established deafness did not improve. (whyte2006pagetsdiseaseof pages 6-10, whyte2002familialexpansileosteolysis pages 13-15)

The leading recent report—Craven et al., *Bone*, published May 2023, [DOI 10.1016/j.bone.2023.116698](https://doi.org/10.1016/j.bone.2023.116698)—described a 10-year-old girl with a de novo 12-bp RANK duplication. Zoledronic acid 0.0125 mg/kg caused prolonged asymptomatic hypocalcemia, nadir 6.8 mg/dL at 2.5 days despite calcium 700 mg three times daily and calcitriol 0.5 μg twice daily. Subsequent alendronate 10 mg weekly maintained marker suppression and improved spinal BMD over 22 months; no pain, fracture, deformity, or focal lesion developed, although dental resorption persisted. This supports early intervention but remains one case with an overlapping allelic phenotype, not proof of FEO disease modification. (craven2023earlyidentificationof pages 6-8, craven2023earlyidentificationof pages 3-4)

Before potent antiresorptives, correct vitamin-D/calcium deficiency, assess renal function, and plan intensive calcium monitoring. The hypocalcemia resembles a high-turnover “hungry-bone” response.

### Hearing, dental, orthopedic, and supportive care

Hearing aids, ossicular surgery in selected conductive disease, and cochlear implantation are used. Bilateral cochlear implantation at 34 months was successful in the 2023 patient. Dental care should emphasize surveillance of permanent-root resorption, preservation where feasible, prosthodontics, and caution with orthodontic force or invasive surgery. Orthopedic management includes fracture care, stabilization/correction of deformity, mobility support, analgesia, and physical/occupational therapy. (craven2023earlyidentificationof pages 3-4, whyte2002familialexpansileosteolysis pages 13-15)

Denosumab, RANK/RANKL-targeted drugs, gene therapy, cell therapy, CRISPR, and RNA therapy are not established for FEO. Intracellular retention of mutant RANK raises a theoretical concern that extracellular RANKL blockade may not correct all abnormal signaling. No FEO-specific NCT study was found. (whyte2014juvenilepagetsdisease pages 11-14, ralston2019rareinheritedforms pages 1-3)

## 13. Prevention

Primary prevention by lifestyle or immunization is not applicable. Reproductive options following molecular diagnosis include genetic counseling, prenatal diagnosis, and preimplantation genetic testing; these prevent transmission or enable informed reproductive decisions but do not alter an affected embryo’s biology.

Secondary prevention comprises cascade testing, childhood audiology and dental surveillance, turnover-marker measurement, scintigraphy/radiography when indicated, and early specialist assessment before irreversible skeletal damage. Tertiary prevention includes antiresorptive control of turnover, calcium/vitamin-D optimization, fall and trauma reduction, prompt fracture treatment, hearing rehabilitation, dental preservation, and deformity management. Trauma/orthodontic precautions are reasonable but supported only by observational evidence. (crone1990theradiographicfeatures pages 5-6, whyte2006pagetsdiseaseof pages 6-10, craven2023earlyidentificationof pages 1-3)

## 14. Other species and natural disease

No naturally occurring veterinary syndrome convincingly established as the direct orthologue of human FEO was identified. Accordingly, no breed association, VBO term, zoonotic potential, or cross-species transmission applies. *TNFRSF11A* is evolutionarily conserved; the relevant experimental orthologue is murine *Tnfrsf11a*. FEO is genetic and noncommunicable.

## 15. Model organisms

The most informative model is a genetically engineered mouse carrying the human-disease-related **Tnfrsf11a 75dup27** insertion. Heterozygous mice developed age-dependent, Paget-like focal hind-limb osteolytic lesions by approximately 12 months. Their marrow showed impaired RANKL-induced osteoclast formation/signaling but increased osteoclast survival independent of RANKL. Zoledronic acid completely prevented lesion development. Homozygous mice instead had congenital osteopetrosis, metaphyseal widening, sclerosis, retained mineralized cartilage, absent osteoclasts, and failure of marrow cells to form osteoclasts after RANKL plus M-CSF. [Alonso et al., March 2021, DOI 10.1002/jbmr.4288](https://doi.org/10.1002/jbmr.4288). (alonso2021insertionmutationin pages 9-9, alonso2021insertionmutationin pages 1-1)

This model recapitulates age-dependent focal osteolysis and demonstrates a preventive antiresorptive effect, but it models a 27-bp early-onset Paget allele rather than classic FEO 84dup18. Its paradoxical homozygous osteopetrosis also shows that simple “constitutive RANK gain of function” is inadequate as a universal mechanistic explanation.

## Evidence appraisal and research gaps

The foundational evidence is human clinical and pedigree-based, including the molecular discovery (PMID **10615125**), five-generation American characterization (PMID **11889411**), allelic expansile skeletal hyperphosphatasia study (PMID **11771666**), Spanish family study (PMID **12362049**), two unrelated FEO cases (PMID **12568416**), dental report (PMID **10509339**), and incus-necrosis report (PMID **8643278**). (whyte2014juvenilepagetsdisease pages 14-15, whyte2014juvenilepagetsdisease pages 15-16)

A representative primary-paper abstract describes FEO as a “rare autosomal dominant disorder characterized by striking focal expansile osteolytic bone lesions and generalized osteopenia,” often with early hearing loss and dental disease. That wording accurately summarizes the phenotype but should not obscure substantial interfamily variability. The major expert conclusion from recent mechanistic work is that defective RANK processing and osteoclast dysregulation are established, whereas the precise route from intracellular mutant receptor to focal hyperresorption remains unresolved. (ralston2019rareinheritedforms pages 4-6, ralston2019rareinheritedforms pages 3-4, craven2023earlyidentificationof pages 6-8)

Critical gaps include reliable prevalence and natural-history registries, standardized phenotype/variant curation, prospective pediatric surveillance, disease-specific quality-of-life measurement, direct studies of classic 84dup18 osteoclasts, biomarkers predicting lesion onset, and controlled comparisons of oral versus intravenous antiresorptive regimens. No substantial FEO-specific 2024 clinical or omics study was identified; the May 2023 report remains the most directly relevant recent clinical development.

References

1. (crone1990theradiographicfeatures pages 1-2): MalcolmD. Crone and RichardG.H. Wallace. The radiographic features of familial expansile osteolysis. Skeletal Radiology, 19:245-250, May 1990. URL: https://doi.org/10.1007/bf00191665, doi:10.1007/bf00191665. This article has 43 citations and is from a peer-reviewed journal.

2. (ralston2019rareinheritedforms pages 3-4): Stuart H. Ralston and J. Paul Taylor. Rare inherited forms of paget’s disease and related syndromes. Calcified Tissue International, 104:501-516, Feb 2019. URL: https://doi.org/10.1007/s00223-019-00520-5, doi:10.1007/s00223-019-00520-5. This article has 40 citations and is from a peer-reviewed journal.

3. (craven2023earlyidentificationof pages 3-4): Meghan Craven, Mary Ellen Vajravelu, Karuna V. Shekdar, Michael A. Levine, Steven Mumm, Michael P. Whyte, and Edna E. Mancilla. Early identification of a 12-bp tandem duplication in tnfrsf11a encoding receptor activator of nuclear factor-kappa b (rank): clinical characterization and response to bisphosphonate therapy. Bone, 170:116698, May 2023. URL: https://doi.org/10.1016/j.bone.2023.116698, doi:10.1016/j.bone.2023.116698. This article has 5 citations and is from a domain leading peer-reviewed journal.

4. (whyte2004heritabledisordersof pages 14-14): MP Whyte and S Mumm. Heritable disorders of the rankl/opg/rank signaling pathway. Unknown journal, 2004.

5. (whyte2004heritabledisordersof pages 1-2): MP Whyte and S Mumm. Heritable disorders of the rankl/opg/rank signaling pathway. Unknown journal, 2004.

6. (whyte2004heritabledisordersofa pages 1-2): MP Whyte and S Mumm. Heritable disorders of the rankl/opg/rank signaling pathway. Unknown journal, 2004.

7. (ralston2019rareinheritedforms pages 1-3): Stuart H. Ralston and J. Paul Taylor. Rare inherited forms of paget’s disease and related syndromes. Calcified Tissue International, 104:501-516, Feb 2019. URL: https://doi.org/10.1007/s00223-019-00520-5, doi:10.1007/s00223-019-00520-5. This article has 40 citations and is from a peer-reviewed journal.

8. (whyte2014juvenilepagetsdisease pages 14-15): Michael P. Whyte, Cristina Tau, William H. McAlister, Xiafang Zhang, Deborah V. Novack, Virginia Preliasco, Eduardo Santini-Araujo, and Steven Mumm. Juvenile paget's disease with heterozygous duplication within tnfrsf11a encoding rank. Bone, 68:153-61, Nov 2014. URL: https://doi.org/10.1016/j.bone.2014.07.019, doi:10.1016/j.bone.2014.07.019. This article has 63 citations and is from a domain leading peer-reviewed journal.

9. (whyte2004heritabledisordersof pages 2-3): MP Whyte and S Mumm. Heritable disorders of the rankl/opg/rank signaling pathway. Unknown journal, 2004.

10. (marik2006familialexpansileosteolysis—not pages 1-3): I. Marik, A. Maříková, E. Hyánková, and K. Kozłowski. Familial expansile osteolysis—not exclusively an adult disorder. Skeletal Radiology, 35:872-875, Feb 2006. URL: https://doi.org/10.1007/s00256-005-0077-x, doi:10.1007/s00256-005-0077-x. This article has 19 citations and is from a peer-reviewed journal.

11. (whyte2004heritabledisordersofa pages 2-3): MP Whyte and S Mumm. Heritable disorders of the rankl/opg/rank signaling pathway. Unknown journal, 2004.

12. (whyte2006pagetsdiseaseof pages 4-6): MICHAEL P. WHYTE. Paget's disease of bone and genetic disorders of rankl/opg/rank/nf‐κb signaling. Annals of the New York Academy of Sciences, 1068:143-164, Apr 2006. URL: https://doi.org/10.1196/annals.1346.016, doi:10.1196/annals.1346.016. This article has 128 citations and is from a peer-reviewed journal.

13. (crone1990theradiographicfeatures pages 2-5): MalcolmD. Crone and RichardG.H. Wallace. The radiographic features of familial expansile osteolysis. Skeletal Radiology, 19:245-250, May 1990. URL: https://doi.org/10.1007/bf00191665, doi:10.1007/bf00191665. This article has 43 citations and is from a peer-reviewed journal.

14. (marik2006familialexpansileosteolysis—not pages 3-4): I. Marik, A. Maříková, E. Hyánková, and K. Kozłowski. Familial expansile osteolysis—not exclusively an adult disorder. Skeletal Radiology, 35:872-875, Feb 2006. URL: https://doi.org/10.1007/s00256-005-0077-x, doi:10.1007/s00256-005-0077-x. This article has 19 citations and is from a peer-reviewed journal.

15. (craven2023earlyidentificationof pages 1-3): Meghan Craven, Mary Ellen Vajravelu, Karuna V. Shekdar, Michael A. Levine, Steven Mumm, Michael P. Whyte, and Edna E. Mancilla. Early identification of a 12-bp tandem duplication in tnfrsf11a encoding receptor activator of nuclear factor-kappa b (rank): clinical characterization and response to bisphosphonate therapy. Bone, 170:116698, May 2023. URL: https://doi.org/10.1016/j.bone.2023.116698, doi:10.1016/j.bone.2023.116698. This article has 5 citations and is from a domain leading peer-reviewed journal.

16. (alonso2021insertionmutationin pages 9-9): Nerea Alonso, Sachin Wani, Lorraine Rose, Rob J. van't Hof, Stuart H. Ralston, and Omar M.E. Albagha. Insertion mutation in tnfrsf11a causes a paget's disease–like phenotype in heterozygous mice and osteopetrosis in homozygous mice. Journal of Bone and Mineral Research, 36:1376-1386, Mar 2021. URL: https://doi.org/10.1002/jbmr.4288, doi:10.1002/jbmr.4288. This article has 15 citations and is from a highest quality peer-reviewed journal.

17. (ralston2019rareinheritedforms pages 4-6): Stuart H. Ralston and J. Paul Taylor. Rare inherited forms of paget’s disease and related syndromes. Calcified Tissue International, 104:501-516, Feb 2019. URL: https://doi.org/10.1007/s00223-019-00520-5, doi:10.1007/s00223-019-00520-5. This article has 40 citations and is from a peer-reviewed journal.

18. (ralston2019rareinheritedforms pages 20-25): Stuart H. Ralston and J. Paul Taylor. Rare inherited forms of paget’s disease and related syndromes. Calcified Tissue International, 104:501-516, Feb 2019. URL: https://doi.org/10.1007/s00223-019-00520-5, doi:10.1007/s00223-019-00520-5. This article has 40 citations and is from a peer-reviewed journal.

19. (whyte2006pagetsdiseaseof pages 6-10): MICHAEL P. WHYTE. Paget's disease of bone and genetic disorders of rankl/opg/rank/nf‐κb signaling. Annals of the New York Academy of Sciences, 1068:143-164, Apr 2006. URL: https://doi.org/10.1196/annals.1346.016, doi:10.1196/annals.1346.016. This article has 128 citations and is from a peer-reviewed journal.

20. (whyte2002familialexpansileosteolysis pages 13-15): MICHAEL P. WHYTE, WILLIAM R. REINUS, MICHELLE N. PODGORNIK, and BARBARA G. MILLS. Familial expansile osteolysis (excessive rank effect) in a 5-generation american kindred. Medicine, 81:101-121, Mar 2002. URL: https://doi.org/10.1097/00005792-200203000-00002, doi:10.1097/00005792-200203000-00002. This article has 54 citations and is from a peer-reviewed journal.

21. (crone1990theradiographicfeatures pages 5-6): MalcolmD. Crone and RichardG.H. Wallace. The radiographic features of familial expansile osteolysis. Skeletal Radiology, 19:245-250, May 1990. URL: https://doi.org/10.1007/bf00191665, doi:10.1007/bf00191665. This article has 43 citations and is from a peer-reviewed journal.

22. (alonso2021insertionmutationin pages 1-1): Nerea Alonso, Sachin Wani, Lorraine Rose, Rob J. van't Hof, Stuart H. Ralston, and Omar M.E. Albagha. Insertion mutation in tnfrsf11a causes a paget's disease–like phenotype in heterozygous mice and osteopetrosis in homozygous mice. Journal of Bone and Mineral Research, 36:1376-1386, Mar 2021. URL: https://doi.org/10.1002/jbmr.4288, doi:10.1002/jbmr.4288. This article has 15 citations and is from a highest quality peer-reviewed journal.

23. (craven2023earlyidentificationof pages 6-8): Meghan Craven, Mary Ellen Vajravelu, Karuna V. Shekdar, Michael A. Levine, Steven Mumm, Michael P. Whyte, and Edna E. Mancilla. Early identification of a 12-bp tandem duplication in tnfrsf11a encoding receptor activator of nuclear factor-kappa b (rank): clinical characterization and response to bisphosphonate therapy. Bone, 170:116698, May 2023. URL: https://doi.org/10.1016/j.bone.2023.116698, doi:10.1016/j.bone.2023.116698. This article has 5 citations and is from a domain leading peer-reviewed journal.

24. (whyte2014juvenilepagetsdisease pages 11-14): Michael P. Whyte, Cristina Tau, William H. McAlister, Xiafang Zhang, Deborah V. Novack, Virginia Preliasco, Eduardo Santini-Araujo, and Steven Mumm. Juvenile paget's disease with heterozygous duplication within tnfrsf11a encoding rank. Bone, 68:153-61, Nov 2014. URL: https://doi.org/10.1016/j.bone.2014.07.019, doi:10.1016/j.bone.2014.07.019. This article has 63 citations and is from a domain leading peer-reviewed journal.

25. (whyte2014juvenilepagetsdisease pages 15-16): Michael P. Whyte, Cristina Tau, William H. McAlister, Xiafang Zhang, Deborah V. Novack, Virginia Preliasco, Eduardo Santini-Araujo, and Steven Mumm. Juvenile paget's disease with heterozygous duplication within tnfrsf11a encoding rank. Bone, 68:153-61, Nov 2014. URL: https://doi.org/10.1016/j.bone.2014.07.019, doi:10.1016/j.bone.2014.07.019. This article has 63 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Familial_Expansile_Osteolysis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 3 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1016/j.bone.2023.116698)—described` (1 mention) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.