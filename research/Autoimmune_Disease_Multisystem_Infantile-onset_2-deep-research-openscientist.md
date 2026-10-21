---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-13T07:45:28.698415'
end_time: '2026-10-13T08:03:56.168768'
duration_seconds: 1107.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autoimmune Disease, Multisystem, Infantile-Onset, 2
  mondo_id: MONDO:0014861
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
citation_count: 19
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 13
  validator_version: 0.3.0
term_validation:
  total_terms: 37
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 10
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0014861
    reported_labels:
    - MONDO
    ontology_label: autoimmune disease, multisystem, infantile-onset, 2
  - term_id: DOID:0061161
    reported_labels:
    - DOID (Disease Ontology)
    ontology_label: infantile onset multisystem autoimmune disease 2
  - term_id: HP:0031540
    reported_labels:
    - Autoimmune bullous skin disease (bullous pemphigoid)
    ontology_label: Linear IgG deposits along the epidermal basement membrane zone
  - term_id: UBERON:0002097
    reported_labels:
    - Skin (epidermal basement membrane)
    ontology_label: skin of body
  - term_id: UBERON:0000178
    reported_labels:
    - Blood / coagulation system
    ontology_label: blood
  labels_variant: 5
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
  path: Autoimmune_Disease_Multisystem_Infantile-onset_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autoimmune_Disease_Multisystem_Infantile-onset_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autoimmune Disease, Multisystem, Infantile-Onset, 2
- **MONDO ID:** MONDO:0014861 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autoimmune Disease, Multisystem, Infantile-Onset, 2** covering all of the
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

# Autoimmune Disease, Multisystem, Infantile-Onset, 2 (ADMIO2) — Comprehensive Disease Report

**Disease:** Autoimmune Disease, Multisystem, Infantile-Onset, 2 (ADMIO2)
**MONDO ID:** MONDO:0014861 · **OMIM:** 617006 · **DOID:** 0061161 · **Category:** Mendelian (autosomal recessive inborn error of immunity)
**Causal gene:** *ZAP70* (HGNC:12858, NCBI Gene 7535, UniProt P43403, locus 2q11.2)

---

## Summary

**Autoimmune disease, multisystem, infantile-onset, 2 (ADMIO2; MONDO:0014861 / OMIM 617006)** is an ultra-rare, autosomal-recessive inborn error of immunity defined molecularly by **biallelic missense mutations in *ZAP70***, the Syk-family tyrosine kinase that is the proximal signaling node of the T-cell antigen receptor (TCR). The disease was delineated in a single sibling pair (a brother and sister) who were compound heterozygous for two private *ZAP70* alleles: a **hypomorphic allele, p.Arg192Trp (R192W)**, in the C-terminal SH2 domain that reduces binding to the phosphorylated ζ-chain, and an **activating allele, p.Arg360Pro (R360P)**, in the N-lobe of the catalytic domain that disrupts kinase autoinhibition to produce a weakly hyperactive enzyme ([PMID: 26783323](https://pubmed.ncbi.nlm.nih.gov/26783323/)). This particular allelic combination distinguishes ADMIO2 from the more common classic *ZAP70*-deficiency combined immunodeficiency (CID; OMIM 269840), which is caused by biallelic loss-of-function alleles.

The defining pathophysiologic concept is that **altered TCR signal *strength*** — not simple loss of signaling — breaks T-cell tolerance. Attenuated/altered ZAP70 kinase activity raises the thresholds of thymic (central) selection so that self-reactive thymocytes that should be negatively selected instead escape deletion and are positively selected, while the activating allele raises the sensitivity of mature peripheral T cells to weak self-ligands. The clinical result is severe, early-onset (first year of life) multiorgan autoimmunity — uncontrollable bullous pemphigoid, colitis, nephrotic syndrome with minimal-change glomerulonephritis, and a factor VIII autoantibody causing acquired hemophilia — superimposed on a partial combined immunodeficiency with CD8 lymphopenia. Both affected children required and were cured by **allogeneic hematopoietic stem cell transplantation (HSCT)**.

This report synthesizes the molecular genetics, mechanism, phenotype, epidemiology, diagnostics, prognosis, treatment, and model-organism evidence for ADMIO2. Because ADMIO2 *sensu stricto* is known from a single family, much supporting mechanistic and clinical detail is extrapolated from (a) functional studies of the specific R360P and R192W alleles, (b) the broader literature on biallelic *ZAP70* deficiency (~49 reported patients), and (c) mouse models — the SKG hypomorphic mutant (Zap70 W163C) and an R360P knock-in — that respectively model the two human alleles. Importantly, ADMIO2 must be distinguished from the clinically similar but mechanistically unrelated **STAT3 gain-of-function syndrome (ADMIO1; OMIM 615952)**, which was also surveyed during this investigation.

---

## 1. Disease Information

**Overview.** ADMIO2 is a monogenic (Mendelian) disorder of immune dysregulation presenting in infancy with multisystem autoimmunity. Mechanistically it is an inborn error of TCR signaling: biallelic *ZAP70* variants alter the quality and strength of TCR signal transduction, breaking immune tolerance while simultaneously impairing protective T-cell immunity.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014861 |
| OMIM | 617006 |
| DOID (Disease Ontology) | DOID:0061161 |
| MedGen | C4310768 / CN934735 |
| UMLS | C4310768 |
| Gene | *ZAP70* — HGNC:12858, NCBI Gene 7535, UniProt P43403, Ensembl ENSG00000115085, locus 2q11.2 |

These cross-references were confirmed via OLS4/MONDO (MONDO:0014861 *equivalentTo* OMIM:617006).

**Synonyms / alternative names.** "ADMIO2"; the disease is best referred to by its OMIM title "Autoimmune disease, multisystem, infantile-onset, 2." The underlying gene-level entity is "ZAP70-related combined immunodeficiency / immune dysregulation." ADMIO**1** (OMIM 615952) is the distinct STAT3-GOF syndrome.

**Information source.** Disease-level knowledge derives from aggregated resources (OMIM, MONDO, HPO) that are themselves built on a **single primary clinical report of two patients** ([PMID: 26783323](https://pubmed.ncbi.nlm.nih.gov/26783323/)). This is a disease-level (literature-aggregated) rather than EHR/individual-patient derived entry, and the small n (2) is the dominant limitation throughout.

---

## 2. Etiology

**Primary cause — genetic.** ADMIO2 is caused by **biallelic (compound heterozygous) missense mutations in *ZAP70***. Whole-exome sequencing of a five-member family identified the two affected siblings as compound heterozygous for two unique missense variants; healthy relatives were heterozygous carriers, establishing autosomal-recessive inheritance ([PMID: 26783323](https://pubmed.ncbi.nlm.nih.gov/26783323/)):

> *"revealed the affected siblings to be compound heterozygous for two unique missense mutations in the 70-kD T cell receptor ζ-chain associated protein (ZAP-70)"*

The two alleles have opposite biochemical effects:

> *"Mutation R192W in the C-SH2 domain exhibited reduced binding to phosphorylated ζ-chain, whereas mutation R360P in the N lobe of the catalytic domain disrupted an autoinhibitory mechanism, producing a weakly hyperactive ZAP-70 protein"*

**Genetic risk factors.** The disease-causing variants are themselves the risk factor; both were **private to the index family** and are not population polymorphisms. There are no established common-variant susceptibility loci or validated modifier genes for ADMIO2 specifically, though inter-individual variability in broader *ZAP70* deficiency (even between siblings carrying identical alleles) implies the existence of unidentified genetic/environmental modifiers ([PMID: 41790376](https://pubmed.ncbi.nlm.nih.gov/41790376/)).

**Environmental risk factors.** None are established as *causal*. As with other combined immunodeficiencies, infectious exposures (e.g., CMV) can precipitate or worsen clinical course in *ZAP70*-deficient patients ([PMID: 33484432](https://pubmed.ncbi.nlm.nih.gov/33484432/)), and endogenous retroviral superantigens modulate autoimmunity in the mouse model (see §6). **Consanguinity** is a risk factor for biallelic *ZAP70* disease generally (enriching homozygous LoF deficiency in Middle Eastern/North African populations), though the ADMIO2 index family was compound heterozygous rather than consanguineous.

**Protective factors.** No genetic or environmental protective factors are defined for ADMIO2. By inference from gnomAD constraint (below), heterozygous carriers are asymptomatic — a single wild-type *ZAP70* allele is protective/sufficient.

**Gene–environment interactions.** The best-characterized GxE axis is from the SKG mouse model: **endogenous mouse-mammary-tumor-virus (MMTV) superantigens and the microbiota** are required to convert the genetic lesion into overt arthritis, and antiretroviral therapy curtails disease ([PMID: 39589811](https://pubmed.ncbi.nlm.nih.gov/39589811/); [PMID: 37394552](https://pubmed.ncbi.nlm.nih.gov/37394552/)). Whether analogous triggers operate in human ADMIO2 is unknown.

---

## 3. Phenotypes

All ADMIO2 HPO annotations derive from the two siblings in [PMID: 26783323](https://pubmed.ncbi.nlm.nih.gov/26783323/):

> *"A brother and sister developed a previously undescribed constellation of autoimmune manifestations within their first year of life, with uncontrollable bullous pemphigoid, colitis, and proteinuria. The boy had hemophilia due to a factor VIII autoantibody and nephrotic syndrome"*

| Phenotype | HPO term | Type | Frequency (n=2) | Notes |
|---|---|---|---|---|
| Autoimmunity | HP:0002960 | Clinical/immunologic | 2/2 | Core feature |
| Infantile onset | HP:0003593 | Temporal | 2/2 | First year of life |
| Autoimmune bullous skin disease (bullous pemphigoid) | HP:0031540 | Physical/skin | 1/1 | Linear IgG along epidermal basement-membrane zone |
| Nephrotic syndrome | HP:0000100 | Clinical/renal | 1/2 | — |
| Minimal change glomerulonephritis | HP:0012579 | Laboratory/pathology | 1/2 | On renal biopsy |
| Podocyte foot process effacement | HP:0031266 | Pathology | 1/1 | Ultrastructural |
| Proteinuria | HP:0000093 | Laboratory | 2/2 | — |
| Colitis | HP:0002583 | Clinical/GI | 1/2 | Childhood onset (HP:0011463) |
| Increased CD4:CD8 ratio | HP:0033221 | Laboratory/immunologic | 2/2 | Reflects CD8 lymphopenia |
| Impaired PHA-induced T-cell transformation | HP:0025834 | Laboratory | 2/2 | Functional T-cell defect |
| Decreased specific antibody response (pneumococcal) | HP:0012476 | Laboratory | 1/1 | Humoral impairment |
| Acquired hemophilia A (factor VIII autoantibody) | — | Clinical/hematologic | 1/1 (boy) | Autoantibody-mediated |

**Phenotype characteristics.** *Onset:* neonatal–infantile (within the first year). *Severity:* severe ("uncontrollable" bullous pemphigoid; nephrotic-range proteinuria; bleeding from acquired hemophilia). *Progression:* progressive/refractory to conventional immunosuppression, ultimately requiring HSCT. *Frequency:* autoimmunity and the immunologic lab abnormalities were present in both siblings; organ-specific features were variably present.

**Broader *ZAP70*-deficiency phenotype (context).** A systematic review of 49 biallelic *ZAP70* patients ([PMID: 32431715](https://pubmed.ncbi.nlm.nih.gov/32431715/)) and a 13-patient HSCT cohort ([PMID: 41080547](https://pubmed.ncbi.nlm.nih.gov/41080547/)) describe profound CD8 lymphopenia (84.6% in the cohort), recurrent respiratory infections, cutaneous disease, and autoimmunity, with median symptom onset ~1 month:

> *"Eleven of thirteen patients (84.6%) exhibited profound CD8"* ([PMID: 41080547](https://pubmed.ncbi.nlm.nih.gov/41080547/))

**Quality-of-life impact.** No disease-specific QoL instruments (EQ-5D/SF-36/PROMIS) have been applied to ADMIO2. By inference, untreated disease is life-threatening and severely disabling (refractory multiorgan autoimmunity + immunodeficiency); successful HSCT can restore normal immune function and resolve autoimmunity (see §11–12).

---

## 4. Genetic / Molecular Information

**Causal gene.** *ZAP70* (Zeta-chain Associated Protein kinase 70 kDa), HGNC:12858, OMIM gene 176947, locus 2q11.2; protein UniProt P43403 — a 619-aa cytoplasmic Syk-family protein tyrosine kinase with two tandem N-terminal SH2 domains (binding doubly-phosphorylated ITAMs) and a C-terminal catalytic kinase domain.

**ADMIO2 pathogenic variants (private to index family).**

| Variant | Domain | Biochemical effect | Class |
|---|---|---|---|
| p.Arg192Trp (R192W) | C-terminal SH2 (C-SH2) | Reduced binding to phospho-ζ chain | **Hypomorphic** (partial LoF) |
| p.Arg360Pro (R360P) | N-lobe of kinase domain | Disrupts autoinhibition → weakly hyperactive kinase | **Activating** (GoF) |

Both are missense substitutions. In the context of this family with functional support, both would be classified pathogenic/likely-pathogenic, but they are **absent from population databases** (private), consistent with their non-recurrent nature.

**Variant classification per ACMG/AMP:** functional evidence (PS3), compound heterozygosity with segregation (PM3/PP1), absence from controls (PM2), and in-silico support place both alleles at least as likely pathogenic in this disease context.

**Allele frequency.** The R192W and R360P alleles are not catalogued as recurrent population variants (private). For the gene overall, **gnomAD constraint** (ENSG00000115085): pLI = 0.88, LOEUF (oe_lof) = 0.173 (90% CI 0.09–0.364), observed/expected LoF = 5/28.8, missense Z = 2.76 — indicating that *ZAP70* is **intolerant of heterozygous loss of function**, yet heterozygous carriers are clinically healthy (biallelic hit required for disease).

**Somatic vs germline.** Germline; inherited from heterozygous carrier parents.

**Functional consequences.** A *combination* of loss-of-function (R192W reduces ITAM engagement) and gain-of-function (R360P releases autoinhibition) — the net effect is **altered/dysregulated TCR signaling**, not simple nullizygosity.

**ClinVar variant landscape (gene-level).** ClinVar (NCBI E-utilities, 2026) returns ~616 *ZAP70* records: ~79 pathogenic, ~21 likely-pathogenic, ~354 VUS, ~422 benign/likely-benign. Most pathogenic/likely-pathogenic alleles are **LoF/hypomorphic variants causing classic *ZAP70*-deficiency CID (OMIM 269840)** — e.g., homozygous p.Ala463Val ([PMID: 33484432](https://pubmed.ncbi.nlm.nih.gov/33484432/)) — whereas the ADMIO2-defining p.Arg192Trp and p.Arg360Pro alleles remain **private to the index family**.

**Modifier genes / epigenetics / chromosomal abnormalities.** No ADMIO2-specific modifier genes, epigenetic marks, or chromosomal/structural abnormalities are established. Phenotypic divergence among siblings with identical *ZAP70* genotypes in the broader literature implies unidentified modifiers ([PMID: 41790376](https://pubmed.ncbi.nlm.nih.gov/41790376/)).

---

## 5. Environmental Information

ADMIO2 is a **monogenic disease with no required environmental cause**. Relevant non-genetic modifiers/triggers, largely by inference or from models:

- **Infectious agents.** Not causal, but infections (notably **CMV**) complicate the associated immunodeficiency and can unmask/worsen disease in *ZAP70*-deficient infants ([PMID: 33484432](https://pubmed.ncbi.nlm.nih.gov/33484432/)). In the SKG mouse, *Brucella* infection drives a spondyloarthritis-like phenotype on the susceptible *Zap70* background ([PMID: 40027658](https://pubmed.ncbi.nlm.nih.gov/40027658/)).
- **Endogenous retrovirus / microbiota.** MMTV-derived superantigens and gut microbiota are required to convert the mouse genetic lesion into overt autoimmune arthritis ([PMID: 39589811](https://pubmed.ncbi.nlm.nih.gov/39589811/); [PMID: 37394552](https://pubmed.ncbi.nlm.nih.gov/37394552/)).
- **Lifestyle factors.** Not applicable (infantile-onset Mendelian disease).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic *ZAP70* missense mutations** (R192W hypomorphic + R360P activating) are inherited → **altered ZAP70 protein** with reduced phospho-ζ binding (R192W) *and* weakened kinase autoinhibition (R360P). *(Demonstrated — functional assays, [PMID: 26783323](https://pubmed.ncbi.nlm.nih.gov/26783323/).)*
2. Altered ZAP70 **changes the strength/quality of TCR signal transduction** at the proximal node (ZAP70 is recruited to doubly-phosphorylated CD3/ζ ITAMs, activated by Lck, and phosphorylates LAT/SLP76 to drive Ca²⁺/NFAT, Ras–MAPK, and NF-κB). *(Pathway demonstrated; allele-specific effect inferred.)*
3. **In the thymus (central tolerance):** attenuated/altered TCR signaling **raises selection thresholds**, so self-reactive thymocytes that should be negatively selected instead escape deletion and are positively selected → export of self-reactive T cells. *(Demonstrated in SKG mouse, [PMID: 37394552](https://pubmed.ncbi.nlm.nih.gov/37394552/).)*
4. **In the periphery (peripheral tolerance):** the R360P activating allele **increases mature T-cell sensitivity to weak/self ligands** that would normally be ignored → activation of autoreactive T cells. *(Demonstrated in R360P knock-in mouse, [PMID: 33531381](https://pubmed.ncbi.nlm.nih.gov/33531381/).)*
5. Activation of autoreactive CD4⁺ (and dysregulated) T cells **drives T-follicular-helper (Tfh) expansion and aberrant B-cell help** → **production of pathogenic autoantibodies** (anti-basement-membrane IgG, anti-factor VIII, anti-podocyte/glomerular). *(Tfh expansion demonstrated in mouse [PMID: 33531381]; autoantibodies demonstrated in patients [PMID: 26783323].)*
6. **Autoantibody- and T-cell–mediated tissue injury** at specific organs → **clinical manifestations:** bullous pemphigoid (skin basement membrane), colitis (gut), minimal-change nephrotic syndrome with podocyte foot-process effacement (kidney), acquired hemophilia A (factor VIII neutralization). *(Demonstrated — clinical/pathology, [PMID: 26783323].)*
7. **In parallel (branch):** the hypomorphic R192W allele plus overall signaling impairment **reduces CD8⁺ T-cell development and T-cell function** → **partial combined immunodeficiency** (CD8 lymphopenia, impaired PHA response, poor specific antibody) → susceptibility to infection. *(Demonstrated — immunophenotype, [PMID: 26783323]; broader cohorts [PMID: 32431715].)*

```
 ZAP70 biallelic missense (R192W hypomorphic + R360P activating)
            │
            ▼
   Altered TCR signal STRENGTH (not absent)
        ┌───────────────┴───────────────┐
        ▼                               ▼
 Raised thymic selection          Increased peripheral T-cell
 thresholds → self-reactive       sensitivity to weak/self
 thymocytes escape deletion       ligands (R360P)
 (central tolerance break)        (peripheral tolerance break)
        └───────────────┬───────────────┘
                        ▼
          Autoreactive T cells + Tfh expansion
                        ▼
              Pathogenic autoantibodies
                        ▼
   Multiorgan autoimmunity: skin (bullous pemphigoid),
   gut (colitis), kidney (nephrotic syndrome), FVIII inhibitor
                        │
            (parallel branch via hypomorphic allele)
                        ▼
   CD8 lymphopenia + impaired T-cell function → infection risk
```

### Supporting detail

- **Molecular pathways.** Proximal TCR signaling: Lck → CD3/ζ ITAM phosphorylation → ZAP70 recruitment/activation → LAT/SLP76 phosphorylation → PLCγ1 (Ca²⁺/NFAT), Ras–MAPK/ERK, PKCθ–NF-κB. (Reactome "TCR signaling"; KEGG hsa04660.)
- **Autoinhibition structural basis.** The tandem-SH2 (tSH2) module locks the kinase in a closed, inactive conformation; ITAM binding or ζ-phosphorylation triggers the closed→open transition ([PMID: 26237552](https://pubmed.ncbi.nlm.nih.gov/26237552/)):
  > *"TCR binding or phosphorylation of Zap70 triggers a transition from a closed, autoinhibited conformation to an open conformation"*
  The ADMIO2 R360P substitution lies in the N-lobe and structurally weakens this autoinhibition. TCR dwell time tunes kinase output ([PMID: 26237552](https://pubmed.ncbi.nlm.nih.gov/26237552/)); tSH2 dynamics differ between Syk and ZAP-70, explaining ZAP-70's tighter autoinhibition ([PMID: 34601763](https://pubmed.ncbi.nlm.nih.gov/34601763/)).
- **Immune system involvement.** Autoimmunity + partial immunodeficiency (immune dysregulation). Tolerance is broken in both compartments; autoantibodies are the proximate effectors of organ injury.
- **Cellular processes / cell types.** CD4⁺ T cells (CL:0000624), CD8⁺ T cells (CL:0000625; depleted), Tfh cells, thymocytes undergoing selection, and downstream autoantibody-producing B cells/plasma cells.
- **GO terms.** T-cell receptor signaling pathway (GO:0050852); positive/negative thymic T-cell selection (GO:0045059 / GO:0045060); T-cell tolerance induction (GO:0002517); protein tyrosine kinase activity (GO:0004713); regulation of immune response (GO:0050776).
- **Functional proof of the two-allele model.**
  > *"disruption of ZAP70 autoinhibition by the R360P mutation enables increased mature T cell sensitivity to self-antigens that would normally be ignored by wild-type T cells, a mechanism that may contribute to the break of tolerance in human patients with R360P mutation"* ([PMID: 33531381](https://pubmed.ncbi.nlm.nih.gov/33531381/))
  > *"Defective TCR signaling by ZAP70 mutation alters thymic selection thresholds and allows the positive selection of otherwise negatively selected self-reactive T cells"* ([PMID: 37394552](https://pubmed.ncbi.nlm.nih.gov/37394552/))
- **Spectrum concept.** Graded reduction of ZAP70/TCR signal produces a continuum from immunodeficiency to autoimmunity ([PMID: 41770842](https://pubmed.ncbi.nlm.nih.gov/41770842/)):
  > *"the effects of graded TCR signal reduction manifest as a disease spectrum encompassing T cell immune deficiency, latent autoimmunity, and overt autoimmune disease"*

---

## 7. Anatomical Structures Affected

**Organ level (primary targets of autoimmunity):**

| Organ / system | UBERON | Manifestation |
|---|---|---|
| Skin (epidermal basement membrane) | UBERON:0002097 | Bullous pemphigoid |
| Kidney (glomerulus/podocyte) | UBERON:0000074 (renal glomerulus) | Nephrotic syndrome, minimal-change GN, foot-process effacement |
| Colon / large intestine | UBERON:0001155 | Colitis |
| Blood / coagulation system | UBERON:0000178 | Factor VIII autoantibody → acquired hemophilia A |
| Immune/lymphoid system (thymus) | UBERON:0002370 (thymus) | Defective T-cell development/selection |

**Secondary involvement.** Infectious complications of the immunodeficiency (e.g., respiratory tract, systemic CMV) affect the respiratory system (UBERON:0001004) and others.

**Tissue / cell level.** Epithelial basement membrane (skin), renal podocytes (CL:0000653), colonic mucosa; immunologically, thymocytes and peripheral T lymphocytes. Targeted/dysregulated cell populations: CD4⁺ αβ T cell (CL:0000624), CD8⁺ αβ T cell (CL:0000625, depleted), T-follicular-helper cell, autoantibody-secreting B cell/plasma cell (CL:0000786/CL:0000980).

**Subcellular level.** ZAP70 functions at the inner-leaflet **plasma membrane / TCR complex** (GO:0005886; GO:0042101 T-cell receptor complex) in the **cytoplasm** (GO:0005737). Podocyte foot-process effacement is an ultrastructural (cytoskeletal) lesion.

**Lateralization.** Systemic/bilateral (skin, kidneys, gut) — not lateralized.

---

## 8. Temporal Development

- **Onset.** Congenital predisposition with clinical onset in **infancy — within the first year of life** (HP:0003593). Pattern is subacute-to-progressive.
- **Progression.** Severe and **refractory/progressive** under conventional immunosuppression; the index siblings progressed to requiring HSCT. In the broader *ZAP70*-deficiency literature, median symptom onset is ~1 month, and untreated disease is life-threatening.
- **Disease course.** Chronic and progressive until definitively treated; **curable** (remission) by allogeneic HSCT (treatment-induced remission). No spontaneous remission is described.
- **Critical period / window of intervention.** Early recognition and HSCT before irreversible organ damage or fatal infection is the key therapeutic window; the infant thymus is more amenable to reconstitution (relevant to experimental intrathymic gene therapy, [PMID: 16075064](https://pubmed.ncbi.nlm.nih.gov/16075064/)).

---

## 9. Inheritance and Population

- **Inheritance.** Autosomal recessive (HP:0000007), confirmed by compound heterozygosity in affected siblings and heterozygous healthy carriers ([PMID: 26783323](https://pubmed.ncbi.nlm.nih.gov/26783323/)):
  > *"Healthy relatives were heterozygous mutation carriers"*
- **Penetrance / expressivity.** Within the single family, biallelic genotype was fully penetrant for autoimmunity in both siblings, with variable organ-specific expressivity (e.g., hemophilia and nephrotic syndrome only in the boy). Broader *ZAP70* disease shows variable expressivity even among identical-genotype siblings ([PMID: 41790376](https://pubmed.ncbi.nlm.nih.gov/41790376/)).
- **Epidemiology.** **Ultra-rare.** ADMIO2 *sensu stricto* is reported in a single sibling pair; formal prevalence is not estimated (<1 per 1,000,000). The broader biallelic *ZAP70*-deficiency entity has ~49 reported cases worldwide ([PMID: 32431715](https://pubmed.ncbi.nlm.nih.gov/32431715/)).
- **Carrier frequency / constraint.** Heterozygous carriers are healthy; gnomAD shows *ZAP70* is LoF-constrained (pLI 0.88, LOEUF 0.173) but disease requires two hits.
- **Founder effects / consanguinity.** The ADMIO2 alleles are private (no founder effect). Classic *ZAP70* deficiency is enriched in consanguineous Middle Eastern/North African populations ([PMID: 41080547](https://pubmed.ncbi.nlm.nih.gov/41080547/); [PMID: 41790376](https://pubmed.ncbi.nlm.nih.gov/41790376/)).
- **Sex ratio / demographics.** No sex predilection (AR); the index pair comprised one male and one female. No established ethnic predilection for ADMIO2 specifically.

---

## 10. Diagnostics

**Immunologic laboratory tests (characteristic pattern).**
- Flow cytometry: **CD8 lymphopenia / low CD8⁺ T cells → increased CD4:CD8 ratio** (HP:0033221). In classic *ZAP70* deficiency, intracellular ZAP70 is absent/reduced on gated T cells ([PMID: 33484432](https://pubmed.ncbi.nlm.nih.gov/33484432/)).
- **Impaired T-cell proliferation to mitogens (PHA/ConA)** (HP:0025834).
- Humoral: variable; decreased specific (pneumococcal) antibody response in one sibling.
- Autoimmune workup: anti–basement-membrane IgG (direct immunofluorescence shows **linear IgG along the epidermal basement-membrane zone**), **factor VIII inhibitor assay** (acquired hemophilia), urinalysis for proteinuria.

**Biopsy / pathology.** Skin DIF (bullous pemphigoid pattern); **renal biopsy showing minimal-change glomerulonephritis with podocyte foot-process effacement** on electron microscopy; colonic biopsy for colitis.

**Newborn screening caveat.** TREC-based SCID newborn screening may be **normal** in *ZAP70* / CID, so a normal TREC screen does not exclude the diagnosis ([PMID: 33484432](https://pubmed.ncbi.nlm.nih.gov/33484432/); [PMID: 22664165](https://pubmed.ncbi.nlm.nih.gov/22664165/)).

**Genetic testing (diagnostic gold standard).** **WES/WGS or a primary-immunodeficiency / inborn-errors-of-immunity gene panel including *ZAP70*** is the definitive test; the disease was discovered by WES ([PMID: 26783323](https://pubmed.ncbi.nlm.nih.gov/26783323/)). Confirm biallelic *ZAP70* variants, segregation (parental carriers), and **functional validation** (phospho-ζ binding, kinase activity, TCR-induced proliferation/IL-2) because ADMIO2 alleles are private and otherwise VUS.

**Clinical criteria / differential diagnosis.** No formal consensus criteria exist. Key differentials for infantile multiorgan autoimmunity:
- **STAT3 gain-of-function (ADMIO1, OMIM 615952)** — early-onset polyautoimmunity, lymphoproliferation, double-negative T cells, responsive to JAK inhibitors ([PMID: 36228738](https://pubmed.ncbi.nlm.nih.gov/36228738/)).
- **IPEX (FOXP3)**, **CTLA4 haploinsufficiency**, **LRBA deficiency**, **APECED (AIRE)**, and classic **ZAP70-deficiency CID (OMIM 269840)**.
Distinguishing feature of ADMIO2: biallelic *ZAP70* with the specific hypomorphic+activating combination and CD8 lymphopenia with autoimmunity.

---

## 11. Outcome / Prognosis

- **Natural course (untreated).** Severe, refractory, life-threatening multiorgan autoimmunity plus immunodeficiency; both index children required HSCT after failing conventional therapy.
- **With definitive treatment.** **Allogeneic HSCT is curative** and resolved the autoimmunity in both ADMIO2 siblings ([PMID: 26783323](https://pubmed.ncbi.nlm.nih.gov/26783323/)). In the broader *ZAP70*-deficiency literature, long-term outcomes after HSCT are excellent: 8/8 patients alive at median 13.5 years, with restored T-cell function and resolution of infections and autoimmunity ([PMID: 27438785](https://pubmed.ncbi.nlm.nih.gov/27438785/)).
- **Complications.** Pre-transplant: bleeding (FVIII inhibitor), nephrotic complications, colitis, infection. Transplant-related: graft failure, GVHD, conditioning toxicity.
- **Prognostic factors.** Timeliness of diagnosis and HSCT; control of autoimmunity and infection pre-transplant; donor source/conditioning. CD8 reconstitution post-HSCT is generally good.

---

## 12. Treatment

**Definitive / curative.**
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — curative; the only established cure (NCIT: Allogeneic Hematopoietic Stem Cell Transplantation, C15349). Both ADMIO2 siblings were cured by HCT:
  > *"Both children required allogeneic hematopoietic cell transplantation (HCT), which resolved their autoimmunity"* ([PMID: 26783323](https://pubmed.ncbi.nlm.nih.gov/26783323/))
  Supported by durable success in *ZAP70* deficiency broadly (8/8 alive at 13.5 yr, [PMID: 27438785](https://pubmed.ncbi.nlm.nih.gov/27438785/); curative in majority of a 13-patient cohort, [PMID: 41080547](https://pubmed.ncbi.nlm.nih.gov/41080547/)).

**Supportive / bridging immunosuppression (pre-HSCT, symptom control).**
- Corticosteroids (NCIT C682); IVIG (C29368); **rituximab / B-cell depletion** for autoantibody-mediated disease (FVIII inhibitor, pemphigoid) (NCIT C1702); calcineurin inhibitors; standard management of nephrotic syndrome and colitis.

**Experimental / preclinical — gene therapy.**
- *ZAP70*-deficient mice have been corrected by **retroviral/lentiviral HSC gene transfer** ([PMID: 12149205](https://pubmed.ncbi.nlm.nih.gov/12149205/)), **intrathymic lentiviral** delivery ([PMID: 16075064](https://pubmed.ncbi.nlm.nih.gov/16075064/)), and **intrathymic AAV8/9/10** gene transfer restoring thymopoiesis and long-term peripheral T-cell function ([PMID: 31513879](https://pubmed.ncbi.nlm.nih.gov/31513879/)):
  > *"Intrathymic AAV-transduced progenitors promote a rapid restoration of the thymic architecture, with a single wave of thymopoiesis generating long-term peripheral T-cell function"*
  Note: gene *addition* addresses the deficiency component; the ADMIO2 activating (R360P) allele is dominant-acting at the cellular level, so a correction strategy for the autoimmune component may require allele-specific considerations.

**Mechanism-informed experimental approaches (from models).** In the SKG hypomorphic model, **antiretroviral therapy and depletion of superantigen-reactive T cells** curtailed arthritis ([PMID: 39589811](https://pubmed.ncbi.nlm.nih.gov/39589811/)); JAK inhibition is effective in the mechanistically analogous STAT3-GOF syndrome ([PMID: 36228738](https://pubmed.ncbi.nlm.nih.gov/36228738/)) but is not established for ADMIO2.

**Pharmacogenomics.** None established specific to ADMIO2.

---

## 13. Prevention

- **Primary prevention.** Not applicable in the usual sense (monogenic recessive disease). **Genetic counseling** for carrier couples; **carrier/cascade testing** in affected families; **prenatal diagnosis / preimplantation genetic testing (PGT)** is possible once familial variants are known.
- **Secondary prevention.** Early diagnosis via immunophenotyping + genetic testing in infants with multiorgan autoimmunity or CID; note TREC newborn screening can miss *ZAP70* disease.
- **Tertiary prevention.** Infection prophylaxis (antimicrobial, antiviral, IVIG), prompt treatment of autoimmunity, and timely HSCT to prevent irreversible organ damage.
- **Counseling.** 25% recurrence risk per pregnancy for carrier couples (AR).

---

## 14. Other Species / Natural Disease

- **Taxonomy / ortholog.** Mouse (*Mus musculus*, NCBI Taxon 10090); ortholog **Zap70** (NCBI Gene 22637). ZAP70 is evolutionarily conserved; TCR-proximal signaling architecture (Lck + ZAP-70/Syk, ITAM recognition) is conserved even in teleosts (rainbow trout homology modeling, [PMID: 41240985](https://pubmed.ncbi.nlm.nih.gov/41240985/)).
- **Natural disease in other species.** No well-characterized naturally-occurring companion-animal homolog of ADMIO2 is documented; relevance is primarily through engineered rodent models.
- **Comparative biology.** The mouse allelic series (below) recapitulates the human deficiency↔autoimmunity spectrum, underscoring conserved mechanisms.

---

## 15. Model Organisms

| Model | Allele | Phenotype | Models which human allele | Key refs |
|---|---|---|---|---|
| **SKG mouse** | *Zap70* W163C (hypomorphic) | CD4⁺ T-cell–mediated autoimmune arthritis (BALB/c) / lupus-like disease (C57BL/6); raised thymic selection thresholds; MMTV-superantigen/microbiota-dependent | Hypomorphic (R192W-like) | [PMID: 37394552](https://pubmed.ncbi.nlm.nih.gov/37394552/), [PMID: 39589811](https://pubmed.ncbi.nlm.nih.gov/39589811/) |
| **R360P knock-in** | *Zap70* R360P (activating) | Grossly normal T-cell development but increased TCR signaling; enhanced Tfh after LCMV; on OTI TCR, heightened responses to weak/self ligands | Activating (R360P) | [PMID: 33531381](https://pubmed.ncbi.nlm.nih.gov/33531381/) |
| ***Zap70* knockout** | Null | Models human *ZAP70*-deficiency SCID: selective absence of CD8⁺ T cells, nonfunctional CD4⁺, thymic block; reversible by gene transfer | Deficiency/null | [PMID: 12149205](https://pubmed.ncbi.nlm.nih.gov/12149205/), [PMID: 16075064](https://pubmed.ncbi.nlm.nih.gov/16075064/), [PMID: 31513879](https://pubmed.ncbi.nlm.nih.gov/31513879/) |

Direct quotes:
> *"Mice with a ZAP70 R360P mutation and polyclonal TCR repertoires exhibited relatively normal T cell development but showed evidence of increased signaling"* ([PMID: 33531381](https://pubmed.ncbi.nlm.nih.gov/33531381/))

> *"the effects of graded TCR signal reduction manifest as a disease spectrum encompassing T cell immune deficiency, latent autoimmunity, and overt autoimmune disease"* ([PMID: 41770842](https://pubmed.ncbi.nlm.nih.gov/41770842/))

**Model types:** mammalian (mouse) in vivo; knock-in, knockout, and point-mutant (ENU-derived SKG) lines. **Recapitulation:** the two alleles are each separately modeled and together support the "altered-signal-strength breaks tolerance" mechanism; the knockout models the immunodeficiency arm. **Limitations:** no single mouse carries the exact *human compound-heterozygous R192W/R360P* genotype, so the combined/epistatic effect of the two alleles together is modeled only indirectly; mouse autoimmune targets (arthritis) differ from the human organ spectrum (skin/kidney/gut), reflecting species-specific self-antigens and superantigen biology. **Resources:** MGI (Zap70, SKG allele), IMPC/IMSR.

---

## Mechanistic Model / Interpretation

ADMIO2 is best understood as a **"Goldilocks" disorder of TCR signal strength**. ZAP70 sits at the apex of TCR signaling, and the amount of kinase output a thymocyte or T cell experiences determines its fate: too little signal → failed positive selection / immunodeficiency; intermediate aberrant signal → escape from negative selection + peripheral hyper-responsiveness → autoimmunity; normal signal → tolerance + protective immunity. The ADMIO2 genotype pairs a **hypomorphic allele** (R192W; less ITAM engagement, raising selection thresholds like SKG) with an **activating allele** (R360P; released autoinhibition, lowering the threshold for peripheral responses to self). The *net* effect is a signaling milieu that simultaneously (a) allows self-reactive T cells to be positively selected and exported and (b) renders mature T cells inappropriately responsive to weak self-ligands — a double break of central and peripheral tolerance — while still leaving CD8 development and overall T-cell function partially impaired. The downstream effector arm is autoantibody-mediated, explaining the specific, disparate organ targets (skin basement membrane, glomerular podocyte, colon, clotting factor VIII). This model is anchored by direct biochemistry of the two alleles ([PMID: 26783323](https://pubmed.ncbi.nlm.nih.gov/26783323/)), structural understanding of ZAP70 autoinhibition ([PMID: 26237552](https://pubmed.ncbi.nlm.nih.gov/26237552/), [PMID: 34601763](https://pubmed.ncbi.nlm.nih.gov/34601763/)), and two complementary mouse models ([PMID: 37394552](https://pubmed.ncbi.nlm.nih.gov/37394552/), [PMID: 33531381](https://pubmed.ncbi.nlm.nih.gov/33531381/)).

---

## Evidence Base

| PMID | Role in this report | How it supports/challenges findings |
|---|---|---|
| [26783323](https://pubmed.ncbi.nlm.nih.gov/26783323/) | **Defining primary report** | Establishes the disease, compound-het *ZAP70* genotype, two-allele biochemistry, clinical phenotype, AR inheritance, and HSCT cure. Sole clinical source (n=2) — the central limitation. |
| [33531381](https://pubmed.ncbi.nlm.nih.gov/33531381/) | Mechanism (activating allele) | R360P knock-in proves increased self-ligand sensitivity → peripheral tolerance break. |
| [37394552](https://pubmed.ncbi.nlm.nih.gov/37394552/) | Mechanism (hypomorphic allele) | SKG model shows altered thresholds → positive selection of self-reactive T cells (central tolerance break). |
| [39589811](https://pubmed.ncbi.nlm.nih.gov/39589811/) | Gene–environment / effector | MMTV superantigen & retrovirus-dependent conversion to overt autoimmunity; ART mitigates. |
| [26237552](https://pubmed.ncbi.nlm.nih.gov/26237552/) / [34601763](https://pubmed.ncbi.nlm.nih.gov/34601763/) | Structural basis | Define ZAP70 autoinhibition and tSH2 dynamics disrupted by R360P. |
| [41770842](https://pubmed.ncbi.nlm.nih.gov/41770842/) | Framing | Graded TCR-signal spectrum (deficiency↔autoimmunity). |
| [32431715](https://pubmed.ncbi.nlm.nih.gov/32431715/) / [41080547](https://pubmed.ncbi.nlm.nih.gov/41080547/) / [41790376](https://pubmed.ncbi.nlm.nih.gov/41790376/) | Broader *ZAP70* context | Phenotype spectrum, CD8 lymphopenia, consanguinity, HSCT outcomes. |
| [27438785](https://pubmed.ncbi.nlm.nih.gov/27438785/) | Prognosis / treatment | Long-term HSCT success (8/8 at 13.5 yr). |
| [12149205](https://pubmed.ncbi.nlm.nih.gov/12149205/) / [16075064](https://pubmed.ncbi.nlm.nih.gov/16075064/) / [31513879](https://pubmed.ncbi.nlm.nih.gov/31513879/) | Experimental therapy | Preclinical gene-therapy correction of *ZAP70* deficiency. |
| [33484432](https://pubmed.ncbi.nlm.nih.gov/33484432/) / [22664165](https://pubmed.ncbi.nlm.nih.gov/22664165/) | Diagnostics | CD8 lymphopenia presentation; TREC screening caveats. |
| [36228738](https://pubmed.ncbi.nlm.nih.gov/36228738/) | Differential diagnosis | STAT3-GOF (ADMIO1) — the key mimic, JAK-inhibitor-responsive. |

---

## Limitations and Knowledge Gaps

1. **Single family (n=2).** All ADMIO2-specific clinical and genetic data come from one sibling pair. Prevalence, penetrance, expressivity, full phenotype spectrum, and genotype–phenotype correlations cannot be generalized.
2. **Private alleles.** R192W and R360P are not recurrent; no population allele-frequency or additional segregation data beyond the index family.
3. **No combined-genotype animal model.** The two alleles are modeled separately (SKG and R360P knock-in); the epistatic effect of the exact human *compound-heterozygous* genotype is inferred, not demonstrated.
4. **Effector mechanism partly inferred.** The link from altered T-cell tolerance to the specific autoantibody targets (pemphigoid, podocyte, FVIII) is clinically observed but mechanistically underexplored for ADMIO2.
5. **No ADMIO2-specific trials or QoL/natural-history data.** Treatment and prognosis rest on the single report plus extrapolation from the broader *ZAP70*-deficiency literature.
6. **Therapeutic uncertainty for the activating allele.** Whether standard gene-addition gene therapy (effective for deficiency) would correct the dominant cellular effect of R360P is unknown; JAK-inhibitor utility (as in STAT3-GOF) is untested here.

---

## Proposed Follow-up Experiments / Actions

1. **International case-finding / GeneMatcher.** Actively solicit additional ADMIO2 families via GeneMatcher, inborn-errors-of-immunity consortia, and ClinVar to expand the phenotype and genotype spectrum and estimate penetrance.
2. **Compound-heterozygous model.** Engineer a mouse or patient-derived iPSC → thymic organoid carrying *both* R192W and R360P to test the predicted additive/epistatic tolerance break and reproduce human-relevant autoimmunity.
3. **Autoantibody repertoire and target mapping.** Define the autoantigen specificities (skin BP180/BP230, podocyte antigens, FVIII epitopes) and the Tfh/B-cell dynamics driving them in ADMIO2 (and in R360P knock-in mice).
4. **Therapeutic screen.** Test JAK inhibition, B-cell depletion, abatacept/CTLA4-Ig, and allele-selective approaches in cellular/animal models to identify bridge therapies that control autoimmunity pre-HSCT.
5. **Gene-therapy feasibility for the activating allele.** Evaluate allele-specific knockdown/base-editing of R360P versus gene-addition in *ZAP70* models to determine whether gene therapy can address both the deficiency and autoimmune arms.
6. **Diagnostic yield of functional validation.** Formalize a functional assay panel (phospho-ζ binding, kinase activity, TCR-induced IL-2/proliferation, Ca²⁺ flux) to reclassify *ZAP70* VUS and flag hypomorphic+activating combinations.

---

*Report compiled from 7 confirmed findings and 35 reviewed papers over 5 investigation iterations. Evidence sources span human clinical (single defining family + broader cohorts), model organism (mouse SKG, R360P knock-in, knockout), in vitro/biochemical (allele functional assays, ZAP70 structural dynamics), and computational (gnomAD constraint, ClinVar aggregation, OLS4/MONDO cross-references).*


## Artifacts

- [OpenScientist final report](Autoimmune_Disease_Multisystem_Infantile-onset_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autoimmune_Disease_Multisystem_Infantile-onset_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 20 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014861` (4 mentions) - the report calls it "MONDO"; MONDO calls it **autoimmune disease, multisystem, infantile-onset, 2**
- `DOID:0061161` (1 mention) - the report calls it "DOID (Disease Ontology)"; DOID calls it **infantile onset multisystem autoimmune disease 2**
- `HP:0031540` (1 mention) - the report calls it "Autoimmune bullous skin disease (bullous pemphigoid)"; HP calls it **Linear IgG deposits along the epidermal basement membrane zone**
- `UBERON:0002097` (1 mention) - the report calls it "Skin (epidermal basement membrane)"; UBERON calls it **skin of body**
- `UBERON:0000178` (1 mention) - the report calls it "Blood / coagulation system"; UBERON calls it **blood**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003593` (2 mentions) - the report calls it "Infantile onset", "infancy — within the first year of life"; HP calls it **Infantile onset**, and lists "Onset in first year of life" among its other names
- `HP:0033221` (2 mentions) - the report calls it "Increased CD4:CD8 ratio", "CD8 lymphopenia / low CD8⁺ T cells → increased CD4:CD8 ratio"; HP calls it **Increased CD4:CD8 ratio**
- `HP:0025834` (2 mentions) - the report calls it "Impaired PHA-induced T-cell transformation", "Impaired T-cell proliferation to mitogens (PHA/ConA)"; HP calls it **Impaired phytohemagglutinin-induced T lymphocyte transformation**, and lists "Impaired T lymphocyte transformation with phytohemagglutinin" among its other names
- `HP:0012476` (1 mention) - the report calls it "Decreased specific antibody response (pneumococcal)"; HP calls it **Decreased circulating specific pneumococcal antibody concentration**, and lists "Decreased specific pneumococcal antibody level" among its other names
- `UBERON:0001155` (1 mention) - the report calls it "Colon / large intestine"; UBERON calls it **colon**, and lists "posterior intestine" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003593` - called "Infantile onset", "infancy — within the first year of life"
- `HP:0033221` - called "Increased CD4:CD8 ratio", "CD8 lymphopenia / low CD8⁺ T cells → increased CD4:CD8 ratio"
- `HP:0025834` - called "Impaired PHA-induced T-cell transformation", "Impaired T-cell proliferation to mitogens (PHA/ConA)"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.