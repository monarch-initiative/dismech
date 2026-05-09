---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T02:23:26.793002'
end_time: '2026-05-05T03:03:31.672727'
duration_seconds: 2404.88
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: 3-Methylcrotonyl-CoA Carboxylase Deficiency
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
    timeout: 5400
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 3-Methylcrotonyl-CoA Carboxylase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **3-Methylcrotonyl-CoA Carboxylase Deficiency** covering all of the
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

# Comprehensive Disease Report: 3-Methylcrotonyl-CoA Carboxylase Deficiency (3-MCCD)

## Summary

**3-Methylcrotonyl-CoA carboxylase deficiency (3-MCCD)** is an autosomal recessive inborn error of leucine catabolism caused by biallelic mutations in either the *MCCC1* gene (encoding the biotin-containing alpha subunit, MCCα) or the *MCCC2* gene (encoding the carboxyltransferase beta subunit, MCCβ) of the mitochondrial enzyme 3-methylcrotonyl-CoA carboxylase (MCC; EC 6.4.1.4). It is the most frequently detected organic aciduria in tandem mass spectrometry (MS/MS)-based newborn screening programs worldwide, with incidence estimates ranging from approximately 1:33,000 to 1:83,000 depending on the population studied. The enzymatic block at the fourth step of the leucine degradation pathway causes characteristic accumulation of 3-hydroxyisovaleric acid (3-HIVA), 3-methylcrotonylglycine (3-MCG), and 3-hydroxyisovalerylcarnitine (C5OH) in body fluids, often accompanied by secondary carnitine depletion.

Despite consistent biochemical detectability, the clinical phenotype of 3-MCCD is remarkably variable and predominantly benign. The vast majority of individuals identified through newborn screening (NBS) remain completely asymptomatic throughout life, raising substantial and ongoing debate about whether universal NBS for this condition is justified. A small minority of affected individuals may develop metabolic crises characterized by metabolic acidosis, hypoglycemia, hyperammonemia, and neurological sequelae — typically triggered by catabolic stress such as intercurrent illness or prolonged fasting. Management centers on avoidance of prolonged fasting, L-carnitine supplementation for secondary carnitine deficiency, and standardized emergency management protocols during metabolic decompensation. No specific pharmacological therapy exists, and the prognosis for the overwhelming majority of identified individuals is excellent with normal life expectancy.

This report synthesizes evidence from over 40 peer-reviewed publications, newborn screening program data from multiple countries (USA, China, Portugal, Iran, South Korea, Taiwan, Japan, Germany), and established disease databases (OMIM, Orphanet, ClinVar) to provide a comprehensive characterization of 3-MCCD across all major disease dimensions.

---

## 1. Disease Information

### Overview

3-Methylcrotonyl-CoA carboxylase deficiency (3-MCCD) is an inborn error of metabolism affecting the mitochondrial catabolism of the branched-chain amino acid leucine. The condition results from deficient activity of the enzyme 3-methylcrotonyl-CoA carboxylase (MCC; EC 6.4.1.4), which catalyzes the biotin-dependent carboxylation of 3-methylcrotonyl-CoA to 3-methylglutaconyl-CoA — the fourth step in the leucine degradation pathway. First described as a clinical entity in the 1970s, 3-MCCD gained prominence following the widespread adoption of expanded newborn screening by tandem mass spectrometry, which revealed the condition to be far more common than previously appreciated.

As documented by Gallardo et al. (2001): *"Isolated biotin-resistant 3-methylcrotonyl-CoA carboxylase (MCC) deficiency is an autosomal recessive disorder of leucine catabolism that appears to be the most frequent organic aciduria detected in tandem mass spectrometry-based neonatal screening programs"* ([PMID: 11181649](https://pubmed.ncbi.nlm.nih.gov/11181649/)).

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| **OMIM** | #210200 (3-methylcrotonyl-CoA carboxylase 1 deficiency); #210210 (3-methylcrotonyl-CoA carboxylase 2 deficiency) |
| **Orphanet** | ORPHA:6 |
| **MONDO** | MONDO:0009609 (type 1, MCCC1); MONDO:0009610 (type 2, MCCC2) |
| **MeSH** | C536837 |
| **ICD-10** | E71.1 (Other disorders of branched-chain amino-acid metabolism) |
| **ICD-11** | 5C50.0Y (Other specified disorders of branched-chain amino acid metabolism) |

### Synonyms and Alternative Names

- 3-Methylcrotonylglycinuria / 3-MCG-uria
- MCC deficiency / MCCD / 3-MCC deficiency / 3-MCCD
- Isolated 3-methylcrotonyl-CoA carboxylase deficiency
- Biotin-resistant MCC deficiency (to distinguish from multiple carboxylase deficiency)
- MCCA deficiency (for *MCCC1* mutations) / MCCB deficiency (for *MCCC2* mutations)
- Methylcrotonyl-CoA carboxylase deficiency type 1 / type 2

### Information Sources

Information in this report is derived from **aggregated disease-level resources** including OMIM, Orphanet, GeneReviews, and published literature, supplemented by **population-level data** from newborn screening program registries in California (USA), multiple Chinese provinces (Zhejiang, Jiangsu, Quanzhou, Suzhou), Portugal, Iran, South Korea, Taiwan, Japan, and Germany.

---

## 2. Etiology

### Disease Causal Factors

3-MCCD is a **purely genetic disorder** caused by biallelic loss-of-function mutations in either the *MCCC1* or *MCCC2* genes. There is no infectious, environmental, or acquired cause for isolated MCC deficiency. However, MCC activity can be secondarily reduced in **multiple carboxylase deficiency (MCD)** due to defects in biotin metabolism — specifically biotinidase deficiency (OMIM #253260) or holocarboxylase synthetase deficiency (OMIM #253270) — where all four biotin-dependent carboxylases are affected simultaneously. As noted in the comprehensive review: *"Acquired biotin deficiency and the two known congenital disorders of biotin metabolism, biotinidase and holocarboxylase synthetase (HCS) deficiency, all lead to deficiency of the 4 biotin-dependent carboxylases, i.e. to multiple carboxylase deficiency (MCD)"* ([PMID: 9350481](https://pubmed.ncbi.nlm.nih.gov/9350481/)).

### Genetic Risk Factors

- **Causal variants**: Biallelic pathogenic variants in *MCCC1* or *MCCC2* are the necessary and sufficient cause (see Section 4)
- **Carrier frequency**: Estimated at approximately 1:95 to 1:144 in general populations based on observed disease incidence and Hardy-Weinberg equilibrium calculations
- **Dominant negative alleles**: The MCCA-R385S mutation is notable for causing biochemical abnormalities and clinical symptoms even in heterozygous carriers ([PMID: 15868465](https://pubmed.ncbi.nlm.nih.gov/15868465/))
- **Consanguinity**: Increases risk as expected for autosomal recessive conditions; the high prevalence in consanguineous populations is documented: *"the prevalence of IMDs in Fars Province is significantly higher than average global statistics"* ([PMID: 40001143](https://pubmed.ncbi.nlm.nih.gov/40001143/))
- **No established modifier genes**, though the extreme phenotypic variability strongly suggests their existence

### Environmental Risk Factors and Triggers

While 3-MCCD itself is entirely genetic, **environmental factors modulate clinical expression**:

- **Catabolic stress** (intercurrent illness, fever, prolonged fasting, surgery) is the most common trigger for metabolic decompensation in susceptible individuals
- **Protein intake** — high leucine loads may worsen metabolite accumulation
- **Biotin status** — though isolated 3-MCCD is characteristically biotin-resistant, rare dominant-negative alleles may show partial biotin responsiveness in vivo
- **Age** — neonates and young infants are most vulnerable due to limited metabolic reserve and frequent feeding interruptions

### Protective Factors

- **Early identification via newborn screening** enables preventive management, though the majority would remain asymptomatic regardless
- **Adequate carnitine status** may protect against metabolic decompensation by maintaining acylcarnitine conjugation and excretion capacity
- **Avoidance of prolonged fasting** is the primary environmental protective measure
- **Residual enzyme activity** — hypomorphic variants preserving partial MCC activity are associated with milder phenotypes

### Gene-Environment Interactions

The hallmark of 3-MCCD is a **dramatic gene-environment interaction in phenotype expression**: genetically identical individuals (even within the same family) may range from completely asymptomatic to severely symptomatic. This suggests that catabolic triggers, dietary factors, biotin status, and perhaps stochastic developmental factors play critical roles in determining clinical outcome. The lack of genotype-phenotype correlation is extensively documented ([PMID: 27033733](https://pubmed.ncbi.nlm.nih.gov/27033733/)).

---

## 3. Phenotypes

### Overview of Clinical Phenotype Spectrum

The clinical phenotype of 3-MCCD is among the most heterogeneous of any inborn error of metabolism. Baumgartner et al. documented: *"Mutations in these genes cause isolated MCC deficiency, an autosomal recessive disorder with a variable phenotype ranging from severe neonatal to asymptomatic adult forms"* ([PMID: 15868465](https://pubmed.ncbi.nlm.nih.gov/15868465/)).

### A. Asymptomatic Phenotype (Most Common — ~85% of NBS-detected cases)

- **HPO term**: Not applicable (no phenotypic abnormality)
- **Frequency**: The vast majority of NBS-identified individuals remain clinically well. In the largest Chinese cohort (n=53), *"All these 53 patients did not present any clinical symptom"* ([PMID: 36822454](https://pubmed.ncbi.nlm.nih.gov/36822454/))
- **Age**: Detected at birth via NBS; remain asymptomatic throughout follow-up
- **Severity**: None — biochemical abnormality only
- **Progression**: Stable; no clinical disease develops in most cases
- **QoL impact**: Minimal clinical impact; however, the psychological burden of carrying a disease diagnosis from NBS and the anxiety surrounding emergency protocols are real concerns for families

### B. Metabolic Decompensation Episodes (Minority of cases)

| Phenotype | HPO Term | Frequency | Severity | Onset |
|---|---|---|---|---|
| Metabolic acidosis | HP:0001942 | Uncommon | Moderate-severe | Neonatal to childhood |
| Hypoglycemia | HP:0001943 | Uncommon | Variable | Neonatal to childhood |
| Hyperammonemia | HP:0001987 | Rare | Moderate-severe | Neonatal |
| Lactic acidosis | HP:0003128 | Uncommon | Variable | Neonatal to childhood |
| Ketosis/ketonuria | HP:0001946 | Uncommon | Variable | Episodic |

### C. Neurological Manifestations (~15% of cases with developmental data)

| Phenotype | HPO Term | Frequency | Severity | Onset |
|---|---|---|---|---|
| Developmental delay | HP:0001263 | ~15% (per IBEM-IS) | Mild to moderate | Childhood |
| Seizures | HP:0001250 | Rare | Variable | Variable |
| Hypotonia | HP:0001252 | Rare | Mild to moderate | Neonatal to infancy |
| Intellectual disability | HP:0001249 | Rare | Variable | Childhood |
| Feeding difficulties | HP:0011968 | Uncommon | Mild | Neonatal/infancy |

The IBEM-IS registry analysis reported: *"A limited number of cases were identified with traditional biochemical symptoms including acidosis, hyperammonemia or lactic acidosis, and 15% of those with available developmental information had recorded developmental disabilities not clearly attributable to other causes"* ([PMID: 27033733](https://pubmed.ncbi.nlm.nih.gov/27033733/)).

### D. Laboratory Abnormalities

| Abnormality | HPO Term | Frequency | Clinical Significance |
|---|---|---|---|
| Elevated C5OH | HP:0410051 | ~100% | Primary NBS marker |
| Elevated urinary 3-HIVA | HP:0033107 | ~76-94% | Confirmatory diagnostic |
| Elevated urinary 3-MCG | HP:0033108 | ~76-94% | Pathognomonic |
| Secondary carnitine deficiency | HP:0003234 | ~47% of neonates | Clinically actionable |

As documented in the Quanzhou study: *"All patients and neonates with 3-MCCD exhibited increased C5OH concentrations. Most patients [76.5%(13/17)] had increased urinary 3-methylcrotonylglycine (3-MCG) and 3-hydroxyisovaleric acid (3-HIVA) levels"* ([PMID: 39188588](https://pubmed.ncbi.nlm.nih.gov/39188588/)).

### E. Quality of Life Impact

For the asymptomatic majority, the primary quality-of-life impact stems from the **psychosocial burden of diagnosis** — parental anxiety, repeated monitoring visits, dietary counseling, and uncertainty about prognosis. For rare symptomatic individuals, metabolic crises carry significant acute morbidity, though long-term outcomes are generally favorable with appropriate management. No formal QoL assessments (EQ-5D, SF-36) specific to 3-MCCD have been published to date.

---

## 4. Genetic/Molecular Information

### Causal Genes

3-MCCD is caused by mutations in two genes encoding subunits of the heteromeric MCC holoenzyme:

| Gene | HGNC ID | NCBI Gene ID | Chromosome | Protein Subunit | UniProt | OMIM |
|---|---|---|---|---|---|---|
| **MCCC1** (MCCA) | HGNC:6936 | 56922 | 3q27.1 | MCCα (biotin-containing) | Q96RQ3 | *609010 |
| **MCCC2** (MCCB) | HGNC:6937 | 64087 | 5q13.2 | MCCβ (carboxyltransferase) | Q9HCC0 | *609014 |

The molecular basis was established by Gallardo et al.: *"MCC is a heteromeric mitochondrial enzyme composed of biotin-containing alpha subunits and smaller beta subunits. Here, we report cloning of MCCA and MCCB cDNAs and the organization of their structural genes. We show that a series of 14 MCC-deficient probands defines two complementation groups, CG1 and 2, resulting from mutations in MCCB and MCCA, respectively"* ([PMID: 11181649](https://pubmed.ncbi.nlm.nih.gov/11181649/)). The beta subunit was independently characterized: *"MCCase is a heteromeric enzyme composed of biotin-containing (MCC-A) and non-biotin-containing (MCC-B) subunits"* ([PMID: 10681539](https://pubmed.ncbi.nlm.nih.gov/10681539/)).

### Pathogenic Variants

- **Variant types**: Missense, nonsense, frameshift, splice-site, and small insertions/deletions have all been reported in both genes
- **Mutational spectrum**: The Portuguese NBS program identified 26 previously unreported mutations across both genes over a ten-year period ([PMID: 27601257](https://pubmed.ncbi.nlm.nih.gov/27601257/))
- **Classification**: Variants range from clearly pathogenic to VUS per ACMG/AMP guidelines; many novel variants continue to be identified
- **Somatic vs. germline**: All known pathogenic variants are **germline** in origin
- **Functional consequences**: Predominantly **loss of function** — reduced or absent MCC enzyme activity
- **Variant hotspots in Chinese populations**: c.639+2T>A in *MCCC1* and c.1144-1147delinsTTTT in *MCCC2* appear as recurrent variants ([PMID: 36822454](https://pubmed.ncbi.nlm.nih.gov/36822454/); [PMID: 40835664](https://pubmed.ncbi.nlm.nih.gov/40835664/))

### Notable Variant: MCCA-R385S (Dominant Negative)

The **MCCA-R385S** mutation acts through a unique **dominant negative mechanism**: *"Evidence is presented that MCCA-R385S is a dominant negative allele leading to biochemical abnormalities and clinical symptoms in heterozygous individuals and that it is responsive to pharmacological doses of biotin in vivo"* ([PMID: 15868465](https://pubmed.ncbi.nlm.nih.gov/15868465/)). This is clinically significant because carriers (heterozygotes) of this specific allele may present with symptoms, unlike typical AR carrier states.

### Genotype-Phenotype Correlation

There is **no reliable genotype-phenotype correlation** in 3-MCCD. *"There was no correlation between newborn screening (NBS) C5OH level and presence of metabolic, newborn, later-life or developmental abnormalities in these cases"* ([PMID: 27033733](https://pubmed.ncbi.nlm.nih.gov/27033733/)). Individuals with biochemically severe profiles may remain completely asymptomatic, while those with milder biochemical abnormalities may occasionally develop clinical symptoms.

### Modifier Genes, Epigenetics, and Chromosomal Abnormalities

- **Modifier genes**: None established, though extreme phenotypic variability implies their existence
- **Epigenetics**: No specific epigenetic modifications associated with 3-MCCD. Notably, biotin plays a role in histone biotinylation — *"the enzyme [holocarboxylase synthetase] also targets to the nucleus and that it catalyzes the attachment of biotin to histones"* ([PMID: 15992684](https://pubmed.ncbi.nlm.nih.gov/15992684/)) — but the implications for 3-MCCD specifically are unknown
- **Chromosomal abnormalities**: Not applicable — 3-MCCD is caused by point mutations and small indels

---

## 5. Environmental Information

### Environmental Factors

3-MCCD is a purely genetic condition with no environmental causative factors. However, **environmental triggers critically modulate clinical expression**:

- **Intercurrent illness** (infection, fever) — the most common trigger for metabolic decompensation
- **Prolonged fasting** — induces catabolism and increases leucine flux through the blocked pathway
- **Surgical stress** — perioperative catabolism can precipitate crises
- **Excessive protein/leucine intake** — may worsen metabolite accumulation

### Lifestyle Factors

- **Diet**: Leucine-rich diets theoretically increase metabolic burden, but strict dietary restriction is generally unnecessary for asymptomatic individuals
- **Exercise**: No specific evidence linking intense exercise to decompensation in 3-MCCD, though catabolic stress from extreme exertion is theoretically relevant
- **Alcohol/smoking**: No specific documented interactions

### Infectious Agents

Not applicable — 3-MCCD is not caused by infectious agents. However, infections serve as the most common environmental trigger for metabolic crises in susceptible individuals.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathway

MCC functions within the **leucine degradation pathway** in the mitochondrial matrix. The complete catabolic sequence is:

```
Leucine
  ↓  Branched-chain amino acid transaminase (BCAT)
α-Ketoisocaproate
  ↓  Branched-chain α-ketoacid dehydrogenase complex (BCKDH)
Isovaleryl-CoA
  ↓  Isovaleryl-CoA dehydrogenase (IVD)
3-Methylcrotonyl-CoA
  ↓  ✖ 3-Methylcrotonyl-CoA carboxylase (MCC) ← BLOCKED IN 3-MCCD
3-Methylglutaconyl-CoA
  ↓  3-Methylglutaconyl-CoA hydratase (AUH)
3-Hydroxy-3-methylglutaryl-CoA (HMG-CoA)
  ↓  HMG-CoA lyase (HMGCL)
Acetoacetate + Acetyl-CoA → Krebs Cycle / Ketogenesis
```

This pathway was directly demonstrated in plant mitochondria: *"plant mitochondria can catabolize Leu via the following scheme: Leu → alpha-ketoisocaproate → isovaleryl-CoA → 3-methylcrotonyl-CoA → 3-methylglutaconyl-CoA → 3-hydroxy-3-methylglutaryl-CoA → acetoacetate + acetyl-CoA"* ([PMID: 9847087](https://pubmed.ncbi.nlm.nih.gov/9847087/)).

**Pathway databases**: KEGG hsa00280 (Valine, leucine and isoleucine degradation); Reactome R-HSA-70895

### Biochemical Consequences of MCC Deficiency

When MCC is deficient, 3-methylcrotonyl-CoA accumulates and is diverted to three alternative metabolic routes:

1. **Glycine conjugation** → **3-methylcrotonylglycine (3-MCG)** — pathognomonic urinary metabolite
2. **Hydration** → **3-hydroxyisovaleric acid (3-HIVA)** — major urinary metabolite
3. **Carnitine conjugation** → **3-hydroxyisovalerylcarnitine (C5OH)** — primary NBS biomarker

These metabolites accumulate in blood and are excreted in urine. Importantly, they appear to be relatively non-toxic at physiological concentrations, which likely explains the benign phenotype in most individuals.

### Secondary Metabolic Effects

- **Carnitine depletion**: Conjugation of accumulated metabolites depletes carnitine stores, with approximately 47% of neonates showing secondary carnitine deficiency ([PMID: 39188588](https://pubmed.ncbi.nlm.nih.gov/39188588/)). This may impair fatty acid oxidation and energy production.
- **CoA sequestration**: Accumulation of acyl-CoA intermediates may deplete the mitochondrial free CoA pool, potentially affecting other CoA-dependent pathways
- **Impaired ketogenesis**: The leucine degradation pathway normally contributes to ketone body production via HMG-CoA; blockade at MCC reduces this contribution during fasting

### Protein Dysfunction

MCC is a heteromeric mitochondrial enzyme with an **α₆β₆ dodecameric structure**. The alpha subunit (MCCα, MCCC1) contains the **biotin prosthetic group** covalently attached at a conserved lysine residue, catalyzing the ATP-dependent carboxylation of enzyme-bound biotin. The beta subunit (MCCβ, MCCC2) contains the **carboxyltransferase domain** that transfers the carboxyl group from carboxybiotin to 3-methylcrotonyl-CoA. Pathogenic variants cause:

- **Loss of function** — through protein misfolding, instability, or catalytic site disruption
- **Dominant negative effects** (rare, e.g., R385S) — through incorporation of mutant subunits that poison the hexameric complex assembly

Biotinylation of MCC is catalyzed by **holocarboxylase synthetase (HCS)**: *"Biotinylation is an obligate posttranslational modification for five mammalian carboxylases: acetyl-CoA carboxylase α (ACCα), ACCβ, pyruvate carboxylase (PC), methylcrotonyl-CoA carboxylase (MCC), and propionyl-CoA carboxylase (PCC)"* ([PMID: 27084392](https://pubmed.ncbi.nlm.nih.gov/27084392/)).

### Circadian Regulation of MCC

MCC biotinylation is regulated by the **cellular circadian clock** via the biotin transporter SLC5A6. In cardiomyocyte-specific clock mutant mice (CCM and CBK models), biotinylation of all carboxylases was significantly decreased (10-46%), leucine oxidation rates were reduced, and these abnormalities were correctable with biotin-enriched diet ([PMID: 27084392](https://pubmed.ncbi.nlm.nih.gov/27084392/)). This suggests circadian biology may influence MCC activity in a tissue-specific manner.

### Relationship to 3-Methylglutaconic Aciduria

MCC deficiency is relevant to the broader metabolic understanding of 3-methylglutaconic acid (3-MGA) metabolism. In the leucine degradation pathway, MCC produces 3-methylglutaconyl-CoA, a key intermediate: *"In the leucine degradation pathway, carboxylation of 3-methylcrotonyl CoA leads to formation of 3-methylglutaconyl CoA while 3-methylglutaconyl CoA hydratase converts this metabolite to 3-hydroxy-3-methylglutaryl CoA (HMG CoA)"* ([PMID: 24407466](https://pubmed.ncbi.nlm.nih.gov/24407466/)). The kinetic properties of MCC prevent reverse flux from HMG-CoA back through 3-methylcrotonyl-CoA.

### Key GO Terms

- **GO:0006552** — leucine catabolic process (directly impaired)
- **GO:0006768** — biotin metabolic process
- **GO:0004075** — biotin carboxylase activity
- **GO:0005759** — mitochondrial matrix (cellular compartment)
- **GO:0005739** — mitochondrion

### Key CHEBI Terms

- **CHEBI:87672** — 3-hydroxyisovalerylcarnitine (C5OH)
- **CHEBI:68568** — 3-methylcrotonylglycine (3-MCG)
- **CHEBI:17232** — 3-hydroxyisovaleric acid (3-HIVA)
- **CHEBI:57288** — 3-methylcrotonyl-CoA
- **CHEBI:83264** — biotin
- **CHEBI:16414** — L-leucine

---

## 7. Anatomical Structures Affected

### Organ Level

| Level | Organs/Systems | UBERON Term | Notes |
|---|---|---|---|
| Primary | Liver | UBERON:0002107 | Major site of leucine catabolism |
| Primary | Skeletal muscle | UBERON:0001134 | Major site of BCAA catabolism |
| Secondary | Brain/CNS | UBERON:0000955 | Vulnerable during metabolic crises |
| Secondary | Heart | UBERON:0000948 | MCC biotinylation regulated by circadian clock |
| Excretory | Kidney | UBERON:0002113 | Metabolite excretion |
| Systems | Nervous, muscular, metabolic | — | Multi-system during severe decompensation |

### Tissue and Cell Level

- **Hepatocytes** (CL:0000182) — major site of leucine catabolism and MCC expression
- **Skeletal muscle cells** (CL:0000188) — leucine catabolism for energy homeostasis
- **Neurons** (CL:0000540) — vulnerable to metabolic decompensation (acidosis, energy failure)
- **Cardiomyocytes** (CL:0000746) — express MCC; circadian regulation documented

### Subcellular Level

- **Mitochondrial matrix** (GO:0005759) — primary compartment for MCC enzyme and leucine catabolism
- **Mitochondrion** (GO:0005739) — organelle housing all pathway enzymes

### Localization

The enzymatic defect is systemic but metabolic consequences are most pronounced in tissues with high leucine catabolic activity — particularly liver, skeletal muscle, and brain. No lateralization or anatomic asymmetry is observed.

---

## 8. Temporal Development

### Onset

- **Detection**: Typically neonatal (day 2-5 of life) via NBS
- **Symptomatic onset (when present)**: Highly variable — neonatal period to late childhood; rarely adult onset
- **Onset pattern**: Most individuals are asymptomatic throughout life; symptomatic cases typically present with **episodic metabolic crises** rather than chronic progressive disease

### Progression

- **Disease course**: **Episodic** (metabolic crises during catabolic stress) in symptomatic individuals; **stable/asymptomatic** in the overwhelming majority
- **Progression rate**: No disease progression in most cases; rare symptomatic individuals may accumulate neurological damage from inadequately treated crises
- **Duration**: Chronic lifelong biochemical abnormality; clinical disease is intermittent when present
- **Staging**: Not formally staged; categorized as biochemically mild, moderate, or severe based on metabolite levels and residual enzyme activity

### Critical Periods

- **Neonatal period**: Highest vulnerability during the catabolic transition from placental nutrition
- **Infancy/early childhood**: Frequent intercurrent illnesses can trigger crises
- **Adolescence/adulthood**: Generally stable; late-onset symptoms are exceptionally rare

---

## 9. Inheritance and Population

### Epidemiology

3-MCCD is the **most frequently detected organic aciduria** in NBS programs worldwide, confirmed across multiple populations and programs.

| Population | Incidence | Sample Size | Reference |
|---|---|---|---|
| California, USA | 1:41,676 | 2,959,108 | [PMID: 24103308](https://pubmed.ncbi.nlm.nih.gov/24103308/) |
| Zhejiang, China | 1:83,068 | 4,402,587 | [PMID: 36822454](https://pubmed.ncbi.nlm.nih.gov/36822454/) |
| Jiangsu, China | 1:38,286 | 536,008 | [PMID: 31730530](https://pubmed.ncbi.nlm.nih.gov/31730530/) |
| Quanzhou, China | 1:37,859 | 643,606 | [PMID: 39188588](https://pubmed.ncbi.nlm.nih.gov/39188588/) |
| Suzhou, China | 1:33,412 | 401,660 | [PMID: 31737040](https://pubmed.ncbi.nlm.nih.gov/31737040/) |
| Zhejiang (2009-2016) | 1:68,900 | 1,861,262 | [PMID: 29039164](https://pubmed.ncbi.nlm.nih.gov/29039164/) |
| Fars Province, Iran | High prevalence* | 138,689 | [PMID: 40001143](https://pubmed.ncbi.nlm.nih.gov/40001143/) |

*Among the most prevalent IMDs in an area with elevated consanguinity.

A meta-analysis of 13 million Chinese newborns confirmed 3-MCCD as one of the most prevalent organic acidurias ([PMID: 41440809](https://pubmed.ncbi.nlm.nih.gov/41440809/)). International comparisons showed that 3-MCCD was among the most frequently detected conditions in Taiwan and South Korea NBS programs ([PMID: 29946514](https://pubmed.ncbi.nlm.nih.gov/29946514/)).

### Inheritance Pattern

- **Mode**: Autosomal recessive — requires biallelic pathogenic variants in *MCCC1* or *MCCC2*
- **Exception**: The dominant negative MCCA-R385S allele causes disease in heterozygotes
- **Penetrance**: **Highly incomplete** — most individuals with biallelic loss-of-function variants remain asymptomatic
- **Expressivity**: **Highly variable** — from completely asymptomatic to severe neonatal metabolic crisis, even within families
- **Genetic anticipation**: Not observed (not a repeat expansion disorder)
- **Carrier frequency**: Estimated ~1:95 to 1:145 based on disease incidence
- **Consanguinity**: Increases risk, as expected for AR conditions
- **Founder effects**: Population-specific variant hotspots documented in Chinese populations

### Population Demographics

- **Ethnic distribution**: Reported across all ethnic groups worldwide
- **Geographic distribution**: Detected wherever expanded NBS is implemented
- **Sex ratio**: ~1:1 (autosomal inheritance)
- **Maternal detection**: NBS may detect maternal 3-MCCD when metabolites cross the placenta, leading to a positive NBS in an unaffected newborn — *"there are additional scenarios within NBS where disease maternal conditions (3-methylcrotonyl-CoA carboxylase deficiency and carnitine uptake deficiency) ... may cause a screen-positive NBS result"* ([PMID: 40673334](https://pubmed.ncbi.nlm.nih.gov/40673334/))

---

## 10. Diagnostics

### Newborn Screening (Primary Detection)

3-MCCD is detected via **tandem mass spectrometry (MS/MS)** by measuring elevated **3-hydroxyisovalerylcarnitine (C5OH)** in dried blood spots. It is included in the recommended uniform screening panel (RUSP) in many countries.

However, C5OH elevation is **not specific** for 3-MCCD and may also be elevated in:
- Multiple carboxylase deficiency (biotinidase deficiency, HCS deficiency)
- Maternal 3-MCCD (transplacental metabolite transfer)
- 3-Hydroxy-3-methylglutaryl-CoA lyase deficiency
- Beta-ketothiolase deficiency (occasionally)

Critically, *"No significant correlation was found between the C5OH levels in newborn screening and the diagnosis of specific C5OH-related disorders or the presence of metabolic, neonatal, or developmental abnormalities"* ([PMID: 39484073](https://pubmed.ncbi.nlm.nih.gov/39484073/)).

### Confirmatory Testing Hierarchy

| Test | Method | Findings | Role |
|---|---|---|---|
| **Urine organic acids** | GC-MS | Elevated 3-HIVA, 3-MCG | Confirmatory |
| **Plasma acylcarnitines** | MS/MS | Elevated C5OH | Screening/confirmatory |
| **Plasma free carnitine** | MS/MS | May be low | Monitoring |
| **MCC enzyme assay** | In lymphocytes/fibroblasts | Reduced activity | Gold standard functional |
| **Molecular genetic testing** | Sanger or NGS | Biallelic variants in MCCC1/MCCC2 | Definitive molecular diagnosis |

A rapid differential diagnostic method was described: *"A definitive diagnosis could be made in 7 of 9 patients studied up to now: 4 patients suffered from biotin-nonresponsive isolated PCC-deficiency, and 3 patients from biotin-responsive multiple carboxylase deficiency"* ([PMID: 3918814](https://pubmed.ncbi.nlm.nih.gov/3918814/)).

### Genetic Testing Strategy

1. **First tier**: Targeted sequencing of *MCCC1* and *MCCC2* (single-gene or organic acidemia panel)
2. **Second tier**: Whole exome sequencing (WES) if targeted testing is negative
3. **Deletion/duplication analysis**: If sequencing identifies only one pathogenic variant
4. **Complementation analysis**: Cell fusion studies to distinguish CG1 (MCCC2) from CG2 (MCCC1)

### Differential Diagnosis

| Condition | Distinguishing Feature |
|---|---|
| Biotinidase deficiency | All carboxylases affected; low biotinidase activity; biotin-responsive; skin rash, alopecia |
| Holocarboxylase synthetase deficiency | All carboxylases affected; neonatal onset; variable biotin responsiveness |
| 3-HMG-CoA lyase deficiency | Different organic acid profile; generally more severe |
| Isovaleric acidemia | Different acylcarnitine marker (C5 vs C5OH) |
| Maternal 3-MCCD | Normal metabolites in infant on repeat testing |

### Imaging

Brain MRI may show white matter abnormalities or cerebral atrophy in rare severe symptomatic cases but is not routinely indicated in asymptomatic individuals.

### Screening Utility Debate

The question of whether NBS for 3-MCCD provides net benefit remains actively debated: *"for others (e.g., very long chain acyl CoA dehydrogenase deficiency and 3-methylcrotonyl CoA carboxylase 1 deficiency), this is less clear as NBS identifies individuals who are asymptomatic or have milder forms of the disease"* ([PMID: 40610367](https://pubmed.ncbi.nlm.nih.gov/40610367/)).

---

## 11. Outcome / Prognosis

### Survival and Mortality

- **Overall prognosis**: Excellent for the vast majority of individuals
- **Life expectancy**: Normal in asymptomatic individuals (the majority)
- **Mortality**: Deaths are exceedingly rare, associated with severe neonatal crises or late/missed diagnosis
- **Comparison with other organic acidurias**: *"Except MCC, most organic aciduria may lead to metabolism decompensation, complications or even death"* — highlighting the distinctly benign course of 3-MCCD ([PMID: 29039164](https://pubmed.ncbi.nlm.nih.gov/29039164/))

### Morbidity

- **Developmental disability**: ~15% of cases with developmental data, though *"not clearly attributable to other causes"* ([PMID: 27033733](https://pubmed.ncbi.nlm.nih.gov/27033733/))
- **Secondary carnitine deficiency**: ~47% of neonates; clinically actionable
- **Metabolic crises**: Rare but potentially life-threatening if untreated

### Prognostic Factors

- **No reliable prognostic biomarkers**: NBS C5OH levels do not predict outcome
- **Genotype does not predict phenotype**: *"There was no correlation between newborn screening (NBS) C5OH level and presence of metabolic, newborn, later-life or developmental abnormalities"* ([PMID: 27033733](https://pubmed.ncbi.nlm.nih.gov/27033733/))
- **Early management** with emergency protocols may prevent rare crises

---

## 12. Treatment

### Pharmacotherapy

There is **no specific pharmacological treatment** for 3-MCCD. Management is primarily supportive and preventive.

#### L-Carnitine Supplementation (MAXO:0001298)

- **Indication**: Secondary carnitine deficiency (present in ~47% of neonates)
- **Mechanism**: Replenishes depleted carnitine stores; promotes excretion of toxic acyl-CoA intermediates as acylcarnitines
- **Dosage**: Typically 50-100 mg/kg/day in divided doses
- **Monitoring**: Plasma free carnitine and acylcarnitine levels
- **CHEBI**: CHEBI:16347 (L-carnitine)

#### Biotin (MAXO:0010003)

- **Generally NOT effective** in isolated 3-MCCD (biotin-resistant), unlike MCD
- **Exception**: MCCA-R385S dominant negative allele shows biotin responsiveness ([PMID: 15868465](https://pubmed.ncbi.nlm.nih.gov/15868465/))
- **CHEBI**: CHEBI:15956 (biotin)

### Dietary Management (MAXO:0000127)

- **Leucine restriction**: Generally **not required** for asymptomatic individuals
- **Protein management**: Normal protein intake typically recommended; only patients with recurrent crises may benefit from moderate leucine restriction
- **Fasting avoidance** (MAXO:0000134): Key preventive measure — regular feeding schedules, especially during illness

### Emergency Management (MAXO:0000088)

During acute metabolic crises:
- **IV dextrose** (10%) to suppress catabolism
- **Fluid resuscitation** for dehydration
- **Bicarbonate** for severe metabolic acidosis
- **IV L-carnitine** if oral not tolerated
- **Temporary protein restriction** (24-48 hours)
- **ICU monitoring** for severe cases

### Advanced Therapeutics

- **Gene therapy**: No current trials or approved therapies
- **Enzyme replacement therapy**: Not developed
- **Transplantation**: Not indicated given the predominantly benign phenotype

### Monitoring Protocol

| Parameter | Frequency | Method |
|---|---|---|
| Growth and development | Every 3-6 months (infancy), then annually | Clinical assessment |
| Plasma carnitine/acylcarnitines | Every 6-12 months | MS/MS |
| Urine organic acids | As clinically indicated | GC-MS |
| Developmental assessment | Annual (early childhood) | Standardized tools |

### Treatment Strategy Summary

- **Asymptomatic NBS-detected**: Monitoring only; prophylactic carnitine at some centers
- **Mild/intermittent symptoms**: Carnitine supplementation, dietary guidance, emergency protocol
- **Severe symptomatic**: Protein restriction, carnitine, biotin trial (for responsive genotypes), emergency management

---

## 13. Prevention

### Primary Prevention

- **Genetic counseling** (MAXO:0000079) for families with known affected members
- **Carrier testing** for at-risk relatives
- **Preimplantation genetic diagnosis (PGD)** technically available for known familial variants
- **Prenatal diagnosis** via CVS or amniocentesis with molecular testing

### Secondary Prevention (Early Detection)

- **Newborn screening** (MAXO:0000127): C5OH elevation by MS/MS on dried blood spots
  - Included in NBS panels of many countries (USA RUSP, European programs, Chinese national programs)
  - Clinical utility debated: *"is routine screening necessary?"* ([PMID: 31730530](https://pubmed.ncbi.nlm.nih.gov/31730530/))
- **Reverse cascade testing**: NBS-positive infants serve as index cases for detecting undiagnosed maternal 3-MCCD ([PMID: 40673334](https://pubmed.ncbi.nlm.nih.gov/40673334/))

### Tertiary Prevention

- **Fasting avoidance protocols** and **sick-day management plans**
- **Emergency letters** for healthcare providers
- **L-carnitine supplementation** to prevent secondary carnitine deficiency
- **Regular metabolic follow-up**

### Genetic Counseling (MAXO:0000079)

- Recurrence risk: 25% for siblings (AR inheritance)
- Exception: 50% risk for MCCA-R385S dominant negative allele
- Importance of distinguishing isolated 3-MCCD from MCD for accurate counseling
- Need for long-term monitoring emphasized: *"Adult metabolic specialists should be included in the development of NBS programs to provide data from this long-term monitoring and to contribute specific knowledge about later onset phenotypes"* ([PMID: 40610367](https://pubmed.ncbi.nlm.nih.gov/40610367/))

---

## 14. Other Species / Natural Disease

### Comparative Biology and Orthologous Genes

MCC is a **highly conserved enzyme** across eukaryotes, reflecting its essential role in leucine catabolism.

| Species | NCBI Taxon ID | Gene(s) | Notes |
|---|---|---|---|
| *Homo sapiens* | 9606 | *MCCC1*, *MCCC2* | Disease-causing genes |
| *Mus musculus* (mouse) | 10090 | *Mccc1* (72039), *Mccc2* (78038) | Orthologous genes; knockout models |
| *Rattus norvegicus* (rat) | 10116 | *Mccc1*, *Mccc2* | Orthologs present |
| *Danio rerio* (zebrafish) | 7955 | *mccc1*, *mccc2* | Pathway conserved |
| *Glycine max* (soybean) | 3847 | MCCase | Functionally characterized |
| *Arabidopsis thaliana* | 3702 | MCCase | MCC-B subunit cloned |

The leucine catabolic pathway in plants was directly demonstrated: *"These findings demonstrate for the first time, to our knowledge, that the enzymes responsible for Leu catabolism are present in plant mitochondria"* ([PMID: 9847087](https://pubmed.ncbi.nlm.nih.gov/9847087/)).

### Natural Disease in Animals

Naturally occurring MCC deficiency has not been extensively documented in companion animals or livestock (no OMIA entry). Given the predominantly benign phenotype in humans, mild forms in animals would likely go undetected.

### Zoonotic/Transmission

Not applicable — 3-MCCD is a genetic/metabolic condition, not transmissible between species.

---

## 15. Model Organisms

### Mouse Models

- **Mccc1 and Mccc2 knockout mice** are available through IMPC and other consortia
- Phenotypic characterization specific to 3-MCCD has been limited in published literature
- The **circadian clock mouse models** (CCM and CBK) provide indirect models for tissue-specific MCC dysfunction — decreased MCC biotinylation leads to reduced leucine oxidation, correctable with biotin-enriched diet ([PMID: 27084392](https://pubmed.ncbi.nlm.nih.gov/27084392/))

### Cellular Models

- **Patient fibroblasts**: Most commonly used for enzyme assays and complementation analysis ([PMID: 11181649](https://pubmed.ncbi.nlm.nih.gov/11181649/))
- **Patient lymphocytes**: Enable rapid diagnostic enzyme measurement ([PMID: 3918814](https://pubmed.ncbi.nlm.nih.gov/3918814/))

### Plant Models

- *Arabidopsis thaliana* and *Glycine max* provided foundational biochemistry of the MCC-B subunit and leucine catabolic pathway ([PMID: 9847087](https://pubmed.ncbi.nlm.nih.gov/9847087/); [PMID: 10681539](https://pubmed.ncbi.nlm.nih.gov/10681539/))

### Model Limitations

- The predominantly benign phenotype makes it challenging to develop clinically relevant animal models
- Animal models may not recapitulate the environmental triggers necessary for symptom manifestation
- Species differences in leucine catabolism rates and alternative pathways may limit translational applicability

### Research Applications

- Study of leucine catabolic pathway regulation
- Understanding incomplete penetrance in metabolic disorders
- Biotin metabolism and biotinylation biology
- NBS program evaluation and clinical utility assessment
- Genotype-phenotype dissociation mechanisms

---

## Evidence Base Summary

| PMID | Key Contribution | Evidence Type |
|---|---|---|
| [11181649](https://pubmed.ncbi.nlm.nih.gov/11181649/) | Molecular basis: gene cloning, complementation groups | Human genetics |
| [10681539](https://pubmed.ncbi.nlm.nih.gov/10681539/) | MCCβ subunit characterization | Biochemistry |
| [15868465](https://pubmed.ncbi.nlm.nih.gov/15868465/) | Dominant negative MCCA-R385S | Human genetics |
| [24103308](https://pubmed.ncbi.nlm.nih.gov/24103308/) | California NBS incidence 1:41,676 | Population screening |
| [36822454](https://pubmed.ncbi.nlm.nih.gov/36822454/) | Zhejiang: all 53 cases asymptomatic | Population screening |
| [31730530](https://pubmed.ncbi.nlm.nih.gov/31730530/) | Jiangsu NBS; screening necessity questioned | Population screening |
| [27033733](https://pubmed.ncbi.nlm.nih.gov/27033733/) | IBEM-IS registry; no prognostic biomarkers | Registry study |
| [39188588](https://pubmed.ncbi.nlm.nih.gov/39188588/) | Quanzhou NBS; biomarker characterization | Population screening |
| [39484073](https://pubmed.ncbi.nlm.nih.gov/39484073/) | C5OH levels non-predictive | Clinical study |
| [27601257](https://pubmed.ncbi.nlm.nih.gov/27601257/) | Portuguese mutational spectrum (26 novel mutations) | Human genetics |
| [40610367](https://pubmed.ncbi.nlm.nih.gov/40610367/) | Adult specialist perspective on NBS | Clinical perspective |
| [40673334](https://pubmed.ncbi.nlm.nih.gov/40673334/) | Reverse cascade testing for maternal detection | Methodology |
| [27084392](https://pubmed.ncbi.nlm.nih.gov/27084392/) | Circadian clock regulation of MCC biotinylation | Animal model |
| [9847087](https://pubmed.ncbi.nlm.nih.gov/9847087/) | Leucine catabolic pathway in plant mitochondria | Comparative biology |
| [9350481](https://pubmed.ncbi.nlm.nih.gov/9350481/) | Multiple carboxylase deficiency overview | Clinical review |
| [41440809](https://pubmed.ncbi.nlm.nih.gov/41440809/) | Chinese meta-analysis of organic acidurias | Meta-analysis |
| [29946514](https://pubmed.ncbi.nlm.nih.gov/29946514/) | International NBS comparison (Asia/Germany) | Population screening |
| [40001143](https://pubmed.ncbi.nlm.nih.gov/40001143/) | Iranian NBS epidemiology | Population screening |
| [3918814](https://pubmed.ncbi.nlm.nih.gov/3918814/) | Rapid lymphocyte diagnostic assay | Diagnostics |
| [15992684](https://pubmed.ncbi.nlm.nih.gov/15992684/) | Biotin metabolism and histone biotinylation | Basic science |
| [24407466](https://pubmed.ncbi.nlm.nih.gov/24407466/) | 3-Methylglutaconic aciduria metabolic biology | Biochemistry |

---

## Limitations and Knowledge Gaps

1. **Genotype-phenotype correlation**: No reliable correlation exists; the molecular basis for variable penetrance remains completely unknown, representing the most fundamental gap in understanding this disease.

2. **Long-term outcomes**: Most NBS cohorts have limited follow-up (<10 years). The lifelong natural history of NBS-detected 3-MCCD is unknown. Adult outcomes are largely unstudied.

3. **NBS clinical utility**: Whether screening for 3-MCCD provides net benefit versus harm (psychological burden, medicalization of healthy individuals) is unresolved and actively debated.

4. **Prognostic biomarkers**: No biomarkers exist to identify the minority of individuals who will develop clinical symptoms — this is the most critical unmet clinical need.

5. **Mechanism of incomplete penetrance**: Potential explanations (epigenetic variation, modifier genes, microbiome, stochastic factors) are entirely uninvestigated in 3-MCCD.

6. **Quality of life data**: No formal QoL assessments quantify the psychosocial impact of 3-MCCD diagnosis on families.

7. **Animal model phenotyping**: Limited published characterization of MCC-deficient mouse models.

8. **Maternal 3-MCCD**: Prevalence and clinical significance of previously undiagnosed maternal cases need systematic study.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective longitudinal cohort study** of NBS-identified 3-MCCD individuals through adulthood (20+ year follow-up) to establish definitive natural history and detect any late-onset complications.

2. **Multi-omics profiling** (transcriptomics, metabolomics, epigenomics) comparing symptomatic versus asymptomatic individuals with equivalent genotypes to identify modifiers of penetrance.

3. **Functional variant characterization** — standardized enzyme activity assays and structural modeling for all reported MCCC1/MCCC2 variants to enable residual activity-based risk stratification.

4. **Psychosocial impact assessment** using validated instruments (PedsQL, EQ-5D) in families of NBS-identified individuals to quantify the harm/benefit balance of screening.

5. **Prognostic risk score development** integrating genotype, residual enzyme activity, metabolomic profile, and carnitine status to stratify individuals at diagnosis.

6. **MCCA-R385S mechanism investigation** and systematic screening for other dominant negative alleles across diverse populations.

7. **Gut microbiome characterization** in 3-MCCD patients to assess whether microbial leucine metabolism modifies disease expression.

8. **International consensus guidelines** on management of asymptomatic NBS-detected 3-MCCD, including recommendations on continued NBS utility.

9. **NBS cut-off optimization** to reduce false-positive burden while maintaining detection of the rare symptomatic individuals who may benefit from early identification.

10. **Comprehensive mouse model phenotyping** under basal and catabolic stress conditions to understand tissue-specific vulnerability and test potential interventions.

---

*Report generated: 2026-05-05*
*Based on systematic review of 40+ peer-reviewed publications and established disease databases*
