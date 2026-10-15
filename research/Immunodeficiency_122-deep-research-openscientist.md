---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-01T20:16:19.422054'
end_time: '2026-10-01T20:43:23.878056'
duration_seconds: 1624.46
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 122
  mondo_id: MONDO:0971151
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
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 4
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 70
  verified: 68
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0971151
    reported_labels:
    - Monarch
    ontology_label: immunodeficiency 122
  - term_id: NCIT:C603
    reported_labels:
    - Immunoglobulin Therapy
    ontology_label: Isotretinoin
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
artifacts:
- filename: final_report.html
  path: Immunodeficiency_122-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_122-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: notes.md
  path: Immunodeficiency_122-deep-research-openscientist_artifacts/notes.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist notes
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 122
- **MONDO ID:** MONDO:0971151 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 122** covering all of the
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

# Immunodeficiency 122 (IMD122) — Comprehensive Disease Characterization

**Disease:** Immunodeficiency 122 (IMD122)
**Causal gene:** *POLD3* (DNA polymerase delta 3, accessory subunit)
**Identifiers:** OMIM:620869 · MONDO:0971151 · DOID:0061088 · MedGen C5935632 (CUI) · UMLS C5935632
**Evidence base:** Ultra-rare Mendelian disorder described in only two unrelated patients (2023). All clinical content is derived from **individual patient reports** (case-level), not aggregated registries, plus in vitro functional and mouse model data.

---

## Summary (Answer to the Research Question)

Immunodeficiency 122 is an **ultra-rare autosomal-recessive syndromic combined immunodeficiency** caused by **biallelic hypomorphic missense variants in *POLD3***, which encodes the p66/p68 accessory, complex-stabilizing subunit of **DNA polymerase δ** (and a shared subunit of translesion polymerase ζ). Reduced polymerase δ function produces **replicative stress, defective S-phase progression, and accumulation of DNA double-strand breaks**, which impair proliferation and V(D)J/TCR recombination in lymphoid progenitors—producing **severe combined immunodeficiency (SCID), frequently presenting as Omenn syndrome**—and injure other highly proliferative lineages, causing **neurodevelopmental delay, sensorineural hearing loss, and ectodermal anomalies**. Onset is neonatal/congenital with a severe course; hematopoietic stem cell transplantation can reconstitute immunity but does not correct the cell-intrinsic replication defect in non-hematopoietic tissues.

---

## 1. Disease Information

- **Overview:** IMD122 is a monogenic inborn error of immunity in the category of **combined immunodeficiencies with syndromic/associated features** (per IUIS classification). It combines a profound T-cell (± B/NK) defect with neurodevelopmental, auditory, and ectodermal manifestations due to a defect in genome replication/maintenance.
- **Key identifiers:**
  - OMIM phenotype: **620869** (Immunodeficiency 122)
  - MONDO: **MONDO:0971151**
  - DOID: **0061088**; MedGen/UMLS: **C5935632**
  - Orphanet: no dedicated code identified (newly described; would fall under "Combined immunodeficiency")
  - ICD-11: maps to **4A00** (Primary immunodeficiencies) / ICD-10 **D81.x** (combined immunodeficiencies)
  - MeSH: no specific descriptor; closest = *Severe Combined Immunodeficiency* (D016511); phenotype also = *Omenn syndrome*
- **Synonyms / alternative names:** IMD122; **POLD3 deficiency**; DNA polymerase delta 3 deficiency; syndromic SCID due to POLD3; autosomal-recessive polymerase δ (PolD) deficiency (POLD3 type); POLD3-related Omenn syndrome.
- **Evidence source:** Individual-patient (case report) level — two probands total (PMID 37030525; PMID 38099988).

---

## 2. Etiology

- **Causal factor (genetic):** Biallelic (homozygous) **pathogenic missense variants in *POLD3*** (AR). Both reported patients were offspring of **consanguineous unions**.
  - *"Here we report a homozygous POLD3 variant (NM_006591.3; p.Ile10Thr) in a Lebanese patient, the product of a consanguineous family, presenting with a syndromic severe combined immunodeficiency (SCID)"* (PMID 37030525).
- **Genetic risk factors:** The causal variants themselves (p.Ile10Thr; p.K373T). No susceptibility loci or modifier genes identified (too few cases). **Consanguinity** is the principal risk context. POLD3 is strongly **LoF-intolerant** (gnomAD pLI 0.994, LOEUF 0.48), so only **hypomorphic missense** alleles—retaining partial function—cause viable disease; complete LoF is presumed lethal (mouse null embryonic-lethal, PMID 29447390).
- **Environmental risk factors:** None established; disease is fully genetically determined. Infectious exposures are **consequences** (opportunistic infection due to immunodeficiency), not causes.
- **Protective factors:** None reported (genetic or environmental). Not applicable at the population level given rarity.
- **Gene–environment interactions:** Not characterized. Mechanistically, exogenous genotoxic/replication stressors (UV, chemotherapeutics, oxidative stress) would be predicted to aggravate the underlying replication defect (inferred, not demonstrated).

---

## 3. Phenotypes

Onset **neonatal/congenital**, severity **severe**, course **progressive**. Frequencies are qualitative (n=2). HPO terms derived from OMIM:620869 annotation.

**Immune / laboratory abnormalities:**
- Severe combined immunodeficiency — **HP:0000958**
- Decreased total T cells — **HP:0500093**; decreased naive CD4+ (**HP:0001744**) and naive CD8+ (**HP:0005359**) proportions; oligoclonal T-cell expansion — **HP:0010975**
- Reduced NK cell count — **HP:0000407**; abnormal B-cell count — **HP:0410243**; decreased unswitched memory B cells — **HP:0040218**
- Decreased IgG — **HP:0001019**; abnormal IgM — **HP:0004315**; **increased IgE — HP:0002716**; eosinophilia — **HP:0001999**
- Thymic aplasia/hypoplasia — **HP:0004430**

**Omenn-syndrome features (clinical signs/physical):**
- Erythroderma — **HP:0410377**; alopecia — **HP:0008404**; lymphadenopathy — **HP:0002110**; hepatomegaly — **HP:0004429**; splenomegaly — **HP:0002783**

**Infections (symptoms):** recurrent viral — **HP:0002788**; bacterial — **HP:0001270**; upper (**HP:0001263**) and lower (**HP:0032126**) respiratory infections; bronchiectasis — **HP:0002007**

**Neurodevelopmental (behavioral/developmental):** global developmental delay — **HP:0001596**; motor delay — **HP:0002718**; (progressive neurological regression in the Omenn patient)

**Sensory:** sensorineural hearing impairment — **HP:0001880**

**Craniofacial / ectodermal (physical):** frontal bossing — **HP:0003212**; abnormal facial shape — **HP:0410378**; enamel hypoplasia — **HP:0011968**; nail dystrophy — **HP:0031430**; dry skin — **HP:0005403**

**Feeding/allergy:** feeding difficulties — **HP:0002240**; food allergy — **HP:0006297**

**Quality-of-life impact:** profound—life-threatening infections, failure to thrive, developmental disability, deafness; without HSCT, SCID is uniformly fatal in infancy. Formal QoL instruments (EQ-5D/SF-36) not applicable/available.

---

## 4. Genetic / Molecular Information

- **Causal gene:** ***POLD3*** — HGNC:20932; NCBI Gene **10714**; Ensembl **ENSG00000077514**; cytoband **11q13.4** (GRCh38 chr11:74,493,851–74,669,117, + strand); transcript **NM_006591.3**; protein **UniProt Q15054** (466 aa, "DNA polymerase delta subunit 3", p66/p68).
- **Pathogenic variants (both germline, homozygous, missense):**
  | Variant (cDNA/protein) | Patient | Classification | Consequence |
  |---|---|---|---|
  | NM_006591.3:c.29T>C, **p.Ile10Thr** | Lebanese, syndromic SCID (PMID 37030525) | Pathogenic (AR) | Abolishes POLD3 **and** POLD1/POLD2 protein expression → complex destabilization |
  | **c.1118A>C, p.Lys373Thr (p.K373T)** | Omenn syndrome (PMID 38099988) | Pathogenic (AR) | Normal PolD subunit levels but defective function → S-phase defect, ↑dsDNA breaks (rescued by WT POLD3) |
- **Variant type/class:** missense (both). No nonsense/frameshift/splice/structural variants reported (consistent with LoF intolerance).
- **Allele frequency:** both variants are **private/ultra-rare**, essentially absent from gnomAD; gene-level LoF constraint pLI **0.994**, LOEUF **0.48**, LoF o/e **0.33** (missense unconstrained, mis_z 0.76).
- **Somatic vs germline:** **germline**.
- **Functional consequence:** **loss/reduction of function (hypomorphic)**. p.Ile10Thr → destabilization of the entire Pol δ heterocomplex; p.K373T → intrinsic functional impairment with preserved assembly.
- **Modifier genes:** none identified.
- **Epigenetic information:** none reported for this disorder.
- **Chromosomal abnormalities:** none (point mutations only). *Downstream*, POLD3 deficiency causes acquired genomic instability (chromosome breaks, micronuclei, aneuploidy — shown in mouse/cell models, PMID 29447390).

---

## 5. Environmental Information

- **Environmental factors:** none causative. IMD122 is a monogenic disorder.
- **Lifestyle factors:** not applicable (congenital, infantile-lethal).
- **Infectious agents:** not causal but central to morbidity—patients suffer **opportunistic and recurrent viral, bacterial, and respiratory infections** secondary to the immunodeficiency (HP:0002788/HP:0001270/HP:0032126). Typical SCID pathogens (inferred from SCID literature): *Pneumocystis jirovecii*, CMV, adenovirus, RSV, candida; live-vaccine organisms (BCG, rotavirus) are contraindicated.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic hypomorphic missense variant in *POLD3*** (p.Ile10Thr or p.K373T) → **reduced functional DNA polymerase δ**, either by destabilizing/degrading the POLD1–POLD2–POLD3(–POLD4) complex (p.Ile10Thr abolishes POLD1/POLD2/POLD3 expression) or by impairing complex function with preserved subunit levels (p.K373T). *(Demonstrated in vitro.)*
2. Reduced Pol δ activity → **impaired high-fidelity DNA replication** (leading- and lagging-strand synthesis, loss of PCNA-stimulated processivity) and reduced DNA repair capacity. *(Demonstrated — UniProt-annotated functions; Conde POLD1/POLD2 data PMID 31449058.)*
3. → **Replicative stress: defective S-phase entry/progression** and **accumulation of DNA double-strand breaks (γH2AX foci)**; the defect is **rescued by wild-type POLD3**, establishing causality. *(Demonstrated — PMID 38099988; analogous mouse data PMID 29447390: extended S-phase, telomere loss, chromosome breaks, micronuclei, aneuploidy, DDR via ATR/ATM/53BP1/RIF1.)*
4a. **Immune branch:** replication stress plus a **defect in the early stages of TCR recombination** → failure of thymocyte proliferation/V(D)J recombination → **profound naive T-cell lymphopenia with restricted/oligoclonal TCR repertoire** → **SCID**; residual autoreactive oligoclonal T-cell expansion with Th2 skewing → **Omenn syndrome** (erythroderma, eosinophilia, high IgE, hepatosplenomegaly, lymphadenopathy). *(Demonstrated — PMID 38099988.)*
4b. **Neurodevelopmental branch:** replication stress in neural progenitors → impaired neurogenesis → **global developmental delay / progressive neurological regression**. *(Inferred by analogy to POLD1/POLD2; PMID 31449058.)*
4c. **Auditory/ectodermal branch:** replication stress in cochlear and ectodermal (skin, hair, nail, dental enamel) progenitors → **sensorineural hearing loss and ectodermal dysplasia-like features**. *(Inferred.)*
5. → **Clinical syndrome:** neonatal-onset syndromic SCID/Omenn with neurodevelopmental delay, deafness, and ectodermal/craniofacial anomalies; death in infancy/early childhood without—and sometimes despite—HSCT.

**Supporting detail:**
- **Molecular pathways/processes:** DNA replication (**GO:0006260**), DNA repair / double-strand-break repair (**GO:0006302**), replication-stress / DNA-damage response via ATR–ATM–53BP1–RIF1, cell-cycle S-phase (**GO:0000082**), V(D)J recombination (**GO:0033151**), T-cell differentiation (**GO:0030217**), apoptosis (**GO:0006915**). Reactome: "DNA strand elongation," "Polymerase switching," "Lagging strand synthesis." KEGG: *DNA replication* (hsa03030), *Base/Nucleotide excision repair*, *Mismatch repair*.
- **Protein dysfunction:** loss/reduction of function of the Pol δ accessory subunit; POLD3 also co-forms **DNA polymerase ζ** (translesion synthesis, with REV3L/REV7) and participates in break-induced replication/homologous recombination—so its loss broadly compromises genome maintenance.
- **Cellular processes:** cell-cycle dysregulation (extended/arrested S phase), genomic instability, apoptosis of stressed progenitors.
- **Immune involvement:** this is a primary **immunodeficiency** (combined T/B/NK), not autoimmunity per se—though Omenn physiology produces immune dysregulation/Th2 inflammation.
- **Cell types (CL):** T cells (**CL:0000084**), naive T cell (**CL:0000898**), thymocyte (**CL:0000893**), double-positive thymocyte (**CL:0000809**), B cell (**CL:0000236**), natural killer cell (**CL:0000623**), hematopoietic stem cell (**CL:0000037**), neural progenitor/neuron (**CL:0000031**/**CL:0000540**), keratinocyte (**CL:0000312**).
- **Molecular profiling:** no transcriptomic/proteomic/metabolomic datasets published for POLD3 patients; functional readouts to date are flow-cytometric immunophenotyping, TCR-repertoire sequencing, cell-cycle/EdU S-phase assays, and γH2AX DSB-foci quantification.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **thymus** (aplasia/hypoplasia, UBERON:0002370), **bone marrow / hematopoietic system** (UBERON:0002371), **lymph nodes / spleen** (lymphadenopathy, splenomegaly; UBERON:0000029/UBERON:0002106), **brain / CNS** (UBERON:0000955), **inner ear / cochlea** (UBERON:0001846/UBERON:0001844).
- **Secondary involvement:** **lungs/airways** (recurrent infection, bronchiectasis; UBERON:0002048), **liver** (hepatomegaly; UBERON:0002107), **skin** (erythroderma, dryness; UBERON:0002097), **hair follicles** (alopecia), **nails**, **teeth/enamel**.
- **Body systems:** immune/lymphatic, nervous, auditory, integumentary, respiratory (secondary), digestive (feeding difficulties).
- **Tissue/cell level:** lymphoid tissue and lymphocyte progenitors; neural tissue; cochlear/sensory epithelium; ectodermal epithelia (epidermis, hair, nail matrix, ameloblasts).
- **Subcellular (GO Cellular Component):** **nucleus (GO:0005634)**, **delta DNA polymerase complex (GO:0043625)**, **zeta DNA polymerase complex (GO:0016035)**, replication fork (GO:0005657). POLD3 localizes to nucleus and cytoplasm (UniProt Q15054).
- **Lateralization:** systemic/bilateral (e.g., bilateral sensorineural hearing loss); not lateralized.

---

## 8. Temporal Development

- **Onset:** congenital/**neonatal**; immunologic and syndromic features manifest in early infancy. Onset pattern **acute to subacute** for infections (SCID presentation), with an **insidious-progressive** neurodevelopmental component.
- **Progression:** rapid for the immune defect; **progressive** neurological regression (documented post-HSCT in the Omenn patient). Disease course is **progressive**, not relapsing/episodic.
- **Duration/stages:** without curative therapy, SCID is fatal in the first 1–2 years; with HSCT, immune reconstitution is possible but **non-immune (neuro/auditory) disease continues to progress** → death reported at **age 4 years** despite HSCT at 6 months (PMID 38099988).
- **Remission patterns:** no spontaneous remission; partial, compartment-specific improvement with HSCT (immune only).
- **Critical period / window of intervention:** the neonatal–early-infancy window (ideally **pre-infection HSCT**, <3.5 months as in classic SCID) is critical for the immune compartment; however, the replication defect in CNS/cochlea likely has a developmental origin that transplantation cannot reverse.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic/homozygous). Both reported families **consanguineous**.
- **Penetrance:** presumed **complete** for biallelic pathogenic genotypes (n=2); **expressivity** variable between the two reports (classic SCID vs. Omenn presentation).
- **Anticipation:** not applicable (not a repeat-expansion disorder). **Germline mosaicism:** not reported.
- **Founder effects / variant geography:** both variants are **private** (one Lebanese, one in a separate pedigree reported from Europe); no founder haplotype established. Consanguinity (e.g., Middle Eastern/North African populations) increases the chance of homozygosity.
- **Carrier frequency:** not established; both alleles are essentially absent from gnomAD, so heterozygous carriers are vanishingly rare.
- **Epidemiology:** **ultra-rare**—only **two patients reported worldwide** (2023). Prevalence/incidence not quantifiable (far below 1/1,000,000). No sex predilection established (both reported probands male, but n too small to infer a sex ratio); AR inheritance predicts equal sex distribution. Age distribution: infants/young children.

---

## 10. Diagnostics

- **Laboratory tests:**
  - Lymphocyte subsets by flow cytometry: **low total/naive T cells** (low TRECs), variable B and **low NK** cells; reduced naive CD4+/CD8+.
  - Immunoglobulins: **low IgG**, abnormal IgM, **elevated IgE**; **eosinophilia** (CBC with differential).
  - TCR-repertoire analysis: **restricted/oligoclonal** repertoire; evidence of defective early TCR recombination.
- **Biomarkers:** no specific circulating biomarker; **cellular replication-stress markers** (γH2AX DSB foci; defective EdU/S-phase incorporation in patient fibroblasts) are diagnostic functional supports (PMID 38099988).
- **Imaging / functional:** absent thymic shadow on chest imaging; **audiometry/ABR** for sensorineural hearing loss; brain MRI for neurodevelopmental assessment; chest CT for bronchiectasis.
- **Biopsy/pathology:** Omenn skin shows erythroderma; lymphoid tissue shows oligoclonal T-cell infiltration (consistent with Omenn; general).
- **Genetic testing (diagnostic gold standard):**
  - **Whole-exome (WES)** or **whole-genome (WGS)** sequencing identified both cases; **IEI/SCID/combined-immunodeficiency NGS gene panels** should include **POLD1, POLD2, POLD3**.
  - **Single-gene/targeted** confirmation and **cascade/segregation** testing in families; homozygosity mapping is useful in consanguineous pedigrees.
  - CMA/karyotype/FISH/mtDNA/repeat-expansion testing: **not indicated** (point-mutation disorder).
- **Clinical criteria / classification:** meets **SCID / Omenn syndrome** diagnostic criteria (profound T-cell lymphopenia ± erythroderma, eosinophilia, high IgE, oligoclonal T cells); classified under IUIS "combined immunodeficiencies with associated/syndromic features."
- **Differential diagnosis:** other SCID/Omenn genes—**RAG1/RAG2, DCLRE1C (Artemis), LIG4, NHEJ1, DNA-PKcs/PRKDC, IL2RG, JAK3, IL7R, ADA, RMRP (cartilage-hair hypoplasia)**; and the related **POLD1- and POLD2-deficiency** syndromes (replication-stress CID; PMID 31449058). Distinguishing features: POLD3/POLD1/POLD2 disease uniquely couples SCID with **replicative stress + neurodevelopmental delay + sensorineural hearing loss + ectodermal signs**. Also distinguish **POLD1 gain-of-function/MDPL** (progeroid, mandibular hypoplasia, lipodystrophy) and **POLD1/POLD2 proofreading-associated polyposis/cancer**, which are mechanistically different and **not** part of IMD122.
- **Screening:** detectable by **newborn SCID screening (TREC assay)** given profound T-cell lymphopenia; **carrier/prenatal/PGT** testing feasible once familial variant known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **poor**. SCID is fatal in infancy without HSCT; even with HSCT at 6 months, one patient **died at age 4 years** from progressive neurological regression (PMID 38099988). Disease-specific mortality is high.
- **Morbidity/disability:** severe—recurrent/opportunistic infections, failure to thrive, **developmental disability**, **sensorineural deafness**, bronchiectasis (chronic lung damage).
- **Recovery potential:** HSCT can reconstitute immunity (hematopoietic compartment) but **does not correct the cell-intrinsic replication defect in CNS/cochlea/ectoderm**, so neurodevelopmental and auditory outcomes remain poor.
- **Prognostic factors:** age at HSCT, pre-transplant infection/organ damage, and—unique to this disorder—**severity of the non-hematopoietic replication defect** (neuro/auditory), which transplantation cannot rescue.
- **Prognostic biomarkers:** degree of replication stress / genomic instability (γH2AX, S-phase defect) is a mechanistic correlate of severity (inferred).

---

## 12. Treatment

*(No disease-specific approved therapy exists; management follows SCID/Omenn principles.)*

- **Definitive:** **Allogeneic hematopoietic stem cell transplantation (HSCT)** — **NCIT:C15431** (Hematopoietic Stem Cell Transplantation) / **NCIT:C105867** (Allogeneic HSCT). Reconstitutes the immune system; performed at 6 months in the reported Omenn patient (PMID 38099988). Does **not** address non-immune manifestations.
- **Supportive / prophylactic (standard SCID care, NCIT terms):**
  - **Immunoglobulin replacement therapy (IVIG/SCIG)** — NCIT:C603 (Immunoglobulin Therapy).
  - **Antimicrobial prophylaxis** — anti-*Pneumocystis* (co-trimoxazole), antifungal, antiviral prophylaxis.
  - **Irradiated, CMV-safe, leukodepleted blood products**; avoidance of **live vaccines**.
  - Nutritional support for feeding difficulties; management of erythroderma; **immunosuppression** (e.g., steroids/cyclosporine) to control Omenn immune dysregulation pre-HSCT.
  - Rehabilitation: **hearing aids/cochlear implantation**, early developmental/physical/speech therapy, audiology follow-up.
- **Gene therapy / RNA / targeted / immunotherapy:** none available or in trials for POLD3 deficiency. In vitro, **WT POLD3 restoration rescues** the cellular phenotype (PMID 38099988), providing proof-of-concept that gene correction could address the cell-intrinsic defect—**experimental/hypothetical only**.
- **Pharmacogenomics:** none specific; standard transplant-conditioning pharmacogenetics (e.g., busulfan, thiopurines) apply generically. Caution with **genotoxic conditioning/chemotherapy** given underlying DNA-repair/replication fragility (inferred; analogous to other DNA-repair SCIDs such as Artemis/LIG4, where reduced-toxicity conditioning is preferred).
- **Clinical trials (NCT):** none identified specific to POLD3/IMD122.

---

## 13. Prevention

- **Primary prevention:** not preventable at the individual level (monogenic, congenital). **Genetic counseling** for consanguineous couples and families with an affected child (25% recurrence risk per pregnancy).
- **Secondary prevention / early detection:** **newborn SCID screening (TREC)** enables presymptomatic detection and **early pre-infection HSCT**, the key opportunity to improve immune outcomes. **Cascade testing** of at-risk relatives.
- **Genetic/reproductive prevention:** **carrier screening**, **prenatal diagnosis**, and **preimplantation genetic testing (PGT-M)** once the familial variant is known.
- **Tertiary prevention:** infection prophylaxis, avoidance of live vaccines and non-irradiated blood products, early audiologic and developmental intervention, pulmonary care to limit bronchiectasis progression.
- **Immunization/public-health/environmental measures:** not applicable beyond standard infection-control for immunocompromised infants.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *POLD3* is conserved across eukaryotes. Mouse ***Pold3*** (NCBI Gene **69745**; *Mus musculus*, NCBI:txid10090); orthologs in rat, zebrafish; the yeast functional homolog is **POL32** (*Saccharomyces cerevisiae*). POLD3/POL32 is part of Pol δ and Pol ζ across species.
- **Natural disease in other species:** no naturally occurring *POLD3* disease reported in companion animals or wildlife (OMIA: none identified). Not a zoonosis; not transmissible.
- **Comparative biology:** the replication/genome-maintenance function of POLD3/POL32 is **deeply evolutionarily conserved**, making model systems highly informative. Complete loss is lethal from yeast to mouse, underscoring essentiality.
- **Veterinary relevance:** none established.

---

## 15. Model Organisms

- **Mouse (*Mus musculus*, Pold3):**
  - **Complete knockout (Pold3⁻/⁻) is embryonic lethal at E6.5** (PMID 29447390). *"complete loss of Pold3 (Pold3-/-) resulted in early embryonic lethality at E6.5."*
  - **Inducible KO / blastocyst outgrowth / ESCs:** rapid DNA-damage response, massive apoptosis, **telomere loss, chromosome breaks, extended S phase, replicative stress, micronucleation, aneuploidy**; Pold3 acts via **53BP1, RIF1, ATR, ATM**.
  - **Pold3⁺/⁻ (haploinsufficient)** mice develop **age-dependent** impaired DSB repair, telomere shortening and chromosome breaks (spermatocytes).
  - **Phenotype recapitulation:** strongly models the **cell-intrinsic replication-stress/genomic-instability** mechanism of human disease; **limitation:** null is embryonic-lethal, so it cannot model the viable, organ-specific human syndrome—**hypomorphic knock-in alleles** (e.g., patient-equivalent) would be needed to recapitulate SCID + neuro/auditory features.
- **Cellular / in vitro models:** **patient-derived fibroblasts** (S-phase defect, γH2AX DSB foci, rescued by WT POLD3 transduction — PMID 38099988); patient immune cells (TCR-repertoire/recombination assays). Yeast **pol32Δ** is a classic genetic model of the accessory subunit.
- **Other organisms:** chicken DT40 and yeast systems have historically defined POLD3/POL32 roles in replication, translesion synthesis, and break-induced replication (background literature).
- **Resources:** MGI (Pold3), IMPC/IMSR, Alliance of Genome Resources, SGD (POL32), Cellosaurus (patient fibroblast lines).

---

## Supported vs. Refuted Hypotheses

**Supported:**
- IMD122 is caused by autosomal-recessive, biallelic hypomorphic *POLD3* missense variants (PMID 37030525; 38099988).
- The mechanism is reduced Pol δ function → replicative stress / S-phase defect / DSB accumulation → impaired lymphopoiesis and TCR recombination → SCID/Omenn, with parallel injury to neural, cochlear, and ectodermal lineages (PMID 38099988; 29447390; 31449058).
- POLD3 is essential and LoF-intolerant; only hypomorphic alleles are viable (gnomAD; mouse null lethality).

**Refuted / excluded:**
- Not caused by environmental, infectious, or acquired/somatic factors; infections are a consequence.
- Not a chromosomal/structural or repeat-expansion disorder.
- IMD122 is **distinct** from POLD1 gain-of-function **MDPL** progeroid syndrome and from POLD1/POLD2 proofreading-associated polyposis/cancer.

## Limitations and Future Directions

- **n=2** patients: frequencies, penetrance range, sex ratio, and full phenotypic spectrum are provisional; natural-history data are absent.
- No omics (transcriptomic/proteomic/metabolomic) profiling, no registry, no clinical trials.
- Unresolved: why certain tissues (cochlea, specific neural populations) are selectively vulnerable; whether reduced-toxicity HSCT conditioning improves outcomes; whether early gene-correction could rescue non-immune disease.
- **Future:** patient-equivalent hypomorphic knock-in mouse models; iPSC-derived neural/cochlear organoids; identification of additional patients via GeneMatcher to define the phenotypic spectrum and genotype–phenotype correlations.

---

### Key References
- **PMID 37030525** — Mehawej et al., 2023. *POLD3 deficiency is associated with severe combined immunodeficiency, neurodevelopmental delay, and hearing impairment.* (First case; p.Ile10Thr.)
- **PMID 38099988** — Riestra et al., 2023. *Human Autosomal Recessive DNA Polymerase Delta 3 Deficiency Presenting as Omenn Syndrome.* (Second case; p.K373T; functional S-phase/DSB rescue.)
- **PMID 31449058** — Conde et al., 2019 (J Clin Invest). *Polymerase δ deficiency causes syndromic immunodeficiency with replicative stress.* (POLD1/POLD2 parent syndrome.)
- **PMID 29447390** — Zhou et al., 2018. *Pold3 is required for genomic stability and telomere integrity in embryonic stem cells and meiosis.* (Mouse model.)
- Database sources: OMIM 620869; MONDO:0971151 (Monarch); UniProt Q15054; gnomAD (POLD3 constraint); HPO annotations (OMIM 620869).


## Artifacts

- [OpenScientist final report](Immunodeficiency_122-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_122-deep-research-openscientist_artifacts/final_report.pdf)
- [OpenScientist notes](Immunodeficiency_122-deep-research-openscientist_artifacts/notes.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 70 |
| Resolved | 68 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0971151` (3 mentions) - the report calls it "Monarch"; MONDO calls it **immunodeficiency 122**
- `NCIT:C603` (1 mention) - the report calls it "Immunoglobulin Therapy"; NCIT calls it **Isotretinoin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002371` (1 mention) - the report calls it "bone marrow / hematopoietic system"; UBERON calls it **bone marrow**
- `UBERON:0000955` (1 mention) - the report calls it "brain / CNS"; UBERON calls it **brain**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.