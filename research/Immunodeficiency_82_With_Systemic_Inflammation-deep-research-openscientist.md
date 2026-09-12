---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-12T13:43:25.531926'
end_time: '2026-09-12T13:55:39.771523'
duration_seconds: 734.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 82 With Systemic Inflammation
  mondo_id: MONDO:0030308
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 12
  validator_version: 0.2.1
term_validation:
  total_terms: 22
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 10
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0001369
    reported_labels:
    - arthritis
    - Clinical sign
    ontology_label: Arthritis
  - term_id: HP:0011123
    reported_labels:
    - inflammatory abnormality of the skin / dermatitis
    - Physical manifestation
    ontology_label: Inflammatory abnormality of the skin
  - term_id: HP:0004297
    reported_labels:
    - diffuse large B-cell lymphoma
    - neoplasm of the immune system / lymphoma
    - Neoplasm
    ontology_label: Abnormality of the biliary system
  - term_id: HP:0002715
    reported_labels:
    - abnormality of the immune system / immunodeficiency
    - Clinical/lab
    ontology_label: Abnormality of the immune system
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_82_With_Systemic_Inflammation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_82_With_Systemic_Inflammation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 82 With Systemic Inflammation
- **MONDO ID:** MONDO:0030308 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 82 With Systemic Inflammation** covering all of the
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

# Immunodeficiency 82 With Systemic Inflammation (IMD82) — Comprehensive Disease Characterization Report

**Target Disease:** Immunodeficiency 82 With Systemic Inflammation
**OMIM:** #619381 · **MONDO:** MONDO:0030308 · **Causal gene:** *SYK* (HGNC:11491)
**Category:** Mendelian (monogenic inborn error of immunity)

---

## Summary

**Immunodeficiency 82 with systemic inflammation (IMD82) is an ultra-rare, autosomal dominant inborn error of immunity (IEI) caused by germline heterozygous gain-of-function (GOF) missense variants in *SYK* (spleen tyrosine kinase).** The disease was defined in 2021 by Wang and colleagues, who identified damaging monoallelic *SYK* variants in six patients presenting with a distinctive triad: immune deficiency, multi-organ inflammatory disease (colitis, arthritis, dermatitis), and diffuse large B-cell lymphoma (DLBCL) ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)). The variants increase SYK phosphorylation and enhance downstream signaling, establishing a gain-of-function mechanism.

Mechanistically, SYK is normally held in an **autoinhibited conformation** in which its tandem SH2 (tSH2) domain and interdomain linkers constrain the kinase domain. Binding of phosphorylated immunoreceptor tyrosine-based activation motifs (pITAMs) plus autophosphorylation switches SYK to its active state ([PMID: 23154170](https://pubmed.ncbi.nlm.nih.gov/23154170/)). IMD82 variants bias SYK toward the active conformation, producing **constitutive ITAM-based signaling** through PLCγ2, PI3K–AKT, MAPK/ERK, and NF-κB. This single hyperactive-kinase lesion simultaneously drives the inflammatory arm (excess cytokine/immune-cell activation) and the malignant arm (sustained pro-survival BCR/PI3K signaling that predisposes B cells to lymphoma).

Because the driver is a **druggable, hematopoietically restricted kinase**, IMD82 is potentially treatable. A knock-in *Syk*-Ser544Tyr mouse (modeling the patient variant p.Ser550Tyr) recapitulated key disease features that could be partially corrected either with a SYK inhibitor or with transplantation of wild-type bone marrow ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)). Fostamatinib, an FDA-approved oral SYK inhibitor (approved for chronic immune thrombocytopenia), provides a clinically available agent whose mechanism directly matches the disease lesion. Diagnosis relies on next-generation sequencing (whole-exome/whole-genome sequencing or IEI gene panels) with confirmatory functional testing of elevated SYK phosphorylation/downstream signaling. Only ~6 patients have been reported worldwide, so much of the clinical natural history remains to be defined.

---

## Key Findings

### Finding 1 — IMD82 is caused by monoallelic gain-of-function variants in *SYK*

Wang et al. (2021, *Nature Genetics*) identified damaging **monoallelic (heterozygous) *SYK* variants** in six patients. Functional assays demonstrated that the variants **increased SYK phosphorylation and enhanced downstream signaling**, formally establishing a gain-of-function (rather than loss-of-function) mechanism and an autosomal dominant mode of inheritance. This is the defining genetic feature of the disease and is catalogued as OMIM #619381 / MONDO:0030308.

> *"We identified damaging monoallelic SYK variants in six patients with immune deficiency, multi-organ inflammatory disease such as colitis, arthritis and dermatitis, and diffuse large B cell lymphomas. The SYK variants increased phosphorylation and enhanced downstream signaling, indicating gain of function."* — [PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)

This finding is notable because most *SYK*-related disease hypotheses historically concerned loss of function; IMD82 is a rare instance where a kinase gain-of-function drives a combined immunodeficiency-plus-autoinflammation syndrome.

### Finding 2 — SYK is normally autoinhibited; GOF variants disrupt the activation switch

Crystal structures of full-length SYK reveal an **autoinhibited conformation** in which the tandem SH2 (tSH2) domain and interdomain linkers restrain kinase activity. Binding of phosphorylated ITAMs to the tSH2 domain, together with autophosphorylation of interdomain-A tyrosines (e.g., Y348/Y352), switches SYK to the active conformation and strongly stimulates in vitro autophosphorylation ([PMID: 23154170](https://pubmed.ncbi.nlm.nih.gov/23154170/)). IMD82 patient variants (e.g., **p.Ser550Tyr**, and residues in the interdomain-A/kinase regions) constitutively bias this switch toward the active state, producing elevated basal phosphorylation and downstream signaling.

> *"Here, we present the first crystal structures of full-length Syk (fl-Syk) as wild type and as Y348F,Y352F mutant forms in complex with AMP-PNP revealing an autoinhibited conformation."* — [PMID: 23154170](https://pubmed.ncbi.nlm.nih.gov/23154170/)

> *"The functional relevance of pITAM binding to fl-Syk was confirmed by a strong stimulation of in vitro autophosphorylation."* — [PMID: 23154170](https://pubmed.ncbi.nlm.nih.gov/23154170/)

This provides a clear structural rationale for the disease: the GOF variants relieve the molecular brake that normally couples SYK activation to receptor engagement.

### Finding 3 — Constitutive SYK signaling links the inflammatory and lymphoma-predisposition arms

SYK is the proximal kinase that transduces signals from the B-cell receptor (BCR) and Fc/C-type-lectin receptors into downstream **PI3K–AKT, PLCγ2, MAPK/ERK, and NF-κB** cascades ([PMID: 35398488](https://pubmed.ncbi.nlm.nih.gov/35398488/); [PMID: 38503806](https://pubmed.ncbi.nlm.nih.gov/38503806/)). Sustained/tonic PI3K-pathway signaling downstream of SYK promotes B-cell **survival** rather than negative selection, and high SYK/BCR signaling activity predicts aggressive B-cell lymphoma behavior. This mechanistically unifies the two seemingly disparate arms of IMD82 — chronic multi-organ inflammation and predisposition to DLBCL — under a single constitutively active kinase.

> *"ZAP70 diverts SYK from activation of NFAT towards tonic PI3K-signaling, which promotes survival instead of cell death"* — [PMID: 35398488](https://pubmed.ncbi.nlm.nih.gov/35398488/)

In mantle cell lymphoma, higher BCR/SYK signaling responses correlate with shorter progression-free and overall survival, underscoring that SYK signaling intensity is a determinant of malignant aggressiveness ([PMID: 38503806](https://pubmed.ncbi.nlm.nih.gov/38503806/)).

### Finding 4 — Clinical phenotype: pediatric-onset immunodeficiency + multi-organ autoinflammation + DLBCL

In the defining cohort of six patients, the phenotype combined **immune deficiency** with **multi-organ inflammatory disease** — colitis (HP:0002583), arthritis (HP:0001369), and dermatitis (HP:0011123) — plus **diffuse large B-cell lymphoma** (HP:0004297) ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)). Onset is typically in childhood, frequently as a very-early-onset inflammatory-bowel-disease-like presentation. IMD82/SYK is incorporated into the formal IUIS Inborn Errors of Immunity classification framework used for diagnosis ([PMID: 41608114](https://pubmed.ncbi.nlm.nih.gov/41608114/)).

> *"immune deficiency, multi-organ inflammatory disease such as colitis, arthritis and dermatitis, and diffuse large B cell lymphomas"* — [PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)

> *"This report provides an updated classification of inborn errors of immunity (IEIs) involving 508 different genes and 17 phenocopies."* — [PMID: 41608114](https://pubmed.ncbi.nlm.nih.gov/41608114/)

### Finding 5 — Ultra-rare autosomal dominant disorder diagnosed by exome/genome sequencing

Only ~6 patients were reported in the defining publication, and no population prevalence/incidence estimates exist (ultra-rare). Inheritance is autosomal dominant (monoallelic/heterozygous variants), consistent with both de novo and inherited transmission. Diagnosis relies on next-generation sequencing (WES/WGS or IEI gene panels), as used across monogenic VEO-IBD and IEI cohorts, with confirmatory functional assays demonstrating elevated SYK phosphorylation/downstream signaling ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)).

> *"We identified damaging monoallelic SYK variants in six patients"* — [PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)

### Finding 6 — The disease is potentially treatable with SYK inhibition or bone-marrow transplant

A knock-in **Syk-Ser544Tyr mouse** (modeling patient variant p.Ser550Tyr) recapitulated aspects of the human disease that could be **partially treated with a SYK inhibitor** or with **transplantation of wild-type bone marrow** ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)). Fostamatinib is an FDA-approved oral SYK inhibitor (approved for chronic ITP), making targeted pharmacotherapy immediately plausible.

> *"A knock-in (SYK-Ser544Tyr) mouse model of a patient variant (p.Ser550Tyr) recapitulated aspects of the human disease that could be partially treated with a SYK inhibitor or transplantation of bone marrow from wild-type mice."* — [PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **germline heterozygous gain-of-function missense variant in *SYK*** (e.g., p.Ser550Tyr) arises de novo or is inherited (autosomal dominant). — *demonstrated* ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/))
2. The variant **disrupts SYK's autoinhibited conformation** — normally maintained by the tSH2 domain and interdomain-A linkers — biasing the kinase toward its active state. — *inferred from structure* ([PMID: 23154170](https://pubmed.ncbi.nlm.nih.gov/23154170/))
3. This **relieves the requirement for pITAM engagement/autophosphorylation**, so SYK exhibits **elevated basal (constitutive) kinase activity** and enhanced phosphorylation independent of full receptor input. — *demonstrated (increased pSYK)* ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/))
4. Constitutive SYK activity **hyper-transduces ITAM-coupled receptor signals** (BCR, Fc receptors, C-type lectin receptors) into downstream cascades: **PLCγ2, PI3K–AKT, MAPK/ERK, and NF-κB**. — *demonstrated/inferred* ([PMID: 35398488](https://pubmed.ncbi.nlm.nih.gov/35398488/))
5. The mechanism then **branches**:
   - **Branch A (autoinflammation/immune dysregulation):** Excess NF-κB/MAPK-driven cytokine production and immune-cell activation in myeloid and lymphoid compartments → **multi-organ inflammation** (colitis, arthritis, dermatitis). Paradoxical **immune deficiency** co-exists, reflecting dysregulated rather than simply amplified immunity. — *demonstrated clinically* ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/))
   - **Branch B (lymphomagenesis):** Sustained tonic **PI3K–AKT survival signaling** downstream of SYK promotes B-cell survival over negative selection, permitting accumulation of transformation-prone clones → **diffuse large B-cell lymphoma**. — *inferred from lymphoma biology* ([PMID: 35398488](https://pubmed.ncbi.nlm.nih.gov/35398488/); [PMID: 38503806](https://pubmed.ncbi.nlm.nih.gov/38503806/))
6. Because the lesion is a **hematopoietically restricted, druggable kinase**, **SYK inhibition** (pharmacologic) or **replacement of the mutant hematopoietic compartment** (WT bone-marrow transplant) partially reverses disease. — *demonstrated in mouse* ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/))

### Schematic

```
  SYK GOF variant (e.g. p.Ser550Tyr)
              │  disrupts
              ▼
  Autoinhibited SYK  ──X──►  Constitutively ACTIVE SYK
   (tSH2 brake)                    │ hyper-signaling
                                   ▼
        ┌──────────── ITAM-coupled receptor cascades ────────────┐
        │      PLCγ2 · PI3K–AKT · MAPK/ERK · NF-κB                 │
        └──────────────┬───────────────────────┬──────────────────┘
                       │                        │
             BRANCH A (inflammation)     BRANCH B (survival)
             cytokines, immune            tonic PI3K–AKT →
             dysregulation                B-cell survival
                       │                        │
                       ▼                        ▼
        Colitis, arthritis,            Diffuse large B-cell
        dermatitis + immune            lymphoma (DLBCL)
        deficiency
                       │                        │
                       └──── TREATABLE via ─────┘
                     SYK inhibitor (fostamatinib) │ WT BMT/HSCT
```

### Upstream vs downstream
- **Upstream (initiating):** the *SYK* GOF variant and loss of autoinhibition.
- **Midstream (amplifying):** constitutive PLCγ2/PI3K–AKT/MAPK/NF-κB signaling.
- **Downstream (manifesting):** organ inflammation and B-cell lymphomagenesis.

### Suggested ontology terms
- **Gene/protein:** *SYK* (HGNC:11491); GO:0004715 (non-membrane spanning protein tyrosine kinase activity); GO:0050853 (B cell receptor signaling pathway); GO:0038094 (Fc receptor signaling); GO:0002250 (adaptive immune response); GO:0006954 (inflammatory response); GO:0043066 (negative regulation of apoptotic process).
- **Cell types (CL):** CL:0000236 (B cell), CL:0000235 (macrophage), CL:0000775 (neutrophil), CL:0000542 (lymphocyte).
- **Subcellular (GO CC):** GO:0005829 (cytosol), GO:0005886 (plasma membrane / receptor-proximal).
- **Anatomy (UBERON):** UBERON:0000160 (intestine) — colitis; joint/synovium — arthritis; UBERON:0002097 (skin) — dermatitis; UBERON:0002509 (lymphoid tissue) — lymphoma.
- **Chemical (CHEBI):** fostamatinib / R788 (SYK inhibitor prodrug); ATP-competitive kinase inhibition.
- **Disease:** MONDO:0030308; **Phenotypes (HPO):** HP:0002583 (colitis), HP:0001369 (arthritis), HP:0011123 (inflammatory abnormality of the skin / dermatitis), HP:0004297 (neoplasm of the immune system / lymphoma), HP:0002715 (abnormality of the immune system / immunodeficiency).

---

## Section-by-Section Report

### 1. Disease Information
IMD82 is a Mendelian inborn error of immunity in which a single hyperactive kinase produces a combined phenotype of immunodeficiency, systemic autoinflammation, and B-cell lymphoma predisposition.
- **Key identifiers:** OMIM #619381; MONDO:0030308; causal gene *SYK* (HGNC:11491). Orphanet, ICD-10/ICD-11, and MeSH-specific codes are not clearly established for this ultra-rare 2021-defined entity; it maps within IEI/combined immunodeficiency-with-associated-features categories.
- **Synonyms:** "Immunodeficiency 82 with systemic inflammation"; "SYK gain-of-function disease"; "SYK-GOF immune dysregulation."
- **Information source:** Aggregated disease-level resources (OMIM, IUIS classification) built from an individual-patient case series (n≈6) rather than large EHR datasets.

### 2. Etiology
- **Causal factor:** Genetic — germline heterozygous GOF missense variants in *SYK* (monogenic, autosomal dominant) ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)).
- **Genetic risk factors:** The causal *SYK* variant itself is necessary and sufficient. Modifier genes are not defined given the tiny cohort. ZAP70 (SYK's paralog) shapes SYK signaling output in principle ([PMID: 35398488](https://pubmed.ncbi.nlm.nih.gov/35398488/)).
- **Environmental risk factors:** No established environmental triggers; inflammatory flares plausibly modulated by microbial/antigenic exposure via ITAM-coupled receptors (inferred, not demonstrated).
- **Protective factors:** None defined. By mechanistic logic, reduced SYK signaling (pharmacologic inhibition) is protective against manifestations.
- **Gene–environment interactions:** Not characterized; the ITAM-receptor biology implies antigen/microbe exposure could amplify constitutive signaling.

### 3. Phenotypes
| Phenotype | Type | HPO | Onset | Frequency (n≈6 cohort) |
|---|---|---|---|---|
| Colitis / IBD-like enteropathy | Clinical sign | HP:0002583 | Childhood/very-early-onset | Core feature |
| Arthritis | Clinical sign | HP:0001369 | Childhood | Core feature |
| Dermatitis | Physical manifestation | HP:0011123 | Childhood | Core feature |
| Immunodeficiency (infection susceptibility) | Clinical/lab | HP:0002715 | Childhood | Core feature |
| Diffuse large B-cell lymphoma | Neoplasm | HP:0004297 | Childhood–young adult | Reported in cohort |

Severity is variable and can be severe/refractory; progression includes both chronic inflammation and episodic flares plus a serious oncologic complication (DLBCL). Quality-of-life impact is substantial (chronic multi-organ inflammation, malignancy risk, treatment burden), though formal EQ-5D/SF-36 data are unavailable for this ultra-rare disease ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)).

### 4. Genetic / Molecular Information
- **Causal gene:** *SYK* (spleen tyrosine kinase), chromosome 9q22, HGNC:11491; encodes a cytoplasmic non-receptor tyrosine kinase with tandem SH2 domains + kinase domain.
- **Variant classification/type:** Pathogenic/likely pathogenic **missense** variants (e.g., **p.Ser550Tyr**) affecting the activation switch (interdomain-A/kinase regions) ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)).
- **Functional consequence:** **Gain of function** — increased phosphorylation and enhanced downstream signaling.
- **Allele frequency:** Effectively absent from population databases (gnomAD) given pathogenicity and rarity.
- **Origin:** Germline (monoallelic); both de novo and inherited transmission consistent with AD inheritance. (Note: a distinct *somatic* ETV6–SYK fusion drives chronic eosinophilic leukemia — a separate entity, not IMD82 — [PMID: 42005114](https://pubmed.ncbi.nlm.nih.gov/42005114/).)
- **Modifier genes / epigenetics / chromosomal abnormalities:** Not defined for this disorder.

### 5. Environmental Information
No established environmental, lifestyle, or infectious causes. The disease is monogenic. Because SYK sits downstream of pattern-recognition and Fc/C-type-lectin receptors, microbial and antigenic exposures are plausible amplifiers of inflammation but are not demonstrated drivers.

### 6. Mechanism / Pathophysiology
Presented above as the ordered causal chain and schematic. In brief: a *SYK* GOF variant disrupts kinase autoinhibition → constitutive ITAM-coupled signaling (PLCγ2, PI3K–AKT, MAPK/ERK, NF-κB) → branches into (A) multi-organ autoinflammation with paradoxical immunodeficiency and (B) tonic PI3K–AKT survival signaling predisposing to DLBCL. Key molecular pathways: **B-cell receptor signaling (Reactome/KEGG), Fc receptor signaling, PI3K–AKT, MAPK, NF-κB**. Cellular processes: inflammation, dysregulated lymphocyte/myeloid activation, and suppressed apoptosis/enhanced survival of B cells. Immune involvement spans both immunodeficiency and chronic inflammation — a hallmark of immune-dysregulation IEIs.

### 7. Anatomical Structures Affected
- **Primary organs/systems:** Gastrointestinal tract (colon — colitis; UBERON:0000160), joints (arthritis; synovium), skin (dermatitis; UBERON:0002097), and the immune/lymphoid system (UBERON:0002509).
- **Secondary/complication:** Lymphoid tissues affected by DLBCL; systemic effects of chronic inflammation.
- **Cell populations:** B lymphocytes (CL:0000236) central; macrophages (CL:0000235), neutrophils (CL:0000775), and other ITAM-receptor-bearing hematopoietic cells contribute.
- **Subcellular:** Cytosolic/plasma-membrane-proximal signaling compartments (GO:0005829, GO:0005886).
- **Laterality:** Systemic/bilateral (not a lateralized disease).

### 8. Temporal Development
- **Onset:** Pediatric/childhood, often very-early-onset (VEO-IBD-like presentation); course is chronic with episodic inflammatory flares.
- **Progression:** Variable; chronic multi-organ inflammation punctuated by the serious late complication of DLBCL.
- **Critical windows:** Early SYK-targeted intervention is mechanistically attractive to blunt both inflammation and lymphoma risk (inferred from mouse rescue data, [PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)).

### 9. Inheritance and Population
- **Epidemiology:** Ultra-rare; ~6 reported patients; no prevalence/incidence estimates.
- **Inheritance:** Autosomal dominant (monoallelic/heterozygous). Penetrance/expressivity not quantifiable in so small a cohort; both de novo and inherited variants are consistent with the genetics.
- **Founder effects/consanguinity/carrier frequency:** Not applicable (dominant, ultra-rare).
- **Demographics:** No described ethnic, geographic, or sex predilection.

### 10. Diagnostics
- **Recommended approach:** Next-generation sequencing — **whole-exome or whole-genome sequencing**, or **IEI/VEO-IBD gene panels** including *SYK* — is the diagnostic backbone ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/); cohorts in [PMID: 42494428](https://pubmed.ncbi.nlm.nih.gov/42494428/), [PMID: 42724325](https://pubmed.ncbi.nlm.nih.gov/42724325/)).
- **Confirmatory functional testing:** Phospho-specific assays demonstrating **elevated basal/inducible SYK phosphorylation (pSYK) and enhanced downstream signaling** distinguish GOF variants from benign or LOF variants — a key step because *SYK* variant interpretation requires functional context.
- **Supportive workup:** Immunophenotyping/immunoglobulin levels (immunodeficiency evaluation), inflammatory markers, endoscopy/biopsy for colitis, and oncologic staging if lymphoma is suspected.
- **Differential diagnosis:** Other monogenic immune-dysregulation/VEO-IBD disorders (e.g., CTLA4 haploinsufficiency — [PMID: 42577265](https://pubmed.ncbi.nlm.nih.gov/42577265/)), other IEIs with autoimmunity/lymphoproliferation ([PMID: 42625995](https://pubmed.ncbi.nlm.nih.gov/42625995/)). Functional pSYK testing plus the specific *SYK* variant distinguishes IMD82.

### 11. Outcome / Prognosis
No formal survival statistics exist for this ultra-rare entity. Prognosis is shaped by (a) severity/refractoriness of multi-organ inflammation and (b) the serious complication of DLBCL, which historically carries substantial mortality. The identification of a **druggable, hematopoietically restricted target** materially improves the outlook, since SYK inhibition or HSCT can address the root cause (mouse-model rescue, [PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)). Prognostic biomarkers plausibly include SYK/BCR signaling intensity, given its correlation with aggressive B-cell lymphoma behavior ([PMID: 38503806](https://pubmed.ncbi.nlm.nih.gov/38503806/)).

### 12. Treatment
- **Targeted pharmacotherapy (NCIT: spleen tyrosine kinase inhibitor):** **Fostamatinib** (R788), an FDA-approved oral SYK inhibitor (approved for chronic ITP), mechanistically matches the lesion; mouse data show a SYK inhibitor partially treats the disease ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)). Fostamatinib's efficacy in other SYK-driven immune disorders (ITP, warm AIHA, TRAF3-deficient autoimmunity) supports the class rationale ([PMID: 40903253](https://pubmed.ncbi.nlm.nih.gov/40903253/); [PMID: 42026764](https://pubmed.ncbi.nlm.nih.gov/42026764/)). **Safety note:** fostamatinib carries potential vascular/thrombotic and off-target concerns (e.g., a reported aortic-dissection case, [PMID: 40962713](https://pubmed.ncbi.nlm.nih.gov/40962713/)).
- **Cell therapy (NCIT: hematopoietic stem cell transplantation):** **Allogeneic HSCT / wild-type bone-marrow transplant** is curative in the mouse model and is a rational option because the disease is hematopoietically restricted ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)).
- **Supportive/anti-inflammatory therapy:** Standard IEI/IBD management (immunoglobulin replacement for immunodeficiency; anti-inflammatory/biologic/JAK-inhibitor strategies for colitis/arthritis/dermatitis, extrapolated from VEO-IBD practice, [PMID: 42499735](https://pubmed.ncbi.nlm.nih.gov/42499735/)).
- **Lymphoma therapy:** Standard DLBCL protocols if malignancy develops; SYK/BCR-pathway inhibitors (SYK, BTK, PI3K) are active in B-cell malignancies ([PMID: 38660880](https://pubmed.ncbi.nlm.nih.gov/38660880/); [PMID: 35296646](https://pubmed.ncbi.nlm.nih.gov/35296646/)).
- **Personalized medicine:** IMD82 is a paradigm for **genotype-guided targeted therapy** — the causal kinase is the drug target.

### 13. Prevention
- **Primary prevention:** Not applicable (monogenic); **genetic counseling** for affected families given autosomal dominant inheritance.
- **Secondary prevention:** Cascade genetic testing of relatives; surveillance for lymphoma and inflammatory complications in carriers.
- **Tertiary prevention:** Early SYK-targeted therapy or HSCT to limit organ damage and potentially reduce lymphoma risk (inferred).
- **Prenatal/preimplantation testing:** Available in principle once the familial variant is known.

### 14. Other Species / Natural Disease
- **Model taxonomy:** *Mus musculus* (NCBI Taxon 10090) via the knock-in Syk-Ser544Tyr allele ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)).
- **Orthologs:** *Syk* is conserved across vertebrates, including jawless fish (lamprey Lj-Syk), with conserved tandem-SH2 and kinase domains ([PMID: 25682127](https://pubmed.ncbi.nlm.nih.gov/25682127/)).
- **Natural disease in other species:** No naturally occurring animal counterpart of IMD82 is documented (OMIA); the disease is defined in humans with an engineered mouse model.

### 15. Model Organisms
- **Principal model:** **Knock-in mouse Syk-Ser544Tyr**, engineered to mirror the human p.Ser550Tyr GOF variant. It **recapitulated aspects of the human disease** and, critically, was **partially rescued by a SYK inhibitor or by wild-type bone-marrow transplantation** ([PMID: 33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/)) — providing both face validity and therapeutic proof-of-concept.
- **Complementary tools:** Chemical-genetic (analog-sensitive) SYK mouse systems and myeloid-specific SYK knockouts exist for dissecting SYK-dependent signaling ([PMID: 31356155](https://pubmed.ncbi.nlm.nih.gov/31356155/)), and B-cell TRAF3-deficient mice model SYK-driven autoimmunity/lymphoma responsive to fostamatinib ([PMID: 42026764](https://pubmed.ncbi.nlm.nih.gov/42026764/)).
- **Limitations:** Partial (not complete) recapitulation/rescue; small human cohort limits cross-validation; models emphasize signaling and inflammation more than the full lymphoma trajectory.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [33782605](https://pubmed.ncbi.nlm.nih.gov/33782605/) | *Gain-of-function variants in SYK cause immune dysregulation and systemic inflammation* (Nat Genet 2021) | **Defining paper.** Establishes monoallelic SYK GOF, clinical triad, mouse model, and therapeutic rescue (SYK inhibitor / WT BMT). |
| [23154170](https://pubmed.ncbi.nlm.nih.gov/23154170/) | *Structural and biophysical characterization of the Syk activation switch* | Structural basis: full-length SYK autoinhibition and the pITAM/autophosphorylation activation switch disrupted by GOF variants. |
| [35398488](https://pubmed.ncbi.nlm.nih.gov/35398488/) | *SYK and ZAP70 kinases in autoimmunity and lymphoid malignancies* | Mechanistic link: SYK-driven tonic PI3K signaling promotes survival over cell death — basis for lymphoma predisposition. |
| [38503806](https://pubmed.ncbi.nlm.nih.gov/38503806/) | *BCR signaling activity identifies higher-risk MCL patients* | High SYK/BCR signaling predicts aggressive B-cell lymphoma behavior; supports Branch B. |
| [41608114](https://pubmed.ncbi.nlm.nih.gov/41608114/) | *Human inborn errors of immunity: 2024 IUIS update* | Situates IMD82/SYK within the formal IEI classification used for diagnosis. |
| [42026764](https://pubmed.ncbi.nlm.nih.gov/42026764/) | *Syk inhibition limits autoimmunity in B-cell TRAF3-deficient mice* | Class-level support that fostamatinib corrects SYK-driven B-cell dysfunction/autoimmunity. |
| [40903253](https://pubmed.ncbi.nlm.nih.gov/40903253/) | *Future directions in warm AIHA management* | Fostamatinib as an established, efficacious SYK inhibitor in immune disease. |
| [40962713](https://pubmed.ncbi.nlm.nih.gov/40962713/) | *Fostamatinib and acute aortic dissection in ITP* | Safety caveat for chronic SYK inhibition. |
| [31356155](https://pubmed.ncbi.nlm.nih.gov/31356155/) | *Chemical-genetics SYK mouse model* | Complementary tool confirming SYK-dependent BCR signaling. |
| [25682127](https://pubmed.ncbi.nlm.nih.gov/25682127/) | *SYK molecular evolution in lamprey* | Evolutionary conservation of SYK tandem-SH2/kinase architecture. |

Evidence-source types: **Human clinical** (PMID 33782605 case series; IUIS classification 41608114); **model organism** (33782605 mouse; 42026764; 31356155); **in vitro/structural** (23154170; 35398488); **lymphoma clinical correlation** (38503806).

---

## Limitations and Knowledge Gaps

1. **Tiny cohort (n≈6):** All core clinical claims rest on a single 2021 case series. Penetrance, expressivity, sex ratio, natural history, and quantitative phenotype frequencies cannot be reliably estimated.
2. **No epidemiology:** Prevalence/incidence are unknown; the disease is ultra-rare with no registry data.
3. **Branch B is partly inferred:** The lymphoma-predisposition mechanism is supported by strong SYK/BCR biology ([PMID: 35398488](https://pubmed.ncbi.nlm.nih.gov/35398488/); [PMID: 38503806](https://pubmed.ncbi.nlm.nih.gov/38503806/)) but has not been dissected specifically in IMD82 patient B cells at scale.
4. **Variant spectrum incomplete:** Only a few variants (notably p.Ser550Tyr) are characterized; the full allelic series and genotype–phenotype correlations are undefined.
5. **Therapeutic evidence is preclinical:** SYK-inhibitor/BMT rescue is demonstrated in mice; human treatment outcomes for IMD82 specifically are anecdotal, and fostamatinib carries vascular/thrombotic safety concerns ([PMID: 40962713](https://pubmed.ncbi.nlm.nih.gov/40962713/)).
6. **No omics depth:** Patient-level transcriptomic, proteomic, metabolomic, or single-cell data for IMD82 are not available in the reviewed literature.
7. **Missing ontology/registry codes:** Orphanet/ICD/MeSH-specific mappings are not firmly established for this recently defined entity.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international IMD82 patient registry** with genotype, functional pSYK data, longitudinal inflammation scores, and lymphoma incidence to define natural history, penetrance, and expressivity.
2. **Expand and functionally classify the *SYK* variant allelic series** (deep mutational scanning across the tSH2/interdomain-A/kinase regions) to build a genotype–phenotype and pSYK-activity map for variant interpretation (ACMG PS3 functional evidence).
3. **Single-cell multi-omics of patient PBMC/gut/lymphoma tissue** to resolve which cell types (B cells vs myeloid) drive Branch A vs Branch B and to identify predictive biomarkers.
4. **Prospective, biomarker-guided fostamatinib trial in IMD82** (with cardiovascular safety monitoring per [PMID: 40962713](https://pubmed.ncbi.nlm.nih.gov/40962713/)), including pSYK/PI3K-AKT pharmacodynamic readouts.
5. **Define HSCT indications and outcomes** for severe/lymphoma-associated IMD82, leveraging the mouse WT-BMT rescue as rationale.
6. **Test whether early SYK inhibition reduces lymphoma incidence** in the Syk-Ser544Tyr knock-in model (chemoprevention proof-of-concept).
7. **Formalize ontology/registry entries** (Orphanet, ICD-11, MeSH) and curate HPO frequency annotations as new cases accrue.

---

*Report compiled from 6 confirmed findings and 32 reviewed papers over 5 investigation iterations. Evidence source types are distinguished throughout as human clinical, model organism, in vitro/structural, or computational.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_82_With_Systemic_Inflammation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_82_With_Systemic_Inflammation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001369` (3 mentions) - the report calls it "arthritis", "Clinical sign"; HP calls it **Arthritis**
- `HP:0011123` (3 mentions) - the report calls it "inflammatory abnormality of the skin / dermatitis", "Physical manifestation"; HP calls it **Inflammatory abnormality of the skin**
- `HP:0004297` (3 mentions) - the report calls it "diffuse large B-cell lymphoma", "neoplasm of the immune system / lymphoma", "Neoplasm"; HP calls it **Abnormality of the biliary system**
- `HP:0002715` (2 mentions) - the report calls it "abnormality of the immune system / immunodeficiency", "Clinical/lab"; HP calls it **Abnormality of the immune system**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002583` (3 mentions) - the report calls it "colitis", "Clinical sign"; HP calls it **Colitis**
- `GO:0038094` (1 mention) - the report calls it "Fc receptor signaling"; GO calls it **Fc-gamma receptor signaling pathway**
- `CL:0000236` (2 mentions) - the report calls it "B cell", "Cell populations:** B lymphocytes"; CL calls it **B cell**, and lists "B lymphocyte" among its other names
- `GO:0005886` (2 mentions) - the report calls it "plasma membrane / receptor-proximal"; GO calls it **plasma membrane**
- `UBERON:0002097` (2 mentions) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0002509` (2 mentions) - the report calls it "lymphoid tissue"; UBERON calls it **mesenteric lymph node**, and lists "nodi lymphoidei mesenterici" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:11491` - called "SYK", "Gene/protein:** *SYK"
- `HP:0002583` - called "colitis", "Clinical sign"
- `HP:0001369` - called "arthritis", "Clinical sign"
- `HP:0011123` - called "inflammatory abnormality of the skin / dermatitis", "Physical manifestation"
- `HP:0004297` - called "diffuse large B-cell lymphoma", "neoplasm of the immune system / lymphoma", "Neoplasm"
- `CL:0000236` - called "B cell", "Cell populations:** B lymphocytes"
- `HP:0002715` - called "abnormality of the immune system / immunodeficiency", "Clinical/lab"