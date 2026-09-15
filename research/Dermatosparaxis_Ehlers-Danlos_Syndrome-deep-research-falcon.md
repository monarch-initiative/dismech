---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-15T22:35:35.890672'
end_time: '2026-09-15T22:46:03.890319'
duration_seconds: 628.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dermatosparaxis Ehlers-Danlos Syndrome
  mondo_id: MONDO:0009161
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 40
  verified: 39
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 15
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0009161
    reported_labels:
    - if available
    ontology_label: Ehlers-Danlos syndrome, dermatosparaxis type
  obsolete_terms:
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dermatosparaxis_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dermatosparaxis Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0009161 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dermatosparaxis Ehlers-Danlos Syndrome** covering all of the
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
- **Disease Name:** Dermatosparaxis Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0009161 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dermatosparaxis Ehlers-Danlos Syndrome** covering all of the
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


# Dermatosparaxis Ehlers–Danlos syndrome: disease-characteristics report

## Executive summary and evidence scope

Dermatosparaxis Ehlers–Danlos syndrome (dEDS) is an ultra-rare, autosomal-recessive connective-tissue disorder caused by biallelic pathogenic variants in **ADAMTS2**. Deficient ADAMTS-2-mediated removal of amino-terminal propeptides from fibrillar procollagens—especially types I and III in skin—produces abnormally organized collagen fibrils and extreme tissue fragility. Hallmarks are congenital or early-childhood skin fragility, easy bruising, soft/doughy or redundant skin, characteristic craniofacial findings, joint hypermobility, umbilical hernia, and postnatal growth restriction. Visceral, vascular, and hemorrhagic complications occur but are incompletely quantified. The best quantified human dataset remains only 15 molecularly confirmed individuals; consequently, percentages below are descriptive, not robust population estimates. A 2024 expert review still classified prevalence as below 1 per 1,000,000 and noted only 15 reported children, with very limited adult follow-up. (dijk2024clinicaldiagnosisof pages 3-4)

Evidence types are labeled where important: **human clinical/genetic**, **human fibroblast/in-vitro**, **mouse knockout**, **natural veterinary disease**, or **expert review**. Recent dEDS-specific research in 2023–2024 was sparse; the principal 2024 advances were updated clinical and molecular diagnostic guidance rather than therapeutic trials. (dijk2024clinicaldiagnosisof pages 3-4, zschocke2024geneticdiagnosisof pages 8-9)

## 1. Disease information

### Definition and nomenclature

dEDS is one of the monogenic Ehlers–Danlos syndromes, characterized by connective-tissue fragility arising from defective collagen processing. Historical names include **Ehlers–Danlos syndrome type VIIC**, **EDS VIIC**, **human dermatosparaxis**, **dermatosparactic EDS**, and **EDS dermatosparaxis type**. (kapfererseebacher2020dentalmanifestationsof pages 1-2, malek2021theroleof pages 2-3, colige1999humanehlersdanlossyndrome pages 1-2)

**Identifiers**

- **MONDO:** MONDO:0009161, as supplied in the target specification.
- **OMIM/MIM:** **225410**. (neto2024unravelingthegenetic pages 5-6, malek2021theroleof pages 2-3, colige1999humanehlersdanlossyndrome pages 1-2)
- **Causal-gene disease label:** ADAMTS2-related dermatosparaxis EDS.
- **Orphanet:** an Orphanet disease entry exists, but its numeric ORPHA identifier was not established by the retrieved primary texts and should be verified directly before database loading.
- **ICD-10:** no dEDS-specific code was established in the retrieved literature; it is generally subsumed under Ehlers–Danlos syndrome/congenital connective-tissue-malformation coding rather than represented as a subtype-specific diagnosis.
- **ICD-11 and MeSH:** no dEDS-specific identifiers were verified in the retrieved full texts; use the broader Ehlers–Danlos syndrome concept with an ADAMTS2/dEDS qualifier after direct terminology-service validation.

The evidence summarized here is predominantly **aggregated disease-level literature**—case series, reviews, and experimental studies—not longitudinal EHR-derived data. Individual-patient observations from published case reports/series underpin many phenotype claims.

## 2. Etiology, risk, protection, and environment

### Primary cause

The necessary initiating lesion is usually **biallelic germline loss of ADAMTS2 function**. ADAMTS2 encodes an extracellular zinc metalloprotease, historically called procollagen-I N-proteinase, that removes amino-terminal propeptides from major fibrillar procollagens. The landmark study found homozygous p.Gln225Ter in five of six then-known patients and homozygous p.Trp795Ter in the sixth, directly linking absent enzyme activity to human EDS VIIC. (colige1999humanehlersdanlossyndrome pages 1-2)

### Genetic risk factors

Risk is determined primarily by inheriting two pathogenic alleles. Reported mechanisms include nonsense, frameshift, canonical splice-site, start-loss, and likely hypomorphic missense variants. Homozygosity is common in consanguineous families, although compound heterozygosity and affected individuals from nonconsanguineous families occur. In the 15-person summary, three individuals had known consanguineous parents; this is ascertainment evidence, not a population risk estimate. (damme2016expandingtheclinical pages 2-3, damme2016expandingtheclinical pages 7-8)

The 2016 human study reported:

- c.2927_2928delCT, p.(Pro976Argfs*42), homozygous;
- c.669_670dupG, p.(Pro224Argfs*24), homozygous;
- c.2751-2A>T, causing out-of-frame exon-19 skipping, homozygous;
- compound heterozygous c.2T>C, p.? and c.884_887delTGAA, p.(Met295Thrfs*26). (damme2016expandingtheclinical pages 1-2, damme2016expandingtheclinical pages 5-7, damme2016expandingtheclinical pages 7-8)

These variants were absent from the population databases queried at the time—1000 Genomes, ESP6500, and ExAC—and several truncated transcripts underwent nonsense-mediated decay, demonstrated by markedly reduced fibroblast ADAMTS2 RNA. Modern gnomAD frequencies and current ClinVar classifications must be checked variant-by-variant; historical absence is not a substitute for current frequency data. (damme2016expandingtheclinical pages 2-3, damme2016expandingtheclinical pages 7-8)

### Modifiers and protective factors

No validated human modifier gene or protective allele is known. **ADAMTS3 and ADAMTS14 are biologically plausible tissue-specific compensators**, not established clinical protective factors: ADAMTS3 processed procollagen I in dermatosparactic fibroblasts, while Adamts14 overlapped with Adamts2 in mature mouse dermis. Their differential expression may explain why skin is more severely affected than cartilage, tendon, bone, cornea, or aorta. (goff2006regulationofprocollagen pages 1-2, goff2006regulationofprocollagen pages 7-8)

There are no demonstrated dietary, lifestyle, pharmacological, or environmental factors that prevent the genotype from causing disease. Trauma and invasive procedures do not cause dEDS, but mechanically challenge fragile tissue and can precipitate tears, hematomas, hemorrhage, prolapse, or rupture. Avoidance of trauma is therefore complication prevention, not etiologic prevention.

### Environmental and infectious factors

No toxin, radiation, pollution, occupational exposure, lifestyle behavior, or infectious organism is known to initiate dEDS. Smoking, alcohol, diet, and exercise have not been evaluated as disease-susceptibility factors. Gene–environment interaction is principally mechanical: genetically abnormal collagen reduces tissue tensile strength, while trauma, vomiting, defecation, surgery, and other physical stresses can reveal or exacerbate manifestations. Diaphragmatic rupture after vomiting and severe rectal prolapse/bleeding exemplify this interaction. (dijk2024clinicaldiagnosisof pages 3-4, damme2016expandingtheclinical pages 2-3, damme2016expandingtheclinical pages 3-5)

## 3. Phenotypes

The most useful quantified summary comes from 15 molecularly confirmed individuals from 14 families. Missing entries meant “not reported,” so the following fractions are not unbiased penetrance estimates. (damme2016expandingtheclinical pages 5-7, damme2016expandingtheclinical pages 7-8)

| Domain | Feature | Reported count / denominator | Approx. percentage | Onset/course | Suggested HPO term |
|---|---|---:|---:|---|---|
| Skin | Severe skin fragility/skin tears | 14/15 | 93% | Congenital in 2; predominantly postnatal and may become more apparent with activity/age | Skin fragility (HP:0001030); Skin ulcer (HP:0200042) |
| Eye | Blue sclerae | 13/15 | 87% | Usually congenital or evident in early childhood | Blue sclerae (HP:0000592) |
| Growth | Postnatal growth restriction | 13/15 | 87% | Develops after birth; persistent short stature common | Postnatal growth retardation (HP:0008897) |
| Skin | Soft, doughy skin | 12/15 | 80% | Congenital or early childhood; persistent | Soft skin (HP:0000977) |
| Craniofacial | Epicanthic folds | 12/15 | 80% | Congenital/early childhood | Epicanthus (HP:0000286) |
| Craniofacial | Micrognathia | 12/15 | 80% | Congenital or progressively recognizable in childhood | Micrognathia (HP:0000347) |
| Craniofacial | Large fontanel/delayed closure | 11/15 | 73% | Congenital; closure delayed into childhood | Large fontanelle (HP:0000239); Delayed closure of the anterior fontanelle (HP:0001476) |
| Skin | Sagging or redundant skin | 11/15 | 73% | Often congenital in severe disease; may become more apparent postnatally | Redundant skin (HP:0001582) |
| Musculoskeletal | Joint hypermobility | 11/15 | 73% | Congenital or recognized in early childhood; persistent | Generalized joint hypermobility (HP:0002761) |
| Musculoskeletal/growth | Short limbs, hands, and feet | 11/15 | 73% | Postnatal growth pattern; generally persistent | Short limb (HP:0009826); Short hand (HP:0200055); Short foot (HP:0001773) |
| Hematologic/skin | Easy bruising | 11/15 | 73% | Usually begins in infancy or childhood; recurrent | Easy bruisability (HP:0000978) |
| Development | Delayed motor development | 8/15 | 53% | Infancy/early childhood; variable severity | Motor delay (HP:0001270) |
| Hemorrhagic | Bleeding complications | 7/15 | 47% | Congenital through later childhood; episodic and potentially severe | Abnormal bleeding (HP:0001892) |
| Visceral | Visceral fragility | 5/15 | 33% | Congenital or postnatal; episodic rupture/prolapse complications | Visceral tissue fragility (closest available: HP:0003549) |
| Abdominal wall | Umbilical hernia | 14/15 | 93% | Usually congenital | Umbilical hernia (HP:0001537) |
| Pregnancy/birth | Preterm birth | 9/15 | 60% | Prenatal/perinatal; mean gestational age across 14 individuals was 34 weeks 4 days | Premature birth (HP:0001622) |
| Pregnancy/birth | Preterm premature rupture of membranes (PPROM) | 6/15 | 40% | Prenatal; precedes some preterm deliveries | Premature rupture of membranes (HP:0001788) |
| Demographic | Sex ratio | 11 male:4 female | 73% male; 27% female | Cohort composition, not a phenotype or established sex predisposition | Biological sex (metadata; no disease-phenotype HPO term) |
| Evidence note | Missingness/ascertainment limitation | 15 molecularly confirmed individuals | Not applicable | Blank entries were “not reported”; counts therefore are not strict prevalence estimates | Evidence qualifier: incomplete phenotype ascertainment |
| Source | Van Damme et al., *Genetics in Medicine* (2016), DOI: 10.1038/gim.2015.188 | 15 individuals from 14 families | Not applicable | Published September 2016 | (damme2016expandingtheclinical pages 3-5, damme2016expandingtheclinical pages 5-7, damme2016expandingtheclinical pages 7-8) |


*Table: Key clinical findings in the 15 molecularly confirmed individuals summarized by Van Damme et al. Counts reflect reported observations with incomplete ascertainment, so percentages should not be interpreted as unbiased prevalence estimates.*

Additional reported manifestations include facial or mucosal lacerations, delayed healing, papyraceous or widened atrophic scars, translucent skin with visible veins, subcutaneous hematomas, hypertrichosis, hypotonia, pes planus, kyphoscoliosis, osteopenia, fractures including congenital skull fractures, myopia, microcornea, glaucoma, gingival hyperplasia or bleeding, microdontia/oligodontia, rectal prolapse, hiatal hernia, bladder diverticula/rupture, diaphragmatic rupture, mitral-valve prolapse, fatigue, and chronic joint pain. Dental evidence remains sparse and cannot support reliable frequencies. (dijk2024clinicaldiagnosisof pages 3-4, damme2016expandingtheclinical pages 3-5, damme2016expandingtheclinical pages 5-7, damme2016expandingtheclinical pages 7-8)

**Phenotype type and course.** Skin tears, bruising, hemorrhage, hernia, prolapse, and rupture are clinical signs or complications; joint pain and fatigue are symptoms; hypermobility, craniofacial gestalt, short extremities, and redundant skin are examination findings. Routine coagulation testing can be normal despite severe bleeding, as illustrated by a later adolescent case with normal CBC, coagulation factors, and rotational thromboelastometry. (balagopal2026exploringthehemorrhagic pages 1-4)

**Onset.** Severe disease can be evident prenatally or at birth through premature membrane rupture, prematurity, friable umbilical cord, congenital tears, skull fractures, or hemorrhage. Milder disease may initially be facial/oral fragility and become more generalized as childhood activity increases. Mean diagnosis age in the 2016 dataset was 62 months, ranging from birth to 13 years, illustrating diagnostic delay and variable expressivity. (damme2016expandingtheclinical pages 7-8)

**Quality of life.** No dEDS-specific EQ-5D, SF-36, PROMIS, or validated disease-specific quality-of-life study was found. Published patients nevertheless experienced recurrent suturing, surgery, activity-limiting tissue injury, progressive widespread joint pain, fatigue, gastrointestinal symptoms, bleeding, and intensive medical follow-up. These observations indicate potentially substantial functional and psychosocial burden but cannot be converted into population-level utility scores. (damme2016expandingtheclinical pages 2-3, damme2016expandingtheclinical pages 3-5)

## 4. Genetic and molecular information

### Causal gene and protein

- **Gene:** ADAMTS2; biallelic pathogenic variants.
- **Protein:** ADAMTS-2/procollagen-I N-proteinase, a secreted disintegrin-like metalloprotease with thrombospondin motifs, a zinc-binding catalytic site, cysteine-rich/disintegrin-like regions, and C-terminal ancillary domains. (goff2006regulationofprocollagen pages 1-2, colige1999humanehlersdanlossyndrome pages 1-2)
- **Disease mechanism:** predominantly loss of function through premature termination, aberrant splicing, or nonsense-mediated RNA decay.
- **Origin:** constitutional/germline. Somatic ADAMTS2 variants are not the cause of inherited dEDS.

The evidence for causality is strong: recessive segregation, recurrent truncating variants, absent/reduced enzymatic activity, abnormal procollagen processing, fibroblast transcript loss, collagen-fibril abnormalities, concordant animal disease, and knockout phenocopy. (colige1999humanehlersdanlossyndrome pages 1-2, damme2016expandingtheclinical pages 5-7, damme2016expandingtheclinical pages 7-8)

### Variant interpretation

Established biallelic null alleles are generally pathogenic under ACMG/AMP concepts because loss of function is the known mechanism. Missense variants require caution: rarity and computational prediction alone are insufficient, and enzymatic, RNA, biochemical, segregation, or collagen-ultrastructure evidence is desirable. A VUS should not by itself confirm dEDS; a 2024 expert review warned that indiscriminate testing can create misleading VUS-based diagnoses. (zschocke2024geneticdiagnosisof pages 2-3)

No validated dominant-negative or gain-of-function dEDS mechanism is known. Large deletions are biologically possible and should be detectable through copy-number analysis, but no recurrent chromosomal rearrangement or aneuploidy defines dEDS. No disease-specific DNA-methylation signature, histone alteration, or other epigenetic biomarker has been established.

### Genotype–phenotype relationship

The 2016 cohort expanded the phenotype to include markedly milder patients despite molecularly demonstrated deficient ADAMTS-2 activity and abnormal procollagen processing. In natural canine disease, early truncating c.10delC/p.(Pro4ArgfsTer175) produced catastrophic juvenile skin fragility with euthanasia before 13 weeks in six dogs, whereas a homozygous p.(Arg966His) dog survived at least nine years, consistent with residual activity as a plausible—but unproven—explanation. This supports quantitative residual function as a candidate severity determinant but does not establish a human prognostic rule. (jaffey2022novelhomozygousadamts2 pages 1-2)

## 5. Environmental information

Environmental causation is **not applicable**. Practical exposure modifiers include trauma, friction, contact sports, falls, poorly fitted equipment, surgery, endoscopy, arterial puncture, forceful vomiting, and constipation/straining. These can precipitate complications in genetically fragile tissue. No infectious trigger, transmissible agent, or zoonotic risk exists.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic ADAMTS2 variants lead to** absent or markedly reduced functional extracellular ADAMTS-2.
2. **Reduced ADAMTS-2 activity leads to** deficient cleavage of N-terminal propeptides from procollagens I and III; effects on type II collagen are often limited by tissue-specific ADAMTS3 compensation. (goff2006regulationofprocollagen pages 1-2, goff2006regulationofprocollagen pages 7-8)
3. **Failed cleavage leads to** accumulation of pN-collagen/procollagen species retaining amino-terminal propeptides, directly demonstrated in patient fibroblasts and Adamts2-null tissues. (colige1999humanehlersdanlossyndrome pages 1-2, damme2016expandingtheclinical pages 5-7)
4. **Retained propeptides lead to** abnormal lateral packing and assembly of collagen monomers into thin, branched, ribbon-like or “hieroglyphic” fibrils rather than regular cylindrical fibrils. (goff2006regulationofprocollagen pages 1-2, colige1999humanehlersdanlossyndrome pages 1-2)
5. **Abnormal fibrillogenesis leads to** reduced extracellular-matrix tensile strength, most prominently in dermis and other mechanically stressed connective tissues.
6. **Reduced tensile strength leads to** skin tearing, poor wound healing, bruising/hematoma, hernias, joint laxity, mucosal and visceral fragility, and—in some patients—major hemorrhage or organ rupture.
7. **Branch A: tissue-specific ADAMTS3/ADAMTS14 expression leads to** partial rescue of procollagen processing in cartilage, bone, muscle/tendon, mature dermis, cornea, and possibly aorta; this branch is experimentally supported in mice/in-vitro but remains inferred as a human severity modifier. (goff2006regulationofprocollagen pages 1-2, goff2006regulationofprocollagen pages 7-8, jaffey2022novelhomozygousadamts2 pages 14-15)
8. **Branch B: severe deficiency of type III procollagen processing in lung leads to** distal-airspace enlargement in Adamts2-null mice; pulmonary surveillance relevance in humans is plausible but not established. (goff2006regulationofprocollagen pages 7-8)

### Detailed biology and ontology suggestions

This is primarily an **extracellular-matrix biosynthesis/assembly disorder**, not a canonical Wnt, MAPK, mTOR, or PI3K–AKT signaling disease. Relevant biological processes include collagen biosynthesis and modification, extracellular-matrix organization, collagen-fibril organization, proteolysis, wound healing, and connective-tissue development. Suggested GO annotations include **extracellular matrix organization (GO:0030198)**, **collagen fibril organization (GO:0030199)**, **proteolysis (GO:0006508)**, **wound healing (GO:0042060)**, and **metalloendopeptidase activity (GO:0004222)**.

The main cell type is the collagen-producing **fibroblast** (suggested CL:0000057), with relevant mesenchymal cells including dermal fibroblasts, tendon/ligament fibroblasts, chondrocytes (CL:0000138), osteoblast-lineage cells (CL:0000062), vascular smooth-muscle cells (CL:0000359), and lung mesenchymal cells. Expression in mouse lung occurred in mesenchyme rather than bronchial epithelium. (goff2006regulationofprocollagen pages 7-8)

Subcellular/localization annotations include the **extracellular region (GO:0005576)**, **extracellular matrix (GO:0031012)**, **collagen-containing extracellular matrix (GO:0062023)**, and secretory pathway/ER for procollagen synthesis. The pathogenic cleavage and fibril-assembly defect is mainly extracellular; no primary mitochondrial, lysosomal, nuclear, autophagic, apoptotic, metabolic, or immune defect is established.

**Molecular profiling.** Patient fibroblast qPCR showed severely reduced ADAMTS2 expression for truncating alleles; radiolabeled-procollagen electrophoresis showed accumulation of pNα1(I)/pNα2(I) and near absence of pCα1(I)/pCα2(I); TEM showed irregular, branched fibrils, sometimes milder than the classic hieroglyphic pattern. These are targeted transcript, protein-processing, and ultrastructural findings—not unbiased transcriptomics, proteomics, metabolomics, lipidomics, single-cell, spatial, or multi-omics profiles. (damme2016expandingtheclinical pages 5-7, damme2016expandingtheclinical pages 7-8)

No dEDS-specific single-cell atlas, spatial transcriptomic map, metabolomic/lipidomic signature, patient organoid, iPSC model, or published therapeutic CRISPR screen was identified.

**Exact primary-literature statement:** Colige et al. reported that retained-propeptide molecules “self-assemble into abnormal ribbonlike fibrils that fail to provide normal tensile strength to tissues.” (colige1999humanehlersdanlossyndrome pages 1-2)

## 7. Anatomical structures affected

**Primary organs/tissues:** skin—especially dermis—and subcutaneous connective tissue; suggested **UBERON:0002097 (skin of body)** and **UBERON:0002067 (dermis)**. The extracellular collagen-fibril network is the primary tissue target.

**Additional structures:** joints, ligaments, tendons, skeletal connective tissue, craniofacial soft tissues, oral/gingival tissues, abdominal wall and umbilicus, gastrointestinal and pelvic-support tissues, diaphragm, bladder, eyes/sclera, and potentially vessels and lungs. Suggested terms include sclera (UBERON:0001775), lung (UBERON:0002048), urinary bladder (UBERON:0001255), diaphragm (UBERON:0001103), and umbilical region/umbilical cord where appropriate.

No consistent lateralization is expected. Findings are generally generalized or bilateral; individual tears, hematomas, fractures, or prolapses may be anatomically focal.

At the cellular level, dermal fibroblasts synthesize abnormal procollagen substrates, while the defect is manifested in collagen-containing ECM. At the subcellular level, procollagen synthesis begins in rough ER/Golgi, but pathogenic N-propeptide retention and fibril malassembly occur after secretion in the extracellular compartment. (goff2006regulationofprocollagen pages 1-2)

## 8. Temporal development and natural history

The molecular defect is present from conception, and the disease is congenital and lifelong. Prenatal/perinatal vulnerability includes membrane rupture, prematurity, friable or ruptured umbilical cord, congenital skin injury, skull fracture, and hemorrhage. In the 15-person series, nine were preterm, six had premature membrane rupture, mean gestational age among 14 was 34 weeks 4 days (range 28–41 weeks), and one newborn died from hemorrhage and shock. (damme2016expandingtheclinical pages 7-8)

During infancy and childhood, activity exposes skin and mucosal fragility; joint hypermobility, delayed motor development, postnatal growth restriction, and characteristic facial appearance become more apparent. Milder patients may lack striking neonatal redundant skin and develop generalized fragility later. Chronic later manifestations may include pain, fatigue, scarring, prolapse, varicose veins, ocular disease, and recurrent hemorrhage. (damme2016expandingtheclinical pages 2-3, damme2016expandingtheclinical pages 3-5, damme2016expandingtheclinical pages 7-8)

There is no validated staging system, remission pattern, or quantified progression rate. The disorder does not remit because the collagen-processing defect persists, although injury frequency may change with age, activity, protection, and residual enzyme function. Critical periods are pregnancy/delivery, early mobility, surgery or invasive procedures, and episodes of vomiting or straining.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two confirmed heterozygous parents, each pregnancy carries a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of a child inheriting neither familial variant. Unaffected siblings have a 2/3 carrier probability after excluding disease.

Clinical penetrance for two true null alleles appears high, but precise penetrance is unknown and hypomorphic alleles may produce subtle disease. Expressivity is clearly variable. Anticipation is not expected. Germline mosaicism has not been established as a characteristic mechanism but cannot be excluded for an apparently de novo parental allele. Consanguinity increases the probability that both partners carry the same rare allele. No validated human founder mutation, carrier frequency, ethnic enrichment, geographic endemicity, or incidence rate is available.

Prevalence is estimated at **<1:1,000,000**. The 2016 synthesis contained 15 molecularly proven patients from 14 families; the 2024 review continued to emphasize only 15 reported childhood cases and extremely limited adult observation. This is a literature count rather than incidence surveillance. (dijk2024clinicaldiagnosisof pages 3-4, damme2016expandingtheclinical pages 7-8)

The 2016 cohort sex ratio was 11 male:4 female, but autosomal inheritance and extreme sample size provide no evidence of biological male predominance. Reported families span multiple ancestries and regions; dEDS should not be considered ethnicity-specific. (damme2016expandingtheclinical pages 7-8)

## 10. Diagnostics

### Clinical recognition and criteria

The 2017 framework uses nine major criteria; a 2024 expert review considered the most discriminating combination to be: (1) extreme skin fragility with congenital or postnatal tears, (2) characteristic craniofacial appearance, (3) redundant/lax skin with wrist and ankle folds, and (4) severe bruising with subcutaneous hematoma/hemorrhage risk. Molecular confirmation is essential because milder dEDS can resemble classical EDS. (dijk2024clinicaldiagnosisof pages 3-4)

The 2016 proposed clinical criteria comprised severe skin fragility; sagging/redundant skin; easy bruising; characteristic congenital or progressive facial gestalt with periorbital swelling, blue sclerae, downslanting palpebral fissures, epicanthi, micrognathia, delayed fontanel closure, and dental anomalies; postnatal growth restriction; short extremities; joint hypermobility; umbilical hernia; and congenital/postnatal visceral or vascular fragility. (damme2016expandingtheclinical pages 7-8)

### Recommended genetic testing

1. Obtain detailed personal, pregnancy/birth, wound, bleeding, surgical, and three-generation family histories plus examination documenting skin fragility, scars, bruising, redundant skin, craniofacial findings, hernia, hypermobility, growth, eyes, teeth, and prolapse.
2. Use a **massively parallel inherited-connective-tissue/monogenic-EDS panel** including ADAMTS2. A 2024 review calls panel testing the current gold standard for monogenic EDS confirmation. Extreme skin fragility specifically prioritizes ADAMTS2. (zschocke2024geneticdiagnosisof pages 8-9)
3. Include full coding/splice-region sequencing and deletion/duplication analysis; phase two variants and perform parental segregation.
4. If panel/exome sequencing is negative despite strong suspicion, consider genome sequencing, analysis of deep intronic/promoter/regulatory regions, RNA sequencing/transcript studies, and reanalysis. Standard exome calling can miss copy-number, intronic, or structurally complex variants. (zschocke2024geneticdiagnosisof pages 8-9)
5. WES or WGS is useful where phenotype overlaps classical EDS, cutis laxa, osteogenesis imperfecta, brittle-cornea syndrome, or skeletal dysplasia. WGS offers better noncoding and structural-variant coverage but does not automatically resolve VUS.
6. CMA, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion assays are not first-line for isolated typical dEDS because it is a sequence-level single-gene disorder.

### Functional and pathology tests

- **Skin-biopsy TEM:** irregular, branched, ribbon-like or hieroglyphic collagen fibrils support the diagnosis, but mild cases may lack the classic severe pattern; a normal/nonspecific biopsy therefore does not exclude dEDS. (damme2016expandingtheclinical pages 5-7, damme2016expandingtheclinical pages 7-8)
- **Cultured fibroblast procollagen analysis:** accumulation of pN-collagen chains and deficient mature processing can demonstrate ADAMTS-2 dysfunction. (damme2016expandingtheclinical pages 5-7)
- **RNA studies/qPCR:** useful for splice variants and suspected nonsense-mediated decay. (damme2016expandingtheclinical pages 7-8)
- **Routine hemostasis:** CBC, PT/aPTT, coagulation factors, and thromboelastometry may be normal despite bruising or bleeding; no validated circulating biomarker exists. (balagopal2026exploringthehemorrhagic pages 1-4)
- **Imaging:** targeted echocardiography, ophthalmic assessment, skeletal imaging, ultrasound/CT/MRI, or organ imaging is driven by manifestations; no diagnostic imaging signature exists.

### Differential diagnosis

Important alternatives include classical EDS (COL5A1/COL5A2), classical-like EDS (TNXB/AEBP1), arthrochalasia EDS (COL1A1/COL1A2 exon-6-related), vascular EDS (COL3A1), kyphoscoliotic EDS (PLOD1/FKBP14), brittle-cornea syndrome (ZNF469/PRDM5), musculocontractural EDS (CHST14/DSE), periodontal EDS (C1R/C1S), osteogenesis imperfecta/COL1 overlap disorders, cutis laxa syndromes, and nonaccidental injury when unexplained bruises or tears occur. dEDS is favored by extreme congenital/postnatal skin fragility, redundant wrist/ankle skin, characteristic face, blue sclerae, short plump extremities, umbilical hernia, and biallelic ADAMTS2 variants.

### Screening

There is no population or newborn screening program. Appropriate strategies are **cascade testing** for adult relatives, targeted familial-variant prenatal testing, and preimplantation genetic testing after molecular confirmation. Carrier screening is reasonable in known families or partners from a high-consanguinity pedigree but is not part of universal screening.

## 11. Outcome and prognosis

No reliable 5-year/10-year survival, life expectancy, mortality rate, disability-adjusted burden, prognostic score, or biomarker has been published. Outcomes range from fatal neonatal hemorrhage to survival into adulthood. In the historic 15-person dataset, one infant died shortly after birth from severe hemorrhage/shock, while only two had follow-up into puberty/adulthood; the 2024 review cited one individual followed to age 19. (dijk2024clinicaldiagnosisof pages 3-4, damme2016expandingtheclinical pages 7-8)

Major morbidity arises from recurrent skin/mucosal wounds, scars, bruising and hematomas, bleeding, hernias, prolapse, pain, fatigue, growth and motor delay, ocular/dental complications, and visceral rupture. Recovery from individual injuries is possible, but healing may be slow and structurally fragile tissue persists. Prognosis is plausibly worse with complete enzyme loss, congenital hemorrhage, major organ fragility, or recurrent traumatic exposure; this remains unvalidated in humans.

The absence of large adult cohorts is a major knowledge gap. Normal coagulation results do not imply low hemorrhagic risk, and mild childhood skin ultrastructure does not guarantee benign long-term disease. (balagopal2026exploringthehemorrhagic pages 1-4, damme2016expandingtheclinical pages 7-8)

## 12. Treatment and current applications

### Disease-modifying therapy

There is **no approved dEDS-specific drug, enzyme replacement, gene therapy, cell therapy, RNA therapy, CRISPR treatment, or validated targeted therapy**. The ClinicalTrials.gov search returned no relevant dEDS interventional trial. No treatment-response rates or pharmacogenomic recommendations exist.

### Supportive management

Management is individualized and multidisciplinary, ideally involving clinical genetics, dermatology/wound care, pediatrics/internal medicine, physiotherapy/occupational therapy, pain medicine, ophthalmology, dentistry, gastroenterology/colorectal or urologic specialists, surgery/anesthesia, hematology for severe bleeding, and high-risk obstetrics where relevant.

Recommended practical measures, based on pathophysiology and rare-disease expert practice rather than trials, include:

- minimize friction, falls, contact sports, heavy collision activity, and unnecessary invasive procedures;
- use protective clothing/padding and adapt home/school/work environments;
- gentle wound handling, low-tension closure strategies, prolonged support, and specialist wound review;
- treat constipation, vomiting, and cough promptly to reduce mechanical stress;
- individualized low-impact strengthening/proprioceptive therapy while avoiding forceful manipulation and end-range loading;
- standard analgesia tailored to comorbidity and bleeding risk;
- regular dental and ophthalmic care;
- establish an emergency plan describing tissue and bleeding fragility;
- undertake surgery or endoscopy only when clinically justified, with experienced teams and anticipation of difficult hemostasis and poor wound healing. General EDS guidance advises reserving surgery for necessary complications because of wound risk. (balagopal2026exploringthehemorrhagic pages 6-7, islam2021ehlersdanlossyndromeimmunologic pages 1-8)

Ascorbic acid, zinc, desmopressin, or celiprolol have occasionally been discussed across EDS care, but dEDS-specific efficacy is unproven. Celiprolol evidence from vascular EDS must not be transferred to dEDS, and supplementation should not be presented as correction of ADAMTS-2 deficiency. A 2026 case used celiprolol and vitamin C, but one uncontrolled case cannot establish benefit. (balagopal2026exploringthehemorrhagic pages 1-4, balagopal2026exploringthehemorrhagic pages 6-7)

Suggested NCIT intervention concepts include **Genetic Counseling**, **Physical Therapy**, **Occupational Therapy**, **Wound Care**, **Pain Management**, **Surgical Procedure**, **Genetic Testing**, and **Supportive Care**; exact NCIT codes should be resolved against the current NCI Thesaurus release.

## 13. Prevention

**Primary prevention:** the phenotype cannot be prevented by vaccination, diet, or environmental modification after an affected genotype is present. Reproductive options include carrier testing, partner testing, preimplantation genetic testing, chorionic-villus/amniotic-fluid testing for known familial variants, donor gametes, and informed family planning.

**Secondary prevention:** early clinical recognition and molecular confirmation permit anticipatory guidance, cascade testing, protection from trauma, and targeted surveillance. There is no newborn biochemical screen.

**Tertiary prevention:** prevent tears, hematomas, hemorrhage, poor surgical outcomes, prolapse, and organ rupture through environmental adaptation, prompt wound care, constipation/vomiting control, cautious procedures, rehabilitation, and emergency planning. Standard immunizations remain appropriate but do not specifically alter dEDS; injection technique and post-injection pressure may need adaptation for bruising.

Genetic counseling should explain recessive recurrence risks, variable expressivity, limitations of prenatal phenotype prediction, and the possibility that a hypomorphic genotype may be milder but not harmless.

## 14. Other species and natural disease

Naturally occurring dermatosparaxis has been reported in cattle, sheep, cats, dogs, and other domestic species. The disease is homologous rather than infectious and has no zoonotic transmission. In the original bovine strain, a homozygous 17-bp ADAMTS2 deletion shifted the reading frame, while affected calf tissues accumulated incompletely processed procollagen and abnormal ribbon-like fibrils. (damme2016expandingtheclinical pages 1-2, colige1999humanehlersdanlossyndrome pages 1-2)

**Dog—Canis lupus familiaris, NCBI Taxon 9615.** A 2022 study identified homozygous ADAMTS2 variants in Pit Bull Terrier, Alapaha Blue Blood Bulldog, Catahoula Leopard Dog, and previously a Doberman Pinscher. Six dogs homozygous for c.10delC/p.(Pro4ArgfsTer175) had wounds, scars, hyperextensible skin, joint hypermobility and swelling; all were euthanized before 13 weeks. Dermal fibrils in two had hieroglyphic cross-sections. By contrast, a p.(Arg966His) Catahoula survived at least nine years. (jaffey2022novelhomozygousadamts2 pages 10-11, jaffey2022novelhomozygousadamts2 pages 1-2)

Among 167 sampled Alapaha Blue Blood Bulldogs selected for carrying at least one likely causal allele, the c.10delC allele frequency was 0.27; because sampling was enriched, this is not a breed-population carrier estimate. In a collection of 26 canine EDS whole genomes, only four had likely causal homozygous ADAMTS2 variants, emphasizing genetic heterogeneity in canine EDS. (jaffey2022novelhomozygousadamts2 pages 10-11, jaffey2022novelhomozygousadamts2 pages 14-15)

Veterinary relevance includes early recognition, avoidance of repeated injury, molecular subclassification, responsible breeding, and carrier testing within affected lineages. Suggested breed concepts require current VBO lookup; the source literature names the breeds but does not provide VBO identifiers.

Comparative pathology is highly conserved: recessive ADAMTS2 deficiency, retained procollagen propeptides, abnormal dermal fibrils, skin hyperextensibility/fragility, wounds, and joint laxity parallel the human condition. Species and genotype differences in survival and extracutaneous disease limit direct prognosis extrapolation.

## 15. Model organisms and experimental systems

### Adamts2-null mouse

The principal engineered mammalian model is the **Adamts2 knockout mouse**. It reproduces deficient fibrillar-procollagen processing and abnormal dermal fibrils/skin fragility, while enabling tissue-specific mechanistic study. Mouse work demonstrated that Adamts2 is a major procollagen-III N-proteinase; mutant tissues showed markedly reduced type III processing. Mutant lungs had enlarged distal airspaces and reduced parenchymal density without inflammation or overt fibrosis, whereas two-month-old aortic histology and fibril ultrastructure appeared normal despite impaired collagen I/III processing. (goff2006regulationofprocollagen pages 1-2, goff2006regulationofprocollagen pages 7-8)

The model’s major application is resolving protease redundancy: Adamts3 co-expression with Col2a1 in cartilage and Col1a1 in bone/musculotendinous tissue, plus in-vitro rescue of procollagen-I processing, supports compensation outside skin; Adamts14 co-expression in mature dermis may account for residual processing. (goff2006regulationofprocollagen pages 1-2, goff2006regulationofprocollagen pages 7-8)

**Limitations:** mouse tissue compensation differs from humans; severe human craniofacial, hemorrhagic, hernia, growth, and visceral manifestations are not comprehensively reproduced; normal young-mouse aortic structure does not exclude later or stress-dependent vascular disease.

### Natural and cellular models

Dermatosparactic cattle and dogs provide large-animal natural models with striking collagen ultrastructure and mechanical fragility. Dogs offer genotype-severity contrasts and clinically realistic wound burden, but euthanasia and breed structure complicate natural-history inference. Patient-derived dermal fibroblasts are useful for transcript analysis, procollagen-processing assays, TEM correlation, splice validation, and candidate rescue studies. ADAMTS3-mediated rescue of procollagen-I processing is a proof-of-mechanism in-vitro result, not a therapy. (goff2006regulationofprocollagen pages 1-2, damme2016expandingtheclinical pages 5-7)

No validated zebrafish, Drosophila, C. elegans, yeast, human organoid, or iPSC disease model was identified in the retrieved evidence. Relevant resources for model registration include MGI/IMSR for mice and OMIA for natural veterinary disease.

## Recent developments, expert interpretation, and research priorities

The important 2024 development was refinement of clinical and molecular diagnosis. Experts emphasized that monogenic EDS should be confirmed by phenotype-directed massively parallel panel testing, that extreme skin fragility prioritizes ADAMTS2, and that negative exome testing may warrant copy-number, noncoding, genome, or transcript analysis. They also warned against overinterpreting VUS. (zschocke2024geneticdiagnosisof pages 2-3, zschocke2024geneticdiagnosisof pages 8-9)

The central expert interpretation is that dEDS severity cannot be inferred solely from the presence of biallelic variants. Residual function, variant position, nonsense-mediated decay, and tissue-specific ADAMTS3/14 compensation probably shape phenotype; however, this model is supported much more strongly by fibroblast, mouse, and canine evidence than by adequately powered human genotype–phenotype studies. (jaffey2022novelhomozygousadamts2 pages 1-2, goff2006regulationofprocollagen pages 1-2, goff2006regulationofprocollagen pages 7-8, damme2016expandingtheclinical pages 7-8)

Highest-priority research needs are: an international longitudinal registry; systematic adult natural history; prospective hemorrhage, vascular, pulmonary, pregnancy, surgical, and quality-of-life outcomes; current ClinVar/gnomAD curation and functional classification of missense/splice variants; standardized procollagen biomarkers; patient-derived iPSC/3D-skin models; and preclinical testing of ADAMTS2 replacement or gene restoration.

## Key sources, publication dates, URLs, and quotations

1. **van Dijk et al., “Clinical diagnosis of the monogenic Ehlers-Danlos syndromes,” November 2024.** DOI/URL: https://doi.org/10.1515/medgen-2024-2060. It reports dEDS prevalence below 1:1,000,000 and stresses extreme skin fragility, characteristic craniofacial findings, redundant wrist/ankle skin, and severe bruising. (dijk2024clinicaldiagnosisof pages 3-4)
2. **Zschocke et al., “Genetic diagnosis of the Ehlers-Danlos syndromes,” November 2024.** DOI/URL: https://doi.org/10.1515/medgen-2024-2061. Abstract quotation: “Gene panel testing with massively parallel sequencing is currently gold standard to confirm diagnoses of the monogenic EDS types.” (zschocke2024geneticdiagnosisof pages 2-3, zschocke2024geneticdiagnosisof pages 8-9)
3. **Van Damme et al., “Expanding the clinical and mutational spectrum…,” online January 14, 2016; print September 2016.** DOI/URL: https://doi.org/10.1038/gim.2015.188. This primary human study added five patients, bringing the molecularly confirmed total to 15, and directly demonstrated reduced transcript, abnormal procollagen processing, and collagen-fibril defects. (damme2016expandingtheclinical pages 1-2, damme2016expandingtheclinical pages 2-3, damme2016expandingtheclinical pages 5-7, damme2016expandingtheclinical pages 7-8)
4. **Colige et al., “Human Ehlers-Danlos syndrome type VII C and bovine dermatosparaxis…,” electronically published June 23, 1999.** DOI/URL: https://doi.org/10.1086/302504. Abstract quotation: “These data provide direct evidence that EDS type VIIC and dermatosparaxis result from mutations in the pNPI gene.” PMID was not present in the retrieved full text. (colige1999humanehlersdanlossyndrome pages 1-2)
5. **Le Goff et al., “Regulation of procollagen amino-propeptide processing…,” April 2006.** DOI/URL: https://doi.org/10.1242/dev.02308. Abstract quotation: “Not all collagen-rich tissues are affected to the same degree, which suggests compensation by the ADAMTS2 homologs ADAMTS3 and ADAMTS14.” (goff2006regulationofprocollagen pages 1-2)
6. **Jaffey et al., “Novel Homozygous ADAMTS2 Variants…in Dogs,” published November 19, 2022.** DOI/URL: https://doi.org/10.3390/genes13112158. Abstract quotation: “Due to severe skin fragility, the owners of all 6 dogs elected euthanasia before the dogs reached 13 weeks of age.” (jaffey2022novelhomozygousadamts2 pages 1-2)

PMIDs were not exposed in the retrieved full-text records and are therefore not guessed. DOI URLs above provide stable primary-source links.

References

1. (dijk2024clinicaldiagnosisof pages 3-4): Fleur S. van Dijk, Chloe Angwin, Serwet Demirdas, Neeti Ghali, and Johannes Zschocke. Clinical diagnosis of the monogenic ehlers-danlos syndromes. Medizinische Genetik, 36:225-234, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2060, doi:10.1515/medgen-2024-2060. This article has 4 citations.

2. (zschocke2024geneticdiagnosisof pages 8-9): Johannes Zschocke, Serwet Demirdas, and Fleur S. van Dijk. Genetic diagnosis of the ehlers-danlos syndromes. Medizinische Genetik, 36:235-245, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2061, doi:10.1515/medgen-2024-2061. This article has 7 citations.

3. (kapfererseebacher2020dentalmanifestationsof pages 1-2): I. Kapferer-Seebacher, D. Schnabl, J. Zschocke, and F. Pope. Dental manifestations of ehlers-danlos syndromes: a systematic review. Acta Dermato-Venereologica, 100:adv00092-160, Mar 2020. URL: https://doi.org/10.2340/00015555-3428, doi:10.2340/00015555-3428. This article has 48 citations and is from a domain leading peer-reviewed journal.

4. (malek2021theroleof pages 2-3): Sabeeha Malek and Darius V. Köster. The role of cell adhesion and cytoskeleton dynamics in the pathogenesis of the ehlers-danlos syndromes and hypermobility spectrum disorders. Frontiers in Cell and Developmental Biology, Apr 2021. URL: https://doi.org/10.3389/fcell.2021.649082, doi:10.3389/fcell.2021.649082. This article has 27 citations.

5. (colige1999humanehlersdanlossyndrome pages 1-2): Alain Colige, Aleksander L. Sieron, Shi-Wu Li, Ulrike Schwarze, Elizabeth Petty, Wladimir Wertelecki, William Wilcox, Deborah Krakow, Daniel H. Cohn, W. Reardon, Peter H. Byers, Charles M. Lapière, Darwin J. Prockop, and Betty V. Nusgens. Human ehlers-danlos syndrome type vii c and bovine dermatosparaxis are caused by mutations in the procollagen i n-proteinase gene. American journal of human genetics, 65 2:308-17, Aug 1999. URL: https://doi.org/10.1086/302504, doi:10.1086/302504. This article has 482 citations and is from a highest quality peer-reviewed journal.

6. (neto2024unravelingthegenetic pages 5-6): Nilton Salles Rosa Neto, Ivânio Alves Pereira, Flávio Roberto Sztajnbok, and Valderílio Feijó Azevedo. Unraveling the genetic collagen connection: clinical and therapeutic insights on genetic connective tissue disorders. Advances in Rheumatology, Apr 2024. URL: https://doi.org/10.1186/s42358-024-00373-z, doi:10.1186/s42358-024-00373-z. This article has 11 citations.

7. (damme2016expandingtheclinical pages 2-3): Tim Van Damme, Alain Colige, Delfien Syx, Cecilia Giunta, Uschi Lindert, Marianne Rohrbach, Omid Aryani, Yasemin Alanay, Pelin Özlem Simsek-Kiper, Hester Y. Kroes, Koen Devriendt, Marc Thiry, Sofie Symoens, Anne De Paepe, and Fransiska Malfait. Expanding the clinical and mutational spectrum of the ehlers–danlos syndrome, dermatosparaxis type. Sep 2016. URL: https://doi.org/10.1038/gim.2015.188, doi:10.1038/gim.2015.188. This article has 68 citations and is from a highest quality peer-reviewed journal.

8. (damme2016expandingtheclinical pages 7-8): Tim Van Damme, Alain Colige, Delfien Syx, Cecilia Giunta, Uschi Lindert, Marianne Rohrbach, Omid Aryani, Yasemin Alanay, Pelin Özlem Simsek-Kiper, Hester Y. Kroes, Koen Devriendt, Marc Thiry, Sofie Symoens, Anne De Paepe, and Fransiska Malfait. Expanding the clinical and mutational spectrum of the ehlers–danlos syndrome, dermatosparaxis type. Sep 2016. URL: https://doi.org/10.1038/gim.2015.188, doi:10.1038/gim.2015.188. This article has 68 citations and is from a highest quality peer-reviewed journal.

9. (damme2016expandingtheclinical pages 1-2): Tim Van Damme, Alain Colige, Delfien Syx, Cecilia Giunta, Uschi Lindert, Marianne Rohrbach, Omid Aryani, Yasemin Alanay, Pelin Özlem Simsek-Kiper, Hester Y. Kroes, Koen Devriendt, Marc Thiry, Sofie Symoens, Anne De Paepe, and Fransiska Malfait. Expanding the clinical and mutational spectrum of the ehlers–danlos syndrome, dermatosparaxis type. Sep 2016. URL: https://doi.org/10.1038/gim.2015.188, doi:10.1038/gim.2015.188. This article has 68 citations and is from a highest quality peer-reviewed journal.

10. (damme2016expandingtheclinical pages 5-7): Tim Van Damme, Alain Colige, Delfien Syx, Cecilia Giunta, Uschi Lindert, Marianne Rohrbach, Omid Aryani, Yasemin Alanay, Pelin Özlem Simsek-Kiper, Hester Y. Kroes, Koen Devriendt, Marc Thiry, Sofie Symoens, Anne De Paepe, and Fransiska Malfait. Expanding the clinical and mutational spectrum of the ehlers–danlos syndrome, dermatosparaxis type. Sep 2016. URL: https://doi.org/10.1038/gim.2015.188, doi:10.1038/gim.2015.188. This article has 68 citations and is from a highest quality peer-reviewed journal.

11. (goff2006regulationofprocollagen pages 1-2): Carine Le Goff, Robert P. T. Somerville, Frederic Kesteloot, Kimerly Powell, David E. Birk, Alain C. Colige, and Suneel S. Apte. Regulation of procollagen amino-propeptide processing during mouse embryogenesis by specialization of homologous adamts proteases: insights on collagen biosynthesis and dermatosparaxis. Development, 133(8):1587-1596, Apr 2006. URL: https://doi.org/10.1242/dev.02308, doi:10.1242/dev.02308. This article has 142 citations and is from a domain leading peer-reviewed journal.

12. (goff2006regulationofprocollagen pages 7-8): Carine Le Goff, Robert P. T. Somerville, Frederic Kesteloot, Kimerly Powell, David E. Birk, Alain C. Colige, and Suneel S. Apte. Regulation of procollagen amino-propeptide processing during mouse embryogenesis by specialization of homologous adamts proteases: insights on collagen biosynthesis and dermatosparaxis. Development, 133(8):1587-1596, Apr 2006. URL: https://doi.org/10.1242/dev.02308, doi:10.1242/dev.02308. This article has 142 citations and is from a domain leading peer-reviewed journal.

13. (damme2016expandingtheclinical pages 3-5): Tim Van Damme, Alain Colige, Delfien Syx, Cecilia Giunta, Uschi Lindert, Marianne Rohrbach, Omid Aryani, Yasemin Alanay, Pelin Özlem Simsek-Kiper, Hester Y. Kroes, Koen Devriendt, Marc Thiry, Sofie Symoens, Anne De Paepe, and Fransiska Malfait. Expanding the clinical and mutational spectrum of the ehlers–danlos syndrome, dermatosparaxis type. Sep 2016. URL: https://doi.org/10.1038/gim.2015.188, doi:10.1038/gim.2015.188. This article has 68 citations and is from a highest quality peer-reviewed journal.

14. (balagopal2026exploringthehemorrhagic pages 1-4): Akshaya Kumar Balagopal, Santhi T S, Ashokraj Selvam, and Vimalraj Vijayakumar. Exploring the hemorrhagic manifestations of an adolescent with dermatosparaxis-type ehlers-danlos syndrome: a case report. Cureus, May 2026. URL: https://doi.org/10.7759/cureus.108459, doi:10.7759/cureus.108459. This article has 0 citations.

15. (zschocke2024geneticdiagnosisof pages 2-3): Johannes Zschocke, Serwet Demirdas, and Fleur S. van Dijk. Genetic diagnosis of the ehlers-danlos syndromes. Medizinische Genetik, 36:235-245, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2061, doi:10.1515/medgen-2024-2061. This article has 7 citations.

16. (jaffey2022novelhomozygousadamts2 pages 1-2): Jared A. Jaffey, Garrett Bullock, Juyuan Guo, Tendai Mhlanga-Mutangadura, Dennis P. O’Brien, Joan R. Coates, Rochelle Morrissey, Robert Hutchison, Kevin S. Donnelly, Leah A. Cohn, Martin L. Katz, and Gary S. Johnson. Novel homozygous adamts2 variants and associated disease phenotypes in dogs with dermatosparactic ehlers–danlos syndrome. Nov 2022. URL: https://doi.org/10.3390/genes13112158, doi:10.3390/genes13112158. This article has 16 citations.

17. (jaffey2022novelhomozygousadamts2 pages 14-15): Jared A. Jaffey, Garrett Bullock, Juyuan Guo, Tendai Mhlanga-Mutangadura, Dennis P. O’Brien, Joan R. Coates, Rochelle Morrissey, Robert Hutchison, Kevin S. Donnelly, Leah A. Cohn, Martin L. Katz, and Gary S. Johnson. Novel homozygous adamts2 variants and associated disease phenotypes in dogs with dermatosparactic ehlers–danlos syndrome. Nov 2022. URL: https://doi.org/10.3390/genes13112158, doi:10.3390/genes13112158. This article has 16 citations.

18. (balagopal2026exploringthehemorrhagic pages 6-7): Akshaya Kumar Balagopal, Santhi T S, Ashokraj Selvam, and Vimalraj Vijayakumar. Exploring the hemorrhagic manifestations of an adolescent with dermatosparaxis-type ehlers-danlos syndrome: a case report. Cureus, May 2026. URL: https://doi.org/10.7759/cureus.108459, doi:10.7759/cureus.108459. This article has 0 citations.

19. (islam2021ehlersdanlossyndromeimmunologic pages 1-8): Mareesa Islam, Christopher Chang, and M. Eric Gershwin. Ehlers-danlos syndrome: immunologic contrasts and connective tissue comparisons. Jan 2021. URL: https://doi.org/10.1016/j.jtauto.2020.100077, doi:10.1016/j.jtauto.2020.100077. This article has 40 citations and is from a peer-reviewed journal.

20. (jaffey2022novelhomozygousadamts2 pages 10-11): Jared A. Jaffey, Garrett Bullock, Juyuan Guo, Tendai Mhlanga-Mutangadura, Dennis P. O’Brien, Joan R. Coates, Rochelle Morrissey, Robert Hutchison, Kevin S. Donnelly, Leah A. Cohn, Martin L. Katz, and Gary S. Johnson. Novel homozygous adamts2 variants and associated disease phenotypes in dogs with dermatosparactic ehlers–danlos syndrome. Nov 2022. URL: https://doi.org/10.3390/genes13112158, doi:10.3390/genes13112158. This article has 16 citations.

## Artifacts

- [Edison artifact artifact-00](Dermatosparaxis_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
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
| Terms whose name was checked | 16 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009161` (2 mentions) - the report calls it "if available"; MONDO calls it **Ehlers-Danlos syndrome, dermatosparaxis type**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0062023` (obsolete collagen-containing extracellular matrix) (1 mention) - replaced by `GO:0031012`