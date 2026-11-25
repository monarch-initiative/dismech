---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-13T08:50:28.273926'
end_time: '2026-11-13T09:35:11.022487'
duration_seconds: 2682.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Blepharocheilodontic Syndrome 2
  mondo_id: MONDO:0040503
  category: Mendelian
  causal_genes: CTNND1
  omim_id: OMIM:617681
  synonyms: blepharo-cheilo-odontic syndrome caused by mutation in CTNND1; CTNND1
    blepharo-cheilo-odontic syndrome
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: 25570f7e-55d9-47ec-b117-b4cc2284be44
citation_count: 0
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Blepharocheilodontic_Syndrome_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Blepharocheilodontic_Syndrome_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Blepharocheilodontic Syndrome 2
- **MONDO ID:** MONDO:0040503 (if available)
- **Causal gene(s):** CTNND1
- **OMIM:** OMIM:617681
- **Synonyms:** blepharo-cheilo-odontic syndrome caused by mutation in CTNND1; CTNND1 blepharo-cheilo-odontic syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Blepharocheilodontic Syndrome 2** covering all of the
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

# Blepharocheilodontic Syndrome 2 (CTNND1): Comprehensive Disease Characterization

**Causal gene: CTNND1** (δ1-catenin / p120-catenin / p120ctn), HGNC:2515, Ensembl ENSG00000198561, chromosome 11q12.1.
**Disease identifiers:** MONDO:0040503 · OMIM:617681 · DOID:0080346 · MedGen:1623594 · UMLS:C4540127 · Orphanet ORPHA:1997 (Blepharo-cheilo-dontic syndrome, gene-agnostic parent entity).

Blepharocheilodontic syndrome 2 (BCDS2) is the **CTNND1-related** form of blepharo-cheilo-dontic (BCD) syndrome. It must not be confused with BCDS1 (OMIM 119580), the allied disorder caused by *CDH1* (E-cadherin) — both genes encode members of the same epithelial cadherin–catenin adhesion complex, and the clinical phenotypes overlap, but the causal gene for the disease requested here (MONDO:0040503 / OMIM 617681) is **CTNND1**.

> Evidence sourcing note: BCDS2 is an ultra-rare Mendelian disorder. The information below is derived from **aggregated disease-level resources** (OMIM, Monarch/HPO, Orphanet, gnomAD) and from **primary individual-patient case series / cohort reports** (human clinical) plus **model-organism (mouse, Xenopus, zebrafish) and in-vitro** functional studies. There are no large EHR cohorts or omics datasets specific to BCDS2.

---

## 1. Disease Information

BCDS2 is a rare autosomal dominant congenital malformation syndrome affecting the **eyelids (blepharo-), lip/palate (cheilo-), and teeth (-dontic)**. The classic triad comprises eyelid malformations (lagophthalmos, ectropion of the lower eyelids, euryblepharon, distichiasis), cleft lip and/or palate, and ectodermal/dental anomalies (oligodontia, conical teeth). The CTNND1-related form additionally carries an expanded spectrum including congenital heart defects, limb anomalies, neurodevelopmental problems, and more recently reported genitourinary and CNS anomalies (PMID 32196547; PMID 40028877; PMID 39487033).

- **Key identifiers:** MONDO:0040503; OMIM 617681; Orphanet ORPHA:1997 (BCD syndrome); DOID:0080346; MedGen C1623594/CUI 1623594; UMLS C4540127. ICD-10: Q87.0 (congenital malformation syndromes predominantly affecting facial appearance); ICD-11: LD2F.1Y/ nearest "other specified syndromes with facial/structural anomalies." No dedicated MeSH descriptor exists; indexed under cleft lip/palate and eyelid abnormality terms.
- **Synonyms:** Blepharocheilodontic syndrome type 2; blepharo-cheilo-odontic syndrome caused by mutation in CTNND1; CTNND1 blepharo-cheilo-odontic syndrome; BCDS2; BCD syndrome (CTNND1-related). Historically overlaps with "lagophthalmos–cleft lip/palate" descriptions (PMID 15930907).
- **Monarch definition:** "Any blepharo-cheilo-odontic syndrome in which the cause of the disease is a mutation in the CTNND1 gene."

## 2. Etiology

**Primary cause — genetic.** BCDS2 is caused by **heterozygous loss-of-function (protein-truncating) variants in CTNND1**, acting through haploinsufficiency (PMID 28301459; PMID 29348693; PMID 32196547). It is a monogenic, autosomal dominant disorder; there is no infectious or primarily environmental etiology.

- **Genetic risk factors:** The causal variant itself is the risk factor. Most BCDS2 variants are *de novo* (6/8 in Alharatani 2020, PMID 32196547), but transmitted (inherited) variants occur in multigenerational families (e.g., a four-generation Chinese pedigree with c.83delG p.(Ala29Argfs*55), PMID 36584998). A positive **family history** raises recurrence risk to ~50% per the dominant pattern.
- **Environmental / lifestyle / occupational risk factors:** None established specific to BCDS2. General orofacial-cleft risk modifiers (maternal smoking, folate status, teratogens) are not demonstrated to modulate this monogenic syndrome.
- **Protective factors:** None identified (no protective alleles or environmental factors reported). The extreme population depletion of CTNND1 LoF variants (gnomAD) reflects purifying selection, not a protective mechanism.
- **Gene–environment interactions:** Not documented for BCDS2. Variable expressivity (below) is presumed to reflect genetic background/modifiers and stochastic developmental factors rather than defined exposures.
- **Modifier genes:** Not formally established. Mechanistically plausible modifiers are other components of the cadherin–p120 complex (CDH1, CDH3/P-cadherin, PLEKHA7, PLEKHA5, ESRP2); the 2026 mouse work shows combined E-/P-cadherin dosage sets a fusion threshold (PMID 41231213), implying cadherin-pathway dosage could modulate severity.

## 3. Phenotypes (with HPO terms and HPOA frequencies)

Curated HPO annotations (Monarch/HPOA) and cohort reports give the following. Onset is **congenital** for all structural features; course is **stable/non-progressive** (a congenital malformation syndrome), though secondary problems (corneal exposure, malocclusion) can worsen without treatment.

| Phenotype | HPO term | Frequency | Type |
|---|---|---|---|
| Conical tooth | HP:0000698 | ~100% | physical/dental sign |
| Tooth agenesis / oligodontia | HP:0009804 (HP:0000156) | ~100% (mean 13.7 missing permanent teeth, range 7–17; PMID 28181393) | physical/dental |
| Ectropion of lower eyelids | HP:0007651 | ~100% | clinical sign |
| Cleft lip (± palate) | HP:0410030 / HP:0000175 | ~67% (bilateral common) | physical |
| Distichiasis | HP:0009743 | ~67% | clinical sign |
| Euryblepharon | HP:0012905 | ~67% | clinical sign |
| Lagophthalmos | HP:0030001 | ~67% | clinical sign |
| Cutaneous syndactyly | HP:0012725 | occasional | physical |
| Facial asymmetry | HP:0000324 | occasional | physical |
| Nail dysplasia | HP:0002164 | reported | ectodermal |
| Flat face / high forehead / hypertelorism | HP:0012368 / HP:0000348 / HP:0000316 | reported | craniofacial |
| Class III malocclusion, short/narrow maxilla, taurodontism | HP:0000689 (taurodontism) | cohort: all patients (PMID 28181393) | dental/skeletal |
| Congenital heart defect | HP:0001627 | subset (PMID 32196547) | structural |
| Limb anomalies | HP:0002813 | subset (PMID 32196547) | structural |
| Developmental delay / neurodevelopmental disorder | HP:0001263 / HP:0012758 | subset (PMID 32196547) | neurobehavioral |
| Genitourinary anomalies (duplex kidney, ureterocele, bicornuate uterus) | HP:0000107/HP:0000070/HP:0000813 | rare (PMID 40028877) | structural |
| Hydrocephalus (prenatal) | HP:0000238 | rare (PMID 39487033) | CNS |

- **Severity:** Variable; dental and lower-eyelid signs essentially fully penetrant, clefting and classic eyelid features highly frequent (~67%).
- **Quality-of-life impact:** Feeding and speech difficulties (cleft), ocular-surface discomfort and keratopathy risk (lagophthalmos/ectropion/distichiasis), dental function and facial aesthetics (oligodontia, malocclusion), and psychosocial impact. No disease-specific EQ-5D/SF-36 data exist; QoL inferred from general cleft and oligodontia literature.

## 4. Genetic / Molecular Information

- **Causal gene:** CTNND1 (HGNC:2515; OMIM *601045), encoding p120-catenin/δ1-catenin; UniProt O60716. Protein domains: N-terminal coiled-coil/regulatory domain and central Armadillo (ARM) repeat domain that binds the cadherin juxtamembrane domain.
- **Variant types:** Predominantly **protein-truncating** — frameshift (e.g., c.83delG p.Ala29Argfs*55, PMID 36584998), nonsense, and canonical **splice-site** variants (e.g., de novo splice variant, PMID 40028877). Ghoumid 2017 described 3 truncating CTNND1 variants; Kievit 2018 added more; Alharatani 2020 reported 8 novel truncating variants (6 de novo) (PMID 28301459; 29348693; 32196547). Some rare missense variants are reported in the broader CTNND1-cleft spectrum.
- **ACMG/AMP classification:** Truncating variants in this LoF-intolerant gene typically meet pathogenic/likely-pathogenic criteria (PVS1 + de novo PS2/PM6 + absence in gnomAD PM2).
- **Allele frequency:** Pathogenic alleles are absent/ultra-rare in gnomAD. Gene-level constraint (gnomAD): **pLI = 1.00, LOEUF = 0.217, observed/expected LoF = 0.143 (16 observed vs 112 expected), LoF Z = 7.70; missense Z = 3.00** — among the most LoF-intolerant genes in the genome, strongly supporting haploinsufficiency.
- **Somatic vs germline:** Germline (constitutional); de novo or inherited. (Somatic CTNND1/CDH1-pathway alterations occur in cancers but are unrelated to this congenital syndrome.)
- **Functional consequence:** **Loss of function / haploinsufficiency** (reduced p120-catenin dosage destabilizing surface cadherins). Dominant-negative mechanisms characterize *CDH1* BCDS1 variants, not CTNND1 LoF.
- **Modifier genes:** See §2. **Epigenetics:** No disease-specific methylation/histone signature reported. **Chromosomal abnormalities:** BCDS2 is a single-gene disorder; no recurrent cytogenetic rearrangement — though a contiguous 17q12 microdeletion was an incidental, unrelated finding in one family (PMID 36584998).

## 5. Environmental Information

Not applicable as a primary driver. **Environmental factors, lifestyle factors, and infectious agents are not causative** of BCDS2; it is a monogenic developmental disorder. General teratogen avoidance in pregnancy is prudent but does not specifically prevent or modify this genetic condition.

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous truncating/splice CTNND1 variant **leads to** nonsense-mediated decay / a non-functional allele → **reduced p120-catenin (δ1-catenin) dosage (haploinsufficiency)** [demonstrated: gnomAD constraint, clinical LoF variants].
2. Reduced p120-catenin **results in** failure to cap and stabilize the cadherin cytoplasmic juxtamembrane domain → **increased cadherin (E-cadherin/CDH1, P-cadherin/CDH3) endocytosis and turnover**, lowering surface cadherin levels [demonstrated in vitro/mouse: PMID 28301459, PMID 41231213].
3. Lowered cadherin levels **drop adhesion below the elevated threshold specifically required for upper-lip epithelial fusion**, and dysregulate **actomyosin contractility** needed to drive fusion → **failed epithelial tissue fusion/integrity** [demonstrated, mouse live-imaging + allelic series: PMID 41231213].
4. Failed fusion/epithelial integrity in the developing **lip, palate, eyelid margins, and tooth-forming (dental lamina) epithelia** → **cleft lip/palate, eyelid malformations (lagophthalmos, ectropion, euryblepharon, distichiasis), and tooth agenesis/conical teeth** [demonstrated: conditional Cdh1/Ctnnd1 mouse deletions recapitulate BCD-like eyelid, craniofacial, tooth features; Ctnnd1-KO recapitulates CL/P: PMID 28301459, PMID 29805042].
5. **Branch A (adhesion/contractility):** the principal, developmentally essential route — p120's **cadherin-stabilizing** function; its RhoA- and Kaiso-binding functions are **dispensable** in mammalian development (PMID 41231213).
6. **Branch B (Wnt/transcriptional):** reduced p120 also **lowers protection of β-catenin from GSK3β-ubiquitin–mediated degradation**, attenuating **Wnt/β-catenin signaling** and perturbing EMT/transcription (Kaiso de-repression) — inferred contributor to vascular/other phenotypes; GSK3β inhibition (LiCl, CHIR-99021) rescues in the CTNND1-FEVR model (PMID 35700046).
7. Additional **p120 roles in neural-crest–derived periocular mesenchyme** → anterior-segment/ocular contributions (Wnt1-Cre Ctnnd1 ablation causes anterior segment dysgenesis in mice: PMID 22736606) — mechanistic support for the ocular component.

- **Molecular pathways:** Adherens junction (KEGG hsa04520), Wnt signaling (hsa04310), Rho GTPase/actomyosin contractility, Rap1 signaling. **Reactome:** adherens junctions interactions; degradation/stabilization of β-catenin.
- **Cellular processes:** Cell–cell adhesion, epithelial tissue fusion, epithelial–mesenchymal transition (EMT), cell migration, regulation of actomyosin contractility, cadherin recycling/endocytosis.
- **Protein dysfunction:** Quantitative **loss of function** (reduced protein), not aggregation/misfolding; downstream loss of cadherin stabilization.
- **Metabolic / immune / oxidative:** No primary metabolic, autoimmune, or oxidative-stress mechanism; tissue "damage" is **developmental dysmorphogenesis** (failed fusion), not degeneration.
- **GO terms:** GO:0016339 (calcium-dependent cell–cell adhesion via plasma-membrane adhesion molecules), GO:0045216 (cell–cell junction organization), GO:0016055 (Wnt signaling pathway), GO:0001837 (epithelial to mesenchymal transition), GO:0003382 (epithelial cell morphogenesis), GO:0060662 (salivary/epithelial fusion-related morphogenesis), GO:0097178 (ruffle assembly/actomyosin). **Cellular component:** GO:0005913 (cell–cell adherens junction), GO:0005912 (adherens junction), GO:0016342 (catenin complex).
- **Cell types (CL):** epithelial cell (CL:0000066), keratinocyte (CL:0000312), neural crest cell (CL:0000333), cranial neural crest–derived mesenchyme, odontogenic/dental epithelial cells, endothelial cell (CL:0000115, relevant to the FEVR/vascular branch).
- **Molecular profiling:** No BCDS2-specific transcriptomic/proteomic/metabolomic dataset. Model work used proteomics to define the p120–β-catenin–Wnt axis (PMID 35700046) and functional CRISPR/Cas9 Xenopus and conditional-mouse approaches (PMID 32196547).

## 7. Anatomical Structures Affected

- **Primary organs/structures:** Eyelids (UBERON:0000074) and eyelid margin; upper/lower lip (UBERON:0001833) and lip fusion sites; secondary palate/palatal shelves (UBERON:0001716); teeth and dental lamina (UBERON:0001091); skin/hair/nails (ectodermal derivatives).
- **Secondary / associated involvement:** Heart (UBERON:0000948) — congenital cardiac anomalies; limbs (UBERON:0002101); kidney/urinary tract (UBERON:0000057/0002113) and uterus (UBERON:0000995) in rare cases; brain/ventricular system (UBERON:0000955) — rare hydrocephalus; anterior segment of eye (cornea/iris) via neural-crest mechanism (model data).
- **Body systems:** Integumentary/craniofacial, ocular/visual, digestive (oral), cardiovascular, musculoskeletal (limb/skeletal malocclusion), and in a minority CNS and genitourinary.
- **Tissue/cell level:** Primarily **epithelial tissue** (and its adherens junctions) plus **neural-crest–derived craniofacial mesenchyme**. **Subcellular (GO CC):** plasma membrane / cell–cell adherens junction (GO:0005913), catenin complex (GO:0016342), cytoplasm.
- **Lateralization:** Eyelid and clefting features are typically **bilateral** (bilateral cleft lip/palate is characteristic; PMID 28181393), though unilateral clefts occur (PMID 40028877); facial asymmetry may be present.

## 8. Temporal Development

- **Onset:** **Congenital** — structural anomalies form during embryonic craniofacial morphogenesis; some are detectable **prenatally** (PMID 39487033).
- **Onset pattern:** Non-acute, developmental/insidious (present at birth).
- **Progression:** **Stable/non-progressive** malformations; disease duration is **lifelong**. Secondary deterioration (exposure keratopathy, malocclusion, dental loss, speech/feeding difficulty) can progress if untreated but the primary lesions do not advance.
- **Critical period / window of opportunity:** The developmental critical period is **embryonic facial fusion** (weeks ~4–10 of human gestation); therapeutically, the actionable windows are **postnatal surgical/reconstructive** (cleft repair in infancy, eyelid surgery to protect the cornea, dental rehabilitation in childhood/adolescence). No remission/relapse pattern (not applicable to a congenital malformation).

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant** (PMID 29348693). Both de novo and transmitted; recurrence risk ~50% for an affected parent; de novo cases carry low recurrence risk tempered by possible **gonadal mosaicism** (reported for the broader group; specific CTNND1 mosaicism data limited).
- **Penetrance:** High/essentially complete for the dental/eyelid signs; **expressivity is variable** (intra- and interfamilial). Classic clefting features are incompletely penetrant (~67%).
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects / consanguinity:** None established; a dominant disorder, consanguinity is not a driver.
- **Carrier frequency / population:** No carrier state (dominant); pathogenic alleles are ultra-rare/absent in gnomAD.
- **Epidemiology:** **Ultra-rare.** Orphanet prevalence for BCD syndrome is **<1/1,000,000**; only a few dozen patients across both CDH1 and CTNND1 forms are reported in the literature. No reliable incidence figure. No strong ethnic predilection (cases reported from Europe, Asia, the Americas, India, the Middle East). **Sex ratio:** no clear sex bias (reported in both sexes). **Age distribution:** diagnosed at birth/infancy.

## 10. Diagnostics

- **Clinical recognition:** Diagnosis is suspected on the **characteristic triad** (eyelid malformations + cleft lip/palate + oligodontia/conical teeth) and confirmed by **molecular genetic testing** of CTNND1 (and CDH1 for BCDS1).
- **Genetic testing (recommended approach):** **Gene-panel or exome/genome sequencing** is the mainstay; targeted single-gene/Sanger of CTNND1 can confirm a familial variant. CTNND1 is included on cleft-palate, orofacial-cleft, and craniofacial/eyelid-anomaly NGS panels. WES/WGS with **reverse phenotyping** enabled a prenatal diagnosis (PMID 39487033). Chromosomal microarray is not diagnostic for this single-gene disorder but may be used to exclude CNV mimics (e.g., 22q11.2 deletion given velocardiofacial overlap).
- **Imaging / functional / other tests:** Not diagnostic per se but used to delineate complications — **echocardiography** (cardiac anomalies), **renal/pelvic ultrasound** (genitourinary anomalies; recommended at diagnosis per PMID 40028877), cephalometric/dental radiographs (malocclusion, oligodontia; PMID 28181393), ophthalmologic exam (corneal exposure). No specific biochemical biomarker, enzyme assay, histopathology finding, or liquid-biopsy test exists.
- **Clinical criteria / differential diagnosis:** No formal consensus criteria. **Differential diagnosis:** BCDS1 (CDH1); ankyloblepharon–ectodermal defects–cleft lip/palate (AEC/Hay–Wells, TP63); ectrodactyly–ectodermal dysplasia–clefting (EEC, TP63); van der Woude syndrome (IRF6, lip pits); velocardiofacial/22q11.2 deletion syndrome; Kabuki syndrome; isolated non-syndromic cleft lip/palate; and isolated lagophthalmos/euryblepharon (PMID 15930907). Distinguishing features: BCD's combination of distichiasis/euryblepharon/ectropion with oligodontia and clefting, plus a CTNND1 (or CDH1) variant.
- **Screening:** No population newborn screening (ultra-rare). **Cascade genetic testing** of at-risk relatives and **prenatal/preimplantation testing** are available once a familial variant is known.

## 11. Outcome / Prognosis

- **Survival / life expectancy:** Generally **normal life expectancy** for patients without severe cardiac or CNS involvement; BCDS2 is not intrinsically life-limiting. No disease-specific mortality statistics; deaths would relate to major associated anomalies (complex congenital heart disease, severe CNS malformation) in a minority.
- **Morbidity / disability:** Mostly **functional and reconstructive** — ocular-surface disease from lagophthalmos/ectropion/distichiasis (risk of corneal exposure keratopathy and visual impairment if untreated), feeding and speech impairment from clefting, dental dysfunction and facial/aesthetic concerns from oligodontia and Class III malocclusion, and possible developmental/learning difficulties in the subset with neurodevelopmental involvement.
- **Disease course:** Stable primary lesions; outcomes are generally **good with multidisciplinary treatment**. **Complications:** exposure keratopathy, recurrent otitis media/hearing issues (cleft palate), speech/velopharyngeal dysfunction, malocclusion.
- **Prognostic factors:** Presence and severity of cardiac, CNS, and neurodevelopmental involvement are the main determinants of overall prognosis; isolated craniofacial involvement has an excellent prognosis. No molecular prognostic biomarker; genotype–phenotype correlation is weak given small numbers (CDH1 variants may be more severe than CTNND1 per PMID 28301459).

## 12. Treatment

**No disease-modifying, pharmacologic, gene, cell, or RNA therapy exists.** Management is **symptomatic, surgical, and multidisciplinary** (PMID 20073547).

- **Surgical / interventional:** Cleft lip repair (NCIT: Cleft Lip Repair) and cleft palate repair (Cleft Palate Repair) in infancy by a cleft team; **oculoplastic/ophthalmic surgery** for lagophthalmos, ectropion, euryblepharon, and distichiasis to protect the cornea; orthognathic surgery for Class III malocclusion.
- **Dental / prosthodontic:** Rehabilitation of oligodontia with **overdentures**, dental implants, orthodontics, and restorative care (PMID 20073547); NCIT: Dental Prosthesis, Dental Implant, Orthodontic Therapy.
- **Supportive / rehabilitative:** Ocular lubricants/moisture protection for exposure; **speech therapy** (NCIT: Speech Therapy); feeding support in infancy; audiology and ENT care; developmental/educational support where needed.
- **Pharmacotherapy / pharmacogenomics:** None specific. **Advanced/targeted therapeutics, immunotherapy, gene/cell/RNA therapy:** none approved or in trials for BCDS2 (no registered ClinicalTrials.gov interventional trials specific to this ultra-rare disorder). The GSK3β-inhibitor rescue of the CTNND1/Wnt axis (LiCl, CHIR-99021) is **experimental, cell/animal-level only** and specific to the FEVR context (PMID 35700046), not a human BCDS2 therapy.
- **Treatment strategy:** Coordinated craniofacial-team pathway (ophthalmology, plastic/oral-maxillofacial surgery, dentistry/orthodontics, speech-language pathology, cardiology, nephrology, clinical genetics) with staged interventions across childhood.
- **NCIT intervention concepts:** Cleft Lip Repair; Cleft Palate Repair; Oculoplastic Surgery; Dental Prosthesis/Overdenture; Dental Implant; Orthognathic Surgery; Speech Therapy; Genetic Counseling.

## 13. Prevention

- **Primary prevention:** Not possible for the genetic lesion. **Genetic counseling** (NCIT: Genetic Counseling) for recurrence-risk assessment (~50% for an affected parent) is central.
- **Secondary prevention / early detection:** **Prenatal diagnosis** (ultrasound + molecular testing with reverse phenotyping; PMID 39487033) and **preimplantation genetic testing (PGT-M)** where a familial variant is known; **cascade testing** of relatives. Early postnatal multidisciplinary evaluation (cardiac echo, renal ultrasound, ophthalmologic exam) for timely intervention.
- **Tertiary prevention:** Protecting the cornea (prevent exposure keratopathy), timely cleft/palate repair (speech/feeding), dental and orthodontic care, and surveillance of associated organ systems to prevent complications.
- **Immunization / public-health / environmental measures:** Not applicable (non-infectious, non-environmental).

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human CTNND1 (NCBI Gene 1500). Orthologs: mouse *Ctnnd1* (NCBI Gene 12388, MGI:105100), zebrafish *ctnnd1* (NCBI Gene 556726), *Xenopus* ctnnd1. p120-catenin is **highly evolutionarily conserved** across vertebrates, and the cadherin–catenin adhesion mechanism is deeply conserved.
- **Natural/veterinary disease:** No naturally occurring CTNND1 blepharocheilodontic syndrome is catalogued in companion animals or wildlife (not listed in OMIA as a spontaneous CTNND1 disorder). Disease knowledge derives from **engineered** models rather than natural animal disease.
- **Comparative biology:** Conditional/engineered loss of Cdh1/Ctnnd1 in mice reproduces eyelid, craniofacial, and tooth phenotypes reminiscent of human BCD (PMID 28301459), indicating conserved mechanism. **Zoonotic potential:** none (not an infectious disease).

## 15. Model Organisms

- **Mouse (Mus musculus, NCBI Taxon 10090):** The principal model. **Conditional knockouts** of *Ctnnd1* (and *Cdh1*) in relevant lineages recapitulate BCD-like eyelid, craniofacial, and tooth defects (PMID 28301459); **Ctnnd1 knockout mice recapitulate the cleft lip/palate spectrum** (PMID 29805042); **Wnt1-Cre; Ctnnd1^fl/fl** neural-crest ablation causes ocular anterior-segment dysgenesis (PMID 22736606). A 2026 **allelic series** separated p120 functions, showing cadherin stabilization is essential while RhoA/Kaiso binding is dispensable, and defined a cadherin adhesion threshold for lip fusion (PMID 41231213). Model type: mammalian, genetic (knockout/conditional/knock-in allelic series).
- **Xenopus:** **CRISPR/Cas9 targeting of ctnnd1** reproduced a subset of craniofacial/epithelial phenotypes and revealed additional mesenchymal roles (PMID 32196547).
- **Zebrafish (Danio rerio, NCBI Taxon 7955):** Functional assays of cadherin–catenin complex variants (used for CDH1 BCDS variants) support dominant impairment of adhesion (PMID 29348693).
- **In-vitro / cellular:** Human epithelial and endothelial cell lines and trabecular-meshwork cells used to show cadherin/β-catenin membrane loss and Wnt-axis effects (PMID 22736606; PMID 35700046).
- **Phenotype recapitulation & limitations:** Models reproduce clefting, eyelid/ocular, and tooth phenotypes well, validating the adhesion-threshold mechanism; limitations include incomplete modeling of the full human multisystem spectrum (e.g., human neurodevelopmental/genitourinary features) and species differences in facial morphogenesis. Resources: MGI, IMPC, ZFIN, Xenbase, Alliance of Genome Resources.

---

## Summary of Supported vs. Refuted Hypotheses

**Supported (evidence-backed):**
- BCDS2 is caused by heterozygous CTNND1 loss-of-function/truncating variants via haploinsufficiency (human cohorts + gnomAD constraint pLI=1.0, LOEUF=0.22).
- The core mechanism is destabilization of surface cadherins and failure of an actomyosin-dependent cadherin adhesion threshold required for craniofacial epithelial fusion (mouse allelic series, PMID 41231213).
- A secondary Wnt/β-catenin branch (p120 protects β-catenin from GSK3β-mediated degradation) contributes to CTNND1-related phenotypes (PMID 35700046).
- Dental and lower-eyelid features are near-fully penetrant; clefting ~67%; expression is variable (HPOA).

**Refuted / downgraded:**
- p120's RhoA- and Kaiso-binding (transcriptional repressor) functions are **not** the essential developmental mechanism — they are dispensable in vivo, with cadherin stabilization being crucial (PMID 41231213).
- A dominant-negative mechanism is **not** the model for CTNND1 (that applies to CDH1/BCDS1); CTNND1 acts by LoF/haploinsufficiency.

## Limitations and Future Directions
- Ultra-rare disease: small cohorts preclude robust genotype–phenotype correlation and precise frequency estimates; many "frequencies" derive from HPOA annotations on limited cases.
- No BCDS2-specific omics (transcriptomic/proteomic/metabolomic) or QoL datasets exist.
- The full extent of the expanding phenotype (cardiac, CNS, genitourinary, neurodevelopmental) needs prospective natural-history study.
- Mechanistic translation (e.g., whether modulating cadherin dosage or Wnt signaling could ever be preventive) remains experimental.

*Evidence types are indicated inline: human clinical (case series/cohorts), model organism (mouse/Xenopus/zebrafish), in vitro (cell lines), and computational (gnomAD constraint, ontology curation).*


## Artifacts

- [OpenScientist final report](Blepharocheilodontic_Syndrome_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Blepharocheilodontic_Syndrome_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.
