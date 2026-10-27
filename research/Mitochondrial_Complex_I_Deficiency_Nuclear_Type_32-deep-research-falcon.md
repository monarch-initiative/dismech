---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-09T10:48:59.284154'
end_time: '2026-09-09T11:14:10.664583'
duration_seconds: 1511.38
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Mitochondrial Complex I Deficiency, Nuclear Type 32
  mondo_id: MONDO:0032635
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032635
    reported_labels:
    - if available
    ontology_label: mitochondrial complex I deficiency, nuclear type 32
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_32-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 32
- **MONDO ID:** MONDO:0032635 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 32** covering all of the
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
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 32
- **MONDO ID:** MONDO:0032635 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 32** covering all of the
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


# Mitochondrial Complex I Deficiency, Nuclear Type 32 (MC1DN32)

## Executive summary and evidence limits

MC1DN32 is an ultra-rare, autosomal-recessive mitochondrial disorder caused by biallelic germline variants in **NDUFB8**, which encodes an accessory subunit of respiratory-chain complex I. The defining phenotype is an infantile, progressive Leigh-syndrome-spectrum encephalo(cardio)myopathy with isolated complex-I deficiency. The disease-specific human evidence remains exceptionally small: the foundational publication described **two affected individuals from two unrelated families**. Accordingly, percentages calculated from these two patients are descriptive—not reliable population frequencies—and no disease-specific prevalence, incidence, survival curve, treatment-response rate, or validated prognostic model exists. The key causal evidence is unusually strong for such a small series because genetic segregation, patient RNA analysis, biochemical testing, and wild-type complementation all converged on NDUFB8 (Piekutowska-Abramczuk et al., published February 8, 2018; *AJHG* 102:460–467; PMID **29429571**; DOI/URL: https://doi.org/10.1016/j.ajhg.2018.01.008). (piekutowskaabramczuk2018ndufb8mutationscause pages 6-7, piekutowskaabramczuk2018ndufb8mutationscause pages 4-5, piekutowskaabramczuk2018ndufb8mutationscause pages 1-2)

The primary article’s abstract states: **“Complementation studies by expression of wild-type NDUFB8 in cells from affected individuals restored mitochondrial function, confirming NDUFB8 variants as the cause of complex I deficiency.”** It concludes: **“Hereby we establish NDUFB8 as a relevant gene in childhood-onset mitochondrial disease.”** (piekutowskaabramczuk2018ndufb8mutationscause pages 1-2)

| Domain | Disease-specific finding | Evidence type/strength | Key quantitative detail |
|---|---|---|---|
| Identifier and gene | Mitochondrial complex I deficiency, nuclear type 32 (MC1DN32; MONDO:0032635) is caused by biallelic germline variants in **NDUFB8**, encoding an accessory subunit of respiratory-chain complex I. | Authoritative disease-target resource plus primary human functional study; strong causal evidence (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 32, piekutowskaabramczuk2018ndufb8mutationscause pages 1-2) | Primary report: 2 affected individuals from 2 unrelated families. |
| Patient 1 variants | Compound-heterozygous **NDUFB8** variants: NM_005004.3:c.227C>A (p.Pro76Gln) and c.432C>G (p.Cys144Trp). The latter predominantly caused exon-4 skipping. | Primary human genetic segregation, patient RNA, biochemical, and complementation evidence; strong (piekutowskaabramczuk2018ndufb8mutationscause pages 4-5, piekutowskaabramczuk2018ndufb8mutationscause pages 2-4) | c.227C>A occurred in 1/246,208 gnomAD alleles; c.432C>G was absent from queried population databases. cDNA products: 39% exon-4-skipped, 14% missense-containing, and 47% from the other allele. |
| Patient 2 variants | Compound-heterozygous **NDUFB8** variants: c.184T>C (p.Tyr62His) and loss-of-function c.189delA (p.Glu63Aspfs*35). | Primary human genetic segregation and functional evidence; strong (piekutowskaabramczuk2018ndufb8mutationscause pages 4-5) | c.184T>C was absent from ExAC and 1000 Genomes; c.189delA occurred in 3/244,804 gnomAD alleles in the original report. |
| Onset and phenotype | Progressive infantile Leigh-like encephalomyopathy characterized by failure to thrive, reduced consciousness, muscular hypotonia, developmental delay, elevated lactate, respiratory failure, and seizures in one patient; cardiac hypertrophy occurred in one patient. | Primary two-patient clinical series; compelling but numerically very limited (piekutowskaabramczuk2018ndufb8mutationscause pages 1-2, piekutowskaabramczuk2018ndufb8mutationscause pages 2-4) | Onset at 3 months and 6 months; observed frequencies within the reported series should not be treated as population estimates. |
| Neuroimaging | Bilateral, symmetric basal-ganglia abnormalities with brainstem or internal-capsule involvement; one patient developed profound brain and brainstem atrophy, cystic lesions, and chronic subdural hematomas. | Primary serial MRI evidence; moderate-to-strong phenotype evidence from 2 patients (piekutowskaabramczuk2018ndufb8mutationscause pages 2-4, piekutowskaabramczuk2018ndufb8mutationscause pages 5-6) | In the illustrated patient, MRI progressed between ages 3 and 6 months. |
| Biochemical defect | Isolated respiratory-chain complex I deficiency with reduced assembled complex I and selectively impaired complex-I-linked respiration. | Primary patient muscle and fibroblast enzyme assays, BN-PAGE, and respirometry; strong (piekutowskaabramczuk2018ndufb8mutationscause pages 1-2, piekutowskaabramczuk2018ndufb8mutationscause pages 2-4) | Patient 1 muscle complex I activity: 5.0% of citrate-synthase activity (reference >6.7%). Patient 2 fibroblast activity: 7 nmol/min/mg (reference 20.1–53.7); malate/glutamate respiration: 1.7 nmol O₂/min/mg (reference 4.7–11.7), with preserved succinate-supported respiration. |
| Functional rescue | Lentiviral expression of wild-type **NDUFB8** restored complex I activity, protein abundance, and cellular respiration, confirming that the variants caused the biochemical defect. | Primary patient-cell complementation; very strong functional causality evidence (piekutowskaabramczuk2018ndufb8mutationscause pages 6-7, piekutowskaabramczuk2018ndufb8mutationscause pages 4-5, piekutowskaabramczuk2018ndufb8mutationscause pages 5-6) | Patient 1 fibroblast complex I/citrate-synthase ratio increased from 0.02 to 0.09 after rescue (reference 0.04–0.12); complex I flow-cytometry signal increased from 2.52 to 7.59 versus control 8.59. |
| Outcomes | The disease course was severe but variable: one child died in infancy, whereas the other was alive in childhood. | Primary case outcomes; very low precision because n=2 (piekutowskaabramczuk2018ndufb8mutationscause pages 2-4) | One death at 15 months; one survivor reported alive at 6 years. |
| Epidemiology gap | No disease-specific prevalence, incidence, carrier-frequency, founder-effect, penetrance, or sex-ratio estimate is available for MC1DN32. General Leigh-syndrome statistics cannot be assigned to this genotype. | Explicit evidence gap; only 2 disease-specific patients reported in the foundational study (piekutowskaabramczuk2018ndufb8mutationscause pages 1-2, shen2025thepathto pages 1-2) | Disease-specific denominator unavailable; published human series n=2. |
| Treatment gap | No approved or proven **NDUFB8**-targeted therapy and no documented treatment-response rate or NDUFB8-specific clinical-trial enrollment were identified. Management is extrapolated from general primary mitochondrial disease/Leigh-spectrum supportive-care guidance. | No disease-specific therapeutic evidence; general consensus and trial evidence only (parikh2015diagnosisandmanagement pages 8-9, NCT06843811 chunk 1, NCT02352896 chunk 1) | Leigh-spectrum trials have evaluated or are evaluating agents such as vatiquinone and sirolimus, but available records do not report an NDUFB8 subgroup. |
| Model gap | Disease-specific models are limited to patient fibroblasts, muscle assays, complementation, and engineered NDUFB8-deficient cells; no validated NDUFB8 animal, iPSC, organoid, single-cell, or spatial-omics disease model was identified. | Direct in-vitro evidence with a major translational-model gap (piekutowskaabramczuk2018ndufb8mutationscause pages 5-6, dang2020analysisofhuman pages 25-27) | Patient-derived cellular evidence represents only 2 genotypes/individuals; fibroblasts may not reproduce neuronal or cardiac tissue pathology. |


*Table: Concise evidence-grade summary of the genetic, clinical, biochemical, and functional findings for NDUFB8-related mitochondrial complex I deficiency. It also highlights the major epidemiologic, therapeutic, and disease-model limitations.*

## 1. Disease information

**Definition.** MC1DN32 is a nuclear-genome-encoded oxidative-phosphorylation disorder in which NDUFB8 dysfunction destabilizes or prevents assembly of mitochondrial complex I, producing deficient NADH-linked respiration and a predominantly neurologic Leigh-like phenotype, sometimes with cardiomyopathy. It belongs to the broader **Leigh syndrome spectrum (LSS)** and primary mitochondrial diseases. (piekutowskaabramczuk2018ndufb8mutationscause pages 1-2, piekutowskaabramczuk2018ndufb8mutationscause pages 5-6)

**Identifiers and nomenclature.** Confirmed identifiers include **MONDO:0032635**, NDUFB8 **MIM 602140**, and the broader biochemical disease **OMIM 252010** (mitochondrial complex-I deficiency). Common names are *mitochondrial complex I deficiency, nuclear type 32*, *MC1DN32*, *NDUFB8-related mitochondrial disease*, *NDUFB8-related complex-I deficiency*, and *NDUFB8-related Leigh-like encephalomyopathy*. Open Targets maps MONDO:0032635 primarily to NDUFB8; its additional HIF1AN signal reflects neighboring/variant-record evidence and should not be interpreted as a second established causal gene. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 32, piekutowskaabramczuk2018ndufb8mutationscause pages 1-2)

No dedicated Orphanet, ICD-10, ICD-11, or MeSH code was established in the retrieved evidence. In practice, broader codes for mitochondrial metabolism disorder, mitochondrial complex-I deficiency, or Leigh disease are used. MeSH includes **Mitochondrial Diseases (D028361)**, **Mitochondrial Complex I Deficiency (C537475)**, and **Leigh Disease (D007888)**. (NCT05162768 chunk 2, NCT06843811 chunk 3)

The evidence is **aggregated disease-level knowledge derived from two published, deeply phenotyped patients and their cells**, not EHR-derived population data.

## 2. Etiology, risk, protection, and gene–environment interaction

The necessary cause is biallelic pathogenic or likely pathogenic **NDUFB8** variation. All reported variants were germline and compound heterozygous. No infectious, toxic, occupational, lifestyle, or environmental cause is known. Family history becomes relevant through carrier status; sex and age are not susceptibility factors in the usual multifactorial sense, although infancy is the observed period of clinical expression. (piekutowskaabramczuk2018ndufb8mutationscause pages 4-5, piekutowskaabramczuk2018ndufb8mutationscause pages 2-4)

No protective variant, modifier gene, epigenetic signature, or validated protective diet has been reported. Likewise, no MC1DN32-specific gene–environment interaction is established. Intercurrent infection, fasting, anesthesia, or other catabolic stress may plausibly precipitate deterioration in primary mitochondrial disease, but this is a **general PMD inference**, not demonstrated specifically in NDUFB8 patients. Consensus care therefore recommends avoiding prolonged fasting and catabolism during illness or procedures. (parikh2015diagnosisandmanagement pages 8-9, sue2022patientcarestandards pages 17-21)

## 3. Phenotypes

Because only two patients are known, “2/2” and “1/2” below describe the original series rather than true frequencies.

- **Infantile onset:** 3 and 6 months (2/2); HPO **HP:0003593, Infantile onset**.
- **Failure to thrive** (2/2), progressive/severe; **HP:0001508**.
- **Muscular hypotonia** (2/2); **HP:0001252**.
- **Reduced consciousness/encephalopathy** (reported at presentation); suggested **HP:0004372, Reduced consciousness/confusion** and **HP:0001298, Encephalopathy**.
- **Global developmental delay** (reported in the disease phenotype); **HP:0001263**.
- **Seizures** (1/2); **HP:0001250**.
- **Respiratory failure** (within the reported phenotype); **HP:0002878**.
- **Elevated blood and CSF lactate**; **HP:0002151, Increased serum lactate**, and **HP:0011971, Elevated CSF lactate**.
- **Bilateral symmetric basal-ganglia lesions** (2/2), with brainstem or internal-capsule involvement; suggested **HP:0002134, Basal ganglia abnormality**, **HP:0002363, Abnormal brainstem MRI signal intensity**, and **HP:0012758, Neurodegeneration**.
- **Progressive cerebral/brainstem atrophy and cystic lesions** in one illustrated patient; **HP:0002059, Cerebral atrophy**.
- **Left-ventricular hypertrophy** in one patient; **HP:0001712** or **HP:0001639, Hypertrophic cardiomyopathy**, depending on documented cardiac criteria. (piekutowskaabramczuk2018ndufb8mutationscause pages 1-2, piekutowskaabramczuk2018ndufb8mutationscause pages 2-4, piekutowskaabramczuk2018ndufb8mutationscause pages 5-6)

Serial MRI in the illustrated patient progressed between 3 and 6 months from symmetric midbrain, putaminal, and thalamic signal abnormalities to profound supratentorial/brainstem atrophy, cystic lesions, and chronic subdural hematomas. (piekutowskaabramczuk2018ndufb8mutationscause pages 2-4)

**Quality of life.** No MC1DN32-specific EQ-5D, SF-36, PedsQL, or caregiver-burden study exists. Severe hypotonia, developmental impairment, feeding/growth failure, seizures, and respiratory disease predict major dependence in mobility, communication, feeding, and self-care, but quantitative QOL attribution is unavailable.

## 4. Genetic and molecular information

**Gene/protein.** **NDUFB8** (RefSeq **NM_005004.3; NP_004995.1**) encodes NADH:ubiquinone oxidoreductase subunit B8, a nuclear-encoded, single-pass inner-mitochondrial-membrane accessory subunit. Suggested annotations include GO **mitochondrial respiratory-chain complex I**, **inner mitochondrial membrane**, **NADH dehydrogenase complex assembly**, and **oxidative phosphorylation**. (piekutowskaabramczuk2018ndufb8mutationscause pages 2-4, dang2020analysisofhuman pages 25-27)

**Reported variants.** In family/patient 1, c.227C>A (**p.Pro76Gln**) occurred in 1/246,208 gnomAD alleles, while c.432C>G (**p.Cys144Trp**) was absent from the queried public databases and 2,000 in-house exomes. The latter created abnormal splicing: approximately 39% of total measured cDNA was exon-4-skipped, 14% retained the missense-containing transcript, and 47% arose from the other allele. (piekutowskaabramczuk2018ndufb8mutationscause pages 4-5, piekutowskaabramczuk2018ndufb8mutationscause pages 2-4)

Patient 2 carried c.184T>C (**p.Tyr62His**) and the loss-of-function frameshift c.189delA (**p.Glu63Aspfs*35**). The missense variant was absent from ExAC/1000 Genomes, while c.189delA was present in 3/244,804 gnomAD alleles in the original analysis. Parental testing confirmed biallelic inheritance. (piekutowskaabramczuk2018ndufb8mutationscause pages 4-5)

The primary paper described the missense/splice changes as likely pathogenic/deleterious and the frameshift as loss-of-function. Contemporary ClinVar classifications should be checked at ingestion time because submissions can change. No somatic variants, chromosomal rearrangements, repeat expansions, or large pathogenic NDUFB8 copy-number variants were reported. No disease-specific modifier genes or epigenetic abnormalities are known.

## 5. Environmental information

No toxin, radiation, pollution, smoking, alcohol, dietary exposure, or pathogen has been shown to cause MC1DN32. Lifestyle does not alter the Mendelian recurrence risk. Avoidance of fasting and prompt treatment of infections are intended to reduce metabolic stress after disease exists, not to prevent the genotype. Vaccination is not contraindicated in PMD; age-appropriate immunization, including influenza vaccination, is recommended under general mitochondrial-care standards. (sue2022patientcarestandards pages 4-7, sue2022patientcarestandards pages 24-26)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic germline NDUFB8 variants lead to** reduced functional NDUFB8 through missense dysfunction, exon-4 skipping, or frameshift loss of function. (Demonstrated.)
2. **Reduced functional NDUFB8 leads to** defective assembly/stability of the distal complex-I membrane arm and reduced mature complex-I abundance. (Demonstrated in patient cells and knockout cells.)
3. **Complex-I loss leads to** impaired NADH-dependent electron transport and proton pumping, while complex-II-linked respiration is relatively preserved. (Demonstrated.)
4. **Impaired proton pumping leads to** reduced oxidative-phosphorylation capacity/ATP production and altered NADH redox balance; compensatory glycolysis leads to lactate accumulation. (ATP/redox step inferred from established complex-I biochemistry; lactate demonstrated.)
5. **Energy failure leads to** selective dysfunction and injury of high-demand neurons, glia, skeletal muscle, respiratory musculature, and cardiomyocytes. (Cell-type assignment partly inferred; clinical organ injury demonstrated.)
6. **Neural energy failure results in** bilateral basal-ganglia/brainstem lesions, hypotonia, developmental impairment, seizures, reduced consciousness, and respiratory failure; **cardiac branch:** cardiomyocyte energy failure results in hypertrophy/cardiomyopathy. (Clinical manifestations demonstrated; cellular bridge inferred.) (piekutowskaabramczuk2018ndufb8mutationscause pages 1-2, piekutowskaabramczuk2018ndufb8mutationscause pages 5-6)

NDUFB8 belongs to the **ND5/Pd membrane module** near complex I’s distal end. Its N-terminus faces the matrix and C-terminus the intermembrane space; it contacts ND5, ND4, NDUFB4, NDUFB9, NDUFB7, and NDUFB10. Structural work suggests participation in CI–CIII–CIV respirasome organization, but a specific mutant-NDUFB8 supercomplex defect has not been directly demonstrated in human disease tissue. (piekutowskaabramczuk2018ndufb8mutationscause pages 5-6, dang2020analysisofhuman pages 25-27)

Quantitatively, P1 muscle complex-I activity was 5.0% of citrate-synthase activity (reference >6.7%). P2 fibroblast activity was 7 nmol/min/mg (reference 20.1–53.7), and malate/glutamate-supported respiration was 1.7 nmol O₂/min/mg (reference 4.7–11.7), whereas succinate-supported respiration was normal. Wild-type complementation raised P1’s complex-I/citrate-synthase ratio from 0.02 to 0.09 (reference 0.04–0.12) and complex-I flow-cytometry signal from 2.52 to 7.59 versus control 8.59. (piekutowskaabramczuk2018ndufb8mutationscause pages 4-5, piekutowskaabramczuk2018ndufb8mutationscause pages 1-2, piekutowskaabramczuk2018ndufb8mutationscause pages 2-4, piekutowskaabramczuk2018ndufb8mutationscause pages 5-6)

Suggested GO biological processes: **mitochondrial electron transport, NADH to ubiquinone; respiratory-chain complex-I assembly; proton transmembrane transport; oxidative phosphorylation; ATP metabolic process; cellular response to oxidative stress**. Suggested cellular components: **mitochondrial inner membrane, respiratory-chain complex I, respirasome**. Suggested CL terms, mostly inferential: **neuron (CL:0000540), astrocyte (CL:0000127), oligodendrocyte (CL:0000128), skeletal muscle cell (CL:0000188), cardiomyocyte (CL:0000746)**.

No MC1DN32-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic patient dataset was found. RNA analysis was targeted to NDUFB8 splicing rather than transcriptome-wide profiling.

## 7. Anatomical structures affected

The **central nervous system** is primary: bilateral putamen/basal ganglia, thalami, midbrain/brainstem, and internal capsule; cerebral tissue becomes involved through progressive atrophy. Suggested UBERON terms include **brain (UBERON:0000955), basal ganglion (UBERON:0002420), putamen (UBERON:0001874), thalamus (UBERON:0001897), midbrain (UBERON:0001891), brainstem (UBERON:0002298), and internal capsule (UBERON:0001871)**. Lesions are characteristically bilateral/symmetric. (piekutowskaabramczuk2018ndufb8mutationscause pages 2-4, piekutowskaabramczuk2018ndufb8mutationscause pages 5-6)

Secondary systems include skeletal/respiratory muscle and heart, particularly the left ventricle. At subcellular level, the lesion is in **mitochondria → inner mitochondrial membrane → complex I/respirasome**. Liver, kidney, endocrine, immune, and sensory-organ involvement has not been established in MC1DN32.

## 8. Temporal development

Pregnancy and birth were unremarkable in both reported cases. Onset was subacute in early infancy at 3 or 6 months, followed by a progressive course. No validated stages exist. A practical clinical sequence is early feeding/growth and tone abnormality, evolving encephalopathy/developmental impairment, MRI progression, and potentially respiratory or cardiac decompensation. One patient died at 15 months; the other was alive at 6 years, demonstrating substantial expressivity despite uniformly early onset. Remission has not been documented. Catabolic illness is a general mitochondrial vulnerability period, and early molecular diagnosis is a key intervention window. (piekutowskaabramczuk2018ndufb8mutationscause pages 2-4, sue2022patientcarestandards pages 4-7)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two confirmed carrier parents, each pregnancy has a 25% affected, 50% carrier, and 25% non-carrier probability. Penetrance for confirmed biallelic pathogenic genotypes cannot be estimated; the two observed patients were affected, but ascertainment precludes claiming complete penetrance. Expressivity is variable, as shown by death at 15 months versus survival to 6 years. Anticipation is not expected. Germline mosaicism, founder effects, consanguinity effects, carrier frequency, sex ratio, and population-specific enrichment are unknown. (piekutowskaabramczuk2018ndufb8mutationscause pages 4-5, piekutowskaabramczuk2018ndufb8mutationscause pages 2-4)

No MC1DN32 incidence or prevalence estimate exists. The often-cited approximately 1:40,000 live-birth prevalence concerns **all classic Leigh syndrome**, not this genotype. LSS is genetically heterogeneous; the 2023 ClinGen project curated 114 relationships—31 definitive, 38 moderate, 43 limited, and 2 disputed—and found autosomal-recessive inheritance in 90, emphasizing why aggregate LSS epidemiology cannot be assigned to NDUFB8 disease. (shen2025thepathto pages 1-2, mccormick2023expertpanelcuration pages 7-9, mccormick2023expertpanelcuration pages 9-10)

## 10. Diagnostics

**Clinical suspicion.** Consider MC1DN32 in an infant with failure to thrive, hypotonia, developmental slowing/regression, altered consciousness or seizures, elevated lactate, and bilateral symmetric basal-ganglia/brainstem MRI lesions. Current LSS frameworks combine compatible neurologic findings, characteristic imaging, biochemical evidence of mitochondrial dysfunction, and mandatory molecular confirmation. (baldo2024acomprehensiveapproach pages 2-4, baldo2024acomprehensiveapproach pages 1-2)

**Initial investigations.** Recommended general LSS testing includes blood lactate and pyruvate with lactate/pyruvate ratio, glucose, blood gas, electrolytes, liver/renal indices, CK, plasma amino acids, acylcarnitines, urinary organic acids, and CSF lactate when neurologically appropriate. Normal metabolites do not exclude disease. Brain MRI with diffusion/T2/FLAIR and, where available, MR spectroscopy can identify symmetric lesions and lactate. ECG/echocardiography are important because hypertrophy occurred in one NDUFB8 patient. (baldo2024acomprehensiveapproach pages 6-8, baldo2024acomprehensiveapproach pages 4-6, sue2022patientcarestandards pages 4-7)

**Genetic strategy.** Trio WES/WGS or a comprehensive nuclear mitochondrial/complex-I panel including **NDUFB8**, with CNV calling, is preferable to phenotype-restricted single-gene testing. Parallel mtDNA sequencing remains appropriate because LSS can arise from either genome. The 2023 UK guideline describes the field’s shift from “biopsy first” toward NGS/WES/WGS using blood or urine, with tissue selection particularly important for mtDNA variants; for this nuclear disorder, blood DNA is ordinarily suitable. Segregation testing confirms phase and enables cascade testing. (mavraki2023genetictestingfor pages 1-2)

Targeted NDUFB8 RNA sequencing/RT-PCR is useful for suspected splice variants, as demonstrated by exon-4 skipping. If genetics is unresolved, patient fibroblast or muscle studies may measure complex-I activity, BN-PAGE/in-gel activity, oxygen consumption, and protein abundance; biopsy is now reserved for severe, organ-specific, conflicting, or unresolved cases. (piekutowskaabramczuk2018ndufb8mutationscause pages 4-5, baldo2024acomprehensiveapproach pages 6-8, baldo2024acomprehensiveapproach pages 4-6)

CMA/karyotype/FISH and repeat-expansion assays are not first-line tests for this single-gene disorder unless another diagnosis is suspected. Differential diagnoses include other nuclear or mtDNA complex-I deficiencies, pyruvate dehydrogenase deficiency, HIBCH/ECHS1 disease, SLC19A3-related biotin-thiamine-responsive basal-ganglia disease, organic acidemias, and other causes of symmetric basal-ganglia injury. Basic metabolic testing is important because some mimics are treatable; a 2024 diagnostic study reported that its biochemical pipeline characterized 80% of its broader LSS cohort and enabled specific intervention in 10%, figures not specific to NDUFB8. (baldo2024acomprehensiveapproach pages 6-8, baldo2024acomprehensiveapproach pages 2-4)

There is no population or newborn screening program for MC1DN32. Molecular cascade testing is appropriate for relatives once familial variants are known.

## 11. Outcome and prognosis

Disease-specific outcome data comprise one death at 15 months and one survivor at 6 years. Therefore, no valid 5- or 10-year survival rate, median life expectancy, or mortality rate can be calculated. Severe early developmental delay, respiratory failure, progressive MRI injury, persistent lactic acidosis, and cardiomyopathy are biologically plausible adverse factors, but none is validated for NDUFB8. In broader LSS, early developmental delay has been associated with poor prognosis, but genotype-specific extrapolation remains uncertain. (piekutowskaabramczuk2018ndufb8mutationscause pages 2-4, NCT06843811 chunk 2)

Expected morbidity includes severe neurodevelopmental disability, impaired mobility and feeding, epilepsy, respiratory compromise, and cardiac disease. Recovery of established neurodegeneration has not been documented. No MC1DN32-specific prognostic biomarker is validated; serial clinical function, lactate, MRI, respiratory status, and cardiac measures are pragmatic monitoring tools rather than proven surrogate endpoints.

## 12. Treatment and current applications

No approved NDUFB8-targeted drug, gene therapy, RNA therapy, cell therapy, surgery, or genotype-specific pharmacogenomic recommendation exists. No treatment response was reported for the two original patients. Real-world management therefore follows multidisciplinary PMD/LSS standards:

- Avoid prolonged fasting/catabolism; maintain an emergency plan and consider dextrose-containing IV fluids during illness/procedures, individualized to glucose, lactate, cardiac status, and contraindications. (parikh2015diagnosisandmanagement pages 8-9, sue2022patientcarestandards pages 17-21)
- Provide nutritional and swallowing assessment, calorie support, and enteral feeding when required.
- Treat seizures with standard agents; levetiracetam and benzodiazepines are commonly preferred. Avoid or use valproate only with specialist risk assessment—especially until POLG disease is excluded—and use topiramate/zonisamide cautiously where acidosis is present. (sue2022patientcarestandards pages 17-21, sue2022patientcarestandards pages 24-26)
- Undertake PT/OT/speech and feeding therapy; PT aims to maintain mobility and prevent contractures, while exercise requires prior cardiac assessment and individualized dosing. (sue2022patientcarestandards pages 26-28)
- Monitor ECG/echocardiography, respiratory function/sleep-disordered breathing, growth, hearing/vision, neurologic status, and endocrine/renal complications according to phenotype. Annual ECG is supported by general PMD standards. (sue2022patientcarestandards pages 4-7)
- Use anesthesia with minimized fasting, glucose monitoring, cautious muscle relaxants, and avoidance/limitation of prolonged propofol infusion. Potential mitochondrial toxicities warrant caution with aminoglycosides, linezolid, metformin, and high-dose acetaminophen. (parikh2015diagnosisandmanagement pages 8-9)
- CoQ10, riboflavin, thiamine, carnitine, creatine, alpha-lipoic acid, or multivitamin “cocktails” are frequently prescribed empirically, but efficacy for NDUFB8 is unproven; supplementation should be specialist-directed and deficiency-based where possible. (parikh2015diagnosisandmanagement pages 8-9)

Suggested NCIt intervention concepts include **Supportive Care**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Enteral Nutrition**, **Anticonvulsant Therapy**, **Genetic Counseling**, and **Clinical Trial**.

**Trials.** No record identified an NDUFB8 participant or subgroup. Completed phase-2 vatiquinone/EPI-743 LSS studies enrolled 35 and 30 children (NCT01721733 and NCT02352896); the latter used up to 15 mg/kg, maximum 200 mg three times daily, but the registry does not establish NDUFB8-specific efficacy. (NCT02352896 chunk 1, NCT01721733 chunk 1) The MIT-E refractory-epilepsy trial, NCT04378075, enrolled 68 and was terminated by sponsor decision; it cannot support routine use. (NCT04378075 chunk 1) A phase-2 enteral sirolimus study, NCT06843811, is enrolling by invitation, with estimated n=15 and genetically confirmed Leigh syndrome eligibility; its rationale derives from Ndufs4 models, not NDUFB8-specific evidence. (NCT06843811 chunk 1, NCT06843811 chunk 2) The completed phase-3 NuPower elamipretide trial enrolled 102 adults with nuclear primary mitochondrial myopathy, but its adult myopathy/PEO phenotype differs substantially from infantile NDUFB8 encephalopathy. (NCT05162768 chunk 1, NCT05162768 chunk 2)

## 13. Prevention

The genotype cannot be prevented through vaccination or lifestyle modification. **Primary reproductive prevention** comprises carrier testing, genetic counseling, preimplantation genetic testing for monogenic disease (PGT-M), and prenatal diagnosis by chorionic-villus sampling or amniocentesis for known familial variants. Mitochondrial replacement therapy is not indicated because NDUFB8 is nuclear, not mtDNA encoded. Secondary prevention comprises early molecular diagnosis, cascade testing, cardiac/respiratory surveillance, and prompt sick-day management. Tertiary prevention includes immunization, nutritional support, seizure control, rehabilitation, contracture prevention, aspiration precautions, and rapid treatment of infections. The UK guideline explicitly addresses family testing and reproductive options in mitochondrial disease. (mavraki2023genetictestingfor pages 1-2, sue2022patientcarestandards pages 24-26)

## 14. Other species and natural disease

NDUFB8 is evolutionarily conserved across vertebrates, with lower conservation in insects and poorer conservation in fungi/plants. No naturally occurring veterinary disorder conclusively equivalent to human MC1DN32 was identified, and there is no zoonotic or transmissible component. Structural information from bovine/porcine complex I supports conserved placement near ND5 and respirasome interfaces, but this is comparative structural biology rather than natural disease evidence. (piekutowskaabramczuk2018ndufb8mutationscause pages 2-4, piekutowskaabramczuk2018ndufb8mutationscause pages 5-6)

Relevant taxa for comparative work include **Homo sapiens (NCBI Taxon 9606), Mus musculus (10090), Drosophila melanogaster (7227), Bos taurus (9913), and Sus scrofa (9823)**. Ortholog identifiers should be retrieved directly from current NCBI Gene/Alliance records before database ingestion.

## 15. Model organisms and experimental systems

The validated disease-specific models are **patient fibroblasts**, patient muscle biochemical assays, lentiviral wild-type rescue, and engineered NDUFB8-deficient cells. Knockout cells failed to assemble complex I, while complementation restored complex-I abundance and respiration. These experiments establish causality but cannot reproduce basal-ganglia circuitry, neurodevelopment, blood–brain-barrier effects, or cardiopulmonary physiology. (piekutowskaabramczuk2018ndufb8mutationscause pages 5-6, dang2020analysisofhuman pages 25-27)

No validated NDUFB8 knock-in mouse, zebrafish, fly disease model, patient iPSC-derived neuron/cardiomyocyte, or brain organoid was found. Broader LSS research uses yeast, *Drosophila*, zebrafish, *C. elegans*, the **Ndufs4−/− mouse**, patient iPSCs, and organoids; a 2024 review emphasizes that these models are complementary but mutation- and cell-type-specific. They are useful for studying complex-I energy failure and screening therapies, but findings—such as mTOR inhibition in Ndufs4−/− mice—must not be treated as NDUFB8 efficacy evidence. (NCT06843811 chunk 1, NCT06843811 chunk 2)

## Current assessment

As of the 2023–2024 literature, the central conclusion has not changed: MC1DN32 is a genetically and functionally well-supported but clinically under-characterized NDUFB8 disorder. The strongest current applications are **genomics-first diagnosis, RNA confirmation of splice effects, functional respiratory-chain validation, cascade/reproductive testing, and multidisciplinary supportive care**. The major research priorities are additional case ascertainment, longitudinal natural history, standardized HPO phenotyping, disease-specific iPSC/neural and cardiac models, and inclusion of molecularly stratified NDUFB8 patients in LSS trials.

References

1. (piekutowskaabramczuk2018ndufb8mutationscause pages 6-7): Dorota Piekutowska-Abramczuk, Zahra Assouline, Lavinija Mataković, René G. Feichtinger, Eliška Koňařiková, Elżbieta Jurkiewicz, Piotr Stawiński, Mirjana Gusic, Andreas Koller, Agnieszka Pollak, Piotr Gasperowicz, Joanna Trubicka, Elżbieta Ciara, Katarzyna Iwanicka-Pronicka, Dariusz Rokicki, Sylvain Hanein, Saskia B. Wortmann, Wolfgang Sperl, Agnès Rötig, Holger Prokisch, Ewa Pronicka, Rafał Płoski, Giulia Barcia, and Johannes A. Mayr. Ndufb8 mutations cause mitochondrial complex i deficiency in individuals with leigh-like encephalomyopathy. American journal of human genetics, 102 3:460-467, Mar 2018. URL: https://doi.org/10.1016/j.ajhg.2018.01.008, doi:10.1016/j.ajhg.2018.01.008. This article has 86 citations and is from a highest quality peer-reviewed journal.

2. (piekutowskaabramczuk2018ndufb8mutationscause pages 4-5): Dorota Piekutowska-Abramczuk, Zahra Assouline, Lavinija Mataković, René G. Feichtinger, Eliška Koňařiková, Elżbieta Jurkiewicz, Piotr Stawiński, Mirjana Gusic, Andreas Koller, Agnieszka Pollak, Piotr Gasperowicz, Joanna Trubicka, Elżbieta Ciara, Katarzyna Iwanicka-Pronicka, Dariusz Rokicki, Sylvain Hanein, Saskia B. Wortmann, Wolfgang Sperl, Agnès Rötig, Holger Prokisch, Ewa Pronicka, Rafał Płoski, Giulia Barcia, and Johannes A. Mayr. Ndufb8 mutations cause mitochondrial complex i deficiency in individuals with leigh-like encephalomyopathy. American journal of human genetics, 102 3:460-467, Mar 2018. URL: https://doi.org/10.1016/j.ajhg.2018.01.008, doi:10.1016/j.ajhg.2018.01.008. This article has 86 citations and is from a highest quality peer-reviewed journal.

3. (piekutowskaabramczuk2018ndufb8mutationscause pages 1-2): Dorota Piekutowska-Abramczuk, Zahra Assouline, Lavinija Mataković, René G. Feichtinger, Eliška Koňařiková, Elżbieta Jurkiewicz, Piotr Stawiński, Mirjana Gusic, Andreas Koller, Agnieszka Pollak, Piotr Gasperowicz, Joanna Trubicka, Elżbieta Ciara, Katarzyna Iwanicka-Pronicka, Dariusz Rokicki, Sylvain Hanein, Saskia B. Wortmann, Wolfgang Sperl, Agnès Rötig, Holger Prokisch, Ewa Pronicka, Rafał Płoski, Giulia Barcia, and Johannes A. Mayr. Ndufb8 mutations cause mitochondrial complex i deficiency in individuals with leigh-like encephalomyopathy. American journal of human genetics, 102 3:460-467, Mar 2018. URL: https://doi.org/10.1016/j.ajhg.2018.01.008, doi:10.1016/j.ajhg.2018.01.008. This article has 86 citations and is from a highest quality peer-reviewed journal.

4. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 32): Open Targets Query (Mitochondrial complex I deficiency, nuclear type 32, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (piekutowskaabramczuk2018ndufb8mutationscause pages 2-4): Dorota Piekutowska-Abramczuk, Zahra Assouline, Lavinija Mataković, René G. Feichtinger, Eliška Koňařiková, Elżbieta Jurkiewicz, Piotr Stawiński, Mirjana Gusic, Andreas Koller, Agnieszka Pollak, Piotr Gasperowicz, Joanna Trubicka, Elżbieta Ciara, Katarzyna Iwanicka-Pronicka, Dariusz Rokicki, Sylvain Hanein, Saskia B. Wortmann, Wolfgang Sperl, Agnès Rötig, Holger Prokisch, Ewa Pronicka, Rafał Płoski, Giulia Barcia, and Johannes A. Mayr. Ndufb8 mutations cause mitochondrial complex i deficiency in individuals with leigh-like encephalomyopathy. American journal of human genetics, 102 3:460-467, Mar 2018. URL: https://doi.org/10.1016/j.ajhg.2018.01.008, doi:10.1016/j.ajhg.2018.01.008. This article has 86 citations and is from a highest quality peer-reviewed journal.

6. (piekutowskaabramczuk2018ndufb8mutationscause pages 5-6): Dorota Piekutowska-Abramczuk, Zahra Assouline, Lavinija Mataković, René G. Feichtinger, Eliška Koňařiková, Elżbieta Jurkiewicz, Piotr Stawiński, Mirjana Gusic, Andreas Koller, Agnieszka Pollak, Piotr Gasperowicz, Joanna Trubicka, Elżbieta Ciara, Katarzyna Iwanicka-Pronicka, Dariusz Rokicki, Sylvain Hanein, Saskia B. Wortmann, Wolfgang Sperl, Agnès Rötig, Holger Prokisch, Ewa Pronicka, Rafał Płoski, Giulia Barcia, and Johannes A. Mayr. Ndufb8 mutations cause mitochondrial complex i deficiency in individuals with leigh-like encephalomyopathy. American journal of human genetics, 102 3:460-467, Mar 2018. URL: https://doi.org/10.1016/j.ajhg.2018.01.008, doi:10.1016/j.ajhg.2018.01.008. This article has 86 citations and is from a highest quality peer-reviewed journal.

7. (shen2025thepathto pages 1-2): Lishuang Shen. The path to precision medicine in leigh syndrome spectrum: a four-decade chronicle of genetic discovery and targeted treatment. Frontiers in Bioscience-Scholar, 17(4):45427, Dec 2025. URL: https://doi.org/10.31083/fbs45427, doi:10.31083/fbs45427. This article has 2 citations.

8. (parikh2015diagnosisandmanagement pages 8-9): Sumit Parikh, Amy Goldstein, Mary Kay Koenig, Fernando Scaglia, Gregory M. Enns, Russell Saneto, Irina Anselm, Bruce H. Cohen, Marni J. Falk, Carol Greene, Andrea L. Gropman, Richard Haas, Michio Hirano, Phil Morgan, Katherine Sims, Mark Tarnopolsky, Johan L.K. Van Hove, Lynne Wolfe, and Salvatore DiMauro. Diagnosis and management of mitochondrial disease: a consensus statement from the mitochondrial medicine society. Sep 2015. URL: https://doi.org/10.1038/gim.2014.177, doi:10.1038/gim.2014.177. This article has 571 citations and is from a highest quality peer-reviewed journal.

9. (NCT06843811 chunk 1): Matthew Demczko. Sirolimus for Leigh Syndrome. Matthew Demczko. 2025. ClinicalTrials.gov Identifier: NCT06843811

10. (NCT02352896 chunk 1):  Long-Term Safety and Efficacy Evaluation of EPI-743 in Children With Leigh Syndrome. PTC Therapeutics. 2014. ClinicalTrials.gov Identifier: NCT02352896

11. (dang2020analysisofhuman pages 25-27): Quynh-Chi L. Dang, Duong H. Phan, Abigail N. Johnson, Mukund Pasapuleti, Hind A. Alkhaldi, Fang Zhang, and Steven B. Vik. Analysis of human mutations in the supernumerary subunits of complex i. Nov 2020. URL: https://doi.org/10.3390/life10110296, doi:10.3390/life10110296. This article has 27 citations.

12. (NCT05162768 chunk 2):  Study to Evaluate Efficacy and Safety of Elamipretide in Subjects With Primary Mitochondrial Disease From Nuclear DNA Mutations (nPMD). Stealth BioTherapeutics Inc.. 2022. ClinicalTrials.gov Identifier: NCT05162768

13. (NCT06843811 chunk 3): Matthew Demczko. Sirolimus for Leigh Syndrome. Matthew Demczko. 2025. ClinicalTrials.gov Identifier: NCT06843811

14. (sue2022patientcarestandards pages 17-21): Carolyn M. Sue, Shanti Balasubramaniam, Drago Bratkovic, Catherine Bonifant, John Christodoulou, David Coman, Karen Crawley, Fabienne Edema‐Hildebrand, Carolyn Ellaway, Roula Ghaoui, Maina Kava, Lisa S. Kearns, Joy Lee, Christina Liang, David A. Mackey, Sean Murray, Merrilee Needham, Rocio Rius, Jacqui Russell, Nicholas J.C. Smith, Dominic Thyagarajan, and Christine Wools. Patient care standards for primary mitochondrial disease in australia: an australian adaptation of the mitochondrial medicine society recommendations. Nov 2022. URL: https://doi.org/10.1111/imj.15505, doi:10.1111/imj.15505. This article has 17 citations and is from a peer-reviewed journal.

15. (sue2022patientcarestandards pages 4-7): Carolyn M. Sue, Shanti Balasubramaniam, Drago Bratkovic, Catherine Bonifant, John Christodoulou, David Coman, Karen Crawley, Fabienne Edema‐Hildebrand, Carolyn Ellaway, Roula Ghaoui, Maina Kava, Lisa S. Kearns, Joy Lee, Christina Liang, David A. Mackey, Sean Murray, Merrilee Needham, Rocio Rius, Jacqui Russell, Nicholas J.C. Smith, Dominic Thyagarajan, and Christine Wools. Patient care standards for primary mitochondrial disease in australia: an australian adaptation of the mitochondrial medicine society recommendations. Nov 2022. URL: https://doi.org/10.1111/imj.15505, doi:10.1111/imj.15505. This article has 17 citations and is from a peer-reviewed journal.

16. (sue2022patientcarestandards pages 24-26): Carolyn M. Sue, Shanti Balasubramaniam, Drago Bratkovic, Catherine Bonifant, John Christodoulou, David Coman, Karen Crawley, Fabienne Edema‐Hildebrand, Carolyn Ellaway, Roula Ghaoui, Maina Kava, Lisa S. Kearns, Joy Lee, Christina Liang, David A. Mackey, Sean Murray, Merrilee Needham, Rocio Rius, Jacqui Russell, Nicholas J.C. Smith, Dominic Thyagarajan, and Christine Wools. Patient care standards for primary mitochondrial disease in australia: an australian adaptation of the mitochondrial medicine society recommendations. Nov 2022. URL: https://doi.org/10.1111/imj.15505, doi:10.1111/imj.15505. This article has 17 citations and is from a peer-reviewed journal.

17. (mccormick2023expertpanelcuration pages 7-9): E. McCormick, Kierstin N. Keller, Julie Taylor, A. Coffey, Lishuang Shen, D. Krotoski, B. Harding, C. Alves, A. Ardissone, Renkui Bai, I.P. de Barcelos, E. Bertini, Krista K. Bluske, J. Christodoulou, Amanda R. Clause, W. Copeland, G. Diaz, D. Diodato, M. Dulik, G. Enns, A. Feigenbaum, C. Fratter, D. Ghezzi, A. Goldstein, A. Gropman, R. Haas, A. Karaa, M. Koenig, B. Monteleone, S. Parikh, B. P. Dueñas, Revathi Rajkumar, Ann Saada, R. Saneto, K. Sergeant, J. Shoffner, Conrad Smith, C. Stanley, Isabelle Thiffault, D. Thorburn, M. Walker, D. Wallace, L. Wong, Xiaowu Gai, Marni J. Falk, Z. Zolkipli-Cunningham, and S. Rahman. Expert panel curation of 113 primary mitochondrial disease genes for the leigh syndrome spectrum. Aug 2023. URL: https://doi.org/10.1002/ana.26716, doi:10.1002/ana.26716. This article has 73 citations and is from a highest quality peer-reviewed journal.

18. (mccormick2023expertpanelcuration pages 9-10): E. McCormick, Kierstin N. Keller, Julie Taylor, A. Coffey, Lishuang Shen, D. Krotoski, B. Harding, C. Alves, A. Ardissone, Renkui Bai, I.P. de Barcelos, E. Bertini, Krista K. Bluske, J. Christodoulou, Amanda R. Clause, W. Copeland, G. Diaz, D. Diodato, M. Dulik, G. Enns, A. Feigenbaum, C. Fratter, D. Ghezzi, A. Goldstein, A. Gropman, R. Haas, A. Karaa, M. Koenig, B. Monteleone, S. Parikh, B. P. Dueñas, Revathi Rajkumar, Ann Saada, R. Saneto, K. Sergeant, J. Shoffner, Conrad Smith, C. Stanley, Isabelle Thiffault, D. Thorburn, M. Walker, D. Wallace, L. Wong, Xiaowu Gai, Marni J. Falk, Z. Zolkipli-Cunningham, and S. Rahman. Expert panel curation of 113 primary mitochondrial disease genes for the leigh syndrome spectrum. Aug 2023. URL: https://doi.org/10.1002/ana.26716, doi:10.1002/ana.26716. This article has 73 citations and is from a highest quality peer-reviewed journal.

19. (baldo2024acomprehensiveapproach pages 2-4): Manuela Schubert Baldo, Luísa Azevedo, Margarida Paiva Coelho, Esmeralda Martins, and Laura Vilarinho. A comprehensive approach to the diagnosis of leigh syndrome spectrum. Diagnostics, 14:2133, Sep 2024. URL: https://doi.org/10.3390/diagnostics14192133, doi:10.3390/diagnostics14192133. This article has 3 citations.

20. (baldo2024acomprehensiveapproach pages 1-2): Manuela Schubert Baldo, Luísa Azevedo, Margarida Paiva Coelho, Esmeralda Martins, and Laura Vilarinho. A comprehensive approach to the diagnosis of leigh syndrome spectrum. Diagnostics, 14:2133, Sep 2024. URL: https://doi.org/10.3390/diagnostics14192133, doi:10.3390/diagnostics14192133. This article has 3 citations.

21. (baldo2024acomprehensiveapproach pages 6-8): Manuela Schubert Baldo, Luísa Azevedo, Margarida Paiva Coelho, Esmeralda Martins, and Laura Vilarinho. A comprehensive approach to the diagnosis of leigh syndrome spectrum. Diagnostics, 14:2133, Sep 2024. URL: https://doi.org/10.3390/diagnostics14192133, doi:10.3390/diagnostics14192133. This article has 3 citations.

22. (baldo2024acomprehensiveapproach pages 4-6): Manuela Schubert Baldo, Luísa Azevedo, Margarida Paiva Coelho, Esmeralda Martins, and Laura Vilarinho. A comprehensive approach to the diagnosis of leigh syndrome spectrum. Diagnostics, 14:2133, Sep 2024. URL: https://doi.org/10.3390/diagnostics14192133, doi:10.3390/diagnostics14192133. This article has 3 citations.

23. (mavraki2023genetictestingfor pages 1-2): Eleni Mavraki, Robyn Labrum, Kate Sergeant, Charlotte L. Alston, Cathy Woodward, Conrad Smith, Charlotte V. Y. Knowles, Yogen Patel, Philip Hodsdon, Jack P. Baines, Emma L. Blakely, James Polke, Robert W. Taylor, and Carl Fratter. Genetic testing for mitochondrial disease: the united kingdom best practice guidelines. European Journal of Human Genetics, 31:148-163, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01249-w, doi:10.1038/s41431-022-01249-w. This article has 100 citations and is from a domain leading peer-reviewed journal.

24. (NCT06843811 chunk 2): Matthew Demczko. Sirolimus for Leigh Syndrome. Matthew Demczko. 2025. ClinicalTrials.gov Identifier: NCT06843811

25. (sue2022patientcarestandards pages 26-28): Carolyn M. Sue, Shanti Balasubramaniam, Drago Bratkovic, Catherine Bonifant, John Christodoulou, David Coman, Karen Crawley, Fabienne Edema‐Hildebrand, Carolyn Ellaway, Roula Ghaoui, Maina Kava, Lisa S. Kearns, Joy Lee, Christina Liang, David A. Mackey, Sean Murray, Merrilee Needham, Rocio Rius, Jacqui Russell, Nicholas J.C. Smith, Dominic Thyagarajan, and Christine Wools. Patient care standards for primary mitochondrial disease in australia: an australian adaptation of the mitochondrial medicine society recommendations. Nov 2022. URL: https://doi.org/10.1111/imj.15505, doi:10.1111/imj.15505. This article has 17 citations and is from a peer-reviewed journal.

26. (NCT01721733 chunk 1):  Safety and Efficacy Study of EPI-743 in Children With Leigh Syndrome. PTC Therapeutics. 2012. ClinicalTrials.gov Identifier: NCT01721733

27. (NCT04378075 chunk 1):  A Study to Evaluate Efficacy and Safety of Vatiquinone for Treating Mitochondrial Disease in Participants With Refractory Epilepsy. PTC Therapeutics. 2020. ClinicalTrials.gov Identifier: NCT04378075

28. (NCT05162768 chunk 1):  Study to Evaluate Efficacy and Safety of Elamipretide in Subjects With Primary Mitochondrial Disease From Nuclear DNA Mutations (nPMD). Stealth BioTherapeutics Inc.. 2022. ClinicalTrials.gov Identifier: NCT05162768

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_32-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032635` (4 mentions) - the report calls it "if available"; MONDO calls it **mitochondrial complex I deficiency, nuclear type 32**
