---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T18:25:57.585769'
end_time: '2026-09-01T18:33:09.311213'
duration_seconds: 431.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: immunodeficiency 35 (complete tyrosine kinase 2 / TYK2 deficiency,
    biallelic null variants)
  mondo_id: MONDO:0012682
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 2
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0012682
    reported_labels:
    - if available
    ontology_label: immunodeficiency 35
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
  path: Immunodeficiency_35-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** immunodeficiency 35 (complete tyrosine kinase 2 / TYK2 deficiency, biallelic null variants)
- **MONDO ID:** MONDO:0012682 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **immunodeficiency 35 (complete tyrosine kinase 2 / TYK2 deficiency, biallelic null variants)** covering all of the
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
- **Disease Name:** immunodeficiency 35 (complete tyrosine kinase 2 / TYK2 deficiency, biallelic null variants)
- **MONDO ID:** MONDO:0012682 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **immunodeficiency 35 (complete tyrosine kinase 2 / TYK2 deficiency, biallelic null variants)** covering all of the
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


# Complete TYK2 deficiency (immunodeficiency 35): research report

## Scope and evidence note

This report concerns **complete autosomal-recessive TYK2 deficiency caused by biallelic null/loss-of-function variants**. It does **not** treat partial/hypomorphic TYK2 deficiency or homozygosity for the common p.Pro1104Ala allele as the same disease. Those alleles can produce narrower defects—especially isolated IL-23 signaling impairment—and materially different clinical phenotypes. The strongest disease-specific evidence remains the 2015 international series and the expanded mechanistic cohort published in September 2022; the 2023–2024 literature mainly provides broader inborn-error-of-immunity or JAK–STAT context rather than a new complete-TYK2-deficiency cohort. Because the disorder is exceptionally rare, most estimates derive from aggregated case reports rather than registries or population studies.

| Domain | High-confidence finding | Evidence type | Suggested ontology/identifier |
|---|---|---|---|
| Disease identifiers | Complete autosomal recessive TYK2 deficiency corresponds to immunodeficiency 35; MONDO association is MONDO:0012682 and OMIM is 611521; causal target is TYK2, Ensembl ENSG00000105397 (OpenTargets Search: immunodeficiency 35,TYK2 deficiency-TYK2, sarrafzadeh2020anewpatient pages 1-3) | Aggregated disease database + human case series | MONDO:0012682; OMIM:611521; TYK2; ENSG00000105397 |
| Disease definition | Mendelian inborn error of immunity caused by biallelic TYK2 loss-of-function/null alleles, distinct from partial TYK2 deficiency and the common P1104A susceptibility allele (ogishi2022impairedil23–dependentinduction pages 4-6, ogishi2022impairedil23–dependentinduction pages 2-3) | Human clinical genetics + functional immunology | Suggested label: inborn error of immunity; suggested label: Mendelian susceptibility to mycobacterial disease spectrum requiring ontology validation |
| Inheritance | Inheritance is autosomal recessive; unaffected heterozygous parents/carriers reported; consanguinity documented in some families (sarrafzadeh2020anewpatient pages 1-3, sarrafzadeh2020anewpatient pages 3-4) | Human pedigree/case report | Suggested label: autosomal recessive inheritance |
| Causal gene/protein | TYK2 encodes tyrosine kinase 2, a JAK family kinase required for signaling downstream of multiple cytokine receptors, especially IL-23, IL-12, IL-10, and type I IFN pathways in this disease context (ogishi2022impairedil23–dependentinduction pages 12-15, boissondupuis2018tuberculosisandimpaired pages 5-6, ogishi2022impairedil23–dependentinduction pages 15-17) | Human patient-cell functional studies | TYK2; suggested GO label: JAK-STAT cascade requiring ontology validation |
| Pathogenic variant classes | Reported complete-deficiency alleles include frameshift, nonsense, essential splice-site, and multi-exon deletion variants causing loss of expression or complete loss of function; examples include p.C70Hfs*21, p.P216Rfs*14, p.E154*, p.L767*, c.2466+1G>T, c.466-1G>A, and exon 19-25 deletion (ogishi2022impairedil23–dependentinduction pages 4-6, ogishi2022impairedil23–dependentinduction pages 7-9, ogishi2022impairedil23–dependentinduction pages 3-4) | Human molecular genetics + patient-cell assays | Suggested label: null variant; loss-of-function variant; germline variant |
| Hallmark phenotype: mycobacterial disease | Mycobacterial disease is a hallmark phenotype, including BCG disease/BCG-osis, environmental mycobacterial disease, and tuberculosis; in the 2022 series, 9 reported patients had mycobacterial disease, including 6 with BCG disease, 1 with environmental mycobacteria, and 3 with tuberculosis (ogishi2022impairedil23–dependentinduction pages 2-3) | Human cohort/series | Suggested HPO label: mycobacterial infection susceptibility requiring ontology validation; suggested HPO label: disseminated BCG infection requiring ontology validation |
| Hallmark phenotype: viral disease | Severe viral disease is also characteristic, including mucocutaneous HSV-1, HSV-1 encephalitis, VZV, molluscum contagiosum, parainfluenza pneumonia, influenza A pneumonia, COVID-19 pneumonia, and MMR vaccine disease (ogishi2022impairedil23–dependentinduction pages 2-3) | Human cohort/series | Suggested HPO label: recurrent viral infections requiring ontology validation; suggested HPO label: herpes simplex encephalitis requiring ontology validation |
| Additional/variable phenotype | Some patients show atopy/eczema, cellulitis, oral thrush, chronic mucocutaneous candidiasis, or parasitic infection such as Leishmania major; hyper-IgE syndrome is not universal and may be absent (sarrafzadeh2020anewpatient pages 1-3, ogishi2022impairedil23–dependentinduction pages 4-6, ogishi2022impairedil23–dependentinduction pages 2-3) | Human case reports/series | Suggested HPO labels requiring ontology validation: eczema; cellulitis; chronic mucocutaneous candidiasis; leishmaniasis susceptibility |
| Temporal pattern | Onset is usually pediatric/early childhood; vaccine-associated BCG complications can appear in infancy, e.g., one reported patient developed fever, lymphadenitis, and ulcers after BCG vaccination at 7 months (sarrafzadeh2020anewpatient pages 1-3) | Human case report | Suggested HPO label: infantile onset requiring ontology validation |
| Core molecular mechanism | Biallelic TYK2 null alleles lead to absent or nonfunctional TYK2 protein, causing impaired cellular responses to IFN-alpha/beta, IL-10, IL-12, and especially IL-23; the unifying antimycobacterial mechanism across TYK2-deficient forms is impaired IL-23-dependent induction of IFN-gamma (ogishi2022impairedil23–dependentinduction pages 12-15, ogishi2022impairedil23–dependentinduction pages 15-17, ogishi2022impairedil23–dependentinduction pages 2-3) | Human patient-cell mechanistic studies | Suggested GO labels requiring ontology validation: response to interferon-alpha; interleukin-23-mediated signaling pathway; interferon-gamma production |
| Immunologic cell types implicated | Defective IL-23-dependent IFN-gamma production has been demonstrated in lymphocyte subsets including MAIT cells, gamma-delta T cells, and NK cells; classic monocytes and myeloid dendritic cells also show impaired IFN-alpha responses (ogishi2022impairedil23–dependentinduction pages 12-15) | Human ex vivo cellular immunology | Suggested CL labels requiring ontology validation: mucosal associated invariant T cell; gamma-delta T cell; natural killer cell; classical monocyte; myeloid dendritic cell |
| Signaling readouts | Patient cells show impaired or abolished STAT1/STAT3 phosphorylation after IFN-alpha, IL-10, and IL-23 stimulation, with IL-23 signaling particularly vulnerable; receptor expression may remain intact, indicating signaling rather than receptor absence as the core defect (boissondupuis2018tuberculosisandimpaired pages 5-6, ogishi2022impairedil23–dependentinduction pages 7-9) | Human patient-cell signaling assays | Suggested GO labels requiring ontology validation: STAT1 phosphorylation; STAT3 phosphorylation |
| Diagnostic confirmation | Diagnosis is confirmed by molecular testing showing biallelic TYK2 variants, typically by WES followed by PCR/Sanger confirmation, plus functional immunology such as lymphocyte transformation tests and impaired IFN-gamma production after BCG + IL-12 stimulation or defective cytokine-induced STAT phosphorylation (sarrafzadeh2020anewpatient pages 3-4, sarrafzadeh2020anewpatient pages 1-3) | Human diagnostic genetics + functional assays | TYK2 sequencing; suggested NCIT label: whole exome sequencing; suggested assay labels requiring ontology validation: cytokine stimulation assay; phospho-STAT assay |
| Differential diagnostic context | Should be distinguished from other MSMD/type I IFN pathway defects and from partial TYK2 deficiency or TYK2 P1104A homozygosity, which can show narrower signaling defects than complete null deficiency (ogishi2022impairedil23–dependentinduction pages 2-3, ogishi2022impairedil23–dependentinduction pages 15-17) | Comparative human genetics/functional studies | Suggested labels requiring ontology validation: IL12RB1 deficiency; IFNAR pathway defects; partial TYK2 deficiency |
| Prevention/management | Avoidance of live BCG vaccination is strongly supported by reported vaccine complications and by families withholding BCG after an affected sibling; management is mainly infection-directed, while IFN-gamma plus antibiotics is supported at the broader MSMD level and should be considered extrapolative rather than TYK2-specific trial evidence (ogishi2022impairedil23–dependentinduction pages 3-4, bustamante2020mendeliansusceptibilityto pages 5-6) | Human case management + review/expert extrapolation | Suggested NCIT labels requiring ontology validation: Bacillus Calmette-Guerin vaccine avoidance; interferon gamma therapy; antibacterial therapy |
| Prognosis/outcomes | Penetrance for at least one infectious phenotype appears high among individuals with biallelic TYK2 genotypes, but precise survival, life expectancy, and long-term disability estimates are not established from current small cohorts (ogishi2022impairedil23–dependentinduction pages 3-4) | Human cohort inference | Suggested label: high infectious penetrance; data gap on survival metrics |
| Epidemiology/data gaps | Extremely rare disease; no robust prevalence or incidence estimates were identified; literature remains limited to small international case series/case reports, and QoL data are lacking (ogishi2022impairedil23–dependentinduction pages 2-3, ogishi2022impairedil23–dependentinduction pages 3-4) | Literature synthesis/data-gap assessment | Suggested label: ultra-rare disease |
| Real-world implementation | Real-world use today centers on genomic diagnosis of children with unusual mycobacterial and/or severe viral infections, especially after BCG disease or herpesvirus/COVID complications, with family-based counseling and cascade testing where relevant (sarrafzadeh2020anewpatient pages 3-4, ogishi2022impairedil23–dependentinduction pages 3-4) | Human clinical implementation | Suggested NCIT label: genetic counseling; suggested label: cascade testing requiring ontology validation |
| Mouse/cellular model | Tyk2-knockout mice are viable, show impaired type I IFN and IL-12/IL-23 biology, and are more susceptible to multiple viruses; they are useful mechanistic models but do not fully recapitulate the breadth of human infectious and atopic phenotypes (meyts2021viralinfectionsin pages 13-14, muromoto2022currentunderstandingof pages 2-4, muromoto2022currentunderstandingof pages 1-2) | Model organism + cellular studies | Suggested model identifiers requiring ontology validation: Tyk2 knockout mouse; Mus musculus |


*Table: This compact table summarizes high-confidence disease knowledge for complete autosomal recessive TYK2 deficiency only, emphasizing identifiers, hallmark phenotypes, mechanism, diagnostics, management, and key data gaps. It is structured for direct use in a knowledge base and flags ontology labels that need formal validation.*

## 1. Disease information

**Definition.** Immunodeficiency 35 is a Mendelian inborn error of immunity in which biallelic TYK2 null alleles abolish or critically disrupt tyrosine kinase 2. The resulting combined cytokine-signaling defect compromises IL-12/IL-23-dependent IFN-γ immunity to intracellular pathogens and type-I-interferon-mediated antiviral immunity. Clinically, the most characteristic manifestations are BCG disease, environmental mycobacteriosis or tuberculosis, together with variably severe viral infections. Hyper-IgE/atopic manifestations occurred in the original Japanese patient but are not defining or universal. The expanded literature explicitly describes complete AR TYK2 deficiency as mycobacterial and/or viral disease with impaired IFN-α/β, IL-10, IL-12 and IL-23 responses. (nemoto2018compoundheterozygoustyk2 pages 1-2, ogishi2022impairedil23–dependentinduction pages 2-3)

**Identifiers and names.** 

- MONDO: **MONDO:0012682**, “immunodeficiency 35.”
- OMIM phenotype: **611521**, commonly rendered *Immunodeficiency 35* or *TYK2 deficiency*.
- Causal target: **TYK2**, Ensembl **ENSG00000105397**, approved name *tyrosine kinase 2*. Open Targets links TYK2 to MONDO:0012682 using human genetic evidence and landmark PMIDs 17088085, 26304966 and 22402565. (OpenTargets Search: immunodeficiency 35,TYK2 deficiency-TYK2)
- Common synonyms: **complete TYK2 deficiency**, **autosomal-recessive TYK2 deficiency**, **TYK2-associated immunodeficiency**, and historically **autosomal-recessive hyper-IgE syndrome due to TYK2 deficiency**. The last term should be deprecated as a general synonym because most patients do not have HIES.
- No disease-specific ICD-10 or ICD-11 code was established in the retrieved evidence. Operational coding generally falls under broader “other specified immunodeficiency” or inborn-error-of-immunity categories. No uniquely specific MeSH descriptor was identified.

**Evidence granularity.** The genetic and clinical descriptions originate from individual patients and families, later aggregated into disease-level resources such as MONDO, OMIM and Open Targets. They are not EHR-derived population estimates. Open Targets records five TYK2–immunodeficiency-35 evidence items. (OpenTargets Search: immunodeficiency 35,TYK2 deficiency-TYK2)

## 2. Etiology, risk and protective factors

### Causal factors

The necessary initiating lesion is a **germline biallelic TYK2 loss-of-function genotype** inherited in an autosomal-recessive pattern. Demonstrated complete-deficiency alleles include frameshift, nonsense, essential splice-site and multi-exon deletion variants, including p.Cys70Hisfs*21, p.Pro216Argfs*14, p.Glu154Ter, p.Leu767Ter, c.2466+1G>T, c.466-1G>A and deletion of exons 19–25. Several were experimentally shown to cause loss of expression and loss of function. (ogishi2022impairedil23–dependentinduction pages 4-6, ogishi2022impairedil23–dependentinduction pages 7-9, ogishi2022impairedil23–dependentinduction pages 3-4)

The disease is not caused by infection itself. Rather, infections expose the inherited defect. BCG vaccination, environmental mycobacteria, *M. tuberculosis*, herpesviruses, respiratory viruses and other intracellular pathogens are **clinical triggers**.

### Genetic risk factors

- Two pathogenic/null alleles are the principal risk factor; heterozygous parents in reported families were healthy. (sarrafzadeh2020anewpatient pages 1-3, sarrafzadeh2020anewpatient pages 3-4)
- Consanguinity increases the probability of homozygosity. One p.Pro216Argfs*14 patient was born to first-degree-consanguineous Persian-Turkish parents and had two maternal/paternal uncles who died in childhood. (sarrafzadeh2020anewpatient pages 1-3)
- The common TYK2 p.Pro1104Ala allele is **not complete TYK2 deficiency**. Homozygosity selectively impairs IL-23 responses and predisposes principally to tuberculosis; it should be represented separately in a knowledge base. (ogishi2022impairedil23–dependentinduction pages 15-17, ogishi2022impairedil23–dependentinduction pages 2-3)
- No validated modifier gene, anticipation, germline-mosaicism series, or chromosomal founder syndrome has been established.

### Environmental and infectious risk

Exposure determines which phenotype becomes manifest. Live BCG is a particularly important avoidable exposure because six of nine mycobacterially affected patients summarized in the 2022 literature had BCG disease. Tuberculosis-endemic residence and contact with environmental mycobacteria plausibly increase risk, while circulating herpesviruses and respiratory viruses reveal impaired antiviral immunity. (ogishi2022impairedil23–dependentinduction pages 2-3, ogishi2022impairedil23–dependentinduction pages 3-4)

No toxin, pollution, diet, smoking, alcohol, occupational or exercise association is established. Age and sex are not causal environmental risk factors. Family history and consanguinity are useful diagnostic clues rather than independent mechanisms.

### Protective factors and gene–environment interaction

No proven genetic modifier or lifestyle factor protects against complete deficiency. Avoiding live BCG and rapidly treating infections reduce exposure-related morbidity but do not correct the genotype. The clearest gene–environment interaction is:

> biallelic TYK2 null genotype + BCG exposure → failure of IL-23/IL-12-dependent IFN-γ immunity → local or disseminated BCG disease.

Two genetically affected individuals remained asymptomatic when BCG was withheld—one specifically because an affected sibling had developed BCG disease—illustrating exposure-dependent penetrance, although absence of BCG does not remove risk from wild mycobacteria or viruses. (ogishi2022impairedil23–dependentinduction pages 3-4)

## 3. Phenotypes

The 2022 synthesis reported 15 previously recognized patients from 13 families and expanded genetic/functional study to **19 patients from 16 families**. Among the earlier clinical group, nine had mycobacterial disease: six BCG disease, one environmental mycobacterial disease and three tuberculosis; categories can overlap. Five had severe viral disease. (ogishi2022impairedil23–dependentinduction pages 2-3, ogishi2022impairedil23–dependentinduction pages 3-4)

| Phenotype | Type and characteristics | Suggested HPO annotation |
|---|---|---|
| BCG infection/BCG-osis | Clinical infection/sign; often infancy or childhood after vaccination; potentially severe or disseminated. One child developed fever, lymphadenitis and ulcers at seven months, with *M. bovis* BCG recovered from biopsy and gastric secretions. | Disseminated BCG infection; recurrent mycobacterial infections; lymphadenitis; fever; skin ulceration |
| Tuberculosis or environmental mycobacteriosis | Infection; childhood through adulthood; episodic but potentially recurrent/severe. Three TB cases and one environmental-mycobacteria case were summarized among nine mycobacterially affected patients. | Increased susceptibility to mycobacterial infection; tuberculosis |
| Severe/recurrent viral infection | Infection; variable severity. Reported agents/conditions include mucocutaneous HSV-1, HSV-1 encephalitis, VZV/chickenpox, molluscum contagiosum, parainfluenza-3 pneumonia, influenza-A pneumonia, COVID-19 pneumonia and disease after live MMR vaccine. | Recurrent viral infections; recurrent herpes simplex infection; viral encephalitis; pneumonia |
| COVID-19 | Infection/lower-respiratory manifestation. Six patients had pre-vaccination COVID-19 and four developed hypoxemic pneumonia in the expanded series. | COVID-19; hypoxemia; pneumonia |
| Candidiasis | Infection; uncommon/variable. Chronic mucocutaneous candidiasis was described in the original Japanese patient; oral thrush occurred in another. | Chronic mucocutaneous candidiasis; oral candidiasis |
| Atopy/HIES-like findings | Physical/laboratory phenotype; not universal. Eczema, skin abscesses, pneumonia and elevated IgE characterized the original case, whereas later patients often had normal IgE and no HIES phenotype. | Eczema; recurrent skin abscess; elevated serum IgE |
| Other infection | Cellulitis and *Leishmania major* infection occurred in individual patients; these are not established high-frequency hallmarks. | Cellulitis; leishmaniasis |
| Functional laboratory abnormality | Impaired IFN-γ production after IL-12/IL-23 stimulation; impaired IFN-α-, IL-10- and IL-23-induced STAT phosphorylation. Routine immunoglobulins, lymphocyte markers and neutrophil oxidative burst may be normal. | Abnormal cytokine secretion; abnormal interferon response; abnormality of immune-system physiology |

The infection spectrum and counts are supported by the expanded human series. (ogishi2022impairedil23–dependentinduction pages 4-6, ogishi2022impairedil23–dependentinduction pages 2-3, ogishi2022impairedil23–dependentinduction pages 12-15) The p.Pro216Argfs*14 case had normal immunoglobulins, CD markers and NBT/DHR despite markedly impaired IL-12-induced IFN-γ production, demonstrating that normal routine immunology does not exclude the disorder. (sarrafzadeh2020anewpatient pages 1-3, sarrafzadeh2020anewpatient pages 3-4)

**Onset/course.** Onset is commonly infantile or pediatric and may be acute after vaccination, followed by episodic or recurrent infections throughout life. The Persian-Turkish patient had BCG complications at seven months, HSV at ages three and seven, aseptic meningitis at six and chickenpox at 6.5 years. (sarrafzadeh2020anewpatient pages 1-3)

**Quality of life.** No TYK2-specific EQ-5D, SF-36, PROMIS, school-function or caregiver-burden study was identified. Nevertheless, recurrent hospitalization, prolonged multidrug antimycobacterial therapy, neurologic viral disease and chronic infection predict substantial burden. This is a clinical inference, not a quantified TYK2-specific result.

## 4. Genetic and molecular information

**Gene.** TYK2 is the sole established causal gene for this entity. It encodes a Janus-family nonreceptor tyrosine kinase containing an N-terminal FERM receptor-binding region, SH2-like region, regulatory pseudokinase JH2 domain and catalytic JH1 kinase domain. Null alleles have been found across these regions. Open Targets identifies TYK2 as the only associated target for MONDO:0012682. (OpenTargets Search: immunodeficiency 35,TYK2 deficiency-TYK2, sarrafzadeh2020anewpatient pages 1-3)

**Representative pathogenic alleles.** Complete deficiency has resulted from p.Cys70Hisfs*21, p.Pro216Argfs*14, p.Glu154Ter, p.Leu767Ter, c.2466+1G>T, c.466-1G>A, exon-19–25 deletion and functionally null missense alleles such as p.Gly1010Asp. Their consequences include nonsense-mediated decay/loss of protein or a stable but catalytically and functionally inactive protein. (ogishi2022impairedil23–dependentinduction pages 4-6, ogishi2022impairedil23–dependentinduction pages 7-9, ogishi2022impairedil23–dependentinduction pages 3-4, ogishi2022impairedil23–dependentinduction pages 15-17)

All disease-causing variants are constitutional/germline, not somatic. Exact ACMG classifications and gnomAD frequencies must be verified per transcript and genomic build in ClinVar/gnomAD before database ingestion; the retrieved papers establish pathogenicity experimentally but do not supply a uniform modern ACMG table or frequencies for every allele. Large chromosomal abnormalities, repeat expansions, mitochondrial variants and aneuploidy are not characteristic.

**Important exclusion.** Compound-heterozygous p.Cys70Serfs*21/p.Arg231Trp with residual TYK2 expression and predominantly IL-23 impairment/T-cell lymphopenia is partial deficiency, not the requested complete-null disorder. (nemoto2018compoundheterozygoustyk2 pages 7-9)

**Modifiers/epigenetics/omics.** No validated modifier gene or disease-specific methylation, histone, metabolomic, lipidomic or spatial-transcriptomic signature is established. Patient leukocyte transcriptomics after cytokine stimulation implicated IFIT1/2/3/5, IRF7/9, ISG15/20 and MX1/2 modules under STAT1/STAT2 and IRF control; this is a stimulated signaling signature, not a validated diagnostic biomarker. (ogishi2022impairedil23–dependentinduction pages 12-15)

## 5. Environmental information

The relevant non-genetic factors are infectious exposures rather than toxicants or lifestyle. Confirmed agents include *Mycobacterium bovis* BCG, *M. tuberculosis*, environmental mycobacteria, HSV-1, VZV, molluscum contagiosum virus, parainfluenza virus 3, influenza A, SARS-CoV-2 and live attenuated MMR vaccine viruses. *Leishmania major* and candidiasis were reported in individual cases. (ogishi2022impairedil23–dependentinduction pages 4-6, ogishi2022impairedil23–dependentinduction pages 2-3)

There is no evidence that diet, exercise, smoking, alcohol, radiation, pollution or occupational chemicals initiate this Mendelian disorder. Standard sanitation, infection-control and prompt evaluation of febrile illness are sensible but have not been tested in TYK2-specific trials.

## 6. Mechanism/pathophysiology

### Ordered causal chain

1. **Biallelic TYK2 null variants lead to** absent TYK2 protein or a completely nonfunctional kinase/scaffold.
2. **Loss of TYK2 leads to** deficient receptor-proximal JAK activation and impaired STAT phosphorylation downstream of IFN-α/β, IL-10, IL-12 and IL-23.
3. **Defective IL-23 and IL-12 signaling leads to** reduced IFN-γ induction in MAIT, γδ-T, NK and other lymphocyte populations.
4. **Reduced IFN-γ production leads to** inadequate macrophage activation and intracellular control of BCG, environmental mycobacteria and *M. tuberculosis*.
5. **Defective IFN-α/β signaling leads to** reduced interferon-stimulated-gene induction and impaired cell-intrinsic antiviral control across leukocyte and nonhematopoietic compartments.
6. **These two branches result in** mycobacterial disease and severe/recurrent viral disease, respectively.
7. **Impaired IL-23/Th17-associated biology may contribute to** candidiasis and some mucocutaneous phenotypes; this branch is biologically plausible and supported in selected patients but is less consistently demonstrated than the IFN-γ/mycobacterial branch.
8. **Organ injury results secondarily from** pathogen replication and host inflammation—e.g., pneumonia, lymph-node/skin disease or encephalitis—rather than a primary degenerative tissue process.

Patient cells show impaired STAT1/STAT3 phosphorylation after IFN-α, IL-10 and IL-23; IL-12 signaling affects TYK2/JAK2/STAT4, and IL-23 affects TYK2/JAK2/STAT3. Receptor abundance may remain normal, localizing the lesion to intracellular signal transduction. (ogishi2022impairedil23–dependentinduction pages 7-9, boissondupuis2018tuberculosisandimpaired pages 5-6)

The key modern mechanistic conclusion is captured in the 2022 abstract: **“Impairment of IL-23–dependent induction of IFN-γ is the only mechanism of mycobacterial disease common to patients with any of the five known forms of autosomal recessive TYK2 deficiency.”** [Ogishi et al., *J Exp Med*, published September 2022, DOI: https://doi.org/10.1084/jem.20220094]. (ogishi2022impairedil23–dependentinduction pages 2-3)

Complete deficiency impairs—but in some cell types does not abolish—IFN-α/β, IL-10, IL-12 and IL-23 responses. Responses to several other IL-10-family cytokines, including IL-26, IL-22, IL-20, IL-19 and IFN-λ, were relatively intact in the experiments retrieved. (ogishi2022impairedil23–dependentinduction pages 15-17)

**Suggested GO terms/labels:** JAK–STAT cascade; cytokine-mediated signaling pathway; type-I-interferon signaling pathway; cellular response to interferon-alpha; interleukin-12-mediated signaling; interleukin-23-mediated signaling; positive regulation of interferon-gamma production; defense response to bacterium; defense response to virus; STAT1/STAT3/STAT4 phosphorylation.

**Suggested CL terms/labels:** natural killer cell, γδ T cell, mucosal-associated invariant T cell, CD4-positive αβ T cell, classical monocyte, macrophage and conventional/myeloid dendritic cell. These labels should be reconciled against the current CL release before ingestion.

## 7. Anatomical structures affected

There is no fixed congenital anatomic malformation. Affected sites reflect infection:

- **Immune/hematopoietic system:** peripheral blood leukocytes, lymphocytes, monocytes, macrophages and dendritic cells; lymph nodes are common BCG sites.
- **Respiratory system:** lungs in TB, influenza, parainfluenza and COVID-19 pneumonia.
- **Skin and mucosa:** BCG ulcers, HSV lesions, molluscum, eczema, abscesses, cellulitis and candidiasis.
- **Central nervous system:** HSV encephalitis and aseptic meningitis in individual patients.
- **Reticuloendothelial organs:** potentially involved in disseminated BCG/mycobacteriosis.

Suggested UBERON labels are blood, lymph node, lung, skin, oral mucosa and brain. Suggested cellular compartments are plasma membrane-associated cytokine-receptor complexes and cytosol (TYK2/JAK signaling), followed by nucleus (activated STAT transcription); relevant GO cellular-component labels include cytoplasm, plasma membrane and nucleus. Lateralization is not a disease feature. (sarrafzadeh2020anewpatient pages 1-3, ogishi2022impairedil23–dependentinduction pages 2-3, boissondupuis2018tuberculosisandimpaired pages 5-6)

## 8. Temporal development

The genetic defect is congenital and lifelong, but clinical onset depends on exposure. BCG vaccination can produce manifestations in infancy; viral and wild-type mycobacterial disease can emerge later in childhood or adulthood. The course is best characterized as **chronic susceptibility with episodic infections**, not a uniform progressive staging disorder. (sarrafzadeh2020anewpatient pages 1-3, ogishi2022impairedil23–dependentinduction pages 3-4)

There are no validated early/intermediate/advanced stages. Remission is generally treatment-induced clearance or suppression of an infection rather than remission of the inherited signaling defect. Critical intervention windows are before live vaccination, during early investigation of BCG complications, and before dissemination or severe pulmonary/CNS infection.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Healthy heterozygous parents and an unaffected wild-type sibling were documented in the p.Pro216Argfs*14 family. For two carrier parents, the conventional per-pregnancy risks are 25% affected, 50% carrier and 25% unaffected/noncarrier, assuming confirmed parental variants and no unusual reproductive event. (sarrafzadeh2020anewpatient pages 3-4)

The 2022 study characterized 19 patients from 16 families and described high penetrance for at least one infectious phenotype among biallelic cases, but exposure-dependent asymptomatic individuals exist. Thus, penetrance is high but not demonstrably 100%, and expressivity is markedly variable. (ogishi2022impairedil23–dependentinduction pages 3-4)

No reliable incidence, prevalence, carrier-frequency, sex-ratio or life-table estimate exists. A prior synthesis described inherited complete IL-12Rβ1 and TYK2 deficiencies individually as rarer than approximately 1 per 600,000, but that figure is not a direct prevalence estimate for complete TYK2 null deficiency and should not be entered as such. Geographic reports include Japan, Iran, Turkey, Saudi Arabia and other regions represented by international cohorts, often with consanguinity; ascertainment is too sparse to infer ethnic susceptibility. Founder effects require variant-specific confirmation.

Anticipation is not expected for a loss-of-function recessive disorder and has not been reported. Germline mosaicism has not been systematically studied.

## 10. Diagnostics

### Recommended approach

1. **Recognize the phenotype:** unusual BCG disease, environmental mycobacteriosis/TB, severe herpesvirus or respiratory viral disease, especially with normal routine immunoglobulins and lymphocyte subsets.
2. **Baseline testing:** CBC/differential, lymphocyte subsets, immunoglobulins/IgE, vaccine antibodies, inflammatory markers, cultures/PCR and imaging directed by infection. Normal NBT/DHR helps exclude chronic granulomatous disease but does not exclude TYK2 deficiency.
3. **Genetic testing:** an inborn-error-of-immunity/MSMD panel including TYK2, or WES/WGS with copy-number calling; confirm candidate variants and segregation by Sanger sequencing. WGS is useful when exome/panel testing misses noncoding, structural or poorly captured splice variants.
4. **Functional confirmation:** TYK2 protein immunoblot/flow assay where validated; phospho-STAT testing after IFN-α, IL-10, IL-12 and IL-23; and whole-blood/PBMC assays measuring IFN-γ after BCG ± IL-12/IL-23. The reported p.Pro216Argfs*14 diagnosis used WES followed by PCR/Sanger confirmation, lymphocyte transformation testing, and BCG/IL-12 cytokine assays. (sarrafzadeh2020anewpatient pages 3-4, sarrafzadeh2020anewpatient pages 1-3)

**Direct diagnostic quote:** the 2018 partial-deficiency paper’s abstract summarizes the complete form as follows: **“A detailed immunological investigation of these patients revealed impaired responses to type I IFN, IL-10, IL-12 and IL-23, which are associated with increased susceptibility to mycobacterial and/or viral infections.”** [Nemoto et al., *Scientific Reports*, May 2018, DOI: https://doi.org/10.1038/s41598-018-25260-8]. (nemoto2018compoundheterozygoustyk2 pages 1-2)

### Differential diagnosis

Major differentials include IL12RB1, IL12B, IL12RB2 and IL23R deficiency; IFNGR1/IFNGR2 and STAT1 loss-of-function; NEMO and CYBB-related MSMD; chronic granulomatous disease; severe combined immunodeficiency; DOCK8 or STAT3 hyper-IgE syndrome; IFNAR1/IFNAR2, STAT2, IRF9 or JAK1 defects; and acquired immunodeficiency. Combined impairment of IL-23/IL-12-driven IFN-γ plus type-I-IFN responses favors complete TYK2 deficiency over isolated IL-12/23-axis disorders. Partial TYK2 deficiency and p.Pro1104Ala homozygosity must be distinguished functionally. (ogishi2022impairedil23–dependentinduction pages 15-17, ogishi2022impairedil23–dependentinduction pages 2-3, bustamante2020mendeliansusceptibilityto pages 5-6)

CMA, karyotype, FISH, mitochondrial testing and repeat-expansion assays are not first-line unless another phenotype suggests them. RNA sequencing may resolve splice/noncoding alleles but is not a validated stand-alone diagnostic. There is no newborn biochemical screen.

## 11. Outcome and prognosis

No robust 5- or 10-year survival, mortality rate or life-expectancy estimate is available. Outcomes depend on pathogen, dissemination, pulmonary/CNS involvement, speed of diagnosis and access to antimicrobials. Reported complications include disseminated BCG disease, TB, severe pneumonia, hypoxemia, encephalitis and chronic mucocutaneous infection. (ogishi2022impairedil23–dependentinduction pages 4-6, ogishi2022impairedil23–dependentinduction pages 2-3)

Routine immune-cell counts may remain near normal, so absence of lymphopenia does not indicate a benign prognosis. Conversely, some genetically affected people remain asymptomatic when major exposures such as BCG are avoided. No TYK2-specific prognostic biomarker beyond genotype/function and prior infection severity has been validated. Disability and QoL have not been quantified.

## 12. Treatment

There is no approved TYK2-replacement drug, gene therapy or disease-specific randomized trial. Care should be coordinated by an immunologist and infectious-disease specialist.

- **Active mycobacterial disease:** species- and susceptibility-directed multidrug antimycobacterial therapy. BCG disease may require prolonged therapy; pyrazinamide is intrinsically inactive against *M. bovis* and regimen design requires specialist input.
- **Adjunctive recombinant IFN-γ:** broader MSMD expert literature supports IFN-γ with antibiotics because it bypasses impaired IL-12/IL-23-driven IFN-γ production. This is mechanistically compelling but remains **extrapolated**, not supported by a TYK2-specific response-rate trial. (bustamante2020mendeliansusceptibilityto pages 5-6)
- **Viral disease:** prompt pathogen-specific therapy where available—e.g., acyclovir for HSV/VZV—and early antiviral management for influenza or COVID-19 according to contemporary guidance.
- **Antimicrobial prophylaxis:** individualized after recurrent/disseminated infection; no standardized TYK2-specific regimen or response percentage exists.
- **Immunoglobulin replacement:** not routinely indicated when quantitative and functional humoral immunity is normal; consider only if a clinically significant antibody defect is independently demonstrated.
- **HSCT:** theoretically replaces hematopoietic TYK2-deficient immunity, but the retrieved disease-specific literature does not establish indications, conditioning, response rate or superiority over medical management. It should therefore be considered experimental/highly individualized rather than standard care.
- **Gene/RNA therapy:** no established clinical implementation was identified.
- **Avoid TYK2 inhibitors:** pharmacologic TYK2 inhibition treats autoimmune disease and would not correct this loss-of-function condition.

Suggested NCIt intervention labels include Anti-Infective Agent, Antibacterial Agent, Antiviral Agent, Interferon Gamma, Hematopoietic Stem Cell Transplantation, Genetic Counseling and Supportive Care; exact current NCIt codes should be validated before ingestion.

No disease-specific NCT study was returned by the ClinicalTrials.gov search. Accordingly, there are no evidence-based treatment-response or adverse-event rates specific to complete TYK2 deficiency.

## 13. Prevention

**Primary prevention of genotype:** impossible after conception. For known carrier couples, genetic counseling, partner testing, prenatal diagnosis and preimplantation genetic testing for the familial variants are available reproductive options.

**Secondary prevention:** cascade testing of siblings and relatives permits diagnosis before BCG or severe infection. There is no population newborn screen; targeted sequencing is appropriate in high-risk families.

**Tertiary prevention:** avoid **live BCG** in affected or not-yet-excluded at-risk infants. Reported families withheld BCG after disease in a sibling, and BCG complications are a recurrent hallmark. (sarrafzadeh2020anewpatient pages 3-4, ogishi2022impairedil23–dependentinduction pages 3-4) Other live vaccines require individualized specialist risk assessment because vaccine-strain MMR disease and severe viral susceptibility have been reported. Non-live vaccines should generally be maintained, although TYK2-specific immunogenicity data are sparse.

Prompt cultures/PCR, early antimicrobials, household TB risk assessment, and infection-avoidance counseling are reasonable. There is no evidence that diet or lifestyle modification changes the molecular disease.

## 14. Other species and natural disease

No well-established naturally occurring companion-animal, livestock or wildlife syndrome equivalent to human complete TYK2 deficiency was identified. The relevant ortholog is **Tyk2** in *Mus musculus* (NCBI Taxonomy **10090**); humans are *Homo sapiens* (Taxonomy **9606**). Ortholog-specific NCBI Gene identifiers should be checked directly in the current NCBI Gene record before database insertion.

There is no zoonotic transmission: TYK2 deficiency is inherited, not contagious. Affected humans may acquire infections from environmental or animal reservoirs, but the immunodeficiency itself cannot cross species.

## 15. Model organisms

The principal model is the **germline Tyk2-knockout mouse**, supplemented by mouse embryonic fibroblasts, macrophages, dendritic cells, lymphocyte progenitors and engineered human cell lines.

Tyk2−/− mice are viable and lack gross developmental or hematopoietic abnormalities, but have partial type-I-IFN signaling impairment. They show defective IL-12/IL-23 biology, impaired dendritic-cell production of IL-12/IL-23 after CpG, reduced Th1/Th17 responses and increased viral susceptibility. Reported challenges include failure to clear vaccinia from spleen, increased LCMV and MCMV susceptibility, 100% mortality after intranasal VSV versus 20% after intravenous VSV, and 100% mortality after EMCV. They remain less susceptible than Ifnar1−/− mice, indicating residual antiviral signaling. (meyts2021viralinfectionsin pages 13-14, muromoto2022currentunderstandingof pages 2-4)

These mice also show reduced disease in collagen-induced arthritis, EAE, colitis and psoriasis models, illustrating why partial pharmacologic TYK2 inhibition can be anti-inflammatory. In DSS colitis, disease is delayed; in one TNBS model approximately 50% of Tyk2-deficient mice survived whereas wild-type controls were reported as lethal. (muromoto2022currentunderstandingof pages 6-7, muromoto2022currentunderstandingof pages 4-6)

**Applications:** dissecting receptor-specific JAK–STAT signaling, antiviral immunity, IL-12/Th1 and IL-23/Th17 biology, testing kinase-dependent versus scaffold functions, and evaluating TYK2 inhibitors.

**Limitations:** murine Tyk2 deficiency does not fully reproduce the breadth and variability of human BCG/TB, herpesviral, candidal and atopic phenotypes. Experimental high-dose pathogen challenge also differs from natural human exposure. Human patient cells remain essential for variant classification and pathway confirmation. (muromoto2021therapeuticadvantageof pages 2-4, muromoto2022currentunderstandingof pages 7-8, muromoto2022currentunderstandingof pages 1-2)

## Evidence appraisal and recent developments

The most important recent disease-specific development is the 2022 demonstration that defective **IL-23-dependent IFN-γ induction**—rather than a generic failure of every TYK2-linked cytokine—is the common mechanism connecting genetically diverse TYK2 deficiencies to mycobacterial disease. The study also expanded the recognized genotype spectrum and documented COVID-19, including hypoxemic pneumonia, in affected individuals. (ogishi2022impairedil23–dependentinduction pages 4-6, ogishi2022impairedil23–dependentinduction pages 12-15, ogishi2022impairedil23–dependentinduction pages 2-3)

The 2023–2024 field increasingly uses WES/WGS, stimulated phospho-protein assays and functional genomics to diagnose inborn errors of immunity, but no 2023–2024 complete-TYK2-null cohort, validated omics diagnostic, interventional trial or gene therapy was identified in the retrieved evidence. Thus, claims about prevalence, formal clinical criteria, survival, QoL, HSCT efficacy, prophylactic regimens and treatment response must remain explicitly **not available**, rather than being inferred from more common immunodeficiencies.

### Principal primary sources

1. Minegishi et al. Initial human TYK2-deficiency report, PMID **17088085** (2006).
2. Kreins et al. *Human TYK2 deficiency: mycobacterial and viral infections without hyper-IgE syndrome*, *J Exp Med* (2015), PMID **26304966**, DOI: https://doi.org/10.1084/jem.20140280.
3. Sarrafzadeh et al. *A New Patient with Inherited TYK2 Deficiency*, *J Clin Immunol* (online November 2019; volume publication 2020), DOI: https://doi.org/10.1007/s10875-019-00713-5. (sarrafzadeh2020anewpatient pages 1-3, sarrafzadeh2020anewpatient pages 3-4)
4. Ogishi et al. *Impaired IL-23–dependent induction of IFN-γ underlies mycobacterial disease in patients with inherited TYK2 deficiency*, *J Exp Med*, September 2022, DOI: https://doi.org/10.1084/jem.20220094. (ogishi2022impairedil23–dependentinduction pages 4-6, ogishi2022impairedil23–dependentinduction pages 12-15, ogishi2022impairedil23–dependentinduction pages 2-3)
5. Nemoto et al. *Compound heterozygous TYK2 mutations underlie primary immunodeficiency with T-cell lymphopenia*, *Scientific Reports*, May 2018, DOI: https://doi.org/10.1038/s41598-018-25260-8; relevant chiefly for distinguishing partial from complete deficiency. (nemoto2018compoundheterozygoustyk2 pages 7-9)

**Knowledge-base recommendation:** represent complete biallelic-null TYK2 deficiency as a distinct disease node, while linking but not merging it with partial TYK2 deficiency and TYK2 p.Pro1104Ala-associated tuberculosis susceptibility. This separation is required because cytokine defects, penetrance and clinical management differ substantially across these molecular forms. (ogishi2022impairedil23–dependentinduction pages 15-17, ogishi2022impairedil23–dependentinduction pages 7-9, ogishi2022impairedil23–dependentinduction pages 2-3)

References

1. (OpenTargets Search: immunodeficiency 35,TYK2 deficiency-TYK2): Open Targets Query (immunodeficiency 35,TYK2 deficiency-TYK2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (sarrafzadeh2020anewpatient pages 1-3): Shokouh Azam Sarrafzadeh, Maryam Mahloojirad, Jean-Laurent Casanova, Mohsen Badalzadeh, Jacinta Bustamante, Stephanie Boisson-Dupuis, Zahra Pourpak, Maryam Nourizadeh, and Mostafa Moin. A new patient with inherited tyk2 deficiency. Journal of Clinical Immunology, 40:232-235, Nov 2020. URL: https://doi.org/10.1007/s10875-019-00713-5, doi:10.1007/s10875-019-00713-5. This article has 39 citations and is from a domain leading peer-reviewed journal.

3. (ogishi2022impairedil23–dependentinduction pages 4-6): Masato Ogishi, Andrés Augusto Arias, Rui Yang, Ji Eun Han, Peng Zhang, Darawan Rinchai, Joshua Halpern, Jeanette Mulwa, Narelle Keating, Maya Chrabieh, Candice Lainé, Yoann Seeleuthner, Noé Ramírez-Alejo, Nioosha Nekooie-Marnany, Andrea Guennoun, Ingrid Muller-Fleckenstein, Bernhard Fleckenstein, Sara S. Kilic, Yoshiyuki Minegishi, Stephan Ehl, Petra Kaiser-Labusch, Yasemin Kendir-Demirkol, Flore Rozenberg, Abderrahmane Errami, Shen-Ying Zhang, Qian Zhang, Jonathan Bohlen, Quentin Philippot, Anne Puel, Emmanuelle Jouanguy, Zahra Pourmoghaddas, Shahrzad Bakhtiar, Andre M. Willasch, Gerd Horneff, Genevieve Llanora, Lynette P. Shek, Louis Y.A. Chai, Sen Hee Tay, Hamid H. Rahimi, Seyed Alireza Mahdaviani, Serdar Nepesov, Aziz A. Bousfiha, Emine Hafize Erdeniz, Adem Karbuz, Nico Marr, Carmen Navarrete, Mehdi Adeli, Lennart Hammarstrom, Hassan Abolhassani, Nima Parvaneh, Saleh Al Muhsen, Mohammed F. Alosaimi, Fahad Alsohime, Maryam Nourizadeh, Mostafa Moin, Rand Arnaout, Saad Alshareef, Jamila El-Baghdadi, Ferah Genel, Roya Sherkat, Ayça Kiykim, Esra Yücel, Sevgi Keles, Jacinta Bustamante, Laurent Abel, Jean-Laurent Casanova, and Stéphanie Boisson-Dupuis. Impaired il-23–dependent induction of ifn-γ underlies mycobacterial disease in patients with inherited tyk2 deficiency. The Journal of Experimental Medicine, Sep 2022. URL: https://doi.org/10.1084/jem.20220094, doi:10.1084/jem.20220094. This article has 83 citations.

4. (ogishi2022impairedil23–dependentinduction pages 2-3): Masato Ogishi, Andrés Augusto Arias, Rui Yang, Ji Eun Han, Peng Zhang, Darawan Rinchai, Joshua Halpern, Jeanette Mulwa, Narelle Keating, Maya Chrabieh, Candice Lainé, Yoann Seeleuthner, Noé Ramírez-Alejo, Nioosha Nekooie-Marnany, Andrea Guennoun, Ingrid Muller-Fleckenstein, Bernhard Fleckenstein, Sara S. Kilic, Yoshiyuki Minegishi, Stephan Ehl, Petra Kaiser-Labusch, Yasemin Kendir-Demirkol, Flore Rozenberg, Abderrahmane Errami, Shen-Ying Zhang, Qian Zhang, Jonathan Bohlen, Quentin Philippot, Anne Puel, Emmanuelle Jouanguy, Zahra Pourmoghaddas, Shahrzad Bakhtiar, Andre M. Willasch, Gerd Horneff, Genevieve Llanora, Lynette P. Shek, Louis Y.A. Chai, Sen Hee Tay, Hamid H. Rahimi, Seyed Alireza Mahdaviani, Serdar Nepesov, Aziz A. Bousfiha, Emine Hafize Erdeniz, Adem Karbuz, Nico Marr, Carmen Navarrete, Mehdi Adeli, Lennart Hammarstrom, Hassan Abolhassani, Nima Parvaneh, Saleh Al Muhsen, Mohammed F. Alosaimi, Fahad Alsohime, Maryam Nourizadeh, Mostafa Moin, Rand Arnaout, Saad Alshareef, Jamila El-Baghdadi, Ferah Genel, Roya Sherkat, Ayça Kiykim, Esra Yücel, Sevgi Keles, Jacinta Bustamante, Laurent Abel, Jean-Laurent Casanova, and Stéphanie Boisson-Dupuis. Impaired il-23–dependent induction of ifn-γ underlies mycobacterial disease in patients with inherited tyk2 deficiency. The Journal of Experimental Medicine, Sep 2022. URL: https://doi.org/10.1084/jem.20220094, doi:10.1084/jem.20220094. This article has 83 citations.

5. (sarrafzadeh2020anewpatient pages 3-4): Shokouh Azam Sarrafzadeh, Maryam Mahloojirad, Jean-Laurent Casanova, Mohsen Badalzadeh, Jacinta Bustamante, Stephanie Boisson-Dupuis, Zahra Pourpak, Maryam Nourizadeh, and Mostafa Moin. A new patient with inherited tyk2 deficiency. Journal of Clinical Immunology, 40:232-235, Nov 2020. URL: https://doi.org/10.1007/s10875-019-00713-5, doi:10.1007/s10875-019-00713-5. This article has 39 citations and is from a domain leading peer-reviewed journal.

6. (ogishi2022impairedil23–dependentinduction pages 12-15): Masato Ogishi, Andrés Augusto Arias, Rui Yang, Ji Eun Han, Peng Zhang, Darawan Rinchai, Joshua Halpern, Jeanette Mulwa, Narelle Keating, Maya Chrabieh, Candice Lainé, Yoann Seeleuthner, Noé Ramírez-Alejo, Nioosha Nekooie-Marnany, Andrea Guennoun, Ingrid Muller-Fleckenstein, Bernhard Fleckenstein, Sara S. Kilic, Yoshiyuki Minegishi, Stephan Ehl, Petra Kaiser-Labusch, Yasemin Kendir-Demirkol, Flore Rozenberg, Abderrahmane Errami, Shen-Ying Zhang, Qian Zhang, Jonathan Bohlen, Quentin Philippot, Anne Puel, Emmanuelle Jouanguy, Zahra Pourmoghaddas, Shahrzad Bakhtiar, Andre M. Willasch, Gerd Horneff, Genevieve Llanora, Lynette P. Shek, Louis Y.A. Chai, Sen Hee Tay, Hamid H. Rahimi, Seyed Alireza Mahdaviani, Serdar Nepesov, Aziz A. Bousfiha, Emine Hafize Erdeniz, Adem Karbuz, Nico Marr, Carmen Navarrete, Mehdi Adeli, Lennart Hammarstrom, Hassan Abolhassani, Nima Parvaneh, Saleh Al Muhsen, Mohammed F. Alosaimi, Fahad Alsohime, Maryam Nourizadeh, Mostafa Moin, Rand Arnaout, Saad Alshareef, Jamila El-Baghdadi, Ferah Genel, Roya Sherkat, Ayça Kiykim, Esra Yücel, Sevgi Keles, Jacinta Bustamante, Laurent Abel, Jean-Laurent Casanova, and Stéphanie Boisson-Dupuis. Impaired il-23–dependent induction of ifn-γ underlies mycobacterial disease in patients with inherited tyk2 deficiency. The Journal of Experimental Medicine, Sep 2022. URL: https://doi.org/10.1084/jem.20220094, doi:10.1084/jem.20220094. This article has 83 citations.

7. (boissondupuis2018tuberculosisandimpaired pages 5-6): Stéphanie Boisson-Dupuis, Noe Ramirez-Alejo, Zhi Li, Etienne Patin, Geetha Rao, Gaspard Kerner, Che Kang Lim, Dimitry N. Krementsov, Nicholas Hernandez, Cindy S. Ma, Qian Zhang, Janet Markle, Ruben Martinez-Barricarte, Kathryn Payne, Robert Fisch, Caroline Deswarte, Joshua Halpern, Matthieu Bouaziz, Jeanette Mulwa, Durga Sivanesan, Tomi Lazarov, Rodrigo Naves, Patricia Garcia, Yuval Itan, Bertrand Boisson, Alix Checchi, Fabienne Jabot-Hanin, Aurélie Cobat, Andrea Guennoun, Carolyn C. Jackson, Sevgi Pekcan, Zafer Caliskaner, Jaime Inostroza, Beatriz Tavares Costa-Carvalho, Jose Antonio Tavares de Albuquerque, Humberto Garcia-Ortiz, Lorena Orozco, Tayfun Ozcelik, Ahmed Abid, Ismail Abderahmani Rhorfi, Hicham Souhi, Hicham Naji Amrani, Adil Zegmout, Frédéric Geissmann, Stephen W. Michnick, Ingrid Muller-Fleckenstein, Bernhard Fleckenstein, Anne Puel, Michael J. Ciancanelli, Nico Marr, Hassan Abolhassani, María Elvira Balcells, Antonio Condino-Neto, Alexis Strickler, Katia Abarca, Cory Teuscher, Hans D. Ochs, Ismail Reisli, Esra H. Sayar, Jamila El-Baghdadi, Jacinta Bustamante, Lennart Hammarström, Stuart G. Tangye, Sandra Pellegrini, Lluis Quintana-Murci, Laurent Abel, and Jean-Laurent Casanova. Tuberculosis and impaired il-23–dependent ifn-γ immunity in humans homozygous for a common tyk2 missense variant. Science Immunology, Dec 2018. URL: https://doi.org/10.1126/sciimmunol.aau8714, doi:10.1126/sciimmunol.aau8714. This article has 246 citations and is from a highest quality peer-reviewed journal.

8. (ogishi2022impairedil23–dependentinduction pages 15-17): Masato Ogishi, Andrés Augusto Arias, Rui Yang, Ji Eun Han, Peng Zhang, Darawan Rinchai, Joshua Halpern, Jeanette Mulwa, Narelle Keating, Maya Chrabieh, Candice Lainé, Yoann Seeleuthner, Noé Ramírez-Alejo, Nioosha Nekooie-Marnany, Andrea Guennoun, Ingrid Muller-Fleckenstein, Bernhard Fleckenstein, Sara S. Kilic, Yoshiyuki Minegishi, Stephan Ehl, Petra Kaiser-Labusch, Yasemin Kendir-Demirkol, Flore Rozenberg, Abderrahmane Errami, Shen-Ying Zhang, Qian Zhang, Jonathan Bohlen, Quentin Philippot, Anne Puel, Emmanuelle Jouanguy, Zahra Pourmoghaddas, Shahrzad Bakhtiar, Andre M. Willasch, Gerd Horneff, Genevieve Llanora, Lynette P. Shek, Louis Y.A. Chai, Sen Hee Tay, Hamid H. Rahimi, Seyed Alireza Mahdaviani, Serdar Nepesov, Aziz A. Bousfiha, Emine Hafize Erdeniz, Adem Karbuz, Nico Marr, Carmen Navarrete, Mehdi Adeli, Lennart Hammarstrom, Hassan Abolhassani, Nima Parvaneh, Saleh Al Muhsen, Mohammed F. Alosaimi, Fahad Alsohime, Maryam Nourizadeh, Mostafa Moin, Rand Arnaout, Saad Alshareef, Jamila El-Baghdadi, Ferah Genel, Roya Sherkat, Ayça Kiykim, Esra Yücel, Sevgi Keles, Jacinta Bustamante, Laurent Abel, Jean-Laurent Casanova, and Stéphanie Boisson-Dupuis. Impaired il-23–dependent induction of ifn-γ underlies mycobacterial disease in patients with inherited tyk2 deficiency. The Journal of Experimental Medicine, Sep 2022. URL: https://doi.org/10.1084/jem.20220094, doi:10.1084/jem.20220094. This article has 83 citations.

9. (ogishi2022impairedil23–dependentinduction pages 7-9): Masato Ogishi, Andrés Augusto Arias, Rui Yang, Ji Eun Han, Peng Zhang, Darawan Rinchai, Joshua Halpern, Jeanette Mulwa, Narelle Keating, Maya Chrabieh, Candice Lainé, Yoann Seeleuthner, Noé Ramírez-Alejo, Nioosha Nekooie-Marnany, Andrea Guennoun, Ingrid Muller-Fleckenstein, Bernhard Fleckenstein, Sara S. Kilic, Yoshiyuki Minegishi, Stephan Ehl, Petra Kaiser-Labusch, Yasemin Kendir-Demirkol, Flore Rozenberg, Abderrahmane Errami, Shen-Ying Zhang, Qian Zhang, Jonathan Bohlen, Quentin Philippot, Anne Puel, Emmanuelle Jouanguy, Zahra Pourmoghaddas, Shahrzad Bakhtiar, Andre M. Willasch, Gerd Horneff, Genevieve Llanora, Lynette P. Shek, Louis Y.A. Chai, Sen Hee Tay, Hamid H. Rahimi, Seyed Alireza Mahdaviani, Serdar Nepesov, Aziz A. Bousfiha, Emine Hafize Erdeniz, Adem Karbuz, Nico Marr, Carmen Navarrete, Mehdi Adeli, Lennart Hammarstrom, Hassan Abolhassani, Nima Parvaneh, Saleh Al Muhsen, Mohammed F. Alosaimi, Fahad Alsohime, Maryam Nourizadeh, Mostafa Moin, Rand Arnaout, Saad Alshareef, Jamila El-Baghdadi, Ferah Genel, Roya Sherkat, Ayça Kiykim, Esra Yücel, Sevgi Keles, Jacinta Bustamante, Laurent Abel, Jean-Laurent Casanova, and Stéphanie Boisson-Dupuis. Impaired il-23–dependent induction of ifn-γ underlies mycobacterial disease in patients with inherited tyk2 deficiency. The Journal of Experimental Medicine, Sep 2022. URL: https://doi.org/10.1084/jem.20220094, doi:10.1084/jem.20220094. This article has 83 citations.

10. (ogishi2022impairedil23–dependentinduction pages 3-4): Masato Ogishi, Andrés Augusto Arias, Rui Yang, Ji Eun Han, Peng Zhang, Darawan Rinchai, Joshua Halpern, Jeanette Mulwa, Narelle Keating, Maya Chrabieh, Candice Lainé, Yoann Seeleuthner, Noé Ramírez-Alejo, Nioosha Nekooie-Marnany, Andrea Guennoun, Ingrid Muller-Fleckenstein, Bernhard Fleckenstein, Sara S. Kilic, Yoshiyuki Minegishi, Stephan Ehl, Petra Kaiser-Labusch, Yasemin Kendir-Demirkol, Flore Rozenberg, Abderrahmane Errami, Shen-Ying Zhang, Qian Zhang, Jonathan Bohlen, Quentin Philippot, Anne Puel, Emmanuelle Jouanguy, Zahra Pourmoghaddas, Shahrzad Bakhtiar, Andre M. Willasch, Gerd Horneff, Genevieve Llanora, Lynette P. Shek, Louis Y.A. Chai, Sen Hee Tay, Hamid H. Rahimi, Seyed Alireza Mahdaviani, Serdar Nepesov, Aziz A. Bousfiha, Emine Hafize Erdeniz, Adem Karbuz, Nico Marr, Carmen Navarrete, Mehdi Adeli, Lennart Hammarstrom, Hassan Abolhassani, Nima Parvaneh, Saleh Al Muhsen, Mohammed F. Alosaimi, Fahad Alsohime, Maryam Nourizadeh, Mostafa Moin, Rand Arnaout, Saad Alshareef, Jamila El-Baghdadi, Ferah Genel, Roya Sherkat, Ayça Kiykim, Esra Yücel, Sevgi Keles, Jacinta Bustamante, Laurent Abel, Jean-Laurent Casanova, and Stéphanie Boisson-Dupuis. Impaired il-23–dependent induction of ifn-γ underlies mycobacterial disease in patients with inherited tyk2 deficiency. The Journal of Experimental Medicine, Sep 2022. URL: https://doi.org/10.1084/jem.20220094, doi:10.1084/jem.20220094. This article has 83 citations.

11. (bustamante2020mendeliansusceptibilityto pages 5-6): Jacinta Bustamante. Mendelian susceptibility to mycobacterial disease: recent discoveries. Human Genetics, 139:993-1000, Feb 2020. URL: https://doi.org/10.1007/s00439-020-02120-y, doi:10.1007/s00439-020-02120-y. This article has 232 citations and is from a peer-reviewed journal.

12. (meyts2021viralinfectionsin pages 13-14): Isabelle Meyts and Jean‐Laurent Casanova. Viral infections in humans and mice with genetic deficiencies of the type i ifn response pathway. Apr 2021. URL: https://doi.org/10.1002/eji.202048793, doi:10.1002/eji.202048793. This article has 128 citations and is from a peer-reviewed journal.

13. (muromoto2022currentunderstandingof pages 2-4): Ryuta Muromoto, Kenji Oritani, and Tadashi Matsuda. Current understanding of the role of tyrosine kinase 2 signaling in immune responses. World Journal of Biological Chemistry, 13:1-14, Jan 2022. URL: https://doi.org/10.4331/wjbc.v13.i1.1, doi:10.4331/wjbc.v13.i1.1. This article has 88 citations.

14. (muromoto2022currentunderstandingof pages 1-2): Ryuta Muromoto, Kenji Oritani, and Tadashi Matsuda. Current understanding of the role of tyrosine kinase 2 signaling in immune responses. World Journal of Biological Chemistry, 13:1-14, Jan 2022. URL: https://doi.org/10.4331/wjbc.v13.i1.1, doi:10.4331/wjbc.v13.i1.1. This article has 88 citations.

15. (nemoto2018compoundheterozygoustyk2 pages 1-2): Michiko Nemoto, Hiroyoshi Hattori, Naoko Maeda, Nobuhiro Akita, Hideki Muramatsu, Suzuko Moritani, Tomonori Kawasaki, Masami Maejima, Hirotaka Ode, Atsuko Hachiya, Wataru Sugiura, Yoshiyuki Yokomaku, Keizo Horibe, and Yasumasa Iwatani. Compound heterozygous tyk2 mutations underlie primary immunodeficiency with t-cell lymphopenia. Scientific Reports, May 2018. URL: https://doi.org/10.1038/s41598-018-25260-8, doi:10.1038/s41598-018-25260-8. This article has 47 citations and is from a peer-reviewed journal.

16. (nemoto2018compoundheterozygoustyk2 pages 7-9): Michiko Nemoto, Hiroyoshi Hattori, Naoko Maeda, Nobuhiro Akita, Hideki Muramatsu, Suzuko Moritani, Tomonori Kawasaki, Masami Maejima, Hirotaka Ode, Atsuko Hachiya, Wataru Sugiura, Yoshiyuki Yokomaku, Keizo Horibe, and Yasumasa Iwatani. Compound heterozygous tyk2 mutations underlie primary immunodeficiency with t-cell lymphopenia. Scientific Reports, May 2018. URL: https://doi.org/10.1038/s41598-018-25260-8, doi:10.1038/s41598-018-25260-8. This article has 47 citations and is from a peer-reviewed journal.

17. (muromoto2022currentunderstandingof pages 6-7): Ryuta Muromoto, Kenji Oritani, and Tadashi Matsuda. Current understanding of the role of tyrosine kinase 2 signaling in immune responses. World Journal of Biological Chemistry, 13:1-14, Jan 2022. URL: https://doi.org/10.4331/wjbc.v13.i1.1, doi:10.4331/wjbc.v13.i1.1. This article has 88 citations.

18. (muromoto2022currentunderstandingof pages 4-6): Ryuta Muromoto, Kenji Oritani, and Tadashi Matsuda. Current understanding of the role of tyrosine kinase 2 signaling in immune responses. World Journal of Biological Chemistry, 13:1-14, Jan 2022. URL: https://doi.org/10.4331/wjbc.v13.i1.1, doi:10.4331/wjbc.v13.i1.1. This article has 88 citations.

19. (muromoto2021therapeuticadvantageof pages 2-4): Ryuta Muromoto, Kazuya Shimoda, Kenji Oritani, and Tadashi Matsuda. Therapeutic advantage of tyk2 inhibition for treating autoimmune and chronic inflammatory diseases. Biological & pharmaceutical bulletin, 44 11:1585-1592, Nov 2021. URL: https://doi.org/10.1248/bpb.b21-00609, doi:10.1248/bpb.b21-00609. This article has 30 citations and is from a peer-reviewed journal.

20. (muromoto2022currentunderstandingof pages 7-8): Ryuta Muromoto, Kenji Oritani, and Tadashi Matsuda. Current understanding of the role of tyrosine kinase 2 signaling in immune responses. World Journal of Biological Chemistry, 13:1-14, Jan 2022. URL: https://doi.org/10.4331/wjbc.v13.i1.1, doi:10.4331/wjbc.v13.i1.1. This article has 88 citations.

## Artifacts

- [Edison artifact artifact-00](Immunodeficiency_35-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012682` (6 mentions) - the report calls it "if available"; MONDO calls it **immunodeficiency 35**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.