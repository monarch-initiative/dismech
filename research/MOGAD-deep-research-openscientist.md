---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-15T19:39:40.664763'
end_time: '2026-05-15T20:25:19.707078'
duration_seconds: 2739.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MOGAD
  mondo_id: ''
  category: Neurological Disorder
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
citation_count: 64
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MOGAD
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **MOGAD** covering all of the
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

# Comprehensive Disease Characterization Report: MOGAD (Myelin Oligodendrocyte Glycoprotein Antibody-Associated Disease)

---

## Summary

**Myelin Oligodendrocyte Glycoprotein Antibody-Associated Disease (MOGAD)** is a rare, antibody-mediated inflammatory demyelinating disorder of the central nervous system (CNS) that is now recognized as a distinct entity from both multiple sclerosis (MS) and aquaporin-4 antibody-positive neuromyelitis optica spectrum disorder (AQP4+ NMOSD). MOGAD is defined by the presence of serum IgG autoantibodies targeting myelin oligodendrocyte glycoprotein (MOG) — a protein exclusively expressed on the outermost surface of CNS myelin sheaths and oligodendrocyte membranes. International consensus diagnostic criteria were published in 2023 ([PMID: 36706773](https://pubmed.ncbi.nlm.nih.gov/36706773/)), formally establishing MOGAD as a unique disease entity with specific clinical, radiological, pathological, and immunological characteristics.

Epidemiologically, MOGAD has an estimated incidence of approximately 0.2 per 100,000 person-years and a prevalence of 1.5–3.9 per 100,000, with a near-equal sex ratio — in contrast to the strong female predominance in MS and AQP4+ NMOSD. The disease affects both children and adults, with age-dependent clinical phenotypes: acute disseminated encephalomyelitis (ADEM) predominates in young children, while optic neuritis is the most common presentation in adults. Approximately 50–65% of patients follow a monophasic course, while the remainder develop relapsing disease. Disability accrual is relapse-dependent rather than progressive, with visual impairment being the most common long-term sequela (36% with severe visual impairment or functional blindness).

Pathologically, MOGAD is characterized by perivenous demyelination (present in 92% of brain biopsy lesions), CD4+ T-cell-dominated inflammation with granulocytic infiltration, complement deposition, and preserved astrocytes — features fundamentally different from both MS (confluent demyelination, slowly expanding lesions) and AQP4+ NMOSD (astrocytopathy). Treatment centers on high-dose intravenous corticosteroids for acute attacks, with maintenance intravenous immunoglobulin (IVIG) emerging as the most effective relapse-prevention therapy (annualized relapse rate 0.081, relapse probability 25.3%). No FDA-approved MOGAD-specific therapies exist yet, but multiple randomized clinical trials are underway, and emerging approaches including CAR T-cell therapy hold promise.

---

## 1. Disease Information

### 1.1 Overview

MOGAD is "a rare, antibody-mediated inflammatory demyelinating disorder of the central nervous system (CNS) with various phenotypes starting from optic neuritis, via transverse myelitis to acute demyelinating encephalomyelitis (ADEM) and cortical encephalitis" ([PMID: 33374173](https://pubmed.ncbi.nlm.nih.gov/33374173/)). The disease is defined by the presence of serum MOG-IgG detected by live cell-based assay (CBA), in the context of compatible clinical demyelinating events.

The 2023 international consensus diagnostic criteria established that "Serum antibodies directed against myelin oligodendrocyte glycoprotein (MOG) are found in patients with acquired CNS demyelinating syndromes that are distinct from multiple sclerosis and aquaporin-4-seropositive neuromyelitis optica spectrum disorder" ([PMID: 36706773](https://pubmed.ncbi.nlm.nih.gov/36706773/)).

### 1.2 Key Identifiers

| Identifier | Value |
|---|---|
| **MONDO** | MONDO:0100475 |
| **ICD-11** | 8A45.0 (Myelin oligodendrocyte glycoprotein antibody-associated disease) |
| **ICD-10** | G36.9 (Acute disseminated demyelination, unspecified — no specific MOGAD code in ICD-10) |
| **MeSH** | Not yet assigned; indexed under "Demyelinating Autoimmune Diseases, CNS" |
| **Orphanet** | ORPHA:610159 |
| **OMIM** | Not applicable (acquired autoimmune, not Mendelian) |

### 1.3 Synonyms and Alternative Names

- MOG antibody-associated disease (MOGAD)
- MOG-IgG-associated disorder
- Anti-MOG-associated disease
- MOG antibody disease
- MOG spectrum disorder
- Anti-MOG encephalomyelitis
- MOG-IgG-associated encephalomyelitis

### 1.4 Information Sources

This report is derived from aggregated disease-level resources including systematic reviews, meta-analyses, international multicenter cohort studies, population-based epidemiological studies, brain biopsy/autopsy series, and clinical trial data. A total of 142 papers were reviewed, with 21 confirmed findings supported by direct abstract citations.

---

## 2. Etiology

### 2.1 Disease Causal Factors

MOGAD is an **autoimmune/antibody-mediated** disease. The primary causal mechanism involves IgG1-class autoantibodies targeting MOG on the surface of oligodendrocytes and myelin sheaths, triggering:

1. **Complement-dependent cytotoxicity (CDC)**: C3d and C5b-9 (membrane attack complex) deposition on myelin ([PMID: 32048003](https://pubmed.ncbi.nlm.nih.gov/32048003/))
2. **Antibody-dependent cellular cytotoxicity (ADCC)**: Granulocytic and macrophage-mediated damage
3. **CD4+ T-cell-mediated inflammation**: Dominant inflammatory infiltrate in MOGAD lesions

The upstream trigger for MOG-IgG production remains incompletely understood but is believed to involve a combination of genetic susceptibility and environmental/infectious triggers.

### 2.2 Risk Factors

#### Genetic Risk Factors

MOGAD is not a Mendelian disorder. Unlike MS, where HLA-DRB1*15:01 is a well-established risk allele, MOGAD lacks confirmed genetic susceptibility loci. However:

- **HLA associations**: HLA-DQB1*06:02 and HLA-DRB1*15:01 have been associated with oligoclonal band-positive optic neuritis ([PMID: 29544193](https://pubmed.ncbi.nlm.nih.gov/29544193/)), though these are more typical of MS
- MOG-IgG subclass: Most MOG antibodies are IgG1 subclass; rare cases with isolated MOG-IgG3 have been reported, sometimes in the context of IgG1 deficiency ([PMID: 41406406](https://pubmed.ncbi.nlm.nih.gov/41406406/))
- No GWAS loci have been confirmed for MOGAD specifically

#### Environmental Risk Factors

- **Preceding infections**: MOGAD is frequently preceded by infections. Sanderson et al. demonstrated that "MOG-specific B cells take up large amounts of MOG from cell membranes. When influenza hemagglutinin is also present in the membrane of the target cell, it can be cocaptured with MOG by MOG-specific B cells via the B-cell receptor" ([PMID: 28057865](https://pubmed.ncbi.nlm.nih.gov/28057865/)). This molecular mimicry/bystander activation mechanism provides a plausible link between infection and autoimmunity.
- **Age**: Bimodal age distribution — peak in early childhood (ADEM phenotype) and in young adulthood (optic neuritis phenotype)
- **Sex**: Near-equal sex ratio, distinguishing MOGAD from MS (female predominance 3:1) and AQP4+ NMOSD (female predominance 9:1)
- **Ethnicity/Race**: Hispanic and non-White non-Hispanic adults may have increased risk of relapsing disease compared to non-Hispanic Whites (adjusted RR 1.52, 95% CI: 1.01–2.30) ([PMID: 37979410](https://pubmed.ncbi.nlm.nih.gov/37979410/))
- **COVID-19**: Reports suggest COVID-19 may trigger ADEM-associated optic neuritis presentations ([PMID: 40728559](https://pubmed.ncbi.nlm.nih.gov/40728559/))
- **TNF-alpha inhibitors**: Adalimumab (a TNF-alpha inhibitor) has been reported as a potential immunologic trigger for MOGAD/FLAMES ([PMID: 41406158](https://pubmed.ncbi.nlm.nih.gov/41406158/))

#### Protective Factors

- **Pregnancy**: Appears strongly protective. In a US two-center study, "No relapses were observed during any of the 22 pregnancies... The mean ARR was 0.26 during the 12-month pre-pregnancy period, 0 during pregnancy, and 0.09 in the 12-month postpartum period" ([PMID: 41066906](https://pubmed.ncbi.nlm.nih.gov/41066906/)). However, "Three-quarters of women with previously monophasic disease transitioned to a relapsing course postpartum" ([PMID: 41747756](https://pubmed.ncbi.nlm.nih.gov/41747756/)), indicating postpartum risk.

### 2.3 Gene-Environment Interactions

The cocapture mechanism described by Sanderson et al. ([PMID: 28057865](https://pubmed.ncbi.nlm.nih.gov/28057865/)) represents a gene-environment interaction wherein viral antigens are cocaptured with MOG by MOG-specific B cells, leading to T-cell help from virus-specific T cells and class-switched anti-MOG antibody production. This suggests that common infections may break tolerance in genetically susceptible individuals.

---

## 3. Phenotypes

### 3.1 Core Clinical Phenotypes

MOGAD presents with age-dependent clinical phenotypes:

| Phenotype | Age Group | Frequency | HPO Term |
|---|---|---|---|
| **Optic Neuritis (ON)** | Adults (most common) | 62.3% in adults | HP:0100653 (Optic neuritis) |
| **ADEM** | Young children (most common) | 34.8% in children | HP:0007305 (CNS demyelination) |
| **Transverse Myelitis (TM)** | All ages | 20-30% | HP:0100510 (Transverse myelitis) |
| **Cortical Encephalitis/FLAMES** | Older children/adults | 7.3% in pediatric MOGAD | HP:0001298 (Encephalopathy) |
| **Brainstem Encephalitis** | All ages | Uncommon | HP:0007305 |
| **NMOSD-like (simultaneous ON+TM)** | All ages | Uncommon | HP:0100653 + HP:0100510 |

"Typical MOGAD presentations consist of demyelinating syndromes, including acute disseminated encephalomyelitis (ADEM) in younger, and optic neuritis (ON) and/or transverse myelitis (TM) in older children" ([PMID: 33162302](https://pubmed.ncbi.nlm.nih.gov/33162302/)).

"The most frequent presentations were optic neuritis in adults (62.3%) and ADEM in children (34.8%); 64.5% had a monophasic disease course over a median follow-up of 38 months" ([PMID: 41657079](https://pubmed.ncbi.nlm.nih.gov/41657079/)).

### 3.2 Optic Neuritis

MOGAD optic neuritis is characterized by:
- **Severe acute vision loss** but better recovery than MS-ON: "significantly worse visual acuity at nadir, but better recovery and thinner global peripapillary retinal nerve fiber layer thickness in MOG-ON patients compared to MS-ON patients" ([PMID: 32785840](https://pubmed.ncbi.nlm.nih.gov/32785840/))
- **Attack-dependent retinal damage** without progressive neurodegeneration: "the absence of attack-independent retinal damage in patients with MOGAD. Yet, ongoing neuroaxonal damage or edema resolution seems to occur for up to 12 months after ON" ([PMID: 35703428](https://pubmed.ncbi.nlm.nih.gov/35703428/))
- **Perineural enhancement** on MRI: most common MRI finding (40.3%) ([PMID: 42070455](https://pubmed.ncbi.nlm.nih.gov/42070455/))
- **Bilateral involvement** more common than in MS
- pRNFL thinning rate: 0.35 μm/year (95% CI 0.04–0.66)

### 3.3 Myelitis

MOGAD myelitis features include:
- **H-sign** (gray matter involvement): present in 63% ([PMID: 37060644](https://pubmed.ncbi.nlm.nih.gov/37060644/))
- **Longitudinally extensive transverse myelitis (LETM)**: 63%
- **Leptomeningeal enhancement**: 61% ([PMID: 41252657](https://pubmed.ncbi.nlm.nih.gov/41252657/))
- **Conus medullaris predilection** ([PMID: 35785363](https://pubmed.ncbi.nlm.nih.gov/35785363/))
- Symptoms: weakness (91%), neurogenic bladder (63%), sensory dysfunction (46%)

### 3.4 Cognitive Impairment

Adults with MOGAD show "mild global cognitive impairment, with pooled MoCA scores of 24.69 (95% CI: 23.31–26.07). Processing speed and working memory were consistently affected, with pooled PASAT-3 means of 39.14 (95% CI: 35.68–42.61), PASAT-2 of 30.91 (95% CI: 28.08–33.75), and SDMT of 44.47 (95% CI: 41.73–47.20)" ([PMID: 41831288](https://pubmed.ncbi.nlm.nih.gov/41831288/)). Pediatric cohorts showed relative preservation (FSIQ: 98.93).

**Suggested HPO terms**: HP:0100543 (Cognitive impairment), HP:0031843 (Processing speed impairment)

### 3.5 Patient-Reported Outcomes

Qualitative interviews revealed that "The most common patient-reported symptoms were eye pain, fatigue, body aches/pain, headaches, and blurred vision. Eye pain and body aches/pain were reported as the most bothersome symptoms and most important to improve with treatment" ([PMID: 40506564](https://pubmed.ncbi.nlm.nih.gov/40506564/)). Quality-of-life impacts include difficulty with household chores, inability to work, depression, and difficulty walking.

### 3.6 FLAMES (FLAIR-hyperintense Lesions in Anti-MOG-associated Encephalitis with Seizures)

A distinctive cortical encephalitis phenotype characterized by:
- Unilateral cortical FLAIR hyperintensities (predominantly frontal lobe)
- Seizures (focal seizures predominant)
- Headache and altered mental status
- Good immunotherapy response
- Prevalence: 7.3% of pediatric MOGAD ([PMID: 40740785](https://pubmed.ncbi.nlm.nih.gov/40740785/))

### 3.7 Overlap Syndromes

**MOG-NMDAR overlap syndrome**: A highly relapsing dual-antibody phenotype with 100% relapse rate (mean interval 6.7 months), 80% cortical encephalopathies, CSF pleocytosis in 90% ([PMID: 39780343](https://pubmed.ncbi.nlm.nih.gov/39780343/)).

---

## 4. Genetic/Molecular Information

### 4.1 Target Autoantigen: MOG

MOGAD is **not a genetic/Mendelian disease**. There are no causal gene mutations or pathogenic variants in the classical sense. The disease is driven by autoantibodies against:

- **MOG gene** (HGNC: 7197; NCBI Gene ID: 4340; UniProt: Q16653)
  - Located on chromosome 6p22.1 within the HLA complex
  - Encodes myelin oligodendrocyte glycoprotein, a type I transmembrane protein exclusively expressed on the outermost surface of CNS myelin and oligodendrocyte membranes
  - MOG constitutes ~0.05% of total myelin protein but its extracellular location makes it accessible to circulating antibodies
  - **GO terms**: GO:0043209 (myelin sheath), GO:0007399 (nervous system development), GO:0042552 (myelination)

### 4.2 Autoantibody Characteristics

- **Primary subclass**: IgG1 (most common and pathogenic)
- **Rare subclass**: IgG3 (isolated cases; [PMID: 41406406](https://pubmed.ncbi.nlm.nih.gov/41406406/))
- **Detection**: Live cell-based assay (CBA) is the gold standard; fixed CBA has lower sensitivity
- MOG-IgG titer correlates with disease activity; seroconversion (becoming negative) is associated with monophasic course
- Caution needed with low-positive results ([PMID: 38043365](https://pubmed.ncbi.nlm.nih.gov/38043365/))

### 4.3 Genetic Susceptibility

- **(TAAA)n polymorphism** in the 3' flanking region of the MOG gene: The 226 bp allele has been associated with anti-MOG antibody positivity ([PMID: 12576235](https://pubmed.ncbi.nlm.nih.gov/12576235/))
- **HLA associations**: Not firmly established for MOGAD specifically, unlike MS (HLA-DRB1*15:01)
- No GWAS studies have been performed specifically for MOGAD

### 4.4 Epigenetic Information

Limited data available. No systematic studies of DNA methylation, histone modifications, or chromatin changes specific to MOGAD have been published. This represents a significant knowledge gap.

---

## 5. Environmental Information

### 5.1 Infectious Triggers

MOGAD is "frequently preceded by infections" ([PMID: 39295869](https://pubmed.ncbi.nlm.nih.gov/39295869/)). The molecular mechanism involves:

1. MOG-specific B cells capture MOG from cell membranes
2. If viral antigens (e.g., influenza hemagglutinin) are present in the same membrane, they are cocaptured
3. This leads to T-cell help from virus-specific T cells, driving class-switched anti-MOG antibody production ([PMID: 28057865](https://pubmed.ncbi.nlm.nih.gov/28057865/))

Reported infectious triggers include upper respiratory tract infections (most common), COVID-19 ([PMID: 40728559](https://pubmed.ncbi.nlm.nih.gov/40728559/)), syphilis and HIV ([PMID: 39295869](https://pubmed.ncbi.nlm.nih.gov/39295869/); [PMID: 40766314](https://pubmed.ncbi.nlm.nih.gov/40766314/)).

### 5.2 Iatrogenic Triggers

TNF-alpha inhibitors (adalimumab): Case reports of MOGAD/FLAMES following TNF-alpha inhibitor therapy for psoriasis ([PMID: 41406158](https://pubmed.ncbi.nlm.nih.gov/41406158/)).

### 5.3 Seasonal Patterns

A Latin American cohort analysis found fewer relapses in autumn (N=21, 17%; IRR 0.17, 95% CI 0.11–0.25, p=0.001) and a peak in November, but circular statistics did not confirm a consistent seasonal pattern ([PMID: 41167050](https://pubmed.ncbi.nlm.nih.gov/41167050/)).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal Chain: From Trigger to Clinical Manifestation

```
UPSTREAM TRIGGERS
    │
    ├── Preceding infection (molecular mimicry / bystander activation)
    ├── Genetic susceptibility (HLA? MOG gene polymorphisms?)
    └── Environmental triggers (TNF-alpha inhibitors, vaccines?)
    │
    ▼
IMMUNE ACTIVATION
    │
    ├── B-cell activation → MOG-specific B cells capture MOG + viral antigens
    ├── T-cell help from virus-specific T cells → class-switched anti-MOG IgG1
    └── CD4+ T-cell priming against MOG epitopes
    │
    ▼
AUTOANTIBODY-MEDIATED DAMAGE
    │
    ├── MOG-IgG1 binds MOG on oligodendrocyte/myelin surface
    ├── Complement activation → C3d + C5b-9 (MAC) deposition
    ├── Complement-dependent cytotoxicity (CDC)
    ├── Antibody-dependent cellular cytotoxicity (ADCC)
    └── Granulocyte and macrophage recruitment
    │
    ▼
TISSUE PATHOLOGY
    │
    ├── Perivenous demyelination (92% of lesions) — ADEM-like pattern
    ├── CD4+ T-cell dominated inflammation
    ├── Variable axonal damage (correlates with cerebral atrophy)
    ├── Preserved AQP4 expression (no astrocytopathy)
    └── No slowly expanding "smoldering" lesions (unlike MS)
    │
    ▼
CLINICAL MANIFESTATION
    │
    ├── Optic neuritis (adults) → severe acute vision loss, perineural enhancement
    ├── ADEM (children) → encephalopathy with multifocal white matter lesions
    ├── Transverse myelitis → H-sign, LETM, conus predilection
    ├── Cortical encephalitis/FLAMES → seizures, unilateral cortical FLAIR
    └── Brainstem syndromes → cranial neuropathies
    │
    ▼
DISEASE COURSE
    │
    ├── Monophasic (50-64%) if MOG-IgG becomes negative (seroconversion)
    └── Relapsing (36-50%) if MOG-IgG persists
        Disability is relapse-dependent, NOT progressive
```

### 6.2 Histopathology

The neuropathological hallmark was defined by Höftberger et al.: "MOGAD pathology is dominated by coexistence of both perivenous and confluent white matter demyelination, with an over-representation of intracortical demyelinated lesions compared to typical MS. Radially expanding confluent slowly expanding smoldering lesions in the white matter as seen in MS, are not present. A CD4+ T-cell dominated inflammatory reaction with granulocytic infiltration predominates. Complement deposition is present in all active white matter lesions, but a preferential loss of MOG is not observed. AQP4 is preserved, with absence of dystrophic astrocytes" ([PMID: 32048003](https://pubmed.ncbi.nlm.nih.gov/32048003/)).

Systematic brain biopsy analysis confirmed: "Most demyelinating lesions in 10 of 11 cases showed a perivenous demyelinating pattern previously reported in ADEM (153/167 lesions) and a fusion pattern (11/167 lesions)" ([PMID: 32412053](https://pubmed.ncbi.nlm.nih.gov/32412053/)). Variable axonal damage was observed, correlating with cerebral atrophy ([PMID: 39267735](https://pubmed.ncbi.nlm.nih.gov/39267735/)).

### 6.3 Comparative Pathology

| Feature | MOGAD | MS | AQP4+ NMOSD |
|---|---|---|---|
| Demyelination pattern | Perivenous + confluent | Confluent with smoldering expansion | Perivenular |
| Cortical demyelination | Prominent intracortical | Subpial | Rare |
| Dominant inflammatory cells | CD4+ T cells, granulocytes | CD8+ T cells | Eosinophils, neutrophils |
| Complement deposition | Present, all active lesions | Variable | Prominent, perivascular |
| AQP4 expression | Preserved | Preserved | Lost (astrocytopathy) |
| Smoldering lesions | Absent | Present | Absent |

### 6.4 Molecular Pathways and Cell Types

| Pathway | Role in MOGAD | GO Term |
|---|---|---|
| **Complement cascade** | CDC via classical pathway (C1q → C3d → C5b-9 MAC) | GO:0006958 |
| **Fc receptor signaling** | ADCC via FcγR on granulocytes/macrophages | GO:0038094 |
| **CD4+ T-cell activation** | Dominant T-cell subset in lesions | GO:0042110 |
| **B-cell receptor signaling** | Antigen capture and presentation by MOG-specific B cells | GO:0050853 |

| Cell Type | Role | CL Term |
|---|---|---|
| **Oligodendrocytes** | Primary target (MOG expression) | CL:0000128 |
| **CD4+ T cells** | Dominant inflammatory infiltrate | CL:0000624 |
| **Granulocytes/Neutrophils** | Effector cells in acute lesions | CL:0000094 |
| **MOG-specific B cells** | Antibody production, antigen presentation | CL:0000236 |
| **Macrophages** | Phagocytosis of damaged myelin | CL:0000235 |

### 6.5 Biomarker Profiling

- **sNfL**: Elevated during attacks (median 16.0 pg/mL in MOGAD-ON vs 6.5 in controls, p<0.001); nonlinearly associated with time from attack onset ([PMID: 39705633](https://pubmed.ncbi.nlm.nih.gov/39705633/); [PMID: 41032997](https://pubmed.ncbi.nlm.nih.gov/41032997/))
- **sGFAP**: Less specific for MOGAD than for AQP4+ NMOSD ([PMID: 33933106](https://pubmed.ncbi.nlm.nih.gov/33933106/))
- **TNF-alpha and alphaB-crystallin**: Upregulated during antibody-mediated demyelination, potentially protective ([PMID: 15478179](https://pubmed.ncbi.nlm.nih.gov/15478179/))

---

## 7. Anatomical Structures Affected

### 7.1 Organ and System Level

| Structure | Involvement | UBERON Term |
|---|---|---|
| **Optic nerve** | Primary (most common in adults) | UBERON:0000941 |
| **Spinal cord** | Primary (myelitis, conus predilection) | UBERON:0002240 |
| **Brain white matter** | Primary (perivenous demyelination) | UBERON:0002316 |
| **Cerebral cortex** | Primary (cortical encephalitis/FLAMES) | UBERON:0000956 |
| **Brainstem** | Secondary (brainstem syndromes) | UBERON:0002298 |
| **Conus medullaris** | Characteristic predilection site | UBERON:0003833 |
| **Retina** | Secondary (attack-dependent RNFL/GCIPL thinning) | UBERON:0000966 |

### 7.2 Tissue and Cell Level

- **Myelin sheaths**: Primary target of MOG-IgG-mediated demyelination
- **Oligodendrocytes** (CL:0000128): MOG-expressing cells; variable destruction
- **Neurons**: Generally preserved acutely; variable axonal damage
- **Astrocytes**: Preserved (AQP4 expression maintained — key distinction from AQP4+ NMOSD)

### 7.3 Lateralization

- Optic neuritis: Can be unilateral or bilateral (bilateral more common than in MS)
- FLAMES: Characteristically unilateral cortical involvement
- Myelitis: Central cord involvement (H-sign on axial MRI)

---

## 8. Temporal Development

### 8.1 Onset

- **Typical age of onset**: Bimodal — childhood peak (median ~5–9 years for ADEM) and adult peak (median ~30–40 years for ON)
- **Onset pattern**: Acute to subacute (days to weeks)
- Pediatric MOGAD median onset: 5.7 years for ADEM, 8.9 years for encephalitis ([PMID: 39393046](https://pubmed.ncbi.nlm.nih.gov/39393046/))

### 8.2 Disease Course

| Course Pattern | Frequency | Characteristics |
|---|---|---|
| **Monophasic** | 50–65% | Single attack, no relapses |
| **Relapsing** | 35–50% | Median time to first relapse: 5 months; ARR 0.92 |
| **Progressive** | Very rare | Not a typical feature of MOGAD |

"The disease followed a multiphasic course in 80% (median time-to-first-relapse 5 months; annualized relapse rate 0.92) and resulted in significant disability in 40% (mean follow-up 75 ± 46.5 months)" ([PMID: 27793206](https://pubmed.ncbi.nlm.nih.gov/27793206/)).

### 8.3 MRI Lesion Dynamics

A critical distinguishing feature is T2 lesion resolution: "Resolution of at least one T2-lesion differentiated MOGAD from MS (sensitivity 77–100%, specificity 86–99%; Youden's index=0.90)" ([PMID: 40685157](https://pubmed.ncbi.nlm.nih.gov/40685157/)). MOGAD patients are more likely to have normal MRI at follow-up vs MS (brain: 32% vs 0%, p<0.001; spine: 78% vs 19%, p<0.001).

### 8.4 Critical Periods

- **Early treatment window**: Early treatment of first attack (<5 days) is associated with higher likelihood of MOG-IgG seroconversion and potentially reduced relapse risk ([PMID: 39226035](https://pubmed.ncbi.nlm.nih.gov/39226035/))
- **Postpartum period**: Window of increased relapse vulnerability; three-quarters of previously monophasic women transitioned to relapsing course postpartum ([PMID: 41747756](https://pubmed.ncbi.nlm.nih.gov/41747756/))

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Metric | Value | Source |
|---|---|---|
| **Incidence** | 0.205/100,000 person-years (95% CI: 0.145–0.281) | Denmark nationwide, [PMID: 41865559](https://pubmed.ncbi.nlm.nih.gov/41865559/) |
| **Prevalence (Denmark)** | 1.51/100,000 (95% CI: 1.18–1.91) | [PMID: 41865559](https://pubmed.ncbi.nlm.nih.gov/41865559/) |
| **Prevalence (South Wales)** | 3.85/100,000 (95% CI: 3.03–4.82) | [PMID: 41657079](https://pubmed.ncbi.nlm.nih.gov/41657079/) |
| **Pediatric prevalence** | 6.59/100,000 (95% CI: 4.18–9.89) | [PMID: 41657079](https://pubmed.ncbi.nlm.nih.gov/41657079/) |

MOGAD incidence/prevalence is approximately 3× higher than AQP4+ NMOSD.

### 9.2 Inheritance Pattern

MOGAD is **not inherited** in a Mendelian pattern. It is an acquired autoimmune disease with complex (multifactorial/polygenic) susceptibility.

### 9.3 Population Demographics

- **Sex ratio**: Near-equal (approximately 1:1) — "Sex ratio was almost equal in males and females" ([PMID: 41657079](https://pubmed.ncbi.nlm.nih.gov/41657079/))
- **Geographic/ethnic variation**: Japanese patients have lower ARR (0.4 vs 0.8, p=0.019) and more monophasic course (64% vs 25%, p=0.002) compared to German patients ([PMID: 33219036](https://pubmed.ncbi.nlm.nih.gov/33219036/))
- **Age distribution**: Affects all ages from infancy to late adulthood; peak incidence 18–39 years

---

## 10. Diagnostics

### 10.1 2023 International Diagnostic Criteria

The 2023 MOGAD criteria ([PMID: 36706773](https://pubmed.ncbi.nlm.nih.gov/36706773/)) require:
1. Core clinical demyelinating event (ON, myelitis, ADEM, cerebral cortical encephalitis, brainstem/cerebellar syndrome)
2. Positive serum MOG-IgG by CBA
3. For low-titer positivity: additional supportive clinical and MRI features required

Validation yielded 100% sensitivity and 55.5% specificity in one institutional cohort ([PMID: 38043365](https://pubmed.ncbi.nlm.nih.gov/38043365/)).

### 10.2 CSF Analysis

"Most strikingly, CSF-restricted oligoclonal IgG bands, a hallmark of multiple sclerosis (MS), were absent in almost 90% of samples (N=151), and the MRZ reaction, the most specific laboratory marker of MS known so far, in 100% (N=62)" ([PMID: 32883348](https://pubmed.ncbi.nlm.nih.gov/32883348/)).

| CSF Finding | MOGAD | MS | Significance |
|---|---|---|---|
| Oligoclonal bands | Absent in ~90% | Present in ≥95% | Key discriminator |
| MRZ reaction | Negative in 100% | Positive in ~75% | Most specific MS marker |
| Pleocytosis | Variable (common in myelitis) | Mild | — |
| Albumin quotient | May be elevated | Usually normal | BBB disruption |

### 10.3 Neuroimaging

#### Brain MRI
MOGAD-specific features ([PMID: 40773034](https://pubmed.ncbi.nlm.nih.gov/40773034/)):
- Conus medullaris T2 lesions, "fluffy" lesions, perineural enhancement
- Peri-ependymal 3rd and 4th ventricle T2 lesions
- T2 lesion resolution over time
- Absence of Dawson's fingers, periventricular ovoid lesions
- No paramagnetic rim lesions (PRLs) — supports discrimination from MS ([PMID: 41512208](https://pubmed.ncbi.nlm.nih.gov/41512208/))

MRI brain lesion distribution criteria distinguish RRMS from MOGAD with **95.2% specificity** ([PMID: 27951522](https://pubmed.ncbi.nlm.nih.gov/27951522/)).

#### Spinal MRI
- H-sign (gray matter, 63%), LETM (63%), leptomeningeal enhancement (61%)
- Conus medullaris predilection ([PMID: 37060644](https://pubmed.ncbi.nlm.nih.gov/37060644/); [PMID: 41252657](https://pubmed.ncbi.nlm.nih.gov/41252657/))

### 10.4 Optical Coherence Tomography (OCT)

- Attack-dependent retinal damage without progressive inter-attack neurodegeneration ([PMID: 35703428](https://pubmed.ncbi.nlm.nih.gov/35703428/))
- Acute RNFL thickening followed by steady thinning; structure-function paradox in recovery ([PMID: 38526582](https://pubmed.ncbi.nlm.nih.gov/38526582/))

### 10.5 Serum Biomarkers

| Biomarker | Utility | Evidence |
|---|---|---|
| **sNfL** | Discriminates attacks from remission | [PMID: 39705633](https://pubmed.ncbi.nlm.nih.gov/39705633/) |
| **sGFAP** | Less specific for MOGAD than AQP4+ NMOSD | [PMID: 33933106](https://pubmed.ncbi.nlm.nih.gov/33933106/) |
| **MOG-IgG titer** | Correlates with disease activity | [PMID: 39226035](https://pubmed.ncbi.nlm.nih.gov/39226035/) |

### 10.6 Visual Evoked Potentials (VEP)

"Ancillary investigations such as visual fields, visual evoked potentials and cerebrospinal fluid analysis may be less discriminatory" than MRI and OCT for MOG-ON diagnosis ([PMID: 38783085](https://pubmed.ncbi.nlm.nih.gov/38783085/)).

### 10.7 Differential Diagnosis

| Condition | Key Distinguishing Features |
|---|---|
| **Multiple Sclerosis** | OCBs present (≥95%), Dawson's fingers, periventricular lesions, slowly expanding lesions, no lesion resolution |
| **AQP4+ NMOSD** | AQP4-IgG positive, area postrema lesions, optic chiasm involvement, astrocytopathy |
| **ADEM (MOG-negative)** | Similar presentation in children; MOG-IgG negative |
| **Anti-NMDAR encephalitis** | Overlap syndrome possible (dual positivity in ~10%) |

---

## 11. Outcome / Prognosis

### 11.1 Long-Term Disability

"The disease resulted in significant disability in 40% (mean follow-up 75 ± 46.5 months), with severe visual impairment or functional blindness (36%) and markedly impaired ambulation due to paresis or ataxia (25%) as the most common long-term sequelae" ([PMID: 27793206](https://pubmed.ncbi.nlm.nih.gov/27793206/)).

### 11.2 Geographic/Ethnic Variation

"Japanese patients had a lower annualised relapse rate (0.4 vs 0.8, p=0.019; no relapse, 64% vs 25%, p=0.002) and lower Expanded Disability Status Scale score at the last visit (1.0 vs 2.0)" compared to German patients ([PMID: 33219036](https://pubmed.ncbi.nlm.nih.gov/33219036/)).

### 11.3 Prognostic Factors

| Factor | Association | Evidence |
|---|---|---|
| MOG-IgG seroconversion | Favorable (monophasic course) | [PMID: 39226035](https://pubmed.ncbi.nlm.nih.gov/39226035/) |
| Persistent MOG-IgG | Relapsing course | Multiple studies |
| Early treatment (<5 days) | Higher seroconversion rate | [PMID: 39226035](https://pubmed.ncbi.nlm.nih.gov/39226035/) |
| Ethnicity (Japanese vs European) | Lower ARR in Japanese | [PMID: 33219036](https://pubmed.ncbi.nlm.nih.gov/33219036/) |
| Hispanic/non-White ethnicity | Higher relapse risk (adults) | [PMID: 37979410](https://pubmed.ncbi.nlm.nih.gov/37979410/) |

### 11.4 Survival

MOGAD is generally not fatal. Life expectancy is believed to be near-normal with appropriate treatment, though severe attacks involving the brainstem can rarely be life-threatening.

---

## 12. Treatment

### 12.1 Acute Attack Treatment

**First-line**: High-dose IV methylprednisolone (1g/day for 3–5 days) — chosen by 84.1% of neurologists ([PMID: 40584638](https://pubmed.ncbi.nlm.nih.gov/40584638/))
- **MAXO**: MAXO:0001298 (corticosteroid therapy)

**Second-line (steroid-refractory)**:
- **Plasma exchange (PLEX)**: Level II evidence for improved visual outcomes in acute ON ([PMID: 41670578](https://pubmed.ncbi.nlm.nih.gov/41670578/)) — MAXO:0000602
- **IVIG**: Alternative rescue therapy — MAXO:0000571

### 12.2 Maintenance/Relapse Prevention

The meta-analysis by Thakolwiboon et al. compared steroid-sparing therapies: "Relapse probabilities and pooled mean ARR during therapies were as follows: AZA 53.1% [ARR 0.291], MMF 38.5% [ARR 0.836], RTX 48.9% [ARR 0.629], and mIVIG 25.3% [ARR 0.081]" ([PMID: 34634625](https://pubmed.ncbi.nlm.nih.gov/34634625/)).

| Therapy | Relapse Probability | ARR | Notes |
|---|---|---|---|
| **Maintenance IVIG** | 25.3% | 0.081 | Most effective; dose ≥1 g/kg q4w preferred |
| **Mycophenolate mofetil (MMF)** | 38.5% | 0.836 | Variable efficacy |
| **Rituximab (RTX)** | 48.9% | 0.629 | Less effective than in AQP4+ NMOSD |
| **Azathioprine (AZA)** | 53.1% | 0.291 | Moderate efficacy |

Pediatric data confirm IVIG superiority: "13% of patients with IVIG relapsed in the first year, compared to 33% in the IMT group (relative risk 0.70, 95% CI 0.53–0.99, p=0.061); HR for early relapse 0.36 (95% CI 0.15–0.87, p=0.023)" ([PMID: 41092852](https://pubmed.ncbi.nlm.nih.gov/41092852/)).

Adult multicenter IVIG data: median ARR decreased from 1.4 pre-treatment to 0 on IVIG (p<0.001). Higher doses (≥1 g/kg q4w) associated with lower relapse risk (HR 3.31 for lower dosing, p=0.02) ([PMID: 35377395](https://pubmed.ncbi.nlm.nih.gov/35377395/)).

### 12.3 Treatment Strategy Considerations

A critical treatment challenge: up to 50% of patients have monophasic disease and may not need maintenance therapy. "Sustained immunosuppression may not be required for all patients with MOGAD, whereas AQP4+NMOSD typically demands continuous therapy" ([PMID: 41927387](https://pubmed.ncbi.nlm.nih.gov/41927387/)).

**Early treatment window**: Treatment of first attack within <5 days may promote MOG-IgG seroconversion and reduce long-term relapse risk ([PMID: 39226035](https://pubmed.ncbi.nlm.nih.gov/39226035/)).

### 12.4 Emerging and Experimental Therapies

| Therapy | Mechanism | Status |
|---|---|---|
| **Satralizumab** | Anti-IL-6 receptor | Phase 3 (NCT05271273) |
| **Rozanolixizumab** | Anti-FcRn | Phase 3 (NCT05063162) |
| **Ravulizumab** | Anti-C5 complement | Phase 3 (NCT05545826) |
| **Tocilizumab (SC)** | Anti-IL-6 receptor | Off-label case reports ([PMID: 41393970](https://pubmed.ncbi.nlm.nih.gov/41393970/)) |
| **CAR T-cell therapy** | CD19/BCMA-directed B-cell depletion | Early phase ([PMID: 41470000](https://pubmed.ncbi.nlm.nih.gov/41470000/)) |
| **Antigen-specific tolerance** | OM-MOG35-55, tolerization | Preclinical ([PMID: 42131329](https://pubmed.ncbi.nlm.nih.gov/42131329/)) |

CAR T-cell therapy represents an emerging transformative approach: "These conditions are driven in part by autoreactive B cells that sustain chronic inflammation and progressive tissue damage. While current immunomodulatory therapies have improved clinical outcomes, they often require lifelong administration and fail to effectively eliminate compartmentalized inflammation within the central nervous system" ([PMID: 41470000](https://pubmed.ncbi.nlm.nih.gov/41470000/)).

### 12.5 Supportive and Rehabilitative Care

- Visual rehabilitation for patients with persistent visual impairment
- Physical therapy for motor disability from myelitis (MAXO:0000011)
- Cognitive rehabilitation for processing speed and working memory deficits
- Pain management (eye pain and body aches are the most bothersome symptoms)
- Psychological support for depression and work/school disruption

---

## 13. Prevention

### 13.1 Primary Prevention

No established primary prevention strategies exist for MOGAD. Avoidance of known triggers (e.g., TNF-alpha inhibitors) in susceptible individuals may be considered.

### 13.2 Secondary Prevention (Early Detection)

- MOG-IgG testing recommended in patients with bilateral ON, ADEM, LETM, cortical encephalitis, or atypical MS presentations
- 90.5% of neurologists send serum MOG-IgG after first demyelinating event ([PMID: 40584638](https://pubmed.ncbi.nlm.nih.gov/40584638/))
- 2024 revised McDonald MS criteria recommend MOG-IgG testing in children <12 years ([PMID: 40975101](https://pubmed.ncbi.nlm.nih.gov/40975101/))

### 13.3 Tertiary Prevention (Relapse Prevention)

- Maintenance IVIG is the most effective relapse prevention strategy
- Regular monitoring of visual function, motor function, and cognitive function
- Postpartum monitoring is critical given the increased relapse risk ([PMID: 41747756](https://pubmed.ncbi.nlm.nih.gov/41747756/))
- Pregnancy counseling: CD20 antibodies increasingly used around pregnancy with promising safety data ([PMID: 41925496](https://pubmed.ncbi.nlm.nih.gov/41925496/))

---

## 14. Other Species / Natural Disease

### 14.1 Natural Disease

No naturally occurring MOGAD equivalent has been described in companion animals or wildlife. MOG is conserved across mammals, but spontaneous anti-MOG autoimmunity has not been documented outside humans.

### 14.2 Orthologous Genes

- **Mouse MOG**: NCBI Gene ID 17441 (Mus musculus, NCBI Taxon: 10090)
- **Rat MOG**: NCBI Gene ID 24558 (Rattus norvegicus, NCBI Taxon: 10116)
- **Marmoset MOG**: Ortholog present (Callithrix jacchus, NCBI Taxon: 9483)

---

## 15. Model Organisms

### 15.1 Mouse MOG-EAE Models

- **MOG35-55 peptide-induced EAE** (C57BL/6): T-cell-mediated model; does not require B cells
- **Recombinant MOG protein-induced EAE**: B-cell-dependent model; better recapitulates antibody-mediated aspects
- B-cell depletion exacerbates peptide EAE but ameliorates protein EAE ([PMID: 20641064](https://pubmed.ncbi.nlm.nih.gov/20641064/))
- Early mitochondrial dysfunction at synapses (day 5 post-injection) precedes clinical signs ([PMID: 41898442](https://pubmed.ncbi.nlm.nih.gov/41898442/))

### 15.2 Marmoset MOG-EAE Model

"MOG-induced EAE in common marmoset monkeys reflects one specific lesional subtype of MS, namely MS pattern II lesions with antibody/complement-mediated damage" ([PMID: 16900750](https://pubmed.ncbi.nlm.nih.gov/16900750/)). CD20+ B-cell depletion "profoundly reduced the development of both white and gray matter lesions" ([PMID: 22002426](https://pubmed.ncbi.nlm.nih.gov/22002426/)). This is the best available model for antibody-mediated demyelination in MOGAD.

### 15.3 In Vitro Models

Rat telencephalon aggregate cultures: Antibody-mediated demyelination with MOG antibodies + complement, showing demyelination without cell death and protective TNF-alpha/alphaB-crystallin upregulation ([PMID: 15478179](https://pubmed.ncbi.nlm.nih.gov/15478179/)).

### 15.4 Model Limitations

- Mouse peptide EAE is primarily T-cell-driven and does not fully recapitulate antibody-mediated pathology
- No animal model perfectly reproduces the monophasic vs. relapsing dichotomy
- Marmoset EAE is more translational but expensive and limited by availability
- MOG-EAE does not capture the age-dependent phenotype spectrum (ADEM vs. ON)

### 15.5 Translational Applications

MOG-EAE models have directly informed treatment approaches including corticosteroids, PLEX, IVIG, complement inhibition, and B-cell depletion strategies ([PMID: 40463369](https://pubmed.ncbi.nlm.nih.gov/40463369/)). Novel remyelination compounds (bavisant, morusin) have been identified through EAE screening ([PMID: 41564155](https://pubmed.ncbi.nlm.nih.gov/41564155/); [PMID: 41828535](https://pubmed.ncbi.nlm.nih.gov/41828535/)).

---

## Evidence Base: Key Literature

### Landmark Papers

| PMID | Topic | Key Contribution |
|---|---|---|
| [36706773](https://pubmed.ncbi.nlm.nih.gov/36706773/) | 2023 Diagnostic Criteria | Defines the disease and diagnostic framework |
| [32048003](https://pubmed.ncbi.nlm.nih.gov/32048003/) | MOGAD Pathology | Definitive neuropathological characterization |
| [32412053](https://pubmed.ncbi.nlm.nih.gov/32412053/) | Brain Biopsy Analysis | Quantifies perivenous demyelination pattern |
| [32883348](https://pubmed.ncbi.nlm.nih.gov/32883348/) | CSF Findings | OCB absence (~90%), MRZ negativity (100%) |
| [27793206](https://pubmed.ncbi.nlm.nih.gov/27793206/) | 50-Patient Study | Long-term disability outcomes |
| [34634625](https://pubmed.ncbi.nlm.nih.gov/34634625/) | Treatment Meta-analysis | IVIG superiority for relapse prevention |
| [41865559](https://pubmed.ncbi.nlm.nih.gov/41865559/) | Danish Epidemiology | First population-based incidence/prevalence |
| [41657079](https://pubmed.ncbi.nlm.nih.gov/41657079/) | South Wales Epidemiology | UK prevalence and phenotype data |
| [28057865](https://pubmed.ncbi.nlm.nih.gov/28057865/) | Cocapture Mechanism | Molecular basis of infection-triggered MOGAD |
| [40685157](https://pubmed.ncbi.nlm.nih.gov/40685157/) | MRI Resolution | T2 lesion resolution discriminates from MS |
| [39226035](https://pubmed.ncbi.nlm.nih.gov/39226035/) | Early Treatment | Treatment timing and seroconversion |
| [41470000](https://pubmed.ncbi.nlm.nih.gov/41470000/) | CAR T-cell Therapy | Emerging therapeutic approach |

---

## Limitations and Knowledge Gaps

1. **No GWAS or comprehensive genetic studies** for MOGAD susceptibility — the genetic architecture is entirely unknown
2. **No epigenetic data** — no studies of DNA methylation, histone modifications, or chromatin states in MOGAD
3. **No FDA-approved MOGAD-specific therapy** — all treatments are off-label or in clinical trials
4. **Biomarker gaps** — no validated biomarker reliably predicts monophasic vs. relapsing course at onset
5. **Limited multi-omics profiling** — transcriptomic, proteomic, and metabolomic signatures largely uncharacterized
6. **Pediatric treatment data** — most evidence from retrospective studies; RCTs in children lacking
7. **Ethnic/geographic heterogeneity** — significant variation in prognosis between populations (Japanese vs. European) is unexplained
8. **Overlap syndromes** — biology and optimal management of MOG-NMDAR overlap poorly understood
9. **Long-term outcomes** — follow-up limited to 5–10 years in most cohorts
10. **Cognitive impairment mechanisms** — pathophysiology of processing speed/working memory deficits not elucidated
11. **Animal model limitations** — no single EAE model recapitulates all aspects of human MOGAD
12. **Pharmacogenomics** — no pharmacogenomic data exist for MOGAD treatments

---

## Proposed Follow-up Experiments and Actions

### Near-Term (1–2 years)

1. **GWAS study of MOGAD**: Recruit large international cohorts (N>1,000) to identify genetic susceptibility loci
2. **Longitudinal biomarker validation**: Prospective studies correlating serial sNfL, sGFAP, and MOG-IgG titers with relapse risk
3. **RCT completion and analysis**: Monitor outcomes of ongoing Phase 3 trials (satralizumab NCT05271273, rozanolixizumab NCT05063162, ravulizumab NCT05545826)
4. **Single-cell transcriptomic profiling**: Characterize immune cell populations in MOGAD CSF and blood during attacks vs. remission

### Medium-Term (2–5 years)

5. **Epigenomic profiling**: DNA methylation and chromatin accessibility studies in MOGAD patient immune cells
6. **CAR T-cell therapy trials**: Controlled trials of CD19-directed CAR T-cell therapy for refractory MOGAD
7. **Antigen-specific tolerance induction**: Advance OM-MOG35-55 through Phase 1/2 trials
8. **Multi-omics integration**: Combine transcriptomics, proteomics, and metabolomics for comprehensive molecular models
9. **Pregnancy management protocols**: Develop evidence-based guidelines for treatment during pregnancy and postpartum

### Long-Term (5+ years)

10. **Precision medicine framework**: Genotype-informed and biomarker-guided treatment algorithms
11. **Natural history registries**: International registries with >20-year follow-up
12. **Improved animal models**: Humanized mouse models expressing human MOG-IgG1

---

## Ontology Term Summary

### HPO (Human Phenotype Ontology)
HP:0100653 (Optic neuritis) | HP:0100510 (Transverse myelitis) | HP:0007305 (CNS demyelination) | HP:0001298 (Encephalopathy) | HP:0001250 (Seizures) | HP:0100543 (Cognitive impairment) | HP:0000572 (Visual loss) | HP:0003470 (Paralysis) | HP:0012378 (Fatigue) | HP:0012531 (Pain) | HP:0012229 (CSF pleocytosis)

### GO (Gene Ontology)
GO:0043209 (Myelin sheath) | GO:0042552 (Myelination) | GO:0006958 (Complement activation, classical pathway) | GO:0042110 (T cell activation) | GO:0050853 (B cell receptor signaling) | GO:0006955 (Immune response) | GO:0005886 (Plasma membrane)

### CL (Cell Ontology)
CL:0000128 (Oligodendrocyte) | CL:0000624 (CD4+ T cell) | CL:0000236 (B cell) | CL:0000094 (Granulocyte) | CL:0000235 (Macrophage)

### UBERON (Anatomical Ontology)
UBERON:0000941 (Optic nerve) | UBERON:0002240 (Spinal cord) | UBERON:0002316 (White matter) | UBERON:0000956 (Cerebral cortex) | UBERON:0002298 (Brainstem) | UBERON:0003833 (Conus medullaris) | UBERON:0000966 (Retina)

### CHEBI (Chemical Entities)
CHEBI:6888 (Methylprednisolone) | CHEBI:64357 (Rituximab) | CHEBI:168396 (Tocilizumab) | CHEBI:2948 (Azathioprine) | CHEBI:168612 (Mycophenolate mofetil)

### MAXO (Medical Action Ontology)
MAXO:0001298 (Corticosteroid therapy) | MAXO:0000602 (Plasmapheresis) | MAXO:0000571 (IVIG therapy) | MAXO:0000780 (B-cell depletion therapy) | MAXO:0001001 (Immunosuppressive therapy)

### MONDO
MONDO:0100475 (MOG antibody-associated disease)

---

*Report generated from systematic review of 142 publications with 21 confirmed findings supported by direct abstract citation evidence across 5 investigation iterations. This comprehensive disease characterization covers all 15 sections of the disease knowledge base template with ontology-annotated entries suitable for database population.*
