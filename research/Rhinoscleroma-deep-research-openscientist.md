---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T14:51:57.987360'
end_time: '2026-09-25T15:07:10.859432'
duration_seconds: 912.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Rhinoscleroma
  mondo_id: MONDO:0005945
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
citation_count: 21
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 23
  on_topic: 17
  off_topic: 1
  off_topic_references:
  - PMID:35130876
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 35
  verified: 34
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 21
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0005945
    reported_labels:
    - MONDO
    ontology_label: rhinoscleroma
  - term_id: HP:0025095
    reported_labels:
    - Nasal crusting
    ontology_label: Sneeze
  - term_id: HP:0009928
    reported_labels:
    - Nasal septal perforation
    ontology_label: Thick nasal alae
  - term_id: HP:0012781
    reported_labels:
    - Upper airway obstruction
    ontology_label: Mid-frequency hearing loss
  - term_id: UBERON:0002110
    reported_labels:
    - Paranasal sinuses
    ontology_label: gallbladder
  labels_variant: 1
  obsolete_terms:
  - term_id: NCIT:C15788
    ontology_label: Clinical Trials, Diagnosis
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Rhinoscleroma-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rhinoscleroma-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rhinoscleroma
- **MONDO ID:** MONDO:0005945 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Rhinoscleroma** covering all of the
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

# Rhinoscleroma (MONDO:0005945): A Comprehensive Disease Characteristics Report

## Summary

**Rhinoscleroma (RS)** is a rare, chronic, progressive granulomatous infection of the upper respiratory tract caused by the Gram-negative bacterium ***Klebsiella pneumoniae* subsp. *rhinoscleromatis*** (also written *Klebsiella rhinoscleromatis*), a human-specific pathogen uniformly bearing the **K3 capsular serotype**. The disease begins in and predominantly affects the nasal cavity (95–100% of cases) but descends to involve the nasopharynx, larynx, trachea, and bronchi, producing progressive fibrosis and airway stenosis. It is endemic to resource-poor, rural regions of Africa, Central/South America, the Middle East, South and Southeast Asia, and Central/Eastern Europe, and is strongly associated with poor socioeconomic conditions, crowding, and malnutrition. Its defining, pathognomonic histopathology is the presence of **Mikulicz cells** (large foamy vacuolated macrophages harboring intracellular bacilli) and **Russell-body-laden plasma cells**.

Mechanistically, RS is now understood as a disorder of aberrant, IL-10-skewed host innate immunity. The bacterium is phagocytosed but survives intracellularly within macrophage vacuoles. Landmark murine work established that Mikulicz cells are **atypical inflammatory monocytes recruited from the bone marrow** (in a CCR2-independent manner) whose maturation into the foamy disease-signature cell is **causally dependent on IL-10**. This immunosuppressive milieu permits persistent intracellular bacterial survival, chronic granulomatous inflammation with a dense plasmacytic infiltrate, and ultimately fibrosis and cicatricial airway stenosis. The K3 capsule is a virulence factor required for full bacterial fitness but is dispensable for Mikulicz-cell formation.

Diagnosis rests on **deep-biopsy histopathology** because culture is positive in only 50–60% of cases. Treatment requires **prolonged (weeks-to-months) courses of macrophage-penetrating antibiotics** — principally fluoroquinolones such as ciprofloxacin, sometimes with rifampicin — with surgical intervention reserved for advanced stenosis or deformity. Because the organism is intracellular, recurrence is common and residual structural airway sequelae are frequent even after microbiological cure. This report synthesizes 10 confirmed findings across 28 reviewed papers, organized against the 15-section disease-characteristics template.

---

## 1. Disease Information

**Overview.** Rhinoscleroma is a chronic, slowly progressive granulomatous infection of the nose and upper airways. As stated in [PMID: 29381692](https://pubmed.ncbi.nlm.nih.gov/29381692/): *"Rhinoscleroma is a human specific chronic granulomatous infection of the nose and upper airways caused by the Gram-negative bacterium Klebsiella pneumoniae subsp. rhinoscleromatis."* The disease is human-specific, meaning no natural animal reservoir has been identified. It follows an insidious clinical course over months to years.

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0005945 |
| ICD-10 | A48.8 / J31.0 (associated); classically coded under specific bacterial diseases |
| ICD-11 | 1C1G (or equivalent scleroma code) |
| MeSH | Rhinoscleroma (D012225) |
| Causative organism (NCBI Taxonomy) | *Klebsiella pneumoniae* subsp. *rhinoscleromatis* |
| OMIM | No Mendelian OMIM entry (infectious disease, not a monogenic disorder) |
| Orphanet | Scleroma / rhinoscleroma (rare infectious disease) |

**Synonyms / alternative names:** Scleroma; respiratory scleroma; nasal scleroma; scleroma respiratorium; Mikulicz disease (historical, in reference to the characteristic cell — not to be confused with Mikulicz syndrome/IgG4 disease); von Frisch disease (after Anton von Frisch, who identified the bacillus in 1882).

**Data provenance.** Information on RS is derived almost exclusively from **aggregated disease-level resources** — case reports, small retrospective clinical series (typically n = 6–88), histopathological/ultrastructural studies, and one well-characterized murine model. There is no large EHR-derived or registry cohort; the disease's rarity in high-income countries means most literature is case-based.

---

## 2. Etiology

**Primary cause (infectious).** RS is an infectious disease. The sole established causal agent is ***Klebsiella pneumoniae* subsp. *rhinoscleromatis***, a Gram-negative, encapsulated, facultatively anaerobic bacillus. All disease-associated strains carry the **K3 capsular serotype**: [PMID: 29381692](https://pubmed.ncbi.nlm.nih.gov/29381692/) reports *"All K. rhinoscleromatis strains are of K3 serotype, suggesting that CPS can be an important driver of rhinoscleroma disease."* One recent case report ([PMID: 42698439](https://pubmed.ncbi.nlm.nih.gov/42698439/)) raises the possibility of microbial complexity/co-isolation in some cases, but the pathogenic contribution of co-isolated organisms remains unproven.

**Environmental risk factors.** The dominant risk factors are environmental and socioeconomic:
- Poor socioeconomic conditions, crowding, and poor hygiene: [PMID: 29578083](https://pubmed.ncbi.nlm.nih.gov/29578083/) — *"Rhinoscleroma is predominantly reported in rural areas, in the presence of poor socio-economic conditions."*
- Rural residence and malnutrition (supported across multiple case series, e.g., [PMID: 35183701](https://pubmed.ncbi.nlm.nih.gov/35183701/), which describes a patient "living in crowded conditions with malnutrition and poor hygiene").
- Prolonged close contact is thought necessary given the low communicability.

**Immunodeficiency as a risk factor.** Immunocompromise (notably HIV, diabetes) is associated with disease and with unusually extensive/atypical presentations. In the French national series ([PMID: 18947330](https://pubmed.ncbi.nlm.nih.gov/18947330/)): *"Two patients with sporadic disease were positive for HIV infection."* An extensive nasopharyngeal case with bone lysis occurred in a diabetic, hypertensive patient ([PMID: 33643651](https://pubmed.ncbi.nlm.nih.gov/33643651/)).

**Genetic susceptibility.** Familial clustering and consanguinity suggest a host genetic-susceptibility component overlaid on the infectious etiology. The French series ([PMID: 18947330](https://pubmed.ncbi.nlm.nih.gov/18947330/)) reported: *"The 3 patients with a familial history of RS presented with early-onset forms of RS"* and *"Two unrelated consanguineous families were identified, 1 of which included 2 affected siblings."* This pattern is consistent with an autosomal-recessive susceptibility trait, though no causal gene has been identified. RS is additionally linked to *"qualitatively and quantitatively abnormal cell-mediated immunity"* ([PMID: 29578083](https://pubmed.ncbi.nlm.nih.gov/29578083/)).

**Protective factors.** No genetic protective variants have been identified. The principal protective factors are environmental — improved sanitation, hygiene, nutrition, and housing — as inferred from the disease's disappearance from high-income regions.

**Gene–environment interaction.** The most plausible model is that the poorly-communicable pathogen produces overt disease only when host factors (genetic susceptibility affecting cell-mediated immunity and/or acquired immunodeficiency) combine with heavy/prolonged environmental exposure under conditions of crowding and malnutrition. Direct GxE data are lacking.

---

## 3. Phenotypes

The clinical phenotype evolves through the disease stages (see §8). Core manifestations and suggested HPO terms:

| Phenotype | Type | Frequency / notes | Suggested HPO |
|-----------|------|-------------------|---------------|
| Nasal obstruction | Symptom / sign | Most common presenting complaint | HP:0001742 (Nasal obstruction) |
| Rhinorrhea | Symptom | Common, often purulent/foul (catarrhal stage) | HP:0031417 (Rhinorrhea) |
| Epistaxis | Sign | Common | HP:0000421 (Epistaxis) |
| Nasal crusting / atrophic rhinitis | Sign | Catarrhal-atrophic stage | HP:0025095 (Nasal crusting) |
| Nasal/facial mass, deformity ("Hebra nose") | Physical manifestation | Granulomatous/sclerotic stages | HP:0000366 (Abnormality of the nose) |
| Dysphonia / hoarseness | Symptom | Laryngeal involvement | HP:0001609 (Hoarse voice) |
| Stridor | Sign | Laryngotracheal stenosis | HP:0010307 (Stridor) |
| Dysphagia | Symptom | Pharyngeal involvement | HP:0002015 (Dysphagia) |
| Anosmia / cacosmia | Symptom | Reported (e.g., PMID 33643651) | HP:0000458 (Anosmia) |
| Headache | Symptom | With extensive/nasopharyngeal disease | HP:0002315 (Headache) |
| Nasal septal perforation | Sign | Advanced disease | HP:0009928 (Nasal septal perforation) |
| Upper airway stenosis | Physical manifestation | Sclerotic sequela; residual even after cure | HP:0012781 (Upper airway obstruction) |

Supporting evidence — [PMID: 21410904](https://pubmed.ncbi.nlm.nih.gov/21410904/): *"The most common complaint is nasal obstruction, other symptoms include; rhinorrhea, epistaxis, dysphagia, stridor, and dysphonia."* In this 88-case endemic series, ~18% presented atypically. Residual airway stenosis is near-universal even after microbiological cure — [PMID: 17086321](https://pubmed.ncbi.nlm.nih.gov/17086321/): *"all of them presented some degree of upper airway stenosis."*

**Onset, severity, progression, frequency.** Onset is typically in young to middle adulthood (early onset in familial cases). Severity ranges from mild (early catarrhal) to severe (obstructive/disfiguring). The course is chronic and progressive over years. The nose is affected in essentially all cases (see §7).

**Quality-of-life impact.** No formal EQ-5D/SF-36 studies exist. Inferred impact is substantial: chronic nasal obstruction, disfiguring facial deformity (social stigma), voice change, and potentially life-threatening airway compromise. [PMID: 30168726](https://pubmed.ncbi.nlm.nih.gov/30168726/) notes symptoms "can be devastating and in some cases fatal."

---

## 4. Genetic/Molecular Information

**Not a Mendelian disorder.** RS is an infectious disease with no causal human gene, no pathogenic germline/somatic variants, no ClinVar/OMIM disease-variant entries, no relevant allele-frequency data, and no chromosomal abnormalities. Genetic testing has no diagnostic role.

**Host susceptibility (candidate/inferred).** Familial and consanguineous clustering with early onset ([PMID: 18947330](https://pubmed.ncbi.nlm.nih.gov/18947330/)) suggests an autosomal-recessive host-susceptibility locus affecting cell-mediated immunity, but no gene has been mapped. This is the single most notable knowledge gap on the human-genetics side.

**Pathogen genetics (the relevant "molecular" axis).** The disease-relevant genetics reside in the bacterium:
- **K3 capsular polysaccharide (CPS) locus** — uniform across strains; encodes the K3 capsule that is an established virulence factor. A capsule-export mutant (KR *cps-*) is strongly attenuated ([PMID: 29381692](https://pubmed.ncbi.nlm.nih.gov/29381692/)): *"a K. rhinoscleromatis CPS mutant (KR cps-) is strongly attenuated and that mice infected with a high dose of KR cps- are still able to induce Mikulicz cells formation, unlike a K. pneumoniae capsule mutant, and to partially recapitulate the characteristic strong production of IL-10."* Complementary *K. pneumoniae* CPS work ([PMID: 39980691](https://pubmed.ncbi.nlm.nih.gov/39980691/)) confirms CPS is *"a critical virulence factor, often evading phagocytosis"* while modulating host-cell internalization.

---

## 5. Environmental Information

- **Environmental factors:** Poor sanitation, crowded/unhygienic living conditions, and rural environments are the dominant drivers ([PMID: 29578083](https://pubmed.ncbi.nlm.nih.gov/29578083/); [PMID: 25933455](https://pubmed.ncbi.nlm.nih.gov/25933455/)). No chemical toxin or occupational exposure is implicated.
- **Lifestyle factors:** Malnutrition and poor personal hygiene are recurrent themes in case reports ([PMID: 35183701](https://pubmed.ncbi.nlm.nih.gov/35183701/)). No association with smoking/alcohol has been established.
- **Infectious agent:** ***Klebsiella pneumoniae* subsp. *rhinoscleromatis*** (Gram-negative bacillus, K3 serotype). CHEBI-relevant entity: the K3 capsular polysaccharide. The organism is of low communicability, requiring prolonged close contact; humans are the only known host.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Exposure/inoculation:** Prolonged close contact under crowded, unhygienic conditions **leads to** colonization of the nasal mucosa by K3-encapsulated *K. pneumoniae* subsp. *rhinoscleromatis*.
2. **Phagocytosis and intracellular survival:** The bacterium is phagocytosed by monocytes/macrophages but **survives intracellularly** within cytoplasmic vacuoles rather than being cleared (viable bacilli demonstrated in Mikulicz-cell vacuoles by electron microscopy; [PMID: 333340](https://pubmed.ncbi.nlm.nih.gov/333340/)).
3. **Inflammatory-monocyte recruitment:** Infection **results in** recruitment of atypical inflammatory monocytes from the bone marrow, in a **CCR2-independent** manner ([PMID: 23554169](https://pubmed.ncbi.nlm.nih.gov/23554169/)).
4. **IL-10 induction (branch point / key driver):** *K. rhinoscleromatis* (unlike *K. pneumoniae*) **induces strong IL-10 production**, creating an immunosuppressive milieu ([PMID: 29381692](https://pubmed.ncbi.nlm.nih.gov/29381692/); [PMID: 23554169](https://pubmed.ncbi.nlm.nih.gov/23554169/)).
5. **Mikulicz-cell maturation:** Under this IL-10-dominated environment, the recruited inflammatory monocytes **mature into foamy, vacuolated Mikulicz macrophages** laden with intracellular bacilli. IL-10 is **causally required** — in IL-10-deficient mice, very few Mikulicz cells form ([PMID: 23554169](https://pubmed.ncbi.nlm.nih.gov/23554169/)).
6. **Plasmacytic response / Russell bodies:** Concurrently, a **dense plasma-cell infiltrate** develops; overproduction of immunoglobulin distends the plasma-cell rough ER into **Russell bodies** ([PMID: 333340](https://pubmed.ncbi.nlm.nih.gov/333340/); [PMID: 8784898](https://pubmed.ncbi.nlm.nih.gov/8784898/)). This defines the **granulomatous (hypertrophic) stage**.
7. **Persistence:** The immunosuppressive/IL-10 milieu **permits ongoing bacterial persistence** and lesion growth (granulomatous mass).
8. **Fibrosis/sclerosis:** Chronic granulomatous inflammation **leads to** fibrosis and scarring — the **sclerotic stage** — producing cicatricial **airway stenosis** and deformity, which persist even after the bacteria are cleared.

```
Exposure ──► Intracellular Klebsiella (K3+) survival in macrophages
                          │
                          ▼
        CCR2-INDEPENDENT recruitment of bone-marrow inflammatory monocytes
                          │
             strong IL-10 induction  ◄── (K. rhinoscleromatis-specific)
                          │  (causally required — KO mice: few Mikulicz cells)
                          ▼
     Maturation into foamy MIKULICZ CELLS (intracellular bacilli persist)
                          │
     + dense plasma-cell infiltrate ──► RUSSELL BODIES (distended rough ER)
                          │  = GRANULOMATOUS STAGE
                          ▼
        Chronic inflammation ──► FIBROSIS/SCLEROSIS ──► airway stenosis
                                   = SCLEROTIC STAGE (irreversible sequela)
```

### Category detail

- **Immune involvement (central):** IL-10-driven immunosuppression is the linchpin. RS represents a failure of Th1/macrophage clearance with an M2-like, IL-10-skewed macrophage phenotype; abnormal cell-mediated immunity is documented ([PMID: 29578083](https://pubmed.ncbi.nlm.nih.gov/29578083/)). Suggested GO: **GO:0032613 (interleukin-10 production)**, **GO:0002444 (myeloid leukocyte mediated immunity)**, **GO:0006954 (inflammatory response)**, **GO:0071216 (cellular response to biotic stimulus)**.
- **Cellular processes:** Granulomatous inflammation; monocyte-to-macrophage differentiation; intracellular bacterial persistence; plasma-cell hyperactivity. Suggested CL: **CL:0000860 (classical/inflammatory monocyte)**, **CL:0000235 (macrophage)** — the Mikulicz cell, **CL:0000786 (plasma cell)**.
- **Protein dysfunction / biochemistry:** Distension of plasma-cell rough ER by immunoglobulin aggregation forms Russell bodies. Mikulicz-cell vacuoles are phagolysosomal compartments harboring bacilli.
- **Molecular pathways:** IL-10 → JAK1/TYK2 → STAT3 signaling is the presumed axis (inferred from IL-10 biology, not directly demonstrated in RS tissue). The K3 CPS mediates immune evasion/anti-phagocytic virulence.
- **Tissue-damage mechanism:** Fibrosis/scarring secondary to chronic granulomatous inflammation (not oxidative-stress or ischemia driven).
- **Molecular profiling:** No human transcriptomic/proteomic/metabolomic datasets exist. Mechanistic data derive from the murine model and ultrastructural pathology.

**Upstream vs downstream:** Bacterial intracellular persistence and IL-10 induction are **upstream**; Mikulicz-cell maturation and plasmacytosis are **midstream**; fibrosis/stenosis is the **downstream** irreversible endpoint.

---

## 7. Anatomical Structures Affected

**Organ level.** Primary organ: the **nose/nasal cavity** (UBERON:0001707, nasal cavity), affected in **95–100%** of cases ([PMID: 17359555](https://pubmed.ncbi.nlm.nih.gov/17359555/): *"The nose is involved in 95-100 per cent of cases."*). Descending respiratory-tract spread with quantified frequencies ([PMID: 19146007](https://pubmed.ncbi.nlm.nih.gov/19146007/)): *"Rhinoscleroma primarily affects the nasal cavity but the nasopharynx (18%-43%), larynx (15%-40%), trachea (12%) and bronchi (2% to 7%) can also be involved. However, the paranasal sinuses are usually free of disease."*

| Site | UBERON | Frequency |
|------|--------|-----------|
| Nasal cavity | UBERON:0001707 | 95–100% |
| Nasopharynx | UBERON:0001728 | 18–43% |
| Larynx | UBERON:0001737 | 15–40% |
| Trachea | UBERON:0003126 | ~12% |
| Bronchi | UBERON:0002185 | 2–7% |
| Paranasal sinuses | UBERON:0002110 | Usually spared |

**Body system:** Respiratory system (UBERON:0001004). **Secondary/rare involvement:** oral cavity/lip (extra-respiratory; [PMID: 35183701](https://pubmed.ncbi.nlm.nih.gov/35183701/), [PMID: 25933455](https://pubmed.ncbi.nlm.nih.gov/25933455/)); rare regional cervical lymph node spread ([PMID: 30364372](https://pubmed.ncbi.nlm.nih.gov/30364372/), [PMID: 572955](https://pubmed.ncbi.nlm.nih.gov/572955/)); rare skull-base/clivus bone lysis in extensive disease ([PMID: 33643651](https://pubmed.ncbi.nlm.nih.gov/33643651/)).

**Tissue/cell level.** Respiratory mucosa (epithelium) and lamina propria (connective tissue). Targeted/involved cells: **macrophages** (Mikulicz cells, CL:0000235), **inflammatory monocytes** (bone-marrow-derived), and **plasma cells** (CL:0000786, with Russell bodies).

**Subcellular level.** Bacilli reside in macrophage **cytoplasmic vacuoles/phagolysosomes** (GO:0005764 lysosome; GO:0045335 phagocytic vesicle). Russell bodies form in the plasma-cell **rough endoplasmic reticulum** (GO:0005791) — [PMID: 333340](https://pubmed.ncbi.nlm.nih.gov/333340/): *"The rough endoplasmic reticulum of plasma cells in scleroma displayed cisternal dilatations forming Russell bodies and cytoplasmic vacuolations containing viable and degenerated bacilli forming Mikulicz cells."*

**Localization/lateralization:** Midline nasal/upper-airway; typically bilateral with midline mass effect; can be asymmetric.

---

## 8. Temporal Development

**Onset.** Chronic and insidious. Typically young-to-middle adulthood; earlier onset in familial cases ([PMID: 18947330](https://pubmed.ncbi.nlm.nih.gov/18947330/)). Pediatric cases occur ([PMID: 40158349](https://pubmed.ncbi.nlm.nih.gov/40158349/)).

**Staging.** The classical three-stage model ([PMID: 17359555](https://pubmed.ncbi.nlm.nih.gov/17359555/)): *"There are three stages of the disease: catarrhal-atrophic, granulomatous (also known as hypertrophic) and sclerotic."* An expanded four-stage description ([PMID: 40158349](https://pubmed.ncbi.nlm.nih.gov/40158349/)): *"The disease progresses through four stages: catarrhal, crusty atrophic, proliferative, and sclerotic."*

| Stage | Hallmarks |
|-------|-----------|
| Catarrhal / atrophic | Nonspecific chronic rhinitis, purulent rhinorrhea, crusting, foul odor |
| Granulomatous / hypertrophic (proliferative) | Rubbery nodular masses; Mikulicz cells + Russell-body plasma cells; nasal enlargement/deformity |
| Sclerotic | Fibrosis, scarring, cicatricial stenosis, disfigurement |

**Progression.** Slow, progressive over months to years if untreated; chronic and lifelong without therapy. Disease course is progressive rather than relapsing-remitting, but **recurrence after treatment is common** due to intracellular persistence ([PMID: 40158349](https://pubmed.ncbi.nlm.nih.gov/40158349/), [PMID: 30168726](https://pubmed.ncbi.nlm.nih.gov/30168726/)).

**Patterns / critical periods.** Treatment-induced regression can be dramatic — an extensive lesion regressed within the first month of ciprofloxacin ([PMID: 33643651](https://pubmed.ncbi.nlm.nih.gov/33643651/)) and a granulomatous mass reached the cicatricial stage after six weeks of therapy ([PMID: 35183701](https://pubmed.ncbi.nlm.nih.gov/35183701/)). The therapeutic window is best **before** the sclerotic stage, since fibrotic stenosis is irreversible.

---

## 9. Inheritance and Population

**Epidemiology.** RS is rare overall and endemic in specific low-income regions. No precise global prevalence/incidence figures are established. Endemic areas: Central/North Africa (esp. Egypt), Central and South America, the Middle East, India, Indonesia/Southeast Asia, and Central/Eastern Europe ([PMID: 25933455](https://pubmed.ncbi.nlm.nih.gov/25933455/); [PMID: 29578083](https://pubmed.ncbi.nlm.nih.gov/29578083/)). In non-endemic (high-income) regions it is *"extremely rare"* and rising with travel/immigration ([PMID: 30168726](https://pubmed.ncbi.nlm.nih.gov/30168726/)).

**Inheritance (of susceptibility).** Not a Mendelian disease, but familial/consanguineous clustering with early onset suggests recessive host susceptibility ([PMID: 18947330](https://pubmed.ncbi.nlm.nih.gov/18947330/): *"Two unrelated consanguineous families were identified, 1 of which included 2 affected siblings."*). Penetrance, expressivity, anticipation, mosaicism, founder effects, and carrier frequency are **not defined** — no gene identified.

**Demographics.** Associated with poor, rural populations. Age: predominantly young adults (French series median 35.7 y, range 5–72; [PMID: 18947330](https://pubmed.ncbi.nlm.nih.gov/18947330/)). Sex ratio is variably reported with a modest female predominance in several series, but not firmly established. No specific ethnic predisposition beyond geographic/socioeconomic distribution.

---

## 10. Diagnostics

**Mainstay — histopathology of deep biopsy.** Because culture sensitivity is limited, diagnosis relies primarily on histology. [PMID: 17359555](https://pubmed.ncbi.nlm.nih.gov/17359555/): *"The diagnosis is made either by positive Klebsiella rhinoscleromatis culture or from the classic histological findings of Mikulicz cells and transformed plasma cells with Russell bodies."* Histology shows *"a dense plasmacytic infiltrate, Mikulicz histiocytes, and Russell bodies within the plasma cells"* ([PMID: 8784898](https://pubmed.ncbi.nlm.nih.gov/8784898/)). Special stains (Warthin-Starry, Giemsa, PAS, Grocott methenamine silver, Steiner) highlight intracellular bacilli within macrophages ([PMID: 38974602](https://pubmed.ncbi.nlm.nih.gov/38974602/)).

**Culture (supportive, insensitive).** [PMID: 17359555](https://pubmed.ncbi.nlm.nih.gov/17359555/): *"only 50-60 per cent of cultures are positive for K rhinoscleromatis."* Modern identification uses VITEK 2 and MALDI-TOF MS with EUCAST susceptibility interpretation ([PMID: 42698439](https://pubmed.ncbi.nlm.nih.gov/42698439/)).

**Imaging.** CT and MRI define disease extent, stenosis, bone involvement, and guide biopsy/surgery. [PMID: 19146007](https://pubmed.ncbi.nlm.nih.gov/19146007/): *"CT scan and MRI are useful for diagnosis."*

**Differential diagnosis (biopsy essential to avoid misdiagnosis).** [PMID: 17086321](https://pubmed.ncbi.nlm.nih.gov/17086321/): *"rhinoscleroma may be erroneously diagnosed as mucocutaneos leishmaniasis, leprosy, paracoccidioidomycosis, rhinosporidiasis, late syphilis, neoplasic diseases or other upper airway diseases."* Also consider granulomatosis with polyangiitis, relapsing polychondritis, amyloidosis, sarcoidosis, and Rosai-Dorfman disease (which can coexist; [PMID: 22643208](https://pubmed.ncbi.nlm.nih.gov/22643208/)). Malignancy is a key mimic — lesions can appear carcinoma-like ([PMID: 35183701](https://pubmed.ncbi.nlm.nih.gov/35183701/), [PMID: 33643651](https://pubmed.ncbi.nlm.nih.gov/33643651/)).

**Genetic/omics testing:** No role (not a genetic disease; no validated omics diagnostics). **Screening:** No population screening exists; prevention is via public-health/hygiene measures.

---

## 11. Outcome / Prognosis

**Survival/mortality.** RS is rarely directly fatal but can be lethal when airway obstruction is severe or disease is extensive ([PMID: 30168726](https://pubmed.ncbi.nlm.nih.gov/30168726/): symptoms "in some cases fatal"). No formal survival statistics are published.

**Morbidity/function.** The principal burden is chronic morbidity: nasal obstruction, disfigurement, voice change, and airway stenosis. Residual structural sequelae are near-universal even after cure — [PMID: 17086321](https://pubmed.ncbi.nlm.nih.gov/17086321/): *"all of them presented some degree of upper airway stenosis."*

**Disease course/recovery.** With prolonged antibiotics, active infection can resolve (a Peruvian series achieved no relapse over 6–12 months in treated patients; [PMID: 17086321](https://pubmed.ncbi.nlm.nih.gov/17086321/)), but recurrence is common — [PMID: 40158349](https://pubmed.ncbi.nlm.nih.gov/40158349/): *"Due to the intracellular nature of the bacteria, recurrence is common."* Fibrotic/sclerotic sequelae do not reverse.

**Prognostic factors.** Earlier stage at treatment (pre-sclerotic), adequate treatment duration, and immune competence favor better outcomes. Immunodeficiency (HIV, diabetes) and advanced fibrosis worsen prognosis. No molecular prognostic biomarkers exist.

---

## 12. Treatment

**Pharmacotherapy (first-line).** Prolonged courses of antibiotics that penetrate and concentrate in macrophages — the intracellular niche. **Fluoroquinolones (ciprofloxacin)** are the mainstay:
- Rationale ([PMID: 11244532](https://pubmed.ncbi.nlm.nih.gov/11244532/)): *"It achieves good tissue penetration, is concentrated in macrophages and may prove to be useful in the therapy of rhinoscleroma."*
- Dosing/duration ([PMID: 17086321](https://pubmed.ncbi.nlm.nih.gov/17086321/)): *"Ciprofloxacin 500 mg bid for four to 12 weeks was used in seven patients,"* with no relapse over 6–12 months' follow-up. Other reports used 3–4 months ([PMID: 33643651](https://pubmed.ncbi.nlm.nih.gov/33643651/), [PMID: 30364372](https://pubmed.ncbi.nlm.nih.gov/30364372/)).
- **Rifampicin** and other macrophage-penetrating agents are alternatives/adjuncts ([PMID: 33643651](https://pubmed.ncbi.nlm.nih.gov/33643651/): *"high concentration in macrophages such as rifampicin and fluoroquinolone"*). Historically tetracyclines, streptomycin, and trimethoprim-sulfamethoxazole were used.
- **Prolonged therapy is required** because the organism is intracellular ([PMID: 40158349](https://pubmed.ncbi.nlm.nih.gov/40158349/)). Suggested NCIT: Ciprofloxacin (NCIT:C376), Rifampin (NCIT:C608), Antibiotic Therapy (NCIT:C15844).

**Surgical/interventional.** Reserved for advanced disease: debridement of granulomatous masses, and relief of cicatricial airway stenosis/deformity (dilation, laser, tracheostomy, reconstructive repair). [PMID: 30168726](https://pubmed.ncbi.nlm.nih.gov/30168726/): *"managed effectively with a combination of antibiotics and surgical debridement and repair; however, recurrence rates do remain high."* NCIT: Surgical Procedure (NCIT:C15329), Debridement (NCIT:C15788).

**Supportive care.** Saline nasal irrigation and crust removal are useful adjuncts ([PMID: 30364372](https://pubmed.ncbi.nlm.nih.gov/30364372/)).

**Advanced/experimental therapeutics.** No gene, cell, RNA, targeted, or immunotherapy approaches are established. Given the IL-10-driven mechanism, **host-directed immunomodulation (e.g., IL-10 blockade)** is a plausible but entirely investigational avenue. Bacteriophage/CPS-depolymerase strategies against *Klebsiella* capsule are being explored for *K. pneumoniae* broadly ([PMID: 35130876](https://pubmed.ncbi.nlm.nih.gov/35130876/)) but not yet for RS. No RS-specific NCT trials were identified.

**Pharmacogenomics / personalized medicine:** Not applicable.

---

## 13. Prevention

- **Primary prevention:** Improvement of socioeconomic conditions — sanitation, hygiene, nutrition, reduced crowding — is the principal preventive strategy, inferred from the disease's disappearance from high-income regions ([PMID: 29578083](https://pubmed.ncbi.nlm.nih.gov/29578083/); [PMID: 25933455](https://pubmed.ncbi.nlm.nih.gov/25933455/)). No vaccine exists.
- **Secondary prevention:** Early recognition and biopsy of chronic nasal lesions in endemic areas to enable treatment before the irreversible sclerotic stage.
- **Tertiary prevention:** Adequate-duration antibiotic therapy and follow-up to prevent recurrence and manage airway complications; surgical relief of stenosis.
- **Public health:** Health education, improved housing/sanitation, and case detection in endemic communities.
- **Immunization / genetic counseling / prophylaxis:** No vaccine, no established chemoprophylaxis. Genetic counseling is not standard, though familial clustering may warrant heightened clinical vigilance in affected families.

---

## 14. Other Species / Natural Disease

RS is **human-specific** — [PMID: 29381692](https://pubmed.ncbi.nlm.nih.gov/29381692/): *"Rhinoscleroma is a human specific chronic granulomatous infection."* Species affected: *Homo sapiens* (NCBI:txid9606). No natural animal reservoir, no naturally occurring veterinary equivalent, no breed predisposition, and no documented zoonotic transmission. The causative organism belongs to the *Klebsiella pneumoniae* species complex (NCBI:txid573), within which the subspecies *rhinoscleromatis* is human-restricted. No orthologous "disease gene" applies, as this is an infectious rather than genetic disease.

---

## 15. Model Organisms

**Murine model (the key experimental system).** A novel mouse model established RS pathogenesis mechanistically:
- [PMID: 23554169](https://pubmed.ncbi.nlm.nih.gov/23554169/) (*A novel murine model of rhinoscleroma identifies Mikulicz cells, the disease signature, as IL-10 dependent derivatives of inflammatory monocytes*) — identified Mikulicz cells *"as atypical inflammatory monocytes specifically recruited from the bone marrow upon K. rhinoscleromatis infection in a CCR2-independent manner"* and showed *"in the absence of IL-10, very few Mikulicz cells were observed, confirming a crucial role of IL-10 in the establishment of a proper environment leading to the maturation of these atypical monocytes."*
- [PMID: 29381692](https://pubmed.ncbi.nlm.nih.gov/29381692/) — a lung-infection murine model *"recapitulating the formation of Mikulicz cells in lungs"* and *"partially recapitulate[s] the characteristic strong production of IL-10,"* used to dissect the role of the K3 capsule via the KR *cps-* mutant.

**Model type:** Mammalian (mouse), induced via bacterial lung/airway inoculation, including genetic variants (IL-10-deficient mice, CCR2-deficient mice) and bacterial mutants (KR *cps-*).

**Phenotype recapitulation:** Strong — the model reproduces the disease-signature Mikulicz cells and the characteristic IL-10-dominated response, enabling causal dissection of monocyte recruitment, IL-10 dependence, and capsule virulence.

**Limitations:** The model uses lung rather than nasal inoculation; it does not fully reproduce the chronic multi-stage progression to human nasal sclerotic deformity, and human-specific host-susceptibility factors are not captured.

---

## Mechanistic Model / Interpretation

Rhinoscleroma is best understood not as a simple pyogenic infection but as a **maladaptive, immunosuppressive host–pathogen equilibrium**. Three interlocking facts define it:

1. **Intracellular persistence** — the bacterium survives inside macrophage vacuoles (ultrastructurally proven, [PMID: 333340](https://pubmed.ncbi.nlm.nih.gov/333340/)), which both explains chronicity/recurrence and dictates therapy (macrophage-penetrating antibiotics for prolonged periods).
2. **IL-10-driven Mikulicz-cell genesis** — the pathogen specifically induces IL-10, which is *causally required* for bone-marrow inflammatory monocytes to mature into the foamy Mikulicz cell (KO-mouse proof, [PMID: 23554169](https://pubmed.ncbi.nlm.nih.gov/23554169/)). This is the mechanistic heart of the disease and the most promising host-directed drug target.
3. **Capsule-dependent virulence, capsule-independent Mikulicz formation** — the uniform K3 capsule drives bacterial fitness/immune evasion but is dispensable for the signature cell ([PMID: 29381692](https://pubmed.ncbi.nlm.nih.gov/29381692/)), cleanly separating the "virulence" and "immunopathology" arms.

The clinical staging (catarrhal → granulomatous → sclerotic) maps directly onto this chain: early colonization, then IL-10/monocyte-driven granuloma, then fibrotic burnout. The therapeutic corollary is that intervention before fibrosis is critical, since sclerotic stenosis is irreversible.

| Axis | Upstream driver | Downstream consequence | Reversible? |
|------|-----------------|------------------------|-------------|
| Bacterial | K3 capsule, intracellular survival | Persistence, recurrence | Yes (with prolonged Abx) |
| Immune | IL-10 induction, monocyte recruitment | Mikulicz cells, plasmacytosis | Partially |
| Structural | Chronic granuloma | Fibrosis, airway stenosis | No |

---

## Evidence Base

| PMID | Contribution | Supports finding |
|------|-------------|------------------|
| [29381692](https://pubmed.ncbi.nlm.nih.gov/29381692/) | Disease definition; K3 uniform serotype; capsule = virulence factor not needed for Mikulicz cells; IL-10 | F001, F007, F008 |
| [23554169](https://pubmed.ncbi.nlm.nih.gov/23554169/) | Mikulicz cells = IL-10-dependent, CCR2-independent bone-marrow inflammatory monocytes | F010 |
| [333340](https://pubmed.ncbi.nlm.nih.gov/333340/) | Ultrastructure: Russell bodies (rough ER), viable intracellular bacilli in Mikulicz cells | F002, F008 |
| [8784898](https://pubmed.ncbi.nlm.nih.gov/8784898/) | Pathognomonic histology: plasmacytic infiltrate, Mikulicz histiocytes, Russell bodies | F002 |
| [17359555](https://pubmed.ncbi.nlm.nih.gov/17359555/) | Three-stage model; nose 95–100%; culture 50–60%; dual diagnostic route | F003, F009 |
| [40158349](https://pubmed.ncbi.nlm.nih.gov/40158349/) | Four-stage model; recurrence from intracellular nature | F003, F005 |
| [18947330](https://pubmed.ncbi.nlm.nih.gov/18947330/) | French series: familial early onset, consanguinity, HIV cases | F004 |
| [29578083](https://pubmed.ncbi.nlm.nih.gov/29578083/) | Rural/poor socioeconomic distribution; abnormal cell-mediated immunity | F004 |
| [11244532](https://pubmed.ncbi.nlm.nih.gov/11244532/) | Ciprofloxacin concentrates in macrophages | F005 |
| [17086321](https://pubmed.ncbi.nlm.nih.gov/17086321/) | Cipro dosing 500 mg bid ×4–12 wk; residual stenosis; differential diagnosis | F005, F009 |
| [19146007](https://pubmed.ncbi.nlm.nih.gov/19146007/) | Anatomical distribution percentages; imaging utility | F006, F009 |
| [21410904](https://pubmed.ncbi.nlm.nih.gov/21410904/) | 88-case series: symptom spectrum and frequency | F006 |
| [39980691](https://pubmed.ncbi.nlm.nih.gov/39980691/) | *Klebsiella* CPS as anti-phagocytic virulence factor (supporting) | F001 |
| [30168726](https://pubmed.ncbi.nlm.nih.gov/30168726/) | Nonendemic rarity; antibiotic+surgery; high recurrence | §11, §12 |

**Coherence:** The evidence is internally consistent across ultrastructural pathology, clinical series, and a mechanistic mouse model. The strongest, most modern mechanistic claims (IL-10 dependence, monocyte origin, CCR2-independence, capsule role) rest on rigorous murine genetics ([PMID: 23554169](https://pubmed.ncbi.nlm.nih.gov/23554169/), [PMID: 29381692](https://pubmed.ncbi.nlm.nih.gov/29381692/)).

---

## Limitations and Knowledge Gaps

1. **No human genetic locus identified.** Familial/consanguineous clustering strongly implies a recessive host-susceptibility gene affecting cell-mediated immunity, but no gene has been mapped — the largest gap.
2. **Mechanistic data are largely murine.** IL-10 dependence and monocyte origin are proven in mice; direct human tissue transcriptomics/proteomics/single-cell data are absent.
3. **No formal epidemiology.** Prevalence/incidence, sex ratio, and mortality are not rigorously quantified; evidence is case-series-based.
4. **No controlled treatment trials.** Antibiotic regimens/durations derive from small uncontrolled series; optimal regimen and duration are undefined, and recurrence rates are imprecisely quantified.
5. **Model gaps.** The mouse model uses lung inoculation and does not fully reproduce chronic nasal sclerotic progression or human-specific susceptibility.
6. **Emerging microbiological complexity.** A recent case suggests possible polymicrobial involvement ([PMID: 42698439](https://pubmed.ncbi.nlm.nih.gov/42698439/)); significance unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Human genetic study:** Whole-exome/genome sequencing of consanguineous multiplex families and early-onset sporadic cases to identify recessive susceptibility genes (candidates in the IL-10/STAT3 or myeloid/cell-mediated-immunity axes).
2. **Human single-cell/spatial transcriptomics** of biopsy tissue across stages to confirm the murine IL-10/inflammatory-monocyte program in humans and map the catarrhal→sclerotic transition.
3. **Host-directed therapy proof-of-concept:** Test IL-10 pathway blockade (anti-IL-10/anti-IL-10R or STAT3 inhibition) as adjunct to antibiotics in the murine model to accelerate clearance and prevent Mikulicz-cell formation.
4. **Prospective treatment registry/trial:** Standardize and compare fluoroquinolone regimens (± rifampicin), define optimal duration, and quantify recurrence and stenosis outcomes.
5. **Capsule-targeted antibacterials:** Evaluate K3-specific bacteriophage depolymerases (cf. [PMID: 35130876](https://pubmed.ncbi.nlm.nih.gov/35130876/)) against *K. rhinoscleromatis* to disarm the K3 virulence factor.
6. **Molecular diagnostics:** Develop and validate PCR/MALDI-TOF-based assays on biopsy tissue to overcome the 50–60% culture sensitivity ceiling.

---

*Report compiled from 10 confirmed findings across 28 reviewed papers over 5 investigation iterations. Evidence sources: human clinical case series, ultrastructural pathology, and a murine model. This is an infectious, non-Mendelian disease; sections keyed to genetic-variant/Mendelian-inheritance content are marked "not applicable" with rationale.*


## Artifacts

- [OpenScientist final report](Rhinoscleroma-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rhinoscleroma-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 23 |
| On topic | 17 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:35130876` (5 mentions) - Structural and biological insights into Klebsiella pneumoniae surface polysaccharide degradation by a bacteriophage K1 lyase: implications for clinical use.
  - shared terms: genetic, human

Weighed against this report's own most characteristic terms: `disease`, `cell`, `stenosis`, `chronic`, `mikulicz`, `nasal`, `il-10`, `airway`, `rhinoscleromatis`, `rhinoscleroma`, `model`, `genetic`, `granulomatous`, `intracellular`, `sclerotic`, `recurrence`, `macrophage`, `monocyte`, `serie`, `human`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 27 |
| Terms named correctly | 21 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005945` (2 mentions) - the report calls it "MONDO"; MONDO calls it **rhinoscleroma**
- `HP:0025095` (1 mention) - the report calls it "Nasal crusting"; HP calls it **Sneeze**
- `HP:0009928` (1 mention) - the report calls it "Nasal septal perforation"; HP calls it **Thick nasal alae**
- `HP:0012781` (1 mention) - the report calls it "Upper airway obstruction"; HP calls it **Mid-frequency hearing loss**
- `UBERON:0002110` (1 mention) - the report calls it "Paranasal sinuses"; UBERON calls it **gallbladder**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C15788` (Clinical Trials, Diagnosis) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000860` (1 mention) - the report calls it "classical/inflammatory monocyte"; CL calls it **classical monocyte**, and lists "inflammatory monocyte" among its other names