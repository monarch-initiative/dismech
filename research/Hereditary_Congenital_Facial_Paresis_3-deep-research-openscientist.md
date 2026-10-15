---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T14:13:20.531389'
end_time: '2026-09-05T14:39:49.086455'
duration_seconds: 1588.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Congenital Facial Paresis 3
  mondo_id: MONDO:0013880
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
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
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
  path: Hereditary_Congenital_Facial_Paresis_3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hereditary_Congenital_Facial_Paresis_3-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Congenital Facial Paresis 3
- **MONDO ID:** MONDO:0013880 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Congenital Facial Paresis 3** covering all of the
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

# Hereditary Congenital Facial Paresis Type 3 (HCFP3) — Disease Characteristics Report

**MONDO:** MONDO:0013880 · **OMIM:** #614744 · **Category:** Mendelian (autosomal recessive)

> Evidence base: HCFP3 is an ultra-rare Mendelian disorder described in only a handful of families worldwide. Consequently, much of the mechanistic detail is derived from the mouse model (*Hoxb1*-/-) and from a small number of human case reports/series. Evidence source types are flagged throughout as **[human clinical]**, **[mouse]**, **[in vitro]**, or **[computational]**. Where a canonical resource (OMIM/Orphanet/HPO) would normally supply information but no primary datum was retrievable in this investigation, the item is marked *"not established / not retrieved."*

---

## 1. Disease Information

HCFP3 is a **congenital cranial dysinnervation disorder (CCDD)** characterized by non-progressive, usually **bilateral weakness/paralysis of the muscles of facial expression** due to maldevelopment of the **seventh cranial nerve (facial nerve, CN VII)** and its brainstem motor nucleus. It is present from birth and frequently accompanied by hearing loss, strabismus, feeding difficulties, and orofacial/ear dysmorphism. **[human clinical]** (PMID 27144914, 22770981, 39235314)

**Key identifiers**
- **MONDO:** MONDO:0013880
- **OMIM:** 614744 (phenotype)
- **Gene:** HOXB1 — OMIM 142968; HGNC:5111; NCBI Gene 3211; Ensembl ENSG00000120094; UniProt P14653; locus 17q21.32
- **Orphanet:** Hereditary congenital facial paresis (ORPHA:91517 group; HCFP3 subtype)
- **ICD-11:** LA05 / 8B88.0-type congenital cranial nerve / facial nerve disorders (congenital facial palsy); **ICD-10:** Q07.8 (other specified congenital malformations of nervous system) — mapping approximate.
- **MeSH:** "Facial Paralysis"; "Cranial Nerve Diseases"; related MeSH "Mobius Syndrome" (differential).

**Synonyms / alternative names:** HCFP3; Hereditary congenital facial paresis, type 3; Congenital facial palsy, HOXB1-related; Facial paresis, hereditary congenital, 3; (broader group) hereditary congenital facial palsy.

**Data source type:** Aggregated disease-level knowledge (OMIM/Orphanet/HPO) plus individual patient case reports (EHR-style descriptions of small families), **not** large registry/EHR cohorts.

---

## 2. Etiology

**Primary cause (genetic):** Biallelic (homozygous or compound heterozygous) pathogenic variants in **HOXB1**, a homeodomain transcription factor. HOXB1 is "the only known causative gene for HCFP" (HCFP3). **[human clinical]** (PMID 27144914)

**Genetic risk factors**
- **Causal variants:** HOXB1 loss-of-function and homeodomain missense alleles (Section 4).
- **Consanguinity:** Strong contributor — recessive disease enriched in consanguineous/endogamous families (e.g., Moroccan consanguineous family; German-American conservative isolate). **[human clinical]** (PMID 27144914, 22770981)
- **Founder effect:** A founder Arg207Cys allele segregates in a "conservative German American population." **[human clinical]** (PMID 22770981)
- **Susceptibility/modifier loci:** Not established.

**Environmental risk factors:** None identified. HCFP3 is a monogenic developmental disorder; unlike acquired/syndromic congenital facial palsy, it is not attributable to birth trauma, teratogens (e.g., misoprostol/Möbius association), or ischemia. Congenital onset means the causal event is embryonic hindbrain patterning.

**Protective factors (genetic/environmental):** None established. In a recessive disorder, a single wild-type HOXB1 allele is effectively protective (carriers are unaffected — PMID 27144914).

**Gene–environment interactions:** None documented; disease is fully genetically determined by biallelic HOXB1 dysfunction.

---

## 3. Phenotypes

| Phenotype | Type | Onset | Severity/Course | Frequency | HPO suggestion |
|---|---|---|---|---|---|
| Bilateral facial (CN VII) palsy | Clinical sign | Congenital | Non-progressive, stable; variable severity | Defining (~100%) | HP:0010628 Facial palsy; HP:0000260 (bilateral) |
| Impaired facial expression / weak eye closure, drooling | Physical manifestation | Congenital | Stable | High | HP:0000317 Facial features / HP:0000508 Ptosis (variable) |
| Feeding/sucking difficulties (infancy) | Symptom | Neonatal | Often improves | Common | HP:0011968 Feeding difficulties; HP:0002033 Poor suck |
| Hearing loss (sensorineural and/or conductive) | Lab/clinical sign | Congenital | Stable | Frequent | HP:0000365 Hearing impairment |
| Strabismus | Clinical sign | Congenital | Stable | Frequent | HP:0000486 Strabismus |
| Ear malformations / low-set or dysmorphic ears | Physical | Congenital | Stable | Variable | HP:0000377 Abnormal pinna morphology; HP:0000369 Low-set ears |
| Orofacial dysmorphism (e.g., upturned nose, upper-lip/philtrum changes) | Physical | Congenital | Stable | Variable | HP:0000463 Anteverted nares |
| Facial nerve axonal neuropathy (± nerve hypoplasia) | Lab (electrophysiology/imaging) | Congenital | Stable | Reported | HP:0009830 Peripheral neuropathy |
| Preserved eye abduction (CN VI intact) — distinguishes from Möbius | Discriminating sign | — | — | Characteristic | (absence of HP:0031747-type abducens palsy) |

**[human clinical]** sources: PMID 27144914, 22770981, 39235314. Note Brugnoli 2025 (PMID 39235314) describes a case with **facial nerve axonal neuropathy without nerve hypoplasia** and **preserved ocular motor skills**, broadening the imaging/electrophysiology spectrum.

**Quality-of-life impact:** Facial diplegia impairs emotional expression, eye protection (risk of exposure keratopathy), articulation, oral competence (drooling, feeding), and social/psychological well-being; hearing loss adds communication/developmental burden. **Measured evidence:** subjects with congenital facial weakness (includes HCFP) have significantly worse oral health-related quality of life than matched controls — **OHIP-14 13.11 ± 8.11 vs 4.46 ± 4.98** (Liberton 2024, PMID 38791829). No HCFP3-specific EQ-5D/SF-36 data exist (broader CFW/facial-palsy inference).

---

## 4. Genetic / Molecular Information

**Causal gene:** **HOXB1** (HGNC:5111; OMIM 142968; 17q21.32) — homeobox transcription factor, HOX family, master regulator of hindbrain antero-posterior patterning. **[human clinical]** (PMID 27144914)

**Pathogenic variants reported**
| Variant (cDNA / protein) | Type | Zygosity / origin | Functional consequence | Reference |
|---|---|---|---|---|
| c.619C>T, p.(Arg207Cys) | Missense (homeodomain Arg5) | Homozygous, **founder** (German-American isolate) | Disrupts DNA minor-groove contact; destabilizes HOXB1:PBX1:DNA complex; altered transcriptional activity **[computational + in vitro]** | PMID 22770981 |
| p.Arg207His (historical) | Missense (same residue) | Homozygous | Same residue class; altered cofactor/DNA binding | (reviewed in 27144914) |
| c.66C>G, p.(Tyr22*) | Nonsense (truncating) | Homozygous, consanguineous Moroccan family | **Loss of function** (first bona fide LOF allele) | PMID 27144914 |
| Two novel compound heterozygous variants | (per report) | Compound het, by exome sequencing | Consistent with LOF; axonal neuropathy phenotype | PMID 39235314 |

- **ACMG classification:** Reported alleles are pathogenic/likely pathogenic; segregation with disease, rarity, and functional data support classification (query ClinVar for current status).
- **Allele frequency:** Causal alleles are extremely rare/absent in gnomAD (private/founder); precise frequencies not retrieved here.
- **Somatic vs germline:** **Germline** (constitutional developmental disorder).
- **Functional class:** **Loss of function** unifies missense (impaired DNA/cofactor binding) and nonsense (truncation) alleles — "all HOXB1 variants reported so far also have severe impact on activity of this transcriptional regulator." **[human clinical / in vitro]** (PMID 27144914)

**Modifier genes:** None established. Candidate interacting partners at protein level include **PBX1** (obligate HOX cofactor) and **MEIS** proteins; HOXA1 is a paralog acting in overlapping hindbrain programs (HOXA1 mutations cause a distinct CCDD, Bosley-Salih-Alorainy/Athabascan brainstem dysgenesis).

**Epigenetic information:** No disease-specific methylation/histone data for HCFP3 (not established).

**Chromosomal abnormalities:** None characteristic for HCFP3 (single-gene disorder; no recurrent CNV/translocation).

**HCFP locus landscape (nosological context).** HCFP is genetically heterogeneous:
- **HCFP3 (OMIM 614744):** *HOXB1*, 17q21.32, **autosomal recessive** (this disease).
- **HCFP1 (OMIM 601471):** maps to 3q21-q22; resolved in 2023 as **heterozygous duplications of a neuron-specific GATA2 regulatory region (two enhancers + one silencer) and noncoding silencer SNVs** (some impair NR2F1 binding) — autosomal dominant. A humanized mouse extends Gata2, favoring inner-ear efferent over facial-branchiomotor fate, rescued by conditional *Gata3* loss. **[human/mouse]** (PMID 37386251)
- **HCFP2 (OMIM 604185):** maps to 10q21.3-q22.1; gene not yet identified — autosomal dominant. (PMID 27144914)
- **Other dominant HCFP gene:** *MEPE* frameshift p.(Gln425Lysfs*38) with mixed hearing loss in a four-generation family. **[human clinical]** (PMID 30287925)

**Convergent mechanism across subtypes:** all HCFP genes act on **maldevelopment of rhombomere-4–derived facial branchiomotor neurons (FBMNs)** — the same lineage disrupted by HOXB1 loss — so a CFW/HCFP diagnostic gene panel should include *HOXB1*, the *GATA2* regulatory region, and *MEPE*.

---

## 5. Environmental Information

- **Environmental factors:** None causal (purely genetic developmental disorder).
- **Lifestyle factors:** Not applicable to disease causation.
- **Infectious agents:** None. (Distinguish from acquired facial palsy such as Bell's palsy [HSV], Lyme disease, otitis media — these are **differential diagnoses**, not HCFP3.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic HOXB1 loss-of-function** (nonsense truncation, or homeodomain missense that cripples DNA/cofactor binding) **results in** absent or non-functional HOXB1 transcription factor in the embryonic hindbrain. **[human clinical/in vitro]** (PMID 27144914, 22770981)
2. This **leads to** failure to **maintain rhombomere 4 (r4) identity** — r4 patterning is initiated but not sustained (molecular markers appear then fade). **[mouse]** (PMID 8967950)
3. Loss of r4 identity **results in** mis-specification of r4-derived **facial branchiomotor (FBM) neurons** and **contralateral vestibuloacoustic (CVA) efferent neurons**. **[mouse]** (PMID 8967950)
4. Mis-specified motor neurons **differentiate but fail to migrate** to their normal positions; instead they form an atypically migrating motor nucleus. **[mouse]** (PMID 8967950)
5. This aberrant development **leads to** **subsequent loss of the facial motor nerve** (hypoplasia/aplasia of CN VII nucleus and nerve). **[mouse]** (PMID 8967950)
6. Absent/deficient facial motor innervation **results in** congenital **bilateral facial muscle paralysis** (impaired expression, eye closure, oral competence). **[human clinical]** (PMID 22770981)
   - **Branch (auditory):** disruption of r4-derived vestibuloacoustic efferents and inner-ear developmental programs **contributes to** **hearing loss**. **[mouse/human]** (PMID 8967950, 22770981) *(inferred link between CVA lineage and auditory deficit)*
   - **Branch (ocular):** associated **strabismus** arises from developmental co-involvement, though eye **abduction (CN VI)** is characteristically **spared**, distinguishing HCFP3 from Möbius syndrome. **[human clinical]** (PMID 27144914)
   - **Branch (variant-specific):** some human cases show **facial nerve axonal neuropathy without frank nuclear/nerve hypoplasia**, indicating the lesion can manifest as an axonal/dysinnervation phenotype rather than complete agenesis. **[human clinical]** (PMID 39235314)

The human founder mutation "recapitulates the phenotype of Hoxb1-/- mice," directly bridging the mouse mechanism to human disease. **[human/mouse]** (PMID 22770981)

### Upstream regulatory context (why r4, and what maintains HOXB1)
HOXB1's r4-restricted expression is set up by a **retinoic acid (RA; CHEBI:15367) morphogen gradient**: RA produced by **Raldh2** in paraxial mesoderm induces Hoxb1 up to r4 through 3′/5′ RA-response elements, while **Cyp26** RA-degrading enzymes sharpen the r3/r5 boundaries. In *Raldh2*-/- embryos, Hoxb1-expressing cells scatter instead of forming a defined r4. **[mouse]** (PMID 15872003, 10654602). Once induced, HOXB1 **maintains its own expression** via an r4 **autoregulatory element (b1-ARE)** driven by **HOXB1:PBX1** heterodimers, further tuned by **TALE cofactors (PREP1/MEIS)** and SOX/OCT complexes; HOXB1 is a stronger activator than its paralog HOXA1. **[in vitro/mouse]** (PMID 11278854, 10654609). Pathogenic homeodomain variants (Arg207Cys) cripple precisely the PBX1/DNA interactions that sustain this loop — mechanistically linking genotype to the "identity-not-maintained" phenotype in step 2 above.

### Category checklist mapped to the chain
- **Molecular pathways:** Upstream **retinoic-acid signaling** (Raldh2/Cyp26 gradient) patterns r4; the core lesion is in the **HOX/PBX–MEIS/PREP transcriptional regulatory network** governing hindbrain segmentation and cranial motor neuron identity (Reactome "Activation of HOX genes"; developmental gene-regulatory network). No classic signaling cascade (Wnt/MAPK/mTOR) is the proximal lesion; the defect is transcription-factor–level. **[mouse/in vitro]** (PMID 15872003, 11278854, 10654609)
- **Protein dysfunction:** Homeodomain Arg207 (= conserved Arg5) normally contacts thymine in the DNA minor groove via hydrogen bonding/electrostatics; mutation destabilizes the **HOXB1:PBX1:DNA** ternary complex → altered target-gene transcription. Nonsense allele → no functional protein. **[computational + in vitro]** (PMID 22770981)
- **Cellular processes:** Cell-fate specification, **neuronal migration** (tangential migration of branchiomotor neurons), maintenance of segmental identity, neuronal survival. **[mouse]** (PMID 8967950)
- **Immune / metabolic / oxidative mechanisms:** Not involved (developmental, non-inflammatory, non-metabolic).
- **Molecular profiling / single-cell / omics:** No disease-specific transcriptomic/proteomic/metabolomic datasets for HCFP3 (not established); mechanistic data come from marker/lineage studies in mouse.

**Upstream vs downstream:** HOXB1 loss (upstream) → r4 identity failure → FBM/CVA mis-specification/migration failure → CN VII nucleus/nerve loss → facial paralysis (downstream clinical readout).

**Ontology suggestions:** GO:0021610 facial nerve morphogenesis; GO:0021612 facial nerve structural organization; GO:0001764 neuron migration; GO:0048704 embryonic skeletal/segment specification; GO:0006357/0006355 regulation of transcription by RNA Pol II; GO:0021546 rhombomere development. **CL:** CL:0000100 motor neuron; CL:0011001 spinal/branchiomotor motor neuron. **UBERON:** UBERON:0005396 rhombomere 4; UBERON:0001647 facial nerve; UBERON:0002894 hindbrain/rhombomere.

---

## 7. Anatomical Structures Affected

- **Organ/system level:** Central & peripheral **nervous system** — brainstem (pons/medulla, hindbrain) and cranial nerve VII; **musculoskeletal** (muscles of facial expression, secondary); **auditory system** (inner ear/CN VIII pathway); **visual/oculomotor** (strabismus).
- **Primary structure:** Facial motor nucleus and **facial nerve (CN VII)** — UBERON:0001647.
- **Secondary involvement:** Muscles of facial expression (denervation), ear structures (hearing loss, pinna dysmorphism), extraocular alignment.
- **Tissue/cell level:** **Neural tissue**; specifically **branchiomotor motor neurons** of rhombomere 4 (CL:0000100 motor neuron), vestibuloacoustic efferent neurons.
- **Subcellular level:** **Nucleus** (GO:0005634) — site of HOXB1 transcription-factor action on chromatin/DNA.
- **Localization & lateralization:** Bilateral (often symmetric) facial involvement; brainstem hindbrain r4 territory. **[human clinical]** (PMID 22770981)

---

## 8. Temporal Development

- **Onset:** **Congenital** (embryonic hindbrain maldevelopment); facial weakness evident at birth/neonatal period (feeding/sucking difficulty, incomplete eye closure). **[human clinical]** (PMID 39235314)
- **Onset pattern:** Static/developmental (not acute or acquired).
- **Progression:** **Non-progressive / stable** over life (a dysinnervation/malformation, not a degenerative process). No disease staging.
- **Course:** Lifelong, chronic, stable. Feeding difficulties may improve with maturation; facial weakness persists.
- **Remission:** None spontaneous; deficits are structural. Interventions are supportive/reconstructive (Section 12).
- **Critical period:** The vulnerable/opportunity window is **embryonic hindbrain segmentation** (r4 identity maintenance); postnatally the developmental lesion is fixed.

---

## 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal recessive** (HCFP3). Contrast: HCFP1 (OMIM 601471) and HCFP2 (OMIM 604185) are autosomal dominant. **[human clinical]** (PMID 39235314, 27144914)
- **Penetrance:** Appears complete in reported biallelic individuals; heterozygous carriers are unaffected. **[human clinical]** (PMID 27144914)
- **Expressivity:** Variable (severity of hearing loss, strabismus, dysmorphism, presence/absence of nerve hypoplasia vary between and within families). **[human clinical]** (PMID 39235314)
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effect:** Yes — Arg207Cys founder allele in a conservative German-American population. **[human clinical]** (PMID 22770981)
- **Consanguinity:** Prominent contributor (homozygous alleles in consanguineous/endogamous families). **[human clinical]** (PMID 27144914, 22770981)
- **Carrier frequency:** Not established (ultra-rare; population-specific).
- **Epidemiology:** HCFP overall is very rare; HCFP3 specifically is reported in only a small number of families/cases worldwide. Precise prevalence/incidence per 100,000 **not established**. Broader hereditary congenital facial palsy is estimated at roughly ~2 per million births (order-of-magnitude, group-level; not HCFP3-specific).
- **Sex ratio:** No strong sex bias expected for an autosomal recessive disorder; formal data not established.
- **Geographic distribution:** Case clusters reported in a German-American isolate (founder), a consanguineous Moroccan family, Russian patients (Murtazina 2023, PMID 38203298), and Italian (Brugnoli 2025). Distribution reflects reporting/founder/consanguinity rather than true endemicity.

---

## 10. Diagnostics

**Clinical evaluation**
- Recognition of **congenital, non-progressive, bilateral facial weakness** with preserved eye abduction; assess feeding, eye closure, hearing, ocular alignment, ear/facial morphology. **[human clinical]** (PMID 27144914)

**Genetic testing (definitive)**
- **Exome sequencing (ES/WES)** is the demonstrated diagnostic modality (used to identify HOXB1 variants). **[human clinical]** (PMID 39235314, 27144914, 22770981)
- **Targeted HOXB1 single-gene / CCDD gene-panel testing** appropriate once phenotype suggests HCFP3.
- **Genome sequencing (WGS)** where ES is uninformative.
- In individuals with congenital facial paralysis, preserved ocular motor skills, and confirmed facial-nerve axonal neuropathy, **"HOXB1 variants and therefore a diagnosis of HCFP3 should be primarily considered."** **[human clinical]** (PMID 39235314)

**Electrophysiology / functional tests**
- **Facial nerve conduction, blink reflex, ± needle EMG:** HCFP (and Möbius) subjects show **low-amplitude CN VII responses without other neuropathic or myopathic findings**, distinguishing them from generalized-neuropathy CFW (e.g., TUBB3 polyneuropathy) or myopathic CFW (Carey-Fineman-Ziter). May also show axonal facial neuropathy. **[human clinical]** (PMID 33389762, 39235314)
- **Audiometry / BAER (ABR):** to detect and characterize hearing loss (sensorineural/conductive).
- **Ophthalmologic exam:** strabismus, tear-film/exposure assessment.

**Imaging**
- **High-resolution MRI (brainstem/CN VII, IAC):** grades facial-nerve maldevelopment **0–4** (0 normal → 1 unilateral hypoplasia → 2 unilateral aplasia → 3 bilateral aplasia/hypoplasia → 4 with additional cranial-nerve involvement) and can reveal inner/middle/external-ear anomalies; in HCFP3 the nerve may be **hypoplastic/aplastic OR normal-appearing despite axonal neuropathy** (variable). **[human clinical]** (PMID 30074067, 39235314)

**Biomarkers / lab chemistry / biopsy:** No specific blood/urine biomarker; diagnosis is clinical + molecular. No pathognomonic histopathology.

**Clinical criteria & differential diagnosis:** Distinguish from **Möbius syndrome** (adds CN VI abduction deficit), acquired facial palsy (birth trauma, Bell's palsy, infection), **HOXA1-related** CCDDs, **TUBB3**-related CFW (adds generalized sensorimotor axonal polyneuropathy on EDx), **Carey-Fineman-Ziter** and other myopathic CFW (myopathic EDx findings), CHARGE syndrome, hemifacial microsomia/oculo-auriculo-vertebral spectrum, and other syndromic congenital facial weakness. Preserved abduction + **isolated low-amplitude CN VII** pattern without neuropathic/myopathic features favors HCFP. **[human clinical]** (PMID 27144914, 33389762)

**Screening:** Carrier/cascade testing within affected families; prenatal/preimplantation testing feasible once the familial HOXB1 genotype is known. Not part of population newborn screening.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **Normal life expectancy**; HCFP3 is not life-limiting (no cardiorespiratory/visceral fatal component). Disease-specific mortality negligible.
- **Morbidity/disability:** Chronic functional impairments — impaired facial expression and eye closure (exposure keratopathy risk), speech/articulation difficulty, oral competence/feeding issues in infancy, hearing impairment, strabismus/amblyopia risk. Psychosocial impact from facial diplegia; measurably reduced oral health-related QoL (OHIP-14 13.11 vs 4.46, PMID 38791829). **[human clinical]** (PMID 27144914, 39235314, 38791829)
- **Recovery potential:** The primary facial-nerve deficit is structural and **does not resolve spontaneously**; supportive/rehabilitative and reconstructive measures improve function. Feeding difficulties often improve with age.
- **Prognostic factors:** Severity of nerve hypoplasia, degree of hearing loss, presence of associated anomalies; earlier multidisciplinary intervention improves functional/QoL outcomes.
- **Prognostic biomarkers:** None established.

---

## 12. Treatment

There is **no disease-modifying or curative therapy**; management is **supportive, rehabilitative, and reconstructive**, delivered by a multidisciplinary team. (No pharmacotherapy targets the underlying transcription-factor defect.)

- **Pharmacotherapy:** No specific drug. Ocular surface protection: **lubricating eye drops/ointments** (artificial tears) to prevent exposure keratopathy. Pharmacogenomics: not applicable.
- **Surgical / interventional:**
  - **Facial reanimation surgery** — **free functional muscle transfer**, most commonly **segmental free gracilis muscle transfer (FGMT)** neurotized by the **masseteric (trigeminal) nerve** or via **cross-face nerve grafts**, is the standard smile-reanimation technique for non-resolving congenital bilateral facial paralysis (the HCFP/Möbius category). **[human clinical]** (PMID 30166122, 33637466). Pediatric outcomes: ~**84%** achieve active gracilis contraction with mean **commissure excursion gains ~9.7 mm at 1 year** (PMID 40738135); gains are **maintained/improved at 5–13 years** (PMID 33191114); 1-stage and 2-stage bilateral approaches give comparable outcomes (PMID 40100160). *(Series are Möbius-dominated but the reconstructive principles apply directly to HCFP3.)* NCIT: facial reanimation; free muscle flap transfer; cross-face nerve grafting.
  - **Ophthalmic:** strabismus surgery; eyelid procedures (gold-weight implant, tarsorrhaphy) for lagophthalmos/eye protection.
  - **Otologic/audiologic:** hearing aids or bone-conduction devices; cochlear implantation if indicated for severe SNHL.
- **Supportive / rehabilitative:** Feeding support in infancy; **speech and language therapy** (articulation, oral competence); **physical/occupational/facial neuromuscular retraining therapy**; early developmental support; ophthalmology and audiology follow-up.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** None developed; congenital developmental fixation of the lesion limits gene-therapy applicability.
- **Experimental treatments / trials:** No HCFP3-specific interventional trials identified (ClinicalTrials.gov — not retrieved for this specific ultra-rare entity).
- **Treatment strategy:** Individualized, phenotype-directed multidisciplinary care (facial reanimation timing, eye protection, hearing habilitation, speech therapy) + genetic counseling.

**NCIT suggestions:** facial reanimation / nerve graft procedures; strabismus surgery; hearing aid; cochlear implant; supportive/palliative care; physical therapy; speech therapy.

---

## 13. Prevention

- **Primary prevention:** Not possible for an inherited developmental disorder other than via **reproductive genetic options** — **genetic counseling**, **carrier testing** in at-risk families/consanguineous couples, **prenatal diagnosis** and **preimplantation genetic testing (PGT-M)** once the familial HOXB1 variants are known.
- **Secondary prevention (early detection/complication avoidance):** Early recognition to institute **eye protection** (prevent exposure keratopathy), **hearing habilitation** (support language development), and **strabismus/amblyopia management** in the critical visual-development window.
- **Tertiary prevention:** Ongoing corneal protection, feeding/nutrition support, speech therapy, and timely facial reanimation to limit functional and psychosocial complications.
- **Immunization / public-health / environmental / prophylaxis:** Not applicable (non-infectious, non-environmental).
- **Counseling:** Autosomal recessive recurrence risk = **25%** for a couple who are both carriers; emphasize consanguinity risk and founder-population screening. **[human clinical]** (PMID 27144914)

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* (NCBI Taxon 9606); disease-model *Mus musculus* (Taxon 10090).
- **Orthologous gene:** Mouse **Hoxb1** (NCBI Gene 15407; MGI); zebrafish **hoxb1a/hoxb1b** (ZFIN) with cofactor **pbx4** (*lazarus*). Highly conserved homeodomain (human Arg207 = conserved homeodomain Arg5). **[mouse/zebrafish]** (PMID 22770981, 8967950, 12645925)
- **Natural disease in other species / breeds:** No naturally occurring HOXB1-facial-paresis disease catalogued (OMIA — not retrieved); no VBO breed association.
- **Comparative biology:** The mouse **Hoxb1-/-** phenotype (loss of r4 identity, FBM/CVA mis-migration, facial motor nerve loss) closely mirrors the human disorder — human founder mutation "recapitulates the phenotype of Hoxb1-/- mice," demonstrating deep evolutionary conservation of the hindbrain segmentation/branchiomotor program. **[human/mouse]** (PMID 22770981, 8967950)
- **Zoonotic potential / cross-species transmission:** Not applicable (genetic disorder).

---

## 15. Model Organisms

- **Primary model:** **Mouse — Hoxb1 knockout (Hoxb1-/-)** [mammalian, genetic knockout]. Key resource: MGI. **[mouse]** (PMID 8967950)
- **Model characteristics / phenotype recapitulation:** Faithfully reproduces the core human mechanism — r4 identity is initiated but not maintained; FBM and CVA neurons are mis-specified and **fail to migrate**, forming an atypically migrating nucleus with **loss of the facial motor nerve** → facial paralysis analog. Explicitly stated to correlate "extensively" with the human phenotype. **[mouse]** (PMID 8967950, 22770981)
- **Second vertebrate model — zebrafish (*Danio rerio*, NCBI Taxon 7955):** *hoxb1a* interacts genetically with *lazarus/pbx4* to control **facial (CN VII) motor neuron migration**; genetic mosaic analysis shows both act **primarily cell-autonomously within the facial motor neurons** (with a minor non-cell-autonomous component). This independently validates the HOX/PBX-driven FBMN migration mechanism disrupted in HCFP3. **[zebrafish]** (PMID 12645925). Orthologs: *hoxb1a*, *hoxb1b*, *pbx4*. Resource: ZFIN.
- **Model types available:** Constitutive knockout (Studer 1996); zebrafish morphant/mutant (Cooper 2003); paralog/compound studies (Hoxa1/Hoxb1) and knock-in swap experiments exist in the developmental-biology literature (not detailed here). A **humanized HCFP1 (GATA2-regulatory) mouse** exists for the related subtype (PMID 37386251). Conditional/humanized HOXB1 alleles — resources via MGI/IMPC (not enumerated in this investigation).
- **Limitations:** Mouse constitutive knockout captures nerve/nucleus maldevelopment but does not fully model human associated features (hearing loss severity, strabismus, human-specific dysmorphism) or the milder axonal-neuropathy-without-hypoplasia human presentations.
- **Applications:** Dissecting hindbrain segmentation, branchiomotor neuron specification/migration, and HOX/PBX transcriptional control; platform for genotype-phenotype correlation.
- **In vitro / computational:** In vitro DNA–protein binding assays and molecular modeling of the Arg207Cys homeodomain–DNA interaction. **[in vitro/computational]** (PMID 22770981)
- **Resources:** MGI (Hoxb1), IMPC/IMSR for alleles.

---

## Summary Answer

**Hereditary Congenital Facial Paresis type 3 (HCFP3; OMIM #614744, MONDO:0013880)** is an ultra-rare autosomal-recessive congenital cranial dysinnervation disorder caused by biallelic loss-of-function of the hindbrain transcription factor **HOXB1** (17q21.32; e.g., founder p.Arg207Cys and nonsense p.Tyr22*). Loss of HOXB1 prevents maintenance of rhombomere-4 identity, causing mis-specification and failed migration of facial branchiomotor neurons and consequent hypoplasia/dysfunction of the facial motor nucleus and nerve — producing congenital, non-progressive **bilateral facial paralysis** with variable hearing loss, strabismus, feeding difficulty and orofacial/ear anomalies, while eye abduction (CN VI) is characteristically spared (distinguishing it from Möbius syndrome). Diagnosis is by exome/HOXB1 sequencing; there is no cure, and management is multidisciplinary and supportive (eye protection, hearing habilitation, speech therapy, facial reanimation) with autosomal-recessive genetic counseling (25% recurrence risk).

## Key Findings (with evidence)
1. **Genetic cause:** biallelic HOXB1 variants → HCFP3 (autosomal recessive), the only established HCFP gene (PMID 27144914, 22770981, 39235314).
2. **Variant spectrum:** founder missense p.Arg207Cys, nonsense p.Tyr22* (LOF), and compound-het alleles; unified by loss of function (PMID 22770981, 27144914, 39235314).
3. **Mechanism:** HOXB1 loss → failed r4 identity maintenance → FBM/CVA neuron mis-migration → facial motor nerve loss → bilateral facial palsy (mouse Hoxb1-/-; PMID 8967950, 22770981).
4. **Phenotype:** bilateral facial palsy + hearing loss + strabismus + orofacial/feeding anomalies, with preserved eye abduction (PMID 22770981, 27144914, 39235314).

## Supported vs. Refuted Hypotheses
- **Supported:** HOXB1 LOF is causal and recessive; mechanism is developmental (r4/branchiomotor); mouse model recapitulates human disease.
- **Refuted / not applicable:** environmental/infectious/metabolic/immune etiology; somatic origin; progressive or degenerative course; gene–environment interaction.

## Limitations & Future Directions
- Ultra-rare disease: prevalence/incidence, penetrance/expressivity ranges, sex ratio, and gnomAD carrier frequencies are **not precisely established**.
- Mechanistic branch linking HOXB1/r4 to human hearing loss and strabismus is **partly inferred** from mouse/lineage data.
- No omics (transcriptomic/proteomic) profiling exists for HCFP3 tissue.
- Future work: broaden genotype–phenotype catalog (ClinVar/GeneMatcher), define natural history/QoL, refine imaging/electrophysiology correlates (hypoplasia vs axonal neuropathy), and explore conditional/humanized models.

---
*Evidence classes: [human clinical] case reports/families & surgical series; [mouse] Hoxb1/Raldh2 knockouts; [in vitro] DNA-binding/enhancer assays; [computational] molecular modeling. Primary PMIDs: 22770981 (Webb 2012, founder HOXB1), 27144914 (Vogel 2016, LOF nonsense), 8967950 (Studer 1996, Hoxb1-/- mouse), 39235314 (Brugnoli 2025, compound-het), 38203298 (Murtazina 2023, phenotype expansion), 15872003 (Sirbu 2005, RA→Hoxb1 r4), 10654602 (Niederreither 2000, Raldh2 hindbrain), 11278854 (Di Rocco 2001, b1-ARE HOXB1:PBX1), 10654609 (Ferretti 2000, PREP1/MEIS), 30556292 (Bell 2019, Möbius differential), 37386251 (Tenney 2023, HCFP1/GATA2 regulatory), 30287925 (Schrauwen 2019, MEPE HCFP), 33389762 (Lehky 2021, electrodiagnostics), 30074067 (Mohammad 2018, MRI grading), 38791829 (Liberton 2024, OHRQoL), 12645925 (Cooper 2003, zebrafish hoxb1a/pbx4), 30166122 / 33637466 / 40738135 / 33191114 / 40100160 (facial reanimation).*


## Artifacts

- [OpenScientist final report](Hereditary_Congenital_Facial_Paresis_3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hereditary_Congenital_Facial_Paresis_3-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005634` (1 mention) - the report calls it "Nucleus", "Subcellular level:** **Nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005634` - called "Nucleus", "Subcellular level:** **Nucleus"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

27 of 29 terms resolved to a current term; the rest could not be looked up either way.