---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-30T06:06:56.568607'
end_time: '2026-08-30T06:23:45.906597'
duration_seconds: 1009.34
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Short Stature, Dauber-Argente Type
  mondo_id: ''
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
citation_count: 9
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 14
  validator_version: 0.2.1
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 11
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0859182
    reported_labels:
    - Disease (MONDO)
    ontology_label: Short stature, Dauber-Argente type
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Short_Stature_Dauber-Argente_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Short_Stature_Dauber-Argente_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Short Stature, Dauber-Argente Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Short Stature, Dauber-Argente Type** covering all of the
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

# Short Stature, Dauber-Argente Type (PAPP-A2 Deficiency): A Comprehensive Disease Characterization

**Disease:** Short Stature, Dauber-Argente Type (SSDA) — PAPP-A2 deficiency
**OMIM:** #619489 · **MONDO:** MONDO:0859182 · **Gene:** *PAPPA2* (OMIM \*619485, HGNC:14615, 1q25.2)
**Category:** Mendelian, autosomal recessive · **Inheritance:** Autosomal recessive

---

## Summary

Short Stature, Dauber-Argente type (SSDA) is an ultra-rare autosomal recessive Mendelian growth disorder caused by biallelic loss-of-function mutations in *PAPPA2*, the gene encoding **pappalysin-2 (PAPP-A2)**, a metalloproteinase that cleaves insulin-like growth factor binding proteins IGFBP-3 and IGFBP-5 to release bioactive IGF-1 from its circulating reservoirs. First described by Dauber, Argente and colleagues in 2016, the disorder defines a novel mechanism of growth failure: not IGF-1 *deficiency*, but IGF-1 *sequestration*. Because PAPP-A2 proteolysis is abolished, IGF-1 remains trapped in high-molecular-weight ternary complexes (IGF-1/IGFBP-3 or -5/ALS), producing the paradoxical and diagnostically distinctive biochemical signature of **elevated total IGF-1, IGFBP-3, IGFBP-5, ALS and IGF-II, but reduced free (bioactive) IGF-1**.

Clinically, affected individuals are typically of normal size at birth and then develop **progressive postnatal growth failure**, accompanied by moderate microcephaly, thin long bones, mildly decreased bone mineral density (BMD), and insulin resistance. The condition has been reported in a small number of consanguineous families (Spanish and Saudi kindreds), consistent with private recessive mutations. The founding families carried the homozygous variants p.D643fs25\* and p.Ala1033Val, with a third family confirming the syndrome via a homozygous nonsense mutation (p.Glu886\*).

Because the fundamental defect is impaired *liberation* of IGF-1 rather than an absolute lack of IGF-1, the disorder is **therapeutically tractable with recombinant human IGF-1 (rhIGF-1, mecasermin)**, which bypasses the proteolytic bottleneck. Long-term (6-year) treatment increased growth velocity and bioactive IGF-1, allowed both treated siblings to reach target height, normalized BMD, increased lean mass, and improved insulin sensitivity, with no hypoglycemia or other adverse effects observed. Recombinant PAPP-A2 (rhPAPP-A2) itself is an emerging, mechanistically direct experimental therapy, with murine data suggesting sex-specific (female-predominant) efficacy. The *Pappa2* knockout mouse faithfully recapitulates the postnatal growth retardation and reduced bone length of the human disease.

---

## Key Findings

### Finding 1 — Biallelic loss-of-function *PAPPA2* mutations cause SSDA

The disease is caused by homozygous (biallelic) loss-of-function mutations in *PAPPA2*. The seminal 2016 report described two unrelated families carrying the homozygous mutations **p.D643fs25\*** (a frameshift) and **p.Ala1033Val** (a missense), both associated with progressive postnatal growth failure. Critically, *in vitro* IGFBP cleavage assays demonstrated that **both mutations cause a complete absence of PAPP-A2 proteolytic activity**, establishing loss of enzymatic function as the disease mechanism rather than reduced expression or altered substrate binding alone.

> *"Two different homozygous mutations in PAPPA2, p.D643fs25\* and p.Ala1033Val, were associated with this novel syndrome of growth failure. In vitro analysis of IGFBP cleavage demonstrated that both mutations cause a complete absence of PAPP-A2 proteolytic activity."* — [PMID: 26902202](https://pubmed.ncbi.nlm.nih.gov/26902202/)

A third, independent kindred from Saudi Arabia subsequently confirmed the syndrome and expanded the mutation spectrum with a new homozygous nonsense mutation, **p.Glu886\*** in exon 7, in two siblings with postnatal growth retardation and decreased IGF-1 availability.

> *"two siblings of a third family from Saudi Arabia with postnatal growth retardation and decreased IGF1 availability due to a new homozygous nonsense mutation (p.Glu886\* in exon 7) in PAPPA2"* — [PMID: 34272725](https://pubmed.ncbi.nlm.nih.gov/34272725/)

Together these independent families establish autosomal recessive inheritance with a variant spectrum dominated by truncating (frameshift, nonsense) and inactivating missense alleles, all converging on complete loss of proteolytic activity. **Variant classification:** pathogenic (ACMG/AMP), functional consequence = loss of function, germline origin.

### Finding 2 — Mechanism: IGF-1 is trapped in ternary complexes, lowering free IGF-1 despite elevated total IGF-1

The pathophysiology is a disorder of IGF-1 bioavailability. PAPP-A2 normally cleaves IGFBP-3 and IGFBP-5, the high-affinity binding proteins that, together with the acid-labile subunit (ALS), form the ~150 kDa ternary complex that serves as the circulating reservoir of IGF-1. When PAPP-A2 activity is lost, IGF-1 cannot be liberated from these complexes. Affected patients therefore show **elevated circulating total IGF-1, IGFBP-3, IGFBP-5, ALS, and IGF-II**, yet **decreased free (bioactive) IGF-1** — the biochemical hallmark of the disease.

> *"Multiple members of two unrelated families presented with progressive growth failure, moderate microcephaly, thin long bones, mildly decreased bone density and elevated circulating total IGF-I, IGFBP-3, and -5, acid labile subunit, and IGF-II concentrations."* — [PMID: 26902202](https://pubmed.ncbi.nlm.nih.gov/26902202/)

Size-exclusion chromatography provided direct mechanistic proof, showing a significant increase in IGF-1 bound in its ternary complex and correspondingly decreased free IGF-1:

> *"Size-exclusion chromatography showed a significant increase in IGF-I bound in its ternary complex. Free IGF-I concentrations were decreased. These patients provide important insights into the regulation of longitudinal growth in humans, documenting the critical role of PAPP-A2 in releasing IGF-I from its BPs."* — [PMID: 26902202](https://pubmed.ncbi.nlm.nih.gov/26902202/)

This makes SSDA a canonical example of a "hormone availability" disorder: total hormone measurements are misleadingly high, and only the free/bioactive fraction reflects the true endocrine deficit at the tissue level.

### Finding 3 — rhIGF-1 therapy improves growth, height, and bone mineral density

Because the defect is sequestration rather than deficiency, exogenous IGF-1 bypasses the proteolytic bottleneck. Two Spanish siblings (homozygous p.D643fs25\*) treated with progressively escalated rhIGF-1 (40–120 μg/kg twice daily) showed a clear increase in growth velocity and height, together with increased bioactive IGF-1 and diminished spontaneous GH secretion (consistent with restored negative feedback), while total IGF-1 and IGFBP-3 remained elevated.

> *"There was a clear increase in growth velocity and height in both siblings. Bioactive IGF-1 was increased, and spontaneous GH secretion was diminished after acute administration of rhIGF-1, whereas serum total IGF-1 and IGFBP-3 levels remained elevated. No episodes of hypoglycemia or any other secondary effects were observed during treatment."* — [PMID: 27648969](https://pubmed.ncbi.nlm.nih.gov/27648969/)

Long-term (6-year) follow-up confirmed durable benefit: both patients achieved their target height, BMD progressively normalized, and lean mass increased.

> *"Growth velocity continued to increase and both patients achieved their target height. Free IGF-1 concentrations increased notably after rhIGF-1 administration, with serum IGFBP-3, IGFBP-5 and ALS levels also being higher during treatment. BMD was progressively normalized and an increase in lean mass was also noted during treatment."* — [PMID: 34358737](https://pubmed.ncbi.nlm.nih.gov/34358737/)

**NCIT term suggestion:** Mecasermin (recombinant human IGF-1) therapy.

### Finding 4 — The *Pappa2* knockout mouse recapitulates postnatal growth retardation

The constitutive *Pappa2* knockout (KO) mouse is a strong model of the human disease. KO mice are normal size at birth but develop postnatal growth retardation, with males ~10% and females ~25–30% lower body weight than wild-type littermates, and reduced adult femur and body length — without significant effects on bone mineral density in the mouse.

> *"The most striking phenotype of the PAPP-A2 KO mouse was postnatal growth retardation. Male and female PAPP-A2 KO mice had 10 and 25-30% lower body weight, respectively, than WT littermates. Adult femur and body length were also reduced in PAPP-A2 KO mice, but without significant effects on bone mineral density."* — [PMID: 21586553](https://pubmed.ncbi.nlm.nih.gov/21586553/)

PAPP-A2 is highly expressed in placenta, with abundant fetal, skeletal, and reproductive tissue expression, consistent with its role in longitudinal growth. The sex-dimorphic severity in the mouse (females more affected) foreshadows the sex-specific therapeutic responses discussed below.

### Finding 5 — SSDA causes insulin resistance and low bone mineral density, both rhIGF-1-responsive

Beyond short stature, patients demonstrate **insulin resistance** and **below-average bone mineral density**, both of which improve on rhIGF-1.

> *"Additionally, the patients demonstrated insulin resistance and below average bone mineral density (BMD). The PAPP-A2 deficient patients were treated with recombinant human IGF-1, resulting in improvements in growth velocity, insulin resistance, and BMD."* — [PMID: 29280739](https://pubmed.ncbi.nlm.nih.gov/29280739/)

Untargeted GC-MS metabolomics of the treated siblings revealed that rhIGF-1 most strongly altered **free fatty acid and amino acid pathways**, implicating lipid and protein metabolism as the primary systemic metabolic targets of restored IGF-1 signaling.

> *"Free fatty acids (FFAs) and amino acids showed the largest changes in the compared metabolic profiles, suggesting that rhIGF1 treatment has the greatest effects on lipid and protein metabolic pathways in the PAPP-A2 deficient subjects."* — [PMID: 30119035](https://pubmed.ncbi.nlm.nih.gov/30119035/)

### Finding 6 — PAPP-A2 acts within the IGFBP–STC2–PAPP-A (ISPa) axis; rhPAPP-A2 is an emerging targeted therapy

PAPP-A2 is one node of a broader regulatory network governing IGF bioavailability. It cleaves IGFBP-3 and -5, and its activity is inhibited by **stanniocalcin-2 (STC2)**. The related protease PAPP-A cleaves IGFBP-4 and -5 and is likewise STC2-inhibited, together forming the **IGFBP4–STC2–PAPP-A (ISPa) axis**.

> *"PAPP-A2 is a protease which cleaves IGFBP-3 and -5, while STC2 inhibits PAPP-A and PAPP-A2 activity."* — [PMID: 29280739](https://pubmed.ncbi.nlm.nih.gov/29280739/)

In *Pappa2*-deficient mice, recombinant rhPAPP-A2 (compared alongside rhGH and rhIGF-1) modulated growth-related IGF-1 signaling with sex-specific effects, supporting rhPAPP-A2 as a mechanistically direct, emerging therapeutic — with efficacy that appears female-predominant.

> *"pointing to rhPAPP-A2 as a promising drug to alleviate postnatal growth retardation underlying low IGF1 bioavailability in a female-specific manner"* — [PMID: 38589872](https://pubmed.ncbi.nlm.nih.gov/38589872/)

### Finding 7 — Diagnostic biochemical signature and the value of circulating PAPP-A2 measurement

Across all reported families, the diagnostic pattern is consistent: **elevated total IGF-1, IGFBP-3, IGFBP-5 (variable), and ALS with decreased free IGF-1**, plus progressive postnatal short stature and moderate microcephaly. Measuring circulating PAPP-A2 directly can focus the workup, because affected individuals have very low or undetectable levels.

> *"pediatric endocrinologists should measure circulating PAPP-A2 levels in the study of short stature as very low or undetectable levels of this protein can help to focus the diagnosis and treatment"* — [PMID: 34272725](https://pubmed.ncbi.nlm.nih.gov/34272725/)

> *"high circulating levels of total IGF1, IGFBP3, and the IGF acid-labile subunit (IGFALS), with decreased free IGF1 concentrations"* — [PMID: 34272725](https://pubmed.ncbi.nlm.nih.gov/34272725/)

Definitive confirmation is molecular (WES or targeted *PAPPA2* sequencing) demonstrating biallelic mutations, ideally supported by demonstration of absent *in vitro* proteolytic activity.

### Finding 8 — Differential diagnosis from other IGF ternary-complex disorders

SSDA is distinguished from the closest mimic, **ALS (IGFALS) deficiency**, by its IGF-1 profile. ALS deficiency shows **low** IGF-1 and disproportionately low IGFBP-3 with mild growth retardation, normal GH-stimulation response, a failed IGF generation test, and insulin insensitivity. PAPP-A2 deficiency shows the opposite IGF-1 direction: **high** total IGF-1/IGFBP-3/ALS but **low** free IGF-1. Both are autosomal recessive and share mild-to-moderate postnatal growth failure and insulin resistance.

> *"complete ALS deficiency is characterized by severe reduction of IGF-I and IGFBP-3 that remain low after GH treatment, associated with mild growth retardation, much less pronounced than the IGF-I deficit. Pubertal delay in boys and insulin insensitivity are common findings"* — [PMID: 20679994](https://pubmed.ncbi.nlm.nih.gov/20679994/)

### Finding 9 — Verified disease and gene identifiers

Identifiers were verified against OMIM, EBI OLS4 (MONDO), HGNC REST, and NIH GTR.

| Entity | Identifier |
|---|---|
| Disease (OMIM) | #619489 — SHORT STATURE, DAUBER-ARGENTE TYPE (SSDA) |
| Disease (MONDO) | MONDO:0859182 |
| Disease (UMLS/GTR) | C5561968 |
| Gene (OMIM) | \*619485 (*PAPPA2*) |
| Gene (HGNC) | HGNC:14615 |
| Gene (NCBI) | 60676 |
| Gene (Ensembl) | ENSG00000116183 |
| Protein (UniProt) | Q9BXP8 (pappalysin-2) |
| Cytogenetic location | 1q25.2 |

No dedicated Orphanet (ORDO), ICD-10/ICD-11, or MeSH term exists specifically for SSDA; it maps generically to growth-disorder categories (e.g., ICD-10 E34.3).

---

## Mechanistic Model / Interpretation

The disease can be understood as a single-point failure in the IGF-1 liberation cascade. The causal chain runs from genotype through impaired proteolysis to reduced tissue-level IGF-1 receptor signaling and, finally, to reduced longitudinal bone growth.

```
  Biallelic LOF PAPPA2 mutation (e.g., p.D643fs25*, p.Ala1033Val, p.Glu886*)
                          │
                          ▼
         Complete loss of PAPP-A2 proteolytic activity
                          │
                          ▼
   IGFBP-3 and IGFBP-5 are NOT cleaved (uncleaved BPs accumulate)
                          │
                          ▼
   IGF-1 remains trapped in the 150 kDa ternary complex
   (IGF-1 / IGFBP-3 or -5 / ALS)  ── reservoir cannot be "opened"
                          │
        ┌─────────────────┴──────────────────┐
        ▼                                     ▼
  ↑ Total IGF-1, IGFBP-3,               ↓ FREE (bioactive) IGF-1
    IGFBP-5, ALS, IGF-II                       │
  (paradoxical labs)                           ▼
                              ↓ IGF-1 receptor signaling at growth plate,
                                bone, and metabolic tissues
                                              │
                                              ▼
     Progressive postnatal growth failure · microcephaly · thin long
     bones · low BMD · insulin resistance
```

**Upstream vs downstream.** The upstream lesion is the loss of proteolytic activity; the elevated total binding proteins and IGF-1 are a *proximal biochemical consequence* (the reservoir backs up), while the low free IGF-1 is the *functionally decisive downstream* event that produces the clinical phenotype. This is why total IGF-1 is a poor guide to disease state and free IGF-1 (or bioactive IGF-1 assays) is essential.

**Regulatory context (ISPa axis).** PAPP-A2 operates in parallel with PAPP-A, both under negative control by STC2. This explains why the axis is physiologically tuned (e.g., PAPP-A/PAPP-A2 levels shift with obesity, exercise, meals, and other growth states) and why perturbations elsewhere in the axis (obesity, Prader-Willi syndrome, GH deficiency) produce related but distinct IGF-bioavailability phenotypes.

**Therapeutic logic.** Two rational strategies follow directly from the mechanism:
1. **Bypass** the block by delivering exogenous free IGF-1 (rhIGF-1 / mecasermin) — clinically validated, safe, and effective.
2. **Replace** the missing enzyme with rhPAPP-A2 to restore physiological IGF-1 liberation — mechanistically direct, currently experimental (mouse-stage), with apparent female-predominant efficacy.

**Comparative table — IGF ternary-complex short-stature disorders:**

| Feature | PAPP-A2 deficiency (SSDA) | ALS (IGFALS) deficiency |
|---|---|---|
| Gene | *PAPPA2* (1q25.2) | *IGFALS* |
| Inheritance | Autosomal recessive | Autosomal recessive |
| Total IGF-1 | **High** | **Low** |
| IGFBP-3 | High | Low / undetectable |
| ALS | High | Low / undetectable |
| Free IGF-1 | Low | Low |
| Growth failure | Progressive postnatal, moderate | Mild |
| Insulin | Insulin resistance | Insulin insensitivity |
| Response to rhIGF-1 | Growth, BMD, insulin sensitivity improve | — |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [26902202](https://pubmed.ncbi.nlm.nih.gov/26902202/) | *Mutations in PAPP-A2 cause short stature due to low IGF-I availability* | Founding paper; identifies the two founding mutations, proves complete loss of proteolytic activity, documents the ternary-complex mechanism (F1, F2) |
| [34272725](https://pubmed.ncbi.nlm.nih.gov/34272725/) | *PAPP-A2 deficiency in a Saudi family* | Third independent family (p.Glu886\*); establishes circulating PAPP-A2 as a diagnostic biomarker (F1, F7) |
| [27648969](https://pubmed.ncbi.nlm.nih.gov/27648969/) | *rhIGF-1 improves growth in PAPP-A2 deficiency* | Initial rhIGF-1 treatment response with increased bioactive IGF-1, no adverse effects (F3) |
| [34358737](https://pubmed.ncbi.nlm.nih.gov/34358737/) | *Adult height and long-term outcomes after rhIGF-1* | 6-year outcome: target height reached, BMD normalized (F3) |
| [21586553](https://pubmed.ncbi.nlm.nih.gov/21586553/) | *PAPP-A2 KO mouse* | Model organism recapitulating postnatal growth retardation, reduced bone length (F4) |
| [29280739](https://pubmed.ncbi.nlm.nih.gov/29280739/) | *Novel modulators PAPP-A2 and STC2* | Insulin resistance/low BMD and their rhIGF-1 response; defines STC2 inhibition (F5, F6) |
| [30119035](https://pubmed.ncbi.nlm.nih.gov/30119035/) | *Metabolomics of rhIGF1 treatment* | Lipid/protein metabolic pathway changes with therapy (F5) |
| [38589872](https://pubmed.ncbi.nlm.nih.gov/38589872/) | *Sex-based differences: rhGH, rhIGF1, rhPAPP-A2* | Emerging rhPAPP-A2 therapy, female-specific efficacy (F6) |
| [20679994](https://pubmed.ncbi.nlm.nih.gov/20679994/) | *ALS deficiency* | Differential diagnosis anchor (F8) |
| [33919940](https://pubmed.ncbi.nlm.nih.gov/33919940/) | *rmIGF-1 sex-specific bone effects in Pappa2 mice* | Supports sex-specific bone remodeling responses (context for F4/F6) |
| [41528724](https://pubmed.ncbi.nlm.nih.gov/41528724/) | *IGF-I bioavailability in isolated GHD (ISPa)* | Contextualizes the ISPa regulatory axis in a distinct disorder |
| [38662803](https://pubmed.ncbi.nlm.nih.gov/38662803/) | *Pappalysins in childhood obesity* | Physiological regulation of the axis (contrast state) |
| [28964325](https://pubmed.ncbi.nlm.nih.gov/28964325/) | *Regulation of the IGFBP-4/STC-2/PAPP-A axis* | Physiological modulators of the axis |
| [38141219](https://pubmed.ncbi.nlm.nih.gov/38141219/) | *Pappalysins in Prader-Willi syndrome* | Axis behavior in a related growth disorder |
| [28445628](https://pubmed.ncbi.nlm.nih.gov/28445628/) | *ACLSD Latin American families* | Expands ALS deficiency phenotype for differential diagnosis |
| [30717585](https://pubmed.ncbi.nlm.nih.gov/30717585/) | *Novel homozygous ALS mutation* | Additional ALS deficiency reference |

**Evidence source types:** Human clinical (case series/family studies: 26902202, 34272725, 27648969, 34358737, 29280739, 30119035); model organism (21586553, 38589872, 33919940); *in vitro* (IGFBP cleavage assays within 26902202); physiological/observational human cohorts (38662803, 28964325, 38141219, 41528724).

---

## Section-by-Section Data Compilation

### 1. Disease Information
A concise overview: SSDA is an ultra-rare Mendelian, autosomal recessive endocrine growth disorder of impaired IGF-1 bioavailability. **Synonyms:** PAPP-A2 deficiency; pappalysin-2 deficiency; short stature due to PAPP-A2 deficiency; SSDA. **Identifiers:** OMIM #619489; MONDO:0859182; UMLS C5561968; no dedicated Orphanet/ICD/MeSH term. Information is derived from aggregated disease-level resources plus individual patient family case series (not EHR-scale).

### 2. Etiology
**Causal factor:** genetic — biallelic loss-of-function *PAPPA2* mutations. **Genetic risk factors:** consanguinity (all reported families are consanguineous, yielding homozygous private mutations); carriers are heterozygous and unaffected. **Environmental / infectious / lifestyle factors:** none established as causal. **Protective factors:** none characterized. **Gene–environment interactions:** none established; the ISPa axis is physiologically modulated by nutrition, obesity, exercise and meals (PMID 28964325, 38662803), which could theoretically modify expressivity but is unproven in SSDA.

### 3. Phenotypes (with HPO suggestions)

| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Short stature / postnatal growth failure | Clinical sign | HP:0004322 (Short stature); HP:0008897 (Postnatal growth retardation) | Postnatal, progressive; moderate–severe; ~all patients |
| Microcephaly | Physical | HP:0000252 (Microcephaly) | Congenital/early; moderate; reported in most |
| Thin long bones / gracile bones | Radiographic sign | HP:0003100 (Slender long bone) | Childhood; mild–moderate |
| Decreased bone mineral density | Lab/imaging | HP:0004349 (Reduced bone mineral density) | Childhood; mild; rhIGF-1-responsive |
| Insulin resistance | Lab abnormality | HP:0000855 (Insulin resistance) | Childhood; variable; rhIGF-1-responsive |
| Elevated circulating IGF-1 | Lab abnormality | HP:0030269 (Increased circulating IGF-1) | Persistent hallmark |

**Quality of life impact:** primarily driven by short stature (psychosocial), and skeletal/metabolic morbidity; substantially improvable with rhIGF-1.

### 4. Genetic / Molecular Information
**Causal gene:** *PAPPA2* (HGNC:14615; OMIM \*619485; 1q25.2; UniProt Q9BXP8). **Pathogenic variants:** p.D643fs25\* (frameshift), p.Ala1033Val (missense), p.Glu886\* (nonsense) — all homozygous, all pathogenic, all complete loss of function. **Allele frequency:** private/ultra-rare, essentially absent from population databases (gnomAD). **Origin:** germline. **Functional consequence:** loss of function (abolished proteolytic activity). **Modifier genes:** none confirmed; STC2 is a physiological inhibitor of PAPP-A2 activity and a candidate modulator. **Epigenetic / chromosomal abnormalities:** none reported.

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors. The disease is fully genetic.

### 6. Mechanism / Pathophysiology
**Molecular pathway:** GH–IGF-1 axis; IGFBP proteolysis (metalloprotease/pappalysin activity). **Cellular processes:** longitudinal bone growth at the growth plate (chondrocyte proliferation), bone remodeling, insulin/glucose metabolism. **Protein dysfunction:** loss of metalloproteinase function of pappalysin-2. **Biochemical abnormality:** failure to cleave IGFBP-3/IGFBP-5, trapping IGF-1 in ternary complexes. **Metabolic changes:** rhIGF-1 predominantly affects free fatty acid and amino acid metabolism (PMID 30119035). **GO term suggestions:** GO:0008233 (peptidase activity), GO:0004222 (metalloendopeptidase activity), GO:0043568 (positive regulation of insulin-like growth factor receptor signaling pathway), GO:0060348 (bone development), GO:0030282 (bone mineralization). **CHEBI:** IGF-1 (peptide hormone). **CL terms:** CL:0000138 (chondrocyte), CL:0000062 (osteoblast).

### 7. Anatomical Structures Affected
**Primary:** skeletal system — long bones and growth plates (UBERON:0002481 bone tissue; UBERON:0006255 epiphyseal plate), skull/head (microcephaly, UBERON:0000033 head). **Secondary/systemic:** endocrine (GH–IGF axis), metabolic tissues (insulin resistance). **Subcellular:** secreted/extracellular protease acting in blood plasma (GO:0005576 extracellular region). **Lateralization:** bilateral/symmetric (systemic endocrine disorder).

### 8. Temporal Development
**Onset:** normal size at birth; **postnatal**, progressive growth failure emerging in infancy/childhood (insidious, chronic). **Progression:** slowly progressive short stature over childhood; **chronic lifelong** biochemical defect. **Critical period / window of opportunity:** childhood and pre-pubertal growth window — rhIGF-1 initiated during active growth allowed attainment of target adult height (PMID 34358737).

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** appears complete in biallelic homozygotes; heterozygous carriers unaffected. **Expressivity:** variable severity, with possible sex differences (mouse data show females more affected). **Consanguinity:** central — all reported families consanguineous. **Founder effects:** private family-specific mutations rather than shared founders. **Epidemiology:** ultra-rare; only a handful of families reported worldwide (Spanish, Saudi); precise prevalence/incidence not established. **Carrier frequency:** not established (essentially absent from population databases).

### 10. Diagnostics
**Biochemical signature (key screen):** high total IGF-1, IGFBP-3, IGFBP-5, ALS, IGF-II; **low free/bioactive IGF-1**. **Direct biomarker:** low/undetectable circulating PAPP-A2 (PMID 34272725). **Confirmatory genetic testing:** WES or targeted *PAPPA2* single-gene/panel sequencing demonstrating biallelic variants; functional confirmation via *in vitro* IGFBP cleavage assay (absent proteolysis). **Imaging:** radiographs (thin long bones), DXA (low BMD). **Differential diagnosis:** ALS (IGFALS) deficiency (low IGF-1), GH deficiency/insensitivity, IGF-1/IGF1R defects, other IGF-axis short-stature syndromes. **LOINC:** IGF-1, IGFBP-3, free IGF-1 assays.

### 11. Outcome / Prognosis
No excess mortality reported; the disorder is not life-threatening. **Morbidity:** short stature, low BMD, insulin resistance; psychosocial impact of short stature. **Recovery potential:** strongly favorable with rhIGF-1 — target height achieved, BMD normalized, insulin sensitivity improved, lean mass increased over 6-year treatment (PMID 34358737, 29280739). **Prognostic factors:** early initiation of rhIGF-1 during the growth window; free (not total) IGF-1 as the treatment-monitoring biomarker.

### 12. Treatment
**Established:** recombinant human IGF-1 (mecasermin), 40–120 μg/kg twice daily, escalated — improves growth velocity, height, BMD, insulin resistance; safe (no hypoglycemia observed) (PMID 27648969, 34358737, 29280739). **Emerging/experimental:** recombinant PAPP-A2 (rhPAPP-A2) — mechanistically direct enzyme replacement; mouse-stage; female-predominant efficacy (PMID 38589872). rhGH is comparatively ineffective because the bottleneck is downstream of GH. **NCIT suggestions:** Mecasermin; recombinant IGF-1 therapy. **Supportive:** monitoring of growth, BMD, glucose/insulin; genetic counseling.

### 13. Prevention
No primary prevention (genetic disorder). **Secondary prevention:** early biochemical screening in short-stature workups (measure free IGF-1 and circulating PAPP-A2 when total IGF-1 is paradoxically high). **Genetic prevention/counseling:** carrier and cascade testing in consanguineous families; prenatal/preimplantation testing feasible once the familial variant is known. **Tertiary prevention:** rhIGF-1 to forestall growth and skeletal complications.

### 14. Other Species / Natural Disease
**Taxonomy:** *Mus musculus* (NCBI:txid10090) used as model. **Orthologous gene:** murine *Pappa2*. No naturally occurring companion-animal or wildlife disease has been characterized (no OMIA entry established here). Disease mechanism (IGF-1 liberation via pappalysins) is evolutionarily conserved.

### 15. Model Organisms
**Primary model:** constitutive *Pappa2* knockout mouse (PMID 21586553) — mammalian, genetic knockout. **Phenotype recapitulation:** strong — normal birth size then postnatal growth retardation, reduced femur and body length; sex-dimorphic severity (females more affected). **Limitations:** mouse KO shows no significant BMD reduction (unlike human low BMD); conditional/tissue-specific models not central to reported work. **Applications:** dissecting IGF-1 bioavailability; testing rhIGF-1/rhGH/rhPAPP-A2 (PMID 38589872, 33919940). **Resources:** MGI.

---

## Limitations and Knowledge Gaps

- **Extremely small patient base.** Conclusions rest on a handful of consanguineous families (Spanish, Saudi). Prevalence, incidence, carrier frequency, penetrance, and the full phenotypic spectrum are not statistically established.
- **No formal Orphanet/ICD/MeSH coding**, complicating registry-based epidemiology and case-finding.
- **Treatment evidence is from uncontrolled case series**, not randomized trials. Long-term (adult) metabolic and skeletal outcomes beyond 6 years are unknown.
- **Sex-specific effects** are strongly suggested by mouse data but not systematically quantified in humans.
- **rhPAPP-A2 remains pre-clinical**; human safety, immunogenicity, dosing, and efficacy are untested.
- **Modifier genetics and the role of the STC2/ISPa axis** in modulating human disease severity are unexplored.
- **BMD discrepancy** between human (low BMD) and mouse KO (BMD unaffected) indicates the mouse does not fully capture the human skeletal phenotype.

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** for *PAPPA2* biallelic cases to define natural history, prevalence, and genotype–phenotype correlations, and to enable prospective outcome tracking.
2. **Prospective, standardized rhIGF-1 dose-response and monitoring study** using free/bioactive IGF-1 as the primary pharmacodynamic marker; assess adult height, BMD, insulin sensitivity, and lean mass with pre-specified endpoints.
3. **Advance rhPAPP-A2 toward clinical translation:** IND-enabling pharmacokinetics/pharmacodynamics, immunogenicity, and sex-stratified efficacy studies in *Pappa2* KO mice, then first-in-human evaluation.
4. **Deploy circulating PAPP-A2 assays** as a first-line screen in pediatric short-stature clinics where total IGF-1 is paradoxically elevated with low free IGF-1, and validate assay cut-offs.
5. **Investigate ISPa-axis modifiers (STC2, PAPP-A, IGFBP-4)** as potential disease modulators and alternative druggable nodes.
6. **Develop humanized or conditional mouse models** and iPSC-derived chondrocyte/osteoblast systems to resolve the BMD discrepancy and study cell-type-specific IGF-1 signaling at the growth plate.

---

## Consensus Answer

Short Stature, Dauber-Argente type (OMIM #619489; MONDO:0859182; PAPP-A2 deficiency) is an ultra-rare autosomal recessive disorder caused by biallelic loss-of-function mutations in *PAPPA2* (1q25.2), encoding the metalloproteinase pappalysin-2 that cleaves IGFBP-3 and IGFBP-5 to release bioactive IGF-1. Loss of this proteolysis traps IGF-1 in circulating ternary complexes, producing the hallmark of high total IGF-1/IGFBP-3/ALS but low free IGF-1, and causing progressive postnatal growth failure with microcephaly, thin long bones, low bone mineral density, and insulin resistance. Because the defect is IGF-1 sequestration rather than deficiency, recombinant human IGF-1 (mecasermin) safely restores growth, bone density, and insulin sensitivity, with recombinant PAPP-A2 an emerging experimental therapy.


## Artifacts

- [OpenScientist final report](Short_Stature_Dauber-Argente_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Short_Stature_Dauber-Argente_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859182` (4 mentions) - the report calls it "Disease (MONDO)"; MONDO calls it **Short stature, Dauber-Argente type**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0030269` (1 mention) - the report calls it "Increased circulating IGF-1"; HP calls it **Increased circulating insulin-like growth factor 1 concentration**, and lists "Increased serum IGF1" among its other names