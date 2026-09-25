---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-22T13:02:56.799932'
end_time: '2026-09-22T13:35:36.355974'
duration_seconds: 1959.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Usmani-Riazuddin Syndrome Autosomal Recessive
  mondo_id: MONDO:0859196
  category: Disease
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
citation_count: 10
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 8
  labels_variant: 7
  unresolvable_prefixes:
  - OMIM
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Usmani-Riazuddin_Syndrome_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Usmani-Riazuddin_Syndrome_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Usmani-Riazuddin Syndrome Autosomal Recessive
- **MONDO ID:** MONDO:0859196 (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Usmani-Riazuddin Syndrome Autosomal Recessive** covering all of the
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

# Usmani-Riazuddin Syndrome, Autosomal Recessive (USRISR): A Comprehensive Disease Characterization

**Disease:** Usmani-Riazuddin Syndrome, Autosomal Recessive
**MONDO ID:** MONDO:0859196 · **OMIM:** #619548 · **Gene:** *AP1G1* (MIM \*603533)
**Report type:** Disease knowledge-base characterization (multi-iteration autonomous investigation)

---

## Summary

Usmani-Riazuddin syndrome, autosomal recessive (USRISR; OMIM #619548; MONDO:0859196) is an **ultra-rare monogenic neurodevelopmental disorder** caused by **bi-allelic (recessive) hypomorphic missense variants in *AP1G1***, the gene encoding the **γ1 (gamma-1) subunit of the heterotetrameric clathrin adaptor protein complex 1 (AP-1)**. The disorder was first delineated in 2021 by Usmani, Riazuddin and colleagues, who described a cohort of 11 families in whom *AP1G1* variants segregated with neurodevelopmental disease in both a recessive and a dominant (de novo) mode. The recessive form is defined by two missense alleles — **c.737C>A (p.Pro246His)** and **c.1105A>G (p.Met369Val)** — that reduce AP1γ1 protein levels and selectively impair the **endosome-recycling arm** of AP-1–mediated vesicular trafficking, rather than disrupting assembly of the AP-1 complex itself ([PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/)).

Clinically, USRISR is a **multisystem neurodevelopmental disorder** presenting in infancy/early childhood with **global developmental delay, intellectual disability, speech and language delay, abnormal muscle tone (hypotonia and/or spasticity), and epilepsy**. Behavioral anomalies (including aggression), variable dysmorphic features, and occasional brain malformations (agenesis of the corpus callosum) are also seen. Because AP-1 mediates the **polarized somatodendritic localization of neuronal membrane proteins**, its dysfunction produces a trafficking-based ("adaptoropathy") mechanism converging on defective neuronal protein sorting. Functional validation in a **zebrafish *ap1g1* knockout** — which is embryonic/gastrula-stage lethal and rescued by wild-type but not variant human *AP1G1* mRNA — confirmed the pathogenicity of the disease alleles and the essentiality of the gene ([PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/); [PMID: 41226632](https://pubmed.ncbi.nlm.nih.gov/41226632/)).

The evidence base remains small and recent: the defining cohort (2021), a subsequent case report defining a recognizable phenotype (2024), and a 2025 functional zebrafish study. *AP1G1* is **extremely intolerant to loss-of-function** (gnomAD pLI = 1.0, LOEUF ≈ 0.12) and to missense variation (missense Z = 3.42), and its ClinVar landscape is dominated by variants of uncertain significance — consistent with a newly delineated disease gene. There is **no disease-specific therapy**; management is supportive (anti-seizure medication, developmental rehabilitation, and genetic counseling for at-risk consanguineous families).

---

## Key Findings

### Finding 1 — USRISR is caused by bi-allelic *AP1G1* variants

USRISR is a Mendelian disorder caused by **bi-allelic (recessive) variants in *AP1G1***. In the disease-defining study, Usmani et al. (2021) reported **two bi-allelic missense variants** — *c.737C>A [p.Pro246His]* and *c.1105A>G [p.Met369Val]* — alongside eight de novo heterozygous variants that cause the allelic dominant disorder (USRISD, OMIM #619467). OMIM designates the recessive form **USRISR #619548** and the dominant form **USRISD #619467**; the causal gene *AP1G1* is catalogued as MIM \*603533.

> *"Here, we report two bi-allelic (c.737C>A [p.Pro246His] and c.1105A>G [p.Met369Val]) and eight de novo heterozygous variants"* — [PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/)

The molecular basis lies in the normal role of adaptor protein complexes: *"Adaptor protein (AP) complexes mediate selective intracellular vesicular trafficking and polarized localization of somatodendritic proteins in neurons"* ([PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/)). AP1G1 encodes the γ1 subunit of AP-1, so bi-allelic hypomorphic alleles compromise this trafficking machinery.

### Finding 2 — Clinical phenotype: multisystem neurodevelopmental disorder

USRISR is characterized by **multisystemic involvement**. Gnazzo et al. (2024) summarize the syndrome as being *"characterized by multisystemic involvement including intellectual disability, speech and developmental delay, behavioral anomalies, muscular tone disorders, seizures, limb defects, and unspecified facial gestalt"* ([PMID: 38665048](https://pubmed.ncbi.nlm.nih.gov/38665048/)). The original cohort ([PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/)) established the three **core neurodevelopmental features**: developmental delay, intellectual disability, and epilepsy.

### Finding 3 — AP1G1 (γ1 subunit) mediates clathrin-dependent polarized protein sorting

*AP1G1* encodes the **γ1 subunit of the heterotetrameric AP-1 adaptor complex**, which acts with **clathrin** in vesicular transport between the **trans-Golgi network (TGN) and early/recycling endosomes**. AP-1 is described as *"a subunit of the adaptor protein complex 1 (AP-1), a key component of the intracellular protein trafficking machinery"* ([PMID: 39269494](https://pubmed.ncbi.nlm.nih.gov/39269494/)).

Loss of the γ1 subunit disrupts polarized cargo sorting: in MDCK cells, *"silencing of clathrin or the γ1 subunit of clathrin adaptor AP-1 by RNA interference … disrupted apical localization of megalin, causing its redistribution to the basolateral membrane"* ([PMID: 31091172](https://pubmed.ncbi.nlm.nih.gov/31091172/)). In neurons, this same machinery governs polarized somatodendritic protein localization; the bi-allelic missense variants (p.Pro246His, p.Met369Val) are predicted **hypomorphic**, impairing AP-1 cargo handling.

### Finding 4 — Recessive variants disrupt endosome recycling; zebrafish model recapitulates disease

Critically, functional studies of the **two recessive missense variants** revealed a mechanism distinct from the dominant alleles: they had **no apparent impact on AP1γ1's interaction with other AP-1 subunits**, but instead **affected the endosome-recycling pathway**. In silico/3D modeling predicted altered protein folding, consistent with observed alterations in AP1γ1 protein levels in heterologous cells ([PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/)).

The gene is essential in vivo: knocking out *ap1g1* in zebrafish caused **severe morphological defects and lethality**, significantly **rescued by wild-type but not variant *AP1G1* mRNA**. A 2025 study confirmed that *ap1g1* knockout is **lethal at the gastrula stage** and rescued by human wild-type mRNA, describing AP-1 as *"a heterotetrameric essential for intracellular vesicular trafficking and polarized localization of somato-dendritic proteins in neurons"* ([PMID: 41226632](https://pubmed.ncbi.nlm.nih.gov/41226632/)).

### Finding 5 — Variant spectrum and genotype–phenotype correlation

The defining cohort ([PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/)) comprised **11 families of diverse ethnicities**, including Pakistani families in which the recessive form segregated (consistent with consanguinity). The allelic architecture is summarized below.

| Inheritance | Variant (cDNA) | Protein | Type |
|---|---|---|---|
| **Recessive (bi-allelic)** | c.737C>A | p.Pro246His | Missense |
| **Recessive (bi-allelic)** | c.1105A>G | p.Met369Val | Missense |
| Dominant (de novo) | — | p.Arg15Gln | Missense |
| Dominant (de novo) | — | p.Arg35Trp | Missense |
| Dominant (de novo) | — | p.Arg35Gln | Missense |
| Dominant (de novo) | — | p.Gln249His | Missense |
| Dominant (de novo) | — | p.Pro820Arg | Missense |
| Dominant (de novo) | — | p.Gln77Lysfs\*11 | Frameshift |
| Dominant (de novo) | — | p.Glu133Aspfs\*37 | Frameshift |
| Dominant (de novo) | c.928-2A>C | (splice acceptor) | Splice-site |
| Dominant (de novo, later report) | c.196G>A | p.Gly66Arg | Missense (dominant-negative) |

The phenotype spanned **mild to severe intellectual disability, epilepsy, and developmental delay**. A subsequently reported de novo variant, c.196G>A/p.Gly66Arg, exhibited a **dominant-negative effect** ([PMID: 41226632](https://pubmed.ncbi.nlm.nih.gov/41226632/)).

### Finding 6 — HPO phenotype spectrum with frequencies (recessive patients, n=3)

Curated HPO annotations for OMIM:619548 / MONDO:0859196 (source [PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/); n = 3 recessive patients):

| Phenotype | HPO term | Frequency (n=3) |
|---|---|---|
| Delayed speech and language development | HP:0000750 | 3/3 (100%) |
| Global developmental delay | HP:0001263 | 3/3 (100%) |
| Intellectual disability | HP:0001249 | 3/3 (100%) |
| Hypotonia | HP:0001252 | 3/3 (100%) |
| Spasticity | HP:0001257 | 3/3 (100%) |
| Seizure | HP:0001250 | 2/3 (67%) |
| Aggressive behavior | HP:0000718 | 2/3 (67%) |
| Hypertelorism | HP:0000316 | 1/3 (33%) |
| Agenesis of corpus callosum | HP:0001274 | 1/3 (33%) |
| Posteriorly rotated ears | HP:0000358 | 1/3 (33%) |
| Low-set ears | HP:0000369 | 1/3 (33%) |
| **Inheritance:** Autosomal recessive | HP:0000007 | — |

### Finding 7 — *AP1G1* is highly constrained; protein is a Golgi/endosomal clathrin adaptor

Population genetic constraint data (gnomAD; ENSG00000166747, chr16q22.2) demonstrate that *AP1G1* is **extremely intolerant to loss-of-function**: **pLI = 1.0**, observed/expected LoF = 0.065 (90% CI 0.037–0.121; **LOEUF ≈ 0.12**), LoF Z = 8.26; it is also **missense-constrained** (missense Z = 3.42; oe_mis = 0.75). The encoded protein (UniProt **O43747**, AP-1 complex subunit gamma-1, **822 aa**) functions in protein sorting at the late-Golgi/TGN and endosomes, recruiting clathrin and recognizing cargo sorting signals; with **AFTPH/aftiphilin** it traffics transferrin from early to recycling endosomes and shuttles **furin and cathepsin D**. Subcellular localizations: Golgi apparatus, TGN, clathrin-coated vesicle membrane, clathrin-coated pit, and perinuclear cytoplasm. The AP1γ1-mediated adaptor complex is *"essential for the formation of clathrin-coated intracellular vesicles"* ([PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/)).

### Finding 8 — ClinVar landscape is VUS-dominant

A ClinVar query (AP1G1[gene]) returned ~50 records with a germline-classification distribution of **Pathogenic 5, Likely pathogenic 3, Uncertain significance 28, Likely benign 3** — i.e., the evidence base is **dominated by variants of uncertain significance**, consistent with a recently delineated disease gene. No additional bi-allelic/recessive USRISR patients were identified in the literature beyond the defining cohort ([PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/)) and subsequent single case reports ([PMID: 38665048](https://pubmed.ncbi.nlm.nih.gov/38665048/); [PMID: 41226632](https://pubmed.ncbi.nlm.nih.gov/41226632/)).

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** USRISR is an ultra-rare autosomal recessive neurodevelopmental syndrome caused by bi-allelic hypomorphic missense variants in *AP1G1*. It belongs to the emerging group of **"adaptoropathies"** — Mendelian disorders of clathrin adaptor protein complexes — and produces a multisystem neurodevelopmental phenotype dominated by intellectual disability, developmental/speech delay, tone abnormalities, and epilepsy.

**Key identifiers.**
- **OMIM:** #619548 (recessive form USRISR); allelic dominant form USRISD #619467; gene *AP1G1* MIM \*603533
- **MONDO:** MONDO:0859196
- **Gene / HGNC:** *AP1G1* (HGNC:555); UniProt O43747; Ensembl ENSG00000166747; chromosome **16q22.2**
- **Orphanet / ICD-10 / ICD-11 / MeSH:** No specific dedicated codes identified; the disorder maps to general categories of hereditary intellectual disability / neurodevelopmental disorder (e.g., ICD-11 6A00 range for disorders of intellectual development). *Not available* as disease-specific codes at time of writing.

**Synonyms / alternative names:** Usmani-Riazuddin syndrome, autosomal recessive; USRISR; AP1G1-related neurodevelopmental disorder (recessive). The allelic dominant disorder is USRISD.

**Data provenance:** Information is derived from **aggregated disease-level resources** (OMIM, HPO, gnomAD, ClinVar, UniProt) and **individual-patient primary literature** (small case cohorts / case reports), not from EHR-scale datasets.

### 2. Etiology

**Causal factors — genetic.** USRISR is a **purely monogenic genetic disorder**. The primary cause is **bi-allelic (homozygous or compound heterozygous) missense variants in *AP1G1*** (p.Pro246His and p.Met369Val in the defining cohort). There is no environmental, infectious, or acquired contribution to disease causation.

**Genetic risk factors.** The causal variants are the recessive *AP1G1* missense alleles. **Consanguinity** is a key facilitating factor for the recessive form (the defining cohort included consanguineous/Pakistani families). No modifier loci or susceptibility variants have been established.

**Environmental risk factors / protective factors / gene–environment interactions:** *Not applicable / not available.* As a fully penetrant Mendelian recessive disorder, no environmental risk factors, protective factors, or gene–environment interactions have been described. Genetic "protection" derives simply from carrying at most one variant allele (heterozygous carriers are unaffected).

### 3. Phenotypes

USRISR is a **multisystem neurodevelopmental disorder** (see Finding 6 for the full HPO-annotated frequency table). Phenotype **types** span:
- **Cognitive/developmental (symptoms/signs):** intellectual disability (HP:0001249), global developmental delay (HP:0001263), delayed speech/language (HP:0000750) — each 3/3 in recessive patients.
- **Neuromuscular signs:** hypotonia (HP:0001252) and spasticity (HP:0001257) — each 3/3; these co-occurring tone abnormalities reflect central nervous system involvement.
- **Neurological:** seizures (HP:0001250) in ~2/3.
- **Behavioral:** aggressive behavior (HP:0000718) in ~2/3.
- **Dysmorphic / structural:** hypertelorism (HP:0000316), posteriorly rotated ears (HP:0000358), low-set ears (HP:0000369), and agenesis of the corpus callosum (HP:0001274) — each ~1/3.

**Characteristics:** age of onset is **neonatal/infantile to early childhood** (developmental delay evident from infancy); severity is **variable (mild to severe)**; course is generally **static/non-progressive** in the developmental sense (a neurodevelopmental, not neurodegenerative, disorder), though epilepsy may be episodic. **Quality-of-life impact** is substantial owing to intellectual disability, communication impairment, motor dysfunction, and behavioral challenges requiring lifelong support; no disease-specific QoL instrument data (EQ-5D/SF-36) are available.

### 4. Genetic / Molecular Information

- **Causal gene:** *AP1G1* (MIM \*603533; HGNC:555; UniProt O43747; 16q22.2), encoding AP-1 complex subunit gamma-1 (822 aa).
- **Pathogenic variants (recessive):** c.737C>A/p.Pro246His and c.1105A>G/p.Met369Val — both **missense**, predicted **hypomorphic** (loss/reduction of function via reduced protein level and altered endosome-recycling function, without disrupting AP-1 assembly).
- **Variant classification:** In the defining study these segregated as pathogenic recessive alleles; the broader ClinVar landscape is **VUS-dominant** (Pathogenic 5, Likely pathogenic 3, VUS 28, Likely benign 3).
- **Allele frequency:** The recessive disease alleles are **extremely rare**; *AP1G1* is highly constrained against both LoF (pLI = 1.0; LOEUF ≈ 0.12) and missense variation (Z = 3.42).
- **Somatic vs germline:** **Germline** (inherited from carrier parents).
- **Functional consequence:** **Loss/reduction of function** (hypomorphic) for the recessive alleles; by contrast, some dominant alleles act via haploinsufficiency (frameshift/splice) or dominant-negative (p.Gly66Arg) mechanisms.
- **Modifier genes / epigenetics / chromosomal abnormalities:** *Not available* — no modifiers, epigenetic marks, or large-scale chromosomal rearrangements have been implicated in the recessive form. (Notably, whole-genome sequencing has been used to characterize *AP1G1* CNVs in an Usmani-Riazuddin case where conventional methods were inconclusive — [PMID: 38840441](https://pubmed.ncbi.nlm.nih.gov/38840441/).)

### 5. Environmental Information

**Not applicable.** USRISR is a monogenic recessive disorder with no established environmental, lifestyle, or infectious contribution. AP-1 is broadly exploited by pathogens (e.g., Hepatitis E virus co-opts AP-1 for capsid trafficking, [PMID: 39117755](https://pubmed.ncbi.nlm.nih.gov/39117755/)), but this reflects general cell biology and has no etiologic role in USRISR.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (recessive form):**

1. **Bi-allelic hypomorphic *AP1G1* missense variants** (p.Pro246His, p.Met369Val) are inherited → **leads to** altered AP1γ1 protein folding (predicted in silico) and **reduced AP1γ1 protein levels** in cells (demonstrated in heterologous systems).
2. Reduced/altered AP1γ1 → **results in** impaired function of the **endosome-recycling arm** of AP-1–mediated trafficking (demonstrated), *without* disrupting AP-1 complex assembly (i.e., subunit interactions preserved — this distinguishes recessive from dominant alleles).
3. Defective endosome recycling → **leads to** mislocalization of **polarized somatodendritic membrane cargo** in neurons (inferred from AP-1's established role in polarized sorting; demonstrated for cargoes like megalin in epithelial models, [PMID: 31091172](https://pubmed.ncbi.nlm.nih.gov/31091172/)).
4. Aberrant neuronal protein sorting → **results in** disturbed neuronal development, connectivity, and excitability (inferred).
5. Disturbed neurodevelopment → **manifests as** global developmental delay, intellectual disability, speech delay, tone abnormalities (hypotonia/spasticity), epilepsy, behavioral anomalies, and (variably) corpus callosum agenesis (clinical observation).

**Branch (dominant allelic disorder, for contrast):** Haploinsufficient (frameshift/splice) or dominant-negative (p.Gly66Arg) alleles → disrupt AP-1 assembly/stoichiometry → overlapping neurodevelopmental phenotype (USRISD).

**Molecular pathway / cellular process:** clathrin-dependent vesicular trafficking (TGN ↔ early/recycling endosomes); AP-1 recruits clathrin and recognizes cargo sorting motifs; partners with AFTPH/aftiphilin to recycle transferrin and shuttle furin and cathepsin D. **GO terms:** intracellular protein transport (GO:0006886), clathrin-coated vesicle (GO:0030136), endosome to plasma membrane / recycling endosome (GO:0055037), establishment of protein localization / neuron projection development. **Cell types (CL):** neuron (CL:0000540), notably somatodendritic compartments. The mechanism is a **trafficking loss-of-function** ("adaptoropathy"); no immune, metabolic-deficiency, oxidative, or fibrotic mechanism is implicated. No disease-specific transcriptomic/proteomic/metabolomic profiling exists.

### 7. Anatomical Structures Affected

- **Primary organ / system:** the **central nervous system / brain** (UBERON:0000955) — the dominant site of pathology (neurons, CL:0000540). Body system: **nervous system** (UBERON:0001016).
- **Secondary structures:** **corpus callosum** (UBERON:0002336) may be absent/dysgenic; craniofacial structures show dysmorphism (hypertelorism; ear anomalies — external ear, UBERON:0001690).
- **Neuromuscular manifestation:** muscle tone abnormalities reflect CNS motor pathway involvement rather than primary muscle disease.
- **Subcellular compartments (GO CC):** Golgi apparatus (GO:0005794), trans-Golgi network (GO:0005802), endosome/recycling endosome (GO:0055037), clathrin-coated vesicle/pit (GO:0030136 / GO:0005905), perinuclear cytoplasm.
- **Lateralization:** manifestations (developmental, cognitive, tone) are **bilateral/generalized**.

### 8. Temporal Development

- **Onset:** **congenital/infantile** — developmental delay is apparent from infancy/early childhood; onset is **insidious/chronic** (a developmental, not acute, presentation).
- **Progression:** the disorder is a **static (non-degenerative) neurodevelopmental** condition; disability is **lifelong**. Epilepsy may follow an episodic course. Severity ranges mild to severe.
- **Patterns:** no spontaneous remission; the **critical period** for intervention is early childhood (developmental/rehabilitative support and seizure control).

### 9. Inheritance and Population

- **Inheritance pattern:** **autosomal recessive** (HP:0000007); the allelic dominant form is de novo autosomal dominant.
- **Epidemiology:** **ultra-rare**; prevalence and incidence are **not established** (fewer than a handful of recessive families reported worldwide). No registry-level figures available.
- **Penetrance / expressivity:** apparently **high/complete penetrance** with **variable expressivity** (mild-to-severe range).
- **Consanguinity / founder effects:** **consanguinity is an important facilitating factor**; the defining cohort included Pakistani families. No formal founder haplotype has been proven.
- **Carrier frequency:** expected to be very low given strong gene constraint; **not formally quantified**.
- **Sex ratio / age distribution / geographic distribution:** no sex bias established; affected individuals identified across diverse ethnicities; geographic clustering limited to consanguineous populations for the recessive form. Genetic anticipation and germline mosaicism: **not applicable / not reported**.

### 10. Diagnostics

- **Genetic testing is definitive.** Diagnosis rests on identifying **bi-allelic pathogenic *AP1G1* variants**, typically via **whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)**; WGS additionally resolves CNVs and zygosity where panels/microarray are inconclusive (as demonstrated for an Usmani-Riazuddin case, [PMID: 38840441](https://pubmed.ncbi.nlm.nih.gov/38840441/)). Segregation/trio analysis distinguishes recessive from de novo dominant alleles.
- **Supporting evaluations:** brain **MRI** (to assess corpus callosum and structural anomalies), **EEG** (for seizures), and developmental/neurological assessment.
- **Variant interpretation:** apply ACMG/AMP criteria; note the **VUS-dominant ClinVar landscape** — functional assays (protein-level, endosome-recycling, zebrafish rescue) are valuable for reclassification.
- **Biomarkers / metabolic / omics diagnostics:** **none specific**; no biochemical or metabolic marker exists.
- **Differential diagnosis:** other genetic intellectual disability / epilepsy syndromes and related **adaptoropathies** — notably **MEDNIK/IDEDNIK syndrome** (biallelic *AP1S1*, the σ1 subunit of AP-1; [PMID: 39269494](https://pubmed.ncbi.nlm.nih.gov/39269494/), [PMID: 41404470](https://pubmed.ncbi.nlm.nih.gov/41404470/)) and the allelic dominant USRISD. Distinguishing features: MEDNIK/IDEDNIK adds enteropathy, deafness, neuropathy, ichthyosis/keratoderma and copper-metabolism dysregulation, which are absent in USRISR.
- **Screening:** carrier and cascade testing within affected consanguineous families; prenatal/preimplantation diagnosis is feasible once the familial variants are known.

### 11. Outcome / Prognosis

- **Survival / mortality:** No systematic survival data. The disorder is **not primarily life-limiting** in reported recessive patients, though severe epilepsy and multisystem involvement may increase morbidity. (The complete loss-of-function state is embryonic-lethal in zebrafish, but human recessive patients carry hypomorphic, not null, alleles.)
- **Morbidity / function:** **significant lifelong disability** — intellectual disability, communication impairment, motor dysfunction, behavioral challenges.
- **Complications:** seizures, behavioral difficulties, feeding/tone-related issues; structural brain anomalies in a subset.
- **Prognostic factors:** severity of intellectual disability and epilepsy burden; no molecular prognostic biomarkers established.
- **Recovery:** none expected (static disorder); management improves function and quality of life but is not curative.

### 12. Treatment

**No disease-specific or disease-modifying therapy exists.** Management is **supportive and symptomatic**:
- **Pharmacotherapy:** **anti-seizure medications** (NCIT: Anticonvulsant Agent) for epilepsy; behavioral/psychiatric medications as indicated for aggression/behavioral anomalies. No pharmacogenomic guidance specific to USRISR.
- **Rehabilitative / supportive care:** **physical therapy, occupational therapy, speech-language therapy** (NCIT: Rehabilitation Therapy / Speech Therapy), special education, and developmental support; nutritional and tone management.
- **Advanced / experimental therapeutics:** **none** — no gene therapy, RNA-based, cell, or targeted therapies are in development or trials for USRISR (no NCT identifiers). Gene-restoration is conceptually plausible given the recessive loss-of-function mechanism but is entirely investigational.
- **Genetic counseling** is a core component of care (see Prevention).

### 13. Prevention

- **Primary prevention** of a recessive Mendelian disorder centers on **genetic counseling and reproductive planning** in at-risk (often consanguineous) families: carrier testing, cascade screening, and — once familial variants are known — **prenatal diagnosis or preimplantation genetic testing (PGT-M)**.
- **Secondary/tertiary prevention:** early developmental intervention and proactive seizure/behavior management to limit complications and optimize function.
- **Immunization / public-health / environmental measures:** *not applicable* (no infectious or environmental etiology). No population newborn-screening program exists for this ultra-rare disorder.

### 14. Other Species / Natural Disease

- **Model / orthology:** *AP1G1* is **evolutionarily conserved**. The zebrafish (*Danio rerio*, NCBI Taxon:7955) ortholog *ap1g1* is essential — knockout is embryonic/gastrula-stage lethal ([PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/); [PMID: 41226632](https://pubmed.ncbi.nlm.nih.gov/41226632/)). AP-1 γ-subunit function is conserved across metazoa and even fungi/protists (e.g., *Botrytis cinerea* AP-1β in cell-wall integrity/virulence, [PMID: 42668171](https://pubmed.ncbi.nlm.nih.gov/42668171/); *Plasmodium falciparum* AP-1 γ, [PMID: 41451970](https://pubmed.ncbi.nlm.nih.gov/41451970/)) — underscoring deep conservation of AP-1 trafficking mechanisms.
- **Natural disease in other species / veterinary relevance / zoonosis:** **none reported** — no naturally occurring *AP1G1* disorder is documented in companion animals or wildlife (OMIA); the disorder is not transmissible.

### 15. Model Organisms

- **Primary model:** **zebrafish (*Danio rerio*)** *ap1g1* knockout — the key functional model, exhibiting severe morphological defects and lethality that are **rescued by wild-type human *AP1G1* mRNA but not by disease-variant mRNA**, thereby validating pathogenicity ([PMID: 34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/); [PMID: 41226632](https://pubmed.ncbi.nlm.nih.gov/41226632/)).
- **Cellular / in vitro models:** heterologous cell systems used to measure AP1γ1 protein levels, subunit interactions, and endosome-recycling function; in silico 3D structural modeling predicted altered folding for the variants.
- **Phenotype recapitulation & limitations:** the zebrafish null captures **essentiality** and provides an in-vivo rescue assay, but as a **complete knockout** it models the null state rather than the human hypomorphic recessive genotype; it does not recapitulate the specific higher-order cognitive/behavioral phenotype. No mouse (MGI) knockout-based USRISR model or iPSC/organoid neuronal model has yet been reported for the recessive disorder.

---

## Mechanistic Model / Interpretation

```
 Bi-allelic AP1G1 missense variants (p.Pro246His, p.Met369Val)   [GERMLINE, RECESSIVE]
                         |
                         v  (predicted misfolding; reduced protein level — in vitro)
        Reduced / altered AP1-gamma1 subunit
                         |
                         |  NOTE: AP-1 complex ASSEMBLY preserved
                         |        (subunit interactions intact — distinguishes
                         |         recessive alleles from dominant ones)
                         v
        Impaired ENDOSOME-RECYCLING arm of AP-1 trafficking   (demonstrated)
                         |
                         v  (inferred for neurons; shown for epithelial cargo e.g. megalin)
        Mislocalization of polarized somatodendritic membrane cargo in neurons
                         |
                         v
        Disturbed neuronal development / connectivity / excitability   (inferred)
                         |
        ---------------------------------------------------------------
        |          |            |            |             |           |
        v          v            v            v             v           v
     Global      Intellectual  Speech     Hypotonia/    Seizures    CC agenesis /
     dev. delay  disability    delay      spasticity    (~2/3)      dysmorphism (~1/3)
     (3/3)       (3/3)         (3/3)      (3/3)
```

The unifying interpretation is that USRISR is a **clathrin adaptor trafficking disorder ("adaptoropathy")**. The recessive missense alleles are **hypomorphic** and act **downstream of complex assembly**, selectively degrading the **endosome-recycling** function of AP-1. Because AP-1 governs **polarized somatodendritic protein localization in neurons**, this trafficking deficit converges on a neurodevelopmental phenotype. This mechanistic model places USRISR firmly alongside other AP-complex disorders such as **MEDNIK/IDEDNIK syndrome** (*AP1S1*), reinforcing the concept that **defective clathrin adaptor-mediated cargo sorting is a recurrent basis for syndromic intellectual disability**.

---

## Evidence Base

| PMID | Title (abbrev.) | Role / contribution | Evidence type |
|---|---|---|---|
| [34102099](https://pubmed.ncbi.nlm.nih.gov/34102099/) | *De novo and bi-allelic variants in AP1G1 cause NDD…* | **Disease-defining study**: recessive & dominant variants, endosome-recycling mechanism, zebrafish rescue | Human clinical + in vitro + model organism |
| [38665048](https://pubmed.ncbi.nlm.nih.gov/38665048/) | *Usmani-Riazuddin syndrome can have a recognizable phenotype…* | Delineates recognizable multisystem phenotype; novel variant | Human clinical (case report) |
| [41226632](https://pubmed.ncbi.nlm.nih.gov/41226632/) | *Functional characterization of a novel c.196G>A variant* | Confirms zebrafish essentiality/rescue; dominant-negative allele | Model organism + in vitro |
| [38840441](https://pubmed.ncbi.nlm.nih.gov/38840441/) | *WGS for CNV detection in rare diseases* | Demonstrates WGS diagnostic utility for AP1G1/USRISR | Human clinical (diagnostics) |
| [31091172](https://pubmed.ncbi.nlm.nih.gov/31091172/) | *Clathrin and AP-1 control apical trafficking of megalin* | Mechanistic proof that γ1-subunit loss disrupts polarized sorting | In vitro (MDCK) |
| [39269494](https://pubmed.ncbi.nlm.nih.gov/39269494/) | *Revising pathogenesis of AP1S1-related MEDNIK…* | AP-1 as core trafficking machinery; differential-diagnosis context | Human clinical + computational |
| [39117755](https://pubmed.ncbi.nlm.nih.gov/39117755/) | *AP-1 essential for HEV ORF2 trafficking* | Supports AP-1 role in TGN↔recycling-endosome transport | In vitro (virology) |
| [42668171](https://pubmed.ncbi.nlm.nih.gov/42668171/); [41451970](https://pubmed.ncbi.nlm.nih.gov/41451970/) | AP-1 in *B. cinerea* / *P. falciparum* | Cross-species conservation of AP-1 γ-subunit trafficking | Model organism |

**Consistency:** All lines of evidence converge — human genetics (bi-allelic segregation), in vitro functional assays (reduced protein, endosome-recycling defect), structural modeling, and in-vivo zebrafish rescue — supporting a robust gene–disease relationship despite the small patient numbers.

---

## Limitations and Knowledge Gaps

1. **Tiny patient cohort.** Only a handful of recessive USRISR patients (n≈3 with curated HPO data) have been reported; phenotype frequencies and the full clinical spectrum are provisional and may shift as more cases accrue.
2. **VUS-dominant variant landscape.** ClinVar for *AP1G1* is dominated by variants of uncertain significance (28/~50), limiting confident recessive-variant interpretation without functional follow-up.
3. **No epidemiology.** Prevalence, incidence, carrier frequency, and any founder haplotype remain unquantified.
4. **Mechanistic inference in neurons.** The endosome-recycling defect is demonstrated in cellular systems, but the specific neuronal cargoes mislocalized in patient neurons are **inferred, not directly demonstrated**; a patient-derived neuronal (iPSC/organoid) model is lacking.
5. **Model gaps.** The zebrafish null models essentiality, not the human hypomorphic genotype; no mammalian (mouse) or humanized recessive model exists.
6. **No natural-history data, no QoL instruments, no prognostic biomarkers, and no therapeutics** specific to the disorder.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient cohort** via GeneMatcher/Matchmaker Exchange to refine genotype–phenotype correlations and reclassify VUS using ACMG PS3/PM functional criteria.
2. **Generate patient-derived iPSC neurons/organoids** carrying p.Pro246His and p.Met369Val to directly test polarized somatodendritic cargo sorting and identify specific mislocalized neuronal proteins.
3. **Build a knock-in mouse or humanized zebrafish** bearing the recessive hypomorphic alleles (rather than a null) to model the actual patient genotype and CNS phenotype.
4. **Deploy targeted functional assays** (AP1γ1 protein-level, transferrin/furin recycling, aftiphilin-dependent trafficking) as a standardized pipeline to adjudicate future *AP1G1* VUS.
5. **Establish a natural-history registry** capturing seizure course, developmental trajectory, MRI findings, and QoL to inform prognosis and future trial endpoints.
6. **Explore proof-of-concept gene/protein restoration** given the recessive loss-of-function mechanism (e.g., AAV-mediated *AP1G1* delivery or read-through/chaperone strategies for misfolding alleles) in the zebrafish rescue platform.

---

*Report compiled from an autonomous multi-iteration investigation (5 iterations; 8 confirmed findings; 13 papers reviewed). Evidence types are annotated throughout as human clinical, in vitro, model organism, or computational.*


## Artifacts

- [OpenScientist final report](Usmani-Riazuddin_Syndrome_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Usmani-Riazuddin_Syndrome_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 15 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 7 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001252` (2 mentions) - the report calls it "Hypotonia", "Neuromuscular signs:** hypotonia"; HP calls it **Hypotonia**, and lists "Muscular hypotonia" among its other names
- `HP:0001250` (2 mentions) - the report calls it "Seizure", "Neurological:** seizures"; HP calls it **Seizure**, and lists "Epileptic seizure" among its other names
- `HP:0000718` (2 mentions) - the report calls it "Aggressive behavior", "Behavioral:** aggressive behavior"; HP calls it **Aggressive behavior**
- `HP:0000316` (2 mentions) - the report calls it "Hypertelorism", "Dysmorphic / structural:** hypertelorism"; HP calls it **Hypertelorism**, and lists "Ocular hypertelorism" among its other names
- `HP:0000007` (2 mentions) - the report calls it "Inheritance:** Autosomal recessive", "autosomal recessive", "Inheritance pattern:** **autosomal recessive"; HP calls it **Autosomal recessive inheritance**
- `UBERON:0000955` (1 mention) - the report calls it "central nervous system / brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names
- `UBERON:0002336` (1 mention) - the report calls it "corpus callosum", "Secondary structures:** **corpus callosum"; UBERON calls it **corpus callosum**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001252` - called "Hypotonia", "Neuromuscular signs:** hypotonia"
- `HP:0001250` - called "Seizure", "Neurological:** seizures"
- `HP:0000718` - called "Aggressive behavior", "Behavioral:** aggressive behavior"
- `HP:0000316` - called "Hypertelorism", "Dysmorphic / structural:** hypertelorism"
- `HP:0000007` - called "Inheritance:** Autosomal recessive", "autosomal recessive", "Inheritance pattern:** **autosomal recessive"
- `HGNC:555` - called "AP1G1", "Gene / HGNC:** *AP1G1"
- `UBERON:0002336` - called "corpus callosum", "Secondary structures:** **corpus callosum"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Taxon`.

24 of 27 terms resolved to a current term; the rest could not be looked up either way.