---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-12T14:48:25.891170'
end_time: '2026-10-12T15:33:15.627750'
duration_seconds: 2689.74
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: FDX2-Related Mitochondrial Myopathy
  mondo_id: MONDO:0020714
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: FDX2-Related_Mitochondrial_Myopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: FDX2-Related_Mitochondrial_Myopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FDX2-Related Mitochondrial Myopathy
- **MONDO ID:** MONDO:0020714 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FDX2-Related Mitochondrial Myopathy** covering all of the
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

# FDX2-Related Mitochondrial Myopathy (MEOAL) — Comprehensive Disease Report

**Disease:** FDX2-Related Mitochondrial Myopathy
**Primary synonym:** MEOAL — *Mitochondrial myopathy, Episodic, with or without Optic Atrophy and reversible Leukoencephalopathy*
**MONDO:** MONDO:0020714 · **OMIM:** #251900 · **Gene:** FDX2 (alias FDX1L), 19p13.2
**Category:** Mendelian (autosomal recessive)

*Autonomous literature-based research report. Evidence types indicated as: [HUMAN] clinical case/cohort; [IN VITRO] cell/biochemistry; [MODEL] model organism; [COMP] computational/database.*

---

## Summary

FDX2-Related Mitochondrial Myopathy, catalogued as **MEOAL (OMIM #251900; MONDO:0020714)**, is an ultra-rare autosomal-recessive inborn error of mitochondrial metabolism caused by biallelic loss-of-function variants in **FDX2 (FDX1L)** on chromosome 19p13.2. FDX2 encodes **mitochondrial ferredoxin-2**, a small [2Fe-2S] electron-transfer protein that serves as the dedicated electron donor for **iron-sulfur (Fe-S) cluster biogenesis**. When FDX2 function is lost, cells cannot efficiently assemble [2Fe-2S] and [4Fe-4S] clusters, crippling every Fe-S-dependent enzyme — most importantly respiratory chain complexes I, II and III, and the TCA-cycle enzyme aconitase. The downstream consequence is mitochondrial energy (ATP) failure accompanied by disordered cellular iron homeostasis and mitochondrial iron overload.

Clinically, the disease presents in childhood with **optic atrophy and nystagmus (by age ~3)**, followed within the first and second decades by an **episodic/progressive myopathy** featuring exercise intolerance, cramps, myalgia, and recurrent crises that can escalate to **severe rhabdomyolysis (CK up to ~320,000 U/L), lactic acidosis, and acute kidney injury**. A **sensorimotor axonal neuropathy** and **reversible (or partially reversible) leukoencephalopathy** on MRI complete the characteristic multisystem picture. Muscle biopsy shows a distinctive pattern of regional succinate dehydrogenase (complex II) and cytochrome c oxidase deficiency with iron accumulation. The disorder is genetically and biochemically related to, but distinct from, other Fe-S/ISC-biogenesis diseases such as FDXR-related neuropathy, ISCU myopathy, and Friedreich ataxia (FXN).

There is **no disease-specific or curative therapy**. Management is supportive and follows general mitochondrial-cytopathy principles: trigger avoidance (fasting, fever, intercurrent illness), graded low-intensity aerobic/resistance exercise, aggressive hydration and renal protection during rhabdomyolysis crises, empirical "mitochondrial cocktail" supplements, and genetic counseling for affected families. The evidence base is derived almost entirely from a small number of consanguineous/founder families plus mechanistic work in human cells, yeast (*Yah1*), and structural biology (cryo-EM of the ferredoxin–ISC complex); no dedicated vertebrate animal model of FDX2 disease has yet been published.

---

## Key Findings

### Finding 1 — Biallelic FDX2 (FDX1L) variants cause autosomal-recessive MEOAL [HUMAN]

FDX2-related disease is a classic Mendelian autosomal-recessive condition. The gene was first implicated by Spiegel and colleagues in 2014, who used **exome sequencing combined with homozygosity mapping** in a consanguineous family with adolescent-onset mitochondrial myopathy and identified a homozygous **c.1A>T** variant that disrupts the ATG start codon of FDX1L/FDX2 ([PMID: 24281368](https://pubmed.ncbi.nlm.nih.gov/24281368/)). The abstract states: *"We employed exome sequencing combined with homozygosity mapping to identify a homozygous mutation, c.1A>T, in the FDX1L gene, which encodes the mitochondrial ferredoxin 2 (Fdx2) protein."*

Subsequent families confirmed the gene and broadened the allelic spectrum: a recurrent homozygous missense **c.431C>T (p.Pro144Leu / P144L)** was reported in **six patients from two unrelated Brazilian families** ([PMID: 30010796](https://pubmed.ncbi.nlm.nih.gov/30010796/); mechanism in [PMID: 39467201](https://pubmed.ncbi.nlm.nih.gov/39467201/), which notes *"the homozygous mutation c.431C>T (p.P144L) described in six patients from two unrelated families"*). A homozygous splice variant **c.200+4A>G** was described in a pediatric multiorgan case ([PMID: 41372147](https://pubmed.ncbi.nlm.nih.gov/41372147/)), and an additional homozygous case presented with severe rhabdomyolysis ([PMID: 37565517](https://pubmed.ncbi.nlm.nih.gov/37565517/)). The consistent requirement for two defective alleles, the frequent consanguinity, and the unaffected heterozygous parents all confirm recessive inheritance.

### Finding 2 — Pathomechanism: FDX2 deficiency impairs Fe-S cluster biogenesis, disabling Fe-S-dependent respiratory complexes and aconitase [HUMAN / IN VITRO]

The core lesion is a failure of **iron-sulfur cluster assembly**. In patient skeletal muscle, FDX2 loss severely impairs the activities of the **Fe-S-dependent respiratory complexes I, II and III and mitochondrial aconitase** ([PMID: 24281368](https://pubmed.ncbi.nlm.nih.gov/24281368/): *"severely impaired activities of iron sulfur (Fe-S)-dependent complexes I, II and III and mitochondrial aconitase"*). FDX2 is the electron donor that promotes assembly of both **[2Fe-2S] and [4Fe-4S]** clusters ([PMID: 39467201](https://pubmed.ncbi.nlm.nih.gov/39467201/)).

Structural work has defined precisely how FDX2 acts within the biogenesis machinery. Cryo-EM shows FDX2 binds the **core ISC complex (ISCU2–NFS1–ISD11/LYRM4–ACP1)** and **competes with frataxin (FXN) for overlapping binding sites**, delivering electrons to the nascent cluster ([PMID: 39632806](https://pubmed.ncbi.nlm.nih.gov/39632806/): *"FDX2 and FXN compete for overlapping binding sites"*). Patient cells carrying the c.200+4A>G splice allele show **impaired mitochondrial respiration, defects in many Fe-S proteins, enhanced mitochondrial iron accumulation, and reduced SOD2** ([PMID: 41372147](https://pubmed.ncbi.nlm.nih.gov/41372147/)), tying the molecular defect directly to multisystem energy failure and redox imbalance.

### Finding 3 — Clinical phenotype: childhood optic atrophy, episodic myopathy, neuropathy, reversible leukoencephalopathy [HUMAN]

The best-characterized cohort (two Brazilian families, 6 patients) defines the syndrome: **optic atrophy and nystagmus developing by age 3**, followed by **myopathy with recurrent episodes of cramps, myalgia and muscle weakness in the first or second decade**, a **sensory-motor axonal neuropathy** with progressive distal weakness, and a **reversible/partially reversible leukoencephalopathy** on MRI ([PMID: 30010796](https://pubmed.ncbi.nlm.nih.gov/30010796/): *"a complex neurological phenotype involving optic atrophy and nystagmus developing by age 3, followed by myopathy and recurrent episodes of cramps, myalgia and muscle weakness in the first or second decade of life"*).

Muscle histopathology is distinctive: *"Muscle biopsy demonstrated an unusual pattern of regional succinate dehydrogenase and cytochrome c oxidase deficiency with iron accumulation"* ([PMID: 30010796](https://pubmed.ncbi.nlm.nih.gov/30010796/)). Acute metabolic crises can be life-threatening: one patient showed **CK up to ~320,000 U/L, lactate 22.3 mmol/L, and acute kidney injury** during a rhabdomyolysis episode ([PMID: 37565517](https://pubmed.ncbi.nlm.nih.gov/37565517/)), and multiorgan involvement has been documented in pediatric disease ([PMID: 41372147](https://pubmed.ncbi.nlm.nih.gov/41372147/)).

### Finding 4 — FDX2 is functionally distinct from FDX1 (adrenodoxin) [IN VITRO]

Humans possess **two mitochondrial ferredoxins**. RNAi depletion established that **FDX2 — not FDX1 — is essential for heme A and Fe/S protein biosynthesis**, whereas FDX1 (adrenodoxin) reduces P450 enzymes for steroidogenesis ([PMID: 20547883](https://pubmed.ncbi.nlm.nih.gov/20547883/): *"we identified a Fdx1-related mitochondrial protein, designated ferredoxin 2 (Fdx2) and found it to be essential for heme A and Fe/S protein biosynthesis"*). FDX2 cannot efficiently reduce P450s or convert steroids, explaining why FDX2 patients have a mitochondrial Fe-S disease rather than a steroidogenic disorder.

Crucially, FDX2 deficiency deranges iron homeostasis: *"Fdx2 deficiency had a severe impact, via impaired Fe/S protein biogenesis, on cellular iron homeostasis, leading to increased cellular iron uptake and iron accumulation in mitochondria"* ([PMID: 20547883](https://pubmed.ncbi.nlm.nih.gov/20547883/)). Both ferredoxins receive electrons from the single ferredoxin reductase **FDXR** (NADPH → FDXR → FDX) ([PMID: 28747430](https://pubmed.ncbi.nlm.nih.gov/28747430/)).

### Finding 5 — Genomic/constraint data confirm a LoF-tolerant, recessive gene [COMP]

FDX2 (ENSG00000267673) maps to **chr19:10,310,045–10,316,015 (cytoband 19p13.2)**. gnomAD constraint metrics indicate the gene is **tolerant of heterozygous loss-of-function**: **pLI = 0.0006**, observed/expected LoF (oe_lof) = 0.70 (90% CI 0.46–1.12), missense oe = 0.95, mis_z = 0.34. This LoF-tolerance is exactly what is expected for an autosomal-recessive disorder in which single-allele carriers are unaffected and two defective alleles are required to produce disease. The protein (UniProt **Q6P4F2**, FDX2_HUMAN) is a **186-amino-acid mitochondrial [2Fe-2S] ferredoxin** with an N-terminal mitochondrial targeting presequence.

### Finding 6 — Differential diagnosis: FDX2 disease within the ISC-biogenesis disorder spectrum [HUMAN]

FDX2 disease belongs to a broader family of **mitochondrial Fe-S/ISC-biogenesis disorders** with overlapping clinical features. The most important differential is **FDXR** (the upstream electron donor to FDX2), whose biallelic mutations cause auditory neuropathy and optic atrophy with mitochondrial iron overload ([PMID: 28965846](https://pubmed.ncbi.nlm.nih.gov/28965846/): *"FDXR encodes the mitochondrial ferredoxin reductase, the sole human ferredoxin reductase implicated in the biosynthesis of iron-sulfur clusters (ISCs) and in heme formation"*). Other differentials include **ISCU** (hereditary myopathy with exercise intolerance / Swedish myopathy, with similar SDH/aconitase deficiency), **FXN** (Friedreich ataxia), and **NFU1/BOLA3/ISCA2/IBA57** (multiple mitochondrial dysfunctions syndrome with glycine elevation).

A pragmatic diagnostic strategy for suspected mitochondrial disease combines biochemical markers (plasma/CSF lactate, alanine, proline) and neuroimaging to predict disease, then applies **first-line clinical exome sequencing**, reserving muscle biopsy for urgent or inconclusive cases ([PMID: 34056100](https://pubmed.ncbi.nlm.nih.gov/34056100/): *"apply first-line clinical exome sequencing to identify a definite diagnosis"*).

### Finding 7 — Model organisms: yeast *Yah1* is the key ortholog; no dedicated vertebrate model [MODEL / IN VITRO]

The *S. cerevisiae* ortholog of FDX2 is **Yah1** (yeast adrenodoxin homolog). Yah1 depletion causes a strong decrease in de novo Fe/S cluster synthesis on the scaffold Isu1p ([PMID: 12970193](https://pubmed.ncbi.nlm.nih.gov/12970193/): *"Depletion of the cysteine desulfurase Nfs1p, the ferredoxin Yah1p or the yeast frataxin homologue Yfh1p by regulated gene expression causes a strong decrease in the de novo synthesis of Fe/S clusters on Isu1p"*). The Yah1–Arh1 ferredoxin/ferredoxin-reductase pair is essential for heme A biosynthesis and FeSC assembly ([PMID: 15211518](https://pubmed.ncbi.nlm.nih.gov/15211518/)). No dedicated mouse or zebrafish model of FDX2 disease has been published; mechanistic insight derives from RNAi knockdown in human cells, patient-derived fibroblasts/myoblasts, yeast complementation, and recombinant-protein biophysics/cryo-EM. The pathway framework is summarized by Braymer & Lill, who note *"some 30 proteins involved in the synthesis of cellular [2Fe-2S] and [4Fe-4S] clusters and their incorporation into numerous apoproteins"* ([PMID: 28615445](https://pubmed.ncbi.nlm.nih.gov/28615445/)).

### Finding 8 — Treatment is supportive/symptomatic; no curative therapy [HUMAN]

No gene-specific or curative treatment exists. Management follows general mitochondrial-cytopathy principles. **Endurance exercise training** increases VO2max, respiratory chain enzyme activity, muscle strength, and quality of life, and is well tolerated ([PMID: 25008908](https://pubmed.ncbi.nlm.nih.gov/25008908/): *"Endurance exercise training increases Vo2 max, respiratory chain enzyme activity, and improves quality of life."*). Patients are advised to avoid exercise during metabolic stress: *"not exercise on days they have fever, superimposed illness, muscle pain, or cramps, and/or if they have fasted for more than 12 hours"* ([PMID: 25008908](https://pubmed.ncbi.nlm.nih.gov/25008908/)). Cochrane review found no evidence of harm from moderate training in muscle disease ([PMID: 20091552](https://pubmed.ncbi.nlm.nih.gov/20091552/)); creatine monohydrate gives mixed/modest benefit in mitochondrial cytopathies ([PMID: 18652078](https://pubmed.ncbi.nlm.nih.gov/18652078/)). Acute rhabdomyolysis crises require aggressive IV hydration and renal protection ([PMID: 37565517](https://pubmed.ncbi.nlm.nih.gov/37565517/)).

### Finding 9 — Verified identifiers [COMP]

EBI OLS4 confirms **MONDO:0020714 = "mitochondrial myopathy, episodic, with optic atrophy and reversible leukoencephalopathy" (MEOAL)**, cross-referenced to **OMIM:251900, GARD:0025221, MedGen:1679560 (UMLS C5193223)**.

---

## The 15-Section Disease Knowledge Report

### 1. Disease Information

FDX2-Related Mitochondrial Myopathy (MEOAL) is an ultra-rare, autosomal-recessive mitochondrial disorder of **iron-sulfur cluster biogenesis**. It manifests as a multisystem neuromuscular syndrome combining optic atrophy, episodic/progressive myopathy with exercise intolerance and rhabdomyolysis, axonal neuropathy, and reversible leukoencephalopathy.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0020714 |
| OMIM | #251900 |
| GARD | 0025221 |
| MedGen | 1679560 |
| UMLS | C5193223 |
| Gene (HGNC) | FDX2 (alias FDX1L) |
| UniProt | Q6P4F2 (FDX2_HUMAN) |
| Ensembl | ENSG00000267673 |
| ICD-10 | G71.3 (mitochondrial myopathy, NEC) — closest applicable; no FDX2-specific code |
| ICD-11 | 8C73 / 5C53.1 (disorders of mitochondrial energy metabolism) — closest applicable |

**Synonyms / alternative names:** MEOAL; mitochondrial myopathy, episodic, with optic atrophy and reversible leukoencephalopathy; FDX1L-related mitochondrial myopathy; ferredoxin-2 deficiency.

**Information source:** Disease-level, derived from aggregated case reports and small consanguineous/founder families (individual patient genotype–phenotype correlations) plus mechanistic in vitro and model-organism data — not from large EHR cohorts.

### 2. Etiology

**Causal factor (genetic):** Biallelic loss-of-function or hypomorphic variants in **FDX2/FDX1L**. Reported variants include start-loss **c.1A>T** ([PMID: 24281368](https://pubmed.ncbi.nlm.nih.gov/24281368/)), missense **c.431C>T (p.P144L)** ([PMID: 30010796](https://pubmed.ncbi.nlm.nih.gov/30010796/)), and splice **c.200+4A>G** ([PMID: 41372147](https://pubmed.ncbi.nlm.nih.gov/41372147/)).

**Genetic risk factors:** The disease is monogenic; "risk" is fully determined by biallelic FDX2 genotype. **Consanguinity** and **founder effects** (e.g., the recurrent Brazilian p.P144L allele) are the principal population-level risk contexts.

**Environmental risk factors:** None cause the disease, but environmental/metabolic stressors act as **crisis triggers** — fasting (>12 h), fever, intercurrent infection, and strenuous exercise can precipitate rhabdomyolysis and metabolic decompensation ([PMID: 25008908](https://pubmed.ncbi.nlm.nih.gov/25008908/); [PMID: 37565517](https://pubmed.ncbi.nlm.nih.gov/37565517/)).

**Protective factors:** No specific genetic or environmental protective alleles are established. Trigger avoidance is protective against acute crises.

**Gene–environment interactions:** The underlying genetic Fe-S/energy deficit interacts with metabolic demand — energy-stress states (fasting, fever, exertion) unmask or worsen the biochemical defect, producing the episodic phenotype.

### 3. Phenotypes

| Phenotype | Type | Onset | Severity / course | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Optic atrophy | Clinical sign | Early childhood (~age 3) | Progressive | Characteristic (majority) | HP:0000648 |
| Nystagmus | Clinical sign | Early childhood | Stable/progressive | Frequent | HP:0000639 |
| Exercise intolerance | Symptom | 1st–2nd decade | Episodic | Characteristic | HP:0003546 |
| Myalgia / muscle cramps | Symptom | 1st–2nd decade | Episodic | Frequent | HP:0003326 / HP:0003394 |
| Muscle weakness (myopathy) | Clinical sign | 1st–2nd decade | Progressive | Characteristic | HP:0003198 |
| Rhabdomyolysis | Lab/clinical | Episodic (crises) | Severe when present | Reported (subset) | HP:0003201 |
| Elevated creatine kinase | Lab abnormality | During crises | Severe (up to ~320,000 U/L) | Frequent in crises | HP:0003236 |
| Lactic acidosis / elevated lactate | Lab abnormality | During crises | Severe (up to 22.3 mmol/L) | Frequent | HP:0003128 |
| Sensorimotor axonal neuropathy | Clinical sign | Childhood–adolescence | Progressive, distal | Characteristic | HP:0007141 |
| Reversible leukoencephalopathy | Imaging/lab | Variable | Reversible/partially reversible | Characteristic | HP:0002352 |
| Acute kidney injury | Lab/clinical | During rhabdomyolysis crises | Severe | Subset | HP:0001919 |

**Quality-of-life impact:** Progressive visual loss (optic atrophy), muscle weakness and exercise intolerance, and neuropathy impair mobility, education/employment, and independence. Acute crises are life-threatening and require hospitalization. Formal QoL instrument data (EQ-5D/SF-36) specific to FDX2 disease are not available given the rarity.

### 4. Genetic / Molecular Information

**Causal gene:** FDX2 (FDX1L), 19p13.2, ENSG00000267673; UniProt Q6P4F2; 186-aa mitochondrial [2Fe-2S] ferredoxin with N-terminal targeting presequence.

**Pathogenic variants (ACMG-consistent, germline, homozygous in reported cases):**

| Variant (cDNA) | Protein | Class | Consequence | Reference |
|---|---|---|---|---|
| c.1A>T | start-loss (p.Met1?) | Pathogenic | Loss of function (no initiation) | [PMID: 24281368](https://pubmed.ncbi.nlm.nih.gov/24281368/) |
| c.431C>T | p.Pro144Leu | Likely pathogenic/Pathogenic | Missense, impaired function (founder, Brazil) | [PMID: 30010796](https://pubmed.ncbi.nlm.nih.gov/30010796/), [PMID: 39467201](https://pubmed.ncbi.nlm.nih.gov/39467201/) |
| c.200+4A>G | splice (exon 2 skip → 19 aa replaced by 21) | Pathogenic | Aberrant splicing, low FDX2 protein | [PMID: 41372147](https://pubmed.ncbi.nlm.nih.gov/41372147/) |

**Allele frequency:** All reported pathogenic variants are rare/private; FDX2 is LoF-tolerant in gnomAD (pLI = 0.0006; oe_lof = 0.70). **Origin:** germline (no somatic disease role). **Functional consequence:** loss of function — reduced protein level and/or impaired electron-donor activity. Notably, the P144L and c.200+4A>G mutant proteins may retain near-normal structure, implicating reduced abundance/activity rather than gross misfolding ([PMID: 41372147](https://pubmed.ncbi.nlm.nih.gov/41372147/); [PMID: 39467201](https://pubmed.ncbi.nlm.nih.gov/39467201/)).

**Modifier genes / epigenetics / chromosomal abnormalities:** None established; no large-scale structural variants reported.

### 5. Environmental Information

Not a primary driver of this monogenic disease. **Non-genetic triggers** of acute metabolic crises include fasting, fever, intercurrent illness, and strenuous/eccentric exercise. **No infectious agent** causes the disease (though infection/fever can precipitate crises). No toxic or occupational exposures are implicated.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. **Biallelic FDX2/FDX1L loss-of-function variant** (c.1A>T start-loss, p.P144L missense, or c.200+4A>G splice) → reduced level/activity of mitochondrial ferredoxin-2 protein.
2. Reduced FDX2 **leads to** loss of the dedicated [2Fe-2S] electron donor within the core ISC assembly complex (ISCU2–NFS1–ISD11/LYRM4–ACP1), where FDX2 normally competes with frataxin for binding and feeds electrons to the nascent cluster ([PMID: 39632806](https://pubmed.ncbi.nlm.nih.gov/39632806/)).
3. Loss of electron donation **results in** defective de novo assembly of **[2Fe-2S] and [4Fe-4S]** clusters on the scaffold (inferred from patient cells + yeast Yah1 depletion; [PMID: 41372147](https://pubmed.ncbi.nlm.nih.gov/41372147/), [PMID: 12970193](https://pubmed.ncbi.nlm.nih.gov/12970193/)).
4. Fe-S deficiency **leads to** loss of activity of Fe-S-dependent apoproteins — **respiratory complexes I, II, III** and **aconitase** ([PMID: 24281368](https://pubmed.ncbi.nlm.nih.gov/24281368/)).
   - **Branch A (bioenergetic):** Respiratory chain failure **results in** impaired oxidative phosphorylation and ATP deficit → exercise intolerance, myopathy, rhabdomyolysis, lactic acidosis.
   - **Branch B (iron homeostasis):** Impaired Fe-S biogenesis is sensed as cellular iron deficiency (via IRP/IRE), **leading to** increased iron uptake and **mitochondrial iron overload** ([PMID: 20547883](https://pubmed.ncbi.nlm.nih.gov/20547883/)); biopsy shows iron accumulation ([PMID: 30010796](https://pubmed.ncbi.nlm.nih.gov/30010796/)).
   - **Branch C (heme A / redox):** FDX2 loss impairs heme A biosynthesis (COX maturation) ([PMID: 20547883](https://pubmed.ncbi.nlm.nih.gov/20547883/)) and reduces SOD2, **resulting in** altered ROS handling ([PMID: 41372147](https://pubmed.ncbi.nlm.nih.gov/41372147/)).
5. Combined energy failure, iron overload, and redox imbalance in high-demand post-mitotic tissues (retinal ganglion cells/optic nerve, skeletal muscle, peripheral nerve, CNS white matter) **leads to** the clinical manifestations: optic atrophy, episodic myopathy/rhabdomyolysis, axonal neuropathy, and reversible leukoencephalopathy.

**Molecular pathways:** Mitochondrial ISC assembly pathway (NFS1/ISCU2/ISD11/ACP1/frataxin/ferredoxin); oxidative phosphorylation; TCA cycle (aconitase); heme A biosynthesis; cellular iron regulation (IRP1/IRP2–IRE).
**Cellular processes (GO):** iron-sulfur cluster assembly (GO:0016226), [2Fe-2S] assembly (GO:0044571), mitochondrial electron transport (GO:0006120), cellular iron ion homeostasis (GO:0006879), oxidative stress response.
**Protein dysfunction:** Loss of function — reduced abundance and/or electron-transfer capacity (not primarily aggregation).
**Metabolic changes:** Impaired OXPHOS/ATP output, lactate accumulation, mitochondrial iron overload, reduced heme A.
**Tissue damage mechanisms:** Bioenergetic failure + oxidative stress + iron-mediated injury in energy-demanding tissues.
**Immune involvement:** None established (not autoimmune/inflammatory).

### 7. Anatomical Structures Affected

- **Organ/system level:** Nervous system (optic nerve/retinal ganglion cells, peripheral nerves, CNS white matter), musculoskeletal (skeletal muscle). Secondary: kidney (acute kidney injury during rhabdomyolysis).
- **Tissue/cell level:** Skeletal muscle fibers (CL:0000188 skeletal muscle cell / UBERON:0001134); retinal ganglion cells (CL:0000740); peripheral neurons/axons (CL:0000101 sensory neuron); CNS white matter / oligodendrocytes and myelin (UBERON:0002316).
- **Subcellular level (GO Cellular Component):** Mitochondrion (GO:0005739), mitochondrial matrix (GO:0005759), mitochondrial inner membrane/respiratory chain (GO:0005743).
- **Localization (UBERON):** skeletal muscle organ (UBERON:0001134), optic nerve (UBERON:0000941), peripheral nerve (UBERON:0001021), cerebral white matter (UBERON:0002437). **Lateralization:** bilateral/symmetric (optic atrophy, leukoencephalopathy, myopathy).

### 8. Temporal Development

- **Onset:** Pediatric. Optic atrophy/nystagmus by ~age 3; myopathy in the first-to-second decade. Onset of visual signs is insidious; muscle crises are acute/episodic.
- **Progression:** Chronic and progressive baseline course (progressive myopathy, distal neuropathy, optic atrophy) **punctuated by acute episodic crises** (rhabdomyolysis, metabolic decompensation). Leukoencephalopathy is notable for being **reversible/partially reversible**.
- **Patterns:** Episodic crises can resolve with supportive care; some white-matter changes reverse. **Critical periods** for intervention are the peri-crisis windows (prompt hydration/renal protection) and trigger avoidance. Lifelong, chronic disorder.

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (biallelic FDX2). Unaffected heterozygous carriers.
- **Epidemiology:** Ultra-rare; fewer than ~15 genetically confirmed patients reported worldwide. No reliable prevalence/incidence estimates (Orphanet prevalence "unknown/<1/1,000,000").
- **Penetrance/expressivity:** Appears high penetrance in biallelic individuals; variable expressivity/severity across variants and families.
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects/consanguinity:** The p.P144L allele is a recurrent founder variant in Brazilian families; consanguinity underlies several reports. Carrier frequency not established but low (LoF-tolerant, rare alleles).
- **Demographics:** Reported in consanguineous Middle Eastern and Brazilian families; no strong sex predilection reported. Age distribution: pediatric onset with lifelong course.

### 10. Diagnostics

- **Laboratory:** Elevated serum/plasma **lactate** (markedly during crises, up to 22.3 mmol/L), elevated **creatine kinase** (up to ~320,000 U/L in rhabdomyolysis), elevated alanine; renal function monitoring during crises ([PMID: 37565517](https://pubmed.ncbi.nlm.nih.gov/37565517/)).
- **Biopsy/histopathology:** Characteristic **regional succinate dehydrogenase (complex II) and cytochrome c oxidase deficiency with iron accumulation** on muscle biopsy ([PMID: 30010796](https://pubmed.ncbi.nlm.nih.gov/30010796/)); reduced Fe-S-dependent complex I/II/III and aconitase activities ([PMID: 24281368](https://pubmed.ncbi.nlm.nih.gov/24281368/)).
- **Imaging:** Brain MRI showing reversible/partially reversible leukoencephalopathy; MR spectroscopy may show a lactate peak.
- **Electrophysiology:** Nerve conduction studies/EMG consistent with sensorimotor axonal neuropathy; myopathic EMG features.
- **Genetic testing (definitive):** **Clinical exome/whole-exome sequencing** is first-line for suspected mitochondrial disease ([PMID: 34056100](https://pubmed.ncbi.nlm.nih.gov/34056100/)); mitochondrial nuclear-gene panels including FDX2/FDX1L, or single-gene/targeted testing; homozygosity mapping is valuable in consanguineous families ([PMID: 24281368](https://pubmed.ncbi.nlm.nih.gov/24281368/)). RNA/functional studies help classify splice variants ([PMID: 41372147](https://pubmed.ncbi.nlm.nih.gov/41372147/)).
- **Differential diagnosis:** FDXR-related auditory neuropathy + optic atrophy ([PMID: 28965846](https://pubmed.ncbi.nlm.nih.gov/28965846/)); ISCU myopathy (exercise intolerance); FXN/Friedreich ataxia; NFU1/BOLA3/ISCA2/IBA57 multiple mitochondrial dysfunctions syndrome; other complex I–IV deficiencies and mtDNA disorders.
- **Screening:** No population newborn screening. **Cascade/carrier testing** in affected families and genetic counseling are appropriate.

### 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics. The chronic course is compatible with survival into adulthood, but **acute rhabdomyolysis crises with lactic acidosis and acute kidney injury are potentially life-threatening** ([PMID: 37565517](https://pubmed.ncbi.nlm.nih.gov/37565517/)).
- **Morbidity/disability:** Progressive visual impairment (optic atrophy), muscle weakness/exercise intolerance, and distal sensorimotor neuropathy produce cumulative disability. Leukoencephalopathy may be reversible.
- **Disease course:** Chronic-progressive with superimposed episodic crises; recovery from individual crises is possible with supportive care.
- **Prognostic factors:** Severity/frequency of metabolic crises, degree of multiorgan involvement, and specific variant (residual FDX2 function) likely influence outcome. No validated prognostic biomarkers beyond lactate/CK trends.

### 12. Treatment

**No curative or disease-specific therapy exists.** Management is supportive (NCIT: Supportive Care, C15277):

- **Acute crisis management:** Aggressive **IV hydration** and renal protection for rhabdomyolysis; treat lactic acidosis; monitor/support kidney function ([PMID: 37565517](https://pubmed.ncbi.nlm.nih.gov/37565517/)).
- **Exercise/rehabilitation (NCIT: Exercise Therapy, C16586):** Graded **endurance + resistance training** improves VO2max, respiratory enzyme activity, strength, and QoL; start low-intensity and avoid exercising during fever, illness, muscle pain/cramps, or after fasting >12 h ([PMID: 25008908](https://pubmed.ncbi.nlm.nih.gov/25008908/)). Cochrane: no evidence of harm from moderate training ([PMID: 20091552](https://pubmed.ncbi.nlm.nih.gov/20091552/)).
- **Supplements (empirical "mitochondrial cocktail"):** CoQ10/ubiquinone, riboflavin, L-carnitine, antioxidants — no FDX2-specific trial evidence. Creatine monohydrate gives mixed/modest benefit ([PMID: 18652078](https://pubmed.ncbi.nlm.nih.gov/18652078/)).
- **Trigger avoidance:** Avoid prolonged fasting, manage fever/illness promptly, pace activity.
- **Genetic counseling** for families.
- **Advanced/experimental therapeutics:** No gene therapy, RNA therapy, or targeted therapy in trials for FDX2 disease to date. **Pharmacogenomics:** none established.

### 13. Prevention

- **Primary prevention:** Not preventable at the individual level (monogenic). **Genetic counseling, carrier/cascade testing, prenatal/preimplantation genetic diagnosis** can prevent recurrence in at-risk families — especially relevant where consanguinity/founder alleles (p.P144L) are present.
- **Secondary prevention:** Early molecular diagnosis (exome-first) enables early supportive management and crisis-prevention education.
- **Tertiary prevention:** Trigger avoidance, prompt crisis management (hydration/renal protection), graded exercise, and multidisciplinary follow-up to limit complications.
- **Immunization/public health/environmental interventions:** Not applicable beyond general infection-prevention to reduce fever-triggered crises.

### 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** Human FDX2 (NCBI Gene ID 614650). Functional ortholog in *Saccharomyces cerevisiae* (NCBI Taxon 4932) is **Yah1** (yeast adrenodoxin homolog), partnered with reductase Arh1 ([PMID: 12970193](https://pubmed.ncbi.nlm.nih.gov/12970193/); [PMID: 15211518](https://pubmed.ncbi.nlm.nih.gov/15211518/)). Mammalian orthologs exist (mouse *Fdx2*, *Mus musculus* NCBI Taxon 10090).
- **Natural disease in animals:** No naturally occurring FDX2 disease reported in companion animals or wildlife (no OMIA entry identified).
- **Comparative biology/conservation:** The ferredoxin-dependent ISC assembly pathway is **highly evolutionarily conserved** from yeast to humans, which is why Yah1 depletion recapitulates the core Fe-S assembly defect ([PMID: 12970193](https://pubmed.ncbi.nlm.nih.gov/12970193/); [PMID: 28615445](https://pubmed.ncbi.nlm.nih.gov/28615445/)).
- **Zoonotic/transmission:** Not applicable (genetic disease).

### 15. Model Organisms

- **Yeast (*S. cerevisiae*):** **Yah1** depletion is the principal genetic model, demonstrating that the ferredoxin is essential for de novo Fe-S cluster synthesis on Isu1p ([PMID: 12970193](https://pubmed.ncbi.nlm.nih.gov/12970193/)) and for heme A biosynthesis with Arh1 ([PMID: 15211518](https://pubmed.ncbi.nlm.nih.gov/15211518/)).
- **Human cell systems:** RNAi/CRISPR knockdown in human cells established FDX2's specific role in heme A and Fe/S biosynthesis and its iron-homeostasis phenotype ([PMID: 20547883](https://pubmed.ncbi.nlm.nih.gov/20547883/)); **patient-derived fibroblasts/myoblasts** show impaired respiration, multiple Fe-S defects, mitochondrial iron accumulation, and reduced SOD2 ([PMID: 41372147](https://pubmed.ncbi.nlm.nih.gov/41372147/)).
- **In vitro structural biology:** Recombinant FDX2 and cryo-EM of the FDX2–core-ISC complex define the electron-donation and frataxin-competition mechanism ([PMID: 39632806](https://pubmed.ncbi.nlm.nih.gov/39632806/); [PMID: 39467201](https://pubmed.ncbi.nlm.nih.gov/39467201/)).
- **Phenotype recapitulation / limitations:** Cellular and yeast models faithfully reproduce the **biochemical core** (Fe-S assembly failure, respiratory/aconitase deficiency, iron overload) but **do not capture the multisystem organismal phenotype** (optic atrophy, episodic myopathy, neuropathy, leukoencephalopathy). **No dedicated mouse or zebrafish disease model of FDX2 has been published** — a notable gap.

---

## Mechanistic Model / Interpretation

```
 Biallelic FDX2/FDX1L LoF variant (c.1A>T | p.P144L | c.200+4A>G)
                 │  (↓ ferredoxin-2 level / electron-donor activity)
                 ▼
 Loss of electron donation to core ISC complex (ISCU2-NFS1-ISD11-ACP1)
      [FDX2 competes with frataxin for overlapping sites]  (PMID 39632806)
                 │
                 ▼
 Defective de novo [2Fe-2S] & [4Fe-4S] cluster assembly  (PMID 12970193, 41372147)
                 │
    ┌────────────┼───────────────────────────┬───────────────────────────┐
    ▼            ▼                            ▼                           ▼
 Complex I/II/III   Aconitase loss        ↑Iron uptake +            ↓Heme A / ↓SOD2
 deficiency         (TCA)                 mito iron overload        (COX maturation,
 (PMID 24281368)                          (PMID 20547883)            redox) (PMID 41372147)
    │                   │                      │                          │
    └─────── ATP deficit / lactic acidosis ◄───┘                          │
                 │                                                        │
                 └──────────► OXIDATIVE STRESS + IRON-MEDIATED INJURY ◄───┘
                 │
                 ▼
 Energy-demanding post-mitotic tissues injured:
   • Optic nerve / RGC  → optic atrophy, nystagmus (by ~age 3)
   • Skeletal muscle    → episodic myopathy, rhabdomyolysis, CK↑, exercise intolerance
   • Peripheral nerve   → sensorimotor axonal neuropathy
   • CNS white matter   → reversible leukoencephalopathy
   • Kidney (secondary) → AKI during rhabdomyolysis crises
```

Upstream (initiating) events are the FDX2 mutation and the Fe-S assembly failure; downstream (effector) events are respiratory/TCA enzyme inactivation, iron mishandling, and tissue-specific energy failure. The **episodic** nature reflects gene–environment interaction: a chronically marginal bioenergetic reserve is tipped into crisis by metabolic stressors (fasting, fever, exertion).

---

## Evidence Base

| PMID | Study type | Contribution |
|---|---|---|
| [24281368](https://pubmed.ncbi.nlm.nih.gov/24281368/) | Human clinical/genetics | First gene identification (c.1A>T); complex I/II/III + aconitase deficiency |
| [30010796](https://pubmed.ncbi.nlm.nih.gov/30010796/) | Human clinical (6 patients) | Defines phenotype (optic atrophy, episodic myopathy, neuropathy, leukoencephalopathy); SDH/COX + iron biopsy; p.P144L founder |
| [41372147](https://pubmed.ncbi.nlm.nih.gov/41372147/) | Human + cellular | Novel c.200+4A>G splice variant; patient-cell respiration/Fe-S/iron/SOD2 defects |
| [37565517](https://pubmed.ncbi.nlm.nih.gov/37565517/) | Case report | Severe rhabdomyolysis (CK ~320,000), lactic acidosis, AKI — crisis management |
| [39467201](https://pubmed.ncbi.nlm.nih.gov/39467201/) | In vitro / structural | Molecular determinants of P144L; FDX2 donates electrons for [2Fe-2S]/[4Fe-4S] |
| [39632806](https://pubmed.ncbi.nlm.nih.gov/39632806/) | Cryo-EM | Two-stage FDX2 binding to core ISC complex; frataxin competition |
| [20547883](https://pubmed.ncbi.nlm.nih.gov/20547883/) | In vitro (RNAi) | FDX2 vs FDX1 functional distinction; iron-homeostasis phenotype |
| [28965846](https://pubmed.ncbi.nlm.nih.gov/28965846/) | Human clinical | FDXR disease — key differential and upstream pathway partner |
| [34056100](https://pubmed.ncbi.nlm.nih.gov/34056100/) | Review/methodology | Exome-first diagnostic strategy for mitochondrial disease |
| [12970193](https://pubmed.ncbi.nlm.nih.gov/12970193/) | Yeast model | Yah1 (FDX2 ortholog) essential for Fe-S assembly on Isu1p |
| [15211518](https://pubmed.ncbi.nlm.nih.gov/15211518/) | Yeast/computational | Yah1–Arh1 pair in heme A and FeSC assembly |
| [28615445](https://pubmed.ncbi.nlm.nih.gov/28615445/) | Review | ~30-protein ISC biogenesis pathway framework |
| [25008908](https://pubmed.ncbi.nlm.nih.gov/25008908/) | Clinical review | Exercise therapy benefits + trigger-avoidance guidance |
| [20091552](https://pubmed.ncbi.nlm.nih.gov/20091552/) | Cochrane review | Safety of strength/aerobic training in muscle disease |
| [18652078](https://pubmed.ncbi.nlm.nih.gov/18652078/) | Clinical review | Creatine in mitochondrial cytopathies (mixed benefit) |
| [28747430](https://pubmed.ncbi.nlm.nih.gov/28747430/) | In vitro | FDXR is sole reductase supplying both ferredoxins |

**Evidence source distribution:** Human clinical/genetics (~5 reports, <15 patients total) + mechanistic in vitro/structural + yeast model. No RCTs, no large cohorts, no vertebrate disease model.

---

## Limitations and Knowledge Gaps

1. **Extreme rarity:** Fewer than ~15 genotyped patients; all epidemiology (prevalence, incidence, sex ratio, survival) is anecdotal. No natural-history study or registry exists.
2. **No vertebrate animal model:** Mechanism rests on yeast, human cell lines, and structural biology; organ-level pathophysiology (why optic nerve and white matter are vulnerable) is inferred, not demonstrated in vivo.
3. **Genotype–phenotype correlation is immature:** Only a handful of variants; residual-function/severity relationships are not quantified. Some mutant proteins (P144L, c.200+4A>G) appear structurally near-normal, suggesting abundance/activity thresholds matter — but this is not fully resolved.
4. **No disease-specific therapy or trials:** All treatment evidence is extrapolated from general mitochondrial-myopathy literature; no FDX2-specific interventional data.
5. **Reversible leukoencephalopathy is mechanistically unexplained:** The basis for white-matter reversibility vs progressive optic atrophy is unknown.
6. **ICD coding** is non-specific (mapped to general mitochondrial myopathy codes).

---

## Proposed Follow-up Experiments / Actions

1. **Establish a vertebrate model:** Generate a conditional/tissue-specific (muscle, retinal ganglion cell, oligodendrocyte) *Fdx2* knockout or knock-in (p.P144L) mouse and/or zebrafish to test phenotype recapitulation (optic atrophy, episodic myopathy, leukoencephalopathy) and to serve as a preclinical therapeutic platform.
2. **International patient registry & natural-history study:** Pool genotyped cases via GeneMatcher/consortia to define prevalence, penetrance, crisis frequency/triggers, survival, and validated outcome measures.
3. **Genotype–function mapping:** Systematically measure residual FDX2 electron-transfer activity and protein stability across variants (c.1A>T, p.P144L, c.200+4A>G, and new alleles) to build a severity-prediction model.
4. **Biomarker development:** Evaluate plasma lactate/CK dynamics, FGF21/GDF15, and iron indices as diagnostic and prognostic biomarkers specific to FDX2 disease.
5. **Targeted therapeutic exploration:** Test whether iron-chelation, antioxidant/SOD2-supporting strategies, or substrate/cofactor supplementation rescue the Fe-S/respiration defect in patient cells and the animal model; evaluate AAV gene-replacement feasibility given the small 186-aa cDNA.
6. **Standardized crisis protocol:** Develop and disseminate a consensus acute-rhabdomyolysis management pathway (hydration, renal protection, trigger avoidance) for FDX2 and related ISC-biogenesis disorders.
7. **Pathway-wide diagnostics:** Ensure FDX2/FDX1L is included on all mitochondrial and Fe-S/ISC gene panels, with reflex RNA/functional testing for splice and missense variants.

---

*Report compiled from 5 investigation iterations, 9 confirmed findings, and 30 reviewed papers. Evidence is weighted toward human case reports and mechanistic in vitro/yeast/structural studies; interpretations involving organ-level vulnerability and episodic triggering are mechanistically reasoned and explicitly flagged as inferred where direct in vivo demonstration is lacking.*


## Artifacts

- [OpenScientist final report](FDX2-Related_Mitochondrial_Myopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](FDX2-Related_Mitochondrial_Myopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 11 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0020714` (5 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **mitochondrial myopathy, episodic, with optic atrophy and reversible leukoencephalopathy**
- `MedGen:1679560` (1 mention) - the report calls it "UMLS C5193223"; MedGen calls it **Acute abdomen**
- `HP:0000648` (1 mention) - the report calls it "Characteristic (majority)"; HP calls it **Optic atrophy**
- `HP:0000639` (1 mention) - the report calls it "Frequent"; HP calls it **Nystagmus**
- `HP:0003546` (1 mention) - the report calls it "Characteristic"; HP calls it **Exercise intolerance**
- `HP:0003198` (1 mention) - the report calls it "Characteristic"; HP calls it **Myopathy**
- `HP:0003236` (1 mention) - the report calls it "Frequent in crises"; HP calls it **Elevated circulating creatine kinase activity**
- `HP:0003128` (1 mention) - the report calls it "Frequent"; HP calls it **Lactic acidosis**
- `HP:0007141` (1 mention) - the report calls it "Characteristic"; HP calls it **Sensorimotor neuropathy**
- `HP:0002352` (1 mention) - the report calls it "Characteristic"; HP calls it **Leukoencephalopathy**
- `HP:0001919` (1 mention) - the report calls it "Subset"; HP calls it **Acute kidney injury**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0020714` - called "if available", "MONDO"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `GARD`.
