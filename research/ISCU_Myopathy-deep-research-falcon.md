---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T23:23:58.773148'
end_time: '2026-09-04T23:34:02.053059'
duration_seconds: 603.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ISCU Myopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:23933728
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 52
  verified: 48
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: NCIT:C15368
    ontology_label: Treatment
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
  path: ISCU_Myopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ISCU Myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ISCU Myopathy** covering all of the
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
- **Disease Name:** ISCU Myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ISCU Myopathy** covering all of the
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


# ISCU Myopathy: Comprehensive Disease-Characteristics Report

**Scope and evidence date.** This report synthesizes retrieved literature through 2024. ISCU myopathy is ultra-rare; consequently, much of the evidence consists of Northern Swedish families, isolated case reports, patient muscle/cell studies, and engineered yeast or mouse systems rather than large cohorts. Frequencies, penetrance estimates, survival statistics, and treatment-response rates are generally unavailable. No disease-specific interventional trial was identified in the ClinicalTrials.gov search.

## Executive summary

ISCU myopathy is principally an autosomal-recessive mitochondrial metabolic myopathy caused by deficient function of the iron–sulfur-cluster scaffold protein ISCU. Classical disease is strongly associated with the Northern Swedish founder variant **ISCU c.418+382G>C**, which activates cryptic splicing and causes muscle-predominant pseudoexon inclusion. Hallmarks are childhood-onset severe exercise intolerance, exertional tachycardia and dyspnea, lactic acidosis, and episodes of rhabdomyolysis/myoglobinuria. Muscle demonstrates profound succinate-dehydrogenase and aconitase deficiency and mitochondrial iron accumulation. No approved disease-modifying therapy exists; a splice-switching antisense oligonucleotide has corrected molecular and metabolic defects in patient cells but has not entered demonstrated clinical use. (mochel2008splicemutationin pages 1-2, selvanathan2022mitochondrialironsulfurcluster pages 3-4, holmeshampton2016useofantisense pages 1-2, holmeshampton2016useofantisense pages 7-7)

The following table is a compact knowledge-base-ready summary; the narrative thereafter provides qualifications and mechanistic detail.

| Knowledge-base field | Curated ISCU-myopathy entry | Ontology suggestions | Evidence type and key references |
|---|---|---|---|
| Disease identity and identifiers | **Hereditary myopathy with lactic acidosis due to ISCU deficiency**; synonyms: **ISCU myopathy**, **iron–sulfur cluster deficiency myopathy**, **Swedish myopathy**, **myopathy with deficiency of succinate dehydrogenase and aconitase**. **MONDO:** MONDO:0009706; **OMIM phenotype:** #255125. Dedicated ICD-10/ICD-11 and MeSH disease codes were not identified; broader mitochondrial/metabolic-myopathy coding is required. Information is aggregated disease-level evidence derived from published patients, families, biopsies, and experimental models—not individual EHR data. | MONDO:0009706 | Curated disease–gene association and human genetic studies (OpenTargets Search: ISCU myopathy-ISCU, mochel2008splicemutationin pages 1-2, selvanathan2022mitochondrialironsulfurcluster pages 3-4). Mochel et al., 2008, PMID:18296749, DOI:10.1016/j.ajhg.2007.12.012. |
| Causal gene and inheritance | **ISCU** (iron–sulfur cluster assembly enzyme; OMIM *611911; Ensembl ENSG00000136003), encoding the mitochondrial scaffold on which nascent Fe–S clusters are assembled. Classical Swedish disease is **autosomal recessive**. A single **de novo heterozygous** p.Gly96Val case supports a possible dominant-negative form, but dominant inheritance remains **provisional** because independent cases are lacking. | GO:0016226 iron–sulfur cluster assembly; GO:0005739 mitochondrion | Human pedigrees, patient tissue, and yeast functional validation (OpenTargets Search: ISCU myopathy-ISCU, selvanathan2022mitochondrialironsulfurcluster pages 3-4, legati2017anovelde pages 1-2, legati2017anovelde pages 5-7). Legati et al., 2017, PMID:29079705, DOI:10.1136/jmedgenet-2017-104822. |
| Principal pathogenic variants | **c.418+382G>C** (historically g.7044G>C or IVS5+382G>C): deep-intronic Northern Swedish founder variant; strengthens a cryptic splice acceptor, inserts pseudoexon 4A, creates a premature stop, and markedly lowers functional ISCU in muscle. **c.149G>A (p.Gly50Glu):** recessive missense allele reported in compound heterozygosity with the founder variant. **p.Gly96Val:** heterozygous de novo missense variant with yeast-supported dominant-negative activity; classification/inheritance should remain provisional. Population allele frequencies and current ClinVar assertion details were not established from the retrieved evidence. All are germline. | Sequence Ontology: intron_variant, splice_region_variant, missense_variant | Human molecular genetics and functional studies (legati2017anovelde pages 1-2, vanlander2018clinicalandgenetic pages 1-3, saha2014thepresenceof pages 1-2, mochel2008splicemutationin pages 2-4, legati2017anovelde pages 5-7). Saha et al., 2014, DOI:10.1074/jbc.M113.526665; Legati et al., 2017, PMID:29079705. |
| Hallmark phenotypes | Usually **childhood-onset**, lifelong severe exercise intolerance with early fatigue, exertional myalgia/cramps, dyspnea, tachycardia or palpitations, and markedly reduced oxidative/work capacity. More strenuous activity can precipitate episodic weakness, rhabdomyolysis, myoglobinuria, and severe lactic acidosis. Weakness may be stable/nonprogressive in classical Swedish disease but slowly progressive with ptosis and wasting in non-founder missense cases. Published samples are too small for defensible percentages; these features are qualitatively common or characteristic. | HP:0003546 exercise intolerance; HP:0003326 muscle weakness; HP:0008947 infantile/childhood muscular weakness; HP:0003323 progressive muscle weakness; HP:0002151 increased serum lactate; HP:0003201 rhabdomyolysis; HP:0002913 myoglobinuria; HP:0001649 tachycardia; HP:0002094 dyspnea; HP:0000508 ptosis; HP:0003236 elevated creatine kinase | Human clinical cohorts and case reports (mochel2008splicemutationin pages 1-2, legati2017anovelde pages 2-3, selvanathan2022mitochondrialironsulfurcluster pages 3-4, montealegre2022fdx2andiscu pages 1-2). Mochel et al., 2008, PMID:18296749; Kollberg et al., 2009, PMID:19567699; Montealegre et al., 2022, DOI:10.1212/NXG.0000000000000648. |
| Tissue specificity and anatomy | Skeletal muscle is the principal affected tissue. For the founder allele, incorrect splicing was approximately **80% in skeletal muscle, 30% in heart, and 10% in liver**, explaining predominant myopathy and relative cardiac/hepatic sparing. Slow-fiber soleus showed especially high mis-splicing in a transgenic system. Cardiac involvement is uncommon in classical disease but has been reported with non-founder variants; exercise-induced pulmonary vascular dysfunction was reported in one homozygous woman. | UBERON:0001134 skeletal muscle tissue; CL:0000187 myocyte; CL:0000748 cardiac muscle cell; GO:0005739 mitochondrion | Human tissue and transgenic/cardiopulmonary evidence (mochel2008splicemutationin pages 1-2, rawcliffe2018ptbp1actsas pages 1-2). Rawcliffe et al., 2018, DOI:10.1002/mgg3.413. |
| Diagnostic biomarkers and functional tests | Resting or exertional **lactate and pyruvate elevation**, elevated CK during muscle injury, myoglobinuria during attacks, and low peak oxygen uptake/poor muscle oxygen extraction support a metabolic myopathy. **FGF21** may be elevated and is a candidate monitoring biomarker, but it is not disease-specific or formally validated. EMG may be myopathic; normal fibroblast respiration does not exclude disease. | HP:0002151 increased serum lactate; HP:0003236 elevated serum CK; HP:0002913 myoglobinuria; HP:0012378 abnormal circulating enzyme concentration | Human physiology, blood biomarkers, and cell studies (selvanathan2022mitochondrialironsulfurcluster pages 3-4, montealegre2022fdx2andiscu pages 1-2, crooks2014elevatedfgf21secretion pages 1-2, holmeshampton2016useofantisense pages 5-6). Crooks et al., 2014, PMID:23933728, DOI:10.1093/hmg/ddt393. |
| Muscle pathology and biochemical diagnosis | Muscle may show markedly diminished/absent **succinate dehydrogenase (complex II)** staining, severe mitochondrial and cytosolic aconitase deficiency, lesser complex-I and complex-III/Rieske defects, mitochondrial proliferation/type-I-fiber predominance, increased capillary density, and iron-positive mitochondrial inclusions. In studied founder-variant muscle, SDH/complex-II and aconitase activities were approximately **10–20% of control**. Perls’ Prussian-blue staining can demonstrate iron accumulation. | HP:0003737 mitochondrial myopathy; HP:0011924 abnormal mitochondrial morphology; HP:0003548 abnormality of mitochondrial metabolism; GO:0000104 succinate dehydrogenase activity; GO:0003994 aconitate hydratase activity | Human biopsy, histochemistry, enzyme assays, and transcriptomics (mochel2008splicemutationin pages 1-2, tong201710ironsulfurproteins pages 31-34, crooks2014elevatedfgf21secretion pages 1-2, crooks2014elevatedfgf21secretion pages 3-4). Mochel et al., 2008, PMID:18296749; Crooks et al., 2014, PMID:23933728. |
| Molecular mechanism | Pathogenic splicing or missense dysfunction **reduces functional ISCU scaffold activity → impairs mitochondrial Fe–S-cluster assembly/transfer → destabilizes Fe–S enzymes, especially aconitase and complex II, with lesser complexes I/III effects → reduces oxidative phosphorylation and oxygen utilization → increases glycolytic pyruvate/lactate production → causes exertional energy failure, pain, weakness, and rhabdomyolysis**. A parallel branch disrupts IRP1/iron regulation and causes mitochondrial iron accumulation; whether iron directly drives myofiber injury is incompletely demonstrated. Tissue-specific splicing is regulated partly by PTBP1. | GO:0016226 iron–sulfur cluster assembly; GO:0006120 mitochondrial electron transport; GO:0006096 glycolytic process; GO:0006879 cellular iron-ion homeostasis; GO:0008380 RNA splicing; GO:0006979 response to oxidative stress | Human muscle, patient myoblasts, biochemical assays, and mechanistic cell studies (tong201710ironsulfurproteins pages 31-34, crooks2014elevatedfgf21secretion pages 1-2, holmeshampton2016useofantisense pages 1-2, rawcliffe2018ptbp1actsas pages 1-2, holmeshampton2016useofantisense pages 1-1). Rawcliffe et al., 2018, DOI:10.1002/mgg3.413. |
| Molecular profiling | Patient-muscle transcriptomics showed induction of **PGC-1α**, mitochondrial biogenesis, fatty-acid oxidation, ketogenic enzyme **HMGCS2**, sulfur-metabolism genes, and **FGF21**, with downregulation of some cytoskeletal/contraction genes. Iron-homeostasis transcripts were altered. These findings indicate compensatory metabolic remodeling rather than a validated diagnostic signature. No disease-specific single-cell, spatial-transcriptomic, lipidomic, epigenomic, or large multi-omics dataset was identified. | GO:0007005 mitochondrion organization; GO:0033539 fatty-acid beta-oxidation using acyl-CoA dehydrogenase; GO:0042776 mitochondrial ATP synthesis coupled proton transport | Human biopsy transcriptomics and cultured-myotube experiments (crooks2014elevatedfgf21secretion pages 1-2, crooks2014elevatedfgf21secretion pages 3-4). Crooks et al., 2014, PMID:23933728, DOI:10.1093/hmg/ddt393. |
| Diagnostic strategy | Confirm with **biallelic ISCU testing** in the classical phenotype: targeted c.418+382G>C analysis is efficient in Northern Swedish ancestry; otherwise use a metabolic/mitochondrial-myopathy panel, WES, or preferably WGS because deep-intronic variants may be missed by routine exome capture. RNA studies from muscle or differentiated myotubes can demonstrate pseudoexon inclusion. Muscle biopsy/enzyme assays are supportive but genetic confirmation is preferred. CMA, karyotype, FISH, mtDNA-only testing, and repeat-expansion testing are not first-line unless another diagnosis is suspected. | NCIT:C15709 genetic testing; NCIT:C101294 whole-genome sequencing; NCIT:C101295 whole-exome sequencing; NCIT:C15189 muscle biopsy | Human diagnostic studies and expert reviews (legati2017anovelde pages 2-3, selvanathan2022mitochondrialironsulfurcluster pages 3-4, mochel2008splicemutationin pages 2-4). Mochel et al., 2008, PMID:18296749. |
| Management | No approved disease-modifying treatment exists. Current care is supportive: individualized activity pacing; avoidance of unaccustomed maximal exertion, dehydration, and prolonged fasting; specialist-supervised submaximal aerobic conditioning where tolerated; physical/occupational therapy; and monitoring of CK, renal function, electrolytes, lactate, cardiac status, and respiratory function according to phenotype. Acute rhabdomyolysis requires standard urgent management with cessation of exertion, hydration, electrolyte/renal surveillance, and treatment of acidosis. Disease-specific controlled outcome data are unavailable. | NCIT:C15311 supportive care; NCIT:C94626 physical therapy; NCIT:C15367 rehabilitation; NCIT:C15368 exercise therapy | Expert review and clinical-practice extrapolation; direct ISCU trial evidence is absent (holmeshampton2016useofantisense pages 5-6, selvanathan2022mitochondrialironsulfurcluster pages 8-8). |
| Experimental therapy | A mutation-directed **18-mer splice-switching ASO** (sequence GATTCTGAAATGAAAGAT; 2′-MOE/constrained-ethyl chemistries) reduced pseudoexon inclusion and restored ISCU protein in patient fibroblasts at roughly **25–30 nM** and myotubes at about **200 nM**. It improved SDHB/complex-II and aconitase activities and normalized excess succinate. This is compelling **in-vitro rescue only**: no ISCU-specific human trial, clinical response rate, safety dataset, regulatory approval, gene therapy, or cell therapy was identified. A 2024 review continues to describe this approach as a promising candidate rather than clinical therapy. | NCIT:C178220 antisense oligonucleotide therapy; NCIT:C179456 splice-switching oligonucleotide | Patient-derived cell experiments and 2024 therapeutic review (holmeshampton2016useofantisense pages 1-1, holmeshampton2016useofantisense pages 7-7, holmeshampton2016useofantisense pages 1-2, holmeshampton2016useofantisense pages 2-3). Holmes-Hampton et al., 2016, PMID:27729411, DOI:10.1093/hmg/ddw338. |
| Epidemiology and population genetics | Ultra-rare, with most classical cases originating in **Northern Sweden** and sharing a founder haplotype; isolated Scandinavian and non-Scandinavian cases carry other genotypes. A historical Northern Swedish carrier estimate of about **1:188** has been reported in the literature, but a contemporary population-based prevalence, incidence, sex ratio, and validated global carrier frequency are **unavailable**. Both sexes are affected. Penetrance appears high in reported biallelic cases, but formal age-dependent estimates are lacking; expressivity varies, especially across genotypes. | Orphan disease; founder variant | Founder mapping, published families, and reviews (mochel2008splicemutationin pages 1-2, vanlander2018clinicalandgenetic pages 1-3, saha2014thepresenceof pages 1-2, mochel2008splicemutationin pages 2-4). Mochel et al., 2008, PMID:18296749. |
| Prognosis | Classical founder-associated disease is chronic and often described as relatively nonprogressive between attacks, but produces substantial lifelong exercise limitation and episodic risk of severe weakness, acidosis, rhabdomyolysis, and renal complications. Missense-associated disease may be more progressive and include ptosis, distal weakness, wasting, anemia, or cardiac involvement. Survival rates, life expectancy, mortality rates, validated quality-of-life scores, and prognostic models are **not available**. | HP:0031796 episodic; HP:0003676 progressive disorder | Human clinical series and case reports (legati2017anovelde pages 1-2, legati2017anovelde pages 2-3, selvanathan2022mitochondrialironsulfurcluster pages 3-4). Legati et al., 2017, PMID:29079705. |
| Prevention and counseling | Primary prevention after conception is not available. Secondary/tertiary prevention includes molecular diagnosis, cascade testing, education about rhabdomyolysis warning signs, personalized exertion plans, hydration, and early treatment of metabolic crises. Autosomal-recessive counseling gives a **25% affected, 50% carrier, 25% unaffected/non-carrier** risk per pregnancy when both parents are carriers. Carrier testing, prenatal diagnosis, and PGT-M are technically feasible once familial variants are known. No newborn-screening program, vaccine, prophylactic drug, or public-health screening program exists. | NCIT:C15278 genetic counseling; NCIT:C92844 carrier testing; NCIT:C17004 prenatal genetic testing; NCIT:C116463 preimplantation genetic testing | Mendelian-risk inference plus established molecular diagnosis; no disease-specific prevention trial identified (vanlander2018clinicalandgenetic pages 1-3, selvanathan2022mitochondrialironsulfurcluster pages 3-4). |
| Models and comparative biology | **Patient myoblasts/myotubes** best reproduce muscle-selective mis-splicing, low ISCU, complex-II/aconitase defects, and ASO rescue; fibroblast abnormalities are milder. **Saccharomyces cerevisiae** engineered variants model respiratory growth, Fe–S-enzyme defects, iron accumulation, and p.Gly96Val dominance; ISU1/ISU2 double loss is lethal. Complete mouse Iscu loss is embryonic lethal; human-ISCU transgenic mice model tissue-specific splicing, but the founder intronic sequence is human/primate-specific, limiting conventional knock-in modeling. No well-established naturally occurring veterinary ISCU myopathy, affected breed, zoonotic transmission, organoid model, or disease-specific zebrafish model was identified. | NCBI Taxon:9606 Homo sapiens; NCBI Taxon:10090 Mus musculus; NCBI Taxon:4932 Saccharomyces cerevisiae; CL:0000187 myocyte | Patient-cell, transgenic-mouse, and engineered-yeast evidence (rawcliffe2018ptbp1actsas pages 1-2, holmeshampton2016useofantisense pages 5-6, saha2014thepresenceof pages 2-3, berti2021thepowerof pages 6-7, legati2017anovelde pages 5-7, holmeshampton2016useofantisense pages 1-1). Saha et al., 2014, DOI:10.1074/jbc.M113.526665; Holmes-Hampton et al., 2016, PMID:27729411. |


*Table: Compact evidence table covering identity, genetics, phenotype, mechanism, diagnosis, management, epidemiology, and experimental models. Quantitative findings and evidence limitations are explicitly labeled for knowledge-base curation.*

## 1. Disease information

### Definition and identifiers

**Preferred name:** hereditary myopathy with lactic acidosis due to ISCU deficiency.  
**Major synonyms:** ISCU myopathy; iron–sulfur cluster deficiency myopathy; Swedish myopathy; hereditary myopathy with lactic acidosis; myopathy with deficiency of succinate dehydrogenase and aconitase.

* **MONDO:** **MONDO:0009706**.
* **OMIM phenotype:** **255125**.
* **Gene:** **ISCU**, OMIM *611911; Ensembl ENSG00000136003; approved name “iron-sulfur cluster assembly enzyme.” Open Targets reports one strongly supported ISCU–disease association, underpinned by human genetic literature including PMIDs 18296749, 19567699, 20206689, and 29079705. (OpenTargets Search: ISCU myopathy-ISCU)
* **ICD/MeSH:** no dedicated disease-specific ICD-10, ICD-11, or MeSH identifier was established in the retrieved evidence. Coding generally requires broader mitochondrial, metabolic-myopathy, lactic-acidosis, or rhabdomyolysis categories.

The evidence is **aggregated disease-level information** derived from published pedigrees, individual patients, muscle biopsies, physiological studies, and experimental systems; it is not an EHR-derived patient dataset.

## 2. Etiology, risk, and protective factors

The initiating cause is a germline pathogenic **ISCU** variant. In classical disease, biallelic loss of functional ISCU impairs mitochondrial Fe–S-cluster assembly. The Northern Swedish founder allele is **c.418+382G>C**, historically reported as g.7044G>C or IVS5+382G>C. It strengthens a cryptic splice acceptor, inserts pseudoexon 4A, introduces a premature termination signal, and markedly reduces functional transcript and protein in skeletal muscle. (mochel2008splicemutationin pages 2-4, holmeshampton2016useofantisense pages 1-2, rawcliffe2018ptbp1actsas pages 1-2)

Additional reported alleles include **c.149G>A (p.Gly50Glu)** in compound heterozygosity with the founder allele and a single de novo heterozygous **p.Gly96Val** allele. Yeast experiments supported pathogenicity and a dominant-negative action of p.Gly96Val, but dominant ISCU myopathy remains provisional because independent human cases have not substantiated it. (vanlander2018clinicalandgenetic pages 1-3, selvanathan2022mitochondrialironsulfurcluster pages 3-4, legati2017anovelde pages 5-7)

**Risk factors:** biallelic pathogenic variants, Northern Swedish ancestry, and family history are the only established disease-occurrence risks. Strenuous or unaccustomed exercise is a **trigger for attacks**, not a cause of the inherited disorder. Dehydration, fasting, intercurrent illness, and heat are clinically plausible metabolic stressors, but disease-specific quantitative interaction studies were not found.

No validated genetic protective variants or modifier genes are known. PTBP1 represses aberrant ISCU splicing experimentally; its tissue-specific abundance may modify expression, but it is not an established protective genotype. Approximately 80% incorrect splicing in skeletal muscle versus 30% in heart and 10% in liver offers a mechanistic explanation for tissue selectivity. (rawcliffe2018ptbp1actsas pages 1-2)

Environmental toxins, infections, smoking, alcohol, occupation, radiation, and diet are not established causes. Hypoxia can suppress ISCU through the miR-210–ISCU axis in pulmonary vascular biology, but this acquired mechanism should not be conflated with inherited ISCU myopathy. (tong201710ironsulfurproteins pages 31-34)

## 3. Phenotypes

The classical phenotype begins in childhood and is chronic/lifelong. Severe intolerance to even modest exercise causes fatigue, muscle pain or cramps, dyspnea, tachycardia, and palpitations. More intense activity may cause acute weakness, painful swelling, rhabdomyolysis, myoglobinuria, and severe lactic acidosis. Maximal work and oxidative capacity are markedly reduced. Suggested terms include **HP:0003546 exercise intolerance**, **HP:0003326 muscle weakness**, **HP:0001649 tachycardia**, **HP:0002094 dyspnea**, **HP:0002151 increased serum lactate**, **HP:0003201 rhabdomyolysis**, and **HP:0002913 myoglobinuria**. (mochel2008splicemutationin pages 1-2, selvanathan2022mitochondrialironsulfurcluster pages 3-4, tong201710ironsulfurproteins pages 31-34)

Non-founder missense disease can broaden the phenotype. The p.Gly96Val patient had delayed walking, falls, hypotonia, wasting, absent reflexes, bilateral ptosis, distal weakness, elevated CK, anemia/leukopenia, and episodic inability to walk; progression was slow with partial recovery between episodes and preserved cognition. Suggested additional terms are **HP:0000508 ptosis**, **HP:0003236 elevated CK**, **HP:0001252 hypotonia**, and **HP:0003202 muscle atrophy**. (legati2017anovelde pages 2-3)

Reliable percentages for symptoms cannot be assigned because published cohorts are tiny and genotype-enriched. Classical disease is often relatively stable between metabolic attacks, whereas missense-associated cases may be slowly progressive. Quality-of-life instruments such as EQ-5D, SF-36, or PROMIS have not been systematically reported; nevertheless, profound restriction of walking, exercise, employment, and daily activity indicates substantial functional burden.

## 4. Genetic and molecular information

ISCU is a nuclear gene encoding a mitochondrial scaffold on which nascent [2Fe–2S] clusters are assembled before transfer to recipient proteins. Suggested annotation: **GO:0016226 iron–sulfur cluster assembly** and **GO:0005739 mitochondrion**. (vanlander2018clinicalandgenetic pages 1-3, tong201710ironsulfurproteins pages 31-34)

The founder and missense alleles are germline. The founder variant is a deep-intronic splice-altering loss-of-function allele; p.Gly50Glu impairs scaffold function; p.Gly96Val behaves dominantly in yeast, including impaired respiratory growth, reduced aconitase and complex-II activity, increased iron, and approximately 30% lower iron binding. Current gnomAD frequencies and variant-specific contemporary ClinVar classifications were not established from the retrieved texts and should be imported directly from those databases before production curation. (saha2014thepresenceof pages 1-2, legati2017anovelde pages 5-7)

No recurrent chromosomal abnormality, somatic ISCU lesion, germline mosaicism, anticipation, or disease-defining epigenetic signature is known. PTBP1, and experimentally IGF2BP1, regulate aberrant splicing and are candidate expression modifiers, not proven Mendelian modifier genes.

## 5. Environmental and lifestyle information

No environmental agent or pathogen causes ISCU myopathy. Exercise is physiologically beneficial in many mitochondrial myopathies but excessive exertion can precipitate rhabdomyolysis in ISCU deficiency. Therefore, lifestyle advice must balance avoidance of maximal exertion with carefully supervised, submaximal conditioning. (holmeshampton2016useofantisense pages 5-6, selvanathan2022mitochondrialironsulfurcluster pages 8-8)

There is no evidence that smoking cessation, alcohol avoidance, or a specific diet prevents the genotype, although general mitochondrial-care principles favor adequate hydration, avoidance of prolonged fasting, and prompt management of illness. These are expert-practice extrapolations rather than trial-proven ISCU interventions.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic c.418+382G>C leads to** activation of a cryptic splice acceptor and muscle-predominant pseudoexon 4A inclusion; alternatively, pathogenic missense variation **leads to** dysfunctional ISCU scaffold activity. (holmeshampton2016useofantisense pages 1-2, legati2017anovelde pages 1-2)
2. Aberrant transcript/protein **results in** reduced functional mitochondrial ISCU, especially in skeletal myofibers. (rawcliffe2018ptbp1actsas pages 1-2)
3. Reduced ISCU scaffold function **leads to** impaired assembly and delivery of Fe–S clusters to apoproteins. (tong201710ironsulfurproteins pages 31-34)
4. Fe–S-cluster deficiency **results in** severe loss of mitochondrial and cytosolic aconitase and complex-II/SDH activity, with lesser complex-I and complex-III/Rieske impairment. In founder-variant muscle, aconitase/complex-II activity was reported at roughly 10–20% of control. (crooks2014elevatedfgf21secretion pages 1-2, holmeshampton2016useofantisense pages 1-2)
5. Respiratory-chain failure **leads to** poor muscle oxygen extraction, reduced oxidative phosphorylation, and compensatory glycolytic flux. (tong201710ironsulfurproteins pages 31-34)
6. Increased reliance on glycolysis **results in** exercise-induced pyruvate and lactate accumulation and metabolic acidosis. (holmeshampton2016useofantisense pages 1-2, rawcliffe2018ptbp1actsas pages 1-2)
7. ATP insufficiency during exertion **leads to** fatigue, cramps, weakness, dyspnea, tachycardia, and—under severe stress—myofiber breakdown, rhabdomyolysis, and myoglobinuria. (mochel2008splicemutationin pages 1-2, crooks2014elevatedfgf21secretion pages 1-2)
8. **Parallel branch:** impaired aconitase/IRP1 and Fe–S homeostasis **leads to** dysregulated iron handling and mitochondrial iron accumulation; iron-mediated oxidative injury is biologically plausible but not fully demonstrated as the proximate cause of human myofiber necrosis. (montealegre2022fdx2andiscu pages 1-2, crooks2014elevatedfgf21secretion pages 3-4)
9. **Compensatory branch:** energetic stress **results in** PGC-1α-driven mitochondrial remodeling, increased capillarity/type-I fibers, fatty-acid oxidation and ketogenic enzymes, and FGF21 secretion. (crooks2014elevatedfgf21secretion pages 1-2, crooks2014elevatedfgf21secretion pages 3-4)

The primary cell is the skeletal **myocyte/myofiber** (**CL:0000187 myocyte**); mitochondria are the key compartment. Relevant processes include **GO:0016226 Fe–S-cluster assembly**, **GO:0006120 mitochondrial electron transport**, **GO:0006096 glycolysis**, **GO:0006879 cellular iron-ion homeostasis**, and **GO:0008380 RNA splicing**.

Human muscle transcriptomics showed induction of mitochondrial, fatty-acid-oxidation, sulfur-metabolism, PGC-1α, HMGCS2, and FGF21 programs, with reduced expression of some contraction/cytoskeletal genes. These are compensatory profiles, not validated diagnostic classifiers. No disease-specific single-cell, spatial-transcriptomic, lipidomic, epigenomic, CRISPR-screen, or integrated multi-omics study was identified. (crooks2014elevatedfgf21secretion pages 1-2, crooks2014elevatedfgf21secretion pages 3-4)

## 7. Anatomical structures affected

The principal organ is **skeletal muscle** (**UBERON:0001134**), especially oxidative myofibers. The relevant subcellular site is the mitochondrial matrix/inner-membrane respiratory machinery. Muscle may display type-I-fiber predominance, mitochondrial proliferation, increased capillary density, reduced SDH staining, and iron-positive mitochondrial inclusions. (mochel2008splicemutationin pages 1-2, crooks2014elevatedfgf21secretion pages 1-2)

The heart and vascular smooth muscle are relatively spared in classical founder disease, consistent with less aberrant splicing, although cardiomyopathy or pulmonary vascular dysfunction can occur in broader ISCU-associated phenotypes. There is no characteristic lateralization; weakness is systemic and generally bilateral. CNS involvement is not typical of classical Swedish disease. (mochel2008splicemutationin pages 1-2, selvanathan2022mitochondrialironsulfurcluster pages 3-4)

## 8. Temporal development

Onset is usually childhood, insidious, and exercise-linked. Classical disease is chronic and frequently described as nonprogressive or slowly changing between crises, but severe attacks are episodic. There is no formal staging system. Missense cases may progress from early fatigability and falls to ptosis, distal weakness, and wasting. (legati2017anovelde pages 1-2, legati2017anovelde pages 2-3)

Critical periods are metabolic stress episodes—strenuous activity, illness, dehydration, or fasting—when energy demand exceeds oxidative capacity. Recovery between attacks can be substantial, but cumulative disability and persistent exercise intolerance remain. Spontaneous molecular remission is not described.

## 9. Inheritance and population

Classical ISCU myopathy is **autosomal recessive**. Affected Northern Swedish families share a homozygous 12q haplotype, supporting a founder effect. A historical carrier estimate near 1:188 has been cited for Northern Sweden, but no contemporary population-based prevalence, incidence, global carrier frequency, or sex ratio is available. Both sexes can be affected. (mochel2008splicemutationin pages 1-2, saha2014thepresenceof pages 1-2, mochel2008splicemutationin pages 2-4)

Penetrance appears high among reported biallelic patients but has not been formally quantified. Expressivity varies by genotype and tissue-specific splicing. Anticipation has not been reported. Consanguinity is not required because the founder allele can produce homozygosity in an endogamous population.

## 10. Diagnostics

Clinical suspicion arises from childhood exercise intolerance, disproportionate exertional tachycardia/dyspnea, lactate elevation, and episodic rhabdomyolysis. Useful measurements include CK, lactate/pyruvate at rest and after controlled exercise, renal function and electrolytes during attacks, urine/blood myoglobin, cardiopulmonary exercise testing, and possibly FGF21. FGF21 is supportive but neither specific nor formally validated for ISCU myopathy. (selvanathan2022mitochondrialironsulfurcluster pages 3-4, crooks2014elevatedfgf21secretion pages 1-2, holmeshampton2016useofantisense pages 5-6)

Muscle biopsy may show absent or markedly reduced SDH staining, aconitase deficiency, iron-positive mitochondria on Perls’ staining, and respiratory-chain defects. Fibroblast respiration can be normal and therefore does not exclude disease. (selvanathan2022mitochondrialironsulfurcluster pages 3-4, montealegre2022fdx2andiscu pages 1-2)

**Genetic strategy:** targeted c.418+382G>C testing is efficient with Northern Swedish ancestry. Otherwise, use a mitochondrial/metabolic-myopathy panel or WES, but recognize that routine exome capture may miss deep-intronic alleles; WGS plus RNA analysis is preferable when suspicion remains high. Muscle or differentiated-myotube RNA can demonstrate pseudoexon inclusion. CMA, karyotyping, FISH, repeat-expansion testing, and mtDNA-only analysis are not first-line for a classic ISCU phenotype. (legati2017anovelde pages 2-3, selvanathan2022mitochondrialironsulfurcluster pages 3-4, mochel2008splicemutationin pages 2-4)

Differentials include fatty-acid oxidation disorders, glycogenoses such as McArdle disease, LPIN1/RYR1-related rhabdomyolysis, mitochondrial respiratory-chain disorders, FDX2-related episodic mitochondrial myopathy, and other Fe–S biogenesis defects including FXN, FDX2, NFU1, BOLA3, GLRX5, and CIAO1 disorders. FDX2 disease can resemble ISCU deficiency but may be more severe and lacks the characteristic ISCU-associated muscle iron accumulation. (montealegre2022fdx2andiscu pages 1-2)

No population newborn-screening program or standardized society diagnostic criteria were identified.

## 11. Outcome and prognosis

Classical disease usually permits survival into adulthood but causes lifelong exercise limitation and recurrent risk of severe metabolic crises. Potential acute complications include rhabdomyolysis, electrolyte abnormalities, acute kidney injury from myoglobinuria, and severe acidosis. Quantitative five- or ten-year survival, mortality, life expectancy, validated disability scales, and quality-of-life scores are unavailable. (legati2017anovelde pages 1-2, mochel2008splicemutationin pages 1-2)

Genotype may be prognostic: founder-associated disease is often relatively stable, while non-founder missense disease can be more progressive and multisystemic. Candidate monitoring markers include CK, lactate/pyruvate, FGF21, exercise capacity, and attack frequency, but none is a validated prognostic model.

## 12. Treatment and current implementation

There is no approved pharmacotherapy, gene therapy, cell therapy, or surgery that corrects ISCU deficiency. Care is supportive and individualized: activity pacing, avoidance of unaccustomed maximal exertion, specialist-supervised submaximal aerobic conditioning, physical and occupational therapy, and phenotype-directed cardiac/respiratory surveillance. Suggested NCIt concepts include **Supportive Care**, **Physical Therapy**, **Rehabilitation**, and **Exercise Therapy**. (holmeshampton2016useofantisense pages 5-6, selvanathan2022mitochondrialironsulfurcluster pages 8-8)

Acute rhabdomyolysis requires standard urgent management: stop exertion, assess CK, creatinine, urine output, potassium and acid-base status, provide appropriate hydration, and treat electrolyte disturbances or acidosis. These measures are standard-of-care extrapolations; ISCU-specific comparative trials are absent.

The leading experimental treatment is a splice-switching **18-mer ASO**, sequence **GATTCTGAAATGAAAGAT**, with 2′-MOE/constrained-ethyl chemistry. In patient fibroblasts, approximately 25–30 nM restored ISCU protein; myotubes required about 200 nM. Treatment increased correct transcript and ISCU protein, restored SDHB/complex-II and aconitase activity, and normalized excess succinate. This is mechanistically strong **in-vitro evidence**, not patient efficacy. (holmeshampton2016useofantisense pages 7-7, holmeshampton2016useofantisense pages 1-2, holmeshampton2016useofantisense pages 2-3)

A 2024 review continued to identify splice-modulating ASOs as promising for inherited metabolic diseases, including ISCU myopathy, but no ISCU-specific human trial, response rate, safety dataset, or regulatory approval was found. The expert assessment is therefore that the founder allele is unusually tractable for precision splice correction, while delivery to widespread skeletal muscle, durability, toxicity, and an ultra-rare trial design remain major barriers.

## 13. Prevention

The inherited genotype cannot be prevented through lifestyle modification. **Secondary prevention** consists of early molecular diagnosis, family cascade testing, and avoidance of diagnostic delay. **Tertiary prevention** includes education about rhabdomyolysis warning signs, hydration, avoidance of prolonged fasting and unaccustomed maximal exertion, and prompt treatment of metabolic crises.

For two heterozygous parents, each pregnancy has a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability. Carrier testing, prenatal diagnosis, and PGT-M are technically feasible after familial variants are established. No vaccine, prophylactic drug, newborn-screening program, or population-wide carrier program is available.

## 14. Other species and natural disease

No well-established naturally occurring ISCU-myopathy syndrome, affected veterinary breed, or zoonotic issue was identified. Relevant taxa include **Homo sapiens** (NCBI Taxon 9606), **Mus musculus** (10090), and **Saccharomyces cerevisiae** (4932). The Fe–S pathway is evolutionarily conserved, but the common human founder mutation lies in a human/primate-specific intronic sequence, limiting direct cross-species modeling. (holmeshampton2016useofantisense pages 5-6)

## 15. Model organisms and experimental systems

Patient-derived myoblasts differentiated into myotubes are the most disease-relevant model: they reproduce muscle-selective mis-splicing, low ISCU, complex-II/aconitase defects, excess succinate, and ASO rescue. Fibroblasts are easier to use but show milder and sometimes normal oxidative phenotypes, limiting negative-result interpretation. (holmeshampton2016useofantisense pages 1-1, holmeshampton2016useofantisense pages 5-6)

In **S. cerevisiae**, ISU1/ISU2 double deletion is lethal. Engineered homologous variants permit testing of respiratory growth, Fe–S enzymes, iron handling, and dominance. The isu1-G97V model supported pathogenicity and a dominant-negative action corresponding to human p.Gly96Val. Limitations include differences in targeting sequences, expression, protein conservation, and inability to model human tissue-specific splicing. (saha2014thepresenceof pages 2-3, berti2021thepowerof pages 6-7, legati2017anovelde pages 5-7)

Complete mouse Iscu loss is embryonic lethal. Human-ISCU transgenic mice have been useful for studying tissue-specific splicing, including high mis-splicing in slow-fiber soleus, but a conventional knock-in of the Swedish allele is difficult because its intronic context is human-specific. No validated disease-specific zebrafish, organoid, or spontaneous animal model was identified. (rawcliffe2018ptbp1actsas pages 1-2, holmeshampton2016useofantisense pages 5-6)

## Recent developments and evidence gaps

Research published in 2023–2024 primarily advanced the broader Fe–S-biogenesis and splice-therapeutics fields rather than producing new ISCU patient cohorts. The most directly relevant recent development is continued recognition of ISCU pseudoexon correction as an actionable ASO strategy. Important unmet needs are an international natural-history registry, standardized exercise and attack outcomes, current allele-frequency analysis, systematic cardiopulmonary surveillance, patient-reported quality-of-life data, a humanized in-vivo model, and first-in-human muscle-directed splice-correction studies.

### Key publications and URLs

* Mochel et al. **March 2008**, *American Journal of Human Genetics*, PMID **18296749**, DOI: https://doi.org/10.1016/j.ajhg.2007.12.012. The study identified the shared ISCU splice mutation and stated that it “causes myopathy with exercise intolerance.” (mochel2008splicemutationin pages 1-2)
* Kollberg et al. **August 2009**, *Brain*, PMID **19567699**, DOI: https://doi.org/10.1093/brain/awp152. Clinical/genetic expansion of ISCU deficiency, including a new mutation.
* Crooks et al. **2014**; advance publication **13 August 2013**, *Human Molecular Genetics*, PMID **23933728**, DOI: https://doi.org/10.1093/hmg/ddt393. The authors identified “elevated FGF21 secretion, PGC-1α and ketogenic enzyme expression” as hallmarks of Fe–S depletion in human skeletal muscle. (crooks2014elevatedfgf21secretion pages 1-2)
* Saha et al. **11 April 2014**, *Journal of Biological Chemistry*, DOI: https://doi.org/10.1074/jbc.M113.526665. The abstract concluded that reduced respiration from diminished Fe–S-cluster synthesis produces muscle weakness. (saha2014thepresenceof pages 1-2)
* Holmes-Hampton et al. **December 2016**, *Human Molecular Genetics*, PMID **27729411**, DOI: https://doi.org/10.1093/hmg/ddw338. The authors reported ASO correction of the splicing error in patient cell lines, with restoration of Fe–S-dependent biochemical functions. (holmeshampton2016useofantisense pages 7-7, holmeshampton2016useofantisense pages 2-3)
* Legati et al. **2017**, *Journal of Medical Genetics* 54:815–824, PMID **29079705**, DOI: https://doi.org/10.1136/jmedgenet-2017-104822. First reported de novo heterozygous p.Gly96Val case; dominant inheritance remains provisional. (legati2017anovelde pages 1-2)
* Rawcliffe et al. **September 2018**, *Molecular Genetics & Genomic Medicine*, DOI: https://doi.org/10.1002/mgg3.413. PTBP1 was shown to repress aberrant tissue-specific ISCU splicing. (rawcliffe2018ptbp1actsas pages 1-2)
* Montealegre et al. **February 2022**, *Neurology Genetics* 8:e648, DOI: https://doi.org/10.1212/NXG.0000000000000648. Human comparison of ISCU and FDX2 rhabdomyolysis highlighted distinct severity and muscle iron regulation. (montealegre2022fdx2andiscu pages 1-2)
* Chen et al. **January 2024**, *BioDrugs* 38:177–203, DOI: https://doi.org/10.1007/s40259-024-00644-7. Contemporary review of splice-modulating ASOs for inherited metabolic disease; ISCU remains a promising preclinical candidate rather than an approved therapy.

References

1. (mochel2008splicemutationin pages 1-2): Fanny Mochel, Melanie A. Knight, Wing-Hang Tong, Dena Hernandez, Karen Ayyad, Tanja Taivassalo, Peter M. Andersen, Andrew Singleton, Tracey A. Rouault, Kenneth H. Fischbeck, and Ronald G. Haller. Splice mutation in the iron-sulfur cluster scaffold protein iscu causes myopathy with exercise intolerance. American journal of human genetics, 82 3:652-60, Mar 2008. URL: https://doi.org/10.1016/j.ajhg.2007.12.012, doi:10.1016/j.ajhg.2007.12.012. This article has 278 citations and is from a highest quality peer-reviewed journal.

2. (selvanathan2022mitochondrialironsulfurcluster pages 3-4): Arthavan Selvanathan and Bindu Parayil Sankaran. Mitochondrial iron-sulfur cluster biogenesis and neurological disorders. Jan 2022. URL: https://doi.org/10.1016/j.mito.2021.10.004, doi:10.1016/j.mito.2021.10.004. This article has 22 citations and is from a peer-reviewed journal.

3. (holmeshampton2016useofantisense pages 1-2): Gregory P. Holmes-Hampton, Daniel R. Crooks, Ronald G. Haller, Shuling Guo, Susan M. Freier, Brett P. Monia, and Tracey A. Rouault. Use of antisense oligonucleotides to correct the splicing error in iscu myopathy patient cell lines. Human molecular genetics, 25 23:5178-5187, Dec 2016. URL: https://doi.org/10.1093/hmg/ddw338, doi:10.1093/hmg/ddw338. This article has 14 citations and is from a domain leading peer-reviewed journal.

4. (holmeshampton2016useofantisense pages 7-7): Gregory P. Holmes-Hampton, Daniel R. Crooks, Ronald G. Haller, Shuling Guo, Susan M. Freier, Brett P. Monia, and Tracey A. Rouault. Use of antisense oligonucleotides to correct the splicing error in iscu myopathy patient cell lines. Human molecular genetics, 25 23:5178-5187, Dec 2016. URL: https://doi.org/10.1093/hmg/ddw338, doi:10.1093/hmg/ddw338. This article has 14 citations and is from a domain leading peer-reviewed journal.

5. (OpenTargets Search: ISCU myopathy-ISCU): Open Targets Query (ISCU myopathy-ISCU, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (legati2017anovelde pages 1-2): Andrea Legati, Aurelio Reyes, Camilla Ceccatelli Berti, Oliver Stehling, Silvia Marchet, Costanza Lamperti, Alberto Ferrari, Alan J Robinson, Ulrich Mühlenhoff, Roland Lill, Massimo Zeviani, Paola Goffrini, and Daniele Ghezzi. A novel de novo dominant mutation in iscu associated with mitochondrial myopathy. JournalArticle, Feb 2017. URL: https://doi.org/10.17863/cam.18560, doi:10.17863/cam.18560. This article has 45 citations.

7. (legati2017anovelde pages 5-7): Andrea Legati, Aurelio Reyes, Camilla Ceccatelli Berti, Oliver Stehling, Silvia Marchet, Costanza Lamperti, Alberto Ferrari, Alan J Robinson, Ulrich Mühlenhoff, Roland Lill, Massimo Zeviani, Paola Goffrini, and Daniele Ghezzi. A novel de novo dominant mutation in iscu associated with mitochondrial myopathy. JournalArticle, Feb 2017. URL: https://doi.org/10.17863/cam.18560, doi:10.17863/cam.18560. This article has 45 citations.

8. (vanlander2018clinicalandgenetic pages 1-3): A. V. Vanlander and R. Van Coster. Clinical and genetic aspects of defects in the mitochondrial iron–sulfur cluster synthesis pathway. Journal of Biological Inorganic Chemistry, 23:495-506, Apr 2018. URL: https://doi.org/10.1007/s00775-018-1550-z, doi:10.1007/s00775-018-1550-z. This article has 33 citations and is from a peer-reviewed journal.

9. (saha2014thepresenceof pages 1-2): Prasenjit Prasad Saha, S.K.Praveen Kumar, Shubhi Srivastava, Devanjan Sinha, Gautam Pareek, and Patrick D'Silva. The presence of multiple cellular defects associated with a novel g50e iron-sulfur cluster scaffold protein (iscu) mutation leads to development of mitochondrial myopathy. Journal of Biological Chemistry, 289(15):10359-10377, Apr 2014. URL: https://doi.org/10.1074/jbc.m113.526665, doi:10.1074/jbc.m113.526665. This article has 43 citations and is from a domain leading peer-reviewed journal.

10. (mochel2008splicemutationin pages 2-4): Fanny Mochel, Melanie A. Knight, Wing-Hang Tong, Dena Hernandez, Karen Ayyad, Tanja Taivassalo, Peter M. Andersen, Andrew Singleton, Tracey A. Rouault, Kenneth H. Fischbeck, and Ronald G. Haller. Splice mutation in the iron-sulfur cluster scaffold protein iscu causes myopathy with exercise intolerance. American journal of human genetics, 82 3:652-60, Mar 2008. URL: https://doi.org/10.1016/j.ajhg.2007.12.012, doi:10.1016/j.ajhg.2007.12.012. This article has 278 citations and is from a highest quality peer-reviewed journal.

11. (legati2017anovelde pages 2-3): Andrea Legati, Aurelio Reyes, Camilla Ceccatelli Berti, Oliver Stehling, Silvia Marchet, Costanza Lamperti, Alberto Ferrari, Alan J Robinson, Ulrich Mühlenhoff, Roland Lill, Massimo Zeviani, Paola Goffrini, and Daniele Ghezzi. A novel de novo dominant mutation in iscu associated with mitochondrial myopathy. JournalArticle, Feb 2017. URL: https://doi.org/10.17863/cam.18560, doi:10.17863/cam.18560. This article has 45 citations.

12. (montealegre2022fdx2andiscu pages 1-2): Sebastian Montealegre, Elise Lebigot, Hugo Debruge, Norma Romero, Bénédicte Héron, Pauline Gaignard, Antoine Legendre, Apolline Imbard, Stéphanie Gobin, Emmanuelle Lacène, Patrick Nusbaum, Arnaud Hubas, Isabelle Desguerre, Aude Servais, Pascal Laforêt, Peter van Endert, François Jérome Authier, Cyril Gitiaux, and Pascale de Lonlay. Fdx2 and iscu gene variations lead to rhabdomyolysis with distinct severity and iron regulation. Feb 2022. URL: https://doi.org/10.1212/nxg.0000000000000648, doi:10.1212/nxg.0000000000000648. This article has 17 citations.

13. (rawcliffe2018ptbp1actsas pages 1-2): Denise F. R. Rawcliffe, Lennart Österman, Angelica Nordin, and Monica Holmberg. Ptbp1 acts as a dominant repressor of the aberrant tissue‐specific splicing of iscu in hereditary myopathy with lactic acidosis. Molecular Genetics & Genomic Medicine, 6:887-897, Sep 2018. URL: https://doi.org/10.1002/mgg3.413, doi:10.1002/mgg3.413. This article has 8 citations and is from a peer-reviewed journal.

14. (crooks2014elevatedfgf21secretion pages 1-2): Daniel R. Crooks, Thanemozhi G. Natarajan, Suh Young Jeong, Chuming Chen, Sun Young Park, Hongzhan Huang, Manik C. Ghosh, Wing-Hang Tong, Ronald G. Haller, Cathy Wu, and Tracey A. Rouault. Elevated fgf21 secretion, pgc-1α and ketogenic enzyme expression are hallmarks of iron-sulfur cluster depletion in human skeletal muscle. Human molecular genetics, 23 1:24-39, Aug 2014. URL: https://doi.org/10.1093/hmg/ddt393, doi:10.1093/hmg/ddt393. This article has 81 citations and is from a domain leading peer-reviewed journal.

15. (holmeshampton2016useofantisense pages 5-6): Gregory P. Holmes-Hampton, Daniel R. Crooks, Ronald G. Haller, Shuling Guo, Susan M. Freier, Brett P. Monia, and Tracey A. Rouault. Use of antisense oligonucleotides to correct the splicing error in iscu myopathy patient cell lines. Human molecular genetics, 25 23:5178-5187, Dec 2016. URL: https://doi.org/10.1093/hmg/ddw338, doi:10.1093/hmg/ddw338. This article has 14 citations and is from a domain leading peer-reviewed journal.

16. (tong201710ironsulfurproteins pages 31-34): Wing-Hang Tong and T. Rouault. 10 Iron-sulfur proteins and human diseases, pages 227-306. De Gruyter, Sep 2017. URL: https://doi.org/10.1515/9783110479850-010, doi:10.1515/9783110479850-010. This article has 0 citations.

17. (crooks2014elevatedfgf21secretion pages 3-4): Daniel R. Crooks, Thanemozhi G. Natarajan, Suh Young Jeong, Chuming Chen, Sun Young Park, Hongzhan Huang, Manik C. Ghosh, Wing-Hang Tong, Ronald G. Haller, Cathy Wu, and Tracey A. Rouault. Elevated fgf21 secretion, pgc-1α and ketogenic enzyme expression are hallmarks of iron-sulfur cluster depletion in human skeletal muscle. Human molecular genetics, 23 1:24-39, Aug 2014. URL: https://doi.org/10.1093/hmg/ddt393, doi:10.1093/hmg/ddt393. This article has 81 citations and is from a domain leading peer-reviewed journal.

18. (holmeshampton2016useofantisense pages 1-1): Gregory P. Holmes-Hampton, Daniel R. Crooks, Ronald G. Haller, Shuling Guo, Susan M. Freier, Brett P. Monia, and Tracey A. Rouault. Use of antisense oligonucleotides to correct the splicing error in iscu myopathy patient cell lines. Human molecular genetics, 25 23:5178-5187, Dec 2016. URL: https://doi.org/10.1093/hmg/ddw338, doi:10.1093/hmg/ddw338. This article has 14 citations and is from a domain leading peer-reviewed journal.

19. (selvanathan2022mitochondrialironsulfurcluster pages 8-8): Arthavan Selvanathan and Bindu Parayil Sankaran. Mitochondrial iron-sulfur cluster biogenesis and neurological disorders. Jan 2022. URL: https://doi.org/10.1016/j.mito.2021.10.004, doi:10.1016/j.mito.2021.10.004. This article has 22 citations and is from a peer-reviewed journal.

20. (holmeshampton2016useofantisense pages 2-3): Gregory P. Holmes-Hampton, Daniel R. Crooks, Ronald G. Haller, Shuling Guo, Susan M. Freier, Brett P. Monia, and Tracey A. Rouault. Use of antisense oligonucleotides to correct the splicing error in iscu myopathy patient cell lines. Human molecular genetics, 25 23:5178-5187, Dec 2016. URL: https://doi.org/10.1093/hmg/ddw338, doi:10.1093/hmg/ddw338. This article has 14 citations and is from a domain leading peer-reviewed journal.

21. (saha2014thepresenceof pages 2-3): Prasenjit Prasad Saha, S.K.Praveen Kumar, Shubhi Srivastava, Devanjan Sinha, Gautam Pareek, and Patrick D'Silva. The presence of multiple cellular defects associated with a novel g50e iron-sulfur cluster scaffold protein (iscu) mutation leads to development of mitochondrial myopathy. Journal of Biological Chemistry, 289(15):10359-10377, Apr 2014. URL: https://doi.org/10.1074/jbc.m113.526665, doi:10.1074/jbc.m113.526665. This article has 43 citations and is from a domain leading peer-reviewed journal.

22. (berti2021thepowerof pages 6-7): Camilla Ceccatelli Berti, Giulia di Punzio, Cristina Dallabona, Enrico Baruffini, Paola Goffrini, Tiziana Lodi, and Claudia Donnini. The power of yeast in modelling human nuclear mutations associated with mitochondrial diseases. Feb 2021. URL: https://doi.org/10.3390/genes12020300, doi:10.3390/genes12020300. This article has 31 citations.

## Artifacts

- [Edison artifact artifact-00](ISCU_Myopathy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:23933728` (3 mentions) - Synchronized dynamics of Tipula paludosa metapopulation in a southwestern Scotland agroecosystem: linking pattern to process.
  - shared terms: none

Weighed against this report's own most characteristic terms: `disease`, `iscu`, `gene`, `genetic`, `human`, `clinical`, `mitochondrial`, `myopathy`, `muscle`, `include`, `exercise`, `protein`, `model`, `cell`, `variant`, `rhabdomyolysis`, `affected`, `metabolic`, `molecular`, `phenotype`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 52 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C15368` (Treatment) (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.

48 of 52 terms resolved to a current term; the rest could not be looked up either way.