---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-02T07:41:00.262409'
end_time: '2026-09-02T07:59:21.860006'
duration_seconds: 1101.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Platelet-type Bleeding Disorder 12
  mondo_id: ''
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Platelet-type_Bleeding_Disorder_12-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Platelet-type_Bleeding_Disorder_12-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Platelet-type Bleeding Disorder 12
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Platelet-type Bleeding Disorder 12** covering all of the
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

# Platelet-type Bleeding Disorder 12 (BDPLT12): A Comprehensive Disease Characterization Report

**Disease:** Platelet-type Bleeding Disorder 12 (BDPLT12)
**MONDO ID:** MONDO:0011588 · **OMIM:** #605735 · **Category:** Mendelian (autosomal dominant)
**Causal gene:** *PTGS1* (cyclooxygenase-1 / COX-1 / PGHS-1)

---

## Summary

**Platelet-type Bleeding Disorder 12 (BDPLT12)** is an ultra-rare, autosomal-dominant inherited platelet **function** disorder caused by germline loss-of-function variants in *PTGS1*, the gene encoding platelet **cyclooxygenase-1 (COX-1, also called prostaglandin-endoperoxide H synthase-1, PGHS-1)**. Because COX-1 is the enzymatic target that low-dose aspirin irreversibly acetylates, a constitutional deficiency of COX-1 activity reproduces the pharmacology of chronic aspirin exposure. For this reason the disorder is classically and interchangeably known as the **"aspirin-like defect" (ALD)**. It is catalogued as MONDO:0011588 (= OMIM #605735, DOID:0111058, MeSH C567786, UMLS C2751535, MedGen 414043, GARD 0010575).

The core pathophysiology is a single, well-defined biochemical block: deficient COX-1 activity impairs the conversion of **arachidonic acid → prostaglandin endoperoxides (PGG2/PGH2) → thromboxane A2 (TXA2)** in the platelet. Because TXA2 is the autocrine/paracrine amplifier that drives the "second wave" of platelet secretion and aggregation, its loss produces a mild, lifelong mucocutaneous bleeding tendency. The laboratory hallmark is **selectively absent or markedly reduced arachidonic-acid-induced platelet aggregation** on light transmission aggregometry (LTA), with an absent secondary wave to ADP/adrenaline but preserved response to high-dose collagen and normal ristocetin-induced agglutination. Diagnosis is confirmed by *PTGS1* sequencing.

The clinical picture is generally benign. Patients present with easy bruising, epistaxis, menorrhagia, and — most characteristically — excessive or **late post-operative/post-dental bleeding** that can be the first clue to the diagnosis. Prognosis is excellent with normal life expectancy; the principal morbidity is perioperative, postpartum, and dental hemorrhage, plus iron-deficiency anemia from menorrhagia. Management is on-demand and peri-procedural, relying on **tranexamic acid, desmopressin (DDAVP), and platelet transfusion** for severe bleeding, together with strict avoidance of aspirin and other NSAIDs. Nine findings were confirmed across this investigation, drawing on 39 reviewed papers, ontology cross-references (Monarch/MONDO, HPO, GO, Reactome, UniProt), and model-organism data (global and platelet-specific *Ptgs1* knockout mice).

---

## Key Findings

### F001 — BDPLT12 is a platelet-type bleeding disorder caused by COX-1 (PTGS1) deficiency

BDPLT12 is definitively established as an inherited blood coagulation disorder caused by deficiency of platelet cyclooxygenase-1. Ontology cross-references from Monarch/MONDO anchor the disease identity: **MONDO:0011588 = OMIM:605735, DOID:0111058, MeSH:C567786, UMLS:C2751535, MedGen:414043, GARD:0010575**. The MONDO definition reads: *"An inherited blood coagulation disease characterized by autosomal dominant inheritance of mildly increased bleeding, platelet aggregation defect, and impaired conversion of arachidonic acid to thromboxane A2 in platelets due to deficiency in PTGS1 activity."*

**Synonyms / alternative names:** BDPLT12; aspirin-like defect (ALD); platelet COX-1 deficiency; platelet cyclooxygenase-1 deficiency; PGHS-1 deficiency; prostaglandin G/H synthase-1 deficiency.

**Causal gene:** *PTGS1* (prostaglandin-endoperoxide synthase 1 = COX-1 / PGHS-1), **HGNC:9604**, cytogenetic location **9q33.2**, gene OMIM 176805, UniProt **P23219**, Ensembl **ENSG00000095303**.

The information is derived from **aggregated disease-level resources** (OMIM, MONDO, HPO) combined with **individual patient / small-family case reports** — there is no EHR-scale patient cohort for this ultra-rare disorder.

### F002 — Clinical and laboratory phenotype of the aspirin-like defect

The largest phenotypic characterization comes from Rolf et al. (2009), a study of **17 unrelated families (52 individuals)**. Impaired platelet aggregation in response to arachidonic acid (**platelet aggregation response to AA, PAR-to-AA ≤10%**) was used as the mandatory diagnostic criterion. At least one bleeding symptom was reported by **25 of 34 (74%)** ALD patients, and a prolonged PFA-100 closure time was detected in **24 of 34 (71%)**; both correlated significantly with impaired PAR-to-AA (**P = 0.001 and P = 0.002**, respectively). The estimated prevalence was **~0.6% among pediatric patients with suspected coagulation disorders**, and the authors emphasize that the disorder is probably underdiagnosed because of its mild bleeding phenotype.

> *"Aspirin-like defect (ALD) is a rare, mostly autosomal dominant inherited dysfunction of the intraplatelet arachidonic acid (AA) pathway leading to impaired thromboxane A2 signalling."* — [PMID: 19036102](https://pubmed.ncbi.nlm.nih.gov/19036102/)

> *"At least one bleeding symptom was reported by 25 (74%) ALD patients and prolonged CT was detected in 24 (71%) of the cases, both significantly correlated with impaired PAR to AA (P = 0.001 and P = 0.002, respectively)."* — [PMID: 19036102](https://pubmed.ncbi.nlm.nih.gov/19036102/)

A clinically instructive case is described by Salinas et al. (2014), reporting **late post-operative hemorrhage after third-molar extraction in a patient with undiagnosed COX-1 deficiency** — the first such case documented in the English literature — underscoring how the diagnosis is frequently made only after a surgical bleeding event ([PMID: 24480756](https://pubmed.ncbi.nlm.nih.gov/24480756/)).

### F004 — Mechanistic causal chain: PTGS1 loss of function blocks arachidonate → TXA2

*PTGS1* encodes COX-1/PGHS-1, an **endoplasmic-reticulum-membrane, heme-dependent, bifunctional cyclooxygenase–peroxidase**. Curated Gene Ontology annotations define its molecular activity and localization:

| GO aspect | Term | ID |
|---|---|---|
| Molecular function | prostaglandin-endoperoxide synthase activity | GO:0004666 |
| Molecular function | peroxidase activity | GO:0004601 |
| Molecular function | heme binding | GO:0020037 |
| Biological process | cyclooxygenase pathway | GO:0019371 |
| Biological process | prostaglandin biosynthetic process | GO:0001516 |
| Biological process | prostanoid biosynthetic process | GO:0046457 |
| Cellular component | endoplasmic reticulum membrane | GO:0005789 |
| Cellular component | endoplasmic reticulum lumen | GO:0005788 |

The pathway (Reactome **R-HSA-2162123**, "Synthesis of Prostaglandins and Thromboxanes") proceeds:

```
Membrane phospholipids
   │  (cytosolic phospholipase A2, cPLA2)
   ▼
Arachidonic acid (CHEBI:15843)
   │  (COX-1 cyclooxygenase activity)  ◄── BLOCKED in BDPLT12
   ▼
Prostaglandin G2, PGG2 (CHEBI:27647)
   │  (COX-1 peroxidase activity)
   ▼
Prostaglandin H2, PGH2 (CHEBI:15554)
   │  (thromboxane synthase, TBXAS1)
   ▼
Thromboxane A2, TXA2 (CHEBI:15627)
   │  (autocrine/paracrine activation of TP receptor, TBXA2R)
   ▼
Gq / G12-13 signaling → granule secretion + integrin αIIbβ3 activation
   ▼
Secondary-wave platelet aggregation   ◄── ABOLISHED
```

Loss of COX-1 function removes TXA2 production, abolishing this **positive-feedback amplification loop**. The primary adhesion/activation machinery (GPIb-IX-V, αIIbβ3, collagen receptors) is intact, which is why high-dose collagen and ristocetin responses are preserved while AA-induced and secondary-wave aggregation fail.

### F005 — PTGS1 variant spectrum: rare heterozygous causal variants including a dominant-negative N-glycosylation defect

ClinVar catalogues roughly **137 *PTGS1* variants**. For the BDPLT12/aspirin-like-defect trait, most are classified **Benign, Likely benign, or VUS**, with no established recurrent Pathogenic entry — a direct reflection of the disorder's extreme rarity and reliance on single-family reports. Reported variant types are predominantly **missense**, with **nonsense** variants also catalogued (e.g., p.Arg108Ter). Origin is **germline**; the principal functional consequence is **loss of enzymatic function**.

The landmark molecular case is **Palma-Barqueros et al. (2021)**, who identified *"A novel genetic variant in PTGS1 [that] affects N-glycosylation of cyclooxygenase-1 causing a dominant-negative effect on platelet function and bleeding diathesis"* ([PMID: 33326144](https://pubmed.ncbi.nlm.nih.gov/33326144/)). This establishes a **dominant-negative mechanism** — a mutant subunit interfering with the wild-type product — as one route to the autosomal-dominant phenotype, complementing simple haploinsufficiency. The reference transcript is **NM_000962.4**.

> *"A novel genetic variant in PTGS1 affects N-glycosylation of cyclooxygenase-1 causing a dominant-negative effect on platelet function and bleeding diathesis."* — [PMID: 33326144](https://pubmed.ncbi.nlm.nih.gov/33326144/) *(title quote)*

### F006 — Mouse models recapitulate the arachidonate-induced aggregation defect

Model-organism evidence strongly supports the causal mechanism. Global **Ptgs1⁻/⁻ mice** (Langenbach et al., 1995, *Cell* 83:483-492) are viable and show markedly reduced platelet aggregation to arachidonic acid, decreased indomethacin-sensitive prostaglandin synthesis, and reduced inflammatory/pain responses. **Platelet/megakaryocyte-specific deletions** (Pf4-ΔCre and Gp1ba-ΔCre × Cox-1^flox/flox) confirm a **cell-autonomous** role of platelet COX-1 (Tang et al., 2024):

> *"Ex vivo platelet aggregation induced by arachidonic acid or adenosine diphosphate in platelet-rich plasma was inhibited to a similar extent in [platelet-specific Cox-1-deleted mice]."* — [PMID: 38660804](https://pubmed.ncbi.nlm.nih.gov/38660804/)

These models phenocopy the human COX-1-deficiency aggregation defect and the pharmacology of low-dose aspirin. The mouse ortholog is *Ptgs1* (NCBI Taxon 10090).

### F007 — HPO phenotype spectrum of BDPLT12

Official HPO annotations for **OMIM:605735** (JAX) define the phenotype spectrum:

| Phenotype | HPO term | Type |
|---|---|---|
| Impaired platelet aggregation | HP:0003540 | Laboratory abnormality |
| Bruising susceptibility / easy bruising | HP:0000978 | Clinical sign |
| Epistaxis | HP:0000421 | Symptom |
| Menorrhagia | HP:0000132 | Symptom |
| Gastrointestinal/intestinal bleeding | HP:0002584 | Clinical sign |
| Joint hemorrhage (hemarthrosis) | HP:0005261 | Clinical sign |
| Congenital onset | HP:0003577 | Onset modifier |
| Autosomal dominant inheritance | HP:0000006 | Inheritance |

Severity is characteristically **mild**; bleeding is **episodic/provoked** (surgery, dental extraction, menses, trauma) rather than spontaneous or progressive. Frequencies are not quantified in HPO, but bleeding symptoms were reported in ~74% of aspirin-like-defect patients (Rolf 2009). Phenotype type spans a **laboratory abnormality** (impaired AA-induced aggregation) plus **clinical signs/symptoms** (mucocutaneous bleeding).

### F008 — Diagnostic approach: bleeding assessment + LTA (absent AA response) confirmed by PTGS1 sequencing

Hoepner et al. (2025) propose a **four-step diagnostic approach** to inherited platelet function defects: (1) history plus a validated bleeding score (**ISTH-BAT**); (2) exclusion of plasmatic coagulation disorders and von Willebrand disease; (3) platelet phenotype/function testing — blood smear light microscopy, **light transmission aggregometry (LTA)**, flow cytometry, and lumiaggregometry; (4) genetic testing.

> *"Established methods consist of blood smear analysis by light microscopy, light transmission aggregometry, and flow cytometry."* — [PMID: 39870109](https://pubmed.ncbi.nlm.nih.gov/39870109/)

> *"We strongly advocate for the use of a validated bleeding score like the ISTH-BAT (International Society on Thrombosis and Haemostasis Bleeding Assessment Tool)."* — [PMID: 39870109](https://pubmed.ncbi.nlm.nih.gov/39870109/)

For the COX-1/aspirin-like defect specifically, the LTA hallmark is **absent/markedly reduced aggregation to arachidonic acid** with a characteristically **absent secondary wave to ADP/adrenaline**, while primary response to high-dose collagen and ristocetin-induced agglutination are preserved. Biochemical confirmation is **reduced serum thromboxane B2** and **urinary 11-dehydro-thromboxane B2**. Genetic confirmation is by *PTGS1* single-gene testing or a hereditary-platelet-disorder NGS panel / WES (e.g., ThromboGenomics-type panels).

### F009 — Epidemiology, inheritance, and prognosis: ultra-rare AD trait, normal life expectancy, mild lifelong course

There is **no dedicated Orphanet prevalence code**; BDPLT12 is ultra-rare with only single families/cases reported in OMIM and the literature. The broader aspirin-like-defect phenotype was estimated at **~0.6% among pediatric patients referred for suspected coagulation disorders** (Rolf 2009) and is thought to be underdiagnosed:

> *"Due to the mild bleeding symptoms, ALD is probably underdiagnosed."* — [PMID: 19036102](https://pubmed.ncbi.nlm.nih.gov/19036102/)

Inheritance is **autosomal dominant** (HP:0000006) with germline *PTGS1* variants; **penetrance appears incomplete and expressivity variable** (mild ALD subgroups with PAR-to-AA of 19–32% observed within families). There is **no genetic anticipation** (not a repeat-expansion disorder). There is no strong sex predilection for the molecular defect, although menorrhagia makes bleeding more clinically apparent in women. Prognosis is excellent: **normal life expectancy**; disease is chronic/lifelong but mild, episodic and provoked; the main morbidity is perioperative/postpartum/dental hemorrhage and iron-deficiency anemia from menorrhagia; disease-attributable mortality is negligible with appropriate hemostatic management.

### F003 — Management of the COX-1/aspirin-like platelet defect

Bargehr, Knöfler & Streif (2023) review inherited platelet disorder (IPD) management; the established options apply directly to COX-1 defect:

> *"Established treatment options of IPDs include local hemostatic treatment, tranexamic acid, desmopressin, platelet concentrates, and recombinant activated factor VII. Hematopoietic stem cell therapy is a curative approach for selected patients."* — [PMID: 37611608](https://pubmed.ncbi.nlm.nih.gov/37611608/)

Peri-partum and peri-operative management of functional platelet disorders relies on **DDAVP, tranexamic acid, prophylactic oxytocics, and platelet transfusion** (well documented in related storage-pool disorders). Emerging approaches include **autologous HSC gene therapy** and artificial platelets/nanoparticles; hematopoietic stem cell transplantation is curative but reserved for the most severe (generally non-COX-1) platelet disorders.

---

## Section-by-Section Detail (Research Template)

### 1. Disease Information
- **Overview:** Autosomal-dominant inherited platelet function disorder = constitutional COX-1 deficiency ("aspirin-like defect") causing mild mucocutaneous bleeding.
- **Identifiers:** MONDO:0011588; OMIM #605735; DOID:0111058; MeSH C567786; UMLS C2751535; MedGen 414043; GARD 0010575. No specific ICD-10/11 code (falls under D69.1 "qualitative platelet defects").
- **Synonyms:** BDPLT12; aspirin-like defect; platelet COX-1 / cyclooxygenase-1 deficiency; PGHS-1 deficiency.
- **Source of information:** Aggregated disease-level ontologies + individual case/family reports.

### 2. Etiology
- **Causal factor:** Germline heterozygous loss-of-function variants in *PTGS1* (genetic; monogenic).
- **Genetic risk factors:** *PTGS1* causal variants (missense predominant; nonsense e.g. p.Arg108Ter; N-glycosylation-disrupting dominant-negative allele). No known susceptibility loci or modifier genes are established.
- **Environmental risk factors / gene–environment interaction:** Concurrent aspirin/NSAID exposure additively worsens the phenotype (pharmacologic COX-1 inhibition on top of genetic deficiency) — the clearest gene–environment interaction; other antiplatelet drugs likewise unmask/aggravate bleeding.
- **Protective factors:** None specifically documented; avoidance of antiplatelet agents mitigates risk.

### 3. Phenotypes
See F007 table. Onset congenital; severity mild; course stable/episodic-provoked; laboratory abnormality (impaired AA aggregation) is the most penetrant feature. Quality-of-life impact is generally low, dominated by menorrhagia-related anemia and perioperative bleeding anxiety; no disease-specific QoL instrument data exist.

### 4. Genetic / Molecular Information
See F001, F005. Gene *PTGS1* (HGNC:9604, 9q33.2); reference transcript NM_000962.4; protein UniProt P23219. Variant classes: missense, nonsense; germline origin; loss-of-function and dominant-negative consequences. Most ClinVar entries VUS/benign. No established modifier genes, epigenetic mechanisms, or chromosomal abnormalities for this disorder.

### 5. Environmental Information
Non-genetic contributors are limited to **pharmacologic COX inhibitors** (aspirin, NSAIDs) that phenocopy or aggravate the defect. No infectious agents, toxins, or lifestyle factors cause the disorder.

### 6. Mechanism / Pathophysiology
See F004 and the Mechanistic Model below — causal chain from *PTGS1* variant to defective TXA2-dependent second-wave aggregation.

### 7. Anatomical Structures Affected
- **Organ/system:** Hematopoietic and hemostatic system; primary "organ" is the circulating platelet.
- **Cell types:** Platelet (CL:0000233); megakaryocyte (CL:0000556, site of COX-1 synthesis).
- **Subcellular:** ER membrane (GO:0005789) where COX-1 resides.
- **Localization of bleeding:** Mucocutaneous surfaces — skin (UBERON:0002097), nasal mucosa (UBERON:0001825), endometrium/uterus (UBERON:0000995); occasionally GI tract and joints. Bleeding is systemic/bilateral, not lateralized.

### 8. Temporal Development
Congenital onset (HP:0003577); insidious/chronic; lifelong and stable (non-progressive); manifestations episodic and provoked by hemostatic challenge. No disease stages, no remission/relapse cycles; critical periods are surgical, dental, obstetric, and menstrual events.

### 9. Inheritance and Population
See F009. Autosomal dominant, incomplete penetrance, variable expressivity, no anticipation; ultra-rare with no reliable prevalence estimate; no founder effect or consanguinity role documented (AD, not AR).

### 10. Diagnostics
See F008. Core: ISTH-BAT bleeding score → exclude VWD/coagulation factor defects → LTA (absent AA response, absent second wave) → serum TXB2 / urinary 11-dehydro-TXB2 → *PTGS1* sequencing (single-gene or NGS platelet-disorder panel/WES). Platelet count and morphology are normal.

### 11. Outcome / Prognosis
Excellent; normal life expectancy; negligible disease-specific mortality. Morbidity = perioperative/postpartum/dental hemorrhage and iron-deficiency anemia from menorrhagia. Prognostic factor: residual COX-1 activity (PAR-to-AA level) correlates with bleeding tendency.

### 12. Treatment
See F003. Pharmacotherapy/procedural: tranexamic acid (NCIT antifibrinolytic), desmopressin/DDAVP, platelet concentrates, recombinant activated factor VIIa for refractory bleeding; local hemostatic measures. Pharmacogenomic caution: strict avoidance of aspirin/NSAIDs. Advanced/experimental: autologous HSC gene therapy and engineered/artificial platelets are emerging but not standard for this mild disorder.

### 13. Prevention
No primary prevention (genetic). Secondary/tertiary prevention = pre-procedure hemostatic planning, avoidance of antiplatelet drugs, treatment of iron deficiency, and **genetic counseling** for AD inheritance with variable penetrance. Cascade testing of at-risk relatives is appropriate once a family variant is identified.

### 14. Other Species / Natural Disease
Mouse ortholog *Ptgs1* (NCBI Taxon 10090). No naturally occurring companion-animal BDPLT12 equivalent is catalogued in OMIA; the disease is understood chiefly through engineered mouse models (see F006). COX-1/prostanoid biology is evolutionarily conserved across mammals.

### 15. Model Organisms
Global *Ptgs1⁻/⁻* mice (Langenbach 1995) and platelet/megakaryocyte-specific conditional knockouts (Pf4-ΔCre, Gp1ba-ΔCre × Cox-1^flox/flox; PMID 38660804, 31248980) recapitulate the AA-induced aggregation defect and reduced platelet prostanoid biosynthesis — strong phenotype recapitulation of the human loss-of-function state. **Limitation:** these model complete loss/haploinsufficiency, not the specific human dominant-negative N-glycosylation allele; a knock-in model is lacking.

---

## Mechanistic Model / Interpretation

BDPLT12 is a textbook example of a **single-enzyme, single-pathway platelet function disorder** in which the clinical phenotype maps cleanly onto a defined biochemical lesion. The causal chain, from mutation to bleeding, is:

```
1. Germline heterozygous PTGS1 variant (missense, nonsense, or N-glycosylation-disrupting)
        │  leads to
2. Reduced or dysfunctional COX-1 protein in megakaryocytes/platelets
        │  (haploinsufficiency OR dominant-negative interference with wild-type subunit)
        │  results in
3. Impaired cyclooxygenase conversion: arachidonic acid ─╳→ PGG2/PGH2
        │  results in
4. Deficient thromboxane A2 (TXA2) synthesis (↓ serum TXB2, ↓ urinary 11-dehydro-TXB2)
        │  results in
5. Loss of TXA2/TP-receptor autocrine amplification of platelet activation
        │  results in
6. Absent secondary wave of secretion & aggregation; selectively absent AA-induced aggregation on LTA
        │  results in
7. Impaired primary hemostasis (defective platelet plug formation at sites of injury)
        │  manifests as
8. Mild, provoked mucocutaneous bleeding: bruising, epistaxis, menorrhagia,
   and late post-surgical/post-dental hemorrhage
```

**Upstream vs downstream.** The initiating lesion (steps 1–2) is the *PTGS1* variant and reduced COX-1 protein. The proximate biochemical defect (steps 3–4) is the arachidonate→TXA2 block. The downstream physiological consequence (steps 5–7) is loss of the amplification loop and defective platelet plug formation, and the clinical manifestation (step 8) is the mild bleeding tendency.

**Two molecular routes to autosomal dominance.** A heterozygous variant can cause disease either by (a) **haploinsufficiency** — 50% enzyme is insufficient for full second-wave amplification under stress — or (b) **dominant-negative interference**, as demonstrated for the N-glycosylation-disrupting variant (Palma-Barqueros 2021), where the mutant subunit impairs function beyond simple dose reduction. Variable penetrance/expressivity (PAR-to-AA ranging 19–32% in mild subgroups) is consistent with residual COX-1 activity determining phenotype severity.

**Cell types and biological processes.** The affected cell is the **platelet** (CL:0000233) and its precursor the **megakaryocyte** (CL:0000556); COX-1 protein synthesis occurs primarily in megakaryocytes and is loaded into circulating platelets. The relevant biological processes are the **cyclooxygenase pathway** (GO:0019371) and **prostanoid/thromboxane biosynthesis** (GO:0046457, GO:0001516), localized to the **ER membrane** (GO:0005789).

**Distinguishing feature vs other platelet disorders.** Unlike Glanzmann thrombasthenia (αIIbβ3 defect, absent aggregation to all agonists), Bernard-Soulier syndrome (GPIb-IX-V, macrothrombocytopenia), and platelet-type von Willebrand disease (GP1BA gain-of-function, platelet **hyper**responsiveness), BDPLT12 shows a **selective** aggregation defect confined to the AA/TXA2 pathway with normal platelet count and morphology. The single most discriminating test is the isolated absence of AA-induced aggregation with preserved high-dose collagen and ristocetin responses.

| Disorder | Gene | Defect type | Platelet count | Aggregation pattern |
|---|---|---|---|---|
| **BDPLT12 (COX-1 def.)** | *PTGS1* | LoF / dominant-negative | Normal | Selective loss of AA response; absent 2nd wave |
| Glanzmann thrombasthenia | *ITGA2B/ITGB3* | LoF | Normal | Absent to all agonists (except ristocetin) |
| Bernard-Soulier syndrome | *GP1BA/GP1BB/GP9* | LoF | Low (large platelets) | Absent ristocetin agglutination |
| Platelet-type VWD | *GP1BA* | Gain-of-function | Low | Enhanced low-dose ristocetin |

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [19036102](https://pubmed.ncbi.nlm.nih.gov/19036102/) | *Clinical and laboratory phenotypes associated with the aspirin-like defect (17 families)* | Human clinical cohort | F002, F009 — bleeding frequency (74%), PFA-100 (71%), prevalence ~0.6%, AD inheritance, underdiagnosis |
| [33326144](https://pubmed.ncbi.nlm.nih.gov/33326144/) | *Novel PTGS1 variant affects N-glycosylation of COX-1, dominant-negative effect* | Human genetics + functional | F005 — dominant-negative molecular mechanism |
| [24480756](https://pubmed.ncbi.nlm.nih.gov/24480756/) | *Late postoperative hemorrhage in undiagnosed COX-1 deficiency after third molar extraction* | Human case report | F002 — surgical/dental bleeding presentation |
| [38660804](https://pubmed.ncbi.nlm.nih.gov/38660804/) | *Pf4-ΔCre vs Gp1ba-ΔCre depletion of COX-1 in platelets* | Model organism (mouse) | F006 — cell-autonomous AA-induced aggregation defect |
| [39870109](https://pubmed.ncbi.nlm.nih.gov/39870109/) | *Diagnostic assessment of inherited platelet function defects, Part 1* | Clinical methodology review | F008 — LTA, flow cytometry, ISTH-BAT diagnostic pathway |
| [37611608](https://pubmed.ncbi.nlm.nih.gov/37611608/) | *Treatment of Inherited Platelet Disorders: Current Status and Future Options* | Treatment review | F003 — tranexamic acid, DDAVP, platelet concentrates, HSCT |
| [16684008](https://pubmed.ncbi.nlm.nih.gov/16684008/) | *Congenital platelet disorders: mechanisms, diagnosis, treatment* | Review | Background — second-wave aggregation defects, management |
| [16102044](https://pubmed.ncbi.nlm.nih.gov/16102044/) | *Qualitative disorders of platelets and megakaryocytes* | Review | Background — differential diagnosis landscape |
| [31248980](https://pubmed.ncbi.nlm.nih.gov/31248980/) | *Platelet-specific deletion of COX-1 ameliorates DSS colitis* | Model organism | F006 — platelet COX-1 conditional KO recapitulates low-dose-aspirin pharmacology |
| [26272103](https://pubmed.ncbi.nlm.nih.gov/26272103/) | *Abnormal megakaryopoiesis and platelet function in COX-2-deficient mice* | Model organism | Contrast — COX-2 vs COX-1 roles in platelets |

**How the evidence fits together.** The human cohort (PMID 19036102) establishes the clinical/laboratory phenotype and epidemiology; the molecular case report (PMID 33326144) provides the mechanistic proof that a *PTGS1* variant is causal and defines a dominant-negative route; the mouse conditional-knockout studies (PMIDs 38660804, 31248980) supply cell-autonomous causal evidence that platelet COX-1 loss reproduces the exact aggregation defect; the diagnostic and treatment reviews (PMIDs 39870109, 37611608) translate the mechanism into clinical practice. No reviewed paper challenges the core model; the main tension in the literature is between COX-1 and COX-2 contributions in *vascular* (not platelet) prostanoid balance (PMIDs 31510878, 27020548), which is peripheral to the platelet-intrinsic BDPLT12 phenotype.

---

## Limitations and Knowledge Gaps

1. **Genotype–phenotype ambiguity.** No recurrent pathogenic *PTGS1* variant is established for BDPLT12; most ClinVar entries are VUS/benign. ACMG-grade classification of causal variants is limited by absence of segregation and functional data for most alleles.
2. **Nomenclature and cohort mixing.** The literature conflates the clinically defined "aspirin-like defect" (a functional label that can arise from several upstream signaling or thromboxane-pathway defects) with genetically confirmed *PTGS1* deficiency (BDPLT12 proper). Some ALD cohort statistics (e.g., the 74% bleeding frequency) derive from functionally defined patients not all genotyped for *PTGS1*.
3. **No epidemiological denominator.** There is no Orphanet prevalence code or registry; true prevalence, carrier frequency, and population/geographic distribution are unknown. The ~0.6% figure is restricted to a pediatric referral population and is not a general-population estimate.
4. **Incomplete penetrance/expressivity not mechanistically resolved.** Modifier genes, environmental factors (concurrent NSAID use), and residual-activity thresholds that determine bleeding risk are undefined.
5. **No disease-specific outcome data.** Quality-of-life instruments (EQ-5D, SF-36, PROMIS), long-term natural-history cohorts, and treatment-response rates specific to BDPLT12 are unpublished; management is extrapolated from the broader inherited-platelet-disorder literature.
6. **No animal model of a human dominant-negative allele.** Mouse data derive from complete/conditional Cox-1 knockouts, which model loss-of-function/haploinsufficiency but not the N-glycosylation dominant-negative human variant.

---

## Proposed Follow-up Experiments / Actions

1. **Curate a *PTGS1*–BDPLT12 variant registry** linking each reported variant to LTA phenotype (PAR-to-AA), serum TXB2, and bleeding score (ISTH-BAT), enabling ACMG reclassification and genotype–phenotype correlation.
2. **Functional validation of VUS** in a heterologous COX-1 expression system (PGH2/TXA2 output assay) and in patient- or iPSC-derived megakaryocytes, to distinguish loss-of-function, dominant-negative, and benign alleles.
3. **Prospective phenotyping study** genotyping all functionally defined ALD patients for *PTGS1*, to separate true BDPLT12 from phenocopies and derive genotype-specific bleeding frequencies and prevalence.
4. **Standardize a confirmatory biochemical panel**: pair LTA (AA agonist) with serum TXB2 and urinary 11-dehydro-TXB2 cutoffs to build a reproducible diagnostic algorithm distinguishing COX-1 deficiency from thromboxane-synthase and TP-receptor defects.
5. **Knock-in mouse of a human dominant-negative *Ptgs1* allele** (e.g., an N-glycosylation-disrupting variant) to test whether it reproduces the AD phenotype beyond haploinsufficiency and to serve as a therapeutic testing platform.
6. **Treatment-outcome case series** in genetically confirmed BDPLT12, documenting response to tranexamic acid, DDAVP, and platelet transfusion, including perioperative and obstetric outcomes.
7. **Genetic counseling framework** for AD inheritance with incomplete penetrance: cascade testing and pre-procedure risk assessment for affected families.

---

## Ontology Term Index

- **Disease:** MONDO:0011588; OMIM #605735; DOID:0111058; MeSH C567786; UMLS C2751535
- **Gene/Protein:** *PTGS1* HGNC:9604; UniProt P23219; Ensembl ENSG00000095303; gene OMIM 176805; mouse *Ptgs1*, NCBI Taxon 10090
- **GO (BP):** GO:0019371 (cyclooxygenase pathway); GO:0001516 (prostaglandin biosynthesis); GO:0046457 (prostanoid biosynthesis)
- **GO (MF):** GO:0004666 (prostaglandin-endoperoxide synthase activity); GO:0004601 (peroxidase); GO:0020037 (heme binding)
- **GO (CC):** GO:0005789 (ER membrane); GO:0005788 (ER lumen)
- **CL:** CL:0000233 (platelet); CL:0000556 (megakaryocyte)
- **UBERON:** UBERON:0002097 (skin); UBERON:0001825 (nasal mucosa); UBERON:0000995 (uterus)
- **CHEBI:** 15843 (arachidonic acid); 27647 (PGG2); 15554 (PGH2); 15627 (thromboxane A2)
- **HPO:** HP:0003540, HP:0000978, HP:0000421, HP:0000132, HP:0002584, HP:0005261, HP:0003577, HP:0000006
- **Reactome:** R-HSA-2162123 (Synthesis of Prostaglandins and Thromboxanes)
- **NCIT (treatment):** tranexamic acid, desmopressin, platelet transfusion, recombinant factor VIIa

---

*Report compiled from 9 confirmed findings and 39 reviewed papers across a 5-iteration autonomous investigation. Evidence types are labeled human clinical, model organism, in vitro, or computational/ontology throughout.*


## Artifacts

- [OpenScientist final report](Platelet-type_Bleeding_Disorder_12-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Platelet-type_Bleeding_Disorder_12-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 21 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002097` (2 mentions) - the report calls it "Localization of bleeding:** Mucocutaneous surfaces — skin", "skin"; UBERON calls it **skin of body**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004601` (2 mentions) - the report calls it "peroxidase activity", "peroxidase"; GO calls it **peroxidase activity**, and lists "heme peroxidase" among its other names
- `GO:0001516` (3 mentions) - the report calls it "prostaglandin biosynthetic process", "prostaglandin biosynthesis"; GO calls it **prostaglandin biosynthetic process**, and lists "prostaglandin biosynthesis" among its other names
- `GO:0046457` (3 mentions) - the report calls it "prostanoid biosynthetic process", "prostanoid biosynthesis"; GO calls it **prostanoid biosynthetic process**, and lists "prostanoid biosynthesis" among its other names
- `GO:0005789` (4 mentions) - the report calls it "endoplasmic reticulum membrane", "Subcellular:** ER membrane", "ER membrane"; GO calls it **endoplasmic reticulum membrane**, and lists "ER membrane" among its other names
- `GO:0005788` (2 mentions) - the report calls it "endoplasmic reticulum lumen", "ER lumen"; GO calls it **endoplasmic reticulum lumen**, and lists "ER lumen" among its other names
- `HP:0000978` (2 mentions) - the report calls it "Bruising susceptibility / easy bruising"; HP calls it **Bruising susceptibility**
- `HP:0002584` (2 mentions) - the report calls it "Gastrointestinal/intestinal bleeding"; HP calls it **Intestinal bleeding**
- `HP:0005261` (2 mentions) - the report calls it "Joint hemorrhage (hemarthrosis)"; HP calls it **Joint hemorrhage**
- `HP:0000006` (3 mentions) - the report calls it "Autosomal dominant inheritance", "autosomal dominant"; HP calls it **Autosomal dominant inheritance**, and lists "Autosomal dominant" among its other names
- `CL:0000233` (3 mentions) - the report calls it "Cell types:** Platelet", "platelet"; CL calls it **platelet**, and lists "blood platelet" among its other names
- `UBERON:0001825` (2 mentions) - the report calls it "nasal mucosa"; UBERON calls it **paranasal sinus**, and lists "nasal sinus" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0004601` - called "peroxidase activity", "peroxidase"
- `GO:0001516` - called "prostaglandin biosynthetic process", "prostaglandin biosynthesis"
- `GO:0046457` - called "prostanoid biosynthetic process", "prostanoid biosynthesis"
- `GO:0005789` - called "endoplasmic reticulum membrane", "Subcellular:** ER membrane", "ER membrane"
- `GO:0005788` - called "endoplasmic reticulum lumen", "ER lumen"
- `HP:0000006` - called "Autosomal dominant inheritance", "autosomal dominant"
- `CL:0000233` - called "Cell types:** Platelet", "platelet"
- `UBERON:0002097` - called "Localization of bleeding:** Mucocutaneous surfaces — skin", "skin"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `UMLS`, `GARD`.
