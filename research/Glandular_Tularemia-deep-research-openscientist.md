---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T09:22:16.042647'
end_time: '2026-09-25T09:49:38.905500'
duration_seconds: 1642.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Glandular Tularemia
  mondo_id: MONDO:0000320
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 39
reference_validation:
  total_references: 39
  verified: 39
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 39
  on_topic: 25
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 21
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 8
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0002716
    reported_labels:
    - Clinical sign
    ontology_label: Lymphadenopathy
  - term_id: HP:0001945
    reported_labels:
    - Symptom/sign
    ontology_label: Fever
  - term_id: HP:0003688
    reported_labels:
    - Symptom
    ontology_label: Cytochrome C oxidase-negative muscle fibers
  - term_id: HP:0002315
    reported_labels:
    - Symptom
    ontology_label: Headache
  - term_id: HP:0003326
    reported_labels:
    - Symptom
    ontology_label: Myalgia
  - term_id: HP:0025145
    reported_labels:
    - Symptom
    ontology_label: Rigors
  - term_id: GO:0005829
    reported_labels:
    - cytosol
    - Subcellular level:** *Francisella*-containing phagosome and host **cytosol
    ontology_label: cytosol
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Glandular_Tularemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Glandular_Tularemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glandular Tularemia
- **MONDO ID:** MONDO:0000320 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Glandular Tularemia** covering all of the
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

# Glandular Tularemia — Comprehensive Disease Characteristics Report

**Disease:** Glandular Tularemia
**MONDO ID:** MONDO:0000320
**Category:** Infectious Disease (zoonotic bacterial infection)
**Causative agent:** *Francisella tularensis* (Gram-negative, facultative intracellular coccobacillus)

---

## Summary

Glandular tularemia is one of the localized clinical forms of tularemia, a zoonosis caused by the highly infectious Gram-negative facultative intracellular coccobacillus *Francisella tularensis*. It is defined clinically as **acute regional lymphadenopathy with flu-like constitutional symptoms but WITHOUT the skin ulcer/eschar** that characterizes the closely related ulceroglandular form. The distinction is purely one of whether a visible inoculation ulcer is present; the underlying pathogen, transmission routes (arthropod bite or direct animal/carcass contact), and management are identical. Glandular and ulceroglandular disease are the dominant presentations of arthropod-borne tularemia and, together, are the most common clinical entities seen across case series worldwide ([PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/), [PMID: 40466250](https://pubmed.ncbi.nlm.nih.gov/40466250/)).

This is a **purely infectious disease with no heritable genetic basis** — there are no human causal genes, pathogenic germline/somatic variants, chromosomal abnormalities, inheritance pattern, penetrance, or carrier frequency. All disease-determining genetics reside in the pathogen genome (notably the Francisella Pathogenicity Island encoding a Type VI secretion system) and in host exposure and immune status. The pathophysiology is a well-defined causal chain: cutaneous/arthropod inoculation → macrophage uptake → Type VI secretion-mediated phagosomal escape → cytosolic replication → drainage to regional lymph nodes → inflammasome-driven necrotizing/suppurative granulomatous lymphadenitis → clinically palpable, sometimes suppurating, regional adenopathy.

The single most important, modifiable determinant of morbidity is **diagnostic delay**. Because *F. tularensis* is intrinsically resistant to beta-lactams and frequently culture-negative, glandular tularemia is repeatedly misdiagnosed and treated with ineffective beta-lactams before the correct diagnosis is made, leading to node suppuration and surgical intervention. When appropriate therapy — an aminoglycoside, a fluoroquinolone, or a tetracycline — is started early, case fatality is <1.5% and defervescence is rapid. Prevention rests on exposure avoidance and antibiotic post-exposure prophylaxis, as **no licensed human vaccine exists**.

---

## Section 1 — Disease Information

**Overview.** Glandular tularemia is a localized form of tularemia presenting as painful regional lymph node swelling accompanied by an abrupt flu-like illness (fever, chills, malaise, headache, myalgia), but lacking the cutaneous ulcer/eschar seen in ulceroglandular disease. In a systematic review of 870 cases spanning 1993–2023, the most common clinical forms were ulceroglandular, oropharyngeal, glandular, and pneumonic disease ([PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)). Arthropod-borne (tick, mosquito, horsefly) transmission mainly presents as the glandular or ulceroglandular form ([PMID: 42601640](https://pubmed.ncbi.nlm.nih.gov/42601640/)).

**Key identifiers.**
- **MONDO:** MONDO:0000320 (glandular tularemia)
- **MeSH:** Tularemia (D014406)
- **ICD-10:** A21.- (Tularemia); glandular tularemia falls under the A21 group (A21.0 is the ulceroglandular subtype)
- **ICD-11:** 1B94 Tularaemia
- **OMIM / Orphanet:** Not applicable as a Mendelian entry — tularemia is an infectious disease, not a heritable disorder. There is no OMIM gene-disease entry.

**Synonyms / alternative names.** Glandular tularaemia (British spelling); "rabbit fever," "deer-fly fever," "Ohara disease," "Francis disease," and "lemming fever" are historical names for tularemia as a whole. Glandular tularemia specifically denotes the lymphadenopathic-without-ulcer subtype.

**Information source.** Disease-level knowledge here is derived predominantly from **aggregated disease-level resources** — systematic reviews, case series, national surveillance (CDC, ECDC), and experimental microbiology — supplemented by individual case reports. It is not derived from a single EHR cohort.

---

## Section 2 — Etiology

**Causal factor.** The disease is **infectious**, caused by *Francisella tularensis*. Two subspecies drive nearly all human disease:

| Subspecies | Type | Geography | Virulence |
|---|---|---|---|
| *F. tularensis* subsp. *tularensis* | Type A | Primarily North America | More virulent; subdivides into A.I (central US) and A.II (western US), with A.II less severe |
| *F. tularensis* subsp. *holarctica* | Type B | Circumpolar Northern Hemisphere (Europe, Asia, N. America) | Lower virulence; rarely fatal |

Whole-genome SNP phylogeography shows type B (holarctica) has a circumpolar distribution and low genetic diversity consistent with recent clonal radiation ([PMID: 19251856](https://pubmed.ncbi.nlm.nih.gov/19251856/)). Type A and type B infections "differ with respect to affected populations, anatomic site of isolation, and geographic distribution" ([PMID: 16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/)). European human infections are predominantly holarctica, frequently acquired from European brown hares (*Lepus europaeus*) ([PMID: 23517149](https://pubmed.ncbi.nlm.nih.gov/23517149/)).

**Genetic risk factors (human).** **None.** There are no human causal genes, susceptibility loci, or modifier alleles. This is not a genetic disease ([PMID: 15677845](https://pubmed.ncbi.nlm.nih.gov/15677845/)).

**Environmental / exposure risk factors.** Arthropod bites (ticks, deer flies, mosquitoes), handling of infected wild animals or carcasses (especially lagomorphs and rodents), contaminated water (type B), inhalation of aerosols (e.g., mowing over carcasses), and occupational/recreational exposure (hunters, farmers, landscapers, laboratory workers). Male predominance in tick-associated regions reflects exposure patterns rather than biological susceptibility ([PMID: 40907418](https://pubmed.ncbi.nlm.nih.gov/40907418/)).

**Host susceptibility / severity modifiers.** Immunosuppression increases severity: severe and atypical courses have been documented during anti-TNF-α (adalimumab)/methotrexate therapy and in immunocompromised patients ([PMID: 19801257](https://pubmed.ncbi.nlm.nih.gov/19801257/)).

**Protective factors.** No genetic protective variants are described. Protection is behavioral (exposure avoidance) and, immunologically, prior antigen exposure conferring Th1 memory.

**Gene–environment interactions.** Not applicable in the classical GxE sense (no host genotype interacting with exposure). The operative "gene–environment" axis is the **pathogen** genotype (subspecies A vs B, FPI content) interacting with route of inoculation, inoculum dose, and host immune status to determine clinical form and severity.

---

## Section 3 — Phenotypes

Glandular tularemia's phenotype is dominated by regional lymphadenopathy plus a flu-like prodrome. Onset is acute, typically **3–5 days (range 1–21)** after exposure ([PMID: 18755386](https://pubmed.ncbi.nlm.nih.gov/18755386/), [PMID: 26738841](https://pubmed.ncbi.nlm.nih.gov/26738841/)).

| Phenotype | Type | HPO term | Frequency / notes |
|---|---|---|---|
| Regional lymphadenopathy | Clinical sign | HP:0002716 | Near-universal in glandular form; defining feature; may become fluctuant/suppurative |
| Fever | Symptom/sign | HP:0001945 | Most patients; abrupt onset |
| Fatigue / malaise | Symptom | HP:0003688 | Common |
| Headache | Symptom | HP:0002315 | Common |
| Myalgia | Symptom | HP:0003326 | Common |
| Chills / rigor | Symptom | HP:0025145 | Common |
| **Absence** of skin ulcer | Distinguishing feature | — | Differentiates glandular from ulceroglandular |

**Characteristics.** Age of onset: any age (exposure-driven; US incidence peaks in children 5–9 years and men >55 years). Severity: mild-to-moderate for type B glandular disease; variable. Progression: acute onset, generally self-limited with treatment, but nodes may persist, suppurate, fistulize, or require drainage. In one ulceroglandular case, painful lymphadenopathy persisted **>5 months** ([PMID: 19551605](https://pubmed.ncbi.nlm.nih.gov/19551605/)). Frequency of the glandular form: ~15.8% of cases in a Central Anatolian series, while (ulcero-)glandular disease combined was the most common entity (10/14) in a German series ([PMID: 23104256](https://pubmed.ncbi.nlm.nih.gov/23104256/), [PMID: 40466250](https://pubmed.ncbi.nlm.nih.gov/40466250/)).

**Quality of life impact.** Acute painful lymphadenopathy and constitutional symptoms cause short-term functional impairment; suppuration requiring surgical drainage and prolonged/relapsing courses (especially with bacteriostatic doxycycline) extend morbidity. Long-term disability is uncommon with appropriate treatment. No disease-specific EQ-5D/SF-36 datasets are available.

---

## Section 4 — Genetic / Molecular Information

**This section is largely NOT APPLICABLE at the human level.** Glandular tularemia has:
- **No causal human genes** (no OMIM gene-disease entry)
- **No pathogenic human variants** (nothing in ClinVar/HGMD as causal)
- **No modifier genes, epigenetic disease signatures, or chromosomal abnormalities** in the host

All disease-relevant genetics reside in the **pathogen**:
- The **Francisella Pathogenicity Island (FPI)**, present in duplicate, encodes an atypical **Type VI secretion system (T6SS)** (genes *iglABCD*, *pdpA–E*, *vgrG*, *dotU*) essential for virulence ([PMID: 30054549](https://pubmed.ncbi.nlm.nih.gov/30054549/)).
- Subspecies/subpopulation markers (RD1, type A.I/A.II, type B) determine geography and virulence ([PMID: 16485467](https://pubmed.ncbi.nlm.nih.gov/16485467/), [PMID: 22859584](https://pubmed.ncbi.nlm.nih.gov/22859584/)).

The absence of human genetic determinants is itself a confirmed finding of this investigation ([PMID: 15677845](https://pubmed.ncbi.nlm.nih.gov/15677845/)).

---

## Section 5 — Environmental Information

**Environmental factors.** Tick and insect vectors, aquatic reservoirs (type B water-borne cycle), and animal carcasses are the principal environmental sources. Aerosolization (e.g., lawn-mowing over infected carcasses) is a recognized route.

**Infectious agent.** *Francisella tularensis* (NCBI Taxonomy ID 263), subspecies *tularensis* (type A) and *holarctica* (type B); subsp. *mediasiatica* and the related *F. novicida* are minor/experimental. The organism has an extremely **low infectious dose — as few as ~10 organisms can establish infection** — and untreated tularemia overall carries up to **30% mortality** ([PMID: 42641375](https://pubmed.ncbi.nlm.nih.gov/42641375/)). It is a CDC Category A / Tier 1 select agent because of this low dose and aerosol potential ([PMID: 25413334](https://pubmed.ncbi.nlm.nih.gov/25413334/)).

**Lifestyle factors.** Hunting, trapping, farming, landscaping, and outdoor recreation in endemic areas increase exposure; seasonality tracks tick activity (summer/early autumn) ([PMID: 39295179](https://pubmed.ncbi.nlm.nih.gov/39295179/)).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Arthropod bite or direct contact with an infected animal/carcass inoculates *F. tularensis* into the skin/subcutis** (very low infectious dose, ~10 organisms) → **leads to** local bacterial deposition at the inoculation site. In glandular disease, no visible ulcer forms (branch point vs. ulceroglandular, where a cutaneous ulcer develops).
2. **Bacteria are taken up by resident macrophages/dendritic cells** → **results in** an intracellular (phagosomal) niche. [demonstrated in vitro]
3. **FPI/T6SS-mediated escape from the phagosome into the cytosol** → **leads to** access to the nutrient-rich cytoplasm. The T6SS effector **OpiA**, a wortmannin-resistant bacterial PI3-kinase, alters phagosomal PI(3)P to promote escape ([PMID: 30057173](https://pubmed.ncbi.nlm.nih.gov/30057173/)); **ClpB (HSP100)** is required for T6SS function ([PMID: 30054549](https://pubmed.ncbi.nlm.nih.gov/30054549/)); **type IV pilus component PilO** mediates macrophage adherence and is required for escape/virulence ([PMID: 35077486](https://pubmed.ncbi.nlm.nih.gov/35077486/)).
4. **Cytosolic replication** → **results in** rising intracellular bacterial burden.
5. **Active subversion of innate immunity** → **leads to** stealthy early spread. In neutrophils the bacterium inhibits NADPH oxidase assembly and **delays constitutive apoptosis** (~80% of infected neutrophils viable at 48 h vs ~50% controls) ([PMID: 22357630](https://pubmed.ncbi.nlm.nih.gov/22357630/)); its atypical tetra-acylated LPS is poorly sensed by TLR4; virulent SchuS4 fails to trigger dendritic-cell/monocyte proinflammatory cytokines unless CD14 is present ([PMID: 19841074](https://pubmed.ncbi.nlm.nih.gov/19841074/)).
6. **Bacteria drain via lymphatics to the regional lymph node** → **results in** localized infection of the node (the anatomical basis of the "glandular" phenotype).
7. **Cytosolic sensing by inflammasomes (AIM2, NLRP3) and eventual Th1 cell-mediated response** → **leads to** pyroptosis, cytokine release, and granuloma formation; **NLRP3 increases host susceptibility** ([PMID: 34690967](https://pubmed.ncbi.nlm.nih.gov/34690967/)).
8. **Necrotizing/suppurative granulomatous lymphadenitis** → **results in** the palpable, tender, sometimes fluctuant/suppurating regional lymphadenopathy that is the clinical hallmark. Histopathology shows granulomas, necrosis, and suppurative inflammation with epithelioid histiocytes and giant cells, sometimes extending extracapsularly ([PMID: 23763361](https://pubmed.ncbi.nlm.nih.gov/23763361/), [PMID: 19801257](https://pubmed.ncbi.nlm.nih.gov/19801257/)).
9. **Protective clearance depends on cell-mediated immunity** (Th1/CD4+/CD8+ IFN-γ, IL-17) → **results in** resolution; antibody responses are secondary. This T-cell dominance is the basis of the *F. tularensis*-specific T-cell diagnostic response ([PMID: 10618057](https://pubmed.ncbi.nlm.nih.gov/10618057/), [PMID: 38713688](https://pubmed.ncbi.nlm.nih.gov/38713688/)).

### Category checklist

- **Molecular pathways:** Bacterial PI3-kinase (OpiA) manipulation of phosphoinositide (PI(3)P) signaling; host NADPH oxidase; TLR4/CD14 innate signaling; inflammasome (AIM2/NLRP3–caspase-1) axis.
- **Cellular processes:** Phagocytosis, phagosomal escape, intracellular replication, inhibition of neutrophil apoptosis, pyroptosis, granulomatous inflammation.
- **Protein dysfunction:** No host protein misfolding — mechanism is driven by bacterial effectors (T6SS, PilO, ClpB) hijacking host cell biology.
- **Immune system involvement:** Innate evasion (weak TLR4 signaling, apoptosis delay, NADPH oxidase inhibition) followed by protective Th1 cell-mediated immunity.
- **Tissue damage mechanisms:** Caseating/suppurative necrosis within lymph nodes; abscess/fistula formation.
- **GO terms (suggested):** GO:0052167 (modulation by symbiont of host innate immune response), GO:0030682 (evasion of host defenses), GO:0006909 (phagocytosis), GO:0043312 (neutrophil degranulation), GO:0042981 (regulation of apoptotic process), GO:0002532 (production of molecular mediators involved in inflammatory response).
- **CL terms (suggested):** CL:0000235 (macrophage), CL:0000775 (neutrophil), CL:0000451 (dendritic cell), CL:0000084 (T cell).

---

## Section 7 — Anatomical Structures Affected

- **Primary organ:** Regional **lymph node** draining the inoculation site (UBERON:0000029). Location of adenopathy depends on inoculation site: cervical/head-and-neck, axillary, epitrochlear, or inguinal.
- **Secondary involvement:** Skin/subcutis at the inoculation site (without ulcer in the glandular form); occasional systemic/typhoidal spread if untreated; rare seeding of prosthetic joints ([PMID: 37209668](https://pubmed.ncbi.nlm.nih.gov/37209668/)).
- **Body system:** Lymphatic/immune system (UBERON:0002405 immune system; UBERON:0006558 lymphatic part of the lymphatic system).
- **Tissue level:** Lymphoid tissue; granulomatous inflammation of nodal parenchyma.
- **Cell populations:** Macrophages (CL:0000235), neutrophils (CL:0000775), dendritic cells (CL:0000451), epithelioid histiocytes and multinucleated giant cells, T lymphocytes (CL:0000084).
- **Subcellular level:** *Francisella*-containing phagosome and host **cytosol** (GO:0005829) — the replicative niche after phagosomal escape.
- **Lateralization:** Typically **unilateral**, reflecting the single inoculation/drainage territory; asymmetric.

---

## Section 8 — Temporal Development

- **Onset:** Acute; incubation typically **3–5 days (range 1–21)** post-exposure, with abrupt fever, chills, malaise, headache, myalgia plus regional lymphadenopathy ([PMID: 18755386](https://pubmed.ncbi.nlm.nih.gov/18755386/), [PMID: 26738841](https://pubmed.ncbi.nlm.nih.gov/26738841/)).
- **Age of onset:** Any age; exposure-driven (bimodal US peaks — children 5–9, men >55).
- **Progression / course:** Generally **self-limited with treatment**; without appropriate therapy the node may enlarge, become fluctuant/suppurative, and fistulize. A prolonged course with painful lymphadenopathy persisting **>5 months** has been documented ([PMID: 19551605](https://pubmed.ncbi.nlm.nih.gov/19551605/)).
- **Suppuration/surgery:** Fluctuant/suppurative nodes require FNA or surgical drainage/excision in **~39–65%** of cases ([PMID: 23104256](https://pubmed.ncbi.nlm.nih.gov/23104256/), [PMID: 42601640](https://pubmed.ncbi.nlm.nih.gov/42601640/)).
- **Remission:** Treatment-induced with early appropriate antibiotics; relapse risk higher with bacteriostatic doxycycline than with aminoglycosides.
- **Critical period:** The therapeutic window is early — before node suppuration; early treatment significantly improves success ([PMID: 23104256](https://pubmed.ncbi.nlm.nih.gov/23104256/)).

---

## Section 9 — Inheritance and Population

**Inheritance:** **NOT APPLICABLE** — infectious disease with no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency.

**Epidemiology.**
- Rare, reportable zoonosis. In the US 2001–2010, **1,208 cases** were reported (median 126.5/yr, range 90–154; ~0.04/100,000/yr); incidence highest among **children aged 5–9 years and men aged >55 years** ([PMID: 24280916](https://pubmed.ncbi.nlm.nih.gov/24280916/)).
- Reported from all US states except Hawaii.
- **Recent re-emergence (2024–2025):** Austria 117, Slovenia 38, France 150, Spain (Castile-León) 206 cases; US reported 220 cases in 2024 ([PMID: 42641375](https://pubmed.ncbi.nlm.nih.gov/42641375/)). An unusual 2024 increase was documented in Alsace, France ([PMID: 40907418](https://pubmed.ncbi.nlm.nih.gov/40907418/)).
- **Geography:** Confined to the Northern Hemisphere (North America, Europe, northern Asia); absent from the Southern Hemisphere ([PMID: 1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/)).
- **Sex ratio:** Male predominance in tick-associated regions (e.g., Alsace 7M/3F, mean age 52), but female predominance in some waterborne/oropharyngeal outbreaks (Central Anatolia ~60% female) — reflecting exposure, not biology ([PMID: 40907418](https://pubmed.ncbi.nlm.nih.gov/40907418/), [PMID: 23104256](https://pubmed.ncbi.nlm.nih.gov/23104256/)).

---

## Section 10 — Diagnostics

**Diagnosis relies on serology and PCR; culture is insensitive and hazardous.**

| Test | Utility / threshold | Notes |
|---|---|---|
| **Serology (microagglutination, MAT)** | Positive ≥1/160; seroconversion in paired sera | Mainstay; may be negative early ([PMID: 22090310](https://pubmed.ncbi.nlm.nih.gov/22090310/)) |
| **PCR** (targets *tul4*, *fopA*; RD1 for subspecies) | Detected DNA in **75%** vs culture **62%** of confirmed ulceroglandular cases | Valuable early, before seroconversion ([PMID: 10618057](https://pubmed.ncbi.nlm.nih.gov/10618057/)) |
| **Culture** | Typically only ~10% positive | Requires BSL-3; hazardous ([PMID: 37209668](https://pubmed.ncbi.nlm.nih.gov/37209668/)) |
| **FNA cytology of node** | Suppurative granulomatous inflammation; provides material for PCR/culture | Cytology alone nonspecific ([PMID: 23763361](https://pubmed.ncbi.nlm.nih.gov/23763361/)) |
| **Histopathology** | Necrotizing/suppurative granulomatous lymphadenitis | Epithelioid histiocytes, giant cells ([PMID: 23763361](https://pubmed.ncbi.nlm.nih.gov/23763361/)) |
| **MALDI-TOF / molecular ID** | Species identification from isolates | Used in prosthetic-joint cases ([PMID: 37209668](https://pubmed.ncbi.nlm.nih.gov/37209668/)) |

PCR outperforms culture, and tularemia can proceed without seroconversion, making PCR valuable early ([PMID: 10618057](https://pubmed.ncbi.nlm.nih.gov/10618057/)).

**Genetic / omics diagnostics:** Not applicable for host diagnosis (no human genetic test). Pathogen molecular subtyping (multiplex real-time PCR distinguishing A.I, A.II, B, novicida) is used epidemiologically ([PMID: 22859584](https://pubmed.ncbi.nlm.nih.gov/22859584/)).

**Clinical criteria & differential.** Diagnosis rests on clinical suspicion (endemic exposure + regional lymphadenopathy + beta-lactam non-response) confirmed serologically/molecularly. **Differential diagnosis:** bacterial lymphadenitis, cat-scratch disease, mycobacterial (tuberculous) lymphadenitis, plague, toxoplasmosis, lymphoma, and other causes of suppurative/granulomatous cervical lymphadenitis. Initial misdiagnosis is common — **9 of 10 cases** in an Alsace series were not initially suspected ([PMID: 40907418](https://pubmed.ncbi.nlm.nih.gov/40907418/)); severe glandular tularemia can mimic glandular tuberculosis ([PMID: 19801257](https://pubmed.ncbi.nlm.nih.gov/19801257/)).

**Screening:** No asymptomatic population/newborn/carrier screening (infectious, non-genetic).

---

## Section 11 — Outcome / Prognosis

- **Case fatality with treatment is very low.** In the 870-case systematic review, fatality among patients treated with aminoglycosides (n=452), fluoroquinolones (n=339), or tetracyclines (n=419) was **0.7%, 0.9%, and 1.2%**, respectively ([PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)). Type B glandular disease is rarely fatal.
- **Untreated tularemia overall** can reach up to **30% mortality** (driven by severe forms, not localized glandular disease) ([PMID: 42641375](https://pubmed.ncbi.nlm.nih.gov/42641375/)).
- **Morbidity:** Node suppuration, fistula, need for surgical drainage/excision (~39–65% of cases); prolonged courses; relapse (higher with doxycycline).
- **Prognostic factors:** Early vs delayed treatment (success significantly higher with early treatment); elevated ESR/CRP predicts therapeutic failure (30.9% failure in one series); comorbidity/immunosuppression worsens outcome ([PMID: 23104256](https://pubmed.ncbi.nlm.nih.gov/23104256/), [PMID: 19801257](https://pubmed.ncbi.nlm.nih.gov/19801257/)).
- **Recovery:** Excellent with appropriate, timely antibiotics; complete recovery is the norm for glandular type B disease.

---

## Section 12 — Treatment

**First-line therapy is aminoglycosides, fluoroquinolones, or tetracyclines.**

| Class | Examples | Role | NCIT (suggested) |
|---|---|---|---|
| Aminoglycosides | Streptomycin, gentamicin | Classic first-line; bactericidal; low relapse | Gentamicin C1010; Streptomycin C777 |
| Fluoroquinolones | Ciprofloxacin, levofloxacin | First-line (2025 CDC); oral; effective even in severe type B | Ciprofloxacin C376; Levofloxacin C1615 |
| Tetracyclines | Doxycycline | First-line oral option; **bacteriostatic → higher relapse** | Doxycycline C509 |
| **Beta-lactams** | Penicillins, cephalosporins | **INEFFECTIVE — intrinsic resistance** | — |

- 2025 CDC guidelines establish **fluoroquinolones and doxycycline as first-line** therapeutic options ([PMID: 42641375](https://pubmed.ncbi.nlm.nih.gov/42641375/), [PMID: 41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/)).
- Fluoroquinolones are effective even in **severe respiratory type B** tularemia, with rapid defervescence and 30-day mortality of 1.5% ([PMID: 38294118](https://pubmed.ncbi.nlm.nih.gov/38294118/)).
- **Beta-lactams fail** — glandular/oropharyngeal cases repeatedly relapse on beta-lactams before diagnosis ([PMID: 39295179](https://pubmed.ncbi.nlm.nih.gov/39295179/), [PMID: 22090310](https://pubmed.ncbi.nlm.nih.gov/22090310/)).
- **Surgical/interventional:** Fluctuant/suppurative nodes often require FNA or surgical drainage/excision (39–65% of cases); prosthetic-joint infections require surgery plus prolonged antimicrobials ([PMID: 23104256](https://pubmed.ncbi.nlm.nih.gov/23104256/), [PMID: 37209668](https://pubmed.ncbi.nlm.nih.gov/37209668/)).
- **Experimental:** Inhaled liposomal ciprofloxacin protected against lethal tularemia in the common marmoset ([PMID: 41416830](https://pubmed.ncbi.nlm.nih.gov/41416830/)).
- **Pharmacogenomics:** Not applicable (no genotype-guided dosing established for this indication).

**Treatment strategy:** Start empirical anti-tularemia therapy on clinical suspicion in endemic settings; early treatment yields <1.5% fatality and rapid defervescence, whereas delay predicts failure ([PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/), [PMID: 23104256](https://pubmed.ncbi.nlm.nih.gov/23104256/)).

---

## Section 13 — Prevention

**No licensed human vaccine exists**, despite >70 years of research; control depends on preventive measures ([PMID: 42641375](https://pubmed.ncbi.nlm.nih.gov/42641375/), [PMID: 25413334](https://pubmed.ncbi.nlm.nih.gov/25413334/)).

- **Primary prevention:** Avoid tick/insect bites (repellents, protective clothing, tick checks); wear gloves when handling wild animals/carcasses (especially lagomorphs/rodents); avoid mowing over animal carcasses (aerosol risk); cook game meat thoroughly; ensure safe water ([PMID: 15677845](https://pubmed.ncbi.nlm.nih.gov/15677845/)).
- **Post-exposure prophylaxis (PEP):** Doxycycline or ciprofloxacin (oral) after high-risk exposures (lab accidents, known bioterrorism release); historically streptomycin/gentamicin/doxycycline/ciprofloxacin ([PMID: 15677845](https://pubmed.ncbi.nlm.nih.gov/15677845/)). The 2025 CDC report provides updated evidence-based treatment and PEP recommendations for naturally acquired and bioterrorism-related tularemia ([PMID: 41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/)).
- **Infection control:** Standard precautions suffice — **no person-to-person transmission**, so no isolation required ([PMID: 15677845](https://pubmed.ncbi.nlm.nih.gov/15677845/)).
- **Vaccine candidates (experimental):** The Live Vaccine Strain (LVS, attenuated holarctica) remains **unlicensed**, does not protect against high inhalational type A doses, and has poorly understood attenuation ([PMID: 33970545](https://pubmed.ncbi.nlm.nih.gov/33970545/)). Subunit candidates — glucan-particle LPS + FTT0814 ([PMID: 38713688](https://pubmed.ncbi.nlm.nih.gov/38713688/)) and TMV-delivered OmpA/DnaK/Tul4 ([PMID: 26098553](https://pubmed.ncbi.nlm.nih.gov/26098553/)) — confer partial protection in rat/mouse models.
- **Genetic counseling / carrier screening:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy of pathogen:** *Francisella tularensis* (NCBI Taxon 263).
- **Host range:** Tularemia has been reported in **>250 animal species** (mammals, birds, fish, amphibians, arthropods, protozoa) ([PMID: 1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/)).
- **Two natural lifecycles / reservoirs:**
  - **Type A (terrestrial):** cottontail rabbits (*Sylvilagus* spp.) and ticks as main reservoirs.
  - **Type B (water-borne):** aquatic rodents — muskrats (*Ondatra zibethicus*), beaver (*Castor canadensis*) in North America; ground voles (*Arvicola terrestris*) in Eurasia ([PMID: 1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/)).
- In Europe, **hares (*Lepus* spp.)** — especially the European brown hare (*Lepus europaeus*) — are most frequently affected and are the key source of human holarctica infections, though not a true maintenance reservoir ([PMID: 23517149](https://pubmed.ncbi.nlm.nih.gov/23517149/)).
- **Vectors:** Arthropods (ticks, deer flies, mosquitoes) are the main transmission vectors; small mammals (rabbits, hares, muskrats) serve as reservoir hosts ([PMID: 18755386](https://pubmed.ncbi.nlm.nih.gov/18755386/)).
- **Zoonotic potential:** High — this is fundamentally a zoonosis; **no human-to-human transmission** occurs.
- **Cross-species / vector competence:** *Dermacentor* spp. are competent vectors, whereas *Ixodes scapularis* is not; cell-line studies show *F. novicida* replicates more productively in *Dermacentor* (DAE100) than *Ixodes* (ISE6) cells, underpinning ecological vector differences ([PMID: 30140074](https://pubmed.ncbi.nlm.nih.gov/30140074/)).

---

## Section 15 — Model Organisms

- **Mammalian models:** Mouse (BALB/c, C57BL/6) and Fischer 344 rat are standard, challenged with attenuated **LVS** or virulent **SCHU S4** (subsp. *tularensis*) ([PMID: 35077486](https://pubmed.ncbi.nlm.nih.gov/35077486/), [PMID: 30054549](https://pubmed.ncbi.nlm.nih.gov/30054549/), [PMID: 38713688](https://pubmed.ncbi.nlm.nih.gov/38713688/)). The common marmoset has been used for inhalational challenge and therapeutic testing ([PMID: 41416830](https://pubmed.ncbi.nlm.nih.gov/41416830/)).
- **Surrogate species:** *F. novicida* is a genetically tractable, lower-biosafety surrogate for mechanistic studies ([PMID: 35077486](https://pubmed.ncbi.nlm.nih.gov/35077486/)).
- **Genetic models:** Bacterial gene-deletion/transposon mutants (Δ*clpB*, Δ*pilO*, Δ*opiA*, *FTL_0883*/*FTT_0615c*) dissect virulence; host inflammasome knockouts (*Aim2⁻/⁻*, *Nlrp3⁻/⁻*) probe innate immunity ([PMID: 30054549](https://pubmed.ncbi.nlm.nih.gov/30054549/), [PMID: 30057173](https://pubmed.ncbi.nlm.nih.gov/30057173/), [PMID: 21670171](https://pubmed.ncbi.nlm.nih.gov/21670171/), [PMID: 34690967](https://pubmed.ncbi.nlm.nih.gov/34690967/), [PMID: 33875472](https://pubmed.ncbi.nlm.nih.gov/33875472/)).
- **In vitro:** Human/murine macrophage, neutrophil, and dendritic-cell infection models; tick cell lines (DAE100, ISE6) for vector-competence studies ([PMID: 22357630](https://pubmed.ncbi.nlm.nih.gov/22357630/), [PMID: 19841074](https://pubmed.ncbi.nlm.nih.gov/19841074/), [PMID: 30140074](https://pubmed.ncbi.nlm.nih.gov/30140074/)).
- **Phenotype recapitulation:** Rodent models reproduce intracellular replication, dissemination, granulomatous pathology, and lethality; SCHU S4 models severe type A disease, LVS models attenuated type B. **Limitation:** these models emphasize pneumonic/systemic lethality rather than the specific localized *glandular* lymphadenitis phenotype, which is best characterized from human case series.

---

## Mechanistic Model / Interpretation

```
 Arthropod bite / animal-carcass contact  (inoculum ~10 organisms)
                     │
                     ▼
   Local deposition in skin/subcutis  ── NO ULCER ──►  GLANDULAR form
   (with ulcer  ──►  ULCEROGLANDULAR form)                │
                     │                                     │
                     ▼                                     │
   Uptake by macrophages / DCs (phagosome)                 │
                     │                                     │
                     ▼   OpiA (PI3K), ClpB, PilO, T6SS      │
   Phagosomal ESCAPE ─────────────► Cytosolic REPLICATION   │
                     │                                     │
                     ▼   (LPS weakly sensed by TLR4;        │
   Innate EVASION     neutrophil apoptosis delayed;         │
                     │  DC cytokines suppressed unless CD14)│
                     ▼                                     │
   Lymphatic drainage to REGIONAL LYMPH NODE ◄─────────────┘
                     │
                     ▼   AIM2/NLRP3 inflammasome; Th1 (IFN-γ/IL-17)
   Necrotizing / suppurative GRANULOMATOUS LYMPHADENITIS
                     │
                     ▼
   Clinical: acute fever + tender regional lymphadenopathy
   (± suppuration/fistula → FNA/surgery in 39–65%)
                     │
        ┌────────────┴─────────────┐
        ▼                          ▼
  Early appropriate Abx       Delayed dx (β-lactam failure)
  (aminoglycoside/FQ/         → suppuration, surgery,
   doxycycline)                 therapeutic failure (30.9%)
        │                          │
        ▼                          ▼
  Fatality <1.5%,            Prolonged morbidity;
  rapid defervescence        untreated overall up to 30%
```

The unifying synthesis (Finding F013) is that **diagnostic delay driven by beta-lactam failure is the chief modifiable determinant of glandular tularemia morbidity**. The organism's intrinsic beta-lactam resistance, frequent culture-negativity, and low clinical familiarity conspire to delay correct diagnosis. Because intrinsic lethality of type B glandular disease is low, the dominant morbidity driver is **time-to-correct-diagnosis**, not disease severity per se. The actionable lever is clinical suspicion (endemic exposure + regional lymphadenopathy + beta-lactam non-response) confirmed by MAT (≥1/160) and/or PCR on node aspirate.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/) | *Systematic Review: Clinical Features, Treatment, Outcomes 1993–2023* | Glandular as major form; fatality by drug class (0.7/0.9/1.2%) |
| [42641375](https://pubmed.ncbi.nlm.nih.gov/42641375/) | *Tularemia: a re-emerging zoonosis* | Low infectious dose, 30% untreated mortality, 2025 CDC first-line therapy, no vaccine, re-emergence data |
| [42601640](https://pubmed.ncbi.nlm.nih.gov/42601640/) | *Tick-borne tularaemia in children* | Arthropod-borne → glandular/ulceroglandular; suppuration/surgery |
| [16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/) | *Epidemiologic/molecular analysis US 1964–2004* | Type A vs B differ in populations/site/geography |
| [19251856](https://pubmed.ncbi.nlm.nih.gov/19251856/) | *Phylogeography of F. tularensis* | Circumpolar type B; clonal radiation |
| [23517149](https://pubmed.ncbi.nlm.nih.gov/23517149/) | *German isolates from brown hares* | European human infection from *Lepus europaeus* |
| [30057173](https://pubmed.ncbi.nlm.nih.gov/30057173/) | *PI3-kinase effector OpiA* | Phagosomal escape mechanism |
| [30054549](https://pubmed.ncbi.nlm.nih.gov/30054549/) | *ClpB mutants* | T6SS function/intracellular replication |
| [35077486](https://pubmed.ncbi.nlm.nih.gov/35077486/) | *PilO virulence determinant* | Adherence/escape/virulence; mouse model |
| [34690967](https://pubmed.ncbi.nlm.nih.gov/34690967/) | *Nlrp3 increases susceptibility* | Inflammasome host susceptibility |
| [23763361](https://pubmed.ncbi.nlm.nih.gov/23763361/) | *Cytopathology of cervical lymphadenitis* | Granulomatous/suppurative histology; FNA role |
| [10618057](https://pubmed.ncbi.nlm.nih.gov/10618057/) | *PCR vs culture* | PCR 75% vs culture 62% sensitivity |
| [22090310](https://pubmed.ncbi.nlm.nih.gov/22090310/) | *Central Anatolia cases* | MAT ≥1/160; beta-lactam failure |
| [23104256](https://pubmed.ncbi.nlm.nih.gov/23104256/) | *Tularemia in central Anatolia* | Early treatment better; 30.9% failure; drainage 39–65% |
| [22357630](https://pubmed.ncbi.nlm.nih.gov/22357630/) | *Neutrophil apoptosis inhibition* | Innate immune evasion |
| [19841074](https://pubmed.ncbi.nlm.nih.gov/19841074/) | *CD14 and DC evasion* | CD14-dependent detection; DC cytokine evasion |
| [24280916](https://pubmed.ncbi.nlm.nih.gov/24280916/) | *Tularemia — US 2001–2010* | 1,208 cases; bimodal age/sex |
| [1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/) | *The ecology of tularaemia* | >250 species; two lifecycles; Northern Hemisphere |
| [18755386](https://pubmed.ncbi.nlm.nih.gov/18755386/) | *Tularemia* (review) | Vectors/reservoirs; acute onset |
| [33970545](https://pubmed.ncbi.nlm.nih.gov/33970545/) | *Innate immune kinetics / chloride transporter* | LVS limitations as vaccine/model |
| [38713688](https://pubmed.ncbi.nlm.nih.gov/38713688/) | *Glucan-particle subunit vaccine* | Partial protection; F344 rat/SCHU S4 model |
| [15677845](https://pubmed.ncbi.nlm.nih.gov/15677845/) | *Bichat guidelines* | Seven clinical forms; PEP agents; no person-to-person spread |
| [41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/) | *CDC 2025 treatment/PEP recommendations* | Updated treatment/PEP guidance |
| [40907418](https://pubmed.ncbi.nlm.nih.gov/40907418/) | *Alsace 2024 increase* | 9/10 not initially suspected; misdiagnosis |
| [19801257](https://pubmed.ncbi.nlm.nih.gov/19801257/) | *Tularaemia mimicking glandular TB on adalimumab* | Immunosuppression as severity factor; histology |
| [38294118](https://pubmed.ncbi.nlm.nih.gov/38294118/) | *Severe respiratory type B, fluoroquinolones* | FQ effective in severe disease |
| [40466250](https://pubmed.ncbi.nlm.nih.gov/40466250/) | *German case series* | (Ulcero-)glandular most common; misdiagnosis; FQ/doxy resolution |

---

## Limitations and Knowledge Gaps

1. **Form-specific data are limited.** Much evidence pools glandular with ulceroglandular disease; pure-glandular-only epidemiology, natural history, and QoL metrics are sparse.
2. **No disease-specific QoL instruments** (EQ-5D/SF-36/PROMIS) have been applied to tularemia.
3. **Mechanistic studies emphasize pneumonic/systemic lethality** (mouse/rat SCHU S4/LVS) rather than the localized glandular lymphadenitis phenotype; some mechanistic steps (e.g., precise inflammasome contribution to nodal granuloma formation) are **inferred** from systemic models.
4. **Culture-based data underrepresent true incidence** given ~10% culture positivity; surveillance likely undercounts.
5. **No human genetic susceptibility work** — whether host immunogenetic variation modulates glandular vs other forms is essentially unstudied.
6. **Vaccine gap:** No licensed human vaccine; LVS attenuation mechanism remains poorly defined.

## Proposed Follow-up Actions

1. **Form-stratified cohort analysis:** Extract glandular-only cases from the 870-case systematic review and national registries to quantify pure-glandular incidence, suppuration rate, relapse, and time-to-diagnosis.
2. **Diagnostic-delay intervention study:** Test whether endemic-area clinician decision aids (regional lymphadenopathy + beta-lactam non-response prompt) reduce time-to-appropriate-therapy and suppuration rates.
3. **Doxycycline vs fluoroquinolone relapse comparison** in localized glandular disease, powered for relapse as the primary endpoint.
4. **Node-localized mechanistic model:** Develop an intradermal/regional-node challenge model to study inflammasome (AIM2/NLRP3) and Th1 contributions specifically to granulomatous lymphadenitis.
5. **Host immunogenetics:** Explore whether TLR4/CD14/inflammasome polymorphisms influence clinical form or severity.
6. **Advance subunit vaccine candidates** (glucan-particle LPS+FTT0814; TMV OmpA/DnaK/Tul4) toward challenge studies against type A.

---

*Report compiled from 13 confirmed findings and 46 reviewed papers over 5 investigation iterations. Evidence classes: human clinical (case series, systematic reviews, surveillance), model organism (mouse/rat/marmoset), in vitro (macrophage/neutrophil/DC/tick-cell), and computational/phylogenomic.*


## Artifacts

- [OpenScientist final report](Glandular_Tularemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Glandular_Tularemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 39 |
| On topic | 25 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 18 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002716` (1 mention) - the report calls it "Clinical sign"; HP calls it **Lymphadenopathy**
- `HP:0001945` (1 mention) - the report calls it "Symptom/sign"; HP calls it **Fever**
- `HP:0003688` (1 mention) - the report calls it "Symptom"; HP calls it **Cytochrome C oxidase-negative muscle fibers**
- `HP:0002315` (1 mention) - the report calls it "Symptom"; HP calls it **Headache**
- `HP:0003326` (1 mention) - the report calls it "Symptom"; HP calls it **Myalgia**
- `HP:0025145` (1 mention) - the report calls it "Symptom"; HP calls it **Rigors**
- `GO:0005829` (1 mention) - the report calls it "cytosol", "Subcellular level:** *Francisella*-containing phagosome and host **cytosol"; GO calls it **cytosol**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0052167` (1 mention) - the report calls it "modulation by symbiont of host innate immune response"; GO calls it **symbiont-mediated perturbation of host innate immune response**, and lists "modulation of host innate immune response" among its other names
- `GO:0030682` (1 mention) - the report calls it "evasion of host defenses"; GO calls it **symbiont-mediated perturbation of host defenses**, and lists "evasion of host defence response" among its other names
- `CL:0000235` (2 mentions) - the report calls it "macrophage", "Cell populations:** Macrophages"; CL calls it **macrophage**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000235` - called "macrophage", "Cell populations:** Macrophages"
- `GO:0005829` - called "cytosol", "Subcellular level:** *Francisella*-containing phagosome and host **cytosol"