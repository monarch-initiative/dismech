---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T20:17:38.268704'
end_time: '2026-10-16T20:41:04.356619'
duration_seconds: 1406.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: CHAND Syndrome
  mondo_id: MONDO:0008959
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
citation_count: 20
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 12
  relevance_assessed: 23
  on_topic: 13
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 30
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 4
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0008959
    reported_labels:
    - MONDO
    ontology_label: CHAND syndrome
  - term_id: HP:0010729
    reported_labels:
    - Ankyloblepharon
    ontology_label: Cherry red spot of the macula
  - term_id: UBERON:0000158
    reported_labels:
    - Ocular adnexa:** Eyelids
    ontology_label: membranous layer
  - term_id: NCIT:C15277
    reported_labels:
    - Supportive Care
    - Protective/cosmetic nail management
    ontology_label: Mastectomy
  - term_id: NCIT:C15313
    reported_labels:
    - Dental procedure
    ontology_label: Radiation Therapy
  - term_id: NCIT:C15215
    reported_labels:
    - Genetic Counseling
    ontology_label: Cryosurgery
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0098742
    ontology_label: obsolete cell-cell adhesion via plasma-membrane adhesion molecules
    replaced_by: GO:0098609
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: CHAND_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: CHAND_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CHAND Syndrome
- **MONDO ID:** MONDO:0008959 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CHAND Syndrome** covering all of the
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

# CHAND Syndrome: A Comprehensive Disease Characteristics Report

**Disease:** CHAND Syndrome (Curly Hair–Ankyloblepharon–Nail Dysplasia Syndrome)
**MONDO ID:** MONDO:0008959 · **OMIM:** 214350 · **Category:** Mendelian (autosomal recessive ectodermal dysplasia)
**Causal gene:** *RIPK4* (HGNC:3772; chr 21q22.3)

---

## Summary

CHAND syndrome is an ultra-rare, autosomal recessive ectodermal dysplasia defined by the clinical triad of **C**urly **H**air, **A**nkyloblepharon (fusion of the eyelid margins), and **N**ail **D**ysplasia. First described by Baughman in 1971 as an apparent autosomal dominant trait, the inheritance was later re-evaluated as autosomal recessive after additional pedigree analysis revealed quasi-dominant transmission driven by multiple consanguineous matings ([PMID: 490586](https://pubmed.ncbi.nlm.nih.gov/490586/)). The molecular basis remained unknown for over four decades until biallelic mutations in *RIPK4* (receptor-interacting serine/threonine kinase 4) were identified, placing CHAND firmly within the **RIPK4/IRF6 periderm-development disease spectrum** that also encompasses the far more severe Bartsocas-Papas syndrome (BPS) and popliteal pterygium syndrome (PPS).

The central mechanistic insight of this investigation is that **CHAND represents the mild, non-lethal end of the RIPK4 allelic spectrum**. The recurrent CHAND mutation, c.850G>A (p.Glu284Lys), lies *just outside* the serine/threonine kinase domain of RIPK4, whereas the mutations causing lethal Bartsocas-Papas syndrome typically fall *within* the kinase domain and abolish kinase activity. RIPK4 functions as an upstream activating kinase for the transcription factor IRF6: it phosphorylates IRF6 at Ser413/Ser424 to drive its nuclear translocation and transactivation, controlling the p63→RIPK4→IRF6→GRHL3/OVOL1 keratinocyte-differentiation cascade and the periderm program that prevents pathological epithelial adhesions during embryogenesis. Hypomorphic RIPK4 variants retain residual activity, producing the comparatively mild adhesion and ectodermal defects of CHAND rather than the widespread pterygia, clefting, and perinatal lethality of BPS.

This report synthesizes evidence from 33 primary sources to characterize CHAND across all 15 requested domains. Because CHAND is genetically determined, well-defined categories (Disease Information, Etiology, Genetics, Mechanism, Inheritance, Diagnostics) are richly supported, while categories designed for common or environmentally-driven diseases (Environmental Factors, Infectious Agents, CHAND-specific model organisms, epidemiological prevalence estimates) are sparse or not applicable, and these gaps are explicitly flagged. Prognosis for survival in CHAND is normal; management is entirely supportive.

---

## Section 1 — Disease Information

**Overview.** CHAND syndrome is a rare congenital ectodermal dysplasia characterized by the triad of curly/kinky hair, ankyloblepharon (partial-thickness fusion of the eyelid margins, "ankyloblepharon filiforme adnatum"), and nail dysplasia. It belongs to the broad family of ectodermal dysplasias — congenital disorders affecting derivatives of the embryonic ectoderm (skin, hair, teeth, nails, and glands). It is formally defined as "an autosomal recessive disorder characterized by curly hair, ankyloblepharon, and nail dysplasia" ([PMID: 28940926](https://pubmed.ncbi.nlm.nih.gov/28940926/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | 214350 |
| MONDO | MONDO:0008959 |
| Causal gene | *RIPK4* (HGNC:3772; NCBI Gene 54101; UniProt P57078) |
| Chromosomal locus | 21q22.3 |
| Orphanet | Within the ectodermal dysplasia / AEC-related spectrum |
| MeSH | Indexed under Ectodermal Dysplasia |

**Synonyms / alternative names.**
- CHANDS (Curly Hair–Ankyloblepharon–Nail Dysplasia Syndrome)
- Curly hair–ankyloblepharon–nail dysplasia syndrome
- Baughman syndrome (eponym from the 1971 original description)
- Often discussed as a clinical variant of AEC (Hay-Wells) syndrome ([PMID: 29440852](https://pubmed.ncbi.nlm.nih.gov/29440852/))

**Information source type.** The knowledge base for CHAND derives almost entirely from **aggregated disease-level resources** (OMIM, Orphanet) and **individual case reports / small consanguineous kindreds** published in the primary literature — not from large EHR cohorts or registries. The disease is so rare that evidence rests on a handful of families.

---

## Section 2 — Etiology

**Disease causal factors.** CHAND is a **monogenic (Mendelian) disorder** caused by biallelic (homozygous or compound heterozygous) pathogenic variants in *RIPK4*. There is no environmental or infectious contribution to disease causation. A homozygous *RIPK4* missense mutation c.850G>A (p.Glu284Lys) segregated completely with disease in a consanguineous Kuwaiti kindred with three affected individuals, "in accordance with an autosomal recessive inheritance pattern, thus supporting pathogenicity of this variant" ([PMID: 26129644](https://pubmed.ncbi.nlm.nih.gov/26129644/)). RIPK4 causation was independently confirmed ([PMID: 28940926](https://pubmed.ncbi.nlm.nih.gov/28940926/)).

**Genetic risk factors.** The sole established genetic risk factor is carriage of biallelic hypomorphic *RIPK4* variants. **Consanguinity** is a strong contributing factor to risk, as recessive *RIPK4* alleles become homozygous through consanguineous unions — the originally reported pedigrees involved multiple consanguineous matings ([PMID: 490586](https://pubmed.ncbi.nlm.nih.gov/490586/)), and the molecularly-solved families were consanguineous (Kuwaiti, Turkish).

**Environmental risk factors.** None identified. CHAND is fully genetically determined and congenital. *Not applicable.*

**Protective factors.** No genetic or environmental protective/modifier factors have been formally described for CHAND. It is plausible — but not demonstrated — that the *position* of the mutation (outside vs within the kinase domain) acts as the primary intrinsic determinant of mild vs severe phenotype (see Section 4).

**Gene–environment interactions.** *Not applicable* — no environmental component.

---

## Section 3 — Phenotypes

CHAND is a congenital disorder; all core features are present at or shortly after birth. Severity is generally **mild** relative to other RIPK4-opathies, and survival is normal.

| Phenotype | Type | HPO suggestion | Onset | Frequency / notes |
|---|---|---|---|---|
| Curly / kinky / wiry hair | Physical manifestation (hair) | HP:0002212 (Curly hair); HP:0002213 (Coarse hair) | Congenital | Core triad feature; coarse "wiry" hair reported ([PMID: 15347331](https://pubmed.ncbi.nlm.nih.gov/15347331/)) |
| Sparse / light-colored hair | Physical manifestation | HP:0008070 (Sparse hair) | Congenital | Reported in case series ([PMID: 29440852](https://pubmed.ncbi.nlm.nih.gov/29440852/)) |
| "Bubbly hair" / "bubble hair" shaft morphology | Laboratory (microscopy) | — | Congenital | Distinctive microscopic finding ([PMID: 29440852](https://pubmed.ncbi.nlm.nih.gov/29440852/)) |
| Ankyloblepharon (filiforme adnatum) | Clinical sign | HP:0010729 (Ankyloblepharon) | Congenital | Core triad; partial fusion of eyelid margins, surgically correctable ([PMID: 29440852](https://pubmed.ncbi.nlm.nih.gov/29440852/)) |
| Nail dysplasia / 20-nail dystrophy | Physical manifestation | HP:0001597 (Abnormality of the nail); HP:0008404 (Nail dysplasia) | Congenital | Core triad feature |
| Abnormal dentition | Physical manifestation | HP:0000164 (Abnormality of the teeth) | Childhood | Reported in cases ([PMID: 29440852](https://pubmed.ncbi.nlm.nih.gov/29440852/)) |
| Hypohidrosis (variable) | Clinical sign | HP:0000966 (Hypohidrosis) | Congenital | Present in some overlap cases ([PMID: 15347331](https://pubmed.ncbi.nlm.nih.gov/15347331/)); often ABSENT in classic CHAND ([PMID: 29440852](https://pubmed.ncbi.nlm.nih.gov/29440852/)) |
| Palmoplantar hyperkeratosis / cutaneous syndactyly / orofacial synechiae | Physical manifestation | HP:0000982; HP:0012725; HP:0000168 | Congenital | At the more severe end of the RIPK4-ectodermal dysplasia spectrum ([PMID: 35220430](https://pubmed.ncbi.nlm.nih.gov/35220430/)) |

**Distinguishing feature:** Unlike AEC (Hay-Wells) syndrome, classic CHAND characteristically **lacks cleft lip/palate** and lacks the erosive scalp dermatitis typical of AEC ([PMID: 26129644](https://pubmed.ncbi.nlm.nih.gov/26129644/); [PMID: 15347331](https://pubmed.ncbi.nlm.nih.gov/15347331/)).

**Severity / progression.** Features are congenital, **stable and non-progressive**. There is marked clinical overlap with AEC, Rapp-Hodgkin, Bowen-Armstrong, and Bartsocas-Papas syndromes, making classification on clinical grounds alone difficult ([PMID: 15347331](https://pubmed.ncbi.nlm.nih.gov/15347331/)).

**Quality of life.** Formal QoL instruments (EQ-5D, SF-36) have not been applied to CHAND. Impact is primarily cosmetic (hair, nails) and, for ankyloblepharon, visual/ocular until surgically corrected. Overall functional impact is modest.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** ***RIPK4*** — Receptor-Interacting serine/threonine Protein Kinase 4. Aliases: **PKK** (Protein Kinase C-associated Kinase), **DIK**, **ANKRD3**. HGNC:3772; NCBI Gene 54101; UniProt P57078; locus **21q22.3** ([PMID: 11278382](https://pubmed.ncbi.nlm.nih.gov/11278382/)).

**Protein architecture.** RIPK4 encodes "an N-terminal kinase domain and a C-terminal region containing 11 ankyrin repeats" and is a membrane-associated, PKC-interacting kinase ([PMID: 11278382](https://pubmed.ncbi.nlm.nih.gov/11278382/)). The ankyrin repeats mediate protein–protein interactions; the kinase domain carries out catalytic phosphorylation of downstream substrates (IRF6, Dvl2, PKP1).

**Pathogenic variants and genotype–phenotype correlation.** This is the central molecular finding. The CHAND recurrent variant and the contrasting BPS variants map to different protein regions:

| Variant (HGVS) | Protein change | Location | Kinase activity | Phenotype | PMID |
|---|---|---|---|---|---|
| c.850G>A | p.Glu284Lys | **Outside** kinase domain | Partially retained (hypomorphic) | **CHAND (mild)** | [26129644](https://pubmed.ncbi.nlm.nih.gov/26129644/) |
| c.362T>A | p.Ile121Asn | Within kinase domain | Abolished | Bartsocas-Papas (severe) | [25246526](https://pubmed.ncbi.nlm.nih.gov/25246526/) |
| c.481G>C | p.Asp161His | Within kinase domain | Abolished | Severe BPS | [33713555](https://pubmed.ncbi.nlm.nih.gov/33713555/) |
| p.Ser376X | Nonsense | Truncation | Loss of function | BPS | [25784454](https://pubmed.ncbi.nlm.nih.gov/25784454/) |

The authors of the CHAND-defining study stated it directly: "Whereas in Bartsocas-Papas syndromes missense mutations are usually located within the serin/threonin kinase of RIPK4, the mutation detected in our family resides just outside of the kinase domain, which could explain the milder phenotype" ([PMID: 26129644](https://pubmed.ncbi.nlm.nih.gov/26129644/)). Notably, the **same p.Glu284Lys mutation also appeared in a fetus with a severe Bartsocas-Papas phenotype** in one report, indicating variable expressivity and the influence of genetic background ([PMID: 28940926](https://pubmed.ncbi.nlm.nih.gov/28940926/)).

- **Variant classification (ACMG/AMP):** p.Glu284Lys — Pathogenic (complete segregation in consanguineous kindred, functional plausibility).
- **Variant type:** Missense (predominant); nonsense/truncating variants cluster at the severe BPS end.
- **Allele frequency:** Extremely rare / absent in gnomAD (consistent with a severe recessive developmental gene).
- **Origin:** Germline.
- **Functional consequence:** **Hypomorphic loss-of-function** (partial reduction of kinase activity) for CHAND; complete loss of function for BPS.

**Modifier genes.** No formal modifier genes identified. The *position* of the mutation relative to the kinase domain is the principal determinant of severity. Genetic background likely contributes, given the same allele can produce different severities ([PMID: 28940926](https://pubmed.ncbi.nlm.nih.gov/28940926/)).

**Epigenetic information.** No CHAND-specific DNA methylation or histone-modification data are available. *Not applicable at present.*

**Chromosomal abnormalities.** CHAND is caused by point mutations, not large-scale rearrangements. Of note, within the broader pterygium spectrum a case of **uniparental disomy of chromosome 21** leading to a recessive RIPK4-region disorder has been reported ([PMID: 25691407](https://pubmed.ncbi.nlm.nih.gov/25691407/)) — relevant because *RIPK4* resides on chr 21.

---

## Section 5 — Environmental Information

- **Environmental factors:** None. CHAND is a purely genetic congenital disorder. *Not applicable.*
- **Lifestyle factors:** None. *Not applicable.*
- **Infectious agents:** None. CHAND is not infectious or pathogen-triggered. *Not applicable.*

*(These categories are included for template completeness; CHAND has no known non-genetic contributors.)*

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **biallelic hypomorphic missense variant in *RIPK4*** (recurrently p.Glu284Lys, outside the kinase domain) **leads to** reduced — but not abolished — RIPK4 serine/threonine kinase activity in keratinocytes. *(Demonstrated for kinase-dead BPS variants; inferred as partial for the CHAND allele given the milder phenotype.)*
2. Reduced RIPK4 catalytic output **results in** impaired phosphorylation of its principal substrate **IRF6 at Ser413 and Ser424** ([PMID: 25246526](https://pubmed.ncbi.nlm.nih.gov/25246526/)).
3. Hypophosphorylated IRF6 **fails to undergo full nuclear translocation and transactivation** — kinase-dead RIPK4 acts by "preventing RIPK4-mediated IRF6 activation and nuclear translocation" ([PMID: 25246526](https://pubmed.ncbi.nlm.nih.gov/25246526/)).
4. Diminished IRF6 transactivation **leads to** collapse of the downstream differentiation cascade **p63 → RIPK4 → IRF6 → GRHL3 → OVOL1/ELF3**, dysregulating keratinocyte terminal differentiation and cornification (SPRR1A/B, TGM1) ([PMID: 27667567](https://pubmed.ncbi.nlm.nih.gov/27667567/)).
5. In parallel (branch A — adhesion), loss of IRF6 output **results in** reduced transcription of **nectin-4/PVRL4** and altered desmosomal components (plakophilin-1/PKP1, desmoplakin), because "PVRL4 is transcriptionally regulated by IRF6, a RIPK4 phosphorylation target" ([PMID: 35220430](https://pubmed.ncbi.nlm.nih.gov/35220430/)).
6. In parallel (branch B — periderm), impaired RIPK4/IRF6 signaling **leads to** abnormal **periderm formation** with "aberrant ectopic localization of E-cadherin on the apical membrane of the outer peridermal cell layers" ([PMID: 25430793](https://pubmed.ncbi.nlm.nih.gov/25430793/)).
7. Defective cell–cell adhesion and periderm failure **result in** pathological **epithelial fusions/adhesions** (E-cadherin–dependent; [PMID: 29317263](https://pubmed.ncbi.nlm.nih.gov/29317263/)) — manifesting at the eyelid margins as **ankyloblepharon** and, at the severe end of the spectrum, as pterygia and orofacial synechiae.
8. Disrupted keratinocyte differentiation and barrier formation **lead to** abnormal hair shaft formation (**curly/sparse hair, "bubbly" morphology**) and **nail dysplasia**, completing the CHAND triad.

> Because the CHAND allele is hypomorphic (residual activity retained), the cascade is only partially impaired — hence the mild, survivable phenotype, in contrast to the complete pathway failure causing lethal BPS.

### Supporting detail by category

- **Molecular pathways:** RIPK4 signals through **NF-κB** and **Wnt/β-catenin** (phosphorylating Dvl2; stabilizing β-catenin) and the **IRF6 transcriptional axis** ([PMID: 29435596](https://pubmed.ncbi.nlm.nih.gov/29435596/); [PMID: 25784454](https://pubmed.ncbi.nlm.nih.gov/25784454/)). The p.Ser376X BPS mutation also "inhibited the stabilisation of β-catenin by RIPK4, and thus may additionally impair Wnt signalling" ([PMID: 25784454](https://pubmed.ncbi.nlm.nih.gov/25784454/)). GO:0016055 (Wnt signaling), GO:0038061 (NIK/NF-κB signaling).
- **Cellular processes:** Keratinocyte proliferation/differentiation homeostasis, cornification, periderm life-cycle, and cell–cell adhesion. RIPK4 activity is regulated by PKC and controlled by SCF-mediated turnover ([PMID: 29435596](https://pubmed.ncbi.nlm.nih.gov/29435596/)).
- **Protein dysfunction:** Hypomorphic (CHAND) vs catalytically dead (BPS) RIPK4; downstream, truncated IRF6 (p.Arg412X) undergoes rapid proteasomal degradation, illustrating that the axis can fail from either partner ([PMID: 25784454](https://pubmed.ncbi.nlm.nih.gov/25784454/)).
- **Immune / inflammatory:** The RIPK4–IRF6 axis also controls proinflammatory cytokine expression (CCL5, CXCL11) in keratinocytes, a "multifaceted role in barrier epithelial homeostasis" ([PMID: 27014863](https://pubmed.ncbi.nlm.nih.gov/27014863/)).
- **Tissue damage mechanism:** Not inflammatory/degenerative but **developmental** — failure to establish a competent periderm barrier and adhesion program during embryogenesis ([PMID: 28803895](https://pubmed.ncbi.nlm.nih.gov/28803895/)).

### Suggested ontology terms
- **GO (biological process):** GO:0030216 keratinocyte differentiation; GO:0070268 cornification; GO:0016055 Wnt signaling pathway; GO:0098742 cell-cell adhesion via plasma-membrane adhesion molecules.
- **CL (cell types):** CL:0000312 keratinocyte; CL:0000362 epidermal cell; peridermal/outer embryonic epithelial cell.

---

## Section 7 — Anatomical Structures Affected

**Organ / system level.**
- **Primary:** Integumentary system — skin/epidermis (UBERON:0001003 skin epidermis), hair/hair follicles (UBERON:0002073), nails (UBERON:0001705).
- **Ocular adnexa:** Eyelids (UBERON:0000158) — site of ankyloblepharon.
- **Oral/craniofacial:** Oral mucosa and palate — orofacial synechiae and periderm-dependent structures in the more severe spectrum ([PMID: 28803895](https://pubmed.ncbi.nlm.nih.gov/28803895/)).
- **Secondary:** Dentition (teeth).

**Tissue / cell level.**
- Stratified squamous **epithelium** (epidermis, oral epithelium).
- **Keratinocytes** (CL:0000312) — the cell-autonomous site of RIPK4 action; "RIP4 functions cell autonomously within the keratinocyte lineage" ([PMID: 12194825](https://pubmed.ncbi.nlm.nih.gov/12194825/)).
- **Periderm** (transient outer embryonic epithelial layer) — central to adhesion defects ([PMID: 25430793](https://pubmed.ncbi.nlm.nih.gov/25430793/); [PMID: 28803895](https://pubmed.ncbi.nlm.nih.gov/28803895/)).

**Subcellular level.**
- **Plasma membrane** (RIPK4 is membrane-associated; ectopic apical E-cadherin; [PMID: 11278382](https://pubmed.ncbi.nlm.nih.gov/11278382/), [PMID: 25430793](https://pubmed.ncbi.nlm.nih.gov/25430793/)) — GO:0005886.
- **Nucleus** (IRF6 nuclear translocation) — GO:0005634.
- **Desmosomes / adherens junctions** (PKP1, desmoplakin, nectin-4, E-cadherin) — GO:0030057 desmosome; GO:0005912 adherens junction.

**Localization / lateralization.** Manifestations are typically **bilateral** (ankyloblepharon affecting both eyelids; 20-nail involvement; generalized hair changes).

---

## Section 8 — Temporal Development

- **Onset:** **Congenital** — all core features present at birth (ankyloblepharon noted at birth and surgically corrected in infancy; hair and nail abnormalities present from birth) ([PMID: 29440852](https://pubmed.ncbi.nlm.nih.gov/29440852/)).
- **Onset pattern:** Developmental/congenital (not acute or acquired).
- **Progression:** **Stable, non-progressive.** Structural features persist; ankyloblepharon is correctable surgically. No staging applies.
- **Disease course:** **Chronic lifelong** (structural/cosmetic features), but **non-deteriorating**. No relapsing-remitting or episodic pattern.
- **Remission:** Not applicable (congenital structural anomalies); ankyloblepharon resolves with surgical lysis.
- **Critical period:** **Embryonic periderm development** is the window of vulnerability — the RIPK4/IRF6 axis acts during formation and function of the periderm to prevent pathological epithelial adhesions ([PMID: 28803895](https://pubmed.ncbi.nlm.nih.gov/28803895/)). There is no postnatal therapeutic window to reverse the developmental lesion.

---

## Section 9 — Inheritance and Population

**Epidemiology.** CHAND is **ultra-rare**; precise prevalence and incidence are **not established** (reported in only a handful of families worldwide). No reliable cases-per-100,000 figures exist.

**Inheritance.** **Autosomal recessive.** Initially described as autosomal dominant (Baughman 1971), re-evaluation of pedigree data showed the mode "is more likely to be autosomal recessive, with an instance of quasi-dominant transmission as a result of multiple consanguineous matings in the family" ([PMID: 490586](https://pubmed.ncbi.nlm.nih.gov/490586/)). Molecular confirmation: homozygous *RIPK4* c.850G>A segregating with disease ([PMID: 26129644](https://pubmed.ncbi.nlm.nih.gov/26129644/)).

- **Penetrance:** Appears complete for biallelic hypomorphic genotypes (full segregation in the reported kindred).
- **Expressivity:** **Variable** — the same p.Glu284Lys allele was associated with both CHAND and a severe BPS fetus ([PMID: 28940926](https://pubmed.ncbi.nlm.nih.gov/28940926/)), and RIPK4 variants span a continuum from mild ectodermal dysplasia to lethal BPS ([PMID: 33713555](https://pubmed.ncbi.nlm.nih.gov/33713555/); [PMID: 25691407](https://pubmed.ncbi.nlm.nih.gov/25691407/)).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Consanguinity:** Major contributor — reported families are consanguineous (Kuwaiti, Turkish; Dutch-extraction inbred kindred; [PMID: 5173251](https://pubmed.ncbi.nlm.nih.gov/5173251/), [PMID: 26129644](https://pubmed.ncbi.nlm.nih.gov/26129644/)).
- **Founder effects / carrier frequency:** Not established; *RIPK4* pathogenic alleles are very rare in population databases.

**Population demographics.** No ethnic predilection beyond the enrichment expected in consanguineous populations. Both sexes affected (autosomal). Geographic distribution reflects individual case reports (Kuwait, Turkey, Europe, India) rather than true endemicity. Age distribution: present from birth.

---

## Section 10 — Diagnostics

**Clinical diagnosis.** Recognition of the congenital triad — curly hair + ankyloblepharon + nail dysplasia — in the absence of cleft lip/palate and erosive scalp dermatitis (which would suggest AEC) ([PMID: 29440852](https://pubmed.ncbi.nlm.nih.gov/29440852/)).

**Specialized / laboratory tests.**
- **Hair shaft microscopy:** "bubbly/bubble hair" morphology is a distinctive, supportive microscopic feature ([PMID: 29440852](https://pubmed.ncbi.nlm.nih.gov/29440852/)).
- **Skin/keratinocyte immunostaining (research):** Loss of **PVRL4/nectin-4** expression in patient epidermis and primary keratinocytes, and altered desmosome morphology, can corroborate RIPK4 dysfunction ([PMID: 35220430](https://pubmed.ncbi.nlm.nih.gov/35220430/)).

**Genetic testing — the definitive diagnostic.**
- **Single-gene / targeted testing of *RIPK4*** (Sanger sequencing of coding region and exon–intron boundaries) is the confirmatory test, as used in the defining families ([PMID: 26129644](https://pubmed.ncbi.nlm.nih.gov/26129644/); [PMID: 33713555](https://pubmed.ncbi.nlm.nih.gov/33713555/)).
- **Whole-exome sequencing (WES)** is highly useful given phenotypic overlap across ectodermal dysplasias; it identified RIPK4 variants in pterygium-spectrum pedigrees ([PMID: 25691407](https://pubmed.ncbi.nlm.nih.gov/25691407/)).
- **Ectodermal dysplasia / orofacial clefting gene panels** should include *RIPK4*, *IRF6*, *CHUK (IKKA)*, *TP63*, *GRHL3*.
- **Chromosomal microarray** is relevant in rare cases (e.g., uniparental disomy of chr 21; [PMID: 25691407](https://pubmed.ncbi.nlm.nih.gov/25691407/)).

**Clinical criteria & differential diagnosis.** No formal consensus diagnostic criteria exist. The key diagnostic challenge is distinguishing CHAND from overlapping ectodermal dysplasias — "This case highlights the difficulties in trying to classify the ectodermal dysplasia syndromes on clinical features alone" ([PMID: 15347331](https://pubmed.ncbi.nlm.nih.gov/15347331/)).

| Differential | Causal gene | Distinguishing feature from CHAND |
|---|---|---|
| AEC / Hay-Wells syndrome | *TP63* (SAM domain) | Cleft lip/palate, erosive scalp dermatitis; AD ([PMID: 17910675](https://pubmed.ncbi.nlm.nih.gov/17910675/)) |
| Rapp-Hodgkin syndrome | *TP63* | Cleft, more severe facial features |
| Bartsocas-Papas syndrome | *RIPK4* (kinase domain) | Popliteal pterygia, severe clefting, often lethal ([PMID: 33713555](https://pubmed.ncbi.nlm.nih.gov/33713555/)) |
| Popliteal pterygium syndrome | *IRF6* / *RIPK4* | Pterygia across joints, genital malformation ([PMID: 25691407](https://pubmed.ncbi.nlm.nih.gov/25691407/)) |
| Van der Woude syndrome | *IRF6* | Lip pits, cleft; AD ([PMID: 25784454](https://pubmed.ncbi.nlm.nih.gov/25784454/)) |

**Screening.** Cascade carrier testing in consanguineous families and prenatal/preimplantation testing are feasible once the familial *RIPK4* variant is known. No population newborn screening exists.

---

## Section 11 — Outcome / Prognosis

- **Survival / life expectancy:** **Normal.** CHAND is the non-lethal end of the RIPK4 spectrum. This contrasts starkly with Bartsocas-Papas syndrome, where "most of the BPS cases reported to date are fatal either in the prenatal or neonatal period" ([PMID: 33713555](https://pubmed.ncbi.nlm.nih.gov/33713555/)), and with *Ripk4*-null mice, which die perinatally ([PMID: 12194825](https://pubmed.ncbi.nlm.nih.gov/12194825/)).
- **Mortality:** No disease-specific mortality in classic CHAND.
- **Morbidity / function:** Mild — primarily cosmetic (hair, nails) and ocular (ankyloblepharon, correctable). No major disability.
- **Complications:** Ankyloblepharon may transiently affect vision until corrected; potential skin-barrier fragility given RIPK4's barrier role ([PMID: 29317263](https://pubmed.ncbi.nlm.nih.gov/29317263/)).
- **Recovery potential:** Structural anomalies are managed, not cured; ankyloblepharon resolves fully after surgical lysis.
- **Prognostic factors:** The principal prognostic determinant is **mutation position/residual kinase activity** — variants outside the kinase domain predict milder disease ([PMID: 26129644](https://pubmed.ncbi.nlm.nih.gov/26129644/)), though variable expressivity means caution is warranted ([PMID: 28940926](https://pubmed.ncbi.nlm.nih.gov/28940926/)).

---

## Section 12 — Treatment

There is **no disease-modifying or curative therapy**; management is entirely **supportive, symptomatic, and multidisciplinary**.

| Intervention | Modality | NCIT suggestion |
|---|---|---|
| Surgical lysis of ankyloblepharon | Ophthalmic/oculoplastic surgery (often in infancy) ([PMID: 29440852](https://pubmed.ncbi.nlm.nih.gov/29440852/)) | NCIT:C15329 (Surgery) |
| Dermatologic care (skin barrier, hair/scalp) | Emollients, supportive skin care | NCIT:C15277 (Supportive Care) |
| Nail care | Protective/cosmetic nail management | NCIT:C15277 |
| Dental care | Restorative/orthodontic management | NCIT:C15313 (Dental procedure) |
| Genetic counseling | Risk assessment, family planning | NCIT:C15215 (Genetic Counseling) |

- **Pharmacotherapy / pharmacogenomics:** None established. *Not applicable.*
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** None in clinical use or trials for CHAND. Because the lesion is a developmental, cell-autonomous keratinocyte deficit established in utero, post-natal gene therapy faces fundamental timing barriers.
- **Experimental treatments / clinical trials:** No CHAND-specific trials (no NCT identifiers).
- **Treatment strategy:** Supportive, individualized to each patient's manifestations.

---

## Section 13 — Prevention

- **Primary prevention:** Not possible for an affected individual; at the family/population level, **genetic counseling and reproductive planning** in consanguineous families is the principal preventive measure.
- **Genetic screening:** **Carrier testing, cascade screening, prenatal diagnosis, and preimplantation genetic diagnosis** are feasible once the familial *RIPK4* variant is identified ([PMID: 25691407](https://pubmed.ncbi.nlm.nih.gov/25691407/) notes clinical implications "for genetic counseling of families with pterygia syndromes").
- **Counseling:** Autosomal recessive counseling — 25% recurrence risk for carrier couples; emphasize variable expressivity, since the same allele can yield markedly different severities ([PMID: 28940926](https://pubmed.ncbi.nlm.nih.gov/28940926/)).
- **Secondary/tertiary prevention:** Early recognition and surgical correction of ankyloblepharon; routine dermatologic and dental surveillance.
- **Immunization / public health / environmental interventions:** *Not applicable* (non-infectious, non-environmental).

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy:** No naturally occurring CHAND-equivalent disease is documented in companion animals or wildlife (no OMIA entry for a CHAND analog).
- **Orthologous gene:** *Ripk4* is conserved in mouse (*Mus musculus*; NCBI Gene 72388) and other vertebrates; the pathway (p63–RIPK4–IRF6–GRHL3) is evolutionarily conserved, with functional parallels demonstrated in *Xenopus* (dominant-negative IRF6 phenocopies RIPK4 loss) ([PMID: 25430793](https://pubmed.ncbi.nlm.nih.gov/25430793/)).
- **Comparative biology:** "Homologous human and mouse phenotypes are observed for IRF6, IKKA, and RIPK4" — loss of these alleles in mouse causes perinatal lethality with cutaneous, limb, and craniofacial defects paralleling the human spectrum ([PMID: 28643456](https://pubmed.ncbi.nlm.nih.gov/28643456/)).
- **Zoonotic potential / transmission:** *Not applicable* (genetic, non-transmissible).

---

## Section 15 — Model Organisms

No model specifically engineered to recapitulate **CHAND** (the mild hypomorphic allele) exists, but the RIPK4 pathway is well-modeled at its severe end:

| Model | Type | Key phenotype | Recapitulation | PMID |
|---|---|---|---|---|
| *Ripk4⁻/⁻* mouse (full KO) | Mammalian knockout | Perinatal lethality; abnormal epidermal differentiation; epithelial fusions; abnormal hair follicles | Models the **severe (BPS)** end; E-cadherin–dependent fusions | [12194825](https://pubmed.ncbi.nlm.nih.gov/12194825/), [25430793](https://pubmed.ncbi.nlm.nih.gov/25430793/) |
| Epidermis-specific *Ripk4* KO mouse | Conditional KO | Allows cornification but impairs skin-barrier formation | Dissects barrier vs fusion roles | [29317263](https://pubmed.ncbi.nlm.nih.gov/29317263/) |
| *Ripk4⁻/⁻*; E-cadherin cKO mouse | Compound genetic | Rescue of tail-to-body and oral epithelial fusions | Proves fusions are E-cadherin–dependent | [29317263](https://pubmed.ncbi.nlm.nih.gov/29317263/) |
| KRT14-Irf6 rescue mouse | Transgenic rescue | Partial rescue of Irf6-KO; survives perinatal period | Validates RIPK4→IRF6 epistasis | [28643456](https://pubmed.ncbi.nlm.nih.gov/28643456/) |
| *Xenopus* dominant-negative IRF6 | Amphibian | Periderm/adhesion defects phenocopying RIPK4 loss | Confirms RIPK4–IRF6 axis in periderm | [25430793](https://pubmed.ncbi.nlm.nih.gov/25430793/) |
| Primary human keratinocytes; cell-based kinase assays | In vitro | IRF6 phosphorylation, nuclear translocation, nectin-4 expression | Directly tests variant functional consequences | [25246526](https://pubmed.ncbi.nlm.nih.gov/25246526/), [35220430](https://pubmed.ncbi.nlm.nih.gov/35220430/) |

**Model limitation:** Full-KO mice model lethal BPS, not the *survivable, hypomorphic* CHAND phenotype. A **knock-in mouse carrying p.Glu284Lys** would be the ideal (currently missing) model to capture CHAND specifically.

**Resources:** MGI (*Ripk4*), IMPC/KOMP (conditional alleles), Xenbase (Xenopus), Cellosaurus/ATCC (keratinocyte lines).

---

## Mechanistic Model (Synthesis)

```
   Biallelic hypomorphic RIPK4 variant (p.Glu284Lys, OUTSIDE kinase domain)
                         │  (partial ↓ kinase activity — hypomorph)
                         ▼
          ↓ Phosphorylation of IRF6 (Ser413/Ser424)         [PMID 25246526]
                         │
                         ▼
          ↓ IRF6 nuclear translocation & transactivation
                         │
        ┌────────────────┼─────────────────────┐
        ▼                ▼                     ▼
  DIFFERENTIATION    ADHESION (branch A)   PERIDERM (branch B)
  p63→RIPK4→IRF6→    ↓ nectin-4/PVRL4      ectopic apical E-cadherin
  GRHL3→OVOL1/ELF3   ↓ PKP1/desmoplakin    abnormal periderm
  (SPRR1A/B, TGM1)   [PMID 35220430]       [PMID 25430793]
        │                │                     │
        └────────────────┼─────────────────────┘
                         ▼
        Defective keratinocyte differentiation + epithelial adhesions
                         ▼
   CURLY/SPARSE HAIR  +  ANKYLOBLEPHARON  +  NAIL DYSPLASIA   (CHAND triad)

   ── Severity switch ──
   Variant OUTSIDE kinase domain → residual activity → CHAND (mild, survives)
   Variant INSIDE kinase domain  → activity abolished → Bartsocas-Papas (lethal)
```

**Upstream vs downstream:** The *RIPK4* mutation is the upstream initiating lesion; IRF6 hypophosphorylation is the proximal node; GRHL3/OVOL1/nectin-4/E-cadherin dysregulation and periderm failure are downstream effectors; the clinical triad is the terminal manifestation. The single most important determinant separating CHAND from lethal BPS is the **degree of residual RIPK4 kinase activity**, which tracks with mutation position.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [26129644](https://pubmed.ncbi.nlm.nih.gov/26129644/) | Novel RIPK4 mutation, BPS/CHAND kindred | **Defining**: establishes p.Glu284Lys, AR inheritance, genotype–phenotype rule |
| [28940926](https://pubmed.ncbi.nlm.nih.gov/28940926/) | Confirmation RIPK4 causes CHAND | Confirms causation; defines triad; shows variable expressivity (same allele → severe fetus) |
| [25246526](https://pubmed.ncbi.nlm.nih.gov/25246526/) | RIPK4–IRF6 signaling axis | **Core mechanism**: RIPK4 phosphorylates IRF6 Ser413/424; kinase-dead variant blocks activation |
| [25430793](https://pubmed.ncbi.nlm.nih.gov/25430793/) | RIPK4–IRF6 prevents epithelial fusions | Periderm/adhesion defect; ectopic apical E-cadherin |
| [35220430](https://pubmed.ncbi.nlm.nih.gov/35220430/) | RIPK4 regulates cell–cell adhesion | Loss of IRF6-dependent nectin-4/PVRL4, desmosomal changes |
| [11278382](https://pubmed.ncbi.nlm.nih.gov/11278382/) | PKK (RIPK4) characterization | Protein architecture: kinase + 11 ankyrin repeats; 21q22.3 |
| [490586](https://pubmed.ncbi.nlm.nih.gov/490586/) | Re-evaluation of CHANDS | Establishes autosomal recessive inheritance |
| [33713555](https://pubmed.ncbi.nlm.nih.gov/33713555/) | Homozygous RIPK4 in severe BPS | Kinase-domain variant (p.Asp161His) abolishes activity → lethal end |
| [25784454](https://pubmed.ncbi.nlm.nih.gov/25784454/) | IRF6/RIPK4 mutations dysregulate signaling | Truncating variants; β-catenin/Wnt impairment |
| [25691407](https://pubmed.ncbi.nlm.nih.gov/25691407/) | Pterygium spectrum expansion | Spectrum concept; UPD chr21; counseling implications |
| [12194825](https://pubmed.ncbi.nlm.nih.gov/12194825/) | RIP4 essential for keratinocyte differentiation | Mouse KO: perinatal lethality, cell-autonomous keratinocyte role |
| [29317263](https://pubmed.ncbi.nlm.nih.gov/29317263/) | Keratinocyte-specific RIPK4 ablation | Barrier vs fusion dissection; E-cadherin dependence |
| [28643456](https://pubmed.ncbi.nlm.nih.gov/28643456/) | IRF6 basal-epithelium rescue | Confirms homologous human/mouse IRF6/IKKA/RIPK4 phenotypes |
| [27667567](https://pubmed.ncbi.nlm.nih.gov/27667567/) | RIPK4–ELF3 relationship | Positions RIPK4 upstream of IRF6–GRHL3–ELF3 hierarchy |
| [27014863](https://pubmed.ncbi.nlm.nih.gov/27014863/) | RIPK4 proinflammatory cytokines | IRF6-mediated CCL5/CXCL11 induction |
| [29435596](https://pubmed.ncbi.nlm.nih.gov/29435596/) | RIPK4 activity control | Dvl2/PKP1/IRF6 phosphorylation; NF-κB; SCF regulation |
| [28803895](https://pubmed.ncbi.nlm.nih.gov/28803895/) | Periderm life-cycle | Periderm biology; p63-controlled IRF6/RIPK4/GRHL3 program |
| [15347331](https://pubmed.ncbi.nlm.nih.gov/15347331/) | AEC/Rapp-Hodgkin/CHAND overlap | Clinical overlap, diagnostic difficulty, wiry hair, hypohidrosis |
| [10886756](https://pubmed.ncbi.nlm.nih.gov/10886756/) | AEC and CHAND overlap | Phenotypic overlap documentation |
| [29440852](https://pubmed.ncbi.nlm.nih.gov/29440852/) | CHAND case ("bubble hair") | Clinical features; bubbly hair; AR; no cleft/hypohidrosis |
| [5173251](https://pubmed.ncbi.nlm.nih.gov/5173251/) | Original CHANDS family | First description, inbred kindred |
| [17910675](https://pubmed.ncbi.nlm.nih.gov/17910675/) | Hay-Wells TP73L mutation | Differential diagnosis (TP63/AEC) |
| [29186361](https://pubmed.ncbi.nlm.nih.gov/29186361/) | PKK deletion promotes tumorigenesis | RIPK4 keratinocyte tumor-suppressor role |

*(Additional RIPK4 oncology papers — melanoma/colon/osteosarcoma — inform RIPK4's broader NF-κB/Wnt biology but are tangential to CHAND developmental pathology.)*

---

## Limitations and Knowledge Gaps

1. **Extreme rarity → small evidence base.** CHAND is defined by a handful of families; prevalence/incidence are unknown and formal natural-history or QoL data are absent.
2. **Functional data for the CHAND allele are inferred, not directly demonstrated.** The hypomorphic (residual-activity) nature of p.Glu284Lys is inferred from the milder phenotype and its position outside the kinase domain; a direct side-by-side kinase/IRF6-activation assay of p.Glu284Lys vs kinase-dead BPS variants has not been published. This is the key unproven step in the causal chain.
3. **Variable expressivity undermines strict genotype–phenotype rules.** The same p.Glu284Lys allele produced a severe BPS fetus in one report ([PMID: 28940926](https://pubmed.ncbi.nlm.nih.gov/28940926/)), implying modifier genes and/or background effects that remain uncharacterized.
4. **No CHAND-specific animal model.** Existing mouse models are full or conditional knockouts modeling the lethal end, not a hypomorphic CHAND model.
5. **No omics/epigenomic data** specific to CHAND patients (no transcriptomic, proteomic, methylation datasets).
6. **No therapeutics pipeline.** Management is supportive only; the developmental, in-utero timing of the lesion is a fundamental barrier to gene/molecular therapy.

---

## Proposed Follow-up Experiments / Actions

1. **Functional validation of p.Glu284Lys.** Perform quantitative in-vitro kinase and IRF6-transactivation assays comparing p.Glu284Lys against wild-type and kinase-dead RIPK4 to empirically confirm residual (hypomorphic) activity — closing the key inferential gap in the causal chain.
2. **Generate a *Ripk4^E284K* knock-in mouse** to test whether it recapitulates the mild, survivable CHAND triad (vs the lethal null), directly validating the severity model.
3. **Modifier screen.** Exome/genome analysis of individuals sharing the same *RIPK4* allele but discordant severity (CHAND vs BPS) to identify genetic modifiers explaining variable expressivity.
4. **Patient keratinocyte / organoid omics.** RNA-seq and proteomics of CHAND patient-derived keratinocytes/skin organoids to map the downstream IRF6→GRHL3/OVOL1/nectin-4 program quantitatively and identify candidate biomarkers.
5. **Curate structured gene–phenotype annotations** (HPO frequencies, UBERON/CL/GO terms) into the target knowledge base using the mappings proposed in Sections 3, 6, and 7.
6. **Establish an international RIPK4-spectrum registry** to accrue prevalence, natural-history, and genotype–phenotype data across CHAND, PPS, and BPS.

---

*Report compiled from 33 primary sources across 5 investigation iterations. Evidence types: human clinical (case reports, consanguineous kindreds), model organism (mouse KO, Xenopus), and in-vitro functional (keratinocyte kinase/transactivation assays). All mechanistic claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](CHAND_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](CHAND_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 23 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008959` (2 mentions) - the report calls it "MONDO"; MONDO calls it **CHAND syndrome**
- `HP:0010729` (1 mention) - the report calls it "Ankyloblepharon"; HP calls it **Cherry red spot of the macula**
- `UBERON:0000158` (1 mention) - the report calls it "Ocular adnexa:** Eyelids"; UBERON calls it **membranous layer**
- `NCIT:C15277` (2 mentions) - the report calls it "Supportive Care", "Protective/cosmetic nail management"; NCIT calls it **Mastectomy**
- `NCIT:C15313` (1 mention) - the report calls it "Dental procedure"; NCIT calls it **Radiation Therapy**
- `NCIT:C15215` (1 mention) - the report calls it "Genetic Counseling"; NCIT calls it **Cryosurgery**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0098742` (obsolete cell-cell adhesion via plasma-membrane adhesion molecules) (1 mention) - replaced by `GO:0098609`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000164` (1 mention) - the report calls it "Abnormality of the teeth"; HP calls it **Abnormality of the dentition**, and lists "Abnormality of the teeth" among its other names
- `GO:0016055` (2 mentions) - the report calls it "Wnt signaling"; GO calls it **Wnt signaling pathway**
- `GO:0038061` (1 mention) - the report calls it "NIK/NF-κB signaling"; GO calls it **non-canonical NF-kappaB signal transduction**, and lists "NIK/NF-kappaB signaling" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15277` - called "Supportive Care", "Protective/cosmetic nail management"