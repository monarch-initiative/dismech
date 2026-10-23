---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T15:55:40.240479'
end_time: '2026-09-25T16:10:22.512676'
duration_seconds: 882.27
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chronic Canaliculitis
  mondo_id: MONDO:0004924
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
citation_count: 34
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 34
  on_topic: 27
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 20
  verified: 20
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 12
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCIT:C15329
    reported_labels:
    - Antibiotic Therapy
    ontology_label: Surgical Procedure
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Chronic_Canaliculitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Chronic_Canaliculitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chronic Canaliculitis
- **MONDO ID:** MONDO:0004924 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Chronic Canaliculitis** covering all of the
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

# Chronic Canaliculitis (MONDO:0004924): A Comprehensive Disease Characteristics Report

## Summary

**Chronic canaliculitis is an uncommon, indolent, acquired infection of the lacrimal canaliculus—the small epithelial-lined channel that drains tears from the eyelid margin toward the lacrimal sac.** It is caused predominantly by the filamentous, Gram-positive anaerobe *Actinomyces* (frequently in polymicrobial combination), which aggregates within the canalicular lumen to form calcified concretions ("canaliculiths") and biofilm. The disease manifests as chronic epiphora (tearing), mucopurulent discharge, a red and "pouting" lacrimal punctum, and medial eyelid inflammation. It is overwhelmingly a disease of **middle-aged and elderly women**, is almost always **unilateral**, and most often affects the **lower canaliculus**. Because its signs mimic more common conditions, it is **frequently and repeatedly misdiagnosed** as bacterial/viral conjunctivitis, chronic dacryocystitis, or chalazion, producing diagnostic delays that commonly reach 10–30 months.

Mechanistically, the disease is not genetic. It arises from a self-perpetuating cycle of **tear stasis → organism colonization → intracanalicular concretion/biofilm formation → chronic mucosal inflammation → further stasis and occlusion**. Age-related involutional changes of the drainage system (punctal atrophy, canalicular fibrosis), dry-eye disease, an odontogenic *Actinomyces* reservoir, and iatrogenic punctal/canalicular plugs used to treat dry eye are the principal predisposing/risk factors. There are no established causal genes, no inheritance, no animal models, and no omics/biomarker datasets specific to this disease—reflecting its status as a localized, acquired, infectious/inflammatory condition rather than a Mendelian or systemic disorder.

Prognosis is **excellent once the concretions are physically removed.** Definitive treatment is canaliculotomy with curettage of concretions, with reported cure rates of ~92–98%, further improved by adjunctive silicone tube intubation and punctum-sparing techniques. Conservative, incision-sparing management (punctal dilation, manual expression, microcurettage, and antibiotic canalicular irrigation) is an effective first-line alternative in selected cases (~83% success). There is no disease-specific mortality; morbidity is limited to local discomfort, recurrent infection, and—if untreated—canalicular dilatation and stenosis. The most important diagnostic principle is clinical vigilance: recognizing the "pouting punctum" and canalicular discharge, supported by high-frequency ultrasound biomicroscopy showing intraluminal concretions, and confirming with expression/curettage plus microbiology/histopathology (which also excludes the rare masquerade of canalicular carcinoma).

---

## 1. Disease Information

**Overview.** Chronic canaliculitis is a chronic, low-grade infection/inflammation of the lacrimal canaliculus. The canaliculi are the initial, epithelial-lined segments of the lacrimal drainage system beginning at the punctum on each eyelid margin. Primary (or "primary chronic") canaliculitis denotes intrinsic infection of the canaliculus, typically associated with concretions; secondary canaliculitis denotes infection provoked by a retained foreign body, most notably a punctal/canalicular plug. The condition is characterized by its indolent course, its tendency to form intraluminal concretions, and its notoriety for misdiagnosis.

> *"Primary chronic canaliculitis is an uncommon disease, which is often misdiagnosed and insufficiently treated."* — [PMID: 15764110](https://pubmed.ncbi.nlm.nih.gov/15764110/)

> *"Primary lacrimal canaliculitis (PLC) is a unique disorder which often gets misdiagnosed by the general as well as speciality-trained ophthalmologists."* — [PMID: 29564416](https://pubmed.ncbi.nlm.nih.gov/29564416/)

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0004924 (canaliculitis) |
| ICD-10 | H04.3 (acute and unspecified inflammation of lacrimal passages); H04.4 (chronic inflammation of lacrimal passages) |
| ICD-11 | 9A27.1 (inflammation of lacrimal passages / canaliculitis) |
| MeSH | Lacrimal Apparatus Diseases (canaliculitis indexed under lacrimal apparatus disease terms) |
| OMIM | Not applicable (no Mendelian entry — acquired infectious disease) |
| Orphanet | Not a listed rare Mendelian disorder |
| SNOMED CT | Canaliculitis (disorder) |

**Synonyms / alternative names.** Lacrimal canaliculitis; primary canaliculitis; primary chronic canaliculitis (PCC); primary lacrimal canaliculitis (PLC); suppurative canaliculitis; chronic suppurative canaliculitis; Actinomycotic canaliculitis (when *Actinomyces* is confirmed). A clinically overlapping but distinct entity is "idiopathic canalicular inflammatory disease" ([PMID: 29373404](https://pubmed.ncbi.nlm.nih.gov/29373404/)).

**Source of information.** The knowledge base for this disease is derived overwhelmingly from **aggregated disease-level resources**—retrospective single-center and multicenter case series and case reports—rather than large EHR cohorts or population registries. This reflects its rarity. The largest series comprise tens to a few hundred patients (e.g., 74, 201, 338 cases).

---

## 2. Etiology

**Primary causal factors.** Chronic canaliculitis is an **infectious/inflammatory acquired disease**, not a genetic one. The dominant causal organism is *Actinomyces israelii* and related *Actinomyces* species—filamentous, Gram-positive, cast-forming anaerobes that aggregate to form canalicular concretions. The infection is frequently **polymicrobial**.

> *"Histological examination identified Actinomyces species in 11 of 15 concretions (73%; 95% confidence interval, Wilson method: 48 - 89%), supporting their leading role as causative organisms of canaliculitis."* — [PMID: 41702562](https://pubmed.ncbi.nlm.nih.gov/41702562/)

**Risk factors — environmental / acquired.**
- **Age** (older adults; mean ages 48–66 y across series) and **female sex** are the strongest demographic risk factors.
- **Dry-eye disease** is a major predisposing factor, both directly (reduced tear clearance/flushing) and indirectly (leading to plug insertion).
- **Punctal/canalicular plugs** inserted for dry eye are a key **iatrogenic** risk factor for secondary canaliculitis.

> *"Dry eye was identified in the vast majority of patients with Actinomycotic canaliculitis. Most cases are odontogenic in origin and the infection occurs in immunocompetent individuals."* — [PMID: 36927124](https://pubmed.ncbi.nlm.nih.gov/36927124/)

- **Odontogenic reservoir:** *Actinomyces* is part of normal oral/periodontal flora; an odontogenic source is common.
- **Involutional anatomical changes:** punctal atrophy, canalicular fibrosis, and nasolacrimal duct stenosis promote tear stagnation ([PMID: 42366665](https://pubmed.ncbi.nlm.nih.gov/42366665/)).

**Genetic risk factors.** None established. No susceptibility loci, modifier genes, or GWAS associations exist for this localized acquired infection.

**Protective factors.** No genetic protective variants are known. Environmentally, adequate tear drainage, avoidance/early removal of punctal plugs, and good oral/periodontal hygiene are logical (though not formally studied) protective measures. Hosts are typically **immunocompetent**, so immune status is not a strong determinant for primary disease (in contrast to fungal cases).

**Gene–environment interactions.** Not applicable — no genetic contribution has been identified.

---

## 3. Phenotypes

Chronic canaliculitis presents with a characteristic cluster of **symptoms and clinical signs** (not laboratory or behavioral abnormalities). The proposed diagnostic **"clinical tetrad"** captures the core phenotype:

> *"We propose a 'clinical tetrad' of 1. medial eyelid edema, 2. pouting and hyperemia of lacrimal punctum, 3. yellowish canalicular hue and, 4. canalicular distention, and expressible discharge, for the easier clinical diagnosis of LC."* — [PMID: 36644466](https://pubmed.ncbi.nlm.nih.gov/36644466/)

| Phenotype | Type | Frequency | HPO suggestion |
|---|---|---|---|
| Epiphora (excessive tearing) | Symptom | ~85–90% (63/74; 90.5% in canaliculoplasty series) | HP:0009926 (Epiphora) |
| Mucopurulent discharge from punctum | Sign | ~85% (85.7%) | Ocular discharge |
| Pouting/hyperemic punctum | Sign | Highly characteristic (tetrad component) | — |
| Medial eyelid/canthal edema | Sign | Common (tetrad component) | HP:0000534 (Abnormal eyelid morphology, broad) |
| Canalicular concretions (canaliculiths) | Physical manifestation | Large majority (15/17; 37/37) | — |
| Canalicular distention/dilatation | Sign | Subset (severe/long-standing) | — |
| Redness/irritation (mimics conjunctivitis) | Symptom/sign | Common | HP:0000509 (Conjunctivitis) |

> *"The most common presenting symptom was epiphora, noted in 63 (85%) patients"* — [PMID: 22836798](https://pubmed.ncbi.nlm.nih.gov/22836798/)

**Phenotype characteristics.**
- **Age of onset:** adult-onset, typically middle-aged to geriatric (mean 48–66 y). Pediatric onset is *extremely rare* ([PMID: 31055896](https://pubmed.ncbi.nlm.nih.gov/31055896/)).
- **Severity:** mild-to-moderate and localized; rarely sight-threatening.
- **Progression:** chronic, indolent, episodic/recurrent; can progress to canalicular dilatation and stenosis if untreated.
- **Frequency among affected individuals:** epiphora and discharge are near-universal; concretions are present in the large majority.

**Quality-of-life impact.** Chronic tearing, recurrent discharge, and repeated ineffective treatment (often over months to years) impose meaningful ocular-surface discomfort and repeated clinic visits, but the disease does not threaten vision or life. No disease-specific EQ-5D/SF-36 data exist.

---

## 4. Genetic / Molecular Information

**Not applicable.** Chronic canaliculitis is an acquired infectious disease with **no causal genes, no pathogenic germline or somatic variants, no modifier genes, no epigenetic signatures, and no chromosomal abnormalities.** There are no OMIM, ClinVar, HGMD, or gnomAD entries relevant to disease causation. Reports of neoplasia (plasmacytoma, carcinoma) associated with or masquerading as canaliculitis are coincidental mass lesions, not a genetic basis for canaliculitis itself ([PMID: 21743365](https://pubmed.ncbi.nlm.nih.gov/21743365/); [PMID: 16534063](https://pubmed.ncbi.nlm.nih.gov/16534063/)).

---

## 5. Environmental Information

**Environmental factors.** The relevant "environmental" exposures are microbiological and iatrogenic rather than chemical/toxic:
- **Iatrogenic foreign bodies:** punctal and intracanalicular plugs (e.g., SmartPLUG) used for dry-eye management. Plug-related canaliculitis represented **18.3%** of all canaliculitis cases in one series; all affected patients were female with prior plug insertion.

> *"Cultures of discharge, concretions, and/or infected plugs mostly revealed Pseudomonas aeruginosa (42%)."* — [PMID: 34139956](https://pubmed.ncbi.nlm.nih.gov/34139956/)

**Lifestyle factors.** Poor oral/periodontal hygiene plausibly contributes via the odontogenic *Actinomyces* reservoir, though this is inferential.

**Infectious agents (the core etiology).**

| Category | Key organisms | Evidence |
|---|---|---|
| Bacteria (dominant) | *Actinomyces israelii/*spp. (leading), *Staphylococcus* spp. (39% most common culture isolate), *Streptococcus* spp., *Nocardia* spp., polymicrobial anaerobes | [PMID: 41702562](https://pubmed.ncbi.nlm.nih.gov/41702562/); [PMID: 22836798](https://pubmed.ncbi.nlm.nih.gov/22836798/); [PMID: 34287258](https://pubmed.ncbi.nlm.nih.gov/34287258/) |
| Bacteria (plug-related) | *Pseudomonas aeruginosa* (42%) | [PMID: 34139956](https://pubmed.ncbi.nlm.nih.gov/34139956/) |
| Rare/novel bacteria | *Arcanobacterium haemolyticum*, *Tsukamurella* spp., *Ottowia massiliensis*, *Fusobacterium periodonticum* | [PMID: 15764110](https://pubmed.ncbi.nlm.nih.gov/15764110/); [PMID: 31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/); [PMID: 40234845](https://pubmed.ncbi.nlm.nih.gov/40234845/); [PMID: 41429755](https://pubmed.ncbi.nlm.nih.gov/41429755/) |
| Fungi | *Candida* (27.1%), *Aspergillus* (23.7%), *Scedosporium* (novel) | [PMID: 42782278](https://pubmed.ncbi.nlm.nih.gov/42782278/); [PMID: 40788664](https://pubmed.ncbi.nlm.nih.gov/40788664/) |
| Viruses | HSV (83.1% of viral cases), VZV | [PMID: 41528827](https://pubmed.ncbi.nlm.nih.gov/41528827/); [PMID: 29426966](https://pubmed.ncbi.nlm.nih.gov/29426966/) |

> *"The most commonly reported species were Candida (27.1%) and Aspergillus (23.7%)."* — [PMID: 42782278](https://pubmed.ncbi.nlm.nih.gov/42782278/)

> *"The majority of viral lacrimal drainage infections were secondary to herpes simplex virus (HSV) (83.1%, 378/455)"* — [PMID: 41528827](https://pubmed.ncbi.nlm.nih.gov/41528827/)

**Suggested NCBITaxon anchors:** *Actinomyces israelii* (NCBITaxon:1659); *Pseudomonas aeruginosa* (NCBITaxon:287); *Candida albicans* (NCBITaxon:5476); *Human alphaherpesvirus 1* (NCBITaxon:10298).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Predisposing anatomical/physiological change** (age-related punctal atrophy, canalicular fibrosis, dry eye, or an inserted punctal plug) **leads to** reduced tear flow and **tear stasis** within the canaliculus.
2. Tear stasis **results in** colonization of the canalicular lumen by resident/odontogenic organisms, chiefly *Actinomyces* (often with co-pathogens).
3. Colonizing filamentous organisms **aggregate and mineralize**, which **leads to** formation of intracanalicular **concretions (canaliculiths) and biofilm**. *(Demonstrated: concretions present in the large majority of cases and shown histologically to contain aggregated Actinomyces/anaerobes.)*
4. The concretion/biofilm **results in** a protected microbial niche that resists topical antibiotics and **sustains chronic mucosal inflammation** of the canalicular epithelium.
5. Chronic inflammation **leads to** the clinical phenotype: pouting hyperemic punctum, mucopurulent discharge, medial eyelid edema, and epiphora.
6. Persistent inflammation **further results in** post-inflammatory sequelae—canalicular dilatation and, ultimately, **fibrosis/stenosis**—which worsen stasis and **feed back** to step 2, closing a self-perpetuating loop. *(Branch: if a foreign body/plug is present, it substitutes for steps 1–3 as the nidus.)*

> *"Lacrimal infection is a vicious circle, in which infection leads to inflammation and post-inflammatory sequelae, themselves a source of occlusion and stagnation, which in turn encourages infection."* — [PMID: 39488146](https://pubmed.ncbi.nlm.nih.gov/39488146/)

```
Dry eye / aging / punctal plug
        │  (reduced tear clearance)
        ▼
   TEAR STASIS ───────────────┐
        │                      │ feedback
        ▼                      │
 Actinomyces (± co-pathogens)  │
 colonize canalicular lumen    │
        │                      │
        ▼                      │
 CONCRETION / BIOFILM  ────────┘
   (protected niche)
        │
        ▼
 CHRONIC MUCOSAL INFLAMMATION
        │
        ├──► pouting punctum, discharge, epiphora  (clinical disease)
        │
        └──► canalicular dilatation → fibrosis/stenosis (sequelae)
```

**Cellular processes & immune involvement.** The core process is **chronic infection-driven inflammation** (GO:0006954, inflammatory response; GO:0006935, chemotaxis of neutrophils) of the **canalicular epithelium**, with mixed suppurative/granulomatous features histologically and no autoimmune basis (collagen-vascular/autoimmune screens negative in the related idiopathic entity). Hosts are typically immunocompetent for bacterial disease; immunosuppression is relevant chiefly for fungal cases.

**Biofilm formation** (GO:0042710) is the pivotal cellular-community process explaining chronicity and antibiotic tolerance. **Concretion mineralization** represents biomineral aggregation of filamentous organisms.

**Molecular pathways / metabolic changes / protein dysfunction.** No specific host signaling cascade (Wnt, MAPK, mTOR, PI3K-AKT), enzyme deficiency, metabolic derangement, or protein misfolding is implicated—consistent with an acquired, localized infection rather than a molecular-genetic disease.

**Molecular profiling.** No transcriptomic, proteomic, metabolomic, or lipidomic disease signatures exist. The only "omics" applied is **metagenomic shotgun sequencing of concretions** for pathogen identification, which detected bacteria (predominantly anaerobes) in all sampled concretions ([PMID: 34287258](https://pubmed.ncbi.nlm.nih.gov/34287258/)).

**Suggested ontology terms.** Biological processes: GO:0006954 (inflammatory response), GO:0042710 (biofilm formation), GO:0009617 (response to bacterium). Cell types: CL:0000066 (epithelial cell) of the canalicular lining; CL:0000775 (neutrophil). Anatomy: UBERON:0002392 (lacrimal canaliculus).

---

## 7. Anatomical Structures Affected

**Organ / system level.** Primary organ: the **lacrimal drainage apparatus**, specifically the **lacrimal canaliculus** (UBERON:0002392). Body system: the ocular adnexa / lacrimal (nasolacrimal) drainage system of the visual system. Secondary involvement: the lacrimal sac and nasolacrimal duct can be secondarily affected in advanced or overlapping disease (dacryocystitis differential).

**Localization and laterality.** The **lower (inferior) canaliculus** is most often affected, and disease is overwhelmingly **unilateral**.

> *"Lower canaliculus was involved in 48 (65%) patients, upper canaliculus in 17 (23%) patients, and both canaliculi in 9 (12%) patients."* — [PMID: 22836798](https://pubmed.ncbi.nlm.nih.gov/22836798/)

**Tissue / cell level.** The affected tissue is the **epithelial lining of the canaliculus** (stratified/columnar epithelium) and adjacent subepithelial stroma, with inflammatory cell infiltration. Concretions occupy the lumen.

**Subcellular level.** No specific organelle/compartment pathology; suggested GO cellular component anchors are extracellular (biofilm matrix; GO:0005576, extracellular region) rather than intracellular.

**Suggested ontology terms.** UBERON:0002392 (lacrimal canaliculus); UBERON:0001817 (lacrimal apparatus); UBERON:0000970 (eye, broad); CL:0000066 (epithelial cell).

---

## 8. Temporal Development

**Onset.** Adult-onset, insidious, and **chronic**. Mean age at presentation ranges 48–66 years; pediatric onset is extremely rare.

> *"It is extremely rare in children and infants."* — [PMID: 31055896](https://pubmed.ncbi.nlm.nih.gov/31055896/)

**Progression and course.** The disease is chronic, indolent, and episodic/recurrent. Diagnostic delay is a hallmark, with mean time-to-diagnosis of ~10 months in one series and **30.6 ± 39.5 months** in a canaliculoplasty series of long-standing disease. Untreated disease can progress from mucosal inflammation to **canalicular dilatation** and ultimately **stenosis/obstruction**.

**Disease stages (as described for the related idiopathic canalicular inflammatory disease, staged 1–5):** edema → progressive centripetal vascularization → pouting of vascularized mucosa → membrane formation → progressive scarring ([PMID: 29373404](https://pubmed.ncbi.nlm.nih.gov/29373404/)). Classic infectious chronic canaliculitis does not have a formal universally adopted staging system.

**Remission / critical periods.** Remission is **treatment-induced** (concretion removal), not spontaneous—residual concretions perpetuate disease. The therapeutic "critical window" is the point of definitive concretion removal before irreversible fibrosis/stenosis develops.

**Duration.** Chronic and persistent until definitively treated; not self-limited.

---

## 9. Inheritance and Population

**Epidemiology.** Chronic canaliculitis is a **rare** lacrimal disorder (historically cited as ~2% of lacrimal disease). Precise population incidence/prevalence figures are not established due to under-recognition and misdiagnosis. Among **primary** canaliculitis, *Actinomyces* accounts for roughly 11% of cases (22/201).

> *"Of the 201 patients diagnosed with primary canaliculitis, 22 (10.9%) were caused by [Actinomyces]"* — [PMID: 36927124](https://pubmed.ncbi.nlm.nih.gov/36927124/)

**Inheritance.** **Not applicable** — acquired infectious disease with no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency.

**Population demographics.**
- **Sex ratio:** female predominance is consistent and often marked—54% female in the largest primary series, rising to 77–83% in others; plug-related cases are essentially all female.
- **Age distribution:** middle-aged to elderly.

> *"Of the 74 patients, 40 (54%) were women. Mean age at presentation was 48 years."* — [PMID: 22836798](https://pubmed.ncbi.nlm.nih.gov/22836798/)

- **Geographic distribution:** worldwide; case series originate from Asia, Europe, North America, and elsewhere, with no strong endemic clustering. No variant geography (no variants).

---

## 10. Diagnostics

**Diagnosis is fundamentally clinical**, confirmed by expression/curettage of concretions with microbiology and histopathology.

**Clinical signs / criteria.** The **"clinical tetrad"** (medial eyelid edema; pouting/hyperemic punctum; yellowish canalicular hue; canalicular distention with expressible discharge) enables bedside diagnosis ([PMID: 36644466](https://pubmed.ncbi.nlm.nih.gov/36644466/)). Expression of concretions/discharge from the punctum is essentially pathognomonic.

**Imaging.** High-frequency (80-MHz) **ultrasound biomicroscopy (UBM)**, optionally combined with color Doppler flow imaging, demonstrates luminal ectasia with a high-echo intraluminal mass (calculi) and uneven mucosal thickening.

> *"Lacrimal canaliculitis (vertical section) showed obvious ectasia of the lacrimal canalicular lumen, with a high echo mass shadow, which might have been calculi"* — [PMID: 31823059](https://pubmed.ncbi.nlm.nih.gov/31823059/)

Adjunctive tools include **dacryoendoscopy** and Fourier-domain OCT (used in the idiopathic inflammatory variant).

**Microbiology / pathology.** Culture (aerobic + anaerobic), Gram stain, and histopathology of curetted concretions establish the organism; *Actinomyces* appears as sulfur-granule-like filamentous colonies. **Metagenomic/next-generation sequencing** can identify fastidious or unculturable pathogens directly from concretions.

> *"Sequencing analysis detected bacteria in all samples"* — [PMID: 34287258](https://pubmed.ncbi.nlm.nih.gov/34287258/)

**Genetic / omics testing.** Not applicable for diagnosis (no genetic basis; no validated biomarkers). Molecular testing is limited to pathogen identification (16S rDNA sequencing, PCR for viral cases).

**Differential diagnosis (critical).** Chronic dacryocystitis, chalazion/hordeolum, and conjunctivitis are the leading mimics; rare masquerades include canalicular carcinoma and plasmacytoma. Histopathology of excised tissue is important in atypical/refractory cases.

> *"A history of chronic redness, watering, discharge, and medial canthal region edema lead to the misdiagnosis of chronic dacryocystitis in 3 (60%) and medial marginal chalazion in 2 (40%) cases."* — [PMID: 29564416](https://pubmed.ncbi.nlm.nih.gov/29564416/)

> *"Carcinoma of the lacrimal canaliculus masquerading as canaliculitis"* — [PMID: 16534063](https://pubmed.ncbi.nlm.nih.gov/16534063/)

**Screening.** No population/newborn/carrier screening applies (acquired, non-genetic, rare).

---

## 11. Outcome / Prognosis

**Prognosis is excellent once concretions are removed.** There is **no disease-specific mortality** and no threat to life; morbidity is local.

| Outcome metric | Value | Source |
|---|---|---|
| Cure by canaliculotomy (large dacryolithiasis series) | 297/302 = 98.34% | [PMID: 40067167](https://pubmed.ncbi.nlm.nih.gov/40067167/) |
| Recurrence-free at 3.7 y (canaliculotomy + silicone tube) | 88% | [PMID: 36431305](https://pubmed.ncbi.nlm.nih.gov/36431305/) |
| Complete remission (canaliculoplasty for dilated canaliculus) | 33/42 = 78.6% | [PMID: 32563241](https://pubmed.ncbi.nlm.nih.gov/32563241/) |
| Success, incision-sparing management | 10/12 = 83.3% | [PMID: 28576205](https://pubmed.ncbi.nlm.nih.gov/28576205/) |

> *"Of 302 cases (89.35%) with canaliculitis, 297 (98.34%) were cured with canaliculotomy"* — [PMID: 40067167](https://pubmed.ncbi.nlm.nih.gov/40067167/)

**Complications.** Recurrent/persistent infection if concretions are incompletely removed; canalicular dilatation; **canalicular stenosis/obstruction** (a recognized post-surgical and post-inflammatory complication—3 patients developed stenosis in the canaliculoplasty series). Punctum-damaging surgery risks punctal deformity, motivating punctum-sparing techniques.

**Prognostic factors.** Completeness of concretion removal is the dominant prognostic determinant. Long-standing disease with canalicular dilatation is a more severe phenotype. No molecular prognostic biomarkers exist.

**Quality of life / disability.** Limited to chronic ocular-surface discomfort and epiphora; no formal QoL instrument data. Full functional recovery is expected after definitive treatment.

---

## 12. Treatment

Treatment aims to **eradicate the microbial nidus by physically removing concretions**, since topical antibiotics alone frequently fail to penetrate the biofilm/concretion.

### Tiered treatment strategy

**1. Conservative / incision-sparing (first-line in selected cases):** punctal dilation, manual expression/massage of concretions, microcurettage, and **canalicular irrigation with susceptible antibiotics** (e.g., fortified cefazolin, ciprofloxacin).

> *"Ten (83.3%) eyes were successfully treated with incision-sparing modalities, and 2 (16.7%) eyes were treated surgically. No recurrences were observed"* — [PMID: 28576205](https://pubmed.ncbi.nlm.nih.gov/28576205/)

> *"The conservative method combining canalicular expression and irrigation with topical susceptible antibiotics is recommendable as initial therapy."* — [PMID: 36927124](https://pubmed.ncbi.nlm.nih.gov/36927124/)

Intracanalicular antibiotics can obviate surgery in some suppurative cases ([PMID: 18580001](https://pubmed.ncbi.nlm.nih.gov/18580001/)).

**2. Definitive surgery — canaliculotomy with curettage:** the mainstay for refractory/recurrent disease, with cure rates ~92–98%.

**3. Adjuncts improving outcomes:**
- **Silicone tube intubation** improves anatomical/functional success and long-term recurrence-free rates.

> *"a higher success rate can be achieved when silicone tube intubation is performed during the procedure"* — [PMID: 34275398](https://pubmed.ncbi.nlm.nih.gov/34275398/)

> *"After a follow-up time of 3.7 ± 1.5 years, 88% of cases showed no recurrence of inflammation."* — [PMID: 36431305](https://pubmed.ncbi.nlm.nih.gov/36431305/)

- **Punctum-sparing / mini-invasive canaliculotomy** preserves punctal function with high success (anatomic 96–98%, functional 91–94%) and no recurrences ([PMID: 36473974](https://pubmed.ncbi.nlm.nih.gov/36473974/); [PMID: 37300269](https://pubmed.ncbi.nlm.nih.gov/37300269/); [PMID: 42530488](https://pubmed.ncbi.nlm.nih.gov/42530488/)).
- **Canaliculoplasty with stenting** for the severe dilated-canaliculus phenotype ([PMID: 32563241](https://pubmed.ncbi.nlm.nih.gov/32563241/)).

**4. Pathogen-directed antimicrobials:** systemic/topical penicillin for *Actinomyces*; topical/systemic **azoles/voriconazole** for fungal (e.g., *Scedosporium*, *Candida*, *Aspergillus*) cases; topical **acyclovir** for HSV/VZV canaliculitis; plug removal for secondary/plug-related disease.

**5. Secondary (plug-related) canaliculitis:** remove the offending plug (office irrigation, retrograde massage, or canaliculotomy); DCR may be needed if obstruction persists ([PMID: 16920195](https://pubmed.ncbi.nlm.nih.gov/16920195/)).

**Suggested NCIT anchors:** NCIT:C15329 (Antibiotic Therapy); surgical canaliculotomy (ophthalmologic surgical procedure); Voriconazole; Acyclovir.

**Pharmacogenomics / advanced therapeutics (gene, cell, RNA, targeted, immuno-therapy):** Not applicable.

---

## 13. Prevention

- **Primary prevention:** manage dry eye without unnecessary permanent plugs; judicious plug selection and monitoring; good oral/periodontal hygiene to limit the *Actinomyces* reservoir. These are logical but not formally trialed.
- **Secondary prevention:** early recognition of the clinical tetrad to avoid diagnostic delay; prompt removal of retained plugs at first sign of inflammation.
- **Tertiary prevention:** complete concretion removal and adjunctive intubation to prevent recurrence and canalicular stenosis.
- **Immunization, genetic screening/counseling, public-health/environmental interventions, prophylactic medication:** Not applicable.

---

## 14. Other Species / Natural Disease

**Not applicable / not reported.** Chronic canaliculitis as described here is a human disease of the lacrimal drainage apparatus. There is no established naturally occurring counterpart catalogued in veterinary resources (OMIA) for this specific entity, no breed predisposition, no orthologous causal gene (there is no causal gene), and no zoonotic transmission. *Actinomyces* and related organisms exist across species, but canalicular concretion disease is not a recognized comparative-pathology entity in the reviewed literature.

**Suggested taxonomy anchor for the host:** *Homo sapiens* (NCBITaxon:9606).

---

## 15. Model Organisms

**None exist.** There are no mouse, rat, zebrafish, invertebrate, cellular, organoid, or iPSC models of chronic canaliculitis in the reviewed literature. This absence reflects the disease's nature as a localized, acquired human infection driven by concretion/biofilm formation—features not readily recapitulated in standard genetic model systems. Consequently there is no phenotype-recapitulation or model-limitation data to report, and no model databases (MGI, RGD, ZFIN, etc.) hold relevant entries. This is a clear knowledge gap: an in vitro **biofilm/concretion model** using canalicular epithelial cells co-cultured with *Actinomyces* would be a logical future development.

---

## Key Findings (Consolidated with Evidence)

### Finding 1 — A rare, misdiagnosed infection with female predominance and older-adult onset
Across the largest primary-canaliculitis series (74 patients), 54% were women, mean age 48 years, epiphora was the leading symptom (85%), the lower canaliculus was involved in 65%, and the mean diagnostic delay was ~10 months; other series report even higher female predominance (77–83%) and older mean ages (57–63 y). Misdiagnosis is the rule rather than the exception. *(Evidence: [PMID: 22836798](https://pubmed.ncbi.nlm.nih.gov/22836798/), [PMID: 29564416](https://pubmed.ncbi.nlm.nih.gov/29564416/))*

### Finding 2 — *Actinomyces* is the leading cause; disease is frequently polymicrobial and concretion-driven
Histology identified *Actinomyces* in 73% (11/15) of concretions and in 8/13 specimens in a separate series, while cultures frequently yield *Staphylococcus* (39%), *Streptococcus*, and *Nocardia*, and metagenomic sequencing shows anaerobe-dominated polymicrobial communities in all sampled concretions. *(Evidence: [PMID: 41702562](https://pubmed.ncbi.nlm.nih.gov/41702562/), [PMID: 22836798](https://pubmed.ncbi.nlm.nih.gov/22836798/), [PMID: 28248874](https://pubmed.ncbi.nlm.nih.gov/28248874/), [PMID: 34287258](https://pubmed.ncbi.nlm.nih.gov/34287258/))*

### Finding 3 — Canaliculotomy with curettage is definitive; adjuncts improve outcomes
Canaliculotomy cured 98.34% of canaliculitis cases in a 302-case dataset; silicone tube intubation raised anatomical/functional success (100%/87.5% vs 78.3%/60.9%); long-term recurrence-free rate was 88% at 3.7 years. *(Evidence: [PMID: 40067167](https://pubmed.ncbi.nlm.nih.gov/40067167/), [PMID: 34275398](https://pubmed.ncbi.nlm.nih.gov/34275398/), [PMID: 36431305](https://pubmed.ncbi.nlm.nih.gov/36431305/))*

### Finding 4 — Broad etiologic spectrum; plugs are a key iatrogenic cause
Plug-related (secondary) canaliculitis constituted 18.3% of cases (all female, *Pseudomonas* dominant, 42%); fungal cases are led by *Candida* (27.1%) and *Aspergillus* (23.7%); viral cases are dominated by HSV (83.1%). *(Evidence: [PMID: 34139956](https://pubmed.ncbi.nlm.nih.gov/34139956/), [PMID: 42782278](https://pubmed.ncbi.nlm.nih.gov/42782278/), [PMID: 41528827](https://pubmed.ncbi.nlm.nih.gov/41528827/))*

### Finding 5 — Diagnosis is clinical (tetrad) plus UBM
The clinical tetrad and 80-MHz UBM (luminal ectasia + high-echo concretion) enable diagnosis; 85% of eyes had been previously misdiagnosed. *(Evidence: [PMID: 36644466](https://pubmed.ncbi.nlm.nih.gov/36644466/), [PMID: 31823059](https://pubmed.ncbi.nlm.nih.gov/31823059/))*

### Finding 6 — Chronic, unilateral, lower-canaliculus, adult disease
Lower canaliculus 65%, upper 23%, both 12%; unilateral and chronic; pediatric onset extremely rare. *(Evidence: [PMID: 22836798](https://pubmed.ncbi.nlm.nih.gov/22836798/), [PMID: 31055896](https://pubmed.ncbi.nlm.nih.gov/31055896/))*

### Finding 7 — Self-perpetuating stasis–colonization–concretion–inflammation cycle
Dry eye and odontogenic *Actinomyces* are key predisposing factors in immunocompetent hosts; involutional anatomical changes drive stasis; infection–inflammation forms a vicious circle. *(Evidence: [PMID: 36927124](https://pubmed.ncbi.nlm.nih.gov/36927124/), [PMID: 39488146](https://pubmed.ncbi.nlm.nih.gov/39488146/), [PMID: 42366665](https://pubmed.ncbi.nlm.nih.gov/42366665/))*

### Finding 8 — Conservative incision-sparing therapy is an effective first-line option
Incision-sparing management succeeded in 83.3% (10/12) with no recurrence; conservative expression + antibiotic irrigation is recommended initial therapy for *Actinomyces* disease. *(Evidence: [PMID: 28576205](https://pubmed.ncbi.nlm.nih.gov/28576205/), [PMID: 36927124](https://pubmed.ncbi.nlm.nih.gov/36927124/), [PMID: 18580001](https://pubmed.ncbi.nlm.nih.gov/18580001/))*

### Finding 9 — Rare disorder with excellent prognosis; watch for carcinoma masquerade
*Actinomyces* accounts for ~11% of primary cases; cure ≥88–98%; no disease-specific mortality; carcinoma can masquerade as canaliculitis, underscoring histopathology in atypical cases. *(Evidence: [PMID: 36927124](https://pubmed.ncbi.nlm.nih.gov/36927124/), [PMID: 29564416](https://pubmed.ncbi.nlm.nih.gov/29564416/), [PMID: 16534063](https://pubmed.ncbi.nlm.nih.gov/16534063/))*

---

## Mechanistic Model / Interpretation

The unifying model is a **biofilm/concretion-centered vicious cycle**. Chronic canaliculitis is best understood not as a simple bacterial infection but as a **niche disease**: age- and dry-eye-related tear stasis permits filamentous *Actinomyces* (often with anaerobic co-pathogens) to colonize and build a mineralized concretion that acts as a protected reservoir. This concretion explains the three most clinically important features of the disease: (1) its **chronicity and recurrence**, (2) its **resistance to topical antibiotics** (poor penetration of the biofilm/calculus), and (3) the **therapeutic imperative of physical removal**—cure tracks with completeness of concretion evacuation, not with antibiotic choice alone. Downstream, unresolved inflammation produces canalicular dilatation and fibrosis/stenosis, which reinforce stasis and close the loop. Secondary (plug-related) disease short-circuits the upstream steps by supplying a ready-made foreign-body nidus.

| Axis | Upstream → Downstream |
|---|---|
| Trigger | Dry eye / aging / plug → tear stasis |
| Microbial | Colonization → concretion/biofilm |
| Host response | Chronic epithelial inflammation → sequelae (dilatation, stenosis) |
| Clinical | Pouting punctum, discharge, epiphora |
| Therapy target | Remove concretion (curettage) ± antibiotics ± intubation |

---

## Evidence Base

| PMID | Contribution | Type |
|---|---|---|
| [22836798](https://pubmed.ncbi.nlm.nih.gov/22836798/) | Largest primary series: demographics, symptoms, localization, microbiology | Human clinical |
| [41702562](https://pubmed.ncbi.nlm.nih.gov/41702562/) | Quantified *Actinomyces* as leading organism (73% of concretions) | Human clinical/histology |
| [28248874](https://pubmed.ncbi.nlm.nih.gov/28248874/) | Concretion series confirming *Actinomyces* histopathology | Human clinical |
| [34287258](https://pubmed.ncbi.nlm.nih.gov/34287258/) | Metagenomic sequencing of concretions; anaerobe predominance | Molecular/clinical |
| [40067167](https://pubmed.ncbi.nlm.nih.gov/40067167/) | 98.34% cure by canaliculotomy (large series) | Human clinical |
| [34275398](https://pubmed.ncbi.nlm.nih.gov/34275398/) | Silicone intubation improves success | Human clinical (comparative) |
| [36431305](https://pubmed.ncbi.nlm.nih.gov/36431305/) | 88% recurrence-free long-term | Human clinical |
| [34139956](https://pubmed.ncbi.nlm.nih.gov/34139956/) | Plug-related canaliculitis; *Pseudomonas* | Human clinical |
| [42782278](https://pubmed.ncbi.nlm.nih.gov/42782278/) | Fungal lacrimal infection spectrum | Review |
| [41528827](https://pubmed.ncbi.nlm.nih.gov/41528827/) | Viral (HSV-dominant) lacrimal infection spectrum | Review |
| [36644466](https://pubmed.ncbi.nlm.nih.gov/36644466/) | Diagnostic clinical tetrad | Human clinical |
| [31823059](https://pubmed.ncbi.nlm.nih.gov/31823059/) | UBM imaging signature | Human clinical/imaging |
| [36927124](https://pubmed.ncbi.nlm.nih.gov/36927124/) | Dry eye + odontogenic *Actinomyces*; conservative therapy | Human clinical |
| [39488146](https://pubmed.ncbi.nlm.nih.gov/39488146/) | Infection–inflammation vicious-circle mechanism | Review |
| [28576205](https://pubmed.ncbi.nlm.nih.gov/28576205/) | Incision-sparing management (83.3%) | Human clinical |
| [16534063](https://pubmed.ncbi.nlm.nih.gov/16534063/) | Carcinoma masquerade — differential caution | Case report |

Additional supporting reports on rare/novel organisms and pediatric disease: [PMID: 15764110](https://pubmed.ncbi.nlm.nih.gov/15764110/), [PMID: 31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/), [PMID: 40234845](https://pubmed.ncbi.nlm.nih.gov/40234845/), [PMID: 41429755](https://pubmed.ncbi.nlm.nih.gov/41429755/), [PMID: 40788664](https://pubmed.ncbi.nlm.nih.gov/40788664/), [PMID: 29426966](https://pubmed.ncbi.nlm.nih.gov/29426966/), [PMID: 31055896](https://pubmed.ncbi.nlm.nih.gov/31055896/), [PMID: 15167737](https://pubmed.ncbi.nlm.nih.gov/15167737/).

---

## Limitations and Knowledge Gaps

1. **Evidence quality:** All data derive from retrospective case series and case reports; there are few randomized trials and no population-based incidence/prevalence estimates. Selection and referral bias toward tertiary dacryology centers is likely.
2. **No molecular/omics profiling:** No transcriptomic, proteomic, metabolomic, or lipidomic disease signatures exist; "omics" is limited to metagenomic pathogen identification.
3. **No genetic architecture:** No causal genes, susceptibility loci, or modifier genes—appropriate for an acquired infection but limiting for knowledge-base fields designed for Mendelian disease.
4. **No animal or in vitro disease models**, precluding mechanistic dissection of concretion formation and biofilm tolerance.
5. **Under-diagnosis:** Chronic misdiagnosis means published cohorts underestimate true burden and skew toward severe/refractory presentations.
6. **Overlap ambiguity:** The boundary between infectious chronic canaliculitis and "idiopathic canalicular inflammatory disease" ([PMID: 29373404](https://pubmed.ncbi.nlm.nih.gov/29373404/)) is incompletely defined.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective multicenter registry** with standardized microbiology (aerobic/anaerobic culture + 16S/metagenomics) to establish true incidence, organism frequencies, and recurrence rates.
2. **Randomized trial** of conservative incision-sparing management vs punctum-sparing canaliculotomy ± silicone intubation, powered for functional success and recurrence.
3. **In vitro biofilm/concretion model** co-culturing canalicular epithelial cells with *Actinomyces* to define mineralization triggers and test anti-biofilm agents.
4. **Concretion "omics"**: shotgun metagenomics + metabolomics of concretions vs healthy lacrimal flora to characterize the pathogenic community and mineral matrix.
5. **Diagnostic pathway intervention study**: measure whether teaching the clinical tetrad + point-of-care UBM reduces diagnostic delay in primary/secondary eye care.
6. **Prospective evaluation of plug safety**: registry of dry-eye patients receiving punctal/canalicular plugs to quantify canaliculitis incidence and identify preventive protocols.
7. **Histopathology mandate in atypical cases** to systematically exclude canalicular carcinoma and other masquerades.

---

*Report compiled from a 5-iteration autonomous investigation; 9 confirmed findings; 42 papers reviewed. Disease category: infectious disease. MONDO:0004924.*


## Artifacts

- [OpenScientist final report](Chronic_Canaliculitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Chronic_Canaliculitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 34 |
| On topic | 27 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 18 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C15329` (1 mention) - the report calls it "Antibiotic Therapy"; NCIT calls it **Surgical Procedure**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0004924` (3 mentions) - the report calls it "canaliculitis"; MONDO calls it **chronic canaliculitis**
- `HP:0000534` (1 mention) - the report calls it "Abnormal eyelid morphology, broad"; HP calls it **Abnormal eyebrow morphology**
- `UBERON:0002392` (3 mentions) - the report calls it "lacrimal canaliculus"; UBERON calls it **nasolacrimal duct**, and lists "lacrimal duct" among its other names
- `UBERON:0001817` (1 mention) - the report calls it "lacrimal apparatus"; UBERON calls it **lacrimal gland**
- `UBERON:0000970` (1 mention) - the report calls it "eye, broad"; UBERON calls it **eye**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0042710` - called "Biofilm formation", "biofilm formation"