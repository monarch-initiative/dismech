---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T12:31:30.334404'
end_time: '2026-11-11T12:48:51.477535'
duration_seconds: 1041.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: PINK1-Related Early-Onset Parkinson Disease
  mondo_id: MONDO:0011613
  category: Mendelian
  causal_genes: PINK1
  omim_id: OMIM:605909
  synonyms: PINK1 Parkinson disease; Parkinson disease caused by mutation in PINK1
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
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 40
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PINK1-Related_Early-Onset_Parkinson_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PINK1-Related_Early-Onset_Parkinson_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PINK1-Related Early-Onset Parkinson Disease
- **MONDO ID:** MONDO:0011613 (if available)
- **Causal gene(s):** PINK1
- **OMIM:** OMIM:605909
- **Synonyms:** PINK1 Parkinson disease; Parkinson disease caused by mutation in PINK1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **PINK1-Related Early-Onset Parkinson Disease** covering all of the
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

# PINK1-Related Early-Onset Parkinson Disease (PARK6): Comprehensive Disease Characteristics Report

**Disease:** PINK1-Related Early-Onset Parkinson Disease
**Causal gene:** **PINK1** (PTEN-induced putative kinase 1)
**MONDO:** MONDO:0011613 | **OMIM:** 605909 (phenotype) / 608309 (gene) | **Orphanet:** ORPHA:2828 (autosomal recessive early-onset parkinsonism) | **Locus symbol:** PARK6

---

## Summary

PINK1-Related Early-Onset Parkinson Disease is a rare **autosomal recessive** form of early-onset parkinsonism caused by **biallelic loss-of-function mutations in PINK1**, the gene encoding PTEN-induced putative kinase 1, a 581-amino-acid mitochondrial serine/threonine kinase on chromosome 1p36. PINK1 was identified as the PARK6 gene by Valente and colleagues in 2004, providing the first direct molecular link between mitochondrial quality control and Parkinson disease pathogenesis ([PMID: 15087508](https://pubmed.ncbi.nlm.nih.gov/15087508/)). PINK1 is the **second most common cause of autosomal recessive early-onset Parkinson disease (EOPD)** after PRKN (parkin), accounting for roughly 1–8% of sporadic early-onset cases and a smaller fraction of familial recessive cases.

Mechanistically, PINK1 functions as a **mitochondrial damage sensor**. On healthy mitochondria it is continuously imported, cleaved by the protease PARL, and degraded by the proteasome. When a mitochondrion depolarizes, PINK1 is stabilized on the outer membrane via the TOMM import machinery, becomes active, and phosphorylates both **ubiquitin and the E3 ubiquitin ligase Parkin at Ser65**. This phospho-Ser65-ubiquitin (pS65-Ub) signal is the obligatory trigger for Parkin-dependent mitophagy — the selective autophagic clearance of damaged mitochondria. Loss of PINK1 kinase activity abolishes this signal, allowing damaged mitochondria to accumulate. Downstream consequences demonstrated in cellular and animal models include mitochondrial calcium overload, excess reactive oxygen species (ROS), a lowered mitochondrial permeability transition pore (mPTP) threshold, impaired axonal mitochondrial transport (via Miro), and bioenergetic failure, which together render substantia nigra dopaminergic neurons selectively vulnerable to age-dependent degeneration.

Clinically, PINK1-PD is a **benign, slowly progressive, excellently levodopa-responsive akinetic-rigid/tremor parkinsonism** with mean onset typically in the 30s to early 40s, often with early prominent lower-limb involvement, gait disturbance, and asymmetric onset, and with dystonia, motor fluctuations, and non-motor features occurring less frequently than in idiopathic PD. It is largely indistinguishable from parkin disease. Treatment is symptomatic — levodopa plus subthalamic deep brain stimulation (STN-DBS), both highly effective — with no disease-modifying therapy yet available. Neuropathology is heterogeneous and Lewy bodies are not obligate. This report synthesizes 16 confirmed findings across 67 reviewed papers into a complete disease knowledge-base entry.

---

## 1. Disease Information

**Overview.** PINK1-Related Early-Onset Parkinson Disease (PARK6) is a monogenic, autosomal recessive neurodegenerative movement disorder characterized by parkinsonism (bradykinesia, rigidity, rest tremor) with onset usually before age 45–50. It is caused by biallelic (homozygous or compound heterozygous) loss-of-function mutations in **PINK1**. Clinically it resembles PRKN-related disease: a relatively benign course, slow progression, excellent and sustained response to levodopa, and absence of early atypical features ([PMID: 22166450](https://pubmed.ncbi.nlm.nih.gov/22166450/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0011613 |
| OMIM (phenotype, PARK6) | 605909 |
| OMIM (gene PINK1) | 608309 |
| Orphanet | ORPHA:2828 (autosomal recessive early-onset parkinsonism) |
| HGNC (gene) | HGNC:14581 (PINK1) |
| ICD-10 | G20 (Parkinson disease) |
| ICD-11 | 8A00.0 (Parkinson disease) |
| MeSH | Parkinson Disease (D010300); Parkinsonian Disorders |

**Synonyms / alternative names.** PINK1 Parkinson disease; Parkinson disease caused by mutation in PINK1; PARK6; Parkinson disease 6, autosomal recessive early-onset; PTEN-induced kinase 1 Parkinson disease.

**Data provenance.** The information is derived predominantly from **aggregated disease-level resources** — OMIM, Orphanet, MDSGene, and primary cohort/case studies — rather than from individual EHR records. Mechanistic data derive from in vitro, iPSC, Drosophila, and mouse model systems.

---

## 2. Etiology

**Disease causal factors.** The disease is **monogenic and genetic**: biallelic loss-of-function mutations in PINK1 are necessary and sufficient to cause disease. Valente et al. identified homozygous PINK1 mutations in consanguineous PARK6 families — "we have identified two homozygous mutations affecting the PINK1 kinase domain in three consanguineous PARK6 families: a truncating nonsense mutation and a missense mutation at a highly conserved amino acid" — establishing loss of kinase function as the mechanism and providing "a direct molecular link between mitochondria and the pathogenesis of PD" ([PMID: 15087508](https://pubmed.ncbi.nlm.nih.gov/15087508/)). Because most reported mutations distribute throughout the serine/threonine kinase domain, the unifying mechanism is **loss of PINK1 kinase function** ([PMID: 17713119](https://pubmed.ncbi.nlm.nih.gov/17713119/)).

**Genetic risk factors.**
- **Causal variants:** biallelic PINK1 pathogenic variants (missense, nonsense, frameshift, splice-site, and exon-level copy-number changes).
- **Heterozygous carriers:** A single heterozygous PINK1 mutation is **not a robust PD risk factor**. A comprehensive assessment of 376,558 individuals (13,708 PD cases, 362,850 controls) found "we did not find evidence to support a role for heterozygous PINK1 mutations as a robust risk factor for Parkinson's disease" ([PMID: 32249012](https://pubmed.ncbi.nlm.nih.gov/32249012/)). An earlier screen (250 EOPD vs 276 controls) found heterozygosity over-represented in patients (4.00% vs 1.81%) but non-significant (p=0.13); biallelic carriers had onset ~11 years earlier than heterozygotes (95% CI 1.4–20.6, p=0.03) ([PMID: 19351622](https://pubmed.ncbi.nlm.nih.gov/19351622/)). Nevertheless, asymptomatic heterozygotes show subclinical dopaminergic and sensory abnormalities (see §3, §10).
- **Modifier genes:** APOE ε4 (rs429358) associates with higher mitophagy-pathway marker pS65-Ub and greater neuropathology; ZMIZ1 (rs6480922) is a suggestive protective modifier ([PMID: 40309932](https://pubmed.ncbi.nlm.nih.gov/40309932/)).

**Environmental risk factors.** Consanguinity enriches cases by increasing homozygosity for recessive founder alleles. Age is a permissive factor: PINK1 loss causes **age-dependent** phenotypes in models ([PMID: 42342694](https://pubmed.ncbi.nlm.nih.gov/42342694/)). No specific toxin or occupational exposure is established as a disease-specific trigger, though mitochondrial complex-I inhibitors (MPTP, rotenone) phenocopy aspects of the pathway.

**Protective factors.** No validated genetic or environmental protective factor is established specifically for PINK1-PD; ZMIZ1 is only a suggestive protective modifier of mitophagy flux ([PMID: 40309932](https://pubmed.ncbi.nlm.nih.gov/40309932/)).

**Gene–environment interactions.** The clearest interaction is **genotype × mitochondrial stress × age**. In mice, loss of Pink1/Prkn alone is insufficient; an additional mitochondrial stressor (e.g., mtDNA mutation) is required to trigger cGAS/STING-mediated innate immune activation and dopaminergic degeneration ([referenced in PMID: 32060339](https://pubmed.ncbi.nlm.nih.gov/32060339/)). This "two-hit" framework (genetic lesion plus acquired mitochondrial stress) is a central gene–environment concept for the disease.

---

## 3. Phenotypes

PINK1-PD presents as a **typical akinetic-rigid/tremor parkinsonism**. Core features and HPO suggestions:

| Phenotype | Type | HPO term | Frequency / characteristics |
|---|---|---|---|
| Bradykinesia | Clinical sign | HP:0002067 (Bradykinesia) | Common/core; progressive |
| Rigidity | Clinical sign | HP:0002063 (Rigidity) | Common/core |
| Rest tremor | Clinical sign | HP:0002322 / HP:0000822 | Common/core |
| Early lower-limb symptoms / gait disturbance | Clinical sign | HP:0002317 (Unsteady gait) | More frequent in PINK1 than other forms |
| Asymmetric onset | Clinical sign | — | More frequent among PINK1 cases |
| Dystonia | Clinical sign | HP:0001332 (Dystonia) | Lower percentage; levodopa-responsive |
| Motor fluctuations / dyskinesias | Clinical sign | HP:0100660 | Less frequent; dyskinesia is main levodopa side effect |
| Excellent levodopa response | Treatment response | — | 94.6–100% good response |
| Non-motor symptoms | Symptoms | — | Occur in a lower percentage of cases |
| Sensory abnormality (temporal discrimination) | Lab/functional | — | Subclinical, even in heterozygotes |

Key supporting evidence: "Bradykinesia, tremors, and rigidity are common features, while dystonia, motor fluctuation, and non-motor symptoms occur in a lower percentage of cases and usually respond well to levodopa" ([PMID: 37150071](https://pubmed.ncbi.nlm.nih.gov/37150071/)). "The reported features of early prominent lower-limb symptoms and gait disturbance with asymmetrical onset are more frequent among PINK1 disease cases" ([PMID: 28789629](https://pubmed.ncbi.nlm.nih.gov/28789629/)). "The phenotype is usually characterized by levodopa-responsive parkinsonism without atypical features" ([PMID: 22166450](https://pubmed.ncbi.nlm.nih.gov/22166450/)).

**Age of onset.** Mean onset in the 30s to early 40s. MDSGene reports monogenic *typical* parkinsonism (including PINK1) onset at ~40 years versus ~24 years for atypical recessive forms: "the age at onset was earlier in monogenic atypical parkinsonism (24 vs 40 years)" ([PMID: 34396589](https://pubmed.ncbi.nlm.nih.gov/34396589/)). **Severity:** mild to moderate, variable; generally benign. **Progression:** slow and progressive. **Quality of life:** motor disability is treatable for many years with levodopa and DBS, so QoL impact is relatively favorable versus idiopathic PD, though chronic and lifelong.

**Subclinical phenotype in carriers.** "Higher mean tactile and visuo-tactile TDTs and TOJs were detected in PINK1 mutation carriers, including not only homozygous patients but also healthy heterozygotes, compared to control subjects" ([PMID: 18584234](https://pubmed.ncbi.nlm.nih.gov/18584234/)) — indicating a measurable endophenotype even in asymptomatic single-mutation carriers.

---

## 4. Genetic / Molecular Information

**Causal gene.** PINK1 (PTEN-induced putative kinase 1), chromosome **1p36**, HGNC:14581, OMIM 608309. "PINK1 contains 8 exons spanning 1.8 kb, and encodes a protein of 581 amino acids with a mitochondrial targeting motif and a serine-threonine protein kinase domain" ([PMID: 17713119](https://pubmed.ncbi.nlm.nih.gov/17713119/)). Protein domains: N-terminal mitochondrial targeting sequence, transmembrane anchor, and a conserved serine/threonine kinase domain.

**Pathogenic variants.**
- **Types:** missense (e.g., G309D, G386A, L347P, T313M, A217D), nonsense/truncating (e.g., Q456*, W437X), frameshift (e.g., Q533Profs*29, R483Serfs*7), splice-site, and exon-level deletions/duplications (genomic rearrangements). "Since point mutations and genomic rearrangements can be present, sequencing and exon dosage are both required for accurate mutational screening of these genes" ([PMID: 22166450](https://pubmed.ncbi.nlm.nih.gov/22166450/)).
- **Classification:** Pathogenic/likely pathogenic per ACMG/AMP; biallelic requirement. Additional novel kinase-domain substitutions (e.g., P416R, S419P) segregate recessively ([PMID: 19087301](https://pubmed.ncbi.nlm.nih.gov/19087301/)).
- **Functional consequence:** **Loss of function** (loss of kinase activity). Kinase-domain mutations (e.g., T313M, L347P) specifically perturb the phospho-Ser65-ubiquitin recognition point essential for mitophagy ([PMID: 42602159](https://pubmed.ncbi.nlm.nih.gov/42602159/)).
- **Allele frequency / origin:** Rare; **germline**. Not somatic (COSMIC/TCGA not applicable).

**Founder mutations / population variants.**
- **p.A217D** — North African founder (Moroccan and Sudanese kindreds): "reports of p.A217D in families of Moroccan and Sudanese origin suggest that p.A217D is a North African mutation due to a founder effect" ([PMID: 28789629](https://pubmed.ncbi.nlm.nih.gov/28789629/)).
- **p.L347P** — common among Malay patients in Malaysia ([PMID: 37209484](https://pubmed.ncbi.nlm.nih.gov/37209484/)).

**Modifier genes.** APOE ε4 (rs429358) and ZMIZ1 (rs6480922) modify pS65-Ub mitophagy flux: "We identified a significant genome-wide association with p-S65-Ub for rs429358 (apolipoprotein E ε4 [APOE4]) and a suggestive association for rs6480922 (ZMIZ1)" ([PMID: 40309932](https://pubmed.ncbi.nlm.nih.gov/40309932/)). In Drosophila, iron-metabolism genes (dZIP13, transferrin) and Rab11 act downstream of Pink1 to modulate respiration/mitophagy ([PMID: 35038358](https://pubmed.ncbi.nlm.nih.gov/35038358/); [PMID: 37302569](https://pubmed.ncbi.nlm.nih.gov/37302569/)).

**Epigenetic / chromosomal.** No disease-specific DNA-methylation or large chromosomal abnormality is established for PINK1-PD. Exon-level CNVs within PINK1 occur but are a minority of EOPD CNV burden, which is dominated by PRKN deletions ([PMID: 42009659](https://pubmed.ncbi.nlm.nih.gov/42009659/)).

---

## 5. Environmental Information

PINK1-PD is fundamentally genetic; environmental factors are **modulatory** rather than causal. Mitochondrial complex-I inhibitors (MPTP, rotenone, paraquat) converge on the same pathway disrupted by PINK1 loss and can model PINK1/Parkin mitophagy deficits (e.g., BAP31/MPTP mouse models, [PMID: 41597212](https://pubmed.ncbi.nlm.nih.gov/41597212/)). **Lifestyle factors:** no PINK1-specific associations established; general PD lifestyle associations (smoking, caffeine) are not validated for this monogenic subtype. **Infectious agents:** none. The relevant "environmental" axis is acquired mitochondrial stress acting on a PINK1-null genetic background (two-hit model; §2).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function mutation in PINK1** → **loss of PINK1 serine/threonine kinase activity** ([PMID: 15087508](https://pubmed.ncbi.nlm.nih.gov/15087508/), [PMID: 17713119](https://pubmed.ncbi.nlm.nih.gov/17713119/)).
2. Loss of kinase activity → **failure to phosphorylate ubiquitin and Parkin at Ser65** on depolarized mitochondria → **no pS65-Ub mitophagy signal** → **failure to activate Parkin-dependent mitophagy**. "Autosomal recessive Parkinson's disease (ARPD) arises from impaired mitophagy due to dysfunction of the PINK1/Parkin pathway, where PINK1-mediated phosphorylation of ubiquitin at Ser65 is essential for pathway activation" ([PMID: 42602159](https://pubmed.ncbi.nlm.nih.gov/42602159/), [PMID: 40020067](https://pubmed.ncbi.nlm.nih.gov/40020067/), [PMID: 24901221](https://pubmed.ncbi.nlm.nih.gov/24901221/)).
3. Failed mitophagy → **accumulation of damaged mitochondria** / reduced mitochondrial quality control ([PMID: 38565869](https://pubmed.ncbi.nlm.nih.gov/38565869/), [PMID: 27453777](https://pubmed.ncbi.nlm.nih.gov/27453777/)).
4. **Branch A — Bioenergetic/transport failure:** loss of PINK1 → aberrant p38 MAPK activation → age-dependent mitochondrial trafficking deficits in nigrostriatal DA neurons → reduced dopamine release and ATP ([PMID: 42342694](https://pubmed.ncbi.nlm.nih.gov/42342694/)); dysregulated Miro and axonal transport ([PMID: 22396657](https://pubmed.ncbi.nlm.nih.gov/22396657/)); disrupted AMPK energy homeostasis in ventral midbrain ([PMID: 30411223](https://pubmed.ncbi.nlm.nih.gov/30411223/)). *(inferred mechanistic branch)*
5. **Branch B — Calcium/ROS cell-death arm:** loss of PINK1 → impaired mitochondrial Ca²⁺ efflux → **mitochondrial Ca²⁺ overload** → ROS production via NADPH oxidase + inhibited glucose transport → lowered mPTP threshold → physiological Ca²⁺ stimuli trigger mPTP opening → neuronal death ([PMID: 19285945](https://pubmed.ncbi.nlm.nih.gov/19285945/)).
6. **Branch C (inferred, model-based) — Innate immune arm:** accumulated mitochondrial damage + stress → cGAS/STING activation → neuroinflammation → DA degeneration (demonstrated in mice; *not* conserved in Drosophila) ([PMID: 32060339](https://pubmed.ncbi.nlm.nih.gov/32060339/)).
7. Convergence → **selective, age-dependent degeneration of substantia nigra pars compacta dopaminergic neurons** → striatal dopamine deficiency → **clinical parkinsonism** (bradykinesia, rigidity, tremor).

### Detail

**Molecular pathways:** PINK1/Parkin mitophagy (the central pathway); p38 MAPK; AMPK energy signaling; NADPH-oxidase ROS; cGAS/STING innate immunity. KEGG "mitophagy – animal" (map04137); Reactome "PINK1/PRKN Mediated Mitophagy."

**Cellular processes (GO):** selective autophagy of mitochondria / **mitophagy (GO:0000423)**; protein phosphorylation (GO:0006468); mitochondrion organization (GO:0007005); apoptotic process (GO:0006915); cellular response to oxidative stress (GO:0034599); regulation of mitochondrial membrane potential.

**Protein dysfunction:** PINK1 is normally short-lived — imported, PARL-cleaved, proteasome-degraded; on depolarization it is stabilized on the outer membrane via the TOMM complex and activated: "Under depolarizing conditions, it accumulates on mitochondria where it becomes activated, phosphorylating both ubiquitin and the ubiquitin E3 ligase Parkin" ([PMID: 40020067](https://pubmed.ncbi.nlm.nih.gov/40020067/)). Disease mutations abolish kinase activity (loss of function). PINK1 phosphorylates Parkin at Ser65 (human) / Ser94 (fly) to boost ligase activity; "A non-phosphorylated form of Parkin fully rescued the muscular mitochondrial degeneration due to the loss of PINK1 activity" — placing PINK1 genetically upstream ([PMID: 24901221](https://pubmed.ncbi.nlm.nih.gov/24901221/)). As damage sensor: "PINK1 is a kinase which functions as a mitochondrial damage sensor and initiates mitochondrial quality control by accumulating on the damaged organelle. There, it phosphorylates ubiquitin, which in turn recruits and activates Parkin" ([PMID: 38565869](https://pubmed.ncbi.nlm.nih.gov/38565869/)).

**Metabolic changes:** reduced ATP; decreased mitochondrial complex-I activity in PD brain ([PMID: 27453777](https://pubmed.ncbi.nlm.nih.gov/27453777/)); impaired respiration restorable by complex I/II substrates in PINK1-deficient cells ([PMID: 19285945](https://pubmed.ncbi.nlm.nih.gov/19285945/)).

**Tissue damage mechanisms:** "PINK1 deficiency causes mitochondrial accumulation of calcium, resulting in mitochondrial calcium overload. We show that calcium overload stimulates reactive oxygen species (ROS) production via NADPH oxidase," and "reduced mitochondrial calcium capacity and increased ROS lower the threshold of opening of the mitochondrial permeability transition pore (mPTP) such that physiological calcium stimuli become sufficient to induce mPTP opening in PINK1-deficient cells" ([PMID: 19285945](https://pubmed.ncbi.nlm.nih.gov/19285945/)).

**Immune involvement:** cGAS/STING innate immune activation in mouse Pink1/Prkn-plus-stress models (not conserved in Drosophila) ([PMID: 32060339](https://pubmed.ncbi.nlm.nih.gov/32060339/)).

**Biomarker of pathway activity:** pS65-Ub accumulates in human autopsy brain with age and correlates with pathology: "the number of pS65-Ub positive cells increases with age but is also associated with Lewy body (LB), neurofibrillary tangles (NFT), and senile plaque (SP) burden" ([PMID: 41326741](https://pubmed.ncbi.nlm.nih.gov/41326741/)).

**Upstream vs downstream:** PINK1 kinase loss is the **upstream initiating lesion**; Parkin activation, Ca²⁺/ROS/mPTP, transport failure, and bioenergetic collapse are **downstream**. Cell types: substantia nigra dopaminergic neurons (**CL:0000700 / CL:0002450** dopaminergic neuron); astrocytes/microglia contribute to the inflammatory arm.

```
PINK1 LoF ─► no kinase activity ─► no pSer65-Ub ─► Parkin not activated ─► mitophagy fails
                                                               │
                        ┌──────────────────────────────────────┼───────────────────────────┐
                        ▼                                       ▼                           ▼
             Ca²⁺ overload → ROS → ↓mPTP            p38 MAPK → transport deficit      cGAS/STING
             threshold → cell death                 ↓DA release, ↓ATP                 neuroinflammation (mouse)
                        └──────────────────────────────────────┼───────────────────────────┘
                                                                ▼
                            age-dependent SNpc dopaminergic neuron degeneration
                                                                ▼
                                             striatal dopamine loss → parkinsonism
```

---

## 7. Anatomical Structures Affected

- **Organ level:** Brain / central nervous system (nervous system). Primary site: **substantia nigra pars compacta** (UBERON:0001965, substantia nigra) and the **nigrostriatal dopaminergic pathway**; downstream **striatum** (UBERON:0002435) dopamine depletion. **Lateralization:** typically **asymmetric** at onset, becoming bilateral.
- **Tissue/cell level:** Nervous tissue; **midbrain dopaminergic neurons** (CL:0000700 / CL:0002450) are the selectively vulnerable population; astrocytes and microglia participate in the neuroinflammatory arm.
- **Subcellular level (GO cellular component):** **mitochondrion (GO:0005739)**; mitochondrial outer membrane (GO:0005741); the autophagosome–lysosome degradation system. PINK1 localizes to mitochondria via its N-terminal targeting motif.

---

## 8. Temporal Development

- **Onset:** Early-onset / young-onset — typically **before 45–50 years**, mean onset in the 30s to early 40s (~40 years for monogenic typical parkinsonism; [PMID: 34396589](https://pubmed.ncbi.nlm.nih.gov/34396589/)). Onset pattern is **insidious/chronic**.
- **Progression:** **Slow and benign**, chronic lifelong. Levodopa response is sustained over many years. Axial signs may become more prominent over time.
- **Disease course:** Progressive but indolent relative to idiopathic PD; no spontaneous remission. Treatment-induced symptomatic improvement (levodopa, DBS) is the only "remission-like" pattern.
- **Critical intervention window:** Symptomatic therapy is effective across the disease course; a disease-modifying window (before substantial nigral loss) is hypothetical given age-dependent model phenotypes ([PMID: 42342694](https://pubmed.ncbi.nlm.nih.gov/42342694/)).

---

## 9. Inheritance and Population

**Inheritance:** **Autosomal recessive** (biallelic). Heterozygous carriers are generally unaffected but show subclinical endophenotypes ([PMID: 18584234](https://pubmed.ncbi.nlm.nih.gov/18584234/)) and are not at robustly increased PD risk ([PMID: 32249012](https://pubmed.ncbi.nlm.nih.gov/32249012/)). **Penetrance:** biallelic appears high/age-dependent; **expressivity:** variable (intra- and interfamilial heterogeneity documented in Sudanese kindreds; [PMID: 37150071](https://pubmed.ncbi.nlm.nih.gov/37150071/)). No genetic anticipation (not a repeat-expansion disorder).

**Epidemiology / frequency.** PINK1 is the **second most common recessive EOPD gene** after PRKN. Representative frequencies:

| Cohort / population | PINK1 frequency | Reference |
|---|---|---|
| Sporadic early-onset PD (onset <45y) | ~1–8% | [PMID: 22166450](https://pubmed.ncbi.nlm.nih.gov/22166450/) |
| Malaysian EOPD (n=161, onset ≤50y) | 6/161 = 3.7% | [PMID: 37209484](https://pubmed.ncbi.nlm.nih.gov/37209484/) |
| African systematic review (6303 PD, 64 studies) | 0.57% | [PMID: 41958045](https://pubmed.ncbi.nlm.nih.gov/41958045/) |
| Biallelic vs heterozygote onset | ~11y earlier (95% CI 1.4–20.6, p=0.03) | [PMID: 19351622](https://pubmed.ncbi.nlm.nih.gov/19351622/) |

Supporting quote: "Mutations in PINK1 and DJ-1 are less common, accounting for ~1-8%, and ~1-2% of the sporadic cases with early-onset" ([PMID: 22166450](https://pubmed.ncbi.nlm.nih.gov/22166450/)). "Autosomal recessive PD linked to PINK1 (0.57%) or PRKN (0.32%)" ([PMID: 41958045](https://pubmed.ncbi.nlm.nih.gov/41958045/)). PRKN remains most common (~15% sporadic, ~50% familial recessive).

**Context — EOPD burden.** Young-onset PD (onset 21–50y) is 3–7% of all PD: "Young-onset Parkinson's disease (YOPD), defined as Parkinson's disease (PD) with onset between 21 and 50 years of age, represents 3-7% of all PD cases" ([PMID: 42247186](https://pubmed.ncbi.nlm.nih.gov/42247186/)). GBD 2021: "in 2021, incident cases reached 81,047 (95% UI: 48,162-122,328), prevalent cases 483,872," with ~2,246 deaths and ~180,325 DALYs, and rising age-standardized incidence/prevalence (EAPC +1.42% and +1.09%) ([PMID: 41876889](https://pubmed.ncbi.nlm.nih.gov/41876889/)). PINK1-PD is a **rare monogenic subset** within this.

**Population demographics / founder effects:** North African founder p.A217D (Moroccan/Sudanese; [PMID: 28789629](https://pubmed.ncbi.nlm.nih.gov/28789629/)); p.L347P common in Malay population ([PMID: 37209484](https://pubmed.ncbi.nlm.nih.gov/37209484/)). **Consanguinity** enriches cases. No strong North vs Sub-Saharan African difference (0.57%; [PMID: 41958045](https://pubmed.ncbi.nlm.nih.gov/41958045/)). Sex ratio is not strongly skewed in the monogenic form.

---

## 10. Diagnostics

**Genetic testing (definitive).** "Since point mutations and genomic rearrangements can be present, **sequencing and exon dosage are both required** for accurate mutational screening" ([PMID: 22166450](https://pubmed.ncbi.nlm.nih.gov/22166450/)). Recommended approach:
- **Single-gene / gene-panel sequencing** of PINK1 (plus PRKN, PARK7/DJ-1, and broader EOPD panels: SNCA, LRRK2, VPS35, ATP13A2, GBA1).
- **Exon dosage (MLPA)** to detect exon-level deletions/duplications missed by sequencing ([PMID: 19087301](https://pubmed.ncbi.nlm.nih.gov/19087301/)).
- **WES/WGS** increasingly used; panels validated in multiple cohorts (Hakka, Irish, Cypriot EOPD studies).

**Biomarkers / functional tests.**
- **pS65-Ub** (phospho-Ser65-ubiquitin) — tissue biomarker of PINK1-PRKN mitophagy; accumulates with age and correlates with neuropathology ([PMID: 41326741](https://pubmed.ncbi.nlm.nih.gov/41326741/), [PMID: 40309932](https://pubmed.ncbi.nlm.nih.gov/40309932/)). Research tool, not yet clinical.
- **Dopaminergic PET/SPECT** — asymptomatic heterozygotes show dopamine hypometabolism; documents nigrostriatal deficit ([PMID: 18584234](https://pubmed.ncbi.nlm.nih.gov/18584234/)).
- **Temporal discrimination thresholds (TDT/TOJ)** — elevated in carriers, including heterozygotes ([PMID: 18584234](https://pubmed.ncbi.nlm.nih.gov/18584234/)).

**Clinical criteria / differential diagnosis.** Diagnosis uses MDS clinical PD criteria plus confirmed biallelic PINK1 genotype. Differential: PRKN-PD (clinically nearly indistinguishable), DJ-1/PARK7-PD, ATP13A2 (Kufor-Rakeb), PLA2G6 (PARK14), idiopathic YOPD, dopa-responsive dystonia (GCH1), Wilson disease. Distinguishing features: recessive inheritance, consanguinity, benign levodopa-responsive course, and genetic confirmation.

**Screening.** Cascade genetic testing of at-risk relatives; carrier screening in consanguineous/founder populations (A217D, L347P).

---

## 11. Outcome / Prognosis

**Survival/mortality.** PINK1-PD is **not primarily life-shortening** the way late-stage idiopathic PD complications are; it is a chronic, benign, treatable parkinsonism. Disease-specific mortality data for the monogenic form are limited.

**Morbidity/function.** The dominant impact is **chronic motor disability**, substantially mitigated by levodopa and DBS for many years. Benign slow progression yields relatively favorable long-term function compared with idiopathic PD. Dyskinesias are the most frequent treatment-related morbidity (~15–40% across monogenic forms on levodopa; [PMID: 33459660](https://pubmed.ncbi.nlm.nih.gov/33459660/)).

**Disease course/complications.** Levodopa-induced dyskinesias and motor fluctuations with chronic therapy; axial/gait signs over time.

**Prognostic factors.** Biallelic (vs heterozygous) genotype → earlier onset ([PMID: 19351622](https://pubmed.ncbi.nlm.nih.gov/19351622/)). Modifiers (APOE ε4) may influence mitophagy flux and co-pathology burden ([PMID: 40309932](https://pubmed.ncbi.nlm.nih.gov/40309932/)). Excellent levodopa responsiveness predicts a favorable symptomatic course.

---

## 12. Treatment

**Pharmacotherapy — levodopa (first-line, highly effective).** "Levodopa showed an overall good outcome, especially in LRRK2, VPS35, Parkin, and PINK1 mutation carriers ('good' response in 94.6-100%)" ([PMID: 33459660](https://pubmed.ncbi.nlm.nih.gov/33459660/)). Adjuncts: dopamine agonists, COMT inhibitors, MAO-B inhibitors (standard PD pharmacology). NCIT: Levodopa (NCIT:C739); Carbidopa-Levodopa. Main side effect: **dyskinesias**.

**Surgical/interventional — subthalamic DBS (STN-DBS).** Highly effective and durable. Bilateral STN-DBS in early-onset parkinsonism produced long-term (3–6y) motor improvement comparable between mutation-positive and -negative patients: "in the long-term follow-up (3-6 years), both groups presented with the same degree of clinical improvement (MUT-: 44% vs MUT+: 42%)" ([PMID: 18378882](https://pubmed.ncbi.nlm.nih.gov/18378882/)). A Han Chinese EOPD-DBS cohort confirmed benefit regardless of genotype (one PINK1 carrier included; [PMID: 41486122](https://pubmed.ncbi.nlm.nih.gov/41486122/)). NCIT: Deep Brain Stimulation (NCIT:C16434).

**Supportive/rehabilitative.** Physical, occupational, and speech therapy; symptom management.

**Experimental / advanced therapeutics.** No approved disease-modifying therapy for PINK1-PD. Research directions: **small-molecule PINK1 kinase activators/stabilizers** (structural studies, [PMID: 38565869](https://pubmed.ncbi.nlm.nih.gov/38565869/)); **Parkin activators / molecular glues** that bypass PINK1 by enhancing pUb-mediated Parkin activation (e.g., BIO-2007817 partially rescues EOPD Parkin mutants; [PMID: 39300082](https://pubmed.ncbi.nlm.nih.gov/39300082/)); **mitophagy enhancers**; and **AAV gene-therapy strategies** developed for the sister recessive gene PRKN ([PMID: 42523270](https://pubmed.ncbi.nlm.nih.gov/42523270/), [PMID: 42984644](https://pubmed.ncbi.nlm.nih.gov/42984644/)) that provide a template for PINK1. An iPSC-based 320-compound screen "recapitulates the deficiency of mitochondrial clearance, ROS accumulation, and increasing apoptosis in these familial PD-derived neurons" and identified candidates improving mitochondrial clearance, ATP, and locomotion in PINK1 models ([PMID: 32470327](https://pubmed.ncbi.nlm.nih.gov/32470327/)).

**Personalized medicine.** Genotype-guided: biallelic PINK1 patients are good candidates for levodopa and DBS; the PINK1→pUb→Parkin pathway defines druggable nodes for future targeted therapy.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (monogenic recessive). The relevant lever is **genetic counseling** in consanguineous and founder populations (A217D, L347P), carrier screening, and reproductive options (preimplantation genetic diagnosis, prenatal testing).
- **Secondary prevention:** Cascade testing of at-risk relatives; early dopaminergic imaging to document presymptomatic nigrostriatal deficit ([PMID: 18584234](https://pubmed.ncbi.nlm.nih.gov/18584234/)).
- **Tertiary prevention:** Optimize levodopa dosing to limit dyskinesias; timely DBS for motor fluctuations.
- **Behavioral/public health/immunization:** No disease-specific interventions. General mitochondrial-stress avoidance (e.g., complex-I toxicants) is biologically plausible but unproven.
- **Counseling:** Autosomal recessive counseling — 25% recurrence risk for offspring of two carriers; founder-variant awareness.

---

## 14. Other Species / Natural Disease

- **Orthologous genes (NCBI Gene):** Mouse *Pink1* (Gene ID 68943); Drosophila *Pink1* (CG4523); zebrafish *pink1*; C. elegans *pink-1*. Evolutionary conservation of the PINK1/Parkin mitophagy axis is strong — PINK1 phosphorylates the conserved serine of Parkin (Ser65 human / Ser94 fly) across species ([PMID: 24901221](https://pubmed.ncbi.nlm.nih.gov/24901221/)).
- **Natural disease:** No well-characterized naturally occurring PINK1-PD equivalent in companion animals/wildlife is documented in the reviewed literature (OMIA not applicable here).
- **Comparative biology:** The STING/innate-immune arm is **not conserved** between mouse and Drosophila — "loss of Sting, or its downstream effector Relish, was insufficient to suppress the behavioural deficits or mitochondria disruption in the Pink1/parkin mutants" ([PMID: 32060339](https://pubmed.ncbi.nlm.nih.gov/32060339/)) — a key cross-species caveat.
- **Transmission:** Not applicable (non-infectious, genetic).

---

## 15. Model Organisms

| Model | Type | Phenotype recapitulation | Reference |
|---|---|---|---|
| *Drosophila* Pink1/parkin mutants | Invertebrate | Impaired climbing/flight, indirect flight-muscle degeneration, mitochondrial fragmentation/swelling; genetically places PINK1 upstream of Parkin; affects DA release/neuron survival | [PMID: 37440574](https://pubmed.ncbi.nlm.nih.gov/37440574/), [PMID: 24901221](https://pubmed.ncbi.nlm.nih.gov/24901221/) |
| Pink1-KO mouse | Mammalian | Age-dependent mitochondrial trafficking deficits via p38 MAPK; ↓dopamine release, ↓ATP; AMPK disruption in ventral midbrain; overt nigral loss mild (requires second hit) | [PMID: 42342694](https://pubmed.ncbi.nlm.nih.gov/42342694/), [PMID: 30411223](https://pubmed.ncbi.nlm.nih.gov/30411223/) |
| Patient iPSC-derived midbrain DA neurons | Cellular/in vitro | Recapitulate deficient mitochondrial clearance, ROS accumulation, increased apoptosis; enable drug screening | [PMID: 32470327](https://pubmed.ncbi.nlm.nih.gov/32470327/), [PMID: 33990932](https://pubmed.ncbi.nlm.nih.gov/33990932/) |
| Primary neurons / cell lines | In vitro | Ca²⁺ overload, ROS, lowered mPTP threshold, calcium-induced death | [PMID: 19285945](https://pubmed.ncbi.nlm.nih.gov/19285945/) |

**Phenotype recapitulation evidence.** In Drosophila, "loss of the early-onset PD gene parkin (the ortholog of human PRKN) results in impaired climbing ability, damage to the indirect flight muscles, and mitochondrial fragmentation with swelling" ([PMID: 37440574](https://pubmed.ncbi.nlm.nih.gov/37440574/)), with the same phenotype shared by Pink1 loss.

**Model limitations.** Rodent Pink1 knockouts show relatively mild overt dopaminergic neurodegeneration without a strong second stressor, and PD pathophysiology "is not faithfully replicated by animal models," motivating human iPSC midbrain DA-neuron models ([PMID: 33990932](https://pubmed.ncbi.nlm.nih.gov/33990932/)). The STING arm is species-divergent ([PMID: 32060339](https://pubmed.ncbi.nlm.nih.gov/32060339/)). Modifier screens in flies (iron metabolism, Rab11) reveal downstream nodes but require human validation.

**Genetic model types available:** knockout, knock-in (phosphomimetic/non-phosphorylatable Parkin), transgenic, RNAi, and patient-derived iPSC lines. **Resources:** MGI, FlyBase, ZFIN, WormBase, Cellosaurus/ATCC.

---

## Mechanistic Model / Interpretation

PINK1-PD is best understood as a **failure of mitochondrial quality control with age- and stress-dependent penetrance in a uniquely vulnerable cell type**. The initiating lesion — biallelic PINK1 kinase loss — removes the single enzymatic step (Ser65 phosphorylation of ubiquitin and Parkin) that licenses damaged-mitochondria clearance. Because substantia nigra dopaminergic neurons are long, highly branched, calcium-cycling, and energetically stressed, they are exquisitely sensitive to the downstream consequences: calcium overload and ROS (Branch B), bioenergetic and transport collapse (Branch A), and, in mammals, innate-immune amplification (Branch C). The three branches converge on selective nigral degeneration and striatal dopamine loss, producing a clinically "pure," levodopa-responsive parkinsonism. The relatively benign course likely reflects restricted downstream pathology (predominantly nigrostriatal, with non-obligate Lewy pathology) compared with the widespread synucleinopathy of idiopathic PD.

The convergence of in vitro, iPSC, Drosophila, and mouse evidence on a single upstream node (PINK1 kinase → pSer65-Ub) is this report's strongest conclusion and the clearest therapeutic rationale: restore or bypass the pSer65-Ub signal (PINK1 activators, Parkin molecular glues, or gene replacement).

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [15087508](https://pubmed.ncbi.nlm.nih.gov/15087508/) | Landmark | PINK1 identified as PARK6 gene; mitochondria–PD link |
| [17713119](https://pubmed.ncbi.nlm.nih.gov/17713119/) | Supports | Gene/protein structure; loss-of-function mechanism |
| [40020067](https://pubmed.ncbi.nlm.nih.gov/40020067/) | Supports | PINK1 stabilization/activation, substrate phosphorylation |
| [42602159](https://pubmed.ncbi.nlm.nih.gov/42602159/) | Supports | pSer65-Ub essential; T313M/L347P perturb recognition |
| [24901221](https://pubmed.ncbi.nlm.nih.gov/24901221/) | Supports | PINK1 upstream of Parkin in vivo (Drosophila) |
| [19285945](https://pubmed.ncbi.nlm.nih.gov/19285945/) | Supports | Ca²⁺ overload/ROS/mPTP cell-death arm |
| [42342694](https://pubmed.ncbi.nlm.nih.gov/42342694/) | Supports | p38 MAPK transport deficit; age-dependent DA/ATP decline |
| [22396657](https://pubmed.ncbi.nlm.nih.gov/22396657/) | Supports | Miro / axonal mitochondrial transport |
| [30411223](https://pubmed.ncbi.nlm.nih.gov/30411223/) | Supports | AMPK disruption in recessive PD midbrain |
| [32060339](https://pubmed.ncbi.nlm.nih.gov/32060339/) | Challenges/nuance | STING arm species-divergent (mouse yes, fly no) |
| [32470327](https://pubmed.ncbi.nlm.nih.gov/32470327/) | Supports | iPSC models recapitulate phenotype; enable screening |
| [22166450](https://pubmed.ncbi.nlm.nih.gov/22166450/) | Supports | Frequency, phenotype, testing requirements |
| [37209484](https://pubmed.ncbi.nlm.nih.gov/37209484/) | Supports | Malaysian EOPD frequency; L347P founder |
| [28789629](https://pubmed.ncbi.nlm.nih.gov/28789629/) | Supports | A217D North African founder; limb/gait features |
| [32249012](https://pubmed.ncbi.nlm.nih.gov/32249012/) | Challenges | Heterozygous PINK1 not a robust risk factor |
| [18584234](https://pubmed.ncbi.nlm.nih.gov/18584234/) | Supports | Subclinical carrier endophenotypes |
| [33459660](https://pubmed.ncbi.nlm.nih.gov/33459660/) | Supports | Levodopa response 94.6–100% |
| [18378882](https://pubmed.ncbi.nlm.nih.gov/18378882/) | Supports | STN-DBS long-term efficacy |
| [40309932](https://pubmed.ncbi.nlm.nih.gov/40309932/) | Supports | APOE/ZMIZ1 mitophagy modifiers |
| [41326741](https://pubmed.ncbi.nlm.nih.gov/41326741/) | Supports | pS65-Ub tissue biomarker |
| [29124790](https://pubmed.ncbi.nlm.nih.gov/29124790/) | Nuance | Lewy bodies non-obligate; few PINK1 autopsies (n=5) |
| [34396589](https://pubmed.ncbi.nlm.nih.gov/34396589/) | Supports | Onset ~40y for monogenic typical parkinsonism |
| [37150071](https://pubmed.ncbi.nlm.nih.gov/37150071/) | Supports | Symptom frequencies; intra/interfamilial heterogeneity |
| [41876889](https://pubmed.ncbi.nlm.nih.gov/41876889/) | Context | GBD EOPD burden |
| [41958045](https://pubmed.ncbi.nlm.nih.gov/41958045/) | Supports | African frequency 0.57% |
| [38565869](https://pubmed.ncbi.nlm.nih.gov/38565869/) | Supports | PINK1 damage sensor; small-molecule modulators |
| [39300082](https://pubmed.ncbi.nlm.nih.gov/39300082/) | Supports | Parkin molecular-glue activators (therapeutic template) |

---

## Limitations and Knowledge Gaps

1. **Sparse human neuropathology.** Only ~5 PINK1 autopsy cases exist (1 biallelic, 4 heterozygotes); "Lewy bodies may be present in syndromes clinically distinctive from PD... and absent in patients with clinical PD syndrome (eg, LRRK2-PD or Parkin-PD)" ([PMID: 29124790](https://pubmed.ncbi.nlm.nih.gov/29124790/)). Whether PINK1-PD is typically Lewy-body-positive is unresolved.
2. **Model-to-human translation.** Rodent Pink1 knockouts under-recapitulate degeneration without a second hit; the STING arm is not conserved across species ([PMID: 32060339](https://pubmed.ncbi.nlm.nih.gov/32060339/)).
3. **Branch weighting.** The relative in vivo contribution of the Ca²⁺/ROS vs transport/bioenergetic vs innate-immune branches to human nigral loss is not quantified.
4. **Epidemiology precision.** True population prevalence/incidence of the monogenic form is imprecise; figures derive from EOPD cohorts of varying ascertainment.
5. **Biomarker maturity.** pS65-Ub is a promising tissue biomarker but lacks a validated accessible (CSF/blood/imaging) assay for clinical use.
6. **No disease-modifying therapy.** All approved treatment is symptomatic.

---

## Proposed Follow-up Experiments / Actions

1. **Build a PINK1-PD natural-history registry** with longitudinal motor/non-motor scales, DAT imaging, and (where possible) autopsy, to resolve the Lewy-body question and progression rates.
2. **Develop an accessible pS65-Ub biomarker** (CSF/peripheral/PET) and test it as a target-engagement readout for mitophagy-enhancing therapeutics.
3. **Advance PINK1 kinase activators / Parkin molecular glues** (e.g., BIO-2007817-class) through PINK1-null iPSC DA neurons and conditional Pink1 mouse models, using the 320-compound screening platform ([PMID: 32470327](https://pubmed.ncbi.nlm.nih.gov/32470327/), [PMID: 39300082](https://pubmed.ncbi.nlm.nih.gov/39300082/)).
4. **Adapt AAV gene-replacement strategy from PRKN** ([PMID: 42523270](https://pubmed.ncbi.nlm.nih.gov/42523270/)) to PINK1, validating pSer65-Ub restoration as the pharmacodynamic endpoint.
5. **Dissect branch contributions** with cell-type-specific rescue (restoring Ca²⁺ handling, transport, or blocking STING) in mice to rank therapeutic nodes.
6. **Genotype-stratified DBS/levodopa outcome studies** powered for PINK1 specifically, and carrier-screening programs in A217D/L347P founder populations.

---

*Report compiled from 16 confirmed findings across 67 reviewed papers over 5 investigation iterations. Evidence sources span human clinical/cohort studies, human autopsy, iPSC in vitro models, Drosophila, and mouse genetics.*


## Artifacts

- [OpenScientist final report](PINK1-Related_Early-Onset_Parkinson_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PINK1-Related_Early-Onset_Parkinson_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 27 |
| Quoted claims found in source | 23 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 40 |
| On topic | 33 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:40309932` *(abstract only)*: "We identified a significant genome-wide association with p-S65-Ub for rs429358 (apolipoprotein E ε4 [APOE4]) and a suggestive association for rs6480922 (ZMIZ1)"
  - closest text in source: "We identified a significant genome-wide association with p-S65-Ub for rs429358 (apolipoprotein E ε4 [APOE4]) and a suggestive association for rs6480922 (ZMIZ1)"
- `PMID:40020067` *(abstract only)*: "Autosomal recessive Parkinson's disease (ARPD) arises from impaired mitophagy due to dysfunction of the PINK1/Parkin pathway, where PINK1-mediated phosphorylation of ubiquitin at Ser65 is essential for pathway activation"
  - closest text in source: "Under depolarizing conditions, it accumulates on mitochondria where it becomes activated, phosphorylating both ubiquitin and the ubiquitin E3 ligase Parkin, at Ser65"
- `PMID:24901221` *(abstract only)*: "Autosomal recessive Parkinson's disease (ARPD) arises from impaired mitophagy due to dysfunction of the PINK1/Parkin pathway, where PINK1-mediated phosphorylation of ubiquitin at Ser65 is essential for pathway activation"
  - closest text in source: "In contrast, phosphomimetic Parkin accelerated mitochondrial fragmentation or aggregation and the degradation of mitochondrial proteins regardless of PINK1 activity, suggesting that the phosphorylation of Parkin boosts its ubiquitin-ligase activity"
- `PMID:22166450` *(abstract only)*: "Mutations in PINK1 and DJ-1 are less common, accounting for ~1-8%, and ~1-2% of the sporadic cases with early-onset"
  - closest text in source: "Mutations in PINK1 and DJ-1 are less common, accounting for -1-8%, and -1-2% of the sporadic cases with early-onset"
