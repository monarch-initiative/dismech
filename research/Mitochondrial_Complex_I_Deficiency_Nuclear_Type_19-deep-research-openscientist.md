---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-14T20:46:30.660094'
end_time: '2026-09-14T21:04:55.977525'
duration_seconds: 1105.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mitochondrial Complex I Deficiency Nuclear Type 19
  mondo_id: MONDO:0032624
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
citation_count: 22
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 23
  validator_version: 0.2.1
term_validation:
  total_terms: 48
  verified: 45
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 24
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032624
    reported_labels:
    - MONDO
    ontology_label: mitochondrial complex I deficiency, nuclear type 19
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0005747
    ontology_label: obsolete mitochondrial respiratory chain complex I
    replaced_by: GO:0045271
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
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_19-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_19-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency Nuclear Type 19
- **MONDO ID:** MONDO:0032624 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency Nuclear Type 19** covering all of the
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

# Mitochondrial Complex I Deficiency, Nuclear Type 19 (MC1DN19): A Comprehensive Disease Characteristics Report

**Disease:** Mitochondrial Complex I Deficiency, Nuclear Type 19
**MONDO ID:** MONDO:0032624 · **OMIM:** #618241 · **Causal gene:** *FOXRED1* (HGNC:26927)
**Category:** Mendelian (autosomal recessive)
**Report date:** 2026-09-14

---

## Summary

**Mitochondrial Complex I Deficiency, Nuclear Type 19 (MC1DN19)** is an ultra-rare, autosomal-recessive primary mitochondrial disorder caused by biallelic loss-of-function variants in *FOXRED1*, a nuclear-encoded gene at chromosome 11q24.2 that encodes a 486-amino-acid FAD-dependent flavoprotein functioning as a **complex I-specific molecular assembly chaperone**. When both *FOXRED1* alleles are disrupted, mitochondrial respiratory chain complex I (NADH:ubiquinone oxidoreductase) fails to assemble and stabilize, producing an **isolated complex I deficiency**. The resulting collapse of oxidative phosphorylation (OXPHOS) and ATP synthesis, together with elevated reactive oxygen species (ROS) and lactic acidosis, drives energy failure in high-demand neurons and produces the bilateral symmetric brainstem and basal-ganglia neurodegeneration that defines **Leigh syndrome (subacute necrotizing encephalomyelopathy)**.

Clinically, MC1DN19 presents as a **severe congenital-to-infantile mitochondrial encephalopathy**: developmental delay and regression, hypotonia evolving to rigidity, epileptic seizures and myoclonus, movement disorder (athetosis), cerebral visual impairment, and in some patients hypertrophic cardiomyopathy — with characteristic elevated blood/CSF lactate and symmetric T2-hyperintense lesions on MRI. The disorder is **extremely rare** (only ~5 reported patients by 2019, with a handful of additional cases since) and was first identified in a consanguineous Iranian-Jewish pedigree. Prognosis is **poor**, with a progressive course punctuated by infection-triggered acute exacerbations, typically fatal in infancy or early childhood.

**There is no curative therapy.** Management is multidisciplinary and supportive (seizure control, nutrition, avoidance of mitochondrial toxins). Empirical riboflavin/cofactor supplementation is mechanistically rational — FOXRED1 is itself an FAD flavoprotein — but evidence remains heterogeneous and unproven for this specific genotype. Experimental strategies (AAV gene replacement, chronic hypoxia / "hypoxia-in-a-pill," and succinate-bypass prodrug NV354) show promise in *Ndufs4*-knockout mouse models of complex I deficiency/Leigh syndrome but have not been tested in FOXRED1-specific systems. This report integrates 11 confirmed findings drawn from 28 reviewed papers to populate a structured disease knowledge-base entry.

---

## 1. Disease Information

MC1DN19 is one of the nuclear-gene subtypes within the large, genetically heterogeneous group of **isolated mitochondrial complex I deficiencies**. Complex I deficiency is the most commonly reported mitochondrial disorder presenting in childhood ([PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/)), and accounts for ~32% of pediatric respiratory-chain defects ([PMID: 15466086](https://pubmed.ncbi.nlm.nih.gov/15466086/)). The "nuclear type 19" designation reflects that the causal gene (*FOXRED1*) is encoded in the nuclear genome rather than mitochondrial DNA, and that it is the 19th nuclear locus assigned an OMIM complex-I-deficiency subtype.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM | #618241 (Mitochondrial complex I deficiency, nuclear type 19) |
| MONDO | MONDO:0032624 |
| Causal gene (HGNC) | *FOXRED1*, HGNC:26927 |
| NCBI Gene | 55572 |
| Ensembl | ENSG00000110074 |
| UniProt | Q96CU9 |
| Cytoband | 11q24.2 (GRCh38 chr11:126,269,024–126,278,131) |

**Synonyms / alternative names:** Mitochondrial complex I deficiency nuclear type 19 (MC1DN19); FOXRED1-related complex I deficiency; FOXRED1-related mitochondrial encephalopathy; FOXRED1-related Leigh syndrome. Clinically the phenotype overlaps with, and is often diagnosed as, **Leigh syndrome / subacute necrotizing encephalomyelopathy** and infantile mitochondrial encephalopathy.

**Source of information:** The evidence base is **aggregated disease-level** knowledge derived from a small number of individual case reports and functional studies (e.g., [PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/), [PMID: 41412221](https://pubmed.ncbi.nlm.nih.gov/41412221/)), supplemented by larger Leigh-syndrome and complex-I-deficiency cohorts used to frame prognosis and diagnostic criteria. There is no EHR-scale patient dataset for this ultra-rare disorder.

---

## 2. Etiology

**Primary cause — genetic.** MC1DN19 is caused by **biallelic (homozygous or compound heterozygous) pathogenic variants in *FOXRED1***. Fassone et al. (2010) identified a homozygous *FOXRED1* mutation (c.1054C>T; p.R352W) in a consanguineous Iranian-Jewish child with infantile-onset encephalomyopathy via homozygosity mapping, and demonstrated causality functionally ([PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/)): *"We describe a patient with complex I deficiency caused by mutation of the molecular chaperone FOXRED1."* Additional cases document compound heterozygous variants, e.g., c.850T>C (p.C284R)/c.1054C>T (p.R352W) and c.1054C>T (p.R352W)/c.3dup (p.I2Dfs\*35) ([PMID: 41412221](https://pubmed.ncbi.nlm.nih.gov/41412221/)).

**Genetic risk factors.** The disease is monogenic; the causal variants are themselves the risk factors. **Consanguinity** is a major risk factor, as demonstrated by the founding consanguineous pedigree ([PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/)). No modifier or susceptibility loci have been established for MC1DN19 specifically.

**Environmental risk factors.** No environmental exposure causes the disease. However, **intercurrent infections** are well-documented triggers of acute metabolic decompensation in Leigh syndrome ([PMID: 24731534](https://pubmed.ncbi.nlm.nih.gov/24731534/)), and a hypothesized mechanistic branch proposes that **protein-, choline-, or folate-deficient diets** may aggravate FOXRED1-related pathology by depleting glutathione and dysregulating nitric oxide metabolism ([PMID: 26235939](https://pubmed.ncbi.nlm.nih.gov/26235939/)).

**Protective factors.** None are established. There are no known protective alleles or dietary/lifestyle exposures that reduce risk in carriers or patients.

**Gene–environment interactions.** Lemire (2015) proposed a specific GxE model: *"Loss of FOXRED1, coupled with protein, choline and/or folate-deficient diets results in the depletion of glutathione, the dysregulation of nitric oxide metabolism and the peroxynitrite-mediated inactivation of complex I"* ([PMID: 26235939](https://pubmed.ncbi.nlm.nih.gov/26235939/)). This remains a hypothesis. Empirically, infection-induced catabolic stress precipitates crises ([PMID: 24731534](https://pubmed.ncbi.nlm.nih.gov/24731534/)).

---

## 3. Phenotypes

MC1DN19 produces a **congenital/neonatal-to-infantile, progressive, multisystem** phenotype dominated by neurological features (Leigh-type encephalopathy), with metabolic and occasional cardiac involvement. Curated HPO annotations for OMIM:618241 / MONDO:0032624 (HPO/JAX, sourced to [PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/) and Calvo 2010, PMID 20818383) plus supporting cohort data yield the following spectrum.

| Phenotype | HPO term | Type | Onset / severity / frequency |
|---|---|---|---|
| Congenital onset | HP:0003577 | Clinical course | Congenital |
| Neonatal onset | HP:0003623 | Clinical course | Neonatal |
| Global developmental delay | HP:0001263 | Neurodevelopmental | Early, severe, common |
| Hypotonia | HP:0001252 | Neurological sign | Early; may evolve to rigidity |
| Rigidity | HP:0002063 | Neurological sign | Later course |
| Loss of ambulation / inability to walk | HP:0002505 / HP:0002540 | Motor regression | Progressive |
| Absent / poor speech | HP:0001344 / HP:0002465 | Neurological | Common |
| Seizure | HP:0001250 | Neurological | ~40% in Leigh cohorts |
| Myoclonus | HP:0001336 | Neurological | Variable |
| Athetosis | HP:0002305 | Movement disorder | Variable |
| Cerebellar atrophy | HP:0001272 | Neuroimaging | Present |
| Delayed/decreased myelination | HP:0012448 | Neuroimaging | Present |
| Ventriculomegaly | HP:0002119 | Neuroimaging | Present |
| Secondary microcephaly | HP:0005484 | Head/neck | Present |
| Cerebral visual impairment | HP:0100704 | Ophthalmologic | Common |
| Optic atrophy | HP:0000648 | Ophthalmologic | Very rare |
| Hypertrophic cardiomyopathy | HP:0001639 | Cardiovascular | Subset; ~40% cardiac involvement in pediatric mito disease |
| Respiratory insufficiency | HP:0002093 | Respiratory | Late/crisis |
| Feeding difficulties | HP:0011968 | Digestive | Common |
| Scoliosis | HP:0002650 | Skeletal | Variable |
| Lactic acidosis | HP:0003128 | Laboratory | Characteristic |
| Hypoglycemia | HP:0001943 | Laboratory | Variable |
| Decreased mitochondrial complex I activity | HP:0011923 | Cellular/lab | 2/2 patients in index reports |
| Irritability | HP:0000737 | Behavioral | Present |
| Gait disturbance | HP:0001288 | Neurological | Present |
| Autosomal recessive inheritance | HP:0000007 | Inheritance | — |

Ophthalmologic signs — nystagmus/roving eye movements and strabismus — are common **presenting** features of complex I Leigh disease: *"Nystagmus or roving eye movements were the most common ophthalmologic manifestations as a presenting symptom of disease"* ([PMID: 18486820](https://pubmed.ncbi.nlm.nih.gov/18486820/)). Cardiac disease affects ~40% of pediatric mitochondrial-disease patients ([PMID: 15466086](https://pubmed.ncbi.nlm.nih.gov/15466086/)).

**Quality-of-life impact:** Given congenital/infantile onset with global developmental delay, motor regression to loss of ambulation, absent speech, seizures, feeding difficulty, and cerebral visual impairment, affected children have **profound impairment of daily functioning** across all domains and require full caregiver dependence. No disease-specific EQ-5D/SF-36 data exist for this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene:** *FOXRED1* — "FAD dependent oxidoreductase domain containing 1" (HGNC:26927; NCBI Gene 55572; Ensembl ENSG00000110074; UniProt Q96CU9), located at **11q24.2**, protein-coding, encoding a **486-amino-acid** FAD-dependent oxidoreductase / flavoprotein ([PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/)).

**Pathogenic variants (biallelic; all reported variants are germline):**

| Variant (cDNA) | Protein | Type | Notes |
|---|---|---|---|
| c.1054C>T | p.R352W | Missense | Recurrent; index homozygous case (PMID 20858599) |
| c.850T>C | p.C284R | Missense | Compound het (PMID 41412221) |
| c.3dup | p.I2Dfs\*35 | Frameshift | Compound het (PMID 41412221) |
| — | p.N430S | Missense | Reported |
| — | p.Q232\* | Nonsense | Reported |

**Variant classification:** reported alleles are **pathogenic / likely pathogenic** per ACMG/AMP, supported by functional evidence (knockdown/rescue) and segregation. **Variant classes** span missense, nonsense, and frameshift.

**Allele frequency / population constraint:** gnomAD shows *FOXRED1* is **not haploinsufficiency-constrained**, consistent with a recessive loss-of-function mechanism: pLI = 1.8×10⁻¹⁶ (≈0), LOEUF (oe_lof upper) = 1.13, observed/expected LoF = 0.90 (52 observed vs 57.8 expected), missense Z = 0.62. Pathogenic LoF alleles are individually rare, giving a low carrier frequency.

**Functional consequences:** **loss of function** — reduced complex I assembly and enzymatic activity. *"Silencing of FOXRED1 in human fibroblasts resulted in reduced complex I steady-state levels and activity, while lentiviral-mediated FOXRED1 transgene expression rescued complex I deficiency in the patient fibroblasts"* ([PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/)).

**Modifier genes / epigenetics / chromosomal abnormalities:** None established for MC1DN19. Oligogenic modification has been speculated in related complex-I subtypes (e.g., NDUFS3 with retinal-gene variants, PMID 42232357) but not for FOXRED1. No epigenetic signatures or large-scale chromosomal rearrangements are implicated. **CHEBI:** FAD cofactor = CHEBI:57692.

---

## 5. Environmental Information

MC1DN19 is a **monogenic disorder with no environmental or infectious cause**. Relevant non-genetic factors are **triggers/aggravators** rather than causes:

- **Infections** precipitate acute metabolic decompensation and hospitalization ([PMID: 24731534](https://pubmed.ncbi.nlm.nih.gov/24731534/)). Illustratively, a patient with a related complex I deficiency (NDUFV1) developed severe dengue hemorrhagic fever with rapid neurological deterioration, underscoring the vulnerability of complex-I-deficient patients to infectious stress ([PMID: 42499220](https://pubmed.ncbi.nlm.nih.gov/42499220/)).
- **Dietary deficiency (protein, choline, folate)** is hypothesized to exacerbate FOXRED1-related pathology via glutathione depletion and peroxynitrite-mediated complex I inactivation ([PMID: 26235939](https://pubmed.ncbi.nlm.nih.gov/26235939/)).
- **Mitochondrial toxins** (e.g., certain drugs) should be avoided as a matter of standard mitochondrial-disease management.

No occupational, radiation, pollution, or pathogen etiology applies.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic FOXRED1 loss-of-function variants** are inherited → **results in** absent/non-functional FOXRED1 flavoprotein chaperone.
2. Loss of FOXRED1 chaperone activity → **leads to** failure of **mid-to-late-stage complex I assembly** and reduced steady-state complex I (demonstrated: siRNA knockdown reduces complex I; lentiviral rescue restores it — [PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/); patient-cell complex I *disassembly* — [PMID: 41412221](https://pubmed.ncbi.nlm.nih.gov/41412221/)).
3. Complex I disassembly → **results in** deficient **NADH:ubiquinone oxidoreductase activity** (isolated complex I deficiency).
4. Deficient complex I → **impairs OXPHOS electron transport and ATP synthesis**, and **increases ROS**; alters mitochondrial membrane potential and causes **NAD imbalance** (demonstrated in patient PBMCs — [PMID: 41412221](https://pubmed.ncbi.nlm.nih.gov/41412221/)).
5. Energy failure + oxidative stress → **produces lactic acidosis** (anaerobic shift) and **energy crisis in high-metabolic-demand neurons**.
6. Neuronal energy failure → **causes bilateral symmetric neurodegeneration** of the brainstem and basal ganglia (Leigh syndrome lesions).
7. Regional neurodegeneration → **manifests as** developmental regression, epilepsy/myoclonus, movement disorder, visual impairment, and (in a subset) hypertrophic cardiomyopathy and respiratory failure.

**Branch (hypothesized, inferred not demonstrated):** FOXRED1 loss (a flavoprotein related to sarcosine/N-methyl amino acid dehydrogenases), when combined with dietary methyl-donor deficiency → **glutathione depletion + nitric-oxide dysregulation → peroxynitrite-mediated inactivation of residual complex I** ([PMID: 26235939](https://pubmed.ncbi.nlm.nih.gov/26235939/)), amplifying the primary assembly defect.

**Branch (from model organisms):** downstream of complex I deficiency, **region-specific innate immune activation** (interferon/RIG-I signaling in the olfactory bulb) and **GABAergic pallidal (Lhx6) circuit dysfunction** contribute to inflammation and epileptic events, respectively ([PMID: 41636927](https://pubmed.ncbi.nlm.nih.gov/41636927/); [PMID: 41321311](https://pubmed.ncbi.nlm.nih.gov/41321311/)). These are demonstrated in *Ndufs4*-KO mice, inferred for FOXRED1.

```
FOXRED1 biallelic LoF
        │ (loss of chaperone)
        ▼
Failed mid-late Complex I assembly ──► ↓ Complex I steady-state
        │
        ▼
↓ NADH:ubiquinone oxidoreductase activity (isolated CI deficiency)
        │
        ├──► ↓ OXPHOS / ↓ ATP ──┐
        ├──► ↑ ROS, ↓ Δψm, NAD  │
        └──► ↑ lactate ─────────┤
                                 ▼
                 Neuronal energy failure (brainstem, basal ganglia)
                                 │
        ┌────────────────────────┼───────────────────────┐
        ▼                        ▼                        ▼
  Encephalopathy /        Epilepsy / myoclonus     Hypertrophic
  developmental           (pallidal Lhx6 circuit)  cardiomyopathy,
  regression, movement                              respiratory failure
  disorder, visual loss
```

**Molecular pathways / processes:** OXPHOS (KEGG hsa00190), mitochondrial respiratory chain complex I assembly. **GO biological process suggestions:** mitochondrial respiratory chain complex I assembly (GO:0032981); ATP synthesis coupled electron transport (GO:0042773); response to oxidative stress (GO:0006979); NADH dehydrogenase (ubiquinone) activity (GO:0008137, molecular function). **Cellular processes:** bioenergetic failure, oxidative-stress-mediated neuronal injury, apoptosis/necrosis of vulnerable neurons, neuroinflammation (innate immune activation, inferred). **Protein dysfunction:** loss of function of an FAD-dependent flavoprotein assembly chaperone. **Metabolic changes:** energy metabolism collapse, lactic acidosis, NAD⁺/NADH imbalance. **Biochemical abnormality:** enzyme (complex I) deficiency. **Cell types (CL):** neurons — especially brainstem and basal-ganglia neurons (CL:0000540 neuron); GABAergic neurons (CL:0000617); cardiomyocytes (CL:0000746).

---

## 7. Anatomical Structures Affected

**Organ level (primary):** brain — specifically **brainstem** (UBERON:0000955 brain; UBERON:0002298 brainstem) and **basal ganglia** (UBERON:0002420). MRI series in Leigh syndrome show **brainstem involvement in 100% and basal ganglia in 62.5%** of children ([PMID: 36412346](https://pubmed.ncbi.nlm.nih.gov/36412346/)). Additional CNS sites: cerebellum (UBERON:0002037), cerebral white matter, dentate nuclei, optic nerves, thalamus, spinal cord.

**Secondary organ involvement:** heart (hypertrophic cardiomyopathy; UBERON:0000948), skeletal muscle (myopathy; UBERON:0001134), eye/visual pathway.

**Body systems:** nervous system (primary), cardiovascular, musculoskeletal, respiratory (insufficiency in crises), and metabolic.

**Tissue / cell level:** nervous tissue (neurons, especially of brainstem/basal ganglia), cardiac muscle. **Cell Ontology:** neuron (CL:0000540), GABAergic neuron (CL:0000617), cardiomyocyte (CL:0000746).

**Subcellular level:** **mitochondrion** (GO:0005739), specifically the **mitochondrial inner membrane** (GO:0005743) on the matrix face, where FOXRED1 localizes and complex I is embedded; **respiratory chain complex I** (GO:0005747). UniProt Q96CU9 localizes FOXRED1 to the mitochondrial inner membrane (matrix side).

**Localization / lateralization:** lesions are characteristically **bilateral and symmetric** (a diagnostic hallmark of Leigh syndrome — [PMID: 27574709](https://pubmed.ncbi.nlm.nih.gov/27574709/)).

---

## 8. Temporal Development

**Onset:** **congenital to infantile.** HPO annotations specify congenital onset (HP:0003577) and neonatal onset (HP:0003623). In the broader Leigh-syndrome framework, *"The median age of disease onset was 7 months, with 80.8% of patients presenting by the age of 2 years"* ([PMID: 24731534](https://pubmed.ncbi.nlm.nih.gov/24731534/)). Onset pattern is typically **subacute/insidious with episodic decompensation**.

**Progression:** **progressive and relapsing**, with a stepwise pattern of developmental regression punctuated by acute exacerbations. *"Approximately 44% of patients experienced acute exacerbations requiring hospitalisation during the previous year, mainly due to infections"* ([PMID: 24731534](https://pubmed.ncbi.nlm.nih.gov/24731534/)). Presence of pathological signs at birth and a history of epileptic seizures are associated with higher occurrence of acute exacerbations/relapses, and elevated CSF lactate correlates with worse outcome ([PMID: 24731534](https://pubmed.ncbi.nlm.nih.gov/24731534/)).

**Disease course:** chronic, lifelong (though life is typically short), progressive with relapsing-remitting acute crises. **Critical periods:** early infancy is both the period of highest vulnerability and the window in which intervention (in future gene/metabolic therapies) would need to act before irreversible neurodegeneration. **Remission:** no spontaneous remission; supportive care can stabilize between crises but does not reverse neurodegeneration.

---

## 9. Inheritance and Population

**Inheritance pattern:** **autosomal recessive** (HP:0000007; OMIM #618241). The founding case was homozygous in a consanguineous Iranian-Jewish pedigree ([PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/)): *"a homozygous mutation in FOXRED1 in a child who presented with infantile-onset encephalomyopathy."* Both compound heterozygous and homozygous genotypes are reported.

**Epidemiology:** **ultra-rare.** Barbosa-Gouveia et al. (2019) noted *"To date, only five patients with mitochondrial complex I deficiency due to mutations in"* FOXRED1 had been reported ([PMID: 31434271](https://pubmed.ncbi.nlm.nih.gov/31434271/)); additional cases have appeared since (e.g., [PMID: 41412221](https://pubmed.ncbi.nlm.nih.gov/41412221/)). No formal prevalence/incidence figure exists. For context, complex I deficiency is the most common childhood mitochondrial disorder ([PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/)) and the most common respiratory-chain defect in pediatric mitochondrial disease (~32% — [PMID: 15466086](https://pubmed.ncbi.nlm.nih.gov/15466086/)); overall childhood mitochondrial disease incidence is ~1 in 5,000–10,000, of which FOXRED1 is a tiny fraction.

**Penetrance / expressivity:** biallelic pathogenic genotypes appear **fully penetrant** for severe infantile disease in reported cases; expressivity is **variable** (e.g., variable cardiac involvement, seizure burden). **Genetic anticipation:** not applicable (not a repeat-expansion disorder). **Germline mosaicism:** not reported. **Founder effects:** none established beyond the single consanguineous index family. **Consanguinity:** an important risk factor. **Carrier frequency:** low, consistent with the small gnomAD LoF allele count (52 observed).

**Population demographics:** no established ethnic predilection beyond the consanguineous index pedigree; **no sex bias** (autosomal recessive); onset in infancy. No geographic clustering of specific variants has been demonstrated.

---

## 10. Diagnostics

Diagnosis follows the **Leigh syndrome diagnostic framework** confirmed by biochemistry and molecular genetics.

**Clinical / biochemical tests:**
- **Elevated lactate** in blood and/or CSF is a core criterion ([PMID: 27574709](https://pubmed.ncbi.nlm.nih.gov/27574709/)).
- **Isolated complex I (NADH:ubiquinone oxidoreductase) deficiency** measured enzymatically in fibroblasts/muscle and by **blue-native PAGE** (reduced complex I assembly and activity) ([PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/); [PMID: 41412221](https://pubmed.ncbi.nlm.nih.gov/41412221/)). HPO: decreased activity of mitochondrial complex I (HP:0011923).

**Imaging:** MRI is pivotal. Leigh criteria require *"characteristic features on neuroimaging (bilateral symmetrical hyperintensities in brainstem, basal ganglia, dentate nuclei, and optic nerves on T2-weighted MRI)"* ([PMID: 27574709](https://pubmed.ncbi.nlm.nih.gov/27574709/)). In an MRI series, brainstem was involved in 100% and basal ganglia in 62.5% of LS children, with **diffusion restriction marking acute/active lesions** ([PMID: 36412346](https://pubmed.ncbi.nlm.nih.gov/36412346/)). MR spectroscopy may show a lactate peak.

**Clinical criteria (Leigh syndrome):** progressive disorder with motor/intellectual delay-regression; brainstem and/or basal-ganglia signs; raised blood/CSF lactate; plus characteristic neuroimaging, typical neuropathology, or an affected sibling ([PMID: 27574709](https://pubmed.ncbi.nlm.nih.gov/27574709/)).

**Genetic testing (confirmatory):** **whole-exome or whole-genome sequencing** is the definitive test. Targeted "MitoExome" sequencing of mtDNA plus exons of ~1,000 nuclear mitochondrial genes gave a firm diagnosis in 24% and candidate genes in 31% of infantile OXPHOS-disease patients ([PMID: 22277967](https://pubmed.ncbi.nlm.nih.gov/22277967/)): *"We performed 'MitoExome' sequencing of the mitochondrial DNA (mtDNA) and exons of ~1000 nuclear genes encoding mitochondrial proteins."* Nuclear gene panels for complex I deficiency / Leigh syndrome include *FOXRED1*. mtDNA testing is used to exclude maternally-inherited causes but is **negative** in MC1DN19 (nuclear gene).

**Differential diagnosis:** other nuclear and mtDNA complex I deficiency subtypes (e.g., *NDUFV1*, *NDUFS3*, *NDUFS4*, *ACAD9*), MELAS, LHON, combined OXPHOS deficiencies, and other causes of Leigh syndrome (>110 genes). Distinguishing feature: **isolated complex I deficiency + biallelic FOXRED1 variants**.

**Screening:** no newborn screening exists. **Cascade/carrier testing** of relatives and **prenatal/preimplantation genetic testing** are feasible once the familial biallelic variants are known.

---

## 11. Outcome / Prognosis

**Prognosis is poor.** MC1DN19 is a **severe, early-onset, progressive** disorder that is typically fatal in infancy or early childhood, consistent with its Leigh-syndrome phenotype. The multicenter Leigh cohort (n=130; 77 with pathogenic mutations) documented median onset at 7 months, frequent seizures (~40%), and infection-triggered acute exacerbations requiring hospitalization in ~44% of patients in a single year ([PMID: 24731534](https://pubmed.ncbi.nlm.nih.gov/24731534/)).

**Prognostic factors (worse outcome):** pathological signs at birth, history of epileptic seizures (both associated with more acute exacerbations/relapses), and **elevated CSF lactate** (correlates with worse outcome) ([PMID: 24731534](https://pubmed.ncbi.nlm.nih.gov/24731534/)).

**Morbidity / function:** profound and multi-domain — motor (loss of ambulation), communication (absent speech), cognitive (global developmental delay), visual (cerebral visual impairment), feeding (requiring support), plus seizure burden. **Complications:** respiratory insufficiency, recurrent infections, cardiac dysfunction, failure to thrive, and status epilepticus. **Recovery potential:** neurodegeneration is largely irreversible; supportive care stabilizes but does not restore lost function.

**Prognostic biomarkers:** CSF lactate (established); complex I residual activity and lesion activity on diffusion MRI are informative but not formally validated for FOXRED1.

---

## 12. Treatment

**There is no curative therapy.** Only limited symptomatic therapies exist for complex I deficiency ([PMID: 42265384](https://pubmed.ncbi.nlm.nih.gov/42265384/)).

**Supportive / standard care (NCIT: Supportive Care):** multidisciplinary management — **anti-seizure medication** for epilepsy, **nutritional support** (including gastrostomy where indicated), physical/occupational/speech rehabilitation, treatment of intercurrent infections, cardiac surveillance, and **avoidance of mitochondrial toxins**. Prompt management of infection-triggered crises is critical given their frequency ([PMID: 24731534](https://pubmed.ncbi.nlm.nih.gov/24731534/)).

**Pharmacotherapy / cofactors:** **Riboflavin** (vitamin B2), a precursor of the complex I flavin cofactors FMN and FAD, is a mechanistically rational option — **especially relevant here because FOXRED1 is itself an FAD-dependent flavoprotein**. A systematic review identified 45 riboflavin-responsive complex-I cases (2 new + 43 literature), with the strongest evidence in ACAD9-related cardiomyopathy/myopathy and some NDUFV1/NDUFV2 leukoencephalopathy ([PMID: 42476091](https://pubmed.ncbi.nlm.nih.gov/42476091/)): *"No curative therapies exist. Riboflavin, a precursor of CI cofactors FMN and FAD, is a potential treatment, but evidence is heterogeneous and formal guidelines are lacking."* Empirical **mitochondrial cofactor cocktails** (e.g., coenzyme Q10, thiamine, other vitamins) are commonly used without high-quality evidence.

**Experimental therapeutics (preclinical, in *Ndufs4*-KO complex I / Leigh models):**

| Approach | Finding | Reference |
|---|---|---|
| AAV9 gene therapy + focused ultrasound | Extends survival, improves brain/cardiac function | [PMID: 41572892](https://pubmed.ncbi.nlm.nih.gov/41572892/) |
| Chronic hypoxia (11% O₂) | Prevents Leigh-like brain disease | [PMID: 40770507](https://pubmed.ncbi.nlm.nih.gov/40770507/), [PMID: 42427540](https://pubmed.ncbi.nlm.nih.gov/42427540/) |
| "Hypoxia-in-a-pill" (GBT601 ± PT2399) | Extends median lifespan from 62 → 105–158 days; rescues neuro phenotypes | [PMID: 42427540](https://pubmed.ncbi.nlm.nih.gov/42427540/) |
| Succinate prodrug NV354 (complex II bypass) | *"prevents brain lesions and late-stage motor dysfunction in mitochondrial complex I deficiency"* | [PMID: 41704780](https://pubmed.ncbi.nlm.nih.gov/41704780/) |
| STN inhibition (circuit-targeted) | Reduces epileptic events | [PMID: 41321311](https://pubmed.ncbi.nlm.nih.gov/41321311/) |
| Encapsulated mitochondrial transplantation | Rescues bioenergetic defects in mito-disease models | [PMID: 41856111](https://pubmed.ncbi.nlm.nih.gov/41856111/) |

None of these have been validated specifically for FOXRED1/MC1DN19; all are **experimental**. **Pharmacogenomics, targeted therapies, immunotherapies, and approved gene/cell/RNA therapies:** none applicable/approved. **NCIT term suggestions:** Supportive Care; Riboflavin; Gene Therapy; Anticonvulsant Agent; Nutritional Support.

---

## 13. Prevention

Because MC1DN19 is a monogenic recessive disorder, prevention is **genetic and reproductive**, not lifestyle-based.

- **Primary prevention:** not possible for a de novo affected fetus, but **genetic counseling** for at-risk couples (especially consanguineous families) is central. Given autosomal recessive inheritance, carrier couples have a 25% recurrence risk per pregnancy.
- **Reproductive options:** **carrier screening**, **prenatal diagnosis**, and **preimplantation genetic testing (PGT)** once the familial variants are known.
- **Secondary prevention:** early molecular diagnosis (WES/WGS) enables earlier supportive intervention; there is no population newborn screening.
- **Tertiary prevention (complication avoidance):** aggressive prevention/early treatment of infections (major crisis triggers), avoidance of mitochondrial toxins, seizure control, nutritional optimization, and cardiac monitoring.
- **Immunization / public-health / environmental interventions:** standard childhood vaccination is advisable to reduce infection-triggered crises; no disease-specific vaccine or public-health measure applies.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring FOXRED1-related disease is documented in companion animals or wildlife (no OMIA entry identified for FOXRED1). Human = *Homo sapiens* (NCBI:txid9606).
- **Orthologous genes:** *FOXRED1* is conserved in mammals; mouse *Foxred1* (Mus musculus, NCBI:txid10090) is the direct ortholog. FOXRED1 belongs to a family related to sarcosine/N-methyl amino acid dehydrogenases ([PMID: 26235939](https://pubmed.ncbi.nlm.nih.gov/26235939/)).
- **Natural disease / veterinary relevance:** none established. Comparative pathology relies on **engineered** models rather than naturally occurring animal disease.
- **Evolutionary conservation:** complex I and its assembly machinery are deeply conserved across eukaryotes, supporting cross-species mechanistic relevance.
- **Transmission / zoonosis:** not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

**FOXRED1-specific models are cellular / in vitro:**
- **siRNA knockdown in human fibroblasts** reduced complex I steady-state and activity, with **lentiviral FOXRED1 re-expression rescuing** the deficiency in patient fibroblasts — the definitive causality demonstration ([PMID: 20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/)).
- **Patient-derived fibroblasts and PBMCs** recapitulate complex I disassembly, respiration defects, altered membrane potential, ROS accumulation, and NAD imbalance ([PMID: 41412221](https://pubmed.ncbi.nlm.nih.gov/41412221/)).
- Additional broadly applicable complex-I-deficiency models include **cybrids** and **human iPSC-derived neurons** (review — [PMID: 42265384](https://pubmed.ncbi.nlm.nih.gov/42265384/)).

**No dedicated *Foxred1* mouse** is established in the reviewed literature.

**Canonical mammalian surrogate — the *Ndufs4*-knockout mouse** (constitutive and conditional) — is the workhorse model of isolated complex I deficiency / Leigh syndrome. It recapitulates progressive encephalopathy, brainstem/olfactory-bulb lesions, epilepsy, cardiac dysfunction, and early death ([PMID: 41572892](https://pubmed.ncbi.nlm.nih.gov/41572892/)): *"the Ndufs4-knockout (KO) mouse."* Key mechanistic and therapeutic insights from this model:

| Model finding | Reference |
|---|---|
| AAV9 + focused-ultrasound gene therapy extends survival | [PMID: 41572892](https://pubmed.ncbi.nlm.nih.gov/41572892/) |
| Pallidal Lhx6 GABAergic circuit dysfunction drives seizures | [PMID: 41321311](https://pubmed.ncbi.nlm.nih.gov/41321311/) |
| Region-specific innate immune (interferon/RIG-I) activation in olfactory bulb | [PMID: 41636927](https://pubmed.ncbi.nlm.nih.gov/41636927/) |
| Late-stage cardiometabolic perturbation | [PMID: 41532297](https://pubmed.ncbi.nlm.nih.gov/41532297/) |
| NDUFS4 links complex I to T-cell immunity | [PMID: 41573538](https://pubmed.ncbi.nlm.nih.gov/41573538/) |
| Chronic hypoxia / hypoxia-in-a-pill / NV354 are protective | [PMID: 42427540](https://pubmed.ncbi.nlm.nih.gov/42427540/), [PMID: 41704780](https://pubmed.ncbi.nlm.nih.gov/41704780/) |

**Model limitations:** *Ndufs4*-KO models a **subunit** defect, not an **assembly-factor** defect like FOXRED1; it therefore captures downstream complex I deficiency and Leigh pathology but not FOXRED1-specific assembly biology. Cellular models capture biochemistry but not the whole-organism neurodegenerative trajectory. Translational relevance is further limited by tissue-specific effects and species differences ([PMID: 42265384](https://pubmed.ncbi.nlm.nih.gov/42265384/)).

---

## Mechanistic Model / Interpretation

MC1DN19 is a clean example of an **assembly-factor loss-of-function mitochondrial disease**. FOXRED1 does not form part of the mature complex I holoenzyme; instead it acts transiently as an **FAD-dependent flavoprotein chaperone at the mid-to-late stages of complex I assembly**. Biallelic loss removes this chaperone, so complex I fails to assemble/stabilize, yielding an **isolated** (as opposed to combined) respiratory-chain deficiency. The downstream pathophysiology — energy failure, ROS, lactic acidosis, and selective vulnerability of high-demand brainstem and basal-ganglia neurons — is the shared final common pathway of Leigh syndrome, which is why FOXRED1 patients are clinically indistinguishable from other complex-I Leigh subtypes and why *Ndufs4*-KO mice serve as a mechanistic surrogate despite a different upstream lesion.

Two features make FOXRED1 mechanistically distinctive and therapeutically suggestive: (1) its **FAD dependence** provides a rational, if unproven, basis for riboflavin/flavin-cofactor therapy; and (2) the **hypothesized glutathione/nitric-oxide/peroxynitrite branch** links FOXRED1 to a redox-and-diet-modifiable amplifying loop, implying that antioxidant/methyl-donor status could modulate severity. Both hypotheses are actionable and testable.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [20858599](https://pubmed.ncbi.nlm.nih.gov/20858599/) | *FOXRED1 mutated in infantile-onset mitochondrial encephalopathy* | **Foundational** — establishes FOXRED1 as cause; knockdown/rescue proof; chaperone identity; epidemiology context |
| [41412221](https://pubmed.ncbi.nlm.nih.gov/41412221/) | *Biallelic FOXRED1 mutations cause… complex I disassembly and basal ganglia degeneration* | Confirms biallelic inheritance, mechanism (disassembly, ROS, NAD imbalance), new variants, DEE phenotype |
| [26235939](https://pubmed.ncbi.nlm.nih.gov/26235939/) | *Glutathione metabolism links FOXRED1 to complex I deficiency* | Leigh syndrome link; hypothesized redox/diet GxE branch |
| [24731534](https://pubmed.ncbi.nlm.nih.gov/24731534/) | *Multicenter study on Leigh syndrome* | Prognosis, onset timing, infection-triggered exacerbations, prognostic factors |
| [27574709](https://pubmed.ncbi.nlm.nih.gov/27574709/) | *Novel mtDNA mutation… Leigh syndrome* | Leigh diagnostic criteria (lactate + symmetric MRI) |
| [36412346](https://pubmed.ncbi.nlm.nih.gov/36412346/) | *MRI abnormalities in Leigh syndrome* | Imaging distribution (brainstem 100%, BG 62.5%); diffusion restriction |
| [22277967](https://pubmed.ncbi.nlm.nih.gov/22277967/) | *Molecular diagnosis with targeted NGS* | MitoExome/WES diagnostic yield |
| [42476091](https://pubmed.ncbi.nlm.nih.gov/42476091/) | *Riboflavin therapy in complex I deficiency* | Cofactor therapy evidence; "no curative therapies exist" |
| [42265384](https://pubmed.ncbi.nlm.nih.gov/42265384/) | *Complex I deficiency-associated diseases and models* | No cure; model landscape review |
| [42427540](https://pubmed.ncbi.nlm.nih.gov/42427540/) | *Second-generation hypoxia-in-a-pill* | Experimental therapy; lifespan extension in Ndufs4-KO |
| [41704780](https://pubmed.ncbi.nlm.nih.gov/41704780/) | *Succinate prodrug NV354* | Experimental metabolic-bypass therapy |
| [41572892](https://pubmed.ncbi.nlm.nih.gov/41572892/) | *Ultrasound-assisted gene therapy* | Experimental AAV gene therapy in Ndufs4-KO |
| [41321311](https://pubmed.ncbi.nlm.nih.gov/41321311/) | *LHX6 pallido-subthalamic projections in Leigh epilepsy* | Circuit mechanism of seizures |
| [41636927](https://pubmed.ncbi.nlm.nih.gov/41636927/) | *Region-specific innate immune activation in Ndufs4-KO* | Neuroinflammation branch |
| [31434271](https://pubmed.ncbi.nlm.nih.gov/31434271/) | *New FOXRED1 variants* | Ultra-rare epidemiology (~5 patients) |
| [18486820](https://pubmed.ncbi.nlm.nih.gov/18486820/) | *Ophthalmologic presentation of OXPHOS disease* | Ocular presenting signs |
| [15466086](https://pubmed.ncbi.nlm.nih.gov/15466086/) | *Spectrum in 113 pediatric mito patients* | CI most common defect; ~40% cardiac involvement |

**Evidence source types:** human clinical/case reports (20858599, 41412221, 31434271, 24731534, 27574709, 36412346, 18486820, 15466086); in vitro/patient-cell functional studies (20858599, 41412221); model-organism preclinical (41572892, 41321311, 41636927, 41532297, 41573538, 42427540, 41704780, 40770507, 41856111); reviews/systematic reviews (42265384, 42476091); computational/diagnostic (22277967).

---

## Limitations and Knowledge Gaps

1. **Extreme rarity.** With only ~5 patients reported by 2019 and a handful since, all clinical claims about MC1DN19 rest on very small numbers, and much of the prognosis/diagnosis framing is **borrowed from the broader Leigh-syndrome literature** rather than FOXRED1-specific cohorts.
2. **No natural-history dataset.** Survival curves, age-specific mortality, and quantitative QoL metrics are unavailable for MC1DN19 specifically.
3. **No dedicated animal model.** Mechanistic and therapeutic inferences come from the *Ndufs4*-KO **subunit** model, which does not reproduce FOXRED1's **assembly-factor** biology; there is a clear gap for a *Foxred1* mouse or organoid.
4. **Unproven therapy.** Riboflavin responsiveness is mechanistically plausible (FAD flavoprotein) but has **not been demonstrated** in FOXRED1 patients; the glutathione/diet GxE hypothesis is untested in vivo.
5. **Genotype–phenotype correlation is unresolved** — too few variants/patients to map specific alleles (e.g., recurrent p.R352W) to severity, cardiac involvement, or survival.
6. **No population frequency/carrier-rate estimate** beyond gnomAD LoF counts; possible founder alleles outside the index consanguineous family are uncharacterized.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a *Foxred1* mouse (and/or patient iPSC-derived brain organoid) model** to capture assembly-factor–specific pathology and enable therapeutic testing that current *Ndufs4*-KO models cannot address.
2. **Directly test riboflavin/FAD supplementation** in FOXRED1 patient fibroblasts/PBMCs (complex I assembly and activity readouts) and, if positive, in a *Foxred1* model — a low-cost, high-value test of the FAD-flavoprotein rationale.
3. **Experimentally test the glutathione/NO/peroxynitrite branch** ([PMID: 26235939](https://pubmed.ncbi.nlm.nih.gov/26235939/)) by measuring glutathione, nitrotyrosine, and complex I activity under methyl-donor (choline/folate) manipulation in FOXRED1-deficient cells.
4. **Cross-apply experimental Leigh therapeutics** (AAV *FOXRED1* gene replacement, hypoxia/GBT601, NV354 succinate bypass) to FOXRED1-specific models to determine whether benefits generalize from *Ndufs4*-KO.
5. **Build an international FOXRED1 patient registry** aggregating genotype, imaging, biochemistry, treatment response, and survival to derive genuine natural-history and genotype–phenotype data.
6. **Assemble a curated variant catalog** (ClinVar submission of all reported alleles with ACMG classifications) to support future diagnostic and prenatal testing.
7. **Implement cascade carrier screening and reproductive counseling** protocols for identified families, especially in consanguineous populations.

---

*Report compiled from 11 confirmed findings across 5 investigation iterations and 28 reviewed publications. Ontology suggestions provided for HPO, GO, CL, UBERON, CHEBI, NCIT, and MONDO to support structured knowledge-base ingestion.*


## Artifacts

- [OpenScientist final report](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_19-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_19-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 29 |
| Terms named correctly | 24 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032624` (3 mentions) - the report calls it "MONDO"; MONDO calls it **mitochondrial complex I deficiency, nuclear type 19**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005747` (obsolete mitochondrial respiratory chain complex I) (1 mention) - replaced by `GO:0045271`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012448` (1 mention) - the report calls it "Delayed/decreased myelination"; HP calls it **Delayed myelination**
- `HP:0011923` (2 mentions) - the report calls it "Decreased mitochondrial complex I activity"; HP calls it **Decreased activity of mitochondrial complex I**
- `UBERON:0002420` (1 mention) - the report calls it "basal ganglia"; UBERON calls it **basal ganglion**, and lists "basal ganglia" among its other names
- `GO:0005747` (1 mention) - the report calls it "respiratory chain complex I"; GO calls it **obsolete mitochondrial respiratory chain complex I**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.