---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-22T16:58:06.046557'
end_time: '2026-09-22T17:17:31.549671'
duration_seconds: 1165.5
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Deficiency 36
  mondo_id: MONDO:0054781
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 4
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 44
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 24
  labels_variant: 4
  unresolvable_prefixes:
  - OMIM
  - NCBIGene
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Oxidative_Phosphorylation_Deficiency_36-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Oxidative_Phosphorylation_Deficiency_36-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Deficiency 36
- **MONDO ID:** MONDO:0054781 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Deficiency 36** covering all of the
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

# Combined Oxidative Phosphorylation Deficiency 36 (COXPD36): Comprehensive Disease Characterization Report

**Disease:** Combined Oxidative Phosphorylation Deficiency 36 (COXPD36)
**MONDO ID:** MONDO:0054781 · **OMIM:** #617950 · **Category:** Mendelian (autosomal recessive mitochondrial disease)
**Causal gene:** *MRPS2* (HGNC:14495; NCBI Gene 51116; chr 9q34.3)
**Prepared:** 2026-09-22 · Evidence base: human clinical case reports + in vitro functional (rescue) studies. No dedicated animal model or omics dataset yet published.

---

## Summary

Combined Oxidative Phosphorylation Deficiency 36 (COXPD36) is an ultra-rare, autosomal-recessive mitochondrial disease caused by biallelic (homozygous or compound-heterozygous) missense mutations in *MRPS2*, the gene encoding **uS2m** (mitochondrial ribosomal protein S2), a structural constituent of the small (28S) subunit of the mitoribosome. The disease was first defined in 2018 by Gardeitchik and colleagues, who identified *MRPS2* mutations by exome sequencing in two unrelated affected individuals in a gene "which has not previously been implicated in disease" ([PMID: 29576219](https://pubmed.ncbi.nlm.nih.gov/29576219/)). To date only approximately **4–5 patients worldwide** have been reported, making COXPD36 one of the rarest recognized mitochondrial translation disorders.

Mechanistically, the pathogenic missense variants **destabilize the MRPS2 protein**, lowering its steady-state abundance. Complexome profiling demonstrated that this loss **prevents assembly of the small mitoribosomal subunit**, which in turn **inhibits mitochondrial translation** of the 13 mtDNA-encoded OXPHOS subunits, producing a **combined deficiency of multiple oxidative phosphorylation complexes** detectable in muscle, liver, and cultured fibroblasts. Re-introduction of wild-type MRPS2 rescues both translation and OXPHOS assembly, confirming causality. The clinical presentation is dominated by a characteristic triad of **sensorineural hearing loss, hypoglycemia, and lactic acidemia**, with variable developmental delay, hypotonia, hepatic and muscular involvement, and — in individually reported cases — microcephaly, joint hypermobility, autistic features, and gallstones.

There is no disease-specific or curative therapy. Management follows the general supportive standards for primary mitochondrial disease (symptomatic control of hypoglycemia and lactic acidosis, hearing rehabilitation, developmental support, avoidance of mitochondrial toxins). Diagnosis rests on the combination of biochemical findings (lactic acidemia, hypoglycemia, elevated alanine, combined OXPHOS enzyme deficiencies on biopsy) and molecular confirmation by exome/genome sequencing. Because the phenotype overlaps broadly with other mitochondrial translation defects, molecular genetic testing is essential for definitive diagnosis. This report synthesizes seven confirmed findings across all 15 requested characterization domains, with ontology annotations and primary-literature citations.

---

## Key Findings

### Finding 1 — COXPD36 is caused by biallelic (autosomal recessive) mutations in *MRPS2*

COXPD36 is a Mendelian, autosomal-recessive disorder. Ontology cross-references establish the identity of the disease across knowledge bases: **MONDO:0054781 = OMIM #617950 = MedGen C4693722 = GARD 0025974 = DOID:0111482**. The Monarch Initiative lists *MRPS2* (HGNC:14495, chromosome 9q34.3) as the CausalGeneToDiseaseAssociation for this entity.

The founding study, *Gardeitchik et al., 2018 (American Journal of Human Genetics)*, identified *MRPS2* mutations by exome sequencing in two unrelated subjects and explicitly noted the novelty of the gene: *"we identified mutations in the gene encoding the mitochondrial ribosomal protein S2, which has not previously been implicated in disease"* ([PMID: 29576219](https://pubmed.ncbi.nlm.nih.gov/29576219/)).

Reported pathogenic / likely-pathogenic variants are all **missense** changes in *MRPS2* (transcript NM_016034.5):

| cDNA variant | Protein change | Classification | Source |
|---|---|---|---|
| c.328C>T | p.Arg110Cys | Pathogenic (ClinVar) | Gardeitchik 2018 |
| c.340G>A | p.Asp114Asn | Pathogenic / likely pathogenic | Gardeitchik 2018 |
| c.413G>A | p.Arg138His | Pathogenic / likely pathogenic | Gardeitchik 2018 |
| c.412C>G | (novel, Chinese case) | Reported pathogenic | Liu 2022 ([PMID: 34991560](https://pubmed.ncbi.nlm.nih.gov/34991560/)) |

The recurrent variant class (missense affecting conserved residues of the ribosomal S2 domain) and the recessive inheritance pattern are consistent across all reported families.

### Finding 2 — Mechanism: MRPS2 mutations destabilize the protein, block small-subunit assembly, and impair mitochondrial translation

The core pathophysiology was demonstrated experimentally in the founding study. Patient fibroblasts showed **decreased steady-state levels of mutant MRPS2**. Using **complexome profiling**, the authors showed that this decrease **prevents the assembly of the small mitoribosomal subunit (mt-SSU / 28S)**. Because the mitoribosome is required to translate the 13 mtDNA-encoded core subunits of the OXPHOS complexes, the assembly failure **inhibits mitochondrial translation**, producing a **combined OXPHOS deficiency** in patient muscle and liver biopsies and in cultured skin fibroblasts.

In the authors' words: *"this decrease was shown by complexome profiling to prevent the assembly of the small mitoribosomal subunit. In turn, mitochondrial translation was inhibited, resulting in a combined OXPHOS deficiency detectable in subjects' muscle and liver biopsies as well as in cultured skin fibroblasts"* ([PMID: 29576219](https://pubmed.ncbi.nlm.nih.gov/29576219/)). Critically, **re-introduction of wild-type MRPS2 rescued** mitochondrial translation and OXPHOS assembly, establishing loss-of-function causality rather than correlation.

### Finding 3 — Core clinical phenotype: sensorineural hearing loss, hypoglycemia, lactic acidemia, developmental delay

Across the reported cases, a consistent clinical core emerges. Gardeitchik 2018 described two unrelated subjects with **sensorineural hearing impairment, mild developmental delay, hypoglycemia, and combined OXPHOS deficiency**, emphasizing the characteristic combination of **lactic acidemia, hypoglycemia, and sensorineural hearing loss**.

Subsequent case reports expanded the spectrum:
- **Liu et al., 2022** (Chinese girl, novel c.412C>G): *"The clinical manifestations included recurrent vomiting, hypoglycemia, lactic acidosis, sensorineural hearing loss, and gall bladder calculi"* ([PMID: 34991560](https://pubmed.ncbi.nlm.nih.gov/34991560/)) — adding gallstones as a novel feature.
- **Papadopoulos et al., 2024** described a new homozygous patient with previously unreported features: *"a new MRPS2 homozygous subject who shows particular features which have not yet been reported: initial microcephaly, joint hypermobility and autistic features"* ([PMID: 38029925](https://pubmed.ncbi.nlm.nih.gov/38029925/)), broadening the recognized phenotype.

### Finding 4 — MRPS2 is a 28S small-subunit mitoribosomal protein; disease localizes to high-OXPHOS-demand tissues

*MRPS2* (NCBI Gene 51116; ENSG00000122140; 9q34.3; aliases uS2m, S2mt) carries Gene Ontology annotations that place it firmly in the mitochondrial translation machinery:

| GO aspect | Term | ID |
|---|---|---|
| Cellular component | mitochondrial matrix | GO:0005759 |
| Cellular component | small mitochondrial ribosomal subunit | GO:0005763 |
| Cellular component | mitochondrial inner membrane | GO:0005743 |
| Biological process | mitochondrial translation | GO:0032543 |
| Biological process | mitochondrial ribosome assembly | GO:0061668 |
| Molecular function | structural constituent of ribosome | GO:0003735 |

The clinically affected tissues are precisely the **high-oxidative-demand organs**: cochlea/inner ear (hearing loss), brain (developmental delay), and liver and skeletal muscle (combined OXPHOS deficiency demonstrated on biopsy) — consistent with a systemic defect of mitochondrial energy production that manifests first where ATP demand is greatest.

### Finding 5 — MRPS2 protein (uS2m, UniProt Q9Y399) is a conserved structural component of the 28S mt-SSU resolved in cryo-EM mitoribosome structures

UniProt **Q9Y399** annotates MRPS2 as *"Small ribosomal subunit protein uS2m,"* a 296-amino-acid protein *"Required for mitoribosome formation and stability, and mitochondrial translation."* It contains the **Ribosomal_S2 domain (Pfam PF00318)** and belongs to the universal uS2 protein family (InterPro IPR001865/IPR005706, spanning bacterial, mitochondrial, and plastid ribosomes). MRPS2 is resolved as a component in **>60 cryo-EM structures** of the human/mammalian mitoribosome (e.g., PDB 3J9M, 6NU2, 6RW4, 6ZM5), confirming its integral structural role in the small subunit. The mouse ortholog *Mrps2* is NCBI Gene 118451.

### Finding 6 — Authoritative HPO annotation set defines the curated phenotype spectrum

The JAX Human Phenotype Ontology annotations for OMIM:617950 (MONDO:0054781; gene *MRPS2*/NCBIGene:51116) comprise **22 curated terms** organized by system:

| System | Phenotype | HPO ID |
|---|---|---|
| Ear | Sensorineural hearing impairment | HP:0000407 |
| Ear | Low-set ears | HP:0000369 |
| Metabolism | Hypoglycemia | HP:0001943 |
| Metabolism | Increased circulating lactate | HP:0002151 |
| Metabolism | Hyperalaninemia | HP:0003348 |
| Metabolism | Elevated ALT | HP:0031964 |
| Metabolism | Elevated AST | HP:0031956 |
| Metabolism | Aciduria | HP:0012072 |
| Nervous system | Global developmental delay | HP:0001263 |
| Nervous system | Intellectual disability | HP:0001249 |
| Nervous system | Poor speech | HP:0002465 |
| Nervous system | Headache | HP:0002315 |
| Musculature | Hypotonia | HP:0001252 |
| Constitutional | Exercise intolerance | HP:0003546 |
| Constitutional | Myalgia | HP:0003326 |
| Limbs | Lower limb muscle weakness | HP:0007340 |
| Growth | Failure to thrive | HP:0001508 |
| Eye | Exodeviation | HP:0020049 |
| Head/neck | Upslanted palpebral fissure | HP:0000582 |
| Skin | Premature skin wrinkling | HP:0100678 |
| Course | Infantile onset | HP:0003593 |
| Inheritance | Autosomal recessive | HP:0000007 |

Frequencies are not curated (blank in the HPO source), and no curated HPO medical actions are listed — reflecting the disorder's rarity and the small evidence base.

### Finding 7 — Integrated mutation-to-phenotype model with full ontology annotations

Synthesizing the above: biallelic missense variants in *MRPS2* (HGNC:14495; NCBIGene:51116; UniProt Q9Y399/uS2m; 9q34.3) — c.328C>T/p.Arg110Cys (pathogenic), c.340G>A, c.413G>A, and c.412C>G — cause autosomal-recessive COXPD36 (MONDO:0054781; OMIM #617950). The mechanism is confirmed by complexome profiling plus wild-type rescue (Gardeitchik 2018, [PMID: 29576219](https://pubmed.ncbi.nlm.nih.gov/29576219/)). Twenty-two curated HPO terms anchor the phenotype; ~4–5 patients are reported worldwide ([PMID: 29576219](https://pubmed.ncbi.nlm.nih.gov/29576219/), [PMID: 34991560](https://pubmed.ncbi.nlm.nih.gov/34991560/), [PMID: 38029925](https://pubmed.ncbi.nlm.nih.gov/38029925/)); management is supportive per Mitochondrial Medicine Society standards ([PMID: 34505344](https://pubmed.ncbi.nlm.nih.gov/34505344/)). No animal model, omics cohort, or clinical trial exists for this specific disease.

---

## Section-by-Section Characterization

### 1. Disease Information

COXPD36 is a Mendelian mitochondrial oxidative phosphorylation disorder resulting from defective mitochondrial protein synthesis. **Key identifiers:** MONDO:0054781; OMIM #617950; MedGen C4693722; GARD 0025974; DOID:0111482. There is no dedicated Orphanet number distinct from the broader "combined oxidative phosphorylation deficiency" grouping, and no specific ICD-10/ICD-11 code (it falls under mitochondrial metabolism disorders, e.g., ICD-10 E88.4 "Mitochondrial metabolism disorders"; ICD-11 5C53.1). **Synonyms/alternative names:** "Combined oxidative phosphorylation deficiency 36"; "COXPD36"; "MRPS2 deficiency"; "mitochondrial ribosomal protein S2 deficiency." The information is derived from **aggregated disease-level resources** (OMIM, HPO, ClinVar) plus a small number of **individual patient case reports** — not from EHR or large registries.

### 2. Etiology

**Causal factor:** purely genetic — biallelic loss-of-function/destabilizing missense mutations in *MRPS2*. **Genetic risk factors:** the only established risk factor is inheritance of two pathogenic *MRPS2* alleles; **consanguinity** increases the risk of homozygosity (several reported cases are homozygous). No modifier genes, susceptibility loci, environmental risk factors, protective factors, or gene–environment interactions have been identified — expected given the ultra-rare, monogenic nature of the disease. **No environmental or infectious contribution** is known.

### 3. Phenotypes

The phenotype is a systemic mitochondrial energy-deficiency syndrome. **Laboratory abnormalities** (biochemical): lactic acidemia (HP:0002151), hypoglycemia (HP:0001943), hyperalaninemia (HP:0003348), elevated transaminases (HP:0031964, HP:0031956), aciduria (HP:0012072). **Clinical signs/symptoms:** sensorineural hearing loss (HP:0000407), global developmental delay (HP:0001263), intellectual disability (HP:0001249), hypotonia (HP:0001252), failure to thrive (HP:0001508), exercise intolerance (HP:0003546), myalgia (HP:0003326), muscle weakness (HP:0007340). **Dysmorphic/physical:** low-set ears, upslanted palpebral fissures, premature skin wrinkling, microcephaly (case-specific), joint hypermobility (case-specific). **Behavioral:** autistic features (case-specific, Papadopoulos 2024). **Onset:** infantile (HP:0003593). **Severity/progression:** variable; energy-crisis features (hypoglycemia, lactic acidosis) can be episodic and provoked by catabolic stress. Frequencies are not curated because of the tiny cohort. **Quality-of-life impact:** substantial — hearing loss, developmental delay, and metabolic instability affect communication, learning, and daily functioning; no formal QoL instrument data exist.

### 4. Genetic/Molecular Information

**Causal gene:** *MRPS2* (HGNC:14495; NCBI Gene 51116; ENSG00000122140; 9q34.3; OMIM *610760). **Variant type/class:** exclusively **missense** to date (no reported frameshift, nonsense, splice, or structural variants), affecting conserved residues of the ribosomal S2 domain. **Classification:** c.328C>T/p.Arg110Cys is ClinVar Pathogenic; c.340G>A/p.Asp114Asn and c.413G>A/p.Arg138His are pathogenic/likely pathogenic; c.412C>G reported pathogenic in a Chinese case. **Allele frequency:** these are private/ultra-rare variants, essentially absent or extremely rare in gnomAD. **Origin:** germline. **Functional consequence:** loss of function via protein destabilization and reduced steady-state abundance leading to failed mt-SSU assembly. **Modifier genes / epigenetics / chromosomal abnormalities:** none identified.

### 5. Environmental Information

Not applicable. No environmental toxins, lifestyle factors, or infectious agents are implicated in causation. As with other mitochondrial disorders, catabolic stressors (fasting, infection, fever) may **precipitate** metabolic decompensation but do not cause the disease.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. Biallelic missense mutation in *MRPS2* (e.g., c.328C>T/p.Arg110Cys) **alters a conserved residue of uS2m** →
2. **destabilizes the MRPS2 protein**, reducing its steady-state level in mitochondria (demonstrated in patient fibroblasts) →
3. loss of assembled MRPS2 **prevents assembly of the small (28S) mitoribosomal subunit** (demonstrated by complexome profiling) →
4. deficient mt-SSU **impairs mitochondrial translation** of the 13 mtDNA-encoded OXPHOS subunits →
5. results in a **combined deficiency of multiple OXPHOS complexes** (complexes I, III, IV, V share mtDNA-encoded subunits) in muscle, liver, and fibroblasts →
6. **impaired mitochondrial ATP production and increased anaerobic glycolysis** →
7. produces **lactic acidemia + hypoglycemia** (energy shortfall) and **tissue-specific dysfunction** in high-energy organs →
8. branches to: **cochlear dysfunction → sensorineural hearing loss**; **CNS energy deficit → developmental delay/intellectual disability**; **hepatic involvement → transaminitis/hypoglycemia**; **skeletal-muscle involvement → hypotonia, exercise intolerance, myalgia**.

*Rescue confirmation:* re-expression of wild-type MRPS2 restores translation and OXPHOS assembly ([PMID: 29576219](https://pubmed.ncbi.nlm.nih.gov/29576219/)).

```
 MRPS2 missense mutation (germline, biallelic)
        │  destabilizes protein
        ▼
 ↓ steady-state uS2m ──▶ mt-SSU (28S) assembly fails
        │                         (complexome profiling)
        ▼
 mitochondrial translation inhibited
        │
        ▼
 combined OXPHOS deficiency (multiple complexes)
        │
   ┌────┼─────────┬──────────────┬───────────────┐
   ▼    ▼         ▼              ▼               ▼
 cochlea  brain   liver        muscle       systemic
 hearing  dev.    hypoglycemia hypotonia    lactic
 loss     delay   transaminitis myalgia     acidemia
```

**Pathways/processes:** mitochondrial translation (GO:0032543), mitochondrial ribosome assembly (GO:0061668), oxidative phosphorylation (Reactome R-HSA-1428517). **Upstream:** MRPS2 destabilization and mt-SSU assembly failure. **Downstream:** OXPHOS enzyme deficiency and bioenergetic failure. **Cell types (CL):** cochlear hair cells (CL:0000202), neurons (CL:0000540), hepatocytes (CL:0000182), skeletal muscle fibers (CL:0000188). **Subcellular (GO CC):** mitochondrial matrix (GO:0005759), small mitoribosomal subunit (GO:0005763), mitochondrial inner membrane (GO:0005743). No disease-specific transcriptomic/proteomic/metabolomic/single-cell datasets exist.

### 7. Anatomical Structures Affected

**Primary organs/systems:** inner ear/cochlea (UBERON:0001844), brain (UBERON:0000955), liver (UBERON:0002107), skeletal muscle (UBERON:0001134). **Body systems:** nervous, auditory, hepatic, musculoskeletal, and systemic metabolic. **Tissues:** neural, hepatic epithelial, striated muscle. **Cells:** cochlear hair cells (CL:0000202), neurons (CL:0000540), hepatocytes (CL:0000182), myocytes (CL:0000187). **Subcellular:** mitochondria (GO:0005739), specifically the mitochondrial matrix and inner membrane. **Lateralization:** bilateral/systemic (hearing loss bilateral).

### 8. Temporal Development

**Onset:** infantile/congenital-to-early-childhood (HP:0003593). **Pattern:** typically chronic with superimposed episodic metabolic crises (hypoglycemia, lactic acidosis) triggered by catabolic stress. **Progression:** variable; developmental delay is persistent, hearing loss is stable-to-progressive. **Duration:** chronic, lifelong. **Critical periods:** neonatal/infantile metabolic decompensations are windows of vulnerability; early hearing rehabilitation and metabolic management are opportunities for intervention. No natural-history study exists given the tiny cohort.

### 9. Inheritance and Population

**Inheritance:** autosomal recessive (HP:0000007). **Epidemiology:** ultra-rare — only ~4–5 patients reported worldwide; true prevalence/incidence unknown (well below Orphanet's <1/1,000,000 ultra-rare threshold). **Penetrance:** presumed complete in biallelic carriers (too few cases to quantify). **Expressivity:** variable (e.g., microcephaly, autistic features, gallstones in individual cases). **Consanguinity:** relevant — homozygous cases reported. **Founder effects/carrier frequency:** none established; variants are private. **Anticipation/germline mosaicism:** not reported/not applicable. **Populations:** reported in European and Chinese individuals; no ethnic predilection established. **Sex ratio:** no established skew (both sexes reported).

### 10. Diagnostics

**Biochemical/laboratory:** elevated blood lactate, hypoglycemia, hyperalaninemia, elevated ALT/AST, organic aciduria; enzymatic assay of respiratory-chain complexes in muscle/liver/fibroblasts showing **combined (multiple-complex) OXPHOS deficiency**. **Biopsy:** muscle and liver biopsies demonstrate combined OXPHOS enzyme deficiency (Gardeitchik 2018). **Genetic testing (definitive):** exome or genome sequencing identifying biallelic *MRPS2* variants; single-gene testing or mitochondrial/nuclear gene panels covering *MRPS2* are alternatives. WES/WGS is the practical route because the phenotype is nonspecific. **Functional confirmation** (research): complexome profiling of mt-SSU assembly, mitochondrial translation assays, wild-type rescue. **Clinical criteria:** no disease-specific diagnostic criteria; diagnosis follows general mitochondrial-disease frameworks plus molecular confirmation. **Differential diagnosis:** other combined OXPHOS deficiencies and mitochondrial translation defects (other *MRPS*/*MRPL* genes, aminoacyl-tRNA synthetases such as *EARS2*/*AARS2*), MELAS and other mtDNA disorders — distinguished by gene-specific testing. **Screening:** no newborn screening; cascade carrier testing possible within affected families.

### 11. Outcome / Prognosis

Prognosis is guarded and variable given the small evidence base. Reported patients survived infancy with chronic disability; outcomes depend on severity of metabolic instability and CNS involvement. **Morbidity** includes permanent sensorineural hearing loss, developmental delay/intellectual disability, and risk of metabolic decompensation. No survival statistics, life-expectancy data, or validated prognostic biomarkers exist. Lactate and glucose stability, and the degree of neurodevelopmental involvement, are reasonable clinical prognostic indicators. **Complications:** recurrent hypoglycemia/lactic acidosis, failure to thrive, and (case-specific) gallstones.

### 12. Treatment

**No disease-specific or curative therapy exists.** Management is **supportive**, following primary mitochondrial-disease standards ([PMID: 34505344](https://pubmed.ncbi.nlm.nih.gov/34505344/)): prevention/treatment of hypoglycemia (avoid fasting, provide carbohydrate support during illness), management of lactic acidosis, nutritional support for failure to thrive, hearing rehabilitation (hearing aids/cochlear implants), developmental/educational support, and physical/occupational therapy. "Mitochondrial cocktail" supplements (e.g., coenzyme Q10, riboflavin, thiamine, L-carnitine) are often used empirically in mitochondrial disease but have **no proven efficacy specifically for COXPD36**. **Pharmacogenomics/gene/cell/RNA/targeted/immunotherapies:** none developed for this disease. **Experimental trials:** no COXPD36-specific clinical trials (NCT) exist. NCIT annotations: supportive care (NCIT:C133421), symptomatic treatment.

### 13. Prevention

**Primary prevention** is genetic: **genetic counseling** for at-risk families, carrier testing of relatives, and reproductive options including **prenatal diagnosis** or **preimplantation genetic testing (PGT-M)** once the familial *MRPS2* variants are known. Avoidance of consanguineous partnerships reduces recessive-disease risk at the population level. **Secondary/tertiary prevention:** early recognition and aggressive management of metabolic crises, avoidance of mitochondrial-toxic drugs, and prompt hearing/developmental intervention to limit complications. No vaccine, public-health, or environmental prevention applies.

### 14. Other Species / Natural Disease

No naturally occurring animal disease equivalent to COXPD36 has been documented (OMIA lists no *MRPS2* entry for this phenotype). **Orthologs:** mouse *Mrps2* (NCBI Gene 118451); the uS2 protein family is universally conserved across bacteria, mitochondria, and plastids (InterPro IPR001865/IPR005706), underscoring deep evolutionary conservation of the mitoribosomal small-subunit function. No zoonotic or cross-species transmission is relevant (non-infectious genetic disease).

### 15. Model Organisms

**No published *Mrps2* animal model of COXPD36 exists.** The disease mechanism has been studied only in **patient-derived cultured skin fibroblasts** and via **in vitro complexome/translation assays with wild-type rescue** ([PMID: 29576219](https://pubmed.ncbi.nlm.nih.gov/29576219/)). A conditional or knock-in mouse (*Mrps2*, Gene 118451) would be expected to be embryonic-lethal if null (as for other essential mitoribosomal proteins), so a hypomorphic/knock-in strategy modeling patient missense alleles would be required. Yeast and other model systems are informative for general mitoribosome biology but not disease-specific. This is a clear resource gap (see Follow-up).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [29576219](https://pubmed.ncbi.nlm.nih.gov/29576219/) | *Bi-allelic Mutations in MRPS2 Cause Sensorineural Hearing Loss, Hypoglycemia, and Multiple OXPHOS Complex Deficiencies* (Gardeitchik et al., AJHG 2018) | **Foundational.** Identifies *MRPS2* as causal gene; establishes mechanism (protein destabilization → mt-SSU assembly failure → translation inhibition → combined OXPHOS deficiency) with complexome profiling and wild-type rescue; defines core phenotype. |
| [34991560](https://pubmed.ncbi.nlm.nih.gov/34991560/) | *Hypoglycemia with lactic acidosis caused by a new MRPS2 gene mutation in a Chinese girl* (Liu et al., 2022) | Third patient; novel variant c.412C>G; adds gallstones; confirms core triad (recurrent vomiting, hypoglycemia, lactic acidosis, sensorineural hearing loss). |
| [38029925](https://pubmed.ncbi.nlm.nih.gov/38029925/) | *New description of an MRPS2 homozygous patient* (Papadopoulos et al., 2024) | Expands phenotype with newly reported features: initial microcephaly, joint hypermobility, autistic features. |
| [34505344](https://pubmed.ncbi.nlm.nih.gov/34505344/) | *Patient care standards for primary mitochondrial disease* (Australian adaptation of Mitochondrial Medicine Society recommendations) | Supports the supportive-care management framework in the absence of disease-specific therapy. |

Supporting ontology/database evidence (non-PMID): OMIM #617950; MONDO:0054781; HPO annotations for OMIM:617950 (22 terms); UniProt Q9Y399; GO annotations for MRPS2; Pfam PF00318 / InterPro IPR001865; PDB mitoribosome structures (3J9M, 6NU2, 6RW4, 6ZM5); ClinVar variant classifications.

Other papers surfaced during literature searches (e.g., SIRM metabolomics reviews, MELAS case reports, the Friedreich's ataxia NAD⁺/exercise trial) provide **contextual background on mitochondrial disease biology and general supportive/experimental approaches** but do **not** address COXPD36 or *MRPS2* directly, and are not used to support disease-specific claims.

---

## Mechanistic Model / Interpretation

COXPD36 is best understood as a **mitochondrial translation disorder** — a subclass of combined OXPHOS deficiencies in which the primary lesion is not in an OXPHOS structural gene but in the machinery that synthesizes OXPHOS subunits. Because the mitoribosome translates all 13 mtDNA-encoded OXPHOS core subunits, a small-subunit assembly defect produces a **generalized, multi-complex ("combined") deficiency**, distinguishing it from isolated single-complex deficiencies. The tissue distribution of disease (cochlea, brain, liver, muscle) reflects **relative bioenergetic dependence**: neurons and cochlear hair cells are exquisitely ATP-dependent, and hepatic/muscle metabolism is destabilized during catabolic stress, explaining the episodic hypoglycemia and lactic acidosis.

The evidence chain is unusually clean for an ultra-rare disorder because the founding study coupled human genetics with a **functional rescue experiment**: identification of biallelic missense variants, demonstration of reduced mutant protein, complexome evidence of mt-SSU assembly failure, and restoration of function by wild-type MRPS2. This satisfies causality criteria (association + mechanism + rescue) and anchors confidence in the gene–disease relationship. The variant spectrum (all missense, all affecting conserved S2-domain residues) is consistent with **destabilizing hypomorphic alleles** rather than complete nulls — biologically plausible because complete loss of an essential mitoribosomal protein would likely be embryonic-lethal.

---

## Supported and Refuted Hypotheses

No formal hypotheses were tested statistically in this investigation; the work was a structured literature/knowledge-base synthesis. The central mechanistic model — *MRPS2* destabilization → mt-SSU assembly failure → mitochondrial translation defect → combined OXPHOS deficiency → clinical triad — is **supported** by direct experimental evidence including a wild-type rescue experiment ([PMID: 29576219](https://pubmed.ncbi.nlm.nih.gov/29576219/)). No competing causal model was found in the literature.

---

## Limitations and Knowledge Gaps

1. **Tiny cohort (~4–5 patients):** frequencies, penetrance, expressivity, natural history, and prognosis cannot be quantified; HPO frequencies are uncurated.
2. **No animal or cellular disease model beyond patient fibroblasts:** limits mechanistic dissection and therapeutic testing.
3. **No omics cohort:** no disease-specific transcriptomic, proteomic, or metabolomic signatures; no biomarkers beyond generic mitochondrial markers (lactate, alanine).
4. **No therapeutics pipeline:** no trials, no targeted therapy, and no evidence base for the "mitochondrial cocktail" in this specific disorder.
5. **Narrow variant spectrum:** only missense variants reported; the pathogenicity landscape (e.g., LoF, structural variants) is uncharacterized.
6. **Genotype–phenotype correlations unknown:** drivers of variable features (microcephaly, autism, gallstones) are unexplained.
7. **No formal QoL or disability data.**

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry / GeneMatcher outreach** to aggregate additional *MRPS2* cases, enabling frequency, penetrance, and natural-history estimates.
2. **Generate a knock-in mouse or zebrafish model** carrying a patient missense allele (e.g., p.Arg110Cys) — a conditional/hypomorphic strategy to avoid lethality — to characterize tissue-specific pathology and test interventions.
3. **Deep functional characterization** of each reported variant (steady-state protein, mt-SSU assembly, translation rate, OXPHOS assembly) in isogenic cell lines to build a variant-pathogenicity map for clinical interpretation.
4. **Multi-omics profiling** (transcriptomics, proteomics, metabolomics) of patient fibroblasts and iPSC-derived neurons/hepatocytes to identify candidate biomarkers and therapeutic targets.
5. **iPSC-derived cochlear organoids and cortical neurons** to model the two most disabling phenotypes (hearing loss, developmental delay) and screen candidate compounds.
6. **Systematic evaluation of "mitochondrial cocktail" components and NAD⁺ precursors** in patient-derived models before any empiric clinical use.
7. **Standardized clinical data collection** (audiology, developmental assessment, metabolic-crisis frequency, QoL instruments) to define prognostic factors.

---

## Consensus Answer

Combined Oxidative Phosphorylation Deficiency 36 (COXPD36; MONDO:0054781, OMIM #617950) is an ultra-rare autosomal-recessive mitochondrial disease caused by biallelic missense mutations in *MRPS2*, which encodes uS2m, a structural protein of the small (28S) subunit of the mitoribosome; the mutations destabilize MRPS2 and block small-subunit assembly, impairing mitochondrial translation and causing a combined deficiency of multiple OXPHOS complexes. It presents in infancy with a characteristic triad of sensorineural hearing loss, hypoglycemia, and lactic acidemia, alongside variable developmental delay and hepatic/muscular involvement; only ~4–5 patients have been reported worldwide, and management is supportive with no disease-specific therapy.


## Artifacts

- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Deficiency_36-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Deficiency_36-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 28 |
| Terms named correctly | 24 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 4 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002151` (2 mentions) - the report calls it "Increased circulating lactate"; HP calls it **Increased circulating lactate concentration**
- `HP:0031964` (2 mentions) - the report calls it "Elevated ALT"; HP calls it **Elevated circulating alanine aminotransferase concentration**, and lists "Elevated serum ALT" among its other names
- `HP:0031956` (2 mentions) - the report calls it "Elevated AST"; HP calls it **Elevated circulating aspartate aminotransferase concentration**, and lists "Elevated serum AST" among its other names
- `HP:0000007` (2 mentions) - the report calls it "Autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `NCBIGene`.

41 of 44 terms resolved to a current term; the rest could not be looked up either way.