---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T08:42:30.940150'
end_time: '2026-09-06T09:21:35.958965'
duration_seconds: 2345.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autoimmune Pancreatitis
  mondo_id: MONDO:0015175
  category: Complex
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
citation_count: 42
reference_validation:
  total_references: 42
  verified: 42
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 42
  on_topic: 29
  validator_version: 0.2.1
term_validation:
  total_terms: 37
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 26
  labels_matching: 15
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0001824
    reported_labels:
    - Symptom
    ontology_label: Weight loss
  - term_id: HP:0002027
    reported_labels:
    - Symptom
    ontology_label: Abdominal pain
  - term_id: HP:0001738
    reported_labels:
    - Lab/functional
    ontology_label: Exocrine pancreatic insufficiency
  - term_id: HP:0000819
    reported_labels:
    - Lab abnormality
    ontology_label: Diabetes mellitus
  - term_id: HP:0030355
    reported_labels:
    - Increased circulating IgG level
    ontology_label: Abnormal circulating interferon-gamma concentration
  - term_id: HP:0001880
    reported_labels:
    - Lab abnormality
    ontology_label: Increased total eosinophil count
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Autoimmune_Pancreatitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autoimmune_Pancreatitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autoimmune Pancreatitis
- **MONDO ID:** MONDO:0015175 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Autoimmune Pancreatitis** covering all of the
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

# Autoimmune Pancreatitis (MONDO:0015175): A Comprehensive Disease Characterization

## Summary

**Autoimmune pancreatitis (AIP)** is a rare, corticosteroid-responsive fibroinflammatory form of chronic pancreatitis that is now understood to comprise **three immunologically distinct subtypes**. **Type 1 AIP** — lymphoplasmacytic sclerosing pancreatitis (LPSP) — is the pancreatic manifestation of the systemic **IgG4-related disease (IgG4-RD)** and accounts for the large majority of cases (~94% of surgically confirmed AIP). It is defined by elevated serum IgG4, storiform fibrosis, obliterative phlebitis, dense IgG4+ plasma-cell infiltration, and frequent multi-organ (biliary, salivary/lacrimal, renal, retroperitoneal, aortic) involvement. **Type 2 AIP** — idiopathic duct-centric pancreatitis (IDCP) — is IgG4-negative, pancreas-restricted, histologically defined by the neutrophilic granulocytic epithelial lesion (GEL), and associated in ~one-third of cases with inflammatory bowel disease, especially ulcerative colitis. **Type 3 AIP** is a newly recognized, drug-induced entity triggered by immune-checkpoint-inhibitor (ICI) cancer immunotherapy.

Mechanistically, Type 1 AIP is driven by a self-sustaining loop between **oligoclonally expanded CD4+SLAMF7+ cytotoxic T lymphocytes (CTLs)** — which possess both direct cytotoxic and profibrotic properties — and **B-lineage cells/plasmablasts** that present antigen and differentiate into IgG4-secreting plasma cells. An upstream **innate-immunity axis** (neutrophil extracellular traps → plasmacytoid dendritic cells → IFN-α) drives IgG4-class switching and is necessary for disease in the principal MRL/Mp poly(I:C) mouse model. Type 2 AIP is instead neutrophil-centric, and Type 3 (ICI-related) is characterized by acinar-centric T-cell infiltration evolving from CD4+ to CD8+ predominance. Genetic susceptibility is **polygenic/multifactorial** (HLA-DRB1, FCGR2B, CTLA4, FCRL3) rather than Mendelian, and etiology combines genetic predisposition, environmental/occupational triggers (industrial fumes, asbestos), lifestyle factors (smoking), and — for Type 3 — drug exposure.

Clinically, AIP typically presents in **older men** (male:female ≈ 3:1; mean age ~65–68 in Japanese surveys) with **painless obstructive jaundice and weight loss** that mimic pancreatic cancer, making the distinction from malignancy the central diagnostic challenge. Diagnosis follows the **ICDC** or **HISORt** frameworks integrating histology, imaging, serology, other-organ involvement, and steroid response. Prognosis is favorable (~85% 10-year survival) but **Type 1 relapses in ~40%** (rising to ~57% cumulatively at 10 years), whereas Type 2 rarely relapses. First-line therapy is corticosteroids; rituximab and immunomodulators manage refractory/relapsing disease, and the anti-CD19 antibody **inebilizumab became the first FDA-approved therapy for IgG4-RD in 2025** (MITIGATE phase 3). This report synthesizes 20 confirmed findings from 52 reviewed papers into a comprehensive knowledge-base entry.

---

## Section 1 — Disease Information

**Overview.** AIP is a rare, distinct form of chronic pancreatitis characterized by pancreatic inflammation with a fibroinflammatory basis and, in most cases, an autoimmune/immune-mediated pathogenesis and dramatic response to corticosteroids. It represents approximately **2% of chronic pancreatitis cases** ([PMID: 25099388](https://pubmed.ncbi.nlm.nih.gov/25099388/)). The disease is now formally divided into three subtypes ([PMID: 40364113](https://pubmed.ncbi.nlm.nih.gov/40364113/)):

- **AIP-1 / Type 1** — lymphoplasmacytic sclerosing pancreatitis (LPSP); pancreatic manifestation of IgG4-RD
- **AIP-2 / Type 2** — idiopathic duct-centric pancreatitis (IDCP)
- **AIP-3 / Type 3** — immune-checkpoint-inhibitor (ICI)-induced

**Key identifiers.**
- **Mondo:** MONDO:0015175
- **MeSH:** Autoimmune Pancreatitis (D000081012)
- **ICD-11:** DC31 (chronic pancreatitis grouping); commonly coded under K86.1 (ICD-10, other chronic pancreatitis) / K85–K86 pancreatic disease
- **Orphanet:** Autoimmune pancreatitis (classified within IgG4-related disease / AIP)
- **OMIM:** No single Mendelian OMIM entry — AIP is a complex/polygenic disease, not a monogenic disorder

**Synonyms and alternative names.** Lymphoplasmacytic sclerosing pancreatitis (LPSP; Type 1); idiopathic duct-centric pancreatitis (IDCP; Type 2); IgG4-related pancreatitis; sclerosing pancreatitis; non-alcoholic duct-destructive chronic pancreatitis.

**Source of information.** The information in this report is derived predominantly from **aggregated disease-level resources** — nationwide epidemiological surveys (Japan), multicenter cohorts, systematic reviews/meta-analyses, GWAS, mechanistic immunology studies, and a phase 3 randomized trial — supplemented by individual case reports. It is not primarily EHR-derived.

---

## Section 2 — Etiology

**Disease causal factors.** AIP etiology is **multifactorial**, involving a complex interplay of **genetic predisposition, environmental triggers, and dysregulated adaptive immunity** ([PMID: 41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/)). No single Mendelian cause exists. Type 3 is uniquely **drug-induced** (ICIs) ([PMID: 42467391](https://pubmed.ncbi.nlm.nih.gov/42467391/)).

> *"The pathogenesis of IgG4-SC involves a complex interplay of genetic predisposition, environmental triggers (e.g., industrial vapors, dust, gases, fumes, and asbestos), and dysregulated adaptive immunity."* ([PMID: 41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/))

**Genetic risk factors.** A Japanese GWAS of 835 IgG4-RD patients vs 1,789 controls identified two genome-wide-significant susceptibility loci: **HLA-DRB1** and **FCGR2B** ([PMID: 38229354](https://pubmed.ncbi.nlm.nih.gov/38229354/)). Earlier associations include the **HLA DRB1\*0405–DQB1\*0401** haplotype and **FCRL3** (Fc-receptor-like 3) polymorphisms ([PMID: 18341485](https://pubmed.ncbi.nlm.nih.gov/18341485/)). **CTLA4** +6230 G/G increased AIP risk (OR 2.48, p=0.011), and the +49A/A and +6230A/A genotypes increased relapse risk (OR 5.45 and 12.66) with elevated serum soluble CTLA4 (8.9 vs 2.9 ng/mL, p<0.001) ([PMID: 18341485](https://pubmed.ncbi.nlm.nih.gov/18341485/)). Targeted high-throughput sequencing implicated **P2RX3** and **TOP1** (surviving Bonferroni correction) among 11 candidate genes for Type 1 AIP susceptibility ([PMID: 28955865](https://pubmed.ncbi.nlm.nih.gov/28955865/)).

**Environmental risk factors.** Occupational/industrial exposures — **industrial vapors, dust, gases, fumes, and asbestos** — are implicated triggers ([PMID: 41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/)). In an AIP cohort, **blue-collar profession and smoking** were potential risk factors for adverse metabolic outcomes ([PMID: 35807009](https://pubmed.ncbi.nlm.nih.gov/35807009/)). **Older age** and **male sex** are strong demographic risk factors (see Section 9).

**Protective factors.** No well-established genetic protective variants have been defined for AIP. Environmental protective factors are not established. Notably, **serum IgG4 normal at diagnosis or normalized after steroids is protective against relapse** ([PMID: 42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/)), and **corticosteroid maintenance** reduces relapse.

**Gene–environment interactions.** The proposed model is that environmental/innate triggers (e.g., NET-inducing stimuli, industrial exposures) act on a genetically primed immune background (HLA-DRB1, FCGR2B, CTLA4, FCRL3) to unleash the pathogenic CD4+ CTL/plasmablast axis. Molecular mimicry (e.g., *Helicobacter pylori* plasminogen-binding protein homology with human carbonic anhydrase) has been **hypothesized but not proven**.

---

## Section 3 — Phenotypes

**Cardinal presenting phenotypes.** The most common presentation overall is **painless obstructive jaundice with weight loss**, closely mimicking pancreatic cancer ([PMID: 38516247](https://pubmed.ncbi.nlm.nih.gov/38516247/), [PMID: 32234378](https://pubmed.ncbi.nlm.nih.gov/32234378/)).

> *"The clinical manifestations of AIP mainly include painless jaundice and weight loss."* ([PMID: 38516247](https://pubmed.ncbi.nlm.nih.gov/38516247/))

In the 2016 Japan survey, **63% of patients were symptomatic**, roughly half of whom had jaundice ([PMID: 31872350](https://pubmed.ncbi.nlm.nih.gov/31872350/)).

| Phenotype | Type | HPO suggestion | Frequency / Notes |
|---|---|---|---|
| Obstructive jaundice | Clinical sign | HP:0000952 (Jaundice) | ~50% of symptomatic; independent risk factor for diabetes ([PMID: 35807009](https://pubmed.ncbi.nlm.nih.gov/35807009/)) |
| Weight loss | Symptom | HP:0001824 | Common presenting feature ([PMID: 38516247](https://pubmed.ncbi.nlm.nih.gov/38516247/)) |
| Abdominal pain | Symptom | HP:0002027 | Variable; usually mild (contrast with acute pancreatitis) |
| Pancreatic exocrine insufficiency (PEI) | Lab/functional | HP:0001738 | 72.7% at diagnosis, 63.5% at follow-up ([PMID: 35807009](https://pubmed.ncbi.nlm.nih.gov/35807009/)) |
| Diabetes mellitus (endocrine insufficiency) | Lab abnormality | HP:0000819 | Prevalence 32.8% at diagnosis; cumulative incidence 17.9% ([PMID: 35807009](https://pubmed.ncbi.nlm.nih.gov/35807009/)) |
| Elevated serum IgG4 | Lab abnormality | HP:0030355 (Increased circulating IgG level) | 86–88% in Type 1 (Japan surveys) |
| Diffuse pancreatic enlargement ("sausage" pancreas) | Imaging sign | HP:0012093-related | Type 1 typical imaging |
| Sialadenitis / lacrimal gland swelling | Physical manifestation | HP:0000163 / HP:0000509-related | IgG4-RD systemic feature (Type 1) |
| Eosinophilia | Lab abnormality | HP:0001880 | Reported in subset of IgG4-RD ([PMID: 38407323](https://pubmed.ncbi.nlm.nih.gov/38407323/)) |

**Phenotype characteristics.** Onset is **adult/geriatric** (see Section 8). Progression is typically **insidious/chronic** with an **episodic/relapsing** course in Type 1. Severity is variable; most cases respond dramatically to steroids.

> *"PEI prevalence at diagnosis was 72.7% and was 63.5% at follow-up. The cumulative incidence of DM was 17.9%, with a prevalence of DM at diagnosis of 32.8%."* ([PMID: 35807009](https://pubmed.ncbi.nlm.nih.gov/35807009/))

**Quality-of-life impact.** Formal EQ-5D/SF-36/PROMIS data specific to AIP were **not identified**. Functional impact is driven largely by exocrine insufficiency (malabsorption, weight loss), new-onset diabetes, and, in relapsing disease, repeated hospitalizations and cumulative organ damage.

---

## Section 4 — Genetic / Molecular Information

**Causal genes.** AIP is **not monogenic**; there are no causal Mendelian genes. Instead, **susceptibility loci** confer polygenic risk:

| Gene / locus | HGNC | Evidence | Effect |
|---|---|---|---|
| **HLA-DRB1** (esp. DRB1\*0405–DQB1\*0401 haplotype) | HGNC:4948 | GWAS genome-wide significant ([PMID: 38229354](https://pubmed.ncbi.nlm.nih.gov/38229354/)); haplotype association ([PMID: 18341485](https://pubmed.ncbi.nlm.nih.gov/18341485/)) | Antigen presentation susceptibility |
| **FCGR2B** | HGNC:3618 | GWAS genome-wide significant ([PMID: 38229354](https://pubmed.ncbi.nlm.nih.gov/38229354/)) | Inhibitory Fc receptor; B-cell regulation |
| **CTLA4** | HGNC:2505 | +6230 G/G OR 2.48 for risk; relapse OR up to 12.66 ([PMID: 18341485](https://pubmed.ncbi.nlm.nih.gov/18341485/)) | T-cell checkpoint |
| **FCRL3** | HGNC:18506 | Polymorphism association ([PMID: 18341485](https://pubmed.ncbi.nlm.nih.gov/18341485/)) | B-cell regulation |
| **P2RX3, TOP1** | HGNC:8535 / HGNC:11986 | Candidate (Bonferroni-significant) ([PMID: 28955865](https://pubmed.ncbi.nlm.nih.gov/28955865/)) | Susceptibility markers |

> *"Two susceptibility loci for IgG4-related disease were identified. Both FCGR2B and HLA loci might have important roles in IgG4-related disease development."* ([PMID: 38229354](https://pubmed.ncbi.nlm.nih.gov/38229354/))

**Pathogenic variants.** Because AIP is polygenic, ACMG/AMP pathogenicity classification does not apply in the Mendelian sense. Associated variants are **common susceptibility polymorphisms/haplotypes** (e.g., HLA class II alleles, CTLA4 SNPs rs231775 [+49A/G], +6230 A/G) rather than rare pathogenic mutations. These are **germline** in origin. Functional consequence is **immune dysregulation** (altered antigen presentation, impaired T-cell checkpoint/inhibitory-receptor signaling) rather than classic loss/gain of function in a structural protein.

**Autoantigens (molecular targets).** Four candidate autoantigens have been described in IgG4-RD: **annexin A11, galectin-3 (LGALS3), laminin 511-E8, and prohibitin 1** ([PMID: 38332916](https://pubmed.ncbi.nlm.nih.gov/38332916/)). Anti-galectin-3 autoantibodies were detected in **13.5%** of IgG4-related cholangitis patients but not in primary sclerosing cholangitis controls.

> *"Four autoantigens have recently been described in IgG4-RD: annexin A11, galectin-3, laminin 511-E8, and prohibitin 1."* ([PMID: 38332916](https://pubmed.ncbi.nlm.nih.gov/38332916/))

**Modifier genes.** CTLA4 genotypes modify **relapse risk** (+49A/A OR 5.45; +6230A/A OR 12.66) ([PMID: 18341485](https://pubmed.ncbi.nlm.nih.gov/18341485/)). Candidate relapse-modifying variants (HLA-C, CXCR3, CACNA1C) were reported by targeted sequencing ([PMID: 28955865](https://pubmed.ncbi.nlm.nih.gov/28955865/)).

**Epigenetic information & chromosomal abnormalities.** No established disease-specific DNA methylation, histone-modification, or chromosomal-abnormality signatures for AIP were identified. This is a **knowledge gap**.

---

## Section 5 — Environmental Information

**Environmental factors.** Industrial/occupational exposures — **industrial vapors, dust, gases, fumes, and asbestos** — are implicated as triggers of IgG4-RD/AIP ([PMID: 41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/)). **Blue-collar occupation** was associated with adverse metabolic outcomes ([PMID: 35807009](https://pubmed.ncbi.nlm.nih.gov/35807009/)).

**Lifestyle factors.** **Smoking** is the best-supported lifestyle risk factor, identified as a potential contributor to diabetes/exocrine-insufficiency outcomes in AIP ([PMID: 35807009](https://pubmed.ncbi.nlm.nih.gov/35807009/)) and a recognized risk factor for chronic pancreatitis more broadly.

**Infectious agents.** **No single infectious agent has been established as causal.** Molecular mimicry involving *Helicobacter pylori* plasminogen-binding protein (homology with human carbonic anhydrase II / ubiquitin-protein ligase) has been hypothesized but **not proven**. AIP is not a transmissible/zoonotic disease.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (Type 1 AIP / IgG4-RD)

```
1. Genetic priming (HLA-DRB1, FCGR2B, CTLA4, FCRL3 risk alleles)
        + environmental/innate trigger
   → leads to →
2. Innate activation: tissue stimulus induces NEUTROPHIL EXTRACELLULAR TRAPS (NETs)
   → NETs stimulate →
3. PLASMACYTOID DENDRITIC CELLS (pDCs) accumulate in pancreas and produce IFN-α
   [NECESSARY step: pDC depletion / IFN-α blockade prevents AIP in mouse model]
   → IFN-α (with BAFF) drives →
4. B-CELL activation & IgG4-CLASS SWITCHING → oligoclonal expansion of IgG4+ PLASMABLASTS/plasma cells
   → plasmablasts present antigen to →
5. CD4+SLAMF7+ CYTOTOXIC T LYMPHOCYTES (CTLs) — oligoclonally expanded — infiltrate lesions
   [self-sustaining loop: CTLs ↔ plasmablasts via continuous antigen presentation]
   → CD4+ CTLs exert DUAL effects →
        (a) direct cytotoxicity → acinar/epithelial cell death (TISSUE DAMAGE)
        (b) secretion of profibrotic factors (e.g., TGF-β) → activate fibroblasts
   → results in →
6. STORIFORM FIBROSIS + OBLITERATIVE PHLEBITIS + dense lymphoplasmacytic infiltrate
   → produces →
7. Mass-forming pancreatic enlargement, ductal narrowing → OBSTRUCTIVE JAUNDICE,
   exocrine & endocrine insufficiency (CLINICAL MANIFESTATION)
```

**Branch — Type 2 AIP (IDCP):** IgG4-independent; **neutrophil-mediated granulocytic epithelial lesions (GEL)** destroy duct epithelium → pancreas-restricted duct-centric inflammation (frequently co-occurring with IBD).

**Branch — Type 3 AIP (ICI-related):** ICI blockade of PD-1/PD-L1/CTLA-4 removes T-cell checkpoint restraint → **acinar-centric T-cell infiltration evolving from CD4+ to CD8+ predominance** → often asymptomatic hyperlipasemia, with pancreatic atrophy/diabetes as sequelae ([PMID: 41922528](https://pubmed.ncbi.nlm.nih.gov/41922528/)).

### Detail by category

**Immune system involvement — the core mechanism.** The traditional Th2 (IL-4/IL-10) paradigm is now considered insufficient to explain tissue destruction and fibrosis. Instead, **oligoclonally expanded CD4+ cytotoxic T lymphocytes (CTLs)** bearing **SLAMF7** are the central effectors, with dual cytotoxic and profibrotic properties ([PMID: 41766862](https://pubmed.ncbi.nlm.nih.gov/41766862/)):

> *"Emerging data highlight the extensive, oligoclonally expanded infiltration of CD4+ cytotoxic T lymphocytes (CTLs) deep within lesions. These cells possess dual cytotoxic and profibrotic properties."* ([PMID: 41766862](https://pubmed.ncbi.nlm.nih.gov/41766862/))

These CTLs are sustained by **continuous antigen presentation by B-lineage cells, particularly plasmablasts** ([PMID: 27667138](https://pubmed.ncbi.nlm.nih.gov/27667138/)), explaining why B-cell depletion (rituximab, inebilizumab) is effective. The CD4+SLAMF7+ population expands in patients and **decreases after glucocorticoid treatment** ([PMID: 29499100](https://pubmed.ncbi.nlm.nih.gov/29499100/)). A distinctive CD4+ response dominated by **Th2, T-follicular-helper (Tfh), and regulatory T cells (Tregs)** drives B-cell activation and IgG4+ plasmablast expansion ([PMID: 41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/)). M2 macrophages also contribute ([PMID: 35737955](https://pubmed.ncbi.nlm.nih.gov/35737955/)).

> *"A distinctive CD4+ T-cell response, dominated by T-helper 2 (Th2), follicular helper T (Tfh) cells, and regulatory T cells (Tregs), drives B-cell activation, oligoclonal expansion of IgG4+ plasmablasts, and progressive fibrosis."* ([PMID: 41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/))

**Innate immunity (upstream trigger).** In the MRL/Mp mouse, disease develops in parallel with pancreatic accumulation of **IFN-α-producing plasmacytoid dendritic cells (pDCs)**; pDC depletion and IFN-α blockade **prevent AIP**, proving necessity ([PMID: 26297761](https://pubmed.ncbi.nlm.nih.gov/26297761/)). **Neutrophil extracellular traps (NETs)** stimulate pDCs to make IFN-α; human patient pDCs cultured with NETs produced greatly increased IFN-α and induced B cells to make **IgG4 (but not IgG1)** ([PMID: 26297761](https://pubmed.ncbi.nlm.nih.gov/26297761/)). **SLAMF7 on CD8+ T cells** is also increased in AIP ([PMID: 37661465](https://pubmed.ncbi.nlm.nih.gov/37661465/)).

> *"patient pDCs cultured in the presence of NETs produced greatly increased levels of IFN-α and induced control B cells to produce IgG4 (but not IgG1)"* ([PMID: 26297761](https://pubmed.ncbi.nlm.nih.gov/26297761/))

**Cellular processes.** Chronic inflammation, epithelial/acinar apoptosis and cytotoxic killing, fibroblast activation, and progressive fibrosis.

**Tissue-damage mechanisms.** Fibrosis (storiform pattern), obliterative phlebitis, lymphoplasmacytic destruction. In Type 2, neutrophilic duct destruction (GEL). Reduced ductal **CFTR** expression contributes to acinar dysfunction; CFTR correctors (C18) rescued function and reduced inflammation in mice ([PMID: 28634110](https://pubmed.ncbi.nlm.nih.gov/28634110/)).

**Molecular profiling.** Circulating **plasmablast expansion** is a robust cellular biomarker (see Section 10). Cytokine signatures (IFN-γ, IL-10, IL-13, IL-5, IL-21) correlate with disease activity ([PMID: 42277154](https://pubmed.ncbi.nlm.nih.gov/42277154/)).

**Suggested ontology terms.** GO:0002250 (adaptive immune response), GO:0001909 (leukocyte-mediated cytotoxicity), GO:0030198 (extracellular matrix organization / fibrosis), GO:0006954 (inflammatory response), GO:0032606 (type I interferon production). Cell types: CL:0000625 (CD8-positive cytotoxic T cell), CL:0000624 (CD4-positive T cell), CL:0000980 (plasmablast), CL:0000784 (plasmacytoid dendritic cell), CL:0000775 (neutrophil), CL:0000890 (M2 macrophage).

---

## Section 7 — Anatomical Structures Affected

**Primary organ.** The **pancreas** (UBERON:0001264) is the primary affected organ in all subtypes.

**Secondary/systemic involvement (Type 1 / IgG4-RD).** IgG4-RD is a systemic mass-forming fibroinflammatory condition affecting nearly every organ ([PMID: 26672716](https://pubmed.ncbi.nlm.nih.gov/26672716/)):

> *"The organs most frequently involved are the pancreas (autoimmune pancreatitis (AIP), salivary and lacrimal glands (Mickulicz disease and sclerosing sialadenitis), biliary tree (sclerosing cholangitis or cholecystitis), retroperitoneum (retroperitoneal fibrosis), aorta (periaortic fibrosis), kidneys (interstitial nephritis) and thyroid (Riedel thyroiditis)."* ([PMID: 26672716](https://pubmed.ncbi.nlm.nih.gov/26672716/))

| Structure | UBERON | Manifestation |
|---|---|---|
| Pancreas | UBERON:0001264 | AIP (primary) |
| Bile ducts / biliary tree | UBERON:0002394 | IgG4-related sclerosing cholangitis |
| Salivary glands | UBERON:0001044 | Sclerosing sialadenitis (Mikulicz) |
| Lacrimal glands | UBERON:0001817 | Dacryoadenitis |
| Kidney | UBERON:0002113 | Tubulointerstitial nephritis |
| Retroperitoneum | UBERON:0003693 | Retroperitoneal fibrosis |
| Aorta | UBERON:0000947 | Periaortitis |
| Thyroid | UBERON:0002046 | Riedel thyroiditis |

Extrapancreatic lesions were detected in **60% of AIP patients** in the 2016 Japan survey ([PMID: 31872350](https://pubmed.ncbi.nlm.nih.gov/31872350/)). **Type 2 AIP is pancreas-restricted** (except rare IBD/sialadenitis) ([PMID: 34670874](https://pubmed.ncbi.nlm.nih.gov/34670874/), [PMID: 32825945](https://pubmed.ncbi.nlm.nih.gov/32825945/)).

**Tissue/cell level.** Pancreatic **ductal and acinar epithelium** (targets), with infiltration by plasma cells, plasmablasts, CD4+/CD8+ T cells, pDCs, neutrophils (Type 2), and M2 macrophages. **Subcellular:** ER (secretory pathway of plasma cells) and ductal apical membrane (CFTR). **Body system:** digestive/endocrine.

**Localization / lateralization.** The pancreas can be diffusely enlarged ("sausage" pancreas, Type 1) or focally involved (mimicking cancer). Not a lateralized organ; involvement is described as diffuse vs focal/segmental.

---

## Section 8 — Temporal Development

**Onset.** **Adult to geriatric.** Mean age at diagnosis ~64.8 years (2016 Japan survey; mean age 68.1) ([PMID: 31872350](https://pubmed.ncbi.nlm.nih.gov/31872350/)); ~59–66 in other cohorts. Onset pattern is **insidious/chronic/subacute**, frequently presenting as painless jaundice. Type 2 tends to occur in somewhat younger patients than Type 1.

**Progression.** Type 1 follows a **relapsing-remitting** course. Cumulative relapse rates in a 10-year Type 1 cohort were **11.0% / 26.9% / 38.3% / 50.0% / 56.9% at 1/3/5/7/10 years** ([PMID: 42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/)):

> *"Cumulative relapse rates at 1, 3, 5, 7, and 10 years were 11.0%, 26.9%, 38.3%, 50.0%, and 56.9%."* ([PMID: 42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/))

Progression is generally **slow**; end-stage disease features pancreatic atrophy, exocrine insufficiency, and diabetes.

**Patterns.** Remission is typically **treatment-induced** (corticosteroids). Type 2 AIP relapse is uncommon (favorable). Corticosteroid **discontinuation independently predicts relapse**, while normal/normalized serum IgG4 is protective ([PMID: 42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/)). Critical intervention window: early steroid therapy induces remission and prevents irreversible fibrotic damage.

---

## Section 9 — Inheritance and Population

**Epidemiology (Japan nationwide surveys — the best-characterized data):**

| Year | Prevalence /100,000 | Incidence /100,000/yr | M:F | Mean age | High serum IgG4 |
|---|---|---|---|---|---|
| 2007 ([PMID: 22466167](https://pubmed.ncbi.nlm.nih.gov/22466167/)) | 2.2 | 0.9 | 3.7 | 63.0 | 87.6% |
| 2011 ([PMID: 25815647](https://pubmed.ncbi.nlm.nih.gov/25815647/)) | 4.6 | 1.4 | 3.2 | 66.3 | 86.4% |
| 2016 ([PMID: 31872350](https://pubmed.ncbi.nlm.nih.gov/31872350/)) | 10.1 | 3.1 | 2.94 | 68.1 | — |

> *"The estimated number of AIP patients in 2016 was 13,436, with an overall prevalence rate of 10.1 per 100,000 persons. The estimated number of newly diagnosed patients was 3984, with an annual incidence rate of 3.1 per 100,000 persons."* ([PMID: 31872350](https://pubmed.ncbi.nlm.nih.gov/31872350/))

Prevalence **more than doubled from 2011 to 2016**, reflecting rising recognition. AIP accounts for ~2% of chronic pancreatitis ([PMID: 25099388](https://pubmed.ncbi.nlm.nih.gov/25099388/)).

**Inheritance pattern.** **Multifactorial / polygenic** — NOT Mendelian. No AD/AR/X-linked/mitochondrial inheritance. Penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, and carrier frequency are **not applicable** in the classical genetic sense.

**Demographics.** **Strong male predominance** (M:F ~3:1), **elderly onset** (Type 1). Subtype distribution among surgically confirmed AIP: **Type 1 ~94%, Type 2 ~6%** ([PMID: 39169289](https://pubmed.ncbi.nlm.nih.gov/39169289/)) — though Type 2 is relatively more common in Western/younger/IBD populations. Type 1 is more prevalent in East Asia; Type 2 is proportionally more common in Europe/North America.

> *"The male-to-female sex ratio was 2.94, the mean age was 68.1, and mean age at diagnosis was 64.8."* ([PMID: 31872350](https://pubmed.ncbi.nlm.nih.gov/31872350/))

---

## Section 10 — Diagnostics

**Diagnostic frameworks.** Diagnosis is established by the **International Consensus Diagnostic Criteria (ICDC)** or **HISORt** (Histology, Imaging, Serology, Other organ involvement, Response to therapy) ([PMID: 25099388](https://pubmed.ncbi.nlm.nih.gov/25099388/)), and the Japan Pancreas Society (JPS) criteria ([PMID: 40996454](https://pubmed.ncbi.nlm.nih.gov/40996454/)).

> *"Diagnosis of AIP is established according to the international consensus diagnostic criteria (ICDC) or HISORt (mnemonic standing for histology, imaging, serology, other organ involvement and response to therapy) criteria."* ([PMID: 25099388](https://pubmed.ncbi.nlm.nih.gov/25099388/))

In **Type 1**, typical imaging changes can suffice even with negative histology; in **Type 2**, histologic evidence (GEL) is required ([PMID: 37947862](https://pubmed.ncbi.nlm.nih.gov/37947862/)).

> *"In type 1 AIP, typical imaging changes are sufficient to establish the diagnosis even with negative histology, whereas for type 2 AIP, histologic evidence is required."* ([PMID: 37947862](https://pubmed.ncbi.nlm.nih.gov/37947862/))

**Serology / biomarkers.**
- **Serum IgG4:** >2× ULN suggestive, **>4× ULN highly specific**; **IgG4/IgG1 ratio >0.24** is discriminatory ([PMID: 41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/)). However, sensitivity is limited — ~13–16% of patients have normal serum IgG4, and in surgical series Type 1 sensitivity can be ~43% ([PMID: 24817416](https://pubmed.ncbi.nlm.nih.gov/24817416/), [PMID: 39169289](https://pubmed.ncbi.nlm.nih.gov/39169289/)).
- **Circulating plasmablasts:** a robust IgG4-independent biomarker — markedly elevated (median 4,698/mL vs 592/mL untreated disease controls, 94/mL healthy; p<0.001); **36% of IgG4-RD patients with NORMAL serum IgG4 still had elevated plasmablasts**; levels fall with rituximab and rise at flare ([PMID: 24817416](https://pubmed.ncbi.nlm.nih.gov/24817416/)).

> *"The IgG4-RD patients had substantially elevated total plasmablast counts (median 4698/mL, range 610-79524/mL) compared to both untreated disease controls (median 592/mL, range 19-4294/mL; p < 0.001) and healthy controls (median 94/mL, range 1-653/mL; p < 0.001)."* ([PMID: 24817416](https://pubmed.ncbi.nlm.nih.gov/24817416/))

- **Type 2 has no established serum marker** — diagnosis requires histologic GEL ([PMID: 34670874](https://pubmed.ncbi.nlm.nih.gov/34670874/)).

> *"Since there are currently no established serum markers, the diagnosis of type 2 AIP is highly challenging and requires the tissue confirmation of neutrophilic injury to the pancreatic ducts, a finding designated as a granulocytic epithelial lesion."* ([PMID: 34670874](https://pubmed.ncbi.nlm.nih.gov/34670874/))

**Imaging.** Diffuse pancreatic enlargement ("sausage" pancreas) with delayed/rim enhancement and narrowed main pancreatic duct (Type 1). **18F-FDG PET/CT** aids diagnosis, staging of systemic involvement, and treatment monitoring ([PMID: 26672716](https://pubmed.ncbi.nlm.nih.gov/26672716/)). **Endoscopic ultrasound (EUS)** with EUS-guided core biopsy is the main modality for tissue sampling and for differentiating AIP from cancer ([PMID: 40996454](https://pubmed.ncbi.nlm.nih.gov/40996454/)).

**Histopathology.** Type 1: storiform fibrosis, obliterative phlebitis, dense lymphoplasmacytic infiltrate rich in IgG4+ plasma cells ([PMID: 28747608](https://pubmed.ncbi.nlm.nih.gov/28747608/)). Type 2: granulocytic epithelial lesion (GEL) — neutrophilic duct epithelial injury ([PMID: 34670874](https://pubmed.ncbi.nlm.nih.gov/34670874/)).

**Differential diagnosis.** The critical differential is **pancreatic ductal adenocarcinoma**; also cholangiocarcinoma, primary sclerosing cholangitis, and other chronic pancreatitis ([PMID: 40996454](https://pubmed.ncbi.nlm.nih.gov/40996454/), [PMID: 40191403](https://pubmed.ncbi.nlm.nih.gov/40191403/)).

**Genetic testing.** Not part of routine diagnosis (polygenic disease). HLA/CTLA4 genotyping is research-only.

---

## Section 11 — Outcome / Prognosis

**Survival.** Favorable. **10-year overall survival 85.5%** in a corticosteroid-treated Type 1 cohort; corticosteroid maintenance associated with better survival ([PMID: 42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/)).

**Relapse (key prognostic issue).** Type 1 relapses in **~40–42%** ([PMID: 40773035](https://pubmed.ncbi.nlm.nih.gov/40773035/), [PMID: 41223493](https://pubmed.ncbi.nlm.nih.gov/41223493/)); cumulative ~57% at 10 years ([PMID: 42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/)). **Type 2 relapse is uncommon** ([PMID: 37826920](https://pubmed.ncbi.nlm.nih.gov/37826920/)).

> *"AIP primarily consists of type 1 and type 2, with relapse being a significant problem mainly associated with type 1 AIP, which has a high relapse rate of approximately 40%, whereas type 2 AIP has significantly lower relapse rates."* ([PMID: 40773035](https://pubmed.ncbi.nlm.nih.gov/40773035/))

**Prognostic factors for relapse:** younger age (<60 y; OR 1.7, 95% CI 1.1–2.7, p=0.022) ([PMID: 41223493](https://pubmed.ncbi.nlm.nih.gov/41223493/)); persistent/insufficiently declining serum IgG4, diffuse pancreatic swelling, proximal biliary/renal involvement ([PMID: 40773035](https://pubmed.ncbi.nlm.nih.gov/40773035/)); corticosteroid discontinuation ([PMID: 42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/)).

> *"The overall relapse rate was 41.9 %, being higher in the <60 years group (46.2 %) than in the ≥60 years group (37.0 %). Age <60 years was significantly associated with increased relapse risk (OR = 1.7; 95 % CI: 1.1-2.7, P = 0.022)."* ([PMID: 41223493](https://pubmed.ncbi.nlm.nih.gov/41223493/))

**Morbidity/complications.** Exocrine insufficiency (up to 72.7%), diabetes (~33% prevalence), biliary strictures, and progressive fibrosis. HbA1c worsened and serum albumin declined (mean −0.27 g/dL) by 10 years ([PMID: 42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/)).

**Malignancy risk.** Overall malignancy risk **not increased** (SIR 1.00, 95% CI 0.59–1.42), but **pancreatic cancer SIR numerically higher (1.98 overall; 2.96 at ≥5 years)** ([PMID: 42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/)). A nationwide Swedish study found autoimmune diseases collectively raise pancreatic-cancer risk (SIR 1.24 men, 1.19 women) ([PMID: 41795138](https://pubmed.ncbi.nlm.nih.gov/41795138/)).

> *"Overall malignancy risk was not increased (SIR 1.00; 95%CI 0.59-1.42), while pancreatic cancer (PC) showed a numerically higher SIR (1.98 overall; 2.96 ≥ 5 years postdiagnosis)."* ([PMID: 42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/))

---

## Section 12 — Treatment

**First-line: corticosteroids.** Oral corticosteroids are the standard first-line therapy, effective in the majority (NCIT: Corticosteroid Therapy) ([PMID: 36293522](https://pubmed.ncbi.nlm.nih.gov/36293522/), [PMID: 38516247](https://pubmed.ncbi.nlm.nih.gov/38516247/)). Prolonged **maintenance glucocorticoid** reduces relapse ([PMID: 40773035](https://pubmed.ncbi.nlm.nih.gov/40773035/)).

> *"The standard therapy for AIP is oral administration of corticosteroids. Rituximab (RTX) has also been proposed for induction of remission and maintenance therapy in relapsing AIP-1."* ([PMID: 36293522](https://pubmed.ncbi.nlm.nih.gov/36293522/))

**B-cell-targeted / immunomodulatory (relapsing/refractory disease).**
- **Rituximab** (anti-CD20; NCIT:C1702) — induction and maintenance in relapsing AIP-1 ([PMID: 36293522](https://pubmed.ncbi.nlm.nih.gov/36293522/)).
- Steroid-sparing immunomodulators: **azathioprine, methotrexate, mycophenolate mofetil** (off-label) ([PMID: 40745228](https://pubmed.ncbi.nlm.nih.gov/40745228/)).

**Inebilizumab (anti-CD19) — first FDA-approved therapy for IgG4-RD (2025).** The phase 3 **MITIGATE** trial (n=135) showed inebilizumab significantly reduced recurrence (**10% vs 60% placebo**), annual exacerbation rate, and glucocorticoid need; serum IgG4 fell ~50% with persistent B-cell depletion over 52 weeks; more infections/lymphopenia but no treatment-associated deaths ([PMID: 40745228](https://pubmed.ncbi.nlm.nih.gov/40745228/)).

> *"The treatment significantly reduced the risk of recurrence (10% vs. 60% under placebo), the annual exacerbation rate and the necessity for renewed administration of glucocorticoids."* ([PMID: 40745228](https://pubmed.ncbi.nlm.nih.gov/40745228/))

> *"Following approval of inebilizumab by the U.S. Food and Drug Administration (FDA) for IgG4-RD in 2025"* ([PMID: 40745228](https://pubmed.ncbi.nlm.nih.gov/40745228/))

**Type 2 AIP.** Responds well to glucocorticoids; **anti-TNF-α antibodies** are a promising alternative ([PMID: 37826920](https://pubmed.ncbi.nlm.nih.gov/37826920/)).

> *"Patients with AIP-2 respond well to glucocorticoids, with anti-tumor necrosis factor-alpha antibodies as a promising alternative therapy."* ([PMID: 37826920](https://pubmed.ncbi.nlm.nih.gov/37826920/))

**Type 3 (ICI-related).** Corticosteroid role controversial; management guidelines not established; ICI cessation and supportive care are used ([PMID: 41922528](https://pubmed.ncbi.nlm.nih.gov/41922528/)).

**Experimental targeted agents (under evaluation).** Anti-SLAMF7 (elotuzumab), obexelimab (CD19), BTK inhibitors, JAK/STAT inhibitors, and T2-inflammation biologics ([PMID: 37858433](https://pubmed.ncbi.nlm.nih.gov/37858433/)). Targeting the **plasmablast–B-cell lineage and CD4+SLAMF7+ CTL** axis is the most promising future direction ([PMID: 35737955](https://pubmed.ncbi.nlm.nih.gov/35737955/)).

**Supportive care.** Pancreatic enzyme replacement (exocrine insufficiency), insulin/oral agents (diabetes), biliary stenting (obstructive jaundice).

**Pharmacogenomics.** CTLA4 genotypes modulate relapse risk ([PMID: 18341485](https://pubmed.ncbi.nlm.nih.gov/18341485/)); no validated genotype-guided dosing protocol exists yet.

---

## Section 13 — Prevention

**Primary prevention.** No established primary prevention (etiology is multifactorial/idiopathic). Modifiable risk-factor reduction (smoking cessation; avoiding industrial exposures) is reasonable but unproven. For **Type 3**, awareness of ICI risk allows monitoring but not avoidance without foregoing cancer therapy.

**Secondary prevention (early detection).** Vigilant differentiation of AIP from pancreatic cancer to avoid unnecessary resection ([PMID: 40191403](https://pubmed.ncbi.nlm.nih.gov/40191403/)); serial serum IgG4 and imaging for early relapse detection.

**Tertiary prevention (complication prevention).** **Corticosteroid maintenance** to prevent relapse and irreversible fibrotic organ damage ([PMID: 40773035](https://pubmed.ncbi.nlm.nih.gov/40773035/), [PMID: 42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/)); long-term surveillance with labs, imaging (MRCP/EUS), and endoscopy for biliary strictures ([PMID: 40191403](https://pubmed.ncbi.nlm.nih.gov/40191403/)); monitoring for exocrine/endocrine insufficiency and pancreatic cancer.

**Immunization, genetic screening, counseling.** Not applicable (non-infectious, polygenic disease). No carrier/prenatal screening.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy:** Human (NCBI:txid9606) is the disease context. Experimental disease is induced in **mouse** (NCBI:txid10090).
- **Naturally occurring animal disease:** No well-established naturally occurring analog of human AIP in companion animals or wildlife was identified in the reviewed literature. (Lymphoplasmacytic/immune-mediated pancreatitis exists in dogs but is not established as an AIP ortholog.) — **Knowledge gap.**
- **Orthologous genes:** CTLA4, FCGR2B, and HLA (H2 in mouse) have murine orthologs used in models.
- **Zoonotic potential:** None — AIP is non-transmissible.

---

## Section 15 — Model Organisms

**Principal model: MRL/Mp mouse + poly(I:C).** Autoimmune-prone MRL/Mp mice given repeated intraperitoneal **polyinosinic–polycytidylic acid [poly(I:C)]** develop experimental AIP with massive pancreatic architecture destruction, immune infiltration, fibrosis, multi-organ involvement, and elevated autoantibodies resembling human IgG4-RD ([PMID: 29512140](https://pubmed.ncbi.nlm.nih.gov/29512140/)).

> *"autoimmune-prone MRL/Mp mice treated with repeated injection with polyinosinic-polycytidylic acid (poly (I:C)) provide an experimental model of AIP. These mice exhibit massive destruction of pancreatic architecture associated with pancreatic immune cell infiltration and fibrosis."* ([PMID: 29512140](https://pubmed.ncbi.nlm.nih.gov/29512140/))

**Key limitation.** *"Although mice lack the IgG4 Ab subtype"* ([PMID: 29512140](https://pubmed.ncbi.nlm.nih.gov/29512140/)) — mice cannot recapitulate the defining IgG4 serology/plasma-cell feature, limiting translational fidelity for the IgG4 axis.

**Other models.** **NOD/ShiLTJ** mice and **BMP6-transduced** mice model Sjögren's/chronic pancreatitis; MRL/Mp models AIP with markedly reduced ductal **CFTR** expression — CFTR correctors (C18) rescued function and reduced inflammation ([PMID: 28634110](https://pubmed.ncbi.nlm.nih.gov/28634110/)).

**Applications.** These models established the **NET → pDC → IFN-α → IgG4** innate axis ([PMID: 26297761](https://pubmed.ncbi.nlm.nih.gov/26297761/)), the role of **SLAMF7+ CD8 T cells** ([PMID: 37661465](https://pubmed.ncbi.nlm.nih.gov/37661465/)), and the therapeutic potential of CFTR correction and steroid response.

**Resources:** MGI (mouse); model strains MRL/MpJ, NOD/ShiLTJ.

---

## Mechanistic Model / Interpretation

The synthesized model positions Type 1 AIP as a **two-compartment autoimmune loop** ignited by innate immunity:

```
 INNATE IGNITION                ADAPTIVE AMPLIFICATION            EFFECTOR / DAMAGE
 ┌────────────────┐            ┌───────────────────────┐         ┌────────────────────┐
 │ Trigger + NETs │──IFN-α──▶  │ pDC → B-cell IgG4      │◀──────▶ │ CD4+SLAMF7+ CTL     │
 │ (genetic prime)│            │ class switch →         │  antigen│  • cytotoxicity     │
 └────────────────┘            │ IgG4+ plasmablasts     │ present │  • profibrotic TGF-β│
                               └───────────────────────┘         └─────────┬──────────┘
                                        ▲   B-cell depletion                │
                                        │   (rituximab / inebilizumab)      ▼
                                        └───────────────────────────  STORIFORM FIBROSIS +
                                                                       OBLITERATIVE PHLEBITIS
                                                                       → jaundice, PEI, DM
```

Two therapeutic insights follow directly from this architecture. First, because CD4+ CTLs are **sustained by plasmablast antigen presentation**, depleting the B-cell/plasmablast compartment collapses the entire loop — explaining why **rituximab** and now **inebilizumab** (anti-CD19, which reaches later B-lineage stages including plasmablasts) are effective. Second, the **innate IFN-α axis** offers an upstream target not yet exploited clinically. Type 2 and Type 3 are mechanistically distinct — neutrophil-driven and checkpoint-release T-cell-driven, respectively — and therefore require different management, underscoring why accurate subtyping is clinically essential.

---

## Evidence Base

| Domain | Key PMIDs | Contribution |
|---|---|---|
| Subtype definition & frequency | [39169289](https://pubmed.ncbi.nlm.nih.gov/39169289/), [38516247](https://pubmed.ncbi.nlm.nih.gov/38516247/), [40364113](https://pubmed.ncbi.nlm.nih.gov/40364113/) | Established Type 1/2/3 taxonomy and 94%/6% split |
| Core immune mechanism | [41766862](https://pubmed.ncbi.nlm.nih.gov/41766862/), [27667138](https://pubmed.ncbi.nlm.nih.gov/27667138/), [29499100](https://pubmed.ncbi.nlm.nih.gov/29499100/), [28747608](https://pubmed.ncbi.nlm.nih.gov/28747608/) | CD4+SLAMF7+ CTL / plasmablast loop; histopathology |
| Innate trigger | [26297761](https://pubmed.ncbi.nlm.nih.gov/26297761/), [29512140](https://pubmed.ncbi.nlm.nih.gov/29512140/) | NET→pDC→IFN-α axis; mouse model |
| Genetics | [38229354](https://pubmed.ncbi.nlm.nih.gov/38229354/), [18341485](https://pubmed.ncbi.nlm.nih.gov/18341485/), [28955865](https://pubmed.ncbi.nlm.nih.gov/28955865/) | HLA-DRB1, FCGR2B, CTLA4, FCRL3 |
| Autoantigens | [38332916](https://pubmed.ncbi.nlm.nih.gov/38332916/) | Annexin A11, galectin-3, laminin 511-E8, prohibitin 1 |
| Epidemiology | [31872350](https://pubmed.ncbi.nlm.nih.gov/31872350/), [25815647](https://pubmed.ncbi.nlm.nih.gov/25815647/), [22466167](https://pubmed.ncbi.nlm.nih.gov/22466167/) | Prevalence/incidence trends (Japan) |
| Diagnosis / biomarkers | [25099388](https://pubmed.ncbi.nlm.nih.gov/25099388/), [37947862](https://pubmed.ncbi.nlm.nih.gov/37947862/), [24817416](https://pubmed.ncbi.nlm.nih.gov/24817416/), [41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/), [40996454](https://pubmed.ncbi.nlm.nih.gov/40996454/) | ICDC/HISORt; IgG4 thresholds; plasmablasts |
| Prognosis / relapse | [40773035](https://pubmed.ncbi.nlm.nih.gov/40773035/), [41223493](https://pubmed.ncbi.nlm.nih.gov/41223493/), [42185503](https://pubmed.ncbi.nlm.nih.gov/42185503/) | 40% relapse; 85.5% 10-yr survival; PC risk |
| Treatment | [36293522](https://pubmed.ncbi.nlm.nih.gov/36293522/), [40745228](https://pubmed.ncbi.nlm.nih.gov/40745228/), [37826920](https://pubmed.ncbi.nlm.nih.gov/37826920/) | Steroids, rituximab, inebilizumab (MITIGATE), anti-TNF |
| Type 2 | [34670874](https://pubmed.ncbi.nlm.nih.gov/34670874/), [37826920](https://pubmed.ncbi.nlm.nih.gov/37826920/), [32825945](https://pubmed.ncbi.nlm.nih.gov/32825945/) | GEL, IBD association, favorable prognosis |
| Type 3 (ICI) | [42467391](https://pubmed.ncbi.nlm.nih.gov/42467391/), [41922528](https://pubmed.ncbi.nlm.nih.gov/41922528/) | Definition, incidence 0.5–5.7%, CD4→CD8 histology |
| Systemic / anatomy | [26672716](https://pubmed.ncbi.nlm.nih.gov/26672716/), [32234378](https://pubmed.ncbi.nlm.nih.gov/32234378/), [40191403](https://pubmed.ncbi.nlm.nih.gov/40191403/) | Multi-organ IgG4-RD; biliary involvement |
| Clinical phenotype | [35807009](https://pubmed.ncbi.nlm.nih.gov/35807009/) | Exocrine (72.7%)/endocrine (32.8%) insufficiency |

The evidence base is internally consistent: mechanistic (mouse/in-vitro), genetic (GWAS), epidemiological (nationwide surveys), and therapeutic (phase 3 RCT) lines converge on a B-cell/plasmablast–CD4+ CTL model of Type 1 AIP, validated therapeutically by the success of B-cell depletion.

---

## Limitations and Knowledge Gaps

1. **Epidemiology is Japan-centric.** The best prevalence/incidence data derive from Japanese nationwide surveys; Western/global incidence, and true Type 2 proportion outside Asia, are less precisely quantified.
2. **No monogenic cause / no ClinVar pathogenic variants.** AIP is polygenic; standard ACMG variant classification, penetrance, and carrier-frequency concepts do not apply. Epigenetic and chromosomal data are essentially absent.
3. **Autoantigen causality unproven.** The four candidate autoantigens (annexin A11, galectin-3, laminin 511-E8, prohibitin 1) are associations; a single dominant, disease-driving autoantigen has not been definitively established.
4. **Serum IgG4 imperfect.** ~13–16% of patients are seronegative; specificity is limited, and it correlates inconsistently with activity in fibrotic/localized subsets ([PMID: 42277154](https://pubmed.ncbi.nlm.nih.gov/42277154/)).
5. **Mouse model lacks IgG4.** The MRL/Mp poly(I:C) model cannot recapitulate the defining IgG4 serology.
6. **Type 3 evidence is thin.** AIP-3 rests on small retrospective series with no consensus diagnostic/management guidelines.
7. **QoL data absent.** No AIP-specific EQ-5D/SF-36/PROMIS data were identified.
8. **Inebilizumab is new.** Long-term (>52-week) safety/efficacy and comparative data vs rituximab are not yet available.

---

## Proposed Follow-up Experiments / Actions

1. **Validate circulating plasmablasts + IgG4/IgG1 ratio as a combined diagnostic/monitoring panel** in a prospective multi-ethnic cohort, particularly to capture IgG4-seronegative patients.
2. **Single-cell / spatial transcriptomics of AIP pancreatic tissue** to map the CD4+SLAMF7+ CTL–plasmablast niche and identify upstream antigen-presenting cell states (fills the "which autoantigen" gap).
3. **Test upstream innate blockade** (anti-IFN-α / anti-type-I-IFN receptor, or NET inhibitors) in the MRL/Mp model as a steroid-sparing strategy, given the demonstrated necessity of the pDC/IFN-α axis.
4. **Head-to-head or registry comparison of inebilizumab vs rituximab** for relapse prevention, with cost, infection risk, and durability endpoints.
5. **Establish international Type 2 and Type 3 registries** with standardized histologic/GEL and ICI-exposure criteria to define incidence, natural history, and management.
6. **Prospective pancreatic-cancer surveillance study** in Type 1 AIP (≥5-year follow-up) to confirm/quantify the numerically elevated pancreatic-cancer SIR and define screening value.
7. **Epigenomic profiling** (methylation/ATAC-seq) of AIP tissue to fill the current absence of epigenetic data.

---

## Consensus Answer

Autoimmune pancreatitis (AIP; MONDO:0015175) is a rare, corticosteroid-responsive fibroinflammatory chronic pancreatitis comprising three immunologically distinct subtypes — Type 1 (lymphoplasmacytic sclerosing pancreatitis, the pancreatic manifestation of IgG4-related disease, driven by a self-sustaining CD4+SLAMF7+ cytotoxic-T-lymphocyte/plasmablast loop with an upstream NET→plasmacytoid-dendritic-cell→IFN-α innate axis producing storiform fibrosis and obliterative phlebitis), Type 2 (idiopathic duct-centric pancreatitis, IgG4-negative, neutrophil/granulocytic-epithelial-lesion-mediated, associated with inflammatory bowel disease), and Type 3 (immune-checkpoint-inhibitor-induced). It is polygenic/multifactorial (HLA-DRB1, FCGR2B, CTLA4, FCRL3), typically presents in older men with painless obstructive jaundice mimicking pancreatic cancer, is diagnosed via ICDC/HISORt criteria, and carries a favorable prognosis (~85% 10-year survival) despite ~40% relapse in Type 1, managed with corticosteroids, rituximab, and the newly FDA-approved anti-CD19 agent inebilizumab.


## Artifacts

- [OpenScientist final report](Autoimmune_Pancreatitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autoimmune_Pancreatitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 42 |
| On topic | 29 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 26 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001824` (1 mention) - the report calls it "Symptom"; HP calls it **Weight loss**
- `HP:0002027` (1 mention) - the report calls it "Symptom"; HP calls it **Abdominal pain**
- `HP:0001738` (1 mention) - the report calls it "Lab/functional"; HP calls it **Exocrine pancreatic insufficiency**
- `HP:0000819` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Diabetes mellitus**
- `HP:0030355` (1 mention) - the report calls it "Increased circulating IgG level"; HP calls it **Abnormal circulating interferon-gamma concentration**
- `HP:0001880` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Increased total eosinophil count**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0030198` (1 mention) - the report calls it "extracellular matrix organization / fibrosis"; GO calls it **extracellular matrix organization**
- `CL:0000625` (1 mention) - the report calls it "CD8-positive cytotoxic T cell"; CL calls it **CD8-positive, alpha-beta T cell**
- `CL:0000624` (1 mention) - the report calls it "CD4-positive T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `UBERON:0002394` (1 mention) - the report calls it "Bile ducts / biliary tree"; UBERON calls it **bile duct**
- `UBERON:0002046` (1 mention) - the report calls it "Thyroid"; UBERON calls it **thyroid gland**, and lists "thyroid" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001264` - called "pancreas", "Pancreas"