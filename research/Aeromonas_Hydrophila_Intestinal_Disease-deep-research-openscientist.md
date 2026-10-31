---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T23:34:38.232591'
end_time: '2026-09-29T23:53:26.511652'
duration_seconds: 1128.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Aeromonas Hydrophila Intestinal Disease
  mondo_id: MONDO:0024459
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
citation_count: 46
reference_validation:
  total_references: 46
  verified: 46
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 46
  on_topic: 18
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 25
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 16
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Aeromonas_Hydrophila_Intestinal_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Aeromonas_Hydrophila_Intestinal_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aeromonas Hydrophila Intestinal Disease
- **MONDO ID:** MONDO:0024459 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Aeromonas Hydrophila Intestinal Disease** covering all of the
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

# Aeromonas hydrophila Intestinal Disease — Comprehensive Disease Characterization

**MONDO ID:** MONDO:0024459 | **Category:** Infectious Disease (bacterial gastroenteritis) | **Report date:** 2026-09-30

---

## Summary

**Aeromonas hydrophila intestinal disease is an acute, non-genetic infectious gastroenteritis caused by the Gram-negative, motile, waterborne/foodborne bacterium *Aeromonas hydrophila* (NCBI Taxonomy txid644).** Clinically it spans a wide spectrum from mild self-limited watery diarrhea, through severe cholera-like "rice-water" diarrhea with dehydration, to dysentery-like bloody diarrhea. In a clinical series of 50 patients with *Aeromonas* acute gastroenteritis, 26% presented with cholera-like rice-water stools and severe dehydration, 16% with a dysentery-like picture, and one died of dehydration and septicaemia ([PMID: 29205196](https://pubmed.ncbi.nlm.nih.gov/29205196/)). Because *Aeromonas* is recovered at similar rates from symptomatic and asymptomatic stools, its status as a true enteric pathogen versus a commensal/coloniser remains debated ([PMID: 39388901](https://pubmed.ncbi.nlm.nih.gov/39388901/)).

The disease is **toxin-driven and multifactorial**. Ingestion is followed by chemotaxis and adhesin/pilus-mediated attachment to intestinal mucus, then secretion and proteolytic activation of pore-forming toxins — principally aerolysin (*aer/aerA*) and the cytotoxic enterotoxin **Act** (*act*) — supplemented by hemolysins, cytotonic enterotoxins (*alt/ast*), and proteases. Act forms transmembrane β-barrel pores, activates p38/JNK/ERK MAPK cascades, drives COX-2/PGE2 and pro-inflammatory cytokine production (TNF-α, IL-1β, IL-6), raises cAMP, and induces caspase-dependent apoptosis — together explaining both the secretory (cholera-like) and inflammatory/dysenteric phenotypes. Virulence scales with the number of toxin genes a strain carries.

The condition is usually **self-limited** and managed with rehydration; when antimicrobials are needed, intrinsic β-lactamase–mediated resistance to ampicillin/penicillins means treatment favours fluoroquinolones, 3rd/4th-generation cephalosporins, carbapenems, aminoglycosides, and cotrimoxazole. *A. hydrophila* is also a **major One Health pathogen**, causing Motile Aeromonad Septicaemia (MAS) in farmed fish with heavy economic losses; here prevention is achieved at the reservoir level through vaccines, phytobiotics, and probiotics (including engineered antimicrobial-peptide–secreting strains) rather than any licensed human vaccine. Global pooled prevalence in children with diarrhea is **4.2% (95% CI 3.1–5.6%)**, higher where water and sanitation are poor, and declining over time ([PMID: 37217902](https://pubmed.ncbi.nlm.nih.gov/37217902/)).

---

## 1. Disease Information

**Overview.** *Aeromonas hydrophila* intestinal disease is an acute bacterial gastroenteritis caused by an environmental, oxidase-positive, facultatively anaerobic, motile Gram-negative rod belonging to the family *Aeromonadaceae*. It is classed as an emerging, opportunistic, waterborne/foodborne enteric infection. The clinical presentation ranges from mild watery diarrhea to cholera-like secretory diarrhea and dysentery-like bloody diarrhea ([PMID: 29205196](https://pubmed.ncbi.nlm.nih.gov/29205196/)).

**Key identifiers.**
- **MONDO:** MONDO:0024459
- **MeSH:** *Aeromonas* infections / Gram-Negative Bacterial Infections; organism MeSH "Aeromonas hydrophila"
- **NCBI Taxonomy:** *Aeromonas hydrophila* = txid644; genus *Aeromonas* = txid642
- **ICD-10:** A04.8 (Other specified bacterial intestinal infections) — *Aeromonas* enteritis has no dedicated code and is captured under other/specified bacterial intestinal infections.
- **OMIM / Orphanet:** Not applicable — this is an acquired infectious disease with no Mendelian basis; no OMIM or Orphanet rare-disease entry.

**Synonyms / alternative names.** *Aeromonas* gastroenteritis; *Aeromonas*-associated diarrhea; *Aeromonas* enteritis; mesophilic *Aeromonas* infection; motile aeromonad infection (in veterinary contexts, Motile Aeromonad Septicaemia, MAS, when systemic in fish).

**Information source.** Content is aggregated from disease-level resources — clinical case series, case-control studies, PCR/genomic surveys, and systematic reviews/meta-analyses — rather than individual EHR-derived patient records.

---

## 2. Etiology

**Primary cause — infectious.** The disease is caused by ingestion of *A. hydrophila* (and closely related motile mesophilic aeromonads such as *A. caviae*, *A. veronii*, *A. dhakensis*). There is **no host genetic etiology**; the disease is entirely acquired. Virulence is multifactorial and strain-dependent (Findings F002, F003).

**Environmental / risk factors.**
- **Waterborne and foodborne transmission** — *Aeromonas* is transmitted via contaminated water, fish, and chicken meat, and can grow competitively at 5 °C, making it a refrigerated-food hazard ([PMID: 27051177](https://pubmed.ncbi.nlm.nih.gov/27051177/)).
- **Young age** — isolation rates are significantly higher in diarrheal than control children (p<0.001) ([PMID: 15005966](https://pubmed.ncbi.nlm.nih.gov/15005966/)); *A. hydrophila* was among the most frequent enteropathogens (9%) in Somali children ([PMID: 3076719](https://pubmed.ncbi.nlm.nih.gov/3076719/)).
- **Immunocompromise / malignancy** — in immunocompromised children with diarrhea (mostly acute lymphoblastic leukemia on chemotherapy), *Aeromonas* spp. were the most commonly detected target (14.6%), with bloody diarrhea in 98.5% ([PMID: 38778271](https://pubmed.ncbi.nlm.nih.gov/38778271/)).
- **Advanced age / hematologic disease** — severe/hemorrhagic disease reported in elderly patients with aplastic anemia/thrombocytopenia ([PMID: 41903649](https://pubmed.ncbi.nlm.nih.gov/41903649/)).
- **Poor water and sanitation** — prevalence 8.8% where water/sanitation quality score is <25% ([PMID: 37217902](https://pubmed.ncbi.nlm.nih.gov/37217902/)).

**Protective factors.** No genetic protective variants are defined (acquired disease). Environmental/behavioural protection derives from **clean water, sanitation, and food safety** (adequate cooking, avoiding prolonged refrigerated storage). In aquaculture reservoirs, probiotics and phytobiotics are protective (Findings F005, F012).

**Gene-environment interactions.** Not applicable to the human host. The relevant axis is on the **pathogen side**: strains carrying more virulence genes are more lethal, and the environmental/host niche selects for hypervirulent clonal lineages (Findings F002, F007).

---

## 3. Phenotypes

| Phenotype | Type | Characteristics | Frequency | Suggested HPO |
|---|---|---|---|---|
| Watery diarrhea (secretory, cholera-like) | Symptom | Acute onset; can cause severe dehydration | 26% had rice-water stools ([PMID: 29205196](https://pubmed.ncbi.nlm.nih.gov/29205196/)) | HP:0002014 (Diarrhea) |
| Dysentery / bloody diarrhea | Sign | Inflammatory, mucoid/bloody stool | 16% dysentery-like ([PMID: 29205196](https://pubmed.ncbi.nlm.nih.gov/29205196/)); 98.5% bloody in immunocompromised children ([PMID: 38778271](https://pubmed.ncbi.nlm.nih.gov/38778271/)) | HP:0025085 (Bloody diarrhea) |
| Dehydration | Sign | Can be severe; life-threatening | Common in severe cases | HP:0001944 (Dehydration) |
| Abdominal pain / cramps | Symptom | Accompanies diarrhea | Frequent | HP:0002027 (Abdominal pain) |
| Fever | Sign | Variable | Variable | HP:0001945 (Fever) |
| Vomiting / nausea | Symptom | Variable | Variable | HP:0002013 (Vomiting) |
| Sepsis / bacteremia | Outcome | Rare complication, mainly immunocompromised/elderly | Rare; one death in 50-patient series | HP:0100806 (Sepsis) |

**Onset:** acute (hours to days after exposure). **Severity:** variable — mild and self-limited in most immunocompetent hosts, severe/hemorrhagic in the immunocompromised and elderly. **Progression:** typically self-limited over days; episodic depending on re-exposure. **Quality-of-life impact:** for uncomplicated cases, transient; severe dehydration or sepsis can be life-threatening.

---

## 4. Genetic/Molecular Information

**Not applicable to the human host.** This is an infectious disease; there are **no causal host genes, pathogenic germline/somatic variants, modifier genes, host epigenetic changes, or chromosomal abnormalities**. Host genetic testing is not indicated.

The relevant "genetics" is **microbial virulence genetics**:
- **aerolysin** (*aer/aerA*) — β-pore-forming toxin, present in up to 87% of isolates ([PMID: 25216211](https://pubmed.ncbi.nlm.nih.gov/25216211/)); 72.7% of fish isolates ([PMID: 30989358](https://pubmed.ncbi.nlm.nih.gov/30989358/)).
- **cytotoxic enterotoxin** (*act*) — 7.7–18.2% of isolates.
- **cytotonic enterotoxins** (*alt*, *ast*) — *ast* 17% ([PMID: 25216211](https://pubmed.ncbi.nlm.nih.gov/25216211/)).
- **hemolysin A** (*hylA*), **serine protease** (*ahp*), **temperature-sensitive protease** (*eprCAI*).
- **Regulation:** DNA adenine methyltransferase (Dam) and tRNA-modifying enzyme GidA co-regulate *act* expression via GATC methylation ([PMID: 22391092](https://pubmed.ncbi.nlm.nih.gov/22391092/)).
- **Pfam / protein family:** aerolysin/ETX family, **Pfam PF01117** (aerolysin).

Strains carrying more virulence genes show progressively higher proteolytic, hemolytic, and cytotoxic activity and lower LD50 in zebrafish; the *aer+alt+act+eprCAI+ahp+* genotype is enriched among diseased hosts and most virulent ([PMID: 21219556](https://pubmed.ncbi.nlm.nih.gov/21219556/), [PMID: 22725694](https://pubmed.ncbi.nlm.nih.gov/22725694/)).

---

## 5. Environmental Information

- **Environmental reservoir:** freshwater, brackish water, wastewater, aquaculture ponds, and food (fish, poultry). Wastewater treatment plants are reservoirs for antibiotic-resistance gene dissemination in *Aeromonas* ([PMID: 40269715](https://pubmed.ncbi.nlm.nih.gov/40269715/)).
- **Psychrotrophy:** growth at 5 °C makes refrigerated foods a hazard ([PMID: 27051177](https://pubmed.ncbi.nlm.nih.gov/27051177/)).
- **Lifestyle factors:** consumption of untreated water, raw/undercooked fish and shellfish; exposure to recreational or occupational water (e.g., paddy-field injuries associated with invasive *Aeromonas* disease, [PMID: 42288750](https://pubmed.ncbi.nlm.nih.gov/42288750/)).
- **Infectious agents:** *Aeromonas hydrophila* (txid644); related *A. caviae*, *A. veronii*, *A. dhakensis*, *A. enteropelogenes*. Toxin entities: aerolysin, cytotoxic enterotoxin Act.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating exposure → clinical manifestation)

1. **Ingestion** of *A. hydrophila* in contaminated water/food **leads to** delivery of viable, motile bacteria to the small and large intestine.
2. **Chemotaxis toward intestinal mucus** (flagella-driven) **results in** localization at the mucosal surface; chemotaxis may be required for obligate pathogenicity ([PMID: 18355183](https://pubmed.ncbi.nlm.nih.gov/18355183/)).
3. **Adhesin/pilus-mediated attachment** to mucus glycoproteins (galactose/mannose receptors) **leads to** stable colonization; stronger adhesion correlates with greater cytotoxicity ([PMID: 18924378](https://pubmed.ncbi.nlm.nih.gov/18924378/), [PMID: 1363704](https://pubmed.ncbi.nlm.nih.gov/1363704/)).
4. **Secretion of toxins** (T2SS-secreted Act and aerolysin; hemolysins; proteases) **results in** inactive pro-toxins at the epithelial surface.
5. **Proteolytic activation** (C-terminal propeptide cleavage of proaerolysin/Act) **leads to** active toxin monomers with increased β-sheet content ([PMID: 9398250](https://pubmed.ncbi.nlm.nih.gov/9398250/)).
6. **GPI-anchored receptor binding + heptamerization** **results in** a prepore that undergoes a concerted "swirling" collapse, **inserting a transmembrane β-barrel pore** (1.14–2.8 nm) ([PMID: 23912165](https://pubmed.ncbi.nlm.nih.gov/23912165/), [PMID: 9317040](https://pubmed.ncbi.nlm.nih.gov/9317040/), [PMID: 34162996](https://pubmed.ncbi.nlm.nih.gov/34162996/)).
7. **Membrane permeabilization** branches into two downstream arms:
   - **7a (secretory arm):** pore formation + Act signalling **raises cAMP and activates COX-2/PGE2 and eicosanoid metabolism** → net fluid/electrolyte secretion → **watery, cholera-like diarrhea** ([PMID: 10768977](https://pubmed.ncbi.nlm.nih.gov/10768977/)).
   - **7b (inflammatory/cytotoxic arm):** Act activates **p38, JNK, ERK1/2 MAPK cascades**, induces **TNF-α, IL-1β, IL-6, iNOS**, and triggers **caspase-3/8/9–dependent apoptosis** in macrophages and human intestinal epithelial cells (T84, HT-29) → mucosal injury, neutrophilic inflammation → **dysenteric/bloody diarrhea** ([PMID: 15215244](https://pubmed.ncbi.nlm.nih.gov/15215244/)).
8. **(Inferred, strain-dependent)** In strains with T3SS/T6SS, effectors **AexU (T3SS) and Hcp (T6SS)** subvert host immune signalling and promote apoptosis/pyroptosis **leading to** deeper invasion and rarely **bacteremia/sepsis** ([PMID: 24199174](https://pubmed.ncbi.nlm.nih.gov/24199174/), [PMID: 23611906](https://pubmed.ncbi.nlm.nih.gov/23611906/)).
9. **(Inferred, lineage-dependent)** Epidemic ST251 clones achieve high virulence **independent of** classical T3SS/T6SS/lateral flagella, instead exploiting **myo-inositol, sialic acid, and L-fucose utilization** pathways ([PMID: 26014286](https://pubmed.ncbi.nlm.nih.gov/26014286/)).

### Category checklist mapped to the chain

- **Molecular pathways:** MAPK (p38/JNK/ERK); cAMP/PKA; arachidonic-acid/COX-2–PGE2 eicosanoid pathway; caspase apoptotic cascade.
- **Cellular processes:** pore-mediated membrane permeabilization; apoptosis (GO:0006915); inflammation; cytokine production (GO:0001816).
- **Protein dysfunction (pathogen toxins):** proaerolysin → active heptameric β-barrel pore; random-coil→β-sheet transition.
- **Immune involvement:** pro-inflammatory cytokines (TNF-α/IL-1β/IL-6), iNOS induction, neutrophilic infiltration; immune subversion by secretion-system effectors.
- **Tissue damage mechanisms:** epithelial pore lysis, apoptosis/necrosis, inflammatory injury.
- **Biochemical abnormalities:** dysregulated ion/fluid transport (secretory diarrhea), elevated cAMP.

**Suggested GO terms:** GO:0006915 (apoptotic process), GO:0000165 (MAPK cascade), GO:0006954 (inflammatory response), GO:0019836 (hemolysis in another organism), GO:0140911 (pore-forming activity), GO:0001816 (cytokine production). **Suggested CL terms:** CL:0000584 (enterocyte), CL:0002253 (epithelial cell of large intestine), CL:0000235 (macrophage), CL:0000775 (neutrophil).

---

## 7. Anatomical Structures Affected

- **Primary organ:** intestine — small intestine and colon (**UBERON:0000160 intestine; UBERON:0002108 small intestine; UBERON:0001155 colon**). Body system: digestive/gastrointestinal (**UBERON:0001007 digestive system**).
- **Secondary involvement:** bloodstream (bacteremia/sepsis) in immunocompromised/elderly hosts; rarely liver (acute hepatitis with invasive *Aeromonas*, [PMID: 41356972](https://pubmed.ncbi.nlm.nih.gov/41356972/)).
- **Tissue/cell level:** intestinal **epithelium (mucosa)** — enterocytes (CL:0000584) and colonic epithelial cells (CL:0002253) are primary targets; **macrophages (CL:0000235)** and **neutrophils (CL:0000775)** mediate inflammation. Toxins act on GPI-anchored-protein–bearing membranes.
- **Subcellular level:** plasma membrane (pore insertion; **GO:0005886**); mitochondria/cytoplasm (caspase-9 intrinsic apoptosis; **GO:0005739**); cell-surface GPI anchor (**GO:0098552**).
- **Localization / lateralization:** diffuse mucosal involvement; not lateralized.

---

## 8. Temporal Development

- **Onset:** acute, within hours to a few days of ingestion (not congenital, not insidious).
- **Progression:** most cases self-limited over several days; a minority (severe cholera-like) progress rapidly to dehydration; dysenteric cases run an inflammatory course. No chronic-lifelong course in immunocompetent hosts.
- **Disease course pattern:** acute, self-limited; can be episodic with re-exposure. Rare progression to invasive/systemic disease in vulnerable hosts.
- **Remission:** usually spontaneous with supportive rehydration; antibiotics shorten severe cases.
- **Critical periods:** early rehydration is the key intervention window; in severe/immunocompromised cases, early appropriate antibiotics prevent progression to sepsis.

---

## 9. Inheritance and Population

- **Inheritance:** Not applicable — acquired infectious disease, no heritability, penetrance, expressivity, anticipation, founder effects, consanguinity, or carrier frequency.
- **Epidemiology:** Global pooled prevalence in children with diarrhea = **4.2% (95% CI 3.1–5.6%)** across 31 studies / 38,663 participants ([PMID: 37217902](https://pubmed.ncbi.nlm.nih.gov/37217902/)). Higher in upper-middle-income countries (5.1%), very populous countries (>100 million: 9.4%), and poor-sanitation settings (<25% score: 8.8%); a significant **decreasing trend over time** (P=0.0001).
- **Demographics:** disproportionately affects **young children**, the **elderly**, and the **immunocompromised** (Finding F008). Higher isolation in diarrheal vs control children (p<0.001, [PMID: 15005966](https://pubmed.ncbi.nlm.nih.gov/15005966/)).
- **Geographic distribution:** worldwide; higher burden where water/sanitation is poor; endemic in tropical/subtropical aquaculture regions. Epidemic hypervirulent clones (ST251) reported from China and the southeastern USA ([PMID: 26014286](https://pubmed.ncbi.nlm.nih.gov/26014286/)).
- **Seasonality:** peaks in warm months.

---

## 10. Diagnostics

- **Stool culture** on blood/selective agar with **oxidase-positive** screening is the mainstay.
- **Species-level identification requires molecular methods** — biochemical and automated systems misidentify *Aeromonas*. In one case, MALDI-TOF gave high scores for two species and an automated system called it "*A. veronii* complex"; **definitive ID required multilocus phylogenetic analysis of *gyrB*, *rpoD*, *gyrA*** ([PMID: 41903649](https://pubmed.ncbi.nlm.nih.gov/41903649/)).
- **PCR / molecular:** multiplex PCR for virulence genes (*aer/act/alt/ast*), and *gyrB*/16S rDNA sequencing for detection and genotyping ([PMID: 25216211](https://pubmed.ncbi.nlm.nih.gov/25216211/), [PMID: 22725694](https://pubmed.ncbi.nlm.nih.gov/22725694/)).
- **Biosensors:** DNA hybridization electrochemical biosensors developed for *A. hydrophila* ([PMID: 20829023](https://pubmed.ncbi.nlm.nih.gov/20829023/)).
- **Clinical criteria / differential diagnosis:** acute infectious diarrhea; distinguish from *Vibrio cholerae* (secretory), *Shigella*/*Campylobacter*/*Salmonella*/EIEC (dysenteric), *C. difficile* (antibiotic-associated). Stool culture is important in severe or protracted illness when antimicrobial therapy is contemplated ([PMID: 3683260](https://pubmed.ncbi.nlm.nih.gov/3683260/)).
- **Genetic/omics diagnostics:** host genetic testing not applicable. Pathogen WGS/MLST is used for outbreak tracing and AMR profiling.
- **Screening:** no human screening program; environmental/food surveillance applies.

---

## 11. Outcome / Prognosis

- **Prognosis:** generally good; most cases are **self-limited** in immunocompetent hosts.
- **Mortality:** low overall but non-zero — one death (dehydration + septicaemia) in a 50-patient series ([PMID: 29205196](https://pubmed.ncbi.nlm.nih.gov/29205196/)). Invasive/bacteremic disease carries substantial mortality, especially in immunocompromised/elderly patients ([PMID: 41903649](https://pubmed.ncbi.nlm.nih.gov/41903649/), [PMID: 42288750](https://pubmed.ncbi.nlm.nih.gov/42288750/)).
- **Complications:** severe dehydration, dysentery, bacteremia/sepsis, rarely acute hepatitis; carbapenem treatment failure reported in critically ill patients due to PK/PD factors ([PMID: 42288750](https://pubmed.ncbi.nlm.nih.gov/42288750/)).
- **Prognostic factors:** host immune status (immunocompromise, malignancy, advanced age worsen outcomes); strain virulence-gene load and hypervirulent lineage; timeliness of rehydration and appropriate antibiotics; AMR profile (ESBL/integron-borne resistance worsens outcomes, [PMID: 41625157](https://pubmed.ncbi.nlm.nih.gov/41625157/)).

---

## 12. Treatment

- **Supportive care (cornerstone):** oral/IV **rehydration** and electrolyte correction; most immunocompetent cases need no antibiotics. **NCIT:** Fluid and Electrolyte Therapy.
- **Antimicrobials (when severe/invasive or immunocompromised):**
  - **Avoid** ampicillin/amoxicillin and 1st-generation cephalosporins — *A. hydrophila* is **intrinsically resistant** via chromosomal β-lactamases (only ~14% amoxicillin-susceptible) ([PMID: 29205196](https://pubmed.ncbi.nlm.nih.gov/29205196/)).
  - **Effective agents:** fluoroquinolones (ciprofloxacin), 3rd/4th-generation cephalosporins (ceftazidime, cefepime), carbapenems (meropenem), aminoglycosides (amikacin, gentamicin), aztreonam, azithromycin, cotrimoxazole — gastroenteritis isolates are almost uniformly susceptible ([PMID: 38783344](https://pubmed.ncbi.nlm.nih.gov/38783344/)). **NCIT:** Ciprofloxacin, Ceftazidime, Meropenem, Amikacin, Trimethoprim-Sulfamethoxazole.
  - **AMR caveat:** emerging ESBL (CTX-M) and class-1-integron–borne resistance, including carbapenem treatment failures ([PMID: 42288750](https://pubmed.ncbi.nlm.nih.gov/42288750/), [PMID: 41625157](https://pubmed.ncbi.nlm.nih.gov/41625157/)). Susceptibility testing should guide therapy.
- **Advanced/experimental therapeutics:** none specific for human *Aeromonas* enteritis. In aquaculture, engineered probiotics secreting antimicrobial peptides are investigational (see Prevention).

---

## 13. Prevention

- **Primary prevention:** clean water, sanitation, and food safety (adequate cooking; limiting refrigerated storage given growth at 5 °C) ([PMID: 27051177](https://pubmed.ncbi.nlm.nih.gov/27051177/), [PMID: 37217902](https://pubmed.ncbi.nlm.nih.gov/37217902/)).
- **Human immunization:** **no licensed human vaccine.**
- **Veterinary/aquaculture prevention (One Health):**
  - **Vaccines:** whole-cell inactivated *A. hydrophila* vaccines give the highest protection (vs live-attenuated/recombinant); i.p. injection most effective; feed-based bivalent (*S. iniae* + *A. hydrophila*) vaccines raise IgM and improve survival ([PMID: 32331001](https://pubmed.ncbi.nlm.nih.gov/32331001/), [PMID: 33857622](https://pubmed.ncbi.nlm.nih.gov/33857622/), [PMID: 32615969](https://pubmed.ncbi.nlm.nih.gov/32615969/)).
  - **Probiotics:** dietary *Saccharomyces cerevisiae* cut post-challenge mortality from 53.3% to 13.3% in African catfish ([PMID: 41946979](https://pubmed.ncbi.nlm.nih.gov/41946979/)); *Bacillus licheniformis*, *Lactobacillus brevis* (+trans-cinnamic acid), and engineered *Bacillus subtilis* secreting piscidin-1/hepcidin improved survival ([PMID: 42067537](https://pubmed.ncbi.nlm.nih.gov/42067537/), [PMID: 42014760](https://pubmed.ncbi.nlm.nih.gov/42014760/), [PMID: 42176787](https://pubmed.ncbi.nlm.nih.gov/42176787/)); *Clostridium butyricum* blocks colonization in vitro ([PMID: 18795975](https://pubmed.ncbi.nlm.nih.gov/18795975/)).
  - **Phytobiotics:** dietary essential oils (basil, thyme, fenugreek) improve immunity and resistance ([PMID: 42400869](https://pubmed.ncbi.nlm.nih.gov/42400869/), [PMID: 42376504](https://pubmed.ncbi.nlm.nih.gov/42376504/)).
- **Public health:** integrated One Health AMR surveillance across environmental, food, and clinical compartments ([PMID: 42288750](https://pubmed.ncbi.nlm.nih.gov/42288750/)).

---

## 14. Other Species / Natural Disease

- **Taxonomy of pathogen:** *Aeromonas hydrophila* NCBI **txid644**; genus *Aeromonas* txid642.
- **Natural disease — fish:** *A. hydrophila* is the usual etiological agent of **Motile Aeromonad Septicaemia (MAS)** in tilapia (*Oreochromis niloticus*), carp (*Cyprinus carpio*), catfish (*Clarias gariepinus*), and other freshwater fish, with high mortality and major economic loss ([PMID: 32331001](https://pubmed.ncbi.nlm.nih.gov/32331001/), [PMID: 30989358](https://pubmed.ncbi.nlm.nih.gov/30989358/)).
- **Other hosts / zoonotic potential:** environmental organism of aquatic habitats; found in hippopotamus oral flora, of zoonotic importance in bite-wound infections ([PMID: 40269996](https://pubmed.ncbi.nlm.nih.gov/40269996/)). Human infection is acquired from environmental/animal reservoirs (One Health).
- **Comparative biology:** the same toxin/virulence machinery (Act, aerolysin, T3SS/T6SS) drives disease across fish and mammals, and virulence-gene load predicts lethality across host models (zebrafish, mice) — indicating conserved mechanisms.

---

## 15. Model Organisms

| Model | Type | Use / recapitulation | Reference |
|---|---|---|---|
| Zebrafish (*Danio rerio*) | Vertebrate, in vivo | LD50 challenge; virulence-gene load correlates with lethality; probiotic protection | [PMID: 21219556](https://pubmed.ncbi.nlm.nih.gov/21219556/), [PMID: 42176787](https://pubmed.ncbi.nlm.nih.gov/42176787/) |
| Mouse | Mammalian, in vivo | Lethality of wound pathotype E1 vs environmental ATCC 7966; IV LD50 of Act = 27.5 ng | [PMID: 23611906](https://pubmed.ncbi.nlm.nih.gov/23611906/), [PMID: 9317040](https://pubmed.ncbi.nlm.nih.gov/9317040/) |
| Rat ileal loop | Mammalian, ex vivo | Minimal fluid-secretion dose of Act = 200 ng — models secretory diarrhea | [PMID: 9317040](https://pubmed.ncbi.nlm.nih.gov/9317040/) |
| Tilapia / carp / catfish | Vertebrate, in vivo | MAS disease model; vaccine and probiotic efficacy testing | [PMID: 32331001](https://pubmed.ncbi.nlm.nih.gov/32331001/), [PMID: 41946979](https://pubmed.ncbi.nlm.nih.gov/41946979/) |
| Human intestinal epithelial lines (T84, HT-29) | In vitro | Act-induced MAPK activation and apoptosis | [PMID: 15215244](https://pubmed.ncbi.nlm.nih.gov/15215244/) |
| Murine macrophages | In vitro | Act-induced cytokine/eicosanoid production, apoptosis | [PMID: 10768977](https://pubmed.ncbi.nlm.nih.gov/10768977/) |
| Rabbit intestine | Ex vivo | Pili adhesion / colonization-factor studies | [PMID: 1363704](https://pubmed.ncbi.nlm.nih.gov/1363704/) |
| HEK293 GPI-biosynthesis knockout library | In vitro | Defines aerolysin GPI-anchor receptor requirements | [PMID: 34162996](https://pubmed.ncbi.nlm.nih.gov/34162996/) |

**Model limitations:** no single model captures the full human clinical spectrum plus the pathogen-vs-commensal ambiguity; fish MAS is a systemic septicaemia rather than a purely enteric disease.

---

## Key Findings (with statistical evidence)

### F001 — Clinical spectrum and pathogen-vs-commensal ambiguity
*A. hydrophila* causes acute gastroenteritis ranging from watery/cholera-like to dysenteric diarrhea, but is often a minor contributor or coloniser. In 50 patients, 26% had cholera-like rice-water stools with severe dehydration, 16% a dysentery-like picture, and one died ([PMID: 29205196](https://pubmed.ncbi.nlm.nih.gov/29205196/)). *Aeromonas* was among the most frequent enteropathogens (9%) in Somali children ([PMID: 3076719](https://pubmed.ncbi.nlm.nih.gov/3076719/)). In N. Israel, positivity was similar in symptomatic (4.24–4.81%) and asymptomatic (4.9%) stools — *"similar positivity rates of Aeromonas spp. in symptomatic and asymptomatic making the distinction between true pathogen versus commensal bacteria difficult"* ([PMID: 39388901](https://pubmed.ncbi.nlm.nih.gov/39388901/)).

### F002 — Multifactorial, dose-dependent virulence
Virulence combines aerolysin (*aer*), Act (*act*), hemolysins, cytotonic enterotoxins (*alt/ast*), and proteases. *aer* was present in 87%, *act* 7.7%, *ast* 17% of a Libyan isolate set ([PMID: 25216211](https://pubmed.ncbi.nlm.nih.gov/25216211/)). Crucially, *"as the present of virulence genes increased, the proteolytic, haemolytic and cytotoxic activities of extracellular products also increased"* ([PMID: 21219556](https://pubmed.ncbi.nlm.nih.gov/21219556/)), and 5-gene strains had lower LD50 in fish ([PMID: 22725694](https://pubmed.ncbi.nlm.nih.gov/22725694/)).

### F003 — Act is the core enterotoxic engine
Act is a 52-kDa aerolysin-related pore-forming toxin (pores 1.14–2.8 nm; rat ileal-loop minimal dose 200 ng; mouse IV LD50 27.5 ng) ([PMID: 9317040](https://pubmed.ncbi.nlm.nih.gov/9317040/)). It *"activates stress-associated p38, c-Jun NH(2)-terminal kinase (JNK), and extracellular signal-regulated kinase 1/2 (ERK1/2)"* and induces apoptosis ([PMID: 15215244](https://pubmed.ncbi.nlm.nih.gov/15215244/)), and *"stimulated the production of tumor necrosis factor alpha and upregulated ... IL-1beta ... and IL-6"* ([PMID: 10768977](https://pubmed.ncbi.nlm.nih.gov/10768977/)).

### F004 — Intrinsic β-lactam resistance shapes therapy
Isolates are uniformly susceptible to cefepime, amikacin, azithromycin, meropenem; only 14% to amoxicillin ([PMID: 29205196](https://pubmed.ncbi.nlm.nih.gov/29205196/)); gastroenteritis isolates almost uniformly susceptible to amikacin, gentamicin, aztreonam, cefepime, ceftazidime, ciprofloxacin, meropenem ([PMID: 38783344](https://pubmed.ncbi.nlm.nih.gov/38783344/)).

### F005 — Major veterinary disease (MAS); vaccines protect
*"The etiological agent of this disease is usually Aeromonas hydrophila. Mortality rates due to MAS are frequently high"* ([PMID: 32331001](https://pubmed.ncbi.nlm.nih.gov/32331001/)); whole-cell inactivated vaccines give highest protection.

### F006 — Molecular ID required for accurate speciation
Routine MALDI-TOF/automated systems misidentify *Aeromonas*; definitive ID needs *gyrB/rpoD/gyrA* MLPA ([PMID: 41903649](https://pubmed.ncbi.nlm.nih.gov/41903649/)).

### F007 — Hypervirulent lineages independent of classical secretion systems
For epidemic ST251 clones, *"the known virulence factors, including a type III secretion system, a type VI secretion system and lateral flagella, are not required for the high virulence"* — instead myo-inositol/sialic-acid/L-fucose metabolism is implicated ([PMID: 26014286](https://pubmed.ncbi.nlm.nih.gov/26014286/)).

### F008 — Waterborne/foodborne transmission; vulnerable hosts
*"The ability of these bacteria to grow competitively at 5°C may be indicative of their potential as a public health hazard"* ([PMID: 27051177](https://pubmed.ncbi.nlm.nih.gov/27051177/)); enriched in diarrheal children (p<0.001, [PMID: 15005966](https://pubmed.ncbi.nlm.nih.gov/15005966/)); leading enteric agent (14.6%) in immunocompromised children ([PMID: 38778271](https://pubmed.ncbi.nlm.nih.gov/38778271/)).

### F009 — Aerolysin: prototype β-pore-forming toxin
Secreted as proaerolysin, proteolytically activated (*"a decrease in random structure and an increase in beta-sheet content"* [PMID: 9398250](https://pubmed.ncbi.nlm.nih.gov/9398250/)), binds GPI anchors, heptamerizes (mass 333,850 Da confirms heptamer, [PMID: 8617369](https://pubmed.ncbi.nlm.nih.gov/8617369/)), and inserts via a *"unique concerted swirling movement ... leading to the insertion of a transmembrane β-barrel"* ([PMID: 23912165](https://pubmed.ncbi.nlm.nih.gov/23912165/)).

### F010 — Global prevalence 4.2%, sanitation-linked, declining
*"The pooled prevalence of Aeromonas in children with diarrhoea worldwide was 4.2% (95% CI 3.1-5.6%)"*; poor sanitation → 8.8%; decreasing trend over time ([PMID: 37217902](https://pubmed.ncbi.nlm.nih.gov/37217902/)).

### F011 — Adhesion/colonization gates cytotoxicity
*"bacteria that showed a stronger adhesion to intestinal mucus were cytotoxic ... and bacteria that showed a weaker adhesion ... did not lead to alterations of monolayers"* ([PMID: 18924378](https://pubmed.ncbi.nlm.nih.gov/18924378/)); pili are colonization factors via galactose/mannose receptors ([PMID: 1363704](https://pubmed.ncbi.nlm.nih.gov/1363704/)).

### F012 — Antibiotic-alternative prevention works in aquaculture
Dietary probiotics reduced post-challenge mortality from 53.3% to 13.3% ([PMID: 41946979](https://pubmed.ncbi.nlm.nih.gov/41946979/)); rising AMR *"necessitat[es] the urgent need for sustainable alternative treatments"* ([PMID: 42573755](https://pubmed.ncbi.nlm.nih.gov/42573755/)).

---

## Mechanistic Model (synthesis)

```
 Ingestion (contaminated water/food, grows at 5°C)
        │
        ▼
 Chemotaxis (flagella) ──► Adhesion (pili, mucus glycoprotein receptors)
        │                        │  stronger adhesion → greater cytotoxicity
        ▼                        ▼
 Toxin secretion (T2SS: Act, aerolysin; hemolysins; proteases)
        │
        ▼
 Proteolytic activation (propeptide cleavage; coil→β-sheet)
        │
        ▼
 GPI-receptor binding → heptamerization → "swirling" β-barrel pore insertion
        │
        ├───────────────► SECRETORY ARM: ↑cAMP, COX-2/PGE2, eicosanoids
        │                   → fluid/electrolyte secretion → CHOLERA-LIKE DIARRHEA
        │
        └───────────────► INFLAMMATORY ARM: p38/JNK/ERK MAPK, TNF-α/IL-1β/IL-6,
                            iNOS, caspase-3/8/9 apoptosis
                            → mucosal injury + neutrophilic inflammation
                            → DYSENTERIC/BLOODY DIARRHEA
        │
        └── (strain-dependent) T3SS/AexU + T6SS/Hcp immune subversion → INVASION/SEPSIS
        └── (lineage-dependent, ST251) metabolism-linked hypervirulence (inositol/sialic acid/fucose)
```

**Upstream** events (colonization, adhesion, toxin activation) gate **downstream** effects (pore formation, signalling, cell death). The two clinical phenotypes (secretory vs dysenteric) branch from the same pore-forming event depending on the balance of cAMP/eicosanoid secretion versus MAPK-driven apoptosis/inflammation.

---

## Evidence Base (selected)

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [29205196](https://pubmed.ncbi.nlm.nih.gov/29205196/) | Speciation, clinical profile & antibiotic resistance | Clinical spectrum (F001); intrinsic β-lactam resistance (F004) |
| [21219556](https://pubmed.ncbi.nlm.nih.gov/21219556/) | *alt/ahp/aerA* virulence & zebrafish virulence | Dose-dependent virulence (F002) |
| [9317040](https://pubmed.ncbi.nlm.nih.gov/9317040/) | Act hyperproduction & mechanism | Act pore-forming mechanism (F003) |
| [15215244](https://pubmed.ncbi.nlm.nih.gov/15215244/) | Act activates MAPK & apoptosis | Inflammatory arm (F003) |
| [10768977](https://pubmed.ncbi.nlm.nih.gov/10768977/) | Act cytokines & arachidonic acid | Secretory/inflammatory cytokines (F003) |
| [23912165](https://pubmed.ncbi.nlm.nih.gov/23912165/) | Aerolysin swirling pore assembly | Structural mechanism (F009) |
| [8617369](https://pubmed.ncbi.nlm.nih.gov/8617369/) | Heptameric pore MALDI-TOF | Heptamer stoichiometry (F009) |
| [37217902](https://pubmed.ncbi.nlm.nih.gov/37217902/) | Global prevalence meta-analysis | Epidemiology (F010) |
| [18924378](https://pubmed.ncbi.nlm.nih.gov/18924378/) | Mucus adhesion & cytotoxicity | Colonization step (F011) |
| [26014286](https://pubmed.ncbi.nlm.nih.gov/26014286/) | ST251 comparative genomics | Lineage-specific virulence (F007) |
| [32331001](https://pubmed.ncbi.nlm.nih.gov/32331001/) | Tilapia MAS vaccination review | Veterinary disease & prevention (F005) |
| [41946979](https://pubmed.ncbi.nlm.nih.gov/41946979/) | Dietary yeast vs challenge | Probiotic prevention (F012) |
| [41903649](https://pubmed.ncbi.nlm.nih.gov/41903649/) | Diagnostic pitfalls case report | Molecular ID requirement (F006) |
| [27051177](https://pubmed.ncbi.nlm.nih.gov/27051177/) | Foodborne review | Transmission & psychrotrophy (F008) |

**Challenging / nuancing evidence:** [PMID: 3584426](https://pubmed.ncbi.nlm.nih.gov/3584426/) found no correlation between toxin production and gastroenteritis, and [PMID: 39388901](https://pubmed.ncbi.nlm.nih.gov/39388901/) shows equal symptomatic/asymptomatic carriage — both underscore that *Aeromonas* enteropathogenicity is strain-dependent and sometimes commensal, tempering simple causal claims.

---

## Limitations and Knowledge Gaps

1. **Causality unmet at population level.** Similar carriage in symptomatic and asymptomatic individuals ([PMID: 39388901](https://pubmed.ncbi.nlm.nih.gov/39388901/)) and no toxin–disease correlation in one series ([PMID: 3584426](https://pubmed.ncbi.nlm.nih.gov/3584426/)) mean attribution specifically to *A. hydrophila* is often uncertain; co-infections are common.
2. **Species misidentification** historically conflated *A. caviae*, *A. veronii*, *A. dhakensis*, and *A. hydrophila*, so species-specific clinical data are imprecise; *A. caviae* now dominates many clinical series ([PMID: 38783344](https://pubmed.ncbi.nlm.nih.gov/38783344/)).
3. **Human vs fish evidence imbalance.** Much mechanistic and prevention data come from fish/aquaculture and cell/animal models, not human enteric disease.
4. **No human clinical trials** define antibiotic benefit for uncomplicated cases; treatment recommendations are extrapolated from susceptibility data.
5. **AMR evolution** (ESBL/CTX-M, class-1 integrons, carbapenem failures) is dynamic and may outpace current guidance.
6. **No host-genetic dimension** — sections 4 (host genetics) and 9 (inheritance) are inherently not applicable for an acquired infection.

---

## Proposed Follow-up Actions

1. **Prospective, culture-independent, species-resolved cohort studies** (metagenomics + strain WGS) pairing symptom status with virulence-gene content to resolve the pathogen-vs-commensal question and define an attributable fraction.
2. **Randomized controlled trials** of antibiotic therapy vs rehydration alone in moderate–severe *Aeromonas* gastroenteritis, stratified by host immune status.
3. **Integrated One Health AMR surveillance** linking environmental/wastewater, food, aquaculture, and clinical isolates to track ESBL/integron gene flow ([PMID: 42288750](https://pubmed.ncbi.nlm.nih.gov/42288750/), [PMID: 40269715](https://pubmed.ncbi.nlm.nih.gov/40269715/)).
4. **Mechanistic dissection of ST251-type metabolism-linked hypervirulence** (inositol/sialic acid/fucose utilization) as potential anti-virulence targets ([PMID: 26014286](https://pubmed.ncbi.nlm.nih.gov/26014286/)).
5. **Anti-virulence / anti-toxin therapeutics** (Act/aerolysin pore inhibitors, adhesion blockers) and continued development of aquaculture probiotic/vaccine reservoir control to reduce human exposure.
6. **Standardize molecular species identification** (*gyrB/rpoD/gyrA*) in diagnostic labs to improve epidemiological precision.

---

*Report compiled from 12 confirmed findings and 64 reviewed papers over 5 investigation iterations. Evidence types: human clinical series/meta-analysis, model organism (zebrafish, mouse, fish), in vitro (epithelial/macrophage cell lines), and structural/computational studies.*


## Artifacts

- [OpenScientist final report](Aeromonas_Hydrophila_Intestinal_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Aeromonas_Hydrophila_Intestinal_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 46 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 46 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 17 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0019836` (1 mention) - the report calls it "hemolysis in another organism"; GO calls it **symbiont-mediated hemolysis of host erythrocyte**, and lists "haemolysis in host" among its other names

Every term resolved, and every label the report gave matched.