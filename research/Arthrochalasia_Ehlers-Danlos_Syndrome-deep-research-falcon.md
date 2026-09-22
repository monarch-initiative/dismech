---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-15T22:24:24.404507'
end_time: '2026-09-15T22:36:20.572315'
duration_seconds: 716.17
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Arthrochalasia Ehlers-Danlos Syndrome
  mondo_id: MONDO:0007525
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
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 15
  verified: 10
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0007525
    reported_labels:
    - if available
    ontology_label: Ehlers-Danlos syndrome, arthrochalasia type
  unresolvable_prefixes:
  - Gene
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Arthrochalasia_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Arthrochalasia Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0007525 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arthrochalasia Ehlers-Danlos Syndrome** covering all of the
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
- **Disease Name:** Arthrochalasia Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0007525 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arthrochalasia Ehlers-Danlos Syndrome** covering all of the
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


# Arthrochalasia Ehlers–Danlos Syndrome: Disease Characteristics Report

**Scope and evidence note.** Arthrochalasia Ehlers–Danlos syndrome (aEDS) is so rare that most evidence consists of molecularly confirmed case reports, small series, expert consensus, and one 2022 systematic review. Approximately 42 patients had been published worldwide by 2022; consequently, frequencies should not be interpreted as stable population estimates. Claims based on EDS generally rather than aEDS specifically are explicitly labeled as indirect evidence. No substantive aEDS-specific publications from 2023–2024 were identified; the principal recent development is a 2024 EDS-wide review showing that orthopedic surgical evidence remains sparse and inconsistent. (martinmartin2022ehlers–danlossyndrometype pages 7-8, martinmartin2022ehlers–danlossyndrometype pages 1-2, schubart2024outcomesoforthopaedic pages 1-2)

The following table provides a compact, ontology-oriented summary before the detailed report.

| Domain | Curated finding | Evidence level/source year | Ontology/code suggestions |
|---|---|---|---|
| Identity and aliases | Arthrochalasia Ehlers–Danlos syndrome (aEDS); formerly EDS type VIIA for **COL1A1**-related disease and type VIIB for **COL1A2**-related disease; Mendelian, autosomal-dominant heritable connective-tissue disorder (malfait2017the2017international pages 12-13, wenstrup2002prevalenceofaortic pages 1-2) | International expert classification, 2017 | **MONDO:0007525**; labels: arthrochalasia EDS, EDS VIIA, EDS VIIB |
| Causal gene: COL1A1 | Heterozygous pathogenic variants affecting exon 6 of **COL1A1**, encoding collagen type I α1 chain, cause aEDS; COL1A1-associated disease may be more severe because approximately three quarters of collagen-I molecules can contain an abnormal α1 chain (OpenTargets Search: arthrochalasia Ehlers-Danlos syndrome-COL1A1,COL1A2, martinmartin2022ehlers–danlossyndrometype pages 7-8, giunta2008thearthrochalasiatype pages 1-2) | Human genetic, biochemical, and ultrastructural evidence; 2008–2022 | **HGNC:2197**; **NCBI Gene:1277**; collagen α1(I) chain |
| Causal gene: COL1A2 | Heterozygous pathogenic variants affecting exon 6 of **COL1A2**, encoding collagen type I α2 chain, cause aEDS; approximately half of collagen-I molecules may contain an abnormal α2 chain (OpenTargets Search: arthrochalasia Ehlers-Danlos syndrome-COL1A1,COL1A2, giunta2008thearthrochalasiatype pages 1-2) | Human genetic, biochemical, and ultrastructural evidence; 2008–2024 | **HGNC:2198**; **NCBI Gene:1278**; collagen α2(I) chain |
| Variant spectrum | Lesions are usually splice-donor, splice-acceptor, or genomic variants producing complete or partial exon-6 loss. A demonstrated **COL1A1 IVS5-2A>T** variant activated a cryptic splice site and deleted the first 15 nucleotides of exon 6; variants are germline and may be inherited or de novo (malfait2017the2017international pages 12-13, giunta2008thearthrochalasiatype pages 2-3, malfait2020theehlers–danlossyndromes pages 6-7) | Molecularly confirmed human cases; 2008–2020 | Sequence Ontology labels: splice-acceptor variant, splice-donor variant, exon loss, in-frame deletion |
| Molecular mechanism | Exon-6 loss removes the type-I-procollagen N-proteinase cleavage site and may remove the N-telopeptide cross-linking lysine and start of the Gly-X-Y triple-helical region. Failed cleavage produces collagen retaining its N-propeptide—**pN-collagen** (giunta2008thearthrochalasiatype pages 2-3, malfait2020theehlers–danlossyndromes pages 6-7, brady2017theehlers–danlossyndromes pages 8-9) | Direct patient-fibroblast biochemical evidence and expert synthesis; 2008–2020 | GO labels: collagen biosynthetic process, collagen fibril organization, extracellular-matrix organization, protein processing |
| Fibrillogenesis | Retained pNα1(I) or pNα2(I) chains disturb collagen fibrillogenesis. Skin electron microscopy shows small, loosely or randomly organized fibrils with irregular or ragged contours; dominant-negative interference is strongly inferred but not directly proven in the cited experiment (giunta2008thearthrochalasiatype pages 2-3, giunta2008thearthrochalasiatype pages 1-2) | Human in-vitro biochemical and skin-biopsy TEM evidence; 2008 | **CL:0000057** fibroblast; labels: dermal fibroblast, collagen fibril, dermis, collagen-containing extracellular matrix |
| Hallmark phenotype | Congenital bilateral hip dislocation is the principal hallmark, accompanied by severe generalized joint hypermobility and recurrent dislocations or subluxations. One molecularly proven but unpublished patient reportedly had unilateral hip dislocation (malfait2017the2017international pages 12-13) | International diagnostic consensus, 2017 | **HP:0001382** joint hypermobility; **HP:0001374** congenital hip dislocation; labels: recurrent joint dislocation, joint subluxation |
| Minor phenotypes | Skin hyperextensibility, hypotonia, kyphoscoliosis, mild osteopenia, tissue fragility, atrophic scars, easy bruising or hematomas, redundant skin, clubfoot, and congenital knee dislocation occur variably (malfait2017the2017international pages 12-13, martinmartin2022ehlers–danlossyndrometype pages 5-7, giunta2008thearthrochalasiatype pages 2-3) | Consensus criteria and human cases; 2008–2022 | **HP:0000974** hyperextensible skin; **HP:0001252** hypotonia; **HP:0002751** kyphoscoliosis; **HP:0000938** osteopenia; **HP:0001075** atrophic scars; **HP:0000978** bruising susceptibility |
| Epidemiology | Population prevalence and incidence are unknown. The 2022 systematic review identified approximately **42 published patients worldwide**, with substantial uncertainty from underdiagnosis and publication bias (martinmartin2022ehlers–danlossyndrometype pages 7-8, martinmartin2022ehlers–danlossyndrometype pages 1-2) | PRISMA systematic review, 2022 | **MONDO:0007525**; rare disease; do not apply aggregate EDS prevalence estimates to aEDS |
| Vascular and cardiac risk | A vascular complication was reported in **1/17 aEDS patients (6%)** in a systematic review. Progressive mitral, aortic, and tricuspid regurgitation has also been reported, but estimates rest on very small samples (dhondt2018vascularphenotypesin pages 3-4, martinmartin2022ehlers–danlossyndrometype pages 4-5) | Systematic review and isolated human case; 2018–2022 | Labels: vascular complication, mitral regurgitation, aortic regurgitation, tricuspid regurgitation |
| Diagnosis | Suggestive findings are congenital bilateral hip dislocation plus either skin hyperextensibility or severe generalized joint hypermobility with multiple dislocations or subluxations, together with at least two minor criteria. Definitive diagnosis requires molecular confirmation (malfait2017the2017international pages 12-13) | International expert classification, 2017 | Sequence **COL1A1** and **COL1A2**; connective-tissue multigene panel; deletion/duplication analysis if sequencing is negative |
| Ancillary diagnostics | Cultured skin-fibroblast collagen analysis can demonstrate abnormal pN-collagen processing. Skin-biopsy transmission electron microscopy may show supportive fibril abnormalities but does not replace molecular confirmation (malfait2017the2017international pages 12-13, giunta2008thearthrochalasiatype pages 2-3, giunta2008thearthrochalasiatype pages 1-2) | Human biochemical/TEM evidence and consensus; 2008–2017 | NCIT labels: skin biopsy, transmission electron microscopy, fibroblast culture, protein electrophoresis |
| Treatment and trials gap | No curative or disease-modifying therapy exists. Care is individualized and multidisciplinary: cautious physiotherapy and strengthening, joint protection, orthoses or mobility aids, pain management, wound precautions, and selective orthopedic intervention. No aEDS-specific treatment-response rates or interventional trials were identified (martinmartin2022ehlers–danlossyndrometype pages 1-2, martinmartin2022ehlers–danlossyndrometype pages 5-7, schubart2024outcomesoforthopaedic pages 1-2) | Systematic and scoping reviews; 2022–2024 | NCIT labels: physical therapy, occupational therapy, orthotic device, pain management, orthopedic surgery, supportive care, genetic counseling |
| Surgery evidence | EDS-wide 2024 evidence comprised 71 primary orthopedic studies—38 case reports, 14 case series, and 19 retrospective cohorts—with no randomized trials and inconsistent outcomes. Findings were not aEDS-specific (schubart2024outcomesoforthopaedic pages 15-16, schubart2024outcomesoforthopaedic pages 1-2) | Scoping review, October 2024; indirect evidence | NCIT labels: orthopedic surgery, preoperative assessment, postoperative care; annotate as EDS-wide indirect evidence |
| Animal and model gap | No validated naturally occurring animal disease or exact **COL1A1/COL1A2 exon-6 aEDS** model was identified. A combined osteogenesis-imperfecta/EDS mouse is mechanistically adjacent but does not reproduce the defining exon-6 lesion and should not be curated as an aEDS-equivalent model | Targeted literature search through 2024; negative or adjacent evidence | **NCBI Taxon:10090** for the adjacent mouse model only; model status: not disease-equivalent |


*Table: Compact extraction table summarizing the identity, genetics, mechanism, phenotype, epidemiology, diagnosis, management, vascular evidence, and research gaps for arthrochalasia Ehlers–Danlos syndrome.*

## 1. Disease information

### Definition and classification

Arthrochalasia EDS is an **autosomal-dominant Mendelian connective-tissue disorder** caused by abnormal processing of type I procollagen. Its defining manifestations are congenital—usually bilateral—hip dislocation, severe generalized joint hypermobility, recurrent joint dislocations or subluxations, and hyperextensible or fragile skin. It is one of the 13 subtypes recognized by the 2017 International EDS Classification. (malfait2017the2017international pages 12-13, islam2021ehlersdanlossyndromeimmunologic pages 31-33)

A useful exact abstract statement from the 2022 systematic review is: **“Ehlers–Danlos syndrome type arthrochalasia (aEDS) is a rare genetic disease characterized by severe generalized joint hypermobility, bilateral congenital hip dislocation, skin hyperextensibility, muscle hypotonia, and mild dysmorphic features.”** The same abstract states: **“Only about 42 cases have been published worldwide.”** The article was published 7 February 2022; DOI URL: https://doi.org/10.3390/ijerph19031870. (martinmartin2022ehlers–danlossyndrometype pages 7-8, martinmartin2022ehlers–danlossyndrometype pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0007525, *Ehlers-Danlos syndrome, arthrochalasia type*.
- **OMIM:** commonly divided historically into **EDS type VIIA** (COL1A1-related; OMIM phenotype 130060) and **EDS type VIIB** (COL1A2-related; OMIM phenotype 130060 is often used for the arthrochalasia phenotype in aggregated resources; database implementations should be checked for version-specific mapping).
- **Orphanet:** *Arthrochalasia Ehlers–Danlos syndrome*; ORPHA mappings should be version-validated before ingestion because legacy VIIA/VIIB records may be handled differently.
- **ICD-10:** no dedicated aEDS code; generally coded under **Q79.6, Ehlers–Danlos syndrome**.
- **ICD-11:** under the Ehlers–Danlos syndrome/heritable connective-tissue disorder hierarchy; no reliably retrieved subtype-specific code should be asserted without checking the current ICD-11 release.
- **MeSH:** *Ehlers-Danlos Syndrome*; no separate aEDS MeSH descriptor was established in the retrieved evidence.
- **Synonyms:** arthrochalasia EDS; EDS arthrochalasia type; Ehlers–Danlos syndrome type VIIA; EDS VIIA; Ehlers–Danlos syndrome type VIIB; EDS VIIB; arthrochalasis multiplex congenita. The VIIA/VIIB distinction respectively denotes COL1A1- and COL1A2-related disease. (malfait2017the2017international pages 12-13, wenstrup2002prevalenceofaortic pages 1-2)

This report is built from **aggregated disease-level resources and published human cases**, not individual EHR records. Open Targets independently associates MONDO:0007525 with COL1A1 and COL1A2 and links supporting human literature including PMIDs 18409203, 9295084, 1867198, 8071956, and 19594296. (OpenTargets Search: arthrochalasia Ehlers-Danlos syndrome-COL1A1,COL1A2)

## 2. Etiology

### Causal factors and genetic risk

The primary cause is a **heterozygous germline pathogenic variant in COL1A1 or COL1A2** that produces complete or partial loss of exon 6 from the mature transcript. Exon 6 encodes functionally critical portions of the type I procollagen N-terminal processing region. Both inherited and de novo cases occur; one reviewed case had a de novo COL1A1 exon-skipping variant. (malfait2017the2017international pages 12-13, martinmartin2022ehlers–danlossyndrometype pages 7-8, malfait2020theehlers–danlossyndromes pages 6-7)

Relevant gene annotations are:

- **COL1A1** — collagen type I α1 chain; HGNC:2197; NCBI Gene 1277; chromosome 17q21.33.
- **COL1A2** — collagen type I α2 chain; HGNC:2198; NCBI Gene 1278; chromosome 7q21.3. (OpenTargets Search: arthrochalasia Ehlers-Danlos syndrome-COL1A1,COL1A2, martinmartin2022ehlers–danlossyndrometype pages 2-4)

Because the disorder is monogenic and highly penetrant clinically in reported families, the principal risk factor is carrying the causal allele or having an affected parent. Family history may be absent because of a de novo event. No validated susceptibility loci, common-variant polygenic risk score, or modifier gene has been established.

### Environmental, lifestyle, infectious, and protective factors

No environmental toxin, infection, diet, smoking exposure, occupation, sex, or lifestyle factor is known to cause aEDS. Mechanical stress does not initiate the disorder but can expose the genetically weakened tissue phenotype by precipitating dislocation, soft-tissue injury, bruising, and pain. This is a **gene–mechanical-environment interaction at the level of manifestations**, not a demonstrated interaction affecting mutation penetrance.

No protective allele or environmental exposure has been established. Joint protection, appropriately dosed strengthening, avoidance of high-impact/contact activity, and prevention of unnecessary tissue trauma are complication-reduction strategies, not protection against inheriting or developing aEDS.

## 3. Phenotypes

### Core and minor manifestations

The 2017 criteria define three major features: (1) congenital bilateral hip dislocation, (2) severe generalized joint hypermobility with multiple dislocations or subluxations, and (3) skin hyperextensibility. Minor criteria are muscular hypotonia, kyphoscoliosis, radiologically mild osteopenia, tissue fragility including atrophic scars, and easy bruising. Foot deformities and congenital knee dislocation are also reported. (malfait2017the2017international pages 12-13, yonko2021orthopedicconsiderationsand pages 2-3, martinmartin2022ehlers–danlossyndrometype pages 5-7, giunta2008thearthrochalasiatype pages 2-3)

| Phenotype | Type, onset, course, and frequency | Suggested HPO annotation |
|---|---|---|
| Congenital hip dislocation | Objective musculoskeletal sign; neonatal. Historically bilateral in all published patients used to formulate criteria, although one molecularly proven unpublished patient reportedly had unilateral involvement. Persistent orthopedic consequences are possible. | Congenital hip dislocation, **HP:0001374**; bilateral congenital hip dislocation label |
| Generalized joint hypermobility | Physical sign; present at birth, usually severe. Hypotonia and hypermobility may become less marked with age but instability can remain lifelong. | Joint hypermobility, **HP:0001382**; generalized joint hypermobility |
| Recurrent dislocation/subluxation | Sign/symptom; childhood onward; episodic and mechanically provoked, with variable sites and severity. | Recurrent joint dislocation; joint subluxation |
| Skin hyperextensibility/redundancy | Physical manifestation; congenital or early childhood; variable. | Hyperextensible skin, **HP:0000974**; redundant skin |
| Tissue/skin fragility and atrophic scars | Physical manifestation; apparent after trauma or procedures; variable and cumulative. | Atrophic scars, **HP:0001075**; skin fragility |
| Easy bruising/hematomas | Physical sign; recurrent and trauma-associated. | Bruising susceptibility, **HP:0000978** |
| Muscular hypotonia | Neonatal sign, often severe; reported to lessen with age. Motor development can be delayed through weakness and instability, while intellectual development is generally normal. | Hypotonia, **HP:0001252** |
| Kyphosis/kyphoscoliosis | Musculoskeletal sign; congenital or developing during growth; variable. | Kyphoscoliosis, **HP:0002751** |
| Mild osteopenia | Radiographic laboratory/imaging abnormality; variable. Available reports do not establish a high fracture rate. | Osteopenia, **HP:0000938** |
| Clubfoot/foot deformity | Congenital structural sign; variable. | Talipes equinovarus/clubfoot; pes planus where applicable |
| Dysmorphism | Mild and variable; reported features include large fontanelle, micrognathia, hypertelorism, and epicanthal folds. | Large fontanelle; micrognathia; hypertelorism; epicanthus |

The disease’s extreme rarity precludes reliable percentage estimates for most manifestations. The major exception is the historical observation that bilateral congenital hip dislocation was present in all published patients informing the 2017 criteria. Reports of very low fracture incidence argue against automatically equating mild osteopenia in aEDS with the fracture burden of osteogenesis imperfecta. (malfait2017the2017international pages 12-13, martinmartin2022ehlers–danlossyndrometype pages 7-8, martinmartin2022ehlers–danlossyndrometype pages 5-7)

### Quality of life

No validated aEDS-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life cohort was identified. Likely burdens—supported clinically but not quantified specifically for aEDS—include impaired mobility, need for orthoses or assistive devices, recurrent injuries, chronic pain, limitations in self-care and employment, and procedural anxiety. The 2022 review states that treatment focuses on improving quality of life, but does not report response rates or standardized scores. (martinmartin2022ehlers–danlossyndrometype pages 1-2)

## 4. Genetic and molecular information

### Pathogenic variant class and consequences

Causal variants are usually splice-donor or splice-acceptor changes, intragenic deletions, or other variants that cause **in-frame complete or partial exon-6 skipping**. An experimentally characterized example was **COL1A1 IVS5-2A>T**—legacy nomenclature—which activated a cryptic splice site and removed the first 15 nucleotides of exon 6. This deleted five amino acids including the procollagen N-proteinase cleavage site. Modern HGVS nomenclature should be generated against the transcript used by the testing laboratory rather than inferred from this legacy description. (giunta2008thearthrochalasiatype pages 2-3)

These are **germline heterozygous variants**. Somatic mosaic disease is not an established mechanism. Pathogenicity should be assigned under ACMG/AMP criteria using segregation/de novo evidence, RNA evidence demonstrating exon loss, collagen biochemical evidence, absence or extreme rarity in population databases, and phenotype specificity. Exact allele frequencies were unavailable in the retrieved papers, but fully penetrant causal alleles for a disorder this rare are expected to be absent or exceptionally rare in gnomAD; this expectation is not a substitute for variant-level database checking.

The functional mechanism is best described as **structural loss with dominant interference** rather than simple haploinsufficiency. Mutant chains enter heterotrimeric type I collagen molecules: approximately three quarters of molecules may be affected for an abnormal α1(I) chain and approximately half for an abnormal α2(I) chain. That provides a plausible explanation for reports that COL1A1-related disease can be more severe, although robust genotype–phenotype statistics are unavailable. Dominant-negative interference is strongly inferred from chain incorporation and abnormal fibrils, but was not directly tested as a separate experimental endpoint in the cited ultrastructural study. (martinmartin2022ehlers–danlossyndrometype pages 7-8, giunta2008thearthrochalasiatype pages 1-2)

No reproducible modifier genes, epigenetic signature, pathogenic aneuploidy, translocation, repeat expansion, mitochondrial lesion, or large chromosomal syndrome is established for aEDS. Copy-number variants restricted to the relevant exon or splice architecture remain plausible and justify deletion/duplication analysis after negative sequencing.

## 5. Environmental information

There is no evidence for causal pollutants, radiation, occupational agents, toxins, dietary deficiencies, alcohol, smoking, or infectious agents. Therefore CTD/toxicogenomic and pathogen annotations should be **not applicable/unsupported**. High-impact activity, forceful manipulation, poor joint positioning, and surgery can aggravate manifestations in genetically fragile tissues; they should be represented as complication triggers, not disease causes. A 2024 chiropractic case illustrates that forceful manipulation can worsen pain and inflammation in EDS, but the patient was not molecularly established to have aEDS, so this is indirect evidence only. (lucente2024chiropractictreatmentof pages 1-2)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A heterozygous germline COL1A1 or COL1A2 splice/deletion lesion leads to partial or complete skipping of exon 6.** (Demonstrated in human cases.) (giunta2008thearthrochalasiatype pages 2-3, malfait2020theehlers–danlossyndromes pages 6-7)
2. **Exon-6 loss leads to deletion of the N-proteinase cleavage site** and may also remove the N-telopeptide cross-linking lysine and first Gly-X-Y helical triplet. (Demonstrated by sequence/protein analysis.) (malfait2020theehlers–danlossyndromes pages 6-7, brady2017theehlers–danlossyndromes pages 8-9)
3. **Loss of the cleavage site results in failure to remove the type I procollagen N-propeptide**, producing pNα1(I)- or pNα2(I)-containing collagen. (Demonstrated by fibroblast collagen electrophoresis.) (giunta2008thearthrochalasiatype pages 2-3, giunta2008thearthrochalasiatype pages 1-2)
4. **Incorporation of uncleaved mutant chains leads to disturbed extracellular collagen-I fibrillogenesis.** Dominant interference is strongly inferred from the proportion of affected heterotrimers and fibril abnormalities rather than proven in an isolated perturbation experiment. (giunta2008thearthrochalasiatype pages 1-2)
5. **Disturbed fibrillogenesis results in smaller, loosely/randomly organized collagen fibrils with irregular or ragged contours** in skin dermis. (Demonstrated by transmission electron microscopy.) (giunta2008thearthrochalasiatype pages 2-3, giunta2008thearthrochalasiatype pages 1-2)
6. **Abnormal collagen architecture leads to reduced tensile and stabilizing competence of ligaments, joint capsules, skin, tendon, and bone connective tissue.** (Mechanistically inferred from tissue function and concordant human phenotype.)
7. **Ligament/joint-capsule weakness leads to congenital hip dislocation, severe generalized hypermobility, recurrent dislocations, and deformity;** **skin/dermal weakness leads to hyperextensibility, bruising, fragility, and atrophic scars;** **musculoskeletal matrix weakness leads to hypotonia-associated motor impairment, kyphoscoliosis, and mild osteopenia.** (Human clinical association; intermediate biomechanics partly inferred.) (malfait2017the2017international pages 12-13, martinmartin2022ehlers–danlossyndrometype pages 5-7, giunta2008thearthrochalasiatype pages 2-3)

### Cellular and biochemical detail

The best direct cellular evidence comes from **cultured dermal fibroblasts**. Patient fibroblasts synthesize abnormal longer α(I) chains retaining their N-propeptide, demonstrable by SDS-PAGE and collagen-fraction analyses. Historical reports of only 10–40% normal “converting proteinase” activity were subsequently reinterpreted after mutant pNα2(I) chains were identified: the primary lesion is substrate structure/processing, not necessarily reduced enzyme production. (giunta2008thearthrochalasiatype pages 2-3, brady2017theehlers–danlossyndromes pages 8-9)

No primary Wnt, MAPK, mTOR, PI3K–AKT, immune, autophagy, apoptosis, mitochondrial, or metabolic pathway defect is established. ER stress is a recognized mechanism in some structural extracellular-matrix diseases, but has not been demonstrated as aEDS-specific pathology and should not be curated as established. Likewise, no aEDS-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omics signature was identified. (lamande2020geneticdisordersof pages 1-2)

Suggested ontology annotations include **GO: extracellular matrix organization; collagen fibril organization; collagen biosynthetic process; protein processing; extracellular structure organization**. Relevant cellular components are collagen-containing extracellular matrix and collagen trimer. Suggested Cell Ontology labels are **fibroblast (CL:0000057), dermal fibroblast, osteoblast, tenocyte, and ligament fibroblast**; only dermal fibroblasts were directly studied, whereas the latter cell types are anatomically plausible but not directly profiled.

## 7. Anatomical structures affected

- **Primary organ/system level:** musculoskeletal system—hips, knees, shoulders and other synovial joints; axial skeleton; feet; bone. Integumentary system—skin and scars.
- **Tissue level:** ligament, joint capsule, tendon, dermis, bone extracellular matrix, fascia and other collagen-I-rich connective tissues.
- **Cell level:** fibroblasts are directly demonstrated; osteoblasts, tenocytes and ligament/joint-capsule fibroblasts are inferred relevant collagen producers.
- **Subcellular level:** COL1A1/COL1A2 transcription and splicing occur in the nucleus; procollagen synthesis and assembly occur in rough ER/Golgi; extracellular N-propeptide processing and fibrillogenesis occur in the extracellular space. Only the extracellular processing/fibril defect and fibroblast collagen products are directly demonstrated in aEDS.
- **Secondary cardiovascular involvement:** rare vascular complications and isolated valvular regurgitation have been reported, but aEDS is not classified as vascular EDS. (dhondt2018vascularphenotypesin pages 3-4, martinmartin2022ehlers–danlossyndrometype pages 4-5)

Suggested UBERON labels are hip joint, knee joint, synovial joint, skin of body, dermis, tendon, ligament, bone tissue and extracellular matrix. Hip involvement is usually bilateral; other dislocations may be bilateral, unilateral, or asymmetric.

## 8. Temporal development

Onset is **prenatal/congenital**. Breech presentation, polyhydramnios, premature rupture of membranes, reduced fetal movement, prematurity, and congenital joint dislocations have been reported. Neonates may have severe hypotonia, generalized hypermobility, large fontanelles and mild dysmorphism. (martinmartin2022ehlers–danlossyndrometype pages 7-8)

The condition is chronic and lifelong, without recognized remission. Hypotonia and apparent hypermobility may lessen with age, but orthopedic instability, recurrent injury, spinal deformity, pain, and scar burden may persist or accumulate. Mental development was normal in reported patients. Published observations span prenatal life through adulthood, but there is no validated stage system or reliable progression rate. (martinmartin2022ehlers–danlossyndrometype pages 7-8, martinmartin2022ehlers–danlossyndrometype pages 4-5)

Critical intervention periods are:

1. **Prenatal/perinatal:** obstetric monitoring because of malpresentation, membrane rupture and prematurity.
2. **Neonatal/infancy:** early recognition and careful management of hip/knee dislocation, hypotonia and clubfoot.
3. **Growth:** prevention and monitoring of scoliosis, recurrent instability and deconditioning.
4. **Before surgery or pregnancy:** individualized tissue-fragility, bleeding, wound-healing, positioning and anesthetic planning. (martinmartin2022ehlers–danlossyndrometype pages 7-8, martinmartin2022ehlers–danlossyndrometype pages 4-5)

## 9. Inheritance and population

Inheritance is **autosomal dominant**. Each child of an affected heterozygous individual has a 50% probability of inheriting the variant, subject to confirmation that the parent is heterozygous and excluding mosaicism. Both sexes are expected to be affected equally; no sex-specific penetrance is established. Expressivity is variable, including possible COL1A1-versus-COL1A2 severity differences. No genetic anticipation is expected because this is not a repeat-expansion disorder. (malfait2017the2017international pages 12-13, martinmartin2022ehlers–danlossyndrometype pages 7-8)

Population prevalence and annual incidence are unknown. The strongest available statistic is approximately **42 published patients worldwide by 2022**. This is a literature count, not prevalence. Aggregate EDS estimates—including 1:5,000 or EDS/hypermobility-code prevalence from national EHR studies—must not be assigned to aEDS. (martinmartin2022ehlers–danlossyndrometype pages 7-8, martinmartin2022ehlers–danlossyndrometype pages 1-2)

No founder effect, ancestry enrichment, geographic concentration, carrier frequency, or role for consanguinity has been established. Consanguinity is not expected to be a major determinant for an autosomal-dominant disorder. Parental germline mosaicism is biologically possible in an apparently de novo case, but an aEDS-specific recurrence rate was not found.

## 10. Diagnostics

### Clinical criteria

The 2017 minimum criteria suggestive of aEDS are:

- congenital bilateral hip dislocation; **and**
- either skin hyperextensibility or severe generalized joint hypermobility with multiple dislocations/subluxations; **and**
- at least two minor criteria: hypotonia, kyphoscoliosis, mild radiographic osteopenia, tissue fragility/atrophic scars, or easy bruising.

A definitive diagnosis requires identification of a causal COL1A1 or COL1A2 variant producing complete or partial exon-6 loss. Clinical criteria alone are insufficient because of overlap with other EDS and skeletal dysplasia phenotypes. (malfait2017the2017international pages 12-13)

### Recommended testing algorithm

1. Document congenital hip status, generalized hypermobility, dislocation history, skin/scar findings, hypotonia, spine/foot deformity, bruising and family history.
2. Perform sequencing of **COL1A1 and COL1A2**, preferably through a validated EDS/heritable connective-tissue-disorder panel that includes splice boundaries and permits phenotype-based differential diagnosis.
3. If negative, perform exon-level deletion/duplication/CNV analysis and review coverage of exon 6 and adjacent intronic regions.
4. For a candidate splice variant, use RNA studies where possible to demonstrate partial or complete exon-6 loss.
5. If panel testing is unrevealing despite a compelling phenotype, WES or WGS can identify atypical intronic/structural lesions or an alternative diagnosis. WGS is especially useful for noncoding splice and structural variants; neither WES nor WGS replaces functional splice interpretation.
6. Segregation and parental testing distinguish inherited from de novo disease and support recurrence counseling.

CMA, karyotyping, FISH, mitochondrial DNA testing and repeat-expansion testing are not routine aEDS tests unless another diagnosis is suspected.

### Ancillary tests

Cultured skin-fibroblast collagen analysis can identify abnormal pN-collagen chains. Skin-biopsy transmission electron microscopy may reveal small, irregular, ragged and disorganized collagen fibrils and can provide supportive evidence, including possible distinction in severity between VIIA and VIIB; it does not replace molecular confirmation. (giunta2008thearthrochalasiatype pages 2-3, giunta2008thearthrochalasiatype pages 1-2)

Clinical evaluation may include hip/spine/foot radiography, bone-density assessment when clinically indicated, echocardiography based on baseline evaluation or symptoms, and vascular imaging only when individualized risk or clinical findings justify it. There is no validated circulating biomarker, enzyme assay, liquid biopsy, electrophysiologic signature, or omics-based diagnostic test.

### Differential diagnosis

- **Other EDS subtypes:** especially classical, classical-like, dermatosparaxis, kyphoscoliotic, musculocontractural and spondylodysplastic EDS; distinguish by molecular testing and subtype-specific skin, vascular, craniofacial or congenital-contracture findings.
- **Osteogenesis imperfecta/COL1-related overlap disorder:** fracture burden, blue sclerae and dentinogenesis imperfecta favor OI, although overlap occurs.
- **Larsen syndrome:** multiple congenital large-joint dislocations and characteristic craniofacial/skeletal findings; FLNB testing.
- **Loeys–Dietz syndrome:** arterial aneurysm/tortuosity and craniofacial findings; TGF-β-pathway genes.
- **Cutis laxa syndromes:** lax rather than hyperextensible/recoiling skin and subtype-specific systemic disease.
- **Congenital hip dysplasia, Marfan syndrome, FLNA-related disorders, and neuromuscular hypotonia syndromes.** The aEDS systematic review specifically highlights Larsen, Loeys–Dietz and cutis laxa syndromes. (martinmartin2022ehlers–danlossyndrometype pages 7-8)

No population newborn screen exists. Appropriate screening is phenotype-triggered testing and cascade testing of relatives after a familial variant is established.

## 11. Outcome and prognosis

No 5- or 10-year survival estimates, disease-specific mortality rate, or validated life-expectancy estimate exists. Available evidence does not show the severe arterial-rupture mortality pattern characteristic of vascular EDS. One systematic review found a vascular complication in **1 of 17 aEDS patients (6%)**, and a case report described progressive mitral, aortic and tricuspid regurgitation; both findings warrant awareness but are too sparse to quantify lifetime risk. (dhondt2018vascularphenotypesin pages 3-4, martinmartin2022ehlers–danlossyndrometype pages 4-5)

One neonatal death in a baby born at 35 weeks was included in the 2022 review, but the evidence does not establish a general neonatal mortality rate. Intellectual development is generally normal. Fractures appear uncommon despite mild osteopenia in some patients. (martinmartin2022ehlers–danlossyndrometype pages 7-8, martinmartin2022ehlers–danlossyndrometype pages 5-7)

Principal morbidity is orthopedic and functional: congenital hip disease, recurrent instability/dislocation, spinal and foot deformity, pain, impaired mobility, skin injury, bruising and surgical/wound complications. Recovery from an individual dislocation or operation is possible, but the underlying collagen defect and lifelong predisposition do not resolve. Prognostic factors have not been validated; plausible factors include variant/gene, severity of congenital instability, scoliosis, recurrent trauma, muscle conditioning and access to specialist care.

## 12. Treatment

### Current strategy

There is **no approved curative, gene, RNA, cell, enzyme-replacement, targeted, or disease-modifying treatment**. The 2022 review’s abstract states: **“Treatment is currently symptomatic and focuses on increasing the quality of life of these patients, as there is no curative treatment.”** (martinmartin2022ehlers–danlossyndrometype pages 1-2)

Management should be multidisciplinary and individualized:

- **Physiotherapy/rehabilitation:** low-impact strengthening, proprioceptive training, postural and gait work, and prevention of deconditioning; avoid forceful end-range maneuvers. Suggested NCIT terms: Physical Therapy, Rehabilitation Therapy.
- **Occupational therapy and joint protection:** activity modification, ergonomic support, adaptive equipment and fatigue management. NCIT: Occupational Therapy, Supportive Care.
- **Orthoses and mobility aids:** braces, splints, footwear, walking aids or wheelchairs according to instability and function. NCIT: Orthotic Device, Assistive Device.
- **Pain management:** multimodal nonpharmacologic care; acetaminophen or appropriately selected analgesics as clinically indicated. No aEDS-specific drug-response or pharmacogenomic data exist. NCIT: Pain Management, Analgesic Therapy.
- **Skin/wound care:** minimize trauma and adhesive injury; careful closure, prolonged support where appropriate, and monitoring for delayed healing or hematoma. NCIT: Wound Care.
- **Orthopedic intervention:** early specialist assessment of congenital hip/knee dislocation, clubfoot and progressive deformity; surgery only after careful risk–benefit evaluation and when conservative care is inadequate. NCIT: Orthopedic Surgery, Joint Stabilization Procedure.
- **Cardiac/vascular care:** symptom-driven or individualized surveillance; standard cardiology management for documented valve or vascular disease.
- **Pregnancy:** high-risk obstetric planning, careful positioning and attention to malpresentation, premature membrane rupture, tissue fragility and postpartum injury. (martinmartin2022ehlers–danlossyndrometype pages 7-8, martinmartin2022ehlers–danlossyndrometype pages 4-5)

### Surgical evidence and 2024 development

The October 2024 EDS-wide scoping review found 71 primary orthopedic studies from 1990–2023—38 single case reports, 14 case series and 19 retrospective cohorts—and **no randomized trials**. Outcomes were inconsistent, and no reliable long-term benefit or aEDS-specific protocol could be established. (schubart2024outcomesoforthopaedic pages 1-2)

A retrospective EDS surgical cohort reported 290 postoperative complications after 320 procedures, with a complication recorded in 91% of cases; however, subtype assignment was unreliable and these data cannot be directly converted into an aEDS risk estimate. General concerns include persistent instability/pain, fixation failure, bleeding, infection, poor wound healing and reoperation. These findings support cautious planning, not avoidance of all necessary surgery. (schubart2024outcomesoforthopaedic pages 15-16, yonko2021orthopedicconsiderationsand pages 1-1, yonko2021orthopedicconsiderationsand pages 6-6)

The ClinicalTrials.gov search retrieved no relevant aEDS-specific interventional trial. No NCT identifier, response rate, or treatment-related adverse-event series specific to aEDS was identified.

## 13. Prevention

**Primary prevention:** The occurrence of a de novo pathogenic variant cannot currently be prevented. For known familial disease, reproductive options include genetic counseling, prenatal diagnosis and preimplantation genetic testing for the established familial variant. These prevent or inform transmission risk; they are not therapies.

**Secondary prevention:** Early diagnosis in an infant with bilateral hip dislocation, severe hypermobility and hypotonia permits appropriate handling, orthopedic care, avoidance of damaging procedures, and cascade testing. There is no population newborn screening or routine carrier screening because aEDS is autosomal dominant and exceptionally rare.

**Tertiary prevention:** Joint-protection education, safe strengthening, appropriate bracing, fall prevention, avoidance of high-impact/contact activities, cautious manual therapy, skin protection, dental and surgical planning, monitoring of deformity and individualized cardiac assessment aim to reduce complications. Vaccination, antimicrobial prophylaxis and environmental remediation have no disease-specific preventive role.

Genetic counseling should explain the 50% transmission risk from a heterozygous affected parent, variable expressivity, possibility of a de novo variant, and residual recurrence risk from parental mosaicism.

## 14. Other species and natural disease

No naturally occurring animal disorder was identified that is securely established as the direct orthologue of human aEDS caused by a heterozygous COL1A1 or COL1A2 exon-6 lesion. EDS-like diseases occur in dogs and other domestic species, but retrieved canine evidence concerned **ADAMTS2-related dermatosparaxis**, not arthrochalasia; it must not be curated as an aEDS model. (lamande2020geneticdisordersof pages 1-2)

Relevant conserved orthologues include mouse *Col1a1/Col1a2*, rat *Col1a1/Col1a2*, zebrafish *col1a1a/col1a1b/col1a2*, and canine *COL1A1/COL1A2*. The collagen-I processing pathway is evolutionarily conserved, but an exact spontaneous veterinary aEDS genotype–phenotype relationship was not established in the retrieved literature. There is no infectious transmission, zoonotic potential or cross-species contagion.

## 15. Model organisms and experimental systems

The most disease-proximal established experimental system is **patient-derived cultured dermal fibroblasts**, which reproduce abnormal transcript processing and secretion/incorporation of pN-collagen. Skin-biopsy transmission electron microscopy directly demonstrates abnormal fibril architecture. These systems are suitable for RNA-splicing assays, collagen electrophoresis, extracellular-matrix imaging and testing splice-correction concepts. (giunta2008thearthrochalasiatype pages 2-3, giunta2008thearthrochalasiatype pages 1-2)

A 2014 mouse was described as a model of combined osteogenesis imperfecta and EDS, but its variants were outside collagen exon 6. It is therefore mechanistically adjacent, not an exact aEDS model, and should not be annotated as fully recapitulating arthrochalasia EDS.

No validated exon-6 aEDS knock-in mouse, rat, zebrafish, Drosophila, organoid, iPSC, humanized model, or CRISPR functional-genomics screen was identified. A high-priority model would be a heterozygous splice-site or precise exon-6 deletion knock-in in *Col1a1* or *Col1a2*, assessed for pN-collagen retention, fibril ultrastructure, congenital hip instability, generalized laxity, skin mechanics and bone phenotype. Its limitations would include species-specific hip development and difficulty quantifying subjective pain and disability.

## Evidence synthesis and research priorities

The strongest evidence is the concordance of molecularly confirmed human cases, patient-fibroblast biochemistry and dermal electron microscopy. Together these establish a causal sequence from COL1A1/COL1A2 exon-6 loss to retained N-propeptide, abnormal fibrillogenesis and systemic connective-tissue laxity. (giunta2008thearthrochalasiatype pages 2-3, giunta2008thearthrochalasiatype pages 1-2, malfait2020theehlers–danlossyndromes pages 6-7)

The most important knowledge gaps are reliable prevalence, prospective natural history, variant-level penetrance and expressivity, validated quality-of-life data, aEDS-specific cardiac/vascular risk, pregnancy outcomes, orthopedic-treatment comparisons, molecular profiling, exact animal models and disease-modifying therapy. The 2024 orthopedic review reinforces the expert view that subtype-confirmed multicenter registries and standardized outcomes are prerequisites for evidence-based surgical algorithms. (schubart2024outcomesoforthopaedic pages 15-16, schubart2024outcomesoforthopaedic pages 1-2)

### Key references

1. Malfait F, et al. **The 2017 international classification of the Ehlers–Danlos syndromes.** *Am J Med Genet C.* Published March 2017. PMID: 28306229. https://doi.org/10.1002/ajmg.c.31552. (malfait2017the2017international pages 12-13)
2. Martín-Martín M, et al. **Ehlers–Danlos Syndrome Type Arthrochalasia: A Systematic Review.** *Int J Environ Res Public Health.* Published 7 February 2022;19:1870. https://doi.org/10.3390/ijerph19031870. (martinmartin2022ehlers–danlossyndrometype pages 7-8, martinmartin2022ehlers–danlossyndrometype pages 1-2)
3. Giunta C, et al. **The arthrochalasia type of Ehlers–Danlos syndrome (EDS VIIA and VIIB): the diagnostic value of collagen fibril ultrastructure.** *Am J Med Genet A.* Published April 2008;146A:1341–1346. PMID: 18409203. https://doi.org/10.1002/ajmg.a.32213. (giunta2008thearthrochalasiatype pages 2-3, giunta2008thearthrochalasiatype pages 1-2)
4. Brady AF, et al. **The Ehlers–Danlos syndromes, rare types.** *Am J Med Genet C.* Published March 2017;175:115–170. https://doi.org/10.1002/ajmg.c.31550. (brady2017theehlers–danlossyndromes pages 8-9)
5. Malfait F, et al. **The Ehlers–Danlos syndromes.** *Nature Reviews Disease Primers.* Published July 2020;6. https://doi.org/10.1038/s41572-020-0194-9. (malfait2020theehlers–danlossyndromes pages 6-7)
6. D’Hondt S, Van Damme T, Malfait F. **Vascular phenotypes in nonvascular subtypes of the Ehlers-Danlos syndrome: a systematic review.** *Genetics in Medicine.* Published June 2018. https://doi.org/10.1038/gim.2017.138. (dhondt2018vascularphenotypesin pages 3-4, dhondt2018vascularphenotypesin pages 1-2)
7. Schubart JR, et al. **Outcomes of orthopaedic surgery in Ehlers-Danlos syndromes: a scoping review.** *BMC Musculoskeletal Disorders.* Published October 2024;25. https://doi.org/10.1186/s12891-024-07937-6. (schubart2024outcomesoforthopaedic pages 15-16, schubart2024outcomesoforthopaedic pages 1-2)
8. Yonko EA, et al. **Orthopedic considerations and surgical outcomes in Ehlers–Danlos syndromes.** *Am J Med Genet C.* Published November 2021;187:458–465. https://doi.org/10.1002/ajmg.c.31958. (yonko2021orthopedicconsiderationsand pages 1-1, yonko2021orthopedicconsiderationsand pages 6-6)

References

1. (martinmartin2022ehlers–danlossyndrometype pages 7-8): Marta Martín-Martín, Jonathan Cortés-Martín, Maria Isabel Tovar-Gálvez, Juan Carlos Sánchez-García, Lourdes Díaz-Rodríguez, and Raquel Rodríguez-Blanque. Ehlers–danlos syndrome type arthrochalasia: a systematic review. Feb 2022. URL: https://doi.org/10.3390/ijerph19031870, doi:10.3390/ijerph19031870. This article has 18 citations.

2. (martinmartin2022ehlers–danlossyndrometype pages 1-2): Marta Martín-Martín, Jonathan Cortés-Martín, Maria Isabel Tovar-Gálvez, Juan Carlos Sánchez-García, Lourdes Díaz-Rodríguez, and Raquel Rodríguez-Blanque. Ehlers–danlos syndrome type arthrochalasia: a systematic review. Feb 2022. URL: https://doi.org/10.3390/ijerph19031870, doi:10.3390/ijerph19031870. This article has 18 citations.

3. (schubart2024outcomesoforthopaedic pages 1-2): Jane R. Schubart, Susan E. Mills, Scott A. Rodeo, and Clair A. Francomano. Outcomes of orthopaedic surgery in ehlers-danlos syndromes: a scoping review. BMC Musculoskeletal Disorders, Oct 2024. URL: https://doi.org/10.1186/s12891-024-07937-6, doi:10.1186/s12891-024-07937-6. This article has 14 citations and is from a peer-reviewed journal.

4. (malfait2017the2017international pages 12-13): Fransiska Malfait, Clair Francomano, Peter Byers, John Belmont, Britta Berglund, James Black, Lara Bloom, Jessica M. Bowen, Angela F. Brady, Nigel P. Burrows, Marco Castori, Helen Cohen, Marina Colombi, Serwet Demirdas, Julie De Backer, Anne De Paepe, Sylvie Fournel‐Gigleux, Michael Frank, Neeti Ghali, Cecilia Giunta, Rodney Grahame, Alan Hakim, Xavier Jeunemaitre, Diana Johnson, Birgit Juul‐Kristensen, Ines Kapferer‐Seebacher, Hanadi Kazkaz, Tomoki Kosho, Mark E. Lavallee, Howard Levy, Roberto Mendoza‐Londono, Melanie Pepin, F. Michael Pope, Eyal Reinstein, Leema Robert, Marianne Rohrbach, Lynn Sanders, Glenda J. Sobey, Tim Van Damme, Anthony Vandersteen, Caroline van Mourik, Nicol Voermans, Nigel Wheeldon, Johannes Zschocke, and Brad Tinkle. The 2017 international classification of the ehlers–danlos syndromes. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 175:26-8, Mar 2017. URL: https://doi.org/10.1002/ajmg.c.31552, doi:10.1002/ajmg.c.31552. This article has 2455 citations.

5. (wenstrup2002prevalenceofaortic pages 1-2): Richard J. Wenstrup, Richard A. Meyer, Jennifer S. Lyle, Leah Hoechstetter, Peter S. Rose, Howard P. Levy, and Claire A. Francomano. Prevalence of aortic root dilation in the ehlers-danlos syndrome. Genetics in Medicine, 4:112-117, May 2002. URL: https://doi.org/10.1097/00125817-200205000-00003, doi:10.1097/00125817-200205000-00003. This article has 164 citations and is from a highest quality peer-reviewed journal.

6. (OpenTargets Search: arthrochalasia Ehlers-Danlos syndrome-COL1A1,COL1A2): Open Targets Query (arthrochalasia Ehlers-Danlos syndrome-COL1A1,COL1A2, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (giunta2008thearthrochalasiatype pages 1-2): Cecilia Giunta, Céline Chambaz, Marina Pedemonte, Sara Scapolan, and Beat Steinmann. The arthrochalasia type of ehlers–danlos syndrome (eds viia and viib): the diagnostic value of collagen fibril ultrastructure. American Journal of Medical Genetics Part A, 146A(10):1341-1346, Apr 2008. URL: https://doi.org/10.1002/ajmg.a.32213, doi:10.1002/ajmg.a.32213. This article has 46 citations.

8. (giunta2008thearthrochalasiatype pages 2-3): Cecilia Giunta, Céline Chambaz, Marina Pedemonte, Sara Scapolan, and Beat Steinmann. The arthrochalasia type of ehlers–danlos syndrome (eds viia and viib): the diagnostic value of collagen fibril ultrastructure. American Journal of Medical Genetics Part A, 146A(10):1341-1346, Apr 2008. URL: https://doi.org/10.1002/ajmg.a.32213, doi:10.1002/ajmg.a.32213. This article has 46 citations.

9. (malfait2020theehlers–danlossyndromes pages 6-7): Fransiska Malfait, Marco Castori, Clair A. Francomano, Cecilia Giunta, Tomoki Kosho, and Peter H. Byers. The ehlers–danlos syndromes. Nature Reviews Disease Primers, 6:1-25, Jul 2020. URL: https://doi.org/10.1038/s41572-020-0194-9, doi:10.1038/s41572-020-0194-9. This article has 409 citations.

10. (brady2017theehlers–danlossyndromes pages 8-9): Angela F. Brady, Serwet Demirdas, Sylvie Fournel‐Gigleux, Neeti Ghali, Cecilia Giunta, Ines Kapferer‐Seebacher, Tomoki Kosho, Roberto Mendoza‐Londono, Michael F. Pope, Marianne Rohrbach, Tim Van Damme, Anthony Vandersteen, Caroline van Mourik, Nicol Voermans, Johannes Zschocke, and Fransiska Malfait. The ehlers–danlos syndromes, rare types. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 175:115-70, Mar 2017. URL: https://doi.org/10.1002/ajmg.c.31550, doi:10.1002/ajmg.c.31550. This article has 318 citations.

11. (martinmartin2022ehlers–danlossyndrometype pages 5-7): Marta Martín-Martín, Jonathan Cortés-Martín, Maria Isabel Tovar-Gálvez, Juan Carlos Sánchez-García, Lourdes Díaz-Rodríguez, and Raquel Rodríguez-Blanque. Ehlers–danlos syndrome type arthrochalasia: a systematic review. Feb 2022. URL: https://doi.org/10.3390/ijerph19031870, doi:10.3390/ijerph19031870. This article has 18 citations.

12. (dhondt2018vascularphenotypesin pages 3-4): Sanne D'hondt, Tim Van Damme, and Fransiska Malfait. Vascular phenotypes in nonvascular subtypes of the ehlers-danlos syndrome: a systematic review. Jun 2018. URL: https://doi.org/10.1038/gim.2017.138, doi:10.1038/gim.2017.138. This article has 107 citations and is from a highest quality peer-reviewed journal.

13. (martinmartin2022ehlers–danlossyndrometype pages 4-5): Marta Martín-Martín, Jonathan Cortés-Martín, Maria Isabel Tovar-Gálvez, Juan Carlos Sánchez-García, Lourdes Díaz-Rodríguez, and Raquel Rodríguez-Blanque. Ehlers–danlos syndrome type arthrochalasia: a systematic review. Feb 2022. URL: https://doi.org/10.3390/ijerph19031870, doi:10.3390/ijerph19031870. This article has 18 citations.

14. (schubart2024outcomesoforthopaedic pages 15-16): Jane R. Schubart, Susan E. Mills, Scott A. Rodeo, and Clair A. Francomano. Outcomes of orthopaedic surgery in ehlers-danlos syndromes: a scoping review. BMC Musculoskeletal Disorders, Oct 2024. URL: https://doi.org/10.1186/s12891-024-07937-6, doi:10.1186/s12891-024-07937-6. This article has 14 citations and is from a peer-reviewed journal.

15. (islam2021ehlersdanlossyndromeimmunologic pages 31-33): Mareesa Islam, Christopher Chang, and M. Eric Gershwin. Ehlers-danlos syndrome: immunologic contrasts and connective tissue comparisons. Jan 2021. URL: https://doi.org/10.1016/j.jtauto.2020.100077, doi:10.1016/j.jtauto.2020.100077. This article has 40 citations and is from a peer-reviewed journal.

16. (martinmartin2022ehlers–danlossyndrometype pages 2-4): Marta Martín-Martín, Jonathan Cortés-Martín, Maria Isabel Tovar-Gálvez, Juan Carlos Sánchez-García, Lourdes Díaz-Rodríguez, and Raquel Rodríguez-Blanque. Ehlers–danlos syndrome type arthrochalasia: a systematic review. Feb 2022. URL: https://doi.org/10.3390/ijerph19031870, doi:10.3390/ijerph19031870. This article has 18 citations.

17. (yonko2021orthopedicconsiderationsand pages 2-3): Elizabeth A. Yonko, Holly M. LoTurco, Erin M. Carter, and Cathleen L. Raggio. Orthopedic considerations and surgical outcomes in ehlers–danlos syndromes. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 187:458-465, Nov 2021. URL: https://doi.org/10.1002/ajmg.c.31958, doi:10.1002/ajmg.c.31958. This article has 36 citations.

18. (lucente2024chiropractictreatmentof pages 1-2): M Lucente and KS Walden. Chiropractic treatment of a patient with ehlers-danlos syndrome: a case report. Unknown journal, 2024.

19. (lamande2020geneticdisordersof pages 1-2): Shireen R. Lamandé and John F. Bateman. Genetic disorders of the extracellular matrix. Anatomical Record (Hoboken, N.j. : 2007), 303:1527-1542, Mar 2020. URL: https://doi.org/10.1002/ar.24086, doi:10.1002/ar.24086. This article has 129 citations.

20. (yonko2021orthopedicconsiderationsand pages 1-1): Elizabeth A. Yonko, Holly M. LoTurco, Erin M. Carter, and Cathleen L. Raggio. Orthopedic considerations and surgical outcomes in ehlers–danlos syndromes. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 187:458-465, Nov 2021. URL: https://doi.org/10.1002/ajmg.c.31958, doi:10.1002/ajmg.c.31958. This article has 36 citations.

21. (yonko2021orthopedicconsiderationsand pages 6-6): Elizabeth A. Yonko, Holly M. LoTurco, Erin M. Carter, and Cathleen L. Raggio. Orthopedic considerations and surgical outcomes in ehlers–danlos syndromes. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 187:458-465, Nov 2021. URL: https://doi.org/10.1002/ajmg.c.31958, doi:10.1002/ajmg.c.31958. This article has 36 citations.

22. (dhondt2018vascularphenotypesin pages 1-2): Sanne D'hondt, Tim Van Damme, and Fransiska Malfait. Vascular phenotypes in nonvascular subtypes of the ehlers-danlos syndrome: a systematic review. Jun 2018. URL: https://doi.org/10.1038/gim.2017.138, doi:10.1038/gim.2017.138. This article has 107 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Arthrochalasia_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 15 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007525` (5 mentions) - the report calls it "if available"; MONDO calls it **Ehlers-Danlos syndrome, arthrochalasia type**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Gene`, `Taxon`.