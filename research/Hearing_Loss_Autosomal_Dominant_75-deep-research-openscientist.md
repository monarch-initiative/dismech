---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-04T13:30:23.149091'
end_time: '2026-09-04T13:43:43.676825'
duration_seconds: 800.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hearing Loss Autosomal Dominant 75
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hearing_Loss_Autosomal_Dominant_75-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hearing_Loss_Autosomal_Dominant_75-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing Loss Autosomal Dominant 75
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Dominant 75** covering all of the
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

# Hearing Loss Autosomal Dominant 75 (DFNA75): A Comprehensive Disease Characteristics Report

**Gene:** *TRRAP* (Transformation/tRanscription domain-Associated Protein) · **Disease OMIM:** #618778 · **Gene OMIM:** *603015 · **Category:** Mendelian (monogenic, autosomal dominant, nonsyndromic sensorineural hearing loss)

## Summary

**Hearing Loss Autosomal Dominant 75 (DFNA75; OMIM #618778)** is a rare Mendelian, autosomal dominant, nonsyndromic sensorineural hearing loss (ADNSHL) caused by heterozygous pathogenic variants in **TRRAP** (Transformation/tRanscription domain-Associated Protein; HGNC:12347; NCBI Gene 8295; 7q22.1; OMIM *603015). The locus/phenotype was defined by Xia et al. (2019), who identified the co-segregating variant **NM_001244580 c.511C>T, p.(Arg171Cys)** across a three-generation Chinese family with post-lingual, progressive ADNSHL, plus three additional novel TRRAP variants in a screen of 66 sporadic hearing-loss cases. Functional validation in zebrafish (morpholino knockdown and CRISPR/Cas9 knockout of *trrap*) produced significant inner-ear defects, establishing TRRAP as required for inner-ear development ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)).

Clinically, DFNA75 presents as **bilateral, post-lingual (onset after speech acquisition), progressive cochlear sensorineural hearing loss**. Because nonsyndromic hearing impairment is almost exclusively cochlear, the resulting deficit is sensorineural, and postlingual nonsyndromic forms typically follow an autosomal dominant trait — consistent with the DFNA (autosomal Dominant, NonsyndromicA) locus series to which DFNA75 belongs. There is no gene-specific or curative therapy; management is supportive, following the general SNHL pathway of hearing amplification for mild-to-moderate loss and cochlear implantation for severe-to-profound loss.

TRRAP is a biologically pivotal protein: the only enzymatically inactive member of the phosphatidylinositol 3-kinase–related kinase (PIKK) family, it functions as an adaptor/scaffold for multiple histone acetyltransferase (HAT) complexes (STAGA/SAGA with GCN5; TIP60/NuA4) and as a scaffold for key transcription factors (E2F1, c-Myc, p53, Sp1). Distinct TRRAP missense alleles cause the allelic multisystem neurodevelopmental disorder **DEDDFA** (Developmental delay with or without dysmorphic facies and autism; OMIM #618454), and recurrent *somatic* TRRAP mutations (p.Ser722Phe) act as oncogenic drivers in melanoma — illustrating that the clinical consequence of TRRAP perturbation is strongly dependent on the specific variant, its domain location, and germline versus somatic context.

---

## Section 1 — Disease Information

**Overview.** DFNA75 is a form of autosomal dominant, nonsyndromic (isolated, no other organ system involvement) sensorineural hearing loss. It belongs to the large, genetically heterogeneous DFNA series of dominant nonsyndromic deafness loci. Hearing loss is the sole clinical manifestation; affected individuals do not have the multisystem features seen in TRRAP-related neurodevelopmental disorder.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #618778 (Deafness, autosomal dominant 75) |
| OMIM (gene) | *603015 (TRRAP) |
| Gene symbol / HGNC | TRRAP / HGNC:12347 |
| NCBI Gene | 8295 |
| Ensembl | ENSG00000196367 |
| UniProt | Q9Y4A5 |
| Cytogenetic location | 7q22.1 |
| MONDO | Corresponds to the OMIM #618778 concept ("autosomal dominant nonsyndromic hearing loss 75") |

**Synonyms / alternative names:** DFNA75; Deafness, autosomal dominant 75; Autosomal dominant nonsyndromic sensorineural hearing loss type 75; TRRAP-related autosomal dominant hearing loss.

**Information source.** Disease-level knowledge here is aggregated from Mendelian genetics resources (OMIM) and the primary literature (a single index family plus sporadic-case screening), rather than from individual EHR data. The defining evidence is a family-based segregation and functional study ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)).

---

## Section 2 — Etiology

**Disease causal factors.** DFNA75 is a **monogenic, genetic** disorder. The primary cause is a heterozygous pathogenic variant in *TRRAP*. There is no established infectious or environmental cause of the Mendelian disease itself, though general environmental insults (noise, ototoxic drugs, aging) can independently compound sensorineural hearing loss in any individual.

**Genetic risk factors.** The causal variant class is heterozygous coding variants in *TRRAP*. The index variant is **c.511C>T, p.(Arg171Cys)** (NM_001244580), which co-segregated with disease across three generations; three additional novel TRRAP variants were identified among 66 sporadic hearing-loss cases ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)). A subsequent report ([PMID: 40004049](https://pubmed.ncbi.nlm.nih.gov/40004049/)) describes a further novel pathogenic TRRAP variant in ADNSHL, reinforcing TRRAP as a bona fide ADNSHL gene.

**Environmental risk factors / protective factors / gene-environment interactions.** No disease-specific environmental risk factors, protective factors, or gene-environment interactions have been characterized for DFNA75. As with other progressive SNHL, avoidance of additional cochlear insults (excessive noise exposure, ototoxic aminoglycosides/platinum agents) is a prudent, non-specific protective measure, but no DFNA75-specific modifier has been demonstrated. This is a **knowledge gap**.

---

## Section 3 — Phenotypes

**Core phenotype: sensorineural hearing loss.** The defining and essentially sole phenotype of DFNA75 is bilateral sensorineural hearing loss. Because nonsyndromic hearing impairment is almost exclusively caused by cochlear defects, affected patients suffer sensorineural (rather than conductive) loss ([PMID: 15850684](https://pubmed.ncbi.nlm.nih.gov/15850684/)).

**Phenotype characteristics.**

| Characteristic | DFNA75 |
|---|---|
| Phenotype type | Clinical sign / laboratory (audiometric) abnormality — sensorineural hearing loss |
| Age of onset | Post-lingual (after speech development); adult/late-childhood onset |
| Severity | Variable; progresses from milder to more severe over time |
| Progression | Progressive (worsens with age) |
| Laterality | Bilateral |
| Frequency among affected | Essentially the defining feature of affected individuals |

The index family is explicitly described as having **"post-lingual progressive ADNSHL"** ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)). Post-lingual onset means hearing and speech develop normally before decline, which typically preserves spoken-language competence and favors auditory rehabilitation outcomes.

**Quality-of-life impact.** Progressive bilateral SNHL impairs speech perception (particularly in noise), communication, education/occupational function, and social participation, and is associated with tinnitus in a subset of SNHL patients. Disease-specific QoL instruments for DFNA75 have not been reported; general SNHL QoL data apply.

**Suggested HPO terms.**
- HP:0000407 — Sensorineural hearing impairment
- HP:0000408 — Progressive sensorineural hearing impairment
- HP:0008619 — Bilateral sensorineural hearing impairment
- HP:0001730 — Progressive hearing impairment
- HP:0000006 — Autosomal dominant inheritance
- HP:0008527 — Congenital sensorineural hearing impairment (explicitly *excluded*; onset is post-lingual)

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *TRRAP* (Transformation/tRanscription domain-Associated Protein), OMIM *603015; HGNC:12347; NCBI Gene 8295; Ensembl ENSG00000196367; UniProt Q9Y4A5; located at chromosome 7q22.1. The protein is large (~3,830 amino acids) and is the enzymatically inactive (pseudokinase) member of the PIKK family.

**Pathogenic variants.**

| Variant (transcript NM_001244580) | Protein | Type | Context | Source |
|---|---|---|---|---|
| c.511C>T | p.(Arg171Cys) | Missense | Germline, co-segregating in 3-generation family | [PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/) |
| 3 additional novel variants | (various) | Missense (reported) | Germline, sporadic hearing-loss cases | [PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/) |
| Novel pathogenic variant | (reported) | — | Germline ADNSHL | [PMID: 40004049](https://pubmed.ncbi.nlm.nih.gov/40004049/) |

- **Variant classification:** the index variant was reported as pathogenic based on co-segregation, rarity/absence in population databases, and functional support in zebrafish. Per ACMG/AMP, classification would rest on segregation (PP1), rarity (PM2), and functional evidence (PS3-supporting via zebrafish modeling).
- **Variant type/class:** predominantly missense.
- **Allele frequency:** the causal variants are rare/absent in population databases (gnomAD), consistent with a highly disease-relevant, constrained gene.
- **Somatic vs germline:** DFNA75 variants are **germline**. This is mechanistically distinct from *somatic* TRRAP mutations in cancer (see Section 6 and Finding F007).
- **Functional consequence:** for DFNA75, the mechanism is inferred to be a dominant, dosage/scaffold-sensitive effect (haploinsufficiency or dominant-negative disruption of HAT-complex scaffolding); zebrafish *trrap* loss-of-function reproduces inner-ear defects, supporting reduced TRRAP function as pathogenic ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)).

**Constraint.** TRRAP is "evolutionarily conserved and is among the top five genes intolerant to missense variation" ([PMID: 30827496](https://pubmed.ncbi.nlm.nih.gov/30827496/)), underscoring that even single missense changes can be pathogenic.

**Modifier genes / epigenetic information / chromosomal abnormalities.** No DFNA75-specific modifier genes, epigenetic marks, or chromosomal abnormalities have been reported (knowledge gap). Notably TRRAP itself is an epigenetic regulator (a HAT-complex scaffold), so the *downstream* consequence of TRRAP dysfunction is dysregulated histone acetylation.

**Suggested ontology terms:** MONDO (autosomal dominant nonsyndromic hearing loss 75); HGNC:12347 (TRRAP).

---

## Section 5 — Environmental Information

DFNA75 is a purely genetic Mendelian condition. **No environmental factors, lifestyle factors, or infectious agents are established as causal or triggering.** As with all sensorineural hearing loss, generic ototoxic exposures (aminoglycoside/platinum chemotherapy, loud noise, aging) may additively worsen hearing but are not part of the disease's causal etiology. This is a **not-applicable / knowledge-gap** section for this disorder.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. A heterozygous germline missense variant in *TRRAP* (e.g., c.511C>T, p.Arg171Cys) **leads to** an altered TRRAP protein in a gene extraordinarily intolerant to missense change.
2. Altered/reduced TRRAP function **results in** impaired scaffolding of histone-acetyltransferase (HAT) complexes (STAGA/SAGA–GCN5; TIP60/NuA4) and of transcription-factor partners (Sp1, c-Myc, p53, E2F1). *(Inferred from TRRAP's known molecular role; not yet directly demonstrated for the DFNA75 alleles.)*
3. Disrupted HAT recruitment **leads to** aberrant histone acetylation and dysregulated transcription of TRRAP/HAT-dependent gene programs governing cell proliferation and differentiation.
4. In the developing inner ear, this transcriptional dysregulation **results in** defective proliferation/differentiation of inner-ear cell populations — demonstrated as significant inner-ear developmental defects in zebrafish *trrap* knockdown/knockout. *(Demonstrated in model organism.)*
5. Impaired cochlear development/maintenance **leads to** progressive cochlear (sensorineural) dysfunction.
6. Cochlear sensorineural dysfunction **manifests** as bilateral, post-lingual, progressive hearing loss (DFNA75).

**Branch (allelic, not DFNA75):** Different TRRAP missense alleles (e.g., clustering near residues 1031–1159) instead disrupt neurodevelopmental transcriptional programs → developmental delay, dysmorphic facies, autism/ID (DEDDFA). A separate *somatic* branch (p.Ser722Phe in melanocytes) drives oncogenesis.

### Molecular detail

**Molecular function / pathways.** "TRRAP, as the only member lacking the enzymatic activity in this [PIKK] family, is an adaptor protein for several histone acetyltransferase (HAT) complexes and a scaffold protein for multiple transcription factors" ([PMID: 34830324](https://pubmed.ncbi.nlm.nih.gov/34830324/)). It bridges transcription factors to chromatin-modifying enzymes: MYC contacts the human STAGA coactivator via multivalent interactions with the GCN5 and TRRAP subunits — "we identify both TRRAP and the GCN5 acetyltransferase as MYC TAD-interacting subunits within native STAGA" ([PMID: 24705139](https://pubmed.ncbi.nlm.nih.gov/24705139/)). TRRAP also participates in the TIP60/NuA4 complex (e.g., Elk-1–recruited TIP60/NuA4 activating prolactin transcription; [PMID: 24075908](https://pubmed.ncbi.nlm.nih.gov/24075908/)).

**Cellular processes.** TRRAP is fundamentally required for cell proliferation. Targeted deletion of *Trrap* causes early embryonic lethality, and tissue-specific ablation in B cells impairs development and drives proliferating cells into apoptosis: "cells induced to proliferate undergo apoptosis. Our findings demonstrate a central and general role of TRRAP in cell proliferation" ([PMID: 24675885](https://pubmed.ncbi.nlm.nih.gov/24675885/)). In neural stem cells, TRRAP acts as a scaffold controlling Sp1 stability/acetylation to regulate microtubule dynamics and adult hippocampal neurogenesis ([PMID: 36618986](https://pubmed.ncbi.nlm.nih.gov/36618986/), [PMID: 34830324](https://pubmed.ncbi.nlm.nih.gov/34830324/)).

**Protein dysfunction.** TRRAP is a giant scaffold pseudokinase; pathogenic missense changes are inferred to perturb protein–protein interfaces required for HAT-complex/transcription-factor assembly (loss of scaffold competence), rather than an enzymatic active site (TRRAP has none).

**Suggested GO/CL terms.**
- GO:0016573 — histone acetylation
- GO:0000123 — histone acetyltransferase complex
- GO:0006357 — regulation of transcription by RNA polymerase II
- GO:0008283 — cell population proliferation
- GO:0060113 — inner ear receptor cell differentiation (developing ear)
- CL:0000855 — sensory hair cell; CL:0002218 — inner ear hair cell (candidate affected cell types, inferred)

---

## Section 7 — Anatomical Structures Affected

**Organ level.** Primary affected organ: the **inner ear / cochlea** (UBERON:0001846 internal ear; UBERON:0001844 cochlea). Body system: **auditory / special sense (nervous) system**. DFNA75 is nonsyndromic — there is no established secondary organ involvement.

**Tissue and cell level.** Nonsyndromic hearing impairment is "almost exclusively caused by cochlear defects" ([PMID: 15850684](https://pubmed.ncbi.nlm.nih.gov/15850684/)); the affected tissue is the cochlear sensory epithelium (organ of Corti). Candidate targeted cells include cochlear sensory hair cells (inner/outer) and supporting cells; zebrafish inner-ear developmental defects indicate broader inner-ear cell populations are TRRAP-dependent ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)). Precise human cell-type localization within the DFNA75 cochlea has not been directly established (inferred).

**Subcellular level.** As a transcriptional/chromatin scaffold, TRRAP localizes to the **nucleus** (GO:0005634); its functional site is nuclear chromatin and HAT complexes (GO:0000123 histone acetyltransferase complex).

**Localization / lateralization.** Bilateral cochlear involvement. UBERON:0001846 (internal ear), UBERON:0001844 (cochlea), UBERON:0002227 (organ of Corti).

---

## Section 8 — Temporal Development

**Onset.** Post-lingual (after normal speech acquisition); typically childhood-to-adult onset, insidious. Not congenital in the index family.

**Progression.** Progressive — hearing worsens over time. The index family is explicitly "post-lingual progressive" ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)). Progression rate and precise audiometric trajectory across the frequency range have not been quantified in detail (knowledge gap); course is chronic and lifelong.

**Patterns.** No spontaneous remission; hearing loss does not recover without intervention. The critical window for intervention is functional (amplification/implantation once thresholds warrant), rather than a developmental critical period, given post-lingual onset.

---

## Section 9 — Inheritance and Population

**Inheritance.** Autosomal dominant (the "A" in DFNA75). Postlingual nonsyndromic hearing impairment "usually follows an autosomal dominant trait" ([PMID: 15850684](https://pubmed.ncbi.nlm.nih.gov/15850684/)), consistent with DFNA75. Segregation was demonstrated across three generations ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)).

**Penetrance / expressivity.** Co-segregation across three generations is consistent with high penetrance in the index family; formal penetrance and expressivity estimates are not established given the small number of reported families (knowledge gap). Genetic anticipation, germline mosaicism, founder effects, consanguinity, and carrier frequency are not applicable/undocumented for this dominant, rare disorder.

**Epidemiology.** DFNA75 is very rare; precise prevalence/incidence are unknown. It is one of >40 genes underlying autosomal dominant nonsyndromic hearing loss. Genetic heterogeneity is substantial: "One percent of the total human genes, i.e. 300-500, are estimated to cause syndromic and nonsyndromic HIH" ([PMID: 15850684](https://pubmed.ncbi.nlm.nih.gov/15850684/)).

**Population demographics.** Reported cases include a Chinese family and sporadic cases ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)) and a further ADNSHL report ([PMID: 40004049](https://pubmed.ncbi.nlm.nih.gov/40004049/)). No ethnic predisposition, geographic clustering, or sex bias has been established (autosomal, so no expected sex skew).

---

## Section 10 — Diagnostics

**Genetic testing is the definitive diagnostic modality.** In the index family and sporadic cases, diagnosis was achieved by **whole-exome sequencing with Sanger confirmation of co-segregation**: "Whole-exome sequencing, bioinformatic analysis, and Sanger sequencing were used to verify the co-segregation of a novel pathogenic variant" ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)).

**Recommended approach.** Because ADNSHL is highly genetically heterogeneous (>40 genes; hundreds of hearing-loss genes overall — [PMID: 15850684](https://pubmed.ncbi.nlm.nih.gov/15850684/)), the practical diagnostic strategy is a **comprehensive hearing-loss gene panel or whole-exome sequencing**, not single-gene TRRAP testing. WGS/WES are useful when panels are negative. Chromosomal microarray, karyotyping, FISH, mtDNA testing, and repeat-expansion testing are not indicated for this SNP/indel-level dominant disorder.

**Clinical tests.**
- **Audiometry** (pure-tone air and bone conduction) documents the bilateral, sensorineural, progressive pattern; speech audiometry and, in children, otoacoustic emissions/auditory brainstem response characterize cochlear function.
- No specific blood/urine biomarker exists; the genetic variant is the diagnostic biomarker.
- Imaging (temporal bone CT/MRI) is used to exclude structural/syndromic causes and for cochlear-implant planning, not for positive DFNA75 diagnosis.

**Differential diagnosis.** Other DFNA-series dominant nonsyndromic hearing losses, and acquired progressive SNHL (noise-induced, ototoxic, presbycusis). Distinguishing features: family history/segregation and gene panel result. Syndromic causes are excluded by the absence of extra-auditory features.

**Screening.** Cascade genetic testing of at-risk relatives once the familial variant is identified; no population newborn-screening program targets DFNA75 specifically (though universal newborn hearing screening detects hearing loss non-specifically).

---

## Section 11 — Outcome / Prognosis

**Survival/mortality.** DFNA75 is **not life-threatening**; it does not affect survival or life expectancy. There is no disease-specific mortality.

**Morbidity/function.** The principal burden is communication disability from progressive bilateral SNHL, with attendant effects on education, employment, and social/psychological well-being, and tinnitus in a subset. Formal disability/QoL metrics specific to DFNA75 are not reported.

**Disease course.** Chronic, lifelong, progressive. Without intervention, hearing declines; there is no spontaneous recovery. With appropriate amplification or cochlear implantation, functional hearing and speech understanding can be substantially restored, particularly given post-lingual onset (preserved language).

**Prognostic factors.** Degree and rate of threshold progression determine timing of hearing-aid versus cochlear-implant candidacy. Post-lingual onset is generally favorable for auditory rehabilitation outcomes. No molecular prognostic biomarker beyond the genotype is established.

---

## Section 12 — Treatment

**No disease-specific or curative therapy exists** for TRRAP-related hearing loss. Management follows the standard progressive-SNHL pathway.

| Modality | Indication | NCIT concept |
|---|---|---|
| Hearing aids / amplification | Mild-to-moderate loss | Hearing Aid (NCIT:C50072) |
| Cochlear implantation | Severe-to-profound loss | Cochlear Implant / Cochlear Implantation |
| Aural rehabilitation, speech therapy, assistive listening | Adjunctive across severities | Rehabilitation Therapy |
| Genetic counseling | All affected/at-risk individuals | Genetic Counseling (NCIT:C15709) |

**Cochlear implantation** is "an established surgical intervention for patients with severe to profound sensorineural hearing loss" ([PMID: 41306947](https://pubmed.ncbi.nlm.nih.gov/41306947/)), with favorable long-term outcomes: large series report overall complication rates ~10.7% (≈6% minor, ≈4.7% major), and "The ten-year overall revision surgery necessity of CI received patients was found to be 5.9%" ([PMID: 41699244](https://pubmed.ncbi.nlm.nih.gov/41699244/)). Bilateral simultaneous implantation reduces cumulative anesthesia/surgical exposure relative to sequential implantation without increasing complications ([PMID: 41699244](https://pubmed.ncbi.nlm.nih.gov/41699244/)). Emerging totally implantable cochlear-implant systems show feasibility with significant speech-perception gains ([PMID: 41243136](https://pubmed.ncbi.nlm.nih.gov/41243136/)), and cochlear stimulation can additionally mitigate tinnitus in some patients ([PMID: 41194213](https://pubmed.ncbi.nlm.nih.gov/41194213/)).

**Pharmacotherapy, gene/cell/RNA therapy, immunotherapy, pharmacogenomics:** none established or approved for DFNA75. Gene-directed therapies for inner-ear disorders remain investigational and none targets TRRAP.

---

## Section 13 — Prevention

- **Primary prevention:** Not applicable for a Mendelian dominant disorder — the disease cannot be prevented at the individual genetic level. Generic cochlear-protective measures (avoiding excessive noise and ototoxic drugs) may limit additive hearing loss.
- **Secondary prevention:** Early detection via newborn/pediatric hearing screening and audiometric surveillance in at-risk families enables timely amplification/implantation to preserve communication function.
- **Tertiary prevention:** Aural rehabilitation and cochlear implantation prevent the functional/communication complications of advanced hearing loss.
- **Genetic counseling and reproductive options:** Autosomal dominant inheritance implies a 50% transmission risk to offspring of an affected individual. Once the familial TRRAP variant is known, cascade testing, prenatal diagnosis, and preimplantation genetic testing are options for family planning.
- **Immunization / public-health / environmental interventions:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs:** TRRAP is evolutionarily conserved. Mouse *Trrap* and zebrafish *trrap* are functional orthologs used in disease modeling.
- **Natural disease in other species:** No naturally occurring TRRAP-related hearing-loss disease has been documented in companion animals or wildlife (knowledge gap; no OMIA entry reported for this phenotype).
- **Comparative biology / conservation:** Deep conservation of TRRAP and its HAT-scaffold function supports cross-species mechanistic modeling. Zebrafish *trrap* mutants recapitulate developmental phenotypes including inner-ear defects ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)) and craniofacial anomalies — "The trrap zebrafish mutants exhibited smaller eyes and heads than the wild-type zebrafish. The size of the ventral pharyngeal arches was reduced and the mineralization of teeth was impaired" ([PMID: 34934055](https://pubmed.ncbi.nlm.nih.gov/34934055/)).
- **Transmission / zoonosis:** Not applicable (genetic, non-transmissible).

---

## Section 15 — Model Organisms

| Model | Type | Key finding | Source |
|---|---|---|---|
| Zebrafish (*Danio rerio*) | Morpholino knockdown & CRISPR/Cas9 knockout of *trrap* | Significant inner-ear developmental defects — validates DFNA75 causation | [PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/) |
| Zebrafish | *trrap* mutant | Smaller eyes/heads; reduced pharyngeal arches; impaired tooth mineralization (craniofacial roles) | [PMID: 34934055](https://pubmed.ncbi.nlm.nih.gov/34934055/) |
| Mouse (*Mus musculus*) | Germline *Trrap* knockout | Early embryonic lethality; reveals essential role in proliferation | [PMID: 24675885](https://pubmed.ncbi.nlm.nih.gov/24675885/) |
| Mouse | B-cell conditional *Trrap* knockout | Impaired B-cell development; proliferating cells undergo apoptosis | [PMID: 24675885](https://pubmed.ncbi.nlm.nih.gov/24675885/) |
| Mouse | Neural conditional *Trrap* deletion | Compromised adult hippocampal neurogenesis via Sp1 scaffolding | [PMID: 36618986](https://pubmed.ncbi.nlm.nih.gov/36618986/) |

**Phenotype recapitulation.** The zebrafish *trrap* loss-of-function model directly recapitulates the disease-relevant phenotype (inner-ear developmental defects), providing the strongest functional support for DFNA75 causation. **Limitations:** the zebrafish inner ear differs anatomically from the mammalian cochlea; embryonic lethality of the mouse null precludes simple whole-animal study of adult hearing; and no dedicated *Trrap* p.Arg171Cys knock-in hearing-loss mouse has been reported — a clear gap for modeling the specific human allele. **Resources:** MGI (mouse), ZFIN (zebrafish), IMPC/KOMP.

---

## Key Findings (Expanded)

### F001 — DFNA75 is caused by heterozygous TRRAP variants
Xia et al. (2019) identified the novel pathogenic variant **NM_001244580 c.511C>T, p.(Arg171Cys)** in *TRRAP* co-segregating with post-lingual progressive ADNSHL across a three-generation Chinese family, and found three additional novel TRRAP variants among 66 sporadic hearing-loss cases. The authors reported "a novel pathogenic variant (NM_ 001244580, c.511C>T, p.Arg171Cys) in the TRansformation/tRanscription domain-Associated Protein gene associated with hearing loss in a three-generation Chinese family with ADNSHL," and that "Knockdown or knockout of TRRAP resulted in significant defects in the inner ear of zebrafish, indicating that TRRAP plays an important role in inner ear development" ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)). DFNA75 corresponds to OMIM #618778.

### F002 — TRRAP is a highly constrained PIKK scaffold with an allelic neurodevelopmental disorder (DEDDFA)
Distinct germline TRRAP missense alleles cause **DEDDFA** (OMIM #618454). Cogné et al. reported 17 distinct de novo/apparently de novo variants in 24 individuals, noting "TRRAP is evolutionarily conserved and is among the top five genes intolerant to missense variation. Through an international collaboration, 17 distinct de novo or apparently de novo variants were identified in TRRAP in 24 individuals" ([PMID: 30827496](https://pubmed.ncbi.nlm.nih.gov/30827496/)). Domain-specific genotype–phenotype correlation is emerging: variants clustering between residues 1031–1159 "result in more pronounced facial anomalies associated with a variable degree of intellectual disability" ([PMID: 41952423](https://pubmed.ncbi.nlm.nih.gov/41952423/)). This allelic relationship is critical for interpretation: TRRAP variant location and type dictate whether the outcome is isolated hearing loss (DFNA75) or a multisystem neurodevelopmental syndrome.

### F003 — TRRAP mechanism: HAT-complex adaptor and transcription-factor scaffold
TRRAP is "the only member lacking the enzymatic activity in this family, [and] is an adaptor protein for several histone acetyltransferase (HAT) complexes and a scaffold protein for multiple transcription factors" ([PMID: 34830324](https://pubmed.ncbi.nlm.nih.gov/34830324/)). It is a subunit of STAGA/SAGA (with GCN5) and TIP60/NuA4, and coactivates MYC via multivalent contacts — "we identify both TRRAP and the GCN5 acetyltransferase as MYC TAD-interacting subunits within native STAGA" ([PMID: 24705139](https://pubmed.ncbi.nlm.nih.gov/24705139/)). It scaffolds Sp1 to regulate microtubule dynamics and adult neurogenesis ([PMID: 36618986](https://pubmed.ncbi.nlm.nih.gov/36618986/)), and is essential for proliferation (embryonic lethality on knockout; apoptosis of proliferating B cells, [PMID: 24675885](https://pubmed.ncbi.nlm.nih.gov/24675885/)). Zebrafish *trrap* mutants show reduced eyes/heads and pharyngeal-arch/tooth defects ([PMID: 34934055](https://pubmed.ncbi.nlm.nih.gov/34934055/)).

### F004 — DFNA75 phenotype: post-lingual, progressive, bilateral SNHL
The index family had post-lingual progressive ADNSHL; the aim was stated as "to identify the causative gene mutation for post-lingual progressive ADNSHL in a Chinese family" ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)). Nonsyndromic hearing impairment "is almost exclusively caused by cochlear defects, [so] affected patients suffer from sensorineural hearing loss," and "Postlingual nonsyndromic HIH usually follows an autosomal dominant trait" ([PMID: 15850684](https://pubmed.ncbi.nlm.nih.gov/15850684/)).

### F005 — Management is supportive: amplification and cochlear implantation
No curative therapy exists. Cochlear implantation is "an established surgical intervention for patients with severe to profound sensorineural hearing loss" ([PMID: 41306947](https://pubmed.ncbi.nlm.nih.gov/41306947/)), with a 10-year revision surgery necessity of 5.9% ([PMID: 41699244](https://pubmed.ncbi.nlm.nih.gov/41699244/)).

### F006 — Diagnosis relies on WES/gene-panel testing of TRRAP (HGNC:12347, 7q22.1)
Diagnosis in the original family used "Whole-exome sequencing, bioinformatic analysis, and Sanger sequencing... to verify the co-segregation of a novel pathogenic variant" ([PMID: 31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/)). Substantial genetic heterogeneity — "One percent of the total human genes, i.e. 300-500, are estimated to cause syndromic and nonsyndromic HIH" ([PMID: 15850684](https://pubmed.ncbi.nlm.nih.gov/15850684/)) — justifies panel/WES over single-gene testing.

### F007 — TRRAP has a distinct somatic oncogenic role, separate from germline DFNA75
Whole-exome sequencing of melanoma found that "TRRAP harbored a recurrent mutation that clustered in one position (p. Ser722Phe) in 6 out of 167 affected individuals (∼4%)," and "The nature, pattern and functional evaluation of the TRRAP recurrent mutation suggest that TRRAP functions as an oncogene" ([PMID: 21499247](https://pubmed.ncbi.nlm.nih.gov/21499247/)). This somatic, cancer-specific event is mechanistically and clinically distinct from the germline heterozygous variants that cause DFNA75.

---

## Mechanistic Model / Interpretation

```
 Germline TRRAP missense variant (e.g., c.511C>T, p.Arg171Cys)
 [gene among top-5 most missense-intolerant]
              │
              ▼
 Altered TRRAP scaffold protein (PIKK pseudokinase, ~3830 aa, nuclear)
              │  impaired assembly of HAT complexes & TF partners
              ▼
 Disrupted STAGA/SAGA(GCN5) & TIP60/NuA4 recruitment;
 altered Sp1 / c-Myc / p53 / E2F1 coactivation
              │  aberrant histone acetylation → dysregulated transcription
              ▼
 Impaired proliferation/differentiation of inner-ear cells
 (demonstrated: zebrafish trrap KD/KO → inner-ear defects)
              │
              ▼
 Progressive cochlear (sensorineural) dysfunction ── bilateral ──► DFNA75
                                                                    (post-lingual,
                                                                     progressive SNHL)

 ── ALLELIC BRANCHES (same gene, different variant/context) ──
   • Other germline missense (e.g., res. 1031–1159) → DEDDFA neurodevelopmental syndrome
   • Somatic p.Ser722Phe in melanocytes → oncogenic driver in melanoma
```

The unifying theme is that TRRAP is a **dosage- and interface-sensitive transcriptional scaffold**: the *identity and location* of the variant, together with germline-versus-somatic context, determines the clinical phenotype. DFNA75 represents the tissue-restricted (cochlear) consequence of specific germline TRRAP alleles that impair inner-ear developmental transcription while sparing broader neurodevelopment.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [31231791](https://pubmed.ncbi.nlm.nih.gov/31231791/) | *Novel TRRAP mutation causes autosomal dominant non-syndromic hearing loss* | **Defining paper** — causal variant, phenotype, zebrafish validation |
| [40004049](https://pubmed.ncbi.nlm.nih.gov/40004049/) | *Novel pathogenic variant of TRRAP (ADNSHL)* | Independent replication of TRRAP as an ADNSHL gene |
| [30827496](https://pubmed.ncbi.nlm.nih.gov/30827496/) | *Missense variants in TRRAP cause autism and syndromic ID* | Allelic DEDDFA disorder; extreme missense constraint |
| [41952423](https://pubmed.ncbi.nlm.nih.gov/41952423/) | *Variants in cluster 1031–1159 of TRRAP* | Domain-specific genotype–phenotype correlation |
| [34830324](https://pubmed.ncbi.nlm.nih.gov/34830324/) | *Beyond HAT Adaptor: TRRAP–Sp1 transcription* | TRRAP molecular function (HAT adaptor/scaffold) |
| [24705139](https://pubmed.ncbi.nlm.nih.gov/24705139/) | *MYC interacts with STAGA via GCN5 & TRRAP* | TRRAP in STAGA complex; MYC coactivation |
| [36618986](https://pubmed.ncbi.nlm.nih.gov/36618986/) | *TRRAP-mediated acetylation on Sp1 regulates neurogenesis* | Scaffold role in adult neurogenesis |
| [24675885](https://pubmed.ncbi.nlm.nih.gov/24675885/) | *Tissue-specific inactivation of TRRAP in B cells* | Essential proliferation role; embryonic lethality |
| [24075908](https://pubmed.ncbi.nlm.nih.gov/24075908/) | *Elk-1 recruits TIP60/NuA4* | TRRAP-associated TIP60/NuA4 complex biology |
| [34934055](https://pubmed.ncbi.nlm.nih.gov/34934055/) | *Zebrafish trrap in craniofacial development* | Model-organism developmental roles |
| [15850684](https://pubmed.ncbi.nlm.nih.gov/15850684/) | *Nuclear/mitochondrial genes in nonsyndromic hearing* | Context: cochlear/sensorineural nature, AD trait, heterogeneity |
| [41306947](https://pubmed.ncbi.nlm.nih.gov/41306947/) | *Complications in cochlear implant surgery* | CI as standard management of severe-profound SNHL |
| [41699244](https://pubmed.ncbi.nlm.nih.gov/41699244/) | *CI complications & bilateral vs sequential outcomes* | CI outcome/revision data |
| [41243136](https://pubmed.ncbi.nlm.nih.gov/41243136/) | *Totally implantable cochlear implant feasibility* | Emerging CI technology |
| [41194213](https://pubmed.ncbi.nlm.nih.gov/41194213/) | *EMLR and CI effects in tinnitus* | CI benefit for associated tinnitus |
| [21499247](https://pubmed.ncbi.nlm.nih.gov/21499247/) | *Exome sequencing identifies GRIN2A/TRRAP in melanoma* | Distinct somatic oncogenic TRRAP role |

**Evidence quality note.** The germline DFNA75 causal evidence rests primarily on a **single index family plus sporadic cases** with functional support from a zebrafish loss-of-function model (human clinical + model organism). Mechanistic inferences about HAT-scaffold disruption in the cochlea are extrapolated from TRRAP's general biology (in vitro / other-tissue models), not directly demonstrated for DFNA75 alleles in cochlear tissue.

---

## Limitations and Knowledge Gaps

- **Small evidence base:** DFNA75 is defined by one detailed family plus limited sporadic/additional cases. Penetrance, expressivity, audiometric progression curves, and prevalence are not quantified.
- **Allele-specific mechanism unproven in ear:** The exact functional consequence (haploinsufficiency vs dominant-negative) of p.Arg171Cys and other DFNA75 alleles has not been demonstrated in cochlear cells; a knock-in mammalian hearing model is lacking.
- **Genotype–phenotype boundary:** Why some TRRAP variants yield isolated hearing loss (DFNA75) versus multisystem DEDDFA is not fully resolved; domain/interface mapping is incomplete.
- **No modifiers, epigenetic, or environmental data** specific to DFNA75.
- **No disease-specific QoL, natural-history, or veterinary data.**
- **No targeted therapy;** all management is generic SNHL supportive care.

---

## Proposed Follow-up Experiments / Actions

1. **Case ascertainment and registry:** Aggregate additional TRRAP-variant hearing-loss families (e.g., via GeneMatcher/hearing-loss consortia) to quantify penetrance, expressivity, and audiometric progression, and to map DFNA75-specific vs DEDDFA-specific variant domains.
2. **Allele-specific functional assays:** Introduce p.Arg171Cys and other DFNA75 alleles into cochlear-relevant cell/organoid systems (inner-ear organoids, iPSC-derived otic cells) and assess TRRAP scaffold integrity, HAT-complex assembly, and target-gene acetylation/expression.
3. **Knock-in mouse model:** Generate a *Trrap* p.Arg171Cys knock-in (or cochlea-conditional) mouse to test whether it recapitulates progressive SNHL and to localize affected cochlear cell types (hair cells vs supporting cells).
4. **Structure–function mapping:** Use AlphaFold/cryo-EM of TRRAP within STAGA/TIP60 to model how DFNA75 versus DEDDFA missense positions perturb specific protein interfaces.
5. **Cochlear cell-type resolution:** Apply single-cell/spatial transcriptomics of the developing inner ear (mouse/zebrafish) under TRRAP perturbation to define the cell populations and gene programs disrupted.
6. **Standardize diagnostics:** Ensure TRRAP is included on comprehensive ADNSHL gene panels and provide ACMG-based reclassification support for new variants; implement cascade testing and genetic counseling protocols for identified families.
7. **Clinical outcome tracking:** Follow hearing-aid and cochlear-implant outcomes in genetically confirmed DFNA75 patients to establish genotype-informed rehabilitation expectations.

---

*Report compiled from a 5-iteration autonomous investigation: 7 confirmed findings, 20 papers reviewed. Evidence types are indicated throughout (human clinical, model organism, in vitro, computational/inferred).*


## Artifacts

- [OpenScientist final report](Hearing_Loss_Autosomal_Dominant_75-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hearing_Loss_Autosomal_Dominant_75-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 23 |
| Quoted claims found in source | 23 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 4 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:41699244` (7 mentions) - Analysis of cochlear implant complications, outcomes of bilateral simultaneous and sequential implantation, and revision cases: a decade of experience.
  - shared terms: cochlear

Weighed against this report's own most characteristic terms: `trrap`, `hearing`, `dfna75`, `loss`, `cochlear`, `gene`, `variant`, `family`, `sensorineural`, `functional`, `dominant`, `nonsyndromic`, `function`, `genetic`, `autosomal`, `progressive`, `zebrafish`, `phenotype`, `cell`, `adnshl`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 19 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0002218` (1 mention) - the report calls it "inner ear hair cell"; CL calls it **immature dendritic epithelial T cell precursor**
- `NCIT:C50072` (1 mention) - the report calls it "Hearing Aid"; NCIT calls it **Modem Device**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016573` (obsolete histone acetylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016573` (1 mention) - the report calls it "histone acetylation"; GO calls it **obsolete histone acetylation**
- `UBERON:0002227` (1 mention) - the report calls it "organ of Corti"; UBERON calls it **spiral organ of cochlea**, and lists "organ of Corti" among its other names
- `NCIT:C15709` (1 mention) - the report calls it "Genetic Counseling"; NCIT calls it **Genetic Testing**
