---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-23T19:10:39.603293'
end_time: '2026-09-23T19:57:56.957511'
duration_seconds: 2837.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Lateral Meningocele Syndrome
  mondo_id: MONDO:0007537
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
citation_count: 29
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 29
  on_topic: 19
  validator_version: 0.2.1
term_validation:
  total_terms: 41
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: GO:0005634
    reported_labels:
    - NOTCH3 ICD acts as a transcriptional co-activator
    ontology_label: nucleus
  - term_id: GO:0005886
    reported_labels:
    - receptor
    ontology_label: plasma membrane
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Lateral_Meningocele_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Lateral_Meningocele_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lateral Meningocele Syndrome
- **MONDO ID:** MONDO:0007537 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lateral Meningocele Syndrome** covering all of the
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

# Lateral Meningocele Syndrome (Lehman Syndrome): A Comprehensive Disease Characterization

**Disease:** Lateral Meningocele Syndrome (LMS)
**Synonyms:** Lehman syndrome
**Identifiers:** OMIM %130720 · MONDO:0007537 · ORPHA:2140 · Gene: NOTCH3 (HGNC:7883), chr19p13.12
**Category:** Mendelian, autosomal dominant

---

## Summary

Lateral Meningocele Syndrome (LMS), also known as Lehman syndrome, is an extremely rare autosomal-dominant multisystem connective-tissue and skeletal disorder caused by **heterozygous truncating variants in the last coding exon (exon 33) of the *NOTCH3* gene**. These variants delete the C-terminal PEST degradation domain, stabilizing the intracellular NOTCH3 fragment and producing a **gain-of-function** in Notch signaling. This mechanism sharply distinguishes LMS from CADASIL — the common cerebral small-vessel disease that is allelic to LMS but caused by cysteine-altering missense variants in the NOTCH3 extracellular domain acting through a fundamentally different, aggregation-based pathway.

Clinically, LMS is defined by **multiple bilateral lateral spinal meningoceles** (the severe end of the dural ectasia spectrum, most prominent in the thoracolumbar spine) accompanied by a **distinctive craniofacial gestalt** (hypertelorism, telecanthus, high-arched eyebrows, ptosis, midfacial hypoplasia, micrognathia), **connective-tissue features** (skin hyperextensibility, joint hypermobility, hernias, scoliosis), hypotonia, and **skeletal osteopenia**. The phenotype is progressively expanding and now includes short stature, congenital heart defects, feeding difficulties/failure to thrive, developmental delay/intellectual disability, sensorineural hearing loss, inner-ear anomalies, renal cystic disease, and — most recently — biliary anomalies. Diagnosis rests on **whole-spine MRI** demonstrating the characteristic meningoceles combined with **molecular confirmation of an exon-33 *NOTCH3* variant**; prenatal molecular diagnosis is now feasible.

Mechanistic work in mouse and human iPSC models has established that the **bone-loss component is driven by NOTCH3-enhanced, RANKL-mediated osteoclastogenesis**, with NOTCH3 acting on osteoblast-lineage cells and osteocytes to upregulate RANKL. This paralog-specific effect (NOTCH1 inhibits, NOTCH2/NOTCH3 promote osteoclastogenesis) mirrors the pathobiology of Hajdu-Cheney syndrome (NOTCH2). No FDA-approved disease-modifying therapy exists; current management is supportive and neurosurgical. However, **Notch3-lowering antisense oligonucleotides (ASOs) and an anti-Notch3 neutralizing antibody reverse the skeletal phenotype in male mouse models**, and allele-selective ASOs achieve 70–80% knockdown of mutant transcript in patient-derived cells — a promising but still preclinical therapeutic avenue.

---

## Key Findings

### F001 — LMS is caused by heterozygous truncating *NOTCH3* variants clustered in the last exon (exon 33)

The causal gene was identified by exome resequencing of five unrelated individuals with LMS, all of whom carried heterozygous truncating *NOTCH3* mutations; a sixth case was confirmed by Sanger sequencing. In total, **five novel *de novo* mutations were identified in six unrelated patients**. The reported variants include a 26-bp deletion (c.6461_6486del, p.G2154fsTer78), a recurrent single-base insertion (c.6692_93insC, p.P2231fsTer11, seen in two patients), and three nonsense variants (c.6247A>T p.K2083*; c.6663C>G p.Y2221*; c.6732C>A p.Y2244*). A defining molecular feature is that **all variants cluster in the last coding exon (exon 33)**, producing premature termination and truncation of the C-terminal region.

> *"We performed exome resequencing in five unrelated individuals with LMS and identified heterozygous truncating NOTCH3 mutations."* — [PMID: 25394726](https://pubmed.ncbi.nlm.nih.gov/25394726/)

> *"All mutations cluster into the last coding exon, resulting in premature termination of the protein and truncation of…"* — [PMID: 25394726](https://pubmed.ncbi.nlm.nih.gov/25394726/)

Additional confirmatory variants have since been reported, including a de novo c.6723_6736del p.(Glu2241AspfsTer8) identified through the 100,000 Genomes Project ([PMID: 40256810](https://pubmed.ncbi.nlm.nih.gov/40256810/)) and an 80-bp deletion in exon 33 ([PMID: 26754023](https://pubmed.ncbi.nlm.nih.gov/26754023/)), reinforcing the exon-33 truncation signature. **Identifiers:** NOTCH3 (HGNC:7883); OMIM gene 600276; disease OMIM %130720.

### F002 — LMS variants cause NOTCH3 gain-of-function through loss of the PEST domain

The exon-33 truncations delete the **C-terminal PEST domain**, a proline-, glutamate-, serine-, and threonine-rich sequence that normally targets the intracellular Notch fragment for proteasomal degradation. Its loss **stabilizes the NOTCH3 intracellular domain**, prolonging and enhancing downstream Notch signaling. This was directly demonstrated in human iPSC models: cells harboring the NOTCH3 c.6692_93insC variant showed **enhanced expression of the canonical Notch target genes HES1, HEY1, HEY2, and HEYL**, confirming gain-of-function.

> *"Lateral Meningocele or Lehman Syndrome (LMS) is associated with NOTCH3 mutations causing deletions of the PEST domain and a gain-of-NOTCH3 function."* — [PMID: 35760307](https://pubmed.ncbi.nlm.nih.gov/35760307/)

> *"NOTCH3 6692-93insC cells displayed enhanced expression of Notch target genes HES1, HEY1, 2 and L demonstrating a NOTCH3 gain-of-function."* — [PMID: 39752389](https://pubmed.ncbi.nlm.nih.gov/39752389/)

**Functional consequence:** gain-of-function via protein stabilization (not haploinsufficiency). **Suggested GO terms:** Notch signaling pathway (GO:0007219); positive regulation of transcription by RNA polymerase II (GO:0045944); protein stabilization (GO:0050821).

### F003 — Bone loss/osteopenia in LMS is driven by NOTCH3-enhanced RANKL-mediated osteoclastogenesis

The skeletal osteopenia of LMS has been mechanistically dissected in mouse models. The **Notch3^em1Ecan^ knock-in mouse**, harboring a 6691TAATGA PEST-truncating mutation homologous to human LMS variants, exhibits **both cancellous and cortical bone osteopenia**. Experimental analysis revealed that the bone loss is **secondary to increased osteoclastogenesis driven by enhanced RANKL (receptor activator of NF-κB ligand) expression** by osteoblast-lineage cells. Osteocyte-specific induction of the Lehman mutation independently caused osteopenia in male mice, localizing a key cellular source of the RANKL signal to osteocytes.

> *"Experimental mouse models of LMS revealed that the bone loss is secondary to increased osteoclastogenesis due to enhanced expression of receptor activator of nuclear factor kappa B ligand by cells of the osteoblast lineage."* — [PMID: 33519922](https://pubmed.ncbi.nlm.nih.gov/33519922/)

**Suggested GO terms:** osteoclast differentiation (GO:0030316); positive regulation of osteoclast differentiation (GO:0045672); bone resorption (GO:0045453). **Suggested CL terms:** osteoblast (CL:0000062); osteocyte (CL:0000137); osteoclast (CL:0000092). **Protein:** TNFSF11/RANKL.

### F004 — Notch3-targeting ASOs and an anti-Notch3 antibody reverse the skeletal phenotype in LMS mouse models (preclinical)

Because stabilized gain-of-function NOTCH3 is the disease driver, **lowering NOTCH3 is a rational therapeutic strategy**. Subcutaneous administration of Notch3 ASOs (25–50 mg/kg) decreased Notch3 mRNA in liver, heart, and bone and ameliorated cortical osteopenia, reducing femoral cortical porosity in Notch3^em1Ecan^ mice. The ASOs were paralog-specific (they did not downregulate Notch1, Notch2, or Notch4). **Allele-selective ASOs targeting the mutant insertion reduced mutant transcript by 70–80% in mesenchymal cells**, offering an approach that spares the wild-type allele. Separately, a **Notch3-neutralizing antibody also reversed the skeletal phenotype in male mice** ([PMID: 31188489](https://pubmed.ncbi.nlm.nih.gov/31188489/)).

> *"Lateral Meningocele Syndrome (LMS) is a monogenic disorder associated with NOTCH3 pathogenic variants that result in the stabilization of NOTCH3 and a gain-of-function."* — [PMID: 37704069](https://pubmed.ncbi.nlm.nih.gov/37704069/)

> *"In vivo, the subcutaneous administration of Notch3 ASOs at 25 to 50 mg/Kg decreased Notch3 mRNA in the liver, heart and bone."* — [PMID: 35536858](https://pubmed.ncbi.nlm.nih.gov/35536858/)

These interventions remain **preclinical**; there is no FDA-approved therapy for LMS. **Suggested NCIT terms:** Antisense Oligonucleotide; Monoclonal Antibody Therapy.

### F005 — LMS is a multisystem connective-tissue/skeletal syndrome defined by lateral meningoceles plus distinctive facies

The **core diagnostic triad** comprises (1) multiple lateral thoracolumbar spinal meningoceles — the severe end of the dural ectasia spectrum, typically most severe in the lower spine; (2) a distinctive facial gestalt; and (3) connective-tissue signs.

> *"Facial features of LMS include hypertelorism and telecanthus, high arched eyebrows, ptosis, midfacial hypoplasia, micrognathia, high and narrow palate, low-set ears and a hypotonic appearance."* — [PMID: 25394726](https://pubmed.ncbi.nlm.nih.gov/25394726/)

> *"The characteristic lateral meningoceles represent the severe end of the dural ectasia spectrum and are typically most severe in the lower spine."* — [PMID: 25394726](https://pubmed.ncbi.nlm.nih.gov/25394726/)

The **expanded phenotype** includes short stature, congenital heart defects, feeding difficulties/failure to thrive, developmental delay/intellectual disability, sensorineural hearing loss, renal cysts, Chiari I malformation, syringomyelia, hydrocephalus, and tethered cord.

> *"Besides the lateral meningoceles, this condition presents with dysmorphic features, short stature, congenital heart defects, and feeding difficulties."* — [PMID: 32141180](https://pubmed.ncbi.nlm.nih.gov/32141180/)

There is substantial phenotypic overlap with Hajdu-Cheney syndrome (NOTCH2), Marfan syndrome, Ehlers-Danlos syndrome, and Loeys-Dietz syndrome, complicating clinical recognition ([PMID: 25821090](https://pubmed.ncbi.nlm.nih.gov/25821090/); [PMID: 40256810](https://pubmed.ncbi.nlm.nih.gov/40256810/)).

**Suggested HPO terms:** Meningocele (HP:0002435); Dural ectasia (HP:0100775); Hypertelorism (HP:0000316); Telecanthus (HP:0000506); Ptosis (HP:0000508); Micrognathia (HP:0000347); Highly arched eyebrow (HP:0002553); Midface retrusion (HP:0011800); Joint hypermobility (HP:0001382); Hyperextensible skin (HP:0000974); Scoliosis (HP:0002650); Muscular hypotonia (HP:0001252); Short stature (HP:0004322); Sensorineural hearing impairment (HP:0000407); Chiari type I malformation (HP:0007099); Syringomyelia (HP:0003396); Tethered cord (HP:0002144).

### F006 — LMS is a very rare, mostly de novo autosomal-dominant disorder (~few dozen reported cases)

LMS is described as "very rare" to "exceedingly rare." A 2019 neurosurgical review identified only **11 articles covering 16 cases (9 males, 7 females) across 14 families**; among those genetically screened, all carried exon-33 *NOTCH3* truncations. The original gene-discovery cohort reported **five de novo mutations in six unrelated patients**. Two instances of vertical (parent-to-child) transmission have been documented, consistent with autosomal-dominant inheritance, but most cases are de novo. Age at diagnosis ranges from infancy (as early as 5 months / 2 years) to 55 years.

> *"Our literature search revealed 11 articles (16 cases) of LMS, which included 9 males and 7 females, belonging to 14 different families."* — [PMID: 31838470](https://pubmed.ncbi.nlm.nih.gov/31838470/)

> *"In total, five novel de novo NOTCH3 mutations were identified in six unrelated patients."* — [PMID: 25394726](https://pubmed.ncbi.nlm.nih.gov/25394726/)

No formal population prevalence or incidence figures are established; Orphanet lists prevalence as <1/1,000,000 (ORPHA:2140). The near-balanced sex ratio (~9:7 M:F) is consistent with autosomal-dominant inheritance without sex bias. A very late diagnosis at age 55 illustrates that milder cases may go unrecognized for decades ([PMID: 24311540](https://pubmed.ncbi.nlm.nih.gov/24311540/)).

### F007 — LMS and CADASIL are distinct allelic *NOTCH3* disorders with opposite functional mechanisms

*NOTCH3* is associated with two mechanistically opposite diseases. **CADASIL** — the most common monogenic cerebral small-vessel disease — is caused by **stereotyped cysteine-altering missense variants in the EGF-like repeats of the NOTCH3 extracellular domain** that change the number of cysteine residues, causing ectodomain misfolding, aggregation (granular osmiophilic material, GOM), and vascular smooth muscle cell degeneration. **LMS** is caused by **PEST-domain truncating variants** producing intracellular gain-of-function. Rare patients carrying both classes of variant have been reported.

> *"CADASIL, the most common monogenic form of cSVD, is caused by stereotyped mutations in the NOTCH3 receptor that alter the number of cysteine residues in its extracellular domain."* — [PMID: 40145673](https://pubmed.ncbi.nlm.nih.gov/40145673/)

> *"the patient was found to have two variants of the NOTCH3 gene, resulting in the diagnosis of lateral meningocele (Lehman) syndrome"* — [PMID: 34172679](https://pubmed.ncbi.nlm.nih.gov/34172679/)

Additional NOTCH3-related phenotypes further map the genotype-mechanism landscape: **biallelic loss-of-function** variants cause a neurodevelopmental disorder with spasticity and childhood-onset stroke, whereas **biallelic cysteine-involving missense** variants produce a CADASIL-spectrum phenotype ([PMID: 39191170](https://pubmed.ncbi.nlm.nih.gov/39191170/)). The molecular pathobiology of CADASIL — non-enzymatic NOTCH3 fragmentation and cysteine-redox–driven aggregation — has been characterized in detail ([PMID: 31901894](https://pubmed.ncbi.nlm.nih.gov/31901894/); [PMID: 35409031](https://pubmed.ncbi.nlm.nih.gov/35409031/); [PMID: 35223989](https://pubmed.ncbi.nlm.nih.gov/35223989/)), underscoring how different its mechanism is from LMS.

### F008 — Diagnosis relies on whole-spine MRI plus molecular confirmation of an exon-33 *NOTCH3* variant; management is neurosurgical/supportive

**Whole-spine MRI** is the key imaging study, demonstrating multiple bilateral well-defined cystic masses within the neural foramina (predominantly thoracolumbar), with neural foraminal widening, dural ectasia, and posterior vertebral body scalloping. CT complements this by showing vertebral/pedicle scalloping and spinal canal widening. **Molecular confirmation** is by exome/genome or targeted *NOTCH3* exon-33 sequencing; "reverse phenotyping" (identifying the variant first, then imaging) has diagnosed presymptomatic and prenatal cases.

> *"showed multiple bilateral well-defined cystic masses within the neural foramina involving the entire spine, predominantly the thoracolumbar regions, with neural foraminal widening and dural ectasia suggestive of multiple lateral meningoceles"* — [PMID: 33042242](https://pubmed.ncbi.nlm.nih.gov/33042242/)

> *"an early genomic analysis allowed us to recognize the presence of lateral meningoceles and to begin early monitoring of her condition for possible neurological complications"* — [PMID: 34121137](https://pubmed.ncbi.nlm.nih.gov/34121137/)

Management is **supportive and neurosurgical**, with no formal guidelines. Symptomatic meningoceles are treated by surgical repair or shunting (cyst-subarachnoid or cystoperitoneal). A recent case documents cyst-subarachnoid shunts at T8 and L5-S1 producing immediate symptomatic improvement and gradual meningocele regression.

> *"Two cyst-subarachnoid (C-S) shunts were placed, at the superior aspect of the meningocele (T8) and the inferior aspect (L5-S1). His symptoms improved immediately, and the meningocele gradually regressed postoperatively."* — [PMID: 41432782](https://pubmed.ncbi.nlm.nih.gov/41432782/)

Surgery is complicated by coexisting Chiari I malformation, syringomyelia, hydrocephalus, tethered cord, and the underlying mesodermal/connective-tissue fragility ([PMID: 31838470](https://pubmed.ncbi.nlm.nih.gov/31838470/); [PMID: 38755334](https://pubmed.ncbi.nlm.nih.gov/38755334/)).

### F009 — Genetically engineered and natural mouse and iPSC models recapitulate the LMS skeletal phenotype

The principal in vivo model is the **Notch3^em1Ecan^ knock-in mouse** (6691TAATGA PEST-truncating mutation), whose heterozygotes reproduce cancellous and cortical bone osteopenia and increased femoral cortical porosity. Osteocyte-specific induction of a NOTCH3 Lehman mutation causes osteopenia in male C57BL/6J mice. **Human iPSC models** (NCRM1/NCRM5 carrying NOTCH3 c.6692_93insC plus isogenic controls) differentiated toward neural crest, mesenchymal, and osteogenic lineages exhibit gain-of-function and enhanced osteogenesis. A spontaneous murine *Notch3* mutation ("humpback") provides a natural model.

> *"We created a mouse model (Notch3^em1Ecan) harboring a 6691TAATGA mutation in the Notch3 locus, and heterozygous Notch3^em1Ecan mice exhibit cancellous and cortical bone osteopenia."* — [PMID: 35536858](https://pubmed.ncbi.nlm.nih.gov/35536858/)

> *"induced pluripotent NCRM1 and NCRM5 stem (iPS) cells harboring a NOTCH3 6692-93insC insertion were created"* — [PMID: 39752389](https://pubmed.ncbi.nlm.nih.gov/39752389/)

These models enabled therapeutic testing (ASOs and antibody rescue). **Phenotype recapitulation is strongest for the skeletal/bone-loss component**; the models less fully capture the meningocele and craniofacial features. The "humpback" natural mutant was precisely genotyped using a PCR-based ARMS system ([PMID: 33860007](https://pubmed.ncbi.nlm.nih.gov/33860007/)). **Resources:** MGI (Notch3 alleles); Alliance of Genome Resources. **Orthologous gene:** mouse *Notch3* (NCBI Gene 18131).

### F010 — NOTCH paralogs have opposing effects on bone; NOTCH3 specifically induces osteoblast/osteocyte RANKL

Paralog specificity explains the LMS bone phenotype. In the skeleton, **NOTCH1 inhibits osteoclastogenesis, whereas NOTCH2 enhances osteoclast differentiation**, and **NOTCH3 induces RANKL expression in osteoblasts and osteocytes**, thereby driving osteoclast differentiation via an indirect mechanism. This is why NOTCH3 gain-of-function in LMS produces net bone resorption/osteopenia — mechanistically parallel to NOTCH2 gain-of-function in Hajdu-Cheney syndrome.

> *"NOTCH3 induces the expression of RANKL in osteoblasts and osteocytes and as a result induces osteoclast differentiation."* — [PMID: 32526405](https://pubmed.ncbi.nlm.nih.gov/32526405/)

> *"NOTCH1 inhibits osteoclastogenesis, whereas NOTCH2 enhances osteoclast differentiation and function by direct and indirect mechanisms."* — [PMID: 32526405](https://pubmed.ncbi.nlm.nih.gov/32526405/)

> *"There are no effective therapies for LMS."* — [PMID: 33519922](https://pubmed.ncbi.nlm.nih.gov/33519922/)

### F011 — The phenotype is progressively expanding; prenatal diagnosis is feasible and new organ involvements continue to be reported

The **first prenatal molecular diagnosis of LMS** was achieved by prenatal exome sequencing following an ultrasound showing fetal cystic hygroma, mild bilateral ventriculomegaly, and facial dysmorphisms; postnatal MRI confirmed lateral meningoceles and evaluation revealed **previously unreported biliary anomalies**.

> *"We report the first case of prenatal molecular diagnosis of LMS, which was made using prenatal exome sequencing after an ultrasound with findings of fetal cystic hygroma, mild bilateral ventriculomegaly, and facial dysmorphisms."* — [PMID: 40771185](https://pubmed.ncbi.nlm.nih.gov/40771185/)

> *"A complete clinical evaluation was performed and unexpected biliary anomalies were found. The occurrence of biliary anomalies has not been previously reported in LMS"* — [PMID: 40771185](https://pubmed.ncbi.nlm.nih.gov/40771185/)

Earlier reports had already expanded the spectrum to include inner-ear abnormalities and multicystic kidney disease.

> *"expands the spectrum of clinical manifestations related to LMS to include inner ear abnormalities and multi-cystic kidney disease"* — [PMID: 32141180](https://pubmed.ncbi.nlm.nih.gov/32141180/)

Strikingly, a molecularly confirmed 8-year-old case **lacked lateral meningoceles entirely**, sharing only the dysmorphic facies, G-tube dependence, failure to thrive, and developmental delay — expanding the phenotype and cautioning that the hallmark meningoceles are not obligate ([PMID: 39119451](https://pubmed.ncbi.nlm.nih.gov/39119451/)). Consistent with the multisystem picture, NOTCH3 functions as a transcriptional activator across diverse tissues.

---

## Full Section-by-Section Report

### 1. Disease Information

LMS is a rare hereditary connective-tissue disorder characterized by multiple lateral spinal meningoceles, distinctive facial dysmorphism, joint/skin laxity, hypotonia, and skeletal, cardiac, and urogenital anomalies. **Key identifiers:** OMIM %130720; MONDO:0007537; ORPHA:2140; MeSH — indexed under "Meningocele" (no dedicated LMS descriptor); ICD-10 Q06.8 / ICD-11 LA05.Y as nearest structural codes (no LMS-specific code). **Synonyms:** Lehman syndrome; Lateral meningocele syndrome. The information base is a mixture of **individual patient case reports/case series** (dominant, given rarity) and **aggregated disease-level resources** (OMIM, Orphanet).

### 2. Etiology

**Primary cause:** genetic — heterozygous truncating variants in the last exon (exon 33) of *NOTCH3* (F001), acting via a **gain-of-function** through PEST-domain loss and protein stabilization (F002). **Genetic risk factors:** monogenic and essentially fully explained by the *NOTCH3* exon-33 variant; no human modifier loci mapped. **Environmental risk factors:** none identified — LMS is not known to be influenced by toxins, lifestyle, or infectious exposures; most cases arise as de novo germline events. **Protective factors:** none described. **Gene–environment interactions:** no evidence — this is a highly penetrant Mendelian disorder.

### 3. Phenotypes

Phenotypes span physical malformations (lateral meningoceles, dural ectasia, craniofacial dysmorphism, scoliosis), clinical signs (joint hypermobility, skin hyperextensibility, hypotonia), and functional/developmental abnormalities (feeding difficulties, developmental delay/intellectual disability, sensorineural hearing loss). See F005 and F011 for the full catalog and HPO mappings. **Onset** is congenital/neonatal-to-childhood; meningoceles were historically identified before age 8 (average age of identification ~4 years), though a meningocele-free case at age 8 and a first diagnosis at age 55 demonstrate wide variability in age of recognition. **Severity** is variable, from severe infantile presentations with failure to thrive to mild adult presentations with chronic musculoskeletal pain. **Progression:** meningoceles/dural ectasia can be progressive (enlarging via CSF pulsation); the syndrome overall is chronic and lifelong. **Frequency:** lateral meningoceles and characteristic facies are near-universal (rare exceptions); connective-tissue signs, hypotonia, and feeding difficulties are common; cardiac, renal, hearing, and biliary involvement are variable. **Quality-of-life impact:** substantial — chronic pain, joint instability, neurological sequelae from meningoceles (including iatrogenic nerve damage after surgery), feeding/growth problems, developmental disability. No formal EQ-5D/SF-36 data exist for this ultra-rare disease.

### 4. Genetic/Molecular Information

**Causal gene:** *NOTCH3* (HGNC:7883; OMIM gene 600276), chr19p13.12. **Variant types:** frameshift (deletions, insertions) and nonsense variants in exon 33 — all truncating, all removing the PEST domain (F001). Representative variants: c.6461_6486del (p.G2154fsTer78); c.6692_93insC (p.P2231fsTer11); c.6247A>T (p.K2083*); c.6663C>G (p.Y2221*); c.6732C>A (p.Y2244*); c.6723_6736del (p.E2241fsTer8); an 80-bp exon-33 deletion. **Classification:** pathogenic per ACMG (PVS1-type truncating in a gene with an established truncating/GoF mechanism, de novo PS2, phenotype-specific). **Allele frequency:** absent from population databases (gnomAD) — private, de novo variants. **Origin:** germline, predominantly de novo; two documented vertical transmissions. **Functional consequence:** gain-of-function through protein stabilization (F002). **Modifier genes:** none established. **Epigenetic changes:** none reported. **Chromosomal abnormalities:** none — LMS is a single-gene disorder.

### 5. Environmental Information

No environmental, lifestyle, or infectious contributors are implicated. LMS is a fully genetic, de novo–predominant Mendelian disorder. (Note: lateral meningoceles as an isolated radiological finding can occur in neurofibromatosis type 1 and as sporadic lesions — e.g., [PMID: 15688204](https://pubmed.ncbi.nlm.nih.gov/15688204/), [PMID: 23607071](https://pubmed.ncbi.nlm.nih.gov/23607071/), [PMID: 38755334](https://pubmed.ncbi.nlm.nih.gov/38755334/) — but these are distinct from *NOTCH3*-driven LMS.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **de novo heterozygous truncating variant in *NOTCH3* exon 33** arises in the germline (demonstrated).
2. The truncation **deletes the C-terminal PEST domain** of the NOTCH3 intracellular domain (demonstrated).
3. Loss of the PEST degron **impairs proteasomal turnover of the cleaved NOTCH3 intracellular domain, stabilizing it** (demonstrated via gain-of-function readouts; direct stabilization inferred and supported by analogy to Hajdu-Cheney NOTCH2).
4. Stabilized NOTCH3 **leads to enhanced and prolonged canonical Notch signaling** — elevated HES1, HEY1, HEY2, HEYL (demonstrated in iPSC models).
5. In the skeleton, this gain-of-function **branch** proceeds: enhanced NOTCH3 signaling in **osteoblasts and osteocytes results in increased RANKL (TNFSF11) expression** (demonstrated in mouse models).
6. Elevated RANKL **drives increased osteoclast differentiation and activity** (demonstrated), which **results in cancellous and cortical bone osteopenia and increased cortical porosity** (demonstrated).
7. In parallel developmental **branches** (mechanistically less resolved), NOTCH3 gain-of-function in neural crest–derived and mesenchymal lineages is **inferred to lead to** the meningocele/dural ectasia, craniofacial, connective-tissue, cardiac, renal, inner-ear, and biliary phenotypes. These arms are demonstrated clinically but the intervening cellular mechanism is inferred rather than experimentally mapped.

**Molecular pathway:** Notch signaling (KEGG hsa04330; Reactome "Signaling by NOTCH3"). **Cellular processes:** osteoclastogenesis, bone resorption, cell-fate specification. **Protein dysfunction:** loss of PEST-mediated degradation → stabilization → gain-of-function (contrast CADASIL's extracellular aggregation, F007). **Key cell types (CL):** osteoblast (CL:0000062), osteocyte (CL:0000137), osteoclast (CL:0000092), neural crest cell (CL:0000333, inferred), mesenchymal stem cell (CL:0000134). **Key GO processes:** Notch signaling pathway (GO:0007219), osteoclast differentiation (GO:0030316), positive regulation of osteoclast differentiation (GO:0045672), bone resorption (GO:0045453). **Upstream vs downstream:** the *NOTCH3* variant and PEST loss are upstream; RANKL induction and osteoclastogenesis are downstream effectors of the bone phenotype.

```
NOTCH3 exon-33 truncation
        │ deletes PEST domain
        ▼
Stabilized NOTCH3 intracellular domain ──► GAIN-OF-FUNCTION Notch signaling (↑HES1/HEY1/2/L)
        │                                             │
        ├───────────── skeletal branch ───────────────┤
        ▼                                             ▼
Osteoblast/osteocyte ↑RANKL          Neural crest / mesenchymal lineages (inferred)
        ▼                                             ▼
↑Osteoclastogenesis                   Meningoceles, dural ectasia, facies,
        ▼                             connective-tissue, cardiac, renal,
Osteopenia / cortical porosity        inner-ear, biliary anomalies
```

### 7. Anatomical Structures Affected

**Primary organs/systems:** nervous system and meninges (spinal dura/arachnoid — lateral meningoceles, dural ectasia; UBERON:0002360 meninges, UBERON:0002240 spinal cord) and skeletal system (vertebrae with scalloping, generalized osteopenia; UBERON:0001474 bone). **Secondary/variable involvement:** cardiovascular (congenital heart defects; UBERON:0000948 heart), genitourinary (renal cysts; UBERON:0002113 kidney), auditory (inner ear/cochlea; UBERON:0001846), hepatobiliary (biliary anomalies; UBERON:0002394 bile duct), craniofacial skeleton and soft tissues, and skin/connective tissue (UBERON:0002097). **Tissue types:** connective tissue, nervous tissue (meninges), bone. **Cell populations:** osteoblasts, osteocytes, osteoclasts, neural crest–derived and mesenchymal cells. **Subcellular:** nucleus (GO:0005634 — NOTCH3 ICD acts as a transcriptional co-activator); plasma membrane (GO:0005886 — receptor); cytoplasm (site of stabilized fragment). **Localization/lateralization:** meningoceles are **bilateral and multiple**, predominantly **thoracolumbar**, most severe in the lower spine.

### 8. Temporal Development

**Onset:** congenital; features usually recognized in infancy or childhood. **Onset pattern:** chronic/insidious. **Progression:** chronic and lifelong; meningoceles/dural ectasia can slowly enlarge; osteopenia is progressive. **Course:** stable-to-progressive rather than episodic or relapsing-remitting. **Critical periods:** prenatal/early-childhood windows for diagnosis and neurological monitoring; surgical timing is dictated by symptomatic meningoceles. **Duration:** lifelong.

### 9. Inheritance and Population

**Inheritance:** autosomal dominant (F006), most cases de novo with two documented vertical transmissions. **Penetrance:** high/complete for the molecular phenotype, though the meningocele feature is not fully obligate (F011). **Expressivity:** highly variable (infantile-severe to adult-mild). **Anticipation:** not described. **Germline mosaicism:** not formally documented but plausible given de novo predominance. **Founder effects/consanguinity:** not applicable (de novo dominant). **Carrier frequency:** not applicable. **Epidemiology:** prevalence <1/1,000,000 (Orphanet); only a few dozen cases reported worldwide; near-balanced sex ratio (~9:7 M:F). **Age distribution:** diagnoses span 5 months to 55 years.

### 10. Diagnostics

**Imaging (central):** whole-spine MRI showing multiple bilateral cystic neural-foraminal masses, neural foraminal widening, dural ectasia, and vertebral scalloping; CT for bony scalloping and canal widening (F008). **Genetic testing (confirmatory):** targeted *NOTCH3* exon-33 sequencing, or WES/WGS; CMA/karyotype are not informative (single-nucleotide/small-indel disorder). Reverse phenotyping (genetics-first) has diagnosed presymptomatic and prenatal cases. **Prenatal:** prenatal exome sequencing after ultrasound findings of cystic hygroma, ventriculomegaly, and facial dysmorphism (F011). **Biomarkers/labs:** no specific biochemical biomarker; no routine metabolomic/proteomic diagnostic. **Clinical criteria:** no formal consensus criteria; diagnosis is gestalt (facies + meningoceles + connective-tissue signs) plus molecular confirmation. **Differential diagnosis:** Hajdu-Cheney syndrome (NOTCH2), Marfan, Ehlers-Danlos (hypermobile/classic), Loeys-Dietz, arterial tortuosity syndrome, neurofibromatosis type 1 (isolated meningoceles), and Copenhagen syndrome (radiological mimic) — distinguished by the *NOTCH3* exon-33 variant and full multisystem gestalt ([PMID: 25821090](https://pubmed.ncbi.nlm.nih.gov/25821090/); [PMID: 40256810](https://pubmed.ncbi.nlm.nih.gov/40256810/)).

### 11. Outcome/Prognosis

**Survival/mortality:** no systematic survival data; LMS is generally not rapidly lethal, though severe infantile presentations with congenital heart defects and failure to thrive carry higher morbidity/mortality risk. **Morbidity:** chronic musculoskeletal pain, joint instability, neurological complications from meningoceles, developmental disability, feeding/growth impairment. **Complications:** neurological sequelae (including iatrogenic nerve damage after meningeal surgery — [PMID: 24311540](https://pubmed.ncbi.nlm.nih.gov/24311540/)), CSF hypotension from meningoceles, Chiari I/syringomyelia/hydrocephalus/tethered cord. **Recovery:** neurosurgical shunting can improve symptoms and regress meningoceles ([PMID: 41432782](https://pubmed.ncbi.nlm.nih.gov/41432782/)), but the syndrome is not curable. **Prognostic factors:** severity of meningoceles/neurological involvement, cardiac anomalies, feeding difficulties. No validated prognostic biomarkers.

### 12. Treatment

**No FDA-approved disease-modifying therapy exists** (F004, F010). Current management is **supportive and neurosurgical** (F008): neurosurgical repair or cyst-subarachnoid/cystoperitoneal shunting of symptomatic meningoceles; management of scoliosis, feeding difficulties (G-tube), cardiac and renal anomalies; physical/occupational therapy for hypotonia and joint instability; audiology support for hearing loss. **Pharmacotherapy:** none disease-specific; the RANKL-axis logic suggests antiresorptives (e.g., denosumab, an anti-RANKL antibody) could be rationally explored for osteopenia, but this is not established for LMS. **Emerging/experimental (preclinical):** Notch3-lowering ASOs (including allele-selective ASOs achieving 70–80% mutant-transcript knockdown) and an anti-Notch3 neutralizing antibody reverse the skeletal phenotype in mouse and iPSC models (F004, F009). **Suggested NCIT terms:** Antisense Oligonucleotide Therapy; Monoclonal Antibody Therapy; Surgical Procedure; Cerebrospinal Fluid Shunt. **Pharmacogenomics:** not applicable.

### 13. Prevention

No primary prevention exists for a de novo genetic disorder. **Secondary prevention:** early molecular diagnosis (including prenatal) enables early neurological monitoring and timely surgical intervention (F008, F011). **Genetic counseling:** recurrence risk is low for parents of a de novo case but 50% for an affected individual's offspring (autosomal dominant); prenatal/preimplantation testing is feasible where a familial variant is known. **Tertiary prevention:** surveillance for and management of neurological, cardiac, renal, and orthopedic complications. No immunization or public-health/environmental interventions apply.

### 14. Other Species / Natural Disease

LMS is a human disorder; no naturally occurring LMS-equivalent disease is documented in companion animals or wildlife (no OMIA equivalent). The gene is evolutionarily conserved: mouse *Notch3* (NCBI Gene 18131) is orthologous to human *NOTCH3*. A **spontaneous murine *Notch3* mutation ("humpback")** exists as a natural model ([PMID: 33860007](https://pubmed.ncbi.nlm.nih.gov/33860007/)). No zoonotic or cross-species transmission applies (non-infectious genetic disease).

### 15. Model Organisms

**Mammalian (mouse):** the engineered **Notch3^em1Ecan^** knock-in (6691TAATGA PEST truncation) recapitulates cancellous and cortical osteopenia; osteocyte-specific conditional induction of the Lehman mutation causes osteopenia in male C57BL/6J mice; the spontaneous "humpback" *Notch3* mutant is a natural model (F009). **Cellular/in vitro:** human iPSC lines (NCRM1/NCRM5 with NOTCH3 c.6692_93insC plus isogenic controls) differentiated to neural crest, mesenchymal, and osteogenic cells demonstrate gain-of-function and enhanced osteogenesis (F002, F009). **Genetic model types:** knock-in, conditional (osteocyte-specific), spontaneous mutant, patient-derived iPSC. **Phenotype recapitulation:** strong for the skeletal/bone-loss component (enabling therapeutic proof-of-concept for ASOs and antibody); **limitations:** do not robustly reproduce the lateral meningoceles or full craniofacial/multisystem phenotype. **Resources:** MGI (Notch3 alleles), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

LMS is best understood as a **NOTCH3 stabilization disorder**. The single molecular lesion — an exon-33 truncation that removes the PEST degron — converts NOTCH3 into a longer-lived, hyperactive transcriptional co-activator. The clearest, experimentally validated downstream consequence is in bone: gain-of-function NOTCH3 in osteoblasts and osteocytes upregulates RANKL, tipping the RANKL/OPG balance toward osteoclast activation and net resorption, producing the osteopenia captured in mouse models. The remaining multisystem features (meningoceles, dural ectasia, craniofacial dysmorphism, connective-tissue laxity, cardiac/renal/inner-ear/biliary anomalies) are clinically well-documented but mechanistically inferred to arise from NOTCH3 gain-of-function in neural-crest and mesenchymal lineages during development — a gap current models do not fully bridge.

The disease sits within an instructive **NOTCH3 allelic and paralogous framework**:

| Disorder | Gene | Variant class | Domain | Mechanism | Core phenotype |
|---|---|---|---|---|---|
| **LMS (Lehman)** | NOTCH3 | Truncating (exon 33) | Intracellular PEST | Gain-of-function (stabilization) | Lateral meningoceles, osteopenia, facies |
| **CADASIL** | NOTCH3 | Cysteine-altering missense | Extracellular EGF repeats | Ectodomain aggregation (GOM) | Cerebral small-vessel disease, stroke, dementia |
| **Biallelic LoF NOTCH3** | NOTCH3 | Biallelic loss-of-function | — | Loss-of-function | Neurodevelopmental disorder, spasticity, childhood stroke |
| **Hajdu-Cheney** | NOTCH2 | Truncating (last exon) | Intracellular PEST | Gain-of-function | Acro-osteolysis, osteoporosis (paralog analogue) |

The parallel between LMS (NOTCH3) and Hajdu-Cheney syndrome (NOTCH2) — both caused by last-exon PEST-truncating gain-of-function variants and both producing bone loss — is a powerful cross-validation of the mechanism and explains why the RANKL-osteoclast axis is central to both.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [25394726](https://pubmed.ncbi.nlm.nih.gov/25394726/) | Landmark gene discovery: exon-33 truncating *NOTCH3* variants; facial and meningocele phenotype | Human clinical/genetic |
| [35760307](https://pubmed.ncbi.nlm.nih.gov/35760307/) | PEST deletion → gain-of-function; osteocyte-specific mouse osteopenia | Model organism |
| [39752389](https://pubmed.ncbi.nlm.nih.gov/39752389/) | iPSC gain-of-function (↑HES1/HEY targets); ASO targeting | In vitro (human iPSC) |
| [33519922](https://pubmed.ncbi.nlm.nih.gov/33519922/) | RANKL-mediated osteoclastogenesis mechanism; "no effective therapies" | Review/model organism |
| [35536858](https://pubmed.ncbi.nlm.nih.gov/35536858/) | Notch3^em1Ecan^ model; in vivo ASO knockdown and osteopenia rescue | Model organism |
| [37704069](https://pubmed.ncbi.nlm.nih.gov/37704069/) | ASO amelioration of cortical osteopenia; drug-target rationale | Model organism |
| [31188489](https://pubmed.ncbi.nlm.nih.gov/31188489/) | Anti-Notch3 antibody reverses skeletal phenotype | Model organism |
| [32526405](https://pubmed.ncbi.nlm.nih.gov/32526405/) | NOTCH paralog specificity; NOTCH3→RANKL→osteoclast axis | Review/mechanistic |
| [31838470](https://pubmed.ncbi.nlm.nih.gov/31838470/) | Neurosurgical review; case count and sex ratio | Human clinical review |
| [32141180](https://pubmed.ncbi.nlm.nih.gov/32141180/) | Phenotype expansion (inner ear, multicystic kidney) | Human clinical |
| [40771185](https://pubmed.ncbi.nlm.nih.gov/40771185/) | First prenatal molecular diagnosis; biliary anomalies | Human clinical |
| [39119451](https://pubmed.ncbi.nlm.nih.gov/39119451/) | LMS without lateral meningoceles — phenotype expansion | Human clinical |
| [40145673](https://pubmed.ncbi.nlm.nih.gov/40145673/) | CADASIL mechanism (extracellular cysteine-altering) — contrast | Review |
| [34172679](https://pubmed.ncbi.nlm.nih.gov/34172679/) | Co-occurring CADASIL/Lehman variants; craniosynostosis | Human clinical |
| [39191170](https://pubmed.ncbi.nlm.nih.gov/39191170/) | Biallelic NOTCH3 genotype-phenotype spectrum | Human clinical |
| [33042242](https://pubmed.ncbi.nlm.nih.gov/33042242/) | Diagnostic MRI appearance (infantile Lehman) | Human clinical |
| [41432782](https://pubmed.ncbi.nlm.nih.gov/41432782/) | Cyst-subarachnoid shunt with meningocele regression | Human clinical |
| [34121137](https://pubmed.ncbi.nlm.nih.gov/34121137/) | Genetics-first (reverse phenotyping) diagnosis in infant | Human clinical |
| [33860007](https://pubmed.ncbi.nlm.nih.gov/33860007/) | "Humpback" natural murine Notch3 mutant | Model organism |
| [40256810](https://pubmed.ncbi.nlm.nih.gov/40256810/) | Novel variant; radiological mimicry (Copenhagen syndrome) | Human clinical |
| [26754023](https://pubmed.ncbi.nlm.nih.gov/26754023/) | 14th case; 80-bp exon-33 deletion; cardiac/feeding phenotype | Human clinical |
| [24311540](https://pubmed.ncbi.nlm.nih.gov/24311540/) | Late diagnosis at 55; vertical transmission; DDx overlap | Human clinical |
| [25821090](https://pubmed.ncbi.nlm.nih.gov/25821090/) | LMS within connective-tissue-disorder differential | Review |
| [31901894](https://pubmed.ncbi.nlm.nih.gov/31901894/) · [35409031](https://pubmed.ncbi.nlm.nih.gov/35409031/) · [35223989](https://pubmed.ncbi.nlm.nih.gov/35223989/) | CADASIL pathobiology (fragmentation/aggregation) — mechanistic contrast | In vitro/review |

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity limits epidemiology.** With only a few dozen reported cases, there are no reliable prevalence/incidence, survival, or natural-history statistics; sex ratio and age-of-onset estimates derive from tiny case series.
2. **Mechanistic gap for non-skeletal features.** The RANKL-osteoclast mechanism is firmly established for bone, but the cellular pathways linking NOTCH3 gain-of-function to meningoceles, dural ectasia, craniofacial dysmorphism, and cardiac/renal/inner-ear/biliary anomalies remain inferred, not demonstrated.
3. **Model-organism incompleteness.** Mouse and iPSC models recapitulate the skeletal phenotype well but do not reproduce the hallmark meningoceles, limiting preclinical testing of therapies for the most clinically significant feature.
4. **No human therapeutic data.** ASO and antibody efficacy is entirely preclinical and demonstrated primarily in male mice; sex-specific effects, meningocele response, and human safety are unknown.
5. **Phenotype still expanding.** Newly reported organ involvements (biliary) and atypical presentations (no meningoceles) indicate the full phenotypic spectrum and its frequencies are not yet defined.
6. **No validated diagnostic criteria or biomarkers**, and no genotype-phenotype correlation study large enough to relate specific exon-33 variants to severity.

---

## Proposed Follow-up Experiments / Actions

1. **Develop a meningocele-capturing model** — conditional NOTCH3-Lehman induction in neural-crest/meningeal lineages (e.g., Wnt1-Cre, PDGFRβ) to test whether dural ectasia and meningoceles can be reproduced and mechanistically dissected.
2. **Test RANKL-axis pharmacology** — evaluate denosumab (anti-RANKL) or bisphosphonates in LMS mouse models and consider registry monitoring of bone outcomes in patients, given the well-defined RANKL mechanism.
3. **Advance allele-selective ASOs toward IND** — extend the 70–80% mutant-knockdown data to systemic and CNS delivery, female cohorts, and long-term safety, with meningocele and craniofacial endpoints where possible.
4. **Establish an international LMS registry and natural-history study** — pool cases to define phenotype frequencies, age-of-onset distributions, complication rates, surgical outcomes, and genotype-phenotype correlations.
5. **Define a multi-organ surveillance protocol** — recommended cardiac, renal, hepatobiliary, audiologic, and spinal imaging screening intervals for molecularly confirmed patients, informed by the expanding phenotype.
6. **Deep molecular profiling of iPSC-derived neural crest/mesenchyme** — transcriptomic and proteomic characterization to identify effectors bridging NOTCH3 gain-of-function to connective-tissue and craniofacial phenotypes, and to nominate additional druggable nodes.

---

*Report compiled from a 5-iteration autonomous investigation: 11 confirmed findings and 30 reviewed papers. Evidence types are distinguished as human clinical/genetic, model organism, in vitro (human iPSC), and review/mechanistic throughout.*


## Artifacts

- [OpenScientist final report](Lateral_Meningocele_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Lateral_Meningocele_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 29 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0005634` (1 mention) - the report calls it "NOTCH3 ICD acts as a transcriptional co-activator"; GO calls it **nucleus**
- `GO:0005886` (1 mention) - the report calls it "receptor"; GO calls it **plasma membrane**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.