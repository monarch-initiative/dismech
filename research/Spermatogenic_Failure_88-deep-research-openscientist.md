---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T20:34:01.648953'
end_time: '2026-10-22T21:11:42.813796'
duration_seconds: 2261.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Spermatogenic Failure 88
  mondo_id: MONDO:0957821
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
citation_count: 8
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 25
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 4
  labels_variant: 3
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spermatogenic_Failure_88-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spermatogenic_Failure_88-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 88
- **MONDO ID:** MONDO:0957821 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 88** covering all of the
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

# Spermatogenic Failure 88 (SPGF88): A Comprehensive Disease Characterization Report

**Causal gene: KASH5 (also known as CCDC155; aliases POF22, HYDM6), chromosome 19q13.33, NCBI Gene 147872, Ensembl ENSG00000161609, UniProt Q8N6L0.**

> **Identifier verification.** The research template supplied MONDO:0957821. This term maps to **OMIM 620547**, MedGen **C5882706**, and the NCBI gene link for this concept points unambiguously to **KASH5 / CCDC155 (Gene ID 147872)** at 19q13.33. This report therefore describes the KASH5-related disease, not any similarly numbered SPGF entry caused by a different gene.

## Summary

**Spermatogenic failure 88 (SPGF88; MONDO:0957821; OMIM 620547)** is an ultra-rare, autosomal recessive form of male infertility caused by biallelic loss-of-function variants in **KASH5**, also known as **CCDC155** (NCBI Gene 147872; aliases KASH5, POF22, HYDM6), located on chromosome **19q13.33**. KASH5 encodes the meiosis-specific outer-nuclear-membrane dynein adaptor of the **SUN1–KASH5 LINC complex** (Linker of Nucleoskeleton and Cytoskeleton). This complex physically couples meiotic telomeres, through the nuclear envelope, to cytoplasmic dynein and the microtubule cytoskeleton, generating the telomere-led chromosome movements that drive homologous-chromosome pairing and synapsis during meiotic prophase I.

When KASH5 function is lost, telomere-led chromosome movements and "bouquet" formation fail, homologous chromosomes do not pair or synapse, and meiotic DNA double-strand breaks (DSBs) are left unresolved. The consequence is an arrest of spermatogenesis at the **zygotene-like (pre-pachytene) stage**, which manifests clinically as **non-obstructive azoospermia (NOA)** — the complete absence of spermatozoa in the ejaculate due to a spermatogenic (rather than obstructive) defect. The identical molecular lesion causes **premature ovarian insufficiency (POI/POF22)** in females, making this a shared male–female meiotic-arrest disorder. *Kash5*-knockout mice faithfully recapitulate the human zygotene arrest and are infertile in both sexes, providing strong cross-species mechanistic confirmation.

Three independent human reports (Fakhro et al. 2018; Wu et al. 2022; Yang et al. 2022) establish KASH5/CCDC155 as a *bona fide* human NOA gene, with pathogenic alleles spanning frameshift, whole/partial-gene-deletion CNV, splice-site, and coiled-coil missense classes — all converging on loss of LINC-complex function. There is no curative therapy; management centers on genetic counseling and assisted reproduction (with donor sperm the likely route given expected poor surgical sperm-retrieval yield). This report compiles disease information, etiology, phenotypes, genetics, mechanism, affected anatomy, temporal course, epidemiology, diagnostics, prognosis, treatment, prevention, and comparative/model-organism biology across all 15 requested sections.

---

## Key Findings

### Finding 1 — SPGF88 is caused by biallelic KASH5/CCDC155 loss-of-function variants at 19q13.33

OMIM 620547 and MedGen C5882706 map SPGF88 to the gene **KASH5** (NCBI Gene 147872; aliases CCDC155, POF22, HYDM6) at **19q13.33**. In the index genotype, Yang et al. 2022 identified a **heterozygous copy-number deletion `del(19)(q13.33)` (chr19:g.49894043-49903011del)** in *trans* with a **heterozygous frameshift LoF variant `NM_144688:c.979_980del, p.(Arg327Serfs*21)`** in a man with non-obstructive azoospermia and in his infertile sister. This compound-heterozygous (biallelic) configuration abolishes functional KASH5 and produced spermatogenic arrest at a zygotene-like stage.

> *"a novel heterozygous copy number variation (CNV) (seq [GRCh37] del(19) (19q13.33) chr19: g.49894043-49903011del) and a heterozygous loss of function variant (NM_144688: c.979_980del: p.R327Sfs*21) in human KASH5 were identified in a non-obstructive azoospermia (NOA)-affected patient and in his infertile sister"* — [PMID: 35674372](https://pubmed.ncbi.nlm.nih.gov/35674372/)

This is the anchoring genetic finding: it establishes the gene, the locus, the biallelic recessive mechanism, and the loss-of-function variant classes (frameshift + CNV deletion).

### Finding 2 — KASH5 loss arrests meiosis at the zygotene stage via failed homolog pairing/synapsis (conserved human–mouse mechanism)

In the human KASH5-deficient proband, spermatogenesis arrested at a zygotene-like stage with deficient homolog pairing and synapsis. This directly mirrors the original *Kash5*-null mouse (Horn et al. 2013), in which males show meiotic arrest with failed pairing of homologous chromosomes and resulting infertility in both sexes. The concordance across species confirms the human phenotype is a direct consequence of lost LINC-complex–mediated telomere–cytoskeleton coupling.

> *"Males display meiotic arrest in which pairing of homologous chromosomes fails. These findings demonstrate that telomere attachment to the NE is insufficient to promote pairing and that telomere attachment sites must be coupled to cytoplasmic dynein and the microtubule system to ensure meiotic progression."* — [PMID: 24062341](https://pubmed.ncbi.nlm.nih.gov/24062341/)

> *"Spermatogenesis in the proband was arrested at zygotene-like stage with a deficiency in homolog pairing and synapsis"* — [PMID: 35674372](https://pubmed.ncbi.nlm.nih.gov/35674372/)

### Finding 3 — KASH5 is loss-of-function–tolerant in gnomAD, consistent with a recessive mechanism

gnomAD v4 constraint metrics for KASH5 (ENSG00000161609) show the gene is **not depleted of heterozygous LoF variants**: pLI ≈ 0 (2.96×10⁻²¹), observed/expected LoF = 0.85 (90% CI 0.71–1.04; LOEUF ≈ 1.04), with 72 observed vs 84 expected LoF variants. This tolerance of heterozygous LoF is exactly what is expected for an autosomal recessive disease gene — heterozygous carriers are unaffected and disease requires biallelic hits. It also argues against a dominant-negative or haploinsufficiency model.

### Finding 4 — A homozygous coiled-coil missense (p.Leu197Pro) causes NOA and POI by mislocalizing the LINC complex

Wu et al. 2022 performed whole-exome sequencing on 15 consanguineous NOA/POI patients and identified a **homozygous missense variant in the conserved coiled-coil (CC) domain of CCDC155/KASH5, `c.590T>C, p.(Leu197Pro)`**, in a brother–sister pair whose parents were first cousins. Functionally, the variant **blocked nuclear-envelope (NE) distribution of KASH5 and prevented NE-specific enrichment of SUN1**, and affected spermatocytes **failed to complete meiotic division with unresolved DNA double-strand-break repair**. This adds a missense variant class and an explicit DSB-repair-failure step to the mechanism. Per UniProt Q8N6L0, KASH5 is a 562-aa protein with a coiled-coil domain (residues 164–349) and a C-terminal transmembrane KASH anchor (522–542); it localizes to telomeres from leptotene to diplotene.

> *"identified a novel homozygous missense mutation in CCDC155 [c.590T>C (p.Leu197Pro)] in a pair of familial NOA and POI patients whose parents were first cousins"* — [PMID: 35587281](https://pubmed.ncbi.nlm.nih.gov/35587281/)

> *"blocked nuclear envelope (NE) distribution and subsequently prevented NE-specific enrichment of Sad1- and UNC84-domain-containing 1 either ex vivo or in vitro"* — [PMID: 35587281](https://pubmed.ncbi.nlm.nih.gov/35587281/)

### Finding 5 — First human KASH5–NOA link (Fakhro et al. 2018) and the authoritative HPO annotation set

Fakhro et al. 2018 (*Genetics in Medicine*) performed WES across 8 consanguineous Middle Eastern (Qatari) NOA families and identified rare deleterious recessive variants in **CCDC155 (KASH5)** — along with NANOS2, SPO11, TEX14, and WNK3 — segregating with disease, the **earliest human evidence** for KASH5-related NOA and a foundational source for OMIM 620547. The official Human Phenotype Ontology annotations for OMIM:620547 (ontology.jax.org) are: **HP:0003251 Male infertility** (3/3 patients), **HP:0011961 Non-obstructive azoospermia** (3/3), **HP:0031039 Spermatocyte maturation arrest** (2/2), **HP:0011462 Young adult onset** (2/2), and **HP:0000007 Autosomal recessive inheritance**.

> *"we identified rare deleterious recessive variants in CCDC155, NANOS2, SPO11, TEX14, and WNK3 segregating with disease. These genes, which are novel to human NOA, have remarkable testis-specific expression"* — [PMID: 29790874](https://pubmed.ncbi.nlm.nih.gov/29790874/)

> *"Nonobstructive azoospermia (NOA) affects 1% of the male population"* — [PMID: 29790874](https://pubmed.ncbi.nlm.nih.gov/29790874/)

---

## Section-by-Section Report

### 1. Disease Information

SPGF88 is a monogenic (Mendelian), autosomal recessive form of **non-obstructive azoospermia** — a spermatogenic failure in which no spermatozoa reach the ejaculate because germ-cell development is arrested within the testis, with patent excurrent ducts. It is one of a numbered series of "spermatogenic failure" OMIM entries, each defined by its causal gene; SPGF88's gene is **KASH5/CCDC155**.

**Key identifiers:**
- **OMIM:** 620547
- **MONDO:** MONDO:0957821
- **MedGen:** C5882706
- **Gene:** KASH5 / CCDC155 (NCBI Gene 147872; Ensembl ENSG00000161609; UniProt Q8N6L0)
- **Locus:** 19q13.33
- **ICD-10:** N46.x (male infertility; no SPGF88-specific code); **ICD-11:** GB04 (male infertility). No disease-specific ICD code exists.
- **Orphanet / MeSH:** No SPGF88-specific entry; subsumed under azoospermia / male infertility (MeSH D053713 Azoospermia).

**Synonyms / alternative names:** Spermatogenic failure 88; SPGF88; non-obstructive azoospermia due to KASH5/CCDC155 deficiency. The female-manifesting counterpart at the same locus is designated **POF22 (premature ovarian failure 22)**.

**Source of information:** Aggregated, disease-level resources (OMIM, MedGen, HPO) built from a small number of individual-patient case reports in consanguineous/familial cohorts — not from large EHR datasets. The total reported human caseload is a handful of patients across three publications.

### 2. Etiology

**Primary cause — genetic.** SPGF88 is caused exclusively by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in KASH5/CCDC155**. No environmental, infectious, or acquired cause is implicated; this is a pure Mendelian meiotic defect.

**Genetic risk factors.** The causal variants reported span several classes, all converging on loss of KASH5 function:
- Frameshift LoF: `c.979_980del, p.(Arg327Serfs*21)` (Yang 2022)
- Whole/partial-gene deletion CNV: `del(19)(q13.33) chr19:g.49894043-49903011del` (Yang 2022)
- Coiled-coil missense: `c.590T>C, p.(Leu197Pro)` (Wu 2022)
- Splice-site (in the POI-manifesting form): `c.747G>A` (Zhang et al. 2022, POI pedigree)
- Rare deleterious recessive variant(s) in CCDC155 (Fakhro 2018)

**Consanguinity** is the dominant risk modifier: homozygous cases arose in first-cousin unions (Wu 2022; Fakhro 2018), reflecting the general pattern for ultra-rare recessive disease.

**Environmental / lifestyle / infectious risk factors:** None known or expected for this monogenic disorder. General NOA risk factors (heat, toxins, chemotherapy, Y-microdeletions, Klinefelter syndrome) are *differential diagnoses*, not contributors to SPGF88 itself.

**Protective factors:** None identified. By inference, a single functional KASH5 allele is fully protective (carriers are fertile and unaffected), consistent with the gnomAD LoF tolerance (Finding 3).

**Gene–environment interactions:** None documented; the phenotype is fully penetrant genetically without a known environmental trigger.

### 3. Phenotypes

The phenotype is reproductive and, in males, essentially monosymptomatic at the organismal level.

| Phenotype | HPO term | Type | Frequency (reported) | Onset | Severity/Course |
|---|---|---|---|---|---|
| Male infertility | HP:0003251 | Clinical sign | 3/3 | Young adult | Severe, stable, lifelong |
| Non-obstructive azoospermia | HP:0011961 | Laboratory abnormality | 3/3 | Young adult | Severe, stable |
| Spermatocyte maturation arrest | HP:0031039 | Histopathology | 2/2 | — | Severe (zygotene arrest) |
| Young adult onset | HP:0011462 | Onset modifier | 2/2 | ~20s–30s | — |
| (Female counterpart) Premature ovarian insufficiency | HP:0008209 | Clinical sign | POI pedigrees | Young adult | Progressive loss of ovarian reserve |

**Characteristics.** Onset is effectively congenital at the cellular level (the meiotic machinery is defective from the first wave of spermatogenesis) but is **clinically recognized in young adulthood** when infertility prompts evaluation. Severity is **severe** (complete azoospermia; no spontaneous conception possible), the course is **stable/non-progressive** in males (no systemic decline), and penetrance for infertility appears complete in biallelic individuals.

**Quality-of-life impact.** The burden is confined to reproduction: inability to father children biologically, with the attendant psychological and relationship impact well documented for NOA generally. There is no systemic morbidity, pain, or reduction in life expectancy. No disease-specific QoL instrument data (EQ-5D/SF-36) exist for SPGF88; impact is inferred from the broader NOA/infertility literature.

### 4. Genetic/Molecular Information

**Causal gene:** KASH5 / **CCDC155** (NCBI Gene 147872; Ensembl ENSG00000161609; UniProt Q8N6L0), 19q13.33. Transcript reference NM_144688. The protein is 562 aa with a central coiled-coil domain (aa 164–349) and a C-terminal KASH transmembrane anchor (aa 522–542).

**Pathogenic variants (all germline):**

| Variant (cDNA / protein) | Type | Zygosity | Classification | Reference |
|---|---|---|---|---|
| c.979_980del / p.(Arg327Serfs*21) | Frameshift (LoF) | Compound het (with CNV) | Pathogenic | Yang 2022 [PMID 35674372] |
| del(19)(q13.33) chr19:g.49894043-49903011del | CNV deletion (LoF) | Compound het | Pathogenic | Yang 2022 [PMID 35674372] |
| c.590T>C / p.(Leu197Pro) | Missense (coiled-coil) | Homozygous | Likely pathogenic / Pathogenic | Wu 2022 [PMID 35587281] |
| c.747G>A | Splice-site | Homozygous | Pathogenic (POI form) | Zhang 2022 [PMID 35708642] |
| CCDC155 rare recessive variant(s) | Deleterious recessive | Recessive | — | Fakhro 2018 [PMID 29790874] |

**Allele frequency:** All reported variants are rare/private; KASH5 is not depleted of LoF in gnomAD (Finding 3), consistent with rare recessive carriers in the general population.

**Functional consequence:** **Loss of function** across all variant classes — truncation/deletion removes the protein; the p.Leu197Pro missense abolishes NE localization and SUN1 recruitment. No gain-of-function or dominant-negative mechanism is supported (the gene's LoF tolerance argues against dominant effects).

**Modifier genes:** None established. Functional partners whose loss produces overlapping meiotic-arrest phenotypes include **SUN1**, **SPDYA (Speedy A)/CDK2**, and the telomere-attachment machinery (TERB1/TERB2/MAJIN), but these are separate SPGF/POI loci, not SPGF88 modifiers.

**Epigenetic information:** None specific to SPGF88 reported.

**Chromosomal abnormalities:** The CNV deletion at 19q13.33 removing KASH5 (Yang 2022) is the relevant large-scale lesion; otherwise the karyotype is normal (SPGF88 is distinct from Klinefelter/Y-microdeletion azoospermia).

### 5. Environmental Information

**Not applicable.** SPGF88 is a monogenic meiotic disorder with no established environmental, lifestyle (smoking/diet/alcohol/exercise), or infectious contribution. Such factors belong to the differential diagnosis of acquired/idiopathic NOA, not to this entity.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic LoF variant in KASH5/CCDC155** (frameshift, CNV deletion, splice, or coiled-coil missense) **leads to** absence or mislocalization of functional KASH5 protein.
2. Loss of KASH5 at the outer nuclear membrane **results in** failure to assemble the meiosis-specific **SUN1–KASH5 LINC complex** at telomere attachment sites (*demonstrated*: p.Leu197Pro blocks NE distribution and SUN1 enrichment).
3. Absent LINC complex **leads to** failure to recruit **cytoplasmic dynein** and couple telomeres to the microtubule cytoskeleton (KASH5 is the dynein adaptor).
4. Loss of dynein/microtubule coupling **results in** loss of **telomere-led rapid chromosome movements** and failure of **meiotic "bouquet" formation** (*inferred in human from mouse; demonstrated in mouse*).
5. Absent chromosome movements **lead to** failed **homologous-chromosome pairing and synapsis** (*demonstrated* in human proband and in *Kash5*-null mice).
6. Failed synapsis **results in** **unresolved meiotic DNA double-strand-break (DSB) repair** (*demonstrated* for p.Leu197Pro spermatocytes).
7. Unresolved DSBs and asynapsis **trigger** the meiotic checkpoint and **arrest at the zygotene-like (pre-pachytene) stage** (*demonstrated*).
8. Meiotic arrest **leads to** **germ-cell elimination / spermatocyte maturation arrest**, so no haploid spermatids or spermatozoa form.
9. Absence of spermatozoa **manifests as** **non-obstructive azoospermia and male infertility** (clinical endpoint).
   - **Branch (female):** The identical LINC-complex failure in oocytes **leads to** accelerated oocyte depletion and **premature ovarian insufficiency (POF22)**.

**Upstream vs downstream:** Steps 1–3 (variant → LINC assembly failure → dynein uncoupling) are upstream molecular causes; steps 5–7 (asynapsis, DSB persistence, checkpoint arrest) are the midstream meiotic failures; steps 8–9 (germ-cell loss, azoospermia) are the downstream clinical outcomes.

**Molecular pathways / processes:** Meiotic telomere clustering and bouquet formation; LINC-complex nucleocytoskeletal coupling; dynein/microtubule-based chromosome motility; meiotic homologous recombination / DSB repair; synaptonemal-complex assembly. KASH5 also participates in the SUN1–SPDYA–CDK2 telomere architecture ([PMID: 34039995](https://pubmed.ncbi.nlm.nih.gov/34039995/)).

**Protein dysfunction:** Loss of the KASH anchor (truncation/deletion) or loss of coiled-coil–mediated NE targeting (p.Leu197Pro) prevents KASH5 from bridging the perinuclear space and binding SUN1 — a loss-of-function structural defect. No experimental structure of human KASH5 has been deposited in the PDB (verified); the AlphaFold model of Q8N6L0 is the available structural proxy.

**Suggested GO / CL terms:**
- **GO:0007129** homologous chromosome pairing at meiosis
- **GO:0007130** synaptonemal complex assembly
- **GO:0070197** meiotic attachment of telomere to nuclear envelope
- **GO:0034993** meiotic nuclear membrane microtubule tethering complex
- **GO:0051321** meiotic cell cycle
- **GO:0000724** DSB repair via homologous recombination
- **Cellular component:** GO:0005640 nuclear outer membrane; GO:0034993 LINC complex
- **CL:0000017 / CL:0000656** spermatocyte; **CL:0000020** spermatogonium; **CL:0000023** oocyte

### 7. Anatomical Structures Affected

- **Organ level (primary):** Testis (**UBERON:0000473**); specifically the seminiferous tubules (**UBERON:0001343**). Female counterpart: ovary (**UBERON:0000992**).
- **Body system:** Male reproductive system (**UBERON:0000079**); the endocrine axis is typically intact (a hypergonadotropic pattern is possible secondary to germ-cell loss).
- **Tissue/cell level:** Germinal epithelium; the targeted population is the **primary spermatocyte (CL:0000656 / CL:0000017)** arrested at zygotene. Somatic Sertoli and Leydig cells are not the primary defect. In females, oocytes (**CL:0000023**).
- **Subcellular level:** **Nuclear envelope / outer nuclear membrane (GO:0005640)**; telomere attachment sites; the LINC complex spanning the perinuclear space; nucleus–cytoskeleton interface.
- **Localization / lateralization:** Bilateral (both testes affected), symmetric. Testicular volume may be preserved or reduced; ducts are patent (non-obstructive).

### 8. Temporal Development

- **Onset:** Cellular defect is **congenital** (present from the first meiotic wave at puberty); **clinical onset is young-adult** (HP:0011462), when infertility is discovered. Onset pattern is insidious/chronic — there is no acute event.
- **Progression:** **Stable and non-progressive** in males — azoospermia is a fixed developmental block, not a degenerative process; lifelong/chronic. In females, the ovarian phenotype (POF22) is **progressive** (accelerated depletion of the oocyte pool).
- **Patterns:** No remission; no relapsing course. The critical period is meiotic prophase I — the window in which the LINC complex is required — which is irreversibly missed.

### 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive (HP:0000007)**; biallelic variants required. Heterozygous carriers are unaffected (consistent with gnomAD LoF tolerance, Finding 3).
- **Penetrance:** Appears **complete** for infertility in biallelic males within reported families (small n).
- **Expressivity:** Consistent severe phenotype (azoospermia) in males; sex-specific expressivity (NOA in males, POI in females) at the same locus.
- **Consanguinity:** Major contributor — homozygous cases arose in first-cousin families (Wu 2022; Fakhro 2018, Qatari cohort).
- **Founder effects / carrier frequency:** None established; variants are private/rare. KASH5 is not LoF-depleted in gnomAD, so rare carriers exist broadly.
- **Epidemiology:** No SPGF88-specific prevalence/incidence exists — it is an **ultra-rare monogenic cause** within the broad NOA category. Context: *"Nonobstructive azoospermia (NOA) affects 1% of the male population"* ([PMID: 29790874](https://pubmed.ncbi.nlm.nih.gov/29790874/)). In the Fakhro consanguineous-cohort analysis, a genetic etiology was found in 13.3% of idiopathic NOA families vs 0 controls (p=0.001), of which CCDC155 was one contributing gene.
- **Demographics:** Reported in Middle Eastern (Qatari) and East Asian (Chinese) consanguineous/familial settings; this reflects ascertainment in consanguineous populations rather than true geographic restriction. Sex ratio is not meaningful (the male disorder affects males; the allelic female disorder is POF22).

### 10. Diagnostics

- **Semen analysis:** Confirms **azoospermia** (no sperm on centrifuged pellet) across ≥2 samples — the defining laboratory test.
- **Hormonal profile:** FSH/LH/testosterone to classify as non-obstructive (often elevated FSH with germ-cell loss); distinguishes from obstructive azoospermia.
- **Physical/imaging:** Scrotal ultrasound to exclude obstruction; testicular volume assessment.
- **Testicular histopathology/biopsy:** **Spermatocyte maturation (meiotic) arrest** at zygotene/pre-pachytene (HP:0031039) — the pathognomonic histology.
- **Genetic testing — the definitive diagnostic:** First exclude Y-chromosome microdeletions and karyotype (Klinefelter). Then **whole-exome sequencing (WES)** or a male-infertility/NOA gene panel including CCDC155/KASH5 identifies biallelic variants. **Chromosomal microarray / CNV analysis** is needed to detect the 19q13.33 deletion allele (as in Yang 2022, where one allele was a CNV). Single-gene testing of KASH5 is appropriate where a familial variant is known.
- **Omics:** KASH5/CCDC155 shows **testis-specific expression** ([PMID: 29790874](https://pubmed.ncbi.nlm.nih.gov/29790874/)), supporting candidacy; research scRNA-seq frameworks are emerging for NOA gene prioritization but are not clinical.
- **Differential diagnosis:** Obstructive azoospermia (normal FSH, patent-duct defect), Klinefelter (47,XXY), Y-microdeletions (AZFa/b/c), and other monogenic meiotic-arrest genes (SYCP3, TEX11, MEIOB, SPO11, STAG3, SUN1, etc.). SPGF88 is distinguished by biallelic KASH5 variants + zygotene arrest.
- **Screening:** Carrier screening/cascade testing of relatives is relevant in consanguineous families once the familial variant is known.

### 11. Outcome / Prognosis

- **Survival/mortality:** No effect on life expectancy or mortality — SPGF88 is confined to fertility. **Not applicable** for survival metrics.
- **Morbidity:** The sole morbidity is **infertility** and its psychosocial impact.
- **Disease course/complications:** Stable; no organ failure or systemic complications. The female allelic disorder (POF22) adds the morbidity of early estrogen deficiency and its sequelae.
- **Recovery potential:** The meiotic block is developmentally fixed and not reversible by medical therapy. **Surgical sperm retrieval (micro-TESE)** yield is expected to be **poor** because the arrest is complete and early (pre-pachytene); no mature or post-meiotic cells are produced.
- **Prognostic factors:** The nature of the variant (complete LoF vs hypomorphic) may in principle influence residual spermatogenesis, but all reported cases showed azoospermia; no favorable prognostic biomarker is established.

### 12. Treatment

- **Curative therapy:** None exists. No pharmacotherapy restores LINC-complex function or reverses meiotic arrest.
- **Assisted reproduction:** Because sperm retrieval is expected to fail, the realistic path to biological parenthood for the couple is **donor-sperm insemination/IVF** or adoption. Micro-TESE with ICSI may be attempted but counseled as low-yield given early complete arrest. (*NCIT:C15215 Assisted Reproductive Technology; NCIT:C92948 Genetic Counseling.*)
- **Gene/cell/RNA therapy, targeted/immunotherapy:** **Not applicable / none in trials** for this indication.
- **Supportive care:** Reproductive counseling and psychological support.
- **Personalized medicine:** Genetic diagnosis chiefly informs prognosis (predicting poor TESE yield) and family planning rather than drug selection.

### 13. Prevention

- **Primary prevention:** Not applicable (genetic disorder; no modifiable exposure).
- **Genetic counseling (central):** For consanguineous couples or families with a known KASH5 variant — counseling on the 25% recurrence risk per pregnancy in carrier×carrier unions, and on the male/female (NOA/POI) implications of the shared locus.
- **Reproductive options:** Carrier screening, cascade testing of relatives, **preimplantation genetic testing (PGT-M)** or prenatal testing when the familial variant is known, and donor gametes.
- **Public-health / behavioral / immunization measures:** Not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Mouse *Kash5* (also *Ccdc155*) is the principal ortholog (conserved LINC-complex function). The gene and mechanism are **evolutionarily conserved** across mammals; related telomere-attachment LINC machinery is documented even on vole B chromosomes ([PMID: 42479255](https://pubmed.ncbi.nlm.nih.gov/42479255/)).
- **Natural disease in animals:** No spontaneous companion-animal/wildlife KASH5 disease is catalogued in OMIA; relevance is experimental rather than veterinary.
- **Comparative biology:** The *Kash5*-null mouse reproduces the human phenotype closely (zygotene meiotic arrest, failed pairing, bilateral infertility), indicating deep conservation of the meiotic-telomere-coupling mechanism.
- **Transmission:** Not applicable (non-communicable genetic disorder).

### 15. Model Organisms

- **Mouse (*Mus musculus*):** The **Kash5-knockout** and **Kash5 C-terminal-deleted** mice are the key models.
  - Horn et al. 2013 ([PMID: 24062341](https://pubmed.ncbi.nlm.nih.gov/24062341/)): KO males show meiotic arrest with failed homolog pairing; both sexes infertile — establishing the mechanism.
  - Zhang et al. 2022 ([PMID: 35708642](https://pubmed.ncbi.nlm.nih.gov/35708642/)): Kash5 C-terminal-deleted mice show defective homolog pairing and accelerated oocyte depletion, modeling the female (POI/POF22) phenotype.
- **In vitro / ex vivo systems:** Wu et al. 2022 used ex vivo and in vitro assays to show the p.Leu197Pro missense blocks KASH5 NE distribution and SUN1 enrichment — a cell-based functional model of the human missense allele.
- **Structural models:** The SUN1–SPDYA–CDK2 crystal structure ([PMID: 34039995](https://pubmed.ncbi.nlm.nih.gov/34039995/)) and EM tomography of mouse LINC complexes at telomere attachment sites ([PMID: 31633067](https://pubmed.ncbi.nlm.nih.gov/31633067/); ~76 LINC complexes estimated per telomere attachment site) illuminate the molecular architecture KASH5 participates in.
- **Phenotype recapitulation:** **High** — the mouse reproduces the defining human feature (zygotene arrest, pairing/synapsis failure, azoospermia/infertility), making it a faithful model. **Limitation:** mouse models and cell assays cannot fully capture human testicular histologic variability or the potential for rare residual spermatogenesis.
- **Resources:** MGI (mouse *Kash5*/*Ccdc155*); IMPC/IMSR for alleles.

---

## Mechanistic Model (Synthesis)

```
 Biallelic KASH5/CCDC155 LoF variant (19q13.33)
   [frameshift p.R327Sfs*21 | CNV del(19)(q13.33) | CC missense p.L197P | splice c.747G>A]
            │  loss of / mislocalized KASH5 protein
            ▼
 Failure to assemble SUN1–KASH5 LINC complex at the nuclear envelope
            │  (p.L197P blocks NE distribution + SUN1 enrichment — demonstrated)
            ▼
 KASH5 cannot recruit cytoplasmic dynein → telomeres uncoupled from microtubules
            ▼
 Loss of telomere-led chromosome movement & bouquet formation (mouse-demonstrated)
            ▼
 Failed homologous pairing & synapsis  ──►  Unresolved meiotic DSB repair
            │                                         │
            └───────────────┬─────────────────────────┘
                            ▼
          Meiotic checkpoint arrest at ZYGOTENE-like (pre-pachytene) stage
                            ▼
          Germ-cell elimination / spermatocyte maturation arrest
                            ▼
        ┌─────────────────────────────┬───────────────────────────────┐
        ▼ (male)                       ▼ (female, same locus)
 Non-obstructive azoospermia      Accelerated oocyte depletion →
 → male infertility (SPGF88)      Premature ovarian insufficiency (POF22)
```

The model is strongly supported: every step from LINC-complex assembly failure through zygotene arrest is demonstrated in either human patients (NE-targeting/SUN1 recruitment, zygotene arrest, DSB persistence) or the mouse (pairing failure, bouquet dependence), with cross-species concordance. The only inferred (vs directly demonstrated-in-human) step is the loss of telomere-led movement/bouquet formation, which rests on mouse and cell-biological evidence.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [35674372](https://pubmed.ncbi.nlm.nih.gov/35674372/) | *Novel bi-allelic variants in KASH5… NOA* | Human clinical | Anchors gene/locus; frameshift + CNV biallelic genotype; human zygotene arrest (Findings 1, 2) |
| [35587281](https://pubmed.ncbi.nlm.nih.gov/35587281/) | *Homozygous missense in CCDC155 disrupts CCDC155/SUN1… NOA & POI* | Human + in vitro | Adds coiled-coil missense class; NE-mislocalization + SUN1-recruitment failure; DSB-repair step (Finding 4) |
| [29790874](https://pubmed.ncbi.nlm.nih.gov/29790874/) | *Point-of-care WES of idiopathic male infertility* | Human clinical | First human CCDC155–NOA link; testis-specific expression; NOA 1% epidemiology (Finding 5) |
| [24062341](https://pubmed.ncbi.nlm.nih.gov/24062341/) | *Mammalian KASH-domain protein coupling meiotic chromosomes to cytoskeleton* | Mouse model | Original Kash5-null mechanism: arrest via failed pairing; dynein-coupling requirement (Finding 2) |
| [24637401](https://pubmed.ncbi.nlm.nih.gov/24637401/) | *The missing LINC…* | Review | Frames SUN1–KASH5 LINC biology; leptotene/zygotene arrest in KASH5-deficient mice |
| [35708642](https://pubmed.ncbi.nlm.nih.gov/35708642/) | *Homozygous variant in KASH5 causes POI…* | Human + mouse | Female (POF22) counterpart; splice variant; disordered homolog pairing |
| [34039995](https://pubmed.ncbi.nlm.nih.gov/34039995/) | *SUN1-SPDYA interaction in meiosis prophase I* | Structural/mouse | Molecular architecture of the telomere–LINC connection |
| [31633067](https://pubmed.ncbi.nlm.nih.gov/31633067/) | *EM tomography of mouse LINC complexes at meiotic telomeres* | Structural | Quantitative LINC-complex architecture (~76 per attachment site) |
| [42479255](https://pubmed.ncbi.nlm.nih.gov/42479255/) | *Meiotic telomeres of vole B chromosomes* | Comparative | Conservation of SUN1/KASH5 telomere-attachment machinery |

All PMIDs above appear in the reviewed literature and directly support the cited claims. Papers in the literature list concerning unrelated NOA genetics (Y-microdeletions, DMRT1, POLG, miRNAs, Fas/FasL, cancer-variant load) were reviewed for context on the broader NOA landscape but do not bear on the KASH5 mechanism and are not cited as evidence for SPGF88-specific claims.

---

## Limitations and Knowledge Gaps

1. **Very small human sample size.** The entire human evidence base for SPGF88 rests on a handful of patients across three families/cohorts. Penetrance, expressivity, and genotype–phenotype correlations cannot be robustly estimated.
2. **No epidemiology.** There is no prevalence/incidence estimate specific to SPGF88; it is an ultra-rare monogenic slice of the ~1% NOA population.
3. **CNV detectability.** One pathogenic allele was a 19q13.33 deletion, meaning WES/panel sequencing alone can miss the second allele; CNV/array analysis is required but not always performed.
4. **No human protein structure.** No experimental KASH5 structure is deposited in the PDB; structural interpretation of missense variants (e.g., p.Leu197Pro) relies on domain annotation and AlphaFold.
5. **Residual spermatogenesis unknown.** Whether any hypomorphic allele permits rare post-meiotic cells (and thus TESE success) has not been demonstrated; all reported cases are azoospermic.
6. **Inferred steps.** Loss of telomere-led movement/bouquet in human patients is inferred from mouse/cell data rather than directly imaged in patient spermatocytes.
7. **No therapeutics.** There is no disease-modifying treatment and no clinical trial; management is supportive/reproductive.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient series** via international consortia (e.g., GeneMatcher, IMIGC) to collect additional biallelic KASH5 cases, enabling genotype–phenotype and penetrance estimates.
2. **Always pair WES with CNV/array analysis** in NOA diagnostics for KASH5, given the demonstrated compound-het CNV allele; report variants to ClinVar to build classification evidence.
3. **Patient testicular histology + immunostaining** (SYCP1/SYCP3 synapsis markers, γH2AX for DSBs, telomere/LINC markers) to directly confirm the inferred bouquet/movement defect in humans.
4. **Functional assays for each new variant** (NE-localization and SUN1/dynein-binding assays as in Wu 2022) to classify VUS and distinguish complete-LoF from hypomorphic alleles.
5. **Correlate variant severity with micro-TESE outcome** prospectively to establish whether any allele predicts rare sperm retrieval, refining counseling.
6. **Structural determination** (cryo-EM/crystallography) of the human KASH5 coiled-coil and KASH–SUN1 interface to mechanistically interpret missense variants.
7. **iPSC-derived germ-cell or organoid models** carrying patient variants to study the human meiotic block and screen for rescue strategies.
8. **Carrier/cascade screening and PGT-M counseling** in affected consanguineous families as a concrete clinical action.

---

*Report compiled from 5 iterations, 5 confirmed findings, and 19 reviewed papers. Evidence spans human clinical case reports, mouse knockout models, in vitro functional assays, and structural/computational data, as indicated per claim.*


## Artifacts

- [OpenScientist final report](Spermatogenic_Failure_88-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spermatogenic_Failure_88-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

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
| Terms checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 7 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011462` (3 mentions) - the report calls it "Young adult onset", "clinical onset is young-adult"; HP calls it **Young adult onset**
- `HP:0008209` (1 mention) - the report calls it "(Female counterpart) Premature ovarian insufficiency"; HP calls it **Premature ovarian insufficiency**
- `GO:0005640` (2 mentions) - the report calls it "Subcellular level:** **Nuclear envelope / outer nuclear membrane"; GO calls it **nuclear outer membrane**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0011462` - called "Young adult onset", "clinical onset is young-adult"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

24 of 25 terms resolved to a current term; the rest could not be looked up either way.