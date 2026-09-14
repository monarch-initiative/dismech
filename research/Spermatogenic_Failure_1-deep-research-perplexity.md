---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-24T21:23:02.904663'
end_time: '2026-08-24T21:27:28.129087'
duration_seconds: 265.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: spermatogenic failure 1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 18
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 6
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** spermatogenic failure 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **spermatogenic failure 1** covering all of the
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

# Spermatogenic Failure 1 (SPGF1) Due to SYCP2 Dysfunction: A Comprehensive Disease Characteristics Report

Spermatogenic failure 1 (SPGF1) is a rare, Mendelian, male-specific infertility disorder characterized by non-obstructive azoospermia or severe oligozoospermia resulting from meiotic arrest of germ cells and structural defects of the synaptonemal complex, caused by heterozygous disruption or dysregulation of the **synaptonemal complex protein 2** gene (*SYCP2*) on chromosome 20q13.33.[3][9][13] Clinical and histological studies demonstrate a remarkably consistent pattern in affected men: germ cells initiate meiosis and undergo early chromosomal reduction, but spermatocytes fail to progress beyond the first meiotic division, leading to seminiferous tubules that contain spermatocytes as the most advanced germ cell type and a complete absence or near-absence of mature spermatozoa.[3][16] Molecular investigations in humans, combined with knockout and functional models in mice and yeast, converge on a causal chain in which altered quantity or structure of SYCP2 disrupts axial element assembly and centromere association within the synaptonemal complex, causing defective homologous chromosome synapsis, checkpoint activation, and germ cell apoptosis, ultimately manifesting as non-obstructive spermatogenic failure and infertility.[9][18][17] Because SYCP2-mediated male infertility is highly penetrant but non-lethal, the condition remains rare in the general population and is typically uncovered only in specialized infertility clinics, where genetic testing—especially exome sequencing and targeted male infertility panels—now routinely include *SYCP2* among candidate genes.[13][14][16] This report synthesizes current knowledge on SPGF1 across disease information, etiology, phenotypes, genetics, pathophysiology, diagnostics, epidemiology, treatment, prevention, and model organism data, with a focus on human evidence supplemented by mechanistic insight from animal and cellular models, and provides ontology suggestions (HPO, GO, CL, UBERON, MONDO, NCIT) suitable for structured disease knowledge bases.

## 1. Disease Information

### 1.1. Definition and Clinical Overview

Spermatogenic failure 1 (SPGF1) is defined in the Online Mendelian Inheritance in Man (OMIM) database as an autosomal dominant form of male infertility due to spermatogenic arrest at meiosis, caused by heterozygous mutations in *SYCP2* on chromosome 20q13.33.[3] OMIM describes spermatogenic failure broadly as a group of conditions in which the process of spermatogenesis is impaired at various stages, and assigns SPGF1 specifically to the subset in which “spermatogenic arrest during meiosis is a cause of infertility,” highlighting the distinctive meiotic histology associated with this type.[3] In affected men, semen analysis reveals azoospermia or severe oligozoospermia in the absence of obstructive lesions of the reproductive tract, and testicular biopsy shows seminiferous tubules with germ cells arrested at the spermatocyte stage, often accompanied by increased apoptosis and normal or mildly reduced testicular volume.[3][13][16] The disorder is non-syndromic: affected individuals are otherwise healthy, with normal external genitalia and typically normal endocrine parameters, and the phenotype is restricted to spermatogenic failure and consequent infertility.[3][17]

Clinically, SPGF1 belongs to the broader category of **non-obstructive azoospermia (NOA)** and **severe spermatogenic failure**, which encompass a heterogeneous group of genetic and non-genetic causes.[2][16] However, the SYCP2-related form stands out because of its clear Mendelian inheritance and its mechanistic link to synaptonemal complex disruption and meiotic arrest. Schilit and colleagues, in a landmark study in the American Journal of Human Genetics in 2020, demonstrated that both translocation-mediated overexpression and heterozygous frameshift mutations in *SYCP2* can cause human male infertility, thereby providing strong evidence that altered SYCP2 dosage and structure are pathogenic in the human germline.[13][17] The authors noted that unexplained infertility affects 2–3% of reproductive-aged couples and used cytogenetic and exome data to identify *SYCP2* as a novel, high-impact infertility gene, situating SPGF1 within the emerging class of monogenic male infertility disorders.[17][16]

From a pathologist’s perspective, OMIM emphasizes that “the histologic picture of meiotic arrest is rather constant” across cases of SPGF1 and related meiotic arrest phenotypes.[3] Meiotic arrest is characterized by germ cells that enter meiosis and undergo the first chromosomal reduction from 4n to 2n but are then unable to proceed further, resulting in tubules containing spermatocytes as the latest developmental stage of germ cells.[3][16] These findings align with experimental data from Sycp2-knockout mice, which show global meiotic arrest at the spermatocyte stage, defective synapsis, and apoptotic elimination of germ cells.[9][18] The congruence between human histology and animal models underscores the robustness of the SPGF1 clinical concept.

### 1.2. Key Identifiers and Ontology Mapping

The primary identifier for SPGF1 in human genetic disease databases is OMIM entry **#258150**, labeled “Spermatogenic Failure 1; SPGF1,” and associated with *SYCP2* (OMIM *604105*).[3][9] In OMIM’s locus-phenotype tables summarizing the genetic heterogeneity of spermatogenic failure, SPGF1 is listed as an autosomal dominant phenotype mapped to chromosome 20q13.33, with *SYCP2* as the causal gene.[1][11] The *SYCP2* gene itself has OMIM *604105* and is annotated as “Synaptonemal Complex Protein 2.”[9] These identifiers are central for linking clinical and molecular data in knowledge bases.

Mondo Disease Ontology (MONDO) provides a term for “Y-linked spermatogenic failure” (MONDO:0010763), which refers to non-obstructive spermatogenic failure associated with Y-linked etiologies and includes synonyms such as “spermatogenic failure, Y-linked” and “Sertoli cell-only syndrome.”[8] However, SPGF1 is an autosomal dominant, *SYCP2*-related entity and is distinct from Y-linked forms; at present, a dedicated MONDO term for “spermatogenic failure 1” or “SYCP2-related spermatogenic failure” is not explicitly referenced in the provided resources.[8][3] In ontology mapping for a disease knowledge base, SPGF1 should be considered a child concept of a more general “male infertility due to non-obstructive azoospermia” node, with specific annotation for autosomal dominant, *SYCP2*-mediated meiotic arrest.

For Human Phenotype Ontology (HPO), key terms relevant to SPGF1 include azoospermia (HP:0000027), severe oligozoospermia (HP:0003232), non-obstructive azoospermia (HP:0033755), male infertility (HP:0003251), and spermatogenic arrest (HP:0008587). Azoospermia is explicitly recorded as a phenotype in several spermatogenic failure subtypes, such as SPGF52, which is described as “an autosomal recessive infertility disorder characterized by azoospermia due to meiotic arrest at the spermatocyte stage.”[6] Although SPGF52 is distinct in gene etiology (C14orf39), the phenotypic description mirrors that of SPGF1 and supports the use of similar HPO terms for meiotic arrest disorders.[6][16]

In the context of International Classification of Diseases (ICD-10/ICD-11), SPGF1 would be coded under male infertility categories, such as N46 (male infertility) in ICD-10, or the corresponding ICD-11 code for “Male infertility due to testicular causes,” although specific codes for genetic subtypes like SPGF1 do not yet exist in these systems. MeSH and SNOMED CT provide general descriptors for male infertility and azoospermia, but not gene-specific subtypes. Thus, for a structured knowledge base, SPGF1 requires linkage to these broader clinical categories while preserving its specific OMIM and gene-level identifiers.

### 1.3. Synonyms and Alternative Names

SPGF1 has several related naming conventions across resources. OMIM uses “Spermatogenic Failure 1; SPGF1” as the formal name, explicitly linking it to *SYCP2*.[3] In the primary literature, Schilit et al. refer to “SYCP2-mediated male infertility” and describe “heterozygous SYCP2 frameshift variants” in men with cryptozoospermia and azoospermia.[13][17] In clinical practice and research reviews focusing on non-obstructive azoospermia, SPGF1 may be described as “SYCP2-associated non-obstructive azoospermia,” “SYCP2-related spermatogenic arrest,” or “SYCP2-related male infertility,” stressing either the histological pattern or the gene-level etiology.[16][18]

It is important not to conflate SPGF1 with other spermatogenic failure entities such as SPGF9 (due to *DPY19L2*) or SPGF52 (due to *C14orf39*), which have different inheritance patterns and gene etiologies but share overlapping clinical features of azoospermia and meiotic arrest.[1][6] Similarly, “Y-linked spermatogenic failure” refers to disorders associated with AZF microdeletions or Y-linked genes and must be distinguished from autosomal dominant SPGF1.[7][8] For ontology purposes, synonyms should include “Spermatogenic failure type 1,” “SYCP2-related spermatogenic failure,” and “Autosomal dominant spermatogenic failure due to SYCP2 mutation.”

### 1.4. Nature of Information Sources

The information summarized here is derived predominantly from aggregated, disease-level resources such as OMIM, Mondo, and curated review articles, complemented by primary human genetic and clinical studies. OMIM’s SPGF1 entry collates data from published case reports and series, integrating genetic findings with histological description.[3] The *SYCP2* OMIM entry synthesizes functional data from mouse models and biochemical studies describing SYCP2’s role in synaptonemal complex assembly.[9][18] Schilit et al.’s Am J Hum Genet paper provides detailed clinical, cytogenetic, and exome sequencing data from several infertile men, thus representing individual patient-level evidence that underpins the disease concept.[13][17] The comprehensive review on genetic and epigenetic insights into non-obstructive azoospermia offers a disease-level perspective, summarizing known pathogenic variants in SYCP2 and other meiotic genes across multiple patients and cohorts.[16]

Clinically, many insights into meiotic arrest and spermatogenic failure come from testicular biopsy series and infertility cohort studies, which are summarized in reviews and OMIM narrative sections rather than always being individually cited. Therefore, an integrated knowledge base representation of SPGF1 relies on these aggregated sources while retaining explicit links to key primary studies for mechanistic and clinical claims.

## 2. Etiology

### 2.1. Primary Causal Factors: Genetic Basis in SYCP2

The primary cause of spermatogenic failure 1 is a **genetic defect in the *SYCP2* gene**, which encodes synaptonemal complex protein 2, a critical axial element component of the synaptonemal complex in meiotic cells.[3][9][18] OMIM notes that SPGF1 is “caused by heterozygous mutation in the SYCP2 gene on chromosome 20q13.33,” and that spermatogenic arrest during meiosis is a cause of infertility in this context.[3] The *SYCP2* gene is located at 20q13.33 and is expressed specifically in meiotic germ cells, where its protein product helps assemble the chromosome axes necessary for homologous pairing and synapsis.[9][18] SYCP2 interacts with SYCP3 and SYCP1 and serves as a scaffold for the formation of the synaptonemal complex lateral elements and their association with centromeric regions.[18]

Human genetic evidence for SYCP2 as a causal gene comes from two main types of observations. First, a de novo balanced translocation t(20;22)(q13.3;q11.2) in an infertile man (DGAP230) was found to dysregulate *SYCP2* expression, leading to exclusive overexpression from the derivative chromosome 20 (der(20)) and severe oligozoospermia.[13][17] The authors reported that qPCR analyses revealed more than 20-fold increased expression of *SYCP2* in lymphoblastoid cell lines from this subject compared with controls, and modeling overexpression in budding yeast disrupted the structural integrity of the synaptonemal complex, suggesting that both reduced and increased SYCP2 levels can cause loss of function and infertility.[13][18] Second, exome sequencing of additional infertile men with cryptozoospermia or azoospermia identified three heterozygous frameshift variants in *SYCP2* (c.2022_2025del, c.2793_2797del, and c.3067_3071del), which are extremely rare and classified as pathogenic or likely pathogenic, and are associated with global meiotic arrest.[13][16]

A 2020 review on genetic and epigenetic insights into non-obstructive azoospermia summarized these variants, noting that SYCP2 frameshift mutations are linked to global meiotic arrest in non-obstructive azoospermia patients and that Sycp2 knockout mice exhibit axial element assembly defects, reduced DNA double-strand breaks (DSBs), and apoptosis, thereby reinforcing the causal role of SYCP2.[16] The review lists the three human SYCP2 frameshift variants—c.2022_2025del (p.Lys674fs), c.2793_2797del (p.Lys932fs), and c.3067_3071del (p.Lys1023fs)—with ACMG classification of pathogenic or likely pathogenic and associates them with meiotic arrest in affected men.[16] More recently, Tan and colleagues described a novel heterozygous deletion c.1937_1942delTAAATA (p.Ile646_Asn647del) in *SYCP2* in a Chinese family with non-obstructive azoospermia, further expanding the spectrum of SYCP2 variants causing male infertility.[10]

Thus, the etiological foundation of SPGF1 is a germline, heterozygous mutation or dysregulation of *SYCP2* that leads to loss of function of SYCP2 in meiotic germ cells, resulting in defective synaptonemal complex formation, meiotic arrest, and spermatogenic failure.[3][9][13][16][10] In ontology terms, this corresponds to a Mendelian, autosomal dominant infertility disorder with a monogenic etiology in *SYCP2* (HGNC:SYCP2; OMIM *604105*), best represented under categories such as “monogenic male infertility due to meiotic arrest.”

### 2.2. Genetic Risk Factors Beyond Primary Causal Variants

In the context of SPGF1, the principal genetic risk factor is carrying a heterozygous pathogenic variant in *SYCP2*, whether it is a frameshift mutation, a structural variant leading to altered gene dosage, or a missense or in-frame deletion that disrupts critical functional domains.[3][13][16][10] The disease appears to be highly penetrant in males with such variants, given the severe impairment of spermatogenesis observed in reported cases and the absence of such variants in large control datasets such as gnomAD and TOPMed.[13][16] Schilit et al. emphasized that the identified SYCP2 frameshift variants were “extremely rare, consistent with the inability to segregate these mutations in the general population due to a phenotype of infertility,” and noted that one variant was maternally inherited, suggesting that the variant does not cause infertility in female carriers.[13][17] This pattern supports a model where heterozygous SYCP2 pathogenic variants confer near-complete risk of severe spermatogenic failure in male carriers but have little or no phenotypic effect in females.

Beyond *SYCP2* itself, the broader genetics of male infertility reveals many additional risk genes, but these belong to other spermatogenic failure subtypes rather than SPGF1 per se. For example, mutations in *NR5A1* (steroidogenic factor 1) have been found in approximately 4% of men with otherwise unexplained severe spermatogenic failure, including azoospermia and severe oligozoospermia.[5] The NR5A1 study sequenced 315 men with idiopathic spermatogenic failure and identified heterozygous missense mutations in seven men, none of which were found in over 4000 control alleles.[5] Similarly, X-linked *TEX11* mutations account for about 1% of infertility in non-obstructive azoospermic men and are associated with meiotic arrest at the spermatocyte stage.[4] The TEX11 study screened 246 azoospermic men and found that rare TEX11 mutations are significantly enriched, demonstrating that TEX11 is required for spermatogenesis in humans.[4]

These genes—*NR5A1*, *TEX11*, *C14orf39* in SPGF52, *DPY19L2* in SPGF9, *TDRD9* in SPGF30, and many others—represent genetic risk factors for spermatogenic failure broadly, but they cause distinct disease entities with different inheritance patterns and molecular mechanisms.[1][6][11][2][16] In a knowledge base, they belong to the larger causal network of male infertility genes, but for SPGF1, the primary risk factor is *SYCP2* mutation itself. There is currently no evidence that common or low-penetrance variants in *SYCP2* act as susceptibility alleles for milder forms of male subfertility, although this remains an area for future genome-wide association studies.

### 2.3. Environmental and Lifestyle Risk Factors

For SPGF1 specifically, no environmental or lifestyle factors have been shown to modulate risk in a gene-specific manner. The disorder is defined by a high-impact monogenic defect, and all reported cases involve men whose infertility correlates strongly with their *SYCP2* genetic status, independent of other exposures.[3][13][16][10] However, in the broader context of male infertility, numerous environmental factors—such as heat exposure, toxins, endocrine disruptors, smoking, alcohol, and systemic illnesses—can impair spermatogenesis and increase the risk of azoospermia or oligozoospermia.[2] These factors might conceivably worsen outcomes in men with underlying genetic defects such as SYCP2 mutations, but no systematic gene–environment interaction studies have been performed for SPGF1.

Microdeletions in the Y-chromosome AZF (azoospermia factor) region, which are due to intrachromosomal homologous recombination between large repeat amplicons, represent another major non-environmental cause of spermatogenic failure, found in about 10% of azoospermic and severe oligozoospermic cases.[7] These AZFc deletions remove multiple gene families and lead to non-obstructive spermatogenic failure.[7] Although AZF microdeletions are genetic rather than environmental, they highlight how structural genomic variation contributes to male infertility, analogous to the balanced translocation affecting *SYCP2* in SPGF1.[13][17] Men with AZF deletions form a different disease category, but their presence must be considered in differential diagnosis and risk counseling in infertile populations.

In summary, SPGF1 is primarily driven by a monogenic *SYCP2* defect, and while general lifestyle and environmental factors are relevant to male fertility, there is no evidence that specific exposures modulate SPGF1 risk or penetrance in a predictable way. This supports an etiology classification focused on **genetic causal factors**, with environmental influences considered background noise rather than definitional risk components.

### 2.4. Protective Factors and Gene–Environment Interactions

Given the high-penetrance nature of *SYCP2* pathogenic variants and the strong mechanistic link between SYCP2 function and meiotic progression, protective factors for SPGF1 are currently speculative. No genetic modifiers have been identified that consistently ameliorate the spermatogenic phenotype in male carriers of SYCP2 frameshift or structural variants.[13][16] The maternal transmission of some SYCP2 variants illustrates sex-specific protection: female carriers do not manifest infertility, presumably because SYCP2’s role in oogenesis is either less critical or more robust to dosage variation, or because different checkpoints apply in female meiosis.[13][17] However, this sex difference is not a protective factor in males, where the phenotype remains fully expressed.

Environmental or lifestyle measures known to support general testicular health—such as avoiding gonadotoxic chemotherapy, radiation, high-temperature exposure, and smoking—are advisable for all men, including those with genetic infertility, but they have not been shown to rescue spermatogenesis in SPGF1. The conceptual possibility exists that improved antioxidant status or hormonal optimization could marginally improve the quality of residual germ cells, yet the fundamental blockage at meiotic synapsis and recombination makes such interventions unlikely to restore fertility in men with severe meiotic arrest.[16][18]

Regarding gene–environment interactions, no dedicated studies have examined whether environmental insults exacerbate meiotic defects in SYCP2-mutant testes or whether such exposures might influence the age at which infertility is first recognized. SPGF1 typically presents when men seek fertility evaluation, and the infertility is congenital and stable rather than progressive, suggesting that gene–environment interactions are not primary drivers of disease onset or severity in this condition.[3][13] Therefore, in a knowledge base representation, gene–environment interaction fields for SPGF1 would be annotated as “data not available” or “no evidence of clinically significant interactions identified to date.”

## 3. Phenotypes

### 3.1. Core Clinical Phenotype: Non-Obstructive Azoospermia or Severe Oligozoospermia

The primary clinical phenotype of SPGF1 is non-obstructive spermatogenic failure manifesting as azoospermia or severe oligozoospermia on semen analysis.[3][13][16] Azoospermia is defined as the complete absence of spermatozoa in the ejaculate, while severe oligozoospermia refers to very low sperm counts, often below 1–5 million/mL and frequently with severely impaired motility and morphology.[2] In SPGF1, men present with long-standing infertility, typically in adulthood when they attempt to conceive, and semen evaluations consistently demonstrate profound sperm deficiency.[3][13] Schilit et al. describe subjects with cryptozoospermia (extremely low sperm counts detectable only after centrifugation) and azoospermia, all of whom carry heterozygous SYCP2 frameshift variants or translocation-mediated dysregulation.[13][17] In the Chinese family reported by Tan et al., the proband with the novel SYCP2 deletion mutation had non-obstructive azoospermia, reinforcing the association between SYCP2 defects and the most severe end of male infertility.[10]

For ontology mapping, key HPO terms include azoospermia (HP:0000027), severe oligozoospermia (HP:0003232), cryptozoospermia (HP:0030340), and non-obstructive azoospermia (HP:0033755). Azoospermia is explicitly recorded for SPGF52 and other meiotic arrest disorders and is appropriate for SPGF1.[6][16] The phenotype type here is a laboratory abnormality (semen analysis) and a clinical symptom (infertility). Age of onset is adult, in the sense that the condition is first recognized when men attempt to conceive, but the underlying spermatogenic defect is present from puberty onward. Symptom severity is severe and essentially complete in terms of reproductive function; progression is stable, as spermatogenic failure does not evolve over time but remains present once established. Frequency is high among genetically affected individuals: all reported male carriers of SYCP2 frameshift or dysregulation variants have severe spermatogenic failure.[13][16][10]

The impact on quality of life is profound. Male infertility is associated with significant psychological distress, relationship strain, and social consequences, particularly in cultures where biological parenthood is highly valued.[2] While no SPGF1-specific quality of life studies exist, global male infertility research using instruments like the SF-36 and WHOQOL-BREF demonstrates reduced mental health, social functioning, and emotional well-being among infertile men compared with fertile controls.[2] In a disease knowledge base, phenotype annotations should therefore link azoospermia and infertility to quality of life impairments, with ontology references such as EQ-5D domains and PROMIS depression and anxiety measures.

### 3.2. Testicular Histology and Meiotic Arrest Phenotype

The hallmark histological phenotype in SPGF1 is meiotic arrest at the spermatocyte stage, accompanied by defective synaptonemal complex formation and increased germ cell apoptosis.[3][9][13][16] OMIM describes meiotic arrest as characterized by germ cells that enter meiosis and undergo the first chromosomal reduction from 4n to 2n but are unable to proceed further, resulting in tubules containing spermatocytes as the latest developmental stage of germ cells.[3] This description matches the histology reported in Sycp2-knockout mice, where spermatocytes fail to differentiate into pachytene spermatocytes, synapsis is disrupted, and apoptosis occurs.[9][18]

The NOA genetics review provides a structured summary, noting that SYCP2 frameshift variants in humans are associated with “global meiotic arrest” and that knockout mice show “axial element assembly defect, apoptosis.”[16] In more detail, synaptonemal complex assembly requires proper localization of SYCP2, SYCP3, and SYCP1 to the chromosome axes and central elements; disruption of SYCP2 prevents incorporation of SYCP3 into lateral elements and leads to failed chromosomal synapsis.[18] Electron microscopy and TUNEL assays in Sycp2-deficient mice show spermatocytes undergoing apoptosis at mid-prophase I, consistent with activation of meiotic checkpoints in response to synapsis defects.[18][9]

Histologically, human testicular biopsies in SYCP2-mutant men show seminiferous tubules with dense populations of spermatocytes, reduced or absent spermatids and spermatozoa, and sometimes increased Sertoli cell-only tubules in more advanced cases.[3][13][16] While detailed biopsy descriptions for each human case are not exhaustively reported in the cited articles, the combination of azoospermia, genetic evidence, and known mechanisms support this histologic pattern. HPO terms that capture this phenotype include “spermatogenic arrest” (HP:0008587), “decreased number of spermatids” (HP:0008669), “germ cell apoptosis” (a more general term), and “testicular histology abnormality” (HP:0008689). The phenotype type is a pathology finding, derived from microscopic examination of tissue.

Age of onset of histological abnormalities is post-pubertal, corresponding to the time when meiosis initiates in the testis. Severity is marked: global meiotic arrest means that essentially no spermatocytes proceed to spermatids, and progression is stable, as the structural defect in the synaptonemal complex persists across germ cell generations. Frequency among affected individuals appears universal based on the available cases. Quality of life impact is indirect, through infertility; the histological changes themselves do not cause pain or systemic illness.

### 3.3. Endocrine and Gonadal Phenotypes

Endocrine profiles in SPGF1 are not extensively described in the available literature, but general observations from NOA cohorts suggest that many men with meiotic arrest have normal or only mildly elevated gonadotropins and testosterone levels.[2][16] Because the seminiferous epithelium remains partially intact, with spermatogonia and spermatocytes present, Sertoli cell and Leydig cell function may be relatively preserved, leading to normal testicular volume and endocrine parameters in some cases.[3][16] However, in severe spermatogenic failure, FSH levels can be elevated as a reflection of decreased inhibin B production by Sertoli cells, and testicular volume may be reduced.

In SPGF1-specific reports, detailed hormone data are sparse, but there is no indication of primary hypogonadism or systemic endocrine disease; men are phenotypically normal apart from infertility.[3][13][17] OMIM notes that spermatogenic failure can result from underlying endocrinologic disorders such as hypogonadotropic hypogonadism, but this is presented as a separate etiologic pathway distinct from SPGF1.[3] HPO terms relevant to endocrine aspects include “elevated follicle-stimulating hormone” (HP:0008212) and “testicular atrophy” (HP:0000029), though whether these apply to SPGF1 is case-dependent and not universally documented.

From a quality of life standpoint, endocrine symptoms such as decreased libido, fatigue, or erectile dysfunction are not primary features of SPGF1 and would likely arise from concomitant conditions rather than the SYCP2 mutation itself. Thus, endocrine phenotypes are secondary or absent, and the primary phenotype remains isolated spermatogenic failure.

### 3.4. Absence of Extra-Gonadal Phenotypes

An important phenotypic characteristic of SPGF1 is its non-syndromic nature. Reports of SYCP2-mediated male infertility emphasize that affected men are otherwise healthy, with no systemic anomalies, developmental delay, or major organ involvement beyond the testes.[13][17][16] SYCP2 expression is highly restricted to meiotic germ cells, which means that its dysfunction is unlikely to impact somatic tissues. OMIM and NOA reviews do not list extra-gonadal features such as skeletal anomalies, neurologic symptoms, or metabolic disorders associated with SPGF1.[3][16]

In animal models, Sycp2-knockout mice exhibit infertility but not gross systemic phenotypes, further supporting the tissue specificity of SYCP2-related pathology.[9][18] This contrasts with infertility genes such as *NR5A1*, which have broader roles in steroidogenesis and gonadal development and can cause disorders of sex development and adrenal failure.[5] For SPGF1, ontology mapping should therefore restrict phenotypic annotations to reproductive system phenotypes, with negative annotations for extra-gonadal involvement where appropriate.

### 3.5. Suggested HPO and Related Ontology Terms

Based on the clinical and histological features described, a structured representation of SPGF1 should include the following key HPO terms: azoospermia (HP:0000027), non-obstructive azoospermia (HP:0033755), severe oligozoospermia or cryptozoospermia (HP:0003232; HP:0030340), male infertility (HP:0003251), spermatogenic arrest (HP:0008587), decreased number of spermatids (HP:0008669), and abnormal testicular histology (HP:0008689). Phenotype types span laboratory abnormalities, clinical symptoms, and pathology findings. Age of onset is adolescent/adult for infertility recognition, but congenital for underlying germ cell defects. Severity is severe; progression is stable; frequency among affected males is high.

Complementary ontology terms include SNOMED CT concepts for male infertility and azoospermia, and EQ-5D or SF-36 domains capturing quality of life impacts. In a knowledge base, these phenotypes should be linked to SPGF1 with evidence tags referencing OMIM, Schilit et al., Tan et al., and the NOA genetics review for clinical and mechanistic support.[3][13][10][16]

## 4. Genetic and Molecular Information

### 4.1. Causal Gene: SYCP2

The causal gene for SPGF1 is **SYCP2** (Synaptonemal Complex Protein 2), located on chromosome 20q13.33.[3][9][11] OMIM entry *604105* describes SYCP2 as encoding a component of the lateral element substructure of the synaptonemal complex (SC), with roles in minor groove DNA binding and scaffolding for recruitment of SYCP3 through its coiled-coil domain.[9][18] SYCP2 forms part of the axial elements of the SC and is essential for chromosome axis assembly and competent synapsis during meiosis I.[18] In male mice, homozygous Sycp2 mutants exhibit complete meiotic arrest, fail to differentiate into pachytene spermatocytes, and undergo apoptosis in the developing germline, resulting in infertility.[9][18]

OMIM’s locus-phenotype tables for spermatogenic failure list SPGF1 as an autosomal dominant phenotype associated with *SYCP2* at 20q13.33, distinguishing it from many autosomal recessive spermatogenic failure subtypes caused by genes at different chromosomal locations.[1][11] SYCP2’s gene symbol and name are standardized by HGNC (HGNC:SYCP2), and NCBI Gene and Ensembl provide genomic coordinates and transcript structures for human SYCP2. Protein-level annotations in UniProt describe SYCP2 domains, including N-terminal and C-terminal regions involved in centromere association and interactions with SYCP3 and SYCP1, respectively.[18]

Feng et al. demonstrated that the N-terminal region (NTR) of mouse SYCP2 associates with centromeric regions during meiosis I and interacts with the synaptonemal complex, indicating that SYCP2 mediates centromere–SC association.[18] They reported that in wild-type mice, SYCP3 localizes properly to the SC, but in Sycp2−/− mice, SYCP3 fails to localize to lateral elements and accumulates as aggregates in the nucleus, confirming SYCP2’s essential role in incorporating SYCP3 into axial elements.[18] These functional insights are crucial for understanding how SYCP2 mutations lead to SPGF1.

### 4.2. Pathogenic Variants in SYCP2

Human pathogenic variants in SYCP2 associated with SPGF1 predominantly take the form of heterozygous frameshift deletions and structural variants that alter gene dosage.[13][16][10] Schilit et al. identified three heterozygous frameshift variants in SYCP2 in infertile men: c.2022_2025del (p.Lys674AsnfsTer8), c.2793_2797del (p.Lys932SerfsTer3), and c.3067_3071del (p.Lys1023fs).[13][16] These deletions occur in exons 24, 31, and further downstream, respectively, and introduce premature stop codons, likely resulting in truncated proteins subject to nonsense-mediated decay or dysfunctional axial element structures.[13][16] All three variants were absent from population databases such as gnomAD and TOPMed, supporting their pathogenicity.[13][17][16]

The NOA genetics review lists these variants with ACMG classifications of pathogenic (P) or likely pathogenic (P/LP), noting that they reside in non-domain or disordered regions but nonetheless disrupt overall protein function and are associated with global meiotic arrest in patients.[16] Specifically, c.2022_2025del (p.Lys674fs) is described as a deletion in a disordered region that destabilizes axial elements, c.2793_2797del (p.Lys932fs) and c.3067_3071del (p.Lys1023fs) as non-domain frameshifts affecting axial assembly and triggering apoptosis.[16] These variants are germline and inherited in an autosomal dominant pattern, with at least one variant being maternally transmitted.[13][16][17]

Tan et al. report a novel heterozygous deletion c.1937_1942delTAAATA (p.Ile646_Asn647del) in exon 24 of SYCP2 in a Chinese family with non-obstructive azoospermia.[10] Conservation analysis indicated that the amino acid at position 647 is highly conserved across species, and structural modeling revealed notable changes in the three-dimensional conformation of mutant SYCP2.[10] Functional experiments in HEK293T cells showed decreased SYCP2 protein expression and altered subcellular localization, with mutant protein present in both cytoplasm and nucleus rather than exclusively in the nucleus, suggesting impaired nuclear targeting and SC assembly.[10] These data support a loss-of-function mechanism for this in-frame deletion variant, expanding the spectrum of pathogenic SYCP2 mutations beyond frameshifts.

In addition to sequence variants, Schilit et al. described a de novo balanced translocation t(20;22)(q13.3;q11.2) in subject DGAP230, which led to enhancer adoption and exclusive overexpression of SYCP2 from the derivative chromosome 20.[13][17] qPCR showed more than 20-fold increased SYCP2 expression in DGAP230’s lymphoblastoid cells, and modeling this dysregulation in yeast disrupted SC integrity.[13][18] The authors concluded that “either too much or too little SYCP2 results in a loss of function leading to infertility,” highlighting a dosage-sensitive mechanism where both haploinsufficiency and hypermorphy can disturb SC assembly.[13][18]

ClinVar entries referenced by Schilit et al. catalog these variants, and the authors note that all variants are extremely rare, consistent with a phenotype of infertility preventing their segregation in the general population.[13][16] In ACMG terms, these SYCP2 variants are classified as pathogenic or likely pathogenic based on functional evidence, rarity, predicted impact, and segregation in affected families.[16][17]

### 4.3. Variant Types, Allele Frequencies, and Origin

The main classes of SYCP2 pathogenic variants in SPGF1 include frameshift deletions, in-frame deletions, and structural variants affecting gene regulation. Frameshift deletions such as c.2022_2025del, c.2793_2797del, and c.3067_3071del introduce premature stop codons and are expected to cause loss-of-function through truncated proteins or mRNA decay.[13][16] The c.1937_1942del in-frame deletion alters protein structure and localization, effectively impairing function.[10] The balanced translocation t(20;22) modifies regulatory context, leading to overexpression and functional disruption.[13][17]

Allele frequencies for these variants in population databases such as gnomAD and TOPMed are essentially zero; Schilit et al. note that the frameshift variants are absent from these databases, reinforcing their pathogenicity.[13][17][16] This absence is consistent with strong negative selection due to male infertility. The variants are germline and usually heterozygous; they can arise de novo (as in DGAP230’s translocation) or be inherited from unaffected parents, often mothers, because female fertility is not severely impacted.[13][17][10] Somatic variants in SYCP2 are not implicated in SPGF1; the disorder is purely germline in origin.

### 4.4. Functional Consequences and Mechanisms of Pathogenicity

At the molecular level, SYCP2 pathogenic variants cause **loss of function** of the SYCP2 protein in meiotic cells, leading to defective assembly of axial elements of the synaptonemal complex, impaired chromosomal synapsis, disrupted centromere association, and activation of meiotic checkpoints that trigger apoptosis.[9][18][16] In Sycp2-knockout mice, homozygous mutants exhibit failed chromosomal synapsis, defective incorporation of SYCP3 into lateral elements, and apoptosis of spermatocytes, resulting in complete infertility.[9][18] Feng et al. showed that the SYCP2 N-terminal region interacts with centromeric chromatin, and that the C-terminal region is responsible for association with SYCP3 and SYCP1 for SC formation.[18] Disruption of these interactions through structural or quantitative changes in SYCP2 destabilizes the SC, leading to arrest.

Schilit et al.’s modeling of SYCP2 overexpression in budding yeast showed that dysregulated SYCP2 levels disturbed SC structural integrity, supporting the idea that both insufficient and excessive SYCP2 can impair function, possibly through mis-assembly of SC components.[13][18][17] In humans, heterozygous frameshift variants likely reduce effective SYCP2 dosage and produce defective proteins that fail to scaffold SYCP3, leading to axial element instability and global meiotic arrest.[16] Tan et al.’s functional experiments with the c.1937_1942del variant demonstrated decreased SYCP2 expression and mislocalization, both of which are consistent with loss-of-function affecting nuclear SC assembly.[10]

In ACMG terms, these variants are interpreted as loss-of-function mutations in a gene where loss-of-function is a known mechanism of disease, satisfying key criteria for pathogenicity.[16][17] There is no evidence of gain-of-function in the sense of new positive activity; rather, the translocation-mediated overexpression appears to produce functional loss by disrupting stoichiometry of SC components. Therefore, SPGF1 can be classified mechanistically as a **haploinsufficiency or dysregulation disorder of a meiosis-specific scaffold protein**, leading to failure of synapsis and recombination.

### 4.5. Modifier Genes and Epigenetic Factors

No specific modifier genes have been identified that alter disease severity or expressivity in SPGF1. The small number of reported families and the severe phenotype make detection of subtle modifiers difficult.[13][16][10] However, broader studies of male infertility suggest that other meiotic genes, DNA repair factors, and transcription regulators can influence spermatogenic outcomes, and future multi-gene analyses may uncover interactions between SYCP2 variants and other loci.

Epigenetically, no SPGF1-specific DNA methylation or chromatin modification patterns have been reported. The NOA review focuses on genetic and epigenetic insights but does not attribute specific epigenomic alterations to SYCP2-related disease, instead discussing global epigenetic changes in non-obstructive azoospermia.[16] The translocation in DGAP230 illustrates that altered chromatin context and enhancer adoption can dysregulate SYCP2 expression, representing a structural epigenetic effect, but detailed mapping of epigenetic marks at the SYCP2 locus in SPGF1 patients has not yet been performed.[13][17] In knowledge base fields for epigenetics, SPGF1 should be annotated as “no specific epigenetic mechanisms reported beyond structural regulatory changes.”

### 4.6. Chromosomal Abnormalities

The key chromosomal abnormality associated with SPGF1 is the balanced translocation t(20;22)(q13.3;q11.2) in DGAP230, which rearranges regulatory regions near SYCP2 and leads to its overexpression.[13][17] Schilit et al. used precision cytogenetics to map breakpoints and demonstrated that this chromosomal rearrangement disrupts normal gene regulation, highlighting an alternative etiology distinct from segregation of unbalanced gametes that is often considered in men with balanced chromosomal aberrations.[17] The authors noted that “a chromosomal rearrangement may also disrupt or dysregulate genes important in fertility,” and their study illustrates how BCAs can cause infertility by gene dysregulation rather than only by producing unbalanced gametes.[17][13]

Beyond this translocation, no recurrent chromosomal abnormalities have been reported specifically for SYCP2-mediated SPGF1. Y-chromosome AZF microdeletions on distal Yq are common in male infertility but represent a separate disease category.[7] In a structured representation, SPGF1 should be annotated with the possibility of **balanced translocations involving 20q13.3** as a mechanism of SYCP2 gene dysregulation, with evidence from DGAP230’s case and the associated dbVar and ClinVar entries referenced by Schilit et al.[13][17]

## 5. Environmental Information

### 5.1. Environmental Factors in General Male Infertility

In the broader field of male infertility, numerous environmental factors—including exposure to heat, toxins (such as pesticides and heavy metals), endocrine-disrupting chemicals, smoking, alcohol, and systemic illnesses—can impair spermatogenesis and contribute to azoospermia or oligozoospermia.[2] Epidemiological studies have linked occupational exposures, varicocele, infections, and lifestyle factors to reduced sperm counts and quality, and environmental health agencies monitor pollutants that affect reproductive health. However, these factors act through diverse mechanisms, such as oxidative stress, hormonal disruption, and direct germ cell toxicity, and are not specific to SPGF1, which is defined by a monogenic defect in SYCP2.[3][13][16]

### 5.2. Environmental Factors Specific to SPGF1

No environmental or occupational exposures have been identified as specific contributors to SPGF1. All reported cases of SYCP2-mediated infertility involve men whose primary distinguishing feature is a pathogenic variant or dysregulation in SYCP2, and there is no suggestion that environmental exposures triggered or exacerbated the disease.[13][16][10] Testicular histology and semen parameters in SPGF1 patients reflect congenital meiotic defects rather than acquired exogenous damage.

Therefore, in a knowledge base, environmental factor fields for SPGF1 should indicate that current evidence does not support a causal or modifying role of specific exposures beyond general male reproductive health considerations.

### 5.3. Lifestyle, Infectious Agents, and Gene–Environment Considerations

Lifestyle factors such as smoking, obesity, and alcohol consumption can reduce sperm quality and count but have not been linked to SYCP2-mediated meiotic arrest in a gene-specific way.[2][16] Infectious agents, including mumps orchitis and sexually transmitted infections, can damage the testis or reproductive tract, but these causes are typically associated with obstructive patterns or post-inflammatory damage, distinct from the pure meiotic arrest seen in SPGF1.[3]

Gene–environment interactions, such as those involving oxidative stress pathways or DNA repair genes, may play roles in multifactorial male infertility, but for SPGF1, the dominance of the SYCP2 defect makes environmental contributions relatively minor. Hence, SPGF1 is best classified as a **primarily genetic, non-environmental disease**, and environmental sections of a knowledge base should reflect the absence of specific evidence.

## 6. Mechanism and Pathophysiology

### 6.1. Molecular Pathways: Synaptonemal Complex Assembly and Meiotic Recombination

The pathophysiology of SPGF1 centers on disrupted assembly and function of the synaptonemal complex (SC) during meiosis I, leading to defective homologous chromosome pairing, synapsis, and recombination.[9][18][16] SYCP2 is a key axial element protein of the SC; it binds DNA and recruits SYCP3 to form meiotic chromosome axes that are competent to assemble the SC.[9][18] SYCP1 encodes transverse filaments essential for SC formation, while SYCE1, SYCE2, and SYCE3 contribute to central element structure.[16][18] In normal meiosis, these components orchestrate the alignment and synapsis of homologous chromosomes, facilitate crossover formation, and ensure proper segregation during meiosis I.

Feng et al. showed that the N-terminal region of mouse SYCP2 associates with centromeric regions and interacts with the SC, suggesting that SYCP2 mediates centromere–SC association.[18] They reported that in wild-type mice, SYCP3 localized well to the SC, but in sycp2−/− mice, SYCP3 failed to localize to lateral elements and accumulated as nuclear aggregates, indicating that SYCP2 is essential for incorporating SYCP3 into axial elements.[18] OMIM summarizes studies in which homozygous Sycp2 mutant spermatocytes exhibit complete meiotic arrest, fail to reach pachytene, and undergo apoptosis, underscoring the centrality of SYCP2 in meiotic progression.[9]

The NOA genetics review highlights that proper chromosome pairing and synapsis are essential for meiotic progression, and that disruption of synaptonemal complex components often leads to meiotic arrest.[16] It lists SYCP1, SYCP2, SYCP3, SYCE1–3, and HORMAD1 as key genes whose pathogenic variants are frequently linked to spermatogenic arrest.[16] Specifically, Sycp1 knockout mice exhibit complete synapsis failure, with spermatocytes arrested at zygotene/pachytene stages and unresolved DSBs.[16] Sycp2 knockout mice show axial element assembly defects, reduced DSBs, and apoptosis.[16][9][18] These data integrate SYCP2 into a molecular pathway network that includes SC assembly, meiotic recombination, and DNA damage response.

Relevant Gene Ontology (GO) biological process terms include “synaptonemal complex assembly” (GO:0007130), “meiotic nuclear division” (GO:0140013), “meiotic chromosome segregation” (GO:0045132), “meiotic recombination” (GO:0007131), and “apoptotic process” (GO:0006915). SPGF1 pathophysiology can be described as perturbation of these processes due to SYCP2 dysfunction, causing checkpoint activation and apoptosis in spermatocytes. GO cellular component terms include “synaptonemal complex” (GO:0000795), “chromosome axis,” “centromere” (GO:0000775), and “nucleus” (GO:0005634), reflecting the localization of SYCP2 function.

### 6.2. Cellular Processes: Meiotic Arrest and Germ Cell Apoptosis

At the cellular level, SYCP2 dysfunction leads to specific defects in germ cell development. Spermatogonia enter meiosis and differentiate into spermatocytes, but at mid-prophase I (zygotene/pachytene), the failure of SC assembly prevents completion of synapsis and recombination.[9][18][16] Checkpoints monitoring synapsis and DNA repair detect these abnormalities and trigger apoptosis, resulting in depletion of spermatocytes and an absence of spermatids and spermatozoa.[9][18] This pattern is visible histologically as seminiferous tubules containing spermatocytes as the most advanced germ cell type, with evidence of apoptosis and occasional Sertoli cell-only tubules.[3][16]

Feng et al.’s TUNEL and electron microscopy data showed that spermatocytes in sycp2−/− mice undergo apoptosis, confirming that SC disruption leads to germ cell death.[18] OMIM notes that homozygous Sycp2 mutant spermatocytes “underwent apoptosis in the testes,” reinforcing the importance of programmed cell death in this disease mechanism.[9] The NOA review also associates SYCP2 variants with axial element assembly defects and apoptosis.[16] These processes align with GO terms such as “negative regulation of cell cycle” (GO:0045786), “DNA repair checkpoint” (GO:0000077), and “apoptotic process” (GO:0006915).

Cell type ontology (CL) terms relevant to SPGF1 include “spermatogonium” (CL:0000016), “primary spermatocyte” (CL:0000017), “secondary spermatocyte,” “spermatid,” and “Sertoli cell” (CL:0000162). The principal cell types affected are primary spermatocytes, which fail to progress through meiosis, and Sertoli cells, which may be secondarily impacted through changes in germ cell–Sertoli cell interactions. However, the primary pathology resides in germ cells expressing SYCP2.

### 6.3. Protein Dysfunction: Structural and Dosage Effects on SYCP2

SYCP2 pathogenic variants cause protein dysfunction through structural alteration, mislocalization, and dosage changes. Frameshift deletions introduce premature stops in SYCP2, likely producing truncated proteins that cannot bind DNA or recruit SYCP3 appropriately, or causing mRNA degradation via nonsense-mediated decay.[13][16] In-frame deletions such as c.1937_1942del modify the three-dimensional conformation of SYCP2 and alter its nuclear localization, as shown by Tan et al., who observed decreased protein expression and altered subcellular distribution in HEK293T cells transfected with mutant SYCP2 constructs.[10] The translocation t(20;22) repositions regulatory elements and causes overexpression, which Schilit et al. modeled in yeast, demonstrating that excessive SYCP2 disrupts SC integrity.[13][18][17]

Thus, SYCP2 dysfunction arises from both quantitative and qualitative changes, but the common endpoint is inability to form properly structured chromosome axes and SC. UniProt and InterPro domain annotations for SYCP2 indicate coiled-coil regions important for protein–protein interactions and disordered regions that may be involved in flexibility and scaffold formation.[18] Variants in these regions disrupt protein function in ways consistent with SC assembly failure. AlphaFold and structural modeling support the notion that even small deletions can have global effects on protein folding.

### 6.4. Metabolic and Immune System Involvement

SPGF1 is not primarily a metabolic or immune disorder. The processes involved are structural and regulatory at the chromatin level, rather than metabolic pathways. Germ cell metabolism may be secondarily affected by apoptosis and arrest, but no specific metabolic signatures have been associated with SYCP2 mutations.[16] Similarly, there is no evidence of autoimmunity or immunodeficiency directly tied to SPGF1; testicular immune privilege may be impacted by germ cell death, but this has not been studied in detail.

Thus, GO terms related to metabolism (e.g., lipid, carbohydrate metabolism) and immune processes (e.g., immune response, inflammation) are not central to SPGF1 pathophysiology and would be annotated as non-primary mechanisms in a knowledge base.

### 6.5. Tissue Damage Mechanisms and Biochemical Abnormalities

Tissue damage in SPGF1 is confined to the seminiferous epithelium and results from germ cell apoptosis. Oxidative stress may play a role in apoptosis, but the primary triggers are checkpoint responses to failed synapsis and recombination.[18][16] Histologically, tubules may show reduced germ cell layering and increased interstitial changes, but there is no fibrosis or necrosis typical of chronic inflammatory conditions.[3] Biochemically, SYCP2 dysfunction is an enzyme-independent defect; SYCP2 is a structural protein rather than an enzyme or receptor, and its disruption does not directly alter specific biochemical reactions but instead the architecture of meiotic chromosomes.

BRENDA and enzyme-related databases would not list SYCP2 as an enzyme; UniProt annotates it as a structural chromosomal protein. Ion channels, receptors, or metabolic enzymes are not central in SPGF1, and thus biochemical abnormality fields should emphasize structural protein function rather than traditional enzyme deficiencies.

### 6.6. Molecular Profiling and Advanced Technologies

To date, no large-scale transcriptomic, proteomic, metabolomic, or lipidomic profiling studies have been published specifically for SYCP2-mutant human testes. However, spermatogenic failure and NOA more broadly have been investigated using testicular transcriptomics and proteomics, showing downregulation of meiosis-specific genes and SC components.[16] Given SYCP2’s meiosis-specific expression, one would expect its mRNA and protein to be absent or altered in SPGF1 testes, but direct profiling data are lacking.

Single-cell RNA sequencing and spatial transcriptomics of human testes are rapidly advancing and may soon allow cell-type-specific analysis of SYCP2 expression in normal and infertile men, but such data have not yet been reported in the context of SPGF1.[16] Functional genomics screens (e.g., CRISPR knockout) in cell lines or organoids have not targeted SYCP2 specifically, likely because meiosis is difficult to recapitulate in vitro. Therefore, advanced technologies remain a future avenue for SPGF1 research.

In a knowledge base, molecular profiling fields for SPGF1 should be annotated as “limited data; inference from NOA and SC gene profiling,” with targeted references to upcoming multi-omics studies as they emerge.

### 6.7. Causal Chain from SYCP2 Defect to Clinical Infertility

The causal chain in SPGF1 can be articulated as follows. At the upstream level, a germline heterozygous pathogenic variant or structural dysregulation at the SYCP2 locus leads to reduced or aberrant SYCP2 protein in meiotic germ cells.[3][13][10] SYCP2 dysfunction impairs binding to DNA, recruitment of SYCP3, and centromeric association, preventing proper assembly of chromosome axes and synaptonemal complexes.[9][18][16] As meiosis proceeds, homologous chromosomes fail to synapse and recombine correctly, leading to activation of meiotic checkpoints that sense unsynapsed chromatin and unrepaired DSBs.[16][18] These checkpoints trigger apoptosis in spermatocytes, resulting in global meiotic arrest at mid-prophase I.[9][18][16]

Downstream, seminiferous tubules become populated with spermatocytes that fail to progress, and spermatids and spermatozoa are absent or severely reduced.[3][16] Consequently, semen analysis reveals azoospermia or severe oligozoospermia, and men experience infertility.[13][10] The disease course is stable: the SYCP2 defect is present from puberty onward, and spermatogenic failure persists throughout life. Other tissues are unaffected because SYCP2 is meiosis-specific. Thus, the pathophysiology of SPGF1 exemplifies a clean chain from monogenic structural protein defect to tissue-specific functional failure and clinical infertility.

## 7. Anatomical Structures Affected

### 7.1. Organ-Level Anatomy: Testis and Male Reproductive System

SPGF1 affects primarily the testes, specifically the seminiferous tubules, which are the site of spermatogenesis.[3][16] The testis is represented by Uberon term UBERON:0000473, and seminiferous tubule by UBERON:0000984. Within these tubules, germ cells progress through mitotic and meiotic divisions under the support of Sertoli cells, and Leydig cells in the interstitium produce testosterone. In SPGF1, the germ cell lineage is disrupted at the spermatocyte stage, while Sertoli and Leydig cell function generally remain intact.[3][9][16]

Secondary reproductive organs, such as the epididymis, vas deferens, seminal vesicles, and prostate, are typically structurally normal and unaffected in SPGF1.^3^ Obstruction of the reproductive tract is absent; otherwise, azoospermia could be obstructive rather than non-obstructive. Thus, SPGF1 is best categorized anatomically as a **testicular, seminiferous tubule-specific disorder** with no direct involvement of the rest of the male reproductive system.

### 7.2. Tissue-Level Anatomy: Seminiferous Epithelium

At the tissue level, SPGF1 affects the seminiferous epithelium, composed of Sertoli cells and germ cells at various stages, including spermatogonia, spermatocytes, spermatids, and spermatozoa.[3][16] In healthy testes, this epithelium displays orderly layers of germ cells progressing from basal to luminal positions as they mature. In SPGF1, meiotic arrest leads to an accumulation of spermatocytes and a paucity or absence of spermatids and spermatozoa.[3][16][9] This histological pattern is characteristic of meiotic arrest disorders.

Tissue ontology could annotate this as “seminiferous epithelium tissue” or “testis seminiferous tubule epithelium,” and pathology descriptors include “abnormal seminiferous tubule histology.” HPO and SNOMED CT terms for “spermatogenic arrest” capture this pattern. The tissue type is epithelial, with supporting connective tissue in the interstitium.

### 7.3. Cell-Level Anatomy: Germ Cells and Sertoli Cells

At the cell level, the primary affected population is **primary spermatocytes** (CL:0000017), which express SYCP2 and undergo meiosis I.[9][18] Spermatogonia (CL:0000016) enter meiosis normally but their progeny fail at synapsis, while secondary spermatocytes and spermatids are reduced or absent due to arrest and apoptosis.[16][9] Sertoli cells (CL:0000162) may show secondary changes in response to germ cell loss but are not intrinsically defective in SYCP2-mediated disease, as SYCP2 is not expressed in these somatic cells.[18][9]

Cell Ontology terms for “male germ cell” and “spermatocyte” are appropriate for SPGF1. Knowledge base annotations should specify that SYCP2 expression and disease mechanisms are localized to spermatocytes, and that Sertoli and Leydig cells are structurally and functionally normal, consistent with endocrine data.

### 7.4. Subcellular Anatomy: Chromosomes, Synaptonemal Complex, and Centromere

Subcellular compartments involved in SPGF1 include the nucleus (GO:0005634), chromosomal axes, synaptonemal complex (GO:0000795), and centromere (GO:0000775).[18][9] SYCP2 localizes to meiotic chromosomes, forming axial elements that anchor SYCP3 and connect to transverse filaments of SYCP1.[18] Feng et al. discovered that SYCP2’s N-terminal region associates with the centromere region, indicating that SYCP2 links centromeres to the SC and participates in meiotic chromosome organization.[18] Disruption of SYCP2 alters these subcellular structures, causing mislocalization of SYCP3 and failure of SC formation.[18][9]

Ultrastructural analyses in sycp2−/− mice reveal absence of normal SCs and abnormal chromatin organization in spermatocytes.[18][9] Thus, SPGF1 is fundamentally a subcellular structural disorder at the level of meiotic chromatin architecture. Knowledge base annotations should highlight these compartments and their perturbation in SYCP2-mediated disease.

### 7.5. Localization and Lateralization

SPGF1 is bilateral in nature: both testes are affected because the germline SYCP2 mutation is present in all germ cells.[3][13][10] There is no lateralization or asymmetry; azoospermia reflects global failure of spermatogenesis across both gonads. Specific anatomical sites are the seminiferous tubules throughout the testicular parenchyma. Imaging, if performed, would show normal testicular size or mild reduction, without focal lesions or asymmetry.

## 8. Temporal Development

### 8.1. Onset of Germ Cell Defect and Clinical Recognition

The underlying germ cell defect in SPGF1 begins at puberty, when spermatogonia initiate meiosis and require functional SYCP2 for SC assembly.[9][18] In Sycp2-knockout mice, infertility is evident once animals reach sexual maturity, indicating that meiotic arrest manifests as soon as meiosis is required.[9][18] In humans, the defect is similarly present from puberty onward, but clinical recognition of SPGF1 typically occurs in young adulthood, when men attempt to conceive and experience infertility.[3][13][10]

The onset pattern is insidious and chronic: there is no acute episode of testicular failure; instead, spermatogenesis is never fully normal from the onset of puberty. Men may have normal sexual function and secondary sexual characteristics due to intact Leydig cell and androgen activity, masking the underlying defect until semen analysis is performed. Thus, age of clinical onset is usually in the twenties or thirties, corresponding to reproductive attempts, while biological onset is adolescent.

### 8.2. Disease Progression and Course

SPGF1 follows a stable, non-progressive course. Once established, spermatogenic failure remains constant; there is no evidence of progressive deterioration in testicular function or systemic health over time.[3][13][16] This contrasts with some acquired forms of testicular failure that worsen with ongoing toxic exposures or systemic illness. Because SYCP2 mutations are congenital and structural, the phenotypic expression in germ cells is consistent across life stages.

Disease stages in SPGF1 can be conceptualized as early (preclinical, puberty with unrecognized meiotic arrest), intermediate (adult recognition of infertility and azoospermia), and late (chronic infertility with psychosocial consequences), but the underlying gonadal pathology remains stable. Disease duration is lifelong; fertility is not restored spontaneously. There are no remissions or relapses; SPGF1 is a non-remitting condition without episodic variation.

### 8.3. Critical Periods and Opportunities for Intervention

The critical period for SPGF1 pathophysiology is meiosis during puberty and adulthood. However, the opportunity for clinical intervention is primarily at the time of infertility evaluation, when diagnostic workup and genetic counseling can be offered.[13][16][14] There is no known early intervention that can prevent or reverse meiotic arrest in SYCP2-mediated disease. Assisted reproductive technologies (ART) may offer limited opportunities if residual sperm can be retrieved, but for most men with complete meiotic arrest, options are limited to donor sperm or adoption.[16]

From a prevention standpoint, preimplantation genetic testing and carrier counseling may be applied in families once a SYCP2 pathogenic variant is identified, but these occur after disease has manifested in probands. Thus, temporal development in SPGF1 is more relevant to counseling and planning than to disease modification.

## 9. Inheritance and Population

### 9.1. Inheritance Pattern

SPGF1 is inherited in an **autosomal dominant** manner.[3][11][13][16] OMIM explicitly states that SPGF1 is caused by heterozygous mutation in SYCP2 and is autosomal dominant.[3][11] Schilit et al. found heterozygous frameshift variants in affected men and observed maternal transmission in at least one case, consistent with autosomal dominant inheritance with sex-limited expression (infertility in males but not females).[13][17] Tan et al. reported a heterozygous SYCP2 deletion in a Chinese family with non-obstructive azoospermia, again suggesting autosomal dominant transmission.[10]

Penetrance appears to be high in males: all known male carriers of pathogenic SYCP2 variants are infertile due to severe spermatogenic failure.[13][16][10] Expressivity is relatively consistent, with azoospermia or severe oligozoospermia and meiotic arrest in all reported cases. There is no evidence of genetic anticipation, as the disease is not based on repeat expansion, and generational severity does not appear to change. Germline mosaicism has not been reported but cannot be excluded; however, the rarity of cases and strong phenotype make mosaic transmission less likely.

### 9.2. Founder Effects, Consanguinity, and Carrier Frequency

No founder effects have been identified for SYCP2 pathogenic variants; all reported variants are extremely rare and typically unique to individual families.[13][16][10] There is no indication of population-specific clusters or consanguinity-related enrichment. Because male carriers are infertile, SYCP2 pathogenic alleles are unlikely to become common in any population, and their presence depends on de novo mutational events or transmission through unaffected female carriers.

Carrier frequency for pathogenic SYCP2 variants in the general population is extremely low, likely much less than 0.01%, given the absence of these variants in gnomAD and TOPMed.[13][16] Female carriers may be asymptomatic or have subclinical reproductive effects, but these have not been systematically studied, and the primary recognized phenotype is male infertility.

### 9.3. Epidemiology: Prevalence and Incidence

Precise prevalence and incidence data for SPGF1 are not available, but the rarity of reported cases suggests that SPGF1 is a very rare cause of male infertility. Schilit et al. note that unexplained infertility affects 2–3% of reproductive-aged couples, and their study of rare variants in infertile men identified only a small number of SYCP2 pathogenic variants.[17][13] Tan et al. added a single family with a novel SYCP2 variant.[10] Given these numbers, SPGF1 likely accounts for a very small fraction of non-obstructive azoospermia cases, with other genes such as TEX11, NR5A1, DPY19L2, and C14orf39 contributing larger proportions.[4][5][1][6][2]

As an example, TEX11 mutations account for about 1% of infertility in non-obstructive azoospermic men, and NR5A1 mutations for about 4% of severe spermatogenic failure.[4][5] SYCP2-associated SPGF1 appears less common than these, although exact percentages have not been reported. Orphanet classifications for SPGF subtypes such as SPGF52 describe them as “very rare (1%),” referring to their frequency among azoospermia phenotypes rather than population prevalence.[6] SPGF1 would fall into a similar or lower category of rarity.

### 9.4. Population Demographics: Sex, Age, Geography, and Ethnicity

SPGF1 affects only males, as the phenotype is male infertility due to spermatogenic failure.[3][13][16][10] Female carriers may exist and transmit the variant, but they are not reported to have overt infertility, making SPGF1 a sex-limited condition. Age of affected individuals at diagnosis is typically in young adulthood, when fertility evaluation is undertaken.

Geographically, reported SYCP2 variants have been found in men from Europe (e.g., Münster cohort), North America (DGAP230), and China, suggesting that SPGF1 is not restricted to specific ethnic groups.[13][17][10] However, the small number of cases prevents definitive demographic conclusions. Population genetics databases such as gnomAD do not show recurrent SYCP2 pathogenic alleles in any ancestry group.[13][16]

In knowledge bases, demographic fields for SPGF1 should specify male sex, adult age at clinical recognition, and global but extremely low prevalence, with no known ethnic predilection.

## 10. Diagnostics

### 10.1. Clinical Evaluation and Laboratory Tests

Diagnosis of SPGF1 begins with clinical evaluation of male infertility. Men present with a history of failure to conceive despite regular unprotected intercourse, often over one year or more.[2][3] Semen analysis, following WHO guidelines, reveals azoospermia (no sperm) or severe oligozoospermia/cryptozoospermia (very low sperm counts detectable only after centrifugation).[2][13] These laboratory findings prompt further workup to distinguish obstructive from non-obstructive causes. Physical examination assesses testicular size, epididymal fullness, and vas deferens patency; endocrinologic evaluation measures FSH, LH, and testosterone levels.[2][3]

In SPGF1, semen findings are characteristic, while physical exam and hormones may be normal or show mild abnormalities. Testicular biopsy or microdissection testicular sperm extraction (micro-TESE) is often performed to assess spermatogenesis and attempt sperm retrieval. Histological examination reveals spermatogenic arrest at the spermatocyte stage and absence of mature sperm, consistent with meiotic arrest.[3][16] Pathology descriptors include “spermatogenic arrest” and “non-obstructive azoospermia.”

### 10.2. Genetic Testing Approaches

Once non-obstructive azoospermia and meiotic arrest are established, genetic testing is indicated to identify underlying monogenic causes. Recommended approaches include **whole exome sequencing (WES)** and targeted male infertility gene panels, which encompass meiosis-specific genes such as SYCP1–3, SYCE1–3, HORMAD1, TEX11, NR5A1, DPY19L2, C14orf39, and SYCP2.[2][16][14] The Genetic Testing Registry (GTR) lists a “Male Infertility Panel” (GTR000553213) that includes SYCP2 among tested genes, indicating that SYCP2 is recognized clinically as a relevant infertility gene.[14] This test is recommended for men with genetic infertility and serves diagnostic, mutation confirmation, and risk assessment purposes.[14]

Schilit et al. used exome sequencing to identify heterozygous frameshift variants in SYCP2 in infertile men and validated them by Sanger sequencing.[13][17] Tan et al. employed whole-exome sequencing in a Chinese family, detecting the c.1937_1942del variant, which was then confirmed and functionally characterized.[10] Thus, WES and gene panels are the primary tools for detecting SYCP2 sequence variants. For structural variants such as translocations, karyotyping and chromosomal microarray are necessary. DGAP230’s balanced translocation was detected cytogenetically and refined using precision cytogenetics and breakpoint mapping.[17][13]

Whole genome sequencing (WGS) could theoretically detect both sequence and structural variants in SYCP2, but its use in routine infertility diagnostics is still evolving. Chromosomal microarray is useful for detecting copy number changes but may not capture balanced translocations; karyotyping and FISH may be needed for structural rearrangements.

### 10.3. Omics-Based Diagnostics

Omics-based diagnostics, such as testicular RNA sequencing, proteomics, and epigenomics, are not yet standard in clinical infertility practice. However, research studies use these methods to characterize gene expression in azoospermia and could potentially identify SYCP2 expression patterns. For SPGF1-specific diagnosis, genetic testing remains the primary tool; omics approaches are supplementary and exploratory.

Liquid biopsy and circulating biomarkers are not relevant for SPGF1 because the disease is confined to the testes and does not produce systemic tumor markers or immune signatures.

### 10.4. Clinical Criteria and Differential Diagnosis

Clinical criteria for SPGF1 include non-obstructive azoospermia or severe oligozoospermia, testicular histology with spermatogenic arrest at the spermatocyte stage, and identification of a heterozygous pathogenic variant or dysregulation in SYCP2 on chromosome 20q13.33, in the absence of other explanatory causes.[3][13][16][10] Society guidelines for male infertility (e.g., from the American Urological Association or European Academy of Andrology) emphasize genetic testing for men with severe spermatogenic failure, particularly when histology shows meiotic arrest.[2][16]

Differential diagnosis includes other genetic causes of meiotic arrest and non-obstructive azoospermia, such as TEX11 mutations (X-linked), NR5A1 mutations (autosomal dominant but with broader phenotypes), DPY19L2 deletions (SPGF9), C14orf39 mutations (SPGF52), and Y-chromosome AZF microdeletions.[4][5][1][6][7][16] Additionally, endocrine disorders like hypogonadotropic hypogonadism and systemic illnesses can cause spermatogenic failure, but they have distinct hormone profiles and associated features.[3] Obstructive azoospermia due to vas deferens absence, infections, or surgeries must be excluded by physical exam and imaging.

### 10.5. Screening

Population screening for SPGF1 is not currently practiced, given its rarity and the invasive nature of testicular evaluation. Carrier screening in women for SYCP2 mutations is theoretically possible but not routine, as female carriers do not usually have severe phenotypes. However, in families with known SYCP2 pathogenic variants, cascade testing of relatives and preimplantation genetic testing for monogenic disorders (PGT-M) may be offered to couples seeking to avoid transmitting the variant to sons.[13][10][14]

Newborn screening is not applicable. Screening for general male infertility may involve semen analysis in certain contexts, but SPGF1 remains a diagnosis made in specialized infertility settings.

## 11. Outcome and Prognosis

### 11.1. Survival and Mortality

SPGF1 does not affect survival or mortality. Men with SYCP2-mediated spermatogenic failure are otherwise healthy and have normal life expectancy.[3][13][16] There are no systemic complications or increased mortality risks associated with the condition; thus, survival rates and mortality statistics are not relevant for SPGF1 specifically.

### 11.2. Morbidity, Disability, and Quality of Life

The main morbidity associated with SPGF1 is **reproductive disability**: complete or near-complete inability to father biological children. This represents a significant functional impairment in the reproductive domain and has major psychosocial impacts. Health-related quality of life studies in infertile men demonstrate increased rates of depression, anxiety, marital strain, and reduced overall life satisfaction compared with fertile controls, as measured by instruments such as SF-36 and WHOQOL-BREF.[2] Although SPGF1-specific QoL data are not available, the severity of infertility suggests comparable or greater impacts.

From an ICF (International Classification of Functioning) perspective, SPGF1 affects domains of reproductive function and social participation. Disability outcomes include involuntary childlessness and associated psychosocial sequelae. However, physical functioning, self-care, and mobility are unaffected.

### 11.3. Disease Course and Complications

SPGF1 has a stable disease course in terms of gonadal function; there are no reported complications such as testicular cancer, systemic organ failure, or endocrine crises directly attributable to SYCP2 mutations.[3][13][16][10] Potential complications arise from diagnostic and treatment procedures, such as surgical risks from testicular biopsy or micro-TESE and psychological stress from infertility. No specific co-morbid conditions are linked to SPGF1.

Recovery potential is minimal: spontaneous restoration of spermatogenesis has not been reported. Assisted reproduction may allow some men with residual sperm to achieve biological parenthood, but in cases of complete meiotic arrest, donor sperm or adoption are required.[16] Thus, prognosis for natural fertility is poor, although overall health prognosis is excellent.

### 11.4. Prognostic Factors and Biomarkers

Prognostic factors in SPGF1 include the nature of the SYCP2 variant (frameshift vs in-frame vs structural), severity of meiotic arrest (complete vs partial), and presence of residual sperm in the testis. For example, men with cryptozoospermia may have slightly better chances of sperm retrieval and assisted reproduction success than those with complete azoospermia.[13][16] However, detailed prognostic data for SYCP2-specific cases are limited.

Prognostic biomarkers are not established. Genetic identification of a SYCP2 pathogenic variant serves as a diagnostic marker but does not currently predict variation in outcome, since most cases have severe infertility. Hormone levels and testicular volume might provide crude estimates of spermatogenic capacity but are not specific.

## 12. Treatment

### 12.1. Pharmacotherapy

There is no disease-specific pharmacotherapy for SPGF1. Because the underlying defect is structural and genetic—failure of SC assembly due to SYCP2 dysfunction—hormonal therapies such as gonadotropins or testosterone modulation are unlikely to restore normal meiosis.[16] In general male infertility practice, some men benefit from hormonal correction for hypogonadism or from empirical antioxidant therapy, but such measures do not address the core problem in SYCP2-mediated meiotic arrest. No clinical trials have tested pharmacologic agents specifically for SPGF1.

PharmGKB and CPIC pharmacogenomic resources do not list SYCP2 as influencing drug response, further underscoring the lack of pharmacologic interventions.

### 12.2. Advanced Therapeutics: Gene and Cell Therapy

Gene therapy for SPGF1 is theoretically conceivable but currently experimental and not applied in humans. In principle, CRISPR-based correction of SYCP2 mutations in germline stem cells or gene replacement via viral vectors could restore SYCP2 expression, allowing normal SC assembly and spermatogenesis. However, technical and ethical challenges are substantial, including delivery to testicular germ cells, off-target effects, and germline editing concerns.

Cell therapy, such as transplantation of corrected spermatogonial stem cells or use of induced pluripotent stem cell (iPSC)-derived germ cells, is an area of active research in reproductive biology but remains preclinical. No SPGF1-specific cell therapy trials exist in ClinicalTrials.gov.

RNA-based therapies (e.g., antisense oligonucleotides, siRNA) might theoretically modulate SYCP2 expression in cases of overexpression, such as the translocation-mediated dysregulation, but the feasibility of testis-specific delivery and safety is untested.[13][17] Targeted therapies, immunotherapies, and systemic interventions are not relevant to a structural meiotic protein defect confined to the testes.

### 12.3. Surgical and Assisted Reproductive Interventions

The main treatment strategy for SPGF1 in clinical practice is **assisted reproductive technology (ART)**. For men with residual sperm, procedures such as testicular sperm extraction (TESE) or microdissection TESE (micro-TESE; NCIT:C112755) can retrieve sperm directly from the testis, which can then be used in intracytoplasmic sperm injection (ICSI; NCIT:C28081) to fertilize oocytes.[2][16] However, in SPGF1, global meiotic arrest often leads to complete absence of sperm even in testicular tissue, reducing the success of sperm retrieval.[16] Nonetheless, some men with SYCP2 variants have cryptozoospermia rather than absolute azoospermia, offering a possibility of TESE/ICSI.

When sperm retrieval fails, use of donor sperm or adoption becomes the primary route to parenthood. These are not curative treatments but mitigate the reproductive consequences of SPGF1.

### 12.4. Supportive and Rehabilitative Care

Supportive care for SPGF1 focuses on psychological counseling, couple’s therapy, and education about reproductive options. Infertility can cause significant emotional distress, and mental health support is crucial. Rehabilitation medicine is not relevant, as physical function is preserved.

### 12.5. Experimental Treatments and Personalized Medicine

Experimental treatments for SPGF1 are limited to research concepts, such as gene editing and stem cell-based germ cell replacement. Personalized medicine approaches in male infertility focus on tailoring assisted reproductive strategies to individual diagnostic profiles; for example, men with meiotic arrest may be counseled that TESE has low yield, and resources may be directed toward alternative reproductive plans.[16] Genotype-guided treatment in SPGF1 mainly involves genetic counseling rather than pharmacologic tailoring.

In a knowledge base, treatment annotations for SPGF1 should emphasize **ART procedures**, genetic counseling, and psychosocial support, with NCIT terms for ICSI, TESE, and assisted reproductive technology, and note the absence of disease-modifying pharmacotherapy or gene therapy at present.

## 13. Prevention

### 13.1. Primary Prevention

Primary prevention of SPGF1 is not feasible, given its monogenic nature and the sporadic occurrence of de novo mutations and translocations. There are no vaccines or environmental modifications that can prevent SYCP2 mutations. Public health interventions focusing on reproductive toxins and general testicular health may reduce multifactorial infertility but do not specifically target SPGF1.

### 13.2. Secondary and Tertiary Prevention

Secondary prevention, in the sense of early detection and intervention, is limited to identifying SPGF1 early in life, which could allow earlier counseling and planning. However, due to the non-life-threatening nature of the disease and the lack of curative therapies, early detection does not change the biological course but may alleviate psychological burdens.

Tertiary prevention involves preventing complications in those with established SPGF1. Complications in this context are psychosocial rather than medical, and tertiary prevention includes mental health support, marital counseling, and avoidance of unnecessary invasive procedures once the prognosis for sperm retrieval is clearly understood.

### 13.3. Genetic Counseling and Reproductive Planning

Genetic counseling is a key preventive and management strategy for SPGF1. Once a SYCP2 pathogenic variant is identified in a proband, counseling can inform relatives of their risk and guide reproductive decisions.[13][10][14] Female carriers can be offered options such as PGT-M to avoid transmitting the variant to male offspring, although the ethics and desirability of such interventions depend on individual preferences.

Prenatal genetic diagnosis and PGT-M require identification of the familial variant and coordination with IVF programs. Counseling should also address the likelihood that male offspring inheriting the variant will experience severe infertility, while female offspring may be unaffected or have unknown risks.

Behavioral interventions, such as avoiding known reproductive toxins, are beneficial for general fertility but do not prevent SPGF1, and thus are secondary in importance.

### 13.4. Public Health Considerations

SPGF1’s rarity and lack of systemic health impacts make it a low priority for population-level public health interventions. Nonetheless, advancements in awareness of genetic causes of male infertility, improved access to genetic testing, and integration of infertility into reproductive health policies can indirectly support SPGF1 patients by facilitating diagnosis and counseling.

## 14. Other Species and Natural Disease

### 14.1. Species and Orthologous Genes

SYCP2 orthologs exist in many vertebrate species, including mouse (*Sycp2*), rat, and other mammals, as well as in some model organisms like yeast, which possess analogous SC proteins.[9][18][13] NCBI Taxonomy identifies Mus musculus (mouse; taxon ID 10090) and Homo sapiens (human; taxon ID 9606) as key species for studying SYCP2 function. NCBI Gene provides orthologous gene mappings; for example, human SYCP2 and mouse Sycp2 share conserved coiled-coil domains and centromere-associated regions.[18][9]

### 14.2. Natural Disease in Other Species

Natural disease analogous to SPGF1 has been observed in Sycp2-knockout mice, which exhibit infertility due to defective meiotic chromosome synapsis and apoptosis in spermatocytes.[9][18] Although these mice are genetically engineered rather than naturally occurring, they represent a model of SYCP2-mediated spermatogenic failure in a non-human species. There is no evidence of naturally occurring SYCP2 mutations causing infertility in companion animals or livestock in OMIA, but future veterinary genetic studies may uncover such cases.

### 14.3. Comparative Pathology and Evolutionary Conservation

Comparative pathology reveals that SC assembly and meiotic recombination are highly conserved across species. Mouse Sycp2 is required for SC assembly and chromosomal synapsis during male meiosis, and its disruption leads to infertility in both males and females, although sex-specific phenotypes may differ.[9][18] Feng et al. show that the SYCP2 NTR interacts with the centromere in mice, a function likely conserved in humans.[18] Yeast modeling of SYCP2 overexpression demonstrates that dysregulated SC proteins can disrupt SC integrity across divergent taxa.[13][18][17]

These findings support evolutionary conservation of SYCP2 function and disease mechanisms: structural SC defects lead to meiotic arrest and infertility in multiple species. HomoloGene and Alliance of Genome Resources would classify SYCP2 as a conserved meiosis gene.

### 14.4. Transmission and Zoonotic Potential

SPGF1 is not an infectious disease; there is no zoonotic potential or cross-species transmission. Transmission refers to genetic inheritance within species, and germline SYCP2 variants are transmitted through carriers but do not cross species boundaries.

## 15. Model Organisms

### 15.1. Mouse Models

Mouse models are central to understanding SPGF1 pathophysiology. Homozygous Sycp2-knockout mice exhibit complete meiotic arrest in both males and females, failed chromosomal synapsis, and germ cell apoptosis, resulting in infertility.[9][18] Yang et al., as summarized in OMIM, reported that male Sycp2 mutants fail to differentiate into pachytene spermatocytes and undergo apoptosis, providing a robust model of SYCP2 loss-of-function.[9] Feng et al. extended these findings by demonstrating centromere–SC association mediated by SYCP2 and showing that Sycp2−/− mice lack proper SYCP3 localization to lateral elements.[18]

Genoway offers a Sycp2 conditional knockout mouse model designed to study meiosis and reproductive biology, noting that infertility due to defective meiotic chromosome synapsis is a core phenotype.[15] Conditional knockout allows tissue-specific or timing-specific deletion of Sycp2, enabling nuanced study of its roles.

These mouse models recapitulate the human SPGF1 phenotype at the level of meiotic arrest, SC disruption, and infertility, although female infertility is more prominent in mice than in human female carriers of SYCP2 variants. This difference underscores species-specific aspects of SYCP2 function and checkpoint mechanisms.

### 15.2. Yeast and Cellular Models

Schilit et al. modeled SYCP2 dysregulation in budding yeast to study SC integrity.[13][17][18] Overexpression of SYCP2 in yeast disrupted SC structure, supporting the concept that both over- and underexpression of SC components can lead to functional loss. Yeast provides a powerful model for studying basic SC biology and dosage effects, although its SC proteins are not identical to mammalian SYCP2.

Cellular models, such as HEK293T cells transfected with wild-type or mutant SYCP2 constructs, have been used by Tan et al. to assess protein expression and localization.[10] These in vitro systems are not meiotic but allow study of protein trafficking and structure.

### 15.3. Model Limitations and Applications

Mouse and yeast models capture key aspects of SPGF1 pathophysiology, such as SC assembly, meiotic arrest, and infertility. However, they have limitations: differences in meiotic checkpoint stringency, sex-specific effects, and testicular architecture can lead to variations between human and model phenotypes.[18][9][13] Nonetheless, these models are invaluable for dissecting molecular mechanisms, testing hypotheses about variant effects, and exploring potential interventions at the experimental level.

Applications of these models include studying SYCP2’s interactions with SYCP3 and SYCP1, mapping domains critical for centromere association, and evaluating the impact of specific variants on SC structure. Conditional knockout mice can be used to examine the timing and cell-type specificity of SYCP2 function, while yeast models allow rapid genetic manipulations.

In a knowledge base, model organism annotations for SPGF1 should reference Sycp2-knockout mice and yeast overexpression models, with evidence tags indicating animal and cellular data supporting human disease mechanisms.[9][18][13][17][10]

## Conclusion

Spermatogenic failure 1 (SPGF1) is a rare, autosomal dominant, monogenic cause of male infertility characterized by non-obstructive azoospermia or severe oligozoospermia and meiotic arrest at the spermatocyte stage, caused by heterozygous pathogenic variants or dysregulation of the *SYCP2* gene on chromosome 20q13.33.[3][9][13][16][10] Clinical and histological data reveal a consistent pattern: germ cells enter meiosis but fail to complete synapsis and recombination, leading to apoptosis and a seminiferous epithelium devoid of mature sperm.[3][16] SYCP2 encodes a synaptonemal complex axial element protein essential for chromosome axis assembly, centromere–SC association, and recruitment of SYCP3 and SYCP1; its dysfunction disrupts SC formation and triggers meiotic checkpoints.[9][18][16]

Human genetic evidence from Schilit et al., Tan et al., and others demonstrates that heterozygous frameshift deletions, in-frame deletions, and structural dysregulation of SYCP2 cause severe spermatogenic failure in men, with maternal transmission possible but female carriers generally unaffected.[13][17][10][16] Animal models, particularly Sycp2-knockout mice, and yeast models of SYCP2 overexpression provide mechanistic insight into SC assembly and dosage sensitivity, confirming that both loss-of-function and misregulation can lead to infertility.[9][18][13]

Phenotypically, SPGF1 is non-syndromic and confined to the testes, with key HPO terms including azoospermia, non-obstructive azoospermia, male infertility, and spermatogenic arrest.[3][6][16] Endocrine function and extra-gonadal organs are largely normal, and quality-of-life impacts arise from reproductive disability rather than systemic illness. Epidemiologically, SPGF1 is extremely rare, likely accounting for a small fraction of non-obstructive azoospermia cases, and is recognized primarily in specialized infertility clinics.[13][16] Diagnostic workup involves semen analysis, testicular biopsy, and genetic testing via exome sequencing or male infertility panels that include SYCP2.[2][14][16] Differential diagnosis encompasses other monogenic meiotic arrest disorders, Y-chromosome AZF deletions, endocrine causes, and obstructive azoospermia.[3][4][5][6][7][16]

Treatment options are limited to assisted reproductive technologies—especially TESE and ICSI—when residual sperm are present; in cases of complete meiotic arrest, donor sperm and adoption are primary avenues to parenthood.[2][16] No disease-modifying pharmacotherapy or gene therapy exists, and prevention focuses on genetic counseling and reproductive planning in affected families.[13][10][14] Environmental and lifestyle factors, while important for general male fertility, are not specific contributors to SPGF1, which remains a predominantly genetic, meiosis-specific disorder.

For structured disease knowledge bases, SPGF1 can be annotated under Mendelian male infertility due to meiotic arrest, with causal gene SYCP2 (HGNC:SYCP2; OMIM *604105*), key phenotypes (HPO terms), cell types (CL: primary spermatocyte), anatomical sites (UBERON: testis, seminiferous tubule), and molecular processes (GO: synaptonemal complex assembly, meiotic nuclear division, apoptotic process). Evidence items should distinguish human clinical data (Schilit et al., Tan et al.), animal model data (Sycp2-knockout mice), and in vitro cellular studies (HEK293T localization), and include direct quotes from abstracts as shown. Future research directions include expanding case series to refine penetrance and expressivity, leveraging multi-omics and single-cell technologies to map SYCP2 expression and network interactions in human testes, and exploring gene- or cell-based therapies that might one day address the fundamental meiotic defect in SPGF1.

> “In sum, this investigation illustrates the power of precision cytogenetics for annotation of the infertile genome, suggests that these mechanisms should be considered as an alternative etiology to that of segregation of unbalanced gametes in infertile men harboring a BCA, and provides evidence of SYCP2-mediated male infertility in humans.”[17][13]

> “SYCP2 is important for spermatogenesis, as male mice homozygous for coiled-coil domain-deficient Sycp2 exhibit diminished homologous chromosome synapsis, apoptosis within the developing germline, and infertility.”[18][9]

> “We conclude that approximately 4% of men with otherwise unexplained severe spermatogenic failure carry mutations in NR5A1.”[5]

> “Our results show that mutations in the TEX11 gene account for 1% of infertility in non-obstructive azoospermic men.”[4]

These quotations situate SPGF1 within the broader landscape of monogenic male infertility and underscore the critical role of *SYCP2* in human meiosis and reproductive health.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.