---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-02T21:49:54.962288'
end_time: '2026-11-02T22:04:01.482422'
duration_seconds: 846.52
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Lassa Fever
  mondo_id: MONDO:0005820
  category: Infectious
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: LF; Lassa hemorrhagic fever
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
citation_count: 40
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Lassa_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Lassa_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lassa Fever
- **MONDO ID:** MONDO:0005820 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** LF; Lassa hemorrhagic fever
- **Category:** Infectious

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Lassa Fever** covering all of the
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

# Lassa Fever (MONDO:0005820): A Comprehensive Disease Characteristics Report

**MONDO:** MONDO:0005820 · **Category:** Infectious (viral hemorrhagic fever) · **Causal agent:** *Lassa mammarenavirus* (LASV)

> **Note on "causal gene."** Lassa fever is an **infectious disease**, not a Mendelian/genetic disorder, so there is **no human causal gene**. The causal factor is the **Lassa virus (Lassa mammarenavirus, LASV)**, a bisegmented ambisense RNA arenavirus. Where "genes" are relevant, they are (a) **viral genes** — *GPC* (glycoprotein precursor), *NP* (nucleoprotein), *L* (RNA-dependent RNA polymerase), *Z* (matrix protein); and (b) **host susceptibility/resistance loci** under natural selection in West Africans — **LARGE1** (HGNC:6511) and **IL21** (HGNC:6005), plus the viral entry receptor genes **DAG1** (α-dystroglycan) and **LAMP1**. These are modifiers, not Mendelian causes.

## Summary

**Lassa fever (LF) is an acute zoonotic viral hemorrhagic fever caused by Lassa mammarenavirus (LASV; family *Arenaviridae*, genus *Mammarenavirus*).** The reservoir host is the synanthropic rodent *Mastomys natalensis* (Natal multimammate mouse), and humans are infected mainly through rodent-to-human transmission. The disease is endemic to West Africa (Nigeria, Sierra Leone, Liberia, Guinea, Benin, and neighboring countries). Where host genetics matter, they act as *modifiers of susceptibility/resistance*: the genes **LARGE** (a glycosyltransferase that builds the α-dystroglycan matriglycan used as the viral entry receptor) and **IL21** show genome-wide signatures of positive selection in West African populations, implying partial host-genetic resistance to Lassa fever.

Clinically, LASV causes a spectrum from asymptomatic/mild infection (~80%) to severe multisystem hemorrhagic disease with hepatic and renal involvement, facial/laryngeal edema, shock, encephalopathy, and death. Hospitalized case fatality ranges from ~15% (mild) to 60% (severe), with recent Nigerian outbreaks reporting up to 25.4%. Modeling now projects ~2.7 million infections and ~3,900 deaths annually across West Africa. The hallmark chronic sequela is **sensorineural hearing loss (SNHL)**, affecting roughly 18–33% of survivors, now understood to be an immune-mediated systemic vasculitis of the inner ear rather than direct viral cytopathology. Pregnancy — especially the third trimester — carries extremely high maternal (up to 30%) and fetal (~87% loss) mortality.

Mechanistically, LASV enters cells via a two-receptor switch (primary receptor **α-dystroglycan → endosomal LAMP1**) followed by pH-dependent, GPC-mediated membrane fusion; the matrix Z protein and stable signal peptide require host **N-myristoyltransferases (NMT1/2)** for budding and fusion. Unlike New World arenaviruses, Old World LASV produces **generalized immune suppression** (nucleoprotein-mediated interferon antagonism, myeloid-suppressor-cell expansion, T-cell anergy), systemic viral dissemination, and endothelial/vascular dysfunction. There is **no licensed vaccine** more than five decades after discovery (Nigeria, 1969), though multiple GPC-targeted candidates are in clinical/preclinical development. Standard of care is **ribavirin** (limited efficacy, notable toxicity), with **favipiravir** emerging as a promising alternative.

---

## Key Findings

### Finding 1 — Lassa fever is a high-burden zoonotic arenaviral hemorrhagic fever endemic to West Africa

Lassa fever is caused by Lassa mammarenavirus, an enveloped, bisegmented, ambisense RNA virus. Contemporary modeling projects approximately **2.7 million LASV infections each year** across West Africa, with an estimated **3,900 deaths and 2.0 million disability-adjusted life years (DALYs) over a decade** ([PMID: 42365235](https://pubmed.ncbi.nlm.nih.gov/42365235/)). Earlier widely cited estimates placed the burden at up to 300,000 infections and 5,000 deaths per year ([PMID: 32155851](https://pubmed.ncbi.nlm.nih.gov/32155851/)). Case fatality ranges from **15% in mild cases to 60% in severe cases**, with recent Nigerian outbreaks reaching **25.4%** in hospitalized patients ([PMID: 40597771](https://pubmed.ncbi.nlm.nih.gov/40597771/); [PMID: 32155851](https://pubmed.ncbi.nlm.nih.gov/32155851/)).

The reservoir is the synanthropic rodent *Mastomys natalensis*: *"Human infections arise from rodent-to-human transmission, primarily from the synanthropic reservoir Mastomys natalensis"* ([PMID: 42049016](https://pubmed.ncbi.nlm.nih.gov/42049016/)). Community seroprevalence reaches ~5.7% in endemic parts of Sierra Leone.

- **Ontology/identifiers:** MONDO:0005820; MeSH D007835 (Lassa Fever); ICD-10 A96.2; ICD-11 1D61; pathogen NCBI Taxon **3052310** (Lassa mammarenavirus).

### Finding 2 — Sensorineural hearing loss is the most common chronic sequela

A systematic review/meta-analysis found that *"The most frequently reported post-acute sequela was hearing loss, with a pooled prevalence of 18% (95% CI 9–32) across 6 studies"* ([PMID: 41912095](https://pubmed.ncbi.nlm.nih.gov/41912095/)). A scoping review reported hearing loss in **16–35% of survivors**, often bilateral and sensorineural with balance disorders in up to 55% ([PMID: 40597771](https://pubmed.ncbi.nlm.nih.gov/40597771/)). The commonly cited frequency is ~33%: *"A notable sequela of LF is sensorineural hearing loss (SNHL) that can develop in about 33% of the patients"* ([PMID: 35758052](https://pubmed.ncbi.nlm.nih.gov/35758052/)). SNHL can occur even at low viral load (high PCR Ct value) and may progress from unilateral to bilateral involvement ([PMID: 41458264](https://pubmed.ncbi.nlm.nih.gov/41458264/)).

- **Suggested HPO terms:** HP:0000407 (Sensorineural hearing impairment); HP:0000408 (Progressive sensorineural hearing impairment); HP:0001251 (Ataxia/balance); HP:0001250 (Seizure); HP:0001268 (Mental deterioration).

### Finding 3 — Ribavirin is standard of care but limited; favipiravir is an emerging alternative

*"At present, ribavirin is the only antiviral drug indicated for use in treatment of these diseases, but because of its limited efficacy in advanced cases of disease and its toxicity, safer and more effective antivirals are needed"* ([PMID: 22022624](https://pubmed.ncbi.nlm.nih.gov/22022624/)). Favipiravir (T-705), a broad-spectrum RNA-polymerase inhibitor, cured Lassa-viremic macaques at 300 mg/kg/day for two weeks: *"We tested favipiravir in Lassa virus-viremic macaques and found that 300 mg/kg daily for 2 weeks successfully treated infection"* ([PMID: 29882740](https://pubmed.ncbi.nlm.nih.gov/29882740/)). A Phase 2 open-label RCT in Nigeria (n=41; ribavirin 21 vs favipiravir 20) met its pharmacokinetic/safety primary endpoints, supporting high-dose favipiravir as a treatment alternative ([PMID: 42141199](https://pubmed.ncbi.nlm.nih.gov/42141199/)).

- **Suggested NCIT terms:** C29460 (Ribavirin); C81668 (Favipiravir); C15245 (Supportive Care).

### Finding 4 — LARGE and IL21 show positive selection in West Africans (host genetic resistance)

Genome-wide scans (HapMap, 1000 Genomes) revealed *"evidence for positive selection in LARGE and interleukin 21 (IL21), two genes implicated in LASV infectivity and immunity"* ([PMID: 22312054](https://pubmed.ncbi.nlm.nih.gov/22312054/)). LARGE encodes a glycosyltransferase that builds the matriglycan on α-dystroglycan — the primary LASV entry receptor — so variation affecting its expression plausibly alters viral entry. This has been framed as host resistance: *"natural selection acting on LARGE—detected in the Yoruba population of Nigeria—conferred resistance to Lassa Fever in some West African populations"* ([PMID: 34452470](https://pubmed.ncbi.nlm.nih.gov/34452470/)).

- **Gene annotations:** LARGE1 (HGNC:6511; NCBI Gene 9215); IL21 (HGNC:6005; NCBI Gene 59067); DAG1/α-dystroglycan (HGNC:2666).

### Finding 5 — LASV entry uses a two-receptor switch and GPC-mediated fusion; immunosuppression drives severity

LASV's glycoprotein precursor GPC is processed into a stable signal peptide (SSP), GP1, and GP2, forming trimeric spikes ([PMID: 39339839](https://pubmed.ncbi.nlm.nih.gov/39339839/)). Entry requires a receptor switch: *"Successful entry of LASV requires the viral glycoprotein 1 (GP1) to undergo a receptor switch from its primary receptor alpha-dystroglycan (α-DG) to its endosomal receptor lysosome-associated membrane protein 1 (LAMP1)"* ([PMID: 38851430](https://pubmed.ncbi.nlm.nih.gov/38851430/)). A conserved histidine triad plus residues L84/K88/L107/H170 govern the pH-dependent switch. The Z matrix protein and SSP require host N-myristoyltransferases (NMT1/2) for budding and fusion — a druggable target ([PMID: 39339839](https://pubmed.ncbi.nlm.nih.gov/39339839/)).

Unlike New World Junín virus (which drives a cytokine storm), Old World LASV causes *"an overall generalized immune suppression"* ([PMID: 24068704](https://pubmed.ncbi.nlm.nih.gov/24068704/)). Fatal disease features systemic dissemination, macrophage/neutrophil infiltration, and excessive inflammation, whereas severity is *"associated with the expansion of suppressive myeloid cells, alterations of the stromal network of secondary lymphoid organs, and the anergy of specific T cells"* ([PMID: 40245043](https://pubmed.ncbi.nlm.nih.gov/40245043/); [PMID: 39652618](https://pubmed.ncbi.nlm.nih.gov/39652618/)).

- **Suggested GO terms:** GO:0019062 (virion attachment to host cell); GO:0075509 (receptor-mediated endocytosis of virus by host cell); GO:0019064 (fusion of virus membrane with host plasma membrane); GO:0039503 (suppression of host innate immune response by virus). **CL terms:** CL:0000235 (macrophage); CL:0000775 (neutrophil); CL:0000084 (T cell); CL:0000889 (myeloid suppressor cell).

### Finding 6 — No licensed vaccine exists; multiple GPC-targeted candidates are in development

*"There is no licensed vaccine available more than five decades after its discovery, and current therapeutic practices rely heavily on ribavirin, a drug supported by limited and methodologically weak evidence"* ([PMID: 42254098](https://pubmed.ncbi.nlm.nih.gov/42254098/)). Candidates target the glycoprotein complex (GPC, Josiah strain). The inactivated rabies-virus-vectored **LASSARAB** completed a Phase 1 dose-escalation trial (n=54) with acceptable safety and no SNHL: *"We evaluated LASSARAB, an inactivated rabies virus-vectored Lassa virus (Josiah strain) glycoprotein complex vaccine"* ([PMID: 42265408](https://pubmed.ncbi.nlm.nih.gov/42265408/)). mRNA-LNP GPC vaccines protected guinea pigs even without neutralizing antibodies ([PMID: 37699929](https://pubmed.ncbi.nlm.nih.gov/37699929/)); a DNA vaccine delivered by dermal electroporation fully protected cynomolgus macaques ([PMID: 29045192](https://pubmed.ncbi.nlm.nih.gov/29045192/)). CEPI is standardizing neutralization assays (International Units) to accelerate development ([PMID: 42382775](https://pubmed.ncbi.nlm.nih.gov/42382775/)), and rational prefusion-stabilized GPC design aims to add neutralizing activity ([PMID: 40555565](https://pubmed.ncbi.nlm.nih.gov/40555565/)).

### Finding 7 — Lassa fever in pregnancy: very high maternal/fetal mortality; uterine evacuation improves maternal survival

In a prospective Sierra Leone study (68 pregnant, 79 non-pregnant), Lassa fever accounted for 25% of maternal deaths. Third-trimester mortality was elevated: *"The odds ratio for death in the third trimester compared with the first two trimesters was 5.57 (95% confidence intervals 1.02 to 30.26)"* and *"Fetal and neonatal loss was 87%"* ([PMID: 3139220](https://pubmed.ncbi.nlm.nih.gov/3139220/)). Uterine evacuation reduced maternal death (OR for death with pregnancy intact = 5.47; p=0.0016). A Southern Nigeria case-control study (43 cases, 170 controls) found Lassa fever in pregnancy sharply increased stillbirth (RR 18.7), premature delivery (RR 5.25), and low birth weight (RR 8.41) ([PMID: 42410380](https://pubmed.ncbi.nlm.nih.gov/42410380/)). Mechanistically, VHF viruses including LASV *"utilize ubiquitous cellular surface entry receptors critical for normal placental function"*, enabling maternal-fetal transmission and stillbirth ([PMID: 36939178](https://pubmed.ncbi.nlm.nih.gov/36939178/)).

### Finding 8 — RT-PCR is the diagnostic gold standard; antigen and serology are adjuncts

*"The diagnostic sensitivity and specificity of the IgM assay were 57% and 77% respectively"* versus RT-PCR in 37 confirmed cases, confirming the limited early sensitivity of serology ([PMID: 23661877](https://pubmed.ncbi.nlm.nih.gov/23661877/)). RT-PCR is the gold standard but is unavailable in most endemic centers. Rapid antigen tests address this gap: *"newly developed recombinant LASV Antigen Rapid Test cassettes and dipstick lateral flow immunoassays (LFI) that enabled the diagnosis of LF within twenty minutes of sample collection"* ([PMID: 21843352](https://pubmed.ncbi.nlm.nih.gov/21843352/)). A qualified anti-LASV-nucleoprotein IgG ELISA now detects prior exposure across LASV lineages I–IV ([PMID: 42391156](https://pubmed.ncbi.nlm.nih.gov/42391156/)). Diagnostics target the nucleoprotein (NP) and glycoprotein (GP) antigens.

- **Laboratory abnormalities:** HP:0002910 (elevated AST/hepatic transaminases), HP:0000083 (renal insufficiency), HP:0001873 (thrombocytopenia).

### Finding 9 — Spillover is driven by *Mastomys natalensis* ecology and climate

Human infection arises mainly from rodent-to-human transmission; LASV antigen prevalence reached **20% in peri-domestic rodents** in Sierra Leone: *"Of the 373 specimens tested, 74 (20%) were positive for LASV antigen"* ([PMID: 42002983](https://pubmed.ncbi.nlm.nih.gov/42002983/)). Climate drives this: *"temperature, rainfall, humidity, vegetation change and large-scale climatic oscillations all contribute to fluctuations in Mastomys natalensis populations which serve as the primary reservoir of Lassa virus"* ([PMID: 42891776](https://pubmed.ncbi.nlm.nih.gov/42891776/)). Socioeconomic ("housing") factors modulate urban spillover risk ([PMID: 42339572](https://pubmed.ncbi.nlm.nih.gov/42339572/)). Novel control concepts include CMV-vectored transmissible vaccines to immunize the rodent reservoir ([PMID: 42361202](https://pubmed.ncbi.nlm.nih.gov/42361202/)).

### Finding 10 — Lassa fever SNHL is immune-mediated systemic vasculitis of the inner ear

In cynomolgus macaques surviving acute LASV infection, profound SNHL developed during convalescence. *"Histologic examination of inner ear structures and other tissues revealed the presence of severe vascular lesions consistent with systemic vasculitides. These systemic immune-mediated vascular disorders have been associated with sudden hearing loss"* ([PMID: 30377282](https://pubmed.ncbi.nlm.nih.gov/30377282/)). The same study confirmed *"approximately 30% of patients develop sudden-onset sensorineural hearing loss after recovering from acute disease."* Consistent with an immune (not direct viral) mechanism, SNHL in ML29-infected STAT1−/− mice was independent of CD4/CD8 T cells ([PMID: 36289695](https://pubmed.ncbi.nlm.nih.gov/36289695/)), SNHL can occur at low viral load ([PMID: 41458264](https://pubmed.ncbi.nlm.nih.gov/41458264/)), and corticosteroid/osmotic therapy shows benefit in case reports.

- **Suggested UBERON/anatomy:** UBERON:0001690 (ear); UBERON:0001844 (cochlea); UBERON:0002227 (organ of Corti). HPO: HP:0000407.

### Finding 11 — Multiple animal models exist; cynomolgus macaques best recapitulate human disease

*"Cynomolgus macaques of non-Mauritius Asian origin best reproduce clinical features of human Lassa fever"* ([PMID: 40763738](https://pubmed.ncbi.nlm.nih.gov/40763738/)). Aerosol LASV in cynomolgus macaques produces multisystemic hemorrhagic disease; *"Immunoreactivity to LASV antigen was first observed in the lungs of one macaque on day 3 and appeared localized to macrophages"* before spreading to all organ systems ([PMID: 38404292](https://pubmed.ncbi.nlm.nih.gov/38404292/)). African green monkeys more consistently reproduce hemorrhagic manifestations ([PMID: 40763738](https://pubmed.ncbi.nlm.nih.gov/40763738/)). BSL-2-compatible surrogate models include Pichinde virus in Hartley guinea pigs (reproduces hemorrhagic fever and SNHL; [PMID: 35758052](https://pubmed.ncbi.nlm.nih.gov/35758052/)) and the ML29 reassortant in STAT1−/− mice ([PMID: 36289695](https://pubmed.ncbi.nlm.nih.gov/36289695/)). Guinea-pig-adapted LASV strains (LF2384) give lethal disease, and reverse genetics identified the L protein as a key virulence determinant ([PMID: 40579376](https://pubmed.ncbi.nlm.nih.gov/40579376/)).

### Finding 12 — Severe disease is multi-system with coagulation and metabolic dysregulation; metabolomic biomarkers predict outcome

Early features are non-specific (fever, malaise, sore throat, retrosternal/chest pain, weakness), progressing in severe cases to bleeding, facial/laryngeal edema, shock, encephalopathy, and multi-organ (hepatic, renal) failure ([PMID: 42365235](https://pubmed.ncbi.nlm.nih.gov/42365235/); [PMID: 21843352](https://pubmed.ncbi.nlm.nih.gov/21843352/)). Untargeted UHPLC-MS metabolomics of Sierra Leonean patients showed that *"Effects of LASV infection on pathways mediating blood coagulation, and lipid, amino acid, nucleic acid metabolism are manifest in changes in the levels of numerous metabolites"*, and that *"platelet activating factor (PAF), PAF-like molecules and products of heme breakdown emerged as candidates that may prove useful in diagnostic assays"* ([PMID: 28922385](https://pubmed.ncbi.nlm.nih.gov/28922385/)). High viremia and elevated AST are established markers of poor prognosis.

---

## Section-by-Section Narrative

### 1. Disease Information
Lassa fever is an acute viral hemorrhagic fever caused by Lassa mammarenavirus. It is a **disease-level, aggregated-resource** concept (not derived from a single EHR patient). Key identifiers: **MONDO:0005820**; **MeSH D007835**; **ICD-10 A96.2**; **ICD-11 1D61**; Orphanet ORPHA:99824. There is no OMIM entry because it is infectious, not Mendelian. Synonyms: LF; Lassa hemorrhagic fever; Lassa mammarenavirus infection.

### 2. Etiology
**Causal factor: infectious** — Lassa mammarenavirus (Arenaviridae). **Risk factors (environmental/behavioral):** residence in or travel to endemic West Africa; contact with *Mastomys natalensis* or its excreta; poor housing/food storage; rodent consumption; healthcare work (nosocomial exposure); pregnancy (especially third trimester). **Genetic susceptibility/resistance (host modifiers):** positive selection on **LARGE** and **IL21** in West Africans suggests resistance alleles (F004). **Gene–environment interaction:** LARGE builds the α-dystroglycan matriglycan that LASV exploits for entry, so host glycosylation genotype intersects directly with the environmental exposure (virus). No validated protective diet/lifestyle factor beyond exposure avoidance.

### 3. Phenotypes
| Phenotype | Type | Frequency | HPO | Onset/Course |
|---|---|---|---|---|
| Fever | Symptom | Very common | HP:0001945 | Acute (1–3 wk incubation) |
| Sore throat / pharyngitis | Sign | Common | HP:0025439 | Acute |
| Retrosternal/chest pain | Symptom | Common | HP:0100749 | Acute |
| Hemorrhage/bleeding | Sign | Severe cases | HP:0001892 | Progressive |
| Facial/laryngeal edema | Sign | Severe, poor prognosis | HP:0000316 | Progressive |
| Elevated AST | Lab | Prognostic | HP:0002910 | Acute |
| Proteinuria/renal failure | Lab/sign | Severe | HP:0000083 | Progressive |
| Encephalopathy/seizures | Sign | Severe | HP:0001250 | Progressive |
| Sensorineural hearing loss | Sign (sequela) | 18–33% survivors | HP:0000407 | Post-acute, often permanent |
| Spontaneous abortion/stillbirth | Outcome | Very high in pregnancy | HP:0200067/HP:0003561 | Acute |

### 4. Genetic/Molecular Information
**No human causal gene.** The *viral* genome is bisegmented ambisense RNA: the S segment encodes **nucleoprotein (NP)** and **glycoprotein precursor (GPC)**; the L segment encodes the **L polymerase** and **Z matrix protein**. Human host-genetic modifiers are **LARGE1** (HGNC:6511) and **IL21** (HGNC:6005), under positive selection (F004). Pathogenic viral "variants" are strain/lineage differences (lineages I–IV), with the L protein as a key virulence determinant (F011). No chromosomal abnormalities, somatic/germline variant classification, or epigenetic human-disease signatures apply in the Mendelian sense.

### 5. Environmental Information
The dominant environmental driver is **rodent reservoir ecology** governed by climate (temperature, rainfall, humidity, vegetation) that drives *Mastomys natalensis* population dynamics and seasonal spillover (F009). Transmission routes: contact with rodent excreta on food/surfaces; aerosolization during cleaning; consumption of rodents; nosocomial/person-to-person in outbreaks. **Infectious agent:** Lassa mammarenavirus, NCBI Taxon 3052310.

### 6. Mechanism / Pathophysiology — Ordered Causal Chain

```
1. Exposure to Mastomys natalensis excreta / aerosol
       → LASV virions contact host mucosa / dendritic cells & macrophages (first targets)
2. GP1 binds primary receptor alpha-dystroglycan (matriglycan built by LARGE)
       → receptor-mediated endocytosis
3. Endosomal acidification triggers GP1 RECEPTOR SWITCH to LAMP1
       (histidine triad + L84/K88/L107/H170)
       → GP2-mediated, pH-dependent membrane fusion  [demonstrated, PMID 38851430]
4. Genome release, replication; Z protein + SSP myristoylated by host NMT1/2
       → virion assembly and budding  [demonstrated, PMID 39339839]
5. NP exonuclease antagonizes RIG-I / type-I interferon
       → GENERALIZED IMMUNE SUPPRESSION  [PMID 24068704]
   |-- Branch A (survival): LASV-specific T-cell response controls virus,
   |        dissemination limited to lymphoid organs  [PMID 39652618]
   |-- Branch B (fatal): expansion of suppressive myeloid cells + T-cell anergy
            → systemic dissemination to all organs
            → macrophage / neutrophil infiltration + excessive inflammation
            → endothelial dysfunction, vascular leak, coagulopathy (up PAF, heme breakdown)
            → shock, multi-organ (hepatic/renal) failure, death  [PMID 40245043, 28922385]
6. POST-ACUTE BRANCH (survivors): immune-mediated systemic vasculitis
       → inner-ear vascular lesions
       → sudden sensorineural hearing loss (~30%)  [inferred from histology, PMID 30377282]
```

- **Molecular pathways:** receptor-mediated endocytosis; type-I IFN/RIG-I antagonism; NMT-dependent myristoylation (druggable). **Cellular processes:** macrophage/dendritic-cell infection, myeloid-suppressor expansion, T-cell anergy, endothelial dysfunction, inflammation. **Metabolic changes:** dysregulated coagulation, lipid/amino-acid/nucleic-acid metabolism, PAF and heme-breakdown accumulation (F012). **Tissue damage:** vascular leak, hepatic necrosis, inner-ear vasculitis. Upstream = viral entry + IFN suppression; downstream = systemic inflammation, organ failure, and post-infectious vasculitic SNHL.

### 7. Anatomical Structures Affected
**Primary organs:** liver (hepatitis, ↑AST; UBERON:0002107), spleen/lymphoid organs (early replication reservoir), vascular endothelium (UBERON:0001986). **Secondary:** kidney (UBERON:0002113), lungs (UBERON:0002048; early macrophage tropism), inner ear/cochlea (UBERON:0001844 — SNHL), placenta (UBERON:0001987 — fetal loss), CNS (encephalopathy). **Body systems:** cardiovascular, hepatic/digestive, renal, immune/lymphoid, auditory, reproductive. **Cell types (CL):** macrophages (CL:0000235), dendritic cells (CL:0000451), neutrophils (CL:0000775), T cells (CL:0000084), endothelial cells (CL:0000115), trophoblasts (CL:0000351). **Lateralization:** SNHL may be unilateral or bilateral.

### 8. Temporal Development
**Onset:** acute, after a 1–3 week (6–21 day) incubation; affects all ages. **Progression:** non-specific febrile prodrome → multisystem severe disease over 1–2 weeks in fatal cases; death typically within 2 weeks of onset. **Duration:** self-limited in most; severe disease rapidly progressive. **Patterns:** survivors recover acutely but may develop SNHL in convalescence (a distinct post-infectious window; F010). **Critical period:** early antiviral initiation (within the first ~6 days) and, in pregnancy, prompt uterine evacuation improve survival (F003, F007).

### 9. Inheritance and Population
**Not inherited** (infectious). **Epidemiology:** ~2.7 million infections and ~3,900 deaths/year across West Africa; endemic in Nigeria, Sierra Leone, Liberia, Guinea, Benin (F001). Community seroprevalence ~5.7% (Sierra Leone). **Geographic distribution of viral variants:** lineages I–III in Nigeria, lineage IV in Sierra Leone/Guinea/Liberia. **Host genetics:** signatures of selection in West African populations (LARGE, IL21). **Sex/age:** both sexes; pregnancy markedly worsens outcome. No founder effects, penetrance, or carrier-frequency concepts apply (non-Mendelian).

### 10. Diagnostics
**Gold standard:** LASV RT-PCR (F008). **Antigen detection:** rapid NP lateral-flow tests (~20 min). **Serology:** IgM/IgG ELISA (IgM sensitivity only 57% early) — better for exposure surveillance; qualified anti-NP IgG ELISA covers lineages I–IV. **Supportive labs:** elevated AST (prognostic), thrombocytopenia, proteinuria, renal impairment. **Differential diagnosis:** malaria, typhoid, other VHFs (Ebola, Marburg, CCHF, yellow fever), leptospirosis, severe bacterial sepsis. **Prognostic markers:** high viremia, high AST, bleeding, and metabolomic signatures (PAF, heme breakdown).

### 11. Outcome / Prognosis
**Mortality:** 15–60% case fatality depending on severity; up to ~25% in recent hospitalized outbreaks (F001). **Prognostic factors:** viremia level, AST, bleeding, facial/laryngeal edema, third-trimester pregnancy. **Morbidity:** chronic SNHL (18–33%), balance disorders (~55% of those with hearing loss), neurological sequelae (paraparesis, seizures, cognitive impairment), ophthalmic manifestations (~42% in one study), depression/delirium (F002, F010, [PMID: 40597771](https://pubmed.ncbi.nlm.nih.gov/40597771/)). **Recovery:** acute survival is common with supportive care; SNHL is frequently permanent.

### 12. Treatment
**Pharmacotherapy:** ribavirin (standard, limited efficacy/toxicity; NCIT C29460); high-dose favipiravir (emerging; NCIT C81668). **Supportive/interventional:** fluid/electrolyte management, treatment of shock and bleeding, renal support; **uterine evacuation** improves maternal survival in pregnancy (F007). **Experimental/advanced:** monoclonal-antibody cocktails and passive neutralization under study; entry inhibitors (e.g., hexestrol) and NMT inhibitors (DDD85646) show preclinical promise. **Pharmacogenomics:** none established. For SNHL, corticosteroid/osmotic therapy shows benefit in case reports.

### 13. Prevention
**Primary:** rodent control, safe food storage, improved housing, community education; infection-prevention and barrier nursing to prevent nosocomial spread. **Secondary:** early diagnosis (RT-PCR/antigen) and prompt antiviral therapy; hearing assessment in survivors. **Immunization:** no licensed vaccine; GPC-targeted candidates (LASSARAB, mRNA-LNP, DNA, viral-vectored) in trials (F006). **Novel:** CMV-vectored transmissible vaccines to immunize the rodent reservoir (F009). **Prophylaxis:** post-exposure ribavirin considered for high-risk contacts.

### 14. Other Species / Natural Disease
**Reservoir:** *Mastomys natalensis* (NCBI Taxon 10112) — asymptomatic persistent carrier. Other rodent species may contribute. **Zoonotic potential:** high (rodent-to-human). **Experimental cross-species susceptibility:** non-human primates (cynomolgus macaque *Macaca fascicularis* NCBI Taxon 9541; African green monkey *Chlorocebus* spp.), guinea pigs (*Cavia porcellus* NCBI Taxon 10141), and mice. **Orthologs:** LARGE1 and IL21 orthologs exist across mammals. No major companion-animal natural disease is documented.

### 15. Model Organisms
| Model | System | Recapitulation | Key use | PMID |
|---|---|---|---|---|
| Cynomolgus macaque | NHP (BSL-4) | Best — full human-like LF | Pathogenesis, vaccines, antivirals | [40763738](https://pubmed.ncbi.nlm.nih.gov/40763738/), [38404292](https://pubmed.ncbi.nlm.nih.gov/38404292/) |
| African green monkey | NHP (BSL-4) | Hemorrhagic manifestations | Alternative NHP | [40763738](https://pubmed.ncbi.nlm.nih.gov/40763738/) |
| Hartley guinea pig + Pichinde virus | Rodent (BSL-2) | Hemorrhagic fever + SNHL | Surrogate; SNHL studies | [35758052](https://pubmed.ncbi.nlm.nih.gov/35758052/) |
| STAT1−/− mouse + ML29 | Rodent (BSL-2) | Acute disease + hearing loss | SNHL mechanism (T-cell independent) | [36289695](https://pubmed.ncbi.nlm.nih.gov/36289695/) |
| Guinea pig + LASV LF2384 | Rodent (BSL-4) | Lethal LF | Virulence determinants (L protein) | [40579376](https://pubmed.ncbi.nlm.nih.gov/40579376/) |

Models have been used to demonstrate favipiravir efficacy ([PMID: 29882740](https://pubmed.ncbi.nlm.nih.gov/29882740/)) and full DNA-vaccine protection in macaques ([PMID: 29045192](https://pubmed.ncbi.nlm.nih.gov/29045192/)). Limitation: no single small-animal model fully reproduces both lethal hemorrhagic disease and SNHL at BSL-2.

---

## Mechanistic Model / Interpretation

The coherent narrative is a **two-stage immunopathology**. In the **acute stage**, LASV exploits a widely expressed glycan (α-dystroglycan matriglycan) for entry, converts to LAMP1 in the endosome, fuses via GP2, and — crucially — its nucleoprotein suppresses type-I interferon. This produces a *generalized immunosuppression* that distinguishes Old World LASV from the cytokine-storm New World arenaviruses. Outcome is decided at a branch point: an early LASV-specific T-cell response limits virus to lymphoid tissue (survival), whereas failure leads to myeloid-suppressor-cell expansion, T-cell anergy, systemic dissemination, endothelial/coagulation dysfunction (reflected in PAF and heme-breakdown metabolites), multi-organ failure, and death.

In the **post-acute stage**, survivors face a separate immunopathological process: a systemic immune-mediated vasculitis that damages inner-ear vasculature, producing sudden SNHL in ~30%. The strongest support for an *immune*, rather than directly viral, mechanism is that (a) macaque histology shows vasculitic lesions, (b) murine SNHL is independent of CD4/CD8 T cells, (c) SNHL occurs at low viral loads, and (d) steroids help. This two-stage model explains why vaccines that protect without neutralizing antibody (via T cells/Fc effector function) are rational, and why early diagnosis plus antiviral therapy (ribavirin/favipiravir) targets the acute branch while anti-inflammatory therapy targets the sequela branch.

---

## Evidence Base (selected)

| PMID | Supports | Role |
|---|---|---|
| [42365235](https://pubmed.ncbi.nlm.nih.gov/42365235/) | F001, F012 | Current burden (~2.7M/yr); clinical spectrum |
| [41912095](https://pubmed.ncbi.nlm.nih.gov/41912095/) | F002 | Meta-analytic SNHL prevalence 18% |
| [30377282](https://pubmed.ncbi.nlm.nih.gov/30377282/) | F010 | Vasculitis mechanism of SNHL (macaque histology) |
| [38851430](https://pubmed.ncbi.nlm.nih.gov/38851430/) | F005 | α-DG → LAMP1 receptor switch |
| [24068704](https://pubmed.ncbi.nlm.nih.gov/24068704/) | F005 | Generalized immunosuppression (Old World) |
| [40245043](https://pubmed.ncbi.nlm.nih.gov/40245043/) | F005 | Myeloid-suppressor expansion, T-cell anergy |
| [22312054](https://pubmed.ncbi.nlm.nih.gov/22312054/) | F004 | Positive selection in LARGE, IL21 |
| [29882740](https://pubmed.ncbi.nlm.nih.gov/29882740/) | F003 | Favipiravir cures viremic macaques |
| [42141199](https://pubmed.ncbi.nlm.nih.gov/42141199/) | F003 | Phase 2 favipiravir RCT (Nigeria) |
| [42254098](https://pubmed.ncbi.nlm.nih.gov/42254098/) | F006 | No licensed vaccine; weak ribavirin evidence |
| [3139220](https://pubmed.ncbi.nlm.nih.gov/3139220/) | F007 | Third-trimester mortality, uterine evacuation |
| [23661877](https://pubmed.ncbi.nlm.nih.gov/23661877/) | F008 | IgM sensitivity 57% vs RT-PCR |
| [42891776](https://pubmed.ncbi.nlm.nih.gov/42891776/) | F009 | Climate–rodent–spillover interaction |
| [40763738](https://pubmed.ncbi.nlm.nih.gov/40763738/) | F011 | Cynomolgus macaque gold-standard model |
| [28922385](https://pubmed.ncbi.nlm.nih.gov/28922385/) | F012 | Metabolomic biomarkers (PAF, heme) |

---

## Limitations and Knowledge Gaps

1. **Burden uncertainty.** Infection is often asymptomatic and surveillance is weak; incidence/prevalence estimates span an order of magnitude (300,000 vs 2.7M/year). The Enable programme ([PMID: 36996258](https://pubmed.ncbi.nlm.nih.gov/36996258/)) aims to refine these.
2. **SNHL mechanism is inferred, not proven in humans.** The vasculitis model derives from macaque histology and mouse genetics; human temporal-bone pathology is scarce. Optimal timing/dose of steroids is unknown.
3. **Host genetics.** LARGE/IL21 selection signals suggest resistance but causal protective alleles and effect sizes in humans are not established.
4. **Therapeutics.** Ribavirin's evidence base is methodologically weak; favipiravir data are early-phase (PK/safety), not yet efficacy-powered. No approved monoclonal cocktail.
5. **No licensed vaccine**, and correlates of protection (neutralizing vs T-cell/Fc) remain debated.
6. **Pregnancy management** relies on small observational studies; mechanisms of placental tropism are partly extrapolated from other VHFs.

---

## Proposed Follow-up Experiments / Actions

1. **Powered efficacy RCT of favipiravir** (vs ribavirin or combination), stratified by viremia/AST, with mortality and SNHL endpoints.
2. **Prospective SNHL cohort** with serial audiometry, viral load, and inflammatory/autoantibody profiling to confirm the vasculitis hypothesis and test early corticosteroid/immunomodulatory intervention.
3. **Define correlates of protection** across vaccine platforms (LASSARAB, mRNA-LNP, DNA) using the CEPI-standardized neutralization International Units ([PMID: 42382775](https://pubmed.ncbi.nlm.nih.gov/42382775/)) and T-cell/Fc assays.
4. **Human genetic association study** in endemic populations to validate LARGE/IL21 resistance alleles and identify severity modifiers.
5. **Field evaluation of reservoir-targeted control** (CMV-vectored transmissible vaccine; [PMID: 42361202](https://pubmed.ncbi.nlm.nih.gov/42361202/)) integrated with climate-informed spillover forecasting.
6. **Decentralized molecular diagnostics** (point-of-care RT-PCR / antigen rapid tests) to shorten time-to-treatment in endemic centers.
7. **Pregnancy-specific trials** evaluating antiviral timing and uterine-evacuation protocols to reduce maternal/fetal mortality.

---

*Report compiled from 12 confirmed findings and 49 reviewed papers over 5 investigation iterations. Evidence types span human clinical studies, non-human-primate and rodent models, in vitro virology, and computational/epidemiological modeling.*


## Artifacts

- [OpenScientist final report](Lassa_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Lassa_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 40 |
| On topic | 34 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 26 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005820` (5 mentions) - the report calls it "if available"; MONDO calls it **Lassa fever**
- `HP:0000407` (3 mentions) - the report calls it "Sensorineural hearing impairment", "18–33% survivors"; HP calls it **Sensorineural hearing impairment**
- `HP:0002910` (2 mentions) - the report calls it "elevated AST/hepatic transaminases", "Prognostic"; HP calls it **Elevated circulating hepatic transaminase concentration**
- `HP:0000083` (2 mentions) - the report calls it "renal insufficiency", "Severe"; HP calls it **Renal insufficiency**
- `UBERON:0001844` (2 mentions) - the report calls it "cochlea", "SNHL"; UBERON calls it **cochlea**
- `HP:0001945` (1 mention) - the report calls it "Very common"; HP calls it **Fever**
- `HP:0025439` (1 mention) - the report calls it "Common"; HP calls it **Pharyngitis**
- `HP:0100749` (1 mention) - the report calls it "Common"; HP calls it **Chest pain**
- `HP:0001892` (1 mention) - the report calls it "Severe cases"; HP calls it **Abnormal bleeding**
- `HP:0000316` (1 mention) - the report calls it "Severe, poor prognosis"; HP calls it **Hypertelorism**
- `UBERON:0001987` (1 mention) - the report calls it "fetal loss"; UBERON calls it **placenta**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0039503` (obsolete suppression by virus of host innate immune response) (1 mention) - replaced by `GO:0052170`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001251` (1 mention) - the report calls it "Ataxia/balance"; HP calls it **Ataxia**
- `HP:0001250` (2 mentions) - the report calls it "Seizure", "Severe"; HP calls it **Seizure**
- `GO:0075509` (1 mention) - the report calls it "receptor-mediated endocytosis of virus by host cell"; GO calls it **endocytosis involved in viral entry into host cell**
- `GO:0039503` (1 mention) - the report calls it "suppression of host innate immune response by virus"; GO calls it **obsolete suppression by virus of host innate immune response**
- `UBERON:0002227` (1 mention) - the report calls it "organ of Corti"; UBERON calls it **spiral organ of cochlea**, and lists "organ of Corti" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000407` - called "Sensorineural hearing impairment", "18–33% survivors"
- `HP:0001250` - called "Seizure", "Severe"
- `HP:0002910` - called "elevated AST/hepatic transaminases", "Prognostic"
- `HP:0000083` - called "renal insufficiency", "Severe"
- `UBERON:0001844` - called "cochlea", "SNHL"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
