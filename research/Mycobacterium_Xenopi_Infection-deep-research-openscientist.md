---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T04:15:50.912239'
end_time: '2026-09-30T04:37:06.197019'
duration_seconds: 1275.29
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mycobacterium Xenopi Infection
  mondo_id: MONDO:0017832
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
citation_count: 37
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 34
  quotes_valid: 34
  relevance_assessed: 37
  on_topic: 33
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 33
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mycobacterium_Xenopi_Infection-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mycobacterium_Xenopi_Infection-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mycobacterium Xenopi Infection
- **MONDO ID:** MONDO:0017832 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Mycobacterium Xenopi Infection** covering all of the
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

# Mycobacterium xenopi Infection — Comprehensive Disease Characteristics Report

**Disease:** Mycobacterium xenopi Infection
**MONDO ID:** MONDO:0017832
**Category:** Infectious Disease (nontuberculous mycobacterial pulmonary disease)
**NCBI Taxonomy:** *Mycobacterium xenopi* txid1789
**MeSH:** D009165 (Mycobacterium Infections, Nontuberculous)
**ICD-10:** A31.0 (pulmonary mycobacterial infection) · **ICD-11:** 1B21.0
**OMIM:** Not applicable (environmentally acquired infection, not a heritable Mendelian disease)

---

## Summary

*Mycobacterium xenopi* infection is a chronic nontuberculous mycobacterial (NTM) disease caused by a **slow-growing, thermophilic environmental bacillus** (optimal growth ~42–45 °C) that permanently colonizes warm and hot potable-water systems and their biofilms. Humans acquire it by inhalation, aspiration, or inoculation from environmental water — **not** from person to person. Its practical ubiquity in hot-water plumbing makes it both a genuine pathogen and a frequent contaminant, so a single positive culture often reflects colonization rather than disease. It is among the most common NTM pulmonary pathogens in **Europe (UK, France, Belgium, Central/Eastern Europe) and Canada (Ontario)**, typically ranking 2nd–3rd after the *Mycobacterium avium* complex (MAC), and in some series (e.g., Serbia, 34.8%) the single most common species.

The disease predominantly affects **older adults with pre-existing structural lung disease** — COPD, bronchiectasis, prior tuberculosis — or **impaired cell-mediated immunity**. It presents insidiously as chronic pulmonary disease in one of two main radiologic forms (nodular-bronchiectatic ~54% or fibrocavitary ~19%), with chronic cough, sputum, dyspnea, fatigue, weight loss and night sweats, and substantially impaired health-related quality of life. In profound immunosuppression (notably advanced HIV/AIDS with CD4 <40/µL), *M. xenopi* can cause extrapulmonary and disseminated infection. Notably, *M. xenopi* carries the **highest mortality among the pulmonary NTM species**, although much of this excess reflects the frailty and comorbidity of the affected host rather than the intrinsic virulence of the organism.

Diagnosis follows the composite **ATS/ERS/ESCMID/IDSA (2020)** criteria requiring concordant clinical, radiographic, and microbiologic evidence, with species identification by MALDI-TOF mass spectrometry and gene sequencing (rpoB, hsp65, 16S rDNA, 16S–23S ITS). Guideline treatment is a **prolonged multidrug regimen** of rifampicin + ethambutol + a macrolide (azithromycin preferred) and/or moxifloxacin, given for ≥12 months after sputum culture conversion, with parenteral amikacin added for cavitary/extensive or macrolide-resistant disease. A **rifamycin-containing regimen is specifically protective** for *M. xenopi* mortality. This is an environmentally acquired, **non-heritable** infection: there are no causal human genes, no Mendelian inheritance, penetrance, or carrier frequency. Human genetics contributes only **polygenic susceptibility** through the IL-12/IFN-γ axis, CFTR, SLC11A1 (NRAMP1), VDR and HLA, plus acquired neutralizing anti-IFN-γ autoantibodies.

---

## Key Findings

### Finding 1 — *M. xenopi* is a slow-growing, thermophilic environmental NTM causing chronic pulmonary disease, prevalent in Europe and Canada

*M. xenopi* is a slowly growing, scotochromogenic nontuberculous mycobacterium whose optimal growth temperature of approximately **42–45 °C** explains its persistent colonization of warm- and hot-water systems. This thermophilia is central to both its ecology and its diagnostic ambiguity. As stated in a mycobacteriosis review, "*M. xenopi permanently colonises most warm water systems, and its practical ubiquity makes difficult the interpretation of ambiguous findings on imaging*" ([PMID: 37871989](https://pubmed.ncbi.nlm.nih.gov/37871989/)).

Geographically, *M. xenopi* is a predominantly **European and Canadian** pathogen. A review of NTM epidemiology notes that "*in regions within Europe, M kansasii, M xenopi, and M malmoense are more common*" ([PMID: 25676516](https://pubmed.ncbi.nlm.nih.gov/25676516/)). Quantitatively, in a French multicenter cohort of 477 patients, "*The three most common NTM species were Mycobacterium avium complex (60%), M. xenopi (20%) and M. kansasii (5.7%)*" ([PMID: 34702233](https://pubmed.ncbi.nlm.nih.gov/34702233/)), making *M. xenopi* the 2nd most common cause of NTM pulmonary disease in France. Other series echo this: Geneva (12% of slow-growing NTM), Denmark (11%), and Serbia (34.8%, the most common species locally).

| Region | *M. xenopi* frequency among NTM | Source |
|--------|--------------------------------|--------|
| France (n=477) | 20% (2nd after MAC) | [PMID: 34702233](https://pubmed.ncbi.nlm.nih.gov/34702233/) |
| Geneva, Switzerland | 12% of slow-growing NTM | [PMID: 34875659](https://pubmed.ncbi.nlm.nih.gov/34875659/) |
| Vojvodina, Serbia (n=23) | 34.8% (most common) | [PMID: 41187188](https://pubmed.ncbi.nlm.nih.gov/41187188/) |
| Denmark | ~11% | [PMID: 40139333](https://pubmed.ncbi.nlm.nih.gov/40139333/) |

### Finding 2 — *M. xenopi* pulmonary disease carries the highest mortality among NTM pulmonary infections

Multiple lines of evidence establish that *M. xenopi* pulmonary disease is associated with the **highest mortality of any pulmonary NTM species**, while emphasizing that causality is confounded by host factors. A retrospective matched cohort study stated directly: "*Mycobacterium xenopi is associated with the highest mortality among pulmonary nontuberculous mycobacterial (NTM) infections, but whether this is due to the infection or other factors is unclear*" ([PMID: 32421543](https://pubmed.ncbi.nlm.nih.gov/32421543/)).

A population-based cohort from Ontario, Canada (9,681 NTM-PD; 10,936 NTM-PI) confirmed that "*NTM-PD was associated with higher death rates for all species combined, Mycobacterium avium complex, and M. xenopi*" ([PMID: 28221106](https://pubmed.ncbi.nlm.nih.gov/28221106/)). In the French cohort where *M. xenopi* comprised 20% of cases, "*The 2-year mortality was 14.4%*" ([PMID: 34702233](https://pubmed.ncbi.nlm.nih.gov/34702233/)); in that analysis, treatment was protective (HR ≈ 0.51) whereas age (HR ≈ 1.02) and *M. abscessus* were adverse. In the matched *M. xenopi* vs MAC comparison, the higher Charlson comorbidity index in the *M. xenopi* group (3.6 vs 3.2) points to **host frailty** as a major driver of the excess mortality rather than organism virulence alone.

### Finding 3 — Host risk factors: structural lung disease, immunosuppression, older age, low BMI, male sex/smoking

*M. xenopi* pulmonary disease occurs predominantly in patients with **pre-existing lung damage and impaired host defenses**. In the French cohort, "*Respiratory comorbidities were found in 68% of cases, tuberculosis sequelae in 31.4% of patients, and immunosuppression in 16.8% of cases*" ([PMID: 34702233](https://pubmed.ncbi.nlm.nih.gov/34702233/)). Radiologic forms in this and related cohorts were nodulobronchiectatic (~54%) and cavitary (~19%). A broad epidemiologic review notes that "*Host factors important to the current epidemiology of NTM pulmonary disease include thoracic skeletal abnormalities, rheumatoid arthritis, and use of immunomodulatory drugs. Clustering of disease within families suggests a heritable genetic predisposition to disease susceptibility*" ([PMID: 25676516](https://pubmed.ncbi.nlm.nih.gov/25676516/)).

Importantly, **pathogen genotype interacts with host susceptibility**. In Ontario, "*sequence type (ST) 5 was dominant in Ontario among 15 distinct STs and caused PD in people even without underlying lung disease, whereas disease due to non-ST5 was found almost exclusively in patients with underlying lung disease*" ([PMID: 29349535](https://pubmed.ncbi.nlm.nih.gov/29349535/)). Smoking and COPD are frequent (Serbia: smokers 55.6%, COPD 43.5%).

### Finding 4 — Guideline treatment: rifampicin + ethambutol + macrolide and/or moxifloxacin for ≥12 months after culture conversion

The 2020 ATS/ERS/ESCMID/IDSA guideline explicitly covers *M. xenopi*: "*This guideline focuses on pulmonary disease in adults (without cystic fibrosis or human immunodeficiency virus infection) caused by the most common NTM pathogens such as Mycobacterium avium complex, Mycobacterium kansasii, and Mycobacterium xenopi*" ([PMID: 32797222](https://pubmed.ncbi.nlm.nih.gov/32797222/), [PMID: 32628747](https://pubmed.ncbi.nlm.nih.gov/32628747/)). The recommended regimen is described as: "*The combination of rifampicin, ethambutol and macrolide (and/or moxifloxacin) is recommended for at least 12 months after conve[rsion]*" ([PMID: 33202438](https://pubmed.ncbi.nlm.nih.gov/33202438/)). Parenteral amikacin or streptomycin is added for cavitary or extensive nodular-bronchiectatic or macrolide-resistant disease, and adjuvant surgical resection is considered in selected patients ([PMID: 32791550](https://pubmed.ncbi.nlm.nih.gov/32791550/)).

Treatment outcomes, from the matched cohort: "*successful treatment was more common with Mx-PD (40.5% versus 16.7%, p = 0.02) owing to superior culture conversion (70.8% versus 33.3%, p = 0.0001)*" ([PMID: 32421543](https://pubmed.ncbi.nlm.nih.gov/32421543/)). High rates of in-vitro drug resistance are reported (84.6% resistant to ≥1 drug in a Polish series, [PMID: 21334944](https://pubmed.ncbi.nlm.nih.gov/21334944/)), but the correlation between in-vitro susceptibility and clinical outcome remains poorly defined for *M. xenopi*.

**Suggested NCIT intervention terms:** Rifampicin (NCIT:C29459), Ethambutol (NCIT:C61890), Azithromycin (NCIT:C737), Moxifloxacin (NCIT:C1741), Amikacin (NCIT:C220), Streptomycin (NCIT:C711).

### Finding 5 — Clinical phenotype: chronic respiratory symptoms with systemic features and marked QoL impairment

*M. xenopi*/NTM pulmonary disease presents insidiously with chronic respiratory and systemic symptoms. A concept-elicitation study for a novel NTM symptom scale reported: "*The concept elicitation interviews identified key symptoms of cough (100%), shortness of breath (98%), fatigue (95%), sputum production (90%), throat clearing (80%), mental fogging (75%), sensitivity to cold (62%), night sweats (55%), poor appetite (53%), chills/feverishness (50%/43%), weight loss (48%), and chest congestion (45%)*" ([PMID: 42070174](https://pubmed.ncbi.nlm.nih.gov/42070174/)). A Danish cohort (11% *M. xenopi*) found: "*Symptoms included cough (62%), expectoration (51%), dyspnea (43%), and systemic symptoms (42%), with 36% experiencing symptoms for over 6 months*" ([PMID: 40139333](https://pubmed.ncbi.nlm.nih.gov/40139333/)).

Quality of life is significantly impaired: "*The mean physical and mental HRQoL scores were 46.82 ± 6.33 and 43.95 ± 11.42, respectively, both significantly lower than the population norm of 50*" ([PMID: 42563732](https://pubmed.ncbi.nlm.nih.gov/42563732/)).

**Suggested HPO terms:** Chronic cough (HP:0031246), Productive cough (HP:0031245), Dyspnea (HP:0002094), Hemoptysis (HP:0002105), Fatigue (HP:0012378), Weight loss (HP:0001824), Night sweats (HP:0030166), Fever (HP:0001945), Bronchiectasis (HP:0002110), Pulmonary cavity (HP:0025426), Abnormal sputum (HP:0031417).

### Finding 6 — Disseminated/extrapulmonary disease in severely immunocompromised hosts (notably advanced HIV/AIDS)

Although pulmonary disease predominates, *M. xenopi* causes extrapulmonary and disseminated infection in profound immunosuppression. In an AIDS series of uncommon pulmonary NTM: "*Sixty-six percent of all patients with AIDS were infected by Mycobacterium xenopi. Chest radiographs of AIDS patients showed a tendency for predominance of interstitial infiltrate and rarity of fibronodular disease*" ([PMID: 9674460](https://pubmed.ncbi.nlm.nih.gov/9674460/)). The degree of immunodeficiency governs risk: "*Antiretroviral therapy (ART) and toxoplasmosis prophylaxis reduced the risk of NTM disease whereas CD4 cells <40/microl at time of the first AIDS defining illness led to a 2.5 fold higher risk*" ([PMID: 11076783](https://pubmed.ncbi.nlm.nih.gov/11076783/)).

*M. xenopi* falls into an "intermediate" clinical-relevance category: "*Mycobacterium avium complex (MAC), M. xenopi, and M. abscessus form an intermediate category between these two extremes*" ([PMID: 23460010](https://pubmed.ncbi.nlm.nih.gov/23460010/)). Extrapulmonary sites reported include spondylodiscitis/vertebral osteomyelitis, genitourinary tract (urine isolates, [PMID: 10624381](https://pubmed.ncbi.nlm.nih.gov/10624381/)), skin/soft tissue, and lymph nodes.

### Finding 7 — Genetic and immunologic host susceptibility: IL-12/IFN-γ axis, CFTR, SLC11A1, VDR, HLA, and anti-IFN-γ autoantibodies

Susceptibility to NTM lung disease, including *M. xenopi*, is linked to genetically determined defects of cell-mediated immunity. A review of susceptibility describes "*patients with genetically determined defects of cell-mediated immunity, including abnormalities of the interleukin-12/interferon-gamma axis, certain human leukocyte antigen alleles, cystic fibrosis transmembrane conductance regulator mutations, and polymorphisms of solute carrier 11A1 (or natural resistance-associated macrophage protein 1) and the vitamin D receptor*" ([PMID: 18515557](https://pubmed.ncbi.nlm.nih.gov/18515557/)). Acquired susceptibility includes "*inhibitory antibodies directed against interferon-gamma, post-menopausal waning of endogenous oestrogen levels, coeliac disease*" ([PMID: 18515557](https://pubmed.ncbi.nlm.nih.gov/18515557/)).

Model-organism genetics corroborate the role of SLC11A1/NRAMP1: in mice, "*susceptibility or resistance to infection caused by M. avium largely depended upon the Slc11a1 genotype*" ([PMID: 17664269](https://pubmed.ncbi.nlm.nih.gov/17664269/)). The Mendelian susceptibility to mycobacterial disease (MSMD) genes involved include IL12B, IL12RB1, IFNGR1, IFNGR2, and STAT1.

**Suggested GO terms:** interferon-gamma-mediated signaling pathway (GO:0060333), defense response to Gram-positive bacterium (GO:0050830), phagocytosis (GO:0006909), macroautophagy (GO:0016236).

### Finding 8 — Prognostic factors: rifamycin protective in *M. xenopi*; cavitation, low BMI, age, comorbidity, smear positivity worsen outcome

A systematic review/meta-analysis of 41 studies (10,452 NTM-LD patients) quantified outcomes: "*The overall all-cause mortality rate was 20% (95% CI 17-24%)*" ([PMID: 37147519](https://pubmed.ncbi.nlm.nih.gov/37147519/)), with clinical progression 46% and radiographic progression 43%. Crucially, a rifamycin regimen was protective specifically in *M. xenopi*: "*increasing body mass index (BMI), hemoptysis, and treatment with rifamycin regimen (in M. xenopi) were significantly associated with decreased all-cause mortality in multivariable analysis*" ([PMID: 37147519](https://pubmed.ncbi.nlm.nih.gov/37147519/)).

Adverse prognostic factors were numerous: "*Older age, male sex, history of TB, diabetes, chronic heart disease, malignancy, systemic immunosuppression, chronic liver disease, presence of cavity, consolidative radiologic features, acid-fast bacillus (AFB) smear positivity, hypoalbuminemia, anemia, increasing platelet count, high CRP, and high ESR were significantly associated with increased all-cause mortality*" ([PMID: 37147519](https://pubmed.ncbi.nlm.nih.gov/37147519/)).

| Direction | Prognostic factors |
|-----------|-------------------|
| **Increased mortality** | Older age, male sex, prior TB, diabetes, cardiac disease, malignancy, immunosuppression, liver disease, cavity, consolidation, AFB smear+, hypoalbuminemia, anemia, high CRP/ESR |
| **Decreased mortality** | Higher BMI, hemoptysis, **rifamycin regimen (M. xenopi-specific)** |

### Finding 9 — Diagnosis: composite ATS/ERS/ESCMID/IDSA criteria; identification by MALDI-TOF and gene sequencing

Diagnosis follows the standardized ATS/IDSA (2007) and ATS/ERS/ESCMID/IDSA (2020) criteria requiring **all** of: (1) pulmonary symptoms; (2) nodular or cavitary opacities on chest radiograph, or HRCT showing multifocal bronchiectasis with multiple small nodules; and (3) microbiologic confirmation (≥2 positive sputum cultures for the same species, OR ≥1 positive bronchial wash/lavage, OR compatible biopsy with granulomatous inflammation plus positive culture), while excluding other diagnoses. A review notes "*Diagnostic evaluation follows the established criteria for all nontuberculous mycobacteria, but with certain qualifications given species-specific and regional differences in pathogenicity*" ([PMID: 37890917](https://pubmed.ncbi.nlm.nih.gov/37890917/)).

Because *M. xenopi* colonizes water and has intermediate/low clinical relevance, a single isolate frequently reflects colonization: "*11 species, including M. fortuitum (32.4%), M. xenopi (20.0%), and M. gordonae (22.9%), showed clinical relevance below 50%*" ([PMID: 39306905](https://pubmed.ncbi.nlm.nih.gov/39306905/)) — underscoring the need for repeat sampling. Species identification uses MALDI-TOF mass spectrometry: "*Species identification was conducted by MALDI-TOF MS*" ([PMID: 40351313](https://pubmed.ncbi.nlm.nih.gov/40351313/)), supplemented by gene sequencing (rpoB, hsp65, 16S rDNA, 16S–23S ITS). **Differential diagnosis:** pulmonary TB, other NTM, lung cancer, chronic aspergillosis, COPD/bronchiectasis exacerbation.

### Finding 10 — Epidemiology: rising NTM-PD incidence worldwide; *M. xenopi* is male-predominant, European/Canadian, and not inherited

NTM pulmonary disease incidence is rising globally. US Medicare data (≥65 y, 2010–2019) reported "*an average annual incidence of 20.1 per 100,000 population. NTM PD incidence was overall highest in the South and among women, Asian individuals, and persons aged ≥ 80 years*" ([PMID: 39358723](https://pubmed.ncbi.nlm.nih.gov/39358723/)). In Korea, "*The incidence rates of NTM-PD annually increased by 14% (95% confidence interval, 10% to 19%) from 1.2 in 2006 to 4.8 in 2016*" ([PMID: 32550717](https://pubmed.ncbi.nlm.nih.gov/32550717/)). US pathogenic NTM prevalence rose 4.5%/year (2009–2015, [PMID: 32818422](https://pubmed.ncbi.nlm.nih.gov/32818422/)), and Japanese NTM-associated mortality rose from 0.63 to 1.93/100,000/year 1997–2016 ([PMID: 32556251](https://pubmed.ncbi.nlm.nih.gov/32556251/)).

Unlike female-predominant MAC, *M. xenopi* typically shows **male predominance**: "*M. avium and M. intracellulare were more often isolated from women, while M. kansasii, M. gordonae and M. xenopi predominated in men*" ([PMID: 30594996](https://pubmed.ncbi.nlm.nih.gov/30594996/)). This is an **environmentally acquired infection — NOT a heritable Mendelian condition**: there are no causal human genes, no inheritance pattern, penetrance, founder effect, or carrier frequency. Host genetic factors are polygenic susceptibility modifiers only.

### Finding 11 — Environmental reservoir and prevention: potable/hot-water contamination, pseudo-outbreaks, water/endoscope decontamination

*M. xenopi* is acquired from environmental water, colonizing potable and hospital hot-water systems and biofilms. Two classic hospital investigations illustrate the reservoir and its pitfalls. A nosocomial pseudo-outbreak (no true disease) was traced to tap water: "*M xenopi was isolated from tap water in 20 of 24 patient rooms tested, the endoscopy suite, and the central hot water mixing tank*" ([PMID: 8132983](https://pubmed.ncbi.nlm.nih.gov/8132983/)). Bronchoscopy-associated pseudoinfections showed that "*specimens obtained by bronchoscopy were more likely to yield M. xenopi than were specimens obtained by other routes (relative risk, 9.7; 95% confidence intervals, 3.2, 29.6)*" ([PMID: 8025757](https://pubmed.ncbi.nlm.nih.gov/8025757/)).

Prevention/control (no vaccine exists) centers on infection control: "*Adequate disinfection of contaminated bronchoscopes and careful collection of specimens to avoid contamination with contaminated water are essential*" ([PMID: 8025757](https://pubmed.ncbi.nlm.nih.gov/8025757/)). This includes hot-water-system management (temperature control, disinfection), sterile-water rinsing of endoscopes, and, for patients, reduced aerosol exposure. In HIV, ART/immune restoration prevents dissemination.

---

## Section-by-Section Report

### 1. Disease Information
*M. xenopi* infection is a chronic infectious disease caused by the slow-growing, thermophilic environmental NTM *Mycobacterium xenopi*. It most commonly manifests as chronic pulmonary disease and, rarely, disseminated/extrapulmonary disease in the severely immunocompromised. **Identifiers:** MONDO:0017832; MeSH D009165 (Mycobacterium Infections, Nontuberculous); NCBI Taxonomy txid1789; ICD-10 A31.0; ICD-11 1B21.0; no OMIM entry (not genetic). **Synonyms:** *M. xenopi* pulmonary disease, Mxe-PD/Mx-PD, xenopi mycobacteriosis, atypical/environmental/nontuberculous mycobacteriosis due to *M. xenopi*. Information is derived from **aggregated disease-level resources** (cohort studies, registries, reviews) rather than individual EHR.

### 2. Etiology
**Causal factor:** infection by *Mycobacterium xenopi* (NCBI:txid1789), acquired from environmental water. **Risk factors** — environmental/host: structural lung disease (COPD, bronchiectasis, prior TB sequelae 31.4%), immunosuppression (16.8%), older age, low BMI, male sex, smoking, thoracic skeletal abnormalities, rheumatoid arthritis, immunomodulatory drug use, advanced HIV (CD4 <40/µL → 2.5-fold risk). **Genetic risk (susceptibility modifiers only):** IL-12/IFN-γ axis genes (IL12B, IL12RB1, IFNGR1/2, STAT1), CFTR, SLC11A1/NRAMP1, VDR, HLA alleles; familial clustering suggests heritable predisposition. **Protective factors:** ART and higher BMI; rifamycin-containing treatment reduces mortality. **Gene–environment interaction:** disease requires the combination of environmental exposure and host defect; pathogen genotype (ST5 vs non-ST5) further modulates whether underlying lung disease is required.

### 3. Phenotypes
See Finding 5. Predominant phenotypes are chronic cough (62–100%), sputum production (51–90%), dyspnea (43–98%), fatigue (95%), weight loss (48%), night sweats (55%), fever/chills (43–50%), and hemoptysis in fibrocavitary disease. **Onset:** adult/late-onset, insidious/chronic. **Severity:** variable (milder in nodular-bronchiectatic, more severe in fibrocavitary). **Progression:** chronic, often progressive. **QoL:** significantly below population norm (physical 46.82, mental 43.95 vs 50). HPO terms listed in Finding 5.

### 4. Genetic/Molecular Information
**Not applicable as a genetic disease** — no causal human genes, pathogenic variants, chromosomal abnormalities, or modifier genes in the Mendelian sense. Human host-susceptibility loci (polygenic) are described in Finding 7: IL12B, IL12RB1, IFNGR1, IFNGR2, STAT1, CFTR, SLC11A1, VDR, HLA. The relevant "genome" for pathogenesis is bacterial: *M. xenopi* strains are typed by IS1395 RFLP and sequence typing (15 STs; ST5 dominant in Ontario). No germline/somatic human variant classification applies.

### 5. Environmental Information
The dominant etiologic factor is environmental: *M. xenopi* colonizes tap water, hospital hot-water tanks, showerheads, and biofilms; it resists chlorination and thrives at 42–45 °C. **Infectious agent:** *Mycobacterium xenopi* (slow-growing scotochromogen). It has also been isolated from fish-pond waters among diverse NTM ([PMID: 41107288](https://pubmed.ncbi.nlm.nih.gov/41107288/)). **Lifestyle:** smoking is a frequent co-factor. Routes of acquisition are inhalation of aerosols, aspiration, and inoculation. No person-to-person transmission.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. Environmental exposure to *M. xenopi* in aerosolized/aspirated warm water **leads to** deposition of bacilli in the distal airways.
2. In a host with impaired mucociliary clearance (bronchiectasis/COPD) or defective cell-mediated immunity, the bacilli **evade clearance and are phagocytosed by alveolar macrophages** (CL:0000583 alveolar macrophage).
3. Defects in the **IL-12/IFN-γ axis** (inferred from NTM susceptibility genetics) **result in** inadequate macrophage activation and failure to restrict intracellular mycobacterial growth (GO:0060333 IFN-γ signaling; GO:0006909 phagocytosis; GO:0016236 macroautophagy).
4. Persistent intracellular infection **leads to** chronic granulomatous inflammation with epithelioid histiocytes and lymphocytes in the lung parenchyma and airways.
5. Chronic inflammation **results in** progressive tissue damage — bronchial wall destruction (bronchiectasis), nodule formation, and, in the fibrocavitary form, caseous necrosis and cavitation.
6. Structural airway damage **leads to** the clinical phenotype (chronic cough, sputum, dyspnea, hemoptysis) and impaired gas exchange.
7. **Branch (immunocompromised host, e.g., CD4 <40/µL):** failure of containment **results in** hematogenous dissemination to extrapulmonary sites (bone, GU tract, skin, lymph nodes).

**Upstream** mechanisms are host immune defect + environmental exposure; **downstream** are granulomatous inflammation, fibrosis/cavitation, and airway remodeling. **Cell types:** alveolar macrophages (CL:0000583), T lymphocytes (CL:0000084), epithelioid histiocytes, bronchial epithelial cells (CL:0002328). **Processes:** granulomatous inflammation, chronic inflammation, IFN-γ signaling, phagocytosis, autophagy. Detailed molecular pathway data specific to *M. xenopi* (transcriptomics, proteomics, metabolomics) are **not available** in the literature reviewed; the chain above is largely inferred from general mycobacterial immunology.

### 7. Anatomical Structures Affected
**Primary organ:** lung (UBERON:0002048). **Structures:** bronchi/bronchioles (bronchiectasis, UBERON:0002185), lung parenchyma (nodules, cavities). **Body system:** respiratory (UBERON:0001004). **Secondary/disseminated:** vertebral column/intervertebral disc (spondylodiscitis, UBERON:0001130), kidney/urinary tract (UBERON:0002113), skin/soft tissue (UBERON:0002097), lymph nodes (UBERON:0000029). **Cells:** alveolar macrophage (CL:0000583), bronchial epithelial cell (CL:0002328), T cell (CL:0000084). **Subcellular:** phagosome/phagolysosome (GO:0045335), where mycobacteria reside. **Lateralization:** often bilateral in nodular-bronchiectatic disease; cavitary disease frequently upper-lobe predominant.

### 8. Temporal Development
**Onset:** adult/late-onset, insidious and chronic; symptoms present >6 months in ~36% at diagnosis. **Progression:** slow but progressive; two radiologic trajectories (nodular-bronchiectatic, generally milder; fibrocavitary, more aggressive). Bronchiectasis and nodules tend to persist even with microbiologic cure, whereas cavities/consolidation/bronchiolitis regress with successful treatment ([PMID: 39088042](https://pubmed.ncbi.nlm.nih.gov/39088042/)). **Course:** chronic, often lifelong; relapse/recurrence common. **Remission:** treatment-induced culture conversion in ~70% of *M. xenopi* patients when treated. **Critical period:** early treatment initiation is advised for smear-positive or cavitary disease.

### 9. Inheritance and Population
See Finding 10. NTM-PD incidence is rising globally (US ~20.1/100,000 in ≥65 y; Korea 14%/year increase). *M. xenopi* is **male-predominant**, European/Canadian in distribution, and **not inherited** (no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency apply). Host susceptibility is polygenic/multifactorial. Age distribution skews older (peak mortality ages 80–84 in Japan).

### 10. Diagnostics
See Finding 9. **Microbiology:** AFB smear, culture (solid + liquid; slow-growing, ~28–68 days), MALDI-TOF MS, gene sequencing (rpoB, hsp65, 16S rDNA, ITS). **Imaging:** chest radiograph and HRCT (nodular bronchiectasis vs fibrocavitary patterns; CT scoring for treatment response). **Criteria:** ATS/ERS/ESCMID/IDSA composite (clinical + radiographic + ≥2 concordant cultures). **Drug susceptibility testing** per CLSI recommended, though clinical correlation is uncertain. **Biomarkers:** anti-GPL-core IgA is specific for MAC/*M. abscessus*, not *M. xenopi*. **Differential diagnosis:** TB, lung cancer, chronic pulmonary aspergillosis, other NTM. Genetic/omics diagnostics are not applicable for diagnosis of this infection.

### 11. Outcome/Prognosis
See Findings 2 and 8. Pooled NTM-LD all-cause mortality ~20% (95% CI 17–24%); *M. xenopi* has the highest mortality among pulmonary NTM, largely comorbidity-driven; French 2-year mortality 14.4%. **Treatment success** ~40.5% for *M. xenopi* (culture conversion ~70.8%). **Prognostic factors** tabulated in Finding 8; rifamycin regimen is specifically protective. **Complications:** respiratory failure, recurrent infection, hemoptysis, progression of bronchiectasis, dissemination in immunocompromised.

### 12. Treatment
See Finding 4. **Core regimen:** rifampicin + ethambutol + macrolide (azithromycin) and/or moxifloxacin, ≥12 months post-conversion. **Intensification:** parenteral amikacin/streptomycin for cavitary/extensive/macrolide-resistant disease; inhaled amikacin (ALIS) for refractory disease. **Surgery:** adjuvant resection for localized/refractory disease (recurrence risk substantial). **Supportive:** airway clearance, pulmonary rehabilitation, nutrition, management of comorbidities. **Refractory disease:** individualized intensification ([PMID: 41733158](https://pubmed.ncbi.nlm.nih.gov/41733158/)). No gene/cell/RNA/targeted/immunotherapies apply. NCIT terms in Finding 4.

### 13. Prevention
See Finding 11. No vaccine. **Primary prevention:** water-system management (temperature/disinfection), endoscope decontamination with sterile-water rinse, aerosol-exposure reduction, avoiding tap-water contact with specimens/instruments. **Secondary prevention:** early detection in high-risk patients (COPD, bronchiectasis, immunosuppressed). **Tertiary prevention:** airway clearance, comorbidity management, ART in HIV to prevent dissemination. No primary chemoprophylaxis is defined specifically for *M. xenopi* (azithromycin prophylaxis applies to disseminated MAC in advanced HIV).

### 14. Other Species / Natural Disease
*M. xenopi* was originally isolated from the toad *Xenopus laevis* (hence the name). It is an environmental organism found in fish-pond waters ([PMID: 41107288](https://pubmed.ncbi.nlm.nih.gov/41107288/)) among diverse NTM. Naturally occurring clinical disease in companion animals/wildlife is not well documented in the reviewed literature. **Zoonotic potential:** not a recognized zoonosis; acquisition is from shared environmental water reservoirs rather than animal-to-human transmission. Orthologous host-defense genes (Slc11a1/Nramp1) in mice control susceptibility to related NTM (*M. avium*).

### 15. Model Organisms
No dedicated *M. xenopi* animal model is established in the reviewed literature. **Relevant models for NTM susceptibility:** mouse strains differing at *Slc11a1* (Nramp1) demonstrate near-monogenic control of susceptibility to environmental mycobacteria (*M. avium*) ([PMID: 17664269](https://pubmed.ncbi.nlm.nih.gov/17664269/)); I/St vs A/Sn mouse comparisons dissect TB vs *M. avium* susceptibility. **Applications:** studying host genetic control of macrophage mycobacterial restriction and the IL-12/IFN-γ axis. **Limitation:** these models use *M. avium*/*M. tuberculosis*, not *M. xenopi*; slow growth and thermophilia of *M. xenopi* complicate murine modeling. **Resources:** MGI (Slc11a1).

---

## Mechanistic Model / Interpretation

```
   ENVIRONMENTAL RESERVOIR                     HOST SUSCEPTIBILITY
   (warm/hot potable water,          +        (structural lung disease:
    biofilms, 42-45°C, chlorine-              COPD/bronchiectasis/prior TB;
    resistant; pseudo-outbreaks)               impaired CMI: IL-12/IFN-γ axis,
            |                                   CFTR, SLC11A1, VDR, HLA;
            | inhalation/aspiration             advanced HIV CD4<40)
            v                                            |
   [1] Bacilli deposited in distal airways  <-----------+
            |
            v
   [2] Phagocytosed by alveolar macrophages (CL:0000583)
            |
            v
   [3] Defective IFN-gamma macrophage activation -> failed intracellular killing
            |
            v
   [4] Chronic granulomatous inflammation
            |
      +-----+---------------------------+
      v                                 v
   [5a] Nodular-bronchiectatic     [5b] Fibrocavitary
        (~54%, milder)                  (~19%, caseation + cavitation, worse)
      |                                 |
      v                                 v
   [6] Chronic cough, sputum, dyspnea, hemoptysis, systemic Sx, low QoL
      |
      | (branch: profound immunosuppression)
      v
   [7] Hematogenous dissemination -> bone, GU, skin, lymph node

   OUTCOME MODIFIERS:  + rifamycin regimen (protective, M. xenopi-specific)
                       - cavitation, low BMI, age, comorbidity, smear+
```

The unifying interpretation is a **two-hit model**: ubiquitous environmental exposure (necessary but not sufficient) combined with a permissive host (structural and/or immunologic defect). The organism's high apparent mortality is largely a **marker of host frailty** — it selectively establishes disease in patients who are already sick — rather than a reflection of exceptional intrinsic virulence. This explains why treatment (especially rifamycin-containing) improves survival while comorbidity burden dominates the prognosis.

---

## Evidence Base

| Finding | Key PMID(s) | Role |
|---------|------------|------|
| Thermophilic waterborne reservoir; Europe/Canada | [37871989](https://pubmed.ncbi.nlm.nih.gov/37871989/), [25676516](https://pubmed.ncbi.nlm.nih.gov/25676516/), [34702233](https://pubmed.ncbi.nlm.nih.gov/34702233/) | Support |
| Highest NTM mortality | [32421543](https://pubmed.ncbi.nlm.nih.gov/32421543/), [28221106](https://pubmed.ncbi.nlm.nih.gov/28221106/), [34702233](https://pubmed.ncbi.nlm.nih.gov/34702233/) | Support |
| Host risk factors; genotype interaction | [34702233](https://pubmed.ncbi.nlm.nih.gov/34702233/), [25676516](https://pubmed.ncbi.nlm.nih.gov/25676516/), [29349535](https://pubmed.ncbi.nlm.nih.gov/29349535/) | Support |
| Guideline treatment | [32797222](https://pubmed.ncbi.nlm.nih.gov/32797222/), [33202438](https://pubmed.ncbi.nlm.nih.gov/33202438/), [32421543](https://pubmed.ncbi.nlm.nih.gov/32421543/), [32791550](https://pubmed.ncbi.nlm.nih.gov/32791550/) | Support |
| Clinical phenotype & QoL | [42070174](https://pubmed.ncbi.nlm.nih.gov/42070174/), [40139333](https://pubmed.ncbi.nlm.nih.gov/40139333/), [42563732](https://pubmed.ncbi.nlm.nih.gov/42563732/) | Support |
| Dissemination in AIDS | [9674460](https://pubmed.ncbi.nlm.nih.gov/9674460/), [11076783](https://pubmed.ncbi.nlm.nih.gov/11076783/), [23460010](https://pubmed.ncbi.nlm.nih.gov/23460010/) | Support |
| Host susceptibility genetics | [18515557](https://pubmed.ncbi.nlm.nih.gov/18515557/), [17664269](https://pubmed.ncbi.nlm.nih.gov/17664269/) | Support |
| Prognostic factors; rifamycin protective | [37147519](https://pubmed.ncbi.nlm.nih.gov/37147519/) | Support |
| Diagnostic criteria; identification | [37890917](https://pubmed.ncbi.nlm.nih.gov/37890917/), [39306905](https://pubmed.ncbi.nlm.nih.gov/39306905/), [40351313](https://pubmed.ncbi.nlm.nih.gov/40351313/) | Support |
| Epidemiology; male predominance; non-heritable | [39358723](https://pubmed.ncbi.nlm.nih.gov/39358723/), [32550717](https://pubmed.ncbi.nlm.nih.gov/32550717/), [30594996](https://pubmed.ncbi.nlm.nih.gov/30594996/) | Support |
| Environmental reservoir; pseudo-outbreaks; prevention | [8132983](https://pubmed.ncbi.nlm.nih.gov/8132983/), [8025757](https://pubmed.ncbi.nlm.nih.gov/8025757/) | Support |

Across 66 papers reviewed, evidence is **highly consistent** on the core narrative. The main internal tension — whether high mortality reflects the organism or the host — is directly addressed by [PMID: 32421543](https://pubmed.ncbi.nlm.nih.gov/32421543/) and resolved in favor of host comorbidity by the elevated Charlson indices and by [PMID: 28387523](https://pubmed.ncbi.nlm.nih.gov/28387523/) ("*few deaths were directly attributable to mycobacterial infection*").

---

## Limitations and Knowledge Gaps

- **Evidence quality:** Most treatment and outcome data derive from retrospective, observational cohorts; there are few randomized controlled trials specific to *M. xenopi*, and guideline recommendations are largely low-certainty (GRADE).
- **In-vitro/in-vivo disconnect:** The correlation between drug susceptibility testing and clinical outcome is poorly defined for *M. xenopi*, complicating regimen selection.
- **Colonization vs disease:** The low clinical relevance of single isolates (~20%) means epidemiologic figures conflate colonization and true disease.
- **Molecular pathophysiology:** No *M. xenopi*-specific transcriptomic, proteomic, metabolomic, or single-cell datasets were identified; the mechanistic chain is largely inferred from generic NTM/mycobacterial immunology.
- **Model organisms:** No dedicated *M. xenopi* animal model exists; susceptibility genetics are extrapolated from *M. avium*/*M. tuberculosis* mouse models.
- **Host genetics:** Susceptibility loci (IL-12/IFN-γ, CFTR, SLC11A1, VDR, HLA) are associations from broader NTM literature, not *M. xenopi*-specific GWAS.

## Proposed Follow-up Experiments / Actions

1. **Prospective *M. xenopi* treatment trial** comparing rifamycin-containing vs rifamycin-sparing regimens, powered on culture conversion and mortality, to confirm the observational protective signal ([PMID: 37147519](https://pubmed.ncbi.nlm.nih.gov/37147519/)).
2. **DST–outcome correlation study**: systematically link CLSI-based susceptibility results to clinical outcomes to establish clinically meaningful breakpoints for *M. xenopi*.
3. **Host immunogenetic profiling**: targeted sequencing/screening of IL-12/IFN-γ axis, CFTR, SLC11A1, VDR and anti-IFN-γ autoantibodies in *M. xenopi* cohorts to quantify attributable susceptibility.
4. **Genotype–phenotype validation**: replicate the ST5/non-ST5 virulence association ([PMID: 29349535](https://pubmed.ncbi.nlm.nih.gov/29349535/)) in independent geographic cohorts with whole-genome sequencing.
5. **Water-system intervention trial**: evaluate hospital hot-water disinfection/temperature protocols on *M. xenopi* pseudo-outbreak and true-infection rates.
6. **Molecular pathophysiology**: generate macrophage-infection transcriptomic/proteomic datasets with *M. xenopi* to move the causal chain from inferred to demonstrated.
7. **Standardized QoL longitudinal tracking** using the NTM symptom scale ([PMID: 42070174](https://pubmed.ncbi.nlm.nih.gov/42070174/)) to define patient-centered treatment endpoints.

---

*Report compiled from a 5-iteration autonomous investigation reviewing 66 papers and confirming 11 findings. Evidence source types: predominantly human clinical (cohorts, registries, guidelines); model-organism (mouse Slc11a1); no in-vitro/computational primary data specific to M. xenopi pathogenesis.*


## Artifacts

- [OpenScientist final report](Mycobacterium_Xenopi_Infection-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mycobacterium_Xenopi_Infection-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 34 |
| Quoted claims found in source | 34 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 37 |
| On topic | 33 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.