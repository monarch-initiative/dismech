---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-09T13:29:36.183684'
end_time: '2026-09-09T14:08:01.590654'
duration_seconds: 2305.41
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Cystic Leukoencephalopathy Without Megalencephaly
  mondo_id: MONDO:0013058
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
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 25
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 1
  labels_variant: 3
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Cystic_Leukoencephalopathy_Without_Megalencephaly-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cystic_Leukoencephalopathy_Without_Megalencephaly-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cystic Leukoencephalopathy Without Megalencephaly
- **MONDO ID:** MONDO:0013058 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cystic Leukoencephalopathy Without Megalencephaly** covering all of the
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

# Cystic Leukoencephalopathy Without Megalencephaly (RNASET2-Deficient Cystic Leukoencephalopathy) — Comprehensive Disease Report

**Disease:** Cystic Leukoencephalopathy Without Megalencephaly
**MONDO ID:** MONDO:0013058 · **OMIM:** #612951 · **Orphanet:** ORPHA:210141
**Causal gene:** *RNASET2* (6q27; HGNC:14015; alias RNASE6PL; NCBI Gene 8635; UniProt O00584) · **Inheritance:** Autosomal recessive
**Category:** Mendelian, ultra-rare leukoencephalopathy / type I interferonopathy / lysosomal storage disorder

---

## Summary

Cystic Leukoencephalopathy Without Megalencephaly is an **ultra-rare, autosomal-recessive infantile leukoencephalopathy** caused by **biallelic loss-of-function variants in *RNASET2*** on chromosome 6q27, which encodes a conserved, glycosylated lysosomal T2-family acid ribonuclease. It was first defined molecularly by Henneke and colleagues in 2009, who recognized that the disorder produces a clinical and neuroradiological picture **indistinguishable from congenital cytomegalovirus (CMV) brain infection** — yet with negative CMV testing — making it a striking **Mendelian mimic** of an acquired congenital infection ([PMID: 19525954](https://pubmed.ncbi.nlm.nih.gov/19525954/)).

The disease sits at the intersection of three mechanistic classes. It is a **lysosomal storage disorder**: RNase T2 normally degrades ribosomal RNA (rRNA) inside lysosomes, and its loss causes undigested rRNA to accumulate in neuronal lysosomes (demonstrated in zebrafish, [PMID: 21199949](https://pubmed.ncbi.nlm.nih.gov/21199949/)). It is also a **type I interferonopathy**: the stored lysosomal RNA aberrantly engages endolysosomal RNA-sensing Toll-like receptors (TLR13 in mice, TLR8 inferred in humans), igniting an **IFNAR1-dependent type I interferon response** with microglial pyroptosis and infiltration of CD8+ T cells and inflammatory monocytes into brain parenchyma (mouse models, [PMID: 34764281](https://pubmed.ncbi.nlm.nih.gov/34764281/); [PMID: 39853306](https://pubmed.ncbi.nlm.nih.gov/39853306/); [PMID: 41453865](https://pubmed.ncbi.nlm.nih.gov/41453865/)). This places it in clinical and pathological overlap with **Aicardi–Goutières syndrome (AGS)** ([PMID: 27091087](https://pubmed.ncbi.nlm.nih.gov/27091087/)).

Clinically, the disorder presents in infancy with a **largely static, severe encephalopathy** — profound psychomotor impairment, spasticity, epilepsy, and sometimes microcephaly, hearing loss, or dystonia. The neuroradiological hallmarks are **bilateral anterior temporal subcortical cysts, multifocal lobar white-matter lesions with sparing of central white matter, and intracranial calcification**. Diagnosis is molecular, since imaging alone cannot separate it from congenital CMV or AGS. There is **no disease-specific therapy**; management is supportive, though the interferonopathy mechanism nominates **JAK1/2 inhibition** (baricitinib, ruxolitinib) as a biologically rational but as-yet-untrialed candidate. Fewer than a few dozen families have been reported worldwide.

---

## Key Findings

### 1. *RNASET2* biallelic loss-of-function is the sole known cause and produces a CMV-mimic phenotype

The founding study (Henneke et al., 2009) mapped and identified **homozygous and compound heterozygous loss-of-function mutations in *RNASET2*** at chromosome 6q27 as the cause of an autosomal-recessive cystic leukoencephalopathy whose clinical and neuroradiological phenotype is *indistinguishable from congenital CMV brain infection*. The verbatim conclusion: *"loss-of-function mutations in the gene encoding the RNASET2 glycoprotein lead to cystic leukoencephalopathy, an autosomal recessive disorder with an indistinguishable clinical and neuroradiological phenotype"* ([PMID: 19525954](https://pubmed.ncbi.nlm.nih.gov/19525954/)). The disorder carries **OMIM #612951** and **MONDO:0013058**. Multiple subsequent families have confirmed the gene–disease relationship, including Tonduti et al. 2016 ([PMID: 27091087](https://pubmed.ncbi.nlm.nih.gov/27091087/)) and Sun et al. 2018 ([PMID: 29336640](https://pubmed.ncbi.nlm.nih.gov/29336640/)). *(Evidence: human clinical/genetic.)*

### 2. The disease is a lysosomal storage disorder in which rRNA is the stored material

Haud et al. (2011) generated *rnaset2* mutant zebrafish and showed that **RNase T2 localizes within lysosomes and that its loss causes accumulation of undigested rRNA inside neuronal lysosomes**: *"loss of rnaset2 in mutant zebrafish results in accumulation of undigested rRNA within lysosomes within neurons of the brain."* High-field MR microimaging revealed white-matter lesions comparable to those in RNASET2-deficient infants, together with amyloid precursor protein accumulation and astrogliosis at sites of neurodegeneration. The authors concluded that *"familial cystic leukoencephalopathy is a lysosomal storage disorder in which rRNA is the best candidate for the noxious storage material"* ([PMID: 21199949](https://pubmed.ncbi.nlm.nih.gov/21199949/)). This finding establishes both the **subcellular site (lysosome, GO:0005764)** and the **initiating molecular lesion**. *(Evidence: model organism — zebrafish.)*

### 3. RNASET2 deficiency is a type I interferonopathy driven by endolysosomal RNA-sensing TLR activation

Two 2025 companion studies converge on **TLR13 as the driver of RNase T2-deficient autoinflammation in mice**. Gomez-Diaz et al. showed that *Rnaset2*-/- mice develop interferon-dependent neuroinflammation, impaired hematopoiesis, and splenomegaly, and that *"the inflammatory phenotype found in Rnaset2-/- mice is completely reversed in the absence of TLR13, suggesting aberrant accumulation of an RNA ligand for this receptor"* ([PMID: 39853306](https://pubmed.ncbi.nlm.nih.gov/39853306/)). Crucially, the phenotype persists in germ-free mice, indicating an **endogenous rRNA-derived ligand**. Sato et al. showed that *"lysosomal RNA stress, caused by the lack of RNase T2, induces macrophage accumulation in multiple organs such as the spleen and liver through TLR13 activation by microbiota-derived ribosomal RNAs"* ([PMID: 39853307](https://pubmed.ncbi.nlm.nih.gov/39853307/)). Because humans lack functional TLR13, **TLR8** is the inferred orthologous endolysosomal RNA sensor in patients. *(Evidence: model organism — mouse.)*

### 4. Microglial pyroptosis and ISG upregulation precede T-cell infiltration and brain atrophy

Wendland et al. (2025) charted the temporal cascade in *Rnaset2*-/- mice. Interferon-stimulated genes (IRF9, RIG-I) are sustainedly upregulated across 3–28 weeks; chemokines *Ccl2, Ccl5, Cxcl10* peak early; and **pyroptosis markers ASC, CASP1, and GSDMD are significantly increased at 3–6 weeks** (declining thereafter) while apoptotic markers (Bax, CASP3/8, PARP) remain unchanged. ASC co-localizes with the microglial marker IBA-1, and *Cd3e*/*Tnf* peak later (~17 weeks). The authors conclude that *"pyroptosis is an early, disease-associated event restricted to microglia that likely contributes to establishing a proinflammatory milieu prior to T cell infiltration and brain atrophy"* ([PMID: 41453865](https://pubmed.ncbi.nlm.nih.gov/41453865/)). This positions **microglial pyroptosis as an early, upstream driver** of neurodegeneration and nominates inflammasome/pyroptosis inhibition as a therapeutic node. *(Evidence: model organism — mouse.)*

### 5. IFNAR1 dependence proves type I interferon causality

Kettwig et al. (2021) generated CRISPR/Cas9 *Rnaset2*-/- mice and demonstrated that neuroinflammation is **IFNAR1-dependent**: *"Rnaset2-/- mice demonstrate upregulation of interferon-stimulated genes and concurrent IFNAR1-dependent neuroinflammation, with infiltration of CD8+ effector memory T cells and inflammatory monocytes into the grey and white matter."* Single-nuclei RNA sequencing revealed *"homeostatic dysfunctions in glial cells and neurons,"* and the mice showed hippocampal-accentuated brain atrophy with cognitive impairment ([PMID: 34764281](https://pubmed.ncbi.nlm.nih.gov/34764281/)). Genetic removal of the type I interferon receptor abrogating the phenotype provides the **causal proof** that type I IFN signaling — not merely storage — drives the neuropathology. *(Evidence: model organism — mouse.)*

### 6. Characteristic clinical and neuroradiological phenotype

Across reported families, the disorder is an **infantile-onset, largely static encephalopathy** with severe psychomotor impairment/developmental delay (the cardinal feature), spasticity, epilepsy/seizures, occasional neurological regression, and **microcephaly — explicitly NOT megalencephaly**. The signature MRI triad is **bilateral anterior temporal subcortical cysts, multifocal lobar white-matter lesions with sparing of central white matter, and intracranial calcification**: Tonduti et al. describe *"bilateral anterior temporal subcortical cysts and multifocal lobar white matter lesions with sparing of central white matter structures"* ([PMID: 27091087](https://pubmed.ncbi.nlm.nih.gov/27091087/)), and Kameli et al. report *"white matter involvement, calcification and anterior temporal cysts"* ([PMID: 31349848](https://pubmed.ncbi.nlm.nih.gov/31349848/)). CMV PCR is negative and metabolic screening is normal, distinguishing the disorder from its acquired mimic. Suggested HPO terms: intellectual disability (HP:0001249), global developmental delay (HP:0001263), spasticity (HP:0001257), seizure (HP:0001250), microcephaly (HP:0000252), cerebral white matter atrophy/leukoencephalopathy (HP:0002352), intracranial calcification (HP:0002514), sensorineural hearing impairment (HP:0000407), dystonia (HP:0001332). *(Evidence: human clinical.)*

### 7. Gene, protein, and representative pathogenic variants

*RNASET2* encodes a **256-amino-acid acidic ribonuclease** of the conserved T2 family — a glycoprotein located on chromosome 6q27 ([PMID: 31349848](https://pubmed.ncbi.nlm.nih.gov/31349848/): *"RNASET2 as a subtype of RNASEs is a 256 amino acid protein, encoded by RNASET2 gene located on chromosome six"*). Inheritance is autosomal recessive with biallelic loss-of-function variants. Reported pathogenic variants include the nonsense variants **c.233C>A p.(Ser78Ter)** ([PMID: 31349848](https://pubmed.ncbi.nlm.nih.gov/31349848/)) and **c.128G>A p.(Trp43Ter)** ([PMID: 29336640](https://pubmed.ncbi.nlm.nih.gov/29336640/)), plus a **430-kb 6q27 microdeletion encompassing *RNASET2*** and the compound-heterozygous/homozygous LoF alleles of the founding study ([PMID: 19525954](https://pubmed.ncbi.nlm.nih.gov/19525954/)). The protein (UniProt **O00584**; alias RNASE6PL) carries two catalytic active-site histidines (CAS I/CAS II). *(Evidence: human clinical/genetic.)*

### 8. RNASET2 is a conserved alarmin and tumor suppressor beyond its housekeeping role

Beyond lysosomal rRNA turnover, human RNASET2 is a **secreted "alarmin" and oncosuppressor** that recruits and activates monocyte/macrophage-lineage innate immune cells. Rosini et al. describe that *"the human RNASET2 protein (hRNASET2) has been reported as an extracellular tumor suppressor protein, endowed with the ability to act as an 'alarmin' signalling molecule"* ([PMID: 32450138](https://pubmed.ncbi.nlm.nih.gov/32450138/)), and Lualdi et al. document its role in *"inducing a sustained recruitment of immune-competent cells belonging to the monocyte/macrophage lineage within a growing tumor mass"* ([PMID: 25797262](https://pubmed.ncbi.nlm.nih.gov/25797262/)). This dual identity — housekeeping lysosomal RNase and innate-immune signaling molecule — helps explain why its loss produces both storage pathology and inflammation. *(Evidence: in vitro / cell biology.)*

### 9. Phenotypic spectrum is variable; anterior temporal cysts are not obligate

The RNASET2-deficiency spectrum is broader than the classic triad. Sun et al. explicitly note that their patient *"did not show anterior temporal lobe subcortical cysts, hearing loss, dystonia or extra-neurological features"* ([PMID: 29336640](https://pubmed.ncbi.nlm.nih.gov/29336640/)) — implying that **sensorineural hearing loss and dystonia occur in other patients** and that the hallmark anterior temporal cysts are **variably present**. Core features (delayed psychomotor development, intellectual disability, seizures) are consistent, but severity and the full imaging picture vary, indicating **variable expressivity**. *(Evidence: human clinical.)*

### 10. Ultra-rare, consanguinity-enriched, reported across diverse populations

As of 2018, *"Only eight families with RNASET2 mutation have been previously reported"* ([PMID: 29336640](https://pubmed.ncbi.nlm.nih.gov/29336640/)), with additional families reported since (e.g., Tonduti 2016, 5 patients; Kameli 2019). Cases span European, East Asian/Chinese, and Iranian populations. Consanguinity contributes homozygous LoF alleles and structural microdeletions. Orphanet lists prevalence as unknown/<1 per 1,000,000. *(Evidence: human epidemiological.)*

### 11. Deep evolutionary conservation and three engineered animal models

The T2/Rh ribonuclease family is ancient and ubiquitous: *"T2-family acidic endoribonucleases are represented in all genomes"* ([PMID: 21199949](https://pubmed.ncbi.nlm.nih.gov/21199949/)). Verified orthologs include human *RNASET2* (GeneID 8635; Taxon 9606), mouse *Rnaset2a*/*Rnaset2b* (GeneIDs 100037283/68195; Taxon 10090), rat *Rnaset2* (GeneID 292306; Taxon 10116), and zebrafish *rnaset2* (GeneID 791890; Taxon 7955). Three engineered models exist — **zebrafish** (lysosomal rRNA storage + white-matter lesions), **mouse** (IFNAR1-dependent neuroinflammation, cystic/white-matter lesions, atrophy), and **rat** (hippocampal neuroinflammation and memory deficits but no cystic lesions; [PMID: 29752287](https://pubmed.ncbi.nlm.nih.gov/29752287/)). No naturally occurring RNASET2 disease is documented in OMIA. *(Evidence: model organism / comparative.)*

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variants in *RNASET2*** (6q27; nonsense, deletion, or microdeletion) **result in** absent/nonfunctional lysosomal T2-family acid ribonuclease. *(Demonstrated — human genetics, PMID 19525954.)*
2. Loss of RNase T2 catalytic activity **leads to** failure of lysosomal ribosomal RNA degradation, so **undigested rRNA accumulates within neuronal lysosomes** — a lysosomal storage state. *(Demonstrated — zebrafish, PMID 21199949.)*
3. Accumulated lysosomal rRNA **acts as a ligand for endolysosomal RNA-sensing Toll-like receptors** — **TLR13 in mice** (genetically proven), **TLR8 inferred in humans**. *(Demonstrated in mouse; human step inferred — PMID 39853306, 39853307.)*
4. TLR activation **drives type I interferon production and signaling**, which is **IFNAR1-dependent**: removing IFNAR1 abrogates neuroinflammation. *(Demonstrated — mouse, PMID 34764281.)*
5. Type I IFN signaling **results in** sustained interferon-stimulated gene (ISG) upregulation and **early microglial pyroptosis** (ASC/CASP1/GSDMD), establishing a proinflammatory milieu. *(Demonstrated — mouse, PMID 41453865.)*
6. The proinflammatory milieu **leads to** infiltration of **CD8+ effector-memory T cells and inflammatory monocytes** into grey and white matter (branch: also splenomegaly, impaired hematopoiesis, emergency myelopoiesis systemically). *(Demonstrated — mouse, PMID 34764281, 39853307.)*
7. Glial/neuronal homeostatic dysfunction and neuroinflammation **cause** white-matter injury, anterior temporal subcortical cysts, intracranial calcification, and cerebral (hippocampal-accentuated) atrophy. *(Demonstrated across models + human imaging.)*
8. These structural lesions **produce** the clinical phenotype: severe, largely static infantile encephalopathy with psychomotor impairment, spasticity, epilepsy, ± microcephaly/hearing loss/dystonia. *(Demonstrated — human clinical, PMID 19525954, 27091087.)*

```
 RNASET2 biallelic LoF (6q27)
            │  loss of lysosomal acid RNase
            ▼
 Undigested rRNA storage in neuronal lysosomes  ── lysosomal storage disorder
            │  endogenous RNA ligand
            ▼
 Endolysosomal RNA-sensing TLR (TLR13 mouse / TLR8 human inferred)
            │
            ▼
 Type I interferon production ──► IFNAR1-dependent signaling ── type I interferonopathy
            │
            ├──► ISG upregulation (IRF9, RIG-I)
            ├──► EARLY microglial pyroptosis (ASC/CASP1/GSDMD)  [3–6 wk peak]
            │
            ▼
 CD8+ T-cell + inflammatory monocyte infiltration [~17 wk]
            │                                   └─(systemic: splenomegaly, myelopoiesis)
            ▼
 White-matter injury · anterior temporal cysts · calcification · atrophy
            │
            ▼
 Severe static infantile encephalopathy (CMV/AGS mimic)
```

**Upstream vs downstream:** The lysosomal storage defect (steps 1–2) is upstream and cell-intrinsic; the TLR→IFN axis (steps 3–5) is the amplifying inflammatory core; T-cell/monocyte infiltration and tissue injury (steps 6–7) are downstream effectors. The IFNAR1-knockout rescue (step 4) and TLR13-knockout rescue (step 3) identify two genetically validated intervention points.

**Cell types involved (CL terms):** neurons (CL:0000540), oligodendrocytes/myelin (CL:0000128), astrocytes/astrogliosis (CL:0000127), microglia (CL:0000129), infiltrating CD8+ T cells, inflammatory monocytes/macrophages.
**Biological processes (GO terms):** lysosomal RNA catabolism (rRNA degradation), Toll-like receptor signaling pathway (GO:0002224), type I interferon-mediated signaling pathway (GO:0060337), pyroptosis (GO:0070269) / inflammasome activation, neuroinflammatory response (GO:0150076).
**Subcellular compartment (GO CC):** lysosome (GO:0005764) — the site of the primary storage lesion.

### Comparison of the three axes of pathogenesis

| Mechanistic class | Evidence | Key node | Therapeutic implication |
|---|---|---|---|
| Lysosomal storage disorder | Zebrafish rRNA accumulation ([PMID: 21199949](https://pubmed.ncbi.nlm.nih.gov/21199949/)) | Failed rRNA degradation | Substrate reduction / enzyme replacement (theoretical) |
| Type I interferonopathy | IFNAR1-dependence ([PMID: 34764281](https://pubmed.ncbi.nlm.nih.gov/34764281/)); TLR13 rescue ([PMID: 39853306](https://pubmed.ncbi.nlm.nih.gov/39853306/)) | TLR→IFN axis | JAK1/2 inhibition; TLR blockade |
| Innate-immune / pyroptotic | Microglial pyroptosis ([PMID: 41453865](https://pubmed.ncbi.nlm.nih.gov/41453865/)) | Inflammasome (ASC/CASP1/GSDMD) | Inflammasome/pyroptosis inhibitors |

---

## Anatomical, Temporal, and Population Summary

**Anatomy (Section 7 of template):** Primary organ — brain (UBERON:0000955), nervous system. Sites — bilateral cerebral/lobar white matter (UBERON:0002316) with central white-matter sparing, anterior temporal lobe subcortical cysts (temporal lobe UBERON:0001871), basal ganglia/intracranial calcification, and cerebral atrophy including hippocampus (UBERON:0002421). Lateralization — **bilateral/symmetric**. Kettwig et al. confirm *"cystic brain lesions, multifocal white matter alterations, cerebral atrophy"* ([PMID: 34764281](https://pubmed.ncbi.nlm.nih.gov/34764281/)).

**Temporal development (Section 8):** Onset is **congenital/infantile**; course is **largely static** (non- or slowly progressive) rather than relentlessly degenerative, though regression is described in some patients. Mouse data reveal a defined temporal order — ISGs and chemokines early, microglial pyroptosis peaking at 3–6 weeks, T-cell infiltration ~17 weeks — suggesting an **early critical window** for anti-inflammatory intervention before irreversible atrophy.

**Inheritance & population (Section 9):** Autosomal recessive; ultra-rare (<1/1,000,000). Consanguinity-enriched; founder-type homozygous LoF and microdeletions occur. Reported in European, Chinese/East Asian, and Iranian families. No strong sex bias reported. Penetrance appears high for biallelic LoF; expressivity is variable (see Finding 9). No genetic anticipation, mosaicism, or repeat-expansion mechanism is implicated.

**Diagnostics (Section 10):** Diagnosis is **molecular** (single-gene *RNASET2* testing, leukodystrophy gene panels, WES, or WGS; chromosomal microarray detects the 6q27 microdeletion), because MRI cannot distinguish the disorder from congenital CMV or AGS. Supportive workup: **negative CMV PCR**, normal metabolic screening, characteristic MRI triad. Differential diagnosis — congenital CMV infection, Aicardi–Goutières syndrome, and other cystic leukoencephalopathies (e.g., megalencephalic leukoencephalopathy, which by contrast features macrocephaly). A blood interferon signature (ISG score) would be expected to support the interferonopathy classification, though it is not yet validated as a routine test in this disorder.

**Prognosis (Section 11):** Severe neurodevelopmental disability; course largely static with lifelong dependency. Morbidity is high (spasticity, epilepsy, cognitive impairment). Formal survival statistics are not established given rarity.

**Treatment (Section 12):** **No disease-specific therapy.** Care is symptomatic/supportive — antiepileptics (NCIT anticonvulsant agents), spasticity management (e.g., baclofen), physiotherapy/occupational/speech therapy, developmental support. **JAK1/2 inhibitors** (baricitinib, ruxolitinib, tofacitinib) are a mechanistically rational, untrialed candidate given the interferonopathy classification; a scoping review of type I interferonopathies found that *"JAK inhibitors improved clinical and analytical parameters and decreased flare numbers, plasma inflammatory markers, and expression of IFN-stimulated genes"* ([PMID: 33856640](https://pubmed.ncbi.nlm.nih.gov/33856640/)). Preclinical work additionally nominates inflammasome/pyroptosis inhibition ([PMID: 41453865](https://pubmed.ncbi.nlm.nih.gov/41453865/)).

**Prevention (Section 13):** No primary prevention exists. Relevant measures are **genetic counseling**, carrier testing in consanguineous families, cascade testing, and prenatal/preimplantation genetic testing where a familial variant is known.

**Other species / models (Sections 14–15):** No naturally occurring animal disease documented in OMIA. Three engineered models — **zebrafish** (faithful lysosomal storage + white-matter lesions), **mouse** (best recapitulation: interferonopathy, cystic/white-matter pathology, atrophy, cognitive deficits), and **rat** (hippocampal neuroinflammation and memory deficits, but lacks cystic lesions). A 2024 review documents zebrafish as a leukodystrophy model ([PMID: 38239149](https://pubmed.ncbi.nlm.nih.gov/38239149/)).

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [19525954](https://pubmed.ncbi.nlm.nih.gov/19525954/) | *RNASET2-deficient cystic leukoencephalopathy resembles congenital CMV* | Human genetics/clinical | Gene–disease causality; CMV mimic (F001, F005, F006) |
| [21199949](https://pubmed.ncbi.nlm.nih.gov/21199949/) | *rnaset2 mutant zebrafish model familial cystic leukoencephalopathy…* | Model organism (zebrafish) | Lysosomal rRNA storage mechanism; conservation (F002, F011, F013) |
| [27091087](https://pubmed.ncbi.nlm.nih.gov/27091087/) | *Clinical, radiological and pathological overlap … and AGS* | Human clinical | MRI triad; AGS overlap (F005, F008) |
| [29336640](https://pubmed.ncbi.nlm.nih.gov/29336640/) | *Novel RNASET2 pathogenic variants in an East Asian child* | Human genetics/clinical | Variants; rarity; phenotypic variability (F006, F009, F010) |
| [31349848](https://pubmed.ncbi.nlm.nih.gov/31349848/) | Kameli et al., RNASET2 case | Human clinical/genetic | Protein size/location; variant; imaging (F005, F006) |
| [34764281](https://pubmed.ncbi.nlm.nih.gov/34764281/) | Kettwig et al., *Rnaset2-/- mice* | Model organism (mouse) | IFNAR1-dependence; cellular infiltrate (F011, F012, F014) |
| [39853306](https://pubmed.ncbi.nlm.nih.gov/39853306/) | Gomez-Diaz et al., TLR13 | Model organism (mouse) | TLR13 as driver; interferonopathy (F003, F014) |
| [39853307](https://pubmed.ncbi.nlm.nih.gov/39853307/) | Sato et al., lysosomal RNA stress | Model organism (mouse) | TLR13/rRNA link; myelopoiesis (F003) |
| [41453865](https://pubmed.ncbi.nlm.nih.gov/41453865/) | Wendland et al., microglial pyroptosis | Model organism (mouse) | Early pyroptosis cascade (F004) |
| [29752287](https://pubmed.ncbi.nlm.nih.gov/29752287/) | Sinkevicius et al., RNaseT2 KO rat | Model organism (rat) | Rat model characteristics (F011) |
| [25797262](https://pubmed.ncbi.nlm.nih.gov/25797262/) | Lualdi et al., RNASET2 alarmin | In vitro | Alarmin/immune recruitment (F007) |
| [32450138](https://pubmed.ncbi.nlm.nih.gov/32450138/) | Rosini et al., hRNASET2 tumor suppressor | In vitro | Alarmin/tumor-suppressor identity (F007) |
| [33856640](https://pubmed.ncbi.nlm.nih.gov/33856640/) | Gómez-Arias et al., JAK inhibitors in interferonopathies | Human clinical (scoping review) | Rational therapy (F008) |
| [38239149](https://pubmed.ncbi.nlm.nih.gov/38239149/) | Review — zebrafish leukodystrophy models | Review | Model relevance (F014) |

**How the evidence coheres:** Human genetics (PMID 19525954) established causality; zebrafish (PMID 21199949) defined the storage mechanism; and a series of rodent models (PMID 34764281, 39853306/07, 41453865) built the inflammatory arc, culminating in two genetically validated intervention points (TLR13, IFNAR1). No study contradicts the consolidated model; the primary uncertainty is translational (the human TLR8-vs-mouse-TLR13 inference).

---

## Limitations and Knowledge Gaps

- **Human TLR identity unproven.** The TLR13 dependence is established only in mice; humans lack functional TLR13, so the orthologous sensor (**TLR8** is the leading candidate) has not been experimentally confirmed in patient cells. This is the single most important translational gap.
- **No human trial data for any disease-modifying therapy.** JAK inhibition and inflammasome/pyroptosis inhibition are mechanistically rational but entirely untrialed in this disease; efficacy, blood–brain-barrier penetration, and timing (early critical window) are unknown.
- **Small evidence base for epidemiology and natural history.** With only a few dozen reported families, prevalence, penetrance, expressivity, sex ratio, and survival statistics are imprecise. No formal registry or natural-history cohort exists.
- **Genotype–phenotype correlations are undefined.** It is unclear why some patients lack anterior temporal cysts or develop hearing loss/dystonia while others do not; modifier genes and environmental modifiers are unexplored.
- **Static-vs-progressive course.** The relative contributions of a fixed developmental lesion versus ongoing inflammation to the "static" clinical picture are not fully resolved, which matters for whether late anti-inflammatory therapy could help.
- **Human neuropathology is limited.** Most cellular/mechanistic detail derives from animal models; direct confirmation of microglial pyroptosis and the ISG signature in human brain tissue is sparse.
- **No epigenetic, proteomic, or metabolomic patient datasets** were identified for this disease; molecular profiling remains model-based.

---

## Proposed Follow-up Experiments / Actions

1. **Confirm the human sensor.** Test whether patient-derived macrophages/microglia (iPSC-derived) or *RNASET2*-knockout human cells show TLR8-dependent type I IFN induction; use TLR8 antagonists and CRISPR knockout to establish the human ortholog of the mouse TLR13 axis.
2. **Preclinical JAK-inhibitor trial in *Rnaset2*-/- mice.** Test whether baricitinib/ruxolitinib started within the early critical window (before the 3–6-week pyroptosis peak) prevents ISG upregulation, T-cell infiltration, and hippocampal atrophy, with dose–timing arms to define the intervention window.
3. **Inflammasome/pyroptosis blockade.** Evaluate GSDMD or CASP1/NLRP3 inhibitors (or genetic *Gsdmd* deletion) in *Rnaset2*-/- mice to test whether interrupting microglial pyroptosis is sufficient to blunt downstream neuroinflammation.
4. **Interferon signature as a biomarker.** Measure a blood ISG score (IFI27, IFI44L, IFIT1, ISG15, etc.) in RNASET2-deficient patients to confirm the human interferonopathy signature and provide a pharmacodynamic readout for future trials.
5. **Establish an international registry / natural-history study** to capture prevalence, genotype–phenotype correlations (including the variable temporal cysts, hearing loss, dystonia), progression, and survival.
6. **Substrate-reduction and enzyme-replacement feasibility.** Explore whether reducing lysosomal rRNA load (e.g., modulating ribophagy) or delivering functional RNase T2 to the CNS is achievable, addressing the upstream storage lesion rather than only the inflammatory consequence.
7. **Human tissue validation.** Where autopsy/biopsy material is available, confirm microglial pyroptosis, ISG expression, and CD8+ T-cell infiltration in patient brain to close the model-to-human gap.

---

*Report compiled from 14 confirmed findings across 5 iterations, drawing on 14 primary and review references. Evidence types are annotated per finding (human clinical/genetic, model organism, in vitro, review). Ontology suggestions: MONDO:0013058, HGNC:14015 (RNASET2), UniProt O00584, GO:0005764 (lysosome), GO:0060337 (type I IFN signaling), GO:0070269 (pyroptosis), UBERON:0000955/0002316/0001871/0002421, CL:0000129 (microglia)/0000540 (neuron)/0000128 (oligodendrocyte)/0000127 (astrocyte).*


## Artifacts

- [OpenScientist final report](Cystic_Leukoencephalopathy_Without_Megalencephaly-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cystic_Leukoencephalopathy_Without_Megalencephaly-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000129` (2 mentions) - the report calls it "microglia"; CL calls it **microglial cell**, and lists "microglia" among its other names
- `GO:0060337` (2 mentions) - the report calls it "type I IFN signaling"; GO calls it **type I interferon-mediated signaling pathway**, and lists "type I interferon signaling pathway" among its other names
- `GO:0070269` (2 mentions) - the report calls it "pyroptosis"; GO calls it **pyroptotic inflammatory response**, and lists "pyroptosis" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

23 of 25 terms resolved to a current term; the rest could not be looked up either way.
