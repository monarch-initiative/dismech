---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-31T17:32:38.525667'
end_time: '2026-08-31T17:52:58.939798'
duration_seconds: 1220.41
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Revesz syndrome (TINF2-associated dyskeratosis congenita with bilateral
    exudative retinopathy and intracranial calcification)
  mondo_id: MONDO:0009990
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 40
  verified: 39
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0009990
    reported_labels:
    - if available
    ontology_label: Revesz syndrome
  obsolete_terms:
  - term_id: GO:0000784
    ontology_label: GO_0000784
    replaced_by: GO:0000781
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Revesz_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Revesz syndrome (TINF2-associated dyskeratosis congenita with bilateral exudative retinopathy and intracranial calcification)
- **MONDO ID:** MONDO:0009990 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Revesz syndrome (TINF2-associated dyskeratosis congenita with bilateral exudative retinopathy and intracranial calcification)** covering all of the
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
- **Disease Name:** Revesz syndrome (TINF2-associated dyskeratosis congenita with bilateral exudative retinopathy and intracranial calcification)
- **MONDO ID:** MONDO:0009990 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Revesz syndrome (TINF2-associated dyskeratosis congenita with bilateral exudative retinopathy and intracranial calcification)** covering all of the
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


# Revesz Syndrome: Comprehensive Disease-Characteristics Report

**Target entity:** Revesz syndrome (RS), a severe, early-onset telomere biology disorder (TBD), usually caused by heterozygous pathogenic **TINF2** variants and characterized by early bone-marrow failure, bilateral exudative retinopathy, and intracranial abnormalities.

**Evidence boundary.** RS is exceptionally rare. The strongest RS-specific quantitative source remains the systematic review of 18 children published by Karremann et al. on **7 October 2020** (DOI: [10.1186/s13023-020-01553-y](https://doi.org/10.1186/s13023-020-01553-y)). No 2023–2024 RS-specific cohort superseding it was identified. Consequently, this report labels recommendations derived from the broader DC/TBD literature as **TBD extrapolation**, rather than presenting them as demonstrated RS evidence. The underlying data are aggregated disease-level literature and case reports, not individual-level EHR data. (karremann2020reveszsyndromerevisited pages 8-9, karremann2020reveszsyndromerevisited pages 1-2, rolles2024inheritedtelomerebiology pages 8-9)

The following table provides a knowledge-base-oriented synopsis.

| Domain | Best-supported finding | Quantitative detail | Evidence type | Knowledge-base ontology suggestions |
|---|---|---|---|---|
| Disease identifiers | Revesz syndrome is an ultra-rare, severe pediatric telomere biology disorder within the dyskeratosis congenita spectrum, classically defined by bilateral exudative retinopathy plus intracranial calcification/cerebellar hypoplasia and early bone marrow failure; OMIM #268130 and MONDO:0009990 are supported in retrieved sources | 18 children summarized in the largest RS-specific review; all pediatric cases (karremann2020reveszsyndromerevisited pages 1-2, karremann2020reveszsyndromerevisited pages 7-8, rolles2024inheritedtelomerebiology pages 8-9, OpenTargets Search: Revesz syndrome-TINF2) | RS-specific systematic review + broader TBD review | MONDO:0009990; MeSH: Dyskeratosis Congenita; HPO: HP:0001872 Pancytopenia, HP:0000510 Blindness, HP:0009713 Nail dystrophy |
| Synonyms / nomenclature | RS is best treated as a disease-level, aggregated literature-defined syndrome; recent sources also describe it as an early severe pediatric TBD and a TINF2-associated dyskeratosis congenita variant | No EHR-derived cohort identified; evidence comes from published case reports/reviews (karremann2020reveszsyndromerevisited pages 1-2, rolles2024inheritedtelomerebiology pages 8-9) | RS-specific + broader TBD extrapolation | MONDO label plus exact synonym string: TINF2-associated dyskeratosis congenita with bilateral exudative retinopathy and intracranial calcification |
| Epidemiology / demographics | Extremely rare; no population prevalence or incidence was identified. Reported sex distribution does not support strong male predominance | 18 cases total; 7 female, 11 male; median survival 6.5 years; none survived beyond 12 years in the 2020 review (karremann2020reveszsyndromerevisited pages 7-8, karremann2020reveszsyndromerevisited pages 1-2) | RS-specific systematic review | HANCESTRO/NCIT demographic annotations as available; evidence gap flag for prevalence/incidence |
| Inheritance | RS is usually caused by de novo heterozygous TINF2 variants, although TINF2-related TBDs more broadly can also show autosomal dominant familial inheritance and anticipation | In reviewed RS cases, all genetically characterized patients reportedly had unaffected parents/de novo events; TINF2 often de novo in broader TBDs (karremann2020reveszsyndromerevisited pages 7-8, savage2022dyskeratosiscongenitaand pages 8-10, rolles2024inheritedtelomerebiology pages 2-4) | RS-specific + broader TBD extrapolation | HP:0000006 Autosomal dominant inheritance; HP:0032113 De novo mutation |
| Causal gene | TINF2 is the established causal gene for RS | Open Targets shows Revesz syndrome–TINF2 association; evidence size 5 (OpenTargets Search: Revesz syndrome-TINF2) | Disease-target association + RS review | HGNC: TINF2; NCBI Gene: TINF2; GO CC: shelterin complex |
| Pathogenic variants | RS-associated variants cluster in TINF2 exon 6, especially around amino acids 280-289; p.Arg282His is the most recurrent hotspot. Truncating variants can also produce severe early phenotypes including RS | In historical TINF2-DC series, c.845G>A (p.Arg282His) accounted for 12 DC, 2 DC/RS, 1 DC/HH/RS probands; RS also reported with c.839delA (p.Lys280Argfs*36); mosaic c.865C>T (p.Pro289Ser) reported in an RS case (sasa2012threenoveltruncating pages 3-4, tomcikova2018whyisit pages 1-2, karremann2020reveszsyndromerevisited pages 7-8) | RS-specific cases + TINF2 variant series | HGVS variant annotations; SO:0001583 missense_variant, SO:0001589 frameshift_variant, SO:0001587 stop_gained |
| Telomere biomarker | Very short telomeres are a defining functional biomarker in RS and early severe TBDs | In 7 RS patients with measurements, telomeres were below the 1st percentile for age; example RS case telomeres 2.47-2.48 kb (karremann2020reveszsyndromerevisited pages 7-8, karremann2020reveszsyndromerevisited pages 4-7, rolles2024inheritedtelomerebiology pages 8-9) | RS-specific review/case + broader TBD review | HPO: HP:0034004 Short telomere; LOINC/assay annotation for flow-FISH telomere length |
| Core phenotype: bone marrow failure | Early bone marrow failure is universal or near-universal in RS and often the dominant life-limiting manifestation | All reviewed patients had early BMF; onset median 1.5 years, within second year; all by age 6 years (karremann2020reveszsyndromerevisited pages 1-2, karremann2020reveszsyndromerevisited pages 7-8) | RS-specific systematic review | HPO: HP:0001876 Pancytopenia, HP:0005528 Bone marrow hypocellularity |
| Core phenotype: retinopathy | Bilateral exudative retinopathy is a defining RS feature and can be the presenting manifestation | Retinopathy in all patients with available data; median onset 1.1 years, typically 6-18 months; severe visual loss common; glaucoma in 3 cases (karremann2020reveszsyndromerevisited pages 1-2, karremann2020reveszsyndromerevisited pages 7-8, tomcikova2018whyisit pages 1-2, rolles2024inheritedtelomerebiology pages 8-9) | RS-specific systematic review + case reports | HPO: HP:0000555 Exudative retinopathy, HP:0011003 Retinal detachment, HP:0000501 Glaucoma; UBERON: retina |
| Core phenotype: intracranial abnormalities | Intracranial calcifications and cerebellar hypoplasia are common neurologic hallmarks; neurodevelopmental delay is frequent but variable | Intracranial calcifications 85%; cerebellar hypoplasia 76%; neurodevelopmental delay/mental retardation 71%; seizures about 20%; intracranial hemorrhage in 3 cases (karremann2020reveszsyndromerevisited pages 7-8, karremann2020reveszsyndromerevisited pages 9-11, rolles2024inheritedtelomerebiology pages 8-9) | RS-specific systematic review + review | HPO: HP:0002521 Cerebral calcification, HP:0001321 Cerebellar hypoplasia, HP:0001263 Developmental delay, HP:0001250 Seizure |
| Other phenotype features | Classical dyskeratosis congenita mucocutaneous triad is less consistently expressed in RS, likely because of early severe course; growth restriction and fine/sparse hair are common | Only 2 RS cases had complete classic DKC triad in the 2020 review; growth retardation frequent qualitatively (karremann2020reveszsyndromerevisited pages 8-9, rolles2024inheritedtelomerebiology pages 8-9) | RS-specific review | HPO: HP:0001510 Growth delay, HP:0002219 Sparse hair, HP:0001597 Aplasia/hypoplasia of the skin pigmentation pattern |
| Mechanism | Germline TINF2 mutation disrupts TIN2, a central shelterin component linking TRF1/TRF2 with TPP1/POT1, leading to defective telomere protection/regulation, accelerated telomere shortening, stem-cell replicative exhaustion, and multisystem degeneration. Specific interaction defects vary by variant class | TIN2 mutants cluster in DC hotspot; truncation mutant severely impaired TRF1 interaction; TIN2L/TRF2 and TIN2L/TRF1 interactions are altered by DC-cluster mutations; TINF2 consequences considered multifactorial in broader TBD reviews (nelson2018thecterminalextension pages 1-3, sasa2012threenoveltruncating pages 1-3, savage2022dyskeratosiscongenitaand pages 8-10, rolles2024inheritedtelomerebiology pages 2-4) | Biochemical/in vitro + human genetics + broader TBD review | GO:0000784 nuclear chromosome telomeric region, GO:0032200 telomere organization, GO:0003691 double-stranded telomeric DNA binding, GO:0090398 cellular senescence |
| Cell and tissue vulnerability | High-turnover stem-cell compartments are most vulnerable; pathology extends beyond blood to retina/CNS and other organs. Tissue-specific shortening may be most severe outside donor-derived hematopoiesis | Broader TBD reviews emphasize HSCs, immune cells, intestinal cells, liver, lung, skin; autopsy in TINF2-DC showed shortest telomeres in lung, liver, kidney and age-appropriate donor hematopoietic tissue after transplant (rolles2024inheritedtelomerebiology pages 2-4, roake2021tissuespecifictelomereshortening pages 1-2) | Broader TBD review + TINF2 human pathology case | CL: hematopoietic stem cell, lymphocyte; UBERON: bone marrow, retina, cerebellum, brain, liver, lung, kidney |
| Diagnostic workflow | Best-supported workup is clinical recognition of RS features plus telomere testing and germline sequencing of TINF2/TBD genes; flow-FISH is the current clinical standard for functional screening | Age-adjusted lymphocyte telomere length <1st percentile is the commonly used threshold; WES/WGS/panel sequencing recommended after short TL or strong suspicion; chromosome breakage testing is recommended to exclude Fanconi anemia (rolles2024inheritedtelomerebiology pages 8-9, rolles2024inheritedtelomerebiology pages 12-14, rolles2024inheritedtelomerebiology pages 10-12, NCT06817590 chunk 1) | Broader TBD review/guidance, applicable to RS | HPO terms above; LOINC assay for telomere length by flow-FISH; SO/ClinVar variant classification |
| Differential diagnosis | Main differentials are other TBDs and inherited bone marrow failure disorders, especially Hoyeraal-Hreidarsson syndrome, Coats plus syndrome, and Fanconi anemia | Coats plus may show exudative retinopathy but not necessarily short telomeres; Fanconi anemia exclusion by mitomycin C/DEB testing is recommended in transplant diagnostic pathways (rolles2024inheritedtelomerebiology pages 8-9, rolles2024inheritedtelomerebiology pages 12-14, NCT01659606 chunk 1) | RS-specific/broader TBD reviews + trial eligibility criteria | MONDO/HPO mappings for Hoyeraal-Hreidarsson syndrome, Coats plus syndrome, Fanconi anemia |
| Prognosis | Prognosis is poor in RS, with death typically in childhood, although transplant may improve hematologic survival in some patients | Kaplan-Meier median survival 6.5 years (95% CI 3.6-9.4); no survival beyond 12 years in 2020 review (karremann2020reveszsyndromerevisited pages 7-8, karremann2020reveszsyndromerevisited pages 1-2) | RS-specific systematic review | NCIT prognosis annotation; HPO complication terms |
| Treatment: hematopoietic transplant | Allogeneic stem-cell transplantation is the only potentially curative therapy for marrow failure, but toxicity is a major concern; reduced-intensity, radiation/alkylator-sparing approaches are preferred in TBDs | In RS review, SCT in 8 children; 4 alive at last follow-up after median 22 months; deaths from pulmonary failure reported post-SCT. Broader TBD data note 10-year post-allo-SCT survival about 23% and benefit of non-myeloablative/radiation-avoiding protocols (karremann2020reveszsyndromerevisited pages 1-2, karremann2020reveszsyndromerevisited pages 9-11, rolles2024inheritedtelomerebiology pages 14-15) | RS-specific review + broader TBD extrapolation | NCIT: Hematopoietic Stem Cell Transplantation; NCIT: Reduced-Intensity Conditioning Regimen |
| Treatment: ophthalmic interventions | Vision-preserving therapy is disease-modifying for the eye but evidence is case-based; laser photocoagulation appears most supported, with anti-VEGF and surgery used in selected eyes | Reported interventions include photocoagulation, intraocular bevacizumab, retinocryopexy, vitrectomy, enucleation; one mosaic TINF2 RS case retained VA 0.9 in treated eye at age 7 after photocoagulation (karremann2020reveszsyndromerevisited pages 9-11, karremann2020reveszsyndromerevisited pages 4-7, tomcikova2018whyisit pages 1-2) | RS-specific case reports/review | NCIT: Laser Photocoagulation; NCIT: Bevacizumab; NCIT: Vitrectomy; NCIT: Enucleation |
| Supportive management | Multidisciplinary surveillance is essential because complications extend across hematologic, ophthalmologic, pulmonary, hepatic, neurologic, mucocutaneous, and cancer domains | No RS-specific formal guideline retrieved; 2022-2024 TBD reviews/guidelines recommend surveillance, specialized-center care, and family counseling (savage2022dyskeratosiscongenitaand pages 5-6, rolles2024inheritedtelomerebiology pages 14-15, NCT04959188 chunk 1) | Broader TBD extrapolation | NCIT care pathway terms; HPO surveillance-linked phenotypes |
| Pharmacotherapy / experimental systemic therapy | No RS-specific drug proven effective. Broader TBD evidence supports androgen responsiveness in some patients and emerging nucleotide/telomerase-directed strategies | Broader TBD: danazol hematologic response 50-100% short-term; 11/12 gained telomere length with mean +386 bp after 24 months in one study summarized in review; applicability to RS is unproven (rolles2024inheritedtelomerebiology pages 14-15, carvalho2022recentadvancesin pages 7-9, savage2022dyskeratosiscongenitaand pages 5-6) | Broader TBD extrapolation | CHEBI/DrugBank: danazol, oxymetholone, deoxycytidine, thymidine |
| Current RS-inclusive trials | RS is explicitly included in current TBD clinical trial frameworks rather than having RS-only trials | NCT01659606 active-not-recruiting phase 2 radiation- and alkylator-free HCT, estimated n=40, explicitly includes Revesz syndrome; NCT06817590 recruiting phase 1 oral deoxycytidine + deoxythymidine, estimated n=36, condition list explicitly includes Revesz syndrome; NCT04959188 completed needs-assessment study, n=53, included DC/TBD patients/caregivers (NCT01659606 chunk 1, NCT01659606 chunk 2, NCT06817590 chunk 1, NCT06817590 chunk 2, NCT04959188 chunk 1) | Trial registry evidence | NCIT: Clinical Trial; NCIT: Alemtuzumab/Fludarabine conditioning; CHEBI: deoxycytidine, thymidine |
| Model organisms / cellular models | No RS-specific animal model was directly retrieved, but TINF2/TBD mechanistic modeling exists in mouse and pluripotent stem-cell systems | TIN2 biochemical cell models show altered shelterin interactions; iPSC DC models recapitulate telomere maintenance defects and loss of self-renewal; a cited mouse study found a DC-associated TINF2 mutation causes telomerase-independent telomere shortening (nelson2018thecterminalextension pages 1-3, batista2011telomereshorteningand pages 1-3, nelson2018thecterminalextension pages 30-33) | In vitro/cellular + cited mouse-model evidence | MGI mouse model annotation; Cellosaurus/iPSC model tags; GO telomere maintenance |
| Environmental / modifier factors | No RS-specific environmental or protective factors were identified. In broader telomere disease literature, smoking, alcohol, viral infections, radiation, and pulmonary-toxic drugs may worsen organ phenotypes or treatment toxicity | Qualitative only; no RS-specific gene-environment study retrieved (carvalho2022recentadvancesin pages 7-9, rolles2024inheritedtelomerebiology pages 12-14) | Broader TBD extrapolation | CHEBI exposure annotations; evidence-gap flag |
| Explicit evidence gaps | Major RS evidence gaps remain: prevalence/incidence, penetrance, founder effects, carrier frequency, modifier genes, protective factors, epigenetics, transcriptomics/proteomics/metabolomics, QoL metrics, standardized diagnostic criteria, and controlled treatment-response data | No robust RS-specific 2023-2024 cohort superseding the 2020 review was retrieved; most modern data are TBD-wide extrapolations (karremann2020reveszsyndromerevisited pages 1-2, rolles2024inheritedtelomerebiology pages 8-9, savage2022dyskeratosiscongenitaand pages 5-6) | Evidence-gap synthesis | Evidence code tags for "not available" / "broader TBD extrapolation only" |


*Table: This table condenses the strongest retrieved evidence for Revesz syndrome across identifiers, genetics, phenotype, mechanism, diagnosis, prognosis, treatment, trials, and evidence gaps. It distinguishes Revesz-specific findings from broader telomere biology disorder extrapolations for knowledge-base use.*

## 1. Disease information

### Definition

RS is an ultra-rare, severe pediatric variant within the dyskeratosis congenita/telomere biology disorder spectrum. Its defining clinical combination is **bilateral exudative retinopathy**, early progressive marrow failure, and CNS abnormalities—particularly intracranial calcification and cerebellar hypoplasia. Unlike classic dyskeratosis congenita, the complete mucocutaneous triad of nail dystrophy, reticular pigmentation, and oral leukoplakia is uncommon at presentation, probably because RS begins and progresses before all age-dependent features can develop. (karremann2020reveszsyndromerevisited pages 8-9, karremann2020reveszsyndromerevisited pages 7-8, karremann2020reveszsyndromerevisited pages 1-2)

A concise direct quotation from the 2020 abstract is: **“RS is a severe variant of DKC with early bone marrow failure and retinopathy in all patients.”** (karremann2020reveszsyndromerevisited pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0009990.
- **OMIM:** #268130.
- **MeSH:** no uniquely retrieved RS descriptor; use the broader **Dyskeratosis Congenita, D019871**, with an RS subtype annotation.
- **ClinicalTrials.gov/MeSH supplementary concept:** “Revesz Debuse syndrome,” concept C538371.
- **ICD-10/ICD-11:** no specific RS code was identified. Coding generally falls under congenital marrow-failure, dyskeratosis congenita, retinal, and neurologic manifestations, depending on jurisdiction.
- **Synonyms:** Revesz syndrome; Revesz–Debuse syndrome; Revesz type dyskeratosis congenita; TINF2-associated Revesz syndrome; TINF2-associated dyskeratosis congenita with bilateral exudative retinopathy and intracranial calcification. (OpenTargets Search: Revesz syndrome-TINF2, karremann2020reveszsyndromerevisited pages 1-2, NCT06817590 chunk 2)

Open Targets links MONDO:0009990 specifically to **TINF2/ENSG00000092330**, supported by five association evidence records and literature including PMID **18252230** and **21477109**. (OpenTargets Search: Revesz syndrome-TINF2)

## 2. Etiology

### Causal factor

RS is primarily a **germline Mendelian disorder** caused by heterozygous pathogenic variants in **TINF2**, encoding TIN2, a central shelterin-complex protein. The causal lesion is constitutional rather than infectious, toxic, or acquired. Most genetically characterized RS cases have apparently de novo variants, although TINF2-related TBDs can be transmitted as autosomal-dominant disorders. (karremann2020reveszsyndromerevisited pages 7-8, sasa2012threenoveltruncating pages 1-3, savage2022dyskeratosiscongenitaand pages 8-10)

### Genetic risk factors

The dominant risk factor is a pathogenic TINF2 variant, especially within the narrow exon-6 dyskeratosis-congenita hotspot. Variants reported in RS or overlapping RS/Hoyeraal–Hreidarsson phenotypes include:

- **NM_001099274.1:c.845G>A, p.Arg282His**, the recurrent hotspot;
- **c.838A>T, p.Lys280Ter**;
- **c.839delA, p.Lys280ArgfsTer36**, a truncating RS-associated allele;
- **c.865C>T, p.Pro289Ser**, reported in mosaic form in one RS case.

The historical variant series showed p.Arg282His in 12 DC probands, two DC/RS probands, one DC/HH/RS proband, and two HH probands, illustrating that a TINF2 genotype does not map uniquely to one syndromic label. (tomcikova2018whyisit pages 1-2, sasa2012threenoveltruncating pages 1-3, sasa2012threenoveltruncating pages 3-4)

### Environmental, protective, and gene–environment factors

No environmental exposure is known to cause RS, and no validated genetic or environmental protective factor, modifier allele, founder effect, diet, or lifestyle intervention has been demonstrated specifically in RS. Broader TBD literature suggests that smoking, alcohol, viral infection, ionizing radiation, and pulmonary-toxic or DNA-damaging drugs may aggravate organ injury or treatment toxicity, but this is **not RS-specific evidence**. (rolles2024inheritedtelomerebiology pages 12-14, carvalho2022recentadvancesin pages 7-9)

## 3. Phenotypes

The frequencies below derive principally from 18 published children and are vulnerable to case-report ascertainment and incomplete reporting.

- **Bone-marrow failure/pancytopenia:** severe, progressive laboratory and clinical phenotype; effectively universal in the reviewed RS series. It occurred from 6 months to 6 years, with median onset **1.5 years**; all affected children had developed it by age six. Consequences include infection, bleeding, anemia, transfusion dependence, and transplant need. Suggested HPO: **HP:0001876 Pancytopenia**, **HP:0005528 Bone marrow hypocellularity**, **HP:0001903 Anemia**, **HP:0001873 Thrombocytopenia**, **HP:0001875 Neutropenia**. (karremann2020reveszsyndromerevisited pages 7-8, karremann2020reveszsyndromerevisited pages 1-2)
- **Bilateral exudative retinopathy:** defining, severe, and progressive; present in all 15 children for whom retinal data were available. Median onset was **1.1 years** (95% CI 0.7–1.5), usually at 6–18 months. It can progress to proliferative vitreoretinopathy, retinal detachment, neovascular glaucoma, blindness, and enucleation. Suggested HPO: **HP:0000555 Exudative retinopathy**, **HP:0011003 Retinal detachment**, **HP:0000501 Glaucoma**, **HP:0000510 Blindness**. (karremann2020reveszsyndromerevisited pages 8-9, karremann2020reveszsyndromerevisited pages 7-8, tomcikova2018whyisit pages 1-2)
- **Intracranial calcification:** imaging sign reported in approximately **85%**. Suggested HPO: **HP:0002514/HP:0002521 intracranial/cerebral calcification**; terminology should be verified against the current HPO release. (karremann2020reveszsyndromerevisited pages 7-8)
- **Cerebellar hypoplasia and ataxia:** cerebellar hypoplasia in approximately **76%**; generally congenital/developmental and non-reversible. Suggested HPO: **HP:0001321 Cerebellar hypoplasia**, **HP:0001251 Ataxia**. (karremann2020reveszsyndromerevisited pages 7-8, rolles2024inheritedtelomerebiology pages 8-9)
- **Developmental delay/intellectual impairment:** approximately **71%**, usually recognized in infancy or early childhood, with variable severity. Suggested HPO: **HP:0001263 Global developmental delay**, **HP:0001249 Intellectual disability**. (karremann2020reveszsyndromerevisited pages 7-8)
- **Seizures:** estimated cumulative frequency approximately **20%**, exclusively beginning in early childhood in the reviewed cases. Suggested HPO: **HP:0001250 Seizure**. (karremann2020reveszsyndromerevisited pages 1-2)
- **Intracranial hemorrhage:** three reviewed patients; potentially catastrophic. Suggested HPO: **HP:0002170 Intracranial hemorrhage**. (karremann2020reveszsyndromerevisited pages 9-11, karremann2020reveszsyndromerevisited pages 7-8)
- **Growth restriction:** intrauterine or postnatal, qualitatively common. Suggested HPO: **HP:0001511 Intrauterine growth retardation**, **HP:0001510 Growth delay**, **HP:0004322 Short stature**. (sasa2012threenoveltruncating pages 1-3, rolles2024inheritedtelomerebiology pages 8-9)
- **Mucocutaneous findings:** nail dystrophy was the most frequent element, with variable reticular pigmentation, oral leukoplakia, and fine/sparse hair. Only two children had the full classic DC triad. Suggested HPO: **HP:0001597 Abnormality of the nail**, **HP:0009713 Nail dystrophy**, **HP:0001000 Abnormality of skin pigmentation**, **HP:0002745 Oral leukoplakia**, **HP:0002219 Sparse hair**. (karremann2020reveszsyndromerevisited pages 8-9, rolles2024inheritedtelomerebiology pages 8-9)

No RS-specific EQ-5D, SF-36, PROMIS, or other standardized quality-of-life measurements were identified. Nevertheless, blindness, developmental disability, transfusion dependence, infection risk, and repeated hospitalization imply profound effects on mobility, education, communication, independence, and family burden. A completed NIH needs-assessment study enrolled 53 DC/TBD patients and caregivers, but it was not RS-specific. (NCT04959188 chunk 1)

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** TINF2, TERF1 interacting nuclear factor 2.
- **Ensembl:** ENSG00000092330.
- **Protein:** TIN2, a shelterin component linking TRF1/TRF2 to TPP1/POT1.
- **Inheritance:** autosomal dominant, usually de novo in severe pediatric TINF2 disease.
- **Origin:** constitutional/germline; mosaicism has occasionally been reported. These are not characteristically somatic cancer-driver lesions. (OpenTargets Search: Revesz syndrome-TINF2, nelson2018thecterminalextension pages 1-3, savage2022dyskeratosiscongenitaand pages 8-10)

### Variant classes and consequences

Both missense and truncating alleles occur. Stable truncated TIN2 protein was demonstrated in patient-derived lymphoblastoid cells, arguing against a simple null/haploinsufficiency model for all alleles. A truncation markedly impaired TIN2–TRF1 interaction, whereas common p.Arg282His had a smaller effect on that particular interaction. TINF2 pathogenesis is therefore best annotated as **multifactorial altered-function/dominant dysfunction**, with variant-dependent effects on shelterin organization, telomerase regulation, telomere cohesion, and end protection; a universal dominant-negative mechanism has not been proven. (sasa2012threenoveltruncating pages 1-3, nelson2018thecterminalextension pages 1-3, savage2022dyskeratosiscongenitaand pages 8-10)

The biochemical abstract states: **“TIN2 is central to the shelterin complex, linking the telomeric proteins TRF1 and TRF2 with TPP1/POT1.”** It further concludes that TIN2 isoforms are functionally distinguishable and that shelterin composition may be altered in patients with TINF2 mutations. (nelson2018thecterminalextension pages 1-3)

Population allele frequencies were not available in the retrieved evidence. Given severe early-onset disease and frequent de novo occurrence, established pathogenic RS alleles are expected to be absent or extremely rare in population databases, but each HGVS allele must be checked directly in current gnomAD and ClinVar before database ingestion. No recurrent RS-associated chromosomal rearrangement, aneuploidy, or large structural variant was identified.

### Modifiers and epigenetics

No validated RS modifier gene or disease-specific epigenetic signature is known. Somatic reversion has been reported in TINF2-related TBD more broadly and may obscure blood-based variant detection, occasionally making fibroblast DNA testing necessary. This has not been established as a protective mechanism in RS. (savage2022dyskeratosiscongenitaand pages 8-10)

## 5. Environmental information

RS is not infectious and has no zoonotic or contagious component. No toxin, pollutant, occupational exposure, smoking pattern, diet, exercise level, or alcohol exposure is established as etiologic. Because telomere-deficient tissues have limited regenerative reserve, avoidance of tobacco, excessive alcohol, unnecessary radiation, and organ-toxic medications is biologically and clinically prudent under general TBD management, but evidence is indirect for RS. (rolles2024inheritedtelomerebiology pages 12-14, carvalho2022recentadvancesin pages 7-9)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A **heterozygous germline TINF2 hotspot or truncating variant** leads to altered TIN2 structure or protein interactions.
2. Altered TIN2 leads to defective integration/regulation of the **TRF1–TIN2–TRF2–TPP1/POT1 shelterin network** and telomerase recruitment; the exact defect is variant-dependent.
3. Shelterin/telomerase dysregulation leads to exceptionally rapid telomere attrition and/or defective telomere capping; telomerase-independent shortening has been demonstrated in a Tinf2-mutant mouse model.
4. Critically short or uncapped telomeres lead to DNA-damage signaling, chromosome instability, senescence, apoptosis, and loss of self-renewal.
5. Stem/progenitor-cell exhaustion leads directly to failure of high-turnover tissues—most demonstrably hematopoietic stem/progenitor cells—resulting in hypocellular marrow and pancytopenia.
6. **Retinal branch:** telomere-associated vascular/endothelial or supporting-cell dysfunction is inferred to lead to peripheral capillary nonperfusion, leakage, neovascularization, exudation, retinal detachment, glaucoma, and blindness; this cell-level sequence remains incompletely demonstrated in RS.
7. **Neurodevelopmental branch:** developmental telomere dysfunction is inferred to disrupt cerebellar and cerebral growth and microvascular integrity, resulting in cerebellar hypoplasia, calcification, white-matter abnormalities, developmental delay, seizures, and occasional hemorrhage.
8. **Systemic branch:** limited tissue regenerative capacity leads to mucocutaneous degeneration, growth restriction, infection susceptibility, and later pulmonary/hepatic complications, compounded in some patients by treatment toxicity. (karremann2020reveszsyndromerevisited pages 9-11, sasa2012threenoveltruncating pages 1-3, nelson2018thecterminalextension pages 1-3, nelson2018thecterminalextension pages 30-33, rolles2024inheritedtelomerebiology pages 2-4, rolles2024inheritedtelomerebiology pages 10-12)

### Processes and ontology suggestions

Relevant GO concepts include **telomere maintenance (GO:0000723)**, **telomere organization (GO:0032200)**, **protein localization to chromosome, telomeric region**, **DNA-damage response**, **cellular senescence (GO:0090398)**, **stem-cell population maintenance (GO:0019827)**, and **apoptotic process (GO:0006915)**. Relevant cellular components include **nuclear chromosome telomeric region (GO:0000784)** and **shelterin complex**. Candidate CL annotations include **hematopoietic stem cell**, hematopoietic progenitor cell, retinal endothelial cell, retinal pigment epithelial cell, photoreceptor cell, neuron, cerebellar granule cell, and glial cell; only hematopoietic stem-cell involvement is strongly demonstrated, while the exact retinal/CNS target populations remain uncertain.

No RS-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omics dataset was identified. DC iPSCs recapitulate telomere-maintenance defects and eventual loss of self-renewal, but the retrieved iPSC study did not specifically model RS/TINF2. (batista2011telomereshorteningand pages 1-3)

## 7. Anatomical structures affected

Primary sites are:

- **Bone marrow/hematopoietic system**—hematopoietic stem and progenitor compartments; UBERON: bone marrow.
- **Both retinas and retinal vasculature**—bilateral by definition; UBERON: retina, retinal blood vessel, vitreous body.
- **Brain**, especially cerebellum and periventricular white matter; UBERON: brain, cerebellum, cerebral white matter, ventricular system.
- **Skin, nails, oral mucosa, and hair follicles**.
- Secondary or later TBD-associated involvement may include **lung, liver, gastrointestinal tract, kidney, and immune system**.

A TINF2-DC autopsy—not a classic RS case—showed donor-derived hematopoietic tissue with age-appropriate telomeres but severe shortening in native tissues, especially lung, liver, and kidney, supporting tissue-specific vulnerability beyond marrow. (karremann2020reveszsyndromerevisited pages 7-8, karremann2020reveszsyndromerevisited pages 4-7, rolles2024inheritedtelomerebiology pages 8-9, roake2021tissuespecifictelomereshortening pages 1-2)

At the subcellular level, the principal compartment is the **nucleus**, particularly telomeric chromatin and shelterin at chromosome ends.

## 8. Temporal development

RS is congenital in genetic origin and usually manifests during infancy. Retinopathy generally appears at 6–18 months, often before or alongside hematologic disease. Marrow failure usually becomes apparent in the second year and was present by age six in all reviewed patients. Neurodevelopmental abnormalities may be evident prenatally or in early infancy; seizures, when present, begin in early childhood. The course is chronic, progressive, and lifelong, without documented spontaneous remission. (karremann2020reveszsyndromerevisited pages 7-8, karremann2020reveszsyndromerevisited pages 1-2)

There is no validated stage system. A practical clinical sequence is: congenital growth/CNS abnormality → infantile retinopathy → early cytopenias/marrow failure → progressive visual and neurologic disability → severe infections, bleeding, pulmonary complications, or transplant-related morbidity. The first 1–2 years constitute a critical window for retinal surveillance and hematologic diagnosis.

## 9. Inheritance and population

RS is autosomal dominant at the molecular level but is most often caused by a **de novo** heterozygous TINF2 variant. Recurrence risk is low but not zero when parents test negative because parental germline mosaicism cannot be excluded. An affected individual would theoretically have a 50% transmission risk, although severe childhood mortality limits observed vertical transmission. Familial TINF2 TBD shows variable expressivity; the penetrance of specific RS alleles has not been quantified. (karremann2020reveszsyndromerevisited pages 7-8, savage2022dyskeratosiscongenitaand pages 5-6, savage2022dyskeratosiscongenitaand pages 8-10)

Telomere-mediated genetic anticipation is recognized across TBDs, but direct multigenerational anticipation data for RS are lacking. No founder allele, population enrichment, consanguinity effect, or carrier frequency has been demonstrated. In the 18-child review there were 11 boys and seven girls; this small difference did not establish a biologically meaningful sex bias. No prevalence or incidence per 100,000 can be calculated reliably. (karremann2020reveszsyndromerevisited pages 7-8, rolles2024inheritedtelomerebiology pages 10-12)

## 10. Diagnostics

### Recommended workflow

1. Recognize the combination of infantile bilateral exudative retinopathy, unexplained cytopenia/hypocellular marrow, intracranial calcification/cerebellar hypoplasia, growth restriction, or DC stigmata.
2. Obtain CBC with differential, reticulocyte count, marrow aspirate/biopsy with morphology and cytogenetics, and infection/immunologic evaluation.
3. Perform complete dilated retinal examination, wide-field imaging and fluorescein angiography where feasible; assess retinal nonperfusion, leakage, exudation, neovascularization, detachment, and glaucoma.
4. Obtain noncontrast head CT for calcification and MRI for cerebellar, callosal, white-matter, hemorrhagic, and cystic abnormalities.
5. Measure leukocyte telomere length by **flow-FISH**, preferably lymphocyte and granulocyte subsets. Lymphocyte length below the age-adjusted **first percentile** is the standard “very short” threshold; seven measured RS patients were below this threshold. (karremann2020reveszsyndromerevisited pages 7-8, rolles2024inheritedtelomerebiology pages 8-9)
6. Sequence **TINF2**, including exon 6, using a comprehensive TBD/inherited-marrow-failure panel. If unrevealing, use WES or WGS with copy-number analysis and consider non-blood DNA if somatic reversion/mosaicism is suspected. (rolles2024inheritedtelomerebiology pages 10-12, savage2022dyskeratosiscongenitaand pages 5-6, savage2022dyskeratosiscongenitaand pages 8-10)
7. Perform mitomycin-C or diepoxybutane chromosome-breakage testing when Fanconi anemia remains possible. CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not first-line RS tests unless another diagnosis is suspected. (rolles2024inheritedtelomerebiology pages 12-14, NCT01659606 chunk 1)

A reported RS child had telomere lengths of **2.47–2.48 kb**, below the first percentile, and TINF2 c.845G>A/p.Arg282His. (karremann2020reveszsyndromerevisited pages 4-7)

### Differential diagnosis

- **Coats plus/CRMCC**, usually CTC1, STN1 or POT1 related: retinal telangiectasia, calcifications, white-matter disease, cysts, GI bleeding, and bone disease; telomeres may be normal.
- **Hoyeraal–Hreidarsson syndrome:** cerebellar hypoplasia, growth restriction, immunodeficiency, microcephaly and severe marrow failure, often DKC1 or biallelic RTEL1 related; exudative retinopathy is less defining.
- **Classic DC/other TBDs:** mucocutaneous triad and marrow failure without the characteristic RS retinal/CNS combination.
- **Fanconi anemia:** congenital anomalies and marrow failure with positive chromosome-breakage testing.
- **Isolated Coats disease/familial exudative vitreoretinopathy:** retinal disease without very short telomeres or systemic marrow failure.
- Congenital infection and metabolic causes of intracranial calcification should be excluded based on context. (rolles2024inheritedtelomerebiology pages 8-9, NCT01659606 chunk 1)

No universally accepted RS-only diagnostic criteria exist; diagnosis is syndromic plus molecular/functional confirmation.

## 11. Outcome and prognosis

In the 18-child review, Kaplan–Meier median survival was **6.5 years** (95% CI 3.6–9.4), and no reported patient survived beyond 12 years. These historical estimates are based on very small, heterogeneous case reports and may not reflect contemporary transplant and ophthalmic care. (karremann2020reveszsyndromerevisited pages 7-8, karremann2020reveszsyndromerevisited pages 1-2)

Major morbidity includes blindness, developmental disability, ataxia, seizures, recurrent infection, bleeding, transfusion dependence, transplant toxicity, and pulmonary failure. Three patients had intracranial hemorrhage. In a 2023 childhood DC natural-history cohort, the RS patient developed cerebral calcifications and retinopathy progressing to blindness and later died from septic shock after dental/gum infection, illustrating combined visual and immune/hematologic morbidity. (karremann2020reveszsyndromerevisited pages 9-11, karremann2020reveszsyndromerevisited pages 7-8)

Poor prognostic markers plausibly include very early marrow failure, severe retinal disease, profound telomere shortening, pre-existing pulmonary/hepatic injury, infection, hemorrhage, and inability to undergo successful transplantation. No validated RS prognostic score or biomarker beyond phenotype, organ status, blood counts, and telomere length exists.

## 12. Treatment

### Hematologic treatment

**Allogeneic hematopoietic-cell transplantation (HCT)** is the only established potentially curative treatment for marrow failure, but it does not correct retinal, neurologic, pulmonary, hepatic, or other native-tissue telomere pathology. Eight of 18 reviewed RS children underwent transplantation; four were alive at last follow-up after a median of 22 months. Two reported late deaths were from pulmonary failure at two and 4.5 years after HCT. (karremann2020reveszsyndromerevisited pages 8-9, karremann2020reveszsyndromerevisited pages 9-11, karremann2020reveszsyndromerevisited pages 1-2)

Reduced-intensity, radiation-avoiding conditioning is preferred because TBD tissues are unusually sensitive to DNA-damaging chemotherapy and radiation. Four RS cases receiving fludarabine/cyclophosphamide/antithymocyte-globulin conditioning had limited acute toxicity, but long-term evidence remains weak. In broader TBD cohorts, 10-year post-HCT survival was about 23%, with progressive pulmonary fibrosis an important late complication. (karremann2020reveszsyndromerevisited pages 9-11, rolles2024inheritedtelomerebiology pages 14-15)

The active-not-recruiting phase-2 **NCT01659606** explicitly includes RS and evaluates an alkylator- and radiation-free regimen of alemtuzumab plus fludarabine, followed by cyclosporine or tacrolimus and mycophenolate prophylaxis; target enrollment is 40. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT01659606. (NCT01659606 chunk 1, NCT01659606 chunk 2)

Suggested NCIT concepts: **Hematopoietic Stem Cell Transplantation**, **Allogeneic Bone Marrow Transplantation**, **Reduced-Intensity Conditioning**, **Fludarabine**, **Alemtuzumab**, **Cyclophosphamide**, and **Antithymocyte Globulin**.

### Ophthalmic treatment

Urgent retinal treatment is warranted before irreversible detachment or glaucoma. Reported approaches include laser photocoagulation of avascular retina, cryotherapy, intravitreal bevacizumab, vitrectomy, and—when a painful blind eye develops—enucleation. Evidence consists of case reports, not comparative trials. (karremann2020reveszsyndromerevisited pages 9-11, karremann2020reveszsyndromerevisited pages 4-7, tomcikova2018whyisit pages 1-2)

One child with mosaic TINF2 p.Pro289Ser had the left eye enucleated for neovascular glaucoma, while photocoagulation of the right ischemic retina preserved reported visual acuity of **0.9 at age seven**. This supports early retinal examination in every young child with unexplained aplastic anemia. (tomcikova2018whyisit pages 1-2)

Suggested NCIT concepts: **Laser Photocoagulation**, **Cryotherapy**, **Bevacizumab**, **Intravitreal Injection**, **Vitrectomy**, and **Enucleation**.

### Pharmacotherapy and supportive care

Transfusions, infection prophylaxis/treatment, dental care, nutritional support, developmental therapies, low-vision services, seizure treatment, and physical/occupational/speech therapy should be individualized. Standard immunosuppressive therapy for acquired aplastic anemia generally has little benefit in constitutional TBD marrow failure. (rolles2024inheritedtelomerebiology pages 10-12, carvalho2022recentadvancesin pages 7-9)

Oral androgens such as danazol or oxymetholone can improve counts in some TBD patients, but there are no RS-specific response data. A 2024 review reported short-term hematologic responses in approximately 50–100% of heterogeneous TBD patients receiving danazol; in one underlying study, 11/12 gained telomere length (mean +386 bp) and 83% had a hematologic response at 24 months. Hepatotoxicity, virilization, lipid changes, and clonal evolution require monitoring. These figures must **not** be interpreted as RS response rates. (rolles2024inheritedtelomerebiology pages 12-14, rolles2024inheritedtelomerebiology pages 14-15)

### Emerging therapy

**NCT06817590**, a phase-1 Boston Children’s Hospital study first posted 10 February 2025, explicitly includes RS. It evaluates oral **deoxycytidine plus deoxythymidine** three times daily for 24 weeks in 36 estimated participants aged 1–70, based on 2023 evidence that thymidine-nucleotide metabolism controls human telomere length (PMID **36959362**). Outcomes include safety, blood counts, telomere length, marrow cellularity, clonal hematopoiesis, and pulmonary function. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT06817590. This is experimental and has no efficacy result yet. (NCT06817590 chunk 1, NCT06817590 chunk 2)

PAPD5 inhibition, engineered telomerase RNA, gene editing, and telomerase gene therapy remain preclinical or early translational TBD approaches. No approved RS gene, RNA, or cell therapy exists. (rolles2024inheritedtelomerebiology pages 14-15)

## 13. Prevention

Primary prevention by lifestyle change is impossible because RS is genetic. Reproductive options after identification of a familial pathogenic variant include genetic counseling, prenatal diagnosis, and preimplantation genetic testing. Parental testing should include discussion of possible germline mosaicism.

Secondary prevention centers on early detection: cascade testing, CBC surveillance, telomere testing where indicated, immediate retinal examination in infants with cytopenia or suspected TBD, and neuroimaging when CNS features are present. Population newborn screening is not available.

Tertiary prevention includes early laser treatment of avascular retina, prompt infection management, meticulous dental care, matched-donor screening, avoidance of affected related donors, reduced-toxicity HCT conditioning, sun protection, smoking avoidance, minimized diagnostic/therapeutic radiation, and surveillance for pulmonary, hepatic, marrow-clonal, mucosal, and malignant complications. General vaccines should follow expert guidance tailored to immune status and transplant timing; there is no RS-specific vaccine. (NCT01659606 chunk 1, savage2022dyskeratosiscongenitaand pages 5-6, carvalho2022recentadvancesin pages 7-9)

## 14. Other species and natural disease

No naturally occurring veterinary syndrome equivalent to human RS was identified in companion animals, livestock, or wildlife. RS has no zoonotic potential and cannot be transmitted between species. TINF2 orthologues are evolutionarily conserved in vertebrates, preserving the central shelterin role, but orthologue identifiers should be retrieved directly from current NCBI Gene/Alliance records before database deposition.

## 15. Model organisms and experimental systems

- **Mouse:** a knock-in model carrying a DC-associated Tinf2 mutation demonstrated telomerase-independent telomere shortening, supporting a direct TIN2 role beyond simply reducing telomerase activity. It models the molecular lesion but has not been shown here to reproduce the complete human RS combination of retinopathy, intracranial calcification, and infantile marrow failure. (nelson2018thecterminalextension pages 30-33)
- **Human patient-derived cells:** lymphoblastoid lines expressing truncating TIN2 demonstrated stable mutant protein and impaired TRF1 interaction. These are useful for shelterin biochemistry but do not reproduce tissue-level RS. (sasa2012threenoveltruncating pages 1-3)
- **Engineered cell systems:** overexpression and CRISPR studies distinguish TIN2S and TIN2L interactions with TRF1/TRF2 and their permissiveness for telomere elongation. (nelson2018thecterminalextension pages 1-3, nelson2018thecterminalextension pages 8-10)
- **DC iPSCs:** patient-derived iPSCs reproduce biochemical telomere defects and loss of self-renewal, making them a platform for therapeutic screening; however, the retrieved study modeled TERT, DKC1, and TCAB1 disease rather than RS-specific TINF2 alleles. (batista2011telomereshorteningand pages 1-3)

No validated RS retinal organoid, cerebral organoid, zebrafish, Drosophila, rat, or naturally occurring animal model was identified.

## Recent developments and expert assessment

The major 2023–2024 advance is not a new RS natural-history cohort but refinement of the broader TBD framework. The July **2024** review by Rolles et al. reaffirmed RS as an early severe pediatric TBD with telomeres “considerably below the 1% percentile,” endorsed lymphocyte flow-FISH followed by germline sequencing, and emphasized reduced-intensity/radiation-avoiding HCT. DOI: [10.1159/000540109](https://doi.org/10.1159/000540109). (rolles2024inheritedtelomerebiology pages 8-9, rolles2024inheritedtelomerebiology pages 14-15)

The 2023 thymidine-metabolism study (PMID **36959362**; DOI: [10.1038/s41588-023-01339-5](https://doi.org/10.1038/s41588-023-01339-5)) supplied the mechanistic basis for the subsequent RS-inclusive dC/dT phase-1 trial. This represents a transition from supportive/transplant care toward attempts to manipulate telomere substrate metabolism, although clinical benefit remains unproven. (NCT06817590 chunk 1, NCT06817590 chunk 2)

The principal expert conclusion is that RS should be managed as a **multisystem developmental and degenerative disorder**, not merely aplastic anemia. HCT can replace hematopoiesis but cannot repair the retina, brain, lung, or liver; successful care therefore requires coordinated hematology/transplantation, ophthalmology, neurology, genetics, pulmonology, hepatology, dentistry, rehabilitation, and psychosocial support. (karremann2020reveszsyndromerevisited pages 9-11, rolles2024inheritedtelomerebiology pages 14-15, NCT04959188 chunk 1)

## Priority knowledge gaps

Reliable prevalence, incidence, penetrance, allele-specific natural history, population frequencies, germline-mosaic recurrence risk, modifier genes, protective factors, quantitative quality of life, retinal cellular mechanism, RS-specific omics, and controlled treatment outcomes are unavailable. Published percentages arise from fewer than 20 historical patients and should be stored with small-sample and ascertainment-bias qualifiers. No 2023–2024 RS-specific cohort, randomized trial, approved targeted therapy, or validated prognostic model was identified. (karremann2020reveszsyndromerevisited pages 7-8, karremann2020reveszsyndromerevisited pages 1-2, rolles2024inheritedtelomerebiology pages 8-9)

References

1. (karremann2020reveszsyndromerevisited pages 8-9): Michael Karremann, Eva Neumaier-Probst, Frank Schlichtenbrede, Fabian Beier, Tim H. Brümmendorf, Friedrich W. Cremer, Peter Bader, and Matthias Dürken. Revesz syndrome revisited. Orphanet Journal of Rare Diseases, Oct 2020. URL: https://doi.org/10.1186/s13023-020-01553-y, doi:10.1186/s13023-020-01553-y. This article has 39 citations and is from a peer-reviewed journal.

2. (karremann2020reveszsyndromerevisited pages 1-2): Michael Karremann, Eva Neumaier-Probst, Frank Schlichtenbrede, Fabian Beier, Tim H. Brümmendorf, Friedrich W. Cremer, Peter Bader, and Matthias Dürken. Revesz syndrome revisited. Orphanet Journal of Rare Diseases, Oct 2020. URL: https://doi.org/10.1186/s13023-020-01553-y, doi:10.1186/s13023-020-01553-y. This article has 39 citations and is from a peer-reviewed journal.

3. (rolles2024inheritedtelomerebiology pages 8-9): Benjamin Rolles, Mareike Tometten, Robert Meyer, Martin Kirschner, Fabian Beier, and Tim H. Brümmendorf. Inherited telomere biology disorders: pathophysiology, clinical presentation, diagnostics, and treatment. Transfusion Medicine and Hemotherapy, 51:292-309, Jul 2024. URL: https://doi.org/10.1159/000540109, doi:10.1159/000540109. This article has 23 citations and is from a peer-reviewed journal.

4. (karremann2020reveszsyndromerevisited pages 7-8): Michael Karremann, Eva Neumaier-Probst, Frank Schlichtenbrede, Fabian Beier, Tim H. Brümmendorf, Friedrich W. Cremer, Peter Bader, and Matthias Dürken. Revesz syndrome revisited. Orphanet Journal of Rare Diseases, Oct 2020. URL: https://doi.org/10.1186/s13023-020-01553-y, doi:10.1186/s13023-020-01553-y. This article has 39 citations and is from a peer-reviewed journal.

5. (OpenTargets Search: Revesz syndrome-TINF2): Open Targets Query (Revesz syndrome-TINF2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (savage2022dyskeratosiscongenitaand pages 8-10): Sharon A. Savage. Dyskeratosis congenita and telomere biology disorders. Hematology. American Society of Hematology. Education Program, 2022 1:637-648, Dec 2022. URL: https://doi.org/10.1182/hematology.2022000394, doi:10.1182/hematology.2022000394. This article has 119 citations.

7. (rolles2024inheritedtelomerebiology pages 2-4): Benjamin Rolles, Mareike Tometten, Robert Meyer, Martin Kirschner, Fabian Beier, and Tim H. Brümmendorf. Inherited telomere biology disorders: pathophysiology, clinical presentation, diagnostics, and treatment. Transfusion Medicine and Hemotherapy, 51:292-309, Jul 2024. URL: https://doi.org/10.1159/000540109, doi:10.1159/000540109. This article has 23 citations and is from a peer-reviewed journal.

8. (sasa2012threenoveltruncating pages 3-4): Ghadir Sasa, Albert Ribes-Zamora, Nya D. Nelson, and Alison A. Bertuch. Three novel truncating tinf2 mutations causing severe dyskeratosis congenita in early childhood. Clinical Genetics, 81:470-478, May 2012. URL: https://doi.org/10.1111/j.1399-0004.2011.01658.x, doi:10.1111/j.1399-0004.2011.01658.x. This article has 118 citations and is from a peer-reviewed journal.

9. (tomcikova2018whyisit pages 1-2): D. Tomcikova, A. Gerinec, B. Busanyova, M. Gresikova, S. Biskup, and K. Hortnagel. Why is it necessary to examine retina when the patient suffers from aplastic anemia? Bratislavske lekarske listy, 119 5:275-277, Jan 2018. URL: https://doi.org/10.4149/bll\_2018\_051, doi:10.4149/bll\_2018\_051. This article has 7 citations.

10. (karremann2020reveszsyndromerevisited pages 4-7): Michael Karremann, Eva Neumaier-Probst, Frank Schlichtenbrede, Fabian Beier, Tim H. Brümmendorf, Friedrich W. Cremer, Peter Bader, and Matthias Dürken. Revesz syndrome revisited. Orphanet Journal of Rare Diseases, Oct 2020. URL: https://doi.org/10.1186/s13023-020-01553-y, doi:10.1186/s13023-020-01553-y. This article has 39 citations and is from a peer-reviewed journal.

11. (karremann2020reveszsyndromerevisited pages 9-11): Michael Karremann, Eva Neumaier-Probst, Frank Schlichtenbrede, Fabian Beier, Tim H. Brümmendorf, Friedrich W. Cremer, Peter Bader, and Matthias Dürken. Revesz syndrome revisited. Orphanet Journal of Rare Diseases, Oct 2020. URL: https://doi.org/10.1186/s13023-020-01553-y, doi:10.1186/s13023-020-01553-y. This article has 39 citations and is from a peer-reviewed journal.

12. (nelson2018thecterminalextension pages 1-3): Nya D. Nelson, Lois M. Dodson, Laura Escudero, Ann T. Sukumar, Christopher L. Williams, Ivana Mihalek, Alessandro Baldan, Duncan M. Baird, and Alison A. Bertuch. The c-terminal extension unique to the long isoform of the shelterin component tin2 enhances its interaction with trf2 in a phosphorylation- and dyskeratosis congenita cluster-dependent fashion. Jun 2018. URL: https://doi.org/10.1128/mcb.00025-18, doi:10.1128/mcb.00025-18. This article has 34 citations and is from a domain leading peer-reviewed journal.

13. (sasa2012threenoveltruncating pages 1-3): Ghadir Sasa, Albert Ribes-Zamora, Nya D. Nelson, and Alison A. Bertuch. Three novel truncating tinf2 mutations causing severe dyskeratosis congenita in early childhood. Clinical Genetics, 81:470-478, May 2012. URL: https://doi.org/10.1111/j.1399-0004.2011.01658.x, doi:10.1111/j.1399-0004.2011.01658.x. This article has 118 citations and is from a peer-reviewed journal.

14. (roake2021tissuespecifictelomereshortening pages 1-2): Caitlin M. Roake, Marisa Juntilla, Rajni Agarwal-Hashmi, Steven Artandi, and Christin S. Kuo. Tissue-specific telomere shortening and degenerative changes in a patient with tinf2 mutation and dyskeratosis congenita. Human Pathology: Case Reports, 25:200517, Sep 2021. URL: https://doi.org/10.1016/j.ehpc.2021.200517, doi:10.1016/j.ehpc.2021.200517. This article has 6 citations.

15. (rolles2024inheritedtelomerebiology pages 12-14): Benjamin Rolles, Mareike Tometten, Robert Meyer, Martin Kirschner, Fabian Beier, and Tim H. Brümmendorf. Inherited telomere biology disorders: pathophysiology, clinical presentation, diagnostics, and treatment. Transfusion Medicine and Hemotherapy, 51:292-309, Jul 2024. URL: https://doi.org/10.1159/000540109, doi:10.1159/000540109. This article has 23 citations and is from a peer-reviewed journal.

16. (rolles2024inheritedtelomerebiology pages 10-12): Benjamin Rolles, Mareike Tometten, Robert Meyer, Martin Kirschner, Fabian Beier, and Tim H. Brümmendorf. Inherited telomere biology disorders: pathophysiology, clinical presentation, diagnostics, and treatment. Transfusion Medicine and Hemotherapy, 51:292-309, Jul 2024. URL: https://doi.org/10.1159/000540109, doi:10.1159/000540109. This article has 23 citations and is from a peer-reviewed journal.

17. (NCT06817590 chunk 1): Suneet Agarwal. Nucleoside Therapy in Patients With Telomere Biology Disorders. Suneet Agarwal. 2025. ClinicalTrials.gov Identifier: NCT06817590

18. (NCT01659606 chunk 1): Suneet Agarwal. Radiation- and Alkylator-free Bone Marrow Transplantation Regimen for Patients With Dyskeratosis Congenita. Boston Children's Hospital. 2012. ClinicalTrials.gov Identifier: NCT01659606

19. (rolles2024inheritedtelomerebiology pages 14-15): Benjamin Rolles, Mareike Tometten, Robert Meyer, Martin Kirschner, Fabian Beier, and Tim H. Brümmendorf. Inherited telomere biology disorders: pathophysiology, clinical presentation, diagnostics, and treatment. Transfusion Medicine and Hemotherapy, 51:292-309, Jul 2024. URL: https://doi.org/10.1159/000540109, doi:10.1159/000540109. This article has 23 citations and is from a peer-reviewed journal.

20. (savage2022dyskeratosiscongenitaand pages 5-6): Sharon A. Savage. Dyskeratosis congenita and telomere biology disorders. Hematology. American Society of Hematology. Education Program, 2022 1:637-648, Dec 2022. URL: https://doi.org/10.1182/hematology.2022000394, doi:10.1182/hematology.2022000394. This article has 119 citations.

21. (NCT04959188 chunk 1):  Needs Assessment for Individuals and Families Affected by Dyskeratosis Congenita (DC) and Related Telomere Biology Disorders (TBD). National Cancer Institute (NCI). 2021. ClinicalTrials.gov Identifier: NCT04959188

22. (carvalho2022recentadvancesin pages 7-9): Vinicius S Carvalho, Willian R Gomes, and Rodrigo T Calado. Recent advances in understanding telomere diseases. Faculty Reviews, Oct 2022. URL: https://doi.org/10.12703/r/11-31, doi:10.12703/r/11-31. This article has 24 citations.

23. (NCT01659606 chunk 2): Suneet Agarwal. Radiation- and Alkylator-free Bone Marrow Transplantation Regimen for Patients With Dyskeratosis Congenita. Boston Children's Hospital. 2012. ClinicalTrials.gov Identifier: NCT01659606

24. (NCT06817590 chunk 2): Suneet Agarwal. Nucleoside Therapy in Patients With Telomere Biology Disorders. Suneet Agarwal. 2025. ClinicalTrials.gov Identifier: NCT06817590

25. (batista2011telomereshorteningand pages 1-3): Luis F. Z. Batista, Matthew F. Pech, Franklin L. Zhong, Ha Nam Nguyen, Kathleen T. Xie, Arthur J. Zaug, Sharon M. Crary, Jinkuk Choi, Vittorio Sebastiano, Athena Cherry, Neelam Giri, Marius Wernig, Blanche P. Alter, Thomas R. Cech, Sharon A. Savage, Renee A. Reijo Pera, and Steven E. Artandi. Telomere shortening and loss of self-renewal in dyskeratosis congenita ips cells. Nature, 474:399-402, May 2011. URL: https://doi.org/10.1038/nature10084, doi:10.1038/nature10084. This article has 316 citations and is from a highest quality peer-reviewed journal.

26. (nelson2018thecterminalextension pages 30-33): Nya D. Nelson, Lois M. Dodson, Laura Escudero, Ann T. Sukumar, Christopher L. Williams, Ivana Mihalek, Alessandro Baldan, Duncan M. Baird, and Alison A. Bertuch. The c-terminal extension unique to the long isoform of the shelterin component tin2 enhances its interaction with trf2 in a phosphorylation- and dyskeratosis congenita cluster-dependent fashion. Jun 2018. URL: https://doi.org/10.1128/mcb.00025-18, doi:10.1128/mcb.00025-18. This article has 34 citations and is from a domain leading peer-reviewed journal.

27. (nelson2018thecterminalextension pages 8-10): Nya D. Nelson, Lois M. Dodson, Laura Escudero, Ann T. Sukumar, Christopher L. Williams, Ivana Mihalek, Alessandro Baldan, Duncan M. Baird, and Alison A. Bertuch. The c-terminal extension unique to the long isoform of the shelterin component tin2 enhances its interaction with trf2 in a phosphorylation- and dyskeratosis congenita cluster-dependent fashion. Jun 2018. URL: https://doi.org/10.1128/mcb.00025-18, doi:10.1128/mcb.00025-18. This article has 34 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Revesz_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009990` (5 mentions) - the report calls it "if available"; MONDO calls it **Revesz syndrome**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0000784` (GO_0000784) (2 mentions) - replaced by `GO:0000781`