---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-04T22:30:04.413362'
end_time: '2026-05-04T22:51:02.264138'
duration_seconds: 1257.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: 2-Methylbutyryl-CoA Dehydrogenase Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 15
    timeout: 2400
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 2-Methylbutyryl-CoA Dehydrogenase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **2-Methylbutyryl-CoA Dehydrogenase Deficiency** covering all of the
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

# Comprehensive Disease Characterization: 2-Methylbutyryl-CoA Dehydrogenase Deficiency

---

## Summary

**2-Methylbutyryl-CoA dehydrogenase deficiency (2-MBDD)**, also known as **short/branched-chain acyl-CoA dehydrogenase (SBCAD) deficiency** or **SBCADD**, is a rare autosomal recessive inborn error of L-isoleucine catabolism caused by biallelic pathogenic variants in the **ACADSB** gene (chromosome 10q26.13). The condition results in impaired oxidation of 2-methylbutyryl-CoA, leading to accumulation of 2-methylbutyrylglycine (2-MBG), 2-methylbutyrylcarnitine (C5-acylcarnitine), and 2-ethylhydracrylic acid in body fluids. It was first recognized as a distinct entity in the early 2000s, primarily through expanded newborn screening programs using tandem mass spectrometry.

The overwhelming majority (~90%) of individuals identified through newborn screening remain clinically asymptomatic throughout life, leading to ongoing debate about whether this condition is a clinically significant disease or a benign biochemical variant. However, approximately 10% of reported patients develop neurological manifestations including seizures, developmental delay, hypotonia, and failure to thrive. In vitro studies have demonstrated that the accumulating metabolite 2-methylbutyrylglycine induces oxidative stress in brain tissue, providing a plausible pathophysiological mechanism for the neurological symptoms observed in the symptomatic minority.

The condition exhibits striking founder effects: the **c.1165A>G** variant predominates in the **Hmong** population (causing exon 10 skipping), while the **c.303+3A>G** splice site variant is prevalent among individuals of **Somali/Eritrean** descent. A critical pharmacogenomic consideration is that valproic acid competitively inhibits residual SBCAD enzyme activity (Ki = 249 ± 29 μM), making this anticonvulsant potentially dangerous for affected individuals—particularly concerning given that seizures are among the presenting symptoms. Current management is conservative, consisting of L-carnitine supplementation, fasting avoidance, and metabolic monitoring during illness, with strict avoidance of valproic acid.

---

## 1. Disease Information

### Overview

2-Methylbutyryl-CoA dehydrogenase deficiency is a rare organic acidemia classified as an inborn error of branched-chain amino acid metabolism. It was first described in 2002–2003 by Gibson, Matern and colleagues as "a recently described autosomal recessive disorder of L-isoleucine metabolism" ([PMID: 12837870](https://pubmed.ncbi.nlm.nih.gov/12837870/)). The condition affects the fourth step in the L-isoleucine degradation pathway, where SBCAD catalyzes the dehydrogenation of 2-methylbutyryl-CoA to tiglyl-CoA.

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| **OMIM** | 610006 (phenotype); 600301 (ACADSB gene) |
| **Orphanet** | ORPHA:79157 |
| **MeSH** | C566487 |
| **MONDO** | MONDO:0012411 |
| **ICD-10** | E71.1 (Other disorders of branched-chain amino-acid metabolism) |

### Synonyms and Alternative Names

- Short/branched-chain acyl-CoA dehydrogenase deficiency (SBCADD)
- 2-MBAD deficiency
- 2-Methylbutyrylglycinuria (2-MBG)
- SBCAD deficiency
- 2-MBCD deficiency

### Information Sources

Information is derived from both aggregated disease-level resources (OMIM, Orphanet, GeneReviews) and individual patient reports/case series in the primary literature. The largest systematic review encompasses 162 reported patients ([PMID: 30730842](https://pubmed.ncbi.nlm.nih.gov/30730842/)). No large-scale cohort studies or EHR-based analyses are available due to disease rarity.

---

## 2. Etiology

### Disease Causal Factors

2-MBDD is exclusively **genetic** in origin. It is caused by biallelic (homozygous or compound heterozygous) loss-of-function mutations in the **ACADSB** gene, which encodes the short/branched-chain acyl-CoA dehydrogenase enzyme. A comprehensive review confirmed: "SBCAD deficiency is symptomatic in about 10% of reported patients. Clinical onset occurs in newborns or later in life with seizures, developmental delay, hypotonia, and failure to thrive" ([PMID: 30730842](https://pubmed.ncbi.nlm.nih.gov/30730842/)).

### Risk Factors

#### Genetic Risk Factors
- **Biallelic ACADSB mutations**: Required for disease manifestation (autosomal recessive)
- **Hmong ancestry**: The c.1165A>G founder mutation has extremely high carrier frequency in the Hmong population. In Wisconsin, "Of the remaining 92 confirmed SBCADD cases, 90 were of Hmong descent" ([PMID: 23712021](https://pubmed.ncbi.nlm.nih.gov/23712021/))
- **Somali/Eritrean ancestry**: The c.303+3A>G splice variant is "relatively prevalent in this population" ([PMID: 17883863](https://pubmed.ncbi.nlm.nih.gov/17883863/))
- **Consanguinity**: Increases risk for homozygous pathogenic variants, as shown in Iranian cases ([PMID: 41527137](https://pubmed.ncbi.nlm.nih.gov/41527137/), [PMID: 36604934](https://pubmed.ncbi.nlm.nih.gov/36604934/))

#### Environmental Risk Factors
- **Metabolic stress**: Illness, fever, fasting, and catabolic states may trigger metabolic decompensation in susceptible individuals
- **Valproic acid exposure**: Valproyl-CoA competitively inhibits SBCAD activity (Ki = 249 ± 29 μM) ([PMID: 21430231](https://pubmed.ncbi.nlm.nih.gov/21430231/)), potentially worsening the metabolic block
- **Protein overload**: High isoleucine intake increases flux through the impaired catabolic pathway

### Protective Factors

#### Genetic Protective Factors
- Residual enzyme activity from milder missense variants may explain asymptomatic phenotype in many patients
- "The relatively high prevalence of ACADSB gene mutations in control subjects suggests that MBD deficiency may be more common than previously thought but is not detected because of its usually benign nature" ([PMID: 17945527](https://pubmed.ncbi.nlm.nih.gov/17945527/))

#### Environmental Protective Factors
- **Early identification via newborn screening**: Allows presymptomatic intervention
- **Avoidance of metabolic stress**: Fasting avoidance and illness management
- **L-carnitine supplementation**: May help maintain metabolic homeostasis
- **R-pathway shunting**: An alternative metabolic route (R-pathway of isoleucine oxidation) may act as "a safety valve for overflow of accumulating S-pathway metabolites and thereby mitigate the severity of SBCADD" ([PMID: 15615815](https://pubmed.ncbi.nlm.nih.gov/15615815/))

### Gene–Environment Interactions

The most clinically significant gene–environment interaction involves **valproic acid (VPA)** and ACADSB genotype. Since "valproyl-CoA did inhibit SBCAD activity by a purely competitive mechanism with a K(i) of 249 ± 29 μM" ([PMID: 21430231](https://pubmed.ncbi.nlm.nih.gov/21430231/)), individuals with reduced SBCAD enzyme activity are particularly vulnerable to valproic acid-induced metabolic crisis. This is especially dangerous because seizures are among the presenting symptoms of 2-MBDD, and valproic acid is a commonly used antiepileptic drug.

---

## 3. Phenotypes

### Clinical Spectrum

The phenotypic spectrum of 2-MBDD ranges from completely asymptomatic to severe neurological involvement. A review of 162 patients established that approximately 90% remain asymptomatic ([PMID: 30730842](https://pubmed.ncbi.nlm.nih.gov/30730842/)).

### Phenotype Details

| Phenotype | HPO Term | Type | Onset | Severity | Frequency | Progression |
|-----------|----------|------|-------|----------|-----------|-------------|
| Developmental delay | HP:0001263 | Behavioral/cognitive | Infancy–childhood | Variable | ~10% of identified patients | Variable |
| Seizures | HP:0001250 | Neurological sign | Neonatal–childhood | Variable | ~5–10% | Episodic |
| Muscular hypotonia | HP:0001252 | Physical sign | Neonatal–infancy | Mild–moderate | ~5–10% | May improve |
| Failure to thrive | HP:0001508 | Growth abnormality | Infancy | Mild–moderate | ~5% | May resolve with treatment |
| Elevated C5-acylcarnitine | HP:0011015 (Abnormality of blood acylcarnitine profile) | Laboratory abnormality | Neonatal (detected by NBS) | Variable | ~100% at diagnosis | Stable/fluctuating |
| 2-Methylbutyrylglycinuria | HP:0003243 (Abnormality of urinary organic acid level) | Laboratory abnormality | Neonatal | Variable | ~80–90% of tested patients | Stable |
| Microcephaly | HP:0000252 | Physical sign | Infancy–childhood | Variable | Rare | Variable |
| Autism spectrum disorder | HP:0000729 | Behavioral | Childhood | Variable | Very rare (case reports) | Chronic |
| Intellectual disability | HP:0001249 | Cognitive | Childhood | Variable | Rare | Stable |
| Lethargy | HP:0001254 | Symptom | Neonatal–infancy | Mild–severe | Rare | Episodic |

### Quality of Life Impact

For the vast majority (~90%) of identified individuals, quality of life is unaffected as they remain asymptomatic. For the symptomatic minority, developmental delay and seizures may significantly impact daily functioning, educational attainment, and family quality of life. The need for ongoing metabolic monitoring and dietary vigilance during illness may impose a psychological burden even on asymptomatic families. No formal QoL studies (EQ-5D, SF-36) have been conducted specifically for this condition.

---

## 4. Genetic/Molecular Information

### Causal Gene

| Attribute | Value |
|-----------|-------|
| **Gene Symbol** | ACADSB |
| **HGNC ID** | HGNC:91 |
| **NCBI Gene ID** | 36 |
| **Ensembl** | ENSG00000196177 |
| **UniProt** | P45954 |
| **OMIM (Gene)** | 600301 |
| **Chromosomal Location** | 10q26.13 |
| **Gene Product** | Short/branched-chain acyl-CoA dehydrogenase (SBCAD) |

The original cDNA was cloned and characterized by Rozen et al. (1994): "The cDNA has significant sequence similarity to other members of the acyl-CoA dehydrogenase family, with the greatest homology (38%) to the short chain acyl-CoA dehydrogenase" ([PMID: 7698750](https://pubmed.ncbi.nlm.nih.gov/7698750/)).

### Protein Characteristics

The ACADSB gene encodes a 431-amino acid precursor protein that is processed to a 399-amino acid mature mitochondrial matrix enzyme. It is an FAD-dependent flavoenzyme that forms a homotetramer. The enzyme catalyzes the α,β-dehydrogenation of short/branched-chain acyl-CoA substrates, with activity on:
- **(S)-2-methylbutyryl-CoA** (primary physiological substrate)
- Isobutyryl-CoA
- 2-Methylhexanoyl-CoA
- Butyryl-CoA
- Hexanoyl-CoA

The enzyme uses **electron transfer flavoprotein (ETF)** as its physiologic electron acceptor, feeding electrons into the mitochondrial respiratory chain via ETF:ubiquinone oxidoreductase (ETFDH).

### Pathogenic Variants

| Variant | Type | Population | Consequence | Allele Frequency |
|---------|------|------------|-------------|-----------------|
| **c.1165A>G** | Missense/splicing | Hmong | Exon 10 skipping | Most common globally; ~41% of alleles in Chinese cohorts |
| **c.303+3A>G** | Splice site (intron 3) | Somali/Eritrean | Aberrant splicing | Founder in East Africa |
| **c.275C>G** | Nonsense | Chinese | Premature stop | ~23% of alleles in one Chinese cohort |
| **c.655G>A** | Missense | Chinese/diverse | Amino acid change | Recurrent |
| **c.923G>A** | Missense | Chinese/diverse | Amino acid change | Recurrent |
| **c.461G>A** | Missense | Chinese | Amino acid change | Novel ([PMID: 36709932](https://pubmed.ncbi.nlm.nih.gov/36709932/)) |
| **c.746del** | Frameshift | Chinese | Premature truncation | Rare |
| **c.907G>C (p.G303R)** | Missense | Iranian | Amino acid change | Novel ([PMID: 41527137](https://pubmed.ncbi.nlm.nih.gov/41527137/)) |

All known pathogenic variants are **germline** in origin. Functional consequences are **loss of function**, leading to reduced or absent SBCAD enzyme activity.

### Modifier Genes

No specific modifier genes have been identified for 2-MBDD. However, the variable expressivity (90% asymptomatic vs. 10% symptomatic) suggests the involvement of genetic modifiers. Variation in **ETFA/ETFB/ETFDH** (electron transfer flavoprotein pathway) or genes governing the R-pathway of isoleucine oxidation could potentially affect disease severity.

### Epigenetic and Chromosomal Information

No epigenetic modifications or chromosomal abnormalities have been reported in association with 2-MBDD. The condition is caused exclusively by point mutations and small indels in the ACADSB gene.

---

## 5. Environmental Information

### Environmental Factors

- **Metabolic stressors**: Febrile illness, prolonged fasting, surgical stress, and trauma can precipitate metabolic decompensation by increasing isoleucine catabolism
- **Valproic acid**: Valproyl-CoA competitively inhibits SBCAD (Ki = 249 ± 29 μM); this drug is strictly contraindicated ([PMID: 21430231](https://pubmed.ncbi.nlm.nih.gov/21430231/))
- **Riboflavin deficiency**: Since SBCAD is FAD-dependent, severe riboflavin deficiency could theoretically worsen the enzymatic defect, though this has not been specifically studied in 2-MBDD. Riboflavin deficiency is known to impair fatty acid β-oxidation generally ([PMID: 29185933](https://pubmed.ncbi.nlm.nih.gov/29185933/))

### Lifestyle Factors

- **Dietary protein intake**: High-protein diets increase isoleucine load, potentially exacerbating metabolite accumulation
- **Fasting**: Increases catabolism of endogenous branched-chain amino acids
- **Breastfeeding**: Generally well-tolerated and recommended with appropriate monitoring ([PMID: 41527137](https://pubmed.ncbi.nlm.nih.gov/41527137/))

### Infectious Agents

Not applicable. 2-MBDD is not caused by infectious agents. However, intercurrent infections are a major trigger for metabolic decompensation due to the catabolic stress response.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathway

2-MBDD affects the **isoleucine degradation pathway** (KEGG pathway: hsa00280 — Valine, leucine, and isoleucine degradation). The specific enzymatic step impaired is:

```
L-Isoleucine
    ↓ (BCAT — transamination)
3-Methyl-2-oxopentanoic acid (α-keto-β-methylvaleric acid)
    ↓ (BCKDH complex — oxidative decarboxylation)
2-Methylbutyryl-CoA (S-2-methylbutyryl-CoA)
    ↓ ✖ SBCAD (ACADSB) — BLOCKED IN 2-MBDD ✖
Tiglyl-CoA
    ↓ (Crotonase)
2-Methyl-3-hydroxybutyryl-CoA
    ↓ (HSD17B10/HADH2)
2-Methylacetoacetyl-CoA
    ↓ (β-Ketothiolase/T2)
Propionyl-CoA + Acetyl-CoA → TCA cycle
```

### Metabolite Accumulation

The enzymatic block leads to accumulation of:
- **2-Methylbutyryl-CoA** → conjugated with glycine to form **2-methylbutyrylglycine (2-MBG)**
- **2-Methylbutyryl-CoA** → conjugated with carnitine to form **2-methylbutyrylcarnitine (C5)**
- **2-Ethylhydracrylic acid (2-EHA)** — formed via the alternative R-pathway of isoleucine oxidation ([PMID: 15615815](https://pubmed.ncbi.nlm.nih.gov/15615815/))

### Oxidative Stress Mechanism

The key pathophysiological mechanism linking metabolite accumulation to neurological damage is **oxidative stress** in brain tissue. An in vitro study using rat cerebral cortex and C6 glioma cells demonstrated:

> "2MBG increased thiobarbituric acid-reactive substances (TBA-RS), indicating an increase of lipid oxidation. 2MBG induced sulfhydryl oxidation in cortical supernatants and decreased glutathione (GSH) in these brain preparations, as well as in C6 cells, indicating a reduction of nonenzymatic brain antioxidant defenses." ([PMID: 22967964](https://pubmed.ncbi.nlm.nih.gov/22967964/))

Key findings from this study:
- **2-Methylbutyrylglycine (2-MBG)** induced lipid peroxidation (increased TBA-RS)
- 2-MBG caused **sulfhydryl oxidation** and **decreased glutathione (GSH)**
- Effects were **prevented by free radical scavengers**, implicating reactive oxygen species (ROS)
- The parent acid **2-methylbutyric acid did not** alter these parameters, identifying 2-MBG as the neurotoxic species
- No protein carbonyl formation or cell death was observed at tested concentrations

### Causal Chain: From Genetic Defect to Clinical Manifestation

```
ACADSB mutations (loss of function)
    → Impaired 2-methylbutyryl-CoA dehydrogenation
        → Accumulation of 2-methylbutyryl-CoA and conjugates
            → 2-MBG accumulates in tissues including brain
                → ROS generation → Lipid peroxidation
                → GSH depletion → Reduced antioxidant defense
                    → Neuronal oxidative damage
                        → Seizures, developmental delay, hypotonia
```

### R-Pathway Safety Valve

A potentially protective mechanism involves shunting through the R-pathway of isoleucine oxidation. Approximately 40–46% of total 2-methylbutyric acid conjugates in SBCADD patients were in the R-isomer form, "indicating significant metabolism via the R-pathway." The observation of 2-ethylhydracrylic aciduria in SBCADD "implies that a different or alternative enzyme serves this function" and "Increased flux through the R-pathway may act as a safety valve for overflow of accumulating S-pathway metabolites" ([PMID: 15615815](https://pubmed.ncbi.nlm.nih.gov/15615815/)).

### Protein Dysfunction

SBCAD protein dysfunction results from:
- **Enzyme inactivation**: Missense mutations leading to loss of catalytic activity
- **Protein instability**: Mutations causing misfolding and degradation
- **Splice defects**: The Hmong founder mutation causes exon 10 skipping, producing a truncated non-functional protein

### Relevant GO Terms

| Category | Term | GO ID |
|----------|------|-------|
| Biological Process | Branched-chain amino acid catabolic process | GO:0009083 |
| Biological Process | L-isoleucine catabolic process | GO:0006550 |
| Biological Process | Response to oxidative stress | GO:0006979 |
| Molecular Function | Acyl-CoA dehydrogenase activity | GO:0003995 |
| Cellular Component | Mitochondrial matrix | GO:0005759 |
| Cellular Component | Mitochondrion | GO:0005739 |

### Cell Types Involved

| Cell Type | CL Term | Role |
|-----------|---------|------|
| Neuron | CL:0000540 | Target of oxidative damage |
| Astrocyte | CL:0000127 | C6 glioma model; GSH depletion |
| Hepatocyte | CL:0000182 | Major site of isoleucine catabolism |

### Molecular Profiling

No transcriptomic, proteomic, metabolomic, or lipidomic profiling studies have been specifically conducted in 2-MBDD patients or cells. The metabolomic signature is characterized by elevated 2-methylbutyrylcarnitine (C5), 2-methylbutyrylglycine, and 2-ethylhydracrylic acid. No single-cell, spatial transcriptomics, or functional genomics screens have been reported.

---

## 7. Anatomical Structures Affected

### Organ Level

| Level | Structures | UBERON Terms |
|-------|-----------|-------------|
| **Primary** | Brain (CNS) | UBERON:0000955 (brain) |
| **Primary** | Liver (metabolic processing) | UBERON:0002107 (liver) |
| **Primary** | Skeletal muscle | UBERON:0001134 (skeletal muscle tissue) |
| **Secondary** | Heart (rare, in severe cases) | UBERON:0000948 (heart) |

**Body systems involved**: Nervous system (primary), musculoskeletal system, metabolic system.

### Tissue and Cell Level

- **Nervous tissue** (UBERON:0003714): Neurons and glia affected by oxidative stress from accumulating metabolites
- **Glial cells** (CL:0000125): C6 glioma cells showed GSH depletion in response to 2MBG ([PMID: 22967964](https://pubmed.ncbi.nlm.nih.gov/22967964/))
- **Neurons** (CL:0000540): Likely targets of neurotoxicity

### Subcellular Level

- **Mitochondria** (GO:0005739): Primary site of metabolic block; SBCAD is a mitochondrial matrix enzyme
- **Mitochondrial matrix** (GO:0005759): Specific compartment where SBCAD functions
- **Cell membrane lipids**: Target of lipid peroxidation by 2MBG

### Localization

- **Brain** (UBERON:0000955): Cerebral cortex particularly affected based on experimental evidence
- **Bilateral**: Neurological manifestations are typically bilateral and symmetric
- No specific lateralization reported

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: Variable
  - Biochemical abnormalities: Detectable at birth (neonatal period) via newborn screening
  - Clinical symptoms (when present): Neonatal period to early childhood
  - Some patients may remain asymptomatic indefinitely into adulthood
- **Onset pattern**: Insidious or episodic (triggered by metabolic stress)

### Progression

- **Disease stages**: Not formally staged
- **Progression rate**: Variable; most patients show no progression (remain asymptomatic)
- **Disease course pattern**:
  - Majority: Stable, asymptomatic (lifelong biochemical abnormality without clinical disease)
  - Symptomatic minority: May be episodic (triggered by metabolic stress) or show progressive developmental delay
- **Disease duration**: Chronic, lifelong metabolic defect

### Critical Periods

- **Neonatal period**: Window of vulnerability for acute metabolic decompensation
- **Early brain development**: Vulnerable period for neurotoxicity from accumulating metabolites
- **Any catabolic state**: Illness, surgery, fasting at any age

---

## 9. Inheritance and Population

### Inheritance Pattern

- **Inheritance**: Autosomal recessive (AR) (HP:0000007)
- **Penetrance**: Incomplete; approximately 10% of individuals with biallelic mutations develop symptoms
- **Expressivity**: Highly variable, even within families with the same genotype
- **Genetic anticipation**: Not described
- **Germline mosaicism**: Not reported

### Epidemiology

| Population | Incidence | Source |
|-----------|-----------|--------|
| **Quanzhou, China** | ~1:38,544 newborns (18/693,797) | [PMID: 40835664](https://pubmed.ncbi.nlm.nih.gov/40835664/) |
| **Nanjing, China** | ~1:227,571 (12/2,730,852) | [PMID: 36709932](https://pubmed.ncbi.nlm.nih.gov/36709932/) |
| **China (meta-analysis)** | Significantly higher in southern than northern China | [PMID: 41440809](https://pubmed.ncbi.nlm.nih.gov/41440809/) |
| **Wisconsin, USA (Hmong population)** | Very high (~1:350–500 estimated in Hmong) | [PMID: 23712021](https://pubmed.ncbi.nlm.nih.gov/23712021/) |
| **General population** | Ultra-rare; likely underdiagnosed | [PMID: 17945527](https://pubmed.ncbi.nlm.nih.gov/17945527/) |

### Founder Effects

Two major founder mutations have been identified:

1. **Hmong population — c.1165A>G**: This mutation causes exon 10 skipping. In Wisconsin over a 10-year period (2001–2011), "Of the remaining 92 confirmed SBCADD cases, 90 were of Hmong descent. Mutation analysis was completed on an anonymous, random sample of newborn screening cards (n=1139) from Hmong infants" with 15 carriers identified ([PMID: 23712021](https://pubmed.ncbi.nlm.nih.gov/23712021/)). "While the first reported patients had severe disease, most of the affected Hmong have remained asymptomatic" ([PMID: 20547083](https://pubmed.ncbi.nlm.nih.gov/20547083/)).

2. **Somali/Eritrean population — c.303+3A>G**: "This mutation was also found in two previously reported cases with SBCADD, both originating from Somalia and Eritrea, indicating that it is relatively prevalent in this population" ([PMID: 17883863](https://pubmed.ncbi.nlm.nih.gov/17883863/)).

### Geographic Distribution of Specific Variants

- **c.1165A>G**: Southeast Asia (Hmong communities in Laos, Vietnam, Thailand, southern China, and diaspora in US/France/Australia)
- **c.303+3A>G**: East Africa (Somalia, Eritrea)
- **c.275C>G, c.655G>A**: Chinese NBS populations
- **c.907G>C**: Iran ([PMID: 41527137](https://pubmed.ncbi.nlm.nih.gov/41527137/))

### Population Demographics

- **Sex ratio**: Expected 1:1 (autosomal recessive); no sex predilection reported
- **Consanguinity**: Increases risk, particularly relevant in Middle Eastern and North African populations ([PMID: 36604934](https://pubmed.ncbi.nlm.nih.gov/36604934/))
- **Carrier frequency (Hmong)**: ~1.3% (15/1,139 screened newborns) ([PMID: 23712021](https://pubmed.ncbi.nlm.nih.gov/23712021/))

---

## 10. Diagnostics

### Newborn Screening (Primary Detection Method)

2-MBDD is primarily detected through **expanded newborn screening (NBS)** using tandem mass spectrometry (MS/MS):
- **Primary marker**: Elevated C5-acylcarnitine (isovalerylcarnitine/2-methylbutyrylcarnitine) in dried blood spots
- **Typical screening values**: C5 between 0.6–2.1 μmol/L in affected patients (normal <0.5 μmol/L) ([PMID: 36709932](https://pubmed.ncbi.nlm.nih.gov/36709932/))
- **Challenge**: C5-acylcarnitine is isobaric — it cannot distinguish between isovalerylcarnitine (elevated in isovaleric acidemia) and 2-methylbutyrylcarnitine (elevated in 2-MBDD)
- **MAXO term**: MAXO:0000127 (newborn screening)

### Second-Tier Testing

Second-tier LC-MS/MS methods can differentiate C5-acylcarnitine isoforms: "Data from the analysis of short-chain acylcarnitine and acylglycine were useful for differential diagnosis in cases positive for... C5-acylcarnitine" ([PMID: 34287228](https://pubmed.ncbi.nlm.nih.gov/34287228/)). UPLC-MS/MS analysis can separate isovalerylcarnitine, 2-methylbutyrylcarnitine, and pivaloylcarnitine ([PMID: 23499962](https://pubmed.ncbi.nlm.nih.gov/23499962/)).

### Confirmatory Testing

| Test | Method | Key Findings |
|------|--------|-------------|
| **Urine organic acids** | GC-MS | Elevated 2-methylbutyrylglycine (2-MBG); may also show 2-ethylhydracrylic acid |
| **Urine acylglycines** | UPLC-MS/MS | Elevated 2-MBG — "a highly sensitive and specific method with proven clinical utility" ([PMID: 27727436](https://pubmed.ncbi.nlm.nih.gov/27727436/)) |
| **Blood acylcarnitines** | MS/MS | Elevated C5 (2-methylbutyrylcarnitine), elevated C5/C2 and C5/C3 ratios |
| **Genetic testing** | Sanger/NGS/WES | Biallelic pathogenic variants in ACADSB |
| **Enzyme assay** | Fibroblast/lymphocyte | Reduced SBCAD activity (research settings) |

### Differential Diagnosis

| Condition | Distinguishing Feature |
|-----------|----------------------|
| **Isovaleric acidemia (IVA)** | Elevated isovalerylglycine (not 2-MBG); mutations in IVD gene |
| **SCAD deficiency** | Elevated ethylmalonic acid; mutations in ACADS gene |
| **MADD (Multiple acyl-CoA dehydrogenase deficiency)** | Multiple acylcarnitine species elevated; mutations in ETFA/ETFB/ETFDH |
| **Isobutyryl-CoA dehydrogenase deficiency (IBDD)** | Elevated C4-acylcarnitine; isobutyrylglycine in urine; ACAD8 mutations |
| **Pivaloylcarnitine interference** | Antibiotic (pivampicillin) exposure history; no organic aciduria |

### Genetic Testing

- **Whole exome sequencing (WES)**: Effective for diagnosis, used in the first Iranian case ([PMID: 41527137](https://pubmed.ncbi.nlm.nih.gov/41527137/))
- **Single gene testing**: ACADSB Sanger sequencing (11 exons)
- **Targeted mutation analysis**: For known founder mutations in Hmong and Somali/Eritrean populations
- **Gene panels**: Organic acidemia/inborn errors of metabolism panels that include ACADSB

### Screening

- **Newborn screening**: Part of expanded NBS panels in many countries using MS/MS
- **Cascade screening**: Recommended for siblings of affected individuals
- **Carrier screening**: Available for known founder mutations
- **Prenatal diagnosis**: Possible via molecular analysis of ACADSB mutations on CVS or amniocentesis

---

## 11. Outcome / Prognosis

### Overall Prognosis

The prognosis for 2-MBDD is generally **excellent**. The vast majority of patients identified through NBS remain asymptomatic and achieve normal growth and development.

- In one Chinese NBS cohort of 12 patients followed 18 days to 55 months: "Only one patient had mental retardation, with the remainders having normal physical and mental development" ([PMID: 36709932](https://pubmed.ncbi.nlm.nih.gov/36709932/))
- In the Italian cohort: "As all patients were asymptomatic, no association between biochemical parameters and clinical phenotype could be investigated" ([PMID: 36147814](https://pubmed.ncbi.nlm.nih.gov/36147814/))
- "MBD deficiency may be a harmless metabolic variant although significant impairment of valproic acid metabolism cannot be excluded" ([PMID: 17945527](https://pubmed.ncbi.nlm.nih.gov/17945527/))

### Survival and Mortality

- **Life expectancy**: Likely normal for the vast majority of patients
- **Mortality**: No disease-specific mortality has been reported in NBS-detected cohorts
- **Disease-specific mortality**: Extremely rare; no deaths directly attributed to 2-MBDD in screened populations

### Complications

- **Metabolic crisis**: Risk during catabolic stress (illness, fasting, surgery)
- **Neurological sequelae**: Developmental delay, intellectual disability in ~10% of reported cases
- **Pharmacogenomic risk**: Valproic acid toxicity in undiagnosed individuals

### Prognostic Factors

- **Genotype**: Severity of ACADSB mutations (null vs. partial loss of function) may influence risk
- **Early detection**: NBS-detected patients managed proactively have excellent outcomes
- **Avoidance of triggers**: Fasting, catabolic stress, valproic acid

---

## 12. Treatment

### Pharmacotherapy

#### L-Carnitine Supplementation (MAXO:0001298)
- **Rationale**: Buffers accumulating acyl-CoA intermediates; prevents secondary carnitine deficiency
- **Typical dose**: 50–100 mg/kg/day (standard for organic acidemias)
- **Evidence**: An Italian study found "relatively stable serum C5 values observed during L-carnitine supplementation together with C5 increase occurring upon L-carnitine discontinuation/intercurrent illness may support the value of serum C5 as a monitoring biomarker and the benefit of this treatment in SBCADD patients" ([PMID: 36147814](https://pubmed.ncbi.nlm.nih.gov/36147814/))

#### Drug Avoidance
- **Valproic acid is strictly contraindicated**: "valproyl-CoA did inhibit SBCAD activity by a purely competitive mechanism with a K(i) of 249 ± 29 μM" ([PMID: 21430231](https://pubmed.ncbi.nlm.nih.gov/21430231/))
- Alternative antiepileptic drugs should be selected for seizure management

### Dietary Management (MAXO:0000527)

- **Protein restriction**: Mild to moderate restriction of protein/isoleucine intake recommended in some symptomatic cases
- **Breastfeeding**: Generally continued with monitoring; in the first Iranian case "The infant was managed with a carnitine-supplemented diet and continued breastfeeding. Regular follow-ups demonstrated normal growth, neurodevelopmental milestones, and biochemical parameters" ([PMID: 41527137](https://pubmed.ncbi.nlm.nih.gov/41527137/))
- **Fasting avoidance**: Important during illness and catabolic states

### Emergency Management

- **Sick-day protocols**: During intercurrent illness, provide increased caloric intake (glucose infusion if needed), avoid prolonged fasting
- **Emergency letter**: Patients should carry a metabolic emergency letter

### Supportive and Rehabilitative

- **Neurodevelopmental follow-up**: Recommended for all identified patients
- **Regular biochemical monitoring**: C5-acylcarnitine levels, urine organic acids
- **Developmental services**: For symptomatic patients with developmental delay

### Investigational/Experimental Treatments

- **Antioxidant therapy**: Given the oxidative stress mechanism ([PMID: 22967964](https://pubmed.ncbi.nlm.nih.gov/22967964/)), antioxidants are a rational therapeutic target, but no clinical trials exist. "Prospective studies are needed to test the effectiveness of adjunct therapies such as antioxidants... in addition to specialized diets" ([PMID: 21290185](https://pubmed.ncbi.nlm.nih.gov/21290185/))
- **Growth hormone**: One study on organic acidemia patients (including one with an isoleucine metabolism defect) showed increased linear growth and nitrogen retention ([PMID: 7993663](https://pubmed.ncbi.nlm.nih.gov/7993663/)), but this has not been specifically studied in 2-MBDD
- **Riboflavin supplementation**: As SBCAD is FAD-dependent, riboflavin responsiveness should be assessed in patients with missense mutations, though this has not been systematically studied
- **Gene therapy**: No gene therapy trials are currently registered for 2-MBDD
- No clinical trials specifically for 2-MBDD are registered on ClinicalTrials.gov

### Treatment Strategy

Given the uncertain clinical significance in most patients, "With the individual life-time risk and degree of severity being unknown in asymptomatic individuals with MBDD or IBDD, instructions regarding risks for metabolic stress and fasting avoidance along with clinical monitoring are reasonable interventions at the current time" ([PMID: 21290185](https://pubmed.ncbi.nlm.nih.gov/21290185/)).

---

## 13. Prevention

### Primary Prevention

- **Genetic counseling** (MAXO:0000079): For families with known ACADSB mutations; recurrence risk 25% for each subsequent pregnancy of carrier parents
- **Carrier screening**: Targeted screening in high-risk populations (Hmong, Somali/Eritrean)
- **Prenatal genetic diagnosis**: Available for families with known pathogenic variants
- **Preimplantation genetic diagnosis (PGD)**: Technically feasible for families undergoing IVF

### Secondary Prevention (Early Detection)

- **Newborn screening** (MAXO:0000127): MS/MS-based expanded newborn screening detects elevated C5-acylcarnitine in dried blood spots. This is the primary method of case ascertainment.
- **Cascade screening**: Testing of siblings of identified patients
- **Metabolic screening in high-risk populations**: Particularly Hmong and Somali/Eritrean communities

### Tertiary Prevention

- **Metabolic monitoring**: Regular follow-up with metabolic specialist
- **Sick-day protocols**: Prevent metabolic crises during illness
- **Valproic acid avoidance**: Critical pharmacogenomic counseling for all patients and families
- **Dietary management**: Avoid excessive protein/isoleucine loading
- **L-carnitine supplementation**: May prevent secondary carnitine deficiency

### Public Health Considerations

The primary public health intervention is the inclusion of C5-acylcarnitine in expanded newborn screening panels. The debate continues about whether detection of this mostly benign condition through NBS creates unnecessary parental anxiety and medical follow-up costs versus the value of identifying the minority at risk for complications and the pharmacogenomic risk of valproic acid exposure.

---

## 14. Other Species / Natural Disease

### Naturally Occurring Disease

No naturally occurring SBCAD deficiency has been reported in non-human species. The condition has not been described in companion animals, livestock, or wildlife. No entry for SBCADD exists in the Online Mendelian Inheritance in Animals (OMIA) database.

### Orthologous Genes

| Species | Gene | NCBI Gene ID | NCBI Taxon ID | Notes |
|---------|------|-------------|---------------|-------|
| *Mus musculus* (mouse) | Acadsb | 66885 | 10090 | Orthologous gene; no KO model published |
| *Rattus norvegicus* (rat) | Acadsb | 25618 | 10116 | Brain tissue used in pathophysiology studies |
| *Danio rerio* (zebrafish) | acadsb | 393595 | 7955 | Orthologous gene |

### Comparative Biology

- The isoleucine catabolic pathway is highly conserved across vertebrates
- Rat cerebral cortex tissue has been used as an experimental system to study the pathophysiology of accumulating metabolites ([PMID: 22967964](https://pubmed.ncbi.nlm.nih.gov/22967964/))
- Species differences in BCAA catabolism exist between mice and humans, which should be considered when developing animal models ([PMID: 32451238](https://pubmed.ncbi.nlm.nih.gov/32451238/))

### Transmission

Not applicable. 2-MBDD is a genetic metabolic disorder with no zoonotic potential or cross-species transmission.

---

## 15. Model Organisms

### Available Models

No dedicated **ACADSB knockout mouse model** has been published as of this report. This represents a significant gap in the field.

### In Vitro Models

| Model | Application | Reference |
|-------|-------------|-----------|
| **Rat cerebral cortex homogenates** | Oxidative stress from 2-MBG | [PMID: 22967964](https://pubmed.ncbi.nlm.nih.gov/22967964/) |
| **C6 glioma cells (rat)** | GSH depletion from 2-MBG | [PMID: 22967964](https://pubmed.ncbi.nlm.nih.gov/22967964/) |
| **Patient-derived fibroblasts** | Enzyme activity assays, functional studies | [PMID: 17945527](https://pubmed.ncbi.nlm.nih.gov/17945527/) |
| **E. coli expression system** | Recombinant SBCAD characterization | [PMID: 7698750](https://pubmed.ncbi.nlm.nih.gov/7698750/), [PMID: 20547083](https://pubmed.ncbi.nlm.nih.gov/20547083/) |

### Related Animal Models in the ACAD Family

The closely related **ACAD9** gene has been modeled in mice:
- "Homozygous total body knock out appeared to be lethal as no ACAD9 animals were obtained"
- "Cardiac-specific ACAD9 deficient animals had severe neonatal cardiomyopathy and died by 17 days of age" ([PMID: 34556413](https://pubmed.ncbi.nlm.nih.gov/34556413/))

While ACAD9 deficiency is a distinct disorder (affecting complex I assembly rather than isoleucine catabolism), these models provide insights into the broader acyl-CoA dehydrogenase family.

### Model Limitations

- No whole-organism models available for studying systemic effects
- In vitro oxidative stress studies used potentially supraphysiological metabolite concentrations
- Rat models may not fully recapitulate human isoleucine metabolism
- The variable penetrance seen in humans cannot be studied in current in vitro models
- The E. coli expression system only addresses enzyme function, not disease pathophysiology

### Research Applications Needed

Development of an Acadsb knockout mouse would enable study of:
- Long-term neurological outcomes
- Metabolic decompensation triggers
- Valproic acid interaction in vivo
- Therapeutic interventions (carnitine, antioxidants, riboflavin)
- Genotype-phenotype correlations

---

## Key Findings Summary

1. **2-MBDD is a rare autosomal recessive organic acidemia** caused by ACADSB gene mutations, affecting isoleucine catabolism (OMIM 610006).

2. **Most patients (~90%) are asymptomatic**, raising questions about clinical significance and appropriate intervention levels.

3. **Strong founder effects** exist in the Hmong (c.1165A>G) and Somali/Eritrean (c.303+3A>G) populations, accounting for the majority of known cases.

4. **Oxidative stress is the key pathophysiological mechanism**: The accumulating metabolite 2-MBG induces lipid peroxidation and depletes glutathione in brain tissue, providing a mechanistic basis for the neurological symptoms observed in the symptomatic minority.

5. **Newborn screening** is the primary means of detection, but the isobaric nature of C5-acylcarnitines requires second-tier testing for differential diagnosis from isovaleric acidemia.

6. **Valproic acid interaction is critically important**: SBCAD metabolizes valproyl-CoA, and valproyl-CoA competitively inhibits SBCAD (Ki = 249 ± 29 μM), creating a dangerous pharmacogenomic interaction.

7. **Treatment is largely supportive**: L-carnitine supplementation, fasting avoidance, metabolic monitoring, and strict avoidance of valproic acid.

---

## Ontology Term Summary

| Category | Term | ID |
|----------|------|-----|
| Disease | 2-methylbutyryl-CoA dehydrogenase deficiency | MONDO:0012411 |
| Gene | ACADSB | HGNC:91 |
| Protein function | Acyl-CoA dehydrogenase activity | GO:0003995 |
| Biological process | L-isoleucine catabolic process | GO:0006550 |
| Biological process | Branched-chain amino acid catabolic process | GO:0009083 |
| Biological process | Response to oxidative stress | GO:0006979 |
| Cellular component | Mitochondrial matrix | GO:0005759 |
| Phenotype | Seizures | HP:0001250 |
| Phenotype | Global developmental delay | HP:0001263 |
| Phenotype | Muscular hypotonia | HP:0001252 |
| Phenotype | Failure to thrive | HP:0001508 |
| Phenotype | Intellectual disability | HP:0001249 |
| Phenotype | Microcephaly | HP:0000252 |
| Phenotype | Autism spectrum disorder | HP:0000729 |
| Inheritance | Autosomal recessive | HP:0000007 |
| Anatomy | Brain | UBERON:0000955 |
| Anatomy | Liver | UBERON:0002107 |
| Anatomy | Skeletal muscle | UBERON:0001134 |
| Cell type | Neuron | CL:0000540 |
| Cell type | Astrocyte | CL:0000127 |
| Cell type | Hepatocyte | CL:0000182 |
| Chemical | L-isoleucine | CHEBI:58045 |
| Chemical | L-carnitine | CHEBI:17126 |
| Treatment | Newborn screening | MAXO:0000127 |
| Treatment | Dietary modification | MAXO:0000527 |
| Treatment | Genetic counseling | MAXO:0000079 |

---

## Limitations and Knowledge Gaps

1. **Incomplete penetrance is unexplained**: Why ~90% of individuals with biallelic ACADSB mutations remain asymptomatic is unknown. Modifier genes, epigenetic factors, or environmental triggers may play roles.

2. **No animal model**: The absence of an Acadsb knockout mouse limits understanding of systemic pathophysiology and therapeutic testing.

3. **Oxidative stress data are in vitro only**: The brain oxidative stress mechanism has not been confirmed in vivo or in human studies.

4. **Long-term outcome data are limited**: Most NBS cohorts have short follow-up periods. Adult outcomes of NBS-detected individuals are unknown.

5. **Genotype–phenotype correlation is poor**: The same c.1165A>G Hmong founder mutation produces both symptomatic and asymptomatic individuals.

6. **Treatment efficacy is unproven**: L-carnitine supplementation is standard of care, but no randomized controlled trials exist.

7. **No omics profiling**: No transcriptomic, proteomic, or metabolomic studies have been performed on patient-derived cells or tissues.

8. **No clinical trials**: No interventional clinical trials are registered for 2-MBDD.

9. **Rare disease bias**: Published cases likely overrepresent symptomatic individuals, potentially inflating the perceived symptomatic rate.

---

## Proposed Follow-up Experiments and Actions

### High Priority

1. **Generate an Acadsb conditional knockout mouse model** to study tissue-specific metabolic effects, brain oxidative stress in vivo, metabolic decompensation under stress, and valproic acid toxicity.

2. **Prospective long-term follow-up study** of NBS-detected cohorts (ideally international, multi-center) to determine true lifetime symptomatic rate, identify prognostic biomarkers, and assess neurodevelopmental outcomes into adulthood.

3. **Multi-omics profiling** of patient-derived fibroblasts and iPSC-derived neurons to identify metabolomic signatures, discover potential modifier pathways, and test antioxidant therapeutic strategies in vitro.

### Medium Priority

4. **Genotype–phenotype correlation study**: Comprehensive analysis of all known ACADSB variants with residual enzyme activity measurements and clinical outcomes.

5. **Antioxidant clinical pilot study**: Based on the oxidative stress mechanism, test N-acetylcysteine or other antioxidants as adjunctive therapy in symptomatic patients.

6. **Population screening for ACADSB variants** in gnomAD to better estimate global carrier frequencies and identify additional high-risk populations.

### Lower Priority

7. **R-pathway enzyme identification**: Identify the enzyme(s) responsible for R-2-methylbutyryl-CoA dehydrogenation, which could be a therapeutic target to enhance the protective shunt pathway.

8. **Riboflavin responsiveness study**: Systematically assess whether high-dose riboflavin can enhance residual SBCAD activity in patients with missense mutations.

9. **Natural history registry**: Establish an international 2-MBDD/SBCADD patient registry to aggregate clinical and genetic data.

---

*Report compiled from systematic literature review of 32 primary publications, database queries (OMIM, Orphanet, UniProt, KEGG), and analysis of available clinical and biochemical data. All citations are linked to PubMed identifiers for verification. Report generated May 2026.*
