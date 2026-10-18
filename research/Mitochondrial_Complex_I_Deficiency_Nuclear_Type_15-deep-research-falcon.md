---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-17T10:25:03.969335'
end_time: '2026-09-17T10:40:53.846763'
duration_seconds: 949.88
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Mitochondrial Complex I Deficiency, Nuclear Type 15
  mondo_id: MONDO:0032620
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
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 31
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032620
    reported_labels:
    - if available
    - Mitochondrial complex I deficiency, nuclear type 15
    ontology_label: mitochondrial complex I deficiency, nuclear type 15
  obsolete_terms:
  - term_id: GO:0005747
    ontology_label: obsolete mitochondrial respiratory chain complex I
    replaced_by: GO:0045271
  unresolvable_prefixes:
  - NCBI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_15-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 15
- **MONDO ID:** MONDO:0032620 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 15** covering all of the
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
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 15
- **MONDO ID:** MONDO:0032620 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 15** covering all of the
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


# Mitochondrial Complex I Deficiency, Nuclear Type 15

## Executive summary and evidence limits

Mitochondrial complex I deficiency, nuclear type 15 is an ultra-rare autosomal-recessive oxidative-phosphorylation disorder caused by biallelic pathogenic variants in **NDUFAF4**, formerly **C6ORF66**. NDUFAF4 is a mitochondrial assembly factor rather than a structural complex-I subunit. Loss of its function impairs modular assembly of NADH:ubiquinone oxidoreductase (complex I), reducing electron transfer, proton pumping, and ATP-generating capacity. The reported clinical spectrum lies within severe pediatric mitochondrial encephalomyopathy/Leigh-spectrum disease. However, disease-specific human evidence is exceptionally sparse: most detailed data derive from three affected relatives carrying the same homozygous missense variant and from their cultured fibroblasts. Consequently, phenotype percentages, prevalence, survival estimates, penetrance, and genotype–phenotype rules cannot be estimated reliably. Open Targets currently maps MONDO:0032620 to one causal target, **NDUFAF4** (ENSG00000123545), supported by five aggregated evidence records. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 15)

| Evidence domain | Key finding | Evidence type/model | Quantitative detail | Citation bibliographic pointer | Limitation |
|---|---|---|---|---|---|
| Disease mapping | Mitochondrial complex I deficiency, nuclear type 15 (MONDO:0032620) maps to **biallelic NDUFAF4** deficiency; NDUFAF4 was formerly called **C6ORF66/HRPA20** and encodes a complex I assembly factor. | Aggregated disease–target databases plus human genetics | One associated causal target, **NDUFAF4** (ENSG00000123545); Open Targets aggregates five evidence records. | Original C6ORF66 report: PMID **18179882**, *Am J Hum Genet.*, January 2008; current disease–target mapping (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 15, diaz2011mitochondrialdisorderscaused pages 12-13) | Database score is not an independent clinical cohort; historical nomenclature and OMIM identifiers may differ among resources. |
| Human genotype/cell lines | Three affected relatives—fibroblast lines **F528, F334, and F511**—were homozygous for **NDUFAF4 c.194T>C (p.Leu65Pro)**. | Human familial cases and primary dermal fibroblasts | Three affected individuals from one family; all homozygous for the same missense variant. | Saada et al., *Am J Hum Genet.*, 2008, PMID **18179882**; Marcus et al., *Molecular Medicine*, published online May 8, 2013, DOI **10.2119/molmed.2012.00343** (marcus2013replacementofthe pages 2-3, nouws2012assemblyfactorsas pages 6-7) | Extremely small, related sample; percentages derived from these cases cannot be generalized to all NDUFAF4 disease. |
| Biochemical defect | The p.Leu65Pro lesion causes defective complex I assembly, accumulation of stalled intermediates, and markedly reduced complex I activity. | Patient muscle mitochondria and fibroblasts | Patient muscle retained approximately **30% residual mature complex I**; all three fibroblast lines showed impaired activity with inter-individual variability. | Saada et al., 2008, PMID **18179882**; Marcus et al., 2013, DOI **10.2119/molmed.2012.00343** (marcus2013replacementofthe pages 1-2, marcus2013replacementofthe pages 5-7) | Exact residual enzyme activities vary by tissue and assay; fibroblast severity may not predict brain, heart, or muscle disease. |
| Causal complementation/protein replacement | Mitochondria-targeted wild-type **TAT–NDUFAF4** entered patient cells and mitochondria and selectively improved complex I function, supporting loss of assembly-factor function as causal. | In-vitro protein replacement in primary patient fibroblasts/isolated mitochondria | Isolated F528 mitochondria: **59–92% increase** in complex I activity; cultured cells: **46%** restoration in F528, approximately **20%** increase in F334, and **23%** increase in F511; optimized conditions produced **20–50%** increases. | Marcus et al., *Molecular Medicine*, 2013, DOI **10.2119/molmed.2012.00343** (marcus2013replacementofthe pages 5-7, marcus2013replacementofthe pages 7-9) | Preclinical cell study only; no pharmacokinetic, blood–brain-barrier, immunogenicity, animal efficacy, or human safety evidence. |
| Cellular bioenergetic rescue | TAT–NDUFAF4 improved OXPHOS-dependent growth and ATP efficiency and reduced oxidative stress in patient cells. | In-vitro patient fibroblasts in glucose-free medium | Cell proliferation increased **25%**; mitochondrial content decreased **23%**; ATP normalized to mitochondrial content increased **25%**; free-radical level decreased approximately **25%**. | Marcus et al., 2013, DOI **10.2119/molmed.2012.00343** (marcus2013replacementofthe pages 7-9) | Surrogate cellular outcomes with short exposure and no demonstration of clinical benefit. |
| Modular assembly mechanism | NDUFAF4 disruption impairs assembly of complex I **Q, N, and PP-b modules**, reduces incorporation of NDUFS3, NDUFV3, and NDUFS5, destabilizes TIMMDC1 in assembly intermediates, and raises ROS. | In-vivo Drosophila muscle-specific RNAi, BN-PAGE, activity assays, immunoblotting, and proteomics | Residual assembled complex I in NDUFAF4-knockdown thoraces was approximately **50% of wild type**; ROS assays used three biological replicates with **40 flies per replicate**. | Murari et al., *iScience*, August 20, 2021, DOI **10.1016/j.isci.2021.102869** (murari2021dissectingtheconcordant pages 1-2, murari2021dissectingtheconcordant pages 2-5, murari2021dissectingtheconcordant pages 5-8, murari2021dissectingtheconcordant pages 8-9) | Knockdown is not the human p.Leu65Pro genotype; flight muscle may not reproduce human CNS or cardiac pathology. |
| Small-molecule screening | **AICAR** was the most consistently beneficial compound in a mixed-genotype complex I-deficient fibroblast screen, improving growth/ATP and reducing ROS through an AMPK-associated response. | In-vitro screening of primary fibroblasts from genetically heterogeneous complex I deficiency cases, including NDUFAF4 | Ten compounds tested in seven patient lines; AICAR showed favorable effects in **5 of 6 evaluable patient lines** at **0.5 mM for 72 hours**. | Golubitzky et al., *PLoS ONE*, October 26, 2011, DOI **10.1371/journal.pone.0026883** (golubitzky2011screeningforactive pages 1-2, golubitzky2011screeningforactive pages 6-7) | Results were pooled across different genes; the evidence does not establish NDUFAF4-specific efficacy or clinical safety. |
| Clinical translation/trials | No approved disease-modifying therapy or registered **NDUFAF4-specific** interventional trial was identified; available studies concern broader Leigh syndrome or mitochondrial-disease populations. | ClinicalTrials.gov search and literature review | Gene-specific trials found: **0**; broader Leigh trials include phase 2 studies, but eligibility or benefit for NDUFAF4 disease is unproven. | ClinicalTrials.gov search current to September 17, 2026; historical reviews report no curative therapy (nouws2012assemblyfactorsas pages 1-2, nouws2012assemblyfactorsas pages 8-9) | Registry status changes over time; absence of a gene-specific trial does not exclude enrollment in genotype-agnostic mitochondrial studies. |


*Table: Evidence ranges from three related human cases and patient-cell complementation to in-vivo Drosophila mechanism studies. It also highlights the major translational limitation: no NDUFAF4-specific clinical trial or approved disease-modifying treatment.*

## 1. Disease information

### Definition

The disorder is a nuclear-encoded mitochondrial respiratory-chain disease in which defective NDUFAF4 prevents normal assembly of complex I. Complex I is the first and largest oxidative-phosphorylation complex: it oxidizes NADH, transfers electrons through iron–sulfur centers to ubiquinone, and couples this transfer to proton translocation across the inner mitochondrial membrane. The resulting electrochemical gradient powers ATP synthase. Complex-I dysfunction can therefore disturb ATP production, oxygen consumption, redox and calcium homeostasis, increase reactive oxygen species (ROS), promote lactate accumulation, and activate cell-death pathways. (nouws2012assemblyfactorsas pages 1-2)

### Identifiers and names

- **MONDO:** MONDO:0032620.
- **Causal gene:** **NDUFAF4**, *NADH:ubiquinone oxidoreductase complex assembly factor 4*; Ensembl ENSG00000123545. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 15)
- **Gene aliases:** **C6ORF66**, **HRPA20**; “NADH dehydrogenase [ubiquinone] complex I assembly factor 4.” (marcus2013replacementofthe pages 1-2)
- **Disease synonyms:** mitochondrial complex I deficiency, nuclear type 15; NDUFAF4-related mitochondrial complex I deficiency; C6ORF66-related complex I deficiency; NDUFAF4-related Leigh syndrome/encephalomyopathy.
- **OMIM:** Secondary reviews associate NDUFAF4 with **OMIM 611776** and disease entry **618237**; older literature also uses the umbrella biochemical phenotype “complex I deficiency,” OMIM 252010. Because historical tables vary in whether they cite the gene or phenotype entry, these identifiers should be verified directly in the current OMIM release before database ingestion. (rodenburg2016mitochondrialcomplexilinked pages 21-23, fernandez‐vizarra2021mitochondrialdisordersof pages 96-99)
- **Orphanet:** No confidently disease-specific Orphanet identifier was recovered; the condition may be nested under mitochondrial complex-I deficiency or Leigh syndrome.
- **ICD-10/ICD-11 and MeSH:** No dedicated subtype code or heading was identified. Coding ordinarily uses broader mitochondrial-metabolism/mitochondrial-disease or Leigh-syndrome categories.

The report is synthesized from **aggregated disease resources and published family/cell studies**, not individual EHR records.

## 2. Etiology

### Causal factor and genetic risk

The established cause is **biallelic germline NDUFAF4 dysfunction**. The best-characterized allele is **NM-reference c.194T>C, p.(Leu65Pro)**, homozygous in affected individuals F511, F334, and F528 from one family. The replacement study states directly: “The patients carry a mutation in the second exon … with a T/C substitution at nucleotide 194 that predicts an Leu65Pro mutation. All of the patients were homozygous.” (marcus2013replacementofthe pages 2-3)

The variant is a missense substitution and behaves functionally as a loss-of-function/hypomorphic assembly-factor allele: patient muscle retained only about 30% mature complex I, stalled intermediates accumulated, and provision of wild-type NDUFAF4 improved complex-I activity. (marcus2013replacementofthe pages 1-2, marcus2013replacementofthe pages 5-7)

A 2016 review listed two NDUFAF4 mutations, but the retrieved evidence did not permit secure reconstruction of the second allele. No disease-specific structural variant, copy-number variant, somatic variant, susceptibility locus, or validated modifier gene was established. (rodenburg2016mitochondrialcomplexilinked pages 21-23)

### Population frequency and variant classification

The retrieved papers do not provide a modern gnomAD allele frequency or current ClinVar ACMG classification for c.194T>C. It should be classified in a production database only after checking the current ClinVar submission record, transcript version, population frequency, segregation, computational evidence, and functional studies. Strong supporting evidence includes homozygosity in affected relatives, segregation, severe biochemical deficiency, abnormal assembly, and rescue by wild-type protein. No somatic origin is implicated.

### Environmental, infectious, and lifestyle factors

No toxin, pathogen, radiation, smoking, alcohol, occupation, diet, sex, or age exposure causes this Mendelian disorder. Intercurrent infection, fasting, dehydration, surgery, or other catabolic stress may plausibly precipitate decompensation in mitochondrial disease, but this has not been demonstrated specifically for NDUFAF4 deficiency. Such exposures are **course modifiers**, not etiologic causes.

### Protective factors and gene–environment interaction

No validated protective allele, modifier gene, diet, supplement, or lifestyle exposure is known. Avoiding prolonged fasting and rapidly treating fever, dehydration, and infection are prudent mitochondrial-care measures, but they have not been shown to prevent NDUFAF4 disease. Variation among siblings with the same mutation indicates variable expressivity and suggests unmeasured genetic, developmental, or environmental modifiers; the review explicitly notes “considerable difference in the development of symptoms” among siblings with the same NDUFAF4 mutation. (nouws2012assemblyfactorsas pages 4-6)

## 3. Phenotypes

Because the ascertainable disease-specific cohort comprises only three related individuals, frequencies below should be treated as **reported/not reported**, not population percentages.

- **Developmental or motor delay** — clinical sign; childhood onset and variable progression in the available family. Suggested HPO: **Global developmental delay HP:0001263**, **Delayed motor development HP:0001270**. (nouws2012assemblyfactorsas pages 6-7)
- **Exercise intolerance** — symptom of impaired muscular oxidative capacity; severity appears variable. Suggested HPO: **Exercise intolerance HP:0003546**. (nouws2012assemblyfactorsas pages 6-7)
- **Encephalomyopathy/Leigh-spectrum disease** — progressive neurologic and muscular involvement is reported at the disease level. Suggested HPO: **Encephalopathy HP:0001298**, **Muscular hypotonia HP:0001252**, and, only when documented by imaging, **Bilateral basal-ganglia lesions HP:0007146**. NDUFAF4 reviews associate the gene with leukodystrophy/Leigh syndrome, encephalomyopathy, and severe neonatal disease. (rodenburg2016mitochondrialcomplexilinked pages 21-23, fernandez‐vizarra2021mitochondrialdisordersof pages 96-99)
- **Lactic acidosis/elevated lactate** — biochemical phenotype expected from impaired NADH oxidation and compensatory glycolysis and included in review-level NDUFAF4 phenotype summaries. Suggested HPO: **Lactic acidosis HP:0003128**, **Increased serum lactate HP:0002151**. Patient-specific values were not recovered. (nouws2012assemblyfactorsas pages 1-2, fernandez‐vizarra2021mitochondrialdisordersof pages 96-99)
- **Isolated complex-I enzymatic deficiency** — laboratory abnormality and central defining phenotype. Suggested HPO: **Decreased mitochondrial complex I activity HP:0011923**. All three tested fibroblast cultures had impaired activity, with inter-individual variability; muscle retained approximately 30% mature complex I. (marcus2013replacementofthe pages 1-2, marcus2013replacementofthe pages 5-7)
- **Cardiomyopathy** — reported in disease-level summaries but not securely assignable to each of the three original individuals. Suggested HPO: **Cardiomyopathy HP:0001638**; subtype should not be asserted without the original clinical record. (fernandez‐vizarra2021mitochondrialdisordersof pages 96-99)
- **Severe neonatal/infantile course and early death** — older literature describes pathogenic C6ORF66 mutations as causing “fatal neonatal mitochondrial disease,” although the accessible sources do not provide dependable patient-by-patient ages at death. Suggested HPO: **Neonatal onset HP:0003623**, **Infantile onset HP:0003593**. (marcus2013replacementofthe pages 1-2)

No validated disease-specific behavioral phenotype, formal neuropsychological profile, pain measure, EQ-5D/SF-36/PROMIS score, or per-phenotype quality-of-life statistic is available. Motor delay, exercise intolerance, encephalopathy, and cardiomyopathy would be expected to impair mobility, feeding, communication, schooling, and independence, but this is clinical inference rather than measured NDUFAF4-specific evidence.

## 4. Genetic and molecular information

**NDUFAF4** encodes a nuclear protein with an N-terminal mitochondrial targeting sequence; the first 34 residues were predicted to constitute this targeting sequence. The mature protein localizes to mitochondria and transiently participates in complex-I biogenesis rather than remaining a stoichiometric component of the final holoenzyme. (marcus2013replacementofthe pages 1-2)

The p.Leu65Pro allele likely destabilizes protein conformation or assembly-factor interactions; direct structural evidence for that specific amino-acid substitution was not found. NDUFAF4 interacts closely with NDUFAF3 and co-migrates with Q-module components NDUFS2, NDUFS3, NDUFS7, NDUFS8, and NDUFA5. (murari2021dissectingtheconcordant pages 2-5)

No validated NDUFAF4 disease-specific DNA-methylation signature, histone alteration, chromatin mechanism, repeat expansion, aneuploidy, translocation, or inversion is known. No established modifier gene exists. **TIMMDC1** is a mechanistic interaction partner rather than a proven clinical modifier: NDUFAF4 disruption reduces TIMMDC1 in assembly intermediates, but TIMMDC1 overexpression did not rescue NDUFAF4 knockdown in flies. (murari2021dissectingtheconcordant pages 14-16)

## 5. Environmental information

The disease is not infectious, transmissible, toxicant-induced, or behaviorally acquired. No relevant pathogen taxonomy or environmental chemical association was identified. General mitochondrial-toxic medications and prolonged catabolic stress warrant individualized specialist review, but no NDUFAF4-specific adverse-exposure dataset exists. Ordinary vaccination does not prevent the genetic defect; routine immunization may indirectly reduce infection-triggered metabolic stress when clinically appropriate.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic NDUFAF4 variants lead to** deficient or dysfunctional mitochondrial NDUFAF4 assembly-factor activity.
2. **Deficient NDUFAF4 leads to** impaired stabilization and maturation of complex-I assembly intermediates, especially incorporation of NDUFS3 into the Q module and NDUFS5 into the proximal membrane PP-b module, with impaired N-module biogenesis and reduced TIMMDC1 association. This step is demonstrated in Drosophila RNAi and supported by human patient assembly studies. (murari2021dissectingtheconcordant pages 2-5, murari2021dissectingtheconcordant pages 5-8, murari2021dissectingtheconcordant pages 8-9)
3. **Defective modular assembly results in** accumulation of stalled intermediates and reduced mature complex-I holoenzyme; patient muscle retained about 30% mature complex I. (marcus2013replacementofthe pages 1-2)
4. **Reduced mature complex I leads to** reduced NADH oxidation, electron transfer to ubiquinone, proton translocation, and respiratory-chain flux.
5. **Reduced respiratory flux results in two principal branches:**
   - **Energy branch:** reduced proton motive force leads to impaired ATP synthesis, which results in energy failure in neurons, cardiomyocytes, and skeletal muscle fibers.
   - **Redox/metabolic branch:** elevated NADH pressure and electron leak lead to compensatory glycolysis/lactate production and increased ROS; ROS and redox imbalance can result in membrane, protein, and DNA injury and apoptosis. The downstream human tissue injury is biologically supported but partly inferred for this specific genotype. (nouws2012assemblyfactorsas pages 1-2, murari2021dissectingtheconcordant pages 5-8)
6. **Energy failure and oxidative/metabolic stress lead to** dysfunction and degeneration of high-energy tissues, resulting in developmental delay, encephalopathy/Leigh-spectrum manifestations, exercise intolerance/myopathy, lactic acidosis, and possible cardiomyopathy.

### Molecular and cellular detail

Complex I is assembled stepwise in modules. The N module oxidizes NADH; the Q module transfers electrons through iron–sulfur centers to ubiquinone; and the membrane P module pumps protons. Current structural understanding supports modular, stepwise assembly, and a 2024 cryo-EM review emphasized that complex-I assembly mirrors this modular architecture. NDUFAF4 is assigned principally to peripheral-arm/Q-module assembly, although functional knockdown reveals broader secondary effects on N and PP-b modules. (murari2021dissectingtheconcordant pages 2-5, fernandez‐vizarra2021mitochondrialdisordersof pages 96-99)

In Drosophila flight muscle, NDUFAF4 knockdown reduced holoenzyme assembly and in-gel complex-I activity, increased ROS, decreased NDUFS3, NDUFV3, and NDUFS5 incorporation, and caused accumulation of membrane-domain intermediates. Residual assembled complex I was approximately 50% of wild type. Complexes II and IV showed increased activity, interpreted as compensatory adaptation rather than primary deficiency. (murari2021dissectingtheconcordant pages 5-8, murari2021dissectingtheconcordant pages 8-9)

Suggested GO annotations include **mitochondrial respiratory chain complex I assembly GO:0032981**, **mitochondrial electron transport, NADH to ubiquinone GO:0006120**, **oxidative phosphorylation GO:0006119**, **ATP metabolic process GO:0046034**, **proton transmembrane transport GO:1902600**, **cellular response to oxidative stress GO:0034599**, and **reactive oxygen species metabolic process GO:0072593**. Relevant cellular compartments are **mitochondrion GO:0005739**, **mitochondrial inner membrane GO:0005743**, **mitochondrial matrix GO:0005759**, and **respiratory-chain complex I GO:0005747**.

Suggested Cell Ontology classes—based on vulnerable tissue biology rather than direct single-cell data—include **neuron CL:0000540**, **cardiac muscle cell CL:0000746**, and **skeletal muscle fiber CL:0008002**. No NDUFAF4-specific single-cell, spatial-transcriptomic, epigenomic, lipidomic, patient-tissue transcriptomic, or integrated multi-omic study was found.

## 7. Anatomical structures affected

The principal system is the **central nervous system**, with secondary skeletal-muscle and possible cardiac involvement. Suggested anatomy terms include **brain UBERON:0000955**, **basal ganglion UBERON:0002420** where Leigh-pattern lesions are demonstrated, **brainstem UBERON:0002298**, **skeletal muscle organ UBERON:0001134**, and **heart UBERON:0000948**. At tissue level, the vulnerable compartments are nervous tissue, skeletal muscle, and myocardium. At subcellular level, the lesion is in the mitochondrial inner membrane/matrix-facing complex-I assembly system.

Leigh lesions, when present, are generally bilateral and symmetric; nevertheless, no NDUFAF4-specific MRI dataset in the retrieved primary family report was sufficient to establish exact localization or universal bilateral involvement. Anatomical annotations beyond the broad organ level should therefore be attached only to patient-level evidence.

## 8. Temporal development

Available reports support neonatal, infantile, or childhood onset, with potentially progressive encephalomyopathy and early mortality. However, the three related individuals showed variable symptom development, so onset and progression are not uniform. (nouws2012assemblyfactorsas pages 4-6)

There is no validated staging system. A pragmatic clinical sequence is: biochemical/developmental abnormalities, progressive motor or neurologic dysfunction, multisystem complications, and—among severe cases—respiratory/cardiac/metabolic decompensation. The disorder is lifelong. Spontaneous remission has not been documented, although symptoms may fluctuate with metabolic stress. No disease-specific critical intervention window has been established; biologically, diagnosis before irreversible neurodegeneration is preferable.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two heterozygous carrier parents, each pregnancy has a 25% probability of an affected child, 50% probability of a carrier child, and 25% probability of a child inheriting neither familial allele. The identified cases were homozygous, consistent with parental relatedness or shared ancestry, although the exact pedigree details were not fully recoverable. (marcus2013replacementofthe pages 2-3, nouws2012assemblyfactorsas pages 6-7)

Penetrance for clearly deleterious biallelic variants appears high but cannot be quantified. Expressivity is variable, including among siblings. There is no evidence of anticipation. Germline mosaicism has not been reported; the usual small residual recurrence risk should be discussed when apparently de novo findings are encountered. No founder effect, carrier frequency, ethnic enrichment, geographic prevalence, sex ratio, or incidence has been established.

General OXPHOS disorders have historically been estimated at approximately 1 per 5,000–8,000 live births, and complex-I deficiency accounts for roughly one-quarter to one-third of respiratory-chain deficiency, but these figures **must not be applied to nuclear type 15**, which is vastly rarer. (nouws2012assemblyfactorsas pages 1-2, golubitzky2011screeningforactive pages 1-2)

## 10. Diagnostics

### Clinical and biochemical workflow

Suspect the disorder in a neonate or child with developmental regression/delay, hypotonia, exercise intolerance, encephalopathy, lactic acidosis, cardiomyopathy, or Leigh-pattern MRI. Initial evaluation may include blood and CSF lactate/pyruvate with cautious interpretation, plasma amino acids, acylcarnitines, urine organic acids, glucose, liver and renal indices, CK, ECG/echocardiography, hearing/vision assessment, EEG if seizures are suspected, and brain MRI/MRS.

Biochemical confirmation can use spectrophotometric respiratory-chain enzyme analysis in muscle or fibroblasts, preferably normalized to citrate synthase, plus oxygen-consumption studies. Blue-native PAGE and complex-I in-gel activity can identify reduced holoenzyme and accumulated assembly intermediates. The defining human findings were severely reduced complex-I activity and approximately 30% residual mature complex I. (marcus2013replacementofthe pages 1-2, marcus2013replacementofthe pages 5-7)

Muscle biopsy is no longer mandatory when molecular diagnosis is clear, but may be useful when blood testing is unrevealing or functional confirmation is required. No NDUFAF4-specific histopathologic signature is established.

### Genetic testing

A practical first-line test is a comprehensive nuclear-and-mitochondrial mitochondrial-disease/Leigh-syndrome panel or trio **WES/WGS**, including **NDUFAF4**, with copy-number calling and full mtDNA analysis. Biallelic variants should be confirmed and phased by parental testing. Single-gene sequencing is efficient when a familial NDUFAF4 variant is known. WGS may detect deep-intronic or structural variants missed by panels/WES. CMA, karyotyping, and FISH have low yield for an isolated single-gene recessive disorder unless syndromic copy-number disease is suspected. Repeat-expansion testing is not indicated.

For uncertain splice variants, RNA sequencing from fibroblasts or another expressing tissue may establish aberrant transcripts. Quantitative proteomics, BN-PAGE, enzyme assays, and complementation can help adjudicate variants of uncertain significance. Patient-cell rescue by wild-type NDUFAF4 is strong functional evidence: the disease-specific study showed selective restoration in NDUFAF4-mutant but not NDUFS2-mutant cells. (marcus2013replacementofthe pages 5-7, marcus2013replacementofthe pages 7-9)

### Differential diagnosis

Key differentials include other nuclear complex-I assembly defects—**NDUFAF1, NDUFAF2, NDUFAF3, NDUFAF5, NDUFAF6, NDUFAF8, ACAD9, FOXRED1, NUBPL, TIMMDC1**—structural complex-I gene disorders, mtDNA complex-I variants, pyruvate dehydrogenase deficiency, other Leigh-spectrum disorders, organic acidemias, and fatty-acid oxidation defects. Phenotype alone is insufficient because genotype–phenotype correlation in complex-I disease is poor. (rodenburg2016mitochondrialcomplexilinked pages 21-23, nouws2012assemblyfactorsas pages 4-6)

There is no population or newborn screen for NDUFAF4 deficiency. Cascade testing is appropriate after a molecular diagnosis.

## 11. Outcome and prognosis

No NDUFAF4-specific 5-year survival, median life expectancy, mortality rate, functional scale, or quality-of-life dataset exists. The historical phenotype includes severe neonatal/infantile mitochondrial disease, progressive encephalomyopathy, and early death, but variable sibling expression means prognosis should not be assigned solely from genotype. (marcus2013replacementofthe pages 1-2, nouws2012assemblyfactorsas pages 4-6)

Likely morbidity includes developmental and motor disability, reduced endurance, feeding and respiratory complications, seizures when present, and cardiac disease. Potential prognostic factors—unvalidated for NDUFAF4—include age at onset, residual complex-I activity, neurologic lesion burden, persistent lactate elevation, respiratory involvement, cardiomyopathy, and frequency of metabolic crises. Recovery from established neurodegeneration is generally limited; transient metabolic deterioration may partially improve with supportive treatment.

## 12. Treatment

### Current care

There is **no approved NDUFAF4-specific disease-modifying treatment**. Management is individualized and multidisciplinary: nutrition and feeding support; prompt treatment of infection/dehydration; avoidance of prolonged fasting; physical, occupational, and speech therapy; seizure management; respiratory support; and surveillance/treatment of cardiomyopathy, hearing loss, visual disease, renal dysfunction, and endocrine complications. Exercise should be prescribed conservatively by mitochondrial specialists rather than avoided categorically.

Empirical “mitochondrial cocktails” may include coenzyme Q10, riboflavin, thiamine, antioxidants, or other cofactors, but controlled NDUFAF4 evidence is absent. Reviews emphasize scarce trials and uncertain benefit of general vitamin/cofactor therapy; riboflavin responsiveness in **ACAD9** deficiency must not be extrapolated to NDUFAF4. (nouws2012assemblyfactorsas pages 8-9, diaz2011mitochondrialdisorderscaused pages 12-13)

Suggested NCIT intervention terms include **Supportive Care C15747**, **Physical Therapy C15308**, **Occupational Therapy C15903**, **Speech Therapy C15309**, **Genetic Counseling C15240**, and gene-specific drug terms only if actually administered.

### Experimental approaches

The most specific experimental intervention is TAT-mediated wild-type NDUFAF4 protein replacement. In patient fibroblasts, TAT–NDUFAF4 entered mitochondria within 30 minutes, increased complex-I activity by 59–92% in isolated F528 mitochondria, restored activity by 46% in cultured F528 cells, and increased activity by approximately 20% and 23% in F334 and F511 cells. It increased OXPHOS-dependent growth by 25%, ATP per mitochondrial content by 25%, and reduced free radicals by approximately 25%. The authors’ abstract states: “TAT-ORF is biologically active and led to an increase in complex I activity.” This is compelling cellular proof of concept, but not evidence of animal efficacy, blood–brain-barrier delivery, long-term safety, or human benefit. Publication: Marcus et al., online May 8, 2013; DOI: https://doi.org/10.2119/molmed.2012.00343. (marcus2013replacementofthe pages 1-2, marcus2013replacementofthe pages 5-7, marcus2013replacementofthe pages 7-9)

A mixed-genotype fibroblast screen found AICAR the most favorable of ten compounds, with positive effects in five of six evaluable patient lines. The abstract reports that AICAR improved growth and ATP while reducing ROS and increasing mitochondrial biogenesis/AMPK activation. This was in vitro and not a NDUFAF4-specific efficacy trial. Publication: October 26, 2011; DOI: https://doi.org/10.1371/journal.pone.0026883. (golubitzky2011screeningforactive pages 1-2, golubitzky2011screeningforactive pages 6-7)

No NDUFAF4-targeted gene therapy, CRISPR therapy, RNA therapy, cell therapy, or clinical protein-replacement trial was found. Broader Leigh-spectrum trials include vatiquinone/EPI-743, cysteamine formulations, sonlicromanol/KH176, sirolimus, and other redox or metabolic approaches, but enrollment and efficacy cannot be assumed for NDUFAF4 disease. No treatment-response rate or pharmacogenomic rule exists for this genotype.

## 13. Prevention

Primary prevention by lifestyle, vaccination, or environmental control is impossible because the disorder is inherited. The effective prevention options are reproductive:

- molecular carrier testing of parents and at-risk relatives;
- genetic counseling with autosomal-recessive recurrence risks;
- prenatal diagnosis by chorionic-villus sampling or amniocentesis for known familial variants;
- preimplantation genetic testing for monogenic disease;
- use of donor gametes where desired.

Secondary prevention consists of early molecular diagnosis, cascade testing, baseline cardiac/neurologic surveillance, and an emergency plan for catabolic illness. Tertiary prevention aims to limit aspiration, malnutrition, contractures, seizures, respiratory failure, and cardiac complications. No prophylactic medication prevents disease onset.

## 14. Other species and natural disease

Orthologs are evolutionarily conserved in model species, supporting a fundamental role in complex-I biogenesis. Relevant taxa include **Homo sapiens NCBI:9606**, **Mus musculus NCBI:10090**, **Drosophila melanogaster NCBI:7227**, and **Caenorhabditis elegans NCBI:6239**. The Drosophila ortholog is **CG11722**. (murari2021dissectingtheconcordant pages 2-5)

No naturally occurring veterinary NDUFAF4 syndrome, breed association, or OMIA disease was identified. The condition has no zoonotic potential and is not transmissible between species.

## 15. Model organisms and experimental systems

### Drosophila

Muscle-specific RNAi against CG11722 is the strongest in-vivo NDUFAF4 model. Potent developmental muscle knockdown yielded no adults; later or weaker thoracic-muscle knockdown permitted survival but caused reduced complex-I assembly/activity, elevated ROS, stalled Q/N/PP-b intermediates, and compensatory elevation of complexes II and IV. This model is valuable for assembly biology, stress adaptation, genetic rescue, and therapeutic screening. Its limitations are knockdown rather than patient-variant knock-in, flight-muscle emphasis, and incomplete representation of human brain and cardiac disease. Publication: Murari et al., August 20, 2021; DOI: https://doi.org/10.1016/j.isci.2021.102869. (murari2021dissectingtheconcordant pages 1-2, murari2021dissectingtheconcordant pages 5-8, murari2021dissectingtheconcordant pages 8-9)

### C. elegans and cellular systems

C. elegans assembly-factor homologues have been studied experimentally, but the retrieved evidence did not establish a standardized NDUFAF4 patient-allele model or a quantitative match to the human phenotype. Human primary fibroblasts F528, F334, and F511 remain the most disease-specific experimental system. They recapitulate impaired complex-I activity and are pharmacologically and genetically rescuable, but fibroblasts may underrepresent post-mitotic neuronal, cardiac, and skeletal-muscle pathology. (marcus2013replacementofthe pages 2-3, marcus2013replacementofthe pages 5-7)

No published NDUFAF4 p.Leu65Pro knock-in mouse, rat, zebrafish, patient-derived iPSC neuron, brain organoid, or conditional mammalian model was found in the retrieved literature. Developing such models is a major research need.

## Recent developments and expert assessment

No 2023–2024 study was found that materially expanded the **NDUFAF4-specific human cohort**. The important recent advance is conceptual: modern cryo-EM and modular assembly studies reinforce that mammalian complex I is constructed through defined intermediates rather than as a single concerted event. The 2024 review by Laube et al. describes cryo-EM as a means to resolve assembly-factor functions and emphasizes stepwise assembly matching complex-I modular architecture (published February 2024; DOI: https://doi.org/10.1107/S205979832400086X). This framework is consistent with the experimentally observed Q-, N-, and PP-b-module defects after NDUFAF4 disruption. (murari2021dissectingtheconcordant pages 2-5, murari2021dissectingtheconcordant pages 5-8, murari2021dissectingtheconcordant pages 8-9)

The authoritative interpretation is therefore cautious: the causal gene and core assembly defect are well supported by segregation, biochemical deficiency, stalled intermediates, patient-cell rescue, and conserved in-vivo knockdown phenotypes. In contrast, disease prevalence, full phenotypic spectrum, variant-specific prognosis, penetrance, natural history, and treatment efficacy remain poorly defined. Future priorities are international case aggregation, harmonized HPO phenotyping, deposition of variants with ACMG evidence in ClinVar, longitudinal outcomes, patient-derived neural/cardiac models, mammalian knock-in models, and testing of CNS-deliverable NDUFAF4 replacement or gene-replacement strategies.

References

1. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 15): Open Targets Query (Mitochondrial complex I deficiency, nuclear type 15, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (diaz2011mitochondrialdisorderscaused pages 12-13): Francisca Diaz, Heike Kotarsky, Vineta Fellman, and Carlos T. Moraes. Mitochondrial disorders caused by mutations in respiratory chain assembly factors. Seminars in fetal & neonatal medicine, 16 4:197-204, Aug 2011. URL: https://doi.org/10.1016/j.siny.2011.05.004, doi:10.1016/j.siny.2011.05.004. This article has 92 citations and is from a domain leading peer-reviewed journal.

3. (marcus2013replacementofthe pages 2-3): Dana Marcus, Michal Lichtenstein, Ann Saada, and Haya Lorberboum-Galski. Replacement of the c6orf66 assembly factor (ndufaf4) restores complex i activity in patient cells. Molecular Medicine, 19:124-134, Jan 2013. URL: https://doi.org/10.2119/molmed.2012.00343, doi:10.2119/molmed.2012.00343. This article has 29 citations and is from a peer-reviewed journal.

4. (nouws2012assemblyfactorsas pages 6-7): Jessica Nouws, Leo G. J. Nijtmans, Jan A. Smeitink, and Rutger O. Vogel. Assembly factors as a new class of disease genes for mitochondrial complex i deficiency: cause, pathology and treatment options. Brain : a journal of neurology, 135 Pt 1:12-22, Oct 2012. URL: https://doi.org/10.1093/brain/awr261, doi:10.1093/brain/awr261. This article has 114 citations.

5. (marcus2013replacementofthe pages 1-2): Dana Marcus, Michal Lichtenstein, Ann Saada, and Haya Lorberboum-Galski. Replacement of the c6orf66 assembly factor (ndufaf4) restores complex i activity in patient cells. Molecular Medicine, 19:124-134, Jan 2013. URL: https://doi.org/10.2119/molmed.2012.00343, doi:10.2119/molmed.2012.00343. This article has 29 citations and is from a peer-reviewed journal.

6. (marcus2013replacementofthe pages 5-7): Dana Marcus, Michal Lichtenstein, Ann Saada, and Haya Lorberboum-Galski. Replacement of the c6orf66 assembly factor (ndufaf4) restores complex i activity in patient cells. Molecular Medicine, 19:124-134, Jan 2013. URL: https://doi.org/10.2119/molmed.2012.00343, doi:10.2119/molmed.2012.00343. This article has 29 citations and is from a peer-reviewed journal.

7. (marcus2013replacementofthe pages 7-9): Dana Marcus, Michal Lichtenstein, Ann Saada, and Haya Lorberboum-Galski. Replacement of the c6orf66 assembly factor (ndufaf4) restores complex i activity in patient cells. Molecular Medicine, 19:124-134, Jan 2013. URL: https://doi.org/10.2119/molmed.2012.00343, doi:10.2119/molmed.2012.00343. This article has 29 citations and is from a peer-reviewed journal.

8. (murari2021dissectingtheconcordant pages 1-2): Anjaneyulu Murari, Shauna-Kay Rhooms, Christian Garcia, Tong Liu, Hong Li, Bibhuti Mishra, Cassie Deshong, and Edward Owusu-Ansah. Dissecting the concordant and disparate roles of ndufaf3 and ndufaf4 in mitochondrial complex i biogenesis. Aug 2021. URL: https://doi.org/10.1016/j.isci.2021.102869, doi:10.1016/j.isci.2021.102869. This article has 14 citations and is from a peer-reviewed journal.

9. (murari2021dissectingtheconcordant pages 2-5): Anjaneyulu Murari, Shauna-Kay Rhooms, Christian Garcia, Tong Liu, Hong Li, Bibhuti Mishra, Cassie Deshong, and Edward Owusu-Ansah. Dissecting the concordant and disparate roles of ndufaf3 and ndufaf4 in mitochondrial complex i biogenesis. Aug 2021. URL: https://doi.org/10.1016/j.isci.2021.102869, doi:10.1016/j.isci.2021.102869. This article has 14 citations and is from a peer-reviewed journal.

10. (murari2021dissectingtheconcordant pages 5-8): Anjaneyulu Murari, Shauna-Kay Rhooms, Christian Garcia, Tong Liu, Hong Li, Bibhuti Mishra, Cassie Deshong, and Edward Owusu-Ansah. Dissecting the concordant and disparate roles of ndufaf3 and ndufaf4 in mitochondrial complex i biogenesis. Aug 2021. URL: https://doi.org/10.1016/j.isci.2021.102869, doi:10.1016/j.isci.2021.102869. This article has 14 citations and is from a peer-reviewed journal.

11. (murari2021dissectingtheconcordant pages 8-9): Anjaneyulu Murari, Shauna-Kay Rhooms, Christian Garcia, Tong Liu, Hong Li, Bibhuti Mishra, Cassie Deshong, and Edward Owusu-Ansah. Dissecting the concordant and disparate roles of ndufaf3 and ndufaf4 in mitochondrial complex i biogenesis. Aug 2021. URL: https://doi.org/10.1016/j.isci.2021.102869, doi:10.1016/j.isci.2021.102869. This article has 14 citations and is from a peer-reviewed journal.

12. (golubitzky2011screeningforactive pages 1-2): Anna Golubitzky, Phyllis Dan, Sarah Weissman, Gabriela Link, Jakob D. Wikstrom, and Ann Saada. Screening for active small molecules in mitochondrial complex i deficient patient's fibroblasts, reveals aicar as the most beneficial compound. PLoS ONE, 6:e26883, Oct 2011. URL: https://doi.org/10.1371/journal.pone.0026883, doi:10.1371/journal.pone.0026883. This article has 134 citations and is from a peer-reviewed journal.

13. (golubitzky2011screeningforactive pages 6-7): Anna Golubitzky, Phyllis Dan, Sarah Weissman, Gabriela Link, Jakob D. Wikstrom, and Ann Saada. Screening for active small molecules in mitochondrial complex i deficient patient's fibroblasts, reveals aicar as the most beneficial compound. PLoS ONE, 6:e26883, Oct 2011. URL: https://doi.org/10.1371/journal.pone.0026883, doi:10.1371/journal.pone.0026883. This article has 134 citations and is from a peer-reviewed journal.

14. (nouws2012assemblyfactorsas pages 1-2): Jessica Nouws, Leo G. J. Nijtmans, Jan A. Smeitink, and Rutger O. Vogel. Assembly factors as a new class of disease genes for mitochondrial complex i deficiency: cause, pathology and treatment options. Brain : a journal of neurology, 135 Pt 1:12-22, Oct 2012. URL: https://doi.org/10.1093/brain/awr261, doi:10.1093/brain/awr261. This article has 114 citations.

15. (nouws2012assemblyfactorsas pages 8-9): Jessica Nouws, Leo G. J. Nijtmans, Jan A. Smeitink, and Rutger O. Vogel. Assembly factors as a new class of disease genes for mitochondrial complex i deficiency: cause, pathology and treatment options. Brain : a journal of neurology, 135 Pt 1:12-22, Oct 2012. URL: https://doi.org/10.1093/brain/awr261, doi:10.1093/brain/awr261. This article has 114 citations.

16. (rodenburg2016mitochondrialcomplexilinked pages 21-23): Richard J. Rodenburg. Mitochondrial complex i-linked disease. Biochimica et biophysica acta, 1857 7:938-45, Jul 2016. URL: https://doi.org/10.1016/j.bbabio.2016.02.012, doi:10.1016/j.bbabio.2016.02.012. This article has 176 citations.

17. (fernandez‐vizarra2021mitochondrialdisordersof pages 96-99): Erika Fernandez‐Vizarra and Massimo Zeviani. Mitochondrial disorders of the oxphos system. Dec 2020. URL: https://doi.org/10.1002/1873-3468.13995, doi:10.1002/1873-3468.13995. This article has 260 citations and is from a peer-reviewed journal.

18. (nouws2012assemblyfactorsas pages 4-6): Jessica Nouws, Leo G. J. Nijtmans, Jan A. Smeitink, and Rutger O. Vogel. Assembly factors as a new class of disease genes for mitochondrial complex i deficiency: cause, pathology and treatment options. Brain : a journal of neurology, 135 Pt 1:12-22, Oct 2012. URL: https://doi.org/10.1093/brain/awr261, doi:10.1093/brain/awr261. This article has 114 citations.

19. (murari2021dissectingtheconcordant pages 14-16): Anjaneyulu Murari, Shauna-Kay Rhooms, Christian Garcia, Tong Liu, Hong Li, Bibhuti Mishra, Cassie Deshong, and Edward Owusu-Ansah. Dissecting the concordant and disparate roles of ndufaf3 and ndufaf4 in mitochondrial complex i biogenesis. Aug 2021. URL: https://doi.org/10.1016/j.isci.2021.102869, doi:10.1016/j.isci.2021.102869. This article has 14 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_15-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032620` (4 mentions) - the report calls it "if available", "Mitochondrial complex I deficiency, nuclear type 15"; MONDO calls it **mitochondrial complex I deficiency, nuclear type 15**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005747` (obsolete mitochondrial respiratory chain complex I) (1 mention) - replaced by `GO:0045271`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0032620` - called "if available", "Mitochondrial complex I deficiency, nuclear type 15"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `NCBI`.
