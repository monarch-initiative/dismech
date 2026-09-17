---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T17:05:04.313751'
end_time: '2026-09-07T17:40:12.584633'
duration_seconds: 2108.27
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 37
  mondo_id: MONDO:0014491
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 14
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:30283440
  relevance_assessed: 16
  on_topic: 8
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0002728
    reported_labels:
    - Clinical sign
    ontology_label: Recurrent mucocutaneous candidiasis
  - term_id: HP:0001508
    reported_labels:
    - Physical manifestation
    ontology_label: Failure to thrive
  - term_id: HP:0002720
    reported_labels:
    - Laboratory abnormality
    ontology_label: Decreased circulating IgA concentration
  - term_id: HP:0005404
    reported_labels:
    - Laboratory abnormality
    ontology_label: Increased total B cell count
  - term_id: HP:0011840
    reported_labels:
    - Laboratory abnormality
    ontology_label: Abnormal T cell physiology
  - term_id: HP:0004313
    reported_labels:
    - Laboratory abnormality
    ontology_label: Decreased circulating immunoglobulin concentration
  - term_id: HP:0040218
    reported_labels:
    - Laboratory abnormality
    ontology_label: Reduced total natural killer cell count
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_37-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_37-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 37
- **MONDO ID:** MONDO:0014491 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 37** covering all of the
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

# Immunodeficiency 37 (BCL10 Deficiency): Comprehensive Disease Characteristics Report

**Disease:** Immunodeficiency 37 (IMD37) · **OMIM:** #616098 · **MONDO:** MONDO:0014491 · **Causal gene:** *BCL10* (1p22.3) · **Category:** Mendelian, autosomal recessive combined immunodeficiency (CBM-opathy)

---

## Summary

**Immunodeficiency 37 (IMD37) is an ultra-rare autosomal recessive combined immunodeficiency caused by biallelic loss-of-function mutations in *BCL10*, the caspase-recruitment-domain (CARD) adaptor protein that nucleates the CARD11–BCL10–MALT1 (CBM) signalosome.** The CBM complex is the molecular bridge that connects antigen-receptor engagement on B and T cells (and innate pattern-recognition receptors on other cell types) to activation of the canonical NF-κB pathway. When BCL10 is absent, antigen-receptor–induced NF-κB signaling is abolished, while proximal tyrosine phosphorylation, MAPK/AP-1, and calcium signaling remain intact. The result is a combined immunodeficiency affecting both **hematopoietic** (lymphocyte) and **non-hematopoietic** (fibroblast innate-receptor) immunity.

Clinically, IMD37 presents in **infancy or early childhood** with recurrent sinopulmonary infections, mucocutaneous candidiasis, gastroenteritis/enteropathy, and failure to thrive. The immunologic hallmark is a **profound deficit of memory B and T cells** with hypogammaglobulinemia and impaired specific antibody responses, despite frequently near-normal total lymphocyte counts. Additional reductions in NK cells, γδ T cells, and regulatory T cells have been documented. The disease is caused by homozygous (often private, consanguinity-associated) nonsense or frameshift alleles that abolish BCL10 protein expression; a single "leaky" linker-region frameshift variant produces a milder hypomorphic phenotype.

**Prognosis is poor without allogeneic hematopoietic stem cell transplantation (HSCT), which is the only curative therapy.** The index patient died at 3 years of age. Supportive care consists of immunoglobulin replacement and antimicrobial prophylaxis. Because *BCL10* is also required in non-hematopoietic cells, HSCT corrects the lymphoid compartment but would not be expected to correct the fibroblast innate-immunity defect. As of 2026, only approximately six to seven patients have been reported worldwide, making this one of the rarest inborn errors of immunity known. This report synthesizes 9 confirmed findings and 31 reviewed papers across all 15 requested disease-characteristic domains.

---

## Key Findings

### Finding 1 — IMD37 is autosomal recessive complete BCL10 deficiency

Immunodeficiency 37 corresponds to OMIM entry **#616098** and MONDO:0014491. It was first characterized in a landmark 2014 study by Torres and colleagues (*Inherited BCL10 deficiency impairs hematopoietic and nonhematopoietic immunity*, J Clin Invest). The index patient was a child homozygous for a loss-of-expression, loss-of-function *BCL10* mutation who presented with a broad combined immunodeficiency and died at 3 years of age. Critically, the defect affected **both hematopoietic and non-hematopoietic immunity**, distinguishing BCL10 deficiency from many other inborn errors of immunity that are restricted to lymphoid cells.

> "we characterized a case of autosomal-recessive, complete BCL10 deficiency in a child with a broad immunodeficiency, including defects of both hematopoietic and nonhematopoietic immunity. The patient died at 3 years of age and was homozygous for a loss-of-expression, loss-of-function BCL10 mutation." — [PMID: 25365219](https://pubmed.ncbi.nlm.nih.gov/25365219/)

The disease is exceptionally rare. A 2026 report confirms the small global patient count:

> "BCL10 deficiency is an exceptionally rare autosomal recessive combined immunodeficiency, with only six patients reported to date." — [PMID: 42473108](https://pubmed.ncbi.nlm.nih.gov/42473108/)

The causal gene, *BCL10*, is located on chromosome **1p22.3**, encodes a CARD-containing signaling adaptor, and carries the identifiers HGNC:989 and gene-OMIM 603517.

### Finding 2 — BCL10 links antigen-receptor signaling to NF-κB via the CBM signalosome

The mechanistic role of BCL10 was defined in Ruland et al. (2001, *Cell*) using *Bcl10*-knockout mice. These animals showed **complete absence of antigen-receptor–induced NF-κB activation**, while early tyrosine phosphorylation, MAPK/AP-1 signaling, and calcium flux remained normal — pinpointing BCL10's specific position in the signaling network.

> "antigen receptor-induced NF-kappaB activation was absent. Thus, Bcl10 functions as a positive regulator of lymphocyte proliferation that specifically connects antigen receptor signaling in B and T cells to NF-kappaB activation." — [PMID: 11163238](https://pubmed.ncbi.nlm.nih.gov/11163238/)

BCL10 acts within the tripartite **CARD11 (CARMA1)–BCL10–MALT1 (CBM) signalosome**. CARD11 nucleates BCL10 filaments, which in turn recruit the MALT1 paracaspase; the assembled complex bridges the T-cell receptor (TCR) and B-cell receptor (BCR) — as well as the innate CARD9/CARD14 receptors — to IKK-mediated canonical NF-κB, JNK, and mTORC1 activation.

> "The caspase recruitment domain family member 11 (CARD11 or CARMA1)-B cell CLL/lymphoma 10 (BCL10)-MALT1 paracaspase (MALT1) [CBM] signalosome complex serves as a molecular bridge between cell surface antigen receptor signaling and the activation of the NF-κB, JNK, and mTORC1 signaling axes." — [PMID: 30283440](https://pubmed.ncbi.nlm.nih.gov/30283440/)

### Finding 3 — Immunophenotype: profound memory lymphocyte defect with near-normal cell counts

Patients characteristically show **near-absence of memory B and memory T cells**, hypogammaglobulinemia with impaired specific antibody responses, and defective T- and B-cell proliferation to antigen-receptor stimulation — all despite frequently near-normal total lymphocyte counts. Mass cytometry of a patient homozygous for the K63X nonsense allele (Garcia-Solis et al. 2021, *Front Immunol*) additionally revealed reductions in NK cells, γδ T cells, and regulatory T cells.

> "in addition to the near absence of memory B and T cells previously reported, this patient displays a reduction in NK, γδT, Tregs, and T" — [PMID: 34868072](https://pubmed.ncbi.nlm.nih.gov/34868072/)

Importantly, the non-hematopoietic arm of the phenotype is real: BCL10-null fibroblasts show dramatically impaired NF-κB–mediated functions, while myeloid PAMP responses are largely preserved. IMD37 can present with an SCID-like picture yet **escape TREC-based newborn screening**, as documented in a case report titled *BCL10 Deficiency Presenting as Severe Combined Immunodeficiency Escaping Newborn Screening* ([PMID: 38159157](https://pubmed.ncbi.nlm.nih.gov/38159157/)).

### Finding 4 — Mouse model recapitulates immunodeficiency and adds a neural tube defect

*Bcl10*-knockout mice recapitulate the core human immunodeficiency and additionally reveal a developmental role. Approximately one-third of *Bcl10*−/− embryos develop **exencephaly** (a neural tube closure defect) leading to embryonic lethality; surviving mice are severely immunodeficient.

> "We show that one-third of bcl10-/- embryos developed exencephaly, leading to embryonic lethality." — [PMID: 11163238](https://pubmed.ncbi.nlm.nih.gov/11163238/)

> "surviving bcl10-/- mice were severely immunodeficient and bcl10-/- lymphocytes are defective in antigen receptor or PMA/Ionomycin-induced activation" — [PMID: 11163238](https://pubmed.ncbi.nlm.nih.gov/11163238/)

Subset-specific studies show that CD4+ T cells are most severely affected, whereas CD8+ T cells retain partial CBM-independent NF-κB activation ([PMID: 18941215](https://pubmed.ncbi.nlm.nih.gov/18941215/)); antigen-experienced CD4+CD44hi memory T cells can even bypass BCL10 for IL-2 production ([PMID: 18583339](https://pubmed.ncbi.nlm.nih.gov/18583339/)). A non-immune role is also evident: *Bcl10*-deficient mice are protected from angiotensin-II–dependent atherosclerosis and aortic aneurysm via the vascular CARMA3–BCL10–MALT1 axis ([PMID: 20605784](https://pubmed.ncbi.nlm.nih.gov/20605784/)).

### Finding 5 — Pathogenic variant spectrum: biallelic loss-of-function nonsense/frameshift alleles

All reported IMD37 patients carry biallelic loss-of-expression, loss-of-function *BCL10* variants. The documented allele spectrum is summarized below.

| Variant | Type | Effect | Reference |
|---|---|---|---|
| Private frameshift (Patient 1) | Frameshift | Complete loss of protein | Torres 2014, [PMID: 25365219](https://pubmed.ncbi.nlm.nih.gov/25365219/) |
| K63X | Nonsense | Complete loss of protein | Garcia-Solis 2021, [PMID: 34868072](https://pubmed.ncbi.nlm.nih.gov/34868072/) |
| R88X | Nonsense | Loss-of-expression / loss-of-function; heterozygous MAF 3.99×10⁻⁶ | Van Den Rym 2020, [PMID: 32008135](https://pubmed.ncbi.nlm.nih.gov/32008135/) |
| c.345_346dup (p.Gly116GlufsTer3) | Linker frameshift | "Leaky" hypomorph, low-abundance truncated protein | Tong 2026, [PMID: 42473108](https://pubmed.ncbi.nlm.nih.gov/42473108/) |

> "we report a new BCL10 mutation in another child with CID who was homozygous for a BCL10 variant (R88X), previously reported as a rare allele in heterozygosis (minor allele frequency, 0.000003986). The mutant allele was a loss-of-expression and loss-of-function allele." — [PMID: 32008135](https://pubmed.ncbi.nlm.nih.gov/32008135/)

> "A novel homozygous BCL10 c.345_346dup (p.Gly116GlufsTer3) variant was identified in a patient with combined immunodeficiency and immune dysregulation, with relatively mild infections" — [PMID: 42473108](https://pubmed.ncbi.nlm.nih.gov/42473108/)

This establishes an emerging **genotype–phenotype correlation**: complete-null alleles produce severe early-lethal disease, while the leaky linker-region frameshift produces a milder, later-recognized phenotype.

### Finding 6 — Clinical phenotype: early-onset infections, enteropathy, and innate fibroblast defects

Onset is in infancy or early childhood. Core clinical features are recurrent **respiratory (sinopulmonary) infections**, **candidiasis/mucocutaneous infections**, **gastroenteritis and chronic colitis/enteropathy**, and **failure to thrive**. The gastrointestinal manifestations show variable expressivity — present in the index patient but absent in the R88X patient.

> "The clinical phenotype shared features, such as respiratory infections, but differed from that of the previous patient that he did not develop significant gastroenteritis episodes or chronic colitis." — [PMID: 32008135](https://pubmed.ncbi.nlm.nih.gov/32008135/)

The non-hematopoietic defect was mechanistically confirmed by showing that fibroblast innate-receptor responses depend on BCL10:

> "TLR4, TLR2/6, and Dectin-1 responses were found to depend on BCL10 in fibroblasts, and final maturation of T cell and B cell maturation into memory cells was affected." — [PMID: 32008135](https://pubmed.ncbi.nlm.nih.gov/32008135/)

### Finding 7 — Treatment and prognosis: HSCT is the only curative option

Human BCL10 deficiency is managed supportively with immunoglobulin replacement (IVIG/SCIG) and antimicrobial prophylaxis, but **allogeneic hematopoietic stem cell transplantation is the only curative therapy**.

> "Human BCL10 deficiency causes combined immunodeficiency with bone marrow transplantation as its only curative option." — [PMID: 38129623](https://pubmed.ncbi.nlm.nih.gov/38129623/)

Proof-of-concept for curative HSCT in the CBM-opathy family comes from the closely related MALT1 deficiency, which was successfully treated with reduced-intensity conditioning and full immunological normalization:

> "The clinical and immunological phenotype of MALT1 deficiency can be successfully treated with hematopoietic stem cell transplantation following reduced intensity conditioning." — [PMID: 27109639](https://pubmed.ncbi.nlm.nih.gov/27109639/)

Prognosis is poor without HSCT — the index patient died at 3 years. No gene therapy or small-molecule therapy exists. A key caveat: HSCT corrects the hematopoietic compartment but would not correct the non-hematopoietic (fibroblast) BCL10 defect.

### Finding 8 — Identifiers, inheritance, and epidemiology

**Disease identifiers:** Immunodeficiency 37 (IMD37); OMIM #616098; MONDO:0014491.

**Gene identifiers** (*BCL10*, "BCL10 immune signaling adaptor"): NCBI Gene 8915; HGNC:989; gene OMIM 603517; Ensembl ENSG00000142867; UniProt O95999; cytoband 1p22.3 (GRCh38 chr1:85,265,776–85,276,640, minus strand). Aliases: CARMEN, CIPER, CLAP, c-E10, mE10, IMD37. Mouse ortholog: *Bcl10* (NCBI Gene 12051).

**Inheritance:** Autosomal recessive, with complete penetrance in biallelic loss-of-function carriers. Heterozygous carriers are healthy. Disease results from homozygous (often private, consanguinity-associated) LoF alleles.

**Epidemiology:** Ultra-rare — only ~6–7 patients reported worldwide as of 2026. No population prevalence or incidence has been established. Both sexes are affected (autosomal locus). Carrier alleles are extremely rare in gnomAD (e.g., R88X MAF 3.99×10⁻⁶).

> "BCL10 deficiency is an exceptionally rare autosomal recessive combined immunodeficiency, with only six patients reported to date." — [PMID: 42473108](https://pubmed.ncbi.nlm.nih.gov/42473108/)

### Finding 9 — Structural basis: BCL10 CARD nucleates helical CBM filaments

Structural work (Qiao et al. 2013, *Mol Cell*) using cryo-EM, crystallography, and NMR revealed that the CBM signalosome is a **helical filamentous assembly**. Substoichiometric CARMA1 (CARD11) nucleates BCL10 CARD filaments; filament formation is highly cooperative and its threshold is sensitized by oligomerized CARMA1 upon receptor activation. These filaments then recruit and activate MALT1 to drive NF-κB. Structure-guided mutagenesis of the BCL10 filament interfaces abolished both MALT1 activation and cellular NF-κB activation.

> "the reconstituted CBM signalosome is a helical filamentous assembly in which substoichiometric CARMA1 nucleates Bcl10 filaments. Bcl10 filament formation is a highly cooperative process whose threshold is sensitized by oligomerized CARMA1 upon receptor activation." — [PMID: 24074955](https://pubmed.ncbi.nlm.nih.gov/24074955/)

This explains why complete loss of BCL10 abolishes NF-κB signaling: BCL10 is the nucleated scaffold that converts receptor engagement into a digital, threshold-gated signaling output.

---

## Section-by-Section Disease Characterization

### 1. Disease Information
IMD37 is an autosomal recessive combined immunodeficiency caused by complete BCL10 deficiency. **Key identifiers:** OMIM #616098; MONDO:0014491; gene *BCL10* OMIM 603517; HGNC:989. **Synonyms/alternative names:** BCL10 deficiency; immunodeficiency 37; IMD37. There is no dedicated Orphanet number widely used beyond the CBM-opathy grouping; ICD-11 would fall under primary immunodeficiency/combined immunodeficiency categories (e.g., 4A00). **Information source:** aggregated at the disease level from a handful of individual case reports (EHR-derived clinical data on ~6–7 patients worldwide), synthesized with model-organism and in-vitro mechanistic data.

### 2. Etiology
**Primary cause:** genetic — biallelic (homozygous) loss-of-function mutations in *BCL10*. **Genetic risk factors:** consanguinity is the dominant risk factor, as disease requires two LoF alleles that are individually extremely rare (e.g., R88X MAF 3.99×10⁻⁶). No susceptibility loci, modifier genes, or protective alleles have been established given the tiny patient count. **Environmental risk/protective factors:** none identified; the disease is fully penetrant Mendelian. **Gene–environment interactions:** the phenotype is triggered by ordinary environmental pathogen exposure acting on a defective immune system, but no specific GxE modifier is documented.

### 3. Phenotypes
| Phenotype | Type | HPO term (suggested) | Onset | Frequency |
|---|---|---|---|---|
| Recurrent respiratory/sinopulmonary infections | Clinical sign | HP:0002783 / HP:0002205 | Infancy | Core, most patients |
| Recurrent candidiasis / mucocutaneous infection | Clinical sign | HP:0002728 | Infancy | Frequent |
| Chronic diarrhea / enteropathy / colitis | Clinical sign | HP:0002028 / HP:0002037 | Infancy | Variable expressivity |
| Failure to thrive | Physical manifestation | HP:0001508 | Infancy | Frequent |
| Hypogammaglobulinemia | Laboratory abnormality | HP:0002720 | Congenital/infancy | Core |
| Decreased memory B cells | Laboratory abnormality | HP:0005404 | Congenital | Core |
| Reduced/absent memory T cells | Laboratory abnormality | HP:0011840 | Congenital | Core |
| Impaired specific antibody response | Laboratory abnormality | HP:0004313 | Congenital | Core |
| Decreased NK / γδ T / Treg cells | Laboratory abnormality | HP:0040218 | Congenital | Documented (K63X patient) |

**Severity:** severe in complete-null genotypes (early death), milder in the leaky hypomorph. **Progression:** progressive with recurrent infections. **Quality-of-life impact:** severe — chronic infection, malnutrition, and early mortality without HSCT.

### 4. Genetic / Molecular Information
**Causal gene:** *BCL10* (1p22.3; OMIM 603517; HGNC:989). **Pathogenic variants:** all biallelic germline LoF — frameshift (private; c.345_346dup p.Gly116GlufsTer3) and nonsense (K63X, R88X). **ACMG classification:** pathogenic/likely pathogenic. **Variant types:** nonsense and frameshift predominate; no missense pathogenic alleles yet reported. **Allele frequency:** extremely rare in gnomAD (R88X MAF 3.99×10⁻⁶). **Origin:** germline. **Functional consequence:** complete loss of function (null) for most; hypomorphic "leaky" loss for the linker frameshift. **Modifier genes/epigenetics/chromosomal abnormalities:** none established for the germline disease. (Note: somatic *BCL10* truncating mutations and t(1;14)(p22;q32) rearrangements occur in MALT lymphoma — [PMID: 10319863](https://pubmed.ncbi.nlm.nih.gov/10319863/), [PMID: 11445840](https://pubmed.ncbi.nlm.nih.gov/11445840/) — a distinct dysregulation context, not IMD37.)

### 5. Environmental Information
No environmental, lifestyle, or toxicant contributing factors are known — IMD37 is a fully penetrant monogenic disorder. **Infectious agents** are downstream *consequences*, not causes: patients suffer recurrent bacterial respiratory pathogens, *Candida* species (mucocutaneous candidiasis), and viral/gastrointestinal infections due to the underlying immune defect.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

```
1. Biallelic LoF mutation in BCL10 (nonsense/frameshift)
        │ leads to
2. Complete absence (or, for the leaky allele, near-absence) of BCL10 protein
        │ results in
3. Failure to nucleate CARD11-BCL10-MALT1 (CBM) helical filaments
   (BCL10 CARD is the nucleated scaffold; CARMA1 seeds it)  [PMID:24074955]
        │ leads to
4. No recruitment/activation of MALT1 paracaspase; no IKK activation
        │ results in
5. Abolished antigen-receptor-induced canonical NF-kB activation
   (proximal tyrosine-P, MAPK/AP-1, Ca2+ remain intact)     [PMID:11163238]
        │ branches into
   ┌────────────────────────────┬──────────────────────────────────┐
6a. Hematopoietic arm:          6b. Non-hematopoietic arm:
   defective B/T proliferation,    fibroblast TLR4, TLR2/6, Dectin-1
   failed memory B/T generation,   responses fail (BCL10-dependent)
   hypogammaglobulinemia,          [PMID:32008135]
   reduced NK/gdT/Treg
        │ leads to                        │ leads to
7. Combined immunodeficiency: impaired adaptive AND innate immunity
        │ results in
8. Clinical manifestation: recurrent respiratory infections, candidiasis,
   enteropathy, failure to thrive -> early death without HSCT
```

**Molecular pathways (KEGG/Reactome):** canonical NF-κB signaling (downstream), also JNK and mTORC1 axes ([PMID: 30283440](https://pubmed.ncbi.nlm.nih.gov/30283440/)). **Cellular processes (GO):** lymphocyte activation (GO:0046649), antigen receptor-mediated signaling (GO:0050851), I-κB kinase/NF-κB signaling (GO:0007249). **Protein dysfunction:** loss of the BCL10 filament scaffold; the CBM complex (GO:0032449) cannot assemble. **Immune involvement:** immunodeficiency, both adaptive and innate. **Upstream vs downstream:** the mutation → loss of scaffold → loss of NF-κB is upstream; memory-cell failure and clinical infection are downstream. **Cell types (CL):** T cell (CL:0000084), B cell (CL:0000236), memory B cell (CL:0000787), memory T cell (CL:0000813), NK cell (CL:0000623), γδ T cell (CL:0000798), regulatory T cell (CL:0000815), fibroblast (CL:0000057).

### 7. Anatomical Structures Affected
**Organ/system level:** immune/hematopoietic system (UBERON:0002405) is primary; secondary involvement of the respiratory tract (lung, UBERON:0002048; airways), gastrointestinal tract (intestine, UBERON:0000160; for enteropathy/colitis), and skin/mucosa (UBERON:0002097; candidiasis). **Tissue/cell level:** lymphoid tissue and lymphocytes; connective-tissue fibroblasts (non-hematopoietic arm). **Subcellular (GO CC):** cytoplasmic CBM signalosome/filament assembly signaling to the nucleus for NF-κB-dependent transcription. **Lateralization:** systemic/bilateral (not a focal lesion).

### 8. Temporal Development
**Onset:** congenital/neonatal-infantile immune defect, clinically manifesting in infancy/early childhood with an insidious-to-subacute course of recurrent infections. **Progression:** progressive without treatment; the leaky hypomorph runs a milder, later-recognized course. **Duration:** chronic and lifelong; fatal in early childhood without HSCT (index patient died at 3 years). **Critical period:** early diagnosis and HSCT *before* the establishment of chronic infections and end-organ (pulmonary) damage is the key intervention window.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive; **penetrance:** complete in biallelic LoF carriers; **expressivity:** variable (GI features variable; leaky allele milder); **carrier status:** heterozygotes healthy. **Consanguinity:** a major contributor (homozygosity for rare private alleles). **Founder effects/anticipation/mosaicism:** none documented. **Epidemiology:** ultra-rare, ~6–7 patients worldwide as of 2026; no prevalence/incidence figures; both sexes affected; no ethnic predilection established beyond consanguineous pedigrees.

### 10. Diagnostics
**Laboratory:** immunoglobulin quantitation (hypogammaglobulinemia), specific antibody responses (impaired), lymphocyte subset immunophenotyping showing near-absent memory B/T cells with often near-normal total counts; extended flow/mass cytometry may show reduced NK, γδ T, and Treg. Functional NF-κB activation assays (impaired). **Genetic testing** is definitive: WES/WGS or a combined-immunodeficiency/primary-immunodeficiency gene panel including *BCL10*; single-gene sequencing confirms biallelic LoF variants. **Newborn screening caveat:** TREC-based SCID screening can miss IMD37 ([PMID: 38159157](https://pubmed.ncbi.nlm.nih.gov/38159157/)). **Differential diagnosis:** other CBM-opathies — CARD11 deficiency (IMD11), MALT1 deficiency (IMD12) — and other combined immunodeficiencies (e.g., DOCK8 deficiency); distinguished by gene identification.

### 11. Outcome / Prognosis
**Survival/mortality:** poor without HSCT; index patient died at 3 years; another died in infancy — high early mortality. **Morbidity:** chronic recurrent infections, failure to thrive, potential end-organ (pulmonary) damage. **Prognostic factors:** genotype (complete-null vs leaky hypomorph), timing of HSCT relative to infection burden. **Recovery potential:** curative HSCT can restore the hematopoietic immune compartment (by analogy with MALT1 deficiency, [PMID: 27109639](https://pubmed.ncbi.nlm.nih.gov/27109639/)), though the non-hematopoietic fibroblast defect would persist.

### 12. Treatment
- **Supportive/pharmacotherapy:** immunoglobulin replacement (IVIG/SCIG; NCIT: Intravenous Immunoglobulin Therapy) and antimicrobial/antifungal prophylaxis.
- **Curative:** allogeneic **hematopoietic stem cell transplantation** (NCIT: Allogeneic Hematopoietic Stem Cell Transplantation) — the only curative option ([PMID: 38129623](https://pubmed.ncbi.nlm.nih.gov/38129623/)); reduced-intensity conditioning is effective in the related MALT1 deficiency ([PMID: 27109639](https://pubmed.ncbi.nlm.nih.gov/27109639/)).
- **Advanced/experimental:** no gene therapy, RNA therapy, or targeted small molecule exists; none in registered trials for IMD37 specifically.
- **Personalized medicine:** genotype-guided — early HSCT for complete-null genotypes; the leaky hypomorph may permit more conservative initial management.

### 13. Prevention
**Primary prevention:** not possible (monogenic); **genetic counseling** for consanguineous families and **carrier/cascade testing** of relatives are the principal preventive measures (NSGC/ACMG framework). **Prenatal/preimplantation genetic diagnosis** is available for families with a known pathogenic *BCL10* genotype. **Secondary prevention:** early molecular diagnosis and pre-emptive HSCT before infection-related organ damage. **Tertiary prevention:** immunoglobulin replacement and antimicrobial prophylaxis to prevent complications. Note that standard TREC newborn screening does not reliably detect IMD37.

### 14. Other Species / Natural Disease
**Taxonomy/orthologs:** mouse *Bcl10* (NCBI Gene 12051; NCBI Taxon 10090) is the principal model ortholog; the gene is evolutionarily conserved. **Natural disease in other species:** no naturally occurring companion-animal or wildlife BCL10-deficiency disease is documented in OMIA to date. **Comparative biology:** the CBM/NF-κB axis is conserved across mammals; the mouse knockout adds an exencephaly/neural-tube phenotype not reported in humans, indicating species-specific developmental requirements. **Zoonotic potential:** not applicable (non-infectious genetic disease).

### 15. Model Organisms
**Principal model:** the *Bcl10*−/− mouse (Ruland et al. 2001, [PMID: 11163238](https://pubmed.ncbi.nlm.nih.gov/11163238/)) — a constitutive knockout. **Phenotype recapitulation:** strong for the immunodeficiency (absent antigen-receptor NF-κB, defective lymphocyte activation and proliferation), providing the foundational mechanistic model. **Model limitations/divergences:** ~1/3 of embryos die of exencephaly (embryonic lethality), a neural-tube phenotype not seen in human patients; subset-specific studies show CD8+ T cells and memory CD4+CD44hi cells retain partial BCL10-independent function ([PMID: 18941215](https://pubmed.ncbi.nlm.nih.gov/18941215/), [PMID: 18583339](https://pubmed.ncbi.nlm.nih.gov/18583339/)). **In-vitro models:** BCL10-null patient fibroblasts and CRISPR/reconstituted Jurkat T-cell NF-κB reporter systems ([PMID: 34236636](https://pubmed.ncbi.nlm.nih.gov/34236636/)) are used to dissect CBM signaling. **Resources:** MGI (mouse), Cellosaurus (cell lines).

---

## Mechanistic Model / Interpretation

IMD37 is best understood as a **"CBM-opathy"** — a disorder of the CARD11–BCL10–MALT1 signalosome. BCL10 occupies the central, non-redundant position in this three-protein module. Structurally, it is the **nucleated filament scaffold**: CARMA1 (CARD11), once oligomerized by receptor engagement, seeds the cooperative polymerization of BCL10 CARD filaments, which display MALT1 for activation. This filamentous, threshold-gated architecture converts a graded receptor input into a switch-like NF-κB output ([PMID: 24074955](https://pubmed.ncbi.nlm.nih.gov/24074955/)).

Because BCL10 is the obligate scaffold, its complete loss produces a **clean, specific lesion**: antigen-receptor signaling still fires its proximal tyrosine kinases, MAPK, and calcium arms, but the NF-κB arm is silenced ([PMID: 11163238](https://pubmed.ncbi.nlm.nih.gov/11163238/)). NF-κB is essential for the terminal differentiation and survival programs that generate immunological memory, which explains why the cardinal laboratory signature is **loss of memory B and T cells with preserved naïve-cell counts**.

A distinctive feature that separates BCL10 deficiency from CARD11 deficiency is the **non-hematopoietic dimension**. CARD11 (CARMA1) is lymphocyte-restricted, but BCL10 also partners with the broadly expressed CARMA3 (CARD10) and with CARD9/CARD14 in innate contexts. Consequently, BCL10-null fibroblasts fail to respond to TLR4, TLR2/6, and Dectin-1 stimulation ([PMID: 32008135](https://pubmed.ncbi.nlm.nih.gov/32008135/)). This dual hematopoietic + non-hematopoietic defect is the key therapeutic caveat: **HSCT replaces the lymphoid compartment but cannot correct the fibroblast (stromal) innate defect**, which may limit long-term cure completeness even after successful transplantation.

| Feature | BCL10 (IMD37) | CARD11 (IMD11) | MALT1 (IMD12) |
|---|---|---|---|
| Cell-type breadth of defect | Hematopoietic + non-hematopoietic | Lymphocyte-restricted | Hematopoietic + non-hematopoietic |
| Core immunophenotype | Loss of memory B/T; hypogammaglobulinemia | CID; variable | CID; inflammatory features |
| Curative therapy | HSCT only | HSCT | HSCT (proven, [PMID: 27109639](https://pubmed.ncbi.nlm.nih.gov/27109639/)) |
| Global patient count | ~6–7 | Rare | Rare |

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|---|---|---|
| [25365219](https://pubmed.ncbi.nlm.nih.gov/25365219/) | *Inherited BCL10 deficiency impairs hematopoietic and nonhematopoietic immunity* | Defines the disease: AR complete BCL10 deficiency, dual immune defect, death at 3 y |
| [42473108](https://pubmed.ncbi.nlm.nih.gov/42473108/) | *A novel linker region truncating variant in BCL10 underlies a leaky immunodeficiency phenotype* | Epidemiology (~6 patients), hypomorphic genotype–phenotype correlation |
| [11163238](https://pubmed.ncbi.nlm.nih.gov/11163238/) | *Bcl10 is a positive regulator of antigen receptor-induced NF-κB and neural tube closure* | Core mechanism (NF-κB–specific defect) + mouse model (exencephaly) |
| [30283440](https://pubmed.ncbi.nlm.nih.gov/30283440/) | *The CBM-opathies* | Places BCL10 in the CBM signalosome; NF-κB/JNK/mTORC1 axes |
| [34868072](https://pubmed.ncbi.nlm.nih.gov/34868072/) | *Clinical and Immunological Features of Human BCL10 Deficiency* | Immunophenotype: memory loss + reduced NK/γδT/Treg |
| [32008135](https://pubmed.ncbi.nlm.nih.gov/32008135/) | *Human BCL10 Deficiency due to Homozygosity for a Rare Allele* | R88X allele + fibroblast innate-receptor dependence on BCL10 |
| [38129623](https://pubmed.ncbi.nlm.nih.gov/38129623/) | *Inherited Human BCL10 Deficiencies* | HSCT as only curative option |
| [27109639](https://pubmed.ncbi.nlm.nih.gov/27109639/) | *HSCT for human MALT1 deficiency* | HSCT proof-of-concept for a related CBM-opathy |
| [24074955](https://pubmed.ncbi.nlm.nih.gov/24074955/) | *Structural architecture of the CARMA1/Bcl10/MALT1 signalosome* | Structural basis: BCL10 filament nucleation, threshold signaling |
| [38159157](https://pubmed.ncbi.nlm.nih.gov/38159157/) | *BCL10 Deficiency Escaping Newborn Screening* | Diagnostic caveat: TREC screening can miss IMD37 |
| [18941215](https://pubmed.ncbi.nlm.nih.gov/18941215/) | *Loss of PKCθ/Bcl10/Malt1 selectively impairs CD4+ T cells* | CD4 > CD8 selectivity; CD8 retains partial CBM-independent NF-κB |

Evidence source types: **human clinical** (case reports of ~6–7 patients), **model organism** (*Bcl10*−/− mouse), **in vitro** (patient fibroblasts, Jurkat reconstitution), and **computational/structural** (cryo-EM/NMR of the CBM filament).

---

## Limitations and Knowledge Gaps

1. **Extremely small patient count (~6–7 worldwide).** All clinical conclusions rest on case reports; no cohort statistics, formal prevalence/incidence, penetrance estimates, or survival curves exist.
2. **Genotype–phenotype correlation is preliminary.** Only one "leaky" hypomorphic allele has been described; the full allelic and phenotypic spectrum (including any missense pathogenic variants) is unknown.
3. **HSCT outcome data are indirect.** Direct long-term transplant outcomes in BCL10-deficient patients are sparse; the curative evidence is partly extrapolated from MALT1 deficiency.
4. **Non-hematopoietic contribution is unquantified.** It remains unclear how much the fibroblast/stromal innate defect contributes to clinical disease, and whether it limits cure after HSCT.
5. **No natural animal disease** and no established modifier genes, epigenetic mechanisms, or environmental modifiers.
6. **Newborn screening gap.** Because IMD37 can escape TREC screening, true incidence may be underestimated.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international BCL10-deficiency registry** to aggregate genotypes, immunophenotypes, HSCT outcomes, and survival — the only way to move beyond single case reports.
2. **Systematic HSCT outcome study** (conditioning regimen, chimerism, immune reconstitution, and whether the fibroblast defect persists post-transplant), ideally with comparison to MALT1/CARD11 CBM-opathy transplants.
3. **Genotype–function mapping:** reconstitute the full allelic series (null vs leaky vs any candidate missense) in NF-κB reporter Jurkat and fibroblast systems to build a quantitative genotype–residual-signal–phenotype map.
4. **Assess the stromal/non-hematopoietic defect in vivo** using conditional (tissue-specific) *Bcl10* mouse models to isolate the fibroblast contribution and test whether HSCT alone is sufficient.
5. **Improve newborn detection:** evaluate whether adding B-cell/KREC metrics or targeted CBM-gene panels to newborn screening captures IMD37 missed by TREC.
6. **Explore gene-correction feasibility** (autologous HSC gene addition/editing of *BCL10*) as a future curative modality that could restore the hematopoietic compartment without allogeneic transplant risks.

---

*Report compiled from 9 confirmed findings and 31 reviewed publications across a 5-iteration autonomous investigation. The evidence base is dominated by human case reports and the foundational* Bcl10−/− *mouse model; all mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_37-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_37-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 16 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:30283440` *(abstract only)*: "The caspase recruitment domain family member 11 (CARD11 or CARMA1)-B cell CLL/lymphoma 10 (BCL10)-MALT1 paracaspase (MALT1) [CBM] signalosome complex serves as a molecular bridge between cell surface antigen receptor signaling and the activation of the NF-κB, JNK, and mTORC1 signaling axes."
  - closest text in source: "The caspase recruitment domain family member 11 (CARD11 or CARMA1)-B cell CLL/lymphoma 10 (BCL10)-MALT1 paracaspase (MALT1) [CBM] signalosome complex serves as a molecular bridge between cell surface antigen receptor signaling and the activation of the NF-κB, JNK, and mTORC1 signaling axes."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002728` (1 mention) - the report calls it "Clinical sign"; HP calls it **Recurrent mucocutaneous candidiasis**
- `HP:0001508` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Failure to thrive**
- `HP:0002720` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Decreased circulating IgA concentration**
- `HP:0005404` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Increased total B cell count**
- `HP:0011840` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Abnormal T cell physiology**
- `HP:0004313` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Decreased circulating immunoglobulin concentration**
- `HP:0040218` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Reduced total natural killer cell count**