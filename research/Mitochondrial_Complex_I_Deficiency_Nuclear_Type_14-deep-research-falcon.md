---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T12:48:01.825023'
end_time: '2026-09-02T12:59:15.882379'
duration_seconds: 674.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mitochondrial Complex I Deficiency, Nuclear Type 14
  mondo_id: MONDO:0032619
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 43
  verified: 42
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032619
    reported_labels:
    - if available
    ontology_label: mitochondrial complex I deficiency, nuclear type 14
  obsolete_terms:
  - term_id: GO:0005747
    ontology_label: obsolete mitochondrial respiratory chain complex I
    replaced_by: GO:0045271
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_14-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 14
- **MONDO ID:** MONDO:0032619 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 14** covering all of the
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
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 14
- **MONDO ID:** MONDO:0032619 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 14** covering all of the
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


# Mitochondrial Complex I Deficiency, Nuclear Type 14

## Executive summary and evidence limits

Mitochondrial complex I deficiency, nuclear type 14 (MC1DN14) is an ultra-rare, autosomal-recessive oxidative-phosphorylation disorder caused by biallelic pathogenic variants in **NDUFA11**, which encodes an accessory membrane-arm subunit of respiratory-chain complex I. The strongest disease-specific evidence remains the 2008 report of six affected individuals from three consanguineous families carrying the same homozygous splice variant. That cohort demonstrated a spectrum from fatal neonatal lactic acidemia to infantile encephalocardiomyopathy. Later literature recognizes NDUFA11-associated late-onset myopathy, but detailed primary data from that report were not retrievable in this search and should not be merged quantitatively with the six foundational cases. Open Targets links MONDO:0032619 exclusively to NDUFA11 and cites PMID **18306244** as the principal human evidence. No disease-specific prevalence study, natural-history registry, validated outcome measure, clinical trial, or approved targeted treatment was found. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 14, berger2008mitochondrialcomplexi pages 1-2)

| Domain | Disease-specific finding | Quantitative evidence | Evidence type/source |
|---|---|---|---|
| Identity | Mitochondrial complex I deficiency, nuclear type 14; **MONDO:0032619**, **OMIM 618236** | One established disease-associated target: **NDUFA11** | Aggregated disease/target database and review (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 14, fernandez‐vizarra2021mitochondrialdisordersof pages 96-99) |
| Causal gene | **NDUFA11**, encoding an accessory membrane-arm subunit of mitochondrial complex I at the complex I–III respirasome interface | Six molecularly confirmed patients in the foundational report | Human genetic cases plus structural/model evidence (berger2008mitochondrialcomplexi pages 1-2, knappwilson2021maintenanceofcomplex pages 2-3) |
| Inheritance and variant | Autosomal recessive; all foundational patients were homozygous for the leaky splice variant **IVS1+5G>A** in legacy notation | Six patients from three unrelated consanguineous families; no carriers among 52 ancestry-matched controls | Human segregation, homozygosity mapping, and RNA analysis (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 1-2) |
| Molecular consequence | Aberrant splicing activates a cryptic site within exon 1, deleting 78 bp and predicting loss of the first transmembrane domain; residual normal transcript may explain variable severity | Fibroblast wild-type:mutant transcript ratio approximately **2:1** | Human fibroblast RT-PCR/qPCR and in-silico topology analysis (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 3-4) |
| Neonatal-lethal cluster | Term infants initially appeared normal, then developed apnea, hypotension, severe lactic acidosis, and subsequent biventricular hypertrophy | Onset **10–24 h**; pH **6.80–6.90**; lactate **10–15 mM**; death at **6–40 days** | Human clinical case series (berger2008mitochondrialcomplexi pages 1-2) |
| Encephalocardiomyopathy cluster | Slow psychomotor development, acquired microcephaly, profound hypotonia and weakness, absent major motor milestones, visual impairment, brain atrophy, cardiomyopathy, and occasional seizures | Three patients; lactate **3.2–10 mM**; cardiac changes at **3–4 months**; two deaths at **18 months** and **4 years** during infection | Human clinical case series (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 1-2) |
| Biochemical defect | Isolated complex I deficiency; activities of the other respiratory-chain complexes were within reference ranges | Muscle complex I assays: **4–10%**, **13–27%**, and **19–39%** of control means, depending on assay; fibroblast NADH:ubiquinone reductase **45%** of control | Human muscle and fibroblast spectrophotometric assays (berger2008mitochondrialcomplexi pages 2-3) |
| Mechanism | NDUFA11 disruption destabilizes complex I and its respiratory supercomplexes, impairing NADH oxidation, proton-motive-force generation, and ATP production; increased lactate and ROS-mediated injury are downstream consequences, with ROS partly model-inferred | NDUF-11-depleted worms showed approximately **83%** protein reduction and approximately **50%** reduction of other complex I subunits | Human biochemical evidence integrated with cardioblast and *C. elegans* studies (knappwilson2021maintenanceofcomplex pages 3-5, knappwilson2021maintenanceofcomplex pages 2-3, jang2018elucidatingthecontribution pages 1-2) |
| Experimental models | *C. elegans* CRISPR knockout causes L2 arrest; partial RNAi causes reduced growth/fecundity, complex I and supercomplex instability, altered respiration, excess ROS, and abnormal cristae. NDUFA11 siRNA in H9c2 cardioblasts disrupts respirasomes, lowers ATP, and increases mitochondrial ROS | Homozygous worm knockout: **L2 arrest**; RNAi: approximately **83%** depletion | Model-organism and in-vitro primary studies (knappwilson2021maintenanceofcomplex pages 1-2, knappwilson2021maintenanceofcomplex pages 2-3, jang2018elucidatingthecontribution pages 1-2) |
| Diagnosis | Confirmation requires compatible disease plus biallelic pathogenic or likely pathogenic **NDUFA11** variants; genome-wide nuclear testing should generally be paired with mtDNA analysis. Respiratory-chain assays, BN-PAGE, and RNA studies can resolve uncertain cases | Current guidance supports simultaneous mtDNA and nuclear-DNA testing where possible; urgent pediatric cases may undergo trio WES/WGS | Disease-specific inference plus 2023 mitochondrial-testing consensus (berger2008mitochondrialcomplexi pages 2-3, mavraki2023genetictestingfor pages 2-3, mavraki2023genetictestingfor pages 1-2) |
| Treatment and trials | No NDUFA11-specific disease-modifying therapy or genotype-specific clinical trial was identified; care is supportive and phenotype-directed. Evidence for empiric vitamins and cofactors in unselected primary mitochondrial disease is insufficient | **95% (106/112)** of surveyed specialists used vitamins/cofactors despite no clinical-trial evidence for these supplements alone or in combination | Trial search plus general mitochondrial-disease practice survey; not NDUFA11-specific (neugebauer2025currentglobalvitamin pages 1-2) |


*Table: Compact evidence table summarizing the identity, genetic cause, clinical clusters, biochemical defect, mechanism, models, diagnosis, and therapeutic gaps for mitochondrial complex I deficiency, nuclear type 14.*

## 1. Disease information

### Definition

MC1DN14 is a Mendelian mitochondrial disorder in which impaired NDUFA11 function destabilizes respiratory complex I and complex-I-containing supercomplexes. The resulting failure of NADH-linked oxidative phosphorylation primarily injures energy-dependent brain, skeletal muscle, and myocardium. The disease is defined molecularly rather than by one clinical syndrome because the same splice defect produced two markedly different clinical presentations in the original families. (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 1-2, berger2008mitochondrialcomplexi pages 3-4)

### Identifiers and synonyms

- **MONDO:** MONDO:0032619.
- **OMIM phenotype:** **618236**, mitochondrial complex I deficiency, nuclear type 14.
- **Causal-gene OMIM:** reviews list NDUFA11 as **612638**; one older review gives 612698, apparently an obsolete or erroneous entry that should not supersede the current gene record. (fernandez‐vizarra2021mitochondrialdisordersof pages 96-99, ugalde2009mitochondrialdisordersdue pages 4-6)
- **Gene:** **NDUFA11**, approved name *NADH:ubiquinone oxidoreductase subunit A11*; Ensembl ENSG00000174886. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 14)
- **Synonyms:** NDUFA11-related mitochondrial complex I deficiency; NDUFA11 deficiency; isolated complex I deficiency due to NDUFA11; NDUFA11-related encephalocardiomyopathy; NDUFA11-related fatal infantile lactic acidemia. “NDUFA11-related late-onset myopathy” describes the expanded allelic phenotype.
- **ICD-10/ICD-11 and MeSH:** no uniquely specific code was identified. In practice it falls under broader mitochondrial metabolism/respiratory-chain disease categories; a generic code should not be represented as disease-specific.
- **Orphanet:** no dedicated disease-specific ORPHA identifier was established from the retrieved evidence.

The core observations are **individual-patient clinical and laboratory data**, subsequently aggregated by OMIM/MONDO/Open Targets and reviews. They are not derived from EHR population surveillance. The foundational paper was received August 27, 2007, accepted November 29, 2007, published online February 27, 2008, and appeared in *Annals of Neurology* in March 2008; DOI: https://doi.org/10.1002/ana.21332; PMID: **18306244**. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 14, berger2008mitochondrialcomplexi pages 1-2)

**Exact abstract quote:** “Using homozygosity mapping, we identified a splice-site mutation in the NDUFA11 gene in six patients from three unrelated families.” The authors further stated that the patients “presented with encephalocardiomyopathy or fatal infantile lactic acidemia.” (berger2008mitochondrialcomplexi pages 1-2)

## 2. Etiology, risk, protection, and environment

The primary cause is **germline biallelic loss or severe reduction of NDUFA11 function**. The original patients were homozygous for a G-to-A substitution at the donor region of intron 1, reported in legacy nomenclature as **IVS1+5G>A**. A modern HGVS expression should be verified against the clinically used NDUFA11 transcript before database entry rather than inferred from legacy notation. The variant weakened normal splicing and activated a cryptic splice site at bases 19–20 of exon 1, producing a transcript missing the final 78 bp of exon 1. (berger2008mitochondrialcomplexi pages 2-3)

The demonstrated genetic risk factors are carrier parents, consanguinity, and shared ancestry. All three couples were first cousins. A shared chromosome-19 haplotype across 342 SNPs supported a founder allele, although the families reported no known relationship. No carriers were found among 52 ancestry-matched controls. No susceptibility loci, common polygenic factors, modifier genes, protective alleles, sex effect, anticipation, or germline mosaicism have been demonstrated. (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 1-2)

The different phenotypes produced by one allele led the investigators to suggest a modifier effect. A more immediate explanation is tissue-dependent residual splicing: patient fibroblasts retained normal transcript at an approximately **2:1 wild-type:aberrant-transcript ratio**, but this ratio may differ in brain, heart, and muscle. This is a plausible genotype–tissue interaction, not a proven modifier gene. (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 3-4)

No toxin, radiation, lifestyle factor, infectious agent, diet, smoking, alcohol, or occupational exposure is known to cause MC1DN14. Intercurrent infection is nevertheless an important **metabolic stressor**: acidosis worsened during infections, and two children died during such episodes. Infection therefore modifies expression and decompensation risk but is not the disease cause. No validated environmental or dietary protective factor exists. (berger2008mitochondrialcomplexi pages 2-3)

## 3. Phenotypes

The following frequencies refer only to the six 2008 cases and are vulnerable to ascertainment and familial clustering.

### Neonatal lethal metabolic presentation—3/6

Three term infants were initially unremarkable but developed apnea, hypotension, severe metabolic acidosis, and hyperlactatemia at **10–24 hours**. Blood pH was **6.80–6.90** and lactate **10–15 mmol/L**. Echocardiograms normal at birth showed biventricular myocardial hypertrophy during the second week. All died from intractable acidosis at **6–40 days**. Suggested HPO terms are neonatal onset (HP:0003623), lactic acidosis (HP:0003128), metabolic acidosis (HP:0001942), apnea (HP:0002104), hypotension (HP:0002615), hypertrophic cardiomyopathy (HP:0001639), and early death (HP:0003819). (berger2008mitochondrialcomplexi pages 1-2)

### Infantile encephalocardiomyopathy—3/6

Three Israeli-Bedouin children had slow early psychomotor development followed by acquired microcephaly, marked generalized hypotonia, muscle weakness, paucity of voluntary movement, and profound motor delay; none rolled or lifted the head when prone. Visual fixation was impaired, with nystagmus in one and bilateral optic atrophy in another. One developed seizures at four months. CT in two showed generalized cerebral atrophy. Plasma lactate was **3.2–10 mmol/L**. Cardiac hypertrophy with mild left-ventricular dilatation appeared at three to four months despite normal neonatal echocardiography. CBC, transaminases, CK, EEG, and hearing were normal in the reported assessments. Two died during infection at 18 months and four years; one was alive at six months when reported. (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 1-2)

Suggested HPO terms include global developmental delay (HP:0001263), acquired microcephaly (HP:0000252), generalized hypotonia (HP:0001290), muscle weakness (HP:0001324), severe motor delay (HP:0001270), decreased voluntary movements (HP:0002361), impaired visual fixation, nystagmus (HP:0000639), optic atrophy (HP:0000648), seizure (HP:0001250), cerebral atrophy (HP:0002059), hyperlactatemia (HP:0002151), hypertrophic cardiomyopathy (HP:0001639), and left-ventricular dilatation (HP:0005132).

The primary tissue injury produces severe dependence in mobility, feeding and caregiving and likely major family burden. However, no EQ-5D, SF-36, PROMIS, developmental-adaptive scale, or disease-specific quality-of-life data have been published for MC1DN14. A later NDUFA11 allelic phenotype of late-onset myopathy is cited by mechanistic reviews, but its exact onset, distribution, progression, biopsy findings, and frequency cannot be responsibly quantified from the available primary evidence. (fernandez‐vizarra2021mitochondrialdisordersof pages 96-99, knappwilson2021maintenanceofcomplex pages 2-3)

## 4. Genetic and molecular information

**NDUFA11** encodes a nuclear-encoded, integral inner-mitochondrial-membrane accessory subunit of complex I. It comprises four predicted transmembrane helices, lies in the membrane-arm/ND1-module region, binds cardiolipin, and occupies part of the interface between complex I and complex III in the respirasome. Suggested annotations include GO:0005743, mitochondrial inner membrane; GO:0005747, mitochondrial respiratory-chain complex I; GO:1990204, oxidoreductase complex; and GO:0098803, respiratory-chain complex. (fernandez‐vizarra2021mitochondrialdisordersof pages 96-99, knappwilson2021maintenanceofcomplex pages 1-2, knappwilson2021maintenanceofcomplex pages 2-3)

The foundational splice allele is germline, autosomal recessive, and functionally hypomorphic or “leaky.” All six available affected samples were homozygous; parents and five healthy siblings were heterozygous, while another healthy sibling carried two normal alleles. RT-PCR directly demonstrated both normal 484-bp and aberrant 406-bp transcripts. The aberrant product predicts loss of the first transmembrane domain and consequent complex destabilization. (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 3-4)

Population allele frequency in gnomAD/TOPMed, dbSNP identifier, current ClinVar ACMG classification, and exact transcript-specific HGVS nomenclature were not established from the retrieved documents. No somatic NDUFA11 mechanism is implicated. No pathogenic copy-number variant, aneuploidy, translocation, inversion, repeat expansion, epigenetic signature, or validated modifier gene has been reported for this disorder.

## 5. Environmental information

MC1DN14 is not an environmental, infectious, or lifestyle disease. Fever, fasting, dehydration, surgery, and infection are biologically credible stressors for mitochondrial energy failure; only infection-associated worsening and deaths are documented specifically in these patients. Avoiding prolonged fasting and rapidly treating intercurrent illness are therefore precautionary mitochondrial-care practices, not proven primary prevention. (berger2008mitochondrialcomplexi pages 2-3)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic NDUFA11 splice disruption leads to** reduced correctly spliced transcript and production of an aberrant transcript lacking 78 bp of exon 1. (Demonstrated in patient fibroblasts.)
2. **Aberrant transcript leads to** predicted loss of the first NDUFA11 transmembrane helix. (Computationally inferred, not directly demonstrated in patient tissue.)
3. **Reduced or structurally abnormal NDUFA11 leads to** impaired assembly/stability of complex I and the I–III–IV respirasome. (Supported by patient enzyme deficiency and directly demonstrated in cardioblast and worm models.)
4. **Complex-I loss leads to** deficient NADH oxidation, electron transfer to ubiquinone, and proton pumping across the inner mitochondrial membrane.
5. **Reduced proton motive force leads to** reduced oxidative ATP production and altered NADH/NAD⁺ redox balance. ATP reduction is demonstrated in NDUFA11-silenced cardioblasts; the patient-level ATP step is inferred.
6. **Impaired oxidative metabolism leads to** pyruvate diversion to lactate, producing hyperlactatemia and severe metabolic acidosis. (Clinically demonstrated.)
7. **A branch from electron-transfer/supercomplex instability leads to** increased mitochondrial ROS and abnormal cristae architecture. (Demonstrated in models; not directly measured in patients.)
8. **ATP insufficiency with probable redox/ROS stress leads to** dysfunction and injury in neurons, skeletal myofibers, cardiomyocytes, retinal ganglion/optic-nerve structures, and respiratory-control networks.
9. **High-energy tissue dysfunction results in** developmental encephalopathy, hypotonia and weakness, cerebral/optic atrophy, cardiomyopathy, apnea, seizures, and potentially fatal metabolic decompensation.

Human muscle showed isolated complex-I activities of **4–10%**, **13–27%**, and **19–39%** of control means across three NADH-linked assays. Patient fibroblast NADH:ubiquinone reductase activity was **45%** of control; other respiratory complexes remained within reference ranges. This tissue difference supports residual function and tissue-specific severity. (berger2008mitochondrialcomplexi pages 2-3)

NDUFA11 knockdown in H9c2 cardioblasts dissociated respirasomes, reduced activities of complexes I, III and IV, lowered ATP, and raised mitochondrial ROS. Structural work places NDUFA11 at stable complex-I/III contacts. These results support supercomplex destabilization but do not prove that every downstream abnormality in cardioblasts occurs in MC1DN14 patients. (jang2018elucidatingthecontribution pages 1-2)

In *C. elegans*, approximately 83% NDUF-11 depletion reduced other complex-I subunits by roughly 50%, destabilized active complex I and supercomplexes, altered respiration and metabolic pathways, and produced abnormal cristae and widened crista junctions/intermembrane space. Complete knockout caused L2 arrest. (knappwilson2021maintenanceofcomplex pages 3-5, knappwilson2021maintenanceofcomplex pages 1-2, knappwilson2021maintenanceofcomplex pages 2-3)

Suggested GO biological-process terms include mitochondrial respiratory-chain complex I assembly (GO:0032981), respiratory electron transport chain (GO:0022904), oxidative phosphorylation (GO:0006119), ATP synthesis coupled electron transport (GO:0042773), proton transmembrane transport (GO:1902600), NADH dehydrogenase activity-related processes, cellular response to oxidative stress (GO:0034599), mitochondrial organization (GO:0007005), and cristae formation/organization. Suggested cell types are neuron (CL:0000540), skeletal muscle cell/myocyte (CL:0000187), cardiomyocyte (CL:0000746), retinal ganglion cell (CL:0000740), and fibroblast (CL:0000057). No disease-specific single-cell, spatial-transcriptomic, lipidomic, epigenomic, or human multi-omic dataset was identified.

## 7. Anatomical structures affected

Primary organs are the **brain**, **skeletal muscle**, and **heart**; visual pathways/optic nerve are also involved. Suggested UBERON mappings include brain (UBERON:0000955), cerebral cortex (UBERON:0000956), skeletal muscle organ (UBERON:0001134), heart (UBERON:0000948), myocardium (UBERON:0002349), retina (UBERON:0000966), and optic nerve (UBERON:0000941). Relevant systems are nervous, neuromuscular, cardiovascular, metabolic, visual, and respiratory-control systems. (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 1-2)

At the subcellular level, the primary lesion is in complex I of the inner mitochondrial membrane; secondary abnormalities involve respiratory supercomplexes, cristae, intermembrane space, proton gradient, and mitochondrial matrix redox metabolism. Cardiac involvement was biventricular rather than lateralized, and cerebral atrophy was generalized. No consistent unilateral or asymmetric localization is reported. (knappwilson2021maintenanceofcomplex pages 1-2, knappwilson2021maintenanceofcomplex pages 2-3)

## 8. Temporal development

The severe form begins acutely within the first postnatal day and progresses over days to fatal acidosis. The encephalocardiomyopathic form has apparently normal neonatal examination followed by insidious developmental delay, progressive microcephaly, weakness and visual dysfunction; cardiomyopathy becomes evident within months. Infection can precipitate episodic worsening on a chronic progressive background. (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 1-2)

No formal stages exist. Useful operational stages are: presymptomatic neonatal period; metabolic/developmental presentation; multisystem progression; acute decompensation; and advanced cardiorespiratory or neurologic failure. The foundational survival range was six days to at least four years, but this is not a survival estimate. No spontaneous remission was reported. The neonatal period, infancy, intercurrent infection, fasting, and other catabolic states are likely critical vulnerability windows.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two heterozygous parents, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of an unaffected non-carrier, assuming classic Mendelian segregation. Apparent penetrance among confirmed biallelic family members was high, but the cohort is too small to estimate penetrance. Expressivity is markedly variable. There is no evidence of anticipation. (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 1-2)

The original families were consanguineous, including Israeli-Bedouin ancestry in family C, and shared a haplotype consistent with a founder mutation. Carrier frequency, sex ratio, ethnic prevalence, geographic distribution, incidence, and disease-specific prevalence remain unknown. General primary mitochondrial disease prevalence—approximately **1 in 4,300**—must not be presented as MC1DN14 prevalence. Current broad estimates are approximately 12.5/100,000 adults and 4.7/100,000 children. (neugebauer2025currentglobalvitamin pages 1-2, mancuso2024managementofseizures pages 1-2, mavraki2023genetictestingfor pages 1-2)

## 10. Diagnostics

### Recommended workflow

1. Suspect mitochondrial disease in neonatal lactic acidosis, unexplained encephalocardiomyopathy, profound hypotonia/developmental delay, optic atrophy, or mitochondrial myopathy.
2. Obtain blood gas, lactate, pyruvate where available, glucose, electrolytes, liver/renal indices, CK, CBC, amino acids, acylcarnitines and urine organic acids. Lactate is supportive but nonspecific.
3. Assess organ involvement with ECG/echocardiography, brain MRI (preferred over CT), ophthalmology, hearing, EEG if seizures, and nutritional/respiratory evaluation.
4. Use comprehensive NGS early. The 2023 UK best-practice guideline recommends simultaneous mtDNA and nuclear-DNA analysis where possible; urgent pediatric cases are appropriate for trio WES or WGS. NDUFA11 should be included in mitochondrial/complex-I panels. (mavraki2023genetictestingfor pages 2-3, mavraki2023genetictestingfor pages 1-2)
5. Confirm candidate variants by segregation and ACMG/AMP classification. For splice variants or VUS, perform RNA studies in fibroblasts or another informative tissue.
6. If genetics is negative or inconclusive, assess respiratory-chain enzymes in muscle or fibroblasts, and consider blue-native PAGE/complexome analysis. Muscle complex-I deficiency may be substantially more severe than fibroblast deficiency. (berger2008mitochondrialcomplexi pages 2-3, scheffler2015mitochondrialdiseaseassociated pages 18-21)

CMA, karyotyping and FISH are not first-line for a single-gene phenotype unless a chromosomal disorder is suspected. Repeat-expansion testing is not relevant. mtDNA analysis remains appropriate because clinical complex-I deficiency can arise from mtDNA variants, but MC1DN14 itself is nuclear and autosomal recessive. The diagnostic field has shifted from “biopsy first” toward genome-wide blood/urine analyses, reserving biopsy for unresolved cases. (mavraki2023genetictestingfor pages 2-3, mavraki2023genetictestingfor pages 1-2)

Differential diagnoses include other nuclear complex-I deficiencies, mtDNA complex-I disorders, pyruvate dehydrogenase deficiency, organic acidemias, fatty-acid oxidation disorders, other causes of Leigh/Leigh-like disease, congenital cardiomyopathy, neuromuscular disorders, and sepsis in a decompensating neonate. Isolated severe complex-I loss plus biallelic NDUFA11 variants distinguishes MC1DN14.

There is no routine newborn screening. Population DNA-first screening is not currently justified because disease-specific treatment, prevalence, variant spectrum, and test-performance data are insufficient. Cascade carrier testing is appropriate after a familial diagnosis.

## 11. Outcome and prognosis

The neonatal metabolic phenotype has a grave prognosis: all three foundational neonates died by 40 days. In the encephalocardiomyopathy group, two of three died at 18 months and four years during infections; the third was only six months old at last report. These data show high early mortality for that splice allele but cannot yield five- or ten-year survival rates or generalize to hypomorphic missense alleles associated with adult myopathy. (berger2008mitochondrialcomplexi pages 2-3, berger2008mitochondrialcomplexi pages 1-2)

Major morbidity includes profound developmental disability, loss or failure of motor milestones, weakness, visual impairment, epilepsy, cardiomyopathy, recurrent metabolic crises, and complete caregiving dependence. Poor prognostic indicators likely include neonatal onset, extreme acidosis, very low muscle complex-I activity, early cardiomyopathy, and recurrent infection-triggered decompensation; none has been validated in a disease-specific prognostic model. No disease-specific FGF21, GDF15, neurofilament-light, imaging, or molecular prognostic biomarker has been validated.

## 12. Treatment

No NDUFA11-specific disease-modifying therapy, gene therapy, RNA therapy, cell therapy, editing strategy, approved drug, or registered genotype-specific clinical trial was identified. Management is multidisciplinary and supportive:

- acute metabolic stabilization with careful airway, ventilation, circulation, glucose and electrolyte management; avoid prolonged fasting and promptly treat infection;
- serial cardiology surveillance and guideline-based treatment of cardiomyopathy/heart failure;
- seizure treatment following standard epilepsy guidance, modified for mitochondrial safety;
- nutritional, swallowing and respiratory assessment; enteral support where needed;
- physical, occupational, speech/communication, visual and developmental therapies;
- ophthalmology, audiology, neurology, metabolic medicine and palliative-care involvement according to severity.

A 2024 Delphi consensus involving 24 experts endorsed standard seizure guidance with specific mitochondrial exceptions, especially avoiding valproate in **POLG** disease; that contraindication is not NDUFA11-specific. (mancuso2024managementofseizures pages 1-2)

CoQ10, riboflavin, thiamine, biotin, niacin, lipoic acid, carnitine, creatine and antioxidants are often included in empiric “mitochondrial cocktails,” but no controlled evidence demonstrates benefit in MC1DN14. A global specialist survey found **95% (106/112)** prescribed vitamins or cofactors, while explicitly noting no clinical-trial evidence for these supplements alone or in combination in unselected primary mitochondrial disease. (neugebauer2025currentglobalvitamin pages 1-2)

Possible NCIt intervention mappings include genetic counseling, whole-exome sequencing, whole-genome sequencing, physical therapy, occupational therapy, speech therapy, nutritional support, anticonvulsant therapy, cardiac monitoring and palliative care. These are supportive interventions, not curative NDUFA11 therapies.

## 13. Prevention

The genetic lesion cannot be prevented through lifestyle change. Primary reproductive prevention consists of carrier testing, genetic counseling, partner testing in high-risk relatives or founder populations, preimplantation genetic testing for monogenic disease, prenatal diagnosis by chorionic-villus sampling or amniocentesis, and use of donor gametes where desired. Familial-variant testing must use validated modern HGVS nomenclature and an accredited laboratory. (mavraki2023genetictestingfor pages 13-14, mavraki2023genetictestingfor pages 2-3)

Secondary prevention comprises rapid molecular diagnosis, cascade testing, early cardiac/neurologic surveillance, and anticipatory planning for metabolic illness. Tertiary prevention includes vaccination according to standard schedules, prompt treatment of infection, avoidance of fasting/dehydration, perioperative planning, rehabilitation, seizure control, nutrition support, and cardiomyopathy surveillance. Vaccination does not prevent the genetic disease but may reduce infection-triggered crises. No prophylactic medication has proven disease-specific efficacy.

## 14. Other species and natural disease

No naturally occurring NDUFA11-associated veterinary disease, breed predisposition, zoonotic potential, or cross-species transmission was identified. NDUFA11 is evolutionarily conserved among animals and fungi, particularly its membrane topology and cardiolipin-interacting features. Disruption of the *Neurospora crassa* homolog causes incomplete complex-I assembly, supporting conserved function rather than documenting a natural animal disease. (berger2008mitochondrialcomplexi pages 3-4, knappwilson2021maintenanceofcomplex pages 2-3)

Relevant taxa include *Homo sapiens* (NCBI Taxonomy 9606), *Caenorhabditis elegans* (6239), *Neurospora crassa* (5141), and *Rattus norvegicus* (10116; source of H9c2 cardioblasts). There is no infectious transmission.

## 15. Model organisms and experimental systems

The best direct model is the *C. elegans* **nduf-11/B0491.5** system. CRISPR-Cas9 null homozygotes arrest at larval stage L2, while RNAi hypomorphs survive to adulthood but are smaller, thinner and less fecund; their progeny arrest at L2. RNAi reduced protein by approximately 83%, lowered other complex-I subunits by approximately 50%, destabilized active complex I and supercomplexes, increased compensatory complex-II activity and ROS potential, and altered cristae ultrastructure. It models dosage sensitivity, bioenergetic failure, structural mitochondrial disease and developmental severity, but not the human tissue-specific neurologic and cardiac phenotype. DOI: https://doi.org/10.1242/jcs.258399; received January 12 and accepted May 28, 2021. (knappwilson2021maintenanceofcomplex pages 3-5, knappwilson2021maintenanceofcomplex pages 1-2, knappwilson2021maintenanceofcomplex pages 2-3)

**Exact model-paper abstract quote:** “Animals homozygous for a CRISPR-Cas9-generated knockout allele of nduf-11 arrested at the second larval (L2) development stage.” The authors also observed “destabilisation of complex I and its supercomplexes and perturbation of respiratory function.” (knappwilson2021maintenanceofcomplex pages 1-2)

H9c2 cardioblast siRNA provides a cardiac in-vitro model: NDUFA11 knockdown disrupted respirasome assembly, reduced complexes I/III/IV activities and ATP production, and increased mitochondrial ROS. DOI: https://doi.org/10.1038/s41598-018-36040-9; publication year 2018. Its limitations include transformed rat cells, acute knockdown, and absence of patient-specific variants. (jang2018elucidatingthecontribution pages 1-2)

Patient fibroblasts are the most disease-proximal cellular model and demonstrated aberrant splicing and 45% residual NADH:ubiquinone reductase activity. Patient-derived iPSCs, neurons, cardiomyocytes, skeletal myotubes, organoids, knock-in mice, zebrafish, and isogenic rescue experiments were not identified. These are important research priorities, especially for testing splice correction, NDUFA11 replacement, metabolic rescue and genotype–phenotype relationships.

## Current interpretation and research priorities

The central expert interpretation is that NDUFA11 is not merely dispensable “accessory” material: it is required for stable complex-I and respirasome architecture. Human enzyme assays, patient RNA, cardioblast knockdown and whole-organism loss-of-function experiments converge on this conclusion. Conversely, ROS-mediated injury, cardiolipin effects, and precise cell-death pathways remain model-supported rather than demonstrated in patients. (knappwilson2021maintenanceofcomplex pages 3-5, knappwilson2021maintenanceofcomplex pages 2-3, jang2018elucidatingthecontribution pages 1-2)

Priority gaps are: systematic identification of additional patients; transcript-verified HGVS and ClinVar curation; gnomAD founder-allele frequency; longitudinal cardiac, neurologic and myopathy outcomes; patient-derived iPSC models; quantitative metabolomic/proteomic signatures; natural-history endpoints; and preclinical testing of splice-switching oligonucleotides or gene replacement. The scarcity of 2023–2024 disease-specific publications is itself informative: recent advances concern mitochondrial genomic diagnosis and supportive consensus care rather than new MC1DN14 cohorts or therapies. The 2023 guidance supports simultaneous nuclear and mtDNA testing and urgent trio WES/WGS, offering the most immediate real-world improvement in case recognition. (mavraki2023genetictestingfor pages 2-3, mavraki2023genetictestingfor pages 1-2)

References

1. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 14): Open Targets Query (Mitochondrial complex I deficiency, nuclear type 14, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (berger2008mitochondrialcomplexi pages 1-2): Itai Berger, Eli Hershkovitz, Avraham Shaag, Simon Edvardson, Ann Saada, and Orly Elpeleg. Mitochondrial complex i deficiency caused by a deleterious ndufa11 mutation. Annals of Neurology, 63:405-408, Mar 2008. URL: https://doi.org/10.1002/ana.21332, doi:10.1002/ana.21332. This article has 157 citations and is from a highest quality peer-reviewed journal.

3. (fernandez‐vizarra2021mitochondrialdisordersof pages 96-99): Erika Fernandez‐Vizarra and Massimo Zeviani. Mitochondrial disorders of the oxphos system. Dec 2021. URL: https://doi.org/10.1002/1873-3468.13995, doi:10.1002/1873-3468.13995. This article has 410 citations and is from a peer-reviewed journal.

4. (knappwilson2021maintenanceofcomplex pages 2-3): Amber Knapp-Wilson, Gonçalo C. Pereira, Emma Buzzard, Holly C. Ford, Andrew Richardson, Robin A. Corey, Chris Neal, Paul Verkade, Andrew P. Halestrap, Vicki A. M. Gold, Patricia E. Kuwabara, and Ian Collinson. Maintenance of complex i and its supercomplexes by nduf-11 is essential for mitochondrial structure, function and health. Jul 2021. URL: https://doi.org/10.1242/jcs.258399, doi:10.1242/jcs.258399. This article has 44 citations and is from a domain leading peer-reviewed journal.

5. (berger2008mitochondrialcomplexi pages 2-3): Itai Berger, Eli Hershkovitz, Avraham Shaag, Simon Edvardson, Ann Saada, and Orly Elpeleg. Mitochondrial complex i deficiency caused by a deleterious ndufa11 mutation. Annals of Neurology, 63:405-408, Mar 2008. URL: https://doi.org/10.1002/ana.21332, doi:10.1002/ana.21332. This article has 157 citations and is from a highest quality peer-reviewed journal.

6. (berger2008mitochondrialcomplexi pages 3-4): Itai Berger, Eli Hershkovitz, Avraham Shaag, Simon Edvardson, Ann Saada, and Orly Elpeleg. Mitochondrial complex i deficiency caused by a deleterious ndufa11 mutation. Annals of Neurology, 63:405-408, Mar 2008. URL: https://doi.org/10.1002/ana.21332, doi:10.1002/ana.21332. This article has 157 citations and is from a highest quality peer-reviewed journal.

7. (knappwilson2021maintenanceofcomplex pages 3-5): Amber Knapp-Wilson, Gonçalo C. Pereira, Emma Buzzard, Holly C. Ford, Andrew Richardson, Robin A. Corey, Chris Neal, Paul Verkade, Andrew P. Halestrap, Vicki A. M. Gold, Patricia E. Kuwabara, and Ian Collinson. Maintenance of complex i and its supercomplexes by nduf-11 is essential for mitochondrial structure, function and health. Jul 2021. URL: https://doi.org/10.1242/jcs.258399, doi:10.1242/jcs.258399. This article has 44 citations and is from a domain leading peer-reviewed journal.

8. (jang2018elucidatingthecontribution pages 1-2): Sehwan Jang and Sabzali Javadov. Elucidating the contribution of etc complexes i and ii to the respirasome formation in cardiac mitochondria. Dec 2018. URL: https://doi.org/10.1038/s41598-018-36040-9, doi:10.1038/s41598-018-36040-9. This article has 72 citations and is from a peer-reviewed journal.

9. (knappwilson2021maintenanceofcomplex pages 1-2): Amber Knapp-Wilson, Gonçalo C. Pereira, Emma Buzzard, Holly C. Ford, Andrew Richardson, Robin A. Corey, Chris Neal, Paul Verkade, Andrew P. Halestrap, Vicki A. M. Gold, Patricia E. Kuwabara, and Ian Collinson. Maintenance of complex i and its supercomplexes by nduf-11 is essential for mitochondrial structure, function and health. Jul 2021. URL: https://doi.org/10.1242/jcs.258399, doi:10.1242/jcs.258399. This article has 44 citations and is from a domain leading peer-reviewed journal.

10. (mavraki2023genetictestingfor pages 2-3): Eleni Mavraki, Robyn Labrum, Kate Sergeant, Charlotte L. Alston, Cathy Woodward, Conrad Smith, Charlotte V. Y. Knowles, Yogen Patel, Philip Hodsdon, Jack P. Baines, Emma L. Blakely, James Polke, Robert W. Taylor, and Carl Fratter. Genetic testing for mitochondrial disease: the united kingdom best practice guidelines. European Journal of Human Genetics, 31:148-163, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01249-w, doi:10.1038/s41431-022-01249-w. This article has 96 citations and is from a domain leading peer-reviewed journal.

11. (mavraki2023genetictestingfor pages 1-2): Eleni Mavraki, Robyn Labrum, Kate Sergeant, Charlotte L. Alston, Cathy Woodward, Conrad Smith, Charlotte V. Y. Knowles, Yogen Patel, Philip Hodsdon, Jack P. Baines, Emma L. Blakely, James Polke, Robert W. Taylor, and Carl Fratter. Genetic testing for mitochondrial disease: the united kingdom best practice guidelines. European Journal of Human Genetics, 31:148-163, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01249-w, doi:10.1038/s41431-022-01249-w. This article has 96 citations and is from a domain leading peer-reviewed journal.

12. (neugebauer2025currentglobalvitamin pages 1-2): Julia Neugebauer, Karit Reinson, Marcello Bellusci, Julien H. Park, Omar Hikmat, Enrico Bertini, Manuel Schiff, and Shamima Rahman. Current global vitamin and cofactor prescribing practices for primary mitochondrial diseases: results of a european reference network survey. Journal of Inherited Metabolic Disease, Nov 2025. URL: https://doi.org/10.1002/jimd.12805, doi:10.1002/jimd.12805. This article has 10 citations and is from a peer-reviewed journal.

13. (ugalde2009mitochondrialdisordersdue pages 4-6): Cristina Ugalde, María Morán, Alberto Blázquez, Joaquín Arenas, and Miguel A. Martín. Mitochondrial disorders due to nuclear oxphos gene defects. Advances in experimental medicine and biology, 652:85-116, Jan 2009. URL: https://doi.org/10.1007/978-90-481-2813-6\_7, doi:10.1007/978-90-481-2813-6\_7. This article has 16 citations and is from a peer-reviewed journal.

14. (mancuso2024managementofseizures pages 1-2): Michelangelo Mancuso, Maria T. Papadopoulou, Yi Shiau Ng, Anna Ardissone, Marcello Bellusci, Enrico Bertini, Lidia Di Vito, Teresinha Evangelista, Carmen Fons, Omar Hikmat, Rita Horvath, Thomas Klopstock, Cornelia Kornblum, Costanza Lamperti, Laura Licchetta, Maria Judit Molnar, Kristin N. Varhaug, Mar O'Callaghan, Ronit M. Pressler, Manuel Schiff, Serenella Servidei, Nora Szabo, Gráinne S. Gorman, J Helen Cross, and Shamima Rahman. Management of seizures in patients with primary mitochondrial diseases: consensus statement from the intererns mitochondrial working group. European Journal of Neurology, Apr 2024. URL: https://doi.org/10.1111/ene.16275, doi:10.1111/ene.16275. This article has 19 citations and is from a domain leading peer-reviewed journal.

15. (scheffler2015mitochondrialdiseaseassociated pages 18-21): Immo E. Scheffler. Mitochondrial disease associated with complex i (nadh-coq oxidoreductase) deficiency. Journal of Inherited Metabolic Disease, 38:405-415, May 2015. URL: https://doi.org/10.1007/s10545-014-9768-6, doi:10.1007/s10545-014-9768-6. This article has 75 citations and is from a peer-reviewed journal.

16. (mavraki2023genetictestingfor pages 13-14): Eleni Mavraki, Robyn Labrum, Kate Sergeant, Charlotte L. Alston, Cathy Woodward, Conrad Smith, Charlotte V. Y. Knowles, Yogen Patel, Philip Hodsdon, Jack P. Baines, Emma L. Blakely, James Polke, Robert W. Taylor, and Carl Fratter. Genetic testing for mitochondrial disease: the united kingdom best practice guidelines. European Journal of Human Genetics, 31:148-163, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01249-w, doi:10.1038/s41431-022-01249-w. This article has 96 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_14-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032619` (4 mentions) - the report calls it "if available"; MONDO calls it **mitochondrial complex I deficiency, nuclear type 14**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005747` (obsolete mitochondrial respiratory chain complex I) (1 mention) - replaced by `GO:0045271`