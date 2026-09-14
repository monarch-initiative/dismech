---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T17:00:19.452031'
end_time: '2026-09-02T17:12:34.308384'
duration_seconds: 734.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: CHEK2-related Cancer Predisposition
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0030766
    reported_labels:
    - multifocal breast carcinoma*, if locally available
    ontology_label: Ear pain
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0090305
    ontology_label: obsolete nucleic acid phosphodiester bond hydrolysis
    replaced_by: GO:0090304
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CHEK2-related_Cancer_Predisposition-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CHEK2-related Cancer Predisposition
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CHEK2-related Cancer Predisposition** covering all of the
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
- **Disease Name:** CHEK2-related Cancer Predisposition
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CHEK2-related Cancer Predisposition** covering all of the
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


# CHEK2-Related Cancer Predisposition: Comprehensive Disease-Characteristics Report

## Executive summary

CHEK2-related cancer predisposition is an **autosomal-dominant, incompletely penetrant hereditary cancer susceptibility state** caused by a heterozygous pathogenic or likely pathogenic germline variant in **CHEK2**, which encodes checkpoint kinase 2 (CHK2). It is not a congenital malformation syndrome: most carriers are clinically normal until, and unless, cancer develops. The best-established manifestations are **moderately increased female breast-cancer risk**, increased contralateral breast-cancer risk after a first breast cancer, and increased prostate-cancer risk. Associations with colorectal, thyroid, renal, pancreatic, melanoma, testicular, and hematologic malignancies are inconsistent, variant- or population-dependent, or insufficiently validated for routine organ-specific surveillance.

The central 2023 ACMG expert conclusion is that CHEK2 risk is a continuum modified by variant class, age, sex, family history, polygenic background, reproductive and lifestyle factors; management should therefore use **personalized absolute-risk estimates**, not the gene result alone. Average female lifetime breast-cancer risk is approximately 25%, with a broad estimated range of 15%–40%. No CHEK2-specific targeted treatment is currently established. The 2024 NCCN colorectal guideline notably **de-implemented intensified colorectal screening based solely on CHEK2 status**. (hanson2023managementofindividuals pages 18-20, hanson2023managementofindividuals pages 23-25, hanson2023managementofindividuals pages 22-23)

| Domain/phenotype | Current evidence level | Quantitative finding | Practical implication | Key source/date/DOI or PMID |
|---|---|---|---|---|
| Female breast cancer | **Established; moderate penetrance** | Average lifetime risk ≈25%, with an estimated **15%–40%** range after accounting for variant type, family history, and modifiers; truncating variants: OR **3.25** (95% CI 2.55–4.13); c.1100delC: OR **2.88** (2.65–3.22) (stolarova2020chek2germlinevariants pages 15-17, hanson2023managementofindividuals pages 18-20) | Use individualized absolute-risk assessment rather than the gene result alone; enhanced breast surveillance is often appropriate for truncating-variant carriers. | Hanson et al., Oct 2023, DOI: [10.1016/j.gim.2023.100870](https://doi.org/10.1016/j.gim.2023.100870); Stolarova et al., Dec 2020, DOI: [10.3390/cells9122675](https://doi.org/10.3390/cells9122675) |
| Contralateral breast cancer | **Established increased risk** | CARRIERS: HR **2.0** (95% CI 1.0–4.2); 10-year cumulative incidence **13% premenopausal** and **4% postmenopausal**. BRIDGES protein-truncating variants: HR **2.25** (1.55–3.27) (hanson2023managementofindividuals pages 23-25) | Discuss intensified surveillance and individualized surgical risk reduction; contralateral mastectomy is **not routinely indicated** solely because of CHEK2. | Yadav et al., Mar 2023, DOI: [10.1200/JCO.22.01239](https://doi.org/10.1200/JCO.22.01239); Hanson et al., Oct 2023, DOI above |
| Male breast cancer | **Probable association, but absolute risk poorly quantified** | CHEK2 is enriched among male breast-cancer predisposition findings, but available evidence does not provide a reliable variant-specific lifetime-risk estimate (hanson2023managementofindividuals pages 27-28) | No CHEK2-specific population screening standard for unaffected men; management should be driven by personal and family history and breast symptoms. | Hanson et al., Oct 2023, DOI: [10.1016/j.gim.2023.100870](https://doi.org/10.1016/j.gim.2023.100870) |
| Prostate cancer | **Established association; moderate/variable penetrance** | Truncating variants are associated with increased prostate-cancer risk, but estimates vary by variant and ancestry; the reviewed evidence does not support one universal absolute-risk figure (stolarova2020chek2germlinevariants pages 7-9, hanson2023managementofindividuals pages 23-25) | Consider PSA-based surveillance through shared decision-making, particularly with a prostate-cancer family history; counsel that evidence is less precise than for female breast cancer. | Hanson et al., Oct 2023, DOI above; Stolarova et al., Dec 2020, DOI above |
| Colorectal cancer | **Current evidence insufficient for a clinically important increase** | Recent cohorts of more than 6,000 heterozygotes found approximately null association (**OR ≈1.10**) for truncating or missense variants; earlier reports were inconsistent (stolarova2020chek2germlinevariants pages 41-43) | **2024 NCCN update de-implemented CHEK2-only intensified colon screening**; use general-population screening unless personal or family history independently warrants earlier colonoscopy. | Hodan et al., Dec 2024, DOI: [10.6004/jnccn.2024.0061](https://doi.org/10.6004/jnccn.2024.0061) |
| Thyroid, kidney, pancreatic, melanoma, testicular and hematologic cancers | **Limited, conflicting, or population/variant-specific** | Associations have been reported, but effect sizes are heterogeneous and often derive from founder populations or selected cohorts; testicular germ-cell tumor studies reported LOF OR **3.87** (1.65–8.86), requiring broader validation (stolarova2020chek2germlinevariants pages 41-43, ozdemir2024molecularandin pages 1-2) | Do not institute organ-specific surveillance solely from CHEK2 status outside research; manage according to symptoms, family history, and standard risk factors. | AlDubayan et al., Apr 2019, DOI: [10.1001/jamaoncol.2018.6477](https://doi.org/10.1001/jamaoncol.2018.6477); Ozdemir et al., Nov 2024, DOI: [10.3390/cancers16223876](https://doi.org/10.3390/cancers16223876) |
| Variant-specific effects | **Established heterogeneity** | c.1100delC and other truncating variants generally confer moderate risk; p.Ile157Thr has lower breast-cancer effect, OR ≈**1.35–1.5**, mainly ER-positive; p.Ser428Phe and many missense variants have low or uncertain actionability (stolarova2020chek2germlinevariants pages 9-11, stolarova2020chek2germlinevariants pages 15-17, hanson2023managementofindividuals pages 22-23) | Do not apply truncating-variant risk estimates to every missense variant. A VUS is nondiagnostic and must not guide surveillance or prophylactic surgery. | Hanson et al., Oct 2023, DOI above; Stolarova et al., Dec 2020, DOI above |
| Breast surveillance and prevention | **Guideline-supported, risk-adapted** | Modeling suggests annual MRI from **age 30–35**, adding annual mammography at **age 40**, may reduce breast-cancer mortality by **>50%** in women with CHEK2 pathogenic variants (hanson2023managementofindividuals pages 18-20) | Calculate personalized risk, ideally with CanRisk or an equivalent model. Risk-reducing mastectomy is optional only after shared decision-making; salpingo-oophorectomy is not indicated solely for CHEK2. | Hanson et al., Oct 2023, DOI: [10.1016/j.gim.2023.100870](https://doi.org/10.1016/j.gim.2023.100870) |
| CHEK2-directed targeted therapy | **Not established** | No validated response rate or predictive biomarker supports treatment selection from germline CHEK2 status alone; ACMG states that no specific targeted medical treatment is currently recommended (hanson2023managementofindividuals pages 18-20, hanson2023managementofindividuals pages 32-33) | Treat the diagnosed cancer according to tumor type, stage, receptor status, and validated somatic biomarkers. PARP inhibitors or other DDR agents should not be used solely because of CHEK2 outside an approved tumor indication or clinical trial. | Hanson et al., Oct 2023, DOI above; TBCRC 048, PMID: [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) |


*Table: Evidence-calibrated summary of established and uncertain CHEK2-associated cancer risks, variant effects, surveillance, and therapeutic implications. Quantitative estimates should be interpreted in the context of variant class, ancestry, family history, and other modifiers.*

---

## 1. Disease information

### Definition and scope

CHEK2-related cancer predisposition denotes inherited susceptibility resulting from a germline CHEK2 pathogenic/likely pathogenic variant. CHEK2 is a moderate-penetrance tumor-suppressor gene; penetrance is age dependent and incomplete, and expressivity ranges from no cancer to one or several primary tumors. It should not be equated with classic Li-Fraumeni syndrome, and a **variant of uncertain significance (VUS) does not establish the diagnosis**. OpenTargets identifies a strong CHEK2–breast-cancer association, supported by human genetic literature including PMIDs **35418303, 37390209, 34375979, and 25958056**. (OpenTargets Search: breast cancer,prostate cancer,colorectal cancer-CHEK2, stolarova2020chek2germlinevariants pages 33-35)

### Identifiers and terminology

- **Preferred name:** CHEK2-related cancer predisposition.
- **Synonyms:** CHEK2-associated cancer predisposition; CHEK2-associated hereditary cancer; hereditary cancer predisposition due to CHEK2; CHEK2-associated breast-cancer predisposition; historically, “CHEK2-associated hereditary breast and colorectal cancer” or HBCC, although the colorectal component is no longer considered firmly established.
- **Gene identifiers:** CHEK2; HGNC **16627**; NCBI Gene **11200**; Ensembl **ENSG00000183765**; OMIM gene **604373**.
- **Chromosome:** 22q12.1.
- **MONDO:** A stable, specific MONDO identifier for the complete CHEK2-related multiorgan predisposition entity was not verified in the retrieved evidence. Do not substitute MONDO:0007254, which denotes breast cancer, or MONDO:0003582, hereditary breast/ovarian cancer syndrome. (OpenTargets Search: breast cancer,prostate cancer,colorectal cancer-CHEK2)
- **Orphanet:** No CHEK2-specific syndrome identifier was verified. Orphanet **227535** (“hereditary breast cancer”) is broader, while Orphanet **145** denotes hereditary breast/ovarian cancer syndrome. (OpenTargets Search: breast cancer,prostate cancer,colorectal cancer-CHEK2)
- **ICD-10/ICD-11:** No dedicated CHEK2 code. Coding generally combines the actual malignancy with genetic-susceptibility/family-history codes; in ICD-10-CM, **Z15.01** is commonly used for genetic susceptibility to malignant neoplasm of breast and **Z15.09** for other malignancy susceptibility, subject to local coding rules.
- **MeSH:** No specific CHEK2-predisposition heading was verified; useful broader headings include *Genetic Predisposition to Disease*, *Neoplastic Syndromes, Hereditary*, and the affected cancer.

This report synthesizes **aggregated disease-level resources, guidelines, cohorts, case-control studies, and experimental models**, not an individual EHR. The 2024 Turkish study is a clinic-based cohort of 1,707 high-risk individuals, illustrating patient-level data aggregated for research. (ozdemir2024molecularandin pages 1-2)

---

## 2. Etiology

### Causal factor

The primary cause is a constitutional heterozygous CHEK2 pathogenic/likely pathogenic variant that reduces CHK2 abundance or kinase function. Pathogenic classes include nonsense, frameshift, canonical splice, exon-level deletion/duplication, and functionally damaging missense variants. A somatic CHEK2 finding alone does not diagnose inherited predisposition; however, tumor-detected CHEK2 pathogenic variants frequently warrant confirmatory germline testing. (stolarova2020chek2germlinevariants pages 9-11, hanson2023managementofindividuals pages 18-20)

### Genetic risk factors and modifiers

Protein-truncating variants generally carry the clearest breast-cancer risk: a cited meta-analysis estimated OR **3.25** (95% CI 2.55–4.13). For **c.1100delC**, the female breast-cancer OR was **2.88** (2.65–3.22). By contrast, **p.Ile157Thr** is a lower-effect allele, with OR approximately 1.35–1.5, principally for ER-positive disease; risks from truncating variants must not be assigned indiscriminately to common missense alleles. p.Ser428Phe and many rare missense variants have low, population-dependent, or uncertain actionability. p.Arg117Gly is an example of a missense variant with stronger functional evidence. (stolarova2020chek2germlinevariants pages 9-11, stolarova2020chek2germlinevariants pages 15-17, hanson2023managementofindividuals pages 22-23)

Family history can shift estimated lifetime female breast-cancer risk from approximately **20% without a family history to as high as 40% with a positive family history** in historical estimates. Polygenic background, reproductive factors, age, and ancestry further modify penetrance. Validated tools such as **CanRisk/BOADICEA**, where locally applicable, are preferable to a fixed gene-level estimate. (stolarova2020chek2germlinevariants pages 15-17, hanson2023managementofindividuals pages 18-20)

### Environmental, hormonal, and lifestyle factors

General cancer determinants—aging, obesity, alcohol, smoking, reproductive/hormonal exposure, ultraviolet radiation, and ionizing radiation—remain relevant, but robust CHEK2-specific interaction estimates are sparse. One historical subgroup estimate found a 10-year breast-cancer risk of 24% in c.1100delC carriers older than 60 who used hormone-replacement therapy and had BMI above 25, but this does not prove a multiplicative interaction. (stolarova2020chek2germlinevariants pages 15-17)

Mechanistically, UV photolesions and estrogen-DNA adducts can stall replication forks; persistent fork collapse produces double-strand breaks that require ATM–CHK2 signaling. Chk2 loss increased UV-B- and DMBA-associated tumorigenesis in models, supporting biologic gene–environment interaction, but direct quantitative translation to human carriers is not established. (mustofa2020rolesofchk2chek2 pages 6-8, mustofa2020rolesofchk2chek2 pages 4-6)

### Protective factors

No CHEK2 allele is established as clinically protective. General reductions in breast- and prostate-cancer risk through healthy weight, physical activity, limiting alcohol, avoiding tobacco, and minimizing unnecessary carcinogenic exposure are reasonable, but CHEK2-specific effect sizes are unavailable. Endocrine breast-cancer risk reduction may be considered using ordinary high-risk criteria; it is not a genotype-specific therapy. Evidence for prophylactic surgery must be based on individualized absolute risk rather than CHEK2 status alone. (hanson2023managementofindividuals pages 22-23)

---

## 3. Phenotypes

The predisposition itself is usually **asymptomatic and lifelong**. The observable phenotypes are malignant neoplasms and their treatment-related consequences.

### Established or probable phenotypes

1. **Female breast carcinoma** — typically adult onset, severity and progression determined by tumor stage and biology. Suggested HPO: **HP:0003002, Breast carcinoma**; **HP:0010619, Bilateral breast carcinoma** where applicable. Average lifetime risk is approximately 25% (range 15%–40%). CHEK2-associated tumors are predominantly ER-positive. (hanson2023managementofindividuals pages 18-20)
2. **Contralateral breast carcinoma** — a metachronous second primary. In CARRIERS, 10-year cumulative incidence was **13% in premenopausal** and **4% in postmenopausal** carriers; HR approximately 2.0. Suggested HPO: bilateral breast carcinoma. (hanson2023managementofindividuals pages 23-25)
3. **Prostate carcinoma** — adult/late-adult onset, with risk particularly supported for truncating variants, although absolute penetrance is less certain than for female breast cancer. Suggested HPO: **HP:0012125, Prostate cancer**. (stolarova2020chek2germlinevariants pages 7-9, hanson2023managementofindividuals pages 23-25)
4. **Male breast carcinoma** — probable but uncommon; absolute lifetime risk is inadequately quantified. Suggested HPO: HP:0003002 plus sex annotation. (hanson2023managementofindividuals pages 27-28)

### Tumor phenotype and pathology

A 2024 pathologic series of 44 breast cancers from 35 women reported median diagnosis age **45 years**; 20% were multifocal and 11% bilateral. Of 44 cancers, **86% were invasive ductal carcinoma/no special type**; 95% of evaluable tumors were ER-positive and 69% were luminal B. Tumor sequencing identified biallelic CHEK2 alteration/LOH in **57% (13/23)**. Neoadjuvant chemotherapy produced pathologic complete response in only **21% (3/14)**, but the cohort was small and not treatment-comparative. Suggested HPO terms include HP:0030766 (*multifocal breast carcinoma*, if locally available), HP:0010619, and HP:0003002. (Study: Schwartz et al., *Breast Cancer Research and Treatment*, online 2023/volume 2024; DOI: https://doi.org/10.1007/s10549-023-07176-8.)

### Uncertain proposed phenotypes

Colorectal, thyroid, kidney, pancreatic, melanoma, testicular germ-cell, pituitary, and hematologic malignancies have been reported. These should be represented in a knowledge base as **limited/conflicting associations**, not obligatory manifestations. For example, a 2019 TGCT study reported CHEK2 loss-of-function OR **3.87** (1.65–8.86) and diagnosis approximately six years earlier, but broad replication and management utility remain limited. (stolarova2020chek2germlinevariants pages 41-43)

### Quality of life

No validated CHEK2-specific EQ-5D, SF-36, or PROMIS profile was identified. Burden arises from cancer, repeated MRI/mammography or biopsies, multiple-primary risk, treatment toxicity, reproductive decisions, and anxiety or decisional conflict surrounding prophylactic surgery. These impacts vary substantially; being a carrier is not itself a functional disability.

---

## 4. Genetic and molecular information

### Gene and protein

CHEK2 spans approximately 54 kb at 22q12.1; the principal transcript has 15 exons and encodes a **543-amino-acid, approximately 65-kDa nuclear serine/threonine kinase**. CHK2 contains an N-terminal SQ/TQ-cluster domain (residues 19–69), FHA domain (92–205), kinase domain (212–501), and C-terminal nuclear-localization signal. (stolarova2020chek2germlinevariants pages 3-5, stolarova2020chek2germlinevariants pages 1-3)

### Pathogenic-variant spectrum

- **Loss-of-function:** frameshift (e.g., NM_007194.4:c.1100del; p.Thr367MetfsTer15), nonsense, canonical splice, and exon-level copy-number variants.
- **Missense:** only variants supported by calibrated clinical and functional evidence should be treated as pathogenic. p.Ile157Thr and p.Ser428Phe are lower-effect alleles and may not justify the same management as truncating variants.
- **Structural variants:** recurrent exon 9–10, exon 2–3, and exon 6 deletions have been reported. Homology/pseudogene sequence around exons 10–14 can complicate NGS and requires a validated assay and orthogonal confirmation where necessary. (stolarova2020chek2germlinevariants pages 9-11)
- **Classification:** use ACMG/AMP criteria, ClinVar expert assertions where available, population frequency, segregation, tumor evidence, and validated functional assays. A VUS must not direct screening, surgery, or predictive testing.
- **Origin:** the predisposition-causing variant is germline; tumors may acquire LOH or another second hit. Somatic CHEK2 variants also occur independently, including in therapy-related clonal hematopoiesis, creating a potential blood-based testing pitfall.

In a historical GeneDx series of 2,508 carriers, about 95% had one of 18 recurrent variants; approximately 73% had one of five frequent founder alleles, while rare variants included at least 17 large intragenic rearrangements. In 2020, 55.9% of 2,195 ClinVar CHEK2 germline submissions were VUS, illustrating the interpretation burden. (stolarova2020chek2germlinevariants pages 9-11)

### Allele frequency and founder effects

c.1100delC approaches **1%** in parts of the United Kingdom and Netherlands but is rare in Mediterranean populations. p.Ile157Thr occurs in approximately **5%** of some Polish, Latvian, Hungarian, and Russian populations and 2%–3% in Czech, Slovak, and German populations. p.Ser428Phe is a recognized Ashkenazi-Jewish founder allele. Exact gnomAD frequencies should be retrieved by genome build, transcript, ancestry, and dataset version rather than stored as a single universal value. (stolarova2020chek2germlinevariants pages 9-11, stolarova2020chek2germlinevariants pages 7-9)

### Modifiers, epigenetics, and chromosomal abnormalities

Family history and polygenic risk are established conceptual modifiers, but no single modifier gene is sufficiently validated for routine standalone management. Somatic LOH supports classical tumor-suppressor behavior in a subset of breast tumors; lack of LOH in other tumors indicates that biallelic inactivation is not universal. No constitutional aneuploidy or recurrent translocation defines the disorder. CHEK2 promoter methylation and altered DDR chromatin states have been studied in tumors, but no validated germline-predisposition epigenetic biomarker was identified.

---

## 5. Environmental information

There is no infectious cause and no zoonotic or transmissible component. Ionizing radiation directly produces double-strand breaks; UV and bulky chemical adducts can produce them indirectly through replication-fork collapse. These exposures engage the pathway in which CHK2 operates, but routine radiation avoidance beyond standard safety practices is not evidence-based for heterozygotes. Available clinical evidence does not establish that breast radiotherapy disproportionately raises contralateral risk in CHEK2 carriers. Smoking, alcohol, obesity, poor diet, and inactivity should be managed according to ordinary cancer-prevention guidance. (mustofa2020rolesofchk2chek2 pages 6-8, mustofa2020rolesofchk2chek2 pages 4-6)

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A germline loss-of-function or damaging CHEK2 variant leads to reduced CHK2 abundance or kinase activity in susceptible epithelial cells.**
2. **DNA double-strand breaks or collapsed replication forks lead to MRN-complex recognition and ATM recruitment/activation.**
3. **ATM activation leads to CHK2 Thr68 phosphorylation, transient dimerization, and trans-autophosphorylation at Thr383/Thr387, generating active monomers.**
4. **Reduced functional CHK2 leads to attenuated phosphorylation of TP53, CDC25A/CDC25C, BRCA1, PML, E2F1, and other effectors.**
5. **Attenuated signaling leads to less effective G1/S and G2/M checkpoint control, apoptosis/senescence, and coordination of double-strand-break repair; the degree of HR impairment is context dependent.**
6. **Survival or replication of damaged cells leads to mutation accumulation, chromosomal instability, and clonal expansion.**
7. **A somatic second hit/LOH in some cells leads to stronger CHK2 deficiency; this step is demonstrated in a subset of breast cancers but is not universal.**
8. **Tissue-, hormone-, polygenic-, age-, and exposure-dependent selection leads principally to ER-positive breast carcinoma and, in men, increased prostate-cancer susceptibility.**
9. **A first breast cancer plus persistent constitutional susceptibility leads to increased contralateral breast-cancer risk.**
10. **Proposed extension to other organs is inferred from selected cohorts and models and remains insufficiently demonstrated for uniform clinical surveillance.**

### Mechanistic detail

The MRN complex senses double-strand breaks and activates ATM; ATM phosphorylates CHK2 and H2AX. CHK2 phosphorylation of TP53 Ser20 supports p53-dependent transcription and arrest, although CHK2 is partly redundant with CHK1 and is not indispensable for all p53 responses. CHK2 phosphorylates CDC25A Ser123, restraining CDK2–cyclin E before S phase, and CDC25C Ser216, promoting 14-3-3 binding and restraining CDK1–cyclin B before mitosis. ATM and CHK2 also phosphorylate BRCA1, connecting checkpoint signaling with homologous recombination. (stolarova2020chek2germlinevariants pages 5-7, smith2020dnadamagecheckpoint pages 2-3, stolarova2020chek2germlinevariants pages 3-5)

Loss of CHK2 therefore differs from complete loss of a core homologous-recombination protein such as BRCA1/2. This distinction helps explain why a CHEK2 variant alone is not a validated predictor of PARP-inhibitor response. The ACMG resource states that evidence is insufficient to select targeted therapy solely from CHEK2 status. (hanson2023managementofindividuals pages 18-20, hanson2023managementofindividuals pages 32-33)

### Molecular profiling

CHEK2-associated breast tumors are usually ER-positive/luminal. Reported recurrent co-alterations include GATA3, PIK3CA, CCND1, FGFR1, ERBB2, ZNF703, TP53, and PPM1D, but these observations come from small tumor series and are not a diagnostic signature. No validated CHEK2-specific metabolomic, lipidomic, proteomic, single-cell, or spatial-transcriptomic signature is ready for clinical use.

### Suggested ontology terms

- **GO biological process:** DNA damage response (GO:0006974); DNA double-strand break repair (GO:0006302); cell-cycle checkpoint signaling (GO:0000075); signal transduction in response to DNA damage (GO:0042770); apoptotic process (GO:0006915); homologous recombination (GO:0035825); maintenance of genome stability (GO:0090305).
- **GO molecular function:** protein serine/threonine kinase activity (GO:0004674); ATP binding (GO:0005524).
- **GO cellular component:** nucleus (GO:0005634); nucleoplasm (GO:0005654); sites of DNA damage.
- **Cell Ontology:** mammary epithelial cell (CL:0002327); luminal epithelial cell of mammary gland; prostate glandular epithelial cell; basal/myoepithelial cells as tumor-context comparators.

---

## 7. Anatomical structures affected

Primary established sites are the **breast/mammary gland** and **prostate gland**. Suggested anatomy terms include **UBERON:0000310 (breast)**, **UBERON:0002367 (prostate gland)**, mammary epithelium, and prostate glandular epithelium. Breast tumors may be unilateral, bilateral, or multifocal; no inherent side preference is established. Secondary anatomical involvement reflects ordinary invasion and metastasis and is not CHEK2-specific. Thyroid, kidney, colorectum, pancreas, skin melanocytes, testis, and hematolymphoid tissues should be annotated as proposed/uncertain sites rather than core disease anatomy.

At the subcellular level, the central compartment is the **nucleus/nucleoplasm**, where CHK2 responds at or near DNA-damage foci. (stolarova2020chek2germlinevariants pages 3-5)

---

## 8. Temporal development

The genotype is present from conception, but cancer onset is generally **adult and insidious**. Penetrance rises with age; there is no neonatal or pediatric syndrome in typical heterozygotes. Once a malignancy occurs, its stages, progression, remission, and recurrence follow the organ-specific AJCC/WHO framework rather than a CHEK2-specific staging system.

The predisposition remains lifelong even after successful cancer treatment. Critical intervention windows are therefore: before cancer, when individualized surveillance can enable early detection; around age 30–35 for initiating MRI in women whose calculated risk justifies it; at approximately age 40 for adding mammography; and after a first breast cancer, when contralateral risk becomes clinically relevant. (hanson2023managementofindividuals pages 18-20, hanson2023managementofindividuals pages 23-25)

---

## 9. Inheritance and population

Inheritance is **autosomal dominant**: each child of a heterozygote has a 50% probability of inheriting the variant. Penetrance is incomplete and age-, sex-, variant-, family-history-, and ancestry-dependent; expressivity is highly variable. There is no evidence of genetic anticipation. Germline mosaicism is biologically possible but not a characteristic feature. Consanguinity is not required.

Biallelic carriers are rare and may have higher cancer risk, but available reports do not define a consistent recessive developmental syndrome; Chk2-null mice are viable and fertile, also indicating substantial pathway redundancy. (stolarova2020chek2germlinevariants pages 7-9, stolarova2020chek2germlinevariants pages 33-35)

Population prevalence cannot be summarized reliably as cases per 100,000 because this is a genotype-defined susceptibility with many unaffected carriers and strong founder effects. Carrier frequency varies markedly by ancestry. In the 2024 Turkish high-risk clinic cohort, approximately **8%** had a CHEK2 variant, but this is a selected referral population and not population prevalence. Nearly half of observed variants had higher frequency than in gnomAD, underscoring the importance of ancestry-matched controls. (ozdemir2024molecularandin pages 1-2)

Sex-specific manifestations differ: female breast cancer is the most strongly quantified phenotype; prostate cancer occurs only in males, and male breast cancer is rare. No universal male:female “disease ratio” is meaningful because unaffected carriers are included in the disease concept.

---

## 10. Diagnostics

### Diagnostic standard

Diagnosis requires identification of a **heterozygous germline CHEK2 pathogenic or likely pathogenic variant** in a validated clinical laboratory, interpreted under ACMG/AMP criteria. A VUS is nondiagnostic. Testing should be accompanied by pre- and post-test genetic counseling. (hanson2023managementofindividuals pages 18-20, hanson2023managementofindividuals pages 22-23)

### Testing approach

1. **Multigene hereditary-cancer panel:** usually preferred because breast/prostate/family-history phenotypes overlap BRCA1, BRCA2, PALB2, ATM, TP53, PTEN, CDH1, mismatch-repair genes, and others.
2. **CHEK2 sequencing plus deletion/duplication analysis:** appropriate for targeted testing or when panel content is restricted. The assay must reliably address problematic homologous regions and copy-number variants. (stolarova2020chek2germlinevariants pages 9-11)
3. **Targeted familial-variant testing:** preferred for relatives after a familial P/LP variant is known.
4. **WES/WGS:** useful when panel testing is negative and the phenotype remains strongly suggestive, or for structural/noncoding research; neither automatically guarantees validated CHEK2 CNV or homologous-region analysis.
5. **CMA, karyotype, and FISH:** not routine for isolated CHEK2 predisposition, although CMA may detect large deletions spanning CHEK2 in a broader genomic disorder.
6. **RNA studies:** may clarify splice variants when blood expression and laboratory validation permit.
7. **Tumor sequencing/liquid biopsy:** cannot by itself distinguish germline from somatic origin; paired normal testing is required. Blood-only sequencing may also detect clonal hematopoiesis.

### Clinical evaluation and differential diagnosis

Record a three-generation pedigree, ages at diagnosis, bilateral/multiple primaries, pathology, and ancestry. Differential diagnosis includes BRCA1/2- and PALB2-associated hereditary breast cancer, ATM predisposition, Li-Fraumeni syndrome, PTEN hamartoma tumor syndrome, CDH1-associated diffuse gastric/lobular breast cancer, Lynch syndrome, and nonhereditary familial clustering. CHEK2 does not have a pathognomonic laboratory chemistry, imaging appearance, or immunohistochemical marker.

### Cascade screening

Offer adult first-degree relatives targeted testing for the familial variant. Testing minors is generally deferred because routine surveillance begins in adulthood and childhood cancer risk is not established. Prenatal and preimplantation genetic testing are technically possible after counseling, but their use for a moderate, incompletely penetrant susceptibility requires careful values-based discussion.

---

## 11. Outcome and prognosis

There is no single syndrome-level survival rate or life-expectancy estimate. Many carriers never develop cancer and have normal longevity. For affected carriers, outcome is primarily determined by organ, stage, grade, receptor status, age, competing illness, and treatment response.

CHEK2-associated breast cancers are commonly ER-positive/luminal, making endocrine therapy relevant. Some c.1100delC studies report worse breast-cancer-specific survival, but confounding by second primaries and tumor biology remains important. In a large 2023 analysis, c.1100delC carriers had shorter breast-cancer-specific survival even after accounting for contralateral cancer (HR **1.30**, 95% CI 1.09–1.56); systemic treatment reduced contralateral risk, while no differential radiotherapy association was found. The supporting survival literature includes PMIDs **24557336** and **24918820**. (hanson2023managementofindividuals pages 32-33)

Major morbidity includes multiple primary cancers, surveillance procedures, surgical/endocrine/chemotherapy toxicity, and psychological burden. No CHEK2-specific prognostic biomarker beyond the germline variant and ordinary tumor biomarkers is validated.

---

## 12. Treatment

### Current standard

Treat the **actual malignancy**, not the inherited predisposition, according to tumor site, stage, histology, receptor status, and validated somatic biomarkers. For ER-positive breast cancer, this may include surgery, radiotherapy, endocrine therapy, chemotherapy, CDK4/6 inhibitors, or other standard agents. For prostate cancer, use standard localized or advanced-disease pathways.

The ACMG expert resource concludes that **“no specific targeted medical treatment is recommended at this time”** for a cancer merely because the patient carries CHEK2; treatment selection from CHEK2 alone is unsupported. (hanson2023managementofindividuals pages 18-20)

### DDR-targeted therapy and trials

Although CHK2 participates in DNA-damage signaling, germline CHEK2 loss does not consistently generate the BRCA-like HR-deficiency phenotype required to predict PARP-inhibitor benefit. In TBCRC 048 (PMID **33119476**), olaparib activity in non-BRCA homologous-recombination genes did not establish CHEK2 as a reliable response biomarker. PARP inhibition should therefore be used only for an approved tumor/genomic indication or a clinical trial, not CHEK2 status alone. (hanson2023managementofindividuals pages 32-33)

CHEK2-inclusive interventional studies identified in ClinicalTrials.gov include:

- **NCT05011383:** recruiting phase II high-dose testosterone for ATM-, CDK12-, or CHEK2-altered prostate cancers; planned n=51.
- **NCT05033756 (COMPRENDO):** active, not recruiting phase II pembrolizumab plus olaparib in HER2-negative breast cancer with deleterious germline mutation or HRD; n=11.
- **NCT02401347:** completed phase II talazoparib in BRCA1/2-wild-type HER2-negative breast/solid tumors; n=21.
- **NCT03786796:** recruiting phase II olaparib for metastatic renal-cell carcinoma with DNA-repair-gene mutations; n=20.
- **NCT06033092:** active phase II low-dose tamoxifen plus lifestyle change for breast-cancer prevention; n=200.

These are basket or pathway trials, not proof of CHEK2-specific efficacy. Gene therapy, RNA therapy, and preventive cell therapy are not available.

### Suggested NCIt intervention concepts

Genetic counseling; cancer screening; magnetic resonance imaging; mammography; prophylactic mastectomy; lumpectomy; mastectomy; radiation therapy; endocrine therapy; tamoxifen; aromatase inhibitor; PARP inhibitor; immune-checkpoint inhibitor; clinical trial. Exact NCIt codes should be resolved against the current NCI Thesaurus release.

---

## 13. Prevention

### Primary prevention

No vaccine or gene-corrective prophylaxis exists. Recommend ordinary cancer-prevention behaviors: avoid tobacco, limit alcohol, maintain healthy weight and activity, use UV protection, and avoid unnecessary ionizing radiation. These recommendations are health-promoting but not proven to normalize CHEK2 risk.

Risk-reducing bilateral mastectomy is **not routinely indicated solely by CHEK2**. It may be considered when personalized lifetime risk, family history, prior biopsies, imaging burden, comorbidity, and patient preferences support it. Risk-reducing salpingo-oophorectomy is not indicated solely for CHEK2 because a clinically important ovarian-cancer association is not established. (hanson2023managementofindividuals pages 22-23)

### Secondary prevention

For women with actionable truncating variants or sufficiently high calculated risk, modeling supports annual breast MRI beginning around **30–35 years**, adding annual mammography around **40 years**; this strategy was projected to reduce breast-cancer mortality by more than 50%. Local guidelines and individualized risk may shift ages. After breast cancer, continue contralateral surveillance unless bilateral mastectomy has occurred. (hanson2023managementofindividuals pages 18-20)

For men, discuss prostate screening—typically PSA with or without digital rectal examination—through shared decision-making, especially with family history. Evidence is insufficient for a universal CHEK2-only regimen.

The important 2024 change is that intensified colonoscopy should **not** be prescribed solely for CHEK2. Use average-risk population screening unless personal history, polyps, inflammatory bowel disease, or family history independently warrants earlier or more frequent examination. Hodan et al., NCCN Version 3.2024, was published December 2024; DOI: https://doi.org/10.6004/jnccn.2024.0061.

There is no evidence-based CHEK2-only screening program for thyroid, renal, pancreatic, melanoma, testicular, pituitary, or hematologic cancer. Symptom-directed care and family-history-specific protocols remain appropriate.

### Tertiary prevention

After cancer, prevent recurrence and second primaries through standard adjuvant therapy, survivorship care, contralateral breast surveillance, adherence to endocrine treatment where indicated, and management of treatment toxicity. Cascade testing can identify relatives who may benefit from surveillance.

---

## 14. Other species and natural disease

- **Human:** *Homo sapiens*, NCBI Taxon **9606**.
- **Mouse:** *Mus musculus*, NCBI Taxon **10090**; ortholog **Chek2**.
- **Other vertebrates:** CHEK2 orthologs are broadly conserved, but no well-established naturally occurring veterinary syndrome directly equivalent to human CHEK2-related cancer predisposition was identified.

There is no infectious transmission or zoonotic potential. Comparative relevance lies in conserved ATM–Chk2 checkpoint biology rather than cross-species transmission. Breed-specific VBO annotations and a validated naturally occurring companion-animal CHEK2 syndrome were not available from the retrieved evidence.

---

## 15. Model organisms and experimental systems

### Mouse models

**Chek2-null mice** are viable and fertile, show reduced p53-mediated responses and DSB-induced apoptosis, relative radioresistance, and only modest late spontaneous-tumor susceptibility. This indicates functional redundancy and is a limitation when modeling human moderate penetrance. (stolarova2020chek2germlinevariants pages 7-9, mustofa2020rolesofchk2chek2 pages 4-6)

**CHEK2 c.1100delC knock-in mice**, especially females, developed spontaneous tumors involving hormonally responsive/ER-expressing tissues, providing face validity for human breast susceptibility. **Chk1+/−;Chk2−/−** mice exhibit spontaneous DNA damage and progressive cancer susceptibility; **Chk2−/−;Rad18−/−** mice develop spontaneous lymphoma. Chk2 loss also increases DMBA- and UV-B-associated skin tumorigenesis. These models are particularly useful for studying pathway redundancy, replication stress, exposure interaction, apoptosis, and checkpoint failure. (mustofa2020rolesofchk2chek2 pages 6-8, mustofa2020rolesofchk2chek2 pages 4-6)

### Cellular and in-vitro models

CHEK2 knockout/knockdown cells, kinase assays, DNA-damage challenge systems, and variant-complementation assays evaluate Thr68 activation, autophosphorylation, substrate phosphorylation, and VUS function. Patient-derived breast-cancer cell lines or organoids can examine LOH and drug response, but no single model predicts clinical penetrance or PARP-inhibitor sensitivity.

### Limitations

Mouse tumor spectra and exposure doses do not reproduce human age-dependent, ancestry-dependent penetrance. Complete knockout can exaggerate effects relative to heterozygosity, while murine redundancy can understate human risk. In-vitro functional impairment is supporting evidence for pathogenicity, not by itself proof of clinical cancer risk.

---

## Recent developments and authoritative interpretation

1. **ACMG 2023:** reframed CHEK2 management around personalized continuous risk rather than a uniform syndrome protocol; recommended genetics input and cautioned that most lower-risk missense variants are not actionable in isolation. DOI: https://doi.org/10.1016/j.gim.2023.100870. (hanson2023managementofindividuals pages 18-20, hanson2023managementofindividuals pages 22-23)
2. **CARRIERS 2023:** quantified contralateral breast-cancer risk in 15,104 prospectively followed women, including 10-year incidences of 13% premenopausal and 4% postmenopausal among CHEK2 carriers. DOI: https://doi.org/10.1200/JCO.22.01239. (hanson2023managementofindividuals pages 23-25)
3. **2024 NCCN colorectal update:** removed CHEK2-only intensified colorectal screening because newer large cohorts do not show a clinically meaningful association.
4. **2024 pathology:** reinforced that CHEK2-associated breast cancer is predominantly ER-positive IDC/luminal disease and demonstrated somatic biallelic inactivation in a subset.
5. **2024 population research:** the Turkish cohort found CHEK2 variants in about 8% of 1,707 high-risk referrals and demonstrated substantial ancestry-specific frequency differences. DOI: https://doi.org/10.3390/cancers16223876. (ozdemir2024molecularandin pages 1-2)

### Representative short abstract quotations

- ACMG 2023: **“cancer risks may be considered as a continuous variable”** and are influenced by family history and other modifiers. (hanson2023managementofindividuals pages 18-20)
- Yadav et al. 2023: women with germline CHEK2 pathogenic variants were at **“significantly elevated risk”** of contralateral breast cancer. (hanson2023managementofindividuals pages 23-25)
- Mechanistic review: CHK2 is a **“critical mediator of the DNA damage response”** with roles in DSB-induced apoptosis and arrest. (mustofa2020rolesofchk2chek2 pages 6-8)

## Knowledge-base curation recommendations

The core assertion should be: **heterozygous pathogenic CHEK2 variants cause autosomal-dominant, moderate, incompletely penetrant predisposition to female breast cancer and contribute to prostate and contralateral breast-cancer risk**. Store risk by **variant class and specific allele**, not merely gene. Mark colorectal risk as disputed/de-implemented for gene-only surveillance and all other organ associations as limited unless new variant- and ancestry-specific evidence warrants upgrading. Separate germline predisposition, somatic tumor alteration, and clonal hematopoiesis. Do not encode VUS as causal, do not infer BRCA-like HR deficiency, and do not attach PARP-inhibitor actionability to CHEK2 alone. (stolarova2020chek2germlinevariants pages 9-11, hanson2023managementofindividuals pages 18-20, hanson2023managementofindividuals pages 22-23)

References

1. (hanson2023managementofindividuals pages 18-20): Helen Hanson, Esteban Astiazaran-Symonds, Laura M. Amendola, Judith Balmaña, William D. Foulkes, Paul James, Susan Klugman, Joanne Ngeow, Rita Schmutzler, Nicoleta Voian, Myra J. Wick, Tuya Pal, Marc Tischkowitz, and Douglas R. Stewart. Management of individuals with germline pathogenic/likely pathogenic variants in chek2: a clinical practice resource of the american college of medical genetics and genomics (acmg). Genetics in Medicine, 25(10):100870, Oct 2023. URL: https://doi.org/10.1016/j.gim.2023.100870, doi:10.1016/j.gim.2023.100870. This article has 103 citations and is from a highest quality peer-reviewed journal.

2. (hanson2023managementofindividuals pages 23-25): Helen Hanson, Esteban Astiazaran-Symonds, Laura M. Amendola, Judith Balmaña, William D. Foulkes, Paul James, Susan Klugman, Joanne Ngeow, Rita Schmutzler, Nicoleta Voian, Myra J. Wick, Tuya Pal, Marc Tischkowitz, and Douglas R. Stewart. Management of individuals with germline pathogenic/likely pathogenic variants in chek2: a clinical practice resource of the american college of medical genetics and genomics (acmg). Genetics in Medicine, 25(10):100870, Oct 2023. URL: https://doi.org/10.1016/j.gim.2023.100870, doi:10.1016/j.gim.2023.100870. This article has 103 citations and is from a highest quality peer-reviewed journal.

3. (hanson2023managementofindividuals pages 22-23): Helen Hanson, Esteban Astiazaran-Symonds, Laura M. Amendola, Judith Balmaña, William D. Foulkes, Paul James, Susan Klugman, Joanne Ngeow, Rita Schmutzler, Nicoleta Voian, Myra J. Wick, Tuya Pal, Marc Tischkowitz, and Douglas R. Stewart. Management of individuals with germline pathogenic/likely pathogenic variants in chek2: a clinical practice resource of the american college of medical genetics and genomics (acmg). Genetics in Medicine, 25(10):100870, Oct 2023. URL: https://doi.org/10.1016/j.gim.2023.100870, doi:10.1016/j.gim.2023.100870. This article has 103 citations and is from a highest quality peer-reviewed journal.

4. (stolarova2020chek2germlinevariants pages 15-17): Lenka Stolarova, Petra Kleiblova, Marketa Janatova, Jana Soukupova, Petra Zemankova, Libor Macurek, and Zdenek Kleibl. Chek2 germline variants in cancer predisposition: stalemate rather than checkmate. Dec 2020. URL: https://doi.org/10.3390/cells9122675, doi:10.3390/cells9122675. This article has 240 citations.

5. (hanson2023managementofindividuals pages 27-28): Helen Hanson, Esteban Astiazaran-Symonds, Laura M. Amendola, Judith Balmaña, William D. Foulkes, Paul James, Susan Klugman, Joanne Ngeow, Rita Schmutzler, Nicoleta Voian, Myra J. Wick, Tuya Pal, Marc Tischkowitz, and Douglas R. Stewart. Management of individuals with germline pathogenic/likely pathogenic variants in chek2: a clinical practice resource of the american college of medical genetics and genomics (acmg). Genetics in Medicine, 25(10):100870, Oct 2023. URL: https://doi.org/10.1016/j.gim.2023.100870, doi:10.1016/j.gim.2023.100870. This article has 103 citations and is from a highest quality peer-reviewed journal.

6. (stolarova2020chek2germlinevariants pages 7-9): Lenka Stolarova, Petra Kleiblova, Marketa Janatova, Jana Soukupova, Petra Zemankova, Libor Macurek, and Zdenek Kleibl. Chek2 germline variants in cancer predisposition: stalemate rather than checkmate. Dec 2020. URL: https://doi.org/10.3390/cells9122675, doi:10.3390/cells9122675. This article has 240 citations.

7. (stolarova2020chek2germlinevariants pages 41-43): Lenka Stolarova, Petra Kleiblova, Marketa Janatova, Jana Soukupova, Petra Zemankova, Libor Macurek, and Zdenek Kleibl. Chek2 germline variants in cancer predisposition: stalemate rather than checkmate. Dec 2020. URL: https://doi.org/10.3390/cells9122675, doi:10.3390/cells9122675. This article has 240 citations.

8. (ozdemir2024molecularandin pages 1-2): Ozkan Ozdemir, Brittany L. Bychkovsky, Busra Unal, Gizem Onder, Ufuk Amanvermez, Eylul Aydin, Berk Ergun, Ilayda Sahin, Merve Gokbayrak, Cansu Ugurtas, Merve Nur Koroglu, Berfin Cakir, Irem Kalay, Naci Cine, Ugur Ozbek, Huma Q. Rana, Ozden Hatirnaz Ng, and Nihat Bugra Agaoglu. Molecular and in silico analysis of the chek2 gene in individuals with high risk of cancer predisposition from türkiye. Nov 2024. URL: https://doi.org/10.3390/cancers16223876, doi:10.3390/cancers16223876. This article has 5 citations.

9. (stolarova2020chek2germlinevariants pages 9-11): Lenka Stolarova, Petra Kleiblova, Marketa Janatova, Jana Soukupova, Petra Zemankova, Libor Macurek, and Zdenek Kleibl. Chek2 germline variants in cancer predisposition: stalemate rather than checkmate. Dec 2020. URL: https://doi.org/10.3390/cells9122675, doi:10.3390/cells9122675. This article has 240 citations.

10. (hanson2023managementofindividuals pages 32-33): Helen Hanson, Esteban Astiazaran-Symonds, Laura M. Amendola, Judith Balmaña, William D. Foulkes, Paul James, Susan Klugman, Joanne Ngeow, Rita Schmutzler, Nicoleta Voian, Myra J. Wick, Tuya Pal, Marc Tischkowitz, and Douglas R. Stewart. Management of individuals with germline pathogenic/likely pathogenic variants in chek2: a clinical practice resource of the american college of medical genetics and genomics (acmg). Genetics in Medicine, 25(10):100870, Oct 2023. URL: https://doi.org/10.1016/j.gim.2023.100870, doi:10.1016/j.gim.2023.100870. This article has 103 citations and is from a highest quality peer-reviewed journal.

11. (OpenTargets Search: breast cancer,prostate cancer,colorectal cancer-CHEK2): Open Targets Query (breast cancer,prostate cancer,colorectal cancer-CHEK2, 9 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

12. (stolarova2020chek2germlinevariants pages 33-35): Lenka Stolarova, Petra Kleiblova, Marketa Janatova, Jana Soukupova, Petra Zemankova, Libor Macurek, and Zdenek Kleibl. Chek2 germline variants in cancer predisposition: stalemate rather than checkmate. Dec 2020. URL: https://doi.org/10.3390/cells9122675, doi:10.3390/cells9122675. This article has 240 citations.

13. (mustofa2020rolesofchk2chek2 pages 6-8): Md. Kawsar Mustofa, Yuki Tanoue, Chie Tateishi, Cyrus Vaziri, and Satoshi Tateishi. Roles of <scp>chk2</scp>/<scp>chek2</scp> in guarding against environmentally induced <scp>dna</scp> damage and replication‐stress. Jul 2020. URL: https://doi.org/10.1002/em.22397, doi:10.1002/em.22397. This article has 40 citations and is from a peer-reviewed journal.

14. (mustofa2020rolesofchk2chek2 pages 4-6): Md. Kawsar Mustofa, Yuki Tanoue, Chie Tateishi, Cyrus Vaziri, and Satoshi Tateishi. Roles of <scp>chk2</scp>/<scp>chek2</scp> in guarding against environmentally induced <scp>dna</scp> damage and replication‐stress. Jul 2020. URL: https://doi.org/10.1002/em.22397, doi:10.1002/em.22397. This article has 40 citations and is from a peer-reviewed journal.

15. (stolarova2020chek2germlinevariants pages 3-5): Lenka Stolarova, Petra Kleiblova, Marketa Janatova, Jana Soukupova, Petra Zemankova, Libor Macurek, and Zdenek Kleibl. Chek2 germline variants in cancer predisposition: stalemate rather than checkmate. Dec 2020. URL: https://doi.org/10.3390/cells9122675, doi:10.3390/cells9122675. This article has 240 citations.

16. (stolarova2020chek2germlinevariants pages 1-3): Lenka Stolarova, Petra Kleiblova, Marketa Janatova, Jana Soukupova, Petra Zemankova, Libor Macurek, and Zdenek Kleibl. Chek2 germline variants in cancer predisposition: stalemate rather than checkmate. Dec 2020. URL: https://doi.org/10.3390/cells9122675, doi:10.3390/cells9122675. This article has 240 citations.

17. (stolarova2020chek2germlinevariants pages 5-7): Lenka Stolarova, Petra Kleiblova, Marketa Janatova, Jana Soukupova, Petra Zemankova, Libor Macurek, and Zdenek Kleibl. Chek2 germline variants in cancer predisposition: stalemate rather than checkmate. Dec 2020. URL: https://doi.org/10.3390/cells9122675, doi:10.3390/cells9122675. This article has 240 citations.

18. (smith2020dnadamagecheckpoint pages 2-3): Hannah L. Smith, Harriet Southgate, Deborah A. Tweddle, and Nicola J. Curtin. Dna damage checkpoint kinases in cancer. Expert Reviews in Molecular Medicine, Jun 2020. URL: https://doi.org/10.1017/erm.2020.3, doi:10.1017/erm.2020.3. This article has 417 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CHEK2-related_Cancer_Predisposition-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 7 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0030766` (1 mention) - the report calls it "multifocal breast carcinoma*, if locally available"; HP calls it **Ear pain**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0090305` (obsolete nucleic acid phosphodiester bond hydrolysis) (1 mention) - replaced by `GO:0090304`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006974` (1 mention) - the report calls it "GO biological process:** DNA damage response"; GO calls it **DNA damage response**, and lists "cellular DNA damage response" among its other names
- `GO:0004674` (1 mention) - the report calls it "GO molecular function:** protein serine/threonine kinase activity"; GO calls it **protein serine/threonine kinase activity**
- `GO:0005634` (1 mention) - the report calls it "GO cellular component:** nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `CL:0002327` (1 mention) - the report calls it "Cell Ontology:** mammary epithelial cell"; CL calls it **mammary gland epithelial cell**, and lists "mammary epithelial cell" among its other names