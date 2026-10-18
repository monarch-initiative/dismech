---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T23:56:03.507572'
end_time: '2026-09-26T00:12:16.505244'
duration_seconds: 973.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Erysipelas
  mondo_id: MONDO:0001266
  category: Infectious Disease
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
citation_count: 38
reference_validation:
  total_references: 38
  verified: 38
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 12
  relevance_assessed: 38
  on_topic: 11
  off_topic: 3
  off_topic_references:
  - PMID:11801184
  - PMID:27806170
  - PMID:30542523
  needs_review: true
  validator_version: 0.3.0rc2
term_validation:
  total_terms: 26
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 6
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Erysipelas-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Erysipelas-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Erysipelas
- **MONDO ID:** MONDO:0001266 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Erysipelas** covering all of the
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

# Erysipelas (MONDO:0001266): A Comprehensive Disease Characterization

## Summary

**Erysipelas is an acute, sharply demarcated bacterial infection of the superficial dermis and dermal lymphatics, caused predominantly by β-hemolytic streptococci** — chiefly *Streptococcus pyogenes* (group A streptococcus, GAS) and Lancefield groups C and G (*S. dysgalactiae* subsp. *equisimilis*, GCS/GGS). Bacteria enter through a breached cutaneous barrier — most often interdigital tinea pedis (toe-web intertrigo), traumatic wounds, or excoriated dermatoses — and in the setting of impaired lymphatic drainage (leg edema, lymphedema, obesity, venous insufficiency) proliferate to produce a fiery-red, raised, well-marginated plaque accompanied by the abrupt onset of fever and chills. Unlike most entries in a disease knowledge base, erysipelas is **not a genetic disorder**: it is an environmentally and microbiologically driven infection, a clinical diagnosis with no causal genes, pathogenic variants, or inheritance pattern.

The disease is **leg-predominant** (~90% of cases), affects **adults and the elderly** with a female predominance in most hospital series, shows **seasonal (summer) clustering**, and is strongly **recurrence-prone**. Its pathophysiology is dominated by a **self-reinforcing erysipelas–lymphedema vicious cycle**: pre-existing (often subclinical) lymphatic impairment predisposes to infection, and each infectious episode further damages lymphatics, worsening edema and increasing the risk of the next episode, culminating in some cases in elephantiasis nostras verrucosa. Management rests on **narrow-spectrum penicillin**, to which erysipelas responds rapidly (≈98% within 2 days), and guideline-adherent narrow-spectrum therapy is associated with better outcomes. Recurrence is countered by **treating the portal of entry** (antifungal therapy for tinea pedis), **edema/lymphedema management**, and — after repeated episodes — **low-dose prophylactic penicillin V**, whose efficacy during treatment is confirmed by two randomized controlled trials (PATCH I & II) and a Cochrane systematic review.

A crucial nosological point for knowledge-base curation: streptococcal erysipelas (the subject of this report, MONDO:0001266) is **distinct from the identically named *Erysipelothrix rhusiopathiae* diseases** — swine erysipelas (a veterinary disease of pigs) and human erysipeloid (Baker-Rosenbach disease, an occupational zoonosis). These share a name and, historically, clinical resemblance, but have a completely different etiologic agent, epidemiology, and reservoir.

---

## Key Findings

### Finding 1 — β-hemolytic streptococci are the predominant cause

Erysipelas is overwhelmingly a **streptococcal** infection. In a large retrospective cohort of 1,142 erysipelas episodes (981 patients), wound cultures grew group A streptococci (GAS, n=56), group G streptococci (GGS, n=53), group C streptococci (GCS, n=11), and *Staphylococcus aureus* (n=153); blood cultures (obtained in 49% of episodes) were positive in 50, most commonly GGS (n=21) followed by GAS (n=13) ([PMID: 26424182](https://pubmed.ncbi.nlm.nih.gov/26424182/)). Because superficial cultures frequently recover skin-colonizing *S. aureus* that is not the true pathogen, serologic and prospective data are decisive. In a prospective cellulitis study (n=216), β-hemolytic streptococcal etiology was confirmed serologically or by culture in **72% (146/203)** of cases, rising to **85%** when probable cases were included; in lower-extremity infection, GCS/GGS were actually more common than GAS (36 vs 22) ([PMID: 26734653](https://pubmed.ncbi.nlm.nih.gov/26734653/)).

> "*Wound cultures were taken in 343 episodes and 56 grew group A streptococci (GAS), 53 grew group G streptococci (GGS), 11 grew group C streptococci (GCS), and 153 grew Staphylococcus aureus.*" ([PMID: 26424182](https://pubmed.ncbi.nlm.nih.gov/26424182/))

> "*Serology or blood or tissue culture confirmed β-hemolytic streptococcal (BHS) etiology in 72% (146 of 203) of cases.*" ([PMID: 26734653](https://pubmed.ncbi.nlm.nih.gov/26734653/))

The relevant pathogens (NCBITaxon suggestions): *Streptococcus pyogenes* (NCBITaxon:1314), *Streptococcus dysgalactiae* subsp. *equisimilis* (NCBITaxon:119602). Group C/G streptococci carry virulence factors closely paralleling GAS — M protein, streptolysin O, streptolysin S, streptokinase, hyaluronidase, and C5a peptidase ([PMID: 20607346](https://pubmed.ncbi.nlm.nih.gov/20607346/)).

### Finding 2 — Skin barrier disruption and leg edema/lymphedema are the dominant risk factors

The two strongest, most reproducible risk factors are a **breach in the skin barrier** and **leg edema**. In a Tunisian multicenter case-control study (114 cases, 208 matched controls), multivariate analysis showed that disruption of the cutaneous barrier (traumatic wound, toe-web intertrigo, excoriated dermatosis, plantar squamous lesions) carried an odds ratio of **13.6 (95% CI 6.0–31)** and leg edema an OR of **7.0 (95% CI 1.3–38)**; notably there was **no** association with diabetes, alcoholism, or smoking ([PMID: 16484815](https://pubmed.ncbi.nlm.nih.gov/16484815/)). A large population-based case-control study of severe lower-leg cellulitis (29,062 case-control pairs) independently confirmed **tinea pedis (AOR 3.05, 95% CI 1.45–6.42)**, **varicose veins (AOR 2.95)**, **lymphoedema (AOR 2.65)**, and **obesity (AOR 2.05)**; incidence reached 204.8/100,000 by 2013, rising 4.7%/year ([PMID: 29427797](https://pubmed.ncbi.nlm.nih.gov/29427797/)).

> "*disruption of the cutaneous barrier ... and leg edema were independently associated with erysipelas of the leg, with respective odds ratios of 13.6 (95% confidence interval: 6.0-31) and 7.0 (1.3-38)*" ([PMID: 16484815](https://pubmed.ncbi.nlm.nih.gov/16484815/))

> "*varicose veins (AOR 2.95, 95% CI 2.50-3.48, p < 0.001), lymphoedema (AOR 2.65, 95% CI 1.71-4.10, p < 0.001), tinea pedis (AOR 3.05, 95% CI 1.45-6.42, p 0.003)*" ([PMID: 29427797](https://pubmed.ncbi.nlm.nih.gov/29427797/))

The clinical corollary is that **toe-web intertrigo is a high-attributable-risk, modifiable portal of entry**, and secondary prevention targeting it has long been advocated ([PMID: 11319357](https://pubmed.ncbi.nlm.nih.gov/11319357/)).

### Finding 3 — Prophylactic low-dose penicillin V reduces recurrence

Recurrence prevention is evidence-based. In the **PATCH I** double-blind RCT (n=274, patients with ≥2 prior episodes), penicillin V 250 mg twice daily for 12 months reduced recurrence during prophylaxis to **22% (30/136) vs 37% (51/138)** on placebo — **HR 0.55 (95% CI 0.35–0.86, P=0.01)**, number-needed-to-treat ≈5 ([PMID: 23635049](https://pubmed.ncbi.nlm.nih.gov/23635049/)). The protective effect **waned after stopping** the drug. **PATCH II** (n=123, mostly patients with a single prior episode) showed a concordant but non-significant 47% risk reduction (**HR 0.53, 95% CI 0.26–1.07, P=0.08**) ([PMID: 21910701](https://pubmed.ncbi.nlm.nih.gov/21910701/)). A pooled economic analysis (n=397) found a **29% reduction in recurrences (IRR 0.71, 95% CI 0.53–0.90, P=0.02)** and cost-effectiveness ([PMID: 24551029](https://pubmed.ncbi.nlm.nih.gov/24551029/)).

> "*30 of 136 participants in the penicillin group (22%) had a recurrence, as compared with 51 of 138 participants in the placebo group (37%) (hazard ratio, 0.55; ... P=0.01)*" ([PMID: 23635049](https://pubmed.ncbi.nlm.nih.gov/23635049/))

### Finding 4 — Rapid penicillin response; narrow-spectrum guideline adherence improves outcomes

Erysipelas responds rapidly to penicillin: in a retrospective study, **98.3% of erysipelas patients responded within 2 days to Penicillin G**, and constitutional symptoms (chills/fever) preceded or coincided with erythema in 91.4% of erysipelas vs only 36.2% of cellulitis patients — supporting clinical differentiation ([PMID: 41562377](https://pubmed.ncbi.nlm.nih.gov/41562377/)). In prospective facial cellulitis (n=65), β-hemolytic streptococcal etiology was probable/confirmed in **75%** and penicillin(-class) monotherapy cured 68% ([PMID: 28768452](https://pubmed.ncbi.nlm.nih.gov/28768452/)). In a cohort of 630 erysipelas/cellulitis cases, **adherence to narrow-spectrum guidelines was associated with fewer poor outcomes (6.3% vs 12.7%, p=0.007)**; bacteremia (AOR 5.21) and peripheral arterial disease (AOR 4.80) predicted poor outcome ([PMID: 30685804](https://pubmed.ncbi.nlm.nih.gov/30685804/)).

> "*Of patients with erysipelas, 98.3% responded within 2 days to penicillin*" ([PMID: 41562377](https://pubmed.ncbi.nlm.nih.gov/41562377/))

> "*A poor outcome was recorded in 54 (8.5%) patients, less frequently in case of adherence to guidelines: 26/410 (6.3%) vs 28/220 (12.7%), p = 0.007*" ([PMID: 30685804](https://pubmed.ncbi.nlm.nih.gov/30685804/))

### Finding 5 — Erysipelas and lymphedema form a self-reinforcing vicious cycle

Lymphatic dysfunction is both **cause and consequence**. Lymphoscintigraphy of 106 post-erysipelas patients found **subclinical lymphedema in the clinically unaffected leg in 82%**, rising from 74% after a single episode to **100% after ≥3 episodes** — implicating pre-existing lymphatic impairment as a primary trigger and demonstrating cumulative damage ([PMID: 40542699](https://pubmed.ncbi.nlm.nih.gov/40542699/)). A prospective cohort of 428 patients identified **obesity, diabetes mellitus, venous insufficiency, lymphedema, and prior surgery** as independent risk factors for recurrence (Cox model, all p<0.05) ([PMID: 33413190](https://pubmed.ncbi.nlm.nih.gov/33413190/)). A retrospective-prospective cohort (n=313) found recurrent erysipelas significantly associated with **obesity (p<0.0001)**, chronic edema/lymphedema, peripheral arterial disease, fungal foot infection, and tonsillectomy (p=0.000001) ([PMID: 30976336](https://pubmed.ncbi.nlm.nih.gov/30976336/)).

> "*Subclinical lymphedema on the unaffected leg was found in 82% of patients*" ([PMID: 40542699](https://pubmed.ncbi.nlm.nih.gov/40542699/))

### Finding 6 — Epidemiology: adult/elderly, female-predominant, leg-predominant, seasonal

Hospital cohorts converge: 428 patients (mean age 58.6 y, 51% women; hypertension 51.6%, diabetes 41.6%, venous insufficiency 36.2%, obesity 12.1%, lymphedema 4.2%; seasonal) ([PMID: 20147345](https://pubmed.ncbi.nlm.nih.gov/20147345/)); a Tunisian series of 647 patients (mean age 44.7 y, M:F ≈1.55, **lower limbs 91.2%**, portal of entry 76.7% mainly toe-web intertrigo, prior erysipelas 26.1%, good outcome 87.8% on IM penicillin G ×10 days) ([PMID: 15822466](https://pubmed.ncbi.nlm.nih.gov/15822466/)); and a 10-year study (n=319, median age 63 y, 65% female, summer-predominant, lower limb 59.2%, recurrence 67.3%, **complications 25%** including abscess, lymphangitis, and elephantiasis) ([PMID: 18069381](https://pubmed.ncbi.nlm.nih.gov/18069381/)).

> "*Erysipelas predominately involved in the lower limbs (91.2%). Antecedents of erysipelas were found in 26.12 %. Portal of entry was found in 76.66% represented essentially by toe-web intertrigo.*" ([PMID: 15822466](https://pubmed.ncbi.nlm.nih.gov/15822466/))

> "*Complications, such as abscess formation, lymphangitis, venous insufficiency, osteitis, arthritis, septic tendonitis and elephantiasis were found in 25%.*" ([PMID: 18069381](https://pubmed.ncbi.nlm.nih.gov/18069381/))

### Finding 7 — Streptococcal erysipelas is distinct from Erysipelothrix disease

**Erysipeloid** (Baker-Rosenbach disease) is an occupational human skin infection caused by traumatic penetration of *Erysipelothrix rhusiopathiae*, presenting as a violaceous, well-demarcated erythematous edema usually on the hand/fingers, often self-limited and penicillin-responsive; it can rarely cause endocarditis (aortic valve predilection) ([PMID: 19663854](https://pubmed.ncbi.nlm.nih.gov/19663854/)). In animals, *E. rhusiopathiae* causes **swine erysipelas**, with domestic pigs the principal host; 30–50% of healthy/convalescent pigs carry the organism in tonsils/lymphoid tissue, and wild boar are a potential reservoir ([PMID: 42687202](https://pubmed.ncbi.nlm.nih.gov/42687202/)). It is a zoonosis affecting farmers, butchers, fishers, and veterinarians ([PMID: 20171435](https://pubmed.ncbi.nlm.nih.gov/20171435/)).

> "*Erysipeloid is an occupational infection of the skin caused by traumatic penetration of Erysipelothrix rhusiopathiae. The disease is characterized clinically by an erythematous oedema, with well-defined and raised borders, usually localized to the back of one hand and/or fingers.*" ([PMID: 19663854](https://pubmed.ncbi.nlm.nih.gov/19663854/))

### Finding 8 — Cochrane meta-analysis supports antibiotic prophylaxis

A 2017 Cochrane systematic review (6 RCTs, 573 evaluable participants, mean age 50–70) concluded that antibiotic prophylaxis (mainly penicillin/erythromycin) reduces recurrence risk **while on treatment**, with the protective effect diminishing after prophylaxis is stopped — consistent with PATCH I/II ([PMID: 28631307](https://pubmed.ncbi.nlm.nih.gov/28631307/)).

> "*We included six trials, with a total of 573 evaluable participants, who were aged on average between 50 and 70.*" ([PMID: 28631307](https://pubmed.ncbi.nlm.nih.gov/28631307/))

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Erysipelas is an acute, non-necrotizing bacterial infection of the **upper dermis and superficial dermal lymphatics**, classically presenting as a fiery-red, raised, well-demarcated, indurated plaque with an advancing border, warmth, tenderness, and abrupt systemic symptoms (high fever, chills). The sharp elevation and clear demarcation distinguish it from cellulitis, which involves deeper dermis and subcutaneous fat with less distinct borders. It is a **clinical diagnosis** made at the disease level (case series, cohorts), not from molecular/EHR variant data.

**Key identifiers:**
- **MONDO:** MONDO:0001266
- **ICD-10:** A46 (Erysipelas); **ICD-11:** 1B70.0
- **MeSH:** Erysipelas (D004886)
- **SNOMED CT:** 33438006 (Erysipelas)
- **OMIM / Orphanet:** Not applicable — erysipelas is an acquired infectious disease with no Mendelian OMIM entry and is not a rare disease with an Orphanet number.

**Synonyms / alternative names:** St. Anthony's fire (historical), "ignis sacer," "the rose" (regional). Note that "erysipelas" in a veterinary/occupational context refers to *Erysipelothrix* disease (see Section 14), which must not be conflated with this streptococcal entity.

**Source type:** Aggregated disease-level evidence (cohorts, case-control studies, RCTs, systematic reviews); no patient-level EHR dataset was supplied for this investigation.

### 2. Etiology

**Causal factors.** Erysipelas is an **infectious disease** caused predominantly by β-hemolytic streptococci — *S. pyogenes* (GAS) and groups C/G (*S. dysgalactiae*); *S. aureus* is a less common contributor and often a colonizer (Finding 1). There is **no genetic causal factor** and no Mendelian inheritance.

**Risk factors (environmental / host):**

| Risk factor | Effect size | Source |
|---|---|---|
| Cutaneous barrier disruption (wound, toe-web intertrigo, dermatosis) | OR 13.6 (6.0–31) | [PMID: 16484815](https://pubmed.ncbi.nlm.nih.gov/16484815/) |
| Leg edema | OR 7.0 (1.3–38) | [PMID: 16484815](https://pubmed.ncbi.nlm.nih.gov/16484815/) |
| Tinea pedis | AOR 3.05 (1.45–6.42) | [PMID: 29427797](https://pubmed.ncbi.nlm.nih.gov/29427797/) |
| Varicose veins | AOR 2.95 (2.50–3.48) | [PMID: 29427797](https://pubmed.ncbi.nlm.nih.gov/29427797/) |
| Lymphoedema | AOR 2.65 (1.71–4.10) | [PMID: 29427797](https://pubmed.ncbi.nlm.nih.gov/29427797/) |
| Obesity | AOR 2.05 | [PMID: 29427797](https://pubmed.ncbi.nlm.nih.gov/29427797/) |
| Diabetes, venous insufficiency, prior surgery | Recurrence RFs (p<0.05) | [PMID: 33413190](https://pubmed.ncbi.nlm.nih.gov/33413190/) |

**Genetic risk factors:** None established. The Tunisian case-control study found no association with diabetes, alcoholism, or smoking after multivariate adjustment ([PMID: 16484815](https://pubmed.ncbi.nlm.nih.gov/16484815/)), underlining the environmental/host-mechanical rather than genetic basis.

**Protective factors:** Treatment of the portal of entry (antifungal therapy for tinea pedis), edema/lymphedema control (compression, elevation), weight reduction, and — for recurrence — antibiotic prophylaxis (Findings 3, 8). No genetic protective alleles are described.

**Gene–environment interactions:** Not applicable in the classical sense; the disease is driven by pathogen–host barrier–lymphatic interactions rather than genotype-by-environment effects.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Frequency / notes |
|---|---|---|---|
| Sharply demarcated erythematous plaque | Clinical sign | HP:0000988 (Skin rash) / HP:0011121 (Abnormal skin morphology) | Defining feature |
| Fever | Symptom | HP:0001945 (Fever) | ~91% report chills/fever at/before onset ([PMID: 41562377](https://pubmed.ncbi.nlm.nih.gov/41562377/)) |
| Chills | Symptom | HP:0025143 (Chills) | Common, precedes rash |
| Local warmth / edema | Clinical sign | HP:0000969 (Edema) | Common |
| Regional lymphangitis / lymphadenopathy | Clinical sign | HP:0002716 (Lymphadenopathy) | Component of complications ([PMID: 18069381](https://pubmed.ncbi.nlm.nih.gov/18069381/)) |
| Leukocytosis / elevated CRP | Lab abnormality | HP:0001974 (Leukocytosis) | Inflammatory response, higher in recurrent cases ([PMID: 19694769](https://pubmed.ncbi.nlm.nih.gov/19694769/)) |
| "Milian's ear sign" (auricle involvement in facial erysipelas) | Clinical sign | — | Localizing sign ([PMID: 32241881](https://pubmed.ncbi.nlm.nih.gov/32241881/)) |

**Characteristics:** Adult/elderly onset; acute onset (hours to 1–2 days); severity mild-to-severe (bullous, hemorrhagic, or abscess-forming variants); course episodic/recurrent. **Quality-of-life impact:** recurrent episodes and resulting chronic lymphedema/elephantiasis impose substantial disability, repeated hospitalization, and reduced mobility. Disease-specific QoL instruments were not identified in the reviewed literature.

### 4. Genetic / Molecular Information

**Not applicable.** Erysipelas has no causal genes, no pathogenic germline/somatic variants, no modifier genes, no disease-associated epigenetic signature, and no chromosomal abnormalities. It is an acquired infectious disease. (The molecular determinants of virulence reside in the *bacterial* genome — e.g., streptolysin O/S, M protein, streptokinase, hyaluronidase, C5a peptidase — [PMID: 20607346](https://pubmed.ncbi.nlm.nih.gov/20607346/); [PMID: 20385762](https://pubmed.ncbi.nlm.nih.gov/20385762/) — not the human host.)

### 5. Environmental Information

- **Environmental / occupational:** breaks in skin from trauma, animal bites/stings (insect bites are a recognized portal → erysipelas [PMID: 16679881](https://pubmed.ncbi.nlm.nih.gov/16679881/)), and use of depigmenting agents (in some populations [PMID: 21695874](https://pubmed.ncbi.nlm.nih.gov/21695874/)).
- **Lifestyle:** obesity is a strong, reproducible factor (Findings 2, 5). Smoking/alcohol were **not** independently associated ([PMID: 16484815](https://pubmed.ncbi.nlm.nih.gov/16484815/)).
- **Infectious agents (NCBITaxon):** *Streptococcus pyogenes* (NCBITaxon:1314); *S. dysgalactiae* subsp. *equisimilis* (groups C/G, NCBITaxon:119602); occasionally *Staphylococcus aureus* (NCBITaxon:1280). Interdigital dermatophytes (*Trichophyton* spp.) act as facilitators by breaching the barrier.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. **Predisposing lymphatic impairment** (pre-existing subclinical lymphedema, venous insufficiency, obesity) **reduces local immune clearance** in the dermis — *demonstrated* by 82% subclinical lymphedema in the unaffected leg ([PMID: 40542699](https://pubmed.ncbi.nlm.nih.gov/40542699/)).
2. A **breach in the cutaneous barrier** (toe-web tinea, wound, dermatosis) **provides a portal of entry** → *leads to* streptococcal inoculation of the dermis ([PMID: 16484815](https://pubmed.ncbi.nlm.nih.gov/16484815/); [PMID: 15822466](https://pubmed.ncbi.nlm.nih.gov/15822466/)).
3. **β-hemolytic streptococci proliferate** in the superficial dermis and **spread along dermal lymphatics** → *results in* the characteristic sharply demarcated, raised, advancing plaque ([PMID: 26424182](https://pubmed.ncbi.nlm.nih.gov/26424182/); [PMID: 26734653](https://pubmed.ncbi.nlm.nih.gov/26734653/)).
4. **Streptococcal virulence factors** (streptolysin O/S, M protein, streptokinase, hyaluronidase, C5a peptidase) **promote tissue spread and impair neutrophil recruitment** → *drives* local injury and dissemination (*inferred* for human erysipelas from GAS biology and animal models: [PMID: 20607346](https://pubmed.ncbi.nlm.nih.gov/20607346/); [PMID: 28947648](https://pubmed.ncbi.nlm.nih.gov/28947648/); [PMID: 11801184](https://pubmed.ncbi.nlm.nih.gov/11801184/)).
5. The **innate immune / inflammatory response** (neutrophil influx, cytokine release) **produces erythema, warmth, edema, and systemic fever/chills and leukocytosis/↑CRP** → *causes* the clinical syndrome ([PMID: 41562377](https://pubmed.ncbi.nlm.nih.gov/41562377/); [PMID: 19694769](https://pubmed.ncbi.nlm.nih.gov/19694769/)).
6. **Inflammatory injury to lymphatic vessels** **further impairs lymphatic drainage** → *worsens* edema. **[BRANCH → vicious cycle]** This cumulative lymphatic damage **increases susceptibility to the next episode**, and repeated episodes drive **chronic lymphedema → elephantiasis nostras verrucosa** (subclinical lymphedema rises to 100% after ≥3 episodes: [PMID: 40542699](https://pubmed.ncbi.nlm.nih.gov/40542699/); complications incl. elephantiasis in 25%: [PMID: 18069381](https://pubmed.ncbi.nlm.nih.gov/18069381/)).
7. **[BRANCH → systemic]** In a minority, bacteremia (blood cultures positive in ~6.9% overall) **leads to invasive complications** — abscess, necrotizing fasciitis, rarely myocarditis ([PMID: 23498835](https://pubmed.ncbi.nlm.nih.gov/23498835/)) — associated with poor outcome ([PMID: 30685804](https://pubmed.ncbi.nlm.nih.gov/30685804/)).

```
Lymphatic impairment ─┐
                      ├─► Barrier breach ─► Strep dermal invasion ─► Lymphatic spread
Skin breach ──────────┘                                                    │
                                                                           ▼
     ┌──────────────────  Inflammation (fever, chills, erythema)  ◄────────┤
     │                                                                     ▼
     │                                            Lymphatic vessel injury
     │                                                     │
     └──────────  VICIOUS CYCLE  ◄── worsening edema ◄─────┘
                        │
                        └─► chronic lymphedema ─► elephantiasis (~25%)
```

- **Molecular pathways / cellular processes:** innate inflammatory signaling (NF-κB–driven cytokine production), neutrophil chemotaxis and phagocytosis. GO suggestions: **GO:0006954** (inflammatory response), **GO:0006935** (chemotaxis), **GO:0050900** (leukocyte migration), **GO:0001945** (lymph vessel development, relevant to damage/repair).
- **Immune involvement:** acute innate response; no autoimmunity or immunodeficiency required, though HIV can predispose to severe disease/necrotizing fasciitis ([PMID: 21695874](https://pubmed.ncbi.nlm.nih.gov/21695874/)).
- **Cell types (CL):** neutrophil (**CL:0000775**), keratinocyte (**CL:0000312**), dermal lymphatic endothelial cell (**CL:0002138**), macrophage (**CL:0000235**).

### 7. Anatomical Structures Affected

- **Primary organ:** skin (**UBERON:0002097**), specifically the superficial dermis (**UBERON:0002067**) and dermal lymphatic vessels (**UBERON:0001473** lymphatic vessel).
- **Body systems:** integumentary and **lymphatic/lymphoid system** (**UBERON:0002465** lymphoid system).
- **Localization:** lower limb / leg (**UBERON:0000978** leg) in ~90% of cases ([PMID: 15822466](https://pubmed.ncbi.nlm.nih.gov/15822466/)); face (**UBERON:0000033** head) is the classic second site (Milian's ear sign, [PMID: 32241881](https://pubmed.ncbi.nlm.nih.gov/32241881/)).
- **Lateralization:** typically **unilateral**; bilateral leg erysipelas is rare and should prompt reconsideration of the diagnosis (pseudocellulitis/stasis dermatitis, [PMID: 36800152](https://pubmed.ncbi.nlm.nih.gov/36800152/)).
- **Tissue/cell level:** epithelial (epidermis/keratinocytes) and lymphatic endothelium; **secondary organ involvement** — abscess, osteitis, arthritis, septic tendonitis, rarely myocarditis (Finding 6; [PMID: 23498835](https://pubmed.ncbi.nlm.nih.gov/23498835/)).

### 8. Temporal Development

- **Onset:** adult/elderly predominance (mean age 44–63 y across series); **acute** onset over hours, often with prodromal chills/fever preceding the rash ([PMID: 41562377](https://pubmed.ncbi.nlm.nih.gov/41562377/)).
- **Progression:** rapid local spread over 1–3 days; **self-limited with treatment** (≈98% respond to penicillin within 2 days, [PMID: 41562377](https://pubmed.ncbi.nlm.nih.gov/41562377/)), but strongly **recurrent/episodic** (recurrence 26–67% across cohorts; [PMID: 15822466](https://pubmed.ncbi.nlm.nih.gov/15822466/), [PMID: 18069381](https://pubmed.ncbi.nlm.nih.gov/18069381/)).
- **Patterns:** treatment-induced remission is the norm; the critical intervention window is early narrow-spectrum antibiotics plus portal-of-entry and edema management to interrupt the vicious cycle. **Seasonal** (summer) clustering is reported ([PMID: 18069381](https://pubmed.ncbi.nlm.nih.gov/18069381/); [PMID: 20147345](https://pubmed.ncbi.nlm.nih.gov/20147345/)).

### 9. Inheritance and Population

- **Epidemiology:** population-based incidence of severe lower-leg cellulitis reached **204.8/100,000 (2013), rising 4.7%/year** ([PMID: 29427797](https://pubmed.ncbi.nlm.nih.gov/29427797/)).
- **Inheritance:** none — not a genetic disease (no AD/AR/X-linked/mitochondrial pattern; no penetrance/expressivity/anticipation/founder/consanguinity/carrier-frequency parameters apply).
- **Demographics:** adult/elderly; **female predominance** in most hospital series (51–65% women); leg-predominant (~90%); comorbidities hypertension (~52%), diabetes (~42%), venous insufficiency (~36%), obesity (~12%), lymphedema (~4%) ([PMID: 20147345](https://pubmed.ncbi.nlm.nih.gov/20147345/); [PMID: 15822466](https://pubmed.ncbi.nlm.nih.gov/15822466/); [PMID: 18069381](https://pubmed.ncbi.nlm.nih.gov/18069381/)).
- **Geographic:** cosmopolitan; toe-web intertrigo as portal of entry is prominent in warm-climate series (Tunisia, Togo).

### 10. Diagnostics

- **Clinical diagnosis** based on the characteristic sharply demarcated, raised, fiery-red plaque with acute fever/chills; constitutional symptoms preceding erythema favor erysipelas over cellulitis ([PMID: 41562377](https://pubmed.ncbi.nlm.nih.gov/41562377/)).
- **Laboratory:** leukocytosis, elevated CRP (LOINC 1988-5), often higher in recurrent cases ([PMID: 19694769](https://pubmed.ncbi.nlm.nih.gov/19694769/)). **Blood cultures positive in only ~6.9%** and generally low-yield ([PMID: 30685804](https://pubmed.ncbi.nlm.nih.gov/30685804/)); serology (anti-streptolysin O, anti-DNase B) increases etiologic confirmation ([PMID: 26734653](https://pubmed.ncbi.nlm.nih.gov/26734653/)).
- **Imaging:** ultrasound/MRI to exclude abscess or necrotizing fasciitis in atypical/severe presentations ([PMID: 28865532](https://pubmed.ncbi.nlm.nih.gov/28865532/)).
- **Differential diagnosis (critical):** stasis dermatitis and other "pseudocellulitis" are frequently misdiagnosed as cellulitis/erysipelas — bilateral presentation, chronicity, and lack of fever favor pseudocellulitis; misdiagnosis drives ~$195–515M/yr in avoidable US spending and unnecessary antibiotics ([PMID: 27806170](https://pubmed.ncbi.nlm.nih.gov/27806170/); [PMID: 36800152](https://pubmed.ncbi.nlm.nih.gov/36800152/)). Also exclude DVT, contact dermatitis, and necrotizing fasciitis.
- **Genetic/omics testing:** not applicable.

### 11. Outcome / Prognosis

- **Favorable** with prompt therapy: good outcome in 87.8% ([PMID: 15822466](https://pubmed.ncbi.nlm.nih.gov/15822466/)); poor outcome in ~8.5%, reduced by guideline adherence ([PMID: 30685804](https://pubmed.ncbi.nlm.nih.gov/30685804/)).
- **Complications (~25%):** abscess, lymphangitis, osteitis, arthritis, septic tendonitis, chronic venous insufficiency, and **elephantiasis nostras verrucosa**; rare systemic sequelae include myocarditis and necrotizing fasciitis ([PMID: 18069381](https://pubmed.ncbi.nlm.nih.gov/18069381/); [PMID: 23498835](https://pubmed.ncbi.nlm.nih.gov/23498835/); [PMID: 21695874](https://pubmed.ncbi.nlm.nih.gov/21695874/)).
- **Prognostic factors for poor outcome:** bacteremia (AOR 5.21), peripheral arterial disease (AOR 4.80) ([PMID: 30685804](https://pubmed.ncbi.nlm.nih.gov/30685804/)); obesity, diabetes, lymphedema for recurrence (Finding 5).
- Mortality is low for uncomplicated disease; deaths cluster in necrotizing fasciitis and immunocompromised patients ([PMID: 21695874](https://pubmed.ncbi.nlm.nih.gov/21695874/)).

### 12. Treatment

- **First-line pharmacotherapy:** **penicillin** (penicillin G IV/IM, or oral penicillin V / amoxicillin) — narrow-spectrum, rapidly effective (Finding 4). NCIT: **C692** (Penicillin), **C61785** (Penicillin V). Duration typically 10 days ([PMID: 15822466](https://pubmed.ncbi.nlm.nih.gov/15822466/)).
- **Penicillin-allergic:** macrolides (erythromycin/roxithromycin), clindamycin, or pristinamycin; a network meta-analysis found no significant cure-rate differences among first/second-line agents for cellulitis, with **pristinamycin showing the highest cure rates for erysipelas** (at some cost in rash) ([PMID: 39240378](https://pubmed.ncbi.nlm.nih.gov/39240378/)).
- **Adjunctive/emerging:** omadacycline and iclaprim have activity in skin/soft-tissue infection including erysipelas (90% clinical success at end of treatment for omadacycline) ([PMID: 42413095](https://pubmed.ncbi.nlm.nih.gov/42413095/); [PMID: 35928265](https://pubmed.ncbi.nlm.nih.gov/35928265/)).
- **Supportive:** limb elevation, edema/compression management, analgesia, and **treatment of the portal of entry** (topical antifungals for tinea pedis).
- **Recurrence prophylaxis:** low-dose penicillin V 250 mg BID (Findings 3, 8). NCIT: **C15329** (Antibiotic Therapy).
- **Pharmacogenomics:** not applicable.

### 13. Prevention

- **Primary:** foot hygiene, prompt treatment of tinea pedis and interdigital intertrigo, wound care, weight management, and edema/venous-insufficiency control (compression) — targeting the highest-attributable, modifiable risk factors ([PMID: 11319357](https://pubmed.ncbi.nlm.nih.gov/11319357/); [PMID: 16484815](https://pubmed.ncbi.nlm.nih.gov/16484815/); [PMID: 29427797](https://pubmed.ncbi.nlm.nih.gov/29427797/)).
- **Secondary/tertiary:** interrupting the erysipelas–lymphedema cycle through lymphedema therapy and, after ≥2 episodes, **antibiotic prophylaxis** with effect confirmed by RCTs and Cochrane review (Findings 3, 8). Protection wanes once prophylaxis stops, so long-term strategy must combine antibiotics with durable risk-factor modification.
- **Immunization:** no licensed vaccine; GAS vaccine development is ongoing but not erysipelas-specific.

### 14. Other Species / Natural Disease

**Important distinction (Finding 7):** Streptococcal erysipelas (this entry) is a human disease. The name "erysipelas" is also applied to *Erysipelothrix rhusiopathiae* disease:
- **Swine erysipelas** — a veterinary disease of **domestic pigs** (*Sus scrofa domesticus*, NCBITaxon:9825); 30–50% of healthy/convalescent pigs are tonsillar carriers; wild boar (*Sus scrofa*) are a reservoir (45.5% tonsil culture-positive) ([PMID: 42687202](https://pubmed.ncbi.nlm.nih.gov/42687202/)).
- **Human erysipeloid** (Baker-Rosenbach disease) — a **zoonotic** occupational skin infection of farmers, butchers, fishers, and veterinarians, with rare systemic forms (endocarditis with aortic-valve predilection; paravertebral abscess/spondylitis) ([PMID: 19663854](https://pubmed.ncbi.nlm.nih.gov/19663854/); [PMID: 20171435](https://pubmed.ncbi.nlm.nih.gov/20171435/); [PMID: 30542523](https://pubmed.ncbi.nlm.nih.gov/30542523/); [PMID: 22526696](https://pubmed.ncbi.nlm.nih.gov/22526696/)).

For **streptococcal** erysipelas itself, there is no significant naturally occurring companion-animal counterpart; GAS/GCS/GGS are human-adapted (GCS/GGS also colonize animals, but streptococcal erysipelas as a clinical entity is essentially human).

### 15. Model Organisms

Human streptococcal erysipelas is not modeled as a discrete named disease, but **murine skin-infection models** of *S. pyogenes* recapitulate key mechanistic steps: dermonecrotic/subcutaneous mouse models demonstrate the roles of **streptolysin S** and **platelet-activating-factor acetylhydrolase Sse** in inhibiting neutrophil recruitment and enabling systemic spread ([PMID: 28947648](https://pubmed.ncbi.nlm.nih.gov/28947648/); [PMID: 11801184](https://pubmed.ncbi.nlm.nih.gov/11801184/); [PMID: 20385762](https://pubmed.ncbi.nlm.nih.gov/20385762/)). These are **pathogen-focused** models (studying bacterial virulence and innate immune evasion) rather than models of the host lymphedema cycle. Resource: MGI for mouse strains; no dedicated erysipelas model database exists. **Limitation:** mouse dermonecrosis models capture bacterial invasion/immune evasion but not the chronic lymphatic-damage/recurrence dynamics central to human erysipelas.

---

## Mechanistic Model / Interpretation

Erysipelas is best understood as a **two-hit, self-amplifying disease**. The *first hit* is a susceptible host terrain — impaired lymphatic drainage (often subclinical), venous insufficiency, and obesity — that locally weakens immune surveillance. The *second hit* is a **portal of entry** (usually toe-web tinea) admitting β-hemolytic streptococci to the dermis. The organism's virulence arsenal drives rapid lymphatic spread and a brisk innate inflammatory response producing the pathognomonic plaque and systemic toxicity. Critically, that same inflammation **injures lymphatics**, so each episode leaves the host more vulnerable — the empirical signature being subclinical lymphedema in 74% of single-episode patients rising to 100% after ≥3 episodes. This explains why erysipelas is simultaneously highly treatable (near-universal rapid penicillin response) and highly recurrent, and why durable prevention requires attacking *both hits* (antifungal/portal care + edema management) alongside antibiotic prophylaxis whose benefit is real but reverses on discontinuation.

| Axis | Upstream driver | Downstream consequence |
|---|---|---|
| Host terrain | Lymphedema, venous insufficiency, obesity | Reduced dermal immune clearance |
| Portal | Tinea pedis, wounds, dermatoses | Streptococcal inoculation |
| Pathogen | SLO/SLS, M protein, spreading factors | Lymphatic spread, neutrophil evasion |
| Response | Innate inflammation | Plaque + fever + **lymphatic injury → cycle** |

---

## Evidence Base

| PMID | Contribution | Type |
|---|---|---|
| [26424182](https://pubmed.ncbi.nlm.nih.gov/26424182/) | Bacteriologic spectrum (n=1142); GGS common in blood | Human, retrospective |
| [26734653](https://pubmed.ncbi.nlm.nih.gov/26734653/) | 72–85% BHS etiology; GCS/GGS > GAS in legs | Human, prospective |
| [16484815](https://pubmed.ncbi.nlm.nih.gov/16484815/) | Barrier breach OR 13.6, edema OR 7.0 | Human, case-control |
| [29427797](https://pubmed.ncbi.nlm.nih.gov/29427797/) | Tinea pedis, varicose veins, lymphoedema, obesity; incidence 204.8/100k | Human, population case-control |
| [23635049](https://pubmed.ncbi.nlm.nih.gov/23635049/) | PATCH I: penicillin HR 0.55 | Human RCT |
| [21910701](https://pubmed.ncbi.nlm.nih.gov/21910701/) | PATCH II: HR 0.53 (NS) | Human RCT |
| [24551029](https://pubmed.ncbi.nlm.nih.gov/24551029/) | Pooled IRR 0.71; cost-effective | Human, economic analysis |
| [28631307](https://pubmed.ncbi.nlm.nih.gov/28631307/) | Cochrane: prophylaxis reduces recurrence on-treatment | Systematic review |
| [41562377](https://pubmed.ncbi.nlm.nih.gov/41562377/) | 98.3% penicillin response ≤2 days | Human, retrospective |
| [30685804](https://pubmed.ncbi.nlm.nih.gov/30685804/) | Guideline adherence improves outcomes | Human, cohort |
| [28768452](https://pubmed.ncbi.nlm.nih.gov/28768452/) | 75% BHS, penicillin cure in facial disease | Human, prospective |
| [40542699](https://pubmed.ncbi.nlm.nih.gov/40542699/) | 82%→100% subclinical lymphedema | Human, imaging |
| [33413190](https://pubmed.ncbi.nlm.nih.gov/33413190/) | Recurrence risk factors | Human, prospective cohort |
| [30976336](https://pubmed.ncbi.nlm.nih.gov/30976336/) | Comorbidities in recurrence | Human, cohort |
| [20147345](https://pubmed.ncbi.nlm.nih.gov/20147345/) | Age/sex/comorbidity epidemiology (n=428) | Human, cohort |
| [15822466](https://pubmed.ncbi.nlm.nih.gov/15822466/) | Leg 91%, toe-web portal 77% (n=647) | Human, retrospective |
| [18069381](https://pubmed.ncbi.nlm.nih.gov/18069381/) | Recurrence 67%, complications 25% | Human, retrospective |
| [19663854](https://pubmed.ncbi.nlm.nih.gov/19663854/) | Erysipeloid definition | Review |
| [42687202](https://pubmed.ncbi.nlm.nih.gov/42687202/) | Pig reservoir for *Erysipelothrix* | Veterinary |
| [39240378](https://pubmed.ncbi.nlm.nih.gov/39240378/) | Antibiotic network meta-analysis | Systematic review |
| [27806170](https://pubmed.ncbi.nlm.nih.gov/27806170/) | Misdiagnosis cost/harm | Human, cross-sectional |

**Consistency:** All etiologic sources converge on β-hemolytic streptococcal predominance; all risk-factor studies converge on barrier breach + edema/lymphedema + obesity; both RCTs and the Cochrane review agree on prophylaxis benefit with post-treatment waning. No reviewed study contradicted the core model.

---

## Limitations and Knowledge Gaps

1. **Etiologic uncertainty at the bedside:** blood/wound cultures are low-yield (bacteremia ~6.9%); much etiologic attribution is serologic or presumptive, and *S. aureus* isolates may be colonizers rather than pathogens.
2. **Erysipelas vs cellulitis overlap:** many studies pool the two entities; findings are partly extrapolated across the boundary.
3. **No molecular/host-genetic layer:** because erysipelas is non-genetic, entire template sections (causal genes, variants, inheritance, pharmacogenomics) are not applicable — a structural mismatch with a genetics-oriented template, not a gap in the literature.
4. **Prophylaxis durability:** benefit reverses off-treatment; optimal duration and the role of combined risk-factor modification are not fully defined.
5. **QoL data** specific to erysipelas are sparse; no validated disease-specific instrument was identified.
6. **Model systems** capture bacterial virulence but not the chronic lymphedema/recurrence cycle.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective interventional trial** combining tinea pedis eradication + compression lymphedema therapy vs standard care to quantify reduction in first and recurrent episodes (targets the highest-attributable, modifiable factors).
2. **Biomarker study** correlating baseline lymphoscintigraphy and CRP kinetics with recurrence, to risk-stratify candidates for prophylaxis.
3. **Comparative-effectiveness / duration study** of penicillin prophylaxis (e.g., 12 vs 24 months, continuous vs intermittent) with off-treatment follow-up to address waning.
4. **Curation action:** ensure the knowledge base cleanly separates MONDO:0001266 (streptococcal erysipelas) from *Erysipelothrix* erysipeloid/swine erysipelas to prevent conflation.
5. **Diagnostic stewardship:** deploy/validate clinical decision tools to reduce pseudocellulitis misdiagnosis and unnecessary antibiotic use.

---

*Report compiled from 5 discovery iterations, 8 confirmed findings, and 44 reviewed papers. Evidence is predominantly human clinical (cohort, case-control, RCT, systematic review), supplemented by murine pathogen-virulence models and veterinary/zoonotic sources for the nosological distinction.*


## Artifacts

- [OpenScientist final report](Erysipelas-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Erysipelas-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc2.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 38 |
| On topic | 11 |
| Off topic | 3 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:11801184` (5 mentions) - Mouse skin passage of a Streptococcus pyogenes Tn917 mutant of sagA/pel restores virulence, beta-hemolysis and sagA/pel expression without altering the position or sequence of the transposon.
  - shared terms: streptococcal
- `PMID:27806170` (4 mentions) - Costs and Consequences Associated With Misdiagnosed Lower Extremity Cellulitis.
  - shared terms: antibiotic, cellulitis
- `PMID:30542523` (3 mentions) - Aortic valve endocarditis with Erysipelothrix rhusiopathiae: A rare zoonosis.
  - shared terms: human

Weighed against this report's own most characteristic terms: `erysipelas`, `disease`, `lymphedema`, `recurrence`, `edema`, `streptococcal`, `penicillin`, `obesity`, `clinical`, `portal`, `episode`, `human`, `prophylaxis`, `tinea`, `antibiotic`, `cohort`, `lymphatic`, `cellulitis`, `fever`, `pedis`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 9 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0001266` (4 mentions) - the report calls it "streptococcal erysipelas"; MONDO calls it **erysipelas**
- `NCBITaxon:119602` (2 mentions) - the report calls it "equisimilis"; NCBITaxon calls it **Streptococcus dysgalactiae subsp. equisimilis**, and lists "Streptococcus equisimilis" among its other names
- `HP:0001974` (1 mention) - the report calls it "Leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names

Every term resolved, and every label the report gave matched.