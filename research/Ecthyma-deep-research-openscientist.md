---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T12:02:00.242513'
end_time: '2026-09-29T12:17:22.960496'
duration_seconds: 922.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ecthyma
  mondo_id: MONDO:0001404
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 32
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 36
  on_topic: 18
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 26
  verified: 25
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 14
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0200037
    reported_labels:
    - Pustule
    ontology_label: Skin vesicle
  - term_id: NCIT:C61825
    reported_labels:
    - "Topical antibiotics** \u2014 mupirocin"
    ontology_label: Meclocycline
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0009405
    ontology_label: obsolete pathogenesis
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Ecthyma-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Ecthyma-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ecthyma
- **MONDO ID:** MONDO:0001404 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Ecthyma** covering all of the
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

# Ecthyma (MONDO:0001404): A Comprehensive Disease Characterization

*Infectious Disease — Disease Knowledge Base Research Report*

---

## Summary

**Ecthyma is a deep, ulcerative bacterial pyoderma — often described as the "punched-out," crusted, scarring form of impetigo — caused chiefly by group A *Streptococcus* (*Streptococcus pyogenes*, GAS) and/or *Staphylococcus aureus*.** Unlike ordinary (non-bullous) impetigo, which is confined to the epidermis, ecthyma extends through the full epidermis into the dermis, producing an ulcer covered by a thick adherent crust and surrounded by an erythematous, indurated margin; because the dermis is breached, ecthyma heals with scarring. It is an **acquired infectious disease with no causal human gene**, occurring predominantly in children and socioeconomically disadvantaged populations of hot, humid, crowded, resource-poor settings, and is frequently seeded by scabies infestation or minor skin trauma (bites, abrasions).

The disease sits within the impetigo/pyoderma spectrum, whose global burden is enormous — an estimated **>162 million children affected at any one time**, with median childhood prevalence around 12.3% and much higher rates (up to 70%) in marginalized Indigenous and tropical communities. Ecthyma and impetigo are highly treatable with topical or oral antibiotics (cure rates 86–95%) and are preventable through hygiene, wound care, and community-level scabies mass drug administration (MDA), which can reduce impetigo prevalence by 66–94%. The principal systemic complication of streptococcal ecthyma is **acute post-streptococcal glomerulonephritis (APSGN)** caused by nephritogenic GAS M-serotypes (2, 49, 55, 57, 60); importantly, streptococcal *skin* infection — unlike streptococcal *throat* infection — does **not** cause acute rheumatic fever.

A critical nosological caveat runs through this report: the word "ecthyma" names **three distinct entities that must not be conflated**. (1) **Bacterial ecthyma** — the subject of this report — an ulcerative GAS/*S. aureus* pyoderma. (2) **Ecthyma gangrenosum** — a life-threatening septic cutaneous vasculitis, chiefly caused by *Pseudomonas aeruginosa* bacteremia in immunocompromised/neutropenic hosts, with high mortality. (3) **Contagious ecthyma (orf)** — a self-limited parapoxvirus zoonosis of sheep and goats, transmissible to humans. This report characterizes bacterial ecthyma in full and formally bounds the two namesakes to prevent knowledge-base contamination.

---

## Key Findings

### Finding 1 — Ecthyma is an ulcerative pyoderma caused by group A *Streptococcus* and/or *Staphylococcus aureus*

Ecthyma's etiology is bacterial and essentially identical to that of impetigo, differing in depth of invasion rather than causative organism. In a therapeutic series of 55 patients with impetigo, ecthyma, or folliculitis, the causative organisms were epicillin-sensitive *Streptococcus pyogenes* or *Staphylococcus aureus* ([PMID: 782505](https://pubmed.ncbi.nlm.nih.gov/782505/)). In a comparative treatment trial of 127 children with impetigo/ecthyma, skin cultures grew Group A beta-hemolytic streptococci or *S. aureus*, with a 93% healing rate when GAS was isolated and 86% when *S. aureus* was the sole pathogen ([PMID: 359752](https://pubmed.ncbi.nlm.nih.gov/359752/)). Contemporary clinical guidelines classify impetigo and ecthyma together as superficial GAS/*S. aureus* skin and soft-tissue infections ([PMID: 29299899](https://pubmed.ncbi.nlm.nih.gov/29299899/)).

> *"Fifty-five patients with impetigo, ecthyma, or folliculitis caused by epicillin-sensitive strains of Streptococcus pyogenes or Staphylococcus aureus"* — PMID 782505

**Interpretation:** Ecthyma is not a genetically determined disorder; it is an acquired pyogenic infection. Its designation is clinical/morphological (deep, ulcerative, crusted, scarring) rather than microbiological. This is the single most important framing fact for the knowledge base: sections on causal genes, inheritance, penetrance, germline/somatic variants, and gene panels are **not applicable**.

### Finding 2 — Impetigo/pyoderma (including ecthyma) carries a high global burden concentrated in children of tropical, resource-poor, and marginalized settings

A systematic review of 89 studies covering 145,028 children found a median childhood pyoderma/impetigo prevalence of **12.3% (IQR 4.2–19.4%)**, highest in underprivileged children even within high-income countries (median 19.4%, IQR 3.9–43.3%), and estimated that **>162 million children are affected at any one time**, predominantly in tropical, resource-poor contexts ([PMID: 26317533](https://pubmed.ncbi.nlm.nih.gov/26317533/)). In The Gambia, 17.4% of children under 5 had pyoderma, significantly associated with scabies (adjusted OR 2.74, 95% CI 1.61–4.67); 80.8% of lesions grew *S. aureus* and 50.8% GAS ([PMID: 31609963](https://pubmed.ncbi.nlm.nih.gov/31609963/)). In remote Aboriginal communities of northern Australia, up to 70% of children have skin sores, with GAS the major pathogen ([PMID: 10954983](https://pubmed.ncbi.nlm.nih.gov/10954983/)). A pooled Australian analysis estimated community impetigo point prevalence of 27.9% (95% CI 20.0–36.5%) in largely Aboriginal and Torres Strait Islander remote settings ([PMID: 38033025](https://pubmed.ncbi.nlm.nih.gov/38033025/)).

> *"we estimate the global population of children suffering from impetigo at any one time to be in excess of 162 million, predominantly in tropical, resource-poor contexts"* — PMID 26317533

**Interpretation:** The dominant risk factors are environmental and social — young age, hot/humid climate, crowding, poverty, poor hygiene, and especially **scabies co-infestation**, which breaches the skin barrier and seeds bacterial superinfection. This anchors the epidemiology, risk factor, and prevention sections.

### Finding 3 — Streptococcal ecthyma/pyoderma can be followed by acute post-streptococcal glomerulonephritis via nephritogenic GAS serotypes

Nephritogenic M-serotypes associated with post-pyoderma acute glomerulonephritis include M types **2, 49, 55, 57, and 60**, distinct from the throat-associated M1/M12 serotypes ([PMID: 399386](https://pubmed.ncbi.nlm.nih.gov/399386/)). In a New Zealand series, skin was the predominant infection site in 68% of post-streptococcal AGN cases, and pyoderma-associated nephritogenic serotypes 49, 57, and 60 accounted for 63% (19/30) of M-typable isolates ([PMID: 6371610](https://pubmed.ncbi.nlm.nih.gov/6371610/)). Scabies-related pyoderma with GAS is epidemiologically linked to APSGN ([PMID: 31609963](https://pubmed.ncbi.nlm.nih.gov/31609963/)). Critically, streptococcal skin infection does **not** cause acute rheumatic fever, unlike streptococcal pharyngitis ([PMID: 399386](https://pubmed.ncbi.nlm.nih.gov/399386/)).

> *"M-types 2, 49, 55, 57, and 60 are now recognized to be of major importance in AGN following pyoderma"* ... *"Although streptococcal skin infections are quite important in AGN, they do not result in acute rheumatic fever"* — PMID 399386

**Interpretation:** APSGN is the chief serious sequela of streptococcal ecthyma. This distinction (skin → nephritis, not rheumatic fever) is a key prognostic and mechanistic fact and provides the rationale for treating and preventing streptococcal skin infection at the population level.

### Finding 4 — Ecthyma pathogenesis involves bacterial virulence factors that promote dermal invasion, neutrophil evasion, and tissue necrosis

GAS secretes a virulence arsenal — M protein, streptolysin O (SLO), streptolysin S (SLS), streptokinase, hyaluronidase, C5a peptidase, and the cysteine protease SpeB — that collectively mediates skin infection ([PMID: 20607346](https://pubmed.ncbi.nlm.nih.gov/20607346/)). SLS (encoded by the *sagA/pel* locus) is required for dermonecrosis: *sagA* mutants are attenuated in a dermonecrotic mouse infection model ([PMID: 11801184](https://pubmed.ncbi.nlm.nih.gov/11801184/)). SLS and the platelet-activating factor acetylhydrolase Sse act synergistically to inhibit neutrophil recruitment, enabling systemic spread from the skin ([PMID: 28947648](https://pubmed.ncbi.nlm.nih.gov/28947648/)). On the staphylococcal side, in bullous impetigo *S. aureus* exfoliative toxins (ETA/ETB/ETD) act as glutamate-specific serine proteases — "molecular scissors" — that cleave a single peptide bond in **desmoglein 1 (Dsg1)**, destroying keratinocyte cell–cell adhesion in the superficial epidermis ([PMID: 17582744](https://pubmed.ncbi.nlm.nih.gov/17582744/)).

> *"glutamate-specific serine proteases that specifically and efficiently cleave a single peptide bond in the extracellular region of human and mouse desmoglein 1 (Dsg1), a desmosomal intercellular adhesion molecule"* — PMID 17582744

**Interpretation:** These findings supply the molecular causal chain — barrier breach, bacterial adhesion/invasion, immune evasion, and enzymatic/toxin-mediated tissue destruction — that converts a colonized abrasion into a deep necrotic ulcer.

### Finding 5 — "Contagious ecthyma" (orf) is a distinct parapoxvirus zoonosis of sheep/goats — an important nosological namesake

Contagious ecthyma (contagious pustular dermatitis, orf) is caused by **orf virus** (genus *Parapoxvirus*, family *Poxviridae*), infecting sheep and goats worldwide and transmissible to humans as a zoonosis ([PMID: 28571550](https://pubmed.ncbi.nlm.nih.gov/28571550/), [PMID: 3895568](https://pubmed.ncbi.nlm.nih.gov/3895568/)). Morbidity is very high among young unvaccinated animals; humans acquire infection through direct contact with lesions or fomites, developing self-limited cutaneous nodules. Histology shows proliferative dermatitis with epidermal hyperplasia, ballooning degeneration, and eosinophilic intracytoplasmic inclusion bodies in keratinocytes ([PMID: 20833245](https://pubmed.ncbi.nlm.nih.gov/20833245/), [PMID: 23201244](https://pubmed.ncbi.nlm.nih.gov/23201244/)). Orf virus encodes a **VEGF homolog (OV132)** that drives dermal capillary proliferation; its deletion attenuates the virus ([PMID: 11044114](https://pubmed.ncbi.nlm.nih.gov/11044114/), [PMID: 36484827](https://pubmed.ncbi.nlm.nih.gov/36484827/)). Live attenuated vaccines exist for animals ([PMID: 3895568](https://pubmed.ncbi.nlm.nih.gov/3895568/)).

> *"The virus is a causative agent of orf in humans or contagious ecthyma in animals which is mostly seen in sheep, goat and cattle"* — PMID 28571550

**Interpretation:** Contagious ecthyma is a viral disease with entirely different etiology, host range, mechanism (VEGF-driven angiogenesis), and prevention (vaccination) from bacterial ecthyma. It is documented here to prevent knowledge-base conflation and to inform the "Other Species / Natural Disease" section.

### Finding 6 — Ecthyma/impetigo is preventable and treatable: antibiotics cure lesions and scabies MDA reduces pyoderma at the population level

A Cochrane review (68 RCTs, 5,578 participants) found topical antibiotics superior to placebo for impetigo (pooled OR 6.49, 95% CI 3.93–10.73) and topical mupirocin superior to oral erythromycin, with no topical antibiotic clearly superior to another ([PMID: 22258953](https://pubmed.ncbi.nlm.nih.gov/22258953/) / [PMID: 15106198](https://pubmed.ncbi.nlm.nih.gov/15106198/)). Benzathine penicillin cured 94.4% of impetigo/ecthyma in children ([PMID: 359752](https://pubmed.ncbi.nlm.nih.gov/359752/)); twice-daily epicillin cured ~95% ([PMID: 782505](https://pubmed.ncbi.nlm.nih.gov/782505/)). At the population level, ivermectin-based scabies MDA reduced impetigo prevalence dramatically — from 21.4% to as low as 1.9% (94% relative reduction in the ivermectin group) in Fiji ([PMID: 26650152](https://pubmed.ncbi.nlm.nih.gov/26650152/)) — and reduced hospitalizations for skin and soft-tissue infections by 17% (IRR 0.83, 95% CI 0.74–0.94) ([PMID: 35345391](https://pubmed.ncbi.nlm.nih.gov/35345391/)). In the Solomon Islands, ivermectin MDA reduced impetigo prevalence by 74% ([PMID: 30956111](https://pubmed.ncbi.nlm.nih.gov/30956111/)); a meta-analysis found scabies MDA reduced impetigo prevalence by 66% ([PMID: 35088849](https://pubmed.ncbi.nlm.nih.gov/35088849/)).

> *"The prevalence declined from 21.4% to 14.6% in the standard-care group"* — PMID 26650152

**Interpretation:** Both individual treatment and community-level prevention are highly effective. Because scabies is a dominant upstream driver, scabies control is a key public-health lever against ecthyma, its complications, and downstream APSGN.

### Finding 7 — The microbial spectrum includes MSSA, community-associated MRSA (often exfoliative-toxin-positive), and GAS; MRSA prevalence is region-dependent

In a Japanese impetigo series, 17 MRSA strains from children belonged to 7 clones, and 14/17 carried exfoliative toxin a or b genes ([PMID: 21327935](https://pubmed.ncbi.nlm.nih.gov/21327935/)). In a Canadian pediatric emergency department, *S. aureus* was the most common SSTI organism (66% MSSA, 33% MRSA), though overall community MRSA incidence was low ([PMID: 24634682](https://pubmed.ncbi.nlm.nih.gov/24634682/)). In Egyptian children with pyogenic skin infections, MSSA predominated (114/121) with CA-MRSA in only 4 ([PMID: 22928620](https://pubmed.ncbi.nlm.nih.gov/22928620/)). CA-MRSA SSTIs impose substantial indirect costs (€1,814–8,224 per patient) ([PMID: 34895206](https://pubmed.ncbi.nlm.nih.gov/34895206/)).

> *"Fourteen of the 17 strains carried exfoliative toxin a or b gene"* — PMID 21327935

**Interpretation:** Empiric therapy should be guided by local resistance patterns. Where CA-MRSA is prevalent, beta-lactam monotherapy may fail; where it is rare, beta-lactams remain effective. This directly informs the pharmacotherapy and antibiogram/diagnostic sections.

### Finding 8 — Ecthyma gangrenosum (distinct namesake) is a life-threatening septic vasculitis, chiefly *Pseudomonas aeruginosa*, in immunocompromised/neutropenic hosts

Ecthyma gangrenosum (EG) is *"a potentially life-threatening, systemic infection generally caused by Pseudomonas aeruginosa"* ([PMID: 35984202](https://pubmed.ncbi.nlm.nih.gov/35984202/)). It presents as erythematous/hemorrhagic macules progressing to necrotic ulcers with a black eschar, most often accompanying bacteremia in immunocompromised individuals ([PMID: 41968428](https://pubmed.ncbi.nlm.nih.gov/41968428/)). *Pseudomonas* sepsis with EG carries a high mortality rate, requiring immediate appropriate antibiotics ([PMID: 15553052](https://pubmed.ncbi.nlm.nih.gov/15553052/)). EG can also be caused by *S. aureus* (of 18 reported *S. aureus* EG patients, 33% had a hematological malignancy and 56% were MRSA; [PMID: 35984202](https://pubmed.ncbi.nlm.nih.gov/35984202/)) and rarely by other organisms including *Streptococcus pyogenes* ([PMID: 42491904](https://pubmed.ncbi.nlm.nih.gov/42491904/)). Severe pediatric EG has occurred with neutropenia and a novel *HELLS* variant ([PMID: 42437106](https://pubmed.ncbi.nlm.nih.gov/42437106/)).

> *"Ecthyma gangrenosum (EG) is a potentially life-threatening, systemic infection generally caused by Pseudomonas aeruginosa"* — PMID 35984202

**Interpretation:** EG is a fundamentally different disease — a manifestation of systemic sepsis in the immunocompromised, with high mortality — and should be recorded as a related-but-distinct entity, not as a severity grade of bacterial ecthyma.

---

## Structured Report by Research Section

### 1. Disease Information

**Overview.** Ecthyma is a deep bacterial pyoderma characterized by punched-out ulcers with a thick, adherent, often yellow-grey crust and a raised, indurated, violaceous margin. It represents a full-thickness (epidermal + dermal) extension of impetigo; because it breaches the dermis, it heals with scarring, unlike superficial impetigo. Lesions are typically found on the lower legs and buttocks, and are frequently multiple.

**Identifiers.**
- **MONDO:** MONDO:0001404 (ecthyma)
- **MeSH:** Ecthyma (D004473)
- **ICD-10:** L08.0 (pyoderma) is commonly applied; ecthyma is grouped under bacterial skin infections. ICD-11: 1B70-range bacterial cellulitis/pyoderma codes.
- **SNOMED CT:** Ecthyma (disorder)
- **OMIM / Orphanet:** Not applicable — ecthyma is an acquired infection, not a Mendelian or rare genetic disorder, so it has no OMIM phenotype number and no Orphanet rare-disease code as a genetic entity.

**Synonyms / alternative names.** Ulcerative impetigo; deep impetigo; "impetigo of the dermis." (Note the non-synonyms that share the name: *ecthyma gangrenosum* and *contagious ecthyma / orf* — see Findings 5 and 8.)

**Data source type.** Disease-level information here is derived from **aggregated disease-level resources** — systematic reviews, clinical trials, treatment guidelines, and microbiological case series — not from individual EHR patient records.

### 2. Etiology

**Causal factors.** Infectious. Primary pathogens: **group A *Streptococcus* (*S. pyogenes*)** and ***Staphylococcus aureus*** (MSSA and CA-MRSA) (Findings 1, 7). No genetic causation in the host.

**Risk factors (environmental/social).** Young age (children); hot, humid climate; crowding and poverty; poor hygiene; minor skin trauma (insect bites, abrasions); and — a dominant driver — **scabies infestation** (aOR 2.74 for pyoderma; Finding 2). Indigenous and marginalized populations bear disproportionate burden.

**Genetic risk factors.** None established for host susceptibility to ordinary ecthyma. (A single pediatric *ecthyma gangrenosum* case linked to a novel *HELLS* variant with neutropenia is a rare exception in the distinct EG entity — Finding 8 — not bacterial ecthyma.)

**Protective factors.** Environmental: intact skin barrier, good hygiene, wound care, treatment of scabies, and reduced crowding. Scabies MDA is protective at the population level (Finding 6). No genetic protective variants are known.

**Gene–environment interactions.** Not applicable for the host. The relevant "interaction" is pathogen genotype × host environment: nephritogenic GAS M-serotypes (2, 49, 55, 57, 60) in disadvantaged, scabies-endemic communities produce clusters of post-pyoderma APSGN (Finding 3).

### 3. Phenotypes

| Phenotype | Type | Suggested HPO term | Characteristics |
|---|---|---|---|
| Skin ulcer (punched-out, dermal) | Physical manifestation | HP:0200042 (Skin ulcer) | Childhood onset; moderate severity; often multiple, lower legs/buttocks |
| Adherent crust / eschar | Clinical sign | HP:0011368 (Epidermal thickening) / crusting | Thick yellow-grey adherent crust over the ulcer |
| Purulent discharge / pustule | Clinical sign | HP:0200037 (Pustule) | Early lesion is a vesicopustule that ulcerates |
| Scarring on healing | Physical manifestation | HP:0000987 (Abnormal scarring) | Distinguishes ecthyma from impetigo; consequence of dermal involvement |
| Regional lymphadenopathy | Clinical sign | HP:0002716 (Lymphadenopathy) | Frequent with local infection |
| Erythema / induration at margin | Clinical sign | HP:0000988 (Skin rash) | Raised violaceous indurated border |
| Hematuria / edema (if APSGN) | Laboratory / clinical (complication) | HP:0000790 (Hematuria) | Downstream complication of nephritogenic GAS |

**Onset:** typically childhood; **severity:** mild-to-moderate locally (severe if complicated by APSGN or systemic spread); **progression:** episodic/acute, self-limited with treatment; **frequency:** ulceration and crusting are near-universal defining features. **Quality of life:** local discomfort, pruritus, cosmetic scarring; population-level QoL and economic burden are substantial in endemic settings (indirect CA-MRSA SSTI costs €1,814–8,224/patient; Finding 7).

### 4. Genetic / Molecular Information

**Not applicable to the host.** Ecthyma has **no causal human gene, no pathogenic germline/somatic variants, no modifier genes, no host epigenetic signature, and no chromosomal abnormality.** It is an acquired bacterial infection (Finding 1). The relevant "molecular genetics" is that of the **pathogen**: GAS virulence genes (*emm*/M protein, *sagA/pel* → streptolysin S, *slo*, *ska* streptokinase, *speB*, *scpA* C5a peptidase, hyaluronidase) and *S. aureus* exfoliative toxin genes (*eta*, *etb*, *etd*) (Findings 4, 7). Nephritogenic potential maps to specific GAS *emm*/M-serotypes (2, 49, 55, 57, 60) (Finding 3).

### 5. Environmental Information

**Environmental factors:** heat, humidity, crowding, poor sanitation. **Lifestyle/social factors:** poverty, limited access to hygiene and healthcare, and — critically — untreated scabies (Finding 2). **Infectious agents (NCBI Taxonomy):** *Streptococcus pyogenes* (txid1314); *Staphylococcus aureus* (txid1280). Scabies mite *Sarcoptes scabiei* (txid52283) acts as a barrier-breaching co-factor. For the distinct namesakes: *Pseudomonas aeruginosa* (txid287, ecthyma gangrenosum) and Orf virus (txid10258, contagious ecthyma).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (bacterial ecthyma):**

1. **Skin barrier breach** (scabies burrows, insect bites, abrasion, or maceration) → **leads to** exposure of dermal/epidermal tissue to skin-colonizing bacteria. *(Demonstrated epidemiologically: scabies aOR 2.74, PMID 31609963.)*
2. Colonizing **GAS and/or *S. aureus* adhere and invade** through the epidermis into the dermis → **results in** establishment of infection deeper than in superficial impetigo. *(Inferred from clinical morphology and microbiology.)*
3. **Bacterial virulence factors are deployed** — GAS M protein (anti-phagocytic), streptokinase (fibrinolysis, spread), hyaluronidase (matrix degradation), C5a peptidase (complement evasion), SpeB (protease), and streptolysins O and S (cytolysis); *S. aureus* exfoliative toxins cleave Dsg1 → **leads to** keratinocyte/tissue destruction and immune evasion. *(Demonstrated: PMID 20607346, 11801184, 17582744.)*
4. **Streptolysin S (SagA/Pel) mediates dermonecrosis**, and SLS + Sse synergistically **inhibit neutrophil recruitment** → **results in** local tissue necrosis, ulcer formation, and potential for systemic spread. *(Demonstrated in mouse models: PMID 11801184, 28947648.)*
5. **Neutrophilic dermal inflammation + necrosis** → **produces** the clinical punched-out ulcer with adherent crust and indurated margin; dermal involvement → **leads to** scarring on healing. *(Inferred from histopathology and clinical description.)*

   **Branch A (local resolution):** appropriate antibiotics + wound care → lesion clearance (86–95% cure; Finding 6).

   **Branch B (immune-mediated sequela):** infection by a **nephritogenic GAS M-serotype (2/49/55/57/60)** → circulating streptococcal antigens/immune complexes and complement activation deposit in glomeruli → **results in acute post-streptococcal glomerulonephritis** (hematuria, edema, hypertension). Streptococcal *skin* infection does **not** trigger acute rheumatic fever. *(Demonstrated epidemiologically/serotypically: PMID 399386, 6371610.)*

**Molecular pathways / processes:** bacterial adhesion and invasion; complement evasion (C5a peptidase); cytolysis (pore-forming streptolysins); ECM degradation (hyaluronidase, streptokinase); host innate immune response (neutrophil recruitment — inhibited by SLS/Sse). **Suggested GO terms:** GO:0006954 (inflammatory response), GO:0042742 (defense response to bacterium), GO:0001909 (leukocyte-mediated cytotoxicity), GO:0030593 (neutrophil chemotaxis), GO:0009405 (pathogenesis). **Suggested CL terms:** CL:0000775 (neutrophil), CL:0000312 (keratinocyte), CL:0000738 (leukocyte), CL:0002187 (basal cell of epidermis).

### 7. Anatomical Structures Affected

- **Organ:** skin (UBERON:0002097, skin of body; UBERON:0002199, integumental system).
- **Tissue/cell:** epidermis (UBERON:0001003) and **dermis (UBERON:0002067)** — the defining feature vs. impetigo is dermal involvement; keratinocytes (CL:0000312) and infiltrating neutrophils (CL:0000775).
- **Secondary organ (complication):** kidney/glomerulus (UBERON:0000074, renal glomerulus) in APSGN.
- **Subcellular:** desmosome (GO:0030057) targeted by exfoliative toxin (Dsg1 cleavage); plasma membrane (GO:0005886) targeted by streptolysins.
- **Localization:** typically **lower extremities** and buttocks; often multiple; laterality variable (frequently bilateral in disseminated disease).

### 8. Temporal Development

**Onset:** acute, most commonly in childhood; lesions evolve over days from vesicopustule to crusted ulcer. **Progression:** without treatment, ulcers enlarge and persist for weeks; with treatment, resolution within 1–2 weeks (Finding 6). **Course:** self-limited to episodic; recurrence common in endemic/scabies settings. **Critical window:** early antibiotic treatment prevents progression and reduces the pool of nephritogenic GAS, limiting APSGN risk. APSGN, when it occurs, typically follows skin infection by ~1–3 weeks.

### 9. Inheritance and Population

**Epidemiology:** median childhood impetigo/pyoderma prevalence 12.3% (IQR 4.2–19.4%); >162 million children affected globally at any time; up to 27.9–70% point prevalence in remote/Indigenous communities (Finding 2). **Inheritance:** not applicable (acquired infection; no Mendelian pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency). **Demographics:** disproportionately affects children; Indigenous, tropical, and socioeconomically disadvantaged populations; hot/wet-season seasonality; no strong intrinsic sex bias (exposure-driven).

### 10. Diagnostics

**Clinical diagnosis** is primary — characteristic punched-out, crusted, scarring ulcers. **Microbiology:** Gram stain and **bacterial culture with susceptibility testing** of lesion swab/exudate to identify GAS vs *S. aureus* and detect MRSA (Findings 1, 7). **Serology:** anti-DNase B (superior to ASO after streptococcal pyoderma) supports recent GAS skin infection and is useful when APSGN is suspected ([PMID: 6995881](https://pubmed.ncbi.nlm.nih.gov/6995881/)). **Antibiogram testing** is recommended where CA-MRSA is prevalent to guide therapy (Finding 7). **Genetic/omics testing:** not applicable. **Differential diagnosis:** impetigo (superficial, no scarring), **ecthyma gangrenosum** (immunocompromised, necrotic eschar, *Pseudomonas* bacteremia — Finding 8), venous/arterial ulcers, cutaneous leishmaniasis, and **contagious ecthyma/orf** (animal contact, viral nodule — Finding 5).

### 11. Outcome / Prognosis

Prognosis is **excellent with treatment**: cure rates 86–95% (Findings 1, 6). Untreated lesions heal slowly with scarring. **Mortality is essentially nil** for uncomplicated bacterial ecthyma. **Complications:** scarring; regional cellulitis/lymphangitis; rarely systemic spread; and, most importantly, **APSGN** via nephritogenic GAS (Finding 3), which is usually self-limiting in children but can cause hypertension and, rarely, renal impairment. (By sharp contrast, the namesake **ecthyma gangrenosum carries high mortality** due to underlying *Pseudomonas* sepsis and immunocompromise — Finding 8.) **Prognostic factors:** promptness of antibiotic therapy, pathogen (nephritogenic GAS serotype → APSGN risk), MRSA status, host immune status, and scabies control.

### 12. Treatment

**Pharmacotherapy (NCIT: antibiotic therapy, NCIT:C15844):**
- **Topical antibiotics** — mupirocin (NCIT:C61825), fusidic acid — first line for limited disease; superior to placebo (OR 6.49) and to oral erythromycin (Finding 6).
- **Oral antibiotics** for extensive/multiple lesions or ecthyma (deeper) — anti-staphylococcal penicillins (flucloxacillin/dicloxacillin/cloxacillin), first-generation cephalosporins (cephalexin), amoxicillin-clavulanate; **benzathine penicillin** for confirmed GAS (94.4% cure; Finding 6).
- **MRSA-active agents** (clindamycin, trimethoprim-sulfamethoxazole, doxycycline) where CA-MRSA is prevalent (Finding 7).

**Treatment strategy:** guided by lesion extent and local resistance; culture-directed therapy where CA-MRSA is common. **Advanced/gene/cell/RNA/targeted/immunotherapies, surgery:** not applicable (simple debridement of crust may aid healing). **Adverse events:** oral antibiotics cause more (mainly gastrointestinal) side effects than topical (Finding 6).

### 13. Prevention

- **Primary:** hygiene, wound care, reduction of crowding, and **treatment of scabies** — including **ivermectin-based mass drug administration**, which reduces impetigo prevalence by 66–94% and SSTI hospitalizations by 17% (Finding 6). NCIT: ivermectin therapy.
- **Secondary:** early detection and prompt antibiotic treatment of skin sores to prevent APSGN and interrupt community transmission of nephritogenic GAS.
- **Tertiary:** monitoring for and managing APSGN.
- **Immunization:** no licensed human vaccine; a Strep A vaccine is in development and would address the broader GAS disease burden. (Note: live attenuated vaccines exist for *animal* contagious ecthyma/orf — Finding 5 — a different disease.)
- **Public health:** integrated skin-health programs combining scabies MDA, hygiene promotion, and antibiotic access are the cornerstone of population-level prevention.

### 14. Other Species / Natural Disease

Bacterial ecthyma as defined here is primarily a human disease. The dominant cross-species consideration is the **namesake "contagious ecthyma" (orf)**, a **parapoxvirus** disease of **sheep (*Ovis aries*, NCBI:txid9940) and goats (*Capra hircus*, NCBI:txid9925)**, with documented cases also in **reindeer** (*Rangifer tarandus*, PMID 23201244) and **camels** (camel contagious ecthyma, PMID 6145344). Orf is **zoonotic** — transmissible to humans via direct animal/fomite contact, producing self-limited nodules (Finding 5). Its mechanism (viral VEGF/OV132-driven angiogenesis and epidermal proliferation) and prevention (live attenuated vaccination) are entirely distinct from bacterial ecthyma. **This must be recorded as a separate entity in the knowledge base.**

### 15. Model Organisms

- **Mouse dermonecrosis model** — the principal experimental system for streptococcal skin infection: *sagA/pel* (SLS) mutants are attenuated for dermonecrosis, and SLS+Sse mutants show impaired neutrophil evasion (Finding 4; PMID 11801184, 28947648). Recapitulates dermal necrosis and immune evasion; limitation: does not reproduce human APSGN or community epidemiology.
- **Mouse Dsg1 cleavage model** — demonstrates exfoliative-toxin-mediated epidermal splitting (PMID 17582744), relevant to the staphylococcal/bullous end of the impetigo–ecthyma spectrum.
- **Animal models of contagious ecthyma (orf)** — experimental parapoxvirus infection in rabbits, mice, reindeer, and goats (PMID 20833245, 23201244, 36484827) — pertain to the viral namesake, not bacterial ecthyma.

No genetic (knockout/transgenic) mouse model of *host* susceptibility to bacterial ecthyma exists, consistent with its non-genetic etiology.

---

## Mechanistic Model / Interpretation

```
          [ Barrier breach: scabies / bites / trauma ]
                          |  (scabies aOR 2.74)
                          v
        [ GAS and/or S. aureus adhesion & dermal invasion ]
                          |
        +-----------------+------------------------------+
        v                 v                              v
 [ GAS virulence ]  [ S. aureus ETs ]           [ Immune evasion ]
  M protein, SLO,    cleave Dsg1                  C5a peptidase;
  SLS(sagA/pel),     ("molecular                  SLS+Sse inhibit
  streptokinase,     scissors")                   neutrophil recruitment
  hyaluronidase,          |                              |
  SpeB, C5a pept.         v                              |
        |          epidermal split              (enables systemic spread)
        v          (bullous end)                         |
 [ Dermonecrosis + neutrophilic inflammation ] <---------+
                          |
                          v
       [ Punched-out ULCER + adherent crust -> SCARRING ]
                          |
        +-----------------+---------------------+
        v (Branch A: treat)                      v (Branch B: nephritogenic GAS)
 [ Antibiotics -> cure 86-95% ]       [ Immune-complex APSGN - M2/49/55/57/60 ]
                                      [ NOT acute rheumatic fever ]
```

The unifying model: **ecthyma is impetigo that has invaded the dermis.** The same organisms and virulence machinery are involved; depth of invasion (favored by barrier breach, and by streptolysin-S-mediated dermonecrosis) determines the ulcerative, scarring phenotype. Upstream drivers are environmental/social (scabies, crowding, poverty, climate); downstream, the chief systemic hazard is nephritogenic-serotype-mediated APSGN. Prevention acts furthest upstream (scabies control, hygiene) and treatment acts at the lesion (antibiotics).

### Distinguishing the three "ecthymas"

| Feature | **Bacterial ecthyma** (this report) | **Ecthyma gangrenosum** | **Contagious ecthyma (orf)** |
|---|---|---|---|
| Class | MONDO:0001404; bacterial pyoderma | Cutaneous manifestation of sepsis | Viral zoonosis |
| Pathogen | GAS, *S. aureus* | *Pseudomonas aeruginosa* (mostly); also *S. aureus* | Orf virus (Parapoxvirus) |
| Host | Healthy children, disadvantaged | Immunocompromised/neutropenic | Sheep/goats; humans via contact |
| Lesion | Punched-out crusted ulcer, scars | Hemorrhagic macule → necrotic black eschar | Proliferative nodule, self-limited |
| Mortality | ~nil (uncomplicated) | High (sepsis) | Nil (self-limited) |
| Key ref (PMID) | 782505, 359752 | 35984202, 15553052 | 28571550, 3895568 |

---

## Evidence Base

| PMID | Role in this report | Support / Challenge |
|---|---|---|
| [782505](https://pubmed.ncbi.nlm.nih.gov/782505/) | Etiology & treatment (GAS/*S. aureus*; ~95% cure) | Supports F1, F6 |
| [359752](https://pubmed.ncbi.nlm.nih.gov/359752/) | Pathogens & penicillin efficacy (93%/86%/94.4%) | Supports F1, F6 |
| [29299899](https://pubmed.ncbi.nlm.nih.gov/29299899/) | Guideline grouping impetigo/ecthyma | Supports F1 |
| [26317533](https://pubmed.ncbi.nlm.nih.gov/26317533/) | Global burden (>162M children; 12.3%) | Supports F2 |
| [31609963](https://pubmed.ncbi.nlm.nih.gov/31609963/) | Scabies risk (aOR 2.74); microbiology | Supports F2, F3 |
| [10954983](https://pubmed.ncbi.nlm.nih.gov/10954983/) | Up to 70% in Aboriginal children | Supports F2 |
| [38033025](https://pubmed.ncbi.nlm.nih.gov/38033025/) | Pooled Australian impetigo prevalence 27.9% | Supports F2 |
| [399386](https://pubmed.ncbi.nlm.nih.gov/399386/) | Nephritogenic serotypes; no rheumatic fever | Supports F3 |
| [6371610](https://pubmed.ncbi.nlm.nih.gov/6371610/) | Skin site 68%; serotypes 49/57/60 | Supports F3 |
| [6995881](https://pubmed.ncbi.nlm.nih.gov/6995881/) | M type 57 skin AGN; anti-DNase B > ASO | Supports F3, diagnostics |
| [20607346](https://pubmed.ncbi.nlm.nih.gov/20607346/) | GAS virulence factor catalog | Supports F4 |
| [11801184](https://pubmed.ncbi.nlm.nih.gov/11801184/) | SLS (*sagA/pel*) required for dermonecrosis | Supports F4 |
| [28947648](https://pubmed.ncbi.nlm.nih.gov/28947648/) | SLS + Sse inhibit neutrophil recruitment | Supports F4 |
| [17582744](https://pubmed.ncbi.nlm.nih.gov/17582744/) | Exfoliative toxins cleave Dsg1 | Supports F4 |
| [22258953](https://pubmed.ncbi.nlm.nih.gov/22258953/) / [15106198](https://pubmed.ncbi.nlm.nih.gov/15106198/) | Cochrane: topical antibiotics OR 6.49 | Supports F6 |
| [26650152](https://pubmed.ncbi.nlm.nih.gov/26650152/) | Scabies MDA reduces impetigo | Supports F6 |
| [35345391](https://pubmed.ncbi.nlm.nih.gov/35345391/) | MDA reduces SSTI hospitalizations 17% | Supports F6 |
| [30956111](https://pubmed.ncbi.nlm.nih.gov/30956111/) | Ivermectin MDA reduces impetigo 74% | Supports F6 |
| [35088849](https://pubmed.ncbi.nlm.nih.gov/35088849/) | Meta-analysis: MDA reduces impetigo 66% | Supports F6 |
| [21327935](https://pubmed.ncbi.nlm.nih.gov/21327935/) | Impetigo MRSA clones carry ET genes | Supports F7 |
| [24634682](https://pubmed.ncbi.nlm.nih.gov/24634682/) | MSSA 66% / MRSA 33% in pediatric SSTI | Supports F7 |
| [22928620](https://pubmed.ncbi.nlm.nih.gov/22928620/) | MSSA predominance in Egyptian children | Supports F7 |
| [34895206](https://pubmed.ncbi.nlm.nih.gov/34895206/) | Indirect SSTI costs €1,814–8,224 | Supports F7 |
| [28571550](https://pubmed.ncbi.nlm.nih.gov/28571550/) | Orf = contagious ecthyma definition | Supports F5 |
| [11044114](https://pubmed.ncbi.nlm.nih.gov/11044114/) / [36484827](https://pubmed.ncbi.nlm.nih.gov/36484827/) | Viral VEGF (OV132) drives orf | Supports F5 |
| [3895568](https://pubmed.ncbi.nlm.nih.gov/3895568/) | Attenuated live vaccine for orf | Supports F5 |
| [20833245](https://pubmed.ncbi.nlm.nih.gov/20833245/) / [23201244](https://pubmed.ncbi.nlm.nih.gov/23201244/) | Orf histopathology; animal models | Supports F5 |
| [35984202](https://pubmed.ncbi.nlm.nih.gov/35984202/) | EG definition; *S. aureus* EG | Supports F8 |
| [15553052](https://pubmed.ncbi.nlm.nih.gov/15553052/) | EG high mortality | Supports F8 |
| [41968428](https://pubmed.ncbi.nlm.nih.gov/41968428/) / [42491904](https://pubmed.ncbi.nlm.nih.gov/42491904/) / [42437106](https://pubmed.ncbi.nlm.nih.gov/42437106/) | EG host/pathogen spectrum | Supports F8 |

---

## Limitations and Knowledge Gaps

1. **Ecthyma-specific data are sparse.** Nearly all quantitative evidence (prevalence, treatment cure rates, MDA effects) is reported for the **impetigo/pyoderma spectrum as a whole**, with ecthyma grouped in. Ecthyma-specific incidence, scarring rates, and complication rates are not separately quantified in the literature reviewed.
2. **APSGN causal attribution.** The link between ecthyma specifically (vs. impetigo generally) and APSGN rests on serotype/site epidemiology, not on ecthyma-stratified prospective cohorts.
3. **Mechanistic inference.** The dermonecrosis and neutrophil-evasion mechanisms come from **mouse models and in vitro studies** of GAS/*S. aureus*, not from human ecthyma lesion studies; the final steps (ulcer/scar formation) are inferred from clinical description and general histopathology.
4. **No host-omics.** Because ecthyma is non-genetic, there are no transcriptomic, proteomic, metabolomic, or single-cell datasets of host disease — a genuine absence, not a search gap.
5. **Nosological confusion risk.** The shared name across three unrelated diseases is the single greatest hazard for an automated knowledge base; findings F5 and F8 exist specifically to bound this.
6. **Cochrane efficacy statistic partly unverified.** The topical-antibiotic OR 6.49 (F6) is drawn from the Cochrane abstract text and is consistent across two Cochrane versions (PMID 22258953/15106198), but the specific snippet was not independently re-verified against full text.

---

## Proposed Follow-up Actions

1. **Disaggregate ecthyma from impetigo** in future data extraction: seek cohort/registry data reporting ecthyma-specific prevalence, scarring, and APSGN rates.
2. **Encode the three-entity disambiguation** explicitly in the knowledge base with cross-references (MONDO ecthyma vs. ecthyma gangrenosum vs. contagious ecthyma), including distinct pathogen, host, mechanism, and prognosis fields.
3. **Populate pathogen-genotype annotations**: link GAS virulence genes (*sagA/pel*, *slo*, *speB*, *emm* nephritogenic serotypes) and *S. aureus* *eta/etb/etd* as the molecular substrate, since host genes are absent.
4. **Attach diagnostic decision support**: culture + susceptibility (region-dependent MRSA), anti-DNase B for suspected post-streptococcal AGN.
5. **Prevention linkage**: connect ecthyma prevention to scabies MDA programs and to the pipeline Strep A vaccine as future primary prevention.
6. **Verify the Cochrane OR** against full text and record the corresponding confidence interval and heterogeneity.

---

*Report compiled from a 5-iteration autonomous literature investigation: 8 confirmed findings, 53 papers reviewed. Evidence types: human clinical trials and systematic reviews (treatment, epidemiology, APSGN), microbiological case series (etiology, resistance), and model-organism/in-vitro studies (virulence mechanisms).*


## Artifacts

- [OpenScientist final report](Ecthyma-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Ecthyma-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 36 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 20 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0200037` (1 mention) - the report calls it "Pustule"; HP calls it **Skin vesicle**
- `NCIT:C61825` (1 mention) - the report calls it "Topical antibiotics** — mupirocin"; NCIT calls it **Meclocycline**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0009405` (obsolete pathogenesis) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000987` (1 mention) - the report calls it "Abnormal scarring"; HP calls it **Atypical scarring of skin**, and lists "Atypical scarring" among its other names
- `GO:0009405` (1 mention) - the report calls it "pathogenesis"; GO calls it **obsolete pathogenesis**
- `UBERON:0001003` (1 mention) - the report calls it "Tissue/cell:** epidermis"; UBERON calls it **skin epidermis**, and lists "vertebrate epidermis" among its other names
- `GO:0030057` (1 mention) - the report calls it "Subcellular:** desmosome"; GO calls it **desmosome**, and lists "spot desmosome" among its other names