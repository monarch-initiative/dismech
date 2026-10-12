---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-08T13:33:01.104330'
end_time: '2026-10-08T14:15:59.613545'
duration_seconds: 2578.51
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dystonia 24
  mondo_id: MONDO:0014019
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
citation_count: 32
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 32
  on_topic: 21
  validator_version: 0.3.0
term_validation:
  total_terms: 30
  verified: 29
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 5
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0014019
    reported_labels:
    - MONDO
    ontology_label: dystonia 24
  - term_id: HP:0032122
    reported_labels:
    - Paroxysmal dystonia
    ontology_label: Very low visual acuity
  - term_id: NCIT:C66099
    reported_labels:
    - Trihexyphenidyl
    ontology_label: Mertiatide
  - term_id: NCIT:C1005
    reported_labels:
    - Botulinum Toxin
    ontology_label: Arsenic Trioxide
  - term_id: NCIT:C38013
    reported_labels:
    - Deep Brain Stimulation
    ontology_label: Range
  - term_id: NCIT:C15682
    reported_labels:
    - Physical Therapy
    ontology_label: Dose-Rate
  obsolete_terms:
  - term_id: GO:0016021
    ontology_label: GO_0016021
    replaced_by: GO:0016020
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Dystonia_24-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Dystonia_24-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dystonia 24
- **MONDO ID:** MONDO:0014019 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dystonia 24** covering all of the
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

# Dystonia 24 (DYT24 / DYT-ANO3): A Comprehensive Disease Characteristics Report

**Disease:** Dystonia 24 (DYT24, DYT-ANO3)
**MONDO ID:** MONDO:0014019 · **OMIM:** #615034 · **Gene:** *ANO3* (anoctamin 3 / TMEM16C), 11p14.3
**Category:** Mendelian, autosomal dominant · **Report date:** 2026-10-08

---

## Summary

Dystonia 24 (DYT24, now preferentially designated **DYT-ANO3**) is a rare, autosomal dominant form of isolated—or occasionally combined—dystonia caused by heterozygous pathogenic variants in *ANO3*, the gene encoding **anoctamin 3 (TMEM16C)**, an endoplasmic-reticulum–associated, Ca²⁺-dependent **phospholipid scramblase/ion channel** that is most highly expressed in the **striatum**. The disorder was defined in 2012 when Charlesworth and colleagues combined linkage analysis with whole-exome sequencing in a UK kindred and identified six putatively pathogenic *ANO3* mutations ([PMID: 23200863](https://pubmed.ncbi.nlm.nih.gov/23200863/)). Its clinical hallmark is **tremulous craniocervical dystonia**—cervical and laryngeal onset are most typical—with a characteristic **dystonic/postural tremor** that distinguishes DYT24 from the related DYT6 (*THAP1*) phenotype and frequently causes misdiagnosis as essential tremor.

Over the subsequent decade the phenotypic spectrum has broadened considerably: from classic adult-onset tremulous craniocervical dystonia to **infantile generalized or paroxysmal dystonia, dystonia-ataxia, truncal dystonia, and even early dyskinetic encephalopathy**, with onset ranging from the first months of life to the fifth decade. Inheritance is autosomal dominant with **reduced, age-dependent penetrance** and **marked intrafamilial variability**. The variant spectrum is overwhelmingly **missense**, clustering near the transmembrane/scrambling region; genetic constraint data (gnomAD missense Z = 3.66, pLI ≈ 0, LoF tolerated) indicate the mechanism is **dominant-negative / gain-of-function**, not haploinsufficiency. Functional studies converge on **dysregulated intracellular (ER) Ca²⁺ signaling and attenuated Ca²⁺-dependent scramblase activation** altering striatal neuronal excitability as the core pathophysiology.

DYT24 is **chronic, non-degenerative, and non-fatal** (brain MRI is typically normal), but it carries substantial motor and non-motor (pain, depression, anxiety) morbidity. There is no cure or disease-modifying therapy; management is **symptomatic**—botulinum toxin for focal forms, anticholinergics (trihexyphenidyl), physiotherapy, and **globus pallidus internus (GPi) deep brain stimulation**, with several reports of marked benefit. Because the disorder is monogenic with no modifiable environmental cause, **prevention is limited to genetic counseling, cascade/predictive testing, and reproductive options**. The sections below detail each disease-characteristic domain with primary-literature citations.

---

## Key Findings

### 1. Disease Information

Dystonia 24 is an **autosomal dominant, isolated (or combined) craniocervical dystonia** caused by heterozygous variants in *ANO3*. It was established as a distinct entity by Charlesworth et al. (2012), who wrote: *"we combined linkage analysis with whole-exome sequencing of two individuals to identify candidate causal variants in a moderately-sized UK kindred exhibiting autosomal-dominant inheritance of craniocervical dystonia"* and reported *"a total of six putatively pathogenic mutations in ANO3, a gene encoding a predicted Ca(2+)-gated chloride channel that we show to be highly expressed in the striatum"* ([PMID: 23200863](https://pubmed.ncbi.nlm.nih.gov/23200863/)).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #615034 (DYT24) |
| MONDO | MONDO:0014019 |
| Gene | *ANO3* (HGNC; anoctamin 3 / TMEM16C), chromosome 11p14.3 |
| Ensembl gene | ENSG00000134343 |
| Reference transcript | NM_031418.4 |

**Synonyms / alternative names:** DYT24; DYT-ANO3; ANO3-related dystonia; anoctamin-3 dystonia; craniocervical dystonia (ANO3 type). The information is derived from **aggregated disease-level resources** (OMIM, ClinVar, gnomAD) and from published **case series and functional studies** rather than from individual EHR records.

### 2. Etiology

**Primary cause — genetic.** DYT24 is a **monogenic disorder** caused by heterozygous pathogenic variants in *ANO3*. There is **no established environmental, infectious, or toxic cause**, and no gene–environment interaction has been demonstrated for this specific entity. The causal variants are overwhelmingly **missense** (see Finding 5 / Section 4).

**Genetic risk factors.** The causative variants are themselves the risk determinants; no additional susceptibility loci or validated modifier genes exist for DYT24. In broader (non-monogenic) cervical dystonia, a GWAS identified a genome-wide significant signal near *COL8A1* ([PMID: 34320236](https://pubmed.ncbi.nlm.nih.gov/34320236/)), but this concerns idiopathic cervical dystonia rather than the monogenic ANO3 form.

**Environmental / protective factors.** None established specifically for DYT24. General observations in idiopathic adult-onset dystonia (e.g., associations of cerebrovascular risk factors with blepharospasm, [PMID: 37717501](https://pubmed.ncbi.nlm.nih.gov/37717501/)) do not apply to the monogenic ANO3 mechanism. No protective variants or dietary/lifestyle protective exposures are known. **Not available / not applicable** for the Mendelian DYT24 entity.

### 3. Phenotypes

The **hallmark is tremor**. Stamelou et al. (2014) characterized 10 patients from 3 families and reported: *"The characteristic feature in all affected individuals was the presence of tremor, which contrasts DYT24 from the typical DYT6 phenotype"* ([PMID: 24442708](https://pubmed.ncbi.nlm.nih.gov/24442708/)). Tremor can be the **sole initial manifestation**, causing misdiagnosis as essential tremor: *"Tremor was the sole initial manifestation in some individuals with ANO3 mutations, leading to misdiagnosis as essential tremor."*

**Anatomical distribution and onset:** *"The age at onset ranged from early childhood to the forties. Cervical dystonia was the most common site of onset followed by laryngeal dystonia"* ([PMID: 24442708](https://pubmed.ncbi.nlm.nih.gov/24442708/)). Electrophysiology showed co-contraction of antagonist muscles and a ~6-Hz arm tremor; one patient had subcortical myoclonus (~3 Hz, ~250 ms).

**Broadened spectrum (Finding 6):** Ousingsawat et al. (2024) described severe pediatric phenotypes: *"Two patients exhibited generalized progressive dystonia, while one patient presented with paroxysmal dystonia. Additionally, another patient exhibited early dyskinetic encephalopathy"* ([PMID: 38079528](https://pubmed.ncbi.nlm.nih.gov/38079528/)). Altıntaş (2025) summarized: *"The onset of clinical features may vary from the first months of life to adulthood, and cases may present with a wide range of clinical spectrum, from focal/segmental to generalized dystonia, and from isolated to tremulous or jerky dystonia"* ([PMID: 41441972](https://pubmed.ncbi.nlm.nih.gov/41441972/)). Additional reported phenotypes include dystonia-ataxia syndrome ([PMID: 39351635](https://pubmed.ncbi.nlm.nih.gov/39351635/)), hereditary truncal dystonia ([PMID: 39692086](https://pubmed.ncbi.nlm.nih.gov/39692086/)), and learning difficulties / mild intellectual disability in several families ([PMID: 38284143](https://pubmed.ncbi.nlm.nih.gov/38284143/), [PMID: 41441972](https://pubmed.ncbi.nlm.nih.gov/41441972/)).

**Suggested phenotype table with HPO terms:**

| Phenotype | HPO term | Type | Onset | Frequency | Progression |
|---|---|---|---|---|---|
| Dystonic/postural tremor | HP:0001337 (Tremor) | Clinical sign | Childhood–adult | Characteristic in all affected | Variable, often stable |
| Cervical dystonia / torticollis | HP:0002019 / HP:0030243 | Clinical sign | Most common onset site | Common | Can spread |
| Laryngeal (spasmodic) dysphonia | HP:0001618 (Dysphonia) | Clinical sign | 2nd most common | Subset | Stable |
| Generalized dystonia | HP:0007325 | Clinical sign | Infantile/childhood | Subset (severe) | Progressive in some |
| Paroxysmal dystonia | HP:0032122 | Clinical sign | Infantile | Rare | Episodic |
| Myoclonus | HP:0001336 | Clinical sign | Variable | Minority | Stable |
| Intellectual disability / learning difficulty | HP:0001249 / HP:0001328 | Behavioral/cognitive | Childhood | Minority of families | Stable |
| Dyskinetic encephalopathy | HP:0001263 + dyskinesia | Severe pediatric | Infancy | Rare | Severe |

**Quality of life impact:** Craniocervical/cervical dystonia produces pain, disability, and poor quality of life with substantial non-motor burden—depression, anxiety, fatigue, and sleep disturbance ([PMID: 33099684](https://pubmed.ncbi.nlm.nih.gov/33099684/); [PMID: 41483253](https://pubmed.ncbi.nlm.nih.gov/41483253/)).

### 4. Genetic / Molecular Information

**Causal gene:** *ANO3* (anoctamin 3 / TMEM16C), chromosome 11p14.3, reference transcript NM_031418.4, UniProt Q9BYT9.

**Mechanistic class of variants — missense, dominant-negative/GoF (Findings 5 & 10).** Genetic constraint from gnomAD v2 (ENSG00000134343, GRCh38) shows **pLI ≈ 0** (loss-of-function tolerated: observed/expected LoF = 0.68, LOEUF 0.58–0.81; 99 observed vs 145 expected LoF), but significant **missense constraint (Z = 3.66, oe_mis 0.75)**. This dissociation indicates that pathogenic dystonia alleles act not by haploinsufficiency but through a **dominant-negative or gain-of-function** mechanism on a missense-intolerant protein.

**ClinVar landscape (queried 2026-10-08):** 772 *ANO3* variant records — 95 Pathogenic, 10 Likely pathogenic, 590 VUS; 398 records annotated with dystonia. Reported pathogenic alleles are missense.

**Recurrent / representative pathogenic variants (NM_031418.4):**

| cDNA | Protein | Note |
|---|---|---|
| c.1528G>A | p.(Glu510Lys) | Recurrent across ancestries |
| c.1952G>A | p.(Ser651Asn) | Recurrent; functionally studied |
| c.1699G>C / c.1699G>A | p.(Gly567Arg) | — |
| c.1943A>G | p.(Asn648Ser) | Trihexyphenidyl-responsive case |
| c.1942A>G | p.(Asn648Asp) | — |
| c.1819A>T | p.(Ile607Phe) | — |
| c.1969G>A | p.(Ala657Thr) | — |
| c.1470G>T | p.(Trp490Cys) | — |
| c.1480A>T | p.(Arg494Trp) | — |
| c.2053A>G | p.(Ser685Gly) | — |
| c.2586G>T | p.(Lys862Asn) | — |
| (original kindred / functional cohorts) | p.Gly6Val, p.Ser116Leu, p.Val561Leu, p.Ala599Asp, p.Arg330His, p.Thr383Ile | [PMID: 23200863](https://pubmed.ncbi.nlm.nih.gov/23200863/), functional studies |

Notably, a nonsense allele **p.(Arg628Ter) is classified VUS**, consistent with LoF not being the primary disease mechanism. Variants near the scrambling domain are associated with a **more severe, earlier-onset phenotype** ([PMID: 38284143](https://pubmed.ncbi.nlm.nih.gov/38284143/)).

**Modifier genes / epigenetics / chromosomal abnormalities:** No validated modifier genes, epigenetic mechanisms, or large-scale chromosomal abnormalities are established for DYT24. **Not available / not applicable.**

**Suggested gene/protein annotations:** HGNC *ANO3*; UniProt Q9BYT9 (ANO3_HUMAN); phospholipid scramblase activity; see Section 6 for GO terms.

### 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors are established for DYT24. As a monogenic disorder, disease is determined by the germline *ANO3* variant. **Not applicable.** (Contextually, idiopathic adult-onset dystonia—a different etiologic category—shows modest associations with cerebrovascular risk factors for blepharospasm, [PMID: 37717501](https://pubmed.ncbi.nlm.nih.gov/37717501/), but this does not extend to monogenic ANO3 disease.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

```
1. Heterozygous missense variant in ANO3 (e.g., p.Glu510Lys, p.Ser651Asn, near the
   Ca2+-binding/scrambling transmembrane region)
        │ leads to
2. Altered ANO3/TMEM16C protein — an ER-associated, Ca2+-dependent phospholipid
   scramblase/ion channel — with attenuated Ca2+-dependent activation
   (dominant-negative/gain-of-function; LoF is tolerated)
        │ results in
3. Dysregulated intracellular (endoplasmic-reticulum) Ca2+ signaling and impaired
   Ca2+-dependent scramblase activity (shown in patient fibroblasts and
   heterologous expression)
        │ leads to  ──────────────┬──────────────────────────────────┐
4a. Altered neuronal excitability │ 4b. (inferred) Perturbed ER membrane lipid
    in striatal neurons, where    │     homeostasis / Ca2+ store regulation
    ANO3 is most highly expressed │
        │ contributes to          │
5. Dysfunction of basal-ganglia sensorimotor and cerebello-thalamo-cortical
   networks — loss of inhibition and maladaptive sensorimotor plasticity (inferred
   from general dystonia pathophysiology)
        │ results in
6. Tremulous craniocervical (or, in severe variants, generalized/paroxysmal)
   dystonia — the clinical manifestation
```

**Molecular detail.** ANO3 (TMEM16C) is an **"intracellular" anoctamin** localized to ER membranes that operates as a **Ca²⁺-dependent phospholipid scramblase** ([PMID: 38657371](https://pubmed.ncbi.nlm.nih.gov/38657371/): *"these so-called intracellular anoctamins are also found in the plasma membrane"*; [PMID: 23532839](https://pubmed.ncbi.nlm.nih.gov/23532839/) demonstrated TMEM16C scramblase activity). Charlesworth et al. (2012) showed patient fibroblasts have **abnormal ER-dependent Ca²⁺ signaling** ([PMID: 23200863](https://pubmed.ncbi.nlm.nih.gov/23200863/)).

Ousingsawat et al. (2024) linked the variants mechanistically: *"ANO3 variants may dysregulate intracellular Ca2+ signalling, as variants in other Ca2+ regulating proteins like hippocalcin were also identified as a cause of dystonia"* ([PMID: 38079528](https://pubmed.ncbi.nlm.nih.gov/38079528/)); their 2025 electrophysiology study found dystonia variants cause **attenuated Ca²⁺-dependent activation** ([PMID: 39773217](https://pubmed.ncbi.nlm.nih.gov/39773217/)). TMEM16C also **facilitates Na⁺-activated K⁺ (Slack/KCNT1) currents** in sensory neurons, modulating excitability: *"TMEM16C modulated the single-channel activity of Slack channels and increased its sodium sensitivity"* ([PMID: 23872594](https://pubmed.ncbi.nlm.nih.gov/23872594/)).

**Network-level pathophysiology.** Morgante & Klein (2013) note that dystonia *"is specifically characterized by maladaptive plasticity in the sensorimotor cortex and loss of cortical surround inhibition"* ([PMID: 24092288](https://pubmed.ncbi.nlm.nih.gov/24092288/)), implicating basal-ganglia and cerebello-thalamo-cortical circuits.

**Striatal expression.** Cameron et al. (2026) found that, across human brain RNA-seq datasets, dystonia genes are enriched in striatum, cortex, hippocampus, amygdala, and substantia nigra, predominantly in neurons; specifically *"ADCY5, GNAL, ANO3 (highest expression in striatum)"* ([PMID: 41400152](https://pubmed.ncbi.nlm.nih.gov/41400152/)).

**Suggested ontology terms:**
- **GO (biological process):** calcium ion transport (GO:0006816); phospholipid scrambling (GO:0017121); regulation of membrane potential (GO:0042391).
- **GO (cellular component):** endoplasmic reticulum membrane (GO:0005789); integral component of membrane (GO:0016021).
- **CL (cell types):** medium spiny neuron (CL:1001474); GABAergic neuron (CL:0000617); glutamatergic neuron (CL:0000679); dopaminergic neuron (CL:0000700).
- **CHEBI:** calcium(2+) (CHEBI:29108); phosphatidylserine (CHEBI:18303).

### 7. Anatomical Structures Affected

**Organ / system level.** DYT24 is a disorder of the **nervous system**, specifically **central motor-control circuitry**. There is **no primary organ damage**; brain MRI is typically **normal/unremarkable** ([PMID: 38079528](https://pubmed.ncbi.nlm.nih.gov/38079528/)). The functional lesion centers on the **striatum/basal ganglia** (UBERON:0002435 striatum; UBERON:0002420 basal ganglion) and associated cerebello-thalamo-cortical networks.

**Tissue / cell level.** The affected cells are **striatal neurons**, where *ANO3* is most highly expressed ([PMID: 41400152](https://pubmed.ncbi.nlm.nih.gov/41400152/)). Dystonia genes are predominantly expressed in **glutamatergic, GABAergic, and dopaminergic neurons**. Suggested CL terms: medium spiny neuron (CL:1001474), GABAergic neuron (CL:0000617).

**Subcellular level.** The key compartment is the **endoplasmic reticulum membrane** (GO:0005789), where ANO3 scramblase/Ca²⁺-regulatory activity operates, with downstream effects on **plasma-membrane ion channels** (Slack/KCNT1).

**Clinical localization / lateralization.** Dystonia typically affects **craniocervical** regions (neck, larynx) and may be **bilateral or asymmetric**; limb tremor can be asymmetric. UBERON: neck (UBERON:0000974), larynx (UBERON:0001737).

### 8. Temporal Development

**Onset.** Highly variable: *"The onset of clinical features may vary from the first months of life to adulthood"* ([PMID: 41441972](https://pubmed.ncbi.nlm.nih.gov/41441972/)); classic series report **early childhood to the forties** ([PMID: 24442708](https://pubmed.ncbi.nlm.nih.gov/24442708/)). Onset pattern is generally **insidious/chronic**; paroxysmal (episodic) onset is described in rare infantile cases.

**Progression.** Most cases are **stable or slowly progressive**; some pediatric generalized forms are **progressive** ([PMID: 38079528](https://pubmed.ncbi.nlm.nih.gov/38079528/)). Dystonia can **spread** from focal to segmental/generalized distribution in a minority. Disease is **chronic and lifelong**, **non-degenerative**.

**Patterns.** No spontaneous remission is characteristic; symptomatic treatment (BoNT, DBS) induces improvement but not cure. **Critical period:** early symptomatic treatment to limit disability; younger age at onset / variants near the scrambling domain predict more severe disease ([PMID: 38284143](https://pubmed.ncbi.nlm.nih.gov/38284143/)).

### 9. Inheritance and Population

**Inheritance.** **Autosomal dominant** with **reduced, age-dependent penetrance** and **highly variable expressivity**. Lohmann & Klein (2013): *"The genetic contribution to dystonia represents a continuum ranging from genetic susceptibility factors of small effect to causative genes with markedly reduced penetrance to those with full penetrance"* ([PMID: 23893446](https://pubmed.ncbi.nlm.nih.gov/23893446/)). Zorzi (2018) places *ANO3* among AD pediatric-onset isolated-dystonia genes with low penetrance: *"The recently discovered genes (GNAL, ANO-3, KTM2B)..."* ([PMID: 29396174](https://pubmed.ncbi.nlm.nih.gov/29396174/)). Intrafamilial variability is well documented—e.g., 16 affected members of an Indian family with a novel variant showing wide phenotypic heterogeneity ([PMID: 41996745](https://pubmed.ncbi.nlm.nih.gov/41996745/)). **No repeat expansion**, so **genetic anticipation does not apply**. No founder population is established, though recurrent variants (p.Glu510Lys, p.Ser651Asn) occur across European, Chinese, Indian, and Turkish cohorts.

**Epidemiology.** No validated ANO3-specific prevalence exists. DYT24 is a **rare single-gene cause** within isolated dystonia (US period prevalence of isolated dystonia 50.2/100,000, 2020–2023; annual incidence 31.8–41.5/100,000; 68.4% female; focal most common at 73%) ([PMID: 42845092](https://pubmed.ncbi.nlm.nih.gov/42845092/)). ANO3 is **uncommon even among adult-onset cervical dystonia**: *"The recently discovered genes ANO3, GNAL and CIZ1 appear not to be a common cause of adult-onset cervical dystonia"* ([PMID: 24978640](https://pubmed.ncbi.nlm.nih.gov/24978640/)). In gene-panel/exome cohorts ANO3 is a rare yield (e.g., THAP1 most common in an Asian Indian cohort; ANO3 among rarer, [PMID: 39749944](https://pubmed.ncbi.nlm.nih.gov/39749944/)).

**Sex ratio.** **Female predominance.** In the MDSGene database (n=1377), *"female participants outnumbered male participants for some genes (GNAL, GCH1, and ANO3) but not for other genes (THAP1, TH, and TOR1A)"* ([PMID: 38778444](https://pubmed.ncbi.nlm.nih.gov/38778444/)).

### 10. Diagnostics

**Diagnosis is clinical + molecular.** There is **no specific laboratory biomarker** and **brain MRI is typically normal** ([PMID: 38079528](https://pubmed.ncbi.nlm.nih.gov/38079528/)). Diagnosis rests on phenomenology (tremulous craniocervical dystonia) plus **molecular confirmation of an *ANO3* variant**.

**Genetic testing approach.** *ANO3* is a standard component of **dystonia/movement-disorder NGS gene panels**. Targeted 127-gene panels yield pathogenic variants in ~22% of selected inherited cases (*"probable pathogenic variants were identified in 83 cases (22.0%)"*, [PMID: 29913018](https://pubmed.ncbi.nlm.nih.gov/29913018/)). **Whole-exome sequencing** increases yield after negative panels, especially in complex/early-onset dystonia: *"Diagnostic yield was higher in complex dystonia compared to non-complex dystonia (66.7%–5.9%; p < 0.002), especially in patients showing intellectual disability"* ([PMID: 32334381](https://pubmed.ncbi.nlm.nih.gov/32334381/)); exome outperforms panels for complex phenotypes ([PMID: 40470849](https://pubmed.ncbi.nlm.nih.gov/40470849/)).

**Supportive electrophysiology (characterizing, not diagnostic).** Tremor recordings, EMG showing co-contraction of antagonist muscles, back-averaged EEG, and C-reflex testing can characterize tremor/myoclonus ([PMID: 24442708](https://pubmed.ncbi.nlm.nih.gov/24442708/)).

**Differential diagnosis.** Essential tremor (tremor-only presentations are frequently misdiagnosed as ET, [PMID: 24442708](https://pubmed.ncbi.nlm.nih.gov/24442708/)); other monogenic dystonias (DYT1/*TOR1A*, DYT6/*THAP1*, DYT25/*GNAL*, *KMT2B*, dopa-responsive dystonia/*GCH1*). Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are **not relevant** to ANO3 diagnosis (missense point variants).

### 11. Outcome / Prognosis

**Survival / mortality.** DYT24 is **non-degenerative and non-fatal**; no reduction in life expectancy is reported. Brain MRI is normal ([PMID: 38079528](https://pubmed.ncbi.nlm.nih.gov/38079528/)). Severe pediatric dyskinetic-encephalopathy cases carry higher morbidity.

**Morbidity / function / QoL.** Disability is driven by motor symptoms **plus pain and non-motor burden**. Cervical dystonia produces *"a myriad of non-motor symptoms including pain, fatigue, sleep disorders and anxiety and depression"* ([PMID: 33099684](https://pubmed.ncbi.nlm.nih.gov/33099684/)).

**Treatment-modified prognosis.** GPi-DBS improves outcomes long-term: *"GPI-DBS significantly improved overall TWSTRS scores by 57% from baseline to 5Y FU"*, with severity/disability/pain sub-scores improved 72%/59%/46% ([PMID: 37542824](https://pubmed.ncbi.nlm.nih.gov/37542824/)). Botulinum toxin combined with physiotherapy outperforms BoNT alone for disability, pain, depression, and QoL (CDIP-58) ([PMID: 41483253](https://pubmed.ncbi.nlm.nih.gov/41483253/)).

**Prognostic factors.** Younger age at onset and variants near the scrambling domain predict more severe disease ([PMID: 38284143](https://pubmed.ncbi.nlm.nih.gov/38284143/)). No molecular prognostic biomarkers are validated.

### 12. Treatment

Management is **symptomatic**; no disease-modifying or gene-directed therapy exists.

| Modality | Agent / intervention | Evidence | NCIT suggestion |
|---|---|---|---|
| Anticholinergic | Trihexyphenidyl | *"She was started on trihexyphenidyl, and at the follow-up, partial improvement in her involuntary movements was observed"* ([PMID: 41441972](https://pubmed.ncbi.nlm.nih.gov/41441972/)) | NCIT:C66099 (Trihexyphenidyl) |
| Chemodenervation | Botulinum toxin (type A) | First-line for focal forms ([PMID: 24092288](https://pubmed.ncbi.nlm.nih.gov/24092288/)); BoNT+PT superior to BoNT alone ([PMID: 41483253](https://pubmed.ncbi.nlm.nih.gov/41483253/)) | NCIT:C1005 (Botulinum Toxin) |
| Neuromodulation | GPi deep brain stimulation | Successful/marked improvement in ANO3 dystonia ([PMID: 38341631](https://pubmed.ncbi.nlm.nih.gov/38341631/); [PMID: 42493765](https://pubmed.ncbi.nlm.nih.gov/42493765/)); 57% TWSTRS improvement at 5y in cervical dystonia ([PMID: 37542824](https://pubmed.ncbi.nlm.nih.gov/37542824/)); mild response in an early ANO3 series ([PMID: 38079528](https://pubmed.ncbi.nlm.nih.gov/38079528/)) | NCIT:C38013 (Deep Brain Stimulation) |
| Rehabilitation | Physiotherapy / tailored PT | Adjunct to BoNT improves disability, pain, depression, QoL ([PMID: 41483253](https://pubmed.ncbi.nlm.nih.gov/41483253/)); holistic neurorehabilitation ([PMID: 33099684](https://pubmed.ncbi.nlm.nih.gov/33099684/)) | NCIT:C15682 (Physical Therapy) |

**Pharmacogenomics, gene therapy, cell therapy, RNA-based or immunotherapies:** none established for DYT24 — **not available / not applicable** at present. No approved targeted therapy. DBS response in ANO3 ranges from mild to marked across reports.

### 13. Prevention

**No primary prevention exists** — DYT24 is a dominantly inherited monogenic disorder with no modifiable environmental cause. Prevention is limited to:

- **Genetic counseling** conveying **autosomal dominant 50% transmission risk** with **reduced penetrance and highly variable expressivity** — an inherited variant does not guarantee disease nor predict severity.
- **Cascade / predictive testing** of at-risk relatives once a familial pathogenic *ANO3* variant is identified.
- **Reproductive options:** prenatal diagnosis and preimplantation genetic testing.
- NGS-based diagnosis is emphasized to *"offer precise genetic counseling to families, and prevent recurrence in the family"* ([PMID: 40302693](https://pubmed.ncbi.nlm.nih.gov/40302693/)).
- **Tertiary prevention** = early symptomatic treatment (BoNT, anticholinergics, physiotherapy, timely DBS) to limit disability ([PMID: 29396174](https://pubmed.ncbi.nlm.nih.gov/29396174/)).

Immunization, public-health/environmental interventions, and behavioral prevention are **not applicable**.

### 14. Other Species / Natural Disease

**Taxonomy / orthologs.** *ANO3*/*Ano3* orthologs exist in mouse (NCBI Taxon 10090) and rat (NCBI Taxon 10116) as *Tmem16c*. No naturally occurring DYT24-equivalent dominant dystonia is documented in companion animals or wildlife. **Veterinary relevance is not established.**

**Comparative biology.** The scramblase/ion-channel function of TMEM16C is **evolutionarily conserved**. Rodent knockouts model **loss-of-function** consequences (neuronal hyperexcitability, febrile-seizure susceptibility — see Section 15), which recapitulate TMEM16C's normal physiology but **not** the dominant human dystonia, consistent with the human disease being missense/dominant-negative rather than LoF.

**Transmission.** Not applicable (non-infectious, non-zoonotic).

### 15. Model Organisms

| Model | Type | Key phenotype | Relevance to DYT24 | Reference |
|---|---|---|---|---|
| *Tmem16c* knockout rat | Mammalian, KO | Diminished Slack (KCNT1) expression, broadened action potentials, increased DRG excitability, increased thermal/mechanical pain | Models **LoF** physiology (excitability), not dominant dystonia | [PMID: 23872594](https://pubmed.ncbi.nlm.nih.gov/23872594/) |
| *Tmem16c* knockout rodent (pups) | Mammalian, KO | Impaired thermoregulation; febrile-seizure susceptibility | GWAS-linked febrile seizure risk; LoF model | [PMID: 33972431](https://pubmed.ncbi.nlm.nih.gov/33972431/) |
| Heterologous expression (HEK/293T) + patient fibroblasts | In vitro / cellular | Dysregulated ER Ca²⁺ signaling; attenuated Ca²⁺-dependent scramblase activation by dystonia variants | Directly models **pathogenic variant** mechanism | [PMID: 23200863](https://pubmed.ncbi.nlm.nih.gov/23200863/); [PMID: 39773217](https://pubmed.ncbi.nlm.nih.gov/39773217/); [PMID: 38079528](https://pubmed.ncbi.nlm.nih.gov/38079528/) |

Knockout rat DRG findings: *"DRG from TMEM16C knockout rats had diminished Slack expression, broadened action potentials and increased excitability"* ([PMID: 23872594](https://pubmed.ncbi.nlm.nih.gov/23872594/)). **Model limitation:** existing rodent models are loss-of-function and do **not** reproduce the dominant, missense-driven dystonia; no knock-in model carrying a human pathogenic *ANO3* missense allele with a dystonia phenotype has been reported. **Model databases:** MGI, RGD.

---

## Mechanistic Model / Interpretation

The weight of evidence (16 confirmed findings; 55 papers reviewed) supports a coherent model of DYT24 as an **endoplasmic-reticulum Ca²⁺/phospholipid-scramblase channelopathy of the striatum**:

```
ANO3 missense variant (ER Ca2+-dependent scramblase/channel, missense-constrained)
        │ dominant-negative / gain-of-function (LoF is tolerated — gnomAD pLI≈0)
        ▼
Attenuated Ca2+-dependent activation + dysregulated intracellular (ER) Ca2+ signaling
        │
        ▼
Altered excitability of striatal neurons (ANO3 highest expression in striatum)
        │  (inferred) via disturbed Ca2+ stores and modulation of K(Na)/Slack channels
        ▼
Basal-ganglia & cerebello-thalamo-cortical network dysfunction
(loss of inhibition, maladaptive sensorimotor plasticity — inferred from general dystonia)
        ▼
Tremulous craniocervical dystonia  ──► (severe variants) generalized / paroxysmal /
                                          dyskinetic-encephalopathy phenotypes
```

**Upstream vs downstream:** The **upstream** lesion is the missense variant and its effect on ER Ca²⁺/scramblase function; the **downstream** manifestation is network-level motor dyscontrol. A crucial interpretive point is the **genetic-constraint/functional convergence**: gnomAD shows LoF is tolerated (pLI ≈ 0) while missense is constrained (Z = 3.66), and the only reported nonsense allele is a VUS—together strongly arguing that **haploinsufficiency is not the mechanism** and that pathogenic missense variants act via **dominant-negative or gain-of-function**. This also explains why rodent *Ano3* knockouts (LoF) model hyperexcitability/febrile seizures rather than dominant dystonia.

**Genotype–phenotype correlation:** Variants near the scrambling domain and younger onset predict more severe, often generalized disease, consistent with a graded effect on scramblase/Ca²⁺ function.

---

## Evidence Base

| PMID | Study (abbreviated) | Contribution |
|---|---|---|
| [23200863](https://pubmed.ncbi.nlm.nih.gov/23200863/) | ANO3 mutations cause dominant craniocervical dystonia | Gene discovery; AD inheritance; striatal expression; abnormal ER Ca²⁺ in fibroblasts |
| [24442708](https://pubmed.ncbi.nlm.nih.gov/24442708/) | Phenotypic spectrum of DYT24 | Tremor as hallmark; onset range; cervical→laryngeal; ET misdiagnosis |
| [38079528](https://pubmed.ncbi.nlm.nih.gov/38079528/) | Broadening clinical spectrum / mechanisms | Pediatric generalized/paroxysmal/encephalopathy; Ca²⁺ dysregulation; DBS; normal MRI |
| [39773217](https://pubmed.ncbi.nlm.nih.gov/39773217/) | ANO3 dystonia due to attenuated Ca²⁺ activation | Electrophysiology of variants; attenuated Ca²⁺-dependent activation |
| [38657371](https://pubmed.ncbi.nlm.nih.gov/38657371/) | Intracellular anoctamins (review) | ANO3 as intracellular anoctamin also at plasma membrane |
| [23532839](https://pubmed.ncbi.nlm.nih.gov/23532839/) | TMEM16 scramblase activity | TMEM16C is a Ca²⁺-dependent lipid scramblase |
| [23872594](https://pubmed.ncbi.nlm.nih.gov/23872594/) | TMEM16C facilitates K(Na) currents | Slack/KCNT1 modulation; KO rat hyperexcitability |
| [33972431](https://pubmed.ncbi.nlm.nih.gov/33972431/) | TMEM16C thermoregulation/febrile seizures | KO model; febrile-seizure link |
| [24092288](https://pubmed.ncbi.nlm.nih.gov/24092288/) | Dystonia (review) | DYT24 classification; network pathophysiology; BoNT/DBS |
| [41400152](https://pubmed.ncbi.nlm.nih.gov/41400152/) | Expression of dystonia genes | ANO3 highest in striatum; neuronal expression |
| [38778444](https://pubmed.ncbi.nlm.nih.gov/38778444/) | Sex differences in dystonia (MDSGene) | Female predominance in ANO3 |
| [41441972](https://pubmed.ncbi.nlm.nih.gov/41441972/) | ANO3 tremulous dystonia case | Onset spectrum; trihexyphenidyl benefit |
| [38284143](https://pubmed.ncbi.nlm.nih.gov/38284143/) | New ANO3 family + review | p.G6V; younger onset = more severe; scrambling-domain variants |
| [23893446](https://pubmed.ncbi.nlm.nih.gov/23893446/) | Genetics of dystonia | Reduced penetrance continuum |
| [29396174](https://pubmed.ncbi.nlm.nih.gov/29396174/) | Pediatric isolated dystonia | AD low-penetrance genes incl. ANO3; tertiary prevention |
| [37542824](https://pubmed.ncbi.nlm.nih.gov/37542824/) | GPi-DBS 5-year outcomes | 57% TWSTRS improvement |
| [41483253](https://pubmed.ncbi.nlm.nih.gov/41483253/) | BoNT ± physiotherapy | PT adjunct improves disability/pain/depression/QoL |
| [33099684](https://pubmed.ncbi.nlm.nih.gov/33099684/) | Neurorehabilitation in dystonia | Non-motor QoL burden |
| [32334381](https://pubmed.ncbi.nlm.nih.gov/32334381/) | Exome in complex dystonia | WES yield in complex dystonia |
| [29913018](https://pubmed.ncbi.nlm.nih.gov/29913018/) | Movement-disorder gene panel | 22% panel yield |
| [40470849](https://pubmed.ncbi.nlm.nih.gov/40470849/) | Neurogenetics clinic yield | Exome superior for complex phenotypes |
| [42845092](https://pubmed.ncbi.nlm.nih.gov/42845092/) | Isolated dystonia epidemiology | 50.2/100,000 prevalence; 68% female |
| [24978640](https://pubmed.ncbi.nlm.nih.gov/24978640/) | Dystonia update | ANO3 uncommon in cervical dystonia |
| [39749944](https://pubmed.ncbi.nlm.nih.gov/39749944/) | Indian dystonia genetics | ANO3 a rare yield |
| [41996745](https://pubmed.ncbi.nlm.nih.gov/41996745/) | 16-member Indian family | Intrafamilial variability |
| [38341631](https://pubmed.ncbi.nlm.nih.gov/38341631/) / [42493765](https://pubmed.ncbi.nlm.nih.gov/42493765/) | DBS case reports | Successful/marked GPi-DBS in ANO3 |
| [40302693](https://pubmed.ncbi.nlm.nih.gov/40302693/) | Childhood dystonia case series | Genetic counseling / recurrence prevention |

---

## Limitations and Knowledge Gaps

1. **No ANO3-specific epidemiology.** Prevalence/incidence of DYT24 specifically is undefined; only the parent class (isolated dystonia, ~50/100,000) is quantified.
2. **Mechanism partially inferred.** The step from striatal neuronal Ca²⁺/excitability changes to network-level dystonia is **inferred** from general dystonia pathophysiology, not directly demonstrated for ANO3.
3. **No faithful dominant animal model.** Existing rodent models are loss-of-function (hyperexcitability, febrile seizures) and do not reproduce dominant dystonia; no knock-in missense model with a dystonia phenotype is published.
4. **Large VUS burden.** 590 of 772 ClinVar *ANO3* records are VUS; functional assays (scramblase/Ca²⁺ activation) are not yet standardized for clinical classification.
5. **Penetrance/expressivity unquantified.** Reduced, age-dependent penetrance is described qualitatively; no numeric penetrance estimates exist.
6. **Treatment evidence is low-level.** DBS and pharmacotherapy data for ANO3 are case reports/small series; no controlled trials specific to DYT24.
7. **No prognostic biomarkers** and no genotype-stratified outcome data beyond the "scrambling-domain = more severe" observation.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse** carrying a recurrent human pathogenic missense allele (e.g., p.Glu510Lys or p.Ser651Asn) to test whether dominant-negative/GoF variants produce a dystonic phenotype and striatal circuit dysfunction — the key missing model.
2. **Standardize a functional assay** (Ca²⁺-dependent scramblase activation / ER Ca²⁺ signaling) to reclassify the 590 ANO3 VUS and establish ACMG PS3/BS3 evidence.
3. **Striatal circuit physiology:** slice electrophysiology and in vivo recordings in patient iPSC-derived striatal neurons/organoids to test predicted excitability changes and link ANO3 variants to K(Na)/Slack modulation.
4. **Genotype–phenotype registry:** assemble a multicenter ANO3 cohort to quantify penetrance, age-of-onset distribution, and domain-specific severity, and to derive ANO3-specific prevalence.
5. **Prospective DBS/BoNT outcome study** restricted to genetically confirmed DYT-ANO3 to move beyond case reports.
6. **Deep single-cell profiling** of human striatum to confirm the specific cell types (medium spiny neuron vs interneuron) most dependent on ANO3.

---

*Report compiled from 16 confirmed findings and 55 reviewed papers over 5 investigative iterations. Evidence types: human clinical (case series, cohorts, registries), in vitro/cellular (fibroblasts, heterologous expression), model organism (rodent knockouts), and computational (gnomAD constraint, ClinVar aggregation, brain RNA-seq).*


## Artifacts

- [OpenScientist final report](Dystonia_24-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Dystonia_24-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 32 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 11 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014019` (2 mentions) - the report calls it "MONDO"; MONDO calls it **dystonia 24**
- `HP:0032122` (1 mention) - the report calls it "Paroxysmal dystonia"; HP calls it **Very low visual acuity**
- `NCIT:C66099` (1 mention) - the report calls it "Trihexyphenidyl"; NCIT calls it **Mertiatide**
- `NCIT:C1005` (1 mention) - the report calls it "Botulinum Toxin"; NCIT calls it **Arsenic Trioxide**
- `NCIT:C38013` (1 mention) - the report calls it "Deep Brain Stimulation"; NCIT calls it **Range**
- `NCIT:C15682` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Dose-Rate**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016021` (GO_0016021) (1 mention) - replaced by `GO:0016020`