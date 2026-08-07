---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-31T00:59:08.912452'
end_time: '2026-07-31T01:19:03.181797'
duration_seconds: 1194.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Febrile Ulceronecrotic Mucha-Habermann Disease
  mondo_id: ''
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 24
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Febrile_Ulceronecrotic_Mucha-Habermann_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Febrile_Ulceronecrotic_Mucha-Habermann_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Febrile Ulceronecrotic Mucha-Habermann Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Febrile Ulceronecrotic Mucha-Habermann Disease** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Febrile Ulceronecrotic Mucha–Habermann Disease (FUMHD): A Comprehensive Disease Characteristics Report

*Evidence base: aggregated disease-level literature — case reports, case series, and systematic reviews (no dedicated registry/EHR cohort, no omics datasets, no animal models). Evidence type throughout is **human clinical** unless otherwise noted. 15 findings confirmed across 5 iterations; 41 papers reviewed.*

---

## Summary

**Febrile Ulceronecrotic Mucha–Habermann Disease (FUMHD)** is a rare, fulminant, potentially fatal variant of pityriasis lichenoides et varioliformis acuta (PLEVA) — the acute pole of the pityriasis lichenoides (PL) spectrum (PLC → PLEVA → FUMHD). It is defined by the **sudden onset of generalized, painful, coalescing ulceronecrotic papules and plaques** with hemorrhagic bullae and necrotic crusts, accompanied by **high fever (≥39 °C)** and multi-organ systemic involvement. It frequently begins as classic PLEVA and evolves over days to a few weeks; in adults it may involve more than 90% of the body surface area.

FUMHD is **immune-mediated and non-genetic**. The best-supported model is a **dysregulated cytotoxic CD8⁺ T-cell response**, typically triggered by an infectious/antigenic stimulus (EBV, HSV-2, *Toxoplasma gondii*, HIV, *Mycoplasma*) or hypersensitivity, producing interface dermatitis, keratinocyte necrosis, and lymphocytic vasculitis. Progression to fulminant disease is associated with **markedly elevated serum TNF-α**, which amplifies keratinocyte apoptosis. A subset of cases harbors a **somatic monoclonal T-cell receptor (TCR) rearrangement**, placing FUMHD on a continuum with cutaneous T-cell lymphoma (CTCL) and predicting worse outcomes. Skin-barrier failure leads to superinfection/sepsis, DIC, and multi-organ failure — the dominant causes of death.

Only ~120 cases exist in the world literature. **Case-fatality is ~12–20%, strongly age-dependent (children ~2% vs. adults ~20%)**. Diagnosis is **clinicopathologic** (no universally accepted criteria; Nofal 2016 proposed a constant + variable criteria framework). Treatment is **empirical and multimodal** — systemic corticosteroids, methotrexate, IVIG, antibiotics, and TNF-α inhibitors in refractory cases — balanced against infection risk. There are no causal genes, no animal models, and no applicable primary prevention; efforts focus on early recognition and sepsis prevention.

---

## Key Findings

### Finding 1 — Definition and nosology

FUMHD is consistently defined as a rare, severe, potentially fatal PLEVA variant marked by sudden generalized ulceronecrotic papules coalescing into ulcers with high fever and systemic symptoms, often progressing from classic PLEVA. *"Febrile ulceronecrotic Mucha-Habermann disease is a rare and severe variant of pityriasis lichenoides, characterized by sudden onset of generalized ulceronecrotic papules that rapidly coalesce into ulcers associated with high fever"* ([PMID: 38959922](https://pubmed.ncbi.nlm.nih.gov/38959922/)). The PLEVA-to-FUMHD progression and high mortality are captured by: *"FUMHD often starts out as classic PLEVA, but goes on to develop widespread ulceronecrotic lesions and is associated with a high mortality rate"* ([PMID: 15583604](https://pubmed.ncbi.nlm.nih.gov/15583604/)).

### Finding 2 — Identifiers, synonyms, classification

Because FUMHD is non-Mendelian, no distinct OMIM number exists; identifiers are inherited from the parent PLEVA/PL entity.

| Resource | Identifier |
|---|---|
| MeSH | **Pityriasis Lichenoides** (D017517) — no dedicated FUMHD heading |
| ICD-10 | **L41.0** (Pityriasis lichenoides et varioliformis acuta) |
| ICD-11 | **EA06.0** (Pityriasis lichenoides) |
| MONDO | **MONDO:0006559** (pityriasis lichenoides et varioliformis acuta) |
| Orphanet | Under PLEVA |
| OMIM | None (non-genetic) |

**Synonyms:** FUMHD; ulceronecrotic Mucha–Habermann disease; pityriasis lichenoides et varioliformis acuta fulminans; PLEVA fulminans; (historic) acute parapsoriasis. Information derives from aggregated disease-level resources and pooled case reports, **not** individual-patient EHR data.

### Finding 3 — Epidemiology

FUMHD is extremely rare. A systematic MEDLINE review identified **119 cases** with overall lethality 14/119 (**12%**, CI 6–17%), children 2% (1/54) vs. adults 20% (13/65): *"Literature review revealed 119 FUMHD cases. Overall lethality was 14/119 (12%, CI 6-17%), and lethality in children was lower (1/54, 2%, CI 0-6%) compared to adults (13/65, 20%, CI 11-31%)"* ([PMID: 34287852](https://pubmed.ncbi.nlm.nih.gov/34287852/)). An independent PRISMA review found 68 patients across 63 publications: *"Out of 68 patients, 55 patients had their condition fully resolved and 13 cases were fatal"* ([PMID: 36483219](https://pubmed.ncbi.nlm.nih.gov/36483219/)). No formal prevalence/incidence estimates exist. There is a clear **male predominance (~75%)** across all ages.

### Finding 4 — Clinical phenotype

The core cutaneous phenotype is sudden, generalized, painful, coalescing ulceronecrotic papules/plaques with hemorrhagic bullae and necrotic crusts, healing with varioliform scars and dyspigmentation; constitutional features include high fever, malaise, arthralgia, and lymphadenopathy. Quantitatively: *"Most of them were male (62/83, 74.7%), with high fever state (50/80, 62.5% had a high fever of 39°C or above), and with more positive skin bacterial cultures (31/41, 75.6%)"* ([PMID: 35950146](https://pubmed.ncbi.nlm.nih.gov/35950146/)).

**Suggested HPO terms:** Skin ulcer (HP:0200041), Cutaneous/epidermal necrosis (HP:0100683), Papule (HP:0200034), Bulla/vesicle (HP:0008064), Fever (HP:0001945), Arthralgia (HP:0002829), Lymphadenopathy (HP:0002716), Thrombocytopenia (HP:0001873), Abnormal skin pigmentation (HP:0001000), Scarring (HP:0200042). Quality-of-life impact is high during the acute phase (severe pain, extensive open wounds, hospitalization); no formal EQ-5D/SF-36/PROMIS data exist.

### Finding 5 — Systemic organ involvement

Systemic manifestations are common and drive mortality: *"Systemic manifestations such as intravascular disseminated coagulation and pulmonary, cardiac, gastrointestinal, and central nervous system involvement are common"* ([PMID: 38959922](https://pubmed.ncbi.nlm.nih.gov/38959922/)). Complications include DIC, interstitial pneumonitis/ARDS (fatal in one de novo case, [PMID: 36686043](https://pubmed.ncbi.nlm.nih.gov/36686043/)), cardiac/GI/CNS involvement, cytopenias, and **hemophagocytic lymphohistiocytosis (HLH)**: *"The patient also met 7 of 9 HLH-2004 criteria, leading to a diagnosis of HLH"* ([PMID: 38457671](https://pubmed.ncbi.nlm.nih.gov/38457671/)). FUMHD can mimic Stevens–Johnson syndrome/TEN and Kawasaki disease ([PMID: 31814284](https://pubmed.ncbi.nlm.nih.gov/31814284/)).

### Finding 6 — Pathogenesis: cytotoxic T cells + TNF-α + clonality

Histology shows a dense perivascular/intramural **CD8⁺ cytotoxic** lymphocytic infiltrate with interface dermatitis, keratinocyte necrosis, and lymphocytic vasculitis; an atypical immunophenotype is described: *"Biopsy indicated a dermal and subcutaneous infiltrate of atypical CD8+ lymphocytes with loss of CD5 and reduction in CD7 expression, along with features of lymphomatoid vasculitis"* ([PMID: 38457671](https://pubmed.ncbi.nlm.nih.gov/38457671/)). The PLEVA→FUMHD transition is associated with elevated TNF-α despite normal CRP: *"his skin lesions started to ulcerate progressively, involving > 90% of his body surface, accompanied by high fever, normal C-reactive protein, but highly elevated serum levels of tumour necrosis factor (TNF)-alpha"* ([PMID: 15840118](https://pubmed.ncbi.nlm.nih.gov/15840118/)). A subset shows monoclonal T cells: *"we report two cases of FUMHD with monoclonal T-cell population, as detected by Southern blot analysis. We propose that clonal FUMHD represents a cutaneous T-cell lymphoma entity"* ([PMID: 15583604](https://pubmed.ncbi.nlm.nih.gov/15583604/)).

**Suggested GO terms:** T cell mediated cytotoxicity (GO:0001913), apoptotic process (GO:0006915), inflammatory response (GO:0006954), tumor necrosis factor-mediated signaling (GO:0033209), leukocyte migration (GO:0050900). **Suggested CL terms:** CD8-positive, alpha-beta T cell (CL:0000625); keratinocyte (CL:0000312); vascular endothelial cell.

### Finding 7 — Etiology and triggers

Etiology is unknown; three hypotheses dominate: *"PLEVA is speculated to be an inflammatory reaction triggered by certain infectious agents, an inflammatory response secondary to T-cell dyscrasia, or an immune complex-mediated hypersensitivity"* ([PMID: 20465660](https://pubmed.ncbi.nlm.nih.gov/20465660/)). Infectious triggers of the PL spectrum: *"Epstein-Barr virus, Toxoplasma gondii, and HIV are the most frequently reported infectious triggers of pityriasis lichenoides"* ([PMID: 12894107](https://pubmed.ncbi.nlm.nih.gov/12894107/)). FUMHD-specific associations include **HSV-2** ([PMID: 19103367](https://pubmed.ncbi.nlm.nih.gov/19103367/)) and *Mycoplasma*. Preceding infection is documented in 60.3% of pediatric PL with winter/spring seasonality. **No genetic, toxin, lifestyle, or occupational risk factor, and no protective factors or gene–environment interactions** are defined.

### Finding 8 — Mortality risk factors and prognosis

*"Risk factors for a fatal outcome (likelihood ratio; P) were sepsis (24.97, P < 0.001), adult vs. pediatric patient age (11.19; P = 0.001), systemic involvement (19.97, P < 0.001), and mucosal involvement (4.58; P = 0.032)"* ([PMID: 34287852](https://pubmed.ncbi.nlm.nih.gov/34287852/)). A proposed mortality score (Age/10 + 4 + 4·[systemic] + 1·[mucosal]) has 93% sensitivity / 77% specificity, and infection is the leading cause of death: *"infectious complications are a frequent cause of death."* An independent review adds clonality: *"Increased age, systemic involvement, and monoclonal T-cell receptor rearrangement were associated with worst prognosis, but mucosal involvement did not affect mortality risk"* ([PMID: 36483219](https://pubmed.ncbi.nlm.nih.gov/36483219/)). The adult effect is large: *"Adults were associated with a higher risk of death (OR = 12.976, 95% CI: 1.049, 160.504)"* ([PMID: 35950146](https://pubmed.ncbi.nlm.nih.gov/35950146/)).

### Finding 9 — Diagnosis

Diagnosis is clinicopathologic with exclusion of mimics. Nofal et al. proposed a two-tier framework: *"We propose two sets of diagnostic criteria... The first comprises constant clinical and histopathological features that are always present in every case, the combination of which is necessary for diagnosis. The second set includes variable features that may be present in some cases"* ([PMID: 26695875](https://pubmed.ncbi.nlm.nih.gov/26695875/)). Characteristic histology/IHC: *"histopathology, which revealed interface dermatitis, intraepidermal vesiculation, and erythrocyte extravasation. Immunohistochemistry revealed perivascular T-cell infiltration"* ([PMID: 40560064](https://pubmed.ncbi.nlm.nih.gov/40560064/)). Supportive labs: leukocytosis/leukopenia, thrombocytopenia, elevated inflammatory markers, elevated serum TNF-α, frequent positive cultures, plus a **TCR clonality assay** for prognosis. **Genetic/newborn/carrier testing is not applicable.** Differential diagnosis: PLEVA, lymphomatoid papulosis, CTCL, SJS/TEN, erythema multiforme, Kawasaki disease, varicella, vasculitis, ecthyma.

### Finding 10 — Treatment

No RCTs exist; therapy is empirical and multimodal: *"Successful treatment modalities for FUMHD included antibiotics, antivirals, systemic steroids, Methotrexate (MTX), cyclophosphamide, Cyclosporine (CYA), Intravenous Immunoglobulins (IVIG), pentoxifylline, and ultraviolet B phototherapy"* ([PMID: 36483219](https://pubmed.ncbi.nlm.nih.gov/36483219/)). Methotrexate + antibiotics produced rapid improvement ([PMID: 26584702](https://pubmed.ncbi.nlm.nih.gov/26584702/)); IVIG can control refractory disease as a single infusion — *"who improved rapidly and achieved disease control with just a single infusion of low-dose intravenous immunoglobulin"* ([PMID: 38234081](https://pubmed.ncbi.nlm.nih.gov/38234081/)). Consistent with the TNF-α mechanism, TNF-α inhibitors help refractory cases — *"TNFα inhibitors may be useful, particularly in resistant cases"* ([PMID: 23391565](https://pubmed.ncbi.nlm.nih.gov/23391565/)) — with complete resolution reported ([PMID: 26790133](https://pubmed.ncbi.nlm.nih.gov/26790133/)); however an infant treated with a TNF-α inhibitor still died ([PMID: 42178566](https://pubmed.ncbi.nlm.nih.gov/42178566/)). Anti-CD25 basiliximab helped a FUMHD-like eruption with clonal T-ALL ([PMID: 28884915](https://pubmed.ncbi.nlm.nih.gov/28884915/)). Aggressive wound care and infection control are outcome-determining, and immunosuppression must be *"balanced against the mortality risk, as infectious complications are a frequent cause of death"* ([PMID: 34287852](https://pubmed.ncbi.nlm.nih.gov/34287852/)).

**Suggested MAXO terms:** glucocorticoid therapy, methotrexate/antimetabolite therapy, immunoglobulin therapy (IVIG), antimicrobial therapy, TNF inhibitor/biologic therapy, phototherapy (UVB), wound care.

### Finding 11 — Temporal development

Onset is acute/subacute across all ages (youngest reported 15 months — *"This report presents the youngest known pediatric case of fatal FUMHD"*, [PMID: 42178566](https://pubmed.ncbi.nlm.nih.gov/42178566/) — through adults and pregnancy). It often evolves from classic PLEVA within ~1–3 weeks: *"Three weeks later, his skin lesions started to ulcerate progressively, involving > 90% of his body surface, accompanied by high fever"* ([PMID: 15840118](https://pubmed.ncbi.nlm.nih.gov/15840118/)). The course is rapidly progressive and potentially fatal untreated, but most patients (especially children) resolve over weeks–months with treatment, healing with varioliform scars; a minority relapse or evolve toward lymphoproliferative disease. **No inheritance pattern** — sporadic and non-familial.

### Finding 12 — Genetics, model organisms, and other species (not applicable)

There are **no causal genes, pathogenic germline variants, chromosomal abnormalities, GWAS loci, or heritable susceptibility alleles** for FUMHD. The only molecular abnormality of significance is a **somatically acquired clonal TCR rearrangement** in skin-infiltrating lymphocytes of a subset. **No animal model** (knockout/transgenic/induced) recapitulates FUMHD, and **no naturally occurring animal equivalent** exists (no OMIA entry) — it is a human-only (NCBITaxon:9606) disease. The nearest in-vivo correlate is FUMHD-like ulceronecrotic disease arising with clonal T-ALL cells ([PMID: 28884915](https://pubmed.ncbi.nlm.nih.gov/28884915/)) — an observation, not a model. Epigenetic, omics, veterinary, and orthologous-gene sections are **not applicable**.

### Finding 13 — Prognosis synthesis

Case-fatality ~12–20% is strongly age-dependent (children ~2% vs. adults ~20%), with the leading cause of death being sepsis of denuded skin and multi-organ failure (DIC, ARDS, CNS). Prognostic factors: adult age, sepsis, systemic involvement, monoclonal TCR. Survivors heal with varioliform scars and dyspigmentation; a subset relapse or progress toward CTCL. No formal 5-/10-year survival statistics exist (rare disease).

### Finding 14 — Prevention

Because FUMHD is sporadic, non-genetic, and of unknown etiology with no modifiable exposure, **no primary prevention** applies. Prevention is secondary (early recognition + prompt therapy) and tertiary (prevent superinfection/sepsis via wound care, barrier protection, surveillance cultures, timely antimicrobials): management centers on *"prevention and care of skin injuries and complications"* ([PMID: 38715678](https://pubmed.ncbi.nlm.nih.gov/38715678/)). Immunization, public-health/environmental interventions, and genetic counseling are not relevant.

### Finding 15 — Integrated synthesis

Integrating all findings yields a coherent staged model (below): an infectious/antigenic or hypersensitivity trigger initiates a dysregulated cytotoxic CD8⁺ T-cell response; elevated TNF-α amplifies keratinocyte apoptosis, driving PLEVA→FUMHD; a subset acquires monoclonal TCR clonality (CTCL continuum, worse prognosis); and skin-barrier failure produces the lethal sepsis/multi-organ node. This explains why TNF-α blockade and immunomodulation work while infection control is simultaneously critical ([PMID: 15840118](https://pubmed.ncbi.nlm.nih.gov/15840118/); [PMID: 36483219](https://pubmed.ncbi.nlm.nih.gov/36483219/)).

---

## Mechanistic Model / Interpretation

```
   [Trigger]                 [Immune dysregulation]             [Amplification]              [Systemic failure]
 Infection / antigen  →   Dysregulated cytotoxic CD8+   →   Elevated serum TNF-α    →   Skin-barrier failure →
 (EBV, HSV-2,             T-cell response:                  amplifies keratinocyte     superinfection / SEPSIS,
 Toxoplasma, HIV,         interface dermatitis,             apoptosis; drives          DIC, pulmonary/ARDS,
 Mycoplasma) OR           keratinocyte necrosis,            PLEVA → FUMHD              CNS, HLH, multi-organ
 hypersensitivity         lymphocytic vasculitis            transition                 failure  →  DEATH (12–20%)
                                   │
                                   └── subset: somatic monoclonal TCR rearrangement
                                        → continuum with cutaneous T-cell lymphoma (CTCL)
                                        → worse prognosis
```

**Upstream vs. downstream.** The trigger and cytotoxic CD8⁺ T-cell response are **upstream**. TNF-α–driven keratinocyte apoptosis is the **key amplifier** converting limited PLEVA into confluent ulceronecrosis. The **downstream, lethal** events are barrier failure → sepsis, DIC, and multi-organ dysfunction. The clonal-TCR arm is a parallel modifier shifting a subset toward a lymphoproliferative phenotype and worse outcomes. This dual structure explains the therapeutic tension: immunosuppression targets the upstream/amplification nodes while antibiotics and wound care address the downstream node — and over-immunosuppression heightens the very sepsis risk that most often kills.

| Model node | Evidence | Key PMIDs |
|---|---|---|
| Infectious/antigenic trigger | EBV/Toxoplasma/HIV; HSV-2; *Mycoplasma*; 60.3% preceding infection in pediatric PL | 12894107, 19103367, 20465660 |
| Cytotoxic CD8⁺ T-cell / vasculitis | Atypical CD8⁺ infiltrate, interface dermatitis, lymphomatoid vasculitis | 38457671, 40560064 |
| TNF-α amplification | Elevated serum TNF-α at PLEVA→FUMHD transition; normal CRP | 15840118 |
| Clonal TCR / CTCL continuum | Monoclonal T-cell population; worse prognosis | 15583604, 36483219 |
| Sepsis / multi-organ failure | Sepsis LR 24.97; DIC/pulmonary/cardiac/GI/CNS; HLH | 34287852, 38959922, 38457671 |

### Anatomical involvement (ontology mapping)

- **Primary organ:** skin (UBERON:0002097) — epidermis (UBERON:0001003), dermis (UBERON:0002067); epithelial + connective tissue with superficial dermal vasculitis.
- **Secondary/multi-organ:** lung (UBERON:0002048), heart (UBERON:0000948), GI tract (UBERON:0000160), brain/CNS (UBERON:0000955), blood/coagulation system, reticuloendothelial/immune system (HLH); mucous membranes may be involved.
- **Cells:** keratinocytes (CL:0000312, target of necrosis), CD8⁺ cytotoxic T lymphocytes (CL:0000625), dermal microvascular endothelium.
- **Localization/lateralization:** generalized, bilateral and symmetric; trunk and flexural extremities predominate, often facial/acral.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|---|---|---|
| [34287852](https://pubmed.ncbi.nlm.nih.gov/34287852/) | Mucha-Habermann disease: pediatric case + risk score | Largest review (119 cases); mortality, LR risk factors, risk score |
| [36483219](https://pubmed.ncbi.nlm.nih.gov/36483219/) | Mortality risk factors: systematic review | 68-patient review; treatment modalities; clonal-TCR prognosis |
| [35950146](https://pubmed.ncbi.nlm.nih.gov/35950146/) | Case report + systematic review | Phenotype frequencies (sex, fever, cultures); adult death OR |
| [38959922](https://pubmed.ncbi.nlm.nih.gov/38959922/) | Case + treatment review | Core definition; systemic organ involvement |
| [15583604](https://pubmed.ncbi.nlm.nih.gov/15583604/) | FUMHD with clonality: a CTCL entity? | Monoclonal T cells; CTCL continuum |
| [15840118](https://pubmed.ncbi.nlm.nih.gov/15840118/) | PLEVA→FUMHD transition + TNF-α | TNF-α as pathogenic driver |
| [38457671](https://pubmed.ncbi.nlm.nih.gov/38457671/) | FUMHD with HLH | CD8⁺ immunophenotype; HLH complication |
| [26695875](https://pubmed.ncbi.nlm.nih.gov/26695875/) | Proposed diagnostic criteria | Constant vs. variable criteria framework |
| [40560064](https://pubmed.ncbi.nlm.nih.gov/40560064/) | 22-month-old case | Histopathologic/IHC diagnostic features |
| [20465660](https://pubmed.ncbi.nlm.nih.gov/20465660/) | PLEVA disease spectrum | Three etiologic hypotheses |
| [12894107](https://pubmed.ncbi.nlm.nih.gov/12894107/) | Infectious causes of PL | Principal infectious triggers |
| [19103367](https://pubmed.ncbi.nlm.nih.gov/19103367/) | FUMHD with HSV-2 | HSV-2 trigger; clonality as prognostic marker |
| [23391565](https://pubmed.ncbi.nlm.nih.gov/23391565/) | Infliximab + IVIG | First TNF-α inhibitor use in FUMHD |
| [38234081](https://pubmed.ncbi.nlm.nih.gov/38234081/) | IVIG in a child | IVIG efficacy in refractory pediatric FUMHD |
| [26584702](https://pubmed.ncbi.nlm.nih.gov/26584702/) | Two cases responsive to MTX | Methotrexate + antibiotics efficacy |
| [28884915](https://pubmed.ncbi.nlm.nih.gov/28884915/) | FUMHD-like disease in T-ALL | Basiliximab; clonal-leukemia link |
| [36686043](https://pubmed.ncbi.nlm.nih.gov/36686043/) | De novo FUMHD, fatal pulmonary | Fatal ARDS; no established criteria |
| [42178566](https://pubmed.ncbi.nlm.nih.gov/42178566/) | Fatal pediatric case | Youngest fatal case; TNF-inhibitor failure |
| [38715678](https://pubmed.ncbi.nlm.nih.gov/38715678/) | Case report | Prevention/care of skin injuries |
| [31814284](https://pubmed.ncbi.nlm.nih.gov/31814284/) | FUMHD mimicking Kawasaki | Differential diagnosis |

Supporting/contextual literature includes pediatric PL cohorts confirming male predominance, seasonality, and non-progression of childhood PL to mycosis fungoides ([PMID: 42152620](https://pubmed.ncbi.nlm.nih.gov/42152620/), [PMID: 41420620](https://pubmed.ncbi.nlm.nih.gov/41420620/)), and a review positioning FUMHD as a complication of the acute PL form ([PMID: 27144956](https://pubmed.ncbi.nlm.nih.gov/27144956/)).

**A note of tension:** The two large systematic reviews disagree on whether **mucosal involvement** independently affects mortality — significant in Blohm et al. ([PMID: 34287852](https://pubmed.ncbi.nlm.nih.gov/34287852/); LR 4.58, P=0.032) but not in Tasouli-Drakou et al. ([PMID: 36483219](https://pubmed.ncbi.nlm.nih.gov/36483219/)). This should be interpreted cautiously given small numbers and heterogeneous reporting.

---

## Supported vs. Refuted Hypotheses

**Supported:**
- FUMHD is a fulminant, potentially fatal PLEVA variant (multiple reviews).
- Pathogenesis is cytotoxic-T-cell–mediated with elevated TNF-α; a subset is clonal/CTCL-like.
- Mortality is age-dependent and driven by sepsis and systemic involvement.
- Multimodal immunosuppression + infection control is the mainstay; TNF-α inhibitors help refractory cases.

**Refuted / Not applicable:**
- A Mendelian/genetic cause (no causal gene; no OMIM).
- Existence of animal models or natural animal disease.
- Availability of omics datasets, formal incidence/prevalence, or RCT-grade treatment evidence.
- A consistent effect of mucosal involvement on mortality (contradictory between reviews).

---

## Limitations and Knowledge Gaps

1. **Evidence quality.** The literature is composed entirely of case reports and case-series-based systematic reviews — substantial publication/selection bias (severe and fatal cases and treatment "successes" preferentially reported), heterogeneous reporting, and short follow-up.
2. **Unknown etiology.** The precise trigger and the host factors determining why only rare individuals progress from PLEVA to FUMHD remain undefined.
3. **Mechanistic depth.** The TNF-α / cytotoxic CD8⁺ model rests on limited biomarker and IHC data; no transcriptomic, proteomic, single-cell, or spatial profiling of FUMHD lesions exists, and TNF-α causality is inferred.
4. **Clonality significance.** Whether monoclonal TCR marks a distinct CTCL subset or a transient reactive clone is unresolved; TCR-PCR data exist for only a handful of cases.
5. **No animal model** precludes controlled mechanistic and therapeutic experimentation.
6. **Diagnostic heterogeneity.** Absence of universally adopted criteria affects case ascertainment and reported frequencies/mortality.
7. **Ontology IDs** (MONDO/ICD/MeSH) should be verified against current releases.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international FUMHD registry** with standardized capture (Nofal criteria, systemic involvement, cultures, TCR clonality, treatments, long-term outcomes) to move beyond isolated case reports and prospectively validate the Blohm mortality risk score.
2. **Longitudinal biomarker profiling** of serum and lesional tissue (TNF-α, IL-2, IFN-γ) across the PLEVA→FUMHD transition to test the TNF-α amplification hypothesis and find progression-predictive markers.
3. **Single-cell and spatial transcriptomics** of lesional skin to characterize the cytotoxic infiltrate, clonal architecture, and keratinocyte/endothelial injury programs, distinguishing reactive from neoplastic clones.
4. **Systematic high-throughput TCR clonality analysis** across a case series to quantify prevalence and prognostic weight of monoclonality and its relationship to CTCL evolution.
5. **Structured infectious-trigger workup** (EBV, HSV-2, *Toxoplasma*, HIV, *Mycoplasma*) applied uniformly at presentation to quantify trigger frequency.
6. **Individual-patient-data meta-analysis** of treatment outcomes to estimate the relative effect of TNF-α inhibitors, IVIG, methotrexate, and corticosteroids while adjusting for severity and the competing risk of sepsis.
7. **Consensus diagnostic-criteria adoption** — validate and operationalize the Nofal framework across centers to harmonize case ascertainment.

---

*Report compiled from 15 confirmed findings across 5 investigation iterations and 41 reviewed papers. Evidence source type: predominantly human clinical (case reports and case-series systematic reviews); no model-organism, in-vitro, or computational primary data exist for this disease.*


## Artifacts

- [OpenScientist final report](Febrile_Ulceronecrotic_Mucha-Habermann_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Febrile_Ulceronecrotic_Mucha-Habermann_Disease-deep-research-openscientist_artifacts/final_report.pdf)