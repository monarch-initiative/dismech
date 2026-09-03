---
provider: openscientist
model: openscientist-autonomous
cached: true
start_time: '2026-09-03T12:44:51.623157'
end_time: '2026-09-03T12:44:51.626531'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 88
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_88-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_88-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 88
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 88** covering all of the
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

# Immunodeficiency 88 (IMD88): Human T-bet Deficiency — Comprehensive Disease Characteristics Report

## Summary

**Immunodeficiency 88 (IMD88; OMIM #619630; MONDO:0030483; MedGen C5562026)** is an ultra-rare, autosomal recessive **inborn error of IFN-γ immunity** caused by complete loss-of-function of the T-box transcription factor **T-bet**, encoded by **TBX21** (17q21.32; HGNC:11599; NCBI Gene 30009; UniProt O95936). It was first defined in a single consanguineous Moroccan boy who was homozygous for the in-frame indel **TBX21 c.466_471delGAGATGinsAGTTTA (p.E156_M157delinsSerLeu)**, a two-residue substitution within the T-box DNA-binding domain that abolishes DNA binding, impairs protein production and nuclear translocation, and prevents induction of *IFNG* ([PMID: 33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/)).

The disease is mechanistically remarkable because **one genetic lesion produces two distinct clinical arms**. First, loss of T-bet abolishes the development and IFN-γ output of **innate and innate-like lymphocytes** — natural killer (NK) cells, invariant NKT (iNKT), mucosal-associated invariant T (MAIT), and Vδ2⁺ γδ T cells — placing IMD88 firmly within the **Mendelian Susceptibility to Mycobacterial Disease (MSMD)** spectrum and producing disseminated *bacille Calmette-Guérin* (BCG) disease. Second, loss of T-bet-mediated repression of the **Th2 program** derepresses IL-4/IL-5/IL-9/IL-13 production, driving blood **eosinophilia** and persistent **upper-airway/asthma-like inflammation** ([PMID: 33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/); [PMID: 34160550](https://pubmed.ncbi.nlm.nih.gov/34160550/)).

Because IMD88 has been reported in only a single patient, most disease-level characteristics (epidemiology, prognosis, treatment algorithms) are **extrapolated** from the broader MSMD framework and from the well-characterized *Tbx21*-knockout mouse, which spontaneously recapitulates the allergic-airway arm of the human disease ([PMID: 11786643](https://pubmed.ncbi.nlm.nih.gov/11786643/)). This report organizes all available evidence across the 15 requested domains, flags where information is inferred rather than demonstrated, and supplies ontology term suggestions (HPO, GO, CL, UBERON, NCIT, MONDO) throughout to support knowledge-base curation.

---

## Key Findings

### Finding 1 — IMD88 is autosomal-recessive T-bet (TBX21) deficiency causing mycobacterial disease

IMD88 is catalogued as OMIM #619630, MONDO:0030483, and MedGen C5562026, and is caused by homozygous mutation in **TBX21** (T-box transcription factor 21; T-bet; OMIM 604895) located at chromosome **17q21.32**. The disorder was defined in a single index patient — a boy born to **consanguineous Moroccan parents** — reported by Yang et al. in *Cell* (2020). Whole-exome sequencing combined with genome-wide linkage identified a homozygous deletion/insertion in *TBX21*. In vitro reconstitution in HEK293T cells demonstrated that the mutant allele produces protein poorly, translocates to the nucleus poorly, fails to bind target regulatory DNA elements, and fails to induce *IFNG* transcription. The authors state directly: *"We report a patient with mycobacterial disease due to inherited deficiency of the transcription factor T-bet"* ([PMID: 33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/)). This establishes IMD88 as a monogenic, recessive loss-of-function disorder of a master immune transcription factor.

### Finding 2 — T-bet deficiency abolishes innate/innate-like IFN-γ-producing lymphocytes

The cellular basis of the mycobacterial susceptibility is a selective failure of the IFN-γ-producing innate compartment. The patient had **extremely low circulating counts of Mycobacterium-reactive NK, iNKT, MAIT, and Vδ2⁺ γδ T lymphocytes**, along with reduced classical Th1 cells; the residual cells produced abnormally little IFN-γ. Notably, CD8⁺ αβ T cells and non-classical CD4⁺ αβ TH1* cells produced IFN-γ normally in response to mycobacterial antigens but **could not compensate** for the missing innate-like output. The authors summarize: *"Human T-bet deficiency thus underlies mycobacterial disease by preventing the development of innate (NK) and innate-like adaptive lymphocytes (iNKT, MAIT, and Vδ2+ γδ T cells) and IFN-γ production by them"* ([PMID: 33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/)). This identifies the specific developmental and functional lesion (loss of a discrete IFN-γ-producing cellular compartment) as the proximate cause of disease.

### Finding 3 — Clinical phenotype: disseminated BCG, asthma/reactive airway disease, eosinophilia

The HPO/MedGen clinical profile (MedGen C5562026) includes **BCGosis / disseminated BCG infection (HP:0032262)**, **Asthma (HP:0002099)**, **Eosinophilia / increased eosinophil count (HP:0001880)**, and a general **Abnormality of the immune system (HP:0002715)**. OMIM #619630 notes **persistent reactive airway disease** associated with increased Th2 cytokine production and decreased IFN-γ. Despite serologic evidence of exposure to numerous viruses and bacteria, the patient did **not** develop other clinical infectious diseases, indicating a relatively selective, mycobacteria-dominant infection phenotype layered on top of an allergic/atopic airway disease ([PMID: 33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/)).

### Finding 4 — T-bet loss derepresses the Th2 program (the second mechanistic arm)

A follow-up study (Yang et al., *J Exp Med* 2021) established the mechanism of the allergic arm. The patient's mutant T-bet **failed to inhibit Th2 cytokine production (IL-4, IL-5, IL-9, IL-13)** when overexpressed in Th2 cells; Herpesvirus saimiri (HVS)-immortalized patient T cells overproduced Th2 cytokines; **plasma IL-5 and IL-13 were markedly elevated**; and patient CD4⁺ αβ T cells produced excess Th2 cytokines upon chronic stimulation **regardless of antigen specificity**, an effect reversed by wild-type T-bet. The result is **blood eosinophilia and persistent upper airway inflammation (UAI)**. The authors state: *"T-bet deficiency thus underlies the excessive production of Th2 cytokines, particularly IL-5 and IL-13, by CD4+ αβ T cells, causing blood eosinophilia and UAI"* ([PMID: 34160550](https://pubmed.ncbi.nlm.nih.gov/34160550/)). This confirms that the atopic manifestations are a direct consequence of the same TBX21 lesion, not a coincidental comorbidity.

### Finding 5 — The Tbx21-knockout mouse recapitulates the asthma/airway arm

Finotto et al. (*Science* 2002) showed that **mice with targeted deletion of the *Tbx21* (T-bet) gene**, and SCID mice reconstituted with CD4⁺ cells from T-bet-knockout mice, **spontaneously developed multiple physiological and inflammatory features characteristic of asthma in the absence of allergen exposure**. Human asthmatic airway T cells showed reduced T-bet expression. The authors report: *"Mice with a targeted deletion of the T-bet gene and severe combined immunodeficient mice receiving CD4+ cells from T-bet knockout mice spontaneously demonstrated multiple physiological and inflammatory features characteristic of asthma"* ([PMID: 11786643](https://pubmed.ncbi.nlm.nih.gov/11786643/)). This provides a validated animal model for the allergic-airway component of IMD88, predating the human disease description by nearly two decades.

### Finding 6 — IMD88 within the MSMD framework: diagnosis, treatment, prognosis

MSMD is defined by inborn errors of IFN-γ immunity, rendering patients *"highly and selectively susceptible to weakly virulent mycobacteria, such as environmental mycobacteria and Bacillus Calmette-Guérin vaccines"* ([PMID: 32025907](https://pubmed.ncbi.nlm.nih.gov/32025907/)). A systematic review of **830 MSMD patients** ([PMID: 38341181](https://pubmed.ncbi.nlm.nih.gov/38341181/)) reported a mean age of ~10.4 years, 52.5% male, a positive family history in 45.5%, highest reported frequencies in Iran/Turkey/Saudi Arabia, and 299 unique mutations across 21 genes. **Lymphadenopathy was the most common manifestation (45.5%)**, followed by fever (30.2%), organomegaly (24.8%), and sepsis (20.8%); *"Lymphadenopathy was the most common clinical manifestation of MSMD, reported in 378 (45.5%) cases."* MSMD carries substantial mortality, driven mostly by impaired control of infection. IMD88 (TBX21/T-bet deficiency) is one of these genetic etiologies, and its clinical management, diagnostic approach, and prognosis are reasonably extrapolated from this larger cohort.

### Finding 7 — Exact TBX21 variant and gene/protein annotations

The index patient is **homozygous for TBX21 c.466_471delGAGATGinsAGTTTA**, an **in-frame insertion/deletion in exon 1** that replaces two highly conserved amino acids, **E156 and M157 (p.E156_M157delinsSerLeu)**, within the **T-box DNA-binding domain**. Parents were heterozygous carriers (WT/M); the patient was homozygous (M/M). The variant is **private** (not a recurrent/founder allele; absent as a benign homozygote in gnomAD). Gene/protein annotations: human **TBX21** (HGNC:11599; NCBI Gene 30009; UniProt O95936; 17q21.32); mouse ortholog **Tbx21** (NCBI Gene 57765; MGI:1888984; chromosome 11). The functional class is **complete autosomal-recessive loss of function** — the mutant protein shows impaired production, impaired nuclear translocation, and abolished DNA binding, failing to induce IFN-γ ([PMID: 33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/)).

---

## Report by Requested Domain

### 1. Disease Information

- **Overview:** IMD88 is a monogenic inborn error of immunity in which loss of the master Th1/innate transcription factor T-bet produces a combined phenotype of **mycobacterial susceptibility** (MSMD-spectrum) and **allergic airway disease with eosinophilia**.
- **Key identifiers:** OMIM **#619630**; MONDO **:0030483**; MedGen **C5562026**; gene OMIM **604895** (TBX21). No dedicated Orphanet or distinct ICD-10/ICD-11 code exists for this ultra-rare entity; it is best coded under broad immunodeficiency categories (e.g., ICD-10 **D84.9**, immunodeficiency unspecified; ICD-11 **4A00** primary immunodeficiencies) and, for the infectious arm, under atypical mycobacterial infection. MeSH lacks a specific descriptor; relevant MeSH concepts include *Mycobacterium Infections*, *Immunologic Deficiency Syndromes*, and *T-Box Domain Proteins*.
- **Synonyms / alternative names:** "Immunodeficiency 88"; **human T-bet deficiency**; **TBX21 deficiency**; "Mendelian susceptibility to mycobacterial disease due to T-bet deficiency."
- **Information source:** Disease-level aggregated resources (OMIM, MONDO, MedGen) built on **individual-patient** primary reports (Yang et al. 2020/2021) — i.e., a single-patient basis, not EHR-scale or registry data.

### 2. Etiology

- **Causal factor:** Purely **genetic** — biallelic loss-of-function in *TBX21*. Environmental exposure (**BCG vaccination**) acts as the trigger that unmasks the mycobacterial susceptibility; the vaccine strain itself becomes the disseminating pathogen.
- **Genetic risk factors:** The single causal genotype is homozygous **TBX21 c.466_471delGAGATGinsAGTTTA**. **Consanguinity** is a major risk enabler (parents were related, consistent with autosomal-recessive inheritance and homozygosity by descent). No susceptibility loci or modifier genes have been formally mapped in this ultra-rare disease.
- **Environmental risk factors:** Exposure to **live BCG vaccine** or environmental non-tuberculous mycobacteria is the key environmental trigger for the infectious arm. Allergen and airway-irritant exposures plausibly modulate the atopic arm (inferred from mouse/asthma biology).
- **Protective factors:** By direct inference, **avoidance of live mycobacterial vaccines** in genetically at-risk siblings is protective. No genetic protective/modifier alleles are described.
- **Gene–environment interaction:** The paradigmatic GxE is **TBX21 loss × BCG exposure → disseminated BCGosis**; without the environmental mycobacterial challenge the infectious phenotype may not manifest, whereas the Th2/eosinophilia arm appears to be cell-intrinsic and largely antigen-independent ([PMID: 34160550](https://pubmed.ncbi.nlm.nih.gov/34160550/)).

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Severity | Frequency (n=1 + MSMD context) |
|---|---|---|---|---|---|
| Disseminated BCG infection (BCGosis) | Clinical sign / infection | HP:0032262 | Childhood (post-vaccination) | Severe | Present in index patient; BCG complications in ~55% of BCG-vaccinated MSMD ([PMID: 36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/)) |
| Asthma / reactive airway disease | Clinical sign | HP:0002099 | Childhood | Moderate, persistent | Present in index patient |
| Eosinophilia | Laboratory abnormality | HP:0001880 | Childhood | Moderate–marked | Present in index patient |
| Elevated Th2 cytokines (IL-5, IL-13) | Laboratory abnormality | (no direct HPO) | Childhood | Marked | Present ([PMID: 34160550](https://pubmed.ncbi.nlm.nih.gov/34160550/)) |
| Upper airway inflammation | Clinical sign | HP:0012384 (airway) | Childhood | Persistent | Present |
| Abnormality of the immune system | General | HP:0002715 | Childhood | — | Present |
| Lymphadenopathy (MSMD-context) | Clinical sign | HP:0002716 | Childhood | Variable | Most common MSMD feature (45.5%) ([PMID: 38341181](https://pubmed.ncbi.nlm.nih.gov/38341181/)) |

- **Progression:** The mycobacterial arm is **episodic/infection-driven**; the atopic arm is **chronic/persistent**.
- **Quality-of-life impact:** No disease-specific QoL instruments have been applied. By analogy, disseminated mycobacterial disease imposes major morbidity (hospitalization, prolonged multidrug therapy) and chronic asthma reduces daily functioning; formal EQ-5D/SF-36 data are **not available**.

### 4. Genetic / Molecular Information

- **Causal gene:** **TBX21** (T-bet), 17q21.32; gene OMIM 604895; HGNC:11599; NCBI Gene 30009; UniProt O95936.
- **Pathogenic variant:** **c.466_471delGAGATGinsAGTTTA (p.E156_M157delinsSerLeu)**, in-frame indel in exon 1, within the T-box DNA-binding domain. **Variant type:** in-frame delins (structural at protein level, altering two conserved residues). **Classification:** Pathogenic by ACMG-style functional evidence (abolished DNA binding, failure to induce IFN-γ, segregation with recessive inheritance, absence in gnomAD). **Allele frequency:** private; absent as benign homozygote in gnomAD. **Origin:** germline. **Functional consequence:** complete **loss of function** (not gain-of-function or dominant-negative in the heterozygous state — parents unaffected).
- **Modifier genes / epigenetics / chromosomal abnormalities:** None described for IMD88 specifically. Relevant epigenetic biology: T-bet normally shapes the chromatin landscape of the *IFNG* locus and represses Th2 loci; the Th17→Th1 plasticity literature notes extensive epigenetic priming of *IFNG* controlled by T-bet-family factors ([PMID: 29275836](https://pubmed.ncbi.nlm.nih.gov/29275836/)). No large-scale cytogenetic abnormalities are involved.

### 5. Environmental Information

- **Environmental factors:** Live attenuated **BCG vaccine** and environmental non-tuberculous mycobacteria are the operative environmental agents.
- **Lifestyle factors:** Not characterized; allergen exposure may aggravate the airway phenotype (inferred).
- **Infectious agents:** ***Mycobacterium bovis* BCG** (disseminated disease in the index patient) and, by MSMD analogy, environmental mycobacteria, *M. tuberculosis*, and *Salmonella* species ([PMID: 32025907](https://pubmed.ncbi.nlm.nih.gov/32025907/); [PMID: 36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Homozygous **TBX21 c.466_471delinsAGTTTA (p.E156_M157delinsSerLeu)** **leads to** a T-bet protein with two altered residues in the T-box DNA-binding domain (demonstrated).
2. This **results in** impaired protein production, impaired nuclear translocation, and **abolished binding to target DNA regulatory elements** (demonstrated in HEK293T reconstitution) ([PMID: 33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/)).
3. Loss of T-bet transcriptional activity **branches** into two arms:

   **Arm A (immunodeficiency / mycobacterial disease):**
   - 4a. Failure to activate the T-bet-dependent Th1/innate transcriptional program **leads to** failed development and maturation of **NK, iNKT, MAIT, and Vδ2⁺ γδ T lymphocytes** (demonstrated: extremely low counts).
   - 5a. This **results in** loss of early, innate **IFN-γ production** against mycobacteria (demonstrated).
   - 6a. Deficient IFN-γ **leads to** impaired macrophage activation and failure to control weakly virulent mycobacteria (inferred from the MSMD paradigm) ([PMID: 32025907](https://pubmed.ncbi.nlm.nih.gov/32025907/)).
   - 7a. This **results in** **disseminated BCG disease** and MSMD-spectrum susceptibility (demonstrated clinically).

   **Arm B (allergic airway disease / eosinophilia):**
   - 4b. Loss of T-bet-mediated **repression of the Th2 program** **leads to** derepressed IL-4/IL-5/IL-9/IL-13 output by CD4⁺ αβ T cells, independent of antigen specificity (demonstrated) ([PMID: 34160550](https://pubmed.ncbi.nlm.nih.gov/34160550/)).
   - 5b. Elevated **IL-5** **results in** **blood eosinophilia**; elevated **IL-13** **results in** airway mucus/inflammation (demonstrated: elevated plasma IL-5/IL-13).
   - 6b. Sustained type-2 inflammation **leads to** **persistent upper-airway inflammation and asthma/reactive airway disease** (demonstrated clinically; recapitulated in *Tbx21*-KO mice, [PMID: 11786643](https://pubmed.ncbi.nlm.nih.gov/11786643/)).

- **Molecular pathways:** IFN-γ–STAT1–T-bet axis (upstream), IL-12/IL-12Rβ1 signaling context of MSMD, and the Th1/Th2 master-regulator circuit (T-bet vs GATA3). TREM-2 has been shown to feed into T-bet induction via the CD3ζ-ZAP70/IFN-γR–STAT1/STAT4 route in the context of *M. tuberculosis* ([PMID: 34623322](https://pubmed.ncbi.nlm.nih.gov/34623322/)).
- **Cellular processes:** Lymphocyte lineage commitment/differentiation; type-1 vs type-2 immune polarization; macrophage activation; inflammation.
- **Protein dysfunction:** DNA-binding loss of function of a transcription factor (not misfolding/aggregation).
- **Immune involvement:** Combined **immunodeficiency** (innate IFN-γ arm) and **immune dysregulation/allergy** (Th2 arm) — a rare "two diseases, one gene" configuration.
- **Suggested GO terms:** GO:0045063 (T-helper 1 cell differentiation), GO:0045064 (T-helper 2 cell differentiation), GO:0032609 (interferon-gamma production), GO:0003700 (DNA-binding transcription factor activity), GO:0006357 (regulation of transcription by RNA Pol II).
- **Suggested CL terms:** CL:0000623 (NK cell), CL:0000814 (mature NK T cell / iNKT), CL:0000940 (mucosal invariant T cell / MAIT), CL:0000798 (gamma-delta T cell), CL:0000546 (T-helper 2 cell), CL:0000545 (T-helper 1 cell), CL:0000771 (eosinophil).

### 7. Anatomical Structures Affected

- **Organ/system level:** **Immune/lymphoid system** (primary); **respiratory system** — airways/lungs (UBERON:0001004 respiratory system; UBERON:0002048 lung; UBERON:0001005 respiratory airway); **upper airway / nasal mucosa** (UBERON:0001728 nasopharynx region). Secondary involvement in disseminated BCG can affect **lymph nodes** (UBERON:0000029), **spleen/liver** (organomegaly in MSMD context), **skin**, and **bone**.
- **Tissue/cell level:** Airway mucosal epithelium and submucosal inflammatory infiltrate (eosinophils, Th2 cells); lymphoid tissue with deficient innate-like lymphocytes. Cell populations: NK, iNKT, MAIT, Vδ2⁺ γδ T (deficient); Th2 cells and eosinophils (expanded).
- **Subcellular level:** **Nucleus** (GO:0005634) — the site of the primary transcription-factor defect (impaired nuclear translocation and DNA binding).
- **Localization/lateralization:** Airway disease is **bilateral/diffuse**; disseminated BCG is **systemic**.

### 8. Temporal Development

- **Onset:** **Childhood**, typically after BCG vaccination for the infectious arm; airway/atopic features also present in childhood. Onset is **subacute-to-chronic**.
- **Progression:** Infectious episodes are **episodic/relapsing** with treatment; airway disease is **chronic and persistent**. Disease is **lifelong** (germline monogenic).
- **Critical period:** The **peri-vaccination window** (neonatal BCG in endemic regions) is the key period of vulnerability and the key opportunity for prevention (avoiding live BCG in at-risk siblings).

### 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic loss of function; heterozygous parents unaffected).
- **Penetrance/expressivity:** Cannot be estimated from n=1; MSMD generally shows incomplete penetrance and variable expressivity across genes.
- **Epidemiology:** **Ultra-rare** — one reported patient worldwide. No prevalence/incidence figures exist for IMD88 specifically. MSMD as a class: mean age at presentation ~10.4 yr, 52.5% male, positive family history 45.5%, clustering in Iran/Turkey/Saudi Arabia and consanguineous populations ([PMID: 38341181](https://pubmed.ncbi.nlm.nih.gov/38341181/)); in Morocco, MSMD comprised ~50% of genetically confirmed innate/intrinsic IEI ([PMID: 41209815](https://pubmed.ncbi.nlm.nih.gov/41209815/)), and *TBX21* accounted for 1 of 22 MSMD patients across 15 Moroccan kindreds ([PMID: 36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/)).
- **Consanguinity/founder:** **Consanguinity** is central to case ascertainment; the variant is **private/non-founder**.
- **Carrier frequency:** Not established; expected extremely low given the private allele.

### 10. Diagnostics

- **Immunologic laboratory tests:** Flow-cytometric enumeration of **NK, iNKT, MAIT, and Vδ2⁺ γδ T cells** (markedly reduced); functional **IFN-γ production assays** (BCG ± IL-12 stimulation of whole blood), which are reduced ([PMID: 33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/); [PMID: 36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/)). **Blood eosinophil count** (elevated; LOINC 26449-9) and **plasma IL-5/IL-13** (elevated) support the atopic arm.
- **Biomarkers:** Low innate IFN-γ output; elevated Th2 cytokines (IL-5, IL-13); eosinophilia.
- **Genetic testing (definitive):** **Whole-exome sequencing** (as used in the index case) or **whole-genome sequencing**, ideally combined with linkage/homozygosity mapping in consanguineous families; targeted **TBX21** single-gene/panel testing once suspected. Upfront genomic sequencing is increasingly recommended for primary atopic disorders and IEI with red-flag features ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)). CMA/karyotype/FISH/mtDNA/repeat testing are **not applicable**.
- **Clinical criteria/differential:** Diagnosis rests on the **MSMD phenotype** (susceptibility to weakly virulent mycobacteria) plus molecular confirmation. Differential diagnosis: other MSMD genes (**IL12RB1, IL12B, IFNGR1/2, STAT1, ISG15, IRF8, SPPL2A, TYK2, RORC, JAK1, CYBB, NEMO**) ([PMID: 30264912](https://pubmed.ncbi.nlm.nih.gov/30264912/)); and, for the atopic arm, other **primary atopic disorders** and hyper-eosinophilic syndromes.
- **Screening:** In BCG-endemic, consanguineous families, **cascade genetic screening** of siblings and **deferral of live BCG** until MSMD is excluded is advised ([PMID: 36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/)).

### 11. Outcome / Prognosis

- **Survival/mortality:** No IMD88-specific survival data (n=1). MSMD as a class carries **substantial mortality driven by uncontrolled infection**; prognosis depends on the specific genetic etiology and infection control ([PMID: 38341181](https://pubmed.ncbi.nlm.nih.gov/38341181/)).
- **Morbidity:** Recurrent/disseminated mycobacterial infection and chronic asthma/eosinophilic airway disease. The index patient did not develop other clinical infections despite broad serologic exposure, suggesting a relatively selective infection risk.
- **Prognostic factors (inferred):** Timeliness of antimycobacterial therapy, avoidance of further live-vaccine exposure, degree of residual IFN-γ immunity, and access to HSCT would be expected to modify outcome.

### 12. Treatment

*(All treatment is extrapolated from MSMD and Th2-directed asthma care; no IMD88-specific trials exist.)*

- **Antimycobacterial pharmacotherapy:** Prolonged **multidrug antimycobacterial regimens** (e.g., rifampin, isoniazid, ethambutol, a macrolide/fluoroquinolone as appropriate) for disseminated BCG/mycobacterial disease (NCIT: antimycobacterial/antitubercular agents).
- **Immunomodulation:** **Recombinant IFN-γ1b** (NCIT:C1732, Interferon Gamma-1b) as adjunctive therapy in IFN-γ-pathway MSMD; rationale is to bolster deficient IFN-γ signaling, though efficacy in a downstream transcription-factor defect that impairs IFN-γ *production* and responsiveness is uncertain.
- **Definitive therapy:** **Hematopoietic stem cell transplantation (HSCT)** (NCIT:C15431) is potentially curative for severe combined IFN-γ-immunity defects; candidacy must be individualized.
- **Anti-Th2 / asthma therapy:** Standard asthma control (inhaled corticosteroids, bronchodilators) plus **biologics targeting the type-2 axis** — anti-IL-5/anti-IL-5Rα (mepolizumab/benralizumab), anti-IL-4Rα (dupilumab), or anti-IgE (omalizumab) — are mechanistically rational given elevated IL-5/IL-13 and eosinophilia ([PMID: 34160550](https://pubmed.ncbi.nlm.nih.gov/34160550/)).
- **Preventive:** **Avoid live BCG** and other live vaccines.
- **Pharmacogenomics/experimental:** None specific; **gene therapy/gene editing of TBX21** is conceptual only.

### 13. Prevention

- **Primary prevention:** In affected kindreds, **withhold/defer live BCG vaccination** in newborn siblings until MSMD is genetically excluded ([PMID: 36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/)).
- **Secondary prevention:** **Cascade genetic screening** and early flow-cytometric/IFN-γ functional testing of at-risk relatives; early recognition of mycobacterial disease.
- **Tertiary prevention:** Prompt, adequate antimycobacterial therapy and type-2-directed asthma control to prevent complications.
- **Genetic counseling:** Recessive inheritance with 25% sibling recurrence risk; **prenatal/preimplantation testing** possible once the familial variant is known. Consanguinity counseling is relevant.

### 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** Mouse **Tbx21** (NCBI Gene 57765; MGI:1888984; chromosome 11) is the direct ortholog of human **TBX21**. T-bet is evolutionarily conserved as the master Th1/type-1 regulator across mammals; ILC1s and Th1 cells across species depend on it ([PMID: 35163778](https://pubmed.ncbi.nlm.nih.gov/35163778/); [PMID: 33126494](https://pubmed.ncbi.nlm.nih.gov/33126494/)).
- **Natural disease in other species:** No spontaneously occurring companion-animal or wildlife equivalent of IMD88 has been reported (no dedicated OMIA entry). Disease knowledge is confined to engineered mouse models.
- **Zoonotic/transmission:** Not applicable — IMD88 is a non-transmissible germline disorder.

### 15. Model Organisms

- **Primary model:** ***Tbx21*/T-bet knockout mouse** — spontaneously develops asthma-like airway physiology and inflammation without allergen challenge, and SCID mice reconstituted with T-bet-KO CD4⁺ cells reproduce the phenotype ([PMID: 11786643](https://pubmed.ncbi.nlm.nih.gov/11786643/)).
- **Model types available:** Constitutive knockout; adoptive-transfer/reconstitution models; conditional/CD4-specific approaches used in related TREM-2/T-bet work ([PMID: 34623322](https://pubmed.ncbi.nlm.nih.gov/34623322/)).
- **Phenotype recapitulation:** The mouse KO **strongly recapitulates the allergic-airway arm** (Th2 derepression, airway inflammation). The mycobacterial-susceptibility arm is supported by the general dependence of Th1/innate IFN-γ immunity on T-bet, but the human innate/innate-like lymphocyte deficiency (iNKT/MAIT/Vδ2⁺) is only partially mirrored in mice, whose innate-like compartments differ.
- **In-vitro models:** HEK293T reconstitution assays (used to prove the DNA-binding/IFN-γ-induction defect) and HVS-immortalized patient T-cell lines (used to prove Th2 overproduction) ([PMID: 33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/); [PMID: 34160550](https://pubmed.ncbi.nlm.nih.gov/34160550/)).
- **Resources:** MGI (Tbx21, MGI:1888984); IMPC/KOMP for T-bet alleles.

---

## Mechanistic Model / Interpretation

```
          Homozygous TBX21 c.466_471delinsAGTTTA (p.E156_M157delinsSerLeu)
                                  |
                (T-box DNA-binding domain: 2 conserved residues altered)
                                  |
        Impaired protein production + nuclear import + ABOLISHED DNA binding
                                  |
                     Loss of T-bet transcriptional function
                    /                                        \
     ARM A: Loss of ACTIVATION                     ARM B: Loss of REPRESSION
     of Th1/innate program                          of Th2 program
              |                                              |
   Failed development/IFN-γ of                    Derepressed IL-4/IL-5/
   NK, iNKT, MAIT, Vδ2+ γδ T                       IL-9/IL-13 (antigen-independent)
              |                                              |
   Deficient innate IFN-γ                          ↑ IL-5 → eosinophilia
              |                                     ↑ IL-13 → airway inflammation
   Impaired macrophage control                              |
   of weakly virulent mycobacteria                 Persistent asthma / upper
              |                                     airway inflammation
   DISSEMINATED BCG / MSMD                          (recapitulated in Tbx21-KO mouse)
```

The unifying insight is that **T-bet is simultaneously an activator of type-1 immunity and a repressor of type-2 immunity.** A single loss-of-function lesion therefore removes both functions, yielding the paradoxical combination of an **immunodeficiency** (susceptibility to mycobacteria) and an **immune-dysregulation/allergy** phenotype (eosinophilic airway disease) in the same patient. Arm A is the demonstrated cause of the MSMD phenotype and is developmental (missing cell lineages); Arm B is cell-intrinsic, antigen-independent, and directly reversible by wild-type T-bet in vitro. The mouse model validates Arm B decisively and supports Arm A through the conserved T-bet dependence of Th1/IFN-γ immunity.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [33296702](https://pubmed.ncbi.nlm.nih.gov/33296702/) | *Human T-bet Governs Innate and Innate-like Adaptive IFN-γ Immunity against Mycobacteria* | Human clinical + in vitro | Defines IMD88; identifies variant; proves DNA-binding/IFN-γ defect; establishes Arm A cellular mechanism |
| [34160550](https://pubmed.ncbi.nlm.nih.gov/34160550/) | *High Th2 cytokine levels and upper airway inflammation in human inherited T-bet deficiency* | Human clinical + in vitro | Proves Arm B: Th2 derepression → IL-5/IL-13 → eosinophilia/UAI |
| [11786643](https://pubmed.ncbi.nlm.nih.gov/11786643/) | *T-bet KO mice spontaneously develop asthma features* | Mouse model | Validates the allergic-airway arm; provides model organism |
| [32025907](https://pubmed.ncbi.nlm.nih.gov/32025907/) | *MSMD: recent discoveries* | Review | Defines MSMD disease class to which IMD88 belongs |
| [38341181](https://pubmed.ncbi.nlm.nih.gov/38341181/) | *830 MSMD patients: systematic review* | Human cohort | Epidemiologic/clinical context, prognosis |
| [36630059](https://pubmed.ncbi.nlm.nih.gov/36630059/) | *MSMD in 22 Moroccan patients (incl. 1 TBX21)* | Human cohort | Population context; BCG-complication rate; TBX21 in Moroccan cohort |
| [41209815](https://pubmed.ncbi.nlm.nih.gov/41209815/) | *Innate/intrinsic immunity in Morocco* | Human registry | MSMD prevalence in Moroccan IEI registry |
| [30264912](https://pubmed.ncbi.nlm.nih.gov/30264912/) | *MSMD: 2014–2018 update* | Review | Differential diagnosis / MSMD gene list |
| [34623322](https://pubmed.ncbi.nlm.nih.gov/34623322/) | *TREM-2 promotes Th1 via CD3ζ-ZAP70* | Mouse/human mechanistic | Upstream signaling context for T-bet induction |
| [39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/) | *Rapid identification of primary atopic disorders by genomic sequencing* | Review | Diagnostic strategy (upfront WGS) |
| [35163778](https://pubmed.ncbi.nlm.nih.gov/35163778/) / [33126494](https://pubmed.ncbi.nlm.nih.gov/33126494/) | *ILCs / CD4 Th subsets reviews* | Review | T-bet/GATA3 master-regulator biology; conservation |
| [29275836](https://pubmed.ncbi.nlm.nih.gov/29275836/) | *Th17 plasticity / IFNG epigenetics* | Review | Epigenetic context of T-bet/IFNG regulation |

---

## Limitations and Knowledge Gaps

1. **Single-patient basis (n=1).** Every disease-specific characteristic — penetrance, expressivity, full phenotype spectrum, natural history, treatment response, prognosis — rests on one individual. Population-level parameters are borrowed from the broader MSMD class and must be interpreted as inference, not established fact for IMD88.
2. **No treatment evidence.** No therapy has been tested specifically in T-bet deficiency. IFN-γ1b efficacy is uncertain because the defect lies downstream at a transcription factor that impairs both IFN-γ production and responsiveness. Type-2 biologics (anti-IL-5/IL-4Rα) are mechanistically rational but untested in this disorder.
3. **Incomplete model concordance.** The mouse *Tbx21*-KO robustly models the airway/Th2 arm but only partially models the human innate/innate-like lymphocyte deficiency, because murine iNKT/MAIT/γδ compartments differ from human.
4. **No epidemiology, QoL, imaging, or omics datasets** exist for IMD88 as a distinct entity; ICD coding and Orphanet classification are not specifically assigned.
5. **Modifier genetics and penetrance** are entirely unknown; whether heterozygous carriers have subtle immune/atopic phenotypes has not been examined.

---

## Proposed Follow-up Experiments / Actions

1. **Case-finding / cohort expansion:** Systematically screen MSMD and unexplained eosinophilia/severe-asthma cohorts (especially consanguineous, BCG-endemic populations) for biallelic *TBX21* variants via WES/WGS and GeneMatcher, to move IMD88 beyond n=1 and define its true phenotype spectrum and penetrance.
2. **Therapeutic proof-of-concept:** Evaluate **type-2-targeting biologics (mepolizumab/benralizumab/dupilumab)** for the eosinophilic-airway arm and formally assess **HSCT** outcomes and **IFN-γ1b** response for the mycobacterial arm in any newly identified patients.
3. **Single-cell/transcriptomic profiling:** Perform scRNA-seq/ATAC-seq on patient PBMCs to map, at cellular resolution, the loss of innate-like lymphocytes and the derepressed Th2 program, and to identify T-bet direct target loci that fail activation vs fail repression.
4. **Structure-function studies:** Model p.E156_M157delinsSerLeu in the T-box domain (crystallography/AlphaFold + EMSA) to define precisely how the two-residue substitution abolishes DNA binding, informing potential correction strategies.
5. **Refined animal models:** Generate **humanized or knock-in mice carrying the patient allele**, and models that better reconstitute human innate-like lymphocyte compartments, to test the mycobacterial arm and candidate therapies.
6. **Carrier / heterozygote studies:** Assess immune and atopic phenotypes in obligate heterozygous relatives to determine whether *TBX21* haploinsufficiency contributes to common asthma/atopy risk.

---

*Report compiled from 5 investigation iterations, 7 confirmed findings, and 22 reviewed papers. Evidence types are distinguished throughout as human clinical, model organism, in vitro, or review/inference. Where information is unavailable for IMD88 specifically, this is stated explicitly and MSMD-class data are used as the nearest available proxy.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_88-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_88-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

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
