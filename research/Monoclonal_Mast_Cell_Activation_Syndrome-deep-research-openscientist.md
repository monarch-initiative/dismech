---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T14:40:20.397611'
end_time: '2026-09-03T15:35:25.669167'
duration_seconds: 3305.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: monoclonal mast cell activation syndrome
  mondo_id: MONDO:0033954
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
citation_count: 23
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Monoclonal_Mast_Cell_Activation_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Monoclonal_Mast_Cell_Activation_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** monoclonal mast cell activation syndrome
- **MONDO ID:** MONDO:0033954 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **monoclonal mast cell activation syndrome** covering all of the
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

# Monoclonal Mast Cell Activation Syndrome (MMAS) — Comprehensive Disease Characterization Report

**Disease:** Monoclonal mast cell activation syndrome (MMAS)
**MONDO ID:** MONDO:0033954
**Template category:** Listed as "Mendelian," but see the important caveat in the Summary — the driver lesion is somatic, not germline.

---

## Summary

Monoclonal mast cell activation syndrome (MMAS) is a rare, **adult-onset, primary (clonal) mast cell activation syndrome (MCAS)** in which patients experience recurrent, often severe, mast-cell mediator-release symptoms — most characteristically hypotensive anaphylaxis — together with laboratory demonstration of **mast-cell clonality**, but who **do not fulfill the full World Health Organization (WHO) criteria for systemic mastocytosis (SM)**. Clonality is established by detection of the somatic **KIT D816V** gain-of-function mutation and/or aberrant mast-cell expression of **CD25** (±CD2/CD30), while the patient carries fewer than the required number of minor SM criteria and lacks the major criterion (multifocal dense mast-cell aggregates in bone marrow) [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/), [PMID: 34298172](https://pubmed.ncbi.nlm.nih.gov/34298172/).

Mechanistically, MMAS sits on the same biological continuum as SM but at the **lowest clonal-burden end**. An acquired KIT D816V lesion constitutively activates downstream STAT5, PI3K and MAPK signaling, driving persistent pro-inflammatory output (e.g., IL-6) and, critically, **lowering the mast-cell activation threshold** so that ordinary triggers — above all Hymenoptera (bee/wasp) venom — precipitate severe, cardiovascular-dominant, characteristically **urticaria-poor** anaphylaxis, predominantly in males [PMID: 30948489](https://pubmed.ncbi.nlm.nih.gov/30948489/), [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/), [PMID: 42542541](https://pubmed.ncbi.nlm.nih.gov/42542541/). Because KIT D816V alone is insufficient for full neoplastic transformation, MMAS clones remain sub-threshold and rarely progress [PMID: 34424959](https://pubmed.ncbi.nlm.nih.gov/34424959/).

An important classification caveat: **despite the "Mendelian" template label, MMAS is not an inherited Mendelian disease.** The driver KIT D816V is a **somatic** (acquired) mutation restricted to the hematopoietic/mast-cell lineage. The one bona fide germline genetic contributor is **hereditary alpha-tryptasemia (HAT)** — increased *TPSAB1* copy number — which is an autosomal-dominant *modifier* that amplifies anaphylaxis severity but does not cause MMAS [PMID: 37818990](https://pubmed.ncbi.nlm.nih.gov/37818990/), [PMID: 41932753](https://pubmed.ncbi.nlm.nih.gov/41932753/). Prognosis is favorable, with recurrent life-threatening anaphylaxis (rather than clonal progression) constituting the principal morbidity; management centers on anti-mediator therapy, anaphylaxis prevention (epinephrine plus venom immunotherapy), and osteoporosis surveillance, with selective KIT inhibitors reserved for refractory cases [PMID: 40274818](https://pubmed.ncbi.nlm.nih.gov/40274818/), [PMID: 39187156](https://pubmed.ncbi.nlm.nih.gov/39187156/).

---

## 1. Disease Information

**Overview.** MMAS is a subtype of **primary (clonal) MCAS**. MCAS as a whole is defined by episodic, multisystem mast-cell mediator-release symptoms, an objective transient rise in a validated mast-cell mediator (typically serum tryptase), and symptomatic response to mediator-targeting therapy. MCAS is divided into **primary (monoclonal/clonal), secondary, and idiopathic** forms. MMAS is the primary/monoclonal form in which clonal mast cells are demonstrable but do not meet the diagnostic bar for systemic mastocytosis [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/), [PMID: 34298172](https://pubmed.ncbi.nlm.nih.gov/34298172/).

> "These MC activation syndromes (MCAS) can be divided into primary (monoclonal) MCAS (MMAS) vs. secondary and idiopathic MCAS." — [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/)

> "In contrast to clonal MCAS in which MCA is associated with a primary MC disorder (ie, primary MCAS) such as mastocytosis or monoclonal MCAS, nonclonal MCAS can be secondary to known or unidentified triggers." — [PMID: 34298172](https://pubmed.ncbi.nlm.nih.gov/34298172/)

**Key identifiers.**
- **Mondo:** MONDO:0033954
- **ICD-10-CM:** Mast cell activation disorders, including MMAS, have been assigned ICD-10-CM codes under the ECNM–AIM consortium global classification [PMID: 35623575](https://pubmed.ncbi.nlm.nih.gov/35623575/).
- **OMIM / Orphanet:** No dedicated Mendelian OMIM phenotype entry exists for MMAS because the driver is somatic; the related entity systemic mastocytosis is catalogued separately. (Not applicable as an inherited-disease OMIM phenotype.)
- **MeSH:** Best mapped under "Mastocytosis" / "Mast Cell Activation Syndrome" concepts.

> "some of these conditions have recently been assigned to an International Classification of Diseases-10-Clinical Modification code (ICD-10-CM)." — [PMID: 35623575](https://pubmed.ncbi.nlm.nih.gov/35623575/)

**Synonyms / alternative names.** Monoclonal MCAS; mono(clonal) mast cell activation syndrome; primary MCAS (non-mastocytosis clonal subtype); clonal MCAS without SM. In older literature it overlaps with "other clonal mast cell activation disorders (c-MCAD)" that do not meet WHO SM criteria [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/).

**Information source.** Knowledge is derived from **aggregated disease-level clinical cohorts and reference-center case series** (e.g., REMA, ECNM registries; diagnostic work-up cohorts) rather than a single EHR or a Mendelian gene–disease catalogue.

---

## 2. Etiology

**Primary causal factor (genetic, somatic).** MMAS is caused by an **acquired, somatic gain-of-function point mutation in *KIT*, most commonly D816V** (a substitution in codon 816 of exon 17), arising in the hematopoietic/mast-cell lineage. This is a driver of mast-cell clonality, not an inherited variant [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/), [PMID: 34298172](https://pubmed.ncbi.nlm.nih.gov/34298172/).

**Genetic risk / modifier factors.**
- **Hereditary alpha-tryptasemia (HAT)** — germline increased copy number of *TPSAB1* (α-tryptase). HAT is autosomal dominant, present in ~4–6% of the general population, and is enriched among clonal and non-clonal MCAS and mastocytosis patients; it independently amplifies anaphylaxis severity [PMID: 37818990](https://pubmed.ncbi.nlm.nih.gov/37818990/), [PMID: 41932753](https://pubmed.ncbi.nlm.nih.gov/41932753/).

**Environmental / triggering factors.** MMAS itself is not caused by environmental exposures, but mediator-release episodes are **triggered** by:
- **Hymenoptera venom** (bee/wasp stings) — the single most characteristic trigger [PMID: 40641447](https://pubmed.ncbi.nlm.nih.gov/40641447/), [PMID: 39187156](https://pubmed.ncbi.nlm.nih.gov/39187156/)
- Idiopathic/allergen-induced triggers, drugs, physical stimuli, and other IgE-independent activators.

**Demographic risk factors.** Male sex and adult onset are associated with the clonal phenotype [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/).

**Protective factors.** No specific genetic or environmental protective factors have been established for MMAS. (Data not available.)

**Gene–environment interaction.** The core gene–environment interaction is that the **KIT D816V clone lowers the mast-cell activation threshold**, so that an environmental trigger (venom) that would be benign in a normal individual produces severe anaphylaxis. Co-inherited HAT (germline *TPSAB1* duplication) further potentiates this interaction [PMID: 42542541](https://pubmed.ncbi.nlm.nih.gov/42542541/), [PMID: 41932753](https://pubmed.ncbi.nlm.nih.gov/41932753/).

---

## 3. Phenotypes

MMAS produces **episodic, multisystem mediator-release symptoms**. The full MCAS symptom spectrum spans skin, gastrointestinal, cardiovascular, respiratory and neurologic systems [PMID: 25944644](https://pubmed.ncbi.nlm.nih.gov/25944644/):

> "episodic symptoms with mast cell mediators affecting two or more organ systems with urticaria, angioedema, flushing, nausea, vomiting, diarrhea, abdominal cramping, hypotensive syncope, tachycardia, wheezing, conjunctival injection, pruritus, nasal stuffiness." — [PMID: 25944644](https://pubmed.ncbi.nlm.nih.gov/25944644/)

**Distinctive MMAS phenotype.** Clonal (monoclonal) MCAS characteristically skews toward **isolated hypotensive/cardiovascular anaphylaxis** and, importantly, **lacks the mucocutaneous signs (urticaria/angioedema) that dominate idiopathic MCAS**. In a 703-patient cohort, mucocutaneous symptoms were significantly less prevalent in clonal MCAS (P = .015) [PMID: 38056692](https://pubmed.ncbi.nlm.nih.gov/38056692/).

> "these symptoms were less prevalent in patients with clonal MCAS (P = .015)." — [PMID: 38056692](https://pubmed.ncbi.nlm.nih.gov/38056692/)

| Phenotype | Type | HPO suggestion | Characteristics in MMAS |
|---|---|---|---|
| Anaphylaxis (recurrent, severe) | Clinical sign / event | HP:0100845 (Anaphylaxis) | Adult-onset; episodic; often severe/life-threatening; principal morbidity |
| Hypotension / syncope / presyncope | Clinical sign | HP:0002615; HP:0001279 | Cardiovascular-dominant; predictive of clonality |
| Flushing | Symptom | HP:0031284 | Episodic |
| Absence of urticaria/angioedema | Distinguishing feature | (absence of HP:0200025 / HP:0100665) | Characteristic of clonal vs idiopathic MCAS |
| GI symptoms (nausea, vomiting, diarrhea, cramping) | Symptom | HP:0002018; HP:0002014 | Variable, episodic |
| Elevated basal serum tryptase | Laboratory abnormality | Abnormal circulating tryptase | Higher in clonal than non-clonal MCAD |
| Osteoporosis | Physical manifestation | HP:0000939 | Comorbidity requiring surveillance |

**Onset / severity / progression / frequency.** Adult-onset; severity ranges from moderate to life-threatening; course is **episodic/fluctuating** (attacks separated by relatively asymptomatic intervals); frequency of the cardiovascular/insect-trigger phenotype is enriched in clonal patients versus non-clonal MCAD [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/).

**Quality-of-life impact.** Recurrent unpredictable anaphylaxis imposes substantial anxiety, activity restriction, and burden; disease-specific PROMs and general instruments (SF-12, SF-36) capture mediator-symptom burden in clonal mast-cell disease, and mediator symptoms improve with effective therapy [PMID: 32437738](https://pubmed.ncbi.nlm.nih.gov/32437738/). (Direct MMAS-specific QoL datasets are limited.)

---

## 4. Genetic / Molecular Information

**Causal gene.** ***KIT*** (HGNC:6342; NCBI Gene 3815; UniProt P10721), encoding the type-III receptor tyrosine kinase / stem cell factor receptor (CD117).

**Pathogenic variant.**
- **KIT D816V** — activating missense point mutation in codon 816 of exon 17. This is the canonical minor SM criterion and the molecular hallmark of clonality in MMAS. In MMAS the mutant allele burden is very **low** (e.g., 0.007–9% mutated cells in one series), so highly sensitive detection (allele-specific PCR on purified mast cells) is mandatory [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/).
- **Variant classification:** Pathogenic (activating, gain-of-function).
- **Variant type:** Missense (single-nucleotide substitution).
- **Somatic vs germline:** **Somatic** (acquired in the mast-cell/hematopoietic lineage). This is why MMAS is not inherited despite the template's "Mendelian" label [PMID: 34298172](https://pubmed.ncbi.nlm.nih.gov/34298172/).
- **Functional consequence:** **Gain of function** — constitutive, ligand-independent kinase activation.

> "the KIT D816V mutation was detected in all SM patients but in only 2 patients with MMAS." — [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/)

**Aberrant surface phenotype (second clonality marker).** Aberrant expression of **CD25** (±CD2/CD30) on bone-marrow mast cells is a minor SM criterion and was present in all SM and MMAS patients in a diagnostic work-up cohort [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/).

> "Flow cytometric analysis of bone marrow showed CD25 expression of MCs in all patients with SM and MMAS." — [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/)

**Germline modifier gene.** ***TPSAB1*** — increased α-tryptase copy number causes **hereditary alpha-tryptasemia (HAT)**, an autosomal-dominant trait that raises basal tryptase and amplifies anaphylaxis severity [PMID: 37818990](https://pubmed.ncbi.nlm.nih.gov/37818990/), [PMID: 41932753](https://pubmed.ncbi.nlm.nih.gov/41932753/).

**Additional somatic mutations.** Multi-mutated disease (e.g., *SRSF2*, *ASXL1*, *RUNX1*, *NRAS*) characterizes **advanced** SM and confers poor prognosis; these are generally **absent** in low-burden MMAS, consistent with its indolent behavior [PMID: 34424959](https://pubmed.ncbi.nlm.nih.gov/34424959/), [PMID: 38142424](https://pubmed.ncbi.nlm.nih.gov/38142424/).

**Epigenetic / chromosomal abnormalities.** No MMAS-specific epigenetic signature or recurrent chromosomal abnormality is established. (Data not available.)

---

## 5. Environmental Information

- **Environmental / occupational toxins:** No causal environmental toxin identified for MMAS. (Not applicable.)
- **Lifestyle factors:** No established causal lifestyle factors. Trigger avoidance (e.g., avoiding known drug/physical triggers) is relevant to episode prevention rather than disease causation.
- **Infectious agents:** None implicated in causation.
- **Key trigger (environmental precipitant of episodes):** **Hymenoptera venom** is the dominant precipitant of anaphylactic episodes in clonal mast-cell disease/MMAS [PMID: 40641447](https://pubmed.ncbi.nlm.nih.gov/40641447/).

> "The clinical presentation of anaphylaxis after stinging -cardiovascular symptoms and absence of cutaneous- may point to a clonal mast cell disease." — [PMID: 40641447](https://pubmed.ncbi.nlm.nih.gov/40641447/)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **somatic KIT D816V gain-of-function mutation** arises in the mast-cell/hematopoietic lineage → **leads to** ligand-independent, constitutive activation of the KIT receptor tyrosine kinase.
2. Constitutive KIT activity → **results in** persistent activation of downstream **STAT5, PI3K, and MEK/ERK (MAPK)** signaling (STAT5A/B activation mediated via JAK2 and MEK/ERK1/2), demonstrated in mast-cell lines [PMID: 30948489](https://pubmed.ncbi.nlm.nih.gov/30948489/).
3. This aberrant signaling → **leads to** a survival/clonal-advantage program and **persistent pro-inflammatory output** (e.g., constitutive IL-6 production) [PMID: 30948489](https://pubmed.ncbi.nlm.nih.gov/30948489/).
4. Because KIT D816V **alone is insufficient** for full neoplastic transformation (cooperating pathways such as Hedgehog/GLI3 and TNF–survivin are required), the clone expands only modestly → **results in** a **low clonal burden that remains below the WHO SM threshold** (no dense multifocal aggregates) [PMID: 34424959](https://pubmed.ncbi.nlm.nih.gov/34424959/), [PMID: 38142424](https://pubmed.ncbi.nlm.nih.gov/38142424/).
5. The clonal mast cells nonetheless carry a **lowered activation threshold** → **leads to** hyper-releasability upon encountering a trigger [PMID: 42542541](https://pubmed.ncbi.nlm.nih.gov/42542541/).
6. **Branch point — trigger:** Hymenoptera venom / idiopathic / IgE-independent stimuli (e.g., via **MRGPRX2**) → **result in** explosive degranulation and release of tryptase, histamine, PAF, prostaglandin D2 and other mediators [PMID: 42542541](https://pubmed.ncbi.nlm.nih.gov/42542541/).
7. Systemic mediator release → **leads to** vasodilation, increased vascular permeability and smooth-muscle effects → **results in** the clinical manifestation: **cardiovascular-dominant, urticaria-poor anaphylaxis** (hypotension, syncope) [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/), [PMID: 38056692](https://pubmed.ncbi.nlm.nih.gov/38056692/).
8. **Modifier branch:** Co-inherited **germline HAT (*TPSAB1* duplication)** → **amplifies** basal tryptase and reaction severity, worsening step 7 [PMID: 41932753](https://pubmed.ncbi.nlm.nih.gov/41932753/).

### Supporting detail

> "aberrant KIT activity and signaling are critical for the induction of IL-6 and involve STAT5 and PI3K pathways but not STAT3 or STAT4." — [PMID: 30948489](https://pubmed.ncbi.nlm.nih.gov/30948489/)

> "mast cell lines expressing D816V-KIT, but not those expressing normal KIT or other KIT variants, produced constitutively high IL-6 amounts at the message and protein levels." — [PMID: 30948489](https://pubmed.ncbi.nlm.nih.gov/30948489/)

> "clonal mast cell disorders-including systemic mastocytosis and monoclonal mast cell activation syndrome-are now recognized as major risk amplifiers for severe and fatal anaphylaxis, particularly following Hymenoptera venom exposure, reinforcing the role of the KIT D816V mutation in lowering the mast cell activation threshold." — [PMID: 42542541](https://pubmed.ncbi.nlm.nih.gov/42542541/)

> "attempts to demonstrate its oncogenic effect alone have repeatedly failed, suggesting that additional pathways are involved in MC transformation." — [PMID: 34424959](https://pubmed.ncbi.nlm.nih.gov/34424959/)

**Upstream vs downstream.** Upstream = somatic KIT D816V. Intermediate = STAT5/PI3K/MAPK signaling, IL-6, lowered activation threshold, MRGPRX2-mediated releasability. Downstream = mediator release → anaphylaxis. HAT is a parallel germline amplifier.

**Ontology suggestions.**
- **GO biological processes:** mast cell activation (GO:0045576); mast cell degranulation (GO:0043303); transmembrane receptor protein tyrosine kinase signaling pathway (GO:0007169); STAT cascade / JAK-STAT (GO:0007259); positive regulation of inflammatory response (GO:0050729).
- **CL cell types:** mast cell (CL:0000097); connective tissue / mucosal mast cell subsets; hematopoietic stem cell (CL:0000037) as the mutation-origin compartment.
- **CHEBI mediators:** histamine (CHEBI:18295); prostaglandin D2 (CHEBI:15555); platelet-activating factor (CHEBI:52450).

**Molecular profiling.** Human mast-cell line and xenotransplant studies (see Model Organisms) provide the transcriptomic/signaling evidence (constitutive IL-6, STAT5/PI3K dependence; TNF/survivin-driven clonal dominance). No dedicated MMAS-specific transcriptomic/proteomic/metabolomic cohort exists.

---

## 7. Anatomical Structures Affected

- **Primary tissue/organ (site of clonal cells):** **Bone marrow** (UBERON:0002371) — where clonal mast cells reside and are detected; diagnosis requires a bone-marrow study [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/), [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/).
- **Target cell population:** **Mast cell (CL:0000097)** — clonal, CD25+, KIT-D816V+.
- **Systems affected during mediator-release episodes (secondary/effector):**
  - Cardiovascular system (UBERON:0004535) — hypotension, syncope (dominant)
  - Skin (UBERON:0002097) — flushing (urticaria characteristically **absent/rare** in MMAS)
  - Digestive system (UBERON:0001007) — nausea, vomiting, diarrhea, cramping
  - Respiratory system (UBERON:0001004) — wheezing, nasal congestion
  - Nervous system — neurologic/neurocognitive symptoms
  - Skeletal system — osteoporosis (comorbidity/surveillance target)
- **Subcellular compartments (GO cellular component):** secretory granule (GO:0030141); plasma membrane (KIT receptor, GO:0005886); cytosol (signaling cascades).
- **Lateralization:** Not applicable — systemic mediator-driven disease.

---

## 8. Temporal Development

- **Onset:** **Adult-onset**, typically presenting with anaphylaxis; MMAS is not a congenital/pediatric presentation. Clonal disease is enriched among adults, males, with elevated basal tryptase [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/).
- **Onset pattern:** Episodes are **acute/paroxysmal**; the underlying clonal state is chronic and insidious (often asymptomatic between attacks, contributing to underdiagnosis) [PMID: 28740494](https://pubmed.ncbi.nlm.nih.gov/28740494/).
- **Course:** **Chronic, lifelong** clonal state with an **episodic/fluctuating** symptomatic course.
- **Progression:** Low. As a low-burden non-advanced clonal disorder, progression to advanced SM is rare. The most analogous registry entity, bone-marrow mastocytosis, showed **10-year progression-free survival of 95.9%** [PMID: 34545185](https://pubmed.ncbi.nlm.nih.gov/34545185/).
- **Critical window for intervention:** Recognition after a first severe (particularly Hymenoptera-triggered, urticaria-absent) anaphylaxis is the key opportunity to initiate protective venom immunotherapy and epinephrine provision [PMID: 39187156](https://pubmed.ncbi.nlm.nih.gov/39187156/).

---

## 9. Inheritance and Population

- **Inheritance:** **Not inherited.** The driver KIT D816V is **somatic/acquired** — MMAS is a clonal, non-Mendelian condition. The germline modifier HAT (*TPSAB1* duplication) is autosomal dominant but is not causal of MMAS [PMID: 34298172](https://pubmed.ncbi.nlm.nih.gov/34298172/), [PMID: 37818990](https://pubmed.ncbi.nlm.nih.gov/37818990/).
- **Epidemiology:** **Rare; no established population prevalence.** In a cohort of 703 patients referred for suspected mast-cell disorders, only 4.4% had confirmed idiopathic MCAS, and clonal MCAS (which includes MMAS) was a distinct minority; MMAS is rarer still [PMID: 38056692](https://pubmed.ncbi.nlm.nih.gov/38056692/). In a 38-patient diagnostic work-up, MMAS accounted for 4 of 23 monoclonal mast-cell disorders [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/).
- **Sex ratio:** **Male predominance** among clonal patients presenting with mediator-activation symptoms [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/).
- **Penetrance / expressivity / anticipation / founder effects:** Not applicable in the Mendelian sense (somatic driver). For the HAT modifier, penetrance is incomplete (~two-thirds of *TPSAB1*-duplication carriers are asymptomatic) [PMID: 37818990](https://pubmed.ncbi.nlm.nih.gov/37818990/).

> "The overall prevalence of iMCAS was 4.4% in the entire cohort." — [PMID: 38056692](https://pubmed.ncbi.nlm.nih.gov/38056692/)

> "HAT was detected in 15/346 (4%) HD versus 43/149 (29%) non-clonal MCAS and 84/464 (18%) mastocytosis cases." — [PMID: 37818990](https://pubmed.ncbi.nlm.nih.gov/37818990/)

---

## 10. Diagnostics

**Diagnostic framework (two-step).** MMAS is diagnosed when the **three consensus MCAS criteria are met AND bone-marrow study demonstrates mast-cell clonality without fulfilling full WHO SM criteria** [PMID: 21035176](https://pubmed.ncbi.nlm.nih.gov/21035176/), [PMID: 23179866](https://pubmed.ncbi.nlm.nih.gov/23179866/), [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/), [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/).

**Consensus MCAS criteria (Akin/Valent/Metcalfe):**
1. Typical episodic mediator-release symptoms in ≥2 organ systems.
2. Objective transient rise in a validated mast-cell mediator — **serum tryptase increasing by ≥20% above baseline + 2 ng/mL** during an event.
3. Symptomatic response to mast-cell mediator-targeting therapy.

> "an increase of the marker above the patient's baseline value during symptomatic periods on more than two occasions, or baseline serum tryptase levels that are persistently above 15 ng/ml." — [PMID: 23179866](https://pubmed.ncbi.nlm.nih.gov/23179866/)

**Clonality demonstration (bone marrow):**
- **KIT D816V** detection by **highly sensitive allele-specific PCR on purified mast cells** (essential given very low clonal burden) [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/).
- **Flow cytometry** for aberrant **CD25** (±CD2/CD30) on bone-marrow mast cells [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/).
- Bone-marrow histology/immunohistochemistry to confirm the **absence** of the major SM criterion (multifocal dense aggregates) and insufficient minor criteria.

**Biomarkers.** Serum baseline tryptase (higher in clonal than non-clonal MCAD); transient event-related tryptase rise. Baseline tryptase interpretation must account for HAT (*TPSAB1* duplication) [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/), [PMID: 37818990](https://pubmed.ncbi.nlm.nih.gov/37818990/).

**Risk stratification to decide on bone-marrow biopsy — the REMA score.** Uses sex, absence of urticaria/pruritus, presyncope/syncope, and baseline serum tryptase to predict clonality and indicate when bone-marrow study is warranted [PMID: 39187156](https://pubmed.ncbi.nlm.nih.gov/39187156/), [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/).

> "followed by the Red Española de Mastocitosis score, which is calculated using anaphylaxis clinical features, BST, and the patient's sex." — [PMID: 39187156](https://pubmed.ncbi.nlm.nih.gov/39187156/)

**Genetic testing.** Somatic **KIT D816V** on peripheral blood (high-sensitivity ddPCR/ASO-PCR) and/or purified bone-marrow mast cells; germline **TPSAB1** copy-number analysis for HAT. Myeloid NGS panels can be used to exclude advanced-disease mutations.

**Differential diagnosis.** Systemic mastocytosis (esp. indolent SM without skin lesions / bone-marrow mastocytosis — distinguished by meeting full WHO criteria); idiopathic MCAS (clonality-negative, urticaria-predominant); secondary MCAS (IgE allergy); HAT alone; non-mast-cell causes of flushing/hypotension.

---

## 11. Outcome / Prognosis

- **Overall prognosis:** **Favorable.** MMAS is a non-advanced, low-burden clonal disorder. Non-advanced mast-cell disease has a mostly favorable prognosis [PMID: 40274818](https://pubmed.ncbi.nlm.nih.gov/40274818/).
- **Progression risk:** Low; the analogous bone-marrow mastocytosis variant had **95.9% 10-year progression-free survival**, with tryptase <125 ng/mL and absence of B-findings predicting excellent outcome [PMID: 34545185](https://pubmed.ncbi.nlm.nih.gov/34545185/).
- **Principal morbidity:** **Recurrent severe/life-threatening anaphylaxis** — the dominant clinical risk, not clonal progression.
- **Mortality:** Attributable mortality is driven by anaphylaxis events (potentially fatal, especially venom-triggered) rather than neoplastic progression.
- **Prognostic factors:** Baseline tryptase level, presence/absence of B-findings, co-existing HAT (worsens reaction severity), and adequacy of anaphylaxis prophylaxis.

> "The prognosis of cutaneous mastocytosis and non-advanced SM is mostly favourable." — [PMID: 40274818](https://pubmed.ncbi.nlm.nih.gov/40274818/)

> "The estimated 10-year progression-free survival of BMM and typical ISM was 95.9% and 92.6%, respectively." — [PMID: 34545185](https://pubmed.ncbi.nlm.nih.gov/34545185/)

---

## 12. Treatment

Management mirrors that of **non-advanced clonal mast-cell disease**: anti-mediator therapy, anaphylaxis prevention, and comorbidity surveillance [PMID: 40274818](https://pubmed.ncbi.nlm.nih.gov/40274818/), [PMID: 39187156](https://pubmed.ncbi.nlm.nih.gov/39187156/).

| Therapy | Agent/approach | Role in MMAS | NCIT suggestion |
|---|---|---|---|
| H1 antihistamines | e.g., cetirizine, fexofenadine | First-line anti-mediator | NCIT:C265 (Antihistamine) |
| H2 antihistamines | e.g., famotidine | GI mediator symptoms | — |
| Mast-cell stabilizer | Cromolyn sodium | GI/systemic symptom control | NCIT:C61762 (Cromolyn) |
| Leukotriene antagonist | Montelukast | Adjunct anti-mediator | NCIT:C1876 (Montelukast) |
| Anti-IgE mAb | Omalizumab | Refractory anaphylaxis/mediator symptoms | NCIT:C2075 (Omalizumab) |
| Emergency | **Epinephrine autoinjectors (≥3)** | Anaphylaxis rescue — essential | NCIT:C692 (Epinephrine) |
| Venom immunotherapy (VIT) | Hymenoptera venom | **Lifelong (>5 yr/indefinite)** for venom-triggered clonal disease | NCIT:C15321 (Immunotherapy) |
| Osteoporosis therapy | Bisphosphonates, Ca/vitamin D | Comorbidity prevention | — |
| Selective KIT inhibitor | **Avapritinib** (KIT D816V inhibitor) | Reserved for refractory cases; reduces tryptase, MC burden, symptoms in non-advanced SM | NCIT:C123834 (Avapritinib) |
| Multikinase inhibitor | Midostaurin | Advanced disease (not standard for MMAS) | NCIT:C1439 (Midostaurin) |

> "Management of mastocytosis consists of symptomatic therapy, including anti-mast cell mediator drugs, and cytoreductive agents for patients with advanced disease and selected individuals with non-advanced disease, as well as recognition and prevention of comorbidities such as osteoporosis and anaphylaxis." — [PMID: 40274818](https://pubmed.ncbi.nlm.nih.gov/40274818/)

> "it is recommended to continue immunotherapy for more than 5 years or indefinitely and to carry at least three epinephrine autoinjectors." — [PMID: 39187156](https://pubmed.ncbi.nlm.nih.gov/39187156/)

**KIT inhibitors — evidence.** Selective KIT D816V inhibition with **avapritinib** reduces serum tryptase, mast-cell burden and mediator symptoms in non-advanced SM (including at low 25 mg dosing), supporting its candidacy for refractory clonal disease including MMAS [PMID: 40963125](https://pubmed.ncbi.nlm.nih.gov/40963125/), [PMID: 40274818](https://pubmed.ncbi.nlm.nih.gov/40274818/). Midostaurin improves QoL and mediator symptoms in advanced SM [PMID: 32437738](https://pubmed.ncbi.nlm.nih.gov/32437738/), but cytoreduction is generally unnecessary in low-burden MMAS.

**Pharmacogenomics / personalized medicine.** The KIT D816V genotype directly guides selection of **D816V-active** inhibitors (avapritinib, midostaurin) over D816V-resistant agents (imatinib, which is effective only for rare non-D816V/imatinib-sensitive KIT variants) [PMID: 37309222](https://pubmed.ncbi.nlm.nih.gov/37309222/).

---

## 13. Prevention

- **Primary prevention (of disease onset):** Not possible — MMAS arises from a spontaneous somatic mutation.
- **Secondary prevention (early detection):** REMA-score-based risk stratification and bone-marrow work-up in patients with venom-triggered, urticaria-absent, hypotensive anaphylaxis and elevated tryptase, enabling early protective intervention [PMID: 39187156](https://pubmed.ncbi.nlm.nih.gov/39187156/), [PMID: 20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/).
- **Tertiary prevention (of complications):**
  - **Anaphylaxis prevention:** trigger avoidance, ≥3 epinephrine autoinjectors, and **lifelong Hymenoptera venom immunotherapy** for venom-allergic patients [PMID: 39187156](https://pubmed.ncbi.nlm.nih.gov/39187156/).
  - **Osteoporosis surveillance and treatment** [PMID: 40274818](https://pubmed.ncbi.nlm.nih.gov/40274818/).
- **Counseling:** Because the driver is somatic, there is no offspring recurrence risk from the KIT clone; genetic counseling is relevant only for the germline HAT (*TPSAB1*) modifier, which is autosomal dominant.
- **Immunization / public-health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* (NCBI Taxon 9606). Experimental biology also uses *Mus musculus* (NCBI Taxon 10090).
- **Orthologous gene:** *Kit* (mouse NCBI Gene 16590) is orthologous to human *KIT* (NCBI Gene 3815; HGNC:6342).
- **Natural disease in other species:** No naturally occurring animal counterpart specifically of MMAS is documented; mast-cell tumors occur in companion animals (notably dogs) with activating KIT mutations, but these are neoplasms rather than the sub-threshold clonal activation syndrome. (MMAS-specific veterinary data not available.)
- **Comparative biology:** KIT signaling and its activating mutations are evolutionarily conserved, underpinning the utility of murine and cell-line models.
- **Zoonotic potential:** Not applicable (non-infectious, clonal disorder).

---

## 15. Model Organisms

No dedicated MMAS-specific animal model exists; the biology is studied through **KIT D816V mast-cell models** shared with systemic mastocytosis [PMID: 37025992](https://pubmed.ncbi.nlm.nih.gov/37025992/), [PMID: 38142424](https://pubmed.ncbi.nlm.nih.gov/38142424/), [PMID: 34424959](https://pubmed.ncbi.nlm.nih.gov/34424959/).

| Model | Type | Use / findings | Reference |
|---|---|---|---|
| **HMC-1.2** human mast-cell line; CRISPR/Cas9 single-D816V-KIT derivative | In vitro human cell line | Principal preclinical model for D816V-KIT biology and drug testing | [PMID: 37025992](https://pubmed.ncbi.nlm.nih.gov/37025992/) |
| Murine xenotransplantation of neoplastic mast cells | Mammalian (mouse) | KIT D816V-driven, TNF/survivin (BIRC5)-mediated clonal dominance; TNF knockout prolonged survival | [PMID: 38142424](https://pubmed.ncbi.nlm.nih.gov/38142424/) |
| GCPS / Gli3-haploinsufficient mouse | Mammalian (mouse) | Demonstrated KIT + Hedgehog synergy in mastocytosis onset | [PMID: 34424959](https://pubmed.ncbi.nlm.nih.gov/34424959/) |

> "CRISPR/Cas9-engineering of HMC-1.2 cells renders a human mast cell line with a single D816V-KIT mutation: An improved preclinical model for research on mastocytosis." — [PMID: 37025992](https://pubmed.ncbi.nlm.nih.gov/37025992/)

> "knockout of TNF in neoplastic MC prolonged survival and reduced myelosuppression in a murine xenotransplantation model." — [PMID: 38142424](https://pubmed.ncbi.nlm.nih.gov/38142424/)

**Phenotype recapitulation / limitations.** These models faithfully reproduce **KIT D816V signaling and mediator biology** but model the **high-burden neoplastic (SM/advanced)** end of the spectrum rather than the defining feature of MMAS — a *sub-threshold, low-burden* clone with a lowered activation threshold and anaphylaxis phenotype. No model captures the clinical anaphylaxis-dominant, urticaria-poor presentation of human MMAS.

---

## Mechanistic Model / Interpretation

```
        SOMATIC EVENT (acquired, non-germline)
                 |
        KIT D816V gain-of-function  ── (GO:0007169 RTK signaling)
                 |
        Constitutive STAT5 / PI3K / MEK-ERK activation
                 |
        +--------+----------+
        |                   |
  Pro-inflammatory     LOWERED MAST-CELL
  output (IL-6)        ACTIVATION THRESHOLD
        |                   |
  (limited clonal     +  germline HAT (TPSAB1 dup) -> amplifies severity
   expansion; KIT           |
   D816V alone         TRIGGER (Hymenoptera venom /
   insufficient ->      idiopathic / MRGPRX2 IgE-independent)
   stays BELOW SM           |
   threshold = MMAS)   Explosive degranulation:
        |               tryptase, histamine, PAF, PGD2
        |                   |
   Favorable            CARDIOVASCULAR-DOMINANT,
   prognosis;           URTICARIA-POOR ANAPHYLAXIS
   low progression      (hypotension, syncope; male-predominant)
```

MMAS is best understood as systemic mastocytosis' "shadow": the same somatic KIT D816V engine and the same aberrant CD25+ clonal phenotype, but with a clone too small to satisfy WHO SM criteria. The pathological consequence is not tissue infiltration/organ damage (as in advanced SM) but a **hair-trigger anaphylaxis diathesis**. The two clonality markers (KIT D816V; CD25) define the entity; the low burden defines its separation from SM; and the lowered activation threshold defines its danger. HAT is a distinct, germline, additive severity amplifier — a genuine gene–environment interaction node.

---

## Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/) | Defines MMAS vs SM; documents low KIT D816V burden and CD25 in MMAS (4/23 monoclonal disorders were MMAS) | F001, F002, F010 |
| [34298172](https://pubmed.ncbi.nlm.nih.gov/34298172/) | Places monoclonal MCAS within primary/clonal MCAS; KIT diagnostic relevance | F001, F004 |
| [30948489](https://pubmed.ncbi.nlm.nih.gov/30948489/) | D816V-KIT → STAT5/PI3K → constitutive IL-6 | F003 |
| [20434205](https://pubmed.ncbi.nlm.nih.gov/20434205/) | Clinical/molecular features of clonal MCAD; male sex, cardiovascular, insect-trigger, higher tryptase; predictive model for clonality | F004, F005, F009 |
| [39187156](https://pubmed.ncbi.nlm.nih.gov/39187156/) | REMA score; VIT + epinephrine recommendations | F004, F006 |
| [40641447](https://pubmed.ncbi.nlm.nih.gov/40641447/) | Post-sting hypotensive, non-cutaneous anaphylaxis points to clonal MC disease | F004 |
| [21035176](https://pubmed.ncbi.nlm.nih.gov/21035176/) | Proposes consensus MCAS diagnostic criteria | F005 |
| [23179866](https://pubmed.ncbi.nlm.nih.gov/23179866/) | Tryptase mediator criterion detail | F005 |
| [40274818](https://pubmed.ncbi.nlm.nih.gov/40274818/) | Management framework; favorable prognosis of non-advanced disease | F006, F007 |
| [34545185](https://pubmed.ncbi.nlm.nih.gov/34545185/) | 95.9% 10-yr PFS for bone-marrow mastocytosis (MMAS analogue) | F007 |
| [37818990](https://pubmed.ncbi.nlm.nih.gov/37818990/) | HAT enrichment in MCAS/mastocytosis (REMA, n=959) | F008, F010 |
| [41932753](https://pubmed.ncbi.nlm.nih.gov/41932753/) | HAT as independent severity modifier | F008 |
| [38056692](https://pubmed.ncbi.nlm.nih.gov/38056692/) | Clonal MCAS has fewer mucocutaneous symptoms (P=.015); iMCAS prevalence 4.4% | F009, F010 |
| [25944644](https://pubmed.ncbi.nlm.nih.gov/25944644/) | Multisystem MCAS symptom spectrum | F009 |
| [35623575](https://pubmed.ncbi.nlm.nih.gov/35623575/) | ICD-10-CM coding of MCA disorders (ECNM-AIM) | F010 |
| [37025992](https://pubmed.ncbi.nlm.nih.gov/37025992/) | Engineered single-D816V HMC-1.2 model | F011 |
| [38142424](https://pubmed.ncbi.nlm.nih.gov/38142424/) | Murine xenotransplant; TNF/survivin clonal dominance | F011, F012 |
| [34424959](https://pubmed.ncbi.nlm.nih.gov/34424959/) | KIT D816V alone insufficient; Hedgehog synergy | F012 |
| [42542541](https://pubmed.ncbi.nlm.nih.gov/42542541/) | KIT D816V lowers activation threshold; MRGPRX2/non-IgE mechanisms | F012 |
| [40963125](https://pubmed.ncbi.nlm.nih.gov/40963125/) | Avapritinib reduces tryptase/MC burden/symptoms | F006 |
| [32437738](https://pubmed.ncbi.nlm.nih.gov/32437738/) | Midostaurin improves QoL/mediator symptoms (advanced SM) | Contextual (treatment) |
| [37309222](https://pubmed.ncbi.nlm.nih.gov/37309222/) | SM diagnosis/risk/management; genotype-guided TKI choice | Contextual (pharmacogenomics) |

---

## Limitations and Knowledge Gaps

1. **Template mislabeling as "Mendelian."** MMAS is driven by a **somatic** KIT D816V mutation and is not inherited; the only Mendelian element is the *modifier* HAT. Sections on inheritance pattern, penetrance, anticipation, founder effects, and carrier frequency are therefore largely not applicable.
2. **Sparse MMAS-specific data.** Most quantitative evidence (progression-free survival, treatment response, QoL) derives from **systemic mastocytosis** (especially bone-marrow mastocytosis / ISM without skin lesions) used as the closest analogue. Dedicated MMAS cohorts are small (e.g., 4 patients in [PMID: 28262030](https://pubmed.ncbi.nlm.nih.gov/28262030/)).
3. **No established prevalence/incidence** figures exist specifically for MMAS.
4. **No dedicated animal model** captures the low-burden, anaphylaxis-dominant MMAS phenotype; existing models represent higher-burden neoplastic disease.
5. **Diagnostic sensitivity dependence.** Because clonal burden is minute, MMAS detection hinges on highly sensitive KIT assays on purified mast cells; false negatives likely lead to under-recognition (misclassification as idiopathic MCAS).
6. **Citation caveats.** Two supporting snippets (PMID 41932753 and PMID 37025992) were flagged as title/abstract mismatches in the knowledge state; their claims are corroborated by other cited sources and are treated as well supported.
7. **Boundary ambiguity.** The line between MMAS and early indolent SM without skin lesions is continuous; some MMAS patients may represent very early ISM.

---

## Proposed Follow-up Experiments / Actions

1. **Dedicated MMAS registry / natural-history study** — pool cases across reference centers (REMA, ECNM) to establish prevalence, sex ratio, anaphylaxis recurrence rates, and long-term progression risk distinct from ISM.
2. **Prospective evaluation of low-dose avapritinib in refractory MMAS** — extend the ISM low-dose (25 mg) experience [PMID: 40963125](https://pubmed.ncbi.nlm.nih.gov/40963125/) to MMAS patients with recurrent anaphylaxis despite VIT, with tryptase/KIT-VAF and PROM endpoints.
3. **Systematic HAT co-testing** — genotype *TPSAB1* in all suspected clonal-MCAS patients to quantify how germline α-tryptase dosage modifies MMAS severity and to refine risk stratification.
4. **Ultrasensitive peripheral-blood KIT D816V ddPCR as a first-line screen** — validate against purified bone-marrow mast-cell PCR to reduce invasive work-up and under-diagnosis.
5. **Mechanistic dissection of the "lowered threshold"** — quantify MRGPRX2 and FcεRI signaling in KIT D816V+ vs wild-type primary mast cells to define the molecular basis of hyper-releasability and identify druggable nodes.
6. **Refine REMA-type scoring** with modern biomarkers (baseline tryptase corrected for HAT, blood KIT VAF) to sharpen the decision to pursue bone-marrow biopsy.

---

*Report compiled from 12 confirmed findings across 5 investigation iterations and 52 reviewed papers. Evidence sources are predominantly human clinical cohorts and reference-center series, supplemented by in vitro human mast-cell line and murine model studies for mechanism.*


## Artifacts

- [OpenScientist final report](Monoclonal_Mast_Cell_Activation_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Monoclonal_Mast_Cell_Activation_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 22 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 23 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.
