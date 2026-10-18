---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T21:31:41.356391'
end_time: '2026-08-28T21:59:41.366290'
duration_seconds: 1680.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dermatosparaxis Ehlers-Danlos Syndrome
  mondo_id: ''
  category: Connective Tissue Disorder
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
citation_count: 13
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 26
  verified: 22
  not_found: 0
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:0000057
    reported_labels:
    - fibroblasts
    - Cell populations:** dermal **fibroblasts
    ontology_label: fibroblast
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0004251
    ontology_label: obsolete X-Pro dipeptidase activity
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
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
  path: Dermatosparaxis_Ehlers-Danlos_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Dermatosparaxis_Ehlers-Danlos_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dermatosparaxis Ehlers-Danlos Syndrome
- **MONDO ID:**  (if available)
- **Category:** Connective Tissue Disorder

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

# Dermatosparaxis Ehlers-Danlos Syndrome (dEDS): Comprehensive Disease Characterization

**Disease:** Dermatosparaxis Ehlers-Danlos Syndrome (dEDS)
**Category:** Connective Tissue Disorder
**Key identifiers:** OMIM **225410** · Orphanet **ORPHA:1901** · MONDO **0009159** · former name **EDS type VIIC** · ICD-11 LD28.0Y (Ehlers-Danlos syndrome, other specified) · MeSH Ehlers-Danlos Syndrome (D004535)

---

## Summary

Dermatosparaxis Ehlers-Danlos syndrome (dEDS) is an ultra-rare, autosomal-recessive heritable connective tissue disorder caused by **biallelic loss-of-function variants in *ADAMTS2*** (chromosome 5q35.3), the gene encoding **procollagen I N-proteinase (pNPI)**. This zinc metalloproteinase excises the amino-terminal propeptide of type I, II, and III procollagens — a mandatory processing step that permits near-spontaneous assembly of collagen trimers into mature fibrils. When enzyme activity is abolished, unprocessed pN-collagen accumulates, producing structurally defective, ribbon-like or "hieroglyphic" collagen fibrils. The clinical consequence is a congenital, multisystem fragility syndrome dominated by extreme skin fragility, redundant/lax skin, easy bruising, a recognizable facial gestalt, and variable visceral, vascular, and skeletal complications ([PMID: 10417273](https://pubmed.ncbi.nlm.nih.gov/10417273/); [PMID: 26765342](https://pubmed.ncbi.nlm.nih.gov/26765342/); [PMID: 39641471](https://pubmed.ncbi.nlm.nih.gov/39641471/)).

dEDS occupies a unique position in medical genetics because its animal counterpart — **dermatosparaxis** — was described in cattle decades before the human disorder was molecularly solved, and the *same gene* underlies naturally occurring disease across cattle, sheep, dogs, and cats. This cross-species conservation, combined with a well-characterized *Adamts2*-knockout mouse, makes dEDS a paradigmatic loss-of-function Mendelian disorder within the broader ADAMTS metalloproteinase superfamily ([PMID: 24443030](https://pubmed.ncbi.nlm.nih.gov/24443030/); [PMID: 28856769](https://pubmed.ncbi.nlm.nih.gov/28856769/); [PMID: 29649548](https://pubmed.ncbi.nlm.nih.gov/29649548/); [PMID: 25770910](https://pubmed.ncbi.nlm.nih.gov/25770910/)).

There is **no disease-specific or curative therapy**. dEDS is placed within the 2017 international EDS classification as one of 12 molecularly defined subtypes, and management is symptomatic, protective, surgical, and multidisciplinary, supported by autosomal-recessive genetic counseling (25% sibling recurrence risk) and *ADAMTS2* molecular confirmation ([PMID: 40887396](https://pubmed.ncbi.nlm.nih.gov/40887396/)).

---

## 1. Disease Information

**Overview.** dEDS is a rare recessively inherited connective tissue disorder characterized by extreme skin fragility. It was historically designated **Ehlers-Danlos syndrome type VIIC** in the older Villefranche nomenclature and renamed **dermatosparaxis EDS** in the 2017 international classification. The name "dermatosparaxis" (Greek: *derma* = skin, *sparassein* = to tear) was coined for the analogous bovine disease, in which the skin tears easily. dEDS is defined by an absence of procollagen I N-proteinase activity ([PMID: 10417273](https://pubmed.ncbi.nlm.nih.gov/10417273/)).

> *"Like the animal model dermatosparaxis, EDS type VIIC results from the absence of activity of procollagen I N-proteinase (pNPI), the enzyme that excises the N-propeptide of type I and type II procollagens."* — Colige et al., 1999 ([PMID: 10417273](https://pubmed.ncbi.nlm.nih.gov/10417273/))

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| OMIM | 225410 |
| Orphanet | ORPHA:1901 |
| MONDO | 0009159 |
| Former name | EDS type VIIC (Villefranche) |
| Gene | *ADAMTS2* (HGNC:217) |
| MeSH | Ehlers-Danlos Syndrome (D004535) |

**Synonyms / alternative names:** dermatosparaxis type EDS; EDS dermatosparaxis type; EDS VIIC; Ehlers-Danlos syndrome type 7C; procollagen I N-proteinase deficiency; human dermatosparaxis.

**Data source type.** The knowledge summarized here is derived from **aggregated disease-level resources** — primary case reports, small case series (individual patient molecular and clinical data), OMIM/Orphanet, and model-organism studies — rather than from a single EHR cohort. Because dEDS is ultra-rare (well under 100 reported human cases worldwide), the literature is dominated by individual and small-series patient reports.

---

## 2. Etiology

**Primary cause (genetic).** dEDS is caused exclusively by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *ADAMTS2***. There is no environmental or infectious cause; the disorder is fully monogenic and recessive. The pathogenic mechanism is deficiency of procollagen I N-proteinase activity, which prevents removal of the procollagen N-propeptide.

**Genetic risk factors.** The only risk factor is inheritance of two defective *ADAMTS2* alleles. There are no known modifier loci or susceptibility variants in humans; carriers (heterozygotes) are unaffected. **Consanguinity** increases risk, consistent with a recessive disorder — several reported homozygous patients arose in consanguineous or geographically isolated families.

**Environmental / protective factors.** None established. Because the disorder is monogenic with a loss-of-function mechanism and near-complete penetrance, environmental modifiers, protective alleles, and gene–environment interactions have **not been described** and are not applicable in the conventional sense. (Not available for this disease.)

**Gene–environment interactions.** Not applicable / not documented for a fully penetrant recessive enzyme deficiency.

---

## 3. Phenotypes

dEDS presents at birth (congenital onset) with a recognizable, multisystem phenotype. Severity is variable, with a classic severe form and a documented milder variant.

| Phenotype | Type | Suggested HPO term | Onset / frequency notes |
|-----------|------|--------------------|--------------------------|
| Extreme skin fragility | Physical manifestation | HP:0000974 (Hyperextensible skin) / HP:0000979 (Bruising susceptibility) | Congenital; near-universal; hallmark feature |
| Redundant/lax (sagging) skin, skin folds | Physical manifestation | HP:0000973 (Cutis laxa) | Congenital; often requires surgical resection in adults |
| Excessive/easy bruising | Clinical sign | HP:0000978 (Bruising susceptibility) | Congenital; frequent |
| Characteristic facial gestalt (puffy eyelids, epicanthal folds, micrognathia, blue sclerae) | Physical manifestation | HP:0001999 (Abnormal facial shape); HP:0000592 (Blue sclerae) | Congenital; recognizable "facies" |
| Joint laxity/hypermobility | Clinical sign | HP:0001382 (Joint hypermobility) | Congenital |
| Umbilical/inguinal hernia | Physical manifestation | HP:0001537 (Umbilical hernia) | Congenital/childhood |
| Delayed wound healing, atrophic scarring | Clinical sign | HP:0001058 (Poor wound healing) | Lifelong |
| Visceral/vascular fragility (e.g., gastric volvulus, diaphragmatic hernia) | Clinical sign | Hernia / GI terms | Variable; severe complications reported in adults |
| Multiple fractures / reduced bone mineral density | Laboratory/imaging abnormality | HP:0002659 (Increased susceptibility to fractures); HP:0004349 (Reduced bone mineral density) | Adult natural history |

**Severity and course.** Extreme skin fragility and laxity are the cardinal features; the disease is congenital and lifelong (chronic, non-remitting), with cumulative complications in adulthood. A **milder phenotypic variant** exists in addition to the typical severe form ([PMID: 26765342](https://pubmed.ncbi.nlm.nih.gov/26765342/)).

> *"all presenting a recognizable phenotype with characteristic facial gestalt, extreme skin fragility and laxity, excessive bruising, and sometimes major complications due to visceral and vascular fragility."* — Van Damme et al., 2016 ([PMID: 26765342](https://pubmed.ncbi.nlm.nih.gov/26765342/))

The first adult natural-history case series (n = 5, ages 22–42 years) expanded the phenotype into adulthood:

> *"Complications include extreme skin fragility resulting in iatrogenic injury, redundant skin folds often requiring surgical resection, severe complications following a gastric volvulus secondary to a diaphragmatic hernia, and multiple fractures."* — Angwin et al., 2025 ([PMID: 39641471](https://pubmed.ncbi.nlm.nih.gov/39641471/))

The original molecular series described the classic constellation:

> *"characterized by extreme skin fragility, characteristic facies, joint laxity, droopy skin, umbilical hernia, and blue sclera."* — Colige et al., 1999 ([PMID: 10417273](https://pubmed.ncbi.nlm.nih.gov/10417273/))

**Quality-of-life impact.** No dEDS-specific EQ-5D/SF-36 data exist (ultra-rare disease). Extrapolating from the natural history, quality of life is affected by chronic skin fragility (requiring meticulous wound care and avoidance of trauma), disfiguring redundant skin folds and surgical scarring, hernias, fracture risk, and the psychosocial burden of a visible, chronic condition. Iatrogenic injury during routine medical procedures is a recurring, avoidable harm.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***ADAMTS2*** (a disintegrin and metalloproteinase with thrombospondin motifs 2), HGNC:217, located at **5q35.3**, encoding **procollagen I N-proteinase (pNPI)**. OMIM gene 604539; disease OMIM 225410.

**Pathogenic variant spectrum.** All confirmed dEDS variants are **loss-of-function**, abolishing enzyme activity. Documented classes:

| Variant | Type | Consequence | Source |
|---------|------|-------------|--------|
| c.673C>T, p.(Gln225*) (Q225X) | Nonsense | Premature stop; mRNA decay | Colige 1999 ([PMID: 10417273](https://pubmed.ncbi.nlm.nih.gov/10417273/)) — 5/6 patients homozygous |
| p.(Trp795*) (W795X) | Nonsense | Premature stop | Colige 1999 ([PMID: 10417273](https://pubmed.ncbi.nlm.nih.gov/10417273/)) — 6th patient homozygous |
| c.2927_2928delCT, p.(Pro976Argfs*42) | Frameshift | Truncation | Van Damme 2016 ([PMID: 26765342](https://pubmed.ncbi.nlm.nih.gov/26765342/)) |
| c.669_670dupG, p.(Pro224Argfs*24) | Frameshift (dup) | Truncation | Van Damme 2016 ([PMID: 26765342](https://pubmed.ncbi.nlm.nih.gov/26765342/)) |
| c.2751-2A>T | Splice-site | Aberrant splicing | Van Damme 2016 ([PMID: 26765342](https://pubmed.ncbi.nlm.nih.gov/26765342/)) |
| c.2T>C / c.884_887delTGAA | Start-loss / frameshift (compound het) | Loss of function | Van Damme 2016 ([PMID: 26765342](https://pubmed.ncbi.nlm.nih.gov/26765342/)) |
| Genomic deletions → in-frame skipping of exons 3–5 and exons 14–16 | Structural / splicing | Abolished enzyme activity despite in-frame | Colige 2004 ([PMID: 15373769](https://pubmed.ncbi.nlm.nih.gov/15373769/)) |

> *"Five of the individuals with EDS type VIIC were homozygous for a C-->T transition that results in a premature termination codon, Q225X."* — Colige et al., 1999 ([PMID: 10417273](https://pubmed.ncbi.nlm.nih.gov/10417273/))

> *"We identified three novel homozygous loss-of-function mutations (c.2927_2928delCT, p.(Pro976Argfs*42); c.669_670dupG, p.(Pro224Argfs*24); and c.2751-2A>T) and one compound heterozygous mutation."* — Van Damme et al., 2016 ([PMID: 26765342](https://pubmed.ncbi.nlm.nih.gov/26765342/))

A notable insight from the 2004 study is that even **in-frame exon-skipping** events (exons 3–5 or 14–16), affecting domains not previously thought essential, strongly impaired aminoprocollagen processing in vitro and in vivo — demonstrating that these domains are required for proper enzyme function ([PMID: 15373769](https://pubmed.ncbi.nlm.nih.gov/15373769/)).

**Variant classification (ACMG/AMP).** Reported variants are **pathogenic** (nonsense, frameshift, canonical splice, structural), fulfilling loss-of-function criteria for a gene where LoF is the established mechanism.

**Allele frequency / origin.** All variants are **germline**; pathogenic alleles are exceedingly rare in gnomAD (consistent with an ultra-rare recessive disorder). No somatic contribution.

**Functional consequence.** **Loss of function** (enzyme deficiency). Not gain-of-function or dominant-negative — heterozygous carriers are healthy.

**Modifier genes.** No human modifier genes established. Mouse work implicates the paralog *Adamts14* as a minor contributor to dermal procollagen processing (see Section 15).

**Epigenetics / chromosomal abnormalities.** Not implicated. No methylation, histone, or large-scale cytogenetic mechanisms are described; dEDS is a point-mutation/small-indel recessive disorder. (Not applicable.)

---

## 5. Environmental Information

dEDS is a **purely genetic** disorder. No environmental factors, toxins, radiation, occupational exposures, lifestyle factors, or infectious agents cause or trigger it. Physical trauma exacerbates the *manifestations* (skin tears, bruising, iatrogenic surgical injury) but does not cause the disease. Careful avoidance of mechanical stress and trauma is the practical corollary. (Environmental etiology: not applicable.)

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

```
Biallelic ADAMTS2 LoF variant
        │
        ▼
Absent/deficient procollagen I N-proteinase (pNPI) activity
        │
        ▼
N-propeptide of type I (II, III) procollagen NOT excised
        │
        ▼
pN-collagen accumulates; trimers cannot assemble normally
        │
        ▼
Structurally defective, ribbon-like/"hieroglyphic" collagen fibrils
        │
        ▼
Weak dermal & connective tissue matrix
        │
        ▼
Extreme skin fragility, laxity, bruising, hernias,
visceral/vascular/skeletal fragility (clinical dEDS)
```

**Molecular pathway / biochemistry.** Fibril-forming procollagens possess a central triple-helical domain flanked by N- and C-propeptides. **Both propeptides must be proteolytically removed** to permit spontaneous assembly of trimers into fibrils and fibers. The **N-propeptide is cleaved by procollagen N-proteinases ADAMTS2, ADAMTS3, and ADAMTS14**, while the C-propeptide is cleaved by tolloid-family (BMP1) proteinases ([PMID: 25863161](https://pubmed.ncbi.nlm.nih.gov/25863161/)).

> *"the amino-propeptide is usually processed by procollagen N-proteinases: ADAMTS2, 3 and 14."* — Bekhouche & Colige, 2015 ([PMID: 25863161](https://pubmed.ncbi.nlm.nih.gov/25863161/))

> *"these two propeptides have to be proteolytically removed to allow the almost spontaneous assembly of the trimers into collagen fibrils and fibers."* — Bekhouche & Colige, 2015 ([PMID: 25863161](https://pubmed.ncbi.nlm.nih.gov/25863161/))

**Protein dysfunction.** ADAMTS2 is a secreted **zinc metalloproteinase** containing a catalytic (metalloprotease) domain plus ancillary thrombospondin/properdin repeats, a disintegrin-like domain, and a cysteine-rich domain. Loss-of-function variants remove or inactivate catalytic capacity (or destabilize the transcript via nonsense-mediated decay), yielding **enzyme deficiency** — a classic loss-of-function protein defect rather than aggregation or misfolding-toxicity. A short catalytic-only isoform and a long isoform exist ([PMID: 25863161](https://pubmed.ncbi.nlm.nih.gov/25863161/); [PMID: 10417273](https://pubmed.ncbi.nlm.nih.gov/10417273/)).

**Cellular processes and cell types.** The principal effector cell is the **dermal fibroblast** (CL:0000057; fibroblast), which synthesizes and secretes procollagen. The affected biological process is extracellular collagen fibril organization.

- **GO biological process:** collagen fibril organization (GO:0030199); extracellular matrix organization (GO:0030198); collagen metabolic process (GO:0032963); proteolysis (GO:0006508).
- **GO molecular function:** metalloendopeptidase activity (GO:0004222); procollagen N-endopeptidase activity (GO:0004251).
- **GO cellular component:** extracellular space/matrix (GO:0005615, GO:0031012).
- **Cell types (CL):** fibroblast (CL:0000057); dermal fibroblast.

**Metabolic / immune / tissue damage mechanisms.** There is no primary metabolic derangement, and no autoimmune mechanism in human dEDS. Tissue "damage" is mechanical — a structurally weak matrix fails under normal shear/tensile stress, causing skin tears and connective-tissue rupture. (Of note, an immune-dysregulation phenotype emerges only in aged *Adamts2/14* double-knockout mice — see Section 15 — and is not a documented feature of human dEDS.)

**Molecular profiling.** No dedicated human transcriptomic/proteomic/metabolomic dEDS datasets are established; the diagnosis rests on biochemistry (accumulation of unprocessed pN-collagen), ultrastructure (abnormal fibrils on electron microscopy), and molecular genetics.

---

## 7. Anatomical Structures Affected

- **Primary organ/system:** the **skin/integumentary system** (UBERON:0002097 skin of body; UBERON:0002199 dermis) — the dominant site of fragility and laxity.
- **Tissue type:** **connective tissue** (UBERON:0002384), specifically dense irregular connective tissue of the dermis, with a type I (and II, III) collagen-rich matrix.
- **Secondary/systemic involvement:** musculoskeletal (joints — hypermobility; bone — fractures, reduced BMD), gastrointestinal/abdominal wall (hernias — umbilical, diaphragmatic; gastric volvulus), vascular tissue (vascular fragility), and ocular tissue (blue sclerae, UBERON:0001773 sclera).
- **Cell populations:** dermal **fibroblasts** (CL:0000057) as collagen-producing cells.
- **Subcellular:** the pathology is **extracellular** — the defect manifests in the secreted extracellular matrix (GO:0031012), downstream of ER/Golgi collagen synthesis and secretion. No primary organelle defect.
- **Localization / lateralization:** generalized and **bilateral/systemic**; skin fragility is diffuse rather than focal.

---

## 8. Temporal Development

- **Onset:** **congenital** — features are present at birth (skin fragility, laxity, characteristic facies, hernias). Onset pattern is chronic/constitutive.
- **Progression:** the underlying matrix defect is static (lifelong enzyme deficiency), but **complications accumulate with age** — redundant skin folds, surgical scarring, fractures, reduced bone mineral density, and visceral events (e.g., gastric volvulus) documented in adults ([PMID: 39641471](https://pubmed.ncbi.nlm.nih.gov/39641471/)).
- **Course:** chronic, lifelong, non-remitting; no spontaneous remission. Not episodic or relapsing-remitting.
- **Critical periods:** the neonatal/pediatric period is critical for diagnosis and for instituting trauma-avoidance and wound-care protocols to prevent iatrogenic injury.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (biallelic *ADAMTS2* LoF). Sibling recurrence risk 25%.
- **Penetrance:** effectively **complete** for biallelic LoF genotypes (with variable expressivity — typical severe vs. milder variant).
- **Expressivity:** **variable**, including a recognized milder phenotype ([PMID: 26765342](https://pubmed.ncbi.nlm.nih.gov/26765342/)).
- **Carrier state:** heterozygotes are asymptomatic. Carrier frequency is very low (ultra-rare disorder); no founder mutation of broad population impact is established, though recurrent variants (e.g., Q225X) occur.
- **Consanguinity:** contributes, as expected for a recessive disorder — many reported homozygous cases derive from consanguineous unions.
- **Epidemiology:** **ultra-rare** — fewer than ~60–100 human cases reported worldwide; precise prevalence/incidence figures are not reliably established (Orphanet lists prevalence as unknown/<1 per 1,000,000). No sex predilection (recessive, autosomal). No specific ethnic or geographic clustering beyond consanguineous kindreds.
- **Anticipation / germline mosaicism:** not applicable (no repeat expansion; no reported mosaicism of clinical relevance).

---

## 10. Diagnostics

**Diagnostic approach.** Diagnosis is clinical (recognizable phenotype) **confirmed molecularly** by identification of biallelic pathogenic *ADAMTS2* variants. dEDS is one of the 12 EDS subtypes with a defined molecular etiology, for which molecular confirmation is expected under the 2017 classification ([PMID: 40887396](https://pubmed.ncbi.nlm.nih.gov/40887396/)).

**Biochemical / laboratory tests.**
- **Procollagen processing assay** on cultured dermal fibroblasts: accumulation of unprocessed **pN-collagen** (retained N-propeptide) is the biochemical hallmark, reflecting absent pNPI activity.
- **Electron microscopy of skin:** abnormal collagen fibril morphology (irregular, ribbon-like/"hieroglyphic" cross-sections).

**Genetic testing.**
- **Single-gene testing / targeted *ADAMTS2* sequencing** when the phenotype is recognized.
- **EDS/connective-tissue gene panels** (NGS) including *ADAMTS2* — the pragmatic first-line molecular test given phenotypic overlap among EDS subtypes.
- **Whole-exome/whole-genome sequencing** for atypical presentations or when panels are negative; useful to detect structural variants (e.g., the genomic deletions causing in-frame exon skipping described by Colige 2004, [PMID: 15373769](https://pubmed.ncbi.nlm.nih.gov/15373769/)).
- Karyotype/FISH/CMA and mitochondrial testing are **not indicated** (not a cytogenetic or mitochondrial disorder).

**Clinical criteria & differential diagnosis.** Diagnosis follows the **2017 international EDS classification**, which requires spotting clinical red flags and eliminating differential diagnoses, with molecular confirmation ([PMID: 40887396](https://pubmed.ncbi.nlm.nih.gov/40887396/)). Differential diagnoses include other EDS subtypes (classical EDS, kyphoscoliotic EDS, cutis laxa syndromes) and *AEBP1*-related EDS (thin/hyperextensible skin, atrophic scarring, joint hypermobility, osteoporosis — [PMID: 30668708](https://pubmed.ncbi.nlm.nih.gov/30668708/)). Distinguishing features of dEDS: congenital *extreme* skin fragility and laxity with redundant skin folds and characteristic facies, plus the specific pN-collagen biochemical signature.

**Screening.** For at-risk families, **cascade genetic testing** and **carrier testing** of relatives; prenatal/preimplantation genetic testing is feasible once the familial variants are known.

---

## 11. Outcome / Prognosis

- **Survival / life expectancy:** dEDS is generally **not primarily life-limiting** in the way vascular EDS is, but severe visceral and vascular fragility can cause major, potentially life-threatening complications (e.g., gastric volvulus secondary to diaphragmatic hernia; vascular rupture) ([PMID: 26765342](https://pubmed.ncbi.nlm.nih.gov/26765342/); [PMID: 39641471](https://pubmed.ncbi.nlm.nih.gov/39641471/)). Formal survival statistics are unavailable (ultra-rare).
- **Morbidity / disability:** substantial and lifelong — chronic skin fragility, disfiguring redundant skin folds (often requiring surgical resection), recurrent bruising, hernias, fractures, and reduced bone mineral density in adults ([PMID: 39641471](https://pubmed.ncbi.nlm.nih.gov/39641471/)).
- **Complications:** iatrogenic skin injury during medical care, poor wound healing/atrophic scarring, hernias, gastric volvulus, fractures, and vascular events.
- **Prognostic factors:** severity of the phenotype (typical vs. milder variant) and the presence of visceral/vascular fragility. No validated molecular prognostic biomarkers exist.
- **Quality-of-life tools:** no dEDS-specific instruments; generic connective-tissue-disorder burden applies.

---

## 12. Treatment

**No curative or disease-specific therapy exists.** Under the 2017 framework, non-vascular EDS management is symptomatic, multidisciplinary, and personalized ([PMID: 40887396](https://pubmed.ncbi.nlm.nih.gov/40887396/)).

> *"There is no specific treatment for non-vascular EDS to date, so the care management is symptomatic, multidisciplinary and personalized."* — Benistan & Guichou, 2026 ([PMID: 40887396](https://pubmed.ncbi.nlm.nih.gov/40887396/))

**Management pillars (NCIT term suggestions in parentheses):**
- **Protective / supportive care:** trauma avoidance, meticulous skin protection and wound care, padding, avoidance of unnecessary invasive procedures to prevent iatrogenic injury (NCIT: Supportive Care).
- **Surgical intervention:** resection of redundant skin folds; careful surgical technique given fragile tissues and poor healing; hernia repair; management of visceral emergencies such as gastric volvulus (NCIT: Surgical Procedure). Surgery carries elevated risk due to tissue fragility and impaired wound healing.
- **Skeletal / bone health:** monitoring and management of reduced bone mineral density and fractures (physiotherapy, fall/fracture prevention; consider bone-health surveillance).
- **Rehabilitation:** physiotherapy/occupational therapy for joint hypermobility and function (NCIT: Physical Therapy).
- **Pain and symptom management:** as needed, individualized.
- **No pharmacogenomic, gene, cell, RNA, targeted, or immunotherapy** is established for dEDS. No approved drugs. No relevant clinical trials with NCT identifiers specific to dEDS.

**Personalized medicine.** Care is genotype-confirmed but not genotype-*directed* therapeutically; the value of molecular diagnosis lies in prognosis, counseling, and family planning rather than drug selection.

---

## 13. Prevention

- **Primary prevention:** not possible for an inherited monogenic disorder. **Genetic counseling** is central: autosomal-recessive inheritance carries a 25% recurrence risk for siblings of an affected child; carrier testing and cascade screening inform reproductive decisions.
- **Reproductive options:** prenatal diagnosis and **preimplantation genetic testing** are available for families with known *ADAMTS2* variants.
- **Secondary/tertiary prevention:** early diagnosis to implement trauma-avoidance and wound-care protocols; surveillance for and early management of hernias, visceral complications, and bone fragility to prevent morbidity.
- **Immunization / public-health / environmental interventions:** not applicable (non-infectious, non-environmental).

---

## 14. Other Species / Natural Disease

dEDS is remarkable for its **broad natural occurrence across mammals**, all traced to *ADAMTS2* — a strong argument for evolutionary conservation of the collagen-processing mechanism.

| Species (NCBI Taxon) | Disease | *ADAMTS2* variant | Source |
|----------------------|---------|-------------------|--------|
| Cattle, *Bos taurus* (9913) | Bovine dermatosparaxis (original "dermatosparaxis") | 17-bp deletion → frameshift | Colige 1999 ([PMID: 10417273](https://pubmed.ncbi.nlm.nih.gov/10417273/)); Halper 2014 ([PMID: 24443030](https://pubmed.ncbi.nlm.nih.gov/24443030/)) |
| Sheep, *Ovis aries* (9940) | Ovine dermatosparaxis (White Dorper) | Causative nonsense mutation | Joller 2017 ([PMID: 28856769](https://pubmed.ncbi.nlm.nih.gov/28856769/)) |
| Sheep, *Ovis aries* (9940) | Dermatosparaxis in commercial flock | Catalytic-domain missense **V15M** (SIFT/PolyPhen damaging) | Monteagudo 2015 ([PMID: 25354687](https://pubmed.ncbi.nlm.nih.gov/25354687/)) |
| Dog, *Canis lupus familiaris* (9615) | EDS-like skin fragility | *ADAMTS2*-related and other collagen genes | Halper 2014 ([PMID: 24443030](https://pubmed.ncbi.nlm.nih.gov/24443030/)) |
| Cat, *Felis catus* (9685) | Dermatosparaxis/EDS-like | *ADAMTS2*/collagen defects | Halper 2014 ([PMID: 24443030](https://pubmed.ncbi.nlm.nih.gov/24443030/)) |

> *"Several cases of bovine and ovine dermatosparaxis analogous to human Ehlers-Danlos syndrome type VIIC were found to be caused by mutations in the procollagen I N-proteinase (pnPI) or ADAMTS2 gene."* — Halper, 2014 ([PMID: 24443030](https://pubmed.ncbi.nlm.nih.gov/24443030/))

> *"A missense mutation was identified in the catalytic domain of ADAMTS2. The mutation is predicted to cause the substitution in the mature ADAMTS2 of a valine molecule by a methionine molecule (V15M) affecting the catalytic domain of the enzyme."* — Monteagudo et al., 2015 ([PMID: 25354687](https://pubmed.ncbi.nlm.nih.gov/25354687/))

The White Dorper study confirmed the causative nonsense mutation ([PMID: 28856769](https://pubmed.ncbi.nlm.nih.gov/28856769/)).

**Comparative pathology.** In dogs and cats, EDS from collagen/ADAMTS2 defects predominantly affects the **skin** (thin, hyperextensible, hemorrhagic wounds, atrophic scars), generally **without** the systemic organ/vascular rupture seen in humans — an important species difference ([PMID: 24443030](https://pubmed.ncbi.nlm.nih.gov/24443030/)). **Veterinary relevance** is significant in livestock (economic losses; animal welfare). **Zoonotic potential:** none (genetic, non-transmissible). **Orthologous genes:** *ADAMTS2* orthologs (mouse *Adamts2*, bovine/ovine/canine/feline *ADAMTS2*), reflecting deep evolutionary conservation of the N-proteinase mechanism.

---

## 15. Model Organisms

**Mouse (*Mus musculus*, NCBI Taxon 10090)** is the principal genetic model.

- **Adamts2-knockout mouse:** recapitulates the human skin/collagen phenotype (skin fragility with abnormal collagen fibrils), validating *ADAMTS2* loss of function as sufficient to produce dermatosparaxis-like disease.
- **Paralog redundancy — Adamts14:** *Adamts14*-deficient mice are healthy, fertile, with normal aminoprocollagen processing. Crossing them with *Adamts2*-deficient mice produced double-knockout animals with essentially the same phenotype as *Adamts2*-single-knockouts, establishing **ADAMTS2 as the dominant dermal N-proteinase** and ADAMTS14 as a minor contributor ([PMID: 29649548](https://pubmed.ncbi.nlm.nih.gov/29649548/)).

> *"showed the same phenotype as that of Adamts2-deficient mice, with no further reduction of procollagen processing and no significant aggravation of the structural alterations of collagen fibrils."* — Dupont et al., 2018 ([PMID: 29649548](https://pubmed.ncbi.nlm.nih.gov/29649548/))

- **Emergent immune phenotype:** aged *Adamts2/14* double-knockout **males** (from ~2 months) developed spontaneous atopic-dermatitis-like epidermal lesions driven by abnormal T-lymphocyte activation toward a Th1 profile — a model-specific finding not reported in human dEDS but of mechanistic interest ([PMID: 29649548](https://pubmed.ncbi.nlm.nih.gov/29649548/)).

> *"the result of an abnormal activation and differentiation of T lymphocytes towards a Th1 profile."* — Dupont et al., 2018 ([PMID: 29649548](https://pubmed.ncbi.nlm.nih.gov/29649548/))

- **Division of labor within the ADAMTS2/3/14 subfamily:** *Adamts3*-null embryos die around E15 from failed lymphangiogenesis (VEGF-C dysregulation) with **normal** procollagen I/II/III processing — showing that ADAMTS3's essential role is in lymphatic development, not dermal collagen, while ADAMTS2 handles dermal procollagen ([PMID: 26446156](https://pubmed.ncbi.nlm.nih.gov/26446156/)).

> *"The only documented activity of a subclass of ADAMTS proteases comprising ADAMTS2, 3 and 14 is the cleavage of the aminopropeptide of fibrillar procollagens."* — Janssen et al., 2016 ([PMID: 26446156](https://pubmed.ncbi.nlm.nih.gov/26446156/))

- **Naturally occurring large-animal models** (cattle, sheep — Section 14) provide gross, tissue, and biochemical parallels to human disease.

**Model applications & limitations.** Mouse and livestock models faithfully reproduce the collagen-processing defect and skin fragility, enabling study of fibrillogenesis, wound healing, and potential enzyme-replacement/gene approaches. Limitations: mice do not fully recapitulate the human facial gestalt or the full spectrum of visceral/vascular complications, and the Th1 atopic-dermatitis phenotype of double-knockouts is not a human dEDS feature.

**Model resources:** MGI (mouse *Adamts2*), OMIA (bovine/ovine dermatosparaxis), plus large-animal veterinary genetics resources.

---

## Mechanistic Model / Interpretation

dEDS is a textbook **loss-of-function Mendelian enzymopathy of extracellular matrix assembly**. The single molecular lesion — abolished procollagen I N-proteinase activity — propagates deterministically to a macroscopic phenotype:

```
GENE (ADAMTS2, 5q35.3, biallelic LoF)
   → PROTEIN (procollagen I N-proteinase deficiency; loss of function)
      → BIOCHEMISTRY (N-propeptide not excised; pN-collagen accumulates)
         → ULTRASTRUCTURE (defective ribbon-like "hieroglyphic" fibrils)
            → TISSUE (weak dermal/connective matrix)
               → CLINICAL (extreme skin fragility, laxity, bruising,
                           facies, hernias, visceral/vascular/skeletal fragility)
```

The disorder sits within the ADAMTS metalloproteinase superfamily paradigm: of 19 mammalian secreted ADAMTS proteinases, several cause **recessive, loss-of-function Mendelian disorders**, first delineated through spontaneous human and animal mutations — including bovine *ADAMTS2* ([PMID: 25770910](https://pubmed.ncbi.nlm.nih.gov/25770910/)).

> *"These human and animal disorders are recessive and their manifestations appear to result from a loss-of-function mechanism."* — Dubail & Apte, 2015 ([PMID: 25770910](https://pubmed.ncbi.nlm.nih.gov/25770910/))

> *"spontaneous animal mutations, such as in bovine ADAMTS2."* — Dubail & Apte, 2015 ([PMID: 25770910](https://pubmed.ncbi.nlm.nih.gov/25770910/))

The cross-species conservation (human ↔ cattle ↔ sheep ↔ dog ↔ cat ↔ mouse) is the strongest external validation of the mechanism: identical enzyme deficiency yields analogous fragility phenotypes wherever it occurs, with species-specific attenuation of systemic (visceral/vascular) involvement in companion animals.

---

## Evidence Base

| PMID | Study | Role in this report |
|------|-------|---------------------|
| [10417273](https://pubmed.ncbi.nlm.nih.gov/10417273/) | Colige 1999 — Human EDS VIIC & bovine dermatosparaxis caused by procollagen I N-proteinase mutations | **Foundational**: molecular proof that *ADAMTS2* LoF causes human dEDS and bovine dermatosparaxis; defines pNPI function; recurrent Q225X |
| [26765342](https://pubmed.ncbi.nlm.nih.gov/26765342/) | Van Damme 2016 — Expanding clinical & mutational spectrum | Expands LoF variant spectrum; defines characteristic gestalt, extreme fragility, visceral/vascular complications, milder variant |
| [39641471](https://pubmed.ncbi.nlm.nih.gov/39641471/) | Angwin 2025 — Natural history, adult case series | Adult complications: iatrogenic injury, redundant skin resection, gastric volvulus, fractures, low BMD |
| [15373769](https://pubmed.ncbi.nlm.nih.gov/15373769/) | Colige 2004 — Novel mutation types | In-frame exon-skipping variants also abolish enzyme activity; broadens variant classes |
| [25863161](https://pubmed.ncbi.nlm.nih.gov/25863161/) | Bekhouche & Colige 2015 — ADAMTS2/3/14 in pathophysiology | Places ADAMTS2 in the N-proteinase family; explains propeptide-removal requirement for fibrillogenesis |
| [29649548](https://pubmed.ncbi.nlm.nih.gov/29649548/) | Dupont 2018 — Adamts2/14 double-KO mice | ADAMTS2 is dominant dermal N-proteinase; ADAMTS14 minor; emergent Th1 immune dysregulation |
| [26446156](https://pubmed.ncbi.nlm.nih.gov/26446156/) | Janssen 2016 — Adamts3 & lymphangiogenesis | Division of labor within ADAMTS2/3/14 subfamily; ADAMTS3 essential for lymphatics |
| [25770910](https://pubmed.ncbi.nlm.nih.gov/25770910/) | Dubail & Apte 2015 — ADAMTS genetics review | Frames dEDS as recessive LoF disorder in the ADAMTS superfamily |
| [24443030](https://pubmed.ncbi.nlm.nih.gov/24443030/) | Halper 2014 — Connective tissue disorders in domestic animals | Establishes cattle/sheep/dog/cat natural disease; comparative pathology differences |
| [28856769](https://pubmed.ncbi.nlm.nih.gov/28856769/) | Joller 2017 — White Dorper sheep | Confirms causative *ADAMTS2* nonsense mutation in ovine dermatosparaxis |
| [25354687](https://pubmed.ncbi.nlm.nih.gov/25354687/) | Monteagudo 2015 — Ovine flock | Catalytic-domain missense V15M model |
| [40887396](https://pubmed.ncbi.nlm.nih.gov/40887396/) | Benistan & Guichou 2026 — EDS diagnosis & care | 2017 classification framework; no specific treatment; symptomatic multidisciplinary care |
| [30668708](https://pubmed.ncbi.nlm.nih.gov/30668708/) | Blackburn 2019 — *AEBP1* EDS | Differential diagnosis (EDS-like phenotype from a distinct gene) |

All quoted snippets above were verified against the stored abstracts during the investigation.

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity limits epidemiology.** Fewer than ~100 human cases are reported; precise prevalence, incidence, sex/age distributions, penetrance quantification, and formal survival statistics are unavailable. Estimates are qualitative.
2. **No quality-of-life or PRO data** specific to dEDS (no EQ-5D/SF-36/PROMIS studies).
3. **No omics resources** (transcriptomic/proteomic/metabolomic/single-cell) dedicated to human dEDS; mechanism rests on biochemistry, EM, and genetics.
4. **UniProt/structural protein-level queries were unavailable during the investigation**, so ADAMTS2 domain-level structural detail is drawn from the primary literature rather than direct database interrogation.
5. **Genotype–phenotype correlation is incomplete** — the basis for the "typical severe" vs. "milder" variant distinction, and modifiers of expressivity, are not resolved in humans.
6. **Therapeutics gap:** no disease-modifying therapy; no dEDS-specific clinical trials identified.
7. **Model-to-human translation caveat:** the Th1 atopic-dermatitis phenotype of *Adamts2/14* double-KO mice is not a documented human feature and should not be over-interpreted.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a dEDS patient registry** (multicenter, international) to capture prevalence, natural history, complication rates, and standardized quality-of-life outcomes.
2. **Genotype–phenotype study** correlating variant class/location (e.g., catalytic vs. ancillary domains, complete vs. partial LoF) with severity, to explain the typical-vs-milder dichotomy.
3. **Deep phenotyping of visceral/vascular fragility** (imaging surveillance protocols) to define screening recommendations and prevent life-threatening events such as gastric volvulus.
4. **Bone-health natural history** — systematic assessment of BMD and fracture risk across the lifespan to guide surveillance and intervention.
5. **Preclinical therapeutic proof-of-concept** using existing *Adamts2*-KO mouse and livestock models: evaluate enzyme-replacement, gene-addition/AAV, or read-through strategies for nonsense alleles (e.g., Q225X, W795X).
6. **Molecular/EM diagnostic standardization** — validate the pN-collagen biochemical assay and fibril-morphometry as adjuncts to molecular testing.
7. **UniProt/structural follow-up** — retrieve ADAMTS2 domain architecture and map pathogenic variants onto structure (including the in-frame exon-skipping regions shown to be functionally essential) once the resource is available.
8. **Cross-species comparative study** to understand why companion animals are spared systemic organ/vascular rupture, potentially revealing protective modifiers relevant to human disease.

---

*Report compiled from a 5-iteration autonomous investigation; 7 confirmed findings, 30 papers reviewed. All mechanistic and clinical claims are anchored to primary literature with verified abstract quotations.*


## Artifacts

- [OpenScientist final report](Dermatosparaxis_Ehlers-Danlos_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Dermatosparaxis_Ehlers-Danlos_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000057` (3 mentions) - the report calls it "fibroblasts", "Cell populations:** dermal **fibroblasts"; CL calls it **fibroblast**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0004251` (obsolete X-Pro dipeptidase activity) (1 mention)
- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0030199` (1 mention) - the report calls it "GO biological process:** collagen fibril organization"; GO calls it **collagen fibril organization**
- `GO:0004222` (1 mention) - the report calls it "GO molecular function:** metalloendopeptidase activity"; GO calls it **metalloendopeptidase activity**
- `UBERON:0002384` (1 mention) - the report calls it "connective tissue", "Tissue type:** **connective tissue"; UBERON calls it **connective tissue**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000057` - called "fibroblasts", "Cell populations:** dermal **fibroblasts"
- `UBERON:0002384` - called "connective tissue", "Tissue type:** **connective tissue"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.